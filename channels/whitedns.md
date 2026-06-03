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
<img src="https://cdn4.telesco.pe/file/EoWwxbdq1D55HCkiE01p0-WQ7NQjEHnFEwYh2cotVBMXf-AsLyZWn86IhQj6rxCJvi7ea2oH350U-43ZGiiXzczUqDBpAVlwaE9avN78B2c3-eqavhTBZAWN6DpiUJ5AklGMl51QaQEVDmFxVOvXg-GsN5I6xpY-rMg35Pv_z3mmNdDs-sjceRzN1p5X33-ppMRZh3NXC-osNU1UaBEqK6XxkR1zuztbxes6SU5QDi9Y6oSmXm_STWxybTU60TjIyz2u4V03BnZEkfeFunRaOInhP2vIfolYfAOpNa_BOMU7pRUgk93osP0ROcqEevkMQma2-NikUfdFZrJQwhcRkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 105K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhisperInHeaven</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 00:03:17</div>
<hr>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوستان و همراهان عزیز، سلام
🌺
لطفاً چند لحظه وقت بگذارید و این پیام مهم را در خصوص
نحوه ارتباط با ادمین‌ها
مطالعه کنید.
آیدی ادمین که در توضیحات (بایو) کانال قرار داده شده،
فقط و فقط
برای موارد خاص زیر است:
🔸
گزارش تخلفات
🔸
پیشنهادات همکاری در زمینه‌های مختلف
⚠️
لطفاً به این نکات توجه ویژه داشته باشید:
۱.
سوالات خود را در گروه بپرسید:
تمامی سوالات و مشکلات فنی باید فقط در
گروه‌های ما
مطرح شوند. لطفاً از ارسال پیام خصوصی (پی‌وی) به ادمین‌ها خودداری کنید. ما تیم پشتیبانی مجزایی نداریم که بتواند روزانه به صدها پیام خصوصی به‌صورت تک‌به‌تک پاسخ دهد.
۲.
توقع پاسخگویی در موارد نامربوط:
متاسفانه روزانه پیام‌های بی‌ربط زیادی دریافت می‌کنیم و در کمال تعجب، برخی از دوستان در صورت عدم دریافت پاسخ شاکی شده و حتی تهدید می‌کنند!
برای روشن شدن موضوع، به طور مثال
موارد زیر در تخصص ما نیست
و از پاسخگویی به آن‌ها در پیام خصوصی معذوریم:
❌
رفع مشکلات کامپیوتر، موبایل و یا خرابی مودم خانگی شما (برای این موارد به متخصصین شهر خود مراجعه کنید).
❌
مشاوره برای خرید تجهیزات سخت‌افزاری (مثل قطعی کابل شبکه و اینکه چه کابلی بخرید).
❌
آموزش خرید رمزارز و معرفی صرافی‌های مناسب.
❌
و هزاران مورد نامربوط دیگر که خارج از حوزه فعالیت ماست.
🙏
خواهشمندیم با رعایت این موارد، از ارسال پیام‌های خارج از موضوع به ادمین‌ها جداً خودداری فرمایید تا بتوانیم در موارد ضروری پاسخگوی شما عزیزان باشیم.
از درک و همراهی شما سپاسگزاریم
🌹</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/929" target="_blank">📅 16:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚠️
⚠️
⚠️
#موقت
⚠️
هر پیام اضافه، سؤال، بحث یا محتوایی غیر از نام سرور زیر این پست، باعث بن شدن خواهد شد.   سلام به همه دوستان عزیز  برای بررسی وضعیت اتصال، نیاز داریم یک تست همگانی انجام بدیم تا مشخص بشه در حال حاضر کدام متدها و سرورها برای شما وصل هستند. …</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/whitedns/927" target="_blank">📅 08:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚠️
⚠️
⚠️
#موقت
⚠️
هر پیام اضافه، سؤال، بحث یا محتوایی غیر از نام سرور زیر این پست، باعث بن شدن خواهد شد.
سلام به همه دوستان عزیز
برای بررسی وضعیت اتصال، نیاز داریم یک تست همگانی انجام بدیم تا مشخص بشه در حال حاضر کدام متدها و سرورها برای شما وصل هستند.
لطفاً قبل از تست، ساب خودتون رو یک‌بار Refresh / Update کنید.
برای شرکت در این تست:
به سابسکریپشن WhiteDNS وصل باشید.
داخل اپلیکیشن موبایل یا کامپیوتر وارد بخش Logs / لاگ‌ها شوید.
نام سروری که به آن وصل شده‌اید را زیر همین پست برای ما ارسال کنید.
لطفاً فقط نام سرور را ارسال کنید.
اگر نمی‌دانید دقیقاً باید چه کاری انجام دهید، مشکلی نیست؛ می‌توانید در این تست شرکت نکنید.
ممنون از همکاری شما
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/whitedns/926" target="_blank">📅 07:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">لینک ساب ها درست شدند
😃
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/whitedns/925" target="_blank">📅 04:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">متأسفانه سروری که برای اسکن و بررسی کانفیگ‌ها استفاده می‌کردیم، به‌دلیل حجم بالای اسکن‌ها، از سمت ارائه‌دهنده به‌عنوان رفتار مشکوک یا سوءاستفاده شناسایی شده و دسترسی آن محدود شده است
😣
در حال بررسی و رفع مشکل هستیم و تلاش می‌کنیم سرویس اسکن را هرچه زودتر دوباره پایدار کنیم.
تا زمانی که این مشکل برطرف شود، می‌توانید از ساب‌های GitHub استفاده کنید؛ اما فعلاً امکان ارسال آپدیت‌های جدید از سمت ما وجود ندارد.
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/whitedns/923" target="_blank">📅 17:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تیم WhiteDNS از ابتدا با هدف کمک به کاربران فعالیت کرده و تمام خدماتی که ارائه داده‌ایم، رایگان بوده و رایگان باقی خواهد ماند.
در این مسیر سخت، تعدادی از شما عزیزان با کمک‌های مالی خود از ما حمایت کرده‌اید. چه کمک‌های کوچک و چه مبالغ بزرگ‌تر، برای ما بسیار ارزشمند بوده و واقعاً دلگرم‌کننده است. همین حمایت‌ها نشان می‌دهد که این مسیر برای خیلی‌ها مهم است و ما بابت این همراهی صمیمانه از شما سپاسگزاریم.
مبلغ کل حمایت از ما تاحالا حدود ۵۰دلار بوده است.
متأسفانه اخیراً کیف پولی که برای دریافت کمک‌ها استفاده می‌کردیم، شروع به مسدود کردن یا محدود کردن تراکنش‌های مربوط به ایران کرده است.
به همین دلیل، از شما خواهش می‌کنیم تا زمانی که راه‌حل امن و مناسبی پیدا کنیم، فعلاً برای ارسال کمک مالی اقدام نکنید.
قدردان محبت، اعتماد و حمایت ارزشمند شما هستیم.
با سپاس فراوان
تیم whiteDNS</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/921" target="_blank">📅 16:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔥
اگر محتوای WhiteDNS برای شما مفید بوده، با Subscribe کردن کانال یوتیوب ما می‌توانید از ادامه فعالیت‌های ما حمایت کنید
.
https://youtube.com/@whitedns</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/whitedns/920" target="_blank">📅 15:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-917">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/917" target="_blank">📅 11:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوستان نگران نباشید، ما ۱۰۰۰ تا دامنه خریدیم این مدت برای سرویس های DNSTT & MasterDNS
تا فردا هم فیلتر کنن
(
🖕
)
ما لینک ساب جدید میسازیم  براتون
لطفا این رو تست کنید و نتیجه رو در کامنت ها بگید. اگر فیلتر بود یکی دیگه میسازیم.
لینک ساب جدید
http://sub.iampedi1.live/sub/mihomo.yaml
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
نکته، تمام آدرس های قبل کار خواهند کرد. ساب گیتهاب و تمام این ساب ها و ساب های آینده یک محتوی خواهند داشت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/whitedns/916" target="_blank">📅 11:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">📌
چند نکته کاربردی برای بهتر وصل شدن با FlClash در اندروید
یکی از کاربران WhiteDNS تجربه‌ی شخصی خودش را از کار با FlClash فرستاده که برای اتصال بهتر مؤثر بوده.
اگر با FlClash مشکل اتصال، آپدیت نشدن ساب، پینگ‌های عجیب یا ناپایداری دارید، این موارد را امتحان کنید.
━━━━━━━━━━━━━━
1️⃣
بعد از نصب، قبل از اضافه کردن ساب، Resourceها را آپدیت کنید
بعد از نصب FlClash، قبل از اینکه لینک سابسکریپشن را اضافه کنید، وارد این بخش شوید:
Tools → Resource
و تمام Resourceها را آپدیت کنید.
⚠️
نکته مهم:
طبق تجربه‌ی بعضی کاربران، اگر اول لینک ساب را اضافه کنید، ممکن است بعداً Resourceها درست آپدیت نشوند یا اپ رفتار عجیب نشان بدهد.
━━━━━━━━━━━━━━
2️⃣
تنظیمات Network
از بخش Network این موارد را بررسی کنید:
✅
گزینه‌ی DNS Hijack را فعال کنید.
❌
گزینه‌ی
Allow applications to bypass VPN
را غیرفعال کنید.
این کار کمک می‌کند برنامه‌ها ترافیک یا DNS را از بیرون VPN رد نکنند.
━━━━━━━━━━━━━━
3️⃣
تنظیمات دسترسی و اجرای پس‌زمینه
بعد از نصب وارد این مسیر شوید:
Tools → Advanced Configuration → On Demand
در این بخش، گزینه‌های مربوط به دسترسی‌ها را روی Authorized قرار دهید.
همچنین در تنظیمات باتری گوشی، برای FlClash حالت Battery Optimization را غیرفعال کنید تا اندروید برنامه را در پس‌زمینه نبندد.
━━━━━━━━━━━━━━
4️⃣
گوشی روی Power Saving نباشد
اگر گوشی روی حالت
Power Saving / Battery
Saver باشد، ممکن است اتصال ناپایدار شود یا برنامه در پس‌زمینه قطع شود.
برای استفاده بهتر از FlClash، هنگام اتصال، حالت Power Saving را خاموش کنید.
━━━━━━━━━━━━━━
5️⃣
تنظیمات DNS
از بخش DNS:
✅
گزینه‌ی Override DNS را فعال کنید.
🌍
گزینه‌ی GeoIP Code را روی IR قرار دهید.
بعد از این تغییرات، لینک ساب را اضافه کنید و تست پینگ بگیرید.
━━━━━━━━━━━━━━
6️⃣
اگر ساب آپدیت نمی‌شود، حذف و دوباره اضافه کنید
طبق تجربه‌ی بعضی کاربران، FlClash گاهی نشان می‌دهد که ساب آپدیت شده، اما در عمل لیست کانفیگ‌ها تغییر نکرده است.
اگر حس کردید ساب درست آپدیت نشده:
1. لینک ساب را حذف کنید.
2. دوباره همان لینک را اضافه کنید.
3. مجدد پینگ بگیرید و تست اتصال انجام دهید.
━━━━━━━━━━━━━━
7️⃣
در تب Auto کمی صبر کنید
طبق تجربه‌ی کاربر، بعد از حذف و اضافه کردن دوباره‌ی ساب و گرفتن پینگ در تب Auto، ممکن است اول فقط چند سرور پینگ بدهند و بقیه Timeout شوند.
اما بعد از اولین اتصال، FlClash ممکن است خودش شروع کند سرورها را دوباره بررسی کند و از بالای لیست Auto دونه‌دونه سرورها را تست کند تا به گزینه‌ی بهتر برسد.
یعنی ممکن است اول یک سرور اصلاً پینگ ندهد یا در لیست بالا نباشد، اما بعد از اولین اتصال، همان سرور یا سرورهای دیگر دوباره تست شوند و وصل شوند.
⏳
گاهی این روند کمی زمان می‌برد، پس اگر همان لحظه همه‌چیز Timeout بود، چند دقیقه صبر کنید و دوباره وضعیت را بررسی کنید.
━━━━━━━━━━━━━━
8️⃣
مرتب‌سازی سرورها بر اساس پینگ
برای اینکه سرورهایی که پینگ گرفته‌اند بالای لیست بیایند، روی سه‌نقطه بزنید و وارد این مسیر شوید:
⋮ → Settings → Sort → Delay
با این کار، سرورهایی که پینگ بهتری دارند بالاتر نمایش داده می‌شوند و انتخاب سرور راحت‌تر می‌شود.
━━━━━━━━━━━━━━
✅
ترتیب پیشنهادی بعد از نصب FlClash
1. نصب FlClash
2. آپدیت Resourceها از بخش Tools → Resource
3. فعال کردن DNS Hijack
4. غیرفعال کردن Allow applications to bypass VPN
5. فعال کردن Override DNS
6. تنظیم GeoIP Code روی IR
7. غیرفعال کردن Battery Optimization برای FlClash
8. خاموش بودن Power Saving گوشی
9. اضافه کردن لینک ساب
10. رفتن به تب Auto و گرفتن پینگ
11. تنظیم Sort روی Delay
12. اتصال و چند دقیقه صبر برای تست خودکار سرورها
━━━━━━━━━━━━━━
⚠️
این تنظیمات تضمینی نیست، چون شرایط اینترنت، اپراتور و گوشی‌ها متفاوت است؛ اما برای بعضی کاربران باعث اتصال بهتر و پایدارتر شده است.
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/whitedns/915" target="_blank">📅 10:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69013b2789.mp4?token=SIoNfseat2RrA99pCzU0Bjfj4o4_WXye_T7ZJlnL42eqA-_J7xIwScGUSRyKlz7XMGIonlG6PtVqtpcUueQ2APk5-g1sMn__5Q6vFL65DFzoPLB8FicZ2RW21GNCyNWulnOuYmo-C4-R6eGXFpsdxK3wDn4AAqvMfuBBYk1_SiG24kwhiePVv8Co_g-WDRNUOG7034L3PYmIyiFf4hDVYC0ia9TqOx8jFA2tPxMgD7hlOX-a5jzxTfaYPFJOwDoxvgHkfc_FMr8eo21sVC_meHtWCCCXzLB6aaWPMVVtwDlSvpy25UobQwY2NTNmh15JITm8KK2uXLxDTsscRY31jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69013b2789.mp4?token=SIoNfseat2RrA99pCzU0Bjfj4o4_WXye_T7ZJlnL42eqA-_J7xIwScGUSRyKlz7XMGIonlG6PtVqtpcUueQ2APk5-g1sMn__5Q6vFL65DFzoPLB8FicZ2RW21GNCyNWulnOuYmo-C4-R6eGXFpsdxK3wDn4AAqvMfuBBYk1_SiG24kwhiePVv8Co_g-WDRNUOG7034L3PYmIyiFf4hDVYC0ia9TqOx8jFA2tPxMgD7hlOX-a5jzxTfaYPFJOwDoxvgHkfc_FMr8eo21sVC_meHtWCCCXzLB6aaWPMVVtwDlSvpy25UobQwY2NTNmh15JITm8KK2uXLxDTsscRY31jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو آموزشی فعال سازی Fragment در اپلیکیشن V2Ray در موبایل و دستکتاپ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/whitedns/911" target="_blank">📅 02:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سلام خدمت همگی،
دوستانی که از همراه اول یا سایر اپراتورها استفاده می‌کنند و اخیراً با مشکل اتصال مواجه شده‌اند،
بر اساس تست‌های انجام‌شده، به نظر می‌رسد در روزهای اخیر روی برخی اپراتورها، از جمله همراه اول، DPI سنگین‌تری نسبت به قبل اعمال شده است.
به همین دلیل پیشنهاد می‌کنیم اگر با اتصال مشکل دارید، گزینه
Fragment
را در تنظیمات اپلیکیشن‌های زیر فعال کنید:
V2Ray
FlClash
Clash Party
Mi Clash
گزینه Fragment می‌تواند در بعضی شرایط به عبور از DPI و بهتر شدن اتصال کمک کند، مخصوصاً زمانی که اتصال روی برخی اپراتورها سخت‌تر شده یا کانفیگ‌ها دیر وصل می‌شوند.
اما توجه داشته باشید که فعال‌کردن Fragment همیشه به معنی افزایش سرعت نیست. در بعضی موارد ممکن است باعث کندتر شدن اتصال اولیه، افزایش جزئی پینگ، کاهش سرعت در بعضی کانفیگ‌ها، ناپایدار شدن برخی سرورها یا مصرف پردازشی و باتری کمی بیشتر در موبایل شود.
بنابراین پیشنهاد ما این است:
اگر اتصال شما مشکل دارد، کانفیگ‌ها وصل نمی‌شوند یا اتصال ناپایدار است، Fragment را فعال کنید و تست بگیرید.
اما اگر اتصال شما بدون مشکل و پایدار کار می‌کند، الزامی به فعال‌کردن Fragment نیست.
به‌زودی آموزش ویدیویی فعال‌سازی Fragment برای هرکدام از این اپلیکیشن ها ارسال میکنیم.
ممنون
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/whitedns/910" target="_blank">📅 02:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اپلیکیشن‌هایی مثل FlClash و Clash Mi چطور کار می‌کنند؟
اپلیکیشن‌هایی مثل
FlClash
در اندروید و
Clash Mi
در آیفون، برنامه‌هایی هستند که به شما کمک می‌کنند راحت‌تر به کانفیگ‌های مختلف وصل شوید.
فرق اصلی این برنامه‌ها با بعضی از اپلیکیشن‌های دیگر این است که لازم نیست تعداد زیادی کانفیگ را یکی‌یکی وارد کنید و هر بار دستی تست کنید کدام وصل می‌شود.
شما فقط یک لینک سابسکریپشن وارد می‌کنید. بعد از آن، برنامه خودش لیست کانفیگ‌ها را دریافت می‌کند، آن‌ها را بررسی می‌کند و بر اساس تنظیمات، بهترین گزینه را برای اتصال انتخاب می‌کند.
مثلاً وقتی شما لینک سابسکریپشن WhiteDNS را داخل برنامه وارد می‌کنید، برنامه یک لیست از کانفیگ‌های آماده را دریافت می‌کند. سپس می‌تواند از بین آن‌ها، کانفیگی را انتخاب کند که در آن لحظه بهتر کار می‌کند.
آیا این برنامه‌ها هم‌زمان به چند سرور وصل می‌شوند؟
معمولاً نه.
این برنامه‌ها معمولاً برای هر اتصال، یک کانفیگ یا یک سرور را انتخاب می‌کنند. یعنی سرعت اینترنت شما با وصل شدن هم‌زمان به چند سرور مختلف ترکیب نمی‌شود.
اما برنامه می‌تواند چند کار مهم انجام دهد:
کانفیگ‌های مختلف را تست کند
کانفیگ خراب را کنار بگذارد
بین کانفیگ‌های سالم، گزینه بهتر را انتخاب کند
اگر یک کانفیگ قطع شد، سراغ گزینه بعدی برود
مسیر بعضی سایت‌ها و برنامه‌ها را از پراکسی عبور دهد و بعضی‌ها را مستقیم باز کند
برای همین استفاده از این برنامه‌ها معمولاً راحت‌تر از وارد کردن دستی تعداد زیادی کانفیگ است.
فرق FlClash و Clash Mi با برنامه‌هایی مثل V2Ray چیست؟
در برنامه‌هایی مثل V2Ray، معمولاً شما یک کانفیگ را وارد می‌کنید، همان را انتخاب می‌کنید و به همان وصل می‌شوید.
اما در برنامه‌هایی مثل FlClash و Clash Mi، شما معمولاً یک لیست کامل از کانفیگ‌ها را وارد می‌کنید. بعد برنامه می‌تواند بین آن‌ها انتخاب کند و بر اساس قوانین مختلف، ترافیک اینترنت شما را مدیریت کند.
به زبان ساده:
V2Ray یعنی: این کانفیگ را بگیر و به آن وصل شو.
FlClash و Clash Mi یعنی: این لیست کانفیگ‌ها را بگیر، تست کن، بهترین گزینه را انتخاب کن و اینترنت را هوشمندتر مدیریت کن.
حالت‌های Direct، Global و Rule یعنی چه؟
در این برنامه‌ها معمولاً چند حالت اتصال وجود دارد:
Direct
یعنی اینترنت بدون پراکسی و مستقیم از اینترنت معمولی شما رد می‌شود.
Global
یعنی تقریباً همه ترافیک اینترنت از یک کانفیگ یا سرور عبور می‌کند.
Rule
یعنی برنامه خودش بر اساس قوانین تصمیم می‌گیرد کدام سایت یا برنامه از پراکسی رد شود و کدام مستقیم باز شود.
برای بیشتر کاربران، حالت
Rule
بهترین گزینه است، چون برنامه هوشمندتر رفتار می‌کند.
چرا استفاده از سابسکریپشن بهتر است؟
وقتی از سابسکریپشن استفاده می‌کنید، دیگر لازم نیست هر بار چندین کانفیگ را دستی کپی و وارد کنید.
کافی است یک لینک وارد کنید و بعد از آن، برنامه خودش لیست جدید را دریافت می‌کند.
اگر لیست به‌روزرسانی شود، برنامه هم می‌تواند کانفیگ‌های جدیدتر را دریافت کند.
این یعنی استفاده راحت‌تر، مدیریت بهتر و دردسر کمتر برای کاربر.
خلاصه خیلی ساده
اپلیکیشن‌هایی مثل FlClash و Clash Mi برای این ساخته شده‌اند که کاربر مجبور نباشد بین ده‌ها یا صدها کانفیگ سردرگم شود.
شما یک لینک سابسکریپشن وارد می‌کنید، برنامه لیست کانفیگ‌ها را می‌گیرد، آن‌ها را مدیریت می‌کند و کمک می‌کند راحت‌تر به گزینه مناسب وصل شوید.
این برنامه‌ها معمولاً چند سرور را با هم ترکیب نمی‌کنند تا سرعت چند برابر شود، اما می‌توانند اتوماتیک و یا در حین اتصال کانفیگ‌های خراب را کنار بگذارند و اتصال پایدارتری ایجاد کنند</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/whitedns/909" target="_blank">📅 17:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه  https://github.com/iampedii/whitedns-sub   لینک ساب برای Clash Party & FLClash https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/whitedns/908" target="_blank">📅 17:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-907">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔥
اگر محتوای WhiteDNS برای شما مفید بوده، با Subscribe کردن کانال یوتیوب ما می‌توانید از ادامه فعالیت‌های ما حمایت کنید
.
https://youtube.com/@whitedns</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/whitedns/907" target="_blank">📅 14:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ما هر ۴۰ دقیقه ساب رو آپدیت میکنیم. شما هم یک آپدیت توی اپ بزنید تا بهترین کانفیگ هارو بگیرید.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/whitedns/905" target="_blank">📅 13:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه
https://github.com/iampedii/whitedns-sub
لینک ساب برای Clash Party & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
@WhiteDNS</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/whitedns/904" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/whitedns/903" target="_blank">📅 13:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-901">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">😊
آموزش استفاده از Clash Party نسخه ویندوز در کانال یوتیوب WhiteDNS
🔥
کانال مارو Subscribe داشته باشید.
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/whitedns/901" target="_blank">📅 12:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آموزش استفاده از FLClash
ممنون از رضا عزیز
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/whitedns/898" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚠️
برای وارد کردن ساب باید به یک وی‌پی‌ان  متصل باشید</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/whitedns/897" target="_blank">📅 10:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/whitedns/896" target="_blank">📅 10:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-893">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG_6D_2sDMXYjwtv1rz4pHX_LQUjkbkTTPGT5OJekBPjoAV-PkDr_5mF1sMb2-tpDb3_8YuuVoT82Ckz3PShkjnwln96oTeRA3fFICmht7QKZKoKBBLicI-CkLPIWdOjU_ZcKNtbe8KaPZMUBBLqnNVyAx5gpyuhfIouKbqx8wjmm3oIbF47l0IsS4xemOIzA9Jl9Q-QazQfrbS_3vAyhRzWbEY6yRwrGLdmQ8oZdveZJoWnLBpF88tNxrU_f_FcR8sgZykY5JTBsx_NiIJNhb3ttTb4DQEdC34Tbv5tiQvbwMX8P-ySwtyDxT4DJeiekyFRFKKHIfH8MnX-oo2wMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی
از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:
اندروید: FlClash
آیفون: Clash Mi
با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.
ما در سرورهای WhiteDNS بخشی از کانفیگ‌ها را بررسی و فیلتر می‌کنیم. سپس اپلیکیشن موبایل به‌صورت خودکار از بین کانفیگ‌های باقی‌مانده، بهترین گزینه‌ها را انتخاب کرده و به آن‌ها متصل می‌شود.
لینک WhiteDNS Sub برای استفاده در این اپلیکیشن‌ها:
http://sub.iampedi1.live/sub/mihomo.yaml
لیست سابسکریپشن ما هر ۱ ساعت یک‌بار به‌روزرسانی می‌شود.
دانلودFLClash برای اندروید، مک، لینوکس و ویندوز
https://flclash.cc/en/download
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/whitedns/893" target="_blank">📅 10:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89b2fd3cd.mp4?token=ePLx23M6Jfd0w9KUD_PxxA_7_4exHqg96SnxC22C2z4Kzru_lPQeuxP09bsplRHeKZs0INrzrYPO7KgSGAjgL__NzAndVzOZGHMQkb3aCJ2VN6t86rqS225Yvwy0uY9JcslL6ut7hQhZFWeTIhiXdNkEJ5Sr57ayLBuuCESGVabSCfE_PKA45usvCFIbsrr1tRt4ybaF0hn-l32zbmnsOoRzU0xoUKDPHUCPpt2DTOHUCErCGtVoGwZbd-ln0V54SmByY6oPECRg8VxNE0ABqr3rIcuN72a30KpjV1IRw7aOtTZY8WkWakP3Pur0LoqxyT1Qxn25sNeLBwlNFxOpVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89b2fd3cd.mp4?token=ePLx23M6Jfd0w9KUD_PxxA_7_4exHqg96SnxC22C2z4Kzru_lPQeuxP09bsplRHeKZs0INrzrYPO7KgSGAjgL__NzAndVzOZGHMQkb3aCJ2VN6t86rqS225Yvwy0uY9JcslL6ut7hQhZFWeTIhiXdNkEJ5Sr57ayLBuuCESGVabSCfE_PKA45usvCFIbsrr1tRt4ybaF0hn-l32zbmnsOoRzU0xoUKDPHUCPpt2DTOHUCErCGtVoGwZbd-ln0V54SmByY6oPECRg8VxNE0ABqr3rIcuN72a30KpjV1IRw7aOtTZY8WkWakP3Pur0LoqxyT1Qxn25sNeLBwlNFxOpVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همچنین کاربران نسخه دسکتاپ می‌توانند از قابلیت
تبدیل کانفیگ‌ها به IPهای سفید
به‌صورت مستقیم در داخل اپلیکیشن استفاده کنند.
🚀
Tools > V2Ray White IP Generator
@WhiteDNS
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/whitedns/885" target="_blank">📅 04:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSObDalX8u595XO-e37UIXiqY-mNIgEQEjfUCyjNY71pz1fMxR5JPBnh2i-DktSrE3KShavjWTYLJG-dTIpyueYYXJwZpTBrPgZcpNJg9s8litl-_rD2fvlzDLdicIDoDSRJScxqB-tHy8ADbi85w47hH28DoYudw1W6EreSRKl4idZlXKW-FcrAB5bqLiaI5f3i-V9FkXX3LCoeUeRXPunIahJTEDUEHzy7Lxhe6dGvKHhMvnSRyIFfN1TcswcORUalI0bi7tWogkKKjQqyUXI8t4skVAZigdFV6YFAKjFgmEveqQvdic3BmrpdNzTI-3JlSjtRgI589uOjs0o_LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش تبدیل کانفیگ به آی‌پی سفید
از این به بعد برای تبدیل کانفیگ، آی‌پی‌های خودتان استفاده می‌شود.
@WhiteDNS_Installer_bot
مراحل کار:
1. وارد ربات شوید.
2. روی گزینه «تبدیل کانفیگ با آی‌پی سفید» بزنید.
3. کانفیگ V2Ray خود را ارسال کنید.
فرمت‌های پشتیبانی‌شده:
VLESS
VMess
Trojan
بعد از تایید کانفیگ، ربات از شما لیست آی‌پی‌ها را می‌خواهد.
می‌توانید آی‌پی‌ها را به این شکل بفرستید:
8.8.8.8
104.18.1.1:8443
یا با کاما:
1.1.1.1, 8.8.8.8, 104.18.1.1:8443
نکته مهم:
اگر پورت وارد نکنید، پورت پیش‌فرض 443 استفاده می‌شود.
اگر آی‌پی را همراه پورت بفرستید، همان پورت استفاده می‌شود.
مثال:
1.1.1.1
→  پورت 443
1.1.1.1:2053
→  پورت 2053
در پایان، ربات فایل کانفیگ جدید را برای شما ارسال می‌کند که host و port آن با آی‌پی‌های ارسالی خودتان جایگزین شده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/whitedns/883" target="_blank">📅 03:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سلام خدمت همگی
❤️
الان تنها راه اتصال پایدار و بی‌دردسر اینه که شما یکبار اسکن کنید، آی‌پی مناسب پیدا کنید و بذارید جلوی کانفیگ‌هاتون.   متاسفانه فرمول یکسانی وجود نداره که برای همه کار کنه.   این روش رو میتونید برای کانفیگ‌های رایگانی که از ربات ما هم دریافت…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/whitedns/882" target="_blank">📅 02:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/whitedns/881" target="_blank">📅 02:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر:
https://t.me/MatinSenPaii/3598
پنل BPB روی گیتهاب:
https://github.com/bia-pain-bache/BPB-Worker-Panel
پروژه اسکنر روی گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت پنل BPB ورژن جدید
2- رفع مشکل پینگ -1 کانفیگ‌های آپدیت جدید و درست کردن تنظیمات کلودفلر برای کار کردن پنل
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Worker
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- توضیح حجم مصرفی و استفاده از این روش روی کلاینت‌های متفاوت
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/whitedns/880" target="_blank">📅 02:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNT-A8CBSOHY-V0YJ7ESi-8clMXfYS_grA1ymm46uzWmggIjaM5-M3SNrf7ZWoujxh3SO9-bcDrpQj5_c8SPfp8WsZPxEYRmqAQOsAZZtXwGXKy93ADkUxk7TE44-ey7DTDb8LI39ir7kLhzKqGtcNExiOUtoy8a9D-W8YnC7S_Ev2OIwaxyCbEzVRDCvXwqalEoWl2SFCJ5L1wk0LW76YIaa0z3KZ6Gw7YFFsXMX9aJza0vekiKC5xes_Z2HZI-zpbureDHYVdmnP44XS2K8AM31QQWhFtAEEYTbJza_-iXX1CvIfzZebt6ZFNESMjIqXvKKCdVS192AvrtzTGBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در شرایط سخت و روزهای «خاموشی دیجیتال»، تلاش کردیم با ساخت ابزارهای مختلف، آموزش‌های کاربردی و راهکارهای ساده‌، کنار مردم باشیم و کمک کنیم تا حداقل دسترسی آزاد به اینترنت حفظ شود.
اگر در تمام این مسیر فقط توانسته باشیم یک نفر را دوباره به اینترنت آزاد جهانی وصل کنیم، برای ما ارزشمند و افتخارآمیز است.
اولویت و هدف تیم WhiteDNS همیشه ساده‌تر کردن ابزارهای پیچیده و تسهیل در دسترسی به آموزش بوده تا به هموطنانمان کمک کند وابستگی به بازار سیاه، واسطه‌ها و مافیای VPN کمتر شود؛ با این نگاه که هر شخص قادر باشد ابزارها و اتصال‌های امن خود را بهتر شناخته، بسازد و مدیریت کند.
امیدواریم هرچه زودتر شرایط بهتر شود و حق اولیه و ساده‌ی دسترسی آزاد به اینترنت دوباره به همه‌ی مردم برگردد.
از تمام اعضای تیم WhiteDNS و تمام وطن‌دوستانی که در این روزهای سخت کنار مردمشان ایستادند، صمیمانه تشکر می‌کنیم.
دم همه‌تون گرم
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/whitedns/879" target="_blank">📅 15:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-878">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGNZevzRZqh9GExdLn0-6IFZD6ytnnWbPhIzboWboNw5Zw0PYdEhiTNyTJt5qcCSGth7xGcS4V5kq49wD5_7XDWKgtfrp2AUDbvQTbjwIda8oXbecp0Ic2mUjoG88OKpxhAZ8ae7ntbN7G_OJ_gfe2IiQ1dmQcqwK6kKNHFpxqZg5zQ4GNgy3OGFyWuk2thQa8Lvg47aRQjSoBoRWWgVOjVYj3HvWqXfUt8WYTigBktX6MIIMIpL6V862sOUsfEGtVh4a3vyjTWg1E2y2nG4CtftrHw0IDeC2T8BDpxpWpcI1nxTFTH13frYdf0gmVX9Qxm1YLOhS5N6L6XrPbFfvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
آموزش V2Ray از صفر تا صد | نصب پنل، ساخت Inbound و Cloudflare Clean IP روی سرور شخصی
در این ویدیو نحوه نصب و راه‌اندازی پنل V2Ray روی سرور را به صورت کامل آموزش می‌دهیم. همچنین با نحوه ایجاد Inbound، مدیریت کاربران، استفاده از IPهای تمیز Cloudflare و اتصال کانفیگ‌ها از طریق اپلیکیشن WhiteDNS آشنا خواهید شد.
سرفصل‌های آموزش:
✅
نصب و راه‌اندازی پنل V2Ray
✅
ایجاد و مدیریت Inboundها
✅
ساخت و مدیریت کاربران
✅
آشنایی با تنظیمات مهم پنل
✅
استفاده از IPهای تمیز Cloudflare
✅
آموزش پیدا کردن و تست Cloudflare Clean IP
✅
آموزش استفاده از اپلیکیشن WhiteDNS برای قرار دادن کانفیگ‌های V2Ray پشت IPهای Cloudflare
✅
افزایش پایداری و کیفیت اتصال با WhiteDNS
✅
تست و بررسی عملکرد کانکشن‌ها
✅
نکات امنیتی و بهینه‌سازی تنظیمات
😊
لینک تماشا در یوتیوب
https://www.youtube.com/watch?v=vVjqNQBUGIc&feature=youtu.be
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/whitedns/878" target="_blank">📅 11:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-877">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🤩
آمورش کامل استفاده از اپ WhiteDNS در نسخه کامپیوتر  - آموزش استفاده از کانفیگ های MasterDNS  / StormDNS و اسکن کردن - آموزش استفاده از V2Ray  - آموزش استافده از Scanner, Validator, White IP Generator
⭐️
دانلود از لینک داخلی  https://guardts.ir/f/6f56591f7b7a…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/whitedns/877" target="_blank">📅 10:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-875">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#موقت
ارسال شده در تاپیک سرور ها
سرور اهدایی از بامداد عزیز برای MasterDNS  قابل استفاده در  اپ WhiteDNS
🔑
Encryption Key
aaf4b6-@JavidnamanIran-aaf4b6fff
💻
Domains
: جداگانه امتحان کنید
b.bamak.xyz
b.igoii.org
b.namad.xyz
b.jnir.my
b.irdmc.com
b.javidnaman.com
Encryption Method
: XOR
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/whitedns/875" target="_blank">📅 04:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/whitedns/873" target="_blank">📅 02:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🤩
آمورش کامل استفاده از اپ WhiteDNS در نسخه کامپیوتر
- آموزش استفاده از کانفیگ های MasterDNS  / StormDNS و اسکن کردن
- آموزش استفاده از V2Ray
- آموزش استافده از Scanner, Validator, White IP Generator
⭐️
دانلود از لینک داخلی
https://guardts.ir/f/6f56591f7b7a
https://up.theazizi.ir/download.php?t=ecabdec17d6cbb16f37a13fe28c724cdb591
😊
مشاهده از یوتیوب
@WhiteDNS</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/whitedns/872" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔥</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/whitedns/870" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اگر در اجرای نسخه مک مشکل خوردید دستور زیر رو اجرا کنید
xattr -cr "/Applications/WhiteDNS Desktop.app"</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/whitedns/869" target="_blank">📅 12:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-linux-amd64.deb</div>
  <div class="tg-doc-extra">19 MB</div>
