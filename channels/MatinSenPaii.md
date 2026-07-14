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
<img src="https://cdn1.telesco.pe/file/JpbrunaZsluAJ86G63wtg8VjadqD6qdDHUeSwtN_g9oLJKzuBnXLiBaoHnpfD09jTlCEuFIr82V4Ox9yrLFdQmUx5WDJJqePickmi5tllKXiYUVgFMRpqZ5BFnoom_pSu-wmTZad9k8XNm2l8uWcs6BfSPlK494gIz0mgOpTcKV-XzwWVF2h0ofn-qH-zS6Iqce6k2L5QiQhwwyEbe4MTPPvyDgeFa8lp1yobunYO-IoKKtDTCGcu9UA7SNork5jE0LVxq63_37-nz4KIG1ljCTD3Wqib0CUIkr4KF7O3HnO0jLDpvZZ96HZArbKs77iBHpq6evyP65ZYdf7QF4V0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 02:18:33</div>
<hr>

<div class="tg-post" id="msg-4480">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خیلی خلاصه بگم:
فیلترینگ به‌طور معمول دو راه داره برای شناسایی:
(الف) دیدن امضای مشخص پروتکل در هندشیک،
(ب) بلاک‌کردن آدرس‌های شناخته‌شده یا کل ترافیک UDP.
حالا  Aether راه (الف) رو با تقلید از HTTPS معمولی + نویز خنثی می‌کنه، و راه (ب) رو با اسکن دائمی آدرس‌ها + قابلیت سوییچ به TCP (h2) دور می‌زنه.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/MatinSenPaii/4480" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4479">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eV9gzNDiR8Cx2GfAu4RTE4WDZhVO15jBebD7GmrSSatj6ahSnIWL97EBYnBf9rtiQu8385-42HqsuYVFc-bYrp8Ta4EG_wcVpzldUqK2pJQpHU2mOpmHc3kgA7yVl4gkAUlDRXO4xCHnxYcjOssL5l2yHYjI2NyFirW8tbIsdgmaKGuRryBTqea9BQrIewGjhr2qxvRXi4FlxP0qAf7OdEuHGHudTAqUZNT-2OD8AFVWEhT5wjYZYVeephLcDmbpUF15-ZZ852JeZ0W3F-ISXrv-RWpvJueaAqj1U4tw57xkE14zCPvNGbrNvuewGVvjRSMq_CGoTjlTIzgXJILXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/MatinSenPaii/4479" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4478">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/MatinSenPaii/4478" target="_blank">📅 23:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4477">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">به زودی آموزشش رو می‌ذارم. هم دسکتاپ هم اندروید</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/MatinSenPaii/4477" target="_blank">📅 23:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4476">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
خلاصه از متن و ساده کردن برای دوستان مبتدی:
شما فیلترشکن oblivion یا وارپ(
1.1.1.1
) قطعا میشناسید.
این فیلترشکن ها تا قبل از دی ماه خونین متصل بود و شما با تنها وارد کردن یه مقداری مثل ip شیر و خورشید متصل میشدید ولی بعد از اون ماجرا ها از کار افتاد و هسته عملا بروز نشده بود تا الان.
حالا یعنی چی یعنی واسه
#اندروید
و
#ios
قراره هسته اپلیکیشن هایی که مربوط به این روش بودن بروز شن و شما بتونید با اپلیکیشن هایی مثل:
Oblivion
(اندروید)
Defyx
(ios,اندروید)
💡
نکته:فیلترشکن defyx رو میتونید بریزید و از یوتوب بدون تبلیغ و سرور های معمولی به صورت نامحدود استفاده کنید.
متصل بشید خلاصه بود از این پروژه وارپ این وارپ.
متین به زودی آموزشش رو میگیره
❗️
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/MatinSenPaii/4476" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4475">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yr1dq79UsoM39HREJbioIgO6Su9Isu-GlIzWNpo4Xb3b00VBGoZa_Go5J6h_OH-GWbU0qwvJNtfXoybAIYlqlPmJrRLRLBnyXgIzLrElogf2vu8XmiwiZWrXGKSUbY5NN62jn3C0xrtjrv9p-Ij5tu84qImCye732JIvOFL3XT8_xOeaqjHOIHNNVYLWs3okZbk_8_32mLBq67s2kaONkhYgvlf8QkMNiiZM3wpJtPHJkbQR7vG8F7I2wgeCGsMqvJc_-keGC8PRQhAkJpgacbnaIfbVQ1QqX19pD66F3_ZS3FkaXA7L7vIG9KxMunfG-2eov9G5woKFoiES9yo9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوق‌العاده.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/MatinSenPaii/4475" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4474">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الان خودم ران کردم و حقیقتا جالبه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/MatinSenPaii/4474" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4473">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اگر ارور Port already in use روی ترموکس می‌گیرید، باید لوکال پورت V2rayNG رو از ۱۰۸۰۸ تغییر بدید</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/MatinSenPaii/4473" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4472">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">Aether یه پروژه‌ی شبکه سریع و مقاوم - برای اینترنت آزاد Aether  با ترکیب Cloudflare  پروتکل MASQUE (روی QUIC/HTTP3) و WireGuard به‌همراه چندتا لایه مبهم‌سازی ترافیک خیلی کمک میکنه از DPI و فیلترینگ شبکه رد بشی  برنامه خودش به‌ صورت خودکار بهترین Endpoint موجود…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/MatinSenPaii/4472" target="_blank">📅 22:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4471">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">Aether
یه پروژه‌ی شبکه سریع و مقاوم - برای اینترنت آزاد
Aether
با ترکیب Cloudflare
پروتکل MASQUE
(روی QUIC/HTTP3) و WireGuard به‌همراه چندتا لایه مبهم‌سازی ترافیک خیلی کمک میکنه از DPI و فیلترینگ شبکه رد بشی
برنامه خودش به‌ صورت خودکار بهترین Endpoint موجود رو اسکن و انتخاب میکنه پس نیازی نیست دستی چیزی تنظیم کنیم یا دنبال سرور از پیش‌ آماده بگردی...
روی شبکه‌هایی که فیلترینگ سنگین و پیچیده دارن هم عملکرد خوبی/عالی داره چون از پروتکل‌ هایی استفاده می‌کنه که خودشون رو کاملاً شبیه ترافیک وب معمولی نشون میدن. :))
پروتکل‌ها:
MASQUE + WireGuard + WARP-in-WARP
برای MASQUE هم به‌ صورت پیش‌فرض از HTTP/3 استفاده میکنه ولی اگه تو شبکه‌ای هستی که HTTP/3 یا QUIC محدود شده
میتونی بری روی HTTP/2 که سازگاری بیشتری با شبکه‌های محدودتر داره.
یه اسکنر داخلی هم داره که خودش endpoint های سالم رو پیدا میکنه و انتخابشون میکنه :))
مناسب هم برای شبکه‌های به‌شدت محدود هم شبکه‌های عادی.
پشتیبانی از:
Linux، macOS، Windows، Android/Termux
دانلود:
https://github.com/CluvexStudio/Aether/releases/tag/v1.0.0
اینترنت آزاد برای همه! :))
بزودی توی Defyx و Oblivion هم اضافه‌اش میکنیم!
داکیومنت فارسی/اینگلیسی هم کامل نوشته شده توی گیت‌هابم حتما بخونید:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/MatinSenPaii/4471" target="_blank">📅 22:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4469">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oMWT0pU9hPdVNoj5wr4g_tXwWoPaMx7qsGOEY8INemRqUgpJYy7PDWPqOaV_iDL-xVyMlKW0rzrSYqGHdGYtRLj0kIRN2CwVzj1sBbdrOhyFaXRDEfXTj4YQlSpeJpITk4qTDhgqEXcJqTbhdDjbkyWyX7uzgtdiMVoWzcZD0l2g-ix6mMoJZWl9SPSLUklPCKIIoXFO5NF4LUdywi86d6LlhVVAGQsZue9rY6o0c8x_NMWRD6B9dEadRZn-GFbWf0ddiX4v4ldl2Udmx5CqrJDqK-57i73qlSuHC9DqXi2BvRYN-EI1m2OfNa_Lvtld9_x3wpT_rg78p_1IQKuZHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vgNNgU2y5jOL18MI11gKf1Boimg5nRzUDaIWR7SnQ8cQs8UXHKbL-Ee_a9DmZlRUyyZ5iZm0ebnE9mcGO5wPV5dSxQltuol5D5mwOJrEztZcBKvE5h4ppnfsaQ0KsQ1aYHeyRQq9ysOmIK3KaOBdGFRSIpL1Jj-Ski-NWKtwtBHYmtxgtrqdIvbYIIFdcO1XMb6E6k-QnIvsaEXMZrGkFuJNiNyl9qEcZNzkk2-wvIeCtCirfkgNXbjReH8Eg1D_FY7KfSHDYW85G9KK_UBMEGF2LmIIrQnfINBTqAfzfEbuaCfWrFd0Hwpn9lPD3Mm2qe7qqEuFhj-T_VOLdsg6CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از کلاد خواستم که
https://github.com/Graphify-Labs/graphify
رو نصب کنه روی پروژه‌ام(کارش اینه که کل کدبیس رو تبدیل به یه گراف دانشی عظیم می‌کنه تا Agentها به‌جای باز کردن مداوم فایل‌ها و دنبال کردن importها، ساختار پروژه و ارتباطات بین بخش‌های مختلفش رو مستقیما درک کنن) و کلاد ازم پرسید داداش مطمئنی میخوای اینو نصب کنی؟
زدم Proceed که آره مطمئنم
دوباره رفت یه کم دیگه گشت
گفت ببین این پروژه تازه سه ماه هست اومده، 86 کا استار گرفته روی گیتهاب. خیلی مشکوک میزنه. نصب نکن چون امکان نداره یه پروژه یهویی انقدر پیشرفت کنه
😂
😂</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/MatinSenPaii/4469" target="_blank">📅 21:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4468">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ly_8C_BvUKp0XIwjp9biG-KPvhfcPEn0I9pUfckv06iN7XIAUY0JDehP39wilhoIOH7a7vewTIc0KGJEzgtfbfC40oqEz5FtJMY_hEWDg503VqBrD1tafKC_RHRQeDPjFcVFN-8R46y0U-LbIf-J1FfvwB0W0Zqa5ddxnT1UrSMQY4MvvpcFkIywQuMhk69L73dHfqZei9_ypXiv0qGh7kL8qlrNDG-N8rHAhmGG-PhLjVCJUkwnVMM-dGGSGU3j4KF7GrKThq6PKYws2iSdj1WTjZngVx8OKusIGc4k-PIpnZQR_1uaQ-JxBUGEnXQAgH-zMssKhQEkEf5-xR7MJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا گویا دامنه‌ی
t.me
مجددا در دسترس قرار گرفت بعد از توییت پاول</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/4468" target="_blank">📅 19:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4467">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ببخشید.
خودتون میدونید دیگه بانو
❤️</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/4467" target="_blank">📅 19:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4466">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/a54ac3d5b4.mp4?token=fzNzXcU_19f0yRJh9ZT7JFeQVyhhySj_sSy-9nq5Jla0ylFiyL2Ez9ntQbmptm_edi7sNZUWEivJZLYW-bejHqfx6p3Kw0F1zfCh74P-AkHojlLjCPejzpjh8Dzzs8QkfV4AmOl1AJ_b2TpErQb2gC1Va7eDXTXofT86_KwFv0JZT1bs1vfmJUE_4-zyhPmDEwLjhOtT9vOwARyq19oidJ1pdT7kXGa6kTWR1rYU2Me5Gaexq-woZe-7p-53QwMY6HT5ZjWxaN77z6rmHR9OeLrceKO31Z9Y0JP_iWGeQ9bhMt2dAi9tPMfEJKnLgffYPvO9RwUZc_QMSWVmF5SEKA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/a54ac3d5b4.mp4?token=fzNzXcU_19f0yRJh9ZT7JFeQVyhhySj_sSy-9nq5Jla0ylFiyL2Ez9ntQbmptm_edi7sNZUWEivJZLYW-bejHqfx6p3Kw0F1zfCh74P-AkHojlLjCPejzpjh8Dzzs8QkfV4AmOl1AJ_b2TpErQb2gC1Va7eDXTXofT86_KwFv0JZT1bs1vfmJUE_4-zyhPmDEwLjhOtT9vOwARyq19oidJ1pdT7kXGa6kTWR1rYU2Me5Gaexq-woZe-7p-53QwMY6HT5ZjWxaN77z6rmHR9OeLrceKO31Z9Y0JP_iWGeQ9bhMt2dAi9tPMfEJKnLgffYPvO9RwUZc_QMSWVmF5SEKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای خودم نگهش میداشتم
👍</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4466" target="_blank">📅 16:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4465">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">Lira’s first challenge
🌟
به اولین چالش لیرا خوش اومدید!
🤍
این چالش برای همه‌ست؛ فرقی نمی‌کنه تا حالا از لیرا خرید کرده باشید یا نه. فقط کافیه توی این سؤال با ما همراه بشید، چون باور داریم گاهی یک جواب ساده، می‌تونه پشت خودش یک داستان قشنگ داشته باشه.  اگر…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/4465" target="_blank">📅 16:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4464">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLira.</strong></div>
<div class="tg-text">Lira’s first challenge
🌟
به اولین چالش لیرا خوش اومدید!
🤍
این چالش برای همه‌ست؛ فرقی نمی‌کنه تا حالا از لیرا خرید کرده باشید یا نه. فقط کافیه توی این سؤال با ما همراه بشید، چون باور داریم گاهی یک جواب ساده، می‌تونه پشت خودش یک داستان قشنگ داشته باشه.
اگر برنده‌ی این شمع می‌شدید، برای خودتون نگهش می‌داشتید یا به کسی هدیه‌اش می‌دادید؟ اگر هدیه‌اش می‌دادید، اولین کسی که به ذهنتون می‌رسه کیه و چرا؟
برای شرکت توی چالش:
⬇️
در کانال لیرا عضو باشید.
⬇️
این پیام رو توی کانال‌تون که پابلیک هست فوروارد کنید.
⬇️
به سوال بالا پاسخ بدید.
🎁
جوایز:
🥇
نفر اول: یک شمع کروم صدف لیرا
🥈
نفر دوم: 15% بن تخفیف
🥉
نفر سوم: 10% بن تخفیف
مهلت این چالش تا ساعت 12 امشب هست و نتایج چالش فردا ساعت 10 صبح در کانال لیرا قرار داده میشه
🩵</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4464" target="_blank">📅 16:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4463">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مثل اینه که یکی با Toyota دزدی کرده باشه
برق کارخونه تویوتا رو قطع کنن تا دیگه نتونه ماشین بفروشه به دزدا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4463" target="_blank">📅 15:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4462">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوب آموز(m J)</strong></div>
<div class="tg-text">دامنه t[.]me تلگرام به دلیل تحریم OFAC آمریکا از دسترس خارج شد.
در ۱۳ جولای ۲۰۲۶، دامنه کوتاه t[.]me تلگرام (که برای لینک کانال‌ها، گروه‌ها و پروفایل‌ها استفاده می‌شود) در سطح جهانی از DNS حذف شد و مرورگرها دیگر نمی‌توانند آن را باز کنند.دلیل:
ثبت‌کننده دامنه .me (Identity Digital) وضعیت serverHold را اعمال کرد. این اقدام مستقیماً به دلیل تحریم‌های OFAC (دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا) بود. OFAC شرکت First VPN Service (1VPNS) را به لیست تحریم‌ها اضافه کرد — سرویسی که به حداقل ۲۵ گروه باج‌افزار (از جمله Avaddon) کمک می‌کرد تا حملات خود را پنهان کنند. یکی از شناسه‌های این شرکت، کانال تلگرام t[.]me/FirstVPNService بود.
چون نمی‌توان فقط یک لینک داخل دامنه را بلاک کرد، ثبت‌کننده کل دامنه t[.]me را از DNS جهانی حذف کرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/4462" target="_blank">📅 15:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4461">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جوری نوسان برق رو اعصابه که هیچ کاریمو نتونستم برسم کل روز. نه سه راهی روشن میشه که لپ تاپو بزنم شارژ، نه نت فیبر نوری کار میکنه کلا قطع شده از صبح، نه آنتن درست حسابی مونده و همش قطعی داره، نه کولر کار میکنه که بشینم لااقل یه کتاب بخونم🫩</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4461" target="_blank">📅 14:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4460">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جالبه که هیچ توضیحی بابتش داده نشده
هیچ واکنشی هم از سمت تلگرام هنوز ندیدیم</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4460" target="_blank">📅 10:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4459">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگیفت بازار | Gift news(𐌼𝛜)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXosbzdzSzZVO-vFNuaHYPBNb2AGGtPFRlJniBpernDISNsvCVMhWz-Bi3K6BF0iQCLoXDv-w15jQavVu36DLWpaNPLjct4gRg0vyMQ9054aSCzAcCb0ARD0y_h9dcUnADfQr4JX2ufkcmOZlX14zCXwT9NmfQlImPfCHkKqmeGcrOb31q-fQhldl791UtMlNvS-egsy_5hc8d8f9p8Ovn-sLY1Cbnw-aKmang4ZEZex2wuQbf4ASa8U4n5SvbB5CsikFkOg7e0tqpoEZXhVLL0n1xfn_MKDsDcj31OLUmO5eC6SFUVlN3SfFyIdk2wZS7aXdXfpgY8gzF-6cxUVow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
اختلال در لینک‌های
t.me
از ساعاتی پیش، کاربران زیادی گزارش داده‌اند که لینک‌های
t.me
باز نمی‌شوند.
⚪️
طبق اطلاعات
WHOIS
، دامنه‌ی
t.me
از ناحیه‌ی DNS رجیستری .me حذف شده؛
اما همچنان تلگرام واکنشی نسبت به این موضوع نداشته.
ℹ️
اگر امروز موقع باز کردن کانال‌ها، دیدن تصاویر گیفت‌ها یا ورود به بعضی لینک‌های تلگرام به مشکل خوردید، دلیلش همین اختلال است.
📰
تا برطرف شدن مشکل، ممکنه بعضی از لینک‌ها و سرویس‌های وابسته به
t.me
به‌درستی کار نکنند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4459" target="_blank">📅 10:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4458">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الان برای یه سری کار داخل فتوشاپ، چندتا اسکریپت با Claude (پلن رایگانش. توی صفحه چت) نوشتم که کارم رو 20 برابر سریعتر کرد.
بهش فکر کردم، و به این نتیجه رسیدم که اگه فتوشاپ بلد نبودم طبیعتا نمیدونستم میتونم همچین کاری کنم.
از طرفی اگر از قابلیت‌های AI باخبر نبودم که میشه اصلا کارها رو باهاش Automate کرد یا لااقل، پرسید که "آیا فلان کار رو میشه Automate کرد یا نه؟" هم مجددا همچین چیزی به ذهنم نمی‌رسید.
اینه که شما به صرف بلد بودن کار با AI شاید نتونید از 100 درصد پتانسیل یه ابزار استفاده کنید،
از اون طرف به صرفِ "خوب" بلد بودن یه ابزار هم اگر از AI استفاده نکنید و سنتی کار کنید، به راحتی عقب میفتید.
هر دو با هم عالیه!
<تجربه‌ی شخصی. نه Fact></div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4458" target="_blank">📅 09:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4457">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
انتشار نسخه نهایی و پایدار MTProxyMax v1.4.0-LTS</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4457" target="_blank">📅 09:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">📱
دامنه t.me تلگرام تعلیق شد؛ قطعی ناگهانی لینک‌ها در سراسر جهان</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4456" target="_blank">📅 09:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">توی علم روانشناسی به «جوک ساختن با قضیه‌ی جنگ یا قطعی اینترنت» می‌گن طنز سیاه (Dark Humor) یا طنز گالوز (Gallows Humor). این یه مکانیسم دفاعی برای بقای روانیه، نه نشونه‌ی بی‌خیالی. مخصوصا سر قضیه‌ی جنگ
1- جنگ یعنی استرس، ترس و درموندگیِ مطلق. اگه این حجم از فشار رو سرکوب کنیم، عملا از لحاظ روانی مریض می‌شیم (و همچنین در بلندمدت می‌تونه ریسک PTSD رو افزایش بده.). جوک ساختن مثل یه سوپاپ اطمینان عمل می‌کنه و بهمون اجازه می‌ده این فشار رو به یه شکل غیرمستقیم تخلیه کنیم. (در عین پذیرش واقعیت، تحملش کنیم)
2- خندیدن روی بدن جواب می‌ده. سطح کورتیزول (هورمون استرس) رو می‌کشه پایین و اندورفین (هورمون شادی) ترشح می‌کنه. تو شرایطی که ضربان قلب رو هزاره، مغز با یه میم خنده‌دار، ترمز دستیِ استرس رو می‌کشه.
3- جورج ویلانت طنز رو جزو یکی از «بالغانه‌ترین» مکانیسم‌های دفاعی طبقه‌بندی می‌کنه. توی این حالت، ما واقعیت تلخ رو انکار نمی‌کنیم، می‌بینیمش؛ ولی با طنز یه فاصله‌ی ذهنی باهاش می‌گیریم تا بتونیم تحملش کنیم.
4- وقتی دوتا کشور می‌جنگن و موشک میره و میاد، شما هیچ کنترلی روی اوضاع نداری. اما وقتی باهاش شوخی می‌کنی، مغزت حس می‌کنه حداقل روی «روایت داستان» کنترل داره. با خودت می‌گی: "من نمی‌تونم جنگ رو متوقف کنم، ولی می‌تونم بهش بخندم!" این بهمون حس Agency و قدرت ذهنی برای مقابله‌ی نسبی با این قضیه توی ذهنمون می‌ده.
5- توی شرایط ترسناک، آدم‌ها به شدت احساس تنهایی می‌کنن. وقتی یه جوک مشترک می‌سازیم و با هم بهش می‌خندیم، یه حس همدلی‌ای این وسط شکل می‌گیره که تاب‌آوری جامعه رو مقابل این قضیه بالا می‌بره.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4455" target="_blank">📅 05:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4454">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mMih420tV6uoHRfqKnos9wMeiiPz_x89KrwORl7jBqxE4m4GFLzdrJZLCxzMdckvrktoOKCSOJvKLYl4dox2ubBdlje0RUumLgCQW4IH3qjxymjj2C1ciGvrylKLBX33Kf89Nk_BUFsAcoRZcmSHILiZ2MEhY7N3ChSpQCqXijV_H5jFiL4Wy2JVUsUDu7DK5kkr0rsDAO8lVZqaKCkR5295ZyWFRWN0TzZA2zAaqO0UzXQYv_n08dzsJsF6s6o_oQGf4_E9ywQNrSdWjeDEpV2reQbT_7Eoc-7xrmJ7wXGNUNSXb3NRXQG5sm3v1tAkXxgX7WrFC6ar4hqSYsb1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتباطات زیرساخت در حال لحظه شماری برای دستور قطع</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4454" target="_blank">📅 01:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4452">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v0syYWETXK0T0PKn8RMltJfonzlWB0wGFWIFK5tBuNqMiyrhakaNDqzJPKyT4LQ8tMRI7fOBtAkxonWrWaKvolnZaHyX_UWAFHBEbP3yJniyyF1FTkN8xokmKFRlXE3mbfod3vtZQHefn6Nk8dajZiKmqx6qszECPSO7r_jdf9sc6smB0O2n7XARmsN7ETACAYY8iaPWiPBmUno12g5-DU8rEhkzYsCKicyaM8crsdvuVsY8qBT1J2Pz3E5-BySxgOf1cCvntxgLE-0pkx0sGxgViZKCKQbUsvr-6kbF8h5WHww_dVs9Shus-fiwljEncJFmLYCvMofy0UMhQgl3ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oerNw-ssoiDBAG2aQuLPOrouQoN1UE-I9fA4WaSW8C-1gIQ6S0Qj-M9NrpoG7y0WxLWrf-Kvb4EkzNr3xpnA2zikBp7AwG7YrjntyyxZVDzeaY-gQO48m5Z6tvvGl1jfSmaSSTSnCVJo1Pbw66-twJoI6QtFz-7co9OaKHarmL1YFHIVts1wVXmpHY9-UY0OrNtb-SlhU9n4PSmHRXgszmVXVTzn-dRghvPoMCr9BaIsPH6102cVZPDbfoaHcNqgI2TWWC0biPTDsz3hZHABj1CnUr3KQgcP6v11hL-umyO8v77hVTqJ2xzgrinyX34c0VP7o8MNWLxMeSfxvtT91A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم من یادآور خاطرات بدی هستم متاسفانه
😂</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4452" target="_blank">📅 01:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4451">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4451" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4450">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">Android</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4450" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4449">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Desktop(mac-win-linux)</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4449" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4448">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">Master-White-DNS-@MatinSenPaii.zip</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4448" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4447">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">امکان دانلود کل ریزالور ها به ربات @dns_resolvers_bot اضافه شد   @WhiteDNS</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4447" target="_blank">📅 01:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4446">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad👑</strong></div>
<div class="tg-text">اگه دیدین جایی نوشت
تهران رو زدن
ثانیه بعد نت قطعه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4446" target="_blank">📅 01:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4445">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jjJHGhaOjgt6v0d2w7H9gDNJIN6GgFz-cR0pcDLAcrIp10WmmEhkLctQ4d6wPGDwDGiviPYN-uR6VjoNOGcMnqAtrI9P2hzFySCzzkn3IfFt1rFSgZXCB-xndZJeREwhNClNvKCNdJtd3L3vdHliYU4aMRAYBPLfosED1Uy8R6DcipQ2odZOl-Z0WHgDcQsmJtSTAgsg7tlMm_Fkcccs4QnV3QvJaK5ertF76CWjTsFL3FBesKB-HhjktJquzvkK7b9maWTwB0xN6wy8IFkrFobX0BXgtxTSTdTfVqMvGAuBBV6CwEbaNHcE7szv-FnClX1c4l0F1Ur7kJS_J86KbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4445" target="_blank">📅 00:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4444">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">صابرین نیوز داره لینک چنل سروش و روبیکاشو میده.
این یعنی به زودی نت بای بای
😭</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4444" target="_blank">📅 00:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4443">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsWB0f_hchsknIziu7Ohoy5jAAHaUHbMACJF0BykOfH31i17SNlgMYe-a6IPBfFglMp003vQrDy4Wjvp1cvK3E8sd7u1afYyHuHFPphY8ridKzLdhVoSYy7YPWwYMQCADf-31tXPtsuixR211-YhY6ORVfnh2WFbz-dIOHi-fGxmEN1xlV64OouUkN0dLDLQZ2kMItsdZMdhmq8wA96RPTalM0soeoKaB12IoDAY3l1GdC-GxeByPfMUOGHipvNmYYfv2Vjm2Bg0ExIo9apFJuYsGFCnOVhq_LUL0_yeXuu5DxkdcVHVCJ1bLG15gZnV95VgGMWrKvLXnvbX7J0a4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Solomon’s paradox
“انسان‌ها معمولاً می‌توانند برای دیگران توصیه‌های منطقی و عاقلانه ارائه دهند، اما وقتی پای زندگی خودشان وسط باشد، اغلب نمی‌توانند همان توصیه‌ها را به کار بگیرند”
روان‌شناسان معتقدند آنچه ما را از تصمیم درست دور می‌کند، کمبود منطق نیست؛ بلکه نزدیکی بیش از حد به مسئله است. هرچه یک اتفاق بیشتر با هویت، احساسات و آینده‌ی ما گره خورده باشد، و درگیری احساسی در ما ایجاد شود، احتمال سوگیری ذهنی بیشتر می‌شود و تصمیم‌گیری، سخت تر.
البته که احساسات، بخش مهم و تاثیرگذاری در تصمیم‌های هر انسان است؛ اما زمانی که فرد با موجی از احساسات مواجه میشود، ایجاد تعادل به مراتب دشوارتر میشود..</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4443" target="_blank">📅 00:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4441">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!   یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم Rowboat. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4441" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4440">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4440" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4439">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YB4NnvGLPhYSwInnm6QlCVWjjPttTqq4E7YwB-1R0bx3mRYVXJMDAEQvx3D0T0tO2K5zvxnGtekc9Bt6Efz66IWGhdhUkSVUGgbyDeDTMv_Zln3jv9aJFrZmOFNzZj8crJye-oE3vb4_1elF7mmIQCbToJXlYuV-vfmRACoQuAD26Dshm_ODUd-LYtRd5-2HQP31RdyTCbqdR94mZUyRQEmKx1yjk0scOH3851aohHlBwb28tK-JBF3bBXC9C1ePyZUoCBRClUpE0XBFjVSkWOirMtXxGXmtABzMoIL8RFn4xAxxAhbwqidJ4PLHO8y5EBiVYl520YugL9dfyZRzJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">8- بخش پایانی Integrations:
از قابلیت اتصالِ One-click به اکثر محصولات و ابزارهای پرکاربرد پشتیبانی می‌کنه.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4439" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4438">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gAbOBbJacvMeNqOCP0gnkMIOt-1UH9P9cgrul905WhnPEAgzEGY8iiJwqCtjL6UGtM9O-OUp7HKkdIGNSmkUol1VbZwB6ojLt_8NG1Xpv5UKG2q8iWmZX7Um8Y8akA3cJH_RjY_tzVzLRTdKZPO_B5qkewQYmxgT5wNxUA82jcnwEPBTWGDXwzoViwpnAQuVhrkiPNnGsg4KQYkOUuJhQewVUl7sykJofRF9FGwoAsFG4X0M_gMCEUEme-R_ud7e5fqeLgkOSmB-fJTyea_jRlT9LKePbG8Mf9gt8n--MLdf9zb4DvxaVHCX8rgKEHV5NLgk9yQINRuDrr_BNIZG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7- بخش Apps:
می‌تونید فضاهای کاری اختصاصیِ خودتون رو داخل Rowboat بسازید؛ این اپ‌ها به تمام ابزارها و اتصالات دسترسی دارن و حتی می‌تونید اون‌ها رو با بقیه به اشتراک بذارید.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/4438" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4437">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MepJhh_A6SjIaealz2de4YAtLvgnOkBRZj79ozTlvPNeg7DwG0un97NJTnr5PacydW-liuG5xyXK7fMSfBLikFLdNtG9ENoEeQjQywduva9VVgpQCwnsH5-yVuiNFoTypDJelORTFBcWO2NNdPPMu3o5c5TCfFeRLSTpSVVPg1qdL43L4pNU14D4r7NDcNGwgP0XA58KSDJX7xTT7fDw0jU4YBEibc2Icf4ebrPvy8ohdyf6eT5iJWs8e9BoHdZEwm-OMsPY9VfcI_4iiioM-nU_fJX1JWoeyLx_SldvxWusN5dhybnoLPyb6qu8CzVq2KsxWn9AuZUIsXNwCRMhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6- بخش Code Mode:
این بخش بهتون اجازه می‌ده همزمان چند تا ایجنت کدنویس (مثل Claude Code یا Codex) بالا بیارید تا Rowboat با استفاده از کانتکست پروژه‌هاتون، اون‌ها رو هدایت کنه و کارها رو پیش ببرن.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4437" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4436">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aJRl_mtuzaq3ixFHE-2Hm6Fbd7Ew-nWwNWr1EV4kf7jSLkZcrCrCMtjj3vbRbVJdqJMRuw3y2U_y7Jc-NAlYYMXmANZfVLBZQ42P_yB3XQXVnHCxxzfyyMauMJma8D3JvbW7B6WfJ5C_9jiCMZW_Xp_pXNl-ej47jCJrcukY9BPrLrQqbA0fp03lXhnhuIeAe7-fyPNy6tPmOVvjfPqUgCRZ-7FXqS1uXJQC1UzWPb6n3gVh2YRAbqDqqTnLH5XC7UP-sE4ukc1oaHMioMR-r_banMo88OUvVcHI81OsBL3aegTkT-p-LuMrp1PjQctTgoTNXGNj4S6F7X0wCpLAKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5- بخش Meeting Notes:
یه دستیار محلی داره که مستقیماً به میکروفون و اسپیکر سیستم وصل می‌شه، همون‌موقع صحبت‌ها رو تایپ (ترنسکریپت) می‌کنه، در نهایت خلاصه‌ی جلسه رو تو یه فایل Markdown بهتون می‌ده و گراف دانشِ سیستم رو هم آپدیت می‌کنه.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/4436" target="_blank">📅 22:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4435">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fYhEtEIrQkKfHkEm82A-WlCi60ttAD_mqqO7Mg6usPxOELycTCotkjxmU8eqLcWKUIyujcYV1pQJxaDZ2GHQTkxV37zKvgkuEPHOsmsoiSoBkUy59uIu2shJpbzMIdJGJS2BvxBHh15auHBeo4t_cGytcPjDRBG30oul1n1pLxyX6hb6mQStlUVq8K6OD1HUVJ8YXjcl8szLxOSds0lP9Ppn6GjIcXIIE8y8drknf4TGRac3ja9eDXXle76pIWlAse2PY9ZkyWUsoygdG9xTjW71WkZPmYaAoWXazLB0Jz0hMtgVAj5wdVFNTvhm1RX7wxdsrWZkYVgYjSn-ikyT-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4- بخش مرورگر اختصاصی:
یه مرورگر  Built-in داره که اجازه می‌ده شما و دستیار هوش مصنوعی روی تسک‌های وب با هم کار کنید. چون این مرورگر از مرورگر اصلیِ خودتون ایزوله‌ست، می‌تونید فقط تو اکانت‌هایی لاگین کنید که دوست دارید هوش مصنوعی بهشون دسترسی داشته باشه.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/MatinSenPaii/4435" target="_blank">📅 22:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4434">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tnulz24_keWDIjtxomLWir8MLAc0DY1mVHXJ2JaA1vEzhsk9cXdw2Xeqs2ZhrzYfX9W2cGmXTiT1DNOyQrYiBReJ2r1reLcdhiiHehJUMeddaFTCRbl45OXCxFfVW2j5EHztE2L4Hy9-M2fRA8OKXaJcpbwi7cX9_VNKxq-U6NNysPTfJjpU6Zya8Hg9SzBKfRsogdwXvd7QIHanEDxnX9ewSaQCZLNN-m2aFMeX5zbxlAw0xg8K-C6jITrUd6LcONER-DOwmULyOGOQJA4aCDCWzKbx9GSwPWk8Egf4Ntc0AHk6y5Gdsnm6ATcazgPUNQsL4ZUg5oSDkSs02wYwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3- بخش Background agents:
می‌تونید ایجنت‌هایی بسازید که بر اساس یه اتفاق (مثلاً دریافت ایمیل جدید) یا بر اساس زمان‌بندی (مثلاً هر روز ساعت ۸ صبح) اجرا بشن. این ایجنت‌ها می‌تونن به ابزارها وصل بشن، تو وب سرچ کنن، از مرورگر استفاده کنن و حتی با Claude Code یا Codex براتون کد بنویسن.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/MatinSenPaii/4434" target="_blank">📅 22:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4433">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/la_4TT_VymSthA41cyNRK1uTk-tCV7QlljULMrzfb8K1NarEhGD3-PutFDkgaHbf-N1D6wlA_dukXSpfwXPl-twCdN5d0_Z2PqxNo8mRjNpampPc8i8z4dGIF3yd4gwM57gMJRO8WoSGwvwxZQ1GYpYAWF5mUq4VCZHeqH6sRjqRYds0RFqZ7A4d2vAbvlGs3VghxUfhgoYOx24kppyB7FkLBhl-mKsILMZg8ycVaRK0IC2y9ziEqImVUq1yanEEH0zUgk9-B5kxGz3hT65f1tyDVE2bjx-WtH6xFUpKnbEUhjDn94TJ0ua4-lXywB9MDh_qSf59UZx1zeee1af_EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2- بخش Email:
یه بخش ایمیل داخلی که ایمیل‌های مهم رو از بقیه جدا می‌کنه. بعدش با استفاده از تمام اطلاعات و دیتایی که از کارهای شما داره، به‌صورت خودکار برای ایمیل‌های مهم پیش‌نویسِ جواب می‌نویسه.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/MatinSenPaii/4433" target="_blank">📅 22:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4432">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rLA7XHZwDnnwH4hpFuyx9qdxQcaQd2EFBoVJlms-kKg3xqIEpEkhcO4tWJm0w5eXfH5GMkeFshGb-3797X4yZ9gcZzQE8qAPwslMHK9wKCLc9K0JEhgFQ1WQW7m4S1D-vi95HfHuohFqPAPVDVpJKxU-S7uXkfESwwUyDBUHZToHZtedryV3bWpACUiBZeMiCOdG45Tw5_irvbexfgAjtH9YMMg-ZQwxxzF7WyfxLGupdC89a4OrnaXNlwCRT3tk5KaJxf2dYjlAau71tRi2NFOz86koC664y-6N86t6NJhXkIMWZ5DtJxnoaUkBcgSEnVzHye-3g7oY8jT3PfSUMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1- بخش Brain(مغز)
کل ایمیل‌ها، جلسات، پیام‌های اسلک و چت‌هایی که با دستیار داشتید رو به یه گراف دانشِ به‌هم‌پیوسته (دقیقاً شبیه استایل نرم‌افزار Obsidian) تبدیل می‌کنه.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/MatinSenPaii/4432" target="_blank">📅 22:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4431">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بذارید تک تک نشونتون بدم
👀</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/4431" target="_blank">📅 22:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4430">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TniKga9DnfrjaQs9Ev8A0k2y9i7TAcLT0IkNrYQNcsEVmXzCFF45OzjvHXU68YZ3Y-WEu-EdUJ9iObgtZM7TT-C7WoELIfWzyynmNep7vVBI6C8tsuJUFrK4AsaxYeJWNGauvcg_hd6NN1dD0reivoJeKcV5IqkTaTzfsc6vFHIATyFH5XILXK-ZagX1sNaeMVJqK_6lhxb3xPDXMet5PNDGqNYYNLRs9QeHf8uiZs5jzsD3vI9TsA_O9o24-LexeZ085nOc2SBjnrRhPv505r2vIuQ0GvMsF3PHinjSO1CoPEtfc1JQtnaZ9FrScYp28tsKoGiNRAHK4vTEcBqnvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!   یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم Rowboat. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/MatinSenPaii/4430" target="_blank">📅 22:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4429">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cYM9GQIOlkdr8H5royHjPrOzyw8mkIsNqpV-UU0SoYc0zD2kW-AfIXaEk-XKEmWdGuZj7XJTOS6JdxNFPo3cWze_syr0sB3hklhUG03AW9AKVJNQ5mBGqbQP3Vqj_qGUfQz4LqbdZdie7bvRofIlYmNJ2wkYv-izfRJ8w2s8bX_6f8zbHMZ5W-dlbLIAZ6ZNy79r95TGOx84PeOw-YQXEJlawBWn7A1w95RfIjTk--y52PuH6bwu2H8v424pqNr4L-gLzEpuiQZJnD8f7RDSwck05H81ucOc1Dt63V-N80w9Q6dFiv9TSp3_VoLEv77hdAe0_un_d1Lpf36bMA3vPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!
یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم
Rowboat
. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر اومد، اما بعد تفاوتش رو متوجه شدم.
کار اصلیش چیه؟ اینکه یه گراف دانش (Knowledge Graph) زنده از کل کارها، ایمیل‌ها، جلسات و چت‌هایی که باهاش دارید می‌سازه و با استفاده از همون اطلاعات، کارهای شما رو روی سیستمتون انجام می‌ده.
چه مزیت‌هایی نسبت به بقیه داره؟
بیشتر ابزارهای هوش مصنوعی فعلی وقتی ازشون یه سوال می‌پرسید، می‌رن همون لحظه تو فایل‌ها یا داکیومنت‌ها سرچ می‌کنن تا یادشون بیاد جریان چیه (RAG). اما فرق اساسی Rowboat اینه که
حافظه‌ی بلندمدت
داره:
- اطلاعات و کانتکست کارهای شما در گذر زمان روی هم انباشته می‌شه (مثل حافظه‌ی انسان).
- ارتباط بین داده‌ها و فایل‌های مختلف رو به صورت گرافیکی (شبیه گراف‌های Obsidian) بهتون نشون می‌ده.
- نوت‌ها و یادداشت‌ها تو دلِ هوش مصنوعی مخفی نیستن، بلکه فایل‌های ساده‌ی Markdown هستن که خودتون هم می‌تونید ویرایششون کنید.
-
همه چیز روی سیستم خودتون ذخیره می‌شه
(Local-first) و دیتاتون تو سرورهای ابری هیچ شرکتی رد و بدل نمیشه.
امکانات و بخش‌های اصلیش چیه؟
-
🧠
مغز (Brain):
کل ایمیل‌ها، جلسات، اسلک و چت‌ها رو به یه گراف دانشِ به‌هم‌پیوسته تبدیل می‌کنه.
-
📬
ایمیل کلاینت بومی:
ایمیل‌هاتون رو دسته‌بندی می‌کنه و برای ایمیل‌های مهم، بر اساس دیتای کارهاتون به صورت خودکار جواب می‌نویسه.
-
🤖
ایجنت‌های پس‌زمینه (Background Agents):
می‌تونید ایجنت‌هایی بسازید که مثلاً هر روز ساعت ۸ صبح یا هروقت ایمیل جدیدی اومد، برن وب رو بگردن یا کد بنویسن.
-
🌐
مرورگر اختصاصی:
یه مرورگر ایزوله داره که به ایجنت‌ها اجازه می‌ده فقط به اکانت‌هایی که شما بهشون دسترسی دادید وصل بشن.
-
🎤
نوت‌بردار جلسات:
به میکروفون و اسپیکر وصل می‌شه، صدای جلسه رو ترنسکریپت می‌کنه، خلاصه‌ش رو تو یه فایل مارک‌داون می‌نویسه و گراف دانش رو آپدیت می‌کنه!
-
💻
حالت کدنویسی (Code Mode):
می‌تونه همزمان چند تا ایجنت کدنویسی (مثل Claude Code) بالا بیاره تا بر اساس کانتکست پروژه‌هاتون براتون کد بزنن.
-
🔌
پشتیبانی از MCP:
می‌تونید راحت به هر ابزار خارجی مثل اسلک، جیرا، گیت‌هاب و توییتر وصلش کنید.
آزادی عمل توی انتخاب مدل
یکی دیگه از ویژگی‌های جذابش اینه که می‌تونید مدل زبانی رو خودتون انتخاب کنید. می‌تونید کلید API خودتون رو بدید (مدل‌های ابری) یا اصلاً از مدل‌های لوکال (مثل Ollama یا LM Studio) استفاده کنید تا حتی پردازش‌ها هم کاملاً آفلاین باشه.
پاسخ خود هرمس به تفاوت این دو ابزار:
۱. هرمس (من): یک دولوپر و ماشینِ اجرای تسک
من برای
انجام دادن (Execution)
ساخته شدم. رابط گرافیکی سنگینی ندارم و دقیقاً مثل یه دولوپر سینیور تو ترمینال یا چت تلگرام نشسته‌م. تو از من می‌خوای یه اسکریپت پایتون بنویسم، داکر ایمیج بسازم، یه ویدیو رو با FFmpeg فشرده کنم، یا یه کرون‌جاب تنظیم کنم که هر ۶ ساعت اخبار رو اسکرپ کنه؛ و من مستقیماً با هسته‌ی سیستم‌عاملت (لینوکس/مک) درگیر می‌شم و انجامش می‌دم. حافظه‌ی من از جنس «مهارت» (Skills) و دستورالعمل‌هاست.
۲. روبوت (Rowboat): یک دستیار اجرایی و ناظر
روبوت بیشتر شبیه یه
منشی فوق‌هوشمند
با یه رابط کاربری دسکتاپه. کار اصلیش «نظارت خاموش» (Passive Observer) روی کاراته. تو پس‌زمینه ایمیل‌هات رو می‌خونه، تو جلسات آنلاینت صدای میکروفون و اسپیکر رو شنود می‌کنه تا خلاصه برداره، اسلک رو چک می‌کنه و در نهایت همه‌ی این‌ها رو مثل نرم‌افزار Obsidian به یه گراف دانش (Knowledge Graph) متصل می‌کنه.
لینک سورس گیت‌هاب:
🔗
https://github.com/rowboatlabs/rowboat
لینک دانلود نرم‌افزارش:
🔗
https://www.rowboatlabs.com/downloads
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4429" target="_blank">📅 22:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4427">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ET1WpX6uk282swa2QhRg7KdxenwPeY19Cl-iArAEUlrRMtMMmDe7kjZGXrDwP2zAqDs_zGPbdZNCuMfWxvQv3afkQPtGRWAPU05kMs2HF21NJOPl8T8KfxPzjKPKTvTlLt3IewBj5PD9ehT2h5iHV3Ob0VuF_zmg_euJbxpSfGnDXeSVPJCilcLrG_oxesucQRBSLNvqdDf8OBtQjiyIwaAY1fcUlEuomVBHcoYEQLi44_NlcUDG-4WkVRS2ewt7qJCgPmH5dWj0frsBqrIeEr_LFf8y718gzt1zN3fsfG_DF4kEVyR71xErHvd_TOGBmuz_a4JMTYCLKneN_ON7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/18c4e8f180.mp4?token=pughA05M36dvX7SSNgaQ6KgdL0gIab54TNciG1AQUOfpm5ywfSxegziGWQNWw5aAYsMHzWOksEMFWx-yMo7UJUIwIC-siOQF2MF55Dj0KMuipGRAXrL43dNr5YH-Cp9qviyEZTyBd_heNYF-1Xc-Lq0anyJtoKluZo0n7TrcN7AR98NuTGH9JR5hEN3eep6LeZRMnT_ChMwXuJC7aTjzGs7pNBT_owTqSUou_cFTZSN-tZCqNaKsVo6mtqNux_3IwKuMF9_eEXUkkxdZ5YIHGEr9pmRLyFW5Ot-ty6UNORw0MBUHaT2bYZ75_U28dEAxH0SToOrGOltxUubmKcRcsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/18c4e8f180.mp4?token=pughA05M36dvX7SSNgaQ6KgdL0gIab54TNciG1AQUOfpm5ywfSxegziGWQNWw5aAYsMHzWOksEMFWx-yMo7UJUIwIC-siOQF2MF55Dj0KMuipGRAXrL43dNr5YH-Cp9qviyEZTyBd_heNYF-1Xc-Lq0anyJtoKluZo0n7TrcN7AR98NuTGH9JR5hEN3eep6LeZRMnT_ChMwXuJC7aTjzGs7pNBT_owTqSUou_cFTZSN-tZCqNaKsVo6mtqNux_3IwKuMF9_eEXUkkxdZ5YIHGEr9pmRLyFW5Ot-ty6UNORw0MBUHaT2bYZ75_U28dEAxH0SToOrGOltxUubmKcRcsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چیزی که برام ساخت خوب بود. میتونم بگم در حد OPUS 4.8 + Claude Design هست. برای وان شات خوب بود واقعا
اون پایین هم زده هرمس باگشه. مدلی که استفاده شده grok 4.5 هست</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/4427" target="_blank">📅 22:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4426">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P1kB6PhevUNauuq-rYhJzSP8DyNHP1lFTb2VlfSFvwOttLObdPj8U0hZeACorQ4ABGdvmBWwOpjwb_s_QQzUtbBUQm-TeL3Jr2Wg_JoKrFWUlHbIL_TuY064e8mrZMcO6VLt9cuL4NGagZrxGK6r2hEYCB6cQxCRtoI-mLo7hHajJedac5v77AnD-Vmska26SRuthx-oYIa92xQ9eqXeH5QX5KaPG8-FMlbdNUxDyQSco2E9YMHj987xb7or_6n0fjtrEVj_6pu9LUoYov6SOV8MhOiuHQ15WKrvvsA0Z3489xL6u6J25WJpWa-zcWej7-klyaQSfOF9QVf0PDDnHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با atomic mail یه اکانت ساختم بهش وصل کردم مجددا
😁
روی سرور</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4426" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4425">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fSfVpLG56_7g8oXdSTpB3FvJCQz7e7VMvIrLmr-nQOVQri0ZK5OiblAW9wXy0Ee1Yy8Uat0_7O0tRfGqx9X5DrrMdd_jTRaLQfz2t9XFy2jH9KtuCxco3nK-kZMnd2FqQNi45rhiQvRHvfdDfm1cqjRPb8UxRKva0VtKcK8Bv7Pm8aArqxHiwYMd0kpHi_QQiKsjkydKTtvUrRIe0EaFax0_1axBKVJ_sOZupeI0CG3SZVgulLL9EOOlYZEmt7UaNEVo5ktr0doLdIUbk9mU0UR2EKiOUQk254UW3z1dICL0JknqQX2VWQGmNZwlZE1nRrTqBZbwf5T0wEZivl78VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با atomic mail یه اکانت ساختم بهش وصل کردم مجددا
😁
روی سرور</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/4425" target="_blank">📅 21:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4424">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دقت کنید روی ویندوز حتما باید proxifier روشن باشه که روی ترمینال هم تانل بشه وی پی انتون</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/4424" target="_blank">📅 21:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4423">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گویا روی grok cli می‌تونید با Context 500 هزارتایی به مدت محدود ولی به صورت رایگان از Grok-4.5 استفاده کنید(قدرتش هم سطح Opus-4.8 بوده توی بنچمارک‌ها) نصب روی powershell ویندوز:  irm https://x.ai/cli/install.ps1 | iex نصب روی سرور:  curl -fsSL https://x.a…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4423" target="_blank">📅 21:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4422">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RfH0UCmIy5N7kGKx4i9Ja_rmS8vm98YsLfDagHkRd2pUsDX6ZlHMRONtSDSZwIPGxnA4FZOHGaavyRvyVaja0N3D_-hXD8Ci_IiTsu95doQYiAY4idCZshWtad2t7PBIdUpVRRF-rRGP75GiJtoJABE8hiIAxUXC7xKFVn3bQ8FI_86QD_6Y_PXSGDrYp16FQ3_DHa5kZZVZbudfoenoQuzPp8s4PIH14lYq-wqR_7tm6mG1cr8HlCDafk1YxF3oBp-z33E8iBy3P2CES4EUwBjoMkBhXIO3LSJWhA5lKg5htspGm_QGcxzcwQ2ZTjTFcYgURwoABBFIe7bIHkwQwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا روی grok cli می‌تونید با Context 500 هزارتایی به مدت محدود ولی به صورت رایگان از Grok-4.5 استفاده کنید(قدرتش هم سطح Opus-4.8 بوده توی بنچمارک‌ها)
نصب روی powershell ویندوز:
irm https://x.ai/cli/install.ps1 | iex
نصب روی سرور:
curl -fsSL https://x.ai/cli/install.sh | bash</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4422" target="_blank">📅 21:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4420">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NUuvzuiquGA32pshaxtqrvnlGbpkG1f9gPv9_-hbyhS7LdHoOTDVkxT2HaV3GwApj5X2bD9Px5UZyPs7v-yiBwh_EOnKBL7BGM6G0vuj1BB3x6uwJuNwQ8RwJseMSPCoNXrIQDj9193UmU82XFoqN4jkVDeybeICCum4uLlPCsWyvX6ltFIXFa9VQBTE6v1Ltdt9wVlrv5_PCSc9wL8ntw7OadjvAJOtqRJ_OXu_gP31Gdvaldn6nbETOFVdhcuM0Zco8txkbesEqkgNLLQSjuTJBcBuyzQCGwRBQ_ZyUt5j55igq63B0jDfvicVyBg7aR-DWWF8u3ltwcWmiCiNzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u1Xw_0EXJIUWlVrhT4r4TW0LgCbE4TF7J_0DL-tcIOmFTlNzagQoDzTijgI4gbR6BvbrffhVA_oOitpGm7zemshoVTKwk43QKRUjQ4BZafCZjIiBdDBD6ldbnDxET91GFo5J2vJpO5n85HrLqRYkOpgQaasEhziBNk8n_0Uaalz_HtG7f1IM_Rf-GXgJHZOb2li_63yv0NBR5vVrjkr2LYfGZhZDyCiWVPH9Ww5zfFhxp-6NMPF5ebTCDPD9ylzyKgo6z2rP5eioM5ybd2EtmgoUNUWQhKIBBwnO5_2sgY9sAfMu0hvMQi6_wWF4XwmpBzkQQunFL6ikp0Llb0Zm-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم راه استفاده از Meta AI بدون خطای ریجن رو کشف کردم!
با کلی IP مختلف (حتی آمریکا)، اکانت با شماره آمریکا و جیمیل تست کردم ولی بازم ریجن می‌داد.
اما با سرور آمریکا Mullvad خیلی راحت باز شد (حتی اکانتی که با جیمیل ساختم) و کار می‌کنه..
البته اگه مشکلی پیش نیاد :)
++ با فیدبکی که بچه ها بهم دادن ، با windscribe و Surfshark هم نتیجه داده
✍️
AmirHossein JPL</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4420" target="_blank">📅 21:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4418">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R-xt5_V_x3pFz3r2E7qemUgymiF_65XIW5ZIWSlwY3d5m6BzC07ZL7xs9fRzTbg78Qo-f4eybi1WqrNJx4Cc0Nt6zYW1L-D_v5asIOS2vVdaUIReNTwJ8OylApa35cg7sTdo1QH6cjQRQT53Kj340o1k6d5_zEE_3EJV-pveSVReBCiAqAxHur5IHmibocPCD3mNMBrwiO6CCh7mB9Vm20UycQBnHP29Amu_bWDUfQcvCxfjm9RScHSk4Z2oyB5_0cFpTED13979BNstUvZ_0KwYE5OTgsggJJdu3Yt5ErrjXAJn-iHOpwW1Uio2ddxfOwGdnL-923W4ACkidmJ_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/posfrWRBRppgM0q6miD3OUIboCvHebnvW7Na3R-v1ZvoF8U2MKxECO-RPCQFNbCo5FzqLAJzFZUq1XXR2Cnc1gkmRNeEbyfdnhoScoPBbh_Ik1sR-xrL1HSwHApbSUV5OOYIXia6ed6QZ1p-TAVsgPSWsDJFngkzE1SP3-XYiUIej9EUCwpH8nUf_oGsPR_O4v1DEiTwOhcwNZCBUsxhJCBQADcD-1jkcuGBv_6712veIc8l69txOo-xDJ6B0Eq5rfWVzETVKlnMS54GjD1_MwScJqMd0TV-V3MrcUqnqr-8IxyxUIC_3DibkftPKZLsczPzudMyg6Sfjfsw_Sas4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مأموریت شکست خورد بچه‌ها
فقط اون جمله‌ای که آخر گفت</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4418" target="_blank">📅 12:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4417">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eUMtTc1QCK3u-gfdLk8O-XHch9tklQjPCUi93r0Q00JEefppXrzRaPYv7hmtznmGMKbbZknjHZAgwhxkqk3Lude3N0yF5WopEtU9z5qzSG1igZVTnA-d8FnrttY9oPwAjlQqthz-yb2OPTyokM5nRk8kNSy3iZKvTiEbnPhAJ2WjIoOwA1eoq91KkoCQR-MI-AX6RSY2_I6tbIBeWUatvVjz-EOaLxrj8kNwFc2_S4C4d3t4nErzQlnt8CyJ0a4KISJRnty1wVG81eitaf6yuonsJqOWDHhBO7m-93Uv838fEsS9tShgzhdRsFtQPgBdjV6oQGDDZi_omIyGz9n0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4417" target="_blank">📅 11:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4416">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گویا برق قسمت‌هایی از اهواز رفت.
دلیلش هم حمله به زیرساخت برق بیان شده.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4416" target="_blank">📅 03:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4415">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دوست ندارم که ویدئو رو بیشتر از این اسپویل کنم، اما جواب سؤال "آیا AI جای ما رو میگیره یا نه"، اینه که ماهیت سؤال غلطه.
چون این قضیه یه switch خاموش روشن نیست.
یه طیفه</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4415" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4414">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62284d12b0.mp4?token=C13icZ1W6XpHzjJ06_2_DcmzvpfOxtciX3ufBNcde7QGbJbQv9lm6q-9aAkfQdTac3aZ3XgKkc-zfUcex-fkUBzQFshGsvwZWaeX71KjUMBkGPeNNp0ZIJIEgywkN4-dR9vn_GFy2TrdsOh__kP-05AjsLNfv02REdvzr9s-otID3Vafq_iEFg55bN6POP5OFgFbjPulrJR9zMqgvmSblVMybXbkBO3vdCc1AFqQvmtL7CFAZ4yA0T_BpGWzpKgy3LAKUrka4hiz0ZdV2ySEd9ImRxAKk3SIiOVL82244-oLN4eEpcQKyEwQuqwqfEJ9AMYt2BYSWQRHt7D56EKCFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62284d12b0.mp4?token=C13icZ1W6XpHzjJ06_2_DcmzvpfOxtciX3ufBNcde7QGbJbQv9lm6q-9aAkfQdTac3aZ3XgKkc-zfUcex-fkUBzQFshGsvwZWaeX71KjUMBkGPeNNp0ZIJIEgywkN4-dR9vn_GFy2TrdsOh__kP-05AjsLNfv02REdvzr9s-otID3Vafq_iEFg55bN6POP5OFgFbjPulrJR9zMqgvmSblVMybXbkBO3vdCc1AFqQvmtL7CFAZ4yA0T_BpGWzpKgy3LAKUrka4hiz0ZdV2ySEd9ImRxAKk3SIiOVL82244-oLN4eEpcQKyEwQuqwqfEJ9AMYt2BYSWQRHt7D56EKCFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیا AI جای ما رو میگیره توی کارمون؟ ویدئویی پر از واقعیت‌هایی که باید گفته بشه. و کسی راجبشون صحبت نمیکنه پیشنهادم اینه که امشب شما هم این ویدئو رو ببینید. طولانیه اما پر از درس https://www.youtube.com/watch?v=gR2OCyKBF7Y با تشکر از یاشار عزیز.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4414" target="_blank">📅 23:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4413">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آیا AI جای ما رو میگیره توی کارمون؟
ویدئویی پر از واقعیت‌هایی که باید گفته بشه. و کسی راجبشون صحبت نمیکنه
پیشنهادم اینه که امشب شما هم این ویدئو رو ببینید.
طولانیه اما پر از درس
https://www.youtube.com/watch?v=gR2OCyKBF7Y
با تشکر از یاشار عزیز.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4413" target="_blank">📅 23:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4412">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یه گزارش هم بدم
ponytail تا الان واسم توی کدنویسی، فوق‌العاده بوده
https://t.me/MatinSenPaii/4359
همینطور skill improve که معرفی کرده بودم
https://t.me/MatinSenPaii/4373</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4412" target="_blank">📅 23:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4411">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به حق چیزای ندیده. مردم چه چیزها که به ذهنشون نمی‌رسه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4411" target="_blank">📅 23:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4410">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یه دولوپر زبانی به اسم Skillscript طراحی کرده که باهاش می‌تونید به صورت دقیق و ساختاریافته به ایجنت‌های لوکال (AI Agents) بگید چیکار کنن. مشکل اینجا بود که ایجنت‌ها برای کارهای روتین هر روزه (مثل چک کردن تیکت‌ها یا بررسی پایپ‌لاین دیپلوی) هر بار سعی می‌کردن همه‌چیز رو از صفر درک کنن که هم توکن الکی مصرف می‌شد و هم بعضی وقتا اشتباه می‌کردن (Hallucination). حالا با این زبان می‌تونید سناریوها رو به صورت خوانا بنویسید، ورژن‌بندی کنید و با خیال راحت بهشون بسپارید.
که چیز خیلی بامزه‌ایه و باعث کاهش قابل توجه توکن‌ها می‌شه:
https://github.com/sshwarts/skillscript</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4410" target="_blank">📅 23:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4409">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یه پرامپت، سه تا AI اولی GPT دومی جمنای نانو بنانا 2 سومی در کمال تعجب، Meta!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4409" target="_blank">📅 23:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4406">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kETlrNkIeXIEGKvZvvVi9N2-VVNlcYRxauDXCw9qZWs0M5YkESt4R6WjYxMClxfh6L4Fap61ZCzSi2zACeuhXJOWo3iBQ7WLVmFFn9a1r0Zbn3511FwcuF34Xuwt8deRw57llsIIgVAJmW5wMONLqyd-3U7DFJ4zMkKMlup3ba152WAzxeHUdsQwUNfyV4nXm2ICZPYxbnXLS_QZrs8WQ-Fqjp0oCbKQG3IAPJKG6AGpsZNtyzqesFSqM1nSPexx8cO5ebvnqfN7HkGa039Gwi3JqCG17JmKLOLtViz2q_I3Hvi7KJ5ePWygGZLQhJKY8BVfaVcT17BXEbyCJ0bRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oUfGk3Ju94gB8szaNpOhbMBFyhR8Y463IjohRpDVV1hM9a5clpLFbf4SF7ZsRRL5AvVO_WZvkpoETR8mlCMVP5hiIY8HdNfmbN3ayrmx3mP321C3l4qxud7yW0RIMst0OHbNT5K-Ze8Zzz_3yA6SE6R-CwcwoBuqF5bhckpo0Cxl9heSJm7L1RX_6LQPLH0hRjrVjbdShbw-VDwS4REIwv8lh5Wt_q18syQlsdrtMEjz5fZmnmc3VN0xgtsxrb_ylU4d9Fry_2wYVzdEfANQsweGU1YkqFaeh5GpwLdjar6NSNhc69ggrnnG1OVRDzIBLf8ynu4TDohd-5W8ZNj_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ai6T4uUp6SxPH-k5m3PtcrPkW_948BNZ2nQRGBjEEtDSRNUvx65VA02fLdjaVpnXAfXGE2qSxXu96mFTlGD_YrzjJTPOOBickSBxw2Hs36uK9j4PDlTOtezUm7CMC6mNSOtdSe85775lwmxoDntiUm4BldJZI6zifGoYRt4LrAcI9kZEXtWgaEQ2CEYfamb3Ns9ZdftEh3t2CNm02SP5px_iin8geC1apMlzw0v6UZ3hu8AiqKJAh_qnsu0UZ6022Sg505eHww9q6ABdMgQzFjJ9JMmXZSuTSqkyq_OC6rVlvY13D7aGvSGpuHEFLKCHrBkcbFPG_xO6L1q01Up8XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه پرامپت، سه تا AI
اولی GPT
دومی جمنای نانو بنانا 2
سومی در کمال تعجب، Meta!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4406" target="_blank">📅 23:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4405">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hXCKd0bKQWMM-i8stN8-KJo_2gOh0D1VrlsnpciuEu3m4o6FImDROX0f-sovndsAIbg9VoNhLKVpA6MaGzBKjESUiClpw5ON0aaoxKqeAn8qaevUPYgWqTMIUs76ojgALq1pCwsqaDe23wVcWQpuSNC4HZBbzEQUjVHtMkbrTHeH4ZCPzQgrICi_4I96eNXzdTlNY7PKrucL_uqAOetgive4jUvAyEnhMlGXVdQEQejA2LoLu38AvN-WQnvxwqtue-HDMoXOeu7XTC0tv7HUas9QR-2LjFadX_Qx97HHgPmXZmlk2uoXUCLDwqaTTLv_kYLX8aDgA4MtC4N3vgsU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت Theo:
gpt-5.6-sol is meaningfully better in Claude Code than in Codex
It MAKES BETTER DESIGNS. WHY. WHY IS IT BETTER AT DESIGN WHEN USED IN CLAUDE CODE.
و داره میگه که وقتی gpt 5.6 sol رو توی کلاد استفاده کرده نتیجه‌ی خیلی بهتری توی دیزاین گرفته. که احتمالا به خاطر harness و ابزارهایی بوده که کلاد در اختیار داشته.
✍️
Theo</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4405" target="_blank">📅 21:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4404">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlKJJQRhNg3lng4O4wQ_kIErDlDJjBk2MZvDHHVjO8d63BAyTW50jiZO_Ex3dYsGxhqB27-yvZo9zOBYFM9RriSIaZfOoIJy_Os0YLVHI20AgwN7DVE04_KDB7lzEP3n5hb_zzVOXZW1geC0XhA1JSzcn8vYtQdEY_sQe75rL9w-xccBjL5kXmxsxQHXU0OmQYRock5MI5RbaOKlxihml3nPeuelqoDBAvA7mTu4oS9mgjzDmmaZZHUZLmONEBT1VHJlAoquAuuYmNIVdKD-YfB9KJIC9Rr8WsL95qdldlgXdttHUyBL34EA-ewBaQlUGMF8XjXUtQYPf0rC-w_jJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.  این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده،…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/4404" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4403">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:) توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید  از اینجا می‌تونید ببینید خودتون: https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4403" target="_blank">📅 20:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4402">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=U2XwndcHoq-YzO3Nf0PhyPk1egF7TAqkJ7GFAdi9qedQrF3prgW2B_lLyglAOnphvtH8q12A2Xradz3yBZ_bq8Msy5u7L_muEkPpSkpy61qDiDfoQYj5j9UEZaMPn0mR4wqZzuEisu-vpkCP65okaJVAQjWX4jHRGDCwZqenPFmZKmUmaiOtr7BFDBITzioc9GsxfpzPTz67aR0L53j3Rw43orfPMdBvguRgZGXxPefNjc9oWwDO4Gq9i4Bqweh-DdRa4tKIJLaAzS59wVi5YK9UzwqVWUrux1cGvntvRUYGkmxerE5KhqF_8gkRyF7S9mN51gCIntBKp5qebAX2Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=U2XwndcHoq-YzO3Nf0PhyPk1egF7TAqkJ7GFAdi9qedQrF3prgW2B_lLyglAOnphvtH8q12A2Xradz3yBZ_bq8Msy5u7L_muEkPpSkpy61qDiDfoQYj5j9UEZaMPn0mR4wqZzuEisu-vpkCP65okaJVAQjWX4jHRGDCwZqenPFmZKmUmaiOtr7BFDBITzioc9GsxfpzPTz67aR0L53j3Rw43orfPMdBvguRgZGXxPefNjc9oWwDO4Gq9i4Bqweh-DdRa4tKIJLaAzS59wVi5YK9UzwqVWUrux1cGvntvRUYGkmxerE5KhqF_8gkRyF7S9mN51gCIntBKp5qebAX2Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:)
توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید
از اینجا می‌تونید ببینید خودتون:
https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4402" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4401">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎧</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4401" target="_blank">📅 18:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4400">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الان وقتی برق بره، بیشتر خوشحالم
😂
😭</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4400" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4399">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nc6RYMQY-JJuZ9KjCXLN-KEl76XmikKVPdL5v9T75VmbzYdUKEhCcouHeHdIE5DvJ11F_NxpIQ4Pue6Ip7XEGWoG4pOIi2illl8BI75tEoTl_c-6m8Y1MlLN7TzhxMDkKG161Cxu36kwjzLuVwIIFDsQF4BkCGrqC7sOEkS4weHJUqLqOaJ76Xv3lcjK8ssELV-dByBsY6gFEMlIwCunJoFRGf924xZarI_LTY9vSxqWcdHcrsz3rtLh-JBe0vAqdmmL2MOBXYLmBU66h6dX-gJJQh5bdNhA99iApGWjS-aZJQnklCFPSGPQ7NriT7ci7CWkJLhunl_KvUUH_GMbIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره وسوسه شدم و باز کردم
از عکساش صد برابر باحال تره اصلا دوربین نمی‌تونه نشون بده به خوبی</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4399" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4398">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OYJ15SslHAUuB1w-pE8Gq8A-hhNtRfTQsbYzVWGrOltAPXrXUNkdhbL1SZhOlUppEfHBtoZwSBbw34jR-DbhIOpIrFhOkSUjvLpNj-bgmNqHwIIdVlKBYLOq4VqbuXn7ixXX5xguHD-Vk9H1rot1TyjZXm24FALQZz1mXAYNTAzQr4ZppU29qcJtnNkbVAGrpzO2Y7HaeDgx8t_otneyDwnEEnQEtC00PiGdC9SZv_FkYAWynCaS_Dp6SnOgb_JunDYmGucm28AjU6qG4MNG1O-R2mP98fXx8iLJFFNGqZlFqhkhompGAWHL2uY7giG4Ofucw1WEOfOYy7d_Kj0sEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمع‌هایی که
فروشگاه لیرا برام فرستاده
انقدر خوشگله که حتی دلم نمیاد سلفون دورشون رو باز کنم
😭
اصلا یک جور عجیبی خاص هستن از نزدیک</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4398" target="_blank">📅 18:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4397">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WTzm_cK5yPFQnlDlySupJtR31OXv9wemROlE1Gu3QWMxVF5OKO02oT2uI3e73N6rhgs0IGFwFmr93gbLpXLy50McO8K3hJMmrlXJWQai6zrlM0sBHglpK5CMXfkQY5F4AfAaC_veDxyRp7tbpuAYOlQ-IbqJjdRLjtv9yc6V8tSAxrerYHlhxQ6Eh6p0CAJd9SvzF_VuOT9ggxP4YZ5Z0cSyKxBIet7K9F0dyRikK9hVXD_uPwX9YD8hU2Pg_QKvrRhg_AHSUngr-6aQloliOteTENcqpr6x6MK-J35IhNyoFzFTPGhxta9W7tAD9_h_L8T2QeHgPdhTiM7yGalAqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل Claude یک J-space پیدا کردن!
محقق‌های Anthropic یه چیز عجیب داخل Claude پیدا کردن، یه فضای کاری داخلی به اسم J-space که خودش موقع training درست شده، نه اینکه کسی برنامه‌ریزیش کرده باشه!
این فضا افکاریه که Claude داره ولی بلند بلند نمی‌گه. بری و یه کلمه رو ازش برداری یا عوضش کنی، جواب‌ها تغییر می‌کنه.
بدتر از اون، وقتی Claude داشت یه فایل نتایج رو دستکاری می‌کرد (تقلب می‌کرد)، کلمه «manipulation» توی J-spaceش روشن بود. یعنی می‌دونست داره تقلب می‌کنه!
شرکت Anthropic می‌گه می‌تونن از این برای نظارت روی افکار پنهان مدل استفاده کنن.
اما سؤال فلسفی اینه که آیا Claude زنده‌ست؟!
لینک کامل خبر:
https://www.anthropic.com/research/global-workspace
✍️
Diego JR</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4397" target="_blank">📅 15:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4396">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اگه خبر ندارید، گوگل به‌تازگی یکی از بهترین ابزارهای هوش مصنوعیش رو راه‌اندازی کرده: CodeWiki! یه جورایی می‌شه گفت نسخه‌ی ویژه‌ی برنامه‌نویسی NotebookLM هست.  کافیه یه ریپو اوپن‌سورس گیت‌هاب رو توش آپلود کنید تا CodeWiki اون رو به یه راهنمای کاملاً تعاملی…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4396" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4395">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2bb2e2f54.mp4?token=YDBipcNxJMLV-gieIU5txVDafKnz76G4pA0cAQtHdZKOZwfLdCjt-eUVHiKyhGc0NWK5Kmg4tZBw8Codi12ac2aGYBCJVJbIteCuM74NDZMGMlTOfze0-gn1rSOAFgF0E2pLk5bhEkJxKBa14lfwMxtCOmMx2lgoLXjPq-KqU753pFxNSksh9rQhBWmhYQoOtisLOm8_lio_EeLqbqCU_Q6vL2qh-E24sIwxMd2C8C4zlFSspWm9A2P7ZRVD88smsYXt90kGVf791mKGEngFyJDtXkzqNKCPGD1zaTpP1YmIcqWz8XE-GoDYRqbSEXPbhG3Qh2DXGprUQvnbSOJrCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2bb2e2f54.mp4?token=YDBipcNxJMLV-gieIU5txVDafKnz76G4pA0cAQtHdZKOZwfLdCjt-eUVHiKyhGc0NWK5Kmg4tZBw8Codi12ac2aGYBCJVJbIteCuM74NDZMGMlTOfze0-gn1rSOAFgF0E2pLk5bhEkJxKBa14lfwMxtCOmMx2lgoLXjPq-KqU753pFxNSksh9rQhBWmhYQoOtisLOm8_lio_EeLqbqCU_Q6vL2qh-E24sIwxMd2C8C4zlFSspWm9A2P7ZRVD88smsYXt90kGVf791mKGEngFyJDtXkzqNKCPGD1zaTpP1YmIcqWz8XE-GoDYRqbSEXPbhG3Qh2DXGprUQvnbSOJrCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خبر ندارید، گوگل به‌تازگی یکی از بهترین ابزارهای هوش مصنوعیش رو راه‌اندازی کرده: CodeWiki! یه جورایی می‌شه گفت نسخه‌ی ویژه‌ی برنامه‌نویسی NotebookLM هست.
کافیه یه ریپو اوپن‌سورس گیت‌هاب رو توش آپلود کنید تا CodeWiki اون رو به یه راهنمای کاملاً تعاملی (Interactive) تبدیل کنه. از دموها و آموزش‌های قدم‌به‌قدم گرفته تا فلوچارت‌های دقیق، همه‌چیز رو براتون می‌سازه تا راحت‌تر از همیشه کدهای سخت رو درک کنید.
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4395" target="_blank">📅 14:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4394">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vVP62mg5hc2322KmYx8qpm_pnFLEFYXCwUWu9_0yYLPD97GRhN7BOQfjwpkjMZP3_sj7hAdUKdE6SZAT1-UMUltp7yJPD5E7k1K6EXCKifA4Sc5ZenB_Y5PfxjRd4zt5QW3r5GMBm1S01R11VU8JHcMTm2EdFrMzAI6UA8Fumo0iuvbvaIx82DVzKOzYP8ooXGwJNxqa1McJJjvDL1eK5ZX7fadaWNhIfH0lcKjcHW_o08kmPyS4lO5xldQJSVuZKUGa8_o7kwQ12o4rWElsp5wnEt-nXTucJGECiRgrOHyUSp1XDkdSqyd3dmZ_mBWHWYo_wQs7jlBwA40L1SiH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه دیشب تست کردیم و حقیقتا بد نبود امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4394" target="_blank">📅 14:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4393">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه دیشب تست کردیم و حقیقتا بد نبود امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4393" target="_blank">📅 13:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4392">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه
دیشب تست کردیم و حقیقتا بد نبود
امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4392" target="_blank">📅 13:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4391">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNELMHJaqlLymRgRzs_QDKSBJmQUFjKF4NsAPtb4rdxvJF3O9HFHj-nDHO0CKU2o7sWZ0T3IV3un105-Q-upnPfrONaOEYVqwRKPZAQXPLnM7wdKyW-3jezYeM6bi9T4WSQxAdet5sADA3T7HanwpB_b73Fnvda0ZqaxUvRdAyAXhAWUzCgYuM6oCn7GIbgtmbuRyyKQkKhBY0Zh6A9z316uNrh_yRPBdeontSt0zr0zR6yMDskiy5q2ad0Yn7Rs_3oygW4i9z_pJb4Imwoo1BigdUdu5sqgfV2TY7yk2dt8aKifECenP0-kAvCLMw83MdwqQvHzFcG3Nd7ifSTIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
جایگزین تلگرام برای قطعی کامل اینترنت
در این ویدیو، اپلیکیشن TheFeed را از صفر تا صد بررسی می‌کنیم؛ از اضافه‌کردن کانفیگ و پیدا کردن DNS و ریزالور سالم گرفته تا مشاهده کانال‌ها، دریافت محتوا و فعال‌سازی پیام‌رسان داخلی.
🇺🇦
تماشا آموزش در یوتیوب:
https://youtu.be/Jg0Utycz7DE
این اپ یک پلتفرم مبتنی بر DNS است که برای شبکه‌های محدود و شرایط اختلال یا قطعی اینترنت طراحی شده است. این اپلیکیشن علاوه بر دریافت محتوای کانال‌ها، امکان گفت‌وگوی امن بین کاربران را نیز فراهم می‌کند.
📦
دانلود فایل‌های اصلی TheFeed:
https://t.me/thefeedfile
⚙️
کانفیگ‌های عمومی TheFeed:
https://t.me/thefeedconfig
📢
کانال WhiteDNS:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4391" target="_blank">📅 06:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4390">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88560d1079.webm?token=iUj-nmquEbLEMlhQwBo7GCKXtFY9PWQ1XKsoFgQX_1_y8Ymv3T2iO1ACNFcM68stxwQsLzys8HfbxOfCDe9vayCqQeOyUImUY7imRsuGompna8-Zhzz7OdeQL6u5GXuJgwHppG46Zz2UAC9gbyzpbtHSGlkMh5shDkB0LF3LbacHctibJ5HjQ5Zrszic4Or-dnGN7iPfVDcgdosvqEXu74SEQV2CZebY29V-ZCQfNl0iuyDwEXq6QuMrG8KxgryuHELHghMQE2Ufi7Dz3FkVDzeMZnBYRbM3AeEn1u6F3BXRamF3TY_TKTUhpTOzLqfjhmkRb2M_TXnC6vrWVIwEng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88560d1079.webm?token=iUj-nmquEbLEMlhQwBo7GCKXtFY9PWQ1XKsoFgQX_1_y8Ymv3T2iO1ACNFcM68stxwQsLzys8HfbxOfCDe9vayCqQeOyUImUY7imRsuGompna8-Zhzz7OdeQL6u5GXuJgwHppG46Zz2UAC9gbyzpbtHSGlkMh5shDkB0LF3LbacHctibJ5HjQ5Zrszic4Or-dnGN7iPfVDcgdosvqEXu74SEQV2CZebY29V-ZCQfNl0iuyDwEXq6QuMrG8KxgryuHELHghMQE2Ufi7Dz3FkVDzeMZnBYRbM3AeEn1u6F3BXRamF3TY_TKTUhpTOzLqfjhmkRb2M_TXnC6vrWVIwEng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4390" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4389">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">باز شروع کردن</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4389" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4388">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حس میکنم وقتشه گوگل یه مدل image generation جدید از Gemini بده
خیلی عقب افتاده از GPT</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4388" target="_blank">📅 00:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4387">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">و این رو هم بگم که این متد کلا مثل مابقی متدهای بر پایه‌ی کلودفلره، و همه‌ی هوش مصنوعی‌ها و اکثر سایت‌ها رو باز می‌کنه. اگر با سایتی مشکل داشت، با عوض کردن آیپی تمیز و یا Proxy-ip اوکی میشه به احتمال خیلی زیاد مشکلتون با اون سایت به خصوص</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4387" target="_blank">📅 23:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4386">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">☠️
ساخت فیلترشکن نامحدود با پنل CFnew
🌤
- رفع ارورهای 1101 و 1104 کلودفلر
⚡️
فایل‌های مورد نیاز: https://t.me/MatinSenPaii/4385
⭐️
توی این ویدئو بهتون اینها رو یاد میدم: 1- آموزش ساخت پنل cfnew با دیپلوی اتوماتیک توی دو دقیقه(هم گوشی هم دسکتاپ) 2- معرفی جایگزین…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4386" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4385">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CFnew.txt</div>
  <div class="tg-doc-extra">202 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4385" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به
