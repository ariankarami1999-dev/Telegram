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
<img src="https://cdn4.telesco.pe/file/KtxxHXWhLDcldvUmKUqkFBu-x3jUSU9b-gI-KkuFZcYM-RroXJUGsw0l4meoxW7M9toW0FXNTLNoEaVSe2uIA09UeRIZcQ7gVesZLS9R603j-mt4wVex8x1lfdcxGNnKakXqw_9vbJSyvYKIpTUkb0AoXGhO61llQqQ41oE305mn0-ZVVIc7jnDXbc-Zr5weSsAjqDBvztKarncdj4qA3xrLbBqpf5gdGVqCB53yVRcMbPeW3XFpCA8wMSBJdyDOkXDpOqhWW4LrkgqoZoB9UIUvzi3h5XMeT7u71OO5fE5yNpfHZ0VZ0HOs2508iwvIpEBIuHYK41ugSgajwdQe2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 21:16:59</div>
<hr>

<div class="tg-post" id="msg-1258">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard
https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1258" target="_blank">📅 15:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1257">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👆
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/whitedns/1257" target="_blank">📅 14:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1252">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">20 MB</div>
</div>
<a href="https://t.me/whitedns/1252" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/whitedns/1252" target="_blank">📅 14:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1251">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQwJQ5axtBq6-R4UODutGdICqzY99XfDxJZ4rppg7d3IZE56MRbh6bG1PlWi9JVjZa_YMs70wcj242OZjIuQXxHA7IyljcIiRWZTzrmq6wrBOXe6xoSyFBdeVIBrFGWXzJSJdxpYjzKFK10729oVUKI5jsY0AM4r3J_46XHRptaxx_Rhe-naN2FnzTdLJCbIP46OcnH6SdC84SzAocyyAVdd6PeLeb8O2Hm1B0CqGCgxAbP6Ma7CjRh5ihVA10roTqRtCmc4-5UJpZJHJSdCFbduVBVIg5-Auo7Dwu5sVCSLAQvTNLPZ7N-uex98IIf5lAwHV_LPMHdaMK-c89AVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/whitedns/1251" target="_blank">📅 14:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1250">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آموزش آماده شد اما تا ادیت میکنیم، ورژن جدید WhiteVPN رو ریلیز کنیم چون آموزش رو با کمک اون ساختیم.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/whitedns/1250" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1249">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">همراه با فیلم آموزشی، درحال آپدیت کردن هسته WhiteVPN و اضافه کردن بهترین پشتیبانی ممکن از آپدیت جدید BPB  هستیم تا اتصال شما ساده تر و پایدار تر بشه.
نامگذازی اپ هامون هم داره کم کم تغییر میکنه تا کمتر گیج کننده باشه براتون
به مرور زمان همه اپ ها تغییر میکنند به نام های زیر:
WhiteDNS
WhiteVPN
WhiteScanner
WhiteBPB</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1249" target="_blank">📅 08:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1246">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">White DNS
pinned «
جلسه پرسش و پاسخ توی همین تلگرام به صورت انلاین بگذاریم  ؟
🔥
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1246" target="_blank">📅 16:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1245">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-poll">
<h4>📊 جلسه پرسش و پاسخ توی همین تلگرام به صورت انلاین بگذاریم  ؟🔥</h4>
<ul>
<li>✓ بله❤️</li>
<li>✓ خیر🫤</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1245" target="_blank">📅 16:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1244">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iXS7zXdAQjCEYmmIlbQsb8T597VChz81sUFCAqAkDmKss5P0y5x89ApxwAHN8FuptCrK-oh5LHTIjLNPdg8wp1jwVWcmV0Pm7r8d2B4uTUog3nDZj_k1LG96CMKYG3UuZjxbAQ8Is5COGrF1s20JFH0M_ewG45snZEPdsWh_rl2sa3W250-RoiwDYzyWMK2ORl_f5wFQu5DLOKuR137WurfyuVRnUwHYEQuYcz-mmRVabrLTy7ZhZ4HOr32V57aR-kFCVqOegpCGoygTJuTGe0dYf6r1PWUt8WBgIMkofGfLI62y0CAJJboUDtX098T0fyplsDL6iaLa4s2u3Y5ncQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ و انقلابی BPB Worker Panel (نسل جدید - نسخه 5.1.1)
🎉
نسخه جدید و کاملاً بازطراحی‌شده پنل BPB با امکانات بی‌نظیر و تغییرات ساختاری عظیم منتشر شد! در این آپدیت، مدیریت پنل و سرورها بسیار یکپارچه‌تر، امن‌تر و بی‌نیاز از درگیری با داشبورد کلودفلر شده است.
✨
مهم‌ترین ویژگی‌ها و تغییرات این نسخه:
🔹
نصب سریع با One-Click Wizard:
دیپلوی پنل حالا فقط از طریق ویزارد آنلاین و اختصاصی انجام می‌شود و پس از نصب، یک لینک کاملاً پرایوت به شما می‌دهد (روش‌های نصب دستی روی این نسخه کار نمی‌کنند).
🔹
داشبورد مدیریت داخلی (Admin Dashboard):
امکان آپدیت پنل به نسخه‌های جدید، حذف کامل پنل، و ریست پسورد مستقیماً از داخل خود پنل اضافه شده است.
🔹
راه‌اندازی ربات تلگرام:
مدیریت کانفیگ‌های تکی، دریافت لینک‌های سابسکریپشن و مانیتورینگ مصرف (همراه با هشدار مصرف بالای ۸۰٪) از طریق ربات تلگرام.
🔹
حذف کامل Environment Variableها:
تمام متغیرهای ثابت (مثل VLESS UUID، Trojan Pass، Proxy IPs و...) از داشبورد کلودفلر حذف شده و مستقیماً داخل پنل قابل آپدیت و مدیریت هستند.
🔹
ارتقای چشمگیر امنیت:
لاگین به پنل حالا نیازمند ایمیل کلودفلر شماست.
مسیر ورود به پنل به یک آدرس تصادفی و امن (Secure Path) تغییر یافته (دیگر با زدن
/panel
وارد نخواهید شد).
🔹
تنظیم سریع Custom Domain:
دامنه‌های سفارشی خود را می‌توانید مستقیماً از بخش Common settings وارد کنید تا کانفیگ‌های مربوطه با تگ
D
به سابسکریپشن شما اضافه شوند.
🔹
قابلیت‌های جدید شبکه و پروکسی:
پشتیبانی از Xhttp و VLESS Encryption برای Chain Proxy در هسته‌های Xray و Clash.
🔹
انتقال آسان تنظیمات:
اضافه شدن قابلیت جذاب به‌روزرسانی و همگام‌سازی تنظیمات از یک پنل ریموت BPB دیگر.
⚠️
نکات بسیار مهم برای اتصال کلاینت‌ها:
حتماً کلاینت‌های خود را به آخرین نسخه آپدیت کنید (حداقل Sing-box نسخه 1.12.0 و v2rayNG نسخه 2.2.3 به بالا).
برای اتصال پایدار در v2rayNG، حتماً گزینه
Hev TUN
را فعال کنید.
در صورت مشکل با فرگمنت در برخی ISPها، حالت
Packet
را روی
1-1
تنظیم کنید.
لینک ریپو :
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases
لینک ویزارد :
https://wizard.bpb-panel.workers.dev/
@whitedns</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/whitedns/1244" target="_blank">📅 12:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1239">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/whitedns/1239" target="_blank">📅 12:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1238">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at6G89XsfaHRIXOkEHgrW5zso0dKJoXFfqBEgtJWPviETib7Djtqklvj_AIOdpF8Di4PGvZjQKiDDgZm5F2P77-ZTQJ9VlcDSwtZicMF7evNr5V36VBemjuSHFvDGjK1lVcujWwqbAJK1rOQfrqG3Sbv8oAkC_28EWqkpog_UEviGv_qEWt6dPJi1cBpIY4zQueFQ5k3G_JS9_96JKpqxTJ45kAXXVEHxCoVdDuVK-h41L7LB-tcPTAP5RUsZ1bH5ziT6ED8yQDhHjKza80Yba1CpsAJwQZgoo9kTo88eq0kshYTVO9Fh6NNFteAichzzW4WgMbFZZRaBZdFbZjbew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/whitedns/1238" target="_blank">📅 12:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1235">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.2 MB</div>
</div>
<a href="https://t.me/whitedns/1235" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تازه‌های نسخه ۱.۱.۰
🆕
اِتِر (Aether)
تایل تنظیمات سریع (Quick Settings)
— روشن/خاموش کردن VPN مستقیم از منوی بالای گوشی، بدون باز کردن برنامه. یک بار اضافه‌اش کنید: منو را پایین بکشید ← دکمه مداد/ویرایش ← تایل
اِتِر
را بکشید داخل.
اشتراک‌گذاری VPN با لپ‌تاپ یا گوشی دیگر
📱
💻
— از منوی کناری ←
اشتراک‌گذاری VPN
. گوشی شما یک پراکسی
HTTP (پورت 8118)
و یک پراکسی
SOCKS5 (پورت 1080)
روی وای‌فای/هات‌اسپات باز می‌کند. آدرس دقیق
ip:port
قابل کپی است و کافی‌است در تنظیمات پراکسی سیستم دستگاه دیگر وارد شود.
تنظیمات پیشرفته در صفحه اصلی
⚙️
— دکمه جدید بالا–راست صفحه، پروتکل، حالت اسکن، نسخه IP و بقیه تنظیمات را در یک پنل پایینی باز می‌کند.
آپدیت بدون حذف برنامه از این به بعد
🔄
— همه بیلدها از این نسخه با یک کلید ثابت امضا می‌شوند، پس نسخه‌های بعدی مستقیم روی نسخه قبلی نصب می‌شوند. نکته: برای آپدیت
از نسخه 1.0.0
فقط یک بار باید برنامه قبلی حذف شود، چون آن نسخه با کلید موقت امضا شده بود.
رفع اشکال:
پنل اشتراک‌گذاری VPN حالا بلافاصله بعد از روشن کردن سوییچ، آدرس
ip:port
قابل کپی را نشان می‌دهد.
✅
عنوان ریلیزها تمیزتر شد (دیگر پسوند "(build N)" ندارد).
📝
Downloads
📥
https://github.com/QW-AI-Code/Aether/releases/tag/v1.1.0-build.2</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1235" target="_blank">📅 11:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1234">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⚡️
اِتِر (Aether) — آزادی، با یک لمس!
⚡️
نسخه اندروید   درویدِ قدرتمند و رایگانِ اِتِر؛ اینترنت بدون محدودیت، بدون ثبت‌نام، بدون سرور شخصی!
🚀
🔥
چرا اِتِر؟
🖱
اتصال با یک لمس — VPN کامل سیستمی؛ همه اپ‌ها و مرورگرها بدون هیچ تنظیمی از تونل عبور می‌کنند
🛡
موتور…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1234" target="_blank">📅 11:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1233">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Iu_IWONEOW13Oc1IEQH4C7otTV_3YCruma8829y0BmLjNHRqPh32Bj1RyrB1M-X3cI44gQ1b1ARIyU4i6tOEnysDUocTSJ2linopeF6tXjSMp44Y-pOOwYTU2Hxhqr6UsbZDWC_e4UoYb1gaq0g3xKHenYzHd33cufVOw9JwY7O6jEmQ2O7boHrd0ni5naC4b2AmMdoQ93Veri7CkTEJ6SkU-PGsqhtrtELD3vt3bta3THXTkiue9DukU72Mk7izAEOm1svWFeEkqBLSaHdNE9udt6cN3tNqALRe0-VdECgiHsQot5tfX2dRANr76YjJih08HGEYacDX5r_buxG1Vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/whitedns/1233" target="_blank">📅 05:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1232">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⚡️
اِتِر (Aether) — آزادی، با یک لمس!
⚡️
نسخه اندروید
درویدِ قدرتمند و رایگانِ اِتِر؛ اینترنت بدون محدودیت، بدون ثبت‌نام، بدون سرور شخصی!
🚀
🔥
چرا اِتِر؟
🖱
اتصال با یک لمس — VPN کامل سیستمی؛ همه اپ‌ها و مرورگرها بدون هیچ تنظیمی از تونل عبور می‌کنند
🛡
موتور پیشرفت
ه WARP با تکنیک‌های ضدفیلترروز:
✅
پروتکل MASQUE (HTTP/3 و HTTP/2)
✅
تونل تو در تو WAR P-in-WARP (حالت gool) برای سخت‌ترین شرایط
✅
قطعه‌قطعه‌سازی ClientHello و مبهم‌سازی ترافیک
✅
اسکن هوشمند و خودکار بهترین endpoint
⚙️
۴ حالت اسکن برای هر شرایطی: Turbo
⚡️
/ Balanced
⚖️
/ Stealth
🥷
/ Thorough
🔍
📊
نمایش زنده ترافیک — سرعت لحظه‌ای و مجموع دانلود و آپلود، درست مثل VPNهای حرفه‌ای
🌍
نمایش IP سرور با پرچم کشور + تایمر مدت اتصال
🧪
تست خودکار سلامت اتصال — بعد از هر اتصال، خودش بررسی می‌کند ترافیک واقعاً جریان دارد یا نه و دقیقاً می‌گوید مشکل کجاست.
🔁
اتصال مجدد خودکار — اگر ارتباط قطع شود، خودش دوباره وصل می‌شود
🔒
امنیت کامل، بدون نشت:
✅
بدون نشت IPv6 و DNS
✅
بدون بکاپ اطلاعات حساس
🎨
رابط کاربری زیبای Material 3 — دوزبانه فارسی و انگلیسی، با منوی مرتب و مینیمال
📱
سبک و بهینه — نسخه مجزا برای هر معماری (arm64 و arm32)
📥
دانلود مستقیم از گیت‌هاب:
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/whitedns/1232" target="_blank">📅 03:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1231">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سلام دوستان عزیز
👋
🌸
اپ CoreForge یک قابلیت جدید برای کاربران iOS اضافه کرده
📱
✨
این اپ شبیه WhiteDNS است که برای iOS و شرایط قطعی اینترنت طراحی شده
🚀
🌐
🔗
لینک:
https://testflight.apple.com/join/3htm1Whc
🎥
آموزش استفاده:
🔗
https://youtu.be/filwdiPKN90?si=O-hvgeNw43t4BUmR
📲
کانال تلگرام:
@WhiteDNS</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1231" target="_blank">📅 17:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1230">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامیرپارسا گودمن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6b89a933.mp4?token=XYqLQhizy5LPbPXCQ8GuCCXyFOHJXJGBTEfpeqySoMm31d_E9WNlmYZOaAg9TpFVfIzGPtBEbrZomIAlX_eZ02TSiwbLuBzkoon88aKSFuBBt-n4iS2nHg6dPBv23oLRZiK4oAlK5IhOwHc181sTzHEq6mzq_1BFghdhvhUfoTSJoOvpsN5X3Zdr3AOIJzvKvk3ceWmMFgWDwNw0F528ijBF3EzDDWuzakrJ_DwhHYLth8BSJfPytFeNCKHSe0V2euARiP4BdRz-u2rVBFtMrjd80IiLE4jzz3IXcaa0EgdtyVbvPcBoTd-tqYBNfhwgZ_p5A5O9onUfXxi450w3mUZqXMqEYduSek76SC3wankSxBjR0Ez7f9vAE5Qb9SzHeVx-Og8gwJtuHYWUwEftnvkt7QWPQPIK-TlAyDD4DxTV6dIclUxRbG9Jiph5fjHR9WL9FGOn39h-EV8nfxxiBlgGHcOgpHpUGW5o1PAHuypGsbdJq5OI-JENxPUX0_oJ329iYR5KmLvU0_JWEub6ZfIw0SNP6Ul0X8NYybvIaz2Td4fTF2A4GtCUtCll94LoNjV6d2pZE74sTSPh3Rm07nC6GsbR6BExy0fkIw1Rvwvy3jKYY4l6ATNUIU0MG1fj_7M2sD9iDgpMj9jeQ8TndAqZDEdL68ar6H3L1YVOU_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6b89a933.mp4?token=XYqLQhizy5LPbPXCQ8GuCCXyFOHJXJGBTEfpeqySoMm31d_E9WNlmYZOaAg9TpFVfIzGPtBEbrZomIAlX_eZ02TSiwbLuBzkoon88aKSFuBBt-n4iS2nHg6dPBv23oLRZiK4oAlK5IhOwHc181sTzHEq6mzq_1BFghdhvhUfoTSJoOvpsN5X3Zdr3AOIJzvKvk3ceWmMFgWDwNw0F528ijBF3EzDDWuzakrJ_DwhHYLth8BSJfPytFeNCKHSe0V2euARiP4BdRz-u2rVBFtMrjd80IiLE4jzz3IXcaa0EgdtyVbvPcBoTd-tqYBNfhwgZ_p5A5O9onUfXxi450w3mUZqXMqEYduSek76SC3wankSxBjR0Ez7f9vAE5Qb9SzHeVx-Og8gwJtuHYWUwEftnvkt7QWPQPIK-TlAyDD4DxTV6dIclUxRbG9Jiph5fjHR9WL9FGOn39h-EV8nfxxiBlgGHcOgpHpUGW5o1PAHuypGsbdJq5OI-JENxPUX0_oJ329iYR5KmLvU0_JWEub6ZfIw0SNP6Ul0X8NYybvIaz2Td4fTF2A4GtCUtCll94LoNjV6d2pZE74sTSPh3Rm07nC6GsbR6BExy0fkIw1Rvwvy3jKYY4l6ATNUIU0MG1fj_7M2sD9iDgpMj9jeQ8TndAqZDEdL68ar6H3L1YVOU_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">https://t.me/xsfilterrnet/3623</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1230" target="_blank">📅 00:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1229">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/aEhG6mLjMub49QfrgtgJ3z1zu0rY7rZCTSNlRmqtlUJrEqL6-MTL4wiodWQtOnjfz2iSquqP57IRRXoTjgyLswj2NUrccS0AqJseJk6oX8pcgNyahpLTzp2rPk5nRxx77xJw2j3qFHmyCcVy-eZT73snSXjcB5PFALqRSQiYpfNHSWb5FLrPcKXBDiJIg0SK1taPBjf09d3oGGQtyDamhA5HLpLw_MkXNilsUv5GQyoplLQIHnrlKceJtbi36kMXeDsHT89NRzmqWHmyHFOs-oIY6Gf3SO_aDIJQgST6APupDDeB4ODp5kecuxPmhWg5GAnK-9a47a9q-tSnv5ZChw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/whitedns/1229" target="_blank">📅 17:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1228">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1228" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1227">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1227" target="_blank">📅 12:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1226">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/whitedns/1226" target="_blank">📅 12:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1225">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rw1FVGQy9g6ZVwwkZyJcBcMYc7nJDAsazJPS0V6H7V-jpO1za5MJ2biYF2NNY9fnUCZg8adv_0aX7HC86o89XYz5xcmORyoGjZVaizl2ioJVb2_D8BZ_HJhmEtHh6tnp3p6R2CFhXO1rhHGBJEXMo_iQuplAQIG5CYrKGEdPsG2pLaspNkIGXHnBfkJWM4L_6S8MAvqK5Y3h2gVMTbIzejIzHR1iU-2o_mherEb_r_L_E5HBSxbDiJRtjCYMskqFFPTARvexkDa_qg3UHgSXXhBw00Sk8w8xYewHv5zacZ6UIgzVY7rj3QInqVIfHYO5iJ2lakd3Woy4MryH7gQ6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/whitedns/1225" target="_blank">📅 06:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1224">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/nHjmtXIt6Fb_3abg4_Cd3P9y6ocNwCsOGRNDi_EpmNqWhud57lAuj7Jfdlitm3CeoD7VBNWUV0SZhDkCF4xMrEmS7dC8wBrr-RDQjORF1iH249FQxw4fBhiXiIv16MbAGOQRn6VErjfPyOE2YjlFXa4CMl28YT32RdKDkdRwP7x6yTvZiQmENDkej9Lf6O-cIE66U1ntTF_4IF9P6mI2HuOCu9u4jvwhpxvKQBfWgQdwzdC88o9v03Mlz7_5s71BU8Ry5BSBxolDkZIkFoGuIobLX75T2mr4OWpV6WcYY5OfP-LoxnUMabCcoyLPpUfZUUDXRQfJLDc5XYlUXpAx5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/whitedns/1224" target="_blank">📅 20:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1219">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1219" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/whitedns/1219" target="_blank">📅 17:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1218">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeweG-uzSfvrVIMlEKNlpYYUQ39xf6UlkZ-cIRS4ArxjblA2jeubY-ORDLy8HLHcKJ9Gjvtbp0rVWo-8cq0rxAaQCrw4mLDJSDVlNn1DrIKpR4_LxLS1AdNBy57dQSSbghO2gXMMLxWNp6zUsZnS-V5czzFC9cuTC6Yzfuu9MwHT0lHJ4s_WK9fMy1_DTN9BAlKvc9il38TdUuqpueVZ9hXB2d8NufWqD0ORy4eI5XlSpd6fj-hMYxvUeq0il9IHx3T-aRN8ecabxQT-5TtSBp9HIlUPgjBRZvGJe3ynryr6UC7Fcn7K6KWWrazrsozgJB14Vk-o4Do5A8qxw_WhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/whitedns/1218" target="_blank">📅 17:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1217">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1217" target="_blank">📅 17:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1216">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم
با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.
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
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1216" target="_blank">📅 14:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1215">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">White DNS
pinned «
دوستان برای همه اینها اموزش هم گذاشتیم که الان لینک را اضافه کردیم .  لطفا بدون دیدن این اموزش ها سوال نکنید
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1215" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1214">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1214" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1213">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">White DNS
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1213" target="_blank">📅 12:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1211">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/N7EHLqBI4qrIaQekTkdGLSPv1BlBWxzG_rbPvpAIYHw-MKuks05-Ageh-mcyuxBwfaWrNMAEgX2V5wOjk9rTCy0-5votabksL_kmrx3o5SED-v2jJPwzc7LIRM5mFCiatBODVNMq0UmLGU6CyzyZPc9Q9lsIBzhX8IO6bRpSQ5SGyfJZMZ65kKEgvCSHBjCrBboLnNHBgc6c0ML2L2RjL2YX480iiFBEINA4WdXzDfAr_ifdma6qMDIh7sUh300npS9o8lxelveuvxyhVbJJWmQr44iFxMUDfp5NuwRjTI_EHEjM5wsHWFh-ndmIm5AyqaJGJeDtx1ojh3ha84BCYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/whitedns/1211" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1210">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kJCw8x9kfszDaHVS2eKMGZGHDIcuMNjyhzh7vYtdzvlJtb2ucwg4MMEm1Sg9F2r1sLCyAqWJ6GZxxJCoUyoJHWo0moiUNmwGLKVjQZwdXPFkA61dNwsg3v2POPqNAEPvpakCe-8U7s9lzGFugXoDwnGobIvmN3pUkACLLE_mLjifk_FsSDVgNLa_xdxipg4Yz80NtTHzIKz_YNFnUh6N2h-WfthQlG9TLBB5O5i-kd9eLujpD_zYhTEP2kjfqbdm2lak4I-A8eAD5ShBC-4rUnS3SPuQrCnRRNmhFLvJhL1LTuYCp5kQyShRUP9qnJ7t04sRnIksxvENYn5xLQh4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در whitedns android</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1210" target="_blank">📅 12:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1208">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rp3Fmnb-Mywn12hXSiOEcrfeQeZU7cCVZ6ZWIqNDJDSJ_AgcBujEVzTioFHqjid8_IIxbnBAu_eX_jzUMIb0oL_Z-VNo3ILRePkjPBUwsgf6nq4sAYTwkREKD2qGFPjYnCI1DjsMdrMtBu3NDsSJzMIfyx03HiKnSozp_WaUftIaoqvTGzACFqQS83BIvBWjE73v7RCfHX9rLkgxp8JCWy3iy0th5AjQd1eIQA-usKDvWzRuUORjyPEf0vTf0cmqJNy60XayK-e28OW9r54SqoSTaHcRHC5ISYZ_thjJu-GbwPROx-EssJfXojPy_c5C6-TtsnSSKvP49pg6lJqr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در Whitedns windows</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/whitedns/1208" target="_blank">📅 12:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1206">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Android.zip</div>
  <div class="tg-doc-extra">2.5 KB</div>
