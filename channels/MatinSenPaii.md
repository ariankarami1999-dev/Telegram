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
<img src="https://cdn1.telesco.pe/file/FCBKSulsz3FEnrE3X8cvoqSC_hUWGJ2foysUezhug_yQKW1pgASwxVxuKauI0BcR7-p_gDr3tV8jedGmIh3DPjsluMM4ZgaPb2NM4qErFDP-0a7zoBR_2s-47we1SMvJtf1_PZS4n58x0LNz8a91E56iL7JQjU3htPbRQv2Pb-pFLzWfqZHmlOhoTbmd8Lx0xJPeJ5pcBGfvmHuMQEBHqDasmGu5G7u5Qb_ZsBHyrEwPs_qgi5d0b2loc_NDc5ODuh7i9h1NkvI_p1162f3BypSPi0oK_JON0TRo-LFnyyDlfwbAAU8wvA8YPL36K7LjX86GUiyA3X0F9857Ixl7yg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 106K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 یوتوبر انیمه و مانگا(الان کمی شبکه؟!) - برنامه‌نویسِ ایده‌های باحال•YouTube:http://www.youtube.com/@Matin_SenPai•AniList:https://anilist.co/user/MatinSenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 04:50:21</div>
<hr>

<div class="tg-post" id="msg-3062">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">masscan.rar</div>
  <div class="tg-doc-extra">1002.7 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3062" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Last side:
متین جان اینم نسخه gui مس اسکن خیلی کار کردن باهاش راحت تره
قبل شروع اسکن باید winpcap-4.13.exe نصب بشه روی سیستم(سرچ و دانلود کنید از گوگل)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/MatinSenPaii/3062" target="_blank">📅 01:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3061">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai.txt</div>
  <div class="tg-doc-extra">1.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3061" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر بسیار پرسرعت Masscan برای اسکن آیپی‌های Akamai:
