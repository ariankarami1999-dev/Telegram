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
<img src="https://cdn4.telesco.pe/file/gfPRKWKhdEZ941-4Bot_YxMc9Ieum1kY164wcePbBaAyfrHStdqGS1rFIZRNP2mnxt7evizAG3OB0V8U8T3bwl4nKWjN_TQrS1DNAKu09R9Ny1EupijNpi4lKRY_qq55dAlhVgwP10FWyF74HxPXsoiX3sKG0qII9R_ZekNZQ6d4taoMhdh79zHFCiItVCHTMiiQ5_WTcjPRSmZFDowWYmgod1pj-VH8SrAZTkI6kTbvDrO27LT0iRQevySYZ3YalZKSiSHiVzuRd61cgAcMsODlGY0v_bMPiCIPonbtVCOI9wmJVyGeQJssGJIh2xcwheerXJlBo3_8XWOwMjxdRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.2M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 05:45:24</div>
<hr>

<div class="tg-post" id="msg-689382">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt0I6rX0Sj0MMbKQ7DHjLQSSk7L6X8oijnVfoyhOJA--NHB5P96s-CViRrHBWTered6guUc6Q4eJChIt1itB9_ntD7flcQNHtnRktzE_sO15TRiIVzVpAVMUPfwijzJqiuxzPmTEpdMUQmLuWPbmLnDDceh9wtjCakwFVmExM2moM7aBCE4HwAshqnSNKcTgvg5EffACUeNSzz7t6Inx2-NrMGxwL47pCRbitoPFUTXjgYvnxqrZoFcpWJQTDlN6BQ5vOJ8w_o2p3q5YcY8f0lt73Kc6T8IK3CJ99LUZan4OGhhZEKfK38C0apMHo5sofISnzDwfApIYkaW1GWsHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رویای تحصیل در خارج از کشور رو داری؟
🔻
قبولی دانشگاه، بورسیه و ویزای تحصیلی شاید پیچیده به نظر برسه؛ اما با انتخاب مسیر درست، می‌تونه خیلی ساده‌تر بشه.
🎓
🔘
در انتخاب همراهت هستیم برای:
✅
اخذ پذیرش از بهترین دانشگاه های خارج
✅
بورسیه‌های تحصیلی
✅
ویزای تحصیلی
✅
پذیرش در مقاطع کارشناسی، ارشد، رشته‌های پزشکی و دوره های زبان
✅
دوره جامع آمادگی آزمون پزشکی ایتالیا
🎯
نمی‌دونی از کجا شروع کنی؟
✉️
فرم درخواست مشاوره تخصصی رایگان رو تکمیل کن تا شرایطت رو بررسی کنیم.
🌐
فرم درخواست مشاوره:
https://ezam.entekhabafarin.com/consultant
⁠
یا با شماره های زیر با ما در ارتباط باش:
📞
۰۲۱۷۹۴۱۲
📞
۰۹۹۸۱۲۵۱۲۵۴
✅
@entekhabafarin
موسسه انتخاب | انتخاب درست، شروع یک آینده بهتر
🎓
✈️</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/689382" target="_blank">📅 00:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689381">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">راز بیورزونانس و فرکانس های زیستی که این روزها خبرش همه جاپیچیده وبیماران زیادی رابهبود بخشیده ،چیه؟
میگن تو دانشگاه امیرکبیر مثل کشورهای پیشرفته با یک سیستم تشخیص هوشمند، بیماری ها را تشخیص و بهبود می دهند.
🔹
اگرشما و نزدیکانتان هم بیماری دارید که کلی هزینه
کردید ونتیجه نگرفتید حتما باهاشون تماس بگیرید
👇🏻
☎️
: 02166961000
02166961005
02166404713
جهت دریافت نوبت مشاوره تخصصی با شماره زیر تماس بگیرید
👇🏻
📞
: 09912250295
کانال تلگرام کلینیک بیورزونانس دانشگاه امیرکبیر
👇🏻
https://t.me/bioresonanceclinic
کانال اینستاگرام کلینیک بیورزونانس دانشگاه امیرکبیر
👇🏻
https://www.instagram.com/clinic_bioresonance_amirkabir?igsh=MTVmNHd3eHM2YTFlZg==
کانال بله کلینیک بیورزونانس دانشگاه امیرکبیر
👇🏻
https://ble.ir/bioresonance_amirkabir</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/689381" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689380">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmacqKUeGuG89oGNGw5PSC-tiwYPe57hGvzZ12ruQfjq3gM625m_bQiLHL_RGwruAM8F_QMa5-_HuyA7DdrkOZChoRDk1ff_lesSuL5OFUzck-xkMrRkBDZU3jEBTMSiLFw8u-c2hHeIOqdlctuqhEA_DIWJc2ey1CJdcyPvfuFoQO29Cds12DK3MOnAmQILK1qhD0289bpSmFuXgCRlfcbGuyLk4gGiFDKwNbDWmH4itOXt3MhmqI82aD9gJ43wux0DDwlnh0FGDVXZ5X6IKVgv7qBMI8a5NdY825LN3bz8Hb_a1AaKntMXVlPyDZf5lkwUqV2adouOwv-PrnZizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👟
جردن شیک با قیمت 1,898,000 تومن!
🔥
اگه دنبال یه کفش اسپرت مردونه‌ای که هم
خوش‌استایل
باشه هم برای استفاده روزمره راحت، این مدل جردن Avin رو ببین
👌
✨
رویه زارا
✅
زیره PU سبک و مقاوم
👌
کفی دوردوزی‌شده برای دوام بیشتر
📏
سایزهای ۴۱ تا ۴۴
🏠
پرداخت درب منزل
🔄
ضمانت تعویض ۳ روزه
🛒
خرید از سایت:
https://memarket24.ir/product/brief/46467/180124/</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/689380" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689379">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luJTslT2wMfgd8xsdLr6UdPSN5RCi4g9cNwjNg7fwmyb484OlwZegaXLaTNNJAenYrtW3oS0IJe9rtLnHZuCsEWvKWamgAOKg0we-J5qDu5gi_DL6RKHTsHVyI0cBV01qCLl8ZtDcwCQHCY0MG5rQpVT5ps9_0CPwXpWSQ3_-BJg8_kLRyIo_f1Wp0xUSqgkNeux6ny9VQom8Q5Ji1Zqr7hfkY4hg8iagbzEPGV4NOnHw5IQl-Sbpl6QTBL_1z1Jyy6ngm5U0wFrjbjCaZlS4zUA99FdIj--mm__lBDpJ8FyJcO3LIun5WT6MESaRl7hE79rz4ybnGmVyjhdTefygA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر می‌کنی چند نفر باید تبلیغتو ببینن تا نتیجه بگیری؟
👀
نه ۱۰ هزار نفر…
نه ۱۰۰ هزار نفر…
بیش از ۵ میلیون مخاطب.
🔥
📣
پکیج تبلیغاتی تلگرام؛
کانال‌های کشوری و استانی خبرفوری
🍂
جشنواره پاییزه شروع شده.
فقط «پاییز» رو بفرست؛ شاید این بار نوبت تبلیغ تو باشه.
📩
@Mahdavi_fahime</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/689379" target="_blank">📅 00:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689378">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e1d5f13fb.mp4?token=VfJxSqy9qhOlpJqlyTJdhceUZR2iGTZbCl0TIK3MoI4WzIfx6y_3KmhTw31Qu3q-_aGeOsXF5LNrVuBRamemvSsAMSNqXEh2jZbtBmwrKOTRbfU5akDa09qZfnlXtAvQHhw4dcUI9o_n57TbGShK4w0cijpb-NphNILkOEyhdY14_L71AgWmwL6DKwG0ytoVxXXcG2buOfeKaobaRdJGeL-TGkF209mhGwYJGd8C50rFnaT24Rj8hXmbILcmdOVuDooFlbuAgKUmc0jQXlUor36W8gV8TSeTsNI45bzBEEVHZaZkgW_UABswuI60ut_lzPUuxIJVtf9y3s29iFSREr70O9TSKAUkN2oouDymRQ52KyVE0U-ftgSgjtpOD2b2L4U9F7w0_5hlBNW9KGvYvVR7SyviXg2ngZAbs_HIh5W8DY1argtVy9oUjQIkkW0blegI7vQjXC8sVkdXWZzXbviNA6JtE8bVyDuQ_qKx13BM6OjXjPUJztx5xC0oFO70OKXqVORBJkRWeFCxKyXU9dOXBQz9nNqsGC1JKlUXaZQ8y_dipwWPazihBXPt489IlXuxJYVejWfVH5MRH7hm0wQhmv9OyyiTg6Kj-A4P9yspaJ3NG42vIPvKjXi--LxbBzk2hTztiNRPfKaTllyGxvZlt517krfX4Sr27yOOaLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e1d5f13fb.mp4?token=VfJxSqy9qhOlpJqlyTJdhceUZR2iGTZbCl0TIK3MoI4WzIfx6y_3KmhTw31Qu3q-_aGeOsXF5LNrVuBRamemvSsAMSNqXEh2jZbtBmwrKOTRbfU5akDa09qZfnlXtAvQHhw4dcUI9o_n57TbGShK4w0cijpb-NphNILkOEyhdY14_L71AgWmwL6DKwG0ytoVxXXcG2buOfeKaobaRdJGeL-TGkF209mhGwYJGd8C50rFnaT24Rj8hXmbILcmdOVuDooFlbuAgKUmc0jQXlUor36W8gV8TSeTsNI45bzBEEVHZaZkgW_UABswuI60ut_lzPUuxIJVtf9y3s29iFSREr70O9TSKAUkN2oouDymRQ52KyVE0U-ftgSgjtpOD2b2L4U9F7w0_5hlBNW9KGvYvVR7SyviXg2ngZAbs_HIh5W8DY1argtVy9oUjQIkkW0blegI7vQjXC8sVkdXWZzXbviNA6JtE8bVyDuQ_qKx13BM6OjXjPUJztx5xC0oFO70OKXqVORBJkRWeFCxKyXU9dOXBQz9nNqsGC1JKlUXaZQ8y_dipwWPazihBXPt489IlXuxJYVejWfVH5MRH7hm0wQhmv9OyyiTg6Kj-A4P9yspaJ3NG42vIPvKjXi--LxbBzk2hTztiNRPfKaTllyGxvZlt517krfX4Sr27yOOaLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از کمین نیروهای مسلح یمن در مسیر مزدوران و نظامیان سعودی
🔹
این عملیات گسترده با نام «والله اشد بأسا و اشد تنکیلا» از چندین محور انجام شد.
🔹
هشدار؛ این ویدئو دارای تصاویری است که ممکن است برای همه مناسب نباشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/689378" target="_blank">📅 00:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689377">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بازخوانی پرونده قتل کارگردان مشهور؛ بابک خرمدین چگونه قربانی شد؟
🔹
پنج سال از قتل هولناک بابک خرمدین، کارگردان سینما، به دست پدر و مادرش می‌گذرد.
🔹
جسد مثله‌ شده او در سطل زباله‌ای در اکباتان کشف شد و اعترافات بعدی متهمان، پرونده را به یکی از پیچیده‌ترین جنایات خانوادگی سال‌های اخیر تبدیل کرد. بازخوانی این پرونده از لحظه جنایت تا اعترافات تکان‌دهنده را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/689377" target="_blank">📅 00:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689376">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
برخی منابع خبری از وقوع یک حادثه دریایی نزدیک سواحل یمن خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/689376" target="_blank">📅 00:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689375">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
روسیه: تاکنون ۴۷ متخصص روس‌اتم به نیروگاه بوشهر ایران بازگشته‌اند
🔹
تعدادی از متخصصان در چارچوب تعمیرات برنامه‌ریزی‌شده واحد نخست نیروگاه بوشهر وارد ایران خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/689375" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689374">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgQsH5gXFYlItXnX52JPcfUvILSi8W4jZsvSFlpML8PX5LkQhiqeCYRsDLLokX7e1ExomzaMM7bi93zgdLUGXB7vfAulJZHd0PSNtQyu4q4iwNP4nyqrc1-b-wf1cJP3797ezuiYrLQ94jw2eitqGJnyNWm8goIaydFLqaN2WkXK25N2mBY3e5Ybx25-XhcMCLcoEiU4ndsCoYWM8bEMMVjZQkOHFZZc8rLA1BXwcuwuAjz1piMEa5-YjB2rJYPhX0fRuX7Q_Q3tEu3SMxx-LjsBw3LWLTG7O9jTQL0EHrcZhis5TiVstKDe5FID-BujVhwcVByUyGuwtbfca_YT6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/689374" target="_blank">📅 00:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689372">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163bee97eb.mp4?token=ViK6F-erfxK5weFGW3sQ-JJq2ON4sUePJZUTDIwZYiUJX9-WbxRV1jjd4VHnhAgQgAyZVq50DX6cUsxAdW1NdlgDdO8NhtUgep0p0W1VNE2abGSX9NeH6q0ipsbwKkln3vS6cFR3gCtZ6Im5_MTEna4T_nzZXhxQilqesDYs6xIj14W-qD19ppC3YcCaCPcTcqnlvQmMNpiquqo4cuPvQX5geuA4IChRbOkse1SQLhUC7E3q04LMtWPwOAqgo73JSdcXuUxGvWiopSTOTF-k9xHzuQiVLDTUio79iZxFOuWK5vLB__L_dRh1FnT8Xwuis-y9sPhG0x3JOHXh1OaRWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163bee97eb.mp4?token=ViK6F-erfxK5weFGW3sQ-JJq2ON4sUePJZUTDIwZYiUJX9-WbxRV1jjd4VHnhAgQgAyZVq50DX6cUsxAdW1NdlgDdO8NhtUgep0p0W1VNE2abGSX9NeH6q0ipsbwKkln3vS6cFR3gCtZ6Im5_MTEna4T_nzZXhxQilqesDYs6xIj14W-qD19ppC3YcCaCPcTcqnlvQmMNpiquqo4cuPvQX5geuA4IChRbOkse1SQLhUC7E3q04LMtWPwOAqgo73JSdcXuUxGvWiopSTOTF-k9xHzuQiVLDTUio79iZxFOuWK5vLB__L_dRh1FnT8Xwuis-y9sPhG0x3JOHXh1OaRWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری زیبا از بندر خمیر؛ تکه‌ای از بهشتی به نام ایران
😍
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/689372" target="_blank">📅 23:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689367">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRIAIEzaNx3OhlbxPDXMxKt8FNnBoyLz7aZJRx0_Q212BXHdh8ZF-kLk5bBvUb2MAAGwVvfckNBsBGRWI8pAHq_iReBE_uKin-K_exsiFuOea8ePeXWngBs5stR2Fe0PipcaQ0A44qtXo_gkhRi43sIAH75D6N1TbaiNHjBOgTb826SfMH_f9Zcu7Gx7sEAB2raRHj1PDN5KiAHC4lYI73k_P1W2osSeOhb2c5bDZvjThJSdAtgyjCBS0SrfictRSPYhbm-hq-taRYDBXFTt7pxdsMz3tlRaAg4-1Bj3M6z0ikp8wALeh-cviyqttp_0QcBvOYSXDjKUdC9-jtVKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8zug8mYqqM4Q0SM4Lt1_1db8Yp2mV3VWPO6c-EWbgdLrQ8LHrrgWL2cMK2vbQ5OxJxMiMH9c2cRutlSjIrLJ4NPPOzxnXkFBe6olUz0O-WPJ_eG1H4aEJ2PNJm3biZlnbzvJ1hgrWeCjzbpYa1hOxEJGwImIIjrLEXh3B4-YbvjoDE63oAdOglTEs4qjJt_8XHGi3tfwsWihMb5IvEGT29pOnt0ZlPGZEM_yiR2z4nFC4MEbCojCoru8bGUpBJ2a18VbVy_Q1VnntVrK-64ovsuiI0E0dVy23ZzdP9eCHVS0Ozg40DvlT_m7H18BBtGrYnovc-zGdL-lnHScS2fOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTK9ZywtioumivVSc4M0WRunn5B_w3x_IzwTnwJ3xzceA-fI0vGqKlXARU9NbHORE5ZmJe3EOZThYxSN_YTtrvPZ2ysOpXYK0DfpEto0XMjFJwbuy1X11C-3GntVbsjvDjcCg89U1pHy5k29CvxZdKkbbyJI23DsObrxQ6r_y6zHPGm3vn6nnG2FBXn8nIHRLo961hQpa5PnUnvpqjyUUd8Eu-uqRBNH-4qOyzClu69x1s40_UIE5kT_jxGlwdctadom8up4m6_gBQLk6nhafZ7fRSzez1FIb6enEuHG-wMx1fSGXMuOaw4za1r7o5EUqUn37v5doseX2slL7HpMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1vajhBiat65yZ1yyEUme6otvIB0UNgrc-mFVpW7_-nfIsZgg0oJpvog0A4A929hst-IJEaTVz1zGdNC1d8EM5bRTMxpfanYzSBvSGiT7RfewYSMMK8nJcFYS-00HP_mezcWwrqAABo8j1Dc1bzE9rXagPQFYVKyG9RR5FdRjqeb9gAcSBixjzaFl-4AlCV4aRcVkjDux981cmTS3iTgSpkr2peVoGS24EQ5N3QjeGKzf_jw7Tz8ZqEM_YkJ3hTO57BFMaa3nHZGGd7ZDCcyV75ZvDjd80GUIPTDME_i0LdSuXQRoQyPkfsIb0NDtR_8j5N3u1vr5ZJwBOELtQY0Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFp7R7AVcOE9dSnw-j3f6Q-y1c0vb8fi-DgYJL0Z12QsNe6HGLkS5k9QSnpZWdARJXZquCWrCJ1aHU2UwGpyVp2Z4pl0U902LiEwTMCRkk-FDsLY_0xZzdCH-VbekqAUgzmQtB9aHgPbNqefasj28HfXDbi_DM_Sab59lYOSDpYn18C6CVH4s5tcc5o2BbEVoTvWQN1QUQYsHxzJ5bP5c6e6-0u2YPBjv06QyBVsEBaDZJI_oS46fTHkRVHXuTyxrfo1HiFvWwZxFZS-mPpiNmAeILmMRbwfEPxAt58CgLnevA7irn2-5A6DonpM_qg5KU-rLajpu0sqC4f4fSIFqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⬇️
همایش هم‌اندیشی مدیران صف و ستاد بانک صادرات ایران برگزار شد
✅
تاکید بر ارتقای کیفی شاخص‌ها در بانک صادرات ایران/ افشین خانی: اعتماد پایدار مشتریان، پشتوانه اصلی توسعه است
💠
همایش هم‌اندیشی مدیران صف و ستاد بانک صادرات ایران با پیروی از شعار محوری «پیشرانی شعب، هوشمندی بانک؛ ارزش‌آفرینی پایدار» برگزار شد و راهکارهای عملیاتی برای توسعه محصولات مشتری‌مدار مورد تاکید قرار گرفت.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/689367" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689366">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_f_CdzTkCd6ItYSl1nZFx5PPV4iplvuZTj0-Te9eWg2FSrVMf1fbfqXVjsKzND4BYrEvdwTkjTF8rDf-jTuZXJWBch_UtxrnXB_SCosFO_yTz_NWJk4Cs98yT-0t1ras-uQjDIy1RSgTjUrtmWCVw2fbN8jODwhWlfxIdHmahNR5AtHjbx1DcVl8uUNtj_BevSpoQ_MTUkFmjOVm0hsykYFQ6rX7QjBEKe2nMSgL1lLmw5o6Rul8JaN2vn_-0Dd-Dsbl_kl-fc46xCIB6gbRY94PMX4PSPSPlk5wulhB7cuj7xrYPJUNZiiHcuPzWWAT6EfwmM5x3ZLLYrxEi_T-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر دارایی اسرائیل: باید شهروندان ایرانی چیزی برای خوردن، نوشیدن، شغل و برق نداشته باشند... ایجاد مشکلات اقتصادی برای مردم آن‌ها هدف ماست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/689366" target="_blank">📅 23:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689361">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9PR5FS6WorM6iKmAfEiCGFltTmoZUGzigXMsFRKV6oO50XpysfMCfxvCpeV-cGGtrf_3pbThcYIxgSUpuyLPG1JZFhSEjUR_MryysW4YGykG-00mEc07rK-nSEiR7hDd0NZboIR6laxVOKhpoTHDQb2-Qx1sWvh4El3-YuOw1cca5qWY1AwkVuX3klr47P0VlW6N4wlJa-EMQGPX8HtELtV0p6nklfkE-I2iqlh4OWzhSqmHXZoBCl7qopsdP6B8xTMiR8W-lCcnmiNSdG0YeODFU0ibrUxJEhGZxbG8O0MQ4pugcAbCOTNAREiJRXN4d-gG6o-4HwZHS-qt0vRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dj7n37SL80aj41xdZG7rp1urFkbM5m33HKxZtqC2G-JM5wFLhBlouOnNf4r2NUJ3ja8rt9zYSKSXjxyTZBehpg_T09-L2qohwEEyBEl-_0adbNVhfRC9Q9fO1bxA8od1OuTdSuJYwmz10RHqsH6VXaimLWyYH1hm1gyDDTT42-PIymg-q0QgessQmteWjR1DQoE8nxA5QlutMRdCjlUi_9uUuDyv9jo657sC_HMD7xEORsE979JcBbBjmZ8WZceMgfEDL0-s89PbNc0O67Sb8JysOiwvlBKzApijFKtjn1k5xomWCYPJVPsPR_CLSfG13ugOOjudkBBfOjELlfTjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvxK7lHLnL-cykyDVXQTbwZFNscyIgTsOeeKf2amMcGIZ0A0NFBk8aTshamymAMZvVIeJ3AVkjPg7b4OfkiUccUqOvYwX4im7GwcqkTZUCIpVoZ2-vgks6vsk6GsBlDBZxEXVECCUtEWOb_58TCZEbYBH6I65sD-EyZHIZOELipUhYu0DreCEP0d7cU3U-ywWiSuNZesUtVhcH72BaAUIYCq2YZZZDF_xlzromvFnQpQgJDTenRVGiDw6u1uWFH_GYY7LCWM-ewbi0Arv4N97_e1r3fdlJqwsIdzJX8yG1sYAgAGSK2youWdjVxCBgLI-IPNdr61teXexAORhCoP4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eST-gaR4o3YvTAmFmywCZQUyF4uB6NDW1CHN_fsuwu4-RBMNkS9fP_Ri84QTMsmZsQe0VrRZziEQ2E0bYau2f1WL3C2iPRGk-snGilFHmJFR8u8vcxEEl4uS2-QxEpDSK9z5_n_C-3QvZqbWVh4OP5wlAPLpmm3xVJLNYnc2I-aHCl6EMgmFfpDTykOR2uG_GMyYV6LifXvNdYOxWHcl2lAu2rdGuLo07QLrmhbJPNbBi2CgGJ00lnKkDkSShaTvhilynxNNKWpE6puHruIjARhXZOFb_KA2u9L5cvZHAUU5paPL8LP3gdm2CqmEZYy9gpfeI5VmUM0yzOis381nJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KbxsL-QxT6uiriwN117GZ6fPN1cJqw0sjU6J4XdVAnkM5Vz6_Hm1qBZRrduEYwZL86RroXBVxsrwkA31YUdHm039o_qTC-zYeFDU2v_4rh-fpHM8dgqiVgQhNmmUSFRwPe-oQJrh3_jX5iIlXDdZa6HRXObtFUqrQ4DNKVCJzzyiIHLYRsx5DfVRSkDtHiDFb7LwQzysUi9mE5LyRbC7H6dxNXsgYZVAk3siPJCy53SHxtflrgxcgk33MSnBjpf9OdHShE4oWP8JXFEZqx_gKyXHH7wUJE4tQXGy-YkBQKOhhCql7L9VMuhXAHJT_gO_g1K8Qlz2qorcsluFgJR0XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سالادهایی که هم به سبک‌تر شدن بدن کمک می‌کنند، هم به شادابی پوست
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/689361" target="_blank">📅 23:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689359">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
کارشناس صداوسیما: اگر رهبری اجازه دهند، ظرف ۲۴ ساعت از سلاح هسته‌ای استفاده خواهیم کرد
🔹
خرید فیوز هسته‌ای از کره شمالی کار خیلی ساده‌ای است و ۵۰ تا فیوز می‌توانیم بخریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/689359" target="_blank">📅 23:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689358">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f55a577156.mp4?token=ferfzAeolb-2S-sWcZ3OEZWsYR8MCPzwytdn6oSu_AsT7FBsHL125ErsGY01cFGmjJs5IAMdvK7y2BQ0WdfCaF6QoYZ4_PaiFgl4Gw4JOCI238LR9zTtmoMhRgpcqkq-gm789vBZs5uTrvGT9ilFsEBbrJNUH7slr4HPhTvYKF4vsr-3g1ePZHzXgd5V20vNETTahrrb4bm4silgOIf3PddZ4tJV-pfMCdy81gtNRiLbi6NeaCN-_TxSH9YiqGwLlVCxmR3V3xxiXwSjuCq0Bqs7S7e9TwXJ4qZrq6bkAu7gUXT7UlsWjsaIXSsDhAi9G1XjlLBkypo4d4U4s8BMJ2Rn9KFkoe2ZUzXDU2JhQw159wXHVdj0N16MckfW4Ab9C3WKNSJNGUytJk4YcEMlNnYCSOWg2Y2IdWGrvxBRoP6u_aXUfb6EfbvLzKJAznwGcCCp2POPSidecZ_kCA3RVSb6KAmVIVmeVWXq4zR6zHCR3ikeJ90mK4ReMr9AukGlpsivfyCBYkPg02E4AJUC9qzW6zidYIXonKLbGfb_CgHH0c_RtTIm5-qIwIB00JCk5v5TzQyJmvNIoi3gu5l8QQNEVE8ENHbl5k0VYRJvXdoDaQBl7TCl-hnsut8spoUfiRHNF1FVXMRhWoirVtwqmDjxPqUWOj60F8M8tZ5Tl64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f55a577156.mp4?token=ferfzAeolb-2S-sWcZ3OEZWsYR8MCPzwytdn6oSu_AsT7FBsHL125ErsGY01cFGmjJs5IAMdvK7y2BQ0WdfCaF6QoYZ4_PaiFgl4Gw4JOCI238LR9zTtmoMhRgpcqkq-gm789vBZs5uTrvGT9ilFsEBbrJNUH7slr4HPhTvYKF4vsr-3g1ePZHzXgd5V20vNETTahrrb4bm4silgOIf3PddZ4tJV-pfMCdy81gtNRiLbi6NeaCN-_TxSH9YiqGwLlVCxmR3V3xxiXwSjuCq0Bqs7S7e9TwXJ4qZrq6bkAu7gUXT7UlsWjsaIXSsDhAi9G1XjlLBkypo4d4U4s8BMJ2Rn9KFkoe2ZUzXDU2JhQw159wXHVdj0N16MckfW4Ab9C3WKNSJNGUytJk4YcEMlNnYCSOWg2Y2IdWGrvxBRoP6u_aXUfb6EfbvLzKJAznwGcCCp2POPSidecZ_kCA3RVSb6KAmVIVmeVWXq4zR6zHCR3ikeJ90mK4ReMr9AukGlpsivfyCBYkPg02E4AJUC9qzW6zidYIXonKLbGfb_CgHH0c_RtTIm5-qIwIB00JCk5v5TzQyJmvNIoi3gu5l8QQNEVE8ENHbl5k0VYRJvXdoDaQBl7TCl-hnsut8spoUfiRHNF1FVXMRhWoirVtwqmDjxPqUWOj60F8M8tZ5Tl64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این جزیره دنیا را به هم ریخت
🔹
یک جزیره فقط با ۱۳ کیلومتر مربع مساحت، تبدیل به بحران امنیتی_اقتصادی برای کل دنیا شده است.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/689358" target="_blank">📅 23:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689357">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-0bwrXa4XTpLDpDg1JhlNTIuzhhtpfZpTlNHSadHJkykN85r9m4i-jkEG5_vMg6DqTJwt7xfCVWCql1_-Mbgjm__93vxsBCo12IRx9afOoBifcoCSdpCUynNhAzGzaKdaVkUymqVMzj-8wCdWgZvL1kAv4CEuwFDdzmF4ePMJVBk7uraTdP9pwZFMsh0_MBpYxg48zcK0ySanMg1jplJ2TbxjlmxRwqQHoS-aWXXD0Rem7zdQw0OqK4wgRr_WiwtPrTNvD5BB10BT6IbshdPkdTSXss_RxTazovMSyPZQlWyX77WML4QC7bkCbe24X83pMZC0PvfMIs2FqOXlwNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای ساخت شات‌های هوایی سینمایی، همیشه به هلی‌شات و تجهیزات گران‌قیمت نیاز نیست! فقط با یک عکس حرکت دوربین رو طراحی و ویدیوی حرفه‌ای بسازید #هوش_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/689357" target="_blank">📅 23:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689356">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
جزئیات جدید درباره تفاهم نهایی ایران و عمان
👇
khabarfoori.com/fa/tiny/news-3244741
🔹
سرگذشت عجیب «بانوی غبار» | زنی که از ۱۱ سپتامبر جان سالم به در برد اما حادثه برای او تمام نشد
👇
khabarfoori.com/fa/tiny/news-3244720
🔹
گرسنگی به‌عنوان سلاح در محاصره پاریس/ چرا ترامپ نمی تواند تاریخ را تکرار کند؟
👇
khabarfoori.com/fa/tiny/news-3244515
🔹
در اجلاس بریکس چه گذشت؟
👇
khabarfoori.com/fa/tiny/news-3244693
🔹
ریما رامین‌فر چگونه این‌قدر لاغر شد؟ | راز یک تغییر دو ساله
👇
khabarfoori.com/fa/tiny/news-3244433
🔹
صفحه ویژه اخبار پربازدید وبسایت خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/689356" target="_blank">📅 22:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689355">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOb3h_drHATll3-7xRGFFvZ0jSPRnoXlBQ6lNeqXKuPtrMs4S1o_GydIN13MFODHKmijqeuIfgaJq05KoOO76XveEz2QxgAUhbr1o3OaZXdcvyX8f7zDb9wtJjK1GW0RMK1BjHO4SsO-srWTOBJqakUc4AcF_3Cfdpqtxg97BI-IP2Le46cRk4FSCdFrywbZWVBU31uh52sq1CoqQ4pMFQurTv29baKuuzxsVSBRBaJW1sMnusAiPQCZLwWNomiJS77DJGCPAf4DDiH1kV1IM5VfQluKpCA6SkLFQKcmEqXIMtYML7CL5iwipY7R-8FyuC2BsUIV8beNjeMahZdEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت ژئوپلیتیک و اهمیت استراتژیک جزیره میون یمن
🔹
جزیره مایون (پریم) با مساحت ۱۳ کیلومترمربع در ۳ کیلومتری ساحل یمن، قلب تنگه باب‌المندب و مسیر تردد میان دریای سرخ و خلیج عدن را کنترل می‌کند.
🔹
این جزیره با داشتن پایگاه هوایی و فاصله ۲۰ کیلومتری از جیبوتی، یکی از استراتژیک‌ترین گلوگاه‌های نظامی و تجاری جهان است.
🔹
در چند روز اخیر، نیروهای انصارالله یمن کنترل این جزیره استراتژیک را در دست گرفته‌اند؛ اقدامی که اهمیت نظامی و ژئوپلیتیکی باب‌المندب را بیش از پیش برجسته کرده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/689355" target="_blank">📅 22:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689354">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4cc63a880.mp4?token=vtbxdeBdq8V0sTzOrc7IKmzN7LzZ2bf-xJZeq9hmWLx8KckpA6SFJJx0DLnyUo3SojRYlseb-bsjjLznZaytlwQ0I0P7yhUa6kw5wNdv4vySHo9gSz13dyZdOEOU0-Mn0uxb63YvsF_JuQmi0SOgUOg1DOZxmk6fMefinDVtXBdEycMZonXg1_TWTYXP5BsDJ03KsfXMbsKuvu-P6ceqBTaZZYxDVMVFE3_IRa_xPtHII-MtqmBLfBwRTQMlWgakhmLmIzMlUzqIFe4HGmTzVVAL5r0ejdEkOZGhncu5zFU3PG0cY2zKQLUC6j_jA-XdPGbEKrCyMz4iw040gF9SRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4cc63a880.mp4?token=vtbxdeBdq8V0sTzOrc7IKmzN7LzZ2bf-xJZeq9hmWLx8KckpA6SFJJx0DLnyUo3SojRYlseb-bsjjLznZaytlwQ0I0P7yhUa6kw5wNdv4vySHo9gSz13dyZdOEOU0-Mn0uxb63YvsF_JuQmi0SOgUOg1DOZxmk6fMefinDVtXBdEycMZonXg1_TWTYXP5BsDJ03KsfXMbsKuvu-P6ceqBTaZZYxDVMVFE3_IRa_xPtHII-MtqmBLfBwRTQMlWgakhmLmIzMlUzqIFe4HGmTzVVAL5r0ejdEkOZGhncu5zFU3PG0cY2zKQLUC6j_jA-XdPGbEKrCyMz4iw040gF9SRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصب CNG رایگان برای تاکسی‌های اینترنتی
🔹
به گفته معاون وزیر نفت، تاکسی‌های اینترنتی پُرپیمایش در اولویت دوگانه سوزشدنِ رایگان قرار دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/689354" target="_blank">📅 22:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689352">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_xNj-qDZGVTMATC-HjJ-dTKnXm3ebd47mqoVWnm0fyZ9oCbXEURnadqyPBuXKeijmqRXVXsZ9xQTZu9ujqDN3hXRm3ZUWqIIFH9zZJYmIS2LbTbwyL_aflFV8xF0B8-FFPh2ysUjrM414RPMIVDpdJwV8QT9vNxx-3H5ienodNykZUFd5Yd4stbLYJh9KjhHr3P3lugs_dhitGCeqls1bYcpvA7BwLFOMMoOXIUY6qyDXs8iXCYUqsku9kwukoQgJjaxamhu90kkyDu88ykxMH3thxP0oOYN6AkZauMj-AmrMf1zYcMet3FdxX5K63G_9NcH1JyTsPj47r-B-AZCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لاله مرزبان جایزه بهترین بازیگر بخش «افق‌ها» جشنواره ونیز را دریافت کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/689352" target="_blank">📅 22:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689351">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
حملۀ عناصر داعش به مقر ارتش عراق در کرکوک
🔹
هنوز ارتش عراق به صورت رسمی این حمله را تأیید نکرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/689351" target="_blank">📅 22:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689350">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8DY3cuCYHW-R4GSH8wri_PNaKLUdY_StvrUgeKp1x5y_El6asMkDBE_ITZ0YK9oO1Yj9xuVTf61hqe6PmF4VZmGpBfUzovKPdRLt7jtO6EFzIYEAtwfUnATKo79cBz1rqw8e4LsWFovfBAFZVfCFg_onhUwDjO0K9WHE9FMWn39X8MYbwmNzAAXChcrPyOLgplv4KStiCASnZlBqs7RLoOHynv2oBM8aGsq0FWLMwdIM7jAa7vQLVZDvEsknwFt18kNSHlVaqbpn8UWp8wJv9xtXrDsKtKPwC-_zGjCkdlaEdy69634lk3rorLArDcKLSn6OfhSFRW29jsng7RyVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فهرست‌بهای رسمی برای کالای ممنوعه! | اقدام عجیب گمرک؛ انتشار فهرست قیمت مشروبات الکلی خارجی | از آبجوی ۴۲۰ هزار تومانی تا بطری ۳۱ میلیونی
🔹
انتشار یک بخشنامه پنج‌صفحه‌ای از سوی گمرک با سربرگ رسمی وزارت امور اقتصادی و دارایی، تناقض ساختاری و دیرینه مواجهه با پدیده مصرف الکل را دوباره مطرح کرده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3244728</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/689350" target="_blank">📅 22:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689349">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
معاون سیاسی و امنیتی استانداری خوزستان: مرزهای شلمچه و چذابه به‌صورت موقت و محدود تا ساعت ۲۴ امشب برای عبور مسافرانی که پشت مرزها باقی مانده‌اند، بازگشایی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/689349" target="_blank">📅 22:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689348">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای منابع عبری: بن سلمان به ایران پیغام داده که جلوی پیشروی یمنی‌ها را بگیرد و در عوض امتیازاتی به ایران خواهد داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/689348" target="_blank">📅 22:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689347">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قیمت لوازم آرایشی و بهداشتی تا ۱۳۰ درصد افزایش داشته است
فرود امینی، رئیس اتحادیه آرایشی و بهداشتی و عطریات در
#گفتگو
با خبرفوری:
🔹
مواد اولیه، کالا و محصولات لوازم آرایشی و بهداشتی مستقیما با قیمت ارز ارتباط دارد و برخی کالاها ۷۰ تا ۱۳۰ درصد افزایش قیمت داشته‌اند.
🔹
در حال حاضر ۸۰ درصد کالاهای قاچاق، تقلبی و حدود ۲۰ درصد آن کالای اورجینال است.
🔹
در بخش لوازم آرایشی، تولیدات داخلی پاسخگوی نیاز بازار نیست و هزینه تمام‌شده تولید داخلی بالا است و ظرفیت برخی خطوط تولید به‌تدریج کاهش پیدا کرده و با توجه به شرایط فعلی و محدودیت تردد، برخی محموله‌های مواداولیه که باید دو ماه پیش می‌رسیدند، هنوز به دست تولیدکنندگان نرسیده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/689347" target="_blank">📅 22:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689346">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5e7b1618.mp4?token=JswAyzIDENqQah3eWtVAA9sZv82Ll2k8t3aVBv4hTz8OFUQwJAiMyjjvxmfswEyfaMW4lI8oqeIw-gByD3DoOVGGlOpJn60y6lOaayFDOK3zrgnOILDJO7KzyIkD1kXknP_dt0FhL-_YbbrS2Z_aKEDTbwXC9XcZwrjt9WPqLqep-XIQFKK2Y8PfQ-9RhuaUrQLsHG5j0zyyGLe7Jdc-cIjMG5FNeX4nb_EQTsDcawIHQgbdfAs-RkOEMnIRP58reglycnml0fyDKwwHI2Zmepn6paBLExMyUazVGNVEiK33qJKqXesOk6ojQMGISIqNDjNTU1HMgnsavqQx2yYZxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5e7b1618.mp4?token=JswAyzIDENqQah3eWtVAA9sZv82Ll2k8t3aVBv4hTz8OFUQwJAiMyjjvxmfswEyfaMW4lI8oqeIw-gByD3DoOVGGlOpJn60y6lOaayFDOK3zrgnOILDJO7KzyIkD1kXknP_dt0FhL-_YbbrS2Z_aKEDTbwXC9XcZwrjt9WPqLqep-XIQFKK2Y8PfQ-9RhuaUrQLsHG5j0zyyGLe7Jdc-cIjMG5FNeX4nb_EQTsDcawIHQgbdfAs-RkOEMnIRP58reglycnml0fyDKwwHI2Zmepn6paBLExMyUazVGNVEiK33qJKqXesOk6ojQMGISIqNDjNTU1HMgnsavqQx2yYZxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش تگرگ در بشاگرد/ جاری شدن روان‌آب و سیلاب در مسیرهای جاده‌‌ای
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/689346" target="_blank">📅 22:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689345">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4044738bc2.mp4?token=YrTM2ENloq5TTAnHa9NmfkRJemcyWe66xbVZmL5aP37l8RRw8cagRQJ7ruEFLDHrvfqNiynGx19W_GmzLwJPnvnhgqAc1ftzvgUal8BlzbNzbMNOt8Gn9VY5MN3E69A90CB_O5GK3XRsjnhewFRywHunIQPdYee8EO_EHUA_sB8FUswNYlQJjVC6YX7JMER-TovWj82DR0vuQnM3Wz9Rm8AXQO_iuvP01gxKC8p1ANKnuN5gu6127Ronm5klr4I1Q_OY7jKtZIoya7kLLJZFU1d0eKtd0-Sx7sIgSforfyYnCpNiOt0nbqo7KQ7Y_OBNV_avte52Bw1hLtIn7u0feA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4044738bc2.mp4?token=YrTM2ENloq5TTAnHa9NmfkRJemcyWe66xbVZmL5aP37l8RRw8cagRQJ7ruEFLDHrvfqNiynGx19W_GmzLwJPnvnhgqAc1ftzvgUal8BlzbNzbMNOt8Gn9VY5MN3E69A90CB_O5GK3XRsjnhewFRywHunIQPdYee8EO_EHUA_sB8FUswNYlQJjVC6YX7JMER-TovWj82DR0vuQnM3Wz9Rm8AXQO_iuvP01gxKC8p1ANKnuN5gu6127Ronm5klr4I1Q_OY7jKtZIoya7kLLJZFU1d0eKtd0-Sx7sIgSforfyYnCpNiOt0nbqo7KQ7Y_OBNV_avte52Bw1hLtIn7u0feA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمادی جالب از ترامپ در دستان مردم در میدان انقلاب
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/689345" target="_blank">📅 22:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689344">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/689344" target="_blank">📅 22:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689343">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSedSD5Dr7f3ePqgbgIDqQ5B2GqAXj6x1w6Wdxvoqr6OpPMqSxNw9NvZtqCAkTYK09qzrXN2ZI_esiZbaBSLg3fmULRQDq-s6iqmYVbDdBmWrnlLLhdDXe0wQagrZMyTHlrphH_YE1u9DpBdvFPogUdGI1pGVnGGrv-cDD8PZcM6g-09qVRMXuG1OlKGTUJ5avLOuOqRMGb7trhf3tK3w4t1W1ArHWW9L-M9r_jsOoMJ-UKSsDzBb_nSmpyPjFVSo8MK9tEZEW1FCR5_zhG761gbsGPNRtNyUkH6L2CC7A9QntX34ForlVX4mPp_Dry9wm_AJv9ioVo6V6ZflLOC7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهکارهای فنی خودرو برای کاهش مصرف بنزین
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/689343" target="_blank">📅 21:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689342">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
حملۀ موشکی یمن به عربستان
/
شنیده شدن صدای انفجارهای مهیب در خمیس مشیط در عربستان
🔹
سازمان دفاع مدنی عربستان خبر داد یک موشک یمن به منطقۀ «جازان» اصابت کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/689342" target="_blank">📅 21:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689341">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f506dbd1.mp4?token=HdWl7l8Uj7YXLrO0iPjfvmMfa06oS5H-ME-mHXraUZYMRQrt0LKtTp0fAzuQg47u-7Iav8P7OEt0WiBscaT9NPQrsl9todZ8E3cJwOGCcAgDbBe0Hc7hCK0BiOP5zpjho-pqT-z_hafiptx4Ix73Vr_KDm-WGokSXi5Snxr4VnR3mowrNDJDF_qV4Ywz4hWO0A4g7m_HytFyuwwI2MEcheRr3cr_HIOW63BMlyUk86w3cGXwek2jFm50YDVqyFvy6IhQ5zRgH8jSWJ_IfrgHJtUnBgokzun4xnIXjHyBJ_eYgL3QvjYEh-QLb4orT6tpfHZZhHvusG-GHTV725cQ2zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f506dbd1.mp4?token=HdWl7l8Uj7YXLrO0iPjfvmMfa06oS5H-ME-mHXraUZYMRQrt0LKtTp0fAzuQg47u-7Iav8P7OEt0WiBscaT9NPQrsl9todZ8E3cJwOGCcAgDbBe0Hc7hCK0BiOP5zpjho-pqT-z_hafiptx4Ix73Vr_KDm-WGokSXi5Snxr4VnR3mowrNDJDF_qV4Ywz4hWO0A4g7m_HytFyuwwI2MEcheRr3cr_HIOW63BMlyUk86w3cGXwek2jFm50YDVqyFvy6IhQ5zRgH8jSWJ_IfrgHJtUnBgokzun4xnIXjHyBJ_eYgL3QvjYEh-QLb4orT6tpfHZZhHvusG-GHTV725cQ2zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ریشه فساد در سینما چیست؟
اشکان ضیایی، کارگردان و فیلم‌ساز:
🔹
هر جا که پول و قدرت باشد، فساد هم هست.
🔹
سینما نیز از این قاعده مستثنی نیست و وجود سرمایه و قدرت در آن زمینه‌ساز فساد می‌شود./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/689341" target="_blank">📅 21:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689330">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZItYyedyiox7lE-g5TVjMVJSynd58TrHtGw3ZVHAVX6tU9JL3NkqjSum0xbcjX-act3CB3M7goQA_pfFGqCC5w4hKQj9OIyAkwFJHILSG-4R4xU0nzVqYU6Oto7_9RI5zXmUXgUjbiS406IqMKG1OpJI7A4zumR1sPiLO8nHNYnu99laroZ9A1NHsW72pjD8tKr3s-prvk8HcJkq6ypLQda_9kiuecxKuyxZIhSsRsyFU2QEeTCRce8l9f6p3hbSVEF2Erncby4U3jL0Dfd6au33aaOxaOO7MV23iFLz9Vm9O0c2usBtMktbbKRbLc9SwCPqcoASoIi42avgKc-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jU3tkq3hqr-1n5MJgdBYMr98Ew0ZfTUaSY7EQYQUVgsjXTv7SP6k2GLjbD9-N_En0jD-GE3Upqcye2X-hhxjTHyQsa_OPe-DSpY_DqvGsFuEbr21y1X0Vmij0VGuaMdxgeqY1thA3nauScAbdjvkdK4P3u9soifzZoGjXIb15NN3Ug5AJ9FwB32bjXFLOMnabczIfw1Re8xrehAZ2rQa0Jwu34vgoTMs-TWZGHz-c8Plff5oM9rNFOOytOkyVUqT6PE1jRGOBVt4U3bvUmPcxUxq-IavFFKwIHeaoqF5_vhQ65G3ACmc-gueQSXWHHlqPlSRE8mYM4-yJAl5RXoNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHtHVMjjsDKYwHhKZi1T7eyJRedQ3N0nMsCCtpwY1684_W1ZRsM1op_cIbx2CvWOTZPuMHz_a3TR2Pbt9IElvsjLFaaE47zsXjI3g_qzJkuL_fjUQ9GIc4DZX9kQJaNHvoq81gWaV3HPhJut5WvS9LnN0z4595i4QXs_ZEhv4sjvW7FAkf0-DzybEYF6TCC8O-p_5A-FOai1wbvcdpUDXObCKt_z77ZQlng5wJXN7A4SxWH1Td_I-qLbXO1aszFKBkWmcVUz1_wAeFUXpkRSQ-qWNZsnYZcXIzcQF_xcAnJQog3oFViadXDZ7DGcaVn-hYRo630vBmNAuxj9W-Bc9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TmUgwasIs8DiRldxQpaYg1Kw0yIKU7TVkkgr-zB6FxvEEprCpS9Tuc2pSV6yucheATx7TiRog4gnkIZzQbOVRHfCi_xf9NxTwMy-8J2rh1Yk--jeA3AUyk_obQBe8FeDyw4GKfneKGPyg8qWsUJARYipqxAMl1li4IrNeJLN8luriZKlSRTyhjKSRC6ZgUHYPKOsa_Kcr-GVgGuia3Q5-FIOYDAmIjh05DPeTnyAFSmAoH0O-0m3rzXnfBRza8AXmBqQYlc431jQr3Jrflr9HIGA7wijqIlm58vYxdGnlx3OAqP7esXsB7IBvcWjDO-BnNGAGHpo5szi02dNpA3tBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOCHONpUT42XI1CPTpE8gej4jTcZzF_ZJsnZFaXj2NlBZ2_aQNyFHnSKSnt8aZkW5e7gGARk-YD0633jwf-n_F6dyE_kFoCbTrWM2_ZEoDnJwc9eiZeX8MZATxfBOlUaWXwBzUro0eFCr21BMBkNEU9Zz1B5Lxxu9pSASXaUeBMJTNmKBOSiDCpAXd_Ci-AXDh4ILDYpKHwr_0EE5aP486ezt4ilYhtYzbD8j1974Yz60zozqHWWmj60pMkCm0YLAMXfupX4Ehdm2_Id1ljh6bpSiCw0C_cNPp9xP5XlnsNY_DkpmP1tK_yYbQmF-7VLTPBf6MUDkPtYzQBOvkJbLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_egxxdyGMYQKlhY1OpzdY-jIUwLj4o9rM7WI1apZ1GSShlh_zpaaNtGZ9aLk6WaYmQGSsK-zm480ee7CGijDCT8uvJzoNPxYCx_AJdZPc4sn2-auK3CL1R0O58Q7ilJ19Jc1PH3_FaEco5OBaopVsOwZar2H_a27X2AUq9Ih4Elk3G30YgccskmiwiJwGdQYtFcPISJWY6ZV3Mjiy6izfQU2fpMGKSrmzjaK0L7in05Wz25LbbkcVv6OYFa_26IWxBdnfWDXFtG_C5gTBPleSnA531iO1IMNCcub9vpLH3KhXcwjyXt4hpI46potDxNa_IjDIQwkqrQF-bAkJFJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P97ckVvsNjOCjMlvOeWEs3fgTCHipKdk9cVdqD6z7GUN-rrd9pqTke8T2ft5qLX3c254xCVTfMIoDERjJsDK54ssvX_FxaTfYzP4bJbL3ErqeRCDzdjcUPgaqrfaEBD40BjR5gRoi--5N5AgPPCyWKEzWyX_sDBq0uPSoy5pfmx2rxMCV5vlaxEmV6HnPlWUBEjYE5CWxrtg2-M_DXv3TOm1IOFuxqG3jKgf0vB0AqOhuGpEu8LRvqFNyfn8_ShmfWGFvl3FALzwA9g-DlEQMK5O3T97cMkXzQA-keD2SYlnVLBj27oWEHMDfiEksAW9iJGLziaZY-qlr8wP4uYuRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-XimoWrOT3AlmbsTVsgUowVnHwZpDQrzKF6dI9732fqokSiroLPwdlZP7liyN8pa3_57_Xz6HOiggW1IOhxjNpf_gd15hI0Phz1EIncKYY7MBwOI1tv8h1SXp86LiD_HnnWOoHGrXmpR-cgKShKbs842mps5GyZY58UhIT_aH9aFQblMpTiqEoU9i5gHxQtWVq490mIMGNKSSr7ZgQz5p2B6doHNJlbGZ3luPMFtG4hMcH_ajR27OHC63IhFa4BJzCANLNYlZJr4BR6fhhy-0mrAY3dZcDJyCzQnw_ufaOKCBs95TUJdEm3p0KPz9reJ5LyBw5jZdI_aDmdw-M7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfq612vjkXXPvbuxd_gsqKQCTgqIz1pWc9Y9QOgmp5P_KKlPsP5haN2amBvZXDiOeDIduebmRynezeX5HbpK25mse3uAse0B8cj8YKcnS297JeWCWuCkBorjIG4uPW5L8NFBGH_unpnLFeB5ZndcJkGjsNzsZ7OuxRATbX-6N4oCJ0P2GlSxXyPPCJj7lrp_uAfDYkWwP060ygHsWS3lkgwA5lcZez0d0yzPT60L5ek_sCJyOsL2IYWnjblZUbxatElvoBDFQKLiVWJzkx4dDqFaknfARfY4Y_s8GM7WKfJ2pQvWwehAiED_TfblBhkPgpM8tEZlj_0T5ySwiPCq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJr2ipIASPSgcXiIozn_mLx04_Ife6borCaD0SUvt_hMnlzZQEnK3qXVUt8MWIlIISPFS7MJnZEvGtnWaLEl1cAblrXgFYbz4iZjGhxss0unkUy1E03BJU4H0bNViyduScbMXf7wDqYrt_kavH2zx9cz4yb8hj_gysZfLDx61GOLQGjhgR24HvNhhsHpkua9MGWm5wcYBgdwUk6K1fzovGL2p_EkIzAakX0Ga-FPMgtBq7xr4Cw6FNn_rX7j_tgx1aaT7_w8Abdw6YXWhqH6x-KSEZTxXbcJAoxtBeoGOXhPH5lKk6I-C7kMa48BLH4yiuYupdnd67RTho7N9LaRtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
روایت مخاطبین الوفوری  از موانع پیش‌رو برای دسترسی آسان به اقلام دارویی ضروری.
🔸
در چند خط  روایت خود را همراه با نام، شهر و نام دارو برای ما ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/689330" target="_blank">📅 21:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689328">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daW9uq8cjS03jh7bSpUuRYyH0hUyTWKlJjVAl0yobY3sOyNbGouA7xBzZXZ-ZgDiQ5PlUlk-OmDinRL0oYnWiBl6t5B2sqjgOCNdcuumYcoQsI6EwH9qOWHezf7JUv-O161Jifl0uPslGYt1RK6NYtLY0RUsb8_brr9IXPnJIhXDqmt39Ix7WpBdMpGFy2jY0tjpnda56q-e3ruiSoYdZ2Tx6aqdlM1Qyg5PK84ihXANTT5fCzPFtZlpkWi1fJI8r_wCSsIoDdt-CNc5maTOzXxWfZH58l2WHqI7QU-8mZSuOciPWk8BIJI0YVMBrJ7p5mspTXm0lQ8yhXK1tBt8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از جیب فقرا تا باک ثروتمندان؛ بنزین به کدام خانه‌ها می‌رسد؟ | ۷۳.۸ درصد فقرا اصلا به پمپ بنزین نمی‌روند
🔹
بنزین در ایران سال‌هاست بیش از آنکه یک حامل انرژی باشد، یک موضوع اجتماعی و اقتصادی است؛ از سهمیه‌بندی و کارت سوخت تا بحث آزادسازی قیمت. اما پرسش کمترپرداخت‌شده این است که این سوخت واقعا در کدام خانه‌ها مصرف می‌شود؟ داده‌های تازه مرکز آمار ایران از هزینه و مصرف بنزین در دهک‌های درآمدی، تصویری روشن و در عین حال نگران‌کننده از نابرابری در الگوی مصرف بنزین ترسیم می‌کند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3244689</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/689328" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689327">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
دقایقی پیش صدای دو انفجار در قشم از سمت دریا شنیده شد
🔹
منابع محلی تاکنون در این باره اظهار نظری نکرده‌اند./ ایرنا
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/689327" target="_blank">📅 21:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689326">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946a6ff60e.mp4?token=toNIqFLgz5Q6aGFB-NpZjcCYlOGQ4RJPrdksXmqdAFLSe9LrDwkvn4hAZfRI2XGX40JVJ-rtGtNaN_QYJa_y7Z3o0t6w8JvUI8HGCmfTISZ6lJb4VhdmiEdGcOIuOZp13uQ5AVtsDWPde1iAe3ksSTzK19hSdtx53VvFlBNyT89bSZ1kgaZT96hlZakVPWxaVzQjOD6Jjnzl4oMAwp0UDRemCsX2YUHDLiCt4BvcQslTbQ1vTP7gVPuDbKnyby8DaFtmmuNuQC_HqLSO8gW6g7-24Vr-GmihZ6lHqaWHf-rcbjxm02AOMev7f4Z3lht8E-3IhtvBzsDdgDBc_N7IZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946a6ff60e.mp4?token=toNIqFLgz5Q6aGFB-NpZjcCYlOGQ4RJPrdksXmqdAFLSe9LrDwkvn4hAZfRI2XGX40JVJ-rtGtNaN_QYJa_y7Z3o0t6w8JvUI8HGCmfTISZ6lJb4VhdmiEdGcOIuOZp13uQ5AVtsDWPde1iAe3ksSTzK19hSdtx53VvFlBNyT89bSZ1kgaZT96hlZakVPWxaVzQjOD6Jjnzl4oMAwp0UDRemCsX2YUHDLiCt4BvcQslTbQ1vTP7gVPuDbKnyby8DaFtmmuNuQC_HqLSO8gW6g7-24Vr-GmihZ6lHqaWHf-rcbjxm02AOMev7f4Z3lht8E-3IhtvBzsDdgDBc_N7IZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شادمهر در راه بازگشت به ایران؟
🔹
محسن نامجو با هماهنگی به ایران برگشت؛احتمالا شادمهر عقیلی هم به کشور بازخواهدگشت. فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/689326" target="_blank">📅 21:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689325">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش قیمت ۱۰۰ درصدی نهاده‌های دامی/ انجمن صنفی گاوداران: افزایش قیمت گوشت ناشی از افزایش هزینه نهاده‌ها است
احمد مقدسی، رئیس انجمن صنفی گاوداران در
#گفتگو
با خبرفوری:
🔹
حدود ۶۰ درصد نهاده‌های مورد استفاده دامداران شامل علوفه، یونجه، کلش گندم و ذرت علوفه‌ای تولید داخل است که قیمت آنها نسبت به سال گذشته ۱۰۰ درصد افزایش یافته است.
🔹
فعلاً دامداران این افزایش هزینه را از جیب خود پرداخت می‌کنند و این افزایش قیمت هنوز به‌طور کامل در قیمت شیر خام منعکس نشده است.
🔹
در دام‌های پرواری، بالغ بر ۷۵ درصد قیمت تمام‌شده دام زنده مربوط به خوراک است و بنابراین افزایش قیمت گوشت که شاهد هستیم تا حد زیادی ناشی از افزایش هزینه نهاده‌ها می‌باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/689325" target="_blank">📅 21:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689324">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
جزئیات جدید درباره تفاهم نهایی ایران و عمان/ تنگه هرمز با این تفاهم باز نمی‌شود   منبع آگاه:
🔹
تفاهم ایران و عمان اوایل شهریور نهایی شد و به زودی با حضور وزرای خارجه کشورهای حاشیه خلیج فارس اعلام می‌شود.
🔹
مسیر ورود به خلیج فارس کاملاً در آب‌های ایران و بخشی…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/689324" target="_blank">📅 21:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689323">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13bb4a0b5.mp4?token=QvKa27H6jFEGdAthtP7v2AQpkKnGA5osAD27OW2j9fw80E9hUhWiBUCZBHAyX1_0P3_lPnQi5fMo76sQtY7sPAFJely0AGqo2MKybc06KgIMhZJ8jHEtMTHvCZTFj0Di6AF0i6lknk0hrA9aL-_eMNWJlxu-fhheiVid1513c1WcRKXVBc0zka_F3TtRwCZVqcF-JRqmS1qDNSBlZ8lvqxj7BvizkeOUF8WveLqNslxU13Sf0v8o728CM6DAv8RCItHaGNJixS_8i0nr2GcS-2ntt62l6zf3v-AaVd3J7SsRIoVVH0UtP9dxTz3VFOZxj6VrS3UOAdKSDY6Ew0iUlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13bb4a0b5.mp4?token=QvKa27H6jFEGdAthtP7v2AQpkKnGA5osAD27OW2j9fw80E9hUhWiBUCZBHAyX1_0P3_lPnQi5fMo76sQtY7sPAFJely0AGqo2MKybc06KgIMhZJ8jHEtMTHvCZTFj0Di6AF0i6lknk0hrA9aL-_eMNWJlxu-fhheiVid1513c1WcRKXVBc0zka_F3TtRwCZVqcF-JRqmS1qDNSBlZ8lvqxj7BvizkeOUF8WveLqNslxU13Sf0v8o728CM6DAv8RCItHaGNJixS_8i0nr2GcS-2ntt62l6zf3v-AaVd3J7SsRIoVVH0UtP9dxTz3VFOZxj6VrS3UOAdKSDY6Ew0iUlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش تابستانی در ماهنشان استان زنجان سیلاب به‌راه انداخت
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/689323" target="_blank">📅 21:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689322">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
عدم نظارت بانک مرکزی بر سامانه‌های طلای آنلاین، مثل این است که بگوییم کلانتری گشت ندارد
آلبرت بغزیان، کارشناس مسائل اقتصادی:
🔹
در بحث فروش آنلاین طلا، ممکن است اقدام به فروش بیش از موجودی طلای فیزیکی صورت بگیرد و زمینه سوءاستفاده فراهم شود.
🔹
اگر بانک مرکزی مسئولیت نظارت را نپذیرد، این سؤال مطرح است که چه نهادی ناظر بوده، موجودی این سایت‌ها را تأیید کرده و مردم را به خرید از آن‌ها دعوت کرده است.
🔹
متولی مجوز دادن به چنین معاملاتی بانک مرکزی است، چنین سامانه‌هایی باید دست بانک مرکزی باشد، چک بکند که آیا سایت‌هایی که اعلام کردند این موجودی طلا را دارند یا زیادی فروختند و خالی‌فروشی کردند.
🔹
تصور می‌شد که این نظارت وجود دارد، نه اینکه بعداً متوجه شویم نظارت بانک‌ مرکزی وجود نداشته است انگار که بفهمیم کلانتری محل شب‌ها گشت ندارد؛
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/689322" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689320">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWbq6JhFbJrcq0vdkYu2bC0RndAzjU4G2ASJwa8SCd9AMjJWjaY6TjO5ktY0nMG38opwd84jMqkUVvQ07ITKbvT11g1FBUNv-7lWZJfp2XKFD6NKk9PtJIpJMYF-e9XFG8odL1oQO453hxiBH0B7KF4QqAlykJwMiHAxQiMjZ7DlblSGHMVxMOsOdtbZ_BFEf3Yv9gJLrHYQOxM68bawN2VGdId-ssE4Y1J-srSXAMUichj-PKgRjpErTFjlarKbOFapqqixlSDSiobJvc5XgCTF4j6qcq0vHlCstz3uAVb5GdiQIXBAtGbfA33IjJf7RPUq95ApxnODo1XsYeG2jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPGn9CSvqw-dZ38mzPJ8bPiwj1alIJnojHiMNZ5hhnVYhOiA6FkIabjnL-nLcVfTUChVbrbSxEkKY443K5T5DX8YE5K2UY-sxldG15hl8AhxZGrgXbpgWnx8CClbL5JHbl63KJQojIxHpi4KzW9-3USpk1ptDKh1bQn1-57SjWI9fCKtDHerc-dY8_XsEwwdM_R8P3tTgoeQgx0Ac3s_nO4fwpLAOi9y1JKkKNmP4UTkdQCnvuJ77qOXgY66kj0CoxjC27NGmovDloiGsbtct2FjQymcqExPgS4e_vLasyjVVrtggpoy4D5GG-RV6FN81Edt-RB39mZ41oNH8wfNrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منچ اوسینت: امروز تنها یک نفتکش چینی با سامانه ردیابی روشن از تنگه هرمز عبور کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/689320" target="_blank">📅 20:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689318">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fcb869d7a.mp4?token=HzrQ_IO7u5iqDdNlD-uoc_uQKnpggvDNAgIZ-spOg9Cjt2Mwozn4w4tkHCZBrq3GrBulm_alJHjOmrdW-iLmFtggTxI7qAn3WrYCfSoo2zTLZn9vYv__FM-luV_1wJi6kGX_1-1NdyAshBvvoMiJgo3Tgy-MFgLIZ6q8W_LyczW0Sx1oDFqNsnrS8CwpNEO63LYUOqHoRdnJ0wNz9kjd6mtRBWo7a-_hD94WmWVV2vbTVdBSAh4YLJsxStfVyeDJHW2Z6fyhfEKnKsL6VYJCYUqMTyoiCKPnH9CByQfZz8NjDCu6e9YPlpADmJV1TMUA9f9j617wWxhiUoTVDun_QjUVJziLk4nbKMzGqYhaDv5D_r-lsKbh-X8zgDE218DF0im6rGV7C47s5IjoX4KiCGYqZZZixiaqscmRBPScV0O6Qp7EFSZIRJpF6u2QNGa8NuslxcQ2WYFJVS-AFgI0kobMvFbJ0u6Vwkj0tZZDRuGd2rdohULwV4PR05Hek_BeaaasZaDo_phq2Q72Bm4PATaPVeM4ErdLHm5743btAZu-4NwcYjb0BKgkhrL5GISVpizheWD_88MR2gp23ASgkWMNtjdMi2OhEjD3vqKcfyLvaNPV11P8JLQjbTBFpLsAMi9a4_hq-QnjTJIan5VN3ykYkPZ2YMS54AAuVcggnkI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fcb869d7a.mp4?token=HzrQ_IO7u5iqDdNlD-uoc_uQKnpggvDNAgIZ-spOg9Cjt2Mwozn4w4tkHCZBrq3GrBulm_alJHjOmrdW-iLmFtggTxI7qAn3WrYCfSoo2zTLZn9vYv__FM-luV_1wJi6kGX_1-1NdyAshBvvoMiJgo3Tgy-MFgLIZ6q8W_LyczW0Sx1oDFqNsnrS8CwpNEO63LYUOqHoRdnJ0wNz9kjd6mtRBWo7a-_hD94WmWVV2vbTVdBSAh4YLJsxStfVyeDJHW2Z6fyhfEKnKsL6VYJCYUqMTyoiCKPnH9CByQfZz8NjDCu6e9YPlpADmJV1TMUA9f9j617wWxhiUoTVDun_QjUVJziLk4nbKMzGqYhaDv5D_r-lsKbh-X8zgDE218DF0im6rGV7C47s5IjoX4KiCGYqZZZixiaqscmRBPScV0O6Qp7EFSZIRJpF6u2QNGa8NuslxcQ2WYFJVS-AFgI0kobMvFbJ0u6Vwkj0tZZDRuGd2rdohULwV4PR05Hek_BeaaasZaDo_phq2Q72Bm4PATaPVeM4ErdLHm5743btAZu-4NwcYjb0BKgkhrL5GISVpizheWD_88MR2gp23ASgkWMNtjdMi2OhEjD3vqKcfyLvaNPV11P8JLQjbTBFpLsAMi9a4_hq-QnjTJIan5VN3ykYkPZ2YMS54AAuVcggnkI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت تعیین‌تکلیف نیروهای شرکتی/ جزئیات تصمیم دولت و مجلس اعلام شد
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/689318" target="_blank">📅 20:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689317">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8qz4mR4SBvuYgw-4nYtj5l8z1Bm41dWDZR6HpIUxv5tknT1356r_vvm7yagAsW6o-uDPNO3fv2uizJyfLKTXpCCw_iqh-RpxsPtNiCzmsoTkKO8iXk0wexz7ww9d7eUD4XvS_ZC6-WfsS-aZ8W6MYxJ36u0xAqeKh-XRBlxuf37Kpy_qH2fv0hg4ewjHks6JM_4XXR4XpKQY-r2yvmsFwldFWiJerwomGhvW_0ZtlXeXgHvcmSnBCaR-ovcVq5lr3ieVIer7SO4t-E7cikmT4dmlTIcLPMDMnsTVKxq1hN2urHRZ9pE-kIu0iCiM9SezOGtRGFfv_ICyuO5fBO9iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسامی شهدای عملیات ضدتروریستی سحرگاه امروز سراوان  روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه:
🔹
در عملیات سحرگاه امروز حافظان امنیت که بر علیه تیم‌های تروریستی، در شهرستان سراوان انجام گردید، تعداد ۳ نفر از رزمندگان اسلام، به‌نام‌های «مسلم فاضلی»، «میثاق ثانی»…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/689317" target="_blank">📅 20:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689316">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc3852da87.mp4?token=Xos6TAZZ2Ty476ZuSJ3lYjujSlK3eiIa8qxfdYjpM8B9OjsBCFqz2XTCgq3YfuoXwGZDfgBiSfT1f4MUfGV7D5KQxljeIh_eOILWeGg1vjQr_HTkDXq9Q_ahuKYVYJk3KBphQZSDZelshycOurFNsP3iEw0FEswG4XiGF7HT4O5P036sFQY82VEfQpHZHo6Xdooo9NOBjFWzSXEJ2WQELWDs8oq122jPFUc7oISHA8Jj6FSogsMdqBo76x9TCwuuFD149czm_5OwY2EnRT4q1ff4ZlIJcyekWJIIAi1Cwpxq7bXEMSgqIvkljyR6VtDD221dYnPCSym5WP5v6dwsVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc3852da87.mp4?token=Xos6TAZZ2Ty476ZuSJ3lYjujSlK3eiIa8qxfdYjpM8B9OjsBCFqz2XTCgq3YfuoXwGZDfgBiSfT1f4MUfGV7D5KQxljeIh_eOILWeGg1vjQr_HTkDXq9Q_ahuKYVYJk3KBphQZSDZelshycOurFNsP3iEw0FEswG4XiGF7HT4O5P036sFQY82VEfQpHZHo6Xdooo9NOBjFWzSXEJ2WQELWDs8oq122jPFUc7oISHA8Jj6FSogsMdqBo76x9TCwuuFD149czm_5OwY2EnRT4q1ff4ZlIJcyekWJIIAi1Cwpxq7bXEMSgqIvkljyR6VtDD221dYnPCSym5WP5v6dwsVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتفاقی باور نکردنی! جیرجیرکی که میلیون‌ها سال در دل کهربا زنده نگه داشته شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/689316" target="_blank">📅 20:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689315">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپلتفرم شیدا | SHEYDA VOD</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odA7QlXf0OtqPuD90OFBKFL_4aADGPAkHK88tJN4e_yjZVJetRCs0uHDTQZKbSeIrWdF__d2RKx_ZvwSypCJQgvhPWVgLmvv0dUQ0ggVeJ9cJkpj9Cw9cu861kDq9_KUjbkT_Vt_MrgY-Ns4CZXEQ_VU2h1dxmq4opSbHWQ7rbTfr-GNKuGA0-Oy-9PHyHuGoDtvaMjBw9wpHwfS1q2TGdxVmYdvZL0-VVro7ieSLnKEaXWFdpQI6DcZQK-IrGdXur_6AJFhpBduhZBAg0S89aGNaDevLCRcOHVotL4N6H-lgzP-Bp-1BKI9lB_nPCxnLqDWYoXNanAfGEr2er-3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با روز ملی سینما؛
تصویربرداری «ده پهلوان»، قصه تازه حسن فتحی در عصر صفویه آغاز شد
تصویربرداری سریال «ده پهلوان» به کارگردانی حسن فتحی و تهیه‌کنندگی زینب تقوایی از بیست و یکم شهریور همزمان با روز ملی سینما شروع شد.
به گزارش روابط عمومی شیدا، این عاشقانه تاریخی به نویسندگی نغمه ثمینی و حسن فتحی، داستان خود را در بستر دوران صفویه روایت می‌کند و نخستین سکانس‌های آن در منطقه پارچین مقابل دوربین رفته است.
در نخستین روز فیلمبرداری، محمدعلی مشکیان، مدیر پلتفرم شیدا، و مصطفی شریفی، مدیر محتوا و استراتژی، با حضور در پشت صحنه این پروژه، از روند تولید بازدید کردند.
«ده پهلوان» روایتی عاشقانه و دراماتیک است که در فضای تاریخی عصر صفوی شکل می‌گیرد و یکی از پروژه‌های مهم شیدا در حوزه تولید آثار نمایشی به شمار می‌رود.
جزئیات بیشتر درباره داستان، بازیگران و سایر عوامل این سریال به‌زودی منتشر خواهد شد.
@sheyda_vod
www.sheyda.com</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/689315" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689314">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
معاون برق وزارت نیرو: احتمال قطعی برق در زمستان
معاون برق وزارت نیرو:
🔹
ذخیره گاز تا زمستان به ۳.۵ میلیارد لیتر می‌رسد، اما به دلیل محدودیت‌های گازی ناشی از جنگ و آسیب‌های جنگی، احتمال قطعی برق در زمستان زیاد است./ جریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/689314" target="_blank">📅 20:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689313">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a04a3913a.mp4?token=qNpIN77pORhNbwSIHRGzBq5TjO25ixRTD7IIi3wlLk4j3WnxLvCAyMee3rAI2dWSGk-Y56WHvvQFx7_reb-W45Eqr0v-0Au4S8uQIdXDHH59wSMr_rPIhQInd5KAaPsvn8UfQQGFwsdiLh3-Cip3_BGjn8fjBfh-hMTiH6TUx1Boe2wYeGCHG8BdhHb63gGav9aBO5npdDcuweLf1KLbCO78qkMo9jOiPLn4v1XHuY83pw2QEt0UQqkBbuKe39e_WoabkRBn44mT4Ud1k8TispKyAej81h33V0S5OerI3_QCDh9CgdNg98_qn8MQLKFK_wttJi9l6OLjyZtZoF61jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a04a3913a.mp4?token=qNpIN77pORhNbwSIHRGzBq5TjO25ixRTD7IIi3wlLk4j3WnxLvCAyMee3rAI2dWSGk-Y56WHvvQFx7_reb-W45Eqr0v-0Au4S8uQIdXDHH59wSMr_rPIhQInd5KAaPsvn8UfQQGFwsdiLh3-Cip3_BGjn8fjBfh-hMTiH6TUx1Boe2wYeGCHG8BdhHb63gGav9aBO5npdDcuweLf1KLbCO78qkMo9jOiPLn4v1XHuY83pw2QEt0UQqkBbuKe39e_WoabkRBn44mT4Ud1k8TispKyAej81h33V0S5OerI3_QCDh9CgdNg98_qn8MQLKFK_wttJi9l6OLjyZtZoF61jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۷۰ سال تکامل کامپیوتر، از کامپیوترهای قدیمی تا ماشین‌های آینده
🖥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/689313" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689312">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تصویری از خسارات وارده به پالایشگاه جیزان متعلق به شرکت آرامکو عربستان در نتیجه حملات یمن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/689312" target="_blank">📅 20:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689311">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff5e01ea0.mp4?token=KXxdfMab94qNoZ5AeC45an4I4iAb62LGGnxVBxcYtvGk_bOnhSNmHh27Kn0J8Ia8SNnipuAM5HQOPoxBZKamir0JwwXeQ3TiKUZGpHIxfs-qA4RzNKu-J2FPC1cCoGwFm-ckmRhC6sb_yYZfXcSKdlWT87_S7HBXlW1pqapBDroN5r4GvlbLdaRNWYpm2Twg_ubkXsw7lTkSnmmq_M4XFMX5vrE1kClKGAaeFXsSFZqW1ne0clzUYaUlYlzJBNxSrRiSMZ8bHkYrmYn0nREWPRJLuRopfPfQRKbYMP8TYTX2GRBZ6lQC9cftFhToSLI4mmPVRqkVVkpiKWSzHUWIcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff5e01ea0.mp4?token=KXxdfMab94qNoZ5AeC45an4I4iAb62LGGnxVBxcYtvGk_bOnhSNmHh27Kn0J8Ia8SNnipuAM5HQOPoxBZKamir0JwwXeQ3TiKUZGpHIxfs-qA4RzNKu-J2FPC1cCoGwFm-ckmRhC6sb_yYZfXcSKdlWT87_S7HBXlW1pqapBDroN5r4GvlbLdaRNWYpm2Twg_ubkXsw7lTkSnmmq_M4XFMX5vrE1kClKGAaeFXsSFZqW1ne0clzUYaUlYlzJBNxSrRiSMZ8bHkYrmYn0nREWPRJLuRopfPfQRKbYMP8TYTX2GRBZ6lQC9cftFhToSLI4mmPVRqkVVkpiKWSzHUWIcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ در مورد حمله به خط لوله نفت عربستان: به احتمال زیاد ایران مسئول این حمله است    ترامپ:
🔹
جنگ ایران خیلی زود پایان خواهد یافت. جنگ ایران احتمالا پس از انتخابات میان‌دوره‌ای پایان خواهد یافت./ حوثی‌ها نمی‌خواهند با ما بجنگند‌‌. #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/689311" target="_blank">📅 20:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689310">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df0873e00.mp4?token=tby1pHCv-LC7lVBKVxizKizBYur-3tB1rKlFaVlEDCaGPgIzrSebiz6k12fVCIDlZI30g_jgnBd7yZ7ZZlijbV2tvloRsUGkjl8FIMtCuoo0-AQXz002Xy8EhB78bgQHjddy3mV0MtINdNGM2PCkSB8DQd18fXreescWNIfQUyHgFzM_40FGai6Oo3p5JL5kJLhgm-Ou_8oQpnUtOonp7HqhLs_Q9M7tM91csEsxQpwha_thyZnX2BY58TdeDZkxQWfIkefmc18PesOm8uIp1XpMqRKBttD2X4lulohIT3VjVjojO_FhIBqU1bYWW_vc-xqzEO7Sddvamvurh6eJ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df0873e00.mp4?token=tby1pHCv-LC7lVBKVxizKizBYur-3tB1rKlFaVlEDCaGPgIzrSebiz6k12fVCIDlZI30g_jgnBd7yZ7ZZlijbV2tvloRsUGkjl8FIMtCuoo0-AQXz002Xy8EhB78bgQHjddy3mV0MtINdNGM2PCkSB8DQd18fXreescWNIfQUyHgFzM_40FGai6Oo3p5JL5kJLhgm-Ou_8oQpnUtOonp7HqhLs_Q9M7tM91csEsxQpwha_thyZnX2BY58TdeDZkxQWfIkefmc18PesOm8uIp1XpMqRKBttD2X4lulohIT3VjVjojO_FhIBqU1bYWW_vc-xqzEO7Sddvamvurh6eJ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بوی سیر روی دستات مونده؟
🧄
😵‍💫
🔹
با این ترفند ساده چند دقیقه‌ای از شرش خلاص شو!
✨
ذخیره‌ش کن که یادت نره
😉
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/689310" target="_blank">📅 20:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689309">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی فیلیمو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6244a14dc9.mp4?token=UnZVn2W421nURZGQy6sFRnPT_4imYgA880G8u4gIKh2df2S-BaVwkiuDA-3Pz4I3x-pGlo7DMTRytcN_wJ8h7FWi-TQstHN0lt6S29sdg_yq_fInwKIKg6lWtMuiNNKd7sOxqlAdvuwLYQojO4QDrY7-qdoFR6wwyC3AFYxCJfHTFi_Ud7NamfzVeykfBc7O4175k-VcsfUdSu2MjoHcVUvHIXd4tzF0IaYMAyoVhas-afpN0EpscSjRjHoWkBjchFqzi-SsXePwR4fUg0llgfHoekrXnxB1e5u95kpV2l1vGA10EHO_mQezGGc_NnRLZxw-Z6jdxnj-v3wQwI0ifKTsEtiWK0nh__3XWnR-CUgn9kCPrGml-rcqBPUpYLqzlaaSOsXih6WVmIJER3p8-d5YbToYaP9gvOt0EYh6TWEIiIykbElPyMTUg4N4w2nCcCu2y-0DDbWtYonUxaXHuQcDaClDwnon8WgfH5Z_j-8-F3pQVqlXt-a9J4UVDBeMTvm-CtwOZcw95PdQjBOAJ7rUe8a6NfNVpKjWPeheXe9WvVOoffKM_X_W1tidcmAKfvHcGGIZGIKSUngaaNvQIHSU8VaMxW_Di3RIC09gX64OLdDLYGlxxrELDqsNnL1PZy6SJOHDQ68CAxlG4Df_asqFUyrP4N3GbhMArYXm0So" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6244a14dc9.mp4?token=UnZVn2W421nURZGQy6sFRnPT_4imYgA880G8u4gIKh2df2S-BaVwkiuDA-3Pz4I3x-pGlo7DMTRytcN_wJ8h7FWi-TQstHN0lt6S29sdg_yq_fInwKIKg6lWtMuiNNKd7sOxqlAdvuwLYQojO4QDrY7-qdoFR6wwyC3AFYxCJfHTFi_Ud7NamfzVeykfBc7O4175k-VcsfUdSu2MjoHcVUvHIXd4tzF0IaYMAyoVhas-afpN0EpscSjRjHoWkBjchFqzi-SsXePwR4fUg0llgfHoekrXnxB1e5u95kpV2l1vGA10EHO_mQezGGc_NnRLZxw-Z6jdxnj-v3wQwI0ifKTsEtiWK0nh__3XWnR-CUgn9kCPrGml-rcqBPUpYLqzlaaSOsXih6WVmIJER3p8-d5YbToYaP9gvOt0EYh6TWEIiIykbElPyMTUg4N4w2nCcCu2y-0DDbWtYonUxaXHuQcDaClDwnon8WgfH5Z_j-8-F3pQVqlXt-a9J4UVDBeMTvm-CtwOZcw95PdQjBOAJ7rUe8a6NfNVpKjWPeheXe9WvVOoffKM_X_W1tidcmAKfvHcGGIZGIKSUngaaNvQIHSU8VaMxW_Di3RIC09gX64OLdDLYGlxxrELDqsNnL1PZy6SJOHDQ68CAxlG4Df_asqFUyrP4N3GbhMArYXm0So" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پارسا پیروزفر و علی شادمان در
#سرخ_و_سیاه
سریال «سرخ و سیاه» به کارگردانی آیدا پناهنده و با نویسندگی ارسلان امیری و آیدا پناهنده، به‌زودی به‌صورت اختصاصی در
#فیلیمو
منتشر خواهد شد.
تهیه‌کنندگان: محمد یمینی و محسن خباز
@filimo</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/689309" target="_blank">📅 20:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689308">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
موشک‌های رهگیر آمریکایی به‌شدت ناکارآمد از آب درآمده‌اند   ویل شرایور، تحلیلگرآمریکایی:
🔹
مسئله فقط کمبود ذخایر نیست؛ واقعیت این است که موشک‌های رهگیر آمریکایی PAC-3، تاد (THAAD) و SM-3 همگی در عمل به ‌شدت ناکارآمد از آب درآمده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/689308" target="_blank">📅 20:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689307">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdZc-h80NJtXOUCGNPIvTJByxAkUd8wZZgXxUfLQovR0fp-O1zTD-_kwMD7QH1gHd5o-RWCdG4I0s3wYY0uKHKzYj4td0BtKfR6uyZQY1mSQSlo8ixAUOmjj4pJUfU4Pp3H1r4axIuQIofVVJF1V0-cvapt7OcRTvaWEZ4QB2GnzhiFkY24vap_P0j3nl3Br7FEGQ0PFE-59PpBel3x_Y23bqrvow5WYdY1bCRov89fdGyp4JXQ-3eTH06n3OMX6GO9nyycJUulZ3rpqaZm3fY-ElHFTwG4mFo_acFG3NAvUgbHJ0-9LbAD8WQphSF1JHSAZorbRepAHw9FMePc-rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابر میانجی
🔹
در حاشیه نشست سران بریکس، شی جین‌پینگ با اعلام آمادگی چین برای میانجیگری میان ایران و آمریکا، پکن را در قامت بازیگری تازه برای گشودن گره جنگ تهران و واشنگتن قرار داد؛ پیشنهادی که می‌تواند معادلات دیپلماتیک منطقه را وارد مرحله‌ای جدید کند.
🔹
هشتصدوپنجاه‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/689307" target="_blank">📅 19:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689306">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e69b20bb2b.mp4?token=PTyTqF0hbAXQ3RdJsMuIe7INvKy6UKJPY4JT_gIgM9jgd1EOvtOO0StcS6MF_qtIZYhV9clV23d-fptgRMZ0YLzLlKHRao9GIv2u87b3UqfU6lH-iLnSm09TtpLXnxXYP74TSVCA5PMipxvfYQ6RiCF8tZWgkigWB7t4kt96tnp2VeXcD_biwYt2cjxMFHNWyRuTrJk50TP_i4_GRuELlRDbNhJ0rs9hdxHxfF1EUGigq5zLSALHPiqjmyamSQ5xtHFiU9FxYd0XeYJjpN7rANH_ieuQngv6vpKmx42aMh7okRrzJtjbwBVCXczUqxuVF-4bclE0Lc4FuAXmqJHTnzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e69b20bb2b.mp4?token=PTyTqF0hbAXQ3RdJsMuIe7INvKy6UKJPY4JT_gIgM9jgd1EOvtOO0StcS6MF_qtIZYhV9clV23d-fptgRMZ0YLzLlKHRao9GIv2u87b3UqfU6lH-iLnSm09TtpLXnxXYP74TSVCA5PMipxvfYQ6RiCF8tZWgkigWB7t4kt96tnp2VeXcD_biwYt2cjxMFHNWyRuTrJk50TP_i4_GRuELlRDbNhJ0rs9hdxHxfF1EUGigq5zLSALHPiqjmyamSQ5xtHFiU9FxYd0XeYJjpN7rANH_ieuQngv6vpKmx42aMh7okRrzJtjbwBVCXczUqxuVF-4bclE0Lc4FuAXmqJHTnzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سازهایی که هر روز صداشونو میشنویم، از کجا اومدن؟
🎶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/689306" target="_blank">📅 19:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689305">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNZXUm_MF2oXc7IR6R3mN8P9htbgQ-bNfZTKxlpnid3xd-u6sgzBbhdwsWMvk3liONmcO0FGnhp6Ve6BfbrV10zWaiK9CUjCyRnWQlooECmdHtjDc_7O8WwwVvPo94u3vgfpinlniHEufjpTSli1FbdazHJX3ploOXuGeYi6j9HVJEgOzv5ak5duupvd4EFoPQ1kx7NAz3UuEV83yGdnD2sOK85_YorPfEhGeeET2oqTJ5yIwMUGgXvZeAfMw7kzt5HvrXczRUMz8wST0JzaVX3joX1jUlkAD93KuH22QVDo07wAPEOB4hWapgjop1LScGoQ2QDsO_BefZoLnG3tpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر فرد در ماه چقدر غذا خورده است؟ | ایرانی‌ها غذا را از سفره حذف کردند؟ | سفره ایرانی زیر فشار یک دهه شوک اقتصادی
🔹
سفره خانوار ایرانی طی بیش از یک دهه گذشته نه فقط کوچک‌تر، بلکه به‌تدریج فقیرتر نیز شده است. بررسی آمار هزینه و درآمد خانوار نشان می‌دهد میزان هزینه واقعی سرانه برای خوراک در سال ۱۴۰۳ نسبت به سال ۱۳۹۰ حدود ۴۳ درصد کاهش یافته است؛ تغییری که تصویری روشن از افت قدرت خرید و کاهش مصرف غذایی خانوارها ارائه می‌کند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3244613</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/689305" target="_blank">📅 19:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689304">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAo3OxkJ3rq34pCzFPz5Sq0hreDaL70cXKGtGZz9nBaLKeqXbuwZBx1wwpw2iD6M-_hdl3KRaYJCnnGXsufYPYhRwI5vn29n5kraeX8R1U3VqPVa633JaLjZyrNrEad4ufOpQt7dQ-01LLIMPoHIoJBpS-ik6QZjgMh4AFZ92yt7ZerK0hrDmjE-ZHLKSk3uLcEiZux19o1D4iPSlXOkL1MofZ7zkeBoaTa0XYAa_vwxn9phFwWej9cZAY9nZh-JE8Wx11q-MwKIePgnhR6A5lQnu6eLMJzhhXNf8BsBYovW3N_TfkNMl_WqUzCkeHfdeTgf-QTa8q7S755sD80_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جبهۀ مقاومت در کنار ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/689304" target="_blank">📅 19:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689303">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
جزئیات جدید درباره تفاهم نهایی ایران و عمان/ تنگه هرمز با این تفاهم باز نمی‌شود
منبع آگاه:
🔹
تفاهم ایران و عمان اوایل شهریور نهایی شد و به زودی با حضور وزرای خارجه کشورهای حاشیه خلیج فارس اعلام می‌شود.
🔹
مسیر ورود به خلیج فارس کاملاً در آب‌های ایران و بخشی از مسیر خروج نیز در آب‌های ایران است؛ تردد تحت ترتیبات ایرانی و مسیر جنوبی بسته می‌شود.
🔹
این تفاهم به معنی باز شدن تنگه هرمز نیست؛ ایران ۷ شرط به آمریکا اعلام کرده و تا اجرای آن‌ها تنگه مسدود می‌ماند
./ مهر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/689303" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689302">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ow-AXOjl87poSgRaMrIh0HORxRbvaWnLH0l_zItnL0l6EFBesJeSEPW_OxcMBbEItjadKInIy4BNC9_79A_DCucl-gAXg80Yq-wdTbj4uP3YFN3PATww-hjPOx9eHb6NlxYWEtZM6agTMaqBGP0MhctltnwFfyOlSdEoS8tH-Iz2UH_s29MAjLsPohUoSQF1K_0F26Zg5ob_5keQCNMItZEvF-w2dqJKzAtvTdYidxPVSJoZ9LsRZerMIN5PaBY-cWRiwUDEqCPvbhNQc3pJthaIrNpLeYy92s7bVI6vNDfn44wVdzVpfyntx2eZxwpDYG-sEcA4QEsZ7-dLW5b13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
قاب ضریح امام حسین (ع)
جلوه‌ای از عشق و ارادت به سیدالشهدا که می‌تواند زینت‌بخش دیوارهای خانه و محل کار شما باشد.
این قاب با حال‌وهوایی معنوی و طراحی چشم‌نواز، یاد حرم مطهر را همیشه نزدیک دل‌ها نگه می‌دارد.
✨
مشخصات محصول:
▫️
ابعاد: ۲۵ × ۳۵ سانتی‌متر
▫️
وزن: ۶۹۰ گرم
▫️
متریال: پلی‌استر و پی‌وی‌سی
▫️
طرح: ضریح امام حسین (ع)
▫️
کاربرد: مناسب دکور مذهبی، هدیه و زینت‌بخش منزل یا محل کار
💰
قیمت اصلی: ۱ میلیون و ۷۹۹ هزار تومان
با تخفیف ویژه : ۱ میلیون و ۵۵۷ هزارتومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/689302" target="_blank">📅 19:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689301">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOagFcrlEeQG2Jg5ElLvG1Gx2lTO82UowAr6ejzlW2wB6sUYn7zpgRmwBAZJ5sK3JRTOkHUE0XcwBdZ-az-YIXSWbipb0QJqLPRni_0n1X1aRWa9BoeNimNFdLdpL6-FfcrCwLM1lEv01xvvJJeMJ7gptjA_pW-5qwIbABMhlnpWE8bk0B5EM7k571H_CHbyMGjDhIcOyTlqJYc0m4HN3vFizQBbyWysN8YoDTIaKs23xVWK7PNmaC0xOcne4rSuJACfrUSNPUdFUqZV1cgNvHEKSdyJAQ4D1KVoictQZ6O9TTmlBAGJcesPwnvS1gBEYasIu79wi-OFFeLl98T9pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از فرح پهلوی در حرم امام علی(ع) - اواسط دهه ۵۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/689301" target="_blank">📅 19:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689300">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
هر شهر، بخشی از یک روایت ملی‌‌ست...
۹۸ سال کنار ایران
🇮🇷
📍
شیراز
🔹
شهری که فقط دیده نمی‌شود؛ در آدم می‌ماند.
🔹
در کوچه‌ها، در صداها، در خاطره‌هایی که از نسلی به نسل دیگر ادامه پیدا می‌کنند.
#اعتماد_می‌ماند
#۹۸سال_کنار_ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/689300" target="_blank">📅 19:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689298">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q40E-N39Ziv3WHHVm47bcLaqzxc09wLeeLvkhO0faBsRgOu0Bqk-xMyJryY0rExRJJxtpVEODwP5cUWRyw8FXcPghJcqgxfl_4GEvmN-yY21_iAZbcHvm2FR_HSdZgGmYvC7kwvY8lRk5AMPux_8k64XBcIj6SFdRRKNo4hUmda44TRVv0Onp8dFqDHPhnTjTMcIo7eShldvabqTXMZ9-vkPMIo4qKOWq97fLU11rXbsPNlS7bpniYDjaWAx9z7o728WuwKcBPfOQd48ayXlnQtx8sF7hoz2M--j_V45Qh2vBDgW_msKlB4O_arFK_ZfPKGudAMkXgCXqH0ZDhXS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیگر نیازی به برنامه فشرده‌ساز نیست؛ ZIP بومی تلگرام دسکتاپ آمد
🔹
در آپدیت آخر تلگرام دسکتاپ می‌توانید بدون نیاز به برنامه جداگانه، چند فایل را با قابلیت داخلی تلگرام به صورت ZIP بفرستید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/689298" target="_blank">📅 19:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689297">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ee7015ef.mp4?token=sxz6f-wSu9ZpUl2saRPkwXGyNpEi3kBzZTpvAb-eOQkQ6ef30oCd8ZKe1SgrH33MlGSodTxPmnnoYacZUhAJ2LggP2COlDsLaaexjSSnyy7bdwyZdHIIjW4GrbUL6gKLrvnwEMFWI4Dxb3tYXBDGdXnl1fRWOAgZgNhkan30_3MaXCmUW8BXsRwjwIGyWXL9ETYZHI_To4-h1PvSave-zY3sdO1GERI8cgkdF_-FdxKLiHqkW2pRnRT2tny8Rm4UT_uhR53SW66HoOm_6Aa8CcktZmVqk09GqqopwtmZT52gC55Wi8oxqDQAr9JN21jCZ-qcWymHO4gIXt9l2HGYGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ee7015ef.mp4?token=sxz6f-wSu9ZpUl2saRPkwXGyNpEi3kBzZTpvAb-eOQkQ6ef30oCd8ZKe1SgrH33MlGSodTxPmnnoYacZUhAJ2LggP2COlDsLaaexjSSnyy7bdwyZdHIIjW4GrbUL6gKLrvnwEMFWI4Dxb3tYXBDGdXnl1fRWOAgZgNhkan30_3MaXCmUW8BXsRwjwIGyWXL9ETYZHI_To4-h1PvSave-zY3sdO1GERI8cgkdF_-FdxKLiHqkW2pRnRT2tny8Rm4UT_uhR53SW66HoOm_6Aa8CcktZmVqk09GqqopwtmZT52gC55Wi8oxqDQAr9JN21jCZ-qcWymHO4gIXt9l2HGYGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طریقه جالب جابجایی جرثقیل‌های غول‌پیکر؛ پشت پرده پروژه‌های عظیم چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/689297" target="_blank">📅 19:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689296">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: باب المندب واسه همه کشتی ها باز هست فقط واسه عربستان بسته هست
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/689296" target="_blank">📅 18:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689295">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nj3Yz1Yq5QJhNVkO9R4r4tPTaOWDpopDBw8f-FLP5A_oVtGSWVaIk7ojEKZYfGpNYAGwpyo29dA891T4xTe4a2Agj_cysFA6UvHd02cNf7jhGhPStPkyc2tXSOm_4Oin3OpQl98pbRtfiqZVSw2F60LnVBnkzZYKfVLPgChrucMyMw7uDxbX54xC9hwMGjUiPX1CuiYunpWzIgNfXsD7BPBK1YL4fnPDkwRhNLAdPHI2pxQv7CTwM2ir_cFIjCvJ0MlF06RintWjkmjlIT51uLqxnxRv-Ibw_bfSMVjlyr9uLO2d0j7pSYeGVErmx7UKEk4e1m3a9zrMszrTIwRKhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا:
فقط در ساعات خاصی از نفتکش‌ها حمایت هوایی می‌کنیم
🔹
پرواز هر ساعت هواپیمای نظامی آمریکا برای پنتاگون بین ۲۵ تا ۷۵ هزار دلار هزینه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/689295" target="_blank">📅 18:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689294">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDjJrBn3QNDIMmkuzppphN_JOj4i5TxO1vDllWnjgKEsi-P7FgZa6eW4HFWqQriudLyXqP5Y3qIPaCla-f1EkJQg-qEBOlvAB49N_JvdTu71y3H12OLDj9madGPB94VEkma0cloQ-StChg5t0lI9K69ib9DdazArPyq04GjX5VEnxx110q0IDs0RMvOd33f8eDxxqFPnsn49K6PaYH2VxeX5JPYo8dMqz162AnYGz7-pG4J_V9ouAlpGbLJpWSVzWJZH8-DUC7Hgu8IRFyCdBlxPzRUo_NELCFk92zPziX6PQYCosRZ7bvoalibuZUrImOEinaNE4WPWvcmulQpaFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو میلیارد تومان جایزه برای بزرگ‌ترین نبرد گیمرهای ایران
🔹
همراه اول پنج هزار گیمر را به رقابت سراسری FC26 دعوت کرده است. این تورنمنت در دو مرحله آنلاین و حضوری برگزار می‌شود و ۳۲ بازیکن برتر آن به فینال تهران راه می‌یابند.
🔹
قهرمان مسابقات ۵۰۰ میلیون تومان جایزه می‌گیرد و به نفرات دوم و سوم نیز ۳۰۰ و ۲۰۰ میلیون تومان تعلق خواهد گرفت. هر ۳۲ فینالیست هم یک مودم 5G با اسکین اختصاصی گیم و یک سال اینترنت هدیه دریافت می‌کنند. همچنین برای تمام شرکت‌کنندگان تأییدشده، بسته ۱۰۰ گیگابایتی اینترنت در نظر گرفته شده است.
🔹
ثبت‌نام از طریق اپلیکیشن «همراه من» انجام می‌شود. اطلاعات بیشتر و قوانین مسابقه:
🌐
mci.ir/mymci-gaming
http://mci.ir/-F8KLRA
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/689294" target="_blank">📅 18:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689293">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
رئیس انجمن واردکنندگان گوشت: قیمت عمده هر کیلو گوشت وارداتی از حدود ۱,۳۰۰,۰۰۰ تومان به ۱,۳۵۰,۰۰۰ تا ۱,۳۶۰,۰۰۰ تومان رسیده
🔹
واردات گوشت متوقف نشده و از مسیرهای زمینی ادامه دارد/ علت افزایش قیمت، رشد نرخ ارز اختصاصی واردات است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/689293" target="_blank">📅 18:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689289">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKuP3BujFyCToSR1RjwRVEMOxN-S2blHethwW-bKChyZvzecqiSZmLrGpLkKO-kfCRDjlyXS1AKtvxuJroN75zvcTYg46IYFdtkiwV_EmXst0tr2v6pzvfxalcOnGEB0cs-ZqByhLp-KQhseYJX2sh-d2RKbwRAYgvXmsxElLj3uPrjVwxwzHA5FKvUKxCuZlk0equ6TkgIQm-GB38-ErmdZd4SFPGFQFPbT5BHYMy4YDVUutRBzx0pyO_GSu9TgkILEE-qodjQSEXNnxvCY8WiYp2VmXsugw1SuPtWxUW4erjNMK-QJtrE-1RhF3i82hTWxXbLJJVFaBj_07DDdnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lXVxJQGgm5i8BwIIhH-T7J6j3iwDvG8li8HQ95eZs-HUe-CsZU6nd9o_AsitGxJLv-aJAq4iSkKTsOt4XeYLljOV5cg-8irW5HGRqGCasfq4PEonL0bwQ_Kmxu24biKL5Ev-l9Z4UUPk4FMNn4Dm6uzo0_IOI10tiELwmDvqenT2NqT8-XnwdW-gy-LS0EUSKHUV9uisWLI0WAqytDdTmnlBWaVe8VJ5zoUeYgeH8sfVZJc5xOHeloB4u1N6YDvgIsyuFU49xj0BdHE8m2MiLQdtGRDdHuh1xKVsIw5nix_C776fIGaJdW96fbo4Sfy3fpllKuQX5eDH_yq5E9DBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BF8jw1Bx00Hvz2jOBXKoRi5SA8PfbS-EiJOwU9mj3ddVXFA5mt3a1mLO42jqe3y1qm5RZbnX1NVk4J4sP_SpbsCltSG3cajxCrRh72SJFUJ9q9PI2pJU2V1IkkGaBYxjYkM7J6KkTBUj39FEQ6nQ96-9cvgxpGuqhafKCGcC8O3xxAex2DVmftkxhZAQ0ynZpDgPy2pAr9Q9WXIf4Xfxp4B7qsbWBmC9yu5JKC_NpQiVOmUoxPLrJrDeB-vrwg3NcTfgO1OZgOAHMgon7G1hWMxOwhJN-fZv4jAvTf_rLQhU3dG_GPyaNPDso_8ftJ3PmlGCa9XzxyW2R1C6oZXRRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر منتشر شده از کشتی‌ها و نفتکش‌های ایرانی آسیب‌دیده در خلیج فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/689289" target="_blank">📅 18:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689288">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khPzz5oGzHRkqr9nYtu0qBgbcIdINt16eEnMHEyRXSZG-tPq0bhxnA1YE1BwZZKKuYBLjiEMFBVYEllzHg_dEAH_exjOtxlNLNe9V_XzsFDxuq0tjnGanlpbOMVCF3lHUF04M7HliqT4xVrFH-Fa2vnZFICx5RW3HVT1q1TWbXxEULCPGNUS4ehFU76P6vcFy0aLbyTiSQ7DFwEto6QQRUTSKBK35iErykbSOF1saNS4crFPMPP4pngNjJmD0LRxjzv3iOsO0auhPhvbrjsI3ouulWCEjV3WwK-zJxyJZb3_3yte-gZFkfxt9j2wN4kGk4mmH-jLYuV4_K8dBeOgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همراه اول رکورددار رومینگ بین‌الملل در ایران
🔹
دسترسی به خدمات ارتباطی در سفرهای خارجی، یکی از مهم‌ترین نیازهای مشترکان تلفن همراه است و گستردگی شبکه رومینگ می‌تواند نقش مهمی در تجربه ارتباطی مسافران داشته باشد. بر اساس آمار بهار ۱۴۰۵ سازمان تنظیم مقررات و ارتباطات رادیویی، همراه اول در حوزه رومینگ بین‌الملل عملکرد بهتری نسبت به دیگر اپراتورهای کشور دارد.
🔹
همراه اول با ۳۳۵ اپراتور خارجی در ۱۴۰ کشور قرارداد رومینگ دارد. این رقم برای ایرانسل ۲۹۴ اپراتور در ۱۳۲ کشور و برای رایتل ۱۹۰ اپراتور در ۱۳۴ کشور اعلام شده است.
🔹
همراه اول هم از نظر تعداد کشورهای تحت پوشش و هم از نظر تعداد اپراتورهای طرف قرارداد، در جایگاه نخست قرار دارد و مشترکان این اپراتور در مقاصد بیشتری امکان استفاده از خدمات ارتباطی را خواهند داشت./ خبرآنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/689288" target="_blank">📅 18:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689286">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8edd44284.mp4?token=KL4bJVxNczVd0mrMlnsfUiMr4kXOVuMlqRzf4Mtp6q49KykjBhLd0jFMW4bL32x2yvWWExdo9vzsEBdZ3r_7DCuUBY_w7q6ouetHhz136Oz_w6TL3ZzMcV7TeuoJv5AC-8BmZ22ZSFjlYFWIL_oQrpG8JIO2fYJL08xoP4qjG1pTIv-XKpPEGxAjMP1gUDiIVyTDkl4c4azN0sWtlbRnkTzMcUK1GhqsKY4TflaaKA-BbEDw11FDhcgqehjIUqBj1ZyPKlarSQqWH0SzZ2gZws_Hq_m-ONXXWCwgWsPaw98rOqpubDMQYNbNfuwv8W21kFeLGMQV9hVaa0xptiRhhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8edd44284.mp4?token=KL4bJVxNczVd0mrMlnsfUiMr4kXOVuMlqRzf4Mtp6q49KykjBhLd0jFMW4bL32x2yvWWExdo9vzsEBdZ3r_7DCuUBY_w7q6ouetHhz136Oz_w6TL3ZzMcV7TeuoJv5AC-8BmZ22ZSFjlYFWIL_oQrpG8JIO2fYJL08xoP4qjG1pTIv-XKpPEGxAjMP1gUDiIVyTDkl4c4azN0sWtlbRnkTzMcUK1GhqsKY4TflaaKA-BbEDw11FDhcgqehjIUqBj1ZyPKlarSQqWH0SzZ2gZws_Hq_m-ONXXWCwgWsPaw98rOqpubDMQYNbNfuwv8W21kFeLGMQV9hVaa0xptiRhhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا کنجکاو شدی وقتی دسته شیر آب رو بالا می‌بری، واقعاً داخلش چه اتفاقی می‌افته؟
🚰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/689286" target="_blank">📅 18:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689284">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aybXq_bX-B_-eFcC7DXfSugXt4HLLXvM4e7a1jxUQ6Fgdawyh6mloPb7GQ0GuIIWrx-4tZBSQYt-gmy40XN0_lpgp6EIdliFqOc5cXAjQ8g_ceYnP_6ftMRrKXS2SxHtj69KbPxJiMt9txiQdFNFgzudkQtKbfxKkiWMi3nMNUFGgoeDVJeEOOP-3klDuOIchFRNlx2WgOXVy_fY4a0rEXvDIpjicfpRyUTjGwFYLSfrFWdtXPlQVkr2pOdwbgGfidkU3wtvAJ7LI4QyT1jy01JGArBbD67b5qZBUdvP8LngtiiQYpIjmq9Tq4tNq6dwb_IshVzTkUprnhNev9Bkxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه: تعداد تروریست‌های به هلاکت‌رسیده در عملیات ضدتروریستی سراوان به ۵ نفر رسید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/689284" target="_blank">📅 18:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689283">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d622c836f4.mp4?token=sMxQg1fzhtpy_8in4CjnHAO-1-aQIPlQiPHcHJx-z5o-hQQwPxt3yavDxpVgUnUJyDLvo5jRPJY4hfrlUOZ5DUDvcXZmO3gAJG0YnGsHAIYde1dFB-3Spa-1vQdyilgjdsfYtVrTeeyTQztQSdpoMZzg174zQ0f0dLJ0gB4CGMiP2JVkIvz1xUtK8Q_5mXOQcqoRMf3pekfhRhN5WWbYI4KKz-rBFzxp71xYYceBXBwPoIbBK3sFNyNUnrxYzGAabKOSgN-3bC73pfhOl6w8_Ovped7IrmsnxmdZQPfN4D_18e01yAXLzLdTPiGEnO221Fjd7_l-gZi1CK2hFEfFVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d622c836f4.mp4?token=sMxQg1fzhtpy_8in4CjnHAO-1-aQIPlQiPHcHJx-z5o-hQQwPxt3yavDxpVgUnUJyDLvo5jRPJY4hfrlUOZ5DUDvcXZmO3gAJG0YnGsHAIYde1dFB-3Spa-1vQdyilgjdsfYtVrTeeyTQztQSdpoMZzg174zQ0f0dLJ0gB4CGMiP2JVkIvz1xUtK8Q_5mXOQcqoRMf3pekfhRhN5WWbYI4KKz-rBFzxp71xYYceBXBwPoIbBK3sFNyNUnrxYzGAabKOSgN-3bC73pfhOl6w8_Ovped7IrmsnxmdZQPfN4D_18e01yAXLzLdTPiGEnO221Fjd7_l-gZi1CK2hFEfFVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوشته جالب تیشرت موتورسوار امریکایی
دو مدل طرفدار ترامپ وجود داره:
🔹
اول: میلیاردرها
🔹
دوم: احمق‌ها/ حساب بانکیت رو چک کن تا ببینی جزو کدومشون هستی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/689283" target="_blank">📅 18:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689281">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgRIynlYI7HEAZAV98vSmOvuUdoMG5g9PMkABg8-SofpTNkeEldCgEatW5QwOoFQnWIgCwXECcTWFsg4_luiFhkOeXfgzUkeU-IXmUepXsIBKSKlSc7xk0pobge0g0frYkaM5QXkIiNeHytqz3-_VfaVPKJdDvHSw8mD8K9vRb8D2cD-t18Mop_qSxFOVkXI9gWUukWW9aVWa_dFWUWhaemjrsdAWuSLbqY3dpv59NVJFUF2ik8szNyRLw-88MhxrElITosnbvTFDTUZ_SB-yzHMK2Nr-3LO90Z2JIpytPSb8zTJGrprZePcSs3qHefuqXUQdIhSc32fKdSlk7B0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لغات کاربردی اتاق خواب به انگلیسی چی میشه؟ #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/689281" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689279">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
عراق با پیشنهاد ایران برای تحقیقات مشترک درباره حمله به عربستان موافقت کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/689279" target="_blank">📅 17:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689278">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
انهدام تیم تروریستی در سراوان
🔹
روابط عمومی قرارگاه قدس سپاه از انهدام یک تیم تروریستی در سراوان و هلاکت ۴ تروریست خبر داد؛ در این عملیات ۳ پاسدار نیز به شهادت رسیدند.
🔹
از مخفیگاه این تیم، سلاح، مهمات و مواد انفجاری کشف شده و احتمال افزایش تلفات تروریست‌ها…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/689278" target="_blank">📅 17:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689277">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae86cf3f01.mp4?token=BqzjclRVDZtVEZ1WCau-wZSKfbRrSzgxSkyv0kRMfWVHbB6KKggWIa8lQ1oIEc1cGNp1Yj_8oA8YsaLZWOSJp8CtM5OQG87t7wAMQogc2gKjKBfNNah5G01vn6Qc1nQIpHt9huwzJ_vFz6BaD-QlXM0hrhSpI5kHOXqSc7uFFAeqjABORMHLBxHPuJHjIC_ya0QzaAnA5YoWRZw1FQs7qUVEDXkhv9fKWihMn9tsmrDERGd-vymN4Pxso53f05hFEqEaw2C1IKqYtV5UHBW0xbdU8myctYEZLSRP-5ACpX_nnWtqjOwnSQTWlgUoB9PxZBr5Fzxv9dUoFu7Nk4mjgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae86cf3f01.mp4?token=BqzjclRVDZtVEZ1WCau-wZSKfbRrSzgxSkyv0kRMfWVHbB6KKggWIa8lQ1oIEc1cGNp1Yj_8oA8YsaLZWOSJp8CtM5OQG87t7wAMQogc2gKjKBfNNah5G01vn6Qc1nQIpHt9huwzJ_vFz6BaD-QlXM0hrhSpI5kHOXqSc7uFFAeqjABORMHLBxHPuJHjIC_ya0QzaAnA5YoWRZw1FQs7qUVEDXkhv9fKWihMn9tsmrDERGd-vymN4Pxso53f05hFEqEaw2C1IKqYtV5UHBW0xbdU8myctYEZLSRP-5ACpX_nnWtqjOwnSQTWlgUoB9PxZBr5Fzxv9dUoFu7Nk4mjgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیدا شدن جستجوگر مادون قرمز رهگیر موشکی تاد نزدیک مرز اردن با سوریه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/689277" target="_blank">📅 17:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689275">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
بقایی: مجموعاً ۴ موشک طی ۳۵ ثانیه به لامرد برخورد کرده‌اند / ما قطعا این جنایت را پیگیری خواهیم کرد  بقائی:
🔹
شواهد و مدارک نشان می‌دهد که جنایت لامرد قطعاً توسط آمریکا اتفاق افتاده است و در آن شکی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/689275" target="_blank">📅 17:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689274">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
بقایی: مجموعاً ۴ موشک طی ۳۵ ثانیه به لامرد برخورد کرده‌اند / ما قطعا این جنایت را پیگیری خواهیم کرد
بقائی:
🔹
شواهد و مدارک نشان می‌دهد که جنایت لامرد قطعاً توسط آمریکا اتفاق افتاده است و در آن شکی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/689274" target="_blank">📅 17:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689273">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51dc103e87.mp4?token=Qlb7OD_SyB3PQccGP821u1C9FXdk1WoYiHFI5dwxCZTGBfAvKV6fOcsS49Y61O69vODkzCKZIa_QdQosX-_KFdbUgWG7uakFlU4BkOUcFqo-EcmhoszFYkogwrFBQIKzmTBM5kdsgJjbEsLT1PTuyRpV78lZcqa_HoVClGi8c13bXV6rOQxlMpAtyUjJp5VLGPHxvExFWOwLaxN3DcsLSqF9fHeZ5D6s9L5b1TcuH7CFZ43r-sm_EXSHkqB-VsPon4-1w8PcIjwAwqVedqAFB6i8lN66ps6y4K2NETX5k5EUgC-xs3hsHg81DVrJNrYutO9iVp3faAAWaqQa2mfFnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51dc103e87.mp4?token=Qlb7OD_SyB3PQccGP821u1C9FXdk1WoYiHFI5dwxCZTGBfAvKV6fOcsS49Y61O69vODkzCKZIa_QdQosX-_KFdbUgWG7uakFlU4BkOUcFqo-EcmhoszFYkogwrFBQIKzmTBM5kdsgJjbEsLT1PTuyRpV78lZcqa_HoVClGi8c13bXV6rOQxlMpAtyUjJp5VLGPHxvExFWOwLaxN3DcsLSqF9fHeZ5D6s9L5b1TcuH7CFZ43r-sm_EXSHkqB-VsPon4-1w8PcIjwAwqVedqAFB6i8lN66ps6y4K2NETX5k5EUgC-xs3hsHg81DVrJNrYutO9iVp3faAAWaqQa2mfFnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از تسلط نیروهای مسلح یمن بر برج کنترل تردد کشتی‌ها در تنگه باب‌المندب در شهر مخا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/689273" target="_blank">📅 17:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689272">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
رویترز به نقل از منابع نظامی عراق: منطقه مرزی الطیب با ایران پس از کشف محل‌های پرتاب پهپاد بسته شده است./ الجزیره
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/689272" target="_blank">📅 17:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689271">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVvaiSXacQaevVpbBDZsTwzngF5XJ-CY1354mFzeFSMgbcBZCdgj6BD6YySWnLxKTgwKf6jOTOzJ5pr6HlhUMvNaMbeXtTQ0Qp-jAW9UT2XKwvqAtU8Kz_c5cONMvwjbTG4VR-qX59mEE9kVXyukZAH44WW3kasY7Zo0NAmO33LHu7cTky9PvwL9YYLXvkQXdkvKsBO1qdTG9wZvmCMuUbrids3aRLiCiEih7iN8bPd7_pbmBf2fQ-T7c-JP0hJxO_Y9LMOtsZHbrq82vRAgvSFA8ePbE44-bBAODQTUNVBe2cth0sOnJf696Yq6UarQUoHCsKjg_ClYHVWW8f-qXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مایک آدامز
:
نفوذ آمریکا در خاورمیانه اکنون کاملاً فروپاشیده است
نویسنده و فعال‌رسانه‌ای آمریکایی:
🔹
تمام شد؛ از اینجا به بعد، کار برای آمریکایی‌ها قرار است خیلی دشوارتر شود؛ ترامپ حسابی گند زد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/689271" target="_blank">📅 17:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689270">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-RulKQ3NddOVfnDIU56xcE_obhqS_41QT7gFUql6qsCXPEKHyyZNdhwzNzQ_xfHrfegqrLioQ0LD9MC7FVPJXA0JPG9dpCar_BkShBK4aX_g6ApmoQgT6Qngd_LFKSt6xkuksa3It9KUdebd776aeLN3WTZ42AsD8IluAR-cF_GODGMNNojYVaKVHUGRFRDzj_pn-rRBQ8UV6YmYHeRkbSAxnRvJf768yAvGX_RGhPpVodWb6VSXTrYTS6KbVRUgW5FNaSOgLrn60moI91oEIynHWDoX05Ld_fEhdiUJDueg7TCpIoHdsSaLsrjX9GpCQWpdVVBnZ-V11TKeFdyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ملک اجاره‌ای دچار خرابی شد؛ مسئول پرداخت هزینه به عهده کیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/689270" target="_blank">📅 17:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689269">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGxXq8jTHDtqPOzB1OQOG73v2LgNxzv8QFYnXHppZl0Tn-o5XeBz-Sz4rTThUyAGPZnXHE7MHM-Sge8mrSZLrSmE-b-2r9aMp2wODikhV4UvzH996mUECLoI55vZwrl8TKIp4RRkW2NmTf5lAaWvgcnyWMKaNHoHcaCbtRF9Y9hAxDpEvavcuVz1UvlVKYRbG8xENLNTSgTsTWokaKH4mEUerX_V-TWHDA1tmzq3K5YnEi1DByRCme0HktHeRYP7G8-FI3ftboV1ZD0prGY3afvZ4Ge-kfoN4nxqIoDd5JHmBl7T0CWcyfkglw4yZFRdlU2vDJj5D3jpbwCDQs8p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اجرای عملیات اضطراری برای جلوگیری از بروز خاموشی در صالحیه و گلستان
🔻
مدیرعامل شرکت توزیع نیروی برق استان تهران از اجرای عملیات اضطراری احداث ۳ فیدر فشار متوسط از پست فوق‌توزیع بهارستان برای افزایش قابلیت اطمینان شبکه و جلوگیری از بروز خاموشی در شهرهای صالحیه و گلستان خبر داد.
🔹
این عملیات با حضور ۴۰ اکیپ عملیاتی و طی ۵ روز انجام شد که طی آن ۱۸ کیلومتر شبکه فشار متوسط هوایی و ۲ کیلومتر شبکه زمینی احداث و ۵ کیلومتر از شبکه موجود نیز اصلاح و بهینه‌سازی شد.
🆔️
@nabzeetehran</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/689269" target="_blank">📅 17:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689267">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
مهاجرانی: فعلاً تغییری در نرخ و حجم بنزین سهمیه‌ای نداریم
سخنگوی دولت:
🔹
به‌محض اینکه منبع مالی پایدار برای کالابرگ تأمین شود، مبلغ کالابرگ افزایش پیدا خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/689267" target="_blank">📅 16:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689266">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQrDL3Xl60SQ2hNQ48xyeWAlvlrKyD9Y16CKdBaoXOXJC6nxb4L2kAsenMrrZlpPYA2Dq8ZbSrx3Ah0zUIp7dI2HpW0U-3SzgQCCY3q2XbD5Vn6kV5rInwm35S50iqfKoUJpmDncdzH8xfYsT2vBHrKGpL0D3hzPq0ipXk_ys3kT2NDxhSD7oCwc8FMgZi_gUXsFrbaYUiJ3SYc48k3aF2tBmE7mSgWr5zviVBnFCvLRNQd5BKmP_cNkjkKRVTHKkyjF0Tti-jtYSOu5Z6Mypnj30mkexqneJ70fcpoSRz42DqZQKwLgVsmYEEMdIzvwmwvw1ntI06M4Ah65M-u85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای کامل از بین بُردن بوی بد در خانه
🏠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/689266" target="_blank">📅 16:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689265">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
بحرین اعلام کرد که در نشست ایران درباره تنگه هرمز شرکت نخواهد کرد/ همچنین طرف هیچ‌گونه نشستی که ایران در آن حضور داشته باشد، نخواهد بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/689265" target="_blank">📅 16:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689264">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
شایعه توقف پروازهای عراق تکذیب شد
سازمان هواپیمایی:
🔹
پروازهای ایران به نجف و بغداد طبق برنامه در حال انجام است؛ فرودگاه بصره به دلایل داخلی عراق بسته شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/689264" target="_blank">📅 16:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689263">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
حاجی دلیگانی، نماینده مجلس: طرح سه فوریتی را برای خروج از NPT آماده کرده‌ایم و بهتر است هر چه زودتر آزمایش‌های لازم را برای سلاح هسته‌ای انجام دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/689263" target="_blank">📅 16:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689262">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c4b31107.mp4?token=ifa_v__xdEpY21UP16yhmMDCu8AoRFHi-AgEvMaVN8hyCOJb-ijK2pSwoD-GqhsyaNJ2WAxeBYLkPXons3Xbl21_wwVD3pWv4bJH3XWvPaF8Pnq230C02ER-s1L0AMUDhXeTmkncgM5BP2L_QBiYGau5EYDoT390LXhjTq3JoRwPAnpBExvnty3JKy3XMap45E1IC-vg11KkFNomTUeRNI4eZpijPo6D1H4w4G_FLwkfAa85Xh6Cffe6FsXuEhBjqIEwAHpAatUvddAGg4GiQxQj00g_Qh79yzNOhk-lvvNkF8_9Sa1dnt1yPv1orBBbSCiFRktNcbtlMRtylX7OTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c4b31107.mp4?token=ifa_v__xdEpY21UP16yhmMDCu8AoRFHi-AgEvMaVN8hyCOJb-ijK2pSwoD-GqhsyaNJ2WAxeBYLkPXons3Xbl21_wwVD3pWv4bJH3XWvPaF8Pnq230C02ER-s1L0AMUDhXeTmkncgM5BP2L_QBiYGau5EYDoT390LXhjTq3JoRwPAnpBExvnty3JKy3XMap45E1IC-vg11KkFNomTUeRNI4eZpijPo6D1H4w4G_FLwkfAa85Xh6Cffe6FsXuEhBjqIEwAHpAatUvddAGg4GiQxQj00g_Qh79yzNOhk-lvvNkF8_9Sa1dnt1yPv1orBBbSCiFRktNcbtlMRtylX7OTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از روی دود اگزوز، عیب خودرو را تشخیص دهید
🚙
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/689262" target="_blank">📅 16:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689261">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-rJZD2mO3fUDWrH3-9ptx7J9_7s3lijlIgRUP9ukOY_LfIZyiSq341iJdCl47yzE7zBZLsXxEckSPP5Gy-WTc6jn1sRULHfzB5ljDlRGbvamC9MMmkPqRHw93n9xG3wMnGrfO7YOhh0zm33KE2F0wmHHJnomUq7bfvyRKWUxypZteesmcboG0OcOgcAvOkGuxSg-3d5i5wkHKyLN8p0RF9_569oEg-dM18tvZTWb22pm_fG87CTkB8ykXmNytsoVg6FOZV6H05RFSTWfcM9dyNt3O9veC3c6bUAh7NsVKoDtPTQlOLSC6Tp558NJttmDdxiNKyW23oulcC7vdB_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره میدان ولیعصر(عج) موقتا تغییر نمی‌کند/ آغاز ایمن‌سازی دیوارنگاره
به‌دلیل انجام عملیات ایمن‌سازی، دیوارنگاره میدان ولیعصر(عج) موقتا با اثر جدید جایگزین نخواهد شد.</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/689261" target="_blank">📅 16:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689260">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر انجمن تولیدکنندگان مرغ گوشتی: ۶۰۰ هزار تن مرغ روی دست مرغداران مانده است
پرویز فروغی، دبیر انجمن تولیدکنندگان مرغ گوشتی در
#گفتگو
با خبرفوری:
🔹
برای تأمین مصرف داخل و ذخایر استراتژیک، حدود ۲ میلیون و ۱۰۰ هزار تن تولید مرغ کافی است اما در شرایط فعلی ما حدود ۲ میلیون و ۷۰۰ هزار تن مرغ تولید می‌کنیم که بیش از نیاز کشور است و این مرغ مازاد روی دست مرغداران مانده است.
🔹
درحال حاضر مرغداری‌ها در ضرر شدید هستند و خیلی از آن‌ها ورشکست شده و از دور خارج شده‌اند و با ادامه این روند شرایط بدتر هم می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/689260" target="_blank">📅 16:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689259">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPl9FGAluc3FXSx_W4Yt2zWyTE5a3sAp474qKiPX5Z7x3-nCA2M55LWmks04OIh8lzU64_R0VwKj4R0T4ipsz85K2nUGFn_IypeE9jcLzb4I1YyD2KCoOTEsj-5Ku3rvm3OQdBOxaVxfnPlk7GrrsuJiDnQCy3cU9YefOyRBgwb_STyVHCBFPSdAKwecgrc4_tVz-lJK_WAR-_TS5CjHhdMusgCz1OpCVWuYMNfNbaF64hHx1LcLhEB-MCa_i-N6ZsMNgBefo1RBAjhfSz8wWes06tQv8drOGMwiXHbVhMl4C3DGmHKnClSelRJKJ4RdVRZ4TQo2WhfSHyP3YRjXUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ که این حرف‌ها را می‌زند، ظاهراً ماجرای آخرین درگیری با حوثی‌ها را یادش رفته؛ همان ماجرایی که ناو «ترومن» مانور گریز داد و یک F-18 آمریکایی در دریای سرخ سقوط کرد!
به توییتر خبرفوری بپیوندید
👇
https://x.com/Akhbare_Fori/status/2098737810995806411</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/689259" target="_blank">📅 16:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689258">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
تحریم به ارسال مقالات رسید
🔹
معاون تحقیقات و فناوری وزیر بهداشت، با انتشار تصویری از صفحه محدودیت دسترسی شرکت Salesforce به دلیل قوانین تحریم‌های آمریکا، از ممانعت کاربران ایرانی از ارسال مقاله به یک مجله علمی خبر داد و گفت: این دیگر تحریم علمی نیست، جنگ علمی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/689258" target="_blank">📅 16:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689257">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سی‌ان‌ان: قیمت گازوئیل در آمریکا بیش از ۵۵ درصد افزایش یافته و در برخی جایگاه‌ها به حدود ۹ دلار رسیده است؛ در صورت عبور قیمت از ۱۰ دلار، برخی تابلوهای پمپ‌بنزین امکان نمایش آن را ندارند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/689257" target="_blank">📅 16:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689256">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z04UJt_f5gvjn3A3iovJAC2co4LYYh608mCbQVMDkoky3YHMCjdoLhAQ5vxz9OeFuOH1cLhuFe6iu-eU-tZd4gfZ9X9Z3DaIt5ymS1WxOZ98sa0tkwSwLIZLh0XQOTpCSBOz8uYthgYItD-8dFtmp7tYLhPaiwbYKmHZXnMrFZ-cVxlMyjFY7TgA2aPYroxnPZneW5nOPg_oCAhVV3pvyf9mSQUydvPQw5kpOy-6RprgfzZTg4BpwlI_22odHmCAeABJW_pPFfndcnjZEySa4Tqe3zGUjQzpyR6lxM-si7A1ZTWtyrUIHMGYalvvh_9DDpPiRDfoClhUf_1Y2ijB4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرداخت خسارت خودروهای جنگ از ۴۰ هزار میلیارد ریال گذشت؛ منازل از امروز در نوبت جبران خسارت
🔹
رئیس‌کل بیمه مرکزی اعلام کرد تاکنون خسارت ۳۵ هزار و ۸۴۱ خودروی آسیب‌دیده در دو جنگ به ارزش بیش از ۴۰ همت  پرداخت شده است.
🔹
همزمان؛ پرداخت خسارت اثاثیه منازل آسیب‌دیده از جنگ ۱۲ روزه از امروز آغاز شده و بیمه ایران روند رسیدگی و پرداخت پرونده‌های باقی‌مانده را ادامه می‌دهد.
🔹
بیمه مرکزی تأکید کرده پرداخت خسارت‌ها بدون وقفه در حال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/689256" target="_blank">📅 16:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
خبرنگار المیادین در صنعا: تردد کشتی‌ها از طریق تنگه باب‌المندب به‌صورت عادی و منظم در جریان است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/689255" target="_blank">📅 16:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689254">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
سخنگوی سابق وزارت‌خارجه آمریکا: ما دقیقا می‌دانستیم داریم مدرسه را هدف می‌گیریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/689254" target="_blank">📅 16:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689253">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f796d356a.mp4?token=YfapI2Ne_5A3pSUWOetXn1gxlOmLOp5-yT2kwblFVWxn4QRhoo0uWCMpXhvPo_WoaZJ-iCcDrqPlwtPpKjY1khCLURrTxNNSOBOjal_9Kwdw3g8juNV1uogirP08JWy4o0lolzhUZjnbGc3Y_y0fQsOdIFi7wXnqUMInUfzFbnZlxN6X-W5eltppRwirx-qwnncl9p_yxGptPuKANvUv1bC_2Z7ENMxJCjZsLpOTevfqgbl58CQ0xMDMDaw7dptOVtg2TBPotgbkb81YdTKRux0do3qE1Y7xmefyb1lBUNePltL1iItGGEEsCKRUYP-0quSNpw8-xt63b63KSvPPbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f796d356a.mp4?token=YfapI2Ne_5A3pSUWOetXn1gxlOmLOp5-yT2kwblFVWxn4QRhoo0uWCMpXhvPo_WoaZJ-iCcDrqPlwtPpKjY1khCLURrTxNNSOBOjal_9Kwdw3g8juNV1uogirP08JWy4o0lolzhUZjnbGc3Y_y0fQsOdIFi7wXnqUMInUfzFbnZlxN6X-W5eltppRwirx-qwnncl9p_yxGptPuKANvUv1bC_2Z7ENMxJCjZsLpOTevfqgbl58CQ0xMDMDaw7dptOVtg2TBPotgbkb81YdTKRux0do3qE1Y7xmefyb1lBUNePltL1iItGGEEsCKRUYP-0quSNpw8-xt63b63KSvPPbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کینه شتری ترامپ از ناتو بخاطر تنگه هرمز!  ترامپ:
🔹
ناتو نمی‌خواست درباره تنگه هرمز به ما کمک کند. پس چرا ما باید به آنها کمک کنیم؟ #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/689253" target="_blank">📅 16:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689252">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
کارشناس قطری: ترامپ قرار بود بر تنگه هرمز تسلط پیدا کند، امروز نه تنها بر هرمز مسلط نیست بلکه تنگه باب المندب هم به دست متحدان ایران افتاده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/689252" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689251">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e33b0ddbc.mp4?token=ndn7oiPYZXGOoJ3_Det7KRkMC_K3G86p6HARsYj2Z1FjOI6YSDTIa8yLkBWGL2z_VzzkMDW4ev2_GImjWMWDVWJUY9xDPpkNy0LWNkBORlAtsGMX92HP1GQ9uO9_1Q5thnviIhcJYGyMadewUVjSnjlUiUlOB_xDLzpZpjzPsZPFPzlvqm5CVlTHrkAZUKAzBo-D0i7SP7lomlO5CmcUnobCksWHmgtVTIYtLKFlS9Cl_4YIfC0f6ZhQytFPu0oKzpcjW6-LbEU2EtxdjGJpbQjdL2Sas0VMTXGtN4uHiz0in77qppOkQCmkwC4Bb2x79oYZMqrSuLI7fl3WGYer8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e33b0ddbc.mp4?token=ndn7oiPYZXGOoJ3_Det7KRkMC_K3G86p6HARsYj2Z1FjOI6YSDTIa8yLkBWGL2z_VzzkMDW4ev2_GImjWMWDVWJUY9xDPpkNy0LWNkBORlAtsGMX92HP1GQ9uO9_1Q5thnviIhcJYGyMadewUVjSnjlUiUlOB_xDLzpZpjzPsZPFPzlvqm5CVlTHrkAZUKAzBo-D0i7SP7lomlO5CmcUnobCksWHmgtVTIYtLKFlS9Cl_4YIfC0f6ZhQytFPu0oKzpcjW6-LbEU2EtxdjGJpbQjdL2Sas0VMTXGtN4uHiz0in77qppOkQCmkwC4Bb2x79oYZMqrSuLI7fl3WGYer8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کینه شتری ترامپ از ناتو بخاطر تنگه هرمز!
ترامپ:
🔹
ناتو نمی‌خواست درباره تنگه هرمز به ما کمک کند. پس چرا ما باید به آنها کمک کنیم؟
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/689251" target="_blank">📅 15:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689250">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb966b696.mp4?token=oqpyS-afJdebVR7E2l4ziBswtaDD9n8mjRcl-2ZG3LyEE6YQAcBtvAUtTslrt_b3xSxqzubWo4ZuzVyFx3k0kdQ0ex3YebmWcZvvFz5TruUo9Am_h_db-BdTdiCj6V1dknRWA2vfoWGM8f_bQvREC4ycapqFxcrZWPzErcofIanr6ldeBB98WcljanrprpmzxGSc9S56XtC2TfxGZ3AY8axnA_lPg5L7gTcOXtlXYyhtubeqt3L94ciSniSgVsZ-7u8H01Pmiv4vmzUcpHgpNYNPSYUjR6Kg-Evu7kjxErN4I-KSMpN4k9UHCvQFjhzUx5ZRPIqQ4osSy4ykyU0kqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb966b696.mp4?token=oqpyS-afJdebVR7E2l4ziBswtaDD9n8mjRcl-2ZG3LyEE6YQAcBtvAUtTslrt_b3xSxqzubWo4ZuzVyFx3k0kdQ0ex3YebmWcZvvFz5TruUo9Am_h_db-BdTdiCj6V1dknRWA2vfoWGM8f_bQvREC4ycapqFxcrZWPzErcofIanr6ldeBB98WcljanrprpmzxGSc9S56XtC2TfxGZ3AY8axnA_lPg5L7gTcOXtlXYyhtubeqt3L94ciSniSgVsZ-7u8H01Pmiv4vmzUcpHgpNYNPSYUjR6Kg-Evu7kjxErN4I-KSMpN4k9UHCvQFjhzUx5ZRPIqQ4osSy4ykyU0kqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید انقلاب: ریشهٔ مردمان زیدیه شیعه در یمن، که امروزه انصارالله یمن را تشکیل می‌دهند، به مازندران و گیلان بازمی‌گردد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/689250" target="_blank">📅 15:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689246">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
والیبال قهرمانی آسیا؛ ایران به فینال آسیا راه یافت، شاگردان پیاتزا کانگوروها را هم شکست دادند
🔹
ایران ۳ - ۱ استرالیا
🇮🇷
۲۵ | ۱۷ | ۲۵ | ۲۵
🇳🇿
۲۱ | ۲۵ | ۱۷ | ۲۲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/689246" target="_blank">📅 15:30 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
