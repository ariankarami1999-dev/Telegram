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
<img src="https://cdn4.telesco.pe/file/NvxOPYZlJW4ifxtr8Id-S0qizuUcJoFSEg08z-hmOvdo7c6De-fM8LzC9nyXw6PGc_jnnj9drRcqczVWKvYcTBAzaxG05ByT06hzbUEJNGApRvZ585ZXfrga_NvBgtREXlsnKtzsUw7l2N97NhQVCczOZA-IZs3YfQKZ1xZftyhejHGxhACmD0Rc3KHekMdhQDwXVNfUssp3bDL-74Aot3jaW3870Dz4DkAKfwfQYZBIxyK6f7h4QXTGPWRFMuyoyBR0gXeVaCYvsTTVPUdPvPe-KUYcfzinRsb1THcm6j9RxaU5LRfHDXYY6e4BKauxXOAAx88ZKBgq_HrKxeSt5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.59K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 07:27:51</div>
<hr>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ویژه
🔥
🔥
🚀
تبدیل گوشی‌های قدیمی اندروید به سرور لینوکس یا هاب خانه هوشمند!
🐧
📱
اگه تو خونه یه گوشی اندرویدی قدیمی دارید که گوشه‌ای خاک می‌خوره، پروژه
Linux-Android
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار که به تازگی در گیت‌هاب ترند شده، یک اسکریپت ساده و قدرتمند است که بدون نیاز به روت (Root)، گوشی اندرویدی شما رو از طریق اپلیکیشن Termux به یک دسکتاپ کامل لینوکس یا سرور خانه هوشمند تبدیل می‌کنه.
🔥
امکانات و کاربردهای بی‌نظیر این پروژه:
1️⃣
نصب خودکار و بدون دردسر:
بدون نیاز به دانش فنی پیچیده، فقط با اجرای یک اسکریپت، لینوکس با محیط دسکتاپ دلخواه شما (مثل XFCE، KDE، MATE یا LXQt) نصب میشه.
2️⃣
تبدیل به سرور خانه هوشمند (Home Assistant):
می‌تونید گوشیتون رو به یک هاب مرکزی (Home Assistant Hub) تبدیل کنید تا وسایل هوشمند مثل لامپ‌ها و پریزهای وای‌فای رو کنترل کنه.
3️⃣
پشتیبانی از شتاب‌دهنده گرافیکی (GPU Acceleration):
با استفاده از درایورهای Turnip، گوشی‌های دارای پردازنده اسنپدراگون گرافیک بسیار روانی روی دسکتاپ لینوکس به شما میدن.
4️⃣
نصب ابزارهای کاربردی:
ابزارهایی مثل مرورگر دسکتاپ (Firefox)، پخش‌کننده ویدیو (VLC)، سرور SSH و حتی اجرای برنامه‌های ویندوزی با استفاده از Wine (به‌صورت اختیاری) قابل نصب هستن.
5️⃣
کاملاً ایمن و بدون نیاز به کلود:
تمام پردازش‌ها روی گوشی انجام میشه و نیازی به سرور ابری ندارید.
⚡️
این پروژه برای آموزش لینوکس، توسعه با پایتون و ساخت سرورهای خانگی فوق‌العاده است.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Linux
#Android
#Termux
#HomeAssistant
#OpenSource
#Github
#Python
#Tools
#TechHack</div>
<div class="tg-footer">👁️ 685 · <a href="https://t.me/archivetell/6542" target="_blank">📅 01:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚀
آموزش اجرای MiMo Code یک AI و ابزار کد نویسی کاملا رایگان و بی محدودیت
1️⃣
نصب Termux
اگر روی موبایل هستی
اول Termux را نصب کن
📱
2️⃣
دستورات داخل Termux
1) آپدیت Termux
pkg update -y && pkg upgrade -y
2) نصب ابزارهای لازم
pkg install -y proot-distro nano
3) نصب Ubuntu
proot-distro install ubuntu
4) ورود به Ubuntu
proot-distro login ubuntu --user root
3️⃣
دستورات داخل Ubuntu
1) آپدیت Ubuntu
apt update && apt upgrade -y
2) نصب پیش‌نیازها
apt install -y curl bash ca-certificates wget git nano gnupg lsb-release software-properties-common build-essential python3 make g++
3) نصب MiMo Code
curl -fsSL https://mimo.xiaomi.com/install | bash
4) اجرای MiMo Code
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس :
mimo
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر MiMo Code را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
mimo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/archivetell/6541" target="_blank">📅 23:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH_GY1yNSoiKmxqFlevsBHCyKIkFa7xfP_A8IjhBEACOYiipXlq6X6mCfY5EJcYJH9uVjx_3HtvuaVbscM0N2lzfJHRzQ9Jg_LEE6exi_8KeUL_KuJV2j90qvXt-0JIESaAQpO80QfMQqBwIvWlNU7P2JAPiO2-zg0bgXiruqciB-tn_j66FTtFoVeY1KCoAz99TqCo8UVhcHrWzsy7nA-44nz1vyKlg2GR62-nepnViDq_YTTwXAiamPNvLnzYikGO9OPPwuSk0u77xvy_Jfe2I8yTryjvTsokcil8sqP4BoRagJwC6ZvoYwe_qhAPpnU4qY9N1NhOcdzV99y6h5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
کتابخونه‌ای به وسعت ۱۱ هزار کتاب!  هوشمندانه جستجو کن و دنیای جدیدی از کتاب‌ها رو کشف کن.
✨
قابلیت‌ها:
•
📖
دسترسی به ۱۱ هزار کتاب با رتبه‌بندی و توصیه‌ها
•
🧠
جستجوی معنایی: «کتابی برای توسعه فردی» یا «متا فیزیک»
•
🔄
مشاهده نسخه‌های مشابه برای هر کتاب
•
🌟
مجموعه‌های پیشنهادی از افراد مشهور
•
📊
جمع‌آوری داده‌ها از کتابخانه‌ها، شبکه‌های اجتماعی و رسانه‌ها
🌐
Site
#کتاب
#کتابخوانی
#معرفی_کتاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/archivetell/6540" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nE2u8w2so271uJSJJ4gKWqsd8FVvdMsZ2G1j7IA2xCV9yNtOxLPucqQ4LzwW7mtkEN2I10V1LhXLehONc2BJ1qEQWoNNfQs48v4Vs7Hvg2mtUPVOvh9FCiHCTg8SwrkY5D0IOqT7gmSlji0MJbA4XdHK1KUxsYTLjKJuVr8-RAawABWTRpJRQgbHFjYvRkrfIX_CZnZ016Udape4zaaSwZ1xVZspKh6LCdlTKD61Q8T2NzFDYvQh_CrstbNzbHVjjzQ9KMRS4bIKouqmgfCdmWtcJJsAHa0vm2io6nsJJSzWi0Dsrr9Vrx9dO5TuXTsJNOKlE-sesQaTMGDrOhUCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EEsa7dQymtm8dllCqqk9GKNP_I11eLasAQai_z2GYb-0RrseSu5Jc2nfDGY7YGi2C2ELCaxQ-clSYcw2jj83Y6Gej57MDA3nqEgP4-8Rwvl88pbWrxLQx0eLOaA0KfwrhfS92ysHPu6hcBXFOfVxGyLF6Pcqv3s0a53571kpC0t04VMhjvGXVuWQiqSNmEPxiNJW4icB1qcbbeXC0J_RDknDPjVvWHwrMkOgKNyj915ZBTkh5KDGoIsNQJHy90eEjAtCjk0JjWSGxHggALB6LbjXedL3okvMPRX8Q3VpXxYprAP_x4bTxVkXC_Zu0NBjZyfxl5qqtvsq8cuQ-Ck-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vRs_ejCH9zFXBgqskRzD3HZnQpjxvUYSi3BL8gWhV_NMrGxeuqjoe5pKUNmRkSmYEXK6Nw2EsKfKwIP73Ipc_5Zzk0bZH5jf8yhDfQENxkpDdWMuJHUXpU-vnr_f1APaMi1pGTZM4YxCXqUig0Dagfdxmhn1DZKAgRDXnN-fFwA7_al7G-MEIU0Yu-nXiH-Fyun7aG5KWXHA21exS0fwBvwJH1WT06X80aMK83jvEkTmUIKa4CY8IPNWDgSS32A2ue8tAIZj0B33rM1I1Brp8jOnL_6tIr9tIGKbZv5_trmthXvhFSONkXF-BAcUiFuK7chJbUNGsx7fDU7xV2YAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7_CxBGHgTMPmTtYNWsxjazIJv0rqy0mMjPzhqSNqc9Nagt3bOYd8YL4tJKwWUx86E5K4JpdHj6l1jt-BceJj12w1Vf5CJciPRou0w5hvZnkXBO7OyX3bQmxXIBcpHW-2ciLGVGfQ_oOct6YRz-rUzI4wMFQVHplP8tWgoS0GkHjVn-F5F3lCPx9GobMJNYNvAuep_ZXjwRTxq-tYRRmRioq6s4JnmRzzTvNJubx22_fzYoZLHJ1FhZBxRVzBUwO8D-Wmv4llc7tshsmkw6z8tt85MMO65tfR8JGAukY0wG_kGOlgAyFQs9MJ32KlNVrW6bHxSnNK0Z-DqspJ2ARmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🍿
نتفلیکس خود را بسازید — یک برنامه رایگان و متن‌باز برای تماشای فیلم‌ها، سریال‌ها و انیمه بدون تبلیغات مزاحم پیدا کردیم.
🔹
بسیار سریع‌تر از اکثر سرویس‌های مرورگر کار می‌کند.
🔹
امکان دانلود محتوا مستقیماً روی دستگاه را فراهم می‌کند.
🔹
از زیرنویس‌های فارسی پشتیبانی می‌کند.
🔹
بر اساس علایق شما توصیه‌ها و مجموعه‌هایی را ایجاد می‌کند.
🔹
برای راه‌اندازی فقط به یک توکن رایگان
TMDB
نیاز دارید که در چند دقیقه تهیه می‌شود.
🌐
GitHub
#OpenSource
#Streaming
#Entertainment
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">worker.js</div>
  <div class="tg-doc-extra">23.5 KB</div>