</div>
<a href="https://t.me/whitedns/865" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/whitedns/865" target="_blank">📅 11:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/whitedns/861" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/whitedns/861" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQHa6KikrP6HYrzWLUJaQFsYm5DGXBZfdpxSn2O7QH5W6FNA7V1WVGVJ48kuSUjdMs8mEZHXNZFACP9Z6Jr7HCw81RU1iaiFFw0BrGqS3VXP5c-Nw8ippK6SV5egUyX2Xi5lpwpcTcCknPRzSHOYZoCVohVjR6TzuG_j-Z7oCwdOao_47Q4Jq6BUEW-0-HIYzj7wfB958T40fnXj9_1KZz1Mq0Bae5_QtwgT4lQ-77XSg8OuVgjnBeKxT-5fewkQGf0pmdNthLknDcdmnTuF6WXEOD0TMBKAjoSpZmH8DhgXaW-firusOUGoCCW7CKhUWqCNcSon3YvwPtRFHn_pFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
انتشار نسخه v1.0.0-beta5 اپیلیکشن کامپیوتر WhiteDNS
⚪️
تغییر هسته از Sing-box به Xray
🔴
اضافه شدن امکان اسکن آی‌پی‌های شرکت‌های زیرساخت ایرانی. با این قابلیت، اگر رکوردهای A+، A یا B پیدا شوند، می‌توانید از آن آی‌پی‌ها به‌عنوان سرور برای کانفیگ‌های خودتان استفاده کنید. شما همچنین میتونید لیست خودتون رو برای اسکن وارد برنامه کنید.
⚪️
بازطراحی بخش کانکشن‌های V2Ray. این بخش حالا برای مدیریت تعداد زیادی کانفیگ مناسب‌تر شده است.
⚪️
اضافه شدن امکان Speed Test برای کانفیگ‌ها.
⚪️
اضافه شدن پشتیبانی از پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، Hysteria2، WireGuard، SOCKS و HTTP Proxy.
⚪️
اضافه شدن قابلیت سفیدسازی کانفیگ‌ها. ابزار جدیدی در بخش Tools اضافه شده که با وارد کردن کانفیگ V2Ray، آن را به کانفیگ‌هایی پشت آی‌پی‌های سفید سرویس‌های مختلف تبدیل می‌کند. همچنین می‌توانید لیست آی‌پی‌های سفید دلخواه خودتان را وارد کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/whitedns/860" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tc5ShOPb34aycLeNohWfT9LZrTvjUezKwKrvnoP_NajHO1tr9Ln_6b4zixTw5aHCxXURIVsQc8yfnumN5BIuK2UYh7fNDV-0htT2ZsF0qxKlfqLhoU6mZkQBSllYVWCewLV7ALMobfn8Z2u_RkLD40Oy8L0Ns5ZVci90wBqotWuWzvgPQzgdk_rWJtQ_xw7XFUBh2LBzBgFpa2SOMHB30OokxOcO5An65J0Y5GSNOxqr8ldKhz94NDTN_DpD-ZGnWDyplHov2czncEAFgzbfXPbmHy37X0X2zHUfLocvunLdMJCgj-Twbg_EyY67DxGadwwz8i6BlX3B3v8ocOi_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/whitedns/859" target="_blank">📅 04:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/whitedns/852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای ورژن‌ها
تغییرات و بهبود‌ها:
- رفع کامل LOSS% اشتباه روی شبکه‌های محدود و DPI (مشکل اصلی کاربران). حالا تایم‌اوت بین Dial، TLS و HTTP به‌درستی تقسیم می‌شه و پکت‌لاس فیک کاملاً برطرف شد.
- ذخیره خودکار IPهای سالم بعد از Quick Scan و کپی در کلیپ‌بورد با زدن دکمه C
- خروجی فقط شامل IPهای سالم (بدون IPهای مرده)
- فرمت txt حالا ساده: فقط یک IP در هر خط( از
https://t.me/MatinSenPaii/3543
برای بازنویسی کانفیگ استفاده کنید)
- پیش‌فرض‌های هوشمندتر برای شبکه‌های محدود (تایم‌اوت ۵ ثانیه، دانلود ۶۴KB)
- کاهش تخصیص حافظه و فشار GC
- حذف IPهای تکراری در اسکن
- اسکریپت نصب یک‌خطی (شامل آپدیت و Termux برای اندروید)
- بهینه‌سازی منو و تمیزکاری کد
ممنون از همه Contributorها:
ProArash
،
M-logique
،
Mralimoh
،
Hoot-Code
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/whitedns/852" target="_blank">📅 04:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">☠️
پروژه‌ی SenPai Scanner — اسکنر IPهای Cloudflare   چی کار می‌کنه؟   از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.  چطور اجرا می‌شه؟   فقط فایل مخصوص…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/851" target="_blank">📅 03:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-850">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nxCZh6-xamjzUSvqkvblata165-v_UtXHqpbymNINZY6xBEqBOYwlAr6qBX4Osv4csJaTBLQwr-UrqnQKr9Lo1QHBWX0xwwEpdo5kTbPfSUZFj6t5ysPM6ujyD8dMl_70GUBCtgpDliNqFU-cvb5J3Smz3nPaPaSwrLkqfk07W92rZ17i0XHCwM4TMfEcpLwu0DGRwy-vmUcp9QIO_iTkBgQd1GK4WVLUAIxzWoMpQDJmGs5hmVaLETECsOMwM1tGKLtub5MPpW9COgkn1HssCQY7z4mvCgOUwvYH86u0G7Ts0NKqw4yxEonxQdtmhRsHTd0RZk8Dab8aqh7uwKV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
پروژه‌ی
SenPai Scanner
— اسکنر IPهای Cloudflare
چی کار می‌کنه؟
از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.
چطور اجرا می‌شه؟
فقط فایل مخصوص سیستم عاملت رو دانلود کن و اجرا کن.
۴ حالت اصلی:
⚙️
Quick Scan
— سریع: تعداد IP، تعداد worker و timeout رو انتخاب می‌کنی و اسکن شروع می‌شه (پیش‌فرض: حالت HTTP + تست واقعی داده)
⚙️
Custom Scan
— کامل: تعداد IP، پورت، محدوده CIDR، فیلتر دیتاسنتر (مثل FRA)، حالت tcp/tls/http، خروجی CSV/JSON/TXT
⚙️
Test IPs
— لیست IPهای خودت رو از فایل
ips.txt
عمیق‌تر تست می‌کنه
⚙️
Discover Colos
— می‌فهمی از شبکه‌ات به کدوم دیتاسنترهای Cloudflare دسترسی داری
چی اندازه می‌گیره؟
- تأخیر (latency) و jitter
- درصد packet loss
- در حالت HTTP: تأیید Cloudflare + شناسایی colo (مثل FRA، AMS)
- یک نمونه دانلود کوچک — تا گول IPی که «وصل می‌شه ولی داده نمی‌ده» رو نخوریم
نکته مهم:
این یه ابزار
پروکسی نیست
— فقط IPهای خوب رو پیدا می‌کنه. تست نهایی هنوز با همون کانفیگ واقعی‌ات روی Xray/V2Ray هست.
---
🎄
پلتفرم‌ها:
Linux · macOS · Windows
🔗
لینک پروژه:
https://github.com/MatinSenPai/SenPaiScanner
دانلود فایل‌ها از گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner/releases
دانلود فایلها از تلگرام:
https://t.me/MatinSenPaii/3526</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/850" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyFfOAe-LXYYyVCbszmv1GF0V-1EWAdK-V-42K70qjQNfQAwCaaFTcI2oddMdMYPVqF91ef4T9OoUMgKFXOjheMFGGF214aGjjt3_sAd4A4QR23wW-JmM0nj6P4wLgPhPDJpSFfovnax-GRLFSeJrlMUVLYsCQ79hjbFSEpM8QOhIFfKyGAnoa0LACk__-Y7Ymg-bM2rV9Fxu9feVlwCT7ADczSG33_pW1mg2hQ-Bm7WUUq_dE3sxg1G5RCqMVq4dINVZvzddfYGGvdgYLLGbylEt1P7PnDq39712iaY1hHLkOkJqQpXWyjy-2VB6q35YemAuydOhEJRWPlxG4UnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/whitedns/848" target="_blank">📅 17:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.  @WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/whitedns/847" target="_blank">📅 14:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-841">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayNG_2.1.8-fdroid_universal (1).apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/whitedns/841" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آپدیت آخر V2rayNG fdroid
🔴
🔴
🔴
دوستان برای اتصال به کانفیگ های بات از این اپ استفاده کنید.
@WhiteDNS_Installer_Bot
@WhiteDNS</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/whitedns/841" target="_blank">📅 13:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/840" target="_blank">📅 13:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iTCd9P8vfNO2Jx0nI15qYsWN11GvwkLaldTzg8EKBEcVQWfjrB_V4dzMtA5toNNBeD8QWSV7uD7uk1qbV4_Kk6SsXosInikiFK0t-vz0nofqAhox5Bjw4d5tYf00LaFhk0ECgow4a9eSSsIt95qp_3HT-dETbJOfvPbtVDFxyDN64RjAKk43sxYRMKIhANCbk5XwQVStCqZoe-lwAik1e6xG0SViV0DFzhsIZStuQxGs-D8gNLVTGWxb3nHeoSx3q_5poWrIG9nzVzi7zOhSedOnLowFH-f11L09q_kwKTObFU0bwDlaSZWMMt5bgwSueeIILR0ePpINi8XKeom-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jWj9A4S5YS3po740R_bPzEL1q4Ix7H5OBjFbgqVKs5XYKNaXXcO7OU2Wj7QAaX_5eOwkySFo1Y5nGVzH9l6ld7qou_gAubUsMeHbW3kka0pnKmWjDygB8oriC1nNvtC8DI5yva-CPjVdh36Ru-Yb--lrFfkwa0M0WGn-2noTRjyj_IT1yAj4Jt7T7owgmipRUgJLqRIPBwMW1Q8PLzcqqZ2_OnePwZ8O7HBQPX9GkzDYM_xANqpKNXkwI4nDcexCd8n6kP4B1X_syZQ5UlS8G0wRrDmJ32FtSpQv2n9REkDMO5kcfeZ8vupsnuoYVg1BQ76DY7aBSqGCNFHTLXWcTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HT7qmhes0-ZXOg6aL_r0nfiPh4ofa_pQcXJ_fMnQalxGM0KAc6dl31y-Cr6j54BMSMyhdcHbTKIbCTsoYj1GMBD_Jy5dePuwNUvxcRttBTwMGUszox1tLk--3d6ikku0a_Ppxvd3yCLSxkl6TFzXpQP99RTBJ4QyplJ_OkmM1EWVtOsx_tTTdGjGjVrJWqw82t7X7XRCx14E6Gd0CHAGm76hpRAvf-AwX2em4effAzNCEFJBqvoVmZxwE4G1nrptKEkGWmyVWApGqbGiIXL7mef4ZQS_iTH0XhuFXYRbtRSYHLwpXKuPrP8OSBZah9DKLs0SKvjr_ZtVdTwq7UAzJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z6Vx0UEQG7u2Mb50V-lWSTAereKyUQj5jzD9LvY4b37h8gDAZFtaX8YCSSNk295hnVM9tad7w0OwfHjZiDjeg7Sd4sOAjLSWbndzQyn8QKLw3EiOoifVsW3biM7mrwzQ26PKxURZqTmWy89jkpnap4BsX00L73pjsXF9IJvHPh8TWNg1KLsDHGrYQZ3_oRrneLeBf3Ubh8RNy_dQy6OCstuZ-4-Atixv3VyBB-wFa_bxa9mGgcQ2mNXF6iJVlmGfqE2IKdloRwfjEwplVYWGt_LLt70Dgjh3iuP-sAGUk-eensJEjq4HbKMWITsTxxc6etKAPpYI53HXsNqABmRGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cFcjCcOyXLTsRc7st3gXm8fxla3XHMQbmfYC57MNPd-YTP0CX_djyTPFm651ECu1Lhn754XGrJTMmuXWhSL69a7whHfU-Gc0yY2KC7endWmbO5lGhLRzbGBGAg1Q1EbREETCz5iNSas4rRgf5c_X_nL8rENsAEk-JHFtei0DmawE4NEw968CoUelTSLKbWFyRkfe7nBuIIto4FXvKfCjf2e_M7xS7_NFvC1mDzeai0poW1QZ2vSug1QCDt5SS5ghlebr6hkEh98ryW3_4_MCkHM7TrXksHXIvV0-0eUTiQU3nNqSaNXTsJP-BcW3f61IjMebaPgA2pCJF-Dbdz5-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E6QhN-Z3w9-5EBpDsKG8_SpuxXAkCPsdDedC9LK9JGY1OgUrw8ogxG1bfSRwOd1qfAexiCIcN9-iHNlQQT7fu3GyY4Ud2_EdLqhdvzW5oid9rNpnyKjUhCePsHt6RIKqb3g__kZmVb4Tly-3YMeCMkmsabnMEqFEJftwfziPArJvC0K3UQzFIvCrmZwJrN9b6WEAHgGQBehVeQ8rVzhorjHWKpq33Ww9puyYEQf5qq9iYl0ZU6PaDfWzcMcMml6O2YmCroYp0pkIf6JTwd1ZhVB2zcGZwF4SeDISIE-rbrbH39v0q-PdP6sn-b87oeT73E8TdsgLM0EKD72orf9xnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DvlP4Lx6SQUrtD08lJqCU4o1MQQ7QcYWbgP-u1OJVkrQcW0xo4M3QWCp_ToVsJNFnbfx3ZmgFLIEHGHFoJyV1QRt6poJr5hUhrX8ayCDsR9WCTCOnsb-rrva4g9Tu74_B6QCjdnOVRsb6K1Sn6N8KFX5S-44-lsThxcXpT02yd3SKs35DXqJJ2YqGKxer-O3wA3AUkIrQPRAlHDu40pp5YeMHoWyqpo1W4vViUOI9lAd-OkyX36amYO7RtH2JrpzjKmm-whBA8GvBVy7uE5Yywf7hMn6abH-P6xQP6uud939XglMKCzGrQIqy-W-M492q0fWQXa17rtTkJHr5F_TaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S5CXQtL0zuRSAXNkfG7rkaN0odq6uADSQx3GmejujtqNVBCMjEo-ylrOjSNLeTiD4ijW0SXg4n7sMtY_ImJ389cDEYS0GbqR-H7d1v6ndY7rniYPFzxqDCc-p5xGF-I7g8TKOxH4mQCFCV2H3Ib8ZpSEhaJXF8ujwrNvnWQzRPxNumA9HgWdmEtbMsj7RmgQ2gR91Wbc3h-mlIdQ39vsQ2AhInwsnTu2dU2IM3nDdtYqfEBKnXczDUmuOoQncjFEPV-0zFAd2MawtfI1GwvTTRKO9fMTCHnqJzOEsl_SiWOXkZPCvER4hgRX7pjfMDuUCjKdo6Po13k0ILzlkdYIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WlFCOSheqhcVJGPB-lRAERD3hammpP5S4Ssaz9b1a53DL9qeLPVtRxNrMAen6AJJQyn1Zitq8g9DQGSt_tZwvp4GmtERWQvjHWgyfI9poOSNYbsp4-L-KnSjeShKm3SFR9F-pLhS6IiBpvrHbByBUmIHzA0bGHQPvUzY3axTHkeRP0eOzcYAdxyDgrN-ZdhduTvo286mii8mCACChsJy43HxC6FZJgF4CDxBMWqaDlhTYRJwpDjPzd9LZdUMO68-37-Tp1vcLS5hoU2lkKMpEzTnyboQCDax6eHc3ZAFJpetKhs3-1C0j-tfj1OeK6lrrBhz--Be5PhqfXFyr-0iWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.  @WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر…</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/whitedns/831" target="_blank">📅 13:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0h7PDiAjxCN-4LTnFhSnZQKT7UL6CCzpWJmJd6ZWM3VRbxVEuWewVyN5FsSeZrmwcOyR9vhqlgs95uuBPBryv29RPhf0AgkCMPuyXrkxWAmoXmigPNJaHl6MvWMNkkcXleUgJ2xUySEp6qKCLn7a-pOqpVrzJ-6p4L5JHqM8jf7CKBr-hnwd490rTtwY6lZmoeS1WyjIAENDJBtrHU1SBX12KRaUnbeT33b0iFRzAAtmPKNErFunrLFXNcMwve2yFyDhp1TnbqaZgFr1lQexZrbe4nZv-U-pN3s4AnlmzpVfLtA8zPUJVJ6pZ5nEgRzkv_ejK5uQ7t9bwm1DOyFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/whitedns/830" target="_blank">📅 12:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-824">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4  با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.  در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/whitedns/824" target="_blank">📅 12:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-820">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta4-linux-arm64.rpm</div>
  <div class="tg-doc-extra">24.8 MB</div>