</div>
<a href="https://t.me/whitedns/1206" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/whitedns/1206" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1205">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uzQuA4O8X_X6XKY5JcftjskheNrlA-asXmOHiOWkxKB6oHWjFj9WG5DXkMbVXxVs2q93V8LI0cLyNTKO2aa_io5kkaycQgqGrTbaG64Gx5yXX1ntTqiLDZ8fmjcfV5HWTeulhsmUTaVl4bcUKythvrqbCT1MLcwqv5nK61T-JDB9UMIh3d5NBTXTFUFcxJNz1J9tp08BJTUVPZEMoRm4PSzsZZ9OdXvy-ntoRe8HjnCtHztWJWN1eDvTgbXcBEGNxamqw6rPDKfhBlAa0WEeN5YgT7ztV4j4h8f7-1_xwkHoaavrTmyNSesgs_pS1RbHnSuFcvHA0yGL0Qs4KTmOFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
افزایش سرعت اتصال WhiteDNS
یکی از مشکلاتی که بسیاری از کاربران با اون مواجه هستن، اتصال موفق
WhiteDNS
با سرعت پایین یا ناپایداره.
✅
یکی از مؤثرترین راه‌ها برای افزایش سرعت و پایداری اتصال، استفاده از تنظیمات بهینه میباشد (البته استفاده از سرور و کانفیگ اختصاصی هم تأثیر قابل توجهی روی کیفیت اتصال داره).
📦
به همین منظور، ۳ تنظیمات پرسرعت برای
اندروید
و
ویندوز
آماده کردیم که می‌تونید از اون‌ها استفاده کنید.
🍏
کاربران آیفون:
اپلیکیشن
CoreForge
به‌صورت پیش‌فرض تنظیمات بسیار مناسبی داره و در اکثر مواقع نیازی به استفاده از تنظیمات اضافی نخواهید داشت.
📥
نحوه استفاده:
• فایل تنظیمات رو مستقیماً داخل اپلیکیشن
Import
کنید.
• یا فایل رو باز کرده و محتوای اون رو
Copy/Paste
کنید.
⚠️
توجه
:
این تنظیمات فقط
مخصوص اپلیکیشن WhiteDNS
(مناسب اینترنت ملی) هستن و به درد استفاده در
WhiteDNS VPN
نمیخورن ؛ لطفاً این دو مورد رو با هم اشتباه نگیرید.
💡
نکته مهم
:
ممکنه این تنظیمات باعث افزایش مصرف اینترنت بشن. بنابراین بعد از اضافه کردنشون ، مقادیر Download Dup و Upload Dup رو متناسب با نیاز خودتون تنظیم کنید:
🔹
مقادیر
بالاتر
👈
مصرف اینترنت بیشتر
✅
اتصال پایدارتر
🔹
مقادیر
پایین‌تر
👈
مصرف اینترنت کمتر
✅
اتصال حساس‌تر و شکننده‌تر
❤️
امیدواریم این تنظیمات تجربه‌ای سریع‌تر و پایدارتر از WhiteDNS براتون فراهم کنه.
@whitedns</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1205" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1204">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1204" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1199">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1199" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/whitedns/1199" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1198">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XArueDsVzOgG9dtA1bPLTaQGBzx_Xxyt6Ol75EEgDWdMDeXEHYA3KtLchdN-pxPF-tJuyzdtA-zO3pQW2qW6jhumu0r61CVgpgMcG4tzMEKcBqYxflu1F_SAI1t5DIEufuXDcqUBo_CMgItREconfuP461HtpoQYXQlrpyKg9ZD0vsjNPjpsohfNXJrcrlgKmpdwYeXf4UCjPvbrY00unHfIptd8Il-BkfTD_MKhpJoP_7KM8YB5fmShcRJjtZZe9GyUF5GjFsF3lcszu1vpMiqndps05FTEZv3BgZBoF69zocQqW01A574yvDJ_CQOu5R1ExP5Y0uTwgv59BBEFmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/whitedns/1198" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1196">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J-SwTBKg4cs-K5TKerZHW6uAXuJaInL9vlsicjmjZvBEyt-oTlxNk_Z7Uk2B8UU1buon8HiMPIHOM9_OQ8mZgQ7FSvBCCdArJMx7S6dE2gGpdtDb5gnHpSmkw34rXGSvYXeroBKzqrhucgpkbzqMB6wqhVODPqjiUOrurg7qhUcQWDACGfx2WzCUFez5GVNbQ_E3-4FtKkl_9JSxgX9HEuyNvFRt5PVCD6DRpYj8qKMnQYR64L2TQ7zBFax2jjHEHnEnE2hjDuRTp1S-HfxVn9kLK30HbIrMCpy5K1VYM0c2SohxIMniZ92GWmkPd7r-kdiDHQnRCJNqPSwW5DR_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lOvkGxzn6g2wC83yw24jk9CFdoPatY4qZd18z1G3S3n3qQP6Ie_-L5eV8exp29srl8o59IEumwAowzrgbwckogHKDNlP_86GSKTTOnDnWVAiY1_NuTXRWjTAVy3YQZRJAFc99a25qQxhLb7dwfLa_ESa7m2iaF22o8e_wK-SbdNTQ0T7z_No8oByCAm413vTJz_RHDBSv3ygdbPXY_MVFqjtg_njaETyWy6G15d76FWzkqUJg7mDo5NNrJMgqWYJfeLVWour6DP7eXUzHFYKBzZbNlGFgnAe_nbzDfM4dNLtXFeIHdEP4Kd6Q47LlReoaz11p-0FcwjSp1luklJXVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپدیت جدید Aether-GUI (نسخه 0.4.0) با هسته‌ی جدید!
نسخه‌ی جدید برنامه آماده‌ست. توی این آپدیت، هسته‌ی اصلی (Aether Core) به ورژن
1.2.0
ارتقا پیدا کرده و قابلیت‌های زیر به GUI اضافه شده:
🔵
رفع مشکل وضعیت Connected فیک:
قبل از این، بخش Validation ابزار با پینگ کردن
1.1.1.1
(که داخل شبکه‌ی خود کلودفلر هست) وضعیت رو متصل نشون می‌داد؛ در حالی که ممکن بود ترافیک واقعی اینترنت قطع باشه و لود نشه. حالا ابزار یک ریزالور خارجی رو هدف قرار میده و باید ۲ بار پشت هم موفق بشه. یعنی وقتی می‌نویسه Connected، واقعاً متصله.
🔵
اضافه شدن انتخاب ترنسپورت برای MASQUE:
توی بخش Advanced الان می‌تونید نوع پروتکل ارتباطی MASQUE رو تغییر بدید:
HTTP/3 (QUIC):
حالت پیش‌فرض؛ سریع‌ترین هاندشیک و بهترین کارایی (اگر شبکه شما با UDP مشکلی نداشته باشه).
HTTP/2 (TCP):
کاملاً شبیه به ترافیک عادی HTTPS؛ مناسب برای زمان‌هایی که شبکه شما UDP/QUIC رو اختلال می‌اندازه یا مسدود می‌کنه.
تنظیمات انتخابی شما به‌طور خودکار ذخیره و در استارت‌آپ بعدی اعمال میشه. (این سوییچ فقط روی پروتکل MASQUE تاثیر داره و برای WireGuard/gool غیرفعاله).
🔵
به درخواست دوستان فرانت کار لوگو هم از دیفالت عوض شد
🤠
دانلود نسخه 0.4.0:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/whitedns/1196" target="_blank">📅 04:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1195">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DdNEnKMoz8op4dbTxw4_dN10lyjfeSpV-7aGF7sH3qWX8CmOXRg_HI370A3VpwqJ5O6scoYYA_r4_ze600EfroqdRf2NL9PSaImNdJER_tameR80pp9c0vSCCNaDvBg9BRVLt1-52FWsj7Os6InXNzOwJKBeI99FEUQack82SkYXy0iZRGk_DDdfLviSjDzEBel-ScZHfn6BkfXPgzwL-gBpwg11gUCrilAnqCjUuPzI7ANMRjWCOa1IhWWASUuDggODSKdPbV-WMRiypRY9vXIMpILjkJqAZZbq5qOgjFcMcNAXC0kqWARc8ZuX18k0X24fsLcnhc1smzsvKoHIDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
راهنمای جامع تنظیمات APN اپراتورهای ایرانی
📱
📥
۱. مراحل تنظیم در اندروید (Android):
1. وارد
تنظیمات (Settings)
شوید.
2. به بخش
اتصالات (Connections)
یا شبکه و اینترنت بروید.
3. بخش
شبکه‌های موبایل (Mobile Networks)
را باز کنید.
4. وارد گزینه
نام نقاط دسترسی (Access Point Names یا APN)
شوید.
5. روی
افزودن (Add / +)
بزنید تا APN جدید ساخته شود.
6. فیلدهای
Name
و
APN
را مطابق لیست زیر پر کنید (بقیه گزینه‌ها مثل پروکسی و پورت حتماً خالی باشند).
7. از منوی سه نقطه بالا گزینه
Save (ذخیره)
را بزنید و آن را فعال کنید.
🍏
۲. مراحل تنظیم در آیفون (iOS):
1. وارد
تنظیمات (Settings)
شوید.
2. به بخش
Cellular (تلفن همراه)
بروید.
3. گزینه
Cellular Data Network
را انتخاب کنید.
4. در بخش
Cellular Data
، روبه‌روی گزینه
APN
مقدار مربوط به اپراتور خود را (از لیست زیر) وارد کنید.
5. یک‌بار اینترنت گوشی یا حالت پرواز را خاموش و روشن کنید.
📋
لیست مقادیر APN اپراتورها (برای کپی آسان روی کلمه‌ها ضربه بزنید):
🔹
همراه اول (MCI)
* Name: MCCI Internet
* APN: mcinet
🔹
ایرانسل (Irancell)
* Name: Irancell-GPRS
* APN: mtnirancell
🔹
رایتل (RighTel)
* Name: RighTel
* APN: rightel
🔹
شاتل موبایل (Shatel Mobile)
* Name: Shatel Mobile
* APN: shatelmobile
🔹
سامانتل (Samantel)
* Name: Samantel
* APN: samantel
🔹
تالیه (Taliya)
* Name: Taliya GPRS
* APN: taliyagprs
⚠️
نکته بسیار مهم:
اگر در فیلدهای
Proxy (پروکسی)
یا
Port (پورت)
در تنظیمات گوشی شما هرگونه عدد، آدرس یا کلمه‌ای وارد شده باشد، سرعت اینترنت شما به شدت افت خواهد کرد یا کاملاً قطع می‌شود. حتماً بررسی کنید که این دو بخش کاملاً
خالی
یا روی
Not set
باشند.
@whitedns</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/whitedns/1195" target="_blank">📅 16:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1194">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1194" target="_blank">📅 13:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1192">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :   ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.    پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1192" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1191">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1191" target="_blank">📅 12:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1190">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/G-MNg8XEQDsmyoQdyLpwGLZvKkTXOsnLzoZ48mPbqwJww_q2EvtdShWT_8gVnUuesn-tqh_GkHngma7RZEBsOf9uIK4vXhby7zlwVZuFonN28mitruWtIJzl6umJMn6OgXOiWcnw0EAuQokQXuFfX6qSBS9QQATfT86hWocqkrJ49jYX0fOsITotqgis0C3RGWVr_y2PpvgzhWfDwUcg5w7XQpqWZ9VkllfHZ2Ji8JjJOsZdjak4RBWfpLZSXicVmTIxHAAdokYfkWPD_r2a7rZeC_NQk9wOz5WNKRp3e-ho8Qj73k6qDsFZx3COnGey1tgDDwqRY7EH-MbBcXae-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/whitedns/1190" target="_blank">📅 12:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1188">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🛡
ورژن جدید WhiteDNS VPN
👆
👆</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1188" target="_blank">📅 11:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1183">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/whitedns/1183" target="_blank">📅 11:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1182">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLn4o3GfpsyM2FUc0jdMYkRhHxZvIkuMrHTb6vK0RbhZuKU8Fu0kLHKPFrHYrltE8Z4DnZyCV0QGhDGghfaQcndRmaD3pj3UXYOs_VW-YohBkev91zDY8o4b59BKdxYbAX5zmoNf2UzlSue668EfNcr-YPMEjMPrUKrLR4a33lbiZn6MXKnFU4l-DBg8HFROE8I0R10aOMX_Kq-FW5FhJpGasxwPrxKf8tmDpi70pCWjrALitEjAjBRN1T_t8EJtT9p0Ko1buoesUMhYvss958GrovdTlpdj1KrNXvTRjt1F6_gWn8CZ0qgU5keTikTvVbbimUA2Elkh_fGl2OYwhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/whitedns/1182" target="_blank">📅 11:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1181">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1181" target="_blank">📅 08:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1180">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/l-IvIrZSGG38-lGqEdt4M0NlBigKh90fwGVcjXi2qfOpHDmxiV1NCX-VI6X3F_96wayPiIFL5cWix_VPaSkcSucZqe-nNbVyNQLuKOiEqH-7IPzl8kb1R2-9u0MWuhoEa0wUrpyamWkPLsrVHDHR8GZd12m3AMfTCwaK5at1nxvb2d7Pqvc3v9eIUBzZQ_F9qza5m2d8Rx8Jfpt6BFvKmb96sxfN3FjLIUrVPGxbwGB-a0cZXLSayPb00m0bZpCXgJTrI8cIOBTpxRtv2TEr3WtxCTW9owq57z45TH5kBvkrZfKZnaubJBKQIwxMzIJAab1yaMaNgE3Ljrp0R8h9Dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/whitedns/1180" target="_blank">📅 08:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1179">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✍️
در مدتی که اینترنت وصل بود، تیم ما تلاش کرد ابزارها و روش‌های جدیدی آماده کند تا در صورت بروز قطعی شدید، بتوانیم بهتر از شما پشتیبانی کنیم.
متأسفانه بسیاری از این ابزارها را تا امروز منتشر نکرده‌ایم که برای این تصمیم دلایل منطقی و امنیتی وجود دارد.
در صورت شروع محدودیت یا قطعی گسترده، تلاش می‌کنیم این روش‌ها را به‌تدریج معرفی و در اختیار شما قرار دهیم.
برای شروع، تعدادی سرور MasterDNS نیز منتشر خواهیم کرد. با این حال، پیشنهاد می‌کنیم در صورت امکان، یک سرور تهیه کنید و با استفاده از ربات زیر آن را به‌سادگی کانفیگ کنید:
@WhiteDNS_installer_bot
❤️
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/1179" target="_blank">📅 04:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1177">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lFipnzRwMRbYA20FLPILoFF6FQPy_4l1YFba2CxwkTr0MKvV9vJAI0Cxv5MxywZg5K7QPbl82Ub5UssWcg075P-gmpKacvoFtiZXtQTz7OyI0t7ZMaXT3SvClqEXILyuSP1J6e24D4RZ-xmmst4IHMI7L6sqmgAgKokySFVtcpmH7qwTkEPgE9FG9hiQK-sasPm1X4Zn0URCj5zAXim3VO8ju-Ux8m-1_I2TmDX5fzuLmFt8_5TvotqC6a14mnEkhy8GMqjskklJORoVFAzBW6ZRpLa5jwX3n-XplZ6WqGmiuvjHBAUQ1HIIN-OZuhIFzroyRGMMjh8UuXx1gX9bXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsResponder_bot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/1177" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1176">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VBLSfLz43nCE2eUWkuUcJTrRKdQtfkxFtLWr389hNoEo-Jye08ei0w73gRAtYcE-AiWRUsaCk-bSFOAtbAs3Va_Q6qcv30-Kb3_9glu7vvkYKXoZ5-2RNWWWZed1NaGu-Op76C3oC5FBgThRLkp9mO2EcdP-mrqvrICbQQ-ql1fKiRRFru0It-FuCl01vZ8j0iNW1P3tCPQi86zkNNDm_hidfSraQbFIm_CSjfMFJ3Lfxmd1N0P0RSnAxhBQjBcxKfqDlu7BdnP7uo6UhiddZ07tRdAMw2OQLZr_Ev_dp_C5m-obI29ORHz0UF4z1hlD6yqmvaRHcvtJUB554xFDOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
OnionHop V3.7.2 - انتشار جدید: اتصال هوشمند و عیب‌یابی شفاف
آیا می‌خواهید ترافیک سیستم خود را بدون درگیری با تنظیمات پیچیده از شبکه Tor عبور دهید؟ OnionHop، ابزار متن‌باز، سبک و قدرتمند ویندوز، برای همین کار ساخته شده است. نسخه جدید 3.7.2 تمرکز ویژه‌ای بر پایداری در شبکه‌های سانسور شده و شفافیت عملکرد دارد.
✨
امکانات و قابلیت‌های کلیدی:
🛡
حفاظت دوگانه:
انتخاب بین حالت
پراکسی
(سبک) و
VPN
(سیستمی).
🌉
عبور از سانسور شدید:
پشتیبانی کامل از Bridgeهای Tor، شامل
obfs4
,
Snowflake
,
WebTunnel
,
meek
, and
dnstt
.
🌍
انتخاب کشور خروجی:
امکان انتخاب دقیق کشور نود خروجی (Exit Node) برای تغییر موقعیت جغرافیایی.
🔒
امنیت بالا:
شامل
Kill Switch
(قطع خودکار اینترنت در صورت قطعی Tor)،
DNS امن (DoH)
و پشتیبانی از
IPv6
.
🚦
تونل‌بندی هوشمند (Split Tunneling):
انتخاب کنید کدام برنامه‌ها از Tor عبور کنند و کدام‌یک مستقیماً متصل شوند.
🤖
اتصال هوشمند (Smart Connect):
قابلیت جدیدی که به طور خودکار بهترین استراتژی اتصال، موتور Tor و Bridge را برای شبکه شما انتخاب می‌کند.
📢
مهم‌ترین تغییرات نسخه v3.7.2:
۱. تشخیص و تأیید ۱۰۰٪ پل‌های WebTunnel
در نسخه‌های قبلی، برنامه فقط آنلاین بودن CDN را بررسی می‌کرد. در نسخه ۳.۷.۲، OnionHop یک
اتصال آزمایشی واقعی (Handshake)
با خود پل برقرار می‌کند تا مطمئن شود که آیا واقعاً ترافیک را عبور می‌دهد یا خیر. این یعنی دیگر پل‌های خراب به اشتباه «سالم» نمایش داده نمی‌شوند و شما زمان را برای تست اتصال‌های مرده تلف نمی‌کنید.
۲. عیب‌یابی شفاف با لاگ‌های دقیق
اگر یک Pluggable Transport (مثل obfs4 یا Snowflake) به هر دلیلی اجرا نشود، دیگر با پیام‌های مبهم مثل "status code 2" مواجه نمی‌شوید. OnionHop قبل از اجرا همه‌چیز را بررسی می‌کند و دلیل دقیق خطا را در لاگ‌ها نشان می‌دهد؛ مثلاً: فایل اجرایی خراب است، نسخه اشتباه پردازنده است، یا مجوز دسترسی وجود ندارد.
🛠
راهنمای قدم‌به‌قدم اتصال (How-To Connect Guide)
براساس اطلاعات مخزن گیت‌هاب، نحوه اتصال بسیار ساده است:
نصب و اجرا:
فایل نصبی (.exe) را از لینک زیر دانلود کرده و اجرا کنید.
اولین اجرا (انتخاب حالت):
Proxy Mode (پیشنهادی):
اگر فقط برای مرورگر یا برنامه‌های خاصی به Tor نیاز دارید، این حالت را انتخاب کنید. نیازی به دسترسی Administrator ندارد. باید تنظیمات پراکسی برنامه خود را روی
SOCKS5 127.0.0.1:9050
قرار دهید.
TUN/VPN Mode (دسترسی ادمین):
اگر می‌خواهید
تمام ترافیک ویندوز
(کل سیستم) از Tor عبور کند، این حالت را انتخاب کنید. این کار با استفاده از Wintun و sing-box انجام می‌شود.
انتخاب پل (در شبکه‌های فیلتر شده):
به بخش
Scanner
بروید. اگر در شبکه‌ای با محدودیت هستید،
Bridges
را فعال کنید و روی
Scan
کلیک کنید تا برنامه‌ها پل‌های سالم را برای شما پیدا کنند.
اتصال:
روی دکمه بزرگ
Connect
کلیک کنید.
Smart Connect:
برای راحتی بیشتر، می‌توانید Smart Connect را در حالت خودکار قرار دهید تا برنامه خودش بهترین تنظیمات را اعمال کند.
🔗
لینک‌های رسمی
🔗
متن‌باز و رایگان
#اوپن_سورس
🚀
دانلود مستقیم نسخه V3.7.2:
https://github.com/center2055/OnionHop/releases/tag/v3.7.2
🌐
وبسایت رسمی:
https://www.onionhop.de
@whitedns</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/whitedns/1176" target="_blank">📅 14:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1175">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns16.7.2026.txt</div>
  <div class="tg-doc-extra">18.3 KB</div>
