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
<img src="https://cdn4.telesco.pe/file/EgSuAuL0l5I0OQ_-6s2RWfsD4IJ7MM_ME2ioUIVOJDJMN2TI1QgiF0oB2dfmhrG5SeVBo1qk_4uAI_KZmvai-34dgwyBVW7CeaslXlarIuV74OaKoJrl0JNTthLQv-t7YQeBgKMxZ2cU7J8S9oOaHQW8PpOBnaXtxRLsLgdU1NRkDVABDkGzzgbJPqw9r9Reffk0k4LItpi3upOmK2uL1oxL5kY7VWbWAAk_bqK2nr33j69G_Yk9hjOT_DwSqnZVUe20wTL9yPPjWm96f7rKeYYD2EbC8_n6Ibd-pSVIkWoUvRVCNy0jFMr0Cxlc4UzIgUIFBejBpeNdzudhBPkbtg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 03:15:42</div>
<hr>

<div class="tg-post" id="msg-1602">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ah0XcYMQlpd3XhEudZE0d-BJr7e3R8vKn9jJ4RdmTBWvVw-938WYQ7JwkUtIAhS02d_bvPDE5Vj8beueSetrBl8Kyjg3XFN3ViXjUVgD3mwn72Cg75rK7W0midAJrAR5k8BITBA5yjal9lXWTPNVYX-En7B1uCVRKBbIEI7XX6nTeR9gRFsVSSjyakcpB6FKFWJVt38h5yYN0fs9jEj9cUKcbi6XIyfNwP-AeZWJbf8VWN0bfrn-I5HDUicFB1UH8qRstTuG4nSCVlqsrwArvRJd7-Lj1pFo9F4oQSnhOW1xqv0NcNMHU8agf48WYJj8gHhnI6hDFhmM-pZBw3bscg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
نسخه جدید موبایل و دسکتاپ به زودی منتشر می‌شود!
این نسخه‌ها شامل چه مواردی است؟
🟢
بهبود عملکرد اتصال برنامه
🟢
ارتقا موتور به ۱.۷.۰
🟢
اضافه کردن امکان LAN sharing
🟢
رفع باگ
🟢
در اندروید امکان اضافه شدن به Quick setting
🟢
استفاده از wireguard و hysteria exit chain برای داشتن حداکثر سرعت
ممنون
@WhiteDNS
🔥</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/whitedns/1602" target="_blank">📅 19:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1601">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OO8OZGVnxMALR9uLMW1c_tn5spiuL7mqK_aLSCNVSf5-uKTnGH7h18mMOGpAuoZZIw_o7TQCwh6pvcTGQfWv-aFZUfCL1NrkO-ZyOx8PtPIKAIRgTqEBCsaUYxIti19w0bmgkKLJL8stYq7LelXi-sT1kAwz6Q6pL0CMTBR17ATTEn_8WkqccBO-6dipp3zrPjIjXtnNFjeyc_yGFoe5LHzUdnd1YXLu8bz-8rlK8EgNd-bucuYIz40H8JJmHXtyLtU5cAD3TgRbtNT84Iys8kmrZKXaCV7P2OkCW0A1sBdhvp6yvc2Jbhm1NsDUuvdBiQpur2JZk74axBLoL8e7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم
⚠️
⚠️
⚠️
⚠️
⚠️
دوستان :
پست  را با دقت مطالعه کنید
https://t.me/whitedns/1568
این کانفیگ های برای قابلیت "exit chain" توی اپ whiteaester و whitevpn هست - که ip شما را ثابت میکنه و یک لایه امنیت بیشتر به شما میده چون TLS هست
چون خیلی از دوستان کانفیگ نداشتن و یا نگران امنیتشون بودند ما این امکان را فراهم کردیم .
این کانفیگ ها برای استفاده مستقیم در اپ هایی مثل v2rayng و غیره نیست، اگر قصد استفاده مستقیم دارید لطفاً درخواست ارسال نفرمایید
تشکر
@whitedns</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/whitedns/1601" target="_blank">📅 17:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1600">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/dfRpFTspLwOI8cq7ZMesmV9TolRu2UsV9Ol3pWs2mO-BTGQ-FbZQaABs5rO0-NBVo5KS0OlsivhxNR33pPGaYSmvAJ41k94iHdM9LwTOkwEwCVjfRjVZTjrbVcdPlSRAxTdRK7b6sMlXESVSON_PcY0daPXy0s7y1YIpIK5Jc45SlwAUqcxZEVLtuCFwY3klDTBDdumu1DgYlt0nkkShAijhnariHcXjC-70rjmxcpWyWaBxZT8kEJi2OzVgtDouGqZyl13Xqtd6bepMCC_zwKaVYXW_PKNwF6Facs3sPUh33Qsnd-u9sDjCCJM9qOGGLaYDMJJvCLnmWJd7mx-zpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/whitedns/1600" target="_blank">📅 17:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1599">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMasterDnsVPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmTp7CkpR7w692Lj-z58TrQLrIGFft0o-blYebScvk7PeSOdkGwb0dQ_fHSyorKoT_Z8GQP4qLaemYrn_zunYYizyJUlQEarXVk73UYAZcGSpjvxFdAWgHXmXkT6Nh4C7ugjCUWC_yRBMd3h17x7GCI-BDJ72ZUUmkB3WedadUOTljw6PHyN_B382C_8qzaUjKlexcnaKUCLKtHuzGVCuy28faNg1jSrxTYB8ORcCwAIqPl3gAIRbx0DsQVisDSenjPM8W26B1kWL3zLRcgIXpdugOtwctgZK3vroS1wZZnhlLHL5i-Wujzi_Wc2ghGmsGdblVMELhYSDzqnrAIbzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👋
درود،
◀️
آموزش رفع مشکل خطای
Sign-in failed: failed to start login server: An attempt was made to access a socket in a way forbidden by its access permissions. (os error 10013)
مربوط به برنامه ChatGPT در ویندوز
◀️
ابتدا در منوی استارت خود کلمه cmd را سرچ کنید.
◀️
سپس روی آن راست کلیک و Run as Administrator را بزنید.
◀️
در نهایت دستورات زیر را وارد کنید و Enter بزنید.
net stop winnat
net start winnat
✅
مشکل شما رفع میشود.
❤️
پیروز و سربلند باشید.
🤨
با تشکر فراوان،
امین محمودی
🗓
3 شهریور ماه 1405
🛡
کانال:
@MasterDnsVPN
💬
گروه:
@MasterDnsVPNGroup
#chatgpt
#هوش_مصنوعی
#رفع_مشکل</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/whitedns/1599" target="_blank">📅 16:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1598">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMasterDnsVPN</strong></div>
<div class="tg-text">👋
درود،
⚠️
یک پروژه هست، دوستان معرفی کردن، من تایید یا رد نمیکنم، فقط منتشر میکنم، خوب بودن و نبودنش با خودتون، من خیلی چک نکردم.
◀️
پروژه واسه جمع کردن کانفیگ های v2ray هست.
👩‍💻
0xRadikal/Free-v2ray-Configs
◀️
تفاوت اصلی پروژه با بقیه ریپوهای کانفیگ رایگان اینه که صرفاً کانفیگ‌ها رو از منابع مختلف جمع نمی‌کنه. کانفیگ‌ها وارد یک pipeline چندمرحله‌ای می‌شن، duplicateها حذف می‌شن، ساختار و endpoint بررسی می‌شه، اتصال TCP تست می‌شه و در نهایت کانفیگ با یک درخواست HTTP واقعی از طریق proxy در ۳ دور مستقل تست می‌شه.
◀️
در حال حاضر پروژه از ۲۱ منبع تغذیه می‌شه و در آخرین اجرای ثبت‌شده:
🔴
۱۱٬۴۱۵ کانفیگ یکتا جمع‌آوری شده
🔴
۲٬۴۰۳ کانفیگ در هر ۳ دور تست موفق بودن و وارد بخش
verified
شدن
🔴
خروجی‌های
verified
،
fast
،
secure
و
top100
تولید می‌شه
🔴
خروجی برای V2Ray/Xray، Clash و sing-box ارائه می‌شه
🔴
کل سیستم هر ۱۵ دقیقه به‌صورت خودکار به‌روزرسانی می‌شه
✅
به گفته ناشر: هدف پروژه اینه که این پروژه تبدیل به یک منبع متن‌باز و قابل‌اعتماد برای کانفیگ‌های رایگان بشه، مخصوصاً برای کاربران ایرانی.
🔴
نمونه همینکار رو هم WhiteDns انجام داده، اینجا میتونین ببینین:
👩‍💻
WhiteDNS/subs-check
🔴
اگر از این پروژه خوشتون اومد میتونین با
⭐️
دادن داخل گیت هاب از ناشر این برنامه حمایت کنین.
⚠️
نکته تکمیلی از سمت خودم: اگر از Vless/Vmess و هر فیلترشکن رایگانی استفاده میکنین، اگر امنیت اطلاعاتتون مهمه، حتما از حالت Chain و ... استفاده کنین، یعنی به وسیله اون VPN به یه VPN دیگه به سرور خودتون وصل بشید و Vmess/Vless سرور خودتون رو داشته باشید، از سرورهای رایگان برای فیلتر نشدن و ... استفاده کنین (البته که من کلا پیشنهاد میدم، VPN رایگان تا حد امکان استفاده نکنین و سرور خودتون رو راه اندازی کنین، اما این سرویس ها ممکنه، برای بعضی ها کاربردی باشه)، اما برای امنیت بیشتر اینکار رو انجام بدید.
❤️
پیروز و سربلند باشید.
🤨
با تشکر فراوان،
امین محمودی
🗓
1 شهریور ماه 1405
🛡
کانال:
@MasterDnsVPN
💬
گروه:
@MasterDnsVPNGroup
#v2ray
#معرفی_پروژه
#اینترنت_آزاد
#فیلترشکن
#vless
#vmess</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/whitedns/1598" target="_blank">📅 09:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1597">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg_NQOclWEAo_cKUtzKuxOnn0PSphaZHMdQ2nBfh9DEbE9tlp1smoCor-NCQ6V-FecVJUeVGHeGUdrRpYqyihUwln-oZrTNhEkhObs6m189OC1R9cqi3AnPIpVzbtnNiFk9AyVvVmH29AEJVzykwg3lgn4XdPQW9zrdtuZBB-Mrf8fuoqrx-4QADQkBvD1YzUtWn05SXqs9T_2cpwxET-jgodN1e4dBFPqwKq6wJNDuoDTOY_6ys5WuCJevSBwaz4APR0CS0ygWybCM0TfN5hkEw4TpKcbKr1W1oR8uQ6CPKyZvdcz47PiazwTjEBv6pJDQnlwSJX_voyL6oIT4I8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برای آیفون اپلیکیشن نداریم؟ چرا، داریم!
اگر از کاربران iOS هستید، می‌توانید از اپلیکیشن
Core Forge
استفاده کنید؛ یک اپلیکیشن کامل که سه قابلیت اصلی را یکجا در اختیارتان قرار می‌دهد:
🔹
اتصال VPN
🔹
استفاده از MasterDNS, CottonDNS
🔹
اتصال از طریق پروتکل Aesther
دیگر لازم نیست برای هرکدام از این قابلیت‌ها یک اپلیکیشن جدا نصب کنید؛ همه‌چیز داخل
Core Forge
در دسترس است.
📥
دریافت Core Forge برای iPhone
🎥
تماشا ویدیو آموزشی در یوتیوب
🔥
لینک ساب WhiteVPN برای استفاده در اپ</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/whitedns/1597" target="_blank">📅 08:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1596">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📹
آموزش اپلیکیشن WhiteVPN کامپیوتر و استفاده اپ داخل
🍏
آیفون برای کاربران IOS
https://youtu.be/tm0ls3r4ppw</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/whitedns/1596" target="_blank">📅 01:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1594">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔭
در ۳۰ روز گذشته، بیش از ۷۰۰ هزار اتصال موفق در اپلیکیشن WhiteVPN ثبت شده.
خوشحالیم که در این مسیر کنار شما هستیم.
🕊️
به امید روزی که همه به اینترنت آزاد دسترسی داشته باشیم و از WhiteVPN فقط برای حفظ امنیت و حریم خصوصی استفاده کنید، نه برای عبور از فیلترینگ.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1594" target="_blank">📅 14:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1593">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🌎
انتشار نسخه ۱.۶.۲ WhiteDNS برای اندروید</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1593" target="_blank">📅 14:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1589">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.2-armeabi-v7a.apk</div>
  <div class="tg-doc-extra">34.2 MB</div>
