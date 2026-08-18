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
<img src="https://cdn5.telesco.pe/file/t0_MR6ijhYrBFEcrt-FSWe_y9-c9apgqFwsLIO-PcTWL8T59ehh7qJbWkYMbIAVZSYKsjbvNHdQeexIwDzWTEsUdPtxl2MoNtjJXW-JPHpVxbZEcEjSwyxQdW1q2pZzhyI2_ePWrqHrP7_MxeZbiJe-wEF6ElMZM31RxOyA7uPUmv7gZLvxmivK_uu2kzkI5EWG8rseRKdOT4j0BEEhot_faHi-pVWTSOa_0-JMRhccerVuObdzuPatX0zxGO4BgHyyrawTfAA_hLSAG5nKmdV8TVlSEvM_W7FGcLkFUQ7LBPHZUGmtt7euA7luJHBJTS5LAdwYEuoKfV1lj4iOeUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 02:43:23</div>
<hr>

<div class="tg-post" id="msg-1521">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIDA9vF-V_N0m2LwJ3Ukfw3es6DGWdZVxtQhNrc54TE7K9DiYHLtJ6JqatRPTXZ0yH4GvPjlDV9lZIEULsjDVMtpQ2KcqGl0TVoKMy57p5Xxr4w9BnnYDnE5sDHIUqroxkipYrPItDR8nsHAvRPxTZHuCCMZCgFzlPhMpY4WhXb4EaKgVWvySCKDgLr4kOKQ1aYKNoaC9wrUsKmDOzhOdpYVGOtEh6ABHr2UhR_TYyGICVMS5JgNQqDAxFj4jrWnOkTK0UTmaMUpmu4myqrqj7XoSXWaG8skqGeu1kuB8mc2fV4aaTq_FQYIK0jZqa6LJheA_Zib4AWTlZlbQTvBRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏯️
آموزش کامل اپلیکیشن WhiteAesther
📍
تماشا در یوتیوب
https://youtu.be/cRfqxbDY1Dg</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/whitedns/1521" target="_blank">📅 18:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1518">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0  توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.   حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/whitedns/1518" target="_blank">📅 14:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1517">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">آموزش نصب پنل رایگان StanNg روی Railway
بدون VPS و بدون هزینه کانفیگ V2Ray بگیر
🔥
از صفر تا صد کامل توضیح دادم، مناسب تازه‌کارها هم هست.
لینک ویدیو:
https://youtu.be/sdiGXCDsDvQ
سوالی داشتی بپرس
👇</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1517" target="_blank">📅 11:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1515">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌎
نسخه جدید WhiteVPN v1.5.0
👆
تغییر های این ورژن کاملا روی فیدبک های شما بوده، و به نظرم از لحاظ تجربه کاربری تغییر خیلی خوبی داشتیم.
😆
ممنون از فیدبک هایی که به ما میدید.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/whitedns/1515" target="_blank">📅 08:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1510">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1510" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/whitedns/1510" target="_blank">📅 08:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1509">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foE_fbyU6dbFDIeJVRkYzX_HK0E8cF8i4pD-cly8IqP-yj6mZedkiWo81bBdU4KmQ2ZwlW1lOqAoSpzDz1ql1Dt9nh8H0tLHpwfTltnlZ0JUbs8zs9CTPKf3pxtNFiBQIsQfCnlCs-Oy19fJ_nitPxdyhipSWy7LCdW_ywk53Nan5pNNOKFcbtlv_Ea51noFOt44kuMQ1RH2hud7vrzRldcqodrEKE2EfeNpiAy353k8JZEKtDnn7ATIqnC-JNgQUzdpLqdLv1wu006aDfDTxkfRBECGCCRvvrJKd5ouo7JsG1QhLontCa0-YQ2Bjemux7GFcNxyz4_I5FaiwG-6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/whitedns/1509" target="_blank">📅 08:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1508">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/whitedns/1508" target="_blank">📅 08:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1507">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستان عزیز سلام
اپ CoreForge از تیم WhiteDNS ظرفیت جدید اضافه کرده برای کاربران IOS
https://testflight.apple.com/join/3htm1Whc
آموزش استفاده
https://youtu.be/filwdiPKN90?si=O-hvgeNw43t4BUmR
@WhiteDNS</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/whitedns/1507" target="_blank">📅 01:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1506">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">💬
لینک ساب تیم WhiteDNS
https://github.com/iampedii/whitedns-sub</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1506" target="_blank">📅 01:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1504">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سلام دوستان :
❤️
اینقدر درخواست برای IP ثابت برنامه های  whiteAesther و whitevpn اومده که دیدیم بهتر هست ، یک پست براتون بگذارم
در حال حاضر  این امکان توی آخرین ورژن های این دو برنامه وجود ندارد
با اعضای تیم داریم روش کار میکنیم و امیدواریم طی روزهای آینده به دستتون برسونیم ، یکم به ما وقت بدید و صبور باشید.
ببخشید که انجام درخواست های شما گاهی طول می‌کشه، چون ما هم مثل تک تک شما درگیر کار و زندگی و مسائل خودمون هستیم و گاهی وقت کم میاریم
ولی مطمئن باشید ما همه پیام های شما را می‌خونیم و تا جایی که بتونیم ترتیب اثر می‌دیم ،
ارادتمند و کوچیک تک تک شما عزیزان دل
ویسپر</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1504" target="_blank">📅 16:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1502">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⚠️
موقت
به نظر میاد که دامنه
workers.dev
کلادفلر رفع فیلتر شده است</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/whitedns/1502" target="_blank">📅 19:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1501">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cUQcFfD3EHBON4XqlfT9cQDOkH5CvIWTNNIU-6-N8aH7fop1blSCMk6yH7SSXiDdOP_tkvxiAA5w3PpaSo5kEbRsEwE0NFRFlukwwMxT6dKfY29rGB2vaQZOOa4oVFFwEbvLvABx8WOZ3ryoob_8snKR3y6mPxcnrmxhkbYUSYR0Wh7Qw7y-WkWFdIdgxmpWYESiTV5XqPBeVv86f4Xr7Nc6aDJvhNR6BolsmncSaJznH-u94ENBhiuVMPY_1D38_9xkHINa3xPkugkd9PXnnZpvXVEnvYWcBF-d49GqiLweEUNBPkoXJiFhkZd8NTAZt2t-H2sjrmyuQBkvTY0gpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
چرا موقع ورود به Gemini با ارور ۴۰۳ مواجه می‌شویم و چطور حلش کنیم؟
خیلی از کاربران هنگام باز کردن
gemini.google.com
با خطای معروف زیر روبه‌رو می‌شوند:
403. That’s an error. Your client does not have permission to get URL / from this server.
🔍
دلیل این ارور چیست؟
سرویس‌های هوش مصنوعی مثل Gemini دسترسی کاربران برخی مناطق را به دلیل محدودیت‌های منطقه‌ای و حقوقی مسدود (Geo-block) می‌کنند. اما اگر از ابزارهای تغییر آی‌پی استفاده می‌کنید و باز هم این ارور را می‌بینید، علت معمولاً یکی از موارد زیر است:
1️⃣
نشت موقعیت (DNS یا WebRTC Leak):
با اینکه کانکشن شما وصل است، مرورگر از طریق درخواست‌های DNS یا قابلیت WebRTC، آی‌پی واقعی شما را لو می‌دهد.
2️⃣
شناسایی آی‌پی دیتاسنتر (Datacenter IP):
گوگل بازه‌های زیادی از سرورهای عمومی و تجاری را شناسایی کرده و مستقیماً مسدود می‌کند.
3️⃣
کش و کوکی‌های ذخیره‌شده:
مرورگر موقعیت قبلی شما را در کوکی‌ها نگه داشته است.
🛠
راهکارهای سریع برای رفع مشکل:
🔹
تست نشت آی‌پی (Leak Test):
ابتدا وارد سایتی مثل
ipleak.net
یا
browserleaks.com/ip
شوید و مطمئن شوید در بخش‌های WebRTC و DNS هیچ نشانی از آی‌پی واقعی یا DNS داخلی وجود ندارد.
🔹
استفاده از حالت ناشناس (Incognito):
یک پنجره Incognito / Private باز کنید یا کش و کوکی‌های مربوط به دامنه‌های
google.com
را پاک کنید.
🔹
فعال‌سازی حالت TUN Mode / روتینگ کامل:
مطمئن شوید کلاینت شما تمام ترافیک و به خصوص درخواست‌های DNS را هدایت می‌کند و ترافیک دامنه‌های گوگل به صورت Direct رد نمی‌شود.
🔹
تغییر نود یا کشور سرور:
اگر آی‌پی سرور فعلی توسط گوگل فلگ شده باشد، با جابه‌جایی نود یا تغییر لوکیشن معمولاً دسترسی بلافاصله باز می‌شود.
💡
اشتراک‌گذاری برای دوستانی که با دسترسی به جمینای مشکل دارند.
@whitedns</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1501" target="_blank">📅 15:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1496">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FpU1A2-HgYnFurJ7FDGv0ECm710We3IMZiwLxcxv3i2c5SesCnKX41h24LdaMiFRqA9qnF8UcyctGx5n3vfCrn6A0jk6fvkJc_c2RR0CAUX5XdRsdOnjLh6kpzJjqWqTRKIAg1kAVBI4ffHeO3KdxdJUmGozGETcqcr4F_0aNTd2g3WDXPBP25vJmuMlmOU2pXLgSJ5UWZv4QxSKgKEUU6OTgrpwcJWIOV651FuHSANHML8OegqHgHKzq9xxt_CFulLjH-rSbMBZjyp6CMl0cUxxiqimQOogQK3RK57YU3KOzHs6sGTCQbVea6P87PP8T_q8lXAl6XBokMRZLH3E7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/whitedns/1496" target="_blank">📅 07:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1495">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RwPr2GYTgX8rA9I5nJHgi9F5ah9a_NAc0Qt_JMI-mP7qoyO-dl7EFlgHDnT6GDszaCr6bQh2B0mNTPk0ouwabtdh03E0O7foXK9i-o6yMRvBvvPqV-khfF9QgS0Isl0mJxiGyWvoL_6Zzufmb-euoLXdiKDQalTakXBCFMpqT9r-bCa3O7XUQh2-Za2bF5XcLQQe-EyGRNat99XtFY9Y6gIA_MQzcJFJU1TfmkWL-Mit_LwLCNR38oTKYV4gLT7ku8d25rEBrvkf0hWw5_1fiKjHfDkiyhKt2UQNL6Bj6uoIAxrEoFRaYqqeW9SpnzDohLCSGhgrzcGbKP1IdlJ4KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1495" target="_blank">📅 07:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1493">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/X7Xrmk-JGQpIKd9WRQg9BYntK-T00eGkYjiDrojwkLHuyxJhXhqfEedkJd3OPPVR-A9K1nwu-4W7MRcdgyBJwbd60ofauq7fi1BtjPQ3IO2ruVoUTNV10dwskdlweJHBykE38R6ulzr5V4yM59o_FQMLz5d0-DpqAP3JPZYF8ciY8SnNdiOrfRLfyMbe4kAAvEzYZVU7voafHXAAf8vs5J_jHz3yHFk6grAxqWRHcQks9aQFG5bCHCqYJ9sqC3XAWGH8Z4pF0eEW3dnoP2HVchnU6KYjVVNAaT_gfQSnWfNQuaiKurpld97MnwTKxhEBK_S02GBUGMtp9CWX50UcGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام :
برای حل این مشکل توی ورژن دسکتاپ و مبایل whitevpn لطفا ساب زیر را دستی وارد کنید
اگر به هر دلیلی ساب برای شما اپدیت نمیشه اول یک فیلترشکن روشن کنید که ساب را بتونید بگیرید و اپدیت کنید بعد استفاده کنید
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
@whitedns</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1493" target="_blank">📅 05:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1491">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
تمام
#نکات
واسه مشکل فیلتر شدن worker رو داخل این پست میگم:
👽
💻
طبق آموزش هایی که قبلا دادم با اپلیکیشن pattng و همچنین v2rayn در ویندوز میتونید مشکل فیلترشدن ورکر رو حل کنید و کانفیگ های -1 رو مجدد متصل کنید.
آموزش مروبطه:
👇
https://t.me/xsfilterrnet/3642
📱
داخل ios هم طبق تنظیمات یه ip تمیز پیدا کنید داخل کلاینت incy یا hiddify بزنید و فرگمنت رو روشن کنید متصل میشه.
یه روش دیگه بعد از بالا اومدن پنل استفاده از کانفیگ های فرگمنت برای bpb هست که با مقادیر low (1-1) رو متصل کنید
🔥
🔗
در مورد لینک ساب های raw هم به گفته خود bpb:
بچه‌ها اگر ساب Raw و کانفیگ TLS استفاده میکنید از این روش در v2rayNG/pattngاستفاده کنید، معلوم نیست تا کی کار کنه، اگر پایدار بود پنلو تغییر میدم.
این رو دو جا وارد کنید:
https://8.8.8.8/dns-query
۱. قسمت Remote DNS تنظیمات برنامه.
۲. ویرایش کانفیگ قسمت echConfigList.
با Mux خاموش
یه نکته دیگه از بچها اینترنت آزاد که جواب داده:
با ECH و استفاده از آدرس udp://1.1.1.1 میتونید فیلترینگ
pages.dev
و
workers.dev
رو دور بزنید.
💓
نکته ای هم که متین سنپای گفته:(همراه با ابزار جدید)
https://t.me/MatinSenPaii/4960
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1491" target="_blank">📅 22:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1489">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdCFkSAXcdfPtR2c6TfttOy6ms2drcMa6CE-aP7eAbbqTjaLoKBRqe1swxTAVwFURTX20gxX78vvKoyqY9c5bXpX3sIivncJ-HmAojEqrtYrwZLSXZzhm0LIIPVfvv-wii5wNolIPKbNESlk5bXC8ibUkD8B5lf4LvTJYKwWhn-dhd52WFL4JHbeEYN5AUp50vuk5HPuCHe8eBYdpfgFFGkVT07up1wLoBD8JDdT1ynkd4VZR1InypokfU68MrYcIEMq9yHj7LzYk51JQEyi_FLATLjIc30XWHFdYat5199-svlIhSwicCZQ_UX8P32kjl9k_9tLIzQ4WGV5OXd27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟   میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro و باقی Wireguard ها وصل بشید.  این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1489" target="_blank">📅 21:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1488">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjj2YXsVX88qtX5sFN_uEpgV191R92l0FsWFyDhkBbIwLGVGw4pblvJeoS0TsydMo5gvyNpRii-PNKxn-RM1v5Hbd6OdWySbqwcvSZ8dN98NsBDiKC1aNFjBXejSa2YrmVxvrFUc4yEiJ8QzYnT_SYfnv0tKHCmU2S3eGFWPvkXHAs4fC4qBUq7al7RGVGOHLn9mizWnC-LEpbgxEsT9NgT8eIuMsoWBxpOiftDdX3fXe0okuENv12wvtKl3ncfx8CRz7mvlthOSDyeRbdJR-xsbfHjpUt7pe3mxW0CQVZ_zDZUjlTm7H4moKBNUdlp7GHm6C78J64S6cBbTzmGUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro و باقی Wireguard ها وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN
لینک ساب Mihomo رو داخل WhiteVPN وارد کنید.</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/whitedns/1488" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1487">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=V7n-NnoN6BTEZFtciPadzWbe3ijBJUvh0wgo6FaHRUdqDAOPOjRnfyzuSvSQKfF38xpbCT3bsaZYPaW26ly26kJcaJNyn_Miyp2Frt-EpN3iPgeXd3ChyulhDB516fxnUDm6EmjcDoF4iybjA8XY32eGbmYZq5XTK3zSB0ktP--j61zgh5FMCnnSmx5k_6cI0wCgWJkEHX9-OVgLTkLBT97Qozb31s5F7MS0TupxqzMUK0LQO62MiYnMlk8r9_4UP7YO9iLWnm-JtW0Sq6YtmqsgBhNc-63yZ0w9p2yNEUH_APzlvFxL2vmpp7TlUSsNu3SGT6x6oitAQeY2ky0KQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=V7n-NnoN6BTEZFtciPadzWbe3ijBJUvh0wgo6FaHRUdqDAOPOjRnfyzuSvSQKfF38xpbCT3bsaZYPaW26ly26kJcaJNyn_Miyp2Frt-EpN3iPgeXd3ChyulhDB516fxnUDm6EmjcDoF4iybjA8XY32eGbmYZq5XTK3zSB0ktP--j61zgh5FMCnnSmx5k_6cI0wCgWJkEHX9-OVgLTkLBT97Qozb31s5F7MS0TupxqzMUK0LQO62MiYnMlk8r9_4UP7YO9iLWnm-JtW0Sq6YtmqsgBhNc-63yZ0w9p2yNEUH_APzlvFxL2vmpp7TlUSsNu3SGT6x6oitAQeY2ky0KQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/whitedns/1487" target="_blank">📅 19:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1486">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1486" target="_blank">📅 19:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1481">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/whitedns/1481" target="_blank">📅 19:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1480">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9hzzgd4A8OFh66wNfpNla0BzV5CuKPdGiKP0IUlpmWAMjZOVyz3NgNcsy-Ao-MNXVUYxgfkMjFeNDc36EAgokEyd2dHk7zUynH59tY0HbwPTAQDe_MQKtPzhgld7ql276g0kTTAHH8X0Ni8hYq9Py5YsauQgvK9X20HXG77YfteDmM730BINxZi_mQ_hKaFbj68YcsT-35Zka4dfId_y886tGGfFvtmJwgOCmPDXxrnSx4xgZYnnyXv7voJa3Rt8eSgdi7aaHq5oRt81ns4OBtFrUwYGUfxUnKFxu8iMNaJZ6ZC-8pb-BOZ7oazfgK4zawzWInWdZ8Xm1UGrcIBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/whitedns/1480" target="_blank">📅 19:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1478">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XB6W6ryx4XFL1I0BmoVvnbKgtEWgHvyW3OkRKbEvyuawU6eHlSM-a6N627p3e_fAXp4corZAryhA8kAlj4pCFwLNh822q-glmMh4Kq9d0kLGsOqi4SQuYcvJ_170Y9nwH3f1D51PJXPm_BOFbTl0S-aTHdWNSoZDMeSVLfnpzMwOdsCncFkOudgVM4ks6pbq5elc9zDbPHBE6wAj5qW6yMmPVU0Jyx0fE0doKjF5EofnCqyBGnDvW4brrouqzL3KSP2HQkO05tlxeJpTqTHH1Vwb20NB7hopHwZvsM3bnd_YypL8ENFhyeS1dKI1AXirbpS6IDLmvJkpmtXmuqgOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
وایت‌استر  —
نسخه‌ی دسکتاپ بتا
WhiteAesther Desktop V1.3.1
یه کلاینت رایگان و متن‌باز برای عبور از فیلترینگ، ساخته‌شده روی هسته‌ی Aether (همون هسته‌ای که تو اپ اندرویدش هم استفاده می‌شه). برای ویندوز، مک و لینوکس؛ کاملاً رایگان و بدون نیاز به کانفیگ دستی.
✨
امکانات:
🔎
جست‌وجوی خودکار مسیر — به‌جای اینکه شما دنبال کانفیگ سالم بگردید، خود برنامه بهترین دروازه رو پیدا می‌کنه (با MASQUE H2/H3، WireGuard و WARP-in-WARP)
📊
نمودار سرعت و تأخیر زنده — تست سرعت واقعی داخل خود برنامه + نمودار پینگ لحظه‌ای
🖥
دو حالت اتصال — «فقط این برنامه» (پراکسی محلی) یا «کل سیستم» (همه‌ی اپ‌ها از تونل رد بشن)
🛡
کلید قطع اضطراری — اگه تونل قطع بشه، ترافیک رمزنشده لو نمی‌ره
🔍
جست‌وجوی تنظیمات با Ctrl+K — هر تنظیمی رو در چند ثانیه پیدا کنید
🧩
چندپلتفرمه — ویندوز، مک (اینتل و اپل‌سیلیکون) و لینوکس، هم x86_64 هم arm64
📖
متن‌باز، برای همیشه — کد کامل زیر مجوز AGPL-3.0 روی گیت‌هاب
⚙️
نحوه‌ی استفاده:
1️⃣
از لینک زیر، نسخه‌ی مخصوص سیستم‌عاملتون رو دانلود کنید
2️⃣
نصب کنید و برنامه رو باز کنید
3️⃣
دکمه‌ی Connect رو بزنید و چند لحظه صبر کنید تا مسیر سالم پیدا بشه
4️⃣
اگه خواستید کل سیستم از تونل رد بشه، پایین صفحه گزینه‌ی «Whole machine» رو بزنید
5️⃣
برای تنظیمات پیشرفته (پروتکل، DNS، حالت جست‌وجو…) روی Advanced بزنید یا Ctrl+K رو بزنید و اسم تنظیم موردنظرتون رو تایپ کنید
📥
دانلود:
github.com/WhiteDNS/WhiteAesther/releases/latest
💬
نکته: چون برنامه امضای اپل/مایکروسافت نداره، ممکنه هنگام باز کردن هشدار «ناشر ناشناس» ببینید؛ کافیه روی فایل راست‌کلیک کنید و Open رو بزنید (تو مک هم از System Settings اجازه‌ی اجرا بدید).
#وایتاستر
#ضدفیلتر
#متنباز
نکته مهم :
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
گزینه whole machine همان system proxy هست - این گزینه فقط اپلیکیشن هایی مثل گوگل کروم که امکان ان را دارند پراکسی میکند - برای همین ممکن هست بعضی از اپ های شما پراکسی نشود
تلاش خواهیم کرد در روزهای اینده امکان TUN را اضافه کنیم
@whitedns</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1478" target="_blank">📅 18:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1477">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوستان عزیز سلام
مثل اینکه آدرس های ورکر کلادفلر فیلتر شدن. و آدرس ساب اپلیکیشن ما داخل ورکر ها هستش. تا آپدیت بعدی، میتونید ساب مارو از لینک زیر وارد اپ WhiteVPN بکنید
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1477" target="_blank">📅 16:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1476">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/MRk1w5rgfDaqHGkdM7q1rutCw-7BIuUOODvVfcz59x58q6hc4JRsvWPErFUfE1IywshKttZTQsGMomjrhOQ-v8WJEZCh7kw8dJy5UzsDY7z2C-DLMm5o6KCT8JrefDs1FofA2RZjGQCQ_GoH0-R5BtcGwCNY9-eIayR_nEphgbJLcBwrvn7riELt7L3ybevEdWC7eacyAInJnr46xFGUYZF0M3S74juNaKeNPzHycYDSCp9SuoGqhu3zMGIJkiwMfbHAMFS60pob0UZJCgMwpfdnhbr1bYF9H_7XdD_LFausoPYuDIOWdKu-yxIpRgmiXDby8WI8pe_n6F1UZ0ml0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther V1.0.2
دوستان سلام :
ما روی هسته Aether که حاصل زحمت دوست عزیزمون
CluvexStudio
هست یک کلاینت**
آزمایشی ورژن بتا
** درست کردیم . که اگر دوست دارید تست کنید و لطف کنید فیدبک بدید.
پیشاپیش ممنونیم
❤️
❤️
❤️
اموزش :
📖
**راهنمای WhiteAesther**
**۱ — نصب**
فایل **arm64-v8a** رو بگیر (تقریباً همه گوشی‌های ۲۰۱۷ به بعد).
مطمئن نیستی؟ **universal** همه‌جا کار می‌کنه، فقط حجمش بیشتره.
**۲ — سه تا نکته اول**
▪️
**Traffic** → گزینه Coverage روی **Whole device** باشه
⚠️
حالت Proxy only خودش هیچی رو رد نمی‌کنه! به‌نظر می‌رسه وصل شده ولی عملاً هیچ ترافیکی از تونل نمی‌ره.
▪️
**Routes** → پروفایل روی **Adaptive**
▪️
**Settings** → اجازه اجرا در پس‌زمینه رو بده، وگرنه با خاموش شدن صفحه قطع می‌شه
**۳ — اگه وصل نشد، به این ترتیب امتحان کن**
**قدم ۱ — پروتکل**
Routes → Advanced → Preferred transport → **MASQUE over HTTP/2**
📌
روی **همراه اول** مدتیه QUIC (یعنی UDP) کاملاً بسته شده. یعنی H3 اصلاً وصل نمی‌شه و فقط H2 جواب می‌ده.
از نسخه ۱.۰.۲ اپ خودش این کار رو می‌کنه.
**قدم ۲ — تیکه‌تیکه کردن TLS**
⭐️
Traffic → Advanced → **Split the TLS handshake** → روشن
فیلترینگ معمولاً فقط تیکه اول بسته رو می‌خونه تا ببینه کجا وصل می‌شی. وقتی تیکه‌تیکه بفرستی، نمی‌تونه بخونه.
اگه با H2 وصل می‌شی ولی کنده، **حتماً اینو امتحان کن**.
**قدم ۳ — پروفایل**
Routes → Profile → **Strict network**
(برای شبکه‌هایی که خیلی چیزها رو می‌بندن)
**قدم ۴ — خاموش کردن IPv6**
Traffic → Addresses → **IPv4 only**
روی خیلی از شبکه‌های موبایل ایران IPv6 نیمه‌کاره‌ست.
**قدم ۵ — مبهم‌سازی**
Traffic → Advanced → Obfuscation → **Aggressive**
💡
اگه قدم ۲ مشکلت رو حل کرد، **Off** رو هم تست کن — شاید پدینگ اضافه فقط داشته سرعتت رو می‌گرفته.
**قدم ۶ — اند‌پوینت دستی**
Routes → Endpoint → Specific address → دکمه **Find endpoints**
⚠️
گزینه Fall back automatically رو روشن نگه دار.
**۴ — گزارش مشکل**
Settings → Diagnostics & logs
۱. Detail level روی **Verbose**
۲. دوباره سعی کن وصل بشی
۳. برگرد و **Send** رو بزن
قبل از ارسال دقیقاً متنی که فرستاده می‌شه رو می‌بینی، و IP‌ها پیش‌فرض مخفی می‌شن. هیچی بدون اجازه‌ات از گوشیت بیرون نمی‌ره.
**نکته:** اون خط خاکستری کوچیک زیر متن بزرگ توی صفحه اصلی، پیغام خود موتوره. برای فهمیدن مشکل همیشه اول اونو بخون.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.0.3
@whitedns</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/whitedns/1476" target="_blank">📅 13:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1474">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FjlCFEa-rSc8ck469971fhYWn946Mop5C-YZpO8T6c1HQv7eLQHK-Obj55HhFwh_Xu6rwaMHHW25g2pej0VmdHLxEO4uw781DNnPCRzovTdGZABxccHTVJpPphrc-MuGczTJfr85T06s7sD1tvfTFEeziFHY7WnCU7olhdNBZo2x2tF8VZo5iZwZ_2SrKM6kzExUkSuHQsNUEYuEK_bVGq7VnaKfENVpKzgqkQZZPx80o7twhX7B1XgP4MnvURXYUle-Jc26XJ-Uv5RjD0L_pp5O3ANIy1m4_pjMeE2U8-1SSDZaNhhAe9NifLbhwTp6xul1aBUmh2zXkpkKlrIt7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS Clean IP Finder 1.3.7
نسخه جدید WhiteDNS Clean IP Finder با تمرکز روی افزایش سرعت پیدا کردن DNS Resolverهای سالم در Desktop و Android منتشر شد.
⚡️
مهم‌ترین تغییرات:
• اجرای همزمان تست‌های DNS Transport و TXT Passthrough برای کاهش Timeout
• اجرای Parallel بررسی‌های NXDOMAIN Hijack
• اضافه شدن Fast Scan با حفظ بررسی‌های اصلی A Record، Recursion، EDNS و TXT Tunnel
• حفظ Full Scan به‌عنوان حالت پیش‌فرض برای بررسی کامل
• بهبود دریافت و Cache اطلاعات Reference DNS
• اضافه شدن UDP/53 Only و TCP/53 Only در Android
• گزارش دقیق‌تر DNS Poisoning، Injection و Hijack
• بروزرسانی دیتابیس Iran & Global ASN شامل IPv4 و IPv6
💻
پشتیبانی از Windows، Linux، macOS و Termux
📱
نسخه Android شامل APKهای مختلف، Universal APK
✅
برای آپدیت نیازی به تغییر تنظیمات قبلی نیست.
📥
دانلود WhiteDNS Clean IP Finder 1.3.7:
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3.7
⚡️
WhiteDNS Clean IP Finder — اسکن سریع‌تر، تشخیص دقیق‌تر و دیتابیس به‌روزتر
@whitedns</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1474" target="_blank">📅 02:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1473">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il-sA8_LPBVi8O2z4gyH_WIqPvRwP09T0Ri8H5j0gVSVzQuQAu9ApOAdunGBYhQbKa6uquetOCiaSPIzvbdLyxmm61YhZVAB1-UJMIR2iMSrLLYBMfr5cumDpy4dlnIZl1nQT_g8sw_934oaaADClEH-orCUC21f9ErxVNuy5BdrTC_ZL8AvgfoMZg5-nyQgxPJ7g-nF0UIaVyuDhJv48LpKwXOILhn_87G09wvlURknGGsp11Ju4R9W4Xfx3kknWgPk81uB1jTgSBwJ-B_J6Yts9bgMAn6vMtu6n1VMDi_izxEBZgXldLn5wQHdlkugQSTbSrEvn87s72UH_WUj4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏯️
آموزش ساخت کانفیگ V2Ray با سرور رایگان!   توی این آموزش با استفاده از Wasmer یه سرور رایگان می‌سازیم و در نهایت بدون نیاز به خرید سرور، ۳ تا کانفیگ V2Ray برای مصرف شخصی دریافت می‌کنیم.
⚡️
⏯️
تماشا در یوتیوب  https://youtu.be/EAjOhvuMw8Q</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1473" target="_blank">📅 21:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1472">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⏯️
آموزش ساخت کانفیگ V2Ray با سرور رایگان!
توی این آموزش با استفاده از Wasmer یه سرور رایگان می‌سازیم و در نهایت بدون نیاز به خرید سرور، ۳ تا کانفیگ V2Ray برای مصرف شخصی دریافت می‌کنیم.
⚡️
⏯️
تماشا در یوتیوب
https://youtu.be/EAjOhvuMw8Q</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1472" target="_blank">📅 21:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1471">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bbTwAxTRpTHIM8Zu5ry7QR66kBFlMiTElBU9y3HYmfXDEmgPDQG7ZOTvL7NUH2m7WzHvSAsnGEnX6lcfyduTMvHmhxOxfW1Bxtnjb8Q8Zj71emmBM9spHZBeMvb9wQCwfO0OA3KtELbAbWZZS2zLag-kYIgPkQXlhImH9qwl8g3SPlkZLGz1pnOLGmqTFXp_KT-or9sf9RIxPMVBgq6b0fd4DOZesRA4vy6W_54YBS3_NVXwnjOUOWUDPN5AHFLNXRJ4MdnUN5oZxoP_5T404E-jPswV7Kd4_lvGqng0sBgIC53ARNOyGIz0cTftCjRZPTic0M84LMxO8UJ6Nz0zeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS دسکتاپ
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/whitedns/1471" target="_blank">📅 18:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1470">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromUAC Sni Spoofer(Behrooz)</strong></div>
<div class="tg-text">🛡
نسخه‌ی 2.0.1 اپلیکیشن UAC SNI Spoofer برای اندروید منتشر شد
در نسخه‌ی 2.0.1 تمرکز اصلی روی این بوده که برنامه در شبکه‌ها، اپراتورها و مناطق مختلف، مسیرهای سالم‌تر و سریع‌تر رو پیدا کنه و در صورت افت کیفیت یا از دست رفتن مسیر فعلی، بتونه مسیر مناسب‌تری رو جایگزین کنه.
⚡️
یکی از مهم‌ترین قابلیت‌های این نسخه، تلاش برای زنده‌کردن کانفیگ‌هایی هست که در حالت عادی دیگه قابل استفاده نیستن.
🔹
اگر کانفیگی دارید که IP سرورش روی اپراتور یا شبکه شما بلاک شده
🔹
مطمئن هستید کانفیگ سالمه ولی در برنامه‌هایی مثل v2rayNG متصل نمی‌شه
🔹
کانفیگ فقط روی یک اپراتور خاص کار می‌کنه و روی اپراتورهای دیگه از دسترس خارج شده
🔹
کانفیگ قبلاً کار می‌کرده ولی به‌دلیل تغییر محدودیت‌های شبکه دیگه متصل نمی‌شه
UAC SNI Spoofer می‌تونه با بررسی ترکیب‌های مختلف مسیر، DNS، Edge، Fragment، MTU و سایر پارامترهای اتصال، برای پیدا کردن یک مسیر قابل استفاده تلاش کنه.
در تست‌های انجام‌شده، برنامه تونسته بخش بسیار زیادی از کانفیگ‌های سالم ولی محدودشده رو دوباره قابل استفاده کنه و در بعضی شرایط میزان موفقیت تا حدود 98٪ هم رسیده.
البته نتیجه نهایی به نوع فیلترینگ، اپراتور، منطقه، وضعیت سرور و کیفیت اینترنت شما بستگی داره.
تغییرات نسخه 2.0.1:
🔹
برنامه برای هر شبکه یک اثرانگشت جداگانه ایجاد می‌کنه و تنظیمات موفق همون شبکه رو ذخیره می‌کنه تا دفعات بعد سریع‌تر به مسیر مناسب برسه.
🔹
بخش Route Speed Test حالا می‌تونه ترکیب‌های مختلف Edge، DNS، Fragment و MTU رو بررسی کنه و بهترین مسیر فقط براساس Ping انتخاب نمی‌شه.
🔹
مسیرها در چند مرحله از نظر اتصال، سرعت، پایداری، نوسان و میزان موفقیت بررسی می‌شن و بهترین نتایج بالای لیست قرار می‌گیرن.
🔹
امکان توقف Route Speed Test و ادامه‌دادن اون در زمان دیگه اضافه شده.
🔹
می‌تونید هر زمان که خواستید مسیرهای سالم پیدا شده رو به مرحله بعد بفرستید و لازم نیست منتظر پایان کامل تست بمونید.
🔹
برای هر کانفیگ و هر شبکه، یک مسیر اصلی و یک مسیر پشتیبان ذخیره می‌شه تا اتصال سریع‌تر انجام بشه.
🔹
اگر شبکه تغییر کنه یا کیفیت مسیر فعلی افت کنه، برنامه می‌تونه سراغ مسیر پشتیبان بره و برای بازیابی اتصال تلاش کنه.
🔹
سرویس‌های مختلف DNS مثل Cloudflare، Google، Quad9، AdGuard و OpenDNS در دسترس هستند و همراه مسیرهای مختلف قابل تست هستن.
🔹
بخش Config Maker دارای دو حالت Quick Scan و Deep Adaptive Test شده؛ یکی برای بررسی سریع و دیگری برای تست دقیق‌تر و گسترده‌تر مسیرها.
🔹
امکان وارد کردن کانفیگ از متن، Clipboard، فایل و Subscription Link وجود داره.
🔹
لینک‌های جدید بدون حذف نتایج قبلی به لیست اضافه می‌شن و کانفیگ‌های تکراری به‌صورت خودکار حذف می‌شن.
🔹
کانفیگ‌های VLESS، VMess و Trojan پشتیبانی می‌شن و مشخصات اصلی کانفیگ تا جای ممکن بدون تغییر باقی می‌مونه.
🔹
برای برنامه‌های گوشی سه حالت Routing در دسترسه: عبور همه برنامه‌ها از VPN، خارج‌کردن برنامه‌های انتخابی از VPN یا استفاده از VPN فقط برای برنامه‌های انتخابی.
🔹
حالت Tunnel و پروکسی محلی SOCKS در دسترس هست و تنظیماتی مثل Fragment، FinalMask، MTU، Mux، Keepalive و کنترل QUIC هم قابل تغییر هستن.
🔹
Ping، میزان دانلود و آپلود، کشور، IP خروجی و اطلاعات فنی اتصال به‌صورت زنده نمایش داده می‌شن.
🔹
بعد از اضافه‌کردن برنامه به Quick Settings اندروید، می‌تونید بدون بازکردن برنامه VPN رو مستقیماً روشن یا خاموش کنید.
⚠️
نکته مهم:
محدودیت‌های فیلترینگ در هر منطقه، اپراتور و حتی در زمان‌های مختلف می‌تونه متفاوت باشه. به همین دلیل ممکنه کانفیگ داخلی برنامه برای بعضی کاربران متصل نشه یا روی بعضی شبکه‌ها کیفیت متفاوتی داشته باشه.
در حال بررسی مسیرها و محدودیت‌های شبکه‌های مختلف هستم تا روش‌های بیشتری شناسایی بشن و برنامه بتونه در مناطق و اپراتورهای بیشتری محدودیت‌ها رو دور بزنه.
همچنین حتماً مطمئن بشید اینترنت اصلی شما سرعت دانلود و آپلود قابل قبولی داره. VPN نمی‌تونه ضعف شدید یا ناپایداری اینترنت پایه رو جبران کنه و کیفیت اتصال نهایی به کیفیت شبکه شما هم وابسته است.
━━━━━━━━━━━━━━━━━━
📥
دریافت نسخه 2.0.1:
https://github.com/Floxu1/UAC-SNI-Spoofer-Android/releases/tag/2.0.1
💻
گیت‌هاب پروژه:
https://github.com/Floxu1/UAC-SNI-Spoofer-Android/tree/main
جهت حمایت از من اگر دوست داشتین وارد لینک رفرال من در NotHolidaySeasonBot بشین
❤️
:
https://t.me/NotHolidaySeasonBot/app?startapp=tr_aFLKAgxVq8ezM310c0sS
📢
کانال:
t.me/UacSniSpoofer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/1470" target="_blank">📅 15:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1468">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bxoQiuaMK0cykqIb_Nxp3gHA1j-rYFSuE_DcmQXkP-3GktVvkI8mW17J_pvghSjWKhXpy1WRbEYzqCksfo4S1YK68RNKBtPOytJBkHgpdmdJfMPO09ADsEgle7T_6tlellV6yMuXo2FGatDB4NyJEMTPmy27vmeB7RE9GSeZh_HrjVfUYzoStd_ni7Nm9vhzC_EQRQMhf4CObgK2WziHwcC-C9tA7lImClZnTR263p1a0jJWfsTGG8OQ0fnFgIte3hsjkZ9sKPHWFB0janWF8FLm-JXuxQnc93_US1OUC8ww1jrNbcYwDh-S25qd-hsg5N0hGafw-q4Ff6y6MOwxGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1468" target="_blank">📅 11:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1467">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qpxgHawyKcBDK2mIqiGGXXCsN7oD41wjgRF1g15QqFrJf4yPtbuCzOH5MhZP69OdnT7JjuoG0xrJpVKK29JalERzdv1mm9L0No_7Qet5QRctqbbvPZy3sHnbGJQu5KwmjPoB3t1yYAaTv5E8pxla_9tzjw7TI_lCJLtdiraJv7IY6FjLqe7g-o5wEX7eJpQTaovWkFAtDTNG2Hyg4TOvUvUi4Cz9e7AF61lr6cRg3rfQGXReTG3UBtABzro_DWTKjzYwt4GeClQ3JBxLyJkfzlvwRTC96pWCVKgnBU9AgrKxOo_tOvEliVIvg85jMyGgUYPcYTs7ahW_spPtcAAl5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Coming soon............
WhithAester desktop
😍</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/whitedns/1467" target="_blank">📅 09:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1466">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🌎
پروژه WhiteVPN رو اوپن‌سورس کردیم و در گیتهاب میتونید بهش دسترسی داشته باشید.   https://github.com/WhiteDNS/WhiteVPN  همراه با پابلیک شدن پروژه، نسخه ۱.۳.۱ هم ریلیز کردیم
⛏
در این نسخه امکان • آپدیت اتوماتیک اپ  بعد از یک ورژن جدید • امکان routing برای…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/whitedns/1466" target="_blank">📅 09:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1464">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🌎
انتشار نسخه ۱.۳.۱ اپلیکیشن WhiteVPN
پست قبلی پاک شد. یک آپدیت کوچیک داشتیم به ورژن ۱.۳.۱
😆
از این به بعد آپدیت هارو اتوماتیک از داخل اپ میتونید بگرید</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/whitedns/1464" target="_blank">📅 08:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1459">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.3.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1459" target="_blank">📅 08:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1458">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjH5WW9y6dWSQdId4BNE_C1cEAFsQmK_8VaacOjjxM-VO5H7q6JMMcCIJPnDH2nbGZkXzwGF-RBBkZBBdMFrmNp1Y3jRjpwOVFKm8UuUcWJwCT28x8ktYMS2LidSy3qKn-v_Yl7iCcl0B1vqCsUfkI7_eeQtuNbzxNdg-P9MxDGh1Qs5W8liOI7t9znijK9wjKyVDBjxQ9yXU8SOlw1AOM23-Wb0fXKdz27T3Vk9ESNF4a-yejThcrYvprpdYl-ljrCOs_5i1O3NxuB8XSusdE4nlQ8zTCmnyeLaX1tltL85SznICpcra8mg0SkdCrZjT9I1KRSkfQkVYR2_WjIfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
پروژه WhiteVPN رو اوپن‌سورس کردیم و در گیتهاب میتونید بهش دسترسی داشته باشید.
https://github.com/WhiteDNS/WhiteVPN
همراه با پابلیک شدن پروژه، نسخه ۱.
۳
.
۱
هم ریلیز کردیم
⛏
در این نسخه امکان
• آپدیت اتوماتیک اپ  بعد از یک ورژن جدید
• امکان routing برای سایت ها و آی‌پی های ایرانی به تنظیمات اضافه شده تا دیگه نیاز نباشه اتصال رو برای سایت های داخلی قطع کنید.
• اشتراک گذاری WhiteVPN در شبکه اضافه شده.
• حالا میتونید اپ پروکسی اپ در داخل اپ های دیگه مثل سایفون استفاده کنید.
• تست سرعت به سابسکریپشن اضافه شده
دانلود نسخه جدید از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.3.1</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1458" target="_blank">📅 08:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1449">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tXiq3gf5rGs4qrEPlPc_4dO8AtBgsSmgIDWZjrKQ4Wrgto0R6GmnKpC_RHro7wN7YW_miq77M_fRd9n2gkmGz_t7CXpM0J0ik2Dr1AXciwd0kWgXbM893X4u9ya9yKSymGE682HazbprFrCFD_X8YFMJ_q9UENEYZm-LDPaujjnQsdPqfmLI_6m6zvwc6ef32oT_LEi1RSzkmEUmJbWpI4C6rB7yWA1YKlthzzGH4XJq_l8R_EQ9K19xaPMPFscI9IUV6RJqhh2xAEoaYtDW6l1ZGRup7wOOtliUbG3sdlIf6oENvUdKSCv5G_YEaw1DHMiPvc8-NkNqxiRBYvqyng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther V1.0.2
دوستان سلام :
ما روی هسته Aether که حاصل زحمت دوست عزیزمون
CluvexStudio
هست یک کلاینت**
آزمایشی ورژن بتا
** درست کردیم . که اگر دوست دارید تست کنید و لطف کنید فیدبک بدید.
پیشاپیش ممنونیم
❤️
❤️
❤️
اموزش :
📖
**راهنمای WhiteAesther**
**۱ — نصب**
فایل **arm64-v8a** رو بگیر (تقریباً همه گوشی‌های ۲۰۱۷ به بعد).
مطمئن نیستی؟ **universal** همه‌جا کار می‌کنه، فقط حجمش بیشتره.
**۲ — سه تا نکته اول**
▪️
**Traffic** → گزینه Coverage روی **Whole device** باشه
⚠️
حالت Proxy only خودش هیچی رو رد نمی‌کنه! به‌نظر می‌رسه وصل شده ولی عملاً هیچ ترافیکی از تونل نمی‌ره.
▪️
**Routes** → پروفایل روی **Adaptive**
▪️
**Settings** → اجازه اجرا در پس‌زمینه رو بده، وگرنه با خاموش شدن صفحه قطع می‌شه
**۳ — اگه وصل نشد، به این ترتیب امتحان کن**
**قدم ۱ — پروتکل**
Routes → Advanced → Preferred transport → **MASQUE over HTTP/2**
📌
روی **همراه اول** مدتیه QUIC (یعنی UDP) کاملاً بسته شده. یعنی H3 اصلاً وصل نمی‌شه و فقط H2 جواب می‌ده.
از نسخه ۱.۰.۲ اپ خودش این کار رو می‌کنه.
**قدم ۲ — تیکه‌تیکه کردن TLS**
⭐️
Traffic → Advanced → **Split the TLS handshake** → روشن
فیلترینگ معمولاً فقط تیکه اول بسته رو می‌خونه تا ببینه کجا وصل می‌شی. وقتی تیکه‌تیکه بفرستی، نمی‌تونه بخونه.
اگه با H2 وصل می‌شی ولی کنده، **حتماً اینو امتحان کن**.
**قدم ۳ — پروفایل**
Routes → Profile → **Strict network**
(برای شبکه‌هایی که خیلی چیزها رو می‌بندن)
**قدم ۴ — خاموش کردن IPv6**
Traffic → Addresses → **IPv4 only**
روی خیلی از شبکه‌های موبایل ایران IPv6 نیمه‌کاره‌ست.
**قدم ۵ — مبهم‌سازی**
Traffic → Advanced → Obfuscation → **Aggressive**
💡
اگه قدم ۲ مشکلت رو حل کرد، **Off** رو هم تست کن — شاید پدینگ اضافه فقط داشته سرعتت رو می‌گرفته.
**قدم ۶ — اند‌پوینت دستی**
Routes → Endpoint → Specific address → دکمه **Find endpoints**
⚠️
گزینه Fall back automatically رو روشن نگه دار.
**۴ — گزارش مشکل**
Settings → Diagnostics & logs
۱. Detail level روی **Verbose**
۲. دوباره سعی کن وصل بشی
۳. برگرد و **Send** رو بزن
قبل از ارسال دقیقاً متنی که فرستاده می‌شه رو می‌بینی، و IP‌ها پیش‌فرض مخفی می‌شن. هیچی بدون اجازه‌ات از گوشیت بیرون نمی‌ره.
**نکته:** اون خط خاکستری کوچیک زیر متن بزرگ توی صفحه اصلی، پیغام خود موتوره. برای فهمیدن مشکل همیشه اول اونو بخون.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.0.3
@whitedns</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/whitedns/1449" target="_blank">📅 11:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1448">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز،
در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.
🔗
https://www.youtube.com/@WhiteDNS
ممنون از همراهی همیشگی شما
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/whitedns/1448" target="_blank">📅 11:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1447">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjMm2QywLi8KwO7DhB0H9OEzsOzwQZ6VbWwapvn5VXl7p9ghojSS4FTz6twPG9Jius9gAAIhcosje4DclVFdr0RjoUw0X1UFJUTQUQev5afQBBrPaBG1WW2XUAmYQC38SgiwLIb3CxjGk6Ivs9D6hEFnuE6m17yisJV86pzQb2dk7oYq6xpS9xR6XkYb16LX6jNRMJkOd28E23wzqNWhzexLbuBk7B9I-54W25KH4JGRMk5hBzuRmBlqbY5vAlJAs9m22q5qGLkVIcnMHjYimKC8DjD5vMRaBkav2Rr3jdS5Atbb2Mg9B-Hi_vGYO_hVBgzEAhqvOn3v1ZDxva4ZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1447" target="_blank">📅 09:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1446">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌎
سلام خدمت همه دوستان عزیز
در آخرین آپدیت سرویس ساسبکریپشن WhiteVPN ما مشکل کشور هارو حل کردیم.
حالا اگر از اپ اندروید یا دسکتاپ کشوری رو انتخاب کنید، کانکشن به کشور درست وصل خواهد شد.
⛏
دانلود آخرین ورژن WhiteVPN اندروید
⛏
دانلود آخرین ورژن WhiteVPN دستکتاپ
اگر اپ رو دارید، اول ساب خودتون رو رفرش کنید.
اگر مشکلی دیدید، حتما با ما به اشتراک بگذارید.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/whitedns/1446" target="_blank">📅 09:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1444">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">موقت
⚠️
هشدار مهم برای همه اعضا
⚠️
⚠️
⚠️
⚠️
دوستان عزیز،
بارها گفتیم:
به هیچ‌کس—چه ناشناس، چه آشنا—برای فیلترشکن، VPN، کانفیگ و… پول ندهید.
دلیل اینکه ما اینجا شبانه‌روز وقت می‌گذاریم همین است که شما
بی‌نیاز از پرداخت پول
باشید و گرفتار افراد سودجو نشوید.
اگر بدون پرسیدن از ادمین‌ها رفتید پول دادید و طرف کلاهبردار از آب درآمد، بعدش پیام می‌دید که «چی کار کنم؟» واقعاً ما در این مرحله کاری از دست‌مان برنمی‌آید.
چرا قبلش نپرسیدید؟
ادمین‌ها ۲۴/۷ پاسخگو هستند.
ما نمی‌توانیم در تک‌تک چت‌های خصوصی شما مراقب‌تان باشیم. لطفاً قبل از هر پرداختی، یک پیام ساده بدهید و سؤال کنید.
کلاهبردار پیام داده 1000 گیگ فیلترشکن BPB - به مرغ پخته بگی خندش میگیره
پول را واریز کرده - اونم در کسری از ثانیه بلاکش کرده -
حتما با تگ کردن ادمین ها افرادی که تبلیغ فروش VPN میکنندیا در خصوصی به شما پیشنهاد میدهند را گزارش دهید
این مکان با کمک و همراهی همه فقط میتونه امن و سالم باقی بمونه
ارادت</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1444" target="_blank">📅 07:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1443">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">Whitevpn dekstop v1.0.16
🍎
🐧
راهنمای استفاده روی مک و لینوکس
حالت TUN فعلاً فقط روی ویندوز کار می‌کند. روی مک و لینوکس دو حالت دیگر هست که برای اکثر کارها کافی‌اند.
━━━━━━━━━━━━━━━
🖥
روی مک — ساده‌ترین حالت
تنظیمات ← اتصال ← «پراکسی سیستم» را انتخاب کنید و وصل شوید. تمام.
مک تنظیم پراکسی را در سطح سیستم اعمال می‌کند، پس تقریباً همهٔ برنامه‌ها (سافاری، کروم، فایرفاکس و بیشتر اپ‌ها) خودکار از تونل رد می‌شوند.
━━━━━━━━━━━━━━━
🐧
روی لینوکس — یک نکتهٔ مهم
«پراکسی سیستم» روی لینوکس تنظیمات گنوم و KDE را عوض می‌کند. ولی این یک ترجیح است، نه اجبار: برنامه‌هایی که این تنظیم را می‌خوانند رد می‌شوند، و برنامه‌هایی که نمی‌خوانند نه.
معمولاً کار می‌کند: کروم، کرومیوم، فایرفاکس
معمولاً کار نمی‌کند: تلگرام دسکتاپ، ابزارهای ترمینال
برای آن‌هایی که کار نمی‌کنند، سراغ بخش بعدی بروید.
━━━━━━━━━━━━━━━
🎯
وصل کردن یک برنامهٔ خاص (روی هر دو سیستم)
اگر می‌خواهید فقط یک برنامه از تونل رد شود — یا برنامه‌ای پراکسی سیستم را نادیده می‌گیرد — این راه مطمئن‌ترین است.
آدرس پراکسی، بعد از وصل شدن، در صفحهٔ اصلی نشان داده می‌شود. روی آن کلیک کنید تا کپی شود. معمولاً:
127.0.0.1:2080
این آدرس هم SOCKS5 و هم HTTP را می‌پذیرد.
📱
تلگرام دسکتاپ
Settings ← Advanced ← Connection type ← Use custom proxy
نوع: SOCKS5 — آدرس:
127.0.0.1
— پورت: 2080
🦊
فایرفاکس
Settings ← Network Settings ← Manual proxy configuration
SOCKS Host:
127.0.0.1
— Port: 2080 — گزینهٔ SOCKS v5
⌨️
ترمینال (curl، git، npm و…)
این‌ها هیچ‌وقت از تنظیمات گرافیکی پیروی نمی‌کنند و باید دستی بهشان گفت:
export http_proxy=
http://127.0.0.1:2080
export https_proxy=
http://127.0.0.1:2080
(فقط برای همان پنجرهٔ ترمینال اعمال می‌شود)
━━━━━━━━━━━━━━━
💡
اگر نمی‌خواهید کل سیستم پراکسی شود
تنظیمات ← اتصال ← «فقط پراکسی» را انتخاب کنید. در این حالت هیچ چیزی روی سیستم شما تغییر نمی‌کند و فقط همان برنامه‌هایی که خودتان تنظیم کرده‌اید از تونل رد می‌شوند.
━━━━━━━━━━━━━━━
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.16</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1443" target="_blank">📅 16:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1440">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">Whitevpn desktop V1.0.15 ( linux 24+)
🐧
راهنمای نصب روی اوبونتو ۲۴ و بالاتر
بعضی از دوستان روی اوبونتو ۲۴ به بالا موقع نصب با خطای dependency روبه‌رو شده‌اند. مشکل از برنامه نیست — فقط باید فایل درست را دانلود کنید.
━━━━━━━━━━━━━━━
📌
اول ببینید نسخه‌تان چند است
در ترمینال بزنید:
lsb_release -a
یا از مسیر Settings ← About نگاه کنید.
━━━━━━━━━━━━━━━
✅
اوبونتو ۲۴.۰۴ و بالاتر (شامل ۲۵ و ۲۶)
فایلی را دانلود کنید که در اسمش webkit41 دارد:
WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.deb
و نصبش کنید:
sudo apt install ./WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.deb
⚠️
حتماً ./ را قبل از اسم فایل بگذارید، وگرنه apt دنبال آن در اینترنت می‌گردد.
━━━━━━━━━━━━━━━
✅
اوبونتو ۲۲.۰۴ و دبیان ۱۲
فایل بدون webkit41:
WhiteVPN-Desktop-1.0.15-linux-amd64.deb
sudo apt install ./WhiteVPN-Desktop-1.0.15-linux-amd64.deb
━━━━━━━━━━━━━━━
🎯
ساده‌ترین راه: AppImage
اگر نمی‌خواهید درگیر نصب و وابستگی شوید، فایل AppImage را بگیرید. اصلاً نصب نمی‌خواهد و به هیچ کتابخانه‌ای روی سیستم شما وابسته نیست:
WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.AppImage
بعد از دانلود، اجازهٔ اجرا بدهید و اجرا کنید:
chmod +x WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.AppImage
./WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.AppImage
(این فایل برای اوبونتو ۲۴ به بالا است)
━━━━━━━━━━━━━━━
💡
چرا دو تا فایل هست؟
اوبونتو در نسخهٔ ۲۴ کتابخانه‌ای که برنامه‌های گرافیکی از آن استفاده می‌کنند را عوض کرد. یک فایل واحد نمی‌تواند هر دو را پوشش دهد، برای همین دو نسخه می‌سازیم. فایل webkit41 مال نسخه‌های جدید است.
📥
دانلود همهٔ فایل‌ها:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1440" target="_blank">📅 13:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1438">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۵
🐧
رفع یک اشکال مهم روی لینوکس
روی لینوکس، بستن پنجره باعث می‌شد برنامه ناپدید شود اما در پس‌زمینه اجرا بماند — بدون هیچ آیکونی برای برگرداندنش. تنها راه بستنش، kill کردن از ترمینال بود.
دلیلش این بود: برنامه فرض می‌کرد آیکون نوار وظیفه ساخته شده، در حالی که خیلی از محیط‌های دسکتاپ (از جمله گنوم بدون افزونهٔ AppIndicator) اصلاً چنین آیکونی نشان نمی‌دهند.
حالا برنامه واقعاً بررسی می‌کند که آیا آیکونی نمایش داده می‌شود یا نه. اگر نه، بستن پنجره یعنی بستن برنامه.
📡
اشتراک اتصال روی شبکهٔ محلی
حالا می‌توانید اتصال این دستگاه را با دستگاه‌های دیگر روی همان شبکه به اشتراک بگذارید — گوشی، تلویزیون، یا هر چیزی که روی همان وای‌فای یا هات‌اسپات است.
تنظیمات ← اتصال ← «اشتراک روی شبکهٔ محلی» را روشن کنید. بعد از اتصال، آدرسی که در صفحهٔ اصلی نشان داده می‌شود را در دستگاه دیگر وارد کنید.
⚠️
توجه کنید: هر کسی که روی آن شبکه باشد می‌تواند از این اتصال استفاده کند و از کسی رمز پرسیده نمی‌شود. این را برای هات‌اسپات خودتان یا شبکهٔ خانگی روشن کنید، نه روی وای‌فای عمومی.
📤
خروجی گرفتن دسته‌جمعی از کانفیگ‌ها
اگر کانفیگ‌های خودتان را وارد اپ می‌کنید و تستشان می‌گیرید، حالا می‌توانید آن‌هایی که تست را پاس کرده‌اند یکجا خروجی بگیرید — به‌جای اینکه یکی‌یکی share بزنید.
تست بگیرید ← موارد سالم را انتخاب کنید ← «خروجی انتخاب‌شده‌ها»
خروجی را می‌توانید کپی کنید یا در یک فایل ذخیره کنید تا به گوشی یا تلویزیون منتقل کنید. حالت Base64 هم موجود است، چون بعضی کلاینت‌ها همان را می‌پذیرند.
━━━━━━━━━━━━━━━
⚠️
اگر نسخهٔ ۱.۰.۱۴ نسخهٔ مک (Intel) را دانلود کرده‌اید
فایل آن نسخه ناقص ساخته شده بود و احتمالاً درست کار نمی‌کند. لطفاً نسخهٔ جدید را دانلود کنید.
📥
دانلود:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1438" target="_blank">📅 12:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1437">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-poll">
<h4>📊 با whitevpn desktop وصل هستید ؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1437" target="_blank">📅 11:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1436">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دوستان، یه توضیح مهم درباره پروژه X4G که توی ویدیوی بالا معرفی کردیم:
بعد از انتشار ویدیو متوجه شدیم که به نظر می‌رسه بخش قابل توجهی از پروژه X4G از پروژه RVG گرفته شده، بدون اینکه اعتبار مناسبی به سازنده اصلی داده شده باشه.
🔗
پروژه اصلی
(لطفا برای حمایت استار بدید)
https://github.com/arvin341az-glitch/RVG
✍️
برای اینکه از سمت WhiteDNS حق و اعتبار سازنده اصلی تا جای ممکن رعایت بشه، این کارها رو انجام می‌دیم:
- اسم RVG رو به عنوان ویدیو اضافه می‌کنیم.
- توضیح مربوط به این موضوع رو در کامنت‌های ویدیو پین می‌کنیم.
- لینک گیت‌هاب داخل توضیحات ویدیو رو به ریپوی اصلی RVG تغییر می‌دیم.
این جور اتفاق‌ها متأسفانه توی دنیای Open Source پیش میاد. ما قبل از ساخت ویدیو با هیچ‌کدوم از توسعه‌دهنده‌های این پروژه‌ها در ارتباط نبودیم و طبیعتاً تشخیص اینکه یک پروژه از پروژه دیگه کپی شده، همیشه از قبل ممکن نیست.
ممنون از دوستانی که این موضوع رو به ما اطلاع دادن.
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/whitedns/1436" target="_blank">📅 03:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1433">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی  این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/whitedns/1433" target="_blank">📅 20:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1432">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=YMQN3Dsch12rzoNmjEzg7QmMjK3IZk1MHC6d0XVf0mEFRMZMoAqC6taECcvrtqrJbeof4Bo4G3GZs1s7QIV15OwKYVLFoqfvF7sfuJznSAlwj0ffjam5Ol59bpiW7hTe5Gvm5SBwWxXEtcei1zNWBD2iIKuxb98Ie4iiEA_vbwh06sn2P3sumP7B8V76NTlQKGolkIG9KgtMAB6ybboO710nswORkGjyTChcXUn6bgAe_q_yCQPwG-lHz32nS7bnEKljMBUVibWjH1_-Jv4n_RMPjUPZxVNiJmJNxk44h8BFRnAK5-5f5FcfAoL_m3uEIMlj1l03eD-w_6FGVQhz2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=YMQN3Dsch12rzoNmjEzg7QmMjK3IZk1MHC6d0XVf0mEFRMZMoAqC6taECcvrtqrJbeof4Bo4G3GZs1s7QIV15OwKYVLFoqfvF7sfuJznSAlwj0ffjam5Ol59bpiW7hTe5Gvm5SBwWxXEtcei1zNWBD2iIKuxb98Ie4iiEA_vbwh06sn2P3sumP7B8V76NTlQKGolkIG9KgtMAB6ybboO710nswORkGjyTChcXUn6bgAe_q_yCQPwG-lHz32nS7bnEKljMBUVibWjH1_-Jv4n_RMPjUPZxVNiJmJNxk44h8BFRnAK5-5f5FcfAoL_m3uEIMlj1l03eD-w_6FGVQhz2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/whitedns/1432" target="_blank">📅 19:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1431">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/whitedns/1431" target="_blank">📅 16:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1430">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">White DNS
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1430" target="_blank">📅 12:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1428">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">White DNS
pinned «
دوستان عزیز،  در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1428" target="_blank">📅 12:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1427">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز،
در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.
🔗
https://www.youtube.com/@WhiteDNS
ممنون از همراهی همیشگی شما
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/1427" target="_blank">📅 12:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1426">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-text">📚
آموزش اسکن Resolver و استفاده در WhiteDNS (cottendns)
اگه دنبال یه Resolver مناسب و پایدار برای راه‌اندازی WhiteDNS هستی، توی این آموزش قدم‌به‌قدم نحوه اسکن و پیدا کردن IPهای مناسب با Clean IP Finder و استفاده از اون‌ها در CottonDNS رو توضیح دادیم.
⚡️
🔍
کاربردها:
• اسکن و پیدا کردن ریزالور های مناسب
• بررسی پایداری و سرعت Resolverها
• استفاده در WhiteDNS
• بهبود کیفیت و پایداری اتصال
📥
دانلود ابزارها:
🔹
Clean IP Finder v1.3.6
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.6
🔹
WhiteDNS v1.6.0
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚡️
ابزارها رو دانلود کن و طبق آموزش پیش برو.
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/whitedns/1426" target="_blank">📅 08:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1424">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۴
🔧
رفع اشکال آیکون نوار وظیفه (taskbar)
در نسخه‌های اخیر، منوی راست‌کلیک روی آیکون کار نمی‌کرد و امکان بستن برنامه از آنجا وجود نداشت — تنها راه، Task Manager بود.
مشکل از حلقه‌ای بود که پیام‌های آیکون را می‌خواند و روی رشتهٔ (thread) اشتباهی اجرا می‌شد.
اگر نسخهٔ ۱.۰.۱۲ یا ۱.۰.۱۳ را نصب کرده‌اید، این به‌روزرسانی را حتما داشته باشید
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.14
@whitedns</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/whitedns/1424" target="_blank">📅 10:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1423">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ITUMrK1jNnYKR-B0l4oQtq9yfwb2bsequRTF7eKyxT5oDGTXswex5h4f4sE8ycIiNmVKTO7elc7BR1xZCMuKuIZQeIGWaverd295bKk3TRgzP1tEmTcsa49yhxEO2yKuX_L-b57pcD0ygpLL7E3eyuDAGhKR9KD5136UZahWKt6KoE-TV_yZ-sBeKf50Cg2brDhpqOBWV0mPi0QhEFS6Vzil-LmnG5SX9gI5hZ9Wr_B9iHPmpgPL6WCfV2NkX6WIrXuTuMMzXTPyDbL9sCA2tjmEfBEE3FS85T08BZe3zzztcSnGuVuQweijyHo4-r1qe3V7VtJU0V1YtLyWCNPFzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۳
Stable
🎯
حالت «فقط پراکسی» اضافه شد
تا حالا دو حالت بیشتر نبود و هر دو کل سیستم را از تونل رد می‌کردند. حالا سه حالت دارید:
• پراکسی سیستم — کل دستگاه (مثل قبل)
• فقط پراکسی — هیچ‌چیز روی سیستم شما تغییر نمی‌کند
• تونل TUN — کل دستگاه، حتی برنامه‌هایی که پراکسی را نادیده می‌گیرند
در حالت «فقط پراکسی» برنامه فقط گوش می‌دهد و شما خودتان تصمیم می‌گیرید چه چیزی از تونل رد شود. مثلاً فقط تلگرام، یا فقط یک افزونهٔ مرورگر — بقیهٔ سیستم دست‌نخورده و با سرعت عادی.
📌
چطور استفاده کنید
۱. تنظیمات ← اتصال ← «فقط پراکسی» را انتخاب کنید
۲. وصل شوید
۳. روی آدرس پراکسی در صفحهٔ اصلی کلیک کنید تا کپی شود
۴. همان را در تنظیمات پراکسی تلگرام وارد کنید
هم SOCKS5 و هم HTTP روی همان یک پورت کار می‌کند.
🔒
پورت دیگر عوض نمی‌شود
در این حالت پورت ثابت می‌ماند و خودتان می‌توانید تغییرش دهید. اگر برنامهٔ دیگری آن را گرفته باشد، همان موقع به شما می‌گوید — نه اینکه بی‌سروصدا پورت دیگری بگیرد و تنظیمات تلگرام شما یک روز بی‌دلیل از کار بیفتد.
━━━━━━━━━━━━━━━
⚠️
نکته برای کاربران فعلی
سوییچ TUN در تنظیمات جای خود را به یک منوی انتخابی داده. اگر قبلاً TUN را خاموش داشتید، روی «پراکسی سیستم» قرار می‌گیرید — یعنی دقیقاً همان رفتار قبلی. تا وقتی خودتان چیزی را عوض نکنید، هیچ فرقی نمی‌کند.
📥
دانلود:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/whitedns/1423" target="_blank">📅 19:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1422">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔵
WhiteVPN Desktop —نسخه 1.0.12
*stable *
🔋
از نسخه ۱.۰.۴ تا حالا تغییرات زیادی انجام  شده.
━━━━━━━━━━━━━━━
🔓
اشتراک‌هایی که باز نمی‌شدند، حالا باز می‌شوند
مهم‌ترین تغییر همین است. روی بعضی شبکه‌ها، اشتراک اصلاً دریافت نمی‌شد و خطای مبهمی دربارهٔ TLS می‌داد.
دلیلش این بود: نام سایت در اولین بستهٔ ارتباط بدون رمز فرستاده می‌شود. فیلترینگ همان یک بسته را می‌خواند و ارتباط را قطع می‌کند — قبل از اینکه اصلاً چیزی رد و بدل شود.
حالا آن اولین بسته به قطعه‌های کوچک شکسته می‌شود، طوری که هیچ قطعه‌ای نام کامل را در خود ندارد. سرور همان چیزی را دریافت می‌کند که همیشه، ولی دیگر چیزی برای تطبیق باقی نمی‌ماند.
این کار فقط وقتی انجام می‌شود که مسیر عادی شکست بخورد، پس روی شبکهٔ سالم هیچ کندی‌ای ندارید.
🔄
اشتراک‌ها خودشان به‌روز می‌شوند
اگر اشتراکی روی شبکهٔ شما باز نشود، فقط وصل شوید — اپ خودش آن را از داخل تونل دوباره می‌گیرد.
🔐
گزینه برای اشتراک‌هایی که گواهی‌شان تأیید نمی‌شود
روی بعضی شبکه‌ها چیزی وسط راه گواهی خودش را جای گواهی سرور می‌دهد. برای این حالت گزینهٔ «دریافت بدون بررسی گواهی» اضافه شده — فقط برای همان یک اشتراک، و فقط وقتی نشان داده می‌شود که واقعاً به کار بیاید.
⚠️
توضیحش را حتماً بخوانید: نشانی اشتراک کلید حساب شماست.
━━━━━━━━━━━━━━━
🔔
اطلاع از نسخه‌های جدید
اپ خودش بررسی می‌کند که نسخهٔ تازه‌تری منتشر شده یا نه و به شما اطلاع می‌دهد. دیگر لازم نیست دستی سر بزنید.
━━━━━━━━━━━━━━━
⚙️
تنظیماتی که حالا واقعاً کار می‌کنند
چند تنظیم بودند که ذخیره می‌شدند ولی هیچ اثری نداشتند. همه درست شدند:
• Split Tunneling —
اپلیکیشنی که کنار می‌گذاشتید واقعاً از تونل خارج می‌شود
• بررسی سلامت TLS — اتصالی که در آن دخالت شده باشد رد می‌شود
• نویز اتصال (Amnezia) — روی اتصال‌های WireGuard اعمال می‌شود
• پراکسی سیستم روی لینوکس — روی GNOME و KDE تنظیم می‌شود
━━━━━━━━━━━━━━━
🛡
حریم خصوصی و امنیت
• نشانی اشتراک دیگر در پیام خطا نمایش داده نمی‌شود. قبلاً اگر از صفحهٔ خطا اسکرین‌شات می‌گرفتید، کلید حسابتان هم در آن بود.
• روی ویندوز دیگر دسترسی Administrator نمی‌خواهد، مگر برای حالت تونل.
━━━━━━━━━━━━━━━
🐞
رفع اشکال
• پنجرهٔ مشکی PowerShell که هنگام اتصال در حالت TUN باز و بسته می‌شد
• نشتی DNS در حالت TUN
• در نصب تازه، لیست سرورها خالی نمایش داده می‌شد
• گزینهٔ پاک کردن اطلاعات برنامه و بازگشت به حالت اولیه در تنظیمات
• پیام‌های خطا حالا می‌گویند دقیقاً چه کاری باید بکنید
━━━━━━━━━━━━━━━
📥
دانلود برای ویندوز، مک و لینوکس:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.12
@whitedns</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/whitedns/1422" target="_blank">📅 14:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1420">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=bnq0j6MSARwb0Ky-42F8QYYidc40BXUqeX9k8juNxKckFbU0ZJv8lMoQkbVgiN-6XKF1V7y4oL6HXhVBZ8if6Yg2czz5-iKAKzPdCFzlMxH637cMvcCgDzvKNVMpP4IiWISZKFmMtsaEX6MiGPPP3l1AZ-iZHLk_v6PW1YGZnPvARmcAQ7ZilUv3ckBuuUD9KvKeclTvpAUdU-UoWneqDSU798nU3MrPLfHItwpsOFsEzDlcZKbrYvPkRTQiAm1ROk_Tp5Crcr66X4EOgbTy4VDyoWeOXczNh8h7kYi1z1-unA7P6QCb6Q253VFyTkwHuM5UyBBD_03E30__DV-jag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=bnq0j6MSARwb0Ky-42F8QYYidc40BXUqeX9k8juNxKckFbU0ZJv8lMoQkbVgiN-6XKF1V7y4oL6HXhVBZ8if6Yg2czz5-iKAKzPdCFzlMxH637cMvcCgDzvKNVMpP4IiWISZKFmMtsaEX6MiGPPP3l1AZ-iZHLk_v6PW1YGZnPvARmcAQ7ZilUv3ckBuuUD9KvKeclTvpAUdU-UoWneqDSU798nU3MrPLfHItwpsOFsEzDlcZKbrYvPkRTQiAm1ROk_Tp5Crcr66X4EOgbTy4VDyoWeOXczNh8h7kYi1z1-unA7P6QCb6Q253VFyTkwHuM5UyBBD_03E30__DV-jag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/whitedns/1420" target="_blank">📅 11:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1419">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔒
WhiteVPN Desktop نسخهٔ ۱.۰.۴ منتشر شد
🚀
۱. رفع نشتی DNS در حالت تونل — مهم‌ترین تغییر این نسخه
🔒
در نسخه‌های قبلی، وقتی روی حالت
TUN
وصل می‌شدید، خودِ ترافیک از تونل عبور می‌کرد — ولی درخواست‌های
DNS
از تونل بیرون می‌رفتند و مستقیم به مودم یا سرویس‌دهندهٔ اینترنت شما می‌رسیدند.
🌐
یعنی محتوای ارتباط شما محافظت می‌شد، اما
فهرست سایت‌هایی که باز می‌کردید برای ISP قابل دیدن بود
.
👀
علت پیدا و برطرف شد. حالت پراکسی هیچ‌وقت این مشکل را نداشت.
✅
⚠️
اگر از حالت TUN استفاده می‌کنید، حتماً بروزرسانی کنید.
🔄
۲. صفحهٔ Servers
🖥
•
انتخاب همه
اضافه شد
✅
•
کپی به کانفیگ‌های من
— یک سرور از ساب را به لیست خودتان کپی کنید و بعد آزادانه ویرایشش کنید
✏️
•
مخفی کردن
— سرورهایی را که نمی‌خواهید از لیست و از مسیر اتصال کنار بگذارید. بعد از بروزرسانی ساب هم مخفی می‌مانند، و هر وقت خواستید برمی‌گردانید
👻
• رفع به‌هم‌ریختگی ستون عملیات
🛠
⬇️
دانلود برای ویندوز، مک و لینوکس:
💻
🍎
🐧
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.4
@whitevpn
📲</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/1419" target="_blank">📅 05:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1418">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=l_4h5tZLAz5F8G9VNNKJJHp8zSLrmsimQVdc3me0cm-YcsM1hF9ozBi-JNYDIGMCDj9UFanMBjMESDkFZom_fUns_tgdSTrEtaOEgvBXXAE5pvRen7hIwDWTuZOPBcIiZY60RuGFJn9kTt524CEoLwtb7KkgG9X8oRmJg-9bsrMiBy98rLDYty8Rz5wzAsx2FWKbyPWNeqOEe8ZCvNRxKwYkcVFmYemX4wk7al18dFw_B7Ospqqt8uaoaOYMGL0eFiXWT7bfFpKk673rcVd93PWK7Vdo0sPJ0lasSB_i4GZjkACfwGp08pWFDEloCFrVZR9MJXB8TUe0NKErVy1wjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=l_4h5tZLAz5F8G9VNNKJJHp8zSLrmsimQVdc3me0cm-YcsM1hF9ozBi-JNYDIGMCDj9UFanMBjMESDkFZom_fUns_tgdSTrEtaOEgvBXXAE5pvRen7hIwDWTuZOPBcIiZY60RuGFJn9kTt524CEoLwtb7KkgG9X8oRmJg-9bsrMiBy98rLDYty8Rz5wzAsx2FWKbyPWNeqOEe8ZCvNRxKwYkcVFmYemX4wk7al18dFw_B7Ospqqt8uaoaOYMGL0eFiXWT7bfFpKk673rcVd93PWK7Vdo0sPJ0lasSB_i4GZjkACfwGp08pWFDEloCFrVZR9MJXB8TUe0NKErVy1wjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/whitedns/1418" target="_blank">📅 01:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1416">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚀
WhiteVPN Desktop نسخهٔ ۱.۰.۳ منتشر شد
۱. اتصال خودکار از پایه بازنویسی شد
✅
حالا دقیقاً مثل نسخهٔ اندروید کار می‌کند: اپ دیگر خودش نودها را یکی‌یکی امتحان نمی‌کند، بلکه انتخاب را به موتور می‌سپارد تا از بین صدها نود، بهترینِ در دسترس را بردارد — و اگر نودی از کار افتاد، خودش روی نود دیگر می‌رود.
نتیجه: اتصال در چند ثانیه
⚡️
، و خطای «could not connect» که خیلی‌ها می‌گرفتند برطرف شد.
۲. رفع مشکل حالت تونل (TUN)
🛠
مشکلی که باعث می‌شد روی بعضی سیستم‌ها کانفیگ در حالت پراکسی وصل شود ولی در حالت تونل نه، پیدا و برطرف شد. کسانی هم که IPv6 سیستمشان را غیرفعال کرده‌اند دیگر با خطا مواجه نمی‌شوند.
۳. حذف و ویرایش کانفیگ در صفحهٔ Servers
✏️
کانفیگ‌هایی که خودتان اضافه کرده‌اید حالا قابل ویرایش و حذف هستند. برای اصلاح یک کانفیگ دیگر لازم نیست همه را پاک کنید و از اول وارد کنید.
۴. پیام‌های خطای واضح‌تر
📢
اگر اتصالی برقرار نشد، اپ دلیل واقعی را نشان می‌دهد نه فقط «ناموفق» — هم برای شما روشن‌تر است، هم گزارش مشکل را خیلی راحت‌تر می‌کند.
⬇️
دانلود برای ویندوز، مک و لینوکس:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.3
@whitedns</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/whitedns/1416" target="_blank">📅 19:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1415">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AgD8uq08Cj_rJeIqlEGxfkG0nQ-4hbvSabtiVxGca41JVAW04sYtrl6M8oHaqLTv_KyjZyfhRmsMH0VJgLJoZYuUehkRjXW98w6hSKZp0vOKHpxVxqYwNLP2qeSYDQGSSNrc5uveNK60nghU0O3XycmJzZlAvkLZqOzUdiCtGu4rFreSBsNinZBfcae0DPfcbRwl-2m0qHjNjpgxMvcOS6UwzLgslQkQBmx7jsYK0hL8S4xP_gbb6poDxq8msZDRyzjFY1KGFhxTKha-dLIn3tjapRl9xBvl0Kk903dnXh1gvelXkVb9S70qZ8UA_HL8EZY9NNP8o5pN47gMy-I32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN
Desktop
نسخه 1.0.2 منتشر شد
🎉
مهم‌ترین تغییر: حالا هر نوع لینک اشتراکی را می‌شناسد
🔓
تا نسخهٔ قبل فقط لینک‌های اشتراک معمولی (vless، vmess، trojan و…) اضافه می‌شدند. اگر پنل شما خروجی Clash یا sing-box یا Xray می‌داد، برنامه خطا می‌داد
❌
از این نسخه این‌ها همه کار می‌کنند
✅
:
- لینک‌های اشتراک معمولی و base64
- کانفیگ Clash / mihomo (چه YAML چه JSON)
- کانفیگ sing-box
- کانفیگ Xray و v2rayN
- و حالت base64 هر کدام از این‌ها
فرقی نمی‌کند پنل شما کدام قالب را بدهد
📝
. سرورها مثل همیشه در صفحهٔ Servers می‌آیند و می‌توانید پینگ و سرعتشان را بگیرید
📶
، مرتب کنید و یکی را انتخاب کنید
🚀
.
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.2
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/whitedns/1415" target="_blank">📅 15:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1414">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🌎
نسخه‌ی دسکتاپ WhiteDns منتشر شد!
📤</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1414" target="_blank">📅 11:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1413">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚀
معرفی اپلیکیشن WhiteDNS Desktop
کلاینت قدرتمند تونلینگ DNS برای کامپیوتر
اگر به‌دنبال ابزاری حرفه‌ای برای تونلینگ DNS، مدیریت پروکسی و عبور از محدودیت‌های شبکه هستید،
WhiteDNS Desktop
یکی از کامل‌ترین گزینه‌های در دسترس است.
این اپلیکیشن یک کلاینت محلی DNS Tunneling را روی سیستم شما اجرا می‌کند و در کنار آن، امکانات پیشرفته‌ای برای مدیریت پروکسی سیستم در اختیارتان قرار می‌دهد.
✨
ویژگی‌ها و امکانات کلیدی
🔹
پشتیبانی کراس‌پلتفرم
قابل اجرا روی Windows، macOS و Linux
🔹
پشتیبانی از موتورهای مختلف
امکان انتخاب بین موتورهای:
• CottenDNS
• MasterDNS
• StormDNS
🔹
پروکسی محلی کامل
دارای پروکسی‌های محلی SOCKS5 و HTTP، همراه با قابلیت تنظیم خودکار پروکسی سیستم
پس از قطع اتصال نیز تنظیمات پروکسی سیستم به‌صورت خودکار به حالت قبلی بازگردانده می‌شوند.
🔹
مدیریت پیشرفته پروفایل‌ها
امکان ساخت و مدیریت:
• پروفایل‌های اتصال چنددامنه‌ای
• پروفایل‌های Resolver
• Import و Export تنظیمات
• تهیه بکاپ از پروفایل‌ها
🔹
پری‌ست‌های آماده
تنظیمات از پیش آماده‌شده برای شرایط مختلف شبکه:
⚡️
Speed
— برای دستیابی به بیشترین سرعت
🛡
Survival
— برای پایداری بیشتر در شبکه‌های محدود
🔒
TCP Survival
— برای اتصال پایدارتر با استفاده از TCP
🔹
مانیتورینگ زنده
نمایش لحظه‌ای:
• وضعیت اتصال
• آمار ترافیک مصرفی
• اطلاعات نشست
• لاگ‌ها و رویدادهای برنامه
⚠️
هشدار امنیتی بسیار مهم
نسخه‌های رسمی WhiteDNS Desktop فقط از طریق ریپازیتوری رسمی پروژه در GitHub منتشر می‌شوند.
برای حفظ امنیت سیستم خود، برنامه را از سایت‌ها، مارکت‌ها، کانال‌ها یا منابع متفرقه دانلود نکنید.
📥
دانلود آخرین نسخه از GitHub رسمی:
https://github.com/WhiteDNS/WhiteDNS-Desktop/releases/tag/desktop-v1.2.0
📢
عضویت در کانال رسمی تلگرام پروژه:
https://t.me/whitedns
🤍
WhiteDNS Desktop</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/whitedns/1413" target="_blank">📅 11:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1412">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌎
نسخه‌ی دسکتاپ WhiteVPN منتشر شد!
📤</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/whitedns/1412" target="_blank">📅 09:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1410">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhXC4vhLHjJAsS4snkrr8jxEb62VzVLdK8EQgy4fFJuZMq-W8qoCnFJft3mjV1LYQviPiBg14lEYlX4NsclVGanaKzsImIW279x767sb96SeUMtYg1MSm0KU56wKF5T5ahIyRkln4lNNs3LqO4C6MpcP_9qp4IqQlCk43dQCIJ0q2spSBIaQTNOncpvNM_f-fZTLcZuJVkHvfB5u-zJnqSYY0zeTgjrY14hJvmwb9mtKNTo6gxexTho_bba6qOFEGnahIBTCYwfeqKD2HJcn5O_ewVJtR69lVYpwxI4azY0dTwoWk-6gLCFJIMuz8-q_77Qp9TYOfLRuXS8SY55gDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
نسخه‌ی دسکتاپ WhiteVPN منتشر شد!
اگر می‌خواهید روی کامپیوتر بدون درگیری با تنظیمات پیچیده به VPN وصل شوید، WhiteVPN Desktop برای شما ساخته شده است.
💻
قابل استفاده روی:
• ویندوز
• مک، هم Apple Silicon و هم Intel
• لینوکس با بسته‌های AppImage، DEB و RPM
⚡️
اتصال ساده و سریع
• اتصال با اشتراک آماده WhiteVPN
• اضافه‌کردن اشتراک شخصی
• انتخاب خودکار بهترین سرور
• انتخاب دستی کشور، نوع اتصال یا سرور دلخواه
• نمایش IP و کشور واقعی اتصال
• بررسی خودکار سلامت اتصال و جایگزینی سرور خراب
📥
واردکردن کانفیگ شخصی
• پشتیبانی از VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard
• امکان واردکردن یک یا چند کانفیگ به‌صورت هم‌زمان
• فقط کانفیگ را کپی کنید و Ctrl+V یا در مک Cmd+V بزنید
• کانفیگ‌های شخصی در بخش Manual و بالای لیست قرار می‌گیرند
🚀
تست کامل سرورها
• بررسی سالم بودن سرور
• تست پینگ واقعی
• تست سرعت دانلود
• مرتب‌سازی بر اساس کشور، پینگ، سرعت و نوع کانفیگ
• تست‌ها بدون قطع‌کردن اتصال فعلی انجام می‌شوند
🛡
تنظیمات حرفه‌ای، با ظاهر ساده
• حالت Proxy برای ویندوز، مک و لینوکس
• حالت TUN برای اتصال کامل ویندوز
• تنظیم DNS و حریم خصوصی DNS
• Split Tunneling برای مدیریت مسیر برنامه‌ها
• تنظیم IP Fronting به‌صورت خودکار یا دستی
• مشاهده گزارش‌ها برای پیدا کردن سریع مشکلات اتصال
🧰
ابزارهای کاربردی
• White IP Generator: ساخت کانفیگ با White IP و اضافه‌کردن مستقیم به برنامه
• Validator: بررسی تعداد زیادی IP یا آدرس و ذخیره نتیجه‌ها
• Full Backup: پشتیبان‌گیری کامل از تنظیمات، اشتراک‌ها و کانفیگ‌ها و بازیابی آن‌ها
🌍
رابط کاربری کامل فارسی و انگلیسی
• نمایش صحیح راست‌به‌چپ
• فونت فارسی Vazir
• محیط ساده و مدرن
• ادامه اتصال در System Tray حتی بعد از بستن پنجره
📌
چند نکته درباره نسخه اول
• حالت TUN فعلاً فقط روی ویندوز فعال است
• در لینوکس ممکن است لازم باشد Proxy سیستم را دستی تنظیم کنید
• برنامه هنوز امضای دیجیتال ندارد؛ بنابراین ویندوز یا مک ممکن است هنگام اجرای اول هشدار نمایش دهد
🔓
WhiteVPN Desktop متن‌باز است و تحت مجوز GPL-3.0 منتشر می‌شود.
⬇️
دانلود آخرین نسخه:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
اگر برنامه برایتان مفید بود، لینک آن را برای دوستانتان هم بفرستید
❤️</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/whitedns/1410" target="_blank">📅 09:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1409">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سرور های فعال WhiteDNS داشته باشید برای تست و زمان قطعی (کلیک کنید روش کپی میشه)
کلاینت اندروید و IOS از CottenDNS پشتیبانی میکنن و به زودی کلاینت ویندوز هم آماده میشه
Server #1 thx to LordofCinder
♥️
Location: Turkey
🇹🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HufCfh7cgdGh4IHRvIExvcmRvZkNpbmRlciIsInNlcnZlciI6eyJkb21haW4iOiJ2LmFzaGVudGFqaXIuc2JzLCBjLmFzaGVudGFqaXIuc2l0ZSIsImVuY3J5cHRpb25fa2V5IjoiZTU1NGI4ZmI4ZGU4Mjc4ZDJmMTFlODcwNDA0NDI2OWEiLCJlbmNyeXB0aW9uX21ldGhvZCI6M319fQ
Server #2 thx to Bamdad
♥️
Location: Germany
🇩🇪
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HqfCfh6ogdGh4IHRvIEJhbWRhZCIsInNlcnZlciI6eyJkb21haW4iOiJjLmJhbWFrLnh5eiIsImVuY3J5cHRpb25fa2V5IjoiMmRkZWI5ZGYyYzJiYTRkMyIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #3 thx to Araskhatare
♥️
Location: France
🇫🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-Hq_Cfh7cgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InBhcmlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI1MjViNjkwYjU4ZmU0MTI0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
Server #4 thx to Araskhatare
♥️
Location: France
🇫🇷
2
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-Hq_Cfh7cgMiB0aHggdG8gQXJhc2toYXRhcmUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiYS5hcmFzLmRwZG5zLm9yZyIsImVuY3J5cHRpb25fa2V5IjoiNzFkM2MwOWYyYmY1NmVkYSIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #5 thx to Coreforge
♥️
Location: Turkey
🇹🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7nwn4e3ICAgdGh4IHRvIENvcmVmb3JnZSIsInNlcnZlciI6eyJkb21haW4iOiJ2LmFub255bW91cy5vYnNlcnZlciIsImVuY3J5cHRpb25fa2V5IjoiYjI3NTAzOTE5OWIxYzhjOSIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #6 thx to Araskhatare
♥️
Location: USA
🇺🇸
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7rwn4e4IDIgICB0aHggdG8gQXJhc2toYXRhcmUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidXNhLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI5MzY5NjVjZWYzOWQzMmE5N2JlMWEzZDA4YzhiZmM5MyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
آموزش استفاده از برنامه اندروید
👇
https://www.youtube.com/watch?v=tz8cj7HzHVI
آموزش استفاده از برنامه ios
👇
https://www.youtube.com/watch?v=filwdiPKN90
آموزش استفاده از برنامه ویندوز
👇
https://youtu.be/Mc--GlKw2wg
@whitedns</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/whitedns/1409" target="_blank">📅 04:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1407">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/3ae84e81b7.mp4?token=pHxhrFG4cwxh__71g_avrXdh4eREiKeArJsL1ovd9uauI-IxT1HNZsBmteJoshyc897oS83z6o1MgtR7Pk4by3Y8EWejujdrkZ5iy0hFAYEP7mwB99imkCKuiM_y03a3gP9FCTSJPpPCKwGI6MTcAuj0u9oiFI88NfgFHr7e6SH_0q-K4amioivNI0vHYdtnZXNJk1NEdWUCHUrsFRFbFHnjP-gf4zlWckanoTZLM5Z5qLinLHNDxGCfOWE9u7fYJ2IA3a9Zm5Y63IlyqkhFlLN7PPLc-3gndkOT9qp2Bt6wzGtXV2h23o9Cmrsqxp0XatDkh2lmry45_2LLGDKrdA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/3ae84e81b7.mp4?token=pHxhrFG4cwxh__71g_avrXdh4eREiKeArJsL1ovd9uauI-IxT1HNZsBmteJoshyc897oS83z6o1MgtR7Pk4by3Y8EWejujdrkZ5iy0hFAYEP7mwB99imkCKuiM_y03a3gP9FCTSJPpPCKwGI6MTcAuj0u9oiFI88NfgFHr7e6SH_0q-K4amioivNI0vHYdtnZXNJk1NEdWUCHUrsFRFbFHnjP-gf4zlWckanoTZLM5Z5qLinLHNDxGCfOWE9u7fYJ2IA3a9Zm5Y63IlyqkhFlLN7PPLc-3gndkOT9qp2Bt6wzGtXV2h23o9Cmrsqxp0XatDkh2lmry45_2LLGDKrdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
نسخه دسکتاپ
whitevpn
اماده شده است و به زودی بعد از طی مراحل آزمایش منتشر خواهد شد
@whitedns</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/whitedns/1407" target="_blank">📅 19:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1403">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
پترنیها یه اپلیکیشن مشابه v2rayng زده که به نظرم از خود v2 هم بهتره چرا؟
هسته بروز که توسط خود پترنیها داخل اپ قرار گرفته و بروز بودنش حتی از v2 هم زودتره(بیشتر آپدیت هسته v2rayng از سمت پترنیها بوده)
رابطه کاربری روان تری داره.
مهم ترین نکته اش اینه با قابلیتی که واسه
#فرگمنت
اضافه کرده شما دیگه محدودیت آپلود داخل کانفیگ هاتون ندارید(بیشتر کلودفلره) ولی بعَی سرور شخصی ها هم مشکل آپلود دارن که طبق تنظیمات پترنیها اکی میشه
🔥
دانلود اپ از گیتهاب:
💓
https://github.com/patterniha/v2rayNG/releases
تنظیمات مربوطه به آپلود:
📝
https://t.me/patt_channel_x/94?single
💡
دوستانی که پترنیها رو نمیشناسن:پتنریها خالق sni spoof و شیر و خورشید و همچنین کلی از کارای بزرگتری بوده و داشته از جمله خود v2ryang و...
@xsfilterrnet
👑
@patt_channel_x
✅</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/whitedns/1403" target="_blank">📅 15:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1402">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال  سریع‌تر و پایدارتر بوده است.  امکانات و بهبودهای جدید: •  شروع اتصال سریع‌تر •  انتخاب هوشمند بهترین سرور •  جابه‌جایی خودکار در صورت اختلال سرور •  کاهش خطا و نیاز به چندبار زدن دکمه اتصال •  بهبود Real…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/whitedns/1402" target="_blank">📅 15:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1401">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS_Setup_Servers.md</div>
  <div class="tg-doc-extra">3.8 KB</div>
