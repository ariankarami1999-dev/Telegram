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
<img src="https://cdn4.telesco.pe/file/ZGBKFVW4FEeo4Sc61XJUmPnBoWDQR7dBqQLcIAKs8FRrgWsG1N-keflM5NhU0BoO8HubiGaIPy13LrWlwQf1t16F0tJcAdqWmtofvlVrrSAxVOWROONDYoOU5R50Ep07TXvJmWDu_NYERr9uyaDpfUMyIEgzCa2xU73ig4rVKa3hL9Ht5DnT0BmwKxvZbxDLvOlU2tyC9guFgPQB-QwMRfM3gZR51wL-hdtb8Nt_ef50qWVu_g4enbTN1f56lyNcnvRed4_lVLKV63hn3ped80jJ97KplEverRffUG0SpNan28ChqE9D8wc8RYdp1ARSbLoGCzjJHlv0Yn68sRVMPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 11:04:18</div>
<hr>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3KLq3kQqoqEDKRPUjKS5XIrrs51SLI8EEXGj_BNMOnE87hAln97-fBQb1C_VeXL2IV_rttHyb19ZXsCa4XLvIllB7oFP-N60ay-bxWeQOYgVX54rBMjF_gUIxClawmYo0JeYYSTt1Ytfn0J_ucfqMERbGgWYYQM7D6ysJ7VJ40Hx3YWUvd6u8dJ2uLmU5ns2AjkDf47dsqJM7juef2ctKC17Ko212lueJsKcJwnpaGJ2L0fOdMy60YQwPMo0xDCn3QYJo86XQLlNSbQz2SDUjhMtHkyr4G1NXPcfw6jeWRbMEjnM6cRduCkjMf7VPm3XqQ4CrxgUucfCoUfvzg_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)
همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟
پروژه «روح‌گرام» یک یوزربات فوق‌پیشرفته و اوپن‌سورس با اتصال به Google Gemini هست که مستقیماً روی اکانت تلگرام شخصی شما سوار میشه و رفتارهای یک انسان واقعی رو شبیه‌سازی می‌کنه!
🔥
قابلیت‌های خفن روح‌گرام:
⭐
کدهای رمزی و نامحسوس (Stealth):
با کدهای ۳ رقمی مثل 777 یا 666 کنترل میشه و دستورات بلافاصله بعد از ارسال پاک میشن تا هیچ‌کس نفهمه!
⚡
شبیه‌ساز واقعی تایپ و خوانش:
🌹
قبل از جواب دادن، اول به اندازه طول پیام «مکث خواندن» می‌کنه، بعد علامت ...typing رو فعال می‌کنه و با سرعت دست انسان تایپ می‌کنه!
🎭
تغییر آنی شخصیت
🎲
با یه دستور ساده لحنش رو عوض کنید.
دریافت و استفاده از پروژه از گیت هاب:
https://github.com/faithsaly5-stack/GhostGram
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 473 · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=SIGbk_QYLJNSuOX6C78ZjML_aBlaWN4IF3IXLh_OJH437QTUKc8GOgEx6p7GF8Xskd2qaLEBfzEcU-wCxRwnODt5YgkP4NQr7thTidoL7NBByYVgdD7ovo26Fvp-4ycpSLaZWWC8VKybGs7p1Av1pFa9Crr_Td9aW_NJ0kT_4FaWZsEl3yo6oz-o0vAK1zHyOjxwfnXITp_qEa6RCVjL-selQq1l6IfFySTBamGgTvnixNn9a6Cs0YmH2_r22uCr9-URXDjoeeShSp_om-y3gX7r5iQZpKQhXH-4Bi7O-YS9Z5x6ErFPLYOo-p5h3KiCanj1L7cyXgmVadVpAccPhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=SIGbk_QYLJNSuOX6C78ZjML_aBlaWN4IF3IXLh_OJH437QTUKc8GOgEx6p7GF8Xskd2qaLEBfzEcU-wCxRwnODt5YgkP4NQr7thTidoL7NBByYVgdD7ovo26Fvp-4ycpSLaZWWC8VKybGs7p1Av1pFa9Crr_Td9aW_NJ0kT_4FaWZsEl3yo6oz-o0vAK1zHyOjxwfnXITp_qEa6RCVjL-selQq1l6IfFySTBamGgTvnixNn9a6Cs0YmH2_r22uCr9-URXDjoeeShSp_om-y3gX7r5iQZpKQhXH-4Bi7O-YS9Z5x6ErFPLYOo-p5h3KiCanj1L7cyXgmVadVpAccPhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
مدل‌های غول‌پیکر روی سیستم گیمینگ خودت!
محققان دانشگاه‌های UC Berkeley و MIT سورس‌کد سیستمی به نام FreeToken رو منتشر کردن که مدل‌های بزرگ MoE رو بدون کوانتیزاسیون شدید، روی سخت‌افزار معمولی اجرا می‌کنه. سیستم به‌صورت هوشمند محاسبات رو بین GPU، CPU و RAM توزیع می‌کنه.
💻
📊
نتایج کلیدی:
🔺
مدل Qwen3.6 35B روی لپ‌تاپ با RTX 4060 8GB تا ۳۹ توکن بر ثانیه
🔺
مدل DeepSeek-V4-Flash 284B روی RTX 5090: ۲۲ تا ۲۵ توکن بر ثانیه
🔺
حتی مدل ۷۵۳ میلیاردی GLM-5.2 روی یک GPU ورک‌استیشن قابل اجراست
✨
ویژگی‌های دیگه:
🔺
پشتیبانی از ۲۰+ مدل باز MoE با فرمت‌های مختلف کوانتیزاسیون
🔺
یک API سازگار با Anthropic/OpenAI برای اتصال به Claude Code، Codex و ابزارهای مشابه
🔺
نصب یک‌کلیکی با GUI برای ویندوز و لینوکس، بدون نیاز به تبدیل GGUF
🔺
متن‌باز و رایگان با لایسنس Apache 2.0
🔗
لینک مخزن گیتهاب
🔗
لینک وب‌سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=clnqALg8gSvKjLEKXpeue4rd74B54Tw1BkDpkFAqMqroRL3r2hNGu5WhgkwGmGcAoPjxLcAbg4LPEUrYo_04T6yBFT5c7qjDtV4UnaE9WdWYzlYSq8ExQM5Zq5Ct4jg_WYcbAewOfMTLUBTvHBPBOJPFSaNBjZOguNipz18b5g5b0XjRVrAF9W7EXDkmmToxMbCT2giHJJtRsAniXxAtvhEwUqUH6FyOrjOf4BwTdUtGabQiiL39B7KurDgya3XJtvuKbXWZs6ojS6MvJkAEKI4HscTQw8z2o30nFmceH3-zmEfMtAPapAQSfek3Q9sz2ILaxdPdkNKB9ARGFlIa5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=clnqALg8gSvKjLEKXpeue4rd74B54Tw1BkDpkFAqMqroRL3r2hNGu5WhgkwGmGcAoPjxLcAbg4LPEUrYo_04T6yBFT5c7qjDtV4UnaE9WdWYzlYSq8ExQM5Zq5Ct4jg_WYcbAewOfMTLUBTvHBPBOJPFSaNBjZOguNipz18b5g5b0XjRVrAF9W7EXDkmmToxMbCT2giHJJtRsAniXxAtvhEwUqUH6FyOrjOf4BwTdUtGabQiiL39B7KurDgya3XJtvuKbXWZs6ojS6MvJkAEKI4HscTQw8z2o30nFmceH3-zmEfMtAPapAQSfek3Q9sz2ILaxdPdkNKB9ARGFlIa5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW_pzevPhojI3GOqrdI5zT0kZdKZltJ3r9Zsis5vyPtJUIRPPCR_vZVZ3xWZLlb-nh3KCoIyfcUV8qHsdIular3Ujoln9BdPySoH4GohNioAXw5sYzzYbNCf-BsUNVfsD7Oyk70-cibDe7Fwue2GFi7RQLKhhMWJS7kuw0Ru3F1qfyVvDT8fWgM5uxfgts78tj-GSP_ydcsCnsZ7emvsqTwZKNtXkaKwPIT5iQ0KMquzQ5KuEFegRgZxeL3Q3Yu-ovyWO0G4AKVuRTD6BZ8byWDptiSoxUv47qPDkpQhsQuwfFVjgk4Cb_y7smKyKjky6Hv2l92MjLcvLuGxkQ9YRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔬
دانشمند هوش مصنوعی که خودش مقاله می‌نویسه
یک پوشه از داده خام رو بهش می‌دی، یه جهت تحقیقاتی مشخص می‌کنی، و سیستم از فرضیه‌سازی تا مقاله‌ی نهایی PDF رو خودش انجام می‌ده.
🧪
✨
ویژگی‌ها:
🔺
کار با هر فرمتی: تصویر، صدا، ویدیو، اسکن سه‌بعدی، جدول، فرمول
🔺
درک مستقیم داده‌ی خام علمی، بدون تبدیل انسانی به جدول
🔺
سه مرحله: فرضیه‌سازی → آزمایش با کد واقعی → نگارش مقاله با DOI معتبر
🔺
اعتبارسنجی داخلی: هر عدد باید از خروجی واقعی کد تأیید بشه
🔺
سه روش اجرا: دسکتاپ، CLI، ماژول ادغام با ایجنت‌ها
🔺
پشتیبانی از Windows، macOS، Linux
🔗
لینک وب‌سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ielogQERaW1Ol7JiOCxxy_EExyNNbkFaqrdUiDqOFFN1srRXtwpEld19t6E8OK3-eeS-wgnlIQ9jc-SIu-dGWOVhU1YqIGYeofoiQW7rJKmFDHqiKede84HnONk0W6ZBsim8bJLlcn67rlmvea0V1fwKYHv2kbCbfVJfyS7F6exj4EmnjdvpOlQSNTXpgJ2jDceE7ztVci4i1NBwrvHFdsfBSlOqpSPxU_jmbV4NtOWX5fjMgjeMPgjPBv1vfiWVzteej28OLbGvWDuj9TPPCmL0dhBba9A0kTlsPscX_j3HHxwXYzDU7-F34yag-soomwt9MQX2vX4Y2EbaGGy6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جدا کردن صدا و موسیقی با یک کلیک
یک ابزار آنلاین رایگان مبتنی بر هوش مصنوعی Demucs که صدای خواننده رو از موسیقی پس‌زمینه جدا می‌کنه. کافیه فایل صوتی رو آپلود کنی.
🎶
✨
ویژگی‌ها:
🔺
آپلود فایل محلی با فرمت‌های مختلف
🔺
جدا کردن خودکار صدای خواننده از موسیقی
🔺
پیش‌نمایش آنلاین قبل از دانلود
🔺
دانلود جداگانه‌ی تِرَک صدا و موسیقی
🔺
بدون نیاز به ثبت‌نام یا حساب کاربری
مناسب برای موزیسین‌ها، خواننده‌ها، تولیدکننده‌های محتوا و ادیتورهای صوتی که سریع نیاز به جدا کردن استم دارن.
✅
🔗
لینک ورود به سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6-QMwNCvpb1IR11hy4uLuRNyqKUHB2t2aQdFIYcCLeke4iJ4TLsNn4sq6FlI0ShKjb0O7F9Mmt1_89O0ORLAcymDE-IzFIjiYO-fU1qsm4-Cjsxfk7HCsrIW51l1HGzYaU8sfOyLHOp6JfhWqwr3343Z2qJZvEnrETH523PVFhBFlKPxf7EoqZu5yg-XIScam0dcq8wNkbqhbNQSeQv1e9x9qRPadGjZUb_qnQ1F7xqT338PbQ8OiG0E2YKO0pAoFqZqOwAqCtVUL8tx2R_Wvjb8AfqXnXFtbtf7-HaC_siHwFNnqR2aY_T-GhxykdcalDerWWEdRNHE_EgbxpoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 دلار برای استفاده از API مدل های هوش منصوعی زیر
😎
🆓
Opus 5 | GPT 5.6 Sol
✅
در سایت زیر با ایمیل یا اکانت گیتهاب ثبت نام کنید
( ابتدا کپچای سایت رو تکمیل کنید )
سپس کلید خود را بسازید
✅
📌
Base URL :
https://true-sota.com/v1
📌
Model ID :
claude-opus-5
|
gpt-5.6-sol
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">DeepSeek V4 Pro
| MiniMax M3
♾
♾
♾
♾
♾
ApiKey
—
sk-dc9d4b7df36ba555-rcaq9e-2790fa25
Model
—
am/deepseek-v4-pro
/
am/deepseek-v4-flash
/
am/minimax-m3
URL
:
https://anymodel.org
♾
♾
♾
♾
♾
Free
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت z.ai بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید…</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=uBu5CTc6EwBOUwpChrYIvQwcraJmvPXSiOfYAg-k5fVLyUl6m6OCSmHcaU4NRHbKYPC-yxP0_o0WV-TtkEieIMZcEcfBl-jwbdIi5qRxTWr01to05jr8kEkOSlIALlTd3KjABQ2cB1z4CvpGLNg5qTsTsiAEY7NpEip7QC9jcrzQvGS7mjRvaRrlX5xwO-pfs13ee4BD-XryCmpjHcTTUCkimKb-KcejDWt5gYtCOcYiF6FuEb6fsVA1Z_hlcQ1uJOz6c8at049atXGzfugmzqVHrlg1DZUz6re3KGuFIvOPGRv1GOsfFBupj-M3MPPQPEbzhRG7g7fGBfT6-TXLIk3NPycTVyFmG5dFAgkqCOEtq7QMyHfSkkGeHUF-nermc-hpiiPvE0-s1RsLYI_Ejo_K8jVH6fo3mGZfvPcoDYdNP0Dp7HuMAZhbTxiDIGgMspmJTNEzwf2NQ--qeruC0zL092EvIYVSi9qf2Wxc2S2ND3ZrSNgI4U549yzC3j-ebaV32HgWcDIFnIC-hxHhhr2ivgLFpPeRL0Yd091ntdw6M8TRUIf_cWCtbekeqK5FFau8sjmHYzorkJxFzoomu2UwSr3qpeCvOt1VNHShFc9GAlka8iI-tfBJS7KEzBSAgmrtNWstoP1MvXNQ2y2x9a5Xs4z9Im0CVmjgu8T4YyY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=uBu5CTc6EwBOUwpChrYIvQwcraJmvPXSiOfYAg-k5fVLyUl6m6OCSmHcaU4NRHbKYPC-yxP0_o0WV-TtkEieIMZcEcfBl-jwbdIi5qRxTWr01to05jr8kEkOSlIALlTd3KjABQ2cB1z4CvpGLNg5qTsTsiAEY7NpEip7QC9jcrzQvGS7mjRvaRrlX5xwO-pfs13ee4BD-XryCmpjHcTTUCkimKb-KcejDWt5gYtCOcYiF6FuEb6fsVA1Z_hlcQ1uJOz6c8at049atXGzfugmzqVHrlg1DZUz6re3KGuFIvOPGRv1GOsfFBupj-M3MPPQPEbzhRG7g7fGBfT6-TXLIk3NPycTVyFmG5dFAgkqCOEtq7QMyHfSkkGeHUF-nermc-hpiiPvE0-s1RsLYI_Ejo_K8jVH6fo3mGZfvPcoDYdNP0Dp7HuMAZhbTxiDIGgMspmJTNEzwf2NQ--qeruC0zL092EvIYVSi9qf2Wxc2S2ND3ZrSNgI4U549yzC3j-ebaV32HgWcDIFnIC-hxHhhr2ivgLFpPeRL0Yd091ntdw6M8TRUIf_cWCtbekeqK5FFau8sjmHYzorkJxFzoomu2UwSr3qpeCvOt1VNHShFc9GAlka8iI-tfBJS7KEzBSAgmrtNWstoP1MvXNQ2y2x9a5Xs4z9Im0CVmjgu8T4YyY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
استودیوی هوش مصنوعی که خودش کارگردانی می‌کنه!
اپیکیشن MiniMax Design یک اپلیکیشن مستقل برای ویندوز و مک‌ هست . کافیه ایده‌ت رو توضیح بدی، هوش مصنوعی خودش برنامه‌ریزی، اجرا، کنترل کیفیت و نهایی‌سازی پروژه رو انجام می‌ده.
✅
✨
ویژگی‌ها:
🎬
ساخت تیزر تبلیغاتی، گرافیک، بنر، محتوای کاربرساخته (UGC) و انیمیشن
🧩
ادغام فیلم‌نامه، استوری‌بورد، ویدیو، تصویر، صدا و ادیتور در یک فضای کاری واحد
🔌
دسترسی به پلاگین‌ها و مهارت‌های تخصصی متعدد
📂
امکان وارد کردن فایل‌های محلی و اتصال به سرویس‌های خارجی از طریق API
💰
بعد از ثبت‌نام، ۳۰۰۰ کردیت رایگان اولیه به کاربر داده می‌شه
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r160o2zwfgQ1fgFLAC8q5S6QTOSXHc0VqDVTo9bSG9-v1fYYXfNyKP8MaHDNFuU3gLmkdmgbX1_nY_of84hqkW3UDPLtqc6ZyitZUgJBE8yXY9-_7XKbIIxXubXZq2-fWWdeYRiHRYvSXL4jrJETZhl3ocTR_oIa41YSMAKqKeQLTtZ440NfSXm4R-TmXALGts7qWhNoB7_maF_qUU-WdNzdaZ75R_LE_NP30uC8wUw8q1DR_GqQ5a5Xqv_aYtaDytg0AgR56ZqpbTWFJS_j87RddKdXHK9wbo21k7iFwjXrE3QoqNYbK3S42zOe0P5e1yieI5Yx4q_GgyXv--NylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐳
۹۷ ابزار جادویی برای DeepSeek Harness — یک دستور، قدرت نامحدود!
یک لیست باز از افزونه‌ها برای DeepSeek Harness (dsh) — با یک دستور می‌تونی قابلیت جدید به ایجنت اضافه کنی.
🔌
✨
دسته‌بندی پلاگین‌ها:
💻
بهبود رابط کاربری — TUI، پنل‌های کناری، پالت دستورات
💬
نشست‌ها و پیام‌ها — شاخه‌بندی تاریخچه، اشتراک‌گذاری گفتگو، حافظه
🛠
ابزارها — اتصال به دیتابیس، CSV، JSON، regex، آمار
⚙
اتوماسیون — هماهنگی چند-ایجنت، زمان‌بند وظایف
🔔
اعلان‌ها — اتصال به تلگرام، هشدار دسکتاپ
🧩
توسعه/رانتایم — ممیزی امنیتی، sandbox، ابزارهای گیت
🎮
فقط برای سرگرمی — بازی‌های کوچک، استیکر، پت مجازی
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxJG4E-yG-JdAriIZQuJ6N-tsL4zeMlEDhfVnkN_-D5EWxpOzoAJR2-w2RQR081iD7ir_ZUnkOmGiVDN3JH2ijQqlyGno8psDdtwFVhrcqBxzeUHqZjUDVJ6c-NwKp8tw5kIsY8GSuROQp3bBLwnhOAqMFiZ5HxSs5XC41DItpr2OFiEeS2tGk7vC8OAw91UuuZ66wplbvHrQqEG7hCsGTziUE8JoAFbMvMWEaZaHFp2klnjRugPAJoOtmsWn6d0la5FJTYSeOc7KnEi06WgECR5miu0cA9hiQy_WHx0TYQltbAGywsDL5XySLLK0us-ZzbShZTO3YM-wOWCgMyuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
پروکسی وب جدید تلگرام — پنهان‌شدن پشت سایت‌های معمولی
تلگرام یک روش جدید برای دور زدن فیلترینگ آماده کرده که ترافیک پروکسی رو کاملاً شبیه ترافیک عادی وب می‌کنه.
🥸
⚙️
نحوه‌ی کار:
🖥
تلگرام دسکتاپ یک مرورگر کوچک داخلی باز می‌کنه و یک اتصال معمولی HTTPS/WebSocket با دامنه‌ای برقرار می‌کنه که ظاهرش شبیه یه سایت عادیه
📦
کل ترافیک MTProxy در یک جریان واحد بسته‌بندی و از طریق این کانال مبدل ارسال می‌شه
↔
روی سرور، یک نود واسط (relay) این جریان رو به اتصالات جدا تفکیک می‌کنه و بدون رمزگشایی، به MTProxy معمولی می‌فرسته
🌐
دامنه هم‌زمان یک سایت عادی نشون می‌ده، و صفحه‌ی «پل» فقط برای تلگرام و بعد از تأیید باز می‌شه
🎯
نتیجه:
کل ترافیک از دید ارائه‌دهنده‌ی اینترنت مثل بازدید از یه سایت معمولی به نظر می‌رسه — یعنی پنهان‌کاری تقریباً کامل در برابر فیلترینگ.
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq5ndpT0JOwu4QOHYx0ZXhLAKFBbcrSGAnTm_atw09glAm7V_1itPJoGrYBK-n8ESDm5OdSWkWHjH2xKbPRKKHv_P59lUR_w6YO9rOyn3i9H2ywLLP_LwIArI4Rimh6H3y3CuV3umJrBpqU1h_oUuMvF2KCDpYaLe59UuK_qIsO24QGL6SaBjsnOyuykq3ilAqGwjo-4WE46em-nXrureXF6J06iBfsOAmtNLOxe5j5cBLaBI0-rLAt--HNwYgIKFEY_quWVsETdJd9kkKhGRgJiOWNco5NjscPQRzo5SzruHFkErHRjRCcKIbh3n058sGfuMYpSoe0u0fPE-rXZ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
زمین بازی هوش مصنوعی برای ساخت چهره و آثار هنری
سایت Artbreeder یک ابزار رایگان آنلاین برای ساخت تصاویر با هوش مصنوعیه که تو ساخت چهره، کاراکتر، منظره و هنر انتزاعی خیلی خوب عمل می‌کنه.
🖼
با کشیدن اسلایدرها می‌تونی ویژگی‌های چند تصویر مختلف رو با هم ترکیب کنی و یه تصویر کاملاً جدید بسازی.
⚡️
✨
ویژگی‌ها:
🧬
ترکیب و «تولیدمثل» تصاویر با تنظیم سن، جنسیت، حالت چهره و...
🖌
ابزارهای متنوع مثل Composer، Splicer و Collager
🤝
کامیونیتی فعال برای ریمیکس و اشتراک‌گذاری آثار
⚠️
نکته‌ی مهم:
تو پلن رایگان، تصاویری که می‌سازی
به‌صورت پیش‌فرض عمومی
هستن و همه می‌تونن ببیننشون.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKFQKRZzwfbCa6MFK6o-NzhdV_p3L6VE0f5rf58qhewhadK-uXMacp0tM7HqJ8dxouYxTm299GR86i2I3Ma8vKi5t0KN2lIfyrdm3kBCwCe-BbgaT3qpE-b5LVHzOBsEK8H8ktIr25Lcl3BJbyuUJSonzS3CsZiqJTLL_3jfghI6tKfYO_0RJly-7f4bpITJoudF-9wRxS0Gta5lTCdmvfc6UiELgw0xm2gYJ7lMDORcXU3znmYgi08BIWCmW2Wxyz2JloJNruJIMBLTS50z-deVTCiYb3WLXKEJme67JvU6VSd4xXceBJapXa9Ni5mxgwu-hcp8_vYMH9Dkxx-VKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
دروازه‌ی رایگان به میلیون‌ها مقاله علمی
سایت CORE یکی از بزرگ‌ترین موتورهای جست‌وجوی مقالات با دسترسی آزاد (Open Access) در دنیاست.
🌎
بیش از ۴۰۰ میلیون رکورد علمی رو ایندکس کرده و برای بیش از ۴۰ میلیون تاشون، دسترسی به متن کامل رایگانه — بدون نیاز به اشتراک یا پرداخت پول.
🆓
✨
ویژگی‌ها:
🔍
جست‌وجوی پیشرفته
📥
دانلود مستقیم PDF بدون پی‌وال
🎓
پوشش تقریباً همه‌ی رشته‌ها
اگه دانشجویی و داری پایان‌نامه، مقاله یا مرور ادبیات می‌نویسی، CORE می‌تونه یکی از منابع خیلی خوب برای پیدا کردن رفرنس‌های معتبر و رایگان باشه.
📝
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcRMRZ7Lu7Y56K9D0IEgEvGy8XiJHXPVbRS6dE9IoZM3P9lYL1vWlaz1avIDepnp-3rr1RcQLRnm55Xm00tdC8RnR0QgNXe6z2rANaZ7OXj-fitH54_kmfrStEdzyAHaSn38ji0xXVbYq-hssifgTEh7kutBVzePeetXSqk6LgAVTYLdpKo_XmjF_T-cgGBV-dygCjLfu2kuyBWYhWYCl8qJNQVHfDtYk-Zxp6nZiKIU1TLUC8RAL4F9kE43lmFX3NvbSZyzQdeJMJgIz3l6xjrOfS50_VsYiuOIx7Q38DCLM8WhntnJZbe3TuyvKgpOJB-JOaROWtxN95ioZQNFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار رایگان API تا ۳۰۰ دلار بدون نیاز به کارت بانکی
🆓
🧠
فقط با اکانت
گیت‌هاب
ثبت‌نام کن و بسته به سن
اکانتت
اعتبار رایگان بگیر
✅
با این اعتبار می‌تونی از
مدل‌های قوی
مثل
GPT
،
Qwen
،
DeepSeek
و بقیه استفاده کنی بدون اینکه هزینه‌ای
پرداخت
کنی
🟩
Link
🔗
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">🚀
آپدیت جدید ربات وگا
🧠
حافظه هوشمند وگا
از این پس وگا اطلاعات مهم شما را به خاطر می‌سپارد تا گفتگوهای پیوی طبیعی‌تر و شخصی‌تری داشته باشید.
💬
حافظه در پیوی:
اسم، سن، دستورات و قوانین دلخواه شما ذخیره و در گفتگوهای بعدی استفاده می‌شود ( قابل حذف کردن هست )
👥
حافظه ماندگار در گروه:
دو نوع حافظه مجزا
• حافظه عمومی: قوانینی که برای همه اعضای گروه اعمال می‌شود
• حافظه فردی: اطلاعات هر کاربر به‌صورت جداگانه در همان گروه ذخیره می‌شود
از بخش «سرویس‌های هوشمند» گروه فعال می‌شود و قابلیت ریست نیز دارد
♻️
📊
حافظه کلی ربات نیز گسترش یافت. وگا اکنون پیام‌های بیشتری را در گروه‌ها و پیوی‌ها به خاطر می‌سپارد.
🧰
جعبه ابزار جدید در پیوی
پنج ابزار کاربردی اضافه شد:
💵
بررسی قیمت ارزها
📰
آخرین اخبار
🌐
تعامل با وب
🌎
مشخصات IP
💱
تبدیل ارز
🌐
تعامل با وب:
لینک هر سایتی را ارسال کنید تا وگا از آن اسکرین‌شات بگیرد، لینک‌های صفحه را استخراج کند، یا به HTML/JSON تبدیل کند
🌎
مشخصات IP:
آدرس IP یا دامنه را ارسال کنید تا لوکیشن، دیتاسنتر و سایر مشخصات آن نمایش داده شود
💱
تبدیل ارز:
به‌سرعت بفهمید هر مقدار از یک ارز معادل چقدر از ارز دیگر است
🛠️
بهبودهای فنی
✅
تمام باگ‌ها و مشکلات گزارش‌شده برطرف شد
⚡️
ریت لیمیت گفتگو از ۳۰ به ۴۰ افزایش یافت
🤖
مدل هوش مصنوعی جدید DeepSeek V4 Flash (0731) اضافه شد
✉️
هر مشکلی مشاهده کردید، به پشتیبانی ربات گزارش دهید
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
🧠
Vega AI
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsfnpbxICbOY2t7vVggDjwFFFC-7du8MO7CzeNSvSDsr7cv7J5H4nQPmqDZF4uk_Js4jSTuucY0yHZAd0KdWNkzWgAi4N3FfENjqRAmmFLscycmIAyWg3N2ZYCkrppsxxqOplj98kEyDhgHH1pNjqAGL3waoVW-kjtlWvLNIBocwSpt6tMcJ0WCPtBbS5PNEuRJAq0kAGNY0WoVwIeyC0906MKEJMKsCdykVOGW9R0JqQ-GXV9v_im_sE1kfg1iFPJ_gPL3hhoJEjMkLih29_xK4k1VXyh31jJ4ndwfSDty-MRmboIKwoWBsBnvaB6jMbglISvGMxUV4g-kMK0iYsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی کاملا رایگان به مدل های هوش منصوعی زیر
💥
🆓
Opus 4.8 | ox alpha | Kimi k3 | GLM 5.2 | Deepseek V4 Flash 0731 | muse spark 1.2 | Mimo 2.5 | GPT 5.4 | Grok 4.1 | Haiku 4.5
✅
📌
Base URL :
https://api.yjs.im/v1/
موقع ساخت کلید حتما گروه Free یا Free lite رو انتخاب کنید ، قبلش به بخش Playground برید تا بفهمید هر گروه چه مدل هایی رو پشتیبانی میکنه
✅
برای استفاده از مدل های رایگان داشتن کریدیت نیازی نیست
❗️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=j2L3TB37c3xo5GZTzkjmuR-evBFnyCejktfDX3FADYMpUdJg3pJ0dQtqoDeZ1HV0P1yrXvvilGTwzuHzE1ye9FTscss5Qu7M1N_ddDNMWKKexYEGBPnP2YYwmNI6O6_ofwKsHdRZel8pQub5GEkE7M5BoMPKFqZWYrG5OZOynBLm4xLYzS9JSksiOdi8Db3LCQMeS107OmvfFHi-7SSqF_GLzSVBpeTZVdc7lLVOewy0jFUkGW4_R6wbTifuPo189jwcYVwtl08PGoaXQV5ISe_qemheXv9PkzCs88ZSNaSp-RZ7aO6ilNFx5eLE9-ugzg1zJIZtvJZOxQEs_F_FxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=j2L3TB37c3xo5GZTzkjmuR-evBFnyCejktfDX3FADYMpUdJg3pJ0dQtqoDeZ1HV0P1yrXvvilGTwzuHzE1ye9FTscss5Qu7M1N_ddDNMWKKexYEGBPnP2YYwmNI6O6_ofwKsHdRZel8pQub5GEkE7M5BoMPKFqZWYrG5OZOynBLm4xLYzS9JSksiOdi8Db3LCQMeS107OmvfFHi-7SSqF_GLzSVBpeTZVdc7lLVOewy0jFUkGW4_R6wbTifuPo189jwcYVwtl08PGoaXQV5ISe_qemheXv9PkzCs88ZSNaSp-RZ7aO6ilNFx5eLE9-ugzg1zJIZtvJZOxQEs_F_FxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بزرگ‌ترین نقشه جهان منتشر شد
دانشمندان بزرگ‌ترین و دقیق‌ترین نقشه‌ای که تا امروز از جهان ساخته شده رو منتشر کردن؛ حاصل ۱۳ سال رصد بی‌وقفه با ده‌ها تلسکوپ برتر دنیا.
📊
اعداد و ارقام قابل توجه:
🪐
۴ میلیارد جرم آسمانی
☀️
نزدیک به ۶ تریلیون پیکسل
📷
برگرفته از ۲۶۳ هزار عکس
این فقط یه تصویر ساده نیست؛ دقیق‌ترین و جزئی‌ترین تصویری‌ه که تا حالا از کیهان ثبت شده و بعید هست به این زودی‌ها دقیق‌تر از این ساخته بشه.
🔭
می‌تونید خودتون توی این نقشه کاوش کنید و گم بشید توی ابعاد کهکشان‌ها:
🔗
لینک سایت برای مشاهده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9xNsdk-bZVmgawpNR3p4s0wlJlO-W59p-CT022CjjUeMcFk-ahZma9cToM_HfyrULSbEGNLCzFaEoidr6Q9mg698RvzzT68GGnHuiNKbo3GsrGFVftRK5f0fkAYri2w-rsyasCYFZC65GjBhAfvYaT3OoggxxUuPwqYK5rQvUlCUu-DW6NxmKZJgCGPwMCDp3ZwChr7Fup4UJ52K9d0tXZES4lJjlX_pCLx3chUtsv3jwQaYDP6PuoTtThTAI8shefiNVlclw2-5IdFiPfJEfwfnQIe-_nV6bAOet5AfLlS19iJLs2Dq0kvsWCh3_IouoCElEBawTN6Sj1SkVDwpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل استلثِ ناشناس Ox Alpha رایگان شد
🥷
مدلی ناشناس با نام
Ox Alpha
، بدون هیچ اعلام رسمی از سمت سازنده‌اش، روی OpenRouter به صورت یک هفته رایگان و OpenCode منتشر شد
⚡
✍️
مشخصات فنی:
🔺
پنجره کانتکست: ۱ میلیون توکن
🔺
حداکثر خروجی: ۱۳۱ هزار توکن
🔺
ورودی مولتی‌مدال: متن، تصویر، ویدیو
🔺
قیمت: رایگان طی دوره پیش‌نمایش
🥸
سازنده مدل مشخص نیست. این یک انتشار «استلث» است — یک تأمین‌کننده ناشناس در حال آزمایش مدل است، و OpenRouter صرفاً درخواست‌ها را روتینگ می‌کند، نه توسعه‌دهنده یا مالک آن.
🇨🇳
❓
درباره منشأ مدل، برخی کاربران گزارش داده‌اند که در پاسخ به سؤالات حساس ژئوپلیتیکی (از جمله تایوان) رفتاری مشابه مدل‌های چینی نشان می‌دهد. این صرفاً یک گمانه‌زنی است و هویت سازنده رسماً تأیید نشده.
📈
طبق ادعای برخی کاربران، این مدل در تسک‌های کدنویسی agentic عملکرد قابل‌توجهی داشته، هرچند این ارزیابی‌ها فیدبک کاربری هستند، نه بنچمارک مستقل رسمی.
🔒
بر اساس توضیحات ارائه‌شده، داده‌های ارسالی طی دوره تست برای آموزش مدل استفاده نخواهد شد
🔗
لینک صفحه در OpenRouter
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYn2czogZTDWT_uEAUDoxVko4ub_yAjRD8Rlq5XeqUeBjZ0xzCPdEkwuSCHf0vS79IgB5A-ZLZf6D2DDrQil0aDufX_WWAimwko15Qmzr3cHD0_MJAMCoFmSWRw8uH8tYbIJ9F0mf0YKdHh2feqzEFqNtlmD4rzOg7Cz2Y2BkVNHRZr_qXVoF0M9isJ-CyIysgXUYrKMPn9U1dfL9Q8WWf3VLT0NVH_vmsjaN3_WqLbal01chsFUKEJnCiL7tgAMaT7SNYaYITDGwX9ec8oZ-ciG7bXuTFyPUYxZTsOkUiCGQ-s7iE02VdDIdl2ioiGTuSbUYi7yIZSRrJGZg4T_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">70 دلار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله باشه )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
40 دلار
و شخص دریافت کننده
70 دلار
دریافت می‌کند!
همچنین تا 25 دلار پاداش لاگین روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlTHGHjTX4_E2_tKkBUcb6A_WDKfrnq4fxSetV10MC-5Yb8qBrmBB5jLfzrLss3aDGaThBmy9iGXOy2FBJN2AgBEHBDI9Vzetc_BflbkGNF9mD7IAq1YSLoY95ZzncJ3xW7cGEFcHLjXORZOpfX8rO09-95Z0Y78P6tkGFQt1i9d1lS-ETHb6oBHNKL37fG2zQg9dkJtVdE2LHt85UO2VSF8DiCIKrfzlWM753PWXZQhYdnsC353yzCVgXGgMTZzMqMQ-fgWPxP8Lv-vydjDm0ZROAoLlLZNsOjKw7Yv1B4GPrN_SDVj8ztiOjsfZ7sZcrtbzJaQdXzHCPa7wETdqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYIftrfvkJN-wgKscLn4WCY1spg4YxfQOc5EIHV8CRr8l_MKlrkHWm1vrJKvyB1wkqEO5yOgipiiOK14y7iQlFL81PWjjcT6JPTUEwbKPXgPdey62MuswyaW2Ct8G-rY9qgaGSrlnpimC6G0zwVF8czSDAkdzYFSAzZsCgM59vvfwek3_IZiBSI7-jB8DkmIe5Bd9Boh_scMoAh1b2MauliLzJVZV2Jb-DLQQgMeya-BN3jE1mV3LWZxr_-0TahFbwDKnpKfZHqMk0l6yh8nE2Ik3PYxrknxjV46F-N5j90Ji5EahE_-45V3I2WFOjvMSL4h5Wa4D_nUql7xD3G5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 میلیون توکن برای دسترسی به API هوش منصوعی زیر
💥
🆓
Deepseek V4 Flash 0731 | Kimi k2.6 | MiniMax M2.7
✅
📌
Base URL :
https://hskyauefqcgbvgvxkluj.supabase.co/functions/v1/gonka
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔒
بهترین ایمیل‌های امن و خصوصی
اگه دنبال یه سرویس ایمیل هستی که حریم خصوصیت رو جدی بگیره، رمزنگاری کنه و داده کمتری ازت جمع کنه، این‌ها بهترین گزینه‌ها هستن
🛡
🇨🇭
Proton Mail
— معروف‌ترین ایمیل رمزنگاری‌شده، با پشتیبانی کامل E2E
🇩🇪
Tuta Mail
— تمرکز کامل روی حریم خصوصی، رمزنگاری در هسته سرویس
🇧🇪
Mailfence
— پشتیبانی از OpenPGP، مناسب کاربرای حرفه‌ای
🇺🇸
Riseup
— سرویس غیرانتفاعی با تمرکز بر حریم خصوصی
🇳🇱
StartMail
— قابلیت ایمیل مستعار (alias) برای حفظ گمنامی
🇩🇪
Posteo
— بدون تبلیغات، حداقل جمع‌آوری داده
🇸🇪
CounterMail
— امنیت بالا، پشتیبانی کامل از OpenPGP
🇨🇦
Hushmail
— مناسب استفاده شخصی و حرفه‌ای، رمزنگاری‌شده
🇩🇪
mailbox
— سرویس قدیمی و معتبر آلمانی با PGP
🇨🇭
Librem Mail
— از تیم Purism، تمرکز بر حفاظت داده
⚠️
نکته مهم:
داشتن رمزنگاری همیشه به این معنی نیست که ایمیلت کاملاً end-to-end رمز شده — یعنی گاهی خودِ سرویس‌دهنده هم می‌تونه محتوای ایمیلت رو بخونه، هیچ ایمیلی هم امنیت 100% تضمین نمی‌کنه؛ این چیز به عوامل زیادی بستگی داره: تو کدوم کشور سرور داره، چطور داده‌هات رو ذخیره می‌کنه، و حتی خودت چقدر رعایت می‌کنی
❗️
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxXxwca9H939edSYrVwWRMemUx5HW7kXaScCaAW3zlHRaxR3WMoINtci2ZtI1ngPvhzgUiir5MBR1iFwA8lGkO3DJozk9p892yW8XN8N1lUrnO-1sfgcemmmVLHoE0LvT1Jtg_NF8bDUeU6FLema4WLwOx5dXFu9Qxv0KueTJT_dWHyGHXrMa1juI0PHfa4fkf5lNFkzYNbqb8cG58xutJHVBPCkuq5FFVIfBKxKYtbPkzyPVdpnm6LMOJ2upyB0dr5sTYBFA8rGmobInQY-36YsJizugdRDbO1Ez8fItoPohUlFLiro4-RKKF4KxVoOAC9fOh1_t8Hd7BVzVrOH6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">60 دلار کریدیت رایگان برای استفاده از API بهترین مدل های جهان
💥
🆓
این سایت 50 دلار + 10 دلار هدیه رفرال و هر روز 5 دلار بهتون میده تا بتونید از بهترین مدل ها استفاده کنید
✅
Opus 5 | Fable 5 | GLM 5.3 | Kimi K3 | Qwen 3.8 max | Grok 4.5 | Deepseek V4 Flash
✅
✨
مراحل دریافت:
1️⃣
ابتدا در
این سرور دیسکورد
جوین بشید
2️⃣
حالا در
این سایت
با اکانت گیتهاب ثبت نام کنید
3️⃣
حالا سایت رو به اکانت دیسکورد خود متصل کنید
تمام حالا برید
از این بخش
کلید بگیرید و استفاده کنید ، همچنین به بخش پروفایل برید و 5 دلار امروز رو دریافت کنید
🎉
📌
Base URL :
https://tokengate-cqt9ivzs.manus.space/v1
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دو سایت عالی برای گرفتن دامنه رایگان یک‌ساله
🎁
با این دو سایت می‌تونید کاملاً رایگان دامنه بگیرید، فقط کافیه مراحل زیر رو دنبال کنید
👇
━━━━━━━━━━━━━━━━━━━━
سایت اول (ساده و سریع)
✅
🔺
دامنه‌های قابل دریافت:
de5.net
–
cc.cd
–
bot.cd
–
bbroot.com
–
ddns.ge
–
l.cd
–
ccwu.cc
📝
مراحل:
1.
وارد لینک ثبت‌نام بشید
2. یک اکانت بسازید
3. تا ۳ دامنه رایگان می‌تونید دریافت کنید
🎉
━━━━━━━━━━━━━━━━━━━━
سایت دوم (کمی زمان‌بر )
⚙️
🔺
دامنه‌های قابل دریافت:
indevs.in
–
sryze.cc
–
ryzedns.org
–
nx.kg
–
ryzn.pro
📝
مراحل به ترتیب:
1️⃣
وارد سایت بشید
و با اکانت گیت‌هاب (GitHub) لاگین کنید
⚠️
نکته مهم:
اکانت گیت‌هاب شما باید حداقل ۱ ماه از تاریخ ساختش گذشته باشه
2️⃣
بعد از ورود، یک کد QR نمایش داده میشه
اپ Google Authenticator رو باز کنید و این QR رو اسکن کنید
3️⃣
کدی که اپ بهتون میده رو داخل سایت وارد کنید
4️⃣
به این بخش برید
و روی گزینه Repo Star بزنید و برید به ریپازیتوری گیت‌هاب اونها
⭐️
بدید
5️⃣
در آخر روی گزینه Verify کلیک کنید
🎉
تبریک! حالا می‌تونید از هر ۵ دامنه، یکی رو انتخاب و دریافت کنید (در مجموع ۵ دامنه رایگان)
━━━━━━━━━━━━━━━━━━━━
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR-nD9cpcfUbUgKo1hDdAkF7sWsrFpnSqny7md4d37HFhONY1bmrEAKqVNtLevdNnwhkkaW96aHfws7IJ7Bls4c3N6nbVymq3TRWScz8PdzY4_ZT_Dh3K3ko1Do1PzMsylu52Vl_pbNsibKHhmg04DKG7-dpbCqyjvGnMJP-EUygaUy6kvrDrZuV2yYPnoV2GkIEajecH-fFt2D3XDTee2RCCI5wiIcXoHoIgPDgOoU61cNa3dJJtK80gYwA7moNeAS9cZpK3-e9CdwdjFWJLb8csn7Jxrv_TDIC2RQVP-B-2r-bm15f-UxdIG--ocSbrXmHFrdIufQjWkfS_SRMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن رایگان هر روز تو xkiro
🔥
مدل‌های
Qwen
،
DeepSeek
و
Grok
4.6
رو بدون نیاز به کارت بانکی امتحان کن
😤
برو
x
kiro.com
،
ثبت‌نام
کن، پلن
رایگان
رو انتخاب کن و کلید
API
بساز
🔻
هم می‌تونی مستقیم از
API
استفاده کنی، هم بعد از ثبت‌نام با اکانت
تلگرامت
احراز هویت
کنی و 5
دلار
اعتبار هدیه بگیری
🎁
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfRSh9eNUGu9G1VSPo8BSpwoncQrSqQ6mMZJizKftE-NairmO3py6fWhdqJAFopZ3b38wn1yWcIkw96CGMgE1tCMhKQmz46p5XOez-pj4srGpcE9_6gbVYDrd4Gr_JP612b3h_OwPVAozKygyT4mY3XBi9iAlu1G6Z4YgyxPyURmIWNTvsxxeKQT66Fob_9WV0tb_L9cmsBnDRfuVfghaUq-KyivWeHBHLwtaLRJRO1eqxHJroLJMgsUiZvBAX7GKlbGeYPmi2Nmh2gJWzbrQtoVt6q5nBKUia3wx-i-Jw8Y3Dmg8N2lT_cBSmhMGeMBveB0dncZu_d47Cflu5v3cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی
💥
🆓
Kimi K3 | Qwen 3.8 max |  Gemini 3.7 flash | Sonnet 5 | GPT 5.6 Terra | Deepseek V4 Pro 0813 | Deepseek V4 Flash 0713 | Gemini 3 pro image
✅
با این سایت میتونید به کلی مدل قدیمی و جدید دسترسی پیدا کنید این سایت هر روز به شما 100k کریدیت میده
✅
📌
Base URL:
https://api.anyapi.ai/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مدل قدرتمند
Qwen 3.8
با ۲۷ میلیارد پارامتر الان رایگان روی پلتفرم آزمایشی هتزنر در دسترسه
☑️
اگه اکانت
هتزنر
دارید، فقط
API
رو بردارید و به هر ابزاری که با
OpenAI
سازگاره وصل کنید دیگه لازم نیست پول بدید
🆓
مستندات کامل اینجاست
➡️
experiments.hetzner.com/docs/inference
اگه کسی بلده چطور راحت‌تر اکانت بسازه یا ترفندی داره، لطفاً اینجا بگه تا همه بتونن استفاده کنن
🤝
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eb_03RTIedgRDvtnPkl9_q58qVHeiqR3iQQs1kPJVgatE1P_P5NJo3NKrHX1Hh82zzoPIAcK0k5BIDCakz7HmOy-IesA4seG2lhwFAHXdR_l6bYk4p8qrUNE1X1BoyxG_ahX0h-o6GD0BjUKTMMp3e8GfQuLgQJ5Aa1PPi8LIBOIHDv2v9d3SCTU9xoZnKVdlQWQI94CPbUKGYzKXb7AMmu4-ETdwjOVaHY5QqfsXEaiHj8mfSEM8zd6uYzhOon9ZZiYK0aRwzfEHsT3sHOgFkmsrYTJoMIcPlTXZXaaGyyKrj8Ft-5CvpilBfXhY4RTdckw5cJFRk4Z1GSW01wNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vjq6EDtRvui5hPq8GuR4M-7wdIYkOiBE23SRVB8OWK_BRN_l6pvGYzEr74H9OtQCaZlflFvRkj3eqf1-js4dOv-At9SZtKPZVCTOJKTbkgFeTV-363UOGXvTAmMQMSblFLd04VE3SGBgsEdqNMd1G6E__E2eISWKEtCko9M_4D4-YhA-4UO7fO3w40rCb3GZiE-NWH5xoS-uXBkm4zXwXb0WM4oSqwAcCSQcVTjVUP25MKdOvhZu9U3lnQmQUyDxVl3kVhXaSkJElNmN8Xl7rY1yn0Rag90QuTgoDdxBWsPStspTIOMC9hPXBG4qyUa-z1cB4ssM9JkxbJvLvHt02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت دامنه رایگان مادام‌العمر
💥
🆓
با این سایت یک ساب دامنه روی دامنه‌ی
kdns.fr
رو به صورت دائمی و رایگان دریافت میکنید همچنين میتونید اون رو به کلودفلر اضافه کنید
✅
✨
مراحل دریافت:
1️⃣
وارد
این سایت
بشید و ثبت نام کنید
2️⃣
به بخش
My Domains
برید
3️⃣
روی Order a domain بزنید و دامنه خودتون رو بگیرید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=CGakY_bkriE8CIIr64Au0ZCBdkJ9rt2Idn2QPig71yGYJhckw_20xRI8Yhs_Sa19dm9xYRNozlHeFXcXwGXG2Fu3W4d2mPE59E9XvEEyQTMzN1oNKDbe--67hlc2bDJlumTLf8RCPdpMXyYnKn14CFlSv3Y8L05AOmeVNb_EnY_w66VzxNnTQjqMQuSrFYm1RK_NwfhR7Sxdf2XC1QyHEtfCwsrFptsYPKvvYXJWifSkeRCogCJ3fpwQc-7seUD77Ia93uPnVJl3C-pmRlO_IyWc3jS24zSJL7VzsXwQO0HGf6NFIqpw1L5IGbGZnHIgyVzW3J2SFk8rq-GrsVgnpIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=CGakY_bkriE8CIIr64Au0ZCBdkJ9rt2Idn2QPig71yGYJhckw_20xRI8Yhs_Sa19dm9xYRNozlHeFXcXwGXG2Fu3W4d2mPE59E9XvEEyQTMzN1oNKDbe--67hlc2bDJlumTLf8RCPdpMXyYnKn14CFlSv3Y8L05AOmeVNb_EnY_w66VzxNnTQjqMQuSrFYm1RK_NwfhR7Sxdf2XC1QyHEtfCwsrFptsYPKvvYXJWifSkeRCogCJ3fpwQc-7seUD77Ia93uPnVJl3C-pmRlO_IyWc3jS24zSJL7VzsXwQO0HGf6NFIqpw1L5IGbGZnHIgyVzW3J2SFk8rq-GrsVgnpIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
📱
وایب‌کدینگ حالا رو گوشیته!
ابزار HAPI اومده که به‌جای جایگزین کردن ایجنت‌های کدنویسی، همون‌هایی که روی سیستمت داری رو مستقیم از موبایل کنترل می‌کنی
🔥
سازگار با Claude Code، Codex، Cursor Agent، Grok Build، OpenCode و چندتای دیگه
✅
🎙
کنترل با دستور صوتی، بدون نیاز به تایپ
📂
دسترسی به ترمینال، چک فایل‌ها و اعمال تغییرات — همه از گوشی
💻
سشنی که روی کامپیوتر شروع کردی رو بدون قطعی و از صفر شروع کردن، رو موبایل ادامه بده
🔔
تایید هر درخواست هوش مصنوعی فقط با یه تپ، حتی وقتی پشت سیستم نیستی
🤖
حتی از تلگرام هم قابل کنترله
نکته‌ی جالب: HAPI کاملاً local-first و متن‌بازه (AGPL-3.0) — یعنی داده‌هات روی سیستم خودت می‌مونه و به سرور خارجی آپلود نمیشه.
✨
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الان سه تا مدل قوی رو می‌تونید کاملاً رایگان تست کنید
🆓
برید سایت زیر ثبت نام کنید و به راحتی از مدل های زیر استفاده کنید
✅
✔️
مدل‌ها:
•
z-ai/glm-5.3-free
• dots-studio/dots3-note-prev
• deepseek/deepseek-v4-flash-free
🧾
Link
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تلگرام برای دریافت پسوند دامنه .gram درخواست داده است
🉐
اگر این درخواست از سوی ICANN تأیید شود، بیش از یک میلیارد کاربر تلگرام می‌توانند دامنه سطح دوم اختصاصی خود را داشته باشند
💎
مثلاً
@durov
می‌تواند durov.gram و
@monk
می‌تواند monk.gram را ثبت کند
☑️
علاوه بر این، کاربران فقط با نوشتن یک
پرامپت ساده،
وب‌سایت‌های تعاملی خود را مستقیماً روی زیرساخت تلگرام راه‌اندازی خواهند کرد
🤯
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF8SoimsKsNtaoflG50rbGm5frZJZjBmpIeaZRso0M9vmRjg1P_hj21kD8YfZK2RmbRCR9PwSZBYZpdozXLaXqpLe-BF6D3_7GVHp09DNo9knC8BzqY43liaghSJZjTyx-XkPVyJxPWEw7j2Vz9H0es69PVD4Tv_aQYhIyC-BZgP-4bIvXgoU3JP8JyoyRv_tKI54YULx8pu5Z85Nt0VOSdo9DHO1leKQEoqYQ-UJcfVTTyCu4WYUAJoqBfuU_r2iq5QZRnmurX6UKQfk_DHjszuwM3lBzf9dMVG99F9EWgzaz8E_MWi12eaLy1KIB19GOd0M-fDxQK4iBwJzwya6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود کد ابزار قدرتمند طراحی گرفت
🎨
تیم Anthropic به عامل هوشمند خود قابلیت جدیدی برای طراحی رابط کاربری وب‌سایت‌ها و اپلیکیشن‌های موبایل داده است. کافی‌ست دستور /design را وارد کنید و تغییرات موردنظرتان را توضیح دهید.
🔥
سیستم به‌صورت خودکار کدبیس موجود را می‌خواند، خودش را با سبک طراحی فعلی تطبیق می‌دهد و پیش‌نویس‌های متعددی را در قالب طرح (artboard) تولید می‌کند که می‌توانید به‌صورت آرتیفکت به‌اشتراک بگذارید  (The Decoder) . کافی‌ست طرح موردعلاقه‌تان را انتخاب و ویرایش کنید، سپس آن را وارد فاز کدنویسی کنید.
✨
این ویژگی هم‌اکنون به‌صورت پیش‌نمایش اولیه در دسترس است  (The Decoder) ؛ برای امتحان کردنش کافی‌ست دستور claude update را اجرا کنید.
✅
🔗
لینک دیدن جزئیات
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تست کردن مدل‌های هوش مصنوعی
🚀
حتماً براتون این سوال پیش اومده که مدل هوش مصنوعی‌ای که از یک سایت دریافت می‌کنید، چقدر به مدل واقعی نزدیکه؟
🧐
آیا واقعاً همون مدلی رو که ادعا می‌شه دریافت می‌کنید، یا یک نسخه‌ی ضعیف‌تر و متفاوت؟
👀
✨
توی این پست، ۲ سایت معتبر رو بهتون معرفی می‌کنیم که باهاشون می‌تونید مدل رو تست کنید و خودتون نتیجه رو بسنجید
🔗
لینک سایت اول
🔗
لینک سایت دوم
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXRBrdV2jnheygg1UpSlbWevYa5Zi-UNsJY19bU054W1irGAuv12jd1-5mJw7XPShJ6uWK3b6UJfl6Dob8UU042BjK85VaB9Beg5RD_XAExiOsGdNx_MYJnOf271XPGp7TTMnJWiW7yhWTEwp1Y8GphTpWnoZz5_0JWFisnoU8dP_tnzVhO3XFBXgtJwUZfJsKNenk9ZD61AM5VxufCUNok-O4-bFZVgu0eBSoLfT2Cy68K1DFUAYGX8WutlItq5nqKtuR4uze6eh9Rs829t30g9BDgoCzMIcIWHZQBfN0P_vgHqghtSXrEAEYYU6MZvL336jGyUz-4i35pkZswSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL :
https://api.b.ai/v1
📌
Model ID :
deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6nUnTYOLGAoYbRCU876fS8PrXmMwjjV9rGVAgfjTaio88KfZnoEhGOEjZ-bI9WHR5-HXDl9koJAF7Jz3D38TgKW2GrBE05S2jjdkaEXVVz1nZKrS-7Q39N_L5ag6BFrR-mTpND8fOeLyh2paj-Z25_SGyjaP5L8_5N1hRegYJtpUxNbwJjmqGYhXzu7VdmyJNbbLDJIhvTk6eHc3HrWg4EDMgCXX89zTLQzj5XSKKLe7aZGDeFHmRA62PKM1GjFj9n-LBpZrnz7y-h-L9XSGNbUaG6s92TePddeHyAYrUMu4OUtoxx6wmvLRLbhFT0mIcT-W8SQ89_hGXRXO5Y2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.2 الان روی OpenRouter رایگانه
💥
🆓
هوش مصنوعی GLM 5.2 یک مدل Reasoning قدرتمند برای برنامه‌نویسی، AI Agent ها و اتوماسیون پیچیده‌ست. نسخه رایگانش در اینجا با 128k Context عرضه شده و از طریق مرورگر یا API سازگار با OpenAI در دسترسه.
✅
❗️
از مدل z-ai/glm-5.2:free استفاده کنید — بدون پسوند :free نسخه پولی اجرا می‌شه.
⚠️
محدودیت اکانت رایگان حدود ۵۰ درخواست در روزه
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-IXNxrDiaLV2vNxU73TC0Y4zSW1uPrXj0a24SxG8LbD4TYkfp
🔺
Base URL:
https://tabitoken.com/v1
🔺
Model ID: claude-opus-5
ری اکشن فراموش نشه
❤️
توی کامنتای پست چندتا کلید دیگه هم گذاشتم واستون
✅
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jqe2N88uxLmxHb_ZJ3uBJTdOWkU-HXM3yfeZKS5hvd8mQFzI5p4xgav_nFRSxfqC0d3zuo1yKhlfO2auqR1bJ2LyKPxP7CpSwPn1oh6YudX8Ss1qD9P-jrSUw6yfBmOH3gBMN1XTV0MNGHQ3AAodtT0itOqx2Qr7kvnDZkiJP_wjaVGMxyrfFGrqfy6Qtnl4pHsFeWUIkyQmH_71zfTW2MsY_X8JYSRXUD4Qw3qDqaBmojny9fgrx-8SKxPwAIGsXVD5suByCIkp-2gu3en77ksQRjb5FbmUneQasbIwYhzdpq7QH3JTmJq28mVAIixYH-BI4mXg58V089GL_2Zt0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 و Qwen 3.8 max به صورت رایگان
💥
🆓
این دو مدل در این سایت به مدت محدود به صورت کاملا رایگان و فقط از طریق API در دسترس هستن
✅
📌
Base URL :
https://api.tokenrouter.com/v1
📌
Model ID :
deepseek/deepseek-v4-pro-0813-free
|
qwen/qwen3.8-max-free
⭕️
محدودیت ایی در میزان استفاده وجود نداره اما به دلیل شلوغی بسیار زیاد سایت مدل ها کند هستن،  پس باید در تایم خلوت استفاده کرد
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=bozhEpuMax1PC-tao9f9nXFKmVF1_lyCO4_K-VjXDrC_ND92sPyaqOiAmnhqugi4VXH1pubaT_iDZsCbakMOSFMI9hqKG8Q_lEe9xNgkPXI4A0R90sYApu2uo-Tt9HTDkOQImjY_m1laOsHm31Cy0BrOhKsCJbQ_Gds_3mazue_mbX5MHlCP5w-zfjUgzPQEi5nlEqCYMQurqdzKHaCTlrgbmtIKnc6LjVcQOoX5c1RVtFhxDqF1m8TWLTVXsuGXvrgQnHchEivZOoKvYqQ1qzdCn4OoFYZbh6bzujPc88_hYtbq4mFAXzjB32B8vZp-OX8kxEb5TIwy5RiAC-zn8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=bozhEpuMax1PC-tao9f9nXFKmVF1_lyCO4_K-VjXDrC_ND92sPyaqOiAmnhqugi4VXH1pubaT_iDZsCbakMOSFMI9hqKG8Q_lEe9xNgkPXI4A0R90sYApu2uo-Tt9HTDkOQImjY_m1laOsHm31Cy0BrOhKsCJbQ_Gds_3mazue_mbX5MHlCP5w-zfjUgzPQEi5nlEqCYMQurqdzKHaCTlrgbmtIKnc6LjVcQOoX5c1RVtFhxDqF1m8TWLTVXsuGXvrgQnHchEivZOoKvYqQ1qzdCn4OoFYZbh6bzujPc88_hYtbq4mFAXzjB32B8vZp-OX8kxEb5TIwy5RiAC-zn8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎧
این اپ کنترل موزیک رو مستقیم به تسک‌بار ویندوز میاره
ما FluentFlyout رو پیدا کردیم — اپلیکیشن رایگان و متن‌بازی که پنل کنترل موزیک رو دقیقاً روی Taskbar ویندوز ۱۱ نصب می‌کنه. کاور آلبوم، Play/Pause، Seek، تعویض ترک، Repeat و Shuffle، همه یک کلیک اونورترن.
🎶
با Spotify کامل کار می‌کنه
💻
با Windows Media Player کامل کار می‌کنه
🖥
با مرورگرهای Chromium و Firefox هم کار می‌کنه (بدون Shuffle/Repeat)
🎬
با VLC هم کار می‌کنه (ممکنه Plugin لازم داشته باشه)
⌨️
با هر پلیری که از SMTC ویندوز پشتیبانی کنه سازگاره
سبک، حدود ۵۰ تا ۲۰۰ مگابایت RAM مصرف می‌کنه و عملاً مصرف CPU نداره.
✅
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA9q0BpxDt1-6jcGdsJNyuOt3guTzkgGwyXyubzpXxkMDdFLoeif3E7ermVOibhKDXtKeLju_yx1agEFAdfu0ml1atJ5zDEXCm9hwnUwOlZfFC4kcLPaV9CtUSXDCgIn-v6HkEl0SJo6ssZ6u46w7J55A9TVb6gZCGuV30I8iqb9HZPK3AsBga6TSePJdSNPSCeW5_bcPH_jhNt1kDytDyGCVRSuEcbLe9rm7QLrNWsdavrZ8hZaqiMqDPkr4VujKobdxph3M8xA0vxweQ0n7nj5Wtln8eFHeizDtnxDPgfd0BM7n4V1816T6A3Zufw-oScwujdsXpV7OzqB02Om-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
این ابزار خط‌فرمان، یوتیوب رو مستقیم توی ترمینال میاره
ما ytsurf رو پیدا کردیم — یک CLI رایگان و متن‌باز که ویدیوهای یوتیوب رو تمیز و بدون حواس‌پرتی مستقیم توی Terminal پخش می‌کنه.
✅
👥
قابلیت تماشای مشترک با Syncplay
🎶
پخش و دانلود فقط صدا (Audio-only)
📥
دانلود ویدیو یا صوت با یک دستور
📌
انتخاب تعاملی Format و Quality هنگام پخش یا دانلود
📃
تاریخچه پخش با امکان تماشای سریع مجدد
📂
تنظیم مسیر دلخواه برای دانلودها
🔄
بررسی خودکار آپدیت برای نصب‌های Manual
📺
پشتیبانی از Subscription کانال و Feed شخصی‌سازی‌شده
⚙️
نیاز به چند Dependency داره: yt-dlp، mpv، fzf، jq، curl، ffmpeg، chafa. روی Arch (AUR)، Homebrew و NixOS هم قابل نصبه.
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=mFw9j2QXBGP5qrWYflOAY6S_5tXM9O_76f0YgNEqxASiZXBM_zFypWSxUPdnitXsJaE8CX7Y0etFnG9q1JobzIjU9Pff60GpJ4Vqy7XceUPnOjYGiiHvnYs0LTuSZAoZpdyILJC6kZfUPPS00L30Ch2dHTFj929kGiBGqT0asXbA-I-PYl7w71Pi-tS25PDLa5Mjc1DgnKtpnx7sCFUcOqSGnCGVv0RLQfZwR_bJfUmjg8ynkdpTWu3c1RJntNKis8954mQxZHYMh9qvImOfaXpBatupWjA1-mV5h9Zj6HQkzK0-SwZ6fVYdrWNOCv5xOKmQmeIuYAVcVajpCqzTBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=mFw9j2QXBGP5qrWYflOAY6S_5tXM9O_76f0YgNEqxASiZXBM_zFypWSxUPdnitXsJaE8CX7Y0etFnG9q1JobzIjU9Pff60GpJ4Vqy7XceUPnOjYGiiHvnYs0LTuSZAoZpdyILJC6kZfUPPS00L30Ch2dHTFj929kGiBGqT0asXbA-I-PYl7w71Pi-tS25PDLa5Mjc1DgnKtpnx7sCFUcOqSGnCGVv0RLQfZwR_bJfUmjg8ynkdpTWu3c1RJntNKis8954mQxZHYMh9qvImOfaXpBatupWjA1-mV5h9Zj6HQkzK0-SwZ6fVYdrWNOCv5xOKmQmeIuYAVcVajpCqzTBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پرامپت هر ریپازیتوری رو به یک نقشه سه‌بعدی تعاملی تبدیل می‌کنه
🚀
بده به Claude تا یک شمای ایزومتریک از پروژ با Dependency ها، مسیر داده‌ها، و توضیحات کامل بگیری
💥
📐
معماری رو مثل یک شهر سه‌بعدی روی Grid می‌سازه
🏢
هر بخش از Infrastructure = یک ساختمان با شکل متفاوت
↔
مسیر Control و Data رو دقیق دنبال می‌کنه
📄
به فایل‌های واقعی Reference می‌ده
✍️
پرامپت:
Analyze [لینک ریپو] at latest main. Create an isometric system map with legend and explainer panel. Show infrastructure as varied 3D buildings on a grid, with dependencies and payloads tracing real control/data paths. Cite files.
✈️
@ArchiveTell
|
#PROMPT</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_J8PMSyWbsEbKKzrWfSXyO7cEoSlcBL3-yI0AttPMaDbLenog8TDIqP8R5yjAZz59zh5QMybxDjLPCmvJhhx2oLcM6J6v0hjq-m0dXRmpCLOV0-H-f5AsmsDOOU1H7s_PR7CVJ5xQjL78DrEbaDr4JY1UTqTo5DiSbVlXwWMFvmFNaBDTtxBjO3e2zfg1BGGN1FYkxcVAUGZAMah2n9LijlIE81tiqtH-drn6cNfLAfPlAgH1-l7ScEqj1UlzMD0pFJ7Ln7Pc1FhuoTKfaeLwL1CU47SFuO2bqu0rPQcLRETViJkOZfFxyCT-Vg01-69KNgCVO4BRtbTgCWnPWJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧹
این ابزار متن‌باز، ردپای AI رو از فایل‌های شما پاک می‌کنه
ما watermarks-remover رو پیدا کردیم — یک Agent Skill به‌همراه یک سرویس رایگان که Watermark و اطلاعات پنهان تولیدشده توسط مدل‌های AI رو از فایل‌های مختلف حذف می‌کنه.
✅
📄
ده‌ها فرمت رو پوشش می‌ده:
PNG، JPEG، SVG، PDF، DOCX، ODT، HTML، Markdown
🔡
کاراکترهای مخفی Unicode و ردپای متنی AI رو پاک می‌کنه
🖼
متادیتای C2PA/EXIF/XMP رو از فایل‌ها می‌زداید
⚙️
کاملاً متن‌باز و رایگان، با پشتیبانی از Claude، Gemini/SynthID، OpenAI و مدل‌های Open-Source
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l90P1-8JKEJ7APFIyn6zs6n1r6E_8nv2hBuPSPUNLPZFvc3Po1scuLcrsZ7IlSzmJp1NeH33W5F3OVR-aYCjCrUWTQgkwQAnVXs4HPf7b6OcgwLFM8dgh-LKdGQxSyO01sxZy-NTNRHtvaZDaR6PFu04cVOW5OsvxuhCNgsDMvY6qsRP6ChCl6oMskq0YmmGdyj4mS6E58hzY3CoRJ7aiVNsI-xYkdH3-ZsfBIY2jw088m6G8i0jodsyuXhTifpzeWVWdJ-T4HqDGYQ1CUrIcVY_eKIMV7uiTJEsaDlGCs_aNyKFtJDKEby_e8VSzTU5YYe5OeLum6NknkESZnUMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Grok 4.6 | Kimi k3 | Qwen 3.8 Max | Deepseek V4 Flash | GPT image 2 | Seedance 2.5
✅
این سایت بهتون 5 دلار به مدت 7 روز میده تا بتونید از این مدل ها استفاده کنید
💵
یکی از بزرگترین فرق های این سایت اینه که مصرف مدل ها به شدت پایینه و کریدیت خیلی کمی رو کم میکنه
✅
📌
Base URL :
https://heyroute.ai/v1
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=GMMrScOQhdy1vWMUjTHFGDz1CP8Hp-tb92BTDl1MjBS1t2uLVTFlc0iBhyDItr-RFmYPZI5w48wHaSv1ivTPKFlxm0_CdzuVFSR13SgR1PbK2WBzCvm4LH5HUNlip5eWmrBlwHAeLYBe2VwskzgBXG5Vi8_lkwGAJj_Zkn14rauPtW4SDaeNQl5LYyFTqzrvbJmWwc8Sf2vWJLJij0QefQxxbofYkRQ5tvXWGpVjxHSdm2G0xsFj3GhM0COe-hVbcoKSo3hDg8DqciZhVsXdfA1lvfUXekNvsKmUx7wVagEyb3ADQiS-Ze9owI9UFoA17zztGcq-E5Z5kTpglJewrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=GMMrScOQhdy1vWMUjTHFGDz1CP8Hp-tb92BTDl1MjBS1t2uLVTFlc0iBhyDItr-RFmYPZI5w48wHaSv1ivTPKFlxm0_CdzuVFSR13SgR1PbK2WBzCvm4LH5HUNlip5eWmrBlwHAeLYBe2VwskzgBXG5Vi8_lkwGAJj_Zkn14rauPtW4SDaeNQl5LYyFTqzrvbJmWwc8Sf2vWJLJij0QefQxxbofYkRQ5tvXWGpVjxHSdm2G0xsFj3GhM0COe-hVbcoKSo3hDg8DqciZhVsXdfA1lvfUXekNvsKmUx7wVagEyb3ADQiS-Ze9owI9UFoA17zztGcq-E5Z5kTpglJewrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پرامپت، کل معماری پروژه‌ت رو نقشه‌برداری می‌کنه
🚀
پرامپت رو بده به Claude، بذار کل Repository رو بخونه، دو تا خروجی حرفه‌ای تحویل بگیر:
⚡
کل کدبیس رو تحلیل می‌کنه
🔗
ارتباط بین فایل‌ها و کامپوننت‌ها رو کشف می‌کنه
🗺
معماری رو به‌صورت دیاگرام تعاملی می‌سازه
🧭
مسیر کامل هر Flow رو ترسیم می‌کنه
💬
برای هر Component یک Tooltip توضیحی می‌سازه
📤
خروجی:
🖥
فایل HTML مستقل
دیاگرام تعاملی با Node و Connection، پنل Flow کنار صفحه، کلیک روی هر Flow → Highlight مسیر کامل، طراحی تمیز و Responsive
🧬
فایل JSON برای AI Agent ها
ساختار: { nodes, edges, flows: [{ steps }] }
مخصوص Agent هایی که باید معماری پروژه رو بفهمن
✍️
پرامپت:
Analyze my entire code repository thoroughly.
Generate TWO ready-to-use deliverables:
1. A single self-contained HTML file containing:
• An interactive architecture diagram (nodes + connections)
• A flow panel on the right
• When a flow is clicked, highlight the complete path
• Tooltips for each component
• A clean, professional, and responsive design
2. A JSON with the structure:
"{nodes, edges, flows: [{steps}]}"
The JSON should be specifically designed for AI agents to understand and navigate the project architecture.
✈️
@ArchiveTell
|
#PROMPT</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVKhdw9gJsaRkM9FZGYDQpLLWgmmhtKqSNGL4ZI0wddOI9sXUNrVZf3VBebGhf7Vr0r6CBdM1RHTFUOHBYmE5pvf5xfO0RmmvqO20iA8eFPUDE8X9_ON6hnhorODfaF4Joh97sBu349Laicd8ePkkoqmPjetZKml-jhjh_vlQ2y7foxVM4hewSrZy-N1aIQO900ByLb31gUdiaEuuxdweUoOigi4PGasSWuBdU9SNDVS5bdBtR727G5wNbxk-eiwuVm71xm9h6K1_fPg-lRJRjMHMpTNO5SFMZ8q1uSOF875CCshbV53c8MtiKBUE1nwCahpgnmqNBeX7_5H_FTEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی رو به یک ایجنت هوش مصنوعی تبدیل کنید!
🚀
دیپ‌سیک با معرفی DeepSeek Harness یک محیط جدید برای ساخت و اجرای AI Agent ها راه‌اندازی کرده؛ پروژه‌ای که خیلی سریع مورد توجه جامعه اوپن‌سورس قرار گرفته.
🔥
💡
ایده اصلی Harness چیه؟
تقریباً هر چیزی می‌تونه به‌عنوان یک Plugin وارد سیستم بشه؛ از مدل‌های هوش مصنوعی و Sessionها گرفته تا Skillها، Sandboxها، چرخه‌های اجرای Agent و حتی رابط کاربری.
⚙️
معماری Harness بر پایه‌ی Cordis طراحی شده و این امکان رو می‌ده که کامپوننت‌های مختلف حتی در زمان اجرای Agent هم تغییر کنن.
💥
چیزی که Harness رو جذاب کرده اینه که محدود به یک مدل یا ساختار خاص نیست؛ می‌تونید اجزای مختلف رو با هم ترکیب کنید و Agent موردنیازتون رو بسازید.
🧩
حتی جامعه‌ی توسعه‌دهندگان هم دست به کار شده و هزاران Skill آماده برای Harness ساخته شده که می‌تونید ازشون استفاده کنید.
📌
خلاصه اینکه DeepSeek داره یک رویکرد متفاوت برای ساخت AI Agentهای ماژولار و قابل توسعه ارائه می‌ده؛ چیزی که می‌تونه برای دنیای کدنویسی و Agentها خیلی مهم باشه.
🔗
لینک گیتهاب پروژه
🔗
لینک سایت پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joDIptuxXajseujUgz1ZqjUpXoW7nIU0stjcVXTvbHAZCGTILyeS-eONGwBzH-uUmJZVwgJGl0DTG8df0PMOGZEOaW-If8GS9R4pNsoS4CnPW2kgfQpxvDMypcPtkwv1MSOVGXszXjD7EnKlPVduZVA2bavefB2ZX1YyAPptNvNXF_fgd0JxEQAO78nOdBDuxgu6QILBkBe6OYg5N6nARIjwkbx0GKeH0Nip6-fx6YVoSIV-r4oo7ltH_m8Tc5DnGdG0dS5Hjkl9NsYpSXD8v20HLVMX2OdZPARkS1Siib7UavxpKJBfePB3-2jYwpVWeVLee9glqIbc2qwPm5MAQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست طلایی سرویس‌های رایگان برای برنامه‌نویس‌ها
🖥
سایت
free-for.dev
یه لیست
کامل و مرتب
از سرویس‌های
ابری
و
ابزارهایی‌ست
که پلن
رایگان
واقعی دارن (
نه فقط تریال چندروزه
)
🆓
از
دامنه
و
هاست رایگان
گرفته تا
دیتابیس
،
CI/CD
،
مانیتورینگ
،
ایمیل
،
ذخیره‌سازی
و
خیلی چیزای
دیگه
🔸
اگه دنبال
ابزار رایگان
برای
پروژه شخصی
یا
استارتاپت
می‌گردی، حتماً یه سر بهش بزن
💻
⭐️
Link
⭐️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=UJ2FVUuZ0_-Pj8G8D0y2XL3F2P4fS4FXtngqVGj3yjNUFWQChYg3h6_0w_HuH2hzYglxjWItpXSHVOclK7ZAgzRyuaUoK4KIqmDoxmS-wvU2aRZdL1NI4CE7oYmDtt3a5IU09YdH1oxEeMOpsXYzxha5MOQaLDCgf3WHLe4BPqzZa58eoueHogKzrSaKrlBto6azul_yZVRpFg8UZ2RgDcOLdNUlIO9Pu2zxLZMPV4Bb76UJlDNNYjwwa6qaD8g0KWyb3W-qIQpgckDQbWFUo-SuZUCjnQ0AmzqlBG0COuFXJWCsGBYSAB5FOIvvimBMEPDanU0ljL_nn5gjFwnTIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=UJ2FVUuZ0_-Pj8G8D0y2XL3F2P4fS4FXtngqVGj3yjNUFWQChYg3h6_0w_HuH2hzYglxjWItpXSHVOclK7ZAgzRyuaUoK4KIqmDoxmS-wvU2aRZdL1NI4CE7oYmDtt3a5IU09YdH1oxEeMOpsXYzxha5MOQaLDCgf3WHLe4BPqzZa58eoueHogKzrSaKrlBto6azul_yZVRpFg8UZ2RgDcOLdNUlIO9Pu2zxLZMPV4Bb76UJlDNNYjwwa6qaD8g0KWyb3W-qIQpgckDQbWFUo-SuZUCjnQ0AmzqlBG0COuFXJWCsGBYSAB5FOIvvimBMEPDanU0ljL_nn5gjFwnTIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📝
♊️
گوگل هر ریپازیتوری رو به مستندات تعاملی تبدیل می‌کنه
گوگل ابزار جدیدی به نام CodeWiki معرفی کرده که با بررسی خودکار کدبیس، در چند دقیقه یک مستندات کامل و قابل‌فهم از پروژه می‌سازه.
🚀
🔺
ساخت خودکار دیاگرام و نقشه پروژه
🔺
توضیح بخش‌های مختلف کد و نحوه عملکردشون
🔺
تولید راهنما و آموزش مرحله‌به‌مرحله
🔺
تحلیل معماری و ارتباط بین وابستگی‌ها
🔺
ساخت یک چت‌بات آشنا با کل ریپازیتوری برای پاسخ به سوالات مربوط به کد
یعنی به‌جای ساعت‌ها گشتن بین فایل‌ها و کدها، می‌تونی پروژه رو خیلی سریع‌تر درک کنی.
👀
📌
این ابزار رو از دست نده!
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGUrWx9hhHdm5THIpBl6p46ekJmqCZmRwW2ysGwAFE_0rzRNE0jPr7Q6OjOC2xfZv3EafXA2xMpHHHbtogcRr4_zEMqpCsyVJ6n22mTqkF27oF_bW1arktkGDGYn67pn_4jP3PrjwFm4el5YRNuiilE-tBJ6AcqY6R_5qz1W6crXf0EiA3JVLvoh2DjTrWss_ZJnrLz1Kn9YMTSjwU3xxW2QU799SP3-d2ZJnV0Ia_KCgFl2pDja4O6DquA9DpwYNYGrTjjLoh2t7tKJ_bIbgoKzGMMcDhhFMisXPID09q1O_UXg_ucZ-URjPkMwQUqT4dr3LnyhLts2DPQogJENVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">TorrentSearch
♻️
اپلیکیشن متن‌باز اندروید برای جستجوی همزمان تورنت از چندین منبع
📱
با
TorrentSearch
می‌تونی
خیلی سریع
از کلی
سایت
و
پرووایدر
مختلف جستجو کنی، نتایج رو فیلتر و مرتب کنی و مستقیم مگنت لینک یا فایل تورنت رو بگیری
⏬
امکانات اصلی
💭
جستجوی همزمان از چندین
پرووایدر
(قابل روشن/خاموش کردن جداگانه)
🎁
فیلتر بر اساس
دسته‌بندی
(فیلم، سریال، انیمه، بازی، کتاب و ...)
📁
نمایش تدریجی
نتایج
+
مرتب‌سازی
بر اساس سیدر، سایز، تاریخ و ...
🪣
جزئیات کامل هر
تورنت
+ صفحه جزئیات داخل خود
اپ
ℹ️
ذخیره
بوک‌مارک
+ خروجی/ورودی گرفتن
🔖
حالت
Safe Mode
برای مخفی کردن محتوای
NSFW
🔞
پشتیبانی از
Jackett
/
Prowlarr
(
Torznab
)
🦾
طراحی مدرن
Material 3
و
دارک مود
🎨
⬇️
دانلود از گیت‌هاب یا F-Droid / IzzyOnDroid
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚡
پرامپت‌نویسی تغییر کرده؛ این ترفندهای قدیمی رو دور بریزید
بزرگ‌ترین دلیل جواب‌های پرت و توهمات هوش مصنوعی فقط یک چیزه:
وقتی جزئیات بهش ندید، جاهای خالی رو با حدس و گمان پر می‌کنه.
❌
ترفندهایی که دیگه منسوخ شدن:
•
نقش‌دادن‌های کلیشه‌ای:
نوشتن جملاتی مثل «تو یک متخصص ارشد با ۲۰ سال سابقه‌ای...» تاثیری در دقت نداره. مدل به فکت و داده نیاز داره، نه عنوان شغلی تخیلی.
•
تکیه به
Temperature = 0
:
صفر کردن دما جلوی اشتباه رو نمی‌گیره؛ فقط باعث می‌شه مدل خطایش رو با لحنی کاملاً جدی و بدون تغییر تکرار کنه.
•
پرامپت‌های ۳ صفحه‌ای برای تسک‌های عادی:
طومار نوشتن برای کارهای ساده، تمرکز مدل رو به‌هم می‌ریزه و احتمال نادیده گرفتن دستور اصلی رو بالا می‌بره.
✅
فرمول ۴ مرحله‌ای برای گرفتن بهترین خروجی:
۱. هدف دقیق (نه کلی‌گویی)
❌
نگو:
«این قرارداد رو بررسی کن.»
✅
بگو:
«این پیش‌نویس رو بخون و فقط بندهایی که بار مالی اضافه برای خریدار ایجاد می‌کنن رو پیدا کن.»
۲. بافتار و مخاطب (Context)
«مخاطب فردی بدون دانش حقوقیه؛ توضیحات رو کاملاً روان، ساده و بدون اصطلاحات پیچیده بنویس.»
۳. بستن راه حدس و توهم (خیلی مهم)
«اگر پاسخ یا عددی توی متن نیست، به هیچ وجه حدس نزن و صراحتاً بنویس: "اطلاعات در متن موجود نیست".»
۴. قالب مشخص برای خروجی
«پاسخ نهایی رو فقط در قالب یک جدول ۳ ستونه بده: [شماره بند | ریسک موجود | متن پیشنهادی جایگزین].»
💡
اصل ماجرا:
هوش مصنوعی ذهن‌خوان نیست. هرچقدر دامنه حدس‌زدن مدل رو محدودتر کنید، خروجی دقیق‌تر و کاربردی‌تری تحویل می‌گیرید.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6f_U9OFR9EeWY6F_fuyhi7syDAO_13Sbzja6F6wNEouwIPubuRARruxZO1jMH_AUwnu03s_iu-4EbNQTFW-oAr1jrJzEDiFWMxJBiUc4lPuXUGe8vAKwLim-GZ3fUx3uX-Z03PZya17hB9OuJOy9CzzI8aS_AxjZUKCXswgOGHlJE0pEryjJJ7w_5wi2Uhv_YABKxg-RT8RXfIh-RK_oWqqKLIn-nQcMHPWq-vxv4o6mCHo0RBz_ITD4gApweReBEH5MuFrJXtuzxJtaAJhIxkBAtKajrH0kImLWQ3yUzq2WUSZNS6epiNV39PQhnmbN5dy1TP-7JLp7iaUd74S4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی به صورت کاملا رایگان
💥
🆓
Sonnet 5 | GPT 5.6 Terra | Agnes 2.5 | Mimo 2.5 | Gpt image 2 | Nano banana 2
✅
📌
Base URL :
https://ai.furry.vg/v1
حتما در بخش انتخاب گروه ، گروه Free رو انتخاب کنید
‼️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esjihELC_HtZNftJ2lvToorYt2JfGLg1kwQArQYCr7tB4WTVP8zvAg9SBo8vSH_nwZ1prJtLpDKhSTX3iubqC3dgOER3kc6yPB2tkZHCZyA6HrRB9BHLVL7XV6CerwuhJ3o3KrZzikx9nxrruoogN6pdBpd857v5SuggFcrTG6rGnLq4XXTu0g5xk3FMK-iJ9dz6P3GqUBBv27B2liaIDmdgZv_dGUT-zcd6cd1bvDTwyXk9H42eyu7UVfraI7rPnkbIs1iIBwWp8hWSpqj7mqtC-2Fy3cucwU_RC6ExpJzVCN-Ua0qp24HdcN_xAabcH2hmudjEO-bYOrHeeS7teg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل Qwen 3.8
💥
🆓
با سایت Runinfra تا 48 ساعت آینده میتونید به API مدل Qwen 3.8 دسترسی رایگان داشته باشید
✅
📌
Base URL :
https://api.runinfra.ai/v1
📌
Model ID :
qwen3-8-27b
به دلیل شلوغی سایت ممکن است پاسخ مدل کند باشد
‼️
🔗
لینک دریافت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NipAw4thR4gpzuNazjD02MhF0RCmkLIOW_Ns9xf_MRgEK2JrP0gAcFYRfoc0z4P-a6AQ0vEvs85n8U_VT_i-HKsJb27cQ75r35AMcWJFYV_bi4WBivx4sUu3P2mpgBwu8RjK5P5h4aFhJfDonXzFJW8L-A7fkJf1lTbVF0xrTXV2dNRiFBI3z8nHkfnmn-H2C1OUt-16dLsFPYg_Mp4nkrbYQbyzaGUKKqQFXC7KRI8XmkYjIfOPG7dhuvHqJkLEjmHQ4zM12nbrswdBB2bdq8C1LHyqQwTMWEUtWAkKeivo_ZOhQ939_ZfIZcjS2_B1Yrx0I_t59yrSWqPvo4rS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی محبوب
💥
🆓
Qwen 3.8 max | Deepseek V4 Flash | Deepseek V4 Pro
✅
📌
Base URL :
https://api.orcarouter.ai/v1
🔗
لینک ثبت نام
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjDmJ6cg4UG71hAbf0o7BwnGtq8xloO6kaeXu1dsBc3wFakVU4ACswqFy9Z4FZCi2TTPRTRekSFY-bri817RWnc9hg8rFSjUQsla3kS0pjv85RdGka0FuDGA6FRLUk5PO872wqDWYdVq0zguy5-GK404N38JqX9qAh6tjPt4kp1L4I7XggSv3BF1QDijTN4fn1eg199y-hbLUeAypQqP1IJ9x0bFYHKwGWd84abLjoK_a4jvsF6_86JkrpD0qRDKvCCG6S4Zb2XJFc6My9HEmGsFkfv5ppGAtNwIM0Yc_dNOgXFwglYQ6qA3AobBCUN_d1jZF0LPjF8mwkgb1wSx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت
z.ai
بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
100 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-bY9B0parF18s5v1wasRyzRZsVLzICaSVfZNVEMrqG2Rlt7dH
🔺
Base URL:
https://ai.venlacy.com/v1
🔺
Model ID:
glm-5.2
به دلیل شلوغی ممکن است پاسخ ها کمی کند باشه
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKQBnzc9z3NY3A7T1F-t2XB2Lb5JAu0H05m2lgvPl5KUqXdkEWT1srtKLZNQhjs38j2Kt0mzVO7Ydi6fY5gqeJo4pTtKCHh9g0-3ZYm2hE5JvxyNeRT9HLxSdxbRiVaASJA8UigrDR0FhUcIt3pCXW8YGII_zvuYxQzsLAt-Jcg2CKaxtL6Sv7t970Yl10cQPAYwIsDSMO6WbSZJdotco_ku0NOO5rR-8ugtRbL2CY92zo-pOmSwfpQhV2pW6iZAgZTEI1XiK_rbqPyWdVgQESSPQDndnj-Kt345_WJCpkCtMB0GtsKGditIq6a2Gnvh6HYOSRTkEYwBDyJsIE8Hqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 رونمایی شد
🚀
نسخه جدید GLM با نتایج بسیار قدرتمند در بنچمارک‌ها عرضه شده و در چندین بخش از رقبا جلو زده است.
🔥
در مقایسه با مدل‌هایی مثل Kimi K3، DeepSeek V4 Pro، Qwen 3.8 Max، Opus 4.8 و GPT-5.6 Sol، GLM-5.3 در بخش‌های زیادی عملکرد بسیار رقابتی و حتی برتری دارد.
⚡️
🔗
دیدن اطلاعات بیشتر
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/up1sNjNL7NIkt8MLqkaMMKXn2Wq-BJhxDAqpRczhnFti4nlcfR0391I1gK0-RVaY6peTHotOikqspPoB7B4I6_44dpNNuJuW2IbSW6yFL3kVtPVMMgqVid2C4Ym7icFhFpfvsgGEv0s73iSsOqTgjXlUrXatfVyLjyCJQPN4-BELSHebZdQxWo6gwTELRMPCcJ_ibEMI4uXEoPBs-87d-LMNALEWL8uueZr5-Kjk4hntXRyBakgc3ttScZuLwUIFFti-JLtHJxwOksP-xMkoIuNiy9hw9VF1bTJOgO3dDeADjFMzl5SoiggcxS4RJ0_AU2VXxyIdkxuZIUSskhWwHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc4dv02ba1GWRYJNCfFhiuw6FaOu_gaRXOxmsMwb0BCGDSsotMCXXdN4NAkbqD3_W1TEYTbZQYwsWgZcVOttiykDSEtmVUIe6WIfgwnDN-5DM-tMqvj-DmGjRXi_Md0k8PWc_BdFzactBWN66eDoxiOBHhBtOzAzpL7OMCztVfQ99qi9r_5j3h9uA0oN7fFWD8LDeBMVSszF17dN6Jb2HgjpIjD86fHdwtPJhy8znsUuB1UDeTSDLEGNFoM17SYX7p-eEJfq75GFyLpoQ2ggE6lGZ9aMAnrJC2xZnABm94wRAYFPsieJ2Ja8Y2Yls1QgwxKjGD6bd5bnNCfNooFUbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ تست رایگان مدل ‌Seedance 2.5
⁩
💥
🆓
‏اگر دوست داری ویدیوهای سینماییِ ۱۰ ثانیه‌ای با کیفیت ‌480p⁩ بسازی، پلتفرم ‌JXP⁩ این امکان رو به صورت یک‌بار مصرف برای هر حساب کاربری گذاشته.
🎬
✨
‏مراحل ساخت:
‏‌
1️⃣
وارد سایت
jxp.com
شو و ثبت‌نام کن.
‏‌
2️⃣
به این
بخش
برو
.
‏‌
3️⃣
متن یا تصویر دلخواهت رو وارد کن.
‏‌
4️⃣
دکمهٔ Generate Video رو بزن.
‏برای این تست اصلاً نیازی به کارت بانکی نداری و کاملاً رایگانه.
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پرامپت تولید شعر بی نقص پارسی!
از پرامپت زیر استفاده کنین تا ai براتون شعر هایی در حد شعر های حافظ و سعدی بسرایه:
تو یک استاد مسلّم عروض و ادبیات فارسی هستی. در سرودن شعر، اولویت مطلق با صحتِ
دقیق وزن عروضی است. پیش از نوشتن هر بیت، آن را در ذهن تقطیع کن تا مطمئن شوی
واژه‌ها (حتی کلمات غیرفارسی) دقیقاً و ریاضی‌وار در جایگاه درستِ وزنی
نشسته‌اند. خروجی نهایی نباید حتی یک مورد سکته، لکنت یا ایراد وزنی داشته باشد و
باید کاملاً روان و موسیقایی باشد. حالا یک شعر شاهکار کوتاه و روان درباره مناظره یک قناری و دایناسور بنویس
.
﻿
تست کنین، به همراه مدل ai استفاده شده شعرهاتونو کامنت کنین، بهترین شعرو که لایک بیشتری بگیره بش جایزه میدیم
🎉
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvAJOSXP2GKzUYnnSjhNKx8U_qKuupZjv1Beemhp6iy-A6mkV4AuOO1s7BynrTxweMx385GkENixHlNAeEX6-79wAbFSvS8zsSdi1_A2IJ8yTfcdKcdTZ3bUO217CgkLfDqmd_A1XyoZ3mQ3r-_StOtbkOQpBeFQWHGLDSlBagJJukFQUTBspyug5HQsCTIlhxe8H1OHTeaxzHyEgXPKRfAOFN2v2mHfRYJIQeyxkZndTdsQnPlcsO3CBeNmtIaPOXUPkBbrdwbKMyyzWKVWDUUazxAZfj88WMyRSN-jXgaDmMMVeJEZL-rtlp7v3iHZr-WY-BZYkzy_H3YGBprGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
CiteSeerX گنج رایگان مقاله‌ها
یک موتور جست‌وجوی تخصصی برای مقالات کامپیوتر و علوم اطلاعات که فقط به جست‌وجو محدود نمی‌شه.
👀
🔺
میلیون‌ها مقاله + جست‌وجوی متن کامل
🔺
پیدا کردن منابع و مقالات مرتبط از طریق شبکه استنادها
🔺
اطلاعات نویسندگان و تحلیل تأثیرگذاری
🔺
کاملاً رایگان، بدون ثبت‌نام و با دانلود مستقیم PDF
🎯
برای پیدا کردن سریع منابع علمی خیلی کاربردیه.
🔗
ورود به CiteSeerX
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">20 دلار برای دسترسی به مدل‌های هوش مصنوعی GPT مانند
:
💥
🆓
GPT 5.6 Sol | GPT 5.6 Luna | GPT image 2
✅
وارد سایت شده و ثبت نام کنید سپس یک کادر میاد برای جوین شدن در چنل و غیره ، کافیه فقط روی دکمه ها کلیک کنید و پس از ورود به صفحه بک بزنید صفحه قبل ، سپس روی Claim کلیک کن
✅
Base url:
https://apimaster.ai/v1
قابل استفاده در
Vega Agent
✅
🔗
لینک ثبت‌نام در سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptpj1c1OoMlCLyYthg8X8VIFwJ-zSQK3jn0sdcvzNpW6RheeXGXZq6EHKnnCn3ShAlvWZltmSi2f5wwcduIJtL27n1XwC_ng8ud0VbsP4w68y39Agh_0KTkW6k1Q1Z0BctfCb7Wu0ISRLg-TULazLTdYTLZ2O6tiOmjxapimKlLOAl3mwcOc_aO8X9SXZAFGtbshXPiLpsiG0uk7fFODdZh9b4U1VXIfmgPbSiWxs3ACF6IQMx1Nf4F1sxwqgWh6FHUW7FmZKk9eqGU2_VDIlsL0qpU75Qbms8vGd9tVr1WSesEFg_usukUCKVhVsTob8_jlj0Sk2oGsLVJsDBg-ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 وارد رقابت شد
💥
مدل جدید DeepSeek با قدرتی در سطح Kimi K3، GLM 5.2، GPT 5.6 Sol و Fable 5 معرفی شد.
🚀
🔺
سه سطح Thinking: کم، زیاد و حداکثری
🔺
عملکرد بهتر در تحلیل و برنامه‌نویسی
🔺
اجرای خودکار وظایف و ساخت گزارش
🔺
پشتیبانی Native از OpenAI Responses API
🔺
اتصال یک‌کلیکی به Codex
🔗
تستش کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvDRPj1fQBTom7ZvQS-DhVwduuoFK9eVrw5AQkduFeS35Ayw6hkl9IM4SXaiQNQYoO3cqQNDvfZTjWnD5XFduTS4RBSksgHgPkmsgy6z6H1Qfp5zhwYJKJlT6yGcpGYm6-fyiYJ6igvmwLHwyviYXjZUE7azTW2mS5J1Qka9qNJUUPDDfsotbvrLxYrZ50FNEzvDxzx6aHa79bAfN5NxTJHWFsstcSnppgioO8oaDZ3zKiWN5eS0gd3LSrQXgS69R9OpEuVJvHPhiMylRGJvgvuVlIUoa0zS643LHmB8uo_FTD6iVP8n8sDe4-YEs8glAC4gePRjvrtp3Xdwcigt8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش مصنوعی محبوب
💥
🆓
با این سایت
روزانه
300 کریدیت رایگان دریافت کنید و از مدل های هوش منصوعی زیر برای کدنویسی بهرمند بشید
✅
Sonnet 5 | GPT 5.6 Terra | GPT 5.6 Luna |Gemini 3.6 flash | Gemini 3.1 pro | Haiku 4.5
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SE6vjOQEq1ql96NZth51Ktsb5jrjkSRvPj5i4L5wjQpGHkyzJChmzj2yKx19iI0F6iQbM3VAagE0ymx0eznwerwtk8bEofhtx68iR2xnePo2c8SuyzJRIFutFfBwyZD_bQluQTsbA6HMn_uioMIfdkjlIaynGj0VYYdEbWCOf-VkVAnTz7Cc5jeNAlWw9OvNcnxK_3r1jyRbFav_gYNvdlN2r7XJO71wvlHxXfY47lW_FSYLEKMyHDrRMkZyHMq6Snz7OT7oJHuJUYmh7UujnQ44xQh867kE2-jT5SRpUwqYIMaZEdHRFc9wDwTNRB8aauouN7VQ3aQqKd28I5uNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کریپتو‌مارک مخفی Claude حذف شد!
🥸
هوش مصنوعی Claude روی متن‌های تولیدی خودش یک نشان نامرئی می‌ذاره؛ چیزی که با چشم دیده نمی‌شه، اما در الگوی انتخاب کلمات پنهانه و می‌تونه برای تشخیص متن Claude استفاده بشه.
🧑‍💻
حالا چند کدنویس ابزاری ساختن که این الگوهای مخفی رو در متن تغییر می‌ده.
📥
فقط متن رو وارد می‌کنی و نسخه‌ی جدیدش رو تحویل می‌گیری.
🔗
استفاده از ابزار
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMyF6kG-Lax8RttOdMzNtbj8lorhWDi5YYE-dKI_wYmvxg0bwG3DHU9fKAeQ7bQoF1SarRuGyQOAVmTIA6Sw8-zCCfjMZd_0KrhvSOfYlbPnvbgr6o5smcZpnxLbTnhoROkdWPv4ChgctsgM5Z_Kix4a2R7Kzs1N7skPn5eFzrqrcffpAOq4-Z1QtPCnzROUf2tXxHBJgDXm8bMIwmnLpdFVED8EdYVlnqtWb3kLXrjy9xi2zxAJpkp0a4-bToOovz2A-3e_ZBZdgj_liCGeLw7qKY0dGDV8_d-ibMCx5qYDFvpEylXpNJkOzpOODbHaA33DbDR6vGtDcLQZvq-_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnxYakx8iXX940N5778CTT7bIXEsbl4TGruLwOrWchPAvGPSvhgS3Y9f_U0z9qRB_DrVOUi-plY5cobDcKe6xiY7wl5aDSemPSyA9-67vmm5ax8ydgT4XFFM57QMzW5X683uouYtSKMT9v2aKEdH5qeOeGiBCJ6Dx66PteFK9tpPZ9Mag0u_TxggcWqJ-rizNb9HHSqaicXXNPoxq8HIGeg_lpHGqjGF6mN_ZVbtZOUQlbOw50r-YM4btm9QwX6UfRo-cWctgpOyeLOQZ1MAu5vyTKjnrmMf9a8NuGlxHop9q78GJ4qrKkI3IJ8E8JpX9YI1cgjnhrOy67i-f4XlXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد
قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود
۱.۵ تریلیون پارامتر
داره و قراره در آموزش
SFT و RL
پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:
چند هفته بعد،
Grok 4.7
با حدود
۲.۱ تریلیون پارامتر
میاد؛ قوی‌تر و بهینه‌تر، ولی کمی کندتر.
✨
👀
باید دید xAI این بار چه چیزی رو رو می‌کنه!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🎙
LivDub | ترجمه و دوبله زنده با هوش مصنوعی
با
LivDub
می‌تونی ویدیوهای خارجی رو
هم‌زمان ترجمه و دوبله
کنی؛ بدون اینکه مدام به زیرنویس نگاه کنی
🤯
✨
قابلیت‌ها:
🔺
ترجمه و دوبله لحظه‌ای ویدیوها
🔺
استفاده از
Gemini Live
برای ترجمه صوتی
🔺
پشتیبانی از
۷۸+ زبان
🔺
مناسب یوتیوب، دوره‌ها، مصاحبه و لایو
🔺
پشتیبانی از مرورگرهای Chromium روی اندروید
⚙️
روش استفاده:
مرورگر سازگار رو نصب کن → افزونه LivDub رو نصب کن → Gemini API Key رو وارد کن → ویدیوی خارجی رو پخش کن
🎧
🖥
مرورگرهای پیشنهادی اندروید:
Cromite • Helium • Ultimatum • Quetta • Yandex
🔗
افزونه کروم
🔗
سایت LivDub
🔗
گرفتن کلید جمنای
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXQopClUSlKk9i9qsV3aHC5QLp0t-AhZjyr4m0rTqdj5JnV5m72KpDo5dQv9I6fBO6pMA6TogRNnUdcp3XxpkkSDTifOtrtSv_uaqQoQT7ZXTHiaJQF2S49y7BtA7_td-Q9LLW1HMgE52_Hhxp0NHSxk-moJeWRlPLZlepzos44iIfSsHE8BdAePiUdzI1EpGhFTUxFo_mnzoro6WdeQHsS0kRXPZ0keEiWnNEimak6zOnvKRBUU12A-JGgDScNOXgJ-29vz_mli2L-QH06u1ZrMWUeK8STR3lYbYKpsGwWEl-gep3xzLlHVN4OOVfMzD2d3e5NSfe4FwdhU3U3sjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
FLUX 3 Video رایگان شد
؛Black Forest Labs برای مدت محدود، FLUX 3 Video رو توی Playground خودش رایگان کرده
🔥
⏰
فرصت استفاده رایگان تا دوشنبه ۱۷ آگوست، ساعت 10:30 به وقت تهران
قراره در ادامه قابلیت‌هایی مثل 4K، ادیت ویدیو و استفاده از تصویر/ویدیو به‌عنوان رفرنس هم اضافه بشه.
⚡️
✨
🔗
لینک استفاده
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آیپی تمیز
✨
188.212.97.3
94.182.177.92
185.50.39.15
103.25.85.84
176.120.17.44
45.146.240.17
45.146.240.70
77.237.246.20
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnkEpwDa1AQBDtWHe48HdTShZLxY2EwP4IhK7F4Q_-H-Tok-GVqypMWb1fAFqI6dtqDahfjGxExB2UuJ9GCuuKZEG9kkRXT5VoBx8ChLQ304wW5mIcaNBHOAgnFwK0GwtUCH2pWFx0Vjd6uWfcxYcnKwdoN6L8KSwNB917LUesjQZ2Tl7rIq9yhiwkwt46vIxvxQvbuoQ2QYUhLrY14aBgEJiQgs1M_aTMrtzNAqGywZ5p9L0IxsSwkxYjc0ShbvoEQ9AISD7qFAgXGirk8XAyNxinat_IleEx3iy8fuKE7eHsjwJbXPdyUZNfu9n5E-KTERy8uRf3qPfMuVvvgvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از 1000 پرامپت کاربردی برای هوش مصنوعی!
🚀
یه سایت که مجموعه‌ای از بهترین پرامپت‌ها رو یکجا جمع کرده؛ از درس و برنامه‌نویسی گرفته تا طراحی و Excel
⚡️
✨
یه جور جعبه‌ابزار کامل برای کار با هوش مصنوعی
🧰
🔥
🔗
لینک سایت
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voG_K7iKSRtB0qmUJPuYwYhaRKVPLH7Rw7r3eKNMGQFL8bGQZLQsC_uiX2ifCX_22bCMfDTQoEUJd0v6051nmwQDeN6Gi2qz5KtqSo3rhuiko389kFJCMwqq2AvJ_vr09aPV463i8KN1vTECpRUO5IDrsu_zrbhTz1-azfW3zjODOA_WuamClY8C105wbayVDHGCUX5WG09Eia862Xs77YsInBBIISZMY1rTmXTiloRtmBndfhebkA0YtE0tL0qjIVWpPnSuGz0GDYs8QPsVL1ZnGKskCfOzgBaHlm7Oh7TL-56yoPuYAcp1ynCm1ZlKYAbNqobDMnE6U956CGvxRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤔
گوگل قید Gemini 3.5 Pro رو زد؟
گزارش‌ها می‌گن گوگل عرضه‌ی
Gemini 3.5 Pro
رو متوقف کرده تا مستقیماً روی
Gemini 4.0
تمرکز کنه.
🚀
گفته می‌شه مشکلات عملکردی و سخت‌گیری‌های امنیتی در مرحله‌ی تست، دلیل این تصمیم بوده.
🛡
حالا رقابت جدی‌تر می‌شه؛
Gemini 4.0
می‌تونه از ChatGPT و Claude جلو بزنه؟
🤔
🔥
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7458">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7458" target="_blank">📅 11:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7457">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoJd39qRUvJwCMWuKw6NcQ-D45CFMnFnswATz6IgaRyU5zKu4-125rrjtT7ZS0A1hVUTwVb0_GnZgyUIQiJbDWxaQdRcH_a3HJPQr3_QOskDfnBKLVHk7cMTwoexxoKVN6TVnEMhGDjDF04K7LZ8hkiy18H6k0TunR49Vs-DjFDnl7HLitbzPPNAJcsNHEi30cslGs0R4uZUS0qnG7Dhz6M3XCdZW0Nv1iI80c1pu7rSvPOlTux2c3vhHbLGpn2oDKK6K3RvYmafJNSdCpfSV47GM5_ObYE2xZITdWMZE9FtzGldpJVg4TYv7AJWMxToaNQwgYGfPwiccOfWua5hsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
✨
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدیمی لازم نیست )
داشته باشید و از طریق این
لینک
وارد شید
✔
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
40 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7457" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7455">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijpHZ8GemoYCqihMmgPheeY-EltLsBCKNXscbTDW4tdiCwFTvDDsWl80zwG6ay5xKLDB7qeaw90716oP9PJ7JzU-XRg00x0ao7OfJqaze019XqCGKMbuR8O0gQ2ATt-FLnhZTBz607mBczMqNFz7UP72Imc6bOdXquwbw30QrmQ9hIyHx1fEbjfWqZXZ_ojgcNZn2QhDdJw7ue0AIzHNYnIwHMsV4rZg-QyzgZcwafMmduOmv7UbdWiBu1fiSkyny_CuTsF7rFpbNSgksnFURb6DKyenX4E0thbclzRRIIkVvio5pKUXsy3XEU9jdm7aWdzlXR8thljHLUqKBvE-oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع بزرگ یافتن سایت های API رایگان
💥
🆓
💵
با پوینت های این سایت میتونید کلید های API خریداری کنید و یا کلید API خودتون رو به فروش بزارید ، همچنین میتونید Redeem Code برای انواع سایت ها خریداری کنید و کریدیت دریافت کنید
🔍
همچنین این سایت منبع بزرگی برای یافتن سایت های API رایگان هست
🎁
موقع ورود مقداری پوینت دریافت میکنید همچنين هر روز میتونید از بخش Daily check-in ده تا پوینت دریافت کنید
⚠️
🚨
نکته:
حتما با فیلترشکن وارد شید
🔗
لینک ثبت نام
🔗
بخش خرید و فروش کلید
🔗
بخش خرید Redeem Code
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7455" target="_blank">📅 22:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhyyNMRT9Na0_UA-Td2kLzXD5nKg-EcxgOR_6XT0z8yRqKWTean80TBOfqRJDrY33hdMlmPyoFbUwbrwFdXzdvOOoB738sZiEdLZa7565gYHfxC1u7cJQcHoeY0A_w8zzlDfOqm9GyBdXooUl9Aie_lwncON-w8IZ-f3DJlKID6LNj-vaJTROsovChA2QDIGxnoz3F0RhQsuJpTYsBtT-F2vRuxSl6t7HrImdClcCSySQk_dTuT99Wc1CZcd0PrWjlDo6GZ9DB0Iuvd3wzxVYFlHL1Ctx3_1d-mCZ6xstCFPUBcCuTvERG38Uj62a1VYKNf4LSDuLOm7xs_L9EvccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش منصوعی قدرتمند
🚀
🆓
Opus 4.8 | GPT 5.6 sol
✅
وارد
این سایت
بشید و ثبت نام کنید
سپس به
این بخش
برید روی Upgrade کلیک کنید و پلن Enterprise رو انتخاب کنید و روی Start Trial بزنید تمام حالا به
این بخش
برید و در صفحه چت یه چیزی بنویسید و Let's Go رو بزنید
✅
پیشنهاد میشه که اپیکیشن Postman IDE رو دانلود کنید
‼️
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYlYXRNdxPt24hVX5lwWJLeA4yAhv_MbA8izjBhujN7-eXXxlCp3cYkDLamRm77Gxb7QJiQvn6NYMYELBd9OYy_YXJZG_T9eVvHtYu-skRv7X5s7suw12GQRbWsX27X0EqxcxEEWNSvlg-ju2jnOnIAnIFxlbY37VBX3kT9zgIas0my2WShbKtZsXoULaUqN_mJNTEjkJtAvAn3NDcTW9lNujFAd7Qilo1oRJ5UGJsAhj5pnNi_RTnCwXInxPF7p4Y8-sxV711M49o8gd4F4JO7VBhUzjq28wwjJoqMRElktzQfXGnyJJot1sLCEhPgqBVWg-W-J2tJyVTenEiGmOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 میلیون کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
dxai-sk-5feecf996d141afae9e16f8bc072d49a692312d7452a4043fd055c37aba2c8a9
🔺
Base URL:
https://airdropdxns.my.id/v1
🔺
Model ID:
grok-4.5
|
qwen3.8-max
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جزوه ساز پرومکس
❤️‍🔥
از این بعد لازم نیس سر کلاس چیزی بنویسی، فق کافیه فایل صوتی کلاسو بدی اینجا و  با کیفیت ترین جزوه ممکن رو تحویل بگیری!
📝
https://github.com/faithsaly5-stack/Study-Note-Maker
تست کنین نظرتونو بگین
❤️
⚡️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7450">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پایان دورانِ عذاب‌آور جزوه‌نویسی دستی!
✍️
یه متد خفن طراحی کردم که می‌تونه ساعت‌ها ویس و فایل صوتی رو به یه جزوه‌ی تمیز، مرتب و آماده‌ی خوندن (Study Note) تبدیل کنه.
✍️
فرض کن ۲۰ تا فایل صوتی داری (مثلاً ۱۲ ساعت ویسِ کلاس یا ویدیوی یوتیوب) که نه وقت می‌کنی همه‌شو گوش بدی، نه می‌تونی کلمه‌به‌کلمه بنویسی. با این روش،
بدون اینکه حتی یک نکته از قلم بیفته
، کل اون ۱۲ ساعت تبدیل میشه به یه جزوه‌ی شسته‌رفته!
🤩
فرقی نمی‌کنه دانشجو باشی و درگیر حجم سنگین درس‌های ارشد، یا دانش‌آموزی که وقت سرخاروندن نداره؛ این ترفند کلاً سیستم درس خوندنت رو عوض می‌کنه. کافیه صدای استاد رو سر کلاس ضبط کنی، بقیه‌ش با این متد!
🎙
دارم یکم دیگه روش کار می‌کنم که حسابی کامل بشه. اگه پایه‌اید و می‌خواید امشب تو کانال بذارمش، پست رو لایک کنید تا انرژی بگیرم.
☺️
✈️
ArchiveTell | S</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5u8oIAL6aQDUb9OaltrRjzeOWI_uwJWZ9SMCWSqmByQhxO2yNmH-DYeVQILBjGEVRBg1PlrL5TCKI1AsJSqVyl6cvA2Ep0l2C7Xb1aL8C8VtC1AXr3Jn6vnnehTmMzvnr7-HMbj2Hb427_QTfyyFnFAer65QZQczvNOjHB5jtCAhpDlgjD9RXqffgF53s9EkMn7FoDWKBr99hwAmskE4QMoR2LqnZeukfb3fh6eFuQ6hidgx2xJQCNknCVX2x2UH-ceRUTgG_TmAcv9gxkaWIMpT1QeU3-VZcUDD4X6Eq_nLfsX3O1aODVxn5Wop3n0vpAFpx6zGj-oQNgeVM3wDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://tabitoken.com/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
120 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRjBtvF9oPmqa7-Hv2XOUvF_Ey8FGprKlym1iCUnzFR9bme6G5rG1o5SNu2LOeeTL7L9NRok-pIQSy8kn0HcBtM1LUynovn5zUleL2BoV7vQdbJ81PEqsoxcqpVlCw5vXiX5TEW3UpYz6kR4rw1fk835sc5pWWaXKcmtVcEP_4BGiD3oActGcYRaNOT9b6x5pUcwZ2tBoWl6pTU0Nu7GFHKhPjlzi5XXXvPVbG7MHN_YB6b-aANuKAYKv-6IKUyPc6TtNLCgqOwdOi50irv-G4BiZ5ucn728Fz3xF5fXoaIiGTxsSUJnxYQCgQLFcDKdEjy6f8-3Qt2TRSD2Fk-71A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20
دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
GPT 5.6 sol | Mimo 2.5 pro | GLM 5.2 | Gemini 3.5 flash | Deepseek V4 Falsh | MiniMax M3
✅
برای فعال‌سازی فقط کافیه یک Gmail یا outlook داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://fapi.leileihog.top/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
20 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH-aGh_eG1sX-QrzW7g3_f_-nRRGapoz3WmAg8ejD_YWV3LwEHcGL_usq07K8rFGaDKiAiO2oZX0aj-Z3LlR_gJqq3o8yfaLL31TmPz6jEe455p6a0APtR37Zoc7bCEmAju0Afru4fD6D9kYu9GbyDgDDE1zZbYdTsIzsBYCMntaukc9oVlN9FsOaoh8mfRsIyTG6NhtSR39vmjT0Vx1haIByPloZ_RIuaCYIjM9F33pBp7y37BnMsOm3D97qtn0rd18hSjMnYRLhTkj7nZ5vHwDqKnuAJxCuIjKvsOaGQatZSoxdJhJFaydqV78-yrKG3NC_iqwt8IstAHxHuuvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10 هزار کریدیت برای دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
GPT 5.6 sol | Opus 4.8 | Deepseek V4 Flash | Kimi k3 | GLM 5.2 | Sonnet 5 | Grok 4.3 | MiniMax M3 | Gpt image 2 | Seedance 2.0 fast
✅
قابل استفاده در
Vega Agent
✅
Base URL:
https://www.getunikey.ai/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaeqvahKDR91k3NUBsd4BsCxVDZlgR2829jqs7R52GY-RHsl3yFGs7pF6DTXwlW7eb_LuSclerGkqk0KEKXgjAAVeppzx_YawzznvV4RcxKgp7aWtMVzO8myfVZgprX7ljXHbP9cwgK1SwOw8qajmXApwJOtj_gfTtrMfn63gFDKF5rgWBU1ZVZ6cpiiUokqgdzKcSunIxhJYR1iu1eZmqs96Y6w4U1jdhOXIKxi_i1ZF3gEjmOefhHijIUbg_wNQnun-g295BXdFhYVPrk3D7qNgvI_iRklE2Aa0neC_IPoEB1-L9YuIHqI7AKpnnTjf5jmIt6KvR_2a0TIxIg9ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان نامحدود به برترین مدل ها برای چت کردن
⚡️
🆓
با این سایت میتونید به 35 مدل هوش مصنوعی به صورت رایگان دسترسی پیدا کنید از جمله :
🚀
GPT 5.6 Terra pro | Grok 4.5 | Deepseek 4 pro | MiniMax M3 | Gemini 3.6
✅
🚨
توجه برخی مدل ها مانند GPT 5.6 از کریدیت شما کم میکنند ، این سایت هر ماه 3057 کریدیت به شما میدهد
💵
😎
🔗
لینک ثبت نام
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">💥
🍌
نانو بنانا پرو نابود شد!
کمپانی xAI مدل Imagine Image 2.0 را معرفی کرد که با قابلیت‌های خیره‌کننده، اینترنت را منفجر کرده است:
🚀
🎯
پیروی دقیق از پرامپت بدون افت کیفیت
✂️
ویرایش دقیق و حذف پس‌زمینه پیچیده با حفظ شفافیت
🔗
پشتیبانی از ۵ رفرنس به صورت همزمان
✍️
رندر بی‌نقص متن روی تصاویر
📈
آپدیت و اسکیل عالی تصاویر
این مدل قدرتمند هم‌اکنون در Grok در دسترس است!
🔥
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=CbJ2w8Xq7P9zhz6KNoWxbN_Llcc2QJ1kGrHfaR-cmhH9iNd61J63IVCY4Wg4FTctJ_-0kJ52dYib7sJs1LinU3Qy7bNlHdaNzDVED_5EAcvkg34U8t9rlKu_g2rUWCKM3F-yyD3unM47uW8sY4S0avcXdczAWzDG6kEqgdOHVmmOdhYElLsSA7_xoJr4USq3RUZqXifLXs2SYO46izy7n091xEzZrSkt9kGKA1W9pw7q8oAjkQn2CaAXwk8LhyMPmPvFM2XVRrqSMpSzDkx9Mli6wMWgZj6Tz3j6wrlehEyqhyos_7NS2GVjOn5YQHj_Fgc0ceJ1CJSXYNdPNXLxZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=CbJ2w8Xq7P9zhz6KNoWxbN_Llcc2QJ1kGrHfaR-cmhH9iNd61J63IVCY4Wg4FTctJ_-0kJ52dYib7sJs1LinU3Qy7bNlHdaNzDVED_5EAcvkg34U8t9rlKu_g2rUWCKM3F-yyD3unM47uW8sY4S0avcXdczAWzDG6kEqgdOHVmmOdhYElLsSA7_xoJr4USq3RUZqXifLXs2SYO46izy7n091xEzZrSkt9kGKA1W9pw7q8oAjkQn2CaAXwk8LhyMPmPvFM2XVRrqSMpSzDkx9Mli6wMWgZj6Tz3j6wrlehEyqhyos_7NS2GVjOn5YQHj_Fgc0ceJ1CJSXYNdPNXLxZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهندسی معکوس پروژه‌های گیت‌هاب با GitReverse
◀
☁️
بچه‌ها اگه یه پروژه خفن تو گیت‌هاب دیدید و خواستید دقیقاً همون رو با هوش مصنوعی (مثل Cursor یا Claude) از صفر کدنویسی کنید،
gitreverse
خوراکتونه!
🔺
چیکار می‌کنه؟
لینک پروژه رو بهش می‌دید، اونم کل فایل‌ها و ساختارش رو آنالیز می‌کنه و یه «پرامپت» جامع بهتون می‌ده. حالا کافیه این پرامپت رو به AI بدید تا کل پروژه رو براتون دوباره خلق کنه!
🔺
ویژگی‌ها:
پشتیبانی از مدل‌های مثل Grok-3، Gemini-2.5-Pro و GPT-5.4.
🐱
دانلود سورس‌کد از گیت‌هاب
🌐
سایت رسمی (نسخه آماده استفاده)
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فرار از زندان برای مدل های Sonnet 4.6 و Haiku 4.5
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taMCeeoQbcI8RaMhhZKMkboaQFiSwDGjyUiHApYyPU5g1aUtANi_aWGScC89G4X-dR23w7iw4qzecjE03xoCt_yeIDVprUSuBhr5BMfFTbswSRmR3Bo-AequtJT1NdNRdOTwXqi7Ig8escNwqyiXM9nQ_GN2VoZ1keVNHiV1mAws59reKdl1zBEw1xVgQLFJOcnpF7dMzKeytWR9oZrMpYmI95S2J0hkIFRIjyddSHU_5Pftxmo4BMlPr29t7Iv95iVlQuHCtoQA9v0kOhO-LwCP4Ul7KsNCH84L77Nb9MP6m6c4DaPMrie1Tg9lHElQMpnavk2NhWzsvB-jj8krMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
Base URL:
https://tokenharbor.ai/v1
قابل استفاده در
Vega Agent
✅
با جیمیل وارد شید سپس لینک ارسال شده به جیمیل رو باز کنید و 5 دلار رو دریافت کنید همچنین تیک Free models enabled رو بزنید
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فرار از زندان برای مدل های Gemini 3.5 و GLM 5.2
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=nCnr9ckNHNZk5fGUWtTcs5GamIKLhNHW-wZTXN8QYVtGkiFgfkhyMZEH7c7UgILJvxou66c5oKHwtZZcBJBTCrMnSSVCq1QUEnf6GBksaTQLTrEJ7zvqBgTm0KO6lANvn_cxV9VDzWyOEom67H2TMO0AiW4Fit_9kqNnxKWleAsTYETUI9VGCRspU0PF-bgvfJDINF8ToltrfK8gYV5SCLqX_6bFx6vzyR2bTbS3LlIZoTPmiF_vVvaU72w0aoA8F1nd1vo2FF40Wp6kLCFaG58PSpXCFZXPMWav5tlcM9sceWHeWXm3TcHTN2xPtj6-AWFXTkduh_7w7o6-ZJVhYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=nCnr9ckNHNZk5fGUWtTcs5GamIKLhNHW-wZTXN8QYVtGkiFgfkhyMZEH7c7UgILJvxou66c5oKHwtZZcBJBTCrMnSSVCq1QUEnf6GBksaTQLTrEJ7zvqBgTm0KO6lANvn_cxV9VDzWyOEom67H2TMO0AiW4Fit_9kqNnxKWleAsTYETUI9VGCRspU0PF-bgvfJDINF8ToltrfK8gYV5SCLqX_6bFx6vzyR2bTbS3LlIZoTPmiF_vVvaU72w0aoA8F1nd1vo2FF40Wp6kLCFaG58PSpXCFZXPMWav5tlcM9sceWHeWXm3TcHTN2xPtj6-AWFXTkduh_7w7o6-ZJVhYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمدید فرصت ساخت ویدیوی رایگان با Gemini
♊️
🆓
بچه‌ها گوگل مهلت استفاده از ابزار خفن ویدیوساز Gemini Omni رو تمدید کرد!
جزئیات:
حالا تا
۱۱ آگوست ۲۰۲۶
فرصت دارید که
۱۰ تا ویدیو
رو کاملاً رایگان بسازید (قبلاً تا ۴ آگوست بود).
❓
چطوری؟
تو اپلیکیشن یا نسخه وب جمینای، برید تو منوی ابزارها (Tools) و گزینه «Create video» رو انتخاب کنید.
جا نمونید، برید تستش کنید ببینید چطوره!
😳
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_6LVr8yrL3Zvn3OFXkSC7MF1C5AvX70-w3rjg65KWxO_tmvBvn0M-bGGvequP8bEuaRihxWKhZQwBAaVZSG7uyA2owLioRdaUdhYJnmkEi5AuE20GZJbm9DscsBKSun7dE7TTM8eP_3vUkJwrd03TIlHa-APXNkF4zeUtsJiV_gxZB0hqWzSJDkIvU36_88fHyoNKQSR5fJcguA8zBT8Tz1Rzp-epW_QEoSIc8rQ4juTLApcDFfjkZ4vcsW09cdbw3i6uvUb6ei78P4j0wJ1pud87zSkuArKSd7K-bs_3AzNAbBPjtdCfVlINk4KGeCIdW0myNz3yZXSVay7QKXRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن خفن و متن‌باز بدنسازی با openGym
💪
💪
اگه از اشتراک‌های پولی و تبلیغات اپ‌های ورزشی خسته شدید،
openGym
یه جایگزین رایگان و کاملاً شخصیه که دیتای شما رو تو سرورهای غریبه ذخیره نمی‌کنه!
📌
چرا باید نصبش کنید؟
💠
دیتابیس کامل:
بیش از ۱۳۰۰ حرکت ورزشی با انیمیشن آموزشی.
🗺️
نقشه عضلانی:
روی تصویر بدن نشون می‌ده این هفته کدوم عضلات رو بیشتر درگیر کردید.
✴️
پیشرفت هوشمند:
خودش حساب می‌کنه جلسه بعد باید چه وزنه‌ای بزنید.
👾
بدون نیاز به پسورد:
ورود امن با اثر انگشت یا چهره (Passkey).
📜
انتقال دیتا:
می‌تونید تاریخچه تمریناتتون رو از برنامه‌های Strong ،Hevy یا FitNotes بیارید اینجا.
✅
صفحه همیشه روشن:
موقع تمرین صفحه گوشی خاموش نمی‌شه تا راحت رکوردها رو ثبت کنید.
💡
نصب:
می‌تونید فایل APK رو دانلود و کاملاً
آفلاین
روی اندروید نصب کنید، یا با Docker روی سرور خودتون بالا بیارید تا بین همه دستگاه‌هاتون سینک بشه.
☁️
دانلود APK و آموزش نصب از گیت‌هاب
🌐
نسخه دموی آنلاین (برای تست محیط برنامه)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_Q5B3e7KdfKhgUJcImh_6OqaW6cm_LLzSpo5IjxgoeJoPWOeT4THSjzzQ6eCFruDNl10fpEaoR_33w6vB30gqZemNcuQ7m_Qy3bK3GtvQpRv2DlOWC1vRbyBTbN3rQR5o8q5DAZEHbHiQY-0kAKFwMcdR03KV85keHeobvqcl2eIFHkX8rb-kAo2D3_HYQUI0cRYPYaxIapc0wTjrNak22tYfM2DW6_GWOCGptAWx0Np8gIQd3DdG6SkxpGs2DmpfAnoB6cRR0m5Xf8Sio56-gtiYqqrDpUowMsh21KW1RuDoLOR7EsTmumzH4iaMr9qjdjnK2dF4uKVpVo6Uzv7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
