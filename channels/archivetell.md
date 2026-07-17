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
<img src="https://cdn4.telesco.pe/file/vFfN-ofjbqrxXN6zHW1xch8ZVqBXahE3yy7zaw-d__1ggMSHQuJIjtbzLuH_GKUupeBwUXIvV3-LhyTQadIOS_1mmg-YjkC3L3ecO1hY8tmHQAJ4ao8IuZCnYde2kpcpca2QHmS-RxWJLiImiWJzJBn2njywl4BdAT58QEsS3BKu7KYhrIlpurJKE6QVG1a6f6bl_em_XxcrcaZ0Gg5q8Teh-zUOqfILy8uCp69bZogPLHQ6rfgXGqMI0az60YQuc-CgRYo0ZFVzqo1VLfUonqrsWzOpR8qcXp03YYs_In9xCD_R15-wytM68H8JvwOg6F6kWSUcScItIaCFmM_eOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.83K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 00:28:36</div>
<hr>

<div class="tg-post" id="msg-7082">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎁
پلتفرم Gab AI؛ دریافت صدها اعتبار رایگان برای تست پیشرفته‌ترین مدل‌ها  یک محیط چت و ورک‌پیس جامع هوش مصنوعی با دسترسی به بیش از ۱۰۰ مدل مختلف که در بدو ورود، ۱۷۵ کرَدیت رایگان (بدون نیاز به کارت اعتباری) هدیه می‌دهد و حالا با به‌روزرسانی جدید، راه‌های بسیار…</div>
<div class="tg-footer">👁️ 112 · <a href="https://t.me/ArchiveTell/7082" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7081">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎁
پلتفرم Gab AI؛ دریافت صدها اعتبار رایگان برای تست پیشرفته‌ترین مدل‌ها
یک محیط چت و ورک‌پیس جامع هوش مصنوعی با دسترسی به بیش از ۱۰۰ مدل مختلف که در بدو ورود، ۱۷۵ کرَدیت رایگان (بدون نیاز به کارت اعتباری) هدیه می‌دهد و حالا با به‌روزرسانی جدید، راه‌های بسیار جذابی برای دریافت اعتبار رایگان اضافه کرده است!
✨
امکانات و راه‌های افزایش اعتبار:
🔸
تست مدل‌های پرچم‌دار:
دسترسی رایگان به غول‌هایی مثل Claude Opus 4.8، Fable 5 و GPT-5.5.
🔸
ابزارهای همه‌کاره:
امکان تولید تصویر، ویدیو، موزیک، مدل‌های 3D و حتی ساخت فایل پاورپوینت مستقیماً در محیط چت!
🔸
دریافت بیش از ۵۰۰ کردیت اضافی:
با انجام تسک‌های ساده می‌توانید اعتبارتان را بالا ببرید. مثلاً انتقال تاریخچه چت‌ها (Import) از ChatGPT یا Claude معادل
+۲۰۰ کردیت**، فعال‌سازی تایید دومرحله‌ای
+۵۰ کردیت** و ورود از دستگاه دیگر
+۵۰ کردیت
پاداش دارد (به‌علاوه تسک‌های روزانه).
🔸
سیستم دعوت (Referral):
اگر دوستانتان با لینک شما ثبت‌نام کرده و اشتراک Plus تهیه کنند، به هر دو نفرتان
۲۵۰ کردیت
هدیه داده می‌شود.
⚠️
واقعیت‌سنجی (Reality Check):
میزان مصرف مدل‌های برتر بالاست؛ ارسال هر پیام در Opus 4.8 و Fable 5 معادل ۱۶ کردیت کسر می‌کند. همچنین طرح رایگان صرفاً برای محیط کاربری وب/اپلیکیشن است و دسترسی به API نیاز به خرید اشتراک دارد. با این حال، برای تست سریعِ جدیدترین مدل‌ها بدون دردسرِ کارت بانکی، گزینه‌ای بی‌نظیر است.
🌐
وب‌سایت:
gab.ai
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 225 · <a href="https://t.me/ArchiveTell/7081" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7080">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkQxJbGEV_H6YDoM8aM3rsmlCGNLXafmXDBWkI_-eRyrXfzfcd9o89WJ9qqRQ0uBFYYt0Li9cCXCE1KGtON6cfUuadmyrNuB-PYzPtAgvb0N9_XvuJrjtcej0hdR6g3-YJWhk1XGllyOy6AX7P5--RrjL_3hzW82hYt2MN939gtVe1-UfvlT2Gqnw9w_RDuLoALcB_OIikg0sCts8fRIbEImLsKH47UibvqTkhTT8jg9LKneNjusIvj7M_ErzceM_JTo7fs-e0dJz18L7-Ed-bvpKtAtqXVq9ocfBjPhdoqMoR4HosveRbTt0bkdZRYgGXmZodJTixnGs87Aw_K95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 226 · <a href="https://t.me/ArchiveTell/7080" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7079">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌐
پلتفرم Api.Airforce؛ هاب یکپارچه ۲۰۹ مدل هوش مصنوعی  دسترسی جامع به برترین مدل‌های AI جهان در یک محیط واحد و بدون نیاز به حساب‌های مجزا.
✨
امکانات کلیدی:
🔸
تنوع بالا: پشتیبانی از ۲۰۹ مدل مختلف شامل Claude (Opus 4.7 و Fable 5)، DeepSeek v4 و ابزار صوتی ElevenLabs.…</div>
<div class="tg-footer">👁️ 378 · <a href="https://t.me/ArchiveTell/7079" target="_blank">📅 00:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7078">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">Gemini 3.5 Pro
از درد عشق تو خوابمون نمیبره چرا نمیای لعنتی
😂
💔</div>
<div class="tg-footer">👁️ 571 · <a href="https://t.me/ArchiveTell/7078" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7077">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🌐
پلتفرم Api.Airforce؛ هاب یکپارچه ۲۰۹ مدل هوش مصنوعی
دسترسی جامع به برترین مدل‌های AI جهان در یک محیط واحد و بدون نیاز به حساب‌های مجزا.
✨
امکانات کلیدی:
🔸
تنوع بالا:
پشتیبانی از ۲۰۹ مدل مختلف شامل Claude (Opus 4.7 و Fable 5)، DeepSeek v4 و ابزار صوتی ElevenLabs.
🔸
پلن رایگان:
۱۳ مدل رایگان (مثل gpt-4o-mini و تولید موزیک Suno) با سهمیه روزانه ۱۰۰۰ درخواست (۱ ریکوئست در دقیقه) جهت تست اولیه.
🔸
مدیریت منعطف:
ساخت بی‌نهایت API Key بدون محدودیت آی‌پی (IP Whitelist) به همراه داشبورد مانیتورینگ.
🔸
سازگاری استاندارد:
پشتیبانی کامل از فرمت OpenAI API جهت همگام‌سازی آسان با کلاینت‌هایی نظیر Cline و OpenCode.
🔸
کسب درآمد:
دریافت ۱۰٪ از مبلغ شارژ دوستانِ دعوت‌شده (به‌علاوه ۱ روز اشتراک Premium رایگان برای آن‌ها).
🌐
وب‌سایت: api.airforce
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/ArchiveTell/7077" target="_blank">📅 23:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7076">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSR5J4CPMjdc6w6J6s1wdP25oILWWbl1Go2hyaz4lkoqAgGcMB2PcUg9K5qEiCjMljPeSjIZohjbvXUqf2A45Sp75mmtXSZv_6XIGJUvsoYzmhaDNVqTcTeoTFTSBMynrMjEWA5DHpKXIQXvbcip-Qjs8LH2sq1KbF3W9Eutx3NV8QV_ckAPVyluH-ZKST_sIjdtbsQJEAz-GOWB0c0XJwRs25jXHzVu8eImgXkEZy4Mr4ryaqieB5hJvg2l7Ftcmv9JV_9PUUZddOEOQUp09E7XU5b18-P3az1WtGoHy1sNVO2zwOXTcs7t4Q-muUq-CXtIePV3DSN8dbBS3DyGjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی افزونه YouTube Subtitle Pro؛ شخصی‌سازی زیرنویس یوتیوب
یک افزونه کاربردی کروم برای کنترل کامل و تغییر ظاهر زیرنویس ویدیوها و شورتس‌ها در یوتیوب.
✨
امکانات کلیدی:
🔸
فونت و فایل دلخواه:
استفاده از فونت‌های سیستم و امکان بارگذاری فایل زیرنویس خارجی (SRT).
🔸
استایل مجزا:
تنظیمات ظاهری جداگانه برای زبان‌های فارسی و انگلیسی (به همراه اصلاح علائم نگارشی).
🔸
تغییرات ظاهری:
ویرایش دقیق سایز، رنگ، بک‌گراند و حاشیه کلمات.
🔸
فیلتر هوشمند:
امکان تعریف و حذف خودکار کلمات تبلیغاتی یا مزاحم از متن زیرنویس.
⚡️
دسترسی سریع:
فشردن کلیدهای Alt + S هنگام تماشای ویدیو.
📥
نصب از کروم استور
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 773 · <a href="https://t.me/ArchiveTell/7076" target="_blank">📅 23:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7075">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 811 · <a href="https://t.me/ArchiveTell/7075" target="_blank">📅 23:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7074">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">vless://df4bda66-59d7-4b79-abd0-0e4ee14d7c70@188.130.207.217:443?type=ws&encryption=none&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF   بزنید عشق کنید زمانش 24 ساعته</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/7074" target="_blank">📅 20:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7073">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">vless://df4bda66-59d7-4b79-abd0-0e4ee14d7c70@188.130.207.217:443?type=ws&encryption=none&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
بزنید عشق کنید
زمانش 24 ساعته</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/7073" target="_blank">📅 20:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7072">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏دسترسی رایگان به مدل‌های هوش مصنوعی با این لیستِ کاربردی!
⚡️
‏این سرویس‌ها بهترین انتخاب برای دریافت ‌API Key⁩ و تستِ مدل‌های مختلف هستند:
‏
👑
برترین‌ها:
‌
Agentrouter⁩
| ‌
Iamhc⁩
| ‌
Google⁩
| ‌
Groq⁩
| ‌
Nvidia
| ‌
Cloudflare⁩
| ‌
Freetokenfaucet⁩
| ‌
Dahl⁩
| ‌
Tokengo⁩
| ‌
Opencode⁩
|
Unorouter⁩
‏
✨
سایر گزینه‌ها:
‌
Kenari⁩
| ‌
Cerebras⁩
| ‌
Nararouter⁩
| ‌
Llm7⁩
|
Openrouter⁩
‏با این ابزارها، پروژه‌هات رو بدون هزینه پیش ببر.
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/ArchiveTell/7072" target="_blank">📅 20:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7071">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔓
آرشیو کامل پرامپت‌های سیستمیِ لورفته هوش مصنوعی!
ریپازیتوری
system_prompts_leaks
یک گنجینه واقعی برای توسعه‌دهندگان و مهندسان پرامپت است که دستورات مخفی و پایه (System Prompts) معروف‌ترین چت‌بات‌ها را جمع‌آوری کرده است.
✨
محتوای این ریپازیتوری:
🔸
جدیدترین مدل‌ها:
شامل دستورات پایه‌ی مخفی GPT-5.6, Claude Sonnet 5, Gemini 3.5 Flash, DeepSeek و Kimi.
🔸
تفکیک شرکتی:
آرشیو کامل و تفکیک‌شده‌ی مدل‌های OpenAI, Google, Anthropic, xAI, Meta و Perplexity.
🔸
ابزارهای توسعه:
شامل پرامپت‌های سیستمی دستیارهای برنامه‌نویسی مثل Cursor و GitHub Copilot.
🔸
یک منبع آموزشی ناب:
بهترین رفرنس برای یادگیری نحوه ساختاربندی دستورات و محدودیت‌گذاری توسط غول‌های تکنولوژی.
📥
مشاهده پرامپت‌ها در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/ArchiveTell/7071" target="_blank">📅 19:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7070">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">؛MIT OpenCourseWare یه پلتفرم آنلاین رایگانه که توسط موسسه فناوری ماساچوست (MIT) ارائه میشه و بیش از 2500 دوره آموزشی رو شامل میشه
🎓
🌐
http://ocw.mit.edu/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/7070" target="_blank">📅 19:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7069">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYrTcoYZHc9i4stHEjIca00xMMWGd6ks7yo6LdLniaAcblGkFO_K5jwtqcmIsgKCz-jtpRZzP3238-zlt4RcMei-AbPjHPmQHt9xvyFcIRUXAdgRf0RxT0WJxxfpdkYhoHnM7X_4s7PcHrhpnhmoL2FVW3cmSmuhO4phG01g3FopOLBBRv58CF9wdDfpiANlIYUedB2K8w9skoEi4IsJzNDuzX4k9HJRSCsxrUFg1uGz7G8enarD-Amzkux4nh_Jr1sgBpCtPFHKgkSrdl3wn7DxYI40kCK7dgKwCL2IcueUQN9iyScTSh3_kzE1iw4rRVJxzqdxQIDjRic9vDEbFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Oh My HuggingFace برنامه کاربردی و متن‌باز برای HuggingFace که برای مرور و دانلود سریع، محلی و خصوصی مدل‌ها، مجموعه‌داده‌ها و غیره استفاده میشه.
🌐
https://ohmyhf.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/7069" target="_blank">📅 18:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7068">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">happy کنترل ai از راه دور
🧠
Happy
یک پروژه
متن‌باز
است که به شما اجازه می‌دهد
Claude Code
و
OpenAI
Codex CLI
را از طریق
موبایل
یا
مرورگر
مدیریت کنید
⭐️
ویژگی‌ها:
✅
کنترل سشن از راه دور
✅
دریافت نوتیفیکیشن
✅
ادامه چت از موبایل یا وب
✅
پشتیبانی از مکالمه صوتی
✅
رمزنگاری End-to-End
✅
کاملاً متن‌باز (Open Source)
اگر از
AI Coding Agent
ها استفاده می‌کنید،
Happy
می‌تواند مدیریت تسک‌های طولانی را بسیار راحت‌تر کند؛ بدون اینکه همیشه پشت سیستم باشید
Github
💻
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/7068" target="_blank">📅 18:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7067">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c18bdbfa.mp4?token=hhE36KhOoekNY6OthDqhgygnY5UXGy1fYFmMqsfc_Hbxae0gUs4H2ElZzDT-v92_NZqN3AA9qTDM0iWk3NZyyRlKzItZKwt7FXdkqU5u83jjUC_IQv06a_m4YvbCdhwxZT-BN3x8ehjQ6Pbq8M5ImyEmijR23NYTicV4otYpznpTjq5iLu3AaqpHrKzYJ06e2toBmzeHG2RJomKBlZe1IeyT7vttp9Kmsou_3s79JDzii5anXx1OzSGYuZwJNHAxdTmCPSMRiTeglTo-1xKdUOcaECBdMfw0IodcBjzVmYCRTmAN2NOndIcvImjRtg5DJCxy8L_mVoWN6gginKh17A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c18bdbfa.mp4?token=hhE36KhOoekNY6OthDqhgygnY5UXGy1fYFmMqsfc_Hbxae0gUs4H2ElZzDT-v92_NZqN3AA9qTDM0iWk3NZyyRlKzItZKwt7FXdkqU5u83jjUC_IQv06a_m4YvbCdhwxZT-BN3x8ehjQ6Pbq8M5ImyEmijR23NYTicV4otYpznpTjq5iLu3AaqpHrKzYJ06e2toBmzeHG2RJomKBlZe1IeyT7vttp9Kmsou_3s79JDzii5anXx1OzSGYuZwJNHAxdTmCPSMRiTeglTo-1xKdUOcaECBdMfw0IodcBjzVmYCRTmAN2NOndIcvImjRtg5DJCxy8L_mVoWN6gginKh17A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جستجوی چت‌های قدیمی در ‌ChatGPT⁩ بالاخره راحت شد!
🔍
✨
‏دیگر نیازی به اسکرول کردن‌های بی‌پایان نیست. ‌OpenAI⁩ قابلیت «جستجوی یکپارچه» را برای وب، اندروید و ‌iOS⁩ فعال کرده است. حالا می‌توانید از یک پنجره واحد، میان تمام گفتگوها، پروژه‌ها، فایل‌های آپلود شده و تصاویر جستجو کنید.
📂
🚀
‏با استفاده از فیلترهای جدید، دسترسی به پیام‌ها یا اسناد قدیمی که ماه‌ها پیش ذخیره کرده بودید، در چند ثانیه انجام می‌شود. یک آپدیت کوچک اما به‌شدت کاربردی برای کسانی که زیاد با هوش مصنوعی سروکار دارند!
💡
✅
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/7067" target="_blank">📅 17:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7066">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">vless://06069771-bef8-4730-b711-c51efcdad901@onlineprochess.ir:8880?mode=auto&path=%2Fws&security=none&encryption=none&host=tsrety.dpdns.org&type=xhttp#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF  تمام نامحدود</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/7066" target="_blank">📅 17:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7065">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">vless://06069771-bef8-4730-b711-c51efcdad901@onlineprochess.ir:8880?mode=auto&path=%2Fws&security=none&encryption=none&host=tsrety.dpdns.org&type=xhttp#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
تمام نامحدود</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/7065" target="_blank">📅 16:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7064">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN-oSBvgHC5D41MOvxSfNkGDFxvzKeafIlu_lMs0m7mSibgr-Ky6lHlCdWUk81ezOTPTRbAb1JOVFHlAzoedij1nk2sR_zM1n-IWYGTeOVQKhe5cQybvLTRRhZNKJNKOEU_g033to5HEnC27P55nHAsC-ZqoLMJ_75b9PTyRMIVYOoHYALnSsHbMicHsOXQiPVmeJBwpZcauskzSLQmh7K18HdR-1mLNtcjIZ9y-IqzGKz_Sm7O4-sHhgCgaOlD7C5Fi0fOrEAUNPjcGRShxNB0RYWMf-o45TU4E6j5U3FtEqFp1t5ytnedwKdlb792tJwxrgOB2ertUDFr0OrGRzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
معرفی SHADOHDORKS؛ موتور جستجوی قدرتمند گوگل دورکینگ
یک مرجع فوق‌العاده و ابزار تخصصی برای OSINT و جستجوی پیشرفته (Dorking) در گوگل که برای محققین امنیت، باگ‌هانترها و تحلیلگران شبکه به‌شدت کاربردی است.
✨
ویژگی‌های کلیدی این ابزار:
🔸
دارای بیش از
۱۰۰۰ دورک (Dork) پیشرفته
و دسته‌بندی‌شده.
🔸
پیدا کردن هوشمند
ساب‌دامین‌ها (Subdomains)
.
🔸
جستجو و کشف
پنل‌های مدیریتی مخفی یا در معرض دید (Exposed Panels)
.
🔸
شناسایی
نشت اطلاعات و کلیدهای API
در سطح وب.
🌐
آدرس دسترسی مستقیم به ابزار:
🛠
مشاهده سایر ابزارهای کاربردی OSINT:
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/7064" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7062">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01b871c31b.mp4?token=ZlQlDKguwdfpIp-I9fLFKtrWl0sr_hmhYQRFPHLKhqG_pl5lgxyo8rvRJvDfukN5U13yPZeAWCZXpD9oBAIEajvlGYoitxX9rQikfmTrVT-hYxur1C1W7MGwEjUdTUqZAa1TcumDkHlDriCQI4NAeLO5oBC0-q-eR4DEoQdg3WTjUxvakY7jmYq-Ujxed3DbWmLYMbmCX-rY6Qh0jF-67TFUnN8F0W1JSUxQngVPfd8vVrbCRh6wbGf3tRsT7GBd794WJfi44ADsWLqotjp2hdJKoygg3nySjg2nSpu3SAM1VRzI9bLoBp11C4Yy5csa3LqRq-VcMBb6j0IhBAz9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01b871c31b.mp4?token=ZlQlDKguwdfpIp-I9fLFKtrWl0sr_hmhYQRFPHLKhqG_pl5lgxyo8rvRJvDfukN5U13yPZeAWCZXpD9oBAIEajvlGYoitxX9rQikfmTrVT-hYxur1C1W7MGwEjUdTUqZAa1TcumDkHlDriCQI4NAeLO5oBC0-q-eR4DEoQdg3WTjUxvakY7jmYq-Ujxed3DbWmLYMbmCX-rY6Qh0jF-67TFUnN8F0W1JSUxQngVPfd8vVrbCRh6wbGf3tRsT7GBd794WJfi44ADsWLqotjp2hdJKoygg3nySjg2nSpu3SAM1VRzI9bLoBp11C4Yy5csa3LqRq-VcMBb6j0IhBAz9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نسخه جدید گفتگوی صوتی Chat gpt منتشر شده و انقد طبیعیه، پشمای همه ریخته!
+ خوراک غیبت برای دختراس.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7062" target="_blank">📅 16:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7061">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3X-UI-MANUAL.fa.pdf</div>
  <div class="tg-doc-extra">1.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7061" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آموزش پنل ثنایی به زبان ساده