</div>
<a href="https://t.me/whitedns/820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4  با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.  در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/whitedns/820" target="_blank">📅 12:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-818">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/818" target="_blank">📅 11:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-817">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دوستانی که از نسخه اندروید اپ WhiteDNS  استفاده میکنند.
برای بیشتر کردن سرعت و پایداری
، میتونید با وارد شدن به بخش ریزالور ها، یک پروفایل جدید با مقادیر زیر بسازید
1.1.1.1
1.0.0.1
8.8.8.8
8.8.4.4
9.9.9.9
149.112.112.112
208.67.222.222
208.67.220.220
94.140.14.14
94.140.15.15
برای کم کردن مصرف
، سپس وارد بخش تنظیمات و پیشرفته بشید و‌مقادیر زیر رو تغییر بدید.
Upload Dup = 1
Download Dup = 2
اگر سرعت شما قابل قبول نبود، دوباره مقادیر Dup رو بالا ببرید.
توجه کنید که این مقادیر فقط مناسب اینترنت پایدار هستش. در صورت بازگشت اینترنت به وضعیت قبلی، باید کانفیگ های متفاوتی اعمال کرد.
ممنون
تیم White DNS</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/whitedns/817" target="_blank">📅 11:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آموزش اتصال V2Ray در نسخه کامپیوتر
دریافت لیست کانفیگ ها برای ایمپورت کردن
https://t.me/whitedns/804
https://t.me/whitedns/805</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/whitedns/816" target="_blank">📅 11:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta4-release-windows-x64.zip</div>
  <div class="tg-doc-extra">23.8 MB</div>