</div>
<a href="https://t.me/whitedns/1175" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@whitedns
🔗</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1175" target="_blank">📅 12:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1174">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/be2Jbep8BxLHHImVdTswxw3VIgd1cr2gEusDB2gBrTxHq6w-Ym0UKeRluK3iP2nxRI5MZhAUQw2MCPQKp1s3z_9LPJmfWVggdsPaGPIHzaBBnDc8xu2vmjhb1H1nhw_7V-XbzwuYm9fQ0T17R5MKk5a7d0QdiEBRhdVY-JkXEz9zaTDTm1L_c8CTLQIz8e6jP-BpZCnfZix393yuZk5yR3FOhfb74qeZpI6M8i28I7Kkq8loo9wsDFQaUXliyaATEus8OpxsMdgl3EMqwwUb_Z65SknoBpJRWlKpzQUV187R6_o9fIArD64t93hJgzoQLgck1GM1Q-f5El2nXTAkHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">16.7.2026
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1174" target="_blank">📅 12:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1173">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1173" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1172">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/G42P38BpkmwvmlQ25c_Dle17Zt-3TRsN7kHcjNNkL0chC211kNBVNmAnQLc6N1G91dtqYrJfml_soOAVqKMZ0nd4JpPtanr-w21OgK-tTB7yN2OxVzbQvFyylSSbjP4ULENClzZtICIK8UjAPJ2QmzyvDw50rJk1MxQYlwSSEECHRbKDHvh2D0JYOik3AscpqKLwDIDdTvtL65jHz80KyaJegJ52qwSfux8yfSRw6gPJqxoIpgADJZTxG9vlfK13BAYdXa4-kV00SggrZUpgyA_FtEcz8VYdjvgPgNjmREac8W7Tmg0icYIZO3_2IsIQujVYTeeBRYKtMVXbPzDVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش جامع استفاده از
WhiteDNS VPN
و
WhiteDNS Scanner
برای اتصال امن و پرسرعت!
🚀
🛡
رایگان
در این ویدیو به بررسی تخصصی ابزارهای اختصاصی *WhiteDNS* پرداخته شده است که به شما کمک می‌کند بدون نیاز به دانش فنی پیچیده، به اینترنت آزاد متصل شوید.
🌐
🔓
خلاصه‌ای از مباحث آموزش داده شده:
📝
راه‌اندازی WhiteDNS VPN:
نحوه نصب اپلیکیشن و اتصال اولیه بدون آی‌پی تمیز (0:00 - 5:30)
⚙️
📲
*
اسکنر قدرتمند WhiteDNS:
آموزش کامل کار با بخش *IP Scanner* برای پیدا کردن آی‌پی‌های تمیز و پرسرعت (7:40 - 18:00)
🔍
⚡️
*
کاربردهای حرفه‌ای اسکنر:
بررسی قابلیت‌های پیشرفته مانند *SNI Scan*، *HTTP Proxy Scan* و *Config Maker* برای ساخت کانفیگ‌های شخصی‌سازی شده (20:30 - 27:30)
🛠
🔧
*
نکات طلایی:
نحوه استخراج آی‌پی‌های تمیز از دیتاسنترهای مختلف و استفاده از آن‌ها در برنامه‌هایی مثل *v2rayNG* و *Psiphon* (22:40 - 25:00)
💎
🌍
✅
این ابزارها با رابط کاربری ساده، برای همه کاربران (مبتدی تا حرفه‌ای) مناسب است.
👨‍💻
👩‍💻
📥
لینک‌های دانلود:
- دانلود اسکنر: [GitHub WhiteDNS]
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.5
- دانلود اپلیکیشن: [Telegram Channel]
(
https://t.me/whitedns/1072
)
💬
با تماشای این ویدیو، سرعت و پایداری اتصال خود را به شکل چشمگیری افزایش دهید!
📈
🚀
لینک ویدیو :
👇
https://www.youtube.com/watch?v=N5hKuWXp37w&t=57s
@whitedns</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1172" target="_blank">📅 11:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1171">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Fw-YCAluCm00WwzG70Cdb-zqmokwg9HIZ3vaWaP2a0fqemNWehatNp5iCtKgaMxkTr2T7A1L-Vk-DyaSYhbnXfNo-217UmWjrdZLaud3V1z7uhu6QL3sFakV6RM-55gDonqqrAKs9U_uLeYQUB_hwL76zcDTMA5pHL-eflZjRILBTGSF1NMr76LFckA-p_p_EqMvjy3TrVTDmhON6LeIME81an-c35Wo-oWCE0xPPFuqcjOcM4t3nGReVL7PI4eP6E82MTJkwh2FDCXbLbuV99OBSpmSV355T3f-p9Oz6qfatkKZgyzNvmjZVx_8x1Ud83oU7O8CkI_r-bP3sDf-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش کامل راه‌اندازی V2Ray با پنل قدرتمند 3x-ui از صفر تا صد!
🎓
اخیراً با کاهش محدودیت‌های اینترنت، روش‌های باکیفیت و پایدار دوباره فعال شده‌اند. در این ویدیو،
WhiteDNS
🛡
تمام مراحل راه‌اندازی سرور شخصی و فیلترشکن اختصاصی را به زبان ساده و کاربردی آموزش می‌دهد:
🔹
سرور و دامین:
نکات کلیدی برای انتخاب سرور خارج و ثبت دامین در کلادفلر
☁️
.
🔹
نصب پنل 3x-ui:
نحوه نصب این پنل کاربردی با استفاده از هسته Xray بر روی سرور
🛠
.
🔹
ساخت Inbound:
آموزش مرحله به مرحله ساخت اولین ورودی برای فیلترشکن
🔄
.
🔹
تنظیمات کلادفلر (Cloudflare):
نحوه ثبت DNS ریکوردها و تنظیمات امنیتی ضروری
🔒
.
🔹
استفاده از آی‌پی تمیز کلادفلر (Cloudflare Clean IP):
روشی برای بهبود سرعت و دور زدن فیلترینگ با جایگذاری آی‌پی‌های تمیز
🚀
.
🔹
ساخت کاربر و استفاده از کانفیگ:
نحوه اضافه کردن کاربر و دریافت کدهای تنظیمات برای استفاده در برنامه‌هایی مثل v2rayNG
📱
.
این ویدیو یک راهنمای کامل برای کسانی است که می‌خواهند فیلترشکن اختصاصی خود را با امنیت و سرعت بالا راه‌اندازی کنند. اگر هنوز شروع نکرده‌اید، این فرصت را از دست ندهید!
✨
برای دیدن آموزش کامل، روی لینک زیر کلیک کنید:
👇
🎥
https://www.youtube.com/watch?v=vVjqNQBUGIc
🆔
@WhiteDNS</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/whitedns/1171" target="_blank">📅 09:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1170">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mSQf6Ec3vnLEd_Vw-QSLHgAq4f50ARBC8ZrEsU-nJGv2XMHXRU9a9DbXQop4nTLvDP-GO80Wuui9ex7vrdsjSfUVSmuQ1tiT-zqhNosYb87j871EHezQdg47fJmPrgbB7RafeZR2w_7nGHiekBzJ3Prvr_ENIlcxYyVjzQhVwOTO5CXZggOrx8aCRZLJPw10luXSdd_GwzgTZ6RogQ8SuSTkhEASbsQfojUjG4DgktL5f74oRSSwBA-f-CGguMXvVSahNf8ZU8vuBazZNuPy9Z1zOf254AiYi9JPxgpm3BpvR9n4GV6p8cIodsO_ivLwfNlL6vCwtt_GoDywYL0Rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
اتصال رایگان و پرسرعت با پروژه Aether + پروتکل ویژه گیم Wireguard
⚡️
لینک پروژه‌ی اصلی:
https://github.com/CluvexStudio/Aether
لینک پروژه GUI من:
https://github.com/MatinSenPai/Aether-GUI
دستور نصب از ترموکس:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
دستور غیرفعال کردن محدودیت مصرف CPU و باتری:
termux-wake-lock
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره. حتی نیاز به اکانت کلودفلر هم نداره
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/whitedns/1170" target="_blank">📅 13:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1169">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/U3ZhUgEpE4brPD1-CVi9dMMXdsTgHec3rNjNCrgCyRsuFXnIpyd0a4Wr_Ml4LvMDtwCmDe1oaWMiu5WYyO_g9Z6I7aJudn_w2QXHyysLDl7Jp58OH0nU9leB6Vg7H1RRSEQL20uN8D1j9VNJaw3SnrrBXkvFr_t00QJ99FOfdJtl-juKSxWiHV3uJQ94FB-WCAASovAIhZGcZZHdAS2zKI8wcd7DRCU9gztY9ZVygIvjT57tOmnC0D6ZtpddlVQvfsG_5mXvrj97fq0lyMpGcqd0DTG9zxXeP915ZgM5tMqcUYLvriJ6Zm4koP-kTMWP2FwdWRz5MOXrn-chbPFuJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر برای استفاده از سرویس‌های هوش مصنوعی (AI) مشکل دارید
🤖
این پراکسی را چک کنید
🔍
برنامه یک اپلیکیشنِ نوار منو (Menu bar)  و یک داشبورد محیط ترمینال است که به عنوان یک
مرکز کنترل و مانیتورینگ برای ایجنت‌های Claude Code
عمل می‌کند.
به طور خلاصه، این ابزار کارهای زیر را انجام می‌دهد:
نظارت یکپارچه بر ایجنت‌ها:
وضعیت تمام ایجنت‌های در حال اجرای Claude Code را در یک نگاه نشان می‌دهد؛ بنابراین دقیقا می‌دانید کدام ایجنت در حال کار است، کدام متوقف شده (خطا داده) و کدام منتظر تایید شماست.
بررسی وضعیت اینترنت و سرور:
به صورت مداوم وضعیت اتصال اینترنت شما و سرورهای Anthropic را چک می‌کند تا در صورت توقف کار ایجنت، دلیل واقعی آن (مثلاً کندی اینترنت یا مشکل خودِ Anthropic) را به شما بگوید.
حفظ لوکیشن (Location Fencing):
ایجنت‌های شما را روی یک کشور خاص قفل می‌کند. اگر VPN شما قطع شود، به جای اینکه ایجنت‌ها با خطای دسترسی (مانند خطای 403) از کار بیفتند، درخواست‌های آن‌ها را موقتاً متوقف نگه می‌دارد تا دوباره به اینترنتِ همان کشور متصل شوید و کارشان را از سر بگیرند.
ردیابی مصرف (Usage Tracking):
میزان مصرف واقعیِ محدودیت‌های اکانت شما را (با خواندن دیتای خود Claude) به طور دقیق نمایش می‌دهد.
https://ghhrmnzdh.github.io/tower/
🔗
@whitedns</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/whitedns/1169" target="_blank">📅 09:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1168">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns 15.7.2026.txt</div>
  <div class="tg-doc-extra">48.7 KB</div>
