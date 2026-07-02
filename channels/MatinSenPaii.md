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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 15:33:43</div>
<hr>

<div class="tg-post" id="msg-4178">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/MatinSenPaii/4178" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4177">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 8K · <a href="https://t.me/MatinSenPaii/4177" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4176">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ویدئو 2 ساعت و نیم ضبطش زمان برد، بعد از ادیت شد نیم ساعت
😭
دستم شکست انقد با موس اسکرول کردم</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/4176" target="_blank">📅 04:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4175">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M-fIpp4dC3jVfMavwVCGqD2r5pYX3MxyqL1Ap1-xTzIG3ZnKzBKNKfw7sFa_OyWDcYY7FGeYLEHukZEzZhKDvmyS-Sd6GiPJyU8izTSPAC2tjXzX7vZHhl1fjXCavIr5Kop-_CVJsqG1IcTICS43lIIjtfpNTammO31w6tZFv04Pkab668VrrH0cZ_DDWK5hE_RSu7s6B8_qwEq-uYL60B3__W8DLYOpWzBJoVnt92AUKI4kxvU3BPLGjHw8DzVO9X8uVeewj7n5KVwr5j5kQRT8Xa6KVOCUcmJFkr0doBNpAR_6RdWPPRzwMb0WBMUVwrNxnSQL4B91FIRfOfWpPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط دسترسی به Fable هم برگشت</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/4175" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4174">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وسط ضبط ویدئو به طرز ضایعی یه ۱۲-۱۳ بار به ارور خوردم
😂
(اون پشت حلشون کردم و شما قرار نیست ببینید. هاها)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/4174" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4168">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/4168" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4167">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/4167" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4166">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XCuAj5ceaDHAq3S2agIGIAcZ9WcbbUpR0QhqSbe8-MqJ1j5qheUGTpcfSlIBxr9j_9K0UGP13DgRYxZv5BpJEnKw2B_3oQEVuic3rfJYMSQq6_R1qarXtH63_0SxqprpudsGChcvCszTj0LpBT4y48z6xr7WBaJgC4MCHaZ9v2xv4YvtqkWaeortD_xMPAlNsybzhPe_JbJp4A13pVL18Luo4_gkkVQ2oHDBYOl9aEecrEAoglvPFjkbcI5r_mg2JkXtJvfWm7gNXvZReGlWUJDuwhEIn3zhAhxTebt8QXdLTm2kfwgiSo4zGSWrKix-cpu25J5s40gb20yzLlMOfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این api هایی که Nvidia میده واقعا سخاوتمندانه‌ست. 40 ریکوئست در دقیقه
با 9router انداختم پشت هرمس، چه میکنه این Qwen و MiniMax3
توی ویدئو آموزشش رو میدم که چطوری بتونید وریفای بکنید و ProxyPool هم بزنید که روی سرور مشکلی نداشته باشه(مثلا با آیپی سرور من مشکل داشت انویدیا که با یه رله کلودفلر حلش کردم)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/4166" target="_blank">📅 22:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4165">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4165" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4164">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EeC09xEtvW44xDS4XyWkLqbEzaOgDOZop0J3JUEYWYeDPBQtQfHOpMvpQMQJLqe9j2arjadaJQm5ShsjyoA1kbsW7nMLNmfDzrG1y02g9cQGQwNNArw_VglOjOui3xcSSMmoEzBH3_FMxut3xx1cGywCQiY7X-YvGso2tfjvD2G8h82gxKWN0AJrnj4Y125UwiKIRnxYCLaEPBdC-e0NIA1J0hzrQucVBP0UErZg-jy1WWqCF_0kKAk9Xxmp1uu7Nusx2hKQPYLoMh_zPhndAw208YYttG-2exSMTLwcDpfz007dDN5GxvCD1cYplTvfXihDx9RXyls8pZ4pvyb41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی زیرساخت‌های پیچیده‌ی پرداخت هم بشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4164" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4163">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">از بین سایت‌هایی که تست کردم برای SMS، کاوه نگار که باید میرفتی از دفتر اسناد رسمی احراز هویتشو انجام میدادی، فراز اس ام اس هم که شیش ساعت گشتم اصلا بخش API پیدا نکردم انقدر UX اش درب و داغون بود. بیست دقیقه وقتمو تلف کردن این دوتا تا وقتی که رفتم
sms.ir
و همه چیش اوکی بود و 10 تا هم پیامک رایگان داد. خیلی هم سرراست api تنظیم شد از خارج به داخل هم دسترسی داد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4163" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4162">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تمام رادار جنگ الان فعاله و AI هر نیم ساعت یه بار، خبرگزاری‌ها و پنج-شیش تا کانال تلگرامی رو چک می‌کنه و اگر جنگ شده باشه و اسرائیل و آمریکا به ایران، یا برعکس حمله کرده باشن، پیامک میده</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4162" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4161">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FAqp3u4Ri_sGFCp3TMGZE6-JV_VIGRgMlBNo_JuMFmM7V7XurW-dwzFV1dfEHT5ej2AZ7hdanN5wXQOgJZUBYkQO1mZB3-SzMO2cAYKU927PymmJtefM0AOjcw-UjmTmC8Dgux3B6696ZhWrZE5gH99gq1NkcU9dLHbY_D2EY1sLzhF7aUmQtFRdChqlGBQuAjMYg46KDquYjDYOyeNDbpUzzIJdiYyNH5GliKK-Y0w6bBc8oCy3-O1dG8EmGXtWIr2NAITgOtLGY3FZ_AcA9jNfqhg_2f-MzqD3IoYrw23z1nQMp3bbCErkCrb9YjyjSq9td6bv0gszJrYeBeleSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4161" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4159">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4159" target="_blank">📅 15:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4158">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ivPw8qGNJJ_44XDsdz77ZsAq2DCjC3ObXD3V5YqShO8FjXROr--ohCGFeD00CRv0hEjOEIFx6Mh2CKU9eA8rOnKmopTSkIOfwg2BW1pgvILIzhCMglVdp_OpTRyt1TFrSiRw9iUUEsVAwnrtN8E1-Rb0x-5yCO13YnbwMxm7_G390MS9am-KIrj1TKApD8Uy8jzwGsnbFLU-mrLbjH4dbLy7Kp_ovXgwp8g4JsjRZiiSSBwHBDKMf9h525fUh1Bu3wNlhu5QaqgCnT9XuOqT3VsFQdPuIIxbUgzN41NYFKu_Fs_lgFiA6TL2Sq5cLDPvt0VdEzUtpjVFED6xubzazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی برای خود یادگیری را شیرین کنیم
(دادم همه رو هرمس با gemini 3.5 نوشت چون هم یادم میره چی رو تا کجا دیدم و هم همه‌اش هی چک میکنم که چقدر ازش مونده و الان درصد دارم و اعصابم آرومه)</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4158" target="_blank">📅 15:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4157">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">می‌خواستم ویدئوی هرمس رو ضبط کنم اما انقدر برق نوسان داره و هی سه راه قطع میشه کلا برقش، اعصابم داغون شد. می‌ذارم یه کم برق بهتر شد میگیرمش آموزش رو</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4157" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4156">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">همین الان ویدئوی یاشار عزیز رو دیدم، و باید بگم دیدگاه فوق‌العاده‌ای میده به شما از ai
اینکه دیدم یه سینیور چطوری بدون گارد و با آگاهی و مطالعه‌ی کامل از ai استفاده می‌کنه توی حوزه‌ی خودش، واقعا لذت‌بخش بود.
نکته همینجاست
با این ai عزیز دل، حتی باید بیشتر از قبل مطالعه کنید و دانشتون رو بیشتر کنید تا برتری داشته باشید نسبت به رقبا. و قوه‌ی حل مسئله‌تون رو تقویت کنید و کارهای تکراری یا سنگین رو، به راحتی بسپرید بهش. اگر به مبحث باگ بانتی هم علاقه ندارید، ۱۵ دقیقه‌ی اولش رو ببینید حتما
https://youtu.be/-Rt_Z0allhM</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4156" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4155">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید  لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4155" target="_blank">📅 13:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4154">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R7Z74pfsNSBBA7nmu2lKpsCQGlCi2LcZwjAGsvR-V2qJKWSQ0B0SgT4q_p7qmgSkYzpDqYyQdWM2JbZ4GuHOESEuvArJWPf9O8J4vINZiUzfjZcDEhQaLdio5PfMPdNTMmKb79oTJjeiBFbrZ75cqzl8Qg8BcjvBUmmARWhA9vM-k_ssJSOwL7sYkF1af4VsxEPgvCGSrtpsZvQgaXrjVjzid5TOsIJ2wUqRmpxxaqmrhQjoV7Ofa0LHvmZWj8rFhDx8he4IebTq4uTCSPTqJBIYsfsleMzjOybttZIRMCu0ufj1cmgq7oHrhJC9U5MxAeq_CU916jF0n63zw0HNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید
لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4154" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4153">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FtLUE1Nq4QxdimBGXmbRyWwg9UM9hYbHL8XiO45T-qIEwBFV4wQIJY5nIC-DIMa9k8_EotHP77leP-Gy2BckUtqaBNiAPOyL8wvoy5Deu4to1LeOR0tmC5K5flAp9l93fXzpBzZvxIluT4Y30MFGUE2r1cY4RZ7iclzGI8G5QkG1M4vZeKGcTGlG4U6ZIpvsaG5w1LNcGyGCxSaXM7iEaWEFwDWZOhN_RqlajrO-KANNRm54FzMYo9EpPSLn3DxtY2afx5RauB6rZG07okV5DxjILPHHGbhMqnkWDhcpmlJXNzyfzKoTSFPyDL6bkZmGJj7YEMbYqt4r2QCG48bT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غول چینی، GLM 5.2
همچنان ارزونتر از حتی Sonnet 5</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4153" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4152">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خب گویا کلاد Fable 5 امروز برمیگرده
😁
آنتروپیک گفتش که با دولت آمریکا مذاکره کردیم و امروز مجددا مدل رو آنلاین می‌کنیم</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4152" target="_blank">📅 10:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4151">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dpwevERZrKLD1GKqQ3cN5jTUG0S0E8tUS6fhZRl0hVVILti5856usxE79VXsFkiilcbfhMXByH-8i3HQtW3TSaFovf3hym5-FcAnUgvqT3lrhATGPSYFp-NlJzzRCJfFUbew6wi099c4k6SQRHkktdaK2V9TjAKAhuFXER23lXH4mJMJ8urRd55xCdCPSe4N992wIWoHL_JD0_Su7hZqachlb_fDeXf3ij5zFVvRtBNDdLStfA4HKWsTX-OGrAfo8RJ2vSWG5mt_p6A4g4vlDOCk4b4nyMYj2iCo393lSLC_M4Rms56XSHB1KkrVbIeKlCeAGYFiYvFpQXvpu8wgEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4151" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4150">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4150" target="_blank">📅 01:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4149">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4149" target="_blank">📅 01:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4148">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4148" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4147">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h5nQWT3cYhIZqdlE5OJWT_2nkW0Aqw-T11unkCSmbBMvH1WoLuVpwfwxjKTl36rzJsiHhxuI6ExH_HJxOT7stdPki1hKVwKToVZmLBcOyXkfrvgpuMfX-_4qw-zeD62-hLVT-QLmFfoN2fPDsy_9DOEonjsXc-KtXUtIq4HPNdSEFQVDQcGibAQXMBpmnxOsDdEyDmnVjrx4okbP05zCMwtLhjSxaNSzTTrSSFmqq-d-OG5x5R9kH_gnseCiKtq89d8lAgYSXUtGAfZgNN5Fqik3EoC3f3XJD35IFPSY-HET5hgRsiYu1h1L5PucuGlUfAsinhr6ALkUx-zl0QC1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک منتشر شده توسط خود کلاد</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4147" target="_blank">📅 23:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4146">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HGKedvYJstP-n9DRyZIJ8imATemw979I3MhUKc5LSdN1IrOJHJHvGfGtV9ffRTh1d2qg-IVC5iOLjkyF7zTkEWhoOlSG_Ytiy7sA1BtS9tYR-GkTB429R2YT3CKqpuLiLUHBihTax-P1p4jis1TnGB95-kc06QIoeGjJolA-aaeZPTMN475LVjX_rcZm5F4AzKVhJ7mAYqtw_Am-0in7Jr1-IVE0O02oYMlorBEwrKnluMQzxxL4RjH49ZTlX2MiWVA-xYlmB-x2QWUPuYo4iddzu6g4UExwWOycqoF5wzeV5-XQ6zX5Kmad8G7yngS9MVUc5bJUW_ilr19TMHGMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌ آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4146" target="_blank">📅 23:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4145">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XJprUHjk-jtJ3MiLtY1RoZLJIj5fY6Z80CaT40GwBlJynuA6Ua5PL3vVVtz9Nkhhmc0ha60MZR2vpsqryG8Qkd8jMJrFS84EaIkuwTAbsLRJ_b2B3aK6GfgcTjX7oUFOTbLSBwrEVj7QfgBIAEfh_uJwN1Y4gUbJBft65zOQdNcgWB7uNyM6WXA9U879QCdAx_oVy4Lv3yMP3RKVkXnaaLeMm6_eviyn9uUIgM19vkGi1M2y7vA_bfhw6zfFw--JvKQoYy40GoE5_dCHSS_xJA2xzyjo98koI4SjvBReags1BF-WnOjmcsDReEC6_7r0se2z12Sl4fnlgfs6Zte7gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌
آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4145" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4144">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!  این ویدیو…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4144" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4143">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4143" target="_blank">📅 21:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4142">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M_mJbp1ydmkHyexKeIGcrgGkFcV23SRD-KSMf6eeWLCNal-IgAZcmyaVW9RE8I3vsNHdInOMxLWzbkPrINAeZhu-_gs6lpeciCVRj8xyZTbGnOxyVIy77KmrFTaq2l55w7OVnIcLZzQwhRHby8d3qkQ2XTOQ_GaxyahJAd3TH3HT_j1M9FaPyRVEqpLgByU1Vsit51LABeSQvR0VqtZjCSWQHfDmkaeio2z4_6e5PJpUlMc_IudGU0Jig2riGwnKUUi2AnkjcBPl6wi0t2SeEvKr0qmEmhF6SV4bjpxkCGxLmd896yaeMP3vVih_hQ1kgYShRa_Q064f2in1CF8tHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب یه قابلیتی آورده به اسم Ask پایین ویدئوها، که می‌تونید وسط ویدئو اگر جاییش رو متوجه نشدید از جمنای بپرسید
🎨
فعلا برای وب فعاله گویا</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4142" target="_blank">📅 21:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4140">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4140" target="_blank">📅 18:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4139">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4139" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4138">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انقدر برق رفت و اومد و نوسان داره روی محافظ میترسم لپ تاپ و همه چی بسوزه آخرش. آقا بیا قطع کن همون دو ساعتو، نخواستیم</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4138" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4137">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بیشترین درخواست توی یوتوب و توییتر ازم این بود که آروم تر صحبت کنم
😁
من فقط نمی‌خوام حوصله‌تون سر بره یا وقتتونو الکی بگیرم
اما از ویدئو بعدی سعی می‌کنم شمرده شمرده تر صحبت کنم</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4137" target="_blank">📅 14:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4136">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LCfwow1QmZodsIIMw4xlYYNqe_8epzUF-2gVCUQHxtIJFoUAEgQwuIHaMJUGpMQb3MhA7ZVELKg4Fk0xssV-Qn553PwlyAdA8MEwD8AxMboKBAMYJbZl9p9QS0w5yOneHpDtePClXwIg_oyr9EuepNaCURgb9zNsReIaKQUNwGa3R7ouuBz0XGpjb0kTs3hXCnF6dPVPq-ulTWk91a4E_DX1bWGGrDnZ8X-YCQTr5O2PQC31XPsf9uG4vk_2fhcUXao8aRlAoP-4q35BBIiRvV1TTd0Dfmdr31nHecWKN82w3HRJLZj6Yrp6TmPHgYOTKrFm2JuHbCTUfyHO1habTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد نسخه‌ی موبایل Hermes، من توی ساب‌ردیتش دیدم که یکی واسش نسخه اندروید ساخته و Pull Request زده روی گیتهاب(که کدش ادغام بشه) منتها هنوز، رسمی منتشر نشده</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4136" target="_blank">📅 14:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4135">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4135" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4132">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k4fnWEyiq6XTSaUg-_pV4fJ5Ysll2z8s8J9GrWnCD0GOWOeaUjzqZ8sncjXaCJ57LdGYINRYAbXG-iCwqh3XWa71D_7Z1mTp99Jf5p-U0wpJ-kdPu01SHgftxONWb8hAmhOgLiJUFmDqrFndnnyMJpnSOoOi8SVwoQ_YwJT4wrZsykLZj06N0ACcc6ZRFLCN5HOaneSp7P8jWLtkYS62xUx0PZa46Zes3j6sHOnQxDDqPPRS1pB3JaY4HVeKQeBRPBLk43qhK6eLCEZTwsnI3ZA2rHczgqledg04TZGFDA-aFlC_xNkXKcm189ABqNyVEAn7-m90nhTdO-z5YtUSNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lv2r0cPwpr_I0sRn6VKtkL-8JcBOzmLcfDcl_DrJKCLufL-eiG8RnsVsrONEvLDAyP2G6nu1StIf8Bt1nus3sjVB4CgOWYr2MJ9e-ZkjqiyigX_K5wUJ7fJJRIOuFWw2jw2oEcBgf7Rpmi6Dj2gYJrYojABVGFY4TjG9C0tgUG4PhEVDQcRxbaNDbJxTximZvlMN_o9wCAKnxizVzz3tzqMop7RdRfGjTeZMwS9_Mj7ybrBFL3Rhh0fMRcg0Z3lmxtzw-NM4i-3DvXnonHymGIOQZcvFolRBwXbiZylxg_1DWoQUQ9j8ZcKx21dqSgepSJ-iaqfcEgWBAcnd4GaqyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tWX1nNIBZyyqEItiSHHIZtaY3JC46te09DK-MOhiVHsGA3ZuuzrXjF-ILlxizF9GO2xT5_A9mAX2sF2ae7CIWXwCEDdb0uyfAiMlTE8qlBFpUOyn-RQsb1fbDRfWP2C3zuqf6LH8EICkdXuEnjVKpkYswouSggUO4cnU9OiYhLeaNVFZxphCVBhvQowhJei-OBJV_yoIQLqw0ZEuwUvBV2hlBNWgMOBiQnfcaYTGi3lzuY1fzjSMdHc2Fvkr-dNNw4C712gnr2jR3sW1EJmCeiq51FsJ3TqUO_3wWR0bZAkccQK7GYYtP2bu55Qz_v1yowl3M7yR8gGa8_qkG6DoBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واقعا Hermes و وصل کردنش روی تلگرام، یه چیز دیگه‌ست!
فقط کافیه ازش بخوای، و بوم
انجام شده. ویدئوی بعدی، هرمس هست
👀</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4132" target="_blank">📅 13:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4131">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4131" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4130">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lc1vxfLzmv9JgP4yQzWza56lbJNDUx55urrmtAmxifN2LfNDMxTBgFXyzhrr1gEe0yktuCNGX4NZLnOQtnEt52ESWTH0hDf11mKXVUkcbzQWZib7AcZFszR93pF2arvRfuX5sl3Z9zt9pozZPW5ZVH-gaA9e0UhkdyKsgZt2K3g-c8_eQTUygxJwVhwRaT7x2Vx1YVoo_6vmorT8HvVI84M6OiFSZgnuaPSzxPlc4fbxIIuE35rpk07gHqQB06uxZyhrUoM_sfuXCVVtxDcCnReTcMJP0e3mc-ymnru5JUL9I0loiKXQ6vNlJyGAqxpV4HokoQ6sEuQSnkcD6D9ZRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4130" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4129">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5950435463.webm?token=B85dw-fA0UpC-g54utoe658mk1MauLZm1mrCN_pI3AgNb8NIKDtGQomdF0nweqEbxABcBkgTGR4EoE4_laWJtHHVqz3Kux5DF5DAiyOilFZ2pxUNq_LwggLTClGdlRJr3i83ecl6Lppj9v5FIUcVXumoqGkmS0wh5NcmpSnErc8yJihoksKyKJIrDlPBIxOlKClGJBcY9ZzmIyvY6GBJkgWqnFSm8EAWb4skhbT5LEHG3irn5tIgOiws37VKRfJAuOgSLQDP63AxEz06KwMMgTsXFKUyRJ8Y94nmEbdPFT9IPkg2SRMtQTbjtdzFgyMZZw2XBuyXDCYWsDVW70aLpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5950435463.webm?token=B85dw-fA0UpC-g54utoe658mk1MauLZm1mrCN_pI3AgNb8NIKDtGQomdF0nweqEbxABcBkgTGR4EoE4_laWJtHHVqz3Kux5DF5DAiyOilFZ2pxUNq_LwggLTClGdlRJr3i83ecl6Lppj9v5FIUcVXumoqGkmS0wh5NcmpSnErc8yJihoksKyKJIrDlPBIxOlKClGJBcY9ZzmIyvY6GBJkgWqnFSm8EAWb4skhbT5LEHG3irn5tIgOiws37VKRfJAuOgSLQDP63AxEz06KwMMgTsXFKUyRJ8Y94nmEbdPFT9IPkg2SRMtQTbjtdzFgyMZZw2XBuyXDCYWsDVW70aLpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4129" target="_blank">📅 04:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4128">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4128" target="_blank">📅 03:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4127">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cB0Ez_wYztxqluFsAbeuyKePQPEuClAme-gRcNQRvH_dKrl1WrLJizaCsLh3aRnZNzC1pt4QKKWQieHFi5z_LZti4BRRx2xaDK8UgEDIlKQvyX8avUNzfP0lGgvZvB4ukyvlJFNmf-qvaljuDe-webj-PQv_-kqEZJVBtp11iTPE7-s6rS7hppG1ouPh3L00kDkxVWaSfyc-e1WWXNdSn7RQp6qDgoR7NN9Qtsulo8imjb4p19ulNC9L97d30G8yFcxLSgaokRuFMUJ-cVO0YrvavZGtqaQo3qtZAiVR6V6mUHshpsCoJFnoD48eK3Y7YHbCWSpVd3DjtoITo0Wrkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4127" target="_blank">📅 03:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4126">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وسط ویدئو متوجه شدم اگر کانکشنتون با api ها خصوصا جمنای قطع میشه هی، می‌تونه مشکل از proxy-ip یا آیپی تمیزتون باشه
گفتم این نکته رو بهتون بگم</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4126" target="_blank">📅 01:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4125">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کمی ویدئو API بیشتر طول میکشه تا آماده بشه
صفر تا صد تمام API های هوش مصنوعی رو میگم بهتون
محتوا رو فدای سرعت نمی‌کنیـم
🥰</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4125" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4120">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4120" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4119">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اگر نمی‌خواید این بلا سرتون بیاد و کس دیگه‌ای بفهمه ای ایران هستید از وی‌پی‌ان‌تون، از نسخه‌ی جدید WhiteDNS استفاده کنید</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4119" target="_blank">📅 18:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4118">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ولی GLM 5.2 واقعا عجیبه. قیمتش روی api تقریبا ۴-۵ برابر از Opus 4.8 کمتره
این چینیا چیکار کردن با آنتروپیک، خدا میدونه</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4118" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4117">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:  1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید: https://grok.com
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4117" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4116">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تمام سعیم رو می‌کنم که سری ویدئوهای AI، برای همه‌ی مردم مناسب باشه. تنها خواهشی که ازتون دارم اینه که نترسید، وقت بذارید، و ویدئوها رو ببینید و کار با این ابزارهای جدید رو یاد بگیرید
🥳
خیلیا که کمی از این فضا دور بودن، فکر  ما داریم راجب چه چیز خفنی حرف می‌زنیم و ...
در صورتی که شاید تفاوت درک و دانش ما از این زمینه با شما، صرفا دو سه روز کلنجار رفتن با ابزارهای مختلف باشه! همین.
به محض اینکه کم‌خوابی ۳۰-۴۰ ساعته‌م جبران شد ویدئو رو واستون ضبط می‌کنم
🤲</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4116" target="_blank">📅 11:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4115">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S9iFaGRTqJXo498kHOp9zu496ZBS6RP7P889P9WboH8C1dfa8AtnMYGdtw05N5FVlv6YU6feWgBi_wEdCTYlCH1AmGQJw5o1HU901Yo9Tvz_I2rZH5Y-xx6fiBtHBjMmshW1jJ9z1tk0wMjqyBEm6114kiczDTeYLLFeExN-5Vx5-Gx6fQ0PQe46nyd7_YciMFSVFB9AvpuU2xD3NDkc3q9jR5sEACsVl_4uLVFNc0JcVwD2KCIvUIrA-fOf2J0tJiCgL0z5u8FJw9cpPhCrKAkw3Vw4Sa-GJ8ZgvdgMi-Nr0obQUkl1mpSxIvWVpF_1GTKGuzxdZmLCuuWloooh0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB  ۱۰۰ دلار میده باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4115" target="_blank">📅 11:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4112">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BbbaxEYaAtqoSojhNUwrrw3ptOuJZNb7s7Pdq1d_YJbjujLBDbvdHTxGzlZoBm7imbn1-RsMvNkIWfkEr19J1otVBHv_oaJOiIxTEmGNHh_GURQP4ZfZauDi-cgRgKvriX3I85TOgBDGf5NjDqN6bT5iZ-9ulFNcobS1dS5C33iniHjuFQ_R-queelkkukpqiV2nDv1txJhl0-uP2MMzTj8moY1xGWamioWqWYRhc5LfHS-y_2DmLt5jIvbNiS4xgcs3_MgYELoKSdyhTKgvkwnJloZsh4Dwr5c8S02Wk8UACnp5Tq-g_LiX2WFyFHcvCFeGPqbCVJzHm9YJakH5kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r8GJWtNMhwbwjgUpwk89v3tX-N0NX1JYlonML6CH027DhFr_mdSo4yrPyMfe-_GGv48xIVdFMJVz6EG7K76FbCE3o0oP5VLgxt1dUPeG51ByQLaUTr96v82x4cy-OqOsq8awUOj1kMmihpWka15c4OXj7tkCVUDGiLs00qsQa1D4rx3gqofT1bVYt2MJbiornAV5ct-cCKLLU8yRl9Fjc0T8fz20LRmBdfCaZhWGbcDMyAVdCdi-mk9oM6n35qxODuxRsrHnKgQH5xBHj9kq6BQzXaMmL1TUegDL3CPrcu6s61QbHPEUgWjRTAlFALubE9Z3A7OPsm-f-CXu4fXz8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bmWRp_mE12jRfZAbJCNxJYvLK6aZiyxV52Jean77ijxC8my5HvSSY6Btfht4fTYPIlopDEsSRvZxBWahLsidnpLtlsOID0Q-s2pPB52oOnsdb7-IZVkRiZvR0zRwaNM6QJ4wS_VUckDDoZe4lY3ny5pnHLYwurWcKpMb3sr8jmLMhW6-1AUM1kODnsQ9nIGPhDOJ6rTfurwAwaSE-NGc8p0RiiUjEjO7ZYsSxQVw3oXjyBmXp4JpTRpiTqHatnqZt-L4h1TC2AaPNGg55LXrnK8lZL2Tmn3rwE-GRU0RhAqUu9f3l1TDv_XJ2MnHMCLIQA8e49sp0PFDDGOZJViZMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی واقعا داره پول میده به یوتوب که ایرانیا رو به دین مسیحیت دعوت کنه
این تیکه هم از یه فیلم بود. دوبله فارسی
😂
😂
وبسایتشون هم بامزه بود
https://daneh.online/four-spiritual-laws/</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4112" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4110">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AO-WTSL5rerEjUMSzwhlJeI54MnqD9x_pclNWF8VJBQ5-ueWAaIDP6IiYTHEbGNm46hyVCp0uyV0v1GbnjEj02g5Uu202YXqY-9cVOLRiEURszeNATRXdRgLe7-JvXFBFsal-BXclaCf3K-Ew7lapVOHETSCmDDq6URMeYzz4a3qYjDHxAOFwmcGpqTY8rSEmZ7N2bGGGC5cjMaiawenDpyrMHxEdnNIjke1KWbMZvNYfEHhdUOD0-1Cqed-LjdjjIN75t51Cw-f2GMGuOAAJOZN7r6iHG65gbKT5ec2gt9d4QByTT_7a6bOrnES61kKi0BskDnVV_DZiy4We0or9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Uv7gtb8cxEOF5Uei8iT5fx4Im_EOZnNXwtaeoxIrRTnysbg2wow3jrvuLPIJHX4kRUEhOW-NjHa3DT-v-dVDC4TvzRi3C0TTakkY6V5ugnt_XT4vZnq7q_lBpv4jLdq8GMa_a0LMtqZq_z5fQ1s7y2mXCqa15gOwisO-pXnW1llaffzuOLqZe3YRaOx-xsGvtzyAQUth1YeMjNYtjLuVI8bm7iH6OgN3_241-yiurE0NtOoCf_KRtBMzItULEk_u9o0RwMLwQSche1QGhry3s9NwTStvV9OV3S3MjDjJ8EJwZrn9wsm--0W707J-8JQeHJO-pTSNdnVr22MwuL0ofQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:)) همه‌ی اینا برای یه تسک ساده. بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو 10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4110" target="_blank">📅 04:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4108">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eRS-Q8gdqJHuGmZYRIdplXxRMYzQeom_uITdjnrZ8qQV_iIP9hltBWT4YwIbwbmvK3D3K6dICCCQGhCQbu50WA7p3zlozMAWs10vLIlgXfISwNAztTOR7wet2XN5Vrhmt8z-rlU4yOJiv6eisdOPmXsypmPKE5BIWgPcujYs0-U9FoYR3iwZPvt7_uChu7o9LMRbUd3M4NW-ycKxHxRPmQJxR_IKEvs8rY5ggTyCbjul3yTpJzGL5LCFkMVx6mDzYpXLy-aCCfskj34KmbZREaggC43qblNnvoUuFzxxy_0v8hPEL1Qp4HS2sbXzo3tKsI3yBuLa_LIoKexZPS5BVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K7dJOeV27jwXjVNXf8w1ow6ZhU5lqhO59xWcUGGQPZpfo3fZLueD_EEvz9NpFTIWowuVx6rV61nNzVSYdf3tggaPWUhRD4mk-0N2SJY17sUeyhEoUkXDl0Suo-QxJr_hkx1Mf5a3k3SflUMo_soM1dZyYAghKErW2Gv3Jy98jqpRswy0ZDowhxhwPynwugrvPDE9iblcFJe7q41az9iC2WUEn0WLAV0FBNITqda7ephVKoLw2RbbG-LUhDH83zXcHat1wFwoW9IlDWYjuc_TB4iabvA1NLPNksUizMflPZtvdBbe4TotwSRYVgzrU-PgUV6D8ytPUHFGbTTYELT7IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:))
همه‌ی اینا برای یه تسک ساده.
بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو
10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی اسپویل طبیعتا)</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4108" target="_blank">📅 04:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4107">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از aistudio.google.com هم می‌تونید بگیرید که…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4107" target="_blank">📅 03:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4106">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از
aistudio.google.com
هم می‌تونید بگیرید که بسیار راحته و توی ویدئو بهتون یاد میدم. در کنار یه سری api و چیز میز دیگه</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4106" target="_blank">📅 03:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4105">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رفقا اگر می‌خواید از نسخه‌ی دسکتاپ Hermes استفاده کنید، به نظرم یه دور Hermes رو با Keep Data حذف کنید و بعد، از اینستالر Desktop استفاده کنید. چون من دو بار روی دوتا سیستم مختلف تست کردم و اگر اول CLI نصب می‌شد، بعدا با Hermes Desktop میخواستم نسخه‌ی دسکتاپ رو بگیرم، به باگ‌های به شدت عجیب غریبی می‌خوردم و یه سری از بخش ها کلا به درستی نصب نشده بود. الان که دانلود کردم از
https://hermes-agent.nousresearch.com/
اینجا، اوکی شد</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4105" target="_blank">📅 01:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4104">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کار خفنی که پدرام امروز کرد این بودش که جلوی دی‌ان‌اس لیک رو گرفت کلا توی اپ WhiteDNS
اگر وصل نمیشید به اپ، حتما از Fronting IP استفاده کنید.
من که با سرعت بالا وصلم</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4104" target="_blank">📅 22:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4103">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4103" target="_blank">📅 22:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4102">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">این 9router واقعا ۱۰۰-هیچ freellmapi رو میزنه. شاید کلا با همین بهتون آموزش دادم</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4102" target="_blank">📅 19:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4101">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یه گزینه هم داره به اسم disable ai
هرچی فیچر ai هست رو غیرفعال می‌کنه توی کل برنامه
اینم برای عزیزان دل مخالف ai
😂</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4101" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fFk23cLYXXf-Sgq53LYPYmlJO3DX5WpY9dqeh9HGHwD_x2hTXdmYdNPnjWbuZCZk7iKud_b7sTzLsVP3L9CmAgzh6lh9VzuZlCnoHOEIeNjaQVx7Q-KemqnfWh8UJEUjzHaT68cvdxXDu3Z1sQhlpeBB054N6V-7UQt8Jm3PCEj4u3E45MUxMZd5YVNJX9bOLjK8ZoV8HWkQMs5O0SnVGiUqb-TJ_1iOp4VXhtVYMqpNPMaaDjciFbbUKuiQrOlsRqUAJxcQu6XxekvdO3RyzhyqzlrM-JDrTQjx67_m_a6c_YrOT8b73gVqKt60zPmSZ-YpFXig9JKRtZffvrquVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bKrMLLcGFdQ4NRy8ix4mRaWBzVOB9kcURiV-T5hPVy_RC6bzyO3SsPacn5leRbYGOMHEE8NNj23qnqGbkXodrJ4zVlZIcVCUq4Jm0ivQv6l9CVTXyyMk1NvP8NhDD-c4t742pqqY3cxEWlNKLQV21m93ZnZtQhfKGK7dnHVtFSNThCDffy8b30KfqM_Y3Aq-27qTOi4vjx3Wn9EjlsemxbIKf8kIog0AkCmxHo-u4Lr2NmEJV1KP0Xk7O_kPwkdgD3EwgLBytBqt8FrmSFzqEMS-57Tgwm1vzHRwuy7KXxXT8pyahnEjKz_7gQv-1uj0ViIHjh1T2uWz5P4Vu2Zdiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zq2Wat33SdkgkhHFoYL6cTkZhW0ToezwM8Uw8xCQhwBVZ-Ka5wxuxlC15Rz3AYgsdlwTpllXYGPyKutUeICkClVH7YIAO1HR6T_WjYGKBgbcyEjk-t_mgHZ5jLKsCm57s8rxW58vg9-dDPsNOWWFvGoPSqap6J1d36YY3kMISw8BT2eYR36LhE5X4Zy44vyHzVGG-QZSoJktlQybeRXOX-wc6YNy7XbiLUEYt-LGT0FUKG9DyD-flLckTBi_yYJAH1-rikV3n7C4wH7rlVCj-jTuNwkcTQouhs00wWf0VeakO3yhpbbL-t_r6oWnFKsBuZKVpjO0TYanPRibaKY8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T-lkxc3DAcg3kpgsYd14H1aQwNQ4tZYdW3wcfzMs1HjQlir_CPrNStI92a5LPt0BJPs2boje6urCiXjl7KxrIET6_zLcakxuF77B0wuH2TQ9iSYYRvs4LUFulYxUXE7OidcG7vT8s0PgUZ0QW2q7yx3KpboOEfCZM0SjOWya5O95sTsbgjsUSEIun426GFkn5IP_VKxJFcuCyJTFXaEApBlgpJb6ofKpUg58H4zi1X4-UBoZlGEpK96LppD8m1OCgeT3mUxxqikVtkUXMt4cteRhxaMOkLq3zLu-cDv8-U68zQO1eBmkEYC-2JpUQxnaW5oSBXlrWiSNO-ZnJRDs8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k2Ftvyoko24XAm5Rh3x738TkS3UIBfkY-rBsqjtWG9QMZGoXe2fUUYW0Go2zB7XkL0r9FcxB7iPgwDBVawDLMbc9L5n5U9ongB-Zp6KLeTqcjsMVCNWn0QDWkISciJlv5RPyJcriVOrfYwA2obWHFITTzMY7DuPbc2LPiJh9WN0Yvkn1ErIrcvzPjm18RxcuUz4RTCkwrvQRbU35D_DSFEPGNjhlNPizv5wH2Fdb0dXGVF1bL4bYt672Vb5rdao2ZwBqIRbuyVRS-pnchkabtImXgDBd8PsdlT6BNYjfIAeAxao5rzGODdHCArjL5AYVSkmptaKDjtWDfmf1CBZbUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/4096" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4095">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-poll">
<h4>📊 بچه‌ها آیا نیازه من یه ویدئوی کوچولو بگیرم واسه‌ی طرز استفاده از همه‌ی این ‌apiها؟</h4>
<ul>
<li>✓ آره. بلد نیستم👍</li>
<li>✓ نه نیازی نیست. بلدم👎</li>
<li>✓ رهگذرم. دیدن نتایج👋</li>
</ul>
</div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.   خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم  در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4095" target="_blank">📅 15:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4093">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tVCqe_ScFEJ_hkxbc3bxThX8LACWXixkLfaCkdnvcPWRqRRWQKBOcMPNFovmRzdGVXGxdoGezzdYh5_2AyMX0gCc61-jrq84neXOisoKZmvjKFBli8IM5OzsWY00skcFhW60yHy4AQRVtiQVjWSjfqkJrCGnW_n7qBTBWVCibt9UNsfqhEBtgQvL7ipz6AqBdqilYb8xu7qCx09o6ZzsB9V9t5VqonTvO1l6muzYu8Nzv_sjYQiVh02hgJc5rLzR88vR-9euBS9QCWR7DBfWd2RXBIxFZOJ0K7uAsAHyJNRb9qQHWxVWz6TXTyXxqF0SHSCV5ciHFzAlZY2smBRzUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DXRVahr8JCfxIyii-kFPQYn2Ajtvf_7JVIiwrO0Ol3MbRttnyKrfGQ882MseyNpwl3FQ9jxZDc0KqOZHMqWDpAbyPE2y9P3dBprJlMMGSn09tVXRNOevfbhswU97YEO1TwnJTPsKq47XwFK1iuJomVxnZBD7XBgSLSEPtLhjMW1iXTVp2_UULyPT7w9lc1QvAcRePHmvkwCKryFkYdUpyzttHAM2GhTkMqChG9xsP1Dxw_cZxKQHW0rWAWl5KcWFUlzdsd3SyEk5ulpOLLUGAboDNWEyn9E9cNVa3Vdh02mpE9fGi3GZGdKsJ5Z2xixa3ftF5Vqsb-P_NXgoOKt6Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اونوقت واسه بوفه خوابگاه ما تو یه روز 30 نفر کارت به کارت میکردن حسابش مسدود میشد به خاطر تعداد تراکنش</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4093" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4092">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWRSARDNrSyxEvZWHpyLcswkTFiTB_R-hSr-_46VGPTzjjzWhWknRnTB9G1wYYAN1aP1Y6ED1EFqF4IUhd2BfF--a1wJxrjZoxm8wLfuyFx-73DTfwmv3n7skzP5-9SNjBtcO6dYPgwNOHAFF_84ly40-Tku7vPMvys64VApr2pEmEDH8JCvnOGGO9YI9kKupgdtrWoF_jWdRHx9Qlgs9SkA3xs6-IrcmGgfntkYjbX4frdyISjkrvqYOVfiVRr3AGdNoBOQuFfv5Oj8yeIJwN3NMt00l92tddlkbdWUabpi1KRcMxBORdrf1s0E8sh8HJiTHonmfkOWwgY8Hw3dEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.
خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم
در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و یه رفرنس خوبی درست بشه
این لینکش، big pickle هم برام درستش کرد دستش درد نکنه:
https://ez-ai-access.yazdan.me/
✍️
Yazdan Fathali</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4092" target="_blank">📅 14:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4091">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">به قول یکی از بچه‌ها انقدر api رایگان پیدا کردیم که حالا نمیدونیم باهاش چیکار کنیم
😂
چندتا نکته:
1- اصلا از api های رایگان روی پروژه‌های خصوصی یا حساستون استفاده نکنید
2- هیچ اطلاعات حساسی بهش ندید
3- توی env پروژه‌تون، api key یا... نذارید مخصوصا api پولی کلاد یا gpt یا چیزی
4- حواستون باشه که به جز شرکت‌های معتبر(مثل خود شیائومی که mimo رو رایگان میده یه مدت)، به هیچکدوم از بقیه‌ی سایت‌هایی که api رایگان میدن اعتبار و اعتمادی نیست</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4091" target="_blank">📅 14:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4090">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aZ4CfdaSyCdPVT-tTth4VALK3_cqGSzE6abxhiW9C2qSh5QGvYqwGiMuc_4XkYWQyc4qT_lxtsIuVv0-k7YnKnHW7XXv2cXY_CKxp78q1i-taKA3lTSnZ0dbR5ZdM6mQvWSn_Y5UGQlvN3l31xwEau0x3KwukHaK6MPF3XwzAt_fRNqtnY7MfvCE7a_hjns7cqVig10AVv9i1csVO6ZpVumGt6pP4MiyrJ0blq_fWNawQ3WduHndaw2ObIMOWs1O7E7tp2OSV_UX84J3qWdVLv0ZC0TI0aCf44KKE_a6ZfTdUXdqjlOYYd6S1Fl_864BJGWHeDg7AP6J_5GNe7gbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت بامزه پیدا کردم تمام اخبار جهان رو با ai رصد میکنه. اوپن سورس هم هستش
خبرای ایران و آمریکا رو هم می‌زنه درجا وقتی موشک میزنن و اینها
این پروژه‌اش:
https://github.com/koala73/worldmonitor
اینم سایتش:
https://worldmonitor.app/</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4090" target="_blank">📅 13:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4089">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4089" target="_blank">📅 11:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4088">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j-o-Vklrqv4S3SgN7PI_WP70v_EcZvM85PV_0RRecjBRNrENv3BxRMwu5bmEDKjHnP065oZBXjtc86cD8UdoDzUAIdTa19ZrR6aKKBC8tX8C0zF-sxPmBVSdZEY14Km1KTbo_e0yroBqKRl0V1GGcVQm7wlf_VUkt5dZHtuu1HZsk6aP7Kve8kob5YhF_nKPxy7XMjjecsoDyEHAQjacoIMbXeqORP1umLgBbYKOFIveLqoW0pIFm-_wvS5sap-SVAq8tw7THVhMG7T8F6cCKKyUWSLeBm4pxG8aDF-gehn9f2ata1A9uvC_CwxiS5FXKde2M-FGe1DHP7s_xBBtkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم علت بن شدن دسته‌ای اکانت‌ها، چیز دیگه‌ای باشه. نه فارسی حرف زدن یا ایران و... .
به نظرم مشکل یا کارتی که باهاش پرداخت شده هست(که شاید کارت‌هایی که batch payment داشتن رو تشخیص داده و اکانت‌ها رو بن کرده)
یا اینکه علت دیگه‌ای داره. چون خود خارجی‌ها هم باهاش درگیرن توی ساب‌ردیت‌ها</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4088" target="_blank">📅 10:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4087">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یادش به خیر یه زمانی مد شده بود می‌گفتن Prompt Engineering کنید قبل از اینکه با ai حرف بزنید و یه سریا دوره برگزار کردن کلی فروختن</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/4085" target="_blank">📅 00:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4084">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CzmfFmXPfT3uP3aty5XARvoER-hO9gp550osuXOjy4G01oEFVzJ7OOLDZSIZ1XAQshvUu5_dd4raW82L3yiCa72xT5ge4qVkKCMhMHHG7qCWCqXOVDpe7n1whKjXDdcOlgsxdbBfARL89XMSkZcyLSj_kadrfJht49ctUCrrOPi48CgbcME46z75WKfRixR9yb4LnwYJAS8JDDbiwhg2fJMuvriCTQmHvc1H6cAX4SLLEh77Z5E635ca76cX5qf96CVOxqcZJKrBfza0WISgMhEZTIu7KqOjcKIUN2uWe7azH8xuoHSkL59U8xf8GumWvru87-LGNn5AqpIwVHW5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید اعتراف کنم وقتایی که حوصله‌ام نمیشه یه ویدئوی یوتوب رو ببینم یا وقت ندارم، میدم
جمنای
واسم خلاصه‌اش کنه
👌
attention span در حال غرق شدن</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/4084" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4083">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:) ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/4083" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4080">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nHAyQU3BFujhOdHkNcopDxikPXgEIqVUsdJ-tBrpuRiCKjkBRSYplMlBzDY-kLoXL5EhH5_M3XOpCc2m9bkSMh5tmCjjs-D3-lZOioTrYW02HrA8pYAa9smOpyb32qOSbvnyE3l5Ywqj0g_6nnA6kHgYFLom9A1BTv8ElwCQLO61f5nKgCqtrG4AGdo8gRlM6uDYWNcUmnVnILVck5ynbjA09aMbwEk6dDGWJB_pmglluPTvvCVid53b5nnzRH8OopDF4iHemMnfZXjMqK5SphAAYjd0aJirkHdfFY3qi6Y7rA0NkWj_KcCbsq3zy128a3eWsc4WYuYtb9gVHUc2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kAm42Vp-hymBI_5wK7m_EtRx9IoGafTiAcc0NLVfChKa0hGadkhGhAGnlMaQpR7rRT01GqUx_1h-aEWTfB7H3QR1p6H7n1k6Ja3YC2FKMV-mG4P0Kb296UB1r8eUXpHUS4b5jYOqPzY7nmWlUbuxxlEoCv6d9fGV-uk1BZUGmMb7J744msZ6p7R5nm4zgU6IPrUhgZUVVemrdgSs9jlXvDShLfDgNLpaYlzVenAfIayLsZsUJF91ZaY4jqHrEB_loDVT8xx14bOzF1d3PTf9kyWpReoG1iDRah_DeWfvYw8ATOcyimAp3CsIkc9-pld_kmIVYjT7W8BqvpDRzTHeGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mE2QubbWaI0995Vf0SzsOMi6sc47fvXZE-ddMfrwNDCvz2Wf1-D8vfAcGuUcRM070ADhwHcCQiWt6MHMXcgUFPJZEWd3FC8hicGCIw-2Ng8uMcuIl6QUPctbiJY7ZFSyCJEwQkz_ToHZC2-31pj85IsyyGmYN1iNTw1MIceE308UzPcykVR6Jl9T0NHmla5vx8ZWSeg0X3FNMLv8bOdYRDL2aMVLhXCPF9PGxIwJ2cCUcO_VC0EC_zkZqFz3SONK3goUMlRmKse72xQIvzJMTg-lnV9i_JZLXlan9tgx1jgLm5WCAk7m2TFWJs8rlS59t_2vcQqCNW9dE53BYEM1hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:)
ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید نصب کنید طبیعتا
محیط داحلش هم عاری از هر گونه حواس‌پرتی و به شدت سبکه. به سرعت تب Git رو بالا میاره و تا اینجا عالی بوده</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/4080" target="_blank">📅 22:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اپل تقریبا ۱۷-۱۸ درصد قیمت محصولاتش رو افزایش داده، اونوقت فروشگاه‌های وطنم نه تنها قیمت رو ۳۵-۴۰ درصد کشیدن بالا، بلکه سفارش در جریان تمام مشتری‌ها رو هم لغو کردن تا مجبور بشن برای قیمت جدید پول بدن. بله ایران درست خواهد شد
✉️</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4079" target="_blank">📅 21:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4078">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fgp7D_bpi52yiYuX7hZndYv84hg61iAA6hsJPQ2n9qWZClWjFmi2NYqSjRwk-gWyqShQg-JvWgZl7lBj7-1pAlWwQtSLPQx_VcWQsZeMumAU5lugSFpEDKb_X9Avu4Z2C9265mSzOc1qopvTVvhiQ2pKuECYmMCZQm2aM7GUnxuXtSz3VdxiUYBGGnhUGicZ5BNFMs1Bm0C5B-dKRwo6dWKNmuNxnxsRs8N8ZMVWkZqfi2PGrmi8fFhYHXGZPbZRLGvtpRe_W2oLpYYdUDlp1Wu9oCRZkYq4zUGcaqwq1Kk6m7z3AjznHRzhdwPqYUm45pLA9aaDBh5Q3Vtc16gESw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/4078" target="_blank">📅 21:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4077">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WCBoVi-lU_RcsORPeh8lqnGzNgWsJQWnuvLiHy2R1hhdz1JXn6cw2Ww8KQpY4hW8bZCBSg5DQ9JFFDpBi_2KQBd2zX3G2tnV7GQm5CHxy1fnYuSEVan4-ugwq5TKr7BSCvust5RXB2EPlrkEoT1HRCcTDf-qJzpkk7BK9MtkA1xj30GIHywEmOWNZNiF44qE-H-C8ZwEkZfpRoTVGTsuGGWHGropWBXM4QO1WVZWlQTgv1bfwnt9sLcztnXmzCYZsvSE51-F4eznuTPfMaynr_RgczeF6vKTcI5BZFtb8yRIlvs7PUKWw3qL6uNqLwjUouD81zW6G3cqKONmoHMAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4077" target="_blank">📅 18:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4076">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jziyeQdjAjJSP_Dq6bqHr77inVGcW65XBMvBEhB9LybSmBAXbjMuZbe8AxkjZRDGZYhXErnTp_FPnllXXf9g7NbJZtaRZ7OFUUkWg5-1bkiaEHHzmPJlsEghAW9fRiItqjM-49IOoNDqESbXKNfsYIA51hpbGfXPBQ9jHu775LQRXUOOZrmHrBACWO8SrQ-mx1BdKbahY-7vvmBBFkvbllBz6rFwReOfsX0-cE4V8iLB3Q_S2wImxA4y92XpOOVCjz6hIAga3cN_dsl-Xl7c0xVxonbwqQZ0ydWn1cvZZAg0iP1hLER0OBqLYFDsbs_u1fyqbFDTuN_gWPIqtXGxbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده.
به شدت هم IDE سبک و خوبیه
از اینجا می‌تونید اقدام کنید:
https://zed.dev/education</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/4076" target="_blank">📅 18:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4075">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=BrpGh1QMtkHQYKLwJoGgsEIMfeg3mLqsqWynMcrfKdK0ruIX74ejzoa8G7GnYXmDjcHqtnZVZ-2vHxMXQEp-qsXO9ABAZ0OiUpkapzk9OfMzY71Aihuy6YpbLGeW7djVNYvgw-RxF03IjKwt1pK41-C--iOQdqrJa_hBJJOCNXJP_UeByW0yVr-NGOwrWW6_BQjVnt2MrtUbkZOOJFh9E-ZYBX8039dP7M2NLJITisK7jw4sYk7rZ3D1hBjEqFOyHOmtJI0WhyDO8fpoeyjEsKT0HczxhOYZN3Rh3_U_IhnkYFIWrRE_JmmgOjGC3mDIdkPaV-VAYdG2BWEb9QiPPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=BrpGh1QMtkHQYKLwJoGgsEIMfeg3mLqsqWynMcrfKdK0ruIX74ejzoa8G7GnYXmDjcHqtnZVZ-2vHxMXQEp-qsXO9ABAZ0OiUpkapzk9OfMzY71Aihuy6YpbLGeW7djVNYvgw-RxF03IjKwt1pK41-C--iOQdqrJa_hBJJOCNXJP_UeByW0yVr-NGOwrWW6_BQjVnt2MrtUbkZOOJFh9E-ZYBX8039dP7M2NLJITisK7jw4sYk7rZ3D1hBjEqFOyHOmtJI0WhyDO8fpoeyjEsKT0HczxhOYZN3Rh3_U_IhnkYFIWrRE_JmmgOjGC3mDIdkPaV-VAYdG2BWEb9QiPPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/4075" target="_blank">📅 16:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4074">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دو ساعت برق رفت، گند خورد وسط کارام و تمرکزم و همه‌چی</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/4074" target="_blank">📅 16:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4073">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/4073" target="_blank">📅 16:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4072">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GxNPcVnBNX3h72TEEyhEYvnXGBwIf2-3GFwTVZz7aO7-4jFhKt4UqdlBu9clwR21TvNz2sXh3epmyxE_BBqoRlqWh7J7NGRV9tHecngGp_YMALRiTgQIf2smVYiaZ2T_avvdyp_ioo4Wyqxb2db2ytZ5U_ESVCKUvNUKFw4leRugAZfqsCwSF23sIhCdSKt3JQ9A9wg2VqTRrPYL8tBCzmSd-nBIaQboOAjINyL_tUdidtJovcHz2Ih0_xJyVscRpK7qOvbLJrM2xMPKdPnJptWKTDRPWw3SSX2i44_QC5Vo4bO00G7bELuWld4qhsYOn2Sux5ycn-3tvyfT50BrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور  /learn  هست. به‌جای اینکه بشینید دستی یه SKILL.md بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/4072" target="_blank">📅 13:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4071">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uJWjfbs6zwGK9IXVmzTzm6Rd69-NiR-UCtzdSMJmVRDtFIcin8nAeEo8pJhBzCxBR5IpJoqbmXUU1sDBFFj2lyReRle7xEuYhnkGoVwWx8n8gzed7YrVtFNIAl7Odp1vroAIBViU93lPrnh06-CalVD0N_gJe9DYBvWKiCSh3tp0fuEU8-hj_n6dmdfVYQKLvcVhKU3buEq38iR01CEggDraXKNTuaL0pcgRWXrxIcSgnCkq_DtHIfCk0YIJkGzRyaLcGdw8vcmqqQqP67mZ_nMUDn3uJIJBHEPhbpYTZEYt2Nv1JuNble4Rkr5azPS3rxMqT1WeCabPITXIqpYLCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">از اینجا ببینید آموزش WhiteDNS VPN رو به همراه آموزش اسکنر اندروید من که پدی زحمتش رو کشید:
https://t.me/MatinSenPaii/3999</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4070" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4069">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خب، من با کمک Hermes و API رایگان MiMo Pro 2.5 و API رایگان جمنای، تونستم یه ربات باحال بنویسم!  توی لپ تاپم کلیک میکنم روی یه اسکریپت .bat ، و رباتی که با mimo نوشتم، فید چندتا سایت اخبار ai که به صلاح‌دید خودش معتبر بودن و زرد نبودن رو، می‌خونه، با Gemini…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4068" target="_blank">📅 03:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4067">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IDO4TXahjufUBlH2tECBv3hwZSTMUYzIAoM9HMRVZ8LzitMj4vm8Eo7aaD4QTXLgDai4tT0FfHlGJKqXtE9PEkDdmwCf5dWcZFror4V0Ql06wQXX9p-KoqckSlPGS1HpqQKWHDpEule1Wb2zMSnjWPsf4UjUnuovQ9cxzF-iv_JWyfsyZNsMwwH0BGF3APIahWIr4hc-FyEH_Y9HhikmXG0kqdz3AqUwfLaZJRV1OLOnv388Ty96oDZTcl10JZU5ydvoae-lkMG89zn_RP467ZSbQn8I_oGGyOdgOSg9sckppcp4YmjdKqzLlSpjhejodsavjUPYoIpDgQNmyaqpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر از اسکنر من استفاده می‌کنید و مطمئن هستید که آیپیتون تمیزه، حتما تیک همه‌ی پورت‌ها رو بزنید برای اسکن. چون به چشم دارم میبینم یه سری آیپی تمیزها فقط روی یه سری پورت‌های خاص کار می‌کنن
آموزش اسکنر و اتصال رایگان به اینترنت ازاد با سیستم(ویندوز-مک-لینوکس):
https://youtu.be/JdNeZnclS-s
آموزش با گوشی اندروید:
https://www.youtube.com/watch?v=2otJfXgNWCM&t=70s</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4067" target="_blank">📅 03:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4066">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dYWgSWcKcasUpPEviVDFxeDXJDsSyo-DGF5_TliBzK1F9D71Rq8Q1w0uha46gWuz6A8U6ODCK1y6RaMN2_Sh8xwy44bNUrvq8FvOju7Pf7B_V6VCD5SnfylTGklf2GPYHT_0aefyJArJm0JE8ot16rHIW_NVjBclw55Jfy-dVua8VAJXac0w-LsJCOb6S06XfQwx-avlkrp8yEwbDz6fmeQtmkpfB6G_kIs7YZZmugUcHLQhGbdgEkhJYsJVIEqrBBaJ2bHEU1VKhAa1XV1KyRdKeoXnNF2syGaBB1rjB-0H8lghAEHnYDdS4aXpSoHpMZIe1DVTonf3vdUnc8rLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fYwezS4Xh6SZjfg-JcxC3w5qBpOo0Ge1vgXarfpvSFLy-wYR3u69l_mlj760soJYA0N6Mmd79STm5vdatwVWeYRIxoXFtJZi2WPFytzpxKAG53z8voOTutNfEwCYpslbZftqBZBOtKL6q1JwgTjXfTsPssWT7NGXcHL0LOm1jQTDkPbsRW-CDa8glCfNhQzQQbhcIVU_7g-cjGtPWZzK0VYdMzMV7fqqLkRq6SRwNwOUMcJQZ9ciQLqXqbsclso57gwBT6R_K60nI3JWlVadssKTmkVrXJURBk_TJzlnCd8EgyEwwlRzIhDWa2pCTEIc-3N4Dp69gRd9LX7lQrgVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MLg6tWLnqVyH8JDfTw_2-RjM-foXYygpaqQ_wISIH0vfZH7yXkinD1sSmtSC2uvSw6QoPseMifAtIj0veKJoTW79wBmz14LfxTzvrQQkbE8kkANq5SzV2YUa7nv3hebwkTkyIbnZa7czSixqHw-uCpOpf6snUk1exgjoaPsosT3dTM8ncubo_6pAx_D7xQQQM5gh8HUWZDZmXhWf8cCcAmF0soC_pKrkq9r_bnuTY4a72t7Wr94uPhq3ghuiMa-73vT2L0aH0DPgTBfiYARava9WjGysJ18KcKDKWSZMp0ReaORRPXnN8CqLf5FhdFC5ZTEYEWvXf12WOmPtByJZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W0k2yEwK0iTiiarem0hFVxRjrp9WBSuohts5SCeiq0_OFlzzgcdmXT9HC0XfCxdGMrqcy-scZ4vwgnGKmEXqbcgxUcXwCy2-ZVy49wxC_DMIShbFcQkgx_VQtTVwPW8jJUP2mNdjO-tn6mxH-qXyU7YTfmcqEdzTzEbDLjuTQpyqTNwOQBWqV3lM_Bkfj6j6mooKic1IDJU0Y91LJgCyfu_EHDAEwPBsr-4dfVESaowCHt0SqOgbvhHSdXED1Xy-egTVamEwyttz960GdUFQOHAHLJaVMwICC4XnINKW_x1VAQcatUYFzqMqeGShTj76OYWm1wcC39i8gUyj4RoNRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4062" target="_blank">📅 02:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4061">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B47yksKrIb-bkHecTjKeczvLiklFYokxogeL5v5t4aCkQHkAOCxHGdf8yGQH8Nd55qvtNsZU8V3mBm2UabHJlWU6X12crXK7iLnvSggE6CP6PG5Rsv_grHWoKjUuUGy-jybNSimxGWsJgrmqZaBcYmC_vIHGtI27ayEQDJvtuQkW0MZBGypSl5sXpOY5ENGK26eBo4OxEGZ7Tuw6clegoMlm023HAyocS54R-FekM9RXbwtH1ZtMGeaFvKN0QVpDR5ViubMmJWv1y5hvh_vA2ihwEmozWwU_I9jBIY_lJLi6CK3T_aBFMhUP6hUvjd3m7ExihvDxgMldhqUj3VrWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه!
یه ربات خیلی کوچولو هم دارم می‌نویسم.
دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes
خوبی این سایته هم اینه که روزی 7 میلیون توکن رایگان از Mistral و MiMo Pro 2.5 میده و هر روز دوباره شارژ میشه. نوع API هم open-ai compatible هست. اینها رو بعدا توضیح میدم برای دوستانی که متوجه نمی‌شن پس نگران نباشید
از این لینک هم می‌تونید ثبت نام کنید داخلش:
https://router.bynara.id/register?ref=PJ6RZMDB
رفرالش هم چیز خاصی نداره فکر کنم، صرفا اگر بعدا خواستید شارژ کنید، وقتی با رفرال وارد شده باشید، توکن رایگان اضافه می‌گیرید</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4061" target="_blank">📅 01:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4060">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مدل پرچم‌دار GPT-5.6 Sol برای برنامه‌نویسی، امنیت سایبری و اجرای ایجنت‌های هوش مصنوعی بهینه شده و از قابلیت‌های جدیدی مانند «استدلال عمیق» و استفاده از چند ایجنت تخصصی برای حل مسائل پیچیده بهره می‌برد.</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4060" target="_blank">📅 00:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4059">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به قول یکی از بچه‌ها یه چرت می‌زنیم بیدار میشیم می‌بینیم ده تا هوش مصنوعی api رایگان دادن
😂
چون خیلی حجم مطالب زیاد شد این دو روز
به زودی دسته‌بندی می‌کنم و می‌ذارم
همینطور بهترین‌هاش رو(که زود گذر نیستن) ویدئو می‌کنم و یاد میدم</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4059" target="_blank">📅 00:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4058">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اگر مثل TTS اش بهش چندین تا لحن و دوبلور اضافه کنه هم عالی میشه. که اتوماتیک تشخیص بده و صدای دوبلور زن و مرد رو تفکیک کنه. که در ادامه به نظرم این کار رو انجام خواهد داد چون همین الانش هم برای بخش پادکست، اضافه‌اش کرده</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4058" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4057">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود! همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا. دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4057" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4056">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=gyGD6W2d6yb0Mcjbi3jPXBHKeWQ3xrfi02RPS8CePEme5blUgqRvcgduWV0_hItlbLGyjT4P3oq_bM8USZlZHEQ7kO0kJ0yyj_HSN2mOa24B7jLaxOz73T2uCbjWFWrxRhhGJZQTufbpz2QzSzurmwtirzSyqL1dpOXfXgD_4L5Yo_Jvm3IRqhjgI_A6_KCaGodmSXxG9elrLP2f_X1CfNHrmATFG65oKvAypWNtA9xv-h1TH7_vNmiLPlQdYnVNZg3b3AOOsiCirUhRnKItSe6Q6UEzo6ylYn0AYMktSKAAeVWm9jX_EqxVSPYrAIqAVHJMJUUJJVPtDlKKuWutEqCHESQY4HMh4m8YIHpoCDouTjYpLxd5jQXn391nu8K8yJjyewxtT7AkN1-YgfCavO9BewIHeIPb7ZXOTwW4qWIhCPKLs7krMOuYW6ZhPifQIRUmWoQHxjBpREH3q4Lly5iAzr-dWvlbnOhHmgDzeiTS7ecRMKrqFYBiJY2VOVRAmhcW200wBmHZQVLptE8blrg5SevNlCp8FIXWSSrHLx8j0w7lKP6hgkJ7VJvFxJ7Ot6RX7y-i7V0k-v1MfO4nPoqqWOD5aWditelupXN0tPoUJetH4lgverzQatk7BxSaAbNHNZm0-ul0jWf_OzfsocVSRqtjNDcFDPQUC60Mv4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=gyGD6W2d6yb0Mcjbi3jPXBHKeWQ3xrfi02RPS8CePEme5blUgqRvcgduWV0_hItlbLGyjT4P3oq_bM8USZlZHEQ7kO0kJ0yyj_HSN2mOa24B7jLaxOz73T2uCbjWFWrxRhhGJZQTufbpz2QzSzurmwtirzSyqL1dpOXfXgD_4L5Yo_Jvm3IRqhjgI_A6_KCaGodmSXxG9elrLP2f_X1CfNHrmATFG65oKvAypWNtA9xv-h1TH7_vNmiLPlQdYnVNZg3b3AOOsiCirUhRnKItSe6Q6UEzo6ylYn0AYMktSKAAeVWm9jX_EqxVSPYrAIqAVHJMJUUJJVPtDlKKuWutEqCHESQY4HMh4m8YIHpoCDouTjYpLxd5jQXn391nu8K8yJjyewxtT7AkN1-YgfCavO9BewIHeIPb7ZXOTwW4qWIhCPKLs7krMOuYW6ZhPifQIRUmWoQHxjBpREH3q4Lly5iAzr-dWvlbnOhHmgDzeiTS7ecRMKrqFYBiJY2VOVRAmhcW200wBmHZQVLptE8blrg5SevNlCp8FIXWSSrHLx8j0w7lKP6hgkJ7VJvFxJ7Ot6RX7y-i7V0k-v1MfO4nPoqqWOD5aWditelupXN0tPoUJetH4lgverzQatk7BxSaAbNHNZm0-ul0jWf_OzfsocVSRqtjNDcFDPQUC60Mv4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود!
همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا.
دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه و خیلی جذاب بود حقیقتا. مخصوصا وقتی که بخواید با یه نفر که به زبان شما حرف نمی‌زنه، میت داشته باشید
از اینجا می‌تونید استفاده کنید:
https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/4056" target="_blank">📅 21:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4055">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⚡
اگر برنامه‌نویس نیستید، API Key را بگیرید و بدون نیاز به ثبت‌نام وارد سایت زیر شوید:
https://B2n.ir/newapi
آدرس سرویس و کلید را وارد کنید و از مدل‌ها استفاده کنید.</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4055" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4050">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کنار iran internet monitor باید یه کانال بالا بیاریم iran bank monitor که وضعیت بانکا رو رصد کنه
بانک ملی درست شده بود باز قطع شد</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/4050" target="_blank">📅 15:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4049">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z8JCT1O4hHvuYUOhkIHd1Thh0M2HDqsm8lZNvS8mNKsp11nFvtojWc_1jI21lnwXDjt5sPBCEdAn3d4KWMFRvo-S_kVggrWkUJYuhZzYLYU8l6qwfy9FLaKc6SZQ_GpqCD-ZPG8fyl0LittrWH8GoCE1NUMM--BbLbftdgXP2vq0ACvuj_Kr-8o2yN450akbdJsFjzLu6aza_RJjfbIZI3JYkSKihWF_qc5ZyuNm_ydhgYB0xRZfhFe6NV_sgik6ppRbkoO1qEWqIXmZOWHiv2PNawnFFzPYUYfgpDcS9F3rnRclIuccRebN9bIldVm7Ihgbn0ANNwL9O6-fT8h3eQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/MatinSenPaii/4049" target="_blank">📅 14:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4048">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6dnCCnIMJyokiJgR5xY0iwdNmVdchrcntEeGVqH0loIeKAsoGnNy7YBQ61pUXDTAKVSdefHEa2--3EFbKS7AOleeEV_q7vRX3pudNlTqgzr1zI_sqR3p_RElSM1kaGOSMUV13SkJY3I87inxyHIlSp65CI3UH4h_6i9fr2skXRMqmyJoK6idV0NH_0wFejr7zf5-SO0tMmyZSk_5ugygdgKp94_FXXrMU9-lviTAWyysqqbqKbroudU_MKytTt-9KGfQkFIRf0tj9HsAs9lUYpNbnn43tNvPNOuxmjKqVffmgN4UwFW7__tTf6RlUbzbT7TeHYtnek4yaq0acN9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزنید این حرف رو بچه‌ها. شما چیزی به من مدیون نیستید
❤️
همه‌اش لطفتونه
و ممنونم ازتون</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4048" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4047">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Dastamo Begir</div>
  <div class="tg-doc-extra">MEZZO</div>
</div>
<a href="https://t.me/MatinSenPaii/4047" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4047" target="_blank">📅 14:27 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
