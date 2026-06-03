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
<img src="https://cdn1.telesco.pe/file/KrIa19vfpqNU0xNGK9OwNq4JPHMysnwQoPlGXo53iWVpTJp9G1iZjjpWjZwsDP2c8NV68YFcchn5DjbJhYPtILWyeg5fiPSTETGKlJ4f8CQp2LHEHjHvPDKahJ1HqD9iUHzJ2V9kKtZtdUBWj7KAgQt4McxTwAKO0WC-WHLOtI1mFmvb8Y-n0dEUUyYYYb0ndcjhA4rRXqFWM2L9K7SIfFZ6zB9z8nAwRwM5mhtQBnRBRnzI7-Vi5MexuMyZY4BcAl71UgXOw65ywimwcyVotIzpp_Iqr747_jOoZ6EmW7qy14UIdq6ZakB8jvDljEe1vsSaZMGGjNN0TxC4HWqkHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 162K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiهمکاری:@MatinPaiSen</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 00:03:17</div>
<hr>

<div class="tg-post" id="msg-3688">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یکی از دوستان این روش رو رفته بود برای مشکل اسکنر و برطرف شده بود این اشکال واسش:
متین جان برای مشکل
https://t.me/MatinSenPaii/3652
از این کد استفاده کنن دوستان
pkg install wget -y && pkg install unzip -y && wget https://uploadkon.ir/uploads/c86602_26senpaiscanner.zip && unzip c86602_26senpaiscanner.zip && cp senpaiscanner /data/data/com.termux/files/usr/bin/ && chmod +x /data/data/com.termux/files/usr/bin/senpaiscanner
بعد از اتمام کار
کافیه برای اجرا
senpaiscanner
رو بنویسن و اینتر بزنن
(توی نسخه ۵ اسکنرت)</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/MatinSenPaii/3688" target="_blank">📅 23:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3687">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به مناسبت ۲۰ هزارتایی شدن، یوتوب هم ۱۲۰۰ دلار از کل درآمد این چند ماهم(که موفق نشده بودم بگیرمش سر مشکل ادسنس) رو خورد و با ادسنس چینج، کلا پروند همه‌اش رو
😂
عاشق این آمریکاییام</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/3687" target="_blank">📅 22:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3686">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">به مناسبت ۲۰ هزارتایی شدن، یوتوب هم ۱۲۰۰ دلار از کل درآمد این چند ماهم(که موفق نشده بودم بگیرمش سر مشکل ادسنس) رو خورد و با ادسنس چینج، کلا پروند همه‌اش رو
😂
عاشق این آمریکاییام</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/3686" target="_blank">📅 22:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3685">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EdmO-kIwWzK0sg71hy85ioW786EtFqNKOp1n4_nSvu5yuaoKK8F0Hj8vPWzi9X5XDuVfu3mNsTq9Ef4SikyBL23zAPf6bDsHXYqi0xND8teTSOcNkFBE310v0Rj2Zgg_tQ8z-cJWk-NyL3bAq0G8c0CiZljdaCB0ZDdysCy71kE8il--qu8Hyv6IB-rU9uBBXWBlFzC9mFkpz8xCgLcw2YRIrTomI7T29uKtstSoIR4ndGghWCCmVBJuz4x0X62QDRv5pD9dTIp1nwFSVIcka-6DisyrHsc93ZyBneq6DDtP4hPPOOxP1ZFRJxksD8eZaa_TAsm_2BxV4WhZ572f-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدده هیچوقت مهم نبوده و نیست. اما مناسبتیه که به خودم یادآوری کنم اهدافم رو. از 2021 که با یه گوشی و ذوق مسیرم رو عوض کردم و اومدم سراغ یوتوب، هدف والا و بلندمدت من، گذاشتن یه تأثیر مثبت روی جوونا و نوجوونای خوب وطنم بوده. کسایی که ارزشش رو دارن، عقاید و شخصیت درستی دارن، انسانیت سرمشق‌ـشونه و شرافتمندانه زندگی می‌کنن.
شاید یه جرقه‌ی امید توی این تاریکی.
شاید جلوگیری از خودکشی چندتا از برادرا و خواهرام.
شاید ایجاد شغل و ایده دادن و کمک بهشون.
توی این خراب شده، ما فقط همدیگه رو داریم.
ممنونم از تینا، پارتنر عزیزم. کسی بود که من رو از تاریکی بیرون کشید، و بهم امید زندگی داد.
پنج سال گذشت، و از مسیری که رفتم پشیمون نیستم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/3685" target="_blank">📅 22:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3684">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شما یه اپلیکیشن می‌بینید، یه لینک ساب می‌بینید، من ساعت‌ها و روزها زحمت و هزاران دلار هزینه از جیب شخصی بدون چشم‌داشت و تلاش شبانه‌روزی می‌بینم. هم از بچه‌های وایت‌دی‌ان‌اس، هم از بقیه‌ی دوستامون که برای اینترنت آزاد تلاش می‌کنن
✌️</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/3684" target="_blank">📅 21:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3683">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/3683" target="_blank">📅 20:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3682">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3682" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3681">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الان که بهش نگاه می‌کنم، از دی‌ماه تا الان نزدیک ده سال گذشت...</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3681" target="_blank">📅 15:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3680">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MSGv33MPVIAXyuoPTFFX_mHD0_9iv4dSVqVnT5xqMhDHZlcCdRW06dr0SvtEtIxnd8Fzx3O3Jeh-qJbcFsKs3awfwSIyAlnjJ4PqmPvzfH-kkrs5z5AKmRxobFB23Yz2hfp9QwmCguTaZzulul8FDEwHJiR11f9v5GBuCJ-0S6a4f6WaFGaPV5aMubADE0Ss3mHMAWKPi3FdZoDJA2FtRm2D2FTlrxq2e14iWDTD2kL6TPUMgCKU09ndeYCOyVcQMtphtG9YY1k8UswTBEbc6cAvM_l4ztxmx2uWN0AtulZ27ymUt5seLew13-hk1xWXJqmO3eGw8gFj7T_ruieGHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام آموزش‌های مبنی بر اینترنت آزاد که من توی کانال یوتوبم منتشر کردم به علاوه‌ی توضیحات و اینکه توی چه شرایطی به چه دردی می‌خورن. از بالا به پایین، برای شرایط سخت‌تر معرفی می‌شن تا شرایط خاموشی کامل:
1- متد Paqet، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل باز شده) واسه‌ی هر نتی(تبدیل سرعت اینترنت داغون به سرعت خدا)
مزایا: سرعت بالا و راه‌اندازی یک باره(هم مستقیم هم تانل)
معایب: نیاز به سرور داره، روش مستقیمش فقط روی سیستم میتونه ران بشه یا گوشی Root شده و تانلش مصرف داده‌اش ۴-۵ برابره
ویدئوی اول آموزش Paqet مستقیم:
https://youtu.be/q4BbgdhPm-w
ویدئوی دوم آموزش Paqet تانل:
https://youtu.be/nwpLOANv7VY
ویدئوی سوم آموزش Paqet با نصب آسان(اسکریپت سم):
https://youtu.be/QkGI8WoOtPc
2- متدهای بر پایه کلودفلر Workers، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل باز شده) واسه‌ی اکثر اینترنتا به علاوه‌ی آیپی تمیز
مزایا: سرعت بالا و راه‌اندازی یک باره، نامحدود بودن(هر اکانت روزانه 6 گیگابایت حدودا(هر شب ریست میشه) و می‌تونید اکانت‌های زیادی بسازید. من خودم نزدیک به ۱۰۰ تا ساختم)
معایب: فقط وب سوکت میشه ساخت و ممکنه برای گیم و... مناسب نباشه اما برای اینستاگرام و یوتوب و اینها خارق‌العادست.
سری اول کلودفلر، پنل BPB:
آموزش اول: ساخت فیلترشکن بر پایه پروژه BPB و اسکن آیپی تمیز با سیستم:
https://youtu.be/_aXy8wwyRG8
آموزش دوم: تنظیمات پنل BPB از سیر تا پیاز:
https://youtu.be/7G9Fjhe_NxM
سری دوم کلودفلر، آموزش پنل Edge:
آموزش اول، ساخت پنل Edge با سیستم به علاوه تمام تنظیماتش و ثابت کردن لوکیشن:
https://youtu.be/svYBcv4bSzo
آموزش دوم، ساخت پنل Edge فقط با یک گوشی موبایل و نصب ترموکس و اسکنر برای پیدا کردن آیپی تمیز:
https://youtu.be/2otJfXgNWCM
3- آموزش کامل خرید سرور و دامنه و نصب کاندوئیت بر روی سرور ویژه ایرانی‌های خارج از کشور که می‌خوان کمک کنن به اتصال از طریق سایفون:
https://youtu.be/DtZyWXWV4BA
4- متد SNI-SPOOFING که در صورتی که یه روزنه‌ی کوچیک باز بمونه، می‌تونید باهاش با نهایت سرعت حتی توی بدترین قطعی‌ها هم وصل بمونید.
مزایا: بدون محدودیت سرعت، می‌تونید کاملا رایگان وصل بشید(با کانفیگ‌های کلودفلر متد شماره 2)
معایب: نیاز به باز بودن اون روزنه داره، و فقط روی سیستم قابل اجراست مثل Paqet. اما قابل اشتراک‌گذاری به دیگر دستگاه‌هاست.
آموزش اول: راه‌اندازی SNI-SPOOFING و استفاده ازش روی ویندوز:
https://youtu.be/dujMBt4sCpw
آموزش دوم: رفع مشکلات و ترکیب لوکیشن متد هر کانفیگی از SNI-SPOOFING روی آمریکا:
https://youtu.be/PuYwXH4D4tU
5- متدهای بر پایه‌ی گوگل. این متدها مادامی که گوگل وصل باشن، کار می‌کنن و طیف وسیعی از متدها رو هم در بر می‌گیرن:
الف- متد MHR و زیرمجموعه‌هاش: این متد محدودیت ۲۰ هزار ریکوئست روزانه روی هر جیمیل داره و سرعت آنچنان بالایی نداره اما با تعداد ایمیل‌های بالا، میشه بهترش کرد.
آموزش اول، متد MHR خام(توصیه میشه بعدیا رو راه بندازید نه این. چون با آیپی خودتون باید برید و هوش مصنوعیا رو نمیاره واستون):
https://youtu.be/jzaqdKl40Ww
آموزش MHR-CFW(ترکیب همین، با کلودفلر برای داشتن آیپی خارج):
https://youtu.be/L3lJZrAqqUQ
آموزش راه‌اندازی MHRv-RUST با گوشی موبایل:
https://youtu.be/7YdJIJloIxY
ب- متد MITM برای دسترسی به سرویس‌های بسته شده‌ی گوگل(چون از روش یک حمله‌ی سایبری استفاده میشه روی تلگرام آپلود شده فقط):
آموزش اول دسترسی به سرویس‌های گوگل و گیتهاب:
https://t.me/MatinSenPaii/3151
آموزش دوم دانلود نامحدود از یوتوب با نت ملی بر پایه‌ی آموزش اول:
https://t.me/MatinSenPaii/3230
ج- متد Skirk بر پایه‌ی گوگل درایو که مزایاش، سرعت دانلود بالا و معایبش، Latency بالا هست؛ از کانال عزیزی:
https://youtu.be/vCr4E6Y1k4c
6- متدهای بر پایه‌ی DNS، که از روز اول جنگ وصل بودن تا آخر قطعی. اما ما اواخر قطعی بود که به بهترین ترکیبش رسیدیم. پروژه‌ی MasterDNS و کلاینت WhiteDNS. مزایا: وصل توی هر شرایطی، قابلیت اجرا روی هر پلتفرم و سیستم عاملی، حتی روی سرور، و اضطراری‌ترین راه چاره‌ی ما
معایب: مصرف حدود دو برابری اینترنت(که به نظر خودم می‌ارزه توی اون شرایط) به علت کوئری‌های DNS فراوان. همینطور نیاز به سرور داره اما از سرورهای رایگان هم می‌تونید استفاده کنید(طبیعتا سرعت خیلی پایینتر)
آموزش کامل راه‌اندازی روی گوشی و سیستم:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3680" target="_blank">📅 14:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3679">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">امروز واستون دسته بندی می‌کنم یه کم راهکارهایی که تا الان دادمو</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/3679" target="_blank">📅 08:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3677">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/keC7hsKlZo1FYQEH4U4Qf9eh2Epk801WwpnW_LkjnpcP7kp4gRF_rgNUsBHYVsg6L1RYfm4_OyZL1ynXsBSiHbVbnNo-WLZUmjmGs27a8QN5vpnjJcXs1KM1cjZws8JMtq66mRbqhRn5LWG3x9-oUYJ0WCdCLw8nOZsv2SKtXMNkL-9h_RP3D8_5_N0NyNEWtoBE5eswaMg6xNpTvmSjCRGJAKcMPoi6rWH9CXOpTfc4Fxei04QtMCGHmtSWulliGAKmJV2E3jplu1dOgxOMfNul9W-d1wnzEXumIoYIfGcGabS1DyIhg81tPqHcqVF0jx8MO0BIltgusF1EI7xSLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/215e27ea42.mp4?token=ptGolGyRfc82fLTmI2FY5OiyRY9TVgWHZq8FXHssFOFxIX85k_B6WIASPK7FfXTlB55nPoR-KCSOmY51gNtpZXd-_fo2_uZg85KSFXn_GN2Ui0oqYR70nvc8jXkO8BHjpmWzbR5hdCqFofLFbqosLIkGbo8G0yJP-HCd4p9B8MV2YWpPldt_SKKr7mRRdZtUqoPg0nctCh7UJ5WQ___v-2lGYvQmzdTC_38Y2JlBxq-qo_nAYTP4-vYCU-XnJlddiu2RfJ4xOccAb0FCr9PPe4V2z-oJAh_LOZQAtTHXbqfWc5kNffpxICXwnGh8CaNEhKq08IPt-Iq2rN9fBk1PzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/215e27ea42.mp4?token=ptGolGyRfc82fLTmI2FY5OiyRY9TVgWHZq8FXHssFOFxIX85k_B6WIASPK7FfXTlB55nPoR-KCSOmY51gNtpZXd-_fo2_uZg85KSFXn_GN2Ui0oqYR70nvc8jXkO8BHjpmWzbR5hdCqFofLFbqosLIkGbo8G0yJP-HCd4p9B8MV2YWpPldt_SKKr7mRRdZtUqoPg0nctCh7UJ5WQ___v-2lGYvQmzdTC_38Y2JlBxq-qo_nAYTP4-vYCU-XnJlddiu2RfJ4xOccAb0FCr9PPe4V2z-oJAh_LOZQAtTHXbqfWc5kNffpxICXwnGh8CaNEhKq08IPt-Iq2rN9fBk1PzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Operator: Asiatech/Datacenter Time: 2026-06-02 22:22:04  The status of this service has changed to:
❌
DNS google.com via 8.8.8.8 : timeout</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3677" target="_blank">📅 04:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3676">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">هیچی.
موشک زده شد؛
اونا هم گفتن دفع کردیم.
ما مردم بدبخت هم چیزای عادی‌تر دیگه‌ای از سبد خریدمون حذف میشه فردا و پس‌فردا و روز بعدش</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/3676" target="_blank">📅 03:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3675">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=T2tzBzBat38gCkRLA1vxIGFBNTIHA5ExIvhylWpJjr7nfN21km_iFwWYvH8-4yvALq8atsf7xdvRc6EzHIYM3xMI5MGMCa8x8GjUcvI3eRSOdvo8ht72_uCVmI4V8YKo2w23KdrYz9g__XSiEww0NCHmoGgMoRCVZFgENqzdRtBBmKiR8sbD_-p97CeWta7EyhTbHxLZDXx_9dEMKNcCal13FD645PXPYvUGdqZjI3z7zOcvKRD1unYi5k8OVJhph0hh9ZcIjvChCS5MFQaJvuj3AhsX2tAHJoHbiRugkHjSYaYmqTHOjog_JqWL-p8Q-Cq7tKyptAaPq5icmjkjZYnaDO5cb7HP1MU3Da6KATF8vW5MhjFWr3iaiyocDAKb8DrZuHCAafmeToeTf4N4pWEsmUwGh6Hra-ho7Y1ex6J99TPTT2BGfOvRDilftkwGrD9qQ51-qxNJlpPIfdhLJ98E_TtSPyMCxDAWk--SB1_a2nQiyccJiKuAwrRlcMb-TcnMfMJMbOh3QQrsLnuRZ9iYRwyLawWVntX4SrPVWU7w9Mnzuxt8mOkGcgTyfl9DnzZL58Wzq6Z09AhcdRBqQxqsk-PZjXw36g5JxF-vWz-UhLHembLceyhryK1UEPV1R5nyYlvTFtMt4uA9jj100EMyhp4HOwJwc53hd_n6alo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=T2tzBzBat38gCkRLA1vxIGFBNTIHA5ExIvhylWpJjr7nfN21km_iFwWYvH8-4yvALq8atsf7xdvRc6EzHIYM3xMI5MGMCa8x8GjUcvI3eRSOdvo8ht72_uCVmI4V8YKo2w23KdrYz9g__XSiEww0NCHmoGgMoRCVZFgENqzdRtBBmKiR8sbD_-p97CeWta7EyhTbHxLZDXx_9dEMKNcCal13FD645PXPYvUGdqZjI3z7zOcvKRD1unYi5k8OVJhph0hh9ZcIjvChCS5MFQaJvuj3AhsX2tAHJoHbiRugkHjSYaYmqTHOjog_JqWL-p8Q-Cq7tKyptAaPq5icmjkjZYnaDO5cb7HP1MU3Da6KATF8vW5MhjFWr3iaiyocDAKb8DrZuHCAafmeToeTf4N4pWEsmUwGh6Hra-ho7Y1ex6J99TPTT2BGfOvRDilftkwGrD9qQ51-qxNJlpPIfdhLJ98E_TtSPyMCxDAWk--SB1_a2nQiyccJiKuAwrRlcMb-TcnMfMJMbOh3QQrsLnuRZ9iYRwyLawWVntX4SrPVWU7w9Mnzuxt8mOkGcgTyfl9DnzZL58Wzq6Z09AhcdRBqQxqsk-PZjXw36g5JxF-vWz-UhLHembLceyhryK1UEPV1R5nyYlvTFtMt4uA9jj100EMyhp4HOwJwc53hd_n6alo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/MatinSenPaii/3675" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3674">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">من الان خودم با WhiteDNS آنلاینم(داشتم تست میکردم دامین اینها نپریده باشه)
خواهش میکنم ستاپ کنید هر چه سریعتر. هرچی نیاز دارید توی ویدیو هست
https://youtu.be/6Pm7kNQb3mo?is=Hh_zNDNmPQGHgzLb</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/3674" target="_blank">📅 01:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3673">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=VcqU_fdMQd3W0uuk4FqW34TmUWR9u1UFi4aNwi1_pDBltcFDPkOsM-D8Rn78APeCFmtp4rFBL-KKQR3dFzd8i5IAj3yKRdaL2PeghbnN0gz_WzYIDbP5-stfzFDvnB4EubMSRit3iEqo6guRbYQsfTZDS4DUCDvolGK55lD0mUnfvymja5VEw0aL30-GBSjX2ZuznUnYmQ0yKWu35m5uipJxPebC-Af5derUrWOXNGHzNMAmCouuP827H9Us8_xt0W1sAVwPp2EF9482C_n70oU9j0Uoh8PaTjISoCP5fQElH6UYWi2_owE-h44oWSeqBlg-Q9C_j0KCGAt9F9s7OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=VcqU_fdMQd3W0uuk4FqW34TmUWR9u1UFi4aNwi1_pDBltcFDPkOsM-D8Rn78APeCFmtp4rFBL-KKQR3dFzd8i5IAj3yKRdaL2PeghbnN0gz_WzYIDbP5-stfzFDvnB4EubMSRit3iEqo6guRbYQsfTZDS4DUCDvolGK55lD0mUnfvymja5VEw0aL30-GBSjX2ZuznUnYmQ0yKWu35m5uipJxPebC-Af5derUrWOXNGHzNMAmCouuP827H9Us8_xt0W1sAVwPp2EF9482C_n70oU9j0Uoh8PaTjISoCP5fQElH6UYWi2_owE-h44oWSeqBlg-Q9C_j0KCGAt9F9s7OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/MatinSenPaii/3673" target="_blank">📅 01:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3672">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">به نظر که جنگه
چون بالستیک زدن
اگه آمریکا نگه اینا نقض آتش‌بس نیست</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/MatinSenPaii/3672" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3671">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">لطفا WhiteDNS رو ستاپ کنید هر چه سریعتر تا قطع نکردن:
https://youtu.be/6Pm7kNQb3mo?is=Hh_zNDNmPQGHgzLb</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/MatinSenPaii/3671" target="_blank">📅 01:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3666">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">استفاده از فرگمنت هم جوابه</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/MatinSenPaii/3666" target="_blank">📅 00:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3665">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k22cSh7ShIk6IzvJePl7nLI0Xw1ciGtXH1yOQc3157nkjewBXeAGNrRP2yDNdY0d_QpihXYXnstTiXT_4xJhmjbRqvyOpu12Jvn5oH7owkzX4rOEpV6Z_RVFFaxm_hG9b8jHCYgRjQ0SUuvp7SYUgT3Ln_6x57MYJ_Ljd4U2ZHTB0oMqEMn7zWsA4EwJEm3Juq39_FO3Lu8SnNcx7ZzKOscQLb2ipKPxQJpTvImLgXVJbCVNiQJt2gmB-rjRQu2ptpuJbh3A5s1EPVJ4VVwmQ16o44Hx9o8YIwlNL7lwTuc4J9sOb6s2JOyp4EisXjHPXqmGZI0NCyaHZCIWNI8rqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مشکل آپلود روی کانفیگ مستقیم پشت CDN، تنها راه استفاده از اسپوفه. sni spoof</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3665" target="_blank">📅 00:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3664">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دیدین گفتم
😂</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/3664" target="_blank">📅 22:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3663">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-text">Operator: Asiatech/Datacenter
Time: 2026-06-02 22:22:04
The status of this service has changed to:
❌
DNS
google.com
via
8.8.8.8
: timeout</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3663" target="_blank">📅 22:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3662">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">Operator: Asiatech/Datacenter Time: 2026-06-02 21:01:30  The status of this service has changed to:
✅
DNS google.com via 1.1.1.1 : 142.251.14.138</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3662" target="_blank">📅 21:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3661">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-text">Operator: Asiatech/Datacenter
Time: 2026-06-02 21:01:30
The status of this service has changed to:
✅
DNS
google.com
via
1.1.1.1
:
142.251.14.138</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/3661" target="_blank">📅 21:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3660">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BGNhiW5V4uflpbX0_b0lQkrx6hLTdw9YXvfSECEzqyWbELDPZzpm05r3nL2-u2g1JOvIMx4j_51jyZbOcJq7aiKN-FIS-CeXhQbuNRnc9QHI-Hr8C_DVQlXzlqQ3pSNnvozxu_Zojz7lC9_DtwPotd8IjxbPLpvjldKjpbIZhg6wAlPzxYAzoeqihJitNkHV2XVL_GuyICRjge6p7xiLNzFrbqBpPo5dOe-BZNjXytzFB0as1vPNUk1SoSCih-ZUcCgfAHnGYoS50f7CHm4WzVQd3I62OgoAeLxSpatCivyhRjeE4bpAVwrIZRx4mXvrhAWKDR-fjE598fN_PLpMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچند یک سری دیتاسنترهای خاص یه سری تانل‌ها روشون جواب میده به راحتی. از جمله Paqet و بک‌هال و  reverse</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/MatinSenPaii/3660" target="_blank">📅 19:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3659">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W3qA_kYoPcQwixuztyo0vkIjFfOK3NjGmf2x2dS6YItELeQVtG59X5FyR4YbZeb9T6Hd8tqiwtGUwnzsLMbMO2TiGZ4uMlnUyQx8arZ2s1hisQaJFGkCxuEs_sLcrCjrlmXJnHvlpKVC3huqqGJQ_6WUsdV6aZNUv6btkNRQNLbvMOJv3ELT9Cbnktxp4G5gTor0Qt_0kZs7NwI0n4hvhzMN5D1q94O7KyYcvbSn-LT6HYVa5OBctTkhXTfBKj5Y7zJwhlbC8BttBzh7RG86_YegBBRzR1L_jumY8VAhSJjy0jnc4glhv0hC0U_FmOPlpXtOXf525K9t6_hVtmGinQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت نامحدود تصویر با هوش مصنوعی Nano Banana 2 گوگل + طراحی رابط کاربری(UI) و ساخت ویدئو و موسیقی
⭐️
توی این ویدئو:
1- بهتون نشون میدم که خودم Thumbnailهام رو چطوری میسازم و چه شکلی می‌تونید به صورت نامحدود از Nano Banana 2 و Pro گوگل استفاده کنید
🎤
2- یه UI باحال با هوش مصنوعی به همراه پروتوتایپ طراحی می‌کنیم
❄️
3- و با همدیگه یه موزیک در مورد 90 روز قطعی اینترنت می‌سازیم
🎧
🤎
اسپانسر ویدئو:
کانال تلگرامی ذغال سیستم؛ فروش لپ تاپ و لوازم جانبی استوک وارداتی دبی:
https://t.me/ZoghalSystem
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3659" target="_blank">📅 17:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3657">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ببینید MHR و mhrv-rust و skirk و flow drive و تمامی متدهای بر پایه‌ی گوگل، با اولین بادی که از سمت سرزمین‌های دشمن بِوَزه قطع می‌شن
تنها چیزی که برای ما می‌مونه، DNS هست که همون هم ممکنه سرعتش خیلی خیلی کم باشه و می‌تونید از اینجا
https://youtu.be/6Pm7kNQb3mo
آموزشش رو ببینید.
متدهای بر پایه کلودفلر مثل BPB و Edge و... هم که یه پله بالاتر از MHR و اینها هستن و طبیعتا همیشه بعد از وصل شدن گوگل، وصل می‌شن.
هرچند به WhiteDns هم نمیشه ۱۰۰ اعتماد داشت که برامون بمونه چون توی هر سری فیلترینگ ما غافلگیر شدیم. مثلا ما به هیچ وجه فکر نمی‌کردیم بتونن جلوی Paqet رو بگیرن اما تونستن. هرچند امثال پترنیها هم با SNI Spoof، اونا رو غافلگیر کردن!
برای همین شما ترجیحا متد مستر دی ان اس رو توی Whitedns به عنوان اضطراری‌ترین راه، داشته باشید علی‌الحساب</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3657" target="_blank">📅 12:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3656">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/MatinSenPaii/3656" target="_blank">📅 11:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3655">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-text">گروه Void Verge در تازه‌ترین
#گزارش
خود اعلام کرده: از زمانی که اینترنت ایران دوباره توسط دولت بازگشایی شده، تغییرات گسترده‌ای در شبکه داخلی کشور درحال انجام است. پس از هفته‌ها قطعی و محدودیت، تقریباً تمام روش‌هایی که در آن دوره مورد استفاده قرار می‌گرفتند مستندسازی شده و به دست نهادهای مسئول رسیده‌اند. سیستم فیلترینگ خود را برای مرحله بعدی اختلال‌ها و قطعی‌ها آماده می‌کند و روش‌هایی مانند DNS Tunneling، MITM و Domain Fronting به احتمال زیاد در قطعی‌های آینده دیگر کارایی گذشته را نخواهند داشت.
علاوه بر این، نهادهای مسئول فیلترینگ اقدامات گسترده‌ای برای ایجاد ارائه‌دهندگان واسط انجام داده‌اند؛ سرویس‌هایی که خدمات خارجی را با محدودیت‌های شدید در اختیار کاربران ایرانی قرار می‌دهند یا وب‌سایت‌های ضروری را که امکان استفاده از روش‌های قبلی را ندارند، از طریق NAT در دسترس قرار می‌دهند. در چنین شرایطی، انتشار عمومی و علنی روش‌ها نتیجه‌ای جز آسان‌تر کردن کار نهادهای فیلترینگ ندارد. این سازوکارها باید دور از توجه، به‌صورت کلوزسورس و کم‌سروصدا فعالیت کنند.
در همین حال، مافیای اینترنت در ایران بیش از گذشته قدرت گرفته است؛ مافیایی متشکل از افرادی با دسترسی به «اینترنت سفید»، برخی ISPها و مراکز داده که از طریق سازوکارهایی مانند سرویس‌های پروکسی و سرورهای اختصاصی مجهز به NAT، اینترنت نامحدود را با قیمت‌هایی در حد صدها میلیون تومان به فروشندگان VPN عرضه می‌کنند. این مافیا آن‌قدر قدرتمند شده که توانسته بر سیاست‌گذاری‌ها نیز اثر بگذارد و حتی در شرایط بحرانی و دوران جنگی هفته‌های گذشته، به حفظ هرچه بیشتر محدودیت‌های اینترنتی کمک کند تا منافع اقتصادی خود را حفظ و افزایش دهد.
برخی شرکت‌های ساده میزبانی وب در ایران تنها طی دو ماه قطعی اینترنت، به فروشندگان بزرگ VPN با درآمدهای بسیار بالا تبدیل شده‌اند. ما در هفته‌های آینده به جمع‌آوری و انتشار اطلاعات و داده‌های لازم ادامه خواهیم داد. اگر این روند ادامه پیدا کند، هدف بعدی باید مقابله با مافیای اینترنت در ایران باشد. امیدواریم این روزهای سخت برای همه ایرانیان به پایان برسد. آسیبی که از سوی دشمنان داخلی و افرادی که زیر سایه جنگ از مردم سوءاستفاده می‌کنند به جامعه وارد می‌شود، گاهی از خود جنگ نیز دردناک‌تر است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3655" target="_blank">📅 11:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3654">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستان برای هیستریا، سرورهای AWS آمازون با این سرعت جوابگو هستن چیزی که من دیدم و دوستان گفتن و متأسفانه دیتاسنتر دیگه‌ای ندیدم که به این خوبی باشه. آمازون هم گرونه به شدت
پس از آموزشش فعلا منصرف شدم</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3654" target="_blank">📅 00:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3653">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شمع Iced latte</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/3653" target="_blank">📅 23:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3652">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ct3vifdgUFq83eBCtAH6MbKwkrnofaj0pWSsms2lZthsIu-qvDU8RZ247MPSbdVVh8ibSZU30jIBRTmle6IsY-ZgAy2WjA2zROwuW7ypi-qXR8X3Ruu8TJT6aIt4Uh7p2h-Du1A2KHqe_5LyeuskgF7TQjkCZ3evy6r3FVg93VmYUA4btbFwAJlgSZCLj8YpOBgikOk7ZhrIUh_3IN98s20q3asSd4_bpivDTQ1rKci7kFa9ytAcrTj0GtAuVVVjTUzYi1Y6RW6G9ESkR3dXyqAyMoEf9AX3lTx94qntbsuZG8aBhL-Umt0tlYkOosf5-AGjCLMfO3WpCdWEQtiP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ارور EOF و 403 گرفتید یعنی گیتهاب هنوز روی اپراتورتون مشکل داره و این یعنی اسکنر نصب نمیشه(باید با وی‌پی‌ان بزنید). طبیعتا وقتی دستور senpaiscanner رو میزنید not found میده چون اصلا چیزی نصب نشده</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/MatinSenPaii/3652" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3651">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3651" target="_blank">📅 20:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3650">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F3s8RXEhXL-vCwBfVOVOm3hDwdGOh86RHBtoSAiXGMlbsiGypO5WNQELUbhvFWB9S4oGVnqkDVElaXewPoWGPKIAfKUSHYEcRbNB3YBrW5KA3NvSejosLKm7sN1Pyip6kCgV-N8-u4mcQ7qUxK2JOH743VMcI4FNxOJcgj_j71-N8Qd-CecYdCKZ9t0B0MEWowVrxCBnW5pOOXfJ6y4546vbmFWK59-Gv3hrN92EbFUOwBFSBGDmPdl3hEkaIKX_Owrt95NSl_IBj1R5CHuQ1C5eVPaTywKir-PK8JM2z-EkI8Pp2n4m7Ofk52VzsI6dBivUgXNeOiSyChKv9wnVMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به این ارور خوردید، پروژه‌ی جدید بسازید. اگر باز هم نشد، با یه اکانت دیگه وارد بشید و مجدد تست کنید. توی این ویدئو
https://youtu.be/_aXy8wwyRG8
به همین ارور خوردم و این شکلی حل شد</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/MatinSenPaii/3650" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3649">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/3649" target="_blank">📅 19:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3648">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون متصل بشید</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/MatinSenPaii/3648" target="_blank">📅 18:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3646">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A9_7PPz0qzBs0Dgze6C5ZKYocBGKD2yttwCgrNWpbbB54TMY6jDbSgsKh-m9E6BQQB9VTMpOzxwwZU7DaMV0xgGnEOq_S80OVRLugjeFEckDBZ5hc1o1clv-l4KX8W80T6zYVfkuGUUMZT3_csYHImJv0HHNLqLpyMTGXgy7eg8rFUDqULbFLePZcYXc0SikcexFwWkwLTWzj0uegSlFhqr5pkyON1mreCZAay0vOgsJ4Pzyv_el3i83hdQams0xV5UW5cBIg1-5H2OUHT9o3W8zRaOw_mhERujLTPRdaYxol5d87Q3h35d4gYqv7tjVr0gDzvELdAsRIpqUWzKYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fj8Ku8KiuZ5Kfjj4u3yS-8onaRq5dcdjWnCbFri9jPxltdrjyjKMSZ3QBpJ-RhgdPmwdgcWX_0kVTyijAnDWNO8Vfuz-OI3YLjYV4t8MEc8k-UIWFEcq9c-ZP9ODznapF2ujhedSGtzUu7BkziK4ly3aBQJcO5N584gPfBuNNa3R6bpSLUQLoWw_R0l5L_57_-MmQ0OCzD08Ga2OMPxSfIpTuH0GVaNT-GgoYPFnwIC8o7iTP-8YI3IIib1Zx8L0vOEqpTInC274EltkVUCX33IMEjxleXGYAtuDRRSlNm7fuHXRTyDXZOLXezF5D3g9_W6ZWd-sBTboGzu7pivyfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/MatinSenPaii/3646" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3645">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V4-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3645" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 33 تایی از کانفیگ‌های Spoof که همه‌شون کار می‌کنن و خودم تستشون کردم</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/3645" target="_blank">📅 17:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3644">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">base.apk</div>
  <div class="tg-doc-extra">11.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اپلیکیشن RSTA(که به زودی اوپن سورسش رو هم میسازن عزیزان)</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/MatinSenPaii/3644" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3643">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-on-Phone.txt</div>
  <div class="tg-doc-extra">350 B</div>
