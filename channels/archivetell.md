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
<img src="https://cdn4.telesco.pe/file/qONBb2GlmMX-iD2P1oV46P-1ZMm_88oS-RAaDECW3XL1Gzb8r7UZrbqTg87Tfj3BtAfLyYzmoS55WCdsXcVrUSAXBSAYEJ3-ARawWVXA88Z2n8ecYXWTzIT4vDCV_MRo8G7HgwDnaeyA5H55heQVG6kCYFBlGAoyadI2PuFCW0D3qWldycdJsqoIY0QzG1F64mAAy1Mz_xJuq2d2pxPNJ2Oi8sfpopJdZAgZmFTNiKOzz_xTLb8ZWMs7vfYUNFYJdxg_IPaqUlKua1mAzHZqFrKmnM8K3gAINK8viF5xq9P01VrnAex3lIG4JewPEIAqvPmjcjWDz1vJh7v2BGK21g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.6K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 00:43:33</div>
<hr>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 708 · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 737 · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUz1-np2DAfyP8zrWDvw3UGyoscPmMpYAtifLkhR-N--4BKOMb9C3DKpo6tIxQUc71HdApU9GEePW7zL9lcKkmYozT3vMP6cX7JtfjxqIwkBlYjpJf4yHyFWx-n31LUF1_DZTWbfVjIkHO_3L1EYCPAwiPJCeEtME5kPdTlERsnb0iwLGyT2zAUHGM7gybQtM8vmyL2lHO3aSpzeNANsjt35Pq3Hxn9W5kcf7MKpDSwG8USsWcNpgCjNZ9h0p4FcHhyWWu1BjeKzYCEJKEvy2E5VAZFGgk-i58gfTAc9vxlbNpdLp63abTNRZxaMvFsB4LSRMaUn8QLzF22A8HOMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 787 · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📢
جدیدترین قابلیت‌های
ربات وگا
را معرفی می‌کنیم:
📚
حل سوالات درسی در پیوی
🔸️
در بخش سرویس های هوشمند
🔹
امکان ارسال عکس سوال
🔹
جستجو در منابع آنلاین
📝
خلاصه خودکار موضوعات گروه
🔹
هر شب ساعت 21:30 ارسال شدن خلاصه مهم‌ترین مباحث در تمامی گروه ها
🌐
بهبود سیستم جستجوی وب
🔹
نتایج بسیار دقیق‌تر و معتبرتر
🔹
دسترسی به اطلاعات به‌روز تر
📰
آخرین اخبار هوشمند
🔹
هر ۸ ساعت بروزرسانی می‌شود
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
⚡️
Vega Bot
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEAdbwhkV9_wWrEzve7SAuc9r5bT8xMQSQEkoXqKPq7J8cXxJCqSpClphcC99I-ya4OU2mJZUdibDFKheSHiuQrVECsM42HL35h_2-dex9Td07ClRZRkGdIsMKSyV0WtGfbNB_EVSy9J8o6OmlRFsrOkYTiMMY4GyoTWXawS35ZJA4x9jXOLCqIM2lnPImJ1VwOi2roz5UPrickivQgjOfGdJHFnTKJmcizK4azVmakrU6dx4qGY1T9np0b7XQT5Cf3QDUAKx6haZp18mS4snN09iKnln_RTpXqo8gVqrbE3yccl7T0_lbbUR5tNnyehGDtQwVDeZ61OgDBro-tKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
OpenAI برای برخی کاربران API Credits رایگان ارائه می‌کند
اگر از APIهای OpenAI استفاده می‌کنید، می‌توانید با فعال کردن اشتراک‌گذاری داده‌ها برای بهبود مدل‌ها، به سهمیه و اعتبار رایگان دسترسی پیدا کنید.
📌
مزایا:
• سهمیه روزانه برای GPT-5.5 و مدل‌های Mini
• اعتبار رایگان API برای حساب‌های واجد شرایط
• دسترسی مقرون‌به‌صرفه‌تر به مدل‌های هوش مصنوعی
⚠️
توجه:
با فعال‌سازی این گزینه، بخشی از داده‌های ارسالی شما ممکن است برای آموزش و بهبود مدل‌ها استفاده شود. برای پروژه‌های حساس یا حاوی اطلاعات محرمانه، قبل از فعال‌سازی شرایط را به‌دقت بررسی کنید.
مسیر فعال‌سازی:
OpenAI Platform → Data Controls → Sharing
#OpenAI
#API
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=V9dTzqrYBNPhCYgfXk8vwes6q6NwMt7-87jmQHICj3DtNPXsNFLSOz3nM3pbjjtseK_kbbc_oBgfRFBu_1SCX4afbDgAFIMvfhDZqhFTLBOJn61QuMO-mlmg3M7wK4o8hcjz9BEZm2weOl1ydbAvV6DUwo-koptJTVAjC48qUeN5y7Xx8khOg6NSoarCDkzJf9P6ocescX05HiBn49fy2nM-x_lcgiYMO_xnrU7ZpRvnGH_1FW_aH8UBxwk_3TZCUB2JPRgkvKcBdHpTVgAZv1P_xA6eUvVYCHqgoZyNTlHMXjUC1JZz5lh8uAB-nZ7-a0-LMDEhM3OLKpCDSEdjIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=V9dTzqrYBNPhCYgfXk8vwes6q6NwMt7-87jmQHICj3DtNPXsNFLSOz3nM3pbjjtseK_kbbc_oBgfRFBu_1SCX4afbDgAFIMvfhDZqhFTLBOJn61QuMO-mlmg3M7wK4o8hcjz9BEZm2weOl1ydbAvV6DUwo-koptJTVAjC48qUeN5y7Xx8khOg6NSoarCDkzJf9P6ocescX05HiBn49fy2nM-x_lcgiYMO_xnrU7ZpRvnGH_1FW_aH8UBxwk_3TZCUB2JPRgkvKcBdHpTVgAZv1P_xA6eUvVYCHqgoZyNTlHMXjUC1JZz5lh8uAB-nZ7-a0-LMDEhM3OLKpCDSEdjIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی ۱۹۷۸ ایران، فقط یک تیم فوتبال نبود؛ نماد غرور، اتحاد و جسارت یک ملت بود نسلی که برای اولین‌بار نام ایران را در جام جهانی طنین‌انداز کرد و نشان داد که می‌توان در برابر بزرگان ایستاد.
از ملبورن تا آرژانتین، از صعود تاریخی تا تساوی مقابل اسکاتلند، این تیم برای همیشه در قلب تاریخ فوتبال ایران جاودانه شد
❤️
یادگاری از دورانی که فوتبال، فراتر از بازی بود، یک رؤیای ملی
✨
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6297" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsZYAzSWhF-ezMG01Gc-oG99UrJBsm3B9ZStBwbqMo1ZiA7d_6zyZx6fdc38kWv241oF4BqsLQT5oQTEcyXCAZlfqa2vP9WGPFrwpWon8H9Ar62WsISA3rhwucUCq9LqQqDhAK1SAuABqjYhUI_Uut5toNzWSKkatA3OTda6F5iJdSeXqwgaQvA90Ji-fu01zKqff3rDGN7f-hoSgZv0O0L09V4swNKlmOna5GDnDgmvqOw0giUhku1Az7wp4GMBgh7tsuAlbHBp-May84vg4F5dPCGFrmQG6MnNilhzwCN8phoenfZ05-ayx5n5uiNw5AfnVZDvYooDPKFyyb3oGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
RuView
با استفاده از سیگنال‌های وای فای، بدون دوربین یا حسگر، موقعیت و علائم حیاتی افراد را حتی پشت دیوارها تشخیص می‌دهد!
✨
قابلیت‌ها:
•
🔹
ردیابی ۱۷ نقطه از بدن انسان
•
⚡
خواندن تنفس (۶‑۳۰ نفس/دقیقه)
•
🛠️
اندازه‌گیری ضربان قلب از راه دور (۴۰‑۱۲۰ bpm)
•
📦
دیدن افراد تا ۵ متر پشت موانع و ردیابی همزمان چند نفر
🔗
لینک:
https://github.com/ruvnet/RuView
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌐
Javid Mask | ابزار افزایش حریم خصوصی برای کاربران استارلینک
اگر از استارلینک استفاده می‌کنید و به دنبال راهی برای مدیریت بهتر ترافیک شبکه، فیلتر کردن دامنه‌های ناخواسته و افزایش حریم خصوصی هستید، پروژه متن‌باز
Javid Mask
می‌تواند گزینه جالبی باشد.
✨
امکانات اصلی:
• محافظت از حریم خصوصی و کاهش نشت اطلاعات شبکه
• فیلتر کردن دامنه‌ها و وب‌سایت‌های ناخواسته
• راه‌اندازی ساده روی سیستم‌های لینوکسی
• پشتیبانی از Raspberry Pi (از جمله Raspberry Pi 5)
• دریافت به‌روزرسانی‌های جدید از طریق پروژه متن‌باز
📋
پیش‌نیازها:
• سیستم‌عامل Linux
• حداقل ۵۱۲ مگابایت رم
• حدود ۱۰۰ مگابایت فضای خالی
⚙️
راه‌اندازی:
1️⃣
سورس پروژه را دریافت کنید:
git clone https://github.com/rowdy-ff/javid-mask.git
cd javid-mask
2️⃣
فایل‌ها را بررسی و دستورات نصب موجود در پروژه را اجرا کنید.
3️⃣
پس از نصب، تنظیمات موردنیاز را اعمال کرده و دامنه‌های دلخواه خود را برای فیلتر یا مدیریت شبکه مشخص کنید.
💡
این پروژه بیشتر برای کاربران استارلینک در ایران طراحی شده و هدف آن بهبود کنترل شبکه و افزایش حریم خصوصی است.
⭐
متن‌باز و رایگان
🔗
GitHub: rowdy-ff/javid-mask
#Starlink
#Privacy
#Linux
#OpenSource
#ArchiveTell
⚠️
قبل از پیاده سازی و نصب، لطفا کد منبع رو بررسی کنید.
چنل ما هیچ تعهدی در قبال این پروژه ندارد.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n49BAMwRbDsZJqAVtou4f0alkTvV3gThExWzPIVPjBqpezWXz8newJlaj8LQSjqUCYBz1H-dS7H2JtspLagY-2Gj1jvC8lcBGVuwh_PUKOBHNsbzyDSL3iKjl2m1FAeZhFs3boXxejoMR13w59mxn_n0fhX3vjqiauakiA4W_S0HzNhBTqvVyg3opTHLZzmvoMloWQS63cQgR3N74wD51--VwxXrF1eMV1wep1PmhNUd3iselrtN14P6OZ5TKVjDMbl-x3yB_N4D_ZcMTRn89mQuyollEXu7CY8DdgIQ_65ICGwqWkw9aEEwLXTkePepap2VXU8-NE7DAonSS4vmFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q2Nsi7i-V8kAQxI4SMOHqPKj_c054ghaxTj0siNBmn0xTjrSRulS2j4MQmQdktaTi2movZ4zVR_4jgCbFRybAqeB6cpyVtQhaEsf11qdQbODTV1BU-Kri1kHfPBLev8_fohHd79Ahtt3xaFzKgm1MV8-n5yuDEKraGxIZtECXNLhYteWSsSR2Ba-ZOaKgjqB-cF4EOCGESln3DO74X6OSzSW25_1B5R-cbgO948WnNatLD1p_CgjaFyrWRx-0AItYz1MNA37cHFDstp3aZfoxR3ueT_0iCN_x2k3C0kfENXR-aFr_YiDpagKS-4LVatyx8TpUSPQO6_nO4TJwbh-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMyrUuh-LQZl0c2vkEzlr4lxRTxvo4r9oIVBANS70uDxR6CIB6bS2mi6wuK9QgIdBdJiBXdqcs77cDOpqpTL2iw1F1ttzMgdB-HXiwHVqK90hFV2t4zEa8eV8QjTBDqs3ApZKMcPBXlIuXhlb_pfR5nRfOOHREV33zRCz45B0EToDzitsyaC6TpE5cyDk4URZDAz10vV729pNcr0I2jld-Eb7erSRuO84aSYjsi7x88B1hcqqbXNA0rs97y_HxqJrlCbHG7UkBgmzKSv9oQSYnH6QIxuB4iZpo0_PdhRSv7b5xjrw0hwctYOu0X_gt6hcO-XeVcc3OWZm4FYLM9sGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
شیائومی MiMo Code: مدل جدید هوش مصنوعی برای برنامه‌نویسان، با هدف پیشی گرفتن از Claude Code.
✨
قابلیت‌ها:
•
🔹
کار با پروژه‌های میلیون‌ها خط کد بدون محدودیت
•
⚡
پردازش مخازن بزرگ بدون از دست دادن داده‌ها
•
🛠️
آموزش مجدد مدل در حین کار روی پروژه
•
📦
تمام این‌ها به‌صورت رایگان و متن‌باز
🔗
لینک:
https://mimo.xiaomi.com/coder
#OpenSource
#Xiaomi
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=D-MZPSYv6-HW9JLassoioJEKjuz6LUMgQfM8FM_Q5egACrQNw14HWl1NjZNF309Zftg0vDUsr9b9Aa4xsadiiTewHinxsKPM9Jp2IIifofvp4PJoCvbg125OiNPuOMv2i1vTxwl-KPQ4uQSRiMVJ87BAeDsNrlkvZPP7m55RJp8tKL_XWLSBU7Mc7QjmVF-iNI3xEwS2RNQPPAA2l5jkrkhMl46mAYtV6nxFg-fkEHV0g1VLA0M7UNg_cWqN53i8BkQGtZim9j5MKdC_uIre4tpdvE30tTw1AUeiQDlYadrfF-CHnxoWdg4hLLoa7eFhZwtFoXBU35Mz_vst9kZaZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=D-MZPSYv6-HW9JLassoioJEKjuz6LUMgQfM8FM_Q5egACrQNw14HWl1NjZNF309Zftg0vDUsr9b9Aa4xsadiiTewHinxsKPM9Jp2IIifofvp4PJoCvbg125OiNPuOMv2i1vTxwl-KPQ4uQSRiMVJ87BAeDsNrlkvZPP7m55RJp8tKL_XWLSBU7Mc7QjmVF-iNI3xEwS2RNQPPAA2l5jkrkhMl46mAYtV6nxFg-fkEHV0g1VLA0M7UNg_cWqN53i8BkQGtZim9j5MKdC_uIre4tpdvE30tTw1AUeiQDlYadrfF-CHnxoWdg4hLLoa7eFhZwtFoXBU35Mz_vst9kZaZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
Every‑PDF
ویرایشگر رایگان PDF با پردازش محلی و بدون ارسال به فضای ابری
✨
قابلیت‌ها:
•
🔹
افزودن متن، امضا، تصویر و واترمارک
•
⚡
تقسیم، ادغام و تغییر ترتیب صفحات
•
🛠️
رمزگذاری
•
📦
کار با فایل‌های بزرگ به‌سرعت
🔗
لینک:
https://github.com/DDULDDUCK/every-pdf
#OpenSource
#PDF
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📊
خلاصه یک سال فعالیت گیت‌هاب در چند ثانیه!
توسعه‌دهنده‌ای با نام
PankajKumardev
ابزار جالبی به نام
GitStory
ساخته که فعالیت‌های سالانه کاربران GitHub را به شکل کارت‌های آماری و قابل اشتراک‌گذاری نمایش می‌دهد.
🔹
کافی است نام کاربری GitHub را وارد کنید.
🔹
سرویس اطلاعات عمومی پروفایل را جمع‌آوری می‌کند.
🔹
سپس آمارهایی مثل تعداد کامیت‌ها، ریپازیتوری‌ها، مشارکت‌ها و فعالیت‌های سالانه را در قالب کارت‌های گرافیکی نمایش می‌دهد.
﻿
💡
اگر توسعه‌دهنده هستید یا می‌خواهید نگاهی سریع به عملکرد یک سال گذشته خود در گیت‌هاب داشته باشید، GitStory ابزار جالبی برای بررسی و اشتراک‌گذاری دستاوردهایتان است.
https://github.com/pankajkumardev/gitstory-2025
#GitHub
#Developers
#OpenSource
#Tools
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚀
دریافت ۲۵۰ دلار کریدیت رایگان برای API
اگر دنبال دسترسی رایگان به مدل‌های زیر هستید، می‌تونید با Agent Router API Key اختصاصی بگیرید
👇
🖋️
Claude Opus 4.6
🧠
Deepseek v4 pro
⚡
GLM 5.1
📌
مراحل فعال‌سازی:
1⃣
وارد سایت
Agent Router
شوید
2️⃣
اگر سایت به زبان چینی بود، از بالا سمت راست
🔝
زبان را به English تغییر دهید
🇺🇸
3️⃣
روی Sign up بزنید و با حساب GitHub وارد شوید
🐱
4️⃣
وارد بخش API KEYS شوید
🔑
5️⃣
یک API Key جدید بسازید
➕
6️⃣
طبق راهنمای این سایت، از کلید ساخته‌شده برای اتصال API استفاده کنید
⚙️
💡
با این API می‌توانید:
🤖
ربات تلگرام بسازید
🌐
وب‌سایت طراحی کنید
⚡
ابزارهای اتوماسیون ایجاد کنید
💻
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت عالی برای تست مدل‌ها بدون پرداخت هزینه
💰
﻿
@Archivetell
✨</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=jMgnJfIbe09kinAVPj1Xbfgfz0FllYksXyeAZf76WVbNC17_IXgWcAjSt4CfNljnAG1GSHhNkhFlMDnPInelLjzBogRFUOUbF65KPlzS8krSKtOpt8hEjBRwgVwl0kShW5FP2d1-anVGFsFIa7zcN5lyPao60TsxdeEluvq7Qpimi65_Fey2aJmV7byWJlew_XS2J3vHms7P7Bp0B1HcPx23NxP3MmjVFwefh2xHA94MNKImwS_Z7JSorf8G_46VE04mXS3v6v3y_TBQJFxZ4RomcDo0f1RQaCmoTuIFs6QmelqJT-a-cNMoM_cuy0z3NrehpRuL0tQsHiUsYNYMzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=jMgnJfIbe09kinAVPj1Xbfgfz0FllYksXyeAZf76WVbNC17_IXgWcAjSt4CfNljnAG1GSHhNkhFlMDnPInelLjzBogRFUOUbF65KPlzS8krSKtOpt8hEjBRwgVwl0kShW5FP2d1-anVGFsFIa7zcN5lyPao60TsxdeEluvq7Qpimi65_Fey2aJmV7byWJlew_XS2J3vHms7P7Bp0B1HcPx23NxP3MmjVFwefh2xHA94MNKImwS_Z7JSorf8G_46VE04mXS3v6v3y_TBQJFxZ4RomcDo0f1RQaCmoTuIFs6QmelqJT-a-cNMoM_cuy0z3NrehpRuL0tQsHiUsYNYMzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
OpenAI
تا ۵۰ هزار دلار اعتبار رایگان API میده!
🎉
•
🔹
۲۵۰ هزار توکن در روز برای GPT-5.5
•
⚡️
۲.۵ میلیون توکن در روز برای مینی‌مدل‌ها
•
🛠️
تا ۱۰ میلیون توکن در روز در سطوح ۳ تا ۵
•
💥
در عوض، داده‌های شما برای آموزش مدل‌ها استفاده خواهد شد.
📦
این ویژگی برای همه فعال نمی‌شود، اما ارزش امتحان کردن دارد — وارد OpenAI Platform شوید، Data Controls را باز کنید و به بخش Sharing بروید.
🔗
لینک:
https://platform.openai.com/
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3JZIRE1RLVNckL6I-n5IL6alp26IFY-954mTQtCRQVd54Bil_vddMkNUggHrSX3PL71GuWo66xgYagjovoPmgAh5tiSmbJmZkSJJFiD05CWBy8tpWoKeJbKUYhMD0kvd6M6Nvh3M9K-0CfNuxr6CMPgkf68w9XTnhUTrwEMgjOJTEe_edYCHbDMcBF8nqC_ItDoNyEcqsrYPquJ0a78Rvwlu8BWm2FP3_nvp0v6wTIPj9wVw3Z9F8jc22MtXDyfOrA4liKyweszCsss_OFV41NXsBwDQjteNxhjBJ1TI_smhgFEGHyf1iKsKh6fXfZr6ZWotfjyKYkCT913AwJabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
BrowseryTools
مرورگر خود را به یک جعبه‌ابزار قدرتمند تبدیل کنید! 136 ابزار رایگان برای فایل، رسانه و هوش مصنوعی، همه در سمت کلاینت.
✨
قابلیت‌ها:
•
🔹
ویرایش تصویر و ویدئو بدون نصب
•
⚡
مبدل‌های فایل سریع و آنلاین
•
🛠️
ابزارهای توسعه‌دهنده با Next.js + TypeScript
•
📦
هوش مصنوعی محلی: رونویسی، ترجمه، حذف پس‌زمینه با Transformers.js
•
🌐
متن‌باز و قابل میزبانی مستقل
🔗
لینک:
https://github.com/aghyad97/browserytools
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=rsnFdIbQ7EdUW4SriP8UxysERPj82vv61oCmIWG49QZiZLpzKYH9PphtVFC9gImmtZQ_gjg5YtNQrDid1Gno8e9SaN68DCjw-qt2u1IDRxDxRDD3CX_KwqIhw42iANtE5QyuQNZ7xGsfKw9npQaRwjXG9blSkeoUg_X3o23-SvY8xe4suXf2fohJ9vPZY0f25nuwWZDYclSG1x1Dp8qyxm26ckyrxf40eiDBGbRvrn88POlIr9jPoPB5jDMS7OUuZCCfqErO2AwAAtKLA42vgwqjpTJ8Jls-Qnpgk21Ib5pNLxEdwrTZtuiQg4BSm_Z6l39KMA6aUerd2h48NgKV0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=rsnFdIbQ7EdUW4SriP8UxysERPj82vv61oCmIWG49QZiZLpzKYH9PphtVFC9gImmtZQ_gjg5YtNQrDid1Gno8e9SaN68DCjw-qt2u1IDRxDxRDD3CX_KwqIhw42iANtE5QyuQNZ7xGsfKw9npQaRwjXG9blSkeoUg_X3o23-SvY8xe4suXf2fohJ9vPZY0f25nuwWZDYclSG1x1Dp8qyxm26ckyrxf40eiDBGbRvrn88POlIr9jPoPB5jDMS7OUuZCCfqErO2AwAAtKLA42vgwqjpTJ8Jls-Qnpgk21Ib5pNLxEdwrTZtuiQg4BSm_Z6l39KMA6aUerd2h48NgKV0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
افزونه ImageToPrompt تصویر شما را در چند ثانیه تحلیل می‌کنه و یک پرامپت آماده برای مدل‌های تولید تصویر می‌سازه.
✨
قابلیت‌ها:
•
🔹
تشخیص سبک، اشیاء، نورپردازی و ترکیب‌بندی
•
⚡
تولید پرامپت دقیق برای Stable Diffusion، DALL‑E و …
•
🛠️
بدون نیاز به ثبت‌نام یا حساب کاربری
🔗
لینک:
https://chromewebstore.google.com/detail/ImageToPrompt/pgabcjhpgdcgbflabemecpficpknnpfn
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt-H7owtya1EUVM7_UiAaPX2d2OqGoT4UhBE5bHw5A14XnuKlIdtORwtiZfGK8Vt2k-tQac_N1Wd_rtFAY2TyKM1UfDPc6mB7F5Tnu2X3Sv5zVYFpDalkc36WPujM5OIrCQIcdVhlLaLuQW8skDuFzdWlZoGFFU6LuxshLN8v-se8MdTl4cm3IbXVNaSb2I51wHJVbvshxZpk0La5ihWJvIRkrFoSmcIsG8pjP1UeosjYz3Xr0eO8aBuAbvJlQ3XMLiXMR8nVH8tLjK_Roc4jnWxFALvClVXyJ8bxVxbmvo5MCLqg0dVvFE4SVjB9VrL5UwAH3QnphBBwQCzqKgErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتقال فایل سریع و پایدار بین دستگاه‌ها با قابلیت ادامه‌دادن پس از قطع
✨
قابلیت‌ها:
•
🔹
انتقال همزمان بین چند دستگاه
•
⚡
ادامه‌دادن خودکار پس از قطع ارتباط
•
🛠️
سازگاری با شبکه‌های پیچیده و متغیر
•
📦
انتقال تطبیقی برای بهینه‌سازی سرعت
🔗
https://shrimpsend.com
دانلود فایل مخصوص ویندوز ، مک و اندروید :
https://github.com/shrimpsend/shrimpsend/releases
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zj1RpKtqk7sKEcEi0Y1GtATFdk2JNaoXaDHJkGN6-yj7ogeqR1UKa8pRxzxqgtsmhc_4V3NmmA48eCzpd3HIDyrOYZutbXFJg4-gMbbLMIgIPQUrpNcjPvHk8islQlqn6vAN9Hlw_-Hw3ehfY3GcmQ2ftRtTcPe9aP9BzdN3QZ3FrFIG4sJ6wUJc4ggKrMZ9NamUZWsOxqakiH-YFgbgoRmyqczvr1AueMG_FMUzKKRGXqzgrniUlzX_mrTWA3bx1JfRxU9JA1dyIn6VEQnavL9YUkFgtxNcnHqRi7xFFxQmOSjmIwYX44C_nJLsUtgof_ol_d4VD8vYVwO01RyXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=M7joD3iLYAe3PIyECkM94VFXkC4YiqpSn57lp64O1tXz-Hu-ieTnCGvGh0FW6ZAGqFxxNKPN5jU3GY79CgNH9JnykNfhFG1Ch6kyuNTRfB5rp5505z5EC3peRacLNDdtGhWbijfxipI3Oh9K2E5iUaoqeHgNeg9QCAVWGRP73_BF6i_dYEOilJLH06oPGalqbXZ86C651u9_IuLDbKR-jCber0_jxMRmwEbe5E57rqurj0-nBWStpJ-CYOFvAi07Oxwl396GQ9XadLfu5S0BTEH0bkr8CAzQ-0vRMfwhIdHTHmtfrMsFWLYwmyR4yzJGd_yBQBvui1emGymHNnjfKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=M7joD3iLYAe3PIyECkM94VFXkC4YiqpSn57lp64O1tXz-Hu-ieTnCGvGh0FW6ZAGqFxxNKPN5jU3GY79CgNH9JnykNfhFG1Ch6kyuNTRfB5rp5505z5EC3peRacLNDdtGhWbijfxipI3Oh9K2E5iUaoqeHgNeg9QCAVWGRP73_BF6i_dYEOilJLH06oPGalqbXZ86C651u9_IuLDbKR-jCber0_jxMRmwEbe5E57rqurj0-nBWStpJ-CYOFvAi07Oxwl396GQ9XadLfu5S0BTEH0bkr8CAzQ-0vRMfwhIdHTHmtfrMsFWLYwmyR4yzJGd_yBQBvui1emGymHNnjfKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=R2KFvMNhn5VBlZqyspYo6B0tqSwdA-SIh6yXyRCdj6c1dPcw2Ry6cka0kcmZWnHirUUzuJxFfsEmR6fVfIloXJSpRDWf_94I78gMEAcKfsDpD3kS4AZbreX-N18TMDyzLhDfw7eRtpkS19pbZV6k1bOe75CvlVANANWhOJG1vk68VRUdzCAbtCQV4VOUsJhDRdSOt2jp-u5W39mK8_7NSR27bPG2bOEgUvby4UEXbRySVmrXJ8hgzBf5Am9pRT15DI6D2NhE39NSxiZBMoVcjFpkgNIhZ2M9hk4-fjeszYNGLVLA-3Jy40vOuV4EDAXysDh7hjP3mua0uVR6WX0nnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=R2KFvMNhn5VBlZqyspYo6B0tqSwdA-SIh6yXyRCdj6c1dPcw2Ry6cka0kcmZWnHirUUzuJxFfsEmR6fVfIloXJSpRDWf_94I78gMEAcKfsDpD3kS4AZbreX-N18TMDyzLhDfw7eRtpkS19pbZV6k1bOe75CvlVANANWhOJG1vk68VRUdzCAbtCQV4VOUsJhDRdSOt2jp-u5W39mK8_7NSR27bPG2bOEgUvby4UEXbRySVmrXJ8hgzBf5Am9pRT15DI6D2NhE39NSxiZBMoVcjFpkgNIhZ2M9hk4-fjeszYNGLVLA-3Jy40vOuV4EDAXysDh7hjP3mua0uVR6WX0nnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=Fd5sJJjllUUtUNqvqxDrMFz-TuNqGp-9BCD3jLEFCoKmZKhvERbjeu9KtVSll7XqzpZeGjma4nooyC9ockQ2HMiCGKm0aXQVJXg_aWYWLZpgn72zF0a-DFtKBrD53q4l9zLCyl1OHBHlNJ0aJYjgUJMdrxCjPaRGT4A5FPJ27WXmmawaPUUxT22vkzeTr_8n3aP3GxnI7VI2hD0hgMSdvQEFy7z04V3Tan2T_vWQA6BZTW4HaCQfmnODv5YtRIvJ93EHi9-jFwEzTB2iGLi8PuI9LQ94FjULi_mrxzqEB4H2yLbZDQWIUFqEgZcbdnvjC0CEkwuhSkgTnr8zVUchJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=Fd5sJJjllUUtUNqvqxDrMFz-TuNqGp-9BCD3jLEFCoKmZKhvERbjeu9KtVSll7XqzpZeGjma4nooyC9ockQ2HMiCGKm0aXQVJXg_aWYWLZpgn72zF0a-DFtKBrD53q4l9zLCyl1OHBHlNJ0aJYjgUJMdrxCjPaRGT4A5FPJ27WXmmawaPUUxT22vkzeTr_8n3aP3GxnI7VI2hD0hgMSdvQEFy7z04V3Tan2T_vWQA6BZTW4HaCQfmnODv5YtRIvJ93EHi9-jFwEzTB2iGLi8PuI9LQ94FjULi_mrxzqEB4H2yLbZDQWIUFqEgZcbdnvjC0CEkwuhSkgTnr8zVUchJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">📝
جنجال جدید در دنیای آفیس‌های متن‌باز
پروژه
Euro-Office
نسخه 1.0 خودش رو به‌عنوان یک جایگزین اروپایی و متن‌باز برای Microsoft Office منتشر کرده، اما این ادعا با واکنش تند تیم
LibreOffice
روبه‌رو شده است
😬
🔹
بنیاد LibreOffice می‌گوید Euro-Office خودش را «اولین مجموعه آفیس متن‌باز اروپایی» معرفی کرده، در حالی که LibreOffice سال‌هاست چنین جایگاهی دارد.
🔹
همچنین توسعه‌دهندگان LibreOffice معتقدند تمرکز Euro-Office روی سازگاری کامل با فرمت‌های مایکروسافت، عملاً آن را به یک «هم‌پیمان غیرمستقیم مایکروسافت» تبدیل کرده است.
⚡️
به نظر می‌رسد رقابت بین پروژه‌های متن‌باز برای جذب کاربران و سازمان‌های اروپایی وارد مرحله جدیدی شده است.
#OpenSource
#LibreOffice
#MicrosoftOffice
#EuroOffice
🐧
📄
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6267" target="_blank">📅 21:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvgmJp61mDFyiklTWVZMGE9ntcQ0Zlos6WZtw4m9TMw9Sc5gmxz6xSgNxz3GPx4A3kvdtmvqDdBQj7e2DlzmkbJp3Ec6uMOJX4-7ZkgVyCwZtr-FMxF2yiR7eV_KQMzHuTsVgjaYsFeyhts0vuiN1XV-p6z5rfucD33SjtJ7yKvuxu9EysnjcGf42ulEN0mOrQ6hwbhMS5DkD9wc2nCLk79Vc6xZ2GnoDN2hzxmVDq3KlSsjVaxOMDZv8Bn1UU2tmZ5UcipQGsKZvzmDveAUdfheb6txRShqhZHEIHSDkrs6Y81MR7mO8rpOP0qMO8nli3Jw97pheuSya_lbY_RKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ZOOOP: همه ابزارهای خلاقیت هوش مصنوعی در یک پلتفرم!
🎨
🤖
✨
قابلیت‌ها:
•
🔹
تولید تصویر، ویدئو و صدا با یک کلیک
•
⚡
کلون حرکتی برای انیمیشن‌های دقیق
•
🛠️
قالب‌ها و مدل‌های محبوب پیش‌ساخته
•
📦
یکپارچه‌سازی ساده و سریع
🔗
لینک:
https://zooop.ai
#OpenSource
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6266" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM68W7YxhY5inPBKQj5OdRe9edFqKbBd5B1pbjVhaAAuNx1E4flM9DRU0-VslcZLoCkSE85aG2xYF06VvR_xa5Cw2eXuY_mIByVLu9O_GtYCD0Ts-RaZrpStBTqqFiLoYBeKDZjIYlblR1kR0s9IGYP3voSr9LhVGKzh4tKTjGbaH9Xc8j8ic9PTGZKmSKQdiDm7HfEaSHIf8rnOzZk5kDDmmC3CnOIyeM8qT4xUdsUNitSkbUIamXZKaH4I7fX7nI1yH8Us3yP5XX89Tn-KBtyddhAljFBRcjG7OXghzx_y__f422r9O_CBHdeJOcGSl3ql2FAExa7MCcEt2NPCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵🏻‍♂️
با این ابزار می‌تونید فقط با وارد کردن یک نام کاربری، حضور احتمالی اون رو در سایت‌ها و پلتفرم‌های مختلف بررسی کنید.
✨
قابلیت‌ها:
• جست‌وجوی خودکار در صدها سایت
• بررسی شبکه‌های اجتماعی، انجمن‌ها، پلتفرم‌های بازی و سرویس‌های دیگر
• نمایش تطابق‌های پیدا شده در یک فهرست
• اجرا مستقیم داخل مرورگر، بدون نصب برنامه
• امکانات پایه رایگان
🔗
لینک:
https://whatsmynameapp.net/
#AI
#OSINT
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6265" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6263">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e875845.mp4?token=UTUIWsKYEbQuglYfRQWdY5HxwOc60hTloUbtSDXb0T3TCepVdMLuwOkXgKtoZPar-i7S5icyMY581SECe8ef_JCHZSequCCNROPMy-_gAJdY4O1ZmzKCae8VYNgWp7yJNiJP8p-GO0_udYXsr7LwrtlO0Sahz2_ZtRWHlXAdqlZpG1ylV6oL28ReewYqyPgijsspbgco38haz62hXIvUUkRJyJI9EYJXEt9Uqds6KpYW4wV49WK9tyjqAXG1lQjia1vIq73VB6ywo9dgpC0bqvI2HUIla65mxQXBPUNLhV16CwuMS7jYAXyzA0kMYIAPcvRpNHYipkHOwy-quEGYuYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e875845.mp4?token=UTUIWsKYEbQuglYfRQWdY5HxwOc60hTloUbtSDXb0T3TCepVdMLuwOkXgKtoZPar-i7S5icyMY581SECe8ef_JCHZSequCCNROPMy-_gAJdY4O1ZmzKCae8VYNgWp7yJNiJP8p-GO0_udYXsr7LwrtlO0Sahz2_ZtRWHlXAdqlZpG1ylV6oL28ReewYqyPgijsspbgco38haz62hXIvUUkRJyJI9EYJXEt9Uqds6KpYW4wV49WK9tyjqAXG1lQjia1vIq73VB6ywo9dgpC0bqvI2HUIla65mxQXBPUNLhV16CwuMS7jYAXyzA0kMYIAPcvRpNHYipkHOwy-quEGYuYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تست رایگان Battlefield 6 در استیم شروع شد؛ تا ۱۵ ژوئن می‌توانید این شوتر را بدون پرداخت هزینه تجربه کنید.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان محدود تا ۱۵ ژوئن
•
⚡
شامل ۵ حالت بازی مختلف
•
🛠️
تجربه ۴ نقشه چندنفره
•
🗺️
بازگشت نقشه‌های کلاسیک مثل بازار قاهره از BF3 و جاده گولماد از BF4
🔗
لینک:
https://store.steampowered.com/app/3028330/Battlefield_REDSEC/
#Battlefield
#Gaming
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6263" target="_blank">📅 18:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سیستم جدیدی به
ربات
افزوده شد.
✨
از این پس، در بخش
سرویس‌های هوشمند >> آخرین اخبار
، امکان دریافت اخبار روز ایران و جهان فراهم شده است
📰
🌍
هر دو ساعت اخبار بروزرسانی خواهد شد
✅</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6262" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🦀
Asterinas 0.18 منتشر شد
پروژه Asterinas یکی از جاه‌طلبانه‌ترین پروژه‌های متن‌باز دنیای سیستم‌عامل‌هاست؛ یک جایگزین مدرن برای لینوکس که تقریباً به‌طور کامل با Rust نوشته شده و روی امنیت حافظه، کارایی بالا و سازگاری با اکوسیستم لینوکس تمرکز دارد.
در نسخه 0.18 تمرکز ویژه‌ای روی اجرای Asterinas در محیط‌های کانتینری و مجازی‌سازی بوده و قابلیت‌هایی مانند Namespaces، cgroups و بهبودهای مختلف VirtIO به آن اضافه شده‌اند.
از دیگر تغییرات مهم:
🔹
درایور جدید NVMe
🔹
بازنویسی درایور فایل‌سیستم EXT2
🔹
پشتیبانی بهتر از نرم‌افزارهای لینوکسی
🔹
اجرای برنامه‌هایی مانند Firefox، QEMU و Codex
اگرچه Asterinas هنوز فاصله زیادی تا جایگزینی کامل لینوکس دارد، اما یکی از جدی‌ترین تلاش‌ها برای ساخت یک سیستم‌عامل مدرن، امن و سازگار با لینوکس بر پایه Rust محسوب می‌شود.
#Linux
#Rust
#OpenSource
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کانفیگ ناب
🔥
trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6260" target="_blank">📅 16:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScaVLIy-TGcuBD834NOn5la7F9wdYvAcwhtD1tKy4DFs-jHQqwYjZX8uBDTBxkUzEHmBmKAVfN2qiMzMQfglnUGcQpCsPGseEzXuItU7TSVxQiyFxLcQ8oXaMdcP_LAS6B1zxjAY5wL-Z50Woqv6dHp8rX7cLCwys2tPD1w6WCIUjoqULZj8hyIfOama_Xjjo85BUXyKM9NlZwIUBGFHBnytsDYj5YtHBQ5xyGG9BeiTK6EeJEP9jb1Nf9BhBi7n1GbSfh-JSVh0a-yo3OYCrCDSGIyxHiHu3AZ0bNAcEXIcQpP_Q9mgoHrNAHSfgKd1B3jFZig6_zcn0-Wt6GdZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
یک ویرایشگر ویدیوی رایگان که مستقیم داخل مرورگر اجرا می‌شود و فایل‌هایتان را روی کامپیوتر خودتان پردازش می‌کند؛ بدون آپلود در فضای ابری.
✨
قابلیت‌ها:
•
🔹
ویرایش چندمسیره ویدیو
•
📝
انیمیشن متن برای ساخت محتوای حرفه‌ای
•
🎧
افکت‌های صوتی کاربردی
•
🎨
تصحیح رنگ و بهبود تصویر
•
📦
خروجی با کیفیت 4K
•
🌐
اجرا در Chrome و Edge بدون نصب نرم‌افزار سنگین
🔗
لینک:
https://github.com/Augani/openreel-video
#VideoEditing
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6259" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=No7XlFRkOOX8JsSTps5YrEcmLbylGoGUQguA5HTvpjoh_iYr0Ju2esyvXlJTI96c4aO_yy76VKBRUug-qTCEDQjqn9WVePFoces-VHLg9K5KXZAimDiir4pzQQWl88kD2pjdMRZC_tX1dEnzYRexYHLTPT75M3gY2nn09QNixRzrcSFP2ObkbaH9PDTf4x8Sk8F1mWxIATi2u5QatKBsqCqxH57zI0uRq9yDHZcGLG0LKv5aCsNn3yvj1TK1ZXhpSzW-qgxhM9eM3ArRDx0mUuEaprLCptqZOKAo_K5-GCBAZjE2Aj0HNlPfhh1BKEANFwjATk2Q7WFPweeijaM4aVnGNX03crf0_VEVEOoDyIUZszScR9tAS1KcpfEQv31YyOM8MDp1cXu3fvEUN9FaZco7L33_1Q88OWg42_KkiSFb8GMyPCOegZeoUPPLWUcHais179wddxT9xZvx5Bz4fsdYzLaTZG63cE-JE4OSUH_eF3HEU6xyJn-EPM0aYQ6DTZudwR-x7o9-Jei92MX6_pu0tTlXMquUS1BhhnUXvreDOfxobZYypfFy79sHQ-yQLjOQbiWOR-MoUFDjxxzsIUF61rP9thw2RSQMcFnNJuWmEj5ojfpofuiDhmZOQYPt3tgoTVm0OjyfShcv_THgMkDfx8jK10bZujwDtEKk4Tk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=No7XlFRkOOX8JsSTps5YrEcmLbylGoGUQguA5HTvpjoh_iYr0Ju2esyvXlJTI96c4aO_yy76VKBRUug-qTCEDQjqn9WVePFoces-VHLg9K5KXZAimDiir4pzQQWl88kD2pjdMRZC_tX1dEnzYRexYHLTPT75M3gY2nn09QNixRzrcSFP2ObkbaH9PDTf4x8Sk8F1mWxIATi2u5QatKBsqCqxH57zI0uRq9yDHZcGLG0LKv5aCsNn3yvj1TK1ZXhpSzW-qgxhM9eM3ArRDx0mUuEaprLCptqZOKAo_K5-GCBAZjE2Aj0HNlPfhh1BKEANFwjATk2Q7WFPweeijaM4aVnGNX03crf0_VEVEOoDyIUZszScR9tAS1KcpfEQv31YyOM8MDp1cXu3fvEUN9FaZco7L33_1Q88OWg42_KkiSFb8GMyPCOegZeoUPPLWUcHais179wddxT9xZvx5Bz4fsdYzLaTZG63cE-JE4OSUH_eF3HEU6xyJn-EPM0aYQ6DTZudwR-x7o9-Jei92MX6_pu0tTlXMquUS1BhhnUXvreDOfxobZYypfFy79sHQ-yQLjOQbiWOR-MoUFDjxxzsIUF61rP9thw2RSQMcFnNJuWmEj5ojfpofuiDhmZOQYPt3tgoTVm0OjyfShcv_THgMkDfx8jK10bZujwDtEKk4Tk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
نسخه ۳.۲ مدل Ray از Luma منتشر شد؛ اما طبق تست‌های اولیه، هنوز با رقبایی مثل Seedance فاصله قابل‌توجهی دارد.
✨
نکات مهم:
•
🔹
پشتیبانی احتمالی از خروجی HDR با فرمت EXR 16-bit
•
⚡
تولید ویدیو تا ۱۰ ثانیه
•
🛠️
ساخت ویدیو بدون صدا
•
📦
ضعف در بافت‌ها، انسجام تصویر، دینامیک حرکت و درک پرامپت
🔗
لینک:
https://lumalabs.ai/ray3-2
#AI
#VideoGeneration
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6258" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXOD0caqzz9yqnfaCrxZAv3McqOZTvoUR79h7W58AaRGCEDfzYqt5-7EowzAJafHjx2gLk0_3OTK5ptmAMPpPgQ59cOrEZZYdrJhPgUGhzJRVhPuF4PiZK5kCdLZvjrWsWQJHAY9VqWGH3DCHXEdnWuifR42orOrKRxDH5tuB_JF05-x6JwU5O7qEuSFJPNYMlNeDIk1OrNIVzPgn6jItGhWcTj-Xwsmm2kbQzRxLmVlXeX3K29ORAkiZLQUA2D8bxMiquiDv2IU1tF3_y-x9df4SuxnYhd_Jj3FIRtlJSD_lobgNrYDAqFf-ECVxs5A1kGMYe5kF9kk0B4OsVBdvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hrk3iW14_-AgZogNb0Er_-vFF80NPXdJ1CLM-wa2R_WjoQTx_Xv8Y0WNoiql8uGPcsp9ljrA-Aq5TDPm0rv4O95fTjSzWu6NB28nfzT25M4kRMrx_BKAIDnSVCjfMJLuAplJ33Ymm8GRYKRDa3dbBZi4dflQGdy_qT1aYUQytitoOCwmdMjgAjQfZ5D8H3uRlMpkj9SAW4Y8noylJVV0AyBr0wSPtGak4ONzhf5fhWwYvyt1_dz9mYvVcJdnEkF0XAK973E55zfxLb4Fs8gvd_MEq5Lj-lYFLyGZShT-F6KOreD3B4EBhzGV-_-5Pw4FlVP8zQgT6YrmQyiMTMHjMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
CodeWhale
یک عامل ترمینال رایگان و متن‌باز برای کدنویسی با DeepSeek و مدل‌های محلی است.
✨
قابلیت‌ها:
•
🔹
خواندن و ویرایش فایل‌ها داخل ترمینال
•
⚡
اجرای دستورها و کار مستقیم با Git
•
🧠
حفظ زمینه بین جلسات کاری
•
🛠️
پشتیبانی از MCP، مهارت‌ها و ابزارهای اضافه
•
📦
اجرا با DeepSeek، OpenRouter یا Ollama
نصب سریع:
npm install -g codewhale
🔗
لینک:
https://github.com/Hmbown/CodeWhale
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6256" target="_blank">📅 15:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آپدیت جدید
ربات وگا
انجام شد
✨
- اضافه شدن GPT-5.4
🚀
- اضافه شدن Gemini 2.5
⚡️
- اضافه شدن Flux 2 Kelvin
🌡️
- جایگزینی Lucid Origin با Flux 2 در گروه ها
🔄
- حل مشکل هنگ کردن Gemini 3
✅
- رفع سایر مشکلات
🔧
>
آموزش گرفتن API رایگان GPT-5.5
<
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6255" target="_blank">📅 13:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">💵
گوگل اشتراک AI Plus را ارزان‌تر کرد؛ حالا فقط ۴.۹۹ دلار در ماه با ۴۰۰ گیگابایت فضای ابری.
✨
قابلیت‌ها:
•
🔹
دسترسی پیشرفته به Gemini 3.1 Pro
•
🧠
Deep Research برای موضوعات حجیم
•
📒
NotebookLM برای تحلیل و ساخت پادکست
•
🎬
تولید ویدئو با Gemini و Flow
•
☁️
۴۰۰ گیگابایت برای Gmail، Drive و Photos
🔗
لینک:
https://gemini.google.com/app
#AI
#Google
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6254" target="_blank">📅 13:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📱
اگه حافظه آیفونت زود پر میشه، iMole می‌تونه حسابی به کارت بیاد.
🔍
این ابزار فضای ذخیره‌سازی آیفون رو بررسی می‌کنه و دقیقاً نشون میده کدوم برنامه‌ها و فایل‌ها بیشترین فضا رو اشغال کرده‌اند.
☁️
از بکاپ‌گیری افزایشی هم پشتیبانی می‌کنه و می‌تونه داده‌ها رو با بیش از ۷۰ سرویس ابری مختلف همگام‌سازی کنه. بعد از اطمینان از سلامت بکاپ، فایل‌های اضافی رو هم پاک می‌کنه.
💻
روی ویندوز، لینوکس و مک اجرا میشه و خروجی JSON هم داره که برای ابزارهای هوش مصنوعی و اتوماسیون کاربردیه.
🛠️
پروژه کاملاً متن‌باز و مناسب کاربرهای حرفه‌ای و علاقه‌مندان به CLI است.
https://github.com/chenhg5/imole
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6253" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید  اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت…</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6252" target="_blank">📅 10:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8JkNOdlJ7p_e6MRFmnjgobkYXqnFT1Gev_33QMnmC9RM3pumkYkC7BwC77bqJjDIYl7a0uTfL-AH0mBJfB5BHjoSTI0B1PbUu4xUY1p-GxrsCL5HaaxQNh8-V-DgeB3RzGIzubfNKxAkM5tLqV3vdGWjKo2D2dc1ASbQt8QJSvBQtPCfiYNMmNfRaibTlspfq5aXJp2YYFpBzMd_dDfW_iaHI9qaGcPpOhhXMKzJjgMUyNvfiXu46d---anbZV04RJHzsn8-bJG4_dhyYAyQ5xNKYCqcuEOem6bCxRoP6p80VG9_ixRIexhDbwEiqDhKMTEcuRYm4vv6HErj_41rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Unlimited hotspot shield vpn method! |  7 days trial
/gen 415464440062
trail→
https://get.hotspotshield.com/trial
zip → 1216
Browser any
Ip usa
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6251" target="_blank">📅 10:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqAVPtkZ7_blTUs2WqZPkC6CgSYyjmHAiQCcK6RyZDMrSMwhSIz85NsJU8ByTlBW7x40PfsUl4BBAa8YkE7l3gzm_kLyJiFU6YlNfVN-m7OCN7Ou69d6Eq7ZaAV0lsA06_AaTdFT6XoCqhzKGebQ8HEKNAFNI-caEe2HfTXJqH_yNHxWzG793xIn24ypc0lB5W0vsY1CcUNwleGOIawTK_zWS_sMEdaRR9lNj2GmzfMlTJQh8-o3qFfNYmsX5Ixb6DnjjH_s0Oshz1NyK0Fguwg-AV8wl-3zuKDythMlF9ovDZkjxnm6GPrbBu9jRMiGKkt8dVjvGFxgGXLpv2nXhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با «تحقیقات عمیق محلی» می‌توانید پژوهش‌های محرمانه را روی سیستم خودتان انجام دهید؛ رایگان و متن‌باز.
✨
قابلیت‌ها:
•
🔹
جستجوی خودکار در وب و منابع علمی
•
⚡
پشتیبانی از arXiv و PubMed
•
🛠️
کار با مدل‌های زبانی مثل Ollama و GPT
•
📄
بررسی اسناد شخصی و محلی شما
•
📚
تولید گزارش نهایی همراه با ارجاعات
🔗
لینک:
https://github.com/LearningCircuit/local-deep-research
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6250" target="_blank">📅 10:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEfVMhQ8mNaTidk0q3QLkTHeK9V9Ut1UTNVo5eWARdO_GJLQ4GbGhD9KRjQOdYrgvoD_axqiXZDa3Wy5q8PgMLbL_wdKB39IuXTpBobIzVmqpmFnynTx8WwrLw2GOT9-PEbUHvICZxS78_uITPKpwgTlUShBwrE-p8xxD5u2U4fdb5fuRSGavSlLYsAP7SVPhQSo5JdBdJ6xKQ7AfwdVtxo71MRldEdpIg0-ma2LJwGP3c0bg0AAaXETzoKNJmPyGWl0-KBLMXjoyp_lE-7TuEGnq2TCdsWB5b-7AuubEvfmRjCEJrkZLHz9e6I96P7D8LgDemz6dLboUBj4A2Igqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید
اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت Split Tunnel برای انتخاب برنامه‌هایی که از VPN استفاده می‌کنن
🔹
پشتیبانی از پروفایل‌ها و سابسکریپشن‌ها
🔹
متن‌باز و رایگان
جذاب‌ترین بخشش اینه که از روش‌های پیشرفته عبور از فیلترینگ مثل Hysteria2، AmneziaWG و حتی olcRTC پشتیبانی می‌کنه؛ روشی که ترافیک رو شبیه تماس ویدیویی نشون می‌ده. همچنین توسعه‌دهنده‌ها اعلام کرده‌اند نسخه ویندوز و لینوکس هم در راهه.
⭐
برای کسایی که دنبال جایگزینی متفاوت برای v2rayNG، Exclave یا Hiddify هستن، ارزش یه تست رو داره.
🐱
GitHub:
https://github.com/yanisplugg/olcvpn-client
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6249" target="_blank">📅 10:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c54422014d.mp4?token=nSRM9XW5V76pVv3V5PBstBjrtNvMLRwhneUgqxrmiSwGTfsEL5eb7nkEjWg8A1YXkcIeuJz0miTxe2IdAfRgUHU2NzyLRrYMXx1oTVgbR1kNQxnijoHU897yLf6G6WD5pEH-7biTUt9JXPgqEksmxvYpnDtia4jGf1Hotyh6p5-bvO_QMI9U7-e5ea5Zq1rVsvUxQDhXVZNFKJBQRFwEUQdWGLKd0K48IiyoSVDjWBWeBu0CS61snD9R7BHWKWmcaIGLeTvCvCsNF2a28z-8z_l_s1cNmWh7sx5_1zp76NdZihmqrMGYnJBF4LAPZOHZeCJqzOSlWMEw__Umqzxx-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c54422014d.mp4?token=nSRM9XW5V76pVv3V5PBstBjrtNvMLRwhneUgqxrmiSwGTfsEL5eb7nkEjWg8A1YXkcIeuJz0miTxe2IdAfRgUHU2NzyLRrYMXx1oTVgbR1kNQxnijoHU897yLf6G6WD5pEH-7biTUt9JXPgqEksmxvYpnDtia4jGf1Hotyh6p5-bvO_QMI9U7-e5ea5Zq1rVsvUxQDhXVZNFKJBQRFwEUQdWGLKd0K48IiyoSVDjWBWeBu0CS61snD9R7BHWKWmcaIGLeTvCvCsNF2a28z-8z_l_s1cNmWh7sx5_1zp76NdZihmqrMGYnJBF4LAPZOHZeCJqzOSlWMEw__Umqzxx-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
تلگرام برای اپل واچ
تلگرام به طور رسمی اپلیکیشن خود را برای اپل واچ بازگرداند.
#Telegram
#AppleWatch
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6248" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX7Qg9sCc0BpIDck_1JUj3zqAntwybg_xP4Pdz2RkAgdzOeoTkfwYQj8FaGPwDvIaHR-oXzLCwIVQBwszp-Fp4py8VihyfrK-_35HmhHnI-Y0qXaqLfFMQD_SNG2b_mcm_dGF7wBg0eFtHFbe7eKH2nCyY7khyMWA38hZz1WL1q5MRf84TV2VNZXzfCIZ4VRo6KC0oLd2nPVBKxl3EZswalMhhR2rNxs2OHXwnW4rGqxap_U438Ua3WBqsrmnOCR5q2-6pgPEcCwOeehyUgRD6MNzvdhgMc-A8PAj6Paqo3KuqrYblIxwH0K6oIvG3JyOGUdm0csCe31mxJH8czDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک فهرست بزرگ از ابزارهای رایگان هوش مصنوعی برای تست، توسعه و اجرای مدل‌ها
🤖
✨
قابلیت‌ها:
•
🔹
مدل‌های متن‌باز؛ از مدل‌های سبک خانگی تا گزینه‌های قدرتمند
•
⚡
ارائه APIهای رایگان برای توسعه و آزمایش
•
🛠️
اجرای محلی مدل‌ها با تمرکز روی حریم خصوصی
•
💻
دستیارهای کدنویسی رایگان جایگزین Cursor و GitHub Copilot
•
📦
فریم‌ورک‌ها و دیتابیس‌های کاربردی برای ساخت سیستم‌های چندعامله
🔗
لینک:
https://github.com/12britz/awesome-free-models
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6247" target="_blank">📅 09:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">💻
NekoBox 5.11.18 برای ویندوز، لینوکس و مک منتشر شد
🔹
یک کلاینت متن‌باز و قدرتمند مبتنی بر Sing-box برای اتصال به انواع پروتکل‌های ضد فیلترینگ.
🔹
پشتیبانی از VLESS، VMess، Trojan، Shadowsocks، Hysteria، TUIC، WireGuard، SSH، Tor و...
⚡️
🔹
دارای حالت TUN برای هدایت کل ترافیک سیستم.
🔹
سبک، سریع، رایگان و بدون تبلیغات.
🔹
گزینه‌ای مناسب برای کاربران Clash Verge، Hiddify Desktop و v2rayN.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6246" target="_blank">📅 08:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">vless://5dcf2dbf-3e82-4456-8961-287cc732bb0f@85.198.20.217:12817?type=ws&encryption=none&path=%2F&host=Play.google.com&security=none#Germany%20Hetzner-.
10 گیگابایت تانل المان</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6245" target="_blank">📅 03:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sg49yDqvndRex4WuQO_jS4CCUV3uCRK_OO6ISMgv16PicpULe-wDMI9Ok0laN_BmqKNvZj18zXN42HOP2thrNqTeF3tH_vfrBkHIgQlRxw2tvnsfwwIhJ6nY2TzZoZe147G1XuooPGjWYYLJxev21ui71pc69VGrYXI6eGBxmjCLQk72pkGM9osnp1NHJGWh0DbftZHq0mOMIyRC0XXOUVq22dLo5bid1nQ5_m1bTK0OIlRT83sDNyhEseE4bkscuAQ-Rz_lgEfGcirXe9cQniG4VkhNHUovUi4iAe1ZrSUrSBFS-QXvpfQoFjgPWN5pDsvlgVXK0xyqCxcIGOeyBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله
😱
💻
اگه با 3X-UI کار می‌کنید، یه پروژه جالب به اسم X-UI-PRO منتشر شده که کلی از تنظیمات REALITY و WebSocket رو خودش انجام میده و دردسر راه‌اندازی رو کمتر می‌کنه.
🚀
🔐
این نسخه Nginx رو هم کنار 3X-UI میاره، SSL رو خودکار تمدید می‌کنه، روی پورت 443 کار می‌کنه و حتی برای مخفی‌تر شدن ترافیک از بیش از ۱۵۰ قالب فیک استفاده می‌کنه.
👀
⚡
از Sing-box، Clash Meta و Cloudflare هم پشتیبانی می‌کنه و برای Ubuntu 24 و Debian 12 آماده شده.
🛠️
اگه دنبال یه پنل کم‌دردسرتر برای REALITY هستید، بد نیست یه نگاه بهش بندازید.
https://github.com/mozaroc/x-ui-pro
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6244" target="_blank">📅 03:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hala Hey _ Live In Concert</div>
  <div class="tg-doc-extra">Armin Zareei _2AFM_</div>