</div>
<a href="https://t.me/whitedns/1589" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/whitedns/1589" target="_blank">📅 14:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1588">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxm2aiKD7l23Urm-chrVf2iYvfy41HeX7-azqrvw-xCXDd6ZivP4XCViRNbQmSqBV7qGZsxIedL1aLi-1fBKL8SzhDyOPRkx7BajKu5DN7geCYc02bqF_zWngWegjGPWVHlxq4Lz7L30f2z_en3kg7GUpODNaqYmcoPf0FOM_o7au_R05W-0uEV6DUE7xZaB6H2a21ptjJ02xUaG_jmy2Y204ZNJ5wVH5dX9atSQJyTyDH-bcTaXFQH828Ku0ONAKDieBkz_iE9tJPzFjIq5nBsb3j6YlPealG6-f2cQ5XeDg6GT7VvoXnFcWN4l1Gp-99ND9ixervMks9yX4i_ljQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
WhiteVPN 1.6.2
✍️
این نسخه اتصال WhiteVPN را سریع‌تر و پایدارتر می‌کند و چند بهبود مهم برای سابسکریپشن‌ها، تنظیمات و Split Tunneling دارد.
✍️
تغییرات مهم
• اتصال مجدد خودکار، سریع‌تر و قابل‌اعتمادتر شده است.
• در صورت بروز مشکل در اتصال، برنامه بهتر و امن‌تر آن را بازیابی می‌کند.
• بررسی سلامت اتصال و مدیریت تغییرات شبکه بهبود یافته است.
• هنگام قطع اتصال، وضعیت واقعی عملیات نمایش داده می‌شود و برنامه تا توقف کامل اتصال در حالت «در حال قطع اتصال» باقی می‌ماند.
• مدیریت و ذخیره‌سازی سابسکریپشن‌ها پایدارتر شده است.
• فایل‌های خراب سابسکریپشن به‌صورت خودکار شناسایی و دوباره دریافت می‌شوند.
• آخرین نسخه سالم سابسکریپشن برای مواقعی که دریافت نسخه جدید ممکن نیست، حفظ می‌شود.
• پشتیبانی از لینک‌ها و کانفیگ‌های SOCKS و SOCKS5 اضافه شده است.
• تنظیمات سابسکریپشن، زبان و ظاهر برنامه به بخش جدید «تنظیمات برنامه» منتقل شده‌اند.
• گزینه «بازنشانی تنظیمات» اضافه شده است؛ بدون حذف سابسکریپشن‌ها، نتایج تست‌ها یا قطع اتصال فعال.
• در بخش Split Tunneling اکنون تمام برنامه‌های نصب‌شده، حتی برنامه‌های بدون آیکون، نمایش داده می‌شوند.
• اسکرول فهرست برنامه‌ها در Split Tunneling اصلاح شده است.
• ذخیره نتایج تست اتصال و به‌روزرسانی صفحه سریع‌تر و روان‌تر شده است.
• حجم نسخه نهایی با حذف منابع اضافی کاهش یافته است.
📱
دانلود از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.2</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/whitedns/1588" target="_blank">📅 14:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1587">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✍️
دوستان، فعلاً سرور ساب WhiteVPN با یک مشکل فنی روبه‌رو شده و بچه‌ها در حال بررسی و برطرف کردنش هستن.  به‌محض اینکه مشکل حل بشه، ساب رو آپدیت می‌کنیم و همین‌جا بهتون خبر می‌دیم.  ممنون که صبورید و شرمنده بابت اختلالی که ممکنه براتون ایجاد شده باشه
🙏
فعلا…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/whitedns/1587" target="_blank">📅 13:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1584">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/PE1MqhpozaHr78GhTEQOj6plIx3vB-npEVaERKzRqqHa-UVZ-srZeUC50Ty95pr8-SNgWuFIBEBZviOklvD9DgSO-k04wF0J3024WHsg0--8lXVYggYNQLBE1i6gQkQeRVF47r6ThgsND3vtR2oytWltu9qrkKwt39GJrNleVWyvWQlo2tUqvO8aImPIubu7YmMfu0mGpacNkEhjIhTwRZaMhyLIaNyd4UtChFGZRz6l1JzYdwLXvq5TChMLz2Hl8Qu2DADLW0T_RWX_1w_TUkor_GUvMVUr6UaCEYQSQODSSVA-S9pIUIX6V3_kJid7xToH3MtmT308IadzpvwA-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم
⚠️
⚠️
⚠️
⚠️
⚠️
دوستان :
پست  را با دقت مطالعه کنید
https://t.me/whitedns/1568
این کانفیگ های برای قابلیت "exit chain" توی اپ whiteaester و whitevpn هست - که ip شما را ثابت میکنه و یک لایه امنیت بیشتر به شما میده چون TLS هست
چون خیلی از دوستان کانفیگ نداشتن و یا نگران امنیتشون بودند ما این امکان را فراهم کردیم .
این کانفیگ ها برای استفاده مستقیم در اپ هایی مثل v2rayng و غیره نیست، اگر قصد استفاده مستقیم دارید لطفاً درخواست ارسال نفرمایید
تشکر
@whitedns</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/whitedns/1584" target="_blank">📅 11:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1582">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✍️
دوستان، فعلاً سرور ساب WhiteVPN با یک مشکل فنی روبه‌رو شده و بچه‌ها در حال بررسی و برطرف کردنش هستن.
به‌محض اینکه مشکل حل بشه، ساب رو آپدیت می‌کنیم و همین‌جا بهتون خبر می‌دیم.
ممنون که صبورید و شرمنده بابت اختلالی که ممکنه براتون ایجاد شده باشه
🙏
فعلا از ساب موقت استفاده کنید تا اون مشکل حل بشه
https://ns1.rmft.tech/top300/sub
https://raw.githubusercontent.com/paranoideveloper/CoreForge-Sub/main/subscription_base64.txt
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/whitedns/1582" target="_blank">📅 07:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1581">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/dtlvvebX77H5yf4h42EyyQ2nkg3wKiUJElmQ1MvPkRugABWypqAtIDfPUYVdVJHkn0KqWzA-df9u5Pthot6h5DRJlIBwOqQPIhifnzHmRo6ialeRquEFLO9JbSwub5HH7n6E4QiHuYA4kDgBWh9IUdwQWXT_4HE0SjXQ3U4e8TYGRmiuNNebLgNGhEeClv5jTETAA6ask34ZXWCpop5en3Xka0rY6cgvoP58Gq6G2Jc6xJnPH2qZvfJcS5QxftBbaos2EullgitaWysLso3sMHG5BfMVlEZqFTFj25_oXQUCGuhBlVc2AaEo_qOpS4ls09yVfe7UWWQonlah80t2XQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/whitedns/1581" target="_blank">📅 06:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1580">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NFECLzlT24p59YjYBmSLBiMe1k-dhsdYdWB7CZHh5BLhbhX1V4va54kh8WX3bb7VX9ouZG3q9kg9e8A6fNAt2DwILqJkK3XA0a9UucaV3AXJN5Exd1OjmRINj6Mzq3wxVIwYHbwdU26RQgtAgQ01QdvMY3RiGFVErN6ULhsKQ4NZDanuGhQelWxSoHWtUNYh5MKzKSMX-17IIDugSRIY-rMXhM9NRKDeVo9Gwnrf3xVaNRORmgiwekz1zT8-g1DxDj6RKdcoCSVR4JnzOPPgSOTqUSZzTGmTeGs_Pgf3Tdc2OHCPbx4GiZAMJrxK9z1RJ7QO6NytO6FHp12SnWHMYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6K · <a href="https://t.me/whitedns/1580" target="_blank">📅 06:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1579">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UBPFIiFa0xVyni7zRMx0OAtmQgsmPHNUpJt80B5uPQb5G86QfTOH_4C0rNcAbOn-lRbdL6BjA7I1-69tSk_Gud_VCk9rs5a5zNfttJ5c9ufoowwQ_9ibTxPSRLHTICBOJQoM2iFtAPntYvM1DU5a6SYB26BkSjpRNAHCFUMLWxiefMP5AYfl_fbqmP0AJ-ybGbj2iDPdbM_ggLtZ5s07QgT0JjJG_hfx2EyjwTWJG8S7TYrsZkYnkiPVEILasAA30RLWZ-Fl4LAURWVvE538dO-jiwzHIhSMmm1eCP_RG3f_q7ZGGwFtcAY5_vv5IoZDEVpE92gYw2HXual11uUvbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم
⚠️
⚠️
⚠️
⚠️
⚠️
دوستان :
پست  را با دقت مطالعه کنید
https://t.me/whitedns/1568
این کانفیگ های برای قابلیت "exit chain" توی اپ whiteaester و whitevpn هست - که ip شما را ثابت میکنه و یک لایه امنیت بیشتر به شما میده چون TLS هست
چون خیلی از دوستان کانفیگ نداشتن و یا نگران امنیتشون بودند ما این امکان را فراهم کردیم .
این کانفیگ ها برای استفاده مستقیم در اپ هایی مثل v2rayng و غیره نیست، اگر قصد استفاده مستقیم دارید لطفاً درخواست ارسال نفرمایید
تشکر
@whitedns</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1579" target="_blank">📅 22:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1577">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📹
آموزش اپلیکیشن WhiteVPN کامپیوتر و استفاده اپ داخل
🍏
آیفون برای کاربران IOS
https://youtu.be/tm0ls3r4ppw</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1577" target="_blank">📅 17:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1576">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLordofCinder</strong></div>
<div class="tg-text">🚀
بالاخره ‎CottenRouter‎ منتشر شد!
چیزی که خیلی‌هاتون بارها درخواست کرده بودید، بالاخره آماده شد.
🔥
اگه روی یک ‎VPS‎ چند ‎DNS Tunnel‎ دارید، دیگه لازم نیست برای ‎Port 53‎ بین سرویس‌ها درگیر باشید.
‎CottenRouter‎ امکان اجرای چند ‎Tunnel‎ روی
یک ‎IP‎ و یک ‎Port 53‎
رو فراهم می‌کنه و هر ‎Domain‎ رو به ‎Backend‎ مربوط به خودش هدایت می‌کنه.
⚡️
پشتیبانی از:
‎CottenDNS‎
‎MasterDnsVPN‎
‎StormDNS‎
‎thefeed‎
‎SlipGate‎
🛠
امکانات:
• ‎UDP / TCP‎
• ‎Multi-Domain‎ و ‎Multi-Backend‎
• ‎Port 53‎ بین چند ‎Tunnel‎
• ‎DoT‎، ‎DoH‎ و ‎HTTPS‎ بر اساس ‎SNI‎
• ‎TUI‎ و ‎Control Deck‎ برای مدیریت و مانیتورینگ
• نصب مستقیم روی ‎Linux‎
• پشتیبانی از ‎Docker‎
• ‎AMD64‎ و ‎ARM64‎
🛡
بدون دستکاری ترافیک ‎Tunnel‎
‎CottenRouter‎ چیزی به پکت ها و تانل اضافه نمیکنه
بنابراین قابلیت‌هایی مثل ‎ARQ‎، ‎FEC‎، ‎Compression‎، ‎MTU Discovery‎، ‎Record Channels‎، ‎SOCKS‎ و ‎TCP Forwarding‎ بدون تغییر باقی می‌مونن.
🔥
خلاصه:
یک ‎IP‎ + یک ‎Port 53‎ + چند ‎DNS Tunnel‎
🔗
‎GitHub‎:
https://github.com/TaJirax/CottenRouter</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1576" target="_blank">📅 15:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1570">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AFWknjWKNWKxT_7eqiEZEM50BqfhKEERan9RDUWDjk_4tGtl3njH9cRLj7mjAjRbFXbjUBvr8mpLwtR4rr62_Tto-m9O09kle3UDRoEHuBGXgfh5mxnkuIf7ptJr7S7pR0amFS8A8pS82wzeVF8nx6KvMIk8gwlY0wGKY58AInWqMIubPdnz2-i1_KSLu4OBEML-oXK9Swiwz2Q_x67zRY1rR5SuNu3_4N8tJzpdcIWXNNcKbWT_arY8DQZ6tXkC95dlunpk4cASxwvfe6UMjgImiguDVQruT4h4Tm72Vk9-GBjV-pHp8_FlcWseBiZpqeMVkb0JLfwnW5gnyEZsvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقت :
یک سوال خودمونی :
تا الان نزدیک 50 نفر کانفیگ دریافت کردن
چرا حتی به خودشون زحمت ندادند یک لایک کنند ؟
این فرهنگ عجیب از کجا اومده ؟
اون لایکی که شما میکنید یک انرژی برای این تیم هست که شما دریغ میکنید .
😏</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/whitedns/1570" target="_blank">📅 06:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1568">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/PQy-rksqvUJ9NzFXmEM5RkTHIis_e3gin-glGYTHUYlrm7p0Dycx5R-5y8_-68NgRtEVLYIiaBuKVWnh54GJy4TD1gV1cHzvwaA4jZ-ur4IDDx90wakh-ChDmqYEajqSG9-3B57YmxASL1_MK2-QvlkqXh5eLidr3603255hwoMFCkxsYBAKCm-FmmCqxgtFtKO7v-W1zwVot-UNT1VDsy6InurK74ICATDxEgSTZ5L2YMGCD-dEI8AHTZY9ZXqLRZNPlcME5I-YbUj8PAKJDg6MAEP5FV2iQ_8qHyHy989e26h2-OCj648m1_QMPafQalUUe8iTMO2gqCuoX37P7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1568" target="_blank">📅 05:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1567">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد
PattNG
/
PattN
کرده و لذت ببرید !
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt
ساب هر ۲۴ ساعت آپدیت میشود.
///
توضیحات:
چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری و تست میکنند و سپس کانفیگهای سالم را فیلتر و در اختیار قرار میدهند پروژه‌ها‌ی
https://github.com/0xRadikal/Free-v2ray-Configs
و
https://github.com/itsyebekhe/PSG
و
https://github.com/Delta-Kronecker/V2ray-Config
هستند.
اما این پروژه‌ها دو مشکل اساسی دارند، اول اینکه تست کانفیگها باید از طریق اینترنت و فایروال ایران انجام شود ولی در حال حاضر تست کانفیگها در این پروژه‌ها از طریق گیتهاب انجام میشود، دوم اینکه روی نت‌های آپلود محدود (ایرانسل و ...) عملا اکثر کانفیگهای این پروژه‌ها آپلود محدود هستند و کیفیت بسیار پایینی دارند.
از آنجا که با روشهای زیادی میتوان محدودیت آپلود را روی کلودفلر دور زد، من در پروژه‌ی خودم اومدم کانفیگهای کلودفلر سالم را از پروژه‌ها‌ی اصلی جدا کردم و تغییراتی را برای دور زدن محدودیت آپلود (و همچنین دور زدن فیلتر دامنه) اعمال کردم (در حال حاضر متد fragment+fingerprint اعمال شده). بنابراین کانفیگهای نهایی سالم و با حداکثر سرعت در تمامی نتها قابل استفاده هستند.
برای دور زدن محدودیت آپلود در نتهای آپلود محدود در حال حاضر فقط باید از کلاینت
PattNG
/
PattN
استفاده کنید، بزودی در سایر کلاینتها نیز این مورد پشتیبانی میشود.
https://github.com/patterniha/Free-Configs</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/whitedns/1567" target="_blank">📅 03:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1566">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sANw3DAIj6LmzJMGu5zZgXeykJ_T-SYzWaPGuv0XmIS7LLaiDXoOxf0h4jmUsKkiX0MZJvbuu10UOznF9uCFbc0DAtvZ18JTWgjFGyWCxMWvfBvvf9sbg3-jzizgVbdmNo2utC5o-fLNpzYbXZ2kE3xBrqxISRDTZaFosguPQOVkj7KuNBSHjJTghYNuvi5YO1poO6S5L9OuVvbD0No_5HJRyKPanj1Yqpu8Rh07A5XvuiWb6goxpu4VPOCz4w3V5Yfsp8uF5OeGit5q_FHYNMVhlbsRkvwjfg1PJBroSfPgDLuqKmSdzzXa_r3MjJMFwOrNC0d8Dvq-Y6HfMS8U7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
WhiteDNS
مسیری که قبل از روزهای قطعی اینترنت شروع شد
تیم WhiteDNS از مدت‌ها قبل از قطعی‌ها و محدودیت‌های گسترده اینترنت فعالیت می‌کرد. از همان ابتدا تلاش کردیم ابزارها، سرویس‌ها و آموزش‌هایی بسازیم که رایگان و در دسترس همه باشند.
در این مدت افراد زیادی به این جمع پیوستند؛ بعضی ماندند و بعضی مسیرشان جدا شد، اما چیزی که ما را کنار هم آورد همچنان پابرجاست:
حرکتی جمعی برای دسترسی آزادتر به اینترنت.
تیم WhiteDNS تا امروز کاملاً مستقل و بدون هیچ منبع درآمدی اداره شده و تمام هزینه‌ها را خودمان پرداخت کرده‌ایم. با این حال، این مسیر را ادامه می‌دهیم و همچنان ابزارها و سرویس‌های رایگان بیشتری را با کمک همین جامعه خواهیم ساخت.
حالا تنها مسیر درآمدی ما کانال یوتیوب WhiteDNS است. اگر می‌خواهید از این حرکت حمایت کنید، کانال را سابسکرایب کنید و ویدیوها را ببینید. همین همراهی کمک می‌کند WhiteDNS مستقل، فعال و جامعه‌محور باقی بماند.
📺
https://www.youtube.com/@WhiteDNS
ممنون که بخشی از این مسیر هستید
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/whitedns/1566" target="_blank">📅 18:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1564">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bSV2mLCOrf9CSq3whxsukBeezb-K35uYa0dIxwbPh_tomI1LO45rruo3FPzPoJqxrk91_oyoCszqO68xGeO4Clm9F51405GjtK42KCuwdGxXDGxQ4QRpZUnU_y-0EbyjeNBgo5VbAiLJQKW7CxvJoXUUtv8NYlI4EzXVv1ukt-2JWBzyWw6WUVKEKBnj-RZEM-1k55Ba-PjXAM__d40n6oFK3Ep9RWqEXNp13hfnLnw62BWUEtdRfh5G4quXh0VfSzFhut_LOw6KohCUxliet5UZkoAqAqzkdBwO9ogg1sCFIliqLiY_jYNq8IHIpLgyHY1qDsqVjNPpgWSzakGf5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/whitedns/1564" target="_blank">📅 17:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1563">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/776e6fda95.mp4?token=mJ2OzkzRT7zo6N6BH602ksBGBTSNxeYs94G7VlwWNKHBI6mB5CJ3LfPTi5cAH2CHi4nJuZRYItH3ITFuv11fL4F18SY_ZiZ7MS-YMrxNElB9dfiglxJbWsBe7K-4iYC7bjFEIHUz_hwnKkDscVSglW2PsdgtpEBOv3oSax9zyBPgxrSGvG6sa9m9EAKGScoM-hmW2ikyUSO-_VxxAz4JW9UDNzpoj7bmAg6kyX1jGM7cUmidKsZqc52DBu6lXBeF0sTTgAItGBl6tMmUAXRBV9wTideoR1eK_erqTNgEVmiV0QlI2tBqMQD5zjjpIPnq4o4TXAT7XdIqNq1VX828rmcABzCne6P3aI59KW_PpKk9tkjUxmlF8EWU58QtOFc-mm7j1O6l5GkBBx4dwpZucicSXPYTSL27V3297nCQlXImRY7ATB7GvLPE5gzpodUJiW1ichN1eoEmaFEqU-0W3KOPv_FfHB61CyD2OEiUuuLxUf7ILmXBvqCX3AcoTQKvR-J0dg8KjXfvo9WP3o_e2POhciPIHGUZvq99Gl7ouKsi1Ad3wK-Kz4jm7b9oU1kxj7MaUHVmmrCOFbUh1j5qXNs72DR_scZSSB5tFGXe9_qfxS41i1RAQUl0D4yFODka45vh4q2n7IJGAhzCLerXe1o02ylf4YzuR99lz_2I8KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/776e6fda95.mp4?token=mJ2OzkzRT7zo6N6BH602ksBGBTSNxeYs94G7VlwWNKHBI6mB5CJ3LfPTi5cAH2CHi4nJuZRYItH3ITFuv11fL4F18SY_ZiZ7MS-YMrxNElB9dfiglxJbWsBe7K-4iYC7bjFEIHUz_hwnKkDscVSglW2PsdgtpEBOv3oSax9zyBPgxrSGvG6sa9m9EAKGScoM-hmW2ikyUSO-_VxxAz4JW9UDNzpoj7bmAg6kyX1jGM7cUmidKsZqc52DBu6lXBeF0sTTgAItGBl6tMmUAXRBV9wTideoR1eK_erqTNgEVmiV0QlI2tBqMQD5zjjpIPnq4o4TXAT7XdIqNq1VX828rmcABzCne6P3aI59KW_PpKk9tkjUxmlF8EWU58QtOFc-mm7j1O6l5GkBBx4dwpZucicSXPYTSL27V3297nCQlXImRY7ATB7GvLPE5gzpodUJiW1ichN1eoEmaFEqU-0W3KOPv_FfHB61CyD2OEiUuuLxUf7ILmXBvqCX3AcoTQKvR-J0dg8KjXfvo9WP3o_e2POhciPIHGUZvq99Gl7ouKsi1Ad3wK-Kz4jm7b9oU1kxj7MaUHVmmrCOFbUh1j5qXNs72DR_scZSSB5tFGXe9_qfxS41i1RAQUl0D4yFODka45vh4q2n7IJGAhzCLerXe1o02ylf4YzuR99lz_2I8KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یه آموزش خفن و کاملاً رایگان براتون داریم!
✨
اگه دوست دارید بدون هیچ هزینه‌ای با
پنل Netra
کانفیگ بسازید، این آموزش دقیقاً برای شماست!
💗
بدون هزینه
🎀
کاملاً رایگان
✨
آموزش مرحله‌به‌مرحله
🎥
آموزش کامل رو آماده کردیم و می‌تونید همین الان توی یوتیوب ببینید:
https://youtu.be/qluhGfGNbwk?si=oTLkVuC1z-5L03fy
💌
اگه آموزش براتون مفید بود، حتماً لایک کنید و برای دوستاتون هم بفرستید!
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1563" target="_blank">📅 15:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1560">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/B7Q3Z5497ah2lGvUQd7Weiuj8cecRh5DSixlMVLvCiN6mdPi8idzrQFCttlORGlkahX0SBfPJ1XwRJ_WWJlkUglpY_0y8UITNtNYF0dPzczPjC2JpPWWyXkMnuISYmLaUbfsdudQT-7xIPrNR7D47wV5IAp4Sywpx_ZnnMoZY9EepZxSMXngwZbf5bqzBTI1xy3TxRgado1e2U5Zb7GC2IAeCB9DIYqNeb6pTndkXmW7o-V-EAR0VgoCaP7p_plGXSJLypk6fobXdD7d5CjOIMVhqluLMf53FNvXlPzjG9PfqubBjFilhAm_hSmFS5M9I1PXeSpO9-id_88HhBXK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteVPN Desktop v1.0.18
زنجیره کردن اتصال (Connection Chaining)
از این نسخه می‌توانید ترافیک را قبل از رسیدن به اینترنت از دو سرور رد کنید.
اتصالی که در صفحهٔ وی‌پی‌ان انتخاب کرده‌اید هاپ اول می‌شود، و سروری که در تنظیمات به‌عنوان هاپ دوم انتخاب می‌کنید جایی است که ترافیک از آن خارج می‌شود.
چطور فعالش کنم؟ تنظیمات ← زنجیره کردن اتصال ← هاپ دوم
پیش‌فرض روی «خاموش — یک هاپ» است و اگر دست نزنید، همه چیز دقیقاً مثل قبل کار می‌کند.
چند نکته که خودِ برنامه رعایت می‌کند:
▪️
سرور هاپ دوم از فهرست هاپ اول حذف می‌شود، تا هر دو سرِ زنجیره یک ماشین نباشند و بی‌دلیل هزینهٔ دو هاپ را ندهید.
▪️
اگر هاپ دوم WireGuard یا Hysteria2 (یا هر پروتکل روی QUIC) باشد، فقط سرورهایی به‌عنوان هاپ اول پیشنهاد می‌شوند که بتوانند UDP را حمل کنند. زنجیره‌ای که هاپ اولش فقط TCP باشد ساخته می‌شود و وصل هم می‌شود، ولی هیچ ترافیکی رد نمی‌کند.
▪️
حالت Automatic همچنان کار می‌کند. اگر هاپ اول قطع شود، خودِ گروه جایگزینش می‌کند و نیازی به اتصال دوباره نیست.
▪️
اگر سروری که به‌عنوان هاپ دوم انتخاب کرده‌اید بعد از به‌روزرسانی اشتراک حذف شود، همان‌جا در تنظیمات به شما گفته می‌شود — نه وقتی که دارید وصل می‌شوید.
⚠️
توجه: دو هاپ طبیعتاً کندتر از یکی است، چون هر سرور باید ترافیک سرور بعدی را هم حمل کند. اگر سرعت برایتان مهم‌تر از لایهٔ اضافه است، همان یک هاپ را نگه دارید.
دانلود: ویندوز (x64 / ARM64) · مک (Intel / Apple Silicon) · لینوکس (deb / rpm / AppImage / tar.gz)
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1560" target="_blank">📅 16:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1558">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Sfs_fz0yx1G6tpIQntV6ePazkBtts8NQreziVcZFWdZHgyTm-iavWfJCvnUSFH5uiW2GRfjTF2cJlHcEHczPE2z2U__afmSnoczVUOWJ2EknLy50hrnNF34vZ2prK_267eFu6lSfJBJiaMnuKF3RtXdoGj72WMFW3uRXNju4A0yt6yZTZauqPf8n5y_DBoYwqECtMu8hqr4AjAo_kqv_ul2qyqO63ZvOsircCljXOqBc7iS0X13qZtLXZHDPPoGcq9KLDelw_C0KiKxj2nviMjp0PMfK50hBW4Nuc5r0yWAYlkGNXMCIT_At9n7tVOKXI_zovJnlmBSzuJmsyDtN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther Android ورژن جدید
🔥
🔥
🔥
🔥
🔥
نسخه ۱.۲.۱ — رفع سه مشکل اتصال
این نسخه قابلیت بزرگ جدیدی نداره؛ سه تا مشکل رو رفع می‌کنه که باعث می‌شد اپ روی خیلی از گوشی‌ها اصلاً وصل نشه. اگه ۱.۲.۰ داری حتماً آپدیت کن.
🛠
چی رفع شد
1
.پروتکل های wireguard و warp in warp برای خیلی از دوستان اصلاً وصل نمی‌شدن
توی ۱.۲.۰ «ثبت‌نام مشترک بین پروتکل‌ها» رو به‌عنوان یک بهبود اعلام کردیم. اون کار اشتباه بود: وقتی MASQUE هویت رو ثبت می‌کرد، کلید WireGuard روی سرور Cloudflare پاک می‌شد. بعدش هیچ اندپوینتی جواب نمی‌داد و اپ می‌گفت شبکه بسته‌ست — در حالی که مشکل از هویت بود، نه از شبکه.
حالا هر پروتکل هویت خودش رو داره. اگه از ۱.۲.۰ آپدیت کنی حسابت از دست نمی‌ره.
⚠️
در عوض، اون کاهش سه‌برابری احتمال rate limit هم برگشت. اگه زیاد نصب و حذف می‌کنی، حتماً از
Settings ← Identity & access
یک بار بکاپ هویت بگیر.
۲
. عوض کردن پروتکل وسط اتصال، همه‌چیز رو خراب می‌کرد
اگه بدون قطع کردن اتصال پروتکل رو عوض می‌کردی، جستجوی اندپوینت از داخل همون تونل قبلی رد می‌شد — یعنی هزاران درخواست دقیقاً به جایی می‌رفت که قرار بود جایگزینش کنه. نتیجه: هیچی وصل نمی‌شد.
۳
. گیر کردن روی پروتکلی که شبکه‌ات بسته
پیش‌فرض قبلی H3 بود که روی UDP کار می‌کنه. اگه شبکه UDP رو بسته بود تلاش اول شکست می‌خورد و اپ دوباره همون رو امتحان می‌کرد. تا نوبت MASQUE H2 برسه چهار دقیقه و نیم گذشته بود، و عملاً هیچ‌کس این‌قدر صبر نمی‌کنه.
✨
چی جدیده
حالت Automatic — از
Routes ← Manual ← Protocol
گزینه اول حالا Automatic هست و پیش‌فرض هم شده. خودش سریع امتحان می‌کنه ببینه شبکه‌ات چی رو اجازه می‌ده، از H2 شروع می‌کنه (چون TCP روی پورت ۴۴۳ هست و شبیه HTTPS معمولی دیده می‌شه)، و هرچی جواب داد رو یادش می‌مونه تا دفعه بعد از همون شروع کنه.
روی نصب تازه: ۱۴ ثانیه تا اتصال، جایی که قبلاً چند دقیقه طول می‌کشید.
گزارش خطای واقعی — قبلاً اگه جستجو نتیجه نمی‌داد فقط می‌نوشت «اندپوینتی پیدا نشد». حالا می‌گه چرا: بسته‌ها از گوشی خارج شدن و جوابی نیومد (مشکل از شبکه‌ست)، یا اصلاً خارج نشدن (مشکل از مسیریابی خود گوشیه). لاگ خود موتور تونل هم از این نسخه داخل
Settings ← Diagnostics
هست — اگه مشکلی خوردی همون گزارش رو بفرست.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/whitedns/1558" target="_blank">📅 14:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1557">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ufB0rtA-Hesvx1XAX2lZ-G5-3A5l-TiO6lcK2iujaYtCco6S1_4ZA-eZS9E57PTLzpGSS2cZ-DURrn1J9yEH82hCbBOCpYz6b8rcN2bmfu6dsoirp-WklVVc3g2ZLr41W8_7I2HFPiFxke3ubZZsa84mLBqV8tZuj7Pgg6eitJ78D9L2ASMaACmRl-FaqPsgKd9_h5WbOumg_3AlDaWEPtSdlHBSPwYwsV0p_A4bFVluA9rj810xYExaBvaIYBZyzD2xnPYRseDHuOyc4WMWa3VmMS-wt0zAjzSwsaXa0go4TX6eu3q9GGyOldp8cd-X7z_a4hJDhUWiwVeVpUStHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/whitedns/1557" target="_blank">📅 14:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1556">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VYFbH2mA6HqiAKlvDscpA-DddtvcVoM-0DmBPSBEjY5HYqxC6KSxpJlJPDIQ5mYjPMjlo2voFF3jSVlu-zaoE8na3zg5cXWsIB2sanyvhERyxqw5BtHzEViAeAjZQEQDUY0PBOu3Rh2P5syqgF00wNrZYFTBnn0pI80lVL8QqYFuB17OdQX85QW-apX7ZXSr50tF-0QZpA6B6t0tY4IRKrmEtNub5ngdo0RXITW3sLQbHz2thhJZaBjR-5TFCdBijzu05ZCSy5KAaFqlJimq5qeM5JZb0wdnpDiFDMc_3oFYMKz9LoUhhjAXiPwgOwPibu22wQSCx7XK2vV_aQF-QA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/whitedns/1556" target="_blank">📅 14:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1555">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyOc1cpOtlHAQCvdoMXkhcDub1kvWE2jgey4jvBYvURUbVSmbtc8-OGnU5-beQxbSfhJ7vpzhDn4CbLJCJMevB8j1JJHj471sYNuUOvWEMgtt9aGUkKLCvxFAz7n7oHJUUBOy64df6aEsDoANnwei1LEKfaoB5bGu_g1dlOiwu4LsVV8QHvwVwKeipXFBwBO-WK9OQmazjDSJh_Q1RvVJFULt9TF-4i2nYeEbw_c5qgUm-KRA4IokSd3FHeeyUWt85fiGVefQFjuvPwYaS1qK_lcrDngzOUAw5A4_cb0hywUcPIjdzuYtTH5Qeq8Mx2-ADjKu8SPARdMxphXSmyiWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
WhiteDNS
مسیری که قبل از روزهای قطعی اینترنت شروع شد
تیم WhiteDNS از مدت‌ها قبل از قطعی‌ها و محدودیت‌های گسترده اینترنت فعالیت می‌کرد. از همان ابتدا تلاش کردیم ابزارها، سرویس‌ها و آموزش‌هایی بسازیم که رایگان و در دسترس همه باشند.
در این مدت افراد زیادی به این جمع پیوستند؛ بعضی ماندند و بعضی مسیرشان جدا شد، اما چیزی که ما را کنار هم آورد همچنان پابرجاست:
حرکتی جمعی برای دسترسی آزادتر به اینترنت.
تیم WhiteDNS تا امروز کاملاً مستقل و بدون هیچ منبع درآمدی اداره شده و تمام هزینه‌ها را خودمان پرداخت کرده‌ایم. با این حال، این مسیر را ادامه می‌دهیم و همچنان ابزارها و سرویس‌های رایگان بیشتری را با کمک همین جامعه خواهیم ساخت.
حالا تنها مسیر درآمدی ما کانال یوتیوب WhiteDNS است. اگر می‌خواهید از این حرکت حمایت کنید، کانال را سابسکرایب کنید و ویدیوها را ببینید. همین همراهی کمک می‌کند WhiteDNS مستقل، فعال و جامعه‌محور باقی بماند.
📺
https://www.youtube.com/@WhiteDNS
ممنون که بخشی از این مسیر هستید
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1555" target="_blank">📅 10:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1553">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">WhiteAesther V1.2.0    دو پروتکل جدید، رفع مشکل قطعی، و مسیریابی اپ به اپ  از این آپدیت سه تا قابلیت جدید اضافه شده و سه تا مشکل قدیمی رفع شده. همه‌شون رو اینجا خلاصه کردم.
✅
چی اضافه شد  ۱. دو پروتکل جدید: WireGuard و WARP in WARP  تا الان فقط MASQUE (روی…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1553" target="_blank">📅 09:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1552">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmdwbz49GhA89fWeFMyF71S3GmKqqCosuM5zOOz4YHN0z4zeUYJysgXCyzw0NZo2xw5RfqomcNvGdPzyWY9KwKMGsaFFFcxku7gSsAGKdb0wobBgoAQcZy4diqUWEg2j5sTDvp3aqpVa07qi6GeSLckPKp1NrSf8Y0ywN7xS4qeo_ToprTRhMrAaHUvhtipOgWSfG8-7bXMO80kknRq68qpSZTwfJKFJw2mK4YiiCwFag2UY9q_jXqjFds-ln-Awg4kEhgfDsvrA9waKELLSombWIJjRMPxOEHQ07nxC17k_6U_L73Lv-20R4CrIi5uzRmtG44342NqSUpVg-_ju4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان عزیز
✍️
از دیروز گزارش های زیادی روی WhiteVPN روی گوشی های قدیمی گرفتیم که بهمون گفتید نصب نمیشه، یا نصب میشه ولی میزنید روی اتصال، اررور میگیرید.
ما سعی کردیم توی ورژن ۱.۶.۱ که از لینک زیر میتونید دانلود کنید این مورد رو حل کنیم.
حالا گوشی های اندروید قدیمی‌تر هم میتونن بدون دردسر وصل بشن.
همچنین مشکل کانکشن هایی که camouflage داشتند هم توی این ورژن حل شده.
تغییر دیگه،ای نداشتیم  جز این دو مورد.
دانلود آخرین نسخه
https://github.com/WhiteDNS/WhiteVPN/releases/latest
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1552" target="_blank">📅 06:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1550">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJMIXFZ_w_LAwmZRzWIk1tVSI96RcxGTzaJcxaGNn28SbR6rWU5I8SvNZmvibv4DzMBNSN6RJl6f8PU4odRZRh4yJXT1fVUZlXQ7nmNqEQSt9TBqIDHL-bhmimFFKdlxvrUomarZEQaNLugnzLzGpFdXAFP256AMVEy2Vv0j5z99ik3i_kCI_jKrd7nIjqJrHvOKLhbwTTFw3-MtxV2Q0ffYyV53s0_iNdGsE36efr-rDmOACs1OIYXO1-vycWfMas3mXKMh49L3XZ-xY_69mzxFZdyNy2NPUU6A4WrUqX58Y_gb8kNYMme3NBrATnluLZ0eQtKc5DlClBcXOmMGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8KAeeuORGwx5wp75e7Qztc-n03HR4Abkb7OhhRHoPjr62ARtWixbkjeGPvXs-Tdcfy0RkmyzFuh7ttiqpTXbSsIHsN_1EgYb1qzTAH2D_lAi_jlzfU78x51-LRzWl-TIlTQIwhguuWbenFNL7xZjY-CIxEJJNtjh3oNg3I1Q0w2abufqf_Dt8pjbTVlVO-VHEVJXfVnqAly-MBQ2Z-DxkjQoLCZ-hg0qMrp2Je4MV7Jt_mxKV4-gDap7_0oqgneN0cZTcdDv4MCNqigkf7y_nmFCuAgut9hE5-QemuPncBbzHSC85uKN2uLeunzUhQ4S_dQH3aTWA_FxI3wN1hpNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان عزیز
لینک ساب رو باید بعد از کلیک کردن روی دکمه Raw مشابه به عکسی که گذاشتیم کپی کنید.
لینک
صحیح WhiteDNS Sub
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/1550" target="_blank">📅 05:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1548">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCore Forge</strong></div>
<div class="tg-text">🚀
CoreForge Build آپدیت جدید منتشر شد
https://testflight.apple.com/join/DRkT6zny
این نسخه یکی از بزرگ‌ترین آپدیت‌های CoreForge تا امروز محسوب میشه.
از Build 90 تا Build 100 طی حدود ۲۰ روز:
• 214 Commit
• بیش از 411 فایل تغییر کرده
• بیش از 86,000 خط کد جدید اضافه شده
• چند Engine و Protocol جدید از پایه اضافه شده
• بخش بزرگی از سیستم Connection، Routing، Failover و Config Management بازطراحی شده
###
🧩
پروتکل‌ها و Engineهای جدید
🔹
OpenVPN
* پشتیبانی مستقیم از فایل‌های .ovpn
* UDP و TCP
* AES-GCM / AEAD
* AES-CBC برای بعضی سرویس‌های قدیمی‌تر
* TLS-Crypt
* Multi-Remote / Multi-Address
* Username / Password
* Client Certificate
* OpenVPN Subscription
* پشتیبانی بهتر از ProtonVPN، VPNGate، SoftEther و کانفیگ‌های مشابه
🔹
Tailscale
* اتصال مستقیم به Tailnet
* انتخاب Exit Node
* MagicDNS
* مدیریت Account داخل CoreForge
* امکان اتصال به Exit Node حتی بدون انتخاب Config معمولی
🔹
Cloudflare WARP / MASQUE
* WARP به‌عنوان یک Outbound واقعی
* MASQUE روی HTTP/2 و HTTP/3
* امکان استفاده داخل Chain
* WARP Endpoint Scanner برای پیدا کردن Endpoint بهتر
* تست Endpoint با handshake واقعی MASQUE، نه فقط TCP Ping
🔹
mKCP
* پشتیبانی از mKCP مربوط به Xray
* همه Header Typeهای اصلی
* قابل استفاده با VLESS و Trojan
🔹
ECH
Encrypted ClientHello حالا به صورت واقعی داخل CoreForge اجرا میشه و برای بعضی Transportها از جمله Hysteria2 هم اضافه شده.
###
⚡
Load Balancer و Failover
Load Balancer فقط اسم نیست و حالا Connectionها واقعاً بین Nodeهای انتخاب‌شده مدیریت میشن.
همچنین:
* Config فعال داخل برنامه نمایش داده میشه
* Exit IP بعد از تغییر Node آپدیت میشه
* Dead Server Detection سریع‌تر شده
* Backup Node از قبل آماده نگه داشته میشه
* اگر Config فعلی از کار بیفته، CoreForge می‌تونه بدون Disconnect کامل به Backup منتقل بشه
* Backup Pool بعد از Failover دوباره پر میشه
###
🌐
Routing
سیستم Routing هم تغییر زیادی کرده:
* Routing Profile شبیه Shadowrocket
* Rule Actions
* Iran Direct Preset
* Iran 2026 Rules
* category-ir
* Import کردن Routing Rules از فایل
* Fragment به‌عنوان Routing Target
###
📂
Configs و Subscriptionها
مدیریت Configها تقریباً کامل بازطراحی شده:
* Swipe برای Ping / Edit / Share / Delete
* Drag & Drop برای مرتب کردن Sectionها
* Groupهای Local
* Bulk Actions
* forge:// Chain Links
* Tap-to-Ping-and-Connect
* Import QR Code از داخل عکس
* Subscription Folder
* Rename / Reorder / Export
* Auto Update جداگانه برای هر Subscription
* Plan Status
* تقویم شمسی
مشکل فایل‌های OpenVPN بزرگ هم برطرف شده؛ برای مثال اگر یک فایل شامل ده‌ها یا صدها Profile باشه، دیگه همه‌ی اون‌ها به‌عنوان یک Config خراب Import نمیشن و Profileها جدا میشن.
###
🔧
Fixهای مهم
در این نسخه تعداد زیادی Bug مهم هم برطرف شده، از جمله:
* Crash روی تعداد زیاد Config
* مشکل Import بعضی لینک‌های VMessAEAD
* مشکل gRPC پشت Cloudflare
* مشکل XHTTP که Connect می‌شد ولی Traffic عبور نمی‌کرد
* مشکل REALITY و extra
* اصلاح UUIDهای VLESS
* Lag شدید Config List
* Writeهای اضافی Keychain
* آپدیت نشدن Connection Details بعد از Failover
* UDP برای VMess، Shadowsocks و SOCKS
* UDP Associate برای Trojan
* gRPC MultiMode
* pinnedPeerCertSha256
* PattNG Fragment / Cipher Suite / Unsafe Fingerprint
###
📱
iPad و UI
* پشتیبانی بهتر از Stage Manager
* Split View
* Resizable Window
* تغییرات Liquid Glass
* اصلاح Light Mode
* بهبود Tab Bar و Headerها
---
⚠️
نکته مهم درباره Build
این نسخه تغییرات خیلی زیادی داشته و طبیعتاً
۱۰۰٪ تضمین نمی‌کنیم که تمام قابلیت‌های جدید روی تمام Serverها، ISPها و Configها بدون مشکل کار کنند.
بعضی قابلیت‌ها هنوز در مرحله‌ی تست واقعی توسط کاربران هستن و ممکنه روی یک Server عالی کار کنن ولی روی Server یا Network دیگه Fail بشن.
به‌خصوص قابلیت‌های جدیدی مثل:
Tailscale / WARP / OpenVPN / ECH / Chainهای پیچیده / بعضی حالت‌های VLESS و REALITY
هنوز نیاز به تست گسترده روی Serverها و اینترنت‌های مختلف دارن.
پس اگر چیزی Connect نشد یا Connect شد ولی Traffic نداشت، حتماً گزارش کنید و در صورت امکان Config، Log و نوع اینترنت رو هم بفرستید.
Build بیشتر از اینکه «نسخه نهایی بدون باگ» باشه، یک جهش بزرگ برای CoreForge ـه و Feedback شما مستقیم روی Fixهای نسخه‌های بعدی تأثیر می‌ذاره.
🛠️
CoreForge Build
⚒️</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1548" target="_blank">📅 15:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1545">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/heKlTbu022iqPtrT21piIIEXqEPg83ATNOpRpMbzQJEZu4D25hZZwtqP1eiuq-5v22fYgiOQxb5mKdvfFq4gqHfPGWgdj8cFJRnUbpWQcuhN2Bv7k29l3T-j04WNQyqJ3lmcj-jwXwuU4fuYePQyzIOkdsTZd95IinjVo6ojj-dkBx3lNX6LMEJqX6ev-LsPJN4jN0u2HuvU8U0iWYTiFOrjWrOrmkQfbgaH9Jg-bqXzRnFHDYSWM1sCTadP4muZtgGuTdbGDqWGXly1lKyl42WRBWPuWDswkk8Taa4IX9zAAtexEeYxSGCUkPU1Rhh2GuYgSP-HXXZVvqhxh_YisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther
V1.2.0
دو پروتکل جدید، رفع مشکل قطعی، و مسیریابی اپ به اپ
از این آپدیت سه تا قابلیت جدید اضافه شده و سه تا مشکل قدیمی رفع شده. همه‌شون رو اینجا خلاصه کردم.
✅
چی اضافه شد
۱. دو پروتکل جدید: WireGuard و WARP in WARP
تا الان فقط MASQUE (روی H3 یا H2) داشتیم. حالا از Routes ← Manual ← Protocol می‌تونی این دو تا رو هم انتخاب کنی:
▫️
WireGuard —
سریع‌تره، ولی روی UDP کار می‌کنه
▫️
WARP in WARP —
یک تونل داخل تونل دیگه، کندتر ولی شناسایی‌ش سخت‌تره
⚠️
هر دوی این‌ها UDP هستن. اگه شبکه‌ات UDP رو کامل بسته باشه (مثل همراه اول این چند وقت اخیر) اصلاً وصل نمی‌شن — اونجا MASQUE H2 که روی TCP کار می‌کنه انتخاب درسته.
۲. بکاپ هویت — راه‌حل قطعی مشکل «چند بار نصب کردم دیگه وصل نمی‌شه»
دلیل اون مشکل این بود که هر نصب، یک هویت تازه از Cloudflare می‌گرفت، و بعد از چند بار ثبت‌نام از یک آی‌پی، دیگه هویت جدید نمی‌داد. حالا می‌تونی هویتت رو قبل از حذف اپ ذخیره کنی و بعد از نصب مجدد برگردونی.
۳. Split tunnel — انتخاب اینکه کدوم اپ‌ها از تونل رد بشن
از Traffic ← Apps: همه اپ‌ها، فقط چندتا اپ خاص، یا همه به‌جز چندتا اپ خاص (مثلاً بانک یا اپ‌های داخلی).
🛠
چی رفع شد
▫️
ثبت‌نام مشترک بین پروتکل‌ها — امتحان کردن هر سه پروتکل قبلاً ۳ بار ثبت‌نام می‌خرید. حالا یکی مشترکه.
▫️
WireGuard و WARP in WARP دیگه روی "trying" گیر نمی‌کنن — از تا ۹ دقیقه بی‌نتیجه، به معمولاً چند ثانیه.
▫️
باگ ساب عوض‌شده که نودهای قدیمی رو نشون می‌داد — درست شد.
📌
آموزش: Split tunnel
۱) Traffic ← Apps
۲) یکی از سه حالت: All apps / Only these apps / All except these
۳) با سرچ اپ‌های موردنظر رو پیدا کن و سوییچشون رو بزن
برای بانک یا اپ داخلی: All except these بزن و همون یکی دو تا رو انتخاب کن.
📌
آموزش: بکاپ هویت
Settings ← Identity & access → Save a backup (قبل از حذف اپ) / Restore from a backup (بعد از نصب مجدد)
⚠️
این فایل مثل رمز عبوره، رمزگذاری نشده — جایی نگهش دار که رمز عبور نگه می‌داری.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1545" target="_blank">📅 12:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1535">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4qsg5KAgjeHKuvikoyfGPx3lYbY6XYETe2mWQWiBHo7DbippkWBOMGmEtL_a6mgEvucaMO78YCox3TwWf2SpL7coEZecZ-Dbgcx217PaALKzOU-RjPHwjl5qpnGtZoWIPMh83Guvg3jQFW1NvHquz7Q9vvvJj3RUkCEduisJvnTU8L-oI5w790dQ-rnR5I87mHBDrb1UeHSrplbDciu4oX3dUo8vg8VcTWjbi6qhobTryDJptVXa8I53EGnoPEkrLU10fu9gjEfvP0W9WYpjKXLX4NgUq5uPUt-PTO1Ng05C9TZifCTvIGvxqcTOOcyRwmDoUWxy9EOebk43tASKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN v1.6.0 منتشر شد
🚀
یکی از بزرگ‌ترین به‌روزرسانی‌های WhiteVPN آماده است؛ با امکاناتی که اتصال‌ها را قدرتمندتر، انعطاف‌پذیرتر و قابل‌کنترل‌تر می‌کند:
📺
پشتیبانی کامل از Android TV
🔗
زنجیره کردن دو اتصال برای امنیت و انعطاف بیشتر
🛡
پشتیبانی از
AmneziaWG v3
و تنظیمات پیشرفته WireGuard
📥
وارد کردن مستقیم لینک‌های
Hysteria2
و
WireGuard
⚡
تست اتصال‌ها از تمام سابسکریپشن‌ها
🌐
بهبود سازگاری، پایداری و رابط فارسی
اگر از WhiteVPN استفاده می‌کنید، همین حالا به نسخه
۱.۶.۰
به‌روزرسانی کنید.
این نسخه با کمک بازخوردهای شما ساخته شده است. اگر مشکلی دیدید یا پیشنهادی داشتید، حتماً در گروه با ما در میان بگذارید.
🤍
WhiteVPN v1.6.0 — دو مسیر، یک اتصال قدرتمندتر.
📥
Github Release
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.0</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1535" target="_blank">📅 09:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1534">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از این به بعد کانفیگ های بیشتری داخل ساب ما خواهد بود.
هر ۳۰ دقیقه بیشتر از ۲۲۰هزار کانفیگ جدید تست میشن و خروجی اونها بین ۲۰۰۰ تا ۳۰۰۰ کانفیگ با کیفیت و سریع خواهد بود.
تعداد کانفیگ های حاضر: ۳۳۵۳
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/1534" target="_blank">📅 07:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1531">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">https://github.com/iampedii/whitedns-sub
لینک ساب برای استفاده در برنامه های white</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1531" target="_blank">📅 18:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1528">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👆
whiteAesther  android V1.1.0
در این نسخه از اپ اندروید شما میتونید با  قرار دادن یک کانفیگ ای پی خودتون را ثابت کنید و احتمالا خیلی از مشکلات مربوط به Gemini , Chatgpt و بقیه هوش مصنوعی ها و وبسایت هایی که روی لوکیشن حساس هستند  حل خواهد شد
نکته  خیلی مهم برای نسخه اندروید :
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
بسته به نوع کانکشن و موارد دیگر ممکن هست 1-5 دقیفه بار اول طول بکشه که شما موفق به اتصال بشید . ولی در دفعات بعدی این موضوع خیلی سریع خواد بود .</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1528" target="_blank">📅 17:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1527">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">WhiteAesther
android V1.1.0
🔥
🔥
🔥
🔥
🔥
🔥
قابلیت Exit Chain
از این نسخه می‌تونی بعد از تونل، یک ایستگاه دوم اضافه کنی.
یعنی چی؟ تا الان ترافیک تو از سرورهای Cloudflare بیرون می‌رفت و سایت‌ها آی‌پی Cloudflare رو می‌دیدن. حالا می‌تونی سرور شخصی خودت (یا سابسکریپشنی که داری) رو آخر مسیر بذاری، و سایت‌ها آی‌پی اون سرور رو ببینن.
مسیر ترافیک این شکلی می‌شه:
گوشی ← تونل رمزنگاری‌شده ← سرور خودت ← اینترنت
به چه دردی می‌خوره؟
▫️
سایت‌هایی که آی‌پی‌های Cloudflare رو بلاک کردن (بانک‌ها، بعضی سرویس‌های خارجی، بعضی بازی‌ها)
▫️
وقتی به آی‌پی یک کشور مشخص احتیاج داری
▫️
و مهم‌تر از همه: اگه شبکه‌ات اصلاً تونل رو بلاک کرده، می‌تونی تونل رو دور بزنی و مستقیم از سرور خودت استفاده کنی
پروتکل‌های پشتیبانی‌شده: vless vmess trojan shadowsocks hysteria2 و بقیه — چه لینک سابسکریپشن، چه کانفیگ تکی که دستی می‌چسبونی.
📌
آموزش — ۵ قدم
۱) اپ رو به نسخه ۱.۱.۰ آپدیت کن.
۲) برو به تب Routes ← گزینه Exit chain.
۳) کلید Exit chain رو روشن کن.
۴) توی کادر Add a subscription لینک سابسکریپشنت رو بذار و Add رو بزن. اگه فقط چند کانفیگ تکی داری، از Paste nodes by hand استفاده کن — هر کانفیگ توی یک خط.
۵) برگرد به Home و وصل شو. تمام.
⚠️
سه نکته که حتماً باید بدونی
۱. لیست سرورها فقط بعد از وصل شدن میاد
قبل از اتصال قسمت Nodes خالیه و این ایراد نیست. سابسکریپشن تو از داخل تونل دانلود می‌شه تا شبکه‌ات نفهمه داری چی می‌گیری. پس اول وصل شو، بعد برگرد به Routes ← Exit chain تا لیست سرورها رو با پینگ‌شون ببینی.
انتخاب سرور قطع و وصل نمی‌خواد — روی همون اتصال جابه‌جا می‌شه.
۲. گزینه Dial nodes through the tunnel
پیش‌فرض روشنه و بهتره روشن بمونه: شبکه/اپراتور تو هیچ‌وقت آدرس سرورت رو نمی‌بینه، و سرورت هم آدرس واقعی تو رو نمی‌بینه.
🔸
ولی اگه اپ اصلاً وصل نمی‌شه یا خیلی طول می‌کشه، این گزینه رو خاموش کن. اون‌وقت WhiteAesther تونل رو کامل رد می‌کنه و مستقیم به سرور خودت وصل می‌شه — دقیقاً برای شبکه‌هایی مثل همراه اول که تونل رو می‌بندن، همین حالت جواب می‌ده و خیلی سریع‌تر هم وصل می‌شه.
۳. Coverage باید روی Whole device باشه
توی تب Traffic. اگه روی Proxy only باشه، Exit chain کار نمی‌کنه و اپ بهت تذکر می‌ده.
💾
حجم اپ بیشتر شده
از حدود ۸ مگابایت رسیده به ۴۷ تا ۵۷ مگابایت. دلیلش موتور جدیدیه که این قابلیت رو اجرا می‌کنه. اگه Exit chain رو روشن نکنی، اپ دقیقاً مثل قبل کار می‌کنه.
▫️
arm64-v8a — تقریباً همه گوشی‌های ۲۰۱۷ به بعد. از این شروع کن
▫️
armeabi-v7a — گوشی‌های قدیمی‌تر و اقتصادی
▫️
universal — اگه مطمئن نیستی (حجمش سه برابره)
⬇️
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
اگه مشکلی خوردی، از Settings ← Diagnostics گزارش بگیر و بفرست — از این نسخه لاگ موتور Exit chain هم داخلشه.
@whitedns</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1527" target="_blank">📅 17:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1526">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📺
خبر خوب برای کاربرهای Android TV
در ورژن بعدی WhiteVPN پشتیبانی کامل از Android TV اضافه شده. تا فردا نسخه جدید اپ اندروید هم ریلیز میکنیم
❤️</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1526" target="_blank">📅 17:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1525">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👆
whiteAesther V1.5.2 desktop
در این نسخه از اپ دسکتاپ شما میتونید با  قرار دادن یک کانفیگ ای پی خودتون را ثابت کنید و احتمالا خیلی از مشکلات مربوط به Gemini , Chatgpt و بقیه هوش مصنوعی ها و وبسایت هایی که روی لوکیشن حساس هستند  حل خواهد شد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1525" target="_blank">📅 16:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1524">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">whiteAesther
V1.5.2 desktop
🔥
🔥
🔥
🔥
🔥
🔥
🔗
قابلیت جدید: Exit chain (زنجیره‌ی خروج)
🔥
🔥
🔥
تا حالا وقتی وصل می‌شدید، ترافیک‌تان امن و رمزنگاری‌شده بود — ولی آدرسی که سایت‌ها می‌دیدند همچنان نزدیک خودتان بود. این ایراد ما نبود: WARP کلادفلر عمداً کشور شما را عوض نمی‌کند، از نزدیک‌ترین نقطه خارج می‌شود و همان‌جا را هم geolocate می‌کند. برای همین خیلی‌ها بعد از اتصال موفق، باز هم به سرویس‌های خارجی دسترسی نداشتند.
Exit chain یک هاپ دوم اضافه می‌کند. ترافیک اول از تونل رد می‌شود، بعد از داخل تونل به نود خودتان می‌رسد و از آنجا وارد اینترنت می‌شود. آدرسی که سایت‌ها می‌بینند، آدرس نود شماست.
دو نکته‌ی مهم در طراحی:
▫️
نود از داخل تونل شماره‌گیری می‌شود — یعنی شبکه‌ی محلی شما فقط یک اتصال عادی به کلادفلر می‌بیند، نه آدرس نود و نه SNI آن.
▫️
به همین دلیل، نودی که از ایران فیلتر شده باز هم کار می‌کند — چون از شبکه‌ی کلادفلر به آن وصل می‌شویم، نه از اینجا.
━━━━━━━━━━━━━━
📘
آموزش
۱. بالای پنجره روی Advanced بزنید، از منوی سمت چپ Exit chain را انتخاب کنید.
۲. دو کلید را روشن کنید:
• Route through a second hop — خود قابلیت
• Dial nodes through the tunnel — پیش‌فرض روشن است، همین‌طور بگذاریدش
۳. نودتان را اضافه کنید، به یکی از دو روش:
• Subscriptions — لینک ساب را بگذارید و Add بزنید (خودش به‌روز می‌ماند)
• Configs pasted by hand — کانفیگ‌ها را خطی یکی paste کنید و Apply بزنید
vless · vmess · trojan · ss · hysteria2 · tuic همه مستقیم پشتیبانی می‌شوند؛ لازم نیست چیزی را تبدیل کنید.
۴. پایین صفحه در بخش Nodes نودها ظاهر می‌شوند با پینگ واقعی‌شان از پشت تونل. با Test هر کدام را بسنجید و با Use یکی را انتخاب کنید.
۵. بالا سمت راست Save profile را بزنید تا دفعه‌ی بعد هم فعال باشد.
━━━━━━━━━━━━━━
⚙️
کدام حالت را انتخاب کنم؟
• Whole machine — کاری لازم نیست، پروکسی سیستم خودکار روی زنجیره تنظیم می‌شود. برای اکثر کاربران همین درست است.
• This app only — مرورگر یا برنامه‌تان را روی آدرسی که در همان کارت نوشته شده تنظیم کنید (معمولاً
127.0.0.1:1820
).
برای اطمینان، کارت What websites see در صفحه‌ی اصلی آدرس واقعی خروجی‌تان را نشان می‌دهد. اگر برچسب Through your node را دید، زنجیره برقرار است.
@whitedns
https://github.com/WhiteDNS/WhiteAesther</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1524" target="_blank">📅 16:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1523">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tcFRAbw5I2x6_zAcfpIdHPxegu137yoNnSa1bJxjjwedbT4rw_nEDC8YUTmte6_WYhzL-1GjTaRwly4W3pC-b22-cZutNxPVLDmHSoohyNwJ6TGI71JbR3MM1ArA_WYyoUcOPZQe4aZmrLHG9KuJT42NEVYsBLBiAwRyhaCekze-OvqgzcWzUbTAgy3h8Hwrj7x_8oga2PxYsJxRFP5hF7XJfVAIeTZTvm-UFgK04RMCq_Duja6FuO2nYMSDe56E168M7G_H3wpBtCJYDMD5z__EmfQ7ONPXhVZaeDoKYzbyHnXLfww8TfQ8MmygPDgw_f0V4EuBzzTvKY9oRio1XQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/whitedns/1523" target="_blank">📅 16:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1522">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qBdvjHtcvDpEuJY2ltucuUoEQo1-Lm8J2rOGUFhrYlJk9n0xhvdR1vlhKkeuTi_9zIWKv0Hqku_nl-YDiZk0fL6RMnagPQRRSwiLVXOFusZ-P8ggupcElmUpM3fhWfOaSQcAMQcyORmyE1SWTIc3B_8Skg5b8hqx6e6sY681pbgMNSfkufrYWZCVE_KvaawWG6UkAVUBM8MSUGHbS2DWmrjLCTd28b2u7Nzhgd0X-Qsg3LeTDOmgO2HNYZDCIyb0tLdHwSWiV70WeaB6zh1SIixRm_BXpDSv70C22VTnnFCN7sfz8k-nW9xTcfWcCFse0MBcyoFugcKZAV56z_04IA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1522" target="_blank">📅 16:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1521">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pruoB9Rm6kGpwZg6OKPsn4DmgnzLNoqHX3seyF_RcITFFE__pP1kZ7e5WOCLN_j1naorA1X4oFG3BHml26okBRDhfGhT5wwk61Mwhl3E9sQaSR315j1XU7yPq3CCGQlLffL80HxkZ85FjqCJS1l8RcwShQZFLRLu2VrqUnMjg-QjRHsDjJiWgO_9Oc5Bep303UvIt9N6sg9zeI4-4Kkb2w6PKWkYpcR6JKu8EG6l2m7TljJ-g-MQK6DS6qWR-GdCEfwwnYkcEd7uOtaCycSWfRXKfK0TvjOTiVyBrFsSgl7My4Un_raQrptwhQbA8ngXoyO1mC7i3du9hfxm6MmwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏯️
آموزش کامل اپلیکیشن WhiteAesther
📍
تماشا در یوتیوب
https://youtu.be/cRfqxbDY1Dg</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/whitedns/1521" target="_blank">📅 18:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1518">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0  توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.   حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/1518" target="_blank">📅 14:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1517">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">آموزش نصب پنل رایگان StanNg روی Railway
بدون VPS و بدون هزینه کانفیگ V2Ray بگیر
🔥
از صفر تا صد کامل توضیح دادم، مناسب تازه‌کارها هم هست.
لینک ویدیو:
https://youtu.be/sdiGXCDsDvQ
سوالی داشتی بپرس
👇</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1517" target="_blank">📅 11:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1515">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌎
نسخه جدید WhiteVPN v1.5.0
👆
تغییر های این ورژن کاملا روی فیدبک های شما بوده، و به نظرم از لحاظ تجربه کاربری تغییر خیلی خوبی داشتیم.
😆
ممنون از فیدبک هایی که به ما میدید.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1515" target="_blank">📅 08:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1510">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1510" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/whitedns/1510" target="_blank">📅 08:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1509">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imZeG5Ygdoe73ADA4pcZpCM-_afzU0y39ALiEYacz0ijAfdir6ZDudO7sFxUriPgX4_SKf84pNRsCvkBbsER0thbcPnI-TWh93ALVaL8J6lw-kKbqI2V3Q8gw9SH2Nl55445HRI0VuNIvsjkm2dZjaNNel1FEsMYFKyGpNhY6rnhAFRxdEpxkhW8PJsuZ3Q9McAdM7BKIE66tBSx7CmwXiIk6qKNc2uNgJV8eM4B7v2T64oecyHfIPm3TJaud1sQZe0VmgQVicl4pPg7QD3JnO2wTgENDcnIaHWAiPG5RwcPJQ6-CmejXIgRJQbwmkNyCa-Oxap8Ocy8gjO1Xow1LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/whitedns/1509" target="_blank">📅 08:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1508">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1508" target="_blank">📅 08:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1507">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دوستان عزیز سلام
اپ CoreForge از تیم WhiteDNS ظرفیت جدید اضافه کرده برای کاربران IOS
https://testflight.apple.com/join/3htm1Whc
آموزش استفاده
https://youtu.be/filwdiPKN90?si=O-hvgeNw43t4BUmR
@WhiteDNS</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1507" target="_blank">📅 01:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1506">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">💬
لینک ساب تیم WhiteDNS
https://github.com/iampedii/whitedns-sub</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1506" target="_blank">📅 01:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1504">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سلام دوستان :
❤️
اینقدر درخواست برای IP ثابت برنامه های  whiteAesther و whitevpn اومده که دیدیم بهتر هست ، یک پست براتون بگذارم
در حال حاضر  این امکان توی آخرین ورژن های این دو برنامه وجود ندارد
با اعضای تیم داریم روش کار میکنیم و امیدواریم طی روزهای آینده به دستتون برسونیم ، یکم به ما وقت بدید و صبور باشید.
ببخشید که انجام درخواست های شما گاهی طول می‌کشه، چون ما هم مثل تک تک شما درگیر کار و زندگی و مسائل خودمون هستیم و گاهی وقت کم میاریم
ولی مطمئن باشید ما همه پیام های شما را می‌خونیم و تا جایی که بتونیم ترتیب اثر می‌دیم ،
ارادتمند و کوچیک تک تک شما عزیزان دل
ویسپر</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/1504" target="_blank">📅 16:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1502">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⚠️
موقت
به نظر میاد که دامنه
workers.dev
کلادفلر رفع فیلتر شده است</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/whitedns/1502" target="_blank">📅 19:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1501">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BsR28RcnzK4kwpwOgy1ENdos6Pna_O7ekdjY5JQF9ShUldwUduThosQTpN7K4lj7uBHKDIR4ANMvAJ0rYEaDW2wXyVM-Vu7YzFqcKeTzoqfdbB0URhMw43mrMt17fuBu-RIWf5EInBKSWe0ekyhk0pYLAinircIm_EqGPn_NORm78kVQm4_bEJ46PF9Al1SKA8tL7nElm7g9S2OFQV5wG7qYesoeImgDIw1b4Zsx2ayHEDmmyiTDgA9lSrvoPY_y-ljRebEjkuvFxbVQ5hLCIZqEwY5PSbzeUFlk8VRhGReKmjmkozsoednUGdaBoWDhb-LWruc6MC4LdlcSPPnySQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/whitedns/1501" target="_blank">📅 15:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1496">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Yic-VlcyVQapz3trMi0TBZX_Ud_1ilWrdQp6hgZy56gc06WxRg874msoy3DioZZyqFlwCXjUomUDCQGDEMTaFqlMyrt_nxpZ1cqUfno0cD0QtpCiOEM9trLqQVF5m2mjptLLtPllyCDRNPCRjT5BnYqDy6ojSTskK2KKpEbdrBNUhn3bAd7MldJq5lw1H6NVaAz-dAch85hlj9xbROyRATg0B5V8wd8UoQrQc-imuK111IHWrkd7m1JMb3crEYoWaa9H8Ujf7NUPaB4h3XF25dKrZERUC0Fx72OPDCFy7754fbAsIpKoikFQdvJqBfyfPa-5iPlBto-s2r1MP1pYjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/whitedns/1496" target="_blank">📅 07:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1495">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/vxJhetgFRbvRcPnZtek_SaQzVM8ryLDW0wGpSoCsOlW0tYa-INyWVsOpJiOJILlWe1rq3rA54oGTFo87ld9ffMQJB4_uQZZ6sDFi6hjy1LadrgPCc7TuthfEePHLSDqYm9sHgnF1dPW5bFwJSOoE9bIApUp6RhnvQyJC95a0WrCkbMBxT0N2ZUWBrWwU3pTv_FhY3lWkh-Z2p5IiGudd8kwDQxMoAdFygM7DxgrvCIPJrFiNuyEicnBcNDaRN58x329MG-cK1tbGqgzmzb5cPDzXP16Cj2bqt30sSliVLdM1D-w_Mis2TOh-6tPSyv2crFLc26CP7zIXb2jqbmOzhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/whitedns/1495" target="_blank">📅 07:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1493">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/W-Si4A8JQDSeUht4aBWjxgRyRn4J1yMjwf6XQb_kxIHEYli9C1y8B1iNay6oOwCLkZXp48oaPG0ZX-_PzM9v6koYnWksk2tGGQSBTDAT1V_Y1YRQDfPjAXi3zR_79Jx-GT35Z-kgeR8iqlZWuKWXI7sCdwv5hYSTVuOZmUp3DwFxpJh54vt0OrJHwfjeWU6KYN-z5KOWP3nfvX1CwgD-DxBlPOUwhdru8IoY_Bnv3f5SEDcd42kvblyM_EFTbpu8qMLtrZeKclix1jc_EKr9YncDe22n2_PMvJbqu5knY1KR74Ee_RkqnUJraw_zybSPk19B6Siai5MWDrONeQ8dRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام :
برای حل این مشکل توی ورژن دسکتاپ و مبایل whitevpn لطفا ساب زیر را دستی وارد کنید
اگر به هر دلیلی ساب برای شما اپدیت نمیشه اول یک فیلترشکن روشن کنید که ساب را بتونید بگیرید و اپدیت کنید بعد استفاده کنید
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
@whitedns</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/1493" target="_blank">📅 05:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1491">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1491" target="_blank">📅 22:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1489">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijc5TVXT3lLjPWVy-kl75LddyHX01fyWurSL7_lK9Dr1JUPLr_siYo9e5xodVCsZDR8cvpCAbMKn-ua60W8oOI8zebqcOQlr35h6k5-I_hoalAEF0Aj0fpE51d51VV9pT5Fu4_RazB1HgWifXHYLyZ0ko05UnTfKmx26aazwrf3Tys8ojycKlZw2mpiudRuUhZcLDU8PY80xMajXvcvZ3w6O2mSnRXB_6Yp56_ed6DwHyK1Ee1jtuEJYTLjwt2qG2KJW5zMgEALqMtoU0YUo8e7zdGXoe4Z7V4iGaB552B9XEWS8yoYazKED7vi8AI6J49qU7AEBO9FNfXZrp7TPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟   میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro و باقی Wireguard ها وصل بشید.  این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1489" target="_blank">📅 21:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1488">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJ0uWOVVmckFSPbs1fiAYX0BimHa5QqH_Qdi56fL7jlBQ3nfUJn0JHwGzKfMdP9VisO6PDncDI-5RQZvdYuwtiGQzbUq_NQPex8gwjCd06PvfqeGFv3ylFlfNhCtmesuD1o-1HFhWbnAmLH3BBdDzLZxFJKlQAT2iyKOCo0cpFJDO0Rj5ItrDiPT1zicFoMS-ouWSwsiAef8chB0uVPEa94L_oVYYJLERnT6KGZs2Q52Fp6wmGVXS7QMCktwO7IF2ggFrtRwBhq5cwQAz1Xrey3q5LiNIwXvkxB_zeg-Rzb9vqf59pl-B81dCzbgPFlcnRgIi9wjabcTRruZ_smhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro و باقی Wireguard ها وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN
لینک ساب Mihomo رو داخل WhiteVPN وارد کنید.</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/whitedns/1488" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1487">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=PhRL-Fdv_iG0FZAcWB2I-v3CH3nLfu3A7d5R91_OQVeblC0Qxog1cJhLVQJzunU5dWV-dahdHjuWx1WaI-mzYTGVPZB7yuyHwGRjGW_mYXKHvUH1S7nvyUCHxTuj3ODxxXDI6h8uxxlT11ttvYnF_Lx6OsKiGOEKcqv6gGGNuJ9GC1vbR1ny1VEEE9OtFalTFk-ABzWmOl6nagJowVoJ0np4Jrx0AVy2kG956t3mn89tRp14MhlmTEEiA_ylvTl5G8X8IPOTi6NSXBmJsdY8uEqEgxrzuSoWozrGpVnglrZwxidDFYDxb38ZkAT-v8v_PMX-dZO045uJQ2sJaApx8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=PhRL-Fdv_iG0FZAcWB2I-v3CH3nLfu3A7d5R91_OQVeblC0Qxog1cJhLVQJzunU5dWV-dahdHjuWx1WaI-mzYTGVPZB7yuyHwGRjGW_mYXKHvUH1S7nvyUCHxTuj3ODxxXDI6h8uxxlT11ttvYnF_Lx6OsKiGOEKcqv6gGGNuJ9GC1vbR1ny1VEEE9OtFalTFk-ABzWmOl6nagJowVoJ0np4Jrx0AVy2kG956t3mn89tRp14MhlmTEEiA_ylvTl5G8X8IPOTi6NSXBmJsdY8uEqEgxrzuSoWozrGpVnglrZwxidDFYDxb38ZkAT-v8v_PMX-dZO045uJQ2sJaApx8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/whitedns/1487" target="_blank">📅 19:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1486">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1486" target="_blank">📅 19:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1481">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/whitedns/1481" target="_blank">📅 19:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1480">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZf62RbYaY-AqUIkzOXwmp9mwo3CIalv1TXH1ZC9FxV1_6KDZ4k0Z5GM_jnp1uPqk7ODcmtnqG9NN5OSrW85CRa5CJOtPDrarf3hndymX_VBcf11qhHmZsyW5HIaNVJlB1TDVy8yPOJKPTgr_gCV1e0p07QICSnlbq9lKg9ZvEBz8ag443dBeCYWa5X1HAD1eidp0uhRqx76J9Nvi8ptfLMPLZtmw-woktNy004kcasDrEIPPdVcTWtmuisr7Z3CrcqK2cHUxIEakHDdUSSV8GwKBTMyOS810yGAAHtnmpE_y9CtzMAgf3doDa6dvFzuvKiWrawMWrXmLg8WaKi9Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/whitedns/1480" target="_blank">📅 19:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1478">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/m6jr_lfb8spozdRUZrWTdMIf9wvIAAMUKyHgNAZVpUHXU6znUzDktdFuYT8CSSsX-PEq8bjAOb1_Qvv-Mz8Qjx83QQUG4l1VGi8DpJpCD3gXhXYDTKs1KNAqJAUn-JbCXf0nbMvAbgitR6rlpSY5cga5shRBATWyoQtMUP7v6P0Wm3AVn0OZuti99wBdynfNV0Tk2O1sxPwVVhsssHxW1rs_e2s__kQdI3dhslgwSF-0duCSO6yvhIA3AHcMglZBEEgA82KgOtCbYmoc3ljEsQ8CSIDAtpez9vGjsGliKBvTzBLuoPgvV6KstyYlwbKUa1sNa1zJXAVasF2w_kKO4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1478" target="_blank">📅 18:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1477">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دوستان عزیز سلام
مثل اینکه آدرس های ورکر کلادفلر فیلتر شدن. و آدرس ساب اپلیکیشن ما داخل ورکر ها هستش. تا آپدیت بعدی، میتونید ساب مارو از لینک زیر وارد اپ WhiteVPN بکنید
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1477" target="_blank">📅 16:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1476">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CULwFQ1pVXOy1Bm4e4ep3QU7nrTBHrW3VzpOlOvEzMF_8itjSVuj90tkx1Plz6JsxIcbdatbcCMnxbv5LAeotVrVc_Hm4kyTh5JcX8AmabNWZOA0NooSmnU0v8OSBsMAUGDykw7yEIDGnTjfd16etkdNNZrsvpLdXt__mf__7j20mcnprWSl-IehGvlaEE2ImsIx8iwAKAHUgrgpaZHIJwHlF1rCy7T9lyYMV2YLDOL5WfgudwI5sMmsMSv6ho4GKOfdNxO4f8ebes2ruMIBiICsw5-QJoDgNT2MEhR0006p5TXrNTgRB3QMNvgnLeht2EDPpKzo9iLfGIMR5vlX2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/whitedns/1476" target="_blank">📅 13:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1474">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DTZSNb2u1EeKGMWKrCyqVNz58ZDWuIMUH2_E5hj3dybjJJ5kBa9-icG5CW7tjokpNLgb9AsdDmNDQAJl6AO5QOsrzPG2nvLycxnFQ4LhrvnwRLfOT8h8YDmhUn0LBsrnGTfKwP0rvvPWVqJXcYUbYg72RPDJ2MXa4Zbe2ArXCBWHUOas6z6c-JP7uUGSg0UTS49PbhnN1x_em8fXWsitQ3GMNw_URN-LlVi_okb39k_yOyy7izDkfSb4Tc_YjS5FR2tm0qYdmQaZ-Ts5HocwPD7yTp0T3mg8z35p4cz1893A7lIndkXgD4Mxzf951aFmIDuDGnbIdf5wmvX0ZVMDhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/1474" target="_blank">📅 02:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1473">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaQpENm-VpnmKtxirvEiJOw7EWwqS-PCvWhMGJeOy6Z8HnPiQlUm7ynci2wjrN7vHxU4wAuJ2CjrKnNzMYiYsI2UZAjkUVRMW2rA9L3urVr5MwkKLxhRL5Ezc6a5IXzsVFeWTtOLXOHr6Sz3pCql-qotSvcQqYenxlnQwe3EO76yD1Pcx7JSQ_zHlBPYjLmrVXMG1xmNmqfJHdvYFbzz-3h11TtikSkUAauk7g7p2BU7xjzGVUoA9O0SAWpRuYQPBtqhHopg2s2e0oIW1O1YvuI11GwoduM6KFBpNvG1F_qhS14ZkM6AfO-5Ugojwib1JIQe4jSQn61bwniXUUyk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏯️
آموزش ساخت کانفیگ V2Ray با سرور رایگان!   توی این آموزش با استفاده از Wasmer یه سرور رایگان می‌سازیم و در نهایت بدون نیاز به خرید سرور، ۳ تا کانفیگ V2Ray برای مصرف شخصی دریافت می‌کنیم.
⚡️
⏯️
تماشا در یوتیوب  https://youtu.be/EAjOhvuMw8Q</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1473" target="_blank">📅 21:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1472">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⏯️
آموزش ساخت کانفیگ V2Ray با سرور رایگان!
توی این آموزش با استفاده از Wasmer یه سرور رایگان می‌سازیم و در نهایت بدون نیاز به خرید سرور، ۳ تا کانفیگ V2Ray برای مصرف شخصی دریافت می‌کنیم.
⚡️
⏯️
تماشا در یوتیوب
https://youtu.be/EAjOhvuMw8Q</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1472" target="_blank">📅 21:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1471">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OZdnYb9XkQEPXRZlji83mLYxJeX4icp2Qcuz5V3WLDPMyTC2Z54wSe4SA2dTACtBkAw-2A5J4jCpVWpz4Qs-x993v5nnIb0r8Sar-LGa9yMC8yYKt19vcKInKNZlOa4tlYpa3AnV9U4mIWtxDjcl49sD1pm-TSpbCHkYnpDIhFJeXNh__cqcJTXfDTWTwmB3vR2-lHW5ceUTH48HFO7nhoAiTyaAFS7yreU7zDJrsp7URYoDIb6J18baNwP-6c_XdlT1f5_Q9qEwt-QB3Tp7M1aRng0DRJdd3cguROG1xutK9WMdFMPRMUIDyk96WL_2sTxchphKClXMxUNTLLZuZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/whitedns/1471" target="_blank">📅 18:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1470">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1470" target="_blank">📅 15:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1468">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BSgRc9w4k-J3UoMJI4TqZ_uC0LiekORLfg-acy4YX699yo1ME3yGQsdR8fn3NcN3LWgF88Aub_BvMLzG8YwzuzZnHTnDloem0LEVuEXrdTB3PtyWa9C8JGb601NX0jS-ZH8v-1lV5TVrUhiaXYlhD3Rg9oCCKump_iQEOSH2jN4wbFynuTbGTe4NdPwxzK_XFUO0j0hgJDfqp8-PNPp27cdaQKnIGAc5zmk8CONLtnbxJK-6TpVOCJAiUeFNzZtHBlz8iEqa9Iv3KXc2DllKUk0t4cY5bYfgF9SBV6P9DzZiFSo5qqQfTyDFu2wWH6EZ7dwnK3BdaolMQt2t0RVBgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1468" target="_blank">📅 11:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1467">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/n7ZwZHdtYqGeDMjEQ3Dz_4__AkzBPcv8tZ8fW0HGbFzMdFtQCH-18ghZBuoUdG_gVySfA9beHKxAkCHEKBqt-rLrfYB7Stv6e_KXbP88VkomV52FLrVkP2C1aQEX1LIiVT7aWgyXE54k8wUTBm19k_dzJtJlXmDlD4ofhduYExJh5yiMrvMPAsS8-s6XHkp8X9ZeF-DK17TyCk4jnlrxg13f07BRuQKBbvk5NyT4l0bjQbMKnhmEQs4z1VmtJo-jzESK9tujuFvb29gLoERAvN3nh5Y_7mbku9RTtvjZEJRnhTObom_JlOoRz0-sxD9nWM_FEzHE1OP1LDEugTzxkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Coming soon............
WhithAester desktop
😍</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1467" target="_blank">📅 09:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1466">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌎
پروژه WhiteVPN رو اوپن‌سورس کردیم و در گیتهاب میتونید بهش دسترسی داشته باشید.   https://github.com/WhiteDNS/WhiteVPN  همراه با پابلیک شدن پروژه، نسخه ۱.۳.۱ هم ریلیز کردیم
⛏
در این نسخه امکان • آپدیت اتوماتیک اپ  بعد از یک ورژن جدید • امکان routing برای…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1466" target="_blank">📅 09:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1464">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌎
انتشار نسخه ۱.۳.۱ اپلیکیشن WhiteVPN
پست قبلی پاک شد. یک آپدیت کوچیک داشتیم به ورژن ۱.۳.۱
😆
از این به بعد آپدیت هارو اتوماتیک از داخل اپ میتونید بگرید</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/1464" target="_blank">📅 08:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1459">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.3.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/whitedns/1459" target="_blank">📅 08:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1458">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWtINwM3oAeC8xFs52LZ1dY0d_0dN3UaASn1RgomKfynVVzgeeuXd2CJ6xhlb3cuU4zu59Pdsd-rViEU3ItLOUrpYsslmwjYO1Y_1sEyrg4A44nK6iwCiBz7CVVNplL4gp8TF9YpKYs7FacT0BKzCeu5oDBpFR8momcLgflDmDS7xsZhw43EhSWAfzPM0aST0huuuzKbBn7lMXEQpnR0qLq7oyQBZmpd14J8wBxZLL-hEJYL8st010qzYe-2dQf5JvlcOZyp_MtbyPsWdfqUQpylnIqHldDUeOhx1_0-TDrk-I5hhbJY6BOxLnNhlrbv0Y6DQoEM0rpndTKhvCXj9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1458" target="_blank">📅 08:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1449">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DTGgwbRTP6NwDywmhhaXCgDnV33M_mVUtZfQtMqfvf0loa5Im6_Exm50_ajVW1N2-eQFmIml_Jn35cIADSfaK4bGJGNKal8_Dj8_4bUyZiCetxTEv1xKNJFH4XD0-RKWNEiQ61BC5swKQr916mzsIA3iGz0AFCrtrlWO_jEcT1IzWgbHpj2MI9UrvIUZTep7WhEL3xTQTjetQK-u30rLSDha76zYDSrUuH0es6lvOCWucmtNEBEINBtFwRxeKtJ1f5iYfsPB7wbtHw95NQGLUW0EcVR0XVNcRw3DkBVQr42kBQlQS2ObocL1csB_hlrqhKY9xDLAY_WWAdUW2F5mcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/whitedns/1449" target="_blank">📅 11:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1448">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/whitedns/1448" target="_blank">📅 11:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1447">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmURihj_2jt3kJOVVB97Q37iZBjNcp37KDdm3pwMlRvkiSZPT3uCblXxyYrzU8o28iD_di3ruKcA_t7Sr_RISHT8qXKcLlqSCBeeyw767-RLozP_MswKhn2rESO8cnwu0xi9o86uUsBlwLUHUlvHJbNzOOPEHtKFtOy6xNC6yTp2YRs_DITLMloUAv-YZoS6x_7OHXpGUFZMBV2ZktCJHMOtlyeEmqTWf8SpdX6IhWBj2q2lpvdKtsY5yRFfnCEm3TYTP5MhR9FoE3Fip6NtuK3AKg3ue1V-gVXxhSijxidZhBtsrfZruPfvvPCGG4QDqfcE1m1ZaOOWiUAw9X-85w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1447" target="_blank">📅 09:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1446">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1446" target="_blank">📅 09:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1444">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1444" target="_blank">📅 07:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1443">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1443" target="_blank">📅 16:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1440">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1440" target="_blank">📅 13:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1438">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/whitedns/1438" target="_blank">📅 12:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1437">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-poll">
<h4>📊 با whitevpn desktop وصل هستید ؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/whitedns/1437" target="_blank">📅 11:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1436">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/whitedns/1436" target="_blank">📅 03:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1433">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی  این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/whitedns/1433" target="_blank">📅 20:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1432">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=iz_29aDYM5zc27LKfZs6S4rr_a02c8r1jJOcaaO9HCGu_DjeoQq17lRHKrrbEB4zS9JUkboSVC54MejScGjhnFrRytUdHFmD_DR-JjRTc1wM62N3bA8sTzoIfgkkx1_pqaNS2_ex6eFfoOM1oDqmdP5sDoiY7dyi-DwXvZbzr955GprzLsCcSFcbC08Ogn8o40djFfSk8uINmJ6pdIhZ8VpCFrIyrbUJMQ750FQYogLeytgVju8FJoQx6-RJZkLodYFkd5NOczE-0H_uDwlY4ePYbrqg5HJaOz4oJMxdz_-TV0l52tgRuPKxQHny3NDVVGO_73XTNGfG6oTuA0R7Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=iz_29aDYM5zc27LKfZs6S4rr_a02c8r1jJOcaaO9HCGu_DjeoQq17lRHKrrbEB4zS9JUkboSVC54MejScGjhnFrRytUdHFmD_DR-JjRTc1wM62N3bA8sTzoIfgkkx1_pqaNS2_ex6eFfoOM1oDqmdP5sDoiY7dyi-DwXvZbzr955GprzLsCcSFcbC08Ogn8o40djFfSk8uINmJ6pdIhZ8VpCFrIyrbUJMQ750FQYogLeytgVju8FJoQx6-RJZkLodYFkd5NOczE-0H_uDwlY4ePYbrqg5HJaOz4oJMxdz_-TV0l52tgRuPKxQHny3NDVVGO_73XTNGfG6oTuA0R7Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/whitedns/1432" target="_blank">📅 19:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1431">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/whitedns/1431" target="_blank">📅 16:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1430">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">White DNS
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1430" target="_blank">📅 12:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1428">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">White DNS
pinned «
دوستان عزیز،  در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1428" target="_blank">📅 12:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1427">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/whitedns/1427" target="_blank">📅 12:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1426">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/whitedns/1426" target="_blank">📅 08:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1424">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/whitedns/1424" target="_blank">📅 10:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1423">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/o-InZTMrK4je3PJ2kKp2YqS8lxuShdNhsWCXAI3dJfwktkyGZXe70uFtj1TBEex5UwaU1EDCw0pdhtioqmNTgKDmlbYH1dTouuQtKF18KbKqgdEWWAaB053zR8X-Exc04vd9f1loncTjUGEQEoco-AQd7XGCdDsdhadKadkA0EOq8dyJhtBRSyAAis_0v_aPgaxWOo6x4QC23HQGMAEZVeQzZexWRMc3li8NarmYoUowDXWzu28WhoZugPUCbe-Rkkv_fni8nMEtXtVYy9c2YsJJCmqJU5JSl5PaENbry6oO8_Sr33cR3t0s754cbEK3Bg9N1-TGeFyTSTKAS9tepw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/whitedns/1423" target="_blank">📅 19:41 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