یکی از دوستان این رو نوشته و خواست بدون انتشار اسمش منتشر کنم این رو:
متین اسکنر سم و پینگ خیلی کندن
از masscan استفاده کنن چند هزارتا در ثانیه اسکن میکنه، من راحت تو ۵ ۶ دقه ۹۰ تا آیپی پیدا کردم
دراپ ریتش ولی رو نرخای بالا زیاد میشه.
کپی از چتای خودم:
چجوری اسکن کنیم؟‌ اگر masscan داشته باشید خیلی کار راحته صرفا این دستور رو بزنید:
sudo masscan
2.16.0.0/13
-p443 --rate=500 -Ss -Pn
جای اون رنج هر کدوم از رنجای زیر (رنجای آکامای هستن) رو میتونید استفاده کنید:
104.64.0.0/10
23.32.0.0/11
23.192.0.0/11
23.0.0.0/12
172.224.0.0/12
2.16.0.0/13
23.72.0.0/13
172.232.0.0/13
184.24.0.0/13
23.64.0.0/14
ریت هم می‌تونید زیاد کنید
https://github.com/robertdavidgraham/masscan
این خود پروژه
ویندوز هم داره
کل رنجای آکامای هم اتچ کردم با فلگ
-iL
میتونی بدی بهش
همشون رو هم ۵ ۶ ساعت بیشتر طول نمیکشن (خیلی زیادن)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/3061" target="_blank">📅 01:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3056">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompatterniha</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">psiphon-helper-force-fastly-1.json</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3056" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">چند کانفیگ سایفون‌هلپر متصل.
تمام اینها صرفا با تغییر ip یا sni در کانفیگهای
force-fastly, force-akamai
که در
https://t.me/projectXhttp/354790
قرار داده شده بدست آمده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/3056" target="_blank">📅 00:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3055">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">برای اسکنر آیپی که خیلی‌هاتون پرسیده بودید دایرکت، ساده‌ترین راه اینه توی ترمینال(چه cmd ویندوز چه ترمینال termux) بنویسید
ping
20.20.20.20
(آیپی مورد نظر)
حالا اگر اسکنر هوشمند بخواید، میتونید از پروژه سم استفاده کنید که اصلش برای کلودفلره، اما میتونید کلا لیست آیپی بدید اسکن کنه:
https://github.com/SamNet-dev/cfray</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/3055" target="_blank">📅 00:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3054">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یکی از بچه‌ها(abol) گفته بودش که:
از وقتی سرتیفیکیتو نصب کردم رو سیستم
دیگه نت سیستم به کل قطع شده
هر چی میگردم راهی برای حذف سرتیفیکیت پیدا نمیکنم
و این شکلی مشکلش رو حل کرد:
ریست شبکه در ویندوز گاهی همه فایل‌ها رو پاکسازی نمی‌کنه. این دستورات رو در حالت ادمین امتحان کن:
توی منوی استارت تایپ کن cmd و روش راست‌کلیک کن و Run as Administrator رو بزن.
این دستورات رو یکی‌یکی وارد کن و بعد از هر کدوم اینتر بزن:
netsh winsock reset
netsh int ip reset
ipconfig /release
ipconfig /renew
ipconfig /flushdns
در نهایت سیستم رو Restart کن.</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3054" target="_blank">📅 20:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3053">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دوستان من، خیلی ممنونم بابت حرف‌های پر از مهرتون
🥰
خیلی خیلی زیاد خوشحال شدم از دیدن اینهمه پیام‌ زیبا
🌱</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3053" target="_blank">📅 20:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3052">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوستان من، خیلی ممنونم بابت حرف‌های پر از مهرتون
🥰
خیلی خیلی زیاد خوشحال شدم از دیدن اینهمه پیام‌ زیبا
🌱</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/3052" target="_blank">📅 20:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3051">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اگر حمایت‌های پارتنرم نبود، مدتها پیش سلامت روانم رو از دست داده بودم حقیقتا. و اصلا بعد از دی‌ماه نمیتونستم هیچ کدوم از آموزش‌ها رو استارت بزنم و شاید از مبارزه ناامید شده بودم. تشکر ویژه از شما، بانو
❤️</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3051" target="_blank">📅 19:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3050">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خب گویا آی‌پی دیفالتی که پشت جیسون بودش رو زدن. مجددا موش و گربه بازی سر آیپی و sni تمیز.
Pypi رو زدن،
خود
python.org
بذارید باید اوکی بشه. همینطور از آیپی های این پست استفاده کنید:
https://t.me/MatinSenPaii/3040?single</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/3050" target="_blank">📅 18:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اگر حمایت‌های پارتنرم نبود، مدتها پیش سلامت روانم رو از دست داده بودم حقیقتا. و اصلا بعد از دی‌ماه نمیتونستم هیچ کدوم از آموزش‌ها رو استارت بزنم و شاید از مبارزه ناامید شده بودم.
تشکر ویژه از شما، بانو
❤️</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/3049" target="_blank">📅 17:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dhl8n2QWGBDIJO9mJa9WROfH-SG6Oj_zjtVqaPCSe07LZPqoQvrcQOTq6qUDkLCZJE0-HBN1ilM8FtCf4w7Aq5Ni0Sg385wXusq6PvDfJ_FX9yufeLhk-dsrrArBgStT1BJGbNoMOz562QfF5ZdFGhbth0fGwz6gw0Ylm_lWJWTVrcJfkSodVnAuX9EnvdTCzFvHs50D6d75PAhrwPwnMuh36Ir5bwIjAw7TIx4LPJD8alOto9vcqQFQR_HuJKMZG3dg020pWv12SbTW7Lc5PbUOzhTaCJQOI_Bta4bla9G9k24f8H5GjIIAoZrh3Hp282GaxJMmzICipF6NiqEMXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Kharabam
:
وقتی رو سایفون ویندوز upstream proxy ست میکنید دیگه اجازه انتخاب لوکیشن نمیده برای دور زدن این محدودیت ریجستری ادیتور رو باز کنید برید به این آدرس
Computer\\HKEY_CURRENT_USER\\Software\\Psiphon3
و EgressRegion رو ادیت کنید و Value data کد هر کشوری که میخواید بهش وصل بشید بذارید</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/MatinSenPaii/3048" target="_blank">📅 17:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3047">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اگر به ارور Upstream proxy میخورید، یعنی پورت رو دقیقا اونی که توی ویدئو گفتم ست نکردید. یا توی بخش مناسبی نزدید. باید مو به مو چیزایی که گفتم انجام بشه دوستان</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3047" target="_blank">📅 17:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3046">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">روی ویندوز از این آموزش استفاده کنید:
https://t.me/MatinSenPaii/3035
روی اندروید مستقیم وصل میشید با این اپ:
https://t.me/MatinSenPaii/3038</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/MatinSenPaii/3046" target="_blank">📅 16:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">Matin SenPai
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3045" target="_blank">📅 16:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3044">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MVVEYkYD5ZMn8pKciDdgm0eChY0u6AY8T78dSZZPEaE48VoH52UXECAJ1hYxoA0TUIkmGPwqEVltJcV_SxRvcgICmGyjLIS8OyOtn_zr4Qxa_JAE4UI8WXsPL1BHpLby92EX9kKP6ae077x5LfcteQZUnC8YXRnQ0YgbozvclxfHum6GVZJ1IQoS-oDBfhn0mYvl4CEZIfs5l0t30tMkC8BhNdwmhLMKNd6QmGNM5imZtsB3LNvciAjuO1ZFd7bExxETAx2Pgs-dKM8Ovkwnuu0rHJ1EgYdizkJcsnbKl-vzJJxBrnJAUSKzx1rI_WQRePiyj4wdMww-GMkwyH-wTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/3044" target="_blank">📅 16:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3043" target="_blank">📅 15:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfB7LUfdEq1cf1Ty6_Bt-pJXelkbQjhEs9hRXfJZMKXRMRfEy56SJ6bQO4A0HdPYjvsRuqXdDmqp-eLhDWR75KsqeiZ2ZTRKbCAc-tiIXvwIXwYwfPq3cCIcKqnLU4OXr4vmAZZzDuTJX18gtNNnpvWEYaOnNJbY2NxMDsSlBEUl7fgebuqndYV-zTiR7pZ76ZGiHAi_ZdyVAwqk-T9fWeSnTgwo2m17_0vcM22ptlQwb4jFgRYx2L6LdBUEe9cOVkG1iiFTPG7OblFVq7mNlIms6rjFzMcrvUNIzzWVU1wNLgvEgP1Ik0nVjJERbISkG0xpd3O8l7JdiT9kNnryBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/MatinSenPaii/3042" target="_blank">📅 15:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3041">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3041" target="_blank">📅 15:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hJ04RVmnTpiAVwG_0vkeJbbodGPCZqOBfftsIkAu27l-CJ_LlDmqU21re-e5z2elfgoZPmxKbC_S_klwORWqERyaf1mnyT-Of7kcYJNfUSYbHUFqoWhtNP5N1StCEJ5uVqHgyos256g6r7q4RM-GY9jfyd5LtkhQr7c4jJ8K7NH9JYrBWY-rqNRygY84MrkzovPDSRbS4jAYmO2L0Eyp1wRy_XNVS6d0Gjjtj96Ii74xnmv6_zSIeI6HAMVLyU3RYCpbveO9uCeAeXj673bSiVTepnFpP3PJ7f-EbskAuhoTEc_JMX10Dbf5p77euljkoUK_MFe1hxwugh_FscRYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rJLqQQtAF_xZMVD1zGskOoOYrlBOxelriXF7VoqOXz6YtQYeGDME0F-r-WLFt-TzCHAdLgAp02H0koSfvKfpZuEld1vRCO1jSBweEiitlUFh4C4JJ1UwzfqZBazSKrcd8UlTj9wmN3qo9ZVhiMleC3kF9BvPMOoWu7hh_r76fOeLHRbOOMrG8px4Mt9JGOfdOZ-SgYVUailLa91nWdHGL-7cTcLKkoIr24kpyQN75jE0sIRnRjjlZ8e7YjdZbIpbCxR8muiQ5K8mqUY-PNQ1uHJkrAsjak0I_LQ7Pd9oP3D_Yk7iuGpa7b1nag39nxyqfKw9nCYMN7VOS15RlCG--A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ShirOKhorshid-2026.05.14.apk</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/MatinSenPaii/3039" target="_blank">📅 15:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3038">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3038" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🛡
مهم: اگر این نسخه رو نصب کنید دیگه دردسر ستاپ کردن MITM و... ندارید!
این نسخه حدودا یک ساعت پیش توسط برنامه‌نویس شیر و خورشید آپدیت شد و به راحتی می‌تونید طبق این آموزش بهش وصل بشید:
1- وارد اپلیکیشن شیر و خورشید(آخرین نسخه که امروز منتشر شده) می‌شید
2- وارد بخش Options میشید از نوار بالا
3- روی More Options کلیک میکنید
4- گزینه‌ی  Connection Protocol رو قرار میدید روی CDN Fronting
5- میرید و عادی کانکت میشید و به راحتی وصل میشه!</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/MatinSenPaii/3038" target="_blank">📅 15:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3037">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حالا دیدین متد ترکیبی سایفون افسانه نبود و واقعا وصل میشد؟
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3037" target="_blank">📅 15:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوستان عزیز، خواهش میکنم به DNS بها بدید. معلوم نیست کی مجددا متدهای حال حاضر رو می‌بندن. از نرم‌افزار و آموزش‌های
@WhiteDNS
استفاده کنید و الان که اینترنتتون شاید اوکی تر باشه، نصب و ستاپ کنید</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3036" target="_blank">📅 15:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/MatinSenPaii/3035" target="_blank">📅 15:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چه حالی میده رایگان وصل بودن
📚
از زمان SNI Spoof اینو تجربه نکردم خدایی</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3034" target="_blank">📅 11:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3033">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بی‌زحمت لینک سایت‌های داخلی برای آپلود(هرسایتی که میشناسید اوکیه) واسم بفرستید، تا زمانی که ویدئو حاضر شد واستون همزمان به همراه کلاینت شیر و خورشید و فایل جیسون و ... روی چندین جا آپلود کنم:
https://t.me/MatinSenPaii?direct</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3033" target="_blank">📅 11:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3032" target="_blank">📅 11:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">قطع و وصلی داره ها، اما هر 5 دقیقه، 10 ثانیه قطعه مثلا
برای گیم شاید عالی نباشه، اما وبگردی، اینستاگرام، تلگرام، توییتر و هوش مصنوعی‌ها همه اوکین</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3031" target="_blank">📅 11:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3030">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IKKYNd_wdech2aSA6iVF_ra-m8KwOP6arUjd3N70zXrR4_qAGnbYS_xUvUs8-8aMExOH90VvIcSTGYf8L9vOFhTpriN4fJ3CBbdB_zrOpObRMQkgjfgdhM_EjOOInCtzdmMmPb_Mf7JrykOMfL79pdh1ZKVyOLVO5F8XC_1xuucCoFFJ-eQmNJfVoOYRcXsdZo4zkm2JnY-Bh7bKZgwH7ok05X0hpw6smif7IwptKp0RQ9B8MvRiHYmjgmGkqxw9xa5Dptq3cYYduxi6LkWApWUKf7l7UjYV9b_HubBCd8wcD3uZn7dgSvRBhsnHj4l59nHWlPDyaahqw1B7oh-rKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم روی گوشی(تمام باگ‌ها و مشکلاتی که توی گروه‌ها گفته شده بود رو در آوردم و دسته‌بندی کردم و خودم امتحان کردم)
این پست هم با همین متد داره فرستاده میشه
🕶️</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3030" target="_blank">📅 11:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3029">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rjRkGyp2aRMBqRT5jQca_M0yDxd5_r4X6APGfarVIhlP9SaV6j9HBmXlxxSf9vDEBaXljdpoNBRkai-vxqGRFc2PhT6jFnffOb7Hb3kjXRfXb6ptb1CRnaItRbRHxSsR6hWjyePEOL99w-OpPyS3qUV0nB4NMX9OSuR930qMUmXTFZh9dTum063r8qPSZ8CQhTUyZ6cw0qzWHRaGtmuu2P_VW8hnT5LIEVNjR1hh9VUPA2fXqL-_H2-iHa0XVuTz3HBnpBl7fH67gOQqNuMiAoOf8ZPAsblNIz5WdFs-nW6p3Hlf6oSPK5jw4qJLlWG99P081VOcH_brLhOPpGS4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای یه روش کاملا رایگان، بدون نیاز به سرور، بدون نیاز به اکانت گوگل، بدون نیاز به شماره حساب خارجی و هیچی، سرعتش عالیه. آموزشش رو می‌ذارم واستون. خیلی ساده‌ست
با تشکر از
@patterniha</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/3029" target="_blank">📅 10:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دوستان عزیز که با اپ میتونن وصل بشن اما چیزی براشون لود نمیشه.</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3028" target="_blank">📅 20:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-_--qwS2uaahMOZKg6Q3tjQ-lBwd8nuFiWzeYdWrNy73EUkNkg7fHh_Sk_PVaHc5NSqvP_KdFrMI8JrE1JSE0nv3OLxKzb2Teomq0ZjoX-MW-lNRH6TSXI3NsWGxnYuroBRLs8y3rtHJ1YOkrmBuqNap2LhUQyPtkpbarU83XpReQrX-VMglJISiAKSt77t482AmbiztSGV2rMLvabBikuLbKKDypzQcM5ewR88OFciiMRmKdif15k5YmcQJ7jZZ8EZacBXt1l-2hvjEMIjr5NK7kGYj369tlsc-3xbdr1V_Hyz30HfjLc_CjmZ5Z8knQLghbBjLWq3RZsHRUSrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امکان دانلود کل ریزالور ها به ربات
@dns_resolvers_bot
اضافه شد
@WhiteDNS</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3027" target="_blank">📅 06:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3022">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره. اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/MatinSenPaii/3022" target="_blank">📅 23:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره. اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/MatinSenPaii/3021" target="_blank">📅 21:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره.
اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم صرفا این محتوا رو دوست داشتن، نه اینکه شخصِ من رو دوست داشته باشن.»
و اینجاست که مغز ما رو به بی‌راهه میکشه.
متأسفانه عموماً از اون لحظه، شخص دیگه حرف‌هاش رو برای بیان نمیگه، بلکه برای حفظ اون حس میگه. و همونجاست که گم میشه و مسیر رو کلا گم میکنه.
به خاطر همین هم هستش خیلی از افرادی که این روزها وایرال میشن، بعدش چیزهایی میگن که ممکنه ازشون بدتون بیاد. توی فرهنگ عامیانه، می‌گن طرف جنبه‌ی شهرت نداشت؛ ولی واقعیت علمیش چیزی بود که خدمتتون گفتم.
اگر وایرال شدید، خواه ناخواه دوپامین کار خودشو میکنه و حس خوبی دریافت می‌کنید اما مدام حواستون به این نکته باشه(همونطور که منِ متین حواسم هست) که این صرفا یک عدده و من تغییری نکردم.
پیروز باشید
✍️
Amir Mokhtari
با کمی تغییر از سمت من</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3020" target="_blank">📅 18:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAbwZH2F53O34XJyifFjkOXvwNA1IoTv16zf_kpmx5cTt6TrKe1exDipBiFFNHIXROff1UzzdaZMdcHF7KrROEH5GW4n7jkm2e9rvZ-A7HZTmyqP03bt7UayiBdvwbTwkJW2W7UccPm3x51cP5BwaM5l5JhWTKRihat_8TR3s9fubhSIxl0pbgi_-xdcsnUyuaRZzcRKxDw4YYMDG11YPpClFdvYRn2Kyytu9T2HkIIcd5VX_14i-VXBSzS-wA371twZbBC5YpBw1SsFiMBXpBxkkpeurbnbozExmXPDoYumwA_BCMHIOcS8qmoLc_BKOZANqEDcsdKci__In49jrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IRCF | اینترنت آزاد برای همه (Twitter/X)
🍷
اپ متن‌باز و
#رایگان
TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
لینک پروژه:
⚡️
http://github.com/MaxiFan/TunnelX/releases/latest
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/3019" target="_blank">📅 17:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzioXyh1wUNPHFZ1kxOE_nBoAd6ohbOvwhlHjCqEK6OYz7eUFpt-l7_DmB0rsVXH_oG-2iTKRrSS4mjopRPwEhqlxk-VW1nnyRxfRncz1Ar6t_o-lL-tZATPpRDv1GHhWgl8iXFu9LCR9FromxtghdV5I8XO6etUAjbEo8SlcrkaB7OaR30z4fCe1g8RO5RAyn8ygYW3ANJjYZ84OqckgkRthLRX-OfQhzEccr0p-DRxUJVXpsRZQczfa8ZOpIoLe_no7EHrq6VI3qGtHm9N8yAmu8DqsiU4gDupCipsMTquXMWHuGJny5YoKj-WRo7okpbgY3wG8FaSfzD80GY6Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای دریافت ریزالورهای MasterDNS / StormDNS در WhiteDNS
ربات WhiteDNS حالا امکان جدیدی برای دریافت ریزالورهای MasterDNS / StormDNS دارد.
برای دریافت لیست ریزالورها مراحل زیر را انجام دهید:
1️⃣
وارد ربات زیر شوید:
@dns_resolvers_bot
2️⃣
دستور زیر را برای ربات ارسال کنید:
/dns_master
3️⃣
بعد از نمایش لیست ریزالورها، برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید.
4️⃣
لیست کپی‌شده را داخل اپلیکیشن WhiteDNS وارد کنید و از آن برای اتصال استفاده کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/3018" target="_blank">📅 17:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3013">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3013" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
تمرکز اصلی این نسخه روی بهبودهای داخلی VPN در خود WhiteDNS بوده است. هدف این بود که اتصال کامل‌تر، پایدارتر و مستقل‌تر شود تا کاربران برای باز شدن سایت‌ها و اپ‌ها دیگر نیازی به NekoBox، NVPN یا راه‌حل‌های مشابه نداشته باشند.
در این نسخه مسیر DNS و ترافیک داخل خود WhiteDNS بهتر مدیریت می‌شود، بنابراین تجربه اتصال ساده‌تر شده و کاربر می‌تواند مستقیماً از داخل اپ وصل شود.
✅
نسخه اپلیکیشن به 1.2.0 ارتقا پیدا کرده
✅
حالت Full VPN کامل‌تر و پایدارتر شده
✅
حالا DNS هم داخل خود WhiteDNS مدیریت می‌شود
✅
دیگر برای باز شدن سایت‌ها و اپ‌ها نیازی به NekoBox، NVPN یا ترفندهای مشابه ندارید
✅
مشکل وصل بودن VPN ولی باز نشدن بعضی سایت‌ها و اپ‌ها برطرف شده
✅
اتصال روی اینترنت‌های کند و Resolverهای دیرپاسخ بهتر کار می‌کند
✅
صفحه اصلی ساده‌تر شده و انتخاب سرور، Resolver و نوع تنظیمات راحت‌تر انجام می‌شود
✅
اگر سرور یا Resolver درست تنظیم نشده باشد، اپ واضح‌تر نشان می‌دهد چه چیزی کم است
✅
می‌توانید تنظیمات پیشرفته را با نام دلخواه ذخیره کنید
✅
امکان ساخت چند پروفایل تنظیمات پیشرفته اضافه شده
✅
می‌توانید هر زمان بین پروفایل‌های ذخیره‌شده تنظیمات پیشرفته جابه‌جا شوید
✅
امکان برگشت سریع به تنظیمات پیش‌فرض اضافه شده
✅
بعد از اتصال، نام پروفایل سرور، Resolver و تنظیمات فعال نمایش داده می‌شود
✅
امکان خروجی گرفتن فایل client_config.toml از داخل اپ اضافه شده
✅
ظاهر صفحه اتصال و دکمه Connect/Stop مرتب‌تر و جمع‌وجورتر شده
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.2.0
از همراهی و حمایت شما ممنونیم
❤️
1⃣
WhiteDNS</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/3013" target="_blank">📅 17:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JkRmE6BxvcRz12JcZO2naOV5qv0AIsWk93LTA6zERoeZ58aIFNOxCf5NU7H0lAng-zSlu6ubHTNe7Gx0_u0leSiKtTbuPLKVqLxhXrvTsPOlkiAwuMMXQW3-fWnGd4yIOv9EtjBAs5PCSBuSvAjxDcRzibFzwHUmeOVGQYioPcZSzRhSix2QezLQc1BtiDyU8Z35QqmDc8U69WReRKam53i4mp4Ofregqvy07ZtR6PrnseO7pXSomOAJWlDE56ixyXIAjdbSjM08XuoVPK39n1iOGI2FgAkF7_AiCY5jDRIqCv4LYd-dVoqU-55T3XKYuEsFXYTCuGnyAgFURzB25A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bk0LdWP-1Xi1Lym_UHug6VqRFLoNbjD8jhYvYhV1orzcit2X61pVWCQXqKdaGZzWSWsThzosTqtuOmrv6kRAGWiBPzHt1yOpZYXTE0zUy7yuicxOYMQRbIFXWghFy6Iug6469aBZ1Vk6eTazToIHwvhvEboOz5J-k2DyKyQtNoTSm-xWydpgiZYW_n5yJEpvDDXVLAe5q-v01Xe-SEL9FSuAvlJ5rS2HKITByVEtssBledBMn56zS2qt4Szt-MZ8fJ2zEi3q0SODobi8Psj_wkY1ErUSTDxilKvYbuxRdESmZp3huvZJDieOSFsa_oybbC6NjHpN3qCcnGCzV0XKuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی یه آموزش بر پایه‌ی DNS داریم. یک دونه رایگان بدون سرور، یکی با سرور.
به همراه آموزش پیدا کردن ریزالور
با تشکر از بچه‌های تیممون، WhiteDNS
(توی این عکس با سرور رایگان وصلم)</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3011" target="_blank">📅 23:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">من تازه دیدم که یک نفر امروز صبح 500 دلار دونیت کرده به wallet های روی پروفایل توییترم. و هر کس که بوده، واقعا ازش ممنونم
❤️
کمک بسیار بزرگی به ادامه‌ی فعالیت و همینطور دلگرمی هست برای من توی شرایطی که درآمد یوتوب قابل برداشت نیست و شرایط اقتصادی داغونه. اگر…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3010" target="_blank">📅 23:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پول پارو کردنی در کار نیست. این پول‌هایی که دارن می‌گیرن بیشتر واسه جبران ضرر و damage control هست که بتونن یه مدت بیشتر قطع نگه دارن.</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/3007" target="_blank">📅 09:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فیبر نوری مخابرات کلادفلر وایت لیست شده ظاهرا.. امیدوارم بازش کنن ناموسا بریم دنبال زندگیمون</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3006" target="_blank">📅 09:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3005">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromfarzad</strong></div>
<div class="tg-text">متأسفانه همه راهها رو معنای واقعی کلمه بستن (غیر از mhr که اونم نصف و نیمه و داغونه) وشما به هر نحوی بخوای به نت بیرون دسترسی داشته باشی باید هزینه زیاد بکنی ، یا بری نت پرو گیگی ۴۰ هزار تومنی بخری یا وی پی ان گیگی ۱۵۰ تومنی مثلا یا بری سرور بگیری cdn بخری وdns بخری و .... بازم هزینه گیگی بالا میوفته ته همشونم پولش تو جیب خود دولت و سپاهه همه ی اینا</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/MatinSenPaii/3005" target="_blank">📅 09:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آقا من نمیدونم این چه وضعیتی هست که درست شده توی این کشور !
هر چی میاد میگن پاپلیک نشه ! شما متوجه هستین مردم بیشتر از 60 روزه با این قطعی نت مشکل توی زندگی ش پیش اومده ؟!</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/3004" target="_blank">📅 08:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3003">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رفقا من متد‌های حال حاضر رو میدونم. بله میدونم که CDN آروان چطوریه داستانش
منتها برام معقول نیست آموزش دادنش. نه هزینه‌ای که باید واسه‌ی CDN داد منطقیه و نه پابلیک بودنش. اینم احساسی که بهش دارم مثل Shecan هستش. یه Back-Door توسط خود حکومت که خب دست خودشونه.
مثل گوگل نیست که بهشون فشار بیاد که باز نگهش دارن. اگر اشتباه میکنم من رو متقاعد کنید</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3003" target="_blank">📅 08:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3001">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromペコリーヌ</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qo829_Pn2NguzneffC2S-Fud6z6MM6CF9DUx11QEji0duFdrpOEYAWoJFtGirGdEbVC8XwAHeMKuy5wSMBV0x-yqjKKlRwZF9jyoCG2OQMGJ1HLyJSUf9tHEa3YEMNpGnPbw8K433-YTAo73fPwveYjT6nf775GOEpmjEKc99NAp4P_YSsbw7v2QYDeF3psfVBrCRtLkRKH-gmrAjpAa_uW9wYtWQCv0By0DI5iCg-pc64pTLWshMnr_sQ-AlygTmn6d1gDXF_WSaUefX7bxMEmXxxqrl4-DHXS6b9xKQ_gSQnhJ_xeXZS-chaMpIX53cvKaHo7LkOuC_ujXN3tX_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JuzwqaqQX6bIFKhp8hwq3YYBqCa1AEdxtZtlTBlkARqra0R8BKrU3OX3kE2pWOLuzzjMckjw1OOfDu3TCmmzenNLgi2IKTRvDSPXijtAByCUOObNFhLU26_uOczbCUf3zB5SCrwyDccEXGuRkkMsmTCRvRf8kWkO4u6Ojcucp-WrOa2m4U3QqATxcTy0OhWASPKGWKEHH7OZ70m7fvNZZu8oPzpPiKvu2xu024iL7p4zPCyMrzyoCbU9ZQtch21w0yxhmtjRWxkZM3oZHGU_Zq51vfWxOYYg2tkusfOzHNFl1UgTDfrjz9jpv9d0CczrBAz5XtT-3Jlhd4ixjHzQRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واسه ۸ گیگ اکانت رو بستن ؟!</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3001" target="_blank">📅 20:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اینا رو سرور ایرانی شکن فعال کردن روش vpn زدن و کانفیک میفروشن، طرف در عرض چند روز یک ترا ترافیک رد کرده مشخصه مشکوک و پیگیر میشن</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/MatinSenPaii/3000" target="_blank">📅 20:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نقره ای دارم یه ماهه استفاده میکنم راضیم چرت و پرت هست این</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/2999" target="_blank">📅 19:28 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GWQAyD4eSboqYWv9QgvfFbMiKVi3bzPIqNnz-96S9TkdPW0m-dxmiLfsenV_JnKFihBSbvH6j1pU8Y7DrqoUnhkr8hpbXCnTUJ9cazk9bREQGzr2AVCccPzejRwXRYEv3L7YhZO3htI7tJSy3okfR-PGXHZ2jPAXqZBWRn2GJqkyOOOCIqY2C7JatCLKb-JiBAF0Ab1R69kSiIBRUfpEVJ_KVTUwfaJX1Eo3aeIJZL8qnTm5jU4IiKQBib2JjX0ZA0WVPun0-Nh-sPaoBiFmcNRARp4e3CW8b2MWNHsKl5sGUObiRJD25YhcFsuoZb-06lsFbX_4AxqpLcx8Y6cWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول به "شکن" و امثالهم هم ندید. یادآوری کنم که چند هفته پیش، به مدت دو سه روز chatgpt روش باز شد و ملت کلی اشتراک خریدن و روش کانفیگ ساختن و باز مسدود شد. پول مردم هم رفت سطل آشغال</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/MatinSenPaii/2998" target="_blank">📅 19:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2997">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">من این تایم 70 روزه رو خودم 5-6 روزشو قطعِ قطع بودم. اما با اینکه توسط چندنفر بهم آشنا و پارتی از زیرساخت معرفی شد(از فعالیت من هم خبر نداشتن و سر آشنایی بود صرفا) باز قبول نکردم همچین چیزی رو و توی تاریکی و قطعیِ کامل در حالی که لپ تاپم بیست-سی ساعت بود داشت dns اسکن میکرد به دی‌ماه فکر می‌کردم. اگر چند روزی دیدید که من نیستم، بدونید قطع بودن رو ترجیح دادم و یا Dns رو هم بستن عزیزان. کسب و کارها یا نابود شدن یا رو به نابودی هست. هر روز کلی پیام دریافت میکنم که من تدوینگر/هانتر/دیزاینر/فری‌لنسر/برنامه‌نویس/... بودم خرج زن و بچه میدم و تمام درآمدم از اینترنت بوده و لطفا یه متد معرفی کن بتونم وصل بشم و من باید با شرمندگی این جواب دردناک رو بدم که هیچ راه معمولی‌ای وجود نداره برای وصل شدن با سرعت قبل.
اما چه کاری میشه کرد! جز نگه داشتن امید و صبر.</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/MatinSenPaii/2997" target="_blank">📅 21:17 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سوخی با همچین موضوعاتی چیز درستی نیست</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/MatinSenPaii/2996" target="_blank">📅 21:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آهنگ (هفتاد روز که من از تو خبر ندارم) ایرانی</div>
  <div class="tg-doc-extra">•(Ali....Amin)•</div>