</div>
<a href="https://t.me/archivetell/6243" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">امشب رو با این معما بخوابین
شرکت در کنسرت این شخص، از نظر اخلاقی، غیراخلاقی هست؟
#Moral_Dillema</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6243" target="_blank">📅 02:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🫠</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6242" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QO5aQpO7M7029mC8pC13oslj-txmHEr72YPKPRzVYAzv1YMguPLwMZDvnPrY199azvafblSj5uAlatl6vnDOVD6nnhmdG2Er1vUgBaDPlU44sCj-tITQV-xivKrsJjeccv6JQi6XZIFpNz4nbTLk1QVHqxSgyvFFOwuFisPDHaLmUb4UnLy0TppBZOs7Vq8h_WM2GKgXHwP_a-rob4Aor8x-bEDUyqlRC0mdNNAUG9KXVqiL8Csg0fHh0BbGuinl6FdaTkWhxi8dEYdX2MSr1dEjlQGH2Fv-ZVkh6JiwuatFw86Hjlh-LZUGWOppFCCF4XpHWAIFT8sTBbM6R1VnEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Gemma 4 بدون سانسور منتشر شد!
🔹
یه نسخه دستکاری‌شده از Gemma 4 اومده که تقریباً هیچ درخواستی رو رد نمی‌کنه.
🔹
روی سیستم‌های معمولی و حتی آیفون هم اجرا میشه.
📱
💻
🔹
حجمش کمه و با Ollama و LM Studio هم سازگاره.
🔹
جالب اینجاست که با وجود حذف محدودیت‌ها، کیفیت مدل تقریباً مثل نسخه اصلی مونده.
⚠️
طبیعتاً دیگه خبری از فیلترها و محدودیت‌های امنیتی نسخه اصلی نیست.
👀
🫠
..
#Gemma
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6241" target="_blank">📅 01:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
بی رفرال
🤐
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 140 / 140
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6240" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">https://t.me/ArchiveTellNews/212
🤨
🤔</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6239" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6238" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app
بخونید نظرتونو بگید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6237" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">StormDNS
a.cyntarix.com
25ffbc77bcfb23b2d4ee225eedcd2466
داشته باشید اگه نت قطع شد</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6236" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این پروژه پایتونی جالب هم برای تشخیص اشیاء توی ناحیه مشخص شده کاربرد داره مثلا طبق مثال خودش که با QWEN ادغامش کرده یه نفر با هودی اومده توی ناحیه مشخص شده تشخیصش داده و به گوشیش نوتیف فرستاده و گفته چه چیزی با چه اطلاعاتی اومده توی ناحیه.
برای دوربین مداربسته خوبه یه ناحیه رو مشخص میکنی هر چیزی اومد توش بهتون خبر میده،کد اصلیش با پایتون نوشته شده و از ابزارهایی مث ffmpeg برای مدیریت استریم‌های ویدیویی استفاده می‌‌کنه.
github.com/roryclear/clearcam
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6233" target="_blank">📅 00:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6232" target="_blank">📅 00:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هر کی 99 تا رفرال داشته باشه ی کانفیگ نپستر میدیم بش
😌
🔥</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6231" target="_blank">📅 00:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6230" target="_blank">📅 00:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6229" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmJvJ1Gfb_7p2QcWPi_YuHj2Rz8TAzlQogXgingpxtUDdMZ1S9cO2kVtqtqNiv7DW0J5FVWMxs9oUqkusT0yHTIXx-OaNwnHhH51i5ixRavS25PjxD8Ihb-5IN10FMfP-YPKV8HPTsC0TY6DdErcO4oR967LoqhbK7WNd42BEkE1UOoXvIPGL2r68HNApmLadoLptUlq3gt_CDGwOMOYtQsf1W8ltxYYIzn_dyB4CHt13WxQ6bRbXqzV1MXNxIDxRksOWS6Rj-YwQ2-OCFK9CbWTlUQs7qjCHEtLskJblR3TZSo5EXpG_GXuHxcAryIJaVefI7IllxCFXI3fCm0Pdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Gitdot؛ رقیب متن‌باز GitHub که با Rust ساخته شده
🔹
پروژه Gitdot توجه زیادی جلب کرده و به‌عنوان یک جایگزین مدرن برای GitHub معرفی شده است.
🔹
این پلتفرم از ساخت مخزن، Push/Pull، ریپوهای خصوصی و عمومی و مهاجرت از GitHub پشتیبانی می‌کند.
🔹
رابط کاربری آن با الهام از ابزارهای CLI مانند Vim و fzf طراحی شده و روی سرعت و ناوبری با کیبورد تمرکز دارد.
⚡️
🔹
قابلیت‌هایی مانند Pull Request، Issues و CI هنوز در دست توسعه هستند.
⚠️
با وجود استقبال کاربران، Gitdot هنوز در مراحل اولیه توسعه قرار دارد و فاصله زیادی تا رقابت کامل با GitHub دارد.
🔵
@ArchiveTell
| Bachelor
⚡️
https://gitdot.io/</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6227" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🛑
پایان uBlock Origin در Chrome نزدیک است
🔹
گوگل آخرین راه‌های دور زدن محدودیت‌های uBlock Origin را مسدود کرد.
🔹
پشتیبانی از افزونه‌های Manifest V2 به‌طور کامل در حال حذف شدن است.
🔹
فلگ kExtensionManifestV2Disabled نیز از Chromium حذف شده است.
🔹
مرورگر‌ های Edge، Opera و سایر مرورگرهای مبتنی بر Chromium هم این مسیر را دنبال خواهند کرد.
⚠️
نتیجه: نسخه اصلی uBlock Origin به‌تدریج از دسترس کاربران خارج می‌شود و کاربران باید به uBlock Origin Lite مهاجرت کنند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6226" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=l-eUOn6oFdt5CGYMeIC6HUsIG7Ej003RsRAcYLkygg87zJuuovoqeBTIUrgl2gITtrsFBYu-Kh0HxsMrzqT0jhrEmKlOqhRWIZ7K9SuXD1o3r0_3EUIBESdqGqJgpk8A28lZn8x63ZktuRmLaSxIJIRKEWSkt-sfdGKvIqp9_idanIvRHgxQXpz66iO5EQRvpZ2-RwQvZCmf3DcY2srYL5YLmSWtWkh_MK92gm4-KOygVzzdX8X5kIqhn_th7CIQ_27wpY5JZWZhoMcNK10jFwZmU-7jMgJBBW7wCXpAEI4TbgV92GW8y4-hbZVPnC22V_seJtwOQF1IBHP9r0inSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=l-eUOn6oFdt5CGYMeIC6HUsIG7Ej003RsRAcYLkygg87zJuuovoqeBTIUrgl2gITtrsFBYu-Kh0HxsMrzqT0jhrEmKlOqhRWIZ7K9SuXD1o3r0_3EUIBESdqGqJgpk8A28lZn8x63ZktuRmLaSxIJIRKEWSkt-sfdGKvIqp9_idanIvRHgxQXpz66iO5EQRvpZ2-RwQvZCmf3DcY2srYL5YLmSWtWkh_MK92gm4-KOygVzzdX8X5kIqhn_th7CIQ_27wpY5JZWZhoMcNK10jFwZmU-7jMgJBBW7wCXpAEI4TbgV92GW8y4-hbZVPnC22V_seJtwOQF1IBHP9r0inSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6225" target="_blank">📅 22:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH396tnGg3FWrEj3GMAwNXWEVO34cldXAU1ZWmhBJk8DhOICQKUAQu2WxA2J6GINYrH6TZDvDP5bkVVqmH9IYxFumGq88QXuFtU_MYfaTlmKDPn33ZTAOlvKp6EJ7MIDk0ER3MfsZh05x44KsryH5cgEXDeCUqnD4zaPxo1WqBgRH43Ie5ZmApUwVbxh7YWJ8nvZLZifaW3mrgshbTPY5wHM8QbTE1nKBqGzpIikxUqfsFIkGnwWMsE3JyTlR7h3ew5zsUgqgPoC1bfK7Hn2ibCaUcDd_-WK2JwFLPz310D0wXwl1LZqklket5nUpUYeLRkI3eav7S7Wi8gl7EIo2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک ویرایشگر ویدیوی کامل که مستقیم داخل مرورگر اجرا می‌شود؛ بدون نیاز به Premiere Pro یا CapCut
🎥
✨
قابلیت‌ها:
•
🔹
پشتیبانی از چندین ترک ویدیو و صدا
•
⚡
رندر سریع با شتاب سخت‌افزاری GPU
•
🛠️
افکت‌ها، ترنزیشن‌ها و ابزارهای تدوین
•
📱
قابل استفاده روی کامپیوتر، تبلت و گوشی
•
🎬
عملکرد پایدار حتی در مرورگر معمولی
🔗
لینک:
https://tooscut.app/
#VideoEditing
#Tools
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6224" target="_blank">📅 22:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">طبق درخواست شما عزیزان
تمامی سرویس هایی که API رایگان هوش مصنوعی در اختیارتون میزارن رو مجدد قرار میدیم
✨
Freemodel.dev
🥇
developers.cloudflare.com
🥈
console.groq.com
🥉
aistudio.google.com
build.nvidia.com
cloud.cerebras.ai
openrouter.ai
console.mistral.ai
llm7.io</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6223" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rk52_NEmoU2S2U2YWEx2vQ1MQJpuENPmCeIhUT1T11xobhIZUVj9MZcyvkFnBjVNckVX0w8iRIsjozb1rTKVB0hdOi68z8b7vkbfwM7jdP8UXrOaSUXNXxhFr5_PryNj8NjoHiHgpE3G9Nk_2-9pP1grGfqoJwCiU1RA-llUMQyW0CjNzihn158Ktv5rFgZUAYC0rjvb-ohIO4br_NRMUoZocsQ1GdUjJyBp-Es6plIar5nvXbspXvzGUBnz9C5SIaAaV6Frfa3tDZBWpdGgSvm6cys4uMQuT89ZMSClhz1ieNGxzEg167sBLrz25Okrc2du0xBgXQcddRR3uevKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
کاهش بار اضافی روی حافظه در ویندوز ۱۱ — غیرفعال کردن فعالیت پس‌زمینه Edge
😎
این کار از طریق ویرایشگر رجیستری انجام می‌شود:
1️⃣
کلیدهای Win + R را فشار دهید → regedit. را وارد کنید.
2️⃣
به مسیر زیر بروید:
HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Edge
3️⃣
روی فضای خالی کلیک راست کنید → «ایجاد» → پارامتر DWORD → نام آن را «StartupBoostEnabled» بگذارید و مقدار آن را 0 انتخاب کنید.
4️⃣
کامپیوتر را ریستارت کنید.
پس از این کار، Edge دیگر در پس‌زمینه اجرا نمی‌شود و منابع را مصرف نمی‌کند.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6222" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">walf.zip</div>
  <div class="tg-doc-extra">12.9 MB</div>