</div>
<a href="https://t.me/whitedns/1168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1168" target="_blank">📅 09:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1167">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/r-pr7XXwXsILQn6xdWT_pNAZjvfRTthKc_HrLNmNqWdSaUszh-HgamR0WB8Dh7uW2VbuGGlSSZBmaOcykoKQ_JIAStpLF9_IaUZEAQ3eb-DIK2kZGfZRA99x6uGfmS5mA1qU79IWqG8JW4MFeiQgEkYnN7P1QuIqAVueAA5PJ_P8EbEK2cOn5xgvxsT0L7mhxgV85rOEM80hFRl8gF4gAENmKXEc4QF3D0xCiTw1oF22TSO0OWeid4SdLsxvfYGJiYJdyAcoq1QdRJ0EpQdqoTL8I3e8F_WjHLtwseLbHrd_h4qPtvU5jonrPjZGlUFvWjcYsGvIWFqgVFZAAfDhwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">15.7.2025
📅
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1167" target="_blank">📅 09:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1166">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سلام به همه
👋
یک موضوع مهم که خیلی از کاربران VPN با آن آشنا نیستند، مسئله‌ی DNS Leak یا همان نشت DNS است.
شاید برای شما هم پیش آمده باشد که VPN روشن است و آی‌پی شما تغییر کرده، اما بعضی سایت‌ها یا سرویس‌ها همچنان شما را به‌عنوان کاربر ایرانی شناسایی می‌کنند یا دسترسی‌تان را محدود می‌کنند.
DNS نشت یعنی چه؟
وقتی وارد یک سایت می‌شوید، دستگاه شما ابتدا از یک سرویس DNS می‌پرسد آدرس واقعی آن سایت چیست. اگر این درخواست به‌جای عبور از داخل VPN، از طریق اینترنت اصلی یا شرکت ارائه‌دهنده اینترنت شما ارسال شود، به آن DNS Leak می‌گویند.
به زبان ساده، با اینکه VPN روشن است، بخشی از اطلاعات اتصال واقعی شما هنوز قابل مشاهده است.
چرا مهم است؟
DNS Leak ممکن است باعث شود:
• موقعیت یا کشور واقعی شما تشخیص داده شود
• بعضی سایت‌ها همچنان دسترسی شما را محدود کنند
• حریم خصوصی شما کاهش پیدا کند
• اتصال VPN شما آن‌طور که انتظار دارید کامل و امن نباشد
چطور تست کنیم؟
1. ابتدا VPN را روشن کنید
2. وارد سایت زیر شوید:
https://ipleak.net
3. چند ثانیه صبر کنید تا نتیجه نمایش داده شود
4. بخش DNS Addresses را بررسی کنید
اگر در نتیجه نام شرکت اینترنت شما، کشور واقعی شما یا DNSهای مربوط به اینترنت اصلی‌تان نمایش داده شد، احتمالاً VPN شما DNS Leak دارد.
پیشنهاد می‌کنیم همیشه از VPNهایی استفاده کنید که نشت DNS ندارند تا هم حریم خصوصی بهتری داشته باشید و هم سرویس‌ها کمتر بتوانند موقعیت واقعی شما را تشخیص دهند.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/whitedns/1166" target="_blank">📅 08:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1165">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Whitedns-14.7.2026.txt</div>
  <div class="tg-doc-extra">241.5 KB</div>
