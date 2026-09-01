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
<img src="https://cdn4.telesco.pe/file/hJFBCv5Ugdp0zR-X_ix5c6G3pIvNnLgGjhBaXMt8ZKkxoor1HKrjGQQcm-VjaEQE1rx9DIh79uQaimd0mOLoYw-CV6ovkWbQZyYo7z3G9naYxa5VAKzYaW-aiGKPRH85X-wgGTTUrT8vWlXX8f4WQ0kbMjeKEMx5UFhWvpJEcuB0f08cA6d1ijUHh2AZS18Fb6KUZc2L4xTYOHjqKYX6PxuVw_oSgzEuJ4GuYGIHooW2s6NLQAsgmZD0p-brv146bScw5VPSJ4esvu9nT1YOFEk5J4vP4xbmTk8ygcnIOffwUnVKt5mbX_gzB0oQfXY4YQ0JM9NrO78Wfv_WpOYh_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 آموزش سئو با محسن طاوسی</h1>
<p>@mohsentavoosiseo • 👥 8.01K عضو</p>
<a href="https://t.me/mohsentavoosiseo" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 من تالیف و تولید می کنم✅. نه ترجمه.نه اخبار. نه گرداوریدوره:mohsentavoosi.com/course/seo/خرید دوره:@mohsentavoosisupportyoutube.com/c/MohsenTavoosiInstagram.com/mohsentavoosi.seolinkedin.com/in/mohsentavoosi</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 22:31:47</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">Overlearning
Unlearning
❗️
مهارت یادگیری زدایی و جلوگیری از زیادی یادگرفتن تو این عصر خیلی مهمه.
❓️
چقدر عمیق شیم؟ از کجا به بعد زیادیه؟ چاهی که از یادگیری زیادی عمیق و بیش از حد داریم می کنیم، به آب و چشمه و گنج میرسه واقعا؟
❓️
چجوری بفهمیم داریم زیاده روی می کنیم تو یادگیری؟
❓️
تله آدم های باهوش و با استعداد و قوی چیه؟
❓️
وسعت دید همیشه باعث بهبود عملکرد میشه؟
❓️
پرداخت بهای عمیق شدن بیش از حد، میصرفه به نتیجش؟
❓️
چجوری بفهمیم تو overlearning افتادیم؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/mohsentavoosiseo/936" target="_blank">📅 23:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">من پیام به کانال رو باز کردم و به نظر شما نیاز دارم.
❗️
اگر برنامه نویس و فنی نیستید. اگر آدم tech یا شبکه کار یا devops نیستید. (مهمه نباشید)،
❗️
و دارید با ChatGPT codex و کلا OpenAI یا با Antigravity گوگل با skill ها و اسناد پروژه و MCP و Connector ها کار می کنید و فقط در حد چت و پرامپت استفادتون نیست،
❓
بهم پیام بدید که چرا کلاد رو انتخاب نکردید؟ مگه کلاد سخت تر بود؟
🔴
تأکید مهم: مهمه که فنی و شبکه کار و برنامه نویس و توسعه دهنده نباشید.
و مهمه که از AI فقط به صورت چت و پرامپت استفاده نکنید و دقیقا وابسته به اسکیل ها و کانکتور ها باشید.
اصلا کسی هست که شرایط بالا رو داشته باشه! چون هرکی تو اینستاگرام کامنت گذاشت که چت جی پی تی کدکس یا انتی گرویتی گوگل بهتر از کلاد هست، بلا استثنا برنامه نویس بود.</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/mohsentavoosiseo/935" target="_blank">📅 15:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">واقعیتش ترسیدم! جدی جدی چت رو بست!   خطرناکه! بنظرم یکی باید جلوی هوش مصنوعی و آنتروپیک رو بگیره. چرا باید یه ماشین لحن صحبت براش مهم باشه و بهش بربخوره و حتی کار قهریه انجام بده و اون چت رو کلا غیر فعال کنه!   پس فردا میاد کل اکانت هم لابد بن میکنه! پس فردام…</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/mohsentavoosiseo/933" target="_blank">📅 14:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uS1QP6sWcWNcjg1wBM_A-iwUdb52-thNgHirw5_dIIpM0_kuVc3nKKFFaV8z9yyFuyCcGBlK8w6Va9nBKSZYrqJwgxWAfx05blSIJYqaK0TvRnjQt0EGSaPYG3uiTQvBobfkPInllpy2-kM6At4jmedGzhA5JKvOiLIF7ax-vCUyTk9epluXHguSMQWneZKsTEyk05y5WiZQnfByPE-kN9QvuujKZRgctWIA9Fokai2bpmJWtC-mRamE-1qxzd6dQacubuvQFogDlAQWAY-aBmmiHmDm4DLacxrggWOtMQ866P_zdtPx-uuIbg-ijEQ3xt7figAn1FmGl6ufdul8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعیتش ترسیدم! جدی جدی چت رو بست!
خطرناکه! بنظرم یکی باید جلوی هوش مصنوعی و آنتروپیک رو بگیره. چرا باید یه ماشین لحن صحبت براش مهم باشه و بهش بربخوره و حتی کار قهریه انجام بده و اون چت رو کلا غیر فعال کنه!
پس فردا میاد کل اکانت هم لابد بن میکنه! پس فردام میاد به ما دستور میده!
من برای اولین بار ترسیدم. این خوب نیست اصلا!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/mohsentavoosiseo/932" target="_blank">📅 14:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/mohsentavoosiseo/931" target="_blank">📅 11:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ساختار سلسله مراتبی URL ها، یک احساس، بیش نیست. هیچ ربطی به درک گوگل از محتوا یا ساختار شما نداره.
+روش پیشنهادی بهتر
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/mohsentavoosiseo/930" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/mohsentavoosiseo/929" target="_blank">📅 13:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
سرابی به نام پروژه گرفتن
❗️
به نام پروژه خارجی داشتن
❗️
فکر نکن تمام ماجرا اینه بلد باشی و حرفه ای باشی.
❓️
من به گذشته برگردم و کسی من رو نشناسه چیکار می کنم؟ محسن طاوسی ای که بلد هست ولی بدون ارتباطات و بدون اینکه بشناسنش، چه مسیری رو میره؟
مسیر من رو نرید. از من استفاده کنید. از دانش من. از تجربه من. ولی مسیر من رو نرید!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/mohsentavoosiseo/928" target="_blank">📅 11:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آموزش پایین اوردن نرخ تبدیل
😶
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/mohsentavoosiseo/926" target="_blank">📅 16:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">صحبت از اپدیت شد، نیاز هست به دوستان یاداوری کنم، محتوای متنی و ویدویی من رو درباره بحث جاوااسکریپت ببینید حتما.
برای وردپرسی ها کاربرد نداره. برای سایت اختصاصی ها و دولوپر هاست:
سئو سایت های وابسته به اجرای جاوااسکریپت در مروگر
ارتباط جاوااسکریپت با هزینه های گوگل
سئو صفحات فیلتر دسته بندی فروشگاه - Faceted Navigation
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/mohsentavoosiseo/925" target="_blank">📅 16:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">Mohsen Tavoosi – چرا آپدیت های گوگل آنقدر ها در لحظه مهم نیست؟</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/mohsentavoosiseo/924" target="_blank">📅 16:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چرا آپدیت های گوگل آنقدر ها در لحظه مهم نیست؟</div>
  <div class="tg-doc-extra">Mohsen Tavoosi</div>