</div>
<a href="https://t.me/archivetell/6221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ℹ️
فایل سرچ پروتکل و سرور ویندسکرایب
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6221" target="_blank">📅 19:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚀
برنامه WALF منتشر شد!
اسکنر خودکار سرورهای ویندسکرایب نسخه PC
اگر از عوض کردن دستی سرورها خسته شدی یا دنبال یه راه سریع برای دور زدن فیلترینگ میگردی، این برنامه دقیقا همون چیزیه که نیاز داری.
کار برنامه چیه؟
برنامه WALF کاملا خودکار و بدون اینکه نیاز باشه کاری کنی، تک تک سرورها، شهرها و لوکیشن های ویندسکرایب رو روی پروتکل ها و پورت های مختلف تست میکنه تا بهترین و سریع ترین اتصال رو برات پیدا کنه.
👇
چطور کار میکنه؟ خیلی ساده:
۱. فایل برنامه رو از لینک زیر دانلود کن و از حالت فشرده درش بیار.
۲. فایل walf.exe رو اجرا کن و دکمه Start رو بزن.
۳. تمام! خود برنامه اگر ویندسکرایب بسته باشه بازش میکنه و شروع میکنه به اسکن کردن کل شبکه تا بهترین اتصال رو برات ردیف کنه. (فقط مطمئن باش که قبلا توی ویندسکرایب اکانتت لاگین شده باشه).
لینک دانلود برنامه سرچ خودکار پروتکل پورت و سرور های ویندسکرایب در پست بعدی
⬇️
با تشکر از چنل
@CubicDreams
که زحمت کشیدن ساختن
🙌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6220" target="_blank">📅 19:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خب یه پست اختصاصی دیگه داریم این فایل رو خیلی جاها میلیونی میفروختن در حالی که رایگان بودش یکم دیگه پابلیک میکنم
🔥</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6219" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gbls2Ys9kVa1f295rDaq0Y1B8vcbmoNnpxDNrsWEflu4toOLAEw9Znjzh5psIKDgh6wd1MBBi_YYkeRLGl_abtRohprQYktBXXoFa3OSDJnFav4X43c77x8u9mKGL4XH5TogWLgSojOEBW00EC7c2n5K_qf6aJbi_hicnaYNE313sZMXTKMu7wB1BA29eA-vnrlnO5J0lR-jGaMecm0H9Wr3pG700Fluaikd9MlhHPQGLOs_vtPHNP_Q_TiCTTa2-sdc0z7YZd5pY7LLPXvrBY9T6t6_pgjd0llzVeTe5w4Y1WIyLxnJoHBFUqv2VUs_14F-xK5tD8zBqzpV5xJHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel  اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت Freemodel شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6218" target="_blank">📅 18:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⚠️
اطلاع رسانی برای افرادی که اشتراک ویندسکرایب پرو خریداری کرده‌اند:
پروتکل
ikev2
روی تمام لوکیشن ها (تقریبا) متصل میشه
✅️
با تست هایی که گرفته شده با فیبرنوری مخابرات  سرعت همه سرور ها دانلود ۲۰۰ مگابیت و اپلود حدود ۵ مگ فعلا قفل هست
(پیش‌بینی میشه پهنای باند ikev2 کم کم محدودیتش برداشته بشه و به قبل شرایط ۱۸ و ۱۹ دی ماه محدودیت شبکه برگرده)
سرعت کانکت شدن به سرور ها و امنیت ، این پروتکل خیلی بهتر از tcp هست حتما استفاده کنید
👌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6216" target="_blank">📅 18:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ArchiveTel
pinned «
ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6215" target="_blank">📅 17:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel
اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت
Freemodel
شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
بخش اول: احراز هویت با شماره تلفن
🔹
بخش دوم: احراز هویت با تلگرام
✅
گزینه احراز هویت با تلگرام را انتخاب کنید.  لینک ربات تلگرام برای شما نمایش داده می‌شود. وارد ربات شوید و استارت را بزنید
🎉
پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار  هر هفته: ۶۶ دلار اعتبار
💰
4️⃣
از منوی سایت وارد بخش API Keys
شوید و یک API Key جدید بسازید.
5️⃣
در بخش Docs می‌توانید مستندات کامل استفاده از API را مطالعه کنید.
🛠
تنظیمات نمونه:
model_provider = "freemodel" model = "gpt-5.5" model_reasoning_effort = "xhigh" disable_response_storage = true preferred_auth_method = "apikey" [model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses"
🤖
حالا API Key و مشخصات بالا را به هوش مصنوعی موردنظر خود بدهید و از آن بخواهید برایتان کد تولید کند:
✅
JavaScript
✅
HTML
✅
Python
✅
PHP
✅
Node.js
✅
و بسیاری زبان‌های دیگر...
💡
می‌توانید با آن:
🔹
ربات تلگرام بسازید
🔹
وب‌سایت طراحی کنید
🔹
ابزارهای اتوماسیون ایجاد کنید
🔹
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت خوبی برای تست GPT-5.5 بدون پرداخت هزینه است.
@Archivetell
✨</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6214" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6213" target="_blank">📅 17:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
hysteria2://5z15av99psrlhdqp@32.195.51.20:39150?alpn=h3%2Chttp%2F1.1%2Ch2&fm=%7B%22udp%22%3A%5B%7B%22settings%22%3A%7B%22password%22%3A%22dlxmzvxvcp3i6v0e%22%7D%2C%22type%22%3A%22salamander%22%7D%5D%7D&fp=chrome&obfs=salamander&obfs-password=dlxmzvxvcp3i6v0e&security=tls&sni=32.195.51.20#usa_hesteria-%40u2vpn-100.00GB%F0%9F%93%8A
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6212" target="_blank">📅 15:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پروکسی‌های اختصاصی آرشیوتل
😎
⚡️
پروکسی ۱
🚀
پروکسی ۲
💥
پروکسی۳
💡
روی لینک بزنید و گزینه Connect را انتخاب کنید.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6211" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwTMdaGJNig9lS38HFsUquW0qwge5WXuOndQEvWyG2DHXWhBqIyX4RoSXrTOM4D_0jGaZxem5LQDrDkk6pv3pX8D4kJ83DLlanQqyX_WUT5Upd2SA0-SiP3Ybb2HMBg_HcV6hIFHfwvTfKT7gI9XRVTetlY3K4tmtUShQWoewvLGqK_TpaY7WVz-_xLri_9IcMkxdCcu3XIaA53iVpQYecDTddSIi_kBowm1xGIsI3Pu71HIJeCOLkc5KSRO33wZV35UCHDHDPslvgQ1MhLTbuVzhSDxW74ovxV_3FoCVgUFXctS6AuO0MzFf7CDjz8jD4PyufO3ObQsQreefCsmsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب یه روش مخصوص ایرانی‌ها اضافه کرده، رو همه اپراتورها عالی کانکت میشه:
Settings → Connection → Anti-Censorship
گزینه Protocol Tweaks رو روی Enable بذارید، بعد وارد Configuration بشید و یکی از دو گزینه آخر که ایران هست رو انتخاب کنید. گزینه Large TLS رو هم روشن کنید.
پروتکل های udp و tcp رو تست کنید
ایرانسل tcp 587 france
مخابرات همراه اول udp 80
با فیک میل اکانت بسازید
https://windscribe.com/signup
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6210" target="_blank">📅 13:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzBqksqxhpIg7EQiRlttc_LfNV5HbdAPHVqV6waOBC01orDIhSo9PWns43BrlZbd-9r23BjKejU_6knyEtECR_hDWmYktUuVw6ojnxBQP0M5HaCKlNJdlVJKOkE4VSdyh5oocHwcBqxLRIudiSyiXx0O_8_UTW4akWVKgVr1FAjumxsxFL4hkFYoLOfagHlvsgoe3PoNfXj5VTDmmtOVJTBVY0oZdQbqdDLLh5rwV9feGugV6COdDLSX4wEaXS8-8Qy5d_7Ul0H4UEFEhB8VYB3GTmHyMvm8EcGXR6ppfuCLb-fx_ZqVzTShY-jdKpBL5OFNMiOVSSKWAGprBiyjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
Impeccable
‏این ابزار به عامل های هوش مصنوعی کمک می‌کند تا وب‌سایت‌های منحصربفرد و بدون الگوهای استاندارد ایجاد کند
🔥
‏
✨
قابلیت‌ها:
‏•
🔹
آموزش عامل‌های هوش مصنوعی برای ایجاد طراحی‌های منحصربفرد
‏•
⚡
کار به عنوان منتقد، توسعه‌دهنده front-end و نویسنده UX
‏•
📊
آزمایش ماکت‌ها، برطرف کردن خطاها و بهبود طراحی
‏
‏
🔗
لینک:
https://github.com/pbakaus/impeccable
‏
#هوش_مصنوعی
#طراحی
#OpenSource
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6209" target="_blank">📅 13:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEWgASYty3g5gJG52IQZeUiUmikB1zI2qV1ZRqSbFja_0utME1UvhB3pHfeT984w1WtXXHcdEr0wcqSo54brJt6aav_eB8v-356UwU6VMnOmXBcUQg1Q3nIOpz0uIJtBvzP384rtQYd0g53Vx4mHp0mOPL8Pe11xLqlTHAGe1vtTYRPRwL2hM-rNofCS4EGbnNrqaQqNSWlwDjfpWpLTeuujM4fRn3i2L68-e2i5iKucpq0-L86jqTyPtKjiHW1GzaSUIhWIBduSjqMOjXkhpt9t6m2BAh01hErAXLQ5-BaHQmQQ0yEgQpbUBeQ_yFK_f70ZzF-TFlC6V6qDFB-lpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GawhOjHln6eWZrNqFR1yrptNqVvVQs5ZJfKVC79TAI-FCKMcYCTJATDHfO49mOD0ecb6G_cGAnc-xp1WcSpUdyOQ8VKVD0t5iPoPCtlB_LlP096Yj8dVx01Z9XrHWb7oMd_-s25HrV54JbvKzNgbC2T5FuCdYiHNz5dZK83RuuGyiRTNk1Q_QpPq7sgnFTYoSnrewCqRcVQO-MR1giV7a_ask_fEcap_K4mHSeDbCZiTDvndy2b1FJ-miQGTCeN1TOp8DbzsvDtha9HSzHYIyicSLyKNKalFqAUvk8xLYYWQM3vn9ztN-6VrDM_B8-261x2cZ4IBX-73chvlQNEMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUJGeNlp8Uy5UepC0qI2_RnlhA3AlzhHCOq-5Mrle9b6iITyEetvN77I30q03VNh5JAb7FJ5GRz6C91mLKaF_f2l2pVILvR-E_cUmqtOIjVJEgxUK-Me_uydBXEYT71kRQKDplPYZwL7Dk2ML312MceMMQw_D5t_yqs07eqqqE43QQSzxkupFcuVIC4iFdev2oB4Dfyp6NEpL2CorkrPqP47BocYHx9vOQgXOGmmcd37PnDD10j8ZHdbkD2c3Hoy0qTiGkZvyKtD270N1lqVsI-DtkBl5G564-VXtk7WLx6_gQYGj1WffeYrL_8Z0TgUSGMWYRqruUQENGZMoZTuuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=AH45hejl5nsmUSpyq7Y1wsPWqnBSsppyJncZaMcWGKGkLaew2O9lgxc4DTFJPfsh_aAt9NMFcH54w561HpZnx1K1JNwzH8FsYvujjSNNNUeK0aHwQMEznPXwC4JoxqXl_5HpvSb7epLwKxA8mJFBRrC7xR1mYWol-pPRJ0sSromqiV-OPlNXaOiEywlI6M00fufY6AAm00Z3A1KGsStOsxqVjilAMqJmwpyB0-Q5Kt8nT87eofHqlntvP2J0vTlFjzd9kEpIv-K1Z-owz2YUsCF7rjtmKPmFDfjrs2Ks2r79Z8B1BLC4fpqq6JxEYd7bVY_Cm25rUpsFTMW7HmfvZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=AH45hejl5nsmUSpyq7Y1wsPWqnBSsppyJncZaMcWGKGkLaew2O9lgxc4DTFJPfsh_aAt9NMFcH54w561HpZnx1K1JNwzH8FsYvujjSNNNUeK0aHwQMEznPXwC4JoxqXl_5HpvSb7epLwKxA8mJFBRrC7xR1mYWol-pPRJ0sSromqiV-OPlNXaOiEywlI6M00fufY6AAm00Z3A1KGsStOsxqVjilAMqJmwpyB0-Q5Kt8nT87eofHqlntvP2J0vTlFjzd9kEpIv-K1Z-owz2YUsCF7rjtmKPmFDfjrs2Ks2r79Z8B1BLC4fpqq6JxEYd7bVY_Cm25rUpsFTMW7HmfvZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
هوش مصنوعی Siri یاد گرفته است که عکس‌ها را مانند Nano Banana Pro ویرایش کند.
✨
قابلیت‌ها:
‏•
🔹
«بازآفرینی فضایی» برای تغییر ترکیب، زاویه و پرسپکتیو عکس‌ها
‏•
📸
ویرایش پیشرفته برای ایجاد عکس‌های خلاقانه
#Apple
#Siri
#Ai
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6205" target="_blank">📅 12:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLuY_nXluQzu8HHcHJAQDYDOoKco3dqZaqyB5uAomf-Q674675Q2e7R9Ba0b7AltAmNeaP1vYJXDpKZdX_aHPkAko292GD7QaorTn765MTRIn4GJASmRAa1Rhn0CCWKpmhso10FqycBP6LL5nEULIsVmxhSeDJD6S2FyRLlgDaRVx7tESkK3hsUbSujz3br_d06DHcEnLtCAcfbmzxDPZsUfGsYbQ84128LXOXWk4vqbaarNIHwXsqFwrC4W7u-g-rffkbmUx_KCWKmoAyEoZl0ZU8RfSOZE5IalQ8oLQxb5zu2m3zPUdR0iwyJ3x_SaDU33UIJUNJTnzsfn8s9czg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
.FrameCoach معرفی شد!
‏این ابزار هوشمند تنظیمات گرافیکی ایده‌آل را برای هر سخت‌افزاری انتخاب می‌کند و حداکثر FPS را استخراج می‌کند
🎮
‏
‏
✨
قابلیت‌ها:
‏•
🔹
انتخاب کارت گرافیک و پردازنده
‏•
⚡
انتخاب بازی از کاتالوگ
‏•
🛠️
دریافت تنظیمات بهینه برای حداکثر FPS یا بهترین گرافیک
‏•
📊
مشاهده تأثیر هر پارامتر بر عملکرد
‏•
📈
تست تنظیمات و پیش‌بینی فریم بر ثانیه
‏
‏
🔗
لینک:
https://theframecoach.com/
‏
#گیمینگ
#بهینه‌سازی
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6204" target="_blank">📅 12:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">با پلتفرم Cerebras به مدل‌های قدرتمند gpt-oss-120b و glm-4.7 با محدودیت بی‌نظیر ۱ میلیون توکن و ۲۴۰۰ درخواست در روز دسترسی پیدا کنید
🚀
شما می‌توانید کلید API خود را دریافت کرده و پروژه‌های هوش مصنوعی‌تان را با سرعت و دقتی فوق‌العاده پیاده‌سازی کنید
🛠️
. این یک موقعیت عالی برای استفاده از مدل‌های سنگین بدون پرداخت هزینه است
💸
، پس آن را از دست ندهید!
✨
cloud.cerebras.ai
🔗</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6203" target="_blank">📅 11:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=HqDWsymj7f8YBgcL2RzAoknzpcjbcGTnjgTInwriwO1a0SAlyYjoSBLheFaXoPkRRvKPSZY7-jsbXJnEtZ7QPR9bYGGXRhq5f9SypqYb2x8ngwsOkE6wiJDokiEwSuDf7OiA_5-NQsAMukQamjbo_pfhCNWSirQNRmU3zMPCpHERqfXH24SFUTR3ZXBUYPo5HNbQW_FhbFCY0ay-QfbrFleyME5dkyPIcd8rbKD863sMRLTXW3HO1I-YM5109ryrhKXMyrtUMjDqj0cFmxP4N3PVmB-3gJvAUbKgRqo2eMEH__yAUXlew_zTyscVAdye_zO4UR3DX1QLBQuV5D-VJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=HqDWsymj7f8YBgcL2RzAoknzpcjbcGTnjgTInwriwO1a0SAlyYjoSBLheFaXoPkRRvKPSZY7-jsbXJnEtZ7QPR9bYGGXRhq5f9SypqYb2x8ngwsOkE6wiJDokiEwSuDf7OiA_5-NQsAMukQamjbo_pfhCNWSirQNRmU3zMPCpHERqfXH24SFUTR3ZXBUYPo5HNbQW_FhbFCY0ay-QfbrFleyME5dkyPIcd8rbKD863sMRLTXW3HO1I-YM5109ryrhKXMyrtUMjDqj0cFmxP4N3PVmB-3gJvAUbKgRqo2eMEH__yAUXlew_zTyscVAdye_zO4UR3DX1QLBQuV5D-VJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🤖
چینی‌ها یک هیولای هوش مصنوعی با ارتشی از عوامل عرضه کردند — Kimi Work می‌تواند تا صد دستیار را به طور همزمان روی یک دستگاه اجرا کند.
‏
‏
✨
قابلیت‌ها:
‏* تا ۳۰۰ عامل می‌توانند به طور موازی روی وظایف مختلف کار کنند
‏* مرورگر را تقریباً مانند یک انسان کنترل می‌کند
‏* دسترسی به داده‌های مالی را بدون پیچیدگی در تنظیم API فراهم می‌کند
‏* عادت‌ها، زمینه و اقدامات قبلی را به خاطر می‌سپارد
‏* با فایل‌ها و اسناد محلی کار می‌کند
‏* کد پایتون را اجرا می‌کند و فرآیندهای روتین را خودکار می‌کند
‏* کمک می‌کند برنامه‌ریزی کنید و وظایف بزرگ را تقسیم کنید
‏
🔗
https://www.kimi.com/products/kimi-work
#kimi
#ai
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6202" target="_blank">📅 11:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram.apk</div>
  <div class="tg-doc-extra">78.2 MB</div>
</div>
<a href="https://t.me/archivetell/6201" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">12.8.0 (6913)
Directly downloadable from
telegram.org/android
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6201" target="_blank">📅 11:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rumFVKU057j77ThcT7kXl9Dp_que4Facw01GQ1NZGE4di4oUSHc-Ke-YlGjzV6fPDLczFPc6j5Ajp6ZFAzukohwoVMCOS0ISNcjKMbSR3S7wcP_pi_uAP-MWQwAV7lVtcYze1N0siLOS1uUev98zvDSE_2AOvMX4t68CQDv-nGS0nOgOA3HMzZughWDrgHXB1ArhBsMWvDIXEXaaKGEoOTGKskSOLRGWurMzOUnsNvzjaz1O-DpXs5_CHsDp8mNfM6z-0DlSpPx0DzJW6w9QUTr6b0KZZZcoVdQmjlfPMnnea9GGq9NexqOeEgqFP_m8cLv4rxg0YBjzoNPZg7nghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
گوگل NotebookLM را با قابلیت‌های جدید هوش مصنوعی ارتقا داد.
حالا این ابزار از مدل جدید Gemini استفاده می‌کند و می‌تواند فراتر از یادداشت‌برداری عمل کند.
🚀
✨
قابلیت‌ها:
•
🤖
پردازش و تحلیل بهتر اطلاعات با Gemini
•
📊
ساخت نمودار و تحلیل داده‌ها
•
💻
اجرای کد مستقیماً داخل نوت‌بوک
•
📝
تولید اسناد و گزارش‌های مختلف
•
☁️
محیط پردازش ابری اختصاصی برای هر پروژه
🎯
ابزار NotebookLM کم‌کم از یک ابزار یادداشت‌برداری به یک دستیار تحقیق و تحلیل کامل تبدیل می‌شود.
🔗
لینک:
https://notebooklm.google.com
#Google
#Gemini
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6200" target="_blank">📅 10:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee5737315.mp4?token=cpBdvgfxDGdRUHmKn8yJcBno56ooSCjiJS8PrjBNof8VQDXtAF93o7RRQgnXRoqDx8gaYkELaub7X3iqKMvWjKmW93uoSIZGqbyFclduaoG0aEdxs0kuCG37RnLJFVvkH4AS8U37iSSywBKPTnQ1mcxFGJSNbJuCQrsJbqeIWkZvG4tU9lDlsTnlNIvYpiBXTG-Oo87w1xOQRTbnN8wV8zKcxECpul4wTmmSkk9quv3yC8RaNfE57N3EFcxV8iC1Q6OTK3z16zoxYMboFhBNIYeRGl9qVGzMAlwNji8-GRU-iM5SXkB0HvOHuU5Kgx3avPPKjXm7qpLBhHFWFXdtwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee5737315.mp4?token=cpBdvgfxDGdRUHmKn8yJcBno56ooSCjiJS8PrjBNof8VQDXtAF93o7RRQgnXRoqDx8gaYkELaub7X3iqKMvWjKmW93uoSIZGqbyFclduaoG0aEdxs0kuCG37RnLJFVvkH4AS8U37iSSywBKPTnQ1mcxFGJSNbJuCQrsJbqeIWkZvG4tU9lDlsTnlNIvYpiBXTG-Oo87w1xOQRTbnN8wV8zKcxECpul4wTmmSkk9quv3yC8RaNfE57N3EFcxV8iC1Q6OTK3z16zoxYMboFhBNIYeRGl9qVGzMAlwNji8-GRU-iM5SXkB0HvOHuU5Kgx3avPPKjXm7qpLBhHFWFXdtwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔤
پیدا کردن فونت هر سایتی در چند ثانیه
ابزار
Font Stealer
یک ابزار رایگان برای طراحان است که فونت‌های استفاده‌شده در هر وب‌سایت را شناسایی می‌کند.
✨
قابلیت‌ها:
• نمایش فونت‌های به‌کاررفته در صفحه
• دانلود فونت‌ها در فرمت‌های مختلف
• پیشنهاد جایگزین‌های رایگان از Google Fonts برای فونت‌های پولی
🎨
ابزاری کاربردی برای طراحان UI/UX و توسعه‌دهندگان وب.
#Design
#Fonts
#WebDesign
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6198" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🌐
اختلال VPNها در روسیه وارد مرحله جدیدی شده است.
گزارش‌ها حاکی از آن است که فیلترینگ در روسیه نیز دیگر فقط بر اساس IP نیست و اکنون الگوی ترافیک و TLS Fingerprint نیز بررسی می‌شود. همین موضوع باعث ناپایداری VPNها، MTProto و پروتکل‌هایی مانند WireGuard و VLESS شده است.
#VPN
#Telegram
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6197" target="_blank">📅 10:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚀
پروکسی محلی برای تلگرام دسکتاپ
TG WS Proxy یک ابزار متن‌باز است که ترافیک Telegram Desktop را از طریق WebSocket عبور می‌دهد تا اتصال پایدارتر و سریع‌تری داشته باشید؛ بدون نیاز به سرور واسط اختصاصی.
✨
قابلیت‌ها:
• اجرای MTProto Proxy به‌صورت محلی روی سیستم
• انتقال ترافیک از طریق WebSocket و TLS
• پشتیبانی از Windows، Linux و macOS
• رابط گرافیکی ساده برای مدیریت تنظیمات
• متن‌باز و رایگان
📥
دانلود و مشاهده سورس:
https://github.com/Flowseal/tg-ws-proxy
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6196" target="_blank">📅 03:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قابلیت جستجو در وب در ربات هوش مصنوعی وگا اضافه شد.
🔍
همین حالا بیاید و اون رو در پیویتون و گروهاتون تجربه  کنید.
😉
@T_Vegabot</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6190" target="_blank">📅 01:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">موتور جستجوی ربات
Vega
چگونه کار می‌کند؟
🤔
بخش جستجو در وب در Vega از مدل gpt-oss-120b پشتیبانی می‌کند که API آن توسط Groq ارائه شده است.
🌐
همچنین در این سایت انواع مدل‌ها وجود دارند که سرویس‌های جستجوی وب مختلفی را ارائه می‌دهند.
🛠
سایت برای دریافت کلید و تست انواع مدل‌ها
✨
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6188" target="_blank">📅 22:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=YSEFDJqp01hjy4RWT6qTrTyVQAY_q8Y7u87ZuNfipwT8BXMBCd0YUOqBrtz36NwV4vNt77w9uTMxEZtDs3Bp7GfAvtGDGcY13aidqAJlSncZ-WlcJJ9L1CNv9sbUzRUOipD4YnWMwAYDHh65kqMSeYDWtIZm6NJ398Ijqb-hJpMDLFSjuH5um7lb2RrvoYNQvg5doaKQeIAUWMkEpJjx2prthw6BXBRaBoJ_vccCj7IoyysMfPJ8knLzimzDKvpHZ4g-DEtQKolY9RbUAtVdVi5rL-Xr0rG8rZxrZBOZmk3J7LeySq8_cP8x5YYMw3vW2hHX6GWdCJbKusRtIg5qsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=YSEFDJqp01hjy4RWT6qTrTyVQAY_q8Y7u87ZuNfipwT8BXMBCd0YUOqBrtz36NwV4vNt77w9uTMxEZtDs3Bp7GfAvtGDGcY13aidqAJlSncZ-WlcJJ9L1CNv9sbUzRUOipD4YnWMwAYDHh65kqMSeYDWtIZm6NJ398Ijqb-hJpMDLFSjuH5um7lb2RrvoYNQvg5doaKQeIAUWMkEpJjx2prthw6BXBRaBoJ_vccCj7IoyysMfPJ8knLzimzDKvpHZ4g-DEtQKolY9RbUAtVdVi5rL-Xr0rG8rZxrZBOZmk3J7LeySq8_cP8x5YYMw3vW2hHX6GWdCJbKusRtIg5qsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍎
Siri AI: تحولی در WWDC 2026!
در آخرین حضور تیم کوک، سیری با قدرت گرفتن از Google Gemini به یک چت‌بات هوشمند با اپلیکیشن مستقل و دسترسی کامل به اکوسیستم اپل تبدیل شد.
🤖
این دستیار حالا با دسترسی عمیق به ایمیل‌ها، عکس‌ها و تقویم، می‌تواند کارهای پیچیده و چندمرحله‌ای را به‌صورت کاملاً بومی مدیریت کند.
✨
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6187" target="_blank">📅 21:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=di3QVaT8xBKgXgOJOWTfABMfwdkHwX-VPrhLWUmXg921I9k2lAO0g9u4tgM4-7WL6x1k_ccaFu8ik_0-vUILeAgEDZtaurjd0fsG2jaeWk70OcuBCknKMEDNQ7Xl2uMBBYsB7nSwJ571roTcVcrZ9qXoVyo5XOFc-zaY_eAEZ3VZ56hSK0bSRBRryupkdpLP_ks-rZuGU4rGQA_E8L8h0wyGdGndAplssWukOPbZhRpb4uvk0xsJIbMtP4NpcdiShpLZRcNko41__FerRAzvwiVT6YkrxEA0MpgDU51MUQ3Esw2sc_s_bkJV3SHiR_NOLmpxeEn75PUN_iYhjlZ08Q" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=di3QVaT8xBKgXgOJOWTfABMfwdkHwX-VPrhLWUmXg921I9k2lAO0g9u4tgM4-7WL6x1k_ccaFu8ik_0-vUILeAgEDZtaurjd0fsG2jaeWk70OcuBCknKMEDNQ7Xl2uMBBYsB7nSwJ571roTcVcrZ9qXoVyo5XOFc-zaY_eAEZ3VZ56hSK0bSRBRryupkdpLP_ks-rZuGU4rGQA_E8L8h0wyGdGndAplssWukOPbZhRpb4uvk0xsJIbMtP4NpcdiShpLZRcNko41__FerRAzvwiVT6YkrxEA0MpgDU51MUQ3Esw2sc_s_bkJV3SHiR_NOLmpxeEn75PUN_iYhjlZ08Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Apple
#WWDC26
has started
Watch live:
https://www.youtube.com/watch?v=hF8swzNR1-o
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6186" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4TRM_Eh1nLLvq925NlVHtk4mRTpoyNFyuGWqjYol2aT1t35XXWeTSXBXF3LVCKluQnyJhQdY3pWITMTO0fCSv7SFfr0yCfSgC8iEJzp2HtK0dS0ioGFdbbYBYyvIGz_xMpXP11dgituE55Qj7Z7O0iTMWvUzXNaZQ64WDaYbzqr06aUw7qeqUJ1K1XqiLmGK3n4zCiGFHXHJiCdVqLHUHv4sVG59AiKpJ_-zuwakP4Q08NPeD_DPYJ7gDPv2IuKhjBWlWZXmbzg5Z7gm6YPb6u1LpZfCVXGja_yvuLuYdPkK_u__j5UdruBRGajMKITfLu-_NpJ1S8fyKLoyTbeWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت ارائه APIهای هوش مصنوعی رایگان
🔥
از مدل‌های چندوجهی شامل متن، تصویر و ویدیو پشتیبانی می‌کند و یک راه‌حل توکن مقرون‌به‌صرفه برای توسعه‌دهندگان ارائه می‌دهد.
🔗
https://agnes-ai.com/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6185" target="_blank">📅 20:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🤖
Kimi Work
دستیار هوش مصنوعی که کارها را خودش انجام می‌دهد
نسخه دسکتاپ Kimi Work منتشر شد؛ یک AI Agent محلی که می‌تواند بخشی از کارهای روزمره را به‌صورت خودکار انجام دهد.
✨
قابلیت‌ها:
• اجرای همزمان تا ۳۰۰ ایجنت هوش مصنوعی روی سیستم
• کنترل مرورگر برای جستجو، کلیک، تایپ و انجام وظایف مختلف
• دسترسی مستقیم به داده‌های مالی از Yahoo Finance و World Bank
• سیستم حافظه برای یادآوری ترجیحات و سابقه کارهای شما
💻
قابل استفاده روی Windows و macOS (Apple Silicon)
🔗
اطلاعات بیشتر
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6184" target="_blank">📅 19:53 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