</div>
<a href="https://t.me/MatinSenPaii/3643" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات اسکنر برای Termux</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/MatinSenPaii/3643" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3642">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux
دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون متصل بشید
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی  Edge برای ساخت کانفیگ رایگان:
https://github.com/cmliu/edgetunnel
فایل دستورات ترموکس:
https://t.me/MatinSenPaii/3643
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
نرم‌افزار RSTA Spoof هم اینجا:
https://t.me/rstasnispoof/2/1076
و
https://t.me/MatinSenPaii/3644
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت کانفیگ Edge(روزانه 6 گیگ رایگان با کلودفلر)
2- نصب و استفاده از Termux برای نصب اسکنر من و پیدا کردن آیپی تمیز
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Edge
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- استفاده از آیپی‌های تمیز توی Json  اسپوف و اتصال پرسرعت به اینترنت آزاد
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز به هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(با کیفیت بالاتر)
💰
دونیت</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/MatinSenPaii/3642" target="_blank">📅 17:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3641">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nGQ-UhcLE1uKmMtj6l9-KXfWMynCIZGo7VF0khLPSucuaKa-dzB34P0jd7x496tIYuTw2J54Y5UkCjMuyOAbldiSlL-18Tu3HPFPd9G7xlmXbtF_IPrndpjR9jNJkmoC9uFbE2r4g7rkAcijjZYvFxMCpheshlONw3Zkid3Q32P2wU1oknVW_VNTJpF9OxRS-q0umVVBJWN7Co3Yll--StSQdiICKMdT9CWvxJJTf5C-scENYOVLl9Am_yqdx8L3udL3RDL3nXLRT0YONbRla1nIuitJhbnbGIY-iqOV7B_IiciAeWGsVimFRB1OHPmi486JNcFztjXdJ_bvXdnMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ربات از
یـ‌ بـ‌ خـ
عزیز واقعا باحاله. یه نگاه بهش بندازید:
@iNewsSummaryBot</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/MatinSenPaii/3641" target="_blank">📅 16:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3640">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تصمیم گرفتم یه آموزش صفر تا صد ضبط کنم برای عزیزای دلی که لپ تاپ ندارن و فقط یه گوشی اندرویدی دارن
از آموزش ساخت کانفیگ اسپوف گرفته(رایگان)
تا اجرای اسکنر روی ترموکس(سردرد)
و استفاده از اپلیکیشن اسپوفی که این دوستانمون ساختن
یه مقدار طولانی میشه اما دوست ندارم واقعا که بچه‌های اندروید کارشون لنگ بمونه</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/MatinSenPaii/3640" target="_blank">📅 15:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3637">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kz7_u6c02a4sgLzNafgN0fM_eRW2yeXZHfC-ZFwgvqgvj7aQM1QY8qTL8Q1iSmX04SO8Tmc-W9_9nxG_7JenaISoMztKrHLX6P-DiRHPA4URkt3qxzN29rjsTlq5d78vmJWYXd8uwNTAf8KbN99_CEUcZpNk9uvx-X5VQ98VmYwg6t3qEV-mON9fk1sUlsKZ99FHUBH4XMWKGuAfljkTsOmvqMaJ1NFlGoRLaKVYEI4aaUEwdffUgpRGGoeS4S76d5kI61Mvm8vEpGMNPzHUduwqT-CqrPW2kUjmeqMscOl1MFZALhP1BeJAHxWb_5KkUS-dMKSvr8qZcz6aGpbSnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ek69igFmuGEtFoVcLuiJfjn2IbJ5VE2HlfgrI8Fi8f5SNbjllqp4kDcMRylGzDutTRjZ7NmcML4sovdAvHlUmLl0SXaNCXbT-0pUnHgZeBQu8GYe_GIfkxSMuBpJ0wGKKUwcMiYXHmguc1MwmXR8yBqGFec22klwNXVVdX_6jzKxDuL-6ZtlOa4rM_ew5ypH9-Ii8MtfXJ35qguYaFr0t8o7p1ZC33qGnE549GF3vJAVtgFtLePXo8saY48ZTLW7H5CamnA_oOJEOUwI9kJEj0ZbuVM84F5Q6hO69gjaQeegYeuUhpNkQDWknbxoueRz-JMHeXY_wrJsfYn0tF0wpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز راجب اینکه چه شکلی می‌تونید کانفیگ اسپوف شخصی بسازید و روی گوشی چه شکلی برای Config-Json می‌تونید اسکن کنید با ترکیب اسکنر من و پروژه‌ی Shin، ویدئو داریم</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/MatinSenPaii/3637" target="_blank">📅 15:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3636">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه
https://github.com/iampedii/whitedns-sub
لینک ساب برای Clash Party & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
@WhiteDNS</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/3636" target="_blank">📅 13:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3635">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">امروز راجب اینکه چه شکلی می‌تونید کانفیگ اسپوف شخصی بسازید و روی گوشی چه شکلی برای Config-Json می‌تونید اسکن کنید با ترکیب اسکنر من و پروژه‌ی Shin، ویدئو داریم</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/3635" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3634">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a4acd74d.mp4?token=ghg9PE7O0T4TAPH0AFrY3k6dSj7iJlq6z1P1WNBt8mBR2oWJzyH29cDPmEwlfyotYGVdHkI_z5wzf-SwmLtxuhbJn0GJXxQB_5BmZGD1FuiKui189Id_Dvd_GNOpHLrIVhai1UjJoWgK54iFVcvDQ8CDaGhg8NriDP39og8P_eqGRK8r-bdmipP3qWJjo6Ix9VCYNQNMAjK8b2Q4gi-HFQqzFHzSAS39Wd8ucoJyL8cc6GiNwfpa-ojnZZkLBJYYBaMNu_Yjdt7gzbBicAFrreUOQlxCZzleCaA6iyMLME_1zJRLGdCtpOc76Zzpy6vN-8GLchEVmxaHm_4aQD3q9RyiuI2Rqd-lhw-NLMbEOy7N8slvcdLX_5gEAkulIgsjUNH0zWgQ-49G5YxRXDhdiHTmuETb3rxazHTLtmVReUlhP9alyp3RXZR6JjHh5g_pVFPjRHm1sSIqRtH6FDp57xt00pJZx9AzZ8HNxiQ8lPOwiRWKza7Nqkj3mA1OAqyNdQ74FUhA9AL5jzTxZ-1eje0nTGAY9M6RqeJfNmavYk2OA5ekFUJeIiO7DiYXQQo1PQcQi49Z0W-hS3hBh_qqXRVkdAb_zRz_cYxVj60djBu-y-HvI8uPdnkRpfHWttAqZQKlxTap7sqhRcyn3fN_IAotXk4YfQNybqFraRVNGcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a4acd74d.mp4?token=ghg9PE7O0T4TAPH0AFrY3k6dSj7iJlq6z1P1WNBt8mBR2oWJzyH29cDPmEwlfyotYGVdHkI_z5wzf-SwmLtxuhbJn0GJXxQB_5BmZGD1FuiKui189Id_Dvd_GNOpHLrIVhai1UjJoWgK54iFVcvDQ8CDaGhg8NriDP39og8P_eqGRK8r-bdmipP3qWJjo6Ix9VCYNQNMAjK8b2Q4gi-HFQqzFHzSAS39Wd8ucoJyL8cc6GiNwfpa-ojnZZkLBJYYBaMNu_Yjdt7gzbBicAFrreUOQlxCZzleCaA6iyMLME_1zJRLGdCtpOc76Zzpy6vN-8GLchEVmxaHm_4aQD3q9RyiuI2Rqd-lhw-NLMbEOy7N8slvcdLX_5gEAkulIgsjUNH0zWgQ-49G5YxRXDhdiHTmuETb3rxazHTLtmVReUlhP9alyp3RXZR6JjHh5g_pVFPjRHm1sSIqRtH6FDp57xt00pJZx9AzZ8HNxiQ8lPOwiRWKza7Nqkj3mA1OAqyNdQ74FUhA9AL5jzTxZ-1eje0nTGAY9M6RqeJfNmavYk2OA5ekFUJeIiO7DiYXQQo1PQcQi49Z0W-hS3hBh_qqXRVkdAb_zRz_cYxVj60djBu-y-HvI8uPdnkRpfHWttAqZQKlxTap7sqhRcyn3fN_IAotXk4YfQNybqFraRVNGcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از دوستان زحمت کشیده یه آموزش ضبط کرده واسه‌ی اسپوف روی موبایل. چک بکنید ببینید موفق می‌شید بسازید یا نه:
https://youtu.be/spTJKgafNV4</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/MatinSenPaii/3634" target="_blank">📅 13:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3633">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O5k7BV_x_-RvMo-chfnHsdj1CP3eUMRf8G6JSDF9HtK9CVFeR0bVwqPcCKif1IRn3_EUMg8KkNCaZWQmTeLgN32X6pdXR-2BnNuGsP0lgHCPpPi0NPhsjw0X09Y1CgpOZh2LkzXhdyVDL7zJX8Cx7JhN1OoV_6Ua_QPrqObcEPtEe6tfWm4QsyT8CeNuBKVD_A4ZmxS8w5ZJEjV8jbT9jPdKDV7q9Gs4meEYWozsMd1XjsEQIaol04d_Z5XHprGgQ54Danzy54gWt0sCcl1Nsfap2CLiHRgqR8HlD-JNno2YwPv9WlWCZH6lQcbzE23sjUVz892N2rOlbClBIlh63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3633" target="_blank">📅 13:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3632">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdJe7SingL_GaZjT8XRrxBV0__cx6EBOozWAyhp7gnzj_T4METUGojR7lp91FOuQDIKYAgB5k-OyKFZNrWfpzjjCQLMlWOAQ-HO1ZkUulVMDBL3DQpOIjlgJp7n3fTCZ6PurR-qdKzOLIqkxonmZK7jYA6c8n6Qyp3NN6KAmuPqWVnHOEo9UueGrsA4K18fuVuD-LaUIt-DmGxhl6xVTm9kq3c3XS4g--vEPDRTRU427sMIOgfdr3qdTF4e2hs_xHnJZj42BldwMs0TlDQm6NSccR5GPyqgwmxwMGCgN9u6GN71hcffYo2lnWsAyRBVX3ah-tHNfHhUP0n_Z9sf0Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی
از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:
اندروید: FlClash
آیفون: Clash Mi
با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.
ما در سرورهای WhiteDNS بخشی از کانفیگ‌ها را بررسی و فیلتر می‌کنیم. سپس اپلیکیشن موبایل به‌صورت خودکار از بین کانفیگ‌های باقی‌مانده، بهترین گزینه‌ها را انتخاب کرده و به آن‌ها متصل می‌شود.
لینک WhiteDNS Sub برای استفاده در این اپلیکیشن‌ها:
https://sub.whitedns.one/sub/mihomo.yaml
لیست سابسکریپشن ما هر ۱ ساعت یک‌بار به‌روزرسانی می‌شود.
دانلود FLClan برای اندروید، مک، لینوکس و ویندوز
https://flclash.cc/en/download
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3632" target="_blank">📅 12:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3631">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">MITM-DomainFronting.json</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/MatinSenPaii/3631" target="_blank">📅 01:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3630">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EYrGk_KrhUPvB2EUyKONkUaXmqWslSQh1WZqvVw_d3JNSCJKbl41crrvrSBLJ_r5BL4P0LOE94K93RCe4SDv4oYM1FWT0VXNo15cpK9dFo1TVe6-Gd5DcApwuxvJKR0LRlm47gWz2f0tiQPlIlVCXj_M5O0UqCBbtMlvUfMOpJ-vSfdQfozwQ9SBJQq3QfRALReui1khuZudnYqTqp1ycj72fpqrLeI3-UYikVXQ9T6IG0K0oCyofBJqnqAhodsx5CveJXEpeHj6NfnOrnXOQRpAY0DeyJTXIt-eIWVut57rgEcgv17wkVcR4CJiitSGF53-hEzBKTMLhF9VlmmVTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا آموزش شکست خورد چیزی که می‌خواستم بهتون یاد بدم فعلا بسته هست و پولم حروم شد
😂
خوبه ساعتیه باز میشه خاموش کرد سعی میکنم اگر راه خوبی پیدا شد مجدد یاد بدم اینم بگم که paqet و gfk کار کردن روش که خب قبلا آموزشش رو دادم(ویدئو سوم و چهارم چنل) به راحتی…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/MatinSenPaii/3630" target="_blank">📅 01:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3629">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3629" target="_blank">📅 01:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3627">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P711hM8ovBzsqnkyhOJW2WTiDeYXmEpn8pvj-3a6h0RD_hd7fHqIMVvu340Q9644r7IsvKpN0I2JJlwg_aE3L1_PQ-XCQpTRGMxvoDbImJLxelz2bxg-C_ljHm1Q6MGuaJpG8v1xUG4Gx_wqMnN3SzcTJUgOUVjp665Vh7-sHfUb_c14x6I_N45sLIMO2wEFBhMmmR-W6SlNy6Jjn5rZc0jsM-um723Ql1CWVvIkrReEUAsYPUfFIFcBjOUoLo-jPIoztrqHELaXcTT8iJmrd135Q4k077qciMmoLYxN3_T-8X1kdki3f0RozEuo4BJedEEX1gbUYROognrJkG8ItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nWtAv48N49FgRijTyvJ8UXUG7aSYJLZWBefsd4uWjIacrCAjX3IL02fTKmhAf0mEFL6s4ibSrJYeIYvab3y4F0gB8DJo-15PgLO71TBcvWH3IeVhgvw3R-yiWLU0U2WuHkzVBiiQHwl4LQ1JtXHIP5MK506qRX3W_8FrA3ton6MByyThQhEiX3eE-vH6pYIq9GAs6w9cO4q_1W4dB1XqwQlmHLnwiMfyRTgFYB6yyAsFYskG63SfczOaXBTaKZWhP871vFnSKlvLiKYksxZaBYlS5DoTpYwh9FPlPTgnM6_33LAE0jbaOtKxKJX2rgDURicR3IgKJUqzb7RxxBqgEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون
بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده آروان سر سرورا اولین بار بود با همچین چیزی مواجه شدم.
و اینکه با سرور فروغش من تونستم به گیتهاب و اینا ریکوئست بزنم نت بین‌الملل داره. نمیدونم از کی وصل شده</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3627" target="_blank">📅 23:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3626">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D5YATdkoVZpiuitpm-z49TRqlhVnMWcQHywXxock7yk9z8rh0TaOWRpyMafWo2EWtjrQmgJ1MAgj111kCMLiaHioTiFgJGYHM7Va5qYgqBS3icdWLPnhrPydqrZH2Yoh-2ZKbug6VpPv-KTodzzvbO5c0DsfnnSnM_VR7hIB3zVy8A_DQv0bgrqArZRdG2OfBRMDMWTgx2NSmi_n0v9YhhcA4WD-_qGHrkVHgIxJdE7dy9IM4f6n4fZzz5dqoH1_xg0YVS45lnGM0bPGmeEOZKA860q_6PlbyJqIxgMeVn15QKMjgd-MGdm9FTqhflaFeEdSNWA8QSO6YZPW-dTbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسرعت‌ترین کانکشنی که میشه از یه سرور خارج داشت، Paqet مستقیم روی سرور ترکیه سه دلاری Yotta
😂
با paqctl
سم ران کردم روی سرور
با آموزش اولیه‌ام
هم روی ویندوز ران کردم</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/3626" target="_blank">📅 19:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3625">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ShadowShare منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...  وبسایت https://shadowsharing.com اندروید https://play.google.com/store/apps/details?id=com.v2cross.shadowshare ایفون https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/MatinSenPaii/3625" target="_blank">📅 17:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3621">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShadowProxy66</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZvwhnB6FFRUO-51TlyPgo36M5CtBRO7hs9TTQt66gewtYV5jm8zFV3xf5YaeUPbArmi8sbYAWZNqmSB8K9VtV73Kjxxvbopb6yr8TCGHYDrmU97RtEix6W1sRM0BCldN6dHstcNswRmVs14xly0tL63Zcij8O_zG_Hfh5Rvo-eUgniwpJOn2WoLcJCrpS6T4hj_VLW4eAo1DjN7XakkJATPOnljp_mtiT6XiheFCJdE-jKh8p25jd24h9jS-MHV3MAfhDnlGee_sVpO41FAhZ7jQbeldNIajYO_2VgNjhlhvwLV4xHfQgP2o3BBG-Gv1oW_I7CJ2zlph1zmVrMamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8XGaAgLXmi66qBqmfunqcaofpywaPpgiLZo0YLzzrveyKylL3y9vtMWYYzm2l6z5DhhdIU9X9m9-49ZUNPI1SJf-T_0NtMMVqtCwhLgDbZIllY2OFnM-yXZEQi50ZvTCwNoBEi7ZCjJT0Qmc2D4ysQB_8McB2K0WZ59a6DUJ7H986t5_koCu147QTfPjz5CLjNpCeKtk8fXZlnzqFnLW3K3UrVxv9PWay9WNBLA98sOYoslaBD0dGr2GZ74ysO6PGXMVKIgkGhx0MbVzWxKbCJ6GLaUCW_RR5FlnAoujNencnHTb-ddA6ltpJ2tufVjB1aZPO9c1aeuTe2jdcGhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IF991h-wmgZ1dNfyPYbQj1XHOcKuRlzkB8n0OtkqpasX6uHeNVqCxLvTtAg8vcYXzZAoZfJb4Fx8A57Vsdm2R1CjAdXJH98_gUORfpiOh46XDM2aBKbEDYGrx44hfLpQD7ytnCBqEThXcXJPjtyRJjN7WbclfKJXdhJ8C9bZ-KdJlY1SSjYjaaeDjwglZv6m7g-eJmO0Of77wlWuzbdsLOlM_23qyj8TUrNahHFZHzsbSOFSBYvspGpy9U0fwelSvK1mnKNdrVjavFCpryBKus5jp-oCo04AY1gG6DUzqF35Ciwcjq6Hn24smWw_oPlc4OYT9ZcsvpPkODnCe1xkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-m64_mtjUVYMMI6JOyxz20kgUOdgLgqnWs2T1zt29viPizFyuELQfnjBUsvHfUwvXqM5TKA1mu6jA3QZnJOSMPmnd8dLzqxE1yOVO5Phh5Ha27fsYM2y4z0UiiKpE3bTSUyCTiLZmidQYQOG7FYB9hTwSmaL3tlQ9pKxv2d58t5JfqirBAm_Qx88cbu3mc5YLyv5YUmIVVmtGBJ2oTpvlFROJ2BAIk44QyIZDonPKiXKPRrJBx0p6u_ZMfopgzEGKbCxc2KcHhQm7U3EyiGPCjoZhhvNerKJbk0elDpIX287sZcQTTzxmWqNXj21zqnZfV4a3WI2N_9Dgi8dEfCjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ShadowShare
منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...
وبسایت
https://shadowsharing.com
اندروید
https://play.google.com/store/apps/details?id=com.v2cross.shadowshare
ایفون
https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده
(توجه داشته باشید کلاینت یا فیلترشکن نیست)
🌐
@ShadowProxy66</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/MatinSenPaii/3621" target="_blank">📅 16:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3620">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V-Q79vqfxAXtQkgUn2eVTWIIxFdO1cOIhJbzWD2tmAJbfQMSfvNJdV-RDf_8Ss7FqQfW37SfjspPCUtEd9vgNDBZn0ocnHI6IuvbhyKYjOK56qGHcw-2fEo1N9yG8pX30x84uvFspzoAa-Zc2NoaXe61tgOfvDpOAm7E-nliYsBqxj_Orul5qdWYDAOzsLhx9Cc0z8tOomYQWyVfniHV6KhHCREQ3OnrRsvp8_2gmaCLV5BDNkrubGmAFvHcdU0cc2zh01gcfUBAMmrzDwkRYC--MgmvGkK_D9biCsEtiLMa603jhK6WZatLHENrE5EVVv7U2ocPiaGBI-E0ZLdDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/MatinSenPaii/3620" target="_blank">📅 12:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3619">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">من الان با این به Spoof وصلم:
{
"LISTEN_HOST": "0.0.0.0",
"LISTEN_PORT": 40443,
"CONNECT_IP": "104.17.89.5",
"CONNECT_PORT": 443,
"FAKE_SNI": "www.speedtest.net"
}
به جای connect ip، میتونید هر آیپی وایت کلودفلری که از اسکنر(
https://t.me/MatinSenPaii/3598
) به دست میارید رو قرار بدید</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/MatinSenPaii/3619" target="_blank">📅 12:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3618">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید: hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/3618" target="_blank">📅 10:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3617">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vJuxf1qOQBF8kgmoLs-kFKpv7CRzUWfcrZ6rEekaxK7cCcdZvQ7VsF3wxgrmrTdZ2CVA5dxmoiW8E5G5kWOSxwkqRpRsltrXy0VkML8HWwbMqrFunyTWht7RSpijqRLjQ2EQg7esN1j6e35JBDhTgO2dVFqP3FZ9ANHUD6selAxwDIWHBhNaw4EJI3jumJkl3BzOleaD-_KfzGJ88W9f3K0BuzXw6dLWIsGfw2Xrt8nVU0NjYrswYQbk1vjf3Oj9vHQi_rOy0NHXgC559su2j9chnPX-ehW9ajvKjAQRaY9imymFypeqeO0-TEQiWHxrCjI2kN-gLaPXv0FmsoDQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید:
hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:444?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:8880?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:1040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:4040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:54040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
این هم لینک سابش:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
این هم کانالشون:
https://t.me/Masir_Sefid
من با همین کانفیگ‌ها توی کالاف پینگ ۶۰ و گنشین پینگ ۱۰۰ دارم و راحت می‌تونم بازی کنم.
کانفیگ هیستریا هم آموزش ساختش روی یوتوب هست، باز اگر لازم بود یه آموزش ضبط می‌‌کنم واستون. اما نیاز به سرور داره</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/MatinSenPaii/3617" target="_blank">📅 10:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3616">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lrl8KModHLTB4__7XbLt1zHWBqTErtyR5TZO7hhyMA46FdFvBIw6v_0CrHrBzBlKwARMhc_y8h1NSm-OK5lMxjFbf8PsVT5z-JHjVwawXWw3qeCd5gxIbU51edq_cYjslz3hgiClpeYx9QhIMmcd1TiNuusr5D8t0A3FBIlGQAO3ejxnqKMkZZvrnTifTmO1n3EFCEpTqrF4ifHXhzaKoMJTHsu617e6m4kUfRAV6VzwxVMyzLz22wIfXBNRp7vL6bXnlbuXNavbKwQyqw6lVPXvbjJqaG2ApkMKrrBG0sLpAiqW-i73FIz4DNfCmhiZsqweNnVBJlaFbaP0dAcz_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/3616" target="_blank">📅 03:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3615">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZzyuMp6MD9WVtWD-zlh2HbabrFUbo8l3WvvHSss8hpz8_SApRORvl5A9ibjr_Wdjdhw9PN7IvQVsykCAheWAkniq7ISw6OdbCHsJW9_io-WMRKtVHUTxVxHxeoh4tD1dsEMlG8ab8ck4wrhWPhirOyktrp_qottOrTKTjG0XDOVIdA04NvYYamcNlCseIB_xu8W6oRgwshxhsMRGUerMuhUSyAjb9xeX4LZW2YxCIeDLoijxdEw8BeM9w2pk-p66ZvUp0l_GpZELNlV0t980O-UIY8R-BWybvTq9N912GhgwN3OBryzx2AMRQ9lS9c1Qm6--uZ1cF8lfHLZ6gLnPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کانفیگ کاستوم دارید(ساب نرمال)، آیپی تمیز رو باید اینجا جای address قرار بدید</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/MatinSenPaii/3615" target="_blank">📅 02:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3614">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑇𝑎ℎ𝑎</strong></div>
<div class="tg-text">https://t.me/MatinSenPaii/3613
خوبیش اینه با این روش میشه رفت و کانفیگ BPB ساخت
برا دوستانی که کلودفلر براشون بالا نمیاد یا نمیتونن وارد سایت اتومیک میل بشن
همه چیز با همین نت بدون نیاز به فیلترشکن کامل انجام میشه
بینظیرید شما
نخبه های ایران.</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3614" target="_blank">📅 02:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3613">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting.json</div>
  <div class="tg-doc-extra">9.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3613" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://up.theazizi…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/MatinSenPaii/3613" target="_blank">📅 01:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3612">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rQK5DBmsQqwUqMSLuGdVIj1j9InhO4ZWPzRCQJCk0yXs0PTFsKl8-cycfzN8kRULfrtYEx4N2rW8tmJiyUH_ZuK8fj-Uu7EXUyS2o4gz3qI5OltMc9dLNarDxoUehnmPuCxbpQLAuhVXTZ7JFJDAaO9yYfMzVQfDBEueC3yXi4nQC3nDY_3_7AhsVhMzFYoMR17wVlZEfjIF0QS6tAqmPa659CC8u0kulRCqoyT8IyxJOujaDgp2MVPCV8nyBY-GXKeVdvnizuum4W7eCdA-6w6x_5RsktI9ZOn2CHXO3S5tblNgLwplJwS-OGhKbQX2NJ7nQEl9f_qH7doCOjnSVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیستریا هم روی اینترنت من باز شد</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3612" target="_blank">📅 01:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3611">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mr Lou _ Ey Iran | مستر لو _ ای ایران (Rock Mr Lou Version)</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/MatinSenPaii/3611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/MatinSenPaii/3611" target="_blank">📅 00:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3610">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دوستان اگر از Undefined در نمیاد،