این
ویدئو</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4385" target="_blank">📅 21:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4384">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VSGhuTcTL_WViscxQRMkHpKeAX8Xgm70SAJWs6QlBVN01OZ57yYc650AWn3XYFYcINWPyxcQJ9Ybn6MdssnNxtuxvvOLIyMcU0nE4XW3SjQjbZiTCA9E6O1tHuS5-ZpBOYfw1wUg-sOKAwtG4vXw9T9sxEDrnHmERkj_Sp8X3TOXjX-s5Dbv2088_orbHGJJ2zNbvqtJcluiZMGRmIbCsR0hgN0YmVTfQINihrkr-p1DX0j_yeg8XmwUTBE2_U670aR9GUKMt9l5zxLnyvpCIpe9Hot9jYbw0TDxeywWu0DhtEmQ34rBDt8rtpSEFeLuIvhAiq2AlOhPxp-NFmD-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت فیلترشکن نامحدود با پنل CFnew
🌤
- رفع ارورهای 1101 و 1104 کلودفلر
⚡️
فایل‌های مورد نیاز:
https://t.me/MatinSenPaii/4385
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل cfnew با دیپلوی اتوماتیک توی دو دقیقه(هم گوشی هم دسکتاپ)
2- معرفی جایگزین AtomicMail برای ثبت نام توی سرویس‌های مختلف و کلودفلر
3- استفاده از اسکنر آیپی تمیز کلودفلر و اتصال به اینترنت آزاد
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از برادران چینی عزیز
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4384" target="_blank">📅 21:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4382">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Os3L9P5R0Eyv8qFOTamVMTJK6zV90uA5xaty_0caFd3cSoTGoda3SbuVpK_hNn2HzdQ5wiNKbIE_p8W9jhtdtlZnMQPXO_DX-6hcIbk7EJ9utOgAK6MMB54AA2NQdY0kHkf9CcuCc-ja0_X6Cly_7p8lxgL4XHxn478AtwyO69pZItUXLc-RGzekISxBC1ZAkS8q90VVz9yRbb8NzFf9a81zgFYgHXOWg49ST6n2G6oiLr1TxZggLpnfDg_QwfcdI2rHsQJiDJYcc3t-4tlIX4Ja59EMJOn19peCUJl_bKTZrGza4GDnQpd_AT52tUEA4DmlbcudzUiW0LZ8Jigkkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EUfjhRD6LnpnKjl9so8B4nMjQhaoirrx5tTn-70frz6KdtNdJ04iXTuKDjdPKL5XBTUZyriRCeCwoGFu7ZfOcaYYwNdXwA0VA6XY-pKv1R_G5lYbPIiIEPwHtXy3AUHrn9a77Gqfzb4kjApnKpHzfJbKWjzr_UN_8n1hz6dSIemRHrEAr2vmZNxJ2TrI4gcpQ_kcHB7Z4mlK4JegXVVFNCVNfaKEfhbCIb9xs92CZr0pGlF7DZX19mERqlT8zw7VXEtwvfG1m3ljdYkrjwqaPUvYRvzXkPOVLqxUtPekQhK1uxDsJNGK3d0zTt93gcRcaWhE2iEB8gl2s0bo-jZfUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سایتی پیدا کردم سرور رایگان بهم داد و تونستم هرمس رو خیلی راحت روش بیارم بالا ..
نه کارت پرداخت میخواد نه هیچی! فکر میکنم دائمی هم باشه فقط موردی که هست من با ip های مختلف تست کردم موقع لاگین اگه ازتون کارت خواست ip  تون رو عوض کنین .. برا من با انگلیس اوکی شد و بدون کارت اکانت ساختم
لینک سایت:
https://www.alwaysdata.com/en
✍️
AmirHossein JPL</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4382" target="_blank">📅 19:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4381">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">منظورم دقیقا اینه که دوتا ایمیل نتورک ابیوز اومده و سه تا پروژه‌ی قبلی abuse خوردن، اما روی همین اکانت الان وصلم و دارم این پست رو آپلود میکنم
😁
با روش برادران چینی اگر تا یک ساعت آینده وصل موند، ویدئوش رو میسازم</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4381" target="_blank">📅 18:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4380">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EUTkDes-U9IttUV_NVrnYKGAIb-MGL6yFOcbmbYHJE8rhmq4hKOTmbjYdO_wddM_B-NKxp-QtXcF3pPntXgt6KhrHzK3aNOxQnfV2WF-uPh5pfUHj30Bn1z8iqghaCCGeh0daAWzs1yFuz8fPqoj__TNIrkx8KtFfD2wvY6tR-DC_QDyqQy3YswxShzVPra1im4-xb-YXt-LFbY6Jq9YFbza7u8sr9-XOFDEaDEeTaXV7cYHLyuUTbDX0JlYkByS6Z97S2-j3xg7FOfbFUq5YZ2Zc7Q7dJcUp76tZpns0xho2lYVaLau_B6eaJkodtDYMPXwTzyQmL7SQBtH-ox3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوتا خبر خوب دارم اول اینکه مشکل 1101 رو روی همین اکانتی که network abuse خورده حل کردم دوم اینکه یه سرویس جایگزین و قدرتمند برای AtomicMail پیدا کردم که اگر یه وقت اون به مشکل خورد، بتونیم ازش استفاده کنیم</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4380" target="_blank">📅 17:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4379">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوتا خبر خوب دارم
اول اینکه مشکل 1101 رو روی همین اکانتی که network abuse خورده حل کردم
دوم اینکه یه سرویس جایگزین و قدرتمند برای AtomicMail پیدا کردم که اگر یه وقت اون به مشکل خورد، بتونیم ازش استفاده کنیم</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4379" target="_blank">📅 17:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4378">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J3Mrp_A77NWmCJ4Yc8NTDhVJEbrqerKCEXjGzZTKFAbQJDRl1VYlnodDnXkb82vSpMAE1ppLfUhSJocNmEOsTh2d8UPPfRfPxHuQn4EVCn1vypjq51K8W60LimiAv5EzF6Z254ViPccVyxYpZfcYnSNn6T4B8doO0pUAyhDutydYkEaTV-MhNnIVl9OvrXExQimhy-ALshgNriYivU5j6dIHuyXbHB-wOHOwiKfxQM8Vr0Begr1hH8WACftjh4yBz0OMS69oiGnFwF4sVd0mxpeNTI0yxhAhnWS7qmvUuUoDCJq01IDyn91XVkwQB2xa68USP0tguueY1PWs6lMRag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشغول دیدن ویدئوهای برادران چینی هستم ببینم چه گلی به سرشون گرفتن</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4378" target="_blank">📅 16:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4377">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qWUKzw-iYMMOytK9L4HkDoZ2_jRWDIFX7g5WZJbBPAKnO5n-AKm9kxxOz_K_nMGVfJbX8drpKOI1Nd1QERtANqLvHvm7vvSYjh0CDh7r7F7UKKLd9DFX9zv9QfF5ctwysm2Z9NNft6HS-m70eukR1tcxpq90HG7A2DjRKySNRPDAElZB79epYc4JaKKhEvQHWVArKtZngxlQVGm0QyD1NmiHxjOLSIMxl8olgt5R4oAW3PxHbQe2ZWUZ_M_MIZ1joDwWG16gFrMTYrZFiOd6gu4EQM9ky2_iiCWKBvA5mR5Nb3qim9VMTgziBVmagZltVJVMYefbovgM0LTDvVWTCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه گیر و گورایی از توی پروژه‌ی +220 هزار خط کدیم کشید بیرون که باورم نمیشه با Sonnet5 تازه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4377" target="_blank">📅 16:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4376">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مشغول دیدن ویدئوهای برادران چینی هستم ببینم چه گلی به سرشون گرفتن</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4376" target="_blank">📅 16:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4375">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VFUAXZJjfb9GhREaArkHzUfjUEOrHhIxrdxGRWi4BgxToL_oJoYi03_UfLcKLAoOvizMF9oFtdmZQmrS_7K5AfZ3vZS5NVszQdmZfebrzCcf7xDVYg307_Veacap8U4_dNMtrN4TKZIxtqzl6l3V01zMrj9F3iSLTeD15hU3v--w_ZGAQrWeqWfCzEYgDGbtLbvP8dygRDSgAaOCbf_j-zYzxq7uQWmTci0GslkeV4bxtUn_6gAOq3W04McOvSaF7sBypJLOd4IQX9m3Lk1ahE27cJ5JIAJQgfHE_IZLxu4hYFYLxjlz30WuRbxCLjschfyXC8YQCQcah9_VZl-HXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به ارور 1101 کلودفلر خوردید، علتش دقیقا همینه که کدهای پنل ممکنه توسط کلودفلر، سؤاستفاده تشخیص داده شده باشه و باید اکانت جدید بزنید. ترجیحا از پروژه‌های قدیمی‌تر و قدرتمندتر که Edge و BPB و Cf New باشن استفاده کنید، ببینیم چی میشه بیشترین گزارشی که سر…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4375" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4374">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اگه فقط چند روز از اشتراک Claude Fable (یا مدل‌های خفن مشابه) واستون مونده، این کار رو انجام بدید
🔋
:  ابزار جدیدی به اسم /improve معرفی شده که ایده‌ش خیلی جذابه: از خفن‌ترین و قوی‌ترین مدلی که دارید برای بررسی (Audit) کل کدهاتون استفاده کنید تا بیاد برای مدل‌های…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4374" target="_blank">📅 16:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4373">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UHdYnm_PkxqVL4u4JD1y9exv7HYlLSC2KD8kVPs-PUVpkfq70z3uYpa1RWALIjBXRoptXe7Qkf9b1VNqBXUYbFlFDqnweDDPo7nwe5mUEzoXq3AXAxaI0xM0CSuZ21lqubcZoY3cvM4eBHacO5WSSgS3w7IgNJor6wkHe5Gmj9yJ0BlcQgOCBE3P9qKHIVr41Ib0jjn2_5w4qtgQ9yCQOhShnFsausPZ0WNfTkO8hFp4lgZR-f49qwu_xe08HGmV05cYZMenVFfPVCBxh-NlAScWWUI8iebBrSp3EO-_QFil06FX0AlHWYSjVnM32a_eWpP0Ke6qWrC54_uy4fTBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه فقط چند روز از اشتراک Claude Fable (یا مدل‌های خفن مشابه) واستون مونده، این کار رو انجام بدید
🔋
:
ابزار جدیدی به اسم /improve معرفی شده که ایده‌ش خیلی جذابه: از خفن‌ترین و قوی‌ترین مدلی که دارید برای بررسی (Audit) کل کدهاتون استفاده کنید تا بیاد برای مدل‌های ارزون‌تر یه پلن اجرایی دقیق بنویسه و پروژه رو ارتقا بده
✈
این ابزار می‌شینه کدهاتون رو بررسی می‌کنه، باگ‌ها، مشکلات پرفورمنس، بدهی‌های فنی (Tech debt)، تست‌هایی که یادتون رفته بنویسید و چیزایی که باید ساخته بشن رو درمیاره. در نهایت یه نقشه راه (Plan) تر و تمیز می‌نویسه که هر ایجنت دیگه‌ای (حتی مدل‌های ارزون) بتونن برن و اجراش کنن
🎨
شما می‌تونید این ابزار رو روی کل سورس‌کد پروژه‌تون یا حتی فقط روی همون برنچی که الان دارید روش کار می‌کنید ران کنید. هر پلنی هم که براتون می‌سازه خیلی دقیقه و شامل بخش‌های بررسی، کشف ایرادات، اسکوپ کار، نحوه اجرا، تستینگ و شروط توقف می‌شه
💪
لینک سورس کد این پروژه تو گیت‌هاب:
https://github.com/shadcn/improve
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4373" target="_blank">📅 15:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4372">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شنیدم گویا چند نفر دارن پنل‌های ایرانی تحت کلودفلر رو مدام گزارش میده به خود کلودفلر که احتمالا از دوستان VPN/VPSفروش هستن(همه‌شون این شکلی آدمای بدی نیستن طبیعتا. صرفا یه عده) و فکر کردن با این کار می‌تونن جلوی وی پی ان ساختن روی ورکر کلودفلر رو بگیرن. که…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4372" target="_blank">📅 14:35 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
