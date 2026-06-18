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
<img src="https://cdn4.telesco.pe/file/eOO09Z5XXEBwvmaZIwQyvLh86-d7AhM_jhTO9-OTjfGiCP3hcsoAGjKOvrgoshaXH4KtOsj_vcFo1lXbFhm-uf8p4t5Sr1Vc5e1xyBK5aR1s4rko2f80DOypL-JfNxmeedfkTlj-7ylxglB8eJoBlcrWj9gCofLOZjrRwM5hX0INcyT_tvj7FfeqdwOJX1KtpaUSAp4ozDap1z8puyrS8n4TCEcbJ9zzqgTuUNkXigVJxHaMD8MF6TXSSnr9QP8sAmy0qWigwfsF7bgL5RprXAa7DFbUK_k-TKIDG8Lh385Nzrk14WJImDhggbYFOH7xW_kiH1UEPXK5Kvt8pyWwMQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 53.4K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 10:27:23</div>
<hr>

<div class="tg-post" id="msg-2683">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDazai GPT</strong></div>
<div class="tg-text">اکانت‌های هوش مصنوعی رو با یک‌دهم قیمت بخر
🛍
🌐
Kiro.dev
Pro
(جایگزین اقتصادی Claude)
- ایجنت برنامه‌نویسی شرکت آمازون
- پشتیبانی از تمامی مدل‌های Claude
- مناسب فقط برنامه‌نویسان
- مصرف کردیت کمتر نسبت به Claude
- ارزان، اقتصادی و با کیفیت
🏳️‍🌈
Gemini Pro:
- پلن مشابه GPT Plus از شرکت گوگل
- پشتیبانی از Antigravity
- ساخت عکس و ویدیوی فارسی
- تجزیه‌ و تحلیل و تحقیق عمیق
- فعال‌سازی روی ایمیل شما (اتوماتیک)
- کاملا اختصاصی (فمیلی نیست)
🔆
Codex 2500 Credits:
- اکانت کدکس شامل 2500 کردیت
- امکان ارسال 625 الی 3200 پیام
- مخصوص فقط برنامه نویسی
- دسترسی به GPT5.5
- کاملا اختصاصی
خرید و توضیحات بیشتر از ربات:
🤖
@ChatGPT_StoreBOT
رضایت مشتری
💎</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/iaghapour/2683" target="_blank">📅 21:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2682">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">💰
مدیرعامل همراه اول: قیمت فعلی اینترنت با قیمت واقعی آن هیچ سنخیتی ندارد!
مهدی اخوان، مدیرعامل همراه اول، در مجمع عمومی سالانه این اپراتور با گلایه از تعرفه‌های فعلی اعلام کرد که هزینه‌های سرمایه‌گذاری ارزی آن‌ها کاملاً مشابه اپراتورهای منطقه است، اما قیمت هر گیگابایت اینترنت در ایران بسیار پایین‌تر از آن کشورهاست.
پ.ن:
جناب مدیرعامل! اتفاقاً تو این مملکت خیلی چیزها هست که هیچ سنخیتی با هم ندارن؛ از کیفیت اینترنت شما و چیزی که واقعاً به دست ما می‌رسه بگیر تا درآمد بالای مردم منطقه و حقوق‌های پایین ما! از همه مهم‌تر، بین زندگی و رفاه شما و واقعیتِ زندگی مردم هیچ سنخیتی نیست!
اگه واقعاً کار براتون نمی‌صرفه ما هم راضی به ضررتون نیستیم، کلاً درِ این اپراتورها رو تخته کنید و جرم‌انگاری استارلینک رو بردارید تا ببینیم تو یه بازار آزاد اصلاً می‌تونید باهاشون رقابت کنید یا نه! واقعیت اینه که سودهای کلان این اینترنت انحصاری (پرو) حسابی به دهنتون مزه کرده و حالا با گرون کردن‌های نجومی و پشت‌سرهم، به هر دری می‌زنید تا جیب مردم رو خالی‌تر کنید. وگرنه این چیزی که دارید به ما می‌فروشید اصلاً اسمش اینترنت نیست؛ هر وقت یه اینترنت واقعی و بدون فیلتر دست مردم دادید، اون‌وقت پولش رو هم بگیرید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/iaghapour/2682" target="_blank">📅 21:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2681">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭕️
دسترسی مستقیم و بدون واسطه به اینترنت آزاد
🔹
کافی است آدرس subscription را در برنامه v2rayN/v2rayNG وارد کنید: https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json  — نکات استفاده
👇🏻
۱. کانفیگ…</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/iaghapour/2681" target="_blank">📅 21:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2680">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGn3z5VFSJqKrIskA5pJJCft85E0oMnqjsyl18fyUbw8WzDoFQBGdB80_DDpAZ2tyunxwbkK_2Oi9IkCaQt77j4YrthiFqzPzDbDvnD-OTP6wWxiW7t5G6gST5S066-MIWoeJ0Cy_bNH3-vnOXGiiQ-jUU4tkEZ5MVBFfrgfDe2ZyJSpq-UPJIpPFb_XLMj-0dzaEnUAnClD00mDC5Qpj7RsuU-Rra-A26vBPOuQd8ad5SHL6JUCX6fW42-Aznf4uYb6DWLda82uoj6OMNOWO6AQNdPiRc9Xl7-zP-973z5FftmiABcugnftHGhXvX0qtDcraTJ2uN15-C4IQfnYjQ.jpg" alt="photo" loading="lazy"/></div>
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
به هیچ‌وجه انتقال مستقیم ارز بین صرافی‌های ایرانی و صرافی‌های خارجی انجام ندید. حتماً از کیف پول‌های شخصی (مثل تراست ولت، متامسک یا ولت‌های سخت‌افزاری) به عنوان واسطه استفاده کنید تا مشکلی برای سرمایه‌تون پیش نیاد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/2680" target="_blank">📅 16:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2679">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDoprax</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMms02431AdbEdluIfYAEpjHaMYXk9KbJJsWWcd5lQNAxJYNNFYQv8BD2V0jlfuKzBGA1H6QNO1tu9EQfGMsO_E9rTdtEGTmoWZuzBBKnLS1HMEWJ6quzyZ4N4URb2qtBOkaRaUJfRlb13dAuSRv_z72UWyNV0MT3aOwmC9MhO2FfbxdH4Ttj4Z1BDW-ln6wmcRZa1NmA_nTLNMLo7wm7O91YIUHn3569Ij6WEOJZvSGQZR0E6pX7hxQG583F-dEg5Ap7qjIwaMMKyol9ZhvYrJzDjObglX2TWK5gZmAvQVCS8PJ3hBi-HnV6lg0BTqU0moGWVjLmH7GP9CJLM0ygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
سرور ابری رو از هر جای دنیا و با هر ارزی که دوست داری بخر!
🌍
دیگه نیازی نیست برای خرید سرور از دیتاسنترهای معتبر جهانی دغدغه پرداخت یا محدودیت لوکیشن داشته باشی. در دوپراکس (Doprax)، بهترین زیرساخت‌های ابری دنیا در یک پنل اختصاصی زیر دست شماست!
با دوپراکس می‌تونی از غول‌های تکنولوژی مثل Google Cloud, DigitalOcean, Hetzner, Vultr و چندین پروایدر دیگر، سرور تهیه کنی.
✨
چرا دوپراکس بهترین انتخاب شماست؟
📍
تنوع لوکیشن:
دسترسی به ده‌ها لوکیشن مختلف در اروپا، آمریکا، آسیا.
💳
پرداخت بدون مرز:
امکان پرداخت آسان با ریال و یا رمزارز.
⏱️
پرداخت ساعتی
: فقط به اندازه‌ای که مصرف می‌کنی پول بده!
🔄
امکان تعویض IP
: قابلیت تغییر آی‌پی در اکثر دیتاسنترها.
همین حالا وارد سایت شو و اولین سرورت رو با کانفیگ دلخواهت بساز
👇
🌐
وب‌سایت:
www.doprax.com
💬
پشتیبانی و اخبار در کانال ما:
@dopraxcloud</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/iaghapour/2679" target="_blank">📅 02:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2678">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_VCbNAG5vFizg0L0mfsGU4dxcAEwr2JfQJDUII9qrHKKmKHNqSUkD7U5AMPu3EAuvGXg1Z8nUUcA7JYWQxbnqzyet_9UOMRXYWgRVPr0vEIW40gZT1TBuGgspC3_MsWYTK_FshvDvI00QAgDX_HOXFnDpHrGezhjXMtJe9wnzfQ2F8x2QlO5cuUOK7N-mRs0LLAdlj7eIyHgysTxFOVWsPl15vKLKsT_5Jz0Tt9vjTCvNTnD5Df181pJ6JkORf2I-Vr3IK2jRhvv2uYrPDaYkzw3BsagTWpKIm_5woT-jJpDvW2X4MsL_HqTKN9okWf7PmYaVN4_bRhYfobezRmtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/iaghapour/2678" target="_blank">📅 19:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2677">
<div class="tg-post-header">📌 پیام #94</div>
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
⚠️
برای کارهای حساس از این روش استفاده نکنید!
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/iaghapour/2677" target="_blank">📅 12:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2676">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNST_cGYbp6W06BbwCN-jHDqNvdRsyIPUtTFn53NEPCIn45lCS-PB_ZGLH9crNWxMMufDZQt6xNQn0UrnPndDRgD7bO-3kMRYNaOk-9J8SP7L6CLHh1vQ9VLuzZ90NYNNGwyGw0vXznsaN_A6Qg9B_ctPyBYXGwvwBXpc_Ul1OWzprRipIa_iiy9HEqo9IEdeLvulBncblzxNIlZ7MMrEvcumdjeaYHd_wICz543nWzfUxILM1RXTl1dbaaRDevlU9tbYGO42p3wD_Do_fvQzYAk5zSXHtzj-jBvev3vgAei_nnvY8n8cFVvWHoTdXC8rl0RroKDaPCGU1F0Ku4sTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ادعای ایلان ماسک: پهنای باند استارلینک ۱۰۰ برابر می‌شود!
اسپیس ایکس از دستاورد جدیدی خبر داده و اعلام کرده که تعداد مشترکان اینترنت ماهواره‌ای استارلینک از مرز ۱۲ میلیون کاربر در ۱۶۰ کشور عبور کرده است. اما این تازه آغاز راه است و ایلان ماسک برنامه‌های بسیار جاه‌طلبانه‌ای برای آینده دارد.
🔸
انقلاب ماهواره‌های نسل سوم:
ماهواره‌های نسل سوم استارلینک، پهنای باندی ۱۰ برابر نسبت به ماهواره‌های فعلی ارائه خواهند داد. همزمان، سرعت پرتاب این ماهواره‌ها نیز ۱۰ برابر افزایش می‌یابد که در نهایت منجر به
افزایش ۱۰۰ برابری پهنای باند کل منظومه استارلینک
خواهد شد.
🔸
کاهش محسوس تاخیر:
ماهواره‌های نسل جدید قرار است در مداری پایین‌تر (فاصله ۳۵۰ کیلومتری زمین به جای ۵۵۰ کیلومتر) حرکت کنند. این کاهش فاصله، طبق ادعای ماسک، زمان تاخیر را به
نصف
کاهش می‌دهد.
🔹
وضعیت در ایران:
این جهش‌های تکنولوژیک در حالی رخ می‌دهد که در ایران، استفاده و خرید و فروش تجهیزات استارلینک همچنان ممنوع و جرم تلقی می‌شود. با این حال، در پی قطعی‌های اینترنت در یک سال اخیر، ده‌ها هزار ترمینال به صورت قاچاق وارد کشور شده است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/iaghapour/2676" target="_blank">📅 18:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2674">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✍🏻
دوستان، در حال حاضر بیش از ۷ اسکریپت (شامل اسکریپت‌های تانل و روش‌های مستقیم و رایگان) رو در دست بررسی داریم. هر کدوم که بدون مشکل جواب بده رو توی یوتیوب معرفی می‌کنیم. اما مواردی رو که به هر دلیلی (مثل محدودیت‌های دیتاسنتر سرورهایی که استفاده میکنیم و...) نتونیم خودمون ازشون جواب بگیریم، داخل کانال تلگرام معرفی میکنیم تا شما بتونید تست کنید.
ممنون از حمایت همیشگی شما.
💚</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/iaghapour/2674" target="_blank">📅 20:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2673">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">واقعاً باید درِ این بانک‌های مزخرف رو گل بگیرن! سالی ۳ بار یا هک می‌شید، یا اپلیکیشن بانک کار نمی‌کنه، یا اختلال دارید و هزارتا کوفت و زهر مار دیگه! آخه مگه می‌شه بانک این‌همه بی‌در و پیکر باشه؟
😒</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/iaghapour/2673" target="_blank">📅 20:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2671">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS9J39cLJBqiZiKF_-JfcaXnT3yjnUCmAvZjcVJBRW6DSrS8AqBQ2-p3p1lFeOgTXLWB29spudRgp76IfVYkTia9XAvjzvHjyVanw3bokDCq5wTQBLzd0PzKTNQhZT8DOVfE4p6i2e_k8HqCqKxQ1c6S-AlEpsNhgwwNEDVnGOjsXmMpQmyqCt_d3H50gWAvpCuM_rDYJVGM1ZQCYK5qJaPZhay0S0Ar-iRQamIwB79cvZsZMndJnwmdM-7FBTOMPNdOxH7zERAbImYz0ePFUsUBQPwr4Ag5sHxQJs6Dl8EXV0riqzcA0rVDsZsmUE6R_l3hvUNjMFGnsxC2Ml1vLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/iaghapour/2671" target="_blank">📅 21:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2670">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_Dv5aMrFJ4AYX3etlvNE_Yw_-8N1ivFXTyeP33I4Ll4nNNAyX1Lvi59x4vBoKeY01eVtA45XdO4Qe4JRemwPNNgS9RL-iIBdp50qcY9FwULqOqV2yjRd8E0Xa8fsuhgrwBRa3Lnrxs7c01FLqDy3NFfBji3r3tiMRjTaOAcGPZF-BQSY1e617wOwiD5cx451gzTWEYPC8_3stnRKyS2aovTJXU3QgNxUoECw6Jtd-MYdoJm2T4z9kpEO1_dIITgsZWZDbu4RFoOEPBPdXnzvhETahT1rkTbCU5jo8KqtIw060gxuoYefE8uh3KyJwxe6lGTaOxBWSmnyxHUrhwW2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/iaghapour/2670" target="_blank">📅 21:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2668">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf-xZTDDgSMTRWI-iK2H4qeG-7rGSg4S1n5NtxiTA73LXC84vpRG49f_fuQ1XFv3o4lb0-mOUsm9FLDrss514MKM4v4ZVkCGslRTVJMmiIPu9e_hAAjeWZugptygmyC92iLNPFiByV8FNhQB5sGEjzY-7GWonHHRlGyMjfqDfqQyvBgX2TE4OP24n27Cjs_KqZegJSNUaEXDC7QGN36hXKNUJz8UE-p6IcrMhJJ0h70QexVtrJ85K11O0Xe8kFlcwM_jjEGJpjOBEoKjoMrswrtwyxLppdIwhU2nxlhTQ322ZABLeJ_7Ogm_Td2MDBNMO2yeyI8pYMBO7MwuXQ2JkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/iaghapour/2668" target="_blank">📅 19:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2667">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127cc882e.mp4?token=YfGSCUyQVrTYPtIKsGzH6SNDuXZdJyG4a6HhHZ4jBnVIYcn_QMobsBNhP5yet7JhqB_6Lhzv-RkN_-RUJxDb0OXY6IRNfvTzsehvjFT08Y3HdkOGddd2ZOIIbmZKpGo5ByM08VuX-UL3GAKpVXyQx6UgGak8nPMRW9ulBypBXVs5GUutKFLM1Cfgj3mxwf5YPYryY0RcU0dEK6I_P4sC6J_3RB5Nhh4Vil7EjvZmteD8kqqBGFGKR4aiA304-pGVQv50or1l0Xoa8Bb-y8gwi-JasXfelg7s1riS82rWd4sitPDZjm7r8kf-IpA-eMvmYoNjB1CqFfh2-1ZoZuVd9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127cc882e.mp4?token=YfGSCUyQVrTYPtIKsGzH6SNDuXZdJyG4a6HhHZ4jBnVIYcn_QMobsBNhP5yet7JhqB_6Lhzv-RkN_-RUJxDb0OXY6IRNfvTzsehvjFT08Y3HdkOGddd2ZOIIbmZKpGo5ByM08VuX-UL3GAKpVXyQx6UgGak8nPMRW9ulBypBXVs5GUutKFLM1Cfgj3mxwf5YPYryY0RcU0dEK6I_P4sC6J_3RB5Nhh4Vil7EjvZmteD8kqqBGFGKR4aiA304-pGVQv50or1l0Xoa8Bb-y8gwi-JasXfelg7s1riS82rWd4sitPDZjm7r8kf-IpA-eMvmYoNjB1CqFfh2-1ZoZuVd9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/iaghapour/2667" target="_blank">📅 16:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2665">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در حال تست و ضبط چند ویدیو جدید هستیم.
👌🏻
ممنون میشم سوالات رو فقط در یوتیوب بپرسید و در بخش ربات ارسال نکنید.
🙏🏻</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/iaghapour/2665" target="_blank">📅 21:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2664">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qw_fO_o-13w94dMvMJwPJ0W1hHPZXIbFxSOx2xewBy_aL3dd6vgfbTNff8ClaLm-ofVrgOSwWAyqAD5zj6scLIk8tYqHBk48HBbkFQ7aizJXt3iTHgPB_Sxon9JzzAN4pONuty6hil44ddvbKDccJwYz_DaPLxhQTFIHZ4jhkq84RFwjLtnd4nR0-2CxdzcVdiDwiN1SYkBN0BuQvmAITqOtR9yUNFQdrPQ2moWNYuQhgenW6Lih827QBuOGyWltqtuf-C5phtxzU7oT4OCrO7SebJDvyUmSR3uGdyu5OzmpszaJjt6nOMKqzZQ3w0vamn-eR_Veq2g5xx-EXq1Msg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/iaghapour/2664" target="_blank">📅 00:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2663">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه چیزی میگم شاید باورتون نشه.
مردم الان بیشتر از اینکه نگران جنگ باشن نگران قطعی دوباره
#اینترنت
هستن.
کسب و کارهای آسیب دیده تا میان دوباره سرپا بشن اینترنت رو قطع میکنن یا اختلال میندازن و....
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/iaghapour/2663" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2661">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boP-a-Mm-pV62MiDhYTmj8h03CzDqpoH4az3oGZ9rI5K_tnmeMIPuG1o1ce2vOE6y9nJxefyyXMt6fO40PID2ieyc6zAW2O8rce-iEj04SO0i4N2WvFvXnFNDYfL6tSmtq6GXTvz5w1myuEM9JUfEAmpOf_mmdW0OAeDh4FEYwNhc8yo8a2t4CO4M0n0pr00FQY9EgupRBC7Q5JPXaAAsvqhVrpXV08n-kGLIWZfYHmAteDSlRP7BjKiwjAftbPeE80aIAZ_YtVyZTdLN_v_XkwDQmHQ7Mjri1SPH3Gzf6O2JLyvULGKiOQ8xL6T3XY2k0gaRZHUR78HewJTj_M21g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/iaghapour/2661" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2660">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgbQkNouovFh-Io10CPcR1ateTrq2Qtqc0tFDgE0BmLZll05i_md2lBXhIFrWZkVBr-A92AL7wdeEAh31-3uQJAFaBEzboIrACIUAnd7zmnQSZdH25tkKtXx-iaXW0FOxuwxOCmcZeZfWFm_0acHqOoGzdLbVQUAZkOzcTe4flSTQtcMEPvNbXbeti3zc5KIc2l3qBNrbTRJJ55W0Yeuv24ViOtPJWU7ENxdBvmDxPH2y8lyhhcmGXoksPFNaEI9WLNk5c46qqTcE8-ervUhkXFDnY8APJPU6oH0ohqhfxCYBe9qw1PgjVgNycfp0hc5vZPyo_QEJ14TzMqEkr5ZGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/iaghapour/2660" target="_blank">📅 20:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2659">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOkbMebSUpiUMEbQTG9RV40qX43vLZdd8k1LSpcTVm9u_1GoPda3mzCwkFewrs90S8dbMl5QSKphRYkSHP7KW-rJjCy1LLuSaMHs6cfAAeOAZBhygzsy6TzK93sHACRvXOWty-Be7-07LzUm8BniNP8Z290mLOkYLhB5yv1cEhIUhqldu4GAFBWAKOQ5WHHdqzo-lgHyt9XcURNsGUFHybU1jnJZY1WFsUR6aafI9sLCXYE3dqE8pPz8GrUieYMkH2HQKFQUbDsykleqqe3gQC1n2QETTeiVBbImtQM41Ubha8HKN6-hkrSKiDe4weoGD1_ntUcmDUNsmscauo4asw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/iaghapour/2659" target="_blank">📅 01:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBLtpe0jZSAIusEZ6jyjKbQDfUQsiJ0sbdR9Y4XIiMjNIvqUCVhCmSMNbFz5jTk3QWNrQIl3TCl-Dhlq77I2Vaden_9VckGMth85yRw-46zVUN-ftBAefdenDP2LYuvPBeqcLkY9tptbDDff3tHBhPx7wEwr_GfxZnbxGM-87t8kQpf7CYerfFxHg9wAthP0go-WOZ0hQ6Bh0UZiPYWWccTN8Mn4JEtfuLYJ8anl9PRQiCHhx10p0qp_ug0wYqFeO-I46bbzirCo-A97eDDOaKjBTYR7Dd6uwf0Pud1ZJ2vXC98FPfK0msG6TjqBw7rWLpjnH6SJ8u-w0dCjuJUWIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/iaghapour/2657" target="_blank">📅 18:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQCP8IngCt5J-GtNEOx-lvDZpOhJOzGc7UKEmRWop0fwuQdcuDEj-bvVSD0XjGmrGrMkbHsTdr9UEuNbkg24zmoeqSQu5Nk0hqu5p4dAOkK4vp-rJregR4xYvsDxhupLbeTcrvZ523hd56nXnxk0CyqPvHJREPPjo_T7bWlHF5Ch8PECj-7V40_DpZvgto6rKT15_aONdERZX-Vl7UHw_W0yqnD6GwVd6g7ffoTQ3htEl0kVqmmVoDt6lqGt61TusezptNSuidV50TMHjpOyfs9Sv7lntgCSYaqC4wleDnaSgT2oXM_tam5Z2oCmGozFC_afJj7AO8oLtZC45G2P5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/iaghapour/2656" target="_blank">📅 17:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📢
دو نکته خیلی مهم برای شما دوستان عزیز
سلام بچه‌ها! امیدوارم حالتون عالی باشه. برای اینکه بتونم تو کانال بهتر راهنماییتون کنم و محتوای باکیفیت‌تری براتون بسازم، نیاز دیدم این دو تا نکته مهم رو باهاتون در میون بذارم:
۱. درباره سوال پرسیدن از ویدیوهای قدیمی
:
همون‌طور که می‌دونید تعداد ویدیوهای کانال زیاده و واقعیت اینه که من مو به مو یادم نمی‌مونه تو ویدیوهای ماه‌های گذشته یا سال‌های قبل، دقیقاً چه مواردی رو پوشش دادم یا چه جزئیاتی رو گفتم. پس اگر درباره یک ویدیوی قدیمی تو کامنت‌ها سوالی براتون پیش میاد، لطفاً
خیلی دقیق و با جزئیات
بپرسید. اگر ممکنه، مشکلتون رو کامل توضیح بدید یا حتی تایم‌لاین (دقیقه و ثانیه) اون بخش از ویدیو رو بنویسید تا سریع متوجه موضوع بشم و بتونم جواب درستی بهتون بدم.
۲. درباره تست روش‌های تانل
:
نکته دوم در مورد آموزش‌های تانلینگ هست. ببینید بچه‌ها، وقتی ما یک روش تانل رو معرفی می‌کنیم، منطقاً امکانش وجود نداره که اون رو روی
تمام
روش‌ها و پروتکل‌های دیگه (مثل وایرگارد، OpenVPN و...) تست کنیم. خیلی وقت‌ها تو کامنت‌ها می‌پرسید که «آیا این تانل روی فلان پروتکل هم جواب میده؟» راستش ما هم اطلاع دقیقی نداریم؛ چون زمان و زیرساخت تست کردن یک روش روی تک‌تک سناریوها وجود نداره. بهترین کار اینه که خودتون اون روش رو روی پروتکل مدنظرتون تست کنید و اتفاقاً نتیجش رو تو کامنت‌ها بنویسید تا بقیه بچه‌ها هم از تجربه‌تون استفاده کنند.
ممنون که مثل همیشه درک می‌کنید و با انرژی خوبتون همراه کانال هستید!
❤️</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/iaghapour/2655" target="_blank">📅 21:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رفقای عزیز سلام!
✌️
دارم روی یه ویدیوی خیلی کاربردی کار می‌کنم که سعی می‌کنم فردا یا نهایتاً پس‌فردا به دستتون برسونم. تو این ویدیو قراره به خیلی از سوالاتتون جواب بدم، ابهامات رو برطرف کنم و یه گپ و گفتی درباره شرایط فعلی داشته باشیم.
ضمناً خواستم یه تشکر ویژه بکنم بابت تمام حمایت‌هاتون؛ چه کامنت‌های پرانرژی‌تون تو یوتیوب و چه حضورتون تو شبکه‌های دیگه. مرسی که با تماشای ویدیوها (و صبوری کردن برای تبلیغات!) از کانال خودتون حمایت می‌کنید تا بتونیم با قدرت بیشتری به کارمون ادامه بدیم. دمتون گرم!
❤️</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/iaghapour/2652" target="_blank">📅 21:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-text">⭕️
کدهای مخفی چت جی‌پی‌تی؛ ۸ ترفندی که پاسخ‌ها را متحول می‌کند!
بیشتر افراد از چت جی‌پی‌تی فقط مثل یک موتور جستجوی ساده استفاده می‌کنند و پاسخ‌های کلیشه‌ای می‌گیرند. اما کاربران حرفه‌ای می‌دانند که با اضافه کردن چند فرمان کوتاه، می‌توان نحوه تفکر و خروجی این هوش مصنوعی را کاملا تغییر داد.
🔹
ساده‌سازی مفاهیم (ELI5):
اگر موضوع علمی یا پیچیده‌ای را متوجه نمی‌شوید، در درخواست خود بنویسید «توضیح بده مثل اینکه ۵ ساله هستم (ELI5)». چت جی‌پی‌تی تمام اصطلاحات تخصصی را حذف و موضوع را به ساده‌ترین شکل بیان می‌کند.
🔸
استخراج چکیده (TL;DR):
اگر حوصله خواندن یک مقاله یا ایمیل طولانی را ندارید، متن را ارسال کنید و در انتها بنویسید «خلاصه کوتاه (TL;DR)» تا در چند جمله لپ مطلب را بگیرید.
🔹
خروجی جدولی (FORMAT: TABLE):
به جای دریافت پاراگراف‌های نامرتب، مثلا هنگام مقایسه دو محصول، عبارت «نمایش به صورت جدول (FORMAT: TABLE)» را اضافه کنید تا اطلاعات کاملا منظم و خوانا تحویل داده شود.
🔸
کشف نقاط ضعف (DEVIL’S_ADVOCATE):
یک ایده کاری دارید؟ با اضافه کردن عبارت «وکیل مدافع شیطان»، هوش مصنوعی تمام دلایل احتمالی شکست ایده و نقاط ضعف آن را بی‌رحمانه به شما گوشزد می‌کند.
🔹
درخواست اطلاعات ناقص (MISSING_INFORMATION):
به جای اینکه هوش مصنوعی با اطلاعات کم شما یک جواب ناقص بسازد، عبارت «ابتدا اطلاعات ناقص را مشخص کن» را بنویسید. با این کار، چت جی‌پی‌تی ابتدا سوالات ضروری را از شما می‌پرسد تا دقیق‌ترین خروجی را بسازد.
🔸
تحلیل گام‌به‌گام (CHAIN_OF_THOUGHT):
با استفاده از دستور «تفکر زنجیره‌ای»، هوش مصنوعی مجبور می‌شود مراحل استدلال و حل مسئله را قدم‌به‌قدم به شما نشان دهد که خطای منطقی پاسخ‌ها را به شدت کم می‌کند.
🔹
شبیه‌ساز مصاحبه شغلی (MOCK_INTERVIEW):
با نوشتن دستور «مصاحبه شبیه‌سازی‌شده برای موقعیت...»، چت جی‌پی‌تی نقش یک مصاحبه‌گر را می‌گیرد، مرحله‌به‌مرحله از شما سوال می‌پرسد و پاسخ‌هایتان را ارزیابی می‌کند.
🔸
ریست کردن حافظه (IGNORE_PREVIOUS):
وقتی مکالمه طولانی می‌شود و هوش مصنوعی گیج می‌زند، با فرمان «بازنشانی دستورهای قبلی» به او بگویید کل پیام‌های قبلی را نادیده بگیرد و با یک نقش جدید شروع به کار کند.
با استفاده از این دستورات ساده، می‌توانید هوش مصنوعی را از یک ربات پاسخ‌گوی ساده، به یک مشاور، تحلیلگر و همکار حرفه‌ای تبدیل کنید.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/iaghapour/2650" target="_blank">📅 22:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa-btuzvRcHr-vQxbHHI6oA-upTk-9e8UJSazTLnDeUPThfHz23zOgod0sLyFEBy8JmzNZGQIhgwSgFLuGLs8sbYDTIp3ODxKLCjfjXk7siAUTpsbEw3D6VZ1HvRqNixBUBL5-vQEChJhnEh00Q-YrZYuQCLOr498rZlQqjqVdZyGFdkvrbGgrlSX7_ZgVNTuSeuz5CXA7bNMEZEwn9DIyRYtYys_zkmolsg3GBKszsZbgvCb5RSGM6e6h0xFj11MItZUkz97cWieVmA9g1HbA4k1JA77FbnCafwAe_dKmFidB7ZjKfyotsqAg_mpVOGRbES-3fAJFqAw528YZqZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی GenyConnect؛ جایگزین مدرن v2rayN برای مدیریت پروکسی
نرم‌افزار GenyConnect یک کلاینت تونلینگ و VPN مدرن (با کاربردی شبیه به برنامه محبوب v2rayN) است که با تمرکز بر عملکرد بالا، حریم خصوصی و کنترل دقیق ترافیک طراحی شده است. ویژگی مهم این ابزار، وابسته‌نبودن به یک پروتکل خاص است؛ به این معنی که می‌تواند به عنوان یک بستر یکپارچه برای موتورهای مختلف تونلینگ عمل کند.
🔹
مسیریابی پیشرفته:
امکان تعیین مسیر ترافیک بر اساس لیست سفید، دامنه‌های خاص، و حتی مسیریابی در سطح اپلیکیشن‌ها و پروسه‌های سیستم.
🔸
سبک و شفاف:
این ابزار با کمترین مصرف منابع سخت‌افزاری کار می‌کند و اطلاعات کاملی از وضعیت شبکه، لاگ‌های زنده و آمارهای لحظه‌ای ترافیک را به شما نمایش می‌دهد.
🔹
انعطاف در پلتفرم‌ها:
برخلاف برخی کلاینت‌ها که فقط مختص یک سیستم‌عامل هستند، این برنامه به صورت یکپارچه برای
ویندوز، مک، لینوکس و اندروید
در دسترس است.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/iaghapour/2648" target="_blank">📅 21:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0iUYUMFf4p1A7MhDQofrlYObWZmCENAVsmoQZdLe_SRy_flkGeuB77gqw_iy29odJzgtlh3GyqZctxYpueLYlmldekXXQSnWRHY5qx3iQpx02AjhMvRqlOjumNXTW5pK7U2P6sutW2trQGqUD69anyjlbFssZUSgabh-rKUkoaofxIj3IKjjIqIFObdDtEz1L1BMOJxwJx8m7b2AqPw_IWO4P7WiB1E-HXMCXr3wHE1SfgCillCG1KnDAn4wdTOd0IhywFD9Q5jIl0zAhh6yuWwE-RpdcKbAErx6Qs5iXGDY85ohNn-I0d_9fa6ipToiWUMl4RWM-y3NmYoov4kog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تون‌کوین به (Gram) تغییر نام می‌دهد!
پاول دورف در کانال رسمی خود خبر بسیار مهمی برای کاربران و سرمایه‌گذاران شبکه TON اعلام کرد. بر اساس این اطلاعیه، ارز دیجیتال بومی این شبکه قرار است با یک ری‌برندینگ بزرگ، نام فعلی خود را کنار گذاشته و به نام اصلی و اولیه‌اش یعنی Gram تغییر کند.
نکات کلیدی که دورف در این پست به آن‌ها اشاره کرده است:
🔹
بازگشت به ایده اولیه:
دورف یادآوری کرده که Gram نام اصلی ارز شبکه در اولین وایت‌پیپر این پروژه بود. او این اتفاق را بازگشت به ریشه‌ها و شروع یک فصل جدید توصیف کرده است.
🔸
زمان‌بندی انتقال:
فرایند این تغییر نام و انتقال، حدود ۳ هفته زمان خواهد برد.
🔹
نام بلاک‌چین تغییر نمی‌کند:
با وجود تغییر نام ارز بومی (از Toncoin به Gram)، نام خود شبکه بلاک‌چین همچنان TON باقی خواهد ماند.
🔸
قدم چهارم از یک نقشه راه:
این ری‌برندینگ تنها یک تغییر اسم ساده نیست، بلکه به گفته دورف، راه را برای اتفاقات مهم بعدی هموار می‌کند و قدم چهارم از یک برنامه ۷ مرحله‌ای برای «عظمت دوباره بخشیدن به TON» است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/iaghapour/2647" target="_blank">📅 21:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nk9PIIMq4hXtA4tm71dNwX30n1xyPWSYj8h4r0JWX_ktVPe_BMQnjgFIq4PW8Tppi8eRqe9oIxCCc1xupyRDGdHjEmU8IOjNr0JuQJLfEdk8pCkovC2uDbIeBTTW-4F35OBHn3TUkRXmPEFNxXUYJkPzEVzziKLL28T1gubRWfL4XBcC-ymHgKdjsmA558NCJiDSJRZLh-bvO2dOioHsyQqV_S4_81ZOcUyH8IkS_Y000ujCQ880wHthPE4Zm16mn1G9tAED188c3nQ8RnwQNlg1rKpBFcimZoXLOgRpQRJIPpVsHXLJyLbjEQlToJLVfCtjZ12XWi655PDMDhsNsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
اسکنر IP سفید کلودفلر با نوا رادار
🔹
نوا رادار یک
اسکنر IP دسکتاپ
است که با Wails v3 (بک‌اند گو + فرانت ری‌اکت/تایپ‌اسکریپت) ساخته شده. این برنامه رنج‌های IP کلودفلر را از منابع متعدد اسکن می‌کند، تأیید پروتکل واقعی (TCP + TLS handshake) انجام می‌دهد و IPهای سالم را مرتب‌شده بر اساس سرعت تحویل می‌دهد.
—
اسکن چندمنبعی
— ۹ منبع IP قابل انتخاب
—
تأیید دو مرحله‌ای
— اسکن سریع TCP → تست عمیق TLS
— مرتب‌سازی بر اساس سرعت
— قابلیت انتخاب پورت
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/iaghapour/2646" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">IP List -- @iAghapour.zip</div>
  <div class="tg-doc-extra">4.7 KB</div>
