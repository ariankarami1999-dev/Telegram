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
<img src="https://cdn4.telesco.pe/file/JwrmCitxYlfG27FkdPHE1LcuQ4_hMLryhFdp3lzxW0icrN4M7lGelSdS6ahHH8RVwl1B9JFQt_kG8Ou9orALZZmVN4KMI7enba7l0CIKOkLTDgCbpaan1SaCDUmPR5y9TDCWdz_l7DWA0s0RGAuBHs1EE7ydmoZH1FdkdD73n_-nuzuFAJiMv1i7xwIpGR47tugqhyuxQF-p2WeAqy4RtBzaSccSYrYrflLlDQQyzdRNvbGt0w2gNotPbH_ykVmjxymz5sYDnLBzXaRlWJjOMNXQ3DyyBZ2RutZc5HJiic9C4IwoAUk_TvJZ03IiWwYGRn-v7-m884TZGB9hRJSXRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.65K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 01:11:33</div>
<hr>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXOzvkNUEqitBBNdJiz3nt_4eCRTmqpSxhVSuX752PZjJa721TFghHmyOOsHwqQsIQLDdsn_nc6H1X56x-yZhnVxzGPFunL36FCn7H00kknYKmP1vZbK_HpltoyG8dBbbvmPVLna8WDPH2WFYFm7Zf5EOqNVOKo29-GeFXjtiAMGtnM0GjyTwKE9XItklajz7TFB43lDqF8mvku1zcQF5-xexTtIaxKKBmtoMQnTVFPQ7EvNn9NCkt3jn3ol9xEh11-vU9RqoK5v0t33xwQ603mzoHKgkGvu_inbGb9ZyPnZjNanq8OSGngG5N6FrOgZCzOahDTmMEqU9g-aYR6H_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 590 · <a href="https://t.me/archivetell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzgpLGww_NwbJFA-JfT4BTh45CSqsmHsWNk2UDkJplexJacRzHtyJ2bNhk74I0N7k0eJtDbxBoImXAo3nHcvrwI3otjNXdOBBpUcRjGq3h7RCmA9ljL_iW1lGYjM91D7GXjoYnpi2UpXUt8ev05qhO4WCd9u-FKIhGXl37pDXfWwSrFsxiVe8Ce-jjXlGLOR6Yx_WYeX1v1VhKdWYlmLjfbhv_4Uk0CnkZ-T46c6CiwasCRxCMuTJ8Fqcha6hgvBQsW1fWpDbsx5gZ6RLrv-X28z9lAKWL6NnmK8G9NkspyqCwXm4fbtJBHEtwRJ0lsRBQuN2PyTGG-j4JjXXXRM45rs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzgpLGww_NwbJFA-JfT4BTh45CSqsmHsWNk2UDkJplexJacRzHtyJ2bNhk74I0N7k0eJtDbxBoImXAo3nHcvrwI3otjNXdOBBpUcRjGq3h7RCmA9ljL_iW1lGYjM91D7GXjoYnpi2UpXUt8ev05qhO4WCd9u-FKIhGXl37pDXfWwSrFsxiVe8Ce-jjXlGLOR6Yx_WYeX1v1VhKdWYlmLjfbhv_4Uk0CnkZ-T46c6CiwasCRxCMuTJ8Fqcha6hgvBQsW1fWpDbsx5gZ6RLrv-X28z9lAKWL6NnmK8G9NkspyqCwXm4fbtJBHEtwRJ0lsRBQuN2PyTGG-j4JjXXXRM45rs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlL-DFNuxP4oeTEcZSH_d7UYw9E69hLwbUMdvY1fgXbGoNHMm4rz92ZDf631NmvV3usa3hVZfJHM3cNCqlnytibnqMHenXcqCpunWaWYMPfsvBtyiBVpHPn_JS9yWVISgsUxRYf12nAcq0UlvZinI1H5vr30c80lpnhJWrXEOHcN7TsrprPw0IddSQFQHL0Q5ZFYNIyNYZkzPZ-lrtzYVd05aYEh6R813lgRPW5FwQGsM4d3mVgxSS7QFXQsxA_OwwYDMae3BgzGDi4_qi4f7ovuS3f_ILESrYtGxd76huQOHImlRc2vtpnfF1fR2qJJ_DNgWuKMJ7s5J60Ux_rMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEuQIEbaakU1zr3ooaOx48JfjwJYMvhyfNQ3Ccg3J40pfhzaRTv2DvMj8S-18hR_5YWx2F6PBvFEivEzEJmlMnFynWcMLJ6BaHVwZ9lB7DCo6TibR73M2Pyi3dAucE-h6M6R_w3UwA1RXCnOpSfogembXmHyGm0Vc7UOXPx2MJmzBm0mMki_fz_W-3_WaGNhlgcJxrkAqkLrmu1N9XLlK4tGMW3wCKqoAa2hBxWdCkQqO46Cf9ANWbKbWR5ycp0wSA6c3UhHO7ub1AhCc0lqBFviRQd8tAhg9V2UdZXOm5y_zcqXU9n-gqcUGOrRo3GcByz_8y-B5pfIFtSnInd3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB3rvVZteb55DZj2Wy5Se9wWiLsGpXmGF-bz_hfpHSFPSJ9DUjdNdlnSExPZ-fAh_ptaSZjyoVtzx2szDwCySovIR9MndlRJSKx32kvrY_y06jKssz-zEiqxCcVNIuBovPrM66V4ng0OA6-TV-x-0AAjQtipKet0psnVwYRlqYqPbc_U05twPVtorSvRlqzAGllvZnIlCxnUK0icivE8V6YirjSL_6-uPgCn3K3I04HiBZ6EwM969FcaWnnsMDRicmTdPc-7Zx7k_tE72fdrjvGnCZ1AVomdFtx3ntu10E5QQ9xth3pRiVjfFa-Dy_ADxn_uawpFBxfyT9bUyCqGPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8WEhatx0JfrEpVZGi0OSvzVmyK8C5UFoRN6XMPiUrqDKd7htd4C_Jcd7uEB2OrgjmyGfkx0xX-_ZQW_lzcWZ12a8p95fi9Opzpm5VUavXbwNzJiLYqpWs4pETCXz0V2SQS429T-uqci-vspN2IdPP_SPsnSOZGoaVg4rmTBoWkWXLtAnLkZOgfKxkySL5OWQN7TQwvtGyLJkxrCf6ZqaXONJBAC-QjI92hY-4xfRObt_Hx0-qNxbgOzPbC95fyB5ABeR2SqN-53iPuxCjTKAJexHjBg4lBwAPRFORgqskj8bEQsX0R1vH_eip0q57I23rFy6peZ7aTbEhqoCdWWWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFMKPfrAYxwdXVvc3fqMS1dXl-B8eWd6X_nQCDH9IkOQqNV5JS1lOVVD5zlb2j_LBvYXPIDZ1kycOq7XZehWLIe3A_8NMW2RYfVydT4QVs6asg5L57UFCrWjfouQkUboPzEaCOGrhYux9za1gyV2-zpErwJZjACGua262QQhiBRJ8oj404jZICpYu6JUNpN8V0weifW0F_a-Zu0kU_zEDktSU_P4pUXFN2hjfPl3kPOkup_bfWZ3I1xbxah--euqp_1OqOhOJTh30_6DuSfbXVCHLQk2fYpOogkZwBxrrcOfM212-6QMMFdnLdtroa7Avl-1i0DjtlftkQN-idgSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-WC6w9qnMCvEu8kp4WeYD_HvRlw9Iwbs1KJyvq-AysodwHQxXsxBtRr77X6-6xqqFu5B7QSILI615-Lqjj857WRw48SGrT27jVbHfxw6JFvDg2d1Ivp28QV5HzyKSwSzzP_VrHaGOsOpzZ7qd7izdLoakIvaQsSDQ-TarTYe_5Kqeo669VBXWXmPDBVDOv6AOXa7KiuPueg5ScoGiCkbxR_L4c4CXo5tqBfCD7n6TqjbCZdtXM66TUfivhuwi1qMgXhZH3SBlfSLqIwhb2x9Tf5AWYMzp6uTtBGnaLkvWCwqcWe_PDRblLvJ4dm4B7BnLL70_pjjzl4sGcwc6E2fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgPAgtVR7cupEQWVr7ZhszI9CLLKo67Qre2VRDExIu1tiRk943Gkc7i_fpo8OFkrylOQ0trPm7Jp2L-5MGATasz6RyPhul_yds7y550QnINCvkq_axjXoQqWPhKxVRBqwXIFhMQcAaEMZsmPGusTc9WxIRmg2_JDc0vV0DrnZdrLVFWk-uJhlIsii_ZoJROZalOaOerKeUXtVnoxcB6XCQHEbRbDqvEoCBttzsEytINzUoebs8zgL1nthl2bCqRU7eYEKPlSRSPFI8DThkAB2jIo3bYT5Z26vTJp7uXI7Tr2YTJvJoa1SgvoSqKgPZ1EeOZQmC_wNQkJQ_MY5Su3Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=GBRFP_8WVI7eRN-ZEoWd_fvoGGAOn4wzuxTmMVeDUTf9yv-KT9thoxXDJ9Ifymb5LpmySC94fY1RDS5rWefPYMDzwdLBYaOp2ULvesXGDKVW7ezBB-eoEs9lC7HObcr4InPEwNrGFoErOJKRmpXJZk0vH1YaN785Ce2-pEo-BDXU9F59Fr1lfVWjrDYjqMyNMmmhNwHeYFl7saadJt75SDwPYR-hFZfOcFXY5NuCwpaGZN6s-kRBn6M0S8VqCWWJ8OjZCpETMe2mQdNAfsn-QYMCOiDTySljkDSukOepOcOpxl8d7A4GPN5yEEN6dnGAFu1t0qoAkCQwPWWUYOE_Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=GBRFP_8WVI7eRN-ZEoWd_fvoGGAOn4wzuxTmMVeDUTf9yv-KT9thoxXDJ9Ifymb5LpmySC94fY1RDS5rWefPYMDzwdLBYaOp2ULvesXGDKVW7ezBB-eoEs9lC7HObcr4InPEwNrGFoErOJKRmpXJZk0vH1YaN785Ce2-pEo-BDXU9F59Fr1lfVWjrDYjqMyNMmmhNwHeYFl7saadJt75SDwPYR-hFZfOcFXY5NuCwpaGZN6s-kRBn6M0S8VqCWWJ8OjZCpETMe2mQdNAfsn-QYMCOiDTySljkDSukOepOcOpxl8d7A4GPN5yEEN6dnGAFu1t0qoAkCQwPWWUYOE_Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">با سلام درود رفقا میخوام یه ربات open vpn بیارم
دنبال پنل درست حسابیشم
اگه کسی پنلی داشت که بشه حجم و کاربر و ایناشو مشخص کرد ممنون میشم داخل کامنت همین پیام یا پیوی بگه ممنونم ازتون
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6433" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo89o-cJJBoP2MBoVWdTHOY9s9P6KKdtKwGvTI9_hIbw006PjWqDJa-_2QkueTQRTz-4qQFBNjoKjbgzeeYmKmOAcyuqqIiuCf1_sblBbjnbAjGZ-0_OWijYXsyDoncQ_ozYwl4p-sKVbmkhmUwG5iVG73fSMB4c_p81Tg3PApVC-gnuNfzo2x2Um_uVIKuJAlFH0x50rXGpqZFWESZtTPn6SlaLDLbRK4lnDJlJP0QngXSbDoSC6Cxz2gpvj-eEMIWKmgJPVhCrdv924Lxizf4xw23t156kdSjMimaD1GOXghILYQQB3f9oE3EJEDJEBWURbEJEztFI9r3hwpEnFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IchWyzJMUB0M4q0kCvEGZ-ztTIdqFhhvoc8a5vaoFgMPuELPMvHWQKoQVDcFJkTHjGqYFPPP45ZfVzRvUxK-TR1Jw7H7sP9fEKJ-2sDwVx7Q3W3fXZwBCZWoGJXttHLj22Gzp3GaGqPAgCG3RaYIAyOW82ecR1-7OqkL875GbR_QCn352yBJXvtTqQAgPiYZXA1S8k4e7Oyjqk2oiy6bmsW55_7DYUi55tmuLmZyDrDg8d6eXx6-Q3fhW322_4d3mD7Yc8x_3JK0E52o2X8qpkjPR2weQzCR-dR5tDRaYl3aPiqbAgQaaiiBk_w88nDT6sPjGGmmFEosiHbkuIv76Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFDaXTO-W5-utXrTN_zQuLXT83vK0c_jPizZEb9vh5xjchmLne-g_XrhGoMFb0kxMRistha_bH5vQj1XvglSeCiLGnF7lzPjevhQMrIzKNXtnaM9bRnRoXPEs5EHDRVpeMJ7ug9NhDXtUWQQ77J9OhAk-6DzFHrzQd65os-BmO9XpSS4t-xLysEY6J-G75uDnlaHBbqkO0lSy7UOuGW4ART4seqRWhLzJdd0j4AT6z9SeJ9iOSPE7pbfGlk4mSY-aRpZIAITGCVvlO4BSZ6MzPTmhaWfHLaYUFkNZT28YIfTCEiEPaJSf14aG-LQJjJEYGuHa9U-3EcY7ciKesz8fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ds1lFJxPx55apwxZ5bkPIWMvRtA7K7_cz10DFpjA14bn68ry12XWGDHnS0OKKGtsUofguCyCBEwvcKKKSX9h86HeVMYoQH5TMCDw3V1ZGkUbrdD3bO4gXjUoTi5q4DzO6VMV2UAdl68Y_rI5KpakpOxScjbxRJhLIHs1CCX4aim25rTtAZaxY5l-rOSKnxbrURSGfqJ_bZB0Xn0a94LvPJ6C6_0w01_E-PsUYs4bvdoktNfZmhfVcgwXl9nbiI4C4mmpLybtGvILT3WnPJC4F9-UPvvxmIv3-0tmQC5v6LA6A3HcKzoPQkuYL7OwZ4Wd5_tLAjMFdHLV58Dn5h0hsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa-K79iCvr-koDIMRHlHDUCYH0MPEwIbnImeOCOJmYhwZUq65F-pdFg2bn8e8KwHFUyB5vef__8qHKLKTFdygUhOApsJ_zZAHHbOptQJj95kCv48BS08FC_fJ5mYLH7126CZyZO4SXbop3c8TASKLt6Y_T65cZXfEC68VG1FN3klE0vCRUduKK-W-4-n6_KfMmtUhC4swPMMMqovDwcniH7uLW_sAolNDVZUJUqEH9YDCa8ofHEHpoOPs3WwXqvdrLJqPgUhGsNDrcpQ12uWS-WFJdilKGBAz9H1cJRjhPNiOFFnf4Cy7tPA6rNPl0jrYS6qh-XGKv1x4F6HpDE-Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bh_ZcpUj_zm-s6PQeEHQIDJwSfJXy49otidN4zo7vsXVQup7yQ1qrmuxLiKYiu_IC_Z7n0FavY9O2aczJ-486MUp0o3eO0A94p3-zC3ok4P8JLLq0VESfGB3kh7ZW1JiD1KyVRoxMczdCkNSuHZoaitl5Vc6pSQp20pTugh711-XsGk2V57eMn_BHtJ3_5DDSGY_zw886gBSMrw_OQjcrpN86y5QLyzp97u0FSnrv8qOpe7IulaBa4vXye56N6-iLmJfK1YwFvH78jLXOQ7qMZI552emmgFFn6p9bEeG3DH7yRAvQP6Mibeva5gOPtc4FEPxsDG41dxlLzujDDDP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKcgj44qtEBsZF5rJ4a7vCbLFhO_KnhwsLVxzSs_JwjcOsuogfKMclJZ_KKGkn-2NuoYIvSK22DJ1DSwftdcaw1maf6oRodRXMiLML3MVYYTsTMc59nlO8uOukJ17UImJjeNqIRIWPV0dHwMLIaKPYty2Vw_mYWO2A8r78KZzEQO0hiCXJKOmUC73lMtwfcEIA2f_v-w7cPFV1F6lFxf20_zJPEaFBg_zaiX2CgjowoXizVEhGe6-PCQR5hvb1hoZLGjS7LSu7e17fdj32sdRTEkO89rI1JTRCn_lrB9C4Yq3jyUYxWcVIoFP6Ecw3kJNZqr8JJFzcq3IBjtGUGDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dle9UyAW0fw-CtUgf4AmudmsRf7ati5EhDRXVwX84Cvi9Ej1W4E2b8r8aovRbJvgkxwaIsTjnOvcU7GGGZQEsRKUyfib_kSY8JsIeI9g6j0Uj1BBAH3ZxaO2q3GFzqbBAP__EdyDLiAlKceb5LIMwIqcaxUbY8pk0bcKUeh3XhwGZuJiZVfnsKPosyoilbHRVn7jRloaPvbTtVSLhtDQ5MOae3rbw-RojKIbY3gI_vh6QJI48gvX-K8zihHZDra0xd72ansyxAhGhORT0prd-p2OrrfP6Q8WvKpCFxoo_UPLeg2qaYsS8pydfcSKLxUbAHgjlMgoQ7IHKBzeiskqHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWXgWhIO1zcKk-Q8r8qaxlLa4Dnq4jfGE_5PfpxnP0qJnJQckeutWFXKTQm5JR7zdqGEIV0OcmIjHJnb-gZCYyH8UB4BWhXCe9KebyWpIO-GJb7gmP_DobrDWOOvj08wdHAgLKE5VQvPj-wW5oKadpMgaUo6PB3Ou9v-WLPnoOAO15LwJIrJPDtjFw0lkNNyRm_0sQ73K3Epqg7H0XMxP7UdEkZlhhMs1K6sWoZ9w6SqEg2kXQRdbRrRJoL09HcspaHw_3dhUarjI1G4Iruq5yww2VhoCq2iaE-zbNEi3_w1ikG3FCP5AGlXng56aKSHXnUqq181mvTMtHn3x_8AaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGk4so9dYzVC84xsF4-h8R1d8sTJZm6JtWBT-eYHCIClTuJWDIrnadzP49y7NJZn7ob3NBRE876ERHA0f6N6cwTnfGmag19mm5qNbvZxc0I9WawnOMiD6M8LBAsVAmuUtw21FnbiLB8iN1tXWv1waPh3mDsObfZIR2h9KZEK7HRdehLZuE3tqdSyM7bTZB53MNQ52OkO0EuV8fCWmxml-dBCsVAu8-rnUjub0dOuKN37nx57bIA4xJzdiPSOYXevQs0LwhVyBsfHRy9mvtOOJ9OiOBx3u_IGkwT1D0hbE37HScpNduMSoU1F0I0sMX8oRLCoZJt_3J9C6UyS76SA3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGOvWpZ18GeaTZJ2g7pqmC444aCbRfdXnXZl1UthOUBkabcDqEZe_GNw7oEZbssN1TW4fXetK6QMdzj-yc3p463fiIBhJGitvD046crXQYpDChLhUBQVv01_uMgfuO2wgr_F3rSCWFIX2tvcXv7yhpTdaTsREFKCqXLHNEHu3FRaSQEIFxUhKx2PWWaAHFthFCOLrmf_Nczx-lKV_sy_74HdIySxNSoeAwWcFJkY-0r0YR0w3hj3GsjqcoK7p4drVENnTar9ipnR2I_JHboBrYFzVBkwMvmNtWUK7mrBYZpW0wvAgyyp937D9MA051-asq02ikq7KDoDXUNHLrsgkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XctNkFBlXwHhCefIojUGUwZ3QW5QKsNYgOurRzA7_Sr8vVwXrN2yNQSrwx5BvigeNhauikynUCaRnmfjC76QHXw25siAyE_cUGBN0t8asvmTPVRUE8uOcmnbU0nGp_e6pvyTfRNXMivoIv85OKrqRaHoc1g602gpR3JxWOji2kkWZrbOAKPMIyrEx21t1UXPtDVBqknifHy0jdcoKfnQ2l15JU4JFQWpkd6Ferw5Y3m0OJuq9PfVfSxEfLHeHtMxYc8y8GvGVIlWBmGy3OL56DNB7syv_j0G3u86BqGy6YekilRUIII4JhbcwGfqEV5rmiB_gbgxw04lGJGOBeuycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QazoUdSZmV2vJSPr6SbqzgeJ7sRrAM18uTo9EGz4d9bqgXNQ13OwjsK3RGzXRp87HuIpOi5eC62tmHZOxpV_Wn-8YJqa86XH9mGUW_aiUns7EDTlhgpVW0-Ol-koa7z-ZdzO6o2dl_IzuNDKOhKHn0Rpk2y5y26Xk1G1Y52SGjEz6v8bh4kt84CftBl4f_-kbYeUpoDpWdge4tAnH5yihRPGQNSNhkdluIPIrwrEdmienBLh_BtXZM-qmCZ3a9ZWaacOMeHA61pbbxUjZ9mzhNGWhFPc4Ii-Krh6hftgqz19vKjt7V0IJTRAFF4W4krr3f4U7o5IS3Yklpf3Z6CKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAu7Eh1DERH52XZByPKJUm6HUFqhsCdeeuUzT-kvCsKx5FdIRQUhckUt8s6y9fq1OGwqU6g0VPSMB_QWBpGJsx239ezmSL1EDUZgkpwLA8Mo0Tc2O6g0l-CpkQrI6zgrCg1Bq2sVDL6LU9q1ck8IKcDZQjgWDUATqes18i_Qu5y5MGli3CrfhT_O8Y46jbj3VO_KJU7Q5Q03wo7_WT6hyBRA5ghtrFhK5asWXrS8Nay0cK-5hM1Yyh2jxLNp07vCLt9EWXFrdQavq1mSgJR5dHexMAFtKVxMrkDmH8oGXqtVmMFiKabHc4QDMslzp41RVxJRHxPUT8pBKQw2eEKfIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=CYiKGdMVBrMWlPDuhbKn80N7_8CHIveM5aTtUIXRL-sz2-Uc1XzK_oxpGVNtEqsBLWd3qDD9e1WcrR8wmiQV9ct6UbdIVcSPrLCZpMn0d9dMNBEEo95gfd7Ng4iP7b2serUlyCw8p8hysAgXrQyb-nRYm40ljkGh92pKux5toK6SZ9K7BDgJah0obWuUgyrnbBwY0A5EK81gnc_G2Vu3oIrGQgHVzPqX_FbNBPU-zTOjzjMtIbIMZGq7fqcVQEqSBRAwlBlBV4l58cafz5bXNpBS3A981yIO8_q18Yg-6uiUNIB_Ff5l0eVWcYE5aPbzVKt091DfITr07Ye-fEXy2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=CYiKGdMVBrMWlPDuhbKn80N7_8CHIveM5aTtUIXRL-sz2-Uc1XzK_oxpGVNtEqsBLWd3qDD9e1WcrR8wmiQV9ct6UbdIVcSPrLCZpMn0d9dMNBEEo95gfd7Ng4iP7b2serUlyCw8p8hysAgXrQyb-nRYm40ljkGh92pKux5toK6SZ9K7BDgJah0obWuUgyrnbBwY0A5EK81gnc_G2Vu3oIrGQgHVzPqX_FbNBPU-zTOjzjMtIbIMZGq7fqcVQEqSBRAwlBlBV4l58cafz5bXNpBS3A981yIO8_q18Yg-6uiUNIB_Ff5l0eVWcYE5aPbzVKt091DfITr07Ye-fEXy2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-text">بچه ها شرمنده یه خبر باید بدم بهتون
من تحقیقاتم از سایت render بر اساس هوش مصنوعی بود الان شخصا سایت و قوانین رو چک کردم
مثل اینکه bandwidth رو ۵ گیگ میده اما پروژه اولی خودم تا ۲۵ گیگ مصرف بعد ساسپند کرد البته این هم بگم من کانفیگ پخش کرده بودم و تقریبا سه روزه داره دست به دست می‌چرخه با کاربر بالا
الان هم کد بهینه تر شده کمتر گیره
خلاصه که شرمنده بازم درباره اطلاعات من احمق برای اطمینان هم از جمنای هم از Claude هم پرسیدم
😑
💔
البته اگر قبلاً ورسل زده باشین میدونین که اون سقف زیاد مهم نیست و اگر شخصی مصرف کنید و ترافیک عجیب رد ندین کم کم برای شما تا ۴۰ گیگ میره بعد ساسپند می‌کنه
ورسل به اون بزرگی با هابیش ۳۰۰ گیگ رد دادم حالا این رندر که چیزی نیس
😂
بگم که ریلوی سقفش همون ۷۰ گیگه
و اینکه اگر ساسپند شدین فوقش با ایمیل فیک ثبت نام کنید و یکی دیگه بسازید بیشتر از ۵ دقیقه کار نداره
بازم عذر میخوام باید شخصا تحقیق میکردم</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIR6O_9IwtTqKpYQpodZ58Q2mJvYa-ICtpNyajhTqvN9S4AEW0tLYvezf5vbl_q2CkZdpID8pKnYs_8T8RYju5TKhJbtNLYjByLP1dLZXua9u-ISI8FeIMJeUXM2DcecK0cJ3zcA_8OZeGRvnhP5NHEyrSF3Ph51sWedqle07XGpyLLUloZh8OXDZRbC9RaCSCg867QnV1lSxs2qk_o8G1eKRcb88Ds3CeorsxmAPVE69jK--EInQewr7d6L7WctS8oZgStpcZG6ZqFVbkJ2nMMxwTRxoZjOmNuxWnil5ANh77JP_5_4X5zxrIP4AATxCuQLlXxT7lg7sF21JGAdvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=SGbe1ZAX6yM3XAk8akPQNo4CjVkkY_-y7bSoCqvG36MlrhCyJcXQSdxPS336Aa4P6SSnFTrlVhgPK_7d6ZCq4RCBgYy0HuGgf7CS3oxbAz9sLFYfXbz6s5gINSZnA8YrOMYPNmy0Xfp1XdQyb6daOrHasXJ-_XyeEY_p0Pfw4Z64IdqzhviZSmS81wKJoCYU-KSLbP6nX5_qXxsNAxFbJYTMcJ77W2F3l0Qe6KsVWGzdOn52dgJCyTnliS0krdIy5VsvthRC_dmj2Hy_IOpmI9TZm6sb1VgnXSfVXgqhjnAzQnrLeiV1v-FLD_bsxjwrT1sauZmEARibLPDmi_LuHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=SGbe1ZAX6yM3XAk8akPQNo4CjVkkY_-y7bSoCqvG36MlrhCyJcXQSdxPS336Aa4P6SSnFTrlVhgPK_7d6ZCq4RCBgYy0HuGgf7CS3oxbAz9sLFYfXbz6s5gINSZnA8YrOMYPNmy0Xfp1XdQyb6daOrHasXJ-_XyeEY_p0Pfw4Z64IdqzhviZSmS81wKJoCYU-KSLbP6nX5_qXxsNAxFbJYTMcJ77W2F3l0Qe6KsVWGzdOn52dgJCyTnliS0krdIy5VsvthRC_dmj2Hy_IOpmI9TZm6sb1VgnXSfVXgqhjnAzQnrLeiV1v-FLD_bsxjwrT1sauZmEARibLPDmi_LuHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک پروژه متن‌باز جذاب برای ساخت ارائه با کمک هوش مصنوعی!
دیگه لازم نیست ساعت‌ها برای ساخت اسلاید وقت بذارید؛ این ابزار رو می‌تونید روی سیستم خودتون اجرا کنید و با هر مدل هوش مصنوعی دلخواه، پرزنت حرفه‌ای بسازید.
✨
ویژگی‌ها:
🔹
پشتیبانی از OpenAI، Gemini، Claude، Ollama و مدل‌های دیگه
🔹
ساخت ارائه از روی متن، فایل و اسناد
🔹
قالب‌ها و تم‌های قابل شخصی‌سازی
🔹
اجرای کامل روی سیستم شخصی
🔹
رایگان و متن‌باز
🎓
مناسب دانشجوها، مدرس‌ها، پژوهشگرها و هر کسی که زیاد ارائه می‌سازه.
🔗
Github
#OpenSource
#AI
#Presentation
#Productivity
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🌍
افزونه Local Translator
؛
افزونه‌ای متن‌باز برای ترجمه صفحات وب بدون ارسال داده‌ها به سرورهای خارجی.
💡
اگر دنبال جایگزینی سبک و خصوصی برای مترجم‌های آنلاین هستید، ارزش امتحان کردن را دارد.
🔹
ترجمه کامل صفحات یا بخش‌های انتخابی متن
🔹
استفاده از Translation API داخلی Chrome
🔹
حفظ حریم خصوصی؛ پردازش روی دستگاه کاربر
🔹
دو حالت نمایش: جایگزینی متن یا نمایش ترجمه زیر متن اصلی
🔹
ذخیره خودکار تنظیمات و فعال‌سازی خودکار
📎
GitHub
#Chrome
#Translation
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGibR8LnYBisHXNTXNQIv1Q-PugoNgAxLq_HoOqFeus_OtzwFqZl44CAn9vyPcHEzORAcgxZotd8RiP3BjWjCLz2Vbq6tR20YyeD1zYr_QQGDiJckdOXSBSMkTZ3O1tI3IGC8mSscywQIjDzaxDwTZ_MSsd8Xuy8oMj176yBFHWoRM6APt17TrBtEbaVPauR2_06Wik_jRlgGWoTy95EIV5HYiiD0Z3V3_PBTXpR_KRQ1-5rK8fB51qUC6qYtCgJ67sByNq9jCQ6tpGeo6n_QWzEgy2qN5zzlHCejDT6CWt5YbolkyWAz9wBN_lkzrbIPMORatPiiVE-JhW5i7a-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با افزونه SkipBait میتونید ویدیوهای یوتیوب رو سریع خلاصه کنید و دقیق‌تر داخل محتوا بگردید
🎬
✨
قابلیت‌ها:
•
🔹
خلاصه‌سازی سریع ویدیوهای YouTube
•
⚡
جستجو داخل زیرنویس‌ها و متن ویدیو
•
🤖
پرسش‌وپاسخ با هوش مصنوعی درباره محتوای ویدیو
•
🌐
پشتیبانی از جستجوی وب برای اطلاعات تکمیلی
🔗
لینک
#AI
#ChromeExtension
#YouTube
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
گزارش‌های تازه از پیش‌نویس توافق آمریکا و ایران
🇺🇸
طبق گزارش Reuters، پیش‌نویس یک تفاهم‌نامه موقت میان آمریکا و ایران روی چند محور اصلی می‌چرخد: توقف درگیری‌ها، بازگشایی تنگه هرمز، کاهش فشارهای نفتی و آزادسازی بخشی از دارایی‌های مسدودشده ایران. همچنین قرار است درباره پرونده هسته‌ای یک بازه ۶۰ روزه برای مذاکره باز شود.
📌
با این حال، Reuters تأکید کرده که این توافق هنوز نهایی نشده و بعضی جزئیات، از جمله رقم دارایی‌های آزادشده و شکل دقیق رفع تحریم‌ها، در گزارش‌های مختلف متفاوت آمده است.
⚠️
فعلاً باید این خبر را در حد پیش‌نویس و گزارش رسانه‌ای دید، نه توافق قطعی.
#Iran
#US
#MiddleEast
#Reuters
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
احتمال بازگشت Claude Fable 5؟
بر اساس گزارش برخی رسانه‌ها، کمپانی Anthropic تیمی از کارشناسان خود را برای مذاکره با مقامات آمریکایی به واشنگتن فرستاده تا محدودیت‌های اعمال‌شده روی مدل Claude Fable 5 را کاهش دهد.
📌
گفته می‌شود این محدودیت‌ها پس از نگرانی‌های امنیتی و گزارش‌هایی درباره روش‌های Jailbreak و دور زدن مکانیزم‌های حفاظتی مدل اعمال شده‌اند. برخی منابع نیز مدعی‌اند که امکان عبور از بخشی از محدودیت‌های امنیتی Claude Fable 5، یکی از دلایل اصلی این تصمیم بوده است.
🔹
هنوز هیچ جدول زمانی رسمی برای رفع محدودیت‌ها منتشر نشده است.
🔹
در صورت توافق، احتمال دارد مدل با لایه‌های امنیتی و محدودیت‌های بیشتری دوباره در دسترس قرار بگیرد.
🔹
کمپانی Anthropic تاکنون جزئیات کاملی درباره آینده این مدل منتشر نکرده است.
⚠️
فعلاً تمام این موارد در حد گزارش‌های رسانه‌ای است و باید منتظر اطلاعیه‌های رسمی از سوی Anthropic و نهادهای آمریکایی ماند.
#Anthropic
#Claude
#AI
#LLM
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qfv3dfLdEwj3smDymuIgD2IpO8eGdR3pnGYmr3w7iagnL4tWISs5QntRx9PUK4nInlOVyWm8BG5Jg09uknNNh30lLynv2xMQdgnpD-xbU5oJbWXzbcqoRBeIvgK3-p7wVkbU5LbMBfIBdkGToG7eR3Pu-reKRt7UuPANbdVxwt5raz-5QAOI1PLFCTtrBkY8ojRrsioZbPKOqppRoFaNHS45P8NxcEIWM_cYdZuXL5um9zr-ICYzFPpK_h1X8Sp2YrEHj__OyZ5EN8FSOeVg2Vd0xRkfasoNc4yACVaXBMcy129i8SQ6fSEPp3RKbNFjwfWXo3f_tdMUYI__dKYfNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: آلمان
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 21/30
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
آلمان
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 21/30
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIrUEd3PFZRacZlV8g-V_0yowDhFjvAhICxKZW8EmixlfJ7D5hZEsD0aTzZkhnPRPJW-37cvIDU2og9yOTmSELyF7ISHiFLng-buMH0xZXam7YBCv_Z60fYvL84CS1u7xV77s5oU_YEIf3L8K_bWeepmhG3JdHpqqD7bkd8eey7hqxPr0Zjy2EKGzQUtJAnz1_Emro0R0bWhYg9fvpmi6TdAwsu6ckjPhbj7931p7lvG42_Ei1Po6AV3SjFDcU9PnIRiKp8YqnpqXCzbdTa-UWTCmsNg5ET8WZmtVXlj36qStPjC04xBS8X6FfMe8kU8gFnLqZMz0XXl9bQXqxHrMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل جدید
GLM 5.2
از چین معرفی شد
توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و Agent
🔹
هزینه API بسیار پایین‌تر نسبت به برخی مدل‌های مطرح بازار
🔹
مناسب برای کدنویسی، اتوماسیون و وظایف طولانی‌مدت
🔹
دسترسی رایگان از طریق محیط توسعه Zcode
﻿
📊
برخی گزارش‌ها نشان می‌دهند GLM 5.2 در چند بنچمارک حتی از بعضی مدل‌های پرچمدار فعلی نیز عملکرد بهتری داشته، هرچند نتایج واقعی بسته به نوع استفاده متفاوت خواهد بود.
🇨🇳
رقابت بین مدل‌های چینی و شرکت‌هایی مانند OpenAI و Anthropic هر روز جدی‌تر می‌شود و GLM 5.2 یکی از جدیدترین نمونه‌های این رقابت است.
🔗
ورود
#AI
#GLM52
#LLM
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚀
ساخت VPN شخصی (VLESS) کاملاً رایگان و بدون نیاز به سرور (VPS)!
اگر دنبال راهی هستید که بدون پرداخت هزینه‌های سنگین برای خرید سرور مجازی (VPS)، یک کانفیگ VLESS اختصاصی با پنل مدیریت حرفه‌ای داشته باشید، پروژه
REN Gateway
دقیقاً همان چیزی است که نیاز دارید.
این اسکریپت که توسط یکی از توسعه‌دهندگان چنل(AssA7778) نوشته شده، به شما اجازه می‌دهد پنل و تونل خود را مستقیماً روی هاست‌های رایگان
Render
راه‌اندازی کنید.
📌
ویژگی‌های جذاب این پروژه:
کاملاً رایگان:
نیازی به خرید سرور یا دامنه ندارید.
پنل مدیریت حرفه‌ای:
دارای داشبورد برای مشاهده مصرف، ساخت لینک‌های VLESS متعدد و تعیین حجم مصرفی (مثلاً ۱ گیگابایت برای هر کاربر).
ضد خاموشی:
دارای سیستم Keep-alive داخلی که هر ۱۰ دقیقه پینگ می‌فرستد تا سرور رایگان شما در رندر خاموش نشود.
پشتیبانی کامل از V2rayNG و NekoBox.
رابط کاربری دو زبانه (فارسی/انگلیسی) و حالت تاریک/روشن.
🛠
آموزش سریع راه‌اندازی در ۵ دقیقه:
۱. وارد لینک گیت‌هاب پروژه (در انتهای پست) شوید و روی دکمه
Fork
کلیک کنید تا پروژه به اکانت گیت‌هاب خودتان منتقل شود.
۲. وارد سایت
Render.com
شوید و با اکانت گیت‌هاب خود لاگین کنید.
۳. از داشبورد رندر، روی
New
و سپس
Web Service
کلیک کنید و مخزنی که فورک کردید را انتخاب کنید.
۴. در صفحه تنظیمات این موارد را وارد کنید:
Region:
حتماً روی
Frankfurt (Germany)
تنظیم کنید تا پینگ بهتری بگیرید.
Build Command:
pip install -r requirements.txt
Start Command:
python main.py
۵. روی
Deploy
کلیک کنید و ۲ تا ۳ دقیقه صبر کنید تا آدرس پنل به شما داده شود (مثلاً
your-app.onrender.com
).
🔐
اطلاعات ورود به پنل:
آدرس ورود:
your-app.onrender.com/login
رمز عبور پیش‌فرض:
admin
(حتماً بعد از ورود از بخش Security تغییرش بدید).
حالا به راحتی روی گزینه Add کلیک کنید، حجم تعیین کنید و لینک VLESS اختصاصی خودتان را کپی کنید!
📥
لینک پروژه در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎁
دریافت اعتبار رایگان API برای مدل‌های هوش مصنوعی
سرویس AeroLink در حال ارائه اعتبار رایگان API برای استفاده از مدل‌های مختلف از جمله Claude، GPT و سایر مدل‌هاست.
💰
اعتبار اولیه:
🔹
ثبت‌نام عادی: 35 دلار
🔹
از طریق لینک دعوت: تا 50 دلار اعتبار
⚡
محدودیت استفاده:
🔸
حداکثر 10 دلار مصرف هر 5 ساعت
🔸
حداکثر 70 دلار مصرف در هفته
📌
مراحل:
1️⃣
ثبت‌نام در سرویس
2️⃣
ورود به پنل و ساخت API Key از بخش
New API Key
3️⃣
شروع استفاده از مدل‌ها
🤖
لیست مدل‌های پشتیبانی‌شده
🌐
ثبت‌نام
⚠️
قبل از استفاده، شرایط سرویس و تاریخ انقضای اعتبار را بررسی کنید.
#API
#Claude
#GPT
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXQtmETcMwm9_KX4QBjokQQZ-rQy_DXdWxsBIHpWd5R8fDHWouEsZ3tuyfVUOW44vv1u6d-iZWe9kVWYaV1xGC75YWoX5oN45TPMBNbmiaTpmHpAY7KKvSYPHm7Lmy-_yw1FNqOKwcB-POj8tw6ywGFDKwMmQqQl3S8xruRhkDTBHXGN386MiEiWajt2m5cofTHBtb-i1x9oS7lJ_zZfr2pQWZXkAm1_zYsYzk2trC0jmrST93UUzLv1qf7-G7U2ygCcpO5mgevpyxvS9ve5dJ5LP911o28bAz5MJcqXeYLST57lYN0PcoGBhqrV7ohT-V4bXZpjep8Mv0OxJb_k8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
OpenRouter قابلیت جدید
Model Fusion
را معرفی کرد
حالا به‌جای تکیه بر یک مدل، چند مدل هوش مصنوعی به‌صورت همزمان روی یک درخواست کار می‌کنند و در نهایت بهترین بخش‌های پاسخ آن‌ها با هم ترکیب می‌شود.
🤖
برای مثال می‌توان GPT-5.5 و Claude Opus را به‌صورت موازی روی یک سؤال اجرا کرد و یک پاسخ نهایی و بهینه دریافت کرد.
✨
نتیجه؟
🔹
پاسخ‌های دقیق‌تر
🔹
تحلیل‌های عمیق‌تر
🔹
عملکرد بهتر در برنامه‌نویسی و مسائل پیچیده
در واقع Model Fusion شبیه یک «اتاق فکر از چند هوش مصنوعی» است که روی یک مسئله همکاری می‌کنند.
🔗
قابل آزمایش در OpenRouter
#AI
#OpenRouter
#LLM
#GPT
#Claude
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100GB
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 43/64
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSQ-1xwKWvMLLd4yjWGaPx67W-KmR9oJ232xJC3MmaKe4aWEtgGzQXzgPQB8i9F_Cb0vf208NieHFmEyOmOHOiGtu9QggG6HjPK-X4pi23iXViYtTIA-vxk7DdVNoalAiQHUkkdtVEzBXpu9N1ZAy1sTVMNz4ntYmfgh-t9vfgG6dHCR1lhwL2X4yJxZa4iuz2mj7e9sh9LVUFZ5Do0eIGRhW_xxDfN5VHWXbrKTNJInUigB1DPQNg-9Jh5ghYez10yj3dWRxUZC5T7iygPCdpQ_6RfhzhsfzFsHlnCvKsd8BNulzI05Q5u8RW61rbbKdQ1PKjxCdNVnd_T-QuJ5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4hirpBhB1lX4XmX7vF1vNqhPJQQM0VUf_rnXhHKwzL-H661sYwzXnE5cq1MgWMyJHB3toK0DzY0-fJuaI5yGqNyytJhhSKAy_RMUibXAzBTpmkv8s6Yyn1dLGOlARCHPrktXLU-ztqXBZY8foM6aVO-3UJUNJmoS0zP1zKPEEEBE1Vi58ROcXzoSHoRnEj3wXDrMgfy42BSurCcmqdt_ytNWHbqaRWCGEMhDxR6a8teienMt_pfkb_MSv4NFnS4C6P5UrE_kW_gWo04IE7y-ZOCI-uos6APd5J2V1ZinGRIMywjFPFWPY-WoVfwkT19yHhfHtaIedNANaxkylJx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه که هوش مصنوعی هم جلوش کم بیاره!
📖
متن چالش:
"Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time to get to sea as soon as I can."
🎁
جایزه ویژه:
۱۰۰ گیگ کانفیگ اختصاصی با آی‌پی ثابت آمریکا
🇺🇸
برای کسی که ترجمه‌اش یک سر و گردن از ترجمه ماشینی (AI) بالاتر باشه!
*(نکته: اگر تعداد ترجمه‌های شاهکار و برنده‌ها زیاد باشه، جایزه رو به قید قرعه به یکی از بهترین‌ها تقدیم می‌کنیم).*
⏳
مهلت ارسال:
فقط تا ساعت
۲:۴۰
فرصت دارید.
👇
نحوه شرکت:
معطل نکنید و ترجمه‌هاتون رو همین الان
زیر همین پست کامنت کنید.
ببینیم چه می‌کنید!
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTIqoV11DrB6ltuFx21zC4US1ib4Xqx1Fwu55lvZ1plbKc8kKgxqx80p81UrQfotFD6PBO8_ZougsaKMm_ojtvFXyGvwSfg5j5FxcUnceU78zL7IURDiIBcXP0DWBxz40tEmvD1N7oJN9ixRBMOoYIshWLXR9_sqNo3gU5YI7lUqICELb5bmOr5VlIDyaOeoeOHYgVpPjQX-5MPNL4ArM7YaexHCdi6QSFxSQpt4OsfTMjX2wUw7DyAmLW0IJ6gZQWiipkkFgsE30KEqsMMtZrgRsUy2p0EOeY_gPwrRagmmw6fUp-3JpeW910_EL3R5sMPN8vjQEM6V-M4SmriPLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OX-HyHKxOLjftY-WCX4CpK0tJ8TJD7MIKn9ImTEdD-Q2YQXSPkSzGWJG_7sXaoXIpx7n9zftCn8UONoxzKlT2N8y20_MVzia-RZTkKx422TBWZXGxRcTgaT1RAHxIT-mml-12dj_ovxlrxM1kkvDjM67UOp8XKCV57SKQtbnBQJdgHh8HGndAbuxrZmxFuLkkHnbqBJqo__3Vu880WsZDcnNUeygnz6fIOBwDgY5zWSnlZMBRoxxyOQAb_jhlWc6_IgBrj1rIJYHssCclccHO7oZZuxw59xv1yTEzXXhSWvUF3Ca5zjvnbEazAXn-zW4jlBmd332pEcEQSdt4Xhvmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن»
یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like it was never there. Match the background, lighting, shadows, and colors. Keep everything else the same.
#Chatgpt
#Gemini
#PromptEngineering
#PhotoEditing
#AITools
#Design
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ0SSshAZDhXS0qzmPXUQOiTkvJhLT9CB2abRyT8Xf4GmwFOp-CLm-_qBuiCWX1O-q9Cvm4djFShXhVhxQPXc4oj6LcMLmotifslcb-MI2swTbj2GXaHLremqI2JJekjvgnoQcEBeOnOjOBzc2-SVM5GuROkUpaak4cRhaNtPBkOZLjbw9PHi3DY6kt6dK_pglNN7EVOSw4-cBaAVHpAy1HuF5ubVQh5pruoRjpYhlzcH678EUTVeqXlI3iLytv-BUbEzFEYAE0HW5yG3AHgoDuYwNnthHBMFhTO3AVv8PGmgZLA44t9kAUrj7PedfBjLTeOv25QGGNuCl2j34xx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMed8NKDkbi-jLEUU87ZBgwUZJURHWQNeLAD0LXOGgMOssiYepgCP6Faa7kHLAF2_Kz0_ZwpsDqoj23pnVRZ9yb92fGd_jVD1NLBxtGcjG2wDqki-J66Dc9ejmKkJWvTwJbycK1cl_y-cHkrEozIBiIm06g-GciDHFJvHMUQjIgW1DqrCex7AZbx0IS5td2B7feYhxpZDM-muVmQIxVXVzjNo6DBUsPxcDTLky3vdRZ9NvvNzsuoRjWZUsE6jhhzvgvp6WQyEXGBXuJxzqiktRtlK7MXoLUmCWCiwdWWTA0VKU20yho4IMsH5IUxuhRZswBmW4xZeyldOLMcX2iSeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
روزانه 6 گیگ کانفیگ رایگان
🟠
پنل BPB کلودفلر
🔹
با جیمیل لاگین کنید
https://dash.cloudflare.com
💻
در ویندوز نرم افزار BPB Wizard رو دانلود و باز کنید
https://github.com/bia-pain-bache/BPB-Wizard/releases/latest/download/BPB-Wizard-windows-amd64.zip
🔹
عدد 1 رو تایپ کنید و اینتر بزنید (اجازه لاگین در کلود بهش بدید)
🔸
لاگین که شد بیاید تو پنجره برنامه گزینه 1 رو بزنید و ورکر بسازید
🔹
تمام سوالات رو بدون تغییر اینتر بزنید و آخرش y رو تایپ کنید
🔸
پنل که باز شد رمز دلخواه ثبت کنید و لاگین کنید
🔺
تنظیمات پنل
Common
:
ipv6 رو خاموش کنید
VLESS - Trojan:
- در بخش
⚙️
Protocols تیک گزینه Trojan رو حذف کنید
- در بخش
🔓
non-TLS Ports تیک عدد 80 رو بزنید
✅
بیاید پایین و گزینه Apply رو بزنید
🌐
دریافت کانفیگ ها در بخش Subscriptions :
- گزینه Raw (without settings) رو بزنید و دکمه کپی رو بزنید
- لینک ساب رو در v2ray وارد کنید (میتونید لینک رو باز کنید در مرورگر و کانفیگ هارو کپی کنید)
🔵
@ArchiveTell
|
#Mz</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8euwPZYtJkk9eEB2GDoa2T3Y2lZxnMOy2cgVKyfozmA6ogp8HszeGWLAzJ4ZzjYqM3WfBX8PivEIpASmLQBe9OAP0GmhBpoo8lHVocgOnSuGjPjaNscUz5zwoRBH0Apr6eq-C2lb-zMK342JIGLgJMLJnQ7KTl-HCImQaNnBJkrCNzg-vrfm79wW7OSNDoX9GHdu6yy-JnOW7nbmGbx127XyF6EW2uD63Ya7KncOA_vKWx9UBXLJjqTVle57Sfy166ye8Vx3LUGCmt5QIcSoAAr8eSZkKVrjxnMxTKE7pES_G0vVBg68PjGx43tEZCFE1ayu-RIQfMBPluQS1xAfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😬
کاربران Gemini از محدودیت‌های جدید گوگل شاکی‌اند!
ظاهراً گوگل بی‌سروصدا سیستم سهمیه Gemini رو تغییر داده و حالا حتی بعضی درخواست‌های متنی ساده هم بخش بزرگی از سهمیه روزانه رو مصرف می‌کنن.
😶
🎥
بعضی کاربران می‌گن ساخت یک ویدئو می‌تونه کل سهمیه روز رو با یک پرامپت تموم کنه!
👀
«جاش وودوارد» مدیر محصول Gemini بعد از موج انتقادها گفته تیمش در حال بررسی ماجراست و احتمالاً تغییراتی اعمال می‌شه.
📌
اگر این چند روز حس کردید سهمیه Gemini زودتر از همیشه تموم می‌شه، احتمالاً تنها نیستید!
#Gemini
#Google
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=fdbJrrSlIUQwUfLJWG3thnE_8-UNtL6qcsVxU-k8sXbaRUSSeMYvO8dAIorRxhOMKCbT8Xz5hX4mhjYx_ETihrwgV3IWew1xd4iLHNhZQ1xuzfA9ECqDlCbDMMS6A3BPc1V2A2sTcyxeT-wmR8QlhiH73Gt8-IMlPYRw-gX12XY9SgvisbhyKVmZyFnY4dREdWB4zBTGuWqzG3FnlxHlturXG7jPREOCyA8A7rT_ERb_XI8KfDioh_fBLUVEN-SJR1M0J6oVmCNicqtaDRd2vwbCy-jGny4IjOrePqJ8FgvKRZwn097VQg91CLQJFWDOE3q1i0oLM0BToF_9gVp7FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=fdbJrrSlIUQwUfLJWG3thnE_8-UNtL6qcsVxU-k8sXbaRUSSeMYvO8dAIorRxhOMKCbT8Xz5hX4mhjYx_ETihrwgV3IWew1xd4iLHNhZQ1xuzfA9ECqDlCbDMMS6A3BPc1V2A2sTcyxeT-wmR8QlhiH73Gt8-IMlPYRw-gX12XY9SgvisbhyKVmZyFnY4dREdWB4zBTGuWqzG3FnlxHlturXG7jPREOCyA8A7rT_ERb_XI8KfDioh_fBLUVEN-SJR1M0J6oVmCNicqtaDRd2vwbCy-jGny4IjOrePqJ8FgvKRZwn097VQg91CLQJFWDOE3q1i0oLM0BToF_9gVp7FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">WhatLetterAI
تصویر را به متن تبدیل می‌کند و به هر زبانی که بخواهید پاسخ می‌دهد!
📸
🤖
✨
قابلیت‌ها:
•
🔹
تشخیص متن از بیش از ۱۰۰ زبان
•
⚡
استخراج متن از تصویر و پاسخ‌گویی هوشمند به سؤالات محتوا
•
🛠️
دریافت خروجی به زبان فارسی یا زبانی که انتخاب کنید
•
📦
پلن رایگان با محدودیت ماهانه برای ترجمه و پردازش متن
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbUEaohUfiXqm5clKtrT9Pe7bedcP8qGp_JxsblV-H4XjNjgTkhGXFBxCLeesbdg9JPkKp14Rru5U2nam38yCuW6J3QefX0ZMS-h1HF-4bwT4T8oKqSsTxMUyiJAdYZgvh4cB0t0ZOWQXGMk6Z6BqKjgv_GmA2cXEnxYZNpBc97gPQBdcp6rjT9rZzNgSuuhqYHD1T0rh05P6BXoPrSt1Dh38bmt_hsz4_L5ZLl8Oa8KLn515GCUivjSIQ2EAOk3hnxIoAb6Rh0geFAwa0oKXynV7Q-pbRYdkKKjZYMzqHK1TlDkP8c0q97TJ939YXhbMlsq8Tm-e9oNc4-2ZcKf7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تولید رایگان تصویر هوش مصنوعی
🔹
بدون نیاز به ورود
🔹
خروجی سریع و بدون واترمارک
✨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhcspozAxh65VWyL9CiLmALU7_DYiFGuof2Wrz6dD5HP9Oq77Ta24Y-_DdwJPkxDuVit6-p-fHer-ZLr1oxHCFUVxyB32lbx-pxMPet72vYP-dSaY0Az7MowNfPMN7zQWy3cVK9j6s-ixY_aWLCE18he9ADXou-brzRLI2Z0bDvFOXZ8XoJ1ESyjyqP3O4jYxBJnFIWj5FQucSsfCn63_5Zos1ax-kz9UORZ0AitrjGuXPXfEiPKTWCXOWSSQDz67XS-EklojtV4ZRWk-YgmoilnLILNW0e3Su1jWufATf_wh6440qdkFKv9AVAS0vCFxIQnyzmJyUFPSDqBNMHStg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=q3Lbe4UG-41qDT6PJCJceHkjH7IJMXccMdOk9bIPq4xQ0ZT3VSjowC7Rjbaj_5UUPTfwhxFLFvNYg1aK69j3ySmKUVptaSAunvl7ka98UMPPO_MC3B-8D_OOcArBkNNhfXseUGRlu1EfL17BiXXMCJMQGbBKjky5au6D63x0j5618364_6L8kXonUleRtGqqC_fTJNEf1UtWnx8eao7DzNA9Fn754jpte6jWVbn_JSXXwvdBdfYuVtFgSSgh4rRSW06OBZN0AaZhC8O576nqx74kALO6QXmN8m9Mf2DETMyxa1KLBQIuc_iExSMiuo2rq0VMuEJ2trV2_c-MCX4l_Bfmd9r4iPkNSvTzZEHBJYd1iv952I9T6ftCKn3-nUKL_yAAMcymHcXDNxC0Lb-NUEVIupbR9xcJ0uzm5t3k1yWMwH3HQOBP_70oNr4VgOFbA64cjC8NLcejoKVNDwxyzUS2JnZBQjuAGhS4KlI-ue13PNqMOJtNKrEv_ikUiDJzxPq7l057tnlWVCxq91JDJSoIinD8eOkDJoAV1sgQQ7rRldFfXQmUMnKcyt2DtNHTuPsCcPARKExDN4IFbfgomYfiuEb6Hk7pIhXhkPvjKthCOBWWqcinBT4fEbNFj0OkSIFit2X7LWZ9GxRCb3ihJPo4ZrX3qmKPCA2u1i9fiG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=q3Lbe4UG-41qDT6PJCJceHkjH7IJMXccMdOk9bIPq4xQ0ZT3VSjowC7Rjbaj_5UUPTfwhxFLFvNYg1aK69j3ySmKUVptaSAunvl7ka98UMPPO_MC3B-8D_OOcArBkNNhfXseUGRlu1EfL17BiXXMCJMQGbBKjky5au6D63x0j5618364_6L8kXonUleRtGqqC_fTJNEf1UtWnx8eao7DzNA9Fn754jpte6jWVbn_JSXXwvdBdfYuVtFgSSgh4rRSW06OBZN0AaZhC8O576nqx74kALO6QXmN8m9Mf2DETMyxa1KLBQIuc_iExSMiuo2rq0VMuEJ2trV2_c-MCX4l_Bfmd9r4iPkNSvTzZEHBJYd1iv952I9T6ftCKn3-nUKL_yAAMcymHcXDNxC0Lb-NUEVIupbR9xcJ0uzm5t3k1yWMwH3HQOBP_70oNr4VgOFbA64cjC8NLcejoKVNDwxyzUS2JnZBQjuAGhS4KlI-ue13PNqMOJtNKrEv_ikUiDJzxPq7l057tnlWVCxq91JDJSoIinD8eOkDJoAV1sgQQ7rRldFfXQmUMnKcyt2DtNHTuPsCcPARKExDN4IFbfgomYfiuEb6Hk7pIhXhkPvjKthCOBWWqcinBT4fEbNFj0OkSIFit2X7LWZ9GxRCb3ihJPo4ZrX3qmKPCA2u1i9fiG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎵
LoFi‑Engine
ساخت رایگان موسیقی LoFi برای خلق فضای کاری دلپذیر!
✨
قابلیت‌ها:
•
🔹
تولید محلی قطعات منحصر به‌فرد LoFi
•
⚡️
صداهای طبیعت (باران، باد، دریا، پرندگان)
•
🛠
تنظیم تصویر و طراحی فضای کاری به دلخواه
•
⌨️
پشتیبانی از کلیدهای میانبر برای کنترل سریع
•
📦
کارکرد آفلاین، بدون نیاز به فضای ابری یا اشتراک
•
💻
اوپن سورس، سازگار با ویندوز، لینوکس و macOS
🔗
لینک
#OpenSource
#AI
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=eQEnGj_HMqyTImTGytgbl1vDrVxEb6dqz1FiBbJH7ulrVnsbWiAylhXq4sidXpOuFgSkFFMRdT4nDKmlgeOWHTOkYfQUOnjB97nf8GO29kZLtZ5g1gpVZjjnJ01jHvDVJyoFiJKu772Y32NCWm0qnBPCwXye0L3Je8B7wtEUvo7UWdBeG1sfCfqxG7RC992HzzqTbGyBwv9OYqg9kI2PdQup32eHcgbnYty-pzFEnIkgI6Tj3Lt1Tywo_Iihw250d18v67oIwmTqTirwfZkCn_I5Cq_2JpVmCwPFKUBhWArKw68msNgqzBjW5w3AtvQ878Up0p0eh2oeEhb2iZIwwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=eQEnGj_HMqyTImTGytgbl1vDrVxEb6dqz1FiBbJH7ulrVnsbWiAylhXq4sidXpOuFgSkFFMRdT4nDKmlgeOWHTOkYfQUOnjB97nf8GO29kZLtZ5g1gpVZjjnJ01jHvDVJyoFiJKu772Y32NCWm0qnBPCwXye0L3Je8B7wtEUvo7UWdBeG1sfCfqxG7RC992HzzqTbGyBwv9OYqg9kI2PdQup32eHcgbnYty-pzFEnIkgI6Tj3Lt1Tywo_Iihw250d18v67oIwmTqTirwfZkCn_I5Cq_2JpVmCwPFKUBhWArKw68msNgqzBjW5w3AtvQ878Up0p0eh2oeEhb2iZIwwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
Runway
با چند کلیک، عکس ثابت را به انیمیشن تبدیل می‌کند، رایگان!
🎞️
✨
قابلیت‌ها:
•
🔹
پشتیبانی از تمام فرمت‌های رایج تصویر (JPG, PNG, TIFF…)
•
⚡
افزودن جزئیات گمشده توسط هوش مصنوعی
•
🛠️
تنظیم سرعت و طول ویدیو به‌صورت دلخواه
•
📦
خروجی MP4/WEBM با کیفیت بالا، آماده انتشار در شبکه‌های اجتماعی
🔗
لینک:
https://runwayml.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">uk-new_domains.txt</div>
  <div class="tg-doc-extra">21.8 MB</div>