</div>
<a href="https://t.me/archivetell/6535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سورس کد ربات تلگرامی برای چت با هوش مصنوعی بر بستر کلودفلر
🌐
ویژگی‌ها:
- گفتگو با مدل‌های GLM 5.2، Kimi k2.7، Gemma 4، GPT 4 و Llama
💬
- تولید تصویر با مدل‌های Lucid origin و Flux 2
🖼️
- تبدیل صدا و موزیک به متن با مدل whisper-large-v3-turbo
🎤
راهنمای اجرای این سورس در بخش کامنت های این پست ارائه شده است
👇
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/archivetell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚀
معرفی Save to Yaps؛ ابزاری برای ذخیره هوشمند و خصوصی مطالب وب!
🌐
✨
اگر از آن دسته افرادی هستید که همیشه ده‌ها تب (Tab) باز در مرورگر خود دارید، یا لینک‌های مهم را برای خود ایمیل می‌کنید و دیگر هرگز سراغشان نمی‌روید، افزونه
Save to Yaps
دقیقاً همان راهکاری است که نیاز دارید!
این افزونه یک "Web Clipper" فوق‌العاده است که هر صفحه وب را به یک یادداشت Markdown تمیز و خصوصی در کامپیوتر شخصی شما تبدیل می‌کند.
🔥
چرا Save to Yaps متفاوت است؟
*
تبدیل هوشمند محتوا:
مقالات را از شر تبلیغات، منوها، بنرها و پاپ‌آپ‌ها پاکسازی کرده و فقط متن اصلی را به عنوان یک یادداشت تمیز ذخیره می‌کند.
*
ذخیره سریع تصاویر:
با قابلیت Hover-to-save (نگه داشتن موس روی تصویر)، می‌توانید عکس‌ها را به سادگی به یادداشت‌های خود اضافه کنید.
*
حریم خصوصی مطلق (Private by Design):
برخلاف سرویس‌هایی مثل Pocket یا Evernote، در این ابزار هیچ اطلاعاتی به سرورهای ابری ارسال نمی‌شود. همه چیز به صورت محلی (Local) روی کامپیوتر شما ذخیره می‌شود.
*
کارکرد آفلاین:
حتی زمانی که به اینترنت دسترسی ندارید، می‌توانید یادداشت‌های خود را ذخیره و مدیریت کنید.
*
سازگاری:
روی تمام مرورگرهای مبتنی بر کرومیوم از جمله کروم، اج، بریو و آرک قابل نصب است.
💡
نحوه استفاده:
برای شروع، کافی است اپلیکیشن دسکتاپ رایگان Yaps (برای مک یا ویندوز) را از
اینجا
دریافت کنید، افزونه را روی مرورگر نصب کرده و با یک کلیک، مطالب مهم را به "Second Brain" یا همان پایگاه دانش شخصی خود منتقل کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#Yaps
#WebClipper
#Privacy
#Productivity
#Markdown
#KnowledgeManagement
#TechTools</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/archivetell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgIXCJNMBDI4LYQpMF8IWJMw4Tc2Jz0e41xBO90cnNIq7HNRo3ui4eMtqOMbQKFgl6sRv2IiqfSZopap4CF-gH41npOxIwMf04dRGQR8SmPPeIdP5C6Kg9Nx8paj5AXAdAk4VF9sO67KEdb_jmnDLrFsrKwW1LdVgoWGcR06ltEoXJwt4Qh-Irq_IOy38dKHYtxmqbN5pcdR5XETtuCACpprJSldXLH6BrB-miglFikZdsXAfa3liHzZ24usM3hIm7AOXgHFfJDLFqrPXpX-GgX-d9cokWIYxDXwP5LwPa6I_sL0CsStn7mqksa6avdMv5rzL6QWMiMVFfa7xTtNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش در سطح MIT و هاروارد رو رایگان تجربه کن!
🎓
بیش از ۱۷۰۰ دوره از بهترین دانشگاه‌های جهان حالا در دسترس شماست.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان به دوره‌های برتر جهانی
•
📚
شامل برنامه‌نویسی، ریاضیات، طراحی، کسب‌وکار، فلسفه و علوم دیگر
•
📹
محتوای کامل: ویدئو، جزوه، تمرین و امتحان
•
💡
مناسب برای یادگیری از صفر تا پیشرفته
•
🔸
یکی از بزرگترین آرشیوهای باز آموزشی
🌐
Site
#Education
#FreeCourses
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6533" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nesl6hQt_kjpem4gPdzq4Hh20lKFwDPF88aCMGKdWAnGAo_loJ90t6qi85zBLmMb72vN5Pp_VgSK3Z5TqRQGERCTtIHXuj23Zhmddn0knDBH5w64U2OffnZFS08yxIoHEkZLfubOcZCxsFpUSPSA7IVjZc-yB8zcDUfynCyi7z66Z3XGxbVbw796Db1oxsyHctXMoeMJ-KYgZjwIqY3FKBBuVEYPOt60jssmh9Cm9ZbNrrWhl5jwrXGEOnp-wf4jblUBKLiVac5I2QOSPUV__qnqqyr4f_THotWuozp06AisFai22Z_iZsfYYAWvLVqaUARuMSYGjAu7BJ1sc1CnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMa065v_ord40SXFvpTakpWWQyvkrZVfY14jy7tJ5nI-Mme_gUcIoZZUPvNruLYerYARH7e3f8XBRIuesbqYA8ueQs4t4Jtg_5MEOQA6i7BzfCBiVisBsuRwTyuuOCIquiAdEV4t6FBj6I1NkauqeOxe9G3_XGy9_u2mOMUIJwnEJA6S-eXiBLXR23hXd6cckZNN6ELUuMyoSFVZtBnF6s6eHymKak9kqAvjJWv6Iv054anXbI0Rcza1Y8JW_9xQ1lUbsRSrKExRlHdKsu4O2MNqEQAlocYBaunl3Y_lgLrRkEBH_pqsq2A_AcgboKBNfTx7QhKA-G4uIIeJ-Gm5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cs0Z_spBXVCJYbaMlIfzNDU9KznG7whT2bbZ25cfcHQpkyjup0UF6a_9RbP48ln04HLH3dowIfyqsPhu0bckGYtxBn845EH6l_QAuyNfiwBUcedMyz09mHS6WEGhPfWgaFSPpvT7akPHqzhfRcXWrDATGE7dw7kCuRAf1icrHSMwOi6e9WhG_5Ram3vgFWZx9kLE0bZg-Dn5_bqZcvPvWugBNF1VGaV1YzkaOocE60KgmCZh5h4EpokMjB0RWHmizXCBVQHBf_e3v4aQ_7rgofIxKPCoQjyAA-uYSRzkaLMltJLMW63DLuY_JqflxE19YcrdlJHvzBOQ1nDEVTg-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bglIVj9OzXIVRwXdhKcl9eoSuwekGGSEJK3mW97KxD6qLadItyZbii86qABSPILRqwSi0fCF3QInEE_BPWULxgMZ9BeDw_kMfOmIXajSObuXgCPYnmGN7T9t0zddiAQXaidxG_jIBp3pVljY1vbWBWWFQq0CU4TUK7lK4sTC0VicSXaem1j6KfW3xGYgoD7jwsP6nmTDr0jw63B9VmgwmtTtBiWXHjBe3lhDrcV6yoX5z0pfu6t0iUBdjs8fXgJPbAzZ7PShKfYQ80eUAnJi2vNDGkYDjxOqU7e1qWDxyn2lukpR7UYsD8w4QMm9Vg_NRwpp7QjBmreuJmLo9I3GoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOWe0FcWRpQ2mqKoEsSah6vQ9bjJh6vxy5SonXwDrCKNSN5PePjE7jHqriojggAfzC_locWRIS_u5ypeM8VRj6BSyeVPBcHEO2ScrJIAdoulavNQGDJ9MqnWkTLZdC6Jcd4df2u4EuE12FFOa_xOviz5sVynV40zT1l-vHCKvmiI_wufZ7DIo-ZgVg-IKSCeP_1GcQE8e3EPBJRJFewEbQSTmC8fHUVb49RbnOSNdK12RTkLl2M5B_0BWbEKAznGapfdZL-WVS_C0xl-vvsp_gjxXVB9CtlPv6k92QgWyC2dKCPYyqjHnb9oCgRcap-i4kKFfdfVytyIM-AEXDX6TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tqk1e1fP4PbO6yxq5QAHOLbRUm0w8a3TGONARczBffAiYWqiy6vBm-HBLuNWdHLlHCMULVdpE9dzx2HREN4U8dHVNFuyu0swf7mlMLlO1wGqssqLloSlFtAev-2rvdMyc-E9ulwfUM7_q8u0RELkmwe_I5n3ztrtJsFl4DHzloeMtYgy9iI9Kmaz7AtWGDtXiM_j1PRXuwPXla0D5v_k-7PbBTXkn-MFAxWl3PaUn2kf7rD9QR5ztyK_KScVCYifxGpQEiYrzpkQbFZL0Jm-yEGYRIqqaRy0jjqdyovhiFIoN336FFThBB5IHEhVY1Tdaoe4EpsTh5ouYO5Sgftysw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6cLgwyKW1GHk0WgbqAwyJlkWPRodzl9L0HSTc7SJvxSR-CIghPdRR099aA-LZ3XjVkx03WkIj0yQl7QrQoO-Ytf6OdzfQUYnecN4E804T0xYoKEib3pRYnxDqgptnIVdN56sUY5jhAqOIki_3W0yorfL5xXe10XxjOk5STTw8UbIPSo5LgLziSOlgaDbopQJPfi2HKNmy0NsygYG4Z0XAKycRfwSufHvNhc1RGcthmgpEL0if7LPNX6P0f4ZsaRYIoADPi4-gHY53nhOJiCQ2pZMsms_rbfPvdiUh68R9eKHSRphE8kZP0IRckOTdqW93pAfg6gOgbbVTTsTJrd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر تورنتی که بخوای رو پیدا کن!  با "EXT Torrents"، یک موتور جستجوی قدرتمند و رایگان، به دنیایی از محتوا دسترسی پیدا کنید.
✨
قابلیت‌ها:
•
🔹
آرشیو عظیمی از فیلم، سریال، انیمه، موسیقی، بازی و نرم‌افزار
•
⚡
جستجوی سریع و دقیق با کلمات کلیدی
•
📂
مرور دسته‌بندی شده و رتبه‌بندی محبوب
•
🔗
پشتیبانی از کپی مستقیم مگنت و دانلود فایل تورنت
•
🆓
رابط کاربری ساده و بدون نیاز به ثبت‌نام
🌐
Site
#Torrent
#SearchEngine
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
معرفی winpodx؛ اجرای اپلیکیشن‌های ویندوز در کانتینرهای لینوکس!
🐧
✨
اگر نیاز دارید برنامه‌های ویندوزی را در محیط لینوکس اجرا کنید اما نمی‌خواهید درگیر سنگینی و کندی ماشین‌های مجازی (VM) شوید،
winpodx
راه‌حل جایگزین و هوشمندانه شماست. این ابزار به شما اجازه می‌دهد برنامه‌های ویندوزی را درون کانتینرهای ایزوله در لینوکس اجرا کنید.
🔥
ویژگی‌های کلیدی:
*
بدون نیاز به ماشین مجازی:
اجرای مستقیم و ایزوله در کانتینر با عملکرد بسیار بالاتر.
*
پشتیبانی منعطف:
اجرای نسخه‌های مختلف ویندوز در محیط کانتینری.
*
توسعه‌یافته با Python:
ابزاری سبک و قابل سفارشی‌سازی برای سناریوهای مختلف.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#winpodx
#Linux
#Windows
#Docker
#Python
#Containers
#DevOps
#OpenSource</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚀
معرفی AI Website Cloner Template
این پروژه یک قالب حرفه‌ای برای
تبدیل هر وب‌سایتی به کد مدرن (Next.js 16 + React 19 + Tailwind)
با کمک ایجنت‌های هوش مصنوعی است.
قابلیت‌ها:
*
مهندسی معکوس هوشمند:
تحلیل سایت، استخراج توکن‌های طراحی (رنگ، فونت) و ساخت کامپوننت‌های دقیق.
*
سازگاری بالا:
پشتیبانی از ایجنت‌های معروف مثل Claude Code، Cursor، Windsurf و Gemini.
*
تکنولوژی روز:
خروجی تمیز با Tailwind CSS v4 و استانداردهای strict TypeScript.
کاربرد:
بازسازی پروژه‌های قدیمی خود یا یادگیری نحوه ساخت کامپوننت‌های پیچیده وب‌سایت‌های حرفه‌ای.
🔗
مشاهده در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=hrVxrJ_KbxTi8zbw57eKXi7GJonGlfMzkcYW499ntDteQynUzF-7-yaLZgOcDKTjyDdy_0Xzr2aH4nxNabL5WTiemuVffGpRiVJZpeIwjJlShZzrxW7OmoS0iy5YE0DMvIH_r-1PEuQXh_DQg5NksvMvLN1eZ7gZpkq6kWDeWFWF79ROZGi4UFwkfprI6txJCd4P4NS8WGq2PD6hESEyyfoycQy3MqPXr9r4fRZVlXcLdOlIfvBTgLZ9vaXefa8MWzn6UrYC5Dyb29L6WKnOffgT-d5vIkEsSf3IlI9xJJsP_FUqQYF0cgCnjaVXnSPTAC7cYgCZUYy5kUPeGosKnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=hrVxrJ_KbxTi8zbw57eKXi7GJonGlfMzkcYW499ntDteQynUzF-7-yaLZgOcDKTjyDdy_0Xzr2aH4nxNabL5WTiemuVffGpRiVJZpeIwjJlShZzrxW7OmoS0iy5YE0DMvIH_r-1PEuQXh_DQg5NksvMvLN1eZ7gZpkq6kWDeWFWF79ROZGi4UFwkfprI6txJCd4P4NS8WGq2PD6hESEyyfoycQy3MqPXr9r4fRZVlXcLdOlIfvBTgLZ9vaXefa8MWzn6UrYC5Dyb29L6WKnOffgT-d5vIkEsSf3IlI9xJJsP_FUqQYF0cgCnjaVXnSPTAC7cYgCZUYy5kUPeGosKnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡
یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده.
این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway
را فراهم می‌کند.
از طریق خود ربات می‌توانید:
✅
پنل موردنظر خود را بسازید
✅
مصرف و وضعیت منابع را مشاهده کنید
✅
دامنه شخصی خود را برای پروژه متصل کنید
✅
آی‌پی تمیز را مستقیماً از طریق ربات دریافت کنید
هدف 𝗥𝗘𝗡 ایجاد یک روند ساده‌تر و خودکار برای مدیریت پروژه‌ها و سرویس‌هاست.
🤖
ربات
💻
سورس پروژه
━━━━━━━━━━━━━━
👨‍💻
توسعه داده شده توسط 𝗔𝘀𝘀𝗔
دوستان اضافه کنم اگر رندر شما ساسپند شد اکانت رو حذف کنید و دوباره با همون ایمیل یا گیت هابی که داشتین ثبت نام کنین مصرفتون ریست میشه
برای حمایت از پروژه star بدین
❤️
(در گیتهاب ترجیحا
😂
)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLZAxWBLCNf6G6nd0QaWufEM6K1T5nPufLFtXi9q3rb2Z2LuRFQXMxv21IGyl22eH0QNi_BJ3XQf-TGB6WR7gmUZrzpKJaYYFcarUJhUi_uFLBvliCTBpb7zctIB0pjfBbW4VL6WfCvUJ2phgpXi-aMVOXzPrbwWEXuUelCTN6cPA2uh5SDokj4X32EKXRb5iBgWvKyjts5neuRdZOugyH2dV2sMshVEkYS6ggjLHeXXHS_JeMgfASiKpXNt69c1p8oLOXPaFLHtDW68KR2PNYerqjZYO8Lvt5QwexyobYyjCJhiyKsILZyGMjpUMkosg0N_jt373KOhXhS3Uw-Rvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی shadPS4؛ سریع‌ترین شبیه‌ساز کنسول پلی‌استیشن ۴ برای کامپیوتر!
🎮
✨
اگر به دنبال اجرای بازی‌های PS4 روی سیستم خود هستید، پروژه
shadPS4
یکی از فعال‌ترین و سریع‌ترین پروژه‌های متن‌باز (Open-Source) در دنیای شبیه‌سازی است که با زبان C++ نوشته شده و با سرعت خیره‌کننده‌ای در حال پیشرفت است.
🔥
چرا shadPS4 در حال حاضر ترند شده است؟
1️⃣
توسعه روزانه:
این شبیه‌ساز تقریباً هر روز آپدیت می‌شود و بیلد‌های جدیدی برای سازگاری با بازی‌های بیشتر منتشر می‌کند.
2️⃣
پشتیبانی چندپلتفرمی:
به راحتی روی
ویندوز
،
لینوکس
و
macOS
اجرا می‌شود.
3️⃣
رشد سریع:
در تاریخ اخیر شبیه‌سازهای کنسول، shadPS4 سریع‌ترین روند بلوغ و افزایش سازگاری با بازی‌های بزرگ (Major Titles) را داشته است.
4️⃣
جامعه کاربری فعال:
با بیش از ۳۱ هزار ستاره در گیت‌هاب، این پروژه به یکی از محبوب‌ترین ابزارهای گیمینگ در اکوسیستم متن‌باز تبدیل شده است.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#PS4
#Emulator
#Gaming
#OpenSource
#Github
#Cplusplus
#RetroGaming</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚀
معرفی OpenSERP؛ دسترسی رایگان به API موتورهای جستجو (جایگزین SerpAPI)!
🌐
✨
اگه برای پروژه‌های هوش مصنوعی، سئو (SEO) یا اتوماسیون خودتون به دیتای موتورهای جستجو نیاز دارید و نمی‌خواید هزینه‌های سنگین برای خرید API بپردازید، ابزار
OpenSERP
دقیقاً همون چیزیه که دنبالشید! این پروژه متن‌باز (Open-Source) دسترسی کاملاً رایگان به نتایج Google, Yandex, Bing, Baidu, DuckDuckGo و Ecosia رو از طریق API فراهم می‌کنه.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
بهترین جایگزین سلف‌هاست:
یک جایگزین رایگان و قدرتمند (Self-Hosted) برای سرویس‌های پولی و معروفی مثل SerpAPI, DataForSEO و Tavily.
2️⃣
خروجی مارک‌داون (Markdown):
قابلیت استخراج دیتا از سایت‌ها و نمایش نتایج جستجو به فرمت Markdown (که برای پروژه‌های RAG، ایجنت‌های هوش مصنوعی و LLMها یک ویژگی طلایی محسوب می‌شه).
3️⃣
جستجوی ترکیبی (Megasearch):
این قابلیت به شما اجازه می‌ده تا یک کوئری رو به‌طور همزمان در تمام موتورهای جستجو سرچ کنید و نتایج تجمیع‌شده رو تحویل بگیرید.
4️⃣
کاربردی برای همه:
ابزاری بی‌نظیر برای متخصصین سئو، توسعه‌دهندگان، برنامه‌نویسان وب‌اسکریپینگ و فعالان حوزه هوش مصنوعی.
⚙️
این ابزار رو هم می‌تونید خودتون هاست کنید و هم از نسخه تحت وب و آماده‌ی اون استفاده کنید.
🔗
لینک مخزن گیت‌هاب
🔗
نسخه آماده و تحت وب
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenSERP
#API
#SEO
#WebScraping
#LLM
#RAG
#OpenSource
#Github
#Tools</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚀
آموزش دریافت یک ماه اشتراک رایگان Duolingo Super!
🦉
✨
اگه از برنامه دولینگو برای یادگیری زبان استفاده می‌کنید، الان می‌تونید با یه ترفند خیلی ساده و جذاب، یک ماه اشتراک پریمیوم (Super) این برنامه رو کاملاً رایگان دریافت کنید و از شر تبلیغات و محدودیت‌های جون (Heart) خلاص بشید!
🔥
مراحل دریافت اشتراک:
1️⃣
نصب اپلیکیشن:
ابتدا
اپلیکیشن Webtoon
را دانلود کرده و یک اکانت جدید در آن بسازید.
2️⃣
جستجو:
در نوار جستجوی برنامه، عبارت
Duo Leveling
را سرچ کنید (این کمیک مشترک دولینگو و وبتون است).
3️⃣
اسکرول کردن:
سه قسمت (اپیزود) از این کمیک را باز کنید. (اصلاً نیازی به خواندن نیست، فقط کافیه صفحات را تا انتها به پایین اسکرول کنید!).
4️⃣
دریافت کد:
بلافاصله بعد از انجام این کار، یک کد فعال‌سازی رایگان Duolingo Super به شما داده می‌شود.
👏
5️⃣
فعال‌سازی:
حالا وارد لینک زیر بشید، وارد اکانت دولینگوی خودتون بشید و کد را وارد (Redeem) کنید:
🔗
ورود
🎉
تبریک! اشتراک یک‌ماهه شما فعال شد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Duolingo
#DuolingoSuper
#Webtoon
#FreeAccount
#LanguageLearning
#Tricks
#Education</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚀
تبدیل عکس شما به مینی‌فیگور واقعی لگو (LEGO) با هوش مصنوعی!
🧱
✨
دوست دارید بدانید اگر یک کاراکتر لگو بودید چه شکلی می‌شدید؟ با استفاده از تولیدکننده‌های تصویر هوش مصنوعی و یک پرامپت (دستور) مهندسی‌شده، می‌توانید هر عکسی را به یک رندر سه‌بعدی و فوق‌العاده جذاب از مینی‌فیگور لگو تبدیل کنید!
🔥
ویژگی‌های این استایل جذاب:
1️⃣
حفظ هویت و جزئیات:
لباس‌ها، مدل مو، رنگ مو، حالت چهره و حتی اکسسوری‌ها کاملاً شبیه عکس اصلی شما بازسازی می‌شوند.
2️⃣
رندر فوق‌واقع‌گرایانه (Photorealistic):
اعمال بافت پلاستیک براق لگو، درزهای قالب‌گیری و نورپردازی استودیویی که باعث می‌شود تصویر کاملاً شبیه یک اسباب‌بازی واقعی به نظر برسد.
3️⃣
رعایت دقیق تناسبات:
سر استوانه‌ای، دست‌های گیره‌ای کلاسیک و بدن بلوکی شکلِ استاندارد لگو.
👇
پرامپت (دستور) برای استفاده در Midjourney یا DALL-E 3:
کافی است عکس خود را در هوش مصنوعی آپلود کنید و دستور زیر را به آن بدهید:
>
Turn the person in the uploaded image into a realistic LEGO minifigure, preserving their individuality, clothing, hairstyle, hair color, facial expression, and accessories as much as possible. The character must match the proportions of a LEGO minifigure: a cylindrical head, simple facial features, a blocky torso with printed clothing details, standard LEGO arms and hands, and a molded plastic hairpiece. Use realistic LEGO plastic texture with a glossy sheen, molded seams, and studio lighting. Plain white background, full body photorealistic 3D render from head to toe.
💡
نکته کاربردی:
این ترفند برای ساخت عکس پروفایل‌های بامزه، آواتارهای تیمی و پست‌های خلاقانه شبکه‌های اجتماعی بی‌نظیر است!
🔵
@ArchiveTell
| Bachelor
⚡️
#LEGO
#AI
#Midjourney
#DALLE3
#Prompt
#PromptEngineering
#3DRender
#Avatar</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCf6chPxN55JdmaCk0Uv8afqmJQFGX93MCdIqeszBMbs9IZjYUN4sAPpcF-Fq8uMA3io_Jf711JnFkTAn5ByBwDv2_6NKTQJijH8rPgSJ-OfJOAWJODMkcCDS7JS9AwSPYsBhRK7CqiGSeGs-0W8rf9Nr0o4G54fn6H-zd-y5yqqUY-8iSfGvNTjoOzmWgiasRsQIbZd-9tezBK9jbvM2DdMckItmqbFMjuo2TwVOWxxL-7g4kGtbo_Pwc_IJrhjHkqdvbxTt14QTX5fqWl3UgcM8TpLuMqzzKYGsf4-aw6fYRiwPVpOmgzHYkKJNj_Lwgh_l9gKKsWTGQsxIV242g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی پریمیوم با مرورگر tabbit
🤯
ChatGPT 5.5 Pro
Gemini 3.5 Flash
Claude Opus 4.8
و بیشتر
در دسترس برای
macOS
و
ویندوز
مرورگر را نصب کنید و استفاده از جدیدترین مدل‌های هوش مصنوعی را به صورت رایگان شروع کنید!
🌐
Site
#Ai
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/archivetell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNObNQWBOKuUdo9naIaJU6CH34KWxhc-QUA-yRd9zRw8h-XiQQ8qGbTrGtbBBemEOQtOgNdVbCpj02zfio6CMdl9PbY_9sNsx0vDt-Vc0SxlDN8LBMLHoGofrtNZfOewGjsZB9KABgjZY_BDtDdqhoV4plVyCNYB5CMSSUbrQkLXQoS3yCnJOXNhVJEnYrjWULLC4GKvzA_rfGdxP69MD10UoJJzLsdC8SnWWNnZ2r2YV02fbqjbXFW0pDGqIrV-SRcjl347avRfxleISkYzNTFHK_WbVmIKAF_p76lFTo1Mjj1erE8kicrVVvzj4cKmrRCTDATvQe9Mn93ptvLMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها مدل Qwythos-9B-Claude-Mythos-5 را معرفی کردند که بر پایه Qwen3.5-9B است و قابلیت پردازش ۱ میلیون توکن را دارد!
🤯
✨
قابلیت‌ها:
•
🧠
تنظیم دقیق بر اساس ترکیبی از Claude Mythos و Claude Fable.
•
📚
پنجره متنی گسترده تا ۱,۰۰۰,۰۰۰ توکن!
•
🌐
انتشار کاملاً متن‌باز
•
✍️
همه‌کاره برای کار با متن، کد و اسناد طولانی.
🌐
Site
#OpenSource
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMNXn5fpT29dpSo5Llv77ZToCkFQ2IMbhiAekALqA2aWwCILoNv7TsKAtlr4-XVAtsuuW455kliM4txNJOYw4SzBxTUO2WrT4UIZjNqiG9vTRrTIZgHv3SbubqZ9t7BBvMHOF1fUUy2bKFxbDwuclTxbaK0HdDdAevQ4mbjNWKPZYe9ZnimHDs4Xyz42iOF7HpCoSWLFlx_7_qskLEkMMzTby9JPOljwB_gHEDCMPdlV-Djv1KUU8WpNQaSPYWZI1KmCrH5y3mmvG6hrd1DXCYBQDBdm-_MayS6X7D9V4ryMcUCMM6ZFwZd2qf1qmxmTWZvoHJy4BEnq5SHoAB6w1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
Consensus — جستجو در مقالات علمی
موتور جستجویی برای ۲۰۰ میلیون مقاله علمی. سوال خود را وارد می‌کنید و مجموعه‌ای از تحقیقات مرتبط و خلاصه نتایج آن‌ها را دریافت می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6511" target="_blank">📅 12:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=IFvmsu74h2kh0xYumy4mxbbAkCPVg9rS01-k-fiZQJdDk7-hhd31ueLrhHy1NPXxwQgOR6xMnEzAfnvcEfJOOo1CqQG7hrJCRvA1L0iV8beZ_lI_eWiEXA7U5TF1iPRRQgUxxqnaKtqOGG5QIpsnLOEbmms8lMkhFnsFGuIfVEbsaZNroFuF06myxvTMNBiIO4Sh8Rxd6XgKCDEnX2u5mfvwuWipXgiE_3YNkZVgF3vtnxqP0-d4if22UTR5CiFt-EOXEQdxh_2jb67A1itUjpNvr8XormThHEhP7MddKl3--XBJy0FYMQNOkj8c48zjERFOwObFRRaVJ8oZUGAdSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=IFvmsu74h2kh0xYumy4mxbbAkCPVg9rS01-k-fiZQJdDk7-hhd31ueLrhHy1NPXxwQgOR6xMnEzAfnvcEfJOOo1CqQG7hrJCRvA1L0iV8beZ_lI_eWiEXA7U5TF1iPRRQgUxxqnaKtqOGG5QIpsnLOEbmms8lMkhFnsFGuIfVEbsaZNroFuF06myxvTMNBiIO4Sh8Rxd6XgKCDEnX2u5mfvwuWipXgiE_3YNkZVgF3vtnxqP0-d4if22UTR5CiFt-EOXEQdxh_2jb67A1itUjpNvr8XormThHEhP7MddKl3--XBJy0FYMQNOkj8c48zjERFOwObFRRaVJ8oZUGAdSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗿
افزونه Caveman پرامپت‌ها و پاسخ‌های هوش مصنوعی را فشرده می‌کند
به‌طور خودکار کلمات اضافی را از درخواست‌ها و پاسخ‌ها حذف می‌کند و در عین حال معنی را حفظ می‌کند. با ChatGPT، Claude و Gemini کار می‌کند.
نویسنده ادعا می‌کند که این افزونه می‌تواند مصرف توکن‌ها را تا ۷۵٪ کاهش دهد. ایده ساده است: کلمات کمتر یعنی هزینه کمتر، و معنی باقی می‌ماند.
🌐
افزونه
#Caveman
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
معرفی Firecrawl؛ قدرتمندترین API برای جستجو، استخراج و تعامل با وب در مقیاس بزرگ!
🔥
✨
اگه توسعه‌دهنده، محقق هوش مصنوعی یا دیتا ساینتیست هستید و نیاز دارید اطلاعات سایت‌ها (حتی سایت‌های پیچیده و مبتنی بر جاوا اسکریپت) رو برای مدل‌های زبانی (LLM) یا دیتابیس خودتون استخراج کنید، پروژه
Firecrawl
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید!
🔥
امکانات بی‌نظیر این ابزار:
1️⃣
استخراج هوشمند (Scrape):
تبدیل هر URL به فرمت‌های تر و تمیز مثل Markdown، HTML، اسکرین‌شات یا JSON ساختاریافته در سریع‌ترین زمان ممکن (میانگین ۳.۴ ثانیه).
2️⃣
پوشش ۹۶ درصدی وب:
به راحتی از پس سایت‌های سنگین JS-heavy برمی‌آید.
3️⃣
خزش و نقشه‌برداری (Crawl & Map):
کشف آنی تمام لینک‌های یک سایت و استخراج کل صفحات آن فقط با یک درخواست (Single Request) یا به صورت گروهی (Batch).
4️⃣
عامل هوش مصنوعی (Agent & Interact):
فقط کافیه به زبان ساده توصیف کنید چه دیتایی نیاز دارید تا Agent این ابزار سایت رو بگرده، باهاش تعامل کنه و دیتای مورد نظر رو جمع‌آوری کنه.
5️⃣
متن‌باز و خوش‌ساخت:
هم به صورت سلف‌هاست (Open-Source) و هم سرویس ابری قابل استفاده است و پکیج‌های آماده برای Python و Node.js دارد.
🔗
لینک سایت رسمی:
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Firecrawl
#WebScraping
#API
#AI
#OpenSource
#Github
#Python
#Nodejs
#DeveloperTools</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6509" target="_blank">📅 09:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=scIR_VHWNzgac2zLSmLxYN7XdnzstHVWzo7lPo7UXt6vxW2KtoSPJF5FAKsEJb7E3kXGShKe7QFwtqSFY3eGh2Ko_wrw5pls3OIGTxxWslDCu8ulyS3P46KEu6DfmfpZO15BOCWG2dbxukxkp3vz_PTKTQKY7jQbLr7bcAMBB40YdoxxgkQE00b7Gf6zyCgCWHriNFjPb9tvYDMFdsocCgBLfDUQ5lMJkTyhXFfvirccLxTLodeqYSjN22dpuDyUKUvd2HfZVu2karIoPM6Os0daf5aXYV5gs5VjQJbebh08qHJf9FEBdyClZA1NadS9JUXp7lGb1F9QBGD-W21Fig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=scIR_VHWNzgac2zLSmLxYN7XdnzstHVWzo7lPo7UXt6vxW2KtoSPJF5FAKsEJb7E3kXGShKe7QFwtqSFY3eGh2Ko_wrw5pls3OIGTxxWslDCu8ulyS3P46KEu6DfmfpZO15BOCWG2dbxukxkp3vz_PTKTQKY7jQbLr7bcAMBB40YdoxxgkQE00b7Gf6zyCgCWHriNFjPb9tvYDMFdsocCgBLfDUQ5lMJkTyhXFfvirccLxTLodeqYSjN22dpuDyUKUvd2HfZVu2karIoPM6Os0daf5aXYV5gs5VjQJbebh08qHJf9FEBdyClZA1NadS9JUXp7lGb1F9QBGD-W21Fig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی KanaiAI؛ چیدمان مجازی مبلمان در خانه شما بدون نیاز به حدس و گمان!
🛋
✨
اگه از اندازه‌گیری‌های دستی و خسته‌کننده برای خرید مبل و وسایل دکوراسیون کلافه شدید،
KanaiAI
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار هوش مصنوعی به شما نشون می‌ده که هر وسیله‌ای دقیقاً چطور در فضای خانه شما قرار می‌گیره.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
مدل‌سازی دقیق:
اسکنر هوشمند این سرویس، یک مدل کاملاً دقیق و سه‌بعدی از اتاق یا محیط خانه شما می‌سازد.
2️⃣
خداحافظی با متر و اندازه‌گیری:
دیگه نیازی به محاسبات و درگیری با ابعاد نیست؛ هوش مصنوعی خودش پارامترهای وسایل مورد نظرتون رو با فضای خالی اتاق تطبیق می‌ده.
3️⃣
تجسم واقعی پیش از خرید:
مبلمان و وسایل جدید را قبل از اینکه پولی بابتشان پرداخت کنید، مستقیماً در دکوراسیون منزل خود ببینید!
🔗
لینک ورود به سایت
🔵
@ArchiveTell
| Bachelor
⚡️
#KanaiAI
#AI
#InteriorDesign
#TechNews
#SmartHome
#Architecture</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMO7HY9czF_QwxrOZE25wCxCXNDKVGB1k6cIpkMKItbrGCEDp-0vWHzg2UcyfaywOpVmt43hbiH-arzNsRKoSl_NTa-XjrjOf8JEoQkFHXLRpt1PmdZRoZhfOLvkkNgHzAopJPOzWVHFt4KthNNoi7FtQA2-xyPRcqGGPy5p4gJwMyMpj3gDbq_jUgAagfFoHG06eg9eR1224aAXfQELFbh08w2TH6NdUhick1roHyYCnDkzlzcHVHK3VmBa7YEuCeSdfMF92qqVlkOfvN8pEmgOyqxRCHuw8UktauIwrpEWX1fBSfoM4Ayx-65GvTYgeJL3Euqf__-T_SZ-QKSESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
Navidrome — اسپاتیفای شخصی خودت رو بساز!
سرور موسیقی رایگان و متن‌باز که کامپیوترت رو به یک مرکز پخش موسیقی خصوصی تبدیل می‌کنه.
☁️
✨
چرا عالیه:
•
🏠
رایانه شخصی = مرکز موسیقی خصوصی
•
📱
دسترسی از هر دستگاه: اندروید، iOS، وب، پلیرها
•
☁️
پشتیبانی از فضای ابری — لازم نیست PC همیشه روشن باشه
•
🍓
اجرا روی سخت‌افزار ضعیف
•
🎚️
کنترل کامل — بدون سانسور، بدون محدودیت
•
💸
کاملاً رایگان — بدون اشتراک
🌐
Site
#Navidrome
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6506" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=XTkAiK6W8rCRPogVkA8YpKolxW0PaocgJiWPR5YBVS_el8Vx1p0RiMH_kAUMCPCOjzOrNkP3a__gNbCVyvi4BzCNwYET4prytrj8foOTbzvSBSsTDuLyKd-BA5NEoW0IWZDQxACKY5Tibeou-NpJMrFwcyPfSL-Tbm1NRzqSd8QgWnTPGL8pyiLbygk1_NdRsoU-PEcjICSEHAU7OaeVL3FXHucNEcX3vVEu_yhz2OYRQHrU8iimGdvYTg0a8Vh4stDjkThApXyFisA-AKWdHE15j7QV9zjRa5RijepLwdB0_WDJZzEYtDo0g_zPcfOodwFgS8hM1VggIV1LvOkVDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=XTkAiK6W8rCRPogVkA8YpKolxW0PaocgJiWPR5YBVS_el8Vx1p0RiMH_kAUMCPCOjzOrNkP3a__gNbCVyvi4BzCNwYET4prytrj8foOTbzvSBSsTDuLyKd-BA5NEoW0IWZDQxACKY5Tibeou-NpJMrFwcyPfSL-Tbm1NRzqSd8QgWnTPGL8pyiLbygk1_NdRsoU-PEcjICSEHAU7OaeVL3FXHucNEcX3vVEu_yhz2OYRQHrU8iimGdvYTg0a8Vh4stDjkThApXyFisA-AKWdHE15j7QV9zjRa5RijepLwdB0_WDJZzEYtDo0g_zPcfOodwFgS8hM1VggIV1LvOkVDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
OpenScreen — ضبط صفحه نمایش، سینمایی و حرفه‌ای
✨
قابلیت‌ها:
•
🖱
حرکت روان و طبیعی موس
•
🎨
پس‌زمینه شیک و حرفه‌ای
•
✏️
ویرایشگر داخلی: زوم، سایه، گرد کردن گوشه‌ها
•
💻
سازگار با ویندوز و مک‌اواس
•
💸
رایگان و متن‌باز — رقبا ماهی ۲۰$ می‌گیرند!
🌐
Site
#OpenScreen
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6505" target="_blank">📅 21:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUGx1Zy1-42lFqcr1WCMw4riglDuppPziJBdbVCQ9Yb6rbWUVsce7IsPOrK6c_5gxcxog6wBjRtU8KwtpkWkEIQn9K0EvoqDC32cX0t_2SaB3da8cdStVbXTu0peRbJQGGtc3mVWGaFKM1dvgBJurx-R8J1NwNfJ23eMDVK_AZgPtjGxpDiclQ9m08AnZZdD4aJkkhewxKn4RyzIXQXv8LuLuK8KbHE5j65eVgiEi_Ggv7Wih3NC3sGSVIiMFeqnGDWXcLi9hzby5gEajSh0bF4Y9Vum8o9cJrJm4DEZ2OC4lTDkCCI9r_eGOe2mCBM47vW8nxgW5UTIfwe096Uc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0NpbXzjw0Qry-YkQMB2S_UBrsoLj-Ej5e8OWf5TwSq2I6pgNpADBoEXbLQHZv-EowFi9juvsvXGFgwobxBMOERvBtk0C9f3HBK063HFnHOtq1PE2cnkM-Fvdx245FyyPR_EDVk-4HOT-gNOWjLpa7Op8ygmhfbNl2UioBlxLFQMDa7Fk1J-7GQhLU9BmF848gozP1goq4fnvNNNPLJF4qjtR6C50nXyVBkewmaWNMnY-nICmu57n0RKCqbMEOSJVKkDDT5C45ZoS3v1NoVdo1C2xo6ab36XnpOlDHHjdU4EG1UOO8KEQwgZqzvtckqmboKtu6MgRYDE293pwouAIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗂
PostKeeper
این افزونه توییتر یا X را به آرشیو شخصی شما تبدیل می‌کند
✨
قابلیت‌ها:
•
🔹
خروجی پست‌ها، لایک‌ها، بوک‌مارک‌ها و لیست‌ها
•
📥
دانلود فایل‌های ساختاریافته برای پشتیبان و مرجع
•
🔒
آرشیو محلی و خصوصی روی دستگاه خودتان
•
🧭
جستجو و دسترسی آسان به تاریخچه حساب
•
🛠
متن‌باز با تمرکز بر حریم خصوصی
🌐
سایت
🌐
افزونه
#Twitter
#X
#OpenSource
#Privacy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Upynx1iF0WeS3Sjhkh993lvLBPfUakn5B239Dw3USpOrI0nSWULQOqbP_juH5yKvN9cNs-GIPPXscZNzrXncJoRca2ILOm-KaYhbaYikYxtCRGfkR1PI2CJWc8ggovn0TZpkiOmZbmD476-ftQR72IoGkj4CtJpBOpaLGiidgE-XWwK5058oA6tbcxQUd7DLY_69NbNOUI-SHdDr4AnW2_Zj1b7OPZZIwZZOttJ0Q4BZnc3owNpG-9ExYTGyrZsZNrjaDXD5A2yRXtpfSU-CwwPulg5z9GvzxYSvU1SP-IPzYTddLYezAGmFBcP2LPr2qfPzm3REOYFe-q-Wmuhf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
80 کریدیت رایگان برای دسترسی به برترین مدل‌های جهان مثل Opus، Fable و GPT
✨
همین حالا وارد سایت
kie.ai
شوید
📝
ثبت‌نام کنید و از امکانات فوق‌العاده آن لذت ببرید
🔑
همچنین می‌توانید API Key اختصاصی دریافت کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6502" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔗
tiny_computer
یک محیط دسکتاپ کامل لینوکس (Debian 12) رو فقط با نصب یک فایل APK روی گوشی اندروید بالا میاره!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6499" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTG9QLQXrTUsmB7oJmvTaBqVgcCZLL9zWhriVaRbwCe08HWISjURLHBnZFL8BayWYunMEhMkl4Cv28iO4WO5h8BrBQhpaqTBD3VKtNo299yy1Qg9auTWy3__YHMpOrz5fJHsAbiHiCqDZ0XDgz_yMj9eg4rSHsEUuhczU79co1Hg_mxLsu17_6PZ0_xnKK3NYJxv1WRfey1kO9g9DH0S_fMOPWGS03KUPof6CwlvCxMSGwgLCp-uaEQZKNxqw2mL55SytTOty9Ef4IKNa5IWkAtEzQJL7-84gTHxJ1QQzNtu21WaDQrSuhnWzh2zCVzHKVxXFEu9J1k4pbGou7rJRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ترسناک بقا که قوانین هر مرحله تغییر میکنه ، در تاریکی از Cobb فرار کن و از سیاه‌چال خارج شو.
🌐
Site
#Game
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6498" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=Sj1F7bbAXNS1KU41sqUK_D2SkztztbS81HQHINue-AwF0i_R8gYWdaoHLUtBC2XLQYq_W2RWv0fsGu_5nx5MaWt22c1s7cvbPE7yoJqd_pKf-qRZMp-lDLr4GbAje22WCaqvc1SGrvNJSH2OFX0YpAaWF28irpofGxtNoVSp0alu-WO5KPQ4N0an7F9l_xQbZ52XZRrc944fG6MENXBu0aD6_tnjvQiJSg84HSvR69J7pWRsJ6MRhruLaN04KE7qnJGRP_ku2zrpkzIHfqooNJF843sBZoOq2DyqjrHuUa8djb5horC6I4YCCxzYHVy0ImzshUck3ZYMndeWWdRpDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=Sj1F7bbAXNS1KU41sqUK_D2SkztztbS81HQHINue-AwF0i_R8gYWdaoHLUtBC2XLQYq_W2RWv0fsGu_5nx5MaWt22c1s7cvbPE7yoJqd_pKf-qRZMp-lDLr4GbAje22WCaqvc1SGrvNJSH2OFX0YpAaWF28irpofGxtNoVSp0alu-WO5KPQ4N0an7F9l_xQbZ52XZRrc944fG6MENXBu0aD6_tnjvQiJSg84HSvR69J7pWRsJ6MRhruLaN04KE7qnJGRP_ku2zrpkzIHfqooNJF843sBZoOq2DyqjrHuUa8djb5horC6I4YCCxzYHVy0ImzshUck3ZYMndeWWdRpDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">MagicVideoAI
تبدیل متن به ویدیو
🔥
شرکت ByteDance (تیک‌تاک) ابزار جدیدی برای تبدیل متن به ویدیو ارائه کرده است .
این مدل از نظر پارامترها از Pika 1.0 و Stable Diffusion-XT پیشی گرفته و ویدیوهای فوق‌العاده‌ای بر اساس متن تولید می‌کند.
🌐
Site
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6497" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruuvPrVbfGoLQao8-8F4RfhJak3sZ1Z0kOucQb2ksgJuuxvBbNjdTETHWBYcrmIGCrrvsV2FDgKDaVu1ub1zcvS13FtyIVFFmFpDCSDD0KFQ_4OOJddJFBOSs7THX0TNdT0cHUu2fmRwCE71Pg29k9sdx0phOXDrjqtOx4GMpJhWrnLX2FAWI6c0Gm-1BpkkauHwz5uPtKk_9wp5RiVeBXQYMfwDC8WdlttX8tV_FUV7GJ7QhfBlXJtxldNQuzO0AeaT5GX7wY6W0gJZ_QCJ1Of_ZvGxxGS8mJZCXa4u1DAtqiySUEqdXS-FfDkL_a4qN31FrgFKEMimqkwhaIMUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام
Sakana Fugu
رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک پلتفرم هماهنگ‌کننده چندعاملی (Multi-Agent) است که در قالب یک API واحد (سازگار با فرمت OpenAI) ارائه می‌شود.
🔥
ویژگی‌های شگفت‌انگیز این سیستم:
1️⃣
دو نسخه متفاوت:
نسخه
Fugu Mini
(با تمرکز بر تاخیر بسیار کم و سرعت بالا) و نسخه
Fugu Ultra
(برای پردازش تسک‌های فوق‌العاده سنگین و پیچیده).
2️⃣
معماری کاملاً پویا (Dynamic):
برخلاف سیستم‌های قبلی که نقش‌های ایجنت‌ها از پیش تعیین می‌شد، هسته Fugu یک مدل زبان سبک و خودران است که بسته به میزان سختی تسک، مدل‌های «کارگر» (Worker) را به‌طور خودکار فراخوانی کرده و کار را بین آن‌ها تقسیم می‌کند.
3️⃣
خوداصلاحی و Test-Time Scaling:
این سیستم قابلیت بازگشتی (Recursive) دارد؛ یعنی می‌تواند خروجی‌های قبلی خود را بخواند، اشتباهاتش را تشخیص دهد و یک گردش کار جدید برای اصلاح آن‌ها ایجاد کند.
4️⃣
پادشاهی در بنچمارک‌ها:
نسخه
Fugu Ultra
در تست‌های به‌شدت سخت استدلال و کدنویسی طوفان به پا کرده است! این مدل در تست‌های GPQAD (۹۵.۱)، LCBv6 (۹۳.۲) و SWEPro (۵۴.۲) توانسته مدل‌های پرچمداری مثل
GPT-5.4
،
Gemini 3.1
و
Claude Opus 4.6
را به‌طور کامل شکست دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#SakanaAI
#Fugu
#MultiAgent
#AI
#GPT
#Gemini
#Claude
#TechNews</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6494" target="_blank">📅 10:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚀
معرفی یک راهنمای جامع و فوق‌العاده برای یادگیری زبان انگلیسی!
🇬🇧
✨
اگه دنبال یه نقشه راه اصولی، متفاوت و البته رایگان برای تقویت زبان انگلیسی می‌گردید، ریپازیتوری
English-level-up-tips
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید. این راهنما با یه رویکرد قدم‌به‌قدم، یادگیری زبان رو از یه غول ترسناک به یه پروسه لذت‌بخش و طبیعی تبدیل می‌کنه!
🔥
ویژگی‌های برجسته این راهنما:
1️⃣
پوشش تمامی مهارت‌ها:
از درک مطلب و دایره لغات گرفته تا لیسنینگ، ریدینگ، اسپیکینگ و رایتینگ؛ همه‌چیز در این آموزش گنجانده شده.
2️⃣
یادگیری با قدرت هوش مصنوعی:
یکی از جذاب‌ترین بخش‌های این راهنما، آموزش نحوه استفاده از ابزارهای هوش مصنوعی مثل
ChatGPT
و
Gemini
برای تسریع و بهبود فرآیند یادگیریه.
🤖
3️⃣
مناسب برای همه سطوح:
فرقی نمی‌کنه مبتدی هستید یا پیشرفته، دانشجو هستید یا یک متخصص؛ این مخزن ترفندهای جذابی برای همه داره.
4️⃣
جامعه کاربری پویا:
یک مسیر ساختاریافته که به شما یاد می‌ده یادگیری زبان یک مسیر پیوسته است، نه یک مقصد نهایی!
🔗
لینک مخزن در گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#English
#Learning
#Github
#AI
#ChatGPT
#Gemini
#Roadmap
#Education</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6493" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enL1I02nqXc3_of8QkQCxC4VCwT57j1nEnfPXIMFACtFMJf-ci1_N-oU5IIsFDLwOIh80IKEP0q_RNwHurtRSHhlgjfCWvqCnkGAAEFrLjMm2TgGBIqYIzPBAbuFE1rvc6r0VKhGVHjnjpr8xrpAHtD_T10Aul4o7VdAr3GZvv9iszCsyRnIOuJ65vBaPXsygo111uUqySK2Hxlrhm2qW4nM30AtMkLjYcaj2yGhXVULi_q5dMhQBv_NWDB1UgXjYOCIejBUh5ua1LesNB6RglYh0RB9GzNjZNdjE9FGF7APc-spBEtw_RMSD_fAH75cRyAp_2d4qpUO38GZH2nL5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
ساخت آرشیو اینترنتی شخصی
ابزاری به نام Monolith می‌تواند کل سایت‌ها را در یک فایل HTML مستقل ذخیره کند.
دیگه نیازی نیست نگران باشید که مقاله، دستورالعمل یا مستندات مورد نیاز روزی ناپدید شوند.
✨
قابلیت‌ها:
•
🔹
ذخیره کل صفحه در یک فایل HTML مستقل
•
🖼
نگهداری تصاویر، استایل‌ها و منابع صفحه
•
⚡️
استفاده ساده بدون تنظیمات پیچیده
•
🛠
اجرا روی ویندوز، لینوکس و مک‌اواس
•
📦
رایگان و متن‌باز
🌐
GitHub
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6492" target="_blank">📅 09:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚀
معرفی OpenPencil؛ رقیب متن‌باز و رایگان فیگما مجهز به هوش مصنوعی!
🎨
✨
اگه به دنبال یک ابزار طراحی جایگزین هستید که هزینه‌ای براتون نداشته باشه، با
OpenPencil
آشنا بشید! این ویرایشگر طراحیِ متن‌باز (Open-Source) با قابلیت‌های شگفت‌انگیز هوش مصنوعی منتشر شده و تمام ابزارهای پولی رو به چالش کشیده.
🔥
چه کارهایی می‌تونه انجام بده؟
1️⃣
پشتیبانی از فایل‌های فیگما:
می‌تونید فایل‌های با فرمت
.fig
رو مستقیماً توش باز و ویرایش کنید.
2️⃣
اجرای محلی (Local):
کاملاً آفلاین و روی سیستم شخصی شما اجرا می‌شه، بنابراین حریم خصوصی پروژه‌هاتون کاملاً حفظ می‌شه.
3️⃣
دستیار هوشمند (Agentic AI):
دارای قابلیت‌ها و ایجنت‌های هوش مصنوعی داخلی برای کمک به پروسه طراحی.
4️⃣
خروجی مستقیم کد (جادوی فرانت‌اند!):
طرح‌های شما رو با یک کلیک به کدهای تمیز و آماده‌ی
Tailwind
و
JSX
تبدیل می‌کنه!
⚛️
5️⃣
یکپارچگی عالی:
قابلیت اتصال و هماهنگی کامل با ابزارهای برنامه‌نویسی محبوبی مثل Claude Code و Cursor.
🔗
لینک دریافت پروژه:
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenPencil
#AI
#Figma
#Design
#OpenSource
#Tailwind
#JSX
#FrontEnd
#DeveloperTools</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6490" target="_blank">📅 04:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📰
خلاصه اخبار مهم سایبری و تکنولوژی هفته:
🚨
✨
🔹
آمریکا و توقیف AI:
دولت آمریکا برای اولین بار در تاریخ، انتشار یک مدل هوش مصنوعی (
Claude Fable 5
) را به دلیل خطرات امنیت ملی ممنوع کرد.
🔹
هک بانکی در ایران:
یک حمله سایبری سنگین، سیستم ۴ بانک ایرانی را فلج کرد.
🔹
شنود تلگرام:
پاول دورف اپراتور بزرگ هندی (Reliance) را به رهگیری ترافیک کاربران تلگرام متهم کرد.
🔹
خطای مرگبار هوش مصنوعی:
یک سیستم AI در برزیل با رد درخواست بستری اورژانسی، باعث مرگ یک بیمار شد.
🔹
فریب موتورهای جستجو:
محققان ثابت کردند موتورهای جستجوی پیشرفته AI به‌راحتی با یک کامنت هدفمند در ردیت (Reddit) فریب می‌خورند!
🔹
ابطال گواهی‌های SSL:
شرکت GlobalSign به دلیل تحریم‌ها، گواهی امنیتی هزاران سایت روسی را باطل کرد.
🔵
@ArchiveTell
| Bachelor
⚡️
#CyberNews
#AI
#Telegram
#Security</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6489" target="_blank">📅 23:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6488">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚀
معرفی Prompts.chat؛ خفن‌ترین و جامع‌ترین کتابخانه پرامپت برای هوش مصنوعی!
🤖
✨
اگه می‌خواید از مدل‌های هوش مصنوعی (مثل ChatGPT، Claude، Gemini، Llama، Mistral و...) خروجی‌های تخصصی و بی‌نقص بگیرید، سایت
Prompts.chat
کامل‌ترین مرجع برای شماست!
🔥
چه چیزهایی تو این سایت پیدا می‌شه؟
1️⃣
قالب‌های آماده و کاربردی:
نیاز به نوشتن یه رزومه‌ی حرفه‌ای دارید؟ یا می‌خواید یه قرارداد پیچیده رو تحلیل کنید؟ پرامپتِ آمادش دقیقاً همینجاست.
2️⃣
پوشش تمام نیازها:
از ایده‌پردازی برای کسب‌وکار و تولید محتوای مارکتینگ گرفته تا خلاصه‌نویسی دروس و برنامه‌ریزی تمرینات ورزشی.
3️⃣
خروجی‌های سطح متخصص:
با استفاده از این پرامپت‌های مهندسی‌شده، هوش مصنوعی طوری جواب می‌ده که انگار یه متخصص حرفه‌ای اون متن رو نوشته!
🏆
اعتبار این مجموعه چقدره؟
این فقط یه لیست ساده نیست! این دیتاسِت
رتبه اول بیشترین لایک در Hugging Face
رو داره، بیش از ۴۰ بار در مقالات علمی معتبر بهش ارجاع (Citation) داده شده و حتی در رسانه‌های بزرگی مثل Forbes و دانشگاه‌های تراز اولی مثل هاروارد و کلمبیا هم ازش نام برده شده!
🔗
لینک ورود به مرجع پرامپت‌ها
🔵
@ArchiveTell
| Bachelor
⚡️
#Prompts
#AI
#ChatGPT
#Claude
#Gemini
#HuggingFace
#Tools
#Productivity</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6488" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚀
معرفی Upscayl؛ افزایش بی‌نظیر کیفیت تصاویر با قدرت هوش مصنوعی!
🖼
✨
اگه عکس‌های بی‌کیفیت، تار یا سایز کوچکی دارید و می‌خواید رزولوشن اون‌ها رو بدون افت کیفیت به شدت بالا ببرید،
Upscayl
دقیقاً همون ابزاریه که نیاز دارید! این نرم‌افزار کاملاً رایگان و متن‌باز (Open-Source) با استفاده از پیشرفته‌ترین مدل‌های هوش مصنوعی، معجزه می‌کنه.
🔥
ویژگی‌های کلیدی:
1️⃣
پردازش گروهی (Batch Processing):
می‌تونید یه پوشه پر از عکس رو بهش بدید تا همه رو با هم و به صورت خودکار باکیفیت کنه.
2️⃣
افزایش وضوح و شارپنس:
رفع تاری، نویز و پیکسلی بودن عکس‌ها به طبیعی‌ترین شکل ممکن.
3️⃣
مدل‌های سفارشی:
امکان اضافه کردن و استفاده از مدل‌های هوش مصنوعی دلخواه برای رسیدن به بهترین نتیجه ممکن.
4️⃣
پشتیبانی کامل:
سازگاری با سیستم‌عامل‌های ویندوز، لینوکس و مک‌اواس (macOS).
⚙️
نکات فنی:
* این برنامه با زبان قدرتمند TypeScript توسعه داده شده است.
* برای اجرای پردازش‌های این ابزار، سیستم شما به یک کارت گرافیک (GPU) سازگار با Vulkan 1.3 نیاز دارد.
🔗
لینک دریافت و گیت‌هاب پروژه:
🔵
@ArchiveTell
| Bachelor
⚡️
#Upscayl
#AI
#OpenSource
#ImageUpscaling
#Tools
#TypeScript
#Github</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6487" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yr3Beb3muYHkQtK2Gw7yKcPK8wUepeMboloblAmRCtTWXfvKESpuhZcRotI7jcgSTFMB61grJE2nXJEDdL-BM-Je_RqkXxVRDsfzH0KwC6WQLMgM6m_5J8VraiNFb49rq7gFpZa9wVtA5iwBbOMONhi1GEj6UahG8gCYLskSnPh_puPl8yvwR-1bgn6lcl7Q2MMDh4LJmDZjE-l0RZYdZgywWY11fqgb1boMoS9mRrbftEJvOl-sDMVflKbT3FFG2Jw65YTsQbCCGxZic8PEW1Ode8TMhF-J-AkOXKoDxdCMyTo47ju0ao36OclOmc8z172id3JvH28D9V2qieAxzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjXAITbCwNfXoUePe24BNKPx24Zwk4XRiYa3gPvQACQYpa3QwcMZii_Z9xp7bo9Xv1b5339qLk8l6UT7jhL1fPyVCYokQe6QkUEhzHcJUjIxCpImki95pF3t4ncrl2ozfpB-OwTOICgnbwgPJ2wRZ-XjaiW8ZjE_lWUEBS-7NqE26qFOAaCwIPym6uYAzQtMEPY-tE728sq9fu6UEvu9YZkprhlellwGBewKY9Gc082H8NTeApE-HJ4QXDTB-PNf_W9O8ICnut-QEGTgwmYRq2YlmkiL04BW1trSK1drvWf64hAlBqaNqoJ-i9XTw3WRiKa94GESW5xdrQC4Aq8IJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
معرفی Lift؛ هوش مصنوعی رایگان برای استخراج و پارس کردن فایل‌های PDF!
📄
✨
تیم Datalab به‌تازگی مدل هوش مصنوعی قدرتمندی به نام
Lift
رو منتشر کرده که می‌تونه داده‌ها و اطلاعات رو از فایل‌های PDF و تصاویر بخونه و در نهایت یک خروجی کاملاً ساختاریافته و تمیز با فرمت
JSON
بهتون تحویل بده.
🔥
ویژگی‌های کلیدی و برجسته:
1️⃣
دقت و کیفیت شگفت‌انگیز:
توسعه‌دهندگان این مدل ادعا می‌کنن که کیفیت خروجی Lift به‌شدت نزدیک به مدل قدرتمند Gemini Flash هست و از خیلی از مدل‌های متن‌باز (Open-Source) فعلی بهتر و دقیق‌تر عمل می‌کنه.
2️⃣
خروجی ساختاریافته (JSON):
این مدل دقیقاً خوراک برنامه‌نویس‌هاست! داده‌های خام، جداول و متن‌های به‌هم‌ریخته رو می‌گیره و یه دیتای مرتب و آماده‌ی استفاده تحویل می‌ده.
3️⃣
کاملاً رایگان و در دسترس:
این شبکه عصبی صددرصد رایگان و متن‌باز منتشر شده و می‌تونید بدون هیچ هزینه‌ای ازش تو پروژه‌هاتون استفاده کنید.
🔗
لینک‌های دسترسی و دانلود:
گیت‌هاب پروژه
مدل در هاگینگ‌فیس
🔵
@ArchiveTell
| Bachelor
⚡️
#Lift
#AI
#PDF
#JSON
#OpenSource
#DataExtraction
#DeveloperTools</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6481" target="_blank">📅 16:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prd0tZE8cFrYvxsaNJshij0-O0e3wbMix8kwfVSlT_LUW8-pm_lVygg4uFmpxEzFH0Jc3vqnyGERKRG0YsErsVUKiw9KxAHCa3phQZCmnh6H9YxSysKjwrrX5eLXYpZdKUj5GdTr-nykNBQJmERe9wX2H3dvxJkyYpzUiYuI6An37cl_Yu_10fmgrK-WY0etl7OypnZVzjooU6awtkY0jKLjom2OHPIEm-S96xmQw8FULUDu4Dpbkcwyp8S0jAAbCVtsLdqxC81cxsnu4yyj6Pt95os7GPXIfmZNV4CQVL4PvKMPjt2qRMhpYIK06devckQ-b8wm0IPwKRgsyGrjCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
مدل Gemini 3.5 Pro احتمالاً ۹ تیر (۳۰ ژوئن) منتشر می‌شود!
🚀
✨
🔹
شایعات داغ:
کاربران شبکه X پیش‌بینی می‌کنند که این مدل قدرتمند دقیقاً در آخرین روز از مهلت وعده داده‌شده توسط مدیرعامل گوگل (۳۰ ژوئن) منتشر شود.
🔹
سوتی عجیب گوگل:
در حین آماده‌سازی بک‌اند برای این آپدیت جدید، رابط کاربری تحت وب Gemini باگ داده و اشتباهاً پاپ‌آپ معرفی نسخه‌های قدیمی (2.0) رو برای کاربران نمایش داده!
🔹
نتیجه‌گیری:
این گاف فنی نشون داد که نسخه وب جمنای هنوز پر از کدهای قدیمی (Legacy) و باگ‌های پیش‌پاافتادست.
🔵
@ArchiveTell
| Bachelor
⚡️
#Gemini
#Google
#AI
#TechNews</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6480" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚀
معرفی WinScript؛ ابزار قدرتمند و متن‌باز برای شخصی‌سازی و بهینه‌سازی ویندوز!
🛠
✨
اگه دنبال یه ابزار سبک، ساده و متن‌باز (Open-Source) برای شخصی‌سازی، سبک‌سازی و افزایش سرعت ویندوزتون هستید،
WinScript
رو از دست ندید. این برنامه به شما اجازه می‌ده اسکریپت‌های اختصاصی خودتون رو برای ویندوز بسازید و روی هر سیستمی که دوست دارید اجرا کنید!
نحوه کار:
خیلی سادست! تو رابط کاربری برنامه، تیک قابلیت‌هایی که می‌خواید حذف یا بهینه‌سازی بشن رو می‌زنید، یه اسکریپت آماده تحویل می‌گیرید و هر زمان که خواستید اون رو روی سیستم خودتون یا هر سیستم دیگه‌ای اجرا می‌کنید.
🔥
امکانات و ویژگی‌های کلیدی:
1️⃣
حذف برنامه‌های اضافی (Debloat):
پاک کردن اپلیکیشن‌های پیش‌فرض و مزاحم ویندوز مثل Copilot، Edge، OneDrive و سایر نرم‌افزارهای غیرضروری (Bloatware).
2️⃣
حفظ حریم خصوصی:
غیرفعال کردن کامل تله‌متری (ردیابی اطلاعات) ویندوز و برنامه‌های شخص ثالث، و مسدود کردن دسترسی و جمع‌آوری داده‌ها.
3️⃣
بهینه‌سازی فوق‌العاده:
تغییر وضعیت سرویس‌های پس‌زمینه به حالت دستی (Manual) برای آزادسازی منابع سیستم، تنظیم DNS و پاک‌سازی فایل‌های موقت (Temp).
4️⃣
نصب سریع نرم‌افزارها:
امکان نصب گروهی و یک‌کلیکه‌ی تمام برنامه‌های مورد نیازتون با استفاده از ابزار قدرتمند Chocolatey.
⚠️
نکات مهم پیش از اجرا:
* اسکریپت تولیدشده حتماً باید با دسترسی ادمین (Run as Administrator) اجرا بشه.
* چون این ابزار تنظیمات ریشه‌ای سیستم رو تغییر می‌ده، ممکنه آنتی‌ویروس (Windows Defender) بهش گیر بده که این یک هشدار اشتباه (False Positive) است. با توجه به متن‌باز بودن پروژه، خیالتون از بابت امنیت راحت باشه.
⚙️
سازگاری:
ویندوز ۱۰ و ویندوز ۱۱ (کاملاً رایگان - لایسنس GPL-3.0)
🔗
لینک دانلود / گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#WinScript
#Windows
#Windows11
#Optimization
#Debloat
#Privacy
#OpenSource</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6479" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLrUr01ySmLc2w7a4WAX0vpmc_Pyk3hWMYviypEn3jzrwD8uvv5Xln4pr1gwzAIMIjmO4DsSCglY-4FJQi6m1G5ZtR2n0I_Ub_R3FVlmkLScLItJ184oJIOaDT_mLfZc7ZBf9ELGeDeYD3dhPXmovoQFnobfUHpPax0_YllXeBOGgz7Dk905GKrvZ7g-HcLxv2XVOcikEa7xjcC0DeQv7WpKpN6qLmYuAJuF_fpWvoEdewUVuD2VHiK8JlgYoKrXXnkOAVrf1k0lWvl4JE-rTqiy970Y5I1UucQKdXHnalsA1fDYUD5ua-tPvR1sVQ3Twnm2xrFD2-3ggJLwohcNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با GeoSpy AI می‌توانید محل احتمالی ثبت یک عکس را از روی جزئیات تصویر پیدا کنید.
•
🔹
تحلیل جزئیات عکس و مقایسه با تصاویر آنلاین
•
📍
ارائه مکان‌های احتمالی همراه با مختصات
•
🎯
مرتب‌سازی نتایج بر اساس احتمال تطابق
•
🏞
دقت بالاتر در مناظر طبیعی و معماری خاص
🔗
لینک:
Site
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6478" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTsurGiZODpIamq7q4nZ-VSxuNYoKmHcJnVDjWe47V0xKDxZySLltAVCvvgsa9eNSQxE7dQrWuQoM0zPej-HdZg0IeqjZezrMUWx808uHJsNcfytchDM9M_u0ZW5x9CCeozfpfWIiDIlOk3LJ7J6J2p7tsa9mtI1f8Amjqk8N2Nxxs9Zf8blxbWISNqxejUPtGGcXvHAOafIBHtY0M8ljijIbbZIVVAS5nJ1TtZv_sQdN0MEmJXu6odQNZB1wV4tvrReY9usRzO24YoHbYeYSHJmyf4-V6jwueOrRqhLu6C5LAlWZ74m9d965xKa85hi9HLaFhmP_CoxmBwHyXK9Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی کاملاً رایگان به مدل‌های هوش مصنوعی با Unlimited AI!
🤖
✨
اگه دنبال یه راه بی‌دردسر و مجانی برای استفاده از مدل‌های هوش مصنوعی هستید، سایت
Unlimited AI
دقیقاً همون چیزیه که نیاز دارید!
🔗
لینک‌های دسترسی سریع:
🌐
وب‌سایت اصلی:
🛠
اسکریپت واسط (Transfer API):
اگه برنامه‌نویس هستید و می‌خواید این سرویس رو به پروژه‌هاتون متصل کنید و ازش خروجی API بگیرید، این ریپازیتوری
گیت‌هاب
کارتون رو راه می‌اندازه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#FreeAI
#API
#Tools
#Github</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=JfblPay4yRX4aycjCTTH2Pu6wAkUGY2cqptECdi7Uo3Ki2wITS1jsbFnhUpLMQRQbevWwXMkz6wjhcQYp3443wsajPjvc1yUCgGj2fcoCrfABb64t6kgnNneD4B1t2RT7EKC_9cVyN33z6G10W0L1zRWyykTH9nU8ZItUH5wrONhwG-nX9PoOQhmOjq4GMrSF2H0kbjPG442oXUJ3nN9uF55CPeB7pMq3iCbnN9N0YpXzki1Q0iGcYwyTtdYbt8edI3eqqT-7Ud9M_NqRqr4pCBJdsLSq60JtIyGDV_CcWaryHoHZAszQndvrLAuuh-Ouafh3vvIl-xZSc809qVFHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=JfblPay4yRX4aycjCTTH2Pu6wAkUGY2cqptECdi7Uo3Ki2wITS1jsbFnhUpLMQRQbevWwXMkz6wjhcQYp3443wsajPjvc1yUCgGj2fcoCrfABb64t6kgnNneD4B1t2RT7EKC_9cVyN33z6G10W0L1zRWyykTH9nU8ZItUH5wrONhwG-nX9PoOQhmOjq4GMrSF2H0kbjPG442oXUJ3nN9uF55CPeB7pMq3iCbnN9N0YpXzki1Q0iGcYwyTtdYbt8edI3eqqT-7Ud9M_NqRqr4pCBJdsLSq60JtIyGDV_CcWaryHoHZAszQndvrLAuuh-Ouafh3vvIl-xZSc809qVFHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
گوشی‌تان را به کنسول رترو تبدیل کنید؛ صدها بازی کلاسیک مستقیم در مرورگر.
•
🕹
بازی‌های PS1، Game Boy، Sega و پلتفرم‌های نوستالژیک
•
⚡️
بدون نصب، حساب کاربری یا اشتراک
•
📱
💻
قابل اجرا روی موبایل و کامپیوتر
•
🎮
پشتیبانی از گیم‌پد
•
🆓
رایگان و آماده اجرا
🔗
لینک:
Site
#Gaming
#Retro
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8rQxn-uwzoX3um2zGSyUB0Y815RWFm1ogW3KpTn_q49S5C9juJIpgsDQ0_1NfocG_E5Q24EXW5Dh8c2JldfN6Td6FGhcmIdME7N0MNPhrgegSJaSzZOl9xjqPZV_2Ge3msj-D5XsZ03k1bQoQcMPeyy8Hq2ht3zgJYJjkicLkXgqW4cP47aDvZHE5TvH9e_dV0d4vpUSce_EBeuKDv0rDUQuKw8TZJseZ3bx0Q69plHdTN1_cefcRzrOCCIjZHZ0dnokJkk6avHyBx8bl9qm20l7-E5jrcAjaOhomzTl_pE1oUfoI8OPgVrXzDje6-MxBTNSX4Gaiaz6bQWjayqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به API مدل DeepSeek-V4-Flash تا ۲۸ ژوئن!
🤖
✨
یه فرصت بی‌نظیر! می‌تونید مدل جدید و فوق‌سریع DeepSeek رو تا ۲۸ ژوئن (۷ تیر) از طریق API کاملاً رایگان دریافت کنید و بدون پرداخت هیچ هزینه‌ای برای توکن‌ها، پروژه‌هاتون رو باهاش پیش ببرید.
🔥
چه کارهایی می‌تونه انجام بده؟
1️⃣
تولید کد و اتوماسیون:
ایده‌آل برای کدنویسی و سناریوهای عامل‌محور (Agentic).
2️⃣
تحلیل و تسک‌های فنی:
عملکرد عالی در تحلیل داده‌ها، تولید محتوای متنی و حل مسائل تکنیکال.
3️⃣
پروتوتایپینگ سریع:
تست سریع ایده‌ها و ساخت نمونه‌های اولیه بدون هیچ نگرانی بابت هزینه‌های API.
4️⃣
پروژه‌های خلاقانه:
خوراکِ آزمایش و پیاده‌سازی روی ربات‌ها، سرورهای بازی و سایر پروژه‌های خاص و غیرمعمول.
🔗
لینک دریافت رایگان
🔵
@ArchiveTell
| Bachelor
⚡️
#DeepSeek
#API
#AI
#Free
#DeveloperTools
#LLM</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvISBj3Ch1saodKaYHulr5Js33dgNQbJNZ7mpEIlEJCuYHcnAxakUEx4dfBbzR3nTec0fZgbrwAUYPvIIH3nXOMrGxqXOCjpCh0l2kQzZf2lrIbCL51NvXiIQalsTCRpA-4SKdjpVZXB4LwYq9E8EsWISxAmUlWC991kwV6a1q-1CrlWnZpM7fnsWwQBK7AHr45sda0IoIzeC9ZTWKLbeV-yZRBP_bNvZrGONiYIkFr5HRQj7sHxVdkfMDI-6L6vBMYudkBRwUNtaUCZJ-Dq4GyxCvdk_yZbfu-zYyLpe-QZgHWsUfLdbM3FAT9kmoTy1_t9RsuJw7JggjS5D7GicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دریافت یک ماه اشتراک پلاس رایگان پلتفرم HotGen AI!
🤩
✨
اگه به دنبال استفاده از قوی‌ترین مدل‌های تولید عکس و ویدیوی هوش مصنوعی هستید، الان می‌تونید اکانت پلاس پلتفرم
HotGen
رو به مدت یک ماه کاملاً رایگان دریافت کنید!
🔥
مدل‌های قدرتمندی که براتون باز می‌شن:
>
🔹
Seedance 2.0
>
🔹
Kling 3.0
>
🔹
Google Veo 3.1
>
🔹
WAN
🛠
مراحل دریافت (بدون نیاز به شماره و کارت بانکی):
1️⃣
وارد سایت
https://hotgen.ai
بشید.
2️⃣
خیلی راحت با اکانت گوگل ثبت‌نام کنید.
3️⃣
توی داشبورد کاربری‌تون، بخش
Tasks
رو باز کنید.
4️⃣
هر ۶ تسک ساده رو انجام بدید (ساخت یک عکس، ساخت یک ویدیو، اشتراک‌گذاری و غیره).
تمام! اشتراک پلاس شما به‌صورت خودکار فعال می‌شه.
✅
🎁
با این اشتراک چی می‌گیرید؟
به مدت ۳۰ روز، سقف محدودیت‌های تولید ویدیو و تصویر برای شما به‌شدت افزایش پیدا می‌کنه و می‌تونید از بهترین مدل‌های روز دنیا با بالاترین ظرفیت استفاده کنید.
(البته جمع کردن توکن به این راحتی نیست. زاییده شدم
😂
، الان تست کردم)
🔵
@ArchiveTell
| Bachelor
⚡️
#HotGen
#AI
#Free
#Kling
#GoogleVeo
#VideoGeneration</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚀
معرفی Remnawave؛ پنل مدیریت پروکسی قدرتمند و مدرن مبتنی بر Xray-core!
🌊
✨
اگه دنبال یه ابزار حرفه‌ای برای مدیریت زیرساخت پروکسی می‌گردید،
Remnawave
با تمرکز روی سادگی و راحتی کاربر طراحی شده است. این پنل به شما اجازه می‌ده نودها، کاربران و اشتراک‌ها رو در یک رابط کاربری وب بسیار تمیز و به‌صورت یکپارچه مدیریت کنید.
تمام بخش‌های این پروژه (بک‌اند، فرانت‌اند و نود) کاملاً با TypeScript و با استفاده از فریم‌ورک‌های NestJS و React توسعه داده شده است.
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
معماری ماژولار و بهینه:
دیتابیس، پنل وب و صفحه اشتراک (Sub Page) کاملاً قابل تفکیک هستند. یکی از بهترین قابلیت‌ها اینه که حتی اگه پنل شما آفلاین بشه، نودها بدون مشکل به کارشون ادامه می‌دن!
2️⃣
مدیریت حرفه‌ای کاربران:
تعیین محدودیت ترافیک، فیلترها و قابلیت جذابِ محدود کردن اتصال به دستگاه‌های خاص از طریق شناسه سخت‌افزار (HWID).
3️⃣
مانیتورینگ و امنیت بالا:
مانیتورینگ لحظه‌ای ترافیک کاربران و نودها، پشتیبانی از ورود با اکانت تلگرام (OAuth)، احراز هویت دو مرحله‌ای (2FA) و هماهنگی کامل با Cloudflare Zero Trust.
4️⃣
امکانات ویژه:
تولید انواع فرمت اشتراک (مثل Mihomo و Sing-box)، پشتیبانی از وب‌هوک (Webhook) برای کاربران و نودها و ابزار داخلی برای اعتبارسنجی کانفیگ‌های Xray.
﻿
⚙️
حداقل سیستم مورد نیاز:
برای نصب این سیستم قدرتمند (از طریق داکر)، به
۲ گیگابایت رم
،
۲ هسته پردازنده
و
۲۰ گیگابایت فضای ذخیره‌سازی
نیاز دارید.
🔗
لینک‌های دسترسی سریع:
داکیومنت
گیت‌هاب
داکر هاب
کامیونیتی
🔵
@ArchiveTell
| Bachelor
⚡️
#Remnawave
#Xray
#Proxy
#VPN
#OpenSource
#TypeScript
#Tools</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NusW6Fmv9Mlbb5pwfjQgYGdLCOcmPmfhYrYBn9uLpAYu8T66nGU18YhrQoicu4htFylxeDnQDKLFAV-xM6xEXm7uAdjADLnjn8HXyY1ne3J5lJwheaBseJ1NYEZvF_DuQRRBXlAVSr9Pa8ycefyKsB94ItqQhLeGduLWc1506UOA29HYBoVOsFcprtMAL1ORXYGPdkY77iPSxlFvyif_MleUML9Mqq8Kgqc-xMUT8ASL4pffmWBsM5p3Uu2zj-zBKWMrcOtG7LpgJy51xhXPZ5hG-j8taLoHn_Wt8U0tncM2IsBEPUDToW3G3EyR4HIwgLabrX-A2AoIO6vTRSb4xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
یک کتابخانه رایگان از پرامپت‌های Nano Banana برای ساخت تصویر با
AI Studio
منتشر شده است.
✨
قابلیت‌ها:
•
🔹
پوشش سناریوهای متنوع برای تولید تصویر
•
⚡️
قابل استفاده رایگان در AI Studio
•
🗂
دسته‌بندی منظم و جستجوی سریع
•
🔄
به‌روزرسانی مداوم با پرامپت‌های جدید
🔗
لینک:
Site
#AI
#Prompts
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚀
معرفی Ladder؛ عبور از پی‌وال‌ها و خواندن رایگان مقالات پولی با یک کلیک!
🔓
✨
🔥
🔥
🔥
اگه برای خوندن مقالات، اخبار یا کتاب‌های معتبر تو سایت‌های خارجی با درخواست خرید اشتراک و صفحه‌های پرداخت (Paywall) مواجه می‌شید، ابزار
Ladder
این مشکل رو برای همیشه حل کرده! این سرویس با شبیه‌سازی رفتار بات‌های موتور جستجو، بهتون اجازه می‌ده محدودیت‌های هزاران سایت رو دور بزنید.
🔥
ویژگی‌های جذاب و کاربردی:
1️⃣
دسترسی نامحدود:
باز کردن مقالات پولی و ویژه در سایت‌های معتبر علمی و خبری مثل WSJ, NYT, Bloomberg, The Atlantic, Nature, Science, The Lancet و کلی سایت دیگه.
2️⃣
وب‌گردی بدون مزاحم:
حذف خودکار تمامی تبلیغات، بنرهای پاپ‌آپ، ترکرها (ردیاب‌ها) و اسکریپت‌های اضافی، تا یک تجربه مطالعه تمیز و راحت داشته باشید.
3️⃣
نصب و اجرای منعطف:
می‌تونید این ابزار رو روی سرور شخصی خودتون (Self-hosted) یا حتی به‌صورت لوکال روی سیستم (PC) نصب و اجرا کنید.
🔗
لینک دریافت ابزار
🔵
@ArchiveTell
| Bachelor
⚡️
#Ladder
#Paywall
#Bypass
#Articles
#Tools
#OpenSource</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZLhGMvuvs4WwiVBzXhvnS9ZvPdofNBMQv0VaGd27G1reuf310C7d61eFaayqlql9LOYgB8Uty-2o7ZRFC00bIgAwTaqTvLd5k3M-fJ__1ati5mW7u4MCufZYJi2UskhY9Uhah6isnEjCkASVkU6oUoiH1q-pcOdgemsd6ZD0jdajQocoAjdzgnnF32YbJZfjXYhrPAIst3p_x2Yt0eu8afwHuNdovSYjS-7IcensNXITtFJIVUhee2Q7cgLtTmusornNqZ9KIITZyN2YqqAjNTGvlyV6IL1SfFzTGrljzsjzfBIDjheVrBWVPHZqcmq_mreu1Dj3ZIh60mFQLT6HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
بازی‌های کلاسیک کنسولی را مستقیم داخل مرورگر اجرا کنید؛ بدون نصب و دردسر.
✨
قابلیت‌ها:
•
🎮
شبیه‌سازی کنسول‌های Nintendo، Atari، Sega و دیگر پلتفرم‌های قدیمی
•
⚡
انتخاب بازی و اجرای سریع از داخل سایت
•
📦
امکان آپلود فایل ROM برای بازی‌های دلخواه
•
☁️
همگام‌سازی ذخیره‌ها با فضای ابری بین دستگاه‌ها
🔗
لینک:
Site
#Gaming
#RetroGames
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎬
معرفی OpenMontage؛ استودیوی شخصی و هوشمند شما برای ساخت ویدیو!
🚀
✨
اگه تدوین ویدیو بلد نیستید اما ایده‌های جذابی تو سرتون دارید، ابزار جدید و متن‌باز
OpenMontage
دقیقاً برای شماست! این هوش مصنوعی خفن، فقط با خوندن توضیحات ساده‌ی شما، یک ویدیوی کامل و حرفه‌ای تحویلتون می‌ده.
🔥
ویژگی‌های جذاب و کاربردی:
1️⃣
صفر تا صد اتوماتیک:
از ایده و سناریونویسی گرفته تا پیدا کردن متریال (عکس، ویدیو، موزیک)، صداگذاری و تدوین نهایی رو خودش انجام می‌ده.
2️⃣
الهام‌گیری از یوتیوب:
فقط کافیه لینک یه ویدیوی یوتیوب رو بهش بدید تا سبک، ریتم و حال‌وهوای اون رو تحلیل کنه و یه ویدیوی جدید با همون فرمون براتون بسازه!
3️⃣
اتصال به ابزارهای مختلف:
این سیستم به ده‌ها هوش مصنوعی دیگه (برای تولید عکس، صدا و موسیقی استوک) وصل می‌شه تا باکیفیت‌ترین خروجی رو بهتون بده.
این ابزار کار رو برای تولیدکنندگان محتوا، معلم‌ها و هرکسی که می‌خواد بدون دردسر ویدیو بسازه، به‌شدت راحت کرده!
🔗
لینک ابزار (گیت‌هاب)
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenMontage
#Video
#AI
#ContentCreator
#Tools</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DX2SOe6bQU0fv9VmiN4MgypdFHmsM6C4OWZw9qwyXXlBeKU2mybTxwQxAtR4rYwZG77hS8AO2HTG7K8vD3-2nzKpwat47V6taSZIzMgwUxCklpt7d7QyouULdNIzE_gdz6y4OryHSF9WF6k-hUozeYVHHUTpt87Gyz3NPcCNfKmZlPfxzggXw0qAVwi8-aPP_sYkkY1M7K6dWDcz71zHk8saEwBA-44XRz8h-7iXOmU_VcbPFQJVHWDQ4MK9x8eeRx8LTK1kXhKIF_EBzFkCjFaGbvzDcxB6hLyD-4rTE6J1XfxUsLti1A2JmIAbT9YUyBy5lkOBK2xscP4dV2Dg3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAF8w4cbHEFlagMz48--8ehAAVQYYJ3Ag1GcehB8ScS9om7F5hCBfQClkHeCeI__PGeAACUoC2bEcN2tlYKfmgdt4IEuTOx3dXGst8VzVLAhhQ_fnEWI59c9csm23waFxhc8XiPUyQVgmgrgYGWlMVCcQRPlPgZNN4J4F6m_Fbs32jSJFPHTHc1JkT_AkqlCja2F7248AeKYo0ImiS1K8cNu-dsauoPK6rGJM2K-nsTysk0wsQg5WEgrcnOns_ofwmJ3ri7c_Ma3aGDOzu02UBSHwnVUbrqRupzJ3eQyUo9W-R75GcixaCjF3xqkfg1MHRiBpKYSMUVx1extm3I6TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2lY-rurimKeqW4Zxf6cs2K5ixSZYS2u_41QJgV1OXXOCYBYHtRUqdHZk5nE1Wz-QrPSp1cTpjNWQc6UENnlWR_Xl2IKL-vBeFWf0mZboR26uXKGRiP56um0PhN7L2qc_D3YQ6dpPcOiMGMonz0NGe5K3HoxHsI55vT4MnwthNX9BXCoWD_qU3wiYE4fQXF52Ho3MnySTkYqO9zeJBKYRIhF4dIFqd2twyRePZVeeKwh7xLWNwW_MWbHRSyl6bjXJMu5g-llabTVMJ2k9T3XLur_rOJZgoqCogpw60OoQVEGPWY_-0Oxr44xeOz4wl4CrQam2foc94OBouMlU9WD9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZIUkmWcrRBByomGf8MsVk7RGhRif-mHG3nXlrSatYmprJMzPJL2r2Y4gOcla53iLQoO5HjNHtR4KhANSFGFlBvLx8hOBEGzEHaTZztlqxnkNXxxblhaWp-K7zUWf76zwnlKlAx0EarWW5ms8aCf6yeUiShjpAI9HJ5OqKFFrUYxg91YtNlimZqN-kpDGMwVvEbiT5IGgYVB2r04e_1gjgS2wtVbJUdVYcX0MwKtfyDsccFfT7tWuoU9Mok8XdwOxDGL34ogUyJIOt6e8JXuaQQbQd7r78Q17gczdMIKFr1hpwoIgwpKCIenzoW2O1WgSw9l64imnmmLFNSk0HSq0IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Splayer
پخش‌کننده موسیقی متن‌باز با قابلیت دانلود از یوتیوب و اتصال به اسپاتیفای
🎵
✨
قابلیت‌ها:
•
🔹
پخش فایل‌های محلی و مدیریت موسیقی‌ها
•
⚡
دانلود صوت و ویدئو از YouTube
•
🛠️
واردکردن پلی‌لیست‌های Spotify
•
🎧
متن همگام‌شده آهنگ‌ها، پادکست و کتاب صوتی
•
🎚️
اکولایزر پنج‌باند، ویژوالایزر و ویرایشگر صوتی
•
🎨
شخصی‌سازی تم و رابط کاربری
🔗
لینک:
GitHub
#OpenSource
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚀
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
تبدیل سایت به اپلیکیشن: هر سایتی که فکرش رو بکنید (مثل ChatGPT، یوتوب، ایکس/توییتر، اسپاتیفای، دیسکورد و...) رو به یک برنامه دسکتاپ مجزا تبدیل می‌کنه.
2️⃣
حجم فوق‌العاده کم: برنامه‌های ساخته‌شده با این ابزار تا ۲۰ برابر کمتر از اپلیکیشن‌های سنگین مبتنی بر Electron فضا اشغال می‌کنن.
3️⃣
سایز مینیاتوری: میانگین حجم هر اپلیکیشنی که باهاش می‌سازید فقط حدود ۱۰ مگابایته!
4️⃣
مصرف بهینه منابع: به لطف استفاده از قدرت زبان Rust و فریم‌ورک Tauri، مصرف رم سیستم به طرز چشمگیری کاهش پیدا می‌کنه.
5️⃣
پشتیبانی کامل: این ابزار کاملاً رایگانه و روی ویندوز، مک (macOS) و لینوکس بدون مشکل کار می‌کنه.</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEth0PUFqAJm5Tdqfu2lYberhMr4tlVfnTv6YBpzVsBV75_gVJIU3zTIbOpz25DmaBVm9kVyQo-Y1FM3XzsRHcRG5AhkhRqTESuU09aiG8yqakgf-yZDTE7uEf2rACXQ9Le5fyqH4g9ENIIcAXz6aVqSwPPo-K56AwsbNvZcOITNPH83Wz-lKL1yDkp3Kf4msd8mVO3vJcR-frmGqbH9_WhnTPYRupdaqJqu9kFbOEzBPy7z3oJnoTb0fQ1HWvT5IUD8kkcwk_b3GVcrrnygbijAkB7mla4m8wd_cr_5EUjMbir8ucAl3F17HrsAB31FZ6fmFUelJpulKUpZPFYXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APkdTzguY5ae4dOQY7KUmHMP_hrHy1XWqX3JJfQReay5dRuEkfP1QLUA2scdWUY8iGlOGA_5ibCbXO9ShsH7yoB7tlQY4L2jGLrc-QfL29aOk-AIh7takQ2Be739Pe1w5dV-NA51JeNNE86eo0ImknZjPDeOtBs69mx3Ep0FrdFM0csjBNk-XLRUKIDvyAUsSahJnX5NWdu3HRSUDlPlzEEJuZzmQrfELUJ3HqGnKtbIScIsi_SHmpJHfrQQ5tIqmRpp_NLoz-wjYq_P3kvxpxUAFJWzu1413MFzR53mlDqstWqO8vOY_5axPrVat1uchu8JfEh16EaSXorMr7d_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFniyjbZJSAR3anl24aEQ1tiE4tZlw32IcUSjtvUg8k66B3eavOy3yHox6Ji5DOJhqs-0uOheehcbVyGfs1z_f8jraEasmMeypf5iPtQTmfTJRnS2I4XxIAEtxeYCqD208ib0lVAkOIW7k3j4_spLFajOga2entos-dKm4GNJhboTOZn0yqwAZGXOhuBIV4Qor4AhhilN2HHjNAgUwAAc4NIBTV8tPmou1mC0WWN8UZrVojYy_HcqKeYhoCg05w9Kzqtq537rkIM9gG7b0kTiYYNtVwM1dYEmeq4DVYRyHZVagRVrAoHeY_-6GEb775wGfHvCNd3HNcfKooTam4d5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NpXudR951ciP_VQwzNnm7WMj3bUkLn29o3rsrRo5p3vwaM85nLHnfGfl3StyngGzdp93F0yndtHs65LcKUzmmySIQW5qP-Ks0kFOpz52LfR0Vhb8qL1V77kV-4-tXgyGHAwLRY0P3Gwx1KaAO6TsXywaYY6V3uQ-E2lXIcCJvK8zpKWDQ5TrbGJh6WlpXxCjHIUJ1z6quDCaOF-ay-epPYLkJdg1BctcpJmZU0RFuY9YLv0UwQ3bblQ9QvhJi11XnTcBkX8UQ_pEg1QlUhUTLmH6hAL0HItB0mJTE6V1tH_Bq1aB5Td7lrZGZ3qWdum8Kt7SbBVNq0RENnwfszApEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=hN6r8OeQQbfyV20N9p5KyuN0MPEgfHTiXZ6X1z3U3a71wEQ4Xqap_TKMf_KJWoNdfnAUljiGHXVy5QVvYBKRyRvVIHas3Wu3-bhZKRlGpiV6XPWQNaLsi8TDyDRTA33ocJcy9wU2HTfgQsa8EG2zF68hIM3U_Ck16UP4x5dBlPoLDBbVRaCThY6-Cb5SwSTKfDUqGXQnCwa-lcXXkEmTfKIUtrbGj7NZBbYGXBzylzGEl4EYVqsCtIVjzKx7ril7nywIzzA3rMVGFjh0E4FmMHhuNxRIl-a8JY36F3HS1Ke5TZKY5LGmwZbIaYG0a5KIybHoCuN0JQJ9Tp6zJgWoRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=hN6r8OeQQbfyV20N9p5KyuN0MPEgfHTiXZ6X1z3U3a71wEQ4Xqap_TKMf_KJWoNdfnAUljiGHXVy5QVvYBKRyRvVIHas3Wu3-bhZKRlGpiV6XPWQNaLsi8TDyDRTA33ocJcy9wU2HTfgQsa8EG2zF68hIM3U_Ck16UP4x5dBlPoLDBbVRaCThY6-Cb5SwSTKfDUqGXQnCwa-lcXXkEmTfKIUtrbGj7NZBbYGXBzylzGEl4EYVqsCtIVjzKx7ril7nywIzzA3rMVGFjh0E4FmMHhuNxRIl-a8JY36F3HS1Ke5TZKY5LGmwZbIaYG0a5KIybHoCuN0JQJ9Tp6zJgWoRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
با Pake هر وب‌سایتی را به برنامه دسکتاپ سبک تبدیل کنید
یک پروژه متن‌باز برای ساخت اپ دسکتاپ از سرویس‌های وب مثل ChatGPT، YouTube، Spotify و Discord و ... است.
✨
قابلیت‌ها:
•
🔹
تبدیل هر وب‌سایت به اپ جداگانه
•
⚡️
اجرای سریع‌تر و مصرف رم کمتر
•
🛠
ساخته‌شده با Rust و Tauri
•
📦
خروجی کم‌حجم، معمولاً چند مگابایت
•
💻
پشتیبانی از Windows، macOS و Linux
🔗
لینک:
GitHub
#OpenSource
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
ترامپ: شرکت Anthropic دیگه تهدید امنیت ملی نیست!
🤖
✨
به گزارش Axios، دونالد ترامپ بعد از دیدار با «داریو آمودی» (مدیرعامل شرکت Anthropic) در حاشیه اجلاس G7 اعلام کرد که دیگه این غول هوش مصنوعی (سازنده مدل‌های Claude) رو یک تهدید امنیتی برای آمریکا نمی‌دونه!
🔥
جزئیات و حواشی این توافق:
1️⃣
ریشه اختلاف:
قبلاً سر آسیب‌پذیری و باگ‌های خطرناک «جیلبریک» (Jailbreak) تو مدل‌های
Claude Fable 5
و
Claude Mythos 5
اختلاف شدیدی بین دولت آمریکا و این شرکت پیش اومده بود.
2️⃣
اقدامات قبلی دولت:
وزارت بازرگانی آمریکا تو ۱۲ ژوئن محدودیت‌های شدیدی اعمال کرده بود تا دسترسی تکنسین‌های خارجی به این مدل‌ها محدود بشه.
3️⃣
همکاری و چارچوب جدید:
الان Anthropic با درخواست‌های اصلاحی دولت کاملاً راه اومده و کاخ سفید به همراه چند نهاد امنیتی در حال تدوین یک چارچوب فنی دقیق برای ارزیابی خطرات مدل‌های هوش مصنوعی هستن.
﻿
⚙️
سیاست کلی آمریکا در قبال AI:
ترامپ تاکید کرده که هدف اصلی، حفظ برتری بی‌چون‌وچرای آمریکا تو رقابت هوش مصنوعی با چینه و اصلاً قصد نداره با بستن یا تصاحب شرکت‌های داخلی، جلوی رشد این صنعت رو بگیره. البته این رو هم اضافه کرده که در شرایط اضطراری، از استفاده از قوانین سخت‌گیرانه نظارتی (مثل قانون تولید دفاعی) چشم‌پوشی نخواهد کرد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Anthropic
#Claude
#AI
#USA
#TechNews
#Security</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YS41gB10nTwWsMP7HtJ99QOHmWludfTFHIlO7AUZRDh-DMGgjYhihREqCZ8qQ8RDfy_aWyh47jvDLzgclC_QxY8cLsNCQMOxkB1tGJnExG1hV2l4B52egwu20JbCjrTQll22ypw5CkdxBy352ujnKdExfYd2utFo0CkCxb-tfftKJ_FbX_aaRGJPnvP3o54oZAXksorehwAgu7FkYe3l5k1z2q40uJeLlHjLV7-zjKmqSLiWNyWk8P2dKZT3-loJUS6ylaQWyXkjT-A6yZRriwEz8J7qXKdKjw98GmRGQ9OegPSFpaJMexh0lWh36nx-iucbekyMZITvPBfoORXjmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">KillerPDF
جایگزین متن‌باز و سبک برای Adobe Acrobat
📄
✨
ویژگی‌ها:
•
🪶
مخصوص ویندوز 10/11 با حجم حدود ۶ مگابایت
•
✏️
ویرایش متن داخل PDF
•
🔗
ترکیب چند فایل PDF
•
📑
استخراج صفحات انتخابی
•
🖊️
نقاشی و افزودن امضا
•
🔒
اجرای کاملاً محلی، رایگان و بدون تبلیغات
🔗
لینک:
GitHub
#OpenSource
#PDF
#Windows
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚀
مدل جدید Janus Pro از DeepSeek منتشر شد؛ پیشتازی در تولید تصویر!
🎨
✨
استارتاپ هوش مصنوعی چینی DeepSeek به‌تازگی گزارش فنی مدل متن‌باز جدیدش به نام
Janus-Pro-7B
رو منتشر کرده. بر اساس بنچمارک‌ها، این مدل در زمینه تبدیل متن به تصویر (Text-to-Image) تونسته عملکردی بهتر از رقبای قدرتمندی مثل DALL-E 3 (از OpenAI) و Stable Diffusion از خودش نشون بده!
این مدل در واقع نسخه ارتقایافته مدل Janus هست که اواخر سال گذشته معرفی شده بود.
🔥
ویژگی‌ها و بهبودهای کلیدی:
1️⃣
کیفیت و پایداری بالاتر:
با بهینه‌سازی فرآیند آموزش، ارتقای کیفیت داده‌ها و بزرگ‌تر شدن سایز مدل، جزئیات و پایداری تصاویر به‌شدت بهبود پیدا کرده.
2️⃣
تغذیه با داده‌های غنی:
در این نسخه از ۷۲ میلیون تصویر ساخته‌شده (Synthetic) باکیفیت در کنار داده‌های واقعی استفاده شده که خروجی‌ها بصری بسیار جذاب‌تری رو تولید می‌کنه.
3️⃣
مدل ۷ میلیارد پارامتری:
این مدل با ۷ میلیارد پارامتر، درک بسیار بهتری از دستورات (پرامپت‌ها) داره و سرعت و دقت تولید تصویر رو به سطح جدیدی رسونده.
📉
تاثیر دیپ‌سیک بر بازار تکنولوژی:
جالبه بدونید اپلیکیشن دستیار DeepSeek (مبتنی بر مدل قدرتمند V3) اخیراً رتبه اول اپلیکیشن‌های رایگان اپ‌استور آمریکا رو فتح کرده!
موفقیت‌های خیره‌کننده دیپ‌سیک و صدرنشینی مدل V3 تو جدول مدل‌های متن‌باز، حتی باعث شد تا سهام غول‌هایی مثل Nvidia و Oracle در روز دوشنبه با افت مواجه بشه. (شرکت‌های OpenAI و Stability AI هنوز به این خبر واکنشی نشون ندادن).
🔵
@ArchiveTell
| Bachelor
⚡️
#DeepSeek
#JanusPro
#AI
#DALL_E
#StableDiffusion
#TechNews</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMhovBE-z_qcuRjgYWH6TmII6Kc3fGuvlze6tOcqRscmGgZt4VubYGhx2BPhT2hB_yiDZngZpocLddpOQJeIJWcKKcTjL5aXmAJTQlEZiidaxab6JPjlBLsackJwI46bubIHLAPG8IdDoz5L9M6pbMhGxG-AyWq9shqGrjJ5HS9jTVpRqQOTwF0xjZez6KGK8Gk-kF_SWys7au_v_wvSju2TlWNfKHHijzWaCPY7SN2-1hvYofxm7cMG6ZFqByyKah86fmr5RxeMHiA9pefAu7mMFqOrlJd2vmD4n6XYX5YWVMuRhT073o5uN1gT9uy9Eb62a-kPvdFkv9qYSitPsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUXbTyhCE-mYpBas2AgWgJozIFkmkuB0HrXaQkultORsVADY8I2CxPPkcJXfsx9jlTxJ0FzHZCTY7t8A8N4jL0ElineIcwfrDM26FBgnOOkrAegg4AfcjcRtAXavC9aY-YQRY6c44t9DUZwtmZO15xMaR-bS27dodol_RQZRH7kMn2nR-7FbLhCYSTNijaf4cftrLAJHZPXt5glnlG3AgltxkHn7PXQdP54kzIUd7Sfv-HWOJP6vOnMMQF8O6PxeMqfAz5Ie5yYdbmZ31CndfJi5JhdaiIGkfUhMsPL5eEu_bINDB-Mu4FJnd_fk7iEE42b6kfUascrHQyw_7AHQHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYTmR-sE7V1OgVIM15oyuGxOIvRgbtvZTEKUhXWFqNX3wF2fuhWDi9EKs0hWslITgAl3XBID-NJZHlFUgEOxlI7osH-VZ0TaZ_bzFpUcCS7rLkyCS9wN-ong9NRi8_X2lCmP3Pxdv_XGU8QOgTYeH5Tft4cqTBQrrlfb2QNeqJ1I9JoXigeaU7a6AYz0Ol2KQT_wf4uNjHeNnF0sFHX0xtrqpQTskkEfB9W66wjkkiotAZlIU8gsN4zjeft-OOTQ2tcOJ1RiRW9L8zz9vEF3J6P5by-sH72ZISb3VT17tMEIvTxPQlZFW5eZZDvjXkOCGAjmi5eX7Bn2dOqerdrTbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی BleachBit؛ ابزار قدرتمند، رایگان و متن‌باز برای پاکسازی سیستم!
🧹
✨
اگه به دنبال یه ابزار امن و کاملاً رایگان برای بهینه‌سازی و پاکسازی سیستم‌عاملتون (چه ویندوز، چه لینوکس) هستید، BleachBit یکی از بهترین گزینه‌ها برای حفظ حریم خصوصی شماست!
این ابزار با حذف فایل‌های اضافی، کش مرورگرها، کوکی‌ها، فایل‌های موقت (Temp) و لاگ‌های سیستم، هم فضای هارد دیسک رو آزاد می‌کنه و هم ردپای دیجیتالیتون رو به حداقل می‌رسونه.
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
خرد کردن فایل‌ها (File Shredding):
حذف دائمی و غیرقابل بازیابی فایل‌های حساس.
2️⃣
پاکسازی فضای خالی (Wipe Free Space):
پاک کردن کامل فضای خالی دیسک برای جلوگیری از ریکاوری اطلاعات قدیمی.
3️⃣
بهینه‌سازی دیتابیس‌ها:
فشرده‌سازی دیتابیس برنامه‌ها برای افزایش سرعت و عملکرد سیستم.
4️⃣
امکانات حرفه‌ای:
پشتیبانی از خط فرمان (CLI) برای اتوماسیون، اجرای پرتابل (بدون نیاز به نصب) و امکان تعریف رول‌های (Rules) اختصاصی برای پاکسازی.
🔗
لینک وب‌سایت و دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
#BleachBit
#OpenSource
#Linux
#Windows
#Privacy
#Tools</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌐
ارتباطات آفلاین، امن و غیرمتمرکز با Nomad Network (نسخه ۱.۲.۰)
🔗
لینک گیت‌هاب
پلتفرم
Nomad Network
پلتفرمی برای ساخت شبکه‌های مش آفلاین با رمزنگاری قدرتمند، محرمانگی پیشرو و حریم خصوصی است.
✨
ویژگی‌ها:
>
🔹
کنترل ۱۰۰ درصدی:
بدون ثبت‌نام، قوانین یا وابستگی به سرورهای متمرکز.
>
🔹
تکنولوژی LXMF و Reticulum:
مسیریابی همتا‌به‌همتا (P2P) و زیرساخت مش رمزنگاری‌شده.
>
🔹
انعطاف‌پذیری بستر:
اجرا روی امواج رادیویی تا کابل‌های نوری.
مناسب برای دور زدن محدودیت‌ها و ساخت شبکه‌های محلی ایزوله.
🔵
@ArchiveTell
| Bachelor
⚡️
#LXMF
#P2P
#Reticulum
#NomadNetwork
#Mesh
#MeshNetwork</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=Due-o-WLTwBDkm2BLIcHnbaZE1y-nSkiDoUzF8P7L3mh5ZN3mtR_EyMDpaULbzUgeOQrxBrzggWD7vjbjH_XnBcQcOr7hGzFmylA_gvUuAj2TSbMCLZRfTcwW-CpHslPaDpVu1cxacLY0oGlobydD893B8_VKrIxogYa6IVxAl82_DkE235t-OGZXZpDmC6tVWfB1SaeUL7f5FMS7xzP8eSDPhul6u4lP7XANCpqNKYm9L-X6jLK60xphfakj8Lcais7sBUKjU3cWAzkMkiooxGq3-RnczWzRIMmkm8VKNSZdcdBRzMF2aOGVVIJDGl1Zs1gE1KrWuwJcbswq00VHi0kowXarLYPyTVbikMcMsjO0zRmHy2S5QwPLOn0uyx83-8aEkJd1IOvnEApLrQPtGOGJBCP4bkT2r5g11DSdSgTGXir7kkh1ADLTVfw_QWO_LqGjAKgJaxy407KKY6f-_o17U6bmw-5IVgROuPJstdXSKqVgR5BeffJWObS4f-A4RkNco4F0-CooRhNu2Bj-ksR1sABQnnZrxzdPCtBz0szridGmh3Rhl9yeQvFTvhMLMHa-_V7MhSUzoQL8A8fF1wQUC_bHOheIG9Jw7TvBU2vxYs-ps5jAYmuwtwsN6zCSC0IIWAU0XC68oCy3Hv1Bkczf4NLQD7pcjUBwtznn0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=Due-o-WLTwBDkm2BLIcHnbaZE1y-nSkiDoUzF8P7L3mh5ZN3mtR_EyMDpaULbzUgeOQrxBrzggWD7vjbjH_XnBcQcOr7hGzFmylA_gvUuAj2TSbMCLZRfTcwW-CpHslPaDpVu1cxacLY0oGlobydD893B8_VKrIxogYa6IVxAl82_DkE235t-OGZXZpDmC6tVWfB1SaeUL7f5FMS7xzP8eSDPhul6u4lP7XANCpqNKYm9L-X6jLK60xphfakj8Lcais7sBUKjU3cWAzkMkiooxGq3-RnczWzRIMmkm8VKNSZdcdBRzMF2aOGVVIJDGl1Zs1gE1KrWuwJcbswq00VHi0kowXarLYPyTVbikMcMsjO0zRmHy2S5QwPLOn0uyx83-8aEkJd1IOvnEApLrQPtGOGJBCP4bkT2r5g11DSdSgTGXir7kkh1ADLTVfw_QWO_LqGjAKgJaxy407KKY6f-_o17U6bmw-5IVgROuPJstdXSKqVgR5BeffJWObS4f-A4RkNco4F0-CooRhNu2Bj-ksR1sABQnnZrxzdPCtBz0szridGmh3Rhl9yeQvFTvhMLMHa-_V7MhSUzoQL8A8fF1wQUC_bHOheIG9Jw7TvBU2vxYs-ps5jAYmuwtwsN6zCSC0IIWAU0XC68oCy3Hv1Bkczf4NLQD7pcjUBwtznn0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Palmier Pro
ویرایشگر ویدیو نوآورانه و رایگان که با هوش مصنوعی کنترل می‌شود
📹
•
🔹
اتصال مستقیم Claude، Cursor و Codex از طریق MCP
•
🔹
برش، تنظیم ریتم، صداگذاری و افکت‌گذاری خودکار
•
🔹
درک رابط کاربری توسط AI بدون تنظیمات اضافه
•
🔹
ابزارهای جانبی برای تولید تصویر و ویدیو
🌐
Site
#AI
#VideoEditing
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcHi8Z-enm1Dc00JG04kqb-Th40lKVUskVlPNM6cG9vbmaVLNNZRFaPczoHqg9dHXuPy75ZB_pJuq1ghfEy7S0OFSecrGCjCTL9tP5r60WHHPnK5nsVIIZlkVa9rity7CeZaGKWjoCk734izebMMi3b0xdEx-MSSyEaijr0DJwDwbHTU8dXlqMYcCendEjdgdZHQ1K6IVdotwK2Xir4x-y32x_NqiAznTRCYpm6wltO-n1ASzHeDYqaZ14JzlYAHzijqyWjyX9GfQMS3Iy8XPMK-KB8c1se8gHRIP4cop3LHHaaIh7zknqmEc_4vyADkeUiDhSXqjrYOuuub-J2AFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdG7R0YYAsgO22xzEacdn6GgCzK-y5jN9EDGaK6oS0f_HKPMG8dVwTwv7iXxhsMWN0bFuFSmvZF0NZEvI25PG60PpBtl-Af2J0fumfEPHImKMfMH7b-l2MNkcv_r4mUsT6GSC-3Zg3f8BJtEL7rJmuj4oYwpo9UJQdGpigG2E_G3ijAkUVd19asezrs5vSU2tIVy2RHqPQzrQuV_g0B2nlxCFJz8p5ZuxvffF5zLQVjnNk2H_LSbXN5O9TRzY53TjJRENNvoD4HEuvuvW4RcQcMSNk_8qh38XyuDBrREaM5AKfPL1ikzsxE-xsll5tWrdAJ5x161nWJ3XR1hx_1oGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚀
آموزش استفاده از مدل‌های قدرتمند GLM در ابزار Claude Code!
💻
✨
اگر از Claude Code (ابزار برنامه‌نویسی محبوب مبتنی بر ترمینال) استفاده می‌کنید، الان می‌تونید با اتصال به پلتفرم Z.AI، مدل‌های بی‌نظیر سری GLM (به‌ویژه نسخه جدید
GLM-5.2
با کانتکست خارق‌العاده ۱ میلیون توکنی) رو جایگزین مدل‌های پیش‌فرض کنید!
🛠
مراحل راه‌اندازی سریع:
1️⃣
نصب Claude Code:
(نیاز به نصب Node.js 18+)
تو ترمینال وارد کنید:
npm install -g @anthropic-ai/claude-code
2️⃣
تنظیم API و متغیرها:
تو سایت
Z.AI
ثبت‌نام کنید و کلید API بگیرید. برای سیستم‌عامل‌های مک و لینوکس فقط کافیه اسکریپت زیر رو اجرا کنید تا همه‌چیز خودکار تنظیم بشه:
curl -O "https://cdn.bigmodel.cn/install/claude_code_zai_env.sh" && bash ./claude_code_zai_env.sh
(برای ویندوز باید متغیرهای
ANTHROPIC_AUTH_TOKEN
و
ANTHROPIC_BASE_URL
رو دستی توی سیستم ست کنید).
🔥
ارتقا به مدل ۱ میلیون توکنی (GLM-5.2):
به‌طور پیش‌فرض کلود کد روی مدل
GLM-4.7
تنظیم می‌شه. اما برای استفاده از نسخه
GLM-5.2[1m]
، فایل
~/.claude/settings.json
رو باز کنید و این مقادیر رو به بخش
env
اضافه کنید:
"CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1000000"
"ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.2[1m]"
"ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.2[1m]"
⚙️
نکته حرفه‌ای در مورد قدرت استدلال (Effort):
با دستور
/effort
داخل محیط کلود کد می‌تونید قدرت تفکر رو تعیین کنید. اگه این گزینه رو روی
max
یا
ultracode
بذارید، مستقیماً به استدلال سطح Max در مدل GLM-5.2 متصل می‌شه که برای حل باگ‌ها و تسک‌های پیچیده عالیه.
💰
هزینه‌ها چطوره؟
استفاده از مدل GLM-5.2 تو ساعات اوج ترافیک (۱۴:۰۰ تا ۱۸:۰۰ به وقت پکن / ۰۹:۳۰ تا ۱۳:۳۰ به وقت ایران) ضریب ۳ برابر داره، اما تو ساعات غیرپیک (به‌عنوان آفر ویژه تا آخر سپتامبر) فقط با ضریب ۱ محاسبه می‌شه!
🔵
@ArchiveTell
| Bachelor
⚡️
#Ai
#Claude
#GLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIw4aHfx_SEnq_Bfh0iTFjRxxUxXERl90Wae6c6KrTZlh63YcWDHXdoo4POJb-1GKMVF7sypzuduKYVnaYDSHLDBch_3d9hG-0RQjX6v94SePQgpGBJ-4ralEK--spnd7A2dFgfbo-50MmdsxHaSCpfjoWGnkZ7AChyhvaF6oxDcU22lEuQ1crnYa3DgYfCiEtVRYbyLux_QQCbWcfO2zmID2aPLKikgCiEEtw9EfhfIexx0VZcJEeXWq0HVR60KXzM6jU4fLFd-mqGe-538LiKXPC1KNTCguByGlTtZB-awlEEa0DDDkcuPCiwnX1ZlRb7z97nYv2lMc2Ob0ApraA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎯
پروژه Universal Android Debloater
📝
این ابزار یه رابط کاربری گرافیکی (GUI) کراس‌پلتفرمِ نوشته‌شده با زبان
Rust
هست که با استفاده از ADB به شما اجازه می‌ده گوشی‌های اندرویدی
روت‌نشده
رو دی‌بلوت کنید (برنامه‌های اضافی و پیش‌فرض سیستم رو حذف کنید). نتیجه این کار؟ بهبود چشمگیر حریم خصوصی، امنیت و افزایش عمر باتری دستگاه شما!
──────────────────────────────
این پروژه متن‌باز (Open-Source) در واقع فورکی از نسخه اصلی Universal Android Debloater است که با تمرکز ویژه روی افزایش امنیت، سرعت و بهینه‌سازی مصرف حافظه توسعه داده شده و با حذف اپلیکیشن‌های غیرضروری، سطح حمله (Attack Surface) رو به حداقل می‌رسونه.
✨
ویژگی‌های کلیدی:
🔹
رابط کاربری ساده، روان و کاربرپسند
🔹
دارای یک لیست جامع و کامل از پکیج‌های سیستمی
🔹
قابلیت دی‌بلوت کردن دستگاه (حتی بدون نیاز به کامپیوتر)
🔹
دارای ویکی (Wiki) و مستندات کامل شامل آموزش راه‌اندازی، راهنمای استفاده و نحوه بیلد گرفتن از سورس‌کد
🛠
از نگاه فنی:
این برنامه با استفاده از زبان Rust و کتابخانه گرافیکی Iced ساخته شده تا تجربه‌ای بدون لگ و یکپارچه رو ارائه بده. از نظر حریم خصوصی هم خیالتون راحت باشه؛ هیچ دیتا یا اطلاعات کاربری جمع‌آوری یا ارسال نمی‌شه و تنها ارتباط خارجی برنامه، درخواست‌های (GET) به گیت‌هاب برای دریافت لیست پکیج‌ها و بررسی آپدیت‌هاست.
چه کاربر مبتدی باشید چه یک متخصص فنی، اگه می‌خواید گوشی‌تون رو بهینه‌سازی کنید، این ابزار یکی از بهترین گزینه‌هاست.
💡
حرف آخر:
با این ابزار، کنترل کامل عملکرد و امنیت گوشی اندرویدی‌تون رو دوباره به دست بگیرید!
──────────────────────────────
🔵
@ArchiveTell
| Bachelor
⚡️
#Github</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oshn-N0rnF4SYVR63YcopWbzQzHB5e5UqlNdlDuE30TPNteazubTYLNhvz7lC9jNV0rZjtsQe_FFfxiK6cqpDhSLdYGVlvEpA3e3FRXXe_bf00U3UPHCwyoRejO58nfuHCINEsjnDyp-xxvkk_vSyQfAMd-1X1PSixhbZcN5zToaAa9UeLRkb92UecE0eNhmXN0khNAnNuLMTc1Mx1hnOIP3It8_txnOVeIARrYfQAIePpc2GWUma9GmA0PF1OrPhZy4awezvLx-ggVPXHcCAFryKIPgQLQU_KTNC5r5fFM-p9vdNukpK3aUkE0rnMkPI1pMJuZ6k63JCtgpyfzKpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دانلود کامل ویدیوهای یوتیوب + ویرایش فوری بدون افت کیفیت
🎬
یک توسعه‌دهنده دانلودر شخصی خودش را متن‌باز منتشر کرده؛ ابزاری ساده برای دانلود و ادیت سریع ویدیوها.
✨
قابلیت‌ها:
•
🔹
دانلود ویدیو با کیفیت اصلی
•
✂️
برش، چسباندن و تقسیم ویدیو داخل برنامه
•
💻
اجرای کاملاً محلی روی سیستم
•
🆓
رایگان و متن‌باز
•
🧩
رابط کاربری ساده و کاربرپسند
GitHub
#OpenSource
#YouTube
#Downloader
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚀
آموزش اجرای GPT 5.5 xhigh در Codex روی ترمینال (کاملاً رایگان)
1️⃣
ثبت‌نام در Freemodel
وارد سایت
Freemodel
شوید
با حساب Gmail ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
گزینه 1: احراز هویت با شماره تلفن
🔹
گزینه 2: احراز هویت با تلگرام
✅
گزینه
Telegram Verification
را انتخاب کنید
🔗
وارد ربات تلگرام شوید و Start را بزنید
🎉
در این مرحله پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار
💰
هر هفته: ۶۶ دلار اعتبار
💰
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Keys
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال
(
به
ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro git curl wget nano tar -y
3⃣
دسترسی به حافظه
termux-setup-storage
4⃣
نصب Ubuntu
proot-distro install ubuntu
5⃣
ورود به Ubuntu
proot-distro login ubuntu
6⃣
آپدیت Ubuntu
apt update && apt upgrade -y
7⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
8⃣
نصب Node.js
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
9⃣
نصب Codex
npm install -g @openai/codex
🔟
تنظیمات Codex
mkdir -p ~/.codex
cat > ~/.codex/config.toml <<'EOF' model = "gpt-5.5" model_provider = "freemodel" preferred_auth_method = "apikey" model_reasoning_effort = "high" disable_response_storage = true
[model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses" env_key = "OPENAI_API_KEY" EOF
🔘
تنظیم API Key
echo 'export OPENAI_API_KEY="کلیدتو اینجا بزار"' >> ~/.bashrc source ~/.bashrc
▶️
اجرای Codex
( با فیلترشکن خوب وارد شوید )
codex
✨
حالا Codex روی ترمینال شما آماده استفاده است
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkua-v7ID3MXlLmJFaWse8xDws2b__l2yVkkh8vBBycOMtO0DwE6-goX1Jbpxd8z0yVKFpFoZ8RY4nq5rrWMJQgjsRI-ZtBDVpMcMRyS-TP4mmwnGwftH5paJHmlCFcwMj4eu6qe-KDN52wCqoARgfYRhsnoLhvrS_gy37V5cQDClOQ0X74iGuWYOzE2fFiFA7LBKmHem4dI526TrT4pYAev-vZtwkaPnZbOnh-Q-cl52-DBT5M-4yCKnDNUftjfE6HvdZc3CM-dKlRckEuMjLCAdOuEUwyXf3cZAg7PUFeQDruzSayyVEbPhaxe4rZOfM8m4VyUriCmDsETgzKYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">💻
ایده داری ولی حوصله نصب ابزار و دردسرهای راه‌اندازی رو نداری؟
🚀
Replit
یه محیط برنامه‌نویسی آنلاین با AI داخلیه که می‌تونی مستقیم از مرورگر پروژه‌هات رو بسازی.
✨
امکانات:
• کدنویسی با کمک AI
🤖
• ساخت سایت، ربات و اپلیکیشن
🌐
• اجرا و هاست پروژه‌ها در همان محیط
⚡
• بدون نیاز به سیستم قوی یا تنظیمات پیچیده
🔧
برای شروع سریع پروژه‌های شخصی، استارتاپی یا AI گزینه جالبیه
👀
🔗
سایت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhuYCaW8VUGxVdZmcOsCaCD28g0LHIagd_sz6GGeP4aeVt0sdW9JLfvQ7hyzY4fiuE_IOC7-45WgGYJ6JLT8NS4dce-oKHPgC7yEbOCDwdUpGmOmAboym4SbjfrpU2CLoXdud47Xu39fzYwEotWRiIv3xJc-Ur4NsGTLq7mrVxILJ96hCSBtK5nTnrP4ROd5JGst9zKsgYQIbO5LSKfIlZMOSTvcbJ_dSisXj6YUeo7WXz_dIMWqqPEd4IAH-yUWGHtuwd_WFJ9sa0NPwaxeWywO2XvgFlu1Z_5hdIMVw38oF7aPSAydJXoWtfZp5XnhXms529hRRFHgrkGTi3B1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دسترسی رایگان به Claude OPUS 4.8 و GPT 5.5 + دریافت ۷,۲۰۰ اعتبار!
💯
🤩
پلتفرم
Gumloop.com
یک رابط کاربری چت حرفه‌ای با قابلیت اتصال به سرویس‌های مختلفه. جالب اینجاست که این شرکت به‌تازگی ۵۰ میلیون دلار هم سرمایه جذب کرده!
مراحل دقیق دریافت اعتبار:
🔹
از طریق حساب گوگل یا مایکروسافت (OAuth) ثبت‌نام کنید.
🔹
در مراحل ثبت‌نام اولیه، به سوالات پاسخ بدید و هر گزینه‌ای که می‌تونید رو انتخاب کنید.
🔹
وقتی به بخش اتصال سرویس‌ها رسیدید، Apify، Semrush و Reducto رو انتخاب کنید (هیچ‌کدوم نیازی به لاگین ندارن).
🔹
اتصال به Slack رو اسکیپ (Skip) کنید و نادیده بگیرید.
🔹
اگه مراحل رو درست برید، حداقل
۷,۲۰۰ اعتبار
به حسابتون اضافه می‌شه!(که مال من نشد
😂
)
🤖
مدل‌های هوش مصنوعی موجود در پلتفرم:
Opus 4.6 تا 4.8، GPT 5.3 Codex، GPT 5.4، GPT 5.5، Gemini 3 Flash، Gemini 3.1 Pro، Gemini 3.5 Flash، DeepSeek V4 Flash & Pro و Kimi K2.6.
❌
در هیچ‌کدوم از این مراحل نیازی به وارد کردن کارت بانکی (Credit Card) نیست.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 Ultra در Claude Code رو ترمینال ( کاملا رایگان )
1️⃣
ثبت‌نام در Freemodel
وارد سایت
Freemodel
شوید
با حساب Gmail ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
گزینه 1: احراز هویت با شماره تلفن
🔹
گزینه 2: احراز هویت با تلگرام
✅
گزینه
Telegram Verification
را انتخاب کنید
🔗
وارد ربات تلگرام شوید و Start را بزنید
🎉
در این مرحله پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار
💰
هر هفته: ۶۶ دلار اعتبار
💰
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Keys
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال ( به ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro nano -y
3⃣
نصب Ubuntu
proot-distro install ubuntu
4⃣
ورود به Ubuntu
proot-distro login ubuntu
5⃣
آپدیت Ubuntu
apt update && apt upgrade -y
6⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
apt install -y curl nano nodejs npm
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
7⃣
نصب Claude Code فیلترشکن بزن
npm install -g @anthropic-ai/claude-code@2.1.167
8⃣
تنظیمات Claude Code
mkdir -p ~/.claude
دستور زیر را برای باز کردن فایل تنظیمات بزنید:
nano ~/.claude/settings.json
کد زیر را داخل فایل پیست کنید (کلید خود را جایگزین کنید) و با زدن Ctrl + X و سپس y و در نهایت Enter ذخیره کنید:
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://cc.freemodel.dev",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
▶️
اجرای Claude Code ( با فیلترشکن خوب وارد شوید )
claude
✨
حالا Claude Code روی ترمینال شما آماده استفاده است
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCnLKh4cFvkTE_j9GW8Ju-uQKMo4ibwXnLpx3KnCTbfD8i74sfOTa4DPqC9CJcHNpirz9kW6yawoPZ58f_xrrDLXLwpYK8ihnQsVYURwh2nsDyAWiEcH3J6l9JI0vojcA8eRReO-aqIa251Z-bnxeHnIRWxGDorES3WKv1kKvRsGyz0pv8JUyZr3A-qk_CMSSj-j3D6PNvi7SZu3VU80L_KBHGxcjmfCxJTy4a_v3FB99Wb5Pt0_cPw5B3fBbfL4sUqfeefU-IzFAkpIsOg2QzSlGFcfPpPSBvmzsL1NQRuaSD0ndIc1n8jMybMPNU9yEIhDa3suSgyxFAMXGbnJkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ دلار اعتبار رایگان OPUS 4.8 و GPT 5.5
🔥
🌐
ثبت نام
#API
#Claude
#GPT
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=oCIJf5m97gmlAW8gceb9yiyQJowV4J93_Ro-NkLl-ZX0EfVcV3FyJQFmzfC_n-7lS3KFk5KjR9SaI2uAYfP2sRDfylXGcAY5NkCESjubYKWOao7K0JOYeBL-2-_hZEHQnaDchC64jeKYkWWbUaTAEtc3zDOAKMKaFQIOED8LNhG6EIeXLzVzn6Kc0TRn_LteKrkmCCtNa4yc6720CXLG2c_OtOLIpl1M3q2nCK45EJphI2VkbxLY7_HxxVlVWWpfYrIr2XuSrOKPiKzdl1PzxyDduDKqoMaFkicJEuIka8IYNo8pWzgw08rC0YlUWrWQLharHonwhPxyVJvdxDFt8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=oCIJf5m97gmlAW8gceb9yiyQJowV4J93_Ro-NkLl-ZX0EfVcV3FyJQFmzfC_n-7lS3KFk5KjR9SaI2uAYfP2sRDfylXGcAY5NkCESjubYKWOao7K0JOYeBL-2-_hZEHQnaDchC64jeKYkWWbUaTAEtc3zDOAKMKaFQIOED8LNhG6EIeXLzVzn6Kc0TRn_LteKrkmCCtNa4yc6720CXLG2c_OtOLIpl1M3q2nCK45EJphI2VkbxLY7_HxxVlVWWpfYrIr2XuSrOKPiKzdl1PzxyDduDKqoMaFkicJEuIka8IYNo8pWzgw08rC0YlUWrWQLharHonwhPxyVJvdxDFt8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
Open Design
یه نسخه اوپن‌سورس از Claude Designه که واقعاً به درد می‌خوره
😮‍💨
باهاش می‌تونی از روی یه پرامپت، سایت، دک، تصویر یا حتی موشن بسازی و بعد همون‌جا توی محیط امن ویرایشش کنی.
✨
چیزای مهمش:
• 150 تا design system آماده
• 260+ پلاگین
• پشتیبانی از Claude، Codex، Gemini، Copilot و بقیه
• خروجی HTML / PDF / PPTX / MP4
• همه‌چی لوکال و بدون قفل شدن به یه سرویس خاص
خلاصه اینکه: یه ابزار جدی برای طراحی با AI، نه فقط یه چت‌بات دیگه
👀
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✨
ویندوزتو سریع‌تر کن با Sparkle
🧹
یه ابزار رایگان و اوپن‌سورس برای بهینه‌سازی ویندوز
• پاک‌سازی و سبک کردن ویندوز (debloat)
• بهینه‌سازی سیستم با یه کلیک
• مدیریت DNS
• نصب برنامه‌ها با Winget / Chocolatey
• حذف فایل‌های اضافی و junk
• بکاپ و ریستور تنظیمات سیستم
🚀
همه‌چی تو یه داشبورد ساده و مدرن
🔗
GitHub
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🧠
AI OS
سیستم عامل هوش مصنوعی لینوکس
👇
یه سیستم‌عامل ساختن که بهش میگی چی کار کنه، خودش واقعاً انجام میده
🤖
🔒
HAL (امنیت):
• کار ساده → خودکار
• کار حساس → تایید می‌خواد
• سیستم → بدون اجازه دست نمی‌زنه
📁
دیتاها لوکال می‌مونه + حتی آفلاین هم کار می‌کنه
خلاصه
👇
دیگه چت‌بات نیست… یه OS هست که کار می‌کنه
🔥
🔗
Github
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚡️
Gemini
داره می‌ره سمت ساخت ویدیو با چهره خودت!
یعنی یه عکس از خودت می‌دی و بعدش می‌تونه ویدیوهایی بسازه که انگار خودت داخلش هستی.
فعلاً این قابلیت دست یه سری تسترهاست، ولی اگه عمومی بشه، تولید ویدیو با AI یه سطح جدید می‌ره
🚀
#AI
#Gemini
#Tech
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qb7qtJuQ0KSorzrKwEeSAARtZdiq32EdmextOFUZBfxiIF_bQI1i8gz7Ec9VYgoh19sDou8dJdBp3niGhs_6cQ0X3hyOoc8ajb8YlpI4e6bkE3nREvQHXiJ4STo3SXg5aGM4wEX_j9ATEU0qr6YbqnhhRYnwFGOlp0dtZf-rlTPjSzOIzG9xX40zvCGYFBj8gZJ5Zxx2fC0AcEBxrvtCIaluh_2PfBvsFmF4gmYkdw8Gof7a7ciV7cSDrEr5um-a4TcWcg525rwHzGiA7kWdG3xRe-DfenAriaTYWsnax0DfADtqFCUMkqgBqg3BaF7ko1I4sU5cgVvvhsjpVEWcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍎
اجرای macOS روی کامپیوتر معمولی بدون راهنماهای پیچیده و تنظیمات دستی — علاقه‌مندان اسکریپتی ساخته‌اند که نصب سیستم را خودکار می‌کند.
🔹
نسخه‌های macOS از High Sierra تا Sequoia را پشتیبانی می‌کند.
🔹
روی پردازنده‌های Intel و AMD کار می‌کند.
🔹
به‌صورت خودکار ماشین مجازی را ایجاد و تنظیم می‌کند.
🔹
کمک می‌کند محیطی برای Xcode، Logic Pro، Final Cut Pro و نرم‌افزارهای دیگر اپل به سرعت راه‌اندازی شود.
🔹
به‌طور منظم به‌روزرسانی و پشتیبانی می‌شود.
▶️
دستور نصب:
/bin/bash -c "$(curl -fsSL https://install.osx-proxmox.com)"
GitHub
#OpenSource
#macOS
#Proxmox
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌐
DigitalPlat FreeDomain
راهی برای گرفتن دامنه رایگان
این
پروژه به شما اجازه می‌دهد بدون هزینه، برای سایت یا پروژه‌تان دامنه بگیرید و سریع راه‌اندازی کنید.
✨
🔹
دامنه‌های رایگان فعلی:
• .DPDNS.ORG
• .US.KG
• .QZZ.IO
• .XX.KG
• .QD.JE
📊
طبق اعلام پروژه، تا الان بیش از ۵۰۰ هزار دامنه ثبت شده و مدیریت همه‌چیز از طریق داشبورد آنلاین انجام می‌شود.
🔗
ثبت دامنه و راهنما
#Domain
#FreeDomain
#Web
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">ایپی 188.114.97.6، تنها ip واقعا تمیز کلودفلرِ ایرانسل دوباره باز شده، بقیه ip ها رو alpn-1.1 (وبسوکت) محدودیت شدید آپلود دارند، در نتیجه پنل های bpb و ... رو اونها قابل استفاده نیست و فقط XHTTP رو سایر ip ها قابل استفاده است.
///
ولی علاوه بر
188.114.97.6
که مستقیم بدون نیاز به چیزی وصل میشه، رو بعضی ip ها مثل
104.17.121.43
نیز فرگمنت باعث میشه که محدودیت آپلود برداشته بشه و اون ip قابل استفاده باشه، تنظیمات زیادی برای فرگمنت کار میکنه به طور مثال در حال حاضر میتونید از:
"ip": "104.17.121.43",
///
"packets": "tlshello",
"length": "1",
"interval": "0"
استفاده کنید.
///
تمام مطالب بالا راجع به ایرانسل (و بعضی نت های دیگر در برخی مناطق) میباشد، و رو بیشتر نت های دیگر محدودیتی وجود ندارد و اکثر ip های کلودفلر به طور مستقیم قابل استفاده اند.</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmjCMyhJj3xaQyTzI0EAhPXpdZtwrrVYttDltAFgkdt06cr9Uq2v-NtC_Nu_H-uf6VChiA3dgO3Fuf-hJvNVOs519fLBVHadCuuieQ9wU9OYVfOHx4UqARrc5V-tp1V8yfb3c97-IB_nlRSeVG1AGAlrizMuGqGT-7SbrK28QbdV5cEPr96QksGWUxd3k28Jc86SqcP5Tm64Wk7yGl5ANDpYt_3LgkTLWbQDdBGC8X5bKoylbJzn6fxbgAwaAbG-Gx1eElJOAniQ_-LZHFK9bnrLAv-o18AM7dyQbIRWqje99KVV4Q6h2ns8fy8oPejXhIIB8pwF7ftqBlqfG2iRVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡️
برنامه Sandboxie؛ اجرای امن برنامه‌ها در محیط ایزوله ویندوز
اگر می‌خواهید نرم‌افزارهای ناشناس، فایل‌های مشکوک یا مرورگر خود را بدون دسترسی مستقیم به سیستم اصلی اجرا کنید، Sandboxie یکی از قدیمی‌ترین و قدرتمندترین ابزارهای Sandbox برای ویندوز است.
✨
امکانات مهم:
🔹
اجرای برنامه‌ها در محیط کاملاً ایزوله
🔹
جلوگیری از تغییر دائمی فایل‌ها و رجیستری ویندوز
🔹
ساخت تعداد نامحدود Sandbox
🔹
فایروال اختصاصی برای هر Sandbox
🔹
محدودسازی دسترسی به اینترنت، کلیپ‌بورد و فایل‌های سیستم
🔹
محافظت در برابر اسکرین‌شات و نشت اطلاعات
🔹
پشتیبانی از مرور امن وب و تست فایل‌های ناشناس
🔹
متن‌باز و رایگان
برنامه Sandboxie از سال ۲۰۰۴ توسعه داده می‌شود و امروزه به‌عنوان یکی از محبوب‌ترین ابزارهای امنیتی ویندوز برای تحلیل فایل‌ها، تست نرم‌افزارها و افزایش حریم خصوصی شناخته می‌شود.
🔗
Github
#Windows
#CyberSecurity
#Sandboxie
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR-Om-Am9_ySsvOOJ5j3u_oydn8p_eBxfu_3tjnNIEBub6w4n6JdRY_T6Evc0UyJ36lsvj8hvr_ZwWEqYkXPYGwCNNN_vCQzVVeirK_4kt76jbXkp37LhzlEjuwdaVoY_6byotRlh0Syu54Ns4m1z_sXj5gnRqQXCsNMC7qrnF-XPTfu8vQ_cfwmGbOCgIUAGUsjARIJqiC6y4U-aPxQJbnrTXC5Z-no-byU4xPL5SCvOmAMsGtsoiND_1rH9s3XPVj1RDYcSe1h6EWxRy2KwR3ie8bCoo0TO-Rb-9ECb47tb8n1X-nCoX-VKWuYOvLLO3Ut97boBrk1gulWpmacDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏬
دانلود ویدیو، موسیقی و پلی‌لیست‌ها بدون تبلیغات، اشتراک‌ها و مبدل‌های آنلاین مشکوک
یک رابط کاربری مناسب برای ابزار افسانه‌ای yt-dlp پیدا کردیم
🔥
قابلیت‌ها:
🔹
دانلود ویدیو از بیش از ۱۰۰۰ پلتفرم محبوب.
🔹
پشتیبانی از کیفیت تا 8K و صدای بدون افت کیفیت.
🔹
قابلیت دانلود کل پلی‌لیست‌ها، کانال‌ها و زیرنویس‌ها.
🔹
امکان قرار دادن ده‌ها فایل در صف دانلود.
🔹
به‌صورت خودکار مرتب‌سازی و تغییر نام دانلودها بر اساس قالب‌ها.
🔹
اجرای محلی روی کامپیوتر شما.
🔹
پشتیبانی از ویندوز، لینوکس و مک‌اواس.
GitHub
#OpenSource
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRMFuqdW-fmnFtlJ63gKQv_mZoNbWD7tnzaECh34e9aPTwU4JIZaS1MH225y75CLzk-oYTCsU2WCnKfcdmYbyJL4dZx9chZl8C3SRMNJzR6L9E3T47ipOtF2PbZ-jtJfcJ3Ezs5n-IoU1o3udm3wLVayk8NvebUHU49MLuMe2hZm8pffZ-9xyYtglRCKPVT0HJFKqNHu441Gj3btT6R5fiQvwaGRLJ_at_DW6-9Qq5gMx7WskZfTx65b3OCKrCduUIlzUtTDrSp1_2UMGAL_TP3G7Va1ldQTwDgLIlLx-r9ts4Uef2uke94UcT8-avVih_0zcbbh7sBTOOQE51kEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQz80DaKGJPGBc49Jdw6kOelYVjVxDLoxNvi_lhYgftp_tglXagLIiIIoZFOhyJAyXUmwRCk1Uh4Rz4kh4QAnVg6S6g4hy_gLcMvLVLsCvvrXqmxx7UXlHT2HMt1s4ILRPKN35m1Q9vlM8Gedjm0pnwycG8GfpeELXommASBA5cgWaI8KLI8_sLnZjPsoE1DyqBio7RvgEIrz5za_SBuu-bw4t51kxHMiELI-kAla2aryjUqjFsSbLtrC8fR_ybpMUKjFgjVdVxwLifFON5jWk7_T6IhQOQfbYB97wl5i_othTNIEUdtIF3QgeJ965Yg0hpevVwgJ1gJqaxtX2WC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مدل Cursor در حال توسعه یک مدل جدید با 1.5 تریلیون پارامتر است!
⚡️
نکات مهم:
🔹
از صفر آموزش داده شده و نسخه ارتقایافته مدل‌های قبلی نیست.
🔹
گفته می‌شود برای آموزش آن از حدود 100 هزار کارت گرافیک H100 استفاده شده.
🔹
علاوه بر کدنویسی، از Agentهای هوش مصنوعی برای مستندسازی و مدیریت تسک‌ها پشتیبانی می‌کند.
📅
طبق گزارش‌ها، این مدل طی چند هفته آینده معرفی خواهد شد.
#Cursor
#AI
#Coding
#LLM
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feI0MsSVav8vrBS6be76NIPms74d_LpP_qC02LjDHaKjrQrD_rB0ZIwJTL_jD3yJsfXGvWbMlvSMTNZwyUevADVcJ1oJVjlrrODehRzziYL-wc7_Cw1Osl74Ucp8mZayWw0zvJHnCPp-tWMkaVgQsOH1nsu_zAD2EDj5oyYkw3-ESCHbWoRyqfkf4F1XziT8heQ_4WHo1ATHjmFjzBVPXDTCh0Z1EPWAZg2wve1svwgIcHK4ySTXL3FjL6gZwknyLq2Yq8ckrdxw6bZX-nF5qX5ZsBpXZq_v5iH83iBHIW49up-F8Bfhn0RM3vvSZlKzvuNvsF_wmLWrX7JkhYUjwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPs-WafGiJ-IvPMrJfeRhe-IjxVArXqSQwBpwIoH86RgXk3UKySCoCzAQZxPxMjMcnnQUT8gcUWSY34nAMwz8hBZ08PKXJi4snjZLaGUKJBYqPEishm_3tQk33242ZH-HqXttXk0Ou1D_ca6MrEgeSydi9azH7wRxw4Fhb3Lvgc-taT7NU_DPlo7ACzOMc6sTQEsrKHAGFqdTqOREWTUxtAZkGHY31jSHhujDrLv4LKdarQQ3MzmfLiYnirLiSWYYwUfYerYK6gSUDYGMBMusPIAjopN1OTwCckGH7BJBklqtAbCyFuQBWJm22h73HKjXupGAHfcHUU5u-pKW7f86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MDvFIRSFqmCFyYq8CyFQwwgahH2noSpFg-JsRL3Y_ZTQHEtJ588hHJp323kFaEPPkq3DefdkPa71pzCDN2ULK6hlLguTjDzaZV4EBcUtGaIuV8R-WP7IT6nu0VBY0VLNdV9IDy6Fho9J_A4dg8BiRQNgQ-ZKzNgTVAx9-dqbW22q7EtcX8GNUdtZvPZLKBI7fswEsujgSkIgsSutklvTGG0NrU79yRuQQ5xwfYFwML7NUelQ-O184Vnyrp26eI-yYpeWKjovq7_ZyOxHC2F28OSP8dmkT4ina2LmEDWQy2gpYg6tsM5O_LYedlZTh_jEFnK9HMMezwa4jgaIdzycyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGIvU4WtBEcbm3fvErTiXG48XscDR_fJ7yW0_TDFCh_MmZDxXTRQFWn-SZDaqPu8EfPY2zjFGpb4PVL09nbtuNPU67gPCDw2WnwSIFcxBTKPG7Abj4a0eIXF703_mdtBvpulUBPczGEfAvHJkxeCidAnd7SG42_w88FGcfB9xHH7ct9ujBhTUP1XLgJIrQZHSwQH1-iG1wBN-4I4Lky2B7-xVBtu_Ryu929QuNYyfjjLKoM2GE7pk64-7pzSnjr_bJK01uQ5ASwJk19ykSDYXJQbcBD6C9JGzyccmA4jsCJgcyQh685ONRAVhi7q7-R0WkXxnDDNTFEz48LtBUT-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHXBe3D_ZayI-vuiKFkD_CxrkINDcP6ydLTjVq3MvCwePX3n6QKOmC6FOIY637kG5KmvnBvKWRaCWo9wyNdkZnuhQ9u-7ltfU44hpUiG_J7TP6kxFiw4-U30z5-wBKZ4qsm2YAimzNcjOqTwhGvSYwVmTz_6_R91K1mRXIb5U8RTBviUMVcD4VKVEctOvv4RH5PWOLQYqwy7r9E4eICBQ-3A2Cuon7Sb9ImalUUiMrMkxOsZsuyiR0LBEZdJ6GwLpqrMhQGteTJ1fGzEBEFWorxiEBaUbn4M--AlXMMISNsUY97izGFiPolJZgd8e9hMSvCwDyCQL2kplmNjaQK6eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رقیب رایگان Suno پیدا شد
🔥
StableDAW
یک استودیوی هوش مصنوعی برای ساخت موسیقی روی کامپیوتر شماست
✨
قابلیت‌ها:
•
🔹
تولید موسیقی بدون نیاز به اشتراک
•
⚡
ساخت ترک با پرامپت متنی یا ملودی خوانده‌شده
•
🛠️
ویرایش دستی ترک‌ها با رابطی شبیه FL Studio
•
🎹
پشتیبانی از MIDI، سازها و استخراج نت‌ها
•
💻
اجرای محلی روی کامپیوتر با سرعت بالا
🔗
لینک
#AI
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">sadra.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">همین الان ساختم
نامحدوده
تست بکنید به احتمال زیاد وصل باشه برای بعضی مناطق
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🌐
ابزار متن‌باز
CF-IP-Scanner
برای پیدا کردن سریع‌ترین IPهای Cloudflare منتشر شد.
این پروژه با اسکن رنج‌های Cloudflare، بهترین IPها را بر اساس پینگ و پایداری اتصال پیدا می‌کند تا در ابزارهایی مثل
Xray، V2Ray، VLESS و Trojan
استفاده شوند.
⚡️
قابلیت‌ها:
🔹
اسکن خودکار IPهای Cloudflare
🔹
نمایش پینگ و نرخ موفقیت اتصال
🔹
مرتب‌سازی نتایج بر اساس سرعت
🔹
خروجی گرفتن از لیست IPها
🔹
اجرای کامل روی ویندوز بدون نیاز به نصب وابستگی اضافی
📈
اگر با افت سرعت یا ناپایداری اتصال مواجه هستید، این ابزار می‌تواند برای پیدا کردن IPهای بهتر مفید باشد.
🔗
Github
#Cloudflare
#Xray
#V2Ray
#OpenSource
#Network
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⚠️
همراه اول بسته نامحدود شبانه که لیمیت سرعت از ۶۰ گیگ به بعد داشت رو حذف کرده
✔️
بسته های حجمی شبانه آورده
🌐
100GB
💳
49,000T
🌐
200GB
💳
69,000T
🌐
300GB:
💳
99,000T
👍
خوبیش اینه لیمیت سرعت نداره
💵
کد دستوری خرید :
💎
*1000*252#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🤖
ابزاری جالب برای اتصال دستیارهای هوش مصنوعی به شبکه‌های اجتماعی و سایت‌های محتوایی!
با این پروژه می‌توانید به مدل‌هایی مثل
Claude Code، Codex و OpenClaw
اجازه دهید در سایت‌هایی مانند YouTube، Bilibili، Xiaohongshu و LinkedIn جستجو و اطلاعات جمع‌آوری کنند.
✨
کاربردها:
🔹
بررسی نظرات کاربران درباره محصولات
🔹
جستجوی فرصت‌های شغلی در LinkedIn
🔹
جمع‌آوری و تحلیل محتوای شبکه‌های اجتماعی
🔹
تحقیق و بررسی بازار با کمک AI
⚡️
گزینه‌ای کاربردی برای توسعه‌دهندگان، پژوهشگران و کاربران حرفه‌ای هوش مصنوعی.
🔗
Github
#AI
#ClaudeCode
#Codex
#LinkedIn
#YouTube
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RoiBkjNpz0TYiQ_eEc__KZZsqmY83-WHybhtHCbPyNB4tMOKQUw1vb_I7ZWBGXoUnMebk6Grmx6I4xWTSJUFGImKzS9aqTTg_lAHSZNhPXyXTDUYN1H5YXyE0cHxJzs5EQU0XuLzEwU_RDs1ekgjayJUN0BfKi7fEtgRJSGXa4vVvvaVhR4yIqdADDuEICYhgFK5HHyT5vMb_lNiaZZj8r91HWngXyxy5ckbeD_l6RPcX2MSxDDYfjT4b6-G5htAZYi-gFTNOklN7auSMbr8A6e0X7L5lTOtjsE2yYBrUTO4V2nN3wHWTyyJbx_epWcsIaHaWd4crSTQY5z7Ot-d7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLzlferuec61EGk4ttWhwufiM0nQ60cCMVzuHt-lkP2JDKkE60pjp-4uNk6x9Y1gxmriSSUsVaWgvdLmx7kN3z77nJ20mkCL39Ku0auQprCFjCzwppuc9ngaLde8DYGW_0iYAY4HNV9kQ-a3w9_XFE75W0S52TWELaSEhmOHT12PDLaT4X0MvgsxM8Vox8jbPKUJgdmyrjB5fEBEI69PDwlU3gj5wUKzkqeJcy-ZlVyGIQP8VeD08AilZZOdlYEqAem2wkFVzvuHsWYGHK491hHonZGG55WYV2NepPrteZEoZKQTvqGuEg_BTxSBA8u2-f1vMXGDPyOyNSA-N8s8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jyvf-rcqPDyVa__7JXI7l1RQvhWZZVnM4jXL1bUOeK78JPX3bSyUcicbIyTvEQfjTFFvdNJVH8WcG2z3Ch8xbzob36iGLaGHePzYBZii4xCrYww4DWXS3im63dkhXQDlu--KXopyq9RkbwbEHRsAwboie0BKMQlzLDMIbfZwoY8dHs4LvJ_g4t6RF73BWsMm1Z0ygCnhE8MiaEjLby6qqYu4l5Rmr8fLR_T8hKdW7pGJCJ-wsr4qpfnR3kr7dYKB8OFao0t7JGEuEjbKjZyZasjm0-IyszsegN0q5Cb9gnw6Hr1TDyhRtuFr27oL1WokRa3pdslvp38MoDEEQqybNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iv6N7nH4r1dhSqo2zKAX2VHvh045zBBHE28mRHtuqCJsGkHsnwT9KwHPohc808oGBqR4m9hkGLEjcpxfFpYE3KyPCmWO0TH-Uk7FgTTqNulofHJA_o5jchBh7QDF6JVf-fvpnIHoQIjdcjAREj0BvzFMIVN9AciSLMmTqsYSjZG2nGiNMS9WuUThlOh7fX0UZAUICyJwQbE_WJ3Sfq38X5_hcVPVj5_UUBNkAi3s1BWsS-GcyK3V_UoGxbEaXKF_6CRJ7QqAUET7opED_3bZ5hxP_nbADegPPfeiFixIaNY5Y21fFgCucLp7h4aU9m2oG2nrwBqp4JxT2v4KLaox3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=iRLCAPWLMt49POmgjNB4IVo0DE9C65uLy1Aov1A3wLieqrIoIb6t-FkjHyfQqXKT381uRMowcPlaCFOy-G7LpIIgzt5ZS0GKlYVklZx4Wf7nmUpEp3zP9fUie4BgcdI7BLAyMpyS-WGt8_fr4E8OCumQ6USyORWlm_iISQB6ZgyqdvrchMrUAZPCdGuxX59SWHA_rxckr8ZHKtUHj0ISihT-_ZvBYhYEzoXXDqAZqlm-wyQQO8uiZ44878Ysf5vQ_PeXDGphefKfh-BKc0cZUAhgK9zbhLyno53uNicSbl57cZ9NSyClY-3crmvD757UXuLIGS3iFYeb3DJiu1UUPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=iRLCAPWLMt49POmgjNB4IVo0DE9C65uLy1Aov1A3wLieqrIoIb6t-FkjHyfQqXKT381uRMowcPlaCFOy-G7LpIIgzt5ZS0GKlYVklZx4Wf7nmUpEp3zP9fUie4BgcdI7BLAyMpyS-WGt8_fr4E8OCumQ6USyORWlm_iISQB6ZgyqdvrchMrUAZPCdGuxX59SWHA_rxckr8ZHKtUHj0ISihT-_ZvBYhYEzoXXDqAZqlm-wyQQO8uiZ44878Ysf5vQ_PeXDGphefKfh-BKc0cZUAhgK9zbhLyno53uNicSbl57cZ9NSyClY-3crmvD757UXuLIGS3iFYeb3DJiu1UUPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
Fable 5
اکنون به صورت رایگان روی کامپیوتر شما در دسترس است.
توسعه‌دهندگان نسخه ویژه Gemma 4 Composer 2.5 را منتشر کردند که با داده‌های استدلال دقیق آموزش دیده است.
🔹
تمرکز اصلی بر کدنویسی، تحلیل و درخواست‌های پیچیده است.
🔹
کاملاً به صورت محلی و بدون نیاز به اشتراک یا API کار می‌کند.
🔹
در قالب GGUF برای Ollama، LM Studio، llama.cpp و سایر ابزارهای محبوب در دسترس است.
دانلود این شاهکار
#Fable
#Ai
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🛢
نفت خام:
81.5$
|
دلار: 159,050 تومان
🕰
بروزرسانی - 26 خرداد 1405 - 03:04
🪙
قیمت لحظه ای رمز ارزهای پرمخاطب:
🟢
BTC:
$66,152.52
(+1.00%)
🟢
ETH:
$1,786.95
(+3.76%)
🟢
BNB:
$615.87
(+0.07%)
🟢
XRP:
$1.24
(+4.98%)
🟢
SOL:
$73.79
(+4.37%)
🔴
TRX:
$0.32
(-0.41%)
🔴
DOGE:
$0.09
(-0.86%)
🔴
ADA:
$0.18
(-0.05%)
🟢
PAXG (Gold):
$4,304.90
(+0.65%)
🚮
قیمت ارزهای تلگرامی:
🔴
TON:
$1.71
(-2.06%)
🔴
NOT:
$0.000448
(-7.03%)
🔴
DOGS:
$0.000044
(-1.64%)
🔴
HMSTR:
$0.000158
(-6.08%)
🟢
EVAA:
$1.258452
(+88.39%)
🟢
X:
$0.000012
(+3.86%)
🟢
MAJOR:
$0.035791
(+2.66%)
🔴
PX:
$0.017240
(-0.23%)
🔴
STON:
$0.578778
(-0.88%)
🟢
REDO:
$0.077989
(+10.89%)
🔴
UTYA:
$0.019192
(-7.00%)
🔴
DUST:
$0.000175
(-2.63%)
🟢
TONNEL:
$0.627903
(+4.80%)
🟢
FISH:
$0.005469
(+1.74%)
🟡
قیمت طلا و نقره:
🌍
انس طلا (دلار):
4,335.20$
🌍
انس نقره (دلار):
70.01$
💰
طلا ۱۸ عیار (هر گرم):
16,296,900
تومان
💰
طلا ۲۴ عیار (هر گرم):
21,729,000
تومان
🥇
سکه گرمی:
25,500,000
تومان
🥇
ربع سکه:
47,620,000
تومان
🥇
نیم سکه:
85,960,000
تومان
🥇
سکه بهار آزادی:
163,625,000
تومان
🥇
سکه امامی:
167,010,000
تومان
🥈
گرم نقره ۹۹۹:
377,140
تومان
🛢
قیمت نفت:
🇺🇸
نفت WTI (تگزاس):
81.5$
(+1%)
🇬🇧
نفت Brent (برنت):
83.7$
(+0%)
#دلار
#طلا
#نفت
🫀
نبض بازار در دستان شماست...
‌</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