</div>
<a href="https://t.me/iaghapour/2644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
آی‌پی ها و فایل html مربوط به ویدیو
ساخت فیلترشکن پرسرعت و رایگان با ورکر کلودفلر
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/iaghapour/2644" target="_blank">📅 20:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tkp0h4T5FDy-og6kepZKztVNZ_v2SNyGnKWGowGgQzrm1I0N-Z6JPz1gaWwZEXHYYb3SCEvqdx0IY8jlnsR7sAaYF7DJgjvS8WsU0fLSy6gN02ocZmZRBoJ3SLwHA6_E8JdUFeug64MbRZqARPOcifyVte_-7VB8P7NmxcH9ddWbwuVDhxzNLN2J-dSWciPnBAXXoTtVZHMXLTM30ayQU5t-6F7-W0O8f5UhoXKakwXv70ntyRCnkEVt3Qf6MOZHFG_G_QP-NTLXtcJAVPB1djdAkUDpBBQLGN7IdcN7CAq-bPFzXB1KmBKLnWSjiUiuLbakvpRrS5GrjrSblDGxIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت فیلترشکن پرسرعت و رایگان با ورکر کلودفلر (تست شده)
🔹
در این ویدیو به صورت قدم‌به‌قدم بهتون آموزش دادم که چطور با استفاده از Cloudflare Workers یک فیلترشکن کاملاً رایگان، و پرسرعت برای خودتون بسازید. این روش کاملاً تست شده و می‌تونید به راحتی روی گوشی و کامپیوتر ازش استفاده کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#رایگان
#پروکسی
#نوا
#novaproxy
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
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/iaghapour/2643" target="_blank">📅 19:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkJ-f1YozutBiyQcK7w2bHQLbubJBLx2My8WoHO3VFMu0A47riuYWj522G_pIMeJPN6sGZe7ypxvPiicGzGmAf6_HyypVhgho5wKKeGY0vddrE6IxrQfvKvqxdpESie6qS5fsV-1hDnEuZ_KJMqlyNS_C2fsbveb4lCWUqsoqckvZmXRKb2xTPVKUsDkkq80fsP-ancOtPLEn1LjOl1qsWz1Bu7P7ZaQ3o5K1b8Ktcb-noOz9SVCJm_P-C2unHrZNM8Tn9QROUF9u-jLsZk6xzX3ZqKhPIEHgmiyQpDjI5i4wIweYFbF_Fqb38XsxPpDG5ogPYukdW71j0ErKsegmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت بزرگ ویندوز ۱۱ منتشر شد؛ پرسرعت‌تر و هوشمندتر!
مایکروسافت به‌تازگی آپدیت جدید ویندوز ۱۱ (نسخه‌های ۲۴H۲ و ۲۵H۲) را با تمرکز بر افزایش سرعت و هوش مصنوعی منتشر کرد.
مهم‌ترین تغییرات این به‌روزرسانی:
🔹
اشتراک‌گذاری صدا:
امکان اتصال هم‌زمان دو هدفون بلوتوثی مجزا به یک سیستم برای تماشای فیلم یا گوش دادن به موسیقی.
🔸
دوربین مشترک:
دسترسی هم‌زمان چند نرم‌افزار به وب‌کم بدون مسدود شدن تصویر.
🔹
افزایش سرعت و جستجو:
ارتقای چشمگیر سرعت منوی استارت و اجرای برنامه‌ها، به همراه امکان پیدا کردن سریع فایل‌ها با جستجوی تنها دو حرف.
🔸
پایش هوش مصنوعی و باتری:
نمایش دقیق میزان مصرف پردازنده عصبی (NPU) در تسک‌منیجر و بهینه‌سازی مصرف انرژی لپ‌تاپ‌ها در حالت استندبای.
این آپدیت با رفع خطاهای ناگهانی و بهبود سیستم امنیتی Windows Hello، تجربه بسیار روان‌تری ارائه می‌دهد و در ژوئن ۲۰۲۶ به‌صورت خودکار برای همه کاربران فعال خواهد شد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/iaghapour/2642" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/iaghapour/2640" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWzDV8_s9_agwM13I7GTeLFy_B_tLhX-_Kvt9hyltkZHBiZ-lqw1pUqu7xn-uYLcaGDBWSaYUMmEAdgsAnaUZmKVdBxCXoH_bUSzs5zsnxI6l6n9EYSnJPDQuCcZUJHkJk4MAcbKRrSg-VmFHF_CPFJvxRG4TtmFGbey3SzuLPLD0nKb6ZrtdZ6zFyo3vTBt3SM6QHwEfn2GhJBbb9JHvfqyXykWYiv_PtfanaR44pS9SckvsQYjJ-Ox66pbsv4uy2TU3XOCgPiTdJYdKiNKxhfFVSN1WiFCA1q1-xjfjGY97BRsLvIAko-vcjLEIDDipUCFJTEJHg2mcK8iSO2rrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم ایران در حال برگشتن به تلگرام
😀</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/iaghapour/2639" target="_blank">📅 20:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">💢
وضعیت اینترنت جوری شده که وقتی نت ملی بود فیلترشکن ها راحت تر متصل میشدن!
راستی گوگل پلی و اپ‌استور در دسترس قرار گرفتن و البته ویندوز آپدیت و...</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/iaghapour/2638" target="_blank">📅 20:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/iaghapour/2637" target="_blank">📅 22:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2636">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
بچه ها میگن انقدر پهنای باند دیتاسنتر ها پایین هستش که اکثر روش های تانل که اجرا میکنن سرعت بدی داره یا دچار قطع و وصلی و اختلال زیاد هستش.
خیلی به روش تانل بستگی نداره بیشتر مشکل پهنای باند ضعیف دیتاسنتر ها مربوط هست.
امیدوارم در روزهای آینده وضعیت بهتر بشه.</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/iaghapour/2636" target="_blank">📅 13:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">میبینم که رو فیلترشکن ها تخفیف زدن :)
هر گیگ رو 10 و 20 هزار تومن دارن میفروشن :)
پولی که بعضی از افراد به جیب زدن تاجر ها نزدن. طرف داخل سرور ایران سایت فروش فیلترشکن داشت! قعطی نداشت. بالای 10 هزار ممبر داشت. اوایل حتی درگاه ریالی داشت. بعد بعضی ها انتظار دارن ما باور کنیم اینا به جایی وصل نبودن!</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/iaghapour/2634" target="_blank">📅 21:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⭕️
چند خبر کوتاه از رسانه ها
🔸
معاون وزیر ارتباطات در پاسخ به زومیت در خصوص زمان بازگشایی اینترنت سیار نیز گفت: «امروز اینترنت همراه نیز وصل خواهد شد.»
با توجه به این اظهارنظر باید منتظر بازگشایی اینترنت همراه تا پایان امروز، سه‌شنبه ۵ خردادماه، در دسترس کاربران قرار بگیرد. هم‌چنین، طبق اعلام‌های قبلی، تا فردا روند بازگشایی اینترنت به وضعیت پیش از دی‌ماه ۱۴۰۴ تکمیل خواهد شد.
🔹
نت‌بلاکس بازگشت بخشی از اینترنت ایران را تایید کرد؛ سطح اتصال به ۳۴ درصد رسید
🔸
چه ‌وب‌سایت‌هایی در دسترس قرار گرفته‌اند؟ /دیجیاتو
ویکی‌پدیا
اپ‌استور
پینترست (Pinterest)
کنوا (Canva)
نوشن (Notion)
تردز (Threads)
کالاف
CallofDuty.com
پابجی (Pubg)
یاهو
دراپ باکس
پلی استیشن
ایکس‌باکس
استیم
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/iaghapour/2633" target="_blank">📅 18:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/iaghapour/2632" target="_blank">📅 18:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اینترنت بین‌الملل وصل بشه یجوری از اینترنت استفاده میکنم اختلال بخوره دوباره قطع بشه.
🫠
گوشی باید آپدیت بشه.
ویندوز باید آپدیت بشه.
لینوکس باید آپدیت بشه.
برنامه ها باید آپدیت بشه.
و...
حس میکنم شما هم با من هم نظر هستید
🫣
😁</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/iaghapour/2631" target="_blank">📅 10:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔻
این روزا انقدر شایعه و خبر بی‌خود درباره وصل شدن اینترنت پیچیده که واقعاً حس و حال خبر زدن در موردش رو ندارم.
با این حال، سعی می‌کنم اسکریپت‌هایی که زحمت کشیدید فرستادید رو حتماً بررسی کنم، به هر حال از دست رو دست گذاشتن که بهتره. راستش با این وضع زندگی، اصلاً هیچ انرژی و انگیزه‌ای برای آدم باقی نمونده.</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/iaghapour/2630" target="_blank">📅 21:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5fqeMfyy4e3xun-o8_dfm_9BGPqhNoOCvKVd7h3Cgz6FV3TKvrq1E5sxtw7RT-4BV9EmmJ01QHanuQochQ-i1LIYDgCSFc7kK68DsRwcGGYtY3HE9htZiDAzlKljGYoZNuu5F1b28PG5ikXlzDFcioE-44Pa1n_DKmqGR8D2vvd3Hwl3lnpLV2HYGL9Xpt8F7NIRpRmJQPk1QqJgW52693nSlnoQJo_67WS4XptTNpNb2_SCK2_CLQ6n-bDklu-hz6VG-UeeDepYEwrrzzbBgWJSMpZnkA39TWxdOr5KSEF-lgEIVU5t47_wkcTxbMBW2XpBH3rlszNljW1APDBgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت جدید کلاینت اندروید GooseRelayVPN
🔹
این مخزن، کلاینت اندروید GooseRelayVPN است که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد.
🛠
پایداری و رفع کرش
‏
🌐
رفع کامل لو رفتن آی‌پی (IPv6 Leak) با موتور جدید tun2socks gVisor FakeDNS.
‏
🎛
پیاده‌سازی کامل Quick Settings Tile.
‏
📊
نمایش کاملاً دقیق سرعت و حجم مصرفی.
‏
🗂
اضافه شدن حالت Bypass به بخش Split-Tunneling.
‏
❄️
رفع فریز شدن برنامه در پس‌زمینه.
‏
📜
اصلاح پرش ناگهانی اسکرول لاگ‌ها و بازطراحی کارت وضعیت اتصال در صفحه Home
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/iaghapour/2628" target="_blank">📅 20:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⭕️
رکورددار تاریکی دیجیتال: ایران طولانی‌ترین قطعی اینترنت جهان را تجربه می‌کند!
روزنامه معتبر اسپانیایی «ال‌پایس» در گزارشی تکان‌دهنده اعلام کرده است که ایران با گذشت حدود ۸۰ روز خاموشی دیجیتال، رکورد طولانی‌ترین قطعی سراسری اینترنت در تاریخ یک جامعه دیجیتال را به نام خود ثبت کرده است. این محدودیت‌ها که ابتدا با توجیه شرایط امنیتی و جنگی آغاز شد، همچنان ادامه دارد.
طبق گزارش این رسانه و به نقل از نت‌بلاکس، این وضعیت حالا حتی از قطعی طولانی‌مدت اینترنت میانمار در سال ۲۰۲۱ نیز فراتر رفته و زندگی میلیون‌ها ایرانی را در بن‌بست قرار داده است:
🔹
آوارگی برای یک اتصال پایدار:
ال‌پایس داستان تلخ افرادی را روایت می‌کند که برای حفظ شغل خود مجبور به مهاجرت موقت شده‌اند. مانند معلم زبانی که برای رهایی از اضطراب قطعی اینترنت، با هزینه ۴۰۰ دلار در ماه به زیرزمینی تاریک در ارمنستان پناه برده است.
🔸
ضربه مهلک به کسب‌وکارهای زنان:
تداوم این اختلالات، آسیب‌های ویرانگری به مشاغل کوچک وارد کرده است؛ به‌ویژه کسب‌وکارهایی که توسط زنان اداره می‌شوند و حیات آن‌ها کاملاً به پلتفرم‌های آنلاین و شبکه‌های اجتماعی گره خورده بود.
🔹
فلج شدن زندگی روزمره:
از کار از راه دور و تبادلات مالی گرفته تا ساده‌ترین ارتباطات انسانی و دسترسی به اطلاعات، همگی تحت تأثیر این محدودیت‌های بی‌سابقه مختل شده‌اند.
گزارش این روزنامه نشان می‌دهد که جهان در حال تماشای انزوای دیجیتال جامعه‌ای است که شهروندانش برای دسترسی به ابتدایی‌ترین حق ارتباطی خود، ناچارند هزینه‌های سنگین روانی، مالی و حتی مهاجرتی بپردازند./ دیجیاتو
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/iaghapour/2627" target="_blank">📅 16:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8E6Fk5A_RVMPT9dz14U_A6yIIONNxSoMuVOUA2wV7oAMrnUsqI2px1XG5ef1jX4V7bfM_lqdQPah6G65OxSFh7vBxL7Tt0-2oh3KIzh8vBEtqKmmpZdvJ2A8VonMZMR92SW5xzoy_ojeDtsWhoaiv2_lSzLbN_cs3IbthMMhKz6h9rWMQ3Ap5viP6GJTe0TY6AfXPGwud0gXeC6Z3JKt7XCFCEQxdmYWN-10WxZWZ2V_c6WLd3mx46VR1onjrIKFK0NpXd5JylUg_o1Ndgpyo6LCe1P26-mAvYxnyZg2SkGcT4ISrvKBqKrvG9mFQoKcNuO6sa3Dmot5NboAKMi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پروژه XPlex؛ راه‌حل هوشمندانه برای جلوگیری از قطعی و پکت‌لاس کانفیگ
اگر از کانفیگ‌های v2ray استفاده می‌کنید و پایداری اینترنت در کارهای حساسی مثل آزمون‌های آنلاین، جلسات ویدیویی یا ریموت‌ورک برای شما حیاتی است، پروژه جدید XPlex یک راه‌حل فنی و کاربردی برای شما دارد.
منطق این اسکریپت ساده اما بسیار کارآمد است و به شما کمک می‌کند تا یک اتصال بدون قطعی را تجربه کنید:
🔹
استفاده هم‌زمان از چند کانفیگ:
منطق کلیدی این پروژه این است که اگر چند کانفیگ v2ray داشته باشید، اسکریپت به صورت هم‌زمان از آن‌ها استفاده می‌کند و ترافیک شما را روی کانفیگی می‌اندازد که کمترین پینگ ممکن را دارد.
🔸
خداحافظی با پکت‌لاس و تایم‌اوت:
این ابزار برای افرادی که کارهای حساسی دارند و ثانیه‌ها برایشان مهم است طراحی شده؛ مثل شرکت‌کنندگان در آزمون‌های آیلتس آنلاین، جلسات کاری با خارج از کشور و...
🔹
هزینه مصرف حجم:
باید توجه داشته باشید که به دلیل ماهیت کارکرد این ابزار، مصرف ترافیک و حجم v2ray شما تقریباً دو برابر خواهد شد که بهای به دست آوردن یک اینترنت کاملاً پایدار است.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/iaghapour/2625" target="_blank">📅 20:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⭕️
نماینده مجلس: ۹۰ درصد مردم با قطعی اینترنت مشکلی ندارند!
علی یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس صراحتاً اعلام کرد که اینترنت جهانی فعلاً بازگشایی نخواهد شد و مسئولان به این نتیجه رسیده‌اند که اتصال مجدد آن به صلاح نیست. او مدعی شده که با پلتفرم‌های داخلی، احتیاجات اکثریت جامعه برآورده شده است!
این اظهارات نشان‌دهنده اصرار بر ادامه سیاست اینترنت طبقاتی و نادیده گرفتن نارضایتی‌های عمومی است:
🔹
انکار نارضایتی‌ها:
این نماینده مدعی است به عنوان نماینده مردم، مراجعات مکرری برای اعتراض به قطع اینترنت نداشته و ۹۰ درصد مردم هیچ مشکل عمده‌ای با این وضعیت ندارند!
🔸
رسمیت یافتن اینترنت پرو:
به گفته او، تا کنون به بالغ بر یک میلیون نفر از افرادِ واجد صلاحیت (مثل تجار و دانشگاهیان) دسترسی به «اینترنت پرو» داده شده و هر قشری که نیاز داشته باشد هم می‌تواند آن را پیگیری کند.
🔹
کوچ اجباری به پلتفرم‌های داخلی:
او مدعی شد که ترافیک شبکه‌ها نشان می‌دهد بیشتر کسب‌وکارها به پلتفرم‌هایی مثل روبیکا و سروش کوچ کرده‌اند و تنها یک «اقلیت ناچیز» باقی مانده‌اند که آن‌ها هم بستر مشخصی برای پیگیری دارند.
در حالی که مسئولان از پایداری وضعیت فعلی و رضایت مردم سخن می‌گویند، بخش بزرگی از جامعه، کسب‌وکارها و متخصصان، اینترنت طبقاتی و محدودیت‌های فراگیر را تلاشی برای حذف کامل دسترسی آزاد به دنیای دیجیتال می‌دانند. / زومیت
پ.ن: اینا نماینده کدوم مردم هستن؟ 90 درصد مشکل ندارن؟ عجب!
حالا فارق از اینکه این ادعا از اول تا آخر دروغ هستش ولی من قبلا هم خواهش کردم اگه مجبور نیستید وارد شبکه های داخلی نشید! اگه مجبور نیستید لطفا سیم‌کارت پرو نخرید! اینا واقعا فکر میکنن مردم به ایتا و بله علاقه دارن! متوجه نیستن خیلی ها به اجبار مهاجرت کردن! در غیر اینصورت کی این اپلیکیشن ها رو به تلگرام و اینستا ترجیح میده؟
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/iaghapour/2623" target="_blank">📅 19:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
دوستان عزیزی که درخواست معرفی افراد معتبر برای خرید فیلترشکن دارید؛ طبق بررسی و نظرسنجی که در
این پست
قرار دادیم، با چندین نفری که از سال‌های قبل همکاری داشتیم صحبت کردیم و ازشون یکسری درخواست‌ها داشتیم؛ از جمله ضمانت بازگشت پول و اینکه مبلغی رو به عنوان ضمانت پیش ما بگذارند.
به همین دلیل ۹۰ درصدشون قبول نکردن و فقط تعداد محدودی پذیرفتن که هفته پیش یکی از اون‌ها رو بهتون معرفی کردیم. بازم اگه کسی از افراد قدیمی شرایط ما رو قبول کنه حتماً معرفی می‌کنیم.
افرادی که به ما تبلیغ می‌دن می‌دونن چقدر تو تبلیغات سخت‌گیر هستیم حالا در هر موضوعی باشه. بیش از ۳۰ درصد کسانی که پیام می‌دن، چون کانال قدیمی یا کاربر زیادی ندارن یا سایت معتبری ندارن، با نهایت احترام تبلیغشون رو اصلاً قبول نمی‌کنیم.
🔹
با این حال بازم سعی می‌کنیم همین یکی دو تا فردی که می‌شناسیم و شرایطمون رو قبول کردن بهتون معرفی کنیم؛ البته اگه خودشون دوباره قبول کنن تبلیغ بدن :)
ممنون میشم افراد جدید برای تبلیغات در زمینه فیلترشکن فعلاً پیام ندن. شرایط رو کامل در
این پست
براشون توضیح دادیم.</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/iaghapour/2622" target="_blank">📅 21:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⭕️
اعتراف رسمی دولت: ۷۰ درصد مطالبات مردم، رفع محدودیت‌های اینترنت است
معاون اجرایی رئیس‌جمهور صراحتاً اعلام کرد که طبق نظرسنجی‌های نهاد ریاست‌جمهوری، بیش از ۷۰ درصد گلایه‌ها و خواسته‌های مردم به محدودیت‌های اینترنت مربوط می‌شود. او تأکید کرد که سیاست پایدار کشور نباید بر مبنای فیلترینگ باشد.
نکات کلیدی سخنان معاون رئیس‌جمهور درباره وضعیت اینترنت:
🔹
تصمیمات اضطراری باید تمام شوند:
محدودیت‌های اخیر به دلیل شرایط خاص امنیتی و جنگی بوده، اما تصمیمات دوران اضطرار نباید دائمی شوند و سیاست پایدار کشور نمی‌تواند بر محدودسازی بنا شود.
🔸
اعتراف به شکست فیلترینگ:
تجربه عملی نشان داد محدودیت‌های فراگیر ارتباطی به نتایج مورد انتظار منجر نشده و استفاده گسترده از فیلترشکن‌ها اثربخشی این محدودیت‌ها را از بین برده است.
🔹
حق آگاهی مردم:
اعتماد عمومی مهم‌ترین سرمایه است و مردم حق دارند بدانند محدودیت‌ها بر چه مبنایی اعمال می‌شود، چه دامنه‌ای دارد و تا چه زمانی ادامه خواهد داشت.
به گفته قائم‌پناه، کشور به یک تفاهم ملی در حوزه ارتباطات نیاز دارد؛ چرا که آینده ایران متصل و فناورانه است و دسترسی پایدار به اینترنت، پیش‌شرط تحقق این آینده خواهد بود./ زومیت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/iaghapour/2621" target="_blank">📅 17:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efWiXyG-vQ9k8nYE9D6Ek5nmc5mi-9wemegzc8GA3vNdGIB5Xbh1QS91j4cKR25jtt9lQq0XaxvLlxK_ixbEQiNI39rIoF9UbZBj3DFlt7v07j-3mdaHwcs9u5Hry2nmKiHDplLQXzWVHccslnUkPMTqQzmw1DsMYHaNu9_kAQe35VeHmd8CmhitHVw3kB0vPK-V5UDdSIHCPdB_LTiIc2z6STuzKM1YaKxy3DawPQxQssmA2v9HXheYYIEzoXvf7kfBLKxCyxtO9jCmG494kK1q1i4uso2G2wUqcwpCzQozrPMv6N28ZqeWIjGApSuKCvt4aTmu-TzC4_9LS62PoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
بحران خاموشی دیجیتال؛ ضربه‌ای جبران‌ناپذیر بر پیکر اقتصاد و جامعه
🔻
بیش از ۱۹۴۴ ساعت خاموشی دیجیتال، تنها قطع یک ابزار ارتباطی روزمره نیست، بلکه یک «بحران تمام‌عیار اقتصادی و اجتماعی» است. در زمانه‌ای که در سراسر جهان حتی چند دقیقه اختلال در اینترنت زیان‌های هنگفتی به بار می‌آورد، تداوم ۸۲ روزه این وضعیت در ایران، آسیبی عمیق به شریان‌های حیاتی کسب‌وکارها و زندگی عادی مردم وارد کرده است.
در واقع، تداوم این قطعی طولانی‌مدت نشان می‌دهد که حفظ حیات اقتصادی مشاغلِ وابسته به فضای مجازی و نیازهای ارتباطی جامعه، در اولویت تصمیم‌گیری‌ها قرار ندارد؛ رویکردی که پیامدی جز نابودی معیشت هزاران نفر، فرسایش سرمایه اجتماعی و آسیب جدی به بدنه نوپای اقتصاد دیجیتال کشور نخواهد داشت.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/iaghapour/2620" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USG2ktTTUXhBwf2dIVtlCGEp0V_GxoXnClCPxa5tApw0k4hYfeCOsDvW5-aqZNrDs0vFJJA7yW82TP2RbiOxKq9315Z66JQh-4dx8jJN5fWfqxadtQ51F9fYJtAfpF-DSiiagGc5e4SnFPyoUp_Wl-pvXOWovcHqDrSJVA7h9oKj75rvMeIkevNWdMzlbdYOokJkqSoQ8pohW4RsHxkTGinLKyd0hSZIDAWOfWlXHtvt9X54MZa_-Jo9QX5st2_CbTSrMaH484zAhacLDymYy1VXYIJHKv5PgML2mUIEeJYh32Eg6SBXICwX46la10BYBTFSm9a0URNsaVL4c3ewAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
شگفتی گوگل در Google I/O 2026؛ معرفی جمینای ۳.۵ فلش با سرعتی باورنکردنی!
در گام نخست، مدل جمینای ۳.۵ فلش عرضه شده است؛ مدلی که با وجود طراحی شدن برای سرعت بالا و هزینه کم، در کمال شگفتی توانسته مدل‌های پرچمدار و پرو نسل‌های قبل را در بنچمارک‌های تخصصی شکست دهد.
🔹
پادشاهی در بخش ایجنت‌ها:
این مدل با توانایی برنامه‌ریزی بالا، می‌تواند چندین ایجنت را به صورت موازی برای پیشبرد پروژه‌های پیچیده و کدنویسی مستقر کند.
🔸
سرعت خیره‌کننده و کاهش هزینه‌ها:
ساندار پیچای اعلام کرد این مدل با سرعت پردازش ۲۸۹ توکن در ثانیه، حدود ۴ برابر سریع‌تر از رقباست.
🔹
شکست رقبای سرسخت:
جمینای ۳.۵ فلش در آزمون‌های تخصصیِ مربوط به کارهای ایجنتی، امتیاز بی‌نظیر ۱۶۵۶ را کسب کرده و عملاً رقیب سرسختی مثل کلود سونیت ۴.۶ آنتروپیک را پشت سر گذاشته است.
🔸
همچنین نسخه قدرتمندتر یعنی جمینای ۳.۵ پرو در ماه ژوئن ۲۰۲۶ رسماً عرضه خواهد شد.
جمینای ۳.۵ فلش هم‌اکنون به عنوان مدل پیش‌فرض در اپلیکیشن جمینای و بخش سرچ گوگل فعال شده است.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/iaghapour/2619" target="_blank">📅 09:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmrouT8f96TuqYn5WsLk4IRqHzVDFQVjBTtha5KZM0PvjNDPw8IUA4y7MUG-I6y6mDVQnj3WfaXqL3R2TKREh2UnnMsaihjzIbE_qLxHPLMZllRsZGEoMEfX2tMxkEdC5wmGKY5_a6IvP-XLZK4eX_SRjyfsnLnIyWeItFsZKk1L3O3d0-dWRTIe2DUf_bqmOVPF9QV6507oyqWkXVW1pKE62UtTkxzDsGs8iQcafbD6YXKKjmNxpSfcK3BUcv_WtVL-ndFSfRHENqv-mRavohqX4DZ6EVIiox1cMRuxPQ39SuEfIKm4KSt5qJeSL8A48vB0YDrV0LUVM4lrZ5h5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دیگه پول فیلترشکن نده! آموزش ساخت فیلترشکن شخصی و رایگان با سرعت بالا
😎
🔹
در این آموزش قدم‌به‌قدم بهت یاد می‌دم که چطور بدون نیاز به دانش خاصی، یک فیلترشکن (VPN) شخصی، امن و کاملاً رایگان برای خودت بسازی. این روش روی تمام اینترنت‌ها جواب می‌ده و سرعت خوبی برای تماشای یوتیوب، وب‌گردی و … داره.
🔗
تماشا ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
#آموزش
#فیلترشکن
#رایگان
#novaproxy
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
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/iaghapour/2618" target="_blank">📅 16:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">از هر 10 نفری که که تو اینستاگرام وصل هستن 8 تاش دختره, 2 تاش هم پسر کانفیگ فروش
🥸</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/iaghapour/2617" target="_blank">📅 17:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ43695hESAHZMDqndhm8Q8d4OlK1q8NKzRV095kl52jI96B0FkJ79cg32hVizNzw_7Q8VLaYnVIV9TfY0vpfn90jtplIUtIwYlCy7Eg9WKoSTO9nBqIEoFauGYAx1K7DJ6KfDP29s-1KGy1ebp5qxATTpsMgkCDbSfnKWf9KkNMIy-v2FDTF2b9faVdNM6NXahW8vjAIivce0kfdhcg-oFWg5lnGbffevwn5EsTvcVyJ_YmfLtewUmM2wRLBe2a1apqjMyXitqicGbWMxmTvVNVCg8wBrnIf1u0xxBmB7EJnX5T8v9YekuSHsOYthXJNW1dwMMgothYBd2riswWsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش نصب ساده و آفلاین 3X-UI روی سرور ایران + SSL (+ معرفی قابلیت های جدید)
🔹
در این ویدیو به سراغ یکی از بزرگترین چالش‌های این روزها رفتیم: نصب پنل 3X-UI روی سرورهای ایران همراه با سرتیفیکیت به صورت کاملاً آفلاین و بدون نیاز به اینترنت آزاد! همینطور سعی کردیم یک معرفی ساده از قابلیت های جدید این پنل داشته باشیم.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
#آموزش
#فیلترشکن
#پنل
#xui
#3xui
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
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/iaghapour/2615" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⭕️
بحران در زیرساخت فناوری؛ سقوط درآمدها و خطر عقب‌ماندگی ۱۰ ساله!
اختلالات اینترنتی دیگر فقط یک مشکل ساده برای کاربران عادی نیست؛ بلکه به گفته رئیس کمیسیون شبکه سازمان نصر، تیشه به ریشه‌ی زیرساخت‌های فناوری کشور زده است. این وضعیت نه تنها درآمد شرکت‌ها را تا ۷۰ درصد کاهش داده، بلکه باعث فرار متخصصان کلیدی و فرسودگی شدید تجهیزات شده است.
🔹
سقوط درآمد و انفجار هزینه‌ها: شرکت‌های حوزه شبکه با کاهش درآمد ۳۰ تا ۷۰ درصدی روبرو هستند. از سوی دیگر، به دلیل اختلال در مسیریابی و افت کیفیت، این شرکت‌ها مجبور به پرداخت جریمه‌های سنگین ناشی از نقض توافق‌نامه سطح خدمات (SLA) شده‌اند.
🔸
تهدید امنیت سایبری: محدودیت دسترسی به مخازن اصلی و سرورهای به‌روزرسانی جهانی، ریسک نفوذ و حملات سایبری را تا ۴۰ درصد افزایش داده است. در واقع، امنیت سایبری قربانی ناپایداری شبکه شده است.
🔹
تخلیه ژنتیکی تخصص: صنعت شبکه با بحران خروج نیروهای کلیدی مواجه است. تربیت یک متخصص ارشد سال‌ها زمان و هزینه‌ی ارزی سنگین می‌طلبد که با مهاجرت این افراد، سرمایه‌های انسانی چند میلیاردی کشور به راحتی از دست می‌رود.
🔸
عقب‌ماندگی ۱۰ ساله: ادامه این وضعیت، ایران را با شکاف تکنولوژیک ۱۰ ساله نسبت به کشورهای منطقه مواجه می‌کند؛ شکافی که در فضای پرشتاب فناوری، جبران آن تقریباً غیرممکن خواهد بود.
زیرساخت شبکه کشور به جای اتصال طبیعی به اینترنت جهانی، در حال حرکت به سمت یک ساختار جزیره‌ای و فرسوده است. اگر ثبات پیش‌بینی‌پذیر به این فضا بازنگردد، شرکت‌های بزرگ فناوری به اپراتورهای ساده تجهیزات قدیمی تنزل پیدا خواهند کرد. / دیجیاتو
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/iaghapour/2614" target="_blank">📅 10:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc3N4taye9OE0ob4WmmF3IDFynhxiLskg9K7eLN-bVTkU1UeJONtYfg7ppgf-a3ggpMyWGAXa-2gY9UUIrsx-H8CT_JTlP0T3htHbkIqlDinetbX2vn8JnzwYsNIt6l69gIlTz4UIIm-TsCARBcljZsO3ROiYegx8ODRHBoFdxYQgZtqmjHMXn_Do3Fbi3j9BZ4f50fh8jrhcqP2NEVpluip479d7M12sYv7g2dJgUkQsNnpA8vANY_zAYYHf-aVKi5oM5DrM6_fu06HPIJWnpci9DhM9auXfOqqRworxuPnAubGBOXnpG54XlWhEPJhMkYSYg0oEpHTDM93K4dJdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
حرف‌زدن درباره‌ی قطعی
#اینترنت
شاید فوری اینترنت را برنگرداند؛ اما
#سکوت
دقیقاً همان چیزی است که ادامه‌ی این وضعیت به آن نیاز دارد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/iaghapour/2613" target="_blank">📅 22:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کل ریپازیتوری گیت هاب علیرضا که شامل X-UI و S-UI میشد بسته شده و هنوز دلیلش مشخص نیست.</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/iaghapour/2612" target="_blank">📅 17:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کل ریپازیتوری گیت هاب علیرضا که شامل X-UI و S-UI میشد بسته شده و هنوز دلیلش مشخص نیست.</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/iaghapour/2609" target="_blank">📅 19:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔻
سوپراپلیکیشن ایتا اعلام کرد امکان ارسال فایل تا حجم ۲۰ مگابایت مجدداً برای همه کاربران فراهم شده است!
کاش تلگرام بیاد از شما یاد بگیره :)
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/iaghapour/2608" target="_blank">📅 12:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✍🏻
دوستان عزیز، همون‌طور که احتمالاً متوجه شدید، در یک هفته گذشته به دلایل مختلفی فعالیت ما کمتر شده.
🔹
در این مدت پیام‌های زیادی داشتیم که درخواست آموزش «روش جدید سنایی» رو داشتن. وقتی بررسی کردیم، متوجه شدیم خود ایشون زحمت تهیه ویدیوی آموزشی رو کشیدن؛ بنابراین نیازی به آموزش مجدد  نبود.
🔸
برای اطمینان بیشتر، این آموزش رو به چند نفر از دوستان دادیم تا تست کنن. بیشتر افراد موفق به اجرا نشدن، اما یکی از کاربران تونست متصل بشه. طبق بررسی‌های ایشون، این روش به‌شدت به رنج آی‌پی‌ها (هم سرور ایران و هم خارج) وابسته است. مشکل اصلی اینجاست که بعد از اتصال و مصرف حجم کمی از اینترنت، ارتباط قطع می‌شه و باید آی‌پی رو عوض کرد؛ هرچند آی‌پی قبلی بعد از ۱ تا ۲ ساعت دوباره قابل استفاده می‌شه.
🔻
متأسفانه در این بین، عده‌ای بدون این‌که تست درستی از پایداری تانل بگیرن، شروع به آموزش کردن که نتیجه‌اش فقط ضرر مالی برای کاربران بوده. چون کاربرا رفتن سرورهای گرون قیمت رو خریداری کردن که البته تعداد این افراد اصلا کم نبوده. (نمونه‌اش رو در عکس ضمیمه می‌بینید).
🟢
در مجموع، به نظر می‌رسه این روش هنوز پایدار نیست، اما از بچه‌های تیم خواستیم تست‌های بیشتری روش انجام بدن. اگر خودتون هم مایلید آموزش رو ببینید، می‌تونید مستقیماً به کانال یا گروه سنایی مراجعه کنید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/iaghapour/2607" target="_blank">📅 22:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⭕️
خلاصه اخبار چند روز گذشته
🔸
اینترنت بین‌الملل به گیمرها ارائه می‌شود؛
ثبت درخواست در سامانه همگرا (اینترنت طبقاتی)
🔹
دولت و مجلس به دنبال حمایت تازه از پیام‌رسان‌های داخلی (رانت و فساد جدید)
🔸
نماینده مردم تهران در مجلس:
درباره خسارت‌های قطعی اینترنت جوسازی می‌شود. (حرف بیخود)
🔹
معاون رئیس‌جمهور:
اینترنت بین‌الملل حتما وصل می‌شود؛ دولت قصد دائمی‌کردن محدودیت‌ها را ندارد. (حرف الکی)
🔸
برآورد انجمن بلاکچین: خسارت ۳۰۰ تا ۷۰۰ هزار میلیاردی از قطعی اینترنت.
🔹
معاون رئیس جمهور: محدودیت حجم و گرانی اینترنت پرو برای جلوگیری از استفاده غیرضروری است. (عجب بابا عجب)
🔸
قطع اینترنت به هفتاد و پنجمین روز خود رسید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/iaghapour/2606" target="_blank">📅 18:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prAxELsvtcWRtL2evNcJ2hBet_s1nG8t7rnm9bGs9iw4mHKawyYk_uArdC1_fXIu6f8PFET3GsYJsETSvkXujk3JxIUUkcg_RjynGsS096idQFBtS88Os9KqaB2s14TKnNKr-218VfZErR2dKOVjEWWvxtNkLnD2d4tE1ezsIxPVwp7orxiCkjk-QX3Xhi3JoIL80aihr8GzHwtaVP_RsAY4arIux3LpvpHivjPWdG8NKvTCvMCQhjzS1kPYR7MvgXHUjfXn85HTyWLLqGpVZrvxfHE-RwFKF4aCzswwO0zRxx_IB-_0JQzxh9CMljpfG__9WEaIWJhRd8q71DzU2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
با اپ TunnelX در ویندوز از قابلیت Split Tunneling استفاده کنید.
🔹
اپ TunnelX برای زمانی ساخته شده که کاربر نمی‌خواهد تمام ترافیک سیستم از وی‌پی‌ان عبور کند. با این برنامه می‌توان فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگر را وارد تونل کرد و بقیه ترافیک سیستم را روی اینترنت عادی نگه داشت. همچنین در صورت نیاز، حالت Full-route برای عبور کل سیستم از تونل در دسترس است.
🔗
دانلود اپ از گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/iaghapour/2605" target="_blank">📅 14:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✍
آدم راننده شوتی باشه به مراتب اضطرابش كمتر از کسیه كه شغلش تو ايران به اينترنت وابسته هستش...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/iaghapour/2603" target="_blank">📅 21:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2602">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚀
آپدیت بزرگ و انقلابی پنل 3x-ui (نسخه‌های 3.0.0 و 3.0.1)
بالاخره یکی از مهم‌ترین آپدیت‌های پنل محبوب 3x-ui منتشر شد! در این نسخه‌ها شاهد بازنویسی کامل رابط کاربری، اضافه شدن قابلیت‌های مدیریتی کلان و بهبودهای چشمگیر امنیتی هستیم.
🌐
۱. بازنویسی کامل و سریع‌تر شدن پنل (مهاجرت به Vue 3)
رابط کاربری از پایه بازنویسی شده است! این یعنی سرعت لود بسیار بالاتر، طراحی مدرن‌تر، صفحه لاگین جدید و بهبود چشمگیر تم دارک.
⚡️
۲. آمار زنده و در لحظه
: با جایگزینی سیستم قدیمی با
WebSocket
، از این پس تمام آمارهای داشبورد، مصرف حجم کلاینت‌ها و وضعیت سرور به صورت «زنده» آپدیت می‌شوند و دیگر نیازی به رفرش کردن صفحه نیست!
🌍
۳. مدیریت چند سروره (Multi-Node Deployment) -
🌟
ویژگی طلایی
یکی از مورد انتظارترین قابلیت‌ها اضافه شد! حالا می‌توانید از طریق یک پنل مرکزی (Manager)، کانفیگ‌ها و اینباندها را روی چندین سرور دیگر (Remote Nodes) مستقر و مدیریت کنید.
📱
۴. رابط کاربری کاملاً سازگار با موبایل
: داشبورد، لیست کلاینت‌ها و بخش لاگ‌ها حالا به صورت "کارتی" و کاملاً بهینه برای نمایشگرهای موبایل طراحی شده‌اند تا مدیریت پنل با گوشی بسیار راحت‌تر شود.
⚙️
۵. خداحافظی با کدهای JSON و تنظیمات آسان‌تر
فرم‌های ساخت کانفیگ (Inbounds) کاملاً ساختاریافته و گرافیکی شده‌اند. دیگر برای تنظیمات پایه نیازی به دستکاری JSON خام نیست (البته تب Advanced برای حرفه‌ای‌ها همچنان وجود دارد). همچنین مدیریت DNSها بسیار پیشرفته‌تر شده است.
👥
۶. مدیریت گروهی کلاینت‌ها (Bulk Actions)
امکان انتخاب گروهی  کلاینت‌ها برای حذف یا اعمال تغییرات اضافه شده که کار ادمین‌ها را بسیار راحت می‌کند.
🛠
۷. امکانات جدید Xray و Outboundها
اضافه شدن پروتکل Loopback، دکمه
Test All
برای تست همزمان همه Outboundها و ارائه گزارش دقیق از تایم‌اوت‌ها، و همچنین خاموش شدن امن هسته Xray.
🔒
۸. ارتقاء امنیت و نصب راحت‌تر
➖
اضافه شدن سیستم امنیتی CSRF Protection برای جلوگیری از حملات.
➖
اضافه شدن گزینه
skip-SSL
در اسکریپت نصب (بسیار کاربردی برای کسانی که از ریورس‌پروکسی یا تانل استفاده می‌کنند و نیازی به سرتیفیکیت روی خود سرور ندارند).
➖
اضافه شدن صفحه مستندات API (API Docs) در داخل خود پنل برای برنامه‌نویسان.
و بسیاری از تغییرات دیگه که میتونید در
این لینک
مطالعه کنید.
💡
نکته:
برای تجربه این تغییرات فوق‌العاده، پیشنهاد می‌شود هرچه سریع‌تر پنل خود را آپدیت کنید. (توصیه همیشگی: قبل از آپدیت بکاپ فراموش نشود!)
✍🏻
با تشکر از ثنایی عزیز.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/iaghapour/2602" target="_blank">📅 18:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⭕️
عصبانیت سخنگوی دولت از انتقاد خبرنگاران از قطع اینترنت
فاطمه مهاجرانی در نشست خبری امروز خود به اعتراض خبرنگاران بابت ادامه قطعی اینترنت واکنش نشان داد.
سخنگوی دولت گفت: «در شرایطی که رئیس جمهور آمریکا اعلام می‌کند آتش بس به دستگاه تنفس مصنوعی وصل است، پاسخ شما چیست؟ کشور در جنگ است. بپذیریم که ویژگی جنگ، امنیت مردم است.»
✍🏻
پ.ن:  خانم مهاجرانی اگه دوباره عصبی نمیشید خواستم بگم کاش به فکر امنیت اقتصادی مردم هم بودید! کاش به فکر امنیت ذهنی و روانی مردم هم بودید! کاش یه فکری برای چند میلیون آدمی که با قطعی اینترنت بیکار و ناامید کردین هم بودید!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/iaghapour/2601" target="_blank">📅 14:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
نمیتونم خبر رو تایید کنم ولی میگن:
— افغانستان اینترنت 5G آورده.
— عراق تلگرام رو رفع فیلتر کرده.
— سوریه هم که ویزا و مستر کارت و...
این که ما درگیر فیلترینگ مسخره هستیم واقعا گریه داره...</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/iaghapour/2600" target="_blank">📅 09:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سلام خواستم یه نکته کوچولو بگم
فقط بحث کسب و کارهای کوچیک نبود
فقط بحث آنلاین شاپ ها نبود
ماهایی که ۴ سال تو دیجیتال مارکتینگ بودیم توی طراحی سایت و سئو و اتوماسیون کار میکردیم هم کاملا ورشکست شدیم
نه از ۹ اسفند
ما یه بار جنگ خرداد زمین خوردیم تا اومدیم بلند شیم از جامون و داشتیم اوکی میشدیم دلار دی ماه سر به فلک کشید و بعد یه قطعی دیگه داشتیم که خیلی ها بهانه کردن و پول ندادن آخر دی ما هیچی پروژه نداشتیم حتی بهترین کارفرماها اومدن گفتن کار شما خیلی خوبه ولی ما واقعا پول پرسنل رو هم به زور میدیم نمیرسه به سئو
بهمن اومدیم خودمون رو جمع کنیم تیر آخر رو اول اسفند بهمون زدن
دفترمون رو تحویل دادیم
نیروهامونو از بهمن تعدیل کرده بودیم
و الان چه جوون ها و چه پدرانی که بیکار شدن
منی که تمام تخصصم همیناست
یک متخصص بیکار محسوب میشم.
©️
پیام ارسالی از کاربر shafikhany</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/iaghapour/2599" target="_blank">📅 01:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✍
حدودا 500 پیام بررسی نشده از 2 روز پیش داریم که پشتیبانی تا فردا همه رو بررسی میکنه.
جدا از بحث بالا، از ته دل آرزو میکنم تو این روزهای عجیب و غریبی که داریم می‌گذرونیم، حال دلتون خوب باشه. می‌بینیم و حس میکنم که زندگی چقدر برای خیلی‌ها سخت شده و دغدغه‌ها چقدر زیادن.
امیدواریم هرچه زودتر این روزهای سخت جاشون رو به روزهای روشن‌تری بدن. هوای خودتون و دلتون رو داشته باشید.</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/iaghapour/2598" target="_blank">📅 03:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqRcHsIXRqKjDmb2q7BvpbRVs4JythBu_fJqtVaBWu6qNATNOhyWqi9wIYMnFs46hsEYivE3_tuT77C3FoY8iyk42wYgKsZMY3Zdk_kcQw_B7iA7Xmc-nwoDWppYxfu_1fnTJmAmMt0OsFLBR5iojq-Buv3ZDV1EDMWZSegJCiuQJ52jmdLq-S6SiWOQ4ILAYcVDqeH3HoMNCZEcz8q2bok_63cG3ZOtmV42wl_Q3D9i1bpiAof-err4U1xdXh6Z4xaawtqdqyA6mNmiavOdvW96-BU3DHaxdhbxYN2u-Gs3Hzg8y0QSweT01uAuvgKux-fh4itlQlUSqcOMhTBIgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت ورژن 0.10.0 سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور ایران خودتون یک مسنجر شخصی بالا بیارید و با دوستان خودتون چت کنید.
توی آپدیت جدید سانگبرد با فعال کردن قابلیت Remote channel، میتونید پست هایی که تو یک چنل تلگرام ارسال میشه رو، به یک چنل توی سرور سانگبرد خودتون استریم کنید.
-
📡
قابلیت Remote channel
-
🔗
ساده سازی سیستم Invite link
-
🎨
بازطراحی بخش ساخت/تغییر کانال و گروه در UI
-
✨
انیمیشن build-up پیام ها در چت ها
-
🔔
بهبود عملکرد push notifications
- تغییرات گرافیکی اسکریپت نصب آسان
-
🐳
پشتیانی از TLS با سرتیفیکیت self-signed در Docker
-
🔧
رفع باگ های گزارش شده
-
📄
اضافه شدن نسخه فارسی فایل readme
🔘
اگه به هر مشکلی خوردین، حتما تو گیت هاب یک issue باز کنید و گزارش بدید.
⭐️
اگه از پروژه راضی بودین، با ستاره دادن تو گیت هاب از پروژه حمایت کنید.
🔹
چنل پروژه
🔗
لینک گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/iaghapour/2597" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭕️
ساده‌ترین راه برای دور زدن فیلترینگ با تانل DNS
اگه خانواده‌ شما هم داخل ایران برای اتصال به اینترنت مشکل دارند، این پیام ممکن است به شما کمک کند.
این برنامه یک برنامه‌ی  گرافیکیست که کار با آن بسیار ساده است و برای اتصال به اینترنت هر دو روش MasterDNS و VayDNS را پشتیبانی می‌کند.
👈
لینک گیت‌هاب
👈
دانلود
اپ
📖
آموزش کامل MasterDNS و VayDNS
▶️
آموزش روی یوتیوب
📱
آموزش KevinNet DNS
▶️
آموزش روی یوتیوب
🔄
آپدیت‌های جدید برنامه
در صورت وجود هرگونه مشکل یا سوالات مرتبط با KevinNetDNS میتوانید با آدرس ایمیل زیر در تماس باشید:
©️
متن تهیه شده توسط نویسنده اسکریپت KevinDNS
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/iaghapour/2596" target="_blank">📅 23:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⭕️
ادعای عجیب نماینده مجلس: با ۴ هزار میلیارد تومان ایتا را به سطح واتس‌اپ می‌رسانیم!
رئیس کمیته ICT مجلس در اظهارنظری جنجالی مدعی شده است که فاصله میان پیام‌رسان‌های داخلی مثل ایتا با نمونه‌های جهانی مانند واتس‌اپ، تنها در کمبود بودجه برای خرید سرور خلاصه می‌شود. به گفته او، ارتقای این پلتفرم‌ها هزینه چندانی برای کشور ندارد.
این نماینده مجلس معتقد است که پلتفرم‌های داخلی از نظر فنی کمبودی ندارند و تنها زیرساخت‌های سخت‌افزاری آن‌ها باید تقویت شود:
🔹
بودجه برای رقابت:
مصطفی طاهری مدعی است با صرف ۳ تا ۴ هزار میلیارد تومان برای خرید سرور، می‌توان کیفیت ایتا را به سطح واتس‌اپ رساند تا توانایی پذیرش بدون مشکل بیش از ۲۰ میلیون کاربر را داشته باشد.
🔸
هشدار درباره جاسوسی سخت‌افزاری:
این مقام مسئول همچنین به موضوع استفاده از بیگ‌دیتا (داده‌های بزرگ) اشاره کرده و مدعی شده که آمریکا قوانینی برای جاسوسی در لایه‌های سخت‌افزاری و تراشه‌ها (حتی پایین‌تر از سطح سیستم‌عامل) دارد.
این اظهارات در حالی مطرح می‌شود که کارشناسان حوزه تکنولوژی، موفقیت پلتفرم‌های جهانی را فراتر از صرفا تعداد سرور می‌دانند و مواردی چون امنیت، پروتکل‌های رمزنگاری، حریم خصوصی و نوآوری‌های مداوم نرم‌افزاری را از عوامل اصلی برتری آن‌ها به حساب می‌آورند.
یکی از کاربرا زیر همین پست در دیجیاتو کامنت جالبی گذاشته بود:
مامان‌بزرگ منم با چند میلیارد نیکی میناژ میشه!
پ.ن: حالا فارق از این حرفا داره میگه اینا دارن از کاربراشون جاسوسی میکنن برای همین ما باید اپ های خودمون رو داشته باشیم... من حرفی ندارم.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/iaghapour/2595" target="_blank">📅 18:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA3RbbHi8wTzD4oduMhoTWKlV-ytg3-v3HL1NTDr8ZA-NSSj8_kkglvTSJ0kLsOyLPim2QhySt4C-sD4XRZky7OGQrqFZiRqUJFzd4962d5_qa6UyVcQTmTUs1_3vy3qYCNJjGlKs9bsu1HkNwZka2FqRG-x7hyk8jApB5QWsP6c3C0HXcgAozb1x5aC0EdLgSp2mPCCWjXe_uaPtSaS6YpseAjcAbUzX8S5gcgJUeZVoG0tk0ZG3S2qMKUR1hXo8eNRuAD63StbmNbJZDE-xBM2QNiN3EVcxRLx0eFR2oMm3fksHEzzfBZmlCsdFiHWptBEkO25EgbEx2Uf8wmrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ایران 11 هفته در خاموشی دیجیتال!
هیچ‌وقت تو زندگیم فکر نمی‌کردم یه روزی برسه که این‌جوری تلخ، شاهد از بین رفتن زحمت‌ آدما باشم. ۱۱ هفته قطعی اینترنت واسه خیلی‌ها فقط یه اختلال ساده نبود؛ قصه پدر مادرا و جووناییه که با هزار امید یه کسب‌وکار کوچیک راه انداخته بودن تا خرج زندگیشونو دربیارن و الان دستشون به هیچ‌جا بند نیست.
تا همین چند وقت پیش با کلی استرس می‌گفتیم کسب‌وکارهای نوپا و خونگی تو «مرز نابودی» هستن و همه‌مون چشم‌انتظار بودیم زودتر اینترنت وصل بشه؛ ولی الان دیگه حرف از مرز نیست. خیلی‌ها کل سرمایه، جوونی و حاصل سال‌ها تلاششون جلوی چشماشون دود شد و رفت رو هوا. کاش دردی که افتاده رو دوش این مردم، میافتاد رو دوش مسئولین...
🆔
@NetProPlus</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/iaghapour/2594" target="_blank">📅 11:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">#فیلترینگ
به ما تحمیل شد,
ولی
#اینترنت_طبقاتی
رو شما باید درخواست بدی تا بهت بدن...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/iaghapour/2592" target="_blank">📅 18:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tS5gxpDsTJIGDwKJPJ5a27_2WCOk812YMFE73Z52u_HWiMpzQA5EhBu3c7qFM-18u7yDb1kCjHGwsxIEIbv7L9DA810h_kfQ0uHU63opZc9wJanmosQQQqOltpGGOXtI5n5OhDOucIlCt4ALsPYAQ3-nKyFXReC3C1XA2jdppjMGdEfbSfn_NyupBCfNh2YJoF47jdk-AazOl4-a1rdizYm0fYqH9aXfT5Dovp2OVNKHYouqIhUGg7ZFN3xDBEHR615zQaXujHv0taDiKnfe0IjJmddD8izdam3pNccyTfwheWUA9lsSd8sQQPOt0-h9zvaeSS6rxkV68G0kqNIllA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت بزرگ تلگرام: ورود دستیار هوشمند به پروفایل شخصی!
تلگرام در آپدیت جدید تمرکز ویژه‌ای روی هوش مصنوعی داشته است. در ادامه مهم‌ترین تغییرات این نسخه را مرور می‌کنیم:
🔹
ربات‌های مهمان:
فراخوانی ربات‌ها در هر چت یا گروهی، تنها با تگ کردن آیدی و بدون نیاز به افزودن آن‌ها.
🔸
منشی شخصی هوشمند:
قابلیت اتصال مستقیم یک ربات به پروفایل شخصی تا در غیاب شما به پیام‌ها پاسخ دهد!
🔹
تعاملات زنده هوش مصنوعی:
تایپ و نمایش لحظه‌ای پاسخ ربات‌ها، به همراه قابلیت جدید ارتباط ربات با ربات برای انجام وظایف پیچیده‌تر.
🔸
امکانات جدید برای کانال‌ها و تولید محتوا:
قابلیت محدود کردن نظرسنجی‌ها (بر اساس کشور یا عضویت در کانال)، مشاهده نمودار آرا، و همچنین ساخت استایل‌های متنی سفارشی.
🔹
اضافه شدن قابلیت انتخاب فونت از سیستم خودتون (میتونید فونت وزیر رو نصب کنید و استفاده کنید).
با این به‌روزرسانی که شامل جستجوی هوشمند ایموجی‌ها، ارسال بی‌صدای پیام زمان‌بندی‌شده و رفع ۲۰۰ باگ فنی است، تلگرام قدم بزرگی برای ادغام کامل پیام‌رسانی انسان و هوش مصنوعی برداشته است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/iaghapour/2591" target="_blank">📅 14:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔻
مومن‌نسب: فضای مجازی به هیچ وجه نباید به حالت قبل برگردد
حالا این آدم انقدر مهم نیست که دربارش صحبت کنیم ولی خواستم بگم این همون آدمیه که چندسال پیش تو صداوسیما میگفت من خطرات اینترنت رو میدونم و اطلاع دارم یک نفر با 2 گیگ اینترنت حامله شده و پدر دختره با گریه اینو برای من تعریف می‌کرد...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/iaghapour/2590" target="_blank">📅 11:35 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
اطلاعیه مهم: معرفی فروشندگان کانفیگ
طبق نتایج
نظرسنجی اخیر،
قصد داریم فروشندگان قدیمی و معتبری که از قبل می‌شناسیم را یکی‌یکی برای خرید به شما معرفی کنیم.
📌
قوانین و شرایط مربوط به فروشندگان:
—
عدم پذیرش فروشنده جدید:
در حال حاضر شخص جدیدی معرفی نمی‌شود؛ بنابراین لطفاً در قسمت
«تماس با ما»
برای معرفی خود پیام ندهید. افرادی که معرفی می‌شوند، همگی پیش‌تر در کانال ما سابقه تبلیغ داشته‌اند.
—
تضمین خرید شما:
مبلغی از پول این افراد نزد ما به عنوان امانت می‌ماند تا در صورت بروز هرگونه مشکل، بتوانیم مطالبات شما کاربران عزیز را پیگیری کنیم.
—
ضمانت بازگشت وجه:
این فروشندگان موظف‌اند در صورت لزوم (بسته به شرایطی که خودشان به شما اعلام می‌کنند)، بین ۴۸ تا ۷۲ ساعت امکان عودت وجه را فراهم کنند.
—
قیمت منصفانه:
تمامی این افراد تعهد داده‌اند که نسبت به شرایط بازار، قیمت‌های منصفانه‌تری برای کاربران کانال ما در نظر بگیرند.
— معرفی فروشندگان صرفاً در زمینه
فروش کانفیگ
انجام می‌شود. هیچ‌یک از فروشندگان معرفی‌شده مجاز نیستند پس از معرفی، در کانال شخصی خود تبلیغات مربوط به "
اوتباند
" قرار دهند و یا به کاربران پیشنهاد خرید آن را بدهند.
⚠️
نکات مهم برای کاربران عزیز:
—
انتظارات از کیفیت:
کانفیگ‌ها باید بتوانند تلگرام، اینستاگرام و یوتیوب را به راحتی باز کنند. با توجه به شرایط فعلی اینترنت، داشتن سرعت‌های بسیار بالایِ گذشته کمی دور از انتظار است (هرچند ممکن است کیفیت سرویس‌ها عالی باشد)، پس لطفاً واقع‌بین باشید.
—
اختلال و پشتیبانی:
ممکن است در طول هفته، گاهی با اختلال مواجه شوید. پشتیبان‌ها موظف‌اند در سریع‌ترین زمان ممکن مشکل را حل کنند؛ اما لطفاً صبور باشید، حداقل یک ساعت به آن‌ها فرصت دهید و از ایجاد فشار زودهنگام به پشتیبانی کانال‌ها خودداری کنید.
— در ضمن، توجه داشته باشید که
ما ذی‌نفع این کانال‌ها نیستیم
و فقط به دلیل درخواست‌های زیاد شما این دوستان را معرفی می‌کنیم.</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/iaghapour/2589" target="_blank">📅 23:36 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSu-hIA4YGfaKB2rmOzzaHxufUe7kGoUMIkRN-Uox_Q3VY29j83S6B_RrbKmxiFiaxCx00DVhCdvXaaXCWyTh5Wrzg2lWugcDd1DafEZUEUixCbo6oDKzxhJGojmClbDP1uJnKzYCttdyfCSN5eq4amt5L6x9887s8jHo2_q0_jLOeUpdHIjp_OHqyUQG-KEAwiN9uk_i1IHt2UucAFWb4U_SY4p_TW2TYoU6ZqedGuYXWu8z-rHd6PB-n-kYEE1R_V8vmM_EDCww67MHszgYXI520LlbdoGPADftWxAwE2y4v48c2kirh5ROGxpJVV5Ts81lBNrxJMlZ49cG0EaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
سخنگو وزارت خارجه حذف تیک آبی خود در شبکه X را (سرکوب حقیقت) خواند.
68 روزه اینترنت مردم ایران رو قطع کردن، بعد یه تیک آبی‌شو گرفتن میگه حقیقت سرکوب شد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/iaghapour/2588" target="_blank">📅 20:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔻
تسنیم: درآمد طرح اینترنت «پرو» در سال به ۹۶ هزار میلیارد تومن می‌رسه!
🔹
خب با این رقم‌های نجومی و پول هنگفتی که درمیاد، معلومه که از این تبعیضی که راه انداختن حسابی راضی‌ان. وقتی محدودیت و فیلترینگ این‌قدر براشون سود داره، چرا نباید اینترنت داخلی و بسته رو بیشتر تحویل بگیرن؟
🔸
این وسط یه تشکر ویژه و خسته نباشید هم باید بگیم به اون دسته از دوستانی که رفتن تو صف اینترنت پرو و این سیستم طبقاتی رو خیلی راحت پذیرفتن. از رئیس فلان اتحادیه و مدیر فلان اداره بگیر تا نماینده صنف لاستیک‌فروش‌ها و یه سری کسب‌وکارهایی که واقعاً بدون اینترنت آزاد هم کارشون لنگ نمی‌موند. تو شرایطی که ۹۹ درصد مردم هیچ دسترسیِ عادی به اینترنت آزاد ندارن، مرسی از شماها که رفتین این اینترنت رو گرفتین و با این کارتون، قشنگ به این تبعیض و نابرابری رسمیت دادین!
پ.ن: البته به این نکته هم توجه کنید که خبرگذاری داخلی اینو گفته و ممکنه دقیقا مقصودشون از این حرف هم همین باشه که بگن چقدر این طرح خوب و سودآور هستش و...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/iaghapour/2587" target="_blank">📅 14:33 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⭕️
وعده بازگشت به وضعیت عادی؛ توجیه محدودیت‌ها یا امید به بهبود اینترنت؟
معاون ارتباطات دفتر رئیس‌جمهور به تازگی اعلام کرده که وضعیت فعلی اینترنت مورد تایید دولت نیست و رئیس‌جمهور، محمدرضا عارف را مامور ساماندهی این شرایط کرده است. به گفته او، این محدودیت‌های شدید و قطعی‌ها صرفا تصمیماتی از سوی شورای عالی امنیت ملی و به دلیل شرایط خاص امنیتی و جنگی بوده‌اند.
🔹
وعده روزهای بهتر:
این مقام مسئول قول داده که با عبور از این شرایط ویژه، اینترنت نه تنها به حالت قبل برمی‌گردد، بلکه وضعیتی بهتر از گذشته پیدا خواهد کرد و وعده‌های انتخاباتی رئیس‌جمهور در این زمینه همچنان پیگیری می‌شوند.
🔸
دفاع از اینترنت پرو:
در واکنش به انتقادات، دولت ادعا می‌کند طرح «اینترنت پرو» صرفا برای نجات کسب‌وکارها در روزهای محدودیت ایجاد شده و نباید به آن برچسب اینترنت طبقاتی زد؛ چرا که به گفته آن‌ها، در شرایط عادی اصلا نیازی به چنین طرحی نخواهد بود.
🔹
کاهش محدودیت‌های عمومی:
خبر دیگر این است که قرار شده تدابیر جدیدی برای دسترسی بهتر سایر شهروندان به اینترنت اتخاذ شود تا فشار محدودیت‌های فعلی روی مردم کاهش یابد.
در حالی که دولت تلاش می‌کند قطعی‌ها و طرح‌های بحث‌برانگیزی مثل اینترنت پرو را صرفا به شرایط اضطراری گره بزند، کاربران و کسب‌وکارها همچنان منتظرند تا ببینند آیا این وعده‌ها در عمل به یک اینترنت آزاد و بدون محدودیت ختم می‌شود یا صرفا وعده‌ای برای کنترل نارضایتی‌های فعلی است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/iaghapour/2585" target="_blank">📅 21:12 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⭕️
ایده عجیب در مجلس: تاسیس «اینستاگرام دولتی» و مدیریت کامل اینترنت!
نمایندگان مجلس در تازه‌ترین نشست خود با وزیر ارتباطات، از طرح‌ها و نگاه‌های جدیدی برای کنترل بیشتر فضای مجازی پرده برداشتند. در این جلسه، پیشنهاد ایجاد یک پلتفرم کاملا دولتی مشابه اینستاگرام مطرح شد تا به زعم آن‌ها، نیاز کشور برطرف شود.
🔹
اینستاگرام دولتی:
یکی از نمایندگان با اشاره به بازار سیاه و چند میلیونی فیلترشکن‌ها، رسما پیشنهاد ساخت یک سکوی دولتی شبیه اینستاگرام را برای پر کردن جای خالی این پلتفرم ارائه داده است.
🔸
رویای مدیریت اینترنت:
نایب رئیس مجلس تاکید کرده که مشکل آن‌ها اصل اینترنت نیست، بلکه می‌خواهند در صحنه بین‌المللی، مدیریت اینترنت کاملا در دست خودشان باشد و این فضا را به یک جبهه تقابل تشبیه کرده است.
🔹
فرصت‌سازی از بحران:
بخش قابل توجهی از صحبت‌های نمایندگان، حسرت خوردن برای از دست رفتن فرصت در شرایط ملتهب و جنگی است؛ آن‌ها معتقدند باید از این شرایط استفاده می‌کردند تا مردم و کسب‌وکارها به اجبار به سمت سکوهای داخلی کوچ کنند.
این صحبت‌ها به وضوح نشان می‌دهد که دغدغه اصلی، کاهش نارضایتی مردم از قیمت و کیفیت اینترنت نیست؛ بلکه تلاش برای بومی‌سازی اجباری، قطع ارتباط با شبکه‌های اجتماعی بین‌المللی و کشاندن کاربران به پلتفرم‌های تحت کنترل و نظارت است. / زومیت
✍🏻
پ.ن: از سوپر اپلیکیشن های ایتا و سروش و گپ و بله که از تلگرام کپی کردین مشخصه توانایی اینکار رو دارید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/iaghapour/2584" target="_blank">📅 19:36 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⭕️
مرگ خاموش اقتصاد خرد: نابودی ۴۰ درصد از کسب‌وکارهای اینستاگرامی!
قطعی‌ها و محدودیت‌های اینترنتی فقط حق دسترسی آزاد ما به شبکه‌های اجتماعی را سلب نکرده، بلکه تیشه به ریشه‌ی اقتصاد خرد و معیشت مردم زده است. طبق اعلام پشوتن پورپزشک، عضو هیئت‌مدیره اتحادیه کسب‌وکارهای مجازی، فیلترینگ و اختلالات باعث نابودی بخش عظیمی از مشاغل آنلاین شده است.
🔹
فاجعه‌ی آماری: نزدیک به ۴۰ درصد از کسب‌وکارهای اینستاگرامی برای همیشه از بین رفته‌اند؛ این یعنی مرگ مستقیم بیش از ۴۰۰ هزار شغل!
🔸
دومینوی ویرانی: وقتی شوکی مثل محدودیت اینترنت وارد می‌شود، ابتدا کسب‌وکارهای کوچک و آسیب‌پذیر می‌میرند، اما این نابودی با کمی تاخیر گریبان شرکت‌های بزرگ اقتصادی را هم خواهد گرفت.
🔹
زنجیره‌ی به هم پیوسته: کسب‌وکارهای بزرگ در تولید، تامین و توزیع به شدت به همین کسب‌وکارهای خرد وابسته‌اند. توهم مصونیت برای شرکت‌های بزرگ، در نهایت منجر به فروپاشی خود آن‌ها می‌شود. منبع: زومیت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/iaghapour/2583" target="_blank">📅 19:29 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اسم این زندگــــــی نبود
یک مبارزه تمام عیار بود...
#جوانی
#زندگی
#جنگ
#اینترنت</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/iaghapour/2581" target="_blank">📅 19:09 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭕️
حل مشکل دانلود از ریلیز گیت‌هاب با LatestReleaseMirror
اگر در دانلود فایل‌ها از بخش ریلیزهای (Releases) گیت‌هاب به دلیل محدودیت‌های اینترنت مشکل دارید، این اسکریپت کاربردی دقیقاً برای شما ساخته شده است!
ابزار
LatestReleaseMirror
به صورت خودکار فایل‌های آخرین آپدیتِ ریپازیتوری‌های دلخواه شما را دریافت کرده و آن‌ها را به عنوان فایل‌های عادی در ساختار پوشه‌های گیت‌هاب ذخیره می‌کند؛ در نتیجه می‌توانید آن‌ها را به راحتی و حتی با اینترنت داخلی دانلود کنید.
🔹
دریافت و آپدیت خودکار آخرین نسخه با استفاده از GitHub Actions.
🔸
امکان فیلتر کردن فایل‌های مورد نیاز (مثلاً فقط نسخه‌های ویندوز یا اندروید)
🔹
دسته‌بندی تمیز فایل‌های خروجی در مسیرهای مشخص.
🔗
لینک ریپازیتوری و راهنمای استفاده
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/iaghapour/2580" target="_blank">📅 16:09 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ركورد جديد سرعت اينترنت ژاپن:
با سرعت 1.02 پتابيت بر ثانيه، كل نتفليكس را در 1 ثانيه دانلود مى‌كند.
✍
ما هم اینجا باید با DNStt وصل بشیم تا بزور بتونیم فقط این خبر رو بخونیم...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/iaghapour/2579" target="_blank">📅 13:56 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭕️
اسکریپت بهینه شده XHTTP Relay ECO برای Vercel Pro
🔹
نسخه ECO طوری تیون شده که علاوه بر امنیت سفت‌وسخت v1.3، کم‌هزینه‌ترین رفتار ممکن روی Vercel Pro رو داشته باشه؛ یعنی با کنترل هوشمند Timeout، Inflight، Throttle و Logها، مصرف منابع و هزینه نهایی تا جای ممکن پایین نگه داشته میشه.
🔸
فقط با GET، HEAD و POST کار می‌کنه تا امنیت بالاتر بره.
🔹
احراز هویت فقط از طریق هدر x-relay-key انجام میشه
🔸
هدرهای اضافی پلتفرم و hop-by-hop رو بی‌رحمانه فیلتر می‌کنیم.
🔹
روی آپلود و دانلود محدودیت سرعت (Throttling) واقعی گذاشتیم.
🔸
بردیمش روی Node runtime با لیمیت ۱۲۸ مگابایت رم و مدیریت کانکشن‌های همزمان.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/iaghapour/2578" target="_blank">📅 22:28 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⭕️
ورژن جدید کلاینت اندروید GooseRelayVPN منتشر شد
کلاینت اندروید GooseRelayVPN که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد. این اپ یک SOCKS5 محلی روی اندروید ایجاد می‌کند و ترافیک TCP را از معماری GooseRelay عبور می‌دهد.
🔹
هسته پروژه به ورژن 1.5.0 آپدیت شد.
🔸
قابلیت fake dns اضافه شد.
🔹
باگ ها در این نسخه برطرف شدن.
🔗
آدرس گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/iaghapour/2577" target="_blank">📅 14:05 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0lgwALAAyaY35tjvby_Wjb2l18c0LBoe-HPtLruocOkkMjtObMjbR3ZeH2oi75fbiF_O-BWI6sgCbe4YsS1ejk9My3Uk-sSxm57bjjEi-Uih92Jjwyq1plQMsVGGg2of6KLEOrqmTvcMs_nKOGAQUU4HLY640VaO-9A5vfbIcXGh9hnqmuihX3MvgUEI27HwSBnhJLXvo1i8DkXFA4mJh4Yo3_vgg6e5fwl4aHI66C134ZeyOy8_ymzp5BhsH2VI7NC8KrBeRLoV8TIubnEJ88_QImMmj5jnJSpqQTUlpWLWWPPIYt7NmbsP17vGh9blAIbyv58wmCrnEz1iSFMuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت فیلترشکن رایگان و شخصی به 2 روش با نت ملی
🔹
با استفاده از دو ابزار قدرتمند MHRV و Nova-Proxy، دیگه نیازی به خرید کانفیگ‌ها و سرورهای گرون‌قیمت ندارید. تو این آموزش قدم‌به‌قدم به ۲ روش مختلف پیش میریم تا بتونید یه اتصال پایدار و بدون قطعی داشته باشید. حتماً تا آخر ویدیو همراه من باشید.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔹
دانلود کلاینت ویندوز
🔸
دانلود کلاینت اندروید
#آموزش
#فیلترشکن
#mhrv
#novaproxy
#رایگان
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
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/iaghapour/2576" target="_blank">📅 19:53 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/in4lniiJYWznNzK7rLjtAGCko0ejNdlAfWomldbZtrPbddi0ctblsJWf3i48DPGHez47fNRjCx_FIRlJ-tGKtbB00glAU9549aBHjVj4KNrBHGq-AU5Zek2-J9gX6lnL2KnwnfrYvO7PQr9lrDyOHUuC7HFJtBvvFB3KomR986LGOSEWb6EqDjWyDpfRgrqNp22YJU5R01GCjpvK_yv5Q11doUiV32uJPCxTxr7KEGFI97iSn_KfPM050pCpfvTTiffFxWwwXbSMnEP9tLJ1xqIPvHh4w4hp3N5t-JnTce6oVDY6VRX5piMnAxh-E5efhTOTe5LDJSGWE1SuZrU_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پشت‌پرده‌ی «اینترنت پرو»؛ امتیاز ویژه یا تله‌ی نظارتی؟
این روزها سیم‌کارت‌های بدون فیلتر با نام «اینترنت پرو» در ازای دریافت هزینه و ثبت کامل مشخصات هویتی به فروش می‌رسند. اما هدف اصلی این طرح، دلسوزی برای نیاز اینترنتی اقشار مختلف نیست.
هدف اصلی و پنهان این ماجرا، چیزی جز «تشخیص هویت دقیق و رصد لحظه‌ایِ کاربر» نیست.
👁‍🗨
وقتی اینترنت آزاد را مستقیماً با نام و کد ملی خودتان دریافت می‌کنید دقیقاً چه اتفاقی می‌افتد؟
🔹
پایان گمنامی:
تمام سایت‌هایی که سر می‌زنید و محتوایی که می‌بینید، مستقیماً و شفاف روی نام خودتان ثبت و مانیتور می‌شود.
🔸
تزریق خودسانسوری:
وقتی می‌دانید هر کلیک شما رصد می‌شود، ناخودآگاه وارد یک «زندان شیشه‌ای» می‌شوید که خودتان هزینه‌اش را داده‌اید!
🔹
تجارت با حقوق اولیه:
حق بدیهی دسترسی به اینترنت آزاد را مسدود کرده‌اند و حالا همان را به قیمت نقض حریم خصوصی، به عنوان یک «آپشن ویژه» به خودمان می‌فروشند.
«اینترنت پرو» یک امکان رفاهی نیست؛ ابزاری برای کنترل نقطه‌ای و عادی‌سازیِ اینترنت طبقاتی است. بهای اصلی این سیم‌کارت‌ها پول نیست؛ حریم خصوصی ماست.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/iaghapour/2575" target="_blank">📅 15:30 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/om3WH7gfyV3zIJV7ze-a5b6EMi9jlwr021ifOmox-JZoX49zyrDDrtVSAbgPbmP86cO7oiM6d_b-fGoax_XLVCgkQSjq_rdw_jz0jU67aKw47BEUp0pngPZJwMhlLbcHTerVCyCR_hcFQ8ikSYQvEX8X4Tuwan0gXEZi-2w1Nl3KT_iqKCjuQM379Kdv4YXcNtnY9QhBA7ZsnOApTtwpT0rvUTPnolkxQYxkEeIPRH0Vv55Vjua6ifYOCEw_v0HbyWcqfO29vxXdmDsAofHpl7T8mkVmdcxw5LxtnzExWV_T3v5xeXjKxnRvHPAp6JANZRMAD0uwnkMenconEB_nlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
کلاینت اندروید GooseRelayVPN
🔹
کلاینت اندروید GooseRelayVPN که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد. این اپ یک SOCKS5 محلی روی اندروید ایجاد می‌کند و ترافیک TCP را از معماری GooseRelay عبور می‌دهد.
🔹
پیکربندی مبتنی بر پروفایل
🔸
وضعیت و تله‌متری در صفحه Home
🔹
تب Logs برای عیب‌یابی Android/Core
🔸
قابلیت Split Tunneling و Internet Sharing
🔗
آدرس گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/iaghapour/2573" target="_blank">📅 20:06 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">💢
رئیس اتحادیه کسب‌وکارهای مجازی
:
به شرکت‌ها زنگ می‌زنند و پیشنهاد فروش اینترنت بدون فیلتر(پرو) برای کارمندانشان را می‌دهند.
⁉️
اگر موضوع واقعاً امنیت ملی است، چطور با پرداخت پول، امنیت تأمین می‌شود؟!
منبع: کانال خبری
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/iaghapour/2572" target="_blank">📅 13:23 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-poll">
<h4>📊 ⁉️نظرسنجی درباره سوال بالا (اگه واقعا نیاز دارید بله رو بزنید).</h4>
<ul>
<li>✓ بله معرفی بشه.</li>
<li>✓ خیر نیازی نیست.</li>
</ul>
</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/iaghapour/2571" target="_blank">📅 00:25 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✍🏻
دوستان، همان‌طور که خودتون در جریان هستید، من در این چند ماه حتی یک مورد
تبلیغ فیلترشکن، اوتباند
و موارد مشابه
قرار ندادم.
الان هم واقعاً تمایلی به این کار ندارم، چون شرایط اصلاً به‌گونه‌ای نیست که بشه کسی را معرفی کرد.
با این حال، در همین چند ماه پیام‌های بسیار زیادی داشتیم که درخواست می‌کردند حتماً یک شخص معتبر را معرفی کنیم؛ چرا که خیلی‌ها از کلاهبرداری‌های پیاپی خسته شدن و ارسال این دست پیام‌ها تا به همین امروز هم ادامه داره.
به همین دلیل، اگه خودتون موافق باشید،
افرادی رو که
از قبل با ما همکاری می‌کردند
و تا حدودی قابل‌اطمینان هستند، یکی‌یکی به شما معرفی کنیم. در این مورد ذکر چند نکته ضروری هستش:
🔸
عدم تضمین صددرصدی:
ناگفته نماند ما واقعاً نمیتونیم کسی را با اطمینان ۱۰۰ درصدی تأیید کنیم، اما افرادی که معرفی میشن همگی سابقه همکاری با ما را دارن.
🔹
عدم پذیرش تبلیغ جدید و اوتباند:
تا زمانی که شرایط استیبل و پایدار نشود، تبلیغ
هیچ فرد جدیدی را قبول نمی‌کنیم.
در ضمن،
تبلیغ فروش اوتباند هم به‌هیچ‌وجه پذیرفته نمی‌شود.
🔸
قیمت‌های منصفانه:
تمام سعی ما بر اینه افرادی را معرفی کنیم که در این زمینه منصف باشند و قیمت‌های بالایی ارائه ندهند. ولی خب، طبیعتاً نمیشه انتظار قیمت‌های قدیمی را داشت؛ چون همان‌طور که خودتون میدونید در حال حاضر هیچ‌کس با اون قیمت‌های قبلی فروشی نداره.
اگه تمایل دارید، لطفاً در نظرسنجی زیر شرکت کنید.
البته نظر شخصی خودم اینه که اگه در حال حاضر واقعاً مشکل خاصی ندارید، در نظرسنجی همان گزینه
(خیر) را انتخاب کنید
.</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/iaghapour/2570" target="_blank">📅 00:24 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⚠️
هشدار مهم درباره اسکریپت VPN Over GitHub
▪️
لطفاً از این ابزار به عنوان
فیلترشکن
استفاده نکنید!
🚫
بن شدن اکانت:
تبدیل گیت‌هاب به تونل ترافیک، خلاف قوانین این سایت است و خیلی زود باعث مسدود شدن حساب شما می‌شود.
🐢
سرعت بسیار پایین:
برای هر ارتباط به یک بار
push
و
pull
نیاز دارد که آن را عملاً غیرقابل استفاده می‌کند.
🔻
خطر برای برنامه‌نویس‌ها:
گیت‌هاب یک سایت حیاتی برای توسعه‌دهندگان است؛ سوءاستفاده از آن ممکن است باعث حساسیت شده و دسترسی به این پلتفرم مهم را دوباره از کار بیندازد. (خارج شدن از لیست سفید و...)
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/iaghapour/2569" target="_blank">📅 19:21 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ای بابا روش Vercel چرا بسته شد؟ هنوز آموزش نداده بودم که.
😁
سازمان فیلترینگ زرنگ شده ها. فک کنم خودشون رو آپدیت کردن دیگه به کانال من نگاه نمیکنن :)</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/iaghapour/2567" target="_blank">📅 16:34 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
دلار 177 و طلا 19,400,000
شب میخوابی صبح بلند میشی یه پله بدبخت تر میشی!</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/iaghapour/2566" target="_blank">📅 11:10 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حالا نیاز نیست پول بدین ری اکشن فیک بزنید.
😁</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/iaghapour/2565" target="_blank">📅 20:52 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GooseRelayVPN Guid -- @iAghapour.txt</div>
  <div class="tg-doc-extra">1.2 KB</div>