</div>
<a href="https://t.me/whitedns/812" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/whitedns/812" target="_blank">📅 11:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJb7RTwOnvo21GwGyzrAP2SuzcexAPx6fUT0r3_3w_LcyBf_5YiJZjr73GnW-oigFClS40VqEbCgeaxYQU4f5vIxeMi7KF6hiHqqqi3zqbQ0rdfBGvpNbinazFPHRWDIS6Iat59YgO4ZcAGbUzcwvCLwk-qzvBONE4APbwYDt4A4NxYYprnB_s83FcsCCjWtOOrHne-0X3atjlhNXdzzjIQTLOr4TF1Ll1kDjM33IFUM0ozKnwn7T_HATXAs3ZYZL38Zj26EMXe4sIbat2yKrNIDLAsStOHXT2qGjNw8d8z8GTh_VdvGJHszFrVDwoTXxLKMgRWRdy4UXY11RNGiuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4
با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.
در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription اضافه شده، و ابزارهای داخلی برای مسیر‌دهی هوشمند، مسدود کردن تبلیغات و عبور مستقیم ترافیک سایت‌های ایرانی از شبکه داخلی فراهم شده است.
اتصال MasterDNS هم پایدارتر و کم‌مصرف‌تر شده؛ درخواست‌های تکراری حذف شده‌اند و مصرف اینترنت حالا تقریباً شبیه یک VPN معمولی است.
✅
پشتیبانی از V2Ray اضافه شده است.
✅
پشتیبانی از VLESS، VMess و Trojan اضافه شده است.
✅
امکان وارد کردن کانفیگ و Subscription اضافه شده است.
✅
آدرس‌های خصوصی و داخلی مستقیم وصل می‌شوند و از مسیر V2Ray عبور نمی‌کنند.
✅
سایت‌ها و آی‌پی‌های ایرانی با geosite-ir و geoip-ir مستقیم از شبکه داخلی عبور می‌کنند.
✅
تبلیغات، بدافزارها، فیشینگ و ماینرها مسدود می‌شوند.
✅
همه ترافیک‌های دیگر از پروکسی V2Ray انتخاب‌شده عبور می‌کنند.
✅
کش داخلی sing-box برای لیست‌های قوانین آنلاین فعال شده است.
✅
MasterDNS پایدارتر و کم‌مصرف‌تر شده است.
✅
درخواست‌های تکراری حذف شده‌اند و مصرف اینترنت تقریباً شبیه یک VPN معمولی شده است.
✅
سرعت اتصال بهتر شده و Packet Loss کمتر شده است.
✅
ریزولورها به گزینه‌های بین‌المللی و قابل اعتماد مثل
1.1.1.1
و
8.8.8.8
تغییر کرده‌اند.
✅
حالت تاریک، Scanner جدید، بکاپ کامل و رفع باگ‌های زیاد هم اضافه شده‌اند.
@WhiteDNS</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/whitedns/811" target="_blank">📅 11:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-810">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">Defyx VPN
🚀
یک اپلیکیشن VPN مدرن، هوشمند و متن‌باز که با Flutter ساخته شده و با تمرکز بر امنیت، حفظ حریم خصوصی و تجربه کاربری جدید، دسترسی آزاد و رایگان به اینترنت را فراهم می‌کند.
🌐
🔓
🔹
متن‌باز و قابل بررسی
📜
🔹
رابط کاربری مدرن و روان
💻
🔹
تمرکز بر حریم خصوصی و امنیت
🔒
🔹
مناسب برای دور زدن محدودیت‌های اینترنت
🕸
بروزرسانی جدید
⬇️
GitHub:
https://github.com/UnboundTechCo/defyxVPN
📂
@whitedns</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/whitedns/810" target="_blank">📅 10:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-809">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">Orbot for Android v17.9.4 BETA 2 (tor
0.9.4.8
)
بروزرسانی جدید
Orbot 17.9.4 (2.7.0) برای اندروید منتشر شد
📲
این بروزرسانی، موتور Tor را ارتقا داده، روش‌های اتصال جدید اضافه کرده و چند مشکل اتصال را برطرف می‌کند
🔒
🔧
.
✨
تغییرات مهم:
• ارتقا به Tor
0.4.9.8
برای پایداری و عملکرد بهتر
🚀
• اضافه شدن پشتیبانی از Shadowsocks داخل خود Orbot
🌐
• امکان استفاده همزمان با پل‌های obfs4 ،Meek و WebTunnel
🌉
• گزینه جدید «بدون پروکسی» برای خاموش کردن سریع پروکسی بدون حذف تنظیمات
⚙️
• بروزرسانی پل‌ها و ابزارهای دور زدن فیلترینگ
🛡
• بهبود DNSTT برای اتصال بهتر در اینترنت‌های محدودشده
📡
• رفع چند باگ و مشکل اتصال
🐛
📱
مناسب برای افرادی که از Tor برای دسترسی آزادتر و امن‌تر به اینترنت استفاده می‌کنند
🔐
🌍
.
دانلود
📥
https://github.com/guardianproject/orbot-android/releases/tag/17.9.4-BETA-2-tor-0.4.9.8
@whitedns</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/whitedns/809" target="_blank">📅 10:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دوستان سلام :
این یک مدت به همه سخت گذشت ، شاید شما اسم دو نفر را بیشتر شنیدید ولی بدونید یک تیم ۳۰ نفره بی نام و نشان پشت این کار بودند  توی بدترین شرایط از همه چیز زدند تا شاید یک روزنه کوچکی باز بمونه ،
ببخشید کم بود ، کافی نبود ،ولی در حد وسع خودمون تلاشمون را کردیم
یک تعداد زیادی از  دوستان پیام دادن ، تشکر کردند و گفتن ادامه بدیم ، خواهش کردند بمونیم
ما هستیم کنارتون ، مگه میشه این همه عشق و محبت را رها کرد
یکم استراحت کنیم ،همه با قدرت بر میگردیم
توی این مدت مراقب خودتون باشید
تیم whitedns
@whitedns</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/whitedns/808" target="_blank">📅 02:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-807">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bH07GU-Gb3Vav-APLlHqAloMuo4F6kxMapuIF4C4nAe2WpQIPRnejsoWdftsZ8sELhSc_-xelfBT-3Nf54r8Zv-tJz5ImSwz_gIG-RgQ2rcfoMrS40G11vAbZxVBFMHTASk70l2HuvZ0KZIW3LE9vp0aCBX6hgS-41sv5Bm7W3haL9I92lK8V-9PyMWp8KSKEhms1lNrHkXfTdrQ4nCtJAbzwL0JruUQhKjrFtufd6cxGwx-8-fF5Xi1PTCk3TBwjo7mcgmRMn2eUkOUqeQNXaoKiesTUj9g9Qr4TFS3mlSbZKvU17_GU1tcPglNTNhPuR-ym20ucs4SAvf-lUt1Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#موقت
یادمون نره کسانی که از ظلم پول در آوردند.</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/whitedns/807" target="_blank">📅 19:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-806">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">برای استفاده از کانفیگ های بالا میتونید از اپ v2ray یا دیگر اپ های مشابه استفاده کنید
👆
👆
👆
اپ های قابل استفاده:
npv tunnel
happ
nekobox
MahsaNG
v2raytun
v2box
V2rayN</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/whitedns/806" target="_blank">📅 19:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-805">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayconfigs_with_WhiteDNS_2.txt</div>
  <div class="tg-doc-extra">30.2 KB</div>
