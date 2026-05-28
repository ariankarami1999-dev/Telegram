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
<img src="https://cdn4.telesco.pe/file/ANBPQI3NpKaHMoTuHF3b3QXmfnev-66ZrvmKGFfkJuXOTrvRTHHbMNUIM9O3tUq0vSRj1sZqwvgS9Pac8KV7zAe2OOG2OOw9aI8DJSDZoGTDzDhQP0UiebIPb1ehfET260qoPzn_NsbPikbe7HwNCb6SDwoYTpUvmbmEyyqELZb3ycCHThKHOniIi-8oQB3l3IAfMlHGwlo6H5HD4qf-64YnRda2aJzoDpuV7HtGaoeCVhrge7IB2YpwDaRZtOnmjvK8Mxrg3c29vap-baRStuN-QmKjPsMMqUV6ITi9sg_Tph1g51Ea9jXvDt_gHLkM_pUqVpcYbOoo5EqQ16nZUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 8.63K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 14:16:28</div>
<hr>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac73908c6d.mp4?token=TTGvubNdIZaCuT9UMFZlaaEjs7fETs9TmlCyQQExv4se7Y73POcS6duUY3BryP1mU81QDpYO9a5CEIJhIB6W067tMQ73WBOi0jSHTgEUNHnubFY44F7Be_EPeAv5bpmx4iMgTf-_23xhGNH5hmvPBxiVeB5YAXZixa6PNnr5MGXTvLRMQ8ZSnClnw4dO-ymSy94N4276BcYk1L6ehckC_Alfh1dJ4iTVosi4I3ZJTSrFqsFR7eS2-_t8DVhP3huwQZ1oY19CYGegocpaQXdyT-rOW9qyzW6frRgVWvaL78I6csPuoosquC5QoOV_5BQl0OzYqmKsIHTGgil6bqaiRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac73908c6d.mp4?token=TTGvubNdIZaCuT9UMFZlaaEjs7fETs9TmlCyQQExv4se7Y73POcS6duUY3BryP1mU81QDpYO9a5CEIJhIB6W067tMQ73WBOi0jSHTgEUNHnubFY44F7Be_EPeAv5bpmx4iMgTf-_23xhGNH5hmvPBxiVeB5YAXZixa6PNnr5MGXTvLRMQ8ZSnClnw4dO-ymSy94N4276BcYk1L6ehckC_Alfh1dJ4iTVosi4I3ZJTSrFqsFR7eS2-_t8DVhP3huwQZ1oY19CYGegocpaQXdyT-rOW9qyzW6frRgVWvaL78I6csPuoosquC5QoOV_5BQl0OzYqmKsIHTGgil6bqaiRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧠
در GitHub پلاگینی به نام agentmemory محبوب شده است که به عوامل هوش مصنوعی حافظه «بی‌نهایت» اضافه می‌کند — این پلاگین تمام زمینه‌های جلسات، اقدامات و پروژه‌های شما را در یک پایگاه ذخیره می‌کند.
• به ۱۶ عامل هوش مصنوعی از جمله Claude Code، Codex و Cursor متصل می‌شود.
• تمام اقدامات آن‌ها را ذخیره می‌کند، به خاطرات فشرده تبدیل می‌کند و به‌طور خودکار در آینده آن‌ها را پیدا می‌کند.
• دیگر نیازی نیست هر بار زمینه را توضیح دهید — عامل همه جزئیات را به خاطر می‌سپارد.
در نتیجه، می‌توان تا ۹۵٪ از توکن‌هایی که معمولاً برای توضیح زمینه صرف می‌شوند را در هر جلسه صرفه‌جویی کرد.
https://github.com/rohitg00/agentmemory
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5651" target="_blank">📅 09:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کانفیگ اهدایی
تشکر از
@thee_LaShi
بابت این کانفیگای ناب
❤️
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@tr-in.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=19aa22f681923dc8&sni=tr-in.api.dznn.net&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/5650" target="_blank">📅 08:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانفیگ اهدایی
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@ninka.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=19aa22f681923dc8&sni=ninka.api.dznn.net&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5649" target="_blank">📅 08:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فیلترچی ری اکشن فیک بزن تا بسوزی
😁</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/5648" target="_blank">📅 08:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5647">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پخش کنید بقیه هم وصل بشن
😁</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/5647" target="_blank">📅 08:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کانفیگ اهدایی
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@tr-in.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=19aa22f681923dc8&sni=tr-in.api.dznn.net&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/5646" target="_blank">📅 08:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5645">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کانفیگ اهدایی
vless://0468a043-e12c-466e-881c-7d685c1b3950@roz1r.skystreamgame.com:8443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QHkXBS2ENHV0khgY9VBYi8_9bpfqnUYDcfQN4cW5Qg0&security=reality&sid=4326&sni=roz1r.skystreamgame.com&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5645" target="_blank">📅 08:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کانفیگ اهدایی یکی از ممبرای عزیز
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@fishsea.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=0a6ba2716a409da6&sni=fishsea.api.dznn.net&type=tcp#@archivetell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/5644" target="_blank">📅 08:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کانفیگ اهدایی یکی از ممبرای عزیز
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@fishsea.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=0a6ba2716a409da6&sni=fishsea.api.dznn.net&type=tcp#@archivetell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/5643" target="_blank">📅 08:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">windscribe_auto_hand .zip</div>
  <div class="tg-doc-extra">12.4 MB</div>
</div>
<a href="https://t.me/archivetell/5642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل اتوماتیک سازی فرایند جست‌وجو لوکیشن برنامه ویندسکرایب فقط نسخه ویندوز  با تشکر از چنل
@windscribe_auto_hand
که زحمت کشیدن کد نویسی این برنامه رو انجام دادن
❤️‍🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5642" target="_blank">📅 02:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5641">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅️
خب از اونجایی که بعضی از پروتکل های ویندسکرایب باز شدن براتون یه اموزش و فایل رو میزارم که فقط مخصوص نسخه ویندوز هست
طبق این این اموزش جلو برید  و تک تک مراحل رو انجامش بدید :
کد exe اتوماتیک سازی فرایند جست‌وجو لوکیشن ویندسکرایب
مخصوص ویندوز
این کد به گونه ای نوشته شده که حتی موقعی که API وینداسکرایب کانکشن نمیده هم وصل بشه
⭕️
نحوه استفاده
اول وینداسکرایب رو باز میکنید
پروتکل و پورت مد نظرتون رو انتخاب کنید
بعد برنامه exe رو اجرا میکنید
وقتی اجرا کردید بلافاصله یه جایی رو windscribe کلیک کنید
حالا کد خودش شروع میکنه همه لوکشین هارو تست میکنه
اگر وصل شد توی پوشه logs تو فایل text مینویسه
تو این فرایند قهوه بنوشید و صبر کنید تا تموم بشه
امیدوارم به کارتون بیاد
❤️
با تشکر از چنل دوستمون
@windscribe_auto_hand
❤️‍🔥
که این اسکریپت رو واقعا زحمت کشیدن نوشتن و تو چنل قرار دادن اون زمان چون ایران اینترنتش اکسس بود قابل استفاده نبود ولی الان میتونید استفاده کنید
⚠️
نکته مهم : وینداسکرایب همچنان روی متد کار میکنن و باهاشون حرف زدم با اینکه اینترنت کمی محدودیت هاش رفته و باز کامل نیست
از پروژه دست نکشیدن و قراره نسخه نهایی رو یکدفعه release کنند که اگه یه زمان دوباره مشکلی پیش اومد همیشه این متد برای ایرانی ها قابل استفاده باشه
با تشکر از تیم ویندسکرایب که خیلی تلاش دارن میکنن نسخه نهایی رو بدون مشکل بسازن
🔥
🤌
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/5641" target="_blank">📅 02:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">FileShare.exe</div>
  <div class="tg-doc-extra">48.6 MB</div>
