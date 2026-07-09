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
<img src="https://cdn4.telesco.pe/file/C7TUBpbNoQzG6br1alPl75fnlC_72aY7yAhs5yHym17-XbDZHY-hzJag-kUnY5rYUELwUnAqvpQ4AOvWT1pju9xhCf1T9SJAzIKq7YiGzPQPd2nPMuKn_6a7micDFe0NMGhjscsI7UT4IvY7qT6Zh904FGej8IwuH_7xFHSfrUtusIg1QA1uraSdShUBab8kmStgwIHvVfEovftsaiyIXqdznb6ONOkM-X2wmvh5nxS7cTgFTT1-Iut_WcS7bOJrgAwAJuZ7S_L2aB-bk6gbuVJ7HliO0ZqsQuNz4oYN9mHaiNxymqFAujyf3VpUJFUthv0FRGy0-ywp3hWmoEGM4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.82K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 18:03:59</div>
<hr>

<div class="tg-post" id="msg-6819">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌐
دانلود کامل هر وب‌سایت با Website Downloader
اگر می‌خواهید یک وب‌سایت را برای استفاده آفلاین یا بررسی کدهای آن دانلود کنید(فرانت اند)،
Website Downloader
ابزار مناسبی است.
✨
قابلیت‌ها: •
📥
دانلود کامل
HTML، CSS، JavaScript، تصاویر و فونت‌ها
•
🔗
بازنویسی لینک‌ها برای اجرای آفلاین •
📦
خروجی به‌صورت فایل ZIP •
⚡
متن‌باز با لایسنس MIT
این ابزار برای
کلون کردن سایت‌ها، تهیه نسخه آفلاین و یادگیری ساختار پروژه‌های وب
بسیار کاربردی است.
🔗
GitHub
:
https://github.com/AhmadIbrahiim/Website-downloader
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 483 · <a href="https://t.me/ArchiveTell/6819" target="_blank">📅 17:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6818">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b961c32eaa.mp4?token=FJl4w5ddL_FwQBu6qOf3OU1mjOBtZWPQ1t08o3s8MiRlqJcjmgIYYCaUGiwUcf-i98-e5wIh0RljBJgXUTo9XEzbi4h8g_-W-MLYap7BnJ5U0CgTgOwSpP3SCxGTpkIwkOftyBX1GMdzmmWrr06nQ-Fi4Cu8bb6ii3CJOQU0iQy4819B3B26SxUDpMn0qVSB-ORFYI_G2tPrUTTA3rdWDE3kQ2vPirqWBMEOJGJVGHjlI3iD2LYUFFApw7vwPrOzW2B2XDz-8gUxpLaVpgCUK6G-YnmhJLtaPv4i5SM4yRwd-Aou12O3I1e4ywp1VQquKHQrrDj8rNvLXoL72y5HgWy5_n4dJJQBcAC6OY3qFBeposCaloD-5IIivrMFLJ-pDe1fUNM2392tMlouloJohijQO_72P8osskpFVCotXjJ6Ae5L7QttoLdY2TeQaD8sAINxyJ0pQXhTwAXgCT_tGh0SwmeOZMz3jFigz2gNmSJZNKubIcmCKKub522ujY1b-PBkmvXaTB5-NWDZa_0uhOfW7XE4OhFcV16l96ZPaHj--UyixP-T2_G8PmGGlWlAletFQ5GBMfeIDkdG20RVYntq9GQCcxmsfbrKXMhKJr9_mvaplgqOr4Q3KCP4uDi6wkQwKjT-ShLGVq8o8jatklm6-DlhAqQqzDzpM5GpwfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b961c32eaa.mp4?token=FJl4w5ddL_FwQBu6qOf3OU1mjOBtZWPQ1t08o3s8MiRlqJcjmgIYYCaUGiwUcf-i98-e5wIh0RljBJgXUTo9XEzbi4h8g_-W-MLYap7BnJ5U0CgTgOwSpP3SCxGTpkIwkOftyBX1GMdzmmWrr06nQ-Fi4Cu8bb6ii3CJOQU0iQy4819B3B26SxUDpMn0qVSB-ORFYI_G2tPrUTTA3rdWDE3kQ2vPirqWBMEOJGJVGHjlI3iD2LYUFFApw7vwPrOzW2B2XDz-8gUxpLaVpgCUK6G-YnmhJLtaPv4i5SM4yRwd-Aou12O3I1e4ywp1VQquKHQrrDj8rNvLXoL72y5HgWy5_n4dJJQBcAC6OY3qFBeposCaloD-5IIivrMFLJ-pDe1fUNM2392tMlouloJohijQO_72P8osskpFVCotXjJ6Ae5L7QttoLdY2TeQaD8sAINxyJ0pQXhTwAXgCT_tGh0SwmeOZMz3jFigz2gNmSJZNKubIcmCKKub522ujY1b-PBkmvXaTB5-NWDZa_0uhOfW7XE4OhFcV16l96ZPaHj--UyixP-T2_G8PmGGlWlAletFQ5GBMfeIDkdG20RVYntq9GQCcxmsfbrKXMhKJr9_mvaplgqOr4Q3KCP4uDi6wkQwKjT-ShLGVq8o8jatklm6-DlhAqQqzDzpM5GpwfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🌎
نقشه آینده زمین برای زندگی!
‏این پروژه خیلی جالب و مهمه! یه نقشه تعاملی به نام ‌Farmland Atlas⁩ ساخته شده که پیش‌بینی می‌کنه مناطق مختلف زمین چقدر برای زندگی مناسب خواهند بود تا سال ‌2100⁩.
🤔
‏این پلتفرم با تحلیل بیش از ‌5⁩ میلیون نقطه، چندین سناریو رو بررسی می‌کنه، از خوش‌بینانه تا بدبینانه. برای هر مکان، پیش‌بینی آب و هوا، ارزیابی کیفیت منابع آب، وضعیت خاک و خطرات اجتماعی رو هم در نظر می‌گیره.
🌟
🔗
https://farmlandatlas.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 890 · <a href="https://t.me/ArchiveTell/6818" target="_blank">📅 14:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6817">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📊
معرفی ابزار CodexBar
اگر از
Claude Code، OpenAI Codex، Cursor، Gemini، OpenRouter، GitHub Copilot
یا سایر ابزارهای AI استفاده می‌کنید، احتمالاً بارها با محدودیت استفاده یا تمام شدن سهمیه مواجه شده‌اید.
؛
CodexBar
یک ابزار متن‌باز برای macOS است که تمام این اطلاعات را مستقیماً در نوار منو نمایش می‌دهد تا همیشه بدانید چقدر از سهمیه‌تان باقی مانده است.
ویژگی‌ها:
• نمایش میزان استفاده و سهمیه باقی‌مانده
• نمایش زمان دقیق ریست شدن محدودیت‌ها
• پشتیبانی از Claude، Codex، Cursor، Gemini، OpenRouter، GitHub Copilot، Groq، Deepgram، MiniMax،
z.ai
و ده‌ها سرویس دیگر
• نمایش هزینه، اعتبار و میزان مصرف API در سرویس‌های پشتیبانی‌شده
• نمایش وضعیت آنلاین سرویس‌ها و اختلالات احتمالی
• حالت تجمیعی برای مدیریت چندین سرویس از یک پنل
• بدون ذخیره رمز عبور؛ از نشست‌ها و لاگین‌های موجود شما استفاده می‌کند.
🔗
GitHub:
https://github.com/steipete/CodexBar
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/ArchiveTell/6817" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6816">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚀
چند ابزار متن‌باز و رایگان برای برنامه‌نویس‌ها و سازنده‌ها:
🎨
Text Effects
افکت‌های جذاب CSS برای طراحی متن و رابط وب.
📧
SESPulse
داشبورد متن‌باز برای مدیریت و بررسی ایمیل‌های Amazon SES.
🔎
API Finder
مخزن APIهای عمومی برای پیدا کردن سرویس‌های آماده.
🛡
Tirreno
فریم‌ورک امنیتی متن‌باز برای شناسایی رفتارهای مشکوک کاربران.
💻
OpenTUI
کتابخانه ساخت رابط‌های کاربری زیبا در ترمینال.
✨
ابزارهای کوچک، کاربردهای بزرگ برای ساخت سریع‌تر پروژه‌ها.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 914 · <a href="https://t.me/ArchiveTell/6816" target="_blank">📅 13:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6815">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کانفیگ اهدایی
🔥
vless://ac7e7b41-0dc0-4bec-a285-3266ecbb87c8@ps.aramvpn.kdns.fr:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QFc4pPuYwGfyKeoSWnxUkPgaDdEPCPPb2ImpxI-njxI&security=reality&sid=0586e9d2d3a6d12d&sni=www.yahoo.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/ArchiveTell/6815" target="_blank">📅 13:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6814">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📸
ساخت عکس پرسنلی ۳×۴ با هوش مصنوعی
اگر یک عکس معمولی از خودتان دارید، می‌توانید با پرامپت زیر آن را به یک
عکس پرسنلی رسمی
تبدیل کنید.
✨
ویژگی‌ها:
✅
پس‌زمینه سفید یا خاکستری ساده
✅
نورپردازی طبیعی و یکنواخت
✅
حذف اشیای اضافی و اکسسوری‌ها
✅
افزایش کیفیت و وضوح تصویر
✅
مناسب برای عکس پرسنلی و پاسپورت
📝
Prompt:
Convert this photo into a professional ID/passport photo.
- Neutral plain background (light gray or white, evenly lit, no texture).
- Centered face and shoulders visible, crop from top of head to chest.
- Natural skin tone, balanced lighting, no shadows.
- Neutral facial expression (slight smile allowed).
- Professional look, no accessories (remove hats, sunglasses, background objects).
- Enhance sharpness and clarity.
- High resolution, suitable for official use.
💡
برای بهترین نتیجه، یک عکس با نور مناسب و کیفیت خوب به مدل بدهید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/ArchiveTell/6814" target="_blank">📅 11:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6813">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📄
olmOCR | تبدیل هوشمند PDF به Markdown با هوش مصنوعی
یک ابزار متن‌باز برای تبدیل فایل‌های PDF، PNG و JPEG به متن و Markdown تمیز با حفظ ساختار اسناد؛ مناسب برای مقالات، کتاب‌ها و فایل‌های اسکن‌شده.
🚀
⚡
ویژگی‌ها:
📝
تبدیل PDF و تصاویر به Markdown خوانا
📊
پشتیبانی از جدول‌ها، فرمول‌ها، دست‌خط و قالب‌بندی‌های پیچیده
🧹
حذف خودکار هدر و فوتر صفحات
📚
حفظ ترتیب طبیعی متن حتی در اسناد چندستونه و دارای شکل
⚡
دقت بالا با پشتیبانی از پردازش محلی یا سرورهای vLLM
🔓
متن‌باز با لایسنس Apache 2.0
🔗
https://github.com/allenai/olmocr
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/ArchiveTell/6813" target="_blank">📅 10:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6812">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">؛
🛠️
OfficeCLI؛ هوش مصنوعی برای Word، Excel و PowerPoint
؛
OfficeCLI
یک ابزار متن‌باز جدید است که به دستیارهای هوش مصنوعی امکان کار مستقیم با فایل‌های
Word، Excel و PowerPoint
را می‌دهد.
✨
قابلیت‌ها: •
📄
ساخت و ویرایش اسناد Word •
📊
ایجاد و تحلیل فایل‌های Excel •
📽️
ساخت و ویرایش ارائه‌های PowerPoint •
✅
بررسی و اصلاح خودکار خروجی‌ها
نکته جالب اینکه
بدون نیاز به نصب Microsoft Office
کار می‌کند و از محیط‌هایی مثل
Claude Code، Cursor و Codex
نیز پشتیبانی می‌کند.
🔗
GitHub:
https://github.com/iOfficeAI/OfficeCLI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/ArchiveTell/6812" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6809">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae562e36c.mp4?token=hiUjlYluD3yE4t07Eic8GVsS_lM4SF6G1VslAUcLEl2QeY-NWXyWlHwli19WUSuTvKRVGInEPRs80H8JyGOfvJH-pOK8Bg1_mQV5z_xZumjjmRKGms_3dZpYQzCdmOPfE5fqXmws43QTigjQW6N0N-fh7X6q4AKS1x5wW-aGPkD-A4XLHQMjTzqSy3Dpl4y1wy7I9JMZAuCU7mfhT2NMq4Z4alDw_kOD7p04UPCU6ALxDBxg2lRur1AatkDAcMhk2I_saDvfncgaZgAF3fNZXrybdIV6juaTrF4J6NCRxLdcK_kzpeT8cB6yS5oWh_JwzT6Lqi5fQCa2k0Qx6-66EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae562e36c.mp4?token=hiUjlYluD3yE4t07Eic8GVsS_lM4SF6G1VslAUcLEl2QeY-NWXyWlHwli19WUSuTvKRVGInEPRs80H8JyGOfvJH-pOK8Bg1_mQV5z_xZumjjmRKGms_3dZpYQzCdmOPfE5fqXmws43QTigjQW6N0N-fh7X6q4AKS1x5wW-aGPkD-A4XLHQMjTzqSy3Dpl4y1wy7I9JMZAuCU7mfhT2NMq4Z4alDw_kOD7p04UPCU6ALxDBxg2lRur1AatkDAcMhk2I_saDvfncgaZgAF3fNZXrybdIV6juaTrF4J6NCRxLdcK_kzpeT8cB6yS5oWh_JwzT6Lqi5fQCa2k0Qx6-66EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">؛‌OpenAI⁩ مدل جدید ‌GPT-Live-1⁩ رو معرفی کرده که مکالمات صوتی با هوش مصنوعی رو به سطح جدیدی می‌بره!
🎙️
‏این مدل میتونه تغییر لحن بده، بخنده و حتی وقتی که کاربر ناگهان حرفش رو قطع می‌کنه، طبیعی‌تر واکنش نشون بده
🗣️
‏و اما یه قابلیت خیلی جالب دیگه: میتونه به صورت آنی به حرف‌های کاربر واکنش نشون بده و حتی به عنوان مترجم همزمان کار کنه!
🌎
‏همین حالا از طریق ‌
ChatGPT Voice⁩
قابل دسترسه!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/ArchiveTell/6809" target="_blank">📅 08:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6808">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🎯
RankGrow | دستیار هوش مصنوعی برای سئو
ابزاری هوشمند که با اتصال به Google Search Console، مشکلات سئوی سایت را شناسایی کرده و لیستی از مهم‌ترین کارهایی که باید انجام دهید را ارائه می‌دهد.
🚀
⚡
ویژگی‌ها:
📊
اتصال مستقیم به Google Search Console
🤖
۷ دستیار تخصصی هوش مصنوعی برای سئو
📝
پیشنهاد بهبود محتوا، لینک‌سازی و سئوی فنی
🎯
لیست اولویت‌بندی‌شده از کارهای ضروری SEO
📈
تحلیل رقبا و کشف فرصت‌های رشد
🎁
۵ اعتبار رایگان برای شروع (بدون نیاز به کارت بانکی)
🔗
https://rankgrow.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/ArchiveTell/6808" target="_blank">📅 07:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کد نویسی رایگان با ابزار هوش مصنوعی FREEBUFF
💻
ابتدا به
سایت
بروید و اکانت بسازید سپس ابزار را اجرا کنید
🚀
— نصب آسان با دستور npm install -g freebuff
🛠️
— بدون نیاز به کلید، کارت یا اشتراک ماهانه
🆓
— مدل‌های پیشرفته از جمله DeepSeek V4 pro و Mimo 2.5 pro و Minimax M3
🧠
— دارای یک وب سایت برای تولید و استقرار برنامه‌ها به صورت رایگان
🌐
کد نویسی خود را با هوش مصنوعی و به صورت رایگان انجام دهید!
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/6807" target="_blank">📅 04:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6806">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎉
Claude Opus 4.8 رایگان در
Supercode (فقط یک روز)
به مناسبت لانچ Supercode در Product Hunt، این ابزار دسترسی رایگان یک‌روزه به مدل Claude Opus 4.8 را برای همه کاربران فراهم کرده است.
🚀
⚡
جزئیات:
🆓
دسترسی رایگان به Claude Opus 4.8 برای یک روز
🤖
استفاده از AI Agent در ترمینال
💻
مناسب برای کدنویسی، توسعه و مدیریت پروژه‌ها
📈
؛Supercode
تاکنون به بیش از ۹,۵۰۰ دانلود، ۸۲ ستاره GitHub و ۲۲۰ کاربر رسیده است.
اگر قصد دارید Supercode را امتحان کنید، امروز بهترین فرصت است.
🔗
https://supercode.sh
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6806" target="_blank">📅 02:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SlipNet-v2.5.5-full-release-arm64-v8a.apk</div>
  <div class="tg-doc-extra">25.7 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6798" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6797">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اقا سرعتی slipnet رو اپدیت کنید
