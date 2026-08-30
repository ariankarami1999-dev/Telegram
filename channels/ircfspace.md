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
<img src="https://cdn1.telesco.pe/file/Aar7xfR95wAsrv8PBub1_uj0NuJ0I5y5WWLDNDvBJ0C13OPVPxO2Qe1cnivhNwDuiEQyAnVx9wxwVXtTIDU3CGi2-ZXJJks-N1BMZvW5LTyWTV5NP7beu4NMB23y0kG88ZEVy5Ra6OFsYE2Pi7RyMOgzEjvkPZTQnpGwQwmRx8H09jPH_Hbt1JCVVwOrqNrRwft8wiGilGnKUwzbRs5VZL3DpieONSRnQ-JMlHFReV9tbjD4NOvrT7EH84kfpaBf_UPbCHhqmSYB7b8jJWyfo4k8MD_yIoWmafi6j0efg7Lrd4jJhmiyQYmY_kjUZbvO9Rv0FEh7OuJ7OCOLMZ3iag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.5K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 00:47:45</div>
<hr>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C-bQPu98kMsrfVaAjg59UQtJHGGrOL792rD0ZMn5MW7QbJtmGkK4tAQfX0FDJh3VC4ZYpHQNLVNgycs6gy2vLPVQfl2DmtTFMxOsYz3-ao-BPMomOZ54kifzZp4JbSwzaSyabzCO6j4pFFJA40y7k064g45hKMIQ9E5AtRr_iuvGgImnAIiV3OuFZPxxN5F4sMjYY_lPxT78oyuqUUCwzwNN4bxprp421K8naJTxF6SzVYznOmO2iB4zO03_C9oMXQ1YbcvPLmu-Vd79NI0hwZoiYlZ6T0K6Vd_I7gVpmjc_MwL97-Nxo3nR_A1ToZ_qxRpL3pEgflOfUO5FVNcyzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dASWtibt9sH3jsKuZ5B98ZdPCLYcRgxhQrzyNXfbFD7UmOUGC66YyoX5y9pKRJ3fE6VdDRS_YUS5atYy6DVily8-DX427evh_CNqMB6Hv4s_VapJNXWFPDcM79CUszvkSQzsOufQ-leuYNrK5j4E32vHbELhBEAAtBySMhRHhxNJfv9dUDcoHreqtg27xWfOresVyxon7l0VJexzH0XlEN_dlI_1J_WpoUhk7pq8JSOpBC_iHbbgiN3Tp5drS3WLXmX5TkuZvhLE5M8gNHz7A-QJCMU2k2KhxTpABg-pLQQ6GK0oLLQyTeMlg0_MsCvNQIIKvT2U_XA_y9JO6DgsZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ezWTEAHS-je6qsEFEQpMRXseQPvXyL6iyFvhruYXAwXVl-rvaQmg0WaeFEtS9fIdMTYZOcKEdomVnw3DpOeo691ZKWr3ohBGdaHZ6KnCnRlQSBCJbaphuZMBr40HDkWJeslQFMbN18RirTwVh1w7KNhyCWsC4tTV1BnNAG60JQWSCywaFE0UGLZAnJvoZOcfKevsQ6JgeMVDSqLiJaSFDYIq2GRthYwwmqkgU7aNPo7cw8nVBPdhy4d8Igp97MQw02vsup2k6EECaRdRpj51z-rnN1PVTlNo5M46Ae_PsibKhIOJKI8khHicMvShTudf18QkqYhQEZ11Msabua37yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CuzVvmgaUm0eW8UmTTuP1xEtRxPJekzj13IbiBtX6l2EhNLYoJLDqAIhsxcxSL2Y3AIy22_-shroNuRzQuftssUrD6cyYI1A1ByZjv0g_uT3Wl3wPWqFGjuaaxpJpNRG25U05dJDC4DocAnyRB9LEEHh8UIhkGElttOrTRvgdk6Us_EzWzOPP_cU2qaBZVfdL2m1D4OqxBoRiigrqnNfsj-UvoKXol6suvORb0_kuu0p1iohpVQMjbovo5LNXcUy7kTYsxFMdjgb1MS9g8Z3_X5MdHcUeOcJI1Wr8Wy-pFt6bR3Wsq-6mA4xPMdnD3I8T3RMMkG8kp5I-1y7LkBe2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gCnNIfU1Zt0uwxNKLcmoliMisanF4mNJ4St3YOcijhI4doHJaVTjSM4uP4GIV95-a49MIr3JuJmmCRr7YffMZiU1ip1FRif3Berml8yWDfmpTXdE8F3FWE_S6CVBwF6dXYK40eSvkhUOrdcTiB00AtsHzpbCvtfnpjpA1-Lykudw19dwJpPxqD58YkOIvoB5bOsA5pu5qpTbOwb9UOQwfG5eTZPJTBEykRgHF0nz-97O7BK9xLoG6rEurSXJLSjTDK_I8mlVtgfLFHAUYc8jeAJ3JSfRw4Nxou5q4qbfEo5YT6TWU11qbHK3CIiyfepyAQbbHBjWaRbRP1eCvlWXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SydOUzQFnT91DARUYd7LA5iULf014MGkjZ1K4-UM-OCnvzgdNkmP23cUtJrxiPiu55aoKfuWXV5GS73zMfaqfGbU8vwNhVMT9hCxNMLW222tpo6uKWBhjT-6RYYGLTPCXxVWwSaJ8qf82-NUVCo--rA3p-Il6Ade4p6cBCcW-GnCUa-agtMh0oBzF6uplKgj59A-GfCCgQoTYnxtzedsO7xLpgmLas2-IEGMgS6ORftRFSd4BdSqZP3zfypm7Q3SGyvJKwwqGlGaLVewz1A9gztBJ0LrCtz9vC9_azB0YEI4GsmpWN924Ti_81lA3V7DX8LNgHRg_N3GOo_tr5v-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qgOkFJqFiR39Sw4MEXNn5tIlXzGpum0TUP2VCbm948TDWRedx867WI5-4UuWzdCE2SendRi1g8LMrC1kEgIr_cOS_fAIbZhp53WjukrHwtWCzQCwAk3iew4ihMXcS859s3ibgLJ5uHyyyZmwyusAeBvZ8WX1YB2ZFKhNl9dVfVlEgOVPIFvrnAD1PkXoD4bIcNHYA7AP_ZxYBLFaYbViBsrmrxAeXEzOT4mV-zBwlJy6UExtCfhTzgp9XjXqWFHTKUFSu2w7dz6EKZtxEO0zrKGekD6xf9-Xbt2n3Q1B_mfyGbhiF43-YBU778Yw2EW7sbDFl2KURM5oKJiI5So0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WxSKkVPZjFJ1ZAUHGZz0raOyIzTdhiqDNs8MCcN7rEchpCMZRB098Z9Rxz3lWG8IiqBTrXimQNOGFZ4ZBCmV-UKk3oJ4y7Ri91AEzVVWkOMDIa1Al7_N79jIC86qEvytC_bz5XoOj7h4ceLSw9kRSmS_W-8o5i2UVqrLVzMSDKxbzI5jKIF3LViz4q5odh2kHcpnEhdalffjrJ2iii__EbTs1B1rCo_rXwOwgbPDchedxVjNhOMAqB2V6glbj-6l5K3bt9wz_9hXeqA2IEtG1dtpWod87B0OuihLVdBVejMSpZZ9EMg_r-KRZb8io-cj_TGopcHuLQBjMdzvW7TiaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CV-1TI7hPYphqZceUKxPO-ofYSxM5f28_2fJGyCRTsOYKD829vslUsXqQUG28iCrsknEjFNVYAtJybmiYlvR_hoCD1vnbX2IN6h1uTPMJSSetC9EQ8DGZEsxHJyQfQV6d-nD85F-FaTyVRNRclXnOaL07-9Z-nc65QZvFmHYji_IQE_EYZ91kAByRyZ--C4QZ-THmmDVAn5yW8CUD30bBb_jERBmS226w4WIbyMzHh6fw-CmoCr9qKYkQf-xZU8LfbuNeVi-0kRSOSzWRAcwEihM8rH8BefzWxeB_zYl8CsM58gRM4hU6ZbwMXsU0zfCB9OCnQfe9M_Db_LxgC_2pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tn2mFsm7cJdO-aX8feewL4-fg--Gxo96g0W89cbCauPY3qqw76NchHP4hbMngxXa_PDt2B-duw69tV-hDHAKwehAa_641ix41-zz85xdtRbwRqwth91SRI-mzDZHMFwLA4noyrTevZ9xDJfxK0rwgEoFg7Eon2tI9KnUC1_fySr6ENzn7pH9g8sFVbQXAjST5oqK124Q1z8wKSYASVyfxahPUQe5hG-KUEewfS49K5X8wHJPaT89FjcL3B06BfyQsPJLLDo2tS3s99ZIl2zC9dUmZUTA4R_YM7t8L6Q93982PbuI0oKR7GVbwa3NqXlT0zC5YLNpKQEloYwFzPbimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LImmH0rw0r4xL8SWGRpsmo22ctY6eGUwZjVoHFY2--JQE8BMmyC2lqDDPSh0k5Dq1Y7WJbCnB2m0qAqqnc9CrrnHt1N1EefZRNdpnjr-Qo7f-VYY___m9nalALKyQI3JJetJq_3FSX0tLQN6E8JAZL8kmY3IrG6i4cKnircRfs1upTZH3PjMWU-VyJAy2vhJhTRMNdCH2lm60P_3VjlqC7D0YGDLYA6lgU42CgPT2ZhuB37JWpH0rQshlQAXkPy8QpbzAx8hOvlAj0HzsmLeJGhtsWnL8rNBBp9JYUMGdtwgB5tSGONtHj4NA4mgfIQV9V2qXH7rM03-T3O6RXqiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mOxUqAg0hfaUdFQA_hDAVFp_pTNAbphKMu4PN-AADfGyVpJyny8wiB0mwMy30Nsh84mSNGHPYcW243g8Q2nYXn4OCDSBynlsKVu4C2VXybXcDOLe1CMszr6now_ZziY7ozoqJyvrFLXtPS_lqMyfmBSrb6RVWnrnh_ZRHpUv37N_FlnxhYGwzru1T86ClzMX-yI5A0dqEOWkYjIeKuVQ43WaCSL6bC3U6mtw6QkI5jqbJf7Ag4th3Lmhv_HqCUtmzJnIi3HYALoukXvOamPTm64oMvoCFIF2sfRZhyUCh9-5RcCyhsHw1-DBs1KxxdQrQ0bCoZejZpUv-yE7gA6-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/giDv2AB6y20ZJCKX6q25hmqSYvrHxTmcJU1xZZ5bOyOSiRVDWPJ-noboM3YxiugIq83NVtR5fUGXw4wyVIJBpgsWj1lDLkEjodtfNcEqZmwzY_tms4wf0AX-PSNsZWjLQrBaJ1ZA8M6hfdMasDCCAsFDlJ0veWZtAu6dseopzAqYeIQU_zSRuKqidALmvg5jPUfRhHJbFiMeZSTmdm-htrBR7ATPwn6eQYclIo_ysIXAFvQ51tnj4307hV3ihRuXzsjGSoWFknSrPeHr_qCaHxGVEk8Njiwz9EFRApigd1U6Oqxe628m7UcjGqTKjNYaFgJisQ9C9VtFrWmalFepdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lKeNgjsqqHNmvS-MPK_cpHebUtqFliga3bhUZWb7obq7dvAYmBqhtT6vgGJLdxQbGkTRzTkjap8QGWWcgdjJEmiJhSaQGLRTXsuTsO4R_evTYEh2UB5I3j_82OHO0Mhqnmu0HhAX-dRPVKpw6TiK5fzmHLd-v4mMobh1R8E7blWM1WRAG6kfTrim_aOQuuzyXXw-bHVjGpwoMZyXT3_NNE8vzN8DHPO9SzFnZ4fjpbBf0vtwKjhAUudz3ixPj6PmVp14gNrPJg1rk65Ri9V1-zRn12TrKvUD3YKh66nvoGiWVb7NScQ3-UQfD_sCN1Uh1oKdKwVigK11oR0za7wMqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=t328xqxu-_vnC9ff6FE559t9-P2dXZE9PHz-3smQ41NGIo4545bmBIcGB-bFgIKLpe3hE5f9qiKWLhWx7g2sKttRaLagpp6K7_Uo1i6uYeRXlm9_hsJtbUQAVZVJOz943ezCnbHt76c0K1dwSwAn00hME31TYq9WmdwsOHoYc9U-S5hEIBjqtn36XIs1mM4MN-tW0AYYaJ-SBdnc7N1n3pbWMULkbxqge7ZeIg5ST68O42KN5YXBoBK9epzVFyuWxS4pLwMwxWqteqbZnHgkkD-gZQ211bFfSNWkMq1pgMPZ7-CVgXU8XzDKqkI9KCVoM_Pj-HgW8DShFXMREp05SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=t328xqxu-_vnC9ff6FE559t9-P2dXZE9PHz-3smQ41NGIo4545bmBIcGB-bFgIKLpe3hE5f9qiKWLhWx7g2sKttRaLagpp6K7_Uo1i6uYeRXlm9_hsJtbUQAVZVJOz943ezCnbHt76c0K1dwSwAn00hME31TYq9WmdwsOHoYc9U-S5hEIBjqtn36XIs1mM4MN-tW0AYYaJ-SBdnc7N1n3pbWMULkbxqge7ZeIg5ST68O42KN5YXBoBK9epzVFyuWxS4pLwMwxWqteqbZnHgkkD-gZQ211bFfSNWkMq1pgMPZ7-CVgXU8XzDKqkI9KCVoM_Pj-HgW8DShFXMREp05SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rGZzK__Jw6-ho-Abnc60KQxpPAyXkj7QbWPKxxfB_pUPtykGdRLwoDqKWR_Bq4SSjmlLaPxGyNQEWSbYT_trbfe98_YcPvz-62Og9S3hYO1X8OLIrO5TfGlBqdFy4G8_QcARE2FHqtLJtpq7w2GAfe3OnIm6DTjP0vXRQuobTdOwQoy5Xoaa5YVtOKvfAfxMXbU_JykoKx6SeIdmUrFC2vpR2CXJOUaq2PCNiMhPieR2cVP5Yz3lokWV6XADSqTOgORd9IemlSiI9exRbmjjuaNY6QjywOK2Y8b971oa9CznvJVHKzj9ZdJYUe5Xj9vAf5pY4m8obFVAYn_MENFgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z4E20KOrGjyf8-Jx9ZTw0FCRPtp_9TabNb83plvOAdNNPphWYRL8n93WmCh9P90_NPowQxbKZJaJ0rfWHibxXzWG3SdAKYoT2L8lClUPDgje3SzimlRXyZ_QXTuBAV7xy0ElpJwFTonWNE0K7eFfIkPdI_KT7G5tXcERplSxR0ksexjusjHXjV3DrAx9w7JA7Zqtt1c6aPwu5g2GSydAWcYRrg3D161eRqDPY5OazBgrCvQVWEgakUf4h3fgi5nwENH0aEmb3Ax2ocyUsU3ZF-ZK0_8es8dICbDMROAkYxzmdOvSQ3M7B93-raqjhTOmo8cy8HsD1to1Db3L7eK1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RZx427fXjRwjjsq3vpsq4YZl3-OB5Hu4UqXH44ugzqV_uZeuWHHtz2oZKII8wPqu38pj0y86AZQkA6U1U4ml-K1IiVGUyqjejyB7eGheHT7KXs-5Lrp-cCONmMMEVCVCX72Jq8A3uNriKRTTSrjtfsMCZpUXwHJ9zCKhwlC5qouoedcGKp_LePFfRKjIF5MtVymCDYr5OJcINpnAGOS-gdK5a3Sr9OeKIK_XfEy8V1VpRO3h9wdwrYW-i1ZHLt_1DNiCm9WIx6DHcjXZpxa9kLEw_N3nDmmK17YF2AZl8pFjm7QzLOxe--l7cxNy2i5oxgKzcQ6ffzGtxIlCcob3Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/og2HAuCngAaL1vTuD86Gus1KnhDJ32c1eak0CXYnqhoruMMw3kfXRCIjVoVn8B-sDuhZhGU0dQLW61aut-2H2XvOteXvFWtiVUO77ExsCZbmlMdn8nUUH71ykW6HkB8aBZQxo67qCt8WoUzGYWenEtOD18j3rlrkg33dVCS8GVatdpXUHYm-SLw8HQpHGtd1JQneXgIA7XVw1OI0ZMIWTCQvjHUvB2pWyQNwwRNMU84t4mPpr4xy0ouKGHLNGUpAP5rqycR4B3k3TSig2ZkU6e6AW0B4ECqALZVRxYr52XbjTaS3aZVXYhJyE5xko4CrpAlJqny1prXOZvlSt7ZgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mb_gg8pbBYh2yVPCUiaDYpA76KrLoWbcGrGLg8pvriuaC3J4x4myUixpLsUAfAJrD-hZ0GVwiAsTBsy9nQdieNkA0c8V3R_E0QrX1Pk9FwtGYGbf1coQHu1aFo2hmCgFhNTzKfhLh-ce20dt1RFK6IMhKgbD4BfPbQsnxA5xyGxCbclVtJzfzUZ9RaraLJD7a7Z9neA41XT4jyhTqDFva7u37ZCCmFtSsYnRs6BGZy11BNUJMJ06P8rt1Npcqmf84tzvec5227gGUmRtbOI94zhpoNDQbyC9O51XTLXFwxxBgT_4lDIlURWUbVb2GL8I_ewK9mxOmybNCui_e5SOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JzSeANmVLZDOrrhg5HNJ3RvYzuE0Lc482ZPItxs1IxzKPmgWUc8DASfEy2rct_F0iz25wteExQ5NuK9iknrQz_M3E9xjyUhbxEyF3JvtKgANvL8fgf-j4LkSupHo6L1SdHdhm9LP3gLpFjnxe2fpcENq8rB-5FWShkuLo9yd1HJ5MjUgb-fCI0Rr0y4sJWmqmUnBH99hb0bJjAVRxenWia3KjBKvKVgSXtGoESTNOUkv2l537iL921dxvqgd2RD0qoaxkSlWftwwbioMoEFIJXFi1bGyyJN1m55gphh8J-ZPAIMfr5r4kG20HUtDsmNvV8AxMJXhFTiRvEXsG_9Q8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dDsZOO3ZSz5wJujZTKWjhUGvsty5L7j5rwyLBr3Uu6vE83lLyT70iubkY7jzHkVViPaDn83S-1XlIOLifJc6BeQWs16YAfvts3Tsk8UAOjuGMcg5IXuGv6qK_MfgmIti7m-UNonvgokdZUMd0uIdEEtfAm-z8O-TMgiRM0PMzACqNPNFN5qs-c2GWTyA6eqsHd0J_UGmV47QAJnOvO-R4hkP_XzPZsxIfs42FAhsalq052zktgAlScdt3Hdm6qj03AKzNHMug4uy1PkVcB-azr_f9U9dPaDwlUuwztVs8CPYBJalJYyWWbSGg52xu_Txgh6-CORE7dpQD1HOX1WeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fKkWVzfHR2nfAd4Az6wcZRpnVqACfL2ap3Ht5z4FNO4-uaXbftiuuVzLSkWVTjKsT6CW5bbK7q0jcpfrfDcUPkCJR6YJRoQm6okVgzhIdFhxL52n2Db0AaIccQDasHhzaJz2or7ONCcimOjVraoudFwCQ_GlapDrJfsgyD-5cnep-0ZVXshHO62ylhBjcNF1JIb7H2j64vx0ALuhyba0mi_DKiS58QaIRIFyUJLRmXku2omUz7BKunQD1T1fUqR5o8xc1kBu3Ajk1wcENb5qEEwAZbA6o3SC8lpYWkhrDnc6Bc343zgfuqr-SuWWds4oPpFOCKO1gMibS0QwpVWUrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LGw5UFD7kWqkecn24whGqnK4AiBSmsNlQo0bzQqtXnLSSdRliMr3wA5P3RXV1lJydriygfunk2cu94A3LRr4405YqV6XfPxOfcO38TzclFaIZBLYIz6MSMT0f0OH7BhkwaUzi-fossx3GFQfvdRHUlAdvOOcuIO3kFRg5otbtVSlEgVe9BuYx_nLZ4rsSDPIaKEeFdrgaJVyyQKKfUro5rjdkuC3vIKVWuIl_bgF--kI3iFBrn2v2_U12vJZUX_yOuUm4tkfEqEat74LX4qpoPppj4fXwRYp8HdJ971EI3YlVpDoLM3dATNgooUfFNSdRv1ANYa31qdPwhnHFEKwqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GsF5hF6g5MwlkjV80KKM-myftGDegXQDawiWZA48z3gg-_GchF2D7T3p0CKZz7bbjRcKUX-iOCWLzxhCL00KDcrJS7Fll5PSIqzmWiE_VDkaDfeRkADqSvcg6bb2fgYnoKxuDbDej8SJUrqIfhdgSb-kaUVNtTUPnQwnQn_dzz5uDsiGjHWBoLd0pbt1B9UzMIqMp6kvw3UiGEAUxcGA1tvNEco2opMk97XL4r0JrnU8q51VitcUdhlmfuKyFFzupGXspV9qKDTbDgrJcOgYmisxWD9ndl6sSO5k0t_5SD_M164JYEEkNLz2wjfxz94dshaAY57u_HTtsmyfilUyDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TUj9kStgUBiLk_4IENAToxJjmso2nMxSuqFmSF9OWVC95Aw1U_XsEK51yAnODP8wuXCzd-TOxkRnOrzwepYQ8UDMLpj6gmj9j_mx8iU3VZRvWrh2jcs1ptJ4f3E3zuwyQyset_VDhcyDZ_zQfSHb-GHfb07nsV-j_TNIK5_r7dvP2lLitRYmmZWO-XJIq_ByFfTCLXpvjLfTRRB1UHhWzF8m6QdbBLcJ6N5CxUkN2Bli4AGKzyUC6AFog_7bRJSYyesq-8Skd4xK6671nSui4jLbsu3-V912diCuxVojg_5-Ys_r6nls40u5_Lw2Al-rPM5tvFXQh7eXbpwWBBHCKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G2zeQYuqyFw_BhpAb7kEFfVHmvR7DTYZPUwJcIhIK72PBcgY_bt2hIU3VPZKrno-sG4ac1U8UPpMrawozZrtwIXA3D4PUSChQRHUQOKFTmQKxxnSzHlL9-ub7nsVNbgLes5ISgotT3R373JzUiTuB0TgEIhbKG2fWgTH4FRAFtLOqvv_VfV89HhucOnLlm5r91ImW5nK5suz5KHKYZHgCsDvWf_07vrXASJPa8NRD04KnDg0_5SVWWZpCG0LtfYhJXPDTz5AdlCACogz6GtekvgMFVr_SIZWqerC8RFBUKVbVRANZjs__VDG3kI3Cd9xKtI-0S0FpNEvtHheB-Nc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fU8yngIjNjCXbQMSzlgVBPWHt3NoN_z61lstubMVtd29FeKS0j9bHS3xufbCZ8t_2tYZm1waVtqEct2EAX_xQzRhFvCKTkRC-KUmpjYp_azFDeK8mS9ZKSLMms3ud9fh3V0hVqD4qrDKrKaTNhTZ4VXHhd6igCXd3VH_n1UT1PxoOOTEaQbTfgHPcjRWv7tvb5nWN-9tnaeFkPQgd1UmrvmwUSlveRZiERtlLZzZGkWXDFsqw59iA3ABOHncG-AzhiwuboPhXd60BJRjzFgP0nzFKMpi4P3yYn5JY8RP4yUqsIISx4qeGQQIdt3K913f6ZXvbyIEr34rEsboGSkyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jgn6_MuNKYA_RY1G1yil0KEI0uPsw43H851EG5gUo76FxWfx2Gf4ZUaro5-XmcVBFqmpxNA7Lz0CgvX9YhZnvM7VOQPwGyj_aqKm4Gj5EKKAEYkh9G1m6ANyCn_IPNKhk4lxbuDiQPj6H0dRSfmVd_TLQT7Eo1itpSnwHFaVF0K-e4Lp7yJ03TWgYvkHJUCalbF6ArQ586kevbXTpYCIa4UDbpKAN6HWFHcWSirN1VZGHPd-4ubaRnJYfyPFXytZAckbC5J_F5SR_G9p1DaFMWilkpmtpWZVtsyKB8bb7Y7-_jj2tt25GKaIXCK9UCcJTEvmYDK2NelBLQKsOKrtqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PAHVcyU-5QOi8QW9iaDPWazF2YyuThX5IPd16PongA3wGnzC-FT3jhYoNpQbafNBZfCYlXsCjwnnTplQVM04wd-LVIBDhHe0dpc5ya-w6rq5BS1kGERhiNNocTWki_a2COP7gykZvKksudpWjd_aPnKrADYCjjPA_5FUyPf96WSwdOSO8CD91SW7D71zjAspHikVdUpWtlfiRoeZVy4ATDeeq6ehbFkAzVTkKNeEosefvSBlY5hcZGAH5m5PILAYzTVtCfNuLrbu0sVKwZDcc73ldAiqHc6wWfIlrSdl3ttMP5dOxR4ipndryp_9onFemAM9qQxHIFIdynE2WPyDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1eR_ZVW-7L3gVsiJNysbIYsz87gbdsBdfzNM7fqxhzzx68pp_QKIqi48azdThGAPnGnQeevD3R1yQHt8H2sQHGw7mBf8YiqtpUCpQqYKjjy9oURp5sEOtV4DYs6Y-SO9LFGnhGfwITCnO1jfmSk-GuqJdRsdT_or4k_xM3VdwMrloPaIR2dMdJXV5YFWyQHsITUnEqbbP89einI_nSUjCpQUbecXDFjk7aMmDZOvFKYN2agTWLuVi9FDfE5mBEjtFXDbuKm--TWnkqRWIumnXAmU1EfFs6cDW9SdBeVjxSrpE1xZCyZ2QwPe1iZyqKxhAHMvILSH1xobmAlytyTkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n_4cSv26H6qi_gM5Tc48KOMcHz4HYdHfmJpVP1RpBu3OzFDl2x3l_X6c47fjjndP3ro9cBHqL0x4ZZxeFu573ud-BvA24u1IZ_4FF7bdoxT387W-v0Q0Maw4RIYzDCLiewc3AxKEkHY4WUUNhWQ0iZNnLZXr_rlWvp3FYXVkYSJkQyVi4BbxbaZOJuwd3jcOWPGzRqmwgkEY9Fc3ZK60Wy1iYIjMm0ioPjSPOi2asy9IitFd8adY2MftTXOrNtnJg-jd4yIaHl2LjV0X6WzdZzEvOPKf-3Pt4Kgq5hFoOQA8vGws9DwirZ3IyF8hDcdat8xTwgrS8YqAmteovT_J5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d9rVMzzz-Yvvs_5_LmEE3BH7K_cLVKCxxjbja44uxSu4d0zl3pLdkaetiN5y7Oa68g0Iuv5PZlEpZhqZ4wsisgfrQIt4vWejSqAf3aCZ1oBeu4IT379KUzOb0sgJmLGoR5VZdN36ib802fLFPcqJLedCHhar8Tpep5J7rt3jDTwNNRTVOTBCstwxj3WQOKQsOR-DfagJPk2tl_5LstsmQYb5EPu6m4isfopVA9PFF4wM2_FIQb0KiIJzf_Xub0jUo_dniX2-HDkq0FD1gxbQIw7J4k9CvM1IPFDSWdLF5RNwj99XxcNJeo-4VsAJ-98YyP8_U6kOx2oiInvQFC9A6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kc7YZJUcn7iwWmXoaYNu0SG1YjW9CbcVRHjS0xC3mf7KkCYzsLG6ntCA0QW0QPgnZkw7x3M36TU6ljG6crIGVDfHAabw2okXvAWqa5knEutTZ1ZFljxgOAKCaG3bkwZALeAwyx5o1sfUYcoT-kK8LvjSS-J2in_Dz6Wu3ka5hdhyQMJGCZ4hGHQUUNJvES68shKpeCVH2u8ZFQihc505BbprVIltPXwtyEup-IyWY--FZsUYGxtmgQReot6H5I3iLkyLHY-5NOXvFplllM1fUwSYa-z-lfSY4IVZXdwkzuidOv-_tJUKTHLCzCMeyHFPBIerv3JuJ9pxJtUyKe1P5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WjPtOXBPW2fdKloz1O_nHyTMwoXg_sFniTPt-gLCTgoMR6y7jN4YtPaq3zVeDGp-cwLJtAt_lDMQ8GUMLi9vMw1KM5lGKnNPqYWiW2oeCGszcJ-i6_y-vcBFWp9j2cBL6Zqk1RHRkrI3nBw45sA8PlfCxIGY7HZI-JLfWmGQ0HMHnGoEuqoWuF5f2d18TrCi-K4wgkd3etQ3bvLmrHzSmx8FA2IGdJwC_XeoRIlox38BO_4y-UqeDueSZxudVnVPFDQg4rt-OAvNlvIrV8MRQqMCTEeRVWhZxOYdyQf6iOsaY56-bhReaw1Se1T1V86kKNfGJ96a9fcre2WSDXWrUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eW_eNzjLc5Ei4pdBVeCHyLeoOWhJZ8Y9LcQHmQLoepMigdilEi4IIrppYnhjfpjX5_X4w6QbEh6GjW_ax4IYocbIZUocJQDKRc7mn_lWu9mND-cRqytdsTJVcBzJrosu6sLl-rN3yukjCThlzQEDEZcVHP2MrumWkhq2dps_Tpl0_8vzC25rsmKqUZHYvjvN4aTx2YsoQfJIWz1xo48LHq9YMFUHkruThTAteuVLvIBPOT1GrAM912HTKxSSYhPYBbY5GcHk3-4AVf7NnGI7A-TkyLzN2QdkgpZQ0T3SA3WAMPEq2_6cz34GoHYsNoXC89yhoWA4GGn7hCVlqtb4zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t3tGdVJuEhopuN3QrOvaotrhErG9nY_Dd8-rXbPGM7c8gl97VWi0LCTUygY5iDb4pdNxOlC63gmpqSmio1dWkv_fEdB7S2R_9R2Zl_stQe1AZ4H_bSU4Q3b1ThsVfVdhBOrDIPmXh8bbRYy6jYBGXu4dDeea9cSbtMcZT65dacWHQaEyZczo_Gc41DmpsewWZnFvuczR83_vtt9ltqJTSofiNF8u2ZyyVv0lmUoc_RWAMxzExSfOYQuKGxkRG9569-D6HU3dT3SxJywF03Hp1w3Q0g01kins37c04wCNjkn5C99iQIOk5wXgW0IVRvj3ZprigQLPAgtQ9rCKvDMp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uGM1s3_IIczg5o8hZpll66RxaSxSX7FG8W3q7UTLZ2jC1nY_5DtVQPPtxrB09zAwHy9Zp5qiqXIM0PnEhi7ZfGPFo4gFIUT1Ch9-9NZrav_KjpjFTnRkZfFE11dHLD17D8By631UunaO0g-2851SMUkSsC7Hn_Fk_tulFpGpUQatbPK7HSDfwjGt4KZGI4gZK5JSvdmMT3IFypBb32lO5zP2P66cyh9qKI_w9Gii0CRuKYOFBdL3r0J_s1krdhRWmg7O9WhgK7yRHCIGZYDIxkOgdCwuZSx6E_i7109yGM1PJi_w_wHH7_8F3H3p9k-0Fa0apNgNGMQ3TX4Qx2UJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gg0NS9QB4jiNdKq3TSGL7Ihze3NNRhWaDhuF8TORW3ZB0jSosWL_NhNH3z9Ch6_O0AnvjitR9aORsOGt0rc88D6dqk7SCC0sSFAZGlfeaOQyq6tYR4JGCwDvDW8zYLMti4Wg9bQ-LwI_2HxwZikH69H6ihgjdwex6Jc--6yQlibbQwwy123enRPair4Qwy-EXsKuhTwduRFzfIcbIMfllAFn5tv5t79HUuiVFoApqCGqxTP_Y5gOIbDFAdXNz9elsReCQlwIuDzTXbtnlYQWsBC97LZ9odZLyn2-FAeil-3Vkth1b2T0i6mpgZDJQ4tJGO-7VNDr9B71nHAZ5UeXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mt0b4aNbKdIPUmEQd_dH03RjTSG03DZaFncsn5Y9PZT-W8daQrA_jkOtn70Sb4EBV9L9WH7PGVW8BboOdy5pI_PNt9aMtH6jtP4OaFLyJUzeB-jpiyMl56WzJgxbRPfk50VeOoqf7NrqKyEuYaP7Hc7j4C1vHUqTlQf2D1t25dVVj26zBq_Z_0iwvBHf6IDuAn5vLvtWdSUgD4qO7VnbfOYP0Gt-wZ58-yi_axcs-F_dQDtRp-dyQXiwjJgMZrZyNcQ8k5_oqMAh_YfCltTFCYUPPNfBDbzXbW-xkZvS5xJsVpYC-BkFAj5CbfXLOBZrRX-cavG0BYcdWO4MQaxx1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V0FCDfK3LSCxKsAstiQKzOghGerandC4RR9Xh-zLBOk42TGKnKhu_BtCH_efQIpyL0vp5ukKvhKIdK7PoFVUv921e1FR3rBvZBaW9Cu1nbmQkjFCn8Pg3vs_0YhBIVGMkBdh1jn_rv5vD-6LaoKjase-DFzgq5xXjI-OPUZyiM_omSb4cPUNTTvliccC1BqZd7Nvef76I8famfRbsMfH7B52sT_yfHPYMvY2EAFfV0r5mlxRZv-I2zx0DMQqzYDeGw2gvekEGpmDPTasB0V0BYrHyTjevL772KWaMtYAKswZz0VyZMD_cLlbNkZQkE6BqEVE28MEscJ9R754c6APpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FC2A_mL5JHQRx-3M0V3CCT_JMyKUSzqInAARxn2xW5669y3zzTOvGZUE2_Y4F1eGfuAfvJBplCZUdizARvGt6TK0mJC1ThrDwWl3wIfrrLvgS6NWr-pRiQfWfDtGJUZbNESV8EiGhzmhmk7wYwxIczs4Ui662JF8TNQ5vqujRC_CwAblx0wq1sZ2b8VXAm0_0Jx5lIEtRNIYRXOK0A9nLIGdoTXODo96eJLO5ljL4rMtNh0PHT_a1MvJb0-dYdjDWfBUV3SZGk7X6ggRktKS3xTbb3syzQA8QznmN42xRwHJmqzbCHSRYfcSjXl4I-fsfBQE6o2b98ZOy0_0Xa0kGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OMbj30oKjx6GgHCYy3UzhowRmL4oxsw2sIaYHSlPm1APvXcWvww5dU9fc_IkjdEi9dhPUYaCRbyGX1_2Ly0btk_CoWLZhaeg0nCMq8MEWqUh9pUggJF0a4XOHwbNcX_mJmxln0Wvo0rIlf-B2ht2X07yTmAi2JCBKM4TMEMvWbUoNlqLAgwajnpzq8Y5r7wAg4wJZC_73MGe1WXIMlPqJJnOTn2mJLSouJEdGa5BqAbql2WDIAI_ELXEQ3G7hUjK2CTDywVD51PD7pGCM6Zy1U8ddJB3VfX45-bjngs22pF-C8S6bN5OFDKVzve8b1oEdwyAlut9XEEVa767qYQJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UX0vHC3ykt0_yJXKc5aQQzvVqdvx_IX4LkJYmry9iKTgk0DNMwoeLXDKSlXWFSOg0UL7t6vZ4hZJmBqgEJESGKyVk9ouXCaDLIZPM1VJ85uE6v3HGGkJ75SZVheD0CReUTQo4WHd4UoB4p3HoHXTJTxM3fkgRX59NdbKNenhlkHoyYBfhPBU0xGoYiVaZJvwPczprExTqt192UAOrGoIOUWD7_T_aFjV9jXCjsRnbqmAm9QoegIk1k54fDcm3Uy0Mf69bzzcTt3VrnyJQ67s4V8cK5Pl-N9YZd52u6rStL-JnXONraUz-mdNbgU1z2UfDQj91HVstOfBDv7jf_GSAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N_GUYiIwB_KNfnT0PQxsOaZWnpyOIk40nMobf9DEWmAMGOAND2ZBqt2tJhSSOQuz-9ibQFrYtGfzxvoaSbjTEujd_pgqV9_4ei8P2NT2b9jpalFykkliIRounX5STr4zhntvjUi2_wP4DfxBZat-SVhI7kvpjGhwCQvpPGgYOVFDTPtUlLJ7CaM943buc9Eszhk907awfcaHEgvQzGtBtrfv_3gc8zRwTF8fLZWFrZIAyMqtL9QGrHRXjUVL-JghTQza6KeIai37CBx88tRKZim9ijSHH4fK9DNKyLlRr6DIo7o-ed_jCcXdG0p35JLQt2srBLhdWgSS_UKLU0Fchw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZeagOwZaBjkrRLuItEQEvqSlQUPqvCS5QK3D3tmffVNgqHksIOMMbehBTm52P9gRZ985l7-GGfMqPGOEaNc2lH-g8Iw3bj3BDXHmgFeOtLdIajWieBdf91DENAepe5E06mZbTlpRJ6KaW4eNBvoIAW8Pso79mWP1nZwCFxriXeLsOQdNojb7XdBwvvmsX6plKuIv9KzuwHCPaaqpGm2c6TT-7I6Bk0_-YEHYfwkedTnLxA4sALLLhhIAptkivz4EmAXCJjLHwRH63i64L3gfwTYaWQqRdTMtcix5SuqPVkVzQa3xhuG62EsdnK-ozv1S87952wxesXrQAyjbWhFrVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ph1yFdsEiKG59Icv7huP6LuZcHhWnHBhaBL-GImSw7KHUQS5AoV7b3EyG_1SopyShni6yMog5e5ooqEnOtbk0u0C_z-nHv4-VNZKX1Oql-v7SsarS1kdM2rsVnn2XtYPNhFDJ1F0wpTV3mZhUAiMdurrAmPAzWM53B7g4SlqOH8Ijj30pMMBdQT3J7sYuifanTO4EfkKQqyLth9bAM8hpoZDLa1X3d_GVp1jNBFM7NhIvGHRRrJ9tMORH9ERicP6Zc-37NpPWzm3obUXJrfAYuaYDqD-oORcVIMsIc-ofD0GR8WdOGfMj-VCjsM-l50EGACP_PJp7ce-dR_JMLPwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fHgGNe8kX3aO0QTJ8CuafNQTen0p5Z4HBwRz1y3YGsl7c7TBIV9RgneObQsIDcrHrQX2mJ-9yAMnCaEsUrc6ZlaTH67ElCeIiA4rnkrB9vKeeVzCmCU1vvfisX-VqY9Sgz8lRu2FRDm83A4qGWWQKhZVOQlOEPtG8_DYxrTRI2yqMXEklYEJ0t9a5bRCWRmbPu24J2tHqttt8y2oLZa5sJIswErvZShJ8vhzPsFvrTYcJf83NCiRZXmvDqbpwJgpfr3Oef4Q_YY7mHYdjAqwBFVPsucYGRngFV1pTveGCGwUy05wmTlB26AXR3FgVTYupyfwxFjzd7zB6kwRN5bcSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lOBqzqReXEFiUX_erXui9dY6w5R-0jxRv3fcIaqOaivQDD2kVT9BlvPy0AJ1S6AR_XcGFroystaKqnsMVcbuueUwQ9GbA_PcR464ao4XlmUYHqm6L9-WZWcuYBSD30q0egNyomgb4xQBlYyGUjebr__XaSvnZpTl9_hD5nT6zVFzsarYl5-g9-rr6tEXRg7kC3N7b_0Fx1Fg-zL8pwc0XBvC-4DAo5s4e8kSLICmPdsbBLYe_RciI5bQsWid7qL3NaCI-bkgXr3SzrwifFCx-wjLs9PiW-3O-038DOlqy8ZAKx2bM7QKXjv-DnvtGF3l_HFqp9pcfxgqcHNnzP7cOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GroG9bkqy9XLcMXexhZfizRjw6aoUP7lxoDqjqfOGcpAmgRgCJYLV39-NWr62ubswZ2pRTHdqL7JMcRJhvKlVrb2s8Odu_aXDPc2Re9sH4B1V3f3V15l3GNuINM9a5bFgUkoDeHzmeoOfQyrNhggz1LC6r3ECf3BZWlno9WzKYIY2sA9DFEwI-TDRDLzgLwboa7Tt4DWBNrbdcMUelEYOjO0Mb_UmaPyofXQSc78aLL4xvZsbjiTa2HcctCJ8d3qbbkAzE7lkFGBnKpHyemRo-Ppd4s-Mcelfm4yzexGZkWGBxOtN_7IXnmHYS4s2yuXCTgVQM0o7axR9KLTXu2FPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f3N2HAvxshQYk2f2LjlqA38G7R554yIl3XPWzcwgJ8jKtqACINk_QaNBG7RnqXrieQGZH8SqMKbEfi6CdTUpTDmvehbWq3Lp-eZc41v5UQrw84aFXd1_uUAyXqSYzdQavLFJ22iTQZfdGQTBOL1jY3edWsbxZ257FJQHTDtWP8kfCYMdPg2YKawFvpYLTfVaH94fPGQDSvWb6WxSFXPuQi-M21iqbnp7x2wR6R7Cp1vVDv6teJjn7JHFOuYO0Beq4MgCYI2h9lCPjsjQysGxX95VxuIlX7IJvcnzgy0DXWqBjpEqfE4o5TJyUdMbD2klBt7b0o4ecW0jpur-znDEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jJ4J_BrIWavN0NOevZCD2xDOozEghAvLX6jSXHsF4ku3AP1Px35HmvoWY7T-maGcIjem_wHeIlvXksKZT4MdEiSPBoeAQsIGmOxj0w_Z83gu-IpcBG32QCAdELt2RXnqeQlLyFaT0OT1hVwKHLDhdfdJyvCl5ptl1kIWrNlE0h28t4WvpCAt5bB0iraKqq7Fiy-64_0nM0gNdyN04TaJpje8JVCfnSEhM2NwxW7qnQS7Zz8GXAb-DBo_B1ne5jX7jxeDJevpprYqtwgh7N-GVODlBpY_c-Ff1NiISe5KlyMyUBuwZvjOoY7cR22iEpHmxKuJAwMAy4FcVRxqrPpSXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eo48AIF1Rz8Q5M4TGSDfSgEtShEeDnO69AlYiLdeywYqlbK1xjKsMIYZVNw0KW9adA084bWK9FrrBTqkVH79AOmesEQRtzbuFMr4tlPP-F33_8PZ5C7490rGZvVIXzgRdpqg7SjP01pbxn8z1tzascj14PYdv5oqXbb6ExhHjLooaYx-wK6UJi6rq6_OKR5RFWaBI4vhO4wkUSHIIbGdn2DUYY2zq8liv5fB48yavnfyV7ao_rhGn2ESAkmKiWbulylHCcxvUO4n5Bp2nuV4Om0BOdc89w2SA6UpPD3knRRRRtJGVC2ejix6ryBptLPIxLKmYV86RSX2reX0Zjhutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HsvGTcqV5FCksU4QDuaHtw8DFOhEAtOOE9K43t6ovXHqmw-rEfOeL4eXcT7SOGWsQmG6eBMIV6yB3hDEAZpBJWQqiX9FtOBxf_N09KyqX5w_r8V2xL_peCuysgEYxXBpLETxOsGzjz-O3bFc3i95gKmI_dbOS8N-0hhopSfiRd1Mu4BB3WCK_JKc8yNs2-RSQbx6bTVfZqgxC8DWSaTtNuo6Sw1hGdrVLch_5joW8zXrnKZWW2TYSUGlNjoNkbCyZkIq9vqKxL0b0SDyG45xzCUW_3Sagy_7-JpRhSfnCGP1OSYdfmWIm9k-tMr0b2_KbMtOknVkrehWNhlzkwR5mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c5ULzfqWj6EmWvSoe_MCKXUMCMVeVjMeU90aB7LBee-InjdDXDEKGwvLkYJQ2J7RbuHdw9xc42uYI3cGerse2zwyOA38IRYeVK4ld06tjHVl2RohSX4fQvkNzOPNgIsKQh5zpGPv6p7rq4qcYfzDOtrKDxqEOsBHDlqYFXJAS0qak1lBLzWnBKzHtu59Za3Ci8o7ZN0HbfakZEuSC8JcGI1y6YAxdZ2mAurUsgsbBhFx-WKb4gHnfDYptHA2b4Q6TW5A4E7m8U8_xw2O9TnYGAVSGkfFgwnllBcYEYwxqhfQjVeDCscx08YDvADOKGe3-kD4jfBNYEHNxlPakvUm5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kippkm-SdL3paM22EJx16j1XgMRFrtrHrl0MdtzrgsjuxFrVHgY7rleRv3aGk1gQOGa0d3Jyi6LdZt09jz7uXy7wlbPa5PSi7cRNinflBwiwnlA0SWSsl087UbjJqW7FwtSQb-42ZFmG5UbLYWvaOsfxrT7FyUeI-85bvspUWQFTgLWgYVBoEyB0sjtWEhDLsNc1PIry23mGzmpTkskb1dRiS7TgU1Brip8D9b8Fff8vuoGyhbnzZZdyF7FyCOXyUP-EVIjwQ1MpqFaxnvtl4r4SCkbeLJyzScXrjC3aWBppayse2ko3PHnndT7WuYXCd7ma7sk1Dj7k-BoNKK5NLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mRZpMJaWryYA1ssGROBaHZ8L2iT68OBbKMMga5GNcRtFO4C2P1b35RpJKv-kUtsT9UYSP-ZRh_x2qbT-WXq4nnw-GqJISjmScAfT7qSLiVhDXWv2SXqRQ_AjjtF3m0G_0Pv4XP2rEecLVIDZKyTpfDIsmDVKnFjeaaMe3DAZlaxGdS8mRFPTOuyhCTKLjQaMCKZe6HcjMmL53sbtrMHRUviEVc1fgRz80yUklFKiCTM3j4OkXXLGaLrJf0RlblrFFmgWzEGbmrvD_a1TcrqAyLGwOyk4wHAbQ3xkQ-Sex65GiPdg83Fwzm4X-9TJp4XI_Q5Q4f2A-ZB4zJs9w9tO_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sv3pBXK50qwvT1LbkLJVT6Sa6dy6zrHdAIsdrMQ_VIH8TRoCwIuB9JONCgapo3i0joTzjvAjQlhfykJcqYW-kagZhQcyiGo9aehYI15xHJcjQOIxfljbvPgzHicHt4RwB3W2BczF5zOmcPFoEN8RxtQVpuv42ZhSc4NJdVJ2UOO_l5Nr5vYnRPq0StzhEt32tqHjlfP3CioWNuSs-wtUqrtzQ8LmHTWeLH4NWN6T-dBg6wLQe30WwbvR64lUWaE08Vsf5Ol7BT41C9auunRqwJXBaknYUWaDRoO4CwKRQl8apX6HgfFGMt96iFGTH9BW5thYdfTf7DNmRFvhNsiBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oLxVhCs5tQfE5U1I0it1zEfCId-yYURzKgbSZERU_sWCt7_dVRMd1ZOpsMiY3YEchO7eQyyf8Bn6bseu1ZzD3_hpifEubAsZ7X7RTeeBGBzbQlOr0uFGdywGvbalW4cSvG4Uf5GN3J-S-sTUjl5S375sgtgupGJJeyNTkLZ15RuznevzPU3aQkd6WWOZL0-PLaly_1C_g1wyVRvfhuGiFBdqI-CdsgdTGoj_KAxezzEKM5wmKO7slJdnDq5tDvXgnjgdlJziBQLqMqhDQrYoP-tGzFPr7hwN87opxgZReRTuWqKN9sbkliZshbhiFe-1SQsiQ6fOHMzYD5QdqBafQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mqNwSHLlexISw_LvRGxIfKLiDplAsLrH-cenIsSB3C4VhUKx-vWtEIUVZB5_lv9YEtiifuTRc3RWp7ZpFWR4CjDWrK8eOU62Ff1H12sF_1Ng5hWh39yhgmHSUN7gXo4FfOZ9DC6Nuut8TkMor5rm-JEs-qHVLJlUpGzp4JMqchr0pqn4Z00EfuhUshSJARnYyC1TvVbPpF3KtUHqjLTbVrdMbh1RyDYukQC9yaL8Q-fMTCet8KU--fmRLaGzId8pUXsd6gZx4nlMx0uxwLwDF6kR0GIPRsTTMnto11s3HFwg9nzRqAnxDiaaH0JzPRGPGYz2W-8ZIylJ4wjFfhnHLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E1w9p2yQ1sroCgAJYilO5ObM0T8-9XC8lehySnkjr9ZDzdJCTwZYkTsD1VvsCHcqN2yDZYMIem5_k__1cM3I0z2pQt8W0jsVT_-Gkmm4aOpNVYtFsFDXEm7EVaod_Dn_O5GocLWx3j_mt8aPWzULR4j1WDEZ5tMNhQmNftoXgLS4-ktbAjWWE09m74f1VQZo4ekosp9pG3m4auWOVSImFEXZS3MgXJYIrBpVNUyI5dEaFVaZGKKQP4URfBUWAdewUcQ7j59RV5NInANjEoiruDt4aLntxoEUCY8IjA_7dnOAraI1CwilpPeAEkRzcSJPGY9T72Rf3nJ6iOLwFYXZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SfogHnkzi5m8b5hJSZPzT20wU1xU9c3vYMKDh6lXHi_f0mnsDD2W3jboYPgi3qJtAqSblAGeUhvi1AxD6_fnQbjo48l1yQGlDn2nVZa-g6iiGROSraZGR2kRwiWZ6-RGqR-iTH_J6Y6Qg47wWVo0rnSgQNQ0Vt9iM8ZDfOVED8r-6gQnQ31WXkd8O-61w0aKlV_6GSfOvJahoI1KhGeSesJSwDB0x1Q-9x_JtDvJTma27VsoqffIFEWBEau2Gpl4JGlk5a0GR9Hv6mXCHdMB2PIiu6hzoghjzL6FJkC_jNbUcfzPcb-SfnBaZbpGvTUQx2fDw7i-kl-V0JxErJfxFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IUDLGk_HQ9Hcyw9NJGXFek-jKrcAv82ShMfr5oi2FfDLe5oYKvxyXN2gU7XZLjbmTMAeJYXM8Z5QcPeMOtH3AndME4k-Ip_qpogvXemuKvVCfkVEJ0fRV5xrwKpcgn26Hl6knlrKJz8hzcBVt4qxMYe730PCjYwtb3WoQTQmCdVbb2d604PeMw7LkYWHYGe2IdJoLzcjfJed85zxdsu2JFd8XEk8AZ2nDLLRjgEI3mJG8wga1k2h9Rxob7VRyH79uBurXOAPx75UFch3SK13rAjqQ1eSqGAq1cAd-JVt6-c0PmJpKJvyVGIwtdRZkIyrVhPrmGgKJTB9LTrFxv5wPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fdQlRh6J3-StF-eNGamGswBq-MpeltGCNnCibTb6JFvpw-Wpxcj-WzFHhjhDq8esDpUsAP8zaPU5lpvMjlTMA0rQXzM8izmtjxwjeFXhhLSGsZkB4cKTszT9QW2u__fl1xZJ64X3R5W4zca3IqMFqeCGV8wTZdW9dYKQdnhV0VqruHwEwjxby1TcE7cUykRO-6wR1fEWoC_b-pCT3qlA1LBldsqOYJZvyRMbOfy3rqhR9-g8v3sDMgQ1MTi8VI_u8BcovCO2h2QBDm6UYHXzwvYzyzOTQN_beKkW_VrpuC6gy22z1fJvVcK6Xjgcg9zbNeNOrmxKSq0YQ-7KLBcwhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jBr3nzaqkB2i0HjIUpaxW0zeivr6br5t-Md6n2fHU9ioMdARmRQXmau11EL2jS9-e7-GBKV64HnVIV12kiDXJqs3LoJUCAmsW4fnLoNMjr783_lqeQiEYn7YCQPnYpfhTmqnYDGBmMr8wX84fyC36XK7b9WLwahJWwM98y17J8N79RVov1PBUpq0Lc-exTIDt3F-1ge_lxdLiBZg7X9Qo5skPHudnaPXedOYbTMSNfKMITp7PKabPQxQT6XVsaCjJ_6-0PowNyPRkBTnkMFKMQl7O5vY3Wk7WL52ydJ9-6ZZtoD-rvgpGPNleG241S4zAAIxAg_Wj1xCFIHaVnt5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IPhXzqgrask74pRwBAMXnoNX7nP1f6WNZ4C-3KZ-feWfWeapJAHWSZFE3MlbpD9Km_L4R4z8AZa4hGiSPbToDyYquHXsqFgEezHYLlW9pC5grQB7qiXPkLvgfphrdAaq6VBunUGMYhhgg3dH5JMjw3dlbbgnQSFuXLMtczpyx5dqAbAFoPQ5X8NsoBe63ZnYtDdCYBt0WWoYaaUdlxjJ91MkwzjA34juXTDWIOkCtNGCYIzvp2t-RSpeDSA-bGiE_81X3ArRI5RaDuiGGli3ElYqT5QLPRTIjEyvyLc0BKdyylSti-CavTF0ed-Eyn_8vZXGlIuXzxS3PKEoimdciw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K0ggerrJkKhEJtMxj90nlWRw7VVYVLXHroSZb19TJ5lt0SOuSZj2dAZYXor_w4oUrK6bFtBmhZaKBZA-vFLPM9kZKdFNlyb8fIQv1V5N4AvhCOdRw3YXlv7VsiVZYN_-ab-zLoILKeUGPlnsl75IzUp-obh5wGIkeanDVSRPzqCAJtf8djRbcmtzWljdHqrXFydqIAjNO44CNWC-WPq5OP1tErdzycs61KgIzh6HOh4UZ2S0GHX_RfXlr4HTzQUz1zjtTtsUkpVnHX85fZkQy5lUyx6rJRdmuRrHN1dR2T3r57WCkepPoeTAy6IIVxmV4UQKlhAlxeX2E_Pm09GXXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O16a58OY8BMkUcOBE7GrpEo2gftKCt52taWy8GVUFPEYJZadfy8TW_vcUk57N4dQuxowYmhoD0StYCEZAHNCfTeVNz4Yt6LI2Qm9ZIE_m64G-eugGPzdwxush70stM4uxYlEd-S0472SV0tJf5cU3TgkhRSs8LnGZYd_IdpcSDDECk-sqOCnokoo_HS6fW15ZawT0-dB416qtd3jcHGvbDcPU4koHkJWSlK4amyH8O0iOpJEiEm4dKqaex5ip1g1wvv8AiQPpIML9XE4ExSNeSCUKT4DLW8wbtuy6cp7eKNbj4GxzAx6exIgBHvtqcU-TPtk-7FoL97W6Jfy-8WdTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZPXmZaXLKX7c-UDiwQsRdrG5nFWMjTfM_tjlQGH2vUsqoBql2Ugzy36vCKuS6EhvphJN3flw36OB3OeXeaDz-vVgjYnJiXxmiFi_nV7kVbOY4EExtyWc49IFrlA-yu769XIwwwlh0pMndXSLknEXwx0BjeEakNUmes1-oWmmzKMpi1_5DGbM1GWucWmW-p7qTq_IymZgVARICTOMyarNEEV1_LAv_k1QxL07ZgjXNgNaKlwxgpWyrw2qrOlPLs6YqNq0nXaWx0f8aQh6oEBq0GwAwIfCIud-GnvhwWoRCZB5vLSKejVGSp8rezPUUkWAFaJp_rlswMix67Hy2kk5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VECH9BicMPfWIHrq4K6QpVxLjAHWg8AVmaGjLp8-e4UgT7EHWhPxhrPCLLjfANgN_yFJU63J2pm2PPqtnLNXCFIXKKd7-7x7PXIc9RvxKKY9Kr1ln6gT0nGRysTCybJk3PGM5FmYf3vqKAhYJn8J1_yyA-7zB_PZlKyLICK6y3UJZ2qE4xDtamEgT4DqV5qQTocMOmf-9bLasPOVxfVZQ3ykMd8FjPn6Eo1vIfG564nbLuqwSxiFYxuMr_1KseEmqT3Rr-EvmLei1X4Dy8PCf50_3Gwgb1fOJhSdgvG8OjRLv0DrCvXZuViMk9YG4woaJmDfrJWaC7Ca0QHcInfsZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GC9brIbCnz-B5W0tNQ2D-KkqLCwB7oGDkCKeSe96uGHkxMaGcN1ipLKXEHKzipT9Y2dOLyaTbe2QHteOOAbe_QcgZafh5qpZkX4G2w8a9PzqbGqo8AQ-ho-PTg0CvWRfwprsSrVPB1Fdk5_m-v5VBc-W-Hwg3EWiE-AplFkaZqQV2N7XfhPKE47eqYYfkRQzkRWnDZWoXnPLF0oVHfql2Vaq2X3T5Rzvs5A5a3Z7ohStLBIV3uvfdYL4DDiUdpHTjUmy4hr8tn3xDAz12_kNXz8JwZDE_SfvK1CwsyNS7yTwhsv65fdD7BBGCazJQXdGihOth_tV1xeKbZVsGJ1Zgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vismGR3iDDRxfxNcildm3MyLaZrR4clZCJOz-RJDBJVNVpXRIQw6nI-SprSvYEzEbPr2i1ctQIE_eq1gd-umzxtjI7o_ASev1SOUIAj6YyQS1MIGy0ZsOCsZmtXOBmBPUv-TwxXDx8Dogf62NQIlblItWwQB2Dl60uLuca9nkwFn0aMQoArBYgP1z1zjCwJ18y329acP3wjxLg-X7AOUZ1e7OlQx35gWW3f5YFIRU3XzakM27GHu3A4dEoA0n7H-os6wJ_J9cfTsw2ZrQzIok-RomIqh94GFRtESCEh758eFFS3oJex4PhsVOEFUrfINIcw_9hFK2iTlhAgRdRl1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Oz3BrOuvZSBz0QkZ-aHIxu5p0B3Nb9EE5CGCnLPEt_ygIhy5JUIoUoLK1kImfaMvB3RdkHKCwfcmEpQ9a5e38r16qZRqC6pMhv1ibVCmcuLQTzSKj4bHMgufE5Xm5eWSxmkut0JG4zEvhAIuZjZyVhGn9WTVEbDeiZ1U2vf1x9OYd3_DisvaN8XLs5x3bLGqkB4IX05WMvSNyDLs3-MhOmUja_H0l1o0fiMLI46yLAnXrf8AZ8-ASdQkJ0yIGCvKf-3rOtVb-ADOaHWvqymF7BVekJ3pvhWjYuQ9ppziyKjZPnw1CBe90SA2IcVtCpUwNsyGZH5hRwrpz6yJXcDvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
