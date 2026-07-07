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
<img src="https://cdn4.telesco.pe/file/YWF6AzjVbf6BrYDSrzmXCiECPLE6TuCN11u2e2QAd2fZd6ZYa-sc1bV3QOVOVe3Mcieh0b6RYqul5az1AasQl6TLqZoTMmp6G2KioEYC7Z2xyC09eVPFkDjeNsoDf9J6SuuPfvjoi6FmhVcanD2RCjgOdQGne6eqRgtoy2Y-c7WGp5tl_KQgTDJeRuJH1owVjXixixklBGRamoN0qUorZovgNdVY-jtib__9aUavYNKwg05GBL2mXM-v2MFnq5OA4M_hQwxwNm6dQl-u-WgamsNcwB54Wxj-TDbtbwSfagaIU0No_D7DH7V33bin3l3kh1sMolfwSQciQ1XVGRDG7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.71K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 11:29:05</div>
<hr>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqPfme6gjKdGVy1Xo147dmI8V9AfMxvDF8zJUZAq2Ayr9u77skzlqivwnlmpiSkNAaH5JIYYnRMI05qV5f453SxdTwSUtULlRiqhLpQrt9RTMUfLNSx-pFFInTFKrYvrtM1zRVDvTF-BLULcdM2sbC3fPeYOA5okS_kj4kdHRrmviOO6npub1OMfO6bTRvsJUfzbbfQnU1LsLMdTC5QtQDmb3rC6y0gB7f6ptY7kyVjRSNYaqcFY_3QwItQCtxRHWobqTCymVNK2wstRLj_cYC5VttWX9DexPtKKvQs_7qlGMWMEM5bk7O25MPyj67_jxRoMAaBr0DZs6UFHDokDCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 439 · <a href="https://t.me/ArchiveTell/6757" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675041278d.mp4?token=JR4rLEELjli00l8SI2ae9Lkxc7zhdnzf9sp-5LjPGunWNLKp-khdG19SMI-kDsmKRgQ3ITY7l4pqYaYwZMJAgLxpfskcgZYxb1maVh-J0WWU-D6tQR-OSEDZCCnvvLzxR7ClVWo_y5U40rCIWwxgzOMK8EOCW_mqRgmBf8h_X3e48R1QFl-_EOVIgoVJq62y03UuiqEQ4QHMj6swihXXY6L2AMIpF5lLqfKKNC4HowOom7Q-Cswpa8t2WQAhl8zwLLF5zlSZqjqTQfNPUr-J7Rx24JtSWISrbvnVW7mw0u9_ofdonFwxkngbf9XMzRT5mbcvEqGulJPpoX_p0Fzs4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675041278d.mp4?token=JR4rLEELjli00l8SI2ae9Lkxc7zhdnzf9sp-5LjPGunWNLKp-khdG19SMI-kDsmKRgQ3ITY7l4pqYaYwZMJAgLxpfskcgZYxb1maVh-J0WWU-D6tQR-OSEDZCCnvvLzxR7ClVWo_y5U40rCIWwxgzOMK8EOCW_mqRgmBf8h_X3e48R1QFl-_EOVIgoVJq62y03UuiqEQ4QHMj6swihXXY6L2AMIpF5lLqfKKNC4HowOom7Q-Cswpa8t2WQAhl8zwLLF5zlSZqjqTQfNPUr-J7Rx24JtSWISrbvnVW7mw0u9_ofdonFwxkngbf9XMzRT5mbcvEqGulJPpoX_p0Fzs4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 422 · <a href="https://t.me/ArchiveTell/6756" target="_blank">📅 10:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 421 · <a href="https://t.me/ArchiveTell/6755" target="_blank">📅 10:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">#اختصاصی
🚀
بهترین وب‌سایت‌های ساخت ویدیوی هوش مصنوعی رایگان (Veo 3 / Sora 2 / Kling...)
۱. VeoAIFree →
https://veoaifree.com
این بهترینه! به حساب کاربری، ایمیل یا هیچ چیز دیگری نیاز ندارید، بدون واترمارک!
۲.
TryVeo3.ai
→
https://tryveo3.ai
از Veo 3.1 (آخرین نسخه از گوگل) استفاده می‌کند. نیازی به ثبت نام نیست، فقط وارد شوید و شروع به کار کنید.
۳.
VeoE.ai
→
https://veoe.ai
وقتی ثبت نام می‌کنید، 100 اعتبار رایگان دریافت می‌کنید و اگر وارد سایت شوید، هر هفته 100 اعتبار دیگر دریافت می‌کنید.
۴.
Videomaker.me
→
https://videomaker.me
اولین ویدیوی شما بدون ثبت نام رایگان است. صدای آن هماهنگ است (شخصیت به صورت واقعی صحبت می‌کند).
۵.
Veo3AI.io
→
https://www.veo3ai.io
این سایت سه مدل را در یک مکان ارائه می‌دهد: Veo 3 گوگل، Sora 2 OpenAI و Seedance ByteDance. شما مدل مورد نظر خود را انتخاب می‌کنید.
۶. EaseMate AI →
https://www.easemate.ai/veo-3-video-generator
وقتی یک حساب کاربری ایجاد می‌کنید، ۳۰ اعتبار دریافت می‌کنید. هر روز، اگر وارد سیستم شوید و روی «ورود» کلیک کنید، اعتبار بیشتری به صورت رایگان دریافت می‌کنید.
۷.
Digen.ai
→
https://digen.ai/veo
این سایت از Veo 3 استفاده میکنه و دارای ویژگی Lip-Sync (حرکت روان دهان شخصیت با گفتار) است. این ویژگی در بسیاری از زبان‌ها کار می‌کند.
۸. MindVideo →
https://www.mindvideo.ai/veo3-1/
شما نسبت تصویر را انتخاب می‌کنید: ۱۶:۹ (برای یوتیوب) یا ۹:۱۶ (برای تیک تاک و ریلز). بدون واترمارک.
۹. Pollo AI →
https://pollo.ai/m/google-veo-3
این یک پلتفرم بزرگ است که Veo 3، Kling، Hailuo و Sora را ترکیب می‌کند. مزیت آن این است که می‌توانید همه مدل‌ها را امتحان کنید و ببینید کدام یک را بیشتر دوست دارید.
آرشیوتل
۱۰. Synthesia Playground →
https://www.synthesia.io
مدل veo 3.1 ، رایگانه، اما باید با یک ایمیل ثبت نام کنید.
۱۱.
AIVideoGenerator.me
→
https://aivideogenerator.me
؛Veo 3 بدون ثبت نام، رابط کاربری بسیار ساده.
۱۲.
Veo3.us
→
https://veo3.us
هر روز اعتبار رایگان برای ساخت ویدیوهای کوتاه دریافت می‌کنید.
۱۳.
Veo3Free.ai
→
https://veo3free.ai
؛Veo3 بدون نیاز به حساب کاربری، شامل صدا.
۱۴.
Sora2.video
→
https://sora2.video
؛Sora2 از OpenAI، آنلاین و رایگان.
۱۵. Aitubo →
https://aitubo.ai
مدل‌های بسیار (Veo، Kling، Hailuo، Sora) و اعتبار روزانه.
۱۶. Eachlabs →
https://www.eachlabs.ai
پلتفرمی برای توسعه‌دهندگان، مشابه Playground، با یک دوره آزمایشی رایگان مناسب.
۱۷.
Fal.ai
→
https://fal.ai
توسعه‌دهندگان از این برای آزمایش مدل‌ها استفاده می‌کنند. برخی از مدل‌ها برای امتحان رایگان هستند.
۱۸. Genspark →
https://www.genspark.ai
یک مجموعه همه فن حریف!
۱۹. Pixnova →
https://pixnova.ai/ai-video
؛Veo/Kling با اعتبار روزانه رایگان.
آرشیوتل
۲۰. AIEase →
https://www.aiease.ai/veo-3
؛Veo 3، شبیه EaseMate؛ شما روزانه وارد می‌شوید و اعتبار کسب می‌کنید.
۲۱. Vixdo →
https://vixdo.art
Sora 2 و veo 3.
170 اعتبار رایگان، بدون ثبت نام و بدون واترمارک است. یکی از بهترین مجموعه‌ها در کل لیست.
۲۲. FreeSoraGenerator →
https://freesoragenerator.com
اعتبار رایگان برای Sora 2 و Sora 2 Pro.
۲۳. GlobalGPT →
https://www.glbgpt.com
یک مرکز بزرگ با Veo 3.1، Kling، Wan و Sora 2 - همه چیز در یک مکان.
۲۴. ​​iMyFone Novi AI →
https://novi.imyfone.com
۶ مدل (Sora 2، Veo، Hailuo 2.0). هم در وب و هم در موبایل کار می‌کند.
۲۵.
Media.io
→
https://www.media.io
یک پلتفرم هوش مصنوعی رایگان با مدل‌های ویدیویی فراوان.
۲۶. SeaArt AI →
https://www.seaart.ai
اعتبار روزانه رایگان، شامل Veo 3 و سایر مدل‌ها. این سایت در بین هنرمندان بسیار محبوب است.
۲۷. Leonardo AI →
https://leonardo.ai
بسیار شناخته شده! شامل Motion 2 و Veo 3 و اعتبار رایگان هر هفته.
۲۸. DomoAI →
https://domoai.app
تخصص در انیمه و تبدیل تصویر به ویدیو. می‌توانید یک تصویر بگیرید و آن را به یک ویدیوی متحرک تبدیل کنید. این برنامه یک دوره آزمایشی رایگان دارد.
۲۹. Hotshot →
https://hotshot.co
جایگزینی برای Veo، متن‌باز
۳۰.
Klap.app
→
https://klap.app
این یکی کمی متفاوت است: یک ویدیوی طولانی (مانند یوتیوب) می‌گیرد و آن را به کلیپ‌های کوتاه برای TikTok برش می‌دهد. این برنامه یک طرح رایگان دارد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 516 · <a href="https://t.me/ArchiveTell/6754" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJO0Hr5HX99ChJ3sC5SsVTcd-wAggLsVnDsIkksXOx5wHMFJlyTaq7X0-JgL-NseBSKP1JdtV52DpFj7vI-_38Z2HcThjfNxbyPW5rphx923BOiCv5_r0K85gFmJ1PWd67-nOUfIOiuCiX4gSCxAQ1f1BCGO0UWc2vPx0RejmTEOVPnK1BCvRMqo4HncuBVhKv2CFQATiiDM2BIvdxzfuqAjTpHlLeAfXecbzDFNJmZ1owA1Bs-dZnBjZthsst_lQrIv72Qrm5eX8bXO64UpZUajPZwabzhO6Dhs3J-Ktx3jppvmGUIehcJi2XFSHaOfszhMXMs7wWHlDXTV-V-3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بقول نیچه
در چنین گفت زرتشت
«من از خردِ خویش به جان آمده‌ام، چون زنبوری که انگبین [عسل] بسیار گرد آورده باشد. نیازمندِ دست‌هایی هستم که به سویم دراز شوند. می‌خواهم ارزانی دارم و بخش کنم...»
بیاین مثه نیچه باشین و این عسل و انگبین چنل رو به سوی دستان دراز بسپارید
نیاز داریم به حمایت شما
❤️‍🔥
https://t.me/ArchiveTell</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/ArchiveTell/6752" target="_blank">📅 01:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor  https://youtu.be/pN3LxWzDtKI
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/6751" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor
https://youtu.be/pN3LxWzDtKI
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/6750" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6749" target="_blank">📅 22:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7XvbtZyghjrWknjaUcIlJ4KmekYa6JKErVzoReAbwwRwKZ2toc6Tf3EqQSIxR8pFNftEPIGH61RwvVIOLAq3oNKVtUr7pN-v3-vl0VX4AMtOkxog8z1f2lgdGtQwHfsSqyKhLXhwe3gWDtRHSwTxZnx11TIcYp7Tvr44bARmP32ghUJwz2g_I_uGhPZlWlu0ijpRssUCHAuP34kyMtogbfRNVC25qFdDdSKS2OAWjOUGF56W4-lqNZs5dVPXkxRC8L4MegHisURuyNI5I14V99zuGPCV233rnhEZDhyh66HNOJHUxMWswjZZ3SF7h20nz5_pd682yZc0SVmyrTH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074191361432035554</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/6748" target="_blank">📅 21:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfsxYfJ-gXjoEfqgYdYohAVmsndi2uVmp4Z0SYoaOFLkUsjt2zAtcbZchPuK0IrHgB8ARwgaQpY1N2oM3mb5jrae_z0XNU6EZ221PpSSeHYrXGZ4Ucmqn3AbVD5PoAIhYt-MZAgs79FzZq9PgFBuDLsFVifJFV0stPtmAYjjWFXPzvabJ2wrBF4q-f5YZMfNakjqasgW7W8pCi5jySLAjbqyUCy_Bq-xQA8y9pHIAiGZBfH6KhJ6monox7XvgpkUyqnLlVKPlfhxcrZgD3n4H7q3rayHR-EBiOqbUpesF5Y3ZLxEbJPFuWNfUbUUsM4PcblnlSk1R3BJsTyWRufLSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/6747" target="_blank">📅 21:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbLAWUuvZMXRV0eA4ZnIz1aHgRYieBmCWR55Y1ahE2F_epxvhXzXVlSzHsg-SlniyjJqP0_wzPJ3JhGO7fwaEk-mnpRog1Tm20ZGCoGXiTI3071VYfGGHsRx7GS5Vt61qZfXJHrjNMYe5m2QXz-ckdpKu0ngmKSQTd_ZIJmJ6PkzISq3SiD_vquFV74MW1x1SXM72BI8xPGPpNQxGVs0Ara8g7NI0dBY53OdYU_feEkftyfd0w8mhx2e4tEbQwRa-Q0SOKf83-rVAkaiz568PCt7kW5Gqu-A8mK_r5LpynaE6LcPCZ8XKjt1V_4zR6tB8TjYiFr0KCMydv99MArj0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6746" target="_blank">📅 19:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llw7vVvym9Lyp2ud9iJX-C0jwdJly9bT0mYmYx76Vf5kvR2kEw4ZCw5hP5WgjJV2NPhR7nTMBntamhh26fj_YrC3JBn6ALojiaejITCJ6amdVG8SmO0x3zosv4Dv1rNIhqhNjsGPP4nT0rX9zjU2BnsonxSoiaiprhdCb7-M6n9k3cTScxS4FUEhaEDvC4RmcX3Mz8Spiialb_7dzKFEZuAiuX2B7a-XY_m6H0ga6al15c_p6Hymi4Aan3EHrOreZ_LLJQmyG_e7C_VlgmYaO1zzqA1BvDfMJUH3IsjM4uuodWm7vt5arN1eco4Zyfc8VkZ3Pgnjb202hxtUgPoJPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/6745" target="_blank">📅 18:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910f222215.mp4?token=bUl4xJ056hU95L7E2X50k85NbqtV-GZRjQBNAzAQ63XIO0B6aftPIr6CswUwr3APaP3uDA0_1cFsG1lscFZ7jFUiTVyqgfesz43w3dWCnJywPL6GdOI2EpXyn-UNS3C0gXEHN93mj4p6Ly7PuGVkDpVRq9h5oYR1SCmO3zrbKB0tfXBqJ4qN2dpi5YSBIyl1SfuRydgdRSahNcUefoh6KZTNudMICXZbEHL7anUTgpou-sYQdN3IgC3FSwQsQxHH2AuTDnEonk8s6pEUhBBwjp5KC8FK18VaFw9tctOowGGi1sB5nmWLyNI2jpH8etYSZGxESh--8WLWtC20WKcB1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910f222215.mp4?token=bUl4xJ056hU95L7E2X50k85NbqtV-GZRjQBNAzAQ63XIO0B6aftPIr6CswUwr3APaP3uDA0_1cFsG1lscFZ7jFUiTVyqgfesz43w3dWCnJywPL6GdOI2EpXyn-UNS3C0gXEHN93mj4p6Ly7PuGVkDpVRq9h5oYR1SCmO3zrbKB0tfXBqJ4qN2dpi5YSBIyl1SfuRydgdRSahNcUefoh6KZTNudMICXZbEHL7anUTgpou-sYQdN3IgC3FSwQsQxHH2AuTDnEonk8s6pEUhBBwjp5KC8FK18VaFw9tctOowGGi1sB5nmWLyNI2jpH8etYSZGxESh--8WLWtC20WKcB1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6743" target="_blank">📅 16:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAZFY8iI8x-3QmEDR60_o5jm4aMDaW4Hoy6dn95cr8HuTvjxuv1HQqUR1bwuoa93LGeONmfT1bc1vnJXUBqB2ZDQdEapwaeFK35v5W1jWr4xayUoDA519ziqBPptJIB3nZs7pnhuXx_RFR4Bh4IH5AIHm2j19WznGDSdqZ11RP9BP4HPB7nakNiS1dR99oox8TlGi6_2p4vSAlm1G0JKBw-SdFfdCa_kSV70lmAUizfxRZ0jMgBjsaM9Gdtnd2MTdW1NZUt0bWu-3u-UCuvraj2K09V_z2XRyu76By5ekGKsMNyFRT3K6ZWRI-EUxL0aefayWif31ADTNcRaqvo2NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6742" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6741" target="_blank">📅 14:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون…</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6740" target="_blank">📅 12:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون فضولی میکنه. یکی میفروشه به دلال های داده (مثه گوگل و مایکروسافت و...) یسریا هم که حریم خصوصی محورن.
الان هرمس اینا رو واقعا نمیدونم. هر چی بیشتر این مدلا رو بیشتر وارد چیزاتون میکنین، ریسکش بالاتر میره در کل. باز این شرکتا اروپایی نظارت بالاتر هست ولی نمیدونم طرف خوشش میاد از ی مدل میگه به به چ مدلی چقد قابلیت بذارم چنل، ملت کلی ویو میزنن استفاده میکنن. طرف به تلگرامش و... هم وصل میکنه بعد اخر بعد چند روز میگه ببخشید هرمس رو شخصی ران نزنید
اینو میخواستم چند روز پیش بذارم ولی گفتم ولش. ولی حس کردم بهتره بگم تا پیشگیری بشه بهرحال</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6739" target="_blank">📅 12:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4KKtWUBeL9gGqZM9dp0wFAciOJ60u5nTzrMSPKvlU0HEn11W9mXrHvwyybUPy8GREuGLO465cmKG5-rRzCH7WM6zVe0R9v6uVZgtRXz--uW2oXEQXcdwWXIQMF1u8OVP1F2x7_xTcnD056Jp66oOFO8tGzDLhYAOgJSD5Y_IDcBJdModIlynL0jJxY1wMHOXkFudTA-rPrfJM0WMpVyZnfM9ylzcuDic-JUYWU58Jl2uNU7g2998vS_MaKUWQx6m5EPyegqU1MNbMZfCu5oGScO8ynKDBJngH4npazNqaweZLahAisQnIXdm9wE29jFn_DHMx0GvnY_agRp22uyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074039784629014892?s=20</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6738" target="_blank">📅 11:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjOcLMEzelHuDGNzgs8r5bKWkoYt2SZFxAEmdwqwMXmsGTPI3sJYeU1bPeNIpEg2mZlSYTTtXsrWHL6lgpZL4dL3IjzGk9qp0MAt2RGs7VRvqjRAwedrOQqXAgY_-M5vsIr7rzMg8aTOFBcYVTDpruVYian3aNcqNTrPLjpdm_pbWDgPuhONoYhcuMs9uCgVWvqf_ogp9zT_-spz2LKgEoHgvk6gAeBWnQOThXobr8vcV1BjpkbBnx8nULyWH6rwjw9AnZvwCMFyrVIUdhJpDkK24dvah5yN_nnmqx0DS_rUtKtitRUuhU0qVNgvh1r8IBap4wocZxVG1e-148NMVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6737" target="_blank">📅 10:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWGqUYZfO_lqwh4QKGHbADh1xH1D-fbTHSWoz3XryXdnin_KxJaG0MbG9bSOnXBXLnvbw1c8QlPuQSNbuz0UG9dSaiRaMYkAO-TGcUHlnIFMVlp2202RPqRGOADYdXM3uaPpKsPgxohdW0wdZK6_zf9srZpMHMbbpfgTRsq_bxfpadtB8dxxbYJg2AkKb1zujPVwH9cm1elBdbt1VCjAk4ZsbgaXtI9AmDwVqAq-wE9jXN8IxWQivswA3ab78FEYPw1ya9fFxD5-HGjin6anQnYMmOdTUtD3XO-AkbzuFloFSmi5SWHFETcONcJAoim8HeLZVFT1AGpyFMjgBiMOzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6736" target="_blank">📅 10:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6735">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjfSAFaOxNZJUJJLZ8BatJdGXvEv75Mg4E4tRWdTNeF5_JZbjZO_X1tTwlNbUzhq3M3uekRVteQ0WxvkVA71P8XF_eSl-PzEqNn7W5OfLhQJfQHhMx7v5Y-pJ3a96X4DRrFfPB37CJLS4vYKP6-O7VygtWmAi2TZO1_K8hfSwwce1WJ18w4cwJRadz4b0xh2sulEc9zrweb9qzbsXspxopdesH3VvaaobWAB_JTGg1P5TDShh0RzNeyo0v9HuOgsMvIWishdPV-HuKfNJ31E6VJZP-QbXTI-vcaq7ADbe5FLJLUr_yvHf5k2eKvKdZxw6ituvKPk0ztlQYVa4TpGCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6735" target="_blank">📅 10:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6734">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0HsLaLHKhT2s7xyrH5jrstpjYCkvumqNVDDalgyuOa6X8mz-cQW6jZ2W9roXI4GpVDSPOr57PfOi0iqcXS7E4me1Xqu-mv5jZPJhNBaJuYLQzQ_oCDwLIrqN2n1Olivvdwvjcw1J5xLwNnvsjJI8XU5To6ZeCr3msqmf8ytmva26Ause8jJd-7hdiaGjE3LJzyQT5HsI-uvHzMHF6tTgeKU7LWOLy9IoyoLcMCt2SEMphveN_pfoKNorDv31DIwhFfGEd8kLr7u9KeLKwum46t3hmfIRSRoKZ2wL9aomRy3dtJ3iXDtuJki8uk7DFq_VfEDSJNs1dSwt_oyVQd0iA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6734" target="_blank">📅 09:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6733" target="_blank">📅 08:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.  اینطوریه که ازت آی‌پی و پس رو میگیره  بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ... خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌  دیگه نیاز نیست دستور های ترمینال رو بدونی…</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6732" target="_blank">📅 04:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6731" target="_blank">📅 02:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6730" target="_blank">📅 01:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6729" target="_blank">📅 00:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6728" target="_blank">📅 21:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6727" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.
اینطوریه که ازت آی‌پی و پس رو میگیره
بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ...
خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌
دیگه نیاز نیست دستور های ترمینال رو بدونی یا حفظ کنی. تو فق به زبان فارسی بش میگی انجام میده</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6726" target="_blank">📅 18:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">https://x.com/ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6723" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دیده‌بان لیکفا منتشر شد
🆕
افزونه‌ای برای مرورگر کروم که هنگام بازدید از وب‌سایت‌ها، اگر آن سایت سابقه نشت اطلاعات داشته باشد، به‌صورت خودکار به شما هشدار می‌دهد. متن‌باز، رایگان، کاملا محلی و بدون ارسال اطلاعات به سرور
👍
Download
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6722" target="_blank">📅 13:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSTynsdPDpY2cHkD0NFb98mEO-L0VVKC16mNfz8eP8LSly4TEkB3S9uKI-hP2FvreojbHrwJl5o3AXR7T9l8w3elLmlX6vFV6K4xWGhpdOYnUEbpSHRJxQC4b0Eg1Cz-oIigeK9MOVbQ6RTukuTtEx9lFFqWW69OS2xlSEqRJnXwjRcErmKdpYIpL5xbUHKygwTcqFyhf_0zmtGdaXD31Rmm55YTvQVyweuGHBoz6WZRYMxN3uURO-xZkGPkCY0sY2g6ZDpgyboTCBE0CutAy5Vwc1POxfkk8h0iUib-ryEgp2rubUday08FriCmFIl2vHvOECF-rdLAZ-9--h-3dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6721" target="_blank">📅 12:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6720" target="_blank">📅 11:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=PDnmPk_pvkj3EOHAuiL33cTcxcRMxJA6Ukmjg_5W7dFbvcyccPe9e5Zzb0gvKdog-guxVtlgwMaMeHikeDW2xweGb6jxpuMbrujND0jIVTNdb2EIPXCYJuM-1DPcm9V2ApyOfRUe3leXGb4b1oiIluFPpxxOtv7QzicSCN2KFU5EF_nz4BEXIdkEyp5nQvFnmkZ6-kiF5z9Hgj8cUEQeAJCOAt9Gm5NB91LE0_6UrRPc1cDLAIVclkyZeD9m8LySNIXyUT6SRqbOAqMd7Bu51VOcTo1ojhorE1NJCgiGImo8vXGOByljh26rRK8C3bpcLc20a8oszIgizUtjMh2eZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=PDnmPk_pvkj3EOHAuiL33cTcxcRMxJA6Ukmjg_5W7dFbvcyccPe9e5Zzb0gvKdog-guxVtlgwMaMeHikeDW2xweGb6jxpuMbrujND0jIVTNdb2EIPXCYJuM-1DPcm9V2ApyOfRUe3leXGb4b1oiIluFPpxxOtv7QzicSCN2KFU5EF_nz4BEXIdkEyp5nQvFnmkZ6-kiF5z9Hgj8cUEQeAJCOAt9Gm5NB91LE0_6UrRPc1cDLAIVclkyZeD9m8LySNIXyUT6SRqbOAqMd7Bu51VOcTo1ojhorE1NJCgiGImo8vXGOByljh26rRK8C3bpcLc20a8oszIgizUtjMh2eZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6719" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q44WblFVVWczGgmhCyZ0UIlK4oT0zPSwxXc4yF9VRWycWYcbUhFYTnRDtGOZRkd9PduUpyPfATmFaZLtxxPosIsNygEoFi_J3cYAK3q1AtWQT0a3lDQNmjIh5_dhQ4OqWEkELeWZ4qquJnnwpQgj1Rx_XpadlH9yXLb7aYdmKb6MLhMJIpn-hm8EEfslK1IEOD1lSfWwk6EDRNnQzrZ90MmpAfpG0UcMmRt_T8BMWADwaUXYokjpFExwsevJc5n8Xk1wuzoL9qfwvArYwj6qlt2V1PpJBJB2BdJ3-tx9v1oHF4UJGQ5n1q76VsP5p4ZI53MSEKT4VFOYHnOdZ2TDWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6717" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6716" target="_blank">📅 10:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6715" target="_blank">📅 03:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=QoHcsQ9xk1d_w_XhVmRPMlhsJmYHYLUBbhuzxwC-1I3ozgAFsYdVJzgNX4wlK20H4Sw2RtOL7gEYj8yFfMdSGDI2dgeU5dRfOIPp10SqP9qz-SG1-4lE1tM0Yw6ov6N7E8JUJQn0p3fGVmjCbq59763dLgTGMg0fQLqML7-lolARzVP-6LRun5BA3tCdcQQCGnwYZsAbVv4HQf5jqhdpDKuOi6zEFGcSiMuWNInbTRFZlEjBKr2ngjBl01C8CbHhxdCpQJdkkm2YZCuLVxHPGlVGArA9GMyuft5qoI7CT1nk6o5Y_z4nYpbS3NWw_7IZFYqQCDMs--_mUneEFkziZl3U9WfXg3rXyrCwSUyJP4MHAQNqBWlKSX_rD9W2USD_UMgXm0HFztCXospVmNcfI51CgxLEb9cxyurmQZvD-QhqWY5U2rAA1O_xLWpulYzWNv_aChBL6Yo8EZGODw31nfr13vVvAYes2RFKHkccPz1ylVGV5gNnzDsiV5tzHcO9W1Q13zcIoBdfljUkmxJxNqgmdzEOLTtM4VMQ57trk5vgfr_wMpMqxnahfmkZijlopA4blb3fiyFbPCbvvaL8u-NdqWZGWDkjB-cjOyX7i3OkCPoYL6zUxhUj03kWMnAbUUKGjsXrpG5RwWptunOWBkiLLxvSNC9d4HUk86u4W-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=QoHcsQ9xk1d_w_XhVmRPMlhsJmYHYLUBbhuzxwC-1I3ozgAFsYdVJzgNX4wlK20H4Sw2RtOL7gEYj8yFfMdSGDI2dgeU5dRfOIPp10SqP9qz-SG1-4lE1tM0Yw6ov6N7E8JUJQn0p3fGVmjCbq59763dLgTGMg0fQLqML7-lolARzVP-6LRun5BA3tCdcQQCGnwYZsAbVv4HQf5jqhdpDKuOi6zEFGcSiMuWNInbTRFZlEjBKr2ngjBl01C8CbHhxdCpQJdkkm2YZCuLVxHPGlVGArA9GMyuft5qoI7CT1nk6o5Y_z4nYpbS3NWw_7IZFYqQCDMs--_mUneEFkziZl3U9WfXg3rXyrCwSUyJP4MHAQNqBWlKSX_rD9W2USD_UMgXm0HFztCXospVmNcfI51CgxLEb9cxyurmQZvD-QhqWY5U2rAA1O_xLWpulYzWNv_aChBL6Yo8EZGODw31nfr13vVvAYes2RFKHkccPz1ylVGV5gNnzDsiV5tzHcO9W1Q13zcIoBdfljUkmxJxNqgmdzEOLTtM4VMQ57trk5vgfr_wMpMqxnahfmkZijlopA4blb3fiyFbPCbvvaL8u-NdqWZGWDkjB-cjOyX7i3OkCPoYL6zUxhUj03kWMnAbUUKGjsXrpG5RwWptunOWBkiLLxvSNC9d4HUk86u4W-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تبدیل ویس به متن تلگرام کاملاً رایگان! (بدون نیاز به پریمیوم) با هوش مصنوعی Cloudflare
https://youtu.be/Xq7e2k3qlqA</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6714" target="_blank">📅 02:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوستان وقت بخیر و خسته نباشید
این چنل زاپاس آرشیوتل هستش
داشته باشین بهتره
❤️‍🔥
ی موقع اگ چیزی شد...
https://t.me/FOSSArchive</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6713" target="_blank">📅 22:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=Ky4v66ZIeDuAdV-XMm2618ubIVfdh7Chwuy6YIZKvweyoMJFjxwTWL_iqCgQHog-7h10NC-fJXAd0-FTPyCWVirBdfmulAh95dXzN70HSjP57A6vmGHKpNV0ANHl0piKIvijQXLIP34OQLy3GzuafermvS5OwFpiJFBNKdeszayC-Co1UGCwL-M5D8N0EiM0GTO_4oIqaY0R9VG3N9zCL2AaDsy5caZ7sjR6heW-9ZZG12UOsbpTM9bJ1UkdahCdGewouK1a456pGPRpqqdAv1ZMsgdbEyMyK4IsDbVrI6EuC0VzMtsil0WDMqt5OcIr8Org9Z_MlIpidqBp2H_GsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=Ky4v66ZIeDuAdV-XMm2618ubIVfdh7Chwuy6YIZKvweyoMJFjxwTWL_iqCgQHog-7h10NC-fJXAd0-FTPyCWVirBdfmulAh95dXzN70HSjP57A6vmGHKpNV0ANHl0piKIvijQXLIP34OQLy3GzuafermvS5OwFpiJFBNKdeszayC-Co1UGCwL-M5D8N0EiM0GTO_4oIqaY0R9VG3N9zCL2AaDsy5caZ7sjR6heW-9ZZG12UOsbpTM9bJ1UkdahCdGewouK1a456pGPRpqqdAv1ZMsgdbEyMyK4IsDbVrI6EuC0VzMtsil0WDMqt5OcIr8Org9Z_MlIpidqBp2H_GsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6712" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423195fff7.mp4?token=f1ssutLxpAgTpnPJu9CA8yYotpqvN_waTbGCMRIwA2vp_pByYjgj-2e9dJHvNSBQlomfzKmN9VcPTAbIlF6Pktv8igwNGsfHZ3Kfj2bUORkJ_Nw4wCW4wPxYkEd-zGag3YcHliSF6EcMZwIMxzBVnQcy3k2Q8X9Ir1Gyw8uY_XMXJrWHpBdhfjHLmopPU8w4iO5c4gn_U_N8lrmOETRfGV8uIS3U3GgRmLJwd0oLBP34SzCnL0MjlIupZRegHH2Qw8m5fvjYEjldtcyNmKChYMXAo0OjA9i8ItDENsUXHkLE_WoWr4WlGYjbIhb7bLutZnaik4nCbI5in2cY2RRKzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423195fff7.mp4?token=f1ssutLxpAgTpnPJu9CA8yYotpqvN_waTbGCMRIwA2vp_pByYjgj-2e9dJHvNSBQlomfzKmN9VcPTAbIlF6Pktv8igwNGsfHZ3Kfj2bUORkJ_Nw4wCW4wPxYkEd-zGag3YcHliSF6EcMZwIMxzBVnQcy3k2Q8X9Ir1Gyw8uY_XMXJrWHpBdhfjHLmopPU8w4iO5c4gn_U_N8lrmOETRfGV8uIS3U3GgRmLJwd0oLBP34SzCnL0MjlIupZRegHH2Qw8m5fvjYEjldtcyNmKChYMXAo0OjA9i8ItDENsUXHkLE_WoWr4WlGYjbIhb7bLutZnaik4nCbI5in2cY2RRKzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏کتابخانه‌ی معروف ‌Pad Shaders⁩ (منبع غنی گرادیان‌ها، پس‌زمینه‌ها و شیدرهای خفن) رایگان و متن‌باز شد!
🎨
✨
‏دیگه نگران لایسنس نباش؛ می‌تونی تمام پلاگین‌ها و ابزارهاش رو تو پروژه‌های شخصی و تجاری استفاده کنی.
https://shaders.paper.design/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6711" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6710">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6710" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCqwvrzarGUryH4lHgIpUN51O5eQkgtXfi5rwG8lOzWCD52V_e5z75Nl_3yuFG2_n8Ufd_utcqiqBKiXsTVnvsHp0jXjB0dQ_CyLvJWWYwUi4nPcSD6B4kXkEEA423U_6o6Aqg8CbdJtA6QJ0iK4ZSbvwNasUxQJcKqzpUxs8pdyrYcXCwPdbZZUPyhB0PfsxCr1ThgJfg64OmDxRy2TUrzeSnKW6Of6mRu7bAUqugA0urDrRdBEBg1MtxnRhQDU5ZkQ7qwerTcB0UjWORaoKOl4-6OMACBWjAcGhrPU3f9QI8IOn9hNVApElvkSq8RWX3pD1l1KJte-Fb43Nmu-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5
هوش مصنوعی رایگان و قدرتمند شرکت انتروپیک
10 دلار کردیت
با لینک زیر 20 دلار
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6709" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سایفون رو اپدیت کنین خوشگل شده
🔥
(نسخه بتا)</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/6708" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=VAvMZ4Rmue1U-2F0u92FadbxTH6J2FogS1Vy1fQDi46WfJkbVlMSjyV_z3se0FVnKGTznLyZY43ZFG-YXiNLcb42fhY9aErKhZpUPxUmDFKbXJ-LN_Ml7FhaxzwG75n8kyrfG7jKfRXU8VHq0hdjWsuhRLvfCfuXHuVel2UQxnLE3oPZm6uk7PUJncSN8MAwO5nS2yz17VJL9yb2sQlxm-9n93x-G9d8IueoTAa1_JIxu5FYtLU-q2nTghVBFPTKZ_3ZKOvO1iV-jBM_q0IKUxQF6Xpdl7doq5cNutm4VWzkR_xW8AS1TL6dEFrvErVmBI5vK0M9HztBFcSSwqRYlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=VAvMZ4Rmue1U-2F0u92FadbxTH6J2FogS1Vy1fQDi46WfJkbVlMSjyV_z3se0FVnKGTznLyZY43ZFG-YXiNLcb42fhY9aErKhZpUPxUmDFKbXJ-LN_Ml7FhaxzwG75n8kyrfG7jKfRXU8VHq0hdjWsuhRLvfCfuXHuVel2UQxnLE3oPZm6uk7PUJncSN8MAwO5nS2yz17VJL9yb2sQlxm-9n93x-G9d8IueoTAa1_JIxu5FYtLU-q2nTghVBFPTKZ_3ZKOvO1iV-jBM_q0IKUxQF6Xpdl7doq5cNutm4VWzkR_xW8AS1TL6dEFrvErVmBI5vK0M9HztBFcSSwqRYlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت 10 تا ایمیل رایگان با ساختن یک ایمیل اتومیک (مولتی اکانت)
https://www.youtube.com/watch?v=XHJ3TwrwG-g</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/6707" target="_blank">📅 03:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBK4JjGDVTfYnMHyKKS17sqyuMlu8ic2gglp8d1yYmXyeTTiUpoJ5cJPdrRBevKMw4XbvMgX0LBFEMSRy4TjCGxDOtmDIjYDYYjiG7eYYYIf3RwyYZI2kaS_rx1WUzbGgcGawC8MAlsufAAcFhfxYpaD1rCVUtmpBCpirHcm0O3CsBKDyVwZtSpJKz16w5boxnxIqYciBzmhmnigtmX4-_zOIfRtbuzECqbi4HwVY1rZdGBnJabtC6ogMsFuiNuHQFIrmUl8xROzcfwBnnAUDgFN-ZUAyeGHJ6tykoA-zmecZ5menCtB9deF9tHJxMmhNRIPHeeSHKBLCMjfQqQORA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6706" target="_blank">📅 02:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9054T1t7fWjgUba4wwtWB6przYnA8Au_JXLkbiSaA0XNH5sB9slZ5_AZ8340-4TUuudulShWYYl82oqbsAbkt_EtN3k1SLfhP4eqAp5DiPI9sHEa6OntAkJEHfdeiE5o9cd67CSWLEzOXbdg6wvCNs6XFdYN2DWz7cnRlPqcupmOcdyIBqvB3COI0dd76BZU2TL_5r39-iBu3xBHhG3_u7CpODo6ARZ35rDq8002AXFTQvVPmhTaOPGN6K02BXEQ43sTmhiJXocYhcn-AvoXNSa5vhgrZcIB2xuYRvqRowOboK4-MCMrRHhpBFn5gIffX0ko0d_jPT-KaJ9t-havw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/6704" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hShJD8-x-xjZwHJiT-GXe-EaKHB3jL_53mALP1IA_OQi2X0Kmlv4tDKMIm0ZNqmuV4PFZKbkktMrxXgc_E5mF-5RBttXn3TE9HxT25AsUDNdHMa9agNucDvWmdKIa8Pfcz7x56Xkkvzzr6FKjixw_ZrzhA6Fd7zAddCVCLD1wK6uxbi1R63NyEWGvmtL8fAGlYgmd3k5sRGBx57kw2Jk60NhDl-PdjPgko3MdsK1cA-uo1z26JXSUnq4Auc-7i5WALx6t4S_tSTIS99jtvpTAPKbb81l8GR3C-jvkiN-jwy0ivFxi9tAt13mQzhS3TvXFJ9TD82jvpHw5gIIz6eKPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/6703" target="_blank">📅 22:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWwXsE9TSOEIAgFMKgUMkenZS-ovPKhsscBnV2nbpVy_3SVrbE-eq_yx37cMFpw7iLgoTQHJGWLaFNGsTFYon680-EJVM-Z7wgIZCX_3To2A7lFKN2RuwCObTy-Hg8Hn6D8yMR6m-z0a7T7um308XtWxdpBYsnibCOAmXkiV9nH0-xLnDWUu0waHKtCO6QSJDTNyasniAZtlGOU3Nh9UE6ktyaDYMW3r6MX0ufxsXdGQtdfk0EHH9ZEQ8uvmAZuxPZuJc8JacySTOVE5SMVioTmGgoJ4iaEMSCuFQe0nq6PIyauKaiNR8kKX8ZhLa35aa2lEBGv6UzzIkd4oZ6txeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا پولاتو چیکار می کنی؟
پولام:
به زودی ۱ میلیارد*
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6702" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1d1XISjmklzix0J9-i7hI53oZLh6S4A_igPIqFDFX903TWcXy0urdXfoFXRYcWqsG8o3cZ2ge9uP5rrEg6dMkFdWBK-KYp2dKu7cWUnjpt97Zx6X15SZwK70-CtWpN2-k25yVE-IvgB1kCR_gD2CDPbjUB4tH_V2rixgQTnz9ApExTZtYnqQwGBPkCMXviRyKxrXeEkzmcyATbnDp-fm7-31qr9yz_IEiK8gcy29dJbPvvwnjWUmQM8Za4CzHcySElmNd_5kjMYCYbMV3vsAcSFdWhdthc2xE9tRI_f3_dZAVGuriBYRh9AHKTyghnzrU-eFYwBnFPQndJFERA5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKopogRmqaQExVNGZudakb0SnJSehHxhL-DTbor7ASXGInpU_JsmcSbJDKOS0FyUViDmThm2yVNmnZCQ2tbDS6Zc-Y5f8_a541SUE_iXa6NIHJh90N-aR4Q6R64E-XXdqfbyAre5r7cF4NyHCyvkv9ax-NZudZB19VBQn-EmkJ2cCyk4ImmNoFx9wN_068pqLHbHXJkYXbC6crLwg9S15rX9xCZPfoZjHVtBS4WqmM31sB-RnW72FXJBzhAIZr5fni1eRTgoAArdlYvJ1moZ2XJex_8Z1kb6EKWbwm0eC2-ZBuhcZ6BibSTpy9i8XLYLqzCXjMuVBUsUjI1BJFOADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SfJj4eSDfRU8s4birjvyZBsP4hvr1mH9dnA_ZAcsing0v5ILHq_zQp_HkEYnP_efHIIDvPRubzoocA3eybfqmKfXrd3FstPftUYTFViynEPhevPuWDPvxvBDazO9Writeq7GDhUsQfcnrCznJK1re0e2RVa_I-grTqf-EuBZxPyUtBKuVfMVGpg7VxmXD4AfM6qToenXdxdHBln447Q7J27A_gD_8Ta3Rw-Z3nTFkbu3u08bKCGS-89UCtCi2iRZJqkCOSnYkGv6t3EQm8K2l1vLyzO2p8Y9Zn5cYb6Yj0gJdK1NVuAHGYNLWBOE3fKn8avWJ-Fd0ez2-Q-x5fmiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppT_oGeZ220H8RVpBhMomQdIl4J1Ps8I-ED2Z5yARK73QiirSW0Fi2Q4EejSwf9qGP7ZSYSSJVh0ZJZ_GBG4hohbKDHWSt1Qx_Nwcgw8iSj3BTlFe-P_K1ydvKRfRJmGLxTAgFPvKyjtShO36ohm6KaFIZ0ExK5cRUcYItsCge12kly5P6uB8pAXORU-ZEGX3CNMj7RH4tqeG8HqbkjLEF5Ei_ZgLQfwKmFHa48kAauDa5YSUEQA0NJYJTxjjs502YDlSk0okO9MJpXXqsjSsvyQs8POjAyB34HQB57zXl-I6VSXRGQLq8nH9u2X7qUrSQ-DwjFXADsV0E83u-4-cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKDhmdpTyDvA-lcMFixBbkgF7c4ZNHQHyf_JCMUsYqjSAjioU5mDF3HZVrjO_tK2cI39IOdEXyjeAf51RpULSt5nD5isTjfzIwCXmCxO5qpCxEAwinm8mx_1nCq9cKj51KrOOCJErFMRojKvVDXBf6oMsQFGRkjdBufvs6TL6Dy9kRw-KFeTElccWwsj_DUTVgD44xL5gFGM_FCBJUAxJEa3bEGUJWOQ1gClS7FmraQgFHOgCTZjuOPO8h90oDqZKaG1FD8XOqvv-9j5cC6u-DU5HWwOC30YD-Cwv5u_j6_sp6RvEo0x1jl7qpeX_bcZQ459xRwvg88D-64W-OZD0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDcrYox8JT009LN_MxQbeI29iHm5nZeCRLLNLgw7TFCBOWsE06x11jNAVjk847DzzrdiEDXQK_vrgIWKogedXM3KZOv5BCr3KpvXSTq57joRi5ADIGpLjK43TyRMgq8becK0MIB-no-OsPctYhGWlhHW3XzWZZKTtbu9mc8YBFXz0TFdXCfeApCSI_U51abmwUVbdkZ13C5UhI56uCpIJknY-yCPm6l0_s14rakCzWreqIC1iXQin-GZMB3eYYXMJl_JzXDxKi6oHDaksbIGE8JWWdnlLE1q33bmiU1PrpQxwvP7VvHuoj2VAwpt9lEKYuc3TDmMWz9Vb0eeQhDUZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJDTfs7UdXg0N0ECpAL14-chn9cpD-olCZ-Jom66wVeF95EC10GAVFiroVwR93zr2fF_UFUYiknZoQKdpl8sf12A5IZMyrAiKfrb2T5QZN0pWlGiHMAL7NQ5Whsu9RH14U8pk_zwNxEHBhLGw18mNFHsjzl47rtOeI-x-WqvANeUS2Sl2Gv3kTJLdImUtNluaZAaVURczwJItDsb7Gz4KCk0jP1e5gl1UEfUojai8pYpd1ogNI9TF3IlumNMQQLGBAQCHOturP3E2N07b4T0tko1Eub58-RuQd1766SD28rNGagFuIzQYwUUN6jtyC21n-Ysv_cBckw-RXUjzFqd3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتایج
جایزه عکاسی با آیفون اعلام شد.
در این مسابقه سالانه عکاسان از سراسر جهان بهترین عکس‌های خود را که با آیفون گرفته اند، ارسال می‌کنند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6695" target="_blank">📅 17:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJodCITZXu_qtezstlVd3PhialacVktwY-r_UCfyeP2xD7_zcpoUEbLXNVbBg5tugLTe0xnAiXezyZNGX4XMvZN3OfK8dGhre4JudaAPm75_VLjJvkFbYpS6E_28QJ_RM2jCP9RVL8svlyxEa5TEid2xNvf7X5jUPdmt4_n7EE7AOmaf0yNhF4ba421X-sCNS0F56qpIIAFkYYL2HYxlG8QPDbe3voRNu77-AU-vWL0Jr5BCTuJdf7qScbMEdCQqnc1wdOsUvSSVfFe2Xpl7EwoRTTshdcDDUx3R-wkUG7A-VKpBH24q5_8CjJlRQNl0NN7zvBXH4uaBTC0FA1HpiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AITwitter Generator
یک افزونه برای تولید توییت است.
این افزونه که بر اساس فناوری پیشرفته هوش مصنوعی ساخته شده، خلاقیت و سرگرمی بی‌حد و حصر را به حساب کاربری توییتر شما اضافه میکند.
https://tweethunter.io/generate-tweets
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6694" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYwKNPydVFxAgebLP7_MpdaxDsLRXkye_KWQ7MhjE_3fz5jqV9r3yzGEKHCewOX6Jowb9qLyfgaYfqwL2_D4Oz1661HIHLxMtoQAYUEDhQM3ljphD7F0xiW3CoJ0yPO0BTP6szhCctmUV1UGSqA0QKoq5atJ6dzWX3FawinE4YJY87cIFcNOzCmrFsC8TUlNbvWVdQ_SwsOBmMHmV8uAT4B7-3iGGZFiMlhTMO25BP_qnHTu9yTJxGrPRgERmhd7xd_mrSXHMT9SlPy3ci8Ca-hBQM4G-iUGEoKEj0ZqkxKc5pwz4KXfE8AsRxKX0ez2T_5z0XYixvSXtFvGHUjvTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک مجموعه‌ای رایگان از پرامپت ها برای Claude ارائه می‌دهد
🤩
این مجموعه شامل ده‌ها راهکار آماده برای بررسی امنیت، رفع اشکال و بازبینی کد، خودکارسازی وظایف و موارد دیگر است. برای هر پرامپت، توضیحات مربوط به نحوه عملکرد آن ارائه شده است.
https://code.claude.com/docs/en/prompt-library
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6693" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2eHqUEtmFdqr47BPSlMclweMtUR9eazTbbW0pG-6fTwk4v_J91yPK3qNXj9z7fHNVMmULKj0V9Na19Ld5iqO6kj3hzwS0tZPF3ebgRFWXCXMknnbejVpUiYA3UY5wTiZbXeIW2JrOuOuSXdcubVUZplUs_zmqEncoqUakz3BVxQz5onaq2e67uqQLM6eMyzHEx9G4R4r3IrN8RT_G3VdF26eUrdnq9BIJERmgHiTtRaiXSnM3aY4dBAVGMlZswZVsQEHEDPhd8mQ1AEVuvdQUkHrETWknwbb69EQuy8e2t7jGNfw3o77JJ1piVHIHSVRUG-kYPg2CRF3uNCECHTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فتوشاپ را فراموش کنید
🤯
یک ابزار مبتنی بر هوش مصنوعی می‌تواند تمام وظایف را با دستورات متنی انجام دهد و برای این کار نیازی به مهارت‌های طراحی یا دانش فنی نیست.
🎨
✨
🔹
همه چیز بسیار ساده است: یک عکس یا تصویر را آپلود می‌کنید، پس‌زمینه را تغییر می‌دهید، اشیاء اضافی را حذف می‌کنید، رتوش انجام می‌دهید، کیفیت را بهبود می‌بخشید و از ده ها امکان دیگر استفاده می‌کنید.
🖼️
🛠️
🔹
بدون ثبت‌نام و مستقیماً در مرورگر
🌐
🔹
کاملاً رایگان
🆓
https://ezmaker.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6692" target="_blank">📅 14:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏
🎁
500 کریدیت رایگان ‌Opus 4.8⁩ و Fable 5 هدیه بگیرید!
‏دنبال دسترسی رایگان به قدرتمندترین مدل‌های هوش مصنوعی می‌گردید؟ با این روش ساده، ماهانه ۵۰۰ کریدیت رایگان دریافت کنید.
🚀
‏
1⃣
وارد سایت زیر شوید:
🔗
‌www.relay.app
⁩
2⃣
‏ ثبت‌نام کنید:
‏با اکانت
گوگل
یا
مایکروسافت
خود وارد شوید.
3⃣
انتخاب مدل:
اگر روی آیکون پروفایل خود کلیک کنید و وارد تنظیمات شوید
در بخش اکانت ، اولین گزینه را بزنید و select model را انتخاب کنید و مدل مورد نظر خود را انتخاب کنید
4⃣
لذت ببرید:
‏از امکانات پیشرفته و کریدیت‌های رایگان ماهانه استفاده کنید.
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/6691" target="_blank">📅 23:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🧠
یک سرویس جدید که قادر است مدل‌های سه بعدی را به کتاب‌های آموزشی تعاملی تبدیل کند!
📚
✨
هر مدل سه بعدی را بارگذاری کنید، سیستم به طور دقیق ساختار آن را تجزیه و تحلیل می‌کند: عملکرد هر قطعه را توضیح می‌دهد و نحوه کارکرد آن را نشان می‌دهد. در پایان، یک آزمون کوتاه برای ارزیابی دانش شما ارائه می‌شود.
🧪
🔧
برای آشنایی اولیه با قابلیت‌های این سرویس، مدل‌های آماده‌ای در زمینه‌های پزشکی، مهندسی و علوم طبیعی در دسترس هستند.
🏥
🏗
🌿
https://atlas3d.space/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6690" target="_blank">📅 23:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=dq646j1C_NHK3A_ERffvc_buSv49WWMwtXcEhu8VKbs7fkhqEhobwQhjmKQlDs4xJdfYOtyFOIptLqkyy_QgneapP_l7vzH_tEjfmnWHo64pwhykuDMwalnjLuiLRvlY7Sx4YFMS0WE1q8umqEisBbM302xw9nesdwpu8bVtbfzkXJ98DKqX67PijoV4MrI6a3vfKoDKTklH-Sc-ASSoOH_oWBb8vCEAsTFd1E3nXIWQZri56wuBXsBhPrVL2sSFF92Q0sAAgN-AwOmWaXgu0VKoUm-3aTwQB8e-A8IVVnOIxnscqoiLMJ8AZ7cy66jGnMrZjVzTwW4cST_NT7dDHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=dq646j1C_NHK3A_ERffvc_buSv49WWMwtXcEhu8VKbs7fkhqEhobwQhjmKQlDs4xJdfYOtyFOIptLqkyy_QgneapP_l7vzH_tEjfmnWHo64pwhykuDMwalnjLuiLRvlY7Sx4YFMS0WE1q8umqEisBbM302xw9nesdwpu8bVtbfzkXJ98DKqX67PijoV4MrI6a3vfKoDKTklH-Sc-ASSoOH_oWBb8vCEAsTFd1E3nXIWQZri56wuBXsBhPrVL2sSFF92Q0sAAgN-AwOmWaXgu0VKoUm-3aTwQB8e-A8IVVnOIxnscqoiLMJ8AZ7cy66jGnMrZjVzTwW4cST_NT7dDHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
😂
سووو رونالدو با رینگتون های مختلف
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6689" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آموزش‌ گرفتن Fable 5 به صورت رایگان تا 1 ماه هر هفته 70 دلار
💰
برید توی
Aerolink
و ثبت نام کنید
📝
لینک ثبت نام
🔗
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
📄
نحوه اجراش روی
claude code
هم همونه فقط این تنظیمات رو بزنید جای اون
⚙️
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
هر ورژنی از claude code هم بزنید قبوله
✅
لیمیتش هم دقیقا مثل
freemodel
هست
🔒
موقع اجرای claude code بجای دستور claude این دستور رو بزنید
👇
claude --model claude-fable-5[1m]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6688" target="_blank">📅 22:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6687" target="_blank">📅 21:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6686" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaWeluEE8-3f3iq6M00Q4dl4Wiv105K09N0hUX4_Ai0ApxvF7LBvtgKJxEkx-_P_0iT6ILjMmgsyE24CKxeC_mWwYtAeDlRrc-FyghHeFBbnjjnz_39qng4wpVh3QBhWSfMvBn8sisvhyEoUei1uQBeK4-SfOaIt09V7WKJQwFZENTF5tpK5_5rtPiezf8pB1MtMfsICDjbHRqd02Xi-IU4pF5ZyMocWHNT0a5kYYxnpqjAMtGYTc7a1lEMy2fr_LgbEWRn8mzeepFuKsLkLX9ixJCbKqNlc2CYGkouVgvtaZ7PyIjQ5dy6QSn5n8B-NFUypp_Ailg-tsZ3LFZ5dCQ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaWeluEE8-3f3iq6M00Q4dl4Wiv105K09N0hUX4_Ai0ApxvF7LBvtgKJxEkx-_P_0iT6ILjMmgsyE24CKxeC_mWwYtAeDlRrc-FyghHeFBbnjjnz_39qng4wpVh3QBhWSfMvBn8sisvhyEoUei1uQBeK4-SfOaIt09V7WKJQwFZENTF5tpK5_5rtPiezf8pB1MtMfsICDjbHRqd02Xi-IU4pF5ZyMocWHNT0a5kYYxnpqjAMtGYTc7a1lEMy2fr_LgbEWRn8mzeepFuKsLkLX9ixJCbKqNlc2CYGkouVgvtaZ7PyIjQ5dy6QSn5n8B-NFUypp_Ailg-tsZ3LFZ5dCQ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیه‌ساز هاگوارتز ( مدرسه جادوگری سری داستان‌های هری پاتر ) از ‌Fable 5⁩
در این قلعه افسانه‌ای می‌توانید درس بخوانید و با جارو پرواز کنید.
🧙‍♂️
‏این شبیه‌ساز مستقیماً در مرورگر اجرا می‌شود.
https://hogwarts-production.up.railway.app/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6685" target="_blank">📅 20:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ظاهرا کلودفلر اعصابش از ایرانیا **ری شده و از این به بعد دیگه ایمیل فیک قبول نمیکنه اگرم بکنه تایید نمیتونین کنین اگرم بتونین تایید کنین بنتون میکنه
😍
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/6684" target="_blank">📅 18:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ArchiveTel
pinned «
دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...  https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6683" target="_blank">📅 18:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/6682" target="_blank">📅 13:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuV5lOVR6xPWUmg81F1ARR7I_TBUGo5ZL-EYsv-gjbhPpb7zJwMcpOw9RuEcnuYKfox_f2VfZ4CFPjEa11rJR6so80w7aVuQFkZl3iM05J2Ki_RXDLCiLl7kEodjiQk1oivdBQyB4_JaZuxDzwP2gLZ4yw_3FZ9IerctIjtgTg-HR0MRcj9vATpwvI1x5_-QigRPFLJoSLsarGn20BtXdG3u4aq1TF_D5YxgV4fxZvgEnT-QkOpuAtJY1NVAHlIejv32TJxRweeGVwSC9RETirt0s9pmg-0NMNmSVqfElA3DxdokKpSI9cfCET1STYVGV9GcesiDyxFMnSG820OvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/6680" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/ArchiveTell/6679" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...
https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/6678" target="_blank">📅 02:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzYX9HVNx4_GIqIeNzpkiZwwfIg8Uk-ElOeNYNMDb8Rp8GBKDl_BAlPiHavTBypbd_NaCjL4i58f5_YgIu8JrBg_D9jtjc3pC4WKxONLo4PbIAgILYzxmKAU95T3OxGtEAoZHI-g5qaqXPveIjzrDmrT8UNOgM2SMzR5wDNcia6_Ce7oCms1U4lL0fDKi6FZaBXYaapAtzt3i7r6gs0t3jL1ZiIKGSOCTn4jPZUj8lrfoRMhyz--eeSiLuS8R4A_M-RJH91pGpdxWNIYMzIrFfbwtshtpSiwx7bcPnkY9UlnioC8U9Y3norhaSc7UhgaUoIfnTbP7Db7yOgMFNkU0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توسعه‌دهندگان چینی GLM ابزار قدرتمند ZCode 3.0 را معرفی کردند
😮
این یک ابزار همه‌کاره برای نوشتن کد و تعامل با عوامل هوش مصنوعی است: همه چیز در یک پنجره جمع شده با امکان کنترل از راه دور از طریق تلگرام.
این سرویس به صورت رایگان در دسترس است.
http://zcode.z.ai/en
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/6677" target="_blank">📅 01:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVq8X5X5196tZRv04SpUEOTbIYFhhZlcsHXljvtBCjp_ZsbgACEkAcu5LEqLh6fvEW489IMtIf_4n0NbiPTvUeZ8kawvD10ou--0SkA1xf4QrvmEbmZeKaGcF3jlNRiO-J4J9hrNHou7lfADXlfxamJV-mJX_0NBg3HZE7C9EIseASEwaS2InLcqLrvgNHY_nzS14ZDO0yM4afU0wtF0YefTBwsyYLiVl2Fyl86ULHuXrZF-SpBOlbcFvcY_yGlXf4_O6X5SvDELK6fqXcxnXxKun3B573mtUiNipgjqmjePHBEh_L5zEM9Yubv02idg8sdx-sQICnFbcwieD7BV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت Fable 5
🔥
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/6676" target="_blank">📅 23:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=ZSg9Hw2ZWYWuHJXf4OtrF-AzDgNyR1y3l99XkeXrVw2RzmLKBNwKKW64fuHMYyvpahdZ7tJU2tkGvELCMEEX_Mw9CfyCqEVpNObdYrX2eT5b1aV0ffT6I25JW0csRo1f2eLT-oc_8q6eiy0AaOBapZUEQI6KtTNMVZHxXONi515XL50nz5qZEP0XVaOdzY8TOJOkz2dpAc-z_gNhI2wYQrDAK0SvOu8eqHeejdpGZ9lAFvaTEbyZfvwXcE67ElmNagbFP1duAkmOmM9gi6MKLDdhhB33BWbKBxTNp31Xm-WpWwAdpWbOn6zHkqH8WLxAEya217m4LChSVxjyl6mjPzkoq0v3Afgi5I6RyaK3N08M0kQXtmaiRfzcSaNiL7J11MMpLckC4-8ZfvMdsTCHZduo4Nf0eWfL678zvXERY4lGkV633Mz-utwFi7fV0e-ku7zMy3znptMc3Ulvkp7dZpxgavXCxhFHGYXmnnRK228cAy-M_R3dZGSqIOQNUAwgpAUHr-1kTFeEe7NBbNnOFVTnxo16dOdIn2b37SHzmE-KQA8AMhBgq8U2DKdd9mUPpJKG2woRvx3dutEzAPlkj9lrZ-8E9Hlt2TCa0n4M-Jc1vRdbDDijok2WYcYMCpD967MlCtD5HNpyUEGcVNVN8gc_rVoSNQ0o8ltrxTLlktA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=ZSg9Hw2ZWYWuHJXf4OtrF-AzDgNyR1y3l99XkeXrVw2RzmLKBNwKKW64fuHMYyvpahdZ7tJU2tkGvELCMEEX_Mw9CfyCqEVpNObdYrX2eT5b1aV0ffT6I25JW0csRo1f2eLT-oc_8q6eiy0AaOBapZUEQI6KtTNMVZHxXONi515XL50nz5qZEP0XVaOdzY8TOJOkz2dpAc-z_gNhI2wYQrDAK0SvOu8eqHeejdpGZ9lAFvaTEbyZfvwXcE67ElmNagbFP1duAkmOmM9gi6MKLDdhhB33BWbKBxTNp31Xm-WpWwAdpWbOn6zHkqH8WLxAEya217m4LChSVxjyl6mjPzkoq0v3Afgi5I6RyaK3N08M0kQXtmaiRfzcSaNiL7J11MMpLckC4-8ZfvMdsTCHZduo4Nf0eWfL678zvXERY4lGkV633Mz-utwFi7fV0e-ku7zMy3znptMc3Ulvkp7dZpxgavXCxhFHGYXmnnRK228cAy-M_R3dZGSqIOQNUAwgpAUHr-1kTFeEe7NBbNnOFVTnxo16dOdIn2b37SHzmE-KQA8AMhBgq8U2DKdd9mUPpJKG2woRvx3dutEzAPlkj9lrZ-8E9Hlt2TCa0n4M-Jc1vRdbDDijok2WYcYMCpD967MlCtD5HNpyUEGcVNVN8gc_rVoSNQ0o8ltrxTLlktA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
واقع‌گرایی GTA 6 شگفت‌انگیز است: یک علاقه‌مند صحنه‌هایی از تریلر رسمی بازی را در دنیای واقعی بازسازی کرد.
بعضی از صحنه‌ها عملاً از نسخه‌های اصلی بازی قابل تشخیص نیستند
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/6674" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOqbPH960hkGRoj_I1lyMSXRnJbn8sLVL1gzVChHjUKkKBth3xuwUithyAyCwx6uRQnho-KPwVaF334LNotPO0Ha9wZiMZbN_o6JL1cYJpTqHgI2TXDJUbHGd7FOysZ9kgai61MyWz6DYMfE1oSm4VtEote2-AY2rFrJpQn8TMVHRN96leG8mSNB9lM_akDquXv-_au8v63DCD-0VvLxE9Gv46-Sa4w4m1lW5tMuIMPxspTWEIJt7mCP0tUNLmn4U4TYN9oIRkBtDiNDMr5hVNrGNgs248G3ESTQhrxVa3Qa9XplU9g36mhvThB8Ps9NoWZ1WrO--UjZut8_9tyk8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون هوش مصنوعی مهارت خودآموزی (self-learning) را به دست می‌آورد — عامل یک راه‌حل پیدا شده را به خاطر می‌سپارد تا در هر جلسه جدید دوباره آن را جستجو نکند.
🧠
وقتی هوش مصنوعی با یک مسئله مواجه می‌شود، این روش را ثبت می‌کند و علامت می‌زند که دقیقاً چه چیزی کار کرده است. دفعه بعد سیستم مسیر اثبات شده را دنبال می‌کند، به جای اینکه دوباره گزینه‌های ناکارآمد را بررسی کند.
https://github.com/Kulaxyz/self-learning-skills
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6673" target="_blank">📅 18:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6672">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMeIAC2uHVseuHJ_cg_MwLudauJmcW4ttJiPFb9SDW00I_3qX02vyl_AnUWooT74_tEglQOvexxWSxb1E14KiDrvBUx8YCAlLiphLf0w5H6mKprXj--PtVzpRFWxOw9RUwxPf6IDq6BagjcJy12dHt1_O3y_3lsOsqWGLOPpsXX5n-ZSgxepL0uhrMYVaOcN9M54NsI2-4jKsj54lRkx0x7JABXcPoQK9qyWrnz_9uT9VXn3yyinYjcvOKxOoNj0O3yQstP0N7z3rI0WlSoQp9R8mTW3BLdqPup_2D1S--6_xiajDpkRRZBxJNQplkNlW9oF9g7pmQKiSgfBgMp3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">RevPDF
ویرایشگر PDF سریع، بومی و متمرکز بر حفظ حریم خصوصی به صورت آفلاین است.
این برنامه امکان ویرایش متن و تصاویر را مستقیماً در سند PDF فراهم می‌کند و همچنین عملیات‌هایی مانند ادغام، تقسیم، فشرده‌سازی و تبدیل فایل‌ها را انجام می‌دهد.
تمامی عملکردها به صورت محلی روی دستگاه اجرا می‌شوند و حریم خصوصی کامل داده‌ها را بدون نیاز به اتصال به اینترنت تضمین می‌کنند.
https://github.com/Pawandeep-prog/revpdf-release
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6672" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6671">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=bZ4yXAMCUDUudDaMTdgesrBEa892JQFOGc02uspJ7itdKY-gdUmydgEpNf9egpy0Yd8NEinUGc4kBbaX18p0fytGSiE2YX8wCH0Mgjl1nGw2fa_EqWyINTVVfMvEtbfzIIOnWBNRIplvMrjGwXuGZnBQngF3dwJoJ8QpmB0Vzi95iw0-mdU9C7COJC5MEVQFQr4lsj_l5uoKy8V-ZWfRjda465o0WmYQ88dd8xmd2JpeImXYWrE8CBjN8K3NsLEKKfeff8zzFXRW_I-VZwdIA8Lhh744uGXUkZCjRVQWf37z_6IXSOJNeRWK4q8dF0nsrHwX522UODnrkhPX8scFKIpjrGaKpvk4Jtgj22j-dmjvNHe4JYJvb-9dZ7htYy0opp00RJQjMX0NQdRNd7HMkQhZAKhnpLhvrFDunyjLuQg-FkBTkp7hiJgiAZIRHZ6xElHPJvDAGta9eJpC8QPM1PJQF8usDLNFfKTk-izlAo0b32cBIvG_zyadPdf4yxJGBtuv7shCqRZVjAl0XuysXNmRileUcT7Jybrhaf4Ak5GqPTFa1TTOL9YnDY7sMc-nJbWz3rNh_nKMGl_zB34I6Gja4lsxtqnZmh7Of___M0JA539DRna0n0_Iw03yJD3oxeBODzTy2dvOxtGHGXkKYrzwxjv5KlBid8flu2mY79w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=bZ4yXAMCUDUudDaMTdgesrBEa892JQFOGc02uspJ7itdKY-gdUmydgEpNf9egpy0Yd8NEinUGc4kBbaX18p0fytGSiE2YX8wCH0Mgjl1nGw2fa_EqWyINTVVfMvEtbfzIIOnWBNRIplvMrjGwXuGZnBQngF3dwJoJ8QpmB0Vzi95iw0-mdU9C7COJC5MEVQFQr4lsj_l5uoKy8V-ZWfRjda465o0WmYQ88dd8xmd2JpeImXYWrE8CBjN8K3NsLEKKfeff8zzFXRW_I-VZwdIA8Lhh744uGXUkZCjRVQWf37z_6IXSOJNeRWK4q8dF0nsrHwX522UODnrkhPX8scFKIpjrGaKpvk4Jtgj22j-dmjvNHe4JYJvb-9dZ7htYy0opp00RJQjMX0NQdRNd7HMkQhZAKhnpLhvrFDunyjLuQg-FkBTkp7hiJgiAZIRHZ6xElHPJvDAGta9eJpC8QPM1PJQF8usDLNFfKTk-izlAo0b32cBIvG_zyadPdf4yxJGBtuv7shCqRZVjAl0XuysXNmRileUcT7Jybrhaf4Ak5GqPTFa1TTOL9YnDY7sMc-nJbWz3rNh_nKMGl_zB34I6Gja4lsxtqnZmh7Of___M0JA539DRna0n0_Iw03yJD3oxeBODzTy2dvOxtGHGXkKYrzwxjv5KlBid8flu2mY79w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
«اودیسه» نولان - تریلر نهایی. این فیلم یکی از بزرگترین آثار چند سال اخیر خواهد بود.
با بازی ستارگان: مت دیمون، تام هالند، ان هتاوی، رابرت پتینسون، لوپیتا نیونگو، زندایا و شارلیز ترون.
اکران: 17 جولای.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6671" target="_blank">📅 18:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUZm-_LuQs9P9RU6yz_-AMNxhrO3vI7i5MBvYxfC8l_G4xYZ-mu_TKKEp59aC7rbSmQQdwfJUOLY5FrARVNrH1Z-RlAo4RHVACbjLUd4Zhrtq1yOtMgkbnersDCNsU1UXMZKvOnf9AekQEZw-bm0iZbeLP-A-fFrvups7Qgz3eteim5tip9Agm84b1Wl3cG5ndZVCLXp7zY7j46XFGqtGAGzB1K8uMzSepv4IZzdlek-8IYOIwCIc6QpfOMG57wTx1CDluNK9fw3sK1tNfc_19BJ2xwI9evmn4icl1gKqPOPuzlVTsBoKj5vgWqFwxQwIQQamnZNnUayUwUBuJ0tmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض چند ثانیه هر نوع کپچا را در سایت‌ها و منابع دیگر رد می‌کنیم
• به سرعت بیش از ۳۰ نوع کپچا را حل می‌کند، رفتار انسان را تقلید می‌کند تا هر محدودیتی را دور بزند.
• با چند کلیک روی کامپیوتر نصب می‌شود، نیازی به ثبت‌نام و نصب نرم‌افزار اضافی نیست.
• فوری و به صورت محلی کار می‌کند.
https://github.com/clawdbrunner/captcha-solver
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6670" target="_blank">📅 18:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268d269709.mp4?token=lou4V5sohkVeAb7hE7tUjCxPFmtdQvraJR8C9BlFvPud5t27pLKstFiTxzAWoc46VxqpNvoggPjjCqENZFwZAqKJSldExE-6KeSWNnMyiimCSKnFkTR09OtoKJVEvXh0g93Bq7-ySXsM6sMRC4xi7uJx6F1Z1Lv2zrYwTjrJa5SWUQ7h1Up3bxsvl6SKxu8G6qAsvamhWVSqygf5yP_W_ytaRqbDuf9UdM3teqDLtC8SxydVCzHieHNQN0qPz0IVwYPx5HtOUj1YK-Xupcd2MHxCGdmZBkI08ttYz4frotAFhG9ns16vih6mBRn9GCl0TXTZZksllreBinojz5Exmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268d269709.mp4?token=lou4V5sohkVeAb7hE7tUjCxPFmtdQvraJR8C9BlFvPud5t27pLKstFiTxzAWoc46VxqpNvoggPjjCqENZFwZAqKJSldExE-6KeSWNnMyiimCSKnFkTR09OtoKJVEvXh0g93Bq7-ySXsM6sMRC4xi7uJx6F1Z1Lv2zrYwTjrJa5SWUQ7h1Up3bxsvl6SKxu8G6qAsvamhWVSqygf5yP_W_ytaRqbDuf9UdM3teqDLtC8SxydVCzHieHNQN0qPz0IVwYPx5HtOUj1YK-Xupcd2MHxCGdmZBkI08ttYz4frotAFhG9ns16vih6mBRn9GCl0TXTZZksllreBinojz5Exmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شبکه عصبی Gamma به ChatGPT اضافه شد — حالا می‌توانید پرزنتیشن‌های زیبا را مستقیماً در چت بسازید.
ابزار هوش مصنوعی محبوبی که صدها هزار نفر در سراسر جهان از آن استفاده می‌کنند، در ChatGPT ادغام شده است. حالا کافی است ایده خود را توصیف کنید یا متن را وارد کنید، شبکه عصبی آن را به یک پرزنتیشن آماده با اسلایدهای طراحی شده تبدیل می‌کند.
می‌توانید تا ۱۰ اسلاید را به صورت رایگان تولید کنید.
🔗
لینک
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6669" target="_blank">📅 17:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebcU7p4OrtW8ioM5X3MJc8FExpO6cZxMKVrkemJoAx84i75Safy3U4nhSmDMUWO5YgU_YIqW5htMR0lHdkA7_28si7GzYCu-jOwZBvXXBP0kgu_c7gobGUAHiKYkumsfriSUjTuzrsi1DK7CBKjyhJkcyFsbCXBPv5XOFuSy5xNWGZnrUFn6hI8as5UjKREVTSSzma5Vl2D7cYMeK7uZ8Y84gR4045EMS9Wsi-iXuZlx-tqDSLMFasjbXdXipXEmBdwuSnAmBvShQGqWHIbnRskHj1ewDsfgWRRDQ09Qd_WYjESDu6Q8ZdhVBJCzqoD04rEkx_u8zT2QD9vb7J0g2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دیسک‌های بازی پلی‌استیشن سال ۲۰۲۸ ناپدید خواهند شد
بازی‌های جدید فقط به صورت دیجیتال منتشر خواهند شد. همچنین سونی فروشگاه PS Store برای PS3 و PS Vita را خواهد بست.
یک عصر به پایان رسید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6667" target="_blank">📅 17:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6665" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVSNSw7ooDMLsxvOQgPG2FtdXFqJVyjdDza8veE1b4yufqqRJot6K-8MSj__G1Pn6Nobn2wyQN3RJGeENkrM2Tx-plmuNgngv2_Qf-H09zGd11Vo7Q6UNaMZSgur0jcYvi05nsGQfogq4xehh18EaHzTG3xj6GG3keKfvXRObwqxKcnB4qpZ5JHpF18hWdU1BVhVUn3NWjTzdYVEh_k36azXLtzVGmMTdasRBuF5_2ZTJN1eIzLfv91ejSHQaURAOMtWsL4mmmtmFLg3RkjWUPqiIgoZctllikpbwb2tUOqKwdAaMYFz1ed7syIjeQuUgg7f9O9eNVevJGWBKkh2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اروین یالوم خودکشی کرده ظاهرا
😐
اروین یالوم نویسنده و تئوریسین روان درمانی اگزیستانسیال</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6664" target="_blank">📅 15:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ep6EI4H8tYO1WhgI2vlyzFj8HegNemA2-lqX-x9BNBYmVjokXBXAhlxwJhJzBXRDv7WSsJZxHCqppN0pFGJROrvoJutjhWVL6yR6lUD-xeholHNqdyE84TUqSozX-HlKAyrmYeGOjL5cRILySGaAkgifL7f2wli9sOP9wicGv8STYcSUQgpbRhGBUPPFiWcI29Wc77_0Ll8aMxVwER59Gzs8M3cuNYU6e_J0bprrsB-I4U2Rs8D2okQCcVGpqAql59FYMBxTo0pyCbfB2WEbkJGqXdW1hqIzD5KKxvcsVk6iGOsruUoWaOaXG8UHs01B3D1MMFoSqqZvMWDEkY-EGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر سرویسی راه‌اندازی کرده است که پروژه را از نظر سئو، جستجوی هوش مصنوعی، احراز هویت ربات وب، MCP و پارامترهای دیگر بررسی می‌کند.
سپس به سایت امتیازی از ۰ تا ۱۰۰ داده می‌شود و یک پرامپت با اصلاحات ارائه می‌شود که می‌توان آن را به شبکه عصبی داد و سایت را بهبود داد تا امتیاز خود را افزایش دهد.
https://isitagentready.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/6663" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4eF2012K0aCRlq8QfkyzmQswerO34HRt57uUgBK1um6FEGBvHnu_V2Ap7VOog5JRPLBdkvOE3miSjae1fUuVSzMJAaUzvBWVkTrBxkaUo1yOFNAN1CKHgbH_VNIu2b13GSOK5nZ9Hjrllj0qjKavtT72-5HLkpA9WWefDCm73IqV11rZ1u49OCi-gQXj0VODDcJBdBYIrOe8lcG-CQP9IJUJr_es9Y_0W-hppAAeVY3x5S35PaeWEe8lGuApUlnhArq8MyQTvWyHdSyc5p_hq6JcKHiaoHKfsC6gjHsv_5kWk3u_SXkTH0YuTA4stnOoIrXfj1juW443CnW2zk2dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع مفید برای توسعه‌دهندگان: در گیت‌هاب یک فهرست عظیم از APIهای رایگان برای همه موارد زندگی جمع‌آوری شده است.
🌐
بیش از ۵۰ دسته‌بندی موجود است: از آب و هوا، ارزهای دیجیتال و مالی گرفته تا یادگیری ماشین، نقشه‌ها، موسیقی، اخبار، انیمه و میم‌های بامزه با حیوانات.
🐱
💻
https://github.com/public-apis/public-apis
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6662" target="_blank">📅 13:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8mvUoS9a5pfabpDQucTnu1A0F9BFMM540rlGWZmhtSIx91AMkj18N-mfgdrIgUpc0Rou1LDSufurLkF5IDUQid23jh_T__yPlBQg2Yr-7XmBGsbUr75w_FPEPfomDjE2oDVvVDJtC8xD7z6QXCD7SxnzgOqrInEgivJCaOxf2f5N3J0dsV5a9ZNCzPc-GOMGLbaD08TNUdLECcpfeoMwWdtwXBmgOCDxkiuhEziitAxCZUBYVZaCGldl2yDys7bjjfFySYgzsf5o2N6qOktQ8rpmvQuj5OxEMp-D6048eHZqheaCA2xrrURt-C9db1NjoOrsG_NjS9MeDyb54EZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2F9JJ6rKdLUiwvPTA4Y9NJu7l2HpuUzUx5UcZ7C7ZvPmHUCWmoL9nl4dguGbcmlrxPFtfRUbtOyFUhiiiONJcxB_HUDGViIpc08-vgg2_WaIGhi3c383H_rLboPsOpMnQCAB__p1AYbu0oLPNW6FjwkyFkOXcyEeFjjQ-7LP6IXPUkorIs7Lz6JriaO4_BsYW40EESXYInI9Voef73_ubJ0JKMSSsgamyIVbZ03CJedK1qXUYhXBBXzqSyn0LovWfreIGQJGCjd6k_M_Nbru82YYD8rr6hpma7egZu6Ozh4U2L01Xl7OWMPQMZ9Z7Ft5ggCiDeups53XCr2NC9rmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vRUTBevtyKuMqc3cLKWYk9xGGSgUMaensGLAH-uRwWNve9wDOIzRUnYmMbgsQ5SePfAl2sFgl-RpxbjEPxVg0XOqhFUQBM5ASFayGeu9NUabj8rvojojH4hDibuV9h9aGo8fMEkGwzW7mNap1oGj4HWlOQoxIMoTTe9wc8E9N5Fkm2o7O23TdjORPq1Mno532jdFm9eKiYDlTYWBjgdyMe6kyangui7hIUNMiJ0bZBnvMsIbE3JUk6wo7l46OAgUPNW1UY9OCRvbiM0ohUqX-khVN3Jen0OrjmAEa2tsjE6P8-65Gj9CGJvgJXQAZb9FoSyMRieyDdXN4NaL7O8EYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Km96YQE23jvUGbi2YRin14euiKzMsoUCwtcJNtHn8MKdDaHfFbsX_Tuq3Y0qu_syEctktGcfOTmZI_Wwm3HETZO-Y81KUHcdGz2SjHprIkABsC7nCukwfNBlLpbvr26i7rXB-ATt_9kuWxoq7HFlLfUsdJbfUILzidENVTb6OQk4GbcN3H-uCwWlB21XPqmd8Z8HIrhp6EllbM1ZIHATUEL_O7aYqp8n72RPpJ7c_ECpLD4F0qB9ryz_ktG1S21DgbuRoIl1U39DsqhiF_IYmxkEDGrNDMAohHJPM3OwBDcK_aG7zzyLKl2a5I-B2Aywhivd8cbQvyIm4Xk07qCS_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">PlayTorrio
مگاتورنتی که همه چیز را دانلود می‌کند:  بازی‌ها، موسیقی، فیلم‌ها، کتاب‌ها و هر نوع فایل.
https://playtorrio.pages.dev/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6658" target="_blank">📅 09:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl4khzucsmQ0oIGJgRAeKwHgBRE7EJdLlrCToXmou1kCzz2lpe70wtMCrvL77eF8WzVN8idPmmUZ2OXcdohE2XqmhXOZUWSqj7OtgD-7qXnh1KcASEAgvsMl8ZqqImlYj2zGKQmH0pvqVkdndCGSlRtMuGiC03ifzIp8jpsayvgccdShIsrHKsEG8UGpPx81ZW6nSZ7ucQy2FNKy16RtHE39Ux5F6o0BIZo6k4i3Br2kdgBQzH3UIDpMyEdOdSsWmeRuEA8Idv2zZTiwY8cVPjN28YM1eRwFWrJd0M2LJ7UCJ40CH7rCS758cYnOYmcB6tlFgXpMCMkvO1e4agwZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود Mythos و Fable 5 برگشته‌اند! دولت ایالات متحده این دو مدل‌ رو از حالت مسدود خارج کرده است.
امروز Fable 5 برای همه کاربران در دسترس قرار می‌گیرد و تا ۷ جولای می‌توانید تا ۵۰٪ از محدودیت‌های هفتگی خود را روی این مدل استفاده کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6657" target="_blank">📅 09:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVIopopYu2AwbfAVwXj6CJT_PBghKSfk8dF3sPoUpRiMajBBDjkaePcG4vKfXO0SgpHnlKQ0LfVyfbnEchh8QdAGgW13eTGh4WWDWd4mI4ovIszgJ1qsbiTgamBIrU3UEi4qXmdiurX8ctX1BhiWQ-Kjcd6RNIDcZaMdqINsqALMAUQ0zsfJZYEKA53qWox5Knw6yuJtlwHNEb40vQjZy8dNLW-HojVWvBhq4FX7_ce3GFFB04SE-4NjsSG06b6orwq3OxCOjeuo4UWNR_j3DTVGhchvPL1OzRvC4BeTJARMD9BAcrsVT4APbioboltNGuQxGmBpM7Pyigf2wtHzdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود اوپوس بدون سانسور منتشر شد!
توسعه‌دهندگان Qwen 3.5 را با داده‌ها و استدلال‌های Opus 4.6 آموزش دادند و یک نابغه شرور واقعی ساختند.
• محدودیت سوالات فقط تخیل شماست.
• می‌توانید هر چیزی، حتی ترسناک‌ترین‌ها را درخواست کنید، اما مسئولیت آن با خودتان است!
• به صورت محلی اجرا می‌شود و بسیار سبک است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6656" target="_blank">📅 08:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6654" target="_blank">📅 05:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الیوم اکملت لکم دینکم
🚶‍♂️‍➡️
😂
(حس تکمیل پروژه خوبه)</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6653" target="_blank">📅 23:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6652" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atmPPP4hmj78YwGMmjv_Bp5NjUHB0hnxPfH0hXkqH7BoVgT-aKi5n1kUp8_M24bWRJave_IpNkrBGyLSfvOaAEaNdDW1XX8_tVkyIbftG3_-0NJ9RX2zDOFKUbfxiYGZJo9U-VQJxm-f7bik7arXHTDjrRjPm-PkAGe1w5ekUjIJ3bRRSqPg8RvbNe-FAYyPA0U8BLLvnZnENu7eUaH6m68XwzfEJxhwdl23o5gcj6_vNr9UYJTo6EBpqYwEV_a2z7265yApyZMwiH9HvgA1QinVJc81_VV_5TnYPYpd_FK3p6Mo-r3bQo3hrLWDKawQL9rjurtRW2GKvuEZEvyzkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=JnpHyg-Vc40</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6651" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6650" target="_blank">📅 23:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6649" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6648" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سورپرایز امشب
اختصاصی
🗿
❤️
از یوتیوب
تقدیم به بچه های گل کانال</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6647" target="_blank">📅 22:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvwXF3O846ZOUbMzqJmi_jnXaR8S_nNJWRIsh1Wr5eSzvv_o3OgadsBawNAdypqljX5HEBkM7Vmw-18FEwYhl9CwSlig0MdsYHBgjpbSQKpjU8JuhCdVINgkMbpDbLSpwTUwVs0Chfd-65wZVnBH9RwFsUzyw_PmRu0alw9MIKr9_2R7iFBhgPCIuEbY50D8QQnpn8TFuTCxI-IUT3X8NfX9LpjzaU3dyaSx58PsLWP0gbFC7dBowrHuXsFIQF46g7vI5FRmb0rwZDgoDw5owC84iwz2C1xO__r9yhphhdEWqwOr_L5gs55Wf6Iavaj-OTvFPZxNn-f_3aRJm0ETsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude Sonnet 5
منتشر شد!
مدل قدرتمندی برای کارهای روزمره اکنون برای تمام کاربران، حتی کاربران رایگان، در دسترس است.
• از نظر عملکرد بسیار به مدل Opus 4.8 نزدیک شده است.
• به مناسبت انتشار، Anthropic همچنین تمام محدودیت‌های مدل‌ها را حذف کرده است.
https://www.anthropic.com/claude/sonnet
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6646" target="_blank">📅 22:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqJ-A8IA3T3DUE-lBKSdcd3EjmE7r0lBDa3fvAokaGmNBxMmPLwb-xj23r1ltZpi1mGUlFzFBQ4yMGiq2VrwzeSnH63vGCAB7ffiLteTrPiuNDkZox7kNgJAKc3A5P8TpYYUaeUl3pSqYlbD6WvIuY_sVgEy18H_Gk9ijiq4ArXPBqWbTPdW5Mk018YJCPjqzzYrrSNGiBSSWFjC1BR2lL3Vqpa3KUho27Jc17fCfEafspE6lIZbJv2EtlOL4KfkmNl6mnXQhL06o4rf5qBbvGeWAxc9dm1CIslN-JBAbGbkftB51p8zMkLPjqxSbgUEjwt-TNwtFYDRDFhZ0LJXoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lN1RRW_2s55FJMEk0nbletS82Sdn--bNT_CTKP7XeVGhnLpYi0R9ehfHTmEvf1kT0qVAysTb2vr5XNkdwyKQi6jl9j5_F0h0ZW8vnFlHuRUlLekUusT300ZNgJ2xJusOK_hvK2XIz92XJBIVJgNOVJkJBrqlZxIjzMR9AjodfoyLahFTJw21R-X95M0Uxl10PHmAKVjUJo1gcCbIz9S6UEHkYUQ0LwsB9Secp_Qbk7xjErW6LQ1fUtb78WWOlIlaemoK0PsGRUT9tr-HAcDyYgjbKDtkvrI_RuEPfvMT_KPU8pi1kppownBxogwJH0k94nGAS4xcjNM4J6Fv4qnStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itmEVUOG3i1dobSqqoSYumkpOIuxPojooOWBWsP7Voo30mc_KAvNOOFkyjjvv1wuDGWIQLTq6b-Izyauf99L9V5sMjNyBy-6ZltM919AUvqglZ-pSkxcNaeYZaW28E5lE4FSp7f6-GxAhl43DuZjg6KBfVjVFkkHdvHy9R8tmMy-G1cO-67-E_2El-FT7zG3ixoTavLBVueb8CgDL5hSpcgZyR8wFfNyH2PGDPyYHbE9AP2dmH-_r4C53nF3oLNlgFto1N0XNciP9nb2uXX82-GFFlJ0Sj58GWNcOWD5rPHZKkzONn9N31P8asFw4Pb5GozKQMvMBpCH1gEcPjrwvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=J3mWFaSb-XfQUJXOQhTXEQ-3fWo41ezs3gyOWfHSE9o-V6DSDYfLyhnN-GGDaZJxwc4RtFV1FExyDF3JWe7l11_Mz3kYcpL80_7nedpqwcFEKx94Fn25KmaGlnaK3ZOtTkZA3QafDlTcZxxMzKgGpvAurA-Nu4trYdDjJCoga1xPmN30dAkSfMROBby9aYUAdtu4WkH9SmLQ-b0oLzLgE1uwPQvDhni_5FC9ax17X_UuDl5T-hO6STS2ZhfXWCHuMIl6iX1tao8qJX1-b8x2Cg2_7IQ5emajE9xo8mmX1xsP3rjsXRWmb6C5_Jz-GpBu2jhOiRgW1HUoXNX4GRbIKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=J3mWFaSb-XfQUJXOQhTXEQ-3fWo41ezs3gyOWfHSE9o-V6DSDYfLyhnN-GGDaZJxwc4RtFV1FExyDF3JWe7l11_Mz3kYcpL80_7nedpqwcFEKx94Fn25KmaGlnaK3ZOtTkZA3QafDlTcZxxMzKgGpvAurA-Nu4trYdDjJCoga1xPmN30dAkSfMROBby9aYUAdtu4WkH9SmLQ-b0oLzLgE1uwPQvDhni_5FC9ax17X_UuDl5T-hO6STS2ZhfXWCHuMIl6iX1tao8qJX1-b8x2Cg2_7IQ5emajE9xo8mmX1xsP3rjsXRWmb6C5_Jz-GpBu2jhOiRgW1HUoXNX4GRbIKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6642" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcbdU7WkZ7n3ZHDcGMuB0kL62VB3JRSE2UUnzABedX8fgDxiqbv6jRHUhlLuIfgPjT9W3duiCoxkzzhme5ey9j8lsctJ2sYKKO7jd_4c98osLToc0aIQLYlQ65YqQv2tVwKxS_YeKjatud774EneHvGOtLs_ZQqc7X75Xp51g-qkrAzQoQ9paShS0Ixor2puCC1GDzeF-46PRifRhLRthRQRSZXGXvB82ftIYJKvYEfpaxAZvq0PpJNwMMXGZqUkIp1M8pYJKBpsDiH4FJG8985YdFDBo8ZNNNSTpE-iqMNJRHnEwAw1YedxaaGk9i7GK-8U0syZPzWD0Zdwy-KqDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی Opus 4.7
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
http://zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6641" target="_blank">📅 20:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=WAVefIEWISTZkdnbfqrvmr7xBsS73zbtba6jRtHJWMBsDEEs8fX4qEMriAO5PdfgEhp-mHRi5IIlKubEzaOErZ4X6Odg2QDML9BC364laOQBKhWaAFJlW-im-x33vKDw5lid0Q5AkUuq7wW8GzqXuUoBnk4a7nLLEWtrbNsoEOtJAC14H0uCVRx34sjocA1YPkrRyTbl0dYac1VMfisMiTzX-8RYvPOuSOYNiY-0tLNzJZWolDz3b44Zmi7KYiID9GjENpwJsgcvoqrdq_ydnyQbiIJQz-gXF076zxjekPLmkG35OEOkA3nEPIE4Dn6R4B0x_HIicwgUjKFlizhKsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=WAVefIEWISTZkdnbfqrvmr7xBsS73zbtba6jRtHJWMBsDEEs8fX4qEMriAO5PdfgEhp-mHRi5IIlKubEzaOErZ4X6Odg2QDML9BC364laOQBKhWaAFJlW-im-x33vKDw5lid0Q5AkUuq7wW8GzqXuUoBnk4a7nLLEWtrbNsoEOtJAC14H0uCVRx34sjocA1YPkrRyTbl0dYac1VMfisMiTzX-8RYvPOuSOYNiY-0tLNzJZWolDz3b44Zmi7KYiID9GjENpwJsgcvoqrdq_ydnyQbiIJQz-gXF076zxjekPLmkG35OEOkA3nEPIE4Dn6R4B0x_HIicwgUjKFlizhKsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقیقا همین‌طور در سال ۲۰۲۷ رم (RAM) خواهیم خرید — یک پروژه با جاسوسان هوش مصنوعی پیدا کردیم که برای شما اینترنت را زیر نظر خواهند داشت
😋
ایده به این صورت است: شما سایت‌ها یا جستجوهای مورد نظر در گوگل را مشخص می‌کنید و «جاسوس‌ها» در فواصل زمانی مشخص اطلاعات را رصد کرده و گزارش را به ایمیل شما ارسال می‌کنند.
https://github.com/firecrawl/open-scouts
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6640" target="_blank">📅 20:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLPsCq0u4zU4qugbLjIX2wZ6MBXHkGavHtRYdQpRuBlVBVPlq_ePdnsJiCvGwFHd48JvMkt9emywkIqdNkKk39Ok39i7UgR9kKktUq0KI-RSSxZQSG1wcre15sBNcjfW7AQZSCQFcuePROYKpjHvvseqkXLJVDzneg6_Tie5MbeRaj4hqjuOSs9DMhuDKhA-d1e3kxABUtHuta604vwBpn7z9Z5bjdaZDsrF6a1LQmivVX61QH76y57D1zLBtzesWQ_A_E1gjBR-K11saJSk6D5VMrZzdK2KdkO65OaqseWfgDZomLaginPp9Gw9LbhNYyS3mXsnGhc6YHw552H4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DocumindAI
راهکاری برای تحلیل اسناد PDF است.
این ابزار قادر است حجم زیادی از اطلاعات در فایل‌های PDF را تحلیل کند، داده‌های کلیدی را استخراج کرده و رابط کاربری منحصر به فردی برای تعامل با خود سند ارائه دهد. این امکان را فراهم می‌کند تا به صورت تعاملی و مؤثر در سند حرکت کرده، اطلاعات موجود در PDF را درک و استفاده کنید.
https://www.documind.chat/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6639" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1ndQ5PL5CvI-secbWpPNQ9yNQXND8ths23g0AiEqBVEEWiD4ZHaiqRGltjyoXcqvfd6qfuCdi28nUf17Cztols2CgglYVmMM4QHJPelPs4yoyoTPJMWHZdMhy5NrQsUuXwBB5IwtWWRHCmJA7pxRyw-Epj4xMcRMFz6gr9kR3WG1Tf1-U2Hbytkq_tCBD9ghAihCAov4X3QjwHXAl4LEdBjy8QTQojPUgRAXsaoGBCVHc6kTHfzVroFFm2jrEUDcX0Qb-OQo6W1C6b_1khZ1KabNP4T2jo3gWNXuEDHqM4zbZFeEoKBZXwvUVM4MnT-uTMRMOWkKNd3VAkIIFj9JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6638" target="_blank">📅 20:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFcozq0PB-Oq3E1hy7XSA1BPhmdSOsAm7-KdU9pD8IKB2kP--Rp7rekhMk3FHGjokOeNEdlmAypkdHTL0_ISRdDSZAbmB2USOFYHSMw6PAO9UJ2D7DlI5g4dKXsOdxOKus3zoxoleW45soMvi660dD0Vc_MX5jCmX0TqCM9TIm4bEd4MSxWwPgGa651c_Ku3Pbtp9FfbhQYQ0HRBRgYodgwRM0a_z5yNMbY3e2An5ruq1k5RCa5mu2jqVwE6udzGW8kmPbupWgvfDHhOfln7YFosdOE8JTOYWIhpAz4DhWuaHBvyZcs6c9-6kQoLnGk_Yk5DNv2vPSM89bxbqhA_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاک کردن واترمارک، افراد، اشیاء مزاحم، متن، برچسب و غیره از تصاویر، با تکمیل خودکار پس‌زمینه توسط AI رایگان
لینک:
https://magicremover.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6637" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_C7fwrmRQ1A7ej6BTeG8SeRxxq_x1CQZzP1BuaiT3a0MmROZ9RGNpByUwGIzEkff9b4xHNB1HCnMy4_Z9vqPWJJxAb5qIRkawCek7vpGjqBwkL-DYhF_51q7HFGJ8zsBv5DQdMfTCmuPkG5OE2QSu6y5OnD1Es7O6JumXW7uXUlw3cc_o3eIm61PySMLdt9DDDjnD6dZrXyGZZQy3ljMWoAyT5X3KrQOYap6ODthjRs9BC0Hg8E1-VBzQ1eynSsR9n_0x2j5-DOLaD_T19D_WnimKR7aFPQO0uKv8ox8XOSrgMmjaE4AjrqJvlXVojrUD3GdLDUUuO1iVMRTpedag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6636" target="_blank">📅 16:18 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