</div>
<a href="https://t.me/whitedns/1401" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
آموزش نصب DNS اختصاصی برای WhiteDNS
آموزش کامل و
قدم‌به‌قدم
نصب و راه‌اندازی:
🟢
CottenDNS
🔵
StormDNS
🟣
MasterDNS
از تنظیم دامنه در Cloudflare تا نصب DNS و دریافت
Encryption Key
🔐
📚
آموزش به‌صورت متنی آماده شده و
لینک آموزش ویدیویی
هم داخل پست قرار گرفته.
🎥
📥
فایل آموزش رو دانلود کن و برای روز مبادا نگهش دار!
🚀
@WhiteDNS
·:¨༺
@BlueKnight_Net
༻:</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/whitedns/1401" target="_blank">📅 16:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1398">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/whitedns/1398" target="_blank">📅 12:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1397">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc0b81933.mp4?token=drYJDEoBxsaBgnEbFYbm7i91vLRkqacu5k6HflwRa39PnZTpAO9WessLm-aYugYd5JgKQQPlHfvV8Q-8EtM4Fp0HgARrMIjmitSjRrPe7zgGzscpL7mBhkEbUxjmKmJgfJtlc2ux5bRDgtGc6TLHwMjRBxuzc0n1tgYe_HODB140qJnWd6rhm8oTEnT57Qgy7u1NuvRkCS71VtTtMfOIcHwxj33CymDEsiNmE4IyoA_nzONSjlgE2GwEVwUZ7Jp4UmJKBT9ZdSXPlu40g5aZzPxuXXnTSnJn81f07WHR11Ce7advwO6QbmvBLMsbXynDfoF-vJdUd0PtPBeaBkn_Oah2LumkhS5QYSa7RJp9uwErWm9L4oMP2fp6bx4KClBGEL-F-HfytwiUyG4oH-m12HwpF3eBCfr3CHGWLJAIQlbZ_ZtjddxFoKgL-MIBta-uC_RZvb8t7WPSC9miEoJ0abaWvDdxU0o1e29eCzxDmta8VpzR7WtpgdUoPdnHXLFY_UW5HBfAt5w0-Q-rVc9qCj25IiVX4YXCcbfA8qA-poS-wWVgEeJbzm_NVMCR6LrUhwmGMZy6dKBfqqcWx7IbRivIj2vxH3BWfrzn4VpmFWYqorVWvzm7ya2ei5cKvCoVUGDHPHz-OzXqJvbc55BnfHInK84iKkzMVcDPp8zo3PM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc0b81933.mp4?token=drYJDEoBxsaBgnEbFYbm7i91vLRkqacu5k6HflwRa39PnZTpAO9WessLm-aYugYd5JgKQQPlHfvV8Q-8EtM4Fp0HgARrMIjmitSjRrPe7zgGzscpL7mBhkEbUxjmKmJgfJtlc2ux5bRDgtGc6TLHwMjRBxuzc0n1tgYe_HODB140qJnWd6rhm8oTEnT57Qgy7u1NuvRkCS71VtTtMfOIcHwxj33CymDEsiNmE4IyoA_nzONSjlgE2GwEVwUZ7Jp4UmJKBT9ZdSXPlu40g5aZzPxuXXnTSnJn81f07WHR11Ce7advwO6QbmvBLMsbXynDfoF-vJdUd0PtPBeaBkn_Oah2LumkhS5QYSa7RJp9uwErWm9L4oMP2fp6bx4KClBGEL-F-HfytwiUyG4oH-m12HwpF3eBCfr3CHGWLJAIQlbZ_ZtjddxFoKgL-MIBta-uC_RZvb8t7WPSC9miEoJ0abaWvDdxU0o1e29eCzxDmta8VpzR7WtpgdUoPdnHXLFY_UW5HBfAt5w0-Q-rVc9qCj25IiVX4YXCcbfA8qA-poS-wWVgEeJbzm_NVMCR6LrUhwmGMZy6dKBfqqcWx7IbRivIj2vxH3BWfrzn4VpmFWYqorVWvzm7ya2ei5cKvCoVUGDHPHz-OzXqJvbc55BnfHInK84iKkzMVcDPp8zo3PM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش دریافت دامنه رایگان و نامحدود
دیگه لازم نیست برای کانفیگ های شخصیتون دامنه بخرید.
https://youtu.be/Tiods_aCJX8
@WhiteDNS</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/whitedns/1397" target="_blank">📅 11:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1395">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوستان عزیز،
در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.
🔗
https://www.youtube.com/@WhiteDNS
ممنون از همراهی همیشگی شما
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/whitedns/1395" target="_blank">📅 10:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1394">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/whitedns/1394" target="_blank">📅 08:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1393">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
لطفا تست کنید و نتیجه رو با ما به اشتراک بگذارید.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/whitedns/1393" target="_blank">📅 07:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1388">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/whitedns/1388" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/whitedns/1388" target="_blank">📅 07:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1387">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py4HYbsayY0P7nx1R-dN-2j42N8gd2WAuHKP_hj-6x1IiKfuKqWnk6qXhZ5MRL3pW7zNirvTpgxPaTLXU_BTtUBG0EwBs5xj3v-cM_EoeVcDWYHCzRFbHAYawUmVaGid5SDow5_senX55y4tTQeARb2zKdlQcn3Ero9Gspk_cl0dJ2aUQ7tEz3caCr49rovkH-oD13kZFhYTHtGN0XFRnlDzUpJuvbi8kGXZ3I69C-s31vn0J0pPbXGnRxEt9gCXMVRutnblqNo8fysJGSXFkQ1zsrtJL2MfagiU-bCtAwYtm-WibTweTWxpyS_9f_rhizySZmoL6WVX3hWQMwBaOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال
سریع‌تر و پایدارتر بوده است.
امکانات و بهبودهای جدید:
•  شروع اتصال سریع‌تر
•  انتخاب هوشمند بهترین سرور
•  جابه‌جایی خودکار در صورت اختلال سرور
•  کاهش خطا و نیاز به چندبار زدن دکمه اتصال
•  بهبود Real Delay Test
•  رفع مشکل متوقف‌شدن اتصال در مرحله شروع
هیچ تنظیم خاصی لازم نیست؛ فقط برنامه را به‌روزرسانی کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/whitedns/1387" target="_blank">📅 07:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1386">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⛏
اگر در اتصال به WhiteVPN مشکل خوردید مراحل زیر را اجرا کنید
۱. به صفحه تنظیات برید
۲. از گرینه حریم خصوصی DNS گرینه DOH را انتخاب کنید
۳. مقدار زیر را جاگزین کنید
https://doh.whitedns.workers.dev/dns-query</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/whitedns/1386" target="_blank">📅 17:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1378">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9WZTniyFu5aSI4tmzUdTs7NdOgyYmttxmZAjX5ox4i_OMyyK7RNyrrxKFPnQAvF4pPmDpec--PIVT-NVS1VhClWaeNXvFOHVn8a-bgA2S6BEKV0MNfbXKaiWKJrklGZA7fyiqNZeEqHp2dwb_zcfSwQgXjPO_feUv9qtZ7X3ww5d2iSbVBNxqYVUQAYTH4R9ycr6tKxMD_uL5gA2LDu_cxK3e59bPjkQez-z4K5nxU-n2JNBM6vP5dpWjg9c7ymLlfMk3IniQ-C0DY_DUifnq3uh07rdA-n_GQUvXY9T-yudvVtVQTsKcuWj4TM3dP2A4smwahxmOxWeEwAQsQOsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای  ویندوز
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
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/whitedns/1378" target="_blank">📅 11:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1377">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kw1UIsdJcM32Y32mHmH5KRj5lKGiS9VruYmKYxPtxg-0SKK0SKm1ij8yTOsiFxfLnOK4UwHiRL4TG838-fEZE1iSIdteGHX6VHlti05Czsnvdpc1yXw78beAhXW0haPWKaj78IUb1HCGtfNNmbbWC1N6jkydqy2INMJ-uSs-ThXMM9qT5Mhir3MRYYnt5Q76VmYOBpCnrKmfCNJ63U5a85kQv9tNvRaCYk-asuAC4kUYs0bA1h6U_5ztqs6tGxSLOgeQ-Tve5e2Ck417SnufEbJTq6fXpymBa1yMYLVFm9XMO1rV203qDiU81rGcuyHoakfWRdhL4OLInUjC2Y5V7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/whitedns/1377" target="_blank">📅 04:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1375">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-text">پروژه دفید روی گوگل پلی قرار گرفت
میتونید از قسمت تنظیمات از چت ها و .. فایل پشتیبان بگیرید و بعد حذف کنید و بعدش از طریق گوگل پلی برنامه رو نصب کنید و دوباره فایل پشتیبان رو بازیابی کنید
https://play.google.com/store/apps/details?id=com.thefeed.android
میتونید با امتیاز ۵ ستاره دادن به پروژه از من حمایت کنید
🙏
❤️
❤️
❤️
ویدیو آموزشی پروژه:
https://t.me/networkti/516</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/whitedns/1375" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1374">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور   https://youtu.be/epG70Xl1xGI   @WhiteDNS</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/whitedns/1374" target="_blank">📅 11:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1373">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=iBprZ3dPfGuwnd117XpzSjBitA09uvZneyF9d4FD7WFjZO2auMQ8HKAD_4roFMw1uAG4s8tcljZveCRP5CnhbmoUED0Tm1K0mY-ImdWqPUN-oxYdly-9btdvLiptvupmcUb2TmPQJmIYO1TiHjQpGw9yRdGveCllUEUoFoike2PCcOO9y9oA6dmMgKD0taNSuzChLZ3tgBXG_8JHwZC8XvykK13Gll3yFpIFGNi-wObQkmllywoJJ_BQXn5CY9FXcdUU44hLQtvv0aB2vZcHirgR-N7xB2VLGLZnvs7PXZYUMJQdbJN06t67rkYHVnEX5Q5Tjrd42U0NUU1YDRAQY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=iBprZ3dPfGuwnd117XpzSjBitA09uvZneyF9d4FD7WFjZO2auMQ8HKAD_4roFMw1uAG4s8tcljZveCRP5CnhbmoUED0Tm1K0mY-ImdWqPUN-oxYdly-9btdvLiptvupmcUb2TmPQJmIYO1TiHjQpGw9yRdGveCllUEUoFoike2PCcOO9y9oA6dmMgKD0taNSuzChLZ3tgBXG_8JHwZC8XvykK13Gll3yFpIFGNi-wObQkmllywoJJ_BQXn5CY9FXcdUU44hLQtvv0aB2vZcHirgR-N7xB2VLGLZnvs7PXZYUMJQdbJN06t67rkYHVnEX5Q5Tjrd42U0NUU1YDRAQY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور
https://youtu.be/epG70Xl1xGI
@WhiteDNS</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/whitedns/1373" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1371">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">3 سرور اهدای CottenDNS
لطفا تست کنید و نتیجه رو بهمون بگید ( کلیک کنید روش کپی میشه )
Server #1 thx to Araskhatare
♥️
Location: Germany
🇩🇪
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HqfCfh6ogdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Imdlcm1hbnkuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjI5ODQ0NDhjZDRkZTYxZjgiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
Server #2 thx to Araskhatare
♥️
Location: France
🇫🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-Hq_Cfh7cgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InBhcmlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI1MjViNjkwYjU4ZmU0MTI0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #3 thx to Araskhatare
♥️
Location: Israel
🇮🇱
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HrvCfh7EgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiIyMjRiOWU4MjVlMzFkNWY0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
@whitedns</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1371" target="_blank">📅 23:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1370">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/C1k9RWr8JpeoNGZ3YZipI_1KP_RgF0K-BdTsvP-aNh-61SAWJD-us_Bwo93rJ7iQ7ebCjobauRZ81mSGiJ1HdrfX6LatWo6DOf6Xh8glLIhwe71JNau3P0u9DyE3i-f-HKfRueY6nt1iGVmrcr3tjfspVugkcbl5gW-i6Icm3W0anLVYyLB0tmJUpdw9ekkQCqwTyZY5LeY8ZdrPhSapgXb9YQLW3hhzY2DoAMlWX7xex9mQSjoe3tplpqzxoUtVy1AQLAcjDsb5t3PCcX_6l1YiIYJdZIXwInwQi3r31k5GNLRxx7H0tJK5AhSmh8t8RNEc4PNmwbOLtSZeA142_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه مهم درباره وضعیت ممیزی امنیتی پروژه‌ها
از این پس، هر پروژه‌ای که از برنامه ممیزی امنیتی
WhiteDNS Security
خارج شود، دیگر تحت نظارت امنیتی ما نخواهد بود.
این موضوع به این معناست که:
آخرین نتیجه ممیزی تنها مربوط به نسخه‌ای است که در زمان ارزیابی بررسی شده است.
هرگونه تغییر در کد، تنظیمات، زیرساخت، وابستگی‌ها یا به‌روزرسانی‌های بعدی می‌تواند وضعیت امنیتی پروژه را تغییر دهد.
پس از خروج پروژه از فرآیند ممیزی، WhiteDNS هیچ تضمین، تأیید یا مسئولیتی نسبت به امنیت نسخه‌های جدید یا وضعیت فعلی آن پروژه نخواهد داشت.
ادامه استفاده از پروژه، صرفاً بر عهده توسعه‌دهندگان و کاربران آن است.
در صورت بازگشت پروژه به برنامه ممیزی و انجام ارزیابی مجدد، نتیجه جدید به‌صورت رسمی اعلام خواهد شد.
آخرین وضعیت معتبر هر پروژه، تنها از طریق اطلاعیه‌های رسمی WhiteDNS قابل استناد است.
@whitedns</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/whitedns/1370" target="_blank">📅 11:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1368">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این روزها شاید همه استرس داشته باشیم
🤯
، بی‌حوصله باشیم
😑
و حالمون خوب نباشه
🥀
برای همین درست نخوانیم
📖
، درست نبینیم
👀
، ...
ولی برای اینکه نه به خودتون
🙅‍♂️
و نه به ما بد بگذره، لطفاً متن‌هایی که توی کانال می‌گذاریم را با دقت بخونید
✨
👀
ممنون
🙏
😊</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/whitedns/1368" target="_blank">📅 05:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1367">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TsF0QbJQsJenNd0b_kJJkcgDlVq-Gjjd83P-PfhFE7CaJmitBhvCyFYYZuvvIhssAMuiogLK31jY6r3zjIYCE5oVZHDqcSaOGSDug9UFpQREXk5cCjOKtan9jQVKCo1WXYFKcmHaB41ONUy5zHVq8j7FYl5ZPTP02vOh1EnzBRCfkJxMrptLtfybA2w5IGzaoBLNFCaptzudCdDjdP1PXPdcU6Hs3v_vAl2DW8cqj9-q_Ldma0zjdBRWQ8EcVr3y8Crtv7yzsaBiyeRNKJe1Yll21digLrKnRuw3NzWXMc5kgwfvK3RILYvaMCdZWSpN4OND8x6IV7cKt1yTWqNmRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!
هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده.
منم یه مشارکت کوچولویی روی خود هسته داشتم.
تغییرات اصلی این آپدیت:
1-
امنیت در پروتکل MASQUE:
قبلاً وقتی وصل می‌شدید، کلاینت هیچ تاییدیه‌ای از سرور نمی‌گرفت و اگر کسی وسط راه سعی می‌کرد با یه سرتیفیکیت فیک گولتون بزنه، برنامه متوجه نمی‌شد. اما الان اتصالات MASQUE سرتیفیکیت سرورهای کلادفلر رو به صورت دقیق (از طریق هش‌های SPKI) بررسی می‌کنن تا دیگه کسی نتونه ترافیک رو شنود کنه.
2-
پایداری WireGuard و Gool:
قبلاً بعضی وقتا برنامه بهتون می‌گفت متصل شدید، در حالی که دیتا اصلاً ردوبدل نمی‌شد و فقط روی یه پروکسی SOCKS5 گیر کرده بود. اما الان یه سیستم بررسی سلامت (Health Check) مداوم داره که اگر دیتایی از سمت سرور برنگرده، خودش به صورت اتوماتیک اتصال رو قطع و دوباره وصل می‌کنه.
3-
اتصال مجدد خودکار در Gool:
تو نسخه‌های قبل اگه تونل بیرونی Gool قطع می‌شد، کل فرآیند کِرَش می‌کرد و خارج می‌شد. الان Gool هم مثل بقیه پروتکل‌ها خودش هوشمندانه دوباره ریکانکت می‌کنه.
4-
فیکس شدن نشت مموری (Memory Leak):
یه باگ رو اعصاب بود که وقتی اتصالتون زیاد قطع و وصل می‌شد، تسک‌های قدیمی تو بک‌گراند باز می‌موندن و آروم‌آروم رمِ سیستم پر می‌شد. این مشکل تو تمام پروتکل‌ها کامل برطرف شد.
5-
هوشمندی در مصرف منابع:
از این به بعد Aether همون اول کار، تعداد هسته‌های CPU و مقدار رم سیستمتون رو می‌خونه و میزان اسکن همزمان (Concurrency)، بافرهای شبکه و صف‌های داخلیش رو بر همون اساس تنظیم می‌کنه. این قابلیت برای کسایی که می‌خوان ابزار رو روی روترها و بردهای ضعیف‌تر بالا بیارن فوق‌العاده‌ست.
لینک گیت‌هاب برای دانلود(نسخه‌های مک، لینوکس و ویندوز):
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.6.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/whitedns/1367" target="_blank">📅 05:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1362">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn-v1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">20.1 MB</div>
</div>
<a href="https://t.me/whitedns/1362" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/whitedns/1362" target="_blank">📅 05:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1361">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9xi4RNifaDtiBYUjpF1v_c_CNan50TG4f3BePafN5SCxU5vdDp5Qm4pwgG0dp4IC8s7yynzdLj-srpFpEvYUFYQcpNilZDu-ytG7N41nKfpy__Xh4iSp3FdHK10pGRGExY_nANdsUcXB6pNW4Y5XZtiZwrOhaUkDPn6x2FbFfnfVsnUI89UJm75vkuSvTnoIIPSer_JtfQSewcQ1nx11NpiUnHrZTD87KX-1XbgQ7y2exSeVnVTroZ2kbE36H3fxdCRltG8S-hERJrcpqVJzk-j4gHK1qcIrabFENxcIYr8hdqVVWlHTUrdmq94QKr7JbRoCaq4DLy1xtHgD3EdMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN 1.1.0 منتشر شد!
در این نسخه چند قابلیت کاربردی اضافه کردیم تا اتصال راحت‌تر، سریع‌تر و امن‌تر باشه:
🛡
اتصال همیشگی VPN
می‌تونید WhiteVPN رو طوری تنظیم کنید که همیشه فعال بمونه و در صورت قطع شدن، دوباره متصل بشه.
🔒
امکان Kill Switch
اگر VPN قطع بشه، اینترنت هم موقتاً متوقف می‌شه تا اطلاعات شما بدون محافظت منتقل نشه.
⚡️
قابلیت Real Delay Test
حالا می‌تونید تأخیر اتصال‌ها رو بررسی کنید، نتیجه‌ها رو ببینید و سریع‌ترین گزینه رو راحت‌تر انتخاب کنید.
✨
طراحی جدید صفحه اشتراک‌ها
صفحه اشتراک‌ها ساده‌تر، مرتب‌تر و خوش‌دست‌تر شده تا مدیریت و انتخاب اشتراک‌ها راحت‌تر باشه.
همین حالا WhiteVPN رو به نسخه 1.1.0 به‌روزرسانی کنید
🤍</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1361" target="_blank">📅 05:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1360">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/r0KUAZEsO43e8sY3E2Mp4dkd51HDquf3BXfq9F1ACNz6U0P0XUUoPD00-6L9pbQHcO-WkfqFSL8JHw1O0ktIjP7luUhbBVClQgDkKDb7nbX97M_vV2Zg4FrYbWwK17h8ot_h8xAf77HM8WaRj6tZLD5RGczOd8gRHYV8mfG54_74vRJYh_RJQtBXE48O2bIftIjRcowFKubVS612MqKd2cCDehAkQfsaFSxMOUzaLdCol7hpzJ-vjgH36M-Gw4WUPqYhfIpBxKM2ebkbWdxAxn1EbCPykhQmWyVZzkLCAcu6dUY4o8r50CJvZrIL1YkUKIvWre0l2K1m-0yUmkW8LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام دوستان
👋
کلاینت Aether  در دو نسخه اندروید و ویندوز که به تازگی توسط کانال ما منتشر شد -دیگر توسط تیم whitedns بررسی امنیتی (audit) نخواهد شد و ما از این لحظه امنیت این کلاینت را تایید نمیکنیم
⚠️
لطفاً با مسئولیت خودتان از این کلاینت استفاده کنید و یا کلاً این کلاینت را حذف کنید
🗑
لینک نسخه اندروید و ویندوز در زیر این پیام برای شما قرار داده شده که بدانید در مورد کدام کلاینت حرف میزنیم
https://t.me/whitedns/1315
https://t.me/whitedns/1335
نکته:
کلاینت مشابهی که توسط Matin senpai انجام شده مشکلی ندارد و میتوانید با خیال راحت از آن استفاده کنید
✅
@whitedns</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/whitedns/1360" target="_blank">📅 04:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1359">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1359" target="_blank">📅 10:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1357">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/MIhYfjuE-rVZvtZ3NiuKs1puEfK2cfo75to-vEYe5vkeynAU6HcLziLh8kplhdeIFw3fof9oVejcLkwAvZ7skbKrIT3BgSfNZBkyraCKblKXcqM9jdb-UnPpEDjcuIfMj3_zp5gkW118T6seipY80Ad08JZJ-AGFzdif_jtDOGoL54HOGlOg5keMWfBCk0ZDf8JtHEO14pdOOhS2GMGIn1GXCOU6heR_fyns0iPAOkKZyl1wWWGTUQMY_9DqDdSlO5_aR-OljytXrX6V8nUHZSHygqLuqL7Q0YX_veQ_GPEXoBo4h5ZXNbl_pVeStjdiKpFUdRGf71bnaKYeDN1o4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/whitedns/1357" target="_blank">📅 04:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1356">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">خب با کمک دوست عزیزم Mr Arrow مشکل سرورلس (فرگمنت) هم تو نسخه
48
برطرف شد.
https://github.com/patterniha/Serverless-for-Iran
* نیازمند:
Xray-core >= 26.6.27
(v2rayNG >= 2.2.6)
* برای آپدیت کانفیگها کافیست سابسکریپشن را آپدیت کنید.
* نکات استفاده را حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1356" target="_blank">📅 02:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1355">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">3 سرور اهدای CottenDNS
لطفا تست کنید و نتیجه رو بهمون بگید ( کلیک کنید روش کپی میشه )
Server #1 thx to Araskhatare
♥️
Location: Germany
🇩🇪
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HqfCfh6ogdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Imdlcm1hbnkuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjI5ODQ0NDhjZDRkZTYxZjgiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
Server #2 thx to Araskhatare
♥️
Location: France
🇫🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-Hq_Cfh7cgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InBhcmlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI1MjViNjkwYjU4ZmU0MTI0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #3 thx to Araskhatare
♥️
Location: Israel
🇮🇱
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HrvCfh7EgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiIyMjRiOWU4MjVlMzFkNWY0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
@whitedns</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/whitedns/1355" target="_blank">📅 18:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1354">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS   cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcn…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/whitedns/1354" target="_blank">📅 13:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1353">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/whitedns/1353" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1348">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.6.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.8 MB</div>
</div>
<a href="https://t.me/whitedns/1348" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/whitedns/1348" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1347">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clLrzQLao0l_k0t5QXcam78naeAqGZVwfhON8aIkAniGi_FMg7ANxsN-FFB53F6qL8YrTsElsEqJJVlphQdUkg0n102jiyanwVDydFDI8EWycLPECTdMwgwv750-NMcxS9XlXiiXAUuEIcMn6lx7ZLU2rwGQAw0M5Bopvu0sTRAV3NIdZ8rAXhvf9QDG3UG4QRyMdXruLbrp1U04XRkbaPj0vsu_UddUPkI6997lGFLr_JCjMejhu_kXcLGwctSreZ9zB_EKncyerxXQiYHUv72jbYZSxFcDjxOUGcywKKdxUPDwnwRgyNKLCxw4e-Ltt54U1U2ALsFiNscEJiOWpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/whitedns/1347" target="_blank">📅 10:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1346">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🌎
دوستانی که با جزئیات فنی پروژه آشنا نیستند، به زبان ساده
CottenDNS نسخه‌ای کامل‌تر و پیشرفته‌تر از پروژه‌های MasterDNS و StormDNS
است.
تیم ما طی چند ماه گذشته، با استفاده از تجربه‌هایی که از قطعی و اختلال گسترده اینترنت به دست آوردیم، روی توسعه و بهبود این پروژه کار کرده است تا اتصال پایدارتر و سازگاری بیشتری با شرایط مختلف شبکه داشته باشد.
نسخه جدید اپلیکیشن
WhiteDNS
که تا ساعاتی دیگر منتشر می‌شود، از سرورهای CottenDNS پشتیبانی خواهد کرد.
هم‌زمان با انتشار نسخه جدید، یک سرور عمومی CottenDNS نیز در اختیار شما قرار می‌دهیم تا بتوانید بدون نیاز به راه‌اندازی سرور شخصی از آن استفاده کنید.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1346" target="_blank">📅 10:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1345">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚀
معرفی پروژه CottenDNS
https://github.com/WhiteDNS/CottenDNS
نسخه پایدار CottenDNS با تمرکز بر اتصال بهتر و پایدارتر در شبکه‌های دارای فیلترینگ، اختلال DNS، پکت‌لاس و تأخیر بالا منتشر شد.
در معماری جدید، سرور به‌صورت پویا با تنظیمات هر کاربر هماهنگ می‌شود. یعنی کاربران می‌توانند بدون تغییر کانفیگ سرور، روش انتقال داده، نوع رمزنگاری، MTU، فشرده‌سازی و قابلیت‌های بازیابی بسته‌های ازدست‌رفته را متناسب با کیفیت اینترنت خود انتخاب کنند.
مهم‌ترین قابلیت‌ها
🔹
سازگاری با شرایط مختلف شبکه
اتصال می‌تواند از طریق UDP و TCP روی پورت 53 و همچنین DoT و DoH انجام شود. اگر یک مسیر مسدود یا دچار اختلال شود، کلاینت می‌تواند از مسیر جایگزین استفاده کند.
🔹
مقاومت بیشتر در برابر پکت‌لاس
CottenDNS با استفاده از ارسال مجدد هوشمند بسته‌ها، Duplication و فناوری FEC تلاش می‌کند اطلاعات ازدست‌رفته را بازیابی کند. این قابلیت‌ها بر اساس وضعیت شبکه به‌صورت خودکار فعال یا غیرفعال می‌شوند تا سربار اضافی ایجاد نشود.
🔹
مدیریت هوشمند Resolverها
Resolverها از نظر سرعت، تأخیر، پکت‌لاس و سلامت بررسی می‌شوند. Resolverهای خراب به‌صورت خودکار کنار گذاشته شده و پس از بهبود دوباره وارد چرخه می‌شوند.
🔹
تنظیم خودکار MTU
کلاینت اندازه مناسب بسته‌ها را برای آپلود و دانلود پیدا می‌کند تا احتمال شکسته‌شدن یا ازدست‌رفتن بسته‌ها کاهش پیدا کند.
🔹
مقابله با DNS Poisoning
با استفاده از روش‌هایی مانند Transaction ID تصادفی، EDNS Cookie، تغییر شکل درخواست‌های DNS و ارسال از چند دامنه مختلف، مقاومت اتصال در برابر پاسخ‌های جعلی و دست‌کاری‌شده افزایش یافته است.
🔹
انتقال داده با فرمت‌های مختلف DNS
داده‌ها می‌توانند با رکوردهای TXT، CNAME، A، NULL و HTTPS/SVCB منتقل شوند. کلاینت می‌تواند بسته به محدودیت شبکه بین این روش‌ها جابه‌جا شود.
🔹
امنیت و رمزنگاری
روش‌های AES-GCM، ChaCha20، XOR و الگوریتم‌های قابل تنظیم پشتیبانی می‌شوند. نوع رمزنگاری هر کلاینت به‌صورت امن و مستقل شناسایی می‌شود.
🔹
سازگاری با نسخه‌های قبلی
کلاینت‌های جدید CottenDNS و کلاینت‌های قدیمی MasterDNS و StormDNS می‌توانند هم‌زمان به یک سرور متصل شوند. بنابراین کاربران قدیمی برای ادامه استفاده نیازی به تغییر فوری ندارند.
در مجموع، سرور CottenDNS امکانات مختلف را فراهم می‌کند و هر کلاینت بر اساس شرایط اینترنت خود، بهترین ترکیب اتصال را انتخاب می‌کند.
❤️
Thanks to
@masterdnsvpn
@WhiteDNS</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1345" target="_blank">📅 10:23 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
