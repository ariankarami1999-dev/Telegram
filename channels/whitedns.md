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
<img src="https://cdn4.telesco.pe/file/FD-znG9gFERL6JvNq7er2Dj-TlHyNGYOmW99a0S7mNM1s1QEAEDIgvWK4pp8pbUkARhoPRKp4ab2VJH393-dswirss1ArlSC6kpz82Pe7OEdAFDzRNvxvHsYkMpTxeiBTQiyWGIBuZ3Yqg5lOCfUrRDNZnnU3z4A7qbUwPZcAgHlYSWjExuOa8Du4Ci-j0H4KXmQDRAQYFx5_JplYoB9DcAbqfnwnLuzTrF6HHxu8jnBB96ZFcmuf_seCtqHqwqMT7dBoRNoJo_DCnNTPevvx3qasdKu_uROKwThmFLvsQXQIzkrueDvekwPZYw03M1Qe-ZPByPZ6jGTpEB_ka3z2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 17:38:01</div>
<hr>

<div class="tg-post" id="msg-1660">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">موقت :
الان ما کلا لایو بگذاریم سوالات را مثل دفعه قبل جواب بدیم ؟
اگر اره بهترین روز و ساعت چی هست ؟</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/whitedns/1660" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-poll">
<h4>📊 محدودیت حجم کانفیگ ربات را از 1 گیگ به چقدر تغییر بدیم که برای انجام کارهای روزمره کافی باشه ؟👀</h4>
<ul>
<li>✓ 1.5</li>
<li>✓ 2</li>
<li>✓ 3</li>
<li>✓ 4</li>
<li>✓ همین خوبه☺️</li>
</ul>
</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/whitedns/1658" target="_blank">📅 13:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/EaRCKWa73CGKstAI8L93_fujZwuvh470VTs7Pcb0gIC60ZtnVfeSEhPH6exLAbB3igkaSA1PgDS8QlM2PqDQp3T7ec3Mrj7Lj6EWO705UR-_QjsYutolERcaRtWSef5sXIQXirHLOAhoUpxX0t4TeaEjIgB9Q5bENCz7XrD2gPBI7JHkRmhRrzji2P8hqxgTbftrbjpNK_BIGTWFLg9_vGQgZfXfio8yVj2nfWndK2HT5hoh8XDtOWny4C6EtB0mmO-Xc_5S5EqikqN9tPRKhXHkdVZLeg5_a8vAn7Adx9JrYNEPQzXFhmk_1uxYz51aiFi5l2enT9lzOxnlUhl9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#آموزش
اگر WhiteAesther mobile با یک بار زدن دکمه اتصال وصل نشد، یعنی هنوز باید تنظیمات درست شبکه خودت را پیدا کنی.
📡
این راهنمای کامل را قدم‌به‌قدم بخوان:
📖
https://github.com/WhiteDNS/WhiteAestherMobile/blob/main/docs/GUIDE.fa.md
@whitedns</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/whitedns/1656" target="_blank">📅 09:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1654">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/t-1CGVqecGt_6du2XQGHW63QRmd_ktf2ym0BCc47mvP7iHbCjRTefHrL2DGzLccAqcyFmIM5zr3e5AujfMFUShBFuWzDHf_v-NXOHbAbgB4w9979cvjuaQtIKyaxBE1vbpDhwpAUF381aJkd_3uP9TJmyg-nc-Z5F2heUp-ptCtMueZNm8KdLs-FoM2CBmwL-mVn7-FiSBhUvkz8aHaSHeLdxCVvlYBQJaDhtmv1EOBcPYGFSEH4duyoOTtVH-b7r8CNBDfQGp0YezwWYwwXPLWM6eGlQ6wYYWhVytiPgJkeXoppL4x2ZCPiMW0Sjj9_mJ1CSbsfp5LmnKOflyIIoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود دوستان عزیز
👋
چند تا کانفیگ جدید به ربات اضافه کردیم  که شاید بهتر بتونید متصل بشید و برای سرویس های خارجی مشکلات کمتری داشته باشید . کانفیگ ها تست شده است و مشکلی نداره
✅
از حالا به بعد شما میتونید تا
3 کانفیگ
را انتخاب کنید
😃
❤️
لطفا برای اطلاعات بیشتر حتما پست زیر را مطالعه کنید
⚠️
⚠️
https://t.me/whitedns/1608
Bot
🤖
:
@WhiteDnsChainbot
@whitedns</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/whitedns/1654" target="_blank">📅 05:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1653">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OoU9YuDol02rugFSFbyVlFk_IDDHfZXZSy7O4Dc8dxBskueM1HRKTgMQeODogeNfW84GChiZaLWxCEDH9eu-_w_sSH2nERVo32QxbupeesNLij2ItfTjJXD72TkOn3jRn3R311oK9yHUxq6n--7YZCVMrNxxgasK836w2zcIjOzbCVGZ0jcIuJrIwXbDaPORNl-SxKwyc4_iKbS_21meQZUZqEv01ljtUczF4iXV9n7YPlonCTu2rTjqH0-TGfVFY77PNH0atAy7kHeZyfY-l37zHAiNKXmkay_EFC91JkkfdqrDWgxKWjVCyK1MNEibgqmV0BlnJfwcMVeU_G8AEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/whitedns/1653" target="_blank">📅 05:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/eDccyBsukkZLjlyrYbvoT4R7YTAHig18O6TSJEcL4LugWam9k7DehZMg2GbdizIyvALcW2vbnYQuzPxWXPd1z2qb35H9AAh9NP-9AJ8lrzqxm7A7ycMPjyH0jwNC8YdD15heiMOw77-huddiPc1Qe5gN38gcE-aj78WMwUotWGeSrTQYCu-b6KuuU14icA8pK8c67lddFlQKmjHLifHaXNfSSQmvLzPGRUnkmatpsC5axmRZMWAKxg7IFySdJCYu92LbZtYWQIPbkyXKCnXDsreLcGNXPZS0Cz5lUq66P3rzwyuYvyPJlZIqgvnt1yyxv-leKy0nL95uomMC599BdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/whitedns/1652" target="_blank">📅 05:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DrcZjIH_0LarVKYF8MrvAaQaP_qeK2u583RvVglWyOEhVQot3kS-sa9K7rirw4kcRIFFbCgbwTqp8FrQGuLo_M44IC3nQNdIBGsM2Ox0w7hiAXO1wnsbMz2p9xLseYK94wwT7aeSvLUkerBY2kEyY7BZPo_eHiomAzU9zagHDUBK4-vlNf5GB8ieuBQTvXrd8Nf8HnRYeJMgQrV2B_4-uOnQ2l2UGkgwmM0kQjgg1QvgK0NUjXHfrb_C4E8YQh2DcKLCB2R3y_X5beKSLdDFGb01hJ0sPtPxG-AVTfoClQ_c8dfFxhP-HpA2k568dBuVAlfv00RAugw4FS73SPpJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
آپدیت WhiteAesther — نسخه 1.2.5
🔥
⚠️
⚠️
⚠️
در این ورژن رفع باگ Android TV انجام شده است و دوستانی که روی گوشی استفاده میکنند لازم نیست اپدیت کنند
⚠️
⚠️
⚠️
مشکل کنترل با ریموت در Android TV برطرف شد. پیش از این، بعد از رسیدن به بخش «Connected for»، امکان حرکت به قسمت‌های پایین‌تر صفحه وجود نداشت.
حالا با دکمه‌های بالا و پایین کنترلر می‌توانید به‌راحتی بین تمام بخش‌های صفحه Home حرکت کنید و اطلاعاتی مثل آدرس، ترافیک مصرفی و جزئیات اتصال را ببینید.
این تغییر فقط مربوط به حالت Android TV است و عملکرد نسخه موبایل تغییری نکرده.
🔗
دانلود رسمی از گیت هاب
@whitedns</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/whitedns/1651" target="_blank">📅 16:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwyzZ6KI4zAdsNrh5xIacgGn_nUvpZx42wjFOu-UY6GeiRIlAFg9YB9qHUwodln9U0S0Wv9JpTu2LCaexPzTEtUHgOddNtvnUc2v4HoOAp0bdfhHPsu8WpIgP_fRm9BaNLPdQqszbrCXynHLRaHAOad56ebZ8bhIM7uUChN3ACn3kZbnvHshPnvJufNLsGg3x-ja09CYMsNKC5rveSFfUP6ToeGYar5_nuoAznYvZmz6ACjRJsWheIcVfYMRZ-VpvS3Ow2Ci5tfpufLMMNya0SaNpQQQJHZTWXjIaHjbjykKSF3aUx7CEsmw4UanF-kkPVY4IIeOGnIlRKPI6UQvNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
نسخه Android TV و Google TV برنامه WhiteAesther منتشر شد
از نسخه v1.2.4 به بعد می‌توانید WhiteAesther را روی تلویزیون، TV Box و دستگاه‌های Google TV فقط با ریموت یا دستهٔ بازی کنترل کنید؛ بدون نیاز به صفحهٔ لمسی.
حداقل نسخه موردنیاز: Android 8
🔗
دانلود رسمی از گیتهاب
⚠️
برنامه را فقط از لینک رسمی بالا دانلود کنید.
🦢
🦢
🦢
🦢
🦢
🦢
📥
کدام فایل WhiteAesther را برای تلویزیون دانلود کنیم؟
برای بیشتر تلویزیون‌ها و TV Boxهای جدید:
"WhiteAestherMobile-1.2.4-arm64-v8a.apk"
اگر مدل پردازنده را نمی‌دانید یا فایل بالا نصب نشد:
"WhiteAestherMobile-1.2.4-universal.apk"
نسخه Universal روی دستگاه‌های بیشتری اجرا می‌شود، اما حجم بیشتری دارد.
گزینه‌های دیگر:
• نسخه "armeabi-v7a": مخصوص دستگاه‌های قدیمی ۳۲ بیتی
• نسخه "x86_64": بیشتر برای شبیه‌سازها و بعضی دستگاه‌های خاص
• فایل "AAB": برای نصب مستقیم مناسب نیست
🦢
🦢
🦢
🦢
🦢
🦢
🛠
نصب WhiteAesther مستقیماً روی Android TV
۱. مرورگر تلویزیون یا برنامه‌ای مثل Downloader را باز کنید.
۲. وارد صفحه رسمی انتشار شوید.
۳. فایل APK مناسب دستگاه را دانلود کنید.
۴. فایل را باز کرده و Install را بزنید.
اگر اجازه نصب داده نشد، گزینه Install unknown apps را برای مرورگر یا Downloader فعال کنید.
این تنظیم معمولاً در یکی از مسیرهای زیر قرار دارد:
Settings → Apps → Special app access → Install unknown apps
یا:
Settings → Security → Unknown sources
بعد از نصب، بهتر است این دسترسی را دوباره غیرفعال کنید.
🔗
دانلود نسخه رسمی از گیتهاب</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/whitedns/1650" target="_blank">📅 10:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDKNzV53GvnAPqZ3TO9aPyrd1HjHNjB9hv2Wa98byizbMKFmfhhQcZEnj5Lvu3MWi3tRrPvuR-Ck1Hulnxl0ktt_i6ESV6p2Ty8jjwTPA29rBWCwo55VnoWxlTHjXJUThwrazMNaz9zy-uVrWAXI8eYt3dU2TiehkEWIYk6TIiHO8UyjCR4XzstAnc3nbJOeo7FJXMhFwZfcUJ0ymfpIQoFPeQUTv9ViDv5braFtPCIxaXNROezC4bE_Y3FpNyA2cMNJ1m3eQGO033bLBoLuLlUdXruzSQvAu83sxL_F5Bmocf-8VHIEpzL5O1x3p4f75smkKdThRaYNorXhTE1pXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
داریم تست های نهایی رو برای WhiteAesther روی AndroidTV  انجام میدی
م</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1649" target="_blank">📅 19:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1645">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/o99UD0Gra0xDe59OSfd3LEYE2eyh-dSCnHRXqjSfJRNoR7PTBTa8732eimqx0R_qdtBuS8ZVTbDVLHgyIUxHUrYoiH0yxmn4OwkeWIWA7O_BElHGmD7RfqfkzwQlMfK5_244sS1EJRdpXvZ43RY5pBCR2zSoysFtR37Igo4Bl2FOZutBqOqweof5N_aElYiwsDkOHmNcvXdZrI3Wel6LdmGDPNrqFrz9pPIVG0jJ-4lRObP4pESIxgTep1k002SrNEY1g1zN4soTsCUH6Kz0xsgr9-pPnAPCNugiw2OmExjIHVscIGw8mwjag9kOn4P0y-65V0QtE_8-cnCD_VmB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Vt26Skj1kwUCzioSy507CAZdk_pRpz9yPdAxC-N5A797b4NNMepHeicNLdnohQ87Vd5CxjjTBf67nxoRMNZY2gR2wMUcFoIb0M-2rEHVLVIEJtOo2wNx68zY2D5GJGL3GC5Q-h42I_tOTHcyG_QrIB3_gIwdW83RLkI-1fxnSrbry9xm6_vKSpkAVvvtR1yayOqOsjN384zmZ8SoCcmK2HDy18rvrW3SSNGsAvvvqx9-ZXGZGfDJLh8q106H8Srf70hdD2ZumQK4Wnhd3wxuqrWupLrZ6r8iMYry0ab6_64UZwvsI7CBVDf6MVUQqshNWVmEl-UiJwLnZanduJKxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/cKTW22YKmH-qYxic83GeCGUDlZhdDRmgurc_KWRELDiQEalchgyQpPLuQcGhRdcnKXdZOTvxDgRgvy4YnCAFwE9G20dTZwEJTY4tn055xSncci5h8jZuyJUi2vV1lKGx5D_Loe3J5MAvmybleNV1v8OLVXsDY_tneknMkyRWgTyY4P8x728nl-Pnr1ZH6bihANA0MowJJBbabtulBRcTaoGk-AyL8nonX40-7vW-xcbMTflHKqo2QjygNNqE_A0pMCh_Vh4FgSmHcuRDG1LB9gKkZGrhShmNas1P_ufDPg_QumqvJApJZQCOs9hed-xuHo4B_Tn8oX4sE7KMisJnKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای زنجیر کردن  Psiphon Desktop
با
whiteaesther
Desktop
🔥
🔥
اول Psiphon را وصل کنید.
در تنظیمات Psiphon proxy محلی را پیدا کنید. و یکی از پورت های زیر را وارد کنید . توصیه میشود از ساکس استفاده کنید
SOCKS5:1080
HTTP:8080
WhiteAesther را باز کنید.
بروید به:
Advanced
→
Routes & transports
→
Anti-blocking
در فیلد
Dial through a local proxy
یکی از این‌ها را وارد کنید:
socks5://127.0.0.1:1080
یا:
http://127.0.0.1:8080
بعد
Save profile
را بزنید.
حالا Connect کنید. مسیر  می‌شود:
App traffic -> WhiteAesther local SOCKS -> Aether/WARP -> Psiphon local upstream -> Internet
اگر میخواهید که whiteaesther سیستم شما را تانل کند روی Full tunnel و اگر نه از پراکسی whiteaesther برای نرم افزارهای خاص خودتون استفاده کنید
نکته : قابلیت exit chain را توی تنظیمات خاموش کنید
⚠️
⚠️
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/whitedns/1645" target="_blank">📅 15:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1644">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG/PattN کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  پروژه های خوبی وجود دارند که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/whitedns/1644" target="_blank">📅 06:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1641">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مطالب اموزشی نسخه 1.6.0 دسکتاپ whiteaesther
🔥
🔥
خلاصه :
🔧
تغییرات و قابلیت‌های جدید
▫️
حالت
Full Tunnel
یک کارت شبکهٔ مجازی ایجاد می‌کند تا تمام ترافیک سیستم از تونل عبور کند؛ حتی برنامه‌هایی که تنظیمات Proxy را نادیده می‌گیرند.
▫️
خروج سایت‌های ایرانی از تونل
شامل ۲۹۰۶ رنج IP و ۴۱٬۷۲۹ دامنه ایرانی است که مستقیماً داخل خود برنامه قرار گرفته‌اند و نیازی به دانلود جداگانه ندارند.
▫️
دریافت خودکار دسترسی Administrator
هر زمان دسترسی ادمین لازم باشد، برنامه خودش پیام تأیید ویندوز را نمایش می‌دهد و با سطح دسترسی لازم دوباره اجرا می‌شود. دیگر نیازی به راست‌کلیک و انتخاب
Run as administrator
نیست.
▫️
اطلاع‌رسانی نسخه‌های جدید
در صورت انتشار نسخه جدید، یک نوار اطلاع‌رسانی بالای برنامه ظاهر می‌شود که با یک کلیک شما را به صفحه دانلود می‌برد.
▫️
چهار تنظیم جدید موتور
تنظیمات بیشتری برای موارد زیر اضافه شده است:
Local Proxy
Domain Sniffing
Identity Re-registration
Keepalive
مقدار پیش‌فرض
Keepalive
نیز از ۵ ثانیه به ۲۵ ثانیه تغییر کرده است.
▫️
عبور مستقیم ترافیک شبکه محلی
ترافیک دستگاه‌های داخل شبکه مثل Printer، Router و NAS دیگر به نود خروجی فرستاده نمی‌شود و مستقیماً در شبکه محلی باقی می‌ماند.
▫️
رفع مشکل آیکون‌های مرده در Taskbar
حالا در تمام حالت‌های خروج از برنامه، آیکون آن به‌درستی از Taskbar و System Tray حذف می‌شود.
▫️
حذف اتصال خودکار
برنامه دیگر بدون اجازه کاربر به‌صورت خودکار متصل نمی‌شود. زمان اتصال کاملاً در اختیار شماست.
▫️
باز شدن صحیح پنجره با کلیک روی آیکون برنامه
مشکلی که در حالت اجرای برنامه با دسترسی Administrator باعث می‌شد ویندوز فرمان باز شدن پنجره را مسدود کند، برطرف شده است.
🛡
۱. حالت Full Tunnel — جلوگیری کامل از DNS Leak
تا الان دو حالت داشتیم:
▫️
فقط همین برنامه
▫️
کل دستگاه
مشکل حالت دوم این بود که فقط برنامه‌هایی را پوشش می‌داد که از تنظیمات Proxy ویندوز استفاده می‌کنند.
خیلی از برنامه‌ها این تنظیمات را نادیده می‌گیرند و مستقیماً به اینترنت یا DNS وصل می‌شوند. در نتیجه ممکن بود بخشی از ترافیک خارج از تونل عبور کند.
حالت جدید
Full Tunnel
یک کارت شبکه مجازی ایجاد می‌کند و
تمام ترافیک سیستم
را از تونل عبور می‌دهد؛ حتی برنامه‌هایی که Proxy سیستم را نادیده می‌گیرند.
این حالت بهترین گزینه برای جلوگیری از DNS Leak است.
🔹
روش فعال‌سازی
۱. برنامه را باز کنید و متصل شوید.
۲. پایین صفحه اصلی سه حالت وجود دارد.
۳. گزینه سوم یعنی Full Tunnel را انتخاب کنید.
۴. ویندوز برای دسترسی لازم از شما اجازه می‌خواهد. گزینه Yes را بزنید.
۵. برنامه به‌صورت خودکار بسته و دوباره با دسترسی لازم اجرا می‌شود.
دیگر لازم نیست روی برنامه راست‌کلیک کرده و Run as administrator را انتخاب کنید.
✅
برای تست
بعد از اتصال، سایت زیر را باز کنید:
dnsleaktest.com
سپس گزینه Extended Test را اجرا کنید.
سرورهای نمایش‌داده‌شده باید مربوط به کشور نودی باشند که به آن متصل شده‌اید.
━━━━━━━━━━━━━━━━━━
🇮🇷
۲. خروج خودکار سایت‌های ایرانی از تونل
دیگر لازم نیست برای باز کردن بانک‌ها، دیجی‌کالا، آپارات و سرویس‌های داخلی، هر بار VPN را خاموش کنید.
سایت‌های داخلی معمولاً نیازی به عبور از تونل ندارند. عبور آنها از تونل فقط می‌تواند سرعت را کاهش دهد و پهنای باند نود را مصرف کند.
حالا می‌توانید کاری کنید که:
سایت‌های ایرانی مستقیم باز شوند و بقیه ترافیک از تونل عبور کند.
🔹
روش فعال‌سازی
به مسیر زیر بروید:
Advanced → Traffic & DNS → Routing Rules
سپس گزینه زیر را روشن کنید:
Iranian sites bypass the tunnel
لیست موردنیاز داخل خود برنامه قرار دارد و شامل:
▫️
۲۹۰۶ رنج IP ایران
▫️
۴۱٬۷۲۹ دامنه
است.
هیچ فایلی هنگام اتصال دانلود نمی‌شود؛ بنابراین این قابلیت حتی زمانی که دسترسی آزاد به اینترنت ندارید نیز قابل استفاده است.
━━━━━━━━━━━━━━━━━━
📱
۳. اشتراک اینترنت با گوشی، تلویزیون و دستگاه‌های دیگر
حالا می‌توانید کامپیوتر خود را به یک Proxy Server تبدیل کنید و دستگاه‌های دیگر را از طریق آن به اینترنت متصل کنید.
بدون نیاز به نصب WhiteAesther روی گوشی.
🔹
روش فعال‌سازی
به مسیر زیر بروید:
Advanced → Traffic & DNS
در بخش:
Share with other devices
گزینه اشتراک‌گذاری را روشن کنید.
برنامه یک آدرس مشابه این نمایش می‌دهد:
192.168.1.24:1080
بار اول ویندوز ممکن است از شما اجازه Firewall بخواهد.
گزینه:
Allow access
را انتخاب کنید.
اگر اجازه ندهید، Proxy فقط روی همان کامپیوتر قابل استفاده خواهد بود.
📱
در Android
وارد تنظیمات Wi-Fi شوید.
شبکه متصل را باز کنید و به بخش تنظیمات Proxy بروید.
حالت Proxy را روی Manual قرار دهید.
برای مثال:
Hostname:
192.168.1.24
Port: 1080
همان IP و پورتی را وارد کنید که WhiteAesther نمایش داده است.
🍎
در iPhone
به مسیر زیر بروید:
Settings → Wi-Fi
روی علامت (i) کنار شبکه بزنید.
سپس:
Configure Proxy → Manual
را انتخاب کرده و IP و Port نمایش‌داده‌شده در WhiteAesther را وارد کنید.
🔐
نکته امنیتی مهم
اگر Username و Password تعیین نکنید،
هر دستگاهی که به همان شبکه Wi-Fi متصل باشد می‌تواند از Proxy شما استفاده کند.
در شبکه خانگی شاید این موضوع مهم نباشد، اما در محل کار، دانشگاه، هتل یا کافه حتماً هر دو فیلد زیر را پر کنید:
Username
Password
خود برنامه نیز در صورت خالی بودن آنها با یک هشدار زرد به شما اطلاع می‌دهد.
یک Port برای هر دو پروتکل استفاده می‌شود:
HTTP
و
SOCKS5
بنابراین همان شماره Port را برای هرکدام که دستگاه شما پشتیبانی می‌کند وارد کنید.
━━━━━━━━━━━━━━━━━━
⚡️
۴. پشتیبانی بهتر از Hysteria2 و TUIC
اگر در Subscription شما نودهای Hysteria2 وجود داشتند و همیشه علامت — نمایش داده می‌شد، این مشکل اکنون برطرف شده است.
مشکل از اندازه Packet بود.
این پروتکل‌ها Packetهایی با اندازه حدود ۱۲۸۰ بایت ارسال می‌کنند، در حالی که تونل قبلی فقط ۱۲۵۲ بایت ظرفیت داشت.
در نتیجه حدود
۲۸ بایت کمبود ظرفیت
باعث می‌شد Packet قبل از ارسال حذف شود.
🔹
روش استفاده
به مسیر زیر بروید:
Advanced → Routes & Transports
سپس Protocol را روی:
WireGuard
قرار دهید.
برای این نودها از MASQUE استفاده نکنید.
در حالت MASQUE این محدودیت از سمت Cloudflare وجود دارد و برنامه نیز کنار نود توضیح می‌دهد که چرا قابل استفاده نیست.
━━━━━━━━━━━━━━━━━━
🔔
۵. اطلاع‌رسانی نسخه‌های جدید
از این نسخه به بعد، وقتی نسخه جدید WhiteAesther منتشر شود، خود برنامه به شما اطلاع می‌دهد.
یک نوار اطلاع‌رسانی در بالای برنامه نمایش داده می‌شود.
با زدن گزینه:
Get it
مستقیماً وارد صفحه دانلود نسخه جدید خواهید شد.
━━━━━━━━━━━━━━━━━━
🔧
سایر تغییرات
▫️
نودهای REALITY حالا با برچسب Not Supported مشخص می‌شوند.
موتور فعلی از آنها پشتیبانی نمی‌کند، بنابراین بهتر است وضعیت آنها واضح باشد تا اینکه نودی نمایش داده شود که هیچ‌وقت متصل نمی‌شود.
▫️
Subscriptionها کامل‌تر پردازش می‌شوند و مشکل جا افتادن بعضی نودها برطرف شده است.
▫️
مشکل باقی ماندن آیکون‌های قدیمی برنامه در Taskbar برطرف شده است.
▫️
برنامه دیگر به‌صورت خودکار متصل نمی‌شود. تصمیم برای اتصال کاملاً با کاربر است.
▫️
تنظیمات بیشتری برای Local Proxy، Keepalive و گزینه‌های پیشرفته اضافه شده است.
▫️
موتور برنامه به نسخه زیر ارتقا پیدا کرده است:
Aether 1.7.0
@WhiteDNS_Laurie</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/whitedns/1641" target="_blank">📅 05:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1640">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IgCMXhH-sWE9vE5UkNth5xACvdrnMGc4phs22-iw7hQG-N7uhk3NfO147jWrLIv9Pfml8BS1sydCXy94fJzDPXOEMlVpuhGI4vaiyAQvvtatkugueywvPkY0laXL9AF9-OTjghsenLb2hKMZXGIBrQnz0JxvIlTICJQGKLabQar05qz5dMaujpAK7K1a_q7iVPW0kBCoyHXOZQWDpHQvsHKZzq7_qcVBbZJEjRgYoEg3eZawSKgjjF5MZSGzgsR6IPzeKjru348Z-LI_Zt5GM-nyrvo3fSwKgw9daF45eRC6YV63rXuiS2-ttnm9_5NBueUYyKGSbP10DPVLsk5wPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه 1.6.0 دسکتاپ  WhiteAesther منتشر شد
بزرگ‌ترین آپدیت WhiteAesther تا امروز.
حالا می‌توانید:
▫️
کل کامپیوتر را تونل کنید
▫️
سایت‌های ایرانی را از تونل خارج نگه دارید
▫️
اینترنت را با گوشی، تلویزیون و دستگاه‌های دیگر به اشتراک بگذارید
━━━━━━━━━━━━━━━━━
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases
نسخه‌های موجود:
▫️
Windows
▫️
Linux —
deb / rpm / AppImage
▫️
macOS Intel
▫️
macOS Apple Silicon
━━━━━━━━━━━━━━━━━━
⚠️
نکته مهم قبل از تست
اگر برنامه رسمی
Cloudflare WARP
روی سیستم شما نصب است، قبل از استفاده از WhiteAesther حتماً آن را کاملاً
Disconnect
کنید.
اجرای همزمان دو VPN روی مسیر شبکه می‌تواند باعث تداخل، قطع اتصال یا نتایج گیج‌کننده شود.
━━━━━━━━━━━━━━━━━━
💬
اگر سؤال یا مشکلی داشتید، همین‌جا مطرح کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1640" target="_blank">📅 05:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1636">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">آموزش تغییر لوکیشن با Exit Chain
داخل اپ‌های WhiteVPN و WhiteAesther
🔥
واسه gemini و بقیه AI هایی ک نیاز دارین عالیه
https://youtu.be/yx-jFqv9pYM?si=VuY0qqm5qbFUJOO6</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/whitedns/1636" target="_blank">📅 03:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1634">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔗
نسخه ۱.۲.۳ اندروید WhiteAesther منتشر
شد ......!
در نسخه جدید سه بخش مهم اضافه شده:
🛡
قفل ایمنی
🧭
قواعد مسیریابی
⚙️
چند تنظیم جدید برای موتور اتصال
پایین، همه موارد را همراه با آموزش توضیح داده‌ایم.
🛡
۱. قفل ایمنی — Kill Switch
چه مشکلی را حل می‌کند؟
تا الان اگر تونل بعد از چند بار تلاش وصل نمی‌شد، برنامه تسلیم می‌شد و گوشی بی‌صدا به اینترنت معمولی برمی‌گشت.
حالا می‌توانید مشخص کنید که در چنین شرایطی، به‌جای برگشت به اینترنت عادی،
تمام ترافیک اینترنت مسدود شود.
آموزش
۱) وارد بخش Traffic شوید.
۲) بخش Advanced را باز کنید.
۳) گزینه زیر را روشن کنید:
Block traffic if the tunnel fails
تمام! از این به بعد اگر تونل از کار بیفتد، هیچ ترافیکی از گوشی خارج نمی‌شود.
🔸
حالت سخت‌گیرانه‌تر
بعد از فعال کردن گزینه بالا، گزینه دیگری ظاهر می‌شود:
Keep blocking after you disconnect
اگر این گزینه را روشن کنید،
حتی زمانی که خودتان اتصال را دستی قطع می‌کنید، اینترنت همچنان مسدود می‌ماند
تا خودتان آن را آزاد کنید.
⚠️
توجه:
در این حالت گوشی واقعاً اینترنت نخواهد داشت. اگر فراموش کنید این گزینه فعال است، ممکن است فکر کنید اینترنت یا شبکه مشکل دارد.
برای برداشتن قفل دو راه دارید:
▫️
از نوتیفیکیشن Traffic is blocked
▫️
یا از صفحه اصلی برنامه و دکمه Lift the block
اگر دوباره به تونل متصل شوید، قفل به‌صورت خودکار برداشته می‌شود.
🧭
۲. قواعد مسیریابی — Routing Rules
چه مشکلی را حل می‌کند؟
بعضی سایت‌ها و اپلیکیشن‌ها با IP خارجی درست کار نمی‌کنند؛ مثل بعضی بانک‌ها، اپ‌های داخلی یا سرویس‌های ایرانی.
قبلاً برای استفاده از آنها مجبور بودید VPN را کاملاً خاموش کنید.
حالا می‌توانید مشخص کنید که
فقط بعضی سایت‌ها یا سرویس‌ها از تونل عبور نکنند
و بقیه ترافیک همچنان از تونل استفاده کند.
آموزش
۱) وارد بخش Routes شوید.
۲) در کارت اول، گزینه Routing rules را که زیر Exit chain قرار دارد انتخاب کنید.
۳) دو کادر خواهید دید:
🔹
کادر
Never connect
هر چیزی که اینجا قرار بگیرد، اصلاً اجازه اتصال نخواهد داشت.
مناسب برای مسدود کردن تبلیغات، ردیاب‌ها و دامنه‌های ناخواسته.
🔹
کادر
Skip the tunnel
هر چیزی که اینجا قرار بگیرد،
بدون تونل و با IP واقعی شما
باز می‌شود.
مناسب برای بانک‌ها، سایت‌ها و اپلیکیشن‌های داخلی.
هر قانون را در یک خط جداگانه بنویسید.
مثال:
bank.example.ir
digikala.com
snapp.ir
نوشتن یک دامنه، زیرمجموعه‌های آن را هم شامل می‌شود.
برای مثال:
digikala.com
شامل این مورد هم خواهد شد:
www.digikala.com
حالت‌های پیشرفته
▫️
فقط همان دامنه دقیق:
full:
example.com
▫️
هر آدرسی که یک کلمه خاص داخل آن باشد:
keyword:tracker
▫️
یک محدوده IP:
cidr:
10.0.0.0/8
▫️
یک پورت مشخص:
port:25
▫️
کل شبکه محلی:
private
▫️
هر خطی که با # شروع شود، به‌عنوان توضیح در نظر گرفته شده و اجرا نمی‌شود.
⚠️
مهم:
هر چیزی که داخل Skip the tunnel قرار دهید، با
IP واقعی شما
به اینترنت متصل می‌شود. بنابراین این لیست را فقط برای موارد ضروری استفاده کنید.
🔸
نکته مهم درباره دامنه‌ها
در مسیر زیر:
Traffic ← Advanced
گزینه‌ای وجود دارد با نام:
Match rules on domain names
این گزینه به‌صورت پیش‌فرض روشن است و بهتر است روشن بماند.
اگر آن را خاموش کنید، قوانینی که با نام دامنه نوشته شده‌اند ممکن است کار نکنند؛ چون برنامه در اندروید معمولاً ترافیک را در سطح IP دریافت می‌کند.
در صورت خاموش بودن این گزینه، خود صفحه Routing rules نیز هشدار خواهد داد.
⚙️
۳. تنظیمات جدید موتور
تمام این تنظیمات در مسیر زیر قرار دارند:
Traffic ← Advanced
🔹
تنظیم DNS داخل تونل
گزینه:
DNS inside the tunnel
می‌توانید DNS دلخواه خودتان را وارد کنید.
مثال:
8.8.8.8
,
1.1.1.1
اگر خالی بگذارید، DNS پیش‌فرض موتور استفاده می‌شود.
آدرس‌های نامعتبر نیز به‌صورت خودکار نادیده گرفته می‌شوند.
🔹
اتصال تونل از طریق یک پروکسی دیگر
گزینه:
Dial out through a proxy
این قابلیت یکی از مواردی بود که کاربران زیادی درخواست کرده بودند.
اگر ابزار دیگری روی گوشی شما در حالت پروکسی فعال است، مثلاً
Psiphon
، می‌توانید اتصال WhiteAesther را از داخل آن عبور دهید.
مسیر اتصال به این شکل می‌شود:
گوشی ← WhiteAesther ← Psiphon ← اینترنت
برای مثال اگر پروکسی SOCKS روی پورت ۱۰۸۰ فعال باشد، وارد کنید:
socks5://127.0.0.1:1080
پورت را باید با پورت واقعی برنامه پروکسی خودتان جایگزین کنید.
پروکسی HTTP نیز پشتیبانی می‌شود:
http://127.0.0.1:8080
🔹
تنظیم WireGuard Keepalive
این گزینه می‌تواند روی مصرف باتری تأثیر داشته باشد.
سه مقدار قابل انتخاب است:
▫️
۵ ثانیه
▫️
۱۵ ثانیه
▫️
۲۵ ثانیه
مقدار پیش‌فرض در نسخه جدید
۲۵ ثانیه
است. در نسخه‌های قبلی مقدار پیش‌فرض ۵ ثانیه بود.
هر بار که این زمان می‌گذرد، گوشی یک بسته کوچک ارسال می‌کند تا اتصال فعال بماند.
در حالت ۵ ثانیه، این کار بسیار بیشتر انجام می‌شود و مخصوصاً روی اینترنت موبایل می‌تواند باعث مصرف بیشتر باتری شود.
مقدار ۲۵ ثانیه نیز مقدار رایج استاندارد WireGuard است.
⚠️
اگر بعد از آپدیت متوجه شدید اتصال WireGuard بعد از چند دقیقه بی‌کاری قطع می‌شود، مقدار را دوباره روی
۵ ثانیه
قرار دهید.
🔹
جایگزینی هویت ردشده
گزینه:
Replace a refused identity
این گزینه به‌صورت پیش‌فرض روشن است.
اگر Cloudflare هویت ذخیره‌شده روی گوشی را دیگر قبول نکند، برنامه به‌صورت خودکار یک هویت جدید دریافت می‌کند.
بدون این قابلیت ممکن است تونل ظاهراً متصل شود، اما هیچ ترافیکی از آن عبور نکند.
📌
خلاصه محل تنظیمات
بخش
Routes
▫️
Protocol
— مثل قبل
▫️
Endpoint
— مثل قبل
▫️
Exit chain
— مثل قبل
▫️
Routing rules
—
جدید
بخش
Traffic ← Advanced
▫️
Obfuscation
— مثل قبل
▫️
Local proxy port
— مثل قبل
▫️
Share with this network
— مثل قبل
▫️
DNS inside the tunnel
—
جدید
▫️
Dial out through a proxy
—
جدید
▫️
WireGuard keepalive
—
جدید
▫️
Block traffic if the tunnel fails
—
جدید
▫️
Match rules on domain names
—
جدید
▫️
Replace a refused identity
—
جدید
⬇️
دانلود آخرین نسخه
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
— مناسب تقریباً همه گوشی‌های سال ۲۰۱۷ به بعد؛
اول این نسخه را امتحان کنید.
▫️
armeabi-v7a
— مخصوص گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید؛ حجم این نسخه تقریباً سه برابر است.
اگر با مشکلی مواجه شدید، از مسیر زیر گزارش بگیرید:
Settings ← Diagnostics
و برای ما ارسال کنید.
@whitedns</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/whitedns/1634" target="_blank">📅 19:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1632">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gij49MPc6pmeG3w4N35fR9ck1QjS8jqEJUfUGch7gilfatlaPOBkjc0HDxO02ckb3tJAjbhHGZy_b1yeI6Qa6ZXhYq-t8wvZj7ubUjIV3VohugtC5vr-eYrIhCKnV8ByMGUZHmrShlOJUQaRWpdQXSlBDn4Zn_cjQL7KLtlw1eIPT9zfm-we96TB28iphL6ZAy7Njwe8KMRuF8tYzmo0Vi-lO6XN211r8zYkAO6SN5PgrRnIsPffZmVTTvE471Sl3OAsoO8pEG8apBwgWRp594BxU7NvCD-pJ2lZ9sw-n6tFTdtadA_XqKnhmemX2AQWn_uD83TQ2Ux5MAQjs98h8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
به‌زودی:  WhiteAesther  اندروید نسخه ۱.۲.۳
🔥
🔥
🔥
▫️
قفل ایمنی (Kill switch) — اگه تونل بمیره، ترافیک بی‌صدا لو نمی‌ره
▫️
قواعد مسیریابی — بگین کدوم سایت‌ها بدون تونل باز بشن (بانک، اپ‌های داخلی)
▫️
اتصال یه پروکسی دیگه (مثل سایفون)
▫️
امکان DNS دلخواه داخل تونل (برای کاهش پینگ)
▫️
بهینه‌سازی مصرف باتری روی WireGuard
@whitedns</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1632" target="_blank">📅 16:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1631">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mWJN3rkwb9JiDFEvmQbn-SzTVC4y9FBL5ahUw37PATkNypIRMwINn5es5R94TAma2YS4hZI_6zStXWHRbUbKwLT68e_e47w7QOwLyqhtoE31PxfBLPKratCUZhvQsXxBDxJQ2oEmzKWCHM4iTXgJ25r7272JjRaMWlQ5aMKUxHVU2i7jAmD6UgqL8Rc81T92WazR8Q5QMv81XelJPc5Y7da04Rjy1vGDJYGEt3YjOJQtHVWZcuqJAzYNkX7oHltPeirrYZcljzZgwZh81BbmBo2FOmx7hzaXFwYRBCdT4Y8jmPFv8sbc0DqzQEwPqXVfiG1QZOdHDp-pzCjBwsykkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/whitedns/1631" target="_blank">📅 10:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1630">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jagEny_twK9CVbyHwuGhJJrPbcWhk_wTekcvToeHHgYjTM9iymbR2PaMglaJCeY0jNNWb62DRbcagb75C6eo4AvC_gSSVTpUH4X6BIapT2jIFc0gy6WCvK68OZwI-qN1ePmLG0leLQ-kTMar1g-A43e9jelx4U9WedztogznF4FIPLhuiiNX3pq_S00MJzajKAbZqCfS_dGJHXoeNEAPk-bjNxxAusILGpqilCOHuS9TsrvbE6bbqKGocYkeQ7Sj1A3V7_uvLsnlu8mQaqHEgtFx7Dhxjafc3sqcpCwdaJWVI_9Dc0EkvRnsACieknmqn-6XU2TXU-W4flftcQKGfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/whitedns/1630" target="_blank">📅 10:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1627">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سابسکریپشن WhiteDNS برای اپ های WhiteVPN / Karing / Clash Mi / Clash Party / FLClash :
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
@whitedns</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1627" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1626">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">Live stream finished (1 hour)</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1626" target="_blank">📅 18:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1618">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmwD-wFbbgZPn7-_9LgFYQHDRWJuPYjIsJsveuKf1JajRgN2KB9ojdpUem63ftbM0rcer3oSf649zs4qUqgvP_2C3DSCa_Wv7zf_nWyar0dMQSNVDIoUBr0STaLILKleSJg8zssOEsk3cvpldNinU99FOhQ_4r09sVW4zqIMQ-7ygSlbbCZUnEP3QMCP3rNZPnqbeBqJni0FxqKGASUR6-hJqWR0MYW0wYnvwCEq5kPvyxWoJeLUzibnHELuCyeEXu7TfwjOk6G-4Fmij9pO77BTPHuZAxmMRkS4h8DUq_zoKsOBmGlz7gravWqro06177_BkeWsB5QS_E0-svAFXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
یک پورت برای حکومت بر همه!
آموزش نصب و راه‌اندازی CottenRouter
🇺🇦
تماشا در یوتیوب
https://youtu.be/N725_-A_-B8
اگر روی یک سرور چند DNS Tunnel مختلف داشته باشید، خیلی زود به یک مشکل می‌خورید: همه‌شون پورت عمومی 53 رو می‌خوان.
سرویس CottenRouter دقیقاً برای حل همین مشکل ساخته شده. جلوی تمام سرویس‌ها قرار می‌گیره، دامنه هر درخواست رو تشخیص می‌ده و بدون دست‌کاری Packet، اون رو به Backend درست می‌فرسته.
یعنی می‌تونید CottenDNS، MasterDnsVPN، StormDNS، thefeed و سرویس‌های مدیریت‌شده با SlipGate رو هم‌زمان روی یک سرور و یک IP اجرا کنید؛ بدون جنگ بر سر پورت 53.
✍️
توی این ویدیو می‌بینیم:
• سرویس CottenRouter دقیقاً چه مشکلی رو حل می‌کنه
• مسیریابی درخواست‌ها بر اساس Domain چطور انجام می‌شه
• چطور چند DNS Tunnel روی یک IP اجرا می‌شن
• پشتیبانی از DNS، DoT و HTTPS
• تفاوت نصب مستقیم با Docker
• پنل مانیتورینگ، محدودسازی ترافیک و قابلیت‌های امنیتی
• نحوه نصب و اتصال Backendها
سرویس CottenRouter هیچ Label یا داده اضافه‌ای وارد Packet نمی‌کنه؛ پس فضای قابل استفاده Tunnel و MTU رو هم کاهش نمی‌ده.
🇺🇦
تماشا در یوتیوب
https://youtu.be/N725_-A_-B8
🔗
سورس‌کد و راهنمای نصب:
https://github.com/TaJirax/CottenRouter
اگر با DNS Tunnelها کار می‌کنید، این پروژه احتمالاً کلی دردسر از مدیریت سرورتون کم می‌کنه.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/whitedns/1618" target="_blank">📅 15:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1616">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔭
یک خبر خوب برای کاربران WhiteVPN
🟢
یک فیلتر جدید به سابسکریپشن
اپلیکیشن ‌های
WhiteVPN اضافه کردیم تا کانفیگ‌هایی که هنگام استفاده از ChatGPT و سرویس‌های OpenAI خطا ایجاد می‌کردند، به‌صورت خودکار از لیست حذف شوند.
🟢
از این به بعد، با تمام کانفیگ‌های موجود در سابسکریپشن باید بتوانید بدون دردسر به ChatGPT و سایر سرویس‌های OpenAI دسترسی داشته باشید.
🟢
برای دریافت لیست جدید، کافی است سابسکریپشن WhiteVPN را یک‌بار به‌روزرسانی کنید.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1616" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1610">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/n9gNADhJLNRcQLPLI2USmn4tspI_7rqjpJgJhXz7z6lD6Q7wFqUNKgbUOHDTpTUOPKcGyOEdxBOG_35qMoYr95SxoFmfnrOLP3XFvocxZrFzQ8XduR2lQ6XCurSHeDVnXoQQYLr9HCVnvfQdu5WaliK-wjZFeyRF_sT2-SojHou09GmxkvKJuIAL-8c7_tf3nEs98mFsmq87qLMoqEb9PrX9M1YAMW1iQx3iXN8HUng8LZEAbhRl3SzwhkODFkKIIw1hiLUr5ziHvxfgrv0YIWRvizW5zBcbxmDhqalkVBUqARrn7HFMAeeB7bRCUWWgUeEkQ0rPUjNY8an4Awu9uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1610" target="_blank">📅 11:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1608">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">"exit chain "
⚠️
✍️
راهنمای استفاده از
#exit_chain
در اپ whitevpn# اندروید
ساب را وارد کن - برو تنظیمات - برو زنجیره اتصال - برو افزونه بعد - اشتراکی که وارد کردی را از اون بالا انتخاب کن - یک تست اتصال بگیر - یکی از کانفیگ ها را انتخاب کن - وصل شو -
تمام
✅
راهنمای استفاده از
#exit_chain
در اپ whiteaesther# اندروید
📱
برو route - گزینه exit chain را روشن کن - یا ساب و یا کانفیگ را وارد کن - برگرد صفحه اول و وصل شو -
تمام
✅
راهنمای استفاده از
#exit_chain
در اپ whiteaesther# دسکتاپ
برو advanced - برو exit chain - ساب و یا کانفیگ را وارد کن - برگرد simple - کانکت را بزن - تمام
✅
👨‍💻
این سه پست را مطالعه کنید :
https://t.me/whitedns/1601
https://t.me/c/3869114465/152008
https://t.me/c/3869114465/151806</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1608" target="_blank">📅 10:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1605">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VmOZtCSkD4ZRpUHtGlWyn2UBYQCj-RupE7J3eerbkAbZuRGV1_L1pD6qFIZw2VdXxtQNqoerGy-1qBDw7tKyK7Mzl48DUz79geLYW0Np9NR1DE65BJje3CXhZSsMUAhZqqzOwAYzPP3HtRffaavsDh9EmCqDe41Gq5wg9oh7pM86I_i38cZPkFh82VVUhN-hHuJkrReZAJpyDSke2GZ67GgxbBAIhQqzbOdrxhEuCWcoSWx-FwRzdB7tkQn9povuQIBxG-G3--rtrDCXfuik77fuRDVEOYyW7Xigv-4yGEi99RneP41HDDo--irgs7OZM9rtaKMogx7yxpX6ymxFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
Wh
iteAesther
✍️
نسخه ۱.۲.۲  برای اندروید منتشر شد !
— موتور جدید و چند قابلیت
این آپدیت موتور تونل رو عوض می‌کنه و چند چیزی که کاربرها خواسته بودن اضافه می‌شه.
🟢
⚡️
موتور جدید (Aether 1.7.0)
▫️
مصرف حافظه محدود شد
— قبلاً هرچی اتصال طولانی‌تر می‌شد، حافظه‌ای که اپ می‌گرفت بیشتر می‌شد تا جایی که تونل می‌افتاد. حالا سقف داره.
▫️
WARP in WARP وقتی یک طرفش قطع بشه دوباره وصل می‌شه
به‌جای اینکه کلاً بمیره.
▫️
پیام خطای واقعی از Cloudflare
— اگه ثبت‌نام رد بشه، حالا می‌گه دلیلش چیه: آی‌پی علامت‌خورده، یا ثبت‌نام زیاد از این آدرس. قبلاً فقط می‌گفت شبکه مشکل داره.
✍️
نودهای hysteria2 و tuic توی Exit chain کار می‌کنن
اگه توی ساب‌تون نود hysteria2 یا tuic دارین و تا حالا هیچ‌وقت بالا نمی‌اومدن، دلیلش پیدا شد و درست شد.
✍️
ولی یک شرط داره:
باید پروتکل رو روی
WireGuard
بذارین (از
Routes ← Manual ← Protocol
).
روی MASQUE همچنان کار نمی‌کنه و این دست ما نیست — محدودیت خود Cloudflareست. اپ هم اگه ببینه روی MASQUE هستین بهتون می‌گه.
🟢
نودهای REALITY حالا مشخص می‌شن
اگه توی ساب‌تون نود REALITY دارین، قبلاً یا اصلاً نمی‌اومد یا می‌اومد و وصل نمی‌شد و معلوم نبود چرا. حالا با برچسب نارنجی
not supported
نشون داده می‌شه و قابل انتخاب نیست.
نود سالمه — موتور فعلی هنوز نمی‌تونه باهاش احراز هویت کنه. وقتی بتونه، خودبه‌خود دوباره کار می‌کنه.
🟢
اشتراک تونل با شبکه (LAN sharing)
می‌تونین تونل گوشی رو با بقیه دستگاه‌های همون وای‌فای به اشتراک بذارین — مثلاً لپ‌تاپ یا تلویزیون.
از
Traffic
حالت رو روی
Proxy
بذارین، بعد بخش Advanced رو باز کنین و
Share with this network
رو روشن کنین. اپ آدرسی که باید توی دستگاه دوم بزنین رو بهتون نشون می‌ده.
⚠️
رمز اختیاریه ولی حواستون باشه:
بدون رمز، هرکی روی اون وای‌فای باشه می‌تونه از تونل شما استفاده کنه و ترافیکش با هویت شما بیرون می‌ره. روی شبکه خونه خودتون مشکلی نیست؛ توی کافه و هتل و خوابگاه حتماً رمز بذارین.
🟢
صفحه اول: آی‌پی و مصرف
•
آی‌پی قبل و بعد از تونل
— که ببینین واقعاً عوض شده
•
سرعت لحظه‌ای دانلود و آپلود
و مجموع مصرف هر نشست
نکته: آی‌پی «بدون تونل» فقط وقتی خونده می‌شه که اپ باز باشه و وصل
نباشین
. اگه مستقیم بزنین connect، اون خونه خالی می‌مونه — این عمدیه، چون خوندنش وسط اتصال یعنی فرستادن آدرس واقعی‌تون از کنار همون تونلی که قراره مخفی‌ش کنه.
🟢
کلید روشن/خاموش توی پنل سریع
از
Settings
دکمه
Add a quick settings tile
رو بزنین. بعدش از پنل بالای گوشی بدون باز کردن اپ وصل و قطع می‌شین.
🟢
مشکل «Allow background running» که نمی‌رفت
روی بعضی گوشی‌ها (مخصوصاً شیائومی) هرچی اجازه می‌دادین، اون کارت باز هم می‌موند. دلیلش این بود که این گوشی‌ها تنظیم باتری خودشون رو دارن و اجازه رو فقط اونجا ثبت می‌کنن، ولی جواب استاندارد اندروید همچنان «نه» می‌مونه.
حالا اپ خودش می‌فهمه این اتفاق افتاده، شما رو می‌فرسته به تنظیمات درست گوشی، و یک دکمه
I've done this
داره که کارت رو ببنده.
📥
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
(۵۴ مگ) — تقریباً همه گوشی‌های ۲۰۱۷ به بعد. از این شروع کنین
▫️
armeabi-v7a
(۴۸ مگ) — گوشی‌های قدیمی‌تر
▫️
universal
(۱۵۷ مگ) — اگه مطمئن نیستین
اگه مشکلی خوردین، از
Settings ← Diagnostics
گزارش بگیرین و بفرستین.
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/whitedns/1605" target="_blank">📅 08:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1603">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tAiAouyS8JqLY42fA70doI3zhWsaJFuF5GF0b-GhfVkQl-IgAyEc_wBYd0sH2vStllDZZWhmJaw7arkjhPSTrTRr85Ic62RkMqvwbsdQjNsmKi1ABGhgVosbn6hu5IbdFjpuhZkQyTbVygfe2tHcGcio5V-YJHOpo-SZU2Wbu0bGzl-uqWJUh4vtx5M6Ml0QyTAvPaSu7j8ZweC43gpFudxsD9cT3bRtBhjRjVl5Alny4CDaEByF-6o90QQoAL9v-kNeBSfWn2nwGSAtFhFI-86K8uHlYn1NaoJjs4f7KhUSRVQual7ebjnE6_gnRzC-aFCNstomy-08mjbjawOBrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
آپ
دیت جدید وایت‌استر برای دسکتاپ (WhiteAesther) منتشر شد!
نسخه:
v1.5.4
در این نسخه تغییرات بسیار جذاب و کاربردی برای راحتی بیشتر شما به برنامه اضافه شده است.
🔭
تغییرات این نسخه:
🟢
اشتراک‌گذاری اتصال در شبکه داخلی (LAN Share)
از این پس می‌توانید اتصال VPN فعال روی سیستم خود را به راحتی با سایر دستگاه‌های متصل به مودم یا شبکه (مثل گوشی موبایل، تلویزیون هوشمند یا لپ‌تاپ‌های دیگر) به اشتراک بگذارید!
🟢
نمایش هوشمند وضعیت گره‌ها (پشتیبانی بهتر از Node ها)
مشکل عدم نمایش وضعیت یا کار نکردن بی‌دلیل گره‌ها برطرف شد. حالا گره‌هایی که برنامه به هر دلیلی نمی‌تواند از آن‌ها استفاده کند (مثلاً نیاز به WireGuard دارند یا از پروتکل REALITY پشتیبانی نمی‌کنند) با
رنگ نارنجی
مشخص می‌شوند. با نگه‌داشتن نشانگر موس روی آن‌ها، می‌توانید دلیل دقیق عدم پشتیبانی را ببینید.
🟢
بهبود مسیریابی کل سیستم (Whole Machine)
(تغییرات نسخه 1.5.3)
حالت System Proxy حالا به درستی ترافیک کل سیستم را از طریق مسیر زنجیره‌ای فعال (Active Chain) شما عبور می‌دهد.
🔭
راهنمای استفاده از قابلیت LAN Share (اشتراک اینترنت با گوشی و
تلویزیون):
۱. در برنامه به بخش
Settings
(تنظیمات) بروید و تب
Traffic & DNS
را باز کنید.
۲. گزینه
"Share this connection on my network"
را فعال کنید.
۳. برنامه به شما یک
آدرس (IP)
و یک
پورت
(مثلاً 1080) نمایش می‌دهد.
۴.
امنیت اتصال:
در همین بخش می‌توانید یک
نام کاربری (Username)
و
رمز عبور (Password)
تعیین کنید تا فقط خودتان بتوانید به آن وصل شوید.
(
⚠️
توجه: اگر این دو کادر را خالی بگذارید، هر دستگاهی در شبکه وای‌فای شما می‌تواند بدون رمز از اینترنت آزاد سیستم شما استفاده کند).
۴. حالا وارد تنظیمات پروکسی (HTTP یا SOCKS5) در گوشی، تلگرام یا تلویزیون خود شوید، آی‌پی و پورت نمایش داده شده را وارد کنید و روی اتصال ضربه بزنید.
(نکته: در اولین استفاده از این قابلیت، فایروال ویندوز از شما یک تاییدیه می‌خواهد که باید روی گزینه
Allow Access
کلیک کنید تا پورت شبکه باز شود).
✍️
هم‌اکنون می‌توانید برنامه خود را به آخرین نسخه به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteAesther/releases/latest
#آپدیت
#وایت_استر
#WhiteAesther
#پروکسی
#تونل
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1603" target="_blank">📅 07:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1602">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gXemKJL3lE668GG4ZfkiEVCg6fhy3QG0wnoEiySUpBtJQ-SRH7ZezD2hHyBAAUsICkre2U-X8VC8tXkdaqnmRKi18Y1kVGKCzBXsV-BZfMA4C59oGMI3HID2n5i-qXW96-L-n_T4-zRV1yfpbmUwa0YDrLadrk788Y91M505dIvG5IUxK56HmHJXlXXX7fZS539I9OmM0FGfI1wLoAl1BqcwNpYOjsu4WuOsiQYoica2LSpG1NFJ9goVpWRddyxBnFkDpyUkhu1Dn5Dwc_kbQhagM8vquwADH9N2zlr_GtYgQSMr2xToX9ckF-vmkKat7vpXLl_p-zWBURvT4GTxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
نسخه جدید موبایل و دسکتاپ به زودی منتشر می‌شود!
این نسخه‌ها شامل چه مواردی است؟
🟢
بهبود عملکرد اتصال برنامه
🟢
ارتقا موتور به ۱.۷.۰
🟢
اضافه کردن امکان LAN sharing
🟢
رفع باگ
🟢
در اندروید امکان اضافه شدن به Quick setting
🟢
استفاده از wireguard و hysteria exit chain برای داشتن حداکثر سرعت
ممنون
@WhiteDNS
🔥</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1602" target="_blank">📅 19:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1601">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/MSe9xQXL93swqq6rk8CNLGjgPffPcFyVIHPhpMM2k90EF8ndQf9m-Rp1RuZc2Eu-p7f0hRRMbb9AfhmiXDDqMO5vhvJfDWcr4KCcYHWbA73x73CV1ABIk6L11QQdqGhoKnpogR6mKG1KBs1H5NE1m64yYKx0o95s7-tmT8RzitpZySvfXXVeCiFZsO8_H_PEaLGxXDdZyXZrw0vPEElp-aASl_GGODS8p_x-QTtX_hOu0KDKpK3LuAM_lj0o0HasUN9P8pbaYauv8wcrnxwhdtkuofpvlfKvCFHi2mACdI169mAGQU-19B8Iy5FPdyK-9cgN-vFAGgGc5oSRoR5bRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم
⚠️
⚠️
⚠️
⚠️
⚠️
دوستان :
پست  را با دقت مطالعه کنید
https://t.me/whitedns/1568
این کانفیگ های برای قابلیت "exit chain" توی اپ whiteaester و whitevpn هست - که ip شما را ثابت میکنه و یک لایه امنیت بیشتر به شما میده چون TLS هست
چون خیلی از دوستان کانفیگ نداشتن و یا نگران امنیتشون بودند ما این امکان را فراهم کردیم .
این کانفیگ ها برای استفاده مستقیم در اپ هایی مثل v2rayng و غیره نیست، اگر قصد استفاده مستقیم دارید لطفاً درخواست ارسال نفرمایید
تشکر
@whitedns</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/whitedns/1601" target="_blank">📅 17:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1600">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/nkjEC2KjT7rvdf71nVXUs6ymTxCfN5Nmu1xvkQwp-gaSt6OdOb7TvrY3hMQbNMB4ShsJlYAioWKCCO7edqCbKIDKbdMeTgx-kmwB-gU84AvN4u9il9kFqgi4w6PY0DGeoxHB1EwzLzdwAYE9-udsUYG_wBAonXHHdKsMfbjRkLec0IpWlIDf70wYttLHTqAcY6E6OKIOAYY8AmPJ8OestQQirf4t1bGITk3UHKKkJB5qydc3nys6FZ1cFJtM0t-QnJEtFYRAv49FjIpEdW-PG7BEYUZpqLQ6tWwWvFJVLyq37Oqe--B0BDdVeTDbbj_loRoxfhWibhhyWsOS9IiGAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/whitedns/1600" target="_blank">📅 17:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1599">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMasterDnsVPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1ZRTyymXdHHaLkwCAIDx1C24e6j8huNGJzlHt2v1YrkcDAIlbXU7QH8TJ6oL4iwm-DKCBABM31Ugaa1TCIhthBbliUV2KN9ZIGbiUL9xYX6RJhtxAmq9_8Z3VwKv8YkKcTySrqI4UmqBfn_hzzmCgaWsE7nycPK7R4YacnJGg1rwnESQHmE4c7GEcDH56vegxluu-hDedroucrFqRXj1q2iWT-BbzVv0-PrYe70o5clgF2Am8268fR261anVZWw5itmbqGR3lcGrHU3m1ZX9Aq0v7dncW_AhKyMsISllpgSn0PfV-AVg82ysw7t8GP-KiU3sMiWijmcu7YiaBHiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👋
درود،
◀️
آموزش رفع مشکل خطای
Sign-in failed: failed to start login server: An attempt was made to access a socket in a way forbidden by its access permissions. (os error 10013)
مربوط به برنامه ChatGPT در ویندوز
◀️
ابتدا در منوی استارت خود کلمه cmd را سرچ کنید.
◀️
سپس روی آن راست کلیک و Run as Administrator را بزنید.
◀️
در نهایت دستورات زیر را وارد کنید و Enter بزنید.
net stop winnat
net start winnat
✅
مشکل شما رفع میشود.
❤️
پیروز و سربلند باشید.
🤨
با تشکر فراوان،
امین محمودی
🗓
3 شهریور ماه 1405
🛡
کانال:
@MasterDnsVPN
💬
گروه:
@MasterDnsVPNGroup
#chatgpt
#هوش_مصنوعی
#رفع_مشکل</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1599" target="_blank">📅 16:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1598">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMasterDnsVPN</strong></div>
<div class="tg-text">👋
درود،
⚠️
یک پروژه هست، دوستان معرفی کردن، من تایید یا رد نمیکنم، فقط منتشر میکنم، خوب بودن و نبودنش با خودتون، من خیلی چک نکردم.
◀️
پروژه واسه جمع کردن کانفیگ های v2ray هست.
👩‍💻
0xRadikal/Free-v2ray-Configs
◀️
تفاوت اصلی پروژه با بقیه ریپوهای کانفیگ رایگان اینه که صرفاً کانفیگ‌ها رو از منابع مختلف جمع نمی‌کنه. کانفیگ‌ها وارد یک pipeline چندمرحله‌ای می‌شن، duplicateها حذف می‌شن، ساختار و endpoint بررسی می‌شه، اتصال TCP تست می‌شه و در نهایت کانفیگ با یک درخواست HTTP واقعی از طریق proxy در ۳ دور مستقل تست می‌شه.
◀️
در حال حاضر پروژه از ۲۱ منبع تغذیه می‌شه و در آخرین اجرای ثبت‌شده:
🔴
۱۱٬۴۱۵ کانفیگ یکتا جمع‌آوری شده
🔴
۲٬۴۰۳ کانفیگ در هر ۳ دور تست موفق بودن و وارد بخش
verified
شدن
🔴
خروجی‌های
verified
،
fast
،
secure
و
top100
تولید می‌شه
🔴
خروجی برای V2Ray/Xray، Clash و sing-box ارائه می‌شه
🔴
کل سیستم هر ۱۵ دقیقه به‌صورت خودکار به‌روزرسانی می‌شه
✅
به گفته ناشر: هدف پروژه اینه که این پروژه تبدیل به یک منبع متن‌باز و قابل‌اعتماد برای کانفیگ‌های رایگان بشه، مخصوصاً برای کاربران ایرانی.
🔴
نمونه همینکار رو هم WhiteDns انجام داده، اینجا میتونین ببینین:
👩‍💻
WhiteDNS/subs-check
🔴
اگر از این پروژه خوشتون اومد میتونین با
⭐️
دادن داخل گیت هاب از ناشر این برنامه حمایت کنین.
⚠️
نکته تکمیلی از سمت خودم: اگر از Vless/Vmess و هر فیلترشکن رایگانی استفاده میکنین، اگر امنیت اطلاعاتتون مهمه، حتما از حالت Chain و ... استفاده کنین، یعنی به وسیله اون VPN به یه VPN دیگه به سرور خودتون وصل بشید و Vmess/Vless سرور خودتون رو داشته باشید، از سرورهای رایگان برای فیلتر نشدن و ... استفاده کنین (البته که من کلا پیشنهاد میدم، VPN رایگان تا حد امکان استفاده نکنین و سرور خودتون رو راه اندازی کنین، اما این سرویس ها ممکنه، برای بعضی ها کاربردی باشه)، اما برای امنیت بیشتر اینکار رو انجام بدید.
❤️
پیروز و سربلند باشید.
🤨
با تشکر فراوان،
امین محمودی
🗓
1 شهریور ماه 1405
🛡
کانال:
@MasterDnsVPN
💬
گروه:
@MasterDnsVPNGroup
#v2ray
#معرفی_پروژه
#اینترنت_آزاد
#فیلترشکن
#vless
#vmess</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1598" target="_blank">📅 09:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1597">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rj8XrRYA9HnusPzIja8Y5B30PfeYeVdxIj-5AKzKHCwCLtUJocywP8WZCwHAN9TSPb-IJ34trYCbZHGzESwE2ZiG6PNcLtxvCX8JGLEL3RAHA3LUPvXBP6N8zJUDKZIW1YdRJmWGRsdtts8EYv0Lody-X4CmCY1OtFoPeSUvGMlRhvbdGwvCqmPm3Sicf4aLo3S3c2QBSLYVZyIoT1e38lQ2G-gQGNCYvoAlOOHNBaKBF8-K02BGqAca9Wwk5N7szAt50xYRVT8TyPnLNXXGaW_TWOmklC4ei4CcAilbzVpzr_PfJO1rnusY5TbIAuXK5_KnNEEJyiJRuKIbcNsA-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برای آیفون اپلیکیشن نداریم؟ چرا، داریم!
اگر از کاربران iOS هستید، می‌توانید از اپلیکیشن
Core Forge
استفاده کنید؛ یک اپلیکیشن کامل که سه قابلیت اصلی را یکجا در اختیارتان قرار می‌دهد:
🔹
اتصال VPN
🔹
استفاده از MasterDNS, CottonDNS
🔹
اتصال از طریق پروتکل Aesther
دیگر لازم نیست برای هرکدام از این قابلیت‌ها یک اپلیکیشن جدا نصب کنید؛ همه‌چیز داخل
Core Forge
در دسترس است.
📥
دریافت Core Forge برای iPhone
🎥
تماشا ویدیو آموزشی در یوتیوب
🔥
لینک ساب WhiteVPN برای استفاده در اپ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1597" target="_blank">📅 08:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1596">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">📹
آموزش اپلیکیشن WhiteVPN کامپیوتر و استفاده اپ داخل
🍏
آیفون برای کاربران IOS
https://youtu.be/tm0ls3r4ppw</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1596" target="_blank">📅 01:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1594">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔭
در ۳۰ روز گذشته، بیش از ۷۰۰ هزار اتصال موفق در اپلیکیشن WhiteVPN ثبت شده.
خوشحالیم که در این مسیر کنار شما هستیم.
🕊️
به امید روزی که همه به اینترنت آزاد دسترسی داشته باشیم و از WhiteVPN فقط برای حفظ امنیت و حریم خصوصی استفاده کنید، نه برای عبور از فیلترینگ.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1594" target="_blank">📅 14:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1593">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌎
انتشار نسخه ۱.۶.۲ WhiteDNS برای اندروید</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1593" target="_blank">📅 14:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1589">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.2-armeabi-v7a.apk</div>
  <div class="tg-doc-extra">34.2 MB</div>