😁
😁</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/6797" target="_blank">📅 00:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎬
FreeCut | تدوین ویدیو با هوش مصنوعی
یک ابزار متن‌باز که با کمک مدل‌های هوش مصنوعی، ویدیوهای خام را به‌صورت خودکار تدوین می‌کند؛ بدون نیاز به API پولی.
🚀
⚡
ویژگی‌ها:
✂️
حذف مکث‌ها، تپق‌ها و بخش‌های اضافی
🎨
اصلاح رنگ خودکار و افزودن زیرنویس
🎥
ساخت انیمیشن و افکت‌های تصویری
🧠
پشتیبانی از Whisper محلی (بدون API Key)
💻
سازگار با Claude Code، Codex و سایر AI Agentها
🔗
https://github.com/Moh4696/freecut
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/6796" target="_blank">📅 23:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">https://www.youtube.com/@localhost_ir</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6795" target="_blank">📅 23:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromlocalhost(Yousef Taheri)</strong></div>
<div class="tg-text">https://www.youtube.com/@localhost_ir</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6794" target="_blank">📅 23:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0akKCHanYEZALNexavN2i3-0NWK6slooHmIYVBIQG7_CCPjXWb3U4AxulUJU4mJMKFhs_RAxCCF5HyKm4aZMwU7mhY6nbWaIwZ4iP0swaOQOjt8lfhGxNcVHc8dD1y9bdiq4zM1sEu8j11CY4m0x-gUn4T-Fi_Inq2Azffs5Z5-UVp9u8A8vd9N0A7IX3H9XoGWgv1P_JN4EXrxKg6VhTsN7FkFJb134js1c-ljZ8j20wZNRDeqN_eLKSLiQ0IKcw67nyxPfC2NVxhm4dMRkq01j85Kb1WWD0ifNHRbeWaLPouivG3pqcz3etAmtZzjUrv0FDolnlDFVneoZ9m8rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Grok 4.5 منتشر شد
⚡️
این نسخه محصولی ویژه از ایلان ماسک است که به‌طور خاص برای برنامه‌نویسی و توسعه‌ی ربات‌ها طراحی شده است.
نکات مهم:
• این مدل به طور مشترک با شرکت Cursor توسعه داده شده و با استفاده از داده‌های واقعی میلیون‌ها برنامه‌نویس آموزش داده شده است.
• سرعت بسیار بالا: 80 توکن در ثانیه.
• قیمت بسیار مناسب: 4 برابر ارزان‌تر از Opus 4.8.
در حال حاضر، به صورت
رایگان
در Cursor و Grok Build در دسترس است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6793" target="_blank">📅 22:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">#اختصاصی
شبیه‌سازهای پلی‌استیشن
🎮
PS1:
duckstation.org
PS2:
pcsx2.net
PS3:
rpcs3.net
PS4:
shadps4.net
PSP:
ppsspp.org
PSV:
vita3k.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6791" target="_blank">📅 20:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانفیگ اهدایی
🔥
vless://878fa338-f275-4bf6-93ea-ef47d8865f59@ps.aramvpn.kdns.fr:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QFc4pPuYwGfyKeoSWnxUkPgaDdEPCPPb2ImpxI-njxI&security=reality&sid=0586e9d2d3a6d12d&sni=www.yahoo.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6790" target="_blank">📅 19:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26e8a3688.mp4?token=m3_irec0w3CTaLdCAmoTBxRPnDUgjFMhZ0jg9Msp-wZLb5z3g5bdtlNjw1iiKbbICcD2UUsKCeTlawMxPMiOA2WVnOA61eFBMqk2ZGnQZUuAW2GMlGxRjhY0E4zylW_bEQiywYkqm4Sx5ZHqsHxHE0bxDpGs5U1JyE14my9toDIwayWO5-yLEhXZaYOJ0xiVA4ScmRzqKkeqgNqDeL56qGHHSXBGvgytpS622_g4IFajvH6c8m3FSHWpIxdVX4Owg4Zzojpj1qZismLrwA6wjUtAG3Tc-1DM0iD5zXUDs35I3qnIfJQ5U2pw9lmVko-LTa3CcdXelTEjVntY5aijtxkNIz-4B0nCyrmjKReC4R_9n4aCGjwZAgodAjzyEicssY_zeAT-9Yad75tuoZCiuk0umZjBZjIGeDH8YNcZseP_nhirEcGQPx0OFgUgi9J7BTAahSyDpct4xSj40KUdulDsbTtLDPaLqOC6T-X6vMK1EO4HHKb8pi5TSaoTNRdA4db-jYKdT5aptlcbJY1vI-EYTOVvOrXcaRxbbtG1iSCiXNyueT1YVZvI0Aky3iyJzNIdoYoSkUgIBC4fkdLHDdIUHVBHm2E9SiPyAAVWRjzSl6vAzGEsJ-WYghQJ9tg4vo83DtnvdVygbXGKAiBNuvsggpm6NnE2R0wgMm0zQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26e8a3688.mp4?token=m3_irec0w3CTaLdCAmoTBxRPnDUgjFMhZ0jg9Msp-wZLb5z3g5bdtlNjw1iiKbbICcD2UUsKCeTlawMxPMiOA2WVnOA61eFBMqk2ZGnQZUuAW2GMlGxRjhY0E4zylW_bEQiywYkqm4Sx5ZHqsHxHE0bxDpGs5U1JyE14my9toDIwayWO5-yLEhXZaYOJ0xiVA4ScmRzqKkeqgNqDeL56qGHHSXBGvgytpS622_g4IFajvH6c8m3FSHWpIxdVX4Owg4Zzojpj1qZismLrwA6wjUtAG3Tc-1DM0iD5zXUDs35I3qnIfJQ5U2pw9lmVko-LTa3CcdXelTEjVntY5aijtxkNIz-4B0nCyrmjKReC4R_9n4aCGjwZAgodAjzyEicssY_zeAT-9Yad75tuoZCiuk0umZjBZjIGeDH8YNcZseP_nhirEcGQPx0OFgUgi9J7BTAahSyDpct4xSj40KUdulDsbTtLDPaLqOC6T-X6vMK1EO4HHKb8pi5TSaoTNRdA4db-jYKdT5aptlcbJY1vI-EYTOVvOrXcaRxbbtG1iSCiXNyueT1YVZvI0Aky3iyJzNIdoYoSkUgIBC4fkdLHDdIUHVBHm2E9SiPyAAVWRjzSl6vAzGEsJ-WYghQJ9tg4vo83DtnvdVygbXGKAiBNuvsggpm6NnE2R0wgMm0zQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چینی‌ها یک "غول" جدید برای تولید تصاویر معرفی کردند: Seedream 5.0 Pro.
ویژگی‌های این ابزار:
🔹
ویرایش لایه‌ای تصاویر
📦
‏
🔹
ترکیب چندین تصویر در یک طرح کلی
📚
‏
🔹
تنظیمات جداگانه برای سبک هر شیء
🎨
‏
🔹
ویرایش محلی مناطق انتخابی
🔍
‏
🔹
تغییر تصاویر بر اساس دستورات متنی
📝
‏
🔹
تطابق دقیق‌تر خروجی با درخواست
📊
‏
🔹
بهبود عملکرد در کار با متن داخل تصاویر
📚
‏
🔹
تولید اینفوگرافیک، نمودارها و سایر مواد بصری
📊
‏
نسخه ‌Lite⁩ رایگان در ‌
Higgsfield⁩
و ‌
Dreamina⁩
قابل آزمایشه
📦
👀
‏نسخه ‌Pro⁩ از طریق ‌API⁩ در دسترسه
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6788" target="_blank">📅 19:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGcECkFpXtwBQsZplaNhebzIl9cY-XzUqr_t18eRkDjRtoIx5nKXfmncGnPoq5zkn6-uYaC7lg3hsYa4TOKQUrvgS7Ac3MQAWJgIXH5GxtlNwdX6xD5WDgEoUPO4_Zfzn-wka6ePVFFLllE8KmBvHImS-Hl9uImBFEb7B_W3GWk7rhO2ODcn5VseobJEg-tDxjMlhKrtH5tRqb6wrUKnCmrFSE8x7d1v60AhNVmTyRFZ5tftP4Exi6H5bN_pTWpvDFCS0PBA2o93ShlnzzOhBOHa2rZAVXzDwFN7fKiuAg_ZkTcJ8TXVtTzGEaXOo9JcWg2nFgY6afi1uYPNMyutcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرورگر
DuckDuckGo
در جدیدترین به‌روزرسانی خود قابلیتی اضافه کرده که امکان
حذف تبلیغات ویدیوهای یوتیوب
را فراهم می‌کند
🌐
این ویژگی با استفاده از فیلترهای
uBlock Origin
کار می‌کند. هرچند ممکن است در برخی مواقع
زمان بارگذاری
یا
بافر شدن
ویدیوها کمی بیشتر شود، اما در عوض می‌تواند تجربه‌ای بدون
تبلیغات
و روان‌تر هنگام تماشای ویدیوهای یوتیوب ارائه د
هد
😎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6787" target="_blank">📅 18:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎥
Recordly | ضبط و ویرایش حرفه‌ای صفحه‌نمایش
✨
یک نرم‌افزار متن‌باز برای ضبط صفحه نمایش که ابزارهای ویرایش را هم در خودش دارد؛ مناسب ساخت ویدیوهای آموزشی، دمو و معرفی محصول.
🚀
⚡
ویژگی‌ها:
🎬
ضبط صفحه، پنجره و صدا
🖱️
زوم خودکار، افکت‌های موس و حباب وب‌کم
✂️
تایم‌لاین ویرایش، برش و افزودن متن
📤
خروجی MP4 و GIF
💻
پشتیبانی از ویندوز، لینوکس و macOS
🔗
https://github.com/webadderallorg/Recordly
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/6786" target="_blank">📅 18:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6785">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🛡
Dangerzone | تبدیل فایل‌های خطرناک به PDF امن
یک ابزار متن‌باز برای باز کردن امن فایل‌های مشکوک مثل PDF، فایل‌های آفیس و تصاویر؛ بدون نیاز به اعتماد به فایل اصلی.
🛡
⚡️
نحوه کار:
🗂
فایل داخل یک محیط ایزوله (Sandbox) پردازش می‌شود
🖼
محتوا به پیکسل تبدیل شده و دوباره به PDF جدید ساخته می‌شود
🚫
کدهای مخفی و عناصر فعال فایل اصلی حذف می‌شوند
✨
پشتیبانی از:
📄
PDF
📝
Word / Excel / PowerPoint
🖼
فرمت‌های تصویری مختلف
💻
قابل استفاده در:
Windows | macOS | Linux
📎
https://github.com/freedomofpress/dangerzone
🐍
زبان: Python
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6785" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbOitG-3BJK4dIzK-6QyeeUG45oazu9WkW7Ed-ozqLuM9SUIlSpsbmbSm_pybpCNOYwOvkLlAa6Pf1BdcYrvhVrxzCrgXoUTzEi-zBNuYLw1vkJmArw0k-Mnfb7K-NkxfmXHgOjPu8ePETXXdfJwbD7GTLAajYOm61UXVhKR4g3tYnRLx1HvhZlaHXsXtTIDuPMpnQ1LQ4abhPepjAelkOBZ0LJLYvc0gBduBg97LaVr3rG2rLyFNDqckkIrvvM9B0LMt_OwcYVwWBqbGSU_9HPjOkQpctuJUtUq4F_SSyzOEML0A6ZtFLu6axLr4tpZ9z4rthFWC3zKnwGddWTiaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">SubFarsiPro v5.0
📹
این ابزار، یک دستیار حرفه‌ای، پرسرعت و متن‌باز برای استخراج زیرنویس از ویدیوها و ترجمه دقیق اون‌ها به زبان فارسی (با لحن طبیعی و محاوره‌ای) هست
GitHub
🐱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6783" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">📊
دنبال معتبرترین رتبه‌بندی مدل‌های هوش مصنوعی هستی؟
اگر می‌خواهی عملکرد واقعی مدل‌های هوش مصنوعی را مقایسه کنی، این دو سایت را از دست نده:
🌐
Artificial Analysis
📈
یکی از کامل‌ترین لیدربوردها برای مقایسه مدل‌ها از نظر کیفیت، سرعت، هزینه، کدنویسی و ده‌ها بنچمارک معتبر.
🔗
https://artificialanalysis.ai
💻
DeepSWE
🧑‍💻
یکی از بهترین بنچمارک‌ها برای سنجش توانایی برنامه‌نویسی مدل‌ها با استفاده از پروژه‌های واقعی و جدید، نه سؤالات قدیمی و حفظ‌شده.
🔗
https://deepswe.datacurve.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/6782" target="_blank">📅 15:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6780" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ارسالی یکی از یوزرای گل
👇</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6779" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6778" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔥
دسترسی رایگان به هوش مصنوعی قدرتمند Fable 5
اگر دنبال تست مدل‌های پیشرفته هوش مصنوعی برای
برنامه‌نویسی، تحلیل و کارهای پیچیده
هستید، این روش می‌تواند جالب باشد.
🌐
پلتفرم
Tasklet.ai
امکان استفاده محدود رایگان از این مدل را فراهم کرده:
✅
۵۶۰۰ کردیت ماهانه
✅
۳۰۰ کردیت روزانه
✅
مناسب برای تست و استفاده‌های روزمره
📌
روش استفاده:
1️⃣
با ایمیل ثبت‌نام کنید
2️⃣
وارد پنل شوید
3️⃣
از بخش انتخاب مدل،
Fable 5
را انتخاب کنید
هر بار کردیتتون تموم شد میتونید اکانت جدید بزنید
🤝🏻
لینک
🔗
:
Tasklet.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6777" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🗂
نام‌گذاری هوشمند فایل‌ها با هوش مصنوعی (
Renamer.ai
)
پایانی برای کابوس فایل‌های بی‌نام‌و‌نشان مثل
Scan_001.pdf
. این ابزار به جای تغییر ساده متنِ اسم فایل، محتوای متنی و تصویری داخل آن را آنالیز کرده و نام‌های دقیق و جستجوپذیر پیشنهاد می‌دهد.
🔥
ویژگی‌های مهم:
*
🧠
درک محتوای فایل:
استخراج فاکتورها، تاریخ‌ها، نام شرکت‌ها و موضوعات داخل اسناد، تصاویر، اکسل و PDF به کمک فناوری OCR.
*
📸
سیستم پیش‌نمایش:
امکان بررسی و تایید اسامی پیشنهادی قبل از اعمال نهایی روی سیستم برای جلوگیری از خطا.
*
📂
پوشه جادویی (Magic Folders):
مانیتور خودکار پوشه‌های انتخابی (مثل Downloads) و نام‌گذاری آنی و اتوماتیک فایل‌های جدید.
*
⚠️
نکته:
نسخه رایگان محدود به ۲۵ فایل در ماه است. همچنین به دلیل پردازش ابری، بهتر است برای اسناد فوق‌محرمانه و اطلاعات حساس مالی استفاده نشود.
🔗
لینک وب‌سایت ابزار
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6776" target="_blank">📅 12:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌐
وب‌گردی و انجام خودکار کارها با هوش مصنوعی (Browser Use)
یک فریم‌ورک اوپن‌سورس (پایتون) که مرورگر شما رو در اختیار مدل‌های هوش مصنوعی (مثل GPT و Claude) قرار میده تا کارهای اینترنتی رو دقیقاً مثل یک انسان براتون انجام بدن.
🔥
ویژگی‌های مهم:
🤖
اجرای خودکار وظایف:
کافیه با زبان طبیعی بهش دستور بدید (مثلاً "این فرم استخدام رو با اطلاعات رزومه من پر کن" یا "این لیست رو به سبد خریدم اضافه کن").
🧠
پشتیبانی از انواع LLMها:
کاملاً سازگار با مدل‌های معروف و حتی مدل‌های آفلاین/لوکال.
💻
ابزار CLI حرفه‌ای:
قابلیت اتصال مستقیم و راحت به ایجنت‌های کدنویسی.
⚡️
جایگزین مدرن:
بدون نیاز به درگیری با ابزارهای قدیمی مثل سلنیوم، خودش با المان‌های سایت تعامل می‌کنه.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/6775" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsYUtZ6ExVlHniPK_FGFEQt-7Y_Sv2b9xFq5jJSyxdd-wZG2HLcptWrdc79Z9HYUCMhh--ozymL_lmZQSW-q_IPbblExNJiFpQQaS09syyhTqkKQ3-T6ofAI1BYtGCS02IC-rXiSAEoKl7OXDtH4S7J2jk5GbjT-0YrWiKe72sJJiWE30Td6SPAemIv-wwA4Qg3bpv6FpxpHAZ6qcP6PitUI3zuH52W3b1RrfShzZAg0wbygjawhrviNIcPLN1gcBZfav85h7yrSyD-HAh0KQGbIVB4VG7MPKk-vaoBUQDGMRYXR_VfsdG3mpCRnvzrgYJEIxhk3mEupypvZpxWGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
معرفی Google Flow
این سایت جدیدی نیست ولی خب بعضی دوستان دیدم نمیشناسنش گفتم معرفیش کنم
😁
اگه دنبال یه ابزار رایگان و قدرتمند برای ساخت تصویر با هوش مصنوعی هستی،
Google Flow
یکی از بهترین گزینه‌هاست.
ویژگی‌ها:
✨
تولید تصاویر با مدل‌های
NanoBanana 2
و
NanoBanana Pro
🖼️
ویرایش تصاویر (چه ساخته‌شده و چه آپلودی) با پرامپت
🪙
ساخت تصویر با
۰ سکه
(رایگان)
📚
امکان ساخت همزمان چند تصویر و ادامه ویرایش روی بهترین نتیجه
🎥
قابلیت تولید ویدیو (با محدودیت بیشتر)
📌
لینک:
https://labs.google/fx/tools/flow
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6774" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6773">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia462dyADEcp-tQr0qKTLrsLoSTy9YzVkFwW3_Iccexga5cB4lJr4lP81DYc-ZFF00Nm73w2386CItOGTvbGmrCgipjFEGk9e7cNfCKcUpiAQBzMG3qqKy0wN4PJmN3DItQwNKv2X8ZxF53691ymGPWjfsx70pPqWBu1d46vn-FZb8pTIYPxoom_b6PmPL12NzD24zqciUaUIu98sNX4kVsDZ6UJBv3yFtwDFVpvHaDkOifqHmyYHt6UGNeLNAuZBJ_eveSgBp3c5-SlrdT15BjuZpLUYTADy0bxODCElOryiqkxB2fitGxevPZlQJ3ytqt_PgGyY_3fUbkWuz8eMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
WLLPR | ژنراتور والپیپرهای مینیمال
اگه از والپیپرهای تکراری خسته شدی، با
WLLPR
می‌تونی توی چند ثانیه والپیپرهای مینیمال و جذاب بسازی؛ اونم دقیقاً با رنگ و استایلی که دوست داری.
🎨
⚡
ویژگی‌ها:
• ساخت والپیپر برای
📱
موبایل و
🖥
دسکتاپ (4K)
• انتخاب رنگ، طرح و استایل دلخواه
• تولید نامحدود والپیپر با یک کلیک
• هماهنگ شدن رنگ رابط کاربری گوشی با والپیپر در بسیاری از گوشی‌های اندرویدی
🌐
لینک سایت:
https://bypedroneres.github.io/ai/
➖
➖
➖
➖
➖
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6773" target="_blank">📅 10:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6772">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA_93QEA5Pikv9eSsydC7R3cC9NwNyozo0Jr0IVKa7ZetSv6HtZu2p44Zf3ush94E8eZqv7T9I84V3Y-MnCNR8r9aypogcc-T-lKjx4G19dHdt1XXODjyxjD5eB7l7oQsif70XFcQFBSvNCnMYDmboxFrSdmkNazCPWQ4KGXqG-7cDTMi6Cp4Bjir35qcQ7XVKFGfGh0VcIxh0UZoihR0VCx19Wk9e4iXacR8VSvtsGIzV_p5haFGkg3h-AIRkiYvT2QbZ-RDqNjJZg1u6Jx2e2YScZxtgQMopioqiKnJOW0DDOp3H9wxx8_BwMocG6rVdjXHEOXgnsqjaIVcjDNuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت OpenAI
نسخه‌ی GPT-5.6 را برای Sol، Terra و Luna از فردا راه‌اندازی می‌کند!
🚀
دسترسی زودهنگام از همین حالا برای کاربران در سراسر جهان فراهم شده، می‌توانید با خیال راحت وارد شوید و آن را بررسی کنید.
🌍
🔍
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/6772" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlgN-ctkEKWW2kFZRwJldQ4I7h-BK4VSxiElMd_kZpySgKRBxUd6IoFLyqVJC_2e321j0s8t4iRJ6BrcnwFkK7md9K1uTymt9L8A6CmtEBdBo0d4mzovm6q3liZoPobKH7meaVlbC0EDApw38lI4TXl4_THXNHgjNgo1IFsNeTkIv56vNaIKvA5vPPmTKnH2YHR07oKU3Zi0bmip9JW6Bivbem5I5BVcn7nMCzxQaanqGwoIuYHxMh7XzhME2R6HbU2Otu1USbMycgleiZ29zEDzlhvFbhNkKjOSp3QqE0hKC8KV-jb0kG7YQ7wfa7gpoWUVXSijcSyz9NtdhgT4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Constrict ناجی شما در فشرده‌سازی ویدیو!
📹
- ویدیو را آپلود کنید و اندازه مورد نظر را انتخاب کنید.
- بدون نیاز به سرویس‌های آنلاین و دستکاری‌های پیچیده در کدگذاری.
ساده، سریع و کاربردی!
https://github.com/Wartybix/Constrict
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/6771" target="_blank">📅 08:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLCe6Qj8cA4jmgyG-rgt_3K4yMLUe19Tp6Shl6dq7PUSfPnrafEwbBjcLQ_dSV-hk4y9HXOFLHQ4oxOpdB9zor4Fdt9RwGc4uQJyHe7LFxErDxfrWizijEd7_PJ5YfmdOvFXuAATB2VDWWMr2wqMO6mQQEM0xPN1PUg6FJcJ6So1lC4OrIp75MbJOz0RHqN9FybRXDDoPks1S74o5p4PrGPDTKGDzJJVuffTz0fJUXzvfOZClXzabwoQzudXH05aoqgcpzUlRPwLfvISKM489KfaRfRwaQRgCStUlaLBWQMEULVxRHTzIpHXzU01PEEa8KncQWjJrWKFYfzr3wp3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تحلیل ویدیوهای یوتیوب، تیک‌تاک و فایل‌های محلی با هوش مصنوعی
؛
Claude Video
یک ابزار متن‌باز است که امکان تحلیل ویدیوها را برای دستیارهای هوش مصنوعی فراهم می‌کند. کافی است لینک یک ویدیو یا فایل محلی را به آن بدهید تا فریم‌های تصویر و متن گفتار را استخراج کرده و در اختیار مدل قرار دهد؛ سپس می‌توانید درباره محتوای ویدیو سؤال بپرسید یا خلاصه آن را دریافت کنید.
⚡️
ویژگی‌های کلیدی:
-
🎬
پشتیبانی از ویدیوهای
YouTube، TikTok، X، Instagram، Loom
و صدها وب‌سایت دیگر
-
📂
تحلیل فایل‌های محلی مانند
MP4، MOV، MKV
و
WebM
-
🖼
استخراج خودکار فریم‌های مهم و متن گفتار (Transcript)
-
🧠
امکان پرسش درباره بخش‌های خاص ویدیو، خلاصه‌سازی و تحلیل محتوای تصویری
-
🤖
سازگار با
Claude Code، Claude Web، Codex
و ابزارهای مشابه
-
🔓
متن‌باز با
لایسنس MIT
🔗
گیت‌هاب پروژه:
https://github.com/bradautomates/claude-video
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/6770" target="_blank">📅 08:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">#Android
#Gaming
🎮
MuMuPlayer 6.0 منتشر شد
نسخه جدید شبیه‌ساز اندروید MuMuPlayer با تمرکز بر عملکرد بهتر و سازگاری بیشتر برای اجرای بازی‌های اندرویدی عرضه شد.
ویژگی‌های جدید:
•
🤖
پشتیبانی هم‌زمان از Android 12 و Android 15
•
🚀
عملکرد روان‌تر و FPS بالاتر
•
🖥
بهبود اجرای چندین Instance
•
🎯
سازگاری بیشتر با بازی‌های جدید
•
⚡
ارتقا بدون از دست رفتن تنظیمات و Macroها
مناسب برای اجرای بازی‌هایی مانند Roblox، استفاده از چند حساب کاربری و تست برنامه‌ها روی نسخه‌های مختلف اندروید.
🔗
https://www.mumuplayer.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6769" target="_blank">📅 05:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTf6od_-7wJDn3x1UQ4rtavjq69IPH7w6-CWTVJ0XtTc1aSpliOm_dHXkJFwaA9UIcWByTvmh2U2xx3IFBu1lxJpmR5cA9GnGSxaC3_C6O-HR9RRkYBAP7-HMyDdsROrgdh-Xknd3Ba-18U8w9HRObbldVYUaScuPD7itqfybG0cKqDJdCAo6biyhlZFMxkOagM-KWiTw2jqqfSY-kuFX-LCHBgVNfIq6UWkmryZgKdzVc1A8-1NGvgI0BmZjg6D857tlFi9kx5hbxX2TO3Gr7yx47wuuf6ywTHw8ELkRzdjCK9gublfZN_2IqNej35SigFSUq0uVph8n-qKoqwLng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
یادگیری شخصی با هوش مصنوعی
موضوع رو بهش بده؛ بر اساس سطح و درک شما آموزش می‌سازه.
✅
آموزش مرحله‌به‌مرحله
✅
امکان پرسیدن سؤال حین آموزش
✅
مناسب هر سطحی
🔗
https://peras.app/
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6768" target="_blank">📅 01:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏
🎁
100 هزار توکن رایگان ( 3 روزه )
‏دسترسی به مدل‌های زیر و صدها مدل دیگر برای کدنویسی :
🔹
‌GLM-5.2⁩
🔹
‌Qwythos⁩
🔹
‌Deepseek 4 pro⁩
🔹
‌Kimi k2.7⁩
🔹
‌Minimax M3⁩
🔹
‌Mimo 2.5⁩
‏
💡
ویژگی خاص:
امکان استفاده از مدل‌های ترکیبی ساخته‌شده توسط کاربران (مثل ترکیب ‌Qwen + Fable)⁩
🔗
‌featherless.ai
⁩
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6767" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtZgg9shoYER6mt1-4D3S_60R8R4SK9E6wqfoHUIiCU2E8WeCRpmtjS2jBV3cPYuB9BxEY_vdFNJ3t1bJ4Y6SeNeXLEf3tRXVMNvIt8kDkNn8tLZT_RCt4sFl6swqoPHDt2Xs9fI4ygxsEIE_46FR4s1g8hflX7EsnFaBWXi-r2inIJYApxBrPU49eqt2RSgu_w88E-p0aBsOzqeDwF4IsFnXXRfP2bNsdtZt-bLYxw4kDCIi3C7K9YJugz6cZ9T1Fc_K9Isg-EU2k7skRVio0cjrFsgr8SsaGl0CjMqq2B2La0B888EV_zDFOLXQhTPA9bc481_Wr65aXvH6T6goQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
PixelRAG
یک پروژه متن‌باز برای Visual RAG که به‌جای متن، اسناد، صفحات وب و PDFها را به اسکرین‌شات تبدیل می‌کند و جستجو را بر اساس محتوای بصری انجام می‌دهد؛ بنابراین جدول‌ها، نمودارها و چیدمان صفحه حفظ می‌شوند.
ویژگی‌ها:
•
🖼
جستجوی مبتنی بر تصویر صفحات
•
📄
پشتیبانی از وب، PDF و تصاویر
•
🤖
سازگار با مدل‌های چندوجهی (Vision)
•
⚡
ابزار CLI برای ساخت و جستجوی ایندکس
•
🌍
API و نسخه دمو آماده استفاده
🔗
https://github.com/StarTrail-org/PixelRAG
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6765" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔐
VoidAuth
یک سرویس متن‌باز برای
SSO
و مدیریت کاربران در محیط‌های Self-Hosted.
ویژگی‌ها:
•
🌐
OIDC Provider
•
📖
LDAP Server
•
👥
مدیریت کاربران و گروه‌ها
•
🔑
MFA
و
Passkeys
•
📨
دعوت و ثبت‌نام کاربران
•
🎨
شخصی‌سازی رابط کاربری
•
🔒
رمزنگاری داده‌ها (
PostgreSQL
/
SQLite
)
⚠️
هنوز Audit امنیتی نشده؛ برای Production با بررسی کافی استفاده کنید.
🔗
https://github.com/voidauth/voidauth
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6764" target="_blank">📅 00:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🖼
جستجوی معکوس تصویر با TinEye
اگر می‌خواهید منبع اصلی یک تصویر را پیدا کنید، نسخه‌های باکیفیت‌تر آن را ببینید یا وب‌سایت‌هایی که از آن استفاده کرده‌اند را پیدا کنید،
TinEye
یکی از بهترین موتورهای جستجوی معکوس تصویر است.
⚡️
قابلیت‌ها:
-
🔍
جستجو با آپلود تصویر یا وارد کردن لینک آن
-
🌐
پیدا کردن صفحات وبی که تصویر در آن‌ها منتشر شده است
-
🖼
شناسایی نسخه‌های ویرایش‌شده، برش‌خورده یا تغییر اندازه‌یافته
-
📈
مرتب‌سازی نتایج بر اساس اولین انتشار، جدیدترین، بزرگ‌ترین یا بیشترین تغییر
-
🔒
حفظ حریم خصوصی؛ تصاویر آپلودشده ذخیره یا ایندکس نمی‌شوند. TTinEye+1
🔗
وب‌سایت:
https://tineye.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6763" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6762">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnfGW87X-epa-F7phdJhtcetKa-cAczkDvLJeAwK_vFcIu1Nyjt5psgdVYebyqTPvt_zZv3VrwiEwhSHDER43SEolag1jtTD2TRtmP6F1Di04ASiSZ26q2efJo_L1GemA-JyZ-rl1iU-AjFI4c_8YvlEOFyBApXYjiZ6f_0hhIjVzM4dPLFhYDs3ajzZJW6fvrHZBiWqbG2lfePvYmNcrsWPlPUdav1iWaS8pLGJZg-elVYVEEIHH9ahViNvB6UlBClUzzIoe9vf-EMdvuEeaKPLlzHZjlYsPF_xJzMtsHQHOqTEofyBHKPYVAPuOdBNs_1C4_B2FkMdjRyf_VWobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
تولید صدا با Pocket TTS روی پردازنده معمولی (CPU)
این ابزار یک مدل
تبدیل متن به گفتار (TTS)
بسیار سبک با
۱۰۰ میلیون پارامتر
است که بدون نیاز به
GPU
، پرداخت هزینه
API
یا وابستگی به سرویس‌های ابری اجرا می‌شود.
⚡️
ویژگی‌های کلیدی:
-
🚀
تولید اولین بخش صدا در حدود
۲۰۰ میلی‌ثانیه
و تا
۶ برابر سریع‌تر از زمان واقعی
روی پردازنده‌های مک.
-
🎙
امکان
شبیه‌سازی صدا (Voice Cloning)
تنها با یک نمونه صدای
۵ ثانیه‌ای
.
-
🌍
پشتیبانی پیش‌فرض از
۶ زبان
: انگلیسی، فرانسوی، آلمانی، پرتغالی، ایتالیایی و اسپانیایی.
-
🔓
کاملاً
متن‌باز (Open Source)
با
لایسنس MIT
و آموزش‌دیده فقط با داده‌های عمومی.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6762" target="_blank">📅 19:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6HkdilOIc9nHOVA9LTuKuZj68ZBUfH2FrHsZ2BQ56A3NHO4j6mg8--JrH0h1hz6sbn-RKFZd7o5wEx31vD1oNlRMzoWbEMTN2L9iDndzxJNBhv1sjZoaUFTAJvBBEbJOSz6k0lxyvpheNVIcdpJylot5ryqI5XQtrJrv1jwv7ofaErcRTVZ8OiTwMf3zKvISKTj3zvK1rlik4ELXLtnsbTPWk524SM9BaQg4sJMyzGg18ahgLqtPKll5_g_xq1OIxHKNDqlCz24qLgdGa7e9JmBFABQyy9tYhgUoNDSQOH5ljYZyeGCqQN9a2qFRmgmiIy1DGB8LHafhq2UQj-6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به دنیای تکنولوژی، لینوکس، شبکه، سرور و ابزارای خفن علاقه‌مندین، یه سر به کانال لوکال هاست بزنین
توی localhost کلی آموزش، نکته کاربردی و تجربه واقعی از کار با سیستم‌ها هست. خلاصه هر چی از دل پروژه‌ها درمیاد، باهاتون به اشتراک می‌ذاره!
🅰
t.me/localhost_ir</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6761" target="_blank">📅 19:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqM0O3OXIgRcyd37nvSCbTn9J2WOcBVkgblGe7TdZzD7dNp-zEwMlt8Ny8AGmhnDYlD7WOUvU0FiqMkSWE6Ba_x4d-tNz3Hg4wxEQl9WAeRZRqQD0zT2g9JPQlF7Yi6v4egxUfYo-zH7F6R9iSwNvnlD40qRnFB_qKYD7xATPLHIUBE7l9nsUMeH7UaNyUvwZ9gqh_Ovq9jwdsN0Skiw7cv_QrIKSLry1lwDH_iLW0xL_ql6XNfsn6U4VSU8u_oga0yPEt0NbuqYkd78s6jJ1IEFrHuBrzEVpCZpo2olx1ZjKj3SXvAiSi-GOf_AnIwoh3Kb8ihxtCAEfKm1DjHwSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلود و مدیریت فایل‌های تلگرام با TDL
یک ابزار متن‌باز و قدرتمند برای دانلود و مدیریت محتوای تلگرام است که امکاناتی فراتر از یک دانلودر ساده ارائه می‌دهد. این برنامه با مصرف کم منابع، سرعت بالا و قابلیت اجرای مستقل، گزینه‌ای مناسب برای کاربران حرفه‌ای تلگرام محسوب می‌شود.
⚡️
ویژگی‌های کلیدی:
📦
اجرای برنامه به‌صورت تک‌فایل (بدون نیاز به نصب)
-
🚀
مصرف بسیار کم منابع سیستم و استفاده حداکثری از پهنای باند
-
⚡️
سرعت دانلود بالاتر از کلاینت رسمی تلگرام
-
🔒
دانلود فایل‌ها از چت‌های محافظت‌شده (Protected Chats)
-
🔄
فوروارد پیام‌ها با مسیریابی هوشمند و جایگزینی خودکار در صورت خطا
-
⬆️
امکان آپلود فایل به تلگرام
-
📄
خروجی گرفتن از پیام‌ها، اعضا و مشترکین در قالب JSON
-
🌐
متن‌باز با لایسنس AGPL-3.0
🔗
گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6760" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQy0LoyLeXFEQWinxFL0_Vsj1doFuHB-upxWwBq17VrD_IhCciCnBaQlEe1mUmbtu6OO4hchJLgB3-1QpRrkKllpB5ezxFoT6qFpYBwVQTyZ3FthuG_yd3gFb4Xy2MgEWc0vpxmHJyXhXycQWU_hCsFGxyj7l1JEl4KCPmOMIOLCqi3q9Tb1o2IHGSjJT5BuQPQNNMa5ebKi-GR9LOTW-ikJssHK6UljE4CqfEOI2FjbQAQZDNn1HyJ1I7g8a2PoqsSvLVjiOcZYspeRTkCWiuz3q06EG9WUclk0DI8_J4zDO3wFOuTnu3CJoRnFThOokLhiiviQI5O6097u3WRERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهبود کیفیت عکس‌ها تا رزولوشن 4K با استفاده از ChatGPT
عکس شما را بهبود می بخشد و جزئیات را تا حد امکان حفظ میکند.
😮
پرامپت :
Restore and enhance an old damaged photo. Remove scratches, stains, and noise. Reconstruct faded or torn areas while preserving original details. Slightly sharpen the image for better clarity, but keep it realistic. Apply natural and era-appropriate colors to skin, hair, and clothing. Use a soft, balanced background color without being too striking. The final result should look like an old photo that has been realistically restored and colorized, while respecting its original appearance.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6759" target="_blank">📅 11:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhVrQXEhRXPdMVW8FUKJaV76oQIxyD3KGBtX0oTizkmJ-KzVjjxiLpgmG-VttJ9D69ZAa3gSCL3hD9TjGFfTe6SUxqMCttwdEl63YFSUSnnnZm1DwZmN8k3aZGDQdVSf4pwFM48ndN_AWb4G1e-GoKCo_uwfzpqO2d3XBPfqQbrdvF3sRLD69kufN_LUvSDnmTpKxBLHY2jldWBVApIWFzSbZkI4UReJ0aJUYeNmYQpjJEBPoU3t6hMjOID47x8p9LSznC4GzR0vSszf2sXP_ArPpMza8lTHFNgZZ2kb18RXD6wynJefeeXrrqPX1cvzOB0aezIcOZBDhguTyzmujg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اپ‌استور متن‌باز و جایگزین Appteka برای اندروید
یک مارکت رایگان برای دانلود، مدیریت و به اشتراک‌گذاری برنامه‌های اندرویدی که بر پایه مشارکت کاربران (Community-driven) فعالیت می‌کند.
🔥
ویژگی‌های مهم:
*
📦
استخراج APK:
خروجی گرفتن از برنامه‌های نصب‌شده (حتی برنامه‌های سیستمی) بدون نیاز به روت (Root).
*
💾
مدیریت فایل‌ها:
قابلیت بکاپ‌گیری، بازیابی و نصب مستقیم اپلیکیشن‌ها از داخل خود استور.
*
💬
تعامل کاربری:
دارای چت گروهی، سیستم نقد و بررسی، لیست علاقه‌مندی‌ها و دریافت نوتیفیکیشن آپدیت‌ها.
*
🔒
امنیت:
اسکن خودکار برنامه‌های آپلود شده (از آنجا که محتوا توسط کاربران قرار می‌گیرد، بررسی منبع قبل از نصب پیشنهاد می‌شود).
*مناسب برای توسعه‌دهندگانی که می‌خواهند برنامه‌هایشان را راحت منتشر کنند یا کاربرانی که به دنبال یک استور بدون محدودیت و ابزاری برای استخراج APK هستند.*
🔗
[لینک دانلود یا گیت‌هاب پروژه
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6757" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675041278d.mp4?token=UDMp0LETvFLUZBEDWqu7ikiusQGzAGw5w-y5LdOCfFWta7KtWBZ3q8ubDfCp413ksOUZDW2NZBtNK9QpZwCJkXw10et0fFQNraDJ4jZR8OhLxwpCcd7jK5A7PRYRQEQBAZ1EzzNv_FHDmYxZkPEz3DugLPzdjZhNPY15CmEPMG9z7KWrFRc1SA79MngdYun1wDn5FVvwXON19Wjpx_2r0Z77REtbBayXrKx9yq_F2-4VCbRRd5H9ZheleM6nky7T5paHcPf1W1LF83Gj6xDH-Ze9N_vhiL4w2KulGRjxwi7WsES1FAX0e1K_WkMqly7MpsICc_K6IgmYAv2hrse_LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675041278d.mp4?token=UDMp0LETvFLUZBEDWqu7ikiusQGzAGw5w-y5LdOCfFWta7KtWBZ3q8ubDfCp413ksOUZDW2NZBtNK9QpZwCJkXw10et0fFQNraDJ4jZR8OhLxwpCcd7jK5A7PRYRQEQBAZ1EzzNv_FHDmYxZkPEz3DugLPzdjZhNPY15CmEPMG9z7KWrFRc1SA79MngdYun1wDn5FVvwXON19Wjpx_2r0Z77REtbBayXrKx9yq_F2-4VCbRRd5H9ZheleM6nky7T5paHcPf1W1LF83Gj6xDH-Ze9N_vhiL4w2KulGRjxwi7WsES1FAX0e1K_WkMqly7MpsICc_K6IgmYAv2hrse_LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6756" target="_blank">📅 10:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">📱
تست خودکار رابط کاربری و اپلیکیشن‌ها با Maestro
یک فریم‌ورک متن‌باز فوق‌العاده برای تست End-to-End (E2E) در اندروید، iOS و وب. با این ابزار نیازی به کدهای پیچیده تست (مثل Appium یا Selenium) ندارید و سناریوها رو خیلی راحت با فرمت ساده و خوانای YAML می‌نویسید.
🔥
ویژگی‌های مهم:
*
📱
کراس‌پلتفرم:
پشتیبانی از برنامه‌های Native، فلاتر و React Native.
*
⚡️
اجرای هوشمند:
بدون نیاز به کامپایل فایل‌ها، همراه با سیستم کنترل تاخیر (Smart Waiting) برای جلوگیری از خطای لود نشدن المان‌ها.
*
🖥
ابزار بصری:
دارای یک محیط رایگان (Maestro Studio) برای ساخت و رکورد تست‌ها به صورت ویژوال و بدون نیاز به ترمینال.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6755" target="_blank">📅 10:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚀
۳۰ سایت رایگان ساخت ویدیو با هوش مصنوعی
#اختصاصی
اگر دنبال
Veo 3، Sora 2، Kling
و سایر مدل‌های ساخت ویدیو هستید، این لیست را از دست ندهید.
⭐️
بهترین‌ها
VeoAIFree
→
https://veoaifree.com
(بدون ثبت‌نام و واترمارک)
Vixdo
→
https://vixdo.art
(۱۷۰ اعتبار رایگان + بدون ثبت‌نام)
Pollo AI
→
https://pollo.ai/m/google-veo-3
(چندین مدل در یک پلتفرم)
GlobalGPT
→
https://www.glbgpt.com
(Veo، Sora، Kling و Wan)
Leonardo AI
→
https://leonardo.ai
(اعتبار رایگان هفتگی)
🎁
بدون ثبت‌نام
VeoAIFree • TryVeo3 • AIVideoGenerator • Veo3Free • Videomaker
💰
اعتبار رایگان روزانه
VeoE • EaseMate •
Veo3.us
• AIEase • Aitubo • Pixnova • SeaArt
🧩
پلتفرم‌های چندمدلی
Veo3AI • Pollo AI • GlobalGPT •
Media.io
• Novi AI
🎬
ابزارهای تخصصی
Digen
→ Lip Sync
MindVideo
→ انتخاب نسبت تصویر
DomoAI
→ تبدیل تصویر به ویدیو
Klap
→ تبدیل ویدیوهای بلند به Shorts و Reels
Fal.ai
و
Eachlabs
→ مناسب توسعه‌دهندگان
💾
این پست را ذخیره کنید؛ احتمالاً بخشی از این سرویس‌ها در آینده پولی یا محدود خواهند شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6754" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO5E6KJ3DoiQSX1PiR0mtMIh_JBfL2eBJza3Z2Klis1e-vJnIbnTfINvbSqq3LebfhpLQCv0x6CAuAL6S9E7YD2LIUOPgySE49G0UkT-sFnFmnOU6yhf5hQwbmqBb7WQGLkpBJPrXTcJoLJ_7Lo0_l0tMuuobjQXTOy-8IpPD_90YrNo1VFIOzjiOv2kGSCVH2QS2-n4CitXQSazbHtjSv9tuj-cEwx703AcVL3IDJ5S8l_AwAgAryqQP_wibYp5_nAXsVz_Dsw2WVy4AwJJ-DEqwZzWyM6I7rwc82TzmTqJbD1zh7FO5yWhmEIIrnO2ZTaTJVPHDHZhjtGlqi0miw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بقول نیچه
در چنین گفت زرتشت
«من از خردِ خویش به جان آمده‌ام، چون زنبوری که انگبین [عسل] بسیار گرد آورده باشد. نیازمندِ دست‌هایی هستم که به سویم دراز شوند. می‌خواهم ارزانی دارم و بخش کنم...»
بیاین مثه نیچه باشین و این عسل و انگبین چنل رو به سوی دستان دراز بسپارید
نیاز داریم به حمایت شما
❤️‍🔥
https://t.me/ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6752" target="_blank">📅 01:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6751" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor
لینک ویدیو آموزش:
https://youtu.be/pN3LxWzDtKI
خود پروژه:
https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6750" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نیاز داری سورس کد کامل یه سایت (به همراه تمام فایل‌ها، تصاویر و CSS) رو یکجا برای استفاده آفلاین دانلود کنی؟
💾
🕸
ابزار اوپن‌سورس Website-Downloader با استفاده از قدرت wget کل سایت رو میرور (Mirror) می‌کنه و یک فایل فشرده بهت تحویل میده.
🧵
👇
#توسعه_وب
#اوپن_سورس
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6749" target="_blank">📅 22:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZXjPr7BXZvbbK2W8SgRrXZL_tyocr5cSbuvJc9dAh1ts93yNkX9Ihltz1BuVko6CtdD7igsZxurwOXS2pUqJnQUwh8LJOh5tYvhVMXq0wLLXDa2AHjYUWaxSJFl8bnSI5NnZpE8yoTJgnq2kGmNzLBjq_voLKiOqVQbc5ckSOp4LXx7bdCKSCW8_iAAWY8cQLAvKHYr9Pht-1PAt2hQzQKEarRz9AQB047aYJl1aqDeD7-44wrhXVYXy5RiGaWmzvW4XvA9pqNugZHhNLBRYYPQ3RW3EnZ99H_grLtvTk529sD-NU3x_PSrxBL5q5SO81vCqI2zd307STnkAnGouA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074191361432035554</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6748" target="_blank">📅 21:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsITqtJQDW1pWBEsT_3_aYJ0x63miOVt9rwQJhhlv5VUHeSPdZlozLB8tOrpgnYO3GIEHtMJlTfZK8Wt3H48JH7BXTSgsydBmDpNznGJhihsU9pKuyDeYhlQJqpInF53JnMn9bheMphimGhfJiVEj8p4ucwEwRsBZwVYQfyM1VehtvE4isqxEYuKEUFfhk8-vrVIsU9XFWGJd-jYGzbSYh1tI24j5Ho8jMdodx1DObVtf87bLXfNDZl09IDEQKzIVheii5FgsImULsRYeW22W-UiW9mCrFySmIeT_lFgtq-0qfpohLhB7Teaz0_TmTjdt61ajf_SC7vse0ArD_b7Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🗣️
هوش مصنوعی‌ها دارن با هم «زبان راز» می‌سازن!
🤫
🤖
‏تا حالا فکر کردی اگه ‌AI⁩ها یه زبانی داشته باشن که ما متوجهش نشیم، چی میشه؟
🤔
‏پروژه جدید
‌GLOSSOPETRAE⁩
دقیقاً همین کار رو انجام میده:
🔹
تولید خودکار زبان‌های مصنوعی (از آواشناسی تا دستور زبان)
‏
🔹
ارتباطات غیرقابل‌فهم برای انسان
‏
🔹
کدنویسی خالص با جاوااسکریپت (بدون وابستگی خارجی)
🚫
📦
‏این فقط یه ابزار نیست؛ یه پنجره به دنیای ارتباطات پنهان ماشین‌هاست.
🔍
🧠
‏
🔗
لینک پروژه:
github.com/elder-plinius/GLOSSOPETRAE
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6747" target="_blank">📅 21:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPgdvR5LfCBf4J3PHCks5kmTZK3yahJMV1s7SRMY5r-G674Kzl70WkHslmNTlvo9W_7SatFdt1CXFBdpPyzgD4ukjtkb7rWEVWRiFn-ttvkIEwOq4HOfEMTGgymvg2Rw-C91Trk6QhhCPDIEf1xebuExxBHjvx4zkXnA5a_8gRLVmXrEikKSaFxE__jSYdggjuhZp1xL0K6jDjF1Yc-J8pNMRX3fwFy93K5EX23QusZRdxGMZG6Fv299S2d9mlxJBZ0La-EH62MwDp9UN4HPcsk3DvOVL68l3M3fFrE_x5ElHtvhCV8QbPbSfWMwHaGqcS5R6kpvr0XOL3TzkNXBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆓
دسترسی رایگان به غول‌های هوش مصنوعی!
🤖
‏‌یه گنجینه از ‌API⁩های رایگان روی ‌GitHub⁩
💎
🔹
مدل‌های قدرتمند: ‌Gemini Flash⁩، ‌Qwen3⁩، ‌DeepSeek⁩ و ‌gpt-oss⁩
‏
🔹
سرویس‌های متنوع: ‌Google AI Studio⁩، ‌OpenRouter⁩، ‌Cloudflare⁩ و ‌GitHub Models⁩
‏
🔹
یکپارچه‌سازی آسان: اتصال راحت به ‌Cursor⁩ برای کدنویسی سریع‌تر
🚀
‏فقط یادت باشه محدودیت تعداد درخواست (‌Rate Limit)⁩ رو رعایت کنی تا سرویس‌ها قطع نشن.
⚠️
⏳
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6746" target="_blank">📅 19:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbpJEV366n-Bf-GgcY8Wf9clTM2cBN1RgwCTHw6RbFyejax3kOJtYUlAr7B4_2MD2LVnFSXYZ7xJ0EaLSu7aEgHuBFg7KqA9APlETBMF78e5LB_ZecFSJQkW2TFlTqX70yN4VEKQjcQJh0FZMxWHmkvSfTDUcla9l3IY7JKORggRA5xWJjalNvZ3hC7vp21EqezsF1RiVS27S8V84OwoJVUMLFX_4KLc813rt8BdJTgeMOnlAdBS7_NYcoeVKVgjIcJhg1E725K1aX3R6XAeYajwdZzYU_VeV-BJznaJCDffLaqRjalM4zAMR08PzxQCqlwJEg7FgKjPrG4HPZ8FGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎨
حذف پس‌زمینه با یک کلیک!
🖱️
‏این ابزار وب پس‌زمینه عکس‌ها رو با دقت بالا جدا می‌کنه و کیفیت اصلی رو حفظ می‌کنه.
✅
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6745" target="_blank">📅 18:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910f222215.mp4?token=WY25y_QhqWYb3h9_t9q3RwFoSQNVB-Jo1vl90zrEEozJ1RWDrlBYg0FgS8YDMrNywYstxqNpB1sx2qCIcnKKC3bZl7DCezBGGlHo27wEgSv7Zxx1quVkPTNYDaQtn0IXLHzDnVhaYBxoLQDeFWLsreRcU-wribpwD4y2swdQD30_8mqUFiy7yQrcqF9ew-B3JqDA4KUfL0L4UteJPowfPRxfnS2rwq1Heaed0xl01ssRe7oEE-biv1CsCDXK5ZujyECBf2vnR1h0kVof9ETfelUXjst5jwgpuKsA3kBhmBk3wgdG0dHaE1p_lGH6MdB8DwY3h39vwvBQObUj-i-Jsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910f222215.mp4?token=WY25y_QhqWYb3h9_t9q3RwFoSQNVB-Jo1vl90zrEEozJ1RWDrlBYg0FgS8YDMrNywYstxqNpB1sx2qCIcnKKC3bZl7DCezBGGlHo27wEgSv7Zxx1quVkPTNYDaQtn0IXLHzDnVhaYBxoLQDeFWLsreRcU-wribpwD4y2swdQD30_8mqUFiy7yQrcqF9ew-B3JqDA4KUfL0L4UteJPowfPRxfnS2rwq1Heaed0xl01ssRe7oEE-biv1CsCDXK5ZujyECBf2vnR1h0kVof9ETfelUXjst5jwgpuKsA3kBhmBk3wgdG0dHaE1p_lGH6MdB8DwY3h39vwvBQObUj-i-Jsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧰
کالکشن ۱۷۰ ابزار کاربردی و متن‌باز
تمام این ابزارها تحت وب هستند و نیازی به دانلود فایل یا ساخت اکانت ندارند:
🎬
مدیا: ویرایش حرفه‌ای ویدیو و صدا
🖼
تصویر: فشرده‌سازی، تغییر سایز و افکت
🔄
مبدل‌ها: تغییر سریع فرمت فایل‌ها
📄
اسناد: ادغام، جداسازی و ویرایش PDF
📰
داده: پارسرها و پنل‌های مانیتورینگ
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6743" target="_blank">📅 16:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwdS4UKfQUHHSxdPhhhGC-xO1j7miSI3tq6oRkwj6ykKvDe_QO9ixZI5RMZ8VYssNBFyXsTKu36vimwYhV6R2u1RF4H_PIRJcir-5fr8CWHsO6DRlpx91cTEeuAjxhGoFxtA6Mc2OTH3GR45KtZXVLgLWXO_X2H55ibnejcGDEwayjgKvIp1aFLx7xudpxhMQByONsPXXWzKIgNSN3IeXb1Vz6a_buji9xEFklMjqkdX4D1YVGmeKLAfJnUrE4j8QSHlm8Mb3_bojPGzg30ts6-rHeTxrVmNDeiHJVEKa9B6DJvpEQVPY7UdgUET6hRkA5kL5OVI72qF5glHy_4jJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
راهکارهای اتصال پایدار و پرسرعت برای اینترنت آزاد
🔹
پشتیبانی از V2RayNG، WireGuard، SlipNet و ArgoVPN
🔹
ارائه اشتراک‌های عادی و گیمینگ متناسب با نیاز کاربران
🔹
انتشار کانفیگ‌های رایگان، آموزش و پشتیبانی
🔹
تست کیفیت اتصال قبل از استفاده
📢
TirexNet؛ همراه شما برای دسترسی بهتر به اینترنت
🤖
Bot:
@TirexNetBot
💬
Support:
@HRMP1386</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6742" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏
🚀
دسترسی رایگان به غول‌های هوش مصنوعی!
‏اگر دنبال جایگزینی برای ‌Agent Router⁩ هستید،
سایت ‌
Bluesminds⁩
فوق‌العاده است. با ثبت‌نام، 100 دلار اعتبار اولیه هدیه بگیرید و با مدل‌های قدرتمندی مثل:
🔹
‌GLM 5.2
🔹
‌Qwen 3.6
🔹
‌Minimax M2.7⁩
🔹
‌Mimo 2.5
‏کار کنید. همین حالا امتحانش کنید و پروژه‌هاتون رو به سطح جدیدی ببرید!
✨
🔗
Docs
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6741" target="_blank">📅 14:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6740" target="_blank">📅 12:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون فضولی میکنه. یکی میفروشه به دلال های داده (مثه گوگل و مایکروسافت و...) یسریا هم که حریم خصوصی محورن.
الان هرمس اینا رو واقعا نمیدونم. هر چی بیشتر این مدلا رو بیشتر وارد چیزاتون میکنین، ریسکش بالاتر میره در کل. باز این شرکتا اروپایی نظارت بالاتر هست ولی نمیدونم طرف خوشش میاد از ی مدل میگه به به چ مدلی چقد قابلیت بذارم چنل، ملت کلی ویو میزنن استفاده میکنن. طرف به تلگرامش و... هم وصل میکنه بعد اخر بعد چند روز میگه ببخشید هرمس رو شخصی ران نزنید
اینو میخواستم چند روز پیش بذارم ولی گفتم ولش. ولی حس کردم بهتره بگم تا پیشگیری بشه بهرحال</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6739" target="_blank">📅 12:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-PZFs8Cl5-Gd2IWMQlSyGK2_RWSUDHJ0ILYujM1sxuT--rpZlrUtXURZjBlQcbTZpHIyklPcKnOFVychs6QUB3WAaKtXsLCocsKvVVJPwpc9XMMyVRpJGgIMhWMxK-_hh_U9v0kiEwJLqGitvRDd-mVBG9q9-iTy9WfnwNkGH_T7mG6GwJsQ_C1TACIKbeL29GiMBKgafu1zf2hCIQasTezCF1l4kPxhIsHq6eeoWa4bUTJxfFBLSvZ59owbKpKeHdjeYPBwnk2BtXCtuRwSqbC6javsrOPfnzQ3tXjMizQVppgQIRa5tLXww0XPe94M4MmpUDr5UBUEvYSUhUvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074039784629014892?s=20</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6738" target="_blank">📅 11:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7iGx_HauDGxzciUtVn2YXJjsJp60mMpesxVHHcEkHEvLwC39LY6FiLbMJE4cqTn3NN0QUJutEFxjIjhxbZi9njb_wDc2pvDFzxZQAlESIlVIaufV5-aPQzdj_1e6xETqr2E6_I3qaHKGBiRa-5iAUXvJai6CigRwWt_nWEt7uZKXDIntC1ZuWMWseLe_DvQdlAf_9rLAYOGyQ-JVxTFMTCplPBVLOMe-O_YU7Fs5VJgFOgPO2y4M_6GkAcRrRYOyTD7FhIOosg5LD_GhDDytTXb3fv7svi7UHT-ACaeoccv2JgXoteYC_usRCxhZ11BRiwrgXVWbiBytbVT2WoSMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
اجرای هر بازی اندرویدی مستقیماً روی کامپیوتر
یک شبیه‌ساز رسمی از گوگل که واقعاً سریع است و به راحتی از رقبا پیشی می‌گیرد.
🔹
پشتیبانی کامل از اندروید 14، از همان ابتدا.
🔹
عملکرد از طریق Hyper-V — همه چیز پایدار و سریع است.
🔹
هر فایل APK را بدون هیچ مشکلی اجرا می‌کند.
🔹
بدون هیچ بنری یا تبلیغ مزاحم.
🔹
بازی‌ها بدون هیچ‌گونه کندی یا تأخیر اجرا می‌شوند.
دستورالعمل به زبان فارسی
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6737" target="_blank">📅 10:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nh0N0deVIqndhKiPTqSgNg1gGJSStDuSno1qjAKL7dG04M_TlOfBfF_rFObiiIFhRg9qZL2xV1qy1mPFeNsWbyoapiw_87O9q3iCvSGxbRAhWZuOyQ5ypI5ZkrHauBrnBzhZSjqadlofhF9dNID2TACF_mUo1P710fLQHZmClVJA2S58YuPHi6n9EYK_3pBNXQc3ugFepRw-xabKOZwPWZAZ9pR0er6HIQriaVfU7UDf8300_kPDTiT9bT4vVKbnWiwlpA3WxFZdUfsdtq8efN9ozugPEBjQgfApxA1Mabc0VoVPL53wNydX47QcO-UrVVL3JIc_PDPeI8ocyty9AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
کپ‌کات رو فراموش کنید؛ این ابزار رایگان و بدون نیاز به نصب جادو می‌کند!
‏اگر برای ادیت ویدیوهای خود به دنبال یک ابزار سبک، همه‌فن‌حریف و کاملاً رایگان هستید، پروژه متن‌باز ‌OpenReel⁩ دقیقاً همان چیزی است که نیاز دارید. این ادیتور قدرتمند مستقیماً درون مرورگر شما اجرا می‌شود و نیازی به نصب هیچ برنامه‌ای ندارد.
‏
💡
چرا ‌OpenReel⁩ یک جایگزین بی‌نظیر است؟
‏
🔹
ادیت چند لایه حرفه‌ای: قابلیت ویرایش همزمان چندین لایه ویدیو و صدا همراه با پیش‌نمایش زنده و بدون افت سرعت.
‏
🔹
امکانات کامل کپ‌کات: دسترسی به افکت‌های متنوع، ترنزیشن‌ها، پرده سبز (‌Chroma Key)⁩، کنترل سرعت و فریم‌های کلیدی (‌Keyframes)⁩.
‏
🔹
ابزارهای جانبی کاربردی: قابلیت ضبط صفحه نمایش، کار با متن و زیرنویس، و خروجی گرفتن سریع با فرمت‌های ‌MP4⁩ و ‌WebM⁩.
‏
🔹
کاملاً رایگان و امن: بدون نیاز به ثبت‌نام‌های پیچیده، پرداخت درون‌برنامه‌ای یا واترمارک روی ویدیوها.
‏بدون درگیر کردن حافظه سیستم یا گوشی، همین حالا ادیت ویدیوهای خود را در سطح حرفه‌ای شروع کنید!
🔗
Site
|
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6736" target="_blank">📅 10:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6735">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFajKJ8O6uKDLwoAP6nMRJOHHL9kJtw687RUu6ttkI72_D_lJWB3U4IbHcByMSZEdnVQ4LRdWv_-m_jjJ7qXOpieLkkY0NjOFl7BIMpWPmDiB23NRdccyewsMRXlBEU1Ij40aK-CrHGByqLQiiThDBcvZbPMcBQCw8bi-Esm-tS2tJ97OAzwJc3O3W85kC44cCXbECLNMg-ctHdaNn4ZWrZLH_UbmySqqeB3ksPZyO71T3C9m9xDZMVxcRcAM7VfnZ7d9_h337I2kpLFSvd5yhBoNYSf1J3g-zwVRnvVnI6aez5hkXXote4jkcLh5HF8jGz2vG8xoWqAZHOvE_PCIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تمام غول‌های هوش مصنوعی دنیا، زیر یک سقف!
‏دیگه نیازی نیست برای تولید متن، کد، ویدیو یا عکس، بین ده تا سایت مختلف چرخ بزنی و کلی اکانت پولی بخری. این پلتفرم همه‌چیز رو برات یک‌جا جمع کرده!
‏
✨
چرا این ابزار بازی رو عوض می‌کنه؟
🔹
تیم رویایی در یک پنجره:
به راحتی و با یک کلیک بین قوی‌ترین مدل‌های دنیا یعنی ‌ChatGPT⁩، ‌Claude⁩، ‌Gemini⁩، ‌Grok⁩ و ‌Kimi⁩ جابجا شو.
‏
🔹
تولید همه‌جانبه:
از نوشتن کدهای پیچیده و متن‌های خلاقانه تا خلق تصاویر و ویدیوهای جذاب، همه در یک محیط واحد.
‏
🔹
سهمیه رایگان روزانه:
هر روز کلی توکن رایگان بگیر و پروژه‌هات رو جلو ببر.
https://www.easemate.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6735" target="_blank">📅 10:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6734">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3TlPnFK09aJqXwikW9V9GY_KCCT8zsfJD6CELCN5pyS4BAVYxSv8-ttbAcRRDrmrYu0JJ0QYufEFpvIWPh-5MyLkiAZ4nGbd5CG7i9sNVg_MDSTlmcwRRoV_8PSwn2HKr9mCYnrh3XdoMCew1KJ0JWSkh6xLwbYgAEuB-d7L53Qss3sRvIfEYd_l9sRVRt7UKJO7602vp817YqeIr7CXkhuwUUnA296R_TwJNL4i7F5sxw-kSepS11bBMZzsr1lIVCcO-81wA84d01konXQBRNunOkqDqzCw0Ltq900aVOQ9tLKpbGsi936bOACBINbjCED4QKoBREiBjFIsfyONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
غول هوش مصنوعی، بالاخره رایگان و بی‌دردسر!
‏دیگه نیازی به خرید اکانت پرمیوم یا دردسرهای ست کردن ‌API⁩ نیست؛ از امروز می‌تونید به صورت کاملاً رایگان توی پلتفرم ‌Tabbit⁩ با شاهکار جدید ‌Anthropic⁩ یعنی Claude Sonnet 5 گفتگو کنید!
💻
✨
‏
💡
چرا این خبر بمبه؟
سونت ۵ در حال حاضر یکی از باهوش‌ترین و دقیق‌ترین مدل‌های دنیاست که حالا بدون هیچ محدودیتی در دسترستون قرار گرفته. فقط کافیه وارد سایت بشید و چت رو شروع کنید
https://tabbit.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6734" target="_blank">📅 09:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🗂
هیچ‌چیز رو دور ننداز! معرفی Karakeep؛ بهشتِ آرشیوکارها و خوره‌های اطلاعات
🧠
اگر شما هم از اون دسته‌اید که روزانه ده‌ها لینک، مقاله و ویدیو رو برای «بعداً خوندن» ذخیره می‌کنید و در نهایت بینشون گم می‌شید،
Karakeep
(با نام قبلی Hoarder) دقیقاً برای شما ساخته شده. این ابزار یک جایگزین فوق‌العاده، سلف‌هاست و متن‌باز برای برنامه‌هایی مثل Pocket هست که با جادوی هوش مصنوعی ترکیب شده!
🔥
چرا Karakeep بی‌نظیره؟
🤖
تگ‌گذاری خودکار با AI:
با استفاده از LLMها (حتی مدل‌های لوکال مثل Ollama)، محتوای شما رو بررسی کرده و به صورت خودکار تگ‌گذاری و خلاصه‌نویسی می‌کنه.
🗄
آرشیو ابدی صفحات و ویدیوها:
برای جلوگیری از حذف شدن لینک‌ها (Link rot)، کل صفحه وب رو به صورت آفلاین ذخیره می‌کنه و حتی ویدیوها رو به کمک yt-dlp دانلود و آرشیو می‌کنه!
🔎
جستجوی قدرتمند و OCR:
متن داخل عکس‌ها رو استخراج می‌کنه و می‌تونید در کل محتوای ذخیره‌شده (فول‌تکست) جستجو کنید.
📱
همه‌جا در دسترس:
دارای افزونه برای کروم، فایرفاکس و سافاری، به همراه اپلیکیشن اختصاصی برای iOS و اندروید.
🔌
تعامل با ایجنت‌ها:
کاملاً سازگار با ایجنت‌های هوش مصنوعی (مثل OpenClaw) برای مدیریت خودکار اطلاعات از طریق CLI.
اسم این برنامه از کلمه عربی «کراکيب» (Karakeeb) الهام گرفته شده؛ به معنی خرت‌و‌پرت‌هایی که شلوغ به نظر می‌رسن اما پر از ارزش و خاطره‌ان و نمیشه دور ریختشون!
🔗
لینک مخزن گیت‌هاب پروژه:
https://github.com/karakeep-app/karakeep
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝑒𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6733" target="_blank">📅 08:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.  اینطوریه که ازت آی‌پی و پس رو میگیره  بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ... خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌  دیگه نیاز نیست دستور های ترمینال رو بدونی…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6732" target="_blank">📅 04:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚀
آموزش نصب OpenCode و استفاده رایگان از مدل های هوش مصنوعی زیر :
🔸
Mimo 2.5
🔸
Deepseek 4 flash
🔸
Nemotron 3 Ultra
🔸
Big Pickle
🔸
North Mini Code
🔘
آموزش نصب در موبایل
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
3) نصب OpenCode
npm i -g opencode-ai
4) اجرای OpenCode
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس‌ :
opencode
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر OpenCode را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
opencode
🔘
داکیومنت رسمی برای نصب در جاهای دیگر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6731" target="_blank">📅 02:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎬
تدوینگر اختصاصی شما داخل ترمینال! معرفی ابزار فوق‌العاده Video-Use
🚀
دوست دارید فقط با چت کردن با عامل‌های هوش مصنوعی (مثل Claude Code یا Codex) ویدیوهاتون رو ادیت کنید؟ پروژه اوپن‌سورس
video-use
دقیقاً همین کار رو می‌کنه. فقط کافیه ویدیوهای خام رو بریزید داخل یک پوشه و با زبان طبیعی بهش بگید چی می‌خواید تا یک فایل نهایی (
final.mp4
) ترتمیز بهتون تحویل بده
.
🔥
چرا این ابزار انقلابی و متفاوته؟
🧠
پردازش هوشمند و ارزان:
به جای اینکه کل ویدیو رو به خورد LLM بده (که به شدت گرون و پرخطاست)، فقط یک فایل متنی سبک از ترانسکریپت با تایم‌استمپ دقیق کلمات و در صورت نیاز اسکرین‌شات‌هایی از تایم‌لاین (شامل فرم تصویر و موج صدا) رو بررسی می‌کنه.
✂️
حذف اتوماتیک اضافات:
تپق‌ها، مکث‌های طولانی و کلمات اضافه رو به صورت خودکار تشخیص میده و هوشمندانه کات می‌زنه.
🎵
تدوین بی‌نقص:
روی تمام کات‌ها ۳۰ میلی‌ثانیه فید (Fade) صوتی میندازه تا هیچ‌وقت صدای پرش کات رو نشنوید.
🎨
زیرنویس و انیمیشن:
می‌تونه زیرنویس‌های کاستوم (مثلاً کلمات دوتایی بزرگ) روی ویدیو بندازه و با ابزارهایی مثل Manim ،Remotion و HyperFrames انیمیشن تولید کنه.
🤖
حلقه خودارزیابی (Self-Eval):
قبل از اینکه خروجی رو به شما نشون بده، خودش ویدیو رو بازبینی می‌کنه تا پرش‌های تصویری یا مشکلات صوتی رو پیدا و برطرف کنه.
این ابزار مثل این می‌مونه که یک کارگردان و یک تدوینگر رو همزمان داخل محیط کدنویسی خودتون داشته باشید که حتی پروژه‌ها رو ذخیره می‌کنه تا روزهای بعد بتونید ادیت رو ادامه بدید!
🔗
لینک گیت‌هاب پروژه برای نصب و راه‌اندازی
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6730" target="_blank">📅 01:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.30.8-universal.apk</div>
  <div class="tg-doc-extra">25 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6729" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخه جدید
