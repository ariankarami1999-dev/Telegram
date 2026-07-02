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
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 18:05:51</div>
<hr>

<div class="tg-post" id="msg-4179">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز: https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو: 00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟ 04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس) 13:47 نصب و راه‌ اندازی روی…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/MatinSenPaii/4179" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4178">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/MatinSenPaii/4178" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4177">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/MatinSenPaii/4177" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4176">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ویدئو 2 ساعت و نیم ضبطش زمان برد، بعد از ادیت شد نیم ساعت
😭
دستم شکست انقد با موس اسکرول کردم</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4176" target="_blank">📅 04:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4175">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M-fIpp4dC3jVfMavwVCGqD2r5pYX3MxyqL1Ap1-xTzIG3ZnKzBKNKfw7sFa_OyWDcYY7FGeYLEHukZEzZhKDvmyS-Sd6GiPJyU8izTSPAC2tjXzX7vZHhl1fjXCavIr5Kop-_CVJsqG1IcTICS43lIIjtfpNTammO31w6tZFv04Pkab668VrrH0cZ_DDWK5hE_RSu7s6B8_qwEq-uYL60B3__W8DLYOpWzBJoVnt92AUKI4kxvU3BPLGjHw8DzVO9X8uVeewj7n5KVwr5j5kQRT8Xa6KVOCUcmJFkr0doBNpAR_6RdWPPRzwMb0WBMUVwrNxnSQL4B91FIRfOfWpPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط دسترسی به Fable هم برگشت</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4175" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4174">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وسط ضبط ویدئو به طرز ضایعی یه ۱۲-۱۳ بار به ارور خوردم
😂
(اون پشت حلشون کردم و شما قرار نیست ببینید. هاها)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4174" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4168">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/4168" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4167">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/MatinSenPaii/4167" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4166">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XCuAj5ceaDHAq3S2agIGIAcZ9WcbbUpR0QhqSbe8-MqJ1j5qheUGTpcfSlIBxr9j_9K0UGP13DgRYxZv5BpJEnKw2B_3oQEVuic3rfJYMSQq6_R1qarXtH63_0SxqprpudsGChcvCszTj0LpBT4y48z6xr7WBaJgC4MCHaZ9v2xv4YvtqkWaeortD_xMPAlNsybzhPe_JbJp4A13pVL18Luo4_gkkVQ2oHDBYOl9aEecrEAoglvPFjkbcI5r_mg2JkXtJvfWm7gNXvZReGlWUJDuwhEIn3zhAhxTebt8QXdLTm2kfwgiSo4zGSWrKix-cpu25J5s40gb20yzLlMOfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این api هایی که Nvidia میده واقعا سخاوتمندانه‌ست. 40 ریکوئست در دقیقه
با 9router انداختم پشت هرمس، چه میکنه این Qwen و MiniMax3
توی ویدئو آموزشش رو میدم که چطوری بتونید وریفای بکنید و ProxyPool هم بزنید که روی سرور مشکلی نداشته باشه(مثلا با آیپی سرور من مشکل داشت انویدیا که با یه رله کلودفلر حلش کردم)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4166" target="_blank">📅 22:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4165">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4165" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4164">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EeC09xEtvW44xDS4XyWkLqbEzaOgDOZop0J3JUEYWYeDPBQtQfHOpMvpQMQJLqe9j2arjadaJQm5ShsjyoA1kbsW7nMLNmfDzrG1y02g9cQGQwNNArw_VglOjOui3xcSSMmoEzBH3_FMxut3xx1cGywCQiY7X-YvGso2tfjvD2G8h82gxKWN0AJrnj4Y125UwiKIRnxYCLaEPBdC-e0NIA1J0hzrQucVBP0UErZg-jy1WWqCF_0kKAk9Xxmp1uu7Nusx2hKQPYLoMh_zPhndAw208YYttG-2exSMTLwcDpfz007dDN5GxvCD1cYplTvfXihDx9RXyls8pZ4pvyb41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی زیرساخت‌های پیچیده‌ی پرداخت هم بشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4164" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4163">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">از بین سایت‌هایی که تست کردم برای SMS، کاوه نگار که باید میرفتی از دفتر اسناد رسمی احراز هویتشو انجام میدادی، فراز اس ام اس هم که شیش ساعت گشتم اصلا بخش API پیدا نکردم انقدر UX اش درب و داغون بود. بیست دقیقه وقتمو تلف کردن این دوتا تا وقتی که رفتم
sms.ir
و همه چیش اوکی بود و 10 تا هم پیامک رایگان داد. خیلی هم سرراست api تنظیم شد از خارج به داخل هم دسترسی داد</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4163" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4162">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تمام رادار جنگ الان فعاله و AI هر نیم ساعت یه بار، خبرگزاری‌ها و پنج-شیش تا کانال تلگرامی رو چک می‌کنه و اگر جنگ شده باشه و اسرائیل و آمریکا به ایران، یا برعکس حمله کرده باشن، پیامک میده</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4162" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4161">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hNDHM3BCg-JopextW9SRkz9vEe-suhgKSL2U0NLQS6ZDZQn44q1SawcriE7p1EMmFMWZ1xmfT0WuXlRFSo3J006AfXdMcyZvhwt-zl0xwBtlu0nF9vXVHnaHRJbh13sFO5zhrbjeN_9CIMeCnff6y1PfWLYETwtfNqXkrUht1fiOwO5kkmXYBT-7ZZINWkBAGWAZ48buDusT-EGJz2M19mLDwUnCW59bFjYxKUf9iR4WIIdRMe9eB0tw7CSxn1OENAPNqZvlUe8tIVdde1H1-gAuYih2sfkIR6oi9_zdMZfZD_ObNxbyzXYTURrXcWotmIce7V-_bXaAWJw_31dQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4161" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4159">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4159" target="_blank">📅 15:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4158">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ivPw8qGNJJ_44XDsdz77ZsAq2DCjC3ObXD3V5YqShO8FjXROr--ohCGFeD00CRv0hEjOEIFx6Mh2CKU9eA8rOnKmopTSkIOfwg2BW1pgvILIzhCMglVdp_OpTRyt1TFrSiRw9iUUEsVAwnrtN8E1-Rb0x-5yCO13YnbwMxm7_G390MS9am-KIrj1TKApD8Uy8jzwGsnbFLU-mrLbjH4dbLy7Kp_ovXgwp8g4JsjRZiiSSBwHBDKMf9h525fUh1Bu3wNlhu5QaqgCnT9XuOqT3VsFQdPuIIxbUgzN41NYFKu_Fs_lgFiA6TL2Sq5cLDPvt0VdEzUtpjVFED6xubzazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی برای خود یادگیری را شیرین کنیم
(دادم همه رو هرمس با gemini 3.5 نوشت چون هم یادم میره چی رو تا کجا دیدم و هم همه‌اش هی چک میکنم که چقدر ازش مونده و الان درصد دارم و اعصابم آرومه)</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4158" target="_blank">📅 15:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4157">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">می‌خواستم ویدئوی هرمس رو ضبط کنم اما انقدر برق نوسان داره و هی سه راه قطع میشه کلا برقش، اعصابم داغون شد. می‌ذارم یه کم برق بهتر شد میگیرمش آموزش رو</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4157" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4156">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">همین الان ویدئوی یاشار عزیز رو دیدم، و باید بگم دیدگاه فوق‌العاده‌ای میده به شما از ai
اینکه دیدم یه سینیور چطوری بدون گارد و با آگاهی و مطالعه‌ی کامل از ai استفاده می‌کنه توی حوزه‌ی خودش، واقعا لذت‌بخش بود.
نکته همینجاست
با این ai عزیز دل، حتی باید بیشتر از قبل مطالعه کنید و دانشتون رو بیشتر کنید تا برتری داشته باشید نسبت به رقبا. و قوه‌ی حل مسئله‌تون رو تقویت کنید و کارهای تکراری یا سنگین رو، به راحتی بسپرید بهش. اگر به مبحث باگ بانتی هم علاقه ندارید، ۱۵ دقیقه‌ی اولش رو ببینید حتما
https://youtu.be/-Rt_Z0allhM</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4156" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4155">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید  لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4155" target="_blank">📅 13:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4154">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R7Z74pfsNSBBA7nmu2lKpsCQGlCi2LcZwjAGsvR-V2qJKWSQ0B0SgT4q_p7qmgSkYzpDqYyQdWM2JbZ4GuHOESEuvArJWPf9O8J4vINZiUzfjZcDEhQaLdio5PfMPdNTMmKb79oTJjeiBFbrZ75cqzl8Qg8BcjvBUmmARWhA9vM-k_ssJSOwL7sYkF1af4VsxEPgvCGSrtpsZvQgaXrjVjzid5TOsIJ2wUqRmpxxaqmrhQjoV7Ofa0LHvmZWj8rFhDx8he4IebTq4uTCSPTqJBIYsfsleMzjOybttZIRMCu0ufj1cmgq7oHrhJC9U5MxAeq_CU916jF0n63zw0HNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید
لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4154" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4153">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FtLUE1Nq4QxdimBGXmbRyWwg9UM9hYbHL8XiO45T-qIEwBFV4wQIJY5nIC-DIMa9k8_EotHP77leP-Gy2BckUtqaBNiAPOyL8wvoy5Deu4to1LeOR0tmC5K5flAp9l93fXzpBzZvxIluT4Y30MFGUE2r1cY4RZ7iclzGI8G5QkG1M4vZeKGcTGlG4U6ZIpvsaG5w1LNcGyGCxSaXM7iEaWEFwDWZOhN_RqlajrO-KANNRm54FzMYo9EpPSLn3DxtY2afx5RauB6rZG07okV5DxjILPHHGbhMqnkWDhcpmlJXNzyfzKoTSFPyDL6bkZmGJj7YEMbYqt4r2QCG48bT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غول چینی، GLM 5.2
همچنان ارزونتر از حتی Sonnet 5</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4153" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4152">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خب گویا کلاد Fable 5 امروز برمیگرده
😁
آنتروپیک گفتش که با دولت آمریکا مذاکره کردیم و امروز مجددا مدل رو آنلاین می‌کنیم</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4152" target="_blank">📅 10:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4151">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dpwevERZrKLD1GKqQ3cN5jTUG0S0E8tUS6fhZRl0hVVILti5856usxE79VXsFkiilcbfhMXByH-8i3HQtW3TSaFovf3hym5-FcAnUgvqT3lrhATGPSYFp-NlJzzRCJfFUbew6wi099c4k6SQRHkktdaK2V9TjAKAhuFXER23lXH4mJMJ8urRd55xCdCPSe4N992wIWoHL_JD0_Su7hZqachlb_fDeXf3ij5zFVvRtBNDdLStfA4HKWsTX-OGrAfo8RJ2vSWG5mt_p6A4g4vlDOCk4b4nyMYj2iCo393lSLC_M4Rms56XSHB1KkrVbIeKlCeAGYFiYvFpQXvpu8wgEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4151" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4150">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4150" target="_blank">📅 01:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4149">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4149" target="_blank">📅 01:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4148">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4148" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4147">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h5nQWT3cYhIZqdlE5OJWT_2nkW0Aqw-T11unkCSmbBMvH1WoLuVpwfwxjKTl36rzJsiHhxuI6ExH_HJxOT7stdPki1hKVwKToVZmLBcOyXkfrvgpuMfX-_4qw-zeD62-hLVT-QLmFfoN2fPDsy_9DOEonjsXc-KtXUtIq4HPNdSEFQVDQcGibAQXMBpmnxOsDdEyDmnVjrx4okbP05zCMwtLhjSxaNSzTTrSSFmqq-d-OG5x5R9kH_gnseCiKtq89d8lAgYSXUtGAfZgNN5Fqik3EoC3f3XJD35IFPSY-HET5hgRsiYu1h1L5PucuGlUfAsinhr6ALkUx-zl0QC1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک منتشر شده توسط خود کلاد</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4147" target="_blank">📅 23:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4146">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HGKedvYJstP-n9DRyZIJ8imATemw979I3MhUKc5LSdN1IrOJHJHvGfGtV9ffRTh1d2qg-IVC5iOLjkyF7zTkEWhoOlSG_Ytiy7sA1BtS9tYR-GkTB429R2YT3CKqpuLiLUHBihTax-P1p4jis1TnGB95-kc06QIoeGjJolA-aaeZPTMN475LVjX_rcZm5F4AzKVhJ7mAYqtw_Am-0in7Jr1-IVE0O02oYMlorBEwrKnluMQzxxL4RjH49ZTlX2MiWVA-xYlmB-x2QWUPuYo4iddzu6g4UExwWOycqoF5wzeV5-XQ6zX5Kmad8G7yngS9MVUc5bJUW_ilr19TMHGMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌ آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4146" target="_blank">📅 23:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4145">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XJprUHjk-jtJ3MiLtY1RoZLJIj5fY6Z80CaT40GwBlJynuA6Ua5PL3vVVtz9Nkhhmc0ha60MZR2vpsqryG8Qkd8jMJrFS84EaIkuwTAbsLRJ_b2B3aK6GfgcTjX7oUFOTbLSBwrEVj7QfgBIAEfh_uJwN1Y4gUbJBft65zOQdNcgWB7uNyM6WXA9U879QCdAx_oVy4Lv3yMP3RKVkXnaaLeMm6_eviyn9uUIgM19vkGi1M2y7vA_bfhw6zfFw--JvKQoYy40GoE5_dCHSS_xJA2xzyjo98koI4SjvBReags1BF-WnOjmcsDReEC6_7r0se2z12Sl4fnlgfs6Zte7gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌
آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4145" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4144">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!  این ویدیو…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4144" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4143">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4143" target="_blank">📅 21:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4142">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M_mJbp1ydmkHyexKeIGcrgGkFcV23SRD-KSMf6eeWLCNal-IgAZcmyaVW9RE8I3vsNHdInOMxLWzbkPrINAeZhu-_gs6lpeciCVRj8xyZTbGnOxyVIy77KmrFTaq2l55w7OVnIcLZzQwhRHby8d3qkQ2XTOQ_GaxyahJAd3TH3HT_j1M9FaPyRVEqpLgByU1Vsit51LABeSQvR0VqtZjCSWQHfDmkaeio2z4_6e5PJpUlMc_IudGU0Jig2riGwnKUUi2AnkjcBPl6wi0t2SeEvKr0qmEmhF6SV4bjpxkCGxLmd896yaeMP3vVih_hQ1kgYShRa_Q064f2in1CF8tHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب یه قابلیتی آورده به اسم Ask پایین ویدئوها، که می‌تونید وسط ویدئو اگر جاییش رو متوجه نشدید از جمنای بپرسید
🎨
فعلا برای وب فعاله گویا</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4142" target="_blank">📅 21:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4140">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4140" target="_blank">📅 18:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4139">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4139" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4138">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انقدر برق رفت و اومد و نوسان داره روی محافظ میترسم لپ تاپ و همه چی بسوزه آخرش. آقا بیا قطع کن همون دو ساعتو، نخواستیم</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4138" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4137">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بیشترین درخواست توی یوتوب و توییتر ازم این بود که آروم تر صحبت کنم
😁
من فقط نمی‌خوام حوصله‌تون سر بره یا وقتتونو الکی بگیرم
اما از ویدئو بعدی سعی می‌کنم شمرده شمرده تر صحبت کنم</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4137" target="_blank">📅 14:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4136">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/stchpxNcEjh9pPkapD-vUnGe3h-P4SKPKTycUlCkjHGMQQf3CqM9WCe4XsQf_fk5uw25oKALZ5VBPDMBYQ0JVWixHoIACluAAQNhNCpdRJOroTMNIlZhol4avmBIRmggt2oZjodfrPUfkY4CGpB8BWXCtW69QZT-cv7IxAsyPXgJ6QWTNC37Z0WJVknj79nRU7e9FHcfj30_6b2lgZ2Lz0Tj1gx6LEiaQ40W1ikJaNOUArTaOhT_P8DIs5vo2r1kCgKeBmHpCeQMDwflkjR_USHiu4V1B_pY-WuwyxqSpj65mQiE-CgI1f5kKi3WsMPpm6xzFztPYJazQkNAGMg_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد نسخه‌ی موبایل Hermes، من توی ساب‌ردیتش دیدم که یکی واسش نسخه اندروید ساخته و Pull Request زده روی گیتهاب(که کدش ادغام بشه) منتها هنوز، رسمی منتشر نشده</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4136" target="_blank">📅 14:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4135">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4135" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4132">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ycg4F4FaqkQ0DNz8qK4Item_nb2A91ZSuvQoNWJ_36ImqlhW0I9d9BnnHVA7ugEAejVrzIGodMGVDwWhSK3H2U3QOH8Iq3UyJmN1gLJ03YGCyn_NN2XzYLGhP1MmSzwRpvMJMUE8jP02lBqviWA49HGoVsMclFJjBJjKa4VNT4LQ1ipFVj13SgRdbLb3iJpXtGfyBqUv3v03roS9HfmGgYuMsK-D3uHYXhsOfp7wLPsELbBZJgMEGppw-aZI0Gbi1b4wLTOnpykOyJN5XBLNEgt3E7CYGRarQ_xEY1NGjvrW3MqTuXuIa9b0DxzHQ178Z3UoRzpf47SlnsiTor6nIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OD3M976VRzG469fe_47SXfZ1JqatjKg3YNuNy4BLog5_icBV254ZtPtNr9o2FO5hZRsVVGmUHheZvCQwUH25MjCrykouZ4k5v7qzxub2exZ9NlpgS2Je6QGTVMxIPmDPQiLoxD8qWF93aJ_4XvJiIAt9Ok6Y7ipvgtt4vGc5v1-P8nIFe4ZJCWHs86ID2w5044eiKWAjSyL_xpcZu8p3DPJ5RnaRhLDTqjE2tbp5ZGiVWudrz8BCKGbAWfAP9H0-f-TfDTreuF3Oo53cESBdZMVzS0uipqrsZk4C3MA3LyiF2nMDy6xq2CeDB3yc8RS61QTG_j_GTf-xwdMnOH0p9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l6hUSh3T09dm1dSLKWHWFpDxdRdlY5w62UHgn-XxtjGZJStnh5g0rdbIN9OFhto43K0tFFcNNeiz8MFyYEy8_4OqyKPZtV2gwSrcxr-nkns4_enwHwINRovtUgVVDpYyoWhSLvTU3ql84FzkHhmnsormo9phd6CKmYjcfLZb0svJKu4NMR1T0tyfp8jCr915sm-rD1t3b6BhIWBcCJeybxCgw_LnGPIAERhJmh6Q37RMrGjPhKJo25ULkuWy6PejsTP-xvI8nhe42LndqYml3V7vDhnru3IGNO-vsyOMHDX1VcauAgx6SXCEklImyiIP0FnKvlfNug3wMhkX4Ysteg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واقعا Hermes و وصل کردنش روی تلگرام، یه چیز دیگه‌ست!
فقط کافیه ازش بخوای، و بوم
انجام شده. ویدئوی بعدی، هرمس هست
👀</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4132" target="_blank">📅 13:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4131">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4131" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4130">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqxMZxCc3qYmfO5pXpvGvvyJXnjUKswCZ8ftiyEVCh97zI5PHboNb8jP08iuEkENf4FAWepKjzKvk3yKVSt2tfC6O-97pAPIPkgzloCKkq0-ArkKYjBruMnbO_oXmMw18psbH1NxGhLMYkuANl1qc-tZtxWv3Id7C7CveXg-U2esUYuHR8HQ1WaOTHRIyqXgheUQXgnR8qaFXC3uZebysCRRlHpbossyQBRdIXe1y2r7a7cXH0jk5PKcJdjJhfABO0d-uHQQX6HtV4GYIzE7kOqRT_vc9lGSluum31EGj5_W-uvFVXIM1wORNgbgmhZ3wsoF5ZafXNkqLHu4J5Ffaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4130" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4129">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5950435463.webm?token=aBZ8wVoB9ea7qmMln__IeRPh_3yKnbrxdJ6qjL3SHRgDMYj8i2ntj_JxiNs9avb7zC6moI_2Caf0oWvQY1A9FRxoaYgSi51FXQIIL9K3q1XpCAev8TW0rEwQOeodYf6n-XebE9NwpKbQLid1o_yOPFM34Hzl81tNgybpMvhTuN56XSsS2iKhOWtDiK1MdWMl8k1ZnN4RmihaAxXHTrGQWlXp0D7fh0nSlmBOd-plk6Lz-P2rEun6-Rl5nhnpuZ4nSaWnpWSTRi734HJqZaK2yPRAWEjXulOyF_ST3LPcXoviDMf7OmWlIcHgR__8J_X91mlIWABatgKIiuaEgAjyTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5950435463.webm?token=aBZ8wVoB9ea7qmMln__IeRPh_3yKnbrxdJ6qjL3SHRgDMYj8i2ntj_JxiNs9avb7zC6moI_2Caf0oWvQY1A9FRxoaYgSi51FXQIIL9K3q1XpCAev8TW0rEwQOeodYf6n-XebE9NwpKbQLid1o_yOPFM34Hzl81tNgybpMvhTuN56XSsS2iKhOWtDiK1MdWMl8k1ZnN4RmihaAxXHTrGQWlXp0D7fh0nSlmBOd-plk6Lz-P2rEun6-Rl5nhnpuZ4nSaWnpWSTRi734HJqZaK2yPRAWEjXulOyF_ST3LPcXoviDMf7OmWlIcHgR__8J_X91mlIWABatgKIiuaEgAjyTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4129" target="_blank">📅 04:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4128">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4128" target="_blank">📅 03:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4127">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U6pcV7YHiIE_-3UNXxe-ZjkzywHYQ1M8Q1l51ZrBNZ7IboiwXY5mCs-9-Atp-81JAoVRYaJxoiLlwTtLNuhg18qZqeX-d8_zbgq8biVwA3x6tzkv4fEGjJzfco61B1L33HrrARnyJyumGOnS1mOQCh7zLeePLKzBSjawfjZhcopQx_jcY6bSiOdyPUGNlBWp7-ajR3gvz1eXVekWhBl3Md8vLDew8XyfJ8u2m87dYg9SV0w0oSKOkk1AFgsohpP1OxueKQuoVMcgwrcpTmnwCIhY49afG9v_Xe6PuXBx32UlUI7L1fLOmFrkndmjk0hES6ym_nNQGGmMwv9AN9GKaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4127" target="_blank">📅 03:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4126">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وسط ویدئو متوجه شدم اگر کانکشنتون با api ها خصوصا جمنای قطع میشه هی، می‌تونه مشکل از proxy-ip یا آیپی تمیزتون باشه
گفتم این نکته رو بهتون بگم</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4126" target="_blank">📅 01:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4125">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کمی ویدئو API بیشتر طول میکشه تا آماده بشه
صفر تا صد تمام API های هوش مصنوعی رو میگم بهتون
محتوا رو فدای سرعت نمی‌کنیـم
🥰</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4125" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4120">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4120" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4119">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اگر نمی‌خواید این بلا سرتون بیاد و کس دیگه‌ای بفهمه ای ایران هستید از وی‌پی‌ان‌تون، از نسخه‌ی جدید WhiteDNS استفاده کنید</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4119" target="_blank">📅 18:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4118">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ولی GLM 5.2 واقعا عجیبه. قیمتش روی api تقریبا ۴-۵ برابر از Opus 4.8 کمتره
این چینیا چیکار کردن با آنتروپیک، خدا میدونه</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4118" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4117">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:  1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید: https://grok.com
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4117" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4116">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تمام سعیم رو می‌کنم که سری ویدئوهای AI، برای همه‌ی مردم مناسب باشه. تنها خواهشی که ازتون دارم اینه که نترسید، وقت بذارید، و ویدئوها رو ببینید و کار با این ابزارهای جدید رو یاد بگیرید
🥳
خیلیا که کمی از این فضا دور بودن، فکر  ما داریم راجب چه چیز خفنی حرف می‌زنیم و ...
در صورتی که شاید تفاوت درک و دانش ما از این زمینه با شما، صرفا دو سه روز کلنجار رفتن با ابزارهای مختلف باشه! همین.
به محض اینکه کم‌خوابی ۳۰-۴۰ ساعته‌م جبران شد ویدئو رو واستون ضبط می‌کنم
🤲</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4116" target="_blank">📅 11:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4115">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UZHspsjhzPN1VdHgmj9PHjKFFTcJxpZO_ETG2GQr2peWIARW4tQSpvw9YwOfoxkbKpeGtAVXDPlIhx1d77jQYcu3kQclj-NNZn-RukKeUFD1YqlWP2EPWy_0psUlMnKJMdH1M5TCU2cZr5Rz95-4IHjla8kSILKkn__h0V29sX6ZHOlTYioZDzimPTTUM4glq6cDcKBoLGuZBhY6GwD9w2bjdfEEi7W_mF7uFYWYbRv9mm0B8PMMDk9MpMMDQYsv-HXs-2uDu5u7ipYUE7HqcNBAjwheBkJw5yazIxisZnNHer6k9cmcyB-ljtU0HQy-1cCCT7-7LDFUfxXD1iRN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB  ۱۰۰ دلار میده باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4115" target="_blank">📅 11:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4112">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HS2flFhMBbDHO2deaBL5FfqrV03FFpsC32Tq81_mWYawKiVOeWoRTmbxEsTEfQ1ZceqN-FdmiptJy9FdjH2LpzwFmfJSs1VTYdSenqvqlR7NVJYLreRwEu3eemufygj0i-Kn9xZISOMYJhhRL-_lgHraeto5Cy7yJ6fe6vyNzsK9tiG0afJSlBeA9tMvETb-Hlz7WefbJ73TmvotjwNI1y0CCujJwMVsH5ABwNqGXqxCxPT2uRkMWRH7ezmqGKPM97ELy0Y4YzbWmTYOmbtmuruxhFSmAECoVcuDvviO7Uy2hmP8JiTRH8_l2ABgV0HM_OewdvcJ4Dnm3pskqq8n_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hwOp0cR-aOopYprQr1ityfdxpfUXHJN-fMtLEkJk7MTG90WPy4gusi4IvTXfGwU5X_fuPXgRUu3KR4OY_dVH3DoNaBV3DggtYjph7G7ZQaGyex-kTIPEu5WKvzgRUdlfGw8AdTz-SK8frEoKpSUJJOBkl7ApzQxuTaPtpFeMKwm7FUHsLogsBvTB5NMXpAY_umvv7wolHeG8XuwQBpI0469ZRsMIGkTXIw4x1skcq1bAJMan-H6INa_9K0ZtYkX9vX4obTKA1PLwQoZ0ukySWbKt69FHteZ6U36oq8KfSNJ9C2OovC-XD69-YRu1F6gHVNGD29yoVnBMiA6vkyKPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sGKIiXU1a4YiF2R4uPZMNq1S7Sh_wiEasHaJlqJijDwBOcDQr5LXC4qH6DM2vumI4DLM2CuoP7bvxQey6CjUISFkgJB--Ae3TxCBnfh602uv2tGXXB8bpAZO3RAkJUW1Hde82gOmPEIBuoJRgltBzczFIcLONz1zZXJbb40Zkfr_wDZmC8fDQ21zFHgkW3vyje-eyBB_eTvJJJlqlvS8SRmtYvy4RyRs3XdI6to42pvEnA6buVihfYF7X5f20hlbguUn_5aQ-5Gmg5fXOIA2DUXz44pKBDQl-j8NErJ6n_gORfR8TcoZo7baPSdGCXLsN087WDEXLTfi3VefjPWTTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی واقعا داره پول میده به یوتوب که ایرانیا رو به دین مسیحیت دعوت کنه
این تیکه هم از یه فیلم بود. دوبله فارسی
😂
😂
وبسایتشون هم بامزه بود
https://daneh.online/four-spiritual-laws/</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4112" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4110">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vx8QzupRsqF13quDEYfttcBNMsbw9e3L1fD31iA2rGiOdSiICGtMvMGTdpKXXeGDv38YiM0NPhpYPXGAgfZx61d2FM1_nFumrciMH83a3I1HgC1wNnsKWuCphMFHpZIhv1EcvVKSpPLozcFIbWzaD_U1jGjl61bS6imFKSWERnQHYbxuvq2TfuEOvIAbkcuvoC1b0ienhGUnVrcxs13Ry150O5NoeZVgD_FEX9SYQVuPOvempQkjnjZ8NvJTwTTfve3bojcaBGbEWrrIXd9pjZZSWOwN97Jk9JhgIB25M-Iy_QIc8MpSdGYTsxXuQgAU3RuH0neNsOz4K_NTMHlU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hs-TapCZkrj3Cqckar7qrD1smXVDEcOzv6D8XC_MkeRgWB9utxkepY3oGy4ifK8OeuaogQ5ZKHVn5Alw5YYRlFd18Crm2karterHWrxQ0jLQ-V4_0ghuGH7bV5vxLq8_F7P35GKoDIYaKmKpKU2leqsnQe-PGbOSJiuH9v4NX9UKV7KmUdzYvuMpCJPRdsMZ8CesGFLeU3xvvVi1N6p1VXUoLRw9S2_RKR6YIG_DiTmlLM7T9UBoyziSv63fgtD23DMLqZEgoAHEgP2ZbrdAWwBO-K4FJ6mKXBVqI6Gd-UIeSuYtE4L-ixnPrmuS0WfFlHZNKHINuWFkdR7vF2rHKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:)) همه‌ی اینا برای یه تسک ساده. بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو 10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4110" target="_blank">📅 04:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4108">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FEAteGMYrnTp_sMd97MeKsyubEnI5gsiUcxtRVZXCjZ5xb52UwsVjifgFJIhfH8L6ibaTzw-JgosK4M_4i5_30OB5bKcEFKPpGdTW02lOYkwo0TDGItPo4piEh7aMxcSs-_qQDfctY4gvyZZ0IRwjwyXhc_2luig8PH_5DQqhh2G2ICV0WxXeM8Ct1foHDFU5NNp581nUX-KfGreAbUUhDoG_EGWluwXhQHkR1a57LYXzv1QHwX2cFwduDKrprELBLULpTxPNujXrCd3pwA8CMT5BbCe_mAKP641ndeg-Ot2_YqEcv9C-lzauDNGEHYdGh-uG6iNAEBt8dIzNVo8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ug859St0UqO8iKvzv6g73PsJds4VsRMnEvZG99xk-Gh1v4Sbxnw0XECxcPbNn6bUY8QxfGnjxkec3_2OFVzhCOpxdtljYHyt5bdk5geHsIJPH3k5aSZL_xdj7xb6SpOxQNI7pQcKenUosK75_KVUE33VOV77AGqfhMkc8-Djy6G4v-YqeK09LHN7sMwRt3Y-KFO8weaWgM4gzNmGIMMQkEWozbHy3AFmbN9C8jyEl0mUEFSps_QJVjQ8WMalZyHeUzWYaBGlZx3USVsPVDzcV5yRpJAzh1L4aaqX703cZcXJbU5rT3a6WOcfqmcVKwaWwbJSFjkZr4s7gRMF17dubw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:))
همه‌ی اینا برای یه تسک ساده.
بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو
10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی اسپویل طبیعتا)</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4108" target="_blank">📅 04:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4107">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از aistudio.google.com هم می‌تونید بگیرید که…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4107" target="_blank">📅 03:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4106">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از
aistudio.google.com
هم می‌تونید بگیرید که بسیار راحته و توی ویدئو بهتون یاد میدم. در کنار یه سری api و چیز میز دیگه</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4106" target="_blank">📅 03:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4105">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رفقا اگر می‌خواید از نسخه‌ی دسکتاپ Hermes استفاده کنید، به نظرم یه دور Hermes رو با Keep Data حذف کنید و بعد، از اینستالر Desktop استفاده کنید. چون من دو بار روی دوتا سیستم مختلف تست کردم و اگر اول CLI نصب می‌شد، بعدا با Hermes Desktop میخواستم نسخه‌ی دسکتاپ رو بگیرم، به باگ‌های به شدت عجیب غریبی می‌خوردم و یه سری از بخش ها کلا به درستی نصب نشده بود. الان که دانلود کردم از
https://hermes-agent.nousresearch.com/
اینجا، اوکی شد</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4105" target="_blank">📅 01:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4104">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کار خفنی که پدرام امروز کرد این بودش که جلوی دی‌ان‌اس لیک رو گرفت کلا توی اپ WhiteDNS
اگر وصل نمیشید به اپ، حتما از Fronting IP استفاده کنید.
من که با سرعت بالا وصلم</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4104" target="_blank">📅 22:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4103">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4103" target="_blank">📅 22:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4102">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این 9router واقعا ۱۰۰-هیچ freellmapi رو میزنه. شاید کلا با همین بهتون آموزش دادم</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4102" target="_blank">📅 19:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4101">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یه گزینه هم داره به اسم disable ai
هرچی فیچر ai هست رو غیرفعال می‌کنه توی کل برنامه
اینم برای عزیزان دل مخالف ai
😂</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4101" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4096">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ezX9Yh0trLYoh9YWeLDO-SmnPo1rPbXXPu2R1yB4APKiheiIZEwUVBuE_OE0hqtllFWBq9qNA4e2F7XWesz4bLQjjnG1rhe-e--bpUf-_tmvzHp65FK7lWpyUaq_TIlFY_K7vqSjoJx5oPzmc75DDjtRsSrhbDne_09eGrUOlSBu4XR5RKvWFsusuITRKdknNnBfgzMjGGjlROAJHKmxGrZTjhCLah_iG2FbnbEgNx85xmQeT0bkrp0f7uE7-t_IisuqkcLG_tLSzfEXbvOhjmI8Nn4f3VKI8ONJ3tBv7r5I1vUuFyQWCSUwCs9t9giTzU6uHtZ23tR78z_tA6y1Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bKrMLLcGFdQ4NRy8ix4mRaWBzVOB9kcURiV-T5hPVy_RC6bzyO3SsPacn5leRbYGOMHEE8NNj23qnqGbkXodrJ4zVlZIcVCUq4Jm0ivQv6l9CVTXyyMk1NvP8NhDD-c4t742pqqY3cxEWlNKLQV21m93ZnZtQhfKGK7dnHVtFSNThCDffy8b30KfqM_Y3Aq-27qTOi4vjx3Wn9EjlsemxbIKf8kIog0AkCmxHo-u4Lr2NmEJV1KP0Xk7O_kPwkdgD3EwgLBytBqt8FrmSFzqEMS-57Tgwm1vzHRwuy7KXxXT8pyahnEjKz_7gQv-1uj0ViIHjh1T2uWz5P4Vu2Zdiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bB9vobyk5Am8tXOv7moHFeB-MDQUC1I4ysE2fGoybQmHJ50Li0-0bMBFKEVA2XpbdXScn8l-UNbX1QUlPZkidWzNHEx-WfUj-F_jNedV8x-ikgnN60Lgo8MSsvVx3XYs8BBrnEoy5vWx4AFB07BoDCKgag2qPLYgLtexU2IT5K4GYMyXqRwnHSKbjVa8K5daz-mTDM_fO1DNSzEKTq4FE0jj1X9Yh2hqgc0iH_8-Af6XzSvZM-_qvex0HOwY9YnIXA6QSFQ65U6e8cZ-LlFlzDThPayoeOb4GUg5EbEiQ8_5I5nNLzac_2kiYDWslJROLmST-FpYgbj5zAFtjTy59g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZbBURMK5SyKqVlXOXcXKrQdP9Uticty4mHmQL8-AY-wBliOy7jIZR_y-IJiU5PRh3ZcwPb8m1la8Ic7U_eP13EXb75rWKOLyQQsjKDkV8FNRPewKnyWp6maDW6cF5v_6CxYhjjjWYxeAVTUVNgYvoGwGOSnfcxbJIh6RHJRZzGhbZ_0yNTJrmSFqYtMHqr-tolRJ76FxDHhVCECF9M0yLR_nuVkBWHx-OSkXYhTof3M64CAnF8Gw6Eoh6EEdeqCutCuuwEdK8WnzPFhm9waWRiF2dKhFufN92rqi8xiqSsSUwXuSUJcLKGMTiriJFIrR5Rmx0WcZ9tk3CohcB9oLLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c-_alOKErbDq8DpIxubCOWxHdxBs0fe71Gjg2T5T2F9NYD13eSyyXi3JsRQ2OA3Sgi3tm1oD02RgRNQ8K318vwj2BI2ggzEeEUkyFQJdLdhSrg0pYptPuXPySv4KhGqN3CmBsvHycF0EXkC5kQr0xJDKKx2h-vRRlu9ax3thi6PxeBB8jrSGNcNU7wJH8ojs6Dolr27OIm7AOYgJkQDIvGSb1AUoIMHEOy69u3zxtztmrfL32m2piLqtFbWb6Q9Y0NwGRNbsfccboz5AfVayZfUXklI6GbETy6L2fYt747SAHtGmxtUoyfMoq6RB0dfrgNs_S-ARZlrQnqIlih7l-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4096" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4095">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-poll">
<h4>📊 بچه‌ها آیا نیازه من یه ویدئوی کوچولو بگیرم واسه‌ی طرز استفاده از همه‌ی این ‌apiها؟</h4>
<ul>
<li>✓ آره. بلد نیستم👍</li>
<li>✓ نه نیازی نیست. بلدم👎</li>
<li>✓ رهگذرم. دیدن نتایج👋</li>
</ul>
</div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.   خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم  در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4095" target="_blank">📅 15:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4093">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Acj9XcdrvsYWsaLuhI6AiXkoZxG4fGk_y07a1LLOt2eqA_NEVYDIpuDGCzGQcByY4NTQ75pC1jDqcQdKeUOicO6pti2uuIN7zlKKSXUZbAjvG9tL3_JkSu6C5DDU4zwkpbE8lezmI77R-a2ILMD55vwa7SE2EV5cPZw_OWvMbi-vTGK6OLLIuvMebWchRUqPE9i7IKFoODc4cerEybcOaD1t-NkuGhAcq83-S_0kBOYWzm6liNcE1meKUx4sHFafDWaP041h6ui_zx6RMAYhU0NibBQrc6wRf_JMlrYhXvfzpK9Z2GMGa0AcVm9c4qebNzhGf1uD6pBCan4gMkAmUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ue7Uz9lCOM6UhydQz3TpXlA1RlJrpHlTeyMjpb22_xcLAkJFtHmBgOzvfR7a071vduKtn8Z7FkU9aJOJ0LsuOUKPyBc2SgK5eY8GqjxiS29eiXsTNWPAKQvtkJGVLn4FxKMx6rjgP9Ke3PklyLqbQPEXAgYdy5GY3KYe-6fxoW7X5o968gcqVRpXHueu_gdP2Crvy4bXGsV8Cv68LC01XJaobY8ABJ2IAMD7gMghylnzCsqL1QZwOy_bFymyGQg6VIWlmeOTy0WSbGSNTIYkOHxE6R4pT2YEjtbNW7ihFeiyr3QEUv-VTVnzomHLkv1T7ZCdjU4e_0qzR-kn9pdgCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اونوقت واسه بوفه خوابگاه ما تو یه روز 30 نفر کارت به کارت میکردن حسابش مسدود میشد به خاطر تعداد تراکنش</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4093" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4092">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iheeRVNWkRY14KBMl2WUBvWBQ3_4sF_PtXWZApth68kGuWpi6JzKnWb8S5kQXCJAEJINnP22LJtLh-gCM9OVH69-vaFpk8SC5KoyQQhVDHV-aKC11tXJsO5_TYWdK-CISXE0eKbpUmg29nhBMYOD8hBUImsC20ENdrpGhjXZ9Z1_L8EdwnP33zLJEZe6pD2QTVfV7t7kI29KZ_9Bb37E-PMIkcOdUoCSWbN1dcnN4g5lAJlSKszb2b4xPobaNHwCdOiiEnkeXgXS_iBahYg7hhWp0FGbmY33c97bH-klRIy9s20YpEcItag5YRxIge2ZudCc5eb4sdZZsF7LmxNF2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.
خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم
در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و یه رفرنس خوبی درست بشه
این لینکش، big pickle هم برام درستش کرد دستش درد نکنه:
https://ez-ai-access.yazdan.me/
✍️
Yazdan Fathali</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4092" target="_blank">📅 14:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4091">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">به قول یکی از بچه‌ها انقدر api رایگان پیدا کردیم که حالا نمیدونیم باهاش چیکار کنیم
😂
چندتا نکته:
1- اصلا از api های رایگان روی پروژه‌های خصوصی یا حساستون استفاده نکنید
2- هیچ اطلاعات حساسی بهش ندید
3- توی env پروژه‌تون، api key یا... نذارید مخصوصا api پولی کلاد یا gpt یا چیزی
4- حواستون باشه که به جز شرکت‌های معتبر(مثل خود شیائومی که mimo رو رایگان میده یه مدت)، به هیچکدوم از بقیه‌ی سایت‌هایی که api رایگان میدن اعتبار و اعتمادی نیست</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4091" target="_blank">📅 14:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4090">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jsFTzJTlliFpjQW32ZiOYq0hkE23PAPdj6vhMyPhrRqIL7J0vluT3vXC2WVNLDaa0YvJDKCfG89usPVQ0GXI_-_eqFwJUc7sHDPPz_Fb86he9rlrAIhymkGeX0YKJyQTydMp6L38BkiDg3Q_tuGHiPR8Uk7Ol-UHxvxsSvOgU7Iu113RIebHu37IPAv9Ua_cftg-diftqcLcZ8nXNt3NtCreOCf4o4RISL6XM6DfJXh7a5y0TZQxK9gzcM8FUyVQRKK-DC8hNxauyXPIzKTMMZKm8teO4_36Exl7FW_6j7W5Idc8XYV5SzvwNuV1oJ1FQOHLhWadhApluoBTJf2n_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت بامزه پیدا کردم تمام اخبار جهان رو با ai رصد میکنه. اوپن سورس هم هستش
خبرای ایران و آمریکا رو هم می‌زنه درجا وقتی موشک میزنن و اینها
این پروژه‌اش:
https://github.com/koala73/worldmonitor
اینم سایتش:
https://worldmonitor.app/</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4090" target="_blank">📅 13:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4089">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4089" target="_blank">📅 11:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4088">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UlOqnRkl4FrrPgokgrxcSUaQ00jIsolEuPlfNb1p2bQRb532vXdQr3m9fPVKa1hkLN20SHpuLO-INuQZRe65vIi_S0Lt8ueJlX_hP81ulAzZVfHYwpSym3qYquz7Kq50eHOPU44ZLXUEZM0tHq2BW5XHYdO8Kqdsrikh_VAjq_hhLsdGuFgYOJaO0cOT3HqdadFvWl58uyE0udpeTsITB4b_tcldq7gpVSwfiyMgDzDIeYFpSoaNowvKqYxRZRuktRziqDPCV04ald0OHMmPkcTfR3PfLaHxZdaEQau_iwB3IzG8IHzOLYS4LmGyiPefEWQvzdfiNmgeAw4AcZVEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم علت بن شدن دسته‌ای اکانت‌ها، چیز دیگه‌ای باشه. نه فارسی حرف زدن یا ایران و... .
به نظرم مشکل یا کارتی که باهاش پرداخت شده هست(که شاید کارت‌هایی که batch payment داشتن رو تشخیص داده و اکانت‌ها رو بن کرده)
یا اینکه علت دیگه‌ای داره. چون خود خارجی‌ها هم باهاش درگیرن توی ساب‌ردیت‌ها</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4088" target="_blank">📅 10:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4087">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/4087" target="_blank">📅 01:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4085">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یادش به خیر یه زمانی مد شده بود می‌گفتن Prompt Engineering کنید قبل از اینکه با ai حرف بزنید و یه سریا دوره برگزار کردن کلی فروختن</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4085" target="_blank">📅 00:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4084">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P7vVHAXAtK_Pgtmj2TM6fHIP4z68iqBuCDtr4_cj9dW7Qq8I4zF7GplwpAfAMb8i80Fv2WQWmM1RbdZ9ayhP0W3xh6XovukvwWQKDVFKDHxdRTPwH-6CBZ3pBWqOFHuVC9EvmKwLAEjkBU95v6AA0PjJp7G3Zny9FUSOHd6BGqu0MY8LUu0bJmEoJm3SDSHArY9UUG9F3Rup42WmDc873KW3OPgHPKNm43-RZglhlbkf2Gx7VZPsM8TS6MUvRprF7etqImmF7s-_f0OjkjFH1dZvSz1mA3BWtbyIKwOi1v5MkpNzs3WrcRlHk5c1qur0BAW4K5Ko8QH2QhCdtbxmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید اعتراف کنم وقتایی که حوصله‌ام نمیشه یه ویدئوی یوتوب رو ببینم یا وقت ندارم، میدم
جمنای
واسم خلاصه‌اش کنه
👌
attention span در حال غرق شدن</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/4084" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4083">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:) ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/4083" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4080">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B4Eh39Ggjvq8yIOMwxGWgbFslgOZQqEEfhaIFHROe-wgYVJaLBv7w-B0Ju0imzc7c9tyoG91b-Dy6wYvxJkwdOMhnV2v5l1M_btx2XrBzcTZfRRmEXSdc102IZ7O-WGto9leyHvIJP5l6Z5vwltBX0LsvN4gw5LjbhlRGE3XXTgAfggspBv4FQ18CVGnzI1kAy38hN_wprV7cOgxEfrId0RkTeny8EWHUi_pPrLdFvaY9vFxnpqgpCFkcLV9f7Hu902XkyKFY56Mqc_Lv2Uby5OjgDYnrs09S6tUIL70ffe0RQlL9MWaM73k0BhN2ScxHfig2LKsFUDltYVHs4g64g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fOIqSVmlhAisQU9YZrSgazoHmdI8r6y1o84wuekxHhDbfStt5Wkajm3zR8W8AlE61wVjEHLUQ-8FUZslcaKCEgcdUv_6qfm0QBU4I29RrDj91-Cfp17sejz3Y0O-bF2a1LnnGprQqSGijofhlupPrs2j6xmBQIQfMa-5JH4a6seJmRHHhNbra6pXPG6oSap2pmwNOCFo1Dvpy6YqdPTXZ2So6hQPnWqb6oadNbqDLRKxcrQ27upR6W1rjMArjsImalZa8xDF0MfydvSzU_dDPRdUr5Ob0707IfNKy8yCxje-Gsna__FiBcHc5rGHfxlSFQ6N9-BrdZgMk--RQj4Lpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nOZ1v6Pdo3D9JwOEsoADxbeJSeVqo4g-kgAFD-MReR-2JxjWKM0ovcfLE1ImMyah78BB1YeOgYGBvY0L8kASTlqsplejd3VvAs9xbHFahMF7SpCzoF4wkcwzWkSh8rwRlcp04EkXS-rNsMdzbVemBDOCTD-1pZunx7LWumKcP0nxnosB0YMfxX0MtQWO0GXZIf6iRjdqBKtFbmH6dqE_olpyQURhLE71I-On7ArB5Hjm7ck1dy1ByscEV-2xaN7PiWzb2Q0jfV46fN97tCs2xdFpXHTtHT66qMRjs36MqfsEsnqKqerkTAHrdtcCo-TkQg07eEF5zFOQGEz3wtdMGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:)
ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید نصب کنید طبیعتا
محیط داحلش هم عاری از هر گونه حواس‌پرتی و به شدت سبکه. به سرعت تب Git رو بالا میاره و تا اینجا عالی بوده</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/4080" target="_blank">📅 22:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4079">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اپل تقریبا ۱۷-۱۸ درصد قیمت محصولاتش رو افزایش داده، اونوقت فروشگاه‌های وطنم نه تنها قیمت رو ۳۵-۴۰ درصد کشیدن بالا، بلکه سفارش در جریان تمام مشتری‌ها رو هم لغو کردن تا مجبور بشن برای قیمت جدید پول بدن. بله ایران درست خواهد شد
✉️</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4079" target="_blank">📅 21:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4078">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hCtMqJIRqAFRUQs3YyG_aWS_BEzhrLPcrByYsOKPWBSXrdV80Sc9W574eUXzIfeqGQpjWxoX7MGIpcjwSDntJ7aCBBl3H8EnHSh0Kf0-YF632hCl3HgQfx8HGOJvHqAaBFhB9Wj_4M0uHMzvsA9fyP2ET0bch6ltSgT3-8FuWl69f45DhsW3KDF40Ue075km9Fs3KMVKZBEBOleI8RFZJKD80teHzNAtouGH9jV67TIyff6MdTJsyux7nXVripJNbDahWC9H12Mwvw3hOYDlQDGtIg-ufl8V0DYkhdzCRqGy-zyaafov9g5n0-KxDtOPQcu_PpSYhJurT7CfReZbXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/4078" target="_blank">📅 21:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4077">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qmiexP5IReMuA268Fvf9PxLqShcfaD4lE3i9NaFM5oLSDMd5QxdQ7k2LUxy3hU_pdlJUmMPslsM3XJUp2Tx9aCii5G9n0QMAq3sIM1lnoiM7Dg8Xn3zsrwLZXukvvN1yJ5GdZzNzml5bNZ1cYWfxzD2kh88RvKSZ1ado-fBTnxNZtFseJtixKIiPVv5QoniYLbtq2IaGt8YmxGAgTL-uxkoPhB_82d-Z3l6Q83R0DqoHddN7AsHcu8pcde4OCskvCiwBc4vus5bZPr16DH3ZFBRPowEc_bZ2aqMj3b5wD99Z3VoPWqk9y8YyFSFaDgqBqrzCkLt4SS2xe_l0q3BEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4077" target="_blank">📅 18:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4076">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fTPZYLf3iU0pJ3btArkn9MyS3xocfB3pevMy84WJXDb3QvVp7j8DA5bpOp-eiCowsOEgy8rvL8mvAhlbTLotkbn0tuE4CeVmuGzz_AMJQcs96BCOGxg62BfFS8XMzYgIEVDu4XjaUwODMm0XrYmyw8ET1gY-Iu0bwQJwulGtpsjA-VjvZ7J3_HGs5nM0qw0MEaUS5V71mp23PUa3dPL_2AUfvr_elcswMx9LgcF-pbCvDFdQAOGyhQXGcvJjuIq_MtHCcgrnDUDfCfZ2A1J7C64h-O1EGyk2Jlu9dshSzC4aYBOwSYlmdsWnH4au4J8AdIXYr0fmec3PoYRDIACqnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده.
به شدت هم IDE سبک و خوبیه
از اینجا می‌تونید اقدام کنید:
https://zed.dev/education</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/MatinSenPaii/4076" target="_blank">📅 18:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4075">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=rk5srUpBO_u_CNrD3F16ldDfUrTnUepaI26DZKUeJwcHLg1xssCOgz4ny_GiTUHfhpDQ5LKHONuFNg-29uEyAxllQKHrn-LTKnh0Z2k7Vc1o6zaP4xZ3AsogCcTu9fe2_T-mBq2woeO1PY0AmkQQ_uIQDkX7RpIDjISJPvozGyKGAuyCkMMBIGTQ4WQiqkZjEZqS2F_ZaqhKbJpe66GQxK14fDOSNJquVhd72EWdLRPSCmv9JCIO5jIVd1q9-z_QzxE7whvackclM-VSOVD7W5lUHz2Rb5jmk0v8ctzzYDiEKc_TxX6TcznWC9qh28KafR2YyJZvvCU6kwnU73Kkgw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=rk5srUpBO_u_CNrD3F16ldDfUrTnUepaI26DZKUeJwcHLg1xssCOgz4ny_GiTUHfhpDQ5LKHONuFNg-29uEyAxllQKHrn-LTKnh0Z2k7Vc1o6zaP4xZ3AsogCcTu9fe2_T-mBq2woeO1PY0AmkQQ_uIQDkX7RpIDjISJPvozGyKGAuyCkMMBIGTQ4WQiqkZjEZqS2F_ZaqhKbJpe66GQxK14fDOSNJquVhd72EWdLRPSCmv9JCIO5jIVd1q9-z_QzxE7whvackclM-VSOVD7W5lUHz2Rb5jmk0v8ctzzYDiEKc_TxX6TcznWC9qh28KafR2YyJZvvCU6kwnU73Kkgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/4075" target="_blank">📅 16:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4074">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دو ساعت برق رفت، گند خورد وسط کارام و تمرکزم و همه‌چی</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/4074" target="_blank">📅 16:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4073">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/4073" target="_blank">📅 16:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4072">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sAvRrmJ8vZAs8IQm67mHl0f0dcKjTqzo67OQfe4kwVHMoEBQtbccX_PecP3Jh7SvQK2KrF5Ok9AEqZvpEVcXCzG9f4Cfnzr_e5rmfwleM--GmT-Obvti36UesPdSUU-ybnapEsb48qGfWXGusP4zQpAawVOAj_lWDvoVTqNIPRMfFL_UEdNERHr8xb8-2wMTojkutTCZEqla3YvuWdGIKa6tWEKnt3OTcd9wCbYCJk85pn1-6W5lMlSmZUFIl_Vk046GZThO9vOQIrPiZCb2_yzaDgymI9lbaGYduikNngl6dKJWOZtPffnVCiTMBUigyUv4zVXdtMrXDB1A2aLkEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور  /learn  هست. به‌جای اینکه بشینید دستی یه SKILL.md بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/4072" target="_blank">📅 13:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4071">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aJXK3p6IiCWJEzash96mMTpDWQAoPF7KGD8z9MucWtvHNn7VYuU655W7P_BVyAY8R_lR2tJYeGC0EwK8rScdU4gb-4FO5pfyl9Wz_Ku6gNMDxkCZsEJxkhg1pFH1_SF5VTMTGr-Z59Shttz_Uy7K53dSAlT4bgyJE2WulRkW9Te_x_7YoskjqkimKPeBdp5oOho3HFstRdEsO7CZUa6Omkpghwrq_r7Hpq62XfehAt3HTx0GcKYcFB4GTlIxrHQBOmqthBiQpV1_Ygu9kfD9PGN333JCHXJqTeOAwvPFbSO07IioQhVne2FJPfiPACO68zsuxNhmF3fjh2cKL07jEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4071" target="_blank">📅 12:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4070">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">از اینجا ببینید آموزش WhiteDNS VPN رو به همراه آموزش اسکنر اندروید من که پدی زحمتش رو کشید:
https://t.me/MatinSenPaii/3999</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4070" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4069">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4069" target="_blank">📅 10:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4068">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خب، من با کمک Hermes و API رایگان MiMo Pro 2.5 و API رایگان جمنای، تونستم یه ربات باحال بنویسم!  توی لپ تاپم کلیک میکنم روی یه اسکریپت .bat ، و رباتی که با mimo نوشتم، فید چندتا سایت اخبار ai که به صلاح‌دید خودش معتبر بودن و زرد نبودن رو، می‌خونه، با Gemini…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4068" target="_blank">📅 03:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4067">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZCLTQPQXUYFzha_ctIj_wBQ8XYf9V98KY6Puf15iOOZc6iva53pb4JBykjxFQexan1JzRjRqjMYabQ1ytxcOPFtGawqtTh2A6VXplbBB3FF87Fg6XvKMjCtSztx62y7DRu2cdBtuo5WmyqCG6jzTbvDLoO20b0Artc-b5DfpBwfCmrlXcqiTiv8dcNX2HZwuPcjzfZDyw6a85_Hz_gn_CfaknGbFFe4vZkT-9HAcNp5lZ8paq9yTLMPjA_Kodfb2GXoCDryett6YzvFqDHx3Bu80T3mTZm66KP-HUrigv7l-v_YkSM6-zUA0LTha_lXHLvWPg9V11RqMRxB6kSM4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر از اسکنر من استفاده می‌کنید و مطمئن هستید که آیپیتون تمیزه، حتما تیک همه‌ی پورت‌ها رو بزنید برای اسکن. چون به چشم دارم میبینم یه سری آیپی تمیزها فقط روی یه سری پورت‌های خاص کار می‌کنن
آموزش اسکنر و اتصال رایگان به اینترنت ازاد با سیستم(ویندوز-مک-لینوکس):
https://youtu.be/JdNeZnclS-s
آموزش با گوشی اندروید:
https://www.youtube.com/watch?v=2otJfXgNWCM&t=70s</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4067" target="_blank">📅 03:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4066">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4066" target="_blank">📅 02:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4062">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IpIOupcCTsqX1PF6XOhW8MFgngCMfrOuqjeFiEoD0sqwobpvJtOQIYuC0fqjmybqvD3t51lEwhZW5HU1CBVW-FvY4dId8n-eSy5qX859Id8CPJc3E_HR8r4X6bFtDfsYPdzGX9ffL5-zuwwymrF6aaGQnpkp7_jMoi6wXBvSUY7VxnCfx40S_7S9xUMdN6HIlhZ-OYPodYKUe1PCFhG6TCyWZl8xPpk4AstoJbLIIOxyL2NpvyEQ4eaYHPpHzszB2IO5rhoWBI6JcdMB4XfXyNpUbuhQJ4doMjMQD9TDqIj97KCaMWdlxBifjcDfpvg4eU7ixhUX3otORVOSyR341A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IwjdAjf2Eb14iB0mi1lZBt9R2cNt7L7uajBrqPun1rN76iMKZDcuDm8U7ZhkELb9jzv-9pAoWDU65BSVZF0xzHMdJLSYoAgy3Lf-uf7W4Y2nMdR5STCm2RnVmh5bykLAAG6JLFFNzp2p1fRF7NTlYPreLAywANBh339gEEsuXY1fhkMttezUswFVV01kRMZTMh17y2xAAM3LSi8xHDR9EkJBYwY65M6NdjREBjH10ORvJpqpB6eoLygyFWV2qrq5UCiYb0LN7QVc6Jf045Yb1wKb3aCaKRoPEPEr-hyw-cWVMWtHLHxSWqkGMXB103VOslBoHs8KHILfstw5zoe-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dG9_NXcftnmaqk6bVq1oGIa1a-OTWPKuDgVwe0Onsti7QZYYb1HfrWFWEmf2Jn1vgCIJTlgcMOPoe8Nxcbq9Z9gXEmdcvYZhqueE1IK4L6FDpvI7POMQVjiMrXCMQZCWBNZIvbIpdjt0Bah5JQA23lS1-9SZwDZOAsUn9WrY6KBeWm9znGkalqYCX7wqDN7IOCxA7LysZ584bO8KtRVt_t3ks-DjLgT_l9JtVO923hRpbjWfscSwM7vN92Zno1NLoHA7UOVUv6WYu_ghILmNT-4aRASrtz4OsD9-9M1_qcaLh6yfwi1X_-tlWGq5heHyw17y1-5NZJW8KQv-JDTutQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cMMnx5oPdUh0DdiS74yyYF061iiXJHo-bwashkXqWr9sLhkpytVoW-YiFePEbwrNMLAlP_5UxmNchUxTkMyxKJIjSyxFmbSocS3po6_3vm3lQ8EvhwJrX84kGVxpBpCjGLzmZqQ8dCQCm6jBM6VU1kFVMqfg0zSYLlBE9Vqxqh1XFXYFwd72_c9yiGzmv-R1MRx86sRkW_L9JRzZtnHeW3FW5Zj4Z6-9vShLhaAbIfcPC6g5PN-JyEGDx1f9vcyB6e7sEazmMNBUKPxKFmsThUcgcn6s-Af62VhIjLlCGltJ2SvNIPdPW8qHKhlFzLF-g4GIFQhyb_lA3y40tdCwsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4062" target="_blank">📅 02:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4061">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/augjQ0I7f52wq4Rja989ROz_2B0MZOZJTunqKw2QBfc4fneJXiHQuFAMbzYDA8HzPkatb6bfDE0WLiPHU1Trzqi9Wa6NKwmCED5bgkB-ZHonU-xU4LwSYv5nhaBNJsWanyls3b8BzVRroBgCZcAPJh9KGuu8jgw7yUqr2uHvwJ029S3B-l0In22u5W-hBKQmaDhEPJC8egaX9MkyMOqdwOZC7Jtm7eJ-7R9CspvKInDF5WZ11OzcUVI9xmk9vna9lkZziIbTbEPhlYPSbyhDP8ElWFuH1cja2o3oGn_VyXAxn1QVVjCCXUnJV4nVLVOCir8eeikLkpOGm1IKNbERNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه!
یه ربات خیلی کوچولو هم دارم می‌نویسم.
دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes
خوبی این سایته هم اینه که روزی 7 میلیون توکن رایگان از Mistral و MiMo Pro 2.5 میده و هر روز دوباره شارژ میشه. نوع API هم open-ai compatible هست. اینها رو بعدا توضیح میدم برای دوستانی که متوجه نمی‌شن پس نگران نباشید
از این لینک هم می‌تونید ثبت نام کنید داخلش:
https://router.bynara.id/register?ref=PJ6RZMDB
رفرالش هم چیز خاصی نداره فکر کنم، صرفا اگر بعدا خواستید شارژ کنید، وقتی با رفرال وارد شده باشید، توکن رایگان اضافه می‌گیرید</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4061" target="_blank">📅 01:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4060">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مدل پرچم‌دار GPT-5.6 Sol برای برنامه‌نویسی، امنیت سایبری و اجرای ایجنت‌های هوش مصنوعی بهینه شده و از قابلیت‌های جدیدی مانند «استدلال عمیق» و استفاده از چند ایجنت تخصصی برای حل مسائل پیچیده بهره می‌برد.</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4060" target="_blank">📅 00:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4059">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به قول یکی از بچه‌ها یه چرت می‌زنیم بیدار میشیم می‌بینیم ده تا هوش مصنوعی api رایگان دادن
😂
چون خیلی حجم مطالب زیاد شد این دو روز
به زودی دسته‌بندی می‌کنم و می‌ذارم
همینطور بهترین‌هاش رو(که زود گذر نیستن) ویدئو می‌کنم و یاد میدم</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4059" target="_blank">📅 00:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4058">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اگر مثل TTS اش بهش چندین تا لحن و دوبلور اضافه کنه هم عالی میشه. که اتوماتیک تشخیص بده و صدای دوبلور زن و مرد رو تفکیک کنه. که در ادامه به نظرم این کار رو انجام خواهد داد چون همین الانش هم برای بخش پادکست، اضافه‌اش کرده</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4058" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4057">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود! همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا. دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4057" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4056">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=U-jf_zEBecCiUGqLte91fLc8lNVhyJNujhCI4ZT7dJOwjs5Dm9bsVhNSaS8yifOGkDhTPYaNrEb_cFC4g9GUlZJfzE5BkLRFwBi9J_xj31aMumc8aMIqkifMzckgi4sE_OxzjIaF4DCUkndR9Z3hY3tc2M_fgx812XoP1AZBEOyZmtzVlc4asLt_JcdnUK1DHHKtFq34bgtnxCZZCALUQ6kfinIggvCPoPkxGNnJKoWP_Ui2ADM-8f1cmqGf1zD6aldzpRFCKDrtLRMAhuqoLqy8qDmTd7kDre31_xy8mfZA_LLfG-AsxM9CC3Y4GfG-gmu6528T682gvXtD7Z2iakemJOZ_23h9pTNfrZZPG6SSDo8GoId4sU0vQweQg1NIzJ8KA-Y61dtnGPWASi16h7lwmLOfFBZN9awIvTwc9MPhxgaqmAPm6f5mqi-vFykHD1PuH-oTq0Dkg8mlYqnzbmGCvlJzS4KLm7KUXfzQ4dCDaleVBJxykD3RzwtwOC6zQbRZhf-I-SfXUqFLksJaOND8zGgPMOw845UY_dYHh8Q9nCeYqTv1CXe3rwFjr3IMFRQ9F8J_x-jSNGMNzXdS-3iqw6--uWRvSFyo2z9ontM5Zef1QhPOHFJqaHvHe5Jc46ig3S5C5GlBE0fdlTj6CnQ3FFq4kdlnJE3AF_yYjp4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=U-jf_zEBecCiUGqLte91fLc8lNVhyJNujhCI4ZT7dJOwjs5Dm9bsVhNSaS8yifOGkDhTPYaNrEb_cFC4g9GUlZJfzE5BkLRFwBi9J_xj31aMumc8aMIqkifMzckgi4sE_OxzjIaF4DCUkndR9Z3hY3tc2M_fgx812XoP1AZBEOyZmtzVlc4asLt_JcdnUK1DHHKtFq34bgtnxCZZCALUQ6kfinIggvCPoPkxGNnJKoWP_Ui2ADM-8f1cmqGf1zD6aldzpRFCKDrtLRMAhuqoLqy8qDmTd7kDre31_xy8mfZA_LLfG-AsxM9CC3Y4GfG-gmu6528T682gvXtD7Z2iakemJOZ_23h9pTNfrZZPG6SSDo8GoId4sU0vQweQg1NIzJ8KA-Y61dtnGPWASi16h7lwmLOfFBZN9awIvTwc9MPhxgaqmAPm6f5mqi-vFykHD1PuH-oTq0Dkg8mlYqnzbmGCvlJzS4KLm7KUXfzQ4dCDaleVBJxykD3RzwtwOC6zQbRZhf-I-SfXUqFLksJaOND8zGgPMOw845UY_dYHh8Q9nCeYqTv1CXe3rwFjr3IMFRQ9F8J_x-jSNGMNzXdS-3iqw6--uWRvSFyo2z9ontM5Zef1QhPOHFJqaHvHe5Jc46ig3S5C5GlBE0fdlTj6CnQ3FFq4kdlnJE3AF_yYjp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود!
همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا.
دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه و خیلی جذاب بود حقیقتا. مخصوصا وقتی که بخواید با یه نفر که به زبان شما حرف نمی‌زنه، میت داشته باشید
از اینجا می‌تونید استفاده کنید:
https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/4056" target="_blank">📅 21:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4055">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⚡
اگر برنامه‌نویس نیستید، API Key را بگیرید و بدون نیاز به ثبت‌نام وارد سایت زیر شوید:
https://B2n.ir/newapi
آدرس سرویس و کلید را وارد کنید و از مدل‌ها استفاده کنید.</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4055" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4050">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کنار iran internet monitor باید یه کانال بالا بیاریم iran bank monitor که وضعیت بانکا رو رصد کنه
بانک ملی درست شده بود باز قطع شد</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/4050" target="_blank">📅 15:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4049">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pmaggdggc4n_LDIVlQ92uGMf7dddu2l7ipEibSzrfvTsEuHCpAmsteMJ96MPX3EXwjrtW1wrRNlqVU45B30bPWaJX6oJ46JFMhyxBtMxC-3pjSR2rde5zkCHvrNxM_Cr9vfi7xRtDdavEW9b7Ewzdr4WaQnk3g-_FFvQLVHjzmpGYMeQ5YRL0TrUBEPFfU4H3twDGiM6-xUjLpoGKXGThCraFwaCh5-bQFsJlYSglS4Mlm3b3gBnmcxAdFw-9rZTS-POClSPI0L9E9FC-oQ-DYrc4-NxVQkxEgARsc91_KwvPtHlNJIv27Xz3d2ACeGxEns7fF5S08W3kXfNj9pYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویکی تجربه یکی از معدود گروه‌هایی بود که بدون هیچ وابستگی و فاند و رانتی، محیطی رو فراهم کرده بود که افراد نظر واقعیشون رو راجب شرکت‌های ایرانی بگن و نظر بدن.
سر همین خیلی از شرکت‌ها می‌گفتن که کامنت‌هایی که راجب ما گذاشتن رو پاک کن وگرنه شکایت می‌کنیم و فلانت می‌کنیم و... یا حتی می‌گفتن بهت پول میدیم، اما قبول نمی‌کرد.
و همینطور یکی از عواملی بودش که باعث شد آموزش‌های من به دست خیلیها برسن، چون همیشه مطالب رو share میکرد و با وجود هزینه‌های سرسام آور سرورهاش و شرایط سخت مالی، توی قطعی نت کنارمون بود.
و آخرین پست کانال تلگرامشون توی
تاریخ ۲۷ مارچ
(۹۰ روز پیش و اواسط جنگ) بود و همه نگران بودیم که نکنه اتفاقی واسه‌ی مالکش افتاده باشه یا دستگیر شده باشه.
و نتونسته دامنه
https://tajrobe.wiki
رو تمدید کنه. امروز دیدم که دامنه‌ی ویکی تجربه توسط ابرناک گرفته شده(احتمالا یکی از شرکت‌هایی که تهدیدش می‌کرد). و در عجبم از اینهمه بی‌شرفی، که میراث شخصی رو که مشخص نیست مرده یا زنده‌ست یا دستگیر شده یا... رو برداشته و اسم تمام اون پلتفرم رو گذاشته انتقام‌گیری.
امیدوارم که حال ویکی تجربه خوب باشه. دامنه و اینها کمترین اهمیت رو داره</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/MatinSenPaii/4049" target="_blank">📅 14:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4048">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R31Ve4FaZ73ZMiUR27s4QIR0hwB_zlJt3WJHB6OdmQeCYseCxZVg33b3KXcgxEufI_knE-LImRquIdC-30Hm3kjT9ZuqOKPMulvQINi_Jlkskljwyt2fJep5xSvZNPaedxwwV5hjV3Zwe9q-8PM1Ke-9mCiQhIePe7huJqnyPvxWtpVmQ8pPETyJL9xoDfO9KLqfwf8_c0WKpkoYa3dT2Th6gKwgbZEn__DA25-dyavBt8Prv_qryUIQu88eOmxp6ejW8w8UO3zcoh__yxpGjxluSninVutlQ_8quTWSNPddXTkrTu4TiNnBDdCdUTaYf88lYAjD2mKAIlYqwt92Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزنید این حرف رو بچه‌ها. شما چیزی به من مدیون نیستید
❤️
همه‌اش لطفتونه
و ممنونم ازتون</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4048" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
