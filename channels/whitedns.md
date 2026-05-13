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
<img src="https://cdn4.telesco.pe/file/B9JibvSs5S-E3SP1Jt_Kd51fxUp6uDviZuNS3hQKSxKgPn4pKvU1GjzgI2H-XMt_MnXuZr-zNgzDlDdyp29wnw1por9KeSQGyUvRGLNWeQfgoEaj6UAeJGDeySNfwKjYlfW3fbaUmsGXY3K1NTiCneCmpm-la05npNzkNDUEBij5_SaL_cwHBkCbZwOIpBpfCpZG_4Of-dySHjFMbO0pHIt4d6B0Qs-DhUtQjEl_IXSXbnFbKx9jzRpSWj0_ezJDQPQq6j7Z6uYX4o9rfwGiiCcmlmWrpoW42Hn6F7Gi5ufWjvAI3FHCl7p2kJ-NDKZVP1vIdhT4gev61mW-LwT1qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 63K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 23:57:33</div>
<hr>

<div class="tg-post" id="msg-588">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بعد از اسکن بیش از
60,000
آی‌پی، تعداد
435
ریزالور سالم و قابل استفاده پیدا شد.
لیست این ریزالورها حالا از طریق ربات زیر در دسترسه:
@dns_resolvers_bot
برای دریافت لیست، وارد ربات شوید و دستور زیر را ارسال کنید:
/dns_master
بعد از ارسال دستور، می‌تونید لیست ریزالورها رو دریافت کنید یا فایل آماده رو دانلود کنید.
از همه کانال‌ها و دوستانی که این لیست رو بازنشر می‌کنند خواهش می‌کنیم حداقل سهم و همکاری‌شون این باشه که کانال ما رو به عنوان منبع ذکر کنند. این داده‌ها با زمان، هزینه و اسکن گسترده جمع‌آوری شده، نه با جادو و دعای نیمه‌شب.
Source:
@WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/588" target="_blank">📅 18:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-587">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سرور اهدایی از چنل
@pythash
از چنل اهدا کننده سرور حمایت کنید.
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 1
Domain:
v1.abolfazlshahi.cloud
Key:
a4c5649c628ac1103ad55c5208e0d74d
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 2
Domain:
v2.abolfazlshahi.cloud
Key:
965a568dccef58af7afb86e8ee55eea6
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
@WhiteDNS</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/whitedns/587" target="_blank">📅 18:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-586">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
پروفایل های مخصوص وایت دی ان اس ورژن رسمی (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲۳ اردیبهشت
👾
لینک دانلود
کلاینت :
1️⃣
WhiteDNS
1.2.0
⬅️
نحوه ی اضافه کردن پروفایل ها
⬅️
فیلم اموزش وایت دی ان اس
👍
تنظیمات مخصوص وایت دی ان اس
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
(پیشنهادی)
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigxKSIsInNlcnZlciI6eyJkb21haW4iOiJ2MS5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigyKSIsInNlcnZlciI6eyJkb21haW4iOiJ2Mi5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigzKSIsInNlcnZlciI6eyJkb21haW4iOiJ2My5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig0KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NC5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig1KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NS5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/586" target="_blank">📅 18:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-585">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/utrVhC-K_qMi0ItyaDhAjMdjFGADchb_54WKKz7YqFT2lydAev9Re7TKytyAL0OppsYlv3BuktQIUYt9GYwq35pzAIJOm9OBIEGbhcV2mwje3Q6Q5s4dWnrwqnqC7-es0ptVI0o_3MzvUUADl3NwQobjQ7BfFz3fzGksLo2Lo3BLnEvw3q-XOKY9H4Cg5WQuq_Lc6ka5xjucG6zzc9d0AAWuVWU2Ya4Su2M043oH7zSq5rdRD_rZYVcCqWlnjt-LAej5Vvagf844SHin7GOoqojR3D_DQA_zRzRCvcKEem9FPXFDlOUPS4UhxM9SbneW9h-1va9ogeW61FHV6DakCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/whitedns/585" target="_blank">📅 16:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-584">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">9.1 MB</div>
</div>
<a href="https://t.me/whitedns/584" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
انتشار اولین نسخه ویندوز WhiteDNS
نسخه
WhiteDNS Windows V1.0.1
منتشر شد.
این اولین نسخه رسمی ویندوز WhiteDNS است؛ نسخه‌ای که برای شبکه‌های سخت، محدود و فیلترشده طراحی شده تا اتصال پایدارتر، سبک‌تر و قابل‌اعتمادتر فراهم کند.
در این نسخه تلاش کردیم هسته‌ی ارتباطی WhiteDNS را برای ویندوز آماده کنیم و امکانات اصلی را در اختیار کاربران قرار دهیم:
• انتقال ترافیک از طریق DNS Tunnel با سربار پایین و پایداری بهتر
• پشتیبانی از چند مسیر اتصال از طریق چند Resolver و Tunnel
• تشخیص سلامت Resolverها و غیرفعال‌سازی یا فعال‌سازی خودکار مسیرها
• مدیریت هوشمند MTU برای حفظ پایداری اتصال در شبکه‌های ضعیف
• بهینه‌سازی جریان اتصال برای SOCKS4 و SOCKS5
• سرویس DNS محلی و قابلیت کش DNS سمت کلاینت
• پشتیبانی از روش‌های رمزنگاری مختلف مثل AES، ChaCha20 و XOR
• استفاده از Wintun Adapter برای ساخت اتصال VPN در ویندوز
• مدیریت Route و DNS به‌صورت خودکار
• رابط کاربری دسکتاپ با امکان ساخت پروفایل، ذخیره‌سازی امن، Import/Export، ویرایش ساده و پیشرفته، نمودار زنده، لاگ‌ها و تنظیمات
این نسخه شروع مسیر WhiteDNS روی ویندوز است و مثل همیشه با کمک فیدبک‌های شما بهتر و پایدارتر خواهد شد.
اگر تست کردید، لطفاً نتیجه اتصال، لاگ‌ها و مشکلات احتمالی را با ما به اشتراک بگذارید تا نسخه‌های بعدی دقیق‌تر و قوی‌تر منتشر شوند.
لینک داخلی :
https://uplod.ir/8h2n22ficr8f/WhiteDns-Windows-Setup.exe.htm
Special thanks to
Masterdns
❤️
for their amazing work - without them non of this was possible
@WhiteDNS</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/whitedns/584" target="_blank">📅 14:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-583">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YY5V5_o3kpASzosuBf7v2OVIEuu8i-MnVt9SwbRRXbqXPdO8MwAd5O0SuV22cjVID4XfRhWkprCSMZj1CRzHHIWR7UKDeLAXF_8bToTvlVsBvA09UgqvjnnxoGt9H-QoCCDwlMDBWT8YQN5LT50dI2iqfyqQZ5yf5IkPzdtcR602jqRq9dMwLqsHHzTeq-UzFTeUszUoyZzrAn2UFgyHBM1Yn0JWSK400MosvqswaQoK2x4DbDRrO3Cv-1jTHKXlvMuDwO8tLLGl__fcJatkfhzL0SSekC9i0CZkFjiZsPjChICcovKAhyggt4YshnrdiwwU3rZepO3Pkw8KLUs9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/whitedns/583" target="_blank">📅 14:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-582">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLtv2bMQ4--wF5ZVUvKIZL6cQgQEyCpa7D628LN53hMXHg9pfIdLFEc-AuX5ICwfjqQv8DuS-Qr1Ifp2jVOy7sodZSAnjh-PwjTVRoH0EpAXFn2TjdVnpY7QFDaPMB1-I9pq3wEGbazVEuxY7H2KGT2tZgrldgmoNiuefc6kx7J9LGmwk5JrPxqMccMlvJf8JblIQgL4yEo82UNj1rbTgvMzDB1nMYPxz1j76DnySLrmM9XtFd5uby0rCCODLLm-ZA-GiEmlixi3zX0D7duhDDdTU_x3gMd8Bq8Rz6P0_Oy3ED9qy96Obty6yDD0n3lkGOEU5HAynLk2bdss2Blznw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز،
یک نکته مهم را لازم دیدیم با شما به اشتراک بگذاریم.
بر اساس بررسی‌هایی که انجام دادیم، فیلترینگ دامنه‌های عمومی همیشه به‌صورت کامل و یکسان انجام نمی‌شود. در واقع این محدودیت‌ها معمولاً به‌شکل منطقه‌ای و بسته به اپراتور، مسیر شبکه و Resolverهایی که استفاده می‌شوند متفاوت است. اینترنت هم طبق معمول تصمیم گرفته مثل یک موجود عصبی رفتار کند.
برای مثال، اگر به وضعیت سرورهای WhiteDNS در تصویر دقت کنید، میزان لود شبکه یکی از سرورهای ما از حدود
4Mbps
به نزدیک
400Kbps
کاهش پیدا کرده است. این یعنی در بعضی مسیرها یا اپراتورها، دسترسی به برخی دامنه‌ها محدودتر شده یا کیفیت ارتباط افت کرده است.
به همین دلیل، ممکن است روی بعضی از سرورها تعداد Resolverهای کمتری دریافت کنید یا کیفیت Resolverها نسبت به قبل پایین‌تر باشد.
ما در حال بررسی راهکاری هستیم تا بتوانیم دامنه‌های سرورها را به‌صورت روزانه به‌روزرسانی کنیم و کیفیت اتصال را پایدارتر نگه داریم.
تا زمان آماده شدن این راهکار، می‌توانید از سرورهای کانال همکار ما،
@Masir_Sefid
، که در پست قبلی معرفی کردیم استفاده کنید.
تمام سرورهای ما و سرورهای کانال همکار، به‌صورت مداوم مانیتور می‌شوند تا در صورت افت کیفیت یا مشکل اتصال، سریع‌تر بتوانیم وضعیت را بررسی و اصلاح کنیم.
ممنون از همراهی و گزارش‌های دقیق شما
🤍
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/whitedns/582" target="_blank">📅 10:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-580">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJmLK-fTF1cQQ6FBIfI3rbTwWthqeFX7quVxupQTLyRdW4dFu2Zu4IVS95T8qTPZZRTAtMF-OuyNrdI226O1JEl9Uef3D0OT0LdicMSwRfaWpA0h4BOGFJorZ4nb0wgVLdUdt9Cqv0hCDzSkWbLYu_izNDhmK71KFlLYfw7tKf7kaOzRFF3p19HTb-3ajY49ZeAkSTtabpA4sW-V8hHjzNf-qfV92t6lUXJqMbb22xnORc7YtcgW0-wY2aEV_PZu5SBLBTy9V7XfwL-OV9EdzEjpZAOBUk_K79UMWm7aF46fIHYQfTW9-S4VeIxcf30_SA_B157b8YJD4nOkGZ6H-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امکان دانلود کل ریزالور ها به ربات
@dns_resolvers_bot
اضافه شد
@WhiteDNS</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/whitedns/580" target="_blank">📅 05:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-579">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">به دلیل تعویض زیاد سرور ها توسط کاربران، تلگرام ممکنه بخاطر امنیت اکانت شما دستگاه شما رو از روی اکانت logout کنه و دیگه نتونید وارد اکانتتون بشید!
راه‌حل:
1. اکانت تلگرام خود را روی یک گوشی دیگر login کنید تا در صورت logout شدن شما بتونید دوباره به اکانت بازگردید.
2. رمز دو مرحله‌ای اکانت و ایمیل بازیابی را فعال کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/whitedns/579" target="_blank">📅 14:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-578">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDL1Qf-MP9QAcRTiha6MqffGQYw4NWrno8qZPdA-mJT1p9iWosF_KKuZnyaBjE0kok5O3uT5bJpvj7S7_7TMnTkStHBSGoAyGSMwEze1JMuo9FRBZr3LoZ6dOGBSMZOztxN7Oflk4vTP3f3Ne8brRVOWpGWTMMFBVkjT2rApS9b41RJ4L9DF_QHz07t_EI_CLJB3gAJGBfXymJSFBdGVmxJ1FqD-vM6Hcy3eKUSGvDv_hpTq0GWDAqPlWkwdKjEnsQ6mw1amfs35yFwcq1OvhalY2-5bn1wOP74OfzsgEUXBLwFT9574RJgUjPKzcxh51ekj094cTwqxv3xcjMCUyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
‏فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
‏ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام ⁧
#اینترنت_پرو
⁩ را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
‏ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
منبع
https://x.com/ircfspace/status/2054094958353678824?s=46</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/whitedns/578" target="_blank">📅 12:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-577">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-poll">
<h4>📊 آیا به اپ WhiteDNS تونستید وصل بشید؟</h4>
<ul>
<li>✓ آره</li>
<li>✓ نه</li>
</ul>
</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/whitedns/577" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-575">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtLr_EFt-3zWeriBjI3E8oGyjv_wD0osxFib0NWO0BsM9qzo5jKndaCmvQ-7xFKRzQOih2hLyCv_jTr94xAK_qnfBIDBF4FyL5adzfs9JinbovvUCZfV2ClfiRlG1CqVOLUhdEA8S71PcOYy7gEGY6t5EB7SePnDbHz4qTwX1TWCuy-VZR5nqDmwmzXFnGGMzsu0EPRXbXIJpX1PB_Q12mhq3In_R_i1N3RRsgKqRi6x-euFa0Jr5zXfC0uSCkgh7IHUOHi_1Mxv6JzrsaFcm0_VBRySx2cuissFvm8t4PDuXM8kpRLp4r8Zhc_OSjgPjGRtDOZk8ejWJ1WPUgM_HA.jpg" alt="photo" loading="lazy"/></div>
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
#آموزشی
@WhiteDNS</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/whitedns/575" target="_blank">📅 10:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-574">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚀
سرور اهدایی از چنل
@Masir_Sefid
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigxKSIsInNlcnZlciI6eyJkb21haW4iOiJzLm80cy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigyKSIsInNlcnZlciI6eyJkb21haW4iOiJzMi5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigzKSIsInNlcnZlciI6eyJkb21haW4iOiJzMy5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig0KSIsInNlcnZlciI6eyJkb21haW4iOiJzNC5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig1KSIsInNlcnZlciI6eyJkb21haW4iOiJzNS5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/whitedns/574" target="_blank">📅 09:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-573">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">White DNS
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/whitedns/573" target="_blank">📅 09:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-572">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9ad3f5766c.mp4?token=nuhaPOLaUOZ5GU0rAmOr7L9gtrbgenSStd13SdFQUnIszB1HvYZbt9Zw-pp5G_twqBevjqmO6m6vW866zhnFy41z7Oj6wAGAMWf2jurzCvaLt-zsANxLolhOEVObImTRFWP-uIV0NgM-HAscfncKAinz0pJj4hNEVDDvGwSWfp5UiNJ-XR_D0RPeWROIObYDW_atpY6wifZIo8VGaNeSspW9HhtJLkHuVXcVhkdq2W2K2Otcbc0KJOt0yQ0dqeRXKc4cPXt2gYuXNF7-2cQfMbel5EnY-96MyQtCPGWXY61ByJtrjY-CaCffP52920PobUnmSer7-AM2SWYPZI8Rcw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9ad3f5766c.mp4?token=nuhaPOLaUOZ5GU0rAmOr7L9gtrbgenSStd13SdFQUnIszB1HvYZbt9Zw-pp5G_twqBevjqmO6m6vW866zhnFy41z7Oj6wAGAMWf2jurzCvaLt-zsANxLolhOEVObImTRFWP-uIV0NgM-HAscfncKAinz0pJj4hNEVDDvGwSWfp5UiNJ-XR_D0RPeWROIObYDW_atpY6wifZIo8VGaNeSspW9HhtJLkHuVXcVhkdq2W2K2Otcbc0KJOt0yQ0dqeRXKc4cPXt2gYuXNF7-2cQfMbel5EnY-96MyQtCPGWXY61ByJtrjY-CaCffP52920PobUnmSer7-AM2SWYPZI8Rcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموژش نسخه جدید Whitedns
📲
✨
یکی از اعضای کانال آقا محسن زحمت کشیدند
👨‍💻
✅
نسخه اپلیکیشن به 1.2.0 ارتقا پیدا کرده
🚀
✅
حالت Full VPN کامل‌تر و پایدارتر شده
🔒
✅
حالا DNS هم داخل خود WhiteDNS مدیریت می‌شود
🌐
✅
دیگر برای باز شدن سایت‌ها و اپ‌ها نیازی به NekoBox، NVPN یا ترفندهای مشابه ندارید
🚫
✅
مشکل وصل بودن VPN ولی باز نشدن بعضی سایت‌ها و اپ‌ها برطرف شده
✅
✅
اتصال روی اینترنت‌های کند و Resolverهای دیرپاسخ بهتر کار می‌کند
⚡️
✅
صفحه اصلی ساده‌تر شده و انتخاب سرور، Resolver و نوع تنظیمات راحت‌تر انجام می‌شود
🎯
✅
اگر سرور یا Resolver درست تنظیم نشده باشد، اپ واضح‌تر نشان می‌دهد چه چیزی کم است
⚠️
✅
می‌توانید تنظیمات پیشرفته را با نام دلخواه ذخیره کنید
💾
✅
امکان ساخت چند پروفایل تنظیمات پیشرفته اضافه شده
📂
✅
می‌توانید هر زمان بین پروفایل‌های ذخیره‌شده تنظیمات پیشرفته جابه‌جا شوید
🔄
✅
امکان برگشت سریع به تنظیمات پیش‌فرض اضافه شده
↩️
✅
بعد از اتصال، نام پروفایل سرور، Resolver و تنظیمات فعال نمایش داده می‌شود
📋
✅
امکان خروجی گرفتن فایل client_config.toml از داخل اپ اضافه شده
📄
#آموزشی
@whitedns</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/whitedns/572" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-567">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/whitedns/567" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/whitedns/567" target="_blank">📅 06:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همگی دوستان
🔴
11 سرور اختصاصی جدید و بهینه برای اپلیکیشن WhiteDNS
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidi53aGl0ZWRucy5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InYud2hpdGVkbnMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiYjA3ZGMzNTczNjBkNmU2ODk2NTA5MTM2ZDcwOTc4OTciLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEyLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEyLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjAwOWM1MTRiMmE2NDNlZDQwY2JkN2NjNjE5Mzg5YjBmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEwLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEwLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjFlY2Q1ZmRmZTM1MWE5MzEzY2VhMzlmZTFiOWM1OWRkIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjkud2hpdGVkbnMuc2hvcCIsInNlcnZlciI6eyJkb21haW4iOiJ2OS53aGl0ZWRucy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJhMmYzMzQ4YmZhMDIxNzA2Mzk5NzBmMmQ2M2YxMDNkYyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjExLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjExLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjRjMTY2OTMyNmNkYmU4OThjYWIwOTY1YWNlMzAxMGMwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEzLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEzLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImUyOTE4ODcwY2U4OGYwNTU0N2ZiZmJhOTlhZWU0ZWM1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE0LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE0LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjliODY3MmEzNTJkMDQwNDg5ZDk2YmU5ZGY5N2VkOTY2IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE1LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE1LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjlhYTY4ZTdlOWE3YzIyZDkxZDhmNDY2ZDY0YTM1ZGZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE2LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE2LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU5Mjg0NWNhMzhmMTk0NjEzODNkMDU3MzNjMzMyMTRjIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE3LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE3LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU3NjU1MDM1NGE3MzA5NTMwYjdmYTI1MTUyZGM2NzJmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE4LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE4LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImQwNTM4YTNkNTQ1YTc4MzBiOGJiMmViMGMzNzQ4ZTk1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
#Servers
@WhiteDNS</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/565" target="_blank">📅 14:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-564">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👇
👇
👇
👇
👇
👇
👇
👇
👇
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/whitedns/564" target="_blank">📅 12:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-562">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">امروز یک هفته از انتشار نسخه بتا۱ اپلیکیشن WhiteDNS می‌گذره
🎉
فکر می‌کنم برای شروع، اپلیکیشن مسیر خوبی رو طی کرده و این فقط با همراهی شما ممکن شده.
خواستم از همه دوستانی که در این مدت با دقت تست کردند، مشکل‌ها رو گزارش دادند و فیدبک درست و کاربردی به تیم ما دادند تشکر کنم. همین بازخوردها باعث شده هر روز بتونیم WhiteDNS رو بهتر، پایدارتر و کاربردی‌تر کنیم.
از اینجا به بعد، سرعت آپدیت‌های نسخه اندروید کمی کمتر میشه تا بتونیم تمرکز بیشتری روی توسعه نسخه ویندوز داشته باشیم.
از دوستان عزیزی که خارج از کشور هستند، همچنان درخواست داریم اگر امکانش رو دارند با دونیت سرور به پروژه کمک کنند. این کمک‌ها مستقیماً به بهتر شدن کیفیت سرویس برای همه کاربران کمک می‌کنه.
از دوستانی که داخل ایران هستند هم یک درخواست مهم داریم:
لطفاً فقط مصرف‌کننده ریزالورها نباشید. برای زنده نگه داشتن شبکه، باید مداوم اسکن انجام بدیم و ریزالورهای جدید پیدا کنیم.
WhiteDNS با کمک جامعه کاربری خودش قوی‌تر میشه؛ نه فقط با استفاده، بلکه با مشارکت همه ما.
ممنون از همراهی شما
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/whitedns/562" target="_blank">📅 10:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-561">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BthD5LEPp1geM4phXgm1EzB7Vd7nwyTN75Jv3QhCBXAi4U9Cnr5e1smauzHpNJ32HwH62NmeIDq0aPPWERjhRnnxDXVETdNa6eN-WpRnS9WlePjId49RxBo2PwYuXY_TGP3Qfc07BtRiwsVGBTjMjdlDnFeI36fVUf5BswpfLscsWbiQYAgiVPLz9_M7HrElUDyVr_0WVu4wJIhq9mSoR0hQithdsMz9OWwW4sQ0Tx1RhjnhHIZuLiohjYDc4XmOGy4CnwgQ9ShpElL62EHCEzjBf9z7nP1exopmYt0QEenBHv6p4_1W0DTF844j0B1NF3j1yd8uisKeIPAMWX0sNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
🙌
دکمه Donation به ورژن بتا۷ اضافه شده. هر کمکی  از سمت شما فقط هزینه ساخت سرور های جدید و بهبود اپ WhiteDNS خواهد شد.
هیچ اصراری برای کمک نیست و تیم WhiteDNS کاملا رایگان و تا اتمام قطعی اینترنت ایران ادامه خواهد داد.
ممنون بابت همراهی شما
🙏
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/whitedns/561" target="_blank">📅 09:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-556">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.1.0-arm64-v8a-1778467437126.apk</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/whitedns/556" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
هدف اصلی از انتشار نسخه ۱.۱.۰، رفع مشکل «وصل می‌شود و دیتا مصرف می‌کند، اما چیزی باز نمی‌شود» است.
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
در این نسخه، اپلیکیشن بعد از اتصال وضعیت واقعی مسیر ارتباط را بررسی می‌کند و دیگر تلاش برای استفاده از Resolver یا تونل ضعیف و بدون پاسخ را بی‌پایان ادامه نمی‌دهد. اگر مسیر اتصال بعد از چند تلاش قابل استفاده نباشد، ارتباط‌های جدید رد می‌شوند و اتصال معیوب بسته می‌شود تا حجم بسته شما بی‌دلیل مصرف نشود.
همچنین هسته StormDNS در این نسخه تغییرات مهمی داشته و به همین دلیل اتصال بسیار سریع‌تر برقرار می‌شود. VPN/Proxy بعد از پیدا کردن حداقل Resolverهای سالم با MTU امن سریع‌تر فعال می‌شود و اسکن کامل Resolverها و MTU در پس‌زمینه ادامه پیدا می‌کند. علاوه بر این، اتصال‌های ناسالم زودتر تشخیص داده می‌شوند، مدیریت ارتباط‌های جدید پایدارتر شده و کتابخانه‌های native برای همه معماری‌های اندروید دوباره ساخته شده‌اند.
در این نسخه تمرکز اصلی روی پایداری بهتر اتصال، شروع سریع‌تر VPN/Proxy، مدیریت راحت‌تر پروفایل‌ها، اشتراک‌گذاری تنظیمات اتصال و عیب‌یابی امن‌تر بوده:
✅
نسخه اپلیکیشن به 1.1.0 ارتقا پیدا کرده
✅
مشکل گزارش‌شده‌ای که بعضی کاربران وصل می‌شدند و مصرف دیتا دیده می‌شد، اما سایت‌ها و اپ‌ها باز نمی‌شدند، برطرف شده
✅
حالا بعد از اتصال، مسیر ارتباط بررسی می‌شود و اگر تونل، Resolver یا مسیر خروجی پاسخ‌گو نباشد، اتصال‌های جدید به جای گیر کردن و مصرف بی‌فایده دیتا رد می‌شوند
✅
وضعیت سلامت اتصال داخل اپ نمایش داده می‌شود تا مشخص باشد اتصال واقعاً قابل استفاده است یا نیاز به بررسی دارد
✅
سرعت شروع اتصال بهتر شده؛ اپ بعد از پیدا کردن حداقل Resolverهای سالم با MTU امن، VPN/Proxy را سریع‌تر فعال می‌کند
✅
اسکن کامل Resolverها و MTU حالا در پس‌زمینه ادامه پیدا می‌کند و Resolverهای سالم بعداً به اتصال اضافه می‌شوند
✅
امکان روشن و خاموش کردن WhiteDNS از Quick Settings اندروید اضافه شده
✅
دکمه Disconnect به نوتیفیکیشن VPN و Proxy اضافه شده
✅
امکان Import پروفایل از لینک‌های stormdns:// اضافه شده
✅
هنگام Export پروفایل، QR Code نمایش داده می‌شود تا اشتراک‌گذاری راحت‌تر باشد
✅
ورود Resolverها ساده‌تر شده و حالا می‌توانید چند Resolver را با کاما، سمی‌کالن یا خط جدا وارد کنید
✅
پورت پیش‌فرض :53 به صورت خودکار مرتب و ساده‌سازی می‌شود
✅
اگر Resolver واردشده اشتباه باشد، اپ قبل از اتصال خطا را نشان می‌دهد
✅
تنظیمات پیش‌فرض MTU و پایداری اتصال بهینه‌تر شده‌اند
✅
مدیریت پروفایل‌ها هنگام اتصال بهتر شده و فقط در زمان Connecting محدود می‌شود
✅
بخش Split Tunnel و تنظیمات پیشرفته مرتب‌تر و جمع‌وجورتر شده‌اند
✅
بخش Logs به جای خروجی فایل، Diagnostics آماده و امن تولید می‌کند که اطلاعات حساس داخل آن مخفی می‌شود
✅
هسته StormDNS برای همه معماری‌های اندروید دوباره ساخته شده و پایداری اتصال بهتر شده است
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.1.0
از همراهی و حمایت شما ممنونیم
❤️
1️⃣
WhiteDNS</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/whitedns/556" target="_blank">📅 06:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-553">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_xDsYsHsn_d3VUEAE16_ExYKLyacNs6GZS5GNl1NeAV3R_RTZzSqV8yXH4VxK-spYonQA4oaJ_7qjvnXgLGbNH_dlqdibqJg8yKrp7rTDNPwtkoGFy1wOHgxYR9dbi3gPmpGGkdMi-P-VyZdT0T8ZOfJI_UNp1LCeTmM0_Pvv7KbL7dkbzDgNqujPN9jd4I-10aLsMqRtS6jw-QcnZRCP9TNJigCK7IgzeBr-3gwcMIelxopuBdM5NIq1veV3Qru8MaOP4gPqBLSrd_MFyB59SwBYG2PANXdFlMmM2iS0qxbmFKmRCdApHh2ue59Lix6PH9pNIOmXFm-R5hlmil-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام سرور هایی که داخل اپ بودن داخل تاپیک سرور این گروه هستند. لطفا عضو بشید و گفت و گو ها اصلی رو اونجا ادامه بدید.
1⃣
t.me/whitedns_group</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/whitedns/553" target="_blank">📅 15:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-552">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCgotzntmAeiDBJHoZF8jgQFfliQIamAkqEqv5teJoltWNwfdjAJ_4zd998vfAQKU8D9DD6OsgnJhDLmVuUQqEiw29r5zc2A1bQu4jcXS7HX98N4W3aoJw6l0hcOyitSS1Vr2r9N0ydWSb7trJC8uUqKC1ZgsVelOPX4UBjL_TPHcZn5qhFghicQiI8uYIy-FSgi5se8tC_dCtdbvMy5hhNEyeTlME2uzrpkHqE54NH1_y9ad--ZCAH_Py-Gh-mwL5i6rC1U5syJvRsC01SANCrZhoN9VyiQlGxrwvK5Fk3xzkeJuMQdru1EEspx5FBBDAFsR_scbTLy2dF3Zwh3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
🙌
دکمه Donation به ورژن بتا۷ اضافه شده. هر کمکی  از سمت شما فقط هزینه ساخت سرور های جدید و بهبود اپ WhiteDNS خواهد شد.
هیچ اصراری برای کمک نیست و تیم WhiteDNS کاملا رایگان و تا اتمام قطعی اینترنت ایران ادامه خواهد داد.
ممنون بابت همراهی شما
🙏
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/whitedns/552" target="_blank">📅 15:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-551">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">White DNS
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/whitedns/551" target="_blank">📅 14:01 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-544">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-x86_64-1778404214016.apk</div>
  <div class="tg-doc-extra">5.3 MB</div>
</div>
<a href="https://t.me/whitedns/544" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
انتشار رسمی WhiteDNS به صورت متن‌باز
دوستان عزیز،
پروژه WhiteDNS رسماً به صورت Open Source روی GitHub منتشر شد.
این نسخه، اولین ریلیز رسمی
1.0.0
بعد از ۷ نسخه بتا است و از این به بعد مسیر توسعه پروژه شفاف‌تر، عمومی‌تر و با مشارکت جامعه ادامه پیدا می‌کند.
در این نسخه، پروفایل‌های پیش‌فرض WhiteDNS از داخل اپ حذف شده‌اند
تا برنامه به شکل مستقل‌تر و عمومی‌تر قابل استفاده باشد.
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
قبل از آپدیت به این ورژن ، تمام پروفایل های خودتون رو Export بگیرید. ورژن جدید دیگه سرور های WhiteDNS را در اپ ندارد.
ورژن جدید اپ Sign شده هستش و از لحاظ امنیتی بهبود یافته.
برای نصب، ورژن قبلی اپ باید به صورت کلی از روی دستگاه شما حذف شود.
از این ورژن به بعد، نیازی برای پاک کردن اپ در هر آپدیت نیست.
👆
👆
👆
👆
👆
👆
👆
👆
👆
👆
👆
👆
از این مرحله به بعد، توسعه‌دهندگان و کاربران می‌توانند پروژه را بررسی کنند، مشکل‌ها را گزارش دهند و در بهبود آن مشارکت داشته باشند.
🔗
GitHub:
https://github.com/iampedii/WhiteDNS
از همراهی و حمایت شما ممنونیم
❤️</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/whitedns/544" target="_blank">📅 12:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-538">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
پروفایل های مخصوص وایت دی ان اس ورژن جدید( 7 WhiteDNS)
👾
کلاینت :
WhiteDNS
1️⃣
|
WhiteDNS
2️⃣
⬅️
نحوه ی اضافه ی کردن پروفایل ها
⭕️
پست تنظیمات کلاینت
⭕️
پست تنظیمات بهینه تر
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oMSkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoicy5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oMikiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczIubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oMykiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczMubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oNCkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczQubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oNSkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczUubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
✉️
Channel |
@link_dakheli_app
| کانال
✉️</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/538" target="_blank">📅 09:40 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-537">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سرور اهدایی از چنل
@pythash
لطفا از چنل دوستان اهدا کننده سرور حمایت کنید.
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey
Domain:
v1.abolfazlshahi.cloud
Key:
a4c5649c628ac1103ad55c5208e0d74d
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
@WhiteDNS</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/whitedns/537" target="_blank">📅 09:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-536">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سلام خدمت همگی دوستان
🔴
11 سرور اختصاصی جدید و بهینه برای اپلیکیشن WhiteDNS
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidi53aGl0ZWRucy5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InYud2hpdGVkbnMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiYjA3ZGMzNTczNjBkNmU2ODk2NTA5MTM2ZDcwOTc4OTciLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEyLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEyLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjAwOWM1MTRiMmE2NDNlZDQwY2JkN2NjNjE5Mzg5YjBmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEwLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEwLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjFlY2Q1ZmRmZTM1MWE5MzEzY2VhMzlmZTFiOWM1OWRkIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjkud2hpdGVkbnMuc2hvcCIsInNlcnZlciI6eyJkb21haW4iOiJ2OS53aGl0ZWRucy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJhMmYzMzQ4YmZhMDIxNzA2Mzk5NzBmMmQ2M2YxMDNkYyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjExLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjExLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjRjMTY2OTMyNmNkYmU4OThjYWIwOTY1YWNlMzAxMGMwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEzLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEzLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImUyOTE4ODcwY2U4OGYwNTU0N2ZiZmJhOTlhZWU0ZWM1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE0LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE0LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjliODY3MmEzNTJkMDQwNDg5ZDk2YmU5ZGY5N2VkOTY2IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE1LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE1LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjlhYTY4ZTdlOWE3YzIyZDkxZDhmNDY2ZDY0YTM1ZGZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE2LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE2LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU5Mjg0NWNhMzhmMTk0NjEzODNkMDU3MzNjMzMyMTRjIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE3LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE3LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU3NjU1MDM1NGE3MzA5NTMwYjdmYTI1MTUyZGM2NzJmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE4LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE4LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImQwNTM4YTNkNTQ1YTc4MzBiOGJiMmViMGMzNzQ4ZTk1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
#Servers
@WhiteDNS</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/whitedns/536" target="_blank">📅 07:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-535">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoWv-3ekb6ImqTvMJpWcj5JDnRj5dDd0Vpd-94_cMGhh7OBy_FgJdAFs1zKKzArzTpENcC3ReFExKUZx_6OaBM3I6oshzHZkkkDoFGH56a5efqCndCS95LeQuOcVTdyq9Ua2TBteFUlKmYTMCnjiGfkbpx0iNh6yfKJYHqWqSpImTOy-O1MQD2Wx_4ogS5CdWlHV4HyPmHEbIo1c-A8IZyQ-ff9WvIoNGGG5I_ggqv2S3o3CP6ucIe_BXmK6pBmBbqkf3r0lCdJxm8lC_n68J69Z_ZIl4q_pDKcbO5uaGWaAzmbVfY7FZF95xW66U2Jx_wxkEF_aS0oKSRoB8Sl0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه بعد از اسکن، DNS های سالم رو برای بعدا ذخیره کنیم؟
بعد از اتصال، زیر دکمه
Connect
یک عدد نمایش داده می‌شود.
اگر روی عدد بخش
Valid
بزنید، فقط لیست ریزالورهایی که با موفقیت تست شده‌اند نمایش داده می‌شود.
می‌توانید همان لیست را کپی کنید و با آن یک پروفایل ریزالور جدید بسازید. بعد از آن، هنگام اتصال، پروفایل جدید را انتخاب کنید.
با این کار هم اتصال سریع‌تر برقرار می‌شود و هم اپلیکیشن سبک‌تر اجرا می‌شود
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/whitedns/535" target="_blank">📅 05:18 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-533">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">White DNS
pinned «
سلام خدمت همه دوستان عزیز
🌿
برای اینکه مطالب، آموزش‌ها، فایل‌ها و بحث‌های مرتبط با WhiteDNS بهتر دسته‌بندی بشن و دسترسی بهشون راحت‌تر باشه، یک گروه جدید برای کانال ساختیم.   متأسفانه تلگرام این امکان رو به ما نمی‌ده که گروه فعلی رو به گروه دارای Topic تبدیل…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/533" target="_blank">📅 20:42 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-532">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سلام خدمت همه دوستان عزیز
🌿
برای اینکه مطالب، آموزش‌ها، فایل‌ها و بحث‌های مرتبط با WhiteDNS بهتر دسته‌بندی بشن و دسترسی بهشون راحت‌تر باشه،
یک گروه جدید برای کانال ساختیم
.
متأسفانه تلگرام این امکان رو به ما نمی‌ده که گروه فعلی رو به گروه دارای Topic تبدیل کنیم. برای همین، جهت حفظ بهتر مطالب و جلوگیری از گم شدن آموزش‌ها و اطلاعات مهم، لطفاً عضو گروه جدید ما بشید.
از این به بعد گفت و گو های اصلی تیم، آموزش‌ها، مطالب فنی و اطلاع‌رسانی‌های مهم داخل گروه جدید انجام می‌شه.
گروه فعلی فقط برای کامنت‌های مربوط به پست‌های کانال استفاده خواهد شد و فعالیت اصلی تیم در اون محدود می‌شه.
ممنون از همراهی همیشگی‌تون
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/whitedns/532" target="_blank">📅 20:38 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-531">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بازی ساده اس !ً مدت ها ذهن شما با قیمت vpn های هر گیگ 1 میلیون و یا 500 هزار و یا 200 هزار تومن عادت کرده بود
حالا وقتی vpn بشه هر گیگ 80 تا 100 کلی حس پیروزی و خوشحالی داری و مدتی لذت میبری ازش .
بعدش پیش خودت میگی خب میرم سیمکارت پرو میگیرم بشه هر گیگ 40 هزار تومن و اون لحظه اس که دیگه حسابی خوشحال خواهی بود چون با نصف قیمت VPN دیگه اینترنت داری  !
حالا اینکه روزی سه چهار گیگ میتونی در روز مصرف کنی و 11 برابر گرون تر از 3 ماه پیشه که اینترنت وصل بود دیگه اصلا به ذهنت نمیرسه چون مدت ها درگیر بازی قیمت توسط حکومت بودی
اینجوری چرخه بردگی تا ابد ادامه پیدا می‌کنه
حالا فهمیدید چرا ما با هر رانت دولتی مخالفیم ؟
@whitedns</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/whitedns/531" target="_blank">📅 19:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-530">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سوالات پرتکرار مربوط به برنامه‌ی WhiteDNS
این تلگراف به مرور تکمیل تر شده و سوال های بیشتری نیز داخل آن قرار خواهد گرفت.
@WhiteDNS</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/whitedns/530" target="_blank">📅 16:17 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-529">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/529" target="_blank">📅 16:15 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-527">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUHZjQk49osb-MeafnJ7cNuTTvGp2Xidmjmk4lpql9kztY0vE4D8THXfVMUdx_KgLrP8b6udr0P3aBMiYygoNwldYLeWqGdilM3nUH_VFPXTnMGUTMtkyAOlMVLg2mj_ohhNwvzGEasV6U95ePMY5DYNg14FnVo4E__p9QxQUsnLd__fdPiw9cW8mD785AWEN2CE9hSa1Seppf3NQQS50t-7LtqnGu8hfafLo5Z01kAKPOahWp3Q5lZV6b0GWEWFwKRbzb564rhdTS5q8U8nbUQov9QRG85mVCBoFMHL15YKTtNevvKK0R-342SMoyi56YI4vJUdeueJRLHzrEyZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
🙌
دکمه Donation به ورژن بتا۷ اضافه شده. هر کمکی  از سمت شما فقط هزینه ساخت سرور های جدید و بهبود اپ WhiteDNS خواهد شد.
هیچ اصراری برای کمک نیست و تیم WhiteDNS کاملا رایگان و تا اتمام قطعی اینترنت ایران ادامه خواهد داد.
ممنون بابت همراهی شما
🙏
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/whitedns/527" target="_blank">📅 13:36 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-525">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnWQrcNGCFha3_sbh5p3IjVDONaxdYKn-CNO9opiM84a8qo1-yEUnxbT5RyOAkQ3xkZmfYC6-KUnofCVKDxyiG2Ry4Yfhr3znLDFgNScL6VGSKA_lWXa_QZPOvcQFjkvlRhkLpYGaCzP80JB5U6VHTbYc0MEZcTxNQwxyDWEcWSgRzcTVX_3Y0KqmnayMhXQAfJvdWlGjjDP5bf6Q-YKBnTkqX38NjCXBu2UM7FGIG3-WLIM5s9jFipSFy4ZEHlQNAHDFZSGvzA-9Hr0IUh6kAv2vbMpNJcw6aZtIRU7YaiwxsWkaawoZkMbrfInQdkocTbqJBMDvYwkaxvpXfNBOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ربات WhiteDNS حالا امکان جدید دارد برای دریافت ریزالور های MasterDNS / StormDNS
۱) وارد بات زیر شوید
@dns_resolvers_bot
۲) متن زیر را برای ربات ارسال کنید
/dns_master
۳) برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/whitedns/525" target="_blank">📅 10:43 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-523">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/523" target="_blank">📅 10:15 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-521">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIuBGn92EZR5wZD411yo8MDZxPrWGf2sil_eZqRhjemFrojw7QaO3BXenQx9PERVNySBSQhsv-ruXkjW3LrkT-OmFDPXvyhZ80WqvyTENhAJ-Dxvk_z0hr8sbb6ZI6H_Cf0CKErovzUTbr9UYQFI0IJtroBy1t-3qjhzddQdB5teVlFWsZT6gUk9L77xD9nmD4OF0E3yUSa3vB-VXbjYpkUbR79CgxEncI50ZMkzJ6hvwvuqM5x-gF6zxWUCwBSoE9sy7Q8wcgFwD13heA64Hie_r5S2FziaGKzDRH3N_8tBqzrKpAyyIIpJWCKFcpYtfVv-Z2cZfFtkxW8J56q2qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ سرور اهدایی از چنل همکار
@link_dakheli_app
برای ایمپورت ابتدا ورژن اپ رو به بتا۷ آپدیت کنید، سپس وارد بخش پروفایل بشید و بعد دکمه ایپمورت رو بزنید.
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidGUubGluay1kYWtoZWxpLWFwcC5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InRlLmxpbmstZGFraGVsaS1hcHAuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiZXUubGluay1kYWtoZWxpLWFwcC5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6ImV1LmxpbmstZGFraGVsaS1hcHAuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoic3IubGluay1kYWtoZWxpLWFwcC5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InNyLmxpbmstZGFraGVsaS1hcHAuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoicy5vNHMuc2hvcCIsInNlcnZlciI6eyJkb21haW4iOiJzLm80cy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbUNoYW5uZWxAbGlua19kYWtoZWxpX2FwcCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiczIubzVzLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczIubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
👾
لینک دانلود نسخه بتا ۷ از سرور داخلی
WhiteDNS
1⃣
|
WhiteDNS
2⃣
@WhiteDNS</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/whitedns/521" target="_blank">📅 10:03 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-516">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Beta7-x86.apk</div>
  <div class="tg-doc-extra">22.8 MB</div>