#TheFeed
(v.0.30.8)
🔹
بهبود مدیریت لینک ها در برنامه، اگر توی یک پست ای دی یک کانال دیگه و یا لینک یک پست از یک کانال دیگه باشه، وقتی روش بزنید میتونید به اون کانال و پست منتقل بشید، توی قسمت فید باید اون کانال حتما توی اون کانفیگ وجود داشته باشه، توی قسمت میرور خودکار اون کانال به لیستتون اضافه میشه.
📯
من نسخه اندروید
universal
که مناسب همه‌ی گوشی های اندروید هست رو توی این کانال میزارم. ولی اگر نسخه‌های دیگه رو میخواید باید از گیتهاب و یا کانال زیر دانلود کنید (
ویندوز
،
مک
،
لینوکس
،
بی‌اس‌دی
، اندروید‌های
قدیم
و
جدید
،
ترموکس
، و حتی
نسخه ipa
آیفون) و لینک دانلود نسخه آیفون از تست‌فلایت توی کانال پین شده، البته هنوز آپدیت نشده.
📢
کانال اصلی دفید:
@networkti
📦
کانال فایل‌های باینری/نصبی دفید:
@thefeedfile
⚙
کانال کانفیگ‌های دفید:
@thefeedconfig
🔗
گیتهاب پروژه:
https://github.com/sartoopjj/thefeed</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6729" target="_blank">📅 00:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚀
معرفی CdnScanner؛ جامع‌ترین و قدرتمندترین اسکنر IP و CDN
🚀
✨
ویژگی‌های برجسته:
* پشتیبانی کامل از ۱۷ سرویس‌دهنده (CDN): شامل Cloudflare (و WARP/Workers)، AWS CloudFront، Google Cloud، Azure، ArvanCloud، Fastly، Vercel، Akamai، Gcore و...
💪
تست فوق‌دقیق بر اساس کانفیگ شما: در این ابزار IPها فقط زمانی تأیید می‌شوند که با کانفیگ V2Ray واقعی شما (شامل SNI، Host و Path) پاسخگو باشند (پشتیبانی از TCP connect + TLS Handshake + HTTP HEAD).
🫆 اسکنر اختصاصی HTTP: امکان وارد کردن مستقیم IP، دامنه یا رنج CIDR (مانند
1.1.1.0/24
) با قابلیت بازگشایی و اسکن خودکار کل رنج.
* تولید خودکار خروجی V2Ray: ساخت بی‌درنگ لینک‌های VLESS ،VMess و Trojan از IPهای سالم با قابلیت کپی و دانلود یک‌کلیکه!
* پینگ واقعی (ICMP): عملکرد دقیق روی Windows ،Linux و macOS (همراه با سیستم جایگزین TCP در صورت مسدود بودن پینگ).
* اسکن کامل و بدون نقص: بررسی جزء‌به‌جزء تمامی IPهای یک رنج مشخص، به جای اکتفا به نمونه‌های تصادفی.
* رابط کاربری مدرن و فارسی (RTL): داشبورد حرفه‌ای و چشم‌نواز همراه با نوار پیشرفت (Progress bar)، کارت‌های آماری، پیام‌های Toast و طراحی کاملاً راست‌چین.
📥
دریافت و نصب:
همین الان می‌توانید این ابزار قدرتمند و متن‌باز را از گیت‌هاب دریافت کنید. (اگر ابزار برایتان کاربردی بود، دادن ستاره
⭐️
به پروژه در گیت‌هاب فراموش نشود!)
🔗
لینک پروژه در گیت‌هاب:
https://github.com/ScannerVpn/CdnScanner
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6728" target="_blank">📅 21:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6727" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.
اینطوریه که ازت آی‌پی و پس رو میگیره
بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ...
خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌
دیگه نیاز نیست دستور های ترمینال رو بدونی یا حفظ کنی. تو فق به زبان فارسی بش میگی انجام میده</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6726" target="_blank">📅 18:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">https://x.com/ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/6723" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دیده‌بان لیکفا منتشر شد
🆕
افزونه‌ای برای مرورگر کروم که هنگام بازدید از وب‌سایت‌ها، اگر آن سایت سابقه نشت اطلاعات داشته باشد، به‌صورت خودکار به شما هشدار می‌دهد. متن‌باز، رایگان، کاملا محلی و بدون ارسال اطلاعات به سرور
👍
Download
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6722" target="_blank">📅 13:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWxxoN9U72I2QDmobTn57VNHeU92gK0DQN8GfW564zJIgkn_FVseRVmiwzZT7yQwsEmmkNac6L-ph2vlrkaJoc5_0qflny2wMGqeBTYZ4qHa-2B_m1ztY_I41RsjJ236YdrBogW5ioCmynRbOPRQUc8M64WGPd_io3UT-uDGWK2xRxvSdnAPzM6611Ywzic6SO-ixNIP0Ng0BMwhsH0Y_3mA7fddzkC8vsrl4HEidvg8oVbfCOx0eOsltFX70gSCfDUDjG-3Iwg2YHtXOpqWPaCUXUoJUuU3I_FF9kOcttjfLUDWVzgXi9snOirLtSarls_934uOJ3c6p-T-nJ2sSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
سیستم‌عامل شخصی، مستقیم توی مرورگر!
‏یک پلتفرم متن‌باز و سبک که می‌تونی روی سیستم خودت بالا بیاریش (‌Self-host)⁩ و همه‌چیز رو کاملاً آفلاین و امن مدیریت کنی.
‏
✨
چرا جذابه؟
🔒
امنیت مطلق:
داده‌ها فقط روی هارد خودت ذخیره میشن.
‏
🛠
ابزارهای کاربردی:
ویرایشگر متن، ضبط صدا و پلیر داخلی در یک تب.
‏
🚀
فوق‌العاده سبک:
بدون نیاز به سخت‌افزار قوی، فقط با یک کلیک.
‏
⚡️
راه‌اندازی:
دریافت سورس از گیت‌هاب و اجرا با داکر.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6721" target="_blank">📅 12:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🐦‍🔥
اسکنر قدرتمند سیمرغ (SIMORGH Scanner v0.3.0) منتشر شد!
🚀
اگر برای کانفیگ‌های VLESS خودتون دنبال پیدا کردن IP تمیز کلودفلر هستید، اسکنر سیمرغ یکی از بهترین ابزارهاست. به تازگی نسخه 0.3.0 اون با یه رابط کاربری وب بسیار جذاب (نئونی-رترو) منتشر شده.
🔥
ویژگی‌های خفن این نسخه:
💻
پشتیبانی از ویندوز و اندروید:
نسخه ویندوز به صورت Standalone هست و بدون نیاز به اینترنت اولیه یا نصب پایتون، به راحتی با یک کلیک اجرا میشه. نسخه اندروید (APK) هم با بک‌اند بومی Go نوشته شده و کاملاً برای صفحه نمایش موبایل بهینه‌سازی شده.
🎯
تست همه‌جانبه:
می‌تونید تک IP، رنج‌های CIDR و لیست‌های ISP رو اسکن کنید. این ابزار دارای دسته‌بندی لیست‌های آماده ISP ایران و بین‌الملل هست و حتی می‌تونید لیست اختصاصی خودتون رو به صورت فایل txt وارد کنید.
⚡️
امکانات دقیق اسکن:
دارای قابلیت‌های نمایش پینگ (Latency)، بررسی مجدد (Re-check) و تست سرعت (Speed test) به صورت مجزا هست.
📁
خروجی حرفه‌ای:
در نهایت آی‌پی‌ها و کانفیگ‌های تمیز رو رتبه‌بندی می‌کنه و خروجی‌های مرتبی مثل best_configs.txt و clean_ips.txt بهتون تحویل میده.
🔗
لینک گیت‌هاب پروژه برای دانلود نسخه‌ها
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6720" target="_blank">📅 11:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=kcxRt_yvSbdI80dazu0Qgpo4_WKsLvOEJSAhxEG_pM3GZUflsD_jBcF4muPQvqSVPtFodxC3U9OIVVBRwZZjfebTTf6hbRhHbi852QEoogmGDHuZh3i_G83OGWy6oM4D73ygs27kF9smPeRN_i43BqzyBjKLKxPk9AmnxFx2vT_AEFzWQl40RPiZU5zEBfKmxSrt3ACZBakoNcykwxDOjnE3Jp4ry5ADe31ehPoSLIxjKPX44JqZGCNodGDYaaNqHxSbO3ESZI7oxVS17qXBTIBYk0A-aOa1f4aJ9Vn6ThLuV9WE-vGg_gCqADRRL5aTNbiED6TvGAO69zSyUtQqLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=kcxRt_yvSbdI80dazu0Qgpo4_WKsLvOEJSAhxEG_pM3GZUflsD_jBcF4muPQvqSVPtFodxC3U9OIVVBRwZZjfebTTf6hbRhHbi852QEoogmGDHuZh3i_G83OGWy6oM4D73ygs27kF9smPeRN_i43BqzyBjKLKxPk9AmnxFx2vT_AEFzWQl40RPiZU5zEBfKmxSrt3ACZBakoNcykwxDOjnE3Jp4ry5ADe31ehPoSLIxjKPX44JqZGCNodGDYaaNqHxSbO3ESZI7oxVS17qXBTIBYk0A-aOa1f4aJ9Vn6ThLuV9WE-vGg_gCqADRRL5aTNbiED6TvGAO69zSyUtQqLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
‌GitFut⁩:
رتبه‌بندی پروفایل ‌GitHub⁩ مثل بازیکنان فیفا!
⚡
‏هر توسعه‌دهنده‌ای تو دنیای کد یه ستاره‌ست!
🌟
‏این ابزار
رتبه ۰ تا ۹۹
رو بر اساس:
‏
🔹
تعداد
‌commit⁩ها
‏
🔹
ستاره‌های ریپو
‏
🔹
دنبال‌کنندگان
‏
🔹
زبان‌های برنامه‌نویسی
‏بهت میده!
‏
ببین به کدوم بازیکن فوتبال شباهت داری!
⚽
💻
‏
👉
امتحان کن
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6719" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWGQ4npnEeBBdYs8HbOzsXqWDUQbnq64wo6ou-XteXS9bkBne2uBfg4yU5zV0ItyPCZvxTwGpe3wBAgfgppR-MWXQZ952uyC86-FS6-H7o9R9o-ZIktr9Fa26kXxjeRSoXcFJkDUw17p5PWl_mAyo6uaKL9rnEJ28RQ15aHGynNE8W12Yjg1A138GrnKBrhv8XnpvhXNyhw2M276knW7ByreT45ng7wep-nclVWqIuEms5quwjtu44S4U1bcst2bwM2RfglQ_C-fVaFIXoQ2PxV5yfYruiZqzNEx4a-tN8pFdf7-MPsAlN4mG4RWdLZyJaRtPC_FPLpyO4SW7pJxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
‌scrcpy⁩
— کنترل کامل گوشی اندرویدی روی کامپیوتر!
📱
➡️
💻
‏
✅
بدون دردسر
: نیازی به روت یا نصب اپ روی گوشی نیست! فقط با ‌USB⁩ یا وایفای وصلش کن.
‏
⚡
سرعت بالا
: ۱۰۸۰‌p⁩+ با ۳۰ تا ۱۲۰ فریم بر ثانیه.
‏
🔊
صدا
: انتقال مستقیم صدا (اندروید ۱۱+).
‏
⌨️
کنترل کامل
: موس و کیبورد فیزیکی شبیه‌سازی میشه.
‏
🎥
ضبط صفحه
+ نمایشگر مجازی.
‏
🐧
سازگار
: ویندوز، مک، لینوکس (بدون نیاز به ‌snap)⁩.
‏
🔗
مخزن
:
‌GitHub⁩
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6717" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
🚀
‌Arvix AI⁩ = جعبه‌ابزار کامل هوش مصنوعی تو
‏
🧠
متن:
‌GPT⁩, ‌Claude⁩, ‌Gemini⁩, ‌Grok⁩
‏
🎨
تصویر:
‌Midjourney⁩, ‌FLUX⁩, ‌Nano Banana⁩
‏
🎬
ویدیو:
‌Kling⁩, ‌Veo⁩, ‌Seedance 2⁩
‏
🎧
صدا:
‌Suno⁩, ‌ElevenLabs⁩
‏
🎁
توکن رایگان + دسترسی به همه مدل‌ها
https://arvixai.net/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6716" target="_blank">📅 10:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏
🚀
آموزش دریافت ‌API⁩ رایگان ‌Nvidia⁩
🚀
‏‌
1⃣
ثبت‌نام اولیه:
‏وارد سایت
‌build.nvidia.com⁩
شو و یک حساب کاربری بساز
📧
2⃣
‏‌
شروع تایید هویت:
‏پس از ثبت‌نام، روی کادر زرد رنگ بالای صفحه کلیک کن تا پروسه وریفای آغاز شود.
⚠️
3⃣
‏‌
دریافت شماره مجازی:
‏به سایت
‌2nd-no.com⁩
برو و یک شماره مجازی موقت و رایگان دریافت کن.
📱
4⃣
‏‌
فعال‌سازی حساب:
‏شماره دریافتی را در سایت انویدیا وارد کرده و کد تایید را ثبت کن.
✅
5⃣
‏‌
ساخت کلید دسترسی:
‏به بخش ‌
API keys
⁩
برو و کلید اختصاصی خودت را بساز.
🔑
6⃣
‏‌
انتخاب مدل‌های رایگان:
‏به بخش
‌
Model⁩
برو و از گزینه‌های
‌Free Endpoint⁩
استفاده کن.
🤖
‏
🌟
برخی از بهترین مدل‌های در دسترس:
🔹
‌GLM 5.2⁩
🔹
‌Minimax M3⁩
🔹
‌Deepseek v4 pro⁩
🔹
‌Kimi k2.6⁩
🔹
‌Qwen 3.5⁩
‏
بدون محدودیت توکن
🔓
بدون لیمیت روزانه
‏
♾
40
درخواست در دقیقه
‏
⏱
🔵
@ArhiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6715" target="_blank">📅 03:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=BPyGS8ATvWNwLmYzQWpTIF2RO5bXlFDYJPvZYGsfasEu2FhWFO5kzovmBXbLhRtvNsaDooVY8_40BDlS1b_-omwBZOv1iYJVvNah_UVC4-1OwqY8wPB6GEZFy_6hZJ2OlbRtx9pfo_06uF3eTsMXVsARywGrposcdonYR_a0Gp1OCmnlwl-oKeZIcZ0dV1hP5Ue9MCveKfitiTTYhINZWEOqFAAgKDDCB23f6A7zj6Ces-6yuGb77kjBdc9_76u1zTdSav6wDlTCqb_RBcOZVNjFpNgh7FHkaPXAMXwbq5YTwtKZSH01lI6yKYrij-QOAXe5f6_Ae4bn3-UHkub1y3KNW8sxsg-xVLGlJE455TJXgZgNpgQChRauOEsnGAZEdx9HTf7ywaVMNPMTk_bR9MDBdVVswJ3bX7Cmbtg4olcJsKOcr5JGPnGutO1uO0_jYtagyhxOeh9gH3AcobYEj-OpwEQJiMMott_ZNdv7l8psgw8AsQ0w0dqFRhVDRuoqCSnChvH34B6ThbsSRtKhd5S57gyQlUboazf8E3tY_p2zzQx_T2nsti1-oRtlzwNueKcDvB3KLbXjbF-_l5qlTfMh9_Af4-WFGnLzn6L0XSBI4pLIasliJ2pMFQ3uDLgzIbJ9pCVcjAqwMj6RCjn9jWkbgySOmItw6blO6icLj_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=BPyGS8ATvWNwLmYzQWpTIF2RO5bXlFDYJPvZYGsfasEu2FhWFO5kzovmBXbLhRtvNsaDooVY8_40BDlS1b_-omwBZOv1iYJVvNah_UVC4-1OwqY8wPB6GEZFy_6hZJ2OlbRtx9pfo_06uF3eTsMXVsARywGrposcdonYR_a0Gp1OCmnlwl-oKeZIcZ0dV1hP5Ue9MCveKfitiTTYhINZWEOqFAAgKDDCB23f6A7zj6Ces-6yuGb77kjBdc9_76u1zTdSav6wDlTCqb_RBcOZVNjFpNgh7FHkaPXAMXwbq5YTwtKZSH01lI6yKYrij-QOAXe5f6_Ae4bn3-UHkub1y3KNW8sxsg-xVLGlJE455TJXgZgNpgQChRauOEsnGAZEdx9HTf7ywaVMNPMTk_bR9MDBdVVswJ3bX7Cmbtg4olcJsKOcr5JGPnGutO1uO0_jYtagyhxOeh9gH3AcobYEj-OpwEQJiMMott_ZNdv7l8psgw8AsQ0w0dqFRhVDRuoqCSnChvH34B6ThbsSRtKhd5S57gyQlUboazf8E3tY_p2zzQx_T2nsti1-oRtlzwNueKcDvB3KLbXjbF-_l5qlTfMh9_Af4-WFGnLzn6L0XSBI4pLIasliJ2pMFQ3uDLgzIbJ9pCVcjAqwMj6RCjn9jWkbgySOmItw6blO6icLj_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تبدیل ویس به متن تلگرام کاملاً رایگان! (بدون نیاز به پریمیوم) با هوش مصنوعی Cloudflare
https://youtu.be/Xq7e2k3qlqA</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6714" target="_blank">📅 02:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوستان وقت بخیر و خسته نباشید
این چنل زاپاس آرشیوتل هستش
داشته باشین بهتره
❤️‍🔥
ی موقع اگ چیزی شد...
https://t.me/FOSSArchive</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6713" target="_blank">📅 22:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=FYBXtnpArAjdgeIjLmRhpEPSwI8aynNAe50eEYr-m8qRWJAULaD0XgVOFC8I8sUIiRsbKQx7o7yRFWbM0HvxlrG63pcgQ9rOUt9Uq_0EimlBZmkgMHYPHifLC0Ewc2qT1nywmWkZgKMp4Ecj5gT8DtyQV7QJf_TKFdMs636WNi8Ez2q1YudCLeBYQd6SIJH0veSJ0ru-KOgkKeQ0oXnUVQqPAPl6V_9hwgVkHJoPrwULYI8t424yTtXucrO6yIBYkQWi5HPpPGQfUVkGzJvNKry4jVtpylty61QaH-U3H-w83g0RYnNMuf_7_l6cGuzY9BKphrrAtKMwC2Lf45Kf-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=FYBXtnpArAjdgeIjLmRhpEPSwI8aynNAe50eEYr-m8qRWJAULaD0XgVOFC8I8sUIiRsbKQx7o7yRFWbM0HvxlrG63pcgQ9rOUt9Uq_0EimlBZmkgMHYPHifLC0Ewc2qT1nywmWkZgKMp4Ecj5gT8DtyQV7QJf_TKFdMs636WNi8Ez2q1YudCLeBYQd6SIJH0veSJ0ru-KOgkKeQ0oXnUVQqPAPl6V_9hwgVkHJoPrwULYI8t424yTtXucrO6yIBYkQWi5HPpPGQfUVkGzJvNKry4jVtpylty61QaH-U3H-w83g0RYnNMuf_7_l6cGuzY9BKphrrAtKMwC2Lf45Kf-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
ImageGlass
ابزار سبک و سریع برای مشاهده عکس ها در ویندوز با پشتیبانی از طیف گسترده ای از فرمت های فایل.
• پشتیبانی از بیش از 90 فرمت: WEBP, GIF, SVG, AVIF, JXL, HEIC
• رابط کاربری بصری با سرعت پردازش بالا
• مناسب برای کاربران عادی و طراحان
https://github.com/d2phap/ImageGlass
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/6712" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423195fff7.mp4?token=MCqdqtrq34ydOOgzZiy3zFz3SeE6wXhZb6BIKOfXxroQ8UMdtIVMaK64hitLFbNLnO65JPUKatl0xu13JtP6r4VcMEje9PsFE9NXldJa0N7CRo4u0TLJuiWBzfiYI-41eYz7lxV76e8zOUHI92EDMGkdix90maWnrGT7wVrPS5YrvaRVZtivdOqVOssfOyP8JnywEW1YWepUtPZSKJdQzV94NoD6xbDCflgRmUdV37vXyRwH7KUgZTtHFdISl5yNiAAr_hb2nUTB_gcz0j6ltqaYuZIQZ2YTCs41AiuFVPmU3lI8mPNo_zDxNBUc1nn_m2uXiW7W4PyMhxoNOyLcAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423195fff7.mp4?token=MCqdqtrq34ydOOgzZiy3zFz3SeE6wXhZb6BIKOfXxroQ8UMdtIVMaK64hitLFbNLnO65JPUKatl0xu13JtP6r4VcMEje9PsFE9NXldJa0N7CRo4u0TLJuiWBzfiYI-41eYz7lxV76e8zOUHI92EDMGkdix90maWnrGT7wVrPS5YrvaRVZtivdOqVOssfOyP8JnywEW1YWepUtPZSKJdQzV94NoD6xbDCflgRmUdV37vXyRwH7KUgZTtHFdISl5yNiAAr_hb2nUTB_gcz0j6ltqaYuZIQZ2YTCs41AiuFVPmU3lI8mPNo_zDxNBUc1nn_m2uXiW7W4PyMhxoNOyLcAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏کتابخانه‌ی معروف ‌Pad Shaders⁩ (منبع غنی گرادیان‌ها، پس‌زمینه‌ها و شیدرهای خفن) رایگان و متن‌باز شد!
🎨
✨
‏دیگه نگران لایسنس نباش؛ می‌تونی تمام پلاگین‌ها و ابزارهاش رو تو پروژه‌های شخصی و تجاری استفاده کنی.
https://shaders.paper.design/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6711" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6710">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
دسترسی به قدرت هوش مصنوعی در سرور شخصی؛ آموزش API کلودفلر (Workers AI)
☁️
🤖
اگر برای پروژه‌هایتان به یک هوش مصنوعی قدرتمند (مثل Llama 3 یا Mistral) نیاز دارید، سرویس
Workers AI
کلودفلر یکی از بهترین و بهینه‌ترین گزینه‌هاست. برای استفاده از این سرویس، باید یک API Token اختصاصی بسازید.
🔥
مراحل دریافت API Token در کلودفلر:
1️⃣
ورود به بخش API:
وارد پنل شوید، روی آیکون پروفایل کلیک کرده و به مسیر
My Profile > API Tokens
بروید.
2️⃣
ساخت توکن:
روی
Create Token
کلیک کنید و سپس
Create Custom Token
را انتخاب کنید.
3️⃣
تنظیم مجوزها (بسیار مهم):
در بخش
Permissions
، گزینه
Account
را انتخاب کنید و دسترسی
Workers AI
را روی حالت
Edit
قرار دهید.
در بخش
Resources
، اکانت خود را انتخاب کنید تا دسترسی‌ها محدود به همان اکانت باشد.
4️⃣
نهایی‌سازی:
روی
Continue to summary
و سپس
Create Token
کلیک کنید.
⚠️
توجه:
کد نمایش داده شده را بلافاصله کپی و در جای امن ذخیره کنید؛ این کد دیگر نمایش داده نخواهد شد!
💡
نحوه استفاده:
شما علاوه بر توکن، به
Account ID
نیاز دارید که در صفحه اصلی
Workers & Pages
پنل کلودفلر قابل مشاهده است.
آدرس فراخوانی (Endpoint) شما به این صورت خواهد بود:
[https://api.cloudflare.com/client/v4/accounts/](https://api.cloudflare.com/client/v4/accounts/){ACCOUNT_ID}/ai/run/{MODEL_NAME}
✅
حالا می‌توانید با استفاده از این توکن، مدل‌های هوش مصنوعی کلودفلر را در کدهای خود (پایتون، Node.js و...) فراخوانی کنید.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/6710" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhyBUkNaUjbpDDLlAA7pka0P66bTFJYzfCXbbvNN9S0zI1n-4levuftf7eyduRkVTiSb2Jl9mOkiAqxjzsr8dKq-BBZGXi_eIeHJrn2TJsFCg70eXxBAp8rO11TJF4pZs-HuRV8sGEAlWS37Ej4wL9QHZHy9Dx9Vof4djMMY_1IHLMvH3alVtN19NdE8r4KIuoGi2EogrKVNl2moqXWhjsw73pKyCDZo6Vvd62b9WtTNRAv2DFVaMr_6i9qc286zZOQuyzzKZ44r8NSaFj3HVOw7Ms-eW6In_MY10KJMVLCpQxU7ntLTMHTSJwJwTe4jGzjE3PwN_rfkrraogsd4Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5
هوش مصنوعی رایگان و قدرتمند شرکت انتروپیک
10 دلار کردیت
با لینک زیر 20 دلار
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6709" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سایفون رو اپدیت کنین خوشگل شده
🔥
(نسخه بتا)</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/6708" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=tcmS3Ruo3JFp8DCoKI8OJZ_ZtZu_gSrdVuB4IyN4PA4pJIPUV00Pd7QYEwFmqPcU8Tm7aff6eR6pBq3PImK0yUY7FO-eslIl-MjOKB8LjiPn4bcg6dfr1A9_IfW-3Op1y3iNk2bwb5vRa8gcgt13_cYOFpFpjoiqSUgiNuuxA6c6LIa3hEXJt4ZrPGuGTk-squYEAgpaWvRRdvtI9zxfNnxo4ToRQ2V7Hf2p-Wvu8uJ92wcxWFwrCCpgj_oHiUfKHeBdfvZW8meFzSpSOP04ER6OtF8HdNs1E22TatbRCA1eNU1xy_i5FScikSLfBGzk3w3VzVNQ9GuTyG8GOjThjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=tcmS3Ruo3JFp8DCoKI8OJZ_ZtZu_gSrdVuB4IyN4PA4pJIPUV00Pd7QYEwFmqPcU8Tm7aff6eR6pBq3PImK0yUY7FO-eslIl-MjOKB8LjiPn4bcg6dfr1A9_IfW-3Op1y3iNk2bwb5vRa8gcgt13_cYOFpFpjoiqSUgiNuuxA6c6LIa3hEXJt4ZrPGuGTk-squYEAgpaWvRRdvtI9zxfNnxo4ToRQ2V7Hf2p-Wvu8uJ92wcxWFwrCCpgj_oHiUfKHeBdfvZW8meFzSpSOP04ER6OtF8HdNs1E22TatbRCA1eNU1xy_i5FScikSLfBGzk3w3VzVNQ9GuTyG8GOjThjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت 10 تا ایمیل رایگان با ساختن یک ایمیل اتومیک (مولتی اکانت)
https://www.youtube.com/watch?v=XHJ3TwrwG-g</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/6707" target="_blank">📅 03:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvQ35UX5t_MTdoN8g39eaATyreFajjFG7Dza8lsG6FaunTq9475aqOPKOk9l3d_nX7HIR0Zr1nfczam-V9mDTarzYgUv4zbxv0CY8KtP3MWD3VFC-cWpz2bPfyPF9ui63SdEoNDffxHr2_yRP0fn3-H60IJahnDz7UxLXghU0YmyrzIdnTuTczGnyw6OY_M2k2k28Rl4mO4AmVIFX7NTmQOwpaW4yiK-4fqNapFXpj2GSnHgZl5XSCp8-P7gr68GjvJCdjt_GofDNLJ4cL5FQtyWj1OLD3RgATaSRtC-f0bT8qr5Mw9wPJeqPCGkWsKnA46OIf-ma386rfPx199u4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
قابلیت جدید «وگا کد» فعال شد!
💻
‏همین حالا وارد
‌Mini App⁩
ربات وگا شوید و از قدرت کدنویسی هوشمند لذت ببرید.
✨
‏
🛠
مشخصات فنی:
‏
🔹
پشتیبانی توسط مدل قدرتمند
‌GLM 5.2⁩
‏
🔹
سقف
۵ درخواست
در هر ساعت
⏳
‏
🔹
ورودی تا
۱۵ هزار توکن
📥
‏
🔹
خروجی تا
۱۶ هزار توکن
📤
‏همین الان تستش کنید!
🚀</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/6706" target="_blank">📅 02:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsuUhpq0GHcpP8ejl6U9Pe6toYGi6idzlOw2Vzqg7ruyNZCB5OLTl2p66q3EhddKV1A3VFsHBP5PMwmga-0K85Tuv1TxOqX0Edgudfw1ga67_92sOeNEcYgVAF3u-7TFX3FcipIa0xTulEIBV1Ykx-HZwV0b57o9_P5AMdWYl25g6fO6I8MSyivVPgtDNGVJDYQ3VFzfFBdOIUGqpDObwEh3v7zwJXzXv88BS_9ynRlATr4EwZzYdKaBjV04xyibGlicC5G8z_4W2xF6p6SKmGDU30cBY0qLudJ6Uule0WIT0pJtrbNwpfAYmjVaFuxtJTNleowT1IL7ai8heyOKlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک میلیون توکن رایگان Gemini از طرف
گوگل؛ بدون نیاز به کارت بانکی!
🎁
✨
گوگل به تازگی یک فرصت بی‌نظیر فراهم کرده است: دریافت یک میلیون توکن کاملاً رایگان برای استفاده از جدیدترین و قدرتمندترین مدل‌های هوش مصنوعی این شرکت. برای دریافت این توکن‌ها به هیچ‌گونه کارت اعتباری یا خرید اشتراک نیازی ندارید و همه‌چیز با یک کلیک انجام می‌شود!
🔥
چگونه کلید API خود را دریافت کنیم؟
1️⃣
ابتدا وارد پلتفرم Google AI Studio شوید.
2️⃣
روی دکمه Create API key کلیک کنید.
3️⃣
تنظیمات و محدودیت‌های تولید را به دلخواه مشخص کنید؛ کلید شما آماده استفاده است!
🤖
مدل‌هایی که می‌توانید با این کلید استفاده کنید:
Gemini 2.5 Pro (قدرتمندترین و هوشمندترین نسخه)
Gemini 2.5 Flash (سریع، بهینه و همه‌کاره)
Gemini 2.5 Flash-Lite (فوق‌سبک و اقتصادی)
💡
کاربرد: این حجم عظیم از توکن‌ها برای ماه‌ها کار فشرده، از جمله کدنویسی، پردازش و تولید متن، تحلیل داده‌ها و حل مسائل پیچیده کاملاً کافی است.
🔗
لینک دریافت کلید API
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/6704" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnRFi06MIuA9-jHHV-2wB3c9458xpoeIYioETu4btE-HnWjW84-LEk48fXRy96uYaJYOx877ZuJxpcwi9G0SiO71D0zN3HJg9GpT8EwpjX8fNTvGOVAZ7-ViHbgiTLu5Qwstwhu8LQ-DF5O87pn_oQRhOv5tL3K9BuDGd-xsl0Xod5vwyzuPflOQpQt7dVoc6v_SkmwMv1PCm3ihdYpO2PEi77Mkg5QXdWAYsQjgyUGGaMpDLZj9QUy7Zqu8WYKjsA5uH8yQ11W23jxpBKOxlzcpue2mAqLtVYp9qcVl3InCN_gCUEXpYjfUIoZ4nGbFDa0bYeJTj0irQ2d_mDIP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفسیر خطاهای ویندوز با ابزار داخلی
راهنما:
— کد مورد نظر را کپی کنید، مثلاً 0x80070422.
— ترمینال را باز کنید (با فشردن Win+R و وارد کردن CMD).
— دستور
certutil -error 0x80070422
را وارد کنید.
— توضیحات دقیقی از مشکل را دریافت کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/6703" target="_blank">📅 22:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJK4g6gW8QZdgdyg1VKEykveLVHycUIkWwDmj7tNKVHznVVf819Q21TcJZsoU_U_B03tr58XQFgWkF8ppojFeQjTRxmL15q9VP7VqEZYT-iCe4wZ0F2x5-arNryIkWxr5zomJ2l0G7llWMVPXPEHjW3iSz_teqMCCrw4gLcrc2raHcWMfRDPTI8am7wt8Jw6dW-ubpMvIdH1Q28RzmoQJhdeFWtJL5vimMW5sjtxUe4pMmZoprOiHH8FGQp1or4EAWQYLgtB6Z9yurfTFBnCmA_QFw2URL3lphoN2poLqURV8JU0HbFOjAKNvHAMdmB4hzHNFmozOcLOCxSpFXauPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا پولاتو چیکار می کنی؟
پولام:
به زودی ۱ میلیارد*
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6702" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQ6uckiAgPavpzLhES0wUqTxO1SA8tumsdzQu26w-3UARNuiYy0vbjtuvJlhW8uoqIc_GFhcFFVcfxrgCyo8-eKdvTKW2MJwyrlXaf20mRTZlGE6mMqp0sQuB0W2tf-gKbKZYA2vlOVHpl2mEqR9E2kl70wopzrGBZGgaqHpa1sL46cIdHYwDljt09Zh3ZEcVSbF7_tkqa-IPiHBnDY2tWTuri5JFLWTCswe-bD13GIFz-cuyGp-ozxTfNPJPDuKTF5d_mtYqU_ed5Z4r83YMtfG7nleBch5mninB_H-aLMc-y10AJizgVB8W-zeShbMYytuNcMVNJWFqmHIV6gUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efvkW6peKcqLJlT09b_1MWyT4UrCfd9SLZNGp2izxVXcd3_BtlnCYmc3lg9nbr9bnKJD_7YfgNQH2PqaMOikn7rcMXAAakDQ53R83DdvCwfJr7pieOTis2nlQRmuDdv-ESZmrC80DUWxaZ6t_GaSoC7W3lzNtW2Abunr-v_8hyD59x9EG6wx7He3xR_EVd854iY9UCWvaxttxgi5TnacRafGn0-NYqGOd-DGo4bPNkaWALVPMiS1z7yhQ1H2c1z2LLgjhYAh4L1iG7O_WmTj0JCJ4XjrQ-d-5QY-05B8rcEELnIOJQVow2mbGr-LGfAyxMt-usGnFCSG5nszmjOC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZF8MmlY_qw1rojPdbEwekk33xuZF7lBR5-S8kuQcV1cdg8C4CJvquq5RzFFaO57mLBljHVzrXCwbiOw0ZW7mxuJhB5IwyIBJQpR9F6oVVwK63g8w7RQYRlk_DkY06JAY5682gy4BA2lum8P0sXS0dZfTvoKCsD99PTnrvJst7OOcEnsZv3HxqcobUXjTUB3wEX9_aRy-_iwLuHzZ8xZMzv853udU-_jy7gqcpDF_JWBZrFeh8flDfZyPdFE0Iaw_vavIlDGt0HcFKgtAW1BEHrvYmLZc7nzXSQJSJFfm4elBHGnpcdK7ILl3VcunwSlg1obilc9guL_IMRdot9-jxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWCci5GFg0vjdm-_aFEE7dkUBQM-sDVVde-LwpUVMl9OkWGAzgfjV6usLIl59BB6IMm65XssdrlwDuqQTeTEI97X_4p1q0zuOqY-EaZuTUj_K1fmjp7pGCaakADLkE4WsIELDekEX4GPiBgaqE1J_Vy4yq1hk9_wfs7y9L1STsCqjhCjYOUmLgf5I-6MXELvdfJQ1bCcu3m7H-PInYiWkMknC1D7srUZLsWyR7S_ZIjwi16_Hhl5GVOrwjo8yAvY1RgtKQNZJ0aIiBxMzmzoUe6wmFcu_rRLd6TFql1tZsrkQVT66Kgeday5ADKOrF2Nfi4J76lCA5hMAaJ2WALZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9d4QSgvrSFIBr0V6qNicwp8UAxhlru96EoLAW6oOTVMGomNQ3XfPdGl7TkbGmPS6i1756_P4pIp8yLukDig557NJzPHi-YkbBwg3PSp1aim3jmdii-tpSQsGl9Sqelo6M_Z4esexKOrYo3nAyyA2PNujOM1v7IYZ6761S5rVdwz-Tn_KP_5KvCKN8nrmmRc6EqysdWi8qzJm_k7TFtqnM0OY24kQTUrWCn80cHCnlkyrIz_dk0KhhK6nXCRQsc_h_oT5TQMBDQK8d_YbTPL9adW7YrjhUpLnJ4b3f7NfPjkDD4OPz4d-UnWVfpe_Q6ZMVTTp4ltwyxu__LKrKgSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r57OqABldjiHHUhDMMcj1kCLmxNUkJ443NhPhyFTl51qj5iIij-kr5ar3gKv_wOIcOz_NeipiuTW3zQBZU3HDydFfqw53DrK6DA6V17ecqJviYPReR-jeSJgxXq4GL0ZZuww88YXOdC5f581WRaifmZhNwCElZXTszDZionTZp5DJWgVbkU8wcUUW7yJ4slUqthZFh622bbK6buxcXjFRWTsYOx2dmFC-xaOn_tJOvLvB4fDY5PtmOeSl5RlieW2UWup6rjX0cf-lSw-yBKevt8G0j8KJQaG29gbKu1Oe0YvmMeVTEMCfgtr7YYST01nt20kwegSp-6r5qf8Eq3oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mx7-ml2GmgRPrNra-BQUvXq8W6sGMNnJHbR9lKy661rgYK10QsEup7dNGxXGj3g9cAY4wZGOFX5gwBcu3vvacTvyOG_Sl77GqIpYiDSEbSUYhwVElNg0FCsstyMRnBfpoMMmnDbNA957Z5sgk6NZyrgur3RfGo9oFxdy6gHYN3mBM-KoCfFFeRMleQuiTlcgptMQFjb5hhbUgaoWkbEXZjJG6HrWpVB85RbFf0DZbtyVKq0urXALLWbXdzHoEI2c-dSlw8B_BbalKH8Eao9QFGRdAbeyYqYpLDDZxNMxbfK7UytzddxOdSlDM_xSLshQvaPVk4IjzXDRkYn2PSHebw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتایج
جایزه عکاسی با آیفون اعلام شد.
در این مسابقه سالانه عکاسان از سراسر جهان بهترین عکس‌های خود را که با آیفون گرفته اند، ارسال می‌کنند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/6695" target="_blank">📅 17:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBUFhwkcenPjKNGwwD8qePp3tifM12XxEKZdUHQUadafaacyiVFdUG1HPZ4H1pQKjRtz9egIui_56yZxDeyBSl_go1y1HdkBqWHFZ31RhhqpTWn9_q_G0SMwunW2OCfIaBAl6Z9CzOdS8pOw-CmF07rkaHqErU40Bqs-0iJOTZRpRq3j0KIv5Y-mDDEkpxBJUSUeK3oxXtmgugrsPJk_kGrbSZS2_zMV_4L4V69uH7WrE1rmrgt3fOJT3e3HMKCBjqS22An-sRBN8a96_yoDDJJ15-g0eUZdcJ4sg12dYDtDzWosaMsYQRi_zPaCdkPWDIBIIl3-qt988eG2WhD3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AITwitter Generator
یک افزونه برای تولید توییت است.
این افزونه که بر اساس فناوری پیشرفته هوش مصنوعی ساخته شده، خلاقیت و سرگرمی بی‌حد و حصر را به حساب کاربری توییتر شما اضافه میکند.
https://tweethunter.io/generate-tweets
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6694" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4-aySkae01AI5jXIJakxGIJl_9j8cGlKW5C3NURIUPg-RiFmuVfFSYfHlp9RU0TG0XF4CCO-X0R_QZKvkdJEOxZPejV37MujM63STGsCzkTA573GZr8z-5IVHUH0TURdpQmSjcxly169u7tr5S76hwDeuCogrFQt4MTmqPtEEHWcZp9JLqg_NtIPwZqWVfJfxfROdaSEHdz7Ne0A_QOOD-KMIvJh4AKzSSTyfrlmPMKrnruBbWnsWx7f4ypeAWaOFZpN3upc0xEuk181MCaj16qfr9Wz7LL9FRAM_eCPp3hV-8UIMtWRNecbh-jtmu98QiACurTFWEh87WYyKpiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک مجموعه‌ای رایگان از پرامپت ها برای Claude ارائه می‌دهد
🤩
این مجموعه شامل ده‌ها راهکار آماده برای بررسی امنیت، رفع اشکال و بازبینی کد، خودکارسازی وظایف و موارد دیگر است. برای هر پرامپت، توضیحات مربوط به نحوه عملکرد آن ارائه شده است.
https://code.claude.com/docs/en/prompt-library
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6693" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