</div>
<a href="https://t.me/whitedns/805" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">115 کانفیگ تست شده دیگه پینگ 100-200
ممنون ازعلی عزیز برای تست و پاکسازی لیست
@WhiteDNS</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/whitedns/805" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-804">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2ray_configs_WhiteDNS.txt</div>
  <div class="tg-doc-extra">38.3 KB</div>
</div>
<a href="https://t.me/whitedns/804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">141 کانفیگ تست شده روی مخابرات پینگ 100-200
ممنون ازعلی عزیز برای تست و پاکسازی لیست
@WhiteDNS</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/whitedns/804" target="_blank">📅 18:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-802">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXFW-gByoh6SwtJ6qJ9MaKgJYEsMHOehkMmosM1en-_2jwHWxhE1iOG5xgBHzHSGSffPlhFDaO2lD8dh61SIzv_i_QbpDEQz-NwSKRaIbwVICb3aZAhtKCpe1yso8kx_f5YC9VHzrx47BIJsLa9_rMO0G-EXEnSnzFR3jUWzq9TsFZ9azOzJ7jUKby_GXv4N8bze4Saz3pQwK8eENB8oRSMC992LGHwLbASDH-3HQKjJfWJ2gHA286LhI81CrLp-i2UU2ggeHMGntlERUysemyrvvJ1rixVV7aS5u1xF_6pAH3dCyxR6TESo_4AOt3LQGIWUzU7h9cg1l2FHk4DWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qd4TXQtg5QqILoWkEkbGY5efdj-d1HW7GeMeundGOLYwkDKZuH7u2JyJa4swLo-of5xrwqXsmywvasWojrFxGrZZTff68hohpzPrv2Soqtw9j3RRfVQbRO-n8MLLee3hX6COvI4IP6MiUivC1_HhIO2zLo_1xkwdtBT-M3YiB5FwkHYFFZSGwroaTsSSQuQI39SbFDTY0eEg7vyCOgeJSFAVNWFaZYJmjNblQShhpU-gsTmNzVQqmrUvOCRYM2xEhKpT-Z32h6i_5wYnJ1RjaxHoZeoaTCYDEQiGS7hFAkoqERlqApLcfVSk2RMtGfsJwbJruPk16b_wO8VNEdOrHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این هم یک تست سرعت با ریزالور های درست و با اختلال کمتر
🤌</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/whitedns/802" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-801">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">“}
سلام خدمت همه عزیزان
❤️
امیدواریم این روند ادامه‌دار باشه و اینترنت به‌زودی برای همه اپراتورها به حالت پایدار برگرده.
برای دوستانی که فعلاً به سرویس‌های دیگه دسترسی ندارن، می‌تونید از ریزالورهای زیر استفاده کنید:
1.1.1.1
8.8.8.8
همچنین بهتره مقدار
Duplicate
رو کمتر کنید تا مصرف اینترنت پایین‌تر بیاد و اتصال داخل اپ پایدارتر بمونه.
حتی در صورت برگشت کامل اینترنت، سرورهای WhiteDNS همچنان فعال می‌مونن و می‌تونید ازشون استفاده کنید.
یادمون نره، مارو از کمترین حقوق شهروندی محروم‌کرده بودند. فراموش نمیکنیم.
دم همگی گرم بابت همراهی و صبوری‌تون
🔥
@WhiteDNS</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/whitedns/801" target="_blank">📅 17:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-800">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">در طول ۳ روز گذشته، کاربر های ما ۱۰۰۰ سرور جدید اختصاصی با ربات WhiteDNS ساختن
🎉
@WhiteDNS_installer_bot</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/whitedns/800" target="_blank">📅 09:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-799">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دوستان گرامی :
ما هیچ گروه و کانال دیگری در هیچ پیام رسان خارجی و  داخلی نداریم
تنها گروه رسمی ما :
https://t.me/whitedns_group
تیم whitedns
@whitedns</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/whitedns/799" target="_blank">📅 03:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-797">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrrX-bsH1UpQ1mWBE9MObCjGXpR7JdZKKV8j2lrjcHyaMb_giLJeYAmFuPVTGCgUKpagYV0EFKPoCacegMbuHFF6MKoS91Wf-dXFDSqVPBqjV94BET1B3rFxfhc2E5VRr5GP_WRS2OIW8ZuwibijF6cfP-Yjq5kjr-U4-y4Is3H5-6EgIwV13vOQl_A9wXqEspvKUQti8tqFOZv2L-onjv5TnPf19PCjJlblpdpLM1vG2wAYOxstjs9jvE2XUW03aNufaLi0cGybZzBP6fo9R--OVuac_ap4gnZyK0nth2MHQL2sL49cWjn7Yd161ErwXdK0ANLCqNYbv1OUJ7nDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کیه این تک دلقکو همیشه میزنه
😂
؟
به افتخارش نفری یدونه بزنید ببینه دلقک کیه
🤡</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/whitedns/797" target="_blank">📅 16:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-796">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=lbckux_kNVdHzQJrRTuWyvWlcUzisTus8ph_d3wafB4m2jSKczV0PyKiij2OcrxQ5WkphyD4zgfNtfnW9PbPUgNdSmsIRLLI79JlVyIGBMJr_AXSbz1TX0-JVB-mXorQkF3W3sg4-QD5j8sx2XzdH4z9wywJMxPFtLkamuKOvrURm_dIiBxw_Rs9F5kq8dTb7UC5iylYgmfmPhUDzJG6ngjawf0W-KyHCtP7BZy-tr3dMBkE9sFTTotC-qiyJfoqvSwmMNN_TRmgOg43tQEoCL7_PrOkiYgRfOGlWW0Fjz-0EvNp0wNjgp1KRtm7q1Pg4NJHtdgHBz4zn5VZhinOG28BoEeNGZxSDkX7pmAv3A6luQO_7KdRzkLrgOYUhA7aWpL25YeHVY9hGY5x6-VMd7ExV11DKoi6PPT3hy_Y_XrgaHMK7ZtLwO9XBcEFTu8twF5aSx_MhrF7IJdEgFZWsEKaillKR5MgsceBuEoK3PPs8Bi7HqFBDcnwKlkVAyQDCYoh-A2xtNpkF-wzdX8EWa6SNK7xEsv2eqfjN4wzI3-mlR3cQ7psOrRZdrKwl6ZFJb-Z8e3UWpZJfI-kPAbl0M8BDla6MeJyfVe9GyXs6QATYAxu7gfjxdHisbqUDpYn1KUrcABQC5koXN0DfVXp3Of83HULOpuLbCZsg8Lkhho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=lbckux_kNVdHzQJrRTuWyvWlcUzisTus8ph_d3wafB4m2jSKczV0PyKiij2OcrxQ5WkphyD4zgfNtfnW9PbPUgNdSmsIRLLI79JlVyIGBMJr_AXSbz1TX0-JVB-mXorQkF3W3sg4-QD5j8sx2XzdH4z9wywJMxPFtLkamuKOvrURm_dIiBxw_Rs9F5kq8dTb7UC5iylYgmfmPhUDzJG6ngjawf0W-KyHCtP7BZy-tr3dMBkE9sFTTotC-qiyJfoqvSwmMNN_TRmgOg43tQEoCL7_PrOkiYgRfOGlWW0Fjz-0EvNp0wNjgp1KRtm7q1Pg4NJHtdgHBz4zn5VZhinOG28BoEeNGZxSDkX7pmAv3A6luQO_7KdRzkLrgOYUhA7aWpL25YeHVY9hGY5x6-VMd7ExV11DKoi6PPT3hy_Y_XrgaHMK7ZtLwO9XBcEFTu8twF5aSx_MhrF7IJdEgFZWsEKaillKR5MgsceBuEoK3PPs8Bi7HqFBDcnwKlkVAyQDCYoh-A2xtNpkF-wzdX8EWa6SNK7xEsv2eqfjN4wzI3-mlR3cQ7psOrRZdrKwl6ZFJb-Z8e3UWpZJfI-kPAbl0M8BDla6MeJyfVe9GyXs6QATYAxu7gfjxdHisbqUDpYn1KUrcABQC5koXN0DfVXp3Of83HULOpuLbCZsg8Lkhho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با بخش TeleMirror
✅
رفع مشکلات رایج کاربران
✅
نکات مهم برای استفاده بهتر از برنامه
دفید یک سیستم مبتنی بر DNS است که امکان دسترسی به محتوای کانال‌های تلگرام را حتی در شرایط محدودیت اینترنت فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصب:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
توضیحات متنی
👇
سلام. توی این ویدیو می‌خوام خیلی ساده و سریع نحوه کار با برنامه The Feed رو توضیح بدم.
بعد از نصب و باز کردن برنامه، اولین کاری که باید انجام بدید اضافه کردن یک کانفیگه. برای این کار از بالا روی علامت جمع بزنید و کانفیگ مورد نظرتون رو وارد کنید. کانفیگ‌های عمومی داخل کانال
@thefeedconfig
منتشر میشن و می‌تونید از اونجا دریافتشون کنید.
هر کانفیگ دارای تعدادی ریزالور پیش فرض هست که توسط سازنده کانفیگ داخل کانفیگ قرار میگیرن. بعد از اینکه کانفیگ رو اضافه کردید، برنامه شروع می‌کنه به بررسی ریزالورها. ریزالورها همون DNS هایی هستن که The Feed از طریق اون‌ها اطلاعات رو دریافت می‌کنه. این مرحله ممکنه چند دقیقه طول بکشه، پس اگر بلافاصله کانال‌ها نمایش داده نشدن نگران نباشید. بعد از پیدا شدن ریزالورهای سالم، لیست کانال‌ها دریافت میشه و می‌تونید وارد هر کانال بشید، پست‌ها رو ببینید و در صورت وجود، عکس‌ها، فایل‌ها، ویس‌ها و ویدیوها رو دانلود کنید.
اگر یه زمانی دیدید برنامه کند شده یا اطلاعات جدید دریافت نمی‌کنه، معمولاً مشکل از ریزالورهاست. برای همین داخل برنامه بخشی به اسم «پیدا کردن ریزالور» وجود داره. وارد این قسمت بشید و روی «بارگذاری لیست پیش‌فرض» بزنید. با این کار حدود ۵۸ هزار ریزالور برای اسکن آماده میشن.
اگه خودتون ریزالور خاصی دارید، می‌تونید به صورت دستی هم واردش کنید. علاوه بر این، ربات
@dns_resolvers_bot
هم می‌تونه برای پیدا کردن ریزالورهای جدید بهتون کمک کنه.
بعد دکمه «شروع اسکن» رو بزنید تا برنامه ریزالورهای سالمی که روی اینترنت شما کار می‌کنن رو پیدا کنه. وقتی چند تا ریزالور پیدا شد، می‌تونید اون‌ها رو به لیست فعال اضافه کنید. فقط یادتون باشه موقع اسکن بهتره VPN خاموش باشه تا نتیجه دقیق‌تری بگیرید.
داخل برنامه یه بخش دیگه هم به اسم Tele Mirror وجود داره. این قسمت با سیستم اصلی TheFeed فرق داره و برای نمایش کانال‌های عمومی تلگرام از سرویس‌های گوگل استفاده می‌کنه. با TeleMirror می‌تونید خیلی از کانال‌های عمومی دلخواهتون رو دنبال کنید، ولی محدودیت‌هایی هم داره؛ مثلاً امکان دانلود فایل یا پخش ویدیو توی این بخش وجود نداره. همچنین اگر سرویس‌های گوگل در دسترس نباشن، ممکنه Tele Mirror کار نکنه. البته این موضوع روی بخش اصلی TheFeed تأثیری نداره و سیستم اصلی برنامه همچنان از طریق DNS به کار خودش ادامه میده.
در نهایت اگر جایی به مشکل خوردید، اولین چیزی که باید بررسی کنید ریزالورها هستن. در اکثر مواقع با پیدا کردن چند ریزالور سالم، مشکل برنامه برطرف میشه. برای دریافت آخرین اخبار پروژه هم می‌تونید کانال
@networkti
رو دنبال کنید، فایل‌های نصب رو از
@thefeedfile
بگیرید و کانفیگ‌های عمومی رو از
@thefeedconfig
دریافت کنید.
ممنون که این ویدیو رو دیدید و امیدوارم از The Feed لذت ببرید.</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/whitedns/796" target="_blank">📅 11:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-795">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhNI51BLDMd9mSZO56rXW-9hCPJGpW8yBrp5IubjyAZTNkVvwQ6RDJRLPgjz_j7kbwjPZvVJ_VMROKgNCN6rgUpuZ1wmUiZdcfYWWV4NnJSfq1Qzp0zBAoTa04pWPopWgyavU1qkYxnnRVSJs9sAJzhGGzjxkIMkjlSYNOqVDa2TYyLt5ZKsnvfTUtgHyYmfNneX0qLkMXu2aR3geLTWpgQfe1-f2IVDQYunPdzqmrdIn4PAblbWVQDMCLUhTy-tI_NsvUj1Y0IeJPGSH8TU-8KkfnvlNqGh1LbaqvM89u8zssv2Q85lm2FWDK9SJE1ZuJbnuiF-9gA6OSkz8TCveA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حال حاضر مشغول تست نسخه جدید اپلیکیشن دسکتاپ WhiteDNS هستیم.
در این نسخه، علاوه بر اضافه شدن حالت دارک مود، تغییرات مهمی در عملکرد داخلی برنامه اعمال شده است.
یکی از تغییرات اصلی این نسخه، تغییر کلاینت داخلی اپ از StormDNS به MasterDNS است.
این تغییر به این معنی نیست که سرورهای StormDNS دیگر قابل استفاده نیستند یا وصل نمی‌شوند. سرورهای StormDNS همچنان قابل استفاده هستند.
اما تنظیمات داخلی برنامه در این نسخه بر اساس آخرین نسخه MasterDNS ساخته شده و در تست‌های اولیه، از نظر سرعت، پایداری و مصرف حجم، عملکرد بهتری نسبت به نسخه‌های قبلی نشان داده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/whitedns/795" target="_blank">📅 09:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-793">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">White DNS
pinned «
دوستان گزارش دادن که Hostinger پولشون رو بلوکه کرده و پشتیبانی جواب نمیده و... ترجیحا نخرید. نکته اینکه شما با دامنه .ir هم میتونید انجام بدید این متد رو اما خب توصیه نمیکنم به شخصه علتش هم واضحه. جای مطمئنی برای دامنه دیدم معرفی میکنم
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/793" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-792">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان گزارش دادن که Hostinger پولشون رو بلوکه کرده و پشتیبانی جواب نمیده و...
ترجیحا نخرید.
نکته اینکه شما با دامنه .ir هم میتونید انجام بدید این متد رو اما خب توصیه نمیکنم به شخصه علتش هم واضحه.
جای مطمئنی برای دامنه دیدم معرفی میکنم</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/whitedns/792" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-791">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سلام خدمت همه همراهان عزیز  ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.   تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.   من پیشنهاد میکنم برای راحتی کار شما، بعد…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/whitedns/791" target="_blank">📅 16:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-789">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">💥
موقت
🚫
دوستان :
اگر سروری دارید از جایی  میگیرید که پورت ۲۲ نمیده اصلا خرید نکنید
ظاهراً یک عده دوباره دارند سر مردم کلاه میگذارند
داستان داریم به خدا
لطفا اگر توی گروه های ما کسی داره کلاهبرداری میکنه با ذکر ID گزارش کنید
@WhisperInHeaven
🚫</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/whitedns/789" target="_blank">📅 12:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-787">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سلام خدمت همه همراهان عزیز
ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.
تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.
من پیشنهاد میکنم برای راحتی کار شما، بعد از خرید دامنه و اتصال DNS از ربات
@WhiteDNS_installer_bot
استفاده کنید.
اگر از این‌ ربات استفاده کنید، فقط با پروکسی کردن تلگرام‌ میتونید سرور خودتون رو مدیریت کنید و در شرایط بحرانی فقط از طریق تلگرام همه چیز رو مدیریت بکنید.
ممنون
@WhiteDNS</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/whitedns/787" target="_blank">📅 05:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-786">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو:
https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو:
https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- خرید دامنه و سرور ارزان با کریپتو(+آموزش)
2- تانل کردن ترمینال با Proxifier و ssh زدن با خود ترمینال
3- تنظیم دامنه در کلودفلر و راه‌اندازی ساده‌ی سرور MasterDNS
4- استفاده از سرور MasterDNS در کلاینت های ویندوز و اندروید WhiteDNS
5- توضیح استفاده از Parallel Testing در WhiteDNS
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز به خریداری یک عدد سرور لینوکسی و دامنه داره(مجموعا 5 دلار نزدیک به 800 هزار تومان) کافی برای اتصال نزدیک به 5 نفر
کانال مستر دی ان اس:
1-
https://t.me/masterdnsvpn
گروهشون:
2-
https://t.me/MasterDnsVPNGroup
کانال وایت دی ان اس:
1-
https://t.me/whitedns
گروهشون:
2-
https://t.me/whitedns_group
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/whitedns/786" target="_blank">📅 05:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-785">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V17gOtD8WX8bJpvowiwIplaNWr4V9G_-Fh6zt_JoChcK9Wlfs4z80-VcOuDdypAmD8DrLQkTd0ynNZhxMqLfyBGG0siAlBAU5bZ8fwvn5QLjScw3oqPil22xXnY7dOCX_oci-261d5NfCX2Rh_CA3jD0MOvVsKf_NYfoSkt_lE4tw3zxq3CLfbgcVaUN6G48Q99JkGOaRIWUwou49nndyJL4li4jdKwp3zCKzWN-iKmWJovmsrSlE1RK5WSMz2BTNwYikJnib4mOxkPx2u4TpiCxsBBQF3zUZpx7wibBZXH3SuR3h5SDORDS44lKAWRRT8m0HKzKPwah_BdeFi_odg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
معرفی ربات جدید WhiteDNS برای راه‌اندازی و مدیریت سرور شخصی MasterDNS
♨️
ربات جدید WhiteDNS آماده استفاده است.
👉
@WhiteDNS_installer_bot
این ربات به شما کمک می‌کند بدون نیاز به درگیر شدن با مراحل پیچیده نصب، سرور شخصی MasterDNS خودتان را روی VPS راه‌اندازی و از طریق تلگرام مدیریت کنید.
✅
نصب خودکار MasterDNS روی VPS
✅
مدیریت سرور از داخل تلگرام
✅
دریافت اطلاعات اتصال و Encryption Key
✅
بررسی وضعیت سرور
✅
ری‌استارت و مدیریت سرویس
✅
مناسب برای استفاده شخصی، دوستان و خانواده
🔐
نکات امنیتی:
اطلاعات کاربر، اطلاعات ورود به سرور، رمز عبور، کلیدها و مشخصات VPS به هیچ عنوان ذخیره یا لاگ نمی‌شود.
اطلاعات فقط در همان لحظه برای اتصال به سرور و اجرای دستور مورد نیاز استفاده می‌شود و بعد از پایان نصب یا اجرای هر دستور، توسط ربات نگهداری نمی‌شود.
بعد از انجام عملیات، اطلاعات ورود و مشخصات سرور توسط هیچ‌کس قابل مشاهده یا دسترسی نیست.
به همین دلیل، کاربران همچنان مالک کامل سرور، دامنه و تنظیمات خودشان هستند.
این ربات فروشنده سرور یا دامنه نیست.
کاربران باید:
* دامنه خودشان را تهیه کنند
* سرور خودشان را تهیه کنند
* دی‌ان‌اس های لازم را روی دامنه تنظیم کنند
هدف ما این است که راه‌اندازی و مدیریت سرور شخصی برای کاربران ساده‌تر شود؛
نه این‌که همه وابسته به چند سرور عمومی و متمرکز بمانند. ما باور داریم کاربران سرعت و پایداری بیشتری با سرورهای شخصی و غیرمتمرکز خواهند داشت.
⚠️
این ربات در اولین نسخه عمومی منتشر می‌شود و ممکن است هنوز باگ یا مشکل داشته باشد.
لطفاً مشکلات و بازخوردها را برای ما ارسال کنید تا سریع‌تر بهترش کنیم.
ویدیو آموزشی خرید سرور و دامنه و تنظیم دی‌ان‌اس به زودی داخل چنل قرار خواهد گرفت.
@WhiteDNS</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/whitedns/785" target="_blank">📅 21:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-784">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejgQLqtM8KQ5b5g9UiZncuhte-JN48EkCUhZY_sos_WhAoQrUXMvElUG9m6UBSwl-M4OvVzFvrlFUda2N4SGhw7aX7XYRzmE-A2V0_vN0YlY8lkoaQBxA7i2Nr-bnKeXKEH21gltJgQHGwx3bCHI_BBrRcfDRlbfP0AyT_C-8vVvZm5wDWV9yxafY-gmVicjB9D46tfrfmFr94caLDPXizECq_bhdhuzAqub3PMosRYF_lXh9BcLuQNi7fsA-CNZ8WO37FRKjXROzU799F4JJfov6817mOio_7bu2XexeCbkKpg2aC82E9hLBc8WJE-QFv-oTicSLUd7R8QkE4g0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
پروژه جدید WhiteDNS در حال آماده‌سازی است
♨️
تیم WhiteDNS بر روی سیستمی کار میکند که کاربران بتوانند فقط با داشتن یک VPS و یک دامنه، سرور شخصی MasterDNS خودشان را مستقیماً داخل تلگرام راه‌اندازی کنند.
هدف این پروژه این نیست که ما به کاربران سرور یا دامنه بفروشیم یا مدیریت کنیم.
هدف تنها ساده‌تر کردن فرآیندی است که امروز برای خیلی‌ها پیچیده، زمان‌بر و فنی محسوب می‌شود.
در این سیستم، کاربر فقط:
• VPS خودش را تهیه می‌کند
• دامنه خودش را تهیه می‌کند
• DNS Record ها را تنظیم می‌کند
و باقی مراحل توسط ربات و Mini App تلگرام به‌صورت خودکار انجام می‌شود.
سیستم به‌صورت اتوماتیک:
• وضعیت DNS Record ها را بررسی می‌کند
• اتصال دامنه به سرور را تست می‌کند
• MasterDNS را نصب و راه‌اندازی می‌کند
• اطلاعات نهایی مثل Domain و Encryption Key را به کاربر تحویل می‌دهد
در عمل، کاربران می‌توانند بدون درگیر شدن با دستورات پیچیده لینوکس و تنظیمات طولانی، سرور شخصی خودشان را راه‌اندازی و مدیریت کنند.
این پروژه متن‌باز خواهد بود تا همه بتوانند کد آن را بررسی کنند.
در حال حاضر پروژه در مراحل نهایی توسعه قرار دارد و طی روزهای آینده نسخه اولیه آن منتشر خواهد شد.
@WhiteDNS</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/whitedns/784" target="_blank">📅 09:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-783">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/783" target="_blank">📅 18:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-782">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F97FL5iPBNIcF7yMHE14GL84MNVvY8gjGIKAiBVyHtq8Om3ceZH7bInYlhaMtcrTSJ8KsMsUeFbQSojD8ECXcHBFkoQpRa3Fo4fh4qhchsuh9mp-8aBWDfJ5rw4oQzMS2Vd_UOaYkzB51bz85Rj6MwvWjTAyBPn-fpxwHJC6ZvnZ6i_rxnwWl_MCghIs4RQI-b_rN0iSMF00DI5ZX0y2s2KvqDUEZfjp-a0P1B1_qpkAX0nPCN9Laqea6AADdZvqz2ZqxMlSi1G9PayktEQECibiBVIDxy1dXZKq-Hzde-fSKPYnf4F8scj77-Hg6jjsMuzBj88DqR_gMRscQIfLRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام دوستان
👋
چون سوالات خیلی تکراری و بی‌هدف شدن
🤔
ما یک گروه با تاپیک‌های مختلف درست کردیم
📂
لطفاً اونجا عضو بشید و توی تاپیک خودش سوال کنید
✅
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/whitedns/782" target="_blank">📅 18:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-781">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plRHXDq__U-1iNAKyaR6zqsABAkn8694O6uaduFrYxe_sWu8dL81W81Z8No-SShYUo4KuYxPCMw9I7t32g2tsxljh3oXqPFmeKi06qeuBCASX1Ane3OM56LIvMiNW08JV2rW0QYEAhsFvXEamUEbCIx-VMUWP3Pc1CHCc6Gc3RtH7OlxOai8mgTloyI49Bo7jHEW57GDrqi3jzrbciDIEzvafUHuX9tMd_TQ7aSIVEVsR0Aln9hISugmg8_DUCA1uOtx9pDZgObyMOluwnbF3HiTrj0hDpS_at7qdxWZmW_XMKi4Htdr_ymmftqVVccRTe7PcEhktMZWdeY-9ML2Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش پروکسی و تانل کردن ویندوز
در این ویدیو نحوه پروکسی کردن فایرفاکس با نرم افزار WhiteDNS
پروکسی کردن کردن کروم ادج
و همینطور تانل کردن کل ویندوز با متود جدید آموزش داده شده است !
لینک دانلود ویدیو ( داخلی ) :
https://dl.toolschi.com/view.php?f=9f27edab8159500e.mp4
لینک دانلود نرم افزار  TunnelX ( داخلی ) :
https://uplod.ir/75m7wx9r6c17/TunnelX-v2.1.0__Whitedns.zip.htm
لینک گیت هاب TunnelX
:
https://github.com/MaxiFan/TunnelX/releases
امکان هست که آنتی ویروس  TunnelX رو حذف کند. در صورت نیاز اون رو به لیست نرم‌افزار های سفید آنتی ویروس خود اضافه کنید.
منبع تصویر کانال اینترنت آزاد
1️⃣
@WhiteDNS</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/whitedns/781" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-780">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">+۲۵۰ ریزالور جدید به ربات تلگرام WhiteDNS اضافه شده
برای دریافت وارد بات شوید
@dns_resolvers_bot
و بعد دستور زیر را اجرا کنید
/dns_master</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/whitedns/780" target="_blank">📅 16:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-779">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/779" target="_blank">📅 16:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-778">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">لینک داخلی آموزش ساخت سرور شخصی StormDNS & MasterDNS
https://guardts.ir/f/d68436b0fc33</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/whitedns/778" target="_blank">📅 10:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-774">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lS9b87a6s_7636qUBRACNdW1EafkzfIpJ9uASRTPH2L0QOwgEBW1er2eBPGBfpVPKzn8d2BH4oy_Jn9Lx_Wobwx6Wj66JSYseNBnShXgIe2dGag-mbJy1zXdk2TGU2T9tiCcmHHep6Y16fW58wINk2FWOGFBu8Jbm77smgG4WdtNhDZVl4cB6rfLspNw3f3ash1Mmbfpny0yXQDWwPRaIbV3gfJR8O2om67uadEO1vrcrZfG5t2ejrhHR-AHYOL7FJ32ScTnPV2-DQvMnI49fBpeF57wVjSydm9slatre9rhPYiqJ7KfY-fO5OCLLQicqto4-So8Y6js9nowbXlOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjsOCqmecZKFqa3vfh4Fqgai_ea5cGteCT5JRm1eqsrLHVkMKdBSqMPIr0w5KR_OvPWsfSzVUEsgJsiMWMz8d5Ljb_9o19K_NqK1iMPF1rSp7ND94zYDeFsBZq7AumogomcqfMwbpabEgmMGeC9KZ6H4_YusNAmlmnNNxRxbfrkeRiMpxqg8zwrtC4mLN8_WVmW_LraW217NHXPP8b8r_a3k20gk9Zk9x_AURia5JFO1K4VbQAenXz6IO-Dn6f7CAUC3muDWbDaeRU6OMCCGkklLIwGT2jEtVFigf19G7uJVrpD3w8y23gnSlBoss6nfQYcKgHTVo6HPwidZJAGDzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWrK-fpRztiB5y6ll1MK03LS9EZlnz97VBQZWS4KSuiJaG7b1oxMg55eJH00rcP5Jp9VJmUmdj47jsINYsLSnJfhqozaQMAgvEV89fCivPfy9N590rtOOuDCJ-fAbdgtZAd-fW20tENlK0EIz8NV-r--Sd--162IwJTCNeNzq9kHvrTb_on-YUObO2o2IDiidSSL8ABQyt1omRmqsib5QI-ndma65AZ6m5VsQtV-QzeUnwFgQH-jo7eEVZtqCG7ej4ifaxYk6-05F_M6Mi__7IMG-O9Rgd21BllaYIT_frNWbdB-EnUt14QKBZgPRNlEcl-G01vBd6w01wCWrilhcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">- برای پیدا کردن سرور برای وصل شدن به تاپیک سرور برید
- برای راه اندازی سرور شخصی به تاپیک سرور شخصی برید
- برای آموزش و یادگیری اولین شروع با این ابزار به تاپیک اولین شروع برید
🫡
لینک گروه اصلی
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/whitedns/774" target="_blank">📅 07:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-773">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جمع‌بندی نهایی
تیم WhiteDNS تمام نشده، رها نشده و قرار نیست فقط به چند سرور عمومی محدود بماند.
برعکس، هدف ما این است که استفاده از WhiteDNS از حالت وابسته به سرورهای عمومی خارج شود.
کاربران می‌توانند با آموزش، سرور شخصی یا گروهی خودشان را راه‌اندازی کنند و اتصال پایدارتر و اختصاصی‌تری داشته باشند.
این روش برای اتصال حیاتی، شرایط سخت و دسترسی ضروری طراحی شده است؛ نه برای مصرف سنگین، دانلود زیاد یا انتظار سرعت VPNهای تجاری.
تیم WhiteDNS همچنان کنار شماست.
فقط قرار است از این به بعد، به‌جای اینکه فقط ماهی بدهیم، بیشتر ماهی‌گیری یاد بدهیم.</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/whitedns/773" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-772">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هدف اصلی WhiteDNS
هدف WhiteDNS کمک به دسترسی آزادتر به اینترنت در شرایط سخت و محدود است.
WhiteDNS یک پروژه غیرانتفاعی است و تمرکز ما روی ساخت ابزار، آموزش و کمک به کاربران برای داشتن راه‌های پایدارتر اتصال است.
ما همچنان مسیر توسعه اپلیکیشن، بهبود کیفیت، آموزش و نگهداری زیرساخت‌های فعلی را ادامه می‌دهیم.
اما می‌خواهیم کاربران کمتر به سرورهای عمومی وابسته باشند و بیشتر بتوانند اتصال اختصاصی خودشان را بسازند.</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/whitedns/772" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-771">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آیا دانش فنی زیادی لازم است؟
برای راه‌اندازی اولیه کمی دقت لازم است، اما آموزش‌ها طوری آماده می‌شوند که کاربران معمولی هم بتوانند مرحله‌به‌مرحله انجام دهند.
اگر هیچ تجربه‌ای با سرور نداشته باشید، شروع کار ممکن است کمی سخت به نظر برسد.
اما بعد از یک بار راه‌اندازی، استفاده از آن بسیار ساده‌تر خواهد بود.
هدف ما این است که این مسیر را تا حد ممکن ساده‌تر، قابل فهم‌تر و قابل انجام‌تر کنیم.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/whitedns/771" target="_blank">📅 07:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-770">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آموزش‌ها کجاست؟
ویدیوها و آموزش‌های مربوط به نسخه اندروید، نسخه دسکتاپ و راه‌اندازی سرور شخصی داخل کانال قرار داده شده‌اند.
لطفاً قبل از پرسیدن سوال، داخل کانال سرچ کنید.
برای پیدا کردن آموزش‌ها می‌توانید این عبارت‌ها را جستجو کنید:
آموزش
سرور شخصی
دسکتاپ
اندروید
StormDNS
MasterDNS
Resolver
آموزش‌ها مرحله‌به‌مرحله منتشر شده‌اند و با کمی جستجو قابل پیدا کردن هستند.
همچنین داخل گروه اصلی تاپیک اولین شروع همه چیز رو توضیح داده
https://t.me/whitedns_group/32380/38590</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/whitedns/770" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-769">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اگر سرور کند بود، مشکل از اپلیکیشن است؟
نه لزوماً.
کندی یا قطعی می‌تواند دلایل مختلفی داشته باشد:
- شلوغ شدن سرور عمومی
- ضعیف بودن Resolverها
- اختلال یا محدودیت سمت اینترنت ایران
- کیفیت پایین مسیر شبکه
- تنظیمات نامناسب
- استفاده تعداد زیادی کاربر از یک سرور مشترک
کیفیت نهایی اتصال به سرور، Resolverها و شرایط شبکه هم بستگی دارد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/whitedns/769" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-768">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">چه انتظاری نباید داشته باشید؟
از WhiteDNS نباید انتظار سرعت بالا برای مصرف سنگین داشته باشید.
ممکن است شبکه‌های اجتماعی باز شوند، اما همیشه سرعت عالی نخواهد بود.
برای مواردی مثل این‌ها مناسب نیست:
- دانلود زیاد
- ویدیو با کیفیت بالا
- وب‌گردی سنگین
- استفاده هم‌زمان چندین اپلیکیشن پرمصرف
- انتظار سرعت شبیه VPNهای تجاری
این روش بیشتر برای دسترسی ضروری طراحی شده، نه مصرف سنگین روزمره.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/whitedns/768" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-767">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این روش برای چه کاری مناسب است؟
WhiteDNS و روش‌های مبتنی بر MasterDNS/StormDNS بیشتر برای شرایط سخت، محدود، ناپایدار و اضطراری ساخته شده‌اند.
این روش برای مواردی مثل این‌ها مناسب‌تر است:
- اتصال حیاتی
- پیام‌رسان‌ها
- دسترسی ضروری
- شرایط محدودیت شدید اینترنت
- استفاده سبک و کنترل‌شده
این روش جایگزین کامل VPNهای پرسرعت تجاری برای مصرف سنگین نیست.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/whitedns/767" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-766">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">استفاده گروهی با دوستان و آشناها
یکی از بهترین روش‌ها این است که چند نفر با هم یک سرور تهیه کنند.
اگر دوست، خانواده یا آشنایی خارج از ایران دارید، می‌تواند برای تهیه یا راه‌اندازی سرور کمک کند.
بعد از راه‌اندازی، اطلاعات اتصال داخل WhiteDNS وارد می‌شود و همان سرور به‌صورت اختصاصی‌تر برای شما یا گروه کوچک‌تان قابل استفاده خواهد بود.
این روش معمولاً از استفاده از سرورهای عمومی شلوغ پایدارتر است.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/whitedns/766" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-765">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هزینه تقریبی سرور شخصی
هزینه راه‌اندازی سرور شخصی معمولاً خیلی بالا نیست.
به‌صورت تقریبی:
شروع کار: حدود 7 دلار
هزینه ماهانه بعدی: حدود 6 دلار
البته ممکن است سرورهای ارزان‌تر هم پیدا کنید.
یک سرور حدوداً 6 دلاری معمولاً می‌تواند برای حدود 5 تا 10 کاربر سبک و معمولی کافی باشد.
اگر چند نفر با هم هزینه را تقسیم کنند، هزینه ماهانه برای هر نفر بسیار کمتر از اکثر سرویس‌های VPN خواهد شد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/whitedns/765" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-764">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مزیت سرور شخصی
راه‌اندازی سرور شخصی یا گروهی چند مزیت مهم دارد:
- فشار کاربران عمومی روی سرور شما نیست
- پایداری معمولاً بهتر است
- در بعضی شرایط سرعت بهتری می‌گیرید
- احتمال پیدا کردن Resolverهای مناسب بیشتر می‌شود
- کنترل کامل‌تری روی تنظیمات دارید
- هزینه آن معمولاً از خرید VPN کمتر است
- می‌توانید با دوستان یا خانواده به‌صورت گروهی استفاده کنید
ابزار WhiteDNS برای همین ساخته شده که فقط محدود به چند سرور عمومی نباشد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/whitedns/764" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-763">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">چرا سرور عمومی جدید منتشر نمی‌کنیم؟
وقتی یک سرور عمومی در کانالی با ده‌ها هزار کاربر منتشر می‌شود، خیلی سریع زیر فشار زیاد قرار می‌گیرد.
در نتیجه:
- سرعت کم می‌شود
- اتصال ناپایدار می‌شود
- سرور گاهی از دسترس خارج می‌شود
- کاربران فکر می‌کنند مشکل از اپلیکیشن است
در حالی که مشکل اصلی معمولاً فشار زیاد روی سرور، محدودیت‌های شبکه، یا وضعیت Resolverهاست.
طبیعتاً یک سرور عمومی نمی‌تواند هم‌زمان برای هزاران نفر مثل VPN اختصاصی کار کند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/whitedns/763" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-762">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وضعیت سرورهای فعلی
سرورهایی که تا امروز توسط تیم WhiteDNS ارائه شده‌اند، همچنان نگهداری می‌شوند و تا جایی که امکان داشته باشد فعال خواهند ماند.
اما از این به بعد برنامه‌ای برای انتشار مداوم سرورهای عمومی جدید از طرف تیم نداریم.
اگر سروری متعلق به خود تیم WhiteDNS باشد، فقط داخل تاپیک «سرورها» اطلاع‌رسانی خواهد شد.
تمرکز اصلی ما از این به بعد آموزش، مستندات و کمک به کاربران برای راه‌اندازی سرور شخصی یا گروهی است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/whitedns/762" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-761">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تمرکز جدید کانال
از این به بعد تمرکز اصلی ما بیشتر روی این موارد خواهد بود:
- آموزش استفاده بهتر از WhiteDNS
- آموزش راه‌اندازی سرور شخصی MasterDNS و StormDNS
- آموزش نسخه اندروید و دسکتاپ
- آموزش پیدا کردن و تست Resolverها
- معرفی تنظیمات بهتر
- رفع اشکال و راهنمایی کاربران
- بهبود اپلیکیشن و اطلاع‌رسانی نسخه‌های جدید
هدف ما این است که کاربران فقط مصرف‌کننده چند سرور عمومی نباشند.
نرم‌افزار های ما طوری طراحی شده که بتوانید از سرورهای خودتان، سرورهای دوستان‌تان، یا هر سرور سازگار با MasterDNS و StormDNS استفاده کنید و اتصال پایدارتر و اختصاصی‌تر بسازید.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/whitedns/761" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-760">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سلام به همه همراهان WhiteDNS
از امروز رویکرد ما در WhiteDNS کمی تغییر می‌کند.
WhiteDNS از ابتدا برای استفاده با سرورهای MasterDNS ساخته شده و همچنین از فورک StormDNS هم پشتیبانی می‌کند.
یعنی استفاده از WhiteDNS فقط محدود به سرورهایی نیست که از طرف کانال معرفی می‌شوند.
هر سرور MasterDNS و همچنین سرورهای سازگار با StormDNS می‌توانند داخل اپلیکیشن WhiteDNS استفاده شوند.
تا امروز، در کنار توسعه اپلیکیشن، تعدادی سرور آماده هم در اختیار کاربران قرار دادیم تا شروع استفاده برای همه راحت‌تر باشد.
👇
اما در ادامه یک سوءبرداشت ایجاد شد:
بعضی از کاربران فکر می‌کنند اگر سرورهای معرفی‌شده شلوغ شوند، کند شوند یا موقتاً در دسترس نباشند، یعنی خود اپلیکیشن WhiteDNS مشکل دارد یا قابل استفاده نیست.
در حالی که WhiteDNS فقط یک اپلیکیشن وابسته به چند سرور عمومی نیست.
قدرت اصلی WhiteDNS این است که هر کاربر یا هر گروه کوچک می‌تواند سرور MasterDNS یا StormDNS خودش را راه‌اندازی کند و از همین اپلیکیشن برای اتصال استفاده کند.</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/whitedns/760" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-759">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">White DNS
pinned «
سرور جدید WhiteDNS   Domain: v.wdn.best Encryption Key: bad99364093861634030e96f11fe3132 Encryption: XOR @WhiteDNS
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/759" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
