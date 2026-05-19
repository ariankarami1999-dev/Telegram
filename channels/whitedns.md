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
<img src="https://cdn4.telesco.pe/file/oxde45B-GIp3IKApKEqMscdSAKmb8zIhOwMh0O8MJKuhZp2IohubCzxm4ykEQsnD3ibtMh2x1_KBN7soLdMU4dn42jjcc1Bd16jpmLjsyDx-xK9u8HMIUxlvupm-uTgwpNeIDJiTTkSp8T1iY2v1K6eh65_Yp4fBPqwZCYAMwkRia_VKdC_I8kaN8YFsbZ_58JLBTDCQ18ic7GW9hoS2uMepe0Qe-HNbEyTrlpKR0gMZsTxp54R1PzAdoBHAuBRzsZUnwjaUXkjdneIvxW3e2DaOud_nCgl6cl2yEX5qS3ozwc7dkddS5av67YCtQRm6gkFUzxmGB8GzHNfn4NYpxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 80.8K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 06:57:32</div>
<hr>

<div class="tg-post" id="msg-701">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-poll">
<h4>📊 با اپلیکیشن های ما تونستید به اینترنت متصل بشید؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/whitedns/701" target="_blank">📅 05:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-700">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
پروفایل های وایت دی ان اس (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲۸ اردیبهشت
👾
لینک دانلود
کلاینت :
1️⃣
WhiteDNS
1.5.0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygxKSIsInNlcnZlciI6eyJkb21haW4iOiJ2MS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygyKSIsInNlcnZlciI6eyJkb21haW4iOiJ2Mi5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygzKSIsInNlcnZlciI6eyJkb21haW4iOiJ2My5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg0KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NC5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg1KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg2KSIsInNlcnZlciI6eyJkb21haW4iOiJ2Ni5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg3KSIsInNlcnZlciI6eyJkb21haW4iOiJ2Ny5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg4KSIsInNlcnZlciI6eyJkb21haW4iOiJ2OC5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg5KSIsInNlcnZlciI6eyJkb21haW4iOiJ2OS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygxMCkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEwLm1hc2lyLXNlZmlkLm15IiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
⚡️
پک ریزالور
👍
تنظیمات مخصوص وایت دی ان اس
⬅️
نحوه ی اضافه کردن پروفایل ها
⬅️
فیلم اموزش وایت دی ان اس
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
(پیشنهادی)
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/700" target="_blank">📅 20:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-699">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/699" target="_blank">📅 18:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-698">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">راهنمای_جامع_استفاده_از_وایت_دی_ان_اس_ویندوز_.docx</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/whitedns/698" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
راهنمای جامع وایت دی‌ان‌اس (WhiteDns) برای ویندوز منتشر شد!
🚀
کاربران عزیز، اگر برای اتصال و تنظیم برنامه WhiteDns در ویندوز با چالشی مواجه هستید، این راهنمای کامل دقیقا برای شما آماده شده است. برنامه WhiteDns یک ابزار قدرتمند دسکتاپ برای تونلینگ و ساخت پروکسی محلی است و با استفاده از این راهنما می‌توانید بالاترین سرعت و پایداری را تجربه کنید.
📌
خلاصه‌ای از آنچه در این راهنما یاد می‌گیرید:
🔹
شروع سریع و آسان:
آموزش قدم‌به‌قدم ایجاد پروفایل، وارد کردن دامنه، کلید رمزنگاری (Encryption Key) و اتصال اولیه.
🔹
انتخاب حالت پروکسی:
تفاوت بین حالت دستی (SOCKS5 only) و اعمال پروکسی روی کل سیستم (System proxy) برای مرورگرها.
🔹
ابزار قدرتمند اسکنر (Resolvers):
آموزش پیدا کردن سریع‌ترین و پایدارترین تحلیلگرهای DNS با استفاده از اسکنر داخلی برنامه (در حالت‌های سریع، عمیق و با دقت بالا).
🔹
تنظیمات پیشرفته و موتورها:
معرفی تفاوت‌های موتور MasterDNS و StormDNS و نحوه استفاده از پروفایل‌های آماده (Presets) مانند
Stable Iran
(برای بالاترین پایداری در شبکه‌های محدود) تا حالت‌های تهاجمی‌تر (Aggressive).
🔹
تنظیمات مخصوص برنامه‌ها:
راهنمای دقیق ست کردن پروکسی محلی (
127.0.0.1:18000
) روی تلگرام دسکتاپ، فایرفاکس، کروم و مرورگر اج.
🔹
رفع مشکلات (Troubleshooting):
راهکارهای عملی برای حل مشکلاتی مثل وصل نشدن مرورگر با وجود اتصال برنامه، قطع شدن مداوم، و یا رفع گیر کردن روی راه‌اندازی کند تونل.
💡
فرمول طلایی اتصال:
بهترین و امن‌ترین مسیر برای اکثر کاربران این است: وارد کردن اطلاعات تونل
⬅️
اسکن تحلیلگرها
⬅️
اعمال بهترین تحلیلگر
⬅️
انتخاب حالت Stable Iran
⬅️
اتصال!
برای استفاده حرفه‌ای از این نرم‌افزار و دور زدن قطعی‌ها، حتماً فایل راهنمای کامل را مطالعه کنید.
#اموزش_ویندوز_whitedns
@whitedns</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/whitedns/698" target="_blank">📅 18:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-697">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">11 MB</div>
</div>
<a href="https://t.me/whitedns/697" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تغییرات WhiteDns ویندوز نسخه 1.0.5
بازسازی رابط مدرن
بهبود جزئیات کوچک رابط کاربری و تراز کارت‌ها برای ظاهری تمیزتر و یکدست‌تر در دسکتاپ.
🖥
✨
اسکنر با دقت بالا :
یک اسکنر با دقت بالا برای شرایط سخت اضافه شد
طراحی شمارنده رزولور بهبود یافته
به‌روزرسانی استایل شمارنده رزولور تا با چیدمان کارت‌های اطراف هماهنگ‌تر شده و ظاهری مدرن‌تر داشته باشد.
🎨
پشتیبانی از سینی ویندوز بهبود یافته
رفتار سینی برنامه به‌روزرسانی شد تا در ویندوز طبیعی‌تر احساس شود و در پس‌زمینه در دسترس بماند.
🪟
🔌
فعالیت شبکه برای حالت SOCKS5 اصلاح شد
فعالیت شبکه اکنون ترافیک را زمانی که برنامه‌ها از پروکسی محلی SOCKS5 استفاده می‌کنند، ردیابی می‌کند، به جای نمایش فعالیت فقط از طریق مسیر HTTP/System Proxy.
🌐
🔍
سازگاری پورت SOCKS سفارشی
فعالیت شبکه اکنون هنگام تغییر پورت SOCKS در تب پیشرفته نیز به کار خود ادامه می‌دهد.
⚙️
حافظه اسکن رزولور اضافه شد
برنامه اکنون بهترین نتیجه اسکن رزولور را به خاطر می‌سپارد و اسکن‌های کامل تکراری را هنگام اتصال مجدد با مجموعه رزولور یکسان کاهش می‌دهد.
💾
🚀
تجربه اتصال مجدد سریع‌تر
اتصالات مجدد باید روان‌تر احساس شوند زیرا برنامه از اسکن مجدد غیرضروری رزولورها هنگام در دسترس بودن نتیجه معتبر قبلی خودداری می‌کند.
⚡️
وارد کردن دستی رزولور اضافه شد
گزینه وارد کردن .txt در کارت «وارد کردن / رزولورهای دستی» برای بارگذاری آسان‌تر لیست رزولورها اضافه شد.
📥
📝
نکات اتصال
از لیست رزولور باکیفیت و کوچک‌تر برای راه‌اندازی سریع‌تر استفاده کنید.
🚀
رزولورهای پایدارتر را در بالای لیست نگه دارید.
📌
هنگام آزمایش اتصال، ابتدا از حالت SOCKS5 استفاده کنید.
🧪
اگر حالت System Proxy با یک برنامه ناسازگار است، آن برنامه را به‌صورت دستی برای استفاده از
127.0.0.1
و پورت SOCKS نمایش داده شده در WhiteDns پیکربندی کنید.
⚙️
مگر در صورت نیاز، از تغییر مقادیر تونل پیشرفته خودداری کنید؛ مقادیر پیش‌فرض معمولاً پایدارترین هستند.
🛡
@whitedns</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/whitedns/697" target="_blank">📅 18:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-696">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">برای اشتراک‌گذاری اتصال
WhiteDNS
روی وای‌فای با دستگاه‌های دیگر، کافی است داخل بخش تنظیمات، مقدار
Proxy Address
را از:
127.0.0.1
به این مقدار تغییر دهید:
0.0.0.0
بعد از انجام این تغییر، در بخش
Connection Info
یک آدرس IP جدید به شما نمایش داده می‌شود. از همان IP می‌توانید برای تنظیم پروکسی روی دستگاه‌های دیگری که به همان شبکه وای‌فای متصل هستند استفاده کنید.
لطفاً دقت کنید که برای اتصال دستگاه‌های دیگر، نباید از
127.0.0.1
استفاده کنید. باید حتماً از آدرس IP جدیدی که داخل
Connection Info
نمایش داده می‌شود استفاده شود.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/696" target="_blank">📅 18:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-695">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پروژه‌ی TheFeed که متعلق به Sarto هست و قبلا درموردش حرف زدیم برای ios هم عرضه شد! میتونید با نصب برنامه‌ی Testflight در Appstore و رفتن به لینک زیر برنامه رو دانلود کنید:
https://testflight.apple.com/join/J6bfxDdZ
لینک کانال TheFeed
@WhiteDNS</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/whitedns/695" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-694">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجاوید نامان ایران(Bamdad)</strong></div>
<div class="tg-text">کانفیگ برای کلاینتهای وایت دی ان اس  بر روی اندروید، آی او اس، مک اوس، ویندوز و لینوکس
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDIiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5iYW1hay54eXoiLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDMiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5pcmRtYy5jb20iLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDQiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5qbmlyLm15IiwiZW5jcnlwdGlvbl9rZXkiOiJhYWY0YjYtQEphdmlkbmFtYW5JcmFuLWFhZjRiNmZmZiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5pZ29paS5vcmciLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDYiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5qYXZpZG5hbWFuLmNvbSIsImVuY3J5cHRpb25fa2V5IjoiYWFmNGI2LUBKYXZpZG5hbWFuSXJhbi1hYWY0YjZmZmYiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDEiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5uYW1hZC54eXoiLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/694" target="_blank">📅 16:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-693">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه تشکر از کانال
https://t.me/Masir_Sefid
این دوستان عزیز از روز های اول شروع کردن به آموزش، تنظیمات و اشتراک گذاری سرور های رایگان برای اتصال رایگان.
اگر دوست دارید عضو چنلشون بشید و از آموزش، سرور و تنظیماتی که میذارن استفاده کنید.
ممنون از همه دوستانی که برای اتصال رایگان هموطن هامون تلاش میکنن
🫡
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/693" target="_blank">📅 15:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-692">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">لیست ۱۰۰ ریزالور با بیشترین درخواست ها به سرور های WhiteDNS
185.94.98.34
185.142.158.162
5.160.128.142
2.189.44.68
93.115.127.9
109.230.89.90
217.219.162.200
94.232.173.28
134.255.206.205
80.75.7.2
185.208.174.167
185.37.55.30
185.51.201.58
185.53.142.174
185.255.91.60
185.88.178.196
164.138.17.122
78.157.41.60
5.202.252.30
31.214.169.244
185.109.61.27
2.188.21.58
185.213.11.85
178.252.128.66
2.188.21.70
185.105.101.1
2.189.44.98
109.107.159.86
77.238.123.179
2.188.21.46
172.64.32.0
173.245.58.0
151.232.36.4
108.162.192.0
185.208.175.228
185.137.25.146
185.208.183.29
207.211.215.145
185.50.37.52
2.188.21.138
109.230.206.175
2.189.44.14
85.185.1.10
46.32.31.30
109.72.197.1
2.189.44.84
2.189.44.82
80.191.163.249
2.189.44.86
2.189.44.83
2.189.44.85
78.39.234.140
85.185.157.181
37.191.95.70
185.191.79.210
185.141.105.139
74.80.77.247
78.38.174.2
74.63.24.210
74.63.24.211
2.189.44.93
185.53.141.230
2.189.44.94
74.80.77.246
2.189.44.91
2.189.44.92
2.189.44.90
2.188.21.146
172.253.228.147
74.63.24.205
172.253.12.151
172.253.12.155
172.253.228.150
172.253.228.145
172.253.12.16
172.253.13.147
172.253.13.146
172.253.13.156
172.253.13.154
172.253.13.152
172.253.13.149
172.253.228.156
78.38.114.66
172.253.12.221
172.253.12.150
172.253.13.157
172.253.12.154
172.253.12.210
172.253.13.145
172.253.13.148
172.253.12.212
172.253.13.151
172.253.12.216
172.253.228.148
@WhiteDNS</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/whitedns/692" target="_blank">📅 15:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-691">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">WhiteDNS-1.5.0-x86.apk</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/whitedns/691" target="_blank">📅 13:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-690">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوستانی که تازه اضافه شدید، سوال دارید یا نمی‌دونید چطوری از WhiteDNS استفاده کنید، تمام مراحل زو اینجا براتون توضیح دادیم
https://t.me/whitedns_group/32380/32404</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/whitedns/690" target="_blank">📅 13:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-685">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/whitedns/685" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر از مطمین نیستید، ورژن یونیورسال رو دانلود بکنید.</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/whitedns/685" target="_blank">📅 13:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-683">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/As79DEvSJWib6ZIGme13M0KR9vV5hoBNNH3OtrJGN2JNhhkVkSJQ0w5-Pd8QY9zph5fqsu8n9bn6SpHwyAehgTtbMbnIhr0Dd4VLCfp8VfKNwYCvD9UK87ckvxxD-5Ky6FPdlKAjdaNgIlElSWDuYv-6dipQ4uUjhMf9n0zd74ZTqqcMGQucvk6D6vostyDAmyV6IZmW0A5j_A91g3MgNks8Z6un1Lr02AWdEBecOzfO0wdyp7C5o-QH7mi7wuxnWW4zm0-I5Wzeriu50zfZztBWIY5e62cuvP_thvKbt0Z_BO5n5WdlN7of3H-zi_ntJ6KBujCAi55i5WqJc4P1hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FoquJXcxJL_LN6zpNmui1EeRS0gOH_gGaHExE7AJwgdjOYMSXPoeozSI8svLK6NkgXdN5Vo1SLHCLlMLRr-JI5BjoEFeMrX9FbTSMs0CP2eqhZVCzHE5yJMhayRyxZl_1fXhWTk0LVSJkW4z9kJQnU2BuXHauhnyrmCYCUV49Qhv9ALzOlVQXpu3ACM9E2h04c_dcKb9iy7JHAJ-mdSY36EsdZYIu82DXzvOpi5IyFg3fKR4gg1oWKmhmd2DUX6cN7hjLEGVt0z_fx848J6kPT7GZwkLRvMsO2C1vvzKAdyqIQh4zHYy5MUfLYh6Tz55VJnT6pI_wk0k24ZogJLsgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام خدمت همراهان عزیز،
تمرکز در این نسخه روی زبان فارسی، دسترسی پذیری برای افراد با مشکلات بینایی، تست گروهی سرور ها و خروجی از ریزالور ها بوده.
✅
نسخه اپلیکیشن به 1.5.0 ارتقا پیدا کرده
✅
تست سرورها اضافه شده و می‌توانید سرعت، Ping و وضعیت سلامت همه سرورها یا هر سرور جداگانه را بررسی کنید
✅
نتیجه تست کنار هر پروفایل سرور نمایش داده می‌شود تا تشخیص سرورهای بهتر یا مشکل‌دار راحت‌تر باشد
✅
زبان فارسی به اپ اضافه شده و می‌توانید از داخل تنظیمات بین فارسی و انگلیسی جابه‌جا شوید
✅
چیدمان فارسی راست‌به‌چپ شده و فونت Vazirmatn برای خوانایی بهتر اضافه شده
✅
بخش‌های اصلی اپ مثل اتصال، پروفایل‌ها، اسکن، لاگ‌ها و تنظیمات فارسی‌سازی شده‌اند
✅
دسترس‌پذیری اپ برای TalkBack و صفحه‌خوان‌ها بهتر شده و دکمه‌ها، تب‌ها، اسلایدرها و کارت‌ها توضیح واضح‌تری دارند
✅
وارد کردن پروفایل با QR راحت‌تر شده
✅
خروجی گرفتن همه Resolverهای ذخیره‌شده در یک فایل اضافه شده و Resolverهای تکراری حذف می‌شوند
✅
تنظیمات Parallel Test مرتب‌تر شده و تنظیمات پایدار به‌صورت پیش‌فرض استفاده می‌شوند
✅
تنظیمات تهاجمی‌تر Parallel Test جدا شده‌اند و فقط در صورت فعال کردن استفاده می‌شوند
✅
نتیجه اسکن Resolver پایدارتر بروزرسانی می‌شود و پروفایل Scanner Result فقط بعد از پایان اسکن تغییر می‌کند
✅
پروفایل Default Resolver دیگر اشتباهی به‌عنوان پروفایل دستی ذخیره نمی‌شود
✅
وضعیت تست سرورها هنگام قطع اتصال یا خطا بهتر پاک می‌شود
ممنون از دانی عزیز برای تغییرات مربوط به زبان و دسترسی پذیری
❤️
در این ورژن تنظیمات جدیدی برای تست موازی MTU اضافه شده. دوستان عزیز که ابتدا مشکل داغ شدن گوشی موبایل داشتن، این گزینه رو بیارن پایینتر. مقدار حدود ۳۰ میتونه خوب باشه. اگر همچنان این مشکل رو داشتید مقدار های کمتر رو امتحان کنید.
همنین دوستانی که گوشی های مدل بالاتر دارند، میتونند مقدار های بالاتر رو تست کنند.
@WhiteDNS</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/whitedns/683" target="_blank">📅 13:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-682">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BxwT9cqfvWq3Zbt9NNulOfGj9H76aHxAGeHBfo0VN2LKzUAUHMMnSxkISSUJWL25T9R4mGfQb05gGCzDsZ1SUnxC5IjFz0-ayEAJeoPndId-Dwzm1N_1uaOxP-1CNcQmIiuPI17AzJzKZMD5HBNte3gWeVvqEnxAWmU0C2g-HJdz_D0eJx7IaF_3Zejlel0DTp9CLtRsT6nW08E14m_dJvMRPTGbydKDyAWuxAyDCCXMPzgWlZfZBNA1E90xzGDS3b1cR-u5y2MgY_1-fhxbEiRZz6Dt6kY4k1WYCqaSZALtkrRVRx6dal__GscJxHeWb0YFYEbj0Tl6UcxKswWTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ اندروید
#چشم_عقاب
نه فقط یه خبرخوان، بلکه یه راه آفلاین برای دسترسی آزاد به اطلاعاته، که بدون اینترنت، بدون VPN و حتی بدون داشتن مجوز اینترنت روی گوشی، خبرها و اطلاعات رو مستقیما از ماهواره روی دستگاه شما میاره.
کافیه کانالش رو روی فرکانس 10762/27500V ماهواره ترکمن‌عالم باز کنین و دوربین گوشی رو سمت کدهای QR که روی صفحه نمایش داده میشن بگیرید، تا اپ در چند ثانیه اطلاعات رو بخونه و روی گوشی ذخیره کنه.
اپ فقط به دوربین دسترسی داره تا QR Codeها رو اسکن کنه و هیچ عکس یا ویدئویی ذخیره یا ارسال نمی‌کنه. تمام محتواهایی که دریافت می‌کنین، قبل از پخش با امضای رمزنگاری‌شده Ed25519 تأیید میشن تا اپ فقط اطلاعات واقعی و معتبر رو قبول کنه.
👉
play.google.com/store/apps/details?id=com.filtershekanha.cheshmoghab
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/682" target="_blank">📅 12:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-681">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from3rf4n vpn(3rf4n)</strong></div>
<div class="tg-text">سرور white dns متصل چنل
✅
Domain :
v.phtv1.lol
Key :
2ff051858125055a6999b91c515d19ef
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQHp5cGhlcnZwbnNhbGxlIiwic2VydmVyIjp7ImRvbWFpbiI6InYucGh0djEubG9sIiwiZW5jcnlwdGlvbl9rZXkiOiIyZmYwNTE4NTgxMjUwNTVhNjk5OWI5MWM1MTVkMTllZiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/681" target="_blank">📅 10:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-680">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
سرور وایت دی ان اس (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲۸ اردیبهشت
Domin Vip :
vip.masir-sefid.my
Domin 1:
v1.masir-sefid.my
Domin 2:
v2.masir-sefid.my
Domin 3:
v3.masir-sefid.my
Domin 4:
v4.masir-sefid.my
Domin 5:
v5.masir-sefid.my
Key :
Telegram-Channel--->@Masir_Sefid
👾
لینک دانلود
کلاینت :
1️⃣
WhiteDNS
1.4.0
1️⃣
WhiteDNS
(Windows)
1.0.5
⚡️
پک ریزالور
⬅️
فیلم اموزش وایت دی ان اس
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
(پیشنهادی)
اگه وصل شدین ری اکشن برید بدونم
❤️
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/680" target="_blank">📅 09:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-679">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=vzejRIu7K1KsNLRpDKWawAUKksyNMiw9522RaJXlTFgldkDaz_ijP1zaDSh9P5exBZ7WJKyp4Uvr7oXrrtoiG_nfLh9SVapZ0_slbbYyaP_kZTObiKaleYVCoPgv8p3P-QnqpdNGQVGSzaesdnn-uCwgyEJRvdJugoRL4E5lKcadaXBKBDcFhaTEsliqTrFC9OfK2INJClTRK170aHBo16JFu8fldifrfOofHCRDbljRjl9zSwCKmWJJNUjdK60xJnuESzicX2glQ9QTbeSULgy4wSFlfjI-DWf6wlnHSYhjKxoT9ywecTP9KiwbUyGXDGsWwF_y8j5K-0Ei1s21JA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=vzejRIu7K1KsNLRpDKWawAUKksyNMiw9522RaJXlTFgldkDaz_ijP1zaDSh9P5exBZ7WJKyp4Uvr7oXrrtoiG_nfLh9SVapZ0_slbbYyaP_kZTObiKaleYVCoPgv8p3P-QnqpdNGQVGSzaesdnn-uCwgyEJRvdJugoRL4E5lKcadaXBKBDcFhaTEsliqTrFC9OfK2INJClTRK170aHBo16JFu8fldifrfOofHCRDbljRjl9zSwCKmWJJNUjdK60xJnuESzicX2glQ9QTbeSULgy4wSFlfjI-DWf6wlnHSYhjKxoT9ywecTP9KiwbUyGXDGsWwF_y8j5K-0Ei1s21JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.wdn.best
Encryption Key:
bad99364093861634030e96f11fe3132
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/whitedns/679" target="_blank">📅 07:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-678">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmNxFHyLqUl-Zh2WEEqU9m78Yu4EqsIp2rKuhHQJqNeWj3_FYTHPyzma6C3D8Gtut1B8Jn6plm6P19vGUNlvBc7mwcvoOpGwgpXf6ODc5QBC7uYYJrLDnadrXzRC43y0-K5jZWSgidw_NdvGhee-ejjZHu5S35kxICAANJys34PpGH01DfVjwKfbwWKUYWZNR8D3gX3bpiJamM3gVPGCyCxZV4C62p0CTGijGICR7WGUv_Pi3ka2x6Lwbjp2OdoXcFo0iImKx8Ebq7uVKHiTQWKLJQBuhuzfYJ9nzzHEBja8qyYPuQzh0pbApSrfYY-ZSLzrbIOolb6IBYenKN-KEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه بعدی WhiteDNS با ترجمه کامل تمام متن‌ها به زبان فارسی منتشر خواهد شد.
همچنین در این نسخه، دسترسی‌پذیری اپلیکیشن برای افرادی که از اسکرین‌ریدر استفاده می‌کنند و کاربران دارای معلولیت‌های جسمی به شکل کامل‌تر و بهتر بهبود داده شده است.
ممنون از دنی عزیز برای PR</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/whitedns/678" target="_blank">📅 07:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-677">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/677" target="_blank">📅 06:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-676">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jV94lb4QVhHwjMbaNCPHVbjl-fatsxj8NRX2CFW1NoYFzaKWdAfo8Udk72e0tXeDhTbDOeBrD7oW79I97llCAYplpZdwxz1NkHLy73UdjE2gtO42vz6ZqybAj3kPWBKnEKdrmLJG00PE7Rg2ESc3xp3nPHpUhow06_xjvU8jbp0r9fOXd_6hj_nXFV82CXxmNqxaxItaoxcC53bvJPGFW9ILu3eVyjOkZ5p7XjQeFgynZnb1QqrwBETihpvMnhpsiSUn6dP0O5QI5IaapOZPDg8ZkAixRrCc16k7EoM-MJLsqcSLkJBzw8ZRq40pEButHVXhfQafjAsOWkpb279W2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/whitedns/676" target="_blank">📅 06:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-675">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">WhiteDNS
❌
WaitDNS
✅</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/whitedns/675" target="_blank">📅 04:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-673">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
سرور وایت دی ان اس (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲۷ اردیبهشت
Domin Vip :
vip.masir-sefid-3.shop
Domin 1:
v1.masir-sefid-3.shop
Domin 2:
v2.masir-sefid-3.shop
Domin 3:
v3.masir-sefid-3.shop
Domin 4:
v4.masir-sefid-3.shop
Domin 5:
v5.masir-sefid-3.shop
Key :
Telegram-Channel--->@Masir_Sefid
👾
لینک دانلود
کلاینت :
1️⃣
WhiteDNS
1.4.0
1️⃣
WhiteDNS
(Windows)
1.0.5
⚡️
پک ریزالور
⬅️
فیلم اموزش وایت دی ان اس
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
(پیشنهادی)
اگه وصل شدین ری اکشن برید بدونم
❤️
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/whitedns/673" target="_blank">📅 17:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-672">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">☄️
WhiteDNS Premium Configs For StormDNS
☄️
😀
کانفیگ‌های اختصاصی، پایدار و قدرتمند
🚀
مناسب برای اتصال سریع، امن و بدون اختلال
📡
Optimized For Better Stability & Performance
🎁
کانفیگ اهدایی از طرف چنل:
@PersiaTMChannel
01.
🌐
Domain:
b1.persiatmx.us
🔑
Encryption Key:
843996e318d85f34a012240b24714d2f
━━━━━━━━━━━━━━━━━━
02.
🌐
Domain:
b2.persiatmx.us
🔑
Encryption Key:
6b51dfc5f065436a03f76f76af4c7416
━━━━━━━━━━━━━━━━━━
03.
🌐
Domain:
b3.persiatmx.us
🔑
Encryption Key:
2bee92b7342be563851a6f8da0090de4
━━━━━━━━━━━━━━━━━━
04.
🌐
Domain:
b4.persiatmx.us
🔑
Encryption Key:
9f9709ec0bb9c380227237e9ef7c9f3c
━━━━━━━━━━━━━━━━━━
05.
🌐
Domain:
b5.persiatmx.us
🔑
Encryption Key:
962f409687cf0069080d5aef96cccbdc
━━━━━━━━━━━━━━━━━━
06.
🌐
Domain:
b6.persiatmx.us
🔑
Encryption Key:
428c0d303605cefb06f7c33123484ac5
━━━━━━━━━━━━━━━━━━
07.
🌐
Domain:
b7.persiatmx.us
🔑
Encryption Key:
3ac7935006ba328616a5df2aef1ed8fd
━━━━━━━━━━━━━━━━━━
08.
🌐
Domain:
b8.persiatmx.us
🔑
Encryption Key:
6aecaa4877f463a773ab364560815f27
━━━━━━━━━━━━━━━━━━
09.
🌐
Domain:
b9.persiatmx.us
🔑
Encryption Key:
7f3aad92ab16b630fc2d0c7e8469c278
━━━━━━━━━━━━━━━━━━
10.
🌐
Domain:
b10.persiatmx.us
🔑
Encryption Key:
7fb2856813f16fe683a4483bb6ae0f71
Special Thanks To
🤝
@WhiteDNS
Channel
⭐️
StormDNS Project
For Their Support & Contribution.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/whitedns/672" target="_blank">📅 15:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-671">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/whitedns/671" target="_blank">📅 14:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-670">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=kJaE8DbyLwehikr2dUYA3QV8x-cxlRviIRDD5IrsYjyPYCKMY03GrwB-9reS3N2Kk-SKLATBw054KXB-HnOQdH9GTtAtCaRD9YPl5IJXbK72qQKZTq_nmSa4CRO400ahzpqkLPEiU_nlwFWmS5ZtQjUY3jBUp7NvIakfRIzR3MQHicbWxx6Wh1ojxUaYtGj88rm4Aa8IGh-pdn-bI7Smr3vc6CTHC2Ib4otHCdY2PynXbWhmtdYVXAXyIpXefEHhxIiku51Tnc4NQ9mlaDDVEkvUCMWGbVK7JJ9CXYGZ8tXdI9bb7gA2gGhTbxQ0t3g6FfGOYtzirK831GBjywDuCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=kJaE8DbyLwehikr2dUYA3QV8x-cxlRviIRDD5IrsYjyPYCKMY03GrwB-9reS3N2Kk-SKLATBw054KXB-HnOQdH9GTtAtCaRD9YPl5IJXbK72qQKZTq_nmSa4CRO400ahzpqkLPEiU_nlwFWmS5ZtQjUY3jBUp7NvIakfRIzR3MQHicbWxx6Wh1ojxUaYtGj88rm4Aa8IGh-pdn-bI7Smr3vc6CTHC2Ib4otHCdY2PynXbWhmtdYVXAXyIpXefEHhxIiku51Tnc4NQ9mlaDDVEkvUCMWGbVK7JJ9CXYGZ8tXdI9bb7gA2gGhTbxQ0t3g6FfGOYtzirK831GBjywDuCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.store
Encryption Key:
bad99364093861634030e96f11fe3132
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
⚠️
⚠️
⚠️
⚠️
⚠️
حجم کپی از کانال ما واقعاً باورنکردنیه؛ در حدی که آدم شک می‌کنه شاید ما ناخواسته برای بعضی دوستان واحد تولید محتوا راه انداختیم.
کمترین کاری که می‌تونید انجام بدید، انتشار همین پست یا حداقل ذکر منبع کانال ماست. باور کنید نوشتن منبع، اینترنت رو خراب نمی‌کنه و از اعتبار شما هم کم نمی‌کنه.
همراهان عزیز WhiteDNS،
اگر دیدید کانالی بدون ذکر منبع مطالب ما رو کپی کرده، لطفاً با احترام منبع اصلی رو بهشون یادآوری کنید. شاید فقط فراموش کردن؛ کپی‌کردن زیاد آدم رو خسته می‌کنه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/whitedns/670" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-669">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سلام خدمت همه دوستان عزیز
🙌
WhiteDNS یک پروژه غیرانتفاعی و رایگان است که برای کمک به دسترسی آزادتر کاربران ایرانی به اینترنت فعالیت می‌کند.
حمایت مالی شما کمک می‌کند این پروژه زنده بماند، سرورهای بیشتری راه‌اندازی شود و افراد بیشتری در ایران بتوانند به اینترنت آزاد متصل شوند.
هیچ اجباری برای کمک مالی وجود ندارد.
تمام حمایت‌ها فقط صرف هزینه‌های سرور، زیرساخت، توسعه و نگهداری پروژه WhiteDNS خواهد شد.
ممنون از اعتماد و همراهی شما
🙏
🤍
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/whitedns/669" target="_blank">📅 10:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-668">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">لیست ۱۰۰ ریزالوری که در ۲۴ ساعت گذشته به سرورهای WhiteDNS متصل شده‌اند:
185.142.158.162
185.255.91.60
94.232.173.28
217.219.162.200
185.53.142.174
134.255.206.206
185.51.201.58
134.255.206.205
5.202.252.30
109.230.89.90
31.214.169.244
93.115.127.9
185.88.178.196
185.208.174.167
185.37.55.30
80.75.7.2
164.138.17.122
5.160.128.142
158.58.184.147
2.189.44.68
2.188.21.58
185.109.61.27
185.50.37.52
5.236.93.157
185.137.25.146
109.230.206.175
178.252.128.66
185.208.175.228
2.186.121.65
2.188.21.70
78.157.41.60
2.188.21.46
108.162.192.0
173.245.58.0
172.64.32.0
46.209.209.209
207.211.215.145
185.141.105.139
78.39.234.140
37.191.95.70
2.189.44.98
2.188.21.138
185.208.183.29
80.191.163.249
5.160.140.16
46.32.31.30
2.189.44.94
2.189.44.91
5.160.227.78
2.189.44.90
2.189.44.92
2.189.44.93
74.80.77.246
66.185.123.244
109.72.197.1
89.32.197.226
85.185.157.181
185.141.106.238
2.188.21.62
74.80.77.247
78.38.174.2
74.63.24.205
74.63.24.206
172.253.12.221
172.253.13.149
172.253.228.150
77.104.104.104
172.253.228.147
172.253.13.147
172.253.13.146
172.253.228.145
172.253.12.210
172.253.13.156
172.253.13.154
172.253.12.216
172.253.12.154
172.253.12.151
172.253.228.152
172.253.13.157
172.253.13.148
172.253.13.152
172.253.13.144
172.253.13.153
85.133.167.108
172.253.228.156
172.253.228.149
74.63.24.210
172.253.13.151
172.253.228.154
172.253.228.151
172.232.181.197
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/whitedns/668" target="_blank">📅 09:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-667">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/whitedns/667" target="_blank">📅 09:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-666">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">full user-facing guide .txt</div>
  <div class="tg-doc-extra">18.6 KB</div>
</div>
<a href="https://t.me/whitedns/666" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
Quick Guide to WhiteDns for Windows!
🚀
Struggling to connect? Here is the absolute easiest way to set up WhiteDns for maximum speed and stability:
🛠
🔹
1. Basic Setup:
Create a profile and enter your Tunnel Domain and Encryption Key.
📝
🔹
2. Find the Best Connection:
Go to the "Resolvers" tab, run a quick scan, and apply the top-ranked resolver to your tunnel.
📡
🔹
3. Ultimate Stability:
Use the
MasterDNS
engine and select the
Stable Iran
preset for the most reliable experience on restricted networks.
🛡
🔹
4. Choose Proxy Mode:
Use
System proxy
to automatically route traffic for browsers like Chrome and Edge, or choose
SOCKS5 only
(
127.0.0.1:18000
) for manual configuration in apps like Telegram or Firefox.
⚙️
💡
The Golden Formula:
Enter details
➡️
Scan Resolvers
➡️
Apply Best Resolver
➡️
Choose 'Stable Iran'
➡️
Connect!
🏆
Check out the full attached guide below for step-by-step instructions and troubleshooting!
📚
@whitedns</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/whitedns/666" target="_blank">📅 09:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-665">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚀
The Comprehensive WhiteDns Guide for Windows is Out!
🚀
Dear users,
if you are facing any challenges connecting and configuring the WhiteDns app on Windows, this complete guide is made exactly for you. WhiteDns is a powerful desktop tool for tunneling and creating local proxies, and with this guide, you can experience the highest speed and stability.
📌
A quick summary of what you'll learn in this guide:
🔹
Quick & Easy Start:
Step-by-step tutorial on creating a profile, entering your domain, encryption key, and making the initial connection.
🔹
Choosing the Proxy Mode:
Understanding the difference between manual mode (SOCKS5 only) and applying the proxy to the entire system (System proxy) for browsers.
🔹
Powerful Scanner Tool (Resolvers):
How to find the fastest and most stable DNS resolvers using the app's built-in scanner across Quick, Deep, Advanced, and High Accuracy modes.
🔹
Advanced Settings & Engines:
Explaining the differences between the MasterDNS and StormDNS engines, and how to use Presets like
Stable Iran
(for maximum stability on restricted networks) up to Aggressive modes.
🔹
App-Specific Configurations:
Detailed instructions on setting up the local proxy (
127.0.0.1:18000
) on Telegram Desktop, Firefox, Chrome, and Edge.
🔹
Troubleshooting:
Practical solutions for common issues like browsers not connecting despite an active app connection, frequent disconnections, or slow tunnel startup.
💡
The Golden Formula for Connection:
The best and safest route for most users is: Set tunnel details
⬅️
Scan resolvers
⬅️
Apply the best resolver
⬅️
Use Stable Iran preset
⬅️
Connect!
@whitedns</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/whitedns/665" target="_blank">📅 08:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-664">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">راهنمای_جامع_استفاده_از_وایت_دی_ان_اس_ویندوز_.docx</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/whitedns/664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
راهنمای جامع وایت دی‌ان‌اس (WhiteDns) برای ویندوز منتشر شد!
🚀
کاربران عزیز، اگر برای اتصال و تنظیم برنامه WhiteDns در ویندوز با چالشی مواجه هستید، این راهنمای کامل دقیقا برای شما آماده شده است. برنامه WhiteDns یک ابزار قدرتمند دسکتاپ برای تونلینگ و ساخت پروکسی محلی است و با استفاده از این راهنما می‌توانید بالاترین سرعت و پایداری را تجربه کنید.
📌
خلاصه‌ای از آنچه در این راهنما یاد می‌گیرید:
🔹
شروع سریع و آسان:
آموزش قدم‌به‌قدم ایجاد پروفایل، وارد کردن دامنه، کلید رمزنگاری (Encryption Key) و اتصال اولیه.
🔹
انتخاب حالت پروکسی:
تفاوت بین حالت دستی (SOCKS5 only) و اعمال پروکسی روی کل سیستم (System proxy) برای مرورگرها.
🔹
ابزار قدرتمند اسکنر (Resolvers):
آموزش پیدا کردن سریع‌ترین و پایدارترین تحلیلگرهای DNS با استفاده از اسکنر داخلی برنامه (در حالت‌های سریع، عمیق و با دقت بالا).
🔹
تنظیمات پیشرفته و موتورها:
معرفی تفاوت‌های موتور MasterDNS و StormDNS و نحوه استفاده از پروفایل‌های آماده (Presets) مانند
Stable Iran
(برای بالاترین پایداری در شبکه‌های محدود) تا حالت‌های تهاجمی‌تر (Aggressive).
🔹
تنظیمات مخصوص برنامه‌ها:
راهنمای دقیق ست کردن پروکسی محلی (
127.0.0.1:18000
) روی تلگرام دسکتاپ، فایرفاکس، کروم و مرورگر اج.
🔹
رفع مشکلات (Troubleshooting):
راهکارهای عملی برای حل مشکلاتی مثل وصل نشدن مرورگر با وجود اتصال برنامه، قطع شدن مداوم، و یا رفع گیر کردن روی راه‌اندازی کند تونل.
💡
فرمول طلایی اتصال:
بهترین و امن‌ترین مسیر برای اکثر کاربران این است: وارد کردن اطلاعات تونل
⬅️
اسکن تحلیلگرها
⬅️
اعمال بهترین تحلیلگر
⬅️
انتخاب حالت Stable Iran
⬅️
اتصال!
برای استفاده حرفه‌ای از این نرم‌افزار و دور زدن قطعی‌ها، حتماً فایل راهنمای کامل را مطالعه کنید.
#اموزش_ویندوز_whitedns
@whitedns</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/whitedns/664" target="_blank">📅 08:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-663">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/whitedns/663" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای صوتی برای whitedns windows v1.0.5
🚀
راهنمای سریع وایت دی‌ان‌اس (WhiteDns) برای ویندوز!
🚀
برای اتصال سریع و پایدار، این ساده‌ترین روش تنظیم برنامه است:
🔹
۱. تنظیمات اولیه:
یک پروفایل در تب Tunnel بسازید و آدرس دامنه (Domain) و کلید رمزنگاری (Encryption Key) خود را وارد کنید.
🔹
۲. یافتن بهترین اتصال:
به تب Resolvers بروید، یک اسکن سریع (Quick) انجام دهید و با انتخاب گزینه "Apply top to tunnel"، بهترین تحلیلگر را روی تونل اعمال کنید.
🔹
۳. بالاترین پایداری:
در تب Advanced، موتور
MasterDNS
را انتخاب کرده و برای داشتن اتصالی بدون قطعی در شبکه‌های محدود، حالت
Stable Iran
را فعال کنید.
🔹
۴. انتخاب پروکسی:
برای استفاده خودکار در مرورگرهایی مثل کروم و اج از حالت
System proxy
استفاده کنید. برای تنظیم دستی در تلگرام یا فایرفاکس، حالت
SOCKS5 only
(آدرس
127.0.0.1:18000
) را انتخاب کنید.
💡
فرمول طلایی:
وارد کردن اطلاعات
⬅️
اسکن تحلیلگرها
⬅️
اعمال بهترین تحلیلگر
⬅️
انتخاب حالت Stable Iran
⬅️
اتصال!
برای آموزش قدم‌به‌قدم و رفع هرگونه مشکل، فایل راهنمای کامل را در زیر مطالعه کنید.
👇
@whitedns</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/whitedns/663" target="_blank">📅 08:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-662">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GQuKQd_d4_kAZ_7GCz3hrqm-NpK5gs_bOeW49c8-ib5WQHd66v9NhqxBGzXwLQ6pPnDuLiwcvBDDEJPRvUL7nxJqdBgZf1t6rNkO8b1oQ9THdPk8BnmhanQ4EH7SNWR_EyMkIy455lFNIe4bEMyamKT0cLOU7vCFZLL8I2m2G4q0oZArfEYs4F3PYVYLktjNy9zWNvf60EXUeApcmmeC5lpgTSSPyleDezkM1riItjfUOXm8ibdBNbbByox1vBhxsJrWysBAFhkFQQnwGlIN3ZXSmsk952-iWeycEq8XiHEoCNpYfDFWuyHC-6oLXWQcfbl0lz2ujTUKkYE7UIOKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش جامع WhiteDns Windows</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/whitedns/662" target="_blank">📅 08:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-661">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دوستان گرامی :
🤝
حتما در گروه اصلی whitedns عضو شوید تا راحت‌تر به آخرین مطالب دسترسی داشته باشید
🚀
سپاس
🙏
آدرس گروه اصلی :
@whitedns_group
📲</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/whitedns/661" target="_blank">📅 06:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-660">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/660" target="_blank">📅 06:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-659">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">11 MB</div>
</div>
<a href="https://t.me/whitedns/659" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تغییرات WhiteDns ویندوز نسخه 1.0.5
بازسازی رابط مدرن
بهبود جزئیات کوچک رابط کاربری و تراز کارت‌ها برای ظاهری تمیزتر و یکدست‌تر در دسکتاپ.
🖥
✨
اسکنر با دقت بالا :
یک اسکنر با دقت بالا برای شرایط سخت اضافه شد
طراحی شمارنده رزولور بهبود یافته
به‌روزرسانی استایل شمارنده رزولور تا با چیدمان کارت‌های اطراف هماهنگ‌تر شده و ظاهری مدرن‌تر داشته باشد.
🎨
پشتیبانی از سینی ویندوز بهبود یافته
رفتار سینی برنامه به‌روزرسانی شد تا در ویندوز طبیعی‌تر احساس شود و در پس‌زمینه در دسترس بماند.
🪟
🔌
فعالیت شبکه برای حالت SOCKS5 اصلاح شد
فعالیت شبکه اکنون ترافیک را زمانی که برنامه‌ها از پروکسی محلی SOCKS5 استفاده می‌کنند، ردیابی می‌کند، به جای نمایش فعالیت فقط از طریق مسیر HTTP/System Proxy.
🌐
🔍
سازگاری پورت SOCKS سفارشی
فعالیت شبکه اکنون هنگام تغییر پورت SOCKS در تب پیشرفته نیز به کار خود ادامه می‌دهد.
⚙️
حافظه اسکن رزولور اضافه شد
برنامه اکنون بهترین نتیجه اسکن رزولور را به خاطر می‌سپارد و اسکن‌های کامل تکراری را هنگام اتصال مجدد با مجموعه رزولور یکسان کاهش می‌دهد.
💾
🚀
تجربه اتصال مجدد سریع‌تر
اتصالات مجدد باید روان‌تر احساس شوند زیرا برنامه از اسکن مجدد غیرضروری رزولورها هنگام در دسترس بودن نتیجه معتبر قبلی خودداری می‌کند.
⚡️
وارد کردن دستی رزولور اضافه شد
گزینه وارد کردن .txt در کارت «وارد کردن / رزولورهای دستی» برای بارگذاری آسان‌تر لیست رزولورها اضافه شد.
📥
📝
نکات اتصال
از لیست رزولور باکیفیت و کوچک‌تر برای راه‌اندازی سریع‌تر استفاده کنید.
🚀
رزولورهای پایدارتر را در بالای لیست نگه دارید.
📌
هنگام آزمایش اتصال، ابتدا از حالت SOCKS5 استفاده کنید.
🧪
اگر حالت System Proxy با یک برنامه ناسازگار است، آن برنامه را به‌صورت دستی برای استفاده از
127.0.0.1
و پورت SOCKS نمایش داده شده در WhiteDns پیکربندی کنید.
⚙️
مگر در صورت نیاز، از تغییر مقادیر تونل پیشرفته خودداری کنید؛ مقادیر پیش‌فرض معمولاً پایدارترین هستند.
🛡
@whitedns</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/whitedns/659" target="_blank">📅 06:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-658">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fEEj3b0EvlhPnE1qkbgJOEtz0MRB3gtiWx3ZhAicrk4GRyzW3Wr9xR5jnNglsvH0TNTBD6NdCHwSPfdLkoZr_iOgrURky1GaiMx16akUZw_Z8zSf7BBQeCbbG_T03nE9d8AK6aRFk0QDWpdTU5j1xNUZIlMQ06XDXIc2Jq49fxfTtZcNjl1OBqTwSf8zMEcRLE7bnEOKELzrhTavsLf_t2C6yJ__Ov9qGbUgz1h61fWICNTVh-ZW2vtYat2P8AsaiOHUWTfdtng42cBslaRDDvKoU1jwhw5TDXdsMbPwBdRCLIQGHFzQcU1sf1iUrQXhLlELXcUzxx2qkiA1U4AUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/whitedns/658" target="_blank">📅 06:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-657">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">DNSForge-Guide-Persian.pdf</div>
  <div class="tg-doc-extra">79.4 KB</div>
</div>
<a href="https://t.me/whitedns/657" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آموزش گام به گام و متنی برای اتصال به نسخه‌ی ios برنامه‌ی WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/whitedns/657" target="_blank">📅 22:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-656">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🙂
نسخه آزمایشی اپلیکیشن iOS تیم WhiteDNS برای تست اتصال‌های MasterDNS و فورک StormDNS آماده شده است.
برای استفاده، ابتدا باید اپلیکیشن TestFlight را روی دستگاه خود نصب کنید، بعد از طریق لینک زیر وارد نسخه آزمایشی شوید:
https://testflight.apple.com/join/GfUqXrFz
⚠️
لطفاً توجه داشته باشید که این نسخه آزمایشی است و ممکن است هنوز باگ یا ناپایداری داشته باشد.
@WhiteDNS</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/whitedns/656" target="_blank">📅 22:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-655">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-text">📱
آموزش کار با برنامه دفید (Thefeed):
برای دریافت آخرین نسخه و کانفیگ‌ها، به کانال زیر بروید و برنامه را نصب‌ کنید و لینک کانفیگ را کپی کنید:
@thefeedconfig
ورود به برنامه:
۱. برنامه را باز کنید و زبان را انتخاب نمایید.
۲. در قسمت مشخص شده (thefeed://...)، کانفیگ کپی شده را وارد کرده و دکمه «وارد کردن» را بزنید تا ثبت شود.
عملکرد برنامه:
پس از وارد کردن اولین کانفیگ، برنامه ریزالورهای موجود در کانفیگ را بررسی کرده (چند دقیقه طول میکشد) و سپس لیست کانال‌ها را دریافت می‌کند. شما می‌توانید کانال‌ها را باز کرده، پست‌ها را مشاهده و عکس، ویدیو، ویس و فایل‌ها را دانلود کنید.
نکته:
لیست کانال‌ها فقط توسط سازنده کانفیگ قابل تغییر است. (جلو تر یک‌روش دیگر برای کانال های دلخواه شما نیز نوشته ام)
افزودن کانفیگ جدید:
در صفحه اصلی با زدن دکمه + می‌توانید کانفیگ جدید وارد کنید یا کانفیگ‌های موجود دیگر را فعال نمایید.
🛠️
بخش ریزالور ها:
در این بخش می‌توانید ریزالورها را مدیریت کنید. دکمه‌ای به نام «بانک ریزالور» وجود دارد که لیست کامل را نمایش می‌دهد. همچنین یک لیست فعال به نام Default وجود دارد که پس از بررسی اولیه، ریزالورهای فعال را در خود نگه می‌دارد. شما می‌توانید برای اینترنت‌های مختلف، لیست‌های فعال متفاوتی داشته باشید. و با زدن دکمه «بررسی مجدد»، می‌توانید از بانک ریزالور فعال برای اینترنت خود را پیدا کرده و به لیست جدید اضافه کنید.
🔍
بخش پیدا کردن ریزالور:
این بخش بسیار مهم است. با استفاده از یک لیست پیش‌فرض ۵۰ هزارتایی، می‌توانید ریزالورهایی که برای اینترنت شما کار می‌کنند را پیدا کنید (زمانی که سرعت برنامه کم شده بود و یا کار‌ نمی‌کرد).
روش کار:
۱. وارد بخش شوید.
۲. دکمه بارگذاری لیست پیش‌فرض را بزنید.
۳. دکمه شروع اسکن را بزنید.
۴. برنامه شروع به پیدا کردن می‌کند. وقتی حدود ۱۰ تا ریزالور پیدا شد، توقف را بزنید و سپس دکمه «افزودن به لیست فعال» را بزنید.
*توجه:* حتماً باید VPN خاموش باشد.
📺
بخش کانال‌های دلخواه (teleMirror):
این بخش کاملاً از قسمت‌های قبلی جداست و مکانیزم متفاوتی دارد. این بخش از طریق سرویس‌های گوگل، پیام و عکس کانال‌های عمومی تلگرام را می‌آورد و نمایش می‌دهد.
*محدودیت‌ها:* این بخش نمی‌تواند ویدیو پخش کند یا فایل دانلود کند (به خاطر محدودیت‌های گوگل). همچنین برخی کانال‌های عمومی اجازه اشتراک‌گذاری در سایت را نمی‌دهند، و پست هایشان در این قسمت نمایش داده نمی‌شود.
نکته مهم:
این بخش فقط زمانی کار می‌کند که گوگل در دسترس باشد. اگر گوگل مسدود شود، فقط قسمت اصلی برنامه (معرفی شده در اول پست) کار خواهد کرد. همچنین سرویس‌های گوگل محدودیت تعداد درخواست دارند که ممکن است شما را محدود کنند.
🔔
برای اخبار پروژه حتما کانال اصلی را دنبال کنید:
@networkti</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/whitedns/655" target="_blank">📅 22:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-654">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.18.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.9 MB</div>
</div>
<a href="https://t.me/whitedns/654" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید TheFeed (v0.18.10)
🚀
🔸
توی این نسخه چیز مهمی تغییر نکرده! فقط از اونجایی که گیتهاب اکانتم رو ساسپند کرد و هنوز اکانت باز نشده، پروژه TheFeed رو به گیتلب منتقل کردم و برنامه رو هم تغییر دادم که لینک ها و این چیزهای که توی برنامه بود به گیتلب هم اشاره کنه. البته قابلیت دانلود آخرین نسخه و نوتیف نسخه جدید هنوز به گیتلب وصل نشده و کار‌نمیکنن (گیتلب فیلتره و کمکی نمیکنه اضافه کردنش
🫠
).
البته توی تنظیمات یک دکمه هست به اسم "بررسی" که وقتی بزنیدش اخرین شماره نسخه رو از سرور میپرسه و نشون میده، این رو سمت سرور تغییر دادم که اگر‌ گیتهاب کار نکرد اخرین شماره نسخه رو از گیتلب بگیره و سمت کلاینت هم یک باگ داشت که رفع شد.
⚠️
این نسخه خیلی مهم نیست و میتونید آپدیت نکنید
آدرس سورس کد پروژه روی گیتلب:
https://gitlab.com/sartoopjj/thefeed
یک نفر لطف کرده بود و فیچر های دسترسی پذیری اضافه کرده بود و پول ریکوئست فرستاده بود، لطفا اگر این پیام رو میبینی مرج ریکویست بفرست روی گیتلب
🥲
❤️
کانال اصلیم:
@networkti
کانال کانفیگ برای برنامه:
@thefeedconfig</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/whitedns/654" target="_blank">📅 22:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/whitedns/653" target="_blank">📅 21:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">WhiteDns-Windows-Setup.exe</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/whitedns/652" target="_blank">📅 09:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">White DNS
pinned «
⚠️
اعلان مهم
📢
تمام تبلیغاتی
📰
که در این کانال قرار می‌گیرند، هیچ ارتباطی با ما ندارند
🚫
و ما هیچ‌گونه مسئولیتی در قبال محتوای آگهی‌ها، معاملات، خرید و فروش، یا هر نوع کلاهبرداری احتمالی
🎭
قبول نمی‌کنیم.  دلیلش ساده است: ما هیچ کنترلی روی تبلیغات ارسال‌شده…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/651" target="_blank">📅 07:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-650">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚠️
اعلان مهم
📢
تمام تبلیغاتی
📰
که در این کانال قرار می‌گیرند، هیچ ارتباطی با ما ندارند
🚫
و ما هیچ‌گونه مسئولیتی در قبال محتوای آگهی‌ها، معاملات، خرید و فروش، یا هر نوع کلاهبرداری احتمالی
🎭
قبول نمی‌کنیم.
دلیلش ساده است: ما هیچ کنترلی روی تبلیغات ارسال‌شده نداریم
🤷‍♂️
. این تبلیغات به صورت خودکار توسط خود تلگرام در کانال گذاشته می‌شوند
🤖
مسئولیت هرگونه تعامل، پرداخت یا ارتباط با آگهی‌دهنده، کاملاً بر عهده خود کاربران
👥
است
@whitedns</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/whitedns/650" target="_blank">📅 07:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-649">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">9.2 MB</div>
</div>
<a href="https://t.me/whitedns/649" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه 1.0.3
یک آپدیت متمرکز بر پایداری است. در این نسخه پایداری اتصال بهتر شده، مپ شدن تنظیمات Advanced اصلاح شده، تفاوت بین SOCKS5 و System Proxy شفاف‌تر شده، و احتمال حالتی که برنامه Connected باشد ولی سایت‌ها باز نشوند کمتر شده است.
WhiteDns Windows v1.0.3
- راهنمای سریع تست
لطفا برای تست اول این تنظیمات را استفاده کنید:
1. برنامه را باز کنید.
2. وارد بخش Connect شوید.
3. گزینه Proxy Mode را روی System proxy بگذارید.
4. وارد بخش Advanced شوید.
5. گزینه Transport preset را روی Balanced بگذارید.
6. این موارد را بررسی کنید:
- Compression = off
- Base64-encode data = Off
- DNS listener enabled = Off
- SOCKS5 authentication = Off
- Packet duplication = 0
7. در صورت نیاز ذخیره کنید و سپس Connect بزنید.
اگر سایت ها ناپایدار بودند یا باز نشدند:
- فقط همین یک مورد را تغییر دهید:
- Transport preset = Stable Iran
لطفا این موارد را گزارش کنید:
- آیا اتصال با موفقیت انجام شد؟
- آیا یوتیوب و سایت های عادی باز شدند؟
- از چه Proxy Mode استفاده کردید؟
- سرعت مرور مناسب بود یا نه؟
- آیا برنامه یا سایتی بود که با وجود Connected بودن کار نکند؟
@whitedns</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/whitedns/649" target="_blank">📅 07:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-648">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CTcBfCR2rZxVB1TfR6kuB3YnbKwAucEFzFzrnvK9GfyGfnnfKEs8wdBpEB0aq82qTFkhbacmzL8yRWR8vvwfjHLfOHlMVxj63gjvSC9ogxW7_hPRE27UnnjSXruLOMtWQ5eZwa1ZDVdageq5EJ8MHJGLZuJqSMGEauEWo9OsstebLiW4ZagKVHwUAupge3rVGBn7X_0kCbrXXwYsTMeScrtdJoe5y3g46gvPnEXB__RrJ6Wg10Xpo8l0kC-6GRIedMqYTuzXADlSeXhPRNyY8ryAANqoqUZHTfdOJZpk1cAca2qjccIUlhFWG8HvjkXtdsmmsyEY1GkIHBgv2a0C1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/whitedns/648" target="_blank">📅 07:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-647">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/whitedns/647" target="_blank">📅 04:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-646">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSOS Iran Connect</strong></div>
<div class="tg-text">🔶
خبرهای خوب:
۱. عبدالکریم، دوست بلوچ ما، تونست اپلیکیشن WhiteDNS را با کار تیمی دوستان راه بندازه
و وصل بشه
🎉
🗣
صدای خودشون، ۱۴۰۵.۰۲.۲۶، ۰۱:۵۲ ایران
۲. من داستان عبدالکریم روشندل را به Pedi جان در
@WhiteDNS
منتقل کردم، و دو درخواست مطرح کردم:
الف. داشتن رابط کاربری (user interface) پارسی در اپلیکیشن WhiteDNS.
ب. افزودن راهنمای پارسی به گیت‌هاب پروژه برای استفاده روشندلان با کمک ScreenReader.
ایشون از ایده‌ها استقبال کرد، ولی به زمان نیاز دارند.
⚪️
هدف دلی ما اینه که کاربرها خودکفا و مستقل باشند.
🫂
#همدلی
#ایران
💛
@WhiteDNS
🆔
@SOSIranConnect</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/whitedns/646" target="_blank">📅 03:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-645">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/whitedns/645" target="_blank">📅 01:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-643">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b77e656a8.mp4?token=UDz3w81xDUuveYsSWr8ZKJUHOXr1cBo5m0VYx1uA2EQayXomRKJyxiilbcpFMyjGf9Bd0Kf87QP76M94N3rTLdipLsVAjmUR_oZ9ZxMNFjocG8PBEAjDS9jnDcSvGB4V74mF9zd7S_YYyN13j6Sbz_E-jjIkhnhWupCzj133bw8CQUv3MtgbRl5MDCikaNOdfKz6zRPDWPfx65jM8Tcv51pvJjcVBGxspWev_Mc7qtCyyMaLLUB0jwgkiEM919th0Rr2jGKLOXi85f8HoW_gts_H5BmyOvaQ6KPOGjSRqG9OaMcNtWQcZQSwYwgoMiPZcIONmek4pvDCb_mFeVzXaUbwN-AESn8ksCD6BzPsmGtibK616hoYUDo6FNW42H5O2mRw1fiDAIAFFrNqBWeuc_HEskNMdehJ3I8_dMWERJvbtwTco6Z4R0G-nmXyMG7b1SUr2eNHJA2jmCazPstHXn8rrfQQ8u1r5I-ml2k3vfvwU18PEIvFHb-O8wrRRsXSChunSciTzuFGPiIWYAX5MX47fCgMLAu4Hq-1UuQIcdSAubqSWBIcJ5pWJuR4M6yCE5giTyz6a8xt_rBqhZDQFSHutG8R6iYgVOSENg7tuLSEIs_YQNXLjLfoUpx4SqyY_BcgJqhC_TU1rsdeJZdYN4yDJEcGd2_JtZzKaNGKLHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b77e656a8.mp4?token=UDz3w81xDUuveYsSWr8ZKJUHOXr1cBo5m0VYx1uA2EQayXomRKJyxiilbcpFMyjGf9Bd0Kf87QP76M94N3rTLdipLsVAjmUR_oZ9ZxMNFjocG8PBEAjDS9jnDcSvGB4V74mF9zd7S_YYyN13j6Sbz_E-jjIkhnhWupCzj133bw8CQUv3MtgbRl5MDCikaNOdfKz6zRPDWPfx65jM8Tcv51pvJjcVBGxspWev_Mc7qtCyyMaLLUB0jwgkiEM919th0Rr2jGKLOXi85f8HoW_gts_H5BmyOvaQ6KPOGjSRqG9OaMcNtWQcZQSwYwgoMiPZcIONmek4pvDCb_mFeVzXaUbwN-AESn8ksCD6BzPsmGtibK616hoYUDo6FNW42H5O2mRw1fiDAIAFFrNqBWeuc_HEskNMdehJ3I8_dMWERJvbtwTco6Z4R0G-nmXyMG7b1SUr2eNHJA2jmCazPstHXn8rrfQQ8u1r5I-ml2k3vfvwU18PEIvFHb-O8wrRRsXSChunSciTzuFGPiIWYAX5MX47fCgMLAu4Hq-1UuQIcdSAubqSWBIcJ5pWJuR4M6yCE5giTyz6a8xt_rBqhZDQFSHutG8R6iYgVOSENg7tuLSEIs_YQNXLjLfoUpx4SqyY_BcgJqhC_TU1rsdeJZdYN4yDJEcGd2_JtZzKaNGKLHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
دور زدن فیلترینگ با کانفیگ سرورلس با ترکیب nekobox و v2rayng
•
✅
لینک کانفیگ nekobox
•
https://pastebin.com/raw/rWeHKSt3
•
✅
لینک داخلی کانفیگ nekobox
•
https://seup.shop/t/exks1
•
✅
لینک کانفیگ V2rayNg
•
https://pastebin.com/raw/Yfymhyy5
•
✅
لینک داخلی کانفیگ‌ V2rayNg
•
https://seup.shop/t/k9mmj
❗️
هر دو کلاینت رو، رو حالتvpnبزارید .
📥
لینک داخلی ویدیوها
•
🎥
https://seup.shop/f/uns5
•
🎥
https://seup.shop/f/v4jx
•
𝕏 Irvictorious
kian
•
@ConfigWireguard
💎
•
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/whitedns/643" target="_blank">📅 19:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-642">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">White DNS
pinned «
💥
💥
💥
💥
💥
💥
💥
برای تبادل نظر و همگرایی در گروه ما عوض شوید
🔄
👥
@whitedns_group
🌐
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/642" target="_blank">📅 19:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-641">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">💥
💥
💥
💥
💥
💥
💥
برای تبادل نظر و همگرایی در گروه ما عوض شوید
🔄
👥
@whitedns_group
🌐</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/whitedns/641" target="_blank">📅 19:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-639">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">لیست ۱۰۰ ریزالور که طول ۲۴ ساعت گذشته به سرور های WhiteDNS وصل شدند
185.94.98.34
2.189.44.68
185.44.36.216
185.137.25.146
94.232.173.28
185.142.158.162
217.219.162.200
185.88.178.196
178.252.143.130
134.255.206.206
80.75.7.2
134.255.206.205
185.53.142.174
89.32.197.226
185.37.55.30
77.238.111.234
31.214.169.244
80.71.149.62
185.109.61.27
62.60.197.83
185.88.178.177
178.252.128.66
158.58.184.147
5.202.252.30
74.63.24.205
74.63.24.211
216.147.121.134
74.63.24.210
46.209.209.209
217.66.203.211
74.80.77.246
80.191.221.26
2.189.44.98
216.147.121.98
164.138.17.122
207.211.215.145
151.232.36.4
185.208.175.228
2.188.21.58
108.162.192.0
172.64.32.0
80.191.163.249
173.245.58.0
78.39.234.140
185.208.183.29
2.188.21.138
2.188.21.70
2.188.21.46
185.255.91.60
66.185.123.243
2.189.44.85
2.189.44.82
2.189.44.83
2.189.44.86
2.189.44.84
2.189.44.14
74.80.77.247
109.107.159.45
2.189.44.92
2.189.44.94
2.189.44.91
2.189.44.93
2.189.44.90
78.157.41.60
193.178.200.3
46.32.31.30
185.208.174.167
85.185.157.181
77.238.123.179
185.141.105.139
5.160.140.16
5.160.227.78
185.53.141.230
185.105.101.1
37.255.223.218
85.133.129.242
78.38.174.2
37.191.95.70
74.80.77.244
74.80.77.245
93.118.109.213
194.61.120.143
121.127.46.65
93.126.5.205
5.160.137.130
2.180.21.241
82.114.164.226
@WhiteDNS</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/whitedns/639" target="_blank">📅 16:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-636">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سرور اهدایی از رسول عزیز از تیم وایت دی ان اس
Name: H3 (Germany)
Domain:
v.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Serbia
Domain:
v3.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Turkey
Domain:
v4.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: USA
Domain:
v5.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Switzerland
Domain:
v6.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: RMFT g1-7
Domain:
g1-7.rmft.tech
Encryption Key:
a337e9fa75161c44bebe7d717da36afc</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/whitedns/636" target="_blank">📅 12:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-635">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سرور اهدایی از چنل
@Masir_Sefid
لطفا از چنل دوستان اهدا کننده سرور حمایت کنید.
Name:
@Masir_Sefid
🕊
(1)
Domain:
v1.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(2)
Domain:
v2.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(3)
Domain:
v3.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Name:
@Masir_Sefid
🕊
(4)
Domain:
v4.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(5)
Domain:
v5.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/whitedns/635" target="_blank">📅 12:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-633">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/whitedns/633" target="_blank">📅 12:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-631">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQ1SYlGOdstUIYffh--vky9wRpR3UeBIaLdq86DIy7q0g56CJv_IJQH-ovkaL0eLdbisRbAC7IhveLbidgTpZKahkyTLFN8Sp_YGzzAChO5g_GJxHsN71GN1mMiaG8jQ12YZ_TGMdpOeQ8Aq-I9GXLPX6YF50b0RDtfcnmviiB72boXHUvK42eAFT54SnMIN5oLJlwCrS90X9L9l-oHi0Mkp2ESRSkuJJaAhc3g6p9rhIuOD3jFqt-un2p7BdLHiLhd9N6d3POoCm3jzzGsvPk9uKH5XD2C4R9Kcc6tfzC3_oy50NsZMmXhsBhOQLyqc8oZOfWgENsGDfnT3B8RhQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X4k4NYpnGOj9WD_WZSz2p8_kv2q4TesRl0wsp4hY7x6Lsp1eYHHi-gnnw2USh9gN-GONL6dxbPsjmncVLQVlFG2jSRH50mPUC2Og6issCej9Hacg3gCFPVnlHFS4TeQH_SOnYEnX1JJdjYiDDNG07MMltxiDmTOnPVc07bEK4xk9SOubPcUDwZVTqdvgUsOVJcMIGJjOEDq0MCiehrKdH6o4eidwVRsOR3B_33aQZfaoFZJYKfqTdgieo8O27b_8Qr2O8STYuPpeMkauisEjdTVAJzjDWzzldUH1cspI6AsKGk9HVJ-D-wQu4jsYhBNy_TtkCFEyv21SMOCTI8IEEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درحال حاضر نزدیک ۱۰۰۰ نفر فقط به سرور ما متصل هستند. سرور تا نزدیک ۲۴۰۰ نفر میتونه کاربر بدون افت کیفیت رو پشتیبانی کنه.
جدا از سرور های ما، سرور های اهدایی باقی چنل ها مثل مسیر سفید هم هست. ویدیو آموزش سرور اختصاصی هم پست های بالاتر گذاشتیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/whitedns/631" target="_blank">📅 11:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-630">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=fJSZIOE-38ubD0Aetnx3CQ4FtACx99VZVS3MZEhN8stygKMVuf-SWddH1eVpYHchlO2TD3kAvHJqQVDSfJwSw7oWuwn-u0r5jfnaqM7zB9hIs0H0s8NASfPGbrqh7UYbGOkLa1gNAGhBC4JbaaPS4u0AHg_eH8O1hEzttqsLDhftHnGdkL1jvzASuRs4KOVC5fC_SiPZXASPhfhwNRNZZ6wnfD8MvasKqww_TwXK1yAxdyJaFN8EN9tNbXxuLEFP3xudIQp3aCMat4R3_8NmO6XiOwfJWCOI2pK0MAepOgI2I2aD6VF1x4gk-vcueIoO2ULstkVol9vncbHcJ_-7ug" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=fJSZIOE-38ubD0Aetnx3CQ4FtACx99VZVS3MZEhN8stygKMVuf-SWddH1eVpYHchlO2TD3kAvHJqQVDSfJwSw7oWuwn-u0r5jfnaqM7zB9hIs0H0s8NASfPGbrqh7UYbGOkLa1gNAGhBC4JbaaPS4u0AHg_eH8O1hEzttqsLDhftHnGdkL1jvzASuRs4KOVC5fC_SiPZXASPhfhwNRNZZ6wnfD8MvasKqww_TwXK1yAxdyJaFN8EN9tNbXxuLEFP3xudIQp3aCMat4R3_8NmO6XiOwfJWCOI2pK0MAepOgI2I2aD6VF1x4gk-vcueIoO2ULstkVol9vncbHcJ_-7ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.site
Encryption Key:
bad99364093861634030e96f11fe3132
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
⚠️
⚠️
⚠️
⚠️
⚠️
حجم کپی از کانال ما واقعاً باورنکردنیه؛ در حدی که آدم شک می‌کنه شاید ما ناخواسته برای بعضی دوستان واحد تولید محتوا راه انداختیم.
کمترین کاری که می‌تونید انجام بدید، انتشار همین پست یا حداقل ذکر منبع کانال ماست. باور کنید نوشتن منبع، اینترنت رو خراب نمی‌کنه و از اعتبار شما هم کم نمی‌کنه.
همراهان عزیز WhiteDNS،
اگر دیدید کانالی بدون ذکر منبع مطالب ما رو کپی کرده، لطفاً با احترام منبع اصلی رو بهشون یادآوری کنید. شاید فقط فراموش کردن؛ کپی‌کردن زیاد آدم رو خسته می‌کنه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/whitedns/630" target="_blank">📅 11:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-625">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.3 MB</div>
</div>
<a href="https://t.me/whitedns/625" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان  نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
🤖
دانلود نسخه یونیورسال از سرور های داخلی
🔴
ویدیو آموزشی استفاده از اپلیکیشن…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/whitedns/625" target="_blank">📅 11:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-624">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQPew2cOzqYDIc82GRcvnSCwA2SCNKzNU6AD2nAh1IqBkWsPlLmyHDX9wUO8KN9KG1jyjDad827lX4CNrJSP0uHUw_acjAOSNBhULXp0vJ6PBuEJDq4bn7ld1iKE-UQa_qQKAvEgIcFmwkkJ11T3syS3eaFKmOa8tcccUN5OIFEy7UVYP1rZg1hn8QBuUUoNQBlea80th6J6Ckc2dhKnL_B6KRU0JHPEk8Be_UaC7BPY5ZD4qIj-aKQOuqCqAMQ1PbDxDKbtWY3e8mCV80lw4_D9y9BeOfudQ3w3tHA6ms2Q_yXG1xJuqAZexIKqEbja8BsQPRvx4Jw5_uMkm3RbhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
🤖
دانلود نسخه یونیورسال از سرور های داخلی
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
تمرکز اصلی این نسخه روی ساده‌تر شدن اتصال و پیدا کردن بهترین تنظیم برای هر کاربر بوده است. هدف این بود که WhiteDNS قبل از اتصال، چند کانفیگ مختلف را با Parallel Test بررسی کند، بهترین گزینه را از نظر سرعت و کیفیت انتخاب کند، و کاربران بدون نیاز به گشتن دنبال Resolver، با لیست پیش‌فرض ۴۵۰۰+ Resolver داخل اپ سریع‌تر اسکن کنند و راحت‌تر وصل شوند.
تغییرات این نسخه
:
✅
نسخه اپلیکیشن به 1.4.0 ارتقا پیدا کرده
✅
قابلیت Parallel Test برای تست هم‌زمان چند تنظیم مختلف قبل از اتصال اضافه شده
✅
حالا WhiteDNS می‌تواند قبل از اتصال، چند حالت اتصال را هم‌زمان بررسی کند
✅
اپ سرعت و Ping هر تنظیم را تست می‌کند و بهترین گزینه را برای همان اتصال انتخاب می‌کند
✅
قابلیت Parallel Test هم برای Proxy Mode و هم برای Full VPN قابل استفاده است
✅
در حالت Full VPN، اپ اول بهترین تنظیم را با Parallel Test پیدا می‌کند و بعد اتصال VPN نهایی را روشن می‌کند
✅
نتایج Parallel Test بعد از اتصال داخل صفحه اصلی نمایش داده می‌شود
✅
می‌توانید تنظیم موفق Parallel Test را با نام دلخواه ذخیره کنید
✅
چند تنظیم آماده WhiteDNS برای تست سریع اضافه شده
✅
می‌توانید پروفایل‌های تنظیمات پیشرفته خودتان را هم وارد Parallel Test کنید
✅
بیش از 4500 Resolver داخل اپ قرار گرفته تا برای اسکن و اتصال راحت‌تر استفاده شود
✅
لیست Resolver پیش‌فرض داخل اپ کامل‌تر شده
✅
پروفایل Default Resolver اضافه شده تا اپ همیشه یک لیست آماده Resolver داشته باشد
✅
امکان اسکن مستقیم لیست Resolver پیش‌فرض اضافه شده
✅
اسکن فایل‌های بزرگ Resolver سبک‌تر و بهتر انجام می‌شود
✅
ریزالورهای تکراری یا قبلاً پیدا‌شده بهتر کنار گذاشته می‌شوند
✅
شمارش Resolverهای سالم و ردشده در اسکن دقیق‌تر شده
✅
اگر پروفایل اسکن سرور یا کلید نداشته باشد، اپ واضح‌تر جلوی شروع اسکن را می‌گیرد
✅
ویرایش سرور، Resolver و تنظیمات از صفحه اصلی راحت‌تر شده
✅
امکان حذف پروفایل‌های اتصال تکراری اضافه شده
✅
پروفایل Default Resolver از حذف یا جابه‌جایی اشتباهی محافظت می‌شود
✅
هشدار باتری حالا قابل بستن است
✅
نمایش سرعت، مصرف اینترنت و آمار اتصال دقیق‌تر شده
✅
تنظیمات پیشرفته برای اتصال‌های کندتر و مسیرهای سنگین‌تر بهتر تنظیم شده
✅
وارد کردن و خروجی گرفتن فایل‌های TOML با گزینه‌های جدید کامل‌تر شده
✅
هسته داخلی StormDNS به‌روزرسانی شده
تنظیماتی که به صورت اتوماتیک انتخاب میشوند، تمرکز روی سرعت و کیفیت دارد. امکان افزایش مصرف اینترنت شما با کانفیگ انتخاب شده می‌باشد. اگر نگران این موضوع هستید تنظیمات را مرور کرده و مقدار  Upload Dup را کمتر کنید.
⚠️
⚠️
⚠️
⚠️
⚠️
حجم کپی از کانال ما واقعاً باورنکردنیه؛ در حدی که آدم شک می‌کنه شاید ما ناخواسته برای بعضی دوستان واحد تولید محتوا راه انداختیم.
کمترین کاری که می‌تونید انجام بدید، انتشار همین پست یا حداقل ذکر منبع کانال ماست. باور کنید نوشتن منبع، اینترنت رو خراب نمی‌کنه و از اعتبار شما هم کم نمی‌کنه.
همراهان عزیز WhiteDNS،
اگر دیدید کانالی بدون ذکر منبع مطالب ما رو کپی کرده، لطفاً با احترام منبع اصلی رو بهشون یادآوری کنید. شاید فقط فراموش کردن؛ کپی‌کردن زیاد آدم رو خسته می‌کنه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/whitedns/624" target="_blank">📅 11:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-623">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoOrL1ytZRvkE6kBHrU0-DiM78kbjHNYwpGL6nFEvvYPDX9s7qvU05OwXt58nrsJnNG4UObEZyrqJ1OlBNRdMysxQA-l3fEZoe0RRNYgAXE0p7RD_KgE5DM9oGHJfzqfUmvP4IpoohXg865ULbCwW2Ao8EFM30yZ1Mk9AAP_m2FDZt7DYx_pR-GnDo4Q3dAcBDPsM7t5ArIjXegR7d70ec87CE05kOF3WyRxGKsTrNXoKkaExXYhezeWgXXZ70Qwn59e1T8ArAXOpFFmYD3sRiUUxFeyM822z6u3wx2hbjI1vpaooVPQuKR0fL6mptjWIREbX5k5EXpuXsRGXgOi2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن ۱.۴.۰ کلاینت اندروید WhiteDNS به‌زودی منتشر می‌شود. در این نسخه سعی کردیم کار شما را راحت‌تر کنیم و اتصال سریع‌تر و ساده‌تر انجام شود.
در این ورژن، اپ به‌صورت خودکار ۷ تنظیم مختلف را با قابلیت Parallel Test بررسی می‌کند و در نهایت بهترین کانفیگ را از نظر سرعت و کیفیت برای شما انتخاب می‌کند.
همچنین بیش از ۴۵۰۰ Resolver که قبلاً داخل بات و گروه منتشر شده بود، به‌عنوان لیست پیش‌فرض داخل اپ قرار گرفته است تا بدون نیاز به گشتن دنبال لیست، بتوانید مستقیم اسکن را شروع کنید و راحت‌تر وصل شوید.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/whitedns/623" target="_blank">📅 10:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-622">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoFVvQssxtU6-6H_qZP2-TvvuEZ3roiM9IghitbAvu0-w-TwVqTLM_TRQjevc_DIP610sO7asYg7rqD3IxINrYKaA0wRQvyzoA9AG8ZytdPJy9Bbh0RILJZpuNrisTUgIWaLEcQbXgBVI5tAGEQ_8jjKxXCyX9erCk_6E5OhiY2blpZuQx-txL9ChsA5Ksffr_HXjdyUC78jB_4WJJ2tH_5260ywKuMf9z5n879yCx0fXjmM44ywTk6R1Dw8SpZTBvQjRbI1In5uhfu-IUPAmhGUoouJp7o0TuGJwiFudGpdEu4mIdypj3oA9RXC1yt7Bhxq0Snx6-Thl_753Mv08w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.space
Encryption Key:
bad99364093861634030e96f11fe3132
از همه کانال‌ها و دوستانی که این لیست رو بازنشر می‌کنند خواهش می‌کنیم حداقل سهم و همکاری‌شون این باشه که کانال ما رو به عنوان منبع ذکر کنند. این داده‌ها با زمان، هزینه و اسکن گسترده جمع‌آوری شده، نه با جادو و دعای نیمه‌شب.
این بزرگترین سرور ما هستش. ۱۲ هسته سی‌پی‌يو و ۲۴ گیگ رم.
✈️
هر مشکلی هست، از سمت اختلال شبکه، تنظیمات و ریزالور ها هستش.
@WhiteDNS</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/whitedns/622" target="_blank">📅 07:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-620">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">StormDNS-Setup-Guide.mp4</div>
  <div class="tg-doc-extra">151.4 MB</div>
</div>
<a href="https://t.me/whitedns/620" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دوستان عزیز سلام
یک فیلم آموزشی آماده کردم برای نحوه راه‌اندازی سرور شخصی StormDNS/MasterDNS
دانلود سرور داخلی
https://guardts.ir/f/3c4216b2ea16
✍️
آموزش متنی
پیش‌نیاز:‌ تهیه سرور و دامنه خارج از ایران
1️⃣
آماده‌سازی DNS
ابتدا یک ساب‌دامین کوتاه بسازید و آن را به نیم‌سروری وصل کنید که به IP سرور شما اشاره می‌کند.
مثال:
ns.example.com  A   1.2.3.4
v.example.com   NS  ns.example.com
توضیح:
ns.example.com
باید به IP سرور شما وصل باشد.
v.example.com
باید به عنوان Subdomain Delegation به
ns.example.com
اشاره کند.
یعنی تمام درخواست‌های DNS مربوط به
v.example.com
به سرور شما ارسال می‌شود. اینترنت هم بالاخره یک جایی باید بفهمد با خودش چند چند است.
2️⃣
نصب سرور
روی سرور لینوکسی خود، دستور زیر را اجرا کنید:
bash <(curl -Ls https://raw.githubusercontent.com/nullroute1970/StormDNS/main/server_linux_install.sh)
بعد از نصب و اجرای سرور، برنامه به صورت خودکار کلید رمزنگاری فعال را نمایش می‌دهد.
همچنین این کلید داخل فایل زیر ذخیره می‌شود:
encrypt_key.txt
برای مشاهده کلید می‌توانید از دستور زیر استفاده کنید:
cat encrypt_key.txt
3️⃣
موارد موردنیاز برای اتصال کلاینت
بعد از راه‌اندازی، برای ساخت پروفایل یا اتصال کلاینت معمولاً به این اطلاعات نیاز دارید:
Domain: v.example.com
Encryption Key: مقدار داخل encrypt_key.txt
Server IP: 1.2.3.4
لینک داخلی:
https://guardts.ir/f/3c4216b2ea16
@WhiteDNS</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/whitedns/620" target="_blank">📅 03:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-617">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HJe8i8UfEa1m-F5OSTaI6-FePego-e8_l1LAHOjjE0wivh3muHxIyOiFNS0nfrjaqEmQaTvNQ1R5VzFYm_cjS1C2M7jPNHN8SutQBJPxBaXVaft5wemJr9l9ogAHqPamN7QOO6p4eOrLzTQUuKW15otiLJSA0MkcUvT57U3rQiWXF8uviPmzOUjbxjeQjC23Nrg5EYOTGCDhGMin2qAAZtP9fmMurbVoRVYlkTuT88c2LTs7OdunQ0buLC1Tvt0EXNs_4uUFFVNcjxz51K65tamNXStHMkb1x2_ke79kNDwLLpSWD3ucu3zR1Yyz9bMPdpfA5JphcxcVw1C6X7keXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bjhM5BGykTgYMRt0xGOs7fa1oepKyvJuyIiJ69spFROno1JdD8oCaiDzbhs7cPpVd_t6TtAIBH0_wrmpqb1Z6kWM9WflNmDeFd8hhGrCtaxQAQu9JQ9L6i0xcmvFZhFu7hl5TpdMrw5v5XiyTl0AfPotjHLCYj0vB0MNOhDEBw7Z4BZCcYNOw86C31x-phCvQ_0zc3HVxGws7s6vJd7GTpuQoAhgHiv5kxLtF_n4lnlrhvzn-jH92jQ0BnQNgU_dGaTgCvUTSFCzLMvT7weqKts80gx717zNQ12E7uW3BeJZzmJAKRxEuU-0x8V3sNM3RFEtalbOg95xcipJMnEvHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داخل پروژه
TheFeed
که متعلق به
Sarto
عزیز هست یک فیچر برای ریزالورها وجود دارد. یک
جدول امتیازدهی برای ریزالورها
درست شده و بازخورد خوبی از سوی کاربران داشته بخاطر اینکه وضعیت ریزالورهای داخل جدول به طور واضح مشخص شده است.
همچنین خود برنامه به صورت رندوم از ریزالورهایی استفاده میکند که امتیاز بیشتری دارند تا کیفیت اتصال ریزالورها به
حداکثر
برسد.
متاسفانه اکانت گیتهاب
Sarto
ساسپند شده اما میتونید برای دریافت برنامه‌ی
TheFeed
به لینک زیر که پست کانال خود
Sarto
هست مراجعه کنید و ازش
حمایت
کنید:
لینک پست
@WhiteDNS</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/whitedns/617" target="_blank">📅 00:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-616">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
آموزش خیلی مقدماتی و ساده برای استفاده از این نسخه
@whitedns</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/whitedns/616" target="_blank">📅 18:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-615">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">6.8 MB</div>
</div>
<a href="https://t.me/whitedns/615" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Whitedns windows v1.0.2</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/whitedns/615" target="_blank">📅 17:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-614">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/T2RIeq3XNgNEJ8EtsN3PIiIbzTYEAlMq8SO8hVoRKPfvqtGUqK2p_0C1H3hAI5jvhVHSfLr_0FBTOej1z3TrltYucnqJHK0bVEQAtsC_853pxqXTSIMcEZGkSLTA7TtKlYIB2sfYHTGxN9W6MZZyASGnVCoHLZQJNyPy5FIWo9c5KaGmB09wwaqmDMWN8TUCeLAsOWVNHS8NMjlrY3MLjS8ynh0pSKtSrU9CdtFd0k1pdRzLN-MSETYlvjiwAHfuh7eiTyMaZLvbzux0Bzr80vn1_EPTEGYcldA4BozCo4RnkpMYhC8t9WahNR3o66LhO1t1ygUBICC8EpoOdg7pJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
🔥
🔥
🔥
🔥
نسخه ۱.۰.۲ بر پایداری، قابلیت استفاده و تشخیص‌های بسیار قوی‌تر رزولور تمرکز دارد.
🛠
این بروزرسانی مشکل آکاردئون را در بخش تنظیمات پیشرفته اصلاح می‌کند تا بخش‌ها با قابلیت اطمینان بیشتری باز و بسته شوند و چیدمان تنظیمات رفتار سازگارتری داشته باشد. همچنین اسکنر رزولور را با یک حالت اسکن پیشرفته جدید بهبود می‌بخشد که رزولورها را به روشی واقع‌گرایانه‌تر و آگاه به تونل، با استفاده از دامنه فعال تونل آزمایش می‌کند، از جمله بررسی‌های DNS بدون کش، قابلیت EDNS0، یکپارچگی NXDOMAIN، مدیریت زیردامنه‌های تو در تو و جستجوهای پروب به شکل تونل.
🌐
تجربه نتایج اسکن نیز بهبود یافت. اکنون خروجی با اطمینان بیشتری کار می‌کند، مرتب‌سازی به درستی عمل می‌کند و نتایج صادر شده اکنون بهتر با آنچه در رابط کاربری نمایش داده می‌شود مطابقت دارند. جزئیات اضافی اسکن مانند امتیاز، دامنه پروب و قابلیت مشاهده بار EDNS اضافه شد تا رزولورهای قوی‌تر را با دقت بیشتری شناسایی کنید.
📊
✨
@whitedns</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/whitedns/614" target="_blank">📅 17:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-612">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/GMCUGbRrSI3MeI0nw-5XWqeYOax0cy6a5z8LVWrLokLNNRwPyMAr7pA5sNs7G-pm3UoOLVnkypisjUPQILWBKVGp8_WjCvXvabj_vMXo7dblZ1qYsHbRpRtehX4Tx-S4o4Y79dwE---g1MWbcaFuOg1rsSf4w4Jvn3dK2srEwJYB035_9kV8AJ5JKVTCwqzCOPKPJrddV1wC4bpuW4XCXa7s5Bc8m9bBUNF3DnJLHU30Vxz9t7P7OxZi7j1gEQUgI5RXO3EynDFnXKbVHXQMHUpZN9SvqBJY7VWyfteNo4P5u_EKh44H7-ZNsOLpSK3N1VIG8GQQtOB-k1q8Y8OQig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/b4DgUyY0TKBX1CPv7tlzh47LIg54HkWWYcPuMJt-AApruNeQAWLlRc7t_IwZNi3ekBsI7uoDml2c2iTzPW2a0aOB5VsVXzDW-cPcy8qVoYGl6UaQpRL2Y0NMRJJr135ohz3S6SksLOCzpJfOAtOUqw0GOjUNZQXpSao53pMm1eOeq-2a2EssaPQHXvVmKNQa0aRXZhVCOMCOuOor7be_MMeL58hJaVQgBdSVFKcLXeQTBqwFB7ZpuYFfwYXErCCb12vrkjX3rb1tmeC2YA2lvBcDqwfIyx8v1wCVUqMAkCrY_hmFeav0kFuI79JzcYWjJlS3desjHTaT5d9J1CNNpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">(موقت)
تنظیمات کلاینت Whitedns اندروید
همراه و رایتل و اپتل و مخابرات
یکی از اعضای عزیزی کانال "ارام " زحمت این کار کشیدید که از ایشون تشکر میکنیم
@whitedns</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/whitedns/612" target="_blank">📅 17:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-611">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/whitedns/611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🛡
مهم: اگر این نسخه رو نصب کنید دیگه دردسر ستاپ کردن MITM و... ندارید!
این نسخه حدودا یک ساعت پیش توسط برنامه‌نویس شیر و خورشید آپدیت شد و به راحتی می‌تونید طبق این آموزش بهش وصل بشید:
1- وارد اپلیکیشن شیر و خورشید(آخرین نسخه که امروز منتشر شده) می‌شید
2- وارد بخش Options میشید از نوار بالا
3- روی More Options کلیک میکنید
4- گزینه‌ی  Connection Protocol رو قرار میدید روی CDN Fronting
5- میرید و عادی کانکت میشید و به راحتی وصل میشه!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/611" target="_blank">📅 16:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-610">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting-14.zip</div>
  <div class="tg-doc-extra">18.3 KB</div>
</div>
<a href="https://t.me/whitedns/610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">☠️
آموزش اتصال رایگان و نامحدود به اینترنت با متد ترکیبی MITM + Psiphon
⚡️
لینک‌های داخلی جهت دانلود: https://guardts.ir/f/db4006f1197c و https://uploadgirl.ir/d/1f4fb76a-c869-494a-b439-b11cb8d35947 (شامل فایلهای V2rayNG، کلاینت شیر و خورشید، ویدئو آموزشی،…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/whitedns/610" target="_blank">📅 16:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-608">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/whitedns/608" target="_blank">📅 15:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-606">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4PhccH1tj2bVBhRO0ky9INtdqKr7JwyQNntPIcFyYgl1wiYWtOC0lKouhw0bATtN81bKmqCiwMtMaNQQhNF7QFbZP9yAK1Ydsi-6WOZ2k3YTztC3g9Pqu1wAiPjawhg39VaK0KTWWWL_KOJ0dFierSIpVKoSSbNxhH_Wqcvw1jDq60OQrIVoaiJIB02V6H2ZpX6wz9AmDbe2i1O2PMvuw2v_Wofuw4lVJinsLok6_RqQoOv0mQIqdBkWYvZ68aqCvfKH8kjjkFJG8LALqRAjUC7JXqHXp4e--UTW2gkBnjq1EDN3j9ELc5cEeFhyXW7tVLwlAkV-PDeRaw_Az5gOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.space
Encryption Key:
bad99364093861634030e96f11fe3132
از همه کانال‌ها و دوستانی که این لیست رو بازنشر می‌کنند خواهش می‌کنیم حداقل سهم و همکاری‌شون این باشه که کانال ما رو به عنوان منبع ذکر کنند. این داده‌ها با زمان، هزینه و اسکن گسترده جمع‌آوری شده، نه با جادو و دعای نیمه‌شب.
این بزرگترین سرور ما هستش. ۱۲ هسته سی‌پی‌يو و ۲۴ گیگ رم.
✈️
هر مشکلی هست، از سمت اختلال شبکه، تنظیمات و ریزالور ها هستش.
@WhiteDNS</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/whitedns/606" target="_blank">📅 09:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-602">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📢
اطلاعیه مهم برای کاربران WhiteDNS
دوستان عزیز،
برای بهبود کیفیت اتصال و افزایش پایداری سرویس، تمام سرورهای فعلی WhiteDNS به‌زودی پاک‌سازی و جایگزین خواهند شد.
✅
سرورهای جدید به‌زودی از طریق همین کانال در اختیار شما قرار می‌گیرند.
تا زمان انتشار سرورهای جدید، لطفاً فقط به سرورهایی متصل شوید کهآدرس آن‌ها
whitedns.shop
نیست.
یعنی فعلاً از اتصال به سرورهای دارای دامنه زیر خودداری کنید:
whitedns.shop
ممنون که همراه ما هستید
🤍
@WhiteDNS</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/whitedns/602" target="_blank">📅 09:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-601">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/i8utipnE_C9IX-1k_gJnEhbOKs2kjC7dwk1hlFpkkJZp6rPekTGTgGLKFzL49zOWjxBw7326ItvqygDe_FyHeWYqIuCpPBNH6pHyySswhj3QzlT6MHdBrskP3VXPXGctGrgBy7JXy561yUpqYhUKxDTGIZ7nnS7zYC_n7zC4rM36yz5DnPLGKIP7BTRQdc9jyhJlQOA4cDH7X721KDJwqJ5FnHb-Qd01ob5tjoRkBW6nAKXNoltU7zwZXiGN4wCarXZcCljp8r1PmVtecJ-MaJ4zUlQyfXzDHZXuS8ZAvmRwv9oRP5XTe8nS8iqukxodcmRuqsD26FErbfFzlg8N-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
به زودی.................
🔥
🔥
🔥
🔥
نسخه ۱.۰.۲ بر پایداری، قابلیت استفاده و تشخیص‌های بسیار قوی‌تر رزولور تمرکز دارد.
🛠
این بروزرسانی مشکل آکاردئون را در بخش تنظیمات پیشرفته اصلاح می‌کند تا بخش‌ها با قابلیت اطمینان بیشتری باز و بسته شوند و چیدمان تنظیمات رفتار سازگارتری داشته باشد. همچنین اسکنر رزولور را با یک حالت اسکن پیشرفته جدید بهبود می‌بخشد که رزولورها را به روشی واقع‌گرایانه‌تر و آگاه به تونل، با استفاده از دامنه فعال تونل آزمایش می‌کند، از جمله بررسی‌های DNS بدون کش، قابلیت EDNS0، یکپارچگی NXDOMAIN، مدیریت زیردامنه‌های تو در تو و جستجوهای پروب به شکل تونل.
🌐
تجربه نتایج اسکن نیز بهبود یافت. اکنون خروجی با اطمینان بیشتری کار می‌کند، مرتب‌سازی به درستی عمل می‌کند و نتایج صادر شده اکنون بهتر با آنچه در رابط کاربری نمایش داده می‌شود مطابقت دارند. جزئیات اضافی اسکن مانند امتیاز، دامنه پروب و قابلیت مشاهده بار EDNS اضافه شد تا رزولورهای قوی‌تر را با دقت بیشتری شناسایی کنید.
📊
✨
@whitedns</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/whitedns/601" target="_blank">📅 08:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-593">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.3.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.2 MB</div>
</div>
<a href="https://t.me/whitedns/593" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
تمرکز اصلی این نسخه روی اسکن Resolverها، مدیریت ساده‌تر پروفایل‌ها و پایدارتر شدن اتصال در خود WhiteDNS بوده است. هدف این بود که کاربران راحت‌تر Resolverهای سالم را پیدا کنند، نتیجه اسکن را ذخیره و دوباره استفاده کنند، و اتصال Proxy یا Full VPN در پس‌زمینه و بعد از قطع‌و‌وصل شدن مطمئن‌تر بماند. در کنار این موارد، امنیت خروجی‌ها، بکاپ و اشتراک‌گذاری فایل‌ها هم بهتر شده است.
✅
نسخه اپلیکیشن به 1.3.0 ارتقا پیدا کرده
✅
بخش جدید Scan برای بررسی و پیدا کردن Resolverهای سالم اضافه شده
✅
حالا می‌توانید فایل Resolver وارد کنید و اپ خودش Resolverهای سالم را جدا کند
✅
نتیجه اسکن به‌صورت خودکار داخل پروفایل‌های Resolver ذخیره می‌شود
✅
می‌توانید نتیجه اسکن را با نام دلخواه به عنوان Resolver Profile جدید ذخیره کنید
✅
Resolverهایی که قبلاً سالم شناخته شده‌اند دوباره بی‌دلیل اسکن نمی‌شوند
✅
امکان توقف اسکن و ادامه دادن آن از همان‌جایی که مانده اضافه شده
✅
سرعت اسکن قابل تنظیم شده تا بین سرعت بیشتر و مصرف باتری کمتر انتخاب کنید
✅
وضعیت اسکن با تعداد کل، سالم، ردشده و میزان پیشرفت واضح‌تر نمایش داده می‌شود
✅
می‌توانید برای اسکن، پروفایل سرور جداگانه انتخاب کنید
✅
اگر پروفایل اسکن سرور یا کلید نداشته باشد، اپ واضح‌تر هشدار می‌دهد
✅
حالت روشن، تاریک و خودکار برای ظاهر اپ اضافه شده
✅
مدیریت پروفایل‌های اتصال، Resolver و تنظیمات پیشرفته مرتب‌تر و راحت‌تر شده
✅
امکان وارد کردن تنظیمات پیشرفته از فایل یا متن TOML اضافه شده
✅
امکان خروجی گرفتن تنظیمات پیشرفته به فایل advanced_settings.toml اضافه شده
✅
خروجی گرفتن و اشتراک‌گذاری فایل‌ها امن‌تر و تمیزتر شده
https://dl.toolschi.com/view.php?f=e15bcec825298e4c.zip
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.3.0
از همراهی و حمایت شما ممنونیم
❤️</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/whitedns/593" target="_blank">📅 06:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-588">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/whitedns/588" target="_blank">📅 18:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-587">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 41K · <a href="https://t.me/whitedns/587" target="_blank">📅 18:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-586">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/whitedns/586" target="_blank">📅 18:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-585">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AsFLX6qczoQ1T-Z7VbiLwt7yPAEzmL57-OhfyLyqMeut9D7uVQC68HLWtGfmbXXDFTJ7Zcz4LLYEBZlNsWycAeMWr4bj5E7hzrLjEE60ShN_cgKrmm7qTHJDcaEow8744eYR9y7WfcG7VkKPzjl6H6UX5DkbkgfzSoACiIVstsAvI1sYysrBSEY4Wl4n90U9e216Ucym4KGVG3u75oZCGIKCfAp4GZmZuDEPx8WEvhwXzEyncdnwK4i7aJUlMzDjJeBDxXOB6EE9e8bfwHb7M26l0k8O_fjHxoPSZges2sBJSI6W0wql1niDBO-KE2krP3tvrld4Zu2SCK8gxj4i4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/whitedns/585" target="_blank">📅 16:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-584">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/whitedns/584" target="_blank">📅 14:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-583">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WwnQIs_o6npp9TKVECz0Q0fY-520ggVZRNUNqeJ3eL9U3m8xfS5bp-v1qQLnjYdOqw3V48xnCIM_NP-98uys6PEQDrv72eyy2P8NsanSmFQmBYqQZwNTzPgrhpHnp1zDdpEpGpkYR3vTqchxej91jyiQzd3l1zAfZOsdRY5xdctJjll6jCwZ7igFrchWNe_hOjYqtQL2tEA0BqivazjDMeoq7pVnH2u4oUrBmA5vmt_ir-gdzTre8IT8z6r4H6AaL8YpAPaFYkWgT14aNd1G20NTSeTTXUCpq1K3b3gH_l9wum_OkM8Z9tW3_y_N_dA79eQWVHQYK3Mdsa92o1cqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/whitedns/583" target="_blank">📅 14:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-582">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMHDIXolzzu7_BExdttX3sE270dvaxgO9HY4bg4mVT0VKdbVwG0ALOa7BI7R1X_vlYScfeiTPNypZ3zoForgK7YQiSQZePmhyqevN4rvtwPzHXkppPmMdQPtjOhcEKwq4OdjkwDGQUzEKunDhDpr8iYNLN6t27ZRwgrabPqFx_x-A1L-HabTcIS32vgaZAqHXGmpAvgYSpSEOrz17wHLNujYSbnEIqrUlQXS09INOt6E99KmxMz947DU0bcIX2qr2P5_DbejUfyyNq-_A85sNnv0O2mLPZn-1blRUY3Ng2WqB3mqsctPV3bTkWmlwV3ymfRCOwX5e0VVfWPHSAQVaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/whitedns/582" target="_blank">📅 10:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-580">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZCzvqt8jSxOeEZRle__V2jm2vbhd6aCtm4sCpj5IyFr_HmPThVv5yb5EIGlGCb-wR72JV1wic9YBfXaIkEcQxzQv95ISc6qQejZ-NqkX4wB7ZfyMGFEc7iRdXmk-KoMX5kq2a6o89APv60VZ3vxOU-NHwxPJ9h18maudYLMuoJmC-bkNp0a_QiQjGHN0Wyfw5778z4Ux3Hadeq8jF5Sawimk4fSD16_SiURcLaVdaAu6iRU6XxeSQamDnx7p1P3wV4Gl8tcEK9XWl285wiJ8VaK9Nyr_PQxvbowIJWDq9vwyXgfqAKojfJjI4aLBcPYYvXRSqIM9I-qKONbAuDRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امکان دانلود کل ریزالور ها به ربات
@dns_resolvers_bot
اضافه شد
@WhiteDNS</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/whitedns/580" target="_blank">📅 05:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-579">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">به دلیل تعویض زیاد سرور ها توسط کاربران، تلگرام ممکنه بخاطر امنیت اکانت شما دستگاه شما رو از روی اکانت logout کنه و دیگه نتونید وارد اکانتتون بشید!
راه‌حل:
1. اکانت تلگرام خود را روی یک گوشی دیگر login کنید تا در صورت logout شدن شما بتونید دوباره به اکانت بازگردید.
2. رمز دو مرحله‌ای اکانت و ایمیل بازیابی را فعال کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/whitedns/579" target="_blank">📅 14:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-578">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVLAU0bsl7vsocoPS1Eo2ozXSw-yxykxY6p0IAzU40dsJkx33wwBkgIjukHenQfNNykvHy0kmyq2Yz_aDDAjYIdNHxHSbrjJqW86bwOyZZf_ekaZh6ghlN1nFuIEoN_mK1S3IK24mNi2LPzqxo4xPg-0Qc-UXDEPMJlmvnXNG5x5QtdTiUEbrw8gDjOb940oHpQoKReZrvssnsKVl-v3agzdvmvRl6-KfRFyvVkmRscR6yBhxEkSXNY_XNMp_rK1fl5vOFz2ldm8FoKa-Pj8Kze9BQefhZnxwV70PsgVzweAdGqstbnobvY4l0O6fk0CxoV8V7KkUtOzkg89nhbZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
‏فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
‏ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام ⁧
#اینترنت_پرو
⁩ را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
‏ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
منبع
https://x.com/ircfspace/status/2054094958353678824?s=46</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/whitedns/578" target="_blank">📅 12:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-577">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-poll">
<h4>📊 آیا به اپ WhiteDNS تونستید وصل بشید؟</h4>
<ul>
<li>✓ آره</li>
<li>✓ نه</li>
</ul>
</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/whitedns/577" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-575">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmxN8ljNmNa2czb5wRByt1gbgA7iR-QpaU5fY_3n5fX8t1tvjPMS73haeWOmWnaACjQP1-et9GLtZUX9iC6KTsH0q-VCG2zYaU56jQcpqPt7d2eF1MxKceH5pRm9VePnEd3PYdYx5Nzrx13WB8WoNtsLMMcwyIZ7hKjozs5trdpEWXMe9KyDU3RMFNMkz7M1FC0DloZHJ05ZS6zjJ0hwHugxE6MVXahIXmksz-UVgEbrh8FmrYn3splL_fusI8rlomi2EMXTWFf2nohj663uhWS1hMLvySKVLQB3h4UBo48jy7_QnHNzHJthiUOY7j3dmeznrSUaI4AX3J00_EetYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/whitedns/575" target="_blank">📅 10:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-574">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
سرور اهدایی از چنل
@Masir_Sefid
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigxKSIsInNlcnZlciI6eyJkb21haW4iOiJzLm80cy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigyKSIsInNlcnZlciI6eyJkb21haW4iOiJzMi5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigzKSIsInNlcnZlciI6eyJkb21haW4iOiJzMy5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig0KSIsInNlcnZlciI6eyJkb21haW4iOiJzNC5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig1KSIsInNlcnZlciI6eyJkb21haW4iOiJzNS5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
@WhiteDNS</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/whitedns/574" target="_blank">📅 09:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-573">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">White DNS
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/whitedns/573" target="_blank">📅 09:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-572">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9ad3f5766c.mp4?token=s9sgeWcCQy--DRZgIhrzBfnO6kdOBi_KrTwGNBOrB68Fm1hQ6GVUiB2bqd-1P_E3iPN0Ruix6z5rCTi6pVE0M_kMZ4lHoBDHM1RP95mdMnv2Dz__wNtxvz4hQq78Cm2sp6CRoPcoZNF42tV53i997gyXz-xViw5OHEBpr9uMIMq16-Qv9UqC4gL8lvqwcBBHz8K-6N7q8fDo5lJDmYMRqGIAhGWva3B7X-GKK-XOa2Wbfd2Ai_T7OliOuysxtTZ511AtAEYeP9ydgRPKZa6Z4jgtgGR176rf6LXdhBh-QfrxG3IcsyoYWDf6-TZlj0rVdprbjVwMxV-497knu27m1w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9ad3f5766c.mp4?token=s9sgeWcCQy--DRZgIhrzBfnO6kdOBi_KrTwGNBOrB68Fm1hQ6GVUiB2bqd-1P_E3iPN0Ruix6z5rCTi6pVE0M_kMZ4lHoBDHM1RP95mdMnv2Dz__wNtxvz4hQq78Cm2sp6CRoPcoZNF42tV53i997gyXz-xViw5OHEBpr9uMIMq16-Qv9UqC4gL8lvqwcBBHz8K-6N7q8fDo5lJDmYMRqGIAhGWva3B7X-GKK-XOa2Wbfd2Ai_T7OliOuysxtTZ511AtAEYeP9ydgRPKZa6Z4jgtgGR176rf6LXdhBh-QfrxG3IcsyoYWDf6-TZlj0rVdprbjVwMxV-497knu27m1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/whitedns/572" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-567">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/whitedns/567" target="_blank">📅 06:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-565">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/whitedns/565" target="_blank">📅 14:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-564">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/whitedns/564" target="_blank">📅 12:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-562">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/whitedns/562" target="_blank">📅 10:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-561">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTi60apw8AEuCSi13K2-0sOzyfBDO_fVP7WHZAUIFnGiCXPKNAksDucNKJMVt9fJdn7yDgnqTjYHTf-IBubKDoQ1o5nGSYs1Hf4UOVAY8lmZI4LfAaYmKwQ8FipzbycvEMKNpfCENrVLpi1AJwyLQ5xJinTF134OZzw3-31ax8YrS-fM-KV2g20iH3dTdsP9p4yNb3YSqNObx7uT6ynZlhCaZULse08d-I2msg6aCiDsU7bDveEX57DAvNxFyDTSJi4h11lT7TTbcO2K2sC-m9DNwApZBd813nxuAItkg43t5QFuIh5dUU9YWl6R9gl7lpU9MZo-jqywRCDvnp5wDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/561" target="_blank">📅 09:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-556">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/whitedns/556" target="_blank">📅 06:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-553">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNxllFpoj3js2PnoYuMmcAzdY6M_vkyyc1GFJG-BCJ9xpE7IBQpoWuhFhdVz4fZJh1KXePXgGXxduxtkAgf4V-leM0bHJvzla88XYFfHxE7r3Nxb6ImfY2XqjyrdVIrBKo-sv2EaAymwvmtwBQ2TOLqMxSVKgGKQSV_5AEiENIHDqhF5LnCR8Xl-1vurC966pv2DZgkQyrVKAv0sALvHLvn87jzbg1hjxSMCKJD_4NkncnEicnSPcv_1WQPi0l8n2MncFcjTNlsDmw2o0_2rhHHn-m98w-dFT7O29oU-rGV9GE_Fap3xxMBfzTee7fli0r5EgbMLPLHhFGmDDKBKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام سرور هایی که داخل اپ بودن داخل تاپیک سرور این گروه هستند. لطفا عضو بشید و گفت و گو ها اصلی رو اونجا ادامه بدید.
1⃣
t.me/whitedns_group</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/whitedns/553" target="_blank">📅 15:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-552">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoaSMvk0t1RRVleU1m-EbNlkcvngig0aYkIyDKc2I7WGE8GpM5uOcglGNiRBj9Mci8gvOzmWY_CbzHVFNwPfph3HV1m75RziPHYRuWqFjIxV_U0IWq4xzYYkdc2Th7MXdyE8vWD_htCsY_f8QyCRhJtCtRXDXL4YMAyXa8LjqmQznGWKGFKUEkyk8qycv92yOiDbLZYMbZ6CXHGwi8BSb_CDiyhET9KxeFtDXBuWJ7LkHxHMBC9HP1t7BKaIsOkpJC27UJZ0nAmvw-DidR_QOVYQ1bq5BieRwwQla6nvOFdiqqTDZwIJ8UTlo8Euh6ybY5n1Tc3ff-a0M_GWT5yhEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/whitedns/552" target="_blank">📅 15:33 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