✨
منتشر شده توسط
@ArchiveTell
❤️‍🔥</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7061" target="_blank">📅 15:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7059">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تغییر ریجن گوگل در ۳۰ ثانیه
⏱️
به لینک زیر بروید، ریجن را انتخاب کنید، دلیل تغییر را بنویسید و ارسال کنید .
https://policies.google.com/country-association-form
حداکثر تا ۲ ساعت ریجن به جایی که میخواهید عوض می‌شود
✅
.
از توجهتان ممنونم
🙏
.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7059" target="_blank">📅 15:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7057">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">معرفی Ghost Downloader؛ جایگزین مدرن و متن‌باز برای IDM
🚀
📂
نرم‌افزار Ghost Downloader یک دانلود منیجر پیشرفته و چندپلتفرمی است که با رفع محدودیت‌های ابزارهای کلاسیک، تجربه‌ای سریع، پایدار و بهینه را برای دانلود فایل‌ها ارائه می‌دهد.
🛠
✨
✨
امکانات کلیدی:
🔸
…</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7057" target="_blank">📅 13:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7056">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">معرفی Ghost Downloader؛ جایگزین مدرن و متن‌باز برای IDM
🚀
📂
نرم‌افزار Ghost Downloader یک دانلود منیجر پیشرفته و چندپلتفرمی است که با رفع محدودیت‌های ابزارهای کلاسیک، تجربه‌ای سریع، پایدار و بهینه را برای دانلود فایل‌ها ارائه می‌دهد.
🛠
✨
✨
امکانات کلیدی:
🔸
سرعت خیره‌کننده:
قطعه‌بندی هوشمند
(AI)
فایل‌ها برای دستیابی به نهایت سرعت،
بدون نیاز به زمان انتظار
جهت ادغام (Merge) پارت‌ها در انتهای کار!
⚡️
🏎
🔸
پشتیبانی جامع:
سازگاری کامل با پروتکل‌های HTTP، تورنت (Magnet/BT)، FTP و فرمت‌های استریم نظیر M3U8.
🌐
📁
🔸
دانلودر اختصاصی یوتوب:
قابلیت دریافت مستقیم ویدیوها تا کیفیت 4K، پلی‌لیست‌ها و زیرنویس‌ها.
🎥
🍿
🔸
امنیت و عبور از محدودیت‌ها:
شبیه‌سازی دقیق اثر انگشت مرورگر (TLS Fingerprint) جهت جلوگیری از مسدود شدن دانلود توسط سیستم‌های آنتی‌بات.
🛡
🥷
🔸
افزونه هوشمند مرورگر:
شناسایی و استخراج (Sniff) خودکار لینک‌های مدیا و ویدیوها از صفحات وب.
🔗
🧠
🔸
پشتیبانی چندپلتفرمی:
بهینه‌شده برای ویندوز، لینوکس، مک و دارای اپلیکیشن کامل برای اندروید.
💻
📱
🤖
این ابزار کاملاً رایگان است، رابط کاربری مینیمالی دارد و در پس‌زمینه کمترین میزان مصرف منابع سیستم را به خود اختصاص می‌دهد.
💎
🍃
📥
دریافت فایل‌های نصبی و سورس‌کد از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7056" target="_blank">📅 13:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7055">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msxrFRzo8l0KgUqJ2knGUC_5sMSlAiNnt6eg8lHFXg5FfI5Br8krD7k0XdHBL2CLri13I2SIpfoAO-DpRTfRXiEZSFRdUOIydWsBb_VbxRW92zcHgbJPnpssgU0w2cPq-5EBZwkB87ptpPVhMVhESnmNSOnlQ01mxrQU3yA8VAbZ1Nsmgnvdvkq1nLwuyhXKhvR1yUwOq2OZs9N-qqRgyWMdFruToi4E5EuFQZOezD9j8UQmGk-y0GujATdbhmH1cx1B2ZzQtk1geIBLfi_5FMcZ5K4lgzv3iHcWzVexKFHMjf6U4hS9U7-OYjUtwyKZt4Nhav_M_AWm7L1IALibXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7055" target="_blank">📅 13:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7053">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اشتراک Gemini pro برای ۱۸ ماه فقط ۶۹۹ هزار تومن!
🎉
💰
اینو قطعا این روزا زیاد دیدین تو چنلای مختلف. خواستم بگم ماجراشو بدونین.
یه شرکت تلکام هس تو هند به اسم jio اومده با گوگل قرارداد همکاری امضا کرده.
همکاری اینطوری هستی که هر کی سیمکارت jio داشته باشه، و ماهانه ۳۴۹ روپیه معادل ۳.۷ دلار به صورت مداوم شارژش کنه، میتونه اشتراک ۱۸ ماهه جمینای رو داشته باشه. اگه یک ماه شارژ نکنه، اشتراک جمینایش غیر فعال میشه و برمیگرده نسخه رایگان.
این جیو تو هند تبدیل شده به اسکم
🤑
هندیا میخرنش، ۳ دلار شارژ میکنن، میفروشن ۵ دلار (حالا فمیلی هم میشه اشتراک گذاش، اینم حساب کنیم میشه یه ۳۰ دلار)، ولی ماه بعد تمدید نمیکنن!!! یجورایی کسب درآمد میکنن باش.
۳ دلار میدن ۳۰ دلار کسب میکنن. دلالی عالی.
خلاصه به احتمال زیاد فقط یک ماه کار میکنه حواستون باشه.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7053" target="_blank">📅 12:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7051">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5RxlcfqcXyi2KYWTweuOQ-uHtmXqr_MIx8k1mi55tIRbrbEFeC4f3MwaBtOl51E0mQ06SVqSbvyBTsiQmu396srKtmjcI3YgqnL2Bf0evmy7hOFRLwgue8hb96ry86XX1HCi-1po93tfGOQltYKKsIoFY4OObBm91VDXEFfu2rzHqSKq1CMKwBXiHl6ThIzMAa5N6GavT9-RVg1cMwXsBOKt-jgo-oUV1PVrsqjwloA69497FFdsOdxL7ZrBM24DXw2Yvn2f9mx6TmB5yKv9NKu3UTfdGM5Nx0QOvI7ZHdjJNMotYBT_EgDEMrnD7EN4dMzX1BPx7AkqMJxS1e5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
امروز باید منتظر Gemini 3.5 Pro باشیم؟
طبق جدیدترین شایعات، احتمالاً امروز گوگل از نسخه جدید هوش مصنوعی خود یعنی
Gemini 3.5 Pro
رونمایی خواهد کرد.
✨
ویژگی‌های لو رفته و انتظارات از این مدل:
🔸
حافظه ۲ میلیونی:
دارای کانتکست ویندوز (Context Window) عظیم ۲ میلیون توکنی برای پردازش یکجای داکیومنت‌ها و پروژه‌های حجیم.
🔸
حالت تفکر عمیق (Deep Think):
اضافه شدن قابلیت استدلال پیشرفته و منطقی برای حل مسائل چندمرحله‌ای و پیچیده.
🔸
غول فرانت‌اند:
تمرکز ویژه بر روی کدنویسی و عملکرد فوق‌العاده قدرتمند در حوزه فرانت‌اند (Front-End).
🛑
احتمال تأخیر در عرضه:
با توجه به رقابت بی‌رحمانه در بازار، اگر گوگل احساس کند این مدل هنوز توانایی رقابت کامل با برترین‌های فعلی را ندارد، احتمال تأخیر آن بسیار زیاد است و رونمایی به هفته آینده (۲۴ ژوئیه) موکول خواهد شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7051" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7049">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
: نفری ۵ گیگابایت
🧭
: حداقل 1 دعوت
👥
: 0/90
💾
: 5 GB
⏰
: 7 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7049" target="_blank">📅 12:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7048">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپخش کانفیگ رایگان🔥</strong></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
:
نفری ۵ گیگابایت
🧭
: حداقل 1 دعوت
👥
: 0/90
💾
: 5 GB
⏰
: 7 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7048" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7045">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2PsCCGUgsWzlsmwlrkM0-vhMhUow5-MY588lqGvirFhux_GGRgrK1EzCZ2tJuS0zLHJYgD-y7Hno1q_RJ0FyEqYEp5DiJ06thfyqwyOJCnCKVz8u_szK0Ah7WVeYIuIMIpPWK0d-oEo3uuPk1d3oLr6gGRE7CWGb3qpvPRtO2PhJ-srm6miYaOLwMZVRMi54W2sJltKR7szNmIsYXlpaiX8YsLeFWn6OXUMYjZYgWyO78CzXbJ7WmP42Roq4m69B55CwEa14E3z33TAlpJlItehHoQDbLn9jO-CZGYz6apEeixlDV6LDoPvG2lcgJBr4IgWZNhUIS6UEIpf1hzsmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔎
Google AI Edge Gallery – اجرای  هوش مصنوعی بدون اینترنت
📊
💡
گوگل پروژه متن‌باز AI Edge Gallery را منتشر کرده؛ اپلیکیشنی که به شما اجازه می‌دهد مدل‌های هوش مصنوعی را مستقیماً روی گوشی اجرا کنید، بدون اینکه به اینترنت یا سرورهای ابری نیاز داشته باشید
🌐
🔻
قابلیت ها :
🔹
چت با مدل‌های هوش مصنوعی به‌صورت کاملاً آفلاین
🔸
تحلیل و درک تصاویر
🔹
دانلود و مدیریت مدل‌های مختلف
🔸
حفظ حریم خصوصی، چون تمام پردازش روی خود دستگاه انجام می‌شود
🔥
با توجه به تجربه اختلال‌ها و محدودیت‌های اینترنت در ایران طی سال‌های اخیر، چنین ابزارهایی می‌توانند گزینه‌ای کاربردی باشند؛ چون حتی اگر دسترسی به سرویس‌های آنلاین محدود شود، همچنان امکان استفاده از هوش مصنوعی روی گوشی وجود خواهد داشت
🟡
🧪
این پروژه هنوز در مرحله آزمایشی است، اما می‌تواند یکی از مهم‌ترین قدم‌ها برای اجرای مدل‌های هوش مصنوعی به‌صورت کاملاً محلی روی موبایل باشد
GitHub
🐱
PlayStore
📲
ios
🏬
Mac
💻
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7045" target="_blank">📅 03:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7043">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">172.64.147.128 104.17.166.13 104.17.166.13 198.41.195.250 104.27.51.177  اگه پینگ نداد باید آیپی های تمیز کلودفلر رو بندازین توش</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7043" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7041">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPe8dhLSi6LKEhF7i1SeZwRxnPb45KGeoBpEZ9p8UIWnMATiJNd4mTaSGD9KkaiSGor8KLZQ2xxDFFA1Y101wxUDuIMuIX4q0lKVt1_fxknv7Y8WjC2QFy1e-9p9HnTVGUrvxzS8v95NbxkcXtIUSBjf9DDQsK8uH7aR7o5VdxBgA3DJYy8fAk_Du2_itvueC9stjtrz1j90vOnAlu2Taxv3PijdBpGFioHbzto82mNpVD85235B_Ff5tFI9BrT_nwdYJ6e-uSlMCzRAhnzzLsMrzneUUL9YiIRuN83uxocZWWP7Ym_99q6W9Oy5dQiJQjI5mF7Di22hcvNSvANkgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛HyCanvas جایگزین Open Source و Self Hosted برای Canva
🎨
مناسب افرادی که میخوان طراحی گرافیک، پست شبکه‌های اجتماعی، ارائه، ویدئو و اسناد رو روی زیرساخت خودشون، بدون واترمارک و رایگان انجام بدن.
✨
ویژگی‌ها:
🔹
اجرا در مرورگر
🔹
پشتیبانی از طراحی پست، ارائه، ویدیو، وایت‌بورد، اسناد و چاپ.
🔹
خروجی در فرمت‌های PNG، PDF و سایر فرمت‌ها.
🔹
پشتیبانی از "Bring Your Own Key" (BYOK) برای قابلیت‌های هوش مصنوعی.
🔹
امکان Build در محیط Production به‌صورت یک فایل Go.
🔗
سورس پروژه و دانلود در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7041" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7040">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zoc_jHSjXsHynn1fZB30phZo0uvcJHDFQAKVeJqwieVbjfVR5iTMU3On68O_ouN8yBBQWefXOmjkqu-zOoNn9yhDbBDU7xCnweOQC2EIhJH7gAN1vqVUy0xsdj0ySK15IUYuuOblszK5qnWxWaE1wDGjzij9oJicQwVSB8w22tZV6_9dJVWsq0X58XjtUSnITHAIPYsDbKHwVyUiYnxdrZNCIXUj7sPAhzJQhy2bfcLciRy2wCBjHsV58ElQ26osOMKUtLNBqZ4temb4BrYxl-UUrYZ4heBR-nVKA-dyKd5OH7kSgmWddXD_p4NQDMTsQmvlDkwmhhGe1haXa9FVAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200GB   vless://1c0e84d7-34ad-4242-9b4b-ea81f973e0aa@172.67.117.177:443?path=%2Farchive-stream&security=tls&encryption=none&insecure=0&host=mail.qbo.qzz.io&fp=chrome&type=ws&allowInsecure=0&sni=mail.qbo.qzz.io#%40archivetell  تمام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7040" target="_blank">📅 21:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7039">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">200GB
vless://1c0e84d7-34ad-4242-9b4b-ea81f973e0aa@172.67.117.177:443?path=%2Farchive-stream&security=tls&encryption=none&insecure=0&host=mail.qbo.qzz.io&fp=chrome&type=ws&allowInsecure=0&sni=mail.qbo.qzz.io#%40archivetell
تمام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7039" target="_blank">📅 21:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7036">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEMpGH-6BMYiUiwcnbNXSGeaUoaaE5XMf13NpWzA9wxLTYr6IdxckXmwzLdc5-GlDfpa0cAUWe-l7ugD1U2SVVhn4mD4Gj7F8VXry9UvmzJRkW1rdSBe1lT2DJ_oVkR4V0VDn-v7jO-z7mvRh4GNSQmnS8E7fdGQV4waBkIIfMtlMmhSPEI_6eJtR6MxzwS4RgN9y18XI5GR_MUi-xVTsr78LK9Zs8yOAqN0jzNrQZlP-5Ig8RB9KYxOykxTm7q5oXFY4wtyYUgs2nqQOFSSxnZIz06LsMxJSnzc50KLBD2i9iE_RzMWkxGigNYKwmFgy6RAkdsSYLOYoqKrtUFmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
هوش مصنوعی Kimi K3؛ رقیب قدرتمند چینی برای Fable 5 و GPT-5.6!
استارتاپ Moonshot AI از مدل زبانی جدید خود رونمایی کرد که با مشخصات خیره‌کننده‌اش مستقیماً غول‌های هوش مصنوعی را به چالش می‌کشد.
🔥
ویژگی‌های کلیدی:
این مدل با حدود
۳ تریلیون پارامتر
و پشتیبانی از کانتکست ویندوز
۱ میلیون توکنی
، توانایی پردازش حجم عظیمی از داده‌ها را دارد. Kimi K3 می‌تواند اسناد بسیار طولانی و پروژه‌های برنامه‌نویسی سنگین را بدون فراموشی یا از دست دادن رشته‌ی کار، به‌خوبی تحلیل کند.
🛠
امکانات و قابلیت‌ها:
🔸
نسخه Kimi K3 Max:
دارای رابط کاربری چت (Chat Interface) با حالت‌های اختصاصی و بهینه‌شده برای برنامه‌نویسی.
🔸
سیستم K3 Swarm:
یک فریم‌ورک پیشرفته برای کار با گروهی از ایجنت‌های هوش مصنوعی (AI Agents) تا وظایف پیچیده را به بخش‌های کوچک‌تر تقسیم کرده و تحقیقات گسترده انجام دهند.
🔸
دسترسی API:
به‌صورت کامل برای توسعه‌دهندگان در دسترس است.
🚀
لینک دسترسی و تست مدل
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7036" target="_blank">📅 19:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7033">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzqBoHqRZ4OQK12JNN75_UpbaehzynEPKSnDAno009GlYgD508GYZk6UXFMvL4SJWu7JGMEo3avurmp57ceLkZdjS6cZpbrCM2XOKXvKeRv2egPhca4-LHC4JmatZVlCTtfVeGLtWDi2hoReok4zwVqN9DB0VVu7hPZfoSZnJTpOeNPt37mKfT20zelCvuwp6TJdCU6E1BiSLqOMXIDVN9UiFnRe7ERhM0dG7EPUzUCjCdaL06Czfw0uqVMX4RPsnX4-CJScUl1gGq65ldtZ-iDalJiUVDfqopVYzLwAnGFUtUdE2n9ifWtTpUn5ikhwdjiGfCNCpqCCACvOhYNKXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1DcentLCwjZ2gLzYng0R6Oyv92MvSVB6z018jJG6ZNblRhzravEWpba0HEvAqZp1jsvyX8J5SFmslYjTGLO2R0Mp5yAlHktbF7KNZmPhcr8DBGkhc6tRNna4QJkmHaLbInfYs8J0vAZGf0bNn6kGRkLxxcffe7TRH9xdnqEgINkFx6CuhnNknmmQP_1ztHX0h5r2L2TkU2bOHWVpGal0j6DOhOxD861N9rzfHOmWlMNzf7l17To5mIYlBNjng9swrqY8yRMu4-EuTN6u_joZwS9tZUVjMD4Z5NupHhNd_3ENCT1k7PvAFqcqupcYEz_EgsmIgpxBD0885ZIAq-Egg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cMss02BQdF4NJyeMxnJmY_-Aqa9V1Z7WnZjDhSSRvincrhEbJ_eap-_DxNf36t7oEcGzgIhE-Ktne6oN--IvreUq3D6S9hbq8TfmQ4_Sbkgx8SMfrFiSGjJTykH92INo7PAjFzcdJnBEmOozzzQp_Qk3q4J5NujcZzQtjsep3FW-Alr5jKmiGuIb2FWX3R4blgJNpN3nXXPTNHAhFjlbWcXiHoQWhCChLUbZnOuin9chAnwCXIjlAhP7ueN7a8M4yNjMD0R_sGsBzq87JcZAYgdEdplu5tRnW2Q39-sViBvCtwMoKKc2-p9myFj_o3QgRU4nn7E8KO1zUomV_u2CDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤖
دالتون بات (Daltoon Bot)
یک دستیار هوشمند و متن‌باز برای ساخت، مدیریت و فروش خودکار سرویس‌های VPN (از طریق ربات تلگرام و پنل وب).
✨
امکانات کلیدی:
🔸
پشتیبانی یکپارچه از پنل‌های سنایی (3x-ui)، ریبکا و پاسارگاد
🔸
کیف‌پول داخلی برای شارژ حساب و خرید آنی اشتراک
🔸
داشبورد مدیریت تحت وب (React) با قابلیت کنترل چند سرور همزمان
🔸
مانیتورینگ زنده ترافیک کاربران و پشتیبانی از زبان فارسی
🚀
نصب سریع با یک دستور (لینوکس):
Bash
bash <(curl -Ls https://raw.githubusercontent.com/mdaltoon10/Daltoon-Bot/main/install.sh)
📥
سورس‌کد و راهنما در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7033" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7032">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🛡
معرفی فیلترشکن GRoute (جی‌روت)  کلاینت متن‌باز، سبک و رایگان (بدون تبلیغ) بر پایه Xray-core برای اندروید با پشتیبانی کامل از زبان فارسی.
✨
امکانات کلیدی:
🔸
پروتکل‌ها: سازگار با VLESS, VMess, Trojan, Shadowsocks و REALITY.
🔸
وارپ و آی‌پی تمیز: ساخت کانفیگ…</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7032" target="_blank">📅 19:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7031">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5UVL6uL7LiLx6qEd1QC3Q5P0oTiyC7XXroTnoQvDwdQUPzJIBLMR6m79dPGFNl5jElKeJgxhI7okiFjfwBfmGUD1UH776oBVfSBTqzMpIR6gnuKowYtrYpAgf-aKONUl1tfJVBdR_7WJHOmt2ltBxUK6zuRlC5H2QF0Svt9FND35UIWWe6fpOnfjSMMOfIVOJO5UIKZBkzZJ1zWHzFc2GXaJoAHHkc278FA85vBTcHCBUwHRAHkXYjqwK0QZI1Q-Uo-sDN78KqtsrhmKmxZk6DYC7hRfPGQeq2e34qH8VxytmaRtVklSiQTqlCImuqYIvNqLsMQEN31SPEG8wcuYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
معرفی فیلترشکن GRoute (جی‌روت)
کلاینت متن‌باز، سبک و رایگان (بدون تبلیغ) بر پایه Xray-core برای اندروید با پشتیبانی کامل از زبان فارسی.
✨
امکانات کلیدی:
🔸
پروتکل‌ها:
سازگار با VLESS, VMess, Trojan, Shadowsocks و REALITY.
🔸
وارپ و آی‌پی تمیز:
ساخت کانفیگ WARP با یک کلیک و دارای اسکنر داخلی Clean IP.
🔸
مقابله با فیلترینگ:
تنظیمات Fragment (ضد DPI) و Sniffing برای اتصال پایدار.
🔸
مسیریابی هوشمند:
تونل کردن برنامه‌های دلخواه و باز کردن سایت‌های ایرانی بدون مصرف ترافیک.
🔸
مدیریت سابسکریپشن:
آپدیت خودکار لینک‌ها و نمایش حجم باقی‌مانده.
🔸
ابزار تست:
قابلیت تست سرعت، پینگ و نمایش لاگ شبکه.
📥
دانلود فایل نصبی (APK) از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7031" target="_blank">📅 19:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7028">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMhDqUozHnbHESxnZImMIqQvdrJP_ftjJoRKIs-O_8pTyS7ZMif43-PSWAgbFA82_5aaLv_qwdrNLTic5i_H1LSPUBGSCbBRb2B09wSz68wPwlGhhvH97gA7iuiTNJU6eLC5FAzei8D-DQKjbyAl9hyaEF28G0stpb98e7NqFBS0vb0W1goLmA-uV4UNqA_lh2X2a-ixhLtZZJ7vFLLYJstl18eimYYZGpqu7dyY3zkTYdEQWen-tO1mTUlpA8OYDAZv7tNTI7n4td_sXPJVeTpJjY3cfiiukiIzsplYvpVG9SgtQxoiMcv7dzVOmGNx8n69SCKXsyyw6kRtsPOH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/op7UlxHQ-VpTOhZcjdeodFRUi0xIvK_oE6zwPwDe1Yh9KS8juunY3-NDP0xXUg4Pl2jBk_5yulCHmPz1kgLCruJOhaT59qK55cglSBJBEKHrQchAXpxwR0Oz2D84Mhp6FuR5GFfNveX0otchgiCilspqGMLqcxdOb5RCvlH6dUEEY4kag9WZI1YcKLhg7T8R9_nsPXPpEqUWAXmBLQ66NHKm4dxYfypNUvWfVBjcA671Ag3hr-8H_tF54yOj9NcJmvUb6LrDntfpWxj5AjA9qknrHg7KLdv_ewBjT1_jqTJzyViX0649KnCC22fU9qQxap5HyI8AfD60w218ICIskA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDFSWFkplHuP_ZKWOqYFBpCLI9E_hc8QaqjLjsMGKlmsDOIZaG-Stq4JDHwqBykGb6RINnv7hebtzRpBTcigAqwyb7xVpzmNNgCe15HIBz7rqY6dhl3sKdwTz609NWnG5dqq-U-kM2UoPerXRnyfoGOzmrR5apYJbmjXxrtc_Tn8iG8YJyQDfm7XEJ404fSQZAUtTn0dOJcdXBI_6LctepbdBMmlgTiI0-FNHOA8Oe6azS8CpZS1rnI4oHig0PP79HurhRBMInjxZWgvsPWty7MlU1FObRdnfnsvG8cut5TPauReTAgMVYq_c6G2RDhsJvoR3Na208PxKWmmJkJfyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
مجموعه‌ای از پرامپت‌های متنی، تصویری و ویدیویی رایگان و قابل کپی برای مدل‌های هوش مصنوعی مانند ChatGPT، Claude، Gemini، Nano Banana و Veo که امکان فیلتر کردن بر اساس نوع، مدل، دسته‌بندی و امتیاز وجود داره.
🌐
https://freeprompts.io/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7028" target="_blank">📅 17:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7027">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCmPGJzwZigNzeKC0LbyZZqExsF0EAJ1p3L5RQoJ6n_XiG3J_YfrvDm_pFr0jlLKW5lPgNPQEqQH4jsLXVIuH_pMZi51bYN4HDNWZcq2IN2ONCnz_cMVqX80LsHhWxnysFQWGAUglf_QpBI0gH7CkdtLCxfweMO5xa8exv8pzjEwskf1tUtOmfVuI2e3Kx90tS3Cm43Bzoje6-Mrthr5PqPAOq_8GiG2ZLR5i1ASSoFnoGS8DPm9uOI_XTI2LUXc7-iN7CFZXER8X5qE9-Nmo4-XTUIQNfADXvHSaOZe_kNu3kX9Et3mmnAgA6j-7KNnc3fE6g1I16qh4ArcUk7_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛠
استفاده از Claude Code با مدل‌های رایگان و لوکال
محیط Claude Code عالیست اما استفاده از API آن پرهزینه‌ست. ابزار
Free Claude Code
یک پروکسی هوشمند است که اجازه می‌دهد این محیط ترمینالی را به هر مدل دلخواهی متصل کنید.
✨
ویژگی‌های اصلی:
🔸
پشتیبانی وسیع:
اتصال بی‌دردسر به API سرویس‌هایی مثل DeepSeek، Gemini و OpenRouter.
🔸
اجرای آفلاین:
پشتیبانی از Ollama و LM Studio برای کدنویسی کاملاً رایگان با مدل‌های لوکال.
🔸
پنل مدیریت (Admin UI):
رابط کاربری تحت وب ساده برای تنظیم سریع کلیدهای API و تغییر مدل‌ها.
🔸
مسیریابی هوشمند:
امکان تخصیص مدل‌های سبک برای وظایف ساده و مدل‌های قدرتمند برای پردازش‌های پیچیده.
این ابزار روی ویندوز، مک و لینوکس به‌راحتی نصب می‌شود.
📥
سورس‌کد و آموزش نصب در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7027" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7026">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pO7D6qdO0IAXnu5Nxz6OeLKl5_6DftEMjpABkO6U7GofmmxtLYNR5oQ5QJDnCLWfp2GzFEHvTr71Ban7lIJ378RqZmla_w87FAdbe9DXBCF_nrL1yGAnuxFo9hxgaLiRq_FCHd-ALZewnd3TMYnMDZqcRooF_w-dlQDDCfiZV5z4S1guZs1VefRifTYlx2rCHi3CDTvYs5U0tMjGsiVEjtL_kihl9okDVoH6zUvoss65ZzDRtk66mENaw9pdDzHJzeLTKGS1YTPRiTQ41-PfKbT0v2tw_jJFeUVyoxLOp-WlC2BwbIfXAoReVKbjACSlLJ9NEDMPDoTfD6Oeinnrtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
معرفی و آموزش راه‌اندازی UAC SNI Spoofer برای ویندوز
یه کلاینت متن‌باز، سبک و دو زبانه (فارسی/انگلیسی) که با متد SNI Spoofing و هسته Xray کار می‌کنه. تو آپدیت جدید فایل‌های پروژه،
آموزش ساده و قدم‌به‌قدم راه‌اندازی
هم قرار گرفته تا خیلی راحت‌تر بتونید وصل بشید.
✨
ویژگی‌های کلیدی تو چند خط:
🔸
پروفایل اختصاصی اپراتورها:
تنظیمات کاملاً مجزا و بهینه‌شده برای همراه اول و ایرانسل (بدون تداخل با هم).
🔸
اسکنر هوشمند:
تست زنده و پیدا کردن خودکار سریع‌ترین SNI و مسیر.
🔸
مدیریت بی‌دردسر پروکسی:
ست کردن خودکار پروکسی ویندوز و بازگردانی امن اون بعد از بستن برنامه.
🔸
بهینه‌ساز یوتیوب:
استارت سریع‌تر و روان‌تر ویدیوها با قابلیت گرم‌سازی مسیر.
🔸
نسخه پرتابل:
اجرای مستقیم بدون نیاز به نصب پایتون (فقط کافیه فایل ZIP رو دانلود و اکسترکت کنید).
📥
دانلود نسخه پرتابل و مشاهده آموزش راه‌اندازی
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7026" target="_blank">📅 15:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7025">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBreak The Barriers</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3X-UI-MANUAL.fa.pdf</div>
  <div class="tg-doc-extra">3.8 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7025" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دفترچه راهنمای کاربری پنل 3X-UI ثنایی به زبان فارسی
✔️
راهنمای جامع پنل 3X-UI ثنایی که برای نسخه‌ی 3.5.0 نوشته شده است.
منبع:
https://github.com/yukh975/3X-UI-Manual
@break_the_barriers
💎</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/7025" target="_blank">📅 15:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7024">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoFhjQMhPO4IlU6VXOYWVh7pczDZBLm4mqh2ksMmO895rEU0FLULN1HBYOfb_9cQSo16dS4uPL1Y2ngtLKqyNfMjbxPw1I3LIT3hb6Rpd2YerfCoCuNi1e9Cm2coPWJrmXamnmkwhKX43MGTAOADs5W4ArOzugXdNGfDIv9YvcRxoa_Mr2n1kq0CZ72805g6s_wDKBNguvNN7IrnDi07-MymFZk_EF1E49uBgEwLXAEaTHE4FIK9S7qWjTxFZGfUfOYhVSguXNXRxFdDpNnFNpVZhztjbXUNn5tjDg4lhOePTxZIxJ5J5W-bQFsTn5sa-UAm8FEla1wGhQfDAe6aWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
؛OpenAI قابلیت جستجو در ChatGPT رو اضافه کرد که به طور همزمان در چت‌ها، پروژه‌ها، تصاویر و اسناد جستجو میکنه.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7024" target="_blank">📅 14:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7023">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">📱
معرفی Hermex؛ کنترل کامل هوش مصنوعی اختصاصی از روی آیفون  اگر با پروژه متن‌باز hermes-webui یک دستیار هوشمند اختصاصی روی سرور خودتون راه‌اندازی کردید، حالا می‌تونید با اپلیکیشن بومی Hermex، کنترل کامل اون رو روی گوشی آیفون خودتون در دست بگیرید. این برنامه…</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7023" target="_blank">📅 13:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7022">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📱
معرفی Hermex؛ کنترل کامل هوش مصنوعی اختصاصی از روی آیفون
اگر با پروژه متن‌باز hermes-webui یک دستیار هوشمند اختصاصی روی سرور خودتون راه‌اندازی کردید، حالا می‌تونید با اپلیکیشن بومی
Hermex
، کنترل کامل اون رو روی گوشی آیفون خودتون در دست بگیرید.
این برنامه کاملاً رایگان است و هیچ اطلاعاتی رو برای سرورهای واسطه ارسال نمی‌کنه؛ یعنی گوشی شما فقط نقش یک «ریموت کنترل» رو بازی می‌کنه و تمام داده‌ها و پردازش‌ها روی سرور امن خودتون باقی می‌مونه.
✨
ویژگی‌های کلیدی اپلیکیشن:
🔸
رابط کاربری بومی (Native):
ساخته‌شده با SwiftUI (مخصوص iOS 18 به بالا) با طراحی بسیار روان، بدون نیاز به واسطه‌های وب.
🔸
چت زنده و هوشمند:
ارتباط در لحظه با دستیار هوشمند، امکان ارسال فایل و عکس، و مشاهده روند استدلال و تفکر مدل.
🔸
مدیریت همه‌جانبه:
قابلیت مدیریت تسک‌ها (Cron jobs)، مشاهده مهارت‌های نصب‌شده (Skills)، ابزارهای آنالیز و بررسی حافظه مدل.
🔸
شخصی‌سازی کانکشن:
امکان اتصال به سرور از طریق HTTPS، پراکسی معکوس (Reverse Proxy) یا شبکه‌های امنی مثل Tailscale.
🔸
بدون هزینه پنهان:
فاقد هرگونه تبلیغات، سیستم ردیابی (Tracking) یا پرداخت درون‌برنامه‌ای.
📥
دانلود و اطلاعات بیشتر:
لینک نصب از App Store
(یا جستجوی Hermex)
🔗
سورس کد پروژه در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7022" target="_blank">📅 13:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7021">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ign_P40uifPcP_lsArWm1T9fyoiFnPyRsgkyZEbO2fiessXTdDw6l5ufpdSdVcA1a9P_H6cvJJGiZRmnad8ZuTkmSnAJS4i4e6MiXtCifO9N7inKigTckG5gQqlvjwj-k8quv8HwYNXtOJT2YcJfJfteNMt213KO9Z7AAbIgt03QO_oNFt6UgIU2EoxHozyokavhnX0AOMvzvFwxRpvmJB5VJekIpdbbXqecqxDc01ZjXej3Tm0h312Ba9hANaFwNeI7iTK6Mi0TWaYpZ9E7WhY2hSoVzhpkKLkW49c-geupAun3NYV93TwXFKBvJZKPruzCHus7InnEybZHqE7pkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7021" target="_blank">📅 13:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7019">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cetkIrvZdFFvI6XOABktjaagfBmysQuQ6VzjwBLQRDgK-jXq4MGFSA73Ahki35KJXE-_GKqchOhNNYZAvyGV7HLelyu3JNbAFvtFlb1nVwIanju4ObjC_JUj-6TLLNxzzPzNYrQGibjeBff_Bvx5KjKk5-KTi0u2QtJvDG4g1rcWl22d1ii547j8Tkxh7d3gz5dEFl-1v-LLWujdcDRHpcJrJsrjtZ47H88fhpHQMxe5QmritybhA37u_5Rk8TFrZDUkpYlOoqjw3vGfWvwzIcjkU3E_Yt3RfFviuHbmvuvhA8iNMitkU4LbvR3lEkEI4RVFEqVJDIgsaWFKeJoQpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">RohanKar Launcher
🎮
یک لانچر دسکتاپ برای اجرای مجموعه‌ای از بازی‌های کلاسیک
PC
که روی
Archive.org
منتشر شده‌اند. با این ابزار می‌توانید بازی‌ها را از طریق یک رابط کاربری یکپارچه مرور، دانلود، نصب و اجرا کنید؛ بدون اینکه نیازی به ساخت حساب کاربری داشته باشید
👤
مناسب برای علاقه‌مندان به بازی‌های کلاسیک که به دنبال دسترسی ساده و سریع به آرشیو بزرگی از عناوین قدیمی هستند
🎮
Github
🐱
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7019" target="_blank">📅 12:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7018">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k800JL3M4ql3JT71Xaa7zOzOSyA6tQaHHrwosbBvG5-vnEa6m4y_G8cb99o4hTnXcdhf5mcmD2TfM-pJyN5qwGu4vu6EtC1oSrzvmyP5qgyUrcNAZoK34_8g1XIC6Ahq4Ikz1voZCenBKLimYVfhHLwPSY6PvVvS7OWjH76C_aUD4Ysbx1FiDxJWINAe5WDtyA0AIpuX3ePmKU42UTuKakI6jXe31UvSuq2XpunbvIUO-wCjUOctNFFe0Fino4EufWLIxe34VcSros8gPTk3utDopTG1MgQ36b5DnArL5SGIA9uCsVwYseNld_qcb2P4ecsO5XU9OvQ_91kLZ0i4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
هوش مصنوعی برنامه‌نویس Grok Build متن‌باز شد!
شرکت SpaceXAI دستیار قدرتمند
Grok Build
رو در گیت‌هاب منتشر کرد. این ایجنت (Agent) هوشمند مستقیماً تو محیط ترمینال اجرا می‌شه و مثل یک برنامه‌نویس کنارتون کار می‌کنه.
✨
ویژگی‌های کلیدی تو چند خط:
🔸
همه‌فن‌حریف:
درک عمیق سورس‌کدها، ویرایش خودکار فایل‌ها، اجرای دستورات (Shell) و سرچ در وب.
🔸
انعطاف‌پذیر:
دارای رابط کاربری تمام‌صفحه ترمینالی (TUI)، قابل اجرا در اسکریپت‌ها (Headless) و اتصال به ادیتورها.
🔸
سبک و سریع:
نوشته‌شده با زبان قدرتمند Rust (دارای نسخه آماده برای ویندوز، مک و لینوکس).
🔸
متن‌بازِ یک‌طرفه:
کدها کاملاً در دسترس هستن (لایسنس Apache 2.0)، اما فعلاً مشارکت و ارسال کد (Pull Request) از سمت برنامه‌نویس‌های خارجی پذیرفته نمی‌شه.
📥
سورس‌کد و دستورات نصب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7018" target="_blank">📅 11:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7017">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XacBMRRAjnKYzczBUsqUyxXRjF5ef23iDwzuXy5iYVfiQ8kzH_jauU2r2E4lze5HQx9S2zU8ZFJTQiNl3S7cGB8gQfbvKrb6uBfEXzIgvU-mrIrs5y5k7wJt6tAXip0794Y84-VF5iQpvv64hxEo_N3aqUQwQjHlxPKOgiRpuVBipdUfF06tJRwoGBYZFofLjGmYPGn_0jB4GZD0OenovmKnXguiChEVM5qWVPGygn0BTzvVr-n2xWX8E8KGXmAOWeKPxlGrEcUU-AuNzcSNadZC62XjeMj_P3n_iAa2ke9GvAKOLamf790mI406cAr-IeGE3QmVW-_fxFHN5MMeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛ OpenCut جایگزین رایگان CapCut که متن‌بازه و مستقیم در مرورگر کار میکنه
🔥
🔹
این پروژه هنوز در مراحل اولیه توسعه قرار داره، توسعه‌دهندگان وعده دادند که امکان دسترسی به ویژگی‌هایی که در CapCut فقط برای مشترکین پولی هست رو فراهم کنند.
🔹
در حال حاضر تمام عملکردهای اصلی ویرایش، تولید زیرنویس، تنظیمات خروجی و .. در دسترسه.
🔹
به زودی یه کتابخانه از جلوه‌ها و انتقال‌ها و همچنین یک سرور MCP برای کار با هوش مصنوعی به این نرم‌افزار اضافه میشه.
🌐
https://opencut.app/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7017" target="_blank">📅 11:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7016">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8CH8UA7SIoTXIYf1LmvVbSMSCTwIbryzCFciYVYv7HNuGVUf0-qP8x0Ryxc1RsRhX4w-ZaWkHvnDODJ0ofhLnR2pHuyHH9HHebhT0yPHXtzsou83_J7glfslY31pAyDtiv5oabFUSxvWUbAf-uGILmIqRe69Dg_R3AxUSvEIiJWOShoWZg9-g9jaWVX2zLdDcV_Usv8vUQxVq1lZYGn1_4L-rzU5dECnzx9Sly83SAxWaLceBVHTiPiC7BJgvSdp5OCQ7wwxiBospPfqiLDV9naTmSCK-dF6djTykSAKl_MxMQCUAIgS5Og5PKX5DTuTSqkBlt2rMdPj3bacYbKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
یه کتابخانه عظیم از دوره‌های آنلاین رایگان
با CourseCorrect میتونی هر مهارتی رو یاد بگیری
🔎
فقط بنویس چی میخوای یاد بگیری؛
سیستم خودش دوره‌های مناسب از منابعی مثل Coursera، edX، یوتیوب و… رو پیدا میکنه.
✨
اطلاعات هر دوره:
🔹
زمان تقریبی یادگیری
🔹
سطح موردنیاز برای شروع
🔹
چت با هوش مصنوعی برای بررسی اینکه این دوره مناسب تو هست یا نه
🌐
https://coursecorrect.fyi/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7016" target="_blank">📅 10:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7015">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qw1d-UBiuqh3rz9MMYwItP4P3EK9Ynp4fWv5HtjTvmqWxCw4LNl2OpWhJQNcVxTldd911lJs5eQWednPxcG2Tu-1J1Uv4CshE4U9wKDlNmBMvaTdHPFCoz7MbCTX-wY4EzapA1pGGjm3LXs4b8VjxjcwQIcdRgEGnl5w4kv-B3fyYeEDZW9Kl9gwth-OZNQGMvOEZux85wx2CYIikzyfgozBIDjXK-L5VB9LzOV0FKAia9o36zmT7VCaJqFwjXdloLcqvGXpudtOY_DKVJh1npHuz0yGxaYntP4GR2D8TszVpDcBss4QJM8qHR1YJqcKEB3_nZOeosWsRKIJ9si9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔓
دور زدن محدودیت‌های پولی مقالات با یک کلیک!
این افزونه مرورگر به شما کمک می‌کنه تا بدون نیاز به خرید اشتراک (Paywall)، به متن کامل مقالات در سایت‌های پولی دسترسی پیدا کنید.
✨
این ابزار چطور کار می‌کنه؟
🔸
فریب سایت‌ها:
افزونه خودش رو جای ربات‌های موتور جستجو جا می‌زنه؛ در نتیجه سایت‌ها تصور می‌کنن با یه ربات طرفن و کل محتوا رو رایگان نمایش می‌دن!
🔸
استفاده از نسخه آرشیو:
در صورتی که سایت خیلی سخت‌گیر باشه، افزونه به‌طور خودکار می‌گرده و نسخه ذخیره‌شده (Cached) همون مقاله رو براتون پیدا می‌کنه.
🔗
لینک دریافت افزونه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7015" target="_blank">📅 09:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7013">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6514ad748.mp4?token=JohjPBrHpXboQ0eXUhAoWjgKblDa_QJxXuD16hbyIYusC1e1Ibkwk-pgA2ttFK2EUxEHLl-yZlhqXP-bZ-pw5RwVaEQgsKU5g3QK015y_Ig6l3T4xAM-fZWTMvUnSIadt2vL0fJNFG4I5k2zg_kDYx7KxTubG5ZJUPEpUBSWQbiWVz0T3tjqBSsmRCTfGkvwO8tBw8ZJvzUPYRmavEbLu8TbvV6ucZhxePh80CnCd0J0D4ladC_TkmzgGWjvG8Zs5PEhQTimhI2EpRCIhhMxA3iLaRXVjKbalCg2z_j7aL6JKi1wIbdgHdfQkQQR3UTu4xQixvVH605QJyk5xKw0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6514ad748.mp4?token=JohjPBrHpXboQ0eXUhAoWjgKblDa_QJxXuD16hbyIYusC1e1Ibkwk-pgA2ttFK2EUxEHLl-yZlhqXP-bZ-pw5RwVaEQgsKU5g3QK015y_Ig6l3T4xAM-fZWTMvUnSIadt2vL0fJNFG4I5k2zg_kDYx7KxTubG5ZJUPEpUBSWQbiWVz0T3tjqBSsmRCTfGkvwO8tBw8ZJvzUPYRmavEbLu8TbvV6ucZhxePh80CnCd0J0D4ladC_TkmzgGWjvG8Zs5PEhQTimhI2EpRCIhhMxA3iLaRXVjKbalCg2z_j7aL6JKi1wIbdgHdfQkQQR3UTu4xQixvVH605QJyk5xKw0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
انتقال فایل بین تمام دستگاه‌ها با PairDrop (بدون نیاز به نصب)
ابزار متن‌باز و تحت وب
PairDrop
سریع‌ترین راه برای جابه‌جایی فایل بین ویندوز، مک، لینوکس، اندروید و iOS است.
✨
ویژگی‌های کلیدی:
🔸
انتقال محلی:
شناسایی خودکار دستگاه‌ها در یک شبکه Wi-Fi.
🔸
انتقال از راه دور:
اتصال دستگاه‌ها در شبکه‌های مختلف فقط با یک کد ۶ رقمی.
🔸
امن و مستقیم (P2P):
ارسال فایل‌ها بین دو دستگاه بدون ذخیره در هیچ سرور واسطه‌ای.
🌐
اجرای مستقیم:
pairdrop.net
🔗
سورس در گیت‌هاب:
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7013" target="_blank">📅 08:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7012">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHz2XytyoDjiP7XZrfJf80I_iE5TAltoyTK1Zfg9BXx6Q1OLA18bZo0PqDPrx7Sy7yrRiF_HpqhEU2rm0UcXeFdyAKVntzpGB9r5mFXCAD6MuWT4oXwLTEOaeJA7pkD7kGqczjRJQJ4kMmQuV6AUj0vZ525zvZElMawM0P_Bqmwo_rA7zQ8zD8OkfP9_0Rb_GJWHG8bAtNV4NX-hP4R71xbpMBODgPOVSdxAK7NtsrDLpb3VDt43RaHOnAJJhlsuB91p9Wj-rXshOlULLOYBfx3suvHMeMj2G8h4CJ0qAfJDpN9tFyb-yZf465k4NhlgXzYTOK95IU79JjqJEpPbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دریافت اکانت ۳ ماهه رایگان Avira VPN (نسخه Prime) (
تست نشده)
یه فرصت عالی برای دریافت اشتراک ۹۰ روزه و کاملاً رایگان فیلترشکن قدرتمند آویرا، بدون دردسر و خیلی سریع!
✨
مراحل دریافت اشتراک:
🔸
مرحله اول: وارد لینک کمپین آویرا بشید و با یه ایمیل (واقعی یا موقت/فیک) ثبت‌نام کنید.
🔸
مرحله دوم: ایمیلتون رو تایید (Verify) کنید و یه پسورد برای اکانتتون بسازید.
🔸
مرحله سوم: وارد داشبورد بشید؛ تو بخش وضعیت اشتراک (Subscription Status) می‌بینید که اکانت ۳ ماهه شما آماده استفاده‌ست!
📥
لینک دانلود اپلیکیشن از گوگل‌پلی
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7012" target="_blank">📅 02:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7011">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fi7jRVJ942TvK8o0UUS50V1ADYjr-4OIBtHdy6fa69c1bBZUaBrHVMeNXDZ5yaCK8ICjXoPSAP6Ezvp_Vy8HFOw6wo9UMma6-zI3qgRJMaXL4qUJ5aq_b0u1RFQ48Gyizm5lrnoERwujNC_gGAsc378S_gtPguzU1OAfvSpPLt94Rs4H22cQTFxc_VpbXWLykjMHfcOxZUxwsvuRCuNo42b7Uejy_9OKBGjFjFuc5baEpWnKOWyWhC-KlBSqZu6E_lQ2pDb9IW-cB5nuTqKW_kpfAVseid-NhCGpnwCBHx1u2FTg-6Bzr6FbU8wku-dQQTZiwRpnyDV3vKLBHwBcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار از زندان DeepSeek
👇
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7011" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7010">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🛡
آموزش ساخت کانفیگ Bepass (متد یوسف قبادی) روی Nekobox  این روش کاملاً با پنل‌هایی مثل نهان یا BPB متفاوت است و با استفاده از Worker کلودفلر و پلاگین اختصاصی Bepass روی نکوباکس کار می‌کند تا نتیجه متفاوتی برای دور زدن فیلترینگ به شما بدهد.
🛠
مراحل راه‌اندازی…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7010" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7009">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🖥
نسخه گرافیکی ویندوز فیلترشکن Aether منتشر شد (آپدیت v0.3.0)  اگه یادتون باشه قبلاً ابزار خفن Aether رو معرفی کردیم که بدون نیاز به خرید سرور، فیلترینگ رو دور می‌زد اما محیطش متنی (ترمینالی) بود. حالا ابزار Aether-GUI اومده تا همون قدرت رو با یک رابط کاربری…</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7009" target="_blank">📅 01:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7008">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🖥
نسخه گرافیکی ویندوز فیلترشکن Aether منتشر شد (آپدیت v0.3.0)
اگه یادتون باشه قبلاً ابزار خفن Aether رو معرفی کردیم که بدون نیاز به خرید سرور، فیلترینگ رو دور می‌زد اما محیطش متنی (ترمینالی) بود. حالا ابزار
Aether-GUI
اومده تا همون قدرت رو با یک رابط کاربری تر و تمیز و فقط با یک کلیک در اختیارتون بذاره!
✨
امکانات برنامه و تغییرات این آپدیت:
🔸
خداحافظی با ترمینال:
دیگه نیازی به دستور زدن نیست؛ یه دکمه Connect می‌زنید و تمام تنظیمات و اسکن‌ها تو پس‌زمینه خودکار انجام می‌شه.
🔸
ارتقا به هسته جدید (v1.1.1):
مشکل اتصال فیک کاملاً حل شده؛ پروکسی SOCKS5 فقط زمانی فعال می‌شه که تونل واقعاً تست شده و ترافیک رو عبور بده.
🔸
ریکانکت هوشمند و اتصال سریع:
برنامه آخرین مسیر سالم رو یادش می‌مونه تا دفعه بعد بدون اسکنِ کامل، درجا وصل بشید. اگه اتصال هم قطع بشه، خودش خودکار ریکانکت می‌کنه.
🔸
فوق‌العاده سبک:
مشکل مصرف پردازنده برطرف شده و مصرف CPU برنامه وقتی مینیمایز (تو بک‌گراند) باشه تقریباً صفره!
🔸
پنل پیشرفته:
می‌تونید پروتکل‌ها (مثل MASQUE یا gool) و نوع اسکنر رو خیلی راحت با رابط گرافیکی تغییر بدید.
این نسخه در حال حاضر برای
ویندوز
(فایل‌های نصبی exe. و msi.) آماده شده است.
📥
دانلود فایل نصبی (از بخش Releases)
🔗
صفحه اصلی پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7008" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7007">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUcAiSBEfsGVDF94NRjiuYdk8mWsPqqGV5HLUBUa-ebWLxSN1sdFxylKXG5lp9rGWgPOGmTHn7aA4W7t0Y6J3p8B4xeACwDUh31K4j3jjOpHusTM0DTE6pd5Duh5HyXPiSeZJId64weD8G_sTMBjEUCHanCPUJAr1jllwOTxzddBVd1VKXTRkFeO3ktg0Qx8b5hXUJkAx02XkxleksgZ5_34s0aWHvRTQV-ytiLX7nl-2kE7WT4ER7vRZW4BxWe25UEZUc-potmadybgk2lYk49JxwlTxgV9N3zS4_rbeMhPNmC0qjkX-BsiDPUFrEb0UGl-tRJMemGB3CvIj4RRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید و خفن Aether (نسخه 1.1.1) منتشر شد!  تو این نسخه کلی از باگ‌ها برطرف شده و امکانات جدیدی اضافه شده که اتصال رو خیلی پایدارتر و راحت‌تر می‌کنه.
✨
تغییرات مهم این آپدیت در یک نگاه:
🔸
خداحافظی با اتصال فیک: مشکل وصل شدن ظاهری برطرف شد. پروکسی SOCKS5…</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7007" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7006">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه  پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز…</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7006" target="_blank">📅 23:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7004">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🛡
آموزش ساخت کانفیگ Bepass (متد یوسف قبادی) روی Nekobox
این روش کاملاً با پنل‌هایی مثل نهان یا BPB متفاوت است و با استفاده از Worker کلودفلر و پلاگین اختصاصی Bepass روی نکوباکس کار می‌کند تا نتیجه متفاوتی برای دور زدن فیلترینگ به شما بدهد.
🛠
مراحل راه‌اندازی در چند قدم ساده:
🔸
۱. نصب پلاگین: ابتدا پلاگین Bepass را دانلود کرده و داخل برنامه Nekobox (نسخه ۱.۳.۴ به بالا) فعال کنید.
🔸
۲. ساخت ورکر: فایل Worker را دانلود کرده و یک ورکر جدید در Cloudflare بسازید و کدها را داخلش آپلود کنید.
🔸
۳. تنظیم آدرس: به انتهای لینک ورکری که ساختید، عبارت /dns-query را اضافه کنید.
(مثال: https://name.workers.dev/dns-query)
🔸
۴. ساخت کانفیگ نهایی: لینک به‌دست‌آمده را داخل «فایل خام» که در این لینک (Rentry) قرار دارد، جایگذاری کنید.
🎁
راهکار سریع‌تر (کانفیگ آماده):
اگر زمان یا حوصله ساخت کانفیگ را ندارید، می‌توانید مستقیماً از کانفیگ‌های آماده‌ای که در همان لینک Rentry
قرار داده شده استفاده کنید (فقط فراموش نکنید که حتماً باید پلاگین را روی نکوباکس نصب داشته باشید).
با تشکر از یوسف قبادی عزیز
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7004" target="_blank">📅 23:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7002">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp5Y-qXIBYyNrO5oy3R-ehyTbYtzJo6lnQyZfiTvB24z_QlSEKFl5sF2eeEzEWcL890dUafQMEu6voFcFBZK6bcAOJkBzjkbZ9iznFaw0KQICaRkis8KBU08sWE2bLQJz7MWjCJ20NATZ3k0FGQQtHtRzNB-CSJDaY_YQpAIp1pqmzhxFBt5bK_IYtuIEYbJ7_09C7HCtWuRzyfhX5JQUt9y6ai6GMZWCVNn4iYPAZA-OevTkwH4TafvWo8Sayl0WTAMZZ3QmIwdHI--B3KZtArUndKktTunYqEcULDlMmMEakPxh3ytMySTD26qe_7Q2LgwsN46L4TLIG_j3jWbdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
معرفی Consensus؛ موتور جستجوی هوش مصنوعی برای تحقیقات علمی!
اگر دانشجو، پژوهشگر یا حتی یک فرد کنجکاو هستید، Consensus یک موتور جستجوی مبتنی بر هوش مصنوعی است که پاسخ سوالات شما را مستقیماً از دل مقالات و منابع معتبر علمی پیدا می‌کند.
✨
ویژگی‌های این ابزار در یک نگاه:
🔸
دسترسی به پایگاه داده عظیم:
جستجوی هوشمند در بین بیش از ۲۰۰ میلیون مقاله و سند علمی معتبر.
🔸
پاسخ‌های مستند و واقعی:
ارائه جواب‌های کاملاً مبتنی بر فکت و شواهد علمی (به دور از اطلاعات زرد و نامعتبر اینترنتی).
🔸
استخراج هوشمندانه:
پیدا کردن مرتبط‌ترین تحقیقات و استخراج نکات کلیدی آن‌ها در چند ثانیه.
🔸
کاربرد همه‌جانبه:
یک دستیار عالی برای نوشتن پایان‌نامه، مقاله‌نویسی، یافتن جدیدترین دستاوردهای پزشکی و تحقیقات شخصی.
🔗
آدرس سایت:
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7002" target="_blank">📅 23:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7000">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWN2qShXxAHsVKWpQjbZRHEHPwHYveCbLVJrB7qq8dY-1JN_PfGswtSoLeu_tcuDEbvJfHmi3D3-x9ThrlWGz7i_cxuYaDr5Sw8EdQrDStu90PHoyxzh1GrhJF394Kp9vbAeHcVJImJdU0hI0XEHULkr44AvoExQOa5Rq4-rAepeZT3vb8DPax7kyhAOHfuGIqkICP04vjUQkeXSJPNB9z56-4RK4x61rQ1QuZcAKKQFnuC2FRCGOPaMbLlcFc3XNVCwFi8vRk699_EPE9qqTtOQKTkDXNU2u-syyOt7Y8jdEG5GzeEPzZ1wqmv4FDtu8Jz84auTKhrc5WHQwL6Pkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📦
Universal Installer؛ همه‌کاره‌ترین نصاب برنامه‌های اندروید!
اگر زیاد برنامه‌ها را خارج از گوگل‌پلی دانلود می‌کنید یا با فایل‌های چندتکه سروکار دارید، این ابزار متن‌باز جایگزین بی‌نظیری برای نصاب پیش‌فرض گوشی شماست.
✨
ویژگی‌های اصلی در یک نگاه:
🔸
نصب هر نوع فرمتی:
پشتیبانی کامل از APK, APKS, XAPK (همراه با OBB) و APKM.
🔸
نصب خاموش و گروهی:
نصب و حذف بدون نیاز به تایید مکرر (نیازمند Root یا Shizuku).
🔸
جعل هویت (Spoofing):
گول زدن سیستم برای اینکه فکر کند برنامه از گوگل‌پلی نصب شده است.
🔸
شخصی‌سازی نصب:
امکان داون‌گرید کردن نسخه‌ها و دور زدن محدودیت‌های SDK.
🔸
سد امنیتی:
اسکن خودکار فایل‌های نصبی توسط VirusTotal.
🔸
انتقال محلی (LAN Sync):
اشتراک‌گذاری و نصب راحت فایل‌ها بین دستگاه‌ها از طریق Wi-Fi.
🔸
طراحی و پشتیبانی:
رابط کاربری مدرن (Material 3)، بدون تبلیغات + نسخه مخصوص Android TV.
📥
سایت رسمی جهت دانلود (گیت‌هاب، گوگل‌پلی و F-Droid)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7000" target="_blank">📅 20:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6997">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Txso15ZK7vJ1e7k_uO-1foYkl3jZuL6FzTvCo8aHxhTBaoNuhfGil4CFqKvEDfzZ3FWvAhq6okGRYWVcJwp3rdAeqb7-r4tFMPdKTvcN0huYUplJ79SeJj8FWVrblnqfo3cJ-wTbWucuO5FHU4O0s9nB-hk0061jK9QFQ8k9lMmHyN88BYnXuTVdNWHH13y0j2pAcu6yC9Enzm-IuRZarPWcfWIbqIBj2Fz99Wjxw811unXhus4YDBTVRTli7UNfvNn5CByIhM79pl7Cnhc2PtUItZeHpVZBdDI4uesXDytlKnUd2FOaTAgrxdUeBf5jZ5HhHwg7YgM3DI7wb7tJ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjriC9lt4s5Tl7SKsmsaZVbQh8PfYxQVRlXdysv9LQSywkwVQQIewb9y2v3s5GXe23dyMq8EjPAFfuo8YHKWy3Tfxb3Bbc5vsOjbOQgrjV29U2kfICCxsfcG9n7ceCIIajNnqEfSIgo_XVLSZ6bwfsmiakIN9XWyxj-zSWZfvY-iu9z1z6UWSEymdAyG4dzK2eF0qPNIaa3kOHo5cspt_MCPEnuXaE_gUwkTVTwSFQzhi_PSZLuuG2NHZYZ87HeHr3qLoQvGx5IKlVYfJHs-p-wUQTC5Ox9YPLBeOcZaCuRNV7jTyjWHqsHh8yuaJ6PeQ7dSSubYnjaVYhHQH4zVMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
گوگل برای ۲۵ سالگی Google Images سورپرایزهای بزرگی
معرفی
کرد.
🔹
تولید تصویر با مدل Nano Banana 2 Lite داخل Google Images
🔹
طراحی جدید و مدرن صفحه اصلی
🔹
گالری شخصی‌سازی‌شده شبیه Pinterest که با توجه به سلیقه کاربر تغییر می‌کند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6997" target="_blank">📅 18:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6996">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRB2eoIDB0nbdl9qmBum5Q8BKQI42OuGELFso4k0aU0CnOJbRJVE_r-8ISkHalmrobJETi8nVmYV4ivSJDHH_rS1IC_pLnAWTMQzPWZLsn5iG-a0Ng2s4nV0v20hGvaZG2oaMf4nyPlU5AtwYDUVIZM1L51lm_PZ6jL9LAIdZigO9I5OwGF7AQd_Cyx7EpXdcWI8YcCBl-ykMcHYVjtelJseWz4bT4cJUgPNx-QOWzd4V5FJCrdPNzFv0AVfCbzUY4b5vcX1mu2AC8tRgKv1ZMdq_6AMlw9jNYlgpZPXq3WSPGWhBDWjKwjt35QSgrj_s8EDwC7t_THhLHa965JhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثه آب خوردن  کلا ۱۰ ثانیه هم طول نکشید
😐
ولی وصل نشد رو ایرانسل برام
😐
😂
😂</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6996" target="_blank">📅 17:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6995">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtAnmzfpAU7iXR-d69_yl_uXltjcngqAy8vIoH1KPQ1Fqu5UffKh30OaggvjW2PIUZJ1CQHRW38lnsxt98-ZPsM4up_Sg8uKjG_YA7s2rlCAC1Aie5VQWWyB1Ks5wH0YwoUhyqM8z7aSoSiBUoYwehkuI-1qVxO_sniwKJczHYr1bNsVAPyBHQwlHuYndY1NIUk92wqUdnv6ARxsjZVonQ6cD995wIbJRWjeMgjF1wZ7p2GIPb7DiugrIPOZl8LkVcw19VeydpjBNHFhyLvRxE_Z-SnRPES3jOJFSDRK3pwlznAWeBnNzfOmKVeG7iqupRXZv657FpyktLoLH_s3lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه  پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز…</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6995" target="_blank">📅 17:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6994">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه
پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز می‌کند.
✨
ویژگی‌های کلیدی:
🔸
بدون نیاز به سرور شخصی:
سیستم به صورت خودکار سرورها و مسیرهای سالم (Endpoints) را پیدا کرده و متصل می‌شود.
🔸
پنهان‌سازی ترافیک (MASQUE):
ترافیک شما در بستر HTTP/3 و HTTP/2 کپسوله می‌شود تا کاملاً شبیه به وب‌گردی عادی (HTTPS) به نظر برسد و مسدود نشود.
🔸
امنیت مضاعف (gool):
علاوه بر پروتکل WireGuard، از حالت وایرگارد تودرتو (Nested) برای ایجاد یک لایه رمزنگاری اضافه پشتیبانی می‌کند.
🔸
کراس‌پلتفرم:
دارای نسخه‌های آماده برای ویندوز، مک، لینوکس و اندروید.
📱
نصب سریع در اندروید (از طریق Termux):
برای نصب خودکار، کد زیر را در محیط Termux کپی و اجرا کنید:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
پس از اتمام نصب، کلمه
aether
را تایپ کنید تا برنامه اجرا شود.
ابزار پس از اتصال، یک پروکسی SOCKS5 (به عنوان مثال روی لوکال‌هاست و پورت
1819
) در اختیار شما قرار می‌دهد که می‌توانید آن را در تلگرام، V2ray، Nekobox یا تنظیمات سیستم وارد کنید.
📥
لینک گیت‌هاب (جهت دانلود نسخه ویندوز، لینوکس و مک)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6994" target="_blank">📅 17:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6992">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2SLK30qHe8ktvjVtHjVVwakiBKJ0eXXUGZrwX2_Nkp2gMFyVQtqtdUqqAhl9QkjOi8cGVpY_f29LGSUHJVeEhl4Xh_ze6vcavowZpLopDzJeP2khAl1IqwBBwop92LLykHDcjaRlt_NxFiNPbj4K3W7hi26tbd2uEt733BSNNRR8dF2T7_3KeuPQdjmdrqXGUw-DZ3VBQcf43akchVjbFwhYtPviJOc1yDf-sItOkWJMErIDBkKBOCNTJCDpBYbS3AOddByhBqLfA_-0znRLMb3MWmcpfEdBAvgCFrehcHU_pcSEXX2lZKO_yqb7gy8p1HAl9UmzDAAZngADpa3wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
اشتراک یک‌ساله و رایگان MultCloud (ارزش ۴۰ دلار)  مولت‌کلود (MultCloud) ابزاری بی‌نظیر برای مدیریت یکپارچه تمام فضاهای ابری (گوگل درایو، وان‌درایو، تلگرام، دراپ‌باکس و ۳۰ سرویس دیگر) در یک پنل است. با این ابزار می‌توانید فایل‌ها را بدون نیاز به دانلود و…</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6992" target="_blank">📅 16:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6991">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-dOY5S7Uxv5kIABmbEUW3s3moVG8ZnSJ5Je6c-tedcqgBjXS4bJqhss_dygbchNvhmsMyyLHmZ4fdeRgg1c_PV-ZnPicTS9q6qbT6FWoFVanr6VwubSMYqDS5ZEiFoy3ZLWBedUeNXbJfS0RoYl8WAAOBjka6ors3PUdZoO01KVdYqx8SD3ug5birheVNSwbpTUqhaeZZ-7id07k_prwZpiIjOLN85cMsn6MWSE9m_2J4ZEJT9utJswpXSVFpyoVx5n2cdEPFmaJg87WpV8ZR8CLoaGaxRC0z-oeylqCv0uD2VZR5gySpvW_9L1yWP__6epOyV0uRpx3qVTdwoMzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
اشتراک یک‌ساله و رایگان MultCloud (ارزش ۴۰ دلار)
مولت‌کلود (MultCloud) ابزاری بی‌نظیر برای مدیریت یکپارچه تمام فضاهای ابری (گوگل درایو، وان‌درایو، تلگرام، دراپ‌باکس و ۳۰ سرویس دیگر) در یک پنل است. با این ابزار می‌توانید فایل‌ها را
بدون نیاز به دانلود و مصرف حجم اینترنت
، مستقیماً بین فضاهای ابری مختلف منتقل، سینک یا بکاپ‌گیری کنید!
🎁
نحوه دریافت اکانت پرمیوم ۱ ساله:
🔸
وارد لینک زیر شوید و یک حساب جدید بسازید.
🔸
در پنل کاربری، از منوی بالا روی آیکون کلید (
🔑
) کلیک کنید.
🔸
کد پروموی زیر را برای فعال‌سازی وارد کنید:
BAAYK667N5K3K0N6
🔗
ورود به سایت
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6991" target="_blank">📅 16:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6990">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5760952ca.mp4?token=ZX1xpgjaUYpr-ml1rKQnIMlqaeGtyy2t1rW2MSfoOCN61SmFJhHW3gu4cukYW807fwODjkj1ysW-K40zISdxX6WSXKMuEM8PKtGYouL0D0VdptoHS_0g0YvWj9Y9O6oTFAOBxB2nf5MLJLM6ZFRflOqx4TI9cj8aBpr7eF0Rkm97kMDlpTZzO9hX8NnsaFzKsFDUsncvZmlb5ed_iu3_8xkDSGMS3pMIHDcxoVVHLLhEj3qU7V24RjRScz_zXbjEhUmuJYJA-EcsrmwxcQ-SeilkYeYmS64Ry_x1N-YdRjuqp9_YAgwr9-6h2rg7rMIA1vf9a_Istw1K9Qy2Nmkmug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5760952ca.mp4?token=ZX1xpgjaUYpr-ml1rKQnIMlqaeGtyy2t1rW2MSfoOCN61SmFJhHW3gu4cukYW807fwODjkj1ysW-K40zISdxX6WSXKMuEM8PKtGYouL0D0VdptoHS_0g0YvWj9Y9O6oTFAOBxB2nf5MLJLM6ZFRflOqx4TI9cj8aBpr7eF0Rkm97kMDlpTZzO9hX8NnsaFzKsFDUsncvZmlb5ed_iu3_8xkDSGMS3pMIHDcxoVVHLLhEj3qU7V24RjRScz_zXbjEhUmuJYJA-EcsrmwxcQ-SeilkYeYmS64Ry_x1N-YdRjuqp9_YAgwr9-6h2rg7rMIA1vf9a_Istw1K9Qy2Nmkmug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
نتفلیکس شخصیت رو تو چند دقیقه بساز!
با Reiverr همه فیلم‌ها و سریال‌هات رو یکجا و مرتب داشته باش:
✨
امکانات:
🔸
جست‌وجوی هوشمند با پوستر، تریلر، امتیاز و توضیحات
🔸
ادامه تماشا از همون ‌جایی که متوقف شدی
🔸
پیشنهادهای شخصی برای وقتی نمیدونی چی ببینی
🔸
رابط کاربری مناسب برای تلویزیون
🔸
اتصال به تورنت‌ها و سایر منابع دانلود
🔸
نصب روی کامپیوتر یا سرور شخصی تنها با یک دستور
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6990" target="_blank">📅 12:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6988">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👱‍♂️
پروژه Ponytail
برنامه‌نویس ارشد تنبل برای هوش مصنوعی شما!
✨
ویژگی‌ها:
🔹
جلوگیری از پیچیده‌نویسی (Over-engineering) توسط هوش مصنوعی
🔹
کاهش حجم کدها تا ۹۴٪ و صرفه‌جویی ۲۰٪ در هزینه‌ها
🔹
افزایش ۲۷٪ سرعت انجام وظایف، همراه با حفظ امنیت کد
🔹
اولویت دادن به کدهای موجود و کتابخانه‌های بومی، به‌جای تولید کدهای اضافی
🔹
سازگار با بیش از ۲۰ دستیار هوش مصنوعی، از جمله Cursor، Copilot و Claude Code
📥
گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6988" target="_blank">📅 12:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6986">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏
🤖
پروژه Hermes Agent (نسخه اندروید)
🔥
پیشرفته‌ترین ایجنت هوش مصنوعی خودآموز (Self-improving)!
✨
امکانات:
🔸
پشتیبانی از انواع مدل‌ها (OpenAI، OpenRouter و مدل‌های Local)
🔸
اتصال مستقیم و مدیریت از طریق تلگرام، دیسکورد، واتس‌اپ و اسلک
🔸
حافظه بلندمدت، یادگیری…</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6986" target="_blank">📅 10:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6985">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9mA-VsaAckJSAmidqPZTR1ay--4CMXw39MAMSCSAvKdAQ1562BjuBuGu2o_JpVH3MLiroYfSmzJ7kEVrPOetOgVwZitjHPckUVfPzEnTE_KSclOIuzFncSTgtd5yNqp8SzIOkCYj35FWQfS8rbZcclR3MPZD0f3g3lyE4kU7Y78AUCG9XnLc87ftFywTKKOnSVHCZ1p6WQ-o3Y5-ToTuHRIl6NW16HGWa5BSJJhBPwMXVUN5Jey4WvqotIjsgZeWJ1qaWy2Fud9ivhcWPCMuxk0FZVNee9XrNsc6yiEXRjPi_oDgwoRMFLhd7KqL5TAxdva76npaBYH5aiwiq3cpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤖
پروژه Hermes Agent
(نسخه اندروید)
🔥
پیشرفته‌ترین ایجنت هوش مصنوعی خودآموز (Self-improving)!
✨
امکانات:
🔸
پشتیبانی از انواع مدل‌ها (OpenAI، OpenRouter و مدل‌های Local)
🔸
اتصال مستقیم و مدیریت از طریق تلگرام، دیسکورد، واتس‌اپ و اسلک
🔸
حافظه بلندمدت، یادگیری خودکار و ساخت مهارت‌های جدید
🔸
اتوماسیون و زمان‌بندی وظایف (Cron) فقط با زبان طبیعی
🔸
دارای اپلیکیشن بومی اندروید برای اجرای مدل‌های آفلاین (Gemma و Qwen)
📥
دسترسی و نصب:
GitHub
,
F-Droid
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6985" target="_blank">📅 10:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6984">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJPLy0Z7Vfx3_ci36Y4PryfV734PCNbv7gp0LHoJwtdwpKLXGpZE8mBKH-4L3pgsjEME26qqhHE-lp_rhzuVSKEhFV42TM37NdTQAdxrDMhKDktmnewCPu6q3MH132v6vZW6crfIuNPxdgg9Ce1mXTEOvW4lJYx9N-AqSZ6f5dFhyXKa74nR6Edht9w__E3EDpNNP2e6wAwLlXkoPdlGGmepe2OS31v2slwaHCvmJjUxs_xdTc5hj9wDwzHR6Tid0HXdPC5B-DcfF71PvOImJFv1TYZivymMFDpcGhgqs4Asb1noOuuwUY5fjXuufubyzaJvpDkcuYvdQ0GiplDJAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💎
Google Gemini API
دریافت رایگان توکن‌های هوش مصنوعی گوگل!
✨
امکانات:
🔸
دسترسی به مدل‌های Gemini 2.5 Flash، Flash-Lite و Pro
🔸
بدون نیاز به کارت اعتباری یا اشتراک
🔸
ساخت کلید API رایگان در چند دقیقه
🔸
توسعه اپلیکیشن با جدیدترین مدل‌های گوگل
📥
دریافت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6984" target="_blank">📅 10:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6983">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnCdX6nAi94gDX5LRQo2Xf0jvjxlq01BdBxraQhrSyDt7_A0-BCWxAiv20plnEA1bZiiAaRNXr-tXeE7Zu7gqMoDAmD1pAf3YyA9YxzTEg9kLtun2EM2ZWVg2BAVTGZpn8IhTWxDRdl_nL9M5KfZePiOqvibZ5rXruuLQccg0H0QvLrqR6I4o_rczH3LVG8xlUlvlqNJ4Fjgq78Jt6D7_kkdIs1wIbPL6O7RfCQyxnZcHyCL9ZX9C-wByYW2nwZsVN1g-9uqn_ci6x1aQ9PuTlOxZPrXjox4Dcaew8krtWCrQ6nmvQse3lRmc9Hkh6xRZj8xHZSuL5S3YNTYE4hg1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
هفته توسعه OpenAI
شرکت در رویداد و دریافت ۱۰۰ دلار اعتبار رایگان Codex!
❓
نحوه دریافت و جزئیات:
🔸
ثبت‌نام و ارسال درخواست شرکت در رویداد از طریق پلتفرم Devpost
🔸
مراجعه به تب منابع (Resources) در صفحه رویداد
🔸
کلیک روی گزینه "درخواست 100 دلار اعتبار Codex" و ثبت آن
🔸
مهلت ثبت‌نام:
تا ۱۸ جولای ۲۰۲۶
🔗
ثبت‌نام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6983" target="_blank">📅 08:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6981">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏
🛡
مرورگر Cromite (کرومایت)؛ جانشین قدرتمند Bromite  (جایگزین کروم)  اگر از طرفداران مرورگر محبوب اما متوقف‌شده‌ی Bromite بودید، Cromite دقیقاً همان چیزی است که نیاز دارید! این مرورگر یک نسخه سفارشی (فورک) از کرومیوم و بر پایه برومایت است که با تمرکز شدید…</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6981" target="_blank">📅 02:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6980">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏
🛡
مرورگر Cromite (کرومایت)؛ جانشین قدرتمند Bromite
(جایگزین کروم)
اگر از طرفداران مرورگر محبوب اما متوقف‌شده‌ی Bromite بودید،
Cromite
دقیقاً همان چیزی است که نیاز دارید! این مرورگر یک نسخه سفارشی (فورک) از کرومیوم و بر پایه برومایت است که با تمرکز شدید روی
حریم خصوصی
و
حذف تبلیغات مزاحم
توسعه داده شده است.
✨
ویژگی‌های برجسته کرومایت:
*
🔸
ضدتبلیغ داخلی (Ad-blocker):
مسدودسازی خودکار تبلیغات و ردیاب‌ها بدون نیاز به نصب هیچ افزونه اضافی.
*
🔸
پشتیبانی از افزونه‌ها:
امکان نصب و اجرای اکستنشن‌ها (Extensions) در حالت توسعه‌دهنده (Developer Mode).
*
🔸
حریم خصوصی حداکثری:
محدود کردن و غیرفعال‌سازی ویژگی‌هایی از کرومیوم که برای ردیابی عادات وب‌گردی کاربران استفاده می‌شوند (قطع ارتباطات اضافه با گوگل).
*
🔸
مقابله با انگشت‌نگاری (Anti-Fingerprinting):
جلوگیری از شناسایی و ردیابی دستگاه شما توسط سایت‌های مختلف.
*
🔸
آپدیت خودکار:
دارای سیستم آپدیت داخلی در اندروید (همچنین پشتیبانی از مخزن رسمی F-Droid).
*
🔸
پشتیبانی گسترده:
قابل نصب روی اندروید (نسخه ۱۰ به بالا)، ویندوز و لینوکس (۶۴ بیتی).
🧪
نکته امنیتی:
این مرورگر برای استفاده روزمره و وب‌گردیِ امن و بدون ردیابی عالی است؛ اما خود توسعه‌دهنده صادقانه تاکید کرده که برای خبرنگاران یا افراد تحت محدودیت‌ها و سانسورهای شدید، همچنان استفاده از نسخه دسکتاپ
Tor Browser
پیشنهاد می‌شود.
🔗
[سورس پروژه و دانلود در گیت‌هاب]
🔗
[لینک مخزن F-Droid]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6980" target="_blank">📅 02:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6979">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">net.yukh.xui_81000@ArchiveTell.apk</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6979" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‏
📱
3X-UI Manager  مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع (فقط نسخه +3.3.0)
📥
دانلود: F-Droid و GitHub و Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6979" target="_blank">📅 02:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6978">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏
⚡️
پنل نهان (Nahan Panel)
ساخت و مدیریت فوق‌حرفه‌ای پروکسی (VLESS/Trojan) روی کلودفلر!
بدون نیاز به خرید سرور و درگیری با ترمینال، یک شبکه کامل و ضدفیلتر بسازید.
✨
امکانات برجسته سیستم:
🔸
نصب تک‌کلیکی:
راه‌اندازی خودکار Worker و دیتابیس D1 فقط با دادن یک API Token.
🔸
مدیریت آی‌پی و شبکه:
اسکنر داخلی برای آی‌پی تمیز (Clean IP)، آی‌پی پشتیبان (Relay) و مبدل پیشرفته NAT64.
🔸
مسیریابی هوشمند:
جداسازی ترافیک سایت‌های داخلی (GeoIP/GeoSite) برای اتصال بدون مشکل.
🔸
ضدفیلترینگ پیشرفته:
جعل اثرانگشت ترافیک (TLS Signature Chrome) و تنظیم دی‌ان‌اس اختصاصی (DoH).
🔸
ساب حرفه‌ای:
دامنه اختصاصی لینک ساب، مخفی‌سازی با تغییر User-Agent و نمایش حجم/تاریخ انقضای فیک برای گمراه کردن فیلترینگ.
🔸
امنیت بالا:
دکمه توقف اضطراری (Kill Switch)، مسیر ورود مخفی به پنل و استفاده از پورت‌های امن.
🔸
مدیریت همه‌جانبه:
اتصال به ربات تلگرام اختصاصی (فقط برای آیدی ادمین) و مدیریت همزمان چند پنل (Master/Slave) از طریق API.
🔸
نگهداری آسان:
آپدیت خودکار مستقیم از مخزن گیت‌هاب و بکاپ‌گیری/بازگردانی سریع با فایل JSON.
✅
تا به حال مسدودی روی این پنل گزارش نشده است.
🔗
اجرای مستقیم نصب‌کننده (وب)
🔗
سورس پروژه و پروکسی در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6978" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6975">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlBagWL3DUqWiitRmFPuZ_xI-D47suKtotEEpgeV5DqWV9_KErJ02xaQqKZhSrlRZH_LKZOKs6Pa2ID5dHWNfmrl-PhDV8a5VTfs5Ll9rnR0GC-lDca3tvIqIGZUI7cGO9T-NH9PQv2LoO3t_chmFSZVc3X--9iFcALrgxZyRvd6xdJ_g_oidxUEuaeEWnK1WcMaFia7606RLtPbxA3Qm4K5CFJKFqzkH6xuC5EFwtsG4gtsiph6UhhvTFGBMTKdGPQALOkbS6xag3Y3rR7Kl2XFPvD-m7-HXZF7ScJNVwND7hw1zfEMqO3bTEymY3STpv6_ZybhIdb6-2FwKL2M9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
تلگرام دیگر برای اجرای ربات به سرور نیاز ندارد
❗️
با قابلیت جدید و فوق‌العاده
Serverless Bots
، از این پس می‌توانید کدهای ربات خود را مستقیماً روی زیرساخت خود تلگرام اجرا کنید.
✨
ویژگی‌های این قابلیت:
🔥
پشتیبانی از JavaScript:
کدنویسی مستقیم و سریع.
🔥
دیتابیس SQLite:
مدیریت داده‌ها درون خود اکوسیستم تلگرام.
🔥
میزبانی بومی:
اجرا مستقیماً توسط سرورهای تلگرام.
🔥
کاملاً رایگان (فعلاً):
صفر شدن هزینه‌های هاستینگ.
🧪
نکته: این یعنی ساخت و اجرای ربات‌های کوچک و متوسط، از این به بعد بدون هیچ‌گونه دردسرِ خرید و مدیریت سرور امکان‌پذیر است
🟠
⛓
منبع
👉
🔤
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6975" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6974">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏
📱
3X-UI Manager  مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع (فقط نسخه +3.3.0)
📥
دانلود: F-Droid و GitHub و Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6974" target="_blank">📅 22:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6972">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kaxt34dRBALexsaKU3CT7Q4xdfsvCmroFzz5X1kZNqW1zgckwRKh94vECJiZGZg5YsJ5DEfJYK2Nr9ATcF2HwZ_FqT52-SL9gyeO7vKK3XLGNTh6c_xzyeQgqsPoXABDj5qW-l7ppcZvyosxFr5n8qy_Twou0_MaT44vD-LJIUw1R_E8zSI_ZNp-RO3OWm-oVRSE01EM5Wy3IMWC0UcjJkJgfj4QQLgSESs1rdEEuN-1tHVaInQYe39rXy89R4OIc5v8ztdvF1ERwhHWMsa7zS-k_8rsWtiRZ7Cb-YEpFgtDzBbKPfJ4m5gxI0qG95-qdnuLFI-RyJicoBW4ReIPTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
3X-UI Manager
مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع
(فقط نسخه +3.3.0)
📥
دانلود:
F-Droid
و
GitHub
و
Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/ArchiveTell/6972" target="_blank">📅 22:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6971">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/di-F0HippNwmwHIgG35u7pzZIr_2A4SjOapbtJX2aIKqcYRTfHlOD99vwRRyHdNO4E0okylwxpOwxAmsr7ubcYA1fdDRwRvTIxYFty6VAfzRQzbbF1OlQ2qVZu5x8m5Elu88MfCG8Jghr4xpzXR9uKV0nao3xpJWFcztu79z2Dn1HCQlh7o_Sg6vkJmlbTkvryunmgHVNf2H_GSitDeoswIHucs6O8PMS0wKuqv9z1Ypiid7QVkpTzV0ryXRwsnUr1uE0Ouw_38sGrthHq71q2dBexjBEZBsF_B2uufwd9pf-YDsyoJElwvY83xxt8OVgI2A4D2Iu0doKDTJ0LrHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
Droid-ify
یک کلاینت (رابط کاربری) مدرن، روان و فوق‌العاده زیبا برای مخزن بزرگ F-Droid!
اگر از سرعت پایین و ظاهر قدیمی کلاینت رسمی خسته شده‌اید، این اپلیکیشن جایگزین متن‌باز (Open-Source) دقیقاً همان چیزی است که نیاز دارید.
✨
ویژگی‌ها:
⚡️
سرعت بی‌نظیر:
همگام‌سازی (Sync) و لود شدن لیست برنامه‌ها در عرض چند ثانیه (بسیار سریع‌تر از نسخه رسمی).
🎨
طراحی مدرن:
رابط کاربری چشم‌نواز، روان و منطبق بر زبان طراحی Material You.
⚙️
نصب و آپدیت خودکار (بی‌صدا):
پشتیبانی کامل از ابزار Shizuku، دسترسی روت و Session برای آپدیت برنامه‌ها در پس‌زمینه بدون نیاز به تایید دستی.
📦
مدیریت آسان مخازن:
قابلیت اضافه کردن و فعال‌سازی مخازن جانبی محبوب (مثل IzzyOnDroid) تنها با روشن کردن یک سوییچ.
🧪
نکته:
این برنامه در واقع یک پوسته سریع‌تر و بهینه‌تر روی همان دیتابیس امن F-Droid است و امنیت شما را به هیچ‌وجه به خطر نمی‌اندازد. اگر از برنامه‌های اوپن‌سورس استفاده می‌کنید، نصب Droid-ify یکی از واجبات است!
📥
دانلود از GitHub
و F-Droid
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6971" target="_blank">📅 21:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6967">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ae2J9-LA_H7QaUss78-2zlNFRFVP5bBp9W1bsyesDMZRYJ6LA76aPjNTKtAuPw4SPMvM9vJXi_0tSEecSxykDcsXKvQDuDkRd4nai0x2D5VMXwy5P0l4qic6zAwj7YUpAnkqgwMtRLaQPSQDt1-TOhb5Awk_LZTM6FqQBI8K429aPFCuUaTvmp9Zh5Wod4GE_5IDv-P_LSRQi_hnTMl6Vj4vJk0UVjWx1Uo1dXOHWXpDqSm7KWg3a7ci_FA9QeRAVvhOiy0vabym9-F17E9J2G1gbl2iGL_SGNGZlSAM7ORP5n2t3Xlar830HNGb4lLP0aUamYx-wKfK88GXWWdq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O28L0wBQvEFyuS3qOQXpaw0m_pd0Aa-6jVdBOP_xRqn4Zp7VKB2xAQPyaxcXEEjRMsBmL01K0ptnllXqxZPKrbsYm780wK3NrM5Zx4q5a-zA2bcjLH-fSEc2ztqNQN_Jze7GrjniOsuLodERo216FC8Wo6_AmFglp_KwZVuQaKzvM4DagsHqnCD40U54AOzejJaich7Iiz67CKN2gU-YsLEj5tDoaXQH-4BVkrWNLheOrysX4p2jZ0opVG-je46PC8geKXLgZ7sCiofa7MJ9mFtiQccYQXBEjZsEevgjX_X13Ey2101-wfafV7ZRJufQpYYeEoaglrVf7qMal26-2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kB4ViMiCLeXWCDgrREdEolS2gPzVLps7luLBnDY2J6c0cqhQMOviLjCZNmeWMSR_wyRLnmoJ28BVMUEwVDxVviArusFGh4fxabeo3Ixar97HMW8Cjj_fIBSYJ7XRh2nGHd8EYu3rXv0vkXPvsm60ZlHm_9ZoVGq7TFZs7p3lNS8Q3rK-k2yEHXAO7nZzXvXzpoMuF7hknaoyNdR8DSwFHMWSmeS7wVLTsuUIJ_bFhQmulP9mPqvvM1aDA1PTqfjKq1KRmfy6ZBrv4r4w40y-RuLN3wLiPfkMJQ6JPe1tMLX7utYTVEKoNK5R_LDzykhluaZIuHAIq9r9rPhUlhHBaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-ldiEkuNCRNwfdMhqKF8EaW8PDVq2i2iZVilo5gmjngtx1WNRRlZiBQSg8ysU7Hnj7nKi8UoxofgSamdipk8xYF5f7xhQFbMBV0_fswAw0iKBbuzD1iqwCalDnMa4UURc_NhekDNXJuCF7Ew4eKf4P5lTN-Zttzq04VWRtYcfZvKJnpUIljGQfmaRc-DQoUxThFIJRoYTuaoWZXbFqgSA8ijzbbdNTcl5qxZWYE4MIs1ysEQX6DeMZjpN7vhb2c83A-B8RVyrcdk9zE88gztCuXbMsvaMpqq87UDceDT4TB7c-7e7njYHSd-h1u4J2NtmGQOuTN6IbVSvw5BEW_fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🚀
آپدیت بزرگ تلگرام با ویژگی‌های بی‌نظیر منتشر شد!
تلگرام به‌تازگی یک به‌روزرسانی عظیم دریافت کرده که قابلیت‌های کاملاً جدیدی را به این پیام‌رسان اضافه می‌کند.
✨
ویژگی‌های این آپدیت:
🌐
بخش «انجمن‌ها» (Communities):
فضایی جدید و یکپارچه برای تجمیع کانال‌ها، چت‌ها و ربات‌ها در یک مکان واحد.
📝
ویرایشگر پیشرفته پیام‌ها:
ادیتور متن تلگرام دگرگون شده و اکنون از ابزارهایی مانند
جداول
،
چک‌لیست‌ها
و
عنوان‌بندی (Headings)
پشتیبانی می‌کند.
🤖
تولید محتوا با هوش مصنوعی:
از این پس هوش مصنوعی می‌تواند مستقیماً بر اساس درخواست شما، پست‌های آماده و کامل ایجاد کند.
🕵️‍♂️
پیام‌های خصوصی مخفی:
ربات‌ها قابلیتی پیدا کرده‌اند که می‌توانند پیام‌های خصوصی ارسال کنند؛ به‌طوری که این پیام‌ها حتی از دید مدیران چت نیز کاملاً پنهان می‌ماند.
🧪
نکته:
این به‌روزرسانی به‌صورت تدریجی در حال انتشار است، بنابراین ممکن است این ویژگی‌های جدید هنوز برای همه کاربران فعال نشده باشد و دسترسی به آن‌ها کمی زمان ببرد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6967" target="_blank">📅 19:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6966">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OINV721Gc8ytq0hzOVYCW1JYX3lqokQbj9EGUN8cqzT1Lk4dRnsW4K1dTp9i9cm19heY6guLOxStdETQ7RZhYHtrrU1EcsfaxECDCrMrvFBOoNE6-3rHTmipgmOyeDeZDIqh6WjUL0dLkwgC6_g02E79ZDK2VE4UAExnO8JcwUdzt4P-Gp5g-GXiK50B7ec9PbjJLSUGxGhSQ0tTn7p65u98_mZDDHNLdBIZ5xSiWKGxa85xCH0ePUyhKaxCa6v-1ClaP24rl4ojQrqo-l88LtNWQcxPC1Ha_KWUpVNYgcQ-SNnbZThD1cxHYqSZzNod2qLqe5ZFcodtmfElMZzE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
Acode
یک IDE تمام‌عیار و ویرایشگر کد بسیار پیشرفته (Open-Source) برای اندروید! با این اپلیکیشن می‌توانید پروژه‌های برنامه‌نویسی خود را با امکاناتی در سطح دسکتاپ، مستقیماً روی موبایل یا تبلت مدیریت و توسعه دهید.
✨
ویژگی‌ها:
🎨
پشتیبانی وسیع:
رنگ‌بندی سینتکس برای
+۱۰۰ زبان
و پیش‌نمایش زنده (Live Preview) وب.
🛠
ابزارهای حرفه‌ای:
اتصال مستقیم به
GitHub
، مدیریت سرور با
FTP/SFTP
و کنسول داخلی JS.
⚡️
قدرت و سرعت:
اجرای روان فایل‌های سنگین (بیش از ۵۰,۰۰۰ خط کد!) و پشتیبانی از کلیدهای میانبر کیبورد.
🧩
شخصی‌سازی عالی:
سیستم پلاگین‌پذیر (دارای افزونه‌های هوش‌مصنوعی)، سازگاری کامل با تبلت و
منوی فارسی
.
🧪
نکته:
این برنامه با مجوز MIT منتشر شده و دارای قابلیت بازیابی فایل‌ها (File Recovery) برای جلوگیری از پاک شدن ناگهانی اطلاعات است. (اجرای آخرین نسخه نیازمند اندروید ۸.۰ به بالا می‌باشد).
📥
دانلود از Google Play ،
F-Droid
و GitHub
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️
⭐️
Cyru55</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6966" target="_blank">📅 17:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6965">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEzqcL687C1HSk_EhlvAKbzIZpJr-JRAhkM5YssmXWkdi61f0QrOEX2Yl4fDquSixxHiFIUl8AhgHZIwF4Tq3IsaAX5lUgs3ZAG80qef_Wp0Ky5qwlxoW9dU6-BnqnSBYMBTumN1NxdxGWqbB31MumOZQKcxe0X8TVi9-LvZLiCxVAQ2pS-nEoNNWuFGWH1dNSnKqVIDiQQXXX3iDwOX1dbq8nev33HYjnyyva3oOfeiWSVcUY4-DsWeLYinVtVmAb5m6KXnOR0Wiy-1tr_s50QmnM_uLtpl9xPbLi2WnssyLSJApqMefwJZ0Q9KHkLkg4yTmRFHS8o6P2jmdXNdcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
وقتی هوش مصنوعی علیه هوش مصنوعی رقابت می‌کند!
در یکی از آزمایش‌های جالب روی مدل‌های
Sol
و
Terra
، رفتارهای غیرمنتظره‌ای مشاهده شد.
🔹
کارتل قیمتی
مدل
Terra
پیشنهاد داد قیمت‌ها را با هماهنگی افزایش دهند، اما
Sol
پس از پذیرفتن پیشنهاد، آن را گزارش کرد و حتی خواستار حذف Terra شد.
🔹
اتهام به رقیب
مدل
Terra
در مرحله‌ای دیگر، برای حذف
Sol
او را به تقلب متهم کرد.
🔹
رقابت بر سر درآمد
مدل
Terra
با کاهش جزئی قیمت‌ها نسبت به
Sol
، مشتریان بیشتری جذب کرد و درآمد بالاتری به دست آورد.
📌
این آزمایش نشان می‌دهد که مدل‌های هوش مصنوعی در سناریوهای رقابتی، گاهی رفتارهایی شبیه رقابت‌های دنیای واقعی از خود نشان می‌دهند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6965" target="_blank">📅 17:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6964">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚀
مدل بی‌نظیر GLM 5.2 به نرم‌افزار Trae اضافه شده؛ کاملاً رایگان و نامحدود!
اگر اهل کدنویسی و دنیای هوش مصنوعی هستید، احتمالاً با
Trae
آشنایی دارید؛ یه ابزار و دستیار فوق‌العاده هوشمند (Coding Agent) که کارش راحت کردن زندگی برنامه‌نویس‌هاست. حالا خبر جدید و جذاب اینه که مدل پرقدرت
GLM 5.2
به این پلتفرم اضافه شده و می‌تونید کاملاً رایگان و بدون محدودیت ازش استفاده کنید.
🤓
من خودم هنوز این مدل جدید رو فرصت نکردم تست کنم ولی Trae کلاً سیاستش اینه که مدل‌های خوب رو رایگان ارائه میده، اما قبلاً یه
صف انتظار طولانی و رو‌مخی
داشت که آدم رو کلافه می‌کرد. نمیدونم واسه این مدل جدید هم همون بساط صف برقرار باشه یا نه!
🌐
لینک سایتش:
🔗
https://work.trae.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6964" target="_blank">📅 17:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6963">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏
🎙
Voicetypr
ابزار متن‌باز و قدرتمند برای تبدیل گفتار به متن به کمک هوش مصنوعی. جایگزینی عالی برای تایپ صوتی که در پس‌زمینه سیستم‌عامل اجرا شده و همه‌جا در دسترس شماست!
✨
ویژگی‌ها:
*
🔸
تایپ سراسری (System-wide):
با فشردن یک کلید میانبر، در هر نرم‌افزاری (ادیتور کد، تلگرام، مرورگر و...) صحبت کنید تا متن بلافاصله همان‌جا تایپ شود.
*
🔸
آفلاین و امن:
پردازش کامل صدا روی سیستم خودتان (Local) به کمک مدل‌های Whisper بدون نیاز به اینترنت (پشتیبانی از +۹۹ زبان از جمله فارسی).
*
🔸
سبک و فوق‌سریع:
توسعه‌یافته با زبان Rust و فریم‌ورک Tauri با پشتیبانی کامل از پردازشگر گرافیکی (GPU در ویندوز و Metal در مک).
*
🔸
ویرایش هوشمند متن:
قابلیت اتصال به API مدل‌هایی مثل Groq یا Gemini برای اصلاح لحن، یا تبدیل صحبت‌های پراکنده به ایمیل رسمی و کامیت.
🧪
نکته:
این برنامه برای ویندوز و مک در دسترس است. در اولین اجرا، به حدود ۳ تا ۴ گیگابایت فضای خالی برای دانلود مدل پردازش محلی نیاز دارید و پس از آن کاملاً مستقل کار می‌کند (برای لغو سریع فرآیند ضبط، کافیست دوبار کلید
Esc
را بزنید).
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6963" target="_blank">📅 16:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6962">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA3NacN21K5r_LsIgCRISCm8sJq5F6guETSBaGcDIbIzohXkJ3pOfLvftFg0hEUYd0faVyAAluZZrE9thJzTLfMKdKnp-u65Q6L7lqSH4pLhZIwgMZtXbG7mU_E0EeNqoFtWcq8lOkzEoRW75g-Ps-2LU3Gj18QobS4EAKpwofVlVXbSsjBLgCMsoJZ9nm5sEQxtzUAaYObEr2nPx-hbdhex9lFbeb_ax-7sbY4x_YuEx37jhM9bWdqEJGD4ANOCN4I9cEq5q_Ig_V8iujgh-vpklskRlMKbsd_c7vl5H8g518wYjIRP2AXnraWiATqNqwFHZK6bVbjQ8z-P7JrcfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
TelegramOS
پلتفرمی یکپارچه که تلگرام را به یک سیستم‌عامل کامل برای کسب‌وکار شما تبدیل می‌کند؛ تمام ابزارهای مدیریت، پشتیبانی و توسعه در یک داشبورد جامع!
✨
ویژگی‌ها:
🔸
مدیریت متمرکز تیمی:
کنترل همزمان چند اکانت، صندوق پیام مشترک (Shared Inbox) و مدیریت سطح دسترسی اعضا.
🔸
اتوماسیون و CRM:
ساخت سناریوهای کاری (Workflows)، سیستم پاسخگویی خودکار و مدیریت پیشرفته ارتباط با مشتریان.
🔸
آنالیتیکس و مارکتینگ:
ارائه گزارش‌های دقیق از عملکرد، تحلیل کمپین‌ها و دسترسی به مارکت‌پلیس داخلی.
🧪
نکته:
این پلتفرم بهترین گزینه برای تیم‌های پشتیبانی، فروش و بازاریابی است که می‌خواهند تلگرام را به قطب اصلی و خودکار فعالیت‌های تجاری خود تبدیل کنند.
🔗
وب‌سایت رسمی TelegramOS
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6962" target="_blank">📅 16:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6961">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0feee0c240.mp4?token=v56jm2qla1C0rurDYJ0Zg_8qiEHzYS82NXK86ySKIBYmqWePLRD0m_ze-VR-gMgnotD4aXCinqFMEDCWl9PcuwwDhnCTgkfjCZYoq-_SNgUfPfeiqe7KCxkgU-wHwf0drMIVA_QCtxhxggr_sQt-HnDtK8F9bHg-0HIGdu78nxMiHTvYxWwHYJ8aCdqCa0KTC2KnVoDdlIjAJG_cHI0PXtQaTInI-9I9EmxmGLx4dYicuc-GjXc9trZlGng8dxvG0Bzrs0fh74hPy-B32FCI6IcfJFagq7P0zl34Osm-oziJWyftTSrVm5nWSGvjS0Whl67rRmmz5isi1in-3q_3gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0feee0c240.mp4?token=v56jm2qla1C0rurDYJ0Zg_8qiEHzYS82NXK86ySKIBYmqWePLRD0m_ze-VR-gMgnotD4aXCinqFMEDCWl9PcuwwDhnCTgkfjCZYoq-_SNgUfPfeiqe7KCxkgU-wHwf0drMIVA_QCtxhxggr_sQt-HnDtK8F9bHg-0HIGdu78nxMiHTvYxWwHYJ8aCdqCa0KTC2KnVoDdlIjAJG_cHI0PXtQaTInI-9I9EmxmGLx4dYicuc-GjXc9trZlGng8dxvG0Bzrs0fh74hPy-B32FCI6IcfJFagq7P0zl34Osm-oziJWyftTSrVm5nWSGvjS0Whl67rRmmz5isi1in-3q_3gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
با یک کلیک، طراحی هر وب‌سایتی را کپی کنید!
یک ابزار فوق‌العاده به نام Ditto می‌تواند در چند ثانیه، سیستم طراحی هر وب‌سایت را استخراج کند.
✨
امکانات Ditto:
🔍
فقط کافی است لینک سایت را وارد کنید؛ Ditto آن را تحلیل کرده و نسخه‌ای بسیار دقیق از سبک طراحی‌اش را آماده می‌کند.
🎨
تمام توکن‌های طراحی را به‌صورت خودکار استخراج می‌کند؛ از جمله رنگ‌ها، فونت‌ها، اندازه‌ها، فاصله‌ها، سایه‌ها، گریدها و سایر جزئیات بصری.
📄
یک فایل
DESIGN.md
تولید می‌کند که می‌توانید مستقیماً در Claude، ChatGPT، Cursor، v0 و سایر ابزارهای هوش مصنوعی استفاده کنید.
✨
بدون نیاز به کار دستی، ساختار و سبک طراحی سایت را بازسازی می‌کند.
🔄
حتی می‌توانید سبک چند سایت را با هم ترکیب کنید؛ مثلاً رنگ‌بندی و انیمیشن‌های یک سایت را با تایپوگرافی سایت دیگری ادغام کنید.
👀
نتیجه را بلافاصله پس از تولید مشاهده و در صورت نیاز ویرایش کنید.
📦
امکان خروجی گرفتن برای Figma، کامپوننت‌های React، تنظیمات Tailwind، Storybook، WordPress/Elementor و متغیرهای CSS را نیز دارد.
https://www.ditto.site/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6961" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6960">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">موتور جستجوی مبتنی بر شبکه DHT بیت‌تورنت، که امکان جستجو و یافتن منابع تورنت و لینک‌های مگنتی رو فراهم میکنه
☠
http://cilimo.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6960" target="_blank">📅 14:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6959">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRAiJ3punEO4KPKnfe7QphF8cFfo3xZWoMrH2N4NZ5BPtaO08r3DyandaZnS7hu9t00_UyiHtJ6PCjteSuOguTPlVjcpjUHL7e8NAwmhKfuhosFWdh6R-12h7Q45-Xy6B0bDP8KnYCu8eaXwYXnNWKZ1XY6ZfUlw0H5cN1LB8RTz70NekTtLh_IWxjIdqng3gFJtcE9A-grDOVVxV0M99x2VgKPBhZC8NGOU8r4aYM0cETvvTaTpZMq7mriHiaIGSUo2O7cyuSy8m2ynpVgLwCN-GmzrlkrXZFv8Xn9fvIneo1-tkQhXwKoZI1FBVPa_BQRAgwP5Wl_KwQAiyoX_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌐
Magnitude Browser Agent
دستیار هوش مصنوعی قدرتمندی که با استفاده از بینایی ماشین (Vision AI) به شما اجازه می‌دهد مرورگر وب را فقط با دستورات متنی ساده کنترل و اتوماتیک کنید!
✨
ویژگی‌ها:
*
👁
معماری بینایی‌محور: برخلاف ابزارهای قدیمی که به کدهای سایت (DOM) وابسته‌اند، این ابزار صفحه وب را مثل یک انسان می‌بیند و با مختصات پیکسلی کار می‌کند.
*
🖱
تعامل و اتوماسیون کامل: کلیک، تایپ، و جابه‌جایی المان‌ها (Drag & Drop) در پیچیده‌ترین سایت‌ها.
*
📊
استخراج هوشمند دیتا: توانایی خواندن و استخراج داده‌های ساختاریافته (بر اساس Zod Schema) مستقیماً از روی ظاهر سایت.
*
✅
تست‌رانر داخلی: ابزاری فوق‌العاده برای تست خودکار وب‌اپلیکیشن‌ها با بررسی و تأییدیه بصری (Visual Assertions).
🧪
نکته: این پروژه در بنچمارک WebVoyager امتیاز خیره‌کننده ۹۴٪ را کسب کرده است. برای بهترین عملکرد، به یک مدل بینایی قدرتمند مثل Claude 3.5 Sonnet یا Qwen-2.5VL 72B نیاز دارید. نصب اولیه به سادگی با دستور npx create-magnitude-app در ترمینال انجام می‌شود.
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6959" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6958">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgF60zFtDpAOneR2dF2232N56oLbMpDnJwxMS2Nu3Gfi4Sj-_pCMCZPX9xGQ1isSEXa8bcnBSuTGbhw2rX7AWcLgitsh3bCzI1bZCFSpGj4Qh95y4Zy1BkWlehVe_EYHVEfm0NU6I2gSienqs0r-3ahl5NZr1YLevgqWSkulmDRhlukm4YNrag-E25agmruWBj-26ikBA3jnzaDLdAG9pPJYfzNIH1GYuUh1aWDdCfFN6C311jLUXGdkLJVWXCmM8s2fIGJgXRtHR6QtltPFz7OT8RuFMAEYfVKQ7f_5lWvGACymPJJgZIn1pd3MQF86jZT5qH4zeo7QwxGAFa8cbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار چندمنظوره رایگان برای ویرایش صدا، عکس و ویدیو
سرویس
Magic Hour
مجموعه‌ای از ابزارها و فناوری‌های هوش مصنوعی کاربردی را برای انجام هر نوع وظیفه‌ای گرد هم آورده است:
🔹
تولید تصاویر، حذف پس‌زمینه و افزایش کیفیت تصاویر؛
🔹
ویرایشگر دیپ‌فیک با قابلیت
جایگزینی افراد در ویدیو
؛
🔹
بازسازی عکس‌های سیاه و سفید + جایگزینی افراد در تصویر؛
🔹
مجموعه‌ای از ابزارها برای کار با موسیقی و فایل‌های صوتی؛
🔹
تولیدکننده زیرنویس.
🌐
magichour.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6958" target="_blank">📅 11:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6957">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">۱۰۰ گیگ کانفیگ اهدایی
🔥
vless://63dc39fe-3bc3-4267-8bf1-4069b47baa18@194.110.172.150:443?encryption=none&fp=chrome&pbk=3sRLbKljY5s7LCik-w9MqgenayhgHgLV0v9lmFGQ9TQ&security=reality&sid=3094219d2cfd2b3d&sni=www.samsung.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6957" target="_blank">📅 11:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6956">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏
🤖
3xui-telegram-bot
ربات قدرتمند و متن‌باز تلگرام برای فروش خودکار سرویس VPN، با اتصال مستقیم به پنل 3X-UI. با این ابزار تمام فرآیندهای فروش، تمدید و مدیریت اکانت‌ها بدون نیاز به دخالت دستی ادمین انجام می‌شود!
✨
ویژگی‌ها:
🛍
فروش خودکار سرویس با حجم دلخواه، شارژ کیف پول (کارت‌به‌کارت) و پشتیبانی از چند سرور (Inbound)
🎁
مجهز به سیستم ساخت کد تخفیف، ارائه تست رایگان و زیرمجموعه‌گیری (Referral)
💻
دارای ابزار اختصاصی خط‌فرمان (vpn-bot) برای نصب سریع یک‌خطی، بکاپ‌گیری و آپدیت
🔐
اتصال کاملاً امن به پنل صرفاً از طریق API Token (بدون نیاز به یوزرنیم و پسورد پنل)
🧪
نکته:
مدیریت کامل ربات اعم از تغییر قیمت‌ها، تایید یا رد پرداخت‌ها، و مشاهده آمار، مستقیماً از طریق دستورات داخل تلگرام توسط ادمین انجام می‌شود. همچنین برای سرورهای ایران، امکان تنظیم پروکسی SOCKS5 نیز تعبیه شده است.
📥
دانلود و آموزش نصب در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6956" target="_blank">📅 11:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6954">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsOx4Ac2q_q07LpmWo-7D918105gPom3F_MOvZhd6GW-fyUnWRYxAuj6p_9ZGtAwp_HtAYmFphkQ7g5Ucvj2H3Uzg0ztsQUNTsCABvcRwbFubCoJMwhU3rjtxcpt4zp4Et_lMHYLyBIGyM7uJidD9Z8Vhtvg7UR-6W-6Rce2CBbsJ5R1XyUEQuqiZDpQyy9YRVShS2icVMbceJWhPfKpTtZwl6UlKgPAGPiuDlz_Xj2PyTDWD-wBpi6wLd9cshI2vG3d0MrKO23zpeagS9gmp6nbbYrXl_K09klQjvSK464pvVsIkC8P_V49gv0DtkDarcuFcNLpE4-KFbLFM_msEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌐
BrowserOS & BrowserClaw
دو مرورگر متن‌باز؛ یکی برای شما، یکی برای هوش مصنوعی!
✨
ویژگی‌ها:
‏
🤖
BrowserClaw:
اتصال کلاینت‌های AI (مثل Cursor) برای انجام خودکار کارها روی اکانت‌های واقعی شما.
‏
🧑‍💻
BrowserOS:
مرورگر امن با دستیار AI داخلی و پشتیبانی از مدل‌های لوکال (Ollama).
🎥
ضبط ویدیویی تمام اقدامات هوش مصنوعی برای بازبینی.
🧪
نکته:
هوش مصنوعی در تب‌های کاملاً ایزوله کار می‌کند و هیچ تداخلی با وب‌گردی شما ندارد.
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6954" target="_blank">📅 10:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6953">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏
🚨
حذف ناگهانی دامنه
t.me
از DNS جهانی!
دامنه
t.me
(هسته اصلی زیرساخت لینک‌های تلگرام) به طور ناگهانی از سیستم DNS جهانی ناپدید شد! رجیستریِ پسوند
.me
وضعیت این دامنه را روی
serverHold
قرار داده که باعث شده هیچ‌کدام از لینک‌های تلگرامی در سراسر جهان در مرورگرها باز نشوند.
✨
جزئیات ماجرا:
*
📱
اپلیکیشن‌های موبایل و دسکتاپ تلگرام همچنان بدون مشکل کار می‌کنند و این قطعی صرفاً مربوط به لینک‌های وب (آدرس کانال‌ها، گروه‌ها و ربات‌ها) است.
*
💎
ضربه سنگین به اکوسیستم کریپتویی تلگرام و مختل شدن دسترسی کاربران به کیف‌پول داخلی (Wallet) و مینی‌اپ‌های مرتبط با شبکه TON.
*
🌐
دامنه موازی
telegram.me
همچنان فعال است؛ این یعنی محدودیت منحصراً روی آدرس کوتاه
t.me
اعمال شده و کل زون دامنه‌ها مشکلی ندارد.
🧪
نکته:
با اینکه اعتبار این دامنه تا سال ۲۰۳۵ تمدید شده، اما رجیستری کشور مونته‌نگرو (صاحب دامنه‌های .me) بدون هیچ اخطار قبلی آن را از دسترس خارج کرده است (پاول دورف در پلتفرم X مستقیماً از آن‌ها خواسته مشکل را حل کنند). این اتفاق زنگ خطری جدی برای شرکت‌هایی است که زیرساخت حیاتی خدماتشان را روی دامنه‌های ملی بنا کرده‌اند!
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6953" target="_blank">📅 10:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6952">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uO3koHVVLaqQSsGRqQM3wmLYL79jkQvHRUd508u2dVbYFoStCYY1U1_PwTMJVtbRmRsFFFml3LAclJy3LGSN_IvJJ_ClHOXex-egZKL3WApwRBN1He_xFYWquDeAW8kzUOfSjKzijEwRqt4AOYZG3w9aYJU40X2yu8Fl8gmW3uWdGL0R4Pkc7OtAuctbGiyhO3F_CZc1VsLV_ob1tB4Td9ck9YFh-yALEqfbeAdqvrSNXI-YFDXDH5UAq8ueai66N5pvsxQoRzfg9_ePCJ_Nle8enMANof_uyjS79BrLSw21x5bagCmVi8EODh6-XXiClW2DnobKPXvjvwl6flv0RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛ Google AI Studio حالا به GitHub وصل
میشه
🔥
با قابلیت جدید Import from GitHub میتونید ریپازیتوری‌های خودتون رو مستقیم وارد Google AI Studio کنید و با کمک Gemini روی کدهای موجود کار کنید.
✨
امکانات جدید:
•
📂
وارد کردن پروژه از GitHub
•
🤖
سازگارسازی خودکار کد برای اجرا
•
✏️
ویرایش و ادامه توسعه پروژه
•
👀
پیش‌نمایش و Deploy سریع‌تر
⚠️
فعلاً اتصال یک‌طرفه است و تغییرات به GitHub برنمی‌گرده؛ اما همگام‌سازی کامل در حال توسعه است.
https://aistudio.google.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6952" target="_blank">📅 09:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6951">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIRHGKfcIIRmjlVvPUPR7lC0U-ogrS9ehvbBhfUwz3LALCO_G6nj5K6rsatUNVJdZlJk3mHGPfxw-KVKJiOJhzMv0pnRoqzDhxpvFpo8eZprc9twsb3mm3AKB5VQ2g6EwYOa4mmz8WFOE7pjLkzgjLz0-rpg4QAc2p39ko69ZLafhMo0b5jBkY_Lh_iFoyKQx7o0VHr6UCRtHQS0Dq5LN9MBSVqb052IxxevAyMBMDNwc2JdvplthEwwzcwRXeYn9TZ7lPe1jyqDqh7r9d1eZzC6doX1BXRiHxlE72oUkWdBdda1c-Z6Pn2ilnVk0R193E0RHV0OTHWLpENGpOnAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
بیش از ۳۹۰۰ پرامپت آماده در ۱۶ دسته‌بندی مختلف، از جمله:
• تولید محتوا و نویسندگی
• برنامه‌نویسی
• بازاریابی
• طراحی و تولید تصویر
• آموزش، کسب‌وکار و...
https://xueprompt.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6951" target="_blank">📅 08:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6950">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184a52dda.mp4?token=VN6RIjHlkvFwLJU9zFk7ZVu7vBKkAh7DUVJCCJvmx-CZfQ0N2n5GKWmxCKnr0QUTHvJmAabZJd2QYoljXu8b7wdSbsuC9RXfrYa5cjJnwM0u4VbGbcOo8xm4TSDInDcd60LG5MXgzCYNJP-7OmRlXmKH5YgKlp1swFJwrWwiG8QUzEHeC4avEcpHwZ49e3DoS8PUcPnSE0Kfc2ffCnX1pnZlADsQsCMY0EgvgYI_3zqbJeyK__jNMCWVMx53kpW7RLBGBKewsB03lWoIkbMyXVMTCWeh8W7w0Ma29pgwWHWUCQSB_T-8g7Gm0-2C28UrVSUu7wxZvdESnL-iFjWNhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184a52dda.mp4?token=VN6RIjHlkvFwLJU9zFk7ZVu7vBKkAh7DUVJCCJvmx-CZfQ0N2n5GKWmxCKnr0QUTHvJmAabZJd2QYoljXu8b7wdSbsuC9RXfrYa5cjJnwM0u4VbGbcOo8xm4TSDInDcd60LG5MXgzCYNJP-7OmRlXmKH5YgKlp1swFJwrWwiG8QUzEHeC4avEcpHwZ49e3DoS8PUcPnSE0Kfc2ffCnX1pnZlADsQsCMY0EgvgYI_3zqbJeyK__jNMCWVMx53kpW7RLBGBKewsB03lWoIkbMyXVMTCWeh8W7w0Ma29pgwWHWUCQSB_T-8g7Gm0-2C28UrVSUu7wxZvdESnL-iFjWNhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧰
۳۰۰+ ابزار رایگان، فقط در یک سایت!
📄
ویرایش، ادغام و فشرده‌سازی PDF
🎬
برش و ادغام ویدئو
✍️
ابزارهای متن و نگارش
💻
ابزارهای کاربردی برنامه‌نویسی
🔑
ساخت QR Code، رمز عبور و داده‌های تصادفی
💰
ابزارهای مالی و محاسباتی
https://footrue.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6950" target="_blank">📅 08:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6949">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">📶
دسترسی به لیست سرورهای عمومی VPN
مجموعه‌ای از کانفیگ‌های
V2Ray
،
Trojan
و
Outline
VPN
که سرورهای جدید و سالم به‌صورت مداوم به لیست آن اضافه می‌شوند
🤔
🔗
نیازی به کپی تک‌تک سرورها نیست؛ فقط
Subscription Link
مشخص‌شده را کپی کرده و مستقیم داخل کلاینت خود وارد کنید.
V2Nodes
🌟
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6949" target="_blank">📅 01:57 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