</div>
<a href="https://t.me/iaghapour/2564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
دستورات
برای ویدیو
GooseRelayVPN
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/iaghapour/2564" target="_blank">📅 14:21 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjOJiZXDAUsqqUEGreKrC5hS6uoz80c4hXl24Aipkk-_Lk8Cuk3umY_hmqHptdjuQBmrOxDmw_LDhSqCyMAyr1_rC0nkqjsqzY4uWpch154LxXS_bS4VhV5S_WsGE9imd5B6td2bPQUp2GSc7i7MF-icAQ-MoiDe831HzAMZqFVF_cbGboT5C6wGgxGbQ_DfGjemmj_OjX1dJEzoidDIVreV5HkhU7nemG0D7GoAKlPpWXasvePsH-hRjHXKFQYqFPr1_uW9jgubCj-LV-7qRrqsqYevlCpOqMcG1fojc4qbAYyVucM97ZKGc4bRReIVJi16jla1q0_xN68cIitDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت فیلترشکن شخصی و تانلینگ امن با سرویس‌های ابری! (GooseRelayVPN)
🔹
در این آموزش، یک روش عالی به نام GooseRelayVPN رو بهتون معرفی می‌کنم. با استفاده از اسکریپت‌های ابری (Apps Script) به عنوان واسطه و اتصال اون به سرور لینوکسی خودمون، یک تانل امن میسازیم.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔻
دانلود فایل کدها
#آموزش
#فیلترشکن
#گوگل
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
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/iaghapour/2563" target="_blank">📅 14:18 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✍🏻
از اونجایی که دیگه کسی حوصله خوندن خبر رو نداره براتون عناوین خبر رو قرار دادم :)
🔸
دو ماه قطعی اینترنت؛ تعدیل ۳۰ تا ۵۰ درصدی نیروی انسانی در شرکت‌های اینترنت اشیا
🔹
ثبت ۳۱۸ هزار درخواست کار در یک روز در جاب‌ویژن
🔸
کانون وکلای اصفهان هم اینترنت «پرو» را نپذیرفت
🔹
ارسال پیامک اینترنت «پرو» این بار برای مهندسان
🔸
خزنده‌های گوگل پس از ۶۰ روز قطعی، دوباره سایت‌های ایرانی را می‌بینند
🔹
ضربه سنگین قطعی اینترنت به اشتغال زنان
🔸
دبیر سابق شورای‌ عالی فضای مجازی: اینترنت بین‌الملل می‌تواند ظرف ۵ دقیقه وصل شود.
🔹
سخنگوی دولت: با پایان بحران وضعیت اینترنت تغییر خواهد کرد
منبع: زومیت - دیجیاتو
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
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/iaghapour/2562" target="_blank">📅 11:54 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسکریپت KevinNet DNS با پشتیبانی از VayDNS آپدیت شد
حدودا 1 هفته پیش یک آموزش ضبط شده به اسم
(بهینه ترین روش اتصال با پروتکل DNS)
و توی این ویدیو ما اومدیم اسکریپت
KevinNet
رو معرفی کردیم. و الان در آپدیت جدید میتونه از VayDns هم ساپورت کنه.
🔹
اضافه شدن قابلیت تغییر مقادیر در برنامه
🔸
قابلیت تست ریزالور حتی در vaydns
🔹
قابلیت ایجاد پروفایل متعدد برای دامنه
. قابلیت های دیگه ...
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/iaghapour/2559" target="_blank">📅 19:22 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVU5fphvOLvDM2ezFqAIuCxD1OHyj7pzPYQk0vbB2UBIHyc5xGp9SZSJG2vksV2RHNc33qpZZNbYQr6GEgr7mJLMAiUZsXcqfG16H_TvR07TYw7ZfakyFUMfA_yTn8YOLr3O_8p_uzCMBKK7EzB2DvVXJ4poFVhyAudnHOCFZ65OrNF3FkEvRmJVh8W_JHiTgVvOy0OuhKUpmC95SFDxU2dHlbCn9Hfyc79hvnPrEw5WYmEpO4s54enRZmOGwItuUn8TBCanV4cRINTGaimkWFogyX82KlBnQwuRBVxByhlHCAHQ15eOHtgR0evCrZOF-wBlUki_xF-o3FlOXJL2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت هارد ۱۰ ترابایت بنفش (Western Digital Purple) ناقابل 108 میلیون
🫠
همینطوری ادامه داشته باشه برای خرید یک گوشی دکمه ای هم باید همین مقدار پول بدیم....
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/iaghapour/2558" target="_blank">📅 09:34 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIupp0aDmMQGJEtWWTkxesUrSazWdIObu09IIuVQ_Jsujy0tVfTuQL3Xyl0Vv6pe-O0BgTtsqXxiVgAWo-PnUCMRTTPUqLowhlKkR8WK_TS41zN2eby9pjkRAsoW_tRemxnsyUa8LLWh318Q7r5GD7XN2TP8MvnTZuyOCRMKm16SAoWTowaRU6vxsqdP8hliTEI6Mb-42KDBJgdbaQJv_Jrx-5ZfARThvX3kU0bOJdZGrwOh8FH2DXD2OyKOHmGTmXcEbMRYH8DSovygcZX2tuXr5mT5OkC79VZ_54oY_xqykA0HAtJfevSozs1jEnoN-WtMtb76LrXIoW_W5J3wLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نصب‌کننده خودکار Parley Chat
🔻
از اونجایی که راه‌اندازی و کانفیگ کامل یک پلتفرم چت روی سرور (با تمام دردسرهای تنظیم دیتابیس، وب‌سرور و گواهینامه امنیتی) کار سخت و زمان‌بریه، این ابزار جذاب اومده تا همه چیز رو براتون ساده کنه!
🔸
راه‌اندازی کامل بکند (Backend) و فرانت‌اند (Frontend)
🔹
کانفیگ خودکار Nginx به همراه دریافت گواهینامه SSL
🔸
ایجاد سرویس‌های Systemd برای مدیریت آسان‌تر و پایداری سرویس
🔗
لینک گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/iaghapour/2557" target="_blank">📅 21:48 · 06 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