</div>
<a href="https://t.me/whitedns/1589" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/1589" target="_blank">📅 14:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1588">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtgKppRzTAVrI8Oawbza4tKWSXZsoK6vaMCF01-7KsOgl53CD3FoA7xKNW2X_mEe-9-1N1I3iAC-b8bKb3NKwskKoyIdB5Qjmenz9f-qJF5OGj6GjLuYgTKtsJOSXgO11nDWdrRnC4iSadY9U3MXuCbgSV0B8-jpIg6xZJZD_GoWCTzCqItpXzmqVPM90EBNli0hMG2OxwbO1v4wEEL2b3bxGbkBFGgXLsVO2E_mwd_-FpEvhnlEQ_j0-N8Lspq1eZT65ClQBU-EOnEFbEqNgJ7AxRGTh0jwv-n4X_aMnkOMwlkYbiLEbFAPiXjJnG_4dsDGHy_LA6OJL5CUjkFAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
WhiteVPN 1.6.2
✍️
این نسخه اتصال WhiteVPN را سریع‌تر و پایدارتر می‌کند و چند بهبود مهم برای سابسکریپشن‌ها، تنظیمات و Split Tunneling دارد.
✍️
تغییرات مهم
• اتصال مجدد خودکار، سریع‌تر و قابل‌اعتمادتر شده است.
• در صورت بروز مشکل در اتصال، برنامه بهتر و امن‌تر آن را بازیابی می‌کند.
• بررسی سلامت اتصال و مدیریت تغییرات شبکه بهبود یافته است.
• هنگام قطع اتصال، وضعیت واقعی عملیات نمایش داده می‌شود و برنامه تا توقف کامل اتصال در حالت «در حال قطع اتصال» باقی می‌ماند.
• مدیریت و ذخیره‌سازی سابسکریپشن‌ها پایدارتر شده است.
• فایل‌های خراب سابسکریپشن به‌صورت خودکار شناسایی و دوباره دریافت می‌شوند.
• آخرین نسخه سالم سابسکریپشن برای مواقعی که دریافت نسخه جدید ممکن نیست، حفظ می‌شود.
• پشتیبانی از لینک‌ها و کانفیگ‌های SOCKS و SOCKS5 اضافه شده است.
• تنظیمات سابسکریپشن، زبان و ظاهر برنامه به بخش جدید «تنظیمات برنامه» منتقل شده‌اند.
• گزینه «بازنشانی تنظیمات» اضافه شده است؛ بدون حذف سابسکریپشن‌ها، نتایج تست‌ها یا قطع اتصال فعال.
• در بخش Split Tunneling اکنون تمام برنامه‌های نصب‌شده، حتی برنامه‌های بدون آیکون، نمایش داده می‌شوند.
• اسکرول فهرست برنامه‌ها در Split Tunneling اصلاح شده است.
• ذخیره نتایج تست اتصال و به‌روزرسانی صفحه سریع‌تر و روان‌تر شده است.
• حجم نسخه نهایی با حذف منابع اضافی کاهش یافته است.
📱
دانلود از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.2</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1588" target="_blank">📅 14:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1587">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✍️
دوستان، فعلاً سرور ساب WhiteVPN با یک مشکل فنی روبه‌رو شده و بچه‌ها در حال بررسی و برطرف کردنش هستن.  به‌محض اینکه مشکل حل بشه، ساب رو آپدیت می‌کنیم و همین‌جا بهتون خبر می‌دیم.  ممنون که صبورید و شرمنده بابت اختلالی که ممکنه براتون ایجاد شده باشه
🙏
فعلا…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1587" target="_blank">📅 13:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1584">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/c6njE3DiByctHaskvupZpNJyiibT6j92-pxdEPIgP92PW6gi-eOyv9Bf8Upw71ZarcTHNWS0Txk8lqj4RrX-vQZSvpPOhe_V9MbN9YTIHCDwvNRuEurI49szAGQdxCgvd-eHBVF9qaFGnULJxVs_Uhlrvny6q-funD0gsE1A7exS-7QZz4VaUdj5XaqHboifzFAE4HV_8ZUCStkl5KtDxLgCbIVNNSzmoxvvb2EIK4g0I4g3FoBssqz-JF3EhDn4XBVVlajJ4FOyghv4-XLMxs2kZv4d6b8zGD459UpHqkyol6ITXUObIwvd_nvDP2HJP3l3Jec6WH8Pv_xegmrsOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم
⚠️
⚠️
⚠️
⚠️
⚠️
دوستان :
پست  را با دقت مطالعه کنید
https://t.me/whitedns/1568
این کانفیگ های برای قابلیت "exit chain" توی اپ whiteaester و whitevpn هست - که ip شما را ثابت میکنه و یک لایه امنیت بیشتر به شما میده چون TLS هست
چون خیلی از دوستان کانفیگ نداشتن و یا نگران امنیتشون بودند ما این امکان را فراهم کردیم .
این کانفیگ ها برای استفاده مستقیم در اپ هایی مثل v2rayng و غیره نیست، اگر قصد استفاده مستقیم دارید لطفاً درخواست ارسال نفرمایید
تشکر
@whitedns</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/whitedns/1584" target="_blank">📅 11:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1582">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✍️
دوستان، فعلاً سرور ساب WhiteVPN با یک مشکل فنی روبه‌رو شده و بچه‌ها در حال بررسی و برطرف کردنش هستن.
به‌محض اینکه مشکل حل بشه، ساب رو آپدیت می‌کنیم و همین‌جا بهتون خبر می‌دیم.
ممنون که صبورید و شرمنده بابت اختلالی که ممکنه براتون ایجاد شده باشه
🙏
فعلا از ساب موقت استفاده کنید تا اون مشکل حل بشه
https://ns1.rmft.tech/top300/sub
https://raw.githubusercontent.com/paranoideveloper/CoreForge-Sub/main/subscription_base64.txt
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1582" target="_blank">📅 07:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1581">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WTMNmYgVWM_fquBSbKDOTQQ2Cy8Yvb9VXNOIa2kVfSqosJq6zWY-m2VZ-DtZGzOh9_7KbrmXbLYGU57o4Hp2VXtBi9ipUkdqutRkyQRUE6EsSF1VU2999yX1Z0qALli7waQLxsKyeM8FOQAtK3jEPAzKgQbsyiH84PHOiD5CF_iWzT1cWSiaCUgBn-UaDV8J_poNHYO1Ov9wxBfBsV8SLB_YSsijpW3p4do7CrOV4vXah2XqNAb1JIQS2nDpNYm70eniWvZY1fVQoSI-2nEsdit1HmJu3QOzcAeT0DRJAIN-Anp3gpyPAwXdR6ey8nhA5roiCCy3KO6q2UvXU66qjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/whitedns/1581" target="_blank">📅 06:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1580">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CvXl0CLvumXRLBzypsSKSqzzIwW8tvZRl9oxvIqSYgLM2_OxzpEAzez3CNh973Fo1h89_1acSJY271vRGgMi24WeR5zASUmX5XA7VMz2NrXWgrMFPUJ1juc-NGROLNJPlQMH39-tJYDmVzS59YBAk8mXe1eOJCFa3h_nhe2E3OwEqJ1Ljzx4voC2jAEEYPIdlQKfTy6dV1jF6hU6clWGjyymP9iBxG8eAhpbZ5Ey84_zcETmZ3TnUBJYyZ2sQptaDwmdJddfNU3EA95t6irRNDIsOU6crSu_Tx6jQPSVhcyKMJMitqn2ZwTjRAjDXB7eJa246C4f-QIMANEhP1hdsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/whitedns/1580" target="_blank">📅 06:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1579">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/M0br-CbNjvNhhmRf46cRJ9fNaNagJXrOae1oUmkDVPYQYdCzFnmGWhH184ujqGoMxqYVjKvxIxM2Gx1lw5UZBqwFeMkcPxyYJ7ekajqM-PG21X95jYF_WPiHeSGHG1IrvMcwSj16J7VBcAfaLkObPzaYeHNlEAmC0_o2789-1PYL-wjRU7BbZJW0fIGe_MZkJ47MdA6ytN4L0jXD6O-RoEKBlhmg7q0kS9u1C6rDRjGd_W2TGgRYZ3O6V-3QpvV_eb9yiKIJHBxfhpiluxD35dcozNN0DCXGs7IgmAWRUXkQkv9WDkx5C4MY3oBF9WNt_iCmCReIoVlVXMGo4_o2qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم
⚠️
⚠️
⚠️
⚠️
⚠️
دوستان :
پست  را با دقت مطالعه کنید
https://t.me/whitedns/1568
این کانفیگ های برای قابلیت "exit chain" توی اپ whiteaester و whitevpn هست - که ip شما را ثابت میکنه و یک لایه امنیت بیشتر به شما میده چون TLS هست
چون خیلی از دوستان کانفیگ نداشتن و یا نگران امنیتشون بودند ما این امکان را فراهم کردیم .
این کانفیگ ها برای استفاده مستقیم در اپ هایی مثل v2rayng و غیره نیست، اگر قصد استفاده مستقیم دارید لطفاً درخواست ارسال نفرمایید
تشکر
@whitedns</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/1579" target="_blank">📅 22:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1577">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">📹
آموزش اپلیکیشن WhiteVPN کامپیوتر و استفاده اپ داخل
🍏
آیفون برای کاربران IOS
https://youtu.be/tm0ls3r4ppw</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1577" target="_blank">📅 17:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1576">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLordofCinder</strong></div>
<div class="tg-text">🚀
بالاخره ‎CottenRouter‎ منتشر شد!
چیزی که خیلی‌هاتون بارها درخواست کرده بودید، بالاخره آماده شد.
🔥
اگه روی یک ‎VPS‎ چند ‎DNS Tunnel‎ دارید، دیگه لازم نیست برای ‎Port 53‎ بین سرویس‌ها درگیر باشید.
‎CottenRouter‎ امکان اجرای چند ‎Tunnel‎ روی
یک ‎IP‎ و یک ‎Port 53‎
رو فراهم می‌کنه و هر ‎Domain‎ رو به ‎Backend‎ مربوط به خودش هدایت می‌کنه.
⚡️
پشتیبانی از:
‎CottenDNS‎
‎MasterDnsVPN‎
‎StormDNS‎
‎thefeed‎
‎SlipGate‎
🛠
امکانات:
• ‎UDP / TCP‎
• ‎Multi-Domain‎ و ‎Multi-Backend‎
• ‎Port 53‎ بین چند ‎Tunnel‎
• ‎DoT‎، ‎DoH‎ و ‎HTTPS‎ بر اساس ‎SNI‎
• ‎TUI‎ و ‎Control Deck‎ برای مدیریت و مانیتورینگ
• نصب مستقیم روی ‎Linux‎
• پشتیبانی از ‎Docker‎
• ‎AMD64‎ و ‎ARM64‎
🛡
بدون دستکاری ترافیک ‎Tunnel‎
‎CottenRouter‎ چیزی به پکت ها و تانل اضافه نمیکنه
بنابراین قابلیت‌هایی مثل ‎ARQ‎، ‎FEC‎، ‎Compression‎، ‎MTU Discovery‎، ‎Record Channels‎، ‎SOCKS‎ و ‎TCP Forwarding‎ بدون تغییر باقی می‌مونن.
🔥
خلاصه:
یک ‎IP‎ + یک ‎Port 53‎ + چند ‎DNS Tunnel‎
🔗
‎GitHub‎:
https://github.com/TaJirax/CottenRouter</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/whitedns/1576" target="_blank">📅 15:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1570">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/u_EhqCOG4TrK8ofMGc-QaI87DMTSyNTQMM-JPgVj-ERFhnkuw3RlWo6de_alRQ6Xb80gU1f4Qeny9Uw7hPnhu6_IZ3uWcbYybPe_MEZKJZyIwmzxpvGfJeDt0a6ZqV8OrPWOshtWESIeNaXDbWzLEtBbB7NgDq3tFqXfCYugunA8ENoN0X89USL994TydCsx_xa9hcbBHqmfmNk-pN58m0z-aM_fyfEw7YVEBdcHG-hqUnPqjfgjKWkVnOdNyVKrvmASYajvvQnSmtw7o1JW7hegUBFE9MPhlSnzBiLAmYES0l55dFtuR2CbqrD24p1Ds1cmQIUcCcnRqiPjs_P9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقت :
یک سوال خودمونی :
تا الان نزدیک 50 نفر کانفیگ دریافت کردن
چرا حتی به خودشون زحمت ندادند یک لایک کنند ؟
این فرهنگ عجیب از کجا اومده ؟
اون لایکی که شما میکنید یک انرژی برای این تیم هست که شما دریغ میکنید .
😏</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1570" target="_blank">📅 06:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1568">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mv05ZFRBJMSWGUblnMhjeBIzjjFmlpz-yRYpFMPl_9_zy7X9kzNfyaf1lTLYxhlEKW6rCY1z4ISBa3-6TfcB47JZGyCL-iSezK5UBubBlbwbwPOpVHskBrIDhhJDnrqPf_gUSrF6Vo-2QGtOQssOQhrchqgq4zcn9QK1TlONLOQwnXoRpKdooQe6yDjTlagjM8sA2dxvyo6GBuWg2LpAYRfOBxpqLGF__ngEy5R1iRh2g_QALa1fg22VNnMfzDq4qenQ2ms7e0827mGRoVyU10hGMdWHVr5JCzZeY-98Z7xmIadEyffrTDrq6Q4aUK3O6Uq9f4_hGZPeLlvww71PFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/whitedns/1568" target="_blank">📅 05:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1567">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد
PattNG
/
PattN
کرده و لذت ببرید !
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt
ساب هر ۲۴ ساعت آپدیت میشود.
///
توضیحات:
چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری و تست میکنند و سپس کانفیگهای سالم را فیلتر و در اختیار قرار میدهند پروژه‌ها‌ی
https://github.com/0xRadikal/Free-v2ray-Configs
و
https://github.com/itsyebekhe/PSG
و
https://github.com/Delta-Kronecker/V2ray-Config
هستند.
اما این پروژه‌ها دو مشکل اساسی دارند، اول اینکه تست کانفیگها باید از طریق اینترنت و فایروال ایران انجام شود ولی در حال حاضر تست کانفیگها در این پروژه‌ها از طریق گیتهاب انجام میشود، دوم اینکه روی نت‌های آپلود محدود (ایرانسل و ...) عملا اکثر کانفیگهای این پروژه‌ها آپلود محدود هستند و کیفیت بسیار پایینی دارند.
از آنجا که با روشهای زیادی میتوان محدودیت آپلود را روی کلودفلر دور زد، من در پروژه‌ی خودم اومدم کانفیگهای کلودفلر سالم را از پروژه‌ها‌ی اصلی جدا کردم و تغییراتی را برای دور زدن محدودیت آپلود (و همچنین دور زدن فیلتر دامنه) اعمال کردم (در حال حاضر متد fragment+fingerprint اعمال شده). بنابراین کانفیگهای نهایی سالم و با حداکثر سرعت در تمامی نتها قابل استفاده هستند.
برای دور زدن محدودیت آپلود در نتهای آپلود محدود در حال حاضر فقط باید از کلاینت
PattNG
/
PattN
استفاده کنید، بزودی در سایر کلاینتها نیز این مورد پشتیبانی میشود.
https://github.com/patterniha/Free-Configs</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/whitedns/1567" target="_blank">📅 03:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1566">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyThTW1aPYpz61AlxABJ9ix8gE3brXCNktshPK6l8RclegrwfwnIY8ckBlhbq3yisB9gjex_Ngr0dmcVkcCe7NHTehKLCqat9jrQmUOcBtPlpo4WEZOJS5BSteF4BgVPtNA8gWst03S4juO46j5AqwS5Cpb4VptfoCL3VMOd4RkjrjMg9uX6lp1hd9TrwJP8oAxLKj9skwzpgbKavfR1VnYDzspKNozYPTblgL8dy_4eO8pBpzDxXyA-LknnAECAc6l4mvYyA98SNGwJ-VvuYqJ589GRbxgqad6rFOxtjPlOhkxc9V_BPIq2GMNk7nqu14BlvGvl6npm3GVQn-HlHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
WhiteDNS
مسیری که قبل از روزهای قطعی اینترنت شروع شد
تیم WhiteDNS از مدت‌ها قبل از قطعی‌ها و محدودیت‌های گسترده اینترنت فعالیت می‌کرد. از همان ابتدا تلاش کردیم ابزارها، سرویس‌ها و آموزش‌هایی بسازیم که رایگان و در دسترس همه باشند.
در این مدت افراد زیادی به این جمع پیوستند؛ بعضی ماندند و بعضی مسیرشان جدا شد، اما چیزی که ما را کنار هم آورد همچنان پابرجاست:
حرکتی جمعی برای دسترسی آزادتر به اینترنت.
تیم WhiteDNS تا امروز کاملاً مستقل و بدون هیچ منبع درآمدی اداره شده و تمام هزینه‌ها را خودمان پرداخت کرده‌ایم. با این حال، این مسیر را ادامه می‌دهیم و همچنان ابزارها و سرویس‌های رایگان بیشتری را با کمک همین جامعه خواهیم ساخت.
حالا تنها مسیر درآمدی ما کانال یوتیوب WhiteDNS است. اگر می‌خواهید از این حرکت حمایت کنید، کانال را سابسکرایب کنید و ویدیوها را ببینید. همین همراهی کمک می‌کند WhiteDNS مستقل، فعال و جامعه‌محور باقی بماند.
📺
https://www.youtube.com/@WhiteDNS
ممنون که بخشی از این مسیر هستید
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/whitedns/1566" target="_blank">📅 18:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1564">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Y7RGBVDeBLzWlt219yorsxjc7uq_-lh4HWXOaYbceZcNtBFDNxjpYIh6axcExyq8Bpg4NtX7pI7Y1qkXQUHNtHzrJskN4crTkjl5DOV2tHJVfBJjVxLSBSG3Nj_psGpDYT5MFJkJwNq0wcy_xkAUhVekWcdtqSMHuFpVujwSa_8xwOkQfN4R6TekWxn56qtGqWWjEnpN1I2rSQTnzu82iQv1u23zYy3XMN5xXOg6c1jU1YoS6PKx-kPmwJlGBUTB2N1v5LyYh3BPN21Cnl-CTAOEzWTgEC3irQaorW9GTZJBlZ2iAPbNSdtvsbGqQGMEm8KqgkGqQNLoU7pR3cYWnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/whitedns/1564" target="_blank">📅 17:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1563">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/776e6fda95.mp4?token=mJ2OzkzRT7zo6N6BH602ksBGBTSNxeYs94G7VlwWNKHBI6mB5CJ3LfPTi5cAH2CHi4nJuZRYItH3ITFuv11fL4F18SY_ZiZ7MS-YMrxNElB9dfiglxJbWsBe7K-4iYC7bjFEIHUz_hwnKkDscVSglW2PsdgtpEBOv3oSax9zyBPgxrSGvG6sa9m9EAKGScoM-hmW2ikyUSO-_VxxAz4JW9UDNzpoj7bmAg6kyX1jGM7cUmidKsZqc52DBu6lXBeF0sTTgAItGBl6tMmUAXRBV9wTideoR1eK_erqTNgEVmiV0QlI2tBqMQD5zjjpIPnq4o4TXAT7XdIqNq1VX828rgKqiZQj9I6rC2IXsg_hjjJCyFRy40apYI78qZRl3LrM_JxrXXOhgOlmmG7fKvBqhY6l5b8dc2SaBcdnnBrMNyYOGfeKo1g7gT5tkeItBwIvH0o2OSpsUDSHnUAt8kK-nlElwFIfgTU9TRypxuEomVaO4pjxC5pGmkm79IDMa_s9yVYtG2AHBGIrZtRx4xQJbsJOfHkcoqJ6Pvi7gLMZUj7v4wE6bCtnMxFkUk9OkhG8zZShEMlM03ZxvefGG3ynrS6OkJPSj42Io_zjYoOCi3yADdOVZOt1L5HYuTaIVSwmKrg7r7pcrfVI9Mp4ZSFbRiggXMpHb40_2OmbgPip6qs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/776e6fda95.mp4?token=mJ2OzkzRT7zo6N6BH602ksBGBTSNxeYs94G7VlwWNKHBI6mB5CJ3LfPTi5cAH2CHi4nJuZRYItH3ITFuv11fL4F18SY_ZiZ7MS-YMrxNElB9dfiglxJbWsBe7K-4iYC7bjFEIHUz_hwnKkDscVSglW2PsdgtpEBOv3oSax9zyBPgxrSGvG6sa9m9EAKGScoM-hmW2ikyUSO-_VxxAz4JW9UDNzpoj7bmAg6kyX1jGM7cUmidKsZqc52DBu6lXBeF0sTTgAItGBl6tMmUAXRBV9wTideoR1eK_erqTNgEVmiV0QlI2tBqMQD5zjjpIPnq4o4TXAT7XdIqNq1VX828rgKqiZQj9I6rC2IXsg_hjjJCyFRy40apYI78qZRl3LrM_JxrXXOhgOlmmG7fKvBqhY6l5b8dc2SaBcdnnBrMNyYOGfeKo1g7gT5tkeItBwIvH0o2OSpsUDSHnUAt8kK-nlElwFIfgTU9TRypxuEomVaO4pjxC5pGmkm79IDMa_s9yVYtG2AHBGIrZtRx4xQJbsJOfHkcoqJ6Pvi7gLMZUj7v4wE6bCtnMxFkUk9OkhG8zZShEMlM03ZxvefGG3ynrS6OkJPSj42Io_zjYoOCi3yADdOVZOt1L5HYuTaIVSwmKrg7r7pcrfVI9Mp4ZSFbRiggXMpHb40_2OmbgPip6qs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یه آموزش خفن و کاملاً رایگان براتون داریم!
✨
اگه دوست دارید بدون هیچ هزینه‌ای با
پنل Netra
کانفیگ بسازید، این آموزش دقیقاً برای شماست!
💗
بدون هزینه
🎀
کاملاً رایگان
✨
آموزش مرحله‌به‌مرحله
🎥
آموزش کامل رو آماده کردیم و می‌تونید همین الان توی یوتیوب ببینید:
https://youtu.be/qluhGfGNbwk?si=oTLkVuC1z-5L03fy
💌
اگه آموزش براتون مفید بود، حتماً لایک کنید و برای دوستاتون هم بفرستید!
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/whitedns/1563" target="_blank">📅 15:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1560">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iLUxEX9RfsI8V3m-kX_TR0Qz6mP_zsJ_lNfwnqzgF8CfHFXQ2LFd21OXl3gK4JG6E59NPswvQ56mj_T0dxlELfnnah4Th0gb4H5L6sBNEzAZPyy06UVV87je6Rj4ufptdOmRu5oBgFHoBKSjJopMkAkndMK5qojhsjnSyCmjv0A2mOalMHzF27MODOxPLJt28sYdPxiBZT3c_BWY50h174mMAF9gbqlSHEULVYuaakBCj3R6Mb4-ObsVnAokOkqdlSBxytuJrHZnrf3bZFLk-Q1TD9dvmbIkbHb5T6Dqo9SzItz5yhXWtiygdh5FkjmECcWTAeDqG3s1_RF50Ej34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteVPN Desktop v1.0.18
زنجیره کردن اتصال (Connection Chaining)
از این نسخه می‌توانید ترافیک را قبل از رسیدن به اینترنت از دو سرور رد کنید.
اتصالی که در صفحهٔ وی‌پی‌ان انتخاب کرده‌اید هاپ اول می‌شود، و سروری که در تنظیمات به‌عنوان هاپ دوم انتخاب می‌کنید جایی است که ترافیک از آن خارج می‌شود.
چطور فعالش کنم؟ تنظیمات ← زنجیره کردن اتصال ← هاپ دوم
پیش‌فرض روی «خاموش — یک هاپ» است و اگر دست نزنید، همه چیز دقیقاً مثل قبل کار می‌کند.
چند نکته که خودِ برنامه رعایت می‌کند:
▪️
سرور هاپ دوم از فهرست هاپ اول حذف می‌شود، تا هر دو سرِ زنجیره یک ماشین نباشند و بی‌دلیل هزینهٔ دو هاپ را ندهید.
▪️
اگر هاپ دوم WireGuard یا Hysteria2 (یا هر پروتکل روی QUIC) باشد، فقط سرورهایی به‌عنوان هاپ اول پیشنهاد می‌شوند که بتوانند UDP را حمل کنند. زنجیره‌ای که هاپ اولش فقط TCP باشد ساخته می‌شود و وصل هم می‌شود، ولی هیچ ترافیکی رد نمی‌کند.
▪️
حالت Automatic همچنان کار می‌کند. اگر هاپ اول قطع شود، خودِ گروه جایگزینش می‌کند و نیازی به اتصال دوباره نیست.
▪️
اگر سروری که به‌عنوان هاپ دوم انتخاب کرده‌اید بعد از به‌روزرسانی اشتراک حذف شود، همان‌جا در تنظیمات به شما گفته می‌شود — نه وقتی که دارید وصل می‌شوید.
⚠️
توجه: دو هاپ طبیعتاً کندتر از یکی است، چون هر سرور باید ترافیک سرور بعدی را هم حمل کند. اگر سرعت برایتان مهم‌تر از لایهٔ اضافه است، همان یک هاپ را نگه دارید.
دانلود: ویندوز (x64 / ARM64) · مک (Intel / Apple Silicon) · لینوکس (deb / rpm / AppImage / tar.gz)
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/1560" target="_blank">📅 16:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1558">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GDa2PFJJvnO5DENrFJSMjY4WPtt6S8uKux9Lbw5WF2h1HGowVap9rGsdUnNlxKypYbhzyKCzy7o0X18y1Q-snD5vyhiZhcMjbPJuEw60pM6SfPpLRpBAvq67HVKvttqGSZmzOVsPXFqJpq9DpYl3vVGX7HYy90cFMjshQM-pH8y5mDdf5aY8leMDlEXCiyFXoUtO36qsQyIaaKa3HraUv60xZKYzOtnslm0VojQJbk1wOKXP6JRQJXqPuV1rd1oSV8XhPnzIkL581Amxb5ntl6Ix5NSHPXjnfW5CbY1GFLCOQxhbaHgfB80y1y4VfMA39ycJhGEBBWifyfju_mYgdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther Android ورژن جدید
🔥
🔥
🔥
🔥
🔥
نسخه ۱.۲.۱ — رفع سه مشکل اتصال
این نسخه قابلیت بزرگ جدیدی نداره؛ سه تا مشکل رو رفع می‌کنه که باعث می‌شد اپ روی خیلی از گوشی‌ها اصلاً وصل نشه. اگه ۱.۲.۰ داری حتماً آپدیت کن.
🛠
چی رفع شد
1
.پروتکل های wireguard و warp in warp برای خیلی از دوستان اصلاً وصل نمی‌شدن
توی ۱.۲.۰ «ثبت‌نام مشترک بین پروتکل‌ها» رو به‌عنوان یک بهبود اعلام کردیم. اون کار اشتباه بود: وقتی MASQUE هویت رو ثبت می‌کرد، کلید WireGuard روی سرور Cloudflare پاک می‌شد. بعدش هیچ اندپوینتی جواب نمی‌داد و اپ می‌گفت شبکه بسته‌ست — در حالی که مشکل از هویت بود، نه از شبکه.
حالا هر پروتکل هویت خودش رو داره. اگه از ۱.۲.۰ آپدیت کنی حسابت از دست نمی‌ره.
⚠️
در عوض، اون کاهش سه‌برابری احتمال rate limit هم برگشت. اگه زیاد نصب و حذف می‌کنی، حتماً از
Settings ← Identity & access
یک بار بکاپ هویت بگیر.
۲
. عوض کردن پروتکل وسط اتصال، همه‌چیز رو خراب می‌کرد
اگه بدون قطع کردن اتصال پروتکل رو عوض می‌کردی، جستجوی اندپوینت از داخل همون تونل قبلی رد می‌شد — یعنی هزاران درخواست دقیقاً به جایی می‌رفت که قرار بود جایگزینش کنه. نتیجه: هیچی وصل نمی‌شد.
۳
. گیر کردن روی پروتکلی که شبکه‌ات بسته
پیش‌فرض قبلی H3 بود که روی UDP کار می‌کنه. اگه شبکه UDP رو بسته بود تلاش اول شکست می‌خورد و اپ دوباره همون رو امتحان می‌کرد. تا نوبت MASQUE H2 برسه چهار دقیقه و نیم گذشته بود، و عملاً هیچ‌کس این‌قدر صبر نمی‌کنه.
✨
چی جدیده
حالت Automatic — از
Routes ← Manual ← Protocol
گزینه اول حالا Automatic هست و پیش‌فرض هم شده. خودش سریع امتحان می‌کنه ببینه شبکه‌ات چی رو اجازه می‌ده، از H2 شروع می‌کنه (چون TCP روی پورت ۴۴۳ هست و شبیه HTTPS معمولی دیده می‌شه)، و هرچی جواب داد رو یادش می‌مونه تا دفعه بعد از همون شروع کنه.
روی نصب تازه: ۱۴ ثانیه تا اتصال، جایی که قبلاً چند دقیقه طول می‌کشید.
گزارش خطای واقعی — قبلاً اگه جستجو نتیجه نمی‌داد فقط می‌نوشت «اندپوینتی پیدا نشد». حالا می‌گه چرا: بسته‌ها از گوشی خارج شدن و جوابی نیومد (مشکل از شبکه‌ست)، یا اصلاً خارج نشدن (مشکل از مسیریابی خود گوشیه). لاگ خود موتور تونل هم از این نسخه داخل
Settings ← Diagnostics
هست — اگه مشکلی خوردی همون گزارش رو بفرست.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/whitedns/1558" target="_blank">📅 14:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1557">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tXixXLWyS3kJU18lxoEfERgfCIaCa4EIql3Qg9Y3dh3IDgjAL-X0st0Ce2lJA-jtsExd26FcXtB2qZxXCYoxIh-vlHJKOfjX3UA0Zs8L7MG1r5ruZjfL1l54r4FjqniRH_cIW9OvcUgxB5MaUAxd9kPT7VJ9VDLOEXDTj8hN42A28uychvTEQYz5RunhnIE-fr-ce9sBvJYN3tk5nV8G3WiZtZD7qrPcbWwYegrtBWISutwuUGej6NDaoD_ry2VA2P8TQslQ7y0xU3R9rHHvfQ6b7JEbfYpL_3bQi5nzZ9U17DEyB_8Bt0jv-ghUOCUJxYWmPIGA69g3iDd6KVQE6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/whitedns/1557" target="_blank">📅 14:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1556">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ljMlDbZML35UrdM_NdPCZQ4JuonxtbxibDAxQWq5Qr_lkvLR-cJKHzQiuTVENH1nwS7ltbpEZlb_k9rIMFTo2zSNCkoGuJQmcg-poTyfh6SD8Tlv6nXzQvebFO4-aLmzfDIQDXd5jkT_XNgAjdOO_hawX_nJp_Y_QA0kl47DJQ9rwEBYRzjqXOTjG1GLoSCwq35fjFIlL_cfpq0fMUy_QRQKh0KMhGNcWsfydaOWg7ME82nOlmZZDEHPmo02jd8TCi168qcrdz7EjtD1v8nFly0M9JWeQkqt_pLCN8I6zX1tJ59xRxUOymuGshMyKHiKq2slnC7XMGYiZlG3Z0rgKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/whitedns/1556" target="_blank">📅 14:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1555">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kg0n3V2ER8LCHwATW0JeL8Og0aV-vRsPyRG00aByK2hlPDW8q2EaemmCtEwq9AHMOAUm8W80cMb3uDNEWZ3s_7v3w8MyZie6sZX8FubCkt_RZZKlNIMLrezLUHcexuE6vLj-Z0KGmw4xYbnnXCq0M2Up5seDzfKzqLeLOjpNRxc3Sd9JWrkM2ugHRRrVLEy0rtTg8D2LVWA1XqH57i9eW5j-NG2qaMLnfhHh3JyQMUUZOVzX6Ah506AAkkdhuGiWIutaJUhiGY0BtQnL6LdkHyWwpoaI-2uP5JvondeuVcXJ1RonZ36XVKEyRi2KxTfZuRnDA75yVHzbu_80dXGCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
WhiteDNS
مسیری که قبل از روزهای قطعی اینترنت شروع شد
تیم WhiteDNS از مدت‌ها قبل از قطعی‌ها و محدودیت‌های گسترده اینترنت فعالیت می‌کرد. از همان ابتدا تلاش کردیم ابزارها، سرویس‌ها و آموزش‌هایی بسازیم که رایگان و در دسترس همه باشند.
در این مدت افراد زیادی به این جمع پیوستند؛ بعضی ماندند و بعضی مسیرشان جدا شد، اما چیزی که ما را کنار هم آورد همچنان پابرجاست:
حرکتی جمعی برای دسترسی آزادتر به اینترنت.
تیم WhiteDNS تا امروز کاملاً مستقل و بدون هیچ منبع درآمدی اداره شده و تمام هزینه‌ها را خودمان پرداخت کرده‌ایم. با این حال، این مسیر را ادامه می‌دهیم و همچنان ابزارها و سرویس‌های رایگان بیشتری را با کمک همین جامعه خواهیم ساخت.
حالا تنها مسیر درآمدی ما کانال یوتیوب WhiteDNS است. اگر می‌خواهید از این حرکت حمایت کنید، کانال را سابسکرایب کنید و ویدیوها را ببینید. همین همراهی کمک می‌کند WhiteDNS مستقل، فعال و جامعه‌محور باقی بماند.
📺
https://www.youtube.com/@WhiteDNS
ممنون که بخشی از این مسیر هستید
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/1555" target="_blank">📅 10:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1553">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">WhiteAesther V1.2.0    دو پروتکل جدید، رفع مشکل قطعی، و مسیریابی اپ به اپ  از این آپدیت سه تا قابلیت جدید اضافه شده و سه تا مشکل قدیمی رفع شده. همه‌شون رو اینجا خلاصه کردم.
✅
چی اضافه شد  ۱. دو پروتکل جدید: WireGuard و WARP in WARP  تا الان فقط MASQUE (روی…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/1553" target="_blank">📅 09:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1552">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KX0mcp2wD7oLUrtPOKLTqBPwjJypN18iW8xLmG22VZ3TuZbSiZUPody9-2qalidW7qUA6gX5sACaylhQfeJdgbfbrfL3NRpDmWiowozbqIXc_ybrRs7wkgffKAS__hHxQJigzRyCvjYkc3vG7yUgijZmNrzMSuhOkTbwT-2vM6rC60DDTrYFNc-F7QqXCRsudAjHAlWM1kqwo6Jv2NEMkoTjvK88yeNGgxpMX75ajz3qS1qhuma1mHFB6_RSJByJLj6LjaSyJpv8fmKO6XA4jkIry9OhgU95wDp5GupBEfvMjC7Lo3Hfi1AVXhHBKx4V4rlNXlZDnGaPxUDp13ZCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان عزیز
✍️
از دیروز گزارش های زیادی روی WhiteVPN روی گوشی های قدیمی گرفتیم که بهمون گفتید نصب نمیشه، یا نصب میشه ولی میزنید روی اتصال، اررور میگیرید.
ما سعی کردیم توی ورژن ۱.۶.۱ که از لینک زیر میتونید دانلود کنید این مورد رو حل کنیم.
حالا گوشی های اندروید قدیمی‌تر هم میتونن بدون دردسر وصل بشن.
همچنین مشکل کانکشن هایی که camouflage داشتند هم توی این ورژن حل شده.
تغییر دیگه،ای نداشتیم  جز این دو مورد.
دانلود آخرین نسخه
https://github.com/WhiteDNS/WhiteVPN/releases/latest
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1552" target="_blank">📅 06:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1550">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Axr3diIWChrjw9jLEYDwJ2JU49X_cltTkKew-KLsTp0R-s8yVuN3irQS4jqJUx8WW6xvFmbQ_ANpIowaIaufnyM82tf3Ts4GRhShczrOa5sJsUo5GXNabq6mdrr0F4Lr84h-WFfi3pIXDxrnpYWi2fBjPtv3499MUsa_Vjz6Hkew7jHI03UOeSWq5T6ecEZH2Ea3Q5FdIhABaPjvbc_ErEg8mo5K6TLimjIJQLT2AVHWmsafRHsbQ1C4LfD6qTuiKc9JPIcK0atZTv8ZlXhQRkRWR0FA-1iJCqoP3gONPnirQ_ia1tkQZGoJEe05zL8-ft37h-KbrryfHDFu447K2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fLspJYYZXnpehXJD9eQQD8QBTmBykMwQG5B4oR-0fFxVryys3RPCoI_J8gFgrxd7hpqGzceObUguQIxFsLrii3Ekw8pxO2smcBPTYi6AKazy31wlsCAF0217iZKzsJWwuWubcjwcjiCLxceRzisEkNluAtOqYvOSoKzmEg1UmG1I6OacGWNMk6JkGGwUdp5unMaJ4Vg2cYiVhTsL1vZTiH4Cm-ZMA7_wkz9Ff3GyKF26ODtk1k4a5YK1LBZD4Vp_tCDKT0NKRqWYuCZtCKVXfsITcXZwHr4nhpgWQ100L-cwYFSyeSxFFdXwCa-JtGEJ0mWbwK4KFuBb7g-jHL1SKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان عزیز
لینک ساب رو باید بعد از کلیک کردن روی دکمه Raw مشابه به عکسی که گذاشتیم کپی کنید.
لینک
صحیح WhiteDNS Sub
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1550" target="_blank">📅 05:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1548">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCore Forge</strong></div>
<div class="tg-text">🚀
CoreForge Build آپدیت جدید منتشر شد
https://testflight.apple.com/join/DRkT6zny
این نسخه یکی از بزرگ‌ترین آپدیت‌های CoreForge تا امروز محسوب میشه.
از Build 90 تا Build 100 طی حدود ۲۰ روز:
• 214 Commit
• بیش از 411 فایل تغییر کرده
• بیش از 86,000 خط کد جدید اضافه شده
• چند Engine و Protocol جدید از پایه اضافه شده
• بخش بزرگی از سیستم Connection، Routing، Failover و Config Management بازطراحی شده
###
🧩
پروتکل‌ها و Engineهای جدید
🔹
OpenVPN
* پشتیبانی مستقیم از فایل‌های .ovpn
* UDP و TCP
* AES-GCM / AEAD
* AES-CBC برای بعضی سرویس‌های قدیمی‌تر
* TLS-Crypt
* Multi-Remote / Multi-Address
* Username / Password
* Client Certificate
* OpenVPN Subscription
* پشتیبانی بهتر از ProtonVPN، VPNGate، SoftEther و کانفیگ‌های مشابه
🔹
Tailscale
* اتصال مستقیم به Tailnet
* انتخاب Exit Node
* MagicDNS
* مدیریت Account داخل CoreForge
* امکان اتصال به Exit Node حتی بدون انتخاب Config معمولی
🔹
Cloudflare WARP / MASQUE
* WARP به‌عنوان یک Outbound واقعی
* MASQUE روی HTTP/2 و HTTP/3
* امکان استفاده داخل Chain
* WARP Endpoint Scanner برای پیدا کردن Endpoint بهتر
* تست Endpoint با handshake واقعی MASQUE، نه فقط TCP Ping
🔹
mKCP
* پشتیبانی از mKCP مربوط به Xray
* همه Header Typeهای اصلی
* قابل استفاده با VLESS و Trojan
🔹
ECH
Encrypted ClientHello حالا به صورت واقعی داخل CoreForge اجرا میشه و برای بعضی Transportها از جمله Hysteria2 هم اضافه شده.
###
⚡
Load Balancer و Failover
Load Balancer فقط اسم نیست و حالا Connectionها واقعاً بین Nodeهای انتخاب‌شده مدیریت میشن.
همچنین:
* Config فعال داخل برنامه نمایش داده میشه
* Exit IP بعد از تغییر Node آپدیت میشه
* Dead Server Detection سریع‌تر شده
* Backup Node از قبل آماده نگه داشته میشه
* اگر Config فعلی از کار بیفته، CoreForge می‌تونه بدون Disconnect کامل به Backup منتقل بشه
* Backup Pool بعد از Failover دوباره پر میشه
###
🌐
Routing
سیستم Routing هم تغییر زیادی کرده:
* Routing Profile شبیه Shadowrocket
* Rule Actions
* Iran Direct Preset
* Iran 2026 Rules
* category-ir
* Import کردن Routing Rules از فایل
* Fragment به‌عنوان Routing Target
###
📂
Configs و Subscriptionها
مدیریت Configها تقریباً کامل بازطراحی شده:
* Swipe برای Ping / Edit / Share / Delete
* Drag & Drop برای مرتب کردن Sectionها
* Groupهای Local
* Bulk Actions
* forge:// Chain Links
* Tap-to-Ping-and-Connect
* Import QR Code از داخل عکس
* Subscription Folder
* Rename / Reorder / Export
* Auto Update جداگانه برای هر Subscription
* Plan Status
* تقویم شمسی
مشکل فایل‌های OpenVPN بزرگ هم برطرف شده؛ برای مثال اگر یک فایل شامل ده‌ها یا صدها Profile باشه، دیگه همه‌ی اون‌ها به‌عنوان یک Config خراب Import نمیشن و Profileها جدا میشن.
###
🔧
Fixهای مهم
در این نسخه تعداد زیادی Bug مهم هم برطرف شده، از جمله:
* Crash روی تعداد زیاد Config
* مشکل Import بعضی لینک‌های VMessAEAD
* مشکل gRPC پشت Cloudflare
* مشکل XHTTP که Connect می‌شد ولی Traffic عبور نمی‌کرد
* مشکل REALITY و extra
* اصلاح UUIDهای VLESS
* Lag شدید Config List
* Writeهای اضافی Keychain
* آپدیت نشدن Connection Details بعد از Failover
* UDP برای VMess، Shadowsocks و SOCKS
* UDP Associate برای Trojan
* gRPC MultiMode
* pinnedPeerCertSha256
* PattNG Fragment / Cipher Suite / Unsafe Fingerprint
###
📱
iPad و UI
* پشتیبانی بهتر از Stage Manager
* Split View
* Resizable Window
* تغییرات Liquid Glass
* اصلاح Light Mode
* بهبود Tab Bar و Headerها
---
⚠️
نکته مهم درباره Build
این نسخه تغییرات خیلی زیادی داشته و طبیعتاً
۱۰۰٪ تضمین نمی‌کنیم که تمام قابلیت‌های جدید روی تمام Serverها، ISPها و Configها بدون مشکل کار کنند.
بعضی قابلیت‌ها هنوز در مرحله‌ی تست واقعی توسط کاربران هستن و ممکنه روی یک Server عالی کار کنن ولی روی Server یا Network دیگه Fail بشن.
به‌خصوص قابلیت‌های جدیدی مثل:
Tailscale / WARP / OpenVPN / ECH / Chainهای پیچیده / بعضی حالت‌های VLESS و REALITY
هنوز نیاز به تست گسترده روی Serverها و اینترنت‌های مختلف دارن.
پس اگر چیزی Connect نشد یا Connect شد ولی Traffic نداشت، حتماً گزارش کنید و در صورت امکان Config، Log و نوع اینترنت رو هم بفرستید.
Build بیشتر از اینکه «نسخه نهایی بدون باگ» باشه، یک جهش بزرگ برای CoreForge ـه و Feedback شما مستقیم روی Fixهای نسخه‌های بعدی تأثیر می‌ذاره.
🛠️
CoreForge Build
⚒️</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1548" target="_blank">📅 15:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1545">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Ob7Hhlj7zKm1ObThXmHrPzsjx-tm6EZim4bCaTGugVgoeoB4ahw1tztJ8VNDUUnkYy7luv5_Tx9ICg-ZGVSVrL5wTecOow-l9YrhkmLFCRTUGwsVPG-2YUim82iag9gaRJrSTdfnecTXOkuqszMHbp7e_15NC5hxYjZWL55LtyJwQC_ZfNDbsuRizlPvYn_L-Zv9ixtBtKEOpEiPIm1vxvKxo61wpiTF0tsPF6o8gReKTZFMykfoCEv70PvawL7AJGt-hg-M4U-Y2osHTPu7YTt8VfxYkuKaSovLDh6tNLDv4K7oN5y8arI8caK0NO_AShjJSpsoYU1jyEJyK8aFBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther
V1.2.0
دو پروتکل جدید، رفع مشکل قطعی، و مسیریابی اپ به اپ
از این آپدیت سه تا قابلیت جدید اضافه شده و سه تا مشکل قدیمی رفع شده. همه‌شون رو اینجا خلاصه کردم.
✅
چی اضافه شد
۱. دو پروتکل جدید: WireGuard و WARP in WARP
تا الان فقط MASQUE (روی H3 یا H2) داشتیم. حالا از Routes ← Manual ← Protocol می‌تونی این دو تا رو هم انتخاب کنی:
▫️
WireGuard —
سریع‌تره، ولی روی UDP کار می‌کنه
▫️
WARP in WARP —
یک تونل داخل تونل دیگه، کندتر ولی شناسایی‌ش سخت‌تره
⚠️
هر دوی این‌ها UDP هستن. اگه شبکه‌ات UDP رو کامل بسته باشه (مثل همراه اول این چند وقت اخیر) اصلاً وصل نمی‌شن — اونجا MASQUE H2 که روی TCP کار می‌کنه انتخاب درسته.
۲. بکاپ هویت — راه‌حل قطعی مشکل «چند بار نصب کردم دیگه وصل نمی‌شه»
دلیل اون مشکل این بود که هر نصب، یک هویت تازه از Cloudflare می‌گرفت، و بعد از چند بار ثبت‌نام از یک آی‌پی، دیگه هویت جدید نمی‌داد. حالا می‌تونی هویتت رو قبل از حذف اپ ذخیره کنی و بعد از نصب مجدد برگردونی.
۳. Split tunnel — انتخاب اینکه کدوم اپ‌ها از تونل رد بشن
از Traffic ← Apps: همه اپ‌ها، فقط چندتا اپ خاص، یا همه به‌جز چندتا اپ خاص (مثلاً بانک یا اپ‌های داخلی).
🛠
چی رفع شد
▫️
ثبت‌نام مشترک بین پروتکل‌ها — امتحان کردن هر سه پروتکل قبلاً ۳ بار ثبت‌نام می‌خرید. حالا یکی مشترکه.
▫️
WireGuard و WARP in WARP دیگه روی "trying" گیر نمی‌کنن — از تا ۹ دقیقه بی‌نتیجه، به معمولاً چند ثانیه.
▫️
باگ ساب عوض‌شده که نودهای قدیمی رو نشون می‌داد — درست شد.
📌
آموزش: Split tunnel
۱) Traffic ← Apps
۲) یکی از سه حالت: All apps / Only these apps / All except these
۳) با سرچ اپ‌های موردنظر رو پیدا کن و سوییچشون رو بزن
برای بانک یا اپ داخلی: All except these بزن و همون یکی دو تا رو انتخاب کن.
📌
آموزش: بکاپ هویت
Settings ← Identity & access → Save a backup (قبل از حذف اپ) / Restore from a backup (بعد از نصب مجدد)
⚠️
این فایل مثل رمز عبوره، رمزگذاری نشده — جایی نگهش دار که رمز عبور نگه می‌داری.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1545" target="_blank">📅 12:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1535">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGEA1HLMC_0vmyelXYC8kzTSGIaeBemWiRos8pj26ad4mOWFrhbSK_BlJrIfmdDpM8DlCF3xlJZ4i77RsBRAa-cbddZ5qjp0FrEg7jUuI6Zyya2sCJyLZ40Q3zdNR2qKfIIwA3ul79_VSaJ84FJWmA9GtmHcCnM1clreWN5Q0j81eHMlt3FLSLlttoi3OkwzHgPFPeawQASxQgvz3rUfFtbSRqISOr8DoizF9YDIwV3fqAvnMzDJfLEuNQ9vScxiU8gHSOFJyRZvsOdAzoOQF2Bl_EyRgs7KB9CIOCwFKqa_pTNa_bxn57N82uLH-eJ9syiAOQXGfUoxzQ2igCq7OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN v1.6.0 منتشر شد
🚀
یکی از بزرگ‌ترین به‌روزرسانی‌های WhiteVPN آماده است؛ با امکاناتی که اتصال‌ها را قدرتمندتر، انعطاف‌پذیرتر و قابل‌کنترل‌تر می‌کند:
📺
پشتیبانی کامل از Android TV
🔗
زنجیره کردن دو اتصال برای امنیت و انعطاف بیشتر
🛡
پشتیبانی از
AmneziaWG v3
و تنظیمات پیشرفته WireGuard
📥
وارد کردن مستقیم لینک‌های
Hysteria2
و
WireGuard
⚡
تست اتصال‌ها از تمام سابسکریپشن‌ها
🌐
بهبود سازگاری، پایداری و رابط فارسی
اگر از WhiteVPN استفاده می‌کنید، همین حالا به نسخه
۱.۶.۰
به‌روزرسانی کنید.
این نسخه با کمک بازخوردهای شما ساخته شده است. اگر مشکلی دیدید یا پیشنهادی داشتید، حتماً در گروه با ما در میان بگذارید.
🤍
WhiteVPN v1.6.0 — دو مسیر، یک اتصال قدرتمندتر.
📥
Github Release
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.0</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1535" target="_blank">📅 09:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1534">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">از این به بعد کانفیگ های بیشتری داخل ساب ما خواهد بود.
هر ۳۰ دقیقه بیشتر از ۲۲۰هزار کانفیگ جدید تست میشن و خروجی اونها بین ۲۰۰۰ تا ۳۰۰۰ کانفیگ با کیفیت و سریع خواهد بود.
تعداد کانفیگ های حاضر: ۳۳۵۳
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1534" target="_blank">📅 07:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1531">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">https://github.com/iampedii/whitedns-sub
لینک ساب برای استفاده در برنامه های white</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1531" target="_blank">📅 18:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1528">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👆
whiteAesther  android V1.1.0
در این نسخه از اپ اندروید شما میتونید با  قرار دادن یک کانفیگ ای پی خودتون را ثابت کنید و احتمالا خیلی از مشکلات مربوط به Gemini , Chatgpt و بقیه هوش مصنوعی ها و وبسایت هایی که روی لوکیشن حساس هستند  حل خواهد شد
نکته  خیلی مهم برای نسخه اندروید :
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
بسته به نوع کانکشن و موارد دیگر ممکن هست 1-5 دقیفه بار اول طول بکشه که شما موفق به اتصال بشید . ولی در دفعات بعدی این موضوع خیلی سریع خواد بود .</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1528" target="_blank">📅 17:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1527">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">WhiteAesther
android V1.1.0
🔥
🔥
🔥
🔥
🔥
🔥
قابلیت Exit Chain
از این نسخه می‌تونی بعد از تونل، یک ایستگاه دوم اضافه کنی.
یعنی چی؟ تا الان ترافیک تو از سرورهای Cloudflare بیرون می‌رفت و سایت‌ها آی‌پی Cloudflare رو می‌دیدن. حالا می‌تونی سرور شخصی خودت (یا سابسکریپشنی که داری) رو آخر مسیر بذاری، و سایت‌ها آی‌پی اون سرور رو ببینن.
مسیر ترافیک این شکلی می‌شه:
گوشی ← تونل رمزنگاری‌شده ← سرور خودت ← اینترنت
به چه دردی می‌خوره؟
▫️
سایت‌هایی که آی‌پی‌های Cloudflare رو بلاک کردن (بانک‌ها، بعضی سرویس‌های خارجی، بعضی بازی‌ها)
▫️
وقتی به آی‌پی یک کشور مشخص احتیاج داری
▫️
و مهم‌تر از همه: اگه شبکه‌ات اصلاً تونل رو بلاک کرده، می‌تونی تونل رو دور بزنی و مستقیم از سرور خودت استفاده کنی
پروتکل‌های پشتیبانی‌شده: vless vmess trojan shadowsocks hysteria2 و بقیه — چه لینک سابسکریپشن، چه کانفیگ تکی که دستی می‌چسبونی.
📌
آموزش — ۵ قدم
۱) اپ رو به نسخه ۱.۱.۰ آپدیت کن.
۲) برو به تب Routes ← گزینه Exit chain.
۳) کلید Exit chain رو روشن کن.
۴) توی کادر Add a subscription لینک سابسکریپشنت رو بذار و Add رو بزن. اگه فقط چند کانفیگ تکی داری، از Paste nodes by hand استفاده کن — هر کانفیگ توی یک خط.
۵) برگرد به Home و وصل شو. تمام.
⚠️
سه نکته که حتماً باید بدونی
۱. لیست سرورها فقط بعد از وصل شدن میاد
قبل از اتصال قسمت Nodes خالیه و این ایراد نیست. سابسکریپشن تو از داخل تونل دانلود می‌شه تا شبکه‌ات نفهمه داری چی می‌گیری. پس اول وصل شو، بعد برگرد به Routes ← Exit chain تا لیست سرورها رو با پینگ‌شون ببینی.
انتخاب سرور قطع و وصل نمی‌خواد — روی همون اتصال جابه‌جا می‌شه.
۲. گزینه Dial nodes through the tunnel
پیش‌فرض روشنه و بهتره روشن بمونه: شبکه/اپراتور تو هیچ‌وقت آدرس سرورت رو نمی‌بینه، و سرورت هم آدرس واقعی تو رو نمی‌بینه.
🔸
ولی اگه اپ اصلاً وصل نمی‌شه یا خیلی طول می‌کشه، این گزینه رو خاموش کن. اون‌وقت WhiteAesther تونل رو کامل رد می‌کنه و مستقیم به سرور خودت وصل می‌شه — دقیقاً برای شبکه‌هایی مثل همراه اول که تونل رو می‌بندن، همین حالت جواب می‌ده و خیلی سریع‌تر هم وصل می‌شه.
۳. Coverage باید روی Whole device باشه
توی تب Traffic. اگه روی Proxy only باشه، Exit chain کار نمی‌کنه و اپ بهت تذکر می‌ده.
💾
حجم اپ بیشتر شده
از حدود ۸ مگابایت رسیده به ۴۷ تا ۵۷ مگابایت. دلیلش موتور جدیدیه که این قابلیت رو اجرا می‌کنه. اگه Exit chain رو روشن نکنی، اپ دقیقاً مثل قبل کار می‌کنه.
▫️
arm64-v8a — تقریباً همه گوشی‌های ۲۰۱۷ به بعد. از این شروع کن
▫️
armeabi-v7a — گوشی‌های قدیمی‌تر و اقتصادی
▫️
universal — اگه مطمئن نیستی (حجمش سه برابره)
⬇️
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
اگه مشکلی خوردی، از Settings ← Diagnostics گزارش بگیر و بفرست — از این نسخه لاگ موتور Exit chain هم داخلشه.
@whitedns</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1527" target="_blank">📅 17:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1526">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📺
خبر خوب برای کاربرهای Android TV
در ورژن بعدی WhiteVPN پشتیبانی کامل از Android TV اضافه شده. تا فردا نسخه جدید اپ اندروید هم ریلیز میکنیم
❤️</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/whitedns/1526" target="_blank">📅 17:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1525">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👆
whiteAesther V1.5.2 desktop
در این نسخه از اپ دسکتاپ شما میتونید با  قرار دادن یک کانفیگ ای پی خودتون را ثابت کنید و احتمالا خیلی از مشکلات مربوط به Gemini , Chatgpt و بقیه هوش مصنوعی ها و وبسایت هایی که روی لوکیشن حساس هستند  حل خواهد شد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1525" target="_blank">📅 16:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1524">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">whiteAesther
V1.5.2 desktop
🔥
🔥
🔥
🔥
🔥
🔥
🔗
قابلیت جدید: Exit chain (زنجیره‌ی خروج)
🔥
🔥
🔥
تا حالا وقتی وصل می‌شدید، ترافیک‌تان امن و رمزنگاری‌شده بود — ولی آدرسی که سایت‌ها می‌دیدند همچنان نزدیک خودتان بود. این ایراد ما نبود: WARP کلادفلر عمداً کشور شما را عوض نمی‌کند، از نزدیک‌ترین نقطه خارج می‌شود و همان‌جا را هم geolocate می‌کند. برای همین خیلی‌ها بعد از اتصال موفق، باز هم به سرویس‌های خارجی دسترسی نداشتند.
Exit chain یک هاپ دوم اضافه می‌کند. ترافیک اول از تونل رد می‌شود، بعد از داخل تونل به نود خودتان می‌رسد و از آنجا وارد اینترنت می‌شود. آدرسی که سایت‌ها می‌بینند، آدرس نود شماست.
دو نکته‌ی مهم در طراحی:
▫️
نود از داخل تونل شماره‌گیری می‌شود — یعنی شبکه‌ی محلی شما فقط یک اتصال عادی به کلادفلر می‌بیند، نه آدرس نود و نه SNI آن.
▫️
به همین دلیل، نودی که از ایران فیلتر شده باز هم کار می‌کند — چون از شبکه‌ی کلادفلر به آن وصل می‌شویم، نه از اینجا.
━━━━━━━━━━━━━━
📘
آموزش
۱. بالای پنجره روی Advanced بزنید، از منوی سمت چپ Exit chain را انتخاب کنید.
۲. دو کلید را روشن کنید:
• Route through a second hop — خود قابلیت
• Dial nodes through the tunnel — پیش‌فرض روشن است، همین‌طور بگذاریدش
۳. نودتان را اضافه کنید، به یکی از دو روش:
• Subscriptions — لینک ساب را بگذارید و Add بزنید (خودش به‌روز می‌ماند)
• Configs pasted by hand — کانفیگ‌ها را خطی یکی paste کنید و Apply بزنید
vless · vmess · trojan · ss · hysteria2 · tuic همه مستقیم پشتیبانی می‌شوند؛ لازم نیست چیزی را تبدیل کنید.
۴. پایین صفحه در بخش Nodes نودها ظاهر می‌شوند با پینگ واقعی‌شان از پشت تونل. با Test هر کدام را بسنجید و با Use یکی را انتخاب کنید.
۵. بالا سمت راست Save profile را بزنید تا دفعه‌ی بعد هم فعال باشد.
━━━━━━━━━━━━━━
⚙️
کدام حالت را انتخاب کنم؟
• Whole machine — کاری لازم نیست، پروکسی سیستم خودکار روی زنجیره تنظیم می‌شود. برای اکثر کاربران همین درست است.
• This app only — مرورگر یا برنامه‌تان را روی آدرسی که در همان کارت نوشته شده تنظیم کنید (معمولاً
127.0.0.1:1820
).
برای اطمینان، کارت What websites see در صفحه‌ی اصلی آدرس واقعی خروجی‌تان را نشان می‌دهد. اگر برچسب Through your node را دید، زنجیره برقرار است.
@whitedns
https://github.com/WhiteDNS/WhiteAesther</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1524" target="_blank">📅 16:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1523">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jwdIasvuMoTLK4wtHy7qSB3I2Z5cmJZqcr8Pk84WyfV6GgGR2UY6RgmnKid6MpEwRkqwNRRErOPoOgei7SeGkLVmHuMDwbSc90b7ec6v4aG7Dl4nk8OJ4yTKWgq5WfT4kMf0He8TSoHoUR5mr1zsXfaDn53vWYU9rk28lOnz0kPUE_TD-592YKyL9L8I8ue5tk9NxMJje8_P8v1A9nP2vNre64js1RQHsfnJjGFuL6q8kfuFSTxPHDbzEAqM6tF8sH2v8whzqG3d87OPaALQkblIY2fkuQ_8fMPhdU0N_6wArKyc1L6veO2Io9FSnNYTF81o-U-GiTYaHArTqBmAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/whitedns/1523" target="_blank">📅 16:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1522">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BEgufPc1EGakuT2ZdeIKUti1SY-2mLffW9n2Nj_bVV1vmzeJihJUApvNCyczW7CGNZSmD9xOVRp7SmshaMQV_odSociaDglflrQKgZ6MhsyrAsD2sNhW0kSrE8zGwdM-lEdiV5etCPanoUXy5CZ3nGWGIEowg1FC-WwuFNEFbLfChGsM5Mo4sue4jw5xNIv1j9j5f1SLmuxZoK2EGaIKQLFrfw7BmxYFMFy18DLCSVjk6waW2S7PItOwRGC6zl1nQ13Gcael0zeXRSF_tJczfieIFgJdLBd4ecfj9nJ6MERj94HZjdwDddPoqv4aJZCkhVPnZKvOjVONwMNv765Aug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1522" target="_blank">📅 16:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1521">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sf1kcL3KIJGamifMUVZ4QIPE1pOAgzzR_Gv-GXv7Ze2nSn0AmrSHm4HoAmHZ5gDZ8wnd3LlM2w5CJTPblXvSdIDSlHJK2soQOx3ld7XA3PJ2C0s680RJOWkhYjlSOA1j6KfZMb6zalSk9RlvWa23ENRalMlNXNgm2IpLi6NUKEQ6vgaiRJkS6E_kHm6jo_RAPCPmhbt6vhAi4jB66lpkrFdaBdlRpC7TtVrB9oQ51_iGjsOi-nPTTOGazo3Ey1c8zU1XFRCeHQ4TmSB4f7YzX96YVYsjGpd00g5yTt6zp05C1CVStsDq-8tTVeBPMCYGSwwCcI-EYJsaqJstDx_CNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏯️
آموزش کامل اپلیکیشن WhiteAesther
📍
تماشا در یوتیوب
https://youtu.be/cRfqxbDY1Dg</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/whitedns/1521" target="_blank">📅 18:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1518">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0  توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.   حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/whitedns/1518" target="_blank">📅 14:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1517">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">آموزش نصب پنل رایگان StanNg روی Railway
بدون VPS و بدون هزینه کانفیگ V2Ray بگیر
🔥
از صفر تا صد کامل توضیح دادم، مناسب تازه‌کارها هم هست.
لینک ویدیو:
https://youtu.be/sdiGXCDsDvQ
سوالی داشتی بپرس
👇</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1517" target="_blank">📅 11:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1515">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🌎
نسخه جدید WhiteVPN v1.5.0
👆
تغییر های این ورژن کاملا روی فیدبک های شما بوده، و به نظرم از لحاظ تجربه کاربری تغییر خیلی خوبی داشتیم.
😆
ممنون از فیدبک هایی که به ما میدید.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/whitedns/1515" target="_blank">📅 08:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1510">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1510" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/whitedns/1510" target="_blank">📅 08:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1509">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqa4DfXYGt3snB646AXCVNevJqFnHwIlNrqP11hhtypFXsflEF8WqE8kt3ZZQBonIlwvIN8-0mPEfWZYebZHLY4lbNcQ5q-Hr_wflCXXqBTCnIhuY0GHOjLx4AKTI32KNSdn4yuJllASZdU26fdyLZV104DKywYUAfRWPP-Y2GpiTpX2IwLJJZFmCJwj31dXyp-szBoJbXBzDUAUofGI7EGT8OQu-RO0pwg7evzceJ2MKXw0w016rTtWYTy7vKtfap4fLlK9DW08k3lq05bM0R1bb0g6dsgyjwYCyfGG4WQ7HY4owNCc7g-KQl4QEI-EpO0T7JeEukzA2uQLiHIROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/whitedns/1509" target="_blank">📅 08:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1508">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1508" target="_blank">📅 08:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1507">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوستان عزیز سلام
اپ CoreForge از تیم WhiteDNS ظرفیت جدید اضافه کرده برای کاربران IOS
https://testflight.apple.com/join/3htm1Whc
آموزش استفاده
https://youtu.be/filwdiPKN90?si=O-hvgeNw43t4BUmR
@WhiteDNS</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/whitedns/1507" target="_blank">📅 01:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1506">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">💬
لینک ساب تیم WhiteDNS
https://github.com/iampedii/whitedns-sub</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/whitedns/1506" target="_blank">📅 01:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1504">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سلام دوستان :
❤️
اینقدر درخواست برای IP ثابت برنامه های  whiteAesther و whitevpn اومده که دیدیم بهتر هست ، یک پست براتون بگذارم
در حال حاضر  این امکان توی آخرین ورژن های این دو برنامه وجود ندارد
با اعضای تیم داریم روش کار میکنیم و امیدواریم طی روزهای آینده به دستتون برسونیم ، یکم به ما وقت بدید و صبور باشید.
ببخشید که انجام درخواست های شما گاهی طول می‌کشه، چون ما هم مثل تک تک شما درگیر کار و زندگی و مسائل خودمون هستیم و گاهی وقت کم میاریم
ولی مطمئن باشید ما همه پیام های شما را می‌خونیم و تا جایی که بتونیم ترتیب اثر می‌دیم ،
ارادتمند و کوچیک تک تک شما عزیزان دل
ویسپر</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/whitedns/1504" target="_blank">📅 16:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1502">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⚠️
موقت
به نظر میاد که دامنه
workers.dev
کلادفلر رفع فیلتر شده است</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/whitedns/1502" target="_blank">📅 19:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1501">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/QHYXz9bs3T5Z7RqwUI0IG5QqNivhihoR9YOWmyjfgCEEaivToI_nD677FPs7BQStTfNBGCo224LhZ_8EMBhEa3JxD59G_utn8LTXQtonCWdBdURtcopoX6gcSuKit9AGAMzPal-D_KlNHiy_-XdXxl_6sQIWGHUG_5KNWgSPNEFLmg4WfXfMFB6rGV-RYkWSRbPaxC5ydQ1KymgQVvXgrSsJD-UEkNPsEa1_828CYel-lJplGrgxtDrgsRGRczmXK8ICtqvENXuot-vaZzFyvrJ0fjVpKbJKdrRho-uwwg3V4jQutw6-Wyho9AWaI6C7xKhTgYIVLrmpMnhu4vmmJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
چرا موقع ورود به Gemini با ارور ۴۰۳ مواجه می‌شویم و چطور حلش کنیم؟
خیلی از کاربران هنگام باز کردن
gemini.google.com
با خطای معروف زیر روبه‌رو می‌شوند:
403. That’s an error. Your client does not have permission to get URL / from this server.
🔍
دلیل این ارور چیست؟
سرویس‌های هوش مصنوعی مثل Gemini دسترسی کاربران برخی مناطق را به دلیل محدودیت‌های منطقه‌ای و حقوقی مسدود (Geo-block) می‌کنند. اما اگر از ابزارهای تغییر آی‌پی استفاده می‌کنید و باز هم این ارور را می‌بینید، علت معمولاً یکی از موارد زیر است:
1️⃣
نشت موقعیت (DNS یا WebRTC Leak):
با اینکه کانکشن شما وصل است، مرورگر از طریق درخواست‌های DNS یا قابلیت WebRTC، آی‌پی واقعی شما را لو می‌دهد.
2️⃣
شناسایی آی‌پی دیتاسنتر (Datacenter IP):
گوگل بازه‌های زیادی از سرورهای عمومی و تجاری را شناسایی کرده و مستقیماً مسدود می‌کند.
3️⃣
کش و کوکی‌های ذخیره‌شده:
مرورگر موقعیت قبلی شما را در کوکی‌ها نگه داشته است.
🛠
راهکارهای سریع برای رفع مشکل:
🔹
تست نشت آی‌پی (Leak Test):
ابتدا وارد سایتی مثل
ipleak.net
یا
browserleaks.com/ip
شوید و مطمئن شوید در بخش‌های WebRTC و DNS هیچ نشانی از آی‌پی واقعی یا DNS داخلی وجود ندارد.
🔹
استفاده از حالت ناشناس (Incognito):
یک پنجره Incognito / Private باز کنید یا کش و کوکی‌های مربوط به دامنه‌های
google.com
را پاک کنید.
🔹
فعال‌سازی حالت TUN Mode / روتینگ کامل:
مطمئن شوید کلاینت شما تمام ترافیک و به خصوص درخواست‌های DNS را هدایت می‌کند و ترافیک دامنه‌های گوگل به صورت Direct رد نمی‌شود.
🔹
تغییر نود یا کشور سرور:
اگر آی‌پی سرور فعلی توسط گوگل فلگ شده باشد، با جابه‌جایی نود یا تغییر لوکیشن معمولاً دسترسی بلافاصله باز می‌شود.
💡
اشتراک‌گذاری برای دوستانی که با دسترسی به جمینای مشکل دارند.
@whitedns</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/whitedns/1501" target="_blank">📅 15:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1496">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FvDmg2jQabmp4A0ThU2dS6xWMj2AxU8fcZMeWSWFxbcQph3MyRKq0XAjTXmOer4neCAlCC-8r4P3ETxMUjMLyPJHCclbNAIe1MWsexwnRpwx_450H1qb2SvbSheCmH98a3s1c0hiHHnz5x-M44CbQFPm2pAyCtJSYWL5byMqa1xbUVEYooBQijl899uaknaaHCxRff2e5O1n61eG0mHOk37cKOUZqSsnH5xsMdgP50cBOPYlweEWnwk4ErVtYmU71ZMIAT6Lb6xeccFtvFJGgm1Zjl5IXOKGivQd1FmPfM6AM7PE6wltDJb3g2SUr8_vNchFDOvCBnLaPS9fUkzddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/whitedns/1496" target="_blank">📅 07:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1495">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Oc0DlGyeK08LcZTgHAK4NfGkiAvyhN6nD-_iCsI_2IC43SC1x0no4SdfeK7wXzBLiirxkDIB8-NYt3Lsjy2bRGbFLu8TOOWTX5PZ1yyDt_DdHy4-DypBZaMlkRAIoDkFj8Fupd1UgC3Gbyb4Cf3zTCFm5nf04jQoAdJsSjdnGujy6Waq3TgBL4LrVFhWpfbNaUCFBkoHI3I2DfP8SFgGUqUy7i_tXuVqUFV_hTU6hPtMRlpW6sKu2Aj_X0TMUQSfQnFk7kR_9gQ-MpRtQm8iimH7piwnzTkqCacX-OFXr8PMcELO4C8fhI_6cnrhRVX6VeGdUTbaA3p1Jl5BQdj83A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/whitedns/1495" target="_blank">📅 07:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1493">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/S6c50Zkq4c7cB20WOrsym9LE9cDeqV27VqbE_99X8kdBmDguT8SkBc7cMz5phSC3SV67e-ShfZXcHSw8nWiQkJ19JATJSCa2nhAwAntHAba9drakufPGG2Vlqs-0nJulaX4qajWJZxrKopJNOeqnlLcFoMpOnw9vc52_vaOBO7kl7EEBddTI_RJLAJWw3FYYd4IeDBbkNPXHSdT2sJwESjZBokMPXjtQVJJ0BW95nqn-2u0yYavvFikH4m6CnHLQy6Lw1_0SC5FQAzSd8OT3KkDP7H5oprGZe4nZmR9zmq7t_--oZ_dvjuuoYAFI8iALj80yT0bYVk6gZ3CIdMwysw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام :
برای حل این مشکل توی ورژن دسکتاپ و مبایل whitevpn لطفا ساب زیر را دستی وارد کنید
اگر به هر دلیلی ساب برای شما اپدیت نمیشه اول یک فیلترشکن روشن کنید که ساب را بتونید بگیرید و اپدیت کنید بعد استفاده کنید
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
@whitedns</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/whitedns/1493" target="_blank">📅 05:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1491">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
تمام
#نکات
واسه مشکل فیلتر شدن worker رو داخل این پست میگم:
👽
💻
طبق آموزش هایی که قبلا دادم با اپلیکیشن pattng و همچنین v2rayn در ویندوز میتونید مشکل فیلترشدن ورکر رو حل کنید و کانفیگ های -1 رو مجدد متصل کنید.
آموزش مروبطه:
👇
https://t.me/xsfilterrnet/3642
📱
داخل ios هم طبق تنظیمات یه ip تمیز پیدا کنید داخل کلاینت incy یا hiddify بزنید و فرگمنت رو روشن کنید متصل میشه.
یه روش دیگه بعد از بالا اومدن پنل استفاده از کانفیگ های فرگمنت برای bpb هست که با مقادیر low (1-1) رو متصل کنید
🔥
🔗
در مورد لینک ساب های raw هم به گفته خود bpb:
بچه‌ها اگر ساب Raw و کانفیگ TLS استفاده میکنید از این روش در v2rayNG/pattngاستفاده کنید، معلوم نیست تا کی کار کنه، اگر پایدار بود پنلو تغییر میدم.
این رو دو جا وارد کنید:
https://8.8.8.8/dns-query
۱. قسمت Remote DNS تنظیمات برنامه.
۲. ویرایش کانفیگ قسمت echConfigList.
با Mux خاموش
یه نکته دیگه از بچها اینترنت آزاد که جواب داده:
با ECH و استفاده از آدرس udp://1.1.1.1 میتونید فیلترینگ
pages.dev
و
workers.dev
رو دور بزنید.
💓
نکته ای هم که متین سنپای گفته:(همراه با ابزار جدید)
https://t.me/MatinSenPaii/4960
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1491" target="_blank">📅 22:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1489">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbNfhkVFJMTRIFss2hJ53e32lNpnpNo3PqIK_ypufr9wPSoCLBB-zIdY5bPlPtrF4vmTM2mq3tEI0Ehf_oFwJp7rwHCB68Y0_s212znoe_Skg_pjXjKqCSKMzRSziiceBaf8_EjimYN4L2VfzY_ZUC8KgWMpuTW5w_sRe6RYjOZ9Ls9nfE3ng1wHdqPCt9kgcFTk6D5_zKUkMwkK3c4YolMHJ0fN2LU1Ugnjyhf_2cOPRHxmTM7ZGo8EPuIfnvUDrlChB5xox44L6WUI81wEjgFe7MOLPHUsLaLO-iINQ3zz_TX_OJZUfFpk-z2q2WWRfTvian8SAxiT8FZNs8Xxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟   میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro و باقی Wireguard ها وصل بشید.  این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1489" target="_blank">📅 21:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1488">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiNv_VqiGQXJf-Pqb4MjWL7sEh3GgxumbMX-Vxd7_Ew9YmndJHcXP1rXWlxz_vas7Fvw-R3Ig2hjzxo8lNlSh-aWcLwYFyOM6j5uYCmtxcxBZYRpyP05_vp8SWzJfvYmjzHYW3otmq-Bdeyv9NHTtCNxKPZdd7wdE0wkdiIR3Z5JzZeS4cuOX9uFXOkBX2j_rE4AxIpAjFq_OsIEU60ARUjx4Wuo35HZO3KxumV5cSgI1iI1NfmGhBSxwUWJFiSnqoSCXk9OqmYrt0ss85Piw47N8qbOfUNUNrbxNiDzyx1By8vw8q8M4xQGK8FbgR4RfcBziDKC8GbhsLMaTTfhKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro و باقی Wireguard ها وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN
لینک ساب Mihomo رو داخل WhiteVPN وارد کنید.</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/whitedns/1488" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1487">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=YAqcFBl4LZYpgoFKZgLgBj7pIUYiYSxOV9PyrKQXN73hbwEADwY756DWuaCY4UMDmOGPZ7kVTY_gE5Oz6M0gB-ywEWw-DVPeAkyKkAYBfHigV2zuei2ekka18Xo9qhmj1v4Cbb02fK9fK1-kNT_p5Ja7xgbjK6ohy-ZEFQRb77HdTlF6s07LHt9kqJcX3lEns5vXXiduG07pgF5-_JQmp0b3Bd6ajgX3amD1qriRPgT8tGvNySOxnGfX5TLH-i-_1LN_-hhxzN-E2uGzcQm_PDhm66fS0k_geGj6_QGlb0Hf37wmvmYkFYK6T4a8vx50_O6aSGtbgeddOfch2SdbSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=YAqcFBl4LZYpgoFKZgLgBj7pIUYiYSxOV9PyrKQXN73hbwEADwY756DWuaCY4UMDmOGPZ7kVTY_gE5Oz6M0gB-ywEWw-DVPeAkyKkAYBfHigV2zuei2ekka18Xo9qhmj1v4Cbb02fK9fK1-kNT_p5Ja7xgbjK6ohy-ZEFQRb77HdTlF6s07LHt9kqJcX3lEns5vXXiduG07pgF5-_JQmp0b3Bd6ajgX3amD1qriRPgT8tGvNySOxnGfX5TLH-i-_1LN_-hhxzN-E2uGzcQm_PDhm66fS0k_geGj6_QGlb0Hf37wmvmYkFYK6T4a8vx50_O6aSGtbgeddOfch2SdbSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/whitedns/1487" target="_blank">📅 19:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1486">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1486" target="_blank">📅 19:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1481">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/whitedns/1481" target="_blank">📅 19:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1480">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XN5pef3gT-hy5oPIIlIEkAgKgX2QAiF-agAdO77fG3GdK4dNc8ttbk9baVxngXcPDw45hD2r_gnnSKacKJfq_Dc8dFDGJ8TK1cAYQzT05KImTIySsh9HrIfx1xPpE1UqWZ74kQhrTMbIopG_rCwFk4zV97Zix6vewzX-oYC5HkTE2Whg4kXVKFSYSfXArBT7z_eWHK6sX9p5t19Bo_Kc0kHyYhQ-9IiBWgnNS6QkpWMEd9IWR0lP7TRLzB3QueblvWz_IF--_c21B2PyDNehzSVHQ-MObHcFJhWpbhMOtLqa-y0eTtVmP7ylQu-8V7e0O2dh-4pOpHxLDCtC3FHedA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/whitedns/1480" target="_blank">📅 19:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1478">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/t5uFxzHhhLZyVEqVHbUxUQH3L8zZtE_JvJ31uYBlxRH6qNvPmOA-yOMPnx3tQzoEVlqN8BYq-y4aFosPdGX9NE-n_YtHjbUhqAZm79ESDPtcw0eoa92bQ5Crat5r4qCzx0aYW_eJLbn0zR1KZA70rVS6xmU_KMCk0ZjwblElmcW0kRiA63eOxFaVynoDbTbfg3orsvL_G6C-M7ZFy31HUozGnHqCi25Jc-sKZPplSH12TDGuc3DAOodqJweLlNKjuYMLIBbi62neUfOKsLQlh9NKJLVrIup0ATsEUrrZyR_X_wp9ErUX5D3cEkaCnczEl1GHbEaEF4-sKh9hPV2Xlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
وایت‌استر  —
نسخه‌ی دسکتاپ بتا
WhiteAesther Desktop V1.3.1
یه کلاینت رایگان و متن‌باز برای عبور از فیلترینگ، ساخته‌شده روی هسته‌ی Aether (همون هسته‌ای که تو اپ اندرویدش هم استفاده می‌شه). برای ویندوز، مک و لینوکس؛ کاملاً رایگان و بدون نیاز به کانفیگ دستی.
✨
امکانات:
🔎
جست‌وجوی خودکار مسیر — به‌جای اینکه شما دنبال کانفیگ سالم بگردید، خود برنامه بهترین دروازه رو پیدا می‌کنه (با MASQUE H2/H3، WireGuard و WARP-in-WARP)
📊
نمودار سرعت و تأخیر زنده — تست سرعت واقعی داخل خود برنامه + نمودار پینگ لحظه‌ای
🖥
دو حالت اتصال — «فقط این برنامه» (پراکسی محلی) یا «کل سیستم» (همه‌ی اپ‌ها از تونل رد بشن)
🛡
کلید قطع اضطراری — اگه تونل قطع بشه، ترافیک رمزنشده لو نمی‌ره
🔍
جست‌وجوی تنظیمات با Ctrl+K — هر تنظیمی رو در چند ثانیه پیدا کنید
🧩
چندپلتفرمه — ویندوز، مک (اینتل و اپل‌سیلیکون) و لینوکس، هم x86_64 هم arm64
📖
متن‌باز، برای همیشه — کد کامل زیر مجوز AGPL-3.0 روی گیت‌هاب
⚙️
نحوه‌ی استفاده:
1️⃣
از لینک زیر، نسخه‌ی مخصوص سیستم‌عاملتون رو دانلود کنید
2️⃣
نصب کنید و برنامه رو باز کنید
3️⃣
دکمه‌ی Connect رو بزنید و چند لحظه صبر کنید تا مسیر سالم پیدا بشه
4️⃣
اگه خواستید کل سیستم از تونل رد بشه، پایین صفحه گزینه‌ی «Whole machine» رو بزنید
5️⃣
برای تنظیمات پیشرفته (پروتکل، DNS، حالت جست‌وجو…) روی Advanced بزنید یا Ctrl+K رو بزنید و اسم تنظیم موردنظرتون رو تایپ کنید
📥
دانلود:
github.com/WhiteDNS/WhiteAesther/releases/latest
💬
نکته: چون برنامه امضای اپل/مایکروسافت نداره، ممکنه هنگام باز کردن هشدار «ناشر ناشناس» ببینید؛ کافیه روی فایل راست‌کلیک کنید و Open رو بزنید (تو مک هم از System Settings اجازه‌ی اجرا بدید).
#وایتاستر
#ضدفیلتر
#متنباز
نکته مهم :
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
گزینه whole machine همان system proxy هست - این گزینه فقط اپلیکیشن هایی مثل گوگل کروم که امکان ان را دارند پراکسی میکند - برای همین ممکن هست بعضی از اپ های شما پراکسی نشود
تلاش خواهیم کرد در روزهای اینده امکان TUN را اضافه کنیم
@whitedns</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/1478" target="_blank">📅 18:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1477">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوستان عزیز سلام
مثل اینکه آدرس های ورکر کلادفلر فیلتر شدن. و آدرس ساب اپلیکیشن ما داخل ورکر ها هستش. تا آپدیت بعدی، میتونید ساب مارو از لینک زیر وارد اپ WhiteVPN بکنید
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1477" target="_blank">📅 16:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1476">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AyuXc4eHNmfIS8OX0P75jEI7_YWI1U0SKU8TAvs6gq_W-T2N-xpjB89ihQEMyaRo45hWebeZxh5YiOZAgJ-zoX1EiX578_tPSE1as2j_zP6c8QDHNCyiPdAl2NPB-ioVNioSV_mGazzRfNUIPXJbsdishhVOLQ_dJ98vlRzzl7MwoDJXn4f9bvKa1JdmYhGl1lITQ9jFFkmzeDNRnECqMz3iOmbryQ8D5FrRkFKeVNVY_fLCdjEfr3dLElnlJUH0aO2-AbQJLgQApfSURuaF9Zik8poaid0RbVRwsGN0ACl-BgBo1gWwYKcJmEj6guH3qAW3GRSPUugAx3gPY750qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther V1.0.2
دوستان سلام :
ما روی هسته Aether که حاصل زحمت دوست عزیزمون
CluvexStudio
هست یک کلاینت**
آزمایشی ورژن بتا
** درست کردیم . که اگر دوست دارید تست کنید و لطف کنید فیدبک بدید.
پیشاپیش ممنونیم
❤️
❤️
❤️
اموزش :
📖
**راهنمای WhiteAesther**
**۱ — نصب**
فایل **arm64-v8a** رو بگیر (تقریباً همه گوشی‌های ۲۰۱۷ به بعد).
مطمئن نیستی؟ **universal** همه‌جا کار می‌کنه، فقط حجمش بیشتره.
**۲ — سه تا نکته اول**
▪️
**Traffic** → گزینه Coverage روی **Whole device** باشه
⚠️
حالت Proxy only خودش هیچی رو رد نمی‌کنه! به‌نظر می‌رسه وصل شده ولی عملاً هیچ ترافیکی از تونل نمی‌ره.
▪️
**Routes** → پروفایل روی **Adaptive**
▪️
**Settings** → اجازه اجرا در پس‌زمینه رو بده، وگرنه با خاموش شدن صفحه قطع می‌شه
**۳ — اگه وصل نشد، به این ترتیب امتحان کن**
**قدم ۱ — پروتکل**
Routes → Advanced → Preferred transport → **MASQUE over HTTP/2**
📌
روی **همراه اول** مدتیه QUIC (یعنی UDP) کاملاً بسته شده. یعنی H3 اصلاً وصل نمی‌شه و فقط H2 جواب می‌ده.
از نسخه ۱.۰.۲ اپ خودش این کار رو می‌کنه.
**قدم ۲ — تیکه‌تیکه کردن TLS**
⭐️
Traffic → Advanced → **Split the TLS handshake** → روشن
فیلترینگ معمولاً فقط تیکه اول بسته رو می‌خونه تا ببینه کجا وصل می‌شی. وقتی تیکه‌تیکه بفرستی، نمی‌تونه بخونه.
اگه با H2 وصل می‌شی ولی کنده، **حتماً اینو امتحان کن**.
**قدم ۳ — پروفایل**
Routes → Profile → **Strict network**
(برای شبکه‌هایی که خیلی چیزها رو می‌بندن)
**قدم ۴ — خاموش کردن IPv6**
Traffic → Addresses → **IPv4 only**
روی خیلی از شبکه‌های موبایل ایران IPv6 نیمه‌کاره‌ست.
**قدم ۵ — مبهم‌سازی**
Traffic → Advanced → Obfuscation → **Aggressive**
💡
اگه قدم ۲ مشکلت رو حل کرد، **Off** رو هم تست کن — شاید پدینگ اضافه فقط داشته سرعتت رو می‌گرفته.
**قدم ۶ — اند‌پوینت دستی**
Routes → Endpoint → Specific address → دکمه **Find endpoints**
⚠️
گزینه Fall back automatically رو روشن نگه دار.
**۴ — گزارش مشکل**
Settings → Diagnostics & logs
۱. Detail level روی **Verbose**
۲. دوباره سعی کن وصل بشی
۳. برگرد و **Send** رو بزن
قبل از ارسال دقیقاً متنی که فرستاده می‌شه رو می‌بینی، و IP‌ها پیش‌فرض مخفی می‌شن. هیچی بدون اجازه‌ات از گوشیت بیرون نمی‌ره.
**نکته:** اون خط خاکستری کوچیک زیر متن بزرگ توی صفحه اصلی، پیغام خود موتوره. برای فهمیدن مشکل همیشه اول اونو بخون.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.0.3
@whitedns</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/whitedns/1476" target="_blank">📅 13:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1474">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gDb8Rmv3cCAm9_RQb8VozFx7HORGQxt0riNe8jSJix6nGgmwDaxS5bWxcCO5NLuCHWgGiDEPf8mufvtNJA_tJ_k55JPMkMROzlZWZ2T6jGAnI-7idR78YU5J9S6Ium75B4-xWHb6i5wj4Nq3ZdOJhzJobbuz6VME9Au7S2FIt7ZrXOSAISG0hEW3_U1fAfzCjpbuXaaUA378FDVS3KvYQahM3-GoWLUcIV1iXwHuPYH7nvQPPtYXkiui1EA-jOjWG7z5nFvPfvtIOa_Y1AIBioEdyj6GZQI4jY1GugD8EkjHqMA-hucJLA2eEYy8f3qw_8X1NP0dAT6G82ifH-mjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS Clean IP Finder 1.3.7
نسخه جدید WhiteDNS Clean IP Finder با تمرکز روی افزایش سرعت پیدا کردن DNS Resolverهای سالم در Desktop و Android منتشر شد.
⚡️
مهم‌ترین تغییرات:
• اجرای همزمان تست‌های DNS Transport و TXT Passthrough برای کاهش Timeout
• اجرای Parallel بررسی‌های NXDOMAIN Hijack
• اضافه شدن Fast Scan با حفظ بررسی‌های اصلی A Record، Recursion، EDNS و TXT Tunnel
• حفظ Full Scan به‌عنوان حالت پیش‌فرض برای بررسی کامل
• بهبود دریافت و Cache اطلاعات Reference DNS
• اضافه شدن UDP/53 Only و TCP/53 Only در Android
• گزارش دقیق‌تر DNS Poisoning، Injection و Hijack
• بروزرسانی دیتابیس Iran & Global ASN شامل IPv4 و IPv6
💻
پشتیبانی از Windows، Linux، macOS و Termux
📱
نسخه Android شامل APKهای مختلف، Universal APK
✅
برای آپدیت نیازی به تغییر تنظیمات قبلی نیست.
📥
دانلود WhiteDNS Clean IP Finder 1.3.7:
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3.7
⚡️
WhiteDNS Clean IP Finder — اسکن سریع‌تر، تشخیص دقیق‌تر و دیتابیس به‌روزتر
@whitedns</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/whitedns/1474" target="_blank">📅 02:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1473">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqFTrgPQzVUBZ6NVEAd9Wx1shs-FF8BVfkU6YkpuHj4ZLfVqglKVph33HslJaD95mOzYuIkPh4s-iKsTmPcytM_GTn1RF9l4r3RdqHf2thOhfV9NqpQpE7FzRDUfukjudFmljhlssKGVOitnLD6M0WBScpsK_8CUX4ZO5dCr557eF5wsSi4UfRNeyc9ZLLVgc9mdRDHhSmDTGJNUg9wfZxUWlcTbV1VqOWgKn6nHFys85GQ6XtX_f18zvd1xaS-rBCgxP0R3G3sXtwIKGGHWkS9AevhL0LQ915Zl7EVpLLF8ou-HEj7x_NRCHs12EI6IB3XOYH9M5y6dVYF5gPt8HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏯️
آموزش ساخت کانفیگ V2Ray با سرور رایگان!   توی این آموزش با استفاده از Wasmer یه سرور رایگان می‌سازیم و در نهایت بدون نیاز به خرید سرور، ۳ تا کانفیگ V2Ray برای مصرف شخصی دریافت می‌کنیم.
⚡️
⏯️
تماشا در یوتیوب  https://youtu.be/EAjOhvuMw8Q</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1473" target="_blank">📅 21:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1472">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⏯️
آموزش ساخت کانفیگ V2Ray با سرور رایگان!
توی این آموزش با استفاده از Wasmer یه سرور رایگان می‌سازیم و در نهایت بدون نیاز به خرید سرور، ۳ تا کانفیگ V2Ray برای مصرف شخصی دریافت می‌کنیم.
⚡️
⏯️
تماشا در یوتیوب
https://youtu.be/EAjOhvuMw8Q</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/whitedns/1472" target="_blank">📅 21:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1471">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hGXdPNp_FLzk0xL1YyJuJwcDlIjsXbnBryQQSFIiee9wjrjKkWdcVtaOfZF6aLcrioBHhnbA9mMMZvZh15kdokqg_xTXocvZ-r2FI6yccfnZ5lCegB0QK0hqMvPR77L6fDIqw74fr-PtGeUb2Oi86ZHZXT9sLHRp7fLkYAauhbmmHVNh3TnWTWaiMXBtETF_oZO0pUP1GYoZWTmQIH61oLOm8iWKlnZ7nLzzF7PPTWZZSSI_iBakCnOzISYEhL3ehaAJe-vKc-l2jAzHj-oSbUnGxAaqVghE2QUfv30b667XU5qoXZSV8mo_hdI04GSylHtrouoJ2eBOKWiZ2jzhHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS دسکتاپ
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/whitedns/1471" target="_blank">📅 18:18 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