</div>
<a href="https://t.me/whitedns/1165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1165" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1164">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lJfXh54-4Gy6WIt6HNgivMq7no5pGVZAiFcva5zLODtc4F9Xb9CvTNd3f3NNTh7O968Br4raEb7t_ffhiMEV4foXfIA8baoUGFb6kLnNRDe1fU_S3Tj2bxJaJeF7_nxrKGBawVa81J7nzwuMfk6GHaM2zn-rPTVKf0X99jLOJuDXnUswYe0FoCFxYoOeMA3zw0JGdbk4UKYrXoUmbGinipF_HPz8nWo2AsaRm_v8QeR1cUo2Cud51TuwonICgeLMDY-gqwNERktSqZFcfNSG7xcLOAfmfDUpvyxGAftNH4rNjkXkdFgkB2hF781JLS8008VaiHZpf46cz058m7Lqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14.7.2026
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/1164" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1163">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Aesi7cIzNHM-rHoICtM8jKmIDqrRhq05zBFn6Y25aNXt8GEdxCTEWFlBz9MI6kF39lHVCRwUueJTBBBD2lL-N79XJKygio_Wbx4l3dS17woIeqTmzbyPrOS8ihN_pnX6EzJ4_U9T8uMWhjhO1kaY5KWPf8kq8a8HDOd705aCih4E0u93Azw39J7H3iqRQjNzxEwxCgGOcEE7cSrXH6hheqSsfGIL4Z_AiliunrE2RpnDgeHuI7MyNwVq3OOKkfkc7uEM5ztupASWxwO4a3BANxfy1B9ZnwoGeDiy3K3lTfUgCethYEGgAQUMS0PKZl2TaqM2UFxA3S5HwOPUNPrkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsResponder_bot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1163" target="_blank">📅 17:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1162">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">White DNS
pinned «
👆
⭕️
⭕️
⭕️
⭕️
موقت :   پرونده اتصال سریع و اسان برای افرادی که دانش و امکان درست کردن کانفیگ ندارند با چند پست بالا بسته شد   این مدل اتصال در صورت قطعی  سراسری کار نخواهد کرد
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1162" target="_blank">📅 17:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1161">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👆
⭕️
⭕️
⭕️
⭕️
موقت :
پرونده اتصال سریع و اسان برای افرادی که دانش و امکان درست کردن کانفیگ ندارند با چند پست بالا بسته شد
این مدل اتصال در صورت قطعی  سراسری کار نخواهد کرد
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1161" target="_blank">📅 17:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1156">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-IP-Scanner-x86_64-release.apk</div>
  <div class="tg-doc-extra">15.6 MB</div>