</div>
<a href="https://t.me/MatinSenPaii/2995" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مردم ایران خطاب به اینترنت
01:00
🫩🫩🫩</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/MatinSenPaii/2995" target="_blank">📅 20:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آمریکا هم عجیبه
ما داریم زجر میکشیم از نت اونا هم اسنادشون رو منتشر کردن راجب یوفو و بشقاب پرنده
https://www.war.gov/UFO/</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/2994" target="_blank">📅 20:02 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2992">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد Advanced Settings شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup:…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/MatinSenPaii/2992" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2991">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuSztmVKY3-Pe7qUODMo9n6ZUH3kBjwIzfXXWsbbSsU6QmM4O97k70tiK4TDTvfnE0gATcOnOlWNC0RLgQmQj0wG80Fht75yOju4XB_zhEU54yAGmGvv2IXMjm3JyVNZgCCpn5sKZFeNR_CvwZYS4XPt6Q8u-CWBuyAOMqmNQop2HIBPu9_Q3jdM2pmYBYFZLRiZCcgaiXaxYPQ25Ut2bPk2yF7buoQF7EsQcEKczOdeRQYE1tV3Sz0etQnleB__8pm-S0S3LNW-wk4OB6vSvkXgu8cVQy5-dYKK3h6qPX7r4vcyO8tMYvK-P9SSoCgtz38agwetuldRX-hqEq9llg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد
Advanced Settings
شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup: 1
🔸
Download Dup: 4
🔸
Upload Compress: OFF
🔸
Download Compress: LZ4
📊
این کانفیگ به‌صورت حدسی انتخاب نشده.
ما لاگ‌های سرور در ۷۲ ساعت گذشته را پردازش و بررسی کردیم و بر اساس پروفایل‌های موفق‌تر، MTUهای پایدارتر و مسیرهایی که سرعت بهتری داده‌اند، این تنظیمات را پیشنهاد دادیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/2991" target="_blank">📅 17:24 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2990">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">thefeed-android-v0.17.4-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/MatinSenPaii/2990" target="_blank">📅 16:40 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2989">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.17.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/2989" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
thefeed-android-v0.17.4-arm64-v8a.apk
📊
Size: 8.9 MB
🔐
SHA256:
466659489e5429db20710d85241012002aec644cb739220338b9dd6aef186fe8
نسخه جدید TheFeed (v0.17.4)
🚀
🟧
تغیرات بخش اصلی
:
🔸
نسخه IOS بصورت ipa در دسترس هست، اگر بلدید خودتون ساین کنید و تست کنید بهم خبر بدید که چطور بود (دارم تلاش میکنم بزارمش روی تست فلایت تا همه بتونن نصب کنن)
📱
🔸
برنامه زمان اجرای اول زبان رو میپرسه
🗣️
🔸
فیلد جستجو فقط با یوزرنیم جستجو میکرد، الان با اسم کانال هم جستجو میکنه
🔍
🔸
زمانی که اسکرول کنید مثل تلگرام تاریخ پست رو بالاش نشون میده
📅
🔸
اضافه شدن بخش حمایت مالی
❤️
🟦
تغیرات بخش کانال های دلخواه
(TeleMirror):
🔹
دکمه نمایش پست های بیشتر به بالای اولین پیام اضافه شده تا بتونید میام های قدیمی تر رو هم لود کنید و ببینید
👀
🔹
قابلیت باز کردن عکس ها
🖼️
🔹
قابلیت تغیر سایز فونت
📝
🔹
نشان دادن ای دی پیام ها
🔢
🔹
رفع مشکل نمایش فایل تکراری
🗑️
🔹
دکمه برای پریدن به اخرین پیام
⏩
کانال اصلیم:
@networkti
کانال کانفیگ:
@thefeedconfig
لینک دانلود نسخه جدید برای تمام سیستم‌عامل‌ها از داخل ایران (با گیتهاب):
https://github.com/sartoopjj/thefeed-files/archive/refs/heads/main.zip
📥</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/2989" target="_blank">📅 16:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">به نظرم اولین اقدام دولت این خواهد بود که یه لگد میزنه به Google و ما، و MHR قطع میشه</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/2988" target="_blank">📅 01:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این کار «زدن و گردن نگرفتن» واقعا رو اعصاب‌ترین بخش جنگه
کی اینو بهتون یاد داد اصلا</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/2987" target="_blank">📅 23:20 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U0UswebsKo9UCh3SjDz65n5fyO7Ogk71N6UWXb9omA4ew30uq_BNCRcwKZWyjthJv9dacAQyJXnlL89I3-o3qfd2nTiU0ytcCllk-Grz6dUbe5bV3s_1RVyXoerZUreQyWB5iPfbGdGNyxWp6R-UKeU4B8bq3X8y1dS7bVGvmplOrLES2g2k3Sk-SQKRwl_JILAvZURylG6TUVTZFJ7sGhJEkGHcqaA_8Mz5rl-Ry422rdU0Hcp7GyszqIdBubqK2s67oXRCXCNLNBvy0LyYQzZ6LJe633r0YjKiYA1KuFcSH_9SGjW4YDyyO3RZJrIIlhftUu2BZA2BNCbEX8FUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچه سریعتر اکانت مایکروسافت ویندوزتون رو از مایکروسافت به Local تغییر بدید تا این بلا سرتون نیاد. همینطور علاوه بر پین کد، پسوورد هم تنظیم کنید و راه‌های دیگه‌ی لاگین.
من دو بار به این مشکل خوردم و متأسفانه تنها راهی که پیش بردم این بود که از طریق Advanced Troubleshooting رفتم و ویندوز رو دوباره نصب کردم(فقط اپ‌های روی درایو C پاک میشن و بقیه درایو‌ها و همینطور پوشه دانلودهاتون سر جاش میمونن)
اینجا یه ضربه‌ی وحشتناک خوردم و اونم این بودش که مجددا بعد از چند روز قفل شد و روز از نو روزی از نو. که فهمیدم راه حلش اینه:
1- تغییر اکانت مایکروسافت روی ویندوز به Local account
2- حذف پین کد(که بکاپش ایمیل مایکروسافت هست) و اد کردن password یا یه راه لاگین دیگه. بعدش مجددا میتونید پین کد هم اضافه کنید
الان سه هفته اینهاست که به مشکل نخوردم دیگه</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/MatinSenPaii/2986" target="_blank">📅 22:44 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2985">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eW3Bw8SlhNUGk_veLcJUadgFA7nCZK9rsLi4lOtA4RqYs_IUiL6H_OticE2B1slVS8hunCc92ks0BKvq_8tHnPn27Dc-Q5PUA1R8qc-5HBKEEzH9QCEbKPxg2zCyvNJ55k2Ss_e0eq_Z4GXGpikSAiLjYvYw7rUfZtD6TBDKdVP6h7P61SEVPNH8vsvgqeA0bX-Hd_YsaGqjNVLDNbGsQJCKXpwnPTFkJ_QE4tkY6CtOcI0QqBLpyGKP-lfXIDSJYYxP3mm8F-v_tBVMFdFmipV5wrTD9O6tqvlp3WFIl2lm976DZOXdsajV_Ok-96Ic9anR-6DzSXSw56Cwyi24zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان فرمودن که با این ریپو: https://github.com/ThisIsDara/mhr-cfw-go تونستن مشکل کامنت‌ها و ارور restricted رو برطرف کنن</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/MatinSenPaii/2985" target="_blank">📅 21:22 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یه سریا برمیدارن Deployment id هایی که من توی ویدئو استفاده میکنم رو می‌زنن و استفاده می‌کنن
😂
من عادت ندارم اصلا پاک کنم چیزیو. و اشکالی هم نداره. فقط کلودفلرم و گوگل اسکریپتمو ترکونده بودین هرچی اکانت روش آموزش دادم
😂</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/MatinSenPaii/2984" target="_blank">📅 21:17 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dBukHdI0NVzVqiBzzNucb1OSxwTkgQctiPhflibByyLEvJnD9BaCRg-hxVcqyzOrqEC8vakelhCCltQ4Ja4Vfdld-i2GmRBskSQ3IQs1ohpKzQ0dpSjHTzkj1Ys0AQIbM9qbj-NcbFH8PWVBekRSSyy7k3xwR7dTKwKFNGQl1McKZ3Noc9KpDeP6_ivspzZB0s4_neeRY8m9AC3q2IYujOtH0AOpSIidyrXy5F3vym61sVouj2h2MZplU34HUPxJ59L2gtaQKQxtwOutd1x3GHSlwWpMWAHQrtEuATxnEu9CFPoxRZD8K-nDGnHFGzlqyvp4a_B_zMP9OBzT_QnlVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان فرمودن که با این ریپو:
https://github.com/ThisIsDara/mhr-cfw-go
تونستن مشکل کامنت‌ها و ارور restricted رو برطرف کنن</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/MatinSenPaii/2983" target="_blank">📅 21:06 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قوانین مسخره ios که نه
خارج از ایران اصلا نیازی نیست mhr بزنن</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/2982" target="_blank">📅 20:51 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2981">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اندروید نداریم</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/MatinSenPaii/2981" target="_blank">📅 20:45 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">☠️
آموزش ساخت متد MHR با گوشی + کاهش مصرف ریکوئست های گوگل
⚡️
لینک‌های داخلی جهت دانلود: https://t.me/MatinSenPaii/2969  لینک پروژه اصلی: https://github.com/therealaleph/MasterHttpRelayVPN-RUST
⭐️
توی این ویدئو بهتون یاد میدم که چطوری متد MHR رو صفر تا صد…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/MatinSenPaii/2980" target="_blank">📅 20:43 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2979">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">می‌دونستین یه نوع اعتیاد هم داریم به اسم اعتیاد اطلاعاتی؟
شما ممکنه ساعت ها با هوش مصنوعی چت کنید و خسته نشید و ولعتون بیشتر بشه برای چت کردن باهاش، یا اینکه یه نصفه روز توی صفحات ویکی پدیا بچرخید و مدام اطلاعات مفید بخونید با این فکر که آره دارم چیزای مفید یاد می‌گیرم، اما این کار شاید ظاهرش به اعتیاد نخوره اما جالب اینجاست چون دوپامین پسیو (دوپامینی که بدون سختی داده بشه) می‌ده و هیچ سودی هم نداره دقیقا خود اعتیاده. فرمول خاصی هم برای ترک کردنش وجود نداره اما مثل همه اعتیاد ها میشه با سختی کشیدن ترکش کرد برای مثال یه کتاب (فقط حتما یک موضوع واحد باشه) رو بخونید دقت کنید فقط موضوعش واحد باشه.
یادتون باشه هرچقدر هم درباره چیز ها در طول روز بخونید اگه اخر شب نتونید 3 خط دربارش بنویسید اون چیز هیچ وقت به آیندنتون کمک نمیکنه و بیشتر جنبه سرگرمی داره.
@Linuxor</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/2979" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">💬
یه سری مطالب از Repo سازنده‌ی MHR واستون قرار میدم(مربوط به این روش: https://t.me/MatinSenPaii/2785) :  اول از همه دقت داشته باشید که به روز ترین نسخه‌ی code.gs رو حتما از گیتهاب پروژه گرفته باشید: https://github.com/masterking32/MasterHttpRelayVPN/blob/…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/MatinSenPaii/2978" target="_blank">📅 15:54 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2977">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ولی من دقت کردم نه کسی پین نگاه میکنه نه سوالشو سرچ میکنه تو گروه فقط میپرسن پشت هم</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/2977" target="_blank">📅 04:14 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2976">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">به نظرم تریدرا الان باید به جای دوره‌ی آموزشی، دوره‌ی تحلیل رفتاری ترامپ رو ببینن</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/2976" target="_blank">📅 01:35 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2975">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbGM3npB0BJFL9UTFi3JcU17KFoT3Le_6v-vhjbf647qzWI3945uXi-AnaO6S53D0vJ4TZG_yJRe-EfEW69iVQ-micf_gZUIr03hhEry1YVG73A_SGB58c97ApJ_M0bH34EWAoyK6o_7dqip494crRetc3oedaChFyJ_R_WnoVGI8_lz6mJdAo_VozSvokzmFxFEaStwaSLCqN7jf4VGfvxTF0DjmdN8l1L41QzpDw0bGWybteAbkZQAf2p52kIMpoPz9Vm5eSZz2FwTbVvKABHMvueizZy8dHKXuKfy-cdZNSs5JjAptsd8j4NEeVdaaSVg9rEsT0GHnSXAWL38Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
دانلود با اینترنت ملی از یوتوب و تورنت و هرجای دیگه!
پروژه AzuDL - GC2GD یه ابزار کاربردیه برای دانلود فایل‌ها از طریق Google Colab و ذخیره مستقیم اونها روی Google Drive
با استفاده از این ابزار می‌تونید لینک‌های مختلف رو داخل Colab اجرا کنید و فایل نهایی رو مستقیم داخل گوگل درایو تحویل بگیرید؛ سپس با متود MHR فایل نهایی رو دریافت کنید.
🖥
قابلیت‌های اصلی پروژه شامل دانلود لینک مستقیم، دانلود ویدیو و پلی‌لیست یوتوب، استخراج فایل Mp3 و... هستش
💡
ویدیوی آموزشی پروژه AzuDL -
GC2GD
سورس پروژه:
https://github.com/TheGreatAzizi/AzuDL-GC2GD
✉️
@MatinSenPaii</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/2975" target="_blank">📅 01:23 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/2974" target="_blank">📅 01:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">لینک های داخلی اموزش و برنامه
📥
mhrv-rs-android-universal-v1.9.14 39.2 MB
📥
mhrv-rs-android-arm64-v8a-v1.9.14 18.1 MB
📥
mhrv-rs-android-armeabi-v7a-v1.9.14 15.8 MB
📥
ویدیو اموزش ساخت متد MHR نت داخلی 18.3 MB
📽️
﻿</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/MatinSenPaii/2973" target="_blank">📅 01:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2972">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیـ بـ خـ(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-text">لینک های داخلی اموزش و برنامه
📥
mhrv-rs-android-universal-v1.9.14
39.2 MB
📥
mhrv-rs-android-arm64-v8a-v1.9.14
18.1 MB
📥
mhrv-rs-android-armeabi-v7a-v1.9.14
15.8 MB
📥
ویدیو اموزش ساخت متد MHR نت داخلی
18.3 MB
📽️
﻿</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/2972" target="_blank">📅 01:11 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2971">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⏱
لینک فایل‌های apk با نت داخلی:  https://guardnet.ir/f/8785ed32c47c (متاسفانه فقط آرمبی ۷ هست باید اون یکی رو هم بذارم)
⏱
لینک دانلود ویدئو: https://guardnet.ir/f/c5321e5300d0</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/2971" target="_blank">📅 19:11 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2970">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یعنی انقدری که سر آپلود و سرعت آپلود توی سایت داخلی اعصابم خورد شد سر تمام  فرآیند ضبط و ادیت و آپلود روی یوتوب و  تلگرام ویدئو اعصابم خورد نشد. بهتره تایپ نکنم دیگه چون اصلا کلمات خوبی به ذهنم نمیرسه</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/MatinSenPaii/2970" target="_blank">📅 19:04 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2969">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⏱
لینک فایل‌های apk با نت داخلی:
https://guardnet.ir/f/8785ed32c47c
(متاسفانه فقط آرمبی ۷ هست باید اون یکی رو هم بذارم)
⏱
لینک دانلود ویدئو:
https://guardnet.ir/f/c5321e5300d0</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/MatinSenPaii/2969" target="_blank">📅 18:59 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2968">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">☠️
آموزش ساخت متد MHR با گوشی + کاهش مصرف ریکوئست های گوگل
⚡️
لینک‌های داخلی جهت دانلود:
https://t.me/MatinSenPaii/2969
لینک پروژه اصلی:
https://github.com/therealaleph/MasterHttpRelayVPN-RUST
⭐️
توی این ویدئو بهتون یاد میدم که چطوری متد MHR رو صفر تا صد با گوشی بسازین، به علاوه‌ی آموزش یه کوچولو کاهش مصرف ریکوئست‌ها(به نظرم دیپلویمنت بیشتر بسازید راحتتره)
🚀
لینک‌های دانلود با نت داخلی:
https://t.me/MatinSenPaii/2969
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
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/MatinSenPaii/2968" target="_blank">📅 18:58 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">Mhr cfw با ترموکس رو بذار لطفا</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/2967" target="_blank">📅 18:03 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2966">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">باو از MHR و این داستانا بکشین بیرون تاوقتی ورسل و نتلیفای هست :)</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/2966" target="_blank">📅 18:01 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2965">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آموزش بعدی روش ساخت MHR کاملا با گوشی هست بدون نیاز به لپ تاپ و مشغول آپلودش هستم
متشکرم از دوستان عزیزی که کانفیگ رسوندن به دست من
داخلی هم واستون آپلود میکنم صد البته</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/MatinSenPaii/2965" target="_blank">📅 17:56 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2964">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک نفر 47 دلار دونیت کرد. ممنونم ازت هر کس که بودی
❤️
کمک‌های شما حمایت و دلگرمی بزرگیه اما دلیل فعالیت من نیست. کار من همیشه بدون چشم‌داشت بوده و هست</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/MatinSenPaii/2964" target="_blank">📅 20:32 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2963">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سؤال: چرا قیمت کانفیگ‌فروش‌ها پایین اومده یهو؟
جواب: 1- تعداد زیادی از کانفیگ‌فروش‌های حال حاضر، زرنگی کردن به حساب خودشون و اومدن از سیمکارت‌های پرو و سفید استفاده می‌کنن، و تا می‌تونن می‌فروشن.
2- همینطور یک تعدادی هم از متدهای خاصی که رندوم واسشون جواب داده استفاده میکنن(به طور مثال یه range آیپی وایت شده سرور ایران اینا هم جزوشون بوده یا استفاده از Shecan)
3- استفاده از اینترنت طبقاتی شرکت‌ها، سازمان‌ها و یا دانشگاه‌ها و اساتید.
4- دلایل دیگه‌ای هم هستن که یا من نمیدونم یا حضور ذهن ندارم.
به خاطر همین قیمت کانفیگ پایین اومده. منتها من پایداری زیادی درونشون نمیبینم. اگر جایی ارزون دیدید که اوکی بود هم، کم کم بخرید. یهو نرید 50 گیگ بخرید</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/MatinSenPaii/2963" target="_blank">📅 16:22 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2962">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(مایلز گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApRuw_tv3i3xsWlgdsbtRPwrlmMUSX8-kMriEUKZUoSQHO812PZamjX8vZpIzMRgicrbfOsl-5KhsE_X7CNY8CiqKuSn-_80baq7Ry5jHfwOXZU8EigYst-1Z-EUALj18OQ8FBNJCQ7-Tj0GwOPRVS_S8TqDGGWXtHdl-RdlpyaffEm-S6sV_mPuftRbjQh0Cdp11wuNClhZtRbJEmJ7-7NR_10-Iya_fz0BfV3PtkqF-T7vwqbod_PoLBsQrPEjlIAhsET9AmXXdbWrdLMmFGMPuTgXkz33cYzOCSD7qdlmpxAUSlHg830O7dI2yFMA8HfdNgd1aWr83H4EOAyS3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
اپ TeleMirror یه تلاش آزمایشی برای دریافت آخرین مطالب کانال
#تلگرام
خودم و سایر کانال‌های موردنظر در شرایط محدودیت شدید اینترنته، که سعی می‌کنه با چند روش مختلف پست‌ها رو بگیره و نمایش بده.
این برنامه
#رایگان
و متن‌بازه و فعلا می‌تونه برای دنبال کردن اخبار تلگرامی بدون نیاز به فیلترشکن، یه گزینه موقت و کاربردی واسه دسکتاپ باشه.
لینک پروژه:
⚡️
http://github.com/ircfspace/teleMirror/releases/latest
(پخت و پز عشق ircf)
@ircfspace
💎
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/2962" target="_blank">📅 21:25 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2961">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حملات آخرالزمانی اسرائیل به جنوب لبنان</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/2961" target="_blank">📅 19:09 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2960">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دی ان اس هاتونو آماده کنید</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/MatinSenPaii/2960" target="_blank">📅 18:43 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2959">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خب فکر کنم دوباره جنگ شد؟</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/MatinSenPaii/2959" target="_blank">📅 18:43 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2958">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/2958" target="_blank">📅 17:17 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اینا که این پایین میاد و خیلی ممبر دارن بازم کلاهبردارن؟</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/MatinSenPaii/2957" target="_blank">📅 17:15 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2956">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XGi5Tws_oWb52f1lNLySEv5tI8eJ6vCemGT3yUItVYoiWPxldapkgNkuaoCjUy_78cdmd-3kOMWD6Oj-kKHOQWzyHN37-ZD-YcajBn-M2zSZIj_gvuQw76rvd2ZN1ZsBiQGqoP40ksiwurM-IJGSH2TgEqUPJRYpBWDU3eck2Qz3yEuQ3eFSAsDk5tWUc0x2o8Tr1bDQNFaiTFE5-FC3d9NxPmlvUp1IWTdvGuHIlm8jrbmBdQMdHCLJt3suNtGxmM_dfuJlTg0u-L-VCZXZm0WRTQT-cUYosGf6a1zLzt5sR2LJ9pBpJixJHWnHrFG1kDX_0ThAR39AmqBiQ-603g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تبلیغات هم مال کانال من نیست. اعصابم خورد میشه با یه ذره Ton تبلیغ میزنن این زیر اونوقت من باید چندین هزارتا Boost بخرم تا تبلیغات رو غیرفعال کنم</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/MatinSenPaii/2956" target="_blank">📅 17:10 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شرایط نت و محدودیت‌ها رو درحال حاضر نمیشه پیش‌بینی کرد. همونطور که میدونید با کوچکترین حرکتی همه‌چیز محدود میشه..
اما به محض اینکه یکم شرایط استیبل بشه، پیگیر کلاه‌بردار ها و کسایی که تو این وضعیت بد جای کمک و کنار مردم بودن ازشون دزدی کردن و زخم تازه ای روی زخم‌هاشون بودن خواهیم بود.</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/MatinSenPaii/2955" target="_blank">📅 16:57 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2954">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">من با این لیست وصل هستم خودم روی همراه اول و سیمکارت شاتل
185.161.112.38
194.225.152.10
217.218.155.155
185.20.163.4
78.157.42.101
31.24.234.37
31.7.78.205
80.75.14.102
185.255.89.57
2.188.21.138
2.188.21.58
2.189.44.68
185.110.244.150
2.189.44.98
2.188.21.62
2.188.21.70
80.210.40.55
85.185.163.4
2.189.44.66
2.188.21.46
2.189.44.84
2.189.44.82
2.189.44.86
2.189.44.85
2.189.44.83
80.210.40.53
2.188.21.146
172.64.32.0
108.162.192.0
78.39.234.230
173.245.58.0
2.188.21.78
2.189.44.44
185.20.163.2
194.60.210.66
217.218.127.127
2.188.21.130
31.24.200.4
2.185.239.138
5.145.112.39
85.185.85.6
217.219.132.88
178.22.122.100
194.36.174.1
185.53.143.3
80.191.209.105
78.157.42.100
213.176.123.5
185.55.226.26</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/MatinSenPaii/2954" target="_blank">📅 11:45 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2953">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گویا یک پروژه‌ی دیگه نوشته شده واسه‌ی Vercel
که تشخیصش سختتره توسط سایت
اما من به دلایلی که قبلا گفتم آموزش نمیدم چون از نظرم به درد نمی‌خوره. مردم نه میتونن راحت اکانت بسازن داخلش، نه اعتباری به وایت موندنش هست، نه اعتباری به بن نشدن اکانت. توصیه‌ی اکیدم هم اینه که اکانت Vercel Pro نخرید. اما باز هم اگر علاقه‌مند بودید،
این خود پروژه هست:
https://github.com/B3hnamR/XHTTPRelayECO
این هم آموزش متنیش:
https://github.com/B3hnamR/XHTTPRelayECO/blob/master/Anti-Ban-Tutorial.md</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/MatinSenPaii/2953" target="_blank">📅 11:31 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2948">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitends-beta3-arm64-v8a-debug.apk</div>
  <div class="tg-doc-extra">22.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/2948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/2948" target="_blank">📅 10:14 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2947">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نسخه‌ی بتای 3 منتشر شد. دوستان از سرورهای دیگه‌ی storm توی چنل استفاده کنید. خود سرورهای built-in سرعتشون یه کوچولو پایین اومده</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/2947" target="_blank">📅 09:40 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2945">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mcxc5c-2z5_WEp7168Df03AGiMhqCh9or5nTvtuaTUgQzFcV6G6Ix_ONq5sGDX24Sp3VVX1pxZSxl1SwW0-6kUH9yXLiNIwy0-gdW7yJflnr7qRVwrDAeEuqbDhTxqslFjNnOXqJBhiyEvS_MYjXoiE3caASxC3kjd38_wYpCWzpkVkdTIU1DZIpVNyZ3gm9ZQTP5eBRYV8MwmCRqKbsepu0JeSDbrfL0YIci1N-ksk7vy-i5xDF2vkP9D8h-8chfQxN8yW8UoksYQBnJbxzEhq9oo_bB5ILR8SwVufM9dGzefpDrUd7W84XAq5ab8u4ne8SFsHzAXcQDbQoIJaI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CVo3g18UCO03EB0tGR_gjB64ctuKjO0AmjEhPFaKLS_mNER0JF3YI-C9mwTjZ9a0-tdTJnLfUx3Elriqhe3f1ElLVKIZXMkFCn4CvpchSKli17cEvZk44Wq2sNz02Orrgsbq0SHYXvGpe985ocVzosXtMq2QRARw0HeiVf113jylN6wBEGl-yEkraHJRIeYv8A2E5yGyFBQafxOpiDUj4kh1LLIsD5-mpEkzA-H8OG70M0iqujZD4HyuRjAYRfUKlcZP5eYOFt4pY0zpmgYp8BKBqryJ-htcBwisX12GfNDrCSiHhwUBqzZohGL7RQCJ_FQYo-eY85R3rTNH9Hm-fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید تستی WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
دانلود سرور داخلی
https://uplod.ir/gce7505a78tl/WhiteDNS-Beta3.zip.htm
https://guardnet.ir/f/whitednsB-3share
در این نسخه تغییرات زیادی روی ظاهر، پایداری و مدیریت کانفیگ انجام شده:
✅
طراحی اپلیکیشن کامل بازطراحی شده و حالا ظاهر جدید، ساده‌تر، مرتب‌تر و دارک دارد
✅
دارک مود و رنگ‌بندی جدید برای خوانایی بهتر اضافه شده
✅
امکان ساخت چند پروفایل کانکشن اضافه شده
✅
امکان ساخت چند پروفایل ریزالور اضافه شده
✅
انتخاب پروفایل کانکشن و پروفایل ریزالور ساده‌تر شده
✅
لاگ‌ها جدا شدند و حالا خواناتر نمایش داده می‌شوند
✅
امکان کپی و خروجی گرفتن از لاگ‌ها اضافه شده تا اگر مشکلی داشتید راحت‌تر برای ما ارسال کنید
✅
دکمه Reset to Default برای برگرداندن تنظیمات پیشرفته به حالت پیش‌فرض اضافه شده
✅
تنظیمات اضافه و گیج‌کننده تا حد ممکن مرتب و حذف شدند
✅
دسترسی Battery Optimization اضافه شده تا اتصال در پس‌زمینه پایدارتر بماند
✅
باگ کرش کردن اپلیکیشن بعد از Disconnect مخصوصا در حالت Full VPN برطرف شده
✅
نسخه جدید بهینه‌تر شده و لاگ‌ها فقط آخرین موارد مهم را نگه می‌دارند تا روی عملکرد اپلیکیشن فشار نیاورد
✅
حالت Proxy Mode به عنوان گزینه پیش‌فرض قرار داده شده چون عملکرد بهتر و پایدارتری دارد
پیشنهاد ما این است که اگر امکانش را دارید از Proxy Mode استفاده کنید. حالت Full VPN هنوز برای تست وجود دارد، اما چون کل ترافیک دستگاه را از تونل عبور می‌دهد ممکن است سرعت و پایداری پایین‌تری داشته باشد.
همچنین اگر سرور StormDNS شخصی دارید، بهتر است از سرورهای خودتان استفاده کنید. فشار زیادی روی سرورهای عمومی WhiteDNS وجود دارد و استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند سرویس عمومی برای بقیه کاربران بهتر کار کند.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
لینک کانال:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/MatinSenPaii/2945" target="_blank">📅 09:39 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2944">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">💬
یه سری مطالب از Repo سازنده‌ی MHR واستون قرار میدم(مربوط به این روش:
https://t.me/MatinSenPaii/2785
) :
اول از همه دقت داشته باشید که به روز ترین نسخه‌ی
code.gs
رو حتما از گیتهاب پروژه گرفته باشید:
https://github.com/masterking32/MasterHttpRelayVPN/blob/python_testing/apps_script/Code.gs
✅
1- برای اسکن سریعترین IP گوگل، این دستور رو اجرا کنید:
python main.py --scan
و بعدش توی config.json، آیپی پیدا شده رو توی بخش
google_ip
قرار بدید اونی که پینگ کمتری از همه داره.
✅
2- گوگل و یوتیوب باز می‌شن، ولی ویدئوها پخش نمی‌شن و سایت‌های دیگه هم باز نمی‌شن:
الف) محدودیت روزانه 20کا ریکوئست شما تموم شده. تا فردا صبر کنید ساعت 10:30 صبح
ب) deployment شما مشکل داره و باید مجددا روی همون اکانت گوگلتون پروژه رو دیپلوی کنید
ج) اکانت شما فلگ شده و باید با جیمیل دیگه‌ای دیپلوی کنید بالکل پروژه رو روی یه جیمیل دیگه دیپلوی کنید
✅
3- ارورهایی از جمله certificate error و ... به خاطر نصب نبودن سرتیفیکیت هستن. ویدئو رو با دقت ببینید و سرتیفیکیت‌ها رو نصب کنید
✅
4-  خطای unauthorized: مقدار auth_key و AUTH_KEY باید یکسان باشه از سمت گوگل و فایل شما
✅
5- ارور timeout آیپی گوگل فیلتره واستون(به سؤال 1 مراجعه کنید)
✅
6-  سرعت کم: سازنده گفته که استفاده از چندین deployment_id و چندین اکانت گوگل، این مشکل رو حل میکنه</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/MatinSenPaii/2944" target="_blank">📅 20:13 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2943">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دیروز به گوشم رسید یکی متد نامحدود خریده بوده 2 میلیون تومن
وقتی که خریده
طرف گفته خب حالا متد رو الان واست میفرستم
پست‌های کانال من راجب MHR رو واسش فوروارد کرده:)))
مراقب باشید اینجوری اسکم نشید دوستان. هر متد عمومی‌ای که باز بشه من و بقیه‌ی بچه‌های کامیونیتی اعلام میکنیم.</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/2943" target="_blank">📅 19:36 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2942">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">❌
پولت رو بده نیازمند، سودش بیشتره تا بخوای شکن بخری! من شکن حرفه‌ای خریدم، اگر اون پول رو میدادم غذا برای گربه‌ها میخریدم، بهشت رو واسه خودم خریده بودم! نمیدونم چرا اینقدر شکن رو بولد میکنن! البته به قول متین: «شکن چند وقت پیش هم اومد خودش رو بولد کرد و مردم حمله کردن اکانت خریدن تا روی chat gpt کانفیگ بسازن، بعد که فروخت، چت جی‌پی‌تی رو بست!» اکثر این‌هایی که تبلیغ شکن میکنن بازاریابِ همین دزدان و قوادان هستن! که مردم برن بخرن بعد قطع کنن! تهشم بگن: «اختلال از سمت زیرساخت هست و ما تابع قوانین کشور هستیم» یعنی پولت رو نمیدیم و بهت هم میخندیم!</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/2942" target="_blank">📅 19:23 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2941">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">توی این سایتِ خودِ گوگل، می‌تونید از مدل هوش مصنوعی نانوبنانا 2 و Pro برای تولید تصویر، به رایگان استفاده کنید. تبلیغات و credit و ... هم نداره امکاناتش هم حتی از اکانت Pro جمنای برای تولید عکس بیشتره: https://labs.google/fx/tools/flow</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/2941" target="_blank">📅 18:38 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2940">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WWpqVPaOGC867am0LF-vOF_vZ6n-jU3ptQkrXj6vJP57JDTEVAUdzSiPzXs8tmYFVjyFzvnZ9uX7s-HOlDRZWTMz1bgj3uLluV0oInUiu9ie1u_adxWhklrj953zTowX_g8mZBkh-BCt8tA-i925DB8MPzgJIvNLldjMiBVYxOz27kdkLHiT-9i8dmWKjHyfUnwaWJ3zqcgiti3_RuFHZZwh11DXUFaSLsLcj7XCDKmWsviJgIS317NDwfn4YprTcI4-5j1pil4JeMjgB0_Rl06eSMDA7qwOQvTcfY3V6AONrDPjskhq8hL_DlT2DfmzlJcwLEV1j1bkHypIY9Lviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این سایتِ خودِ گوگل، می‌تونید از مدل هوش مصنوعی نانوبنانا 2 و Pro برای تولید تصویر، به رایگان استفاده کنید. تبلیغات و credit و ... هم نداره امکاناتش هم حتی از اکانت Pro جمنای برای تولید عکس بیشتره:
https://labs.google/fx/tools/flow</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/MatinSenPaii/2940" target="_blank">📅 18:31 · 13 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
