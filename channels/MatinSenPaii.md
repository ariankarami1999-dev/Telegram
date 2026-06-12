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
<img src="https://cdn1.telesco.pe/file/OoMsmD8IkY9p2q8rCWElSPq2zJV0Ua8Fhb3erlNPtyoTOLxGkuig4kq_FpPb_dzvCJWOaMVcOp5B5U5ha5oxaBNE_Gwc-ILYStZvY13UX2jEmzKethBIPlgUFQeP_cjxgsNtKcFi1uMo2CHlmw1tWB4vDI-L28ZvmRvvvrvyuM3M8s-_EwZzqWHPkXuE_WjEdw1doGme5cq8__3oJZpTnYCIkKz7sIn0PTNVttmuMZlHwJgSp9BIFFUsw4894I9R8BFK-BXZCQsKw5AfjUc1OrIODRny8vXyUCP7UJsMo8O_IIujy_i9WS12_Y8rqywkUz0wibnRPzUeHOe-rLPr0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 163K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 09:56:29</div>
<hr>

<div class="tg-post" id="msg-3814">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q7ejXXJ8B5Nucn-NTLazRkXeco3dTkWpz1sQ09fCPbnzvF2YYIIe4rnSTD2UW0ppc3AROpnc8nX5NCKTFjPANSAfhk0TubczFGC8IO9BsuSYvKdnfW7AvBZfoVggkwul-YeJVY-JV5KxjGsvCvSs6g9S_ekHYZ1Z7Ken4AjgcXKr1vYNIaRclHG2E_tewS8wmpPglt_F8MrdL_wOF5QFIJgP92niZfywmZhX9TfAn8KzNLVALjbA3n--19d4LYbzlY29mt75T9Ur8nqrq48avVXIHOYxRvSoumanKrFbyQJtrTIT7yi8xcfn52lPl6e8zl2TkVLhId6I6ngDmXX26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!
همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.
بعد از چند دور summarize کردن، نهایتا بخشی از دیتای مهم از بین میره و تسک به صورت کامل انجام نمیشه! پس اومدیم یک سری تکنیک پیاده کردیم مثل تقسیم کار بین sub-agentها تا از پر شدن سریع کانتکس اصلی جلوگیری کنیم.
بعد این ایده مطرح شد که بیایم هدف نهایی (PRD) رو تعریف کنیم و اون رو به تعداد زیادی sub-task تقسیم کنیم، بعد مدل رو در یک loop بندازیم که با هر بار اجرا، یک context و یک prompt جدید داشته باشه و بعد از هر iteration چک کنیم که تسک به صورت کامل انجام شده، و در غیر اینصورت چرخه رو دوباره تکرار کنیم!
در واقع به جای اینکه برای اتمام تسک به مدل اعتماد کنیم، ما در یک لایه بالاتر این رو validate میکنیم و اجینتِ تنبل رو harness می‌کنیم :))
✍️
Amir</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/MatinSenPaii/3814" target="_blank">📅 09:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3813">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/brsXq3Ogmx5xy_dSQpjhEuO6ugzS4L20eQ3-n4scYgjtk1zVcKgx1kDfje4rABC-WjhEYB7PTkIoolwZeRFhw2cxbupBXrOf-__iwyUTv2pgV8TCSE18QJFhrxdi7vPcODjToOJnS32IM2LT9rx5Tz6e1Lrpz8GOZfy091sm-mkcmuqNRw8ipKp26C1KIB570iTN2n-5k3ESW839VSNiRAsjEpfJJUV80LyPPldNSB3aCv5A2khNDe1Bl8Z2RkICdUi4DHL2oGtYvrGl8lUxtbgglI2n1dgRhYOo6p63L5fArQipZX8jXLI0b_nYoAhd091-Mv3fFPwyQvBvDrSrrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله شما می‌تونید دامنه و سرور خارج رو از سایت‌های ایرانی هم بخرید، اما چندتا نکته وجود داره:
۱- احراز هویت سایت‌های ایرانی کلا جالب نیست و خب این ریسک رو باید در نظر داشته باشید
۲- توی شرایط قطعی، فروش دامنه و سرور همه‌ی این سایت‌ها میره روی هوا
۳- شاید عجیب باشه شما اگر از سایت‌هایی مثل netlen و با کریپتو خرید کنی دامین+سرور رو، شاید ۸۰۰ هزار تومن(با کارمزد و همه‌چیش) پات بیفته. اما همین دوتا رو از سایت ایرانی بخری زیر 1 تومن نیست</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/MatinSenPaii/3813" target="_blank">📅 07:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3811">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نکات استفاده</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/3811" target="_blank">📅 01:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3809">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C9HrTyqBRLFSiGzxxuC1xyOppE0ZXlW3MFpGXbmNLmH-u4p5Xpdfph10cULF6uGiONNccPfO3X02r-2b1W2O7-R1RvhtmLo6R2Or1v1eELvhQ_ZokaWY92nAow-BCcy8Yk3MirdDdn3qHx7KuEVe_Rd5iV_7TlYUdW3X9mS2NZBnUS0kv1gFRRad1GtKdXlZ2J8J4AlUj_VVu6mm1qt8KnCqLZKN5eCESIyIWAzzAU3NZGBfsh-Yqz-TBPmx5Z8qFhqfmwyH8ngCwiYWucruqnKku6cxX0vDDA_2dM6ZWIVTXbQLpZFQZBvD3VCYVOpBHxBuT_SOC7n7pjJMiujmew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran  * دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)  ///  * حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)  * کافی است لینک subscription را وارد…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/3809" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3808">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/3808" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3807">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/THYShmWLkC_WA1McNUABVgV3y07PvVHJFaoaOPgqQzPKi8ol3SGJs-jgDDTkdukDwEJA9FCzLkKiAZh08zB63jZJrO7lwnn0j3yv9GjAsV0ZDo0s6dpVq1FSZHK3r5J_9YlEU5AZo4sV4qtTobllyHEwRoYca6sJ00_VQ8uyD6DVfYsppG4HMfCivOvbR33QhLz9T34ZhNbna8TEs2YxRgbxRNFIzugIbaMoDq4PGPFiLQ7HphV2CILmp4e4o6qCLCzV6oUL5WAqcXfYzoHmi9Q_ga9PeRuBqweZmEhu8Tvpdn4ESzYtmgYENMY2Eawgnk20W4CcJ9eDKlWSbo0ekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از http://Netlen.com.tr بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰ باز هم خود دانید</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/3807" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3806">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">درود به همه رفقا
🍷
اگر از پنل bpb و... استفاده میکنید میخواید ip ثابت باشه ولی جز لوکیشن آلمان
🇩🇪
میتونید از ابزار زیر استفاده کنید برای ip های مختلف برای مثال:
میتونید از ip چین استفاده کنید برای دور زدن تبلیغات یا از ip آمریکا برای بیشتر هوش مصنوعی ها خلاصه این ابزار مشابه واسه خود bpb برای ثابت کردن ip هست ولی با لوکیشن بیشتر
❗️
لینک پروژه:
✅
https://smart-ip-scanner.10-354.workers.dev/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/3806" target="_blank">📅 22:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3805">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید  محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان»…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/3805" target="_blank">📅 22:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3804">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X-poJRLrGzPgn2aBB-svYL1__mpM7cxqc3KMg9xE2fpOT0gIkAnmKz7axcKFDYVcmmTVvlSizKuJQIvZkRRuyjfK6cpftDB7UCtxDjvkQrF-d31shw2a7LavCwQQ4vqJna-wYX-KcdduF0kXUpabgackr6pz5ZP4xg_-mB3Kij45xoF737JslNifjB8ADAdsXpZxCs5Sq6F6mrJWdVvbLwxuVanYC9GZFd6buwoVHjjoSp9-tLcz60rU5FM--HM09JoGMIkFxU-32_Bt0_3TYlI9XmDtAlbzpiLDSc2SRFScRkPU0Lex54d8OGdyJVW1rSrXbM4M1Caa5bSV7YYdVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید
محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان» (X-VPN) است که برای نصب بدافزاری به نام STX RAT روی سیستم قربانیان استفاده شده است. این بدافزار می‌تواند رمزهای ذخیره‌شده، نشست‌های فعال و اطلاعات سیستم را سرقت کند و به مهاجم امکان اجرای دستور از راه دور بدهد.
در این حمله سرویس ایکس وی‌پی‌ان هک نشده و کانال‌های رسمی دانلود این برنامه سالم هستند. خطر اصلی متوجه کاربرانی است که نسخه آلوده را از منابع غیررسمی (در این مورد، یک مخزن ناشناس در سرویس Bitbucket) دانلود کرده‌اند. در پاسخ به این تهدید، ایکس وی‌پی‌ان به‌سرعت آپدیت نسخه ۷۷.۵.۳ ویندوز را با کنترل‌های سخت‌گیرانه‌تر منتشر کرد.
➕
نوشدارو پلاس: این هشدار مشخصاً به نسخه ویندوز X-VPN مربوط است، آن هم زمانی که کاربر نسخه جعلی و دست‌کاری‌شده را از منابع غیررسمی دانلود کرده باشد. طبق اعلام X-VPN، نسخه‌های رسمی دریافت‌شده از وب‌سایت X-VPN یا Microsoft Store تحت تأثیر این سناریو نیستند.
▪️
روش زیرکانه هکرها برای اجرای حمله
این کمپین ابتدا با نسخه‌های جعلی برنامه‌هایی مانند «بایننس» (Binance)، «بای‌بیت» (Bybit)، متاتریدر ۵ (MetaTrader 5) و کیف پول اکسودوس (Exodus)، معامله‌گران را هدف قرار داد. آن‌ها حتی به سراغ پلتفرم بازی استیم نیز رفتند و در نهایت تمرکز خود را روی کاربرانی گذاشتند که از ابزار تغییر آی‌پی ایکس وی‌پی‌ان برای حفظ حریم خصوصی بهره می‌برند.
💡
نکته: بد نیست بدانید شرکت Kaspersky (کسپرسکی) پیش‌تر متوجه شده بود که همین بدافزار با نفوذ به سایت CPUID، بیش از ۱۵۰ قربانی را در صنایع و کشورهای مختلف آلوده کرده بود.
بر اساس یافته‌های شرکت سایدرز، مهاجمان در فایل نصبی اپ‌های معتبر یک فایل مخرب به نام CRYPTBASE.dll جاسازی می‌کنند؛ تکنیکی که به آن «بارگذاری جانبی» (DLL Sideloading) می‌گویند.
به دلیل ساختار سیستم‌عامل ویندوز، فرایند نصب برنامه در ظاهر کاملاً عادی پیش می‌رود، اما فایل پنهان‌شده، بدافزار را مستقیماً به حافظه دستگاه تزریق می‌کند تا آنتی‌ویروس‌ها متوجه ردپای آن نشوند. پس از فعال‌سازی، بدافزار می‌تواند ارتباطات خود را در قالب ترافیک عادی و قفل‌گذاری‌شده وب پنهان سازد.
▪️
چطور قربانی برنامه‌های جعلی نشویم؟
دفاع در برابر این نوع حملات بسیار ساده است و نیازی به دانش فنی ندارد:
• دانلود از منابع رسمی: برنامه‌ها را فقط از وب‌سایت اصلی شرکت یا فروشگاه‌های رسمی دانلود کنید. این هشدار برای ما کاربران ایرانی که اغلب ناچار به دانلود از منابع واسطه هستیم، اهمیتی دوچندان دارد.
• تایپ مستقیم آدرس: برای جلوگیری از ورود به سایت‌های مشابه و جعلی، آدرس را مستقیم تایپ کنید و روی تبلیغات کلیک نکنید.
• استفاده از نرم‌افزارهای امنیتی: داشتن یک آنتی‌ویروس قدرتمند و به‌روز در کنار رعایت اصول دانلود امن، لایه محافظتی محکمی ایجاد می‌کند.
اگر گمان می‌کنید نسخه جعلی را نصب کرده‌اید، فرض را بر لو رفتن اطلاعاتتان بگذارید. فوراً رمزهای عبور خود را از یک دستگاه امن تغییر دهید، از حساب‌ها خارج شده و احراز هویت دومرحله‌ای را فعال کنید.
✍️
یونس مرادی(نوشدارو)</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/3804" target="_blank">📅 21:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3803">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ntyPk9pbDsCTyM_o_cH6F8YnzzkyX3t_uwee2_ATNFlIA3c2nIdwWAQ8v_BCXesHpszgwWA8YUyZZFY_f1UoVMW_T3n5Ql_Q6KrkQ4Ip8a4uI_Xb9BUsDGqNbUQBm-stQeJ0n8nJLi-9EGLEHWwS7tNWsmBrjE6cDxXTLrdQ8wmUVvcDS-kS5FQ04pfhAFS-iTHLgpfzdrVJCEuWwG-Y0DRia7-k7FKNF4B3R74BMzGdDbTrodLJjsOvQxBGWMPSQvMA-YUY6FOhSgl72JJeMAp8dc9gYzmVKnypX4bbfOg6f9qQM9OuiEHz1iDan3nI07DsIQdoeznKonPhO0yPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏یه نکته‌ی جالب از کنفرانس WWDC اپل!
توی ویدیو هر بار که کلمه سیری گفته می‌شد فرکانس‌های ۳، ۴، ۵ و ۶ کیلوهرتز صدا رو کات می‌کردن. چرا؟
برای اینکه وقتی دارید ویدیو رو می‌بینید، سیری توی دیوایس‌های اطراف شما بی‌دلیل بیدار نشه.
✍️
Behrad Javed
منبع</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/3803" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3802">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اگر از
http://Netlen.com.tr
بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار
یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰
باز هم خود دانید</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3802" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3801">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ببینید واقعا درک می‌کنم که ۶ دلار هزینه سرور و دامنه براتون زیاده، اما اگر سه چهار نفر با هم بگیرید بهتون فشار نمیاد. همه هم می‌تونید استفاده کنید
برای من سود و ضرری نداره صرفا می‌خوام بدونید که با نفری ۱۵۰-۲۰۰ میتونید راهش بندازید</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/3801" target="_blank">📅 19:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3800">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-poll">
<h4>📊 میتونم بپرسم چرا هنوز راه ننداختین؟</h4>
<ul>
<li>✓ هزینش زیاد بود واسم</li>
<li>✓ آموزش پیچیده بود واسم</li>
<li>✓ حوصله‌ام نشد و بعد از قطعی مغزم نیاز به استراحت داشت</li>
</ul>
</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/3800" target="_blank">📅 18:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3799">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اینطور که من می‌بینم، قطعی در پیش داریم به زودی</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/3799" target="_blank">📅 17:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3798">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تمام آموزش‌های مبنی بر اینترنت آزاد که من توی کانال یوتوبم منتشر کردم به علاوه‌ی توضیحات و اینکه توی چه شرایطی به چه دردی می‌خورن. از بالا به پایین، برای شرایط سخت‌تر معرفی می‌شن تا شرایط خاموشی کامل:  1- متد Paqet، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3798" target="_blank">📅 17:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3797">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اینطور که من می‌بینم، قطعی در پیش داریم به زودی</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/3797" target="_blank">📅 17:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3796">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-poll">
<h4>📊 آیا سرور MasterDNS راه انداختید برای خودتون و خانوادتون؟</h4>
<ul>
<li>✓ آری👍</li>
<li>✓ خیر👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3796" target="_blank">📅 17:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3794">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">هرچی کانفیگ مرده بود با این تنظیمات واسم زنده شد. توضیحاتش رو هم میدم خدمتتون که هر کدوم چیه و Mux رو خاموش بذارید</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/3794" target="_blank">📅 16:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3793">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uaDBf9u6uAdLPeOZXs2yz56yJEyi2LNCZhRDAgUnyU01FHqOEKfvKB5e1EZwZqkp75PfVXtpdQ9nXJ1uv7R_4ggWalSVnnG3MVHlKPrV2gy0EgRcbYx3X38XaGJZ5UlimzzxH-hpw116mB3safwspqWFtOMB9OWh3B1HFir6_6_nWKg4pe1fBHJ4ABkXPQWlzc8rRvU9f0IAELZPO50U8W2pyiW7P9E_yR52j97P3XI1QeoKrpZDKy5Zcc2RcSMD56T4AZTg6YadV0BRBR0tdJxav1pyKLZ--0mVm17LrEGugHkA1-nb2WwhKK-S69BP3lfkrw2A-c8O5Vuubs5H5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی کانفیگ مرده بود با این تنظیمات واسم زنده شد.
توضیحاتش رو هم میدم خدمتتون که هر کدوم چیه
و Mux رو خاموش بذارید</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/3793" target="_blank">📅 15:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3789">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pQggdNXWPaVClXNyuiPcV4-2U5QzJJX9dm5EO-9HHJNT_56HR2le24JNHzMGm7dvUaw0Xfqe9_essO2kMzigphmFYc92qa92xcJmOg059mhO0VJR5G0dE7cMJp24LrPhuhAxcRXcgrO3-LQfX11zU-MUf2dvpsuZ1YeaZnKIml8pA_wKxn-MqHqHm00UuVoOGf5NwgsoA5OumAH_AmRT7yqlofhvKpxMbBI0Ycp5MZsaDlfCFGadeaWq6wUQkVjsHYRVq9grvBVqenc4WFODQWbd_oUmFvsVWx0cULUZSiw_kSx85O8qHr5JSP5EsfLWGhC-QLOe0PvjYPr0qJi-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PPFGIfD3_D432a2iM7gKQ8zsB3_DpRQaXp7Iol89EjpJDStRfG3zelKFLsV9LhvAsOvwCv2q3aaLhw-__zzsc1TW5BafK9kE1cOORQqQ-z9uGLuJJ7cNaDhzS5CAc8fsbRf1gstnxiaH7XLnf8QQkmvXa5m8T-E-5Uh2i4b0lKgg0B_X_1mT-n8orbLI0h76Y5-FrJ1r_fpLJDmJGFR_rHr-rftjTBylICiZACQt7SD7eSQco67TOmLnOO7kN16XxW_S8xSYFoDgR1vNkWOnh5w29H9vxfmxRhLimksEvXLqc1X1zJ_On5MOz8p4m27Qj6ViJtUjenHYT1lEjo4iOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MGRPB5IR0M_tFyeVo_bXzSt4CkHZOurjxwyApsapxeEdK1a9ervNGTie-T9uU1q2IUB6D7Wtmj6QoRvowrD79fQuLlaiDG5WlXzy0WWx2kA1YZO3sDlW7lW0QDf6np0JRwFnhdWiibtuP0tPP7fQkOxKKhKwTntV7O6qAETDzVlrbDggKJVCry88ss3qa-7-wCFdky8Gp8R7iLckEqwkICa6Nto30yme2p3W74ew-Ntw5egTfCATzFR-qKZdsJdKmzGP9bcMJQNFtEeFaJKF08OkuPk--CU2dk__4sZR0s9kjSi1WP6BvsCdTOQ3PXldICNQrrSd9sDLfxdfzAirZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LIgBKmBd-Qr7ZjwhuK-z0kNwQmv1w57DhI7rWw8cVvMaHdNU-yvGT_B0vCDPOXyAXlYHGtbo_D72kvNExyDJvceyY8qmSFQKLodKfhXbPTfy34-y8azyfXTmvaFZNzIWd9AUCA9kNL94S6tbHWgpviQW3D-DH0Ye7TvM5uRV7euZTjmGG2BAOyfo7fyX_rsZ9H9qXeSIkf-0Mu4JhTIIdN9i8hBdj9v-XRhNfvE47YS2zmLytilkukwZQJXqNwDGsmBqVwI4qOXiWSdHM_1DZEBoZlfujGPURm8549YCFc39u0DXHV1LSnDt3pKj9jGd7Mf2D3OFH_objQVTZLuWkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش فعالسازی Fragment توی اپلیکیشن MahsaNG برای رفع مشکل سرعت آپلود و محدودیت اتصال توی برخی نقاط
روی Auto بذارید فعلا، من در ادامه واستون یه سری تنظیمات پیش‌فرض می‌ذارم که تست کنید روی اینترنتتون
اگر الان کانفیگ واستون با سرعت خوبی وصله، نیازی به فعال کردن Fragment ندارید. چون سرعت کلی رو پایین میاره</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3789" target="_blank">📅 13:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3788">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ما آخر نفهمیدیم جنگ شد یا نشد</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3788" target="_blank">📅 09:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امیدوارم
WhiteDNS
ستاپ کرده باشید. برای اتصال توی شرایط جنگ
دیگه حوصله‌ی اصرار نیست</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/MatinSenPaii/3784" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3782">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اگر خواستید مفهوم فیلترینگ منطقه‌ای رو بفهمید، سوار اتوبوس بشید و از تهران برید خوزستان. به هر شهری می‌رسید آیپی تمیزهاتون از کار میفتن و باید دوباره اسکن کنید. به استان خوزستان که می‌رسید، گوشی تبدیل به یه پاره آجر بی‌مصرف میشه و فقط می‌تونید باهاش زنگ بزنید
😂</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/MatinSenPaii/3782" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3781">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MDYB1t8Ouawc5nH0pHLgKB03kPPly2NDkbKQfrWzwlsXY1qIRlDUHYL9gNflXiOs92Qm2SlBq0rA8ssJMTAlkRjO0o0Wdu7vLf-BqYEODJG1Hq6LYlIEEZQ9PMcSz8rMdmruJn7Vna3kHjVpBqtrBxKgagD1fwP-NdwX5P8WAeLaWgcByTlHBqvqz1Yy7Iu1kSqPNdp0ZK2xqOWuxxwwXLQI-Iudr6AAdRBOJJJMK6yyW2yAyMEzbjy37ZHKEK1NmXJeZhMlGLTarEljmVy6zNLNzzzr8_0g6RzCltVo9yoePnEzTt1y6-bYWmXeVxLrHAdpH5g8HOik1Zb-KY5oTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وقتشه یه سری حقایق راجب بورسیه MEXT ژاپن بگم.
حالم از این پوسترا مخصوصا راجب بورسیه‌ی ژاپن به هم می‌خوره.
واقعیت:
۱- از چندین هزار متقاضی، سالانه زیر ۵۰ نفر(متغیر) مجموعا از تمام مقاطع برگزیده میشن که اونم کاملا شانسیه.
۲- انتخاب شدن شما تماما به نیاز ژاپن بستگی داره و اصلا هم اعلام نمی‌کنن که ما به فلان رشته نیاز داریم. ممکنه شما تمام شرایط عالی رو داشته باشی با بالاترین نمره، اما «امسال ژاپن به رشته شما نیاز نداشته باشه»(مقطع ارشد و دکتری) و این رو به صورت مبهم فقط بهتون میگن که شما رد شدید! یعنی هیچ دلیلی برای رد شدنتون بهتون نمیدن توی هیچ مقطعی. شخص A با دانش نزدیک به صفر بدون بلد بودن انگلیسی یا ژاپنی قبول میشه چون ژاپن این رشته رو نیاز داره، شخص B بدون توضیح رد میشه با اینکه دانش و علم خیلی بالایی داره یا حتی مدرک زبان ژاپنی داره، چون به رشته‌اش نیاز ندارن. و فقط میگن رد شدی بدون توضیح.
۳- روند غربالگری به شدت غیراستاندارد، و رد شدن توی هر مرحله بدون توضیح هست(سه مرحله داره شامل ارسال مدارک و آزمون کتبی و مصاحبه که هرجا رد شدید، علتی نمیگن)
۴- ثبت نام برخلاف به روز بودن خود کشور ژاپن، به صورت کاملا سنتی و با پست کردن مدرک کاغذی برای سفارت توی یه فرآیند بسیار زمان‌بر و استرس‌زا(نکنه فلان چیز رو یادم رفته باشه) و هزارتا دنگ و فنگ انجام میشه. همه چیز کاغذی. همه‌چیز. یعنی حتی زحمت نمی‌دن به خودشون کد ملی شما رو وارد کنن اطلاعاتتون رو بگیرن. و توی همه‌ی ۱۵-۲۰ تا مدرکی هم که می‌خوان، یه نقطه اگر اشتباه باشه رد می‌شید توی مرحله‌ی اول. که باز هم توضیحی نمی‌دن بهتون که چرا رد شدید. صرفا میگن نقص مدارک
۵- شما ممکنه تمام تلاشتون رو بکنید، همه‌ی مراحل رو قبول بشید، اما در نهایت ژاپن توی اون سال Mext رو برای ایران کنسل کنه!! بله درست شنیدید. پارسال به خاطر جنگ ۱۲ روزه، ژاپن بورسیه‌اش رو برای ایران لغو کرد(
🤣
🤣
🤣
) صرفا چون تایم آزمونش جنگ شد. به تعویق هم ننداخت. لغو کرد. امسال هم همین شد دقیقا و به دلیل وضعیت کشور، لغو کرد. و تمام کسایی که پارسال و امسال هدفشون رو گذاشته بودن Mext، گند خورد به زندگیشون.
خلاصه‌ی کلام اینکه برای بورسیه تمرکزتون رو روی ژاپن به تنهایی نذارید و چندین تا کشور زیر نظرتون باشه</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3781" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3780">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aD6umUR2CIXjaq7W7Ds45Y4Tvli-mroOSNV3th8gaF6RHdkriUsv7wnN6XZGpvI6dzlOWeyKFKrujXAJ2G68ubc8w6j8zEKIOvPIE0axU45TZkjCZE9xPPTRu78v3a_v1uwxofzNMw8pg9lqRkg-p4sKagOl-ccKdgE1ZFXGgN_0-s4egHc5UDQmeoyVrxtQxeqOJkHPLCU8sTA-421hAaXuzffZdJRvMqN9bH3L5RZNV6f7K7CaYqwxieSI_8-IWCwhpXmxn8cDHfPtghHevVirwr4TNWqcJNjZWnMifB9IGsN__4yqfk_ibLls_5gMbYRna56LI523CWlQNhsaiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
پروژه‌ی FreeLLMAPI — یه پروکسی OpenAI-compatible فوق‌العاده‌ست که ۱۶ تا از بهترین ارائه‌دهنده‌های LLM(مدل‌های زبانی بزرگ. همون هوش مصنوعی خودمون) رایگان رو روی هم جمع کرده!
تقریباً ۱٫۷ میلیارد توکن توی هر ماه ظرفیت inference (از Google Gemini، Groq، Mistral، Cerebras، OpenRouter، GitHub Models، Cloudflare، NVIDIA، HuggingFace و ... + هر endpoint سفارشی مثل Ollama، vLLM، LM Studio و غیره) می‌ده.
ویژگی‌های اصلی:
🔤
یه endpoint واحد (/v1/chat/completions) برای همه‌چی
🔤
روتینگ هوشمند + failover خودکار (اگر یه کلید به rate limit خورد، سریع میره سراغ بعدی)
🔤
مدیریت دقیق quota هر api key تا زیر حد استفاده‌ی رایگان بمونیم
🔤
کلیدها به صورت رمزنگاری‌شده ذخیره میشن
🔤
داشبورد باحال برای مدیریت api key
🔤
نصب خیلی راحت با Docker
در واقع همه free tierهای پراکنده رو تبدیل کرده به یه LLM قدرتمند و همیشه در دسترس، بدون اینکه مجبور بشی با کلی SDK و rate limit جداگانه کلنجار بری.
بهترین‌ها برای کدنویسی (بر اساس این پروژه و لیست هوش مصنوعی‌ها) عمدتاً DeepSeek V4 Pro، Qwen3-Coder سری (مخصوصاً Qwen3-Coder Next و 480B) و Codestral/Devstral هستن.
⚡️
لینک پروژه:
https://github.com/tashfeenahmed/freellmapi
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3780" target="_blank">📅 23:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3779">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">من خودم با Hiddify راحتترم برای ساب، از اون استفاده میکنم کلا(با نت H+ الان دارم این پست رو می‌ذارم با همین ساب) اگر پینگ نداد، توی تنظیمات Tls Fragment رو روشن کنید</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/3779" target="_blank">📅 22:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3777">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jFrHHaXHdq4drAYbr7cBtJPDgfVJyekoxXow3jbnSSM0VDCMCdYwqqeGldosT_oiWJj49c2EjH_ZURromXzJkmU7a9iqj1rYD2lKCkuQxt68vgkncHrdpMIyazQL6uvLWHlnXfhimE8UuRZUO1ehDj3Lhx0rdDmRJEpK0l1CTiTEj0LwF9HcMe4WF62H3rXylYr2mkcmk3OWYncO7uHTWlj1ZTD-U0XxmynGIicfYGcjkL43fIX4Dez1BI_V9QA15UGOI7kV_xeTx81LA99-0TSfnTpmFmiU-0FaO7TCewvsWwGD6Bwb_vkixBYn91nOwy8kqyZFKPSLoEAYPiwfFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tcZ11TzDgj8EU5zq6oj_0OjRH2vMJfp5RdhZkCXVLWkhLPAGkl7JBCZguY5TWnKYzL-SIz4zN1Vk366JbRuuLWdkkwj26Vj8C0JlL0acdDT-Fa63Qr4IN_PBXdz-bXlrl4LsXECpNkngDQq0Nvaq6j5zKeQskDeZukn5uDFEhC4EF-pv8FSXIuwncjNhgCERMNJ52DWUPPpAN1nNxSO9EXGQ6P56iQJi3O5k_7Ikh-t6A0ca4tJeXEzKZQhgGqMxrzNyKvlWKS9NGksS_63Ar0xF6wzLExBMh47B92m28yVidIAK23pnyEqEzfNjDuPVRYe28Zr-5ITZYHHD9WuMkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بچه‌های WhiteDNS دارن رو یه چیزی کار می‌کنن که شاهکاره ایده‌اش
(عاشق UI اولیه‌ی اپلیکیشنم
😂
)</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3777" target="_blank">📅 21:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3776">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hrE5JNdLz-xan1UnNDHfNL9IO8PxxomGwWdnSFeZJda0Gtqj8eA-yBMr1KrEuL_R88WrxTEI9dyoLFef0mzlUNj8lZfqUhGw1viOYORb6qJBI9NddolFx0M7Zi6inhpry4d5bjlVcTBLWAIMaOfx9iK4D24LuNxc8xL3Yu-QOdX32fVrS7F8EgyMKE5-Eg7A1Hi2EJ_c_rW11o9hTxt_mN4Q1eLLr3fj3L4cKDUs6BwEx6_0lZczE3l-fosfObS2QBYGRgSnk9qxOPBenMg6ek6E3yeFxTy2yvVqgKwDliBYL1JRY2THEALQ3wErhGBk9rUC6DkB1iQWBVVrERr9PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک هنوز جوهر Opus 4.8 خشک نشده بود، مدل جدید Fable 5 رو به عنوان قوی‌ترین مدل عمومی Claude معرفی کرد!  این مدل توی برنامه‌نویسی، تحقیق و همینطور تحلیل تصویر عالی‌ترینه؛ هرچقدر کارمون پیچیده‌تر بشه، برتریش نسبت به مدل‌های دیگه بیشتر و بیشتر مشخص می‌شه.…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3776" target="_blank">📅 19:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3775">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79adfc024d.mp4?token=U2o42dZqde1i73oY3CKPrO8-MLtl5M64TnI2ZlkdhjibE9BSn_kyweie39Nv3-DnkoMNWNyB84smr-42LhdYpEhIeL3QgGghiwzev7rkOYIi-8pQP5iZ9osYoNqVUSM_yJd-yYGLxjSbgz0mKBpZXqsJbndXpOPguczq0TYlttVEBXYJMp3ZI7XAdQXOFJGcpl2eU7uOC2AoQoQ3kuLsi4j3RzT_oBrJgoreTv4B31W80QPp6NCCQ_d9jYYG9g5VDIRiNhfw3zcJz_nhLCPPB2DhWedsFmo4Y_PiqjU9FfZRkxiupIvtwjDX2Ya3YRaELNKdu3SG4r96NCtk7CT5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79adfc024d.mp4?token=U2o42dZqde1i73oY3CKPrO8-MLtl5M64TnI2ZlkdhjibE9BSn_kyweie39Nv3-DnkoMNWNyB84smr-42LhdYpEhIeL3QgGghiwzev7rkOYIi-8pQP5iZ9osYoNqVUSM_yJd-yYGLxjSbgz0mKBpZXqsJbndXpOPguczq0TYlttVEBXYJMp3ZI7XAdQXOFJGcpl2eU7uOC2AoQoQ3kuLsi4j3RzT_oBrJgoreTv4B31W80QPp6NCCQ_d9jYYG9g5VDIRiNhfw3zcJz_nhLCPPB2DhWedsFmo4Y_PiqjU9FfZRkxiupIvtwjDX2Ya3YRaELNKdu3SG4r96NCtk7CT5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آنتروپیک هنوز جوهر Opus 4.8 خشک نشده بود، مدل جدید Fable 5 رو به عنوان قوی‌ترین مدل عمومی Claude معرفی کرد!
این مدل توی برنامه‌نویسی، تحقیق و همینطور تحلیل تصویر عالی‌ترینه؛ هرچقدر کارمون پیچیده‌تر بشه، برتریش نسبت به مدل‌های دیگه بیشتر و بیشتر مشخص می‌شه.
همینطور به دلیل توانایی‌های بالاش، برای موضوعات حساس مثل امنیت سایبری(هک و امنیت)، زیست‌شناسی(شاید تولید سلاح‌های زیستی)، شیمی(شاید تولید مواد مخدر
😂
) و مطالب مشابه، از مدل ضعیف‌تر Opus 4.8 استفاده می‌شه.
همینطور همزمان مدل Mythos 5 هم معرفی شده که یه نسخه از Fable 5 با محدودیت‌های امنیتی کمتره.
فعلاً Mythos 5 فقط در اختیار تیم‌های امنیت سایبری خود آمریکا و زیرساخت‌های حیاتیش هست و ممکنه بعداً برای پژوهش‌های پزشکی و امنیتی به افراد مورد اعتماد بیشتری داده بشه. طبق جدول منتشر شده، Mythos 5 و Fable 5 در بنچمارک‌ها امتیاز بالاتری نسبت به GPT 5.5 و Gemini 3.1 Pro و خود Claude Opus 4.8 کسب کردن</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3775" target="_blank">📅 18:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3774">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X0T-4IfcedtgMZuGZDauflJ0SCymWnLAH9ZcsDRdIkMGTebGtpoWz0JK9aLqMBrBTqe91NJd1zZn15VwL01f5mJr_FOUb5bP350ObZDgQO7FT7t5YsLgal7O6t1ucqvq0ljwGod51gmk5VmpDmaoarRoZtOEig55NGKNWnsLMyER75ojt4zARvcHO6hF76-HygXI7JjQMsleVBMRlN_d9B8aSU9YeYqJYoj_aUy3mz730K-5p54_YLvYgtFQcfWeIlQMyNWOqR7Y73NNwdIq1uDqPQI9eco5CvfRGDXtt30cGLJriFxM2DMPn9Ms_8zpLl1-nrGQjDj1n1Gf1oIZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من خودم با Hiddify راحتترم برای ساب، از اون استفاده میکنم کلا(با نت H+ الان دارم این پست رو می‌ذارم با همین ساب) اگر پینگ نداد، توی تنظیمات Tls Fragment رو روشن کنید</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3774" target="_blank">📅 16:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3773">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UrZp8bYVmGq1w8967aMcYZgLU6bExYDAF7Tree7slX7udFNzPMdbVSrQhYLfSPP-nL4rPqYXxhj-dU6cUszFfG-pVetGM2XjXotmktSsnoOs4aWD_ieuuEyP4ZaizecphwjjPzhoYADbkHMuc3-y9htiiY2tcIreN59_SBOgNt9gGbln_Jy8MXaetm6As72URXMZnNDGqaKqmtc_Q9_5MlZMBOlsg9P250QsbYZnQLP6aE04QSbj6qh9_hlp7d8R5BihAPu7J4KcEtKCZmO93TNQjEsMJ89wgZ_qocW8JibvqJxg6rGypdTM7Fd-gJ-62AFReBJ77nCMnM_m8KUsgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ساب‌ها رو می‌تونید توی هر کلاینت V2rayای که دارید وارد کنید و استفاده کنید ازشون</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3773" target="_blank">📅 14:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3772">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ساب لینک مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها: https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3772" target="_blank">📅 13:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3771">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">ساب لینک
مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها
:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
⚡️
توی تمامی کلاینت ها به جز npv میتونین استفاده کنین پینگ نگیرین وصله
🟢
نحوه ی اضافه کردن ساب لینک با اپدیت خودکار
⭐️
پروکسی 1
⭐️
دونیت برای کمک به ادامه دادن این مسیر
❤️
🪐
Channel |
@Masir_Sefid
| کانال
🪐</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/3771" target="_blank">📅 13:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3770">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⏯️
ویدیو آموزش استفاده از WhiteDNS Wizard و نصب و راه‌اندازی کامل و اتوماتیک پنل ثنایی
https://youtu.be/rxxlNXLcaqU</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/3770" target="_blank">📅 11:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3769">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🛡️𝔽𝕣𝕖𝕖 𝕋𝕣𝕚𝕒𝕝 𝕂𝕖𝕪𝕤🗝️(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2b536338.mp4?token=bxO86x-eSqS3IiRqxfQXqojrbdNrnUfpK0T8aKZ4N3uZDBmDYb1KQ3vFNAO3FdxoIjg1EujmGbmXrrzY7mQDiN3AOfTlJ7N--grfcJ2HBTPDA0XM4Cf1jA9ZZBapCn97qHqfr7W4O24nRnd75mcNw19OkVE9Td4TMzbhF-9x-zEVA5LUByN-Lyqvq4xMXlyom_VKVCSDvkdYRKIQ-XmcBdp9QHdLkFD3TWOjceV1p7arNHqRSA5O4r-S67nAX1Z7Q9qYwDPHkn1n8tW5MjxS7r3JGRdCVuFU-GLGvMf4CkPR_V6rhyjfHLWLIHsHOmgg5f5lOmGuyMYp2c1sMZMhkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2b536338.mp4?token=bxO86x-eSqS3IiRqxfQXqojrbdNrnUfpK0T8aKZ4N3uZDBmDYb1KQ3vFNAO3FdxoIjg1EujmGbmXrrzY7mQDiN3AOfTlJ7N--grfcJ2HBTPDA0XM4Cf1jA9ZZBapCn97qHqfr7W4O24nRnd75mcNw19OkVE9Td4TMzbhF-9x-zEVA5LUByN-Lyqvq4xMXlyom_VKVCSDvkdYRKIQ-XmcBdp9QHdLkFD3TWOjceV1p7arNHqRSA5O4r-S67nAX1Z7Q9qYwDPHkn1n8tW5MjxS7r3JGRdCVuFU-GLGvMf4CkPR_V6rhyjfHLWLIHsHOmgg5f5lOmGuyMYp2c1sMZMhkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روش وارد کردن کلید avast secureline
هر کلید برای صد کاربر هستش
اگه به لوکیشن گیر داد داخل نرفت یبار کلیر کش کنید دوباره کلید رو وارد کنید یا به نت دیگه و vpn دیگه</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3769" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3768">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🛡️𝔽𝕣𝕖𝕖 𝕋𝕣𝕚𝕒𝕝 𝕂𝕖𝕪𝕤🗝️(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b056aeeb9d.mp4?token=Ktm0c_tFDfZysebXiee3W-rEDt--sf12lWycj8sSILyL-8Gk4NiDrjCYrQHGN8QufbW5BygLFy3s4hDOdtqsNWhkNL_X1D22ZRvXUPdrx8GT-DG-ZI9dhJcQmCW7PaSmNwYbWF-0Mh3aAPyXz2ka8Gsnpk4E7vDgGkH6ci5jwocBRHOE_SY0b0yDpULAUwQ_IGzdg7jz0VlZzqj_i1dHSP0UAhC8_52SN6aIaGSSAamyQB2KKuFAzrD5TJJ3-zz4jGbzAFZyoq7Ceg_vBidkLW-Ej92PvwB-vxnq6JHFj0OWXNsBTalJ8jDUB6OfttO-freR2CjOM2BUB4Rhd4LE6Y-5cdG6NmmPmXOWofsxR0jEAqUpA6XlmayeSlwpQ8fd_rTbrekR3OlXcehYObHZ40zO0IZ78QySypBjfWfVA6ChwbeqSnbC8KEL_PRyDWIM4qE7BCyDzdRO3cBOSlb-4xvtiTFCI61M0L_g6SNvylDAbG2XUSb_17Yyjgr0MBTmg7lnJcMczbOFnReb3Ltt7jqB8tYmcYYRT8dFcwrU73qBio1eszQa2AP2YPHrx4qphfwVitK5tih63mNXRR-WsVthYBxslsZ8jA-e4OqH86r7dp9AgKuyPJRq2BlA_HhEzSep088lmxOVan3DLYG9WjbgknKjF46Ki6ORWrXvVO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b056aeeb9d.mp4?token=Ktm0c_tFDfZysebXiee3W-rEDt--sf12lWycj8sSILyL-8Gk4NiDrjCYrQHGN8QufbW5BygLFy3s4hDOdtqsNWhkNL_X1D22ZRvXUPdrx8GT-DG-ZI9dhJcQmCW7PaSmNwYbWF-0Mh3aAPyXz2ka8Gsnpk4E7vDgGkH6ci5jwocBRHOE_SY0b0yDpULAUwQ_IGzdg7jz0VlZzqj_i1dHSP0UAhC8_52SN6aIaGSSAamyQB2KKuFAzrD5TJJ3-zz4jGbzAFZyoq7Ceg_vBidkLW-Ej92PvwB-vxnq6JHFj0OWXNsBTalJ8jDUB6OfttO-freR2CjOM2BUB4Rhd4LE6Y-5cdG6NmmPmXOWofsxR0jEAqUpA6XlmayeSlwpQ8fd_rTbrekR3OlXcehYObHZ40zO0IZ78QySypBjfWfVA6ChwbeqSnbC8KEL_PRyDWIM4qE7BCyDzdRO3cBOSlb-4xvtiTFCI61M0L_g6SNvylDAbG2XUSb_17Yyjgr0MBTmg7lnJcMczbOFnReb3Ltt7jqB8tYmcYYRT8dFcwrU73qBio1eszQa2AP2YPHrx4qphfwVitK5tih63mNXRR-WsVthYBxslsZ8jA-e4OqH86r7dp9AgKuyPJRq2BlA_HhEzSep088lmxOVan3DLYG9WjbgknKjF46Ki6ORWrXvVO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Avast
Secureline
آموزش دریافت لایسنس‌کی یکماهه
لینک سایت
https://businesshub.avast.com/dashboard
فیک میل
https://temp-mail.org/en/
https://internxt.com/temporary-email
https://mail.tm/en/
https://temp-mail.io/en
لینک دانلود
•
Android
•
iOS
برای کانکت شدن از ی vpn کمکی حتما استفاده کنید
از پروتکل mimic و openvpn استفاده کنید
ÐΛɌ₭ᑎΞ𐒡𐒡</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3768" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3767">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SAg7syHymCOJiigfymtH5WaYyib9bjFCB3tmcNYDAx41RcfcruU92695pOaz4njomWsZbX0e38u7vc_jGWNSttLe4qDNLWhpq6V0aFq-kAVTs_fKMqyR8S2y988l1EAjmFPIhF9KPRjwzgFmbH7LO_pBmkM_J8kV2fXoYSQaQQifUX9Ds81hdRjxmIL8elbvY9PvJAWSjAlrgHg5JDL3YX5Q-uZzSJIrvCrRs6KheY8zu4ULzLlQZLt83LJYT7CcBYbP0tcRycLSzDTn7w7DFZ8QvL1vgzzEpunyrmqdQmCTJ3SKywKT3VxRjw7gjci_AgRqJw5s1sl8anfjQCflpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد وایب کده. اسم دیگه روش گذاشتن قرار نیست ماهیتش رو عوض کنه
و نه خوبه نه بد. بحثش به شدت مفصله</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/MatinSenPaii/3767" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3766">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">برای WhiteDNS از
http://Netlen.com.tr
هم میتونید سرور بگیرید. فقط قبلا یه تایمی درگاه ترونش خراب بود نمیدونم درست شده یا نه
اینجا میتونید با شماره ایرانتون هم رجیستر کنید</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3766" target="_blank">📅 17:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3765">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mvb1Gp_7NHUcJkjkloctFp0GL_6jLbMsawohmwt0IDdVc_AixW1jMqbP32irCPXrw0W5Sb9X2em5vKgIIxt5IgpXommRuuf9vx48hT4w9wUPBwEbBAVgeGvPT8eA6v92O_3WNg5N1UOSrYxlQusLbJgOahrLr0pY65mLRJmwv1OcxayxTeLVzCN_t2Xe6xf64jTkAmOphN2j9uOAhCEzPAw0jojHHY1cZvS4F44q0hTxwgHhJrps79U-iKWP38RCUDwTC4pBWmUCGOP_YU6drTNrXaRUS99fif1ZqxM1Ol_6OE_DhSVvPvAKoH-zuGuLD2sc35Bnt9B1Oy9aA6PeZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام بچه‌ها:
متین جان لطفا تو کانال اعلام کن که از namecheap دامنه نگیرن. من گرفتم و بعد دو روز به علت تحریمات اکانتمو بست.</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/MatinSenPaii/3765" target="_blank">📅 13:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3764">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اگر توی ساخت پنل bpb یا edge یا nova یا نهان ارور 1101 گرفتید، کلا از اون اکانت Log out کنید و با یه اکانت جدید شروع کنید</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/3764" target="_blank">📅 10:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3763">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اگر توی ساخت پنل bpb یا edge یا nova یا نهان ارور 1101 گرفتید، کلا از اون اکانت Log out کنید و با یه اکانت جدید شروع کنید</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/MatinSenPaii/3763" target="_blank">📅 09:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3762">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستان اگر خواستید از سایت yotta سرور و دامنه بگیرید، می‌تونید آدرس فیک از
fakexy.com
بگیرید و استفاده کنید</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3762" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3761">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">Valid-08-June-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/MatinSenPaii/3761" target="_blank">📅 16:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3760">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67cf13d855.webm?token=HKdCVskJBkx5J9uHj7cX1jMzINUjidycrFYJEeI4A5X1lXIBXoWjb-1aTjtYyzr698IiLR94MKIVKYYLHQZYDySIFLIXt16KCpx6GZV2SyNgUbjNPvftnRMDaiN9vxe-Lxm_Sh90NbUNel0Yg_AZy0QL85K6k8NsO1lyv4v0l-UAM_RLsDF6q2qMxMa87tzZIXD3ESghNa4lAWOjTgpbIEsGEf0LFuR9lP1iqswXBkAGk6ceDLb94D86w1krMMEkdUgaqjRuggJvRxhQ7rCS-E5bxHpphkoB9lfFES4s6t_xFur76zqXRkwZeM2UdPr9Y5TnE_Bubs5AelIWaGj9kA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67cf13d855.webm?token=HKdCVskJBkx5J9uHj7cX1jMzINUjidycrFYJEeI4A5X1lXIBXoWjb-1aTjtYyzr698IiLR94MKIVKYYLHQZYDySIFLIXt16KCpx6GZV2SyNgUbjNPvftnRMDaiN9vxe-Lxm_Sh90NbUNel0Yg_AZy0QL85K6k8NsO1lyv4v0l-UAM_RLsDF6q2qMxMa87tzZIXD3ESghNa4lAWOjTgpbIEsGEf0LFuR9lP1iqswXBkAGk6ceDLb94D86w1krMMEkdUgaqjRuggJvRxhQ7rCS-E5bxHpphkoB9lfFES4s6t_xFur76zqXRkwZeM2UdPr9Y5TnE_Bubs5AelIWaGj9kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/MatinSenPaii/3760" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3759">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Valid-08-June-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3759" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینها 688 تا ریزالوری هستن که Valid بودن توی دوره‌ی قطعی برای من، از اون 5800 تا ریزالور ویدئوی WhiteDNS</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/MatinSenPaii/3759" target="_blank">📅 15:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3758">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-poll">
<h4>📊 دوستانی که سرور دارید، دیتاسنترای ایرانتون...</h4>
<ul>
<li>✓ اصلا وصل نشده بود هنوز اینترنتش</li>
<li>✓ وصل شده بود، الان قطع شد</li>
<li>✓ وصل شده بود و هنوز وصله</li>
<li>✓ سرور ندارم، دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/MatinSenPaii/3758" target="_blank">📅 13:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3757">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترجیحا هیچ VPNای نخرید دوستان. هیچ تضمینی نیست که اگر اینترنت قطع بشه هم اونا وصل بمونن یا نه. مثل اوایل جنگ که خیلیا اسکم شدن
همون هزینه رو بذارید whitedns راه بندازید</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/MatinSenPaii/3757" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3756">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هر پنج دقیقه میرم یه پینگ میگیرم ببینم وضعیت چیه
روانیمون کردن</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/MatinSenPaii/3756" target="_blank">📅 12:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3755">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اینکه هنوز اینترنت قطع نشده جای تعجب داره به خدا</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/MatinSenPaii/3755" target="_blank">📅 12:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3754">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مجددا تأکید می‌کنم که سرورهای عمومی سرعت به شدت پایینی دارن مخصوصا توی محدودیت‌های شدید و بسته شدن ریزالورها. تمام تلاش رو بذارید روی راه‌اندازی
سرور+دامنه شخصی</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/MatinSenPaii/3754" target="_blank">📅 11:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3753">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سرورهای عمومی MasterDns(با کلاینت WhiteDNS):
1-
https://t.me/Masir_Sefid/612</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/MatinSenPaii/3753" target="_blank">📅 09:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3752">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sHQM_LrgnjLNaA9D2FfxNqvwsLO6-_urhl3ZUzYPEgkmHzSqW-MkvnVb5CTGAPL9QthVgMMQpc8T3OE4GhPJ6nQ01ckpUkJ6Q0cDcS_4ELK2Gs0bAxOZ5crt1UnJgkeeb7qSh68GoxH8NHlFJNqU_Gv1KPpqrsJbX_L70UGCdbXwVasIkb4DI5QVGnE0h9uapeHWQOX97nVDWyW8TZVrHESgfplKdQpEF4zzqSNGTfYLSkFdRU3ls_xHkDYB3DL-9IkKuv_O428cOf9AVOjB7-qeqe2Kq5-Xo8RX3bagjy_Y94jgG24sexypEt0cu1qBzLYRV0vYXwXdeGNUEvsXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب همونی شد که فکر می‌کردیم. جنگی در کار نیست انگار تا بعد از جام جهانی. فعلا اینترنت داریم</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/MatinSenPaii/3752" target="_blank">📅 08:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3751">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خب همونی شد که فکر می‌کردیم. جنگی در کار نیست انگار تا بعد از جام جهانی. فعلا اینترنت داریم</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/MatinSenPaii/3751" target="_blank">📅 08:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3750">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دوستان دامین سالم این شکلیه. نه اینکه از ۵۸۰۰ تا بهتون ۴ تا valid بده</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/MatinSenPaii/3750" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3749">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ut0ddOfD3l06YJHfFe8wevzB9gVH8QHyZWtl1fLutWznCjgL8aVVgbdS-4CzGQLlrsu3xELuBStKFqn7oEerrkodmq_X4-ox0ipMYie5XdgcodAu8Aj2VZA6w068wxYs0OgAXU-epb95lxOIA0mCXT4k1SN_M9PvENix8bsMFS7wrNjMxRfN5Pv-mgpnIp9cC8JzibbuAYzvi73twRQ6xa1Vo9dhxzADTRDTYLoG430p1AMSbK5MvFUmu9r9iQOLa3lNjAcqq-_6avVLIIObLMthPH98lh596IH9jjT4Qp38mIJku-V8tL3l42FuQZLGc_HtWtwJ8uPuQDD2SPbk8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان دامین سالم این شکلیه. نه اینکه از ۵۸۰۰ تا بهتون ۴ تا valid بده</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/MatinSenPaii/3749" target="_blank">📅 00:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3748">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-poll">
<h4>📊 سرعت اینترنتتون؟</h4>
<ul>
<li>✓ تفاوتی نکرده</li>
<li>✓ یه کم کندی حس میکنم</li>
<li>✓ تمام کانفیگا از کار افتاده و نمیتونم به هیچی وصل بشم</li>
</ul>
</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/MatinSenPaii/3748" target="_blank">📅 23:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3746">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">Matin SenPai
pinned «
دوستان با این اوصاف حمله‌ی پیش‌دستانه WhiteDNS+Master راه بندازید که هر لحظه ممکنه اینترنت رو قطع کنن متأسفانه. توی ویدئو آموزش خرید سرور و دامنه و راه‌اندازی و تانل کردن کل سیستم و راه‌اندازی روی گوشی و سیستم هست کامل: https://youtu.be/6Pm7kNQb3mo سر هر تحرک…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3746" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/MatinSenPaii/3745" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3744">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تا حالا حمله‌ی پیش‌دستانه تجربه نکردیم. اگر منطقی باشه، اینترنت به جای قطع شدن باید قوی‌تر بشه</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/MatinSenPaii/3744" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دوستان با این اوصاف حمله‌ی پیش‌دستانه WhiteDNS+Master راه بندازید که هر لحظه ممکنه اینترنت رو قطع کنن متأسفانه.
توی ویدئو آموزش خرید سرور و دامنه و راه‌اندازی و تانل کردن کل سیستم و راه‌اندازی روی گوشی و سیستم هست کامل:
https://youtu.be/6Pm7kNQb3mo
سر هر تحرک نظامی و موشک مجبورم این حرفو بزنم چون احتمالش هست واقعا هر لحظه</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/MatinSenPaii/3743" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">تغییرات WhiteDNS Wizard v1.1.0
- خطای ACME و DNS بهتر تشخیص داده می‌شود.
- قبل از ساخت SSL، برنامه چک می‌کند دامنه واقعا روی Cloudflare فعال و درست تنظیم شده باشد.
- پیام‌های خطا واضح‌تر شده‌اند و کاربر بهتر می‌فهمد مشکل از توکن، دامنه یا DNS است.
- آموزش دسترسی‌های Cloudflare در README کامل‌تر شده.
- Reality XHTTP با Reality TCP Vision جایگزین شد.
- Reality حالا از
xtls-rprx-vision
استفاده می‌کند.
- انتخاب SNI برای Reality امن‌تر و پایدارتر شده.
- مسیر نصب روی سرور از
/opt
به
/var/lib/whitedns
منتقل شد تا روی VPSهای بیشتری بدون مشکل کار کند.
- مشکل ساخت فایل Docker Compose روی بعضی سرورها رفع شد.
- نصب Docker Compose Plugin روی سیستم‌عامل‌های مختلف بهتر شده.
- بیلدهای GitHub Release سریع‌تر شده‌اند و به صورت موازی ساخته می‌شوند.
- چند مشکل مربوط به مسیر فایل‌ها، ریستور، تست‌ها و آپلود فایل‌ها رفع شد.
https://github.com/iampedii/WhiteDNS-Wizard/releases/tag/v1.1.0</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/MatinSenPaii/3742" target="_blank">📅 21:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یه جمله‌ی مشترک که از افرادی که پایتون اولین زبان برنامه‌نویسیشون بوده و بعد از اون رفتن سراغ یه زبان دیگه(علی‌الحصوص
زبان‌های کامپایلری
) زیاد شنیدم، این بوده که تازه با یاد گرفتن یه زبان جدید فهمیدن برنامه‌نویسی چیه. و درک و قدرت حل مسئله‌شون اونجا بوده که رشد کرده. علتش برام جالبه</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/MatinSenPaii/3741" target="_blank">📅 20:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این پنل هم دیدم بچه‌ها زیاد باهاش ساخته بودن vpn روی کلودفلر. یه تست بکنید https://github.com/IRNova/Nova-Proxy</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/MatinSenPaii/3740" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این پنل هم دیدم بچه‌ها زیاد باهاش ساخته بودن vpn روی کلودفلر. یه تست بکنید
https://github.com/IRNova/Nova-Proxy</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/MatinSenPaii/3739" target="_blank">📅 15:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">ساب لینک
مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها
:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
⚡️
توی تمامی کلاینت ها به جز npv میتونین استفاده کنین پینگ نگیرین وصله
🟢
نحوه ی اضافه کردن ساب لینک با اپدیت خودکار
⭐️
پروکسی 1
|
پروکسی 2
|
پروکسی 3
⭐️
دونیت برای کمک به ادامه دادن این مسیر
❤️
🪐
Channel |
@Masir_Sefid
| کانال
🪐</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/MatinSenPaii/3738" target="_blank">📅 11:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیـ بـ خـ(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4hfsJfbQYFgoNJ7p0Qtl5G9sy2WfQ74s1tLxfJRWztn5p-rI_6AqRMkI6Nct2vrdHdbrg7nlUxD_HKpVw9ASFkJuuriWMBEV3pMrweTt7ORUdM6eGIE7YIt2tH45I4sBHuHpq2xVvB2n7BG2GiUGbXF7ycKLouoUMuiFP81lR-brezBWAutMCOncM0CADiOPuYsi4i2Ty_XTGjNIg8wuT4gkdJH8aWBm_3sVqwDNdCd_HTvojZ8jTcL8rJe3HOVNhoN3xvppIaDVYCxdAVPIp__w1AXUYP7S_NKu9s0wDvSGNqICwCPJVhIQk8NCetpkQpWYPsv3foF8NiAgbLaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه نهان
🍷
پنلی بر بستر
#کلودفلر
با کلی قابلیت به صورت رایگان و تنها با دادن ip واسه خودتون یا خانواده فیلترشکن بسازید...
ویژگی های این پنل:
✅
⭐
محدودیت حجم گذاشت
🗓
تاریخ انقضا تعیین کرد
🚫
دسترسی رو قطع کرد
✅
دوباره فعالش کرد
❗️
مصرفش رو دید
و همه اینا بدون دست زدن به مستقیم به Worker یا KV.
‏یه سری امکانات مدیریتی هم داره که بعد از مدتی استفاده واقعاً به درد می‌خورن:
⚡️
داشبورد مصرف
☁️
Cloudflare Analytics
🔔
نوتیف با بات تلگرام
💾
Backup / Restore
و چندتا ابزار دیگه که کم‌کم بیشتر میشن.
لینک خود پروژه:
https://github.com/itsyebekhe/nahan
@yebekhe
👑</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/MatinSenPaii/3737" target="_blank">📅 08:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🍷
یه سری نکات رو بگم در مورد bpb:  کانفیگ ممکنه پینگ نده واستون ولی کار کنه الویت رو پینگ نزارید  داخل تنظیمات اگر مشکلی بود به جای chrome از firefox استفاده کنید  اگر اینترنت شما 8.8.8.8 کار نمیکنه یا اختلال داره سعی کنید از dns زیر استفاده کنید:(کمترین اختلال…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/3736" target="_blank">📅 01:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3735">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">☠️
آموزش ساده آپدیت پنل BPB به آخرین نسخه  نکته: همونطور که توی ویدئو گفتم این صرفا آموزش آپدیته و هنوز نسخه‌ی استیبل نیومده اما می‌تونید استفاده کنید از ورژن‌های Pre-release
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی  BPB برای دانلود فایل…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/MatinSenPaii/3735" target="_blank">📅 01:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3734">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏نسخه‌ 4.2.2 پنل BPB منتشر شد
🕶️
طبق گفته‌ی
برنامه‌نویس پروژه
، این نسخه مشکلاتی که از سمت کلادفلر بودن رو برطرف کرده
🔁
اگر دارید پنل جدید باهاش می‌سازید هیچ کار اضافه‌تری نیاز نیست، ولی اگر آپدیت می‌کنید باید همه‌ی ساب‌ها رو آپدیت کنید و اگر دستی توی داشبورد مقدار compatibility date رو تغییر داده بودید، بذارید روی جدیدترین تاریخ
طبق ویدئویی که برای آپدیت دادم
📆
تغییرات این نسخه:
1- بخش جدید External Raw configs:
میتونید ساب و کانفیگای شخصیتون رو اضافه کنید که همه‌شون به ساب Raw اضافه می‌شن
💪
2- بخش UpStream اضافه شده که می‌تونید به طور مثال
127.0.0.1:40443
رو به عنوان آیپی و پورت دیفالت بذارید(برای اسپوف) که به ساب Normal و Raw اضافه میشه و دیگه نیازی نیست دستی ویرایش کنید
💪
3- تغییرات جدید هسته‌ی Xray اعمال شده که حتما باید کلاینتاتون(V2rayNG یا هر کلاینتی استفاده می‌کنید) آخرین نسخه رو داشته باشه
😎
جزئیات کامل تغییرات رو اینجا بخونید:
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases/tag/v4.2.2
آموزش ویدئویی آپدیت از نسخه قدیمی به جدید:
https://t.me/MatinSenPaii/3732
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/MatinSenPaii/3734" target="_blank">📅 00:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3733">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JVKODrWyLXK9PDXwXOz2IMt6nCyBdIL5g3bYmSGsPD53DYcUSW7T10auQ3NthGp1jKMK0t3FJPCRiSMhw2cxXt0B-MtvEcxUv0TIJ6IyZsqW0NPLKHB12AWbPR6sHdRJHLaKGcm6Fk5juqwrQ1LDcdnO4NU1AjCclh3KNJhy6r0LyxHVbao92DpsJMwmunLQiESKtjtyfsMLbKGHchJKm6oW3_VT3gxi8JLAxEtMTWuhwY5ErGPdLk23n4ia4twOVBRDYHMT6fOWxL1_R_ePq6dPMyB_EIGs-ec64W8Wabz5MKIwsv7-hWxfFUjFuMnfxxLUT29mcmWUx2afI_wmEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار دیسلایک اضافه کردن به توییتر</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/MatinSenPaii/3733" target="_blank">📅 20:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3732">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">☠️
آموزش ساده آپدیت پنل BPB به آخرین نسخه
نکته: همونطور که توی ویدئو گفتم این صرفا آموزش آپدیته و هنوز نسخه‌ی استیبل نیومده اما می‌تونید استفاده کنید از ورژن‌های Pre-release
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی  BPB برای دانلود فایل ورکر:
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases
⭐️
توی این ویدئو بهتون یاد میدم که چه شکلی می‌تونید پنل BPB رو آپدیت کنید
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
قبلش باید این شکلی یکی ساخته باشین:
https://youtu.be/_aXy8wwyRG8
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3732" target="_blank">📅 16:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3731">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔥
1500 کانفیگ جدید به ساب WhiteDNS اضافه شد
.
همون ساب های قبلی رو رفرش کنید.
⬅️
آموزش استفاده از FlClash
⬅️
آموزش استفاده از Clash Party
ممنون از همراهی شما
🤍</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/3731" target="_blank">📅 15:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3730">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⚠️
Confirmed: Metrics show a major disruption to internet connectivity in Pakistan-administered Azad Jammu and Kashmir.</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/3730" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3729">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">یک سری بحث و احتمال هست که یوتیوب فیلترش برداشته بشه، همون‌طور که گویا برای یک سری شده الان هم (البته مشخص نیست اختلاله یا واقعا داره رفع فیلتر میشه).
اینکه حقی که ازمون گرفتن رو بدن هنر نیست، ولی خب واقعا خوب میشه اگه این اتفاق بیفته و مردم همه بتونن دسترسی داشته باشن
♥️
همون‌طور که
قبلاً هم بارها گفتم
، ما یوتیوبر بی خانمان هم بشیم مهم نیست، مهم دسترسی درست هست و آزاد برای همه هستش.
اون یوتوبر بی‌شرفی که ناراحت میشه از آزاد شدن دسترسی هم بنظرم هرچه سریعتر آرک تمرینی نفس نکشیدن رو شروع بکنه
🫵🏻</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3729" target="_blank">📅 12:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3728">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مراقب باشید سرور ۱۲۸ مگابایت رم و بدون ipv4 و اینا نخرید دوستان
😂
اونا رو هیچ کاریشون نمی‌تونید بکنید</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/3728" target="_blank">📅 12:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3727">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یکی از دوستان توییتر(ixAbolfazl)، دیشب یه سایت معرفی کردش برای پیدا کردن ارزون‌ترین سرورهای مجازی یه سریاش قیمت سالیانه‌شون کلا 2-3 دلاره. در این حد و کریپتو هم قبول میکنن مجدد یه سریا  آدرس: serverhunter.com</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3727" target="_blank">📅 11:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3726">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D1KMyAPbBSdkvsnMuIV494r0Ru36Ux0P9JBJIi29fqvfShAqcaNDxzQyZWBm-8IJkjxl0IuCcqp5fW42oEEXF7pkp742766el1_Cb4Upe-eG6R871sDO0zVdCo86FfMnDwl0Y68vDq7OHXM9VM4Ms1-W0ZpH-y0uxiPeVUiF581cdmhN2DXEAI-qs0Cr_d4AsFcgV-Fu-o5hhSY6nY4bpbQTyDDU9L_j9-WtSCpRDs3sIDdxszzyTp7esrtKoh0fYDkTkriqhz4JcGQcx2umWLg4DTq5cEXtlgk6-jSlvzh8WNVB5nr657KV8JaMLwVP70sgSAl1bc1Je0Kjj20Pgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان توییتر(
ixAbolfazl
)، دیشب یه سایت معرفی کردش برای پیدا کردن ارزون‌ترین سرورهای مجازی
یه سریاش قیمت سالیانه‌شون کلا 2-3 دلاره. در این حد
و کریپتو هم قبول میکنن مجدد یه سریا
آدرس:
serverhunter.com</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/MatinSenPaii/3726" target="_blank">📅 08:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3724">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ij2MfqH2FWUvw9wgc_QcOdnN0HbCQLbs73d_VXP0xoh10FIqcYdlK-BQUDIXeFpgYfiYwp-b0aWzz7yjwt9Qa2nOBXq7fTFDO99dTuD2bANkKaK0OnmOMrAZ6LvjLogaK-3CMwqkwLzNMrjJ81tMkL-Li9iP9oun463pkzbMztDsoA-Lvsa09_-SPUEFImWd5EMaM4tJTviVrRC-YPPp80X9R29qm8WFjyfBQQdE3wYLaDl4aLnCS4ObR67JUXEe-4zkenEH_SsqXYL4UktyyyntZbzrfX6fIU3pjEvR6u2EC5kNJ_ty5h-wFKCfZkbfuFjKTWC_DspXVwP13BmR-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rg5mbiki9Vis6y6hOQo60D2FHWARdiouidHn0AtTgpglpdn-5DMFQUibfQWjMQdQW6sEuS2ninm8Uu4PShk1-BpI8ZMJb6wFb6W5wp8u17hEx96gwAVqO8QxTC37hKbxk3FyRymeVOH45w2m1XvTnsw78fnk7qfu_alAQ1gDVQoUFiMNqIshnRFePe91F4CTNSi5UVutg_Gqj36lku2wt9PAWya3LN_TZPTfN7WZnL_IvxaC2D_TiYkso81qnj7_9jEktRVQxGcT_IC3JxQS3aWjYlkE61V5J0oD6FLsCCSzLzHu-BrkMgv2KARVbXcHHI1Gy0ZO0t5VB2XkJPdvOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">والا برای من هیچکدوم روی ایرانسل و همراه اول نمیان
یه سری شایعه شده بود که میخوان یوتوب رو رفع فیلتر کنن
اما خب بازیشونه دیگه. سرگرم کردن ملت</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/3724" target="_blank">📅 02:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3723">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/us6WMI3ABRPiU4qQb0zhXUJB58MYMy3t3Uk3taBXsrpGOL5AaIAWoNPiNuF2ntR9Xl9R65pJNVDpFaoAzIOw7SPauGJxtvb62q-oaB93zCiUUyIZN0EW2hdYex4kpl2IjMqdxxpjzQgfuyf7PWUrRrK5rFpzqD26JmptPBUj_Fq1mXW1q7AgV_VZm-GZYsjH91EvY2vjJFgiSRzZAka5qwovCVtr9zQ9Dx459NEMEmHb6Oy0kMIbu22ZCc13hJvmgM4orPeza20xOk7MaQadSz24R7qUMxa2jcC0dI14oSvC7vmOq_jzutIGsHdhMFwllc5HjkbtHR6VmiQkWmx_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شما هم این شکلی شده بچه‌ها؟ با لایک و دیسلایک بگید
شنیدم این رو چند بار از سر شب</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3723" target="_blank">📅 02:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3716">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3716" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بفرمایید تست کنید. ورژن 0.6.0</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/MatinSenPaii/3716" target="_blank">📅 02:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3715">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R1z9bjvA7ifakLIXBm5-ozTRHMtvIDht7T-rvocEVGglVIjRnyIEK1QiVzPeZou0hhkbPLmOOyYg7xcjOaquufEPC1SQTdVGbCfACrRWTDSZrWZKHUKG8Mz7MN5mguReKaPP7F363IpRLtS3IFU2XU7512bs1VfJ9jsVCocanh2P2sGPM2HMmnuU-x8Da-mkpke-h3ndk6T4hEND3RsZpVxdv8G6gYsjpu6UGXBwNmh4kPGfqTvD4jwryMBmXpSLNUQWpDQ-W1ZciD7QZYtT0AGljJRQ48uS1dzjTsazL7jS6lJvupOtP_IE-K78twvb4vQLe_C7uU8BUe7fzuZAXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل بزرگ اسکن روی اینترنت سیمکارت هم حل شد</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3715" target="_blank">📅 01:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3714">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مشکل بزرگ اسکن روی اینترنت سیمکارت هم حل شد</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3714" target="_blank">📅 00:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3713">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uXUlr8hrieELs7XAWwwVwXH5VaYt84tY9hHqSLKrhZfq9Qq26vy2VwU6LwBBAakJuBigfNvoHIgyRwC8T2Uuoyonj6yUWSkC5pLz-p46Q3ZyU3gjCvwOwnKRe1KH6p03ZAgjH1eJdIiUbZxkiAKJhQpPdkD4aNlGs43R6PlmoBTOijvxorkRSsT1ZFJm9gKVKYAk-7ERQGUw1XxJdacRpM7IE1JJCSooaR7vciXu4oVjWLDdQzIWVWlT51vLJhLSUDr8k2Y8XxK9SCFXHlJYc3EfxgFx6LjJYyuQskY7DRNUaw_vknQEa6mSPGapfIEh1bPuCN4wI0yqSw-bt7OLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان این رو بگم توی ورژن جدید هسته‌ی ایکس ری، حتما باید Allow Insecure رو False بذارید توی کانفیگ وگرنه ارور میده</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/MatinSenPaii/3713" target="_blank">📅 00:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3712">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یه کار جالبی یکی از بچه‌ها سر SenPaiScanner در آورده که واستون قرار میدم به زودی. PR های بقیه‌ی دوستان هم بررسی کردم و همه عالی بود و تأیید شد و رفت روی کد اصلی</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/MatinSenPaii/3712" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3711">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یه کار جالبی یکی از بچه‌ها سر SenPaiScanner در آورده که واستون قرار میدم به زودی. PR های بقیه‌ی دوستان هم بررسی کردم و همه عالی بود و تأیید شد و رفت روی کد اصلی</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3711" target="_blank">📅 00:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3710">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XlL0EtYSWNewYJgOin4tayBG69wTfNAOzgxa0pIjSAjc-ieIJVHbHnJA_ECtS2qWHrCrL2PCz-s_uubNuOUX0aKP1oN6TnzPOtml_259cEJ7LVnW0eofaDcEBDjYprNcaL7Fg190ZW5XECOGOnhHwV72N4OTQRM9ScOz9-i3AhQOjf6vusulkTNhdyb2WtG8t_V2Pf54l0FVFvb2Z36H-zJpBV5xYY3LjMZPd_dtb6R1J65sFIuEuNqAwBy_hpOTya-bN77OcH4lAumLWKxgCXOKfLPGeLttKc2dk0Vmy7Hexb19o6XeX4kyN5DIb6kud_oXzDhlGoyPwPLmC4uH4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس WhiteDNS-Wizard برای کسایی طراحی شده که سرور و دامنه خریدن، و حالا نمی‌دونن که با اینا چیکار بکنن
👍
این نرم‌افزار مولتی‌کراس پلتفرم تحت CLI اوپن سورس، از شما اطلاعات سرور و دامنه میگیره، به علاوه API-TOKEN کلودفلر، و برای شما صفر تا صد کار نصب پنل، گرفتن سرتیفیکیت و ssl و ... رو انجام میده. و این خروجی‌ها رو میده:
1- کانفیگ VLESS WS شخصی
2- کانفیگ REALITY-XHTTP شخصی
3- کانفیگ Hysteria2 شخصی
4- کانفیگ Shadowsocks شخصی
5- کانفیگ Tor vless ws
6- کانفیگ Tor Hysteria2
7- کانفیگ Tor direct
8- به زودی مستر و ... هم اضافه میشه
آموزشش رو هم داریم با آپدیت بعدی
گیتهاب:
https://github.com/iampedii/WhiteDNS-Wizard
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3710" target="_blank">📅 22:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3709">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGeghCqB-qnznxdsh7z9KEWIYhb5XVksXD4MbIqliCgeKKJLKqZwwtN356931WRxzzFzsrLZlYK-n5I7CAJB4rhfFH_nn0uM3t5p3q5-qW3ibq8DMAAhdMBwVPovAX62cSYSKD3bYAwUqfPTXBt_rMwBZdlb_5vZjUvz8_NT0ttQEG7b6MC_9jog60tqnkKnjXANbOt2oT2QTMas1V_9EJT32yBQvPuO5eaKqMDru6kYogFMFodLI5zE2UltSHh8gWpXoSeZl3rQ9x5LniMUdvIZdtkLgsoWQd2ysbZ9jLVQuDQfQQA_9ynkx4641_0-sF3zUUlZkwPMclXFIM1P-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AzadiTunnel نسخه آیفون شیر و خورشید
👑
یک اپ iOS برای اتصال امن و پایدارتر، با تمرکز روی تجربه ساده، CDN Fronting، DNS هوشمند و تست اتصال.
📱
لینک مستقیم اپ استور:
https://apps.apple.com/ca/app/azaditunnel/id6776486891
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3709" target="_blank">📅 20:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3708">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ورژن جدید 4.2.0 BPB رو تست کنید بچه‌ها. سازنده‌ی عزیز روی مشکل Undefined کار کرد و درستش کرد. همینطور بخش Compatibility date رو نیازی نیست دست بزنید دیگه https://github.com/bia-pain-bache/BPB-Worker-Panel/releases/tag/v4.2.0</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/MatinSenPaii/3708" target="_blank">📅 18:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3707">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NcVUqYhniNkELYZayT4lXuGXZrwvPLcDoiMXn-TPfGbTFGYOTPpUHaA5nQXMKRbNMH3_LlhvHMGJ2B-l1d-wyZ5x52U18Cp-CLI7tL4UpTIxOHmvofbCr3vVKrRd4wYIyBymYrqR36AFnRumTaH7Xi-noBwGSUsxw1BqG-5zP8X205BYs2It0mZDve_tkFix41iaXBwr81VA1Gls6qyLCtDcc5-2jEm1PfPH1tiKnJ54Q3vgLGQ4gjSZm69wtgEeAZdDWzmDZkJUiahQmymucq7WF2HTyy3MUEfWuopQPaDCy27PyCHspmoxirs0kwOuVaxNW3sbf9Qv5hijJPAlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شرکت OpenAI ویژگی Dreaming رو برای حافظه ChatGPT معرفی کرد!
بالاخره بعد از مدت‌ها انتظار، OpenAI ویژگی خیلی مهمی به اسم Dreaming رو برای ChatGPT معرفی کرد. این آپدیت حافظه رو از حالت «یادآوری ساده» به یه سیستم هوشمند و پویا تبدیل کرده.
قبلاً چی بود؟
قبلاً ChatGPT چند تا نکته رو یادش می‌موند، ولی بعد از مدتی قدیمی و بی‌ربط می‌شد. مثلاً اگه بهش گفته بودی رژیم غذایی خاصی داری یا پروژه‌ای داری، بعد از چند هفته دیگه درست به یادش نمی‌اومد.
حالا با Dreaming چی شده؟
با این قابلیت ChatGPT تو پس‌زمینه (حتی وقتی باهاش حرف نمی‌زنی) همه چت‌هات رو بررسی می‌کنه، خلاصه می‌کنه، الگوها رو پیدا می‌کنه و حافظه‌ش رو همیشه تازه و به‌روز نگه می‌داره. انگار داره «رویا می‌بینه» و اطلاعات رو مرتب و هوشمندانه سازماندهی می‌کنه.
فایده‌های واقعی‌ش چیه؟
شخصی‌سازی خیلی بهتر: ترجیحاتت، علایقت، محدودیت‌هات و جزئیات زندگی‌ت رو خیلی دقیق‌تر به خاطر می‌سپاره. مثلاً اگه قبلاً گفتی عاشق عکاسی طبیعت هستی، دیگه پیشنهادهای generic نمی‌ده؛ مستقیم بهت ایده‌های مرتبط با سبک مورد علاقه‌ت می‌ده.
پروژه‌های طولانی: اگه روی یه پروژه چند ماهه کار می‌کنی (مثل نوشتن کتاب، راه‌اندازی بیزینس یا یادگیری زبان)، لازم نیست هر بار از اول توضیح بدی. ChatGPT زمینه کامل رو حفظ می‌کنه.
آپدیت خودکار: مثلاً اگه گفتی قراره به سفر بری، بعد از سفر خودش متوجه می‌شه و اطلاعات قدیمی رو پاک یا آپدیت می‌کنه.
کنترل کامل داری: می‌تونی حافظه رو ببینی، ویرایش کنی، بگی چی رو فراموش کنه یا چی رو حتماً یادش بمونه.
در کل، ChatGPT دیگه مثل یه دوست معمولی عمل می‌کنه که فقط حرفاتو گوش می‌ده (حتی این هم با ما دوست معمولیه!) حالا مثل یه دستیار واقعاً باهوش شده که تو جزئیات زندگی و کارتو درگیره و همیشه به‌روزه.
این ویژگی از امروز برای کاربران Plus و Pro در آمریکا فعال شده و به زودی برای بقیه کشورها و حتی کاربران معمولی هم می‌رسه.
لینک کامل توضیحات OpenAI:
https://openai.com/index/chatgpt-memory-dreaming/
✍️
Diego JR</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/MatinSenPaii/3707" target="_blank">📅 15:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3706">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ورژن جدید 4.2.0 BPB رو تست کنید بچه‌ها. سازنده‌ی عزیز روی مشکل Undefined کار کرد و درستش کرد. همینطور بخش Compatibility date رو نیازی نیست دست بزنید دیگه
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases/tag/v4.2.0</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3706" target="_blank">📅 14:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3705">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nQGFYivGhQ0LgK-SzYCQJvUarZN5FD8lmp4-93lQvXBXpoqKeYBgA2ec9dgalsmbwO98HtUaBYmiuNjfPBCE8xXZs7v7t95H00-lhkK0LgScIpnYMat77ZMxxmtpITzaYT5SMnHagmVe2lJpb-piajpsVjykBQwJDY1oAFo3Minc4iLdZrGU7cVXxht4iUpv2l1FoPv59abdaBiun1O5-h9iaK69Mah6U9JXBxAXwQRMSLWNrXLbzsYasl51w-ScjTkPLb_bK-jObxKawiqEcdFjYl0bqPpDejDHGK-862Tcjh2P-OjXkjw-syLl1C6EC4Ndwi3FZv-QwO_Ou8wrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اگر کانفیگ worker پینگ می‌ده اما درست وصل نمیشه تنظیمات مثل عکس قرار بدید fingerprint روی Firefox و Alpn روی http/1.1
یا اگر توی mahsang هستید Psiphon انتهای اتصال قرار بدید
✍️
🏴
Amin
🏴</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/MatinSenPaii/3705" target="_blank">📅 11:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3704">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دوستان این رو بگم توی ورژن جدید هسته‌ی ایکس ری، حتما باید Allow Insecure رو False بذارید توی کانفیگ وگرنه ارور میده</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/MatinSenPaii/3704" target="_blank">📅 06:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3703">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SZ51dwxWvr-F6gwiqAMoDFS8eMXrg4Lh5RRijnemGGhcgnoomDW2CNLJUf0zi0hL1-FXCcEQI2y7Qre8x--ec0nb69d5ER-6tg8tTqNBN2uEpp0G0dXKc_1s8W_EsRZDfmHuTNe5SB_7UBegmcdjW6w-Hsr12p4pvGeRHgx751rdxxcI4HkwfMzf1M1ay3SLLqbBY753oH42qVe7A4ZEDv9L1TKuDyr1BXym5d3TYNRzplAEcN44CppYLWnEhvl5SP0UDjDag8Xh6mBzXOo5pr4wPijLos9lmTZz29mCzAvW2XMboBrpgpuH20di4zICFWGUiTNx3sev3AMXUCVSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به چند سرویس تحریمی مثل اسپاتیفای، گراک، کلاد و ... ربطی به آتش‌بس، توافق و رفع تحریم‌ها نداره و مربوط میشه به دستکاری شبکه توسط فیلترچی و عبور ترافیک از شبکه آذربایجان!</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/MatinSenPaii/3703" target="_blank">📅 23:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3702">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FRdF2wFUrLo1q7y1zhhUjgxwFOBUAbn7Rx_bhJIqLalxlynX86ycQKSUFBEdZZAVoCXsJFX_pQMsY_6rs7mtTF3HX262lbhqmMspiK9_DWZT5FN5zC9Jdl5OB5wv9vBBe3m4u12OCmusI2Vosqsp2nNM4wXr3m9l0YfqCQCZG1Q4s4PXc0a9Oli9sLVfNNQgZRtYfX9EJ5Vm4neK_a0VPgw9-FrtKYYsTPGPBDk6FlfNmnRVeE4nyThSQECue2Xa6iQGXmmTsVNmrHPMO2L8LnHaM7oxPaQH90CcpO7sWh8CgfclGsg7Jv9FrMzw8A6k_puvXzNe8Zg8DbVWdKSPWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدودیت کلودفلر(روزانه تقریبا ۶ گیگ) روی اکانت کلودفلر شماست. نه خود Worker
پس اگر می‌خواید این محدودیت بشه 12 گیگ، یه اتمیک میل جدید می‌سازید، یه اکانت کلودفلر جدید می‌سازید، و یه بار دیگه مراحل ساخت رو پیش میرید روی اکانت جدید</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/MatinSenPaii/3702" target="_blank">📅 23:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3701">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
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
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/MatinSenPaii/3701" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3700">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">😊
آموزش استفاده از Clash Party نسخه ویندوز در کانال یوتیوب WhiteDNS
🔥
کانال مارو Subscribe داشته باشید.
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3700" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3699">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این هم آموزش‌های مربوطه. از لینک ساب گیتهاب استفاده کنید</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/MatinSenPaii/3699" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3698">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-poll">
<h4>📊 چرا نتونستید وصل بشید؟</h4>
<ul>
<li>✓ بلد نشدم وارد کنم</li>
<li>✓ لینک ساب رو زدم آپدیت نشد</li>
<li>✓ لینک ساب رو ژدم آپدیت هم شد، وصل نشد</li>
<li>✓ الکی دیسلایک زدم اصلا وارد نکردم</li>
</ul>
</div>
<div class="tg-text">تونستید به ساب جدید WhiteDNS وصل بشید؟</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3698" target="_blank">📅 20:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3696">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔥
لینک ساب جدید
https://sub.iampedi2.live/sub/mihomo.yaml
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3696" target="_blank">📅 19:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3695">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">به یاد محمد جواد حضوری.npvt</div>
  <div class="tg-doc-extra">3.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💔
این کانفیگ رو به یاد محمدجواد حضوری عزیز که هم محلی من بود و دیگه پیش ما نیست میزارم تا یادش تا ابد در ذهن من و شما خواهد ماند...
به یادتیم پسر
💔
💔
💔
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3695" target="_blank">📅 13:38 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