</div>
<a href="https://t.me/archivetell/6351" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیپی کلودفلر
آمریکا انگلیس آلمان
با این آموزش اسکن کنید
https://t.me/archivetell/5657</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">Cloudflare Germany
🇩🇪
103.21.244.0/22
103.22.200.0/22
103.31.4.0/22
104.16.0.0/13
104.24.0.0/14
108.162.192.0/18
131.0.72.0/22
141.101.64.0/18
162.158.0.0/15
172.64.0.0/13
173.245.48.0/20
188.114.96.0/20
190.93.240.0/20
197.234.240.0/22
198.41.128.0/17</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">Cloudflare ranges
74.115.51.0/24
23.227.38.0/23
185.158.133.0/24
216.198.54.0/24
212.104.128.0/24
216.24.57.0/24
66.235.200.0/24
198.202.211.0/24
103.133.1.0/24
199.60.103.0/24
63.141.128.0/24
137.66.28.0/24
137.66.28.116
185.133.35.0/24
208.103.161.0/24
185.148.106.0/24
209.94.90.0/24
160.153.0.0/24
199.34.228.0/24
160.153.0.0/24
198.41.223.0/24</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nignh_GLwNzONc-TYfGtSas39zbUNR_iwRmm2U1hEmP2jomxVqUZs-xWZa52asY5fF7qWmI4U9m7RV4vmazL1WiBmgxYy1i4hvNfMq_hA5-rAC5DaITvquB73Gv5SR1n-4BphVSLAFxIiBsnUq1hRxW_AkmFzOA-CtsmwEkSvge9nYpvibYljbek4YUjJv8eqK2Ey84Ul9cVnHkIcQNBxzHlWp0wrgyS3vrQm74Z2Ew3Hm2tu28cFN8_EAspll83ueD-r2GlC7bUhMy6LxGI_pF-EyLi6ITM7CbA-DDj5GB0XMlEP_F52vthjtKBXZ-K7NMiJB8GGJyCV99o62SUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbmW76If_3mhv3t64IChir0XmAOXpj0_NJnLz5EGIb_P-aMBW1g4S_deNBPjsYxdx-61GCIs9sWHWTDmvjm-OCLcpQfOFIN4lYS1k9D6swZexiESNVpoTSx9qjjfckfXMB2kCGe2LQBgcy3czFxOSyntHxyBOInoMyaBGQIEIiAS83HIX-y-3eiRSuFCi1e4MTuGKe2p_9y1roCVov4hbm93cYW9VeoGyJKpesSD9KEItAGm_b2o43wbbIXMUIqtGfvSnDDdAcQszb1e60Ih616RXSHFUcozT6GnBQ8IjBynvHXhv_ZRYbGf_qRvED-bzhe4aQYz6EUjJrYLBBN1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AgGMy1Om3BMiGAq0EduhksEVP13-3C55uKRIQng2QSxd6AUjBe1zPczukNjmWrjYld5Cq1VSYNJgFC6NuuocYVIcxxwaV7SJTd4BUYT9BIDwCtVSW19vDfUNN8_zn9Ez_xusvQk-5MKSmMoKgdtxBA6cSAoXUWRdgfhEAmkEMXv2qdZgfUyQLoS698iGGHL_ZgTq_z-QeOrwnkj8mp6oDiTLbhwHbowNRCh1CAj_XMg7CtWtGDc8bjrpqEUWj6KTA1Y4iTGPpqKxzzTWzIB0amuQZ38VK4Q5sybb2RM10BiiT-VkHeDT1XsjGFaiqm3Uf3bFV7pgoYdHRgDofNc85Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fu9Iek5RoAD9fB71PmX_pVQXwgcSAjap_jjY2EVDAkHgpxFB9EelEmjI0BbG7rZP4uA1kiOaVAN5zQ_BZHf0ssb9mrTR3MMybPSJYZu8dc5Z3e1v448SIDJkrsCJ-VyS425aHfujwsdfPTXE_IOaDytZspmG08BOeSjj24sXpg1dQ7qT1LMLTkx0jAn2V3_R03ISKS_O-3N2-jaXcpjiZPA-GhhRXk1RUpcYA6Sz0F-tXBvDRsfaU3Vx4iAvuh9BT5fW4Nt590LdTkg1ukpNesJD_aNptk5PIUqdOMFF_kN3MPs_8_GNjsiIKyDrWr5PVTeqkQnc5IitbUU9aZ4jdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-EnUTx4pIlN8UxzhGi8TEJwNsRtk9oPI1kS4ENBPqwZj9eC7P0UdK8p5S0pV7RezY-BdCeVbIlxJcvSjTfTWwkf_4DCIUEkt5o2qfv1v1mi6LI8L6qkF0QsRiMznFR-3bEPchU96P94mLxuCdT3k2NB17JByjIHziJm0RW7of8K1YtwsdK58zhHV-y0ZdRaRRn0CgGmQALqtVlZwkrJeRqOCy3aCw11pVDvPL8XYA58pJSdchh9QPc6C6MFZs25YgAwiO1D6uFoW3OOcYnuyYhNZmqb1IobszcnwxkkZRNzw_hVxlX9elZ3Dt3j6Z2KRTboD1uBilLIy9fa3wk0Iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0iWdiYp80hOATm8Hk8jlU497tTmSuwWZN42J5ZvB49Mzy5BECh9OCfk5JleqPbpVXxu7SDTmdn0iZvoJFu13xmn9D0Sh5IcjXk3QLMdPcZWUYT9gIJ-zbRe-F2hQnzNkEjItqgfbKOf4QsAyBb1yxkkKEdwpSPnZ-eIEq_25GEOwVUCyPL1jnrNNAz3IfwEw1i_ex1Omhi64qzkMsOooe21bwJVSFryZwYY63Mh8fV8SeKwRzztHOuZ5B3Gk9R1V56t4hCoBhjCJyoFaPbq6ZltF0QDshJef_eKHvsFH8ZynY337rr9u3VRY4QusbIzVnpMDu3UEHBLPEu_Y5GGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_3z8bhBc-YwnGmYq2yzGh3f49CcjxWBqAcZ7ldNJ2xyh0Pz4RwCRjELnRcaj-5i2iTTJjJ3Ovc3kbUb2Pnb2IEu_ZGKLgVdpl6o-YZw1rYnU_I7g25z21yPQYb88WqtdgVRTuun5Enhn6YupLUp8Efn4WDciFIW0HJVghSKtJywRPX0_Ny1xZdi-Rxj5aaFQFshGJdGtuC_djIhCwXSWqTzRxpH7GF6zALKujCx-Cm_pEPzO9K4oCJxSyxJjqUzn4DZggr-t3-6fysRwwQ8NSIoGBCiwNXbt8iRiZ3DvEYVWdxacLQ4tn2HAAP68zhYELQQgNq29Pdkev5I_e4nbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpUXKlNe8854Mwly7E0K05CvXhr1W_0P-RLHku0plbp-P2oWi7bpf9k66tV0Kl8xEs9SlFf-6bPaKW4SYOHwfn9jw89ZQ-bFolw2EvJ9ZSWO5614hMSlFJJljRmh_AWQwYGAdJxpoUtxxI0_BqsgjphyOsGAXLumKTmFuHuM64xR6HS1XuD08mhmAS-H4jK0W6AGfJap1ZHt1rGJOgrM7sss96fZb26LSzQuURoG8M-Dr0UDQ9UqoFPLZZeja2B2Ad-zTX3PEm8tt1bEkw-kp5fXsMROhIaS6UYY1Za23v1E9MAIPLgIR0kTKUda7f0ov-udSRkVFH9p8dGxCId7HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4fBFKC37JZap2ijz6i9cwYvksqH6Rh1xK8FilX88v6D4FVuMnMHiruKTSRbTOMPzcfLMFnJtxkTxm8SjnT08oP2TF81JEQB_ZPmOYn0kPiCOEYBDA7LNqhZQdkfzzDpUolUddVDFeSPMmGNOxsbS4xQKxrRbicHZob0BelFse6rdLFQHy1HE0_dlvLHZvACwb4TTjnXH613hxFQSoisqLYd3Cj3ia_Gj__IXRKLuZXcAsBGIMOygrfmskOwrqLoP75J2Jlw4trntFJyHzLwu144YTsrqtREicpYOA3zjQj0ohAPvUvJvrFTruIQc-7nXWIPwMX9j2NEzXaF1n5YGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpH-UCyFTXSExH6FKBOmZ6DozssAQ-ao7T72w1vRSwuWdh6TEbdr0oJ_VjQgQe4XH0LLwewKgcZhEAweS51tpcNrBKYuhWJI5rNeSGAwxFuZfm-vsn5BzYT2LfANVaeyLjCxIGMG4hJQhAQpVOWrknQR9XFZKm-S_ysgInlNilxhCST0IqPbF025CEQqUXiNEzTh66fU6knCZG9j1_GpMGqC47x8T-bfxigRUiCF3g9Jm-EpjsgvsGtdEopJ596bw846-qBMPdyoTAim_9ohZ4GMoe38XL5HvodlTqKSG7TtgToDLkp7wxfu2bGCpZw4HFVe6bnYEaEu87KfcIUjgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU8DVgquAxD5wrYRjg1wRdwR_KXAUzqvpfsN33y5vgRISI6lkeINc3vfI0A1gIsQRX8HaM7QloX5BaKM_lKO3ewHD8misPzZkTfD8lYiuNVImCq6iGIfqUbpnqPljl92ivY2i8Ht4GA-jiVTRO1MXUj6Tx2wpedIAKRzLdN-QX8rhW3fUetcdJdjB301ApGJ9hmtntLYHo6Mmo2_GB67Nm-QSJ1UqVQkwYVC4RTbrIjY2TGxh2ls2NJlzHbOokpez54nEU11hIDU0thByhKmxFRi74TlgUlWQl6fhhK-KUAFsMha5MJgLpgtKYT49yMV6fEB4AyqXMeFQJaHJo-_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XI6et_RhKqwmdXYOjUT8KADL2dbmnMo9leYiNY_lNxNfC3CSZ8gn19HxJ_NwVKiXSVEKw6VlRE-v0n0m7yyG6069mbUN2Q_bnXgomUl4Qaw3A7-aH1MhgFkKQ6M3pexO6b12jPjvM_7wUCIKJQuQRSZ1YuJngAqUi3PJuT8WJuIZF97sgSkeyQvt_ZAfqAX5TdB1Vlm0WklfFcJkCrxNlmq-SW_mVL7_wEdtTCsMtOrUE6dGE_Sv6H0w0PXnyNVL7bng1L6yjqV473jbPqHOXzxMoAwMW16pVBLZ08T9err8xk57DX8U1tExcEl2eov1-7odlLz2z1GUvuZk403-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=IbU_u9PU35V1_ub5xftSn78tSbbxiDloggAQtSa5fo2bASrrtGrhTbN25gemkaiED8fV8V9uGBtb63YX9hWhk5X6Js709m60GMCDhzVXfreMFAoQw6mDuKiG3cXekmY5JczY2aWYVLSMKm5Z2lq6Vydf5BpU57n49UryCgC8sTOMP4ZzA872ByzULPGiScGp085B63U__1OYdJOmFGLE-CPQr8nL-aoSgRQUwUYgCbPOTTYitokTxbQ-3nGAcBENsbyxnLv8zVHhudl-8QhtKFOTMZ713r2iEZdxjGj4nGWrrauzAKwm3TfVfPMV0P0_cJvqE6sS33kx5RKA4o5WbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=IbU_u9PU35V1_ub5xftSn78tSbbxiDloggAQtSa5fo2bASrrtGrhTbN25gemkaiED8fV8V9uGBtb63YX9hWhk5X6Js709m60GMCDhzVXfreMFAoQw6mDuKiG3cXekmY5JczY2aWYVLSMKm5Z2lq6Vydf5BpU57n49UryCgC8sTOMP4ZzA872ByzULPGiScGp085B63U__1OYdJOmFGLE-CPQr8nL-aoSgRQUwUYgCbPOTTYitokTxbQ-3nGAcBENsbyxnLv8zVHhudl-8QhtKFOTMZ713r2iEZdxjGj4nGWrrauzAKwm3TfVfPMV0P0_cJvqE6sS33kx5RKA4o5WbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqtugyIpyL7lg1WXEAdjb8D27rmpfoxHpUac-mTYNFXVfDKlSPwO4bYe5eXGFtO6IK788lFVwYERG5Qky4ShUkKNXAxXLdVuHLtRui13ZVKUkclAfafa8lGNgFZCnuKPITr74eN5zMhCxp8zJR2XyhLm9hB77Q0wcdk_4bWg7V_t-q8UmtYacaK0T7yy7PO1h97KqCKhFmB7vCoAuIKjP0ZlYxmFmJouzU89SNFnt1mVdO1GFHsWeTC4wDGuhGEFJL9L_E9bJ1E75Kd158k2zpLVJc0Vdj-4gXz0QxaHCOl31E-vDV6lR34xUaLHachGoEz2rYGARxHpqBwLJpewmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7wwcsfOoKwTVSxFSy3kzbr93hZXHJSM2CTdki2uWbfx079e_pBRiFhiuw33E732toSJUjVNPFMCsZJ8Am13f0-7wiQvGH2RNon6XOOu3j0vmHy8miOgE3fuexc-mXLodvhpXwUCo-In7v344HqIpl0UBI5YvyMtLclUELiaF6Sn0aBSN0xoDf1Lz0BJp_-_YePHKVHQLiCub0I2zNVZ53arzhm7GwCbALfl5PxrX8TjYj4ZvELGkDZIhbbxfzNCMeY75gf4mxa-AqiFCrCTDralF1-JgZordu6jpmRkvOaBLBEPOXTNns6AnbtS06bQ7CIJqhXkPmcktgWjUA2yPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
-
لینک سایت در مرحله اول
-
لینک سایت در مرحله دوم
#GPT5
#AI
#API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7jKEVqEU57d3xucYCdMJ1ZaLOA7toetoRgwRqfbiPVhSZCTLxdRQBdDQeMIO_2R865qyaQD4_PBdbrTQ7vkpjLIfBsQXA_SamSoFv5799-ifM18sO5UrZteTO7V0n0l3XJPsip8LzO8f_mxwDrWG9sRJSmrCM4ueu-ofiYSs5ecI0PpB5yqSEpogTrXHSm_YUIckHCgKBm7GNaj--Kp1EZHxA0vIXoxahIXjgZx4eLHWX6KQGCSX9--5-4jZtg5DR1fgyPpR4QGQXQA2TjLzFnNo9znRPFdQVid8uSb_0DWhxeuz0s7opTKn1KgwqJgfTuZfe4-FUj7W4CpiCbzJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSL4_VedxNxhzKmJfTKZ_f-vXMbA7_po1zy6-F3WnxM8ExLHb9romjcp5VRnupCG2HNz16tEjiUOGDtqRLyqsL67B2qT_-8l-vTFWdH5jr76d71fJDlgPk4t5QLlT2yM1VYdGrCKf0uoBJgwIpK9ediznVKH7vIleyYdl-efU3dy-7MbbsBn6Co2D11_BAkTBRBWC9qCjLQfXVBnF3Pnkh5LLsL6CqrkMcckJ2vIPMB9qqgmsSl6HrIuKwAgIX5ib7L7yf-TVrhc2O3eEiDdNVgKA8iqqCMpuRDPJgF_oMlvdF_BuG-avr-jQRLrH120hcghquDWZ9o33XNPfk-3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت بازسازی عکس‌های قدیمی بدون از دست دادن حس نوستالژیک
📸
Repair physical damage on this vintage photo: remove scratches, creases, stains, and tears. Restore faded colors, rebuild missing details naturally, and keep the original grain, lighting, softness, and period aesthetic. Do not modernize the photo, oversharpen it, change faces, or make it look AI-generated.
#ChatGPT
#Prompts
#AI
#PhotoEditing
#Gemini
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=o6Cpz64Vb2Hs1tW2MaGRi0Pxhkz06ASTzXQutZUwpaXsXH9EV9shEvmEgn1wRZANE4lJD-0TW8m2QnI1AaNgqbu88HWvAFKhe9mEh-VAfXrUpk2TVowP_hvynTwvFvutv7Lvtm4KTRoJnJnQEafBYDHpexkvCy5Z8efwTfbOu_3qdRoY2u9Mg0VFcjJxGMrkhSTBx1Nvv7GpYs3i5IpmPyPnSrLHg4oTg28rrGxbDujzHmJAerdSrAG0WHFcRsFblVF8lsakKIhlWZpmxPFi68R4S6hR5xJ5T55jjKmlW7mySz7tqPfSC-Kh2u8ptrGSJPLDDC-m4uo5we-7fQqYSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=o6Cpz64Vb2Hs1tW2MaGRi0Pxhkz06ASTzXQutZUwpaXsXH9EV9shEvmEgn1wRZANE4lJD-0TW8m2QnI1AaNgqbu88HWvAFKhe9mEh-VAfXrUpk2TVowP_hvynTwvFvutv7Lvtm4KTRoJnJnQEafBYDHpexkvCy5Z8efwTfbOu_3qdRoY2u9Mg0VFcjJxGMrkhSTBx1Nvv7GpYs3i5IpmPyPnSrLHg4oTg28rrGxbDujzHmJAerdSrAG0WHFcRsFblVF8lsakKIhlWZpmxPFi68R4S6hR5xJ5T55jjKmlW7mySz7tqPfSC-Kh2u8ptrGSJPLDDC-m4uo5we-7fQqYSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
ClaimCircle
با یک کلیک، خبرهای جعلی را شناسایی کنید
✨
قابلیت‌ها:
•
🔹
تشخیص خودکار متن، پست یا تصویر فقط با کشیدن دایره
•
⚡
تجزیه و تحلیل لحظه‌ای محتوا و نمایش نتیجه در همان صفحه
•
🛡️
حفظ حریم‌خصوصی: پردازش در مرورگر، بدون ارسال داده به سرورهای خارجی
•
📚
پشتیبانی از چندین منبع اعتبارسنجی برای نتایج دقیق
🔗
لینک:
https://chromewebstore.google.com/detail/claimcircle/ominadfbilailbklmclcmdbpmckckdad
#claimcircle
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