</div>
<a href="https://t.me/whitedns/516" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید تستی WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
در این نسخه تمرکز اصلی روی مدیریت راحت‌تر پروفایل‌ها، اشتراک‌گذاری تنظیمات اتصال و پایداری بهتر بوده:
✅
نسخه اپلیکیشن به 1.0.0-beta7 ارتقا پیدا کرده
✅
امکان Import و Export پروفایل‌های اتصال StormDNS اضافه شده
✅
حالا می‌توانید تنظیمات سرور شخصی را به شکل لینک stormdns:// خروجی بگیرید و برای دیگران بفرستید
✅
امکان وارد کردن چند لینک پروفایل به صورت هم‌زمان اضافه شده
✅
دکمه‌های Copy و Share برای لینک پروفایل اضافه شده‌اند
✅
امکان Export All اضافه شده تا بتوانید همه اتصال‌های سفارشی را یکجا خروجی بگیرید
✅
پروفایل‌های اتصال حالا با کشیدن و رها کردن قابل مرتب‌سازی هستند
✅
Resolver Profileها هم حالا قابل مرتب‌سازی شده‌اند
✅
ظاهر بخش Profiles مرتب‌تر شده و دکمه‌های ویرایش، حذف و خروجی گرفتن واضح‌تر شده‌اند
✅
وضعیت پروفایل انتخاب‌شده و پروفایل فعال واضح‌تر نمایش داده می‌شود
✅
قابلیت Traffic Warmup اضافه شده تا بعد از اتصال، مسیر ارتباط سریع‌تر آماده شود
✅
قابلیت Keepalive اضافه شده تا با ارسال ترافیک سبک دوره‌ای، اتصال پایدارتر بماند
✅
Traffic Warmup و Keepalive هم در Proxy Mode و هم در Full VPN فعال هستند
✅
از تنظیمات پیشرفته می‌توانید Traffic Warmup را روشن یا خاموش کنید و مقدار آن را تغییر دهید
✅
نمایش لاگ‌ها و وضعیت اتصال سبک‌تر و مرتب‌تر شده تا صفحه هنگام دریافت پیام‌های زیاد روان‌تر بماند
✅
دکمه Donate اضافه شده و امکان کپی کردن آدرس‌های حمایت مالی داخل اپ وجود دارد
پیشنهاد ما این است که اگر فقط به تنظیم پروکسی نیاز دارید، همچنان از Proxy Mode استفاده کنید. حالت Full VPN برای تست وجود دارد و بهتر شده، اما چون کل ترافیک دستگاه را از تونل عبور می‌دهد ممکن است روی بعضی دستگاه‌ها یا شبکه‌ها سرعت و پایداری متفاوتی داشته باشد.
اگر سرور StormDNS شخصی دارید، حالا می‌توانید پروفایل اتصال خود را راحت‌تر با لینک stormdns:// ذخیره یا برای دیگران ارسال کنید. همچنین استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند فشار روی سرورهای عمومی WhiteDNS کمتر شود.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
#WhiteDNS
لینک کانال:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/whitedns/516" target="_blank">📅 09:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-515">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/P4WWIF14fnENnh3IaC8EgD85DBx1O5XC5ib18MvGDu_Ztkw2W1ml693KBDOSqtzYArjIrlIrkjvgKouqiWUDZl7cGafNF6QoU6IBEC24H7Bt6xXygebG3ivwSY8C6nnutyIHMJJAYpZ-IpM-oyuNJKQBJWsj-IT-IwmKBwMakWtQxpT8705M3MtWNaKePBZh3kAWWDeucHAzACESyOAnyboyufTTneKdIjhz9gszyo16gLT1Yf2qHLLLgm8C9gUmheYIiGzCXselDwW4IvMc4Q0VfSKwICKHfZQVp6hlFa7cDLdCuzj6zppttqjqp9vvhSYcRmrTnp-I0D1P2Vc5OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/whitedns/515" target="_blank">📅 06:59 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-513">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❤️
سرور اختصاصی whitedns برای Slipnet
❤️
آموزش کامل :
https://t.me/whitedns/294
دانلود کلاینت :
https://github.com/anonvector/SlipNet/releases/tag/v2.5.3
User:
whitedns
Password:
whitedns
[dnstt-socks] Public Key: 1b23cc151ab07274a4f2623a94b7172d61803956fa068f5074e38ec5eb800516
[dnstt-socks]
slipnet://MjJ8ZG5zdHR8ZG5zdHQtc29ja3N8dC5pcmFubW90b3IuYml6fDguOC44Ljg6NTM6MHwwfDUwMDB8YmJyfDEwODB8MTI3LjAuMC4xfDB8MWIyM2NjMTUxYWIwNzI3NGE0ZjI2MjNhOTRiNzE3MmQ2MTgwMzk1NmZhMDY4ZjUwNzRlMzhlYzVlYjgwMDUxNnx3aGl0ZWRuc3x3aGl0ZWRuc3wwfHx8MjJ8MHwxODUuMjMwLjIxOS4xNjd8MHx8dWRwfHBhc3N3b3JkfHx8fDB8NDQzfHx8MHx8MHwwfHwwfHwwfDB8MTA4MHwwfHR4dHwxMDF8MHwwfDB8MHwwfDB8MHx8fDgwODB8fDB8L3wxfHw=
[noizdns-socks]
slipnet://MjJ8c2F5ZWRuc3xub2l6ZG5zLXNvY2tzfHQuaXJhbm1vdG9yLmJpenw4LjguOC44OjUzOjB8MHw1MDAwfGJicnwxMDgwfDEyNy4wLjAuMXwwfDFiMjNjYzE1MWFiMDcyNzRhNGYyNjIzYTk0YjcxNzJkNjE4MDM5NTZmYTA2OGY1MDc0ZTM4ZWM1ZWI4MDA1MTZ8d2hpdGVkbnN8d2hpdGVkbnN8MHx8fDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[dnstt-ssh] Public Key: 1b23cc151ab07274a4f2623a94b7172d61803956fa068f5074e38ec5eb800516
[dnstt-ssh]
slipnet://MjJ8ZG5zdHRfc3NofGRuc3R0LXNzaHx0cy5pcmFubW90b3IuYml6fDguOC44Ljg6NTM6MHwwfDUwMDB8YmJyfDEwODB8MTI3LjAuMC4xfDB8MWIyM2NjMTUxYWIwNzI3NGE0ZjI2MjNhOTRiNzE3MmQ2MTgwMzk1NmZhMDY4ZjUwNzRlMzhlYzVlYjgwMDUxNnx3aGl0ZWRuc3x3aGl0ZWRuc3wxfHdoaXRlZG5zfHdoaXRlZG5zfDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[noizdns-ssh]
slipnet://MjJ8c2F5ZWRuc19zc2h8bm9pemRucy1zc2h8dHMuaXJhbm1vdG9yLmJpenw4LjguOC44OjUzOjB8MHw1MDAwfGJicnwxMDgwfDEyNy4wLjAuMXwwfDFiMjNjYzE1MWFiMDcyNzRhNGYyNjIzYTk0YjcxNzJkNjE4MDM5NTZmYTA2OGY1MDc0ZTM4ZWM1ZWI4MDA1MTZ8d2hpdGVkbnN8d2hpdGVkbnN8MXx3aGl0ZWRuc3x3aGl0ZWRuc3wyMnwwfDE4NS4yMzAuMjE5LjE2N3wwfHx1ZHB8cGFzc3dvcmR8fHx8MHw0NDN8fHwwfHwwfDB8fDB8fDB8MHwxMDgwfDB8dHh0fDEwMXwwfDB8MHwwfDB8MHwwfHx8ODA4MHx8MHwvfDF8fA==
[slipstream-socks]
slipnet://MjJ8c3N8c2xpcHN0cmVhbS1zb2Nrc3xzLmlyYW5tb3Rvci5iaXp8OC44LjguODo1MzowfDB8NTAwMHxiYnJ8MTA4MHwxMjcuMC4wLjF8MHx8d2hpdGVkbnN8d2hpdGVkbnN8MHx8fDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[slipstream-ssh]
slipnet://MjJ8c2xpcHN0cmVhbV9zc2h8c2xpcHN0cmVhbS1zc2h8c3MuaXJhbm1vdG9yLmJpenw4LjguOC44OjUzOjB8MHw1MDAwfGJicnwxMDgwfDEyNy4wLjAuMXwwfHx3aGl0ZWRuc3x3aGl0ZWRuc3wxfHdoaXRlZG5zfHdoaXRlZG5zfDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[vaydns-socks] Public Key: ecef7073cd119405e62f1347daa949794193ccd618f0f879fa7c10da37a7f53e
[vaydns-socks]
slipnet://MjJ8dmF5ZG5zfHZheWRucy1zb2Nrc3x2LmlyYW5tb3Rvci5iaXp8OC44LjguODo1MzowfDB8NTAwMHxiYnJ8MTA4MHwxMjcuMC4wLjF8MHxlY2VmNzA3M2NkMTE5NDA1ZTYyZjEzNDdkYWE5NDk3OTQxOTNjY2Q2MThmMGY4NzlmYTdjMTBkYTM3YTdmNTNlfHdoaXRlZG5zfHdoaXRlZG5zfDB8fHwyMnwwfDE4NS4yMzAuMjE5LjE2N3wwfHx1ZHB8cGFzc3dvcmR8fHx8MHw0NDN8fHwwfHwwfDB8fDB8fDB8MHwxMDgwfDB8dHh0fDEwMXwwfDB8MHwwfDB8MnwwfHx8ODA4MHx8MHwvfDF8fA==
[vaydns-ssh] Public Key: ecef7073cd119405e62f1347daa949794193ccd618f0f879fa7c10da37a7f53e
[vaydns-ssh]
slipnet://MjJ8dmF5ZG5zX3NzaHx2YXlkbnMtc3NofHZzLmlyYW5tb3Rvci5iaXp8OC44LjguODo1MzowfDB8NTAwMHxiYnJ8MTA4MHwxMjcuMC4wLjF8MHxlY2VmNzA3M2NkMTE5NDA1ZTYyZjEzNDdkYWE5NDk3OTQxOTNjY2Q2MThmMGY4NzlmYTdjMTBkYTM3YTdmNTNlfHdoaXRlZG5zfHdoaXRlZG5zfDF8d2hpdGVkbnN8d2hpdGVkbnN8MjJ8MHwxODUuMjMwLjIxOS4xNjd8MHx8dWRwfHBhc3N3b3JkfHx8fDB8NDQzfHx8MHx8MHwwfHwwfHwwfDB8MTA4MHwwfHR4dHwxMDF8MHwwfDB8MHwwfDJ8MHx8fDgwODB8fDB8L3wxfHw=
@whitedns</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/whitedns/513" target="_blank">📅 05:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-510">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎁
۷ سرور اهدایی
با تشکر از رسول عزیز، یکی از اعضای خوب WhiteDNS
❤️
#Servers
🌐
Domain:
g1.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g2.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g3.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g4.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g5.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g6.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g7.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/whitedns/510" target="_blank">📅 05:14 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-507">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کانفیگ تمام سرور های WhiteDNS و اهدایی آپدیت شد
🚀</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/whitedns/507" target="_blank">📅 03:39 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-506">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دانلود WhiteDNS Beta6 از سرور های داخلی
📶
WhiteDNS Beta 6
1⃣
📶
WhiteDNS Beta 6
2⃣
منبع
@link_dakheli_app</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/whitedns/506" target="_blank">📅 18:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-505">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">White DNS
pinned «
سلام خدمت همه دوستان  ما تا امروز حدود ۳۰ سرور مختلف داخل کانال منتشر کردیم. بعضی از این سرورها داخل اپلیکیشن اضافه شده‌اند و بعضی دیگر از پست‌های فوروارد شده یا منابع مختلف بوده‌اند.  برای اینکه همه چیز یکجا و مرتب باشد، لیست کامل سرورها را اینجا قرار می‌دهیم.…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/505" target="_blank">📅 18:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-504">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سلام خدمت همه دوستان
ما تا امروز حدود ۳۰ سرور مختلف داخل کانال منتشر کردیم. بعضی از این سرورها داخل اپلیکیشن اضافه شده‌اند و بعضی دیگر از پست‌های فوروارد شده یا منابع مختلف بوده‌اند.
برای اینکه همه چیز یکجا و مرتب باشد، لیست کامل سرورها را اینجا قرار می‌دهیم. ممکن است کیفیت و پایداری بعضی سرورها در زمان‌های مختلف تغییر کند، پس اگر یک سرور کار نکرد، سرورهای دیگر را هم تست کنید.
ادامه داشتن این پروژه و وصل ماندن کاربران، مستقیم به حمایت شما بستگی دارد. اگر دانش فنی دارید و می‌توانید ماهانه حدود ۵۰ دلار هزینه کنید، با دونیت کردن ۵ سرور می‌توانید به وصل شدن تعداد زیادی از کاربران کمک کنید.
domain:
t1.prs612.us
Encryption Key:
3e80a0eb3e1fba2bf17e0e0eb5783dc5
domain:
t2.prs612.us
Encryption Key:
afc1bd5e98cd98cde7515adb7295122b
domain:
t3.prs612.us
Encryption Key:
8786a860148e2d4d55403ae3c80ba854
domain:
t4.prs612.us
Encryption Key:
943664f15fd1763e242ce12ba993d9c9
domain:
t5.prs612.us
Encryption Key:
6a9ab24a8bd3937378efbfb3c23e1358
domain:
t6.prs612.us
Encryption Key:
71201fedadfbc0b62189c08961bce651
domain:
t7.prs612.us
Encryption Key:
c4ff91174a79e9e03a4d6727878ada17
domain:
t8.prs612.us
Encryption Key:
ae5db6f03e485214e1fcc9d26a4c0a2f
domain:
t9.prs612.us
Encryption Key:
a01c03a340a3e684a2815961e086eb27
domain:
t10.prs612.us
Encryption Key:
f3a3c5d02bb7ce04f6a4f144fc35e9cb
domain:
t11.prs612.us
Encryption Key:
e7f2db07e778563d31ed1fc80d5fe612
domain:
te.link-dakheli-app.shop
Encryption Key:
TelegramChannel@link_dakheli_app
domain:
s.o4s.shop
Encryption Key:
TelegramChannel@link_dakheli_app
domain:
s2.o5s.shop
Encryption Key:
TelegramChannel@link_dakheli_app
domain:
v.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v3.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v4.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v5.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v6.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v.whitedns1.shop
Encryption Key:
c8328f9d541860df1637b9b3ed7b990e
domain:
v.whitedns2.shop
Encryption Key:
7ecd7b6271c47e348f6ab177517ee8fa
domain:
v.whitedns3.shop
Encryption Key:
9d7aedcaf1f94e784a24fdfc1348a337
domain:
v.whitedns4.shop
Encryption Key:
0ce14ab71acebbd46b8129e25593155a
domain:
v.whitedns5.shop
Encryption Key:
2dffd162cb02b278c1ab57ee17fe07ae
domain:
v.whitedns6.shop
Encryption Key:
e32afdaa30ca36ead696cd90d84ced15
domain:
v.whitedns7.shop
Encryption Key:
6394eec942238533798ec7524eb7ea66
domain:
v.whitedns8.shop
Encryption Key:
1c167e9850936655c480e4938b2c5c35
domain:
ob.networks.icu
Encryption Key:
3947d5ac68015a09a53a0b361bd82999
domain:
ts.networks.icu
Encryption Key:
e0e71e667e5dcfe3b18e3bce659773d2
domain:
zw.networks.icu
Encryption Key:
0798c0e8aa05080125e6c65282fd792b
domain:
v.0x0.guru
Encryption Key:
33815e1bcb88873f2199c735828ea745
domain:
v.iranmn.best
Encryption Key:
aaed913b8367fce3e20910472d9e3e2d
domain:
v.kmjhfilterchi.shop
Encryption Key:
4f3d0262ba2bd7cc20b596bdbc77f761
@WhiteDNS</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/whitedns/504" target="_blank">📅 18:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-503">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcisQLE55gFOPTuBH_4J0fYbOxrlev8E9AGjdbl7a4ArlW0IGjEA5KemkNxjAn4wd1VI5J3-cgiJAKLbXA-MggjaIaMcKvn4A19BivjlvXaancnY5EmfCro6nV8omHR1KwujLVMyzhay8kh7OdbdM5K_k3rDmFcXWeGYlVI7qaxrXIxuEaTbtU52Twur5b-GJqamXRZGqoVm2JQUwyTl7B_5WduKxdI7Sew3VFr77icuvWykoaIsN8DnqCWz0TNe_-UN5deMGeu7ff6NrTyXG3xKOTFc7albKyn4uWIsD6eU3ey6_MD-1se-Mr1tUh7GnYVzYYukU4UP7s4uQOawYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/whitedns/503" target="_blank">📅 16:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-502">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uf3zQmslG2qS0v6SGgN13jh6b9Cplw_qK6iiEXH2lJire9dBblypFYwY0QWyiiEo-O0z_zYcuE443yx0ecHbcwHOMdz4L1auq36UcNfstC4oPbEWpMXV4JKkY9dZJWPFV-L3bX1j30rDFDsTu594lLSgAy4ruvhqQOvaWBv7AGsbUhccKQOUS7LbWcQS7k_VZEfOiqNfsoAUT7ITgLXX2eamr2PwaJ6MEjudwNqkPddwfhRERttXlir0P476OB562A03kavWPB96n1HAia0vypLGl01c0GZgXiIgPJhPUcx2c4YNvj2zVBHJqDfoHWTScXNHliq8WDLweRPYbFl50w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به هر دلیلی میخواهید از حالت پراکسی در whitedns استفاده کنید بهترین کار استفاده از اپ نکوباکس هست   https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/tag/1.4.2  #Nekobox #Proxy #WhiteDNS  @whitedns</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/whitedns/502" target="_blank">📅 12:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-501">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/EUheFaVtr3oJhaWspQe-oFFARYS2aO5ZRsnbYWniY2guCPoARX1yMGXtcMn80tOwc6yrgz4sC73_IIlp7XVc16gHGUX7oytI-puca16uxPM7tm9vjcsKX3cyCDtaDJnTh5pXJda5Y7MrnkO78HRNO4ubI6q2qXUzSSkZCuDSxTrN0yhxwahy0-6kh3CLeejOXR2P0hHpNq-9GzmYe36BW8IL4SOXqobT-Vw-saMLB81P8_j85390uEB3oHLVvEnXBV_Y8_3Y1L191ICU719eyZWvD_ealrNzGpHBybM6bTMa50H1TWZWRe2g9rBv9a0kS2064euZIvnf_fU6paz8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/whitedns/501" target="_blank">📅 11:59 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-495">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromConfig plus</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGy9WwwYSLP-RvGNL5pDOsfiFiaEQ4fdX7KuFAxau0g2rzhvnHar0PuZk8OkL9WcvA06zLtDAvpuSUqjD5z8aa-uD3csH4WhVYiF1H3vv-oFyRDCt9KP7V1rpX9uhPH3ooOuwo8Vg5CmxyShGvXoFvZ9YuD1B9c38Da_HxYGf9PC8uhFLWegAkBGXgm3Rxq83hErT86Vt1L9XNxQ5Zyvkbo567m65UTmCQ3xnKDE1sFb_bvnTh_sAvtm9WRHDwNzLWZ8HZkdS6M5HVnWmIF_IlooJpKjkXPuof19NYoEXfotjFMEn4yxae6s8GLAs5inpRKxl00BREfbv80jO07ucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMKnLl1EO5jeSolZbKV1IdfOYVZqV2SD6wjM8tB_6Va2tf79M4FL5vAqbgG4eLkzTAxBMDpO8oTSDoUyQgD9lBWtoR0wO-rhOhQGXhHUdeL7xxwSpK77MFyUM9oJ_UM8J7x2pxRKTVZIqz8FothK95eFKFD5DDCRzx0f6J0H71B-iwlg5_CVRS-ByJADHOoNnfwZYNGZoFQUw3Cd3cny-wGP2K2OVxD-HhUIihrL7lm7HPnAWq-puoc3L99HD1rarMWuZZymNasuTsYFW8kNJ3Dg3N61ve2gNS8qWFqcz0Dg8usqVLCDyJ0PyxUaQmrm1wB2e_jk2NB-aV5ik7bqEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uH9EqQDW-CgA7OviuzJ_HLhHvaPWISy53o0RRAFYLgJCX2dCBPF_2JK9KjNCPtxgUheRR-HMO8o42dULnYpD3eAedWJxTjhbYk9-1sI35i-b8QKY6wg1qtDITf9B7OruxPGhTMmjF-Uh19SMgXRmqB1HLYTHsDzki6Lia4feIX4hoN7G4a1q-l3dJTFfsfAoXSyT4afmrKDbzOAx6yi_Hb9-tbiu_piklOy4jKASJhvASu5eKdiFfk_7n1y42lM2aNSRjR-3E_hG0ArzmJxQurLmQjQbQ_2dYQREl8sdIYobXPaAPn-z1sENZLQe7coa6qAovDqiJN-_T6wi0B4c0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IhBm07uvVizXbKfs1HIsOEK2h0zF9DlcP3FIFqyEXvnBrAvIt_BeM3s-M6ShRhpiHYp8Ozq07DxQz7hfBNE3mGZbTIOqhQmTc9vUIYn97X-CDpt_ew91cSGfo3dlzECfnJe3hvQlEIfoFKj4QXZHW2HZiQgsKaECSXbhJum8OinMWuthrsg2SPueZRzTymP-YUV3t7iNYSwRPRIpASspOQIPb6TpZCij8aCXIUzIpH45gDZquY4Mvxh3zbQSqSxaizBNOfhhJk4WckZoS5Ps54NA4yvcA42FESz_znbGWQ2RShrksM2n6iTslx4ZSVdf9AyGVAnrTUbYdTvNQqhdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SLBIV2IDJ2JOL9QmQwSLfSZ6Pz1y2iTntSSuhwuOeGKggryZk_muK88-EK0o2-ThUBU8eArCmnCu1hLzDAhyJl_WCGRc8Y1bnwZltKqtA4eNdYgnkPz9jZxuKt36EE2OV_nYxwgEVkPWUVDRfTAKj2pWIEqV19NLHiidg3iuTmFEjfaKYrWrP5N8qGAdFcbBfVwSArCXXO8sDhknGeL2ThHmW7hP0YH-QK5EmUuKkes695WPRcb92Y5T9umeesKVdpY8adoMy4KL94r0a8S__v4O4xliAKfw_ZhdrGVPebS3PuhR3LQWrV0P5EngkekaSlweccTqWfLEt24x6N-YrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKy7VHH5hgCzWjlR1JXj3N5cI2ChV_YyOxddDz8qp1PnhKDdH-t5LgjJzQgRa6m1lKG_q8dASIcqWDyTHA9XoZCsgIqPoJ7pSE1sWKJI6_O-NnUu-Pi7UMGN81OgcoPMALfIrRjb0anxoqHgy9OKxX-Dx-bcx0clxrs_PJFEX6unvI6lFM0ue1pAbQwkgtju9ZQ1VWdtmE_zR00plTQs6l5tyeHooetmyGlTjwXi0rd7eKZUCsIvcTPkNsyQGQRIJHqsYFFCbSzoKN-nzSGJ0zVYd-3uXYMRJHiH8axZN5jVyWxs3OhKC8zxtNoBwMSMTgg2SG37WXS3GfEiJSVnCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔺
آموزش اتصال به برنامه whiteDNS در اندروید
1.ابتدا اول برنامه رو دانلود کنید از طریق لینک داخلی :
https://guardnet.ir/f/8f0ef50b3049
رمز فایل موقع استخراج:
3666
مطابق تصاویر بالا کانفیگ ها و ریزالوز ها را وارد نرم افزار کرده و تست کنید.
کانفیگ ها :
1- دامنه :
ob.networks.icu
🔐
کلید رمزنگاری :
3947d5ac68015a09a53a0b361bd82999
2- دامنه :
ts.networks.icu
🔐
کلید رمزنگاری :
e0e71e667e5dcfe3b18e3bce659773d2
3- دامنه :
zw.networks.icu
🔐
کلید رمزنگاری :
0798c0e8aa05080125e6c65282fd792b
اتصال برای تلگرام با پروکسی از طریق پورت 10886 و لوکال‌ هاست
127.0.0.1
به پروکسی زیر متصل شده و وارد تلگرام شوید و حدود 3 الی 5 دقیقه منتظر بمانید تا تلگرام آپدیت بخوره
https://t.me/socks?server=127.0.0.1&port=10886
این روش و برنامه برای تلگرام تست شده ولی خیلی خوبه ، برای اینکه سرعت بهتری داشته باشد در تایم شب بهتر عملکرد دارد و سرعت بالاتری دارد. اما در طی روز هم برای تلگرام برنامه جواب میده.
هر گونه سوال بود داخل دایرکت هستم :
t.me/Config0plus?direct
🟢
Join:
https://t.me/Config0plus
جهت حمایت از ما ری اکشن فراموش نشه</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/whitedns/495" target="_blank">📅 09:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-494">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سرورهای WhiteDNS تا امروز نزدیک به ۶ ترابایت دیتا جابه‌جا کرده‌اند.
این آمار فقط مربوط به سرورهای اصلی WhiteDNS است و دیتای سرورهای اهدایی داخل این عدد حساب نشده.
حالا بیایید خیلی ساده حساب کنیم:
اگر هر گیگ کانفیگ فیلترشکن را حدود ۲۰۰ هزار تومان در نظر بگیریم:
۶ ترابایت = ۶۱۴۴ گیگابایت
۶۱۴۴ × ۲۰۰,۰۰۰ تومان = ۱,۲۲۸,۸۰۰,۰۰۰ تومان
یعنی با کمک هم، تا امروز چیزی حدود ۱.۲ میلیارد تومان هزینه خرید کانفیگ را کمتر کرده‌ایم.
برای مقایسه، هزینه سرورهای ما نهایتا حدود ۳۰۰ دلار بوده.
اما اگر همین حجم دیتا را می‌خواستیم از فروشنده‌های فیلترشکن بخریم، با دلار حدود \`۱۸۰ هزار تومان\`، هزینه‌اش تقریبا می‌شد:
\`۶,۸۰۰ دلار\`
این یعنی با یک هزینه خیلی کمتر، چندین برابر ارزش واقعی سرویس به کاربران رسیده.
دم همه کسانی که تست کردند، گزارش دادند، سرور اهدا کردند و کمک کردند این مسیر ادامه پیدا کند گرم.
WhiteDNS رایگان ساخته شده، رایگان می‌ماند، و هدفش این است که دسترسی آزادتر برای همه راحت‌تر شود.
ممنون از سازنده های اصلی پروژه هایی مثل MasterDNS و فورک StormDNS
🙏
این اعداد فقط برای سرور های ما هست و نه سرور های اهدایی. اعداد واقعی خیلی بیشتر از این چیزا هستش.
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/whitedns/494" target="_blank">📅 09:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-493">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQz7Lilr0R99ZBTckprqzAJX8eCNTJEtB5kJRnrnPz-qDr23xm45aG-qJ7YGuJXb2UfjSZ7b383QZZUHzKr0dBV7afvVMYpcGfSX9McN-EW1RTOiabBNiGY6NefsUa6m5MKc4jkh1xHvH3zm7fNLxGuqfnAxnRuUcck88JC6a5yjFaP0Fgtsc7JU_4Q1RGM0g1CDFK1Hb85kWep0FGnmZ4Z02OpPDCr7IRMsf_J7sUpGTZXtbnsPRZpKcgAm-kJXyg9X_43GISIMu0Nv0XVqCwx8rFWw7hVc2nXi_QB3dAnAiWHzwA-PD1wy4vs-kx19uS77FNcxR7WCwf7Y5ttGzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ربات WhiteDNS حالا امکان جدید دارد برای دریافت ریزالور های MasterDNS / StormDNS
۱) وارد بات زیر شوید
@dns_resolvers_bot
۲) متن زیر را برای ربات ارسال کنید
/dns_master
۳) برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/whitedns/493" target="_blank">📅 09:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-491">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">server_config.toml</div>
  <div class="tg-doc-extra">11.1 KB</div>
</div>
<a href="https://t.me/whitedns/491" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
StormDNS Server Tuning برای لود بالا
پست مخصوص دوستانی که سرور شخصی دارند
!
ما برای سرورهای StormDNS یک اسکریپت تیونینگ آماده کردیم که هدفش پایداری بهتر زیر
فشار و کاهش قطعی کاربران است.
این اسکریپت چه کار می‌کند؟
👇
✅
قبل از هر تغییر، از فایل‌های مهم بکاپ می‌گیرد
✅
تنظیمات server_config.toml را برای لود بالا بهینه می‌کند
✅
تعداد UDP reader و DNS worker را بیشتر می‌کند
✅
صف پردازش درخواست‌ها را بزرگ‌تر می‌کند
✅
بافر UDP/socket را افزایش می‌دهد
✅
محدودیت فایل‌ها و پردازش‌ها را در systemd بالا می‌برد
✅
تنظیمات kernel/sysctl مخصوص UDP و شبکه را اعمال می‌کند
✅
پورت‌های DNS یعنی 53/udp و 53/tcp را در فایروال باز می‌کند
✅
لاگ را روی WARN می‌گذارد تا زیر لود، سرور با لاگ زیاد کند نشود
✅
تایم‌اوت اتصال SOCKS را روی 5s می‌گذارد تا مقصدهای خراب یا unreachable کاربرها را
مدت طولانی معطل نکنند
✅
در پایان سرویس stormdns را ری‌استارت می‌کند تا تنظیمات اعمال شوند
⚠️
نکته مهم: ری‌استارت باعث قطع شدن sessionهای فعلی می‌شود، پس بهتر است روی هر سرور در زمان مناسب اجرا شود
اگر نمی‌خواهید همان لحظه ری‌استارت کند:
sudo bash /root/stormdns_tune_all_servers.sh --no-restart
اجرای عادی:
sudo bash /root/stormdns_tune_all_servers.sh
📌
این تیونینگ جادو نمی‌کند؛ اگر مشکل از resolver، DNS delegation، مسیر اینترنت
کاربر، یا destinationهای خارجی باشد، فقط با افزایش منابع حل نمی‌شود.
ولی برای سرورهای پرلود، باعث بهتر شدن queue، socket buffer، limitها و رفتار اتصال
می‌شود.
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/whitedns/491" target="_blank">📅 08:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-490">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروح جنگلی👻</strong></div>
<div class="tg-text">اخرین اپدیت سرور های روح جنگلی از ۵ سرور ۳ عدد به استورم اپدیت شدن
سرور فنلاند
v.0x0.guru
Key:
33815e1bcb88873f2199c735828ea745
سرور فنلاند
v.iranmn.best
Key:
aaed913b8367fce3e20910472d9e3e2d
سرور آلمان
v.kmjhfilterchi.shop
Key:
4f3d0262ba2bd7cc20b596bdbc77f761
روح جنگلی
WhiteDNS</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/whitedns/490" target="_blank">📅 08:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-489">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuTUyx7EyavFsxFVVJkqcy4TFGHILlCZFTPvLK48_vSovApmX_kixRoiZ0cO-yzvMKO-FFEyshadPz5OTyROHoKnG5D6SlR9VsLRat_NeV-ugvPGDAgeacOf3Kw-ph6pE5mVPLUV8iHHWL_aKKYMl4PNnn7baxu9Uqdr3m-xvtnk4ZuE2-zq-Z1kO8sk64ZCC21yYV6lNCzny0yHO2S7XBPsG8g-48NMc4edv1kWXy8OLt-1HplvkqDmZhl6NeEovmJuaoARbnMUqj5DztAZw5SENqiDXb7DTmd57VUrqyrjyuMui0wUGC6wogL2Mii9quyo6_DLXggUW25No6AT9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همه دوستان
🌐
برای دریافت آخرین آپدیت‌ها، آموزش‌ها و اطلاعیه‌های مهم خارج از تلگرام، حتماً اکانت جدید ما در X رو دنبال کنید:
🔗
https://x.com/WhiteDNS_Team
@WhiteDNS</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/whitedns/489" target="_blank">📅 07:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-488">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/whitedns/488" target="_blank">📅 05:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-487">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/487" target="_blank">📅 05:01 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-486">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwZk7V4AaWqokka3pGCeU_VAk8V4c-2X1KFTRVZn6oWwE5lBDCaK0fy5rW7r0sGAztwdG4PFgfkEwoudQ2lU2LCXbCENLwl2QCyLpcO_qntrdQIQCGGi2g92_Ps7RDjKcUyk258J2AscKFYLj1oxPEu7BSFdo9Xzd295Jv5z2AGEYP-E-M9KESmwqNwFUio4nxcCvvGnu54isCilbpWNyYdYK3PMh8Mg6vGv2PqzkflKnoeWs_hsLQtBwhM-6_r056H41GQEQfs6VnniJIjgC3ydCTDIMYtcDqiUre8Cp4Zpcs-rf5bj23Yl6sQywRMNKuYH4_MoMHx1jLw3lWcnqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/whitedns/486" target="_blank">📅 04:59 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-485">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS_Resolvers.txt</div>
  <div class="tg-doc-extra">8.5 KB</div>
</div>
<a href="https://t.me/whitedns/485" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">۵۱۲ ریزالور جدید تست شده تیم  WhiteDNS
مخصوص اتصال StormDNS/MasterDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/whitedns/485" target="_blank">📅 02:44 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-478">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخدماتی حامد📱📶</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcgldgcsp45IQVEo54sq1w4BS-jRDkt25oXerJWdZT2iWYx8Ng5_WipNS-1zyrqS2R8_IqoX9IaqWCK674uFp_ft1tDq0T5U44VKnhF8akvKtWPb9WXGSn_j7yntOuO_ylW93bwyJKrRCUCjrjXYCs540kbhvLYodf8OAU_hCrwB_aUxR3nV76lt3zPs0kmN1Xh7W1UJBjLLubjigPNvQl67YYzgBpSBjk56xqpv3mCeBSKX4OZ_m75AcaPxlpLf7HWWnWcVjG2wieMJSKgkDuzt0wUcKeyAOz6hPKoYi3pvPzj_1ifl155qhpbxtn44e4aRnDafe4Wot3v07NI8oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmPE5RaVADEqeMckQ0WB-KKX4GWLYldh5OsVZI9-qGC3tcXgihXCxSGtmJHLiW1JrzN7LMBUrO8EoSOGJMjOI7umC5kgqJiJbCsqfEyQSuQUArmD1wqEtbwYxWfszJ_gPJs0iNxPxrqwTIlnv4vNSf1ufjh-t85hXdd5_nKAfxf8b3FMLvfwfdQ8EduGE8nLwRLp3nX5159sL0T8EDgwmbEZznqPK0FcuK9UJ1JNyzrbDQm2V809e9Tt2ruMJYLyE35qckUPh_-UkTXHDCFcag5WL6x-yqiBMoknKBLT40kvKquf-N93dTkeJoH32hyb1_3q8k40H9JmuAuzuyi_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLBoFd8RFKlp_Yavvbmt6K2Ek7wmIWey_g85d7vvhzPxtqbPdfeiuqvdhpwpWFuFYlCix9hA1rNvOSDO6Otx9tl3d2-d2Rhxed0FPQG6q3_HG-HcXAPPyevbDn3WUAClwNB3AjfAm3izggSjU5tarUdjYpGxgXtQEsClDlMqll-Djdcfa2sOtR6qK0LrupNPxgLsgeZ9IpD5e0U6cdB2TExS6sUttv1Ku_UHfQVjCALdtFrNWs7m8hgV55MD8hKT7gVR8-5A6hEZmvyuN_bNlAhaNWNgy54jrL7n2TqTcGRX987NZLiKGIPrAduIrPooSzrAAKOCJXjuDyoKJ25npQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NkTn3wkVeJRPA3R3i_4quWoAMNgi5X-ShQu9UsnpH5Zl33KAs3FKv64cD9o2ueHbPgBEtShU1tzUtBMdmIV_0VRF2wMnVHnE7ZIOCRzY1S1GQFadayfyg4zWzLbVsDAORVvJNpO95A2Dr4WdBKUiIA3shtDB6BKS0NPsoH96rzqxQfJGx_sgRm4_apWm6B4mlkSNhoWPq1MAV6_mWH-_Fd9ulI8t3HIc8OfmO_zd6F-RANWUe9CYutLq5y3jzKNf0TYe7Ib1Zk73xyD6jLwEBuoSO2J9iQl_b2ph_p6ckrjdFpmMsfSZCLGyW4JTxOXLvm58Ha3huRlfAJvO-kJxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpl4iVz1qRzeM-tWqebnbvEwShL-JPEGLK9XkKe8ddkfRDGvO9bOLyBjK9rWumudcxAfy5DtqgNp3t0uNltq_EhWC8zEC4OsJT6ciJX0lxW2DbXlYt5DVUEtY0UbXhDb-aCgDuD3nUMXldqSwTBRV9tEW6MZpNDv0ZgVYy0fK8WV8zAWUOZ9qU4xdPejUQ4HECrp_ESKIZdAjs5rUTetel3DbaS_bF2guGm_-axrcaI_YNEe7VHD1lRbuS7SD4C3oHg4NUjxFiMwh6jz3S6pexXg0dPJBblpVL_8FqcGpRKkfMtIrv7v2u5dnFzk0yWDq8NwJtquJ8QCp2jRY1BLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qYxnAddtdaWQJl0NPGJgsNdKMj8xSSipcGRNPvrIV0m8Kwy4bgdZvXwd-fPxgGBfjmqCulKJ9pkLbdwOCI0THBxKowsX7jPNFhUYO2RYlA1x1b5e1kgA10k-ES_zOozV4_d3ptfzDbWmY5mTrwC4XJ0AmGEoUqTfT13xIcOxxIaNlYS6WAOT89jzcan8xlWioql4lWMs6713jaQsg43bAXAKlCjquOyqSx3p-BZ48UEstJhsV0koGmCNbiEYNsOJVC88xCrHGe4KdXOFKLvKx2JHsa5bmRpyKeFlq3VzHq-qZ4ogpdPQXBZSzUYsP68QSKNJ__rJBCvnMdEY2qyA3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش اتصال وایت dns در اندروید
1- نرم افزار را از آدرس های زیر یا پیام بعدی دانلود و نصب کنید. (White DNS)
لینک شبکه داخلی (بدون نیاز به فیلتر شکن)
https://dl.toolschi.com/view.php?f=48c485b41de6bf08.zip
https://guardnet.ir/f/Universal
رمز فایل : 3666
2- مطابق تصاویر بالا کانفیگ ها و ریزالوز ها را وارد نرم افزار کرده و تست کنید.
کانفیگ ها :
1-
🌐
دامنه :
ob.networks.icu
🔑
کلید رمزنگاری :
3947d5ac68015a09a53a0b361bd82999
2-
🌐
دامنه :
ts.networks.icu
🔑
کلید رمزنگاری :
e0e71e667e5dcfe3b18e3bce659773d2
3-
🌐
دامنه :
zw.networks.icu
🔑
کلید رمزنگاری :
0798c0e8aa05080125e6c65282fd792b
برای دریافت ریزالوزها از ربات زیر استفاده کنید :
@dns_resolvers_bot
اتصال این نرم افزار در اندروید روی پورت 10886 و لوکال هاست (
127.0.0.1
) است.
پروکسی تلگرام :
tg://socks?server=127.0.0.1&port=10886
‌‌
@hamedvpns
☑️
لایک   |   Like
👍
❤️
اشتراک بزارین   |   Share
⭐</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/whitedns/478" target="_blank">📅 02:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-477">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/whitedns/477" target="_blank">📅 13:21 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-476">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/igaV7K9M23kEvKJ3byxWYoIu01o9VtRtqe1PF0oaBwgP1i1PGmX6Bf8eeKHbQ1ExTTfBKYl5df-1-hd1bjfkQa_Gs0Vy2ch_Eth2CH1RN0vSopNsJWNtk8S8ZYiTu-9j89UqQb1qg7a0UmhC5583UuNoqOKg-7tH5Zw32rjUoe1_3E167J6oqpgPtkkcxoP8vDYfWqMmzdGblhSWANG-74vcItENeidliKIsAH9GEcAntogytlrlEUMDe6v_CAxKcoDL95Jy-qnbpUeSIfruCEG3hxYfuy1knUb_WjWylhkulov-5qnxtPMF-7uJ2BIdyOPtK3dlMt7BC_8qCZ72Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/whitedns/476" target="_blank">📅 13:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-474">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYLJrIBLJOJTITM-0HB32j5Vkop-GnIZ-2Ka1yhumQWpjjJbgKxF7iAvducvrnbjqWbODDo9PnupT0rxJsGPLqr8LPpXvSspz6BaI241c8tROsxlE193ebUZeSAPsuXVo1qwaz2pSWD1EN0RqXyzcA96jojhqwN3h90x7znTWDlWBOu2EfZRNXl3z4tZ4knnJqkOhL1L2StC2y-wZpxt-8gbFB-NvBzJdMYASAEXxDC-xZF1uCN9kcXiXNjdJbrD8Hm5Zsa-Ime3XrXYJ193K-hN2jE0yVnWMHxuGb9Y___16p5QOpgaQXYe5bhv0V_n4I-Mu-6idlJOfjsvyCpfzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/va5KqNnoK7k50dwWWqZEwxoFTTmeufPSKp6-dlJBVUSzG0uPrPN02d1XIoBn2UAox5C-_3fwpaa29avOAcW_W34AjCOPS5rHqf9PGnmpKJ4noPfSPYlOfXBvuIK4ssmBiWPGLjt3iRcfqK2coQ2gC7zEXhrOCmXC4mqw44GTLtJpJGScrDQyFue7JxKmlHt79AWJiGxmCwipFN3VMqP34Z9Pudqo7jTPB3u1_U2_c-5jtAsglmY1AfJ5xBTRkks3HBrWlu93TPxw7RPtIq4I8HiH4gno5FBSH9KTPMFGnCeYuW_j6ensox0GzLcD2zoKY7LTbubVY_Yr6S-DAODYAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">╭────────────────────────────╮
⚡️
WhiteDNS Configs For StormDNS
⚡️
🔐
۱۰ کانفیگ‌های اختصاصی و پرسرعت ╰────────────────────────────╯  01.
🌐
Domain: t1.prs612.us
🔑
Encryption Key: 3e80a0eb3e1fba2bf17e0e0eb5783dc5 ━━━━━━━━━━━━━━━━━━ 02.
🌐
Domain: t2.prs612.us…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/whitedns/474" target="_blank">📅 12:31 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-473">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">╭────────────────────────────╮
⚡️
WhiteDNS Configs For StormDNS
⚡️
🔐
۱۰ کانفیگ‌های اختصاصی و پرسرعت
╰────────────────────────────╯
01.
🌐
Domain:
t1.prs612.us
🔑
Encryption Key:
3e80a0eb3e1fba2bf17e0e0eb5783dc5
━━━━━━━━━━━━━━━━━━
02.
🌐
Domain:
t2.prs612.us
🔑
Encryption Key:
afc1bd5e98cd98cde7515adb7295122b
━━━━━━━━━━━━━━━━━━
03.
🌐
Domain:
t3.prs612.us
🔑
Encryption Key:
8786a860148e2d4d55403ae3c80ba854
━━━━━━━━━━━━━━━━━━
04.
🌐
Domain:
t4.prs612.us
🔑
Encryption Key:
943664f15fd1763e242ce12ba993d9c9
━━━━━━━━━━━━━━━━━━
05.
🌐
Domain:
t5.prs612.us
🔑
Encryption Key:
6a9ab24a8bd3937378efbfb3c23e1358
━━━━━━━━━━━━━━━━━━
06.
🌐
Domain:
t6.prs612.us
🔑
Encryption Key:
71201fedadfbc0b62189c08961bce651
━━━━━━━━━━━━━━━━━━
07.
🌐
Domain:
t7.prs612.us
🔑
Encryption Key:
c4ff91174a79e9e03a4d6727878ada17
━━━━━━━━━━━━━━━━━━
08.
🌐
Domain:
t8.prs612.us
🔑
Encryption Key:
ae5db6f03e485214e1fcc9d26a4c0a2f
━━━━━━━━━━━━━━━━━━
09.
🌐
Domain:
t9.prs612.us
🔑
Encryption Key:
a01c03a340a3e684a2815961e086eb27
━━━━━━━━━━━━━━━━━━
10.
🌐
Domain:
t10.prs612.us
🔑
Encryption Key:
f3a3c5d02bb7ce04f6a4f144fc35e9cb
━━━━━━━━━━━━━━━━━━
11.
🌐
Domain:
t11.prs612.us
🔑
Encryption Key:
e7f2db07e778563d31ed1fc80d5fe612
╭────────────────────────────╮
🚀
Powered By StormDNS + WhiteDNS
📡
Stable • Fast • Secure
Configs by
@PersiaTMChannel
@WhiteDNS
#Servers
╰────────────────────────────╯</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/whitedns/473" target="_blank">📅 12:20 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-472">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuWJzFc0AE09U4g3WcTUT4BlGVcsPI_zd5gPN1W-o6y0X-RbSEZBXNTolmQcrApwvW8KcpeHAaVvf8smx0dnmaXI2IiqYorakJscazkVgc65dpXAJEwV3I_iWGxAjPqtFF6dVxFnoa7ugAEssdTL7WZd5z4Ebn571_AHqkvpdo_ZVAXJX72gobBdO9x9wfKFSqdrzBmhbJRIADgJhuT-cudyjDeVNjzJEBVw8HOLxog9iAD3E3woeBALrInpBOBvmbU1DWzmHLbkuOEPNUZYNKsnqYguhEgMhNUIwgXz5lBfhXEyhPwnZUtEgMb_BiJgSgvwQGK5nH-kMgTJawh7Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteDNS روی گوشی مثل «کلاینت» کار می‌کند و به سرور StormDNS/MasterDNS وصل می‌شود. چون این روش ترافیک را داخل درخواست‌های DNS می‌فرستد، برای اینکه روی اینترنت ضعیف یا پر از قطعی پایدارتر باشد، بعضی پیام‌ها را چند بار می‌فرستد.
Upload Dup = 3 یعنی وقتی گوشی می‌خواهد داده‌ای به سمت اینترنت بفرستد، همان داده در مسیر DNS تقریباً ۳ بار ارسال می‌شود. سرور معمولاً نسخه‌های تکراری را تشخیص می‌دهد و فقط یک بار به مقصد واقعی می‌فرستد، اما حجم اینترنت گوشی قبلاً مصرف شده است.
Download Dup = 7 کمی اسم گمراه‌کننده‌ای دارد. یعنی خود فایل دانلودی لزوماً ۷ بار دانلود نمی‌شود، بلکه پیام‌های کوچک تأیید دریافت دانلود چند بار فرستاده می‌شوند. ولی چون هر پیام DNS جواب هم می‌گیرد، این هم می‌تواند مصرف اضافه ایجاد کند.
نتیجه: این تنظیمات می‌تواند مصرف اینترنت را خیلی بالا نشان بدهد. مخصوصاً با مقدارهای فعلی مثل Upload Dup = 3 و Download Dup = 7 و اندازه بسته‌های خیلی کوچک، داده به قطعات زیاد تقسیم می‌شود و روی هر قطعه هم هزینه اضافی DNS، رمزنگاری و تکرار اضافه حساب می‌آید.
برای مصرف کمتر، معمولاً بهتر است تست کنید با:
Upload Dup = 1
Download Dup = 2 یا 3
اگر پایداری هنوز خوب بود، همین مقادیر مصرف اینترنت را خیلی منطقی‌تر می‌کنند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/whitedns/472" target="_blank">📅 11:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-467">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Beta6-arm64-v8a.apk</div>
  <div class="tg-doc-extra">22.2 MB</div>
</div>
<a href="https://t.me/whitedns/467" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه WhiteDNS Beta6 آماده دانلود است.
ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
لینک دانلود (Universal) :
https://guardnet.ir/f/8f0ef50b3049
رمز فایل:
3666
در این نسخه تمرکز اصلی روی پایداری اتصال و رفع چند مشکل گزارش‌شده بوده:
✅
نسخه اپلیکیشن به 1.0.0-beta6 ارتقا پیدا کرده
✅
قابلیت HTTP Proxy اضافه شده
✅
حالا علاوه بر SOCKS Proxy، می‌توانید از HTTP Proxy هم استفاده کنید
✅
صفحه اتصال حالا درصد پیشرفت را هنگام وصل شدن نشان می‌دهد
✅
هنگام اتصال، وضعیت بررسی Resolverها واضح‌تر نمایش داده می‌شود
✅
بعد از وصل شدن، تعداد Resolverهای فعال و سالم نمایش داده می‌شود
✅
امکان دیدن و کپی کردن Resolverهای فعال اضافه شده
✅
وارد کردن Resolverها بهتر و دقیق‌تر شده
✅
حالا اگر Resolver اشتباه وارد شود، اپلیکیشن بهتر آن را تشخیص می‌دهد
✅
امکان Import کردن لیست Resolver از فایل اضافه شده
✅
5 سرور عمومی جدید به مسیرهای داخلی اضافه شده‌اند
✅
پایداری جابه‌جایی بین Proxy Mode و Full VPN بهتر شده
✅
اگر اپ را ببندید و دوباره باز کنید، وضعیت اتصال فعال بهتر تشخیص داده می‌شود
✅
نوتیفیکیشن اتصال بهتر شده و وضعیت مصرف دیتا را واضح‌تر نشان می‌دهد
✅
هشدار Full VPN حالا قابل بستن است
✅
آیکون اپلیکیشن به‌روزرسانی شده
پیشنهاد ما این است که اگر فقط به تنظیم پروکسی نیاز دارید، همچنان از Proxy Mode استفاده کنید. حالت Full VPN بهتر شده، اما ممکن است روی بعضی دستگاه‌ها یا بعضی شبکه‌ها رفتار متفاوتی داشته باشد.
همچنین اگر سرور StormDNS شخصی دارید، بهتر است از سرورهای خودتان استفاده کنید. فشار زیادی روی سرورهای عمومی WhiteDNS وجود دارد و استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند سرویس عمومی برای بقیه کاربران بهتر کار کند.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
#WhiteDNS
لینک کانال:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/whitedns/467" target="_blank">📅 11:22 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-466">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(سال گودمن)</strong></div>
<div class="tg-text">📣
تمام پروژه های به درد بخور برای دسترسی به
#اینترنت
همراه با یه سری ابزار های دیگه:
💎
پروژه آموزش تانل گوگل به vps
💎
آموزش کامل slip net برای سرور
💎
آموزش متد MHr
💎
آموزش نصب تانل به گوگل(خارج)
💎
آموزش متد Flowdrive
💎
پروژه آپلود داخلی بدون محدودیت
💎
آموزش قابلیت های Mahsang
💎
رادار چک کردن وضعیت اینترنت
💎
پروژه پیام رسان داخلی(شخصی)
💎
اپلیکیشن فیلم و سریال رایگان
💎
پروژه انتقال فایل به اپ داخلی
💎
متود گوگل درایو برای اندروید
💎
متود MHR و بردن پشت کلودفلر
💎
پروژه گوز مشابه MHR پرسرعت تر
💎
جلسه آنلاین با نت داخلی
💎
بالا آوردن کانال های تلگرامی داخلی
💎
آموزش متین برای Mhrv
💎
نسخه جدید اپ vay dns
💎
سایت رایگان فیلم و سریال
💎
پروژه vps شخصی با mhr
💎
اخطار کلودفلر
💎
پروژه تلگرام داخلی
💎
پروژه وایت dns
💎
پروژه های عزیزی
💎
پروژه Mhr روی اندروید
لیست بروز میشود
🍿
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/whitedns/466" target="_blank">📅 10:49 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-465">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
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
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/whitedns/465" target="_blank">📅 10:41 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-464">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(مایلز گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3ssqf3t9JsRgal0suq8xCGfbanmDacSUFgmld87VK-8e-Y6MqaDJzsQFKaXjK_8zhw_MhnJHhP3sGQC1HQ8_autUC3bALJwnmwlPJwmhPatek9x7EZz1XAsmD-J4oT-1eDx_HjpWbknh3qDVX1MAGzSd_j2ExkXot3E8TuRxhzsDOkmrQyYlR4C2mrZ2uZFVk-sA0G0IkwbQIGkiLtgSnskv18vTnhUoSJsp59iwVnSyHudL3hmPC6NNZfElfil6NtF72h1TmcDzIeXrqparUes9mpgn96oiR6TvgSUckwsjtXZ3J7WVgZcfVm9FW_F3hnyhbGK4WY_v5OAcESCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پروژه AzuDL - GC2GD
پروژه AzuDL - GC2GD یک ابزار کاربردی برای دانلود فایل‌ها از طریق Google Colab و ذخیره مستقیم آن‌ها روی Google Drive است.
💡
با این ابزار می‌تونید لینک‌های مختلف رو داخل گوگل کلب اجرا کنید و فایل نهایی رو مستقیم داخل گوگل درایو تحویل بگیرید؛ سپس با متود MHR فایل نهایی رو دریافت کنید.
قابلیت‌های اصلی پروژه:
⚡️
✔️
دانلود لینک مستقیم روی Google Drive
✔️
دانلود ویدیو و پلی‌لیست YouTube
✔️
انتخاب کیفیت ویدیو
✔️
استخراج فایل صوتی MP3
✔️
دانلود Magnet / Torrent
✔️
دانلود چندتایی یا Batch Download
✔️
تشخیص خودکار نوع لینک
✔️
نمایش نوار پیشرفت دانلود
✔️
ذخیره تاریخچه دانلودها
✔️
مدیریت فایل‌های دانلودشده
﻿
🚀
ویدیوی آموزشی پروژه در تلگرام:
https://t.me/luluch_code/22941
🔗
لینک‌های مهم:
🐱
سورس پروژه در GitHub:
https://github.com/TheGreatAzizi/AzuDL-GC2GD
👩‍💻
سورس پروژه در Git سلف‌هاست:
https://git.theazizi.ir/TheAzizi/AzuDL-GC2GD
📌
وبسایت Google Colab:
https://colab.research.google.com
📌
وبسایت Google Drive:
https://drive.google.com
🗣️
اینترنت برای همه، یا هیچ‌کس!
👑
@xsfilterrnet
🗣
@luluch_code
🏠
theazizi.ir</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/464" target="_blank">📅 08:59 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-463">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
سرور استورم دی ان اس (StormDNS)
Domin 1:
te.link-dakheli-app.shop
Domin 2:
s.o4s.shop
Domin 3:
s2.o5s.shop
Key :
TelegramChannel@link_dakheli_app
👾
کلاینت ها :
1️⃣
MasterDNS
|
WhiteDNS
2️⃣
MasterDNS
|
WhiteDNS
اگه وصل شدین ری اکشن برید بدونم
❤️
✉️
Channel |
@link_dakheli_app
| کانال
✉️</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/463" target="_blank">📅 08:27 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-455">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">tele-mirror-win-x64.zip</div>
  <div class="tg-doc-extra">141.6 MB</div>
</div>
<a href="https://t.me/whitedns/455" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📡
معرفی TeleMirror  در شرایطی که دسترسی مستقیم به تلگرام سخت، کند یا حتی مسدود می‌شود، TeleMirror یک راه ساده و قابل‌اعتماد برای مشاهده محتوای کانال‌های تلگرامی فراهم می‌کند.  این ابزار با استفاده از چند روش مختلف برای دور زدن محدودیت‌ها و همچنین منابع جایگزین،…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/whitedns/455" target="_blank">📅 08:00 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-454">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx-Vwx7nz_2451F7anzSYBa_zmGdHl6AOVnaXSpU8dFwyTOV1G3vCaGkWJOQ6Pi8pNXbU-aFJAdVGTwm6uMCPcnwCC15vGRIog0zCN9imSKWZolDnZlNRZtszMDw-kFD9uPf-bXzhNOXcy5n97iqikI3NSMgZvAviMm-V8bIu8aarqfzEDj0Qtb9xbM4FIPk133LIznmP8hPWtarTYMKG3NporCZSN37wahQo_f22hqlyvWGR6715cY_IHo5C2EPKUxi6-c-AFV0WvNg4F92fP83DvQaZFbDzJi9RWc1gvon2pm722B0MsJJIYSq13NKQmhHUmpW1IJ-Xkz8924UJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
معرفی TeleMirror
در شرایطی که دسترسی مستقیم به تلگرام سخت، کند یا حتی مسدود می‌شود، TeleMirror یک راه ساده و قابل‌اعتماد برای مشاهده محتوای کانال‌های تلگرامی فراهم می‌کند.
این ابزار با استفاده از چند روش مختلف برای دور زدن محدودیت‌ها و همچنین منابع جایگزین، کمک می‌کند محتوای کانال‌ها حتی زمانی که اتصال مستقیم به تلگرام ممکن نیست، همچنان در دسترس بماند.
☁
https://github.com/ircfspace/teleMirror
🤩
🤩
🤩
🤩
✨
ویژگی‌ها
👀
بدون نیاز به تلگرام
برای دیدن محتوای کانال‌ها نیازی به نصب اپ رسمی تلگرام نیست.
🔄
دسترسی چندمنبعی
ترکیب دسترسی مستقیم به تلگرام + نسخه پشتیبان JSON روی GitHub برای پایداری بیشتر.
🛡
روش‌های پیشرفته برای عبور از فیلترینگ
استفاده از چند روش Proxy مختلف، حتی روش‌هایی مثل Google Translate برای افزایش شانس دسترسی.
🎨
رابط کاربری تمیز و ساده
طراحی مدرن و مناسب برای خواندن راحت محتوا، بدون شلوغ‌کاری‌های بی‌خود، چون ظاهراً همین اینترنت هم به اندازه کافی اعصاب‌خردکن هست.
💾
کش هوشمند
کاهش تعداد درخواست‌ها، افزایش سرعت لود و تجربه بهتر برای کاربر.
📊
نمایش محتوای کامل‌تر
نمایش پست‌ها همراه با View، پیش‌نمایش Media و اطلاعات کاربردی‌تر.
🌐
پشتیبانی چندزبانه
امکان جابه‌جایی بین فارسی و انگلیسی فقط با یک کلیک.
---
TeleMirror برای زمانی ساخته شده که دسترسی آزاد به اطلاعات تبدیل به یک جنگ روزمره شده؛ ابزاری ساده، سبک و کاربردی برای اینکه محتوای کانال‌ها از دسترس خارج نشود.
☁️
https://github.com/ircfspace/teleMirror
@WhiteDNS</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/454" target="_blank">📅 07:54 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-453">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/whitedns/453" target="_blank">📅 04:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-452">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۵ سرور اهدایی از رسول عزیز به کانال WhiteDNS  StormDNS Server Configs
🇩🇪
Germany Domain: v.eshkaftak.vip Key: 8705eb75abeedcd99001ef8d01cf9fad
♠️
♠️
♠️
♠️
♠️
🇷🇸
Serbia Domain: v3.eshkaftak.vip Key: 8705eb75abeedcd99001ef8d01cf9fad
♠️
♠️
♠️
♠️
♠️
🇹🇷
Turkey Domain:…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/whitedns/452" target="_blank">📅 23:46 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-451">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/whitedns/451" target="_blank">📅 12:48 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-447">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlEYXWT2msgDFH7KomU2JPpjjtjuMI7KxmSfhv7v1oE1IYqZyfZ3RxX1U35H6loL0UOVLTE8AGI9pTy7MZbbV0dl3d0PH3x2HsLHCLGh3kAmu4apjqgCwhcrp1jiaFVYMqTxzigfEH2GmUQxnEjLZWlu1PDibxehgHrZtKtAUVXKPPTPycMxU14PX2VgHTwzBNVoP-wcrqUXhPAzNaHajzgZgcoMiy2hMtAnpl5Zj8EtC4lQbyN0IO5C7cTXcFzOMJysqeXlGI2-GUBViJqot9bBbJ5FjahLEwyYtBm7M6UUDTTy2QOcXS-IuJpEXFJhhF7e2X5rnKaFfy5TtAMJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد ۱۲۵ ریزالور جدید به لیست بات چنل WhiteDNS اضافه شد
برای دسترسی داخل ربات ما بشید و دستور /dns رو اجرا کنید
@dns_resolvers_bot
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/whitedns/447" target="_blank">📅 02:33 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-446">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b225116bd.mp4?token=FUKBDMUmYEKz5Z2nrrBrczheisFyrXwEH-EAJVlnedYU-BlO5JLu58aQl2P5Ng7o4dJI17GSSQmcu6BehSsZ_JrkiAT6XLme1TotarioIFJcvKMV5P8IGwNtW_eb2hMBDanI4fRVc2q_qoclcrxffyM3IE20k0CQZbfENpjI7OnzT3f6-B_IaDEFM_3zUe6QiMid7NOA1VCA8zS40Tf0jCjTt0T5EkIgEbLyJ1BvwwWhIKFR-FCKVVA97SZGebqm1YKSFxuYsrG3UJoUKfAlNTzC92fcwFzYDyB4fdfPZU4-vvYsRLR2eO_kky3K1OA2H9vLZ3lhKOGkEZS_PNr-BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b225116bd.mp4?token=FUKBDMUmYEKz5Z2nrrBrczheisFyrXwEH-EAJVlnedYU-BlO5JLu58aQl2P5Ng7o4dJI17GSSQmcu6BehSsZ_JrkiAT6XLme1TotarioIFJcvKMV5P8IGwNtW_eb2hMBDanI4fRVc2q_qoclcrxffyM3IE20k0CQZbfENpjI7OnzT3f6-B_IaDEFM_3zUe6QiMid7NOA1VCA8zS40Tf0jCjTt0T5EkIgEbLyJ1BvwwWhIKFR-FCKVVA97SZGebqm1YKSFxuYsrG3UJoUKfAlNTzC92fcwFzYDyB4fdfPZU4-vvYsRLR2eO_kky3K1OA2H9vLZ3lhKOGkEZS_PNr-BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش قدم به قدم و نحوه استفاده از اپلیکیشن WhiteDNS
دوستان این سرویس صرفا یک کلاینت برای StormDNS هستش. میتونید از هر کانفیگ استورم دیگه ای استفاده کنید تا وصل بشید.
بعد از اتصال، برای پراکسی کردن روی لینک زیر کلیک کنید
https://t.me/socks?server=127.0.0.1&port=10886&user=&pass=
#WhiteDNS
#Tutorial</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/446" target="_blank">📅 15:40 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-445">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سرور اهدایی از علی عزیز به کانال WhiteDNS
StormDNS Server Configs
Domin :
te.link-dakheli-app.shop
Key :
TelegramChannel@link_dakheli_app
لینک کانال منبع
@link_dakheli_app
#Server
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/445" target="_blank">📅 14:56 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-444">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HExkSBQShpkOcn0pxTJ8pn8qqVsRwOvx8Qe5UYzGQ_TTtcLFbJuKBf9vQ85BoJ2f_BPeRRQvaczBh1xfKvrouphkgLeuuRs0o0Vn1UFbKogJoRGuhAbBWlYGznqd67TLG-heo2BA5BAFO8yLh9ZEp12-fLNMtuZeS4u0P5FWaLWj9WKRPl46xPzLYWaZubhCRYvRPffiCgSCqq4CkUbtea8edq35J31nZ0dEQcNG1rymRjRpGJAeGEs14XxfPJjnYcRY5fEKydy73J84dkBBnvhogQe3iSZgWUAf_hX-76DVlqEP9Qrv9YCE3C0UbS1VJ7avUUWpldzqtytFspXyYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که نگران مصرف بالا هستند، میتونید مقدار های Download Dup  و Upload Dup رو کمتر بکنن.
تغییر این مقادیر امکان داره اتصال شما رو ناپایدار بکنه. بهتره خودتون مقدار هارو تغییر بدید تا جایی که براتون پایدار
متصل بمونه.
توضیحات تکمیلی
👇
👇
👇
👇
"Upload dup" و "Download dup" در زبان غیررسمی شبکه‌های کامپیوتری و نرم‌افزار رایج هستند و معمولاً به وضعیتی اشاره دارند که در آن یک فایل یا بسته داده، به صورت تکراری و غیرمنتظره بارگذاری (Upload) یا بارگیری (Download) می‌شود.
· معنای کلی "dup": مخفف کلمه Duplicate به معنای کپی تکراری یا اضافی است.
· منظور از "Upload Dup": فرآیندی که در آن یک فایل یکسان که قبلاً در سیستم یا سرور وجود دارد، دوباره بارگذاری می‌شود.
· منظور از "Download Dup": فرآیندی که با شروع دانلود، یک کپی اضافی و تکراری از آن فایل به صورت خودکار در جای دیگری از سیستم ایجاد می‌شود.
💡
مفهوم "Upload Dup" (بارگذاری تکراری)
این اصطلاح معمولاً در سیستم‌های مدیریت محتوا یا ذخیره‌سازی ابری دیده می‌شود:
· تشخیص فایل تکراری: زمانی که فایلی را آپلود می‌کنید، سیستم بررسی می‌کند که آیا فایلی با محتوای دقیقاً یکسان (معمولاً با بررسی HASH فایل) قبلاً در سرور وجود دارد یا خیر.
· اطلاع‌رسانی و تصمیم‌گیری: در صورت یافتن فایل مشابه، پیغام "Upload Duplicate" نمایش داده شده و معمولاً گزینه‌هایی مانند ادامه برای آپلود مجدد (Continue) یا رد شدن از آپلود (Skip) به شما داده می‌شود.
· مدیریت سیستم‌های ذخیره‌سازی: برخی سیستم‌ها هم از "Duplicate on Upload" استفاده می‌کنند که به صورت خودکار و پشت‌صحنه یک کپی از محتوای در حال آپلود در یک مقصد ذخیره‌سازی دوم ایجاد می‌کند تا از اطلاعات نسخه پشتیبان تهیه شود.
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/whitedns/444" target="_blank">📅 14:34 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Beta5-x86.apk</div>
  <div class="tg-doc-extra">22.6 MB</div>
</div>
<a href="https://t.me/whitedns/439" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید تستی WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
https://dl.toolschi.com/view.php?f=48c485b41de6bf08.zip
https://guardnet.ir/f/Universal
password : 3666
در این نسخه تمرکز اصلی روی پایداری اتصال و رفع چند مشکل گزارش‌شده بوده:
✅
نسخه اپلیکیشن به 1.0.0-beta5 ارتقا پیدا کرده
✅
مشکل کار نکردن بعضی اپ‌ها یا مرورگرها در حالت Full VPN تا حدی بهبود داده شده . در این ورژن باید بتونید به
x.com
متصل بشید.
✅
مشکل وصل شدن زودهنگام VPN قبل از آماده شدن کامل اتصال برطرف شده
✅
وضعیت اتصال حالا دقیق‌تر نمایش داده می‌شود
✅
مشکل Resolverهای دستی برطرف شده
✅
اگر چند Resolver مثل 1.1.1.1،
8.8.8.8
و
9.9.9.9
وارد کنید، اپلیکیشن باید درست آن‌ها را تشخیص دهد
✅
مشکل پیام اشتباه Resolvers are required to connect در بعضی شرایط برطرف شده
✅
پایداری حالت Full VPN بهتر شده
✅
پایداری Split Tunnel بهتر شده
پیشنهاد ما این است که اگر فقط به تنظیم پروکسی نیاز دارید، همچنان از Proxy Mode استفاده کنید. حالت Full VPN بهتر شده، اما ممکن است روی بعضی دستگاه‌ها یا بعضی شبکه‌ها رفتار متفاوتی داشته باشد.
همچنین اگر سرور StormDNS شخصی دارید، بهتر است از سرورهای خودتان استفاده کنید. فشار زیادی روی سرورهای عمومی WhiteDNS وجود دارد و استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند سرویس عمومی برای بقیه کاربران بهتر کار کند.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
#WhiteDNS
لینک کانال:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/whitedns/439" target="_blank">📅 14:11 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/whitedns/435" target="_blank">📅 13:27 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-432">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">۵ سرور اهدایی از رسول عزیز به کانال WhiteDNS
StormDNS Server Configs
🇩🇪
Germany
Domain:
v.eshkaftak.vip
Key:
8705eb75abeedcd99001ef8d01cf9fad
♠️
♠️
♠️
♠️
♠️
🇷🇸
Serbia
Domain:
v3.eshkaftak.vip
Key:
8705eb75abeedcd99001ef8d01cf9fad
♠️
♠️
♠️
♠️
♠️
🇹🇷
Turkey
Domain:
v4.eshkaftak.vip
Key:
8705eb75abeedcd99001ef8d01cf9fad
♠️
♠️
♠️
♠️
♠️
🇺🇸
USA
Domain:
v5.eshkaftak.vip
Key:
8705eb75abeedcd99001ef8d01cf9fad
♠️
♠️
♠️
♠️
♠️
🇨🇭
Switzerland
Domain:
v6.eshkaftak.vip
Key:
8705eb75abeedcd99001ef8d01cf9fad
#Server
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/whitedns/432" target="_blank">📅 09:33 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-431">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/431" target="_blank">📅 07:16 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-427">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">NekoBox-1.4.2-x86_64.apk</div>
  <div class="tg-doc-extra">15.2 MB</div>
</div>
<a href="https://t.me/whitedns/427" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">https://c224731.parspack.net/c224731/ex/NekoBox_armv8_v1.4.2.apk
Nekobox
#Android
@whitedns</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/whitedns/427" target="_blank">📅 06:25 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-422">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/GPFcIFZyv2IJDZTG0dVscKoHR6wUiSXLZJF0F4eyDEUxy8kGB-fY1cztQ-2Y06ETG0_Wxmu7BFCSfcvt_cB1DOX0U1hvvfnK2Wdmy9QAWbo9_3DYqxLfuVWTiy4-xC2pA4EWtRULijYr9g38D2daxTZ9GiYvmrT-j-38B8Brtxr6Zp6GzVtivIHWWh3xUzlGg8Kd8v6-HhjfJMlanleehXu2HwYVFPAt5YvkxAk1k-lc71tkaF-9ZIte1lbP-CISiQa3KktAImxaHemxiWx9IEhip-HnruVxP0RSKvLWoeGpD0NBBx8-mwJX15EdHOaOyhk3e6bEhl3oY05XBlLyww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/wBMgsXyB8omMdv5HmjdxRZopueqPz4Xn2Hoyh1ZDUe5vJ4HjGPfEKnojjM2CLlz2-iMLf-562JfMijRq7E_1ofy8ya2SrO-h-0R20LhHLgtmTNtVEdfdSEx7JP2Km2buk5N_wgDHAsMn1Mt8VzZnKEoY2LCQ1L9vZteuKlCZqQyUaWIev8TuDH59bqxM5enwVXD30n0QiJYjwnVTvPb6WInc-F_1eU_tlAovaJG6qmMdck95JQu2-74z86qYe2y93xf5a9IVUXyskkPVhs1ZNyNM6aWUyMDTckstDdIMcZ06gGucCiqdJMbkyuVFqJj7rzUNGVPFO_y0CkHEbFncCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/mKogMQqXCxtM7riSclqauGdS5Qpklwv3O7sQDa8fgcLnrNB71BFFVYSz_3Gp1pkk6hs-uabbs1W2ECdkhVcv2vAyt0w90NdrV1yFwy5Pz9XW2n4F-QY0-zLnWBeHxOxCyf0J_m7pDpqzqR_5AsNthIhf6MWimpQvGEr43ItakcaTkj9iasRR6Zits83ku1TBahc656oTrzEhv87UzvbEziJv2F54xFSot8v5cL-nYBTmQoq-hpE5CqM0X6Jq9hJRTYlkWZBOxYNd-_gtXUDynbWW48QUih3CrmladR3965WBpENW3igEVBKuItntv5Uaz9rC57MmRzIq8muECCmCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/SVWQlhNKxtDvIaliPgc4lapMEls1kQDu4x0eVklLDZpCmTVNr7k56xh-CGYuaz0aagdFq2RIt5rKz4oweVvbN2OgGwp0cr-o_bwbMP1OwsgYd3L2Vfy7bNm2R-yxZBvUPlDyNiBdku_lF2j-LwiYrVHhGnHHULtprf6YjpIFbcEjFDS5Dej4rnxa7gSdURLB-pc6pKpCC0dqF5VFMa1YUm6Z6YH0b0VD6NnFOEUIJJMbHa-sZEoCGSH-Eh8JtWlHv45bMJ6JHe_26Oa4HfAffDHkdcXWhFuvWgrN_zpBveqLiA2lFaL30_OwtqsXK2x7Aiy72CXe_qR8SL6j4aZ_Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/WdSoZgV50J9AacUPy85qC9aFmn_jV8CahBhZyS-tjX_8_QM4EjlVgoln-txI892itPECIdApA_gVTDYVq_3JYU9C7-SX4AoPZlYlytBEiGrCUkPBjoNEl97X5sgwbmv3OtORiK5z9k3Xhu8oYj6MwmPz6mnYoaUuNhTG0Q7WdolHAuKPJiEyIDN8yXmFliAdC10afohnzpOzZyLUYpVvekL6TbuYKHSbbIREQviZ1QZGQEnkDxwZNPq5_iI1GWrlCwxhxNSvvBK6LkmABfJSRPhxw2TNq9Lw5-P4O1p7wzkb-mCvumaG7sscH-WAU6eApFNyvLGYEFoBdPSu8OeR0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر به هر دلیلی میخواهید از حالت پراکسی در whitedns استفاده کنید بهترین کار استفاده از اپ نکوباکس هست
https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/tag/1.4.2
#Nekobox
#Proxy
#WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/whitedns/422" target="_blank">📅 06:17 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-421">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">لیست کامل از ۱۳۳ ریزالور که به سرور های WhiteDNS در ۲۴ ساعت گذشته وصل شدن
91.92.214.110
185.88.178.196
2.189.44.68
217.219.162.200
185.53.142.174
2.188.21.58
2.189.44.82
2.189.44.83
2.189.44.86
2.189.44.84
2.189.44.85
2.188.21.70
185.128.82.2
94.182.154.105
2.188.21.46
2.189.44.91
2.188.21.138
2.189.44.90
2.189.44.93
2.189.44.92
2.189.44.94
31.214.169.244
108.162.192.0
172.64.32.0
2.188.21.62
2.189.44.98
173.245.58.0
5.56.132.97
74.63.24.205
5.160.140.16
178.252.143.130
62.60.197.83
2.188.21.130
185.109.61.27
162.159.38.0
74.80.77.245
188.122.68.218
79.175.172.101
217.219.29.66
2.188.21.146
79.127.170.15
79.127.170.12
149.102.250.14
45.135.241.33
44.244.148.52
2.189.44.66
207.211.215.145
2.188.21.78
78.38.77.2
193.178.200.3
194.61.120.143
80.191.163.249
151.232.36.4
185.236.90.12
172.253.228.147
172.253.12.157
31.7.78.205
79.175.172.98
74.80.77.247
172.253.12.216
172.253.13.148
83.212.7.243
172.253.13.153
172.253.12.222
172.253.13.149
172.253.13.156
172.253.12.221
172.253.228.145
172.253.13.146
172.253.228.154
172.253.12.209
172.253.12.153
172.253.13.158
172.253.13.157
74.80.77.246
172.253.13.150
172.253.228.150
172.253.13.155
172.253.12.210
172.253.13.152
172.253.228.148
172.253.228.155
172.253.12.146
172.253.228.152
172.253.12.155
172.253.228.157
172.253.13.145
172.253.228.158
93.118.109.213
172.253.13.151
185.53.141.230
74.63.24.206
216.147.121.35
77.238.123.179
46.164.99.102
185.10.71.13
172.253.12.151
172.253.228.146
172.253.12.215
172.253.228.144
172.253.228.153
172.253.12.145
172.253.12.217
172.253.13.144
46.245.76.162
217.66.203.211
172.253.12.147
172.253.12.212
156.146.33.97
172.253.228.149
172.253.12.149
172.253.13.147
172.253.12.211
172.253.12.150
79.127.211.213
172.253.12.154
172.253.228.156
172.253.12.144
5.160.137.130
172.253.12.158
172.253.12.148
172.253.228.151
172.253.12.220
74.120.14.49
74.63.24.211
74.80.77.244
74.63.24.208
188.122.68.216
216.147.121.181
5.160.227.78
85.185.1.10
172.253.13.154
172.253.12.213
#Resolvers
@WhiteDNS</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/whitedns/421" target="_blank">📅 05:35 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-420">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/420" target="_blank">📅 04:54 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-415">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Beta4-arm64-v8a-debug.apk</div>
  <div class="tg-doc-extra">22.2 MB</div>
</div>
<a href="https://t.me/whitedns/415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید تستی WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
https://guardnet.ir/f/universalb4
https://guardnet.ir/f/arm64-v8a-D4
https://guardnet.ir/f/armeabi-v7a-D4
https://guardnet.ir/f/X86-X64-D4
pass 3666
در این نسخه تمرکز اصلی روی پایداری اتصال، اجرای پس‌زمینه و کنترل بهتر Full VPN بوده:
✅
نسخه اپلیکیشن به 1.0.0-beta4 ارتقا پیدا کرده
✅
قابلیت Split Tunnel برای حالت Full VPN اضافه شده
✅
حالا می‌توانید مشخص کنید VPN برای همه اپ‌ها فعال باشد، فقط برای اپ‌های انتخابی فعال شود، یا بعضی اپ‌ها را از VPN عبور ندهد
✅
بخش انتخاب اپ‌ها برای Split Tunnel اضافه شده و امکان جستجو بین اپ‌های نصب‌شده وجود دارد
✅
سرویس VPN حالا به شکل Foreground Service اجرا می‌شود تا در پس‌زمینه پایدارتر بماند
✅
حالت Proxy Mode هم به سرویس جداگانه منتقل شده و حالا مدیریت بهتری در پس‌زمینه دارد
✅
نوتیفیکیشن دائمی برای VPN و Proxy اضافه شده تا اندروید اتصال را پایدارتر نگه دارد
✅
اگر دسترسی Notification غیرفعال باشد، اپلیکیشن هشدار می‌دهد و کاربر را به تنظیمات مربوطه هدایت می‌کند
✅
در حالت Proxy اگر StormDNS بعد از اجرا متوقف شود، سرویس تلاش می‌کند آن را دوباره راه‌اندازی کند
✅
راه‌اندازی Full VPN پایدارتر شده و StormDNS حالا داخل سرویس VPN مدیریت می‌شود
✅
لاگ‌های خطا و وضعیت اتصال واضح‌تر شده‌اند تا پیدا کردن مشکل راحت‌تر باشد
✅
آمار مصرف دیتا و سرعت اتصال مخصوصا در حالت VPN دقیق‌تر شده
✅
تغییرات Split Tunnel در حالت VPN بهتر مدیریت می‌شود
✅
ظاهر برخی بخش‌ها مثل هشدارها، وضعیت‌ها، رنگ‌بندی انتخاب‌ها و اطلاعات اتصال مرتب‌تر شده
پیشنهاد ما این است که اگر فقط به تنظیم پروکسی نیاز دارید، همچنان از Proxy Mode استفاده کنید. حالت Full VPN برای تست وجود دارد و در این نسخه بهتر شده، اما چون کل ترافیک دستگاه را از تونل عبور می‌دهد ممکن است روی بعضی دستگاه‌ها یا شبکه‌ها سرعت و پایداری متفاوتی داشته باشد.
همچنین اگر سرور StormDNS شخصی دارید، بهتر است از سرورهای خودتان استفاده کنید. فشار زیادی روی سرورهای عمومی WhiteDNS وجود دارد و استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند سرویس عمومی برای بقیه کاربران بهتر کار کند.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
#WhiteDNS
لینک کانال:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/whitedns/415" target="_blank">📅 04:11 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-414">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZMMPsU965fbRFu_JvLHFzl8dg3e-r_rqzNaw1bM_nLVKkXLhFGkqKwiYkMnNZygKWycBfDYVX6eOz6H7h_sodmkZzfHqWIBbf97T_4gTe8MpI_FVoNWGjLrBXK9mjivJ-NF5mPF2fGQIWmlyVtpwyTd-bKix6Y6KIjPbotWj6rJrR5FPy3QwGeZZi8B8vofNQFNGWveWxs06-OO2MtpFTd0nkaFsRNhGWcTdKc9O9EnNgWGUiZK3NYpndrRbDA6qvXdXDtkrpQu4xYpgjavegg8y6xB1gbxxf7D876hXsMxYj5aBmg04-VGMi22VqGGbQ0tosBaMUPInRX2pMcUGmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید Shade قرار گرفت
🙂
- قابلیت exit node از طریق
http://val.town
اضافه شد. الان chatgpt و claude هم باز میشن
- حتما طبق دستورالعمل داخل برنامه، اسکریپت جدید دیپلوی کنید
- تغییرات و بهبود رابط کاربری
این کلاینت برای MacOs است
https://github.com/g3ntrix/Shade/releases/tag/v1.4.0
#WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/whitedns/414" target="_blank">📅 19:15 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-407">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFtpiv816jKZlquHhvW8bQgOcAwZYxa1f3vOjYG9_nrxhvmMigRGrR9XVCckOEDbyUfCnDtkqJl4eyLOoAspK2rIPDYLZv_jJlnGtRwKUu4shsMLXLOBkBz4kq-yY3Bb2eKZLGMmd0dUqEcpfDVogjwuE0EOUkmJY-lk72ATHySPya8jS7iURhF5HrckpZPq546gaWjSm7WeqRCdgb-HGMVbMET6EO_yOaRI4VnJk6WZEutoCyCamAKCZl3Hbj2ll-dh6_5r_ZOry_yUI0tQIEAAgmLz132D4AuyuLDZn7K8sBI7CTidWeYZCrXonxXvSFSJl9bh6vEze4p6fHKA5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IoqQ0bcQqCH7CJW4O68kEnfqokcR69J3Dh0Wt9qGr0D7BwnqnzewtOlxKcApgZ8RAS1X5BmVq8cXkZbFeLlj2iSRUznvDEGxpZ0M01ns0Sl09afZqn5NtHi_la8uKejHTHGgLrGR6m7kdUHuFgQg1NBoozkesPepkE6_FKNVe3iTxPWSBPOjMaZ6tt3ZdrEM61fOL5-MRTAyK419m6ya6XdmNRkaf6QpEdr0-a2fDCQ6-uvUZEWW9yEeUtBWEBIGANN3sSKTT9QsyYb55mH-L1_EFvWAaXTrd3ByqP8d84Om1Q6w59IgAcDzrpc_fGgKIDTvotXx8M_lCAEaWbcLoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAb5d106QZTPFBCjDLygVsznYfIPVyOEsyHnASSreAW6LofIJODB85F3ty9s0PJ6CpG77qVfEIHQeSMZTpfRI1at6XEaqU0xe_175kCyn_crLc9jmnBlg4KzoffT99E-skRmzj0mEXxasmyFm5m6y7FHja3gafHsQyi8g8wgTGUZ7ymY0yHSfEYthzwRky4ykjTawBtkrWZ-cHs-fDItruidiZphfvnTkHCzHKJzku8ZqeaUEEZOkPMNDJq8VrG7cSbUfliYo8cze2LlukVscxcKA4E5cyFEBT4L3KWgA0QANA7nnfBH_qAEc35bYUU5pzBm9aPZxB65fkeBGni5DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYGd-mURh82k5guz9bDh770RznqcCvVcnIWqaf7EkvExn4PCZHZfkcFTtmh1GdVlyjH9WCR3I-gJPzXv5CZSU5ICrl5conjno67z70qxgymiMZ0BVLmqxYLvw_5RgQ2NT1Ro_WMrwSlxSXPPnz7GCD5jGAaftALY6nolaimYi5f9oHn8UMAHGeH5hAh8Njr-RqFUqi1M-y18s4kcC4HHyQFEUgAG3czkZB1EgUqTwXnywaNlr_GTs_ZS-U3PJClbS_BRDlmbzpmLBsLKQeWd4vvdd-5WTnbRNXMHcl5nlp6Bf2-XHmpSjbpldix-mCe-99aDkOJI5B4yYbLz_grVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnGUSYFIZGk3sQyu8VX2op_ISUFG2JaCBA9lAFgWad3yAS86TA__qhpvCThcPQFpwmHF0ye2jRTBgYhiSWwJrGuDVtyaMhHllp8fmlsjhvdj9CqTECqfgDmF7q3gl_MTmiIQC1uPi7-9UNifoz8m7zOROTb29n6hqMDRsHceh2V6KPWewk9iACSaLQV7zB0f-u-qiL3_nezDJbaapJtRp7IHlipaK0_GSIm7SeGl__hYOpGLBu3mZz8F3QkDE0644FGCEhGw4HEze_B5Ca1AKDIKFRrlI4nqSqkGDelzqTIBhQYr90Y374mdqlhqFdd0w2w0E8Sh7V_9x_G8S_vPyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bFL_e_KeHE2mEgXKxTlDI690Ou0_raU8HI4XGQZGzY4NlPcDd8HqsW4uZNPfPbTiZGpVA1nAFjMOjIQiTjJWTGHze3jb8zfJHvboXEAb9ORcci9aPwQZWlLm8QOv9Ylz1cdDfxypHvxUlzsDw063aB4ITOhh4CyWBXZXLqupSKDPJdy-kEYqiJDDfbek2ylgEh_01NGtc8RInazccA5LocH5PAUilrCvOLWnqJX-1byKJj3pxo0JTbyp1e0jsL6_pYeMUmEozGEMc-dQu68AZb0-8UvRNViRJgk8hfej_uMXR7-OFXNWReUNwedYWh1fN87OnopOtRo9U27kXRlZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQYz5rzVJLQr15OFqTGEayUKEmpfujO-VaMq-HjVHQ8C73hlaM49YI818kzr0O-ODQS8D0jM9p5KjDsK15CWUivrY056oD6Y3qbJ-1zWB8hozovJ7LCxMll6uzvbMA5pOzDA-WoUQCpttoc-Li9HWENk_8IoITDem-dui3ahspdcKIHLaOp77wBXYEnBTsT-XaN7hwx7QqLibbSK_ZgGGwGOhRwazxvmArqZXTRrb6s0IVS3o9YReW4w3r7Q54zHRLKZUcIrnFgwVFlBfOa6flB0NeQVUso5LOcuY5qZooHF4Be0rXND6916vtnPFmLvidepzNiLyMaLYlt8wdpDlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همه دوستان
Network Activity روی سرورهای WhiteDNS به‌طور قابل‌توجهی در چند ساعت گذشته بیشتر شده. به نظر می‌رسه تغییراتی که روی سرورها انجام دادیم کمک کرده و تعداد بیشتری از کاربران تونستن کانکت بشن.
در حال حاضر سرورها پایدار هستند، اما اگر امکانش رو دارید، پیشنهاد می‌کنیم سرور شخصی خودتون رو هم کانفیگ کنید. این کار هم فشار روی سرورهای عمومی رو کمتر می‌کنه، هم اتصال پایدارتری برای خودتون می‌سازه.
در روزهای آینده آپدیت جدید اپلیکیشن رو منتشر می‌کنیم تا چند مورد از باگ‌هایی که گزارش شده هم فیکس بشه.
ممنون از همراهی و گزارش‌های خوبتون.
مثل همیشه، لطفاً اگر مشکلی دیدید با جزئیات گزارش کنید تا سریع‌تر بررسی کنیم.
لطفا چنل StormDNS هم دنبال کنید و ازشون حمایت کنید.
https://t.me/nulllroute1970
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/whitedns/407" target="_blank">📅 17:10 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-406">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b225116bd.mp4?token=OLzWctYdxDueuJcgwt6XWHf1raP9wsmlXNugPh_eM-yYjRM-W3F4eYBj5c1N3LKm54P5P6nxvW0GA1Ol_84VzM-Tftg_0eVk5TRVMhGnzoTx8W3lHvVuzuiaFFuqNadmsTPPCbFeYLoQf1XPFc27397dN1xgvhPqUABeroxeq0LNa3pPEg7aTQ8QS5vF-7wwFl-gObBnHPK1pCsKieK-CGy1adR4WNFSboYV7W6bQ0IlJkSXKokmgcQfpsxZMefnsozIucXt-XxwLxoTjmTpZ6FyXrf2dne6p6uMY76MbxdoqJWfZFizlRHsknNeG_9YiTvMQSwKKLrvaGNFmndvqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b225116bd.mp4?token=OLzWctYdxDueuJcgwt6XWHf1raP9wsmlXNugPh_eM-yYjRM-W3F4eYBj5c1N3LKm54P5P6nxvW0GA1Ol_84VzM-Tftg_0eVk5TRVMhGnzoTx8W3lHvVuzuiaFFuqNadmsTPPCbFeYLoQf1XPFc27397dN1xgvhPqUABeroxeq0LNa3pPEg7aTQ8QS5vF-7wwFl-gObBnHPK1pCsKieK-CGy1adR4WNFSboYV7W6bQ0IlJkSXKokmgcQfpsxZMefnsozIucXt-XxwLxoTjmTpZ6FyXrf2dne6p6uMY76MbxdoqJWfZFizlRHsknNeG_9YiTvMQSwKKLrvaGNFmndvqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش قدم به قدم و نحوه استفاده از اپلیکیشن WhiteDNS
دوستان این سرویس صرفا یک کلاینت برای StormDNS هستش. میتونید از هر کانفیگ استورم دیگه ای استفاده کنید تا وصل بشید.
بعد از اتصال، برای پراکسی کردن روی لینک زیر کلیک کنید
https://t.me/socks?server=127.0.0.1&port=10886&user=&pass=
#WhiteDNS
#Tutorial</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/whitedns/406" target="_blank">📅 12:50 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-405">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/405" target="_blank">📅 11:46 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-404">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستانی که امکان ساخت سرور دارن لطفا StormDNS رو دریابن
کانفیگ این سرور ها برای بچه های ایران امکان پذیر نیست هم از نظر هزینه هم دسترسی
اما کانفیگ کردن این ها برای شما فقط ماهی ۵دلار هزینه داره
با یک سرور شما شاید ۱۰۰ ها نفر به راحتی میتونن وصل بشن
اگر از نظر فنی اطلاعات کافی ندارید میتونید از پروژه گیتاب StormDNS آموزش رو دنبال کنید
https://github.com/nullroute1970/StormDNS
لینک چنل StormDNS
https://t.me/nulllroute1970</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/404" target="_blank">📅 10:30 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-403">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLzVGabRbKYhgUF3ao4Ez0uW6W2qP9RcOfg0aCFabH_1mKxQau00LygdoS_xf4V15lGE-ybuiB90yEk6u3JaobnuoFvBbgGXBNjEIz_bEoLzSEyUnrKV19H5_rSxGVcRjXo23BZfvF-IA15WSAYohajatn3vvUp-95l34OxbBkh7F4YlZcAUkr9eOhqyMDthjWqQdiPezkLFKr46BIL9DCi5jyDuxK_nz7IkIG661xnD8BMwFjASGyuiguRS3iBYrxd5UgrjeBMSVkXpGEpOK8PyTK7TqriQzmwMxknKD-q66euRkRCwG9uTBNLZLuWv5WzJrfrfPirxZIB78C26jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیکس برتای پنهان شدن منو زیر نوار سفید اندروید هستش</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/whitedns/403" target="_blank">📅 10:26 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-398">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a.apk</div>
  <div class="tg-doc-extra">22.1 MB</div>
</div>
<a href="https://t.me/whitedns/398" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
دوستانی که مشکل کاور شدن منو زیر منوی اصلی اندروید رو داشتن، میتونید از این ورژن استفاده کنید.
همچنین نسخه منسب برای cpu های مختلف اضافه کردیم.
⚠️
اگر مشکلی با منو نداشتید، نیازی به دانلود و آپدیت به این نسخه ها ندارید.
اپلود شد ورژن یونیورسال
https://uploadb.com/rtfjbrhh1dml/Beta.zip.html
پسورد زیپ : iran
لینک کمکی
https://punkpaste.ir/f/app-universal-a55ax7
لینک کمکی
https://guardnet.ir/f/arm64-v8a
https://guardnet.ir/f/universal
https://guardnet.ir/f/armeabi-v7a
https://guardnet.ir/f/x86-x64
https://guardnet.ir/f/beta3-debug
password : 3666
@WhiteDNS
#WhiteDNS</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/whitedns/398" target="_blank">📅 10:25 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-395">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKB0ae_M7IwfW-OFGcskUqoMWK7fVxw0dbJgAcsWC9K2xRBdrIHZGAvrXr4-KsAryh6m5DIAjPjUoEEi8AagEo0gDUKJbLkj1zLHU5UVTXeh2FqhkfbCWv_qLeHJ03EwjJKD9m2f4j6o_SHYRe_Y1ycidiOrQKwdwNV3QjE3ka7lUJPAWyw1ViBZmL3LocSoDPHNS60Bmo9zghRinNFUKRFyqWDvQ2RuWeHvHwo3stfKUJIOUaQibOxVFtAnlrJ4-2i3OYw_wTN8ulxhPA7EybQCL7uHzyKcNQ61YjynHkey2t-xcjwMiHwNT7x2Fkd-SkLrBTdetudY7jhMvDwDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRE_icaNJtEKTQaZUXe43SV1IIlxiOLpwzf7dvpIbWKtDNXuIwuacFOuDAE9z8qAv36cCX8a27gjBZ7ZRIrCvOFEz8P4n9pwIK8e-9QRtADYmqeMrqQPW2z-KmbogWMAZj-Pu7Bp4rw4kuJufDGhC93iM1EjdAPbi-lpQPJFNwvxTRiTWgsL5vfDfhFNFUYHLNViALQ4b8WVJlZqgWL25-yS22T6qPM3vC0HQJrtFIcL1vhrG-3iac_GVyO3eYYgS6yFMSROhTtAe5ZuME-i1CwM-S0nzTeASMD56iZVY4FqScK-RzXALWDrazjR69nZg4vaJ4fODYpR6bvFKjUfyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید تستی WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
دانلود سرور داخلی
https://uplod.ir/9iei532m163a/WHD-B3.zip.htm
https://dl.toolschi.com/view.php?f=5bc735f5b4753205.zip
رمز فایل 3666
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
https://t.me/whitedns
#WhiteDNS</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/whitedns/395" target="_blank">📅 09:31 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-394">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJzJm2GirveobdifulgcahykNWh8TwEQgrDjDSRtcCEUevTwED6zO5O5SlXPflXjeXvxplRxZR6nqxclmn72hw6VTOIBNZTEVu89rU8oC4k0l4TqRJiY5pcyFKOzdqhJdvEwh3_cWiYs2H1sUKE5h3OXQx5p572NQnodKLLkZqIYRVIfBVot4XRS1gIZKsMvNaX1ku0b-THQYc4jYrkFaHeQQoivBHnzRSOKcU3XYqVoGK2A_ZY-XWKDYSHlfk4_DpouNOlfKioNvHvq3AoRQuDbAojq5DyMqRB5qpBBMNcBZem5-5m7nsyCGPNJTC-9kVfi8RP_dILuPWzKVyBQsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ سرور اختصاصی وایت دی‌ان‌اس برای StormDNS
domain:
v.whitedns1.shop
EncryptionKey:
c8328f9d541860df1637b9b3ed7b990e
domain:
v.whitedns2.shop
EncryptionKey:
7ecd7b6271c47e348f6ab177517ee8fa
domain:
v.whitedns3.shop
EncryptionKey:
9d7aedcaf1f94e784a24fdfc1348a337
domain:
v.whitedns4.shop
EncryptionKey:
0ce14ab71acebbd46b8129e25593155a
domain:
v.whitedns5.shop
EncryptionKey:
2dffd162cb02b278c1ab57ee17fe07ae
domain:
v.whitedns6.shop
EncryptionKey:
e32afdaa30ca36ead696cd90d84ced15
domain:
v.whitedns7.shop
EncryptionKey:
6394eec942238533798ec7524eb7ea66
domain:
v.whitedns8.shop
EncryptionKey:
1c167e9850936655c480e4938b2c5c35
آموزش اتصال با پی‌سی
https://t.me/whitedns/383
همچنین میتونید از اپلیکیشن WhiteDNS استفاده کنید تا وصل بشید.
@whiteDNS</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/whitedns/394" target="_blank">📅 16:50 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-393">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">WhiteDNS-Beta2.apk</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/whitedns/393" target="_blank">📅 16:21 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-392">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Beta2.apk</div>
  <div class="tg-doc-extra">22 MB</div>
</div>
<a href="https://t.me/whitedns/392" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
ممنون از همه کسانی که نسخه تست WhiteDNS رو نصب کردند، تست گرفتند و با فیدبک‌هاشون کمک کردند باگ‌ها رو سریع‌تر پیدا و رفع کنیم.
دانلود سرور داخلی
https://kalbodteam.ir/free/file/Z0YF19
https://dl.toolschi.com/view.php?f=21c0a01f957ec510.zip
در نسخه جدید
1.0.0-beta2
چند تغییر مهم اعمال شده:
✅
تست کانکشن بعد از اتصال حذف شد.
توجه کنید ممکنه اتصال برقرار بشه، اما به‌خاطر MTU نامناسب یا Resolver ضعیف، سرعت خیلی پایین باشه یا بعضی سایت‌ها لود نشن.
✅
گزینه Load Default Resolver حذف شد.
این روش بیشتر از اینکه کمک‌کننده باشه، باعث فشار اضافی روی سرور و اختلال در تست‌ها می‌شد.
✅
امکان استفاده از سرور شخصی StormDNS اضافه شد.
از بخش Advanced Settings می‌تونید دامنه، کلید و تنظیمات سرور StormDNS خودتون رو وارد کنید و از کلاینت برای سرورهای شخصی هم استفاده کنید.
✅
مشکل قطع نشدن VPN سیستم برطرف شد.
وقتی داخل اپلیکیشن Disconnect می‌زنید، VPN اندروید هم به‌درستی قطع میشه.
⚠️
این نسخه همچنان نسخه تست اولیه است. هیچ اصراری برای استفاده از این روش وجود نداره؛ فقط اگر تمایل دارید، می‌تونید با تست کردن و ارسال فیدبک به بهتر شدن پروژه کمک کنید.
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/whitedns/392" target="_blank">📅 16:00 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-391">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هرکسی وصل شد لطفا خبر بده. نتیجه این تست خیلی برای ما مهم هستن.
اگر هم نشد، پایین اپلیکیشن ثسمت لاگ هستش. میتونید کپی کنید و برای ما بفرستید.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/whitedns/391" target="_blank">📅 14:05 · 13 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
