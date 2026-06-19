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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 23:41:36</div>
<hr>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 870 · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlL-DFNuxP4oeTEcZSH_d7UYw9E69hLwbUMdvY1fgXbGoNHMm4rz92ZDf631NmvV3usa3hVZfJHM3cNCqlnytibnqMHenXcqCpunWaWYMPfsvBtyiBVpHPn_JS9yWVISgsUxRYf12nAcq0UlvZinI1H5vr30c80lpnhJWrXEOHcN7TsrprPw0IddSQFQHL0Q5ZFYNIyNYZkzPZ-lrtzYVd05aYEh6R813lgRPW5FwQGsM4d3mVgxSS7QFXQsxA_OwwYDMae3BgzGDi4_qi4f7ovuS3f_ILESrYtGxd76huQOHImlRc2vtpnfF1fR2qJJ_DNgWuKMJ7s5J60Ux_rMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEuQIEbaakU1zr3ooaOx48JfjwJYMvhyfNQ3Ccg3J40pfhzaRTv2DvMj8S-18hR_5YWx2F6PBvFEivEzEJmlMnFynWcMLJ6BaHVwZ9lB7DCo6TibR73M2Pyi3dAucE-h6M6R_w3UwA1RXCnOpSfogembXmHyGm0Vc7UOXPx2MJmzBm0mMki_fz_W-3_WaGNhlgcJxrkAqkLrmu1N9XLlK4tGMW3wCKqoAa2hBxWdCkQqO46Cf9ANWbKbWR5ycp0wSA6c3UhHO7ub1AhCc0lqBFviRQd8tAhg9V2UdZXOm5y_zcqXU9n-gqcUGOrRo3GcByz_8y-B5pfIFtSnInd3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QK1ZiNG_Rz-mUKGyqJPCMBvUV-tSNY8Yi-AwNOxZTZKj9y_rDtQl3bCsED11eK2BkE45gYODDGHksdY_HD2mrwrpSW47RTssVI4P8tw1DR8ms6u_Y-wGNtqjnTb6s2z7k3QIcj0X5T5-sUoJp78AOmHl3uJVi2jZruZtM3BkRBjHSHbOZ241GAq8WLEShMVR4jtjcqQEyDWi-nlcd6BSQs_CahqO0p75pQ4LK8ooR0Nk-XJdcR9OqE3tk72If0pvOlKJPBtvFASUuxah0bIjfiG_5U5aLkySrn9Afi8tvpyVtSzH6fn_86GGKoyY1LiwYdpdPYS8aDTgBhqmEo3iCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFMKPfrAYxwdXVvc3fqMS1dXl-B8eWd6X_nQCDH9IkOQqNV5JS1lOVVD5zlb2j_LBvYXPIDZ1kycOq7XZehWLIe3A_8NMW2RYfVydT4QVs6asg5L57UFCrWjfouQkUboPzEaCOGrhYux9za1gyV2-zpErwJZjACGua262QQhiBRJ8oj404jZICpYu6JUNpN8V0weifW0F_a-Zu0kU_zEDktSU_P4pUXFN2hjfPl3kPOkup_bfWZ3I1xbxah--euqp_1OqOhOJTh30_6DuSfbXVCHLQk2fYpOogkZwBxrrcOfM212-6QMMFdnLdtroa7Avl-1i0DjtlftkQN-idgSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">با سلام درود رفقا میخوام یه ربات open vpn بیارم
دنبال پنل درست حسابیشم
اگه کسی پنلی داشت که بشه حجم و کاربر و ایناشو مشخص کرد ممنون میشم داخل کامنت همین پیام یا پیوی بگه ممنونم ازتون
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6433" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNH9ebg_M6krG6b67_Kgl6Obx_Ddptd_udhbSkLIYBaZ7SBHlUJXbLm3ApHbGX5xSyqUeHyyo4IUx2snRzVQjv9wGI0VPM3t0Q4nlgGuhGD0BvIao4axgOiWgpWyUI4GbSFY7hq2HZWOVcUWcooPtz8fVWIoQGL9HnFdM2Pfb3bEHAm2f7bBoLaAEo3mIN8UQ4OHg5mmC7LoR3KGwcGwGdPAfWLCM7CBkh01bxb5_gEpE5Fa8SL9ch6k3-7Ja6S6Kp8_mSDKv8eaLPXX9ygBV2PzQQbcgu9Ud5sWqBCROK-UKsD72T8RjRAoVungOThaoZS-48m7wxd9jVJUB9hORQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBpYJJ-Exq9AvO6FmrxiWNl2ct7fsqODqZ6N-UkRLHZlscwMmYmGUHlrpRnAaZonIHTAlzfitGG3rq-xd26IEYmYwFiGYuWfvCad98mmy--gyJ2joPBHaRkNWkPlqKqOQqOCmSufEMhahHF7UAmQFmsasXVxJtOD7yS1W-_VnfqOLZzYhuk3PnmM7BQHYAvuNMk9PW85dMdZe5bFgRUBVlpglbx0NPEGY_tvzOrWWogKH0hAltTdZhPvBGIWx6mtnXudIzTm7kVmjs_V5eD2ze1-sdbAotzekn-e9-mg6DvAWoPFCYEi7hidhbIE4oxd9mbW-FCQJI2nnTnlmYaHpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxvtnWYU_3a9we_OZ_pse_CcMIWADFBT6BdyU4aHofFIn7jhq1z1HYqDdH3ZVnKars9zOvwuJgfl8PNVMdnVVtzTk-3sbkJ-Z-zLkiklVsacfK0qqsnxS1SkOscAMVWqpRmXs2efRgycHRrQBsWSMsU7lsJC7iBp-1Pm-Afe9YdGcyJ2nloXWWTqnUoF7YDn3OJuiZ_48YKC-uQOZoVlVIFD0wiQ20VyAreI0v7K0NAI5avAZ1OCNMiWcCAI1ayebiuDyga4qMfuxLkrROX17W4KTDEz8Q-iUlLD1Yie12dtnhH7QS5LckDNti_XnUsVMLYxT7qTob2VEDO1D4hNiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8eeFLBHg8KGV_DtUYlMIcK5hRjK5tXDttOhVkoonO6xcRMiex6erWkNE-CbZDHo6J_SLH4ce6042qXnBGBgjtFTJfQd4AfOfq_he7FlBWatipCIf4Ho8j-xqvuLzyoEoOsOX-Aw_PbtcHxofM4Yk8giAoEyBCpiBT-duL_N5tEtV9aEC-iqih6XogJwVZ5D4f0hqz5xB4Aor1lkRm2jaK9HO6a-NXaNjP9cUmjLtB-avQsS9EKTvwil1xSZcCzt3eZ2hMl_A_fcAYe_v85OsZZQJ46MlS9Njv7xa58oDH8LGdVANw8yYCG7N91-fm38Zs0jzEqJLgUL9V5w8wXclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKcgj44qtEBsZF5rJ4a7vCbLFhO_KnhwsLVxzSs_JwjcOsuogfKMclJZ_KKGkn-2NuoYIvSK22DJ1DSwftdcaw1maf6oRodRXMiLML3MVYYTsTMc59nlO8uOukJ17UImJjeNqIRIWPV0dHwMLIaKPYty2Vw_mYWO2A8r78KZzEQO0hiCXJKOmUC73lMtwfcEIA2f_v-w7cPFV1F6lFxf20_zJPEaFBg_zaiX2CgjowoXizVEhGe6-PCQR5hvb1hoZLGjS7LSu7e17fdj32sdRTEkO89rI1JTRCn_lrB9C4Yq3jyUYxWcVIoFP6Ecw3kJNZqr8JJFzcq3IBjtGUGDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XKg3P5JEsY-7sW0dvKXcNxMAk-ie4407gMNXhsgbYpdFXcruUfHAn2N8dQOlgBVauW79RcKdVlAsHxBHVMlaWys0SbzYr2si_2yClFiRRDxQ-hWSQNKaaAQeAaXDjbIRxWt6rVAnuxPDURLZnUEV_QNlmPx8wfNTWCc2I9UF0AMib_jUfCykyTwR55PNQ_ZRZTC7dMGbWJe-xgPzNYayIQ4pGq4qHZ5Da5-vEq7etWWPsuwA-cvod6BHgr90G1qBrLvcgxeLrHMDCY_CZDY0bLQZoApMsi04jTDG2PKAqrfZ4_EnbrSQFQLvuqfI9eHJMMiUzglmnNlO5BBwhyNvTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjRtoKYTel0ddmM0x3tsczW3RWQlGpMDg2TaTU-Ag-DOwx2ygJ2pSTbBOJKYZduUhNOWgSPQJgAFWyJkwl-EsaYz3mnJGnDSx8dCoTaYNmqbPvLayYdbvoT-2fVS_gonZy8QCy7VCZupKlvWmsf2tuD0VS-25vsNOpsMDAASSKjM-pH8snoVuEP9WeHYHv8GXi4sZqS0uf7IhrkRMEwiRoO4YF9nZqe9GEOv_rGpc8Jxu7uYZdTXoCLA-CeyUVLq46ZT4dXaOMfG8PBYKM-r3pEXEFg-GFkcwfCR6Y8fkvS4aU_AEmj6x1RA7lLB5Uf4ZQDHP7Dtz8G6j8xHEVt0-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGOvWpZ18GeaTZJ2g7pqmC444aCbRfdXnXZl1UthOUBkabcDqEZe_GNw7oEZbssN1TW4fXetK6QMdzj-yc3p463fiIBhJGitvD046crXQYpDChLhUBQVv01_uMgfuO2wgr_F3rSCWFIX2tvcXv7yhpTdaTsREFKCqXLHNEHu3FRaSQEIFxUhKx2PWWaAHFthFCOLrmf_Nczx-lKV_sy_74HdIySxNSoeAwWcFJkY-0r0YR0w3hj3GsjqcoK7p4drVENnTar9ipnR2I_JHboBrYFzVBkwMvmNtWUK7mrBYZpW0wvAgyyp937D9MA051-asq02ikq7KDoDXUNHLrsgkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UThHAwQqaBWOjdaIiXDJCalKKgraXv3NvRiv47k-II98p9Wq2Mh23-QK6WSFGwBAFP6ijFIqX36W-swp1SXG8ouBsGK9wna0iajO0LEHfD4AiqQZ-Hg6o-mIwenHl4NM53pt0jhUlxXA7xMYO0q7pByZDCfJgwDWYWtCSTpBCISlv__lzdN-oBc35ZtXiJmBM08grc8ge9uGbEZIJl5YJ1bwv4G6J4qzniOP9fKGHE--IucCka-TLc8ORbkjhg0kVdLsEzjnOnhtWTMPCTkDIeq13MKL6ET91WHGPQj9cumVtBBtmqY2Gy7f7XeQhZpCPB6JIZTrxKf86SxjSK37yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITfSjRCQ0VqUKEyFxG4FoAJFXDvKErpR_bBowuSo2On0KPUuHN3SsBe6NWi6XwU7C32YuYQrcXrmEyj85iOmjZ9rRrchCBWLyMcFBpZKuqIaxGVJzGNhDqRAUKjCPQ1beMMqnHDHBBmZuwr0GwXj9qoYcSk0XhK__9CuCq7uJNwoFwE7zsIpw7bkKm19wcb9duwaHp8knMpHhr1RtAIYKTUVKN5uzEZw4e58zYYkinV8AITHX7GtrgjJ53xj1TAvUSQvnYcN6q2H7t16I5TTJMwMf4SRhNX5Wdafl8Y7sKf3KkpCrzt9lVGK28FNYsSRbfjn3BgP31eSNkpvqOMExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAu7Eh1DERH52XZByPKJUm6HUFqhsCdeeuUzT-kvCsKx5FdIRQUhckUt8s6y9fq1OGwqU6g0VPSMB_QWBpGJsx239ezmSL1EDUZgkpwLA8Mo0Tc2O6g0l-CpkQrI6zgrCg1Bq2sVDL6LU9q1ck8IKcDZQjgWDUATqes18i_Qu5y5MGli3CrfhT_O8Y46jbj3VO_KJU7Q5Q03wo7_WT6hyBRA5ghtrFhK5asWXrS8Nay0cK-5hM1Yyh2jxLNp07vCLt9EWXFrdQavq1mSgJR5dHexMAFtKVxMrkDmH8oGXqtVmMFiKabHc4QDMslzp41RVxJRHxPUT8pBKQw2eEKfIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=hC_IhzU5IQretGf0gVRDqPrne7WZORUlLLWuBm5VStMDfmiPfpAbpDI6a6OhICCoTEzHt18ndmFfR7F5JikNeXsvywC2kjxybAV8qN-xS8gaNaReZVuADryjnJBa80sgQLWsivlZxVnKeTKLzuJ9KOp6zAasu588FcolTc6QiqxNTE0rx_OsC1WN38h4YbuN7zAwZG1uO6B3hkyGVJl0dfcPNv7tArs-3uZ2wHhEtkVcaNFLj_MrRESmUuXLfT0VrHr-i1xBGytAyDz5qEwfJnjPXBx1NW6rnQ9xwY4Oj8dbnjJa7TZs2u8RnduuJDi1SYjNEElAgX5mLufLGbMyaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=hC_IhzU5IQretGf0gVRDqPrne7WZORUlLLWuBm5VStMDfmiPfpAbpDI6a6OhICCoTEzHt18ndmFfR7F5JikNeXsvywC2kjxybAV8qN-xS8gaNaReZVuADryjnJBa80sgQLWsivlZxVnKeTKLzuJ9KOp6zAasu588FcolTc6QiqxNTE0rx_OsC1WN38h4YbuN7zAwZG1uO6B3hkyGVJl0dfcPNv7tArs-3uZ2wHhEtkVcaNFLj_MrRESmUuXLfT0VrHr-i1xBGytAyDz5qEwfJnjPXBx1NW6rnQ9xwY4Oj8dbnjJa7TZs2u8RnduuJDi1SYjNEElAgX5mLufLGbMyaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-yPXOXgrJIGKmbDBzPOtWPtFDnpOrQ6ti8VadgZhsvFtt3OE6353x1tRO-zhb8h7-FMUiAQRalT7LWRZpvvkdWU4r2oCEBtKAwQZ_GR7y3kAFZ_7EUFfOtn28hXLHo8jj21V_KYtR4MIGbdYE34J915Sk8LqvfKmICApgQFlfiWJ-oJWk0blC2C8SfFpGir3v2FfDFKGXwHi_Tcizj_z5eWYHsdu6bZgfdUkzltm9MfLH1wXC0moE_cnLZ3qWeKRzjwfpwHAPyztVNGF45EdWsKXxCB1eiF4XpYqcJYTdTdllvTlOVMSNvPPWhvyH5YjUdpvMP5sbcsETgVhaW_qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=GIbI892e761-FXJa7H-hj_rGcEu1_ItUfoGBrF_UsV-z0EOTbWoAzgL_qt8weNGWvMxsAi2ue2bNNLQtcC-c-wnPAOJpaLjsOpMNFu4pljj5mNrlGgVE0x103eJmSrqdi09mW4xY6v0igCl3F3IG-o1GhM6gNxpvB0kFBkyJANcBIEp9LR51y2hjshl32Qfnlr_ieR7VeLxwFG_K-9PoXSM0UMu__dIQjVgwlpwlNqUfXJPlJ0Xf2sy3750wZVRnsP1c0Z2IujdY65ETQQTAMT3kOqXlj0qU5cbjd-UnTk2dzBylN1hXFry1taJVzHaLEFowleQbvP5ePo2TtmZGDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=GIbI892e761-FXJa7H-hj_rGcEu1_ItUfoGBrF_UsV-z0EOTbWoAzgL_qt8weNGWvMxsAi2ue2bNNLQtcC-c-wnPAOJpaLjsOpMNFu4pljj5mNrlGgVE0x103eJmSrqdi09mW4xY6v0igCl3F3IG-o1GhM6gNxpvB0kFBkyJANcBIEp9LR51y2hjshl32Qfnlr_ieR7VeLxwFG_K-9PoXSM0UMu__dIQjVgwlpwlNqUfXJPlJ0Xf2sy3750wZVRnsP1c0Z2IujdY65ETQQTAMT3kOqXlj0qU5cbjd-UnTk2dzBylN1hXFry1taJVzHaLEFowleQbvP5ePo2TtmZGDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5mpp2zScw1lzsbxVn89qra2rwpwIIDrTWRhkn6ln7gRa85Nz8GFFRFBiR_WrR_YFPTRonWkjt0zMAX_hekLa4YDgvCIm6VFG9Y1D4_w9txOnPT1tl6TsA-gOgWVkpusv1DM43TOnrLcXYs7NuLkcadan1M6GRiPECswEiW082UH1pl0C0xd8t0yqXhmcE5j4OHK4b0-gA9ktj7dmtryIuOPHXpeoqL79uf2YBxLl5IgaQkSfK26jAYKv3KAyh8rEHJwy2-LMw2qSWTmljFz-9rZXTI4tihRp1FTBqZIddiLp7nPdaylzUe7UE3Le6m3yn4p1NEu5_dIxLRr0GsphA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NWm-SuqYjv4O274DCCUCyyEaJdJYmskWK4t8GPTZHzbYl3ei-wbxvyBSTUAn6lRGwkOqdTJPsDBwxvgFrUhOLNce8wCfYyfH5cYzJAu0v5ad6lzDht_jNBRSWR0y5ENsqZoAPf5li4RrN14XXyQbu-8C1KfpU52_JdXW9EtzxZ3c4jhkqxwriqQj4CiwhJj9aMQSrvKTtukDfo035ELNvTF82j3ZA_7uiYMkMJ00AZh2qT0SNyCKRQXUERnchMKN4-vpLx7dBF23jKJbIFbOKZ9BQ_uYMM7gH5JVlxvvweVHpIDWOx7DQsRiBbi8OJXrwXIJNkhwPbwmkoxdAXwtSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLcRiWEZVBY-_9S1RX78x0_OBOz5wW9o_MOxQ64T5dH93YfYtXHq9uYOFOHBnNqE0_XWMfKLmVVd3aA9FjnYHqWPIccNULxgfMGaRoLoVEBcvGZgitOLOcZjoz1Ak3oyZi2hz9t4OqEpecpD1xz53LzscH2GRme5qXIC_MMQOS8YIqvg_B0GHjiFV867hv2LkIC2NNUegLSJf9addQjMV9gJVzVRgJo6w6eYHjnhoNOclqrHkz_xb9znBHgSw9mtTiY3Tc32A3VFV2FfvuzVJoid2QeIiUhq3mlWJBTN21Pyly5DNOj91ZxAgHKD9AJSAP7sNh-9gzFBhQew7kAGRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_AKJ7otcgf_pLc3CNsz3pqRK1ySyTqQEy1DCeYp7ImZ0o-Ku8qYrub7Q20ZdzJ4G-KQScUMZIhx6UUNoo1rgNDgi3ul2pTwEnBiCFXakkkV-yuW0TOZlWNQiMrmWzksw-8Y1CQl00FJk-IfKJk5-qzdn0YVDbltxu9UqT-9tvBlVR6jat27JH_3YC7xvgEFS9ZT5VlzGix-9sn9LSNkkgl1sDpx22Ag29YSmIB9yBusgeNRTZ9j01osbJ2dIBkHj60cMt3SFyQFMseAq2niaxHE4-Eyv0ICSyVPfruHUN_5XlHrEjiMgbHvskDa-h-L1ftE09lM47Cq7JOyVupgKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnTHwyjcfwR9SnhsDDmxBjQvt_pBE1w0VXgzRlEKVbEvIGAEi83HeUK4uQPhcEPMClwisiW6F9H4Vt_VnqimkW8oTutBWnEZWvs3JgrX9r3xAQfJ2TC-ZMaXYRhqfAm9Z9fkWRRzThjHPt_ZoTYkSOP-J29nea_2fD97flPbO_9IpiSGe1eH3NukAMmj7--MOUlwhOgURbsAqVLBbslYNuXR7Gsbv49eAB8nzT-qNoDu2WwIxJ0fcrlrkYFFLM9gn2DrHiJW3BGehTPE5_AF9TUSITuG3oyO0SQDmoXkTNrmLpr6j0P_GCz7I_p3t47XrpDAuc6Uv1tTgRnEV7hf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvxBvx3zWahmp8WLUYYu-sZJPEb8nlFWJis8X74PJ0T0uKGtvfa5oqhkQKSDJYpQ0hfqT5i18VEITz-HfixFF_nNtBLNlV_wsx4p59WMChgPjad990Bx3gnUWrXKfV_uY-doNO00L0Bqo8sF7DHHLMLgPOFo0-T_BZ1lKX3XWZ0vSaRK9ukYm_iHsU2HitsCn0d6m58CZa4kzr6rLRpIwIsngMzx7KefJA3zyxxFomrNFSW5qFMcC7PvjN5fszLHn23QW3vIom6FDtqvjG3R8GpgWNjtvJ0Rmg8hQq8xBfe4CsRwjbNPU9LBwTtEEk_OON8P_gUYQjiezM5-S4EK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT8A6E4hxQvh9gZ3ke8N8g-14liyX1DEOvoaCrpDHlKBTNsKwSk4PMvmS8__wqvn3Y8kkUw4vx4eTJYai0dHunFIogcvK51D1LsvLmLSH9n_sRoItWgbWUybMfhX67F1wj_vSVq5P1Nv7LoZKHOfYDtTplcGWi2cG1mS5VEzAlenFn2b5d8gI_vzifKJdilvS_qyYedWXP9FiPHCWpvDMsVpRMITTyW4qk91v9gu7i0I1aysPLP5oUvY3ANBNC54goyjbO4Zv05jPJ-_sfltP0SQwe6TkcMT744J09sXgK9L2FrKQShDXCmtucGPAnNY-_yXYegYNRwLBLeFjJNJdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW0FZe4BGHIf3NDYK8hl-DYmF0c7j3gMGG73pqGcdhZVOH3sVkBqGX6eGp85dDfM3BCJSezHXiKCU1243OXg6eWVYQOyTfLxLqR3EY87cP2pAxYEP782MRs0SQReknvAmTF1K9kHkl2nVCRNhR0vNPtEv21XunK8xQtHsoAVVKe6kIfNNYOybs-FaRNd-1FlP5hpfRuTqnx0AO25THWFuhzeqgd-DQlaSjwtsA0cX-unjjhMCb097v0EVQBcKo3v2H-AgXiHFOAM4_uduvDWhrY6kH2kabaMfVFDCR6QjP5WMev3A7fZ6GwSgYtt7Yaco0Z325HRdsb0Rg7fHtiJhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSYYWBQDwO9zznCVPNFFi4CpfnGg_KeULOQkaanF96UK8mJbvCZp83mnrIMSmgYsar0JuAw2Xf7PCOBnJ13t3A5tHs23k5ouyRGrbhfRI2jNKxOEO-XxcLV2r0co7nqNfKq4PZ50abRpPd9_YoL--DSy2oIgDa1rSfjL4zm1Eg6UN0tpQgJ7p0283gId6m95zJIQU_vBZEQc908I3WSo2LUyeqwtE0Uvm09MXC7sogEhNYh5xYg4Mu7gfFAoJXlaVm9C1Jr_9qRZQ5T_bk0lrDxu63joE7UiOM7WzlgDVxmEfAfE2KhmnfxWFSBA1EAMQHOycJWodlLGOH7GA56gfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiD2ZIShBA5snVmzmJ6arn-4xg_8zoHXMh7nXyG2Db2jthPwJMw8ZTVAJ6itncHpubWf2EDP0QgUzVX0HjiNM2QKWoO4BjaPXGUvRmT2zYOoVACEzgKDnmcHISmMXr5eSij05C0fYEi4BaA6iv-SM223v5d8ux93l7609-t4zL0ZRQ0bSgtahHPNh6di2klkppO7zY_JR8WPOkK6mfKwsGh3wfV2QDnFa3UcHhtPANqQRvQFg08Za90XYYFwuDqOiLc6JJ1rE5S48V21Xd9eokaGVun5Dm3CHad8YrPBOFml_KsqYJw_Xx2JdDRV1wNaG-zsi5PlhE7iB3AwRfGtSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHSlFd1zeHEUpSpO7s3zG5RnHFYjg5qbHgr6VgEJuf-G6tnq1JBj4PZlXP9pLP5IzwX6f8ewTiq3Gd-rYhXV11PgURUXuvQdnFAhUVSCz985neUItRI0ShxApMAB-QbNuWvTn0lofK9LE3-sglZ2ZcAvMw1DYMfHWFIYMc00LM_SigQX7gjfSX1Lw_s50NynX_2bVQ6RPCaCMf8l7KQRDGpFpAmsuyMklO5bj4Epj23PSbXmeATEJaUQMkvAzYHlHabDdFnpUqJ6bhVzmxJK_0IBU3aewLYcEp_GX8A4kZ_CoE6J5spD4HWMXoE0vgDNsMNqVJ4LW7iEg7dYDMHiLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=a_aXxO6MCcg1Utf1TO4Fn4CNfkiUIrH97lPgdYERsknAFw8txiVa4J62HI11BgojSjdmGSOYErdJLiTaC7aTUc-u6N_fbm4dmb5ZND-RVNCkKkdvbYISL1o_zwGz4B_D-eNIg7DZVSBeGhZwRr0ZHQmR4E04bcN8S0cK0vWAi44kxabw7t3q3Zd1EU9DJBL9cE9Pfp-kOanQMUEvajf7twxpDOrwaMHF-4ycL0GqvcST8PkUJiyXWwjoJUE07rU4T4JvuUE-_fDUViGRw0EhsY_qbMnEPdXraObDnA5NyzKOpYC1YGAdvNYWO82-LYzlx9zW7_9DFIudW5gjkTinbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=a_aXxO6MCcg1Utf1TO4Fn4CNfkiUIrH97lPgdYERsknAFw8txiVa4J62HI11BgojSjdmGSOYErdJLiTaC7aTUc-u6N_fbm4dmb5ZND-RVNCkKkdvbYISL1o_zwGz4B_D-eNIg7DZVSBeGhZwRr0ZHQmR4E04bcN8S0cK0vWAi44kxabw7t3q3Zd1EU9DJBL9cE9Pfp-kOanQMUEvajf7twxpDOrwaMHF-4ycL0GqvcST8PkUJiyXWwjoJUE07rU4T4JvuUE-_fDUViGRw0EhsY_qbMnEPdXraObDnA5NyzKOpYC1YGAdvNYWO82-LYzlx9zW7_9DFIudW5gjkTinbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niaFFTM69_NzzzDGv-IlIRgs91iStThdF-yswMOpDvBxeH4KfEzwoTSZ_lcelTBGiLTq3eF-rxPbOczcALwOjEppUxJ5eOWxlHW_wM89UUUCfbmpTgiLHbIWnHecBAOpHlkF7_yOlaLWpK3Mkim-tF3MhWDlDendZd-Y1IDKoEoKTtoqBW5z9ghzET5y82ivtYWlvGeNdtAjrRFaTQocC6T2UZ_WTyR0TPeznz14LBYVVBq7V4EdSvtgIHXQgb009jpKVwytQLrJZCW-6w4FUUercOkQZNsyxFBnabxlKl1v67UBYzJ0lMi8KiuoLOFMD0qM-jAlghgJtl3IHhtvZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8d-rcREGhG4F0z8IsP705XbfdsH4nJN0Z99rXtCJH3bsWlVmzxLQ6N8BmsJhzVC8poTuQwQ_Ma4q1jSQhH20_Zz5i_6PKkTYM4HNndgBZVhp8JVefOJzo1AhfTM7HSzgm2rWdHA9AdOjYdUDSaGJVIy4d33p4jO3CbLjkl4Q-mv4Y2ZLjqpr-PO9EQ7ZvVgauYgzWD5qmwofj2dUyeDhFwoWzeyBpe9fq0GXzFTPzxgOFrB98JZjRR9PWEb4dHCjogOicgB0tKIk5asnJHn5JKz3lDg5Vd5-JVQZqSeYRifCVrsAK3RNLOvz3HqcFCUG-SSF0hdB13YWTEik99w-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=lt0NiMZ_JN2uSjnNGVbYR7IdN73ZSgVkJ1SVY2jJ3lvD2vltuESR8heWxcdnXRXhFMq6DxkEaW7ImXfNJiEZD3WCSuXmp2BjJA4Ik27uI0KUDX5kM1bQxABceq48ILUbzFYJcpUdzWc7jybq4MfRkmg_t0CgegAd25jCQOA5V-_Qt2O4UtY0a5PJum6LTuMONY1OMR0-8ACFayF4r9yOu_wXq-9XnWAOglw992qu5atupOp_2b7LMyEIERksv1tjsYq5U_SgYNCOHu3uetGHnpvMLr8t0iNv7q3MFhXyFxoiHwioG9sclLDiP79eb5MHDwSebpDfpp1e9hEUEQqW95nO54WxEL8ltJVIqdeXpF5hZFQx0iMTEcYy_fRdkQHr9Y1gep0P5kF2-rclqiq6yLiKY7ArifHncVIlq7-4F1ymDnlXy0FpRFCLwlp3bB2_gaV3Y_pMZZmK2zi2QA-rivGxDSRzChMiV7yBY7Q5Sa6_T6cQBOlm9BBtDWRlJbNrQdyUB8vTzsclrRYT0sB9ZZPC3nZylqEGbrCqiSctABoJvysRoeLOq9rDN3OIgpQKta5QdlQ7QewLljIUyq5vOS6InTETobNUUY1awxjI_OTGFHWm5bTu_XwQ3-WBth3Pn_vqFEk7mmdOuwLAT4SMM11xZtf9R2yecb-ShE160T4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=lt0NiMZ_JN2uSjnNGVbYR7IdN73ZSgVkJ1SVY2jJ3lvD2vltuESR8heWxcdnXRXhFMq6DxkEaW7ImXfNJiEZD3WCSuXmp2BjJA4Ik27uI0KUDX5kM1bQxABceq48ILUbzFYJcpUdzWc7jybq4MfRkmg_t0CgegAd25jCQOA5V-_Qt2O4UtY0a5PJum6LTuMONY1OMR0-8ACFayF4r9yOu_wXq-9XnWAOglw992qu5atupOp_2b7LMyEIERksv1tjsYq5U_SgYNCOHu3uetGHnpvMLr8t0iNv7q3MFhXyFxoiHwioG9sclLDiP79eb5MHDwSebpDfpp1e9hEUEQqW95nO54WxEL8ltJVIqdeXpF5hZFQx0iMTEcYy_fRdkQHr9Y1gep0P5kF2-rclqiq6yLiKY7ArifHncVIlq7-4F1ymDnlXy0FpRFCLwlp3bB2_gaV3Y_pMZZmK2zi2QA-rivGxDSRzChMiV7yBY7Q5Sa6_T6cQBOlm9BBtDWRlJbNrQdyUB8vTzsclrRYT0sB9ZZPC3nZylqEGbrCqiSctABoJvysRoeLOq9rDN3OIgpQKta5QdlQ7QewLljIUyq5vOS6InTETobNUUY1awxjI_OTGFHWm5bTu_XwQ3-WBth3Pn_vqFEk7mmdOuwLAT4SMM11xZtf9R2yecb-ShE160T4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=DD_SzNc1KHFPcvscideo0XWYkBA6BAZPl1cX5oO9861Zpl3824PXnDsIq6OvgE3Ol1Vqrfy4pF8GhWXH_phYcrokSPG-PA2bGijNjTMapxdFQwe80pFHIamaYrlnuKk4Qq56BTVSq8KwDVwPG6snwRsQIxTUMI9E0ogv68Qj5lQ9K_e00JTmXnrD0jYRPD6HYseNEwcZTArlzzS-oMLIVRzfAy_xR3rI_ubcwlg9SiO8WBZpnx0to-Vw86O6IOZwGSRQ4eJV4GJRiqN_llJaMpp1TFyThL_dHDz5rgBUrnyvcQ8CJJbZ7m8OObpWLoxVn75plblY4ZgtFKeF8PdK4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=DD_SzNc1KHFPcvscideo0XWYkBA6BAZPl1cX5oO9861Zpl3824PXnDsIq6OvgE3Ol1Vqrfy4pF8GhWXH_phYcrokSPG-PA2bGijNjTMapxdFQwe80pFHIamaYrlnuKk4Qq56BTVSq8KwDVwPG6snwRsQIxTUMI9E0ogv68Qj5lQ9K_e00JTmXnrD0jYRPD6HYseNEwcZTArlzzS-oMLIVRzfAy_xR3rI_ubcwlg9SiO8WBZpnx0to-Vw86O6IOZwGSRQ4eJV4GJRiqN_llJaMpp1TFyThL_dHDz5rgBUrnyvcQ8CJJbZ7m8OObpWLoxVn75plblY4ZgtFKeF8PdK4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToXGW1xFWsle6KmWQQRfCaVXRJYiEJHDKq6kxqnk4qzLgHWchUrFfwK0Dt0SEPqoSlFkjMF9SsOP3_azdH8KgUGN1pg7sqLSFaR4sbEkbBZwESYTTc6B-eKEU1Uzk7agUfRdqShysrEUI50sJLkvypHJnmr7xJIU0RGNT441dcGZYioorTaF7KWchbSVW0qTdsv7jxXNWrMopWEfE-3Mog_WVY-4-jCqIh44ffCezsCvGfW0ahQiKBgzs8riHiThauiZbMqLkV49Kw-Lqk_zKswpOGoQFkkDpeis_zR1HZi1g3UMV4DZTx9Gn1UV7-UR2m_3f1xxz9xMTZseqOrBYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc8D-4XwmdNB_70ebT_5ieKUq8tN4BriWUKl_JOvi_8LbVbahaQogG5GIjDBuxVl-ASf0rcAT5rRjz3RT2Thv8P665inE437B72hGZCeWxc3x7w-K73Et87XhE2QMlby7YewOIEtSQmg4nZsl80byRgfmV2NysAjjJ4YAznGE8ewJzPRwhapYy-HXRJSvfSNrf6ptcHUclmTt5LMr3LXBA9wXoVz6iDOyPf4rD3fZTCULoQ-AW0SOhSD7R0D06IfeL5rKvO5b6uy4e_NgUzmuzs2-USQKp4Qe13x97yS8te_Uf4uYhJZdWRRQtRxvh22KDfWBqigwnMjyJVfMPqQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mi4PU5Z4lm2q78ed-lePLxENCniRbLeRwEneTSLx6iO72gdTri-HN6alOow2U7p8xgm_0a_pJ7WwKTc5Xp3f5N-NGyLdwYTOHzoXfUEH6c2abatjwoxEPTGlw9U4Q18gOb1HiQ_kr9u_CY9uK8WO-NbOVzYCfn7hGtWmMSvbJfhXYHbu39-USnaz8wxoQJy5dsAAMaVk7000_mVizfUU6mQZ1G5LBQJsaJz6aHR2PfpKjzhRlPX_CZqbyABbTidVxEZsMYPJS3mufWUD2lBMJUwKI3M5otjTpFZBiCztLan8tcOxYm6rXfHrvabVpBc4uYdMNK-XqFEZlxZ_sy-7Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jzW7ap3cLjFBeK7djdy9ZY8XL9M-0d4zB6m7UiTs1QUifReAtBWnBbgvR8VAECuMQfP77DjIGWZcfajFFo5p3sdk6UBSSEIfiWfcJp3ZJSBj_CpcKfpA8lqQnEpH19lewf7yXmSuMyoQaCkNuweINuHknnvrvZQY1g7_rc9A9qEzT34piIl-59IhqXKVDjLFM6V8f16GsKNLlsDbxcIBICw48O8pfrgqgRLinPs9_mDtVftIVjgj2UnQfLAJiZjKp67HnpGLDqm_owFeaiSQ7OHCAlqlneUOA3-mwpScKpHKpTSiH1Emw41kH-TsVgGkTAFVwucHf1U3j0_SZkOHkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgVuj8sAQ4bbTbgtMJA1nhQgqgEDiNeZDFMATILkZ6-_t0hEPSUf01a5dlRpO5tFAvvZfxcm8FgsPHpOaB5Tn0ebRbyXDf2e5SBiMzA4OT5UZmW4Pa2Uhwz5tz8l6InzEwwDTC5cc2rYX4hUu_QE5um01IrV0b8PNu6VUQDEIx7GMlP6hjuYadqfGuzTZHv1xvABGAVm5JL6OhqENoD8NUT4bxXV623IaHYQ13aExqxNrHhPTXucSKIxhlF28R0JxE99b0AZON6LYG_2NFWgUPuUUM38flUdRQoIU72VglH2dsA0iW-qMaZ_WTIxWMYXjvivMoNKIe8jxTvqMgv8zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omBGYq8Gi9swblupmbH8gTqcZhletKBPJs0NIct2SU9TIIhu4DoCOQZY4ln-bWTzC52tgVSWXrmqUZGdd1g4nC8B4UqATL4Ibys61LeOa31W4jsF-6cJRaSIki8gLlADNsipkKITPKb2igemNHAWJO9QNgFuX5CoKcQJbeclW4UzfQzWH3HY_s3WetZKeYy5JhpGr8nmk_9Lno014pjhcWHWEg-DFfXrza3GjNE8iThiefXt0bdar54bwACHxCw1OYX5bavqc7cusePln9ypwAj6RKqcNTV0eB5oZKvw1PDBw_taxvH6Fpmu7l98Csu3ApfU07d-dRb2cW9WQ5QESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gd8h9bUar8QKhWJqxoB-gIgapE_9w5cz1dofp-NpHVdBJ1gBc1Qho5kq4cvQLHKotpEjwhZyLOKVXTkwAbh7PdfCJDMhZUuRjO-RVyMwLKrgdxmp3NhIv3NdKJnqdyPuTS3ucayFo1VLjlEFuSy9lIqHO9BccU8POHcgDJvV0Wzerc1ECm2NhtaOZ9hK8A7KpzkfvrwnehzftxseSmwyd_wi5zR9IdDXqeBFmnbEeohgeXs3Be-36R03x6DhPSszdtOf3gsS2gY_9gRDH8s_ydimuK42o3BoDgZodUHFLMPkDUK9Y5eGU-vy5f_PiXMZm2H1xJVUw8Y8eXmyUsnDEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtL-TEzCRSowdV-zdy93cEUsMH0H1yLpbd5CD3uC2f_DFqZ1ar0gMmzq2z-kL_v1ivcTYrWtMC98q1QxjlP8w1N9e9utU2v_R0L-6cqcwS44c4BTl3ERqDY8yeRl93dYt5p7Z00eTX8g12dXIByaYkCy4qK_li6ws_A0hRNhyIsUNj6gB1J9henMMDI6iayl2YFaErB7Y_iayn5VjPSDW5rA1DBnOSOwZo2Zock7t77i_ESUkRSd4gY_s9GhzTLdPykR_GrZV5EUmHpy45gr9cAkwf0mj6b77BpqytnnlXX6rq4o3MPQcdp8eJCIzAysLTLOzjeBzrRtfn2UFLGLZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCNPCZM58aNcpGtfiDZIn2j2eK36XUEC8p6PKzLh2xossbS4o7qwRbw2jCOi_8Y8o_lhK1qloaPckuQ7CCqXRwLzOXJYCx7-LHIHrjkrINVvn7sHGUqTHvt5IVclchjNNBqZffgsDa88ieipcP3lEqWGlpn7b7PxBvQzBdj6b6UHIe3mHPUjq0sVc5_5Oe-iKdXPpHQ72s_VOQ2neMqRxxezbyOMFVpkPEK5V48NyRsbmqUpt6mfHRtCCBJH492Wc6GS5bAg-r3HgmbaAGvdlpv49Ky3VYeHJH_9EvrqVF6pDXn9TuWQ4i56h87iQybgbT7O-yQZ4OdxRw4Tkc0H4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSUcM4vaeByOB8fJ4fthq0M1rzapaMPZ1-tQ9Lg9njQGtuT73n5zR5dTXFcGFKCfZ4O52z1npVw6lQbwQpix48T7FEuFkFfSCoFgk3B0ZS1EXvcWrrwCFDXjHpO9akevvHzu__j0LpHtp2cELSoBrAA5wfcdHvOawc1sm7A6deqazfC2ImR5_QaSFYUYAcCH_fgzKEKjo5h9kby2Q7KFFFVEcUoOs5w5GOxuXLYHNCc7KKyFTEtxOqZQC_utTUId1qsTOJl2WeRG1xt0fkgnu1WegXtslmOlVrwjy0IJfJPArNk-QS7kUyKdzLuEjI69UeyRUSffQSK3patOw-DvDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFMZLvwVlKEYn_BaBrNZzHFynBOT9cvekz9QE6VNZeqdN9wZToxGpaZCfP0zyC5Q6VYAsbxQ2zt4u5BUTy0mlE72Z7HLiBJNR7qv7GE5WuzaXRQcjc3PvTUVKr6VGyqXKBB51cERpvQ0TQ4YzU5eAaMgP6nLNEKj_o7ThrxsMlYkQ3mUif_Q3IpXXe6DEOgahxPVndFlWvvqSObuAhswxc9UUM9eWQEY5rjWLcw5NQM9Dv0XczaPhqUz3kZW6zo3al2T7PmHcgD3gF0K8v0rWKXzs6Aju-yVaJIPww0qnxiOGZvT-kKnkqxrbajBO46xu8nUdSAvHmrz2CNkfR1fLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dd6LHJATZjuTjh-nyWUkJpId1GOzC8x-N-1eCjIK6nfWK00LOaMxGANwyiFsgICXzb448DNt7x3AdN4IXNWybPIG4zlfVZ82ANMdYTeVXyICp83h5fHQ656qGiY0RBiU0pCAzVFM1OO2b9ggieoHfGuxcN64BQDTtAiAoiJzX_wbqrXfnPbCcZONlB_6uPKVoRWhbHrNMmdvKVWRJX8ViehS6EOKE1-25Y2ZVVbD9I5Bcup_Tr-C489QhXWyvteoNEFsOYnbRwBtaeNgmK59yMeIZyXD8jUhv2qgdzK5p2qDp_GRakgh720XJvpzxfrhksY8taPS00YkCMNdtlcWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=iwN83Akp5Nk6rO9Inw1FV8O_txH19CchVraEwoTMf0Vs2V2YITgBWbNlM2aE92t4wcuWFQn8fP5JdHyATppROs2hnms9DeYJL4Ry4h42tOO-4VO33VatHJcOdvFRwB2upK8pc0o7O_9qFsJy8TWxlQmFTL8VFfs_fhGC5yEHtbpCxSZTGMGpheZrKEqMs0PckverXfNdva3ptleLgi80Hn6dFEhxwUvJgUSESkzubh4vbzTy8uto8fc1nGNGJpZN0RkSQKXAINzFqaeCPm9fyAF7zUUEzmmALBq5XBRCFmzhiqLDmns_kx_n3nSTUTm3VGBbpNpu1oHFkvUqNfps4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=iwN83Akp5Nk6rO9Inw1FV8O_txH19CchVraEwoTMf0Vs2V2YITgBWbNlM2aE92t4wcuWFQn8fP5JdHyATppROs2hnms9DeYJL4Ry4h42tOO-4VO33VatHJcOdvFRwB2upK8pc0o7O_9qFsJy8TWxlQmFTL8VFfs_fhGC5yEHtbpCxSZTGMGpheZrKEqMs0PckverXfNdva3ptleLgi80Hn6dFEhxwUvJgUSESkzubh4vbzTy8uto8fc1nGNGJpZN0RkSQKXAINzFqaeCPm9fyAF7zUUEzmmALBq5XBRCFmzhiqLDmns_kx_n3nSTUTm3VGBbpNpu1oHFkvUqNfps4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itJ4gR63vMgFCpmRyJLqPlSU7_7-MtsJTaYsoJFqOzXEYlw42-HMbcyLnPPh02JLhsnROCHt_e5Ivdn7dtuZHWeGTktI3CTv8Ivrq-dvgZ8w-Wjb6-9NZFl8Vz6K8PLnjo0jUyYwbXrF6RIm6RA1lU7gS_n9n6E7bSP7uqOVnn7g6KhTkwa8iXKr8SwaWJKWfgGJi11morKMo3RtK9PvLX_nbltNnmvzHAMJ19acuRn36E1-XDooGWRBdZGd4r7c_go2Ch6Q-_J4knt5oJBsgz_uRjq_z2bJjzOo2vkeaMBRd2t0yQ8sEzYXtI0Z5aVJlln2fSwpYlGk6IzQM80rMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seo3CbWDO_Gwgv3Pgw4Aza3lKZONgvVfLPsMCLJGd0qsMQUS__-uRrqXh3EaZY_NvUIdDCpJNLXehbPJ4QVP2P4SkdLS19j-SffPz5DyDry7dKp49kcrxTd4F1PAOuGpBGLmhEO8HgIgs8oAYToRInHzg3YvdWr880IqlGimXUBPn308C0eNuw4l-zNPzwg37Cb_NpLHyq1tXwA7E_tHY5Im-Cb5L0jD7ORUZeaEpnEezg8ApQLTLf-ogUzYt4oLXBjII2AZS5qNJdlitCXTwnQ4Dm40DKWMjZFyG59v18eDhM2Q0M9WIpKEF3HKzV8LIWkSVMCF24BtZ_NOcyvqog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NohmX_b1WhF3mf0S_s9r_JfEJeWA8kapOhYDa6M_eSfj-MQyTZzpsxdUGc4PQeNk75gRXxl9Udbz3vmkbjuPH9Jh-cVan9w5ye7ixasU0OmUNoVs9Fcrc3CxFm6xrX4pRUl6iMpenhMrgk_R3QArABeTfR5b0-hUvx_9VJo2xgw_By91KFsYDMmeckTWhgQPPrLLYeEgryEdlsXzxRuQaEOHCervP4C1Z4Go4XRXFHewXkZaE3dXsjz0Sd3B0SURMyT_M0QOJrxk7AxjKhFsws9GEiR8cQ3O3bWASIqm0-mkIYAVRzBoym9eJy5FAuPqm_rXbNZc8B_FsmCsTFFS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJta6QKAdRaBhcVVbEbkGl0-amNhHkv6-m57tjSf0RdV4GNDER-FZpgOOb4bZAScFzq3-hZfJHbjQ8yTW9DFd3gAuASTCU1h6D-TjRrzaXYKJ1KUavtFAbIVUTZUXz8JR4GiPprrXHlN8IoLJQXk7bzPblL9hNtx0_q1w--6Cf1H9jKABWN4w-xbYY44omqlOU9VBgT248yt9ojqrRYzUsd47yeOrgX3lvJZ3hGCpMBf4g-n_Gb3E4JYQS04mq-4DdfW-qvLLGSOooDfgDqxrTRVrqN2VvVXIkov_2zTmOMt56dttdX4QoMLbqLlMvRduGHssnnGgvn1ul6g5g94bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=E57GRKXQWETD-Lq3tisDDhMbYz2rD8ozhE-ydIbTxMxMj8xpySfaPPYX3p8uTA1Vxs1VFbKGhfaRDHrWLXdFgb7WfngksX5IJJlrcEByaYHR6Ouoi8PTF5xLHNZzaIuvAztmxSGRg9e5n7qgHQiGmHTvEjij1-g7hfWsXlqe1hbhbSSA1JKwDRBsaKIwseplrEbHHTEgGJe3ghSHTTekhpGv83mjBiW7MFYHFPAlFbeq_uES4XRPPiwwxt60ebpBBSW1BmX-qMDvsI0Z5GO-0XUvMVZArRm-lt_mmGN8N47IggP7uwwlWLTPdgJBg5HlFaoq8ga9uAFvjlvEY4m4hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=E57GRKXQWETD-Lq3tisDDhMbYz2rD8ozhE-ydIbTxMxMj8xpySfaPPYX3p8uTA1Vxs1VFbKGhfaRDHrWLXdFgb7WfngksX5IJJlrcEByaYHR6Ouoi8PTF5xLHNZzaIuvAztmxSGRg9e5n7qgHQiGmHTvEjij1-g7hfWsXlqe1hbhbSSA1JKwDRBsaKIwseplrEbHHTEgGJe3ghSHTTekhpGv83mjBiW7MFYHFPAlFbeq_uES4XRPPiwwxt60ebpBBSW1BmX-qMDvsI0Z5GO-0XUvMVZArRm-lt_mmGN8N47IggP7uwwlWLTPdgJBg5HlFaoq8ga9uAFvjlvEY4m4hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOiIh3hvaKf6f_QouxzlHWthniS7YJXUhz9xND9-zDbjfKWaJATBGE58XtkoZn-7bye4j6iEd9CCKYQwZ2VnAfELXbhXK4G-7YB6oL9nkXNOCdSM30QZwErI54FDMP32GZsRhXv2ciHDvmRWd8_Jrr-ayUpQQYWVr4goJ89cT2Ufe0K-sGkJwbbi6DhUCbI_fkzYbdI6d0k6EDN1ZH3YnlSVvesgiBsEDKpBtGJPycDu-kaJ2WKiJF8rofKi2dWJlwyVqSMZw5rniV0wTkI8XsmeirclAYwJi0mP8pG_shQmejyDlO7-JVxjn4BMeS7ywOt2NioVcv4d8c6o4U-HwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پخش FLAC با کیفیت lossless بدون محدودیت!
✨
قابلیت‌ها:
•
🔹
دسترسی به کاتالوگ گسترده موسیقی از تمام ژانرها
•
⚡
دانلود همزمان چندین ترک با سرعت بالا
•
🛠️
ذخیره فایل‌ها با وضوح اصلی بدون فشرده‌سازی مجدد
•
📦
پخش مستقیم بدون نیاز به سرویس‌های استریمینگ
🔗
لینک:
https://flac.music.hi.cn/
#Music
#Flac
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
