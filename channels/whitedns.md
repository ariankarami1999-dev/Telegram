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
<img src="https://cdn4.telesco.pe/file/ib4cqvMHwT_hbcNetQnO_jwOX731p7mmu00D84bHdCc5qr6GBVskQ5ckFv_SQx-JUqu-SNYQApdGbJ9LpVefn1OU7Vv5IJzM4yRbeXA22ZXn6-neo77d4YorJcTb7Od3mTy0vg6HkBdfDAsXMq_BrBCR3bpR-QMepS074w8Z2CuInDHBfijDO6huGuZQP6Fb5rO2PnY0KUvYj-6HYJJ-RaJ5wl_6ndon638RXuKZr6EwHcwTCKfyv7NDeKroAHesIqsf7dKjfLW6ezPJG0AUxHAqXkq9kcisuFf-aHzZiObXsoZy8k-6msjS-W8Vl8MmFtDxinVajh1U_Bc7dNR1pA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 83.7K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 14:55:14</div>
<hr>

<div class="tg-post" id="msg-729">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سلام عزیزان، امیدوارم در این اوضاعِ به شدت خراب و زندگی در کشوری که توسط یک رژیم فاسد اداره میشه همچنان قویی باشید و حال دلتون عالی باشه. همونطور که میدونید ما
به شدت
با پروسه‌ی فروش
مخالف
بوده ایم و تمام فعالیت های ما برای
تمام
مردم ایران به صورت
کاملا
رایگان
بوده؛ اما جا داره که از تمام کسانی که چه با کریپتو و چه با استارز زدن به پست ها از ما حمایت میکنند تا فعالیت چنل و سرورها مداوم باشه، تشکر کنم. در این مدت دقت کردم که تمامی پست های چنل حداقل یک استارز خورده و بدونید که تمام این حمایت ها حتی یک استارزی که میزنید برای ما خیلی با ارزشه و از شما قدردانی میکنیم که در این راه دشوار و مبارزه با این حکومت خون‌خوار در کنار ما ایستاده اید!
❤️
- کوچیک شما Patrick.
WhiteDNS-Team
@WhiteDNS</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/whitedns/729" target="_blank">📅 14:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-728">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">لینک داخلی تمام پلتفرم های برنامه‌ی WhiteDNS Desktop:
Macos-amd64:
https://guardts.ir/f/736498ddfb14
Macos-arm64:
https://guardts.ir/f/4594c5008167
Windows-x64(amd64):
https://guardts.ir/f/2549b69980b3
Windows-arm64:
https://guardts.ir/f/05e3847a8a43
@WhiteDNS</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/whitedns/728" target="_blank">📅 13:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-727">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فیلم آموزش استفاده از نسخه WhiteDNS Desktop</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/whitedns/727" target="_blank">📅 13:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-726">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فیلم آموزش استفاده از نسخه WhiteDNS Desktop</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/726" target="_blank">📅 11:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-725">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nssB1r5TuHvpxPf0SaApApdjc9qVBTp7BfTVg68imKGlkC0cP1btD2dE1u5iaxxhWCCVqM45Q4Ti_avoQLW-LwnLI3w3ALzwvw5LsMqCR8pXvVotk9Jw3PAm7OzbRK-j1qV-h5On0FMe20cE--slgOhHiZ5nELB6TbOHFHAscTa7PoWBxLPYpJ07bNTE_NSEDLv0UEccbwU8YGSD01he6yZTGHSfSuCCZpdJqk3VVP1WfMQ4yLU-VVNPUvC43H0XY1yOuyF0pJHP-mKGhEv5JsZpx5ZvDhkcrNnWcvaZAh0JVnWvmiopxeXTrwF2vJEXZfT0EvVfcWqf-3ebdLl9jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی مک، دوستانی که مشکل باز کردن اپ رو دارید، دستور زیر رو اجرا کنید
chmod +x "/Applications/WhiteDNS Desktop.app/Contents/MacOS/WhiteDNS Desktop"
xattr -dr com.apple.quarantine "/Applications/WhiteDNS Desktop.app"
open "/Applications/WhiteDNS Desktop.app"</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/725" target="_blank">📅 11:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-721">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta2-macos-amd64.zip</div>
  <div class="tg-doc-extra">25.8 MB</div>
</div>
<a href="https://t.me/whitedns/721" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه WhiteDNS Desktop V1.0.0-beta2
✅
حل مشکل باز کردن در ورژن های قدیمی مک
✅
حل مشکل وصل نشدن و خطا بعد از ۴۵ ثانیه
✅
حل مشکل وارد کردن کانفیگ به صورت گروهی
✅
حل اضافه شدن دگه ذخیره برای ریزالور های سالم و. فعال به صورت جداگانه
✅
حل مشکل مشکی شدن صفحه در ویندوز
✅
اضافه شدن نسخه های لینوکس</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/721" target="_blank">📅 10:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-717">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">macos-amd64.zip</div>
  <div class="tg-doc-extra">25.8 MB</div>