1- صفحه رو رفرش کنید
2- حداقل نیم ساعت صبر کنید
3- اگر نشد، پروژه‌ی Worker جدید بسازید و دوباره مراحل رو انجام بدید</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/MatinSenPaii/3610" target="_blank">📅 00:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3609">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3609" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3608">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/MatinSenPaii/3608" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3607">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/3607" target="_blank">📅 23:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3606">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ox4-TqrbY1plwdxBb9Hg9MQ6BiH_jAwi8lc0oeyQIbySC2zdq72c91zxvMgcPPayoB9HiCqejSSKcSbxEmBRxpwbD9oLs2EZ0mKa52Nr_jNfkUu0P_lQ8yiOam5pmTnMtjkfr84GAbmeu9t-vMGncUCYwo8SAxAY7wMPyWcgdJkgTdfrA1-yqDN9j2nZ4aO_J0wKTprFtuXal_qBxLDLRObrPuqCFSZNXJnX6vk1t71wOGLX05L0ZPtg8RvA-JGpJ910OEL_j9YkiWkYOaQdGf_x_PJuqDz-glcBxWoLpGWcrziHaPWn_fcECMtH31djYQNDiE97OvgOlupejM--yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای SNI Spoofing
SNI =
www.speedtest.net
IP =
104.17.148.22
✍️
Kharabam</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/MatinSenPaii/3606" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3605">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/MatinSenPaii/3605" target="_blank">📅 22:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3598">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3598" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ورژن 0.5.0 اسکنر
راهنمای نسخه ها</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/MatinSenPaii/3598" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3597">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 96K · <a href="https://t.me/MatinSenPaii/3597" target="_blank">📅 21:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3596">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.  https://github.com/MatinSenPai/SenPaiScanner/…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/MatinSenPaii/3596" target="_blank">📅 19:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3595">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.5.0</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/MatinSenPaii/3595" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3594">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZzUeQyHoTVN6m6tZyFtxSz22A2hMdThXdAtgyz4DF7iOlGspEIW4_eAWj4ZSG9X9fKWeambqucb2q5p2VlhKhG1lq8EhN9Mjx70PlI8TYciWBFDHWKiMXQ9UL1H3uceKeVVS5paecPWH07vMBFd9hKFGw9Qxkpsdhm8YPAtwIBBoIDu2o-mjxxMZlg-ahOPYvpkgnmbOBTTswGFXlGwubCxXcvvvrqtWhWZ4GE9Oa1k1D0PFe6RV7h-KO1s58-CJk5rw3mlXbzodz2qVgmvo14GFtSRLSFCRysCNibdqjIZ0AW_-yR0snkASYPVVLZE1jdtrntGveCp_gNH2inq4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51K · <a href="https://t.me/MatinSenPaii/3594" target="_blank">📅 17:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3592">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اینترنت دیتاسنترها هم برگشت بالاخره؟</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3592" target="_blank">📅 17:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3591">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏دوستان می‌دونستید که این روشن/خاموش شدن Wifi ویندوزتون باگ نیست؟! به‌خاطر فیلترینگ شدید فایروال‌های ایرانه
🤦🏻‍♀️
دلیل و راه‌حلش:
تست اتصال مایکروسافت (NCSI) که فیچر ویندوز ۱۰ به بعده بلاک می‌شه؛ به زبان ساده، به‌خاطر فیلترینگ، ویندوز فکر می‌کنه اینترنت قطع شده و برای همین هی وای‌فای رو خاموش/روشن می‌کنه تا اتصال برقرار شه.
راه غیرفعال کردنش:
۱. همزمان کلید Windows + R رو فشار بده (کلید ویندوز همون لوگو ویندوز روی کیبورد)
۲. توی کادر Run که باز شد، بنویس regedit و اینتر رو بزن.
۳. برو این مسیر:
HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\NlaSvc\\Parameters\\Internet
۴. روی EnableActiveProbing دابل‌کلیک و بعدش Value رو ۰ کن.
۵. سیستم رو ری‌استارت کن و تمام.
دیگه این فیچر غیرفعال می‌شه و VPNتون قطع نمی‌شه :(
البته تا وقتی که غیرفعاله حتی اگه اینترنت قطع باشه، همیشه «Connected» نشون می‌ده.
✍️
گیک‌زهرا</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/MatinSenPaii/3591" target="_blank">📅 16:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3590">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PlkbXKiHgygnNbCqXoBZvPyVJe1fjTxcGfy7WPq16kowg0N6bapkmBfzCKfryzHSsdpLfXhGmA209KqR5fZmMLIY0Iloob9UX8CnNxmTEwKsjbsbejHd8tRNM8fET0ljzg4yuiGAY6Z5VaS2jTHDrrNJKWkVuHLP5VwRFzLv-yC36xkUUghwFN2EH7zORRMiL4JkBn_HjGXeZjvj0Wr4S6w4UpSbtnpAJrHzQhRvJGrWkUtZJuPj1s350H5r_wFNUKmlVYf21Xe16FL9-_9p1_uwRRS7e2MQkG415LXWD2xQT4_rZQornTeiUhh-cf4WfnQG42dWlUPtAjURHpSwpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه به این علت باید حتما اسکنر رو توی لیست سفید آنتی ویروس قرار بدید. ویندوز دقیقا این بلا رو سر BPB Wizard هم آورده بود یادمه</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/MatinSenPaii/3590" target="_blank">📅 10:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3589">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">متشکرم از دوتا دوست عزیزی که 105 و 3 دلار دونیت کردن. من تازه ولت رو چک کردم
❤️
مقدارش مهم نیست. کم یا زیادش یه اندازه ارزشمنده و کمک بسیار بزرگیه به من. ازتون ممنونم</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/MatinSenPaii/3589" target="_blank">📅 09:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3588">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/MatinSenPaii/3588" target="_blank">📅 09:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3587">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/3587" target="_blank">📅 07:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3586">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X5SmVj91uTD1bojD9h17sfKnM07RueuDaiemWtW5Wwy5bfodBTjN3yAmbX27C7hFH9XxHdjfxCtcIvyNRJr1RXqJD-ITz74m6wEEs5UnMYwUYtt9dHaTaf2l4R8rYfUflLzbmZhDJ2zTx0CHaXhwwuT5MaSsf0p3N-jnQIgD3zttWskR1UCJZZGSt-PgcnyU0wr3b3hzD16f64agopVLW53ntUyLDkuYrzAlnvgM6qFQz9eznXL9WnMxf7ZS_-5SLl4rfnHXusJA-i44DxGzzaGTRlR2P1xukk7UoPZ8EmlcHcX6sS5vuwQOH6JtEtizp9EAhyqpeiAcNwenMukXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/MatinSenPaii/3586" target="_blank">📅 07:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3585">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ozoi2f563uAGKOWcrkrGn8MznU-dKkj6mhhxP5Nk5WDLOKdhvFmhk8C4ycyIc8QPmyS-JEQgpWnTvsJK977HAc5GRiUA2yGsxDLXQYKfIdB4Dbkhntd21ctPrqeiXurko1nx_NNWxfB-GVNBFLy6dNv1NLb64jjm9CoUeSzFnM6cXgqqxntaSQgUBbbm3nCP3kYWAji9aZ2ln61bKf4lHehXLGMN2wIZfoKw9vf_bEEaZhfbvcpT8rztHR-jgahc1IcS78Jh-MrYH4VFWZXQQN1L-pPAkbIfelcwMKP802Zgua34cRdHfeyHUENrRKeYgNcZFCxkNCI93h_Jwz6bnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار که عملکرد اوکی شد بالاخره. چندتا دیگه از دوستان هم گفتن
نسخه‌ی اندروید و دارای ui درست و حسابی به احتمال زیاد منتشر نمیکنم چون خیلی درگیری و کار و درس دارم، اما سعی میکنم روش کار کنم با contributerها. فعلا تمرکز روی درست بودن عملکرد بود که حل شد
برای همین prهای فعلی هم reject میشن همه. تا ببینم تست چطور بوده تا به اینجا</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/MatinSenPaii/3585" target="_blank">📅 07:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3578">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3578" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V0.4.0</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/MatinSenPaii/3578" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3577">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e1RXtU-J_QyBpBNwIK8h85SAaHyyo2kK4iVxiRauFRe8TfTugjFKL-meyrgb08O4bgVbNEyi5Nd0QvdSQBkmzHr0BBPn8ySB0fXNrbs5DVZCEBvlpHT9h7LDufPtMRHk381YO_BvU3DzM-W-HmccGR0-_yqzvZ8I3OUno-yox8NWpHGLAUP_xyB1Cfy567MJc3wjE0UrhwLYF3R8RE47hpVIrB3Dwz3b1VDhkKfcoCu4v5oKKI4E1D_AmeGPIc7URUZeWbhzkvmQ2kdtvrcOMHfszca-boEoQ7b6DPAdjnUTb1W40E5M-ya0AlfK4oD38j5H6R5ZmtoJz3qw3v1Ngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب، فکر کنم یک بار برای همیشه مشکل آیپی تمیز فیک حل شد.
و ممنون میشم تست کنید و بازخوردتون رو بگید. تا اگر مشکلی داره برطرف بشه و بره برای ریلیز</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/3577" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3576">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ihyQU9glZl0snaV47d7_wFoENj7x9Yx5X8DqZ6ImOyj4H0SeY1uK9Tfm5djZlljpSGZNAjOwYTw-TAxfYCl55yPcCsRYhFBuKD-7uIMdzGmTd2c83VWdO-Nzf1qIs7ptOsKRDnFJdGahePWEokiccph4Hf0jRAsbNCv-tmW1124acSIquPlMTpB6XI4yK-X-f36wIQoLLOEfwUhPW5y91l2BZb-w56hQYvbl1sLdWER_NaAibzqDy4yZ3rrL6LM4Q2Mz_WlB_RPaRtFLytmhnjU3WJLLM9a89lkIYINCSbELz3aZTMi2DmxrXxcYujXi-GoMWBKyWxszcPnNGmNbmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها گویا روی یه متد جدید کار میکنه که به راحتی می‌تونه فیلترینگ الان رو با یه استراتژی جدید دور بزنه.
منتظریم ببینیم تصمیمش این میشه که الآن منتشر کنه، یا بعدا</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3576" target="_blank">📅 04:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3575">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان، اگر پیامتون توی دایرکت سین میشه به این معنی نیست که من دیدم و جواب ندادم
🙏
من میزنم بیاد پایین، همه سین میشه
روزانه بالای ۶۰۰-۷۰۰ تا پیام هست و من نمیرسم متأسفانه جواب همه رو بدم</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3575" target="_blank">📅 03:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3574">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YPW8AEFkHHo4XAj2vSY3B7AHAkcDbYBEvMYiSvX2ukfofOuBvJtIJfOFZKRhGoFgWP4WBR3kVjVpivK1v1GXxaf0IVEUKHWhgJTQQ3Q_thEKXFoQYmq80cuIy6VIs7Onyj4Gswc-6n1aK_TqB9xE_7v-rOMKKNWRVVbfoYClJOHKb0FMBvxluvQmVBgpHgfmElQa8a6qh-5hR5SG8BSb2RTE2oubWWxyirqIhsSsil2WQmn5qbkDKDkQsUl6wlvNLrcv62qHU9mkO796Pal_2Cb8D9qTBjm7UbxKkyHsD5Sj0IxrWHKZUeEWXBhCunsoAxta2NXdmPRX-ODXXip8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک 20 دلاری Cursor اصلا نمی‌ارزید. خیلی خیلی خیلی زود تموم شد با اینکه از مدل‌هایی مثل Opus هم استفاده نکردم
اکثرا gpt 5.3 بود یه کم هم Sonnet
افتضاح زود تموم شدش</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/MatinSenPaii/3574" target="_blank">📅 03:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3573">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مشغول حل کردن مشکل رو اعصاب آیپی healthy فیک هستم. خدا رو شکر یه سیمکارت پیدا کردم که روش دقیقا همین مشکل رو داره</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/MatinSenPaii/3573" target="_blank">📅 03:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3572">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R8LAvD8FW3sBfUQVewVsbwTsKzR7fEJyYVKHp1qIuL8hLiU5cNne8_9asEP99IPNWzwGTg6SUgs8tnkCtbYazPJkgVf3MkViaMJieUPcEf10O65UeLOmcqSd4_Lw2rRScti4W6Su7D7EzSR9e933YEelEo_oNdagk_XOfouvxA0vW0TVYEyUZee47ESi4-fqdC_J7TSiPI95E92VzreIEUPAJXosp31FjZLrhqIQg0sxHFOTU12hTsy0Js0Lep26LUJXYUv1RJwSAP-M5aD7kkzY7TelwIpozweGeJusulkXo1X0J4S7TjyPB4T6EknLE6W14azAajbfU4nmh5Dbtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی یه اینترنت عادی هم این شکلیه نسبت. یعنی تعداد آیپی‌های سالم کمه و همین هم شانسیه چون range ها به صورت رندوم انتخاب میشن. حداقل 200 هزارتا اسکن کنید</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/MatinSenPaii/3572" target="_blank">📅 20:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3571">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">V4-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/MatinSenPaii/3571" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3570">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اسکنر همچنان مشکل داره متاسفانه روی اینترنت‌های دارای اختلال. دارم روش کار می‌کنم</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/MatinSenPaii/3570" target="_blank">📅 20:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3569">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V4-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3569" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V3-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/MatinSenPaii/3569" target="_blank">📅 20:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3568">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ورژن 3 منتشر شد https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/MatinSenPaii/3568" target="_blank">📅 19:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3567">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اگر اکانت جدید می‌خواید بسازید، از BPB استفاده نکنید فعلا. با این آموزش، edge tunnel بسازید:
https://www.youtube.com/watch?v=svYBcv4bSzo&t=618s</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/MatinSenPaii/3567" target="_blank">📅 19:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3566">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ورژن 3 منتشر شد
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3566" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3565">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ojkTr_w2uWK8Cm8gZP07p-n0iReqU2uoVge_YItrCNEOFeiIbSEM_TjafHUGeDWlXv147oTtXPZr_94lRLpay1DL85eQm6JqhlRgtxDctScNGjjGYX94_B9qXbq43drDk6vXvooIa38fQTHN96OJpSTN27iZnNxaREeQGT1JQYUVL54eFPH45MHFDWAL4_raXcT39AnlfnH4lgIIEsbfkiMcmux0fjfr6BIsau2c7vXFWkmeYOF-ozqMGs6HaVL-wh00ZxXwAbKFPU9cz7XKJG3JofvV_uxjz03EbR1fD4_-uOvFmS-Fqva3xvJ4DaFa3N8RlRa5oE8KVHV9nn1_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/MatinSenPaii/3565" target="_blank">📅 19:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3564">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/MatinSenPaii/3564" target="_blank">📅 18:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3563">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F64B7VEYMNSQGPwdlqHD-DI80WDGRRzivVpCR5_HR0a8x-C0sZ_sEW6-ay8-66JpMIzYPrxai88_6-ZjcraM3lL0abhtIalFJ-TkjZtIdCMQje_8DYe1vqnfnWGV_BFvYf9B_5KGgKhxC4kwE_1AHBuKsNz4u7HsZmoWoRS6ZiLDnyUWV_Nt4IUS0NCbBqjB64yl_O-vNRzSieS-TfZ2Bw_fO-TmB3uMK4R3eX7XFSK5UfV2GEPRnyZNSNOEpxxPudsBcGtZvMRy8dHkU-wP0gG416DwuCtSvjNKVDhvt7XscAHk4ZnGUD0oKZXmq81_CVZ_cwafmYY9949mtEDUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">BPB - Edge - VahidFarid
فقط Edge داره کار میکنه. هر سه هم روی یک اکانت</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/MatinSenPaii/3563" target="_blank">📅 17:45 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
