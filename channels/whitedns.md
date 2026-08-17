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
<img src="https://cdn5.telesco.pe/file/mdDrQGvr8V8TJIlTsHxTStIj5mb2N2x-uSv05GyCv6isIjJjS3zKbLBAFg7p92cVWkJGfmoUrLItE6Ff8-Rd8vDJbFgxyBFYgqDHvST2IrVogIuhGoJLSnnQLjX36U_GkEBXiiK-uQcGI8N-0BpjFUhs1XApM2EppOjhJAQD-s0PIzQEQi_2Q_ukPx3bM3ddvfHUwlonUrEIRlOedolKUSpMAvLMlxGL5Y1J1zAlQBKVwjGC4zuRtvyMMZBTUPwzI0OKHK86_XdxZhmux4zej-cgYvHAxkebEUbWY-ZXzx2xPlDd6s2bIWUi9pwZC0p34PTfZ35dqf6-ljaWicA-RA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 20:22:01</div>
<hr>

<div class="tg-post" id="msg-1504">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سلام دوستان :
❤️
اینقدر درخواست برای IP ثابت برنامه های  whiteAesther و whitevpn اومده که دیدیم بهتر هست ، یک پست براتون بگذارم
در حال حاظر  این امکان توی آخرین ورژن های این دو برنامه وجود ندارد
اما ما دو نفر هستیم که داریم روش کار میکنیم و امیدواریم طی روزهای آینده به دستتون برسونیم ، یکم به ما وقت بدید و صبور باشید.
ببخشید که انجام درخواست های شما گاهی طول می‌کشه، چون ما هم مثل تک تک شما درگیر کار و زندگی و مسائل خودمون هستیم و گاهی وقت کم میاریم
ولی مطمئن باشید ما همه پیام های شما را می‌خونیم و تا جایی که بتونیم ترتیب اثر می‌دیم ،
ارادتمند و کوچیک تک تک شما عزیزان دل
ویسپر</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/whitedns/1504" target="_blank">📅 16:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1502">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚠️
موقت
به نظر میاد که دامنه
workers.dev
کلادفلر رفع فیلتر شده است</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1502" target="_blank">📅 19:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1501">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cu15FhfDZ90lD8VlO8YwMGmTISMXIOQh9R4PUnUf-SlZSDj0Mr_gF-pzMAlEk51fKfiCCDsR5lGaIfRlpit0eovP8DKp88zATCrz4yu3z7pI1tFwAI0bj4J71wtdKdr1w8kCDMaN4o76k4My92SlXCNDQYlxPpguak_XxJDQx7BHHi6YEUXRzbmw5dXgy_XGDw4iBtI2lhJKfiYm-WUsAx7uwTH3f7QRElYeKR4nor2UKKHydr4kltEeIr5XKST9nBRtN3iP-88gAELU3FCZMSs2FNGCD1GQX1vi2KLdAWdMCIg9Rdfh0Ftt6rnYaZmHFk0mmCBC1gJgXgOxs3XaCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1501" target="_blank">📅 15:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1496">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/TuXNnWW_WkVF_Gb7JgnZJ2qyk51zllsjqWyMunT2aRRc6gzJ5_J-KN1lzT0ZgtNvCZ6Rqqk-NDYUqBiey5OBbkEPuSWgaR6sydVaxzBrtaTkhjeCNH_PLh-Qap5GOjQR3Qgq3HMoY3-PyZTvZKQKAxPei-TElDB0JUotK4-B0JDwHIrxpuPWS4nF_1dEq0wzM1JabCrAI_U-OsjuUak11GVS6owR9rqTG6qahf_L5MaINHNJ0YbyQdKuFe7C3IuVdzWYXAvdcfVMGAPbvZ9VeTLuR5JipoBoF3lChbyLlnr4p7DKT2VtMiH6m_F0o3EHY5aBAUQFdyadeLORhA40aQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/whitedns/1496" target="_blank">📅 07:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1495">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RrgZvrR3WHt6bcTlLQHofckpURTNNA-L5h36sceMun0Ij45vMrv9Gt4_LDgpCz0agceYKVquBfqDIflB28CK2iXIdo3PWtuUMcXS9f8MXUPwp06FLp2PVYRFtGFXsixQyka4OR9ytG5HUWKg6f2xT-vaxxb_yT3Pf9-BdjW4OrDnu_O0xnKApn0DKb1Tdh8Hrm3FimugQ3764flQkHpyNuKQLig0IhmNwTn81dmLY3kAqBjtbv8OcQTvUKjCuFY2A1ugoq7QA2SFFtpQeOgszpPiKK7m0YAWhg_HJrqRkKt3FUJE6kYH0KWnlLo3YdOIMJR8Fo3f7OW0vtfpuaSebQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/whitedns/1495" target="_blank">📅 07:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1493">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IAJu72Ao_GKVSjkYECX5amRejsfgUjrQViMc5vIJaVp9rl6wVntBwYvuFTFFoSxhthMdw5FpUycGY6qBwlrJRDSCB3bSWEwJNwNZmZae1RH4KYzuMrBKLxYLPeBnWnI60NJt7246bOo3p7EOlHKLCfZRSZP5jd2Z47pTnHW87kfKeLtHuEwMGepWzPBULJhpjYwTHBkRVl7rWPt7mDLKQanFIoSp0EI5_M82QOQX2XNQWzBWegNKxqer7WJKych_Sml_hQSqCksUM1CU6eaYUy-VEh66BifxPoG-hL56hTM61i7wvNZyf83BYK3U0RjxYF_S1b7s-Zy_0qR32m6omA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام :
برای حل این مشکل توی ورژن دسکتاپ و مبایل whitevpn لطفا ساب زیر را دستی وارد کنید
اگر به هر دلیلی ساب برای شما اپدیت نمیشه اول یک فیلترشکن روشن کنید که ساب را بتونید بگیرید و اپدیت کنید بعد استفاده کنید
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
@whitedns</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/whitedns/1493" target="_blank">📅 05:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1491">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/whitedns/1491" target="_blank">📅 22:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1489">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWnI4JFFahZAGClQlVEzBbVGMS7r1MuYY6U0UXSNNpLEZrVbCWdVdjlIwM4HX8u8pJGmSs2xkkOGEnM40AlhiPj6d79zEskyRyXCXlJwDy8X--xIVpmeTmzU8FVrYiz9dF5Ew6LOHwvonEd1FOaHIqIPmXN6b21ua9bY3jsgtj_zLokF6bIf_MqsUcnWa7XRLJM8_K8wWJOlXmXBZacGv82MxwgboBBYHiwtic4Nu1VeQxy_kk3r3hgYkg94ytFYDGt1ssL3kqkD9ClB1lBeSZ9phPtS6NDWvY1ppSWZILQ0Atyqmmxx2mk1vZpVmFjSyYxptyz2gYs_tIajDU5Scg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟   میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro و باقی Wireguard ها وصل بشید.  این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1489" target="_blank">📅 21:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1488">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cP4udT3_O3il7qU9xzzi6mIpSgclhNhs4Ased6KFi7bcPeUslh_Xpp6LFtLq9hTjsz0IC9DI11lhQtLY1-95QJFF1UFZue3uOEFsnX6lAhE6o9vLtmIQJn8HsDQ54RP20qzCxKoO-ltAI0KO9O4SQFz9gSnxUXB2MjEqdsNjicVOvlxNbumX64Pb4MUSFp9dWQ4KN5em7C0E1YmXXa1KVBjkgPq9jmxyjlbMMJqZScbgtcvpWkMdXkHf8-mscgtW6qw7U438_2y9Vztoz2Vpj5CtqBFIPJsTBfPGoJOxgLoXBUYaSZyFwmaq8QjXAd8paddsgXIzFosrphSvjo2Urw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro و باقی Wireguard ها وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN
لینک ساب Mihomo رو داخل WhiteVPN وارد کنید.</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/whitedns/1488" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1487">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=tW5rLGxzDitkwPwNnoNXqR03pwNurRZLmVxgqWKlmgYT8ChMmjYuuQ5dlH7Bs5aDYYApriBvjV_5CMhlFNKrPCJ_E13YhEnSE2hPmurvS_eosTYFnYa2QQOaUU5iJf1zzzhFFHJWQdxrVJbg_GxtWyhr94oyR047aBrVhJWCqxRnn1qNWL2EHVjl4NbHXvZVIOtpVR6u8ICnTxbU4yYjWz-sBZThGonlUiMXhrPs-ik2Sf68P0MSgkGPC90kSlf907Hu1fIYiTyixQO6yfaVzopTOPndUpxdEDagkrMzBipOo0x4wgdlGdBjHcK10os9egHFGah4xnjHZMZ1w7Z9Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=tW5rLGxzDitkwPwNnoNXqR03pwNurRZLmVxgqWKlmgYT8ChMmjYuuQ5dlH7Bs5aDYYApriBvjV_5CMhlFNKrPCJ_E13YhEnSE2hPmurvS_eosTYFnYa2QQOaUU5iJf1zzzhFFHJWQdxrVJbg_GxtWyhr94oyR047aBrVhJWCqxRnn1qNWL2EHVjl4NbHXvZVIOtpVR6u8ICnTxbU4yYjWz-sBZThGonlUiMXhrPs-ik2Sf68P0MSgkGPC90kSlf907Hu1fIYiTyixQO6yfaVzopTOPndUpxdEDagkrMzBipOo0x4wgdlGdBjHcK10os9egHFGah4xnjHZMZ1w7Z9Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/whitedns/1487" target="_blank">📅 19:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1486">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/whitedns/1486" target="_blank">📅 19:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1481">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/whitedns/1481" target="_blank">📅 19:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1480">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bsf8snbafA7rtLBWDUF0O-PiAN4ABws3OfLbXb_Kk6sNhKG002ApFd_IMOLZBYESPWywNjEhOzvxVTOKNiB5vOyh2e3_KIne56SucWungy8n8WwVyyqF7QMYHEJQS0UJ4XZV2FcD9ozYQtmOxKwfTxXkaflm3KTiLitntr32Lh4JwDbX2cUKSy7CAzzGdbQYYZyVtwuGPn_EzdFWQYiFAanPrrZRWP5aovk5gHRfjcEH48NqrQyfGZohHbUaP1HXTzlKSU8CDDJOANGUFHJLb0Z91ZTSmAJLMpMQb4DDW3lmNO_Xh52KBabfJRLEQfgQOxpd_xlIT7M6Xxa5KNVZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/whitedns/1480" target="_blank">📅 19:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1478">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Y1HK9WEWueBeYIm3WgRVQRf21QPYwm6lQEO05SqSNnxb4gVHbjc8DMKybMnlxBdxIc5sv4Rp2onytBXkOYhVe-EYM4nYkSCFTMQ1QXSY-0l-IFFSLptQhrlJxEZ16lhxDDxXiq-n7s2ZsrlFoIX2fr-OrmG7QPIkNCUk2s8QDUjdiekDjJTO3KW3EgiHROMSPeHBF9ijEw5ndsTZBm-_yLUT4IZAGPz0iVBz4GY3EQC4BwRxizBD16ITQDtJhjuyyPXzINHpqJdcZ19BrkO_w-Q2BDrjKpZv4B3oitViEnxjvnxrPWKGzAKy9vMgQne0uIO5AiNigQJCOOtcAxmRWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1478" target="_blank">📅 18:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1477">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوستان عزیز سلام
مثل اینکه آدرس های ورکر کلادفلر فیلتر شدن. و آدرس ساب اپلیکیشن ما داخل ورکر ها هستش. تا آپدیت بعدی، میتونید ساب مارو از لینک زیر وارد اپ WhiteVPN بکنید
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1477" target="_blank">📅 16:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1476">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/vvjBFo9EiASHl8m8f_26Id1OpXDpFgj4AwXevtnAfIqLjJN67NHNBVgyVnujeQClUYVikDcW7Q61ZbBleaUxx-xxwEk1Kfyk797Q6gAGBNSD6EsyafHRFe5ffLr1PJSwxCcBTex_Cof5nCF7dpu2KVjk4oCpavAN1AZo56zgH_I04zFURixZ6drxuMoq83qZe3ClQl3uMCbDcGkPr2znxT8pkItZT7VxeQPlClWPDXqxmTyc4ww_4XisPgl2iFSiqt7WMuuQot-4iOvlrKALlftQ8yDTfbjsuEi5kcxVJKFsUj8nNXRdwSfDgsJf5Q3OxfR2EJU6O9YcJVfa6whJtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/whitedns/1476" target="_blank">📅 13:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1474">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XC5mnO6G1ORi1VmQmJOCBSJjaXka8rNF7sx2JlmN_NX5FaKyoS8my-G2RcZjcjhj2rudLJ1dmNdays86CSAU4icvUyucRNiH9yn_oobk8YGE0JywJCYc2Oions8BQf4x1i9Pmf8ALIBNruXLoB_INxCoT4DSfmhuZCFtv3ur9Lp5Ayggtj97TGa8sLSZj6IrxSZEBNdhCyGUTyI-tvMxrMRtrpro-E7vPG4W6x7wKR4UdcSajtNgsG1yEEHMUsfg4bEYIZbXgLj2lMkJlGLs_2Sy__OwwfmTRKSTbUEAWUQbamS5SjWZks2DM3WW9klwQyi4W8O7BkpFzcxf2BtDdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1474" target="_blank">📅 02:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1473">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VH60t4nIu5P1wSKmlUfCvu8tp_08IFLeclEOEyxEU8pm-xbEHLACXN27oCJ3ErGchqP7hXcUbDWXbI7hJ8qM7yPd1LXIpBn-nwFnMK508dF8m6WR-6h89J7Zx1kAc9JOHafsRRGFcpezQdUs_89PDBbIL1oiOyumtTAP13_A49ht6dT46xXS9fi9wpRMK4DZlPaM-JyVw81kxFCMZWgzHf7q9qDNGfKNwOOi2QRVD30UP0CLalLL54OXL6lEYu9RUg8tI6G9-Lj0p-lTtvFyQTb0HR__wENyKFKrwfOf_g5NzQz77nGthUonHuXrJqQFP8WTc_RQYaisKW_J_0Twog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏯️
آموزش ساخت کانفیگ V2Ray با سرور رایگان!   توی این آموزش با استفاده از Wasmer یه سرور رایگان می‌سازیم و در نهایت بدون نیاز به خرید سرور، ۳ تا کانفیگ V2Ray برای مصرف شخصی دریافت می‌کنیم.
⚡️
⏯️
تماشا در یوتیوب  https://youtu.be/EAjOhvuMw8Q</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1473" target="_blank">📅 21:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1472">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⏯️
آموزش ساخت کانفیگ V2Ray با سرور رایگان!
توی این آموزش با استفاده از Wasmer یه سرور رایگان می‌سازیم و در نهایت بدون نیاز به خرید سرور، ۳ تا کانفیگ V2Ray برای مصرف شخصی دریافت می‌کنیم.
⚡️
⏯️
تماشا در یوتیوب
https://youtu.be/EAjOhvuMw8Q</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1472" target="_blank">📅 21:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1471">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/T9IDjxAMT_2QoK4Ta-DiWE_Hh1q1KszmWwcUnnq1oQJNN-5LZphP9begDowlF1Jg5GNyACSZGnSFsBoZV99xWzvYJJhQlJ7X2dEuv_RzDn9PO2Y1AtBnH1IE-faT7kJkagpBERUuJO_TZwzGWFe5sc6Zj-K7gXSNI5RN0t9-Vf3kXo76yO0a-yUeWHbLm_QwlXXM4SPCfvSsdUgkd7KDSiplVPKaUj01ihexGL_W6DKHClORqYiClvqSuGVrCIB8VcpanU0xeMS1_nLwSXF_MoHdK3IuVA2YlfVsZ9z_Gv5KB_N2NC0JcFYhf-xATHT7yfo-gGJpHPEb9RRhzelymw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/whitedns/1471" target="_blank">📅 18:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1470">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1470" target="_blank">📅 15:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1468">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RcNmAAsX9ucffooRftTZZhqAp6VZjbcQcaRm_faXP1YfuHtBrbyuyEPZYY9ZQvZTPEjuttnCLOm-AZDj-eALja21i1aZ5AmkbvA6aZsxjabvrzq7y6uL0h0k7bPktAT5_Z7xd5CsmJmkKWPUAtzE2dKyf_BltZBKlA9yV5QgJZhqTL_zmoDyqPEWKQSuvq7eoRGkjf1FAu1o1fanhHLQO9KkzX2PYeQcvxzRdoNIrcmIlJCXwl-Jz_1r4CG5rdRLb22s33YugrgyLdOGJPHXGiLg9wMeiSSnsWhP6J0FmPwvAQqAl9cxek_guIhQ_in8T5NTVMS8i8NaYK7MoA1WCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1468" target="_blank">📅 11:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1467">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GGa0VTqKCUTciVe_PjW-SXtz_QU8seYZgngsh_Xwf9UlKsHOUAaPOtL26yWUJ4cSziney32n5mk7CZK-TC_Z_dWgySmZ-kqvy_34jM87Dz16IHcI3o6npGg-W60hBStI18zvtHndqxcTKiR7Fw4pinP2ienUPjxsjvQyBHbCSYHOPbwpBiyrKSiBAl-X_ltmBWP3kyzkgqK1aBLs26Z6-hZwb63RdyahlHU3WYfp2Q1Q7Xhl2fQqDUVabpdNar8Q7T3v7g78f88-pQ3NbWZoEGJdYkC1dKXcxCxzlI_QFWMEgYyyon3Fpu6CRRNsdGdr5KF5_jRdI5N-3JVoODmfJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Coming soon............
WhithAester desktop
😍</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/whitedns/1467" target="_blank">📅 09:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1466">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌎
پروژه WhiteVPN رو اوپن‌سورس کردیم و در گیتهاب میتونید بهش دسترسی داشته باشید.   https://github.com/WhiteDNS/WhiteVPN  همراه با پابلیک شدن پروژه، نسخه ۱.۳.۱ هم ریلیز کردیم
⛏
در این نسخه امکان • آپدیت اتوماتیک اپ  بعد از یک ورژن جدید • امکان routing برای…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/whitedns/1466" target="_blank">📅 09:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1464">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌎
انتشار نسخه ۱.۳.۱ اپلیکیشن WhiteVPN
پست قبلی پاک شد. یک آپدیت کوچیک داشتیم به ورژن ۱.۳.۱
😆
از این به بعد آپدیت هارو اتوماتیک از داخل اپ میتونید بگرید</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1464" target="_blank">📅 08:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1459">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.3.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/1459" target="_blank">📅 08:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1458">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_HkKLffIGAqcBM8htQVqFX2V5aamxSBtvsdJGr7Ks6TFGICGdlEIprEyERRwOty6dSOVxE6Nj7_TR_6Y3VqJ5L_LtDq2JJT7wFxwCQejrytgaFS8qsyAPIUOjhXYrXsAHNUrDjSoGeSJQpmLUkyv-zflFfvJV-CBOp4cwnQv_M2STHI4-34VGxhEiBa8KWm0AESVAScGXZdY72SGK_7z2t1dUyPNXDMCwkKf-O-pN39TgI07TddwlBAPXzykvSLtVlJ4-zV29cniWUVhMxaj257dJ8iyrvycr6P63SLg8RvQSrukrDpTE2IUKjIFuKU4liQ2v-Hq9qUSpGHE5jW_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1458" target="_blank">📅 08:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1449">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/S-bxxk9dGOic7epEvdQQq4L6WiyZ6EvZrPCIQPHgIEDOhysRdsITZxQ-U3GkWhmU-x2hkhfpPkZ_A3TLG9Y_WWvGv788btol1jBnleN8iSqpo4aichp11tSCgrwobNpUT6DTRI1NrF2djXSW14mtCiLjJa0AZpcDQttVoaKPKYLE4Qwv9taCEY6_vDoMYFHWjSeQZQyOtLU2xgH0-L-QsLJFBHctVEwfacn2Q7kE28dLbhC9cv0t0WfZNonCZ822w6P3D1185kXrm-6t7lH13w4FnwPTJiF1SAPBYcpFgYVOBl21uSzWMW0SQQuZCJVHq9BV9R8iy_QDAQEXjdkGaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1449" target="_blank">📅 11:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1448">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/whitedns/1448" target="_blank">📅 11:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1447">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sb13nZrvgRYCrLqPp_hYYubvXuNFUTfu_z1TwOjHsecDQTHoi_gr6bHU_iM2rvI_ATDor-pXcxL1ddGPDaeanZtfVSff8LUgsk2QaGIPQg1DIkl6B14NFl5PtMjjCFZ3GVpDYJVJj2sufAdTBbRE9StuXA-gEZZebsTV1buc1QO-ZxXxH-dgIwypCizGinlW1jE9OwvRuQ-blYoSMYAt2MJr4DgO6Gz54OsgfaNT4I3kG1xfhdBGVZyqcV16x13jTeF0VngkXv_v1DbD0eZTXBXP7df4MNXYPTP8ZEBfLgxziKkFITiu2ISY0Rkwz37C8jx-QYyHGrOErzGRV02kQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1447" target="_blank">📅 09:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1446">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1446" target="_blank">📅 09:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1444">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1444" target="_blank">📅 07:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1443">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1443" target="_blank">📅 16:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1440">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1440" target="_blank">📅 13:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1438">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1438" target="_blank">📅 12:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1437">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-poll">
<h4>📊 با whitevpn desktop وصل هستید ؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1437" target="_blank">📅 11:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1436">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/whitedns/1436" target="_blank">📅 03:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1433">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی  این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/whitedns/1433" target="_blank">📅 20:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1432">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=A6PzlIpVtmZSLOJY-pXXjnqiMFaWkpYsESqcFAgwPEyT4aDACwkx4iou0wWry5VLUEcb25_oU2qgrUlhh99sxfwYUZph6YB7boI3i1B_vDCfbC5HQNck5Ood-c4OeWYdIr6mBCCcTrh917x_axzryuGuaPSITupNHz8msYghXvr5UmGtcVyKlPF7vgjkk_k4GQIXlqZa_i_oAYQ328N5YUt-1mRgLyaj9fsjEPChSNtGTxpqIPWBd--AVykCdptQXfTSw4C1bwwgEyzGN2SmSCh7dR7mrfGlBOZsa5RcWQugWo2tTrjdplhYQ2q9l_5qqlJPgL9ujP9OQR0xyij3Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=A6PzlIpVtmZSLOJY-pXXjnqiMFaWkpYsESqcFAgwPEyT4aDACwkx4iou0wWry5VLUEcb25_oU2qgrUlhh99sxfwYUZph6YB7boI3i1B_vDCfbC5HQNck5Ood-c4OeWYdIr6mBCCcTrh917x_axzryuGuaPSITupNHz8msYghXvr5UmGtcVyKlPF7vgjkk_k4GQIXlqZa_i_oAYQ328N5YUt-1mRgLyaj9fsjEPChSNtGTxpqIPWBd--AVykCdptQXfTSw4C1bwwgEyzGN2SmSCh7dR7mrfGlBOZsa5RcWQugWo2tTrjdplhYQ2q9l_5qqlJPgL9ujP9OQR0xyij3Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/whitedns/1432" target="_blank">📅 19:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1431">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/whitedns/1431" target="_blank">📅 16:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1430">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">White DNS
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1430" target="_blank">📅 12:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1428">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">White DNS
pinned «
دوستان عزیز،  در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1428" target="_blank">📅 12:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1427">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/whitedns/1427" target="_blank">📅 12:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1426">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/whitedns/1426" target="_blank">📅 08:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1424">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/whitedns/1424" target="_blank">📅 10:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1423">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/E4o1dGrIwzPsugVIffzqgt_mQvOL4ciXoPNgyflw_9fI5sHDvd0RULvP7TKCuEYAMYeFcG6eHm8HHYblMX5jh0Y7mLlF5kiDCRxGS8jeU1CfgJao5UTabTfY0-T14M9u299Kbl_FAgCWOOCV9ISdqSGWWgu6O_jdst07vqTyM8z3O4UuamYOKGchOYQnWP-r-M3eAAusDzY6X6DCX-Ynlg7-icyKohJewM1SrOiUczqVcONUMzehhjBteiQpBYKRN_Xni_7iGtVB8fIZgRhnfNm0CNyogAX-tiQH2ZFtLNC-oJhnQX_5EsZdN5Wlb1wPgJLt1rGlREe0zuHYS6bkoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/whitedns/1423" target="_blank">📅 19:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1422">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/1422" target="_blank">📅 14:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1420">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=E0iVK6c8_X4cgX7PlmEeAZ8YcLH8eKGEQFlHvl4DFprJAIGjmko2oK52dpusKdISYWU30ig7XdzP_mdZt7paNOAYk-k7peAd1HsKuZjizBxcs_Xqj1hUD7N-7eYYq7vJVsZZ9c4iOtHqA9KFoeNOHmE04WmPHAdWyON29-08nJ4bjsnTjchFiRY-FZ6OjLiFxG0zsUukd_rAT3KLVU5WKKQ1qh_Rrz4qUOd8dHcKILylfR0JhaRT2JEX_yHHGxIxOennuo5PH2lAVlpeQnmde1ED-D7gCTjcETYhqSlAXBOgyfCF5qysDxFsYZqsIAJ6Jp39oa3TgpE7ATb3zy01hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=E0iVK6c8_X4cgX7PlmEeAZ8YcLH8eKGEQFlHvl4DFprJAIGjmko2oK52dpusKdISYWU30ig7XdzP_mdZt7paNOAYk-k7peAd1HsKuZjizBxcs_Xqj1hUD7N-7eYYq7vJVsZZ9c4iOtHqA9KFoeNOHmE04WmPHAdWyON29-08nJ4bjsnTjchFiRY-FZ6OjLiFxG0zsUukd_rAT3KLVU5WKKQ1qh_Rrz4qUOd8dHcKILylfR0JhaRT2JEX_yHHGxIxOennuo5PH2lAVlpeQnmde1ED-D7gCTjcETYhqSlAXBOgyfCF5qysDxFsYZqsIAJ6Jp39oa3TgpE7ATb3zy01hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/whitedns/1420" target="_blank">📅 11:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1419">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/whitedns/1419" target="_blank">📅 05:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1418">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=UfKkzNWv9Syx4Ot8Bqmw57uOacYCN1-dy41TVkxc-k6sQnN13p_byMPDZrwvVhKVhaVeSd2A2J0ziXKLwNJWOV668y8KHQFUc2RlvdVSq6n896zwPeQUvQoJxs1Lgm3wN5ioepb-MQKdl_1BEth9_yPuLxmFX1HvtX6NFkgaGRPKKN-InDdV4T5pe-9jgeiSgiy0Xe0AH2qcYwVCPT3FQkNEJMQsSaFcmre8dCo1K28awIisQ78R0qL0XMONVwLgcQ4q1mkKM9HRCYMvgrpyQt6x_SIbok_CzRQntZeQbEQUanpzuo8IcMalPN1CBipHuZcJAohd6vyj3kGcaXNq4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=UfKkzNWv9Syx4Ot8Bqmw57uOacYCN1-dy41TVkxc-k6sQnN13p_byMPDZrwvVhKVhaVeSd2A2J0ziXKLwNJWOV668y8KHQFUc2RlvdVSq6n896zwPeQUvQoJxs1Lgm3wN5ioepb-MQKdl_1BEth9_yPuLxmFX1HvtX6NFkgaGRPKKN-InDdV4T5pe-9jgeiSgiy0Xe0AH2qcYwVCPT3FQkNEJMQsSaFcmre8dCo1K28awIisQ78R0qL0XMONVwLgcQ4q1mkKM9HRCYMvgrpyQt6x_SIbok_CzRQntZeQbEQUanpzuo8IcMalPN1CBipHuZcJAohd6vyj3kGcaXNq4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/whitedns/1418" target="_blank">📅 01:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1416">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/whitedns/1416" target="_blank">📅 19:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1415">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ROdNDr7E6-ZTGpdVMTLcUBgCecCgwEVneg70YFJLScGCfaW8CtMSZ_jz1ZczzInzk2McmIuwtPw9wc-wBCWMYVXzvpRUEmRuX8Lmdih-LFwiHRkLDlIOggyAXYUrhsPVZ8ZA7pC8sJek4oqMqn6cyv53Doa1jvOCI43DgpQ6759StyLg6-nLBb0th0g_PynfJCyzRDIZEb-EBO9XmRMtHHNHC4mwhlFXLff66F6Zuu-wRV_xynOQ-1mlnqmaaUCp_IlaLtvf1JiAfFKcSL29kCsI2R1lVDLJbWumUvE_Os_EuRgWxEuXx1RsMmuFnGv4JoFmMOAX8S8ixJbrLRzzVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/whitedns/1415" target="_blank">📅 15:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1414">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌎
نسخه‌ی دسکتاپ WhiteDns منتشر شد!
📤</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1414" target="_blank">📅 11:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1413">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/whitedns/1413" target="_blank">📅 11:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1412">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🌎
نسخه‌ی دسکتاپ WhiteVPN منتشر شد!
📤</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1412" target="_blank">📅 09:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1410">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmEVUPglxybXpsXrQQpLFRdUuZFMbSrEhSq6B-RlmJL7rEp9g-n7k_VQTGrgB-uqFy5S8M66EW7WL7AAuGfxBP1Yb5Vgfz38Alu4HeShra120odgT0SuGU_AAFVXRNUPW34Wjjcqa5BOr5SCdGOZWIh2CgrXpVAIsRTLrABGLX_NfSlRMM1wgT1P1ej9plof5wV1i_pixPBxUhjAHSEaHRTe8hT7T1OFEhW6xxUOc7W9tPIpHiiJUvdGgACxi-pCO4j25X4uExqH2z9mJNb_IvxmL7CTE27YbCjiFwX43JzqKXVJ6QcDn969H2QC2U1oHs-scxaT52ddXN4cOlYR2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/whitedns/1410" target="_blank">📅 09:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1409">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/whitedns/1409" target="_blank">📅 04:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1407">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/3ae84e81b7.mp4?token=bMbFpZ6FiOiauc2oJLMq6Lzk1ywTTmUZJEjFAh_qQKwlK526PioaxfMuqmMMedmIZq_ODWFF26U_55AaA--GQVtoeLz-CXZ6ZpL8beXYi_i-hT0c4fOOBBQK_EKBvODnFZP9VuL9Qc6Bfgx8C_XdZNaWeQpIBwAOV84MgEDa3AyKHBU9f80kLYVUn2hYF9YaCSKPw1tVg5O3MJbe9_F6LUbTfSs-Ea2C9spwRUZ0lLvlx0rEgOjs1Yo24F2zkPZTPYWNMInNJ31N8VHkn__6VTKswbRKfdrvYCJ5yIJnnNoOnolWWgwSxBIz7CIt81Zs3QX4NEoZOgCIWMfjig8Big" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/3ae84e81b7.mp4?token=bMbFpZ6FiOiauc2oJLMq6Lzk1ywTTmUZJEjFAh_qQKwlK526PioaxfMuqmMMedmIZq_ODWFF26U_55AaA--GQVtoeLz-CXZ6ZpL8beXYi_i-hT0c4fOOBBQK_EKBvODnFZP9VuL9Qc6Bfgx8C_XdZNaWeQpIBwAOV84MgEDa3AyKHBU9f80kLYVUn2hYF9YaCSKPw1tVg5O3MJbe9_F6LUbTfSs-Ea2C9spwRUZ0lLvlx0rEgOjs1Yo24F2zkPZTPYWNMInNJ31N8VHkn__6VTKswbRKfdrvYCJ5yIJnnNoOnolWWgwSxBIz7CIt81Zs3QX4NEoZOgCIWMfjig8Big" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1407" target="_blank">📅 19:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1403">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1403" target="_blank">📅 15:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1402">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال  سریع‌تر و پایدارتر بوده است.  امکانات و بهبودهای جدید: •  شروع اتصال سریع‌تر •  انتخاب هوشمند بهترین سرور •  جابه‌جایی خودکار در صورت اختلال سرور •  کاهش خطا و نیاز به چندبار زدن دکمه اتصال •  بهبود Real…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/whitedns/1402" target="_blank">📅 15:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1401">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/whitedns/1401" target="_blank">📅 16:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1398">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/whitedns/1398" target="_blank">📅 12:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1397">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc0b81933.mp4?token=ARjhloJNuTHO7n3vCDJPV90uTL9kTSr7KhWTAdjJBR1opSx4GSlrAMZ0vfTfLtZWHiG2xVeAblFIanIgxSNngHHNXXxHnUPQFPYnWbv7lGe0Wc2ClWecd_xjU6Z3i6b8WGUrj0M0_r2VogJQYCW-CVRfPEhggntHNn61GPT4X9aWuA1Eg244SCWTmwjyzpdqhINv_DUbuu6UuKWrxvsjvAZr18smMI4zvcBXTKezLATOFDz38NXkgAKo2fRTUfpaANvgjEFnIg0GRd8nYKcNZKTTvdjaa1hPEZ4ro6H8x-SZ3abbMDz9xoihyRrjYxWJ69grumAKzzz5QJRxEAN3dUkUtRscJOmXhw81WvfncqIKcc_vxG8gUeKKRDjpJsA0QNYHwZfKatxon0MQwaDQWqoQdr_c8-_n7QQm0E-Y8t5HheqzKyGEI33w-f9xTxb2Y7vXh74e2ULKB5KWR3b8N03PioMpnFdCn5VuaLE3cRdXfRhDA8ZmGyJLtSDOHDe131IQihNAHqS_TiiPzZh67pNd6o4ehSpJsJ_LBE-EF2K1ZaLoPuRQRmPSlfNF7L2TNrcoDMVFvQ2yGbzTGXuq3RnhGe_7M4ZddcOTcW3lRWBB8FrTvFpxIQGLQTqxeAGByUyLDU1cS6AXPARjVA48gjxu-LL9J9nOsos42Ld9IlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc0b81933.mp4?token=ARjhloJNuTHO7n3vCDJPV90uTL9kTSr7KhWTAdjJBR1opSx4GSlrAMZ0vfTfLtZWHiG2xVeAblFIanIgxSNngHHNXXxHnUPQFPYnWbv7lGe0Wc2ClWecd_xjU6Z3i6b8WGUrj0M0_r2VogJQYCW-CVRfPEhggntHNn61GPT4X9aWuA1Eg244SCWTmwjyzpdqhINv_DUbuu6UuKWrxvsjvAZr18smMI4zvcBXTKezLATOFDz38NXkgAKo2fRTUfpaANvgjEFnIg0GRd8nYKcNZKTTvdjaa1hPEZ4ro6H8x-SZ3abbMDz9xoihyRrjYxWJ69grumAKzzz5QJRxEAN3dUkUtRscJOmXhw81WvfncqIKcc_vxG8gUeKKRDjpJsA0QNYHwZfKatxon0MQwaDQWqoQdr_c8-_n7QQm0E-Y8t5HheqzKyGEI33w-f9xTxb2Y7vXh74e2ULKB5KWR3b8N03PioMpnFdCn5VuaLE3cRdXfRhDA8ZmGyJLtSDOHDe131IQihNAHqS_TiiPzZh67pNd6o4ehSpJsJ_LBE-EF2K1ZaLoPuRQRmPSlfNF7L2TNrcoDMVFvQ2yGbzTGXuq3RnhGe_7M4ZddcOTcW3lRWBB8FrTvFpxIQGLQTqxeAGByUyLDU1cS6AXPARjVA48gjxu-LL9J9nOsos42Ld9IlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش دریافت دامنه رایگان و نامحدود
دیگه لازم نیست برای کانفیگ های شخصیتون دامنه بخرید.
https://youtu.be/Tiods_aCJX8
@WhiteDNS</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/whitedns/1397" target="_blank">📅 11:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1395">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوستان عزیز،
در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.
🔗
https://www.youtube.com/@WhiteDNS
ممنون از همراهی همیشگی شما
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/whitedns/1395" target="_blank">📅 10:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1394">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/whitedns/1394" target="_blank">📅 08:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1393">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
لطفا تست کنید و نتیجه رو با ما به اشتراک بگذارید.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/1393" target="_blank">📅 07:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1388">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/whitedns/1388" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/whitedns/1388" target="_blank">📅 07:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1387">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqZGm160Wi_57DwDrhqYb6QwSyGJ70hkl52aFijVehFn___yPe5i6ClbUtLnTliu0x8le-Ih49GTOAMpUUsU4dJFoyZSK0EBUDv1uithIefPEhGCR6ovON3GuSj2QgkfaVY5t21JFme_sKDVFBUGefSiTnVCi_3ltDPRQhBB-gut6P6lZpy7znMDklViD5hw1y7HMpEM_LGMVIjtaGULTebVt_hBifnmv3hX9XSwwbRkLXxc-gq2DtyKhHyruiOr1nb-SgbRe0tMw3Lf4SdBKEO9WdciFpZ-blY3aR02HuEEa8hfS9HaCOP150D6KieX6vPlkxkgzUlGfVcrsfWYgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/whitedns/1387" target="_blank">📅 07:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1386">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⛏
اگر در اتصال به WhiteVPN مشکل خوردید مراحل زیر را اجرا کنید
۱. به صفحه تنظیات برید
۲. از گرینه حریم خصوصی DNS گرینه DOH را انتخاب کنید
۳. مقدار زیر را جاگزین کنید
https://doh.whitedns.workers.dev/dns-query</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/whitedns/1386" target="_blank">📅 17:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1378">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIwkNrIEyfelgyWKDw4-bG_QvoXCujtxO9DfWRx59F2MWfuGLTIdUS-_Ew3ceqeP_OFjhw6Fqo-w_WNAa73cX2aM6kHcw5VXf6HNvAIPA3t524o_rMhj_3uv9hRdK3xWlN-5AvPuVhhnK4EQ6EtAW38nkrvvel97GqA2ORku0XtzwQEeqMGghTZXMieGTCJ2_89eiX7iFqaBwX7vEoNJq3oCpzM8wo9VIrrjcAXLbKjam5STNmp_fEu0rEx6FUjt_164hgLT_CyxzaHgB7i9U4dmFMo_K5q2_X3DgzMJiozJOivr605pWF38zGTtHot80qmZZeKdf2DDB6vpS1jnjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/whitedns/1378" target="_blank">📅 11:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1377">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLmjNOWMFq5-xji_gt906kymXtqUSbooiVCsoXlYWlJ3LrMRNnwCdWki0K5LDYAh_YbWftyiBH9EcuD2gr9XnebFwrR0_GCiza2x3L4IdQXq2FAbGSReFAeM6HJM2McrQDW8ZOTClf1uKYiiYkDCx-YT52tpGi4FFB6zCoiuJSS_o69x7_xn5MynonlVZm7hJ0GwN1vlgpfXU2UMEO1LfS4cYjptCr9xWHzAiKvsmdT4SlJ__r29ZkJuq-YJpHk0f3ial11MzNHVFLfLH6NBMl39Jaf8vL3dEM3ys4T6KciPaXiJr8frjxUmLTZBfXr0mJ9c7dykcyRj0q8Zg36aLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/whitedns/1377" target="_blank">📅 04:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1375">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/1375" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1374">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور   https://youtu.be/epG70Xl1xGI   @WhiteDNS</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/whitedns/1374" target="_blank">📅 11:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1373">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=suvsjUYWolAIroFt0cDE2w3NdyIDuch5Or75Dse5y8f5-ljwfN2TcUsVMfDHFlsx3HLZEtBi9pIy47zLetQFDPveuztbINRS8b1gRgskly4Zci_KNWG3fatm3WaLbRpDqtiUzoScynF4BMUA1NzhkEGhZKhATTp6ytKLPypSTnZvQlgXDgHshb84caTRBdfym_ij0jFn_ibfL30h7-dUn53NRNifVFXecl1i7TF6ZMJP-GcrNdiUQsdM0NGaJJ1Q3OO3_Sk7YxExGt6xtb7HzEY2SyrLXYyPUe0tLalYIT22TKqdzOIKGwIu5qpDzrzEf_P4LCXrp8q3mCUGGdrCn4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=suvsjUYWolAIroFt0cDE2w3NdyIDuch5Or75Dse5y8f5-ljwfN2TcUsVMfDHFlsx3HLZEtBi9pIy47zLetQFDPveuztbINRS8b1gRgskly4Zci_KNWG3fatm3WaLbRpDqtiUzoScynF4BMUA1NzhkEGhZKhATTp6ytKLPypSTnZvQlgXDgHshb84caTRBdfym_ij0jFn_ibfL30h7-dUn53NRNifVFXecl1i7TF6ZMJP-GcrNdiUQsdM0NGaJJ1Q3OO3_Sk7YxExGt6xtb7HzEY2SyrLXYyPUe0tLalYIT22TKqdzOIKGwIu5qpDzrzEf_P4LCXrp8q3mCUGGdrCn4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور
https://youtu.be/epG70Xl1xGI
@WhiteDNS</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/whitedns/1373" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1371">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/1371" target="_blank">📅 23:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1370">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Sg3I4WeHm-ZYtp8aGPUxKjTDZjzBbF53gh_owjFHHanX_689M_P1cj0-hJqu5Lo0Y97KliaJhXaxnrZ638fQmQ93VM-tkITZtna0nwl0qmmQMoSZi5vycvTsZ_IGLFeU8jSm9otkDN7rZPqkFiT_5qA3LatW60WZWJ6PhhnINtO3lFI0WaSPAybutUjw0dM88E78ijJro72A767n14t_0wMu4jE5-U-88ygTg5QppKOn84VLauDRW6CVzHgbkWx0YMk2z3K2a-1JnNKi6SzLDFNJGuVbsu8rML47-5VkXrLZsuWiOpVGFKWpAkuH2kDLv-XJmsb3TGBMApH5vOnVoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/whitedns/1370" target="_blank">📅 11:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1368">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/1368" target="_blank">📅 05:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1367">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HwhjmNAXLdj0tr1PfFmfotVJ-gLvWEWXVAQQXyM8ltk-M6zbltO742LuWxItJy_7NzYTaYR56habXE8fV3rGtK5VX-nnYJDtb2Wj9qqqOz1aJmIW3UgITu20R-f04Y2mHnjeP3CwjO4fqleepeU9CJGsI8mpF28obkfJ3pZV53EgC-pA8cIfhNeRcD5JOV0GOfYmUho5lCYi8a_XIptMsY3wp3pqRCmeYsfhkvdcQVpn8I3u9zBm1aWu_-Iq0SaBlfJHF_tbkFRjaBhMvCjzQkA5Isx3HD8-uBd7CS5_nvn3gK4Et0yKwWDP39GvNht_CLIZjnEcpi-_dfK6GXYGrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/whitedns/1367" target="_blank">📅 05:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1362">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn-v1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">20.1 MB</div>
</div>
<a href="https://t.me/whitedns/1362" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/whitedns/1362" target="_blank">📅 05:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1361">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJViRaAxqfaxz7ponI0qOEueAVzhMzejwN38Htu1JPWVt_TE0WNMKJtkXURoDr2K7XWF7x-ZQtQwNb5fT3eTjcSdqcRSbCLEMvZlB0lws3pbac9pKIoTd6HQ9FdMBbe0ihv6rUSAovnr75BmsXCUrJsiQMIYWnla4Eb0om_i8AHAnMhvxWTQBUE65aK-zruxK2eMSIWNRJTMU7eV7CXHS17MlwQIcpKjo9K5x7MRY7unoQT8xxehVrJUzvW-8kffN0--kOac2eciFa2NqiY8I4Lk_T0UsAlrQ4NB8PwipqHarngQW67g3Q2FB9OGJPRK3EBb-wa5J4JJFJ8HoCjDqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1361" target="_blank">📅 05:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1360">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/R3qFP4VtGRcCUAQnRm68UzRxshRDgDE2rnaF7yb31TKa9-avHlSpoANdiskJeIbchUbakW0nrznSgNJBdhsrAD4pUv7_s4RyxTkLy7bmD6Pe5m-ZYd84fVqwnrmEVxn6hwQHOsPffPSnpsnA1u8i5KKA4qsj2-c3V6n0rbYbhkvRmCqZXKxhR-TucqhEb-BkPtlH7o_ytii-0Pk8DdBebyW1iDGIKfenN7kbyqqUbVAoQhOHsacAfviBK6vex2Y4gUME2cRj8_kc8HmyGuil5MDQ7KuHWboVOKvUnZVFI7Ib_l1LYIKO041WSEXbi6VezNB4lt9QZ78HFyyILL978A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1360" target="_blank">📅 04:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1359">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1359" target="_blank">📅 10:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1357">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DJD_b0NXaN5VAFRLjOoWPB1_NX4nc-zzQ2bVP-Kc0DmGSmGGwpuoQGeZIdwkqSYckRqtPhvm_mlvN88RajdfKEPWnkYOTUkh5TeEvAlENqHHs6cyYPukoQ-lc1PwhJLUmAbIl4IWwuqNi-NGR37ej_qa3aCzDrY8LrrxDEBssbTr4lPoPTH4XTvyi4LFG64oic5N9I0l_Vq4osvwYScHFbRrdqCSZXr38BgLCoS1X3JPbHqn4dQXUc_lOBRr_Fdw3hynsK3xMJydYPOua7vXu_T8LijH3Ucnz-WTU7mvQ_1D2MlxObCuJ3n_mS1WzaRKdux0wy0RKzKhJRPCt5_Xww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/whitedns/1357" target="_blank">📅 04:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1356">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/whitedns/1355" target="_blank">📅 18:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1354">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS   cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcn…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/whitedns/1354" target="_blank">📅 13:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1353">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/whitedns/1353" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1348">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.6.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.8 MB</div>
</div>
<a href="https://t.me/whitedns/1348" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/whitedns/1348" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1347">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVp44xqby_JybwIrrCka59fMogK5ZKcN9t6xtqCr5beyHn-s8tnnVeyWI0ZwR_2dawp-FE_k8MQbyRyq_hArYopOcFjANLOwdaIvhzZDt7omQ1v7y2-DkC2Wg1JM4dOUtpXMNpdoRl_Q5tD7ltyB_xCmPFSkJK4U_DZJJWwcgStMQUVYxQmt-lWmeyyqeMlnzucjXv7tOkqTmWsqGSxV946QeZynAJ5saohC2zVMPPE-NOGlo8czj9OvAacgZstQdPx31VeHWM8pG7UJfkModszMZx7Poqv9VA3Q6zRmzWH5xvJgpj7d6yqAZ676q9buN278bpZ63UXPiWR5S23zwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/whitedns/1347" target="_blank">📅 10:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1346">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🌎
دوستانی که با جزئیات فنی پروژه آشنا نیستند، به زبان ساده
CottenDNS نسخه‌ای کامل‌تر و پیشرفته‌تر از پروژه‌های MasterDNS و StormDNS
است.
تیم ما طی چند ماه گذشته، با استفاده از تجربه‌هایی که از قطعی و اختلال گسترده اینترنت به دست آوردیم، روی توسعه و بهبود این پروژه کار کرده است تا اتصال پایدارتر و سازگاری بیشتری با شرایط مختلف شبکه داشته باشد.
نسخه جدید اپلیکیشن
WhiteDNS
که تا ساعاتی دیگر منتشر می‌شود، از سرورهای CottenDNS پشتیبانی خواهد کرد.
هم‌زمان با انتشار نسخه جدید، یک سرور عمومی CottenDNS نیز در اختیار شما قرار می‌دهیم تا بتوانید بدون نیاز به راه‌اندازی سرور شخصی از آن استفاده کنید.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1346" target="_blank">📅 10:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1345">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1345" target="_blank">📅 10:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1344">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XFMtCBPxp4M6tt5YYraRKBt414Vcgy5A4uden2Ycq8RUjX0hB94CABHmGez63Fww61_lZIWaHaf35WYOZWHZILg39HAXIRcxWnhUHNDVU9euXKK0t4r3-y5fpeYzJsBi0N61KCZG10mEUpvUSGBEgx_VaqHJ8CSY1mL1oexs9Kk5fehkKWizil0QD_BJo1wxp1TvVp3uW9vohUhTlHk2o6iw1fHvdBXX36874IX2YtjWOzYeB_zI_0ndN3wdYQHNUAafOwmaDTJ_qdJXXcXFGcmOk3M5zfVdbdk-yzf5j-ddPv5RPgBxIgb-fM6dNmb4p7VCddeYADIKzdbjL7wEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضویت
در گروه whitedns
در گروه اختصاصی ما عضو شوید لطفا
🤝
@whitedns</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/whitedns/1344" target="_blank">📅 09:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1339">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn-v1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">20.1 MB</div>
</div>
<a href="https://t.me/whitedns/1339" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/whitedns/1339" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1338">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDQDwwkEsPQoCCHWwYk2g4WxKjdt9RzEpq9TdnwGxyDaGfQM74-zBLm8M3D2EREmoAR3IfvfX7xVq9YqpcvA6WRn_gopi0aHTlxKdpGPC9nEcXTq6i-mI_oe1Dy-0KLhbf-hZHBhoc6WlTC7WszAInBMyMQoV-fiVOoHJOZlCYQlCT4vUutvSdWaGOliVmmYsQi4a5MXc1q_IQvqiuBwuAuG3AXv3bHeZnk_4QA_-RuYIG6Wjv4qqVFZGsqR_CMEi3u9ghbD3Q1LyxYdJK0s37fRfvYwIlzH-QxYWrqTzL3JfMKsUuhyFvaAVu7r71oasvirjHWMEU_nnnUYSU1xqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/whitedns/1338" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1337">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ACzpzyWduJqZY4nhNqYZmtJgss7aMBYAh0SsiJekk8jSi_Mrq5-24SD3lulEpOXIFo66By1Gx5an6PyC6a6w75Jq2X3FQjwX9efVx2_rhkpokuWVi5EvtUaILeT0Qbq2gp5lbmOK72RkkEEz849EJTT7h0F1ldCZFblLRGnnA89faDCNKN4zLv8qzq0D6Ulfwl1-AcJKctX4mA1SINUlHoEpsFEAHzOpH_PtqSUhGz6AMmLHVTT1azNknppiRKgRugk-ffCaAPg5Xxf0xjYsRiEk-hKTf8T-NHv6sbURVTHvqgu1z6N7dxGf_nhCzTw5L1It50p-6VKJ_dCRe0NuYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
👋
:
حالا همیشه هم پست برنامه و توضیح نگذاریم، بعضی وقتها یکم حرف بزنیم با هم، اینجا همه با هم داریم کار را جلو می‌بریم
🤝
✨
برای اینکه یک پروژه درست بشه ساعت‌ها وقت و هزینه صرف میشه تا به دست تو برسه
💸
⏳
، وقت و هزینه‌ای که میشد گذاشته نشه، زمانی که میشد در کنار دوست و خانواده بود و یا اصلاً رفت عشق و حال کرد
😔
💔
. اغلب دولوپرهای این تیم کلاً نیازی به بودن اینجا ندارند، فقط احساس دین می‌کنند
🙏
.
شما میتونی با لایک
👍
و دیس‌لایک
👎
، پروژه را تایید کنید یا ردش کنی و یا با قلب
❤️
حمایت کنی و ....
خطاب به اون چند نفر :
اینکه تو اینقدر بی‌شخصیت هستی که آیکن
🤮
می‌گذاری این فقط یک چیز را می‌رسونه، تو لیاقت این را نداری که کوچکترین خدماتی حتی با دریافت هزینه بهت داده بشه
🚫
🛠️
. تو همون کسی که اصلاً برات مهم نیست چی به مردمت می‌گذره، برات هیچی مهم نیست
🤷‍♂️
.
متاسفانه تو جرات نداری بیای توی گروه‌ها خودت را نشون بدی و بحث فنی کنی
💻
🛑
، والا تکلیف مشخص میشه.
یک تعداد زیادی از شماها که همراه ما هستند یکی از یکی خوب‌تر و مایه انرژی ما و بقیه هستید
🔥
⭐
، دلیل اینکه ادامه می‌دیم شماها هستید، والا کار ما خیلی وقت هست که تمام شد
🏁
.
ارادتمند
👋
ویسپر
🎤
تیم whitedns
🛡️</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/whitedns/1337" target="_blank">📅 08:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1335">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GAwnpqClw2wvIt_nvN95j6kCRblP5x2NrXvtWW0jHKfCoOMcANBvemr9LWraJylAVfVik2wQQJ_6dEGVIN9nBCAFhJpBYqH8iL9KVj3JXkVEhCAyydIHDyW7ciQc1Evta4kXLypeh_FIj7wJGbPIcghbYOoRXhV6V3gXiaDzxZK9x8kqy5BZYfSTAFhAng5RhFCXzBW09UGDeEiGPIdpnL1ueF4bkVsBQdHhtYAeTWzth7UyS5WuY0DEt_RVdK0DBCooCMKFK0ttkgFyhNdYAVJV4jFlKqrYLMldUdo3XfKBWLUOrXzglX9WgtIZuFhKLqTNzLoHQEQM_MfbAaAv8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Aether Desktop اومد! — آزادی، با یک لمس
🔥
بالاخره نسخهٔ ویندوزی Aether رسید!
🎉
همون اپ محبوب اندرویدی، حالا روی ویندوز — با همون ظاهر، همون آیکون و همون هستهٔ قدرتمند. نسخهٔ 1.0.0 اولین انتشار دسکتاپه و هیچی از نسخهٔ اندروید کم نداره!
✨
چی داره؟
🔌
اتصال قدرتمند:
▫️
۴ پروتکل: Smart (انتخاب خودکار) · MASQUE · WireGuard · WARP×2
▫️
۵ حالت اسکن: از Turbo تا Ironclad
▫️
اتصال مجدد خودکار تا ۵ بار + انتخاب هوشمند پروتکل اگه یکی جواب نداد
▫️
پشتیبانی IPv4، IPv6 یا هر دو باهم
▫️
نمایش زندهٔ سرعت، پینگ، سرور و IP با پرچم کشور
🏳️
🎨
رابط کاربری خیره کننده و زیبا :
▫️
کاملاً دوزبانه (فارسی و انگلیسی) با پشتیبانی کامل راست‌به‌چپ
▫️
تم تیره با طراحی دقیقاً مثل موبایل، بهینه برای مانیتورهای بزرگ
▫️
نوار عنوان به سبک ویندوز ۱۱
⚙️
تنظیمات پیشرفته:
▫️
نویز (از سبک تا تهاجمی و GFW) · MTU دلخواه · Fragment · ECH
▫️
تونل تفکیکی (Split Tunneling) — انتخاب کن کدوم برنامه‌ها از تونل رد بشن
📡
اشتراک با بقیه دستگاه‌ها:
▫️
SOCKS5 روی پورت 10810 و HTTP روی 10811
▫️
هر دو پورت خودکار پروتکل رو تشخیص می‌دن — هر کدومو هرجا بزنی کار می‌کنه!
🛠
عیب‌یابی حرفه‌ای:
▫️
تست زندهٔ اتصال + بررسی ۶ موردی محیط سیستم
▫️
کنسول لاگ زنده و رنگی با دکمهٔ کپی
🪟
مخصوص ویندوز:
▫️
تونل واقعی سطح سیستم با درایور رسمی و امضاشدهٔ مایکروسافت (Wintun)
▫️
پروکسی سیستمی خودکار تنظیم می‌شه و موقع قطع، برمی‌گرده سر جاش
▫️
نیازی به Visual C++ نداره؛ WebView2 هم نبود، خودش نصبش می‌کنه
📦
دانلود:
▫️
نصب‌کنندهٔ گرافیکی برای ویندوز ۶۴ و ۳۲ بیتی
▫️
نسخهٔ پرتابل بدون نصب — هیچ ردی روی سیستم نمی‌ذاره!
👌
▫️
فایل SHA256 برای راستی‌آزمایی سلامت فایل‌ها
⚡️
ساخته‌شده با Rust + Tauri 2 — یعنی حجم نصب فقط چند مگابایته، نه ۱۰۰ مگ مثل اپ‌های Electron! کل بیلد و انتشار هم صددرصد خودکار با GitHub Actions انجام می‌شه، بدون هیچ دخالت دستی.
📋
پیش‌نیاز: ویندوز ۱۰ (نسخهٔ ۱۸۰۹ به بالا) + دسترسی Administrator برای ساخت آداپتور شبکه
📄
لایسنس: MIT — کاملاً متن‌باز و رایگان
💙
⬇️
همین الان از بخش Releases گیت‌هاب دانلود کن و آزادی رو با یک کلیک تجربه کن!
📥
دانلود مستقیم از گیت هاب
https://github.com/QW-AI-Code/Aether_Desktop/releases/
سلام دوستان عزیز
✋
یه یادآوری مهم که حتماً بخونیدش
👇
برای اینکه اپ (چه نسخه اندروید چه ویندوز) براتون وصل شه، این چند تا نکته رو رعایت کنید تا بهترین نتیجه رو بگیرید:
⏳
رو هر پروتکل ۱ تا ۳ دقیقه صبر کنید تا وصل شه. بسته به اپراتور و منطقه‌تون این زمان فرق می‌کنه، عجله نکنید.
🔄
پروتکل‌ها و تنظیمات مختلف رو تست کنید. چرا؟ چون DPI هر سیم‌کارت با سیم‌کارت دیگه، هر منطقه با منطقه دیگه و هر شهر با شهر دیگه فرق داره.
📱
اگه با موبایل وصل نشدید: چند بار گوشی رو ببرید رو حالت هواپیما و برگردونید تا رنج آی‌پی‌تون عوض شه، بعد دوباره پروتکل‌های مختلف رو تست کنید. خلاصه باید قلق DPI اپراتور و منطقه خودتون دستتون بیاد
😉
📶
اگه با وای‌فای هستید: مودم رو ۱ تا ۲ دقیقه خاموش کنید تا رنج آی‌پی عوض شه، بعد دوباره با پروتکل‌ها و تنظیمات مختلف امتحان کنید.
❌
اگه بازم وصل نشد، یعنی این وی‌پی‌ان با نت شما جواب نمی‌ده و باید برید سراغ وی‌پی‌انی که با نت شما سازگاره.
⚠️
و نکته آخر: بعضی از کاربرا میگن این اپ مشکل داره و واسشون کار نمیکنه.
اگه مشکل از خود اپ بود، نباید برای هیچ‌کس کار می‌کرد! همونطور که می‌دونید برای خیلی‌ها داره کار می‌کنه و هر کسی تجربه متفاوتی داره.
پس اگه برای شما وصل نمی‌شه، مشکل از Aether نیست؛ مشکل از DPIایه که رو اپراتور شماست و جلوی کار کردن اپ رو می‌گیره.
#VPN
#فیلترشکن
#Aether
#ویندوز
#متن_باز</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1335" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1334">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8d366d7.mp4?token=oqyGNs-NnriRLIgPdHUa6gloZ1dL8J4zLPIbCSN2qBc0100DkwHy02ox0zQwZEAT4JvW29TCJccw4IuEKjQmvRlerWOeKorgUqmra64tLneZa9eYYgJ1hNTZCvRt8KFZOZ9Oo4VBvfbMwiDPKnFbr21kF6o7OQKdi8cdUQm4KHSheI8OjhGCeTJ9PAMfWnLXpz2Z0X0mrsoUKenumNa9c8Rj0NaNFJIZSGMngpmicRElhliyLfSbZO544ke3wfp2uKLX-Khy8Q3oh1wZo8b_rPIyh9bNcjm9_Ue77Uswls3vTgZi7Eul1Fk-r0oOuHVZlrYoYDNRIi7rwwDUGgIGGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8d366d7.mp4?token=oqyGNs-NnriRLIgPdHUa6gloZ1dL8J4zLPIbCSN2qBc0100DkwHy02ox0zQwZEAT4JvW29TCJccw4IuEKjQmvRlerWOeKorgUqmra64tLneZa9eYYgJ1hNTZCvRt8KFZOZ9Oo4VBvfbMwiDPKnFbr21kF6o7OQKdi8cdUQm4KHSheI8OjhGCeTJ9PAMfWnLXpz2Z0X0mrsoUKenumNa9c8Rj0NaNFJIZSGMngpmicRElhliyLfSbZO544ke3wfp2uKLX-Khy8Q3oh1wZo8b_rPIyh9bNcjm9_Ue77Uswls3vTgZi7Eul1Fk-r0oOuHVZlrYoYDNRIi7rwwDUGgIGGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">UAC SNI Spoofer Desktop
نسخه 1.0.6
━━━━━━━━━━━━━━━━━━
تغییرات جدید نسخه 1.0.6
• قابلیت Mobile Gateway اضافه شد. دستگاه‌های متصل به شبکه وای‌فای مشترک می‌توانند بدون تغییر تنظیمات Proxy، IP یا DHCP از VPN کامپیوتر استفاده کنند.
• امکان پینگ‌گرفتن از کانفیگ‌های موجود در تب Configs و مرتب‌سازی آن‌ها براساس کمترین پینگ یا کشور اضافه شد.
• باگ‌های جزئی بخش SNI Config Maker برطرف شدند. اکنون کانفیگ‌های بیشتری از مخازن شناسایی، دریافت و پردازش می‌شوند.
• مشکل فعال‌نشدن دستی کانفیگ‌ها، به‌خصوص هنگام استفاده از Auto Mode، برطرف شد.
━━━━━━━━━━━━━━━━━━
لینک دریافت نسخه 1.0.6:
https://github.com/Floxu1/UAC-SNI-Spoofer-Windows/releases/tag/1.0.6
لینک گیت‌هاب پروژه:
https://github.com/Floxu1/UAC-SNI-Spoofer-Windows
t.me/UacSniSpoofer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1334" target="_blank">📅 00:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1333">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🌎
نسخه جدید WhiteVPN 1.1.0 منتشر شد!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1333" target="_blank">📅 17:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1328">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn-v1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">20.1 MB</div>
</div>
<a href="https://t.me/whitedns/1328" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/whitedns/1328" target="_blank">📅 17:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1327">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAo2_pkB1haKW9jZlRNN_QdYTAdMeursD3GhT0IRWLGKvHRHo46THIrxAxPpyp48iY0Uk54k_abWGQJG0xcXul0x2rXU_yT1s8XP7zXk69nIS-L6iXVPhqQ_uZFmeZkUp5Krn_Lb__x4dThFlxpuZiu2D_ZUrGZ39j3DddVNFwPV1yS-qJt3q8rfcF9ZXJVOTE-m3TWrOoNtzNloBBr32_B7HWLqTsIv4-7x53MdFMey7sgiX5zoboUZdtE1PRDc9NcYSM-5fYsICFa3pF4_nAI0WAOPYMn3Q52lc_hPxw4MsoTGqGAeonnlpdsbuOLYxVUeMON3fPtTfpuTv7JMOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48K · <a href="https://t.me/whitedns/1327" target="_blank">📅 17:43 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