</div>
<a href="https://t.me/whitedns/717" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎉
WhiteDNS Desktop منتشر شد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/717" target="_blank">📅 08:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-716">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCiPBV4a8Ibh0KqJoaonbQ9awwyc9vsebup7Q5rVc0tzm0nFWpeZzM7AF55Q_cpjHzypg9PwBAgAR1zJuJ0HqI1Y10HtLpkk3sbfYhNEIufLHV3p5UEe9lMhHZcJXJxuWC69Oi3_xvgI2GdrsVnp6qPUlox8-S1TQg_mDaBXuHGrwk9z_z-Cm2imnAfUohr-sog2GFZSYLIA97-8xj1E7WFA8UzG3ZwyHFvmnONDXRRCFa-k5_MxNUIKnw6_5NO09OKYixS-RNrhCyMZGcmCXaF2JLp-sAf6fKwVX6S8iCQoNwOHzNKs6uvCejtN-9loCJBkSCcdntToqHWK3Zi_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
WhiteDNS Desktop منتشر شد
نسخه دسکتاپ WhiteDNS حالا آماده استفاده است.
این برنامه برای کسانی ساخته شده که می‌خواهند اتصال‌های MasterDNS و StormDNS را روی کامپیوتر، ساده‌تر، سریع‌تر و بدون درگیر شدن با ترمینال و فایل‌های تنظیمات اجرا کنند.
با WhiteDNS Desktop می‌توانید پروفایل اتصال را وارد کنید، Resolverها را مدیریت کنید، اتصال را فقط با یک دکمه روشن یا خاموش کنید و وضعیت همه‌چیز را به‌صورت زنده ببینید.
✨
امکانات اصلی
✅
اتصال و قطع اتصال فقط با یک دکمه
✅
رابط گرافیکی ساده برای Windows و macOS
✅
پراکسی محلی آماده برای مرورگرها و برنامه‌های دیگر
✅
پشتیبانی از SOCKS و HTTP از طریق sing-box
✅
امکان فعال کردن System Proxy
✅
وارد کردن پروفایل‌های آماده با لینک‌های
stormdns://
✅
ساخت و مدیریت چند پروفایل اتصال
✅
ساخت و مدیریت چند لیست Resolver
✅
بررسی خودکار معتبر بودن Resolverها
✅
نمایش Resolverهای فعال، آماده‌باش و ردشده
✅
نمایش سرعت دانلود، سرعت آپلود و مصرف کل داده
✅
نمایش روند اتصال و درصد پیشرفت هنگام راه‌اندازی
✅
امکان توقف و ادامه دادن تست MTU هنگام اتصال
✅
خروجی گرفتن از تنظیمات به‌صورت
client_config.toml
✅
بخش لاگ و جست‌وجوی لاگ‌ها برای عیب‌یابی راحت‌تر
⚙️
تنظیمات پیشرفته برای شبکه‌های ضعیف و ناپایدار
برای کاربرانی که روی اینترنت‌های محدود، ضعیف یا ناپایدار هستند، تنظیمات پیشرفته هم داخل برنامه قرار داده شده است:
✅
انتخاب روش بالانس بین Resolverها
✅
تنظیم Packet Duplication برای پایداری بیشتر
✅
تنظیم فشرده‌سازی آپلود و دانلود
✅
تنظیم MTU، Timeout، Retry و تعداد تست هم‌زمان
✅
کنترل Workerها، Streamها و صف‌ها برای سیستم‌های مختلف
✅
وجود Watchdog برای بررسی زنده بودن اتصال
🔍
ابزار Scanner داخلی
در این نسخه، یک ابزار Scanner هم داخل برنامه اضافه شده است تا تست و بررسی Endpointها راحت‌تر شود:
✅
تست سریع یک Host با چند پورت
✅
اسکن گروهی از فایل‌های TXT، CSV یا JSON
✅
تست پروتکل‌های TCP، TLS، HTTP، WebSocket، UDP، QUIC/H3 و DNS
✅
نمایش Score، Grade، Latency، Jitter، Packet Loss و Stability
✅
بررسی اینکه Endpoint برای Tunnel آماده هست یا نه
✅
امکان دیدن و کپی کردن نتیجه کامل به‌صورت JSON
این نسخه برای کاربران عادی طراحی شده تا اتصال راحت‌تر و بدون دردسر انجام شود؛ اما برای کاربران حرفه‌ای هم تنظیمات دقیق‌تر در دسترس است تا بتوانند اتصال را با شرایط شبکه خودشان بهتر هماهنگ کنند.
⚠️
توجه: این نسخه هنوز بتا است.
اگر مشکلی مشاهده کردید، ارسال گزارش خطا، لاگ برنامه و توضیح شرایط شبکه شما کمک زیادی به بهتر شدن نسخه‌های بعدی می‌کند.
ممنون از همراهی شما با WhiteDNS
🤍</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/716" target="_blank">📅 08:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-715">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9WR76gczOfN0tSwOpN2cG_ZuA7lG1ZzwrPqTOxh8OFVutXWH0vlCzgByJ6Get5xQR0XgtxbdgNje0aSJoHcwb31Ge5otbH4iYBWWtR-1MclPtMriXqQ6TyxXV9rGNWrvDzb_Lyy6ucd0mZ4LvtlzOt0hiyy7_s_cXL5w2NqU8juM2snl6uArowJx9yxjubemfmrILCNbb7rLtqjkKmno0nMqLj7zF1dVEeNPYqEpfQY_J5J_SN9uf4myxUuL2jD7grjurgzcBRa7a8GKLKFQoytaDODFTAueIsz3SEImXg9dt7fQSuzaJVFxmQEZ4dCppqYCkMKugW713wUxwo4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همراهان عزیز،
بعد از بازخود هایی که ما از ورژن قبلی اپ ویندوز گرفتیم، تصمیم به بازنویسی این نرم‌افزار برای سیتم عامل های
مک ، ویندوز و لینوکس
گرفتیم.
تقریبا تمام امکانات اپلیکیشن اندروید در این اپ خلاصه شده اما با قدرت و منابع بیشتر.
سعی میکنیم هرچه زودتر اپ رو آماده و در اختیارتون قرار بدیم.
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/whitedns/715" target="_blank">📅 07:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-714">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">خب این هم آموزش SNI Spoof برای مک.
فرآیندش برای ویندوز و لینوکس کاملاً مشابه هم هستش. فقط باید فایل اجرایی‌ای که برای sni spoof هستش رو مطابق سیستم‌عاملتون دانلود کنین.
فرقی هم نداره که از چه برنامه‌ای برای کانفیگ‌ها استفاده کنین.
لینک دانلود برنامه SNI Spoof برای مک و لینوکس
برنامه آپلود شده در تلگرام
لیست کانفیگای جمع آوری شده توسط متین عزیز.
کانفیگ JSON
لینک دانلود ویدئو بالا برای اینترنت ایران.
@khosrow_v2ray</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/714" target="_blank">📅 02:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-713">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy2mjF73VvJ2t82jFhKZgZ_rPbbIp_GbjuixGPEktk-2jnhPeltsvkyR5ieYpOooFEtzY6KK44Ydkl7X2Yi9zwe5vkdMiVtY1hcfQ9xnbK_sdNqtHRwUcP_KDEHzdGZFd0sMR7iFrgJUkPIxiuxtnUeWKZgiq0OwywU9x1X8PHiJ4_eb-JeYJIaevMwQ1ggupcH5IdiTalM3XAQ0227_kPIm1C56Ix7KJebihLaNwpkiHr5BIdxIJpcP30Ah7lW6eAOj23nrAgz_NpCadz-KRAMk-0YBZ7EqsZkSb1IOAuNCoqYDh2w1Yq3bLCggOUXuoPbiaQHhGak8Z6Jky8nisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد میکنم تنظیمات موازی سازی MTU رو بین ۵۰ تا ۳۰۰ بسته به جدید قدرت گوشی همراهتون بذارید.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/whitedns/713" target="_blank">📅 18:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-708">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/whitedns/708" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/whitedns/708" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-707">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUZWq_yOHguQTydNJvSVh2N2PZTLu_JvCifBI62V6Re_PwetHPB_8IEXWdJ1c5dj8zg6mWTtba-cdVXvdPM9av8697WiIMjtzS3YxsLLNEuNcAkKXO_ipalUyHx5kSJnjF4Y8TeQ83iONIjaGXWtfn9PQTGPO1MrzTBvB2QFpTIVybFQVX7cw8vBowjb18_9i-6vLuts8mwTu3Du9MXCwh4o4PA23Nq9QE_7J0BzrEEnfM9YxRK7qoS34PNpdmlXW_h34EeVC_ajd3bJfjyMLlRcVzLWdscU4myskvI-KRJVV2rNvoE4MKQAin07R8lDQWmHuT0LL9qtCl6Mg2qkDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همراهان عزیز
تغییر بزرگی در این ورژن انجام نشده. تمرکز در این نسخه روی
بهبود  تست موازی تنظیمات بوده. در این نسخه تنطیمات بیشتری و بهینه تری به این قابلیت اضافه شده.
✅
نسخه اپلیکیشن به 1.5.1 ارتقا پیدا کرده
✅
جدا شدن تنظیمات پر مصرف و بهینه در تست موازی.
✅
بعد از یک همه پرسی در کانال، حالا تنظیمات در ۱۰ دسته متفاوت تقسیم شده تا بهینه ترین تنظیمات بر اساس ریزالور های انتخاب شده برای شما استافده شود.
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/whitedns/707" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-705">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">برای باز کردن اینستاگرام در مرورگر گوشی (بدون اینکه وارد اپلیکیشن شوید)، می‌توانید این مراحل را دنبال کنید:
📱
💻
۱.
مرورگر خود را باز کنید:
🌐
وارد مرورگر گوشی خود (مثل Chrome در اندروید، Safari در آیفون، یا Firefox) شوید.
۲.
به سایت اینستاگرام بروید:
📍
در نوار آدرس بالای صفحه،
[www.instagram.com](https://www.instagram.com)
را تایپ کرده و جستجو کنید.
۳.
وارد حساب کاربری خود شوید (Log In):
🔐
در صفحه باز شده، روی گزینه
Log In
ضربه بزنید و نام کاربری (یا ایمیل/شماره موبایل) و رمز عبور خود را وارد کنید.
نکته مهم (جلوگیری از باز شدن خودکار اپلیکیشن):
⚠️
بسیاری از اوقات، وقتی آدرس اینستاگرام را در مرورگر وارد می‌کنید، گوشی به طور خودکار شما را به اپلیکیشن اینستاگرام (اگر نصب باشد) هدایت می‌کند. برای جلوگیری از این اتفاق، می‌توانید از ترفندهای زیر استفاده کنید:
راه حل اول (سریع‌ترین راه):
🚀
مرورگر خود را در حالت
ناشناس (Incognito یا Private)
باز کنید و سپس سایت اینستاگرام را در آن وارد کنید. در این حالت، لینک‌ها به اپلیکیشن منتقل نمی‌شوند.
راه حل دوم (تغییر تنظیمات در اندروید):
🤖
به تنظیمات گوشی (Settings) بروید.
بخش برنامه‌ها (Apps) را باز کنید و Instagram را پیدا کنید.
به بخش
Open by default
(باز شدن به‌طور پیش‌فرض) یا
Set as default
بروید.
گزینه باز کردن لینک‌های پشتیبانی‌شده (Open supported links) را خاموش کنید یا روی حالت "همیشه بپرس" (Ask every time) قرار دهید.
راه حل سوم (در سافاری آیفون):
🍎
در گوگل کلمه Instagram را جستجو کنید. روی لینک سایت اینستاگرام در نتایج جستجو
انگشت خود را نگه دارید
(Long press) و از منوی باز شده گزینه
Open in New Tab
را انتخاب کنید.
@whitedns
📡</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/whitedns/705" target="_blank">📅 07:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-704">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">WhiteDns-Windows-Setup.exe</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/whitedns/704" target="_blank">📅 07:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">11 MB</div>
</div>
<a href="https://t.me/whitedns/703" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteDns Windows 1.0.6
🖥
🔌
راهنمای اتصال هوشمند (Smart Connect)
🤖
قابلیت اتصال هوشمند به برنامه WhiteDns کمک می‌کند تا بهترین تنظیمات اتصال را به‌طور خودکار انتخاب کند. کاربران عادی نیازی به تغییر دستی تنظیماتی مانند MTU، Workers (تعداد پردازش‌گرها)، Packet Duplication (تکثیر بسته‌ها)، فشرده‌سازی (Compression) یا سایر تنظیمات در بخش پیشرفته (Advanced) ندارند.
✅
نحوه استفاده
📝
۱. برنامه
WhiteDns Windows
را باز کنید.
🪟
۲. به تب
Connect
(اتصال) بروید.
🔗
۳. مطمئن شوید که گزینه
Smart Connect
روی حالت روشن (
On
) قرار دارد.
🟢
۴. هدف اتصال خود را انتخاب کنید:
Stable (پایدار)
🛡
بهترین گزینه برای شبکه‌های ضعیف یا فیلترشده. این امن‌ترین و مطمئن‌ترین گزینه است.
Balanced (متعادل)
⚖️
برای اکثر کاربران توصیه می‌شود. این حالت تلاش می‌کند ضمن حفظ پایداری اتصال، سرعت خوبی نیز ارائه دهد.
Fast (سریع)
🚀
بهترین حالت برای زمانی که شبکه شما از قبل قوی است. ممکن است در این حالت از تنظیمات تهاجمی‌تری استفاده شود.
۵. موتور (Engine) را انتخاب کنید:
⚙️
MasterDNS
برای اکثر کاربران و اتصالات پایدار توصیه می‌شود.
StormDNS
در صورتی از این گزینه استفاده کنید که پروفایل/سرور شما برای StormDNS ساخته شده است یا می‌خواهید موتور سریع‌تر را آزمایش کنید.
⛈
۶. حالت پروکسی را انتخاب کنید:
🌐
System proxy (پروکسی سیستم)
برای وب‌گردی معمولی توصیه می‌شود. مرورگرها و بسیاری از برنامه‌های ویندوز به‌طور خودکار از WhiteDns استفاده خواهند کرد.
🖥
SOCKS5 only (فقط SOCKS5)
اگر می‌خواهید پروکسی را به‌صورت دستی در برنامه‌هایی مانند تلگرام تنظیم کنید، از این گزینه استفاده کنید.
📱
۷. روی
Connect
کلیک کنید.
👆
چه اتفاقاتی به‌طور خودکار رخ می‌دهد؟
🔄
وقتی اتصال هوشمند (Smart Connect) روشن است، WhiteDns کارهای زیر را انجام می‌دهد:
- استفاده از موتور انتخاب‌شده (MasterDNS یا StormDNS).
🛠
- بررسی تنظیمات موفق که در دفعات قبل جواب داده‌اند.
✔️
- انتخاب یک پیش‌تنظیم (Preset) مناسب بر اساس هدف شما.
🎯
- استفاده از بهترین تنظیمات شناخته‌شده برای تحلیلگر (Resolver).
📊
- امتحان کردن تنظیمات جایگزین امن‌تر (Fallback) در صورتی که تلاش اول ضعیف باشد.
🛡
- به خاطر سپردن تنظیمات موفق برای استفاده در دفعات بعدی.
💾
کدام هدف (Goal) را باید انتخاب کنم؟
🤔
ابتدا از
Balanced
استفاده کنید. این بهترین حالت پیش‌فرض برای اکثر کاربران است.
✅
در شرایط زیر از
Stable
استفاده کنید:
- اتصال مرتباً با شکست مواجه می‌شود.
❌
- اینترنت شما به شدت فیلتر است.
🚫
- تونل وصل می‌شود اما اتصال به سرعت قطع می‌گردد.
- سرعت برایتان نسبت به پایداری و اطمینان در درجه دوم اهمیت قرار دارد.
در شرایط زیر از
Fast
استفاده کنید:
- حالت Balanced در حال حاضر به خوبی کار می‌کند.
- سرعت بیشتری می‌خواهید.
⚡️
- شبکه یا سرور شما قوی است.
💪
تنظیمات پیشنهادی برای کاربران عادی
👥
اتصال هوشمند (Smart Connect):
On (روشن)
🟢
هدف (Goal):
Balanced
⚖️
موتور (Engine):
MasterDNS
🛠
پروکسی:
System proxy
🌐
سپس روی
Connect
کلیک کنید.
👆
اگر متصل نشد چه کار کنیم؟
🛠
این مراحل را به ترتیب امتحان کنید:
۱. هدف را به
Stable
تغییر دهید.
🛡
۲. گزینه Smart Connect را همچنان
On (روشن)
🟢
نگه دارید.
۳. دوباره روی
Connect
کلیک کنید.
۴. اگر باز هم متصل نشد، به بخش
Resolvers
بروید و یک اسکن اجرا کنید.
🔍
۵. بهترین نتایج Resolver را اعمال (Apply) کنید و سپس دوباره سعی کنید متصل شوید.
✅
برای کاربران تلگرام
💬
اگر از گزینه
SOCKS5 only
استفاده می‌کنید، پروکسی تلگرام دسکتاپ را به این شکل تنظیم کنید:
نوع (Type): SOCKS5
هاست (Host):
127.0.0.1
پورت (Port): 18000
نام کاربری/رمز عبور (Username/Password): خالی بگذارید
🔓
اگر از
System proxy
استفاده می‌کنید، مرورگرها معمولاً به‌طور خودکار متصل می‌شوند، اما تلگرام ممکن است همچنان به وارد کردن تنظیمات دستی SOCKS5 نیاز داشته باشد.
برای کاربران حرفه‌ای
🎓
اگر گزینه اتصال هوشمند را خاموش (
Off
) کنید، WhiteDns از پروفایل فعلی و تنظیمات پیشرفته‌ی (Advanced) شما دقیقاً همان‌طور که هستند استفاده خواهد کرد. این ویژگی برای زمانی که می‌خواهید کنترل کامل و دستی روی تنظیمات داشته باشید بسیار مفید است.
🔧
🚫
خیلی مهم :
به هیچ عنوان هیچ نرم افزار vpn دیگری مثل v2ray و یا ..... نباید روی سیستم شما باز باشد . مطمن شوید که حتی در پس زمینه هم بسته شوند
🚫
برای تست روی مرورگر ها حتما از گزینه New Private window یا New incognito window استفاده کنید
👍
@whitedns</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/whitedns/703" target="_blank">📅 07:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/smF0TPJOukoDpwEa14cp6X-5ih2bTcnsAHzCVgxKOIaWMcA2UI2Nuc0xfOmnVEVUXd7nSQI01NkD_XzAtxGolozftjNv0-JrJZsm0YDn4gIa0euOUE8EVKeR9FiC0_gYNLwmPb_Qt9Tk27WUnVEJzNZmNVbS6KWDAdA9GvIbItA3vVnGUpiPrio40uUXB4-dGtbqaahmQf2ZSLc2A23Hg3MzPt7RjpmB99SxoPxqKk0jDEKUH2fHWFw4BIerlmKbJ_zipsQvESuvp9ap1YjnCJw1K6_glps4tnx6G1niIOWFx8e8T2b0ONM-MKm4BsoNwmvrDU3BzPZ2pxu6zKhVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در نسخه ۱.۰.۶ -
WhiteDns Windows
🪟
قابلیت
«اتصال هوشمند» (Smart Connect)
اضافه شده است؛ یک حالت اتصال خودکار جدید که به کاربران کمک می‌کند بدون نیاز به تغییر دستی تنظیمات در تب پیشرفته (Advanced)، به تنظیماتی پایدار و مطمئن دست پیدا کنند.
🚀
اکنون قابلیت اتصال هوشمند می‌تواند اتصال را بر اساس موتور (Engine) انتخاب‌شده، سرور، کیفیت تحلیلگر (Resolver) و نتایج موفق قبلی تنظیم و بهینه‌سازی کند.
⚙️
کاربران می‌توانند یک هدف ساده را انتخاب کنند:
پایدار (Stable)
🛡
متعادل (Balanced)
⚖️
سریع (Fast)
⚡️
. سپس برنامه پیش از برقراری ارتباط، به‌طور خودکار تنظیمات انتقال و تحلیلگر امن‌تری را برای MasterDNS یا StormDNS انتخاب می‌کند.
همچنین این نسخه نتایج موفق اتصال هوشمند را به تفکیک هر سرور، موتور و شبکه به خاطر می‌سپارد؛ در نتیجه اتصالات بعدی می‌توانند با استفاده از تنظیماتی که پیش‌تر جواب داده‌اند، سریع‌تر برقرار شوند.
🧠
اگر مسیر اتصال ضعیف باشد، قابلیت اتصال هوشمند پیش از نمایش پیام خطا، تنظیمات جایگزین امن‌تری (Fallback) را امتحان می‌کند.
🔄
صفحه اتصال (Connect) با یک پنل کنترل جدیدِ اتصال هوشمند به‌روزرسانی شده است، در حالی که امکان اتصال دستی معمولی همچنان برای کاربران حرفه‌ای در دسترس قرار دارد.
🛠
@whitedns</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/whitedns/702" target="_blank">📅 07:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-poll">
<h4>📊 با اپلیکیشن های ما تونستید به اینترنت متصل بشید؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/whitedns/701" target="_blank">📅 05:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-700">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
پروفایل های وایت دی ان اس (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲۸ اردیبهشت
👾
لینک دانلود
کلاینت :
1️⃣
WhiteDNS
1.5.0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygxKSIsInNlcnZlciI6eyJkb21haW4iOiJ2MS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygyKSIsInNlcnZlciI6eyJkb21haW4iOiJ2Mi5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygzKSIsInNlcnZlciI6eyJkb21haW4iOiJ2My5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg0KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NC5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg1KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg2KSIsInNlcnZlciI6eyJkb21haW4iOiJ2Ni5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg3KSIsInNlcnZlciI6eyJkb21haW4iOiJ2Ny5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg4KSIsInNlcnZlciI6eyJkb21haW4iOiJ2OC5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg5KSIsInNlcnZlciI6eyJkb21haW4iOiJ2OS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygxMCkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEwLm1hc2lyLXNlZmlkLm15IiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
⚡️
پک ریزالور
👍
تنظیمات مخصوص وایت دی ان اس
⬅️
نحوه ی اضافه کردن پروفایل ها
⬅️
فیلم اموزش وایت دی ان اس
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
(پیشنهادی)
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/whitedns/700" target="_blank">📅 20:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-699">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/whitedns/699" target="_blank">📅 18:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-698">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">راهنمای_جامع_استفاده_از_وایت_دی_ان_اس_ویندوز_.docx</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/whitedns/698" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
راهنمای جامع وایت دی‌ان‌اس (WhiteDns) برای ویندوز منتشر شد!
🚀
کاربران عزیز، اگر برای اتصال و تنظیم برنامه WhiteDns در ویندوز با چالشی مواجه هستید، این راهنمای کامل دقیقا برای شما آماده شده است. برنامه WhiteDns یک ابزار قدرتمند دسکتاپ برای تونلینگ و ساخت پروکسی محلی است و با استفاده از این راهنما می‌توانید بالاترین سرعت و پایداری را تجربه کنید.
📌
خلاصه‌ای از آنچه در این راهنما یاد می‌گیرید:
🔹
شروع سریع و آسان:
آموزش قدم‌به‌قدم ایجاد پروفایل، وارد کردن دامنه، کلید رمزنگاری (Encryption Key) و اتصال اولیه.
🔹
انتخاب حالت پروکسی:
تفاوت بین حالت دستی (SOCKS5 only) و اعمال پروکسی روی کل سیستم (System proxy) برای مرورگرها.
🔹
ابزار قدرتمند اسکنر (Resolvers):
آموزش پیدا کردن سریع‌ترین و پایدارترین تحلیلگرهای DNS با استفاده از اسکنر داخلی برنامه (در حالت‌های سریع، عمیق و با دقت بالا).
🔹
تنظیمات پیشرفته و موتورها:
معرفی تفاوت‌های موتور MasterDNS و StormDNS و نحوه استفاده از پروفایل‌های آماده (Presets) مانند
Stable Iran
(برای بالاترین پایداری در شبکه‌های محدود) تا حالت‌های تهاجمی‌تر (Aggressive).
🔹
تنظیمات مخصوص برنامه‌ها:
راهنمای دقیق ست کردن پروکسی محلی (
127.0.0.1:18000
) روی تلگرام دسکتاپ، فایرفاکس، کروم و مرورگر اج.
🔹
رفع مشکلات (Troubleshooting):
راهکارهای عملی برای حل مشکلاتی مثل وصل نشدن مرورگر با وجود اتصال برنامه، قطع شدن مداوم، و یا رفع گیر کردن روی راه‌اندازی کند تونل.
💡
فرمول طلایی اتصال:
بهترین و امن‌ترین مسیر برای اکثر کاربران این است: وارد کردن اطلاعات تونل
⬅️
اسکن تحلیلگرها
⬅️
اعمال بهترین تحلیلگر
⬅️
انتخاب حالت Stable Iran
⬅️
اتصال!
برای استفاده حرفه‌ای از این نرم‌افزار و دور زدن قطعی‌ها، حتماً فایل راهنمای کامل را مطالعه کنید.
#اموزش_ویندوز_whitedns
@whitedns</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/698" target="_blank">📅 18:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-697">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">11 MB</div>
</div>
<a href="https://t.me/whitedns/697" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تغییرات WhiteDns ویندوز نسخه 1.0.5
بازسازی رابط مدرن
بهبود جزئیات کوچک رابط کاربری و تراز کارت‌ها برای ظاهری تمیزتر و یکدست‌تر در دسکتاپ.
🖥
✨
اسکنر با دقت بالا :
یک اسکنر با دقت بالا برای شرایط سخت اضافه شد
طراحی شمارنده رزولور بهبود یافته
به‌روزرسانی استایل شمارنده رزولور تا با چیدمان کارت‌های اطراف هماهنگ‌تر شده و ظاهری مدرن‌تر داشته باشد.
🎨
پشتیبانی از سینی ویندوز بهبود یافته
رفتار سینی برنامه به‌روزرسانی شد تا در ویندوز طبیعی‌تر احساس شود و در پس‌زمینه در دسترس بماند.
🪟
🔌
فعالیت شبکه برای حالت SOCKS5 اصلاح شد
فعالیت شبکه اکنون ترافیک را زمانی که برنامه‌ها از پروکسی محلی SOCKS5 استفاده می‌کنند، ردیابی می‌کند، به جای نمایش فعالیت فقط از طریق مسیر HTTP/System Proxy.
🌐
🔍
سازگاری پورت SOCKS سفارشی
فعالیت شبکه اکنون هنگام تغییر پورت SOCKS در تب پیشرفته نیز به کار خود ادامه می‌دهد.
⚙️
حافظه اسکن رزولور اضافه شد
برنامه اکنون بهترین نتیجه اسکن رزولور را به خاطر می‌سپارد و اسکن‌های کامل تکراری را هنگام اتصال مجدد با مجموعه رزولور یکسان کاهش می‌دهد.
💾
🚀
تجربه اتصال مجدد سریع‌تر
اتصالات مجدد باید روان‌تر احساس شوند زیرا برنامه از اسکن مجدد غیرضروری رزولورها هنگام در دسترس بودن نتیجه معتبر قبلی خودداری می‌کند.
⚡️
وارد کردن دستی رزولور اضافه شد
گزینه وارد کردن .txt در کارت «وارد کردن / رزولورهای دستی» برای بارگذاری آسان‌تر لیست رزولورها اضافه شد.
📥
📝
نکات اتصال
از لیست رزولور باکیفیت و کوچک‌تر برای راه‌اندازی سریع‌تر استفاده کنید.
🚀
رزولورهای پایدارتر را در بالای لیست نگه دارید.
📌
هنگام آزمایش اتصال، ابتدا از حالت SOCKS5 استفاده کنید.
🧪
اگر حالت System Proxy با یک برنامه ناسازگار است، آن برنامه را به‌صورت دستی برای استفاده از
127.0.0.1
و پورت SOCKS نمایش داده شده در WhiteDns پیکربندی کنید.
⚙️
مگر در صورت نیاز، از تغییر مقادیر تونل پیشرفته خودداری کنید؛ مقادیر پیش‌فرض معمولاً پایدارترین هستند.
🛡
@whitedns</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/whitedns/697" target="_blank">📅 18:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-696">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">برای اشتراک‌گذاری اتصال
WhiteDNS
روی وای‌فای با دستگاه‌های دیگر، کافی است داخل بخش تنظیمات، مقدار
Proxy Address
را از:
127.0.0.1
به این مقدار تغییر دهید:
0.0.0.0
بعد از انجام این تغییر، در بخش
Connection Info
یک آدرس IP جدید به شما نمایش داده می‌شود. از همان IP می‌توانید برای تنظیم پروکسی روی دستگاه‌های دیگری که به همان شبکه وای‌فای متصل هستند استفاده کنید.
لطفاً دقت کنید که برای اتصال دستگاه‌های دیگر، نباید از
127.0.0.1
استفاده کنید. باید حتماً از آدرس IP جدیدی که داخل
Connection Info
نمایش داده می‌شود استفاده شود.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/whitedns/696" target="_blank">📅 18:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-695">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پروژه‌ی TheFeed که متعلق به Sarto هست و قبلا درموردش حرف زدیم برای ios هم عرضه شد! میتونید با نصب برنامه‌ی Testflight در Appstore و رفتن به لینک زیر برنامه رو دانلود کنید:
https://testflight.apple.com/join/J6bfxDdZ
لینک کانال TheFeed
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/whitedns/695" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-694">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجاوید نامان ایران(Bamdad)</strong></div>
<div class="tg-text">کانفیگ برای کلاینتهای وایت دی ان اس  بر روی اندروید، آی او اس، مک اوس، ویندوز و لینوکس
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDIiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5iYW1hay54eXoiLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDMiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5pcmRtYy5jb20iLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDQiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5qbmlyLm15IiwiZW5jcnlwdGlvbl9rZXkiOiJhYWY0YjYtQEphdmlkbmFtYW5JcmFuLWFhZjRiNmZmZiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5pZ29paS5vcmciLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDYiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5qYXZpZG5hbWFuLmNvbSIsImVuY3J5cHRpb25fa2V5IjoiYWFmNGI2LUBKYXZpZG5hbWFuSXJhbi1hYWY0YjZmZmYiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDEiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5uYW1hZC54eXoiLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/whitedns/694" target="_blank">📅 16:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-693">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه تشکر از کانال
https://t.me/Masir_Sefid
این دوستان عزیز از روز های اول شروع کردن به آموزش، تنظیمات و اشتراک گذاری سرور های رایگان برای اتصال رایگان.
اگر دوست دارید عضو چنلشون بشید و از آموزش، سرور و تنظیماتی که میذارن استفاده کنید.
ممنون از همه دوستانی که برای اتصال رایگان هموطن هامون تلاش میکنن
🫡
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/whitedns/693" target="_blank">📅 15:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-692">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">لیست ۱۰۰ ریزالور با بیشترین درخواست ها به سرور های WhiteDNS
185.94.98.34
185.142.158.162
5.160.128.142
2.189.44.68
93.115.127.9
109.230.89.90
217.219.162.200
94.232.173.28
134.255.206.205
80.75.7.2
185.208.174.167
185.37.55.30
185.51.201.58
185.53.142.174
185.255.91.60
185.88.178.196
164.138.17.122
78.157.41.60
5.202.252.30
31.214.169.244
185.109.61.27
2.188.21.58
185.213.11.85
178.252.128.66
2.188.21.70
185.105.101.1
2.189.44.98
109.107.159.86
77.238.123.179
2.188.21.46
172.64.32.0
173.245.58.0
151.232.36.4
108.162.192.0
185.208.175.228
185.137.25.146
185.208.183.29
207.211.215.145
185.50.37.52
2.188.21.138
109.230.206.175
2.189.44.14
85.185.1.10
46.32.31.30
109.72.197.1
2.189.44.84
2.189.44.82
80.191.163.249
2.189.44.86
2.189.44.83
2.189.44.85
78.39.234.140
85.185.157.181
37.191.95.70
185.191.79.210
185.141.105.139
74.80.77.247
78.38.174.2
74.63.24.210
74.63.24.211
2.189.44.93
185.53.141.230
2.189.44.94
74.80.77.246
2.189.44.91
2.189.44.92
2.189.44.90
2.188.21.146
172.253.228.147
74.63.24.205
172.253.12.151
172.253.12.155
172.253.228.150
172.253.228.145
172.253.12.16
172.253.13.147
172.253.13.146
172.253.13.156
172.253.13.154
172.253.13.152
172.253.13.149
172.253.228.156
78.38.114.66
172.253.12.221
172.253.12.150
172.253.13.157
172.253.12.154
172.253.12.210
172.253.13.145
172.253.13.148
172.253.12.212
172.253.13.151
172.253.12.216
172.253.228.148
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/whitedns/692" target="_blank">📅 15:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-691">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">WhiteDNS-1.5.0-x86.apk</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/whitedns/691" target="_blank">📅 13:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-690">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستانی که تازه اضافه شدید، سوال دارید یا نمی‌دونید چطوری از WhiteDNS استفاده کنید، تمام مراحل زو اینجا براتون توضیح دادیم
https://t.me/whitedns_group/32380/32404</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/whitedns/690" target="_blank">📅 13:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-685">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/whitedns/685" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر از مطمین نیستید، ورژن یونیورسال رو دانلود بکنید.</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/whitedns/685" target="_blank">📅 13:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-683">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUjEG32eBlogrP-ARUliHGQhd7Grhf-PayEJiaZ3BQHqrL3gFfaRIaV0RsyIHw2z0XuxL9VXHYu5INrDUHKDc2ppPVTOPqNIbF7MRaa8VU3LnbEHRx5kUa16byK8JDUJAVdefHTl3XlTKtS0DgGWHlCGHUpO1XRwKTggkUi-3WjGuefRl4d13ZOPXnXl_D-Kh_D-8a4IOKkarBMv-060UzVc-RPCymbHD3zjdrFNaxBTRxGe-kUe-XKajGdmqEpExxv-M3bgxamh_ZQX9yNXgkafw8ulwI-28tXtF4iWLH9tUMjJxBwrDOy4NgUJPu-toatGRjNtkvugEiuxG-Y3_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWFcxyW9YZps0mWgoNrDPKeQh0v8GKtMxDMPUZZFUvaFA8NhiCPJjQaLBEA7kM_3nTbxhNUPjnGtLm7YAhMdRuJMPUxtsHxW113pO2EfUd1Kuxyfdg-CMNE96v9C0owNLdPoLxb6lGDrvEP-4pEkIR-cdwCJVGhlGHjMioTCq_AKF9ViEL4ofCfYz0y7eTRAHEeifRKalerWdKWBWE9ie_EAJbqmLQ9wR0Yu5Pc9kpX2CDkOsrakejBjdyTGrBH-g87YWtqaHGfAEyvphlOcGcaV93R-Y3KUAecl-6MChUEcjJf65FabAO71AAa5HR2wX1YJ350hHS0Jten2NVodMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام خدمت همراهان عزیز،
تمرکز در این نسخه روی زبان فارسی، دسترسی پذیری برای افراد با مشکلات بینایی، تست گروهی سرور ها و خروجی از ریزالور ها بوده.
✅
نسخه اپلیکیشن به 1.5.0 ارتقا پیدا کرده
✅
تست سرورها اضافه شده و می‌توانید سرعت، Ping و وضعیت سلامت همه سرورها یا هر سرور جداگانه را بررسی کنید
✅
نتیجه تست کنار هر پروفایل سرور نمایش داده می‌شود تا تشخیص سرورهای بهتر یا مشکل‌دار راحت‌تر باشد
✅
زبان فارسی به اپ اضافه شده و می‌توانید از داخل تنظیمات بین فارسی و انگلیسی جابه‌جا شوید
✅
چیدمان فارسی راست‌به‌چپ شده و فونت Vazirmatn برای خوانایی بهتر اضافه شده
✅
بخش‌های اصلی اپ مثل اتصال، پروفایل‌ها، اسکن، لاگ‌ها و تنظیمات فارسی‌سازی شده‌اند
✅
دسترس‌پذیری اپ برای TalkBack و صفحه‌خوان‌ها بهتر شده و دکمه‌ها، تب‌ها، اسلایدرها و کارت‌ها توضیح واضح‌تری دارند
✅
وارد کردن پروفایل با QR راحت‌تر شده
✅
خروجی گرفتن همه Resolverهای ذخیره‌شده در یک فایل اضافه شده و Resolverهای تکراری حذف می‌شوند
✅
تنظیمات Parallel Test مرتب‌تر شده و تنظیمات پایدار به‌صورت پیش‌فرض استفاده می‌شوند
✅
تنظیمات تهاجمی‌تر Parallel Test جدا شده‌اند و فقط در صورت فعال کردن استفاده می‌شوند
✅
نتیجه اسکن Resolver پایدارتر بروزرسانی می‌شود و پروفایل Scanner Result فقط بعد از پایان اسکن تغییر می‌کند
✅
پروفایل Default Resolver دیگر اشتباهی به‌عنوان پروفایل دستی ذخیره نمی‌شود
✅
وضعیت تست سرورها هنگام قطع اتصال یا خطا بهتر پاک می‌شود
ممنون از دانی عزیز برای تغییرات مربوط به زبان و دسترسی پذیری
❤️
در این ورژن تنظیمات جدیدی برای تست موازی MTU اضافه شده. دوستان عزیز که ابتدا مشکل داغ شدن گوشی موبایل داشتن، این گزینه رو بیارن پایینتر. مقدار حدود ۳۰ میتونه خوب باشه. اگر همچنان این مشکل رو داشتید مقدار های کمتر رو امتحان کنید.
همنین دوستانی که گوشی های مدل بالاتر دارند، میتونند مقدار های بالاتر رو تست کنند.
@WhiteDNS</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/whitedns/683" target="_blank">📅 13:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-682">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mNQPlJmfurOEJimdGBMXlohS7xePFtu_a8tmQDGHTQebiZChspBrjgv7esLJ1SFx99JH4fbZrmMKAmc0l_DqfYUoppD89MOETD9c8gLeDgTouT4xEORwVFuKis5WjlbRbPuWbdAK0WVJhnkvjsZNPj8X1bVaPE_Y5oUGXtkSVuYhSvJZCzMBo5mJX90rvFXKglglEaGuXgEed6oHSiu4nmU6a7jNn1LnsXB9i6KFnx2kOS9YygI9Ci4jFDZdwyRhfAawP5u9RfCIKpjF9J8Xu0Yhdms6DhaDm8xVyfWks770ZysLB8wu4fpU-nYzZeZ-V-fILp_mHdYdOJG9tdzqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ اندروید
#چشم_عقاب
نه فقط یه خبرخوان، بلکه یه راه آفلاین برای دسترسی آزاد به اطلاعاته، که بدون اینترنت، بدون VPN و حتی بدون داشتن مجوز اینترنت روی گوشی، خبرها و اطلاعات رو مستقیما از ماهواره روی دستگاه شما میاره.
کافیه کانالش رو روی فرکانس 10762/27500V ماهواره ترکمن‌عالم باز کنین و دوربین گوشی رو سمت کدهای QR که روی صفحه نمایش داده میشن بگیرید، تا اپ در چند ثانیه اطلاعات رو بخونه و روی گوشی ذخیره کنه.
اپ فقط به دوربین دسترسی داره تا QR Codeها رو اسکن کنه و هیچ عکس یا ویدئویی ذخیره یا ارسال نمی‌کنه. تمام محتواهایی که دریافت می‌کنین، قبل از پخش با امضای رمزنگاری‌شده Ed25519 تأیید میشن تا اپ فقط اطلاعات واقعی و معتبر رو قبول کنه.
👉
play.google.com/store/apps/details?id=com.filtershekanha.cheshmoghab
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/whitedns/682" target="_blank">📅 12:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-681">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from3rf4n vpn(3rf4n)</strong></div>
<div class="tg-text">سرور white dns متصل چنل
✅
Domain :
v.phtv1.lol
Key :
2ff051858125055a6999b91c515d19ef
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQHp5cGhlcnZwbnNhbGxlIiwic2VydmVyIjp7ImRvbWFpbiI6InYucGh0djEubG9sIiwiZW5jcnlwdGlvbl9rZXkiOiIyZmYwNTE4NTgxMjUwNTVhNjk5OWI5MWM1MTVkMTllZiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/whitedns/681" target="_blank">📅 10:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-680">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
سرور وایت دی ان اس (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲۸ اردیبهشت
Domin Vip :
vip.masir-sefid.my
Domin 1:
v1.masir-sefid.my
Domin 2:
v2.masir-sefid.my
Domin 3:
v3.masir-sefid.my
Domin 4:
v4.masir-sefid.my
Domin 5:
v5.masir-sefid.my
Key :
Telegram-Channel--->@Masir_Sefid
👾
لینک دانلود
کلاینت :
1️⃣
WhiteDNS
1.4.0
1️⃣
WhiteDNS
(Windows)
1.0.5
⚡️
پک ریزالور
⬅️
فیلم اموزش وایت دی ان اس
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
(پیشنهادی)
اگه وصل شدین ری اکشن برید بدونم
❤️
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/whitedns/680" target="_blank">📅 09:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-679">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=KBjGglQUOIVx55uazTTCdyzCTTL5GyOIcdt8hS5hI8x5bHYYp4w-0Sj2M_OVnq3lET883j15qGhwSaaj_xVYGU_rcznmHyaVmoKf8AoyMlfvmjxi68gxCbA-7Kmn2KovgjbexW4Q0i3QeATwud7SKPec1ko6wyI1-GaMAou6RusJr8tWU8cg6ev8FuIw66gOuNj4CBBcltrwSKF6osEQsjfBPT5MEaMpJuCJT8piBhhi1SyOUHs9kwntPz3qToyzMhT9m9cCy1Bk1lcWrNjh7gwt578BVRQepM6iU5DM_iVpldSuCr2ym3xtk353cCgfyI6EDt7T7E1d6xeawBYGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=KBjGglQUOIVx55uazTTCdyzCTTL5GyOIcdt8hS5hI8x5bHYYp4w-0Sj2M_OVnq3lET883j15qGhwSaaj_xVYGU_rcznmHyaVmoKf8AoyMlfvmjxi68gxCbA-7Kmn2KovgjbexW4Q0i3QeATwud7SKPec1ko6wyI1-GaMAou6RusJr8tWU8cg6ev8FuIw66gOuNj4CBBcltrwSKF6osEQsjfBPT5MEaMpJuCJT8piBhhi1SyOUHs9kwntPz3qToyzMhT9m9cCy1Bk1lcWrNjh7gwt578BVRQepM6iU5DM_iVpldSuCr2ym3xtk353cCgfyI6EDt7T7E1d6xeawBYGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.wdn.best
Encryption Key:
bad99364093861634030e96f11fe3132
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/whitedns/679" target="_blank">📅 07:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-678">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7K57fxlPEnRVdIaUrBaQ39FIiNOdlrSCOxFJtFzccB9A7rCuLgQRRt_apfIW60rPlf3RfMxBGIiWBXplm8XyOUYYu-KdmSrwYmUlf1K3XImo-GBUh431iVa8MeJ3VUCRUzBBp7Wej76nDKVi2Z7z1k4h3Q37JJc31_YRjjvEtxXQn4X7eDrMur2_6RIUtf-Qno82SZv6UQRctfBL_Xsv8wVlx7NxbBHSFsQuLETJry0Bln2ulqmWLFfNn-zfVPqFrd9n3PjrEDHMhusZnbijHt24GCGBEzwfBC1VUkLncbmXaKZchZSnnW7kwpJ-q-MoJMQt6DctfUM1T3mGOacBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه بعدی WhiteDNS با ترجمه کامل تمام متن‌ها به زبان فارسی منتشر خواهد شد.
همچنین در این نسخه، دسترسی‌پذیری اپلیکیشن برای افرادی که از اسکرین‌ریدر استفاده می‌کنند و کاربران دارای معلولیت‌های جسمی به شکل کامل‌تر و بهتر بهبود داده شده است.
ممنون از دنی عزیز برای PR</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/whitedns/678" target="_blank">📅 07:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-677">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/677" target="_blank">📅 06:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-676">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-3PUgIC53bIi_LKF4RbEw5yluwvNEc4cPyRHIGhS2PUxOZ3fThKSuF8xea8sghxWXmzEuNv7ED9XRdzVENQ2mXA4vR57WK6vXJo-ENaycnWzYINZSQnBLNT7yVjDj6HNTRH8bkxXJ4L_o4vdMtX1t38ld3D1IFWQuBkcMG-Iy2MNR6feIuMCAGnAfxDolAMFbxWos9qu2BEJbPjHKY_IX2GLC1y8UFL-NudOSBZ5bagJOAG1t2gwf01mdbQLsu8w7AajyWKtj3XUEd-xmsfSUznVY3vwP-LsD7BAPvTBGajfCP8Yzd0WwasnsTGmkxlaXzz7ZsEd4nVudY8P4zR9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/whitedns/676" target="_blank">📅 06:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-675">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">WhiteDNS
❌
WaitDNS
✅</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/whitedns/675" target="_blank">📅 04:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
سرور وایت دی ان اس (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲۷ اردیبهشت
Domin Vip :
vip.masir-sefid-3.shop
Domin 1:
v1.masir-sefid-3.shop
Domin 2:
v2.masir-sefid-3.shop
Domin 3:
v3.masir-sefid-3.shop
Domin 4:
v4.masir-sefid-3.shop
Domin 5:
v5.masir-sefid-3.shop
Key :
Telegram-Channel--->@Masir_Sefid
👾
لینک دانلود
کلاینت :
1️⃣
WhiteDNS
1.4.0
1️⃣
WhiteDNS
(Windows)
1.0.5
⚡️
پک ریزالور
⬅️
فیلم اموزش وایت دی ان اس
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
(پیشنهادی)
اگه وصل شدین ری اکشن برید بدونم
❤️
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/whitedns/673" target="_blank">📅 17:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-672">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">☄️
WhiteDNS Premium Configs For StormDNS
☄️
😀
کانفیگ‌های اختصاصی، پایدار و قدرتمند
🚀
مناسب برای اتصال سریع، امن و بدون اختلال
📡
Optimized For Better Stability & Performance
🎁
کانفیگ اهدایی از طرف چنل:
@PersiaTMChannel
01.
🌐
Domain:
b1.persiatmx.us
🔑
Encryption Key:
843996e318d85f34a012240b24714d2f
━━━━━━━━━━━━━━━━━━
02.
🌐
Domain:
b2.persiatmx.us
🔑
Encryption Key:
6b51dfc5f065436a03f76f76af4c7416
━━━━━━━━━━━━━━━━━━
03.
🌐
Domain:
b3.persiatmx.us
🔑
Encryption Key:
2bee92b7342be563851a6f8da0090de4
━━━━━━━━━━━━━━━━━━
04.
🌐
Domain:
b4.persiatmx.us
🔑
Encryption Key:
9f9709ec0bb9c380227237e9ef7c9f3c
━━━━━━━━━━━━━━━━━━
05.
🌐
Domain:
b5.persiatmx.us
🔑
Encryption Key:
962f409687cf0069080d5aef96cccbdc
━━━━━━━━━━━━━━━━━━
06.
🌐
Domain:
b6.persiatmx.us
🔑
Encryption Key:
428c0d303605cefb06f7c33123484ac5
━━━━━━━━━━━━━━━━━━
07.
🌐
Domain:
b7.persiatmx.us
🔑
Encryption Key:
3ac7935006ba328616a5df2aef1ed8fd
━━━━━━━━━━━━━━━━━━
08.
🌐
Domain:
b8.persiatmx.us
🔑
Encryption Key:
6aecaa4877f463a773ab364560815f27
━━━━━━━━━━━━━━━━━━
09.
🌐
Domain:
b9.persiatmx.us
🔑
Encryption Key:
7f3aad92ab16b630fc2d0c7e8469c278
━━━━━━━━━━━━━━━━━━
10.
🌐
Domain:
b10.persiatmx.us
🔑
Encryption Key:
7fb2856813f16fe683a4483bb6ae0f71
Special Thanks To
🤝
@WhiteDNS
Channel
⭐️
StormDNS Project
For Their Support & Contribution.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/whitedns/672" target="_blank">📅 15:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-671">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/whitedns/671" target="_blank">📅 14:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-670">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=KN60loKNC1B2e6mbruZXQFeT_X3wFPjJ4nM7fKg1pxgyzckvZSYfsDyOZbNHlfw_F7NihUlFgwD2_VmCSQZk_MK6LCKSx9JXosn_8YxBXi-BaE8taDHxuWOHjytIFGBZlnOz5VYaELbYeGrggPgLW9ipna2UXChXlMI_WzWgPpqcx-EhGJtFkejLT5T6Ajj27Y9SeqDwuXCR53O7ehfTYPjdT4qdjKbFql0s7jAQpYYdy1myAs8lVUotWfIu38Q0VzZiwK4MdTuichomMp0UP1whL3NZlTGZYxa_dj1KMBPQ-3QarnFUbT8VtmPUks-7emqqBh56OuYzI6Y18aBFMw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=KN60loKNC1B2e6mbruZXQFeT_X3wFPjJ4nM7fKg1pxgyzckvZSYfsDyOZbNHlfw_F7NihUlFgwD2_VmCSQZk_MK6LCKSx9JXosn_8YxBXi-BaE8taDHxuWOHjytIFGBZlnOz5VYaELbYeGrggPgLW9ipna2UXChXlMI_WzWgPpqcx-EhGJtFkejLT5T6Ajj27Y9SeqDwuXCR53O7ehfTYPjdT4qdjKbFql0s7jAQpYYdy1myAs8lVUotWfIu38Q0VzZiwK4MdTuichomMp0UP1whL3NZlTGZYxa_dj1KMBPQ-3QarnFUbT8VtmPUks-7emqqBh56OuYzI6Y18aBFMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.store
Encryption Key:
bad99364093861634030e96f11fe3132
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
⚠️
⚠️
⚠️
⚠️
⚠️
حجم کپی از کانال ما واقعاً باورنکردنیه؛ در حدی که آدم شک می‌کنه شاید ما ناخواسته برای بعضی دوستان واحد تولید محتوا راه انداختیم.
کمترین کاری که می‌تونید انجام بدید، انتشار همین پست یا حداقل ذکر منبع کانال ماست. باور کنید نوشتن منبع، اینترنت رو خراب نمی‌کنه و از اعتبار شما هم کم نمی‌کنه.
همراهان عزیز WhiteDNS،
اگر دیدید کانالی بدون ذکر منبع مطالب ما رو کپی کرده، لطفاً با احترام منبع اصلی رو بهشون یادآوری کنید. شاید فقط فراموش کردن؛ کپی‌کردن زیاد آدم رو خسته می‌کنه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/whitedns/670" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-669">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سلام خدمت همه دوستان عزیز
🙌
WhiteDNS یک پروژه غیرانتفاعی و رایگان است که برای کمک به دسترسی آزادتر کاربران ایرانی به اینترنت فعالیت می‌کند.
حمایت مالی شما کمک می‌کند این پروژه زنده بماند، سرورهای بیشتری راه‌اندازی شود و افراد بیشتری در ایران بتوانند به اینترنت آزاد متصل شوند.
هیچ اجباری برای کمک مالی وجود ندارد.
تمام حمایت‌ها فقط صرف هزینه‌های سرور، زیرساخت، توسعه و نگهداری پروژه WhiteDNS خواهد شد.
ممنون از اعتماد و همراهی شما
🙏
🤍
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/whitedns/669" target="_blank">📅 10:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-668">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">لیست ۱۰۰ ریزالوری که در ۲۴ ساعت گذشته به سرورهای WhiteDNS متصل شده‌اند:
185.142.158.162
185.255.91.60
94.232.173.28
217.219.162.200
185.53.142.174
134.255.206.206
185.51.201.58
134.255.206.205
5.202.252.30
109.230.89.90
31.214.169.244
93.115.127.9
185.88.178.196
185.208.174.167
185.37.55.30
80.75.7.2
164.138.17.122
5.160.128.142
158.58.184.147
2.189.44.68
2.188.21.58
185.109.61.27
185.50.37.52
5.236.93.157
185.137.25.146
109.230.206.175
178.252.128.66
185.208.175.228
2.186.121.65
2.188.21.70
78.157.41.60
2.188.21.46
108.162.192.0
173.245.58.0
172.64.32.0
46.209.209.209
207.211.215.145
185.141.105.139
78.39.234.140
37.191.95.70
2.189.44.98
2.188.21.138
185.208.183.29
80.191.163.249
5.160.140.16
46.32.31.30
2.189.44.94
2.189.44.91
5.160.227.78
2.189.44.90
2.189.44.92
2.189.44.93
74.80.77.246
66.185.123.244
109.72.197.1
89.32.197.226
85.185.157.181
185.141.106.238
2.188.21.62
74.80.77.247
78.38.174.2
74.63.24.205
74.63.24.206
172.253.12.221
172.253.13.149
172.253.228.150
77.104.104.104
172.253.228.147
172.253.13.147
172.253.13.146
172.253.228.145
172.253.12.210
172.253.13.156
172.253.13.154
172.253.12.216
172.253.12.154
172.253.12.151
172.253.228.152
172.253.13.157
172.253.13.148
172.253.13.152
172.253.13.144
172.253.13.153
85.133.167.108
172.253.228.156
172.253.228.149
74.63.24.210
172.253.13.151
172.253.228.154
172.253.228.151
172.232.181.197
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/whitedns/668" target="_blank">📅 09:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/whitedns/667" target="_blank">📅 09:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-666">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">full user-facing guide .txt</div>
  <div class="tg-doc-extra">18.6 KB</div>
</div>
<a href="https://t.me/whitedns/666" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
Quick Guide to WhiteDns for Windows!
🚀
Struggling to connect? Here is the absolute easiest way to set up WhiteDns for maximum speed and stability:
🛠
🔹
1. Basic Setup:
Create a profile and enter your Tunnel Domain and Encryption Key.
📝
🔹
2. Find the Best Connection:
Go to the "Resolvers" tab, run a quick scan, and apply the top-ranked resolver to your tunnel.
📡
🔹
3. Ultimate Stability:
Use the
MasterDNS
engine and select the
Stable Iran
preset for the most reliable experience on restricted networks.
🛡
🔹
4. Choose Proxy Mode:
Use
System proxy
to automatically route traffic for browsers like Chrome and Edge, or choose
SOCKS5 only
(
127.0.0.1:18000
) for manual configuration in apps like Telegram or Firefox.
⚙️
💡
The Golden Formula:
Enter details
➡️
Scan Resolvers
➡️
Apply Best Resolver
➡️
Choose 'Stable Iran'
➡️
Connect!
🏆
Check out the full attached guide below for step-by-step instructions and troubleshooting!
📚
@whitedns</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/whitedns/666" target="_blank">📅 09:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-665">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚀
The Comprehensive WhiteDns Guide for Windows is Out!
🚀
Dear users,
if you are facing any challenges connecting and configuring the WhiteDns app on Windows, this complete guide is made exactly for you. WhiteDns is a powerful desktop tool for tunneling and creating local proxies, and with this guide, you can experience the highest speed and stability.
📌
A quick summary of what you'll learn in this guide:
🔹
Quick & Easy Start:
Step-by-step tutorial on creating a profile, entering your domain, encryption key, and making the initial connection.
🔹
Choosing the Proxy Mode:
Understanding the difference between manual mode (SOCKS5 only) and applying the proxy to the entire system (System proxy) for browsers.
🔹
Powerful Scanner Tool (Resolvers):
How to find the fastest and most stable DNS resolvers using the app's built-in scanner across Quick, Deep, Advanced, and High Accuracy modes.
🔹
Advanced Settings & Engines:
Explaining the differences between the MasterDNS and StormDNS engines, and how to use Presets like
Stable Iran
(for maximum stability on restricted networks) up to Aggressive modes.
🔹
App-Specific Configurations:
Detailed instructions on setting up the local proxy (
127.0.0.1:18000
) on Telegram Desktop, Firefox, Chrome, and Edge.
🔹
Troubleshooting:
Practical solutions for common issues like browsers not connecting despite an active app connection, frequent disconnections, or slow tunnel startup.
💡
The Golden Formula for Connection:
The best and safest route for most users is: Set tunnel details
⬅️
Scan resolvers
⬅️
Apply the best resolver
⬅️
Use Stable Iran preset
⬅️
Connect!
@whitedns</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/whitedns/665" target="_blank">📅 08:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-664">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">راهنمای_جامع_استفاده_از_وایت_دی_ان_اس_ویندوز_.docx</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/whitedns/664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
راهنمای جامع وایت دی‌ان‌اس (WhiteDns) برای ویندوز منتشر شد!
🚀
کاربران عزیز، اگر برای اتصال و تنظیم برنامه WhiteDns در ویندوز با چالشی مواجه هستید، این راهنمای کامل دقیقا برای شما آماده شده است. برنامه WhiteDns یک ابزار قدرتمند دسکتاپ برای تونلینگ و ساخت پروکسی محلی است و با استفاده از این راهنما می‌توانید بالاترین سرعت و پایداری را تجربه کنید.
📌
خلاصه‌ای از آنچه در این راهنما یاد می‌گیرید:
🔹
شروع سریع و آسان:
آموزش قدم‌به‌قدم ایجاد پروفایل، وارد کردن دامنه، کلید رمزنگاری (Encryption Key) و اتصال اولیه.
🔹
انتخاب حالت پروکسی:
تفاوت بین حالت دستی (SOCKS5 only) و اعمال پروکسی روی کل سیستم (System proxy) برای مرورگرها.
🔹
ابزار قدرتمند اسکنر (Resolvers):
آموزش پیدا کردن سریع‌ترین و پایدارترین تحلیلگرهای DNS با استفاده از اسکنر داخلی برنامه (در حالت‌های سریع، عمیق و با دقت بالا).
🔹
تنظیمات پیشرفته و موتورها:
معرفی تفاوت‌های موتور MasterDNS و StormDNS و نحوه استفاده از پروفایل‌های آماده (Presets) مانند
Stable Iran
(برای بالاترین پایداری در شبکه‌های محدود) تا حالت‌های تهاجمی‌تر (Aggressive).
🔹
تنظیمات مخصوص برنامه‌ها:
راهنمای دقیق ست کردن پروکسی محلی (
127.0.0.1:18000
) روی تلگرام دسکتاپ، فایرفاکس، کروم و مرورگر اج.
🔹
رفع مشکلات (Troubleshooting):
راهکارهای عملی برای حل مشکلاتی مثل وصل نشدن مرورگر با وجود اتصال برنامه، قطع شدن مداوم، و یا رفع گیر کردن روی راه‌اندازی کند تونل.
💡
فرمول طلایی اتصال:
بهترین و امن‌ترین مسیر برای اکثر کاربران این است: وارد کردن اطلاعات تونل
⬅️
اسکن تحلیلگرها
⬅️
اعمال بهترین تحلیلگر
⬅️
انتخاب حالت Stable Iran
⬅️
اتصال!
برای استفاده حرفه‌ای از این نرم‌افزار و دور زدن قطعی‌ها، حتماً فایل راهنمای کامل را مطالعه کنید.
#اموزش_ویندوز_whitedns
@whitedns</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/whitedns/664" target="_blank">📅 08:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-663">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/whitedns/663" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای صوتی برای whitedns windows v1.0.5
🚀
راهنمای سریع وایت دی‌ان‌اس (WhiteDns) برای ویندوز!
🚀
برای اتصال سریع و پایدار، این ساده‌ترین روش تنظیم برنامه است:
🔹
۱. تنظیمات اولیه:
یک پروفایل در تب Tunnel بسازید و آدرس دامنه (Domain) و کلید رمزنگاری (Encryption Key) خود را وارد کنید.
🔹
۲. یافتن بهترین اتصال:
به تب Resolvers بروید، یک اسکن سریع (Quick) انجام دهید و با انتخاب گزینه "Apply top to tunnel"، بهترین تحلیلگر را روی تونل اعمال کنید.
🔹
۳. بالاترین پایداری:
در تب Advanced، موتور
MasterDNS
را انتخاب کرده و برای داشتن اتصالی بدون قطعی در شبکه‌های محدود، حالت
Stable Iran
را فعال کنید.
🔹
۴. انتخاب پروکسی:
برای استفاده خودکار در مرورگرهایی مثل کروم و اج از حالت
System proxy
استفاده کنید. برای تنظیم دستی در تلگرام یا فایرفاکس، حالت
SOCKS5 only
(آدرس
127.0.0.1:18000
) را انتخاب کنید.
💡
فرمول طلایی:
وارد کردن اطلاعات
⬅️
اسکن تحلیلگرها
⬅️
اعمال بهترین تحلیلگر
⬅️
انتخاب حالت Stable Iran
⬅️
اتصال!
برای آموزش قدم‌به‌قدم و رفع هرگونه مشکل، فایل راهنمای کامل را در زیر مطالعه کنید.
👇
@whitedns</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/whitedns/663" target="_blank">📅 08:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-662">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/urnCwcn54HmBtixtTMJ_pOkMQhVAZtZwBos-PFxmehDyuyD5cgXU4QbBBzUGNjhGPFtzSJwlkSDBY20aRoK-hrqNo-5npt5xi1uSeloWa_7LSHp0_Qtp7iPSqHxpFwFxrIwUJT9yRBWvMbzwvc5qb0HVq8xaItyKquxE_vhm2SJCwQfrRz_CXacdiNW6Y4pqFiEGgtpPKNPwbl9Dw4Rn-ir4Pg2J7LKxMsqSdv18ZzIqKjqPMxaWVIJ4uN7vLYH9YDgoebAedRJCzZvZ3q8FVrxEUYxKvimmJy8I_VQqH0H2PhaYxyqg8ms8hWZrOOGn-Z_JYli4IhlCPPWXtP3XEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش جامع WhiteDns Windows</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/whitedns/662" target="_blank">📅 08:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-661">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستان گرامی :
🤝
حتما در گروه اصلی whitedns عضو شوید تا راحت‌تر به آخرین مطالب دسترسی داشته باشید
🚀
سپاس
🙏
آدرس گروه اصلی :
@whitedns_group
📲</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/whitedns/661" target="_blank">📅 06:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-660">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/660" target="_blank">📅 06:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-659">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">11 MB</div>
</div>
<a href="https://t.me/whitedns/659" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تغییرات WhiteDns ویندوز نسخه 1.0.5
بازسازی رابط مدرن
بهبود جزئیات کوچک رابط کاربری و تراز کارت‌ها برای ظاهری تمیزتر و یکدست‌تر در دسکتاپ.
🖥
✨
اسکنر با دقت بالا :
یک اسکنر با دقت بالا برای شرایط سخت اضافه شد
طراحی شمارنده رزولور بهبود یافته
به‌روزرسانی استایل شمارنده رزولور تا با چیدمان کارت‌های اطراف هماهنگ‌تر شده و ظاهری مدرن‌تر داشته باشد.
🎨
پشتیبانی از سینی ویندوز بهبود یافته
رفتار سینی برنامه به‌روزرسانی شد تا در ویندوز طبیعی‌تر احساس شود و در پس‌زمینه در دسترس بماند.
🪟
🔌
فعالیت شبکه برای حالت SOCKS5 اصلاح شد
فعالیت شبکه اکنون ترافیک را زمانی که برنامه‌ها از پروکسی محلی SOCKS5 استفاده می‌کنند، ردیابی می‌کند، به جای نمایش فعالیت فقط از طریق مسیر HTTP/System Proxy.
🌐
🔍
سازگاری پورت SOCKS سفارشی
فعالیت شبکه اکنون هنگام تغییر پورت SOCKS در تب پیشرفته نیز به کار خود ادامه می‌دهد.
⚙️
حافظه اسکن رزولور اضافه شد
برنامه اکنون بهترین نتیجه اسکن رزولور را به خاطر می‌سپارد و اسکن‌های کامل تکراری را هنگام اتصال مجدد با مجموعه رزولور یکسان کاهش می‌دهد.
💾
🚀
تجربه اتصال مجدد سریع‌تر
اتصالات مجدد باید روان‌تر احساس شوند زیرا برنامه از اسکن مجدد غیرضروری رزولورها هنگام در دسترس بودن نتیجه معتبر قبلی خودداری می‌کند.
⚡️
وارد کردن دستی رزولور اضافه شد
گزینه وارد کردن .txt در کارت «وارد کردن / رزولورهای دستی» برای بارگذاری آسان‌تر لیست رزولورها اضافه شد.
📥
📝
نکات اتصال
از لیست رزولور باکیفیت و کوچک‌تر برای راه‌اندازی سریع‌تر استفاده کنید.
🚀
رزولورهای پایدارتر را در بالای لیست نگه دارید.
📌
هنگام آزمایش اتصال، ابتدا از حالت SOCKS5 استفاده کنید.
🧪
اگر حالت System Proxy با یک برنامه ناسازگار است، آن برنامه را به‌صورت دستی برای استفاده از
127.0.0.1
و پورت SOCKS نمایش داده شده در WhiteDns پیکربندی کنید.
⚙️
مگر در صورت نیاز، از تغییر مقادیر تونل پیشرفته خودداری کنید؛ مقادیر پیش‌فرض معمولاً پایدارترین هستند.
🛡
@whitedns</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/whitedns/659" target="_blank">📅 06:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-658">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/MVTM7OPO8aYrMIiOAQNE5fdHA-ukTyUM9Sd3oO6u_zAaPXvH5I6GFpA2nuQbdqBNYJmKDBFgXKnvV6IQE-W1zG-gENXlRJULvHwm1KmcKTEnT7jrdeVe42FKQc1nJP4wYA_rYnntvwJq7ZsDOioz_2NK_iJ-kKda6RQrZrPtbRvVZBvTyP2Ub260hFkoEyJ_Dbk9p3tJE9falX-w776cht0Kkgo0Zy9e4HLM_AxjetFZYxBpY7i34_3iCLcD8_r4hVF_zVTi_9_QEo70VbV0r3Tq2qptbyWKT6NiGKhL3-PyEcUA4MHHeQBfllf_3nJaItrFvwH8-kusCSfJW-chSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/whitedns/658" target="_blank">📅 06:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-657">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">DNSForge-Guide-Persian.pdf</div>
  <div class="tg-doc-extra">79.4 KB</div>
</div>
<a href="https://t.me/whitedns/657" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آموزش گام به گام و متنی برای اتصال به نسخه‌ی ios برنامه‌ی WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/whitedns/657" target="_blank">📅 22:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-656">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🙂
نسخه آزمایشی اپلیکیشن iOS تیم WhiteDNS برای تست اتصال‌های MasterDNS و فورک StormDNS آماده شده است.
برای استفاده، ابتدا باید اپلیکیشن TestFlight را روی دستگاه خود نصب کنید، بعد از طریق لینک زیر وارد نسخه آزمایشی شوید:
https://testflight.apple.com/join/GfUqXrFz
⚠️
لطفاً توجه داشته باشید که این نسخه آزمایشی است و ممکن است هنوز باگ یا ناپایداری داشته باشد.
@WhiteDNS</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/whitedns/656" target="_blank">📅 22:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-655">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-text">📱
آموزش کار با برنامه دفید (Thefeed):
برای دریافت آخرین نسخه و کانفیگ‌ها، به کانال زیر بروید و برنامه را نصب‌ کنید و لینک کانفیگ را کپی کنید:
@thefeedconfig
ورود به برنامه:
۱. برنامه را باز کنید و زبان را انتخاب نمایید.
۲. در قسمت مشخص شده (thefeed://...)، کانفیگ کپی شده را وارد کرده و دکمه «وارد کردن» را بزنید تا ثبت شود.
عملکرد برنامه:
پس از وارد کردن اولین کانفیگ، برنامه ریزالورهای موجود در کانفیگ را بررسی کرده (چند دقیقه طول میکشد) و سپس لیست کانال‌ها را دریافت می‌کند. شما می‌توانید کانال‌ها را باز کرده، پست‌ها را مشاهده و عکس، ویدیو، ویس و فایل‌ها را دانلود کنید.
نکته:
لیست کانال‌ها فقط توسط سازنده کانفیگ قابل تغییر است. (جلو تر یک‌روش دیگر برای کانال های دلخواه شما نیز نوشته ام)
افزودن کانفیگ جدید:
در صفحه اصلی با زدن دکمه + می‌توانید کانفیگ جدید وارد کنید یا کانفیگ‌های موجود دیگر را فعال نمایید.
🛠️
بخش ریزالور ها:
در این بخش می‌توانید ریزالورها را مدیریت کنید. دکمه‌ای به نام «بانک ریزالور» وجود دارد که لیست کامل را نمایش می‌دهد. همچنین یک لیست فعال به نام Default وجود دارد که پس از بررسی اولیه، ریزالورهای فعال را در خود نگه می‌دارد. شما می‌توانید برای اینترنت‌های مختلف، لیست‌های فعال متفاوتی داشته باشید. و با زدن دکمه «بررسی مجدد»، می‌توانید از بانک ریزالور فعال برای اینترنت خود را پیدا کرده و به لیست جدید اضافه کنید.
🔍
بخش پیدا کردن ریزالور:
این بخش بسیار مهم است. با استفاده از یک لیست پیش‌فرض ۵۰ هزارتایی، می‌توانید ریزالورهایی که برای اینترنت شما کار می‌کنند را پیدا کنید (زمانی که سرعت برنامه کم شده بود و یا کار‌ نمی‌کرد).
روش کار:
۱. وارد بخش شوید.
۲. دکمه بارگذاری لیست پیش‌فرض را بزنید.
۳. دکمه شروع اسکن را بزنید.
۴. برنامه شروع به پیدا کردن می‌کند. وقتی حدود ۱۰ تا ریزالور پیدا شد، توقف را بزنید و سپس دکمه «افزودن به لیست فعال» را بزنید.
*توجه:* حتماً باید VPN خاموش باشد.
📺
بخش کانال‌های دلخواه (teleMirror):
این بخش کاملاً از قسمت‌های قبلی جداست و مکانیزم متفاوتی دارد. این بخش از طریق سرویس‌های گوگل، پیام و عکس کانال‌های عمومی تلگرام را می‌آورد و نمایش می‌دهد.
*محدودیت‌ها:* این بخش نمی‌تواند ویدیو پخش کند یا فایل دانلود کند (به خاطر محدودیت‌های گوگل). همچنین برخی کانال‌های عمومی اجازه اشتراک‌گذاری در سایت را نمی‌دهند، و پست هایشان در این قسمت نمایش داده نمی‌شود.
نکته مهم:
این بخش فقط زمانی کار می‌کند که گوگل در دسترس باشد. اگر گوگل مسدود شود، فقط قسمت اصلی برنامه (معرفی شده در اول پست) کار خواهد کرد. همچنین سرویس‌های گوگل محدودیت تعداد درخواست دارند که ممکن است شما را محدود کنند.
🔔
برای اخبار پروژه حتما کانال اصلی را دنبال کنید:
@networkti</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/whitedns/655" target="_blank">📅 22:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-654">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.18.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.9 MB</div>
</div>
<a href="https://t.me/whitedns/654" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید TheFeed (v0.18.10)
🚀
🔸
توی این نسخه چیز مهمی تغییر نکرده! فقط از اونجایی که گیتهاب اکانتم رو ساسپند کرد و هنوز اکانت باز نشده، پروژه TheFeed رو به گیتلب منتقل کردم و برنامه رو هم تغییر دادم که لینک ها و این چیزهای که توی برنامه بود به گیتلب هم اشاره کنه. البته قابلیت دانلود آخرین نسخه و نوتیف نسخه جدید هنوز به گیتلب وصل نشده و کار‌نمیکنن (گیتلب فیلتره و کمکی نمیکنه اضافه کردنش
🫠
).
البته توی تنظیمات یک دکمه هست به اسم "بررسی" که وقتی بزنیدش اخرین شماره نسخه رو از سرور میپرسه و نشون میده، این رو سمت سرور تغییر دادم که اگر‌ گیتهاب کار نکرد اخرین شماره نسخه رو از گیتلب بگیره و سمت کلاینت هم یک باگ داشت که رفع شد.
⚠️
این نسخه خیلی مهم نیست و میتونید آپدیت نکنید
آدرس سورس کد پروژه روی گیتلب:
https://gitlab.com/sartoopjj/thefeed
یک نفر لطف کرده بود و فیچر های دسترسی پذیری اضافه کرده بود و پول ریکوئست فرستاده بود، لطفا اگر این پیام رو میبینی مرج ریکویست بفرست روی گیتلب
🥲
❤️
کانال اصلیم:
@networkti
کانال کانفیگ برای برنامه:
@thefeedconfig</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/whitedns/654" target="_blank">📅 22:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/whitedns/653" target="_blank">📅 21:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">WhiteDns-Windows-Setup.exe</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/whitedns/652" target="_blank">📅 09:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">White DNS
pinned «
⚠️
اعلان مهم
📢
تمام تبلیغاتی
📰
که در این کانال قرار می‌گیرند، هیچ ارتباطی با ما ندارند
🚫
و ما هیچ‌گونه مسئولیتی در قبال محتوای آگهی‌ها، معاملات، خرید و فروش، یا هر نوع کلاهبرداری احتمالی
🎭
قبول نمی‌کنیم.  دلیلش ساده است: ما هیچ کنترلی روی تبلیغات ارسال‌شده…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/651" target="_blank">📅 07:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-650">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⚠️
اعلان مهم
📢
تمام تبلیغاتی
📰
که در این کانال قرار می‌گیرند، هیچ ارتباطی با ما ندارند
🚫
و ما هیچ‌گونه مسئولیتی در قبال محتوای آگهی‌ها، معاملات، خرید و فروش، یا هر نوع کلاهبرداری احتمالی
🎭
قبول نمی‌کنیم.
دلیلش ساده است: ما هیچ کنترلی روی تبلیغات ارسال‌شده نداریم
🤷‍♂️
. این تبلیغات به صورت خودکار توسط خود تلگرام در کانال گذاشته می‌شوند
🤖
مسئولیت هرگونه تعامل، پرداخت یا ارتباط با آگهی‌دهنده، کاملاً بر عهده خود کاربران
👥
است
@whitedns</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/whitedns/650" target="_blank">📅 07:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-649">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">9.2 MB</div>
</div>
<a href="https://t.me/whitedns/649" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه 1.0.3
یک آپدیت متمرکز بر پایداری است. در این نسخه پایداری اتصال بهتر شده، مپ شدن تنظیمات Advanced اصلاح شده، تفاوت بین SOCKS5 و System Proxy شفاف‌تر شده، و احتمال حالتی که برنامه Connected باشد ولی سایت‌ها باز نشوند کمتر شده است.
WhiteDns Windows v1.0.3
- راهنمای سریع تست
لطفا برای تست اول این تنظیمات را استفاده کنید:
1. برنامه را باز کنید.
2. وارد بخش Connect شوید.
3. گزینه Proxy Mode را روی System proxy بگذارید.
4. وارد بخش Advanced شوید.
5. گزینه Transport preset را روی Balanced بگذارید.
6. این موارد را بررسی کنید:
- Compression = off
- Base64-encode data = Off
- DNS listener enabled = Off
- SOCKS5 authentication = Off
- Packet duplication = 0
7. در صورت نیاز ذخیره کنید و سپس Connect بزنید.
اگر سایت ها ناپایدار بودند یا باز نشدند:
- فقط همین یک مورد را تغییر دهید:
- Transport preset = Stable Iran
لطفا این موارد را گزارش کنید:
- آیا اتصال با موفقیت انجام شد؟
- آیا یوتیوب و سایت های عادی باز شدند؟
- از چه Proxy Mode استفاده کردید؟
- سرعت مرور مناسب بود یا نه؟
- آیا برنامه یا سایتی بود که با وجود Connected بودن کار نکند؟
@whitedns</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/whitedns/649" target="_blank">📅 07:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-648">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LoZZG_aza_xi-pAYBxbePqOB1gGYm9XvRKLI3k8j-FG1eOIdhiaOupAYD1liN13Ix63MhAJevmLKD1bzkv0zSaD6HCEK8dBu2DRkhzQ5cnaftiwUqOYqqACDFylw4_qx8G6fYFcsXPCLtXeJr9NYZAcVd4Lzu9UybIQdf_l5eCj8w5Nb6iBwN25OSN-vPjb8aTZ-HmNxP5T7sNbVcfX9wTaYSYRYzcmN3aOS93Rw68TpsEDmRjYtXCzfIpjl_NdVq7oS_2dWOzhiYiuFu6ysg6aeOBt3etMaoQA1iW9gO6SRKPEzjoAb2vsa2WRufptEVOwYO9OovHPf04ol0gDFBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/whitedns/648" target="_blank">📅 07:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-647">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/whitedns/647" target="_blank">📅 04:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-646">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSOS Iran Connect</strong></div>
<div class="tg-text">🔶
خبرهای خوب:
۱. عبدالکریم، دوست بلوچ ما، تونست اپلیکیشن WhiteDNS را با کار تیمی دوستان راه بندازه
و وصل بشه
🎉
🗣
صدای خودشون، ۱۴۰۵.۰۲.۲۶، ۰۱:۵۲ ایران
۲. من داستان عبدالکریم روشندل را به Pedi جان در
@WhiteDNS
منتقل کردم، و دو درخواست مطرح کردم:
الف. داشتن رابط کاربری (user interface) پارسی در اپلیکیشن WhiteDNS.
ب. افزودن راهنمای پارسی به گیت‌هاب پروژه برای استفاده روشندلان با کمک ScreenReader.
ایشون از ایده‌ها استقبال کرد، ولی به زمان نیاز دارند.
⚪️
هدف دلی ما اینه که کاربرها خودکفا و مستقل باشند.
🫂
#همدلی
#ایران
💛
@WhiteDNS
🆔
@SOSIranConnect</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/whitedns/646" target="_blank">📅 03:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-645">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/whitedns/645" target="_blank">📅 01:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-643">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b77e656a8.mp4?token=cNuwf2S-VC1vWkzgToDRIUa1M-IHFV7Z8zUliLZdEgiSG8RtdGp0FZLZbmMA17PpElrA2jY9Zv5dsQyOhGVZOOacvNqbqeedE-SgGoxTCzSA_NXidYj6qyYD8aaUXFy8csNj1y4ZTXQ88Gg85of1Tvixe0dHmRbGaWTRan8QyTToblJs6KHt0rukb_RhDUEpEykDjU29cOfnoYCPdCfqBJFzoxMVbcHQk41Gedmt1RBexe-55fdCHPkbkiLwl9HrIHEJ3J5I1cgdQF_K22dYm3C4Jn65hx7zCVnWciapP3lgOPsMs8xJRVedMzNfND2EDXU4jIhSfGpygdSmfF_DIiDx59hW5kvW6kG92PccR4w7u134YywaoXr2FRgK6xzc07njDLGrRUHhhqXGabX5MAz4Cp2lyBYSYfFQerpsAkycg6lJKkwH74Yo4eIuoPMdCAfwwoMP_zV0iivW7eAwJjGGA1t7iWGEsZjsC1N3M_B_KxDVkhkASzxXeqEeDFrxW61VAcR3Me3ptUxX4CpVgyUNvEy1jPNvvgELtCqJTUS-CSWh5k6BGG5giMVCFfJsVxhx8B_spNXlDkvhKr1WLpkDYVbzc399TSd2ZwlMPAoYqwMwLZfxZkmmqS6e8jjWfIpfZFmB4YKfRfqQbC0YtP-ZaXnYioUJOTUmWGDRCBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b77e656a8.mp4?token=cNuwf2S-VC1vWkzgToDRIUa1M-IHFV7Z8zUliLZdEgiSG8RtdGp0FZLZbmMA17PpElrA2jY9Zv5dsQyOhGVZOOacvNqbqeedE-SgGoxTCzSA_NXidYj6qyYD8aaUXFy8csNj1y4ZTXQ88Gg85of1Tvixe0dHmRbGaWTRan8QyTToblJs6KHt0rukb_RhDUEpEykDjU29cOfnoYCPdCfqBJFzoxMVbcHQk41Gedmt1RBexe-55fdCHPkbkiLwl9HrIHEJ3J5I1cgdQF_K22dYm3C4Jn65hx7zCVnWciapP3lgOPsMs8xJRVedMzNfND2EDXU4jIhSfGpygdSmfF_DIiDx59hW5kvW6kG92PccR4w7u134YywaoXr2FRgK6xzc07njDLGrRUHhhqXGabX5MAz4Cp2lyBYSYfFQerpsAkycg6lJKkwH74Yo4eIuoPMdCAfwwoMP_zV0iivW7eAwJjGGA1t7iWGEsZjsC1N3M_B_KxDVkhkASzxXeqEeDFrxW61VAcR3Me3ptUxX4CpVgyUNvEy1jPNvvgELtCqJTUS-CSWh5k6BGG5giMVCFfJsVxhx8B_spNXlDkvhKr1WLpkDYVbzc399TSd2ZwlMPAoYqwMwLZfxZkmmqS6e8jjWfIpfZFmB4YKfRfqQbC0YtP-ZaXnYioUJOTUmWGDRCBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
دور زدن فیلترینگ با کانفیگ سرورلس با ترکیب nekobox و v2rayng
•
✅
لینک کانفیگ nekobox
•
https://pastebin.com/raw/rWeHKSt3
•
✅
لینک داخلی کانفیگ nekobox
•
https://seup.shop/t/exks1
•
✅
لینک کانفیگ V2rayNg
•
https://pastebin.com/raw/Yfymhyy5
•
✅
لینک داخلی کانفیگ‌ V2rayNg
•
https://seup.shop/t/k9mmj
❗️
هر دو کلاینت رو، رو حالتvpnبزارید .
📥
لینک داخلی ویدیوها
•
🎥
https://seup.shop/f/uns5
•
🎥
https://seup.shop/f/v4jx
•
𝕏 Irvictorious
kian
•
@ConfigWireguard
💎
•
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/whitedns/643" target="_blank">📅 19:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-642">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">White DNS
pinned «
💥
💥
💥
💥
💥
💥
💥
برای تبادل نظر و همگرایی در گروه ما عوض شوید
🔄
👥
@whitedns_group
🌐
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/642" target="_blank">📅 19:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-641">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">💥
💥
💥
💥
💥
💥
💥
برای تبادل نظر و همگرایی در گروه ما عوض شوید
🔄
👥
@whitedns_group
🌐</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/whitedns/641" target="_blank">📅 19:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-639">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">لیست ۱۰۰ ریزالور که طول ۲۴ ساعت گذشته به سرور های WhiteDNS وصل شدند
185.94.98.34
2.189.44.68
185.44.36.216
185.137.25.146
94.232.173.28
185.142.158.162
217.219.162.200
185.88.178.196
178.252.143.130
134.255.206.206
80.75.7.2
134.255.206.205
185.53.142.174
89.32.197.226
185.37.55.30
77.238.111.234
31.214.169.244
80.71.149.62
185.109.61.27
62.60.197.83
185.88.178.177
178.252.128.66
158.58.184.147
5.202.252.30
74.63.24.205
74.63.24.211
216.147.121.134
74.63.24.210
46.209.209.209
217.66.203.211
74.80.77.246
80.191.221.26
2.189.44.98
216.147.121.98
164.138.17.122
207.211.215.145
151.232.36.4
185.208.175.228
2.188.21.58
108.162.192.0
172.64.32.0
80.191.163.249
173.245.58.0
78.39.234.140
185.208.183.29
2.188.21.138
2.188.21.70
2.188.21.46
185.255.91.60
66.185.123.243
2.189.44.85
2.189.44.82
2.189.44.83
2.189.44.86
2.189.44.84
2.189.44.14
74.80.77.247
109.107.159.45
2.189.44.92
2.189.44.94
2.189.44.91
2.189.44.93
2.189.44.90
78.157.41.60
193.178.200.3
46.32.31.30
185.208.174.167
85.185.157.181
77.238.123.179
185.141.105.139
5.160.140.16
5.160.227.78
185.53.141.230
185.105.101.1
37.255.223.218
85.133.129.242
78.38.174.2
37.191.95.70
74.80.77.244
74.80.77.245
93.118.109.213
194.61.120.143
121.127.46.65
93.126.5.205
5.160.137.130
2.180.21.241
82.114.164.226
@WhiteDNS</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/whitedns/639" target="_blank">📅 16:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-636">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سرور اهدایی از رسول عزیز از تیم وایت دی ان اس
Name: H3 (Germany)
Domain:
v.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Serbia
Domain:
v3.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Turkey
Domain:
v4.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: USA
Domain:
v5.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Switzerland
Domain:
v6.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: RMFT g1-7
Domain:
g1-7.rmft.tech
Encryption Key:
a337e9fa75161c44bebe7d717da36afc</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/whitedns/636" target="_blank">📅 12:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-635">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سرور اهدایی از چنل
@Masir_Sefid
لطفا از چنل دوستان اهدا کننده سرور حمایت کنید.
Name:
@Masir_Sefid
🕊
(1)
Domain:
v1.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(2)
Domain:
v2.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(3)
Domain:
v3.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Name:
@Masir_Sefid
🕊
(4)
Domain:
v4.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(5)
Domain:
v5.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/whitedns/635" target="_blank">📅 12:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-633">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سرور اهدایی از چنل
@pythash
لطفا از چنل دوستان اهدا کننده سرور حمایت کنید.
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 1
Domain:
v1.abolfazlshahi.cloud
Key:
a4c5649c628ac1103ad55c5208e0d74d
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 2
Domain:
v2.abolfazlshahi.cloud
Key:
965a568dccef58af7afb86e8ee55eea6
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/whitedns/633" target="_blank">📅 12:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-631">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHpn0QmTsaXB0doU4ac9dT8SiLxn0pzq0ctjciLaw_hdpc9SYz9rAvWtwAPVeHImfw9bQows4Trq0XSqQMx2p7blkt6WUT9_kZSfOKq4kl0o0Z8jahz1Ixq2H3IMPRAHPfzuaHRSZRiU4owzoFLe7WM51lvnJ97O2ImyA5mCTRYFZXUHzYrc0XPguwNgLO6M9mtYj2Ts-fm3p16bX4Z1bhvyGzTHV5lFkPhURRpzPm3MTOFG3aaMJT19xZ_6NSaFCyDMarXlLGLNi0E2IFh4aXg7YpDwoJq37jpaU8I_-Y4UusUwQsk3TkV_Fw657U5dmYTf3F2ohpM-di8u3n3y9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEHTim42I_xdALF11W6j2Mqg36HzPpCrphnCWZsSCo5GftLR9FGTJhDzKB8YtCid3jGo2MjiDfUnGtdx4e4uSa6NpGdlv71elWY4f30txqHPzIfkt1xFx9PTa6dBdM5I-2ZTDsDE1hEcLm_bMgDI1YGq3GOcp3VnN7chZeM8jO-MtbhM29GCd18dwN0Fg0-1IYojEXU7xuX6NPqtGkOE9F1z6-PRAiM3ATCLh3VZrhBwPzOIREue-wtXrP4cl7Qcv7aYRvfod9eL2UkAGVK_zBKLwoA8GuRd63xc9a_ZfES62GmE9y1OJfL2zv7wsks-0QsuqhiEKUXddB6YSbDz3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درحال حاضر نزدیک ۱۰۰۰ نفر فقط به سرور ما متصل هستند. سرور تا نزدیک ۲۴۰۰ نفر میتونه کاربر بدون افت کیفیت رو پشتیبانی کنه.
جدا از سرور های ما، سرور های اهدایی باقی چنل ها مثل مسیر سفید هم هست. ویدیو آموزش سرور اختصاصی هم پست های بالاتر گذاشتیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/whitedns/631" target="_blank">📅 11:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=XhwtNGRorqOIRG_ETjj0ddh1rwZHH-DfumCDOSFyFG5K_6YOVWTb5QE0ZifndG_8cvosDAx59nqs3wfJ8xp6_4kg_PK84Gamaosj1Ae3W_cN51duT6hJS6WMFQM3F-oK4DHakl_HkB2Dm5CZFQIYY8994-Vo4jehhU-JjJde2yLnKorRGb4O8J8-seez7nrr9lBDx0EX6Vl_xvAH0JTKewmPoGfngqO8NOPH1J-UTpf3u7yqtq_FtsLVvk7NSQ0Ba4-N6q_kgESK1n6SWfj22gc8RL7YWC2OUy6a5MndSZKmgUqMYNkb5_KneJ9ramHcRrtHHxWxdcp5BsF8NynXFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=XhwtNGRorqOIRG_ETjj0ddh1rwZHH-DfumCDOSFyFG5K_6YOVWTb5QE0ZifndG_8cvosDAx59nqs3wfJ8xp6_4kg_PK84Gamaosj1Ae3W_cN51duT6hJS6WMFQM3F-oK4DHakl_HkB2Dm5CZFQIYY8994-Vo4jehhU-JjJde2yLnKorRGb4O8J8-seez7nrr9lBDx0EX6Vl_xvAH0JTKewmPoGfngqO8NOPH1J-UTpf3u7yqtq_FtsLVvk7NSQ0Ba4-N6q_kgESK1n6SWfj22gc8RL7YWC2OUy6a5MndSZKmgUqMYNkb5_KneJ9ramHcRrtHHxWxdcp5BsF8NynXFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.site
Encryption Key:
bad99364093861634030e96f11fe3132
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
⚠️
⚠️
⚠️
⚠️
⚠️
حجم کپی از کانال ما واقعاً باورنکردنیه؛ در حدی که آدم شک می‌کنه شاید ما ناخواسته برای بعضی دوستان واحد تولید محتوا راه انداختیم.
کمترین کاری که می‌تونید انجام بدید، انتشار همین پست یا حداقل ذکر منبع کانال ماست. باور کنید نوشتن منبع، اینترنت رو خراب نمی‌کنه و از اعتبار شما هم کم نمی‌کنه.
همراهان عزیز WhiteDNS،
اگر دیدید کانالی بدون ذکر منبع مطالب ما رو کپی کرده، لطفاً با احترام منبع اصلی رو بهشون یادآوری کنید. شاید فقط فراموش کردن؛ کپی‌کردن زیاد آدم رو خسته می‌کنه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/whitedns/630" target="_blank">📅 11:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-625">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.3 MB</div>
</div>
<a href="https://t.me/whitedns/625" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان  نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
🤖
دانلود نسخه یونیورسال از سرور های داخلی
🔴
ویدیو آموزشی استفاده از اپلیکیشن…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/whitedns/625" target="_blank">📅 11:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-624">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLw0Y7DpEXFklwNUdTADG-0_8rnupUQIqdgEwruT90Xqd0aBzRo-iBmW63PgyUT-FTzsLokyNBT8PtpwoXb9NBIzNv6YUBE4KOS0WbJNYCH6ux3GbB4Bsea9uTTI9UMj5hNjB1uidNGJ41eTKHqRduKiaapIf_2QIqm3hTH8QImQ37B8VXQ9haxau-OlwJXnaUTrL94UDoNgn0b8fKeFdQbGCqbSkg-cHRDb3VM-3aStTd81DIlqpL00sC2f2drha1jh2eEinRL2-MiFvRhYt0OL9FHZENRRdjXZidIV8g5jEzOrpDdX2J0u3bgFgMt_SItx6zGJLm8SKnmDFUt9Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
🤖
دانلود نسخه یونیورسال از سرور های داخلی
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
تمرکز اصلی این نسخه روی ساده‌تر شدن اتصال و پیدا کردن بهترین تنظیم برای هر کاربر بوده است. هدف این بود که WhiteDNS قبل از اتصال، چند کانفیگ مختلف را با Parallel Test بررسی کند، بهترین گزینه را از نظر سرعت و کیفیت انتخاب کند، و کاربران بدون نیاز به گشتن دنبال Resolver، با لیست پیش‌فرض ۴۵۰۰+ Resolver داخل اپ سریع‌تر اسکن کنند و راحت‌تر وصل شوند.
تغییرات این نسخه
:
✅
نسخه اپلیکیشن به 1.4.0 ارتقا پیدا کرده
✅
قابلیت Parallel Test برای تست هم‌زمان چند تنظیم مختلف قبل از اتصال اضافه شده
✅
حالا WhiteDNS می‌تواند قبل از اتصال، چند حالت اتصال را هم‌زمان بررسی کند
✅
اپ سرعت و Ping هر تنظیم را تست می‌کند و بهترین گزینه را برای همان اتصال انتخاب می‌کند
✅
قابلیت Parallel Test هم برای Proxy Mode و هم برای Full VPN قابل استفاده است
✅
در حالت Full VPN، اپ اول بهترین تنظیم را با Parallel Test پیدا می‌کند و بعد اتصال VPN نهایی را روشن می‌کند
✅
نتایج Parallel Test بعد از اتصال داخل صفحه اصلی نمایش داده می‌شود
✅
می‌توانید تنظیم موفق Parallel Test را با نام دلخواه ذخیره کنید
✅
چند تنظیم آماده WhiteDNS برای تست سریع اضافه شده
✅
می‌توانید پروفایل‌های تنظیمات پیشرفته خودتان را هم وارد Parallel Test کنید
✅
بیش از 4500 Resolver داخل اپ قرار گرفته تا برای اسکن و اتصال راحت‌تر استفاده شود
✅
لیست Resolver پیش‌فرض داخل اپ کامل‌تر شده
✅
پروفایل Default Resolver اضافه شده تا اپ همیشه یک لیست آماده Resolver داشته باشد
✅
امکان اسکن مستقیم لیست Resolver پیش‌فرض اضافه شده
✅
اسکن فایل‌های بزرگ Resolver سبک‌تر و بهتر انجام می‌شود
✅
ریزالورهای تکراری یا قبلاً پیدا‌شده بهتر کنار گذاشته می‌شوند
✅
شمارش Resolverهای سالم و ردشده در اسکن دقیق‌تر شده
✅
اگر پروفایل اسکن سرور یا کلید نداشته باشد، اپ واضح‌تر جلوی شروع اسکن را می‌گیرد
✅
ویرایش سرور، Resolver و تنظیمات از صفحه اصلی راحت‌تر شده
✅
امکان حذف پروفایل‌های اتصال تکراری اضافه شده
✅
پروفایل Default Resolver از حذف یا جابه‌جایی اشتباهی محافظت می‌شود
✅
هشدار باتری حالا قابل بستن است
✅
نمایش سرعت، مصرف اینترنت و آمار اتصال دقیق‌تر شده
✅
تنظیمات پیشرفته برای اتصال‌های کندتر و مسیرهای سنگین‌تر بهتر تنظیم شده
✅
وارد کردن و خروجی گرفتن فایل‌های TOML با گزینه‌های جدید کامل‌تر شده
✅
هسته داخلی StormDNS به‌روزرسانی شده
تنظیماتی که به صورت اتوماتیک انتخاب میشوند، تمرکز روی سرعت و کیفیت دارد. امکان افزایش مصرف اینترنت شما با کانفیگ انتخاب شده می‌باشد. اگر نگران این موضوع هستید تنظیمات را مرور کرده و مقدار  Upload Dup را کمتر کنید.
⚠️
⚠️
⚠️
⚠️
⚠️
حجم کپی از کانال ما واقعاً باورنکردنیه؛ در حدی که آدم شک می‌کنه شاید ما ناخواسته برای بعضی دوستان واحد تولید محتوا راه انداختیم.
کمترین کاری که می‌تونید انجام بدید، انتشار همین پست یا حداقل ذکر منبع کانال ماست. باور کنید نوشتن منبع، اینترنت رو خراب نمی‌کنه و از اعتبار شما هم کم نمی‌کنه.
همراهان عزیز WhiteDNS،
اگر دیدید کانالی بدون ذکر منبع مطالب ما رو کپی کرده، لطفاً با احترام منبع اصلی رو بهشون یادآوری کنید. شاید فقط فراموش کردن؛ کپی‌کردن زیاد آدم رو خسته می‌کنه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/whitedns/624" target="_blank">📅 11:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-623">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yr0jf6qw2z4cqSOT2nognhA83zMonP705StaL4mRmZMwWwYCBLK6jsocmRghy0ixyGRwdeNXx3__jwmSZMcFpK0pwH8JmIfMQ7XpC5AflReZ6Mx6yLKu0EqfgC9URy48SCFBuSpCbr8ijy4xm-2xTDi6-cln_6hA_UuYo7JRssdFtLM56CCz1uTxj3yjI7c4Dui9UYvnkOHhW2FAU5Vw4yBHAlo5Yym7AoH2I7SPfdRWS7Ae-_mCEpiYCAtLIGDNpvaWgHS4rIXFXQpCrpUK4j5ualATQeuSfw8ZVQ2kwEQqd-eW7asz9ogqNAiXI4bFPbmwJgYkRk_5hjQqjIKJBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن ۱.۴.۰ کلاینت اندروید WhiteDNS به‌زودی منتشر می‌شود. در این نسخه سعی کردیم کار شما را راحت‌تر کنیم و اتصال سریع‌تر و ساده‌تر انجام شود.
در این ورژن، اپ به‌صورت خودکار ۷ تنظیم مختلف را با قابلیت Parallel Test بررسی می‌کند و در نهایت بهترین کانفیگ را از نظر سرعت و کیفیت برای شما انتخاب می‌کند.
همچنین بیش از ۴۵۰۰ Resolver که قبلاً داخل بات و گروه منتشر شده بود، به‌عنوان لیست پیش‌فرض داخل اپ قرار گرفته است تا بدون نیاز به گشتن دنبال لیست، بتوانید مستقیم اسکن را شروع کنید و راحت‌تر وصل شوید.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/whitedns/623" target="_blank">📅 10:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-622">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQIGLLm9Ps0HMYky5XY9hhQI6gnmBF7GwtjKXSbxr2Cx7uOPGPE2dOtKdPXqdUrdA0wgfYISrlR-vC_FN95E2vyNzeZ4FlwvrhP-lOe7VVgtKunn_tS9hjxuY2lS23bg_ItByxqOs7iBpovOUAvg8HpR2pFOwuJYGKM0MRlrSktQxYRGHMoQBWMPteNOx2li_UYzGnxk0EV7AumsIF0hTQObH-RFwDKFsZU_3v5WMji0iJAlCxEr6a9hxff5Zizq1HWbIQS-uRqLZnGNQaiAgJcdKk10EmWwdg1mi1nV9okLP2Ao_zZKVtTNwt3uY7690z5EMYfc1l_5-BeG5Ppoaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.space
Encryption Key:
bad99364093861634030e96f11fe3132
از همه کانال‌ها و دوستانی که این لیست رو بازنشر می‌کنند خواهش می‌کنیم حداقل سهم و همکاری‌شون این باشه که کانال ما رو به عنوان منبع ذکر کنند. این داده‌ها با زمان، هزینه و اسکن گسترده جمع‌آوری شده، نه با جادو و دعای نیمه‌شب.
این بزرگترین سرور ما هستش. ۱۲ هسته سی‌پی‌يو و ۲۴ گیگ رم.
✈️
هر مشکلی هست، از سمت اختلال شبکه، تنظیمات و ریزالور ها هستش.
@WhiteDNS</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/622" target="_blank">📅 07:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-620">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">StormDNS-Setup-Guide.mp4</div>
  <div class="tg-doc-extra">151.4 MB</div>
</div>
<a href="https://t.me/whitedns/620" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دوستان عزیز سلام
یک فیلم آموزشی آماده کردم برای نحوه راه‌اندازی سرور شخصی StormDNS/MasterDNS
دانلود سرور داخلی
https://guardts.ir/f/3c4216b2ea16
✍️
آموزش متنی
پیش‌نیاز:‌ تهیه سرور و دامنه خارج از ایران
1️⃣
آماده‌سازی DNS
ابتدا یک ساب‌دامین کوتاه بسازید و آن را به نیم‌سروری وصل کنید که به IP سرور شما اشاره می‌کند.
مثال:
ns.example.com  A   1.2.3.4
v.example.com   NS  ns.example.com
توضیح:
ns.example.com
باید به IP سرور شما وصل باشد.
v.example.com
باید به عنوان Subdomain Delegation به
ns.example.com
اشاره کند.
یعنی تمام درخواست‌های DNS مربوط به
v.example.com
به سرور شما ارسال می‌شود. اینترنت هم بالاخره یک جایی باید بفهمد با خودش چند چند است.
2️⃣
نصب سرور
روی سرور لینوکسی خود، دستور زیر را اجرا کنید:
bash <(curl -Ls https://raw.githubusercontent.com/nullroute1970/StormDNS/main/server_linux_install.sh)
بعد از نصب و اجرای سرور، برنامه به صورت خودکار کلید رمزنگاری فعال را نمایش می‌دهد.
همچنین این کلید داخل فایل زیر ذخیره می‌شود:
encrypt_key.txt
برای مشاهده کلید می‌توانید از دستور زیر استفاده کنید:
cat encrypt_key.txt
3️⃣
موارد موردنیاز برای اتصال کلاینت
بعد از راه‌اندازی، برای ساخت پروفایل یا اتصال کلاینت معمولاً به این اطلاعات نیاز دارید:
Domain: v.example.com
Encryption Key: مقدار داخل encrypt_key.txt
Server IP: 1.2.3.4
لینک داخلی:
https://guardts.ir/f/3c4216b2ea16
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/whitedns/620" target="_blank">📅 03:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-617">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tauy9BokIv7ESOLaAf8b4inPYCHFZ-qs8XNh9yG6U3FITLC3SwYaAoZlJZjUcUXp3xtokorfEHJPRw5sZHW8pKquR-04XnEd3OSD4vIPNCP1pQhLQ2nmrEwYWNAM-766KStLijbVIvEDge1H1dO-yRqViGYDOgYI45ozVUtX-eJv_o_V3tqyQXCMLClO0auIDZ46qLMCwibEOULLtZIv-gLmftWCKou-u18JKSeBojpATVlM6_CcHgiOSrNthXqndIc6ijqttar_LjGctjAAfbEyoVFDrGxH60xq_4IpgvtMIX9wpyWKfUZCai0yEAXDUmEPb_7rpK-zJMoklvGxGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vD5MMXgXV2_IzB1-zwnhBNK6kBuhFOJKGQ-wqnegY1BsAsM0kyjIgK2-o-fP0WERC80QwH2d4HnAojHWzuS05_JNkIhc7uzpBjOiF_rfu4G4nlHouOs1sByZ50Hf2MBaUCybirAheP3FdLwGakKio_OuQwdNUkNS9TfLV5YLulBzuSpkE994Zrcmr9bZgJXxgjV8i0EaCPruoX9K1QofuVwpgWRl15BwR-PFE4XX6eJRRgKUd1jDW6UJFYKgY859LxKCPXoOtN0_cv4K5u3jrNkNmb_X1a6cjNKuDKN3mh5uUfAoPPZXERO8vaVJmXGa2DxYJBZhnLamV0xAUeOV9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داخل پروژه
TheFeed
که متعلق به
Sarto
عزیز هست یک فیچر برای ریزالورها وجود دارد. یک
جدول امتیازدهی برای ریزالورها
درست شده و بازخورد خوبی از سوی کاربران داشته بخاطر اینکه وضعیت ریزالورهای داخل جدول به طور واضح مشخص شده است.
همچنین خود برنامه به صورت رندوم از ریزالورهایی استفاده میکند که امتیاز بیشتری دارند تا کیفیت اتصال ریزالورها به
حداکثر
برسد.
متاسفانه اکانت گیتهاب
Sarto
ساسپند شده اما میتونید برای دریافت برنامه‌ی
TheFeed
به لینک زیر که پست کانال خود
Sarto
هست مراجعه کنید و ازش
حمایت
کنید:
لینک پست
@WhiteDNS</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/whitedns/617" target="_blank">📅 00:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-616">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
آموزش خیلی مقدماتی و ساده برای استفاده از این نسخه
@whitedns</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/whitedns/616" target="_blank">📅 18:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-615">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">6.8 MB</div>
</div>
<a href="https://t.me/whitedns/615" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Whitedns windows v1.0.2</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/whitedns/615" target="_blank">📅 17:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-614">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LmV03CkZ4LhLiwqEklwO9LNv54wDMhCmtFijgaVqSB3G_a1QUMXjp4wLlGOlNHaBid58j4UsRzPeYsUxNvPMQAvM0GWKjRFeT_CxOFqLZ-z5g14_mw4p5ju1fTX5iDxbEU5925vn9jjfwM--oplJPc277L6WBiBHEp5uYDCOv84z9Q72nDKfu80ibGlSnuORHwEmUFtSAkqKZsZvAbf7k_l0bdpDz4MKLsYgDKucrtEzwYHJNtI9GMiaIdeNt-_asgnxYWCS2sBVmsdaz31DbUQ_kSAXmEFbvoROGGpBT_kHpaOnA5kWTHI6hoBdGIFm-Nvl4TmVMsMkR7xiPbGCLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
🔥
🔥
🔥
🔥
نسخه ۱.۰.۲ بر پایداری، قابلیت استفاده و تشخیص‌های بسیار قوی‌تر رزولور تمرکز دارد.
🛠
این بروزرسانی مشکل آکاردئون را در بخش تنظیمات پیشرفته اصلاح می‌کند تا بخش‌ها با قابلیت اطمینان بیشتری باز و بسته شوند و چیدمان تنظیمات رفتار سازگارتری داشته باشد. همچنین اسکنر رزولور را با یک حالت اسکن پیشرفته جدید بهبود می‌بخشد که رزولورها را به روشی واقع‌گرایانه‌تر و آگاه به تونل، با استفاده از دامنه فعال تونل آزمایش می‌کند، از جمله بررسی‌های DNS بدون کش، قابلیت EDNS0، یکپارچگی NXDOMAIN، مدیریت زیردامنه‌های تو در تو و جستجوهای پروب به شکل تونل.
🌐
تجربه نتایج اسکن نیز بهبود یافت. اکنون خروجی با اطمینان بیشتری کار می‌کند، مرتب‌سازی به درستی عمل می‌کند و نتایج صادر شده اکنون بهتر با آنچه در رابط کاربری نمایش داده می‌شود مطابقت دارند. جزئیات اضافی اسکن مانند امتیاز، دامنه پروب و قابلیت مشاهده بار EDNS اضافه شد تا رزولورهای قوی‌تر را با دقت بیشتری شناسایی کنید.
📊
✨
@whitedns</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/whitedns/614" target="_blank">📅 17:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-612">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/LMIgqAJI2oU2QNAQHZbvzlPJQkbanMuHfMGaf73iLyeDNzEqKiDXS8XDDclke2OXmkZ04qQJ90k45hxRn6OMqAFfZCTiM0-BPeLHRiWRcwJLz5ZQQL4W2P3A0INUJKwjarLcNJO-v-3YGjj5n5tOY9eE-xYSfmRqbnOKVym1vsuKkOd1XbEueJnuobh9U47fj0ctzB43Bpj-dlJEXKR9r6CrCTuoIuTyAcUrFfgDLWbTrtuZ6f9rfOCxgWxKAHK16jRrHWzknq94ox0QmNl3FojbR5FiP0StUbZfsd3It_6PkoUuC2RxFZemJ-Do81iGJOPdi-iSHlEQqVa2ldMeiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/ntgUm7W80bl9XaxREG-o6f33W9a-l1KtXx1n_PHwlYd_760eg1a7r0qKclZMWT_41xAgQUH6iPK7pgW0pV2rKjKx-n44am0hbr8rSCD7kSRyL8SiPZN7Xv573of6cIOEmVIBY8TrQKfwOyYu3dtavOTs696DQYYMKmwC2ZEL6tcvPTY55ptxaiGeTdJ-Xb7VrRbeGaqmXFU_-sE6zKNVZuXCpi172xpaDhFbxlz6lrQE8WWftdVjR6lHrrsMVu4gl7HEQ6PuC5R2sl9TiFkktRn0_prqN_WAbIEK_rlFTkim7zt4O3ryBhzkn1fUlicC5PdDo-z8wsjYqubBZ-zm9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">(موقت)
تنظیمات کلاینت Whitedns اندروید
همراه و رایتل و اپتل و مخابرات
یکی از اعضای عزیزی کانال "ارام " زحمت این کار کشیدید که از ایشون تشکر میکنیم
@whitedns</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/whitedns/612" target="_blank">📅 17:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-611">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/whitedns/611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🛡
مهم: اگر این نسخه رو نصب کنید دیگه دردسر ستاپ کردن MITM و... ندارید!
این نسخه حدودا یک ساعت پیش توسط برنامه‌نویس شیر و خورشید آپدیت شد و به راحتی می‌تونید طبق این آموزش بهش وصل بشید:
1- وارد اپلیکیشن شیر و خورشید(آخرین نسخه که امروز منتشر شده) می‌شید
2- وارد بخش Options میشید از نوار بالا
3- روی More Options کلیک میکنید
4- گزینه‌ی  Connection Protocol رو قرار میدید روی CDN Fronting
5- میرید و عادی کانکت میشید و به راحتی وصل میشه!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/611" target="_blank">📅 16:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-610">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting-14.zip</div>
  <div class="tg-doc-extra">18.3 KB</div>
</div>
<a href="https://t.me/whitedns/610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">☠️
آموزش اتصال رایگان و نامحدود به اینترنت با متد ترکیبی MITM + Psiphon
⚡️
لینک‌های داخلی جهت دانلود: https://guardts.ir/f/db4006f1197c و https://uploadgirl.ir/d/1f4fb76a-c869-494a-b439-b11cb8d35947 (شامل فایلهای V2rayNG، کلاینت شیر و خورشید، ویدئو آموزشی،…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/whitedns/610" target="_blank">📅 16:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-608">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش اتصال رایگان و نامحدود به اینترنت با متد ترکیبی MITM + Psiphon
⚡️
لینک‌های داخلی جهت دانلود:
https://guardts.ir/f/db4006f1197c
و
https://uploadgirl.ir/d/1f4fb76a-c869-494a-b439-b11cb8d35947
(شامل فایلهای V2rayNG، کلاینت شیر و خورشید، ویدئو آموزشی، V2rayN و فایل Certificate Generator و خود فایل Json پترنیها)
لینک پروژه اصلی:
https://github.com/patterniha/MITM-DomainFronting
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از متد ترکیبی سایفون(کلاینت شیر و خورشید) + کانفیگ دامین فرانتینگ پترنیها، به اینترنت بین‌الملل وصل بشید!
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/whitedns/608" target="_blank">📅 15:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-606">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQqqxz6xhyCXoHt4ZJ79NsuhIED8zH2IECciKM0GLOnYXTQS7Xeel4IYXQ_Xr_dEDrPf_o4uvYNIwRNOaUpaDKsrTIK_vDCM4iPAY1MrJRhSjqHO9JvnQOk9GejVtD0m1bTx2SpPTaLvek9G6NoOoUm36ayOVrSvnSHsrZktKU4l26ZV4e7l6CNUIY-xHQmWsk8aLjKBH-My3cJjvS2cBRUD1zlJHqfFbQRbFkxwXZ5wXJrRtIKiNui1iZNna6Quv4hM6cKliNvV3IAPsotDUMEGL9-nPHdXlfOOnvfOWpTOFaGE4MuFDezxUHT7GUlM3ldmQUlcPUPreEq8dVRRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.space
Encryption Key:
bad99364093861634030e96f11fe3132
از همه کانال‌ها و دوستانی که این لیست رو بازنشر می‌کنند خواهش می‌کنیم حداقل سهم و همکاری‌شون این باشه که کانال ما رو به عنوان منبع ذکر کنند. این داده‌ها با زمان، هزینه و اسکن گسترده جمع‌آوری شده، نه با جادو و دعای نیمه‌شب.
این بزرگترین سرور ما هستش. ۱۲ هسته سی‌پی‌يو و ۲۴ گیگ رم.
✈️
هر مشکلی هست، از سمت اختلال شبکه، تنظیمات و ریزالور ها هستش.
@WhiteDNS</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/whitedns/606" target="_blank">📅 09:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-602">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">📢
اطلاعیه مهم برای کاربران WhiteDNS
دوستان عزیز،
برای بهبود کیفیت اتصال و افزایش پایداری سرویس، تمام سرورهای فعلی WhiteDNS به‌زودی پاک‌سازی و جایگزین خواهند شد.
✅
سرورهای جدید به‌زودی از طریق همین کانال در اختیار شما قرار می‌گیرند.
تا زمان انتشار سرورهای جدید، لطفاً فقط به سرورهایی متصل شوید کهآدرس آن‌ها
whitedns.shop
نیست.
یعنی فعلاً از اتصال به سرورهای دارای دامنه زیر خودداری کنید:
whitedns.shop
ممنون که همراه ما هستید
🤍
@WhiteDNS</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/whitedns/602" target="_blank">📅 09:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-601">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/E61epcfHv0UfnY8sG8HXBIo3T3JpzWpNjh7GBKJ1V316LZuUNexTeWEAHjk8eymnMQD1cf_XWNsnDnFCePJYCikAA-a70r1DA3pZPHuYQ_lf3vB4Sa2x0xhDAtUJXKksLfR6G6JcG7hT61QpzNMqRCY3C9pnjw6SoJRFur0g9QPy8pDIKQ4vlyaDQEftTk2FMj4Z1dQUx1cY7EP01DEJb_GP9g4EM_StsBbMHovunKarwLsSjXUkfguG1EFdi1BYIX01RwqctM26sHkw2ea_Opj_lY6NOY3eBCwg20OdiUAuH4L1GxBegux1YaZ5BOVTDftwSskv7VHtTV-L5yfHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
به زودی.................
🔥
🔥
🔥
🔥
نسخه ۱.۰.۲ بر پایداری، قابلیت استفاده و تشخیص‌های بسیار قوی‌تر رزولور تمرکز دارد.
🛠
این بروزرسانی مشکل آکاردئون را در بخش تنظیمات پیشرفته اصلاح می‌کند تا بخش‌ها با قابلیت اطمینان بیشتری باز و بسته شوند و چیدمان تنظیمات رفتار سازگارتری داشته باشد. همچنین اسکنر رزولور را با یک حالت اسکن پیشرفته جدید بهبود می‌بخشد که رزولورها را به روشی واقع‌گرایانه‌تر و آگاه به تونل، با استفاده از دامنه فعال تونل آزمایش می‌کند، از جمله بررسی‌های DNS بدون کش، قابلیت EDNS0، یکپارچگی NXDOMAIN، مدیریت زیردامنه‌های تو در تو و جستجوهای پروب به شکل تونل.
🌐
تجربه نتایج اسکن نیز بهبود یافت. اکنون خروجی با اطمینان بیشتری کار می‌کند، مرتب‌سازی به درستی عمل می‌کند و نتایج صادر شده اکنون بهتر با آنچه در رابط کاربری نمایش داده می‌شود مطابقت دارند. جزئیات اضافی اسکن مانند امتیاز، دامنه پروب و قابلیت مشاهده بار EDNS اضافه شد تا رزولورهای قوی‌تر را با دقت بیشتری شناسایی کنید.
📊
✨
@whitedns</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/whitedns/601" target="_blank">📅 08:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-593">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.3.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.2 MB</div>
</div>
<a href="https://t.me/whitedns/593" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
تمرکز اصلی این نسخه روی اسکن Resolverها، مدیریت ساده‌تر پروفایل‌ها و پایدارتر شدن اتصال در خود WhiteDNS بوده است. هدف این بود که کاربران راحت‌تر Resolverهای سالم را پیدا کنند، نتیجه اسکن را ذخیره و دوباره استفاده کنند، و اتصال Proxy یا Full VPN در پس‌زمینه و بعد از قطع‌و‌وصل شدن مطمئن‌تر بماند. در کنار این موارد، امنیت خروجی‌ها، بکاپ و اشتراک‌گذاری فایل‌ها هم بهتر شده است.
✅
نسخه اپلیکیشن به 1.3.0 ارتقا پیدا کرده
✅
بخش جدید Scan برای بررسی و پیدا کردن Resolverهای سالم اضافه شده
✅
حالا می‌توانید فایل Resolver وارد کنید و اپ خودش Resolverهای سالم را جدا کند
✅
نتیجه اسکن به‌صورت خودکار داخل پروفایل‌های Resolver ذخیره می‌شود
✅
می‌توانید نتیجه اسکن را با نام دلخواه به عنوان Resolver Profile جدید ذخیره کنید
✅
Resolverهایی که قبلاً سالم شناخته شده‌اند دوباره بی‌دلیل اسکن نمی‌شوند
✅
امکان توقف اسکن و ادامه دادن آن از همان‌جایی که مانده اضافه شده
✅
سرعت اسکن قابل تنظیم شده تا بین سرعت بیشتر و مصرف باتری کمتر انتخاب کنید
✅
وضعیت اسکن با تعداد کل، سالم، ردشده و میزان پیشرفت واضح‌تر نمایش داده می‌شود
✅
می‌توانید برای اسکن، پروفایل سرور جداگانه انتخاب کنید
✅
اگر پروفایل اسکن سرور یا کلید نداشته باشد، اپ واضح‌تر هشدار می‌دهد
✅
حالت روشن، تاریک و خودکار برای ظاهر اپ اضافه شده
✅
مدیریت پروفایل‌های اتصال، Resolver و تنظیمات پیشرفته مرتب‌تر و راحت‌تر شده
✅
امکان وارد کردن تنظیمات پیشرفته از فایل یا متن TOML اضافه شده
✅
امکان خروجی گرفتن تنظیمات پیشرفته به فایل advanced_settings.toml اضافه شده
✅
خروجی گرفتن و اشتراک‌گذاری فایل‌ها امن‌تر و تمیزتر شده
https://dl.toolschi.com/view.php?f=e15bcec825298e4c.zip
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.3.0
از همراهی و حمایت شما ممنونیم
❤️</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/whitedns/593" target="_blank">📅 06:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-588">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بعد از اسکن بیش از
60,000
آی‌پی، تعداد
435
ریزالور سالم و قابل استفاده پیدا شد.
لیست این ریزالورها حالا از طریق ربات زیر در دسترسه:
@dns_resolvers_bot
برای دریافت لیست، وارد ربات شوید و دستور زیر را ارسال کنید:
/dns_master
بعد از ارسال دستور، می‌تونید لیست ریزالورها رو دریافت کنید یا فایل آماده رو دانلود کنید.
از همه کانال‌ها و دوستانی که این لیست رو بازنشر می‌کنند خواهش می‌کنیم حداقل سهم و همکاری‌شون این باشه که کانال ما رو به عنوان منبع ذکر کنند. این داده‌ها با زمان، هزینه و اسکن گسترده جمع‌آوری شده، نه با جادو و دعای نیمه‌شب.
Source:
@WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/whitedns/588" target="_blank">📅 18:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-587">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سرور اهدایی از چنل
@pythash
از چنل اهدا کننده سرور حمایت کنید.
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 1
Domain:
v1.abolfazlshahi.cloud
Key:
a4c5649c628ac1103ad55c5208e0d74d
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 2
Domain:
v2.abolfazlshahi.cloud
Key:
965a568dccef58af7afb86e8ee55eea6
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
@WhiteDNS</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/whitedns/587" target="_blank">📅 18:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-586">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
پروفایل های مخصوص وایت دی ان اس ورژن رسمی (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲۳ اردیبهشت
👾
لینک دانلود
کلاینت :
1️⃣
WhiteDNS
1.2.0
⬅️
نحوه ی اضافه کردن پروفایل ها
⬅️
فیلم اموزش وایت دی ان اس
👍
تنظیمات مخصوص وایت دی ان اس
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
(پیشنهادی)
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigxKSIsInNlcnZlciI6eyJkb21haW4iOiJ2MS5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigyKSIsInNlcnZlciI6eyJkb21haW4iOiJ2Mi5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigzKSIsInNlcnZlciI6eyJkb21haW4iOiJ2My5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig0KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NC5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig1KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NS5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/whitedns/586" target="_blank">📅 18:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-585">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/av_p4q8DY1d6KQgm94xY1TUCHZtkVFSeizf17lINLXvHMbVnB9B6ChCOm4WkX1WvEe1JRnoUJkUvWiUewUytnaZGqkZPTppReYMEg-PXOVH_Y4S_2EJvGvTo-1ZdvDtwmD_FCeP2ZenERf3kaVmb00Batx9HMGiJTiHj7BdVSP3c4XehHntHLKrtV_fGKdv7kc7EmRg4o3EQ3iULuVKRU2tvi39n1DROzUN0JRd4aYpZdgVYEQAfEoAicBFrK_ilVJAUbItXUqYvj7MVyoi2bWnaHflTfC_zUjtMxmqFlb5bwgO-Mp9lwWyBhJP_ClX81bEGemYTXlZHccM6osaMKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/whitedns/585" target="_blank">📅 16:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-584">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">9.1 MB</div>
</div>
<a href="https://t.me/whitedns/584" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
انتشار اولین نسخه ویندوز WhiteDNS
نسخه
WhiteDNS Windows V1.0.1
منتشر شد.
این اولین نسخه رسمی ویندوز WhiteDNS است؛ نسخه‌ای که برای شبکه‌های سخت، محدود و فیلترشده طراحی شده تا اتصال پایدارتر، سبک‌تر و قابل‌اعتمادتر فراهم کند.
در این نسخه تلاش کردیم هسته‌ی ارتباطی WhiteDNS را برای ویندوز آماده کنیم و امکانات اصلی را در اختیار کاربران قرار دهیم:
• انتقال ترافیک از طریق DNS Tunnel با سربار پایین و پایداری بهتر
• پشتیبانی از چند مسیر اتصال از طریق چند Resolver و Tunnel
• تشخیص سلامت Resolverها و غیرفعال‌سازی یا فعال‌سازی خودکار مسیرها
• مدیریت هوشمند MTU برای حفظ پایداری اتصال در شبکه‌های ضعیف
• بهینه‌سازی جریان اتصال برای SOCKS4 و SOCKS5
• سرویس DNS محلی و قابلیت کش DNS سمت کلاینت
• پشتیبانی از روش‌های رمزنگاری مختلف مثل AES، ChaCha20 و XOR
• استفاده از Wintun Adapter برای ساخت اتصال VPN در ویندوز
• مدیریت Route و DNS به‌صورت خودکار
• رابط کاربری دسکتاپ با امکان ساخت پروفایل، ذخیره‌سازی امن، Import/Export، ویرایش ساده و پیشرفته، نمودار زنده، لاگ‌ها و تنظیمات
این نسخه شروع مسیر WhiteDNS روی ویندوز است و مثل همیشه با کمک فیدبک‌های شما بهتر و پایدارتر خواهد شد.
اگر تست کردید، لطفاً نتیجه اتصال، لاگ‌ها و مشکلات احتمالی را با ما به اشتراک بگذارید تا نسخه‌های بعدی دقیق‌تر و قوی‌تر منتشر شوند.
لینک داخلی :
https://uplod.ir/8h2n22ficr8f/WhiteDns-Windows-Setup.exe.htm
Special thanks to
Masterdns
❤️
for their amazing work - without them non of this was possible
@WhiteDNS</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/whitedns/584" target="_blank">📅 14:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-583">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BDH-Dl1m0NmoDuS7br5PjKjxArlmji6GmqQiAMdnD7cnuDrTzUJdEZtbSE0xpVCXfIDZ5fQ2FSJHITp5xcUstBt1iSeQEdg0G-dDr4gkrDbnkGZx91uVfailtQpdabICUQ8v26SeGA1tYtqpAh8zrgKhpA8ZSeiSxSdBHE-RbrGlmJCLuYiblbZ7O9XjMXvViYAAOUBftwi-7znMnxeUUSHW5LYkMkA82Tv3uod0qpgu0a1pZiGn74vgGx6TL73a_qmrFSAIRgZtHICrVxCfcBsy6iNR1vovTXcpQ4BtZncijvWygrmbXRmGJEXldYfrz3chtP3WGtHjxVeAylB8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/whitedns/583" target="_blank">📅 14:29 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
