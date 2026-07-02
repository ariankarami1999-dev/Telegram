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
<img src="https://cdn1.telesco.pe/file/LT2f9SjUzaqJO7RWmztSs8Jr5M6gZzlxUGC9yDEp1ZYBUag3JR1kL_EPR74wh1FE5dehrxebKaLHMLEBjdxRFQWDqCvcI_B6YUBQdNQpglkRIGaFLC6i08bYLK0CAh3nrJkRAcbDKgKp9rXBRzHnBfegsQtJZ6x3PGZBz7K0bSP-6Vfzd6TvOOyeAXsU7_E_JVQOA1ujsERHgve-Jczf5UGMQCl3JxbISgI_3JAaZ2IO3b2wBWbXz1Cl6rP8cFr-ZAR2nalCs6J0DloniWUqwtxhp8eTappZVlUNzB01VUB2uXl_dlb0acxmb0aIDn8yX_SCQ6hsV-aeVfEV4ZpSpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 159K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 21:52:34</div>
<hr>

<div class="tg-post" id="msg-4187">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/MatinSenPaii/4187" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4186">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:
matinsp.job@gmail.com
سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/MatinSenPaii/4186" target="_blank">📅 21:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4185">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X7xTmv-nPLyrv9XSppzmDQ8YuWqVZYK5IrZldDFj7qu0ZJGxnO8ZZ9BCI5WRJ-s0bEnYE03WZphiQysCoXQNP4vZ9NJf6nrcaG97keo2r0XhUH17GhXfg3TFir4V4Fs-tRHsRpwjYQnzALHwXzqOjMl8ZW6YOWSduBvmwc1ZweEhRjUg6W0JHKW33T_55XNBFlAYoAJtMEf8mSfY86yQCJFnXZ-_ufmrKd9a4VaHPtuEcT5kuvsbE4DT1ildOk-YaGlGEdKLJcCr0kb7vECK2npdsEc1bjRxdEjKm9SJu7W4yKbtOcEOkI8WeGTxyZYyZqdh7clFtQHz3wlPsdN5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی هم تر و تمیز و عالی</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/MatinSenPaii/4185" target="_blank">📅 21:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4184">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فیلم آموزشی Clash Party
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/MatinSenPaii/4184" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4183">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/MatinSenPaii/4183" target="_blank">📅 21:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4182">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.
نتیجه این تست، هر ۳۰دقیقه داخل این مخزن گیتهاب برای سرویس های متفاوت قابل دسترسی خواهد بود.
🌎
ساب مناسب اپ های V2Ray, V2rayNG & ...
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
🌎
ساب مناسب Clash Mi, Clash Party
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
🍏
IOS App
: Clash Mi, Karing
👾
Android App
: Clash Party, Karing
👍
Mac App
: Clash Party
📱
Windows App
: Clash Party
📱
Linux App
: Clash Party
@WhiteDNS</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/MatinSenPaii/4182" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4181">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده. هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/MatinSenPaii/4181" target="_blank">📅 20:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4180">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده.
هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/4180" target="_blank">📅 19:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4179">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز: https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو: 00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟ 04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس) 13:47 نصب و راه‌ اندازی روی…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4179" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4178">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">886 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4178" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات نصب Hermes روی سیستم‌عامل‌های مختلف و سرور
سایت YottaSrc:
https://yottasrc.com/
سایت Netlen:
https://www.netlen.com.tr/
سایت Senko:
https://senko.digital/</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4178" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4177">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tudDCb-5ih9vIjFQ3Y0rO8KHtXYRbLpHzXe00Mk3ZzMxNbDvshwIYWsuynbLWmLb4jMqKLr-gq-IMTFmkvWecT9RXCMl55Lr8vxhneOo7XQ7iqSIzxlyeAMYMXXTOT5cJCiJ8NlhNJ3ei9YmMm0AiYH2UZ7sDoKrM3g-Y-pwj8dskx-dQvXsqswaIinSEc_nzcTrNzMekho5eLMI9zRqcF9WXvyKEEZSO5ZunWhu0F3jLEtQ31GUoTUPKWDK5g9GIlVwO8pWWa_E189GMFbl98076-ppsYFYddY9e8GAYK9rIF8NeCGFPtNdqUFpL8-5RQBq9T0AiYFyauJv_-9vqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو:
00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟
04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس)
13:47 نصب و راه‌ اندازی روی سرور لینوکسی
16:46 نصب 9Router روی سرور لینوکسی
18:10 استفاده از API و مدلهای رایگان قدرتمند Nvidia
21:20 دور زدن محدودیت دسترسی به API ها با Worker کلودفلر
22:40 استفاده از Endpoint 9Router بر روی لینوکس و ساخت Combo
24:31 اتصال Hermes به اکانت تلگرام( و واتس اپ و دیسکورد و...)
26:35 نوشتن یه کرون جاب کوچولو که هر 5 دقیقه قیمت بیت کوین رو بفرسته و تحلیل کنه
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4177" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4176">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ویدئو 2 ساعت و نیم ضبطش زمان برد، بعد از ادیت شد نیم ساعت
😭
دستم شکست انقد با موس اسکرول کردم</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4176" target="_blank">📅 04:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4175">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M-fIpp4dC3jVfMavwVCGqD2r5pYX3MxyqL1Ap1-xTzIG3ZnKzBKNKfw7sFa_OyWDcYY7FGeYLEHukZEzZhKDvmyS-Sd6GiPJyU8izTSPAC2tjXzX7vZHhl1fjXCavIr5Kop-_CVJsqG1IcTICS43lIIjtfpNTammO31w6tZFv04Pkab668VrrH0cZ_DDWK5hE_RSu7s6B8_qwEq-uYL60B3__W8DLYOpWzBJoVnt92AUKI4kxvU3BPLGjHw8DzVO9X8uVeewj7n5KVwr5j5kQRT8Xa6KVOCUcmJFkr0doBNpAR_6RdWPPRzwMb0WBMUVwrNxnSQL4B91FIRfOfWpPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط دسترسی به Fable هم برگشت</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4175" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4174">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وسط ضبط ویدئو به طرز ضایعی یه ۱۲-۱۳ بار به ارور خوردم
😂
(اون پشت حلشون کردم و شما قرار نیست ببینید. هاها)</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4174" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4168">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4168" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4167">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMl3yluK-Jt4xkbaPUcKvWHpeCKLe6p9uIAH529AGg49xOoQ7PPEI0P1mLsC4qBuXKs0ZZZm26ocMxlgvKgXiXtmnNmcJEzf8JBRwOvISu6Tmgwntip1QEppHLt66Vpi7HSzWqHaOftVwTLjAbVOSEDLjqTiKW8p88vdfj0bIK3hlxW4QDeNZDxfnCO8r6HwcnHLB1c6RWhOXZcLo356tvWdKUxpMdC1zPTs8sA3QnQPAXSc2kUgi8w5TPn445CBdWaI9774wjtwjAEzL071StdyO74xrZvmW92I2y3u4hknrvBOuJL-Cm8PUSuTgmSCQ62mximKk5Gwx9mr6HuNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop 1.0.0-beta6 منتشر شد
در این نسخه، ماژول جدید WhiteDNS VPN به WhiteDNS Desktop اضافه
شده.
امکانات این نسخه:
• اضافه شدن WhiteDNS VPN به اپ دستکتاپ
•  انتخاب هوشمند بهترین سرور
•  نمایش کشور و وضعیت سرورها
•  اتصال بدون نیاز به تنظیمات پیچیده
•  تجربه کاربری ساده و روان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/4167" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4166">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XCuAj5ceaDHAq3S2agIGIAcZ9WcbbUpR0QhqSbe8-MqJ1j5qheUGTpcfSlIBxr9j_9K0UGP13DgRYxZv5BpJEnKw2B_3oQEVuic3rfJYMSQq6_R1qarXtH63_0SxqprpudsGChcvCszTj0LpBT4y48z6xr7WBaJgC4MCHaZ9v2xv4YvtqkWaeortD_xMPAlNsybzhPe_JbJp4A13pVL18Luo4_gkkVQ2oHDBYOl9aEecrEAoglvPFjkbcI5r_mg2JkXtJvfWm7gNXvZReGlWUJDuwhEIn3zhAhxTebt8QXdLTm2kfwgiSo4zGSWrKix-cpu25J5s40gb20yzLlMOfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این api هایی که Nvidia میده واقعا سخاوتمندانه‌ست. 40 ریکوئست در دقیقه
با 9router انداختم پشت هرمس، چه میکنه این Qwen و MiniMax3
توی ویدئو آموزشش رو میدم که چطوری بتونید وریفای بکنید و ProxyPool هم بزنید که روی سرور مشکلی نداشته باشه(مثلا با آیپی سرور من مشکل داشت انویدیا که با یه رله کلودفلر حلش کردم)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4166" target="_blank">📅 22:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4165">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4165" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4164">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cGPRiXxjjNp9ZTUVIpgV_pP4_MstyN7cTUp0Ds4oJ0W3WZLRPeAlv6pv0F7DR_9AFdj1lpgcVajNWrQo83-Mu2D3CgxZ8G17lweIMFOPz1Y1R-k2yf_NrCKJrx7BwdmgirFM5GZ1S75c-4ri-59lSI_QyUXBqXm5KExmKRTR8wMAZcQUTGysIwV4bn6DiHBFeSecqz2BP2G0m5rz2bUY61eQ49l_r1M7GVUYYUQ63ZyapT2seI4FkGbPLnuqyv9k-eMA7Ww-0l_mIQ34KpG7FNst0x5lJgCnXekgYbYMDrqA8w2NvhJnGw6PhdupETvTkrmcmM_y-dtPpaEDDQZRbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی زیرساخت‌های پیچیده‌ی پرداخت هم بشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4164" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4163">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">از بین سایت‌هایی که تست کردم برای SMS، کاوه نگار که باید میرفتی از دفتر اسناد رسمی احراز هویتشو انجام میدادی، فراز اس ام اس هم که شیش ساعت گشتم اصلا بخش API پیدا نکردم انقدر UX اش درب و داغون بود. بیست دقیقه وقتمو تلف کردن این دوتا تا وقتی که رفتم
sms.ir
و همه چیش اوکی بود و 10 تا هم پیامک رایگان داد. خیلی هم سرراست api تنظیم شد از خارج به داخل هم دسترسی داد</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4163" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4162">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تمام رادار جنگ الان فعاله و AI هر نیم ساعت یه بار، خبرگزاری‌ها و پنج-شیش تا کانال تلگرامی رو چک می‌کنه و اگر جنگ شده باشه و اسرائیل و آمریکا به ایران، یا برعکس حمله کرده باشن، پیامک میده</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4162" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4161">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hNDHM3BCg-JopextW9SRkz9vEe-suhgKSL2U0NLQS6ZDZQn44q1SawcriE7p1EMmFMWZ1xmfT0WuXlRFSo3J006AfXdMcyZvhwt-zl0xwBtlu0nF9vXVHnaHRJbh13sFO5zhrbjeN_9CIMeCnff6y1PfWLYETwtfNqXkrUht1fiOwO5kkmXYBT-7ZZINWkBAGWAZ48buDusT-EGJz2M19mLDwUnCW59bFjYxKUf9iR4WIIdRMe9eB0tw7CSxn1OENAPNqZvlUe8tIVdde1H1-gAuYih2sfkIR6oi9_zdMZfZD_ObNxbyzXYTURrXcWotmIce7V-_bXaAWJw_31dQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4161" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4159">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4159" target="_blank">📅 15:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4158">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ivPw8qGNJJ_44XDsdz77ZsAq2DCjC3ObXD3V5YqShO8FjXROr--ohCGFeD00CRv0hEjOEIFx6Mh2CKU9eA8rOnKmopTSkIOfwg2BW1pgvILIzhCMglVdp_OpTRyt1TFrSiRw9iUUEsVAwnrtN8E1-Rb0x-5yCO13YnbwMxm7_G390MS9am-KIrj1TKApD8Uy8jzwGsnbFLU-mrLbjH4dbLy7Kp_ovXgwp8g4JsjRZiiSSBwHBDKMf9h525fUh1Bu3wNlhu5QaqgCnT9XuOqT3VsFQdPuIIxbUgzN41NYFKu_Fs_lgFiA6TL2Sq5cLDPvt0VdEzUtpjVFED6xubzazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی برای خود یادگیری را شیرین کنیم
(دادم همه رو هرمس با gemini 3.5 نوشت چون هم یادم میره چی رو تا کجا دیدم و هم همه‌اش هی چک میکنم که چقدر ازش مونده و الان درصد دارم و اعصابم آرومه)</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4158" target="_blank">📅 15:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4157">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">می‌خواستم ویدئوی هرمس رو ضبط کنم اما انقدر برق نوسان داره و هی سه راه قطع میشه کلا برقش، اعصابم داغون شد. می‌ذارم یه کم برق بهتر شد میگیرمش آموزش رو</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4157" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4156">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">همین الان ویدئوی یاشار عزیز رو دیدم، و باید بگم دیدگاه فوق‌العاده‌ای میده به شما از ai
اینکه دیدم یه سینیور چطوری بدون گارد و با آگاهی و مطالعه‌ی کامل از ai استفاده می‌کنه توی حوزه‌ی خودش، واقعا لذت‌بخش بود.
نکته همینجاست
با این ai عزیز دل، حتی باید بیشتر از قبل مطالعه کنید و دانشتون رو بیشتر کنید تا برتری داشته باشید نسبت به رقبا. و قوه‌ی حل مسئله‌تون رو تقویت کنید و کارهای تکراری یا سنگین رو، به راحتی بسپرید بهش. اگر به مبحث باگ بانتی هم علاقه ندارید، ۱۵ دقیقه‌ی اولش رو ببینید حتما
https://youtu.be/-Rt_Z0allhM</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4156" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4155">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید  لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4155" target="_blank">📅 13:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4154">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R7Z74pfsNSBBA7nmu2lKpsCQGlCi2LcZwjAGsvR-V2qJKWSQ0B0SgT4q_p7qmgSkYzpDqYyQdWM2JbZ4GuHOESEuvArJWPf9O8J4vINZiUzfjZcDEhQaLdio5PfMPdNTMmKb79oTJjeiBFbrZ75cqzl8Qg8BcjvBUmmARWhA9vM-k_ssJSOwL7sYkF1af4VsxEPgvCGSrtpsZvQgaXrjVjzid5TOsIJ2wUqRmpxxaqmrhQjoV7Ofa0LHvmZWj8rFhDx8he4IebTq4uTCSPTqJBIYsfsleMzjOybttZIRMCu0ufj1cmgq7oHrhJC9U5MxAeq_CU916jF0n63zw0HNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید
لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4154" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4153">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FtLUE1Nq4QxdimBGXmbRyWwg9UM9hYbHL8XiO45T-qIEwBFV4wQIJY5nIC-DIMa9k8_EotHP77leP-Gy2BckUtqaBNiAPOyL8wvoy5Deu4to1LeOR0tmC5K5flAp9l93fXzpBzZvxIluT4Y30MFGUE2r1cY4RZ7iclzGI8G5QkG1M4vZeKGcTGlG4U6ZIpvsaG5w1LNcGyGCxSaXM7iEaWEFwDWZOhN_RqlajrO-KANNRm54FzMYo9EpPSLn3DxtY2afx5RauB6rZG07okV5DxjILPHHGbhMqnkWDhcpmlJXNzyfzKoTSFPyDL6bkZmGJj7YEMbYqt4r2QCG48bT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غول چینی، GLM 5.2
همچنان ارزونتر از حتی Sonnet 5</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4153" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4152">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خب گویا کلاد Fable 5 امروز برمیگرده
😁
آنتروپیک گفتش که با دولت آمریکا مذاکره کردیم و امروز مجددا مدل رو آنلاین می‌کنیم</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4152" target="_blank">📅 10:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4151">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dpwevERZrKLD1GKqQ3cN5jTUG0S0E8tUS6fhZRl0hVVILti5856usxE79VXsFkiilcbfhMXByH-8i3HQtW3TSaFovf3hym5-FcAnUgvqT3lrhATGPSYFp-NlJzzRCJfFUbew6wi099c4k6SQRHkktdaK2V9TjAKAhuFXER23lXH4mJMJ8urRd55xCdCPSe4N992wIWoHL_JD0_Su7hZqachlb_fDeXf3ij5zFVvRtBNDdLStfA4HKWsTX-OGrAfo8RJ2vSWG5mt_p6A4g4vlDOCk4b4nyMYj2iCo393lSLC_M4Rms56XSHB1KkrVbIeKlCeAGYFiYvFpQXvpu8wgEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4151" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4150">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4150" target="_blank">📅 01:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4149">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=JgnhdFiIX7MNdspciBzjq9IDmoI-q8FN8Cy4W-WKKWBEPu6pXtozDeYutSs1UvW2zvmLQebiNFGa5zLptqo_XnxFcBRfwKryuu4L8J8AZvqNIOjlLA9Z_VYVm5YWTuczJfHRiU79GoTeE0eSFJL0CkHG1qqW263QWIz9Q82pEabvAiTGR-Hzk6JudbxnWzjkXseQD298X74ztMhgbvtfnykwrT3jTmv5LhTGYnA9OEZfJEOj5wiuvcSG8yJopVRw6M3xJ0uYKYLZ8zENnworX16dAHhp0GkObbBqvzbI0WN9h16f7gUiW9U7s4CFkJgn6eNljKpFM5L5BN22ShKWlg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=JgnhdFiIX7MNdspciBzjq9IDmoI-q8FN8Cy4W-WKKWBEPu6pXtozDeYutSs1UvW2zvmLQebiNFGa5zLptqo_XnxFcBRfwKryuu4L8J8AZvqNIOjlLA9Z_VYVm5YWTuczJfHRiU79GoTeE0eSFJL0CkHG1qqW263QWIz9Q82pEabvAiTGR-Hzk6JudbxnWzjkXseQD298X74ztMhgbvtfnykwrT3jTmv5LhTGYnA9OEZfJEOj5wiuvcSG8yJopVRw6M3xJ0uYKYLZ8zENnworX16dAHhp0GkObbBqvzbI0WN9h16f7gUiW9U7s4CFkJgn6eNljKpFM5L5BN22ShKWlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Anthropic از Claude Science رونمایی کرده که به صورت اختصاصی برای مراحل مختلف کارهای پژوهشی و علمی طراحی شده.
توی این نسخه محقق‌ها می‌تونن کدهایی که مدل می‌نویسه (Artifacts) رو به طور دقیق ردیابی کنن، محیط‌های اجرای کد رو بر اساس نیازشون همون‌جا بسازن، و جالب‌تر از همه، بیشتر از ۶۰ تا دیتابیس معتبر علمی رو مستقیم به کلود متصل کنن تا تحلیل‌ها روی داده‌های واقعیِ علمی انجام بشه. این نسخه فعلا تو حالت بتا در دسترسه.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4149" target="_blank">📅 01:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4148">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9603918fce.mp4?token=msnUV5rwqai9rbZKM0XmDgMOQ9CscBeme7Vw-EDTvQXDUgd0gWr5tl2aivZuD2fznjKJiVgGplzrNeNa0hgJDpieADMaOFI2AclS3OMajesOT_MN1b7JhGt1JitP8LB-Kr0g_ytzJrJ7P1QaBHrLJ9LZdOFB8GsnfIfLnwlI82tSu0HhlciEiyxn2X6cXmmPQ8i0KMGRXpI2WCGnjpZftUCiOlkWtQCIkx7HxmqjDsLYno4ylEjvGGXXUXlG8NjB0j1loh0NXSLzed_oIpx1F9CQohZmO24RPMJsnvoiCadmTtKeem--G7KdkfN__u0aFc5voE_QcnWOKHHSmfAt8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9603918fce.mp4?token=msnUV5rwqai9rbZKM0XmDgMOQ9CscBeme7Vw-EDTvQXDUgd0gWr5tl2aivZuD2fznjKJiVgGplzrNeNa0hgJDpieADMaOFI2AclS3OMajesOT_MN1b7JhGt1JitP8LB-Kr0g_ytzJrJ7P1QaBHrLJ9LZdOFB8GsnfIfLnwlI82tSu0HhlciEiyxn2X6cXmmPQ8i0KMGRXpI2WCGnjpZftUCiOlkWtQCIkx7HxmqjDsLYno4ylEjvGGXXUXlG8NjB0j1loh0NXSLzed_oIpx1F9CQohZmO24RPMJsnvoiCadmTtKeem--G7KdkfN__u0aFc5voE_QcnWOKHHSmfAt8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسخه جدید Hermes Agent سرعت خوندن صفحات وب رو ۶۰ برابر بیشتر و هزینه مصرف توکن رو ۴۹ برابر کمتر کرده.
تیم توسعه‌دهنده‌اش، Nous Research،  با حذف پردازش‌های میانی کاری کردن که دیتای تمیز مستقیماً از بک‌اند به ایجنت برسه. همچنین برای صفحات طولانی و سنگین، داکیومنت‌ها اول روی سیستم کاربر ذخیره میشن و ایجنت به صورت صفحه‌بندی‌شده و فقط در صورت نیاز اطلاعات رو می‌خونه.
این تغییر یعنی کیفیت تحلیل و پردازش هیچ افتی نمی‌کنه، اما زمان و هزینه‌ای که بابتش صرف میشه به شکل چشم‌گیری کاهش پیدا کرده. و یکی از نقاط ضعفش یعنی مصرف زیاد توکن رو پوشش میده!
کم کم تیم Hermes داره یکی یکی مشکلات محصولش رو برطرف می‌کنه و امیدوارم همین شکلی جلو بره
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4148" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4147">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h5nQWT3cYhIZqdlE5OJWT_2nkW0Aqw-T11unkCSmbBMvH1WoLuVpwfwxjKTl36rzJsiHhxuI6ExH_HJxOT7stdPki1hKVwKToVZmLBcOyXkfrvgpuMfX-_4qw-zeD62-hLVT-QLmFfoN2fPDsy_9DOEonjsXc-KtXUtIq4HPNdSEFQVDQcGibAQXMBpmnxOsDdEyDmnVjrx4okbP05zCMwtLhjSxaNSzTTrSSFmqq-d-OG5x5R9kH_gnseCiKtq89d8lAgYSXUtGAfZgNN5Fqik3EoC3f3XJD35IFPSY-HET5hgRsiYu1h1L5PucuGlUfAsinhr6ALkUx-zl0QC1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک منتشر شده توسط خود کلاد</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4147" target="_blank">📅 23:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4146">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HGKedvYJstP-n9DRyZIJ8imATemw979I3MhUKc5LSdN1IrOJHJHvGfGtV9ffRTh1d2qg-IVC5iOLjkyF7zTkEWhoOlSG_Ytiy7sA1BtS9tYR-GkTB429R2YT3CKqpuLiLUHBihTax-P1p4jis1TnGB95-kc06QIoeGjJolA-aaeZPTMN475LVjX_rcZm5F4AzKVhJ7mAYqtw_Am-0in7Jr1-IVE0O02oYMlorBEwrKnluMQzxxL4RjH49ZTlX2MiWVA-xYlmB-x2QWUPuYo4iddzu6g4UExwWOycqoF5wzeV5-XQ6zX5Kmad8G7yngS9MVUc5bJUW_ilr19TMHGMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌ آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4146" target="_blank">📅 23:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4145">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XJprUHjk-jtJ3MiLtY1RoZLJIj5fY6Z80CaT40GwBlJynuA6Ua5PL3vVVtz9Nkhhmc0ha60MZR2vpsqryG8Qkd8jMJrFS84EaIkuwTAbsLRJ_b2B3aK6GfgcTjX7oUFOTbLSBwrEVj7QfgBIAEfh_uJwN1Y4gUbJBft65zOQdNcgWB7uNyM6WXA9U879QCdAx_oVy4Lv3yMP3RKVkXnaaLeMm6_eviyn9uUIgM19vkGi1M2y7vA_bfhw6zfFw--JvKQoYy40GoE5_dCHSS_xJA2xzyjo98koI4SjvBReags1BF-WnOjmcsDReEC6_7r0se2z12Sl4fnlgfs6Zte7gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌
آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4145" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4144">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!  این ویدیو…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4144" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4143">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!
این ویدیو دقیقاً به شما یاد میده که:
✅
چطور کاراکترهای ثابت و باکیفیت طراحی کنید.
✅
چطور با استفاده از AI سناریو و موزیک مخصوص کودک بسازید.
✅
چطور انیمیشن‌ها رو با صدای کاراکترها لیپ‌سینک (همگام‌سازی لب) کنید.
اگر به دنبال یک بیزینس مدل جدید و پولساز در حوزه هوش مصنوعی هستید، این آموزش گام‌به‌گام رو از دست ندید.
ویدیو با حجم 300 مگابایت اپلود شده , از طریق نسخه دسکتاپ تلگرام میتونید با حجم کمتر دانلود کنید.
〰️
〰️
〰️
〰️
〰️
〰️
در صورتی که مایل بودید میتونید از لینک زیر دونیت کنیدتا قسمت های بعدی و موضوعات بیشتری پوشش داده شود.
🌎
donate.isega.ro
〰️
〰️
〰️
〰️
〰️
〰️
📽
زیرنویس فارسی
🌐
ترجمه این ویدیو با وب‌سایت
isega.ro
انجام شده — حتماً سر بزن!
📌
برای دیدن قسمت‌های بعدی کانال رو دنبال کن:
📺
🌐
@AiSegaro
🚀
هر روز یک قدم نزدیک‌تر به آینده‌ای هوشمند!
📤
بازنشر آزاد با</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4143" target="_blank">📅 21:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4142">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sJCtm93oRm2L8_0ZMscuv686Vwu1Or0N-9hf1ihDbYSxhQxK7iyaS9mfTSHE0LtsIiUaSZZd2pn3naFTeu8AsDneD2ZoEpCSRq3hPgvSEtxKt7Ms7oETvh-P-qZdh1zlwUpkI-70KTvBBKcUmU56h7Gvyh8O92Lliqh42HhZcOPgXqNClpraLKDAt0lQSJa0JMYFZ90lwohll73GQSadympc3CBAl0nWdNGNLyydUI-wULD38uGbpMuIaghP2WwSTwXfh7_S2ffES2fYw5_ZSi1LA8ySGFp9opsn2bZXJCctgOad1vCJv8rW12AIHHaOLTEPvjnpB24KP_Q1b0oUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب یه قابلیتی آورده به اسم Ask پایین ویدئوها، که می‌تونید وسط ویدئو اگر جاییش رو متوجه نشدید از جمنای بپرسید
🎨
فعلا برای وب فعاله گویا</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4142" target="_blank">📅 21:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4140">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4140" target="_blank">📅 18:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4139">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4139" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4138">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انقدر برق رفت و اومد و نوسان داره روی محافظ میترسم لپ تاپ و همه چی بسوزه آخرش. آقا بیا قطع کن همون دو ساعتو، نخواستیم</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4138" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4137">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بیشترین درخواست توی یوتوب و توییتر ازم این بود که آروم تر صحبت کنم
😁
من فقط نمی‌خوام حوصله‌تون سر بره یا وقتتونو الکی بگیرم
اما از ویدئو بعدی سعی می‌کنم شمرده شمرده تر صحبت کنم</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4137" target="_blank">📅 14:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4136">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hvBvHeaWJJeUc90IFxTAS8-cPV0Uvz6A-90wka4InU7LwzQsX7GO3iPYevt3CJFi4ddvv4ANWSpK7z8_IGSK6Sab20DxcseMBeo5w-uWE7ELzpQJJMfHc6bnq0TmS7cN60X6_qU3U4SEd8wVnVqzXkLT3CyCmykJCjZ7kVQcFvD1p9954uAiPJD9cQim3re0-i9WI-fmD56CCIyUMkxg5fvHc6iI7lpCGbXZfV32Z3muM5GkbzClY-HgX9gx0A281kJg-ZCn8l8Nv0i6R2Q20Ph7VOLudxjRWPmkoLs2cfIIJ2Z3pEdOOdI4TZf7yl2PxW155CwBu2yBH1DRuk477Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد نسخه‌ی موبایل Hermes، من توی ساب‌ردیتش دیدم که یکی واسش نسخه اندروید ساخته و Pull Request زده روی گیتهاب(که کدش ادغام بشه) منتها هنوز، رسمی منتشر نشده</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4136" target="_blank">📅 14:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4135">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4135" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4132">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/adFhrmF4hOYfdkwdi6XcW7fQmw6tkXbnt06y3VBNm8vKMstsyQvL6t5JkP-CdKa9vtBt-v3jHvLZwYqcORStrs_b3cJKh6dE4amBkP--eSed6Kh5qrE3AZt58bGnw_trs4mjaHMO7MhLfw4z7dIey7RvDZ2UnMup3FHF-RNDT8pXK4_NfsONWqDEbJ1DpGAKhTn4XFRRczuQaZ9izzwWiz-Vxo6ELeSLGViVMgVMj4nvf2EgBfWY8hRDqRSuaPN9vKuXXpJiAv3J1o-urpM_4CsRaEdlcsRHvpTSQ9xhwib-vW6TvXBXS5UA2mhemErAhEfUiXDgH7zb3slut1ufwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gIITl_IRCqXW21zDGAzw0g2Rd4AFjEAL2ImOvIJmG4w-gEGEQswOYQjaNfs4WNb4HNk55AwTxR2E2tgxrICytkUegOpS9tmyRfxSHm1z_9finfMS5hip60KaIUXw3EyTSv9ffr-mAyWfV0ITIvSSSXpEzKtoq9T6Olj1ikcfWjpCNRVuLv0E_9G5mAeV01PWWIECqRq5qb7pKjZz7uIvGtVhjzOlDqgQ38rVawCnZ-yD9T3_lB0ijAQ-v7fCvRaC6_HuKIOkEEzyDDY407jL-lfxYdknhcsHBrM2UlQK-f0JcvXyeOSHCjfDTyyV1YeTvUx6zPO3joAVUmjmtojLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u6N0NWQFzQHUz2uVrhkcJGxknMEr04a9x0gLVGBUKy8r9mpmbbCFMkzPkzHa21XUsE_nS2rhnD-y8--SIXXMdj0gWCSbN9nBOnrM2Qqbo5YJaWnkB3pdDtq1pDirqbps6O_oFcUlpjh-exoJjMg_Y_6G1gA39IS3oPzdEY7n0iJENd6_hRbFABaxKbem9FsS82I7Xnfxua-PQlnhGaOv97-VBp0kWA2ZOZyLA0MeYZJ-yCxsKydbHmEiqlb3u6srxPjisQE2IuhFlPr3-oanMznBaPtP04mwzsmOmTEyqKGLjwlqooyTT2MSzCKuUJq19uDDULqOrD2ufMi03DJH6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واقعا Hermes و وصل کردنش روی تلگرام، یه چیز دیگه‌ست!
فقط کافیه ازش بخوای، و بوم
انجام شده. ویدئوی بعدی، هرمس هست
👀</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4132" target="_blank">📅 13:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4131">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4131" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4130">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAZYSC72OQKJOhCK4EBcAdioUEvB9OI-Oyflh9pValOvCuwoL4s66CuHTJDrBcsu8Ifu9pAGHO9Sb4pQwxZ8dmCFUk7iV9IZa7ewHARbr1uzISXgzzxnB6jmgAJQ-32keALndrcWgM1Xe65RMBui3G7qFX0E271Sbgsfg20RwNFrmNnyD5dVk1UlTd9llZI8yWnmR4SCzkwk6D8sIBfO132HAxpKilDu4dU4fjNGPtu2ZAaVCGWyjQdOy3E-ZxpCfS5YVxHX_j-I1LzCCT6j0kn-Qnn7HmhELRMQAMpa4BS7VLttOItK-xzWVSKbR--lHuJUjamIAyFIPhbKStAxVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اسکنر WhiteDNS
اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ
مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3desktop
📱
نسخه اندروید
سبک، بهینه‌شده برای موبایل و قابل استفاده روی گوشی، با امکانات کاربردی نسخه دسکتاپ.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3
⛏
قابلیت‌ها:
• لیست آماده از ASNهای ایران و ASNهای معروف داخل اپ
• امکان وارد کردن لیست آی‌پی دلخواه
• Health Check برای توقف خودکار اسکن در زمان ناپایداری اینترنت و ادامه بعد از پایدار شدن اتصال
• ادیت یک کانفیگ و ساخت تعداد زیادی کانفیگ روی آی‌پی‌های تمیز با چند کلیک
• استخراج آی‌پی از داخل کانفیگ‌ها
• تست سرعت دانلود و آپلود آی‌پی‌های اسکن‌شده
• انتخاب پورت از لیست آماده یا وارد کردن پورت دلخواه
• لاگ پیشرفته برای بررسی لحظه‌ای روند اسکن
• خروجی کامل و دقیق از نتایج اسکن
متدهای اسکن:
⭐️
IP Scan
برای پیدا کردن آی‌پی‌های تمیز از دیتاسنترهای داخلی و خارجی و استفاده در کانفیگ‌ها.
⭐️
HTTP Scan
برای پیدا کردن آی‌پی‌هایی که امکان استفاده به عنوان پروکسی HTTP رو دارن.
⭐️
SOCKS5 Scan
برای شناسایی آی‌پی‌هایی که می‌تونن به عنوان پروکسی SOCKS5 استفاده بشن.
⭐️
SNI Scanner
برای اسکن دامنه‌های موردنظر روی لیست آی‌پی‌ها و پیدا کردن آی‌پی‌های مناسب برای SNI Spoofing.
⭐️
Speed Test
برای تست سرعت دانلود، آپلود و Packet Loss آی‌پی‌های اسکن‌شده، همراه با رتبه‌بندی خودکار.
این ابزار برای کاربرهایی ساخته شده که می‌خوان با دقت بیشتری آی‌پی‌ها رو بررسی کنن، خروجی تمیزتر بگیرن و زمان کمتری برای تست دستی تلف کنن.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4130" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4129">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5950435463.webm?token=f4kIcIUIODU41ovUCME5OEZFEaB3_X8PkwNdhxq-PiFCGhZkuGbK6KoPI1UkFQoKhK33t3ykQSn0Ak3l3uyQHYVRfFb0viALPRC8noKFABP0MtFc1GKVXiYSldtq8S2Y_7Sccp5wBCq4HBQMv9xi5nvy0gK9NZwfKyfWRTfFw33FLyzo_yQeS4p3BBAi8KR9FovgNtM6V4vbebDR4QrWt6Oy4fdubNqsZYuBQbfbSV2_rRoiW_upIN34IAC9E2oaYiKcZDUe7lTM9XfMkz6SWoBrMYHQt-VQPrJly5ipm6LG-Et2wPdXysVrAt2b4HRPVglAONI6ml_NhMUek6-sSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5950435463.webm?token=f4kIcIUIODU41ovUCME5OEZFEaB3_X8PkwNdhxq-PiFCGhZkuGbK6KoPI1UkFQoKhK33t3ykQSn0Ak3l3uyQHYVRfFb0viALPRC8noKFABP0MtFc1GKVXiYSldtq8S2Y_7Sccp5wBCq4HBQMv9xi5nvy0gK9NZwfKyfWRTfFw33FLyzo_yQeS4p3BBAi8KR9FovgNtM6V4vbebDR4QrWt6Oy4fdubNqsZYuBQbfbSV2_rRoiW_upIN34IAC9E2oaYiKcZDUe7lTM9XfMkz6SWoBrMYHQt-VQPrJly5ipm6LG-Et2wPdXysVrAt2b4HRPVglAONI6ml_NhMUek6-sSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4129" target="_blank">📅 04:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4128">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4128" target="_blank">📅 03:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4127">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N7UJafQKYIznGctpY9gv5XNFYsrTnfUGxG4DugiBLui8I-g9OWjI5iCiE1EGVVoLI5IPHIgcUI895yITMS1difEuW7C1D9IfjFBT7sJ7ssfHbIJf-NCO0yczM47DaPHK-EtTL4YIydDFvg3hvxzC8SZZJn8iZzscjuGTP5c50247RevnWLMDikWbJ2pPR0MsnLoXew4tIUyjLeD63mregecJ-Wcpz6yE9ZE_gAe7VlVsJdYdVd0CMOu1YQUHAyjnrq2OTDReIXzkS-aJXt5W_LFgHDvV9jIiEUdaEz66O8L5cjFpACl62rTnzIBgRIiXDLcNX-3q5G4lqzEDWDosqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router:
https://9router.com/
⭐️
توی این ویدئو:
1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم
2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم
3- کلی API رایگان وصل می‌کنیم بهش
3.5- اگر تیک آبی توییتر داریم، به راحتی از گروک 4 و اگر جمنای پرو داریم، از AntiGravity استفاده می‌کنیم
4- از امکانات 9Router مثل Combo استفاده می‌کنیم و چندین هوش مصنوعی رو توی یه مدل فرضی کنار هم میاریم
5- به ChatBox و افزونه Cline وصلش می‌کنیم که هم بتونیم عادی چت کنیم، هم بتونیم کد بزنیم باهاش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگان و ساده‌ست و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4127" target="_blank">📅 03:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4126">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وسط ویدئو متوجه شدم اگر کانکشنتون با api ها خصوصا جمنای قطع میشه هی، می‌تونه مشکل از proxy-ip یا آیپی تمیزتون باشه
گفتم این نکته رو بهتون بگم</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4126" target="_blank">📅 01:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4125">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کمی ویدئو API بیشتر طول میکشه تا آماده بشه
صفر تا صد تمام API های هوش مصنوعی رو میگم بهتون
محتوا رو فدای سرعت نمی‌کنیـم
🥰</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4125" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4120">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⭐
نسخه جدید WhiteDNS VPN 0.0.8 منتشر شد
میدونم آپدیت کردن این سرعت یکم برای هم شما هم من سخته. اما تونستم دقیق مورد رو پیدا کنم و فیکسش کن
ی
م.
ممنون از تمام دوستانی که نسخه‌های قبلی رو تست کردند و مشکلات رو گزارش دادند.
⛏
در این نسخه، مشکل لود شدن بعضی سرویس‌ها مثل یوتیوب و اینستاگرام برطرف شده و اتصال‌ها پایدارتر شده‌اند.
✍️
از همه شما بابت اختلال‌ها و مشکلاتی که در اتصال داشتیم صمیمانه عذرخواهی می‌کنیم. ممنون که همراه ما هستید و با گزارش‌هاتون کمک می‌کنید WhiteDNS بهتر بشه.
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4120" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4119">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اگر نمی‌خواید این بلا سرتون بیاد و کس دیگه‌ای بفهمه ای ایران هستید از وی‌پی‌ان‌تون، از نسخه‌ی جدید WhiteDNS استفاده کنید</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4119" target="_blank">📅 18:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4118">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ولی GLM 5.2 واقعا عجیبه. قیمتش روی api تقریبا ۴-۵ برابر از Opus 4.8 کمتره
این چینیا چیکار کردن با آنتروپیک، خدا میدونه</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4118" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4117">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:  1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید: https://grok.com
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4117" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4116">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تمام سعیم رو می‌کنم که سری ویدئوهای AI، برای همه‌ی مردم مناسب باشه. تنها خواهشی که ازتون دارم اینه که نترسید، وقت بذارید، و ویدئوها رو ببینید و کار با این ابزارهای جدید رو یاد بگیرید
🥳
خیلیا که کمی از این فضا دور بودن، فکر  ما داریم راجب چه چیز خفنی حرف می‌زنیم و ...
در صورتی که شاید تفاوت درک و دانش ما از این زمینه با شما، صرفا دو سه روز کلنجار رفتن با ابزارهای مختلف باشه! همین.
به محض اینکه کم‌خوابی ۳۰-۴۰ ساعته‌م جبران شد ویدئو رو واستون ضبط می‌کنم
🤲</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4116" target="_blank">📅 11:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4115">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YA_vyIbP99dA9pDQCzeYtib5DKyADKnol9OsOrne2dDohpQq6V81Peuieqjkm4t_BtnFypAhchBZaslNIy8THCm9wGSESsvSprPkzCV8liO2g83poD9dVt92z8LyWdjTE4NAz36DxX6yoHuUS2_gdOQPl-wyxdRn5w1KOX19eP4o1BQKriASeonF5vXgIqaY5ZDrCBe6myBzdcDb3NsD6CeNAZTmOSFog1dM3vGucgujsCa306rGQRP54U2jOQ4IqDIRzgYZ1ytjWRY9FVwpuex6ZESh_aBL3pU0rmoYP801RkFhJc--_dZ5Po6igukCCLDSyWQIJABoporNhHOijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB  ۱۰۰ دلار میده باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4115" target="_blank">📅 11:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4112">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nayWjV2EWN0sToasYfH0MxHUGvZXdNzrZM6I-wJizFLwmo-oQC9wvKYHiLPOkXMYxczn3DoO9lRSMppmdbQa6mI07-Mbogz-1KNiRTuViWvtpmJMdhLrtRpZekxdznfwOHvOxh4TCMg6Q91RNLx5wAYAjqz6n4-MRNR5sqA54jlU3xiJvU7A5JsdZC42OBHpj-6F8VdkQxcmWkPA_qk4l755TImZAVWlxz7A8dHTDmplYXrYjXuUl0o4YaODcjuGtaHqyW8engCHjjN0E1PhZXDkgkURO3Kv81EC9TmncDC7DoUqvjw4SFQorem0BEZ1xbidQ3EOrfMY_7MZGiz2Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nGztyc-DqfBvWkAR74IJVAOAxbK59byV5UZfWPmGq9LHRz2MHX7XrpfwTkrSX7mAo8NozLvb4XLObSBVLH3OPB4EN_ee6haHQZNPtyluK_jAWhBHzJPN_yMbMH1gcbEDshPxAwZJFL-vD7Z8ztr1aGf2pTcBzR2-CiwaY60N3K1xExxHJmcN_dJKrSjPOHosy_wPbtGwT4cGIsKzc1SiBaTboLiLhuTyRAa3PIiNqocy_PYYjFntoeRbhat1Ax6lL1su_ba8sQ3G17O9mFq5LOkybtzn_aS5A26J4sZ1H-wprlHTElrGI8aM4T9h6VaPMJ__RtGUcu_4FOM0KPnFEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gC6dzVAcNwLaklUZsLG1WsnrvSbQqnHxyT75Z0nBX2TwegTsoqH433UaFOw8OgY4xE48Cma_PfHXHydyQt8Y2PESAh97E9LyCA9JksY8Uvrt7CXpMFjCq_wMF7okDou6a9UyshiZrTWfyl3u7Rr4vKxbuU8Kf6l89vSVo7uNo_uvckMUk6wq0oD3lr1g9uwp2H5fQVAZ7jmqmuZ4JVQAtFR74UdcKBys-CT-QaO1jeQtpNkMK44XBAtRxJV9gHvJCulhR2-ad9wr5MIzSB-0ebVusXKO2U9Bzqz3hWrhWlE05S9EzsYyVwE-gTIKB_5bHZ3xDhGIHZnk-QX7OdGF_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی واقعا داره پول میده به یوتوب که ایرانیا رو به دین مسیحیت دعوت کنه
این تیکه هم از یه فیلم بود. دوبله فارسی
😂
😂
وبسایتشون هم بامزه بود
https://daneh.online/four-spiritual-laws/</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4112" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4110">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k_pYwZE3Q_OluVQMlljHIb8_7BlZeLZSAEup39d7b5g1-5fPZiSBawI1TUz6uT3oamoeAiRdnl1Eg4q5Yydp1ZC57td5JNtMg0WBH_EmOHqRNofKpIzmpRfmlrx9qsf9D4_KOBkkvFyy2MWOW-eUJ29QnaKD2ETyNSo8z1UIBnPdR52H9JsIOoYHnY9Ldd8PGsfLZGZMztThko34bCK5zBAs0-ex0Nxsn0XzhkXSkqwguGlzgpMnLEjuGmywBpKVvfrJsaabJXuUkU_GAGtt_3TFa4fukhShxtbGEJ02itXlic-vx2DkUzRLrVGsp_lSTbttbB9TfKO9nkS4gQk0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N-7N5wiDOEPJ0eUmCbZy35vQaqH0LddQX0xE_GFjZfXAN-kMUMRotHH5XBx4XgNRGF1fyj2PdbW9fuSUZ7wUCXjqe4d70BQQwY9d9Yve9W1ERr7zSlsMJWl9sW1oEtYmUx1hrdBf4b9i1HS6OE8Obw-xr580_Y11rLZlW73SpLnACXSzNK9vgxTl-hCQH0-0bmhuUNbVqEJf5fBqG5KsiizEhsVJiKzvSL_9lSPPgMWEkih8rMcTDyzknPA6lGNzZINGqls3-SAh7VkMK46auBRBFe-Sxt9JFHQhSNPRIezqVjYuE6sAdBNBde48T8F3-fv1RuEU2k5fxF8RvZBRNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:)) همه‌ی اینا برای یه تسک ساده. بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو 10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4110" target="_blank">📅 04:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4108">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ddDd11XtiXgldRWJNOtkk9ga-yHarc5Kez2HHedhLiZZy9G-9gBgwXJvdQexwaXjZFLEOO2RfdVsIChudyccZIs_guy3KCh2aq_IEmPjHks9grlPha69PWEC3KKSTxYWcjDMtqvp4-sXQI4zjrtStpTxh0rnt1pmjE3_t0A_xe9YtV8kmrbvRuI45RtwEtZ2RRB_VOksNEDiXUqbNJ8opmdKAePdaCWRcXRyrffY7IwyNjCJOyh9W3qphtcwjeBdF_qKwZjLOAB3tsm9bg897wcd-b8ZQTDTYYtGg7WI6y-JzZgGwkifdJZFaKR8zdyRGsLJVI4PCQIM1dF7YtPfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bcxHaZfmT04M_3zOF0ZSUHbPOtb0vAmj_mP8dPhFc-xXYaP57LrRxqevkzwe7n_DWIGAPd2dn3QR3Pg-Da4pi9BqCfh19IWDgXFTiewwtTd7456AmIrmzbYcVFn1Fdj1quhARowBbzIgLJDWVre_7_yKoJJ3J4ngbucalbbbD0IfDT8BfrfpeSbtLJAWoRI-Rr3i2jd567D7ua6T4ZsA8HQ3vimOGHqmWRlga6vNkBkV1iVJv9F3xUCeYIoHd6tgJbDYO53YKX2seUFyhGAbcAUGxD2CEPHKiDNsu7IDdV9de9vPj4MVut4KdPNphhAk3CCRZPegubplNJbe-Kdo8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:))
همه‌ی اینا برای یه تسک ساده.
بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو
10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی اسپویل طبیعتا)</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4108" target="_blank">📅 04:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4107">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از aistudio.google.com هم می‌تونید بگیرید که…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4107" target="_blank">📅 03:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4106">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از
aistudio.google.com
هم می‌تونید بگیرید که بسیار راحته و توی ویدئو بهتون یاد میدم. در کنار یه سری api و چیز میز دیگه</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4106" target="_blank">📅 03:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4105">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رفقا اگر می‌خواید از نسخه‌ی دسکتاپ Hermes استفاده کنید، به نظرم یه دور Hermes رو با Keep Data حذف کنید و بعد، از اینستالر Desktop استفاده کنید. چون من دو بار روی دوتا سیستم مختلف تست کردم و اگر اول CLI نصب می‌شد، بعدا با Hermes Desktop میخواستم نسخه‌ی دسکتاپ رو بگیرم، به باگ‌های به شدت عجیب غریبی می‌خوردم و یه سری از بخش ها کلا به درستی نصب نشده بود. الان که دانلود کردم از
https://hermes-agent.nousresearch.com/
اینجا، اوکی شد</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4105" target="_blank">📅 01:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4104">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کار خفنی که پدرام امروز کرد این بودش که جلوی دی‌ان‌اس لیک رو گرفت کلا توی اپ WhiteDNS
اگر وصل نمیشید به اپ، حتما از Fronting IP استفاده کنید.
من که با سرعت بالا وصلم</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4104" target="_blank">📅 22:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4103">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
سلام به همراه عزیز WhiteDNS
تغییرات جدیدی روی سرویس WhiteDNS VPN اعمال شده که از همین حالا در دسترس هستند:
✅
تمام کانکشن‌ها با دقت بالا از نظر DNS Leak بررسی و اعتبارسنجی می‌شوند.
✅
قوانین جدید پراکسی اضافه شده تا سایت‌های داخلی ایران به صورت مستقیم باز شوند و دیگر نیازی نباشد برای دسترسی به آن‌ها VPN را قطع کنید.
✅
تبلیغات از بسیاری از وب‌سایت‌ها حذف می‌شوند تا تجربه بهتری داشته باشید.
برای استفاده از این قابلیت‌ها نیازی به آپدیت اپلیکیشن نیست. کافی است یکی از کارهای زیر را انجام دهید:
• یک‌بار دیتای اپ WhiteDNS VPN را پاک کنید.
• یا اپلیکیشن را مجدداً نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا تنظیمات جدید به صورت خودکار از سرور دریافت شوند.
ممنون از همگی.
🙏
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4103" target="_blank">📅 22:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4102">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این 9router واقعا ۱۰۰-هیچ freellmapi رو میزنه. شاید کلا با همین بهتون آموزش دادم</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4102" target="_blank">📅 19:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4101">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یه گزینه هم داره به اسم disable ai
هرچی فیچر ai هست رو غیرفعال می‌کنه توی کل برنامه
اینم برای عزیزان دل مخالف ai
😂</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4101" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4096">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W3Yhxgj72YRh1RmG0ShB11ryO_D7oZBP7ZwUEk4N6k8Z1eHUYflFphPuGCJ8SvNaqDAtHuuLxg_3tS_i4zK7pIhlPzfezF03kK6PMe9WVk8QfcsR7VhiAmn3-TNcmqC0IVozrVbhCLfUTuispmEIy0aljsOWPl-1n8vqGMHsKS1dB5vCnntCVhptmEalNKH2jAx22Uys7p_1GAiYeszeNAnF7Qac6n3EsoBW5BQSwvtqRPSrUT0CwOA82ZM0O-9s3rWRU5kh8KplJecyB1lPWX9YJfXBjtyxkwHXBSsG6oB0BCPbOJba4kz_3tlN-gnHSKDNK5aWLz9mKmwa9lZznA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CVhrMfYhSAW6tnZ88VKM9TzkWqkRkfYxbI3ein_1Pp4jQNHG3KEm-ujX5oQ4Rfrf6_THzo6jwoiofwduAPEtYHyUdvqZeDAyw7J5tVf0XK7d7lV8J2CucX3bpzmKhu5CaJysExhxzC1BjdV9JjuxY7XM_Gj8lJws5_mkd43t1TtLIWFBPU71hTF0WSzavchjalnWR3Xe2xx36FUbVTIpKEBdnM0T5pxQkXKuS9qr9ZKqBN3MDCvOF8BGJZuj5gT8KKXKbiYIxFVDykSN52PKvSHCUx-Gldhqh_Nz0VkgW5SxCU9u8wfEbzG5YTWBVxhX00t2zZmFt4UKD6UBZ9Lipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AzhzQGWcXfDuSr9oeq7RxooEY3b44nDf3pCzacftI1yUda1kF6GGfuuxmgIqj-eIEA2Evkq-J7SmuPinI8CCwCLC5YstJZiSuHRjwhbXfX4BKrfc-plm-yAGvUt8TNZT1F2qfU3wTfyqkKQLG_2Okd5qx1m8d35gwo55_4eMfPnex0bdNvlUpMNPASiVSaZ334QyJ0i4NBHYRjCBb1aXNUOkscQlcGPGp7TeUdPXlWhWd-cEG019xoR4cJomj5mp362kPrhI5UoPFdPadxmEIQhua-qVlZX95Wf82HfdMzEvvlYDsbsw_-vwWL73TmV2Vi8hvLHzQ0gbUOBPRoHqrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z6feD_buw011PjhoSet1knE6_jlVQZ7ktm5bygOvXh1_aI2JUnTOtvPpkTWzkpnbSLuOju5F-WZpvv0VByQeXWBtxXxW1XZEVB9g-c-PENeDHx38_kWAJu_5Kb7_fAFQ4NrVJ8eTDkyhBUmm_QDALy9hn4ovX90Pth1CEOaMNebMaLAEoaJ-VAmnst0anH2G1np1jAM5wZrBFPVqyjZAyA2K_kvzyBmta7ekBmuQnHyB-9uNw4z9H5BwmkNBxXq034rvKsYJuTZ97LPaNzUc1X9ECXl_7S0PqIU8_hSFI0zkefbrqVpdZOQlpWhsHci3Xj_WeUjwsOtPka6xu_62OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Yyt2X4vgUEEEnv9c6iJjWHreUV1mWykSrk9FU3RAMNBS8KO1uPfthLM4oCTwQbMVakzYWBKcIs7aEu9toMtUwFnQsxn17z8aFw-82E7umNulfGdLO_XG-RskaFwrdLNWt3Gz8Rj--7MebqKknlTYswfCwHZaZO8vdce9A1J3dR-UkeAX16JZ8xkOm09XZ504QT6XUtwINw6pumD4D8OBuN8GBhz0kbrCJ4P73kLF_e8DRfMqih_NlaI8_px1Mp5eRQVKvuNBjbqAz8e5wyWcMeYA6diuZ9grytwqmqJOLa7eUGmDFr9qwUGmlXr5BardsAk8szxilD3SSgiRKARUuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4096" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4095">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-poll">
<h4>📊 بچه‌ها آیا نیازه من یه ویدئوی کوچولو بگیرم واسه‌ی طرز استفاده از همه‌ی این ‌apiها؟</h4>
<ul>
<li>✓ آره. بلد نیستم👍</li>
<li>✓ نه نیازی نیست. بلدم👎</li>
<li>✓ رهگذرم. دیدن نتایج👋</li>
</ul>
</div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.   خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم  در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4095" target="_blank">📅 15:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4093">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sRR_ncbqthMsJaKWIdq3ZjU9uF4N9_tyy8ju1V03tSZkaY7dyRvl9faq9P-h6jBlFky3aUfAmBOMSUg0OiEd8zS37xPdhseAowUkCPCOYfXfx4cr6n38A7Xuz-Y9tqpkfDYlPA40dwtksONhJGp7Kz4uBgDsXwVxSDn0-u6UkWvBpZET_I78XYqwh2pX2QcL0kz-SEmUYTslofHGnl1qLpvJ93Wo9r-HmWjijJkr2XAp9QBOpmXuAJ3Daeqak5oKKM2aHTyXKs8-nhw2as5fuOx163PXi4CyiXtXrpcu-Nufsg3bx9rnmnivq7dxU67S5kSOXS023l0zQ9xgUzCISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QIeOZaJxW8jaFkS7EK9_GuGGE0tH3lX6oRILI10wRxtwM6udVPtFGlGwX8FNdxRAZistqQdzGPjkD1dR8VG6GMSIt7iZTfdVkjqnh1gQS1aepjdShXCa-vQdCUIAznMNO8RFctgUsHSoHw8iDVA5Pm1wg5jTHFVsU-ZB2tw5r80MJtIwZcK0nhl74bY_jXSynZr_EnpenvDpBMZtcQjO96IFGxef8dYFh5bKpj_Kdt_yz23X6DVrsw5gYhpalcRvsqR0n-j1SsIXMmzDaGVdXnArcY2jyf1_TS9plLtOnSTgEx94rjcd8zCmCmq_U13WND-owpDSgIck8ERjB5axmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اونوقت واسه بوفه خوابگاه ما تو یه روز 30 نفر کارت به کارت میکردن حسابش مسدود میشد به خاطر تعداد تراکنش</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4093" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4092">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CheYc_PHCSG2h2EwLd5RSmF0uS-OgkqD82A6ocE11WumXP412KBIowCu80gbPb6EkdFyU2b3_uBXwdB7IWUlttgTvVimhmS3ocIVeEUUjtoeONRsa_jmK4WO2_Iglzd8udlbIzC1D3CVCAbmY3pGWmrfH_ROaPqc-y5aVtqQAwDY0Sy5X1itilmNb0OMM5VOx0ILBHbHQSYl_SuALL1rDnPGlj_hhkcYRmPzmyvp85-PtNhBBKilDv0abU6opnhUIrBaxY6JrPr99PWs90exog24kQ-z9FUbWwKA6yGYsBScTrBXDPtjv-MmxdlZjjQtHHCHr4QT58stZR4yzQti5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.
خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم
در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و یه رفرنس خوبی درست بشه
این لینکش، big pickle هم برام درستش کرد دستش درد نکنه:
https://ez-ai-access.yazdan.me/
✍️
Yazdan Fathali</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4092" target="_blank">📅 14:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4091">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به قول یکی از بچه‌ها انقدر api رایگان پیدا کردیم که حالا نمیدونیم باهاش چیکار کنیم
😂
چندتا نکته:
1- اصلا از api های رایگان روی پروژه‌های خصوصی یا حساستون استفاده نکنید
2- هیچ اطلاعات حساسی بهش ندید
3- توی env پروژه‌تون، api key یا... نذارید مخصوصا api پولی کلاد یا gpt یا چیزی
4- حواستون باشه که به جز شرکت‌های معتبر(مثل خود شیائومی که mimo رو رایگان میده یه مدت)، به هیچکدوم از بقیه‌ی سایت‌هایی که api رایگان میدن اعتبار و اعتمادی نیست</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4091" target="_blank">📅 14:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4090">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pxuKjjzgKtR4y-J2FJxdlMf3_sJyMsqslXTMC750OiIu_X0Je9Vb4EjMz6y0ps1itJIpSwpie5RgrAZ6_BACkcf7eEvI7eOfNrtewEfcCQ7wq_H_9MtOqVuONY2VuNscUu5TkJIdmpRj-ZPnaKQu-scrWnvvsEIy-OA8gMkVyU2FuBFvaRWT28_vq_CLKmizn_FAmi5t3t9a5jgh5Va1eyriKScROw6Z6dtC9TS0f0ZL5tf7iyG9NLQ7TYs59PebIHHcsnXvSfQdDvGIXUAz-9nRl5UMKgYklwq2xUWxMGO7giygVhE7Dp-yTwCSJ7YMIHKlzFMkjRVQ_y-LbcLMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت بامزه پیدا کردم تمام اخبار جهان رو با ai رصد میکنه. اوپن سورس هم هستش
خبرای ایران و آمریکا رو هم می‌زنه درجا وقتی موشک میزنن و اینها
این پروژه‌اش:
https://github.com/koala73/worldmonitor
اینم سایتش:
https://worldmonitor.app/</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4090" target="_blank">📅 13:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4089">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4089" target="_blank">📅 11:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4088">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LlzIlUdGX9lXsgIsM0gmXe7SgL0nd4tvlu5dFFOcAaHxqpf-RIPu2IFFBqyJv6YAsF9fgD-uKUfeIAzsctYLlBa76t6NUjMdysTm4Wn5TXC_n-itOjEfKEQsUPM5rPlsm7Hl1jjPuTwHrjU62TjCcecos81HGnqL3hgIatACvZeRaB5HR8HgIXYWutwMsCQCpNMUiuDUJ22rm7G_16ZwqthcDBa6hU0_OMvKfRSLnhbWm-nlZwmvErwKvneIkvte6nxxUWMaTHeZ5D5tTsPIznw1j7U-rBDdN15EnoqtBxoOvHO03gZiee8gfY7AT1u0cdMTJDd2-DxiPI1yPNhhew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم علت بن شدن دسته‌ای اکانت‌ها، چیز دیگه‌ای باشه. نه فارسی حرف زدن یا ایران و... .
به نظرم مشکل یا کارتی که باهاش پرداخت شده هست(که شاید کارت‌هایی که batch payment داشتن رو تشخیص داده و اکانت‌ها رو بن کرده)
یا اینکه علت دیگه‌ای داره. چون خود خارجی‌ها هم باهاش درگیرن توی ساب‌ردیت‌ها</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4088" target="_blank">📅 10:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4087">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پیشرفت ai واقعا گاهی اوقات ترسناک به نظر می‌رسه، اما من به شخصه باور دارم که نه جای متخصصینِ واقعی رو قراره بگیره، نه قراره اتفاق بدی برای زندگیمون بیفته(به جز افزایش قیمت رم
🤣
)
در کل، نباید نسبت بهش گارد گرفت. نباید هم نسبت بهش پذیرای 100 درصد بود که "آره ai خداست هرچی بگه درسته"
مخصوصا توی برنامه‌نویسی خیلی خیلی جنگ و دعوا هست و می‌بینم که کسایی که به خودشون میگن وایب کدر و کسایی که به خودشون نمی‌گن وایب کدر، هر روز توی سر و کله‌ی همدیگه می‌زنن. که خب صحبت طولانی‌ایه؛ اما
نه اونی که می‌گه نباید از ai زیاد استفاده بشه اشتباه می‌کنه
نه اونی که می‌گه کلا همه چیز رو باید سپرد دست ai
چون این دوتا دارن راجب دوتا شرایط و چیز کاملا متفاوت صحبت می‌کنن. و این وسط یه سری سؤتفاهم‌های بزرگی پیش اومده و هر دو دسته پیش همدیگه منفور شدن.
به نظرم با گذشت زمان، خودش درست میشه
بازار، خودشو پیش می‌بره و پیدا می‌کنه
و در نهایت، کار هر دو دسته هم مشخص میشه.
الان همگی توی قطار پیشرفت ai هستیم و صدای همدیگه رو نمی‌شنویم:) بهتره صبر کنیم ببینیم کجا می‌ایسته، یا لااقل سرعتش کمی کمتر می‌شه، اون زمان میشه بحث و استدلال کرد دقیق</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/4087" target="_blank">📅 01:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4085">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یادش به خیر یه زمانی مد شده بود می‌گفتن Prompt Engineering کنید قبل از اینکه با ai حرف بزنید و یه سریا دوره برگزار کردن کلی فروختن</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/4085" target="_blank">📅 00:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4084">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KfYxodIZUsLU1sNxDn2llEDEx3cJ8LWnQr7oV_iRwU_NybThV1XzyLxAFkZyINdFrucyMXozFiVkpyyWEOrYWzwMc-PNu_lEKvSPzXtk6CgPYoQSyGTUoAG2NmdHSCVnvRSmfG6pS5G4KvgSw4JR5ICT-7S1o0AYEU8secrP4hWD8MUnx_aPS5o6JmKkgqAcf4YJMYXiO8aBarSUQFvLr4sjSRNcRYMmT6XlxGynHRhn5WNDiqa-JtLRl0A--VByeIpIqd2Nvup1dX2-rgG6Knq0uaS0Dww-Yblm0dYWch46s6XvpWNEwwAPBujn7pArdYpB_iNby5EaM31jqbR9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید اعتراف کنم وقتایی که حوصله‌ام نمیشه یه ویدئوی یوتوب رو ببینم یا وقت ندارم، میدم
جمنای
واسم خلاصه‌اش کنه
👌
attention span در حال غرق شدن</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/4084" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4083">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:) ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/4083" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4080">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KWCDDVkZAhTg1-9iNLcSo-eudHGdp-Rk11z3FaUUFxN518nwWmhD2P3lDHE9wVBlM1tWwxvovthYCcHhzK2GcZnUn7knpVQWJWHSSuuBarpzWQZ_1sOCl3VR4Q0M56-iXgLHBi1Tzjb4xxN8pf63UMuMSn6OfvjYt8HFIRsGmBtJT6aSTu-fk0udk87U2Qq3euc3-dVthfDSjc9H8FaflbP7-kr7fP2M0RbNWfy1Hb15uNSxOVorZwyZGwSVOyGyI-0Nfc5lpe2k9l3SE1jyXDpLMeHje5be6Y0ILUv1hDbKOkUeoaZP612QmSlTUgemSLTTuoIZlIT0WXa83vVnkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/unh5YtM61i5RsmJWzv8t9tGdas5qaDd2EjgAXsOz6Mb2wdP1yB5mZJM3xYjl3yMUsrZb1jFgXelSRNjY8p0Iq3eq8rlA9lmLu6dQVigeOPhgq_w9tA2Z01fwc_Vy1Rk-GBP9a_oTyw6tf173ueobLihIOKJxhEQy5Ld1-CJLpnWJf0eNEAG-ykcFG1K4uyv8XcDYNwHxpHDb50xkF3Fhm6D75j80y1XknMqa1JmOkmN5gm-CuE0yIQVBcnhxYiA7zgVwWvuSZdOb-eUnxMsXvWB-l8Qif6izO7LLw7iofloOW3fWKnIkZWbSWQOLIW5wFMmNh-AxVYuMDT4-jjRqvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BC4qG-vn6127L-A6ThUNlCCT3lYGm6GA2vDvqRc6jgCLWINIuj1FoIRY27cKt7fgdhf3Ro8oJ67xMAcl8ZxovmdcKj1jOFUg4BVsSr0ZD3ZLC8kwGJXKTgH7iYWFnhZ1dbXMNBsXGDrvXKmKejQ3qxEzLBrmRkzfNOArMztK_Maog9CtFKOfaB0lhvWQcvW95eidcuyxiWrTZrqUQV5yJTLTaQKSaHiWeQ-wspYXDOq_1jSAy3sApmz4KI1bOiTdE6KWd7-UpvHhGxrDAziqqFmTJDON5sGBg1JtXu_Mf67sjXHcdjpa3cIWCrvjECwr_hg98THHrRzYnT9hDpyeIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:)
ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید نصب کنید طبیعتا
محیط داحلش هم عاری از هر گونه حواس‌پرتی و به شدت سبکه. به سرعت تب Git رو بالا میاره و تا اینجا عالی بوده</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/4080" target="_blank">📅 22:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4079">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اپل تقریبا ۱۷-۱۸ درصد قیمت محصولاتش رو افزایش داده، اونوقت فروشگاه‌های وطنم نه تنها قیمت رو ۳۵-۴۰ درصد کشیدن بالا، بلکه سفارش در جریان تمام مشتری‌ها رو هم لغو کردن تا مجبور بشن برای قیمت جدید پول بدن. بله ایران درست خواهد شد
✉️</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4079" target="_blank">📅 21:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4078">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sseW6gFPiEo4dVqkUQf7l-pvrtzPxtgi5KBDNPvzljSp2IDbDQMjc3iVaKInsckflrGkyvfjGNiVddQP1TSlLYxWKjtNd3QG1x-aGUbrCV8YjO8Ep0SLcBCy7Wl8Szg53tfA1TqLgoquw87zlzVSl8m1VBO3PVsD1Dz8kV-18eKgihtsIB91e6nTL3cx6PiT_Auy7rytRo6i6rgJvTvimsFsn_5f8fwEe76YIVYOMhH4u5rwhbg8e9TAmH-8xn2gZwk31A477XIq8zcsqMIoZWwlBVnB_wMfYvN0kp9bSD0V7ImnVBbwAFtgytm5Yb6LzOPk9hokE0-3s_96cPmd_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر توی ردیت، مدل GLM 5.2 رو روی سیستم خودش راه انداخته با ۴ تا RTX 3090 و 192 گیگ رم
😂
وزن Q2 مدل رو هم ران کرده که توضیح میدم چیه. همینطور با اینکه تقریبا از بیس‌ترینش استفاده کرده، گفته که GLM 5.2 داره کار کدنویسی و پلن و هرچی که نیاز دارم رو عالی انجام میده.
تأکید کرده که مدل توی کد زدن، پروسه‌نویسی و حتی کارهای طولانی و autonomous خیلی قوی عمل می‌کنه. و واقعا حس Frontier Model می‌ده.
حالا Q2 یعنی چی؟
حرف Q مخفف Quantization (کوانتایز) هست. یعنی وزن‌های مدل رو از دقت بالا (معمولاً ۱۶ بیت) به دقت خیلی پایین‌تر کاهش دادن تا:
حجم فایل خیلی کوچک‌تر بشه
حافظه (VRAM/RAM) خیلی کمتر مصرف کنه
سریع‌تر اجرا بشه
Q2 یعنی مدل به ۲ بیت کوانتایز شده.
این پایین‌ترین سطح کوانتایز رایج هست (از Q2 تا Q8 و حتی Q1 وجود داره).
همینطور طبق گفته‌ی خودش برقش هم خورشیدیه و هزینه‌ی برق نمیده
🔋
مشخصات سیستمش هم اینه:
۴ تا RTX 3090 (هر کدوم ۲۴ گیگ) که میشه ۹۶ گیگ VRAM
سی‌پی‌یو هم Ryzen 9 9900X
۱۹۲ گیگ رم DDR5 (Overclock شده روی ۵۶۰۰ مگاهرتز)
مادربرد MSI 840B (هرچند بهش گفتن برای این ستاپ ایدئال نیست، ولی خودش جواب داده که فعلا داره جواب می‌ده
😂
)
ایشالا قسمت ما هم بشه
پست اصلی:
https://www.reddit.com/r/ZaiGLM/s/Ew9JHC2XIA
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/4078" target="_blank">📅 21:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4077">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OTP9fjPuRfLHxBLbJipjGnGff9TUVVFR-5Mv6jPWLyHy-vRjk_OPU6Ge7AmPuUOq3iS3DEYFzfmTTulqBf0fRCmSQm92Y1HRcRx3LxeDfqiVEUjpEyjHYeo_HCDcBtDJ2hXUYITFotCcJ-8gbJlwXyMGoUE4BmX4WoLiMrnBL2ZB8pmpOJeV0akWVB_oi8FSVmaHOUPRLGDbeoLmezi1sy2n7kppt3fjz31QGTlQBNqAXpfYjSYAYL3sltDQSrjpsrnNp26QtOC1MwabdaOpmQr9wLrjB1Y5y97JFeKFg1HVVFtQm_n8a5bTLYWqflBS1q0_ZQESCUssnxM9DiXGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4077" target="_blank">📅 18:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4076">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kVYPR2YQsHoKq2c2VZ97MJju3-8mGz1ZizjtPl6VG8hAm-zaCHEIQbNE1TE0yV-YHNsOnLygXLU0O9EMDr6R_lH4yUx7fn48Zz5PQFT7lV7Rtcyhleq87zVfVeLY2Gqw3g6jbEGKKJ7mmqyQGF4c4I-lPA5nr9w4_RlNZxpMvHFjn4WFpAZgYQVkSu007Yxe43ZsW0Gi1-YAhGJBy8UxqO8KUq1LNtSRUlDyGVOCdCJmoEzTiLg45IMRidV7G2DEuBkwfXb7Eb0gZUq9GWML9VxXfi977LAVhYYiaNaemvd6ryR7oVlQ5q5pDt1JHcOTIK17jqgb4U_LQ62dqTUz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده.
به شدت هم IDE سبک و خوبیه
از اینجا می‌تونید اقدام کنید:
https://zed.dev/education</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/MatinSenPaii/4076" target="_blank">📅 18:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4075">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=dWqikKksziZGNLfnlce_dSlKptEu2l9VdD-QfALhv_qThAdWWKffppz8Q03S2nIr6L9d4vqZfEEbMLvRA_eUMqup94py5v_Tj6HgslbT-DSXzonPwj_G-NOofxMeH_DA7U3iCPyQeK-Ey_I-fRvmEHj2DuP5Tdl0YpcJfCBT5-RukSF2vpbMdxKznGsFyLapL4iCSpihRhVGgoDVb_KonQJ1kr-evLHkt4SjSWm9MLlVJLTRqLVEngEj-D0-s8Hm7P4o02vogTHelirNGKM3QCXTRjbisTFzVd1ZTj8Mggx8BTPdnBm1OPu6tP8hvJarV31il2FkyC_toxYYcsn5NA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=dWqikKksziZGNLfnlce_dSlKptEu2l9VdD-QfALhv_qThAdWWKffppz8Q03S2nIr6L9d4vqZfEEbMLvRA_eUMqup94py5v_Tj6HgslbT-DSXzonPwj_G-NOofxMeH_DA7U3iCPyQeK-Ey_I-fRvmEHj2DuP5Tdl0YpcJfCBT5-RukSF2vpbMdxKznGsFyLapL4iCSpihRhVGgoDVb_KonQJ1kr-evLHkt4SjSWm9MLlVJLTRqLVEngEj-D0-s8Hm7P4o02vogTHelirNGKM3QCXTRjbisTFzVd1ZTj8Mggx8BTPdnBm1OPu6tP8hvJarV31il2FkyC_toxYYcsn5NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/4075" target="_blank">📅 16:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4074">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دو ساعت برق رفت، گند خورد وسط کارام و تمرکزم و همه‌چی</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/4074" target="_blank">📅 16:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4073">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/4073" target="_blank">📅 16:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4072">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ev4hV_Pr0jlopBU-n9ZawfnnN2Fdb_hTOPvV9I9wW8QT5fQwR8gRsvDTrCOmKF4_UcZM8KrUWe6CGDMqwn0gbMombTmpnnXQzPTgAEy3rYJW2tdsHp9u2BV0tDtlrCjT6TdeQvsgRyJyMRstvG77wPQRsU0vi7pQNJBaKsJU89DV5A7R2yblz2fjE5xIMN_HLdtzBFWyXfbnlWuu9TQJs4V2v4Ny70uAEb5wDj1-6NtbDf8sBc5pXSKcMRMoRuq6hCc0-vmEXms908QxAAp34gTXMBDBXed3-NKVD3gjLIrSEVv4S0eslzBF3R821hgkSyiDMvAw8DFahGcsbIZqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور  /learn  هست. به‌جای اینکه بشینید دستی یه SKILL.md بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/4072" target="_blank">📅 13:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4071">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kAt_bJmF8k65mdyv8V7Yy9IoeRWOwpMXXUm0IqUXqJg6bshDc8gxvWWoWyG9XCkNpeiF7Qgj8qfOatfuEgbYIhVRg0g7LrxnaUyoXowe6fuVGmfyTCu4XaWABi46PGqf1cFXXQf6mWUJxaQxW9YIfVglJPMoxLIh55pv3KccxLSPHsSjKhu-GZM0Kfz3SciGUux5g3qIIvHKbKgDItRE_uCP6FgpF9Ob8RSk-g5oKYU_rSNlNdlQgJ6IsgWMTv2SnahkN4_bNLBpeFnWnhsQB3iVVqhrcmryhCuxjNUniybnwJ0hrwi-LAwgMd73rkOO67IiSEWFQgBTgCWkfa0mqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور
/learn
هست.
به‌جای اینکه بشینید دستی یه
SKILL.md
بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش بقیه‌ش رو انجام بده.
🗃️
وقتی دستور /learn رو می‌زنید، ایجنت با ابزارهای خودش (read_file، search_files، web_extract) منبع رو می‌خونه، یه skill استاندارد می‌سازه و ذخیره می‌کنه — و روی همه‌جا یکسان کار می‌کنه.
چند تا مثال که بهتر متوجه بشید:
۱- /learn the auth flow in ~/projects/backend
کل منطق احراز هویت پروژه‌تون رو یاد می‌گیره؛ دفعه‌ی بعد برای پروژه‌ی بعدی، فقط صداش می‌زنید.
📞
۲- /learn
https://docs.someapi.com
مستندات یه API رو می‌بلعه و تبدیلش می‌کنه به یه مهارتِ آماده. مثلا من خودم سر API تلگرام و اینکه هی آپدیت میده و ai ها رسما نادون میشن سرش، این قضیه خیلی به دردم خورد
💻
۳- /learn my writing style at
https://example.blog.com
استایل نوشتن خودتون رو بهش یاد می‌دید که من روی این می‌خوام یه کم مانور بدم و قشنگ تستش کنم و نتیجه رو بهتون می‌گم:)
📚
🌍
نکته‌های باحالش:
• مهارت‌ها توی ~/.hermes/skills/ ذخیره و persistent می‌شن
• بارگذاری سه‌سطحیه؛ محتوای کامل skill فقط وقتی نیاز باشه لود می‌شه — توکن الکی نمی‌سوزه
• و اما مهم‌ترینش از نظر من: نمی‌خوای کورکورانه بنویسه؟ با write_approval: true توی تنظیماتش، هر skill رو قبل از ذخیره خودت تأیید کن! کنترل کامل=)
🛡
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4071" target="_blank">📅 12:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4070">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">از اینجا ببینید آموزش WhiteDNS VPN رو به همراه آموزش اسکنر اندروید من که پدی زحمتش رو کشید:
https://t.me/MatinSenPaii/3999</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4070" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4069">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">↗️
تعداد کانکشن ها موفق WhiteDNS VPN به ۱۰،۰۰۰ کانکشن روزانه رسیده .
✍️
در حال حاظر تمرکز اصلی ما روی اضافه کردن وی‌پی‌ان به نسخه ورژن ویندوز، مک و لینوکس هستش.
✍️
مواردی گزارش DNS Leak توی کانکشن‌ها داشتیم. درحال آماده کردن سیستمی هستیم که علاوه بر تست‌های سرعت، امنیت و پایداری، تست DNS Leak  هم از کانفیگ ها گرفته بشه.
ممنون از همگی
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4069" target="_blank">📅 10:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4068">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خب، من با کمک Hermes و API رایگان MiMo Pro 2.5 و API رایگان جمنای، تونستم یه ربات باحال بنویسم!  توی لپ تاپم کلیک میکنم روی یه اسکریپت .bat ، و رباتی که با mimo نوشتم، فید چندتا سایت اخبار ai که به صلاح‌دید خودش معتبر بودن و زرد نبودن رو، می‌خونه، با Gemini…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4068" target="_blank">📅 03:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4067">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vM28OjnyTrLuqx2MHydInOO4AUKfRZA4r1LUapP_RbWxC7FqvEpPqgOkUAYAWggcLCTr6thozq47bdKzz1fhk9-PPTfC3sqaG4FlD4FxMS5ECFDgP22gUXxDNFLSxhYajG0WjgcRsF3BumfIwqI85ZFk4AJ4tX6cCEI3nLqHgd9kNED0mV3z-FVJ436Ul6nui7kzCcQiOGTG1r29bwBeyE_0bJCBxnPmNj3-B9yE1FINTSacZ6uv0HUlR9NPgjbv6spV02tKHoEHdPj3UqdhSjOxAXxRnN5OEEGBugaqan8Jn2iMD0So_t9TO3FlPzHJJSjam-f2yHCnExjymzTKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر از اسکنر من استفاده می‌کنید و مطمئن هستید که آیپیتون تمیزه، حتما تیک همه‌ی پورت‌ها رو بزنید برای اسکن. چون به چشم دارم میبینم یه سری آیپی تمیزها فقط روی یه سری پورت‌های خاص کار می‌کنن
آموزش اسکنر و اتصال رایگان به اینترنت ازاد با سیستم(ویندوز-مک-لینوکس):
https://youtu.be/JdNeZnclS-s
آموزش با گوشی اندروید:
https://www.youtube.com/watch?v=2otJfXgNWCM&t=70s</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4067" target="_blank">📅 03:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4066">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ai-news-bot-MatinSenPaii.zip</div>
  <div class="tg-doc-extra">50.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4066" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1- باید فایل .bat رو ادیت کنید و مسیر پوشه‌ی خودتون رو از فایل پایتون بهش بدید