</div>
<a href="https://t.me/mohsentavoosiseo/922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">چرا آپدیت های گوگل اونقدر ها هم در لحظه مهم نیست؟
چرا نباید نگران اپدیت ها باشید؟
وقت تلف کن ترین کار ممکن، اینه که تند تند برید ببینید گوگل چه اپدیتی داد. رسمی بود یا غیر رسمی.
درست اینه که فرض کنید گوگل هرروز اپدیت میده. اونم چندین اپدیت. هم رسمی هم غیر رسمی. واقعا هم همینه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/mohsentavoosiseo/922" target="_blank">📅 16:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">طنز:
موقع تهیه گزارش به کارفرما، وقتی پروژه ای 400 تا دونه کلیک داره در ماه، و 40 تا کلیکش کم میشه، میگیم، طبیعیه ده درصد کم و زیاد اصلا درست نیست در محاسبات و تحلیل بیاد در دنیای Organic Search.
اما وقتی 40 کلیک زیاد میشه نسبت به ماه قبل، 40 بار در گزارش، مینویسیم 40 تا کلیک اضافه شده
😎
✅
ولی واقعا، جدی، رشد و افت و درجا زدن رو باید همه رو نوشت. فاکتور هایی که هیجان الکی هست چه مثبت چه منفی هم باید نوشت.
✅
برند رو از نان برند هم باید جدا کرد حتما.
✅
میزان رشد ایمپرشن ها رو باید لحاظ کرد وقتی کیورد جدید رتبه گرفته ولی کلیک نگرفته.
کارهایی که فعلا باعث رشد نمیشه و حتی ممکنه باعث افت کلیک بشه ولی زیرساختی و لازم هست(مثل اصلاح تارگتینگ و هرس)، باید بهش اشاره بشه که توقع و انتظار طرف از نتیجه سریع، بیاد پایین.
❌
به هیچ وجه هم نباید نمودار کلی پوزیشن نشون داد از کل سایت. برای تک کیورد Exact اکیه. برای کل سایت، بسیار بسیار اشتباه و غیر حرفه ای هست.
اینجا
و
اینجا
رو بخونید.
متاسفانه بعضی ها که تجربشون بیشتر میشه فکر مکنن ایمپرشن کلیک ملاک نیست، میانگین رتبه ملاکه و شبیه پزشکان متخصصی عمل میکنن که زمان پزشک عمومی بودنشون، درمانشون بهتر جواب میداد. نمودار کلی رتبه برای کل یک دامنه، آمار بسیار بسیار تباهی هست.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/mohsentavoosiseo/921" target="_blank">📅 14:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAPPXAZSB5D33XLCkGqUjfb_CIsgEGWJ9TDZGEtlrNF8gUp2KW4OUP5jb_VAbgy1q1176QpXQwPptMhuG_6dHi7PNJDEucj-MJrK-lPFa7QAaonXnVHcKPWL30vDskrE0nXA5lGug7LLu_XkJ5u06XfmX2I7d3yh5mmCw-llWwUatfukruuR9XAmVS69XjRaB3y7rxyFw949Zb7dp2vSNvgpmQEtVDR6sV_eTpeF6cXI4okT01B8Ft3dmZRo_St3K8c8Bzu8iLLl5-Fm97YanNaSP5MkCfdJwAt58BGfzmkR2Z2lr1cy4N5gQmuJXYbXcB8Z90AWm3OG5NrLizlUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیچاره گوگل. عقبه هنوز.
تازه تو بعضی سایت های غیر فارسی بخش Generative AI داخل Performance اضافه کرده.
فعلا کلیک رو یا اصلا دیتاش رو ثبت نمیکنه یا تو گزارش نمیتونه بندازه. یا اصلا کلیک نمیگیره که برای من ننداخته. و طبیعیه که کلیک نگیره.
چرا بیچاره؟ چون خیلی عقبه. ما رفتیم تو آمار گیری از Generative Engine ها، این تازه بعد مدت ها آمار AI Overview خودش رو تازه داره میندازه. از گوگل انتظار بیشتری بود. ولی خب. خوبه باز.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/mohsentavoosiseo/920" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">لیست بایگانی مقالات (پست ها) من که سال 93 , 94 منتشر شدند! یعنی 12 سال گذشته. از سایت web archive.
✅
که همچنان معتبر هست! و بسیار همین الان با پوست و گوشت، لمس می کنید! باز هم باید بگیم سئو عوض شده؟ اصول سئو همون اصول هست!
اون زمان کسی نمینوشت و فقط بلغور ترجمه در سطح وب بود.
ولی می تونید خط فکری الان من رو 12 سال پیش ببینید! حتی پست دارم با عنوان "عصر بی حوصلگی آدم ها! که متاسفانه تو web archive نبود.
هوش مصنوعی گوگل به زبان ساده
اشتباه نکنید! این مقاله سال 93 من هست!
چرا محاسبات ما در سئو غلط از آب در می آید؟
قوانین نانوشته گوگل
خاصیت تضریبی فاکتور های سئو
تشخیص رقابت کلمات کلیدی
(پست تلگرام رو اپدیت کردم و این رو اضافه کردم. جا افتاده بود)
تناقض های گوگل
بروز رسانی Freshness گوگل – تغییر لحظه ای نتایج با فرشنس
پرستش گوگل
114 فاکتور رتبه بندی گوگل
لینک بیلدینگ نکنید وگرنه پنالتی می شوید!
اینجا در نقد تفکر اون زمان بود که تازه پنگوئن نسخه های چندمش رو داده بود و همه ترسیده بودند که کلا دیگه لینک سازی نباید کرد. و این تفکر که بک لینک بی اثر شده. اون زمان هم بود. اون موقع من میگفتم A و T از EAT رو چیکار می کنید پس؟ بهرحال فعالیت اف پیجی حتی نوفالو نیازه. میگفتن نه فقط محتوا کافیه. محتوای خالی فقط E هست. اون موقع هنوز E دوم یعنی Experience نیومده بود.
سه راه پنالتی شدن در گوگل
روش های خروج از پنالتی گوگل و ریکاوری
تراست رنک
محتوا پادشاه نیست
قوانین گوگل درباره بک لینک
جهت اطلاع کسانی که تازه وارد سئو شدند، هنوز هم در اواخر 2026 همین قوانین هست!
برندینگ، دست برتر سئو
اولین ویدیو یوتیوب من سال 94
- بررسی چند موضوع رقابتی در ایران
(ورودم به سئو از 91)
اگر دوره من رو دیدید یا حتی ویدیو های رایگان من رو، ادبیات و لحن این مقاله ها، براتون آشناست.
همین مطالب هم متاسفانه بدون منشن و یاد کردن و چیزی، توسط بعضی از دوستان، از زبان خودشون مطرح میشه.
حالا همون محسن طاوسی 15 سال پیش، یک اپدیت game changer داره که کاملا تهاجمیه! و عملا انقدر بزرگه که میتونم بگم یک دوره است!
دوره تهاجمی سئو بین المللی با Claude . بدون مرز جغرافیایی و زبانی. برای اکثر مدل های SERP فارسی و غیر فارسی. که در حال ضبط هست و برنامم اینه قبل از پایان 2026 منتشر بشه و هرکس دوره رو داشته باشه رایگان دریافت میکنه.
چرا تهاجمی؟ Aggressive در اینجا به معنی شدید و طوفانی هست. تا نبینید متوجه نمیشید چرا اسمش این هست. برای همین سورپرایز هست. ولی انتظار رو پایین نگه دارید که بعدا سرخوردگی ایجاد نشه. فرض کنید یک آپدیت معمولیه. خیلی معمولی. سرفصل های حدودیش هم در صفحه دوره هست هم در
این پست تلگرام
.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/mohsentavoosiseo/919" target="_blank">📅 12:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-917">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">به زودی به جایی میرسیم که اخاذی از skill ها و md ها و اسناد کلاد میشه.
ما بحثی داریم به نام پرامپت های چرخشی یا لوپ یا تکرار شونده. بعد بالغ شدشون میشن Agent.
پیچیده نیست ها! مثلا یه کار رو سه بار میگی چک کنی بازبینی و اصلاح کنه. بعد مامور(agent) درست میکنی که اینکارو انجام بده. بعد اون ایجنت رو میذاری سر کارش، هربار خودکار انجام بده.
چند وقت یک بار هم میری سوله مامور هات، بهشون آب و علف میدی و پیچشون رو سفت میکنی و برمیگردی پی زندگیت.
چجوری اخاذی می کنند؟
مثلا میدزدند فایل های شخص، شرکت و سازمان شما رو و میگن انقدر بده تا این همه زحمتی که کشیدی این سیستم و مستندات و مهارت ها و بلوغ رو که ساختی، بهت برگردونیم.
دو بیت کوین بده بهت پس بدیم. شرکت های بزرگ هم می ارزه براشون که این باج رو بدن.
من بخش سئوییش رو آموزش میدم تو اپدیت جدید دوره که در حال ضبطه. بخش های دیگه خارج از سئوش با خودتون
😎
البته سئوش رو استاد شید بقیش هم استاد میشید.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/mohsentavoosiseo/917" target="_blank">📅 19:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مقاله من حدود دوازده سال پیش!
March 2015!
ویرایش هم نشده. همون خاصیت تضریبی فاکتور های سئو، چیزیه که تازه بعضی ها دارن کشفش میکنن. یا بهش فکر میکنن.
من خیلی خوب بلدم پیچیده حرف بزنم جوری که فکر کنید واااای من حالا حالا باید دانشمو زیاد کنم تا بفهمم محسن طاوسی چی میگه. اما فایدش برای شما چیه؟
برام مهمه مخاطب من، یه چیزی دستش بگیره و اجرا کنه و فقط نمایش سواد من نباشه.
114 فاکتور رتبه بندی در گوگل
https://www.linkedin.com/pulse/114-%D9%81%D8%A7%DA%A9%D8%AA%D9%88%D8%B1-%D8%B1%D8%AA%D8%A8%D9%87-%D8%A8%D9%86%D8%AF%DB%8C-%D8%AF%D8%B1-%DA%AF%D9%88%DA%AF%D9%84-mohsen-tavoosi
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/mohsentavoosiseo/916" target="_blank">📅 16:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🟢
دوره جامع SEO/AEO بین المللی با AI
🟢
قیمت، در سایت به روز شد (فعلا از خارج به روز شده. سرور ایرانم رو هنوز به روز نکردم) و از این به بعد، هر ماه، قیمت به صورت تدریجی افزایش داره و دیگه اطلاع رسانی مرتبط با قیمت انجام نمیشه.
https://mohsentavoosi.com/course/seo/
آپدیت جدید، صفر تا صد سئو هست و سرفصل هاش این موارد هست که هنوز در لینک صفحه دوره قرار داده نشده و محتوای این صفحه، بعد از انتشار کامل این بروز رسانی جنجالی، به روز خواهد شد:
🟢
مباحث کار با هوش مصنوعی، OKF, Skill، اسناد AI، Memory، MCP, Connectors.
🟢
انواع SERP در گوگل در در زبان ها و کشور های مختلف
🟢
کسب رتبه در Google Shop (Merchant)
استاندارد سازی پروژه ها با هوش مصنوعی
آنبوردینگ انسان و Agent
🟢
کسب رتبه در کشور خاص، زبان خاص، یا جمعی از کشور ها و زبان ها یا به صورت کلی کسب رتبه و افزایش شانس نمایش و پیشنهاد توسط AI به صورت بین المللی (مثل
booking.com
)
🟢
ساخت پلاگین لینک داخلی خودکار با کلاد برای وردپرس با وایب کدینگ.
🟢
ساخت دسته جمعی صفحات سایت با AI
🟢
تحقیق بازار شامل Intent, Keyword و محدوده سوالاتی که از AI پرسیده می شود.
🟢
ساخت صفحات (تارگتینگ، کلاسترینگ به روش محسن طاوسی. نه اینکه هرکاری اکثریت کردند شما هم بکنید و فرصت ها بسوزند!)
🟢
سئو تکنیکال برای گوگل، بینگ و AI ها.
🟢
بهینه سازی داخلی سایت.
🟢
تولید محتوا با AI
🟢
کسب لینک از کشور ها و زبان های مختلف
کل بحث Off-Page
🟢
هرس صفحات و بهبود نرخ خزش
🟢
چند زبانه کردن سایت از نظر SEO
🟢
گزارش نویسی به هر زبانی
با تمام سرفصل های بالا، AI آمیخته شده است. کلا همشون با AI هست. بیشتر کلاد (اختصاصی از خود کلاد) و تا حدی هم Gemini
به سرعت در حال ضبط هستم. و تیم تدوین، در حال تدوین هست. از نظر خودم این اپدیت، سورپرایز هست! اما دوست ندارم چیز بزرگی در ذهنتون بسازید که بعدا انتظار ایجاد بشه.
این امضا یا مشابهش، از این به بعد زیر پست بسیاری از محتواهای کانال، قرار خواهد گرفت و اطلاع رسانی قیمت و... حذف خواهد شد.
——-———————————————————-
🟢
لینک صفحه خرید دوره سئو
🟢
پیام جهت خرید دوره
🟢
اطلاعات بیشتر در info کانال(bio)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/mohsentavoosiseo/914" target="_blank">📅 12:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/mohsentavoosiseo/911" target="_blank">📅 15:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/mohsentavoosiseo/910" target="_blank">📅 14:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/mohsentavoosiseo/909" target="_blank">📅 14:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/mohsentavoosiseo/908" target="_blank">📅 13:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-907">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خطاب به همه کسانی که خیلی حرفه ای و باهوش هستند.
خطاب به کسانی که از اینکه یک سری بی سواد یا کم سواد حرف اشتباه میزنن، ناراحتن.
خطاب به همه با سواد ها!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/mohsentavoosiseo/907" target="_blank">📅 13:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یه اشتباه بزرگ کسانی که تازه مهاجرت کردند یا تازه درگیر پروژه های غیر فارسی شدند یا حتی مدت زیادی گذشته اصلا،
❗️
اینه که فکر میکنن جهان یا بین الملل یا "خارج"! یا کشورهای دیگه، همونی هست که ازش تجربه دارند و همه چیو با عینک خودشون میببنن.
❗️
❗️
حتی استناد میکنن که فلان همکار یا مدیر خارجی هم اصلا اعتقادش همینه.
❗️
❗️
❗️
در حالی که همون همکار خارجی هم اشتباه میکنه. اون هم فقط نگاه خودشو داره میگه و تجربیات خودشو.
✅️
در همه جای جهان(غیر از هند و پاکستان و اندونزی و روسیه و...)، لینک بیلدینگ و پست مهمان مشابه رپورتاژ، بوده و هست و خواهد بود.
✅️
مدل پیدا کردن و صحبت با رسانه ها در کمپین های روابط عمومی PR، یعنی کاملا کلاه سفید، بوده و هست و خواهد بود.
✅️
مدل اینکه کلا کمپین اف پیج یا PR و کلاه سفیدم ران نشه و فقط تبلیغ بنری یا گوگل ادز یا کلا کمپین های تبلیغاتی فقط ران بشه هم هست که سئوشون فقط تکنیکال و سئو داخلی و کیورد ریسرچ و ساخت صفحه میشه(اونم محدود).
✅️
✅️
همه اینا هست. فقط شرکت با شرکت، فرق داره. سایت با سایت فرق داره‌. هرچقدر بزرگ تر باشن شرکت ها، مدلاشون به مدل آخر نزدیک تر میشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/mohsentavoosiseo/906" target="_blank">📅 22:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سوال:   دوستان من یه دسته بندی رو آوردم بالا و رتبه ۴ صفحه ی یک هستش  اولین سایت که ترب هستش  ولی اگه ترب رو حساب نکنیم میشه سایت سوم طبق سرچ کنسول توی بازه ۲۸ روز ، ۱۲۹ سرچ داشته  ولی کلیک ۵ تا!! راه حل برای کلیک گرفتن چیه؟ عنوان  و متا هم از دو رقیب دیگه…</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/mohsentavoosiseo/903" target="_blank">📅 20:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-902">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سوال:
دوستان من یه دسته بندی رو آوردم بالا و رتبه ۴ صفحه ی یک هستش
اولین سایت که ترب هستش
ولی اگه ترب رو حساب نکنیم میشه سایت سوم
طبق سرچ کنسول توی بازه ۲۸ روز ، ۱۲۹ سرچ داشته
ولی کلیک ۵ تا!!
راه حل برای کلیک گرفتن چیه؟
عنوان  و متا هم از دو رقیب دیگه خیلی بهتر هستش.
چون روی کلمه ی اصلی اومده بالا
پاسخ در ویس:
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/mohsentavoosiseo/902" target="_blank">📅 19:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-901">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سوال:   من از وقتی هاست سایتم رو برم روی Geo Dns میهن وب هاست یه مشکلی پیدا کردم. کلمات کلیدی تو سرچ کنسول رتبه دارن ولی وقتی خودم دستی سرچ میکنم نیستن. اکثر ساتیتام اینجوری شدن. این طبیعیه؟  پاسخ: https://t.me/mohsentavoosiseo/511 این ویس و ویس پایین  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/mohsentavoosiseo/901" target="_blank">📅 13:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-900">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سوال:
من از وقتی هاست سایتم رو برم روی Geo Dns میهن وب هاست یه مشکلی پیدا کردم. کلمات کلیدی تو سرچ کنسول رتبه دارن ولی وقتی خودم دستی سرچ میکنم نیستن. اکثر ساتیتام اینجوری شدن. این طبیعیه؟
پاسخ:
https://t.me/mohsentavoosiseo/511
این ویس و ویس پایین
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/mohsentavoosiseo/900" target="_blank">📅 13:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/mohsentavoosiseo/898" target="_blank">📅 11:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/mohsentavoosiseo/897" target="_blank">📅 15:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تولید محتوا با کلاد
استاندارد سازمان رو برای کلاد تعریف کردن
هوش مصنوعی، چت کردن و چهار تا فایل اتچ کردن و اسکرین شات فرستادن و چهار تا پرامپت خوب دادن نیست! اینا خیلی مقدماتیه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/mohsentavoosiseo/896" target="_blank">📅 15:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">https://t.me/mohsentavoosiseo/846
بن میشیم نمیتونیم کلاد بگیریم!
Ban
#بن
#ban
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/mohsentavoosiseo/895" target="_blank">📅 15:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/mohsentavoosiseo/894" target="_blank">📅 15:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-893">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تفاوت کلاد تو چیه دقیقا؟ نسبت به بقیه AI ها؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/mohsentavoosiseo/893" target="_blank">📅 14:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67db1cde60.mp4?token=haCBHbmDC9M3cNBu_HP5c6tXt0Dza2b-spgKPJ8GZPGcZtRz8gfouutqyBCkj384dDZsehdNOnsSWqPN2tbGxYNp95MowuIXCm-BL9WXWNPGVLHaUmZHD3rHHWo39D6Tpo0hkhqyxs2EoxV2GNZMrma8QHf-ztBvqIfSVjgVNBPmRfHp5QKJVWo3fISwAI3U8acdfSYHsOg0IqUbN0sUzVWd_uO4qXjJtBXX4OE8mLgroXjBkHyFa9fgRpol9zJSaihp4kPwxRF_ckE3EHusLFWyjVnG4XDYe-nt2fIpBLy4033Zq5Bx_3PzkV-Lq3u7O9Bt17-4UVT9XjVsbB_EsUx3aeU3zsDQBMGse0axNhS_FqIb9l9pEH4QEnZGdpHX1FNjTJ_XlqcEFNYjv1EfnrB8iDCeLmn8xVqwT_QHlxuUDe9AOlNl0PI0_2jCI9PiZzyDcBhVlWUu9AEglOIcET65ZBaCQFAZ7kmC3uK6OjAJPF5VfSO8KuCHvmsgtomkwt-AIECOd5LsUAmgfQqPOjvDyuBkW1jv5cnGcYXcroRAHAWiUg7CBzlfhu3pR2RWs951OsRbWEawwxH063kNu_yD8Evjfg_wro-kYWuToX1uurSe973jJNqr5aI-uosjUve7wIPtfrRmYaoSV96uC4_9CdGdsExBfsDDaWT3KnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67db1cde60.mp4?token=haCBHbmDC9M3cNBu_HP5c6tXt0Dza2b-spgKPJ8GZPGcZtRz8gfouutqyBCkj384dDZsehdNOnsSWqPN2tbGxYNp95MowuIXCm-BL9WXWNPGVLHaUmZHD3rHHWo39D6Tpo0hkhqyxs2EoxV2GNZMrma8QHf-ztBvqIfSVjgVNBPmRfHp5QKJVWo3fISwAI3U8acdfSYHsOg0IqUbN0sUzVWd_uO4qXjJtBXX4OE8mLgroXjBkHyFa9fgRpol9zJSaihp4kPwxRF_ckE3EHusLFWyjVnG4XDYe-nt2fIpBLy4033Zq5Bx_3PzkV-Lq3u7O9Bt17-4UVT9XjVsbB_EsUx3aeU3zsDQBMGse0axNhS_FqIb9l9pEH4QEnZGdpHX1FNjTJ_XlqcEFNYjv1EfnrB8iDCeLmn8xVqwT_QHlxuUDe9AOlNl0PI0_2jCI9PiZzyDcBhVlWUu9AEglOIcET65ZBaCQFAZ7kmC3uK6OjAJPF5VfSO8KuCHvmsgtomkwt-AIECOd5LsUAmgfQqPOjvDyuBkW1jv5cnGcYXcroRAHAWiUg7CBzlfhu3pR2RWs951OsRbWEawwxH063kNu_yD8Evjfg_wro-kYWuToX1uurSe973jJNqr5aI-uosjUve7wIPtfrRmYaoSV96uC4_9CdGdsExBfsDDaWT3KnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/mohsentavoosiseo/892" target="_blank">📅 14:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سوال یکی از بچه های گروه دوره:
میشه بهم نظرتون رو بگید که چقدر تفاوت هست بین جمنای با اشتراک گوگل پرو و کلاد ؟
چرا کلاد انقدر محبوب شده و اقلای طاووسی هم دارن تاکید میکنن روش؟
تفاوت سطحش با جمنای در چی هست ؟
خصوصا برای تولید محتوا تجربه دارید جفتش رو مقایسه کنیم؟
البته چون اپدیت جدید در حال ضبطه این سوال پیش اومده براشون
😎
. پاسخ:
https://www.instagram.com/reel/DcBLYe_MLHx/
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/mohsentavoosiseo/891" target="_blank">📅 14:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پاسخ سوالات پر تکراری که درباره دو پست بالا پرسیده شد:
❓
آیا ما که قبلا دوره رو خریدیم دریافت می کنیم این اپدیت رو؟
بله! فکر کردید من شرکت های خودروسازی داخلی هستم؟ حالا که بازی قشنگ شده جدا شیم؟ شما همراهان قدیمی رو تنها بذارم؟ هوای شما رو که بیشتر باید داشته باشم! پشتیبانی هم دو نفره شده از دو نفر قوی. قدیمی های سال اول خبر ندارند پشتیبانی تلگرامی دارند. جایی دیدید بیفته دنبالتون بگه این ویژگی اضافه شده بیا دریافتش کن. قبلا پولش رو دادی. من میگم! الانم گفتم
😎
❓
این اپدیت چه زمانی منتشر میشه؟
شما تا پایان 2026 روش حساب کنید. خودم نمیدونم. در حال ضبطم. دوسه ماه طول میکشه حداقل. همین ماه البته فصل اولش میاد که البته سبک هست فصل اولش.
❓
من تهیه کردم ولی اون دوره بین المللی، توش خالی هست هیچی نیست!
بالاتر گفتم، اون رو تا اخر 2026 حساب کنید کامل بشه. کم کم میاد در حال ضبطم. اصلا هم نمیتونم عجله کنم. شما اون یکی رو ببینید. دوره سئو جامع. سوالات بعدی هم بخونید!
❓
به درد سایت فارسی هم میخوره؟
بله. ولی مثال های من به همه زبان هاست و کلا مبتنی بر زبان یاد نمی گیرید. مبتنی بر وردپرس هم یاد نمیگیرید. اما هر زبانی و هر CMS و برای وردپرس هم یاد می گیرید.
❓
برای چه سطحی هست؟
از صفر تا خیلی حرفه ای ها. همه. ولی کسی که تا حالا پشت کامپیوتر نبوده یا در حد لاگین کردن تو سایت ها بلد نیست یا تا حالا تو زندگیش فایل word باز نکرده یا بلد نیست وی پی ان استفاده کنه، نه ها!
❓
باید صبر کنیم اپدیت جدید بیاد؟
نه! ببینید دوره فعلی رو. دوره جامع فعلی که دسترسی دارید، کامل و به روز هست. اگر خیلی بی حوصله هستید از فصل "تحقیق کلمات کلیدی و صفحه بندی در عصر هوش مصنوعی" شروع کنید. همش مهم هست و موثر و به روز و کاربردی.
❓
میشه فقط آپدیت AI سئو بین المللی رو جداگونه بگیریم؟
کلا یکی هست! صفر تا صد هست. هوش مصنوعی جدا نیست. بین المللی هم جدا نیست. قیمت دوره هم بسیار پایین هست بخاطر جنگ. کلا امکان بخش خاصی رو جدا خریدن وجود نداره. یا همه یا هیچ هست.
❓
سرفصل های این اپدیت جدید که تصویر یک دوره جدید گذاشته بودید چی هست؟ تو صفحه دوره فعلی سر فصل های این اپدیت هست؟
اون عملا میشه محتوای فصل سئو بین المللی همین دوره جامع، که صفر تا صد سئو به هر زبانی و کاملا آمیخته با هوش مصنوعی(Claude) هست.
توی صفحه فعلی دوره، این سرفصل ها نیست. اما اگر بخرید، این ها هم دریافت خواهید کرد:
موضوعاتی که در آپدیت، پوشش داده میشه این هاست ولی دقیقا عنوان سرفصل ها این نیست. به دلایل متعددی، فقط کسی که دسترسی داره، عنوان ها و سرفصل ها رو دقیق میبینه بعد از انتشار:
🟢
مباحث کار با هوش مصنوعی، OKF, Skill، اسناد AI، Memory، MCP, Connectors.
🟢
انواع SERP در گوگل در در زبان ها و کشور های مختلف
🟢
کسب رتبه در Google Shop (Merchant)
استاندارد سازی پروژه ها با هوش مصنوعی
آنبوردینگ انسان و Agent
🟢
کسب رتبه در کشور خاص، زبان خاص، یا جمعی از کشور ها و زبان ها یا به صورت کلی کسب رتبه و افزایش شانس نمایش و پیشنهاد توسط AI به صورت بین المللی (مثل
booking.com
)
🟢
ساخت پلاگین لینک داخلی خودکار با کلاد برای وردپرس با وایب کدینگ.
🟢
ساخت دسته جمعی صفحات سایت با AI
🟢
تحقیق بازار شامل Intent, Keyword و محدوده سوالاتی که از AI پرسیده می شود.
🟢
ساخت صفحات (تارگتینگ، کلاسترینگ به روش محسن طاوسی. نه اینکه هرکاری اکثریت کردند شما هم بکنید و فرصت ها بسوزند!)
🟢
سئو تکنیکال برای گوگل، بینگ و AI ها.
🟢
بهینه سازی داخلی سایت.
🟢
تولید محتوا با AI
🟢
کسب لینک از کشور ها و زبان های مختلف
کل بحث Off-Page
🟢
هرس صفحات و بهبود نرخ خزش
🟢
چند زبانه کردن سایت از نظر SEO
🟢
گزارش نویسی به هر زبانی
با تمام سرفصل های بالا، AI آمیخته شده است. کلا همشون با AI هست. بیشتر کلاد (اختصاصی از خود کلاد) و تا حدی هم Gemini
جهت خرید، به
@mohsentavoosisupport
پیام بدید. من نیستم پشت این اکانت. بچه ها هستند.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/mohsentavoosiseo/890" target="_blank">📅 18:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
قیمت دوره، قرار بود سال 1405 بشه 18 تومن. بخاطر دو تا جنگ و دی ماه، با مبلغ پایین تر در دسترس شد و از 1 شهریور(هفته دیگه)، مشه حدود 6. و سپس هر ماه یا هر سه ماه، افزایش قیمت داره. و طبق معمول، تخفیف دوره ای و مناسبتی هم نداره و هر ماه یا هر 3 ماه، افزایش تدریجی داره.
کاهش قیمت بخاطر جنگ بود و هست. کسی که پارسال 12 تومن میداد، امسال 5 تومن رو سخت تر از اون 12 تومن پارسال میده. درامدش فرقی نکرده و هزینه هاش هم سه برابر شده!
✅
به نقل از خود شرکت کنندگان دوره میگم که در هایتلایت اینستاگرامم هم گذاشتم:
اگر اهل یادگیری سئو یا نمایش یا فروش بیشتر در AI ها هستید یا میخواید اپلای کنید یا پروژه بگیرید، یا کسب و کار خودتون در داخل یا خارج رو به هر زبانی، گسترس بدید، اگر دوره رو ندارید یا نگیرید، احتمال پشیمونی و حسرت که چرا زودتر نگرفتید بالاست. به نقل از خود بچه ها.
❕
اما در عین حال، تضمین نمی کنم. هیچ تعهد و در باغ سبزی هم نشون نمیدم. صرفا هر آنچه دارم رو در دوره آموزش میدم که هر کس با من جلو بیاد، قوی، حرفه ای، بازای و تجاری و بین المللی و با زیرساخت درست بالا بیاد و آبکی نباشه آموزشش و
احتمالا
به چرخه عوض کردن دوره های مختلفش پایان بده.
🟢
قبلش تحقیقات خودتون رو انجام بدید. اگر ذره ای شک داشتید، تهیه نکنید. پولی که با شک پرداخت می کنید برای من جذاب نیست.
و در نظر بگیرید، برای کسب و کار خودتون، خرج نقدی میخواد. فکر نکنید فقط یادگیری هست. پول هم باید خرج کنید. مگر اینکه بخواید استخدام بشید یا پروژه بگیرید.
خرید در:
@mohsentavoosisupport</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/mohsentavoosiseo/889" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-888">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOfF02RDYP5FHuFF3yIKSrq6ZaqWw0Ue4Se7iY3imuOTeGU9-J1Z3QodzmFfD9iMP1fUeJhbBeJTlRPwBo7kqHlWX8MRM6JGeVy903ZCkHftjLGyZoUdx8b9C14WkHBv7Lo1LyUpHVMMhMjk4Cp3BIREGFcBy6m1HMF0zPSm7oClYT118_h185CQu5VTV3Bad19M4Urj_N4OzsTf3yYCGIeEVyeOIgQjI-OvR108EU4V-DQqSNutqrwSfuYkZFwVyZT4wc_BCuRmFQEMzfBPigrmSQjRey2jhjv1UrDi9PgI0mlq6ucaR4-bzNmk2a_LaMHhVQO6IvHV8NK9vAUpAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسانی که جدیدا دوره رو میخرند، دو تا دوره دریافت می کنند(قدیمی ها نگران نشید تا آخر بخونید).
دوره جدید، برای راحتی ذهن شما جداگونه قرارداده شده و دوره صفر تا صد SEO و AEO برای همه زبان ها و همه کشور هاست! و کاملا آمیخته با AI که ابزار اصلیمون Claude هست. کلاد اختصاصی در محیط خود کلاد. نه این Opus که هوش مصنوعی های ایرانی و خارجی، میفروشند.
البته بگم من مثال هندی پاکستانی نمیزنم. ولی از شرق آسیا یعنی ژاپن، تا قاره آمریکا رو پوشش میدم. آلمانی، ژاپنی، ترکی استانبولی، روسی، فرانسوی، اسپانیایی داریم. فارسی و انگلیسی هم که سرجاش.
این آپدیت احتمالا تا آخر مهر کامل میشه و برای قدیمی ها در فصل سئو بین المللی قرار میگیره. و برای جدید ها، در این یکی دوره
هم
قرار میگیره.
خرید در:
@mohsentavoosisupport
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/mohsentavoosiseo/888" target="_blank">📅 14:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کلاد، برای هر متخصص SEO و هر متخصص دیگه ای ضروری هست و یک هزینه جاری هست. شما میگید من غذا نمیخورم؟ سوار وسیله نقلیه نمیشم؟ اجاره خونه یا پول قبض نمیدم؟
کلاد هم بهش اضافه کنید. بایدیه. اونم اختصاصی. نه اشتراکی. اصلا با محدودیتی که کلاد رو اکانت هاش داره اشتراکی معنا نداره. با این همه قابلیت، فقط چت نیست! باید اختصاصی بگیرید.
اپدیت دوره که تو همین شهریور یک فصلش میاد، کلا با Claude هست. کوبیدم از اول ساختم. نه فقط ایرانی و فارسی. نه فقط حتی انگلیسی! هرچند Base همون قبلی ها هست که الان هم تو دوره هست. فقط یک ابزار قدرتمند بهمون اضافه شده.
به زودی سورپرایز خواهید شد!
😎
پی نوشت:
(کلاد تلفظ انگلیسیش کلاد هست)، ریشه اسمش فرانسوی هست که میشه کلود. شرکت آنتروپیک هم آمریکایی هست.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/mohsentavoosiseo/886" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ابزار های سئو خارجی رو به صورت اشتراکی از کجا تهیه کنیم؟ از سایت لیمیت پس! Limitpass.com ایرانی چطور؟ ابزار جت  سئو و کیورد چی و چند ابزار خوب دیگه...  http://limitpass.com/ https://www.jetseo.ir/ https://keywordchi.com/    کد تخفیف سه سایت بالا:  mohsentavoosi…</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/mohsentavoosiseo/885" target="_blank">📅 20:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یکی از
شاخص های سواد از نظر یونسکو
، توانایی یادگیری زدایی(unlearning) و یادگیری مجدد و توانایی استفاده کاربردی از دانش خود است.
خیلی از آموزش هایی که ما میبینیم فقط احساس یادگیری میده و چیز کاربردی یاد نمیده.
نه باعث افزایش درامد میشه. نه اپلای و کسب موقعیت شغلی بهتر، نه پروژه گرفتن و نه حتی نتایج و راحتی بیشتر و بهتر و کم خرج تر برای بهبود رتبه گوگل و شانس پیشنهاد شدن در AI!
خب الان فایدش چی شد؟ درک بیشتر تا یه حدی معنی داره. ارزش داره بری اتحاد، مشتق، انتگرال، اعداد مختلط، سری فوریه رو یاد بگیری که بعد بهتر بتونی مثلا معماری ساختمون انجام بدی؟ یا کد بزنی؟
اگه اعداد مختلط نون شد اومد سر سفره، یا ماشینتو عوض کردی یا خونتو یا دارایی هات رو یا زندگیت با کیفیت تر شد، قطعا مسیرت درسته.
حالا به جای این ریاضیات، هرچیزی بذار. از الگوریتم های گوگل تا مستندات و نحوه کارکرد مدل Fable کلاد تا... .
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/mohsentavoosiseo/884" target="_blank">📅 20:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">با توجه به اینکه فصل اول اپدیت جدید، که یک دوره کامل جدید هست،
با عنوان "سئو بین المللی با AI با پوشش GEO/AEO" ضبطش شروع شد و زودتر از موعد(زودتر از آبان 1405)، منتشر میشه، قیمت دوره از 1 شهریور 1405،
⭕️
افزایش خواهد داشت و بین معادل 40 تا 80 دلار خواهد شد.
و طبق معمول هیچ کمپینی برگزار نمیشه و به جاش سال به سال، افزایش داره.
انقدر که آمیخته با AI (Claude) و مباحث بین المللی و چند زبانی و چند فرهنگی هست، برای من حتی تدوینش و ضبطش هم خیلی جذاب هست.
کسانی که به دوره فعلی(دوره جامع سئو) دسترسی کامل دارند، در فصل سئو بین المللی، این دوره جدید (اپدیت بزرگ) رو دریافت می کنند.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/mohsentavoosiseo/883" target="_blank">📅 20:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
این پست حاوی ایده درامد دلاری و افشاگری پشت پرده هست. دست به دست پخش کنید که در جریان قرار بگیرید پشت پرده چه خبره یا خودتون ازش استفاده کنید:
این نظر سنجی که روش ریپلای زدم رو یادتونه؟
نتیجش این شد که من ورود نمیکنم بهش. ولی شما ورود کنید! در ادامه میگم چرا من ورود نمیکنم.
اینجا بهتون میگم ممکنه برای بعضی ها به صرفه باشه خودتون کاسبیشو راه بندازید:
(توجه: لینک ها درست هستن. با آی پی ایران نرید. من لینک غلط نمیذارم! راهشو پیدا کنید و باز کنید لینک هارو)
https://www.trendyol.com/google/gemini-pro-18-ay-kisisel-mail-e-davet-p-1098587629
این جمینای رو میده240 لیر 18 ماهه. یعنی حدود 1 میلیون تومن. یعنی اگه ویزامستر کارت داشته باشی میخری. اصلا نداشته باشی هم میخری. میدی برات میخرن.
حالا اگه خواستی کاسبی راه بندازی این میشه یکی از منابعت که ازش بخری و بیای بفروشی.
یا برای کلاد بری 150 تا Seat بخری هر کدوم میشه 20 دلار. از ریجن نیجریه میتونی تا 16 دلار و یک کم کمتر بگیری. حالا ریجن نیجریه رو باید با اپل آیدی نیجریه ای بگیری. برای هر 150 تا اکانت که میفروشی(max seats) باید یه اپل ای دی جدا داشته باشی. برای اپل آی دی جدا هم باید از نامبرلند یا هرجا شماره مجازی نیجریه بگیری. ریسک های از دست دادن اکانت اپل و شمارت هم در نظر بگیر.
بعد باید بشینی مدیریت کنی اکانت هایی که میدی رو. و اکانت هایی که تمدید نمی کنن رو. چون از کارتت سر ماه کم میشه مگر اینکه لغو کنی.
من خودم حدود ده تا دونه، یک مدت کوتاه اکانت chatgpt فروختم و خیلی ها هم دوباره پیام دادن که باز هم میخوان. یادتونه؟ چرا متوقف کردم؟ از کجا خریدم خودم؟ از اینجا:
https://www.trendyol.com/openai/chatgpt-plus-aboneligi-kendi-mailinize-davet-ile-tanimlanir-p-947506812
اون موقع میداد 100 لیر و دعوت نامه ای بود! بعد ناگهان تمام سایت های ترکیه، ناموجود کردند! همه با هم! الان میده 600 لیر. یعنی 13 دلار حدودا. باز زیر قیمته.
از اینجا هم میخریدم:
https://www.epinline.com/chatgpt-plusgpt-5dall-e-vip-1-ay-p-26417-m-1
این الان یک ماهه میده 350 لیر. میشه حدود 7.8 دلار.
آیا برای من صرف داره از اینجا بخرم 8 دلار بفروشم 18 دلار اصلا؟ کمتر از 20 دلار خود chatgpt؟ بله ارزش داره!
یعنی رو هر اکانتی که میفروشی حتی دو دلار کمتر از سایت اصلیش، باز بین 5 تا 12 دلار سود میکنی. گاهی هم ممکنه سودت در حد 2 دلار باشه.
این جمینای یک ساله رو میده 150 لیر. یعنی 3 دلار!
https://www.epinline.com/gemini-google-pro-12-ay-mail-adresinize-davet--p-27078-m-1
هزینه جاری خرید اکانت ها، مدیریت، پشتیبانی، تبلیغات و اینکه اطمینان کنن ازت بخرن هم در نظر بگیر.
من بخش اعتماد کاربر و اطلاع رسانیش رو داشتم. با بخش مدیریت و توسعه پذیریش به نسبت دردسر مدیریتش تا رسیدن به سود ماهی 2.3 هزار دلار به صورت غیر فعال(بدون درگیری خودم) اکی نبودم. اگه یه روزی بفروشم، همینه روش کار. حداقل پایه اش اینه. فعلا اصلا ظرفیت ندارم برای پروژه جدید باز کردن تو زندگیم.
و خیلی ساده با گذر زمان همه این پست رو یادشون رفته. من یه پست میذارم میگم اکانت میفروشم. خوبی تلگرام و اینستاگرام همینه که با گذر زمان کسی برنمیگرده پست های قبلی رو بخونه
😅
😎
شاید هم همین الان یکی از بات های فروش این اکانت ها مال منه! از کجا معلوم؟ خدا میدونه
😶
حالا به شما گفتم! قطعا برای خیلی ها به صرفه هست برن تو کارش!
هم سایت بزن هم ربات تلگرام. خیلی راحت با کلاد بنویس ربات رو با وایب کدینگ(همین الان بات احراز هویت و ارتباط با پشتیبان های دوره من، همینطوری نوشته شده توسط خودم با کلاد).
بعد هم پول بده تبلیغ کن جا بنداز پشتیبانی خوب هم بده. این بخش از خود تامین، سخت تر هست. اول فروش. دوم فروش. سوم فروش. بعدا محصول. قطعا باید بها بپرداخت برای اینکه بشناسن محصول شما رو و اعتماد کنن. خیلی بیشتر از بهای خرید و تهیه و تامین خود محصول.
رفع مسئولیت: من فقط تجربه خرید خودم از این سایت ها و دانسته های خودم رو گفتم. هر قدمی برمیدارید خودتون مسئولید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/mohsentavoosiseo/882" target="_blank">📅 14:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igK6GNg_lU3LiBmbIOU5MYO1Kj3Kc_NoRdiGJCNxPJoPcMDw0EL1nGj_yyGaVpVVzNjGOOgei7hU_EWFXJaYmwVQ5qS1CdAi8q2VIDfj_JYR4yg4JJDpC7HUHUCIAK-r6KE6cKZcIvSWlqOYQEKQL8tZbTznqyVA_TlPC7D7XXYiRrrLsch2wYFmyLo9eS1AIur6z70UkITT5Qh-BbhOdUKRoVoVX_ZbsVPdBmdMq7sm0R64E5JbYzMv8V1iY47I8PQBxQBh5nTV-3i5PCiLVrOYr6IARa0uGyAXe75Roz240LP6GCZ3iKatJAqzJYUxvziysBePX03FdM6XK_u1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یکی از ساده ترین هنرکاری های کلاد هست! از منوی رفلکت، بهتون عملکرد خودتونو میگه و واقعا بازخورد های جذابی میده! در اپدیت پیش روی دوره، تمام کسانی که دوره رو دارند، سئو بین المللی با کلاد رو به خشن ترین حالت ممکن یاد می گیرند
😎
.
به من گفته:
ایراد هایی که از skill ها و عملکردشون میگیری، به خاطر دستورات خودت وسط کار هست و یادت میره که خودت خرابش کردی!
😅
یا گفته فلان جا حرف من رو بدون سند رد کردی و هنوز میگه تو اشتباه کردی!
بعد میگم کلاد خداست میگید نه! بازم میرید از فلان جی پی تی، ایرانیش رو میخرید؟ خیلی فرق داره! اختصاصی بگیرید. کانکتور و اسکیل و داکیومنت و کوورک و... تو اختصاصی هست فقط.
mohsentavoosi.com/1
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/mohsentavoosiseo/881" target="_blank">📅 15:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEU8xPPy_6ld0b7SrxM79ERu660w_QwNfRBT8JounBuUREvuEF-1tEyJj-XGpoGgHrT_K5772gvlIpRnQK8JreXyPWfCKjNU-Ivn3TZtiUbB_wBjm1eSlos_HJ_LQ_T1RfSi73HnOEJBeKDQE0pB3BoqCuFtpdWzj790l6pF0kobZ-8HHdGh0wVVvyRgnoMnfWOoXDkBia-rtSbuVE3m2G_o4NxUXxo8skKZceIaz9Den7y4hW0Uf2OgtQCdz6O7acbb_P7tQR03L5Nf-Y6u1IgeaA7JlV4ZD1xfcVx2-HOoGcsPv9h-bVYTuePd1JcEUwt2LKUS1pXt1zCgrcBadA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❓️
از کدوم هوش مصنوعی استفاده کنیم؟
کلاد
❓️
با چی ایجنت بسازیم؟
کلاد
❓️
از ایجنت کدوم هوش مصنوعی استفاده کنیم؟
کلاد
❓️
از کدوم مدل ها LLM ها استفاده کنیم؟
همه مدل های کلاد. Haiko. Fable. Sonnet. Opus.
❓️
از کدوم AI های اشتراکی یا api داخلی غیر فیلتر استفاده کنیم؟
هیچ کدوم. فقط کلاد اختصاصی.
❓️
برای کد نویسی از چه AI استفاده کنیم؟
Claude Code
❓️
برای مدیریت تسک هامون و انجامشون چطور؟
Claude Cowork
❓️
برای تولید محتوا؟
کلاد
❓️
برای مردن؟
کلاد
❓️
برای...... انقدر سوال نپرس. پاسخ:
کلاد.
❓️
جایگزین کلاد چیه؟
سوال گستاخانه ای بود.
❓️
از سایت های ایرانی کلاد اوپوس گرفتم. خوبه؟
پناه بر کلاد
😭
❓️
چیکار کنم دیگه هی نگی کلاد؟
از کلاد بپرس.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/mohsentavoosiseo/879" target="_blank">📅 20:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-877">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خیلی مهم و جالب درباره گزارش نویسی و عملکرد و نقد کار خود، در ویس پایین.  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/mohsentavoosiseo/877" target="_blank">📅 13:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-875">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPXAx8Qq3_l5RC1CVfFJgQLtdGgIy5IclCF_cMb7vYkz-JKHsn0HGAl-t-nrOoU6iVmJE0Oop8BnVyzq2IiflAwZQhnIPw8GFJxGBnSRz9s2_jrtkRC4GiN4k9gqZFZAT8_bjA72I0LqWpfbRe5GSnI0yWVTJwbmk_2Cih3wJdhO2sNqGuk06AGaQHIcJM7kwtkH7XxhgRTq0Zc9PUDOxeFlstNzy0b8qgATvd5OtnIHWH0HoOieZ1ogyRDPIjfp8g2T1YuICzH1NYQOlAjoWOnhXAgiQsfxxb8-ER5pR5r-3YDH2jXctvNTWIObFy3tSuGcGx5nywAtaQKEvtStRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی مهم و جالب درباره گزارش نویسی و عملکرد و نقد کار خود، در ویس پایین.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/mohsentavoosiseo/875" target="_blank">📅 13:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYpyJzZbBn8c-877ULZuJY5_yOO1-FNK3QF0v6yknOCPONx23Xy7AR0KClbDns8My7qxUu32T4_1TXoutnT3D6YPvwvwfdY7xrzPO6wvwi9hakuA_Tn4tw-5sBC2l5614ATZW8OJGHfVJXur0PKaDov9ctGli4KkDkrDBpPqfY-uWlYEmLvB8RaM53XIdSTIfN4ycz_LdwrEzBKxTZpsvPZDa488PiVSj9senYJi6UY7DyYWEUU2za5Lye5jNpaoqY2f5k4JsvvoG-5yq5jrYze0cG2GilBfqVnJWNTqFSImm4VX3TuMoa4fUM8FWrnYixFW1hoBk3VZghkZlxyWkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUGkFRdE9-3kxGeFPuHuFIP5wbCVvnojz1ttDUseqRX_ALVGoicuqvDP4jFjgNDVzPY8RbY_KQHV3ygLiAXG5QDcEj8cqMFDgwOaXseVPkeuy6aTiglF7xknFTL0Kg0QWZKwrgKS37o-fhL-_x-p_bXuBKAsgKNJ9OKmnVDb6SoNMqeSc4isKlkQQpyf1ldCE_dvX1S8cpKOca4pAUD46lyUiZqa-KFh23FhL6m0dGEFYMKm7aKc2CtGq05K9PmOfo1QqlHQAjDi3TyniFZiKiRPDmQcTSFh7M3W1RTzMEy7rdflTxNUW1BkoL5t1MMpei39qbpc0kcHIXt_LqKLNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصویر چهارستونه(گرونتر) برای ابزار keyword tool هست و تصویر سه ستونه(ارزون تر) برای ابزار Mangools که ایرانی ها به KWFinder میشناسنش.
شما خودتون رو بذارید جای سایتی که ابزار اشتراکی میفروشه.
منگولز، روزی 500 تا سرچ میده. هر منگولز رو به 20 نفر بده، میشه روزی 25 تا برای هر نفر. نفری 2 دلار میشه هزینه خودش. کلا 40 دلار برای 20 نفر میده. میتونه تو پکیج کلیش بگنجونه.
حالا اگه کیورد تول 390 دلاری رو بده، 200 تا در روز داره کلا. به 20 نفر بده هر نفر ماهی 10 تا سرچ داره(بجای 25 تا) و نفری 20 دلار میفته براش. یعنی با دلار نرخ امروز نفری 4 میلیون تومن فقط یه دونه اشتراکیش! فکر کن حالا بخود بیاره تو پکیج هایی که حداکثر یک یا یک و نیم میلیون تومنه!
به من بگو دقیقا چطوری باید این کارو انجام بده؟ در یک صورتی میتونه! اینکه یا جمع کنه بره یا خیریه باز کنه به همه از جیب خودش ابزار اشتراکی بده.
این رو برای مخاطبین خودم پرمیوم هستند نگفتم. چون شما همه چیز رو با دید تجاری پخته نگاه می کنید و نمیگید اااا چرا گرون شد چرا نیست. میفهمید پشت قضیه چطور هست.
برای کسانی گفتم که دید تجاری قوی ندارند.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/mohsentavoosiseo/873" target="_blank">📅 12:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تیم پشتیبانی رفع اشکال دوره تغییر کرده، دیگه یک نفر نیست و روز های تعطیل آخر هفته هم پوشش داده شده. مگر تعطیلات خیلی بزرگ یا استثناها.
که سرعت پاسخگویی بالاتر بره.
نه تیکتی هست نه لزوما تایپی. نه وبینار هست که بخواد ساعت خاصی برگزار شه و آزادی زمانی شما گرفته بشه یا مجبور باشید تو روزها یا ساعت های خاصی آنلاین بشید. چت تلگرام هست. بهترین حالت ممکن.
البته قبلا هم چت تلگرام بود!
خیلی از شرکت کنندگان دوره، خبر ندارن و کلا از چیزی که دارند استفاده نمی کنند.
من که مشکلی ندارم استفاده نکنید
😎
. سر بچه ها خلوت تر میشه راحت تر هستند
😎
. ولی استفاده کنید کنتور نمیندازه! نمیگیم چرا زیاد سوال میپرسی! نمیگیم چرا هر چی توضیح میدی ما نمیفهمیم! برعکس کمک می کنیم سوال رو درست بتونید بپرسید. خیلی راحت هم اگر خارج از سئو باشه یا بلد نباشیم، میگیم نمیدونیم!
"نمیدونم" گفتن تو فرهنگ ما (تیم محسن طاوسی) تابو نیست. برعکس، کسی که همه چیز رو میدونه، احتمالا کلا چیزی نمیدونه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/mohsentavoosiseo/872" target="_blank">📅 12:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سوال یکی از بچه های دوره در گروه دوره:
من سئوکار یه مجموعه هستم
قرار هست یه سایت دیگه هم بالا بیاریم و کارفرما میگن که کل محصولات همه چی رو یه صفحه باشه(  صفحه اصلی)  و تمامی فیلترها مثلا ارزان ترین گران ترین و تمامی محصولات بیاد صفحه اصلی.
و صفحه تک محصولات و درگاه و تمام
و ن لندینگ ن کتگوری هیچی هیچی
همه چی داخل صفحه اصلی
و من هرچی توضیح  میدم که این اصلا منطقی نیست از لحاظuxدرست نیست از لحاظ سئو چالشی دارید نمیشه کار کرد از همه لحاظ مشکل داره اما اصرار دارن که همین باشه.
حوزه سئویی هم حوزه خیلی سختی هست
چه پیشنهادی دارید؟؟
پاسخ:
اگه یکی اصرار کنه من ماشین با چرخ چهارگوش میخوام شما چون مکانیک یا خودروسازی باید بگی باشه؟ ولشکن کلا. نمیشه. اون کارفرما دید و اطلاعات حداقلی نداره. ولی شما که دارید.
نکته برای سوال کننده:
شما یو ایکس رو ولکن. چالش داره از نظر سئو درست نیست! کلا نمیشه. چالش یه چیز کوچکتر و معمولا قابل حله. نه یه زیرساخت مهم اصلی که بخواد وجود نداشته باشه.
و قطعا شما قاطع نگفتی نمیشه. داری چونه میزنی. اونم میخواد چونه بزنه. تخصصشو نداره که. از مدل سوال که نوشته شده "چالش داره سئوش" مشخص هست خود سوال کننده محکم نگفته نمیشه. خودشم شک داره. بدیهیه که کارفرما که دل خجسته ای داره بنده خدا و اطلاعات نداره چونه میزنه و اصرار میکنه که بشه. من ایرادی تو کارفرما با توجه به سوال(بخش چالش) نمیبینم. اون حق داره بخواد. شما حق نداری ببری رو اصرار و چالش و موضع غیر محکم. پاسخ انجام یک چیز چالش دار و با فشار نیست!
پاسخ یک "نه" و "کلا نمیشه" صد درصدی بزرگ و قاطع هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/mohsentavoosiseo/871" target="_blank">📅 23:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">درباره کمپین تبلیغات محیطی ا.......پ
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/mohsentavoosiseo/870" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/mohsentavoosiseo/869" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">https://t.me/mohsentavoosiseo/737
صفر تا صد مشکلات ایندکس شدن صفحات سایت.
❗️
دست و پا نزن برای به زور ایندکس کردن.
✅️
7 چیزی که باید چک کنید. تمام پاسخ های من به این موضوع
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/mohsentavoosiseo/868" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوستانی که ایران نیستند،
با توجه به اینکه اپدیت پیش روی دوره، بسیار تمرکزش سئو بین المللی و چند زبانه و مبتنی بر هوش مصنوعی هست،
و اسپات پلیر هم دوباره از وایت لیست خارج شده و از خارج دوباره در دسترس نیست و دیتا سنتر ها دوباره محدودیت هایی برای دسترسی از خارج به داخل اعمال کردند،
اگر نیاز به وی پی ان ایران دارید به دایرکت همین کانال(آیکون پیام یا کلید message) پیام بدید تا وی پی ان ایران براتون بفرستم. وی پی انی که خودم استفاده می کنم (میخرم).</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/mohsentavoosiseo/867" target="_blank">📅 12:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-866">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چرت تر از دو جمله زیر نمیشناسم تو زندگیم:
❌️
درخت پربارتر افتاده تر است.
❌️
هرجا خبری هست ادعایی نیست.
بولشیت کامل. Absolutely nonsense.
مغز اصلا نباید دنبال این باشه که کی متواضعه کی پرباره. هر قسمتی که برامون سودمنده بصورت متغیر و داینامیک و قسمت شده، بر میداریم و استفاده می کنیم.
❗️
نمونه انسان ها و شرکت های سوپرموفق و پر ادعا و متکبر و غیر متواضع:
✅️
استیو جابز. هم بنیانگذار اپل و مخترع صفحه نمایش لمسی و اسکرولی که همین الان گوشی ها دارند و کلی چیز دیگه.
اخلاق گند مرحوم به گوش همه رسیده.
✅️
تراویس کالانیک، هم بنیانگذار اوبر که بخاطر اخلاق گندش از شرکت خودش به عنوان مدیرعاملی اخراج شد. همچنان ثروتمند و صاحب شرکت Atoms هست که ربات تولید میکنه.
✅️
هنری فورد! شرکت بی نظیر خودرو Ford
✅️
ارسطو اوناسیس، غول کشتیرانی یونانی قرن گذشته.
✅️
لاری الیسون. هم بنیانگذار اوراکل.
✅️
پابلو اسکوبار. قاچاقچی و تولید کننده معروف کوکائین مدیین کلمبیا(مدلین که همه میگن غلطه. ل نیست. ی هست. Medellín) سی چهل سال پیش. راستی خلافکارای موفق چی؟ ادعا باید داشته باشن یا باید متواضع باشن؟
هزاران مثال می تونید در طول تاریخ پیدا کنید. کلا من با گره زدن اخلاق و کسب و کار یا موفقیت، مشکل دارم.
قطعا مرتبط و موثرند روی هم. قطعا اخلاق و انسانیت مهمه. کسب پول از راه سالم و بدون دروغ و فریب و دزدی و... مهمه. آسیب نزدن به کره زمین، طبیعت، آدم ها، همدیگه و حیوون ها مهمه و ضروریه. قطعا مهربونی با حیوانات نشانه ای از تمدن و انسانیت هست و بدرفتاری باهاشون نشانه عقب ماندگی و بربریت.
ولی خیلی گوگولی و کودکانست اون دو جمله بولشیت اول این پست درباره تواضع و ادعا.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/mohsentavoosiseo/866" target="_blank">📅 13:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/mohsentavoosiseo/864" target="_blank">📅 12:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فیچر و امکانات و قابلیت: ۱۰ درصد
فروش و به سود رسیدن: ۹۰ درصد
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/mohsentavoosiseo/863" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حالا با توجه به دو پست بالا، الان سئو مرده با هوش مصنوعی؟
چرا سرچ کنسول جمع نمیکنه پس؟ چرا فیچر وریفای کردن پیج اینستا و...هم اضافه کرده؟ اون تیم به این بزرگی دنبال چی هست برای سئویی که مرده؟ ( اون تیم، عملا تیم پر هزینه توسعه سرچ کنسول هست برای وب مستر ها که زمین بازی و دون پاشی برای محصول اصلی یعنی گوگل ادز هست).
گوگل ادز چرا نمیمیره؟ چرا رشد هم داره فروش ادز؟ مگه جستجوی کلمه ای نمرده؟ چرا هنوز آدم ها و شرکت های زیادی در سراسر جهان، کمپین های بزرگ گوگل ادز با جستجوی کلمات کلیدی اجرا میکنند؟
الان این تحلیلی که داشتیم چه ربطی به هوش مصنوعی داشت؟
چرا این سئو بجای اینکه بمیره هی قدرتمند تر و مهم تر میشه؟
هوش مصنوعی فقط تسهیل گر و سرعت بخش و بالا برنده دقت ماست برای اجرا و پیاده سازی. برای تحقیق. برای تحلیل. قبلا چرتکه بود تو فروشگاه ها. الان کارتخوان متصل به صفحه نمایش دوطرفه و لمسی هست. حتی تو خیلی از فروشگاه ها که صندوق های فول اتوماتیک هست، باز یک مسئول و یک اپراتور تنظیم و تعمیر و راهنما داره.
شما اون اوپراتور هستید که خیلی بیشتر از یک اپراتور پشت صندوق، باید حرفه ای باشید و اصول رو بلد باشید بدون وابستگی به ابزار. بدون وابستگی به CMS و وردپرس بودن یا نبود و کد سایت و زبان پروژه!
حالا شما باید کلاد رو کانفیگ کنید که خروجی خوب بده. دیتا رو درست بخونه. یه مستر(استاد و حرفه ای) باید بالاسر هوش مصنوعی باشه تو سئو.
و اون Master شمایید. کسی که به هوش مصنوعی وقتی چیزی میگه، هوش مصنوعی میگه آهان اره و ادامش میده.
اون مغز متفکر که هوش مصنوعی از رود دستش باید ادامه بده، شمایید. پس باید کامل سئو رو بلد باشید. سنتی ولی عمیق بلد باشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/mohsentavoosiseo/861" target="_blank">📅 17:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">این عکس، نمودار حدود 8 ماه گذشته یکی از پروژه های انگلیسی هست. هیچ فیلتری جز زمان هم ست نشده.  تاریخ 5 فوریه زمان شروع همکاری بوده.  به نظرتون بد شده اوضاعش یا خوب شده؟ اگه میخواید بگید نمودار پوزیشن بدتر شده پس بده که متاسفانه تحلیلتون غلطه و کل سئو رو درست…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/mohsentavoosiseo/860" target="_blank">📅 17:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBB79dC8OAeqcS6Z_TVqYmteZQALi-n1b5iPg37E-01NDZ1OOdSjX7op-kNSUS95I6zPD4vUOE8hR6C7u2wTsAnj92UcOqUZ0yUxUT25u3WzD9ZJXW0cPRmWTPxXJd4p7xbPiZ_h5Ck4WUxwyLxVMjsBdGsa0qEULgCtOqZ0X58bWhxJ0FVXnf9MCi2V7w-wsjrd6BTrnfyOwQMGhQ_oRQeT9Fdoo2WvHyeZtzEVC-oK8SEV34iX0BUbnV0PoUUEy_RYtkPoflq-Bt13s44ACfBG8lNDhkraZ49uUh-o9DihfaBoc6u9jL5ZojuaDY1aoC5B7Tz7pGWPtydAE9UJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس، نمودار حدود 8 ماه گذشته یکی از پروژه های انگلیسی هست. هیچ فیلتری جز زمان هم ست نشده.
تاریخ 5 فوریه زمان شروع همکاری بوده.
به نظرتون بد شده اوضاعش یا خوب شده؟
اگه میخواید بگید نمودار پوزیشن بدتر شده پس بده که متاسفانه تحلیلتون غلطه و کل سئو رو درست یاد نگرفتید. (
اینجا
توضیح دادم چرا).
اگر میخواید بگید کلیک ها کمتر شده در کل، پس بدتر شده، مثل پوزیشن اونقدر تحلیلتون اشتباه نیست. ولی باز هم کافی نیست. لزوما بدتر نشده.
اتفاقی که افتاده اینه که کلی صفحه با کیورد های اشتباه، حذف شدند. کلی صفحه که مانع رتبه گرفتن بقیه صفحات میشدند ریدایرکت و ادغام شدند(اصلاح تارگتینگ) و کلی صفحه بیخود که فقط باجت رو مصرف می کردند حذف شدند.
این یعنی کلیک هایی که الان نزدیک شده به کلیک زمان شروع این پروژه، نرخ تبدیل بالاتری دارند و کارفرما کاملا تفاوت تماس و مشتری از سایت رو متوجه میشه و مستقیما تاثیر مثبت مالی داره.
سوالم رو دوباره میپرسم. حالا به نظرتون وضعیت سایت بهتر شده یا بدتر؟
😎
سئو رو عمیق و درست یاد بگیریم و با دید تجاری. نه با بلغور ترجمه. نه سطحی. نه غیر کاربردی. نه با لفظ بازی بی کاربرد.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/mohsentavoosiseo/859" target="_blank">📅 17:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-858">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فلسفه زندگی من
روتین
نون کردن
پرداخت بهای غیر زمانی و غیر مالی
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/mohsentavoosiseo/858" target="_blank">📅 14:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ادامه پست قبلی:  مغزتون رو درگیر واژه ها نکنید. تو بحث پیچیده و علمی و خاص و واژه سازی حرف زدن، من پروردگار پیچیده سازی هستم! میتونم یه کاری کنم از این به بعد پست های من رو ببینید بگید ااااااااا وای چقدر این آدم خفن و با سواده. ولی کاربرد نداره و بیشتر کسانی…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/mohsentavoosiseo/857" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-855">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ادامه پست قبلی:
مغزتون رو درگیر واژه ها نکنید. تو بحث پیچیده و علمی و خاص و واژه سازی حرف زدن، من پروردگار پیچیده سازی هستم! میتونم یه کاری کنم از این به بعد پست های من رو ببینید بگید ااااااااا وای چقدر این آدم خفن و با سواده. ولی کاربرد نداره و بیشتر کسانی گول میخورن که تجربه کمتری دارند.
مهمه که انتقال مفهوم و آموزش دادن، ساده باشه، کاربردی باشه و یه نونی بده دستت یا تنور نونواییت رو داغتر کنه. وگرنه آدم ها بعد از مدتی دیدن آموزش هات، میفهمن که با واژه ها، کارشون باتو پیش نمیره.
الان همین پیلار کلاستر که من تو دوره دو فصل دربارش حرف زدم با عنوان Keyword Targeting on Pages،
شاخص داره، ل
ینک داخلی ازش در میاد،
عنوان ها ازش در میان،
نرخ تبدیل ازش در میاد،
رقابت و سرچ والیوم ازش در میاد،
اولویت بندی ازش درمیاد،
انتیتی ها خودبخود اجرا میشن،
ویژگی ها و صفت ها و کاربرد ها ازش در میان،
نالج گراف تا حد مورد نیاز و نه بیشتر، خودبخود تکمیل میشه
و به طور پیشفرض اصلا نقشه موضوعی یا Topical Map استخراج میشه.
و در نهایت منجر به رشد اعتبار موضوعی یا Topical Authority میشه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/mohsentavoosiseo/855" target="_blank">📅 14:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-854">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جمله زیر رو یکی از بچه ها در گروه شرکت کنندگان دوره به نقل از دیگری نوشت که نظرم رو در ادامه، زیرش مینویسم.
به نظر من کیورد ریسرچ به شکل سنتی خیلی وقته منسوخ شده.
اگر هنوز فرآیند سئو رو با پیدا کردن کیورد و ساختن لیست کلمات شروع می‌کنید، بهتره رویکرد رو تغییر بدید و وارد مسیرهای جدید بشید:
به جای کیورد ریسرچ، EAV Research
به جای پیدا کردن کلمه، Entity Research
به جای تمرکز روی سرچ‌ولوم، Topic Research
به جای پیلار کلاستر،  Topical Map
به جای تولید محتوا برای کلیک و ایمپرشن ، تکمیل Knowledge Graph سایت
امروز باید ببینید :
موجودیت اصلی کسب‌وکار شما چیست
چه Attribute هایی دارد
چه Entity هایی به آن مرتبط هستند
چه ارتباطی بین آن‌ها باید ساخته شود.
سئو دیگر فقط گرفتن رتبه برای Query نیست؛ ساختن یک مدل معنایی کامل از یک حوزه است که گوگل بتواند تخصص و اعتبار سایت را در آن درک کند.
این حرف، بسیار دهن پر کن و جذاب هست. اما در دنیای اجرا و عمل، برمیگرده به همون چیزهای قبل. وقتی شما به شکل سنتی کیورد ریسرچ میکنی بیشتر از 80 درصد موارد بالا، خودبخود انجام شده است.
یکی از جملات من در دوره که تو آموزش رایگان هم درباره تحقیق کلمات کلیدی در
این لینک
گفتم، اینه که تحقیق کلمات کلیدی، بر اساس صفت، برند و کاربرد باید انجام بشه. دقت کنید: صفت، برند و کاربرد.
همچنین آموزش دادم که چطور خارج از اون کیورد هم کلمه در بیاریم. مثلا برای دسته لوازم جانبی موبایل، "قاب موبایل" که توش "لوازم جانبی" نداره.
پس عملا شما با کیورد ریسرچی که من گفتم یا  خودتون به هر شکلی یاد گرفتید و اینطوری انجام میدید، بیشتر از 80 درصد جملات جذاب نقل قول شده بالا رو دارید اجرا میکنید.
حالا در این شرایط،
EAV Research و Entity Research و Topic Research و چه Attribute هایی دارد و چه Entity هایی به آن مرتبط هستند و  چه ارتباطی بین آن‌ها باید ساخته شود
خودبخود انجام شده. احتمالا نویسنده خودش روش هاش خیلی بیش از حد قدیمی بوده.
این جمله هم کلا اشتباهه:
به جای تولید محتوا برای کلیک و ایمپرشن ، تکمیل Knowledge Graph سایت.
چون اصلا نباید اینکار رو کنید به خصوص در این عصر هوش مصنوعی که AI Overview میاد از رقیب های  همین دیتا رو کامل تر از تو برمیداره و جستجوی عبارت های informational رفته سمت هوش مصنوعی.
گذشت زمانی که باید کامل راجع به یک چیزی حرف بزنی تا رتبه بگیری. واقعیت از اول هم اینطوری نبود اصلا!
یعنی برای اینکه تو "بروکر فارکس" بیای بالا لازم نیست عین همون الفبای قبلی رو درباره ترید مثل "اسپرد چیست" مثل "تحلیل تکنیکال و فاندامنتال" و... که تکرار مکررات هست بیای بنویسی دربارش.
قرار نیست برای اینکه تو کلمه "طراحی سایت" بیای بالا راجع به همه طراحی های سایت ها حرف بزنی. اصلا به این سادگی ها نیست. حرف بزن. بعد که صفحه 5 گیر کردی و رقیبت با Off-Page و ترافیک قوی و بدون هیچ نالج گراف کاملی در سایتش اومد بالا، بیا باهم صحبت کنیم اون موقع.
این جمله کلا از اساس غلطه و نویسنده حتی نمی دونه "موجودیت" یعنی چی.
موجودیت اصلی کسب‌وکار شما چیست.
یه برنامه نویس بهتر متوجه میشه entity یا موجودیت یعنی چی.
کسب و کار که موجودیت نمیشه! مجموعه ای از موجودیت های متصل به هم میشه یک کسب و کار. اگه بخوایم از نگاه اسکیما بهش موجودیت بدیم، میشه یه local business یا person یا organization. کسب و کار محلی، شخص یا سازمان. همین! الان این حس خفن بودن میده؟ واااااااای من موجودیت کسب و کارم رو دراوردم! سلطان خود پیش فرض افزونه های سئو وردپرس اینو برات میندازن اصلا. نیازی به زحمتت نبود!
اگرم منظور خود موجودیت غیر اسکیمایی هست که یک کسب و کار، یه دونه موجودیت نیست که! جمله غلطه!
انتیتی یا موجودیت یعنی یک چیز! واقعا چیز! یک thing. که جدا و قابل تشخیصه. و اسم داره، هویت داره، ویژگی داره و ارتباط با سایر موجودیت ها. الان محسن طاوسی یک موجودیت هست. اسم داره. مکان داره ویژگی داره. و تمام ویژگی های موجودیت "انسان" رو به ارث میبره.
الان حس می کنی سئو رو خیلی خفن تر بلدی؟ نه فقط مغز بیچارت رو پر از دیتای بی کاربرد کردی که تو رو از پول دور میکنه ولی احساس کاذب خفن بودن بهت میده.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/mohsentavoosiseo/854" target="_blank">📅 14:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نظر من درباره ابزار های تحقیق کلمات کلیدی:
🔴
موافق اصرار بر اینکه کیورد تول خوبه منگولز خوب نیست(KWFinder) نیستم. این صرفا یه احساس هست. واقعا منگولز یه چیز دیگست. اگر مبلغ اورجینال اختصاصیشو حساب کنیم، از کیورتول ارزون تر هم هست. خیلی هم کامل تره. سرچ با دامنه هم داره. و کلی امکانات دیگه.
🟢
فقط برای کیورد های فارسی، همون سئو سیگنالز کافیه مگر اینکه دوست داشته باشید ابزار جهانی بخرید. یعنی صرفا با سئو سیگنال چیزی از دست نمیدید برای کیورد های فارسی. اتفاقا استخراج کلمات با وارد کردن دامنه هم داره. قوی هم هست تو فارسی ها.
عدد های سرچ والیوم(تعداد جستجوی کلمات در ماه) هم خیلی روش حساب نکنید. همه ابزار ها دقیق نیستند. کلا نمیشه دقیق فهمید. حدودی هم نمیشه فهمید. ولی نسبت رو میشه فهمید. همون کافیه. رو هر عددی که ابزار ها میدن حساب کنید. اما برنامه ریزی مالی روش نکنید.
🟢
ابزار خارجی ارزون تری که اشتراکیشم راحت تر در دسترس هست، سمراش هست. Semrush جستجو با دامنه هم داره. یعنی استخراج کلمات با وارد کردن دامنه. و گپ رقبا. اما خیلی ضعیف تر از منگولز و کیورد تول هست.
🟢
برای گپ، نیازی نیست خود اون ابزاره گپ داشته باشه. من تو آموزش زیر به صورت کاملا رایگان و با گوگل شیت یا اکسل، استخراج کیورد گپ رو آموزش دادم. کافیه با ابزار ها بر اساس دامنه، استخراج کنید. بعد رقیباتون رو طبق آموزشی که گفتم قرار بدید تو شیت. خودتونم کیورد های سایت خودتونو قرار بدید تو شیت.
و خود این فایل شیت که دادم(کپی بگیرید ازش)، گپ رو میده:
https://mohsentavoosi.com/video/keyword-gap-excel/
اینم لینک کامل آموزش و مستنداتش و گوگل شیتش(تقاضای دسترسی ندید. read only هست). به جاش کپی کنید ازش از منوی File، و برای خودتون مستقل داشته باشید و هر بلایی خواستید سرش بیارید.
اگر آموزش میدید یا به کسی کمک میکنید، منشن من و منبع(اینجا) رو فراموش نکنید. من کپی کننده خارجی ها نیستم که بگید خودشوم از خارجیا برداشته و این حرفا.
❕
پی نوشت 1:
کیورد گپ یعنی رقباتون رو چه کیورد هایی رتبه یا ایمپرشن کلیک دارند و شما ندارید. شکاف کلمات کلیدی. قسمت خالی کلمات کلیدی و ضعف شما نسبت به رقباتون.
❗️
پی نوشت 2:
کامنت های زیادی زیر پستی که گذاشتم اومده که لینک گوگل شیت کجاست؟ در حالی که تو متن پست گذاشتم تو ویدیو هم کلامی و تصویری گفتم لینک رو. بخونید کامل صفحه رو.
‼️
پی نوشت 3:
ترخدا مغزتونو با استوری و پست دیدن اینستا و یوتیوب نابود نکنید. مغز خیلی ها بدو بدو شده یه صفحه رو نمیتونن یک بار بشینن کامل بخونن. پنج هزار بار درباره محتوایی که میبینن سوال تو ذهنشون ایجاد میشه چون یک بار نمیتونن ببینن و تمرکز کنن. خیلی اوضاع تمرکز ذهن ها خرابه.
‼️
پی نوشت 4:
بخدا من هم ADHD دارم یا ژنتیکی یا از محیط و عادت. ولی کنترلش کردم. من هم درون گرام یا حداقل درون گرایی قوی دارم. ولی توجیه نمیکنم(میون پرانتز، توجیه رو توجیح ننویسید)  که چون از درون انرژی میگیرم، پس ارتباطات بلد نباشم یا خجالت بکشم، و بگم من خجالت و بلد نبودنم اشکال نداره چون درون گرام!
درونگرا باید بتونه جلوی پنج هزار نفر سخنرانی کنه حتی با تپق ولی بدون خجالت و بتونه احساساتشو در جمع بیان کنه. اگر نمیتونه ربطی به درون گرایی نداره. به خدا قسم نداره. اگر آتئیستی به خاک استیفن هاوکینگ و داروین قسم که بی مهارتیه. شرم الکیه. جای رشد داره.
درون گرا فقط از درون خودش بیشتر از بیرون انرژی دریافت میکنه. شارژش تو تنهاییه. همین! چه ربطی به خجالتی بودن و بی مهارت بودن تو ارتباطات داره؟!
یه ای دی اچ دی در سطحی که تو جامعست(نه بچه هایی که از سنین کم اختلال یادگیری دارند)، هم میتونه یاد بگیره تمرکز کنه. بدون قرص. یه بار هم که شده مسئولیت خودمونو گردن بگیریم. تو این عصر هوش مصنوعی میخواید همچنان بدو بدو همه چیو ببینید؟ چجوری میخواید AI Agent تربیت کنید پس؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/mohsentavoosiseo/852" target="_blank">📅 17:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a9cb06f1.mp4?token=pzOHy1Irhi63kl790HbhrAfXSO7SbPcvnn1CW7DvZ8t1TuS0oxweuKau_hp17fh1vsyHpEclumqXMmmFzp0C5Yigwg0TY2Yd3LIIZ_zhC8qisgU7X9wlHx3VsDyJ7-UZnFPIGCiy1JtNrDi9trCIdQtQKfqUPGhW5UtjIn3u_yFhoOnpmrgDt8mwGBqveoLBkWPRVjI1pZjWxWv39HwVTmYavtpyCSMn5ZXCBID-cnvd5TLQdN8fsF7JN7nEFUb6ORJKIBjKkSLGm20l9VDP4XGzOCvbS7AVBO1z9VzBQ1V9CcEOiDkPp6bSlLLlFbUCybZK9sEPzcdpDHqDPe9SYzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a9cb06f1.mp4?token=pzOHy1Irhi63kl790HbhrAfXSO7SbPcvnn1CW7DvZ8t1TuS0oxweuKau_hp17fh1vsyHpEclumqXMmmFzp0C5Yigwg0TY2Yd3LIIZ_zhC8qisgU7X9wlHx3VsDyJ7-UZnFPIGCiy1JtNrDi9trCIdQtQKfqUPGhW5UtjIn3u_yFhoOnpmrgDt8mwGBqveoLBkWPRVjI1pZjWxWv39HwVTmYavtpyCSMn5ZXCBID-cnvd5TLQdN8fsF7JN7nEFUb6ORJKIBjKkSLGm20l9VDP4XGzOCvbS7AVBO1z9VzBQ1V9CcEOiDkPp6bSlLLlFbUCybZK9sEPzcdpDHqDPe9SYzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
تو جشنواره تریبون، رتبه‌ات رو برگردون
🍀
تا ۸۰٪ تخفیف خرید رپورتاژ
🌼
تا ۶۰٪ تخفیف خرید بک‌لینک
🌿
۲٪ کش بک روی هر سبد خرید
🌼
رپورتاژ رایگان و امکان پرداخت قسطی
🍒
فقط تا ۳ مرداد
🍊
همین الان وارد جشنواره تریبون شو و رتبه‌ات رو برگردون
اطلاعات بیشتر در:
⬇️
tribn.ir/Vrfz6P
tribn.ir/Vrfz6P
ℹ️
این پست، تبلیغ هست. Ad
ℹ️</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/mohsentavoosiseo/851" target="_blank">📅 16:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستان اینجا کسی هست تو عنوان نویسی رپورتاژ قوی باشه ؟
چه جالب مگه عنوان نویسی شاخه جدایی داره خوب هر کی مقاله رو بنویسه عنوانم در میاره دیگه! مگه اینجوری نیست!؟
Are you kidding? Realy?
واقعا بعد از دیدن دوره و این همه ویدیو و سرفصل، سوال دوم بالا سواله؟
😭
😭
یعنی تولید کننده محتوا اطلاعات داره از سرچ والیوم و ابزار کیورد ریسرچ و میانگین موضوع کیورد و سایت شما و سایت رسانه رپورتاژ که این همه تو دوره ویدیو داره؟
طبیعیه که ادم ها دوره رو کامل نبینن. ولی بهتر نیست سوال شه که ااااا راجع بهش تو دوره هست؟ کدوم فصل ها کدوم ویدیو ها؟
تو این عصر هوش مصنوعی همه رو از AI میپرسی یا از دانشگاه یوتیوب! پس قطعا من باید ارزش افزوده دیگه ای داشته باشم. وگرنه که این همه مدرس. این همه آموزش رایگان. این همه منبع.
اگر دوره من رو دارید، ببینیدش! استفاده کنید ازش. دریاییه که تو محتواش غرق میشید. ولی موج سوار تو دریای طوفانی بیرون میاید.
THANKS FOR YOUR ATTENTION TO THIS MATTER. PRESIDENT MT.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/mohsentavoosiseo/848" target="_blank">📅 00:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/mohsentavoosiseo/847" target="_blank">📅 18:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دوستانی که اکانت کلاد خریدند و تجربه موفق دارند و بن نشده لطفا تو دایرکت همین کانال اعلام کنید.   با توجه به نظر سنجی بالا من نمیبینم توی خودم که ماهانه به ۱۰۰۰ نفر بفروشم. نهایت میشه ۱۰۰ نفر با کلی دردسر. میشه حداکثر ماهی ۲۰۰ دلار با کلی مکافات.   پس من ورود…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/mohsentavoosiseo/846" target="_blank">📅 14:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-844">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دوستانی که اکانت کلاد خریدند و تجربه موفق دارند و بن نشده لطفا تو دایرکت همین کانال اعلام کنید.   با توجه به نظر سنجی بالا من نمیبینم توی خودم که ماهانه به ۱۰۰۰ نفر بفروشم. نهایت میشه ۱۰۰ نفر با کلی دردسر. میشه حداکثر ماهی ۲۰۰ دلار با کلی مکافات.   پس من ورود…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/mohsentavoosiseo/844" target="_blank">📅 12:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دوستانی که اکانت کلاد خریدند و تجربه موفق دارند و بن نشده لطفا تو دایرکت همین کانال اعلام کنید.
با توجه به نظر سنجی بالا من نمیبینم توی خودم که ماهانه به ۱۰۰۰ نفر بفروشم. نهایت میشه ۱۰۰ نفر با کلی دردسر. میشه حداکثر ماهی ۲۰۰ دلار با کلی مکافات.
پس من ورود نمی کنم به اینکار. و میخوام شما بگید از کجا میگیرید که عمومی بذارم بقیه هم برن بگیرن. کلاد بدون دردسر و بدون محدودیت.
از یک سرویس عمومی که همه بتونن. نه دوست و آشنا و کارت خارجی خودتون.
بگید که منم به بقیه بگم. تو دایرکت کانال بفرستید.
اگر ا......ت بوده فقط اگه بعد از اون بن شدن های دسته جمعیش بوده باشه بگید.</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/mohsentavoosiseo/843" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/mohsentavoosiseo/842" target="_blank">📅 15:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-841">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/mohsentavoosiseo/841" target="_blank">📅 15:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ربطی به سوال بالا نداره. کلی هست.
با کلاس و بی کلاس در تعریف من.
پرداخت به هرچیزی جز خود‌ عیب جویی از هرکسی جز خود. مطابق مطالب زرد و سطحی.
#تروما
#آسیب
#سمی
#طرحواره
#تله
#عیب
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/mohsentavoosiseo/840" target="_blank">📅 15:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/mohsentavoosiseo/839" target="_blank">📅 14:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-838">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/mohsentavoosiseo/838" target="_blank">📅 14:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پاسخ سوال بالا، قسمت ششم
در تجارت، تواضع اشتباه هست.منت گذاشتن بسیار مهم و جایز هست. ترکیب تضادها در کار.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/mohsentavoosiseo/837" target="_blank">📅 14:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پاسخ سوال بالا، قسمت پنجم
انتقال پیام پنهان ضعف
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/mohsentavoosiseo/836" target="_blank">📅 14:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پاسخ سوال بالا، قسمت چهارم
هم خدا هم خرما. در نظر گرفتن استاندارد تخفیفی.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/mohsentavoosiseo/835" target="_blank">📅 14:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/mohsentavoosiseo/834" target="_blank">📅 14:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/mohsentavoosiseo/833" target="_blank">📅 14:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/mohsentavoosiseo/831" target="_blank">📅 13:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJJ5P029Oqnd7boJcFx1OUA463PNcsGoAnPARfkKlXVY5wMJ9l6sTdASLKikxkow7gng72896EYdfnK0dcqyEewF4EKi-XJDTuVMdwdKB37gOXYy3htCvcutPg3qJrFr5V3EiW_WkB7EX1zcLKWN_VbkotOWnDF-qa5JG01Tu23_4AeN8IS3yqjy8iQ0RkPlGrxhmuioIKQNPnk2R9HbLL_U0n3ARIDHwqOTos5EA_yBBsSa9stKyRzQ9YnUK-oEyDsDgL3VUVuJxVgWJOtqc4rfKhcTOD7y7pWSIKc3ebhxZf_347ltGpHlePrOixB74MlcG6_Rkypgm0ka9TFb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/mohsentavoosiseo/830" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره ( مثلا تخفیف بگیره یا نگه داره فردا پس فردا نکنه) ؟
حس‌میکنم این بازاریا وقتی دادن پولتو یک روز هم بیشتر طول میدن احساس برنده بودن میکنن . اینو چطوری بهش غلبه میکنین
مثلا طرف قفل میکنه تخفیف بده
یا همشو نمیدم نصف میدم نصف یوقت دیگ
وقتی سفت میگیری کلا ناراحت میشن و کار نمیگیره وقتی هم که راه میای باید داستان داشته باشی
نه که ندن ولی پولو از ارزش میندازن یبار
جواب سوال بالا در ادامه.(یه پادکست ضبط کردم. طولانی شد ویس ها).
#پروژه
#پروژه_گرفتن
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/mohsentavoosiseo/829" target="_blank">📅 13:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یه کلاس زبان عمومی باید برای کلمه "People" قرار بدیم. اینجوری فایده نداره. خوب نیست دیگه انقدر آدم بی سواد باشه در عصر هوش مصنوعی که مترجم در لحظه و رایگان در دسترس هست.</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/mohsentavoosiseo/828" target="_blank">📅 12:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پاسخ سوال بالا
https://t.me/mohsentavoosiseo/826
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/mohsentavoosiseo/827" target="_blank">📅 21:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-826">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سوال از پشتیبان دوره(سانسور شده):
من دسترسی کامل به دوره دارم و دارم رو سایتم کار می کنم.
کارفرما اومده بهم میگه که یه محصولی به نام x یا خرید x ما تقریبا از سه ماه پیش اومدیم روی رتبه یک و محصولی بوده که تقریبا فقط ما داشتیم.
الان رقیبمون هم این محصول رو موجود کرده. در صورتی که دو سه روزه محصول رو تو سایت گذاشته و اومده لینک دو. اما ما خیلی طول کشید تا بیایم لینک یک.
من جواب لحظه ای که به کارفرما دادم این بود که شما سرمایه گذاری درستی روی سایتت نکردی الان سایتت از نظر UX و پرفورمنس و اعتبار و off page  صفره و مسلمه که سایتی با این اعتبار سریع میاد لینک دو و بعد ما.
الان کارفرما میگه با من با عدد حرف بزن و منطقی بهم بگو که دقیق چیکا کنم که تا چند روز اینده این سایت نیاد جای من که رتبه یک هستم رو بگیره.
پاسخ در voice پیش رو:
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/mohsentavoosiseo/826" target="_blank">📅 21:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/mohsentavoosiseo/825" target="_blank">📅 22:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-824">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بخاطر احترام به حقوق تولید کننده تصویر لینک پستش رو میذارم. ولی حرفم خود تصویر نیست.  بعد از نظر سنجی پایین، چیز دیگه ای میخوام بگم.</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/mohsentavoosiseo/824" target="_blank">📅 22:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-823">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-poll">
<h4>📊 این تصاویر رو می بینید کامل؟</h4>
<ul>
<li>✓ نه فقط کلی نگاه میکنم ببینم راجع به چیه.</li>
<li>✓ کلا حوصله ندارم ببینم اینارو</li>
<li>✓ کامل میبینم. دونه دونه فرایند ها و تصاویر و عناوین و متن هاشو.</li>
</ul>
</div>
<div class="tg-text">بخاطر احترام به حقوق تولید کننده تصویر لینک پستش رو میذارم. ولی حرفم خود تصویر نیست.  بعد از نظر سنجی پایین، چیز دیگه ای میخوام بگم.</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/mohsentavoosiseo/823" target="_blank">📅 18:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TL6f0_wcWQOXjacdisRrIjmTZuCUOgSvbZI2AJ2yM_lmgsNgJ7sr0_ks1LlrF9QTV0dNRvOr0jwx5Fy4WrTLTDG77yxEfo6N8pFBRjdO0MMj3V4wGVOrMZ6pG-5tin3VvPquvPAd8qIQe4w3-h7Ni_9ThS47_5WrhGyeDPxoVYUFAGJSVQI1dI5s9H9NJYunvD5btKL-8fKwn2WZWrDIhOt9EcQFI-aUwKxtz8hh8sMDRX6zfBZo6V2_qtzQJMbdLlhMH2hRHAQ9DrLv4XBXVPj2Kce4UIalfLP1PgVG0yMByKazujU6l-8fy3vBIHaMJt_Vhy9PatPVM0AkP-RBtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر احترام به حقوق تولید کننده تصویر
لینک پستش
رو میذارم. ولی حرفم خود تصویر نیست.
بعد از نظر سنجی پایین، چیز دیگه ای میخوام بگم.</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/mohsentavoosiseo/822" target="_blank">📅 18:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اگر از داخل ایران وصل میشید، کشور رو یک کشور در نظر بگیرید و هربار یه کشور نشه. جوری نشه که انگار طی الارض دارید صبح آلمانید یک ساعت بعد آمریکا یک ساعت بعد ترکیه. (بیاید فرض کنیم پیاده از مرز سوئیس نمیرید آلمان و بین مرزهای شنگن در حالی که کلاد رو باز می کنید).</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/mohsentavoosiseo/819" target="_blank">📅 18:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-818">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کاهش احتمال مسدود شدن اکانت Claude
بجز اکانت گوگلی که باهاش تو کلاد لاگین میشید و بجز کارتی که باهاش پرداخت میشه،
اگر از داخل ایران وصل میشید، کشور رو یک کشور در نظر بگیرید و هربار یه کشور نشه. جوری نشه که انگار طی الارض دارید صبح آلمانید یک ساعت بعد آمریکا یک ساعت بعد ترکیه. (بیاید فرض کنیم پیاده از مرز سوئیس نمیرید آلمان و بین مرزهای شنگن در حالی که کلاد رو باز می کنید).
و چک کنید وی پی ان رو با یک سایت تحریم(بدون شکن) مثل
https://developers.google.com/search/docs
که 403 نده. اگه سایت های فیلتر براتون باز میشه ولی 403 میده این ها، یعنی به راحتی وی پی انتون قابل تشخیص هست که از ایران وصل میشید.
همچنین توی  incognito یا private mode مرورگر، وارد سایت
https://whatismyipaddress.com/
بشید و ببینید کدوم کشور هست آی پیتون.
من چون ایران نیستم خودم دست به تست نشدم. ولی همونطور که قبلا گفته بودم، کشور وی پی ان، با کارت پرداخت کننده اون حساب، باید بخونه. معمولا خرید مستر کارت مجازی همون کشور، راه امن تری هست. ولی روی کلاد تجربه ندارم که با این کار هم باز میبنده یانه.
چون اغلب آدم ها حوصله ندارن وی پی ان و مسترکارت مجازی رو خودشون بخرن بزنن. میدن یکی پرداخت کنه. همین خودش باعث دردسر میشه.
به شرطی که سایت پرداخت کننده هم، اون کارت مجازی رو قبول کنه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/mohsentavoosiseo/818" target="_blank">📅 18:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-817">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تفاوت کلاد در چت بات(پایین ترین سطح استفاده از کلاد):  متأسفانه لینکی که دادی به خاطر AJAX فیلتر می‌شن و محتوای واقعی سوال‌ها رو نمی‌تونم ببینم سیستم فیلتر کردن با JavaScript کار می‌کنه که من بهش دسترسی ندارم.  اشاره به همون بحث همیشگی SSR در سئو(https://…</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/mohsentavoosiseo/817" target="_blank">📅 14:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تفاوت کلاد در چت بات(پایین ترین سطح استفاده از کلاد):
متأسفانه لینکی که دادی به خاطر AJAX فیلتر می‌شن و محتوای واقعی سوال‌ها رو نمی‌تونم ببینم سیستم فیلتر کردن با JavaScript کار می‌کنه که من بهش دسترسی ندارم.
اشاره به همون بحث همیشگی SSR در سئو(
https://t.me/mohsentavoosiseo/267
) که گفتم فاز لبه تکنولوژی برداشتن بر ضد پول و به ضرر خودمون هست.
هوش مصنوعی های دیگه نمیفهمن به خاطر جاوااسکریپتی لود شدن با Query string نشون نمیده. این عین انسان میفهمه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/mohsentavoosiseo/816" target="_blank">📅 14:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-813">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مباحث امنیتی(امنیت ایالات متحده)</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/mohsentavoosiseo/813" target="_blank">📅 14:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صحبت خارج از موضوع کلاد:
چون خیلی شکایت میشنوم میگم. وگرنه جالب نیست بگم. چون اون ها هم بهرحال از دوستان من هستند. میگم که شاید تغییری ایجاد شه.
از ل............ت برای احترام اول به اعصاب بعد به پولتون توصیه نمیکنم خریدی انجام بدید. آدم های خوبی هستند. اما چون همه چیز دست مدیران فنی هست و ذهنشون همه چیو فنی میبینه و با ذهن تکنیکال غیر تجاری میخوان مشکلات رو حل کنن و تصمیم گیری کنند،
در مدیریت فرایند سفارش ها به مشکلات زیادی میخورن و بعد میان موردی دونه دونه حل میکنن.
افتادند توی لوپ و حلقه بهینه سازی(بازم فنی) که دیگه یک بار برای همیشه درستش کنند. چند ساله. اما گاهی باید ورود کرد دستی کار رو جمع کرد. باید هزینه کرد. بیخیال سود بیشتر شد و به روش غیر فنی، فعلا شرایط رو درست کرد.
بماند که در تشخیص فنی اینکه مشکل کجاست هم اشتباه میکنند. چون فقط از یک زاویه دارن به مشکل نگاه می کنند.
همون چیزی که همیشه میگم مغز صرفا دولوپری و غیر تجاری،
1- یا ایده هاش شکست میخوره،
2- یا نمیتونه بفروشه اصلا و جمع میکنه
3- یا نارضایتی از محصول یا خدماتش ایجاد میشه که نمیتونه حلش کنه(این ها سومی هستند و حداقل تو یک و دو گیر نکردند).
این نکته برای خود اون کسب و کار و کسانی که دریچه دریافتشون بازه، میلیون دلاری ارزش داره. باید میلیارد ها تومن یا صد ها هزار دلار از دست بدن تا این بازخورد رو از زبون یه مشاور که ایراد کسب و کارشون رو میگه بشنون.</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/mohsentavoosiseo/812" target="_blank">📅 14:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⭕️
❗️
🟢
درباره معلق شدن اکانت های کلاد
موجی که راه افتاد ظاهرا همه کسانی که از سایت ا.........ت خریده بودند suspend شدند. اما از گزارش هایی از ساسپند شدن غیر از ا.......ت هم هست.
برای ما نشده. لاگین از ایران هم داریم با وی پی ان. و لاگین های ما از چند کشور هست. ولی هربار کشورش عوض نمیشه.
پرداخت هم از یکی از کشور های ثابت اتحادیه اروپاست با کارت شخصی. با کارت زراعت بانک، ایش بانک و وکیف بانک ترکیه و ورود از ترکیه هم مشکلی نداشته.
مکالمه ما هم فارسی هست اکثرا. ربطی به زبان شما نداره. حساسیت اصلیش روی پرداخت کننده هست و هویت پرداخت کننده.
چون بحث احراز هویت سنی و مباحث امنیتی(امنیت ایالات متحده) توش لحاظ میشه.
اکثر ادم ها هم استفاده های سنگین ندارند. حتی از skill و connector ها که پایه ترین و ابتدایی ترین قابلیت کلاد هست استفاده نمیکنن. فعالیتی که توسعه کد سنگین تو گیت هاب به صورت انلاین و مواردی که میتونه منجر به استفاده عمومی بشه رو بهش حساس تر هست.
اما خودشون میدونن دقیقا رو چی حساسن. تو متن خودش هم نوشته موارد خاص و این خاص رو تعریف نکرده.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/mohsentavoosiseo/811" target="_blank">📅 14:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-810">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کسانی که گزینه "خوشحال" رو زدند که از جایی با قیمت خیلی کمتر به صورت اختصاصی میخرند،
ممنون میشم دایرکت پیام بدید(آیکون یا کلید message همین کانال) و من رو هم از این نون سهیم کنید
😒
. زشته کارتون که مخفی نگهش داشتید
😏</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/mohsentavoosiseo/810" target="_blank">📅 15:58 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