</div>
<a href="https://t.me/whitedns/1156" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر براتون سوال پیش اومده که لیست ipfronting ها را از کجا آوردیم . پاسخ خیلی ساده است
😊
👇
با استفاده از Whitedns Ip finder
🛠
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases
📂
@whitedns
📱</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/whitedns/1156" target="_blank">📅 17:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1155">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/eLq8xgtlGRxk52SgC9gR2r_hJ8xSBnPQTemuCiSb5bgQpHoYujj69ieJiuWoTInCRg_hBo4Z9P5nrGKqyRVfbX6ywd8VBgKO2UXoL3z8fxcoG3zgxAxL_tjrmXWg1cVFceLm39_mu_0E114-jNm-c-KrtOj8XN4DAV0NIUZSTNlBa7ALu2jU7Wl6voScK4ExPQRIQX6P8AnAoDCHyVIwUbeBPkIjHB4AdkKUzWzC13_OrcN5ZVRTtR4CqMclFTcOkBzGsI-csiVAqQDPLg-tixgd2kfQWoMQwx7RG0Fmqp-zmk1hp6ibUgL6jmRjcLIVtCc27u_cu8rbxW7qHcNt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1155" target="_blank">📅 17:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1154">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZxEwBf56dDNX7sN23UTbw3ltt90cDUvAzWWfLRW4k12Zgte2-m6t6lt8u342wxAod-Y-xkWNgVqHid35IsIQYosS78cCE482220qK8yLGsTMKpHMqBOI3rfXojB1rSzHYMTSGDahT9t_iqEpCuyUuZt2_mZEeRukBoxtMi5yzJWabNGXu8D5YKU4kAEbaNDw4JFmJXPR563hhh1wI58MpfqMPSOSqumklSzzxcFfFMbYj2hcrwYgxvaucAiTl1fAP37JE509yDIf1U1bigMs3xWyblIrQ8NAi5TY4DBtSjcjZPcwOz6eICagpkm3VzfijvpR3pTDcMJr9CUgyBXXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان :
در صورتی که موفق نشدید با برنامه whitedns vpn وصل بشید
🙄
🔌
وارد قسمت advanced بشید و ای پی های زیر را دونه دونه امتحان کنید
👇
🛠
2.189.86.45
2.189.86.102
2.189.86.42
2.189.86.46
2.189.86.41
185.8.173.179
2.189.86.44
45.149.77.160
194.62.43.166
94.101.184.211
37.152.185.169
37.152.182.54
185.226.118.234
185.231.182.55
185.226.118.234
185.231.182.55
185.226.117.67
185.228.236.4
2.189.86.43
2.144.21.79
2.144.21.120
2.144.21.79
2.144.23.129
2.144.21.120</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1154" target="_blank">📅 17:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1152">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">White DNS
pinned «
دوستان :
👋
یک مورد کوچیک در مورد whitedns VPN بگم
📱
این اپلیکیشن بر اساس کانفیگ های متناسب با هسته x-ray یا سینگ باکس هست ، به طور مثال vless ,vmess, Trojan ,....
⚙️
اگر وصل شد حتما اول با مرورگر یک تست بگیرید
🌐
، اگر هیچی باز نشد ، دکمه refresh را بزنید…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1152" target="_blank">📅 16:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1151">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دوستان :
👋
یک مورد کوچیک در مورد whitedns VPN بگم
📱
این اپلیکیشن بر اساس کانفیگ های متناسب با هسته x-ray یا سینگ باکس هست ، به طور مثال vless ,vmess, Trojan ,....
⚙️
اگر وصل شد حتما اول با مرورگر یک تست بگیرید
🌐
، اگر هیچی باز نشد ، دکمه refresh را بزنید
🔄
اینقدر این کار را تکرار کنید تا یک کانکشن پایدار متناسب با وضعیت شما براتون پیدا بشه و هر بار تست کنید روی مرورگر
🧪
✅
تیم whitedns
👥
@whitedns
📩</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1151" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1146">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1146" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اپلیکیشن Whitedns vpn 0.0.8
📱
یک برنامه بر پایه هسته‌های x-ray و singbox است که بدون نیاز به وارد کردن اطلاعات و تنها با فشردن دکمه‌های Connect یا Refresh، به راحتی یک اتصال اینترنت مناسب ایجاد می‌کند
🚀
🌐
.
ٌ
@Whitedns</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1146" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1145">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Hk-ME3IiiQIZ3fbHNB8uK-8aXPUp4kJ17FjOHXwvMg2D7wILpDEEKatvG5ZZwaUPJhZ0n49upMnRNCqtFj9APR8t8SjT3f5WGUXY2y5jf7dFYWB8XP2guLu0t1qJ4qj2D5WjAXgMo6A-THJvQAMuMnODt2Hqib67viRhYpLhq4Wq42FUzTXmQYy0UAsPSBuxQaVsWUaVNHsdxxO52KbMgIEP63KRxS9sRQ11BSdgJT_hj4QDkjefWkDZxyfVgiDVdfwImqNGj7jMOEfGGhD2Y2Waz57zz0ec3SFbQ6rhC48nPjpLuc-Pgd9XCuf9CJ-mt2gWvvNdn_Ev492l9Y6chw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1145" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1144">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برای اینکه دوستان قاطی نکنند، ما دو نوع اپلیکیشن برای اتصال داریم
📱
:
۱
. اپلیکیشن بر پایه پروتکل‌های DNS محور مثل masterdns, stormdns, ...
🌐
مثل Whitedns 1.5.1
۲. اپلیکیشن بر پایه هسته‌های x-ray, singbox که پروتکل‌هایی مثل vless, vmess, ... دارند
⚙️
مثل  0.0.8 whitedns vpn</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/whitedns/1144" target="_blank">📅 16:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1136">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-poll">
<h4>📊 وضعیت اینترنت چطوره ؟</h4>
<ul>
<li>✓ ☺️مثل قبل هست  , وصلیم</li>
<li>✓ 😔اختلال داره ولی وصلیم</li>
<li>✓ 😡اختلال شدید ، به ندرت وصل میشیم</li>
</ul>
</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/1136" target="_blank">📅 16:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1135">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🛡
مدتی پیش اپلیکیشنی برای اسکن Resolverهای متد DNS ساختیم که می‌توانید آخرین نسخه‌ی آن را از لینک زیر دانلود کنید:
https://github.com/WhiteDNS/IP-Range-Scout-Android/releases/tag/v0.1.2
اگر امکان اسکن Resolverها را ندارید، می‌توانید از ربات ما استفاده کنید:
@dns_resolvers_bot
همچنین اگر برای اولین‌بار از WhiteDNS استفاده می‌کنید، پیشنهاد می‌کنیم در گروه اصلی، تاپیک «اولین شروع» را مطالعه کنید.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/whitedns/1135" target="_blank">📅 03:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1134">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه. با توجه به شرایط کنونی خاورمیانه، ترجیحا هم اپلیکیشن WhiteDNS را نصب/آپدیت کرده و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/whitedns/1134" target="_blank">📅 03:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1133">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
با توجه به شرایط کنونی خاورمیانه، ترجیحا هم اپلیکیشن WhiteDNS را نصب/آپدیت کرده و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/whitedns/1133" target="_blank">📅 00:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1129">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO2PUUfCZehrxNRt-S_fSaHJcPNkVZI1PY-jakiLoH9hF1WpkxPMS5xaRHG7lpvPDcH1ZIcRYuGlX5BIG8SGlpABSe5_3hbLzr_iQJJH6-mukr2Og6FU7Kph3xc7TbmILblIqN0v8pCLEaG6OMyGtu8ZlgtmkZn81SN1d1L1WNSp3ag0vGgpJUJH3WGKMrPw35WsT37wj45MjkM2EdMyEeNw0RoorBw5B3ZL_V_3ZBCWQscdAl6VfjHEno6O6xXc2KADb5TdgFkFpopbYqIpiOnosnKqZRpXHzoT-_xPSbG6rqMJ_2znPHhXQU5ppAFUysCNy7p-LIMoC-oCtVpuig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/whitedns/1129" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1127">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1127" target="_blank">📅 14:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1126">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KOzddzdu9CByrzop0PJC7ZXeno8zumwuKkWryS3H--DFCMeKARjgMwweRwHJlGjOBHcfc00wbzz3sYAfnrKXezZx2IgUeZx2Tiqrj1T3gFQmVqmRsi689tz7yiCZQ2woW_7bzdP3yZJih1X9jKLU59cpYu43rr3TpGI5e3mvhxhqMMo-R8_On-yfiK-fv4pTcrF00Y8A63kTrM5ypVMsL0WTyXg7GfBzO9pF4105rd5ENYZRZnAPbgTojQstYQLI7dTEEBuiiMhE-K9sirc1qPxUT_ULnRD78Y7mwk2l0zMtTfefqpPztv02y0M9DuAoSjygagq5yAsiCGSG9sZwTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsResponder_bot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/whitedns/1126" target="_blank">📅 13:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1125">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">White DNS
pinned «
⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم  با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.  در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1125" target="_blank">📅 10:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1124">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌎
آموزش کامل WhiteDNS Desktop بری ازمان قطعی اینترنت
لینک مشاهده ویدیو
https://www.youtube.com/watch?v=Mc--GlKw2wg</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/whitedns/1124" target="_blank">📅 05:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1123">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم
با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.
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
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/whitedns/1123" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1122">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMasterDnsVPN</strong></div>
<div class="tg-text">👋
درود،
⬅️
ایران موشک بخوره یا موشک بزنه اعضای اینجا زیاد میشن، همه چیز آروم باشه اعضای اینجا کم میشه، تعداد ممبرای این کانال شده یه چیزی مثل «شاخص پیتزای پنتاگون»
😂
⬅️
ولی من واقعا دوست ندارم، اینترنت قطع بشه و شمارو دوباره سر همون موضوع قبلی اینجا ببینم
😕
امیدوارم وضعیت اینترنت جوری درست بشه که اعضای این کانال صفر بشن، ولی مارو یادتون نره
😁
❤️
پیروز و سربلند باشید.
🤨
با تشکر فراوان،
امین محمودی
🗓
18 تیر ماه 1405</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/whitedns/1122" target="_blank">📅 02:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1120">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/whitedns/1120" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1119">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🛡
معرفی CoreForge برای iOS فیلترشکن ساده و قدرتمند مخصوص آیفون  دوستان عزیز،  اپلیکیشن CoreForge برای iOS آماده تست عمومی شده و می‌تونید از طریق TestFlight نصبش کنید.
📥
نصب CoreForge از TestFlight: https://testflight.apple.com/join/u1vfEHur   CoreForge برای…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/whitedns/1119" target="_blank">📅 10:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1118">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🛡
معرفی CoreForge برای iOS
فیلترشکن ساده و قدرتمند مخصوص آیفون
دوستان عزیز،
اپلیکیشن CoreForge برای iOS آماده تست عمومی شده و می‌تونید از طریق TestFlight نصبش کنید.
📥
نصب CoreForge از TestFlight:
https://testflight.apple.com/join/u1vfEHur
CoreForge برای شرایط سخت اینترنت طراحی شده؛ مخصوصاً زمان‌هایی که اختلال شدید داریم، خیلی از روش‌های معمول وصل نمی‌شن، یا حتی اینترنت به سمت حالت بسته و محدود می‌ره. خلاصه برای همان روزهایی که اینترنت تصمیم می‌گیرد انسانیت را ترک کند.
این اپ دو حالت اصلی دارد:
✍️
RelayForge
حالت پیشنهادی و روزمره برای استفاده عادی
مناسب وب‌گردی، اپلیکیشن‌ها، تماس، شبکه‌های اجتماعی و استفاده عمومی
✍️
DnsForge
حالت اضطراری برای زمان‌هایی که بیشتر روش‌ها بسته شده‌اند
این حالت از تونل DNS استفاده می‌کند و برای شرایط قطعی شدید یا اینترنت ملی می‌تواند کمک‌کننده باشد. سرعتش مثل VPN معمولی نیست، اما برای دسترسی اضطراری، پیام‌رسان، وب ساده و کارهای ضروری طراحی شده.
🛡
قابلیت‌های مهم CoreForge:
• مخصوص iPhone / iOS
• اتصال ساده و سریع
• پشتیبانی از کانفیگ و اشتراک
• تست و انتخاب بهترین مسیر اتصال
• حالت Full Tunnel
• حالت اضطراری DNS Tunnel
• مناسب دوران اختلال شدید و قطعی اینترنت
• طراحی شده برای استفاده ساده، حتی برای کاربران غیر فنی
📌
نکته مهم:
DnsForge آخرین راه‌حل است. یعنی اول از RelayForge استفاده کنید، اگر روش‌های معمول جواب ندادند، سراغ DnsForge برید. اینترنت خودش به اندازه کافی اذیت می‌کند، ما دیگر لازم نیست داوطلبانه سخت‌ترش کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/whitedns/1118" target="_blank">📅 10:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1117">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♨️
معرفی ربات جدید WhiteDNS برای راه‌اندازی و مدیریت سرور شخصی MasterDNS
♨️
ربات جدید WhiteDNS آماده استفاده است.
👉
@WhiteDNS_installer_bot   این ربات به شما کمک می‌کند بدون نیاز به درگیر شدن با مراحل پیچیده نصب، سرور شخصی MasterDNS خودتان را روی VPS راه‌اندازی…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/whitedns/1117" target="_blank">📅 06:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1116">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s79rp8qDgk0gJ9wJEudfpkJdZnC443Qx7qBGsmiZoGhh_YsFnHApwkKqVjviAFmlsZXmZuLBYpVNOKJd5IkI74d0a_buFTCSyNVmcqF_fpmxMs_2Mk7oc_Z3EwanX4N_mxnh4r4Gp_RwOEWIOP-dqpAXNBBvIu0E4DfkwZrV0xEQR6A7siJQMdsTgeLnaheWc5iz_qi1B6c11XndCmSTl4B-vbpzZM4bAPDmwArEt7w73ay0vnrQ0KLAv_GJstKGAy86PW8gNVR39WC3fTAQdDiq3mTtVZOp4mL_n7KDdSO8NVgk9ef2xqjz2EpXZPhM4J5_p_yW_2U8WvkpXpzrfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
معرفی ربات جدید WhiteDNS برای راه‌اندازی و مدیریت سرور شخصی MasterDNS
♨️
ربات جدید WhiteDNS آماده استفاده است.
👉
@WhiteDNS_installer_bot
این ربات به شما کمک می‌کند بدون نیاز به درگیر شدن با مراحل پیچیده نصب، سرور شخصی MasterDNS خودتان را روی VPS راه‌اندازی و از طریق تلگرام مدیریت کنید.
✅
نصب خودکار MasterDNS روی VPS
✅
مدیریت سرور از داخل تلگرام
✅
دریافت اطلاعات اتصال و Encryption Key
✅
بررسی وضعیت سرور
✅
ری‌استارت و مدیریت سرویس
✅
مناسب برای استفاده شخصی، دوستان و خانواده
🔐
نکات امنیتی:
اطلاعات کاربر، اطلاعات ورود به سرور، رمز عبور، کلیدها و مشخصات VPS به هیچ عنوان ذخیره یا لاگ نمی‌شود.
اطلاعات فقط در همان لحظه برای اتصال به سرور و اجرای دستور مورد نیاز استفاده می‌شود و بعد از پایان نصب یا اجرای هر دستور، توسط ربات نگهداری نمی‌شود.
بعد از انجام عملیات، اطلاعات ورود و مشخصات سرور توسط هیچ‌کس قابل مشاهده یا دسترسی نیست.
به همین دلیل، کاربران همچنان مالک کامل سرور، دامنه و تنظیمات خودشان هستند.
این ربات فروشنده سرور یا دامنه نیست.
کاربران باید:
* دامنه خودشان را تهیه کنند
* سرور خودشان را تهیه کنند
* دی‌ان‌اس های لازم را روی دامنه تنظیم کنند
هدف ما این است که راه‌اندازی و مدیریت سرور شخصی برای کاربران ساده‌تر شود؛
نه این‌که همه وابسته به چند سرور عمومی و متمرکز بمانند. ما باور داریم کاربران سرعت و پایداری بیشتری با سرورهای شخصی و غیرمتمرکز خواهند داشت.
⚠️
این ربات در اولین نسخه عمومی منتشر می‌شود و ممکن است هنوز باگ یا مشکل داشته باشد.
لطفاً مشکلات و بازخوردها را برای ما ارسال کنید تا سریع‌تر بهترش کنیم.
ویدیو آموزشی خرید سرور و دامنه و تنظیم دی‌ان‌اس به زودی داخل چنل قرار خواهد گرفت.
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/whitedns/1116" target="_blank">📅 06:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1115">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✍️
دوستان :
آیدی ادمین که توی دیسکریپشن کانال گذاشته شده، برای حل مشکلات شخصی شما نیست. ممنون که لطف می‌کنید و درد دل‌های روزانه خودتون رو برای ما می‌فرستید، ولی متاسفانه قادر نیستیم پاسخگو باشیم چون تعداد پیام‌ها خیلی خیلی زیاد هست.
اینکه موبایل شما و یا کامپیوتر شما دچار مشکل شده، یا اینترنت شما کار نمی‌کنه، شرکت تامین‌کننده اینترنت شما کلاه سرتون  می‌گذاره، و یا اپلیکیشن‌هایی که ما گذاشتیم دچار فلان مشکل هست و غیره رو برای آی‌دی ادمین نفرستید، توی گروه مرتبط با خودش مطرح کنید.
آیدی ادمین فقط و فقط برای مواردی هست که شما قادر نیستید توی گروه های عمومی ما براش پاسخی پیدا کنید (که تقریبا غیر ممکن است )و یا گزارش و یا یک مورد خیلی فوری را میخواهید به دست تیم ما برسونید
در ضمن بازم تاکید می‌کنیم برای اون دسته از دوستان طلبکار و بی ادب  ، شما حقوق ما را نمی‌دید و ما هم از جایی بودجه نمی‌گیریم ، ما بدهی به شما نداریم ، بی ادبی شما جوابش فقط بلاک شدن و حذف شما از کانال و گروه های ماست ،
از امروز مواردی غیر مرتبط به هیچ عنوان پاسخ داده نمیشود
سپاس
❤️
تیم whitedns</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/whitedns/1115" target="_blank">📅 10:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1114">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا
اگر داخل پنل های نهان و bpb یا هر فیلترشکنی که دارید مشکل باز شدن یه سری اپلیکیشن ها رو دارید(تلگرام،یوتوب و...) طبق تنظیمات زیر داخل هر کلاینت برید این تنظیمات رو داره:
Dns:
💎
9.9.9.12
8.26.56.26
8.8.8.8
8.8.4.4
208.67.220.220
208.67.222.222
Fragment:
✅
Google.com
Length:10-20
Interval:10-20
Packets:1-1
💡
نکته:قسمت فرگمنت بیشتر برای مشکل آپلود یا باز نشدن اپ هاست لذومی نیست حتما روشن کنید.
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/whitedns/1114" target="_blank">📅 04:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1113">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kLMzuFCt3TRNMXTw5uUgUU83jQJMzdUMS4tL7whkghYa9KgG4tO8G1FBNESdZk11m0jleAake0lp-p0KLYNY2BMZ_I7ATraFlsJAlS414hvOoT8_Sg84drFMEmzgJ8V52K6MI9NQZPZPLcTmC_1lRpCDZ0QzZAbQ6FAI8qqrxcXDhIAaeDJCo_CVv85cN3gbe0xe9_GNeHX4ln8R85WdR0Q9CSJazOFkHupn1HWWab6Nobx45Z9uQzB1HLYlgJgHDQObGz5n4fRauPoneKuehvw-MDHO09hoix7AcHipJPAh5zzw2WFgoqV-bkWkJWZx5cokdr8v9fucq-7_jdsHSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/whitedns/1113" target="_blank">📅 20:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1110">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhitednsProxyProfiler-Android-v1.0.7.apk</div>
  <div class="tg-doc-extra">55.4 MB</div>