2- من با venv و همه چیز گذاشتم که دردسر نصب یا ... نکشید
3- توی config.json هم باید api جمنای و توکن BotFather و آیدی عددی خودتون رو قرار بدید. توی این ویدئو اینها رو یاد دادم که چه شکلی بگیرید:
https://www.youtube.com/watch?v=7qYPK3dGoK4</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4066" target="_blank">📅 02:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4062">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g7xUzbxVBM-fJtx1Q-9gn-ba-9E3fIIEKPQ3Ni3wpUIz8y0K-eAoCy5Uz1vanUxamFqVf7pqZ191uDM6kcJ3zNycNmSONjoF2CrFpYZrOrFNH2OKdrKAw1WuoxHQ8oeRJ7tpG8JDplGi7PGlziRPO4Ws48Rmf2fE9O2bDQiaIVdsB-FdGAHBBAgs2gAfzONDb7YqX0yicH8LpRW5CDkPu1XnSmJsDWY7GYY9B6w8xZ9QiVZ31su64S1Z0kgY9LTLlXVMxrNYdmjnJD1ohViCW9oR1Gmm_4tSC1lkXCnb6u1GTObJOn_u81NeO8g3lfBATWhFlyQePtwtS7ZMdma5GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sgSoYBgLsNOg7CEsHpPPYHcXENdbWe4EFGlBZMGHS8vYBlGu-kXscGrdMjlUm5vfp355qi_OezQ4Yk1j_frblVw6LMcdWaPhTgKN2CNdrMMbzYl-1aMpJs51HpZjFioseDIz4KuXAJOvi93i_E0g87tMWA40i51vl7koTBd1bq7s_Mu64t8CZjZLKyZNTKV027-RNr0FJ40oSj6Z9bi2qJ1-dsDxRdJadXtRVuqL6IzwIVZpNM2Vqztn8wGcDQSuojOyCDClQ0LjEHpmU_ZjXNv69535ljJx1n1H65tyxzhk9RFqBYFpoD7ymwcqrzp3dBxxQnsEZ0hIyvJDdHsWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oj5QFbJfsQzMpP6LpnbiQdGChHIQqALcOgxi1Ue8FNMP3bPtwHtQACv5eEsjMf81ZZDR7TZtBUbzDnzcNm8pfJ9ncJjoUM14WF-v02dXxKmczhbnfAtd9oL7E3SlfCxRoykGt-H0PlA1xBbPKOoeVHNT-QpCyYYvNGNARupdgkzHaFfFqn06WyW1UWWz5DTg2bXvCPA3NX7TyiE8qZparznHoO0FSY3s__KP2UCEorIdKxHlPN-ywrX52h5pYsXYU_0gY6f2Sv9sDuEakIOfcAyaU4BUo1XFCcMS8jDXuxaAHNDoTgF7-uX1-oLfbihN0A5RKvoFZXmKTFDf2e9ofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AMv6Ng9_6b4rdyue4m5_LtzDHuJCiAbjPVF1HwKwsiMdIxjmi1I4AXE-YpxLQycX-rPtN4jol8Ab-cdJjmvT6u4RRGCHBPTZttWYoFof0RSqT_gsBrtONc5S1Ne3Kz0x9jm5oqO6K4AXDtOSpABHoiQRqcmRcB-iydPpTu3WMiLiW8kHmX01sbvxwa-tt_oKKbJKLkVi6gd4nq7VWfzVlLpS-2kKWoTs4vyAB97T6If20bbF98OF70_hdQkj1f8l49BiJBhU8OIqCi2bEWywf4cD1nC1-Xr3BDxKgSwztOe--5Kw9zGQSxrdsVpYmH0ZC8hgcJoEC4eHgG22-w9Whg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب، من با کمک Hermes و API رایگان MiMo Pro 2.5 و API رایگان جمنای، تونستم یه ربات باحال بنویسم!
توی لپ تاپم کلیک میکنم روی یه اسکریپت .bat ، و رباتی که با mimo نوشتم، فید چندتا سایت اخبار ai که به صلاح‌دید خودش معتبر بودن و زرد نبودن رو، می‌خونه، با Gemini 3.5 flash lite ترجمه‌ی روون می‌کنه به فارسی، و توی ربات تلگرامم می‌فرسته پیوی من. که خب کار ساده‌ایه و بهتون ایده میدم چه شکلی می‌تونید پیچیده‌ترش هم بکنید!
الان، شروع می‌کنم فرآیندی که این اسکریپت خیلی ساده رو ساختم، بهتون توضیح می‌دم.
1- اولین کار، گرفتن API ها بود. از Nara Router تونستم 7 میلیون توکن رایگان روزانه بگیرم که اینجا گفتم چه شکلی:
https://t.me/MatinSenPaii/4061
و همینطور از
https://aistudio.google.com
هم یه api رایگان جمنای گرفتم. که مدلهای دیگه‌اش به درد نمیخورن از لحاظ لیمیت، ولی مدل Gemini 3.1 flash lite واقعا توی لیمیت‌ها خداست. 500 تا ریکوئست روزانه و 250 کا توکن که اصلا پر نمیشه. برای ترجمه عالیه. اما برای خود Hermes مناسب نیستش چون که TPM بالایی مصرف می‌کنه و Exceed میشه.
2- توی Hermes، از قسمت مدل‌ها،  Nara رو اضافه کردم. خودش اتوماتیک تشخیص داد و گفت کدوم مدلش رو می‌خوای؟ گفتم mimo pro 2.5(که در حال حاضر رایگانه توی Nara اما خب واقعا توکن مصرفیش هم بد نبود برای تسک من).
3- وارد چت Hermes شدم، و چیزی که می‌خواستم رو بهش گفتم. گفتم که می‌خوام یه ربات تلگرام بنویسی که هر بار رانش می‌کنم، آخرین اخبار ai رو با api جمنای بگیره، و حتما از مدل gemini-3.1-flash-lite استفاده کنه و عینا همین.(اگر نگید دقیقا یهو میره مدل 2.0 رو میذاره بدبخت میشید) و برام بفرسته.
5- سری اول ربات رو ساخت، و بعدش بهش گفتم یه سری قابلیت اضافه کنه. مثلا زمانش رو بگه که چقدر وقت پیش بوده یا فرمت بندی رو درست کنه. همینطور گفتم که برام یه اسکریپت ویندوزی بنویسه که هر بار کلیک کردم روش، این رو ران کنه( این شکلی راحتترم خودم)
6- همونطور که توی تصویر می‌بینید، خیلی تمیز برداشت خبر GPT 5.6 که واقعا هم سه ساعت پیش اومده بود رو پوشش داد، همینطور خبر های دیگه که یکی از نیازهای روزمره‌ی من رو برطرف کرد تا حدی. که یه دید کلی نسبت به اخبار ai روز داشته باشم. سورس کدش رو هم براتون پست می‌کنم که اگر دوست داشتید، تست کنید. هرچند چیز خاصی نیست؛ خودتون می‌تونید بهترش رو بنویسید
7- چطوری می‌تونید بیشتر درگیرش بشید؟
بیاید با همین "بات جمع‌آوری اخبار مربوط به ai" مثال بزنم.
شما می‌تونید این رو روی یه سرور لینوکسی ران کنید که 24/7 ران باشه و هر خبر جدیدی اومد، درجا بفرسته واستون. یا حتی ببریدش روی worker کلودفلر. و هر یه ساعت یه بار چک کنه، اگر خبر جدیدی اومده باشه واستون بفرسته
همینطور می‌تونید یه سیستم پست‌ساز نیمه خودکار بسازید برای تلگرام و بدید که پست بسازه برای چنلتون(و این وسط توسط خودتون یا یه agent هوش مصنوعی دیگه review بشه!)
خلاصه که راه برای درگیر شدن باهاش زیاده. کمی تایم بذارید، و کار با این ابزارهای جدید رو یاد بگیرید. من هم خودم اول یادگیری هستم طبیعتا:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4062" target="_blank">📅 02:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4061">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nm4Yq77pOSnxmGOXdDhFeV0WRFTenNsSEptjtIZCzM3Ovlj8kNvjOhwlui2BU_fo6tzF-R4myIPaTD6bUE9NlKqVbysfxaz4TJcfFzDCcPg9WqBLPYBQdByEYPUMEgdmKoESjfMZh-TnvRTEky8VGnGSn2kF9cpIL2bm9xMjfdlittBxmqF23yedxWmrzT8e3I816k6_dagvONlPv1SjvC5EmGnYQ6OOS-drXwdCgGii29GiI8otXehFjcqmEeRLOPBMyz9U1e9Pmq3Tlz-_rZI1OIiY0WLItDf7H1NNdNzIVO2mjomCmJ9scl6ubU2G8z3EDv_TJjl1W6VjyQGqwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه!
یه ربات خیلی کوچولو هم دارم می‌نویسم.
دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes
خوبی این سایته هم اینه که روزی 7 میلیون توکن رایگان از Mistral و MiMo Pro 2.5 میده و هر روز دوباره شارژ میشه. نوع API هم open-ai compatible هست. اینها رو بعدا توضیح میدم برای دوستانی که متوجه نمی‌شن پس نگران نباشید
از این لینک هم می‌تونید ثبت نام کنید داخلش:
https://router.bynara.id/register?ref=PJ6RZMDB
رفرالش هم چیز خاصی نداره فکر کنم، صرفا اگر بعدا خواستید شارژ کنید، وقتی با رفرال وارد شده باشید، توکن رایگان اضافه می‌گیرید</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4061" target="_blank">📅 01:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4060">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مدل پرچم‌دار GPT-5.6 Sol برای برنامه‌نویسی، امنیت سایبری و اجرای ایجنت‌های هوش مصنوعی بهینه شده و از قابلیت‌های جدیدی مانند «استدلال عمیق» و استفاده از چند ایجنت تخصصی برای حل مسائل پیچیده بهره می‌برد.</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4060" target="_blank">📅 00:10 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
