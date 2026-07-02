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
<img src="https://cdn4.telesco.pe/file/I10DwcWki_RFPJ_ovAkZ-_ruQ9qGz6iN3STHfR14Vw8-0BvbvAiwRDTmx_kO_qQNyLZSs28nld20BWRinF7IlDJ7NBImK5YDAuluVFk6jugzyR4LB7T2-CdyXiXP1nCLcly33-f_erSoPKoEZC4mqvQqTVJihH2NbCa2N68UIVBgCMyAx6iWXCudNKpzjEkqtRItA3DrmZ6trvO1u0UUDpSke3nX0vGBtkNig7BIoG2mivmQ8Jle2XFDmrB5bspdYMuHD0AOubzsS6F6OXDZEJoC08HaM7twMQf7WN79qbCxLWP3WYvxEs73bfmTu6syuZa0Em1XdeHA7-7l9rL-sQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.66K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 21:52:34</div>
<hr>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚀
معرفی Qwen Gate؛ دسترسی رایگان به API مدل قدرتمند Qwen 3.7-Max!
🤖
✨
مدل Qwen 3.7-Max در حال حاضر یکی از بهترین مدل‌های هوش مصنوعی است، اما استفاده از API رسمی آن هزینه دارد. ابزار متن‌باز Qwen Gate نسخه وب (
chat.qwen.ai
) را به یک API کاملاً سازگار با استاندارد OpenAI تبدیل می‌کند تا بتوانید به صورت کاملاً رایگان و لوکال از آن در پروژه‌هایتان استفاده کنید!
🔥
ویژگی‌ها و قابلیت‌های این ابزار:
1️⃣
سازگاری گسترده:
قابلیت اتصال بی‌دردسر به دستیارهای برنامه‌نویسی مثل Cursor, Claude Code, Continue و سایر کلاینت‌های مبتنی بر OpenAI.
2️⃣
چرخش اکانت (Multi-account rotation):
پشتیبانی از مدیریت و چرخش بیش از ۳ حساب کاربری برای جلوگیری از محدودیت‌ها.
3️⃣
امکانات کامل:
پشتیبانی از فراخوانی ابزارها (Tool calling)، استریمینگ سریع و دارای یک داشبورد حرفه‌ای برای گزارش‌گیری.
4️⃣
پشتیبانی از مدل‌های مختلف:
دسترسی به Qwen 3.7-Max, 3-Max, 3-Plus و سایر نسخه‌ها.
💻
نصب و راه‌اندازی سریع:
برای نصب کافیست دستور زیر را در ترمینال اجرا کنید:
Bash
curl -sSL https://raw.githubusercontent.com/youssefvdel/opengate/main/install.sh | bash cd opengate && qg
پس از اجرا، آدرس
http://localhost:26405/dashboard
را در مرورگر باز کرده و اکانت Qwen خود را اضافه کنید. حالا می‌توانید از آدرس http://localhost:26405/v1 به عنوان Endpoint (درگاه API) در نرم‌افزارهای خود استفاده کنید.
⚠️
توجه بسیار مهم:
از آنجا که این ابزار بر پایه اتوماسیونِ رابط کاربری وب کار می‌کند، احتمال مسدود شدن اکانت توسط سیستم‌های امنیتی وجود دارد.
حتماً از اکانت‌های فرعی و تستی استفاده کنید
و به هیچ وجه حساب اصلی خود را متصل نکنید.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 241 · <a href="https://t.me/ArchiveTell/6687" target="_blank">📅 21:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚀
ساخت بی‌نهایت اکانت معتبر با یک Gmail!
📧
✨
سایت‌های حساس (مثل صرافی‌ها، ChatGPT یا AWS) ایمیل‌های فیک را مسدود می‌کنند. اما با ترفند پنهان «پلاس» (+) می‌توانید بدون نیاز به شماره موبایل، بی‌نهایت ایمیل معتبر (برای دریافت اکانت‌های تریال) بسازید!
🔥
این ترفند چطور کار می‌کند؟
قانون جیمیل این است: هر عبارتی که بعد از علامت + (و قبل از @) بیاید، نادیده گرفته می‌شود.
مثلاً اگر ایمیل اصلی شما ArchiveTell@gmail.com باشد، می‌توانید با این آدرس‌ها در سایت‌های مختلف ثبت‌نام کنید:
ArchiveTell+twitter@gmail.com
ArchiveTell+vpn123@gmail.com
از نظر سایت‌ها، این‌ها ایمیل‌هایی کاملاً متفاوت هستند، اما تمام کدهای تایید مستقیماً به
اینباکس همان ایمیل اصلی شما
ارسال می‌شوند!
🛠
ابزار کمکی:
برای ساخت خودکار هزاران آدرس مشابه، می‌توانید از ابزارهای آنلاین
Gmail Generator
استفاده کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#آموزش
#ترفند_جیمیل</div>
<div class="tg-footer">👁️ 793 · <a href="https://t.me/ArchiveTell/6686" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65311253ad.mp4?token=VUT1q1HFjUf57O_hz2xn4ksNjr8V08zQwAZd7h898UsHG_Aa2j9imNooi3N87p9OkNUDrVvWwg48ssJ-KM049SQQW0ZyXjflxZ7MXrgl6pYsh9cOKn-8jA2cQgUhbuTClr34uXDF4VTuMYo7Z1zgcW4xFqNwwuD9_pRU9coSf6r9OZJ71-j19eSH74bIY3P1kMhp5x4L0abxFgD-fcnvLuTUlsDSQBc0uTaixCuXDpEgO1XhkzVYRdLV1ANudS0EKj6IwyTTzgaWRJVsY0IXGAKAfFBhRWpL7Ho0qdVHCJ1AyV-Uv-eS_2ceGJNvXujG5_hDHkKeMFRUbYDUoV8SWIGOo2Qej4z4SQWoUwDjFooPqMZ92_2P0qlsS7DjX1ikBOcH2RF9pGpSn_6M1c6BV34u7j4iLIi6g10j5vywq_rdRmkg92IskjdcqBKF9JHZ7AUIOucwTout4aXNhWZ75onYg-ReP7tYiLQGlKkurdOQiAKxncWPNx-KbkRgtjQ9NGyLeGhJpiXndDMtWZ6pFHylSlULBcWinwKxQXmtCNjeb4rQ5cAQkN3k-znshKOYPszA27kSE6PJhwAbFHo4-Dkufu5EeQSQ4rTLwjQ39QWOW_R-bhUhdFWY3P36jXCoPY986QnwrFNxHDS_lJftPhwU6z0RGoBiinwv-wmmejY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65311253ad.mp4?token=VUT1q1HFjUf57O_hz2xn4ksNjr8V08zQwAZd7h898UsHG_Aa2j9imNooi3N87p9OkNUDrVvWwg48ssJ-KM049SQQW0ZyXjflxZ7MXrgl6pYsh9cOKn-8jA2cQgUhbuTClr34uXDF4VTuMYo7Z1zgcW4xFqNwwuD9_pRU9coSf6r9OZJ71-j19eSH74bIY3P1kMhp5x4L0abxFgD-fcnvLuTUlsDSQBc0uTaixCuXDpEgO1XhkzVYRdLV1ANudS0EKj6IwyTTzgaWRJVsY0IXGAKAfFBhRWpL7Ho0qdVHCJ1AyV-Uv-eS_2ceGJNvXujG5_hDHkKeMFRUbYDUoV8SWIGOo2Qej4z4SQWoUwDjFooPqMZ92_2P0qlsS7DjX1ikBOcH2RF9pGpSn_6M1c6BV34u7j4iLIi6g10j5vywq_rdRmkg92IskjdcqBKF9JHZ7AUIOucwTout4aXNhWZ75onYg-ReP7tYiLQGlKkurdOQiAKxncWPNx-KbkRgtjQ9NGyLeGhJpiXndDMtWZ6pFHylSlULBcWinwKxQXmtCNjeb4rQ5cAQkN3k-znshKOYPszA27kSE6PJhwAbFHo4-Dkufu5EeQSQ4rTLwjQ39QWOW_R-bhUhdFWY3P36jXCoPY986QnwrFNxHDS_lJftPhwU6z0RGoBiinwv-wmmejY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیه‌ساز هاگوارتز ( مدرسه جادوگری سری داستان‌های هری پاتر ) از ‌Fable 5⁩
در این قلعه افسانه‌ای می‌توانید درس بخوانید و با جارو پرواز کنید.
🧙‍♂️
‏این شبیه‌ساز مستقیماً در مرورگر اجرا می‌شود.
https://hogwarts-production.up.railway.app/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 798 · <a href="https://t.me/ArchiveTell/6685" target="_blank">📅 20:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ظاهرا کلودفلر اعصابش از ایرانیا **ری شده و از این به بعد دیگه ایمیل فیک قبول نمیکنه اگرم بکنه تایید نمیتونین کنین اگرم بتونین تایید کنین بنتون میکنه
😍
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/6684" target="_blank">📅 18:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ArchiveTel
pinned «
دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...  https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6683" target="_blank">📅 18:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🛡
آیا وای‌فایِ شما واقعاً امن است؟ (یک تستِ ساده و حیاتی)
خیلیا فکر می‌کنن چون روی وای‌فای‌شون پسورد گذاشتن، امنیتشون کامله. اما حقیقت اینه که اگر پسورد شما ضعیف باشه، نفوذ به شبکه و شنودِ ترافیکِ شما برای یک فردِ آشنا به تکنیک‌های ساده، کمتر از ۱۰ دقیقه زمان می‌بره.
⚠️
چطور تست کنیم؟
در دنیای امنیت، ما از روشی به اسم «Capture Handshake» استفاده می‌کنیم. وقتی یک دستگاه به مودم وصل می‌شه، یک تبادلِ اطلاعات (Handshake) بین اون دستگاه و مودم انجام می‌شه. اگر کسی این تبادل رو ضبط کنه، می‌تونه آفلاین و بدونِ اتصال به مودمِ شما، اونقدر رمز عبور رو حدس بزنه تا بالاخره یکی درست دربیاد!
💡
چطور نفوذناپذیر شویم؟ (اقدامات فوری)
۱.
پسوردِ قوی انتخاب کنید:
رمز عبور باید حداقل ۱۶ کاراکتر شاملِ (ترکیبِ حروفِ بزرگ/کوچک، اعداد و کاراکترهای خاص) باشه. رمزهای ساده مثل شماره تلفن یا کلماتِ دیکشنری، در لیست‌هایِ هکِ «آفلاین» در عرض چند ثانیه شکسته می‌شن.
۲.
غیرفعال‌سازی WPS:
این قابلیت که اجازه می‌ده با فشار دادنِ یک دکمه روی مودم وصل بشید، یک درِ پشتی (Backdoor) خطرناکه. حتماً وارد تنظیماتِ مودم بشید و
WPS رو کاملاً Disable کنید.
۳.
ارتقا به پروتکل WPA3:
اگر مودمِ شما از WPA3 پشتیبانی می‌کنه، حتماً تنظیماتِ امنیتِ وای‌فای رو روی این گزینه بذارید. WPA3 به شکلی طراحی شده که اصلاً Handshake به روشِ قدیمی تولید نمی‌کنه و عملاً در برابر این حملات ایمنه.
۴.
تغییرِ دوره‌ایِ رمز عبور:
حتی اگر رمزِ پیچیده‌ای دارید، هر چند وقت یک‌بار اون رو تغییر بدید تا اگر کسی قبلاً در حالِ شنودِ ترافیکِ شما بوده، دسترسی‌اش قطع بشه.
این پست رو برای کسانی که هنوز رمزِ وای‌فای‌شون ضعیفه، فوروارد کنید!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6682" target="_blank">📅 13:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd8t6vp568EB7fWZ-wLAJa0tHUbW4DHcZplkD-4GMagMcLDOxhZpBcBLc4P77xHmt3rSbqYepLcpnFcKnr4tABD5DzPbNgidKJc0NVSRM-C_FNBza-KPaXsLGyXNIM3EMEqMdPgFA292q70ZNpz6VdbQysLdpg6G_Pw9cGx7xmP03GX37RlmUyxG9NlkDwso51SjBZ4vZGwpeFn5mqWKs3qcErHUuKIpikI5kQRQNf0TSMo-EKkxz1RegiNSc1C5XZ-uSSdDI04H87PPpqpGEkNIKg_-dB4059s_-Rew9YcTumD27EWYmg2ZDN6kW_UYBta6m2mSLrdoBx3MHo_t0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6680" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است. با اجرای این ترفند، می‌توانید نسخه گران‌قیمت Ultimate را به راحتی فعال کنید!
🔥
آموزش قدم‌به‌قدم فعال‌سازی:
1️⃣
ثبت‌نام:
به سایت
gitlab.com
مراجعه کنید و با یک حساب گوگل جدید یا یک ایمیل معمولی اکانت بسازید.
2️⃣
تعیین نقش (مرحله حیاتی):
در بخش تنظیمات و شخصی‌سازی پروفایل، نقش خود را حتماً به عنوان
مدیر سیستم (System Administrator)
انتخاب کنید.
3️⃣
انتخاب نوع کاربری:
زمانی که پرسیده شد چه کسی از این فضا استفاده خواهد کرد، به جای گزینه «فقط من»، حتماً
«تیم من» (My team)
را انتخاب کنید.
4️⃣
تکمیل مشخصات:
کادرهای مربوط به نام شرکت، پروژه و گروه را پر کنید. (اگر با خطای «مسیر گرفته شده است / Path taken» مواجه شدید، کافیست چند عدد تصادفی به انتهای نام گروه خود اضافه کنید).
5️⃣
فعال‌سازی نهایی:
روی گزینه «ادامه به GitLab» کلیک کنید تا لایسنس آزمایشی ۳۰ روزه Ultimate شما فوراً فعال شود.
⚠️
نکته بسیار مهم برای جلوگیری از خطای دسترسی (Permissions):
وقتی وارد داشبورد شدید، به هیچ وجه چت هوش مصنوعی را مستقیماً از صفحه اصلی (عمومی) باز
نکنید
. ابتدا وارد داشبورد خود شوید، روی صفحه گروه یا پروژه‌ای که ایجاد کرده‌اید کلیک کنید و سپس از آنجا روی آیکون چت
GitLab Duo
ضربه بزنید.
در نهایت، از منوی کشویی انتخاب مدل،
Claude Fable 5
را انتخاب کنید و از دستیار برنامه‌نویسی حرفه‌ای خود لذت ببرید!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/6679" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...
https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6678" target="_blank">📅 02:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDn0pslniY706ENcjee6InrLC4CraiLp8ikMEuHSsWdZEioEVPz8kPSTSs3xk5H6-F7Whq-F4yCPG4uHQtM9Tt0wtK8HwF5jP1KrDWzX6QXvtjzm1xzKp3Wml66PBp8TmQ894M7ilVxehFtuW0GGyQGLAWNzcjqKKH0aV2-R6D0OMlYGkwrEDZ_Omc3vWQZ0TmRSiOaRgwdhhwsHsicFbz6z2XXjNriBjZhpqM_37T5nEcgcSvY1dIbYJK_nFfyh50H59y8dhfhbd8G8d78sBKVF6CHK9hVuAKoZCxoUFGXj7lWBGik84NjX5TPbxzmO6DaqJrrPWZ1ADtHaLEVHJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توسعه‌دهندگان چینی GLM ابزار قدرتمند ZCode 3.0 را معرفی کردند
😮
این یک ابزار همه‌کاره برای نوشتن کد و تعامل با عوامل هوش مصنوعی است: همه چیز در یک پنجره جمع شده با امکان کنترل از راه دور از طریق تلگرام.
این سرویس به صورت رایگان در دسترس است.
http://zcode.z.ai/en
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6677" target="_blank">📅 01:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN58w0VDbQGTZKAgptbdY-PxEx1ezCkpCyRF6zikCoSFlpP1oUNiPAjhH0DgCFY1cP92CTRxTLOfwdgnbGm0NppZogPKiMSMJqWBNxG5ygtBPV7nS3Q4zcFyI0k_EqYR7t6q9a1nEnVIn3KI46fqfXoAfQ7_AbR9zC-1VcHlskJOqacDsAngIi8kr4QRo68vgsGutdaeOk1ywRttsTdddunxtJHdwakYi4vF-6moGdBqNxrxcqEwd0DCTrM45PonScgoBJMfNZbASb9MgZeNGbeUhd96K1sttcGd6jYM0s7-zb9mdtYDgv3aPC7M1wBPTJ1i79-igIZKFZ3F_lN2RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت Fable 5
🔥
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6676" target="_blank">📅 23:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=nocE6EcS9SSZHqaobuY1_CEZV39qIxfCWnh9ILLqv1jFE_Rbu7moYl-F4A--Js-7ihWSXwuEcmFWgPsPwjytCPHIGW8D6PLWdElADhAmrRBGqgKs6TNcBO4E06pTl1VgCGCMXmCiWd5qa2dJycueEN9ptdn64-enL8Fu1GP1vUWI9qcbce_CXsfEN_UUQaawmY3xHT3RCAIJplQLHySFccwkdLPs2qFX5AT9phF2fCjssEeKRU8-tyjZw6bmjMU0MihCYY6WQ_saXDbYiAj67D9tCyr8zHvphdqY0cGSYt4vX9A8J86tHe7Nb3SlZm_YCvTn7TGbQLHmSOyObizbWV50teFSdSBDGQcJHB6L0UwpVBxcG0I2JG6nbC47e-wMRhYAVa-_ymLt90LyIjstnyiTpxU7-LFtUqtcNZ7X6I6vJyjfM_AI8Zp-RB7m0H6adWPuNRI8NK1x6S9UBoFwTrhP_k7yiet8NR9gsOQl-r42ZevlYvKyX4OmtX3e81kfsXsFlFkVLa8FT5QAZWzzJZtWYakGoFD8Meyif-jjpiLSmv_JcddPl56B9USWmWukPTFB8JqLmbDczPblYq7WRtyKwz6WQhHOt7pnwPareCfBqVXf1Jb2nIcw1fPpPrKDQ5_BBsMVKWhRc2f6eU0miyJYRgFIGaLlUd01DTAy-XE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=nocE6EcS9SSZHqaobuY1_CEZV39qIxfCWnh9ILLqv1jFE_Rbu7moYl-F4A--Js-7ihWSXwuEcmFWgPsPwjytCPHIGW8D6PLWdElADhAmrRBGqgKs6TNcBO4E06pTl1VgCGCMXmCiWd5qa2dJycueEN9ptdn64-enL8Fu1GP1vUWI9qcbce_CXsfEN_UUQaawmY3xHT3RCAIJplQLHySFccwkdLPs2qFX5AT9phF2fCjssEeKRU8-tyjZw6bmjMU0MihCYY6WQ_saXDbYiAj67D9tCyr8zHvphdqY0cGSYt4vX9A8J86tHe7Nb3SlZm_YCvTn7TGbQLHmSOyObizbWV50teFSdSBDGQcJHB6L0UwpVBxcG0I2JG6nbC47e-wMRhYAVa-_ymLt90LyIjstnyiTpxU7-LFtUqtcNZ7X6I6vJyjfM_AI8Zp-RB7m0H6adWPuNRI8NK1x6S9UBoFwTrhP_k7yiet8NR9gsOQl-r42ZevlYvKyX4OmtX3e81kfsXsFlFkVLa8FT5QAZWzzJZtWYakGoFD8Meyif-jjpiLSmv_JcddPl56B9USWmWukPTFB8JqLmbDczPblYq7WRtyKwz6WQhHOt7pnwPareCfBqVXf1Jb2nIcw1fPpPrKDQ5_BBsMVKWhRc2f6eU0miyJYRgFIGaLlUd01DTAy-XE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
واقع‌گرایی GTA 6 شگفت‌انگیز است: یک علاقه‌مند صحنه‌هایی از تریلر رسمی بازی را در دنیای واقعی بازسازی کرد.
بعضی از صحنه‌ها عملاً از نسخه‌های اصلی بازی قابل تشخیص نیستند
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6674" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0KPEJLlvGl03FffGOo_bZQ1zruGZbJGv5xn--jQkKIgvOj9h9UpB8YKEdRweYb-QCjQPh-6_E3N3BMjd4kbHzuXHlM77WCv1nq3R5Lx5lNvLYUxhDn8ytum28w003sK0rpwlxBqd9Jj24VYOIfu4SpEPhUPVznK8JwMIBrpRj9liBcA81leIsg_9j5Ikt8X6ORJC08w4acTeYpa8zdGpB7QmAJrW4XQcbtR_HMPHl8OS_i_Hkpzsac5RNzkbETSszqYZayBvc6Aez3-WKp725SIH5Aw7uxHzJkU1ZyvdMHqsmgSA1DH0drfBOGVquL7r74KjhrVeY-Vc1U9H38WQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون هوش مصنوعی مهارت خودآموزی (self-learning) را به دست می‌آورد — عامل یک راه‌حل پیدا شده را به خاطر می‌سپارد تا در هر جلسه جدید دوباره آن را جستجو نکند.
🧠
وقتی هوش مصنوعی با یک مسئله مواجه می‌شود، این روش را ثبت می‌کند و علامت می‌زند که دقیقاً چه چیزی کار کرده است. دفعه بعد سیستم مسیر اثبات شده را دنبال می‌کند، به جای اینکه دوباره گزینه‌های ناکارآمد را بررسی کند.
https://github.com/Kulaxyz/self-learning-skills
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6673" target="_blank">📅 18:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6672">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq_WSMKib5AvVBLsmrNWGyNhpUy1fQIJ7UoMTdCCX_yK1pXGjl23iGlJvRjSrT8OUU93iBEgnzlA2QJZ73SrDZq_7x3OBAtXCYYS_n-Ae2mM89YN3Bz1aKIVyGZUB6Xsex_UOWV9e4B0nnSdSYFyIHub73afPoGDq_xh0kLw4zXZfQQCVLr-8EJ78D5Pbnrbpmpwt7YdESihlZRDicBx0xjbC77dch4rrjNjxEu9YNWxOpvJ33nNxeKynOMbb3nR6o0kEGjQC86cgbaP9X7gXsQdOX0irTJmGg0eLaAnNQi1PNjnUubN1FhQLUqGjXScr84Q4qXqk9ReufePwVjUHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">RevPDF
ویرایشگر PDF سریع، بومی و متمرکز بر حفظ حریم خصوصی به صورت آفلاین است.
این برنامه امکان ویرایش متن و تصاویر را مستقیماً در سند PDF فراهم می‌کند و همچنین عملیات‌هایی مانند ادغام، تقسیم، فشرده‌سازی و تبدیل فایل‌ها را انجام می‌دهد.
تمامی عملکردها به صورت محلی روی دستگاه اجرا می‌شوند و حریم خصوصی کامل داده‌ها را بدون نیاز به اتصال به اینترنت تضمین می‌کنند.
https://github.com/Pawandeep-prog/revpdf-release
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6672" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6671">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=D5tik6w5RiuN-kPw7_7tMhvbnzr3gGOu1iWJOdnetoCUmnVyynYzfX2YTk2gE0_IRmAWcxl2KDaGfftm7ksfQKLzIExRIyF38sj0AEyMMIKJqzwp07iwDMgVqU8uVHmuLz4TanaZS_QxMYzD1W6Bh8j5sGXi71Y1AHEYrlq15N73t4YoJ0AhKKgrEgcPPtODZvgYVlHIbuboFIkPhHH9kyMgQkk1M7Xd2WSjNBx_lSDpJ6cUVW3dcUKk8R5xp01awfGoKxgxSgMo9yQlub0l1NBNw8oc5Z_V06mHo5j2M6BIQB79BdEdWYD3gdIaT6C9WBU8qhT1kUB0pkIcdLW2IHC6UGjvTiLVhcEhDKWxjAXxy4OPHjkj8SDYk2VY8nMkcIi54WD56f7w_EFthVs4_zNSlOL0wS0S2wbvdPb-edW2DSMYE1TKLdGNYkdXgKFxxURJYNmw7fq7nJjpuYe7cR35VmGUURRys5LhKx0RzHQF2tP6mCaFMtliLn0yOrWbT-0JrmdpdeiqTwj50PiWs_yr9AuXD0YSShTXn9Cz9RYUjC7mIbtI_Mh2_A9fh9gBI7s9pdnhFTMG_NRj-wF07QxnerNJY82KgKP8e-bfBSBF96pqmeln9PBxOLn1uf4BqkAvhV0nVruJES78T1M0n30tMH6_0MUonb5-1BZ-COk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=D5tik6w5RiuN-kPw7_7tMhvbnzr3gGOu1iWJOdnetoCUmnVyynYzfX2YTk2gE0_IRmAWcxl2KDaGfftm7ksfQKLzIExRIyF38sj0AEyMMIKJqzwp07iwDMgVqU8uVHmuLz4TanaZS_QxMYzD1W6Bh8j5sGXi71Y1AHEYrlq15N73t4YoJ0AhKKgrEgcPPtODZvgYVlHIbuboFIkPhHH9kyMgQkk1M7Xd2WSjNBx_lSDpJ6cUVW3dcUKk8R5xp01awfGoKxgxSgMo9yQlub0l1NBNw8oc5Z_V06mHo5j2M6BIQB79BdEdWYD3gdIaT6C9WBU8qhT1kUB0pkIcdLW2IHC6UGjvTiLVhcEhDKWxjAXxy4OPHjkj8SDYk2VY8nMkcIi54WD56f7w_EFthVs4_zNSlOL0wS0S2wbvdPb-edW2DSMYE1TKLdGNYkdXgKFxxURJYNmw7fq7nJjpuYe7cR35VmGUURRys5LhKx0RzHQF2tP6mCaFMtliLn0yOrWbT-0JrmdpdeiqTwj50PiWs_yr9AuXD0YSShTXn9Cz9RYUjC7mIbtI_Mh2_A9fh9gBI7s9pdnhFTMG_NRj-wF07QxnerNJY82KgKP8e-bfBSBF96pqmeln9PBxOLn1uf4BqkAvhV0nVruJES78T1M0n30tMH6_0MUonb5-1BZ-COk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
«اودیسه» نولان - تریلر نهایی. این فیلم یکی از بزرگترین آثار چند سال اخیر خواهد بود.
با بازی ستارگان: مت دیمون، تام هالند، ان هتاوی، رابرت پتینسون، لوپیتا نیونگو، زندایا و شارلیز ترون.
اکران: 17 جولای.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6671" target="_blank">📅 18:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1ZRsLcieQtBu9GrRyNHNvI9jRP74g1e6XfQkNq-i0SZF4Rarzg8iTUPXijF8y836LI_q_JzE3FRmvN4FKc9vt_w9jegiDuzmibAUVUNBclgacmtxPBd2TMtkbrhS8dhkXqnkD2BUl59mE9NG4HN4wWv-nVOqzglIbzr3_ZyRCx2I0P5jvgT9_04BSl80gqFui9UhLPKXZMxjPZV8pxw6HS332C4_UYFoKtiTlW47XqRxsdptxrxQyP3VctbS9tRF2xgNM42Y4ODaHBspB_NvBULCd49A_hfw1AJBh89hv3F6I3wa54DDnNePXmmDMtL7w9i-51hQ4LXoeeGDYzspw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض چند ثانیه هر نوع کپچا را در سایت‌ها و منابع دیگر رد می‌کنیم
• به سرعت بیش از ۳۰ نوع کپچا را حل می‌کند، رفتار انسان را تقلید می‌کند تا هر محدودیتی را دور بزند.
• با چند کلیک روی کامپیوتر نصب می‌شود، نیازی به ثبت‌نام و نصب نرم‌افزار اضافی نیست.
• فوری و به صورت محلی کار می‌کند.
https://github.com/clawdbrunner/captcha-solver
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6670" target="_blank">📅 18:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268d269709.mp4?token=C0kkf81tTfWjzV-cvDJ9Ghw6FkbQLz0Vt0zW3h5ra3Rs71und6NvBCa1UdqELOCbbDC6NOK5konl7GO2-PtkXcKIS5zVYWnQdkkdvg8RQE-NmrRszJmi38WUkzUWKZvrZRD7Hh1UkYOLZk33i138KJ1HW7Jz2_grz8hBmU8kKMfTOUdAWw84XbX9kZrdbgIjlSuP7qM_8e5FEu8KECTrCi1u9xa-TWYoAcIl6t0VmQ1MrnhWjad78LeJ4r-r1MkQLyOinYwqz__V0bRrWzySoA4KnYAxCgNN5E-D6S9OE2GL8yjwnu6-SBJHgobrR2C_84fv98SvAiakW07xhNZhrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268d269709.mp4?token=C0kkf81tTfWjzV-cvDJ9Ghw6FkbQLz0Vt0zW3h5ra3Rs71und6NvBCa1UdqELOCbbDC6NOK5konl7GO2-PtkXcKIS5zVYWnQdkkdvg8RQE-NmrRszJmi38WUkzUWKZvrZRD7Hh1UkYOLZk33i138KJ1HW7Jz2_grz8hBmU8kKMfTOUdAWw84XbX9kZrdbgIjlSuP7qM_8e5FEu8KECTrCi1u9xa-TWYoAcIl6t0VmQ1MrnhWjad78LeJ4r-r1MkQLyOinYwqz__V0bRrWzySoA4KnYAxCgNN5E-D6S9OE2GL8yjwnu6-SBJHgobrR2C_84fv98SvAiakW07xhNZhrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شبکه عصبی Gamma به ChatGPT اضافه شد — حالا می‌توانید پرزنتیشن‌های زیبا را مستقیماً در چت بسازید.
ابزار هوش مصنوعی محبوبی که صدها هزار نفر در سراسر جهان از آن استفاده می‌کنند، در ChatGPT ادغام شده است. حالا کافی است ایده خود را توصیف کنید یا متن را وارد کنید، شبکه عصبی آن را به یک پرزنتیشن آماده با اسلایدهای طراحی شده تبدیل می‌کند.
می‌توانید تا ۱۰ اسلاید را به صورت رایگان تولید کنید.
🔗
لینک
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6669" target="_blank">📅 17:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvLtTP_DXKO1S9awqE2usz2oiVSeM39obb5HFjhnwmAnJg6LvjHNk_Xz5SL5kDWNUD-2O8JNZH1NzIZrgBdVesGeXTX3xiePQxezNpcRgqtATuE1tlKVcb1SbRzOvIEQWygkMss7Um3BsqpNwjLFnpEIYr63YjcH_jTX7Db17rELcNWzJ3KGXDS3WADJKgukmGEsrrRmwkQEvCJROh3RuJylSWfGCTT2XTZ5NRpd288kFR0QekJrD7cGUaQu7UvVgLUyRI9JjVQMBEp_rhhQbql8wErtZ0E-a466KEC2-5mGBmJFBNeRY3FT_SJC-i0Br6BtzRKUn_W8xBFzPCti2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دیسک‌های بازی پلی‌استیشن سال ۲۰۲۸ ناپدید خواهند شد
بازی‌های جدید فقط به صورت دیجیتال منتشر خواهند شد. همچنین سونی فروشگاه PS Store برای PS3 و PS Vita را خواهد بست.
یک عصر به پایان رسید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6667" target="_blank">📅 17:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚀
معرفی Superfile؛ فایل منیجر مدرن و فوق‌سریع برای محیط ترمینال!
📁
✨
اگر از طرفداران محیط خط فرمان (ترمینال) هستید و به یک مدیر فایل قدرتمند، زیبا و سریع نیاز دارید، ابزار
Superfile
دقیقاً برای شما ساخته شده است. این ابزار با رابط کاربری بصری (Intuitive) و کنترل آسان از طریق کلیدهای میانبر، تجربه مدیریت فایل‌ها در ترمینال را به سطح کاملاً جدیدی می‌برد.
🔥
ویژگی‌ها و امکانات برجسته این ابزار:
1️⃣
پشتیبانی کراس‌پلتفرم (Cross-platform):
اجرای بی‌نقص روی تمامی سیستم‌عامل‌های دسکتاپ از جمله لینوکس، ویندوز و macOS.
2️⃣
شخصی‌سازی بی‌نهایت:
دارای سیستم پیشرفته برای نصب پلاگین‌ها و تم‌های متنوع جهت تغییر ظاهر و افزودن قابلیت‌های جدید به محیط برنامه.
3️⃣
نصب سریع و بی‌دردسر:
قابلیت نصب تنها با یک دستور ساده از طریق پکیج‌منیجرهای معروف مانند curl، winget، scoop یا Homebrew.
4️⃣
محبوبیت و پایداری بالا:
توسعه‌یافته با زبان قدرتمند
Go
که توانسته بیش از ۱۷.۷ هزار ستاره (Star) در گیت‌هاب به دست آورد و نشان‌دهنده استقبال بی‌نظیر توسعه‌دهندگان از آن است.
https://github.com/yorukot/superfile</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6665" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFhxY7jDfw6dbTMI38muOkPKQQYOp6deH3UcqSHNRUm1PLEmiMOOpmJecgG5gYHKs3BzDohyRmobTy7hYtGhqifdXft1_3NtVc-hZmZO7t73hnGNtVoW3V2SiRp87dgtpxdGVu8kFRkVYtNM3WyFAo2R2XGcyUbOEbq2_n13Fr59LGv0FYWL910JbMsbnZkZk_BM1P_dPDKfhcIH2iG7BpW--b0Z2o0oac3xWWnAcRCzpdGASJGds-HbjZVRd-yJ_XsVGma0UJQ9tAPJrvvI8tL9cdV1UyfpXhf6EmEDLKyiI89zP8xkum4XCIJKTkTweoQM_lhsZo5jPjNewor3Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اروین یالوم خودکشی کرده ظاهرا
😐
اروین یالوم نویسنده و تئوریسین روان درمانی اگزیستانسیال</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6664" target="_blank">📅 15:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUyG8zdEG1vciH198wWBqHljTiWW2kYQ2ma8CNpOuVwP1oiewGI4wgWTNQKwP4DTdCIGSWMIcAV75fSLrC6lkldppzRPKUNmZ4jdLQTBNaKRVJkIIPjsPwjJAxLUFYaUCwjePTEaNAqvLN48BgPf_MwncSXHPsLbWaN7fiIY79CTYvsZqHnhw_FcWms4Jjr7CKOkhzX9qG06bCctLCBnfk55UWe_i1Jhn6OboeTN0Wc_ZswU9Xfr1XaDx2-xyZ1qibdsUKO3nJY9TSHUGvJHYg8a_0M0uMT2Rf_utcgFvo0VqpvFsg1RgKQee6UXWlVWzNXJTW161-Ur-rPpqNd7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر سرویسی راه‌اندازی کرده است که پروژه را از نظر سئو، جستجوی هوش مصنوعی، احراز هویت ربات وب، MCP و پارامترهای دیگر بررسی می‌کند.
سپس به سایت امتیازی از ۰ تا ۱۰۰ داده می‌شود و یک پرامپت با اصلاحات ارائه می‌شود که می‌توان آن را به شبکه عصبی داد و سایت را بهبود داد تا امتیاز خود را افزایش دهد.
https://isitagentready.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6663" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJjfv8wvdrJ7FXqANfh39r_tnS3nwJizf3wF93_lcJyZDsMFME1zv8EO7zxGhIdT0x447OnPnYJYfd4bZ3NrNTxnW5P2hHvvIYq51dIllgJ11rxO4Ku01oj7Srke6yqlJwjbVQyBTfumrvWmJBuxMV1jLCWp5v34h1aLf_OISGQ7nMJrXM6STV4j9jwxMTugQ1ntoInBAV-K5-SdJheTTsmjVZ2bhROfoJJTHuKO_ayyd7CcR5lPpWITyX0lPO_9DfoH3ZH6x853kM3nCWqzqzSYcF244UCrKKeaYaHNQAx461ehCpNlbfuJCF4CQOgzUjJPGbxGCztgAStSYCuuCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع مفید برای توسعه‌دهندگان: در گیت‌هاب یک فهرست عظیم از APIهای رایگان برای همه موارد زندگی جمع‌آوری شده است.
🌐
بیش از ۵۰ دسته‌بندی موجود است: از آب و هوا، ارزهای دیجیتال و مالی گرفته تا یادگیری ماشین، نقشه‌ها، موسیقی، اخبار، انیمه و میم‌های بامزه با حیوانات.
🐱
💻
https://github.com/public-apis/public-apis
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6662" target="_blank">📅 13:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dq_OJ7dDgUtVcfGWzW3vUQ1EbwBvO1wbav-jWFTc5y6KjC_tc1VNQnw5adn_rA3HVzfcdn-r2MGPARkgcCuUlAFaBywFBi-ve3p-djbJiz5vZNR6iAQytHtTrx03cf6x7jwtk64tgcI5-AZi8OqlCKV7yUwJxa_wWMP65ZQpjDSMd4Wo-B-qkNtGXchfghENLqGSCpA7yq7emAjHAapYpuInkld46FYUOi3ne47ilIAdORhrT5ANt7N-2eRUvJERfC_A01EeknIcgGARBpWQvEaGCGV5lTbD-149YCiY45Sn-O9WcwMkji5N1gv0fcMraUn3rxJgXwRPZ7mh3KBcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkjJWGijd5iVny95bjzaR-GsoobMQpgaLayGxXVb5fMnbMmQ2_m8OH_9fgPlkkq-Bs7M6pqEHS8-qYRAS1mY_1apmSp_zXbhokiLNSm5DaJ9Pd3MloK7IMsRkR1oSuyhpTBxVBXLbrz09VF4nBbMPCdyJ0TaV3HUNl5Grki1Cr_dyonOxXfr1J4mcYWK9LhGjNe6TXw3S_hULDOsy3R65hSBIBVtuosXcq5fqTipdaDk-m01Tj6fDNwqg5ZvhrTGQVpstutbvbP23BvVB2NPJJ7I2JB4_ydcxILyu2r6sKEIccw4SmzooMare-WboahXjm4_griCyFT32am2I0VmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AsWNQQt6dwf6Ngy6igYoNM1mhBjVEhWlZwA3G71y811TZ_K_2MvqIYbaSupzzOMsMmOcodMSN-SY1EKW7IaGelcug6dRxN5afg6XJYYHQVDLkwE7VRZJzY7qxKh6XSyfe0jXXn8oSMEMBGuwGTlYNr64E0rFMTiAXLltMXac2CAVPQIgFZcBT-JnU8BpV-WDW2uMB5Dz8nwTANcoJKKNlMSA0W1u6sST9CuIemIDFs-FPtjozH7chfmrnDImiH4mFy7Qg8_pB1NyGAmiXnMERgmrF4l47P4ZXfA31GqlCRp5Ee11dn6RWCnf-A7IB0X62YHZJaQR62MY3NqmZ-HCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQDoNrEAXQoqbYeXsd-sat_HhyI5Y2I_DQk3E9qCzedP1QMgXDeNoNOe4WhkJLaY_7sH5OV0aj9-jMIIumDrMADbpImdhecyg_7i2Q_3XZegoXAXnCEBwgtbOUPKh_GYvZwucXUdGsK_fAn4kzwpWnj6H0swNg-IYlW_WJo6zcJrTda-vgpzgcxknzt2HDkXkkwV2fuOBHBiL2YQplLEb9Coacr4Z3Gsa3MvZLzfKjOADxjiVdN1g_Zk1GLPjE07GlZ_mmI8y2T2MWPl8LUN95zaNaIVaG2ooYskS0DVwNj9wmSfr2gcKaInUIv5hppSPAYh7OufW54EtCJ8kUHpig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">PlayTorrio
مگاتورنتی که همه چیز را دانلود می‌کند:  بازی‌ها، موسیقی، فیلم‌ها، کتاب‌ها و هر نوع فایل.
https://playtorrio.pages.dev/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6658" target="_blank">📅 09:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUdHdyolTReuy-tAgzH1A0xZDgUqVWceo4Ct_lOHAn4vSNkUc0p00ba8PzXFKVbU_u6SkBhYn_J8EgIV5haq2OZtU4ClIAwT1CQnY3wOFe6X9f2_m1LRpBLn7WQWqZIE6Yzp8CGO4R012fH7Xvr2RkT5C2-fYQhU9bm9LkWysslHlE1j7P0CXHyZE2JvmJmBQZRDuKmfCsCTVLO3vIA6UbPfR64Ip0JpbeKf7wBj3gJ0Y_XEKplGRdI9tqz-SaZGj7Do8eaxnNi5AHXMR9xeLV63K8dLurPPX4UiYeWWq3eV8gPz44LTSipIA-V4ib4_ELxgcBs-HxTE9bPWW6QL8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود Mythos و Fable 5 برگشته‌اند! دولت ایالات متحده این دو مدل‌ رو از حالت مسدود خارج کرده است.
امروز Fable 5 برای همه کاربران در دسترس قرار می‌گیرد و تا ۷ جولای می‌توانید تا ۵۰٪ از محدودیت‌های هفتگی خود را روی این مدل استفاده کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6657" target="_blank">📅 09:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEh9-NTMrMeKm-TJm2kd_laaVNMkKdPQohlOteMRc_YDco8UC9WWsmOIIf6sfdvB4ESVZYo_fhbqheADxPymnUBC0hGTZpexcg3JMHegBoSM9md77a6EhbIJva9o9_7stjHcNy8XNJQt5YLLhphkPJvd84tvAVEEhZQKOouQ63l00rNOFrU7-VZcb7-NY2XIssPPujLhTLn7PaOjWy7hlS51Le88rmbpWhK5TsH06R10bOVcUiNIhYGoofTYQtYyJbTuoKAdlJfhy8T96WgwoFa0Cj5NhoOWxWiWdLv_JP--rzElNd_NdOEEAsr6t-ba9mqVrnk79EbK32p0POWwvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود اوپوس بدون سانسور منتشر شد!
توسعه‌دهندگان Qwen 3.5 را با داده‌ها و استدلال‌های Opus 4.6 آموزش دادند و یک نابغه شرور واقعی ساختند.
• محدودیت سوالات فقط تخیل شماست.
• می‌توانید هر چیزی، حتی ترسناک‌ترین‌ها را درخواست کنید، اما مسئولیت آن با خودتان است!
• به صورت محلی اجرا می‌شود و بسیار سبک است.
https://huggingface.co/DavidAU/Qwen3.5-9B-Claude-4.6-HighIQ-THINKING-HERETIC-UNCENSORED
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6656" target="_blank">📅 08:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ArchiveTel
pinned «
🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6655" target="_blank">📅 08:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">درود دوستان AssA هستم
بابت خرابی ربات
@REN_WZA_BOT
دیروز معذرت می‌خوام
حقیقتا به خاطر شرایط نتونستم سرور تهیه کنم و ربات روی کلودفلر ران شده
فکرش رو نمی‌کردم که قراره انقدر استقبال بشه که سقفش به نصف روز نکشیده پر شه
😄
خبر خوب اینه که یه ربات بک اپ گذاشتم برای وقتی که سقف اولی پر شد بتونید کار هاتون رو راحت روی ربات دوم انجام بدین
جای نگرانی هم نیست تمام اطلاعات دیپلوی ها و کاربر ها انتقال داده میشن پس عملا هیچ فرقی برای شما نداره
مورد دیگه این هستش که خیلی از دوستان بدون اینکه پنل قبلی شون از کار افتاده باشه یا مشکلی پیش اومده باشه ده تا ده تا میسازن که واقعا عجیبه
🤔
خلاصه که دیگه قرار نیست به همچین مشکلی بر بخورید
و نکته سوم هم اینکه ربات دوم کمی با عجله ساخته شد اما از تست های خودم سالم بیرون اومد
اگر باگی یا مشکلی دیدین با تگ کردن آیدی ام توی چت بهم بگین
@Assa_7788
(بابت مشغله های کاری و پی وی شلوغ به احتمال زیاد پاسخ ندم بهتون پس ممنون میشم پیامتون رو با تگ کردن آیدی ام توی گروه بنویسین)
و عذر بنده رو برای طولانی شدن پیام بپذیرید
🌚
❤️</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6654" target="_blank">📅 05:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الیوم اکملت لکم دینکم
🚶‍♂️‍➡️
😂
(حس تکمیل پروژه خوبه)</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6653" target="_blank">📅 23:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6652" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9QmGZkDurHZwvVeIT-05RmgyvQ7ZpTiD8RLKrYXCt25XDEv91ymI8oP4oNneTIi19tvNdrQHR8sAxoiRDCHURPsmbUTiBB8WfdIL5s5mRZOdV5Bn9HLuIAGN3VNMynvBHolk3Ql6DInQdyEVCo-mjpfXkFU8-aD6oi1MLV9Zoe-0U4SYQVnwX-NUrqn1g2madu-sp_ycgN1tJ4C2ZO0gYZ67cvKAWeKDKtHKsHOlrMJm1Qabc_w4Wq4iB-ZkezLbpIqaltYOiPq0dZtZXw7FK0thLCCpY7TG1oagIIy7M2E8XeIcg16jURQOJ_OUpX3W9lXrgWfbaS7cY8qZZ1t2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=JnpHyg-Vc40</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6651" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CFMail@ArchiveTell.zip</div>
  <div class="tg-doc-extra">471.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6650" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6650" target="_blank">📅 23:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6649" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام!
تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک شدن.
تو این آموزش یک ترفند فوق‌العاده رو پیاده کردیم: ساخت یک سرویس ایمیل موقت اختصاصی روی دامنه شخصی خودتون با استفاده از زیرساخت رایگان کلودفلر!
🚀
این سیستم کاملاً ضدِ بلاک هست و می‌تونید تا بی‌نهایت آدرس ایمیل فیک بسازید و همون لحظه پیام‌هاش رو دریافت کنید.
🎥
آموزش ویدیویی و قدم‌به‌قدم (از صفر تا صد) رو تو یوتیوب آپلود کردم. حتماً ببینید:
🔗
[لینک ویدیوی یوتیوب ]
👇
خلاصه مراحل و کدهای مورد نیاز برای رفقایی که ویدیو رو دیدن:
۱. مخزن اصلی گیت‌هاب (برای فورک کردن فرانت‌اند)
۲. ساخت دیتابیس (D1) و کش (KV):
یک دیتابیس به اسم
mail_db
و یک فضای KV به اسم
mail_kv
تو کلودفلر بسازید. فایل
schema.sql
(موجود در مخزن بالا) رو تو تب Console دیتابیس اجرا کنید.
۳. متغیرهای طلایی (Environment Variables):
موقع ساخت Worker برای بک‌اند، این متغیرها رو دقیقاً با همین نوع و مقادیر اضافه کنید (راحت کپی کنید):
DOMAINS
(نوع JSON)
👈
["yourdomain.com"]
DEFAULT_DOMAINS
(نوع JSON)
👈
[]
DISABLE_ANONYMOUS_USER_CREATE_EMAIL
(نوع Text)
👈
true
JWT_SECRET
(نوع Text)
👈
یک_رمز_طولانی_و_رندوم_انگلیسی
ADMIN_PASSWORDS
(نوع JSON)
👈
["رمز_ورود_شما"]
ENABLE_USER_CREATE_EMAIL
(نوع Text)
👈
true
USER_ROLES
(نوع JSON)
👈
کد زیر رو کپی کنید:
JSON
[
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "vip"
},
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "admin"
}
]
🚀
مرحله ۵: آپلود کد بک‌اند و هدایت ایمیل‌ها
۱. در منوی
Runtime
ورکر، تو بخش Compatibility flags، کلمه
nodejs_compat
رو اضافه کنید.
۲. روی
Edit code
کلیک کنید و کدهای فایل
worker.js
پروژه رو کپی و پیست کنید. Deploy رو بزنید.
۳. تو تب
Triggers
، یه ساب‌دامین اختصاصی (Custom Domain) برای بک‌اند اضافه کنید (مثلاً
apimail.yourdomain.com
).
۴. حالا به بخش
Email Routing > Routing rules
تو دامنه‌تون برگردید. اون پایین قسمت
Catch-all address
رو ویرایش کنید، Action رو روی
Send to a Worker
بذارید و ورکر پروژه‌تون رو انتخاب کنید.
6. اتصال ظاهر سایت (فرانت‌اند):
مخزن پروژه را در گیت‌هاب شخصی خود
Fork
کنید.
در کلودفلر به
Workers & Pages > Create > Pages > Connect to Git
بروید و مخزن خود را متصل کنید.
تنظیمات Build (دقیقاً این مقادیر را وارد کنید):
Framework preset:
None
Build command:
npm run build:pages
Build output directory:
dist
Root directory:
frontend
تنظیمات محیطی:
یک Environment Variable به نام
VITE_API_BASE
بسازید و آدرس ورکری که در مرحله اول ساختید را در آن قرار دهید (بدون اسلش آخر).
تنظیم SPA:
در مسیر
Settings > General
، مقدار
Not Found behavior
را روی
single-page-application
تنظیم کنید.
روی
Save and Deploy
کلیک کنید.
ارادت، Bachedev
✌️
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6648" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سورپرایز امشب
اختصاصی
🗿
❤️
از یوتیوب
تقدیم به بچه های گل کانال</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6647" target="_blank">📅 22:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLz_tLTUhLldryULPG_QEUYK24sj_PD3jYiFnbBvGHGMTz-jmTBSFJd6q8FnNnRputQZ1t21YTXTBds29nT9bguloen6JZQiFOrx6EjasFgENfATDt2CxcIqg9Wx2EhRjZqMuV6dghWA_s2ebhyOBlAnlwzufxTTUiXgEVf2i6kVD6nFHDZNJsw8FY1UGpwEwgxefpHU9GLOCY5cOnb2kewP02BzcT1ns-ZbE33iay_eD4qVv1POWicZpMESY89GJ-tZQjnBeWs9ssk0-wey9D2QsBrZEkJ6rIkIBmhD2aPwUR8CskOzwICkziz3Gv9COGTypzJ4t8raumVotQETQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude Sonnet 5
منتشر شد!
مدل قدرتمندی برای کارهای روزمره اکنون برای تمام کاربران، حتی کاربران رایگان، در دسترس است.
• از نظر عملکرد بسیار به مدل Opus 4.8 نزدیک شده است.
• به مناسبت انتشار، Anthropic همچنین تمام محدودیت‌های مدل‌ها را حذف کرده است.
https://www.anthropic.com/claude/sonnet
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6646" target="_blank">📅 22:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puz4bld2yP-hiX6PM7YuhPuK37E8P446VW1C5KhDk_wSvBR9rTswnumm5or16eZeKWfHBmGcYxQ1k_hNnsc6cGTG2GLRVn0JV1cg185f_ZhYwRT0JCOupBN5lJSDfdp32yJbrE8Oh9nad7dmrTd6GD7HacnOE9DqhQUkqIazU3XK5nvtcbA4vT4qVgXDP27fyidVpoM0KVJDiaexfClXSHjAWoev_8SoByXbXj5V7Y0IlZu_IQedagOyA3Q7KrywB0QP1CxEy619o8C8d4yJLfSgN-EJZ7Dx_CbvGEsTcc-3ucUoVD-FwgssNm7Scu7dMQOvrqN3PUbRaSVTuhdNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgLCIre1rKDqKgZUyd3ib1oNBuA2cXXDwLVu8rFnqwlg0gpCsdX6FOOX1qqLDTouUqxRDqQnOlTsIWYycYiGcmvSD58G54LhdNiyuXEhnMKxrAqgtHxoUxobybmddiEMfGmjoem77U02BUHWtxfAy36mw3pPTaNZmXhRbfJCtiNJBbjKs_Sd_W_y8FDe5yNitLkTu7ZcBX9biNsEf9cBAXNZ1BVyxbg-jWHZ2CiZG793BFTbHfuluCSFNzg4qCyH6y8fDkjtrhROoowFfHRVzOp5gSyJwQz_bh0xBwJ78e6psT7y2tc5AZDGH6-WInJvRS-0C4Uav2FRBWbYScH6lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEPCNeH9reSPkQmtgNkz_u_piQl0PljtLal7jAn0Gh9bHjQA5YdMyBLlgjP1piKcBP2NcpRjBcMBmpk9jVJQQC31B85tgP-iYiZsz9HF7jtTpBucjMuuQ9X1PtTp8PIjVf6oFspmfttkMbef2YT3EbnX3SRB_ZVM82gL1vA-6_hlXYRg2PGHz6szMGV1QeWeevjfALUDBtHNesXJYnYWZgY1oQ7OfOs0ZmX2h56QDcKwUFVE548I6uQ0Xx1NUeS368L76WK-IcZrWxu3FrIIkuBUQD89Qq3IDvrRLuXP0YPwCEVk0vHa9-MODOjmcL6oCYscrYKZNSm7FUpj0Aounw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=qXIxV7RHjxGPHz9-151_DSG1yoL1Zrigg17fsYSBpzDDIux-ifWiPfN35DBd2s1IsWJAcy8vDsRyvctL41yBs3lHFTq1cr95BYf2bX6nQyygbXRzF8HQFHeMTNW3pcP6Ff48rIvFsCx5b-DuzHB3GBlcnd1sDrGmxgyi_EX6U6nSAiIqPS4wrg8TjMXITIdfd7KagCvUJqfZJeKzsSmWwiJuMyEB65WMVgZ3L-0b9PJKbePXRERVVZy5k1I9BhGLoQKGbSPDhsYHX6JtpGNbScFlJJ4Cli5jL45LaycsOZ71iky6P7zqis_2bpRRbBEatTqs_HC22v260GiYiCdK1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=qXIxV7RHjxGPHz9-151_DSG1yoL1Zrigg17fsYSBpzDDIux-ifWiPfN35DBd2s1IsWJAcy8vDsRyvctL41yBs3lHFTq1cr95BYf2bX6nQyygbXRzF8HQFHeMTNW3pcP6Ff48rIvFsCx5b-DuzHB3GBlcnd1sDrGmxgyi_EX6U6nSAiIqPS4wrg8TjMXITIdfd7KagCvUJqfZJeKzsSmWwiJuMyEB65WMVgZ3L-0b9PJKbePXRERVVZy5k1I9BhGLoQKGbSPDhsYHX6JtpGNbScFlJJ4Cli5jL45LaycsOZ71iky6P7zqis_2bpRRbBEatTqs_HC22v260GiYiCdK1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💰
تولید محتوا ارزان‌تر می‌شود — گوگل مدل‌های Nano Banana 2 Lite و Omni Flash را معرفی کرد، نسخه‌های سبک‌تر از مدل‌های محبوب خود.
نکات مهم:
؛Nano Banana 2 Lite تصاویر را تقریباً در ۴ ثانیه ایجاد می‌کند و هزینه آن حدود ۰.۰۳۴ دلار برای هر ۱۰۰۰ توکن است.
با وجود قیمت پایین‌تر، مدل کارایی خوبی در زمینه متن دارد، متن را به درستی پردازش می‌کند و نتیجه‌ای با کیفیت و بدون آثار قابل توجه ارائه می‌دهد.
؛Omni Flash مسئول ایجاد و ویرایش ویدئو است. هزینه تولید هر ثانیه حدود ۰.۱۰ دلار است.
از نظر هزینه، Omni Flash در سطح Veo 3.1 Fast قرار دارد، اما کیفیت بصری بسیار قابل قبول است.
ویژگی اصلی — می‌توان مدل‌ها را با هم استفاده کرد: ابتدا تصویر را سریع با Nano Banana 2 Lite ایجاد می‌کنیم و سپس آن را به ویدئو با Omni Flash تبدیل می‌کنیم.
https://deepmind.google/models/gemini-image/flash-lite/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6642" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E56yQ0S4bASkJiF2bWzNwohREIp_ABGGt-ipYEJsR1dTU72-L6GzKvYMHGo2RBGBUSTPkJwJWFsvjAgbuTZ8HUixC5WqCxcyFS-0aPvHfRI07O08h8ni93QbWaPPUibUgLLDcfAGv76MnqTaTZcwZoRVHS89m1pBGJlSrTYidGGuefU1esBJg8kzx_lEGvZ6Qg3WG6MgzNVV-a8RpjwTr2nKGqT8j8XbEB9QpCJ56UCvy2SYf0hTJw5DcAa45r58G1Z1OeZNmWopMa8UK2Ucxt4zdQ7cw7HuyCmcKmwh0yfzdEZJMO2Jm0v-90L4i7hd_F55j8KeeLT5tit0b-s8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی Opus 4.7
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
http://zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6641" target="_blank">📅 20:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=KOG7j7CZ5rczNJfUeaotOgTsaFhht0ZLQxMMilG9RHmDY0hEC9wp48QoPU77SwDWHrehw7yAbax7RK1qoTy2NIoBR6EpDHE9iLvGeoYQNFmGWT8wCyikK4JfDl5nFvCLvJbvSnImBwgTC99zFSEUpF06n6xINdAnWU2IHzywvxzvumzRbeeDIj8XVD09qFRLRp2Jqq-n-I5vkwAnfUcpVOxBZzZ-CEt9NXtTLRmruGpO9d-vOA-iiyY3AM7rT_8xVl1LDjvaXNtC9HjwVR9qJmRp7hSHY4tdc2Wa44OpO_uekOC7ZRfkfEcYBJi9vHpgH4jgbAjrwWClVUj6vmyBOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=KOG7j7CZ5rczNJfUeaotOgTsaFhht0ZLQxMMilG9RHmDY0hEC9wp48QoPU77SwDWHrehw7yAbax7RK1qoTy2NIoBR6EpDHE9iLvGeoYQNFmGWT8wCyikK4JfDl5nFvCLvJbvSnImBwgTC99zFSEUpF06n6xINdAnWU2IHzywvxzvumzRbeeDIj8XVD09qFRLRp2Jqq-n-I5vkwAnfUcpVOxBZzZ-CEt9NXtTLRmruGpO9d-vOA-iiyY3AM7rT_8xVl1LDjvaXNtC9HjwVR9qJmRp7hSHY4tdc2Wa44OpO_uekOC7ZRfkfEcYBJi9vHpgH4jgbAjrwWClVUj6vmyBOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقیقا همین‌طور در سال ۲۰۲۷ رم (RAM) خواهیم خرید — یک پروژه با جاسوسان هوش مصنوعی پیدا کردیم که برای شما اینترنت را زیر نظر خواهند داشت
😋
ایده به این صورت است: شما سایت‌ها یا جستجوهای مورد نظر در گوگل را مشخص می‌کنید و «جاسوس‌ها» در فواصل زمانی مشخص اطلاعات را رصد کرده و گزارش را به ایمیل شما ارسال می‌کنند.
https://github.com/firecrawl/open-scouts
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6640" target="_blank">📅 20:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-heScUubi1oIcCzCJCJAyCjh6Kk8N4aAUj31-9oCUl3CzDjNJfK8p2oXMW3otEqwSkgeuhqru_6wQ9LN7FybMJYERQKgSmTkNIxQjyYXI_UNJh1cSDQ6RceVwToNW1TsKjRAbbTke1FgKfrLQn_im1Rtc_P5KrQ_P223oorDVDiX_hfbcvdetjc7p9XAp4hTf-07zRBf3N8Twk5KW1meHf4FLOQhjjkh3xfMdtArCsA9vGcxd_6OmYzyrR-GUCS_RMG5To_KyKDHXzpotGXSgWvhtfgmAedB2OLDp8ZDjchob_oOpq85r-2wqoP155YvXPMZW1osr8y60H63VHoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DocumindAI
راهکاری برای تحلیل اسناد PDF است.
این ابزار قادر است حجم زیادی از اطلاعات در فایل‌های PDF را تحلیل کند، داده‌های کلیدی را استخراج کرده و رابط کاربری منحصر به فردی برای تعامل با خود سند ارائه دهد. این امکان را فراهم می‌کند تا به صورت تعاملی و مؤثر در سند حرکت کرده، اطلاعات موجود در PDF را درک و استفاده کنید.
https://www.documind.chat/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/6639" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHUvWxuhHi1kuZNXVKjdA1ZgWOQg_tXNDnNGn1G4PgorCWj-T9phzqI5XrogW-fsE9UCmmyjcwLF1B7xenzKbm6ZqktQcMunRbCghGBKin8a7V8uT3XS8YpSNKGC0ElHApm6woV9W2ocx_eP7tYYIeUtPBD5WP4JBkJQE22YqqOQ2eTIH1SMFp8z5JDveeaDipT-Zh04-fH04FSj6a_9I_HzCurRDdNRG3dTsjO8_zWuuMCevIgoqFI91I8jSGin-DlxiFsVpbR5O9UhWaGaX8_cOseASHYviZWEf_0UOt_2KeOGVq826Ni7F9oBExPePVh14DRRcstQOc5ZLVDdlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
نورون‌ها بالاخره دیگر هیچ چیز را فراموش نمی‌کنند — OpenHuman حالت Super Context را دریافت کرده است که بین جلسات، زمینه را حفظ می‌کند و کار را از جایی که متوقف کرده‌اید ادامه می‌دهد.
🔹
در هر بار باز کردن چت، زمینه را به خاطر می‌سپارد.
🔹
مستندات را مطالعه می‌کند، لاگ‌ها را تحلیل می‌کند، ایمیل‌ها را بررسی می‌کند و می‌تواند آنچه روی صفحه نمایش اتفاق می‌افتد را ببیند.
🔹
به طور مستقل اهداف را تعیین می‌کند.
🔹
به ۱۱۸ برنامه متصل می‌شود.
🔹
با سبک کاری شما سازگار می‌شود و به صرفه‌جویی در توکن‌ها کمک می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6638" target="_blank">📅 20:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjAHyihvDtp0QxJ7UI7MjCV8zpfpdWegKowK6iIhSYhmSa1J7pOp3ukhiPmoNue0BXew8ozo_7FR5FSNp8gUAiUqqaQ3nj72mkPwDr2KCf_IA8LThQ4PjmzoqLdp9Bu1psNNeQ8sKUZhPHx1k9hD4BE--3ynYtfrI9q-dKJOEzh6WzPDcJJgLzdeUWF-tF4t6kf6lWKqWZzGC_mQt7UWJD8RiNSh4Siejd7SfIzE7X9rbYESPYM0JqR9wmg_9BW-oj_s51FM6nx7c4SQmOBha4SarHByXu543w1XImLMyiar6fsp8vz_dckRUiuJS7coWojzoaiU3VMXzP9vFCnlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاک کردن واترمارک، افراد، اشیاء مزاحم، متن، برچسب و غیره از تصاویر، با تکمیل خودکار پس‌زمینه توسط AI رایگان
لینک:
https://magicremover.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6637" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4Wj8M02OyItSyPWVOIMFLBzW3ojsLcYZbGsH76NNrHDx2YVcO6Zg5EfcGC8CGWnZMG28Yr6DWFuZ1m2qUAZlj-K4F_c08P87_cvQwVWE3-V-gZFqV32rKEegzmbHNIeI94Ers2LsxVsTcXKHtjJ_jCKXx6O2oOGQWUK0jx6JkV0qlGjbIkB9Qtte6J7cBx64cR4nvXynCTTrubWn225CiPo78NnIkehpJzWNs2g7C34WruOjJhijfn1K5sCJMwTUXbXwVpELljhR0vPwbnl4cHF9cebpkn-AqgKdp88ddgzlucXAhsoKbD62nNX8KgdcParygclEhLKFWslAegJYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
گوگل را دور بزنید! ‌NotebookLM⁩ رایگان و لوکال شد
🚫
☁️
‏نسخه متن‌باز و محلی ‌NotebookLM⁩ منتشر شد؛ دقیقاً همان تجربه قدرتمند گوگل، اما روی سخت‌افزار خودتان و بدون ارسال داده به سرورهای خارجی.
💻
🔒
🔹
چت هوشمند: تحلیل عمیق، خلاصه‌سازی و یافتن تناقضات در اسناد
🧠
‏
🔹
ارجاع دقیق: لینک مستقیم به پاراگراف‌های خاص، بدون جستجوی دستی
🔗
‏
🔹
تولید چندرسانه‌ای: ساخت پادکست، نقشه ذهنی و دوره‌های آموزشی از روی ‌PDF⁩ و ویدیو
🎙️
🗺️
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6636" target="_blank">📅 16:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-7zoBPsL6ZQ_1muaJIz5WlqvCwSoSlNBSwgmrtXTYMqcN9S8tbRhLK-Zb_85CHWFQCviGHhRVV_y4K3LmjXoUMxBWEbz4przmRXnXbpaFIjfqIFHF5F5_9F09_UF7wLpSCZjej-jzdVxBLpUS4xdI730Eqhh9wLodB3NPCAShRtd_ygaCq89K_QuNyrxC2tbCJ6VeaWt5G6EkxxD0WvjXbXJEqbA0Q4Nmq4USsqrnF9K4lWNJdE0yKHHpEbywcF4JPfBKM9Sco5BOfVMGoC9VyVaTvoVsYoLDsrj18G_Cm6dgs7VkDeHDfnOxFnpkrtT3_kvhxdVDpb1pcQExhmNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود فایل از اینترنت با ‌Torlink⁩، سریع‌تر از همیشه
🤯
‏این ابزار خط‌فرمانی، جستجوی فایل را برایت خودکار می‌کند تا بدون دردسر به منابع معتبر دسترسی داشته باشی.
‏
✨
قابلیت‌ها:
‏•
🔹
بررسی هوشمند منابع و یافتن فایل‌های سالم
‏•
⚡
نمایش دقیق حجم و تعداد سیدها
‏•
🛠️
دانلود مستقیم از محیط ترمینال
‏•
📦
متن‌باز و بدون نیاز به ثبت‌نام
‏
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6635" target="_blank">📅 14:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=G2GGc3r7R9AlXp6DGNbJfBc3OS51pp8-CMM79f9k84kLEsuHomuSXaEUwMi2YyBb2Ay_o5eXE7OK86F1xmh9uFsNNVwYKUrznIpybunb7P506sOugapaqAUobWHdtHaUPmiEIpHPG6mdSr9US-r86oP8tP-ZS1PhGRucytw4Y32_nFW-vzoC7dKLo1GC2CYUujudsImR7HoC138-2zFAj9Kgn8uVR64uAAQuP_3zq1Qd4_u3yx2aiEObndD_2x0RcBOsMmQrvZ6LJJSI0B6OwB22orkIokKEHVnEaFRpZK-Ag9aa0xUvMHZ_fThubCuoH1KXOdNKTihwEQBZFDmNeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=G2GGc3r7R9AlXp6DGNbJfBc3OS51pp8-CMM79f9k84kLEsuHomuSXaEUwMi2YyBb2Ay_o5eXE7OK86F1xmh9uFsNNVwYKUrznIpybunb7P506sOugapaqAUobWHdtHaUPmiEIpHPG6mdSr9US-r86oP8tP-ZS1PhGRucytw4Y32_nFW-vzoC7dKLo1GC2CYUujudsImR7HoC138-2zFAj9Kgn8uVR64uAAQuP_3zq1Qd4_u3yx2aiEObndD_2x0RcBOsMmQrvZ6LJJSI0B6OwB22orkIokKEHVnEaFRpZK-Ag9aa0xUvMHZ_fThubCuoH1KXOdNKTihwEQBZFDmNeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل تصمیم گرفته که پشتیبانی از API پلتفرم Tenor، بزرگ‌ترین مخزن انیمیشن‌های GIF در جهان را متوقف کند.
دسترسی مستقیم به کتابخانه عظیم Tenor از تلگرام، دیسکورد، توییتر و سایر شبکه‌های اجتماعی غیرقابل دسترس خواهد بود.
اگر بخواهید یک گیف انتخاب کنید، باید خودتان تصویر را جستجو کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6634" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhdR7EjQxvmOBesL6C8WrXSfqQjcWoY2GjNcEbAvx2BnW7omyFW6_Wr-ZSSofY7Mm0YDU06S2fM4fDr8Cfkj0SbMs7Du2Pw4fkHhMLbOXT9x5hw5V7aFhAe7bNpTt2lJj91c_itOQJFUrXAiDM3dGorLiteL0HCW_qGEKdzK8ReAQ82vtbqm2jNFQqNqoQnFgk5GOB_cyXLcTkCgCxjoUeJlp1qvsVaVa2QtX1cKfNottxqY8e_8QgMznogTQiGIvXNhYDtf9-imDkq1WwHnBggQ2aKFhKDi9Fwe_KEwjq0uaUusSBpypg_V5OO19-NVaoV_ZxaBHFMZJasf7r845w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
غیرفعال کردن ردیابی در مرورگر — راه‌حل ایده‌آل برای کسانی که از جمع‌آوری گسترده داده‌ها خسته شده‌اند و به دنبال حفظ حریم خصوصی واقعی هستند.
افزونه
Fingerprint Detector
در سه حالت کلیدی کار می‌کند:
🔹
شناسایی — نشان می‌دهد که سایت دقیقاً چه اطلاعاتی را از کاربر استخراج می‌کند.
🔹
شبح — داده‌های واقعی را مخفی می‌کند و آن‌ها را با مقادیر «میانگین» جایگزین می‌کند و دسترسی به canvas، audio و WebGL را مسدود می‌کند.
🔹
جعل — رد دیجیتال شما را به طور کامل با یک رد جعلی تولید شده جایگزین می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6633" target="_blank">📅 11:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3Mwfu2YkTfDUkbaEOJDwBq0lR-6UOyTn28rfosGR3vDHOK46nmCr_Fanfp3x0p-v6phsMqsBZiOAElrGN7Z-_kRpgTHw0MnXlwWvCa0aLHHN0w3Q0_XAOAfRCqliPowZZiMqt8oxjMC_TQKTaPR_NHpuN7r4EoUCUFXXNLdDUFGArPhQa3EfuA6Mbbb2Ta0ni019OA9jv6AIuYFUcJ2GIuxrwdbcS1FumZ-EKEGYqbOWCp7fedy-neU_7zbfkyzI0W_0N1bYDEanoCC6BFdtsiHUG2_mVyaootudpu-ziBHkgnY6CXaI4qlubUmkv8EDmrLxePHjbxuIXiI32pOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
هوش مصنوعی بساز، پول دربیار!
‏فکر می‌کنی ساختن هوش مصنوعی فقط مخصوص نوابغ سیلیکون‌ولی است؟
🤔
اشتباه بزرگی است!
‏تصور کن یک جعبه‌ابزار جادویی داری که از صفر مطلق شروع می‌کنی و تا جایی پیش می‌روی که محصولت را به شرکت‌ها می‌فروشی. این دوره دقیقاً همین مسیر را بدون پیچیدگی‌های خشک دانشگاهی به تو نشان می‌دهد.
🛠️
‏
✨
چرا این دوره خاص است؟
🐍
مبانی:
پایتون و ریاضیات را مثل آب خوردن یاد می‌گیری.
‏
🧠
دانشمند:
مدل‌ها را آموزش می‌دهی و بهینه‌سازی (کوانتیزاسیون) را مسلط می‌شوی.
‏
💼
مهندس:
سرویس‌های واقعی می‌سازی و مشتری پیدا می‌کنی.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6632" target="_blank">📅 11:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این هم آموزش راه اندازی</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6631" target="_blank">📅 05:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚀
آپدیت جدید بات تلگرام ما منتشر شد!
✨
بخش جدید
Hugging Face
اضافه شد!
از این به بعد می‌تونید خیلی راحت پروژه‌های خودتون رو از طریق تلگرام دیپلوی کنید:
🔹
فقط کافیه در سایت
huggingface.co
ثبت‌نام کنید
🔹
از طریق بات، توکن خودتون رو دریافت کنید
🔹
پروژه به‌صورت خودکار دیپلوی میشه
🚀
⚡
برخلاف خیلی از گزینه‌های دیگه، این بخش فقط از
سرورهای آمریکا
استفاده می‌کنه.
درسته که سرعتش به پای سرویس‌هایی مثل Render نمی‌رسه، اما در عوض:
✅
حجم بسیار بالا
همچنین در بخش
IP تمیز
می‌تونید این IPها رو اضافه کنید:
🇮🇷
Irancel:
52.214.248.106
32.195.122.200
108.133.38.41
🌐
All net:
amazonaws.com
108.133.38.41
34.196.7.222
3.162.112.2
18.185.80.10
23.162.112.25
2.92.189.25
115.185.114.108
18.138.171.15
135.160.210.199
🔥
تجربه دیپلوی راحت‌تر با
@REN_WZA_BOT
💻
توسعه داده شده توسط
AssA
📌
سورس پروژه
⭐
برای حمایت از پروژه، می‌تونید وارد گیت‌هاب بشید و با دادن Star از ادامه توسعه حمایت کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6630" target="_blank">📅 05:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سورپرایز تو راهه...
Ren panel</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6629" target="_blank">📅 04:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5oolhfKYFAMRNtyId8Ad-2QLRXN-l7rhBlwnDudcnM54dpHXGR4DgkeZDtsQt1Unu-CZdS-Gvyj1LVsMD27WKWmwe-F66ngcPz2iX-7yowERLnS5v28mCJ51OkqD8ACLrcDg-QtKfItsfKdRPDXJHz-brBRiu-mgt4K-GhdA747aSPeg_Vko8QP9PYNSoUltBH0nnWPASvtW5fTEfx1WtB2bD0PMRT1QsdyYeffDN6Xe7Tovuw3sv9BlpU9fnvlsPRk-SgNeClnU_wTMez4zUxN4HWAivWQOIn2tCsKQtBXqyuIFRl2csDhg8_eWwLMy2Ly95YCEqLqU0d0YriORQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واتس‌اپ پس از تقریباً ۱۷ سال از وجود خود، نام‌های کاربری را معرفی کرد — می‌توان بدون شماره تلفن با کاربر شروع به گفتگو کرد.
تلگرام به انقلاب سال واکنش نشان داده است
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/6628" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=VsPEcK4wf7MQCzWgeZC_1XyVVb18HjVTw8TK_7d-Vs8p6jFZFUbZ5YOJLu2KTPdUPHaFDT6wsONOQLnvUCZandzueTHf04tE5mM6SPuKjS_WLTU-N-H49SSQhn0vE2v1q2QfS_TGiNZGBHSLVBonOMaDlCXcD0QrdIofg5No4Z__ZSXPvCgahTyAqpatv6OWiBLfO6UDkae1ZNT5Td_Rig0jmKf1OViI6gef3OhZLfk2qu5UKZPkubJHPwra_m4Xn0oKqIoZMR6gY9gWK-6E_lWLMPBJut5dxGEpvHGr0YyWBoCFKxd46PMyng7sSrFUyTZC-FUfZnjWRM_yCfnl2iLDSKV_BRZUO-Jwys-NH1ea3NNEPpGpw1EOIT9WIXGaCM1UQu8wseAluUJ8dp7d8f-UJ0CWrVocPSxt7rkrLocjPxRGiS89O2K55UQurxp3Jo49-GvUQ0EyoDHcV-ndUih6itTc4oR3oTsD_1HOwRIZLcsVHGFqaUjbGTTGTu64SRO18pDauPhhDf1PuvBS6Uhvi2mD7byDPF72DpXmC3MzyxF7Pwq0oAGaf5E2UdkEBa-q3cq2pZpW6-zCQpNr08y2aPQ8-cgbm1MKlklQLC4q7iNgGCDAfw0VGre5Lf9ntLjZL3znqKhqJ0hWZ8JLVqSKXck_ivfCV8ZNSm-S3yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=VsPEcK4wf7MQCzWgeZC_1XyVVb18HjVTw8TK_7d-Vs8p6jFZFUbZ5YOJLu2KTPdUPHaFDT6wsONOQLnvUCZandzueTHf04tE5mM6SPuKjS_WLTU-N-H49SSQhn0vE2v1q2QfS_TGiNZGBHSLVBonOMaDlCXcD0QrdIofg5No4Z__ZSXPvCgahTyAqpatv6OWiBLfO6UDkae1ZNT5Td_Rig0jmKf1OViI6gef3OhZLfk2qu5UKZPkubJHPwra_m4Xn0oKqIoZMR6gY9gWK-6E_lWLMPBJut5dxGEpvHGr0YyWBoCFKxd46PMyng7sSrFUyTZC-FUfZnjWRM_yCfnl2iLDSKV_BRZUO-Jwys-NH1ea3NNEPpGpw1EOIT9WIXGaCM1UQu8wseAluUJ8dp7d8f-UJ0CWrVocPSxt7rkrLocjPxRGiS89O2K55UQurxp3Jo49-GvUQ0EyoDHcV-ndUih6itTc4oR3oTsD_1HOwRIZLcsVHGFqaUjbGTTGTu64SRO18pDauPhhDf1PuvBS6Uhvi2mD7byDPF72DpXmC3MzyxF7Pwq0oAGaf5E2UdkEBa-q3cq2pZpW6-zCQpNr08y2aPQ8-cgbm1MKlklQLC4q7iNgGCDAfw0VGre5Lf9ntLjZL3znqKhqJ0hWZ8JLVqSKXck_ivfCV8ZNSm-S3yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی با چشم‌درد دیجیتال!
👋
👀
تا حالا شده بعد از چند ساعت کار با لپ‌تاپ، چشمانت بسوزد و احساس کنی  به یک لامپ ۱۰۰۰ وات خیره شدی؟
💡
😫
بیایید روراست باشیم: صفحه نمایش‌های امروزی مثل آینه‌های صیقلی هستند که نور را مستقیم به چشم‌هایت پرتاب می‌کنند. اما تصور کن اگر بتوانی یک لایه نامرئی از «کاغذ واقعی» یا «شیشه مات» روی مانیتورت بکشی. جادوی
Paperman
دقیقاً همین است! این ابزار با تغییر بافت پیکسل‌ها، صفحه نمایش را از حالت آزاردهنده به یک سطح نرم و خوانا تبدیل می‌کند، درست مثل ورق زدن یک کتاب قدیمی و دلنشین.
📖
☕
✅
چرا باید همین الان نصبش کنی؟
•
🧊
حذف بازتاب نور:
صفحه مات می‌شود و دیگر نور چراغ سقف روی مانیتورت نمی‌افتد.
•
🎨
تنوع بافت:
از کاغذ کاهی تا E-Ink (مثل کیندل)، هر سلیقه‌ای را پوشش می‌دهد.
•
🎯
هوشمند و انتخابی:
می‌توانی افکت را فقط برای مرورگر فعال کنی و در فتوشاپ یا بازی‌ها خاموشش کنی.
•
🖥️
همه‌کاره:
هم روی ویندوز و هم مک‌او‌اس به زیبایی کار می‌کند.
به نظرت کدام بافت برای کارهای روزمره‌ات مناسب‌تر است؟ کاغذ کاهی یا شیشه مات؟
👇
💬
🔗
دانلود:
Windows
macOS
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6627" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اولین تریلر Cyberpunk  Edgerunners 2 منتشر شد!
🔥
انتظار داشته باشید که هر ۱۰ قسمت این فصل جدید،
پاییز امسال
پخش شوند.
آماده‌اید برای بازگشت به نایت‌سیتی؟
🏙️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6626" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حدود 900 تا کانفیگ مختلف
📶
https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Germany.txt
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6625" target="_blank">📅 20:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">#اختصاصی
🎧
استودیوی کامل AI: از ایده تا مسترینگ
۱۱ ابزار برای ساخت حرفه‌ای موسیقی:
🎤
تولید: Suno, Udio
🗣️
کلون صدا: Kits AI, Synthesizer V
🎹
سمپل/لوپ: Stable Audio, Splice Create
✂️
جداسازی/ویرایش: LALAL, RipX
🎚️
میکس/مستر: Sonible, iZotope Ozone 11
🔊
پاکسازی: Adobe Enhance
💡
نکته: ترکیب این ابزارها فرآیند تولید را از هفته‌ها به چند ساعت کاهش می‌دهد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6624" target="_blank">📅 17:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaGBqGIVlSIbTnGoy0st2Bc_1TZbZDAc3vo3I8WwgeqaBYmImD-92_gWMWZ4w97k6ffS32laBk5pFF9E98WoHyn8EW6os6NzRCP5jAQxUl0wL4XMq4JNL5BA1wfVHEtBgWCjIRdRB4VO7BuVYuA2lG_yKQDdsJUjF8ixjmllKl4GNRUAPoRmP98JBKLqDlOetIQOaWi7ROm-fyB-U4ehOzwG6LHoebSqbsjCzEPE8LlL573VtXLUKP75M1IjdavFbES7uA_7rocgSkoCkUKxeK624z5QOElc0Dlhbu2a5NoUiETOkPAMTPk1_iwwDrvvsagj_j78mcUSx-s1ca0alw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GTweak؛ جعبه‌ابزار همه‌کاره برای شخصی‌سازی و بهینه‌سازی حرفه‌ای ویندوز!
💻
✨
اگر به دنبال یک ابزار پرتابل (بدون نیاز به نصب) هستید که کنترل کامل سیستم‌عامل ویندوز را به شما بدهد، GTweak یکی از قدرتمندترین گزینه‌هاست. این برنامه با رابط کاربری نوشته…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6623" target="_blank">📅 15:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین   بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .   irm https://get.activated.win | iex   اگر کد به مشکل خورد و اجرا نشد دستور زیر…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6622" target="_blank">📅 15:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین
بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .
irm https://get.activated.win | iex
اگر کد به مشکل خورد و اجرا نشد دستور زیر رو بزنین ( نیاز به ویندوز ۱۰ یا ۱۱ به روز داره )‌
iex (curl.exe -s --doh-url https://1.1.1.1/dns-query https://get.activated.win | Out-String)
Github
😀
📱
@Archivetell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6621" target="_blank">📅 14:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حجم : نامحدود
زمان : تا ۱۲ شب
vless://63b43d54-3bdc-4d9e-b3f3-10163c892936@64.90.7.102:8443?type=ws&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
وصل شدید بگید</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6620" target="_blank">📅 12:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvqjJ11VTYnl_t2zQv_AUy9N8EAAC92prwlaFQJqGQahKP3sSc-Qar2ljCOaepc1kv9y6LRXeP2Aghk5LdWT2dfvOzRYj3aR-gndzOJpv5NZsCTsZmXb_NxY0YOFRLrEav1KKnNw5oZdXvuYRXg-b6FztfJfqpm1MOJfemsvwmeEPgtCzUemV0v8CBpj2x2WB6I_fQLfXqzUbM-eeRzWIKa6wKL2pLPi5c-KJVpTAo_02l3DuNraKLzcFWasquwxv-UDldPneVlX1h6AW9VB17yhmK9S0EJJehhuLurbh_1X73H7bh4XOITPcO3kutHs_c9PMvvQyn5j755Kem2VjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه راه جامع علوم کامپیوتر: ۸۰۰+ منبع از دانشگاه‌های برتر جهان
🎓
اگر می‌خواهی به یک توسعه‌دهنده حرفه‌ای تبدیل شوی، این مخزن گنجینه‌ای از دوره‌های دانشگاه‌های هاروارد، استنفورد، MIT و شیکاگو است.
✨
چرا این لیست؟
•
🏛
منابع معتبر:
دسترسی به دوره‌های دانشگاه‌های تاپ جهان.
•
🤖
پوشش کامل:
از الگوریتم‌ها و زبان‌های برنامه‌نویسی تا هوش مصنوعی و رباتیک.
•
📚
دسته‌بندی هوشمند:
گم نمی‌شوی؛ دقیقاً همان چیزی را که نیاز داری پیدا می‌کنی.
•
🔄
همیشه به‌روز:
نویسندگان مخزن را مداوم آپدیت می‌کنند.
مسیر یادگیری‌ات را از اینجا شروع کن!
👇
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6619" target="_blank">📅 11:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjR7jOr9qo4bBC4vyk10Nztr00bWvyxZcUpY20jZBFtKWdk7deGD_UZezjk45aJbyegBpNqp64inmIQXEVbtYRpIw5Tr4mH377lvaB_SwTBZ082BL_2qYBTOn8-EpCWd46OMiPjB9pM1Kjh_7v2ag0Mh6wQQNKXdqwOV19t_1J3WrYXO7LwJAryWcm3u_9Y477xe0yvCmkf6-y514F7fSrlejnJTezhuQirhhyJIQAFdXc5Imkqv1yItd6CIDrbkDwJkAmkaCRr3ELnNxMwCFy0zPCOs53sjskCDPa6XCvM3gB0L5tA-xLSPV4EpBFhV7C8C9XSKuoWFGiFCpLfhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Anthropic بسیاری از دوره‌های هوش مصنوعی خود را رایگان کرده است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6618" target="_blank">📅 09:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCTELVaUWYtNq72J_k36_pwE1n_Xtgvf6wfDT_i0CxXCSnsDNfpGzvcPZvkms36yiTwF0PZ2rLHNbjV3lVi_lPOJet4-hOadIajSOCFgsmQ1HccokGiOayxnJomcDZby1HdbDXg9vszLCtTmhZ7tWKMD_QovSjBCaSDSFQ3rzw48W371frnKfO2lU2y3YJpElR1npaeV-D4V8Ts_Q_0OLzyMl0PDlZ99WMqRYIyNkjOOSXGzPxDpvTblpX5TOIECTh1-WTLdroB14Ajt2wF0Vh_H-rE60-XVsQccIvsm8pDCiWdWO4ITvlZUUapF3Sv2On88_u0Gci0wVBgMwGnX7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">OmniRoute
۱۶۰+ هوش مصنوعی رایگان در یک API!
🤯
دیگر نگران تمام شدن توکن‌ها نباشید. OmniRoute با ارائه
توکن‌های نامحدود رایگان
، تمام مدل‌های برتر جهان را در یک نقطه جمع کرده است.
✨
چرا OmniRoute؟
•
🔄
تغییر خودکار مدل:
اگر توکن یک مدل تمام شد، بلافاصله به مدل بعدی سوئیچ می‌کند.
•
📉
فشرده‌سازی هوشمند:
تا ۹۵٪ کاهش حجم متن برای صرفه‌جویی بیشتر.
•
🌐
دسترسی جامع:
GLM، Grok، Mistral، DeepSeek، Qwen و... همه در دسترس.
•
🛠
پشتیبانی کامل:
سازگار با MCP و مهارت‌های پیشرفته.
یک API، تمام هوش‌های مصنوعی دنیا. رایگان و بی‌نهایت!
🚀
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6617" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">10 میلیون توکن رایگان هوش مصنوعی Mercury 2
🎁
وقتشه ربات تلگرامیت رو با هوش مصنوعی ارتقا بدی!
✨
✅
مناسب برای ساخت چت‌ بات
✅
دسترسی فوری و رایگان
⚡️
همین الان فعال کن:
🔗
platform.inceptionlabs.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6616" target="_blank">📅 02:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=vuXav1mJ4i35ccWHbIV6ibhqnJpkV1oW4rm3MAayzhFKsF8dyf3WWXy019etwKc1VcMsE_Nw09e1NFTqpHsLLnPLilGhFA0uKKJGrP0TIwiFAdNhECrazyvLUY6gXYZipDMf7di5NfjA6hZacJEwG_A3VEkY7HTFXsJSDg11JJLCFhbTrDIooAVCNohqirCn42QMAD3guCqNegmjgVnrAS7s2tPKzQWJthifBleNLiV79FCNDBKkOF48nlPR2uWGD_ZAEE5FlM_0l3uSA1WNFUyAsLUAYbZYcKYBRpKE06pYmvYLX0C9BlF8wqw1SY3gthK7frEdvgekz3xGz8W7KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=vuXav1mJ4i35ccWHbIV6ibhqnJpkV1oW4rm3MAayzhFKsF8dyf3WWXy019etwKc1VcMsE_Nw09e1NFTqpHsLLnPLilGhFA0uKKJGrP0TIwiFAdNhECrazyvLUY6gXYZipDMf7di5NfjA6hZacJEwG_A3VEkY7HTFXsJSDg11JJLCFhbTrDIooAVCNohqirCn42QMAD3guCqNegmjgVnrAS7s2tPKzQWJthifBleNLiV79FCNDBKkOF48nlPR2uWGD_ZAEE5FlM_0l3uSA1WNFUyAsLUAYbZYcKYBRpKE06pYmvYLX0C9BlF8wqw1SY3gthK7frEdvgekz3xGz8W7KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6615" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده و متن‌باز
PokieTicker
دقیقاً برای شما ساخته شده است!
🔥
این ابزار چگونه کار می‌کند و چه امکاناتی دارد؟
1️⃣
تلفیق اخبار و نمودار:
نقاطی روی نمودار کندل‌استیک ظاهر می‌شوند که نشان‌دهنده اخبار منتشر شده در آن روز هستند. با کلیک روی هر نقطه، متوجه می‌شوید چه خبری باعث آن نوسان شده است.
2️⃣
فیلتر هوشمند اخبار:
دسته‌بندی اخبار بر اساس تأثیرات مختلف (گزارش درآمد، تغییرات مدیریتی، محصولات جدید، سیاست‌گذاری و...).
3️⃣
تحلیل و پیش‌بینی با هوش مصنوعی:
با استفاده از مدل‌های قدرتمند
XGBoost
و
Claude
، سنتیمنت (احساسات) اخبار را تحلیل کرده و روند قیمتی سهم را برای روزهای آینده (T+1, T+3, T+5) پیش‌بینی می‌کند!
4️⃣
کشف الگوهای مشابه:
روزهای گذشته که اخبار و شرایط مشابهی داشتند را پیدا می‌کند تا ببینید در آن زمان بازار چه واکنشی نشان داده بود.
5️⃣
رایگان و آماده استفاده:
دیتابیس لوکال (SQLite) از قبل در مخزن گیت‌هاب قرار دارد و برای اجرای اولیه نیازی به خرید API کلیدهای پولی ندارید.
﻿
⚡️
مشخصات فنی:
*
بک‌اند:
Python (FastAPI) + SQLite
*
فرانت‌اند:
React + TypeScript + D3.js
*
مدل‌های AI/ML مورد استفاده:
XGBoost, Claude Haiku / Sonnet
﻿
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6614" target="_blank">📅 00:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6613">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=FL8aB9LzoYb-umNdooSyZNL63Qu9Ls8qBNS01KKVk14uSDB-4JftAfLaQfnwWzn4AUhJFF_N7Ji0b62nEmy827tR_ksvcxRMkftfgttH7D1BvMWnI2MMZKMnX5_aHsaRXwd38l3B6jGHcrIv61JUzcn-dvj1VMQJcp3YVwpucDD2pVNLssnhAshMNB0MO3cOsSUNgP_fmYBPgzfDkfD1_tD7K-KAzNjTZurxdXfYorhIlBOkuZ1eZtcHMwdjb6ndJkIi8AkHiJ6ny-9fqYJjLIlGavsEiKEDqSSK1OONluqzc3T4UuUTqvSdTQSBrqDBgywjdwAeZxwgzMxiL_lgrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=FL8aB9LzoYb-umNdooSyZNL63Qu9Ls8qBNS01KKVk14uSDB-4JftAfLaQfnwWzn4AUhJFF_N7Ji0b62nEmy827tR_ksvcxRMkftfgttH7D1BvMWnI2MMZKMnX5_aHsaRXwd38l3B6jGHcrIv61JUzcn-dvj1VMQJcp3YVwpucDD2pVNLssnhAshMNB0MO3cOsSUNgP_fmYBPgzfDkfD1_tD7K-KAzNjTZurxdXfYorhIlBOkuZ1eZtcHMwdjb6ndJkIi8AkHiJ6ny-9fqYJjLIlGavsEiKEDqSSK1OONluqzc3T4UuUTqvSdTQSBrqDBgywjdwAeZxwgzMxiL_lgrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">DewatermarkAI
حذف واترمارک با هوش مصنوعی در مرورگر
این سرویس رایگان واترمارک‌ها را از عکس‌ها حذف می‌کند و فایل آماده را می‌توان با وضوح اصلی دانلود کرد.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6613" target="_blank">📅 00:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qs9vOQxL74E-fqiInzazasW20QE3OcCg6O4ixhOjt3ynhZUdI2iI2aVb6HiYLt_fqp9wRub_Xf6irhSkkeFepynrUL25SUdyBDtu95DTwWw5zTlqujr3aebOm9KEjcCXTJ-TFXU4cFj_I2mn1tG_B4Ps-aV54X0rQZronM-MiNVF5IjqkLpRZZ8v_Hh5UcgnW-T_ZO0ZJKOJxsxqLrS-JxjFzw-sa_CSuGHIIsapR-_TURiglGTxoOnLi2nPKVCT1I_yJi5DXFD-XIYD7oJ6Yflhv1nWpIFK_pp39nc7zPVf73og5vyhhklPR9UsNDo0thngvp0_zYuSnUO5ptZBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از به‌هم‌ریختگی اسکرین‌شات‌ها خسته شده‌اید؟ Trickle دستیار جدید هوش مصنوعی است که همه اسکرین‌شات‌های شما را به‌طور منظم سازماندهی و خلاصه می‌کند
فقط یک اسکرین‌شات بگیرید و آن را به Trickle ارسال کنید. هوش مصنوعی پیشرفته Trickle یک خلاصه دقیق تولید می‌کند که اطلاعات کلیدی مانند متن، نمودارها و یادداشت‌های دست‌نویس را استخراج می‌کند و سپس می‌توانید این داده‌ها را جستجو و درخواست کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6612" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJBpsxbnWZ9dKp_EzIOtenGo7O0CY7PVkTyJPf0zcJABturzaX_mZhsePe0Ge3VTm5znYxFDeDXZixVoEzGPCD2bK3Dw79_JtHehdB_0E_LFnJyKG43XgwdD2QOMj7kMFnaFqdC5Jl0QUFgF7xIlC2KHXR_DpOrKBMjNjdtXJCaxuLHQcRdZR5XJVBkvgr3Qec4Yk4xCTwbFN3bKRgEIaowsmpbzv9pqQ5sbVC8kqGwSTZk7VdJ9yCGZn0usNwicS0nI98Jl3PjGeAXbnfL_rbpDwSLvgmTwKc7c97GFY48kWNcrH2gctKClmIFk0x8wOkHn9rcfWXm-Kk1tea__Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
شورای خردمندان هوش مصنوعی: تصمیم‌گیری با قدرت ۱۸ متخصص
آیا از پاسخ‌های ساده و تکراری هوش مصنوعی خسته شده‌اید؟ با این ابزار، مسئله خود را به شورای مجازی فیلسوفان، دانشمندان و مهندسان بسپارید و تحلیلی عمیق و چندجانبه دریافت کنید.
➖
مناظره کامل بین ۱۸ کارشناس مجازی (سقراط، ارسطو، سون‌تزو، آندری کارپاتی و...)
➖
بررسی مسئله از زوایای مختلف فکری و تخصصی
➖
ارائه راه‌حل‌ها همراه با نقد و رد استدلال‌های رقیب
➖
دریافت نتیجه‌گیری نهایی بر اساس جمع‌بندی بحث‌ها
➖
تحلیل واقعی به جای پاسخ‌های کلیشه‌ای
این ابزار برای تصمیم‌گیری‌های پیچیده و نیاز به دیدگاه‌های متنوع، گزینه‌ای بی‌نظیر است.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6611" target="_blank">📅 21:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHryxq_BXj8F2fEXZLXfZlaWAYk8cn7kfQ91_ORPfmsv3JrGsZrCWmomZuwAOrh8hflThvryIbZHqdTcUabtOsfkVKPksPO41wWkDzFoNOfKOr9kwYKuOWhQ1B6wNz9VKoeoJtZv7IpUzCs779lR73dt-u9H9LS8ezSv8HsVZ_DWJbjcR3rQwFMZNH59sHdCHkIMtB8QQRryu7m25Hr6DijwXSmCeCwW8t3S1DJCyb-wwhrj7BLi1S-5vxDR_Qqn7oi0CnLN4Wuac2n1azgaWy42GXJG3vck0lbojpafr2jpnmYrcHyYIMhpfpj6ClWG574vgsx7KELc56o8bvieng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
OFPlayer: پخش‌کننده موسیقی محلی و حرفه‌ای
➖
پشتیبانی کامل از فرمت‌های FLAC و MP3
➖
مدیریت آسان کتابخانه و لیست‌های پخش
➖
نمایش متن ترانه (Lyrics) و کاور آلبوم
➖
تحلیل دقیق فراداده‌های صوتی
➖
اتصال به سرویس‌های WebDAV، Subsonic و Navidrome
➖
رابط کاربری ساده، رایگان و بدون نیاز به ثبت‌نام
این پخش‌کننده برای کاربران NAS و کسانی که مجموعه موسیقی شخصی دارند، بسیار مناسب است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6610" target="_blank">📅 21:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQJSm4pjjLnz5j4KFGx8tTZnaRlpq1ya4DjuJREaNTOg47euWxlpE2yRCjSDFQMJbZ_E_mJlvgBTjSMezgJNRCwA4tGZS4RxMdb2l7dQYIA5nxAEGGmeOsWwwpID_IUHrqNS4iVGmg4UHw6F8jFSoiTvfmeuR5yAyUz5s0mLPD3EwFbj0h0oeO30cyW7IHjnUIv9CJ4QHit75CKeRk25pRby-7qk1uXxTaNJBIrxEf8CQ3eJMa_g0mM2xj1lqZAy3ElenEo71R_yZA81a_OmZkxtKtDgVO9abFLgyk__IrNKYPLsAiYjdw1bKb_FFKp744eeiRYM8ZynDfKjlT6UEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏋️‍♂️
مخزن کد با ۱۳۲۴ تمرین برای اپلیکیشن فیتنس!
اگه میخوای اپلیکیشن فیتنس خودت رو بسازی، این گنجینه رو از دست نده:
• ۱۳۲۴ تمرین کامل
• انیمیشن‌ها و تصاویر باکیفیت
• جزئیات عضلات درگیر و تجهیزات مورد نیاز
• دستورالعمل‌های گام‌به‌گام حرفه‌ای‌
پروژه خودت رو با این داده‌های غنی شروع کن!
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6609" target="_blank">📅 19:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خب Claude Fable هم استفادش برای مردم عادی کنسل شد
چینیا هم دارن مدرک جعلی میسازن تا بتونن ازش استفاده کنن
😂</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6608" target="_blank">📅 19:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚀
تبدیل جادویی اسناد پیچیده به Markdown خالص با MinerU!
📄
✨
اگر برای استخراج متن، جداول و فرمول‌ها از فایل‌های درهم‌ریخته و پیچیده مشکل دارید، ابزار متن‌باز
MinerU
دقیقاً همان چیزی است که نیاز دارید! این پروژه فوق‌العاده که با استقبال بی‌نظیری روبرو شده و بیش از ۷۰ هزار ستاره در گیت‌هاب دریافت کرده است، اسناد شما را به راحتی و با بالاترین دقت به فرمت تمیز Markdown تبدیل می‌کند.
🔥
ویژگی‌های برجسته این ابزار:
1️⃣
پشتیبانی از فرمت‌های متنوع:
توانایی پردازش و تبدیل فایل‌های PDF، DOCX، PPTX، XLSX، تصاویر و حتی صفحات وب.
2️⃣
استخراج دقیق جزئیات:
بیرون کشیدن بی‌نقص متن‌ها، جداول و فرمول‌های پیچیده (ریاضی و علمی) از دل اسناد.
3️⃣
پشتیبانی از ۱۰۹ زبان:
قابلیت تشخیص و پردازش بی‌نظیر اسناد در اکثر زبان‌های دنیا.
4️⃣
کاملاً رایگان و متن‌باز:
یک پروژه Open Source قدرتمند و بدون هیچ‌گونه محدودیت پرداخت یا نیاز به سرویس‌های ابری پولی.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6607" target="_blank">📅 18:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7tPlQWO5GCKmvVupK0ndzoVluWeygI0sqGucPOKbiZ43O9VO7Pvlb4xb3XHRcIjBHA3wKjsXMXMsPTLybCxdBgC7ax2fvahB0Mh3tDnhTUEOWC1H7kHnnDe60w6S18yMBlQd4QosDYlw3F1Xeog2oHMNJRC7Cz-gvPoxmyv96hZm4WX6-nC1tncQdKjRZtSvj5FBBPjGpndnYazWPD4dhI2kFFvn2c-JxPv3-WQWSiCMqPhLLFDSpznfaDVP5Yu3PfEStKD-M-zTb4Upl-F5Z-Ju6RDM7-h627_eLY3_baODitIEcjUQ5o3wtYFLgFe0CaADeri61K0nIfyL_AYSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها ElevenLabs را کشتند!
💀
توسعه‌دهندگان ByteDance نسخه SeedAudio 1.0 را عرضه کردند که هر نوع گفتار و افکت صوتی را کلون و تولید می‌کند.
1⃣
ایجاد گفتگو با چندین شخصیت: هر شخصیت متمایز است، دارای احساسات، سرعت، تمبر و حتی لهجه منحصر به فرد؛
2⃣
دریافت تا سه منبع برای کپی کامل صدا، احساسات و سبک؛
3⃣
تولید صداها بر اساس پرامپت، مرجع صوتی یا حتی تصویر.
آیا این پایان دوران انحصار ElevenLabs است؟
🤔
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6606" target="_blank">📅 16:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDPWTwwOlSVW5V5ZA26B-8uGJmMJyjydHqDjObGlLAOMfAY_HNo1W3aeY2rsr5XxVbGlKYhC2YPRjM7BLDlSnRR_TDMpjbywJUUog3aFjHTExltS_0txV2AaZ5csK7ihwciIeTcdsuZ3PlBF1w4A0PcJPoxljg6_oh9VtecJU4H6TQFZIQbiGBWZ098-nnSbJqArFA0c3g-HPRxR1JWe3Y5hwtvMuvv1rPmEQviWMMEPAdBxYz2sYTBreaBcY-t9RWCYm4hjxigmYYnmvS_DN1l0krYTd1tQ0V4Xam_YU6ICTwv3BrsY2lTZvGUHSjbcxwsBvY26VMh6sMvt76Ey6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
تولید رابط‌های کاربری زیبا با پرامپت‌های آماده
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6605" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
معرفی IstanPdf؛ ابزار قدرتمند و آفلاین برای مدیریت فایل‌های PDF و DOCX!
📄
✨
اگر از سایت‌های پولی، تبلیغات آزاردهنده و محدودیت‌های سرویس‌های آنلاین تبدیل فرمت خسته شده‌اید، اپلیکیشن
IstanPdf
دقیقاً همان چیزی است که نیاز دارید. این ابزار کاملاً آفلاین توسعه یافته تا جایگزینی بی‌نقص و رایگان برای سرویس‌های پولی (Freemium) باشد. در این اپلیکیشن حریم خصوصی شما در بالاترین سطح قرار دارد و هیچ فایلی از گوشی شما خارج نمی‌شود!
🔥
امکانات فوق‌العاده IstanPdf (نسخه v1.0):
1️⃣
ابزارهای حرفه‌ای PDF:
*
Merge:
ترکیب و چسباندن چندین فایل PDF به یکدیگر.
*
Split:
استخراج صفحات دلخواه با تعیین محدوده صفحات.
*
Remove & Reorder:
حذف صفحات اضافی و تغییر ترتیب صفحات یک فایل.
2️⃣
تبدیل فرمت (Conversions):
* تبدیل یک یا چند تصویر به یک فایل PDF یکپارچه.
* استخراج صفحات PDF و ذخیره آن‌ها به عنوان عکس.
3️⃣
ابزارهای کاربردی DOCX:
امکان حذف صفحات خاص و تغییر چیدمان و ترتیب صفحات در اسناد ورد.
4️⃣
حریم خصوصی و امنیت مطلق:
کاملاً آفلاین، بدون نیاز به ساخت حساب کاربری، بدون محدودیت حجم و آپلود، و فاقد هرگونه تبلیغات و پرداخت درون‌برنامه‌ای.
🔗
دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6604" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uarZM6Xa9DIrcDku7PRk7AKiM-BSsxeQ25XIRlwLCEJ72hgvDnZcTYb_9kyOeEUlt6J2M4tjj7S6ojk70PtxyJcwHti6_ncq2qENrF5TlyC7wunq3wOdq8vAclkEY7X87agIaEIcJpoxKtW8Z56oLvBSLX1kgWHhyWdChWPw71ru4Xb9vPNWkKdIMQkCMBEq0hM85lesSzH9IX802m9hGwqgdIogbu63Cktu5MdhcHlKlLbjkrtL5fqPqd5_RmKXHCcoHMeDLhO2GMRcBohP7tQ7XPMK6LH4yt3fauIzkG8_nQYE7aDkE0aJRtlwPRhm1aT_x3br25VHrK4iPjOvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها:
•
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه
•
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان
•
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب
•
📝
فقط پرامپت بنویسید و کد آماده دریافت کنید
🌐
Site
#AI
#Coding
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6603" target="_blank">📅 11:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=CiYEXBSJR1OkL7PWweX-rJlc8_opIhz2OUzMGqB7Wwh3IklPVDdURbLuv9-NwZqLietC_T2QUjAuf9Y20_7NY_xIZUi6rLZREgbkwisf4wbuFPJP2AKrTjSXF6MruL00Da4CCOSsMHRhrsluNs00vxQVIWsMtp-h6m3AT5PzlIsh_Z-d-uMCxdeqOdtZf7qFtDKibEZ1rkjaVxKOOdQ41W3jD1Wfudi5jl_djoInOVX7STHMLlcZhO81ka44UuYhEy3pbJKGMzopbM8WD7dDD8i7Tha3HAmuGLqYBlKsxGk2CfimxtIi8-dUtXi5B9hx3kQRDZmLc32iW0LnlqK72Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=CiYEXBSJR1OkL7PWweX-rJlc8_opIhz2OUzMGqB7Wwh3IklPVDdURbLuv9-NwZqLietC_T2QUjAuf9Y20_7NY_xIZUi6rLZREgbkwisf4wbuFPJP2AKrTjSXF6MruL00Da4CCOSsMHRhrsluNs00vxQVIWsMtp-h6m3AT5PzlIsh_Z-d-uMCxdeqOdtZf7qFtDKibEZ1rkjaVxKOOdQ41W3jD1Wfudi5jl_djoInOVX7STHMLlcZhO81ka44UuYhEy3pbJKGMzopbM8WD7dDD8i7Tha3HAmuGLqYBlKsxGk2CfimxtIi8-dUtXi5B9hx3kQRDZmLc32iW0LnlqK72Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🔥
🔥
هر نوع رسانه‌ای را از تلگرام و حتی چت‌های خصوصی دانلود کنید
🤯
• دانلود صوت، پیام‌های صوتی، ویدئو، GIF از چت‌ها، استوری‌ها و حتی چت‌های خصوصی که دانلود در آن‌ها ممنوع است.
• پشتیبانی از دانلودهای چندگانه بدون کاهش سرعت.
• قوانین تلگرام را نقض نمی‌کند، می‌توانید با خیال راحت استفاده کنید.
🌐
GitHub
#Telegram
#Tools
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/6600" target="_blank">📅 08:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دریافت 7 میلیون توکن روزانه AI به صورت رایگان!
🎁
🤖
مدل‌های موجود:
• Mimo 2.5 Pro
• Mimo 2.5
• Mistral Large
• Mistral Medium 3.5
💻
کاربرد:
• ساخت وب‌ سایت
🌐
• ساخت ربات تلگرامی
🤖
• کدنویسی در ترمینال
⚙️
🔗
NaraRouter
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6599" target="_blank">📅 01:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Metapi؛ هاب هوشمند و همه‌کاره برای مدیریت APIهای هوش مصنوعی!
🤖
✨
اگر برای دسترسی به مدل‌های هوش مصنوعی در سایت‌های مختلفی ثبت‌نام کرده‌اید، حتماً می‌دانید مدیریت ده‌ها API Key، چک کردن مداوم موجودی و تغییر دستی تنظیمات هنگام قطعی یک سرور چقدر کلافه‌کننده است. پروژه متن‌باز
Metapi
توسعه یافته تا به عنوان «پروکسیِ پروکسی‌ها» تمام این مشکلات را حل کند!
🔥
امکانات و ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
تجمیع تمام APIها (Aggregation):
شما ده‌ها کلید مختلف را به Metapi می‌دهید و این ابزار به شما
فقط یک API Key و یک Base URL واحد
می‌دهد. حالا می‌توانید این کلید واحد را در تمام برنامه‌های خود (مثل Open WebUI، Claude Code یا Cherry Studio) قرار دهید.
2️⃣
مسیریابی هوشمند (Smart Routing):
اگر سرور یکی از ارائه‌دهنده‌ها قطع شود یا مدل خاصی در آن گران باشد، به صورت خودکار درخواست شما را به یک سرور جایگزین، سالم‌تر و ارزان‌تر می‌فرستد (بدون اینکه شما متوجه قطعی شوید!).
3️⃣
دریافت اعتبار خودکار (Auto Check-in):
به صورت زمان‌بندی‌شده در سایت‌هایی که سهمیه رایگان روزانه می‌دهند لاگین کرده و اعتبار شما را به‌طور خودکار جمع‌آوری می‌کند.
4️⃣
حریم خصوصی ۱۰۰٪ و نصب آسان:
به راحتی با داکر (Docker) روی سرور یا سیستم شخصی شما نصب می‌شود و تمام داده‌ها فقط در دیتابیس محلی (SQLite) خودتان ذخیره می‌مانند.
5️⃣
سیستم هشدار پیشرفته:
در صورت بروز قطعی یا اتمام موجودی، از طریق تلگرام و ایمیل (SMTP) به شما نوتیفیکیشن می‌دهد.
⚡️
برخلاف پروژه‌های مشابه که برای تیم‌ها و فروش API طراحی شده‌اند، Metapi کاملاً برای
استفاده شخصی
بهینه‌سازی شده و رابط کاربری بسیار سبک و تمیزی دارد.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#API
#Metapi
#OpenSource
#Github
#SelfHosted
#Docker
#Tools
#OpenWebUI
#LLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6598" target="_blank">📅 01:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Awesome Android Root؛ گنجینه‌ای بی‌نظیر برای روت و شخصی‌سازی اندروید!
📱
✨
اگر به دنیای روت، کاستوم رام‌ها و دستکاری عمیق سیستم‌عامل اندروید علاقه‌مند هستید، مخزن
Awesome Android Root
یک دایرکتوری جامع و بی‌نظیر است که بیش از ۴۰۰ ابزار، اپلیکیشن و ماژول مخصوص دستگاه‌های روت‌شده را به همراه آموزش‌های دقیق در یک‌جا جمع‌آوری کرده است.
🔥
امکانات و ویژگی‌های کلیدی این لیست:
1️⃣
آموزش‌های قدم‌به‌قدم:
راهنماهای کامل و دقیق برای آنلاک کردن بوت‌لودر (Bootloader Unlocking) و نصب کاستوم ریکاوری‌ها (Custom Recovery).
2️⃣
پشتیبانی از جدیدترین متدهای روت:
پوشش کامل و معرفی ابزارها برای روش‌های مدرن روت سیستم از جمله
Magisk
،
KernelSU
و
APatch
.
3️⃣
کالکشن گلچین‌شده ماژول‌ها:
مجموعه‌ای از بهترین و کاربردی‌ترین ابزارها برای مسدودسازی تبلیغات (Ad-blocking) در سطح سیستم، اتوماسیون وظایف و شخصی‌سازی عمیق رابط کاربری اندروید.
⚡️
مشخصات فنی:
*
زبان:
Python (برای مدیریت و استخراج داده‌های لیست)
*
پلتفرم:
Android
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#Root
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6597" target="_blank">📅 20:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سلام
دوستان اگر به وایب کدینگ علاقه دارید یه نگاهی به این سایت بندازید:
https://risman.pro
برای ساخت محصولات فنی میتونه خیلی کمکتون کنه. (بدون نیاز به هیچ دانش نرم‌افزاری و برنامه‌نویسی)
امکان انتشار در دامنه خودتون هم بهتون میده.
با اولین لاگین حدود ۱۰۰ هزار تومان توکن هدیه میگیرید و اگر خواستید توکن بیشتری مصرف کنید میتونید از کد تخفیف welcome برای ۵۰% تخفیف تا سقف ۱ میلیون تومان استفاده کنید.</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6596" target="_blank">📅 19:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMXjJQL0WUkjfBNfd17mi1YkBVlmOlf2rEUgxsHAeM49KB8j_Y3mGX8unhReM8BBcuAd4gHtap8of9-Q3BQGP6jVnCFymp1fO8QMAObtXJ_TpwQ9acBieqCbAS4kdLSXTj08ZNexuhGMTGXVDrSkFjAOI9YkhmsYVHhlaWsB1mLcmBgKc_Vy9s-CDNlp1NMheZRSf6pIbSUbvTITninA_N06y4mi775r79T05_ZSaEQreiUrKvs1-mKfOLWHzTkRUIfjeV_QLa_kq0kk0cbja93Hgg61qBxsv4WryhqyLIHXCMrYH7yM67jj4xarKPmn3Ol6GesOeTC0lEGtLYIfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابلیت ست کردن پراکسی لوکال
خیلیم ساده
مرورگر باحالیه
🔥</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6593" target="_blank">📅 15:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn14bRN-vGLUMcpX8sGekuUhDGKZUlZgOBlY6ddLCR7AeBZPjcDCidaCm04J8PSoUJ0UQnRcE9hU9oHXMGUX-Bfz3gGqA1yd91XpBfoucWH0i5Y_lSC2Y17Ys8abaEaU9J9rzI83iKcr_VPC-OIbNMjHoSS0_uD9-W90iJ5zEksBafllUgthqb6OSBnXas9usYY5YZYAdOetMLWSq8AOYcxCjHqJxMTxepk-hcRAirYJEW48mGLK7W-sBuryQqDO5O0fjJ430oANdX9xBsItzo8J2oO8FGWdJXlGRWB59Ta83_5jvCLo_I81ZrGJX6VwFxxPf2UPqVirqMZcB4vI0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن Solipsism یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی…</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6591" target="_blank">📅 15:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن
Solipsism
یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی با ایده خلاقانه "Rail-first" تمام کنترل‌ها و نوار آدرس را به جای بالا یا پایین، در یک نوار کناری (سمت چپ یا راست) قرار می‌دهد تا کار با گوشی‌های بزرگ با یک دست بسیار راحت‌تر شود.
🔥
ویژگی‌های شگفت‌انگیز این مرورگر:
1️⃣
طراحی نوآورانه (Rail-first):
قرارگیری منوها در نوار کناری با قابلیت تنظیم اندازه (از کوچک تا Super Compact) متناسب با اندازه دست و صفحه نمایش شما.
2️⃣
زبان طراحی Material 3:
رابط کاربری بسیار زیبا با گوشه‌های گرد، انیمیشن‌های روان، سایه‌ها و قابلیت هماهنگ‌سازی رنگ‌ها با تم سیستم‌عامل اندروید.
3️⃣
ابزارهای قدرتمند حریم خصوصی:
دارای مسدودکننده تبلیغات (Ad Blocker)، وب‌گردی ناشناس، کنترل کوکی‌ها و WebRTC، پاک کردن خودکار داده‌ها هنگام خروج، و یک قابلیت بی‌نظیر به نام
Decoy Mode
(تولید تاریخچه وب‌گردی جعلی برای محافظت از حریم خصوصی!).
4️⃣
امکانات کاربردی و سریع:
دارای اسکنر QR داخلی، قابلیت نصب مستقیم وب‌سایت‌ها به عنوان اپلیکیشن (PWA)، پخش تمام‌صفحه و بدون مزاحمت ویدیوها و ابزار دانلود حرفه‌ای.
5️⃣
صفحه خانگی شخصی‌سازی‌شده:
امکان تغییر والپیپر هوم‌پیج یا تنظیم آن روی حالت کاملاً تاریک و بی‌صدا.
﻿
⚡️
این مرورگر سبک که بر پایه WebView اندروید ساخته شده، تجربه‌ای کاملاً متفاوت، سریع و مدرن از وب‌گردی را به شما ارائه می‌دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Solipsism
#Android
#Browser
#Privacy
#Material3
#AdBlocker
#WebDevelopment
#MobileApp
#TechTools
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6590" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚀
هوش مصنوعی دیگر کدهای شما را فراموش نمی‌کند؛ دستیار حافظه دائمی برای ایجنت‌های برنامه‌نویسی!
🧠
✨
اگر از پریدن کانتکست (Context) در چت با هوش مصنوعی و توضیح دادن‌های تکراری خسته شده‌اید، این ابزار جدید مشکل شما را حل می‌کند! به تازگی یک دستیار هوشمند برای مدل‌هایی مثل Claude، Codex و Cursor منتشر شده که دانش و اطلاعات پروژه شما را بین سشن‌های (Sessions) کاری مختلف حفظ می‌کند.
🔥
این دستیار چه کارهایی انجام می‌دهد؟
1️⃣
حفظ همیشگی کانتکست:
اطلاعات جلسات کاری شما را ذخیره می‌کند تا با بستن پنجره، کدهای شما فراموش نشوند.
2️⃣
یادگیری ساختار پروژه:
معماری، دایرکتوری‌ها و ویژگی‌های خاص کدبیس (Codebase) شما را کاملاً به خاطر می‌سپارد.
3️⃣
بسته‌بندی خودکار دانش:
اطلاعات جمع‌آوری‌شده را به صورت خودکار و هوشمند بایگانی و بهینه‌سازی می‌کند.
4️⃣
بازخوانی در کسری از ثانیه:
هر زمان که ایجنت به اطلاعات قدیمی نیاز داشته باشد، در کمتر از یک ثانیه آن را فراخوانی می‌کند.
5️⃣
پشتیبانی بسیار گسترده:
سازگاری کامل با
Claude Code
،
Cursor
،
Codex
،
LangGraph
،
CrewAI
و سایر ایجنت‌های هوش مصنوعی.
🔗
لینک دریافت و راه‌اندازی پروژه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#CodingAgents
#Claude
#Cursor
#Codex
#LLM
#Memory
#ProgrammingTools
#DevTools</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6589" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6jaCyLO6oPvZG8Cj9nEZerlxy77PB9-huQFftrGU2orIx5Us2dj753OKtzHS1EGDrpgTBAbrIlcgv_mUObqIKAss3vcZSH0uuZNIzSJnNerAIrxwB2jm9-HprkysBMiREdM636zKoHsZxVf7sXpq37YbHS2PSLNAtZGWW9qU0CTEQV9nBP-vxtN7GACx1T6b2uq8YJuVusaXziO4AR_KdJOVCIl9KBXZ63IbUzSmKJKA_fASoVMj5V1sdQou6tb6Rik6mFLT1eQenY5I7kOzN0eWGas1jffolNGKJ8Du9qyECbHWJJ7hSgN47ofuuv1-BUyjqYnjwbIggm1ZjqTrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 1T کانفیگ شخصی
🔑
🟢
از لینک زیر میتونین شروع به ساخت اکانت کنید :
➡️
sign up
بعد از ثبت نام وارد اکانت بشید و روی
Quick Subscription
کلیک کنید و داخل اپ هایی مثل :
Nekobox,hiddify,singbox و ...
اکسپورت کنین .
به دلیل نوع پروتکل یعنی AnyTls بودن فقط داخل اپ های ذکر شده میتونین اکسپورت کنین و داخل اپ هایی مثل V2ray کار نمیکنن
😬
خط های تست شده :
🛜
🛜
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/6588" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMwJTjY7m8obMQUlP9l4V8eY1g3vN2gvE33nPLulgMk-Bf2NYYFMP9emwi2THcQ47n07PPNTdVxoekS7EUAmMsX-CgxKG613_u_MnW1a4cadEKM9rPDmIqUtGDxXO24ngbe5NVcShQg-8rRmsep2RFPyULpY0ljgap2vikuOGxS6tzKmlfu-ZgAWkoBm4_r7ogZX7PEHoNTSYMnx6airXJUPY-JLlobE0zuIXeWegMGFEbm4y2DAHCRMN0Z9eaJ_ECtj1CCj-k-ReYmT87QcrzZm4zrHYTqw-rqzPfP49BNGjsqIGuvxQyOoWSYPqTmCW-qSoBEAG4cs1cI6Xd95nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6oiNVGBjjjCm_kGqtxuFZlkG0AY5CzIuyYMutr0pF_eoqJNBmL-BJmJ12XGo-_IeFUHJj-6HIIY-jzok5VbPDNVaHq_IxU5TXM--n5ens7sRicTGAsWKLF1_vTpuMRyx-Z9dbpFQ1BVJPN-iyDmhwFCb5aSDs0Ok0bT-KEI5TnHIiLH_Q8aWUJz8kCTMxsJEPV9RJvIuDntRA9NZaLJMvxP8knuKAKBG8W5yX56eBTr3XvR_55oD7xKZtU6AwmkW837N7KPQ47wiKwZnqrKCFFG4FIeRXpyU4nbezAffQdPbU-FejDtArfYzakQHw0sGWhGDTIm_TQNBpELqeC2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZRJ9hhQpvcHZFfAk9ZRUsn9LaGRz8Qdm1Zw03nBUXkNZB_PyKZxycKoZeev7ZRf7W65J6fgcfuHEh6O0fvhOCObKiZAutr72q-glBX2AMqIOU9mS6YnhGwr8slh3ctCvIqiVYNkVB5BAbpzk9NhBQtLbSs5-8YKQHzOUaqlseIZkubTLGifQuCjJjETZjhXbd9qYgvRnIhhEpK4cB4olISEBRubO-tkGbTtaHQz_QllMg4iCHr-4QLsbyE_0PKOMI-DjeIDa-WoXuqslc9CKQa7VIUNwzdbT34bOUC1iV9w93XCEwt5MW9URtIOF8hiwOXe0Ryk1tm5XXD9T9WiAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبدیل عکس‌های معمولی به شاهکارهای هنری با هوش مصنوعی
🔥
✨
قابلیت‌ها:
•
🎨
انتقال سبک هنری (مثل ون‌گوگ) به تصاویر شما
•
🪄
انتقال سبک بصری یک عکس به عکس دیگر
•
⚡
مبتنی بر شبکه‌های عصبی کانولوشنی و الگوریتم‌های پیشرفته
•
🛠️
رابط کاربری ساده و سریع برای ویرایش آنلاین
•
📦
بدون نیاز به نصب نرم‌افزار سنگین
🌐
Site
#AI
#Art
#Tech
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6585" target="_blank">📅 11:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFkp8NAH1Dds21_aSGXQhSUjb9st1XoY700fqEflyoOA4h1FUwVM77rgqkhyPm2AZ33thB7fy29S-06DTydGoNwPk0JrOZmvQn-fqyDz-87BW1LOJ_6jPvi0gYuWjicfQC4ldrVGDpGuEVPVH_9qBlqMb-lZFuoWr1mBgojVTthlNbPIRcOy6eW-lCFORRviy5pVGX4acKwS9A8apcv5CGezFzq4ZfwmmqFJDR4QjvqZIUMxPg72JrYMc-ABt5p0zzbRR7HRnnAZjg37z08swFwKbB6LNxyNP5By-k7JsnOpkvJ1pbJojgWi_Jq8YdRO_I6Eq57oKDmnij8KFY85RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه Orcafile دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما…</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه
Orcafile
دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما را مجبور کند پوشه به پوشه بگردید، کل یک دایرکتوری (یا حتی یک درایو کامل) را اسکن کرده و تمام فایل‌ها را بر اساس پسوندشان (Extension) گروه‌بندی می‌کند.
🔥
ویژگی‌های کلیدی Orcafile:
1️⃣
اسکن فوق‌سریع:
قابلیت اسکن بیش از ۱۰۰ هزار فایل در پس‌زمینه بدون افت عملکرد سیستم.
2️⃣
مشاهده لحظه‌ای پیشرفت (Real-time):
نمایش لحظه به لحظه وضعیت اسکن فایل‌ها.
3️⃣
جستجو و فیلترینگ هوشمند:
جستجوی آنی نام فایل‌ها و فیلتر کردن دقیق بر اساس فرمت و پسوند.
4️⃣
دسترسی سریع:
امکان باز کردن مستقیم فایل‌های پیدا شده در فایل اکسپلورر ویندوز.
⚡️
مشخصات فنی و
پلتفرم:
توسعه‌یافته با ترکیب قدرتمند
Python
و
PyQt6
.
نسخه اجرایی (App) در حال حاضر فقط برای
ویندوز
منتشر شده است، اما از آنجا که پروژه متن‌باز است، با استفاده از سورس‌کد و دستورالعمل‌ها می‌توانید آن را در هر سیستم‌عاملی (مثل لینوکس و مک) اجرا کنید.
🔗
سایت پروژه
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Orcafile
#Python
#PyQt6
#OpenSource
#FileManagement
#WindowsApp
#Github
#Tools
#Productivity
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=ronr6HgH6-jySvV-fzUPEAxaF6kGfdZbnigrcpjLM8IGKkmBN71u0LFAqp6Eq0u_Ef2ED_WfUH0GjG4dWMtT57zF6ChjkGMdoCccDdnJVja0rYbaYT2fX520GqJZo8T1i6HPb6lQ6eNVC-lAfuZtJVEcoNDBIJsaiwfhEOvAnX8-q1W74PM7gmQaM9RKmESC6YgioA79VRxVZ8wF3YlNPG9jmB_wBWwe_wlClHqI_B9OUCbQJGFPSPfyR2TEFlL2lDuQXCkl39O6bF1YLHlYR8IOAHT3aPTbZlO8k059s4KuFUj_lZYMkw1DZGBwCerJKI6ChyzJv8j9mSRhakkE7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=ronr6HgH6-jySvV-fzUPEAxaF6kGfdZbnigrcpjLM8IGKkmBN71u0LFAqp6Eq0u_Ef2ED_WfUH0GjG4dWMtT57zF6ChjkGMdoCccDdnJVja0rYbaYT2fX520GqJZo8T1i6HPb6lQ6eNVC-lAfuZtJVEcoNDBIJsaiwfhEOvAnX8-q1W74PM7gmQaM9RKmESC6YgioA79VRxVZ8wF3YlNPG9jmB_wBWwe_wlClHqI_B9OUCbQJGFPSPfyR2TEFlL2lDuQXCkl39O6bF1YLHlYR8IOAHT3aPTbZlO8k059s4KuFUj_lZYMkw1DZGBwCerJKI6ChyzJv8j9mSRhakkE7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💻
JanAi
جایگزین محلی ChatGPT
این برنامه مستقیماً روی کامپیوتر اجرا می‌شود و نیازی به اتصال به اینترنت ندارد. می‌توان از مدل‌های زبانی مختلف برای متون، برنامه‌نویسی و سایر وظایف استفاده کرد.
🌐
Site
#AI
#OpenSource
#LocalLLM
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BneUqjBw7vKW4sQyetevbZLtegbz6bUtgYesIjNsFU3V1lsCQPM_gy326UfqiWtxUfpnChhxdaDQxhYyWidckEs8SHqW4KMm93lDHC69KZAKr59XxNPUCK4n92kb5ftMUFCAsdfVsbNTXoLZFHF_TjK8x_a2d2yDD4mrR9Q2hu3wCyPiFOwudiyP-S-P1stOSNLYHTbX2yJqOCy_O2THvHS6YwgIGdEpc4K89wCSZtl44y2afPJZHgUqdoyAQK7ot1UXntJpAoajR_KZBNDs4Kd9ftYIebtD3uz0q7-_08AVxgMsr2ZszAedPHVO9N-1Ecu3qICPUudN06nxe9ykUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BEJGOv27hIXNPQo-OM4PFg7gnWgyTvHM0--iuLn82EIrSP7aZPJFGUl8O7fHoRvagZvT3NCqlYDKKkEFoS4pshGw5aAKMM1tGP3uoVtsZxfp5_Qp0-LWcClliECWAgNXngfSN-vLjzQQdJIuUBCcLOu7BQcqaCggZ5HNDqV2-JO0rzSk9w070FGA-fHFmyYRqsybxojIBpOcbuQPUg6dQeQoASzS_XnzN6QiHlXxj9Gbkrr24t4he9H-5m2eAHIUvT3Q7cFP8r0XE18MF0zSX3p3dtFOt_0LQeQcQv56bEaQ_JfUczVCO9ts8_LB6CgLQwm5OSTBfJFBhWSHT_eSpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
«انجمن‌ها» به تلگرام اضافه می‌شوند — در نسخه آزمایشی برنامه چند ویژگی جدید پیدا شده که عملاً پیام‌رسان را به دیسکورد تبدیل می‌کند.
• در انجمن‌ها می‌توان چند گروه را در یک فضا ادغام کرد، چت‌های عمومی و خصوصی اضافه کرد و همچنین دعوت‌نامه‌ها را به آنجا ارسال کرد.
• همچنین می‌توان کانال‌ها را به انجمن‌ها اضافه کرد، اما این ویژگی هنوز فعال نشده است.
تاریخ انتشار به‌روزرسانی بعدی هنوز اعلام نشده است.
#Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">طراحی وب و اپلیکیشن در یک ثانیه با ابزار جدید GenSpark
🚀
✨
قابلیت‌ها:
•
🔹
تحلیل مستقیم فایل‌های Figma، عکس و کد
•
⚡
تولید طرح نهایی بدون نیاز به کدنویسی دستی
•
🛠️
دسترسی به قالب‌های آماده برای وب و موبایل
•
📦
ساخت رایگان نمونه‌کار برای فریلنسرها
🌐
Site
#AI
#WebDesign
#GenSpark
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6577">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpQ6yyqOue-1WMiGQuxv1XTkBZdUDlV5J_JFUJyOYA7QSmLbV_I4vdkZGNdT4WpqGDWC9KfXNlJGBu46zWZC_e_LoYb3jodEC8p-SDeLLveUcplQaW-p5tQpMULB3kgVAtmWmPuCxiwajT1mFOn-W7BG9JNF6UeB8dVgNpp8HDXW61xldO2a7gFztKuVoqmv5pCFiN2rIegd4XpAmv6vepWPmdmv6-uKwyAbTmcP6s7_DkPaWBAAFn1gR5hKkxGYQGgzriYnijRGKC1eW6z65kMp68NDcSRwi4dLVbWCMdkWsCppH8bEQGyCUk4pfz0nuZJySQb-7AixLJKzHnOeVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
انگلیسی رو تو حرکت، باشگاه یا پیاده‌روی تقویت کن!
با این ۵ پادکست، بدون کتاب‌های خسته‌کننده به گفتار زنده عادت می‌کنی:
•
🇺🇸
American English Podcast
: انگلیسی آمریکایی، فرهنگ ایالات متحده و مکالمات واقعی.
•
🧠
English Learning for Curious Minds
: داستان‌های جذاب درباره علم، کسب‌وکار و زندگی.
•
⏰
6 Minute English (BBC)
: قسمت‌های کوتاه با واژگان جدید، اصطلاحات و موضوعات روز.
•
🗣️
The English We Speak
: عبارات مدرن، زبان عامیانه و اصطلاحات مکالمه‌ای.
•
🇬🇧
Luke's English Podcast
: تحلیل زبان و فرهنگ بریتانیایی، یکی از معروف‌ترین‌ها.
#EnglishLearning
#Podcast
#Language
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6577" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1SGVgDoK6Z0LZ9t3DdPI1G61s_QZcYKZjeBfNndMLuM4O9WetDr4S1sSi_fQqBMa-4_d-g1I6pW2C8lcm2PASLUYviwKN75uT5L-ot5ykn8sMaegq_6Hadm38R3AAwnepu7Tn25X35Gq2Q89Dhlh35jAgTSjys_FrG-yX3Uc1u7bAb9FBt8htnZ9ch1Nl9NhB5zsoZtfuvrfWwWFwFpY4DWx3yyRT7Nn6LrSDfb5h6eDWGCutnBXQ51Uk9j4CJZ4Va9-psf0XDTHMpziOpyA00pigl62Fa8T0ExaU7k3wrrhGJDN-XJiV_hlmbHSaA0GdZFUIjwBvvYlDdj1CU2mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2zv0dQo2IAA-9Ko8y_yx5SotRDoSVKIyztwTSKJETMHyPDGx1v6_2MOpE30q1y-gY1DrNE_8AKZniwOcazxFMWAMp6jmf9GgI0C99oFt7L0TnpURna0E-WT3VDq1ZSDMoPX6J3BW4uG7fERzxVLpqRgzXoxcUdXyjM8Aaj4f3biOzy98QhwjSGuN-aX6ApPt792pBVpYZXWAAVaDeMIQU-jJo01vAWa0iVAhVWfQ2RlMYArZz21P6HlTlcwKafcAwyUfZODuIhv5O_0x0zfnPLk4Ri_6Ig50lsFXS0Wz2YCX1VZCdDGgbWvKVtyK_F4dDRjvayeaIOpvOKiwcDPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pI73g1lS8HCGDhs6s-hRe6NQSraLJjg29oonvVIi5mnYJ9aRrbcX13BXk-LpHwy6ZPIuLLOUKCQNYMeZIF94TD8GHSvU82_yPT2ITt51RuNbh73IaN1jbyQP20QY9XuTlDL46YWKk19InaThZA2TddOE6BZQZkJHplM02X66Pigz0EWtnnTMfBzOC0qJDwK5A_7KjUtlDgaFbwRZy8LMoNiDDHfls1N9aSAj_w390fAgzOefkEWPuYAFdh55V_nM55J0j_UZ2UfSh2A-0oVQ2fz2mgB9heHyPRHqxFS1AQbZVeizLnNx-wm-qeYErDD4pRkF47PSzBfaWy0hLRGDww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
OpenAI
مدل جدید GPT-5.6 Sol را معرفی کرد؛ مدلی که در چند بنچمارک مهم، حتی از رقبای مطرح هم جلو زده و تمرکز اصلی‌اش روی کارهای پیچیده و توسعه نرم‌افزار است.
💻
🧠
•
🔹
عملکرد بهتر در بنچمارک‌هایی مثل Terminal-Bench 2.1
•
⚡
توانایی کار مداوم روی پروژه‌ها برای ساعت‌های طولانی
•
🛠️
مناسب‌ برای توسعه نرم‌افزار با دخالت کمتر انسان
•
📦
معرفی مدل‌های سبک‌تر و ارزان‌تر Terra و Luna در کنار Sol
🌐
Site
#AI
#OpenAI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6574" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الان برای API بهترین
aerolink
هست که بهتون
opus 4.8
میده
خیلی ساده
لینک ثبت نام
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
نحوه اجراش روی
claude code
هم همونه فقط تنظیمات رو این بزنید
هر ورژنی از claude code هم بزنید قبوله
{
"env": {
"ANTHROPIC_API_KEY": "کلید",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلید'"
}
لیمیتش هم دقیقا مثل
freemodel
هست
فقط مشکل اینه هر ip ایی تو claude code قبول نمیکنه باید تست کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6573" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=mowRG13jIlmSkgNhrAi_D7Fc5lcgLnxnEm5hw0Ds7jQLtrri5jnuSzKd2ogc8sYhMoc0satQ8KcoKEtb810Em4al_deUSsj0dpZByFYfWd-VmFYXgWTPHxdtFSTKTJw7q5RtAOWRru6wb44ufpZcXLftlLHNOhaltKQKejmHqnfHiHMFoO0jBv-qxeJC4cuk0kjHTusJwF2lNBXjnLgTAs3KaMZ-hOU3Au_vHjcySJW3lc7S6Sn9wysMA_fPrY1HySO_povSNb0z9cU_6QTIEPajXgb-VuwLL5BkWcSxTnsicT_sQmtHO_ANzSKkq3yXcVrY8H71VAwmXnv_oOwpXaGX-ON9Ya7x32kBt6k0AcQf8dsdKyRH5B_tPghbYdwMnWqVI3_P-beX6bJMWX8a5aJ4cwQjciDlNIvMnmdEKcy2nKTs6tZJhPI0rYGGmvBqjxF6KPkw_AYMudiMn6HZuVYbz0uccTmq2PPxt6JW0Th8jluY3ax7rc4MPaqlMO0hMFFoG79V2ZBNz0-cBhvw83DwUsdM6iK56Jzbfoy2Vshxvn6VVWRshmjxN2Lii6xlCI65BTeoR-TTE5y1KRooybpPyjQrMuXuE8E9mAkGxZULcC4bs1TA9OGa32so0KCZLD_AKRTptADphS-CsNH5OxQMykz8QcqT1P3jHyf9pmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=mowRG13jIlmSkgNhrAi_D7Fc5lcgLnxnEm5hw0Ds7jQLtrri5jnuSzKd2ogc8sYhMoc0satQ8KcoKEtb810Em4al_deUSsj0dpZByFYfWd-VmFYXgWTPHxdtFSTKTJw7q5RtAOWRru6wb44ufpZcXLftlLHNOhaltKQKejmHqnfHiHMFoO0jBv-qxeJC4cuk0kjHTusJwF2lNBXjnLgTAs3KaMZ-hOU3Au_vHjcySJW3lc7S6Sn9wysMA_fPrY1HySO_povSNb0z9cU_6QTIEPajXgb-VuwLL5BkWcSxTnsicT_sQmtHO_ANzSKkq3yXcVrY8H71VAwmXnv_oOwpXaGX-ON9Ya7x32kBt6k0AcQf8dsdKyRH5B_tPghbYdwMnWqVI3_P-beX6bJMWX8a5aJ4cwQjciDlNIvMnmdEKcy2nKTs6tZJhPI0rYGGmvBqjxF6KPkw_AYMudiMn6HZuVYbz0uccTmq2PPxt6JW0Th8jluY3ax7rc4MPaqlMO0hMFFoG79V2ZBNz0-cBhvw83DwUsdM6iK56Jzbfoy2Vshxvn6VVWRshmjxN2Lii6xlCI65BTeoR-TTE5y1KRooybpPyjQrMuXuE8E9mAkGxZULcC4bs1TA9OGa32so0KCZLD_AKRTptADphS-CsNH5OxQMykz8QcqT1P3jHyf9pmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بخش انتخاب پنل ۴ تا انتخاب وجود داره
طبق تجربه نوا و زئوس پنل های خوبین</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚀
معرفی Cloud WZA
با Cloud WZA مدیریت سرور و ساخت کانفیگ‌های کلود ساده‌تر از همیشه شده است!
🤖
یک ربات تلگرامی قدرتمند برای ساخت کانفیگ و مدیریت سرویس‌ها، با امکان دیپلوی سریع پنل‌های محبوب:
⚡
Nova
⚡
Zeus
⚡
BPB
⚡
Nahan
فقط با یک دکمه پنل موردنظر خودت را دیپلوی کن و بدون دردسر شروع به استفاده کن
✅
✨
امکانات Cloud WZA:
🔹
ساخت و مدیریت کانفیگ کلود
🔹
دیپلوی خودکار پنل‌ها
🔹
مشاهده میزان مصرف کاربران
🔹
ساخت کاربر جدید
🔹
مدیریت کاربران
🔹
تغییر رمز عبور
🔹
مدیریت آسان و سریع از داخل تلگرام
Cloud WZA؛ راهی ساده، سریع و هوشمند برای مدیریت سرویس‌های کلود
☁️
🚀
🤖
ربات:
@nova_wzabot
ــــــــــــــــــــــ
توسعه داده شده توسط AssA
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=GHteixSZftBy7VznqAD4fc794ObEW-VeD6sJZPxupoE8fv0uVgNRGkmcwFM_tfCzmbNWS07LNrZowhEkLTGGa47Wi2zYTKEBX9PNwD_TAxrVR93SHKC7ZYLZIxCDQIsOxpg-4IOdieF6eAGOF2P4i6id24IOqe3tBLwe3W2cg4P7kBWl1R-cGn_DcTKz40-V1gA-PmCx-tJLw9Uz9CP2Jyr5_8AXdAycBX4OlHBgATL2Dqwfk_dMxtbIyEfT5MlhtFieIXJxlcOcHGYolYuhxFUxxECFuD5YTLp1H0ahRGWRavbEquxeIZDlbZD1E57ZX7tCyuQDIn6TAKmXWQ4j-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=GHteixSZftBy7VznqAD4fc794ObEW-VeD6sJZPxupoE8fv0uVgNRGkmcwFM_tfCzmbNWS07LNrZowhEkLTGGa47Wi2zYTKEBX9PNwD_TAxrVR93SHKC7ZYLZIxCDQIsOxpg-4IOdieF6eAGOF2P4i6id24IOqe3tBLwe3W2cg4P7kBWl1R-cGn_DcTKz40-V1gA-PmCx-tJLw9Uz9CP2Jyr5_8AXdAycBX4OlHBgATL2Dqwfk_dMxtbIyEfT5MlhtFieIXJxlcOcHGYolYuhxFUxxECFuD5YTLp1H0ahRGWRavbEquxeIZDlbZD1E57ZX7tCyuQDIn6TAKmXWQ4j-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">KREA.AI
Enhancer
تصاویر پیکسلی را تا 22K ارتقا دهید!
دیگر نگران کیفیت پایین عکس‌هایتان نباشید؛
KREA.AI
با ابزار قدرتمند Enhancer خود، تصاویر بی‌کیفیت را به وضوح خیره‌کننده تبدیل می‌کند.
🖼️
✨
✨
قابلیت‌ها:
•
🔹
ارتقاء کیفیت تصاویر تا وضوح 22K
📈
•
⚡
تبدیل پیکسل‌های بی‌کیفیت به جزئیات واضح و شارپ
🔍
•
🛠️
استفاده آسان و سریع برای نتایج حرفه‌ای
🚀
🌐
Site
#AI
#ImageEnhancement
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zzn-lj2lE54_DzSaGxpMPi-nGCNmormuEFCE8at0P8FGB7TXYqSR0VDWLma4WP9zAiYJ6lrlC9t2vr8h8XOrEKMRavS_lgwW8abNf72e_taBNz3H3eL6qIECijxbSPV4KV94xZjalyQuY0lhWE0WeOMiZKICBcX33L1V2rDgvjfko06er_eybLM0NNPQHb5b5OKFe5SbLSnq49yZR833mLHdM-s9gUrmakg7CciwgY5iNt2o-0_MvIQGX6YveBV0ttKaYp2N5jUEHL7qg5p4M44-Fqwcv3PDpxPrq6N42pRPkFCwpiYZoJ0MqJM_cDvRiREM-wyFpzFvjDdmERDf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1000 برنامه رایگان برتر برای آیفون و کل اکوسیستم اپل: یک دانشنامه واقعی از نرم‌افزارهای مفید در گیت‌هاب ساخته شده است!
🍏
در این مجموعه همه موارد ضروری پیدا خواهید کرد: از پیام‌رسان‌های امن گرفته تا ابزارهایی برای تماشای فیلم از طریق تورنت.
🎬
🔐
🌐
GitHub
#Apple
#iPhone
#FreeApps
#GitHub
#OpenSource
#Productivity
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=qb-88dJwyBjAwQhIr7mNgYkTDtJJr7lN416LMxJfwQG15o_09oA0p83LDl_IJsSLjUm8k0lAPwEBSon1TDBVcA7JXHysTVUPVpJwTYcOgDvISIYi1CQCehYoxTi9QdfJJyIPzYD0LeT-n43TmBRo2ZzdkuZextYXook-ICeMfk87hZ_7hgxB2EJqSAJpnRrbhTNtLkedb_dOuDovSJBVmy20dSBebZbxc5Avnz3gI_IsRou4a1FQUeVJzaY_q60NnJ3QRzsougJPpIjZ8Ha7wCNNw1zgjWOUI5IvuGWD5V_V12gwOK6WYWgwDDMGdvfd5Y6ooMoiGURZEI5qry5w-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=qb-88dJwyBjAwQhIr7mNgYkTDtJJr7lN416LMxJfwQG15o_09oA0p83LDl_IJsSLjUm8k0lAPwEBSon1TDBVcA7JXHysTVUPVpJwTYcOgDvISIYi1CQCehYoxTi9QdfJJyIPzYD0LeT-n43TmBRo2ZzdkuZextYXook-ICeMfk87hZ_7hgxB2EJqSAJpnRrbhTNtLkedb_dOuDovSJBVmy20dSBebZbxc5Avnz3gI_IsRou4a1FQUeVJzaY_q60NnJ3QRzsougJPpIjZ8Ha7wCNNw1zgjWOUI5IvuGWD5V_V12gwOK6WYWgwDDMGdvfd5Y6ooMoiGURZEI5qry5w-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک برنامه‌نویس جوان توانست با ترکیب علاقه و مهارتش، درختی که با پایتون کدنویسی کرده بود را به قیمت 8 هزار دلار بفروشد. این پروژه از 100 دلار شروع شد و در چند روز به این قیمت رسید
🤯
#Python
#Programming
#Business
#DigitalArt
#Success
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter
وارد سایت
Agentrouter
شوید
با حساب Github ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Token
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
"ANTHROPIC_BASE_URL": "https://agentrouter.org/",
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
حالا آماده استفاده است
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