</div>
<a href="https://t.me/whitedns/1110" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پروفایلر پروکسی WhiteDNS نسخه ۱.۰.۷
🛠
پروفایلر پروکسی WhiteDNS یک ابزار تشخیصی برای ویندوز و اندروید است که بهترین ترکیب‌های پروتکل پروکسی/VPN را در یک شبکه پیدا می‌کند. این ابزار می‌تواند هم بررسی‌های محلی بدون VPS و هم تأییدات عمیق‌تر مبتنی بر VPS را اجرا کند.
🌐
ویژگی‌های اصلی
اسکن شبکه محلی:
آزمایش سریع بدون نیاز به اعتبارنامه‌های VPS.
🏠
اسکن VPS:
تأیید از راه دور عمیق‌تر با استفاده از اعتبارنامه‌های VPS شما.
🖥
تست پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، WireGuard، Hysteria و HTTP.
🚀
پشتیبانی از انتقال‌های TCP/RAW، WebSocket، gRPC، XHTTP، HTTPUpgrade و mKCP.
🔄
پشتیبانی از ترکیب‌های TLS، REALITY و بدون امنیت (در صورت معتبر بودن).
🔒
تشخیص دسترسی‌پذیری، فیلترینگ، پورت‌های مسدود شده، مشکلات SNI/TLS و رفتارهای شبیه DPI.
🔍
نمایش نتایج تشخیصی دقیق و اطمینان از شواهد محلی.
📊
کمک به شناسایی ترکیب‌های ایمن‌تر پروتکل، پورت، انتقال و امنیت.
🛡
نحوه استفاده
برای یک آزمایش سریع بدون VPS، گزینه
اسکن شبکه محلی
را انتخاب کنید.
⚡️
از
تنظیمات پیشرفته
برای تست پروتکل‌ها، پورت‌ها، مقادیر SNI، انتقال‌ها و انواع امنیتی بیشتر استفاده کنید.
⚙️
وقتی به شواهد قوی‌تر سمت سرور نیاز دارید، گزینه
اسکن VPS
را انتخاب کنید.
🌍
آی‌پی VPS، پورت SSH، نام کاربری و رمز عبور یا کلید SSH خود را وارد کنید.
🔑
اسکن را شروع کنید و پروفایل پیشنهادی کارآمد یا نتایج تشخیصی را بررسی کنید.
✅
نکته مهم
اسکن محلی نشان می‌دهد که شبکه فعلی شما به چه مواردی دسترسی دارد. اسکن VPS شواهد قوی‌تری ارائه می‌دهد زیرا هم سمت کلاینت و هم آنچه واقعاً به VPS می‌رسد را بررسی می‌کند.
🧐
نسخه:
۱.۰.۷
🏷
@WhiteDNS</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/whitedns/1110" target="_blank">📅 19:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1109">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سلام
❤️
توی این آموزش، تمام بخش‌های برنامه V2Ray را از مبتدی تا حرفه‌ای به‌صورت کامل بررسی کردیم؛ از اضافه کردن کانفیگ و Subscription گرفته تا تنظیمات پیشرفته، Routing، آپدیت برنامه و حالت‌های مختلف Tunnel.
🇺🇦
لینک آموزش در یوتیوب:
https://youtu.be/i1-XenoSalk?si=5jbQK3BrGAe4ctsu
اگر موضوع یا نرم‌افزار دیگری هست که دوست دارید آموزش کاملش را ببینید، داخل کامنت‌های یوتیوب یا گروه تلگرام پیشنهاد بدید تا برای آن هم آموزش تهیه کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/whitedns/1109" target="_blank">📅 18:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1108">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDr Alan(Dr . A)</strong></div>
<div class="tg-text">چجوری کانفیگ رایگان بسازم بدون دردسر؟
🤔
همه چیز با یک کلیک در WhiteDNS BPB
🚀
مرحله 1:
اول از همه برنامه رو نصب کنید و وارد برنامه بشید
📲
مرحله 2:
وقتی وارد برنامه شدید دکمه Connect CloudFlare رو بزنید
☁️
مرحله 3:
وقتی به مرورگر هدایت شدید، اطلاعات حساب Cloudflare خود را وارد کنید
🔐
مرحله 4:
بعد از وارد کردن اطلاعات به یک صفحه منتقل میشید که از شما میخواد اجازه استفاده WhiteDNS BPB رو از اکانت کلادفلر خودتون رو بدید. برای این کار به پایین صفحه اسکرول کنید و دکمه آبی رنگ Authorize رو بزنید
✅
مرحله 5:
دو حالت وجود دارد. یا شما میخواد یک برنامه رو انتخاب کنید که باید برنامه WhiteDNS BPB رو انتخاب کنید. یا به یک صفحه دیگه منتقل میشید در این حالت به برنامه WhiteDNS BPB برگردید و دکمه I Finished رو بزنید
🏁
﻿
مرحله 6:
بعد از اتصال حساب کلادفلر شما به برنامه، به تب(بخش) Bpb Deployment برید و دکمه eCreat Panel رو بزنید
⚙️
مرحله 7:
به یک صفحه منتقل میشید که میتونید تغییرش ندید و بزارید در حالت پیش فرض بمونه و دکمه آبی رنگ Create Panel رو بزنید
مرحله 8:
بعد از کمی صبر پنل شما با موفقیت ساخته میشه. دکمه Subscriptions رو بزنید و اولین ساب رو کپی کنید
📋
مرحله 9:
میتونید اون لینک ساب رو در برنامه های v2ray / v2box ... وارد کنید یا از داخل تب VPN در برنامه WhiteDNS BPB لینک رو وارد کنید و همونجا به کانفیگا وصل بشید
🌐
⚠️
توجه:
به هیچ وجه از ایمیل های فیک و رندوم استفاده نکنید
🚫
حتما باید اکانت کلادفلر شما Verify شده باشه در غیر این صورت با خطا مواجه میشید
❌
اگر از فیلترشکن استفاده می‌کنید، توجه داشته باشید که باید ایپی شما ثابت
باشه
🛡️
لینک دانلود نرم افزار:
https://t.me/whitedns/1018
@WhiteDNS
با تشکر
🙏</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/whitedns/1108" target="_blank">📅 04:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1106">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/whitedns/1106" target="_blank">📅 19:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1105">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا یکی از بچها زحمت کشید یه ویدیو کوتاه واسه این ابزار درست کن با کمی بهینه و میانبر واسه دریافت توکن که میتونید ببینید و واسه خودتون و خانوادتون فیلترشکن رایگان بسازید
✅
ویدیو یوتیوب:
📹
https://www.youtube.com/watch?v=e8FNffowfYo
بات دکی:
👑
@itsyebekhebot
نوا پروکسی دریافت توکن:
✅
https://novaproxy.online/install
داشبورد کلودفلر:
💎
https://dash.cloudflare.com
ایمیل فیک:
⚡️
@TempMail_org_bot
خلاصه: داخل ویدیو نحوه دریافت توکن آسون تر شده و این که یه سری بهینه سازی هم داخل ویدیو هست
❗️
@yebekhe
👑
@mehdisedighinasab
💎
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/whitedns/1105" target="_blank">📅 16:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1102">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">↗️
تعداد کانکشن های موفق WhiteDNS VPN در ۲ هفته به ۱۰۰هزار رسیده
.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/whitedns/1102" target="_blank">📅 15:18 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