</div>
<a href="https://t.me/archivetell/5638" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
انتشار نسخه جدید File Share v1.2
توی این آپدیت کلی تغییر و بهبود اضافه شده:
✅
امکان انتخاب پوشه اختصاصی برای اشتراک‌گذاری فایل
کاربر حالا می‌تونه هر پوشه‌ای رو برای اشتراک در شبکه محلی انتخاب کنه.
✅
اضافه شدن آیکون اختصاصی برنامه
از نسخه 1.2 برنامه ظاهر حرفه‌ای‌تری گرفته.
✅
جایگزینی پنل ویندوزی به جای محیط ترمینال
رابط کاربری ساده‌تر و کاربرپسندتر شده.
✅
رفع باگ‌ها و بهبود عملکرد
پایداری و سرعت برنامه بهتر شده.
📡
File Share یه ابزار انتقال فایل تحت شبکه محلیه که بدون اینترنت کار می‌کنه.
کافیه کاربر دوم IP سیستم رو داخل مرورگر وارد کنه تا از طریق محیط وب:
⬇️
دانلود فایل
⬆️
آپلود فایل
💬
تبادل پیام بین دستگاه‌ها
به‌صورت کاملاً آفلاین و داخل شبکه محلی انجام بشه.
🛠
همچنین پروژه روی GitHub قرار گرفته تا به‌صورت Open Source در دسترس همه باشه و سورس کدها برای توسعه، بررسی و مشارکت در اختیار همگان قرار بگیره.
لینک گیت هاب پروژه</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/5638" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b370928a6c.mp4?token=AS_2ax_bORjMwb2EX3PZIsQW9NymqjyrnmzZGe9xHp_9xhS8w7dTs4N-C06Y7nrTHMI4WExT-UddXaYrPRL5GKAKX4_INIXBhRRzTwfFXZb8gnFW-zjmgW7_tpwSvNBjVNF00nf7WgtoTNrx4pONc8-gcuUXBlJXJwnxpuz4dQVa0Ndu2s8XQFoez31mpbtRxLJtnwKPEN5INMQWbbXwdhRtaxCc3m1XjZmu7xPHLP257LFSe5XJWtejAyenW-byFUXHhY5lHIqQEXxF5uiIddueLEd_dSjDNzt7RYdJ-qqRgddum0_519NnCet2Ls_m-9PuiCR2B1RAdkuUGcXfug" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b370928a6c.mp4?token=AS_2ax_bORjMwb2EX3PZIsQW9NymqjyrnmzZGe9xHp_9xhS8w7dTs4N-C06Y7nrTHMI4WExT-UddXaYrPRL5GKAKX4_INIXBhRRzTwfFXZb8gnFW-zjmgW7_tpwSvNBjVNF00nf7WgtoTNrx4pONc8-gcuUXBlJXJwnxpuz4dQVa0Ndu2s8XQFoez31mpbtRxLJtnwKPEN5INMQWbbXwdhRtaxCc3m1XjZmu7xPHLP257LFSe5XJWtejAyenW-byFUXHhY5lHIqQEXxF5uiIddueLEd_dSjDNzt7RYdJ-qqRgddum0_519NnCet2Ls_m-9PuiCR2B1RAdkuUGcXfug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاربران ChatGPT اکنون می‌توانند مستقیماً از طریق چت برنامه‌های واقعی بسازند
فروشگاه برنامه ChatGPT
به تازگی
AppDeploy
را اضافه کرده است و این قابلیت برای حساب‌های رایگان نیز فعال است.
توضیح دهید که چه چیزی می‌خواهید بسازید، ChatGPT کد را می‌نویسد، AppDeploy به طور خودکار در همان چت استقرار را انجام می‌دهد و بلافاصله یک لینک کارآمد به شما بازمی‌گرداند.
رایگان برای استفاده. نیاز به اشتراک یا کارت اعتباری نیست.
👉
نصب AppDeploy در ChatGPT
و راه‌اندازی اولین برنامه خود در چند دقیقه
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/archivetell/5637" target="_blank">📅 00:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گوگل پلی رفع فیلتر شده..</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/archivetell/5636" target="_blank">📅 23:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گوگل پلی رفع فیلتر شده..</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/archivetell/5635" target="_blank">📅 23:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ربات جدید تبدیل لینک به فایل
@url_uploder_nrbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5634" target="_blank">📅 23:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12fb4063f0.mp4?token=CMkZ8flfpzilHY6XkC_dzBR13tpa-SOnunTeTO36qD2kTSQVVW8kjwupnTxU5X37oF6K1N2p5CkyrT_N5ZMK_ELYbQ28lROCPpt5Rvk0zYojgu_I-1tir7baQ03x0t5zpIEqUhFRFZcQ31A5k48MyXDLJoS_52FkROTcVZpPaz5JgTb9dSWOpZC1w0ohxa0IHlXLZ7jkL71zjxWjFEVJYTS02tCQ59I-KhJ76xwXonE9mA3MYJHPYTVCfkuHDfh7HLrWSR7XM3nVvqj6xrJyOqItBYUDdj-5IGJiEij0rnMjtRLeO7k8H3DmZ8NHH8U80cctUfwOAzN0nfj-5oQf7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12fb4063f0.mp4?token=CMkZ8flfpzilHY6XkC_dzBR13tpa-SOnunTeTO36qD2kTSQVVW8kjwupnTxU5X37oF6K1N2p5CkyrT_N5ZMK_ELYbQ28lROCPpt5Rvk0zYojgu_I-1tir7baQ03x0t5zpIEqUhFRFZcQ31A5k48MyXDLJoS_52FkROTcVZpPaz5JgTb9dSWOpZC1w0ohxa0IHlXLZ7jkL71zjxWjFEVJYTS02tCQ59I-KhJ76xwXonE9mA3MYJHPYTVCfkuHDfh7HLrWSR7XM3nVvqj6xrJyOqItBYUDdj-5IGJiEij0rnMjtRLeO7k8H3DmZ8NHH8U80cctUfwOAzN0nfj-5oQf7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک مجموعه برتر از انیمیشن‌های رابط کاربری وب برای طراحان رابط کاربری که تمایلی به صرف زمان در ایجاد انیمیشن‌ها از پایه ندارند
https://transitions.dev/
این مجموعه شامل انیمیشن‌های آماده‌ای برای کارت‌ها، منوها، فهرست‌ها و کلیدهای تغییر وضعیت می‌باشد.
امکان بررسی مستقیم انیمیشن‌ها در وب‌سایت پیش از بهره‌برداری فراهم است.
ادغام در پروژه‌های فرانت‌اند واقعی به سادگی امکان‌پذیر است.
پشتیبانی از ادغام به عنوان یک قابلیت برای عوامل هوش مصنوعی ارائه می‌گردد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/archivetell/5633" target="_blank">📅 22:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121da40c06.mp4?token=m1Cpflt1wiPRKXjYdWkN_AvnhWEalQ_fszKFgnOiZ6CoKY_-Iv3tu-IUgiQyjaVvxdAjyISJYq6NAeDxTQOGmRGlGff0tMH4vu8x00Ty4lDgKBHlYqjD1yMlR_vJ_fv6q6pRfrvmXrs7RjiDNmOxtrwlTKkKJT5yFIStbckvqNoKtZ1i1B2MRPhkZ-G0fp4uou3y0nO_A8GXakUrqp4ZDTYRP7rIecdvWuk56B7Fwe74OojsqYvFp5eVz8qCdfHXLDznkVBri1FOQClwTj6b7N5m62gh_0uIOowAPd8j2hetZHYi9SWG5xBrsfPJ6X_cRxfvvlGu4-82UnDsR5U01g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121da40c06.mp4?token=m1Cpflt1wiPRKXjYdWkN_AvnhWEalQ_fszKFgnOiZ6CoKY_-Iv3tu-IUgiQyjaVvxdAjyISJYq6NAeDxTQOGmRGlGff0tMH4vu8x00Ty4lDgKBHlYqjD1yMlR_vJ_fv6q6pRfrvmXrs7RjiDNmOxtrwlTKkKJT5yFIStbckvqNoKtZ1i1B2MRPhkZ-G0fp4uou3y0nO_A8GXakUrqp4ZDTYRP7rIecdvWuk56B7Fwe74OojsqYvFp5eVz8qCdfHXLDznkVBri1FOQClwTj6b7N5m62gh_0uIOowAPd8j2hetZHYi9SWG5xBrsfPJ6X_cRxfvvlGu4-82UnDsR5U01g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎹
سونو را دور می‌اندازیم — ElevenLabs نسخه Music V2 را عرضه کرده است. توسعه‌دهندگان این را بزرگ‌ترین به‌روزرسانی شبکه عصبی موسیقی تا به امروز می‌نامند.
https://elevenlabs.io/music
🕤
تولید ووکال، ابزارها و آرنجمنت‌ها در همه ژانرها به طور قابل توجهی قدرتمندتر شده است.
🕤
سبک آهنگ را می‌توان در حین پخش تغییر داد.
🕤
هر بخش از آهنگ به طور جداگانه ویرایش می‌شود — ثانیه مورد نظر را انتخاب کرده و فقط آن را بازتولید می‌کنید.
🕤
پشتیبانی از رفرنس‌ها: می‌توانید صدا، متن، ژانر یا پرامپت معمولی بارگذاری کنید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/archivetell/5632" target="_blank">📅 22:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کانفیگ پرسرعت
ایپی استاتیک کره شمالی
جهت سفارش پی‌وی
🐱</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/archivetell/5631" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شما می‌توانید Llama 4، Qwen3، Gemma 4 را اجرا کنید — همه رایگان، همه خصوصی، روی لپ‌تاپ خودتان.
🖥️
⚡
این همان Ollama است.
🔗
ollama.com
این یک ابزار رایگان است که به شما اجازه می‌دهد مدل‌های قدرتمند هوش مصنوعی متن‌باز را به صورت محلی اجرا کنید — بدون نیاز به اینترنت، بدون هزینه API، بدون خروج داده‌ها از دستگاه شما.
فقط دانلود کنید، یک مدل بکشید و شروع به گفتگو کنید.
چرا مردم واقعاً از آن استفاده می‌کنند:
→ بدون هزینه‌های ابری
→ کاملاً خصوصی — داده‌های شما هرگز از دستگاهتان خارج نمی‌شود
→ به صورت آفلاین کار می‌کند
→ مدل‌هایی مانند DeepSeek-R1، Llama 4، Qwen3، Gemma 4 را اجرا می‌کند
نسخه ۲۰۲۶ اکنون شامل یک رابط کاربری دسکتاپ داخلی، شتاب‌دهی Apple Silicon از طریق MLX، و پشتیبانی ابری برای مدل‌های بزرگ‌تر است — همه در یک رابط کاربری تمیز.
اگر برای اشتراک‌های هوش مصنوعی هزینه می‌پردازید و هیچ کار حساسی با داده‌هایتان انجام نمی‌دهید... Ollama ارزش ۱۰ دقیقه وقت شما را دارد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/archivetell/5630" target="_blank">📅 20:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎁
دریافت یک سال اشتراک پرمیوم RoboForm (رایگان)
---
رفقا سلام!
✋
یه آفر فوق‌العاده و محدود داریم. پسورد منیجرِ معروف، امن و پرطرفدار
RoboForm
، به کاربراش
۱۲ ماه اشتراک پرمیوم کاملاً رایگان
(به ارزش حدود ۳۰ دلار) میده.
اگر هنوز از یه ابزار مدیریت پسورد خوب برای ذخیره امنِ رمزها، قابلیت اتوفیل (Autofill) و همگام‌سازی بین گوشی و لپ‌تاپ استفاده نمی‌کنید، الان بهترین فرصته.
💻
مراحل دریافت اشتراک:
۱. وارد لینکِ آفر در پایین پست بشید.
۲. ایمیل خودتون رو وارد کنید و روی دکمه
Redeem Offer
کلیک کنید.
۳. مراحل ثبت‌نام و فعال‌سازی اکانت رو انجام بدید.
✅
تمام! اشتراک یک‌ساله پرمیوم به صورت خودکار روی اکانتتون فعال میشه.
⚠️
نکات مهم این آفر:
-
💳
بدون نیاز به کردیت کارت:
برای فعال‌سازی اصلاً نیازی به وارد کردن اطلاعات پرداخت یا کارت بانکی نیست.
-
🆕
کاربران جدید:
این آفر فقط برای اکانت‌ها و کاربرانی هست که تا حالا پرمیوم نبودن.
-
⏳
مهلت استفاده:
فقط تا
۳۱ می ۲۰۲۶
(۱۱ خرداد ۱۴۰۵) فرصت دارید این آفر رو دریافت کنید.
🔗
لینک دریافت آفر ویژه روبوفروم:
🌐
https://www.roboform.com/lp?frm=offer-ga
📌
#آفر
#رایگان
#RoboForm
#پسورد_منیجر
#امنیت
#پرمیوم
#کاربردی
#تخفیف
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/archivetell/5629" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">600 گیگ کانفیگ مستقیم متصل همه نتا
اهدایی یکی از ممبرای عزیز
❤️
vless://22768339-9096-48aa-9109-ff28141145b9@roz2r.skystreamgame.com:8443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QHkXBS2ENHV0khgY9VBYi8_9bpfqnUYDcfQN4cW5Qg0&security=reality&sid=4326&sni=roz2r.skystreamgame.com&type=tcp#Aqa.rza
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/archivetell/5628" target="_blank">📅 19:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">kiro.dev
یک ابزار کدنویسی هوش مصنوعی از AWS که فقط کد نمی‌نویسد.
این ابزار کل پروژه شما را از صفر برنامه‌ریزی، طراحی و می‌سازد.
⚡
Free trial with 500 credits
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/archivetell/5627" target="_blank">📅 19:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آیپی تمیز کلودفلر، تست شده روی ایرانسل 104.16.81.122 104.16.81.43 104.16.81.86 104.16.81.12 104.16.81.24 104.16.81.125 104.16.81.40 104.16.81.133 104.16.81.68 104.16.81.101 104.16.81.23 104.16.81.155 104.16.81.112 104.16.81.106 104.16.81.67 104.16.81.82 104.16.81.157…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/archivetell/5625" target="_blank">📅 18:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">Defyx VPN  رایتل سرعت بالا  https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5624" target="_blank">📅 18:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آیپی تمیز کلودفلر، تست شده روی ایرانسل
104.16.81.122
104.16.81.43
104.16.81.86
104.16.81.12
104.16.81.24
104.16.81.125
104.16.81.40
104.16.81.133
104.16.81.68
104.16.81.101
104.16.81.23
104.16.81.155
104.16.81.112
104.16.81.106
104.16.81.67
104.16.81.82
104.16.81.157
104.16.81.6
104.16.81.1
104.16.81.110
104.16.81.72
104.16.81.10
104.16.81.16
104.16.81.126
104.16.81.75
104.16.81.53
104.16.81.134
104.16.81.119
104.16.81.156
104.16.81.2
104.16.81.91
104.16.81.45
104.16.81.21
104.16.81.77
104.16.81.73
104.16.81.66
104.16.81.19
104.16.81.32
104.16.81.88
104.16.81.132
104.16.81.74
104.16.81.8
104.16.81.18
104.16.81.121
104.16.81.48
104.16.81.145
104.16.81.51
104.16.81.13
104.16.81.104
104.16.81.80
104.16.81.42
104.16.81.144
104.16.81.111
104.16.81.105
104.16.81.118
104.16.81.117
104.16.81.26
104.16.81.78
104.16.81.159
104.16.81.57
104.16.81.25
104.16.81.60
104.16.81.54
104.16.81.149
104.16.81.136
104.16.81.97
104.16.81.38
104.16.81.90
104.16.81.137
104.16.81.140
104.16.81.59
104.16.81.22
104.16.81.41
104.16.81.150
104.16.81.64
104.16.81.31
104.16.81.33
104.16.81.61
104.16.81.76
104.16.81.69
104.16.81.46
104.16.81.49
104.16.81.35
104.16.81.50
104.16.81.79
104.16.81.34
104.16.81.93
104.16.81.102
104.16.81.129
104.16.81.71
104.16.81.115
104.16.81.92
104.16.81.5
104.16.81.99
104.16.81.84
104.16.81.130
104.16.81.128
104.16.81.47
104.16.81.36
104.16.81.96
104.16.81.9
104.16.81.37
104.16.81.4
104.16.81.124
104.16.81.58
104.16.81.52
104.16.81.55
104.16.81.113
104.16.81.44
104.16.81.65
104.16.81.138
104.16.81.95
104.16.81.29
104.16.81.135
104.16.81.56
104.16.81.108
104.16.81.103</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/5623" target="_blank">📅 18:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
مدل بعدی Grok از xAI ممکن است ظرف ۲ تا ۳ هفته آینده عرضه شود
👀
⚡
گزارش‌ها حاکی از آن است که مدل جدید ممکن است از مدل پایه بسیار بزرگ‌تر ۱.۵ تریلیون پارامتری V9-Medium استفاده کند که جهش عظیمی نسبت به معماری ۰.۵ تریلیون پارامتری V8-Small در Grok 4.3 است.
جزئیات جالب دیگر:
گفته می‌شود داده‌های کدنویسی Cursor برای آموزش اضافی استفاده می‌شود.
Grok5؟
👀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/5622" target="_blank">📅 18:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">#اختصاصی
🌐
دامنه‌های رایگان برای هر پروژه‌ای
https://github.com/DigitalPlatDev/FreeDomain
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5621" target="_blank">📅 18:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbhU-NQ1BvMlTp90Bb-WruJk61MTXMIihvDMHUfggEsiOlkUwAUCQ-tpW91PqPqFsNAx1P0W2419dMouxlZRAZuYDh1zqSct62fvW0MvorVfe3yyT4Jk-APLBb1_1cY0EXa7NQqiKwnNfytB3vFgu-FOBDv4fWPhZw03yXl_Uc0cnOk5l4-kLrywNXjF32AtS7KNv-lzkILGfsVm_enkNliq_8ztwBjbL__BHRyP8W13oRzS1p7U2FTJM4wIw8ijKGFyxqDC12msq9o-yDyUiOO4KcRmzo1bD22WZsDlak1N5VTQG2TvCU1QKTZoJQk-1fHzfIs8BUqcitrg5ET1mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Defyx VPN  رایتل سرعت بالا  https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn  @ArchiveTell</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/archivetell/5620" target="_blank">📅 17:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Defyx VPN
رایتل سرعت بالا
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/archivetell/5619" target="_blank">📅 17:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5618">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">configs.txt</div>
  <div class="tg-doc-extra">195.4 KB</div>
</div>
<a href="https://t.me/archivetell/5618" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دوستان میتونین با Hiddify روی سرور های رایگانش وصل بشید یا از گیت هاب بگردین دنبال ساب بندازین داخلش
👋
**میتونین داخل Github هم بگردین ساب های مختلف و وارد اپ کنین و تست بگیرید
👍
لینک دانلود داخلی Hiddify
👋
💀
@archivetell</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/archivetell/5618" target="_blank">📅 16:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5617">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHNXIogQ-RwYhmGHIO3Owr8kZkE4Cbg2iUYghEsKeM9-IqEwQFAtDWoIWbH7B2M_h2YEZcnJWdagkX65Ke6bxpdQFLj-7khlaMBoRETvsYfbRFwqxiF2DlxnKnjlKGw91bJXuz54bGzLSaY2ogt7ZZ4ex6hC9qOs5xfD8JlnoaRaWQrUz2zxS7xElYvfdXplN_eLtf5M3wt2ea1bnQ36Pc-LxmzsXJxodXHty2TcV_V9J9UqQIJib2JWsWFy5ZMDOEgrbYq_2b-Vgze4xN73HkSx7BOACbMPlX7TzAH-KMk6WG3hWifG4ZS9cIITwzoSmFuiGLW9PhbdneDa51IfvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان میتونین با Hiddify روی سرور های رایگانش وصل بشید یا از گیت هاب بگردین دنبال ساب بندازین داخلش
👋
**میتونین داخل Github هم بگردین ساب های مختلف و وارد اپ کنین و تست بگیرید
👍
لینک دانلود داخلی Hiddify
👋
💀
@archivetell</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/archivetell/5617" target="_blank">📅 16:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/archivetell/5616" target="_blank">📅 15:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uADKu438IexKhjcIi52sgymQaqjdvWqOpHsIpe_6csUmRXZPrImvcYfzHNB0pDH_5_S0hRNlgYMtREzCUntyzadBqa0purD6rrtpOtlzemJqiNUHlQ7MYeTzz7KQ9p5QsIJxiXMzfvM44VEIANRJC0Aga2eloYqSYA9yLfeYJawaKfrbCCtrXdoqyEpx3HvHFJ60dT1TF95ii4TJeVYN_e2fU75Sqb-1r34x3v76WQLRF_dYWumK7vCD1uAzqjiDQUaB5E1oAhLGKtscR0Z-yVNfgP7h_D6da-7wGrne0jeZAzEF00mUTPb8Cubq7-sfuLlGIG-U53brqvghvHOm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">162.159.192.1
162.159.193.3
162.159.195.1
برای وارپ وایرگارد با این آیپی وصل شدم.
پینگ می ده، لوکیش ایران می زنه
😂
ولی تلگرامم الا بالاس دارم باهاش پیام می دم.</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/archivetell/5615" target="_blank">📅 13:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">در کل این اپلیکیشن D-Tools خیلی خوبه ولی حیف توسعه داده نمی شه، وگرنه یه اسکنر Google CDN و Cloudflare CDN و Fastly CDN می‌آورد خیلی خوب می شد.</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/archivetell/5613" target="_blank">📅 13:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">در کل این اپلیکیشن D-Tools خیلی خوبه ولی حیف توسعه داده نمی شه، وگرنه یه اسکنر Google CDN و Cloudflare CDN و Fastly CDN می‌آورد خیلی خوب می شد.</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/archivetell/5612" target="_blank">📅 13:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu6qjcIqp47tBE-6XwNziihFCV01_F_mvPSGzYXgv-ByMdwBhkrQ6IJ4qf7bo6NFHyZYeVILbEZwvGG3uBJKTB0yzECBRJ4BxNFV0SzOKqr96vbB2EIUVUxzIhXsULDTk2Oyo1QtE7EURcVZZ5OjYf-CVfIK7lCBoji9UD_F2Ac9E4Aes5y_4-8lx3MPV-1K4gNGlAALw2bRlbg299IkW9qVTOZzqhTDJnITAsKOHLXcvjB-CwY7OyYErJgVzf9EWxTw9LEjcBhvD4BtUGTwD0f2tTUvunTT5LvzZgfCrAhgR8QfSugwx2gq_MgiMnRBiolAaBk121x9gz0rLM2Uxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ساختن وارپ به این نیاز نیستا.  کانتریبیوتر v2ray، یک ریپو داره به اسم D-Tools. اپلیکیشن از پلی استور حذف شده ولی توی اینترنت پیدا می شه به شکل xapk. بدون سرور مجازی براتون کانفیگ warp می سازه.  {   "local_address": [     "172.16.0.2/32",     "2606:47…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/archivetell/5611" target="_blank">📅 13:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">D-Tools_0.0.6_apkcombo.com.xapk</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/archivetell/5610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینم فایل اپلیکیشنش.
😊
@archivetell</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/5610" target="_blank">📅 13:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5J00PorXXhdmyxx7uiw_BIp5VatnEzn6cs5TPRfCfbZR7A-l64Nl8vG4GUrPuVZZKRjeH-PkdE3dpPRcyXHHtb2bZ1vESz41xbltQBxxHDSU9vSH4bf_HXd7O3hGV29skGkrk1o8JsTXV3k3EJ0wO4XT0aAwNcYewBuWXykwr0NPq66fayQ6_X_gz3yKOXJ69Gf1xAALyPgRpyjLb0o11jkQyX5v9HNU4jcacW4sCxaatj9zePDrMmYFYL59QbiyOUUHerzHNCoq5QvCgfJ84lh7D0WTLFEuu3JGyhYkuE48OOSx-9RIzUy0Z_BveN-LEQI-vfwSRPv89Elpi50Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش ساخت کانفیگ وارپ (نیاز به سرور مجازی )  با استفاده از الگوهای زیر، کانفیگ اختصاصی خودتون رو بسازید :  کانفیگ‌های خام:  warp://licence@ip:port/?ifp=40-80&ifps=50-100&ifpd=2-4&ifpm=m4  warp://licences@ip:port/?ifp=30-60&ifps=50-100&ifpd=3-6&ifpm=m6 برای…</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/archivetell/5608" target="_blank">📅 13:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌐
بات تست رایگان بدون رفرال (خرید نزنید)
@Cheap_v2ray_bot</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/archivetell/5607" target="_blank">📅 13:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آموزش ساخت کانفیگ وارپ (نیاز به سرور مجازی )
با استفاده از الگوهای زیر، کانفیگ اختصاصی خودتون رو بسازید :
کانفیگ‌های خام:
warp://licence@ip:port/?ifp=40-80&ifps=50-100&ifpd=2-4&ifpm=m4
warp://licences@ip:port/?ifp=30-60&ifps=50-100&ifpd=3-6&ifpm=m6
برای استخراج لایسنس، آی‌پی و پورت مورد نیاز، اسکریپت زیر رو اجرا و مقادیر رو در الگو جایگذاری کنید:
اسکریپت استخراج:
bash <(curl -fsSL https://raw.githubusercontent.com/Ptechgithub/warp/main/endip/install.sh)
☑️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/archivetell/5606" target="_blank">📅 12:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">همراه اول
Windscribe UDP 443 Censorship On Dallas BBQ
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/archivetell/5605" target="_blank">📅 12:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کسایی که سرور دارن.
اینباند:
Vless+xhttp+tls+Cloudflare clean ip
بزنین با آی‌پی تمیز کلادفلیر
عالی وصله‌
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/archivetell/5604" target="_blank">📅 12:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">همراه اول
Windscribe UDP 443 Censorship On Atlanta Peachtree
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/archivetell/5603" target="_blank">📅 12:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">و اینکه، نرم افزار Karing گزینه وارپش کار می کنه و پینگ داره و کار می‌کنه.
😊
@archivetell</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/archivetell/5602" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">واقعا باورم نمی شه مردم چقدر می تونن عقده ای بشن.
📘
مگه ما فروشنده ها چیکارتون کردیم؟
😭
طرف با کانفیگ رایگان بعد ۹۰ روز وصل شده زنگ می زنه مسخره کنه. چه رویی دارین خدایی.
حالا من به وصل شدنشون می گم وصل، طرف فقط می تونه با کانفیگش پینگ بگیره
🤡
😊
@archivetell</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/archivetell/5601" target="_blank">📅 12:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">لینک داخلی
Am tunnle
(pro)
Am tunnle
(lite)
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/archivetell/5600" target="_blank">📅 11:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">AM TUNNEL
سرور ۱۶ fast dns روی ایرانسل و همراه اول سرعتش خیلی بالاست
https://play.google.com/store/apps/details?id=app.vpn.amtunnelpro
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/archivetell/5598" target="_blank">📅 11:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEQ38B2YSMBaEYXWRG7vU_HvFxuENSlTC8nPJBa5NksbBHoOJEuKo4khFC7O--_ZiO0toSGerUq3jW6GIi5wSY-ypEhI_knwE6QHOifm9rZplSGJls9QiWzFjXuOPKrHDZHkyy33jwknyfU17a2GbDzLX0vvfz7f3aQdpPm5Q_WrnhraH4lEyKcTBA7OWmeTCnrUWvQsQfz_hc5stD1UWIwggUmYHhX47jq3rDqV9w7ybTW2acyMd9Xh8YyPpaGBHaf5ElxmXZ4wrOnMOxna2kroTqp_3bNK8jEDBAAXF6ke8vTE65DO41c9RtcS9CtXa313VgVyn4VROORJi6rTNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Optimize-Windows
اسکریپت‌های بهینه‌سازی و ساده‌سازی نصب ویندوز
https://github.com/ShivamXD6/Optimize-Windows
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/archivetell/5597" target="_blank">📅 10:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcxBZqP7FN024eGD4hInMlHgEueq9Wopd95oqba4fsxtVszz8LhAK7FuI2TOg3R2G_HGt3gQwjrqiQZTfXLyr4CI9wGDhju7zUa0w3kMl1BI6WZ66GovqnbRjSJ_QRs29mgjJfuRmyzUBXtGPm6P_w63zMubi1mCxNILiUD9T8Jw0CRravfcP2vkTzbfuR6s3-3WucaWfMaP7I6jVfCe19s8CBXjYuLMmEAuTNM0fiRtOgh5hslEt72hX_PKH6nn4na9rtN1A9m8RYksGf8YxjeArDiQ6I5NEqWPP2Mq8Buv5P6vYh3rO0ObTETwIvZV-08G9zjOrxo0WE1ZcIMFxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYgn9Xkd6BhY0VcC644evdOXKNyTQRGX76d6bkZjYSIFTLKqRgI4H0NyvXgoxPp6wsRleOPlgqc7wSwjnDY0WMdKxyLzPOpE7ZxpQQsVqmG_2-JYJdONrC60vE2ugHLa-Uvz3aVymB6wIVNUllIhi0VEV9X2Gs7r9b687p5ckrFZsjhi48yNJTnHevPhIiLQ_l6l7GPgFIzo5I0GhsbNI5teSuOcz5Kh2aWKyNgE8I36gMWPlvzyhCydwi3tpqPtfSlAa7YGlUN0lXCv_CMUSsuAOqIs2MBLcXFG-eQJjOs3FeiUWIxtGhpDbYRUyunYaAz3-KUHSPyFllB0cjFn3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0SXHXm8M216vfHP13MJtSDUq-L70Ae0-_Dl0XWGZu2NDGtI3TZdSEtV5Cqqd61ZJ96kcdx6Ye6Q652qNTdQs4hGdCBAGNKUPuvuwgCxah1BD44lOsXlX20KfQ2qEtOeVjbhEFW0FNTeT6Luo04RQ4GL3hs_jG5cpque5TSlFFlcifRGZ3gsgvK1wfhu0-50uPM7LG2QPFAhYQYVGN8vxnQv-7zuYju0_evCxKfoweQTJvO1NGvYMEUiC0NSmm9_fFzRlcopyWqHjtkCoYmn9DhEAOvoAEF9WuZATN1apZ97rXCBlFDT16itDUqGPxgzjN4h89ckViGeKPOWCLDhIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnIM9lcIZ37UAYPv7ujxCTIal9pH7OCwjGWUhZiMkqxYf-JxS0rxkLKv2pICd4VSsHfoKeS6B1HdPuH8TC-fgscpRRK6Y0HkqMF-ojN4w9C1zY2YbnyV_GcvXqxQaP1lnEFew6VRR3KSUGh0oJ53OJg--P9O2FYhIv5Mf8MufXOgKR3rCLCZ-mz75X7QdQHaA4YuJO_pj6PSBONSav99U85vlA7MJROcPUm0kLkh3KxiHvToDbDK-GAkRONFrH72zabnvSTjKNTmJx5MIkQA7qm80vXa29VqY8-zxDFm5rlk5PskkdueMGPnPRFYurBntM442amKWUV-oLbON7EXbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rKd6s6qfPCH9YdKPMq3nclLf3TI0Jo1653M6bR11cXdz9M4Bcot4LzKmOxvgfoyZ09dnH7xu2Wrn3RfF3pNde7sgM80ZnSqp6p6HZ1haktUJ9ZJRoXVMXLfIr2sMTAO6V71WtRvyU8yigRjhWu0z4MR5yHQRxjooq3jZKQU2snWocf96rToNkFGSA3eeY_d6-KHC7oH-315Yza4n1VtyK_tZg5vBAjva5IEzfdhdi7_7g_aPkvlU9C1Ff53aLuXiLTevk7T5nafoEAX5BCsPKU6-64aUqEcvjU7L8IzoK6QhotyIr0WbXsVeE7AF1Me_AMl9lTgxijtU1cuQy0RU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTtjc_CkhS1N26TOQQrruqRLtorKuk3hF65GfBhLJvueS96T96T3WJeCAeGpeaIQh-7B0zwW0jvQen6UDSF2EcHIm15-nPE3WDIM-pIZAjjsakXB9iaAZCdHymMngSolBfguzCsq61fWjrXRsJpILpNc1w4i9aRs2HZQpIV3hEXOGR9PDvhKCxP3-VOsMgEIJwp9Vrz1E6blIS6tZiAdt428QafaSEFi7CfEIhlbyEv55vN-5qbm92YmcJNETOcZYzUUyqZj4DWQ4Im4uO5szzXYyQjYFUjWSPKwnEKYkP1ChgLZL6SDR5gW9YNT-s00MQC7DeV8t1RP-JhIav26MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltnbJ0l3CP1mQPCe0hphjEK4IewYVvVK8VmJ70i-DNQkuK_3YPWF98JjyeSd4izI-vIqG4Xn3WoPfpgcje6iCJUqdLB72OIBJa8RKWIrtymanGpdsLi9mNBsBz98BgmRVwvfRgbjKeMeQSfw_oNj__uFIYNoiNIxg8b-ZxzEHCIcj5R5nRxfZk8g5i1Z_IoAzsZ-quNdJeNTC148X09XrZI2b28CTAuudwMMr9uHMSEf8p0PFjEvCPorp1ozYDIzJaUQRyC2xjtwsKejVwMmXwNp6eHnSL7XSpGt2ZUoGJvlHZdjrFNRdYD8VI89HKSJQ5eiTOP2p4hEG6qBXy9ktQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ربات دریافت پل تور
@GetBridgesBot
پل webtunnel سامانتل و ایرانسل وصله
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/5590" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Invizible_Pro__beta_ver.2.6.9.apk</div>
  <div class="tg-doc-extra">38.1 MB</div>
</div>
<a href="https://t.me/archivetell/5588" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">InviZible Pro beta 2.6.9
* Updated Tor to version 4.9.8.</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/5588" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gh2R8MSxWNx0Vx4lOg6D0GDKHSZypykXpXMZ6IScJL8vygjQIqrtpT9YX9_TkcfHK0Vpzv2MvD9yWn4t7fwEyzRsFo8jR9p7PzxrbX0Fs7Feb-yOduitGHgbkDUEvyykZx0mkrnUaIcAyxjuiF9lhMw0T2OsEmFnP-897lkEx736aiYdpkov1Tylz_oHUHngbXEFeKJlzMKNYP4AUkTqbZloBpANecbRRMB3qpAtSWzsrEokxaNiJAEgIlsDJbZBlb8LKsr8AERQ7X574fgA94Yhh2fQKffb5e9TGp5kalR8JFcGO82czU_uLnErvLNPZOuGIV2Fc9j-dgpbWkmoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش invizible pro به زودی..</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/archivetell/5587" target="_blank">📅 09:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">MetaMask یا Trust Wallet?
🤔
👇</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/5586" target="_blank">📅 09:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">BD NET VPN
مخابرات، متصل
سرور BCCF 01
@ArchiveTell
https://play.google.com/store/apps/details?id=dastan.prince.bdfreevpn&hl=en-US</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/archivetell/5585" target="_blank">📅 09:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شیر و خورشید بدون آیپی
مخابرات ، همراه اول و ایرانسل وصله
تنظیمات رو به حالت اولیه برگردون ( کلیر دیتا ) و پروتکل رو بذار رو CDN ، متصل میشی ( کمی صبر نیازه )
﻿
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5584" target="_blank">📅 09:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آیپی تمیز کلودفلر سامانتل
208.103.161.170
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/archivetell/5583" target="_blank">📅 08:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">📱
صد گیگ کانفیگ اوتلاین به همراه شادوساکس بهتون میده
✅
( پروکسی ام میتونین انتخاب کنین )
@OutlineKeysRobot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/archivetell/5582" target="_blank">📅 05:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کلا tor برای وبگردیه فقط، هیچکدوم سرعت خاصی ندارن.  وقتی وصل شدین برین یکم تو این سایت وبگردی کنین
😊
https://tor.taxi/
اونایی که می دونن
🔫
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/archivetell/5578" target="_blank">📅 02:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwMtUqDhDRoCg3x11hkGjIuTM4Rhh5Qw7L12WWbCT8LfcGht9inDESY-R_xqk8M6cvUawU1Czg5xCX6DyAtHy5P806xA1a6TJ0t_brtyHP9yQkQK25ZpJD9NhqrHqo8KBqAifn7Yn04jUMsRVpzX8TF3ZrCrQIi00zn6ljaX6fXNMkOHBA6lGGwoZZngk9UWIr8aoCbvNMtzcZRupV0aY8nbe9zrWmDetnO4DGImlFWGcf9Spr5zl5-29NfvywWv35KX5svT4NJ-Nh0li1ZSehhYEApKd29DvddESKTizSY2zDtXEzy2Vh0trmf7pMdUySmzBO_wYkXmHYrgws7jLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کلا از نظر سرعت بخوایم مقایسه کنیم ظاهرا به ترتیب Obfs4/WebTunnel Meek Azure Snowflake اگه اشتباه نکنم</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/archivetell/5577" target="_blank">📅 02:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5576">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">octohide VPN
ایرانسل سرعت عالی
لینک گوگل پلی
از ربات
@octohide_bot
کد ۳ ماهشو بگیرین فعال کنین
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/archivetell/5576" target="_blank">📅 02:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🟢
نسخه جدید Argo VPN (اندروید)
🔺
بخش Network type رو روی Public Network قرار بدید و متصل بشید
اگه ارور داد یکبار برنامه رو ببندید و دوباره وارد بشید
https://dl.toolschi.com/view.php?f=ac33499153243a31.zip
(لینک دانلودداخلی)</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/archivetell/5575" target="_blank">📅 02:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کلا tor برای وبگردیه فقط، هیچکدوم سرعت خاصی ندارن.  وقتی وصل شدین برین یکم تو این سایت وبگردی کنین
😊
https://tor.taxi/
اونایی که می دونن
🔫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5574" target="_blank">📅 02:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivU0mNupD8GAnzq2Si9oujoZ3LG69qKY88NS2K74zm9aRfpegc_mET1rZn-_BmJo6i8YwmbtixKRs_GPry3q0x0BFs3zpflYtlmj3fWn0qY76GmjzLPO4CJWun17pYgb4MXEzMOxW3Qo-7M7S7bu1SCNPCf28Ln8TeIVN0oRv97kAG1HPyVGQybuFfw-4n46asgo4YKl4FC1odcioqHmIvLjotGV8XeZRVhdv3HY1wqDO3TVvRnCq7iQUtqyIIFGJAsSftvR-zd2gpagvmKhdsKyowsXK1PNFC5-M-dNkSMdNz74Knc21b0EgpbSCLNnTz748QYNmOE1Ri2ARjWJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلا tor برای وبگردیه فقط، هیچکدوم سرعت خاصی ندارن.  وقتی وصل شدین برین یکم تو این سایت وبگردی کنین
😊
https://tor.taxi/
اونایی که می دونن
🔫
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/archivetell/5573" target="_blank">📅 02:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5572">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوستان کلا از نظر سرعت بخوایم مقایسه کنیم ظاهرا به ترتیب Obfs4/WebTunnel Meek Azure Snowflake اگه اشتباه نکنم</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/archivetell/5572" target="_blank">📅 02:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوستان کلا از نظر سرعت بخوایم مقایسه کنیم ظاهرا به ترتیب
Obfs4/WebTunnel
Meek Azure
Snowflake
اگه اشتباه نکنم</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/archivetell/5571" target="_blank">📅 00:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5570">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کلاینت های Exclave, SlipNet از ssh پشتیبانی میکنن
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/archivetell/5570" target="_blank">📅 00:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxIJB_q9HnMGV8r1br_hnplTrNJCc5EliL3qvrOwnoyAzJ7dX-5qxM5MrxLABQDVfwfSJvy_U9sJQr4MHe1Vc-iE-hANa2eXB2d7AQrrVxPkAOOuOaVLRzt0MbmX-ZGhdRA97H-SSseibADw64eVQDtLwLIqSonMEJX-eHWhE0TdukHcosXqQOYgztWMiH6qXdQ3NepqbONXjXVFLHkJsMHa14RDJ3DxmyOjd-ub6Wu2k_MTYhYBsgjbCEeYLJrsk-LcMfDjbULRDGXzpouNjzdTtbDzAERTIJ3_PJkLWCJjdbYHL6SwLUVY2XyeYjbTNC2bucZctKY1hObPhKNwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iAnHhUlcqD2LrjbqPAC0B3kNYLc0jcg1V48oKaGJz0nqLNGaX23ka96TEYktX98CN10WRmnc-yPdavJBGc5Wry5F8I4GvS1P2OkerBNRuKoDL4rWM1zBNGUqXOb9p5y4Spl4jP4FaLuVSi0jKyktTnyYGN2O5OvgJAZVMEemy9MrZonGw-aoewujlhtskFs8ioGz7H1aneND8Tn_qXH882-Sp_XqGvtawnggYojsIZhD6N-34FRLeVw4TwitzlFzDXOkQEM58LYMVLsjf00fgzVPxIWzlnwGLfTm71usCnUI5WDiXlXdLNNwwA1Wu8_U5HAmjqH7JDeoWBTfpL7kag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hqV6ot8E7E59DWHuSaTlNCghpxVJyB-KZfUcFY1pd0J78-_5dOsyLtJ5AtwMeaM2RSk9xz9jvqSZ_FvP85pvOuVBskzYkdyrB1-Kkiajdr_c1CnGveIrqWGjwBOseDn--S6kDA0UDK1OOPaQSm-5ltLHBIR6nCnLbjYqVZCPj1CcdwZq_mwL84hHp4Zd74nhqpXAmkZb-F1u-840bz_FtbQV9SsGITtjm859OMCPVYmM-RK5YvmN_4tFirKweLhH8umC5hAEcKD6h13L-3aAqXKNP1tjET2d_m_AI8TEH14Xz-0AIvrqDT4uj_ns-28nnULmFTufq0NIvOWoXWKO1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hqVIqzKg-5U5BshmmXKAkWK03eFkt1rlHwgoeRfTkj1K23qem46jC2IuZ8eYQRXUoknHPCy_h1HNNM-JAhQOR3HEIZR4nBU-OSEoqDsa3CE7-8P2G2Q4zDafEUyBr9DF89zwkpuKb4ojjI0Kb3Otd1Vkv_ey8ZeaplqgJ_Hc4kZNtyDg8_4F_7fqn-Gphiid_rmRqzkJVLNr6BEBXYUgw92tL8LNghjUQNMsZWbjM4Jpsrqu2LmJxDi5SeksJtj5cFbQb3KOtnu8Ybi70mkw5kChqWT0TU0dgif47u0OXl5K6EL0Fwz2NzQta3xjRahJIKYPTInFdN1Cj6CKTl7byw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4Cs57PGimMWhxxU2fXsm-Gfqr-T2CBCkhCjTKKTGR7TCfFE_5A3WZvbeiixw_jkbkDMF4tsOQ5O393xxArGvJQbVSr4Jzt4GK5sf_-YwzJLOxyurjwfAAim1pE7Hw6LQ6eOqH92AZTrjTK0c1gcz6SWum5cNbSxkGvf8ZbrcQELuHVmj1j_AwsRT96LDoTSmhuR1vfq2rvGa3dJlgYIRiU_nebWh_K95iv0w0Ub7XcKP485c5ipjhpxsfQN9h8nvtIv8HJ8gSq4TwLYFBS7P-8liFONvTHQPSHtTmeWfD1I33JgzUz6De-jpuqz5dnxa-TrPKJISW3H28z8aMvoeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EfVvXX1ogM_9FXv9qQxiBi6YAfSsxh2vMvNu9J-cIzI9dzYzMmkmtHjH3EtAPLhHrn7QyEBS49XNCQx6gte7qm9V12cy9K3RFFRSZiVj7n2ARfwc5tOzLJipDJmsXcnhjYdrdXTxWft5_1oFU0k5lGu699YDVdU4V1rP-yPySVmWla1ekrpgzCM6GGwEGjf1TSN-fHSWg_fT7UXSTSyf5nZU6fCPXLd4OruX0VFRyi60cb5MyZ3lXJ14186MbV6okr1R3PYjPdsBPjQyLOP_-K8Obsy-V97tPSGZkyYMrgezK6OCuZ7Oxvit7_SaiKJJjE-1dO2cB8yQtX8Cf3M10g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از بالا چپ به راست
اتصال Tor با برنامه اسلیپ نت
پل Obfs4
بقیه هم میتونید تست کنید
Snowflake, Meek Azure
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/archivetell/5564" target="_blank">📅 00:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پاکت هدیه
🎁</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/archivetell/5563" target="_blank">📅 00:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سوپرایز anonvector
❤️
🚀
آپدیت جدید و هوشمند کلاینت SlipNet (نسخه v2.5.5)
---
نسخه جدید اپلیکیشن
SlipNet
منتشر شد. توی این آپدیت، سازنده تمرکز اصلیش رو روی هوشمندسازیِ فرآیند اتصال و تنظیمات DNS گذاشته تا کانکشن‌ها خیلی سریع‌تر و پایدارتر بشن.
✨
مهم‌ترین قابلیت‌های این نسخه:
🔸
تنظیم خودکار شبکه (DNS Auto-Tune):
برنامه حالا می‌تونه به صورت کاملاً هوشمند، پارامترهای حساس مثل
Query Length
و
Rate Limit
رو بر اساس وضعیتِ فعلیِ اینترنت شما (برای کانفیگ‌های DNSTT، NoizDNS و VayDNS) تشخیص بده و موقع اتصال تنظیم کنه.
🔸
انتخاب خودکارِ بهترین دی‌ان‌اس (DNS Pool):
اگه این قابلیت رو از تنظیمات فعال کنید، برنامه قبل از هر اتصال لیست DNSها رو اسکن می‌کنه و ۱۰ تا از سریع‌ترین‌ها (با کمترین پینگ) رو برای کانفیگ شما ست می‌کنه. *(دو حالت اسکن سریع ۱۰ ثانیه‌ای و اسکن دقیق ۱۸ ثانیه‌ای هم داره).*
🔸
اسکنر و مدیریت پیشرفته DNS:
حالا می‌تونید آی‌پی‌های سالمی که اسکن کردید رو در قالب یک گروه یا استخر (Pool) ذخیره کنید و هر زمان که خواستید با یک دکمه فوراً لودشون کنید.
🔸
بهبودهای ظاهری و امنیتی (UI):
- منوی اضافه کردن کانفیگ جمع‌وجورتر شده.
- می‌تونید برای باز کردنِ باندل‌ها و قفل کردنِ پروفایل‌ها، پسوردهای کاملاً مجزا و مستقل تعیین کنید.
---
📥
دریافت آپدیت:
می‌تونید فایل نصبی این نسخه رو مستقیماً از لینک گیت‌هاب زیر (بخش Releases) دانلود و نصب کنید:
🔗
https://github.com/anonvector/SlipNet/releases/tag/v2.5.5
📌
#آپدیت
#SlipNet
#فیلترشکن
#اندروید
#DNS
#تونل
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/archivetell/5562" target="_blank">📅 23:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SlipNet-v2.5.5-full-release-arm64-v8a.apk</div>
  <div class="tg-doc-extra">25.7 MB</div>
</div>
<a href="https://t.me/archivetell/5554" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/5554" target="_blank">📅 23:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-text">v2.5.5 Changelog
🌐
DNS Pool (New)
•
Auto-Scan:
Automatically picks the top 10 lowest-latency resolvers at connect.
•
Verification Toggle:
Faster scans by default (10s timeout); optional full HTTP/SSH verification (18s timeout).
⚡️
DNS Auto-Tune (New)
• Auto-tunes query length and rate limits for DNSTT, NoizDNS, and VayDNS profiles at connect.
🔍
DNS Scanner
• Save working IPs as named pools and load them instantly via a new button.
🎨
UI Improvements
• Replaced the "add-profile" bottom sheet with a compact 3-column grid.
• Moved DNS section above Network in Settings.
• Independently set bundle-decrypt and per-profile lock passwords.
———————
✨
قابلیت‌های اصلی جدید این نسخه:
قابلیت Auto Tune: تشخیص و تنظیم خودکار و هوشمند پارامترهای Query Length و Rate Limit بر اساس وضعیت شبکه.
قابلیت DNS Pool (قابل فعال‌سازی در تنظیمات): اسکن خودکار و سریع لیست DNSها قبل از هر اتصال، و ست کردن بهترین و سریع‌ترین Resolver روی کانفیگ.
بهود رابط کاربری و رفع باگ
دانلود از گیت هاب:
https://github.com/anonvector/SlipNet/releases/tag/v2.5.5
🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5553" target="_blank">📅 23:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAdh_N5ffjnkPccPEgaDKMvvGyEk8cAwhzpY-7B1y8NWIsBUByQOvoSPM84LJgdm09C2jv3HuifqwEW3BWCt4oBJ5UOUtPsPZ7wWtpf-xtRRMRuxSDkzUgOfLLkKX84cd2l_yKc0yp0agHSxN2c-Ggp5pso7qvRIHwM3l6X_p6eApskjN79xyYgZwKHLjg7LRu2MQWyl4mo_EyQJLD4u6GfdQ6ntBzt83xpUFvRdsIfzUQwMTZumrncaDyF_LXnvkCSpmbcQCWJzQHPGRAmXQU10g0z78gnOy_UfTlygdo1XQ64OcIiQmNFu1FApqi4UP7879F55T6l3OIc6F7BacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله  یکم لایک و انرژی بدین اپ تر و تمیز که رو ایرانسل کانکت میشه یافتم
🙊
🙈
❤️</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/archivetell/5552" target="_blank">📅 23:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5551">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سبحان الله  یکم لایک و انرژی بدین اپ تر و تمیز که رو ایرانسل کانکت میشه یافتم
🙊
🙈
❤️</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/archivetell/5551" target="_blank">📅 23:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سبحان الله
یکم لایک و انرژی بدین
اپ تر و تمیز که رو ایرانسل کانکت میشه یافتم
🙊
🙈
❤️</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/archivetell/5550" target="_blank">📅 23:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نت شخمی نشده؟
کانفیگا پولی هم بد وصله
😐
😂</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/archivetell/5549" target="_blank">📅 23:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ایرانسل پر سرعت وصل
Windscribe UDP 443 Censorship On
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/archivetell/5548" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">همراه اول تست شده
vless://06ef598c-1555-4887-b3f9-08214a2f6792@104.16.7.70:443?encryption=none&host=2026.hhhhh.eu.org&path=%2F222.167.202.31%3A7443&security=tls&sni=2026.hhhhh.eu.org&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/archivetell/5547" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سامانتل بدون فیلتره اینستا
😁</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/archivetell/5546" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سامانتل بدون فیلتره اینستا
😁</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/archivetell/5545" target="_blank">📅 22:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompatterniha</strong></div>
<div class="tg-text">پیامهای تشکر و محبت آمیز زیادی دریافت کردم، ظاهرا به خواست خدا وارد قلب هزاران نفر از مردم شدم، فقط میتونم بگم از همگیتون ممنونم.
البته به نظر من کمک اصلی رو "امین محمودی" کرد، پروژه های mhr و masterDNS بینظیر بودن و باعث شد عده ی زیادی متصل بمونن.
واقعا با یک تلاش دسته‌جمعی درصد قابل توجهی از خرید کانفیگهای گران قیمت بی نیاز بودن، افرادی مثل "aleskxyz" ،
"ناکر" ، "samim"، "Sarto" , "shahab", "گروه وایت dns", "مارک پشم‌فروش"  ، "Break_The_Barriers" , "CyberNigga" , "بیا پایین بچه"و ... کمک شایانی در این قضیه انجام دادن.
عده ی زیادی هم تو بحث آموزش این متدها نقش داشتند، عزیرانی مثل "متین سنپای" که آموزشهای روان و ویدیویی در اختیار عموم قرار میدادن که بدون آن قطعا عده‌ی زیادی نمیتونستند از این متدها استفاده کنند.
همچنین جا داره از RPRX بنیان گذار project-X که توجه ویژه ای به ایرانی ها داشت هم تشکر کنم، واقعا v2ray الان به ابزار اصلی ارتباطات اینترنتی تبدیل شده.
از دوست چینیمون "zhc" هم بسیار سپاسگزارم، با دانش بینظیرش کمک قابل توجه ای به مردم ایران کرد.
واقعا یک تلاش بینظیر دسته جمعی صورت گرفت که نمیشه از همه نام برد، من هم خوشحالم که نقشی در این زمینه داشتم، باز هم از همگیتون ممنونم
❤️
///
هنوز نت به طور کامل باز نشده ولی با متدهایی که در حال حاضر وجود داره باز شدن کوچکترین روزنه ای به معنی باز شدن کل اینترنت خواهد بود.</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5544" target="_blank">📅 22:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">همراه اول bdnet وصل</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5543" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHosseini.h</strong></div>
<div class="tg-text">همراه اول bdnet وصل</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/5542" target="_blank">📅 21:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑴𝒓 𝑯𝒂𝒎𝒊𝒅༗</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swsKqXJUvnA3omrpDh0qPvMOQP7bIKe2sWGx1sZSvYlMWo5DO5vrjJzLd2cII6-yO27oDMi3pay_2e3rPIr1iAaITz0tx3kX0Nzxzb407xcioShVvuzAVuiiM7S0oknKDO1x6xKuNOcmJaJlgr7iOHsOmpApuBCxL_vU6O5XY5Fl9lH3y_8PtavbNVAtOEy-yjJnNF1gKFmWLc_p9Q8K68qgkFwuJ8ejSiIP8BKbH102yijs-Pn-ixpPial3wTnP81U6URyuJ99jv6edfs1p6su3sqdtVGInN3F1k7yvWgVLTzJBT3C34ZwohFUoXtHO_Ivc-lP5VVinnwweG-o-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YpMjyzk4ay4uigIAtuDeEjio2xIBgGdIOVPOebzXZ3wW3k4LMFWjmQearnbKNuSAiJIqbW8aLVD0X1v2fABfftUci3UJnGHO4wrve5t0i_PpeKW2eBKIdj9ojQNOEInsrBRxacVS0Ug7KNAbnCszeLgO0dePXPxP2ERGL0G_idfW5IJZn6epIuatrHf_q8eeD24lG12UUlelZFKGcS78w29jvRqCutw4NIgVoOtj--wgoyBm1TDEY356xkTkfvDRktLbWNIbrEyDAPCGQxH3Z4hXUwVZ2tDg5iTtFcj6YLC-RYw6tkRTFc767l8u9IhhusIq-T9jtcTG6tAtgeazsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این دوتا وصل شدن همراه اول</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/archivetell/5540" target="_blank">📅 21:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">vless://IR_NETLIFY@194.59.183.234:42115?type=ws&encryption=none&path=%2F&host=&security=none#IR-NETLIFY
مستقیم وصل</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5538" target="_blank">📅 20:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">همراه اول کلودفلر وصل
trojan://8r%3C%5B9%27l6hAO%238ZQi@104.18.12.149:40443?allowInsecure=1&host=Koma-YT.PAGeS.Dev&path=%2Ftr&sni=Koma-YT.PAGeS.Dev&type=ws#%F0%9F%87%A8%F0%9F%87%A6%20Canada%20(CA)%20-%20Toronto%20@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5537" target="_blank">📅 20:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آیپی تمیز همراه اول
104.18.12.149
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5536" target="_blank">📅 20:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiliya</strong></div>
<div class="tg-text">اینم یادتون نره بزارید
شاید بدرد کسی بخوره مستقیم هم سایفون وصله</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5535" target="_blank">📅 20:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiliya</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PsiphonProSetup_x64.exe</div>
  <div class="tg-doc-extra">76.1 MB</div>
</div>
<a href="https://t.me/archivetell/5534" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/5534" target="_blank">📅 20:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiliya</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oy2hXSsJkQ_E25u9ghY3RVF5rsf3wNyFeQ5YFnSFReOW5bEvVgdGCE_LGNTwfv3iet6H_znLhyPeEr0gf2DWDZeNIJ0N58J-YIIDc9JjITS2hBoDumSLPSZoFMUSXcW3_QxmxZnhGiDuuMHZzadgwS_7BypcFJAp7Vi3cEGASzEWqZxhEUthPyk8GaCHwJUw-rg5DvypAyUbK-jAa0d-6MdtNBimBHnm0p9BXaXDt8_fuIJf9ALL-_90nEU2dbu_-Rx4bYVj_W_Y5tWSCLHeRqDBw0u8fe81Ly3cKRQGKSR856CBckREyJ8D9qEaVXReDPBRU3scP_qmJ8HK3Zv4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1rFkVEheauTJ0X15u99He3qRvbQr2teH67_rk0v5ucbfRLt7iTtnANA0RQjA-wrlFCtiXIuJHzVgbI3rOnssgCpKISdNKtR50QT4ZD_mkKNIyiZBsQUMD8Ma55F6CXzglFh4Ute75qV5PQI10zcjr77casgfp_65lvKqdCD3Kl7Ate2p-H-Wm09yD8j-o_xtM1bTR7M08pT5uP3fdLqSCVPSO8cPAAcE_IkGBt1J54gBjj0Isg_Jjzwa62zq42XPxOI-8jx6IT6m76ArU3tQku-9ZD3aYDGkUqW08O3HQiLKRx1GoD_axCNnX1HXx0BpR3DTbQK-YU2DqMuHz33vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برنامه ی سری تغییرات دادم و تو خود برنامه میشه کانفیگ زد ترکیبی وصل شد و بین مود های
psiphon
v2ray
v2ray+psiphon
جا ب جا شد</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/5532" target="_blank">📅 20:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آیپی تمیز ایرانسل   27.50.48.49 @ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/5531" target="_blank">📅 20:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آیپی تمیز ایرانسل   27.50.48.49 @ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5530" target="_blank">📅 20:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">https://t.me/proxy?server=191.101.113.153&port=443&secret=ee3ef807f06138530624d5631232bfa592636c6f7564666c6172652e636f6d
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5529" target="_blank">📅 20:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آیپی تمیز ایرانسل اسکن کردم   واستون میذارم
😁
❤️</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/5528" target="_blank">📅 20:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سیمکارت ها هم وصل شدن</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5527" target="_blank">📅 20:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آیپی تمیز ایرانسل اسکن کردم
واستون میذارم
😁
❤️</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5526" target="_blank">📅 20:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🛡
معرفی ابزار فوق‌العاده Paqctl: عبور از سخت‌ترین فیلترینگ‌ها با دور زدن DPI
---
اگر سرور مجازی (VPS) دارید اما آی‌پی‌تون مدام فیلتر میشه یا سرعتتون به خاطر سیستم‌های تشخیصِ هوشمند (DPI) افت می‌کنه، امروز ابزاری رو بهتون معرفی می‌کنم که قواعد بازی رو عوض کرده:
Paqctl
(بر پایه هسته قدرتمند Paqet).
💡
این ابزار چطور کار می‌کنه؟
روش کار این ابزار با V2ray یا کانفیگ‌های معمولی فرق داره. Paqet ترافیک شما رو از لایه‌های بسیار پایینِ شبکه (Raw Sockets) عبور میده. در واقع پکت‌های اینترنتی رو طوری "دستکاری" می‌کنه (مثلاً فلگ‌های TCP رو تغییر میده یا پکت‌های عمداً خراب می‌سازه) که سیستم فیلترینگ (DPI) گیج میشه، نمی‌تونه تشخیص بده این ترافیکِ پروکسی هست و در نتیجه اجازه عبور میده!
⚙️
دو روش قدرتمند در یک ابزار:
این اسکریپت به شما اجازه میده دو روش مختلف رو روی سرورتون نصب کنید:
۱.
روش Paqet (ساده و پیشنهادی):
از پروتکل KCP روی پکت‌های خام TCP استفاده می‌کنه. شناسایی این روش برای فایروال‌ها بی‌نهایت سخته. خروجی این روش یک پروکسی SOCKS5 روی پورت
1080
سیستم شماست.
۲.
روش GFK (مخصوص سانسور شدید):
از ترکیب پکت‌های "نقض‌شده" (Violated TCP) و تونل QUIC استفاده می‌کنه و در نهایت به یک هسته Xray وصل میشه (پورت
14000
). اگر اینترنتتون به شدت محدوده، این روش معجزه می‌کنه.
---
💻
آموزش نصب سریع (مخصوص لینوکس):
مرحله اول: راه‌اندازی روی سرور (VPS)
وارد سرور لینوکسی خودتون بشید و دستور زیر رو کپی و اجرا کنید (نیاز به دسترسی روت دارید):
curl -fsSL https://raw.githubusercontent.com/SamNet-dev/paqctl/main/paqctl.sh | sudo bash
بعد از نصب، با زدن دستور
sudo paqctl menu
یک منوی جذاب باز میشه که می‌تونید سرویس‌ها رو نصب، استارت یا مدیریت کنید.
برای دریافت اطلاعاتِ اتصال (آی‌پی، پورت و کلیدها) کافیه دستور
sudo paqctl info
رو بزنید.
مرحله دوم: راه‌اندازی روی کلاینت (ویندوز/مک/لینوکس)
ابزار Paqctl فایل‌های کلاینت رو هم در اختیارتون می‌ذاره. کلاینت رو روی سیستم خودتون اجرا می‌کنید و اطلاعاتی که در مرحله قبل گرفتید رو بهش میدید. کلاینت در پس‌زمینه اجرا میشه و به شما یک پورت SOCKS5 میده که می‌تونید اون رو در مرورگر، تلگرام یا برنامه‌هایی مثل v2rayN و NekoBox وارد کنید!
---
🔗
لینک‌های دانلود و گیت‌هاب پروژه:
سورس اصلی پروژه و آموزش‌های دقیق‌تر برای نصب کلاینت ویندوز رو می‌تونید از گیت‌هاب‌های زیر بردارید:
🌐
ابزار مدیریت و نصب آسان (SamNet):
https://github.com/SamNet-dev/paqctl
🌐
هسته اصلی و خام برنامه (hanselime):
https://github.com/hanselime/paqet
⚠️
نکته:
اجرای کلاینت روی ویندوز نیازمند نصب بودن پیش‌نیاز
Npcap
هست که داخل گیت‌هاب کامل توضیح داده شده.
اگر کسی این متدِ Raw Packet رو روی سرورش تست کرد، حتماً از وضعیت پینگ و پایداریش توی کامنت‌ها برامون بنویسه.
👇
📌
#آموزش
#سرور
#فیلترشکن
#VPS
#تونل
#Paqet
#Paqctl
#DPI
#لینوکس
#ویندوز
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5525" target="_blank">📅 20:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5524">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">همراه اول سورف شارک وصله</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/5524" target="_blank">📅 20:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ایرانسل cdn شیرو خورشید نسخه جدید وصله سرعت عالی
لینک داخلی شیر و خورشید</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/5523" target="_blank">📅 20:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترکیبی سایفون یا شیر و خورشید با v2ray
ایرانسل و همراه اول
trojan://humanity@193.151.152.206:40443?allowInsecure=1&host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5522" target="_blank">📅 20:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سلامتی اونی که امروز گیگ بالا اوتباند گرفته
😔
❤️
🍷</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5521" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
