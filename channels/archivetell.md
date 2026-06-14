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
<img src="https://cdn4.telesco.pe/file/tSSl_Z0Lx-9yWpSxbU4W3CW1FZ8nep-_C2sCvNUjRUppck7dFzkALkDMHPFt7twia05Pqw1SQ90qGVnKJhUfi28m8NKP-0bETY6_SSX0O2KS2ROsBEEnVE4UEdLxt6djuE2lMsGw2l534_7RiCwDv62h6y-B5Tj98wHC1SIVSAQVo8fRkOFeyWhYrGVwbDf2OiRGkvyb9jCBWJ8_iznPd23ymbPHolxFp8t4MTwPnIEKg6ufINymsVTRIHk1zO7LZNn02KKSJB5tP7AyIZmDNLEbYsXCNU3IBWWL1uazJQxvSkNmXC4aFWZXm-GIjHvY5xsk3oxowIuRkghlG0G-mQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.61K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 18:06:42</div>
<hr>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbqTPImMueLyCxTymN9YhWF03AT7MzYUUKIqvy7L7OHzJVFguqAbEETGaAhZwo5mNw9F2KWfecSUCeNZkZ8oSlbdPDUQ4jrQZPK_ywNSmSHpjpZ_AC2A6B29cDvVKop2KpCj-P54Jb38rQBTmDNckJxERJwg5xkmu87WLrdg55CGTL3eydUBoNbGs70DP9MCQ5NDFhbED8qLz74-ibGxxPRaFElC6CYZDd7bknqigztRpM1vZwZKsA8GMxwymbkM5DKpQ-3PQ8Gp_ziAs8HVTFQiLbVLZPJuf_E-UfgucoX4Bwhfx6MJNUate1ZiSOqFlryhNqWe9NkCELsijsLZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ1YdhqOPd08WL2ooZXs09wfNKWod0shur6oPS9d1JN1R0THFLOIrJXfGEnrB38HpI9Ub34dk8yLI7UnUUsr4z2Stnr9Z7ZdEIKxvAwrjZyW-IV2mHEXUnTJ9ZqvzM1R-P8Wo7yr4_ROepHNcjAP6apN1tfEEyeC1zLYJbaiqr-LAZlJBaNbNIx3L3MITLuZMwqEZAl3Diwr9GRgIrCziqsoUkZreG8Es12KYrjGu9in97Urm_N6Mkzr79Nt1_jCevQsAo10vKZiZbmh2_E2CL5guKbRlFQMCRcPlr-xxfMIiexVUlGXV3YhV54mf-KGtxF5rY3xbgiGJD9AKSXqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5E5MttT82gEWfuWLBltRURoswNrn-6SID5VKyfBdNyRNAGZxTqVUBVeUodwPrgmceJ_96rPaYyV9oVGFjbQAwK_Maek6oXu_Kq9YCdYK7pTabaTPMkjs0c7jow32IIr1nHuoH3ggSS8qhNOefDMIfCAeMHpr_wbfMWIV7J3jk8gB6Zrv2_lBLhWMZVPQH1AvZvIXbB8ST3aFO24feu-4eQEeVfvaLPjealQO3fPYP4aqqkUV9B_cTl038rusaFhUVzio3ZABJ-BB8DexpQ0fzZDpAprHpFhAMotmkQw13k9WGA8SKgYWGX1CNJ0FtUUcuNOPIQNiYaVmWrem9oGZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmBfxILFbdHUResqZw3qVFT3kjf3RcTEazo-zsIicC035DABGw5L4Fn95SosqP79QewQd6bLLYS6La_V7uw4rEK1WdDs3Spp1YT5wh1lOlZBA1kQVdPu60jKeBBavYqYqEOWm6_hEyUf3nYtNEHq5IcQOxLM3P4WqonLK87yvpzB7UnT6TH0wL47cBdYZwIOpk3ZTcur8OFSCaVP4DEmXwBDLmaLdD5mZDaleB8lsLsnoErqa1MYwASSt_f-GXeuvGw7Fr_cvRcGgvoGmMz5MZ5F_eGR2c9AY3MYH-Kcc4_CLJbKlo8vRij96MbMIjVkOmyYIWcdvhGvy2VlimIV5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mo6u7WMjr3fxVA0wunLDUTFPFpg9zDQUtjBuqOq9F5baNX9SrfNamsRLGG5070GR5eh3XnSFB7N4DX6Qhz6MqYG0W7tzQn6UOWKfsFahtES5Mt-nABuiaeYvGM59DttDLHXVacgQnkVTIWB9YeRCIiG755tyMWZQzqbx0MXqZOch6OJB8grPVB8yCo7Iph7XvMy8phmD8db1HpL8qajmIChW9nee0H5-0OZPOaxU5npkAjJMHTLAZn6_u39k-i7iF3yeMZiDNOobtDafq_RCqZu_ZeAlz1DpljhPCH3jO_-WdDFJnfUJ_U1R_enNEt7rOdjDr-lO4ML9N7eQMp-ePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnwKRE_N_PGBuDPMQGbXXhkOkzifoSdkS2WN54jJCzuet_Xy1ZPEUZ3Oqsa1DhGU78c6WX9A_Cjd04O1WjhLDGOc9WUDl4l1_AVR9CQgZPt7Iwe6w2FfjSoB9Xp2aKZndKKCtc4sBCZaHBaummTCvkFxmcJ2ejFoHotsXgFamTQDiQp18G9uPF59wCTEGwPapAc-5nJ2yEZ4GRnxgckFaUwCYaRe1cmtmqPe8aXpLauqwCmI9zHSdCB1pYRONjjLaADCe5sFJchJ99DKdxFc6d8PGIRIqxmXZY9WmEaNbbTmZXsv5cvrCq1cksXn2D7ehiwLNejbVSbpLVUrFT-bFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIU-p14hNTFmDcFZ8e5vKsMXt7oCoP4Z07MLNph5LgoHWv4jT63mEw59zvZTka3ICx8dNLtyxbaRl7RVpAM4jtUmK8fjrZ1ckXmSoxEdRjkczG6otHMiLCVd_-yTidg1812Lc3IXk_9LC_QUZZ_reipIkjtmMLAl-cHNbwPOfsGsbLKIuuaFpdp4mvSk9DIkdeWzKhmXu_xTuWUJM9ZNzz2CrGJS5LRZ6y6LrPNJ4mc6c3x7ACMmxUQSWUsM9VaLSMBaueVo5LmN8Ks_f4Wna1KSvchHjxzBJySyNmhHm8BdrA42WgoUmoySCFnNFdiVitclAS48C1N_Aab6532PUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=Pb0AQU7qtWX2BcUPsW2X6ZCBmzdcRHlwiFxUB4kpJbgy_XIgpdfofWEf0c3g5dBUifRSKhcWIRJP9wNTmooQCYW9KaphkqGvGs2FkUO6s6kNb2NfcMNS6XDqsugpXA6lO7EimW0hq8phGwfBNDobRiL1WmeMMjmHN8UTIIvY4-vUhhvZl4dTwzeg8THEglgLYmXIE5rxoYLKYRLEyn7dkAedXQbjRCMGjiFkDOfA5nysKU6JacLkLdYpVPkHskm1IQ3xY8nOoqMgHZIQxN4O24WghiMd49NgoY1YNgmpDdZIk6YWtpIU4IhBe2tINq2H_qGHfz0fKT2bNYx9QeYiOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=Pb0AQU7qtWX2BcUPsW2X6ZCBmzdcRHlwiFxUB4kpJbgy_XIgpdfofWEf0c3g5dBUifRSKhcWIRJP9wNTmooQCYW9KaphkqGvGs2FkUO6s6kNb2NfcMNS6XDqsugpXA6lO7EimW0hq8phGwfBNDobRiL1WmeMMjmHN8UTIIvY4-vUhhvZl4dTwzeg8THEglgLYmXIE5rxoYLKYRLEyn7dkAedXQbjRCMGjiFkDOfA5nysKU6JacLkLdYpVPkHskm1IQ3xY8nOoqMgHZIQxN4O24WghiMd49NgoY1YNgmpDdZIk6YWtpIU4IhBe2tINq2H_qGHfz0fKT2bNYx9QeYiOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbxxY76iggMGez159gzTo-ZezAJFQFfOk2iXpBsOmuuWkuE2bzo_8HIbTWfbwkHnLjL3oKXPBF8yeLtJTBN6d0iWTxZWAaCqu5OdWsPhoPsxxh33z-wrtgr7nVXCX1kIVIet7RovgEJXCg0_sdYn3WReNOrWgfFN81AxVpyChZAzCu95lQnNsEjODMvqOGTs4bSodChQDgSClxTWbgqA5sJ07g4UC8iHLOjpaWTUyuGxwvnRsQBtdIzbhdGhoKfXruRlIyv-0u7yKtGN3jIWy0ZpyrPJe1I5XIC-XYQYjVcRq7hme5lCD9M3l3AGXCaRB8jvUTKBgpVLw80AF_eKMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjgJXOpqmVRRMAdIUtpXteC7__pZ_PkezJ5uQA86CTZ6gU-rhFGasDvu_8S_2mRGUWjVlYyRBP9DMmIU9WXhpmEw6w5oH4ITSnnvoOPCbSAcqUCOF8uNmCMyHCiq5lZ834tfenkb98CJYvtp98-TcWC4O65WKtIm-UdBWwHSLHBenzcv1cxMFinn9ImAExFDl6YoxSThHSTpSuNtTxjAOJa4dMiQCPMpMTnu4vF7boNxEv5QGiGwSmkJUDMjchHqoxPYCqXvpOsqFgV5LOIgTAusZ8AKzmZogATEsGoGAck_wTktN1Q-1LmkEDry7XxIJ2hyvdZ1NxBk9MV92xrS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=bTwHfZyqbG1V6p4H70eAY1onDVIo5_3JltuXovFDqa7rLO7ncNnN6aKEdO6ZVqt-kPIr4-qPE6gJ1k6yp85HmG7welWu9SDVsCuBWFTxofQbwTKW4EdgSoZeA_VLekaDjxwREiifd9XSU4ISJDBLSXxEoeX2E1GjF_05gyPtXW2E9kL8gvaGBHMrVLzH9hYYsxSHtKnLhYLmqIkfd2OkMDzZY-jrazgxbX3q1Tm4aWAAGcg8sUT_2boVGIM0eOgofK8sNPdB99V9F2z_wwNqjpW2JTpUxPVE-RHGv5masBJIcO5cUC8NzPKcr_0k6F1emtA38kCHpy9xwU2_BQYFsbCpi0av06jvf4hPcD1RjOvSllJGxfgf0pGNiqCFL6YZkzLuTUJgD2zvmZMj2BltnZRsw167Cxe71TkCeBbCXi6Xy7___Jcl1Tvvmtcpy44bMV1DCoon3l8--ngLTAgFwqDNjOdD6ARfNRcDrcfBy50vz-O5z4UBWSKc5YFtaGMfXd63Yz2QMKGydE97vyFHN7LqDQ87OZXPreoQCph3YbWLuMAWSYnBiHa6XLKioG_-WNIzj-fYna3TAuyiH-44UhwcjD84aLojAGIvby32hq1ViOvAsku7OYjMFYK7Y1dceL2bnSnKGK8sSz1VGqP5h5BDlCL7gFjelwXVd9E4AGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=bTwHfZyqbG1V6p4H70eAY1onDVIo5_3JltuXovFDqa7rLO7ncNnN6aKEdO6ZVqt-kPIr4-qPE6gJ1k6yp85HmG7welWu9SDVsCuBWFTxofQbwTKW4EdgSoZeA_VLekaDjxwREiifd9XSU4ISJDBLSXxEoeX2E1GjF_05gyPtXW2E9kL8gvaGBHMrVLzH9hYYsxSHtKnLhYLmqIkfd2OkMDzZY-jrazgxbX3q1Tm4aWAAGcg8sUT_2boVGIM0eOgofK8sNPdB99V9F2z_wwNqjpW2JTpUxPVE-RHGv5masBJIcO5cUC8NzPKcr_0k6F1emtA38kCHpy9xwU2_BQYFsbCpi0av06jvf4hPcD1RjOvSllJGxfgf0pGNiqCFL6YZkzLuTUJgD2zvmZMj2BltnZRsw167Cxe71TkCeBbCXi6Xy7___Jcl1Tvvmtcpy44bMV1DCoon3l8--ngLTAgFwqDNjOdD6ARfNRcDrcfBy50vz-O5z4UBWSKc5YFtaGMfXd63Yz2QMKGydE97vyFHN7LqDQ87OZXPreoQCph3YbWLuMAWSYnBiHa6XLKioG_-WNIzj-fYna3TAuyiH-44UhwcjD84aLojAGIvby32hq1ViOvAsku7OYjMFYK7Y1dceL2bnSnKGK8sSz1VGqP5h5BDlCL7gFjelwXVd9E4AGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=tH65ZAU7bQ7roYfF5l5iqN0M9xLQijR20dAIu1_CZ_Q1CrBedpOcLyAHNJ-6KowGmjnSmqGcJS_aLcbo64Br7B7XPQYzw9DZz8pAcyGMaRmI41HX9UlVpvSkPMRBMlsLlPTeYmsshtAyUUllenERqTRzwhv1NBhg44ENqKbiggn4FPth3N9xClvs3o5xCZKYjAaeWvFbzCDd8r8tFJswWNwWGcBvVuqztXBUScrdLIHWWme4SnshM3BUalXtUyvUmKDPSFyn7wuhKHaBFcGmWeiQMayp-wpGV4DqbLXgTkMCAmveO9aO_g2M5usS95JlPd3u453knUiD0BcPZb7uVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=tH65ZAU7bQ7roYfF5l5iqN0M9xLQijR20dAIu1_CZ_Q1CrBedpOcLyAHNJ-6KowGmjnSmqGcJS_aLcbo64Br7B7XPQYzw9DZz8pAcyGMaRmI41HX9UlVpvSkPMRBMlsLlPTeYmsshtAyUUllenERqTRzwhv1NBhg44ENqKbiggn4FPth3N9xClvs3o5xCZKYjAaeWvFbzCDd8r8tFJswWNwWGcBvVuqztXBUScrdLIHWWme4SnshM3BUalXtUyvUmKDPSFyn7wuhKHaBFcGmWeiQMayp-wpGV4DqbLXgTkMCAmveO9aO_g2M5usS95JlPd3u453knUiD0BcPZb7uVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_y7KVg0oAX4zB7pT79sA0Gdw3hLM2NdSYpmIDob_Hv3ZdByRyzzNyNNcSiCvnlhbj2Cec9Ao1ssUriK4wpZzPdbzOeL1Fhk1friNPZQBu9hFQ1wWqJBvJE2NeKTeNpLXIMbq1c-ZE10-k73CDVe7uGLZNCehnq3P4sq_TmAA1Ctxr_dKYYp7mzTxgePXmKSyUzGgfkccbXPD3fk_1rCXXfur4Z4eVNiouKizxj4LfPVau3Wz1JKvdbm9BZ0loKb9n8DFhcxpw2Ler5uo0-GbHo8qzRyPASk9J2TWveuzkvh3hufubHcifYMR4qEhrXLsSxjwBlOXF4df0-V9DqvnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdQTL8wo90SExEt3Tte3BxjCbt5iybeOj2yQP_QddbH7NU_uZfyb7xf_a8aGslfFNfEx7D-zkGKtXBh1A2EwRHeagy30gWC3zdtaYWgPnWj-MNKgP4kD_GShAptIlecG2R-wWGe2Qq8BDgzqIFYQ3-DYU2g0MfIestp7b3TkH8cCK4PRMTz7v-f7e6TAvxT8AhQLDkUfvN-rkI5DhH5bS9M7n0NcgzwhTJwKbu9dCfbrwrqdWWluuzc8MJjS0Vplh71H9h244XZXS5c-m9oynO9WIdGtr_Eu_67deUFj1uMJjhma_ANgm1WhOiUFuSQtehIkNUNzdbdAWKV_LLEhYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vgbtPSG-9RDb9pkZFxgP3AYsoebMfAQrhEGlP0nBaWDFNCVT8bSKaYeqaAjupZDru0G8M_ovAuTp_fFFmB0GRibhVrwl4EFdJdFx3_yKKpvyDZN6CnnhifrvJkiWJG02Cij3-nHZXvEpbHNPdsLeTXiwjKm7zh4u1tQxojq0dGRiJcybOn0Qo10qFTNotSsiXG1xlXhohHWijShwqxuUTAm2bsfWZy95YLxikkGGvGy4vgrTrhfhO8tL34gy1mNUWJ7bDH97qRF8F8NnLGnMyJjH27lxwfzmvcOJEg3jqKuDUigwR6zE5t66hSrEA7fxKCDHETmu2m3xKpg-bSTBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYB1AxEV17iVVtlxSCQZA1Nod4GC81n2IMGXCehticCKzMA2QJspxaAg3caC_EYdbZf9Boo_bZ5TpS-_kX7XMbJqH--wLEH4FgtvC41vPZMYf7HMYkjS38Qa0q5LDTeYMGmGu8tLpt1-aafyKtNUXRE65BFR6Q7s1U31Oc1aJYYPJ_YDBbk_9bO3G7QiLd3k0_RAcK87yhclw9iAfRtOgAVQj0aqcn-EpVoizPfT0VhTux8gBKjYOCsaNnlw983QJf3wq4lbyvUKjcBxD4rId69z2wx4o3fAwC9d-DYVRnZS9T0QIpBtLfuWdBCjvLK3zvy_79XSNBtB2D26MfHzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqtPlCX4Z8i8IoWIDgRAKs6pLf5ZFN16iIQDp3xH-V_pvuNTINqj9XjY8N6_TLKd0qm2GwxR5tUw-3h3Xr5VwfaFKUK-eP0Fx19WbIS4Vzim6hKT4xKW8T4DTJm7vWSKN-_iBQCAOTmOtTR2hltEqHDpiSn1O9mHnaejzUibxJoMpeFmpnV9qZ_WS588DW_vuNoYnr00JwJ1gt48qpQWC_5h5WCV0cv_b5IMKaPJ4Ihwpue9wnC0GgOXi6KLFs_RhqGYdE7H7xzDI44fVuq0EV9CBTxPLmUTahgQ_usnVhCn_TwuTCNTuMystmjo1GgfYZziLe9lA6TzVuiDTBtp6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dw01GjsP_svTyZ7bwO0cYfSKq_AYji7K84an1Ln7CQfxIGa2dOt_nNiGyuXCIEEv62C7JR1aoMRx0Y3bEHhrm5dxqXGEXc-C73yfLqTpWn2YxXT8wZ-efzWycRgR3YTofiARyr7w-azkyw5t79nV8YDRLGk-WAuNIAzj5bmPak8ezjGwsqTyMVNMR4xRU9vn2r5Dd587LYHjf0-6UvbKPpWTuhisEsWg57aO0lRgleXK_g04F5exPjdGcjymcr--ef9q71nk898nfE4k4oAQ2Ejj8rf3Q94n1b8WlXXSM1ACodvWmfAC_KhybvfOT7T93GHnfN_U1w6iM8AoYR0Tfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saHYcLgUziRKRw5kme0952Ep6n5ZrtzToPHDRDWeJP8M_Xse6b1CyhjugG_v-rHSlSkjJjPDcxVgYsra3RthSwzJSnJN-Om6EyQjwtbRlUFIrCUopEaFk7Gmh3a9K3KTvMiy4mMVoFZ_T45O5ENKOq7u5_KR1lTcmqkQ-3ziBBBuph_zGbhQMYT1EGS2HVIPQrOqJYjvXnJ80RDuO8KPFnkhEmOp8XjMLpTPzXbt1hPebzZyAAYVMiMBH4ef16oRt5f7nRoLli5_wSJtk69adYkP5Blz94SmOclkSf5lsxznBpt7axr6qggcGqtr_eVDq-1jJQMf-x02aWiK0LSFlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9IH9_q2itHxlpVGaNelq4FnmENsgMZsRlPerjjaMS2VjTcrDxxUOKIj0prumjp72nX5k4e125yGwVNH8C9UBFzpRVpzvSMvBZMaiYtnIaU6xePgpxIfgQB2TLI6h7_EaOFmCh-IytqNwH3p36A6vhdBRrwbttbTCJmiy4tupbw2ZoJSRGzrigA43Wc8_cuyJmX0cskM8M2VWZDAJiELf2qUm7kEdRkVfhQUju2D_etvuUy2ygixL6GfCO3zZxzJguprG_i8EYY7JSbwZdP91DvrDreeXWy8P_xt0ltZAlWZcuBMAOwK2k5QxBa-BsW6hYR6K4l4l2fT4AGMpEQhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNfjFz_nkJoDsoBsBpT_-SHVbSotLlkCQgDZggCu1WLexuOaDtKdTYj69noASe_FYpbDTUY_tOIcMsOFQMzADQ1ydd97Nt5JU6rvVAcz-aLk5vbndmhOLTe4Bco-ovlFJeFMQHeRnlfbze4cJB9S5pzsnJXrR8D3XFMBXJ-sEw1Rq5YIJDZDJSzhoarsq6VI5yD4dgvNSyr1UST5pFeUa7CsJnF9Ts11CZBqC6WuCyVnP3nbQ85JlbgrTMFJiefGyyZ_kc3rRUbSgm8Zrk1gxmt7A4II64Y_j_WyL9cqAItTeSFjLBtRiOtVPIboCgu-ZTQmBWg6w0PbqXzZpAHQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkx5GofuFmocPEVrrGCUQ4kf69w9b-0FbbMWW1bKivejqAB9miLYPP-vxVyavlBfQhNGFKQDKkSMgv1-1F4xdbHV1GAq2pwueeHmG0Kt6BTjtWss47nDEg-ogOvtuhfi4Eu18azj7wGb9d7qdfjHcJalbl558JNV1Q8x3daStKPlmIthyuvgl4n99jDBGZzC_L-oLc94OxxjSDPSF3AEpY6Wm9agEwmA0jcT1SpQ13sYPAbZLJtsuACqC-qOjds7VQIzxOvHfD9yAC05N_Zaeeu-x--HtVoX6ek3dSWcKrUfDQZU1QAO321pRIl0Ok7xnaprXW4tyaE2BlsRPgvqeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibz7t1Rr2vM-5jXdkQVJgwZWrKHQ-UuVYlKhvs0yetNxCdI5JfMdOEekVPZjVXXRXfU80mhM2WyBypCGTrIdFOBbbKmDpU9anv9e5VW596Vf_lJFdxQPLBQalJxYd3w9ALdJ1MlS2XYdXjtVtSPCdarbBzkZ-ltJONRqimxWYz6m9ds1ofa-Qg5vNEcz1i0YNmqlR-uCm1DLDFKXdTrGW86cW2dCnWKSanNVbG34P0sfRdX3VZ_KsxKqYItQT9f2jtV2flS9LjyW9S5v62kYGV7zHUZzeGK0EelyG7Nn-DuAK8vLXiQuKX91GOnU4teHcMRYtnqZLMtFIoyhWcfVag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDfCM3M_ZW88_au-yiQN63dLMCFYe6wae9SwBbUACABfeQ80pjYbB-3bR4ZVYOsQvSkVm5WIzjKRwqP5fou45MLTC_1ojhAqCAOE-ZLnv2yGqmKVo6az0juKmqEQui6TX_q-Rkr2WX1LxohWsCjev-a2Qu0SZQs_Z4r2RRX3Ur640Pvzq1IWVC3KSB7GPjEhzWY5Uq5SAWSEzY1_1pjqQ5PjNSu1vduXaZ_WThHZ1lcIItIjgPOJvXvoM9zZlN6Dku0eVyJZbv7Z2G-S0y6dXwBVzBpjM6gi89iDGvPvbHsrSwr2pu104taw-2ZUojijAAQfyoYgh-Qxi1lR9aj-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=AFhjw5v_f_Jnasdd-E3c9ycyYVme6ROKQVqAag2nuxSgovJrWXifoyI0vACD7yoH__VwqmH_FItt38WivX1IWmpVyqyzDOMV2N3X0VcowedDkpnRRUC47aigXh85BT-I6fxJOJui-mp2v3Jjeaz7ZPP7D_QoSy26R0DEWpOAD-HQI7NRxkDMs4l1ynAby5sT53zy2vUz5fR97uqWls8yLGJ8Avng3mUKgGo_VD-b-HzYOBg60TrB_Fk6YVdStH2KjcUl7xsLVt6pUoijCv3N11edUzOlfyR0LSw0t3lqeNjCEY-CL8bvMuJ8byqNNRy6HsJs4lezA5pj3jN0rxSpVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=AFhjw5v_f_Jnasdd-E3c9ycyYVme6ROKQVqAag2nuxSgovJrWXifoyI0vACD7yoH__VwqmH_FItt38WivX1IWmpVyqyzDOMV2N3X0VcowedDkpnRRUC47aigXh85BT-I6fxJOJui-mp2v3Jjeaz7ZPP7D_QoSy26R0DEWpOAD-HQI7NRxkDMs4l1ynAby5sT53zy2vUz5fR97uqWls8yLGJ8Avng3mUKgGo_VD-b-HzYOBg60TrB_Fk6YVdStH2KjcUl7xsLVt6pUoijCv3N11edUzOlfyR0LSw0t3lqeNjCEY-CL8bvMuJ8byqNNRy6HsJs4lezA5pj3jN0rxSpVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sncp-WM9-YDRlwexaLZ1Mncsv7YpPMgWeY07dCmOzZN6Fhutmj34jAEv0O3-2ls0Szj21npIDYFUUZh1SKaBjkI5IWtE3EKokJ8-Zsx_eEdN2dKZS48QdbmhakfWdDdkisaN4vXDigAGnUbUw0lhnVs19xFL2PsvQGf-UqYqGsiRNkEQaTlVe3Wa1fqWOcsA57j9o7-pmbLGzPpXko3jSrw51TUacQMAuuc9KNeH9_zs591BeMp97kffs4W-4_KRFWPX6rfjZaw3iRh9ghvhW46X4Lm4AfY6qHyeX7xVus4l5Nb2WgP0nPuY4ZCzGugT5URwp1ffCy9hpTN4Ks7Yug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPFuQhUC0CpwWquEI7TbnQGgtNTyWrmRHl4r2D-Iq2zTZUizsuzg5fRLiXUZvqmGG0w-SvOSK1ZEqkncRI3-KfPecA81G-o0NiAffba247n_Q-EJRl88zxrtowX52jst-I1dx1pVRiruoS0-ufg5jIWS6deLThCUDzuTRJv3RI6_qVHKETtEtXavOjP524fBBDygzS7oVhwCy1lMTk9VuuiruscsD8M5YvXtgrGr0jAfiEqvRYi8RXsB-ju5U20xr0LawehyIgAY7Huxe6L4HFpqOcCGrGg_gLs7DWv8PNqdJrrgGTeaMrb7KhPyMNmEeSBS8QjsNXXdJhimC_egtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkJfl8bR7zHeLPuJFH9dYVc1dR0XeHtq4kdPVZz21eYtGqt-f5FYO9GmzAEja_INNDlN1930-1uQopAxIfPd5yHfhem74tszLXgm34Mz6SphFyDd9DYE-rkV3KEA_vKjYi7MaSsU1p-PhaIcJw5TJV273st35Gul6gB3ZtetuuHvZyHSaWaXKc253iiqQPrljPfeJIaJrdKrja2NxIdZn9kHDMHjuSClXBelySgiGRA6VVs5Y4SKx4SCaNtlX-lTnLGKRfn5bheDstRAl0Hzbvq9JywqIagxWerb-klRjG9X3ctYMi3f6RewtrBvMIJ-4qfzx0pGd8rip41YmFjtwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfYj9I1TBkhYsbIuqIc5-cAUYjAMxgDMmxu1rvHbEr-GsBiu6u9pgTz2LWYS9ucIZ2EXYGsPHIBT9svmmTFWBzBvRGUlzxZ4MgVT7mGGdagx21kKojt84Hdk_pXG_Xgld9CVkGLHYMDLaI_qVFowREvX8c0prBy2QmY0TCMImLGaq8YPTKUCntQeTZpBx2X-R21YUfZTOEbuG6dGHc-Er2mLYcNiBTbjWItHrIrCyZdpZzxYX4LSR5QtfmyhsjNiWJcbfOuHALIgZDB9dVb7I9dmg11vS9Wzs0Qx6vUmCk_PiQEb_OLnWja0eAPXMq7Utit9ktSJZtA-upULx-R26w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=FuVTK0E91eNWhMyCCsSQoqWYQJqlOQbVh0NVUKhf4EYiNrIQyV80Pc1ohcO-6olOLbypCI55saJMvePstYRo9g6eVezbqYr4XyUTqsDRXUkzCXk-rMdfXTnSm7EXSGisw-3V2DcoBDDj6y1UhVSzr7hMUbqopMymCglYwxMNe7NeYCHkLKPWjlSo8RX7XUjxYPGF8ByFR-lmkvs3aPhgD7ZNF_u3pWwTC-pCUA_8cWtu6oEa2jA-SEXD4AsXpOee3P-Pe3_1usmxQGRbX5GQEK3jEL7vOA9OmLGLugrel-yqVNGe-Vv5u4rBBcDDRWj6iXorxaBW1GeH65-s-7iGdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=FuVTK0E91eNWhMyCCsSQoqWYQJqlOQbVh0NVUKhf4EYiNrIQyV80Pc1ohcO-6olOLbypCI55saJMvePstYRo9g6eVezbqYr4XyUTqsDRXUkzCXk-rMdfXTnSm7EXSGisw-3V2DcoBDDj6y1UhVSzr7hMUbqopMymCglYwxMNe7NeYCHkLKPWjlSo8RX7XUjxYPGF8ByFR-lmkvs3aPhgD7ZNF_u3pWwTC-pCUA_8cWtu6oEa2jA-SEXD4AsXpOee3P-Pe3_1usmxQGRbX5GQEK3jEL7vOA9OmLGLugrel-yqVNGe-Vv5u4rBBcDDRWj6iXorxaBW1GeH65-s-7iGdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6vl6M5EjwMeJGebF8fTwgXDVbuwOiK4WFEDPjYX7QoyX2cELfJgStsGtlRTnSzItW4HSVM4nuJa3ZpD-_FM-LhaeyRpXxWZKKYk7F9Tha2IqIisXMUZ8gx7XJ4e1ecfE5GH_b6lmhccuJphFJgOEQFR2mTbzuPe-OIerJI8uD2VrvsQQLea5C8-25VcSUC4eeV0CB3IOcGOoEUloMgEmKikoVqdtR22FwOHHMcrpJ0e__t_aGxPuXcx-tGzLVHLzDkPQl6s22THWtP5J8t7xGWqJtiJlcXCJiSCqvdDfMpdNCy27qRfZjQy7PXteKKOs8MCHbnZ2EUJkMaI79gzqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📢
جدیدترین قابلیت‌های
ربات وگا
را معرفی می‌کنیم:
🔗
قابلیت AI Agnet در گروه
🔸️
ادمین باید از پنل استارت ربات در گروه به بخش تنظیمات برود و قابلیت را خاموش یا روشن کند
🔹️
با این قابلیت ربات طبق اتمسفر گپ صحبت میکند
🔮
قابلیت خودمونی بودن در گروه
🔸️
ادمین از پنل استارت ربات در گروه به بخش تنظیمات برود و قابلیت را خاموش یا روشن کند
🔹️
با این قابلیت ربات بی سانسور و صمیمی جواب می‌دهد
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
⚡️
Vega Bot
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
50GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 50 / 50
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZXEZiFXcTr-eV-8IFyYM-04rd9wXDyxAJ1dmq44gKEB0jI4Eh3rHB9Z4LyIYGCwBs12aGnPFf6BPm25TKFEJhA0Dl13Tu5iditiX0jPnRD92WaK_zNsdnOATbnVsqquI6krps1NwSq7FCXOTEGNRY_A2zuXuP_n1j7_wBDRvEhnv5mrjfA8NNlzb7ZQJR8mND_Clv0GsT-fy-3wh6Sfzb88NmcUMfXLYiMhq2dX1YVZTA9Ar3rTUZHjatn2Z4T6gnqi9dy6D-fijd5td45RqYUsGmRJBzql8GJloGNWiGzK48IaH8qxTUtuSNHVKGybuUoH75OQTfIpQVx0Yffs8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
تولید انیمیشن کوتاه از متن + عکس فقط با یک کلیک!
🎬
✨
✨
قابلیت‌ها:
•
🔹
حفظ ثبات شخصیت در تمام صحنه‌ها
•
⚡
پیوند صحنه‌های طولانی بدون قطع
•
🛠️
دوبله چندزبانه برای مخاطبان بین‌المللی
•
📦
رابط کاربری ساده و سریع
🔗
https://aianimation.video
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anLHeLeDpurvKmiMpyyPj_z0z7uXmdYBnzKrk91ZvL1b2b5gSfZEJ7wGDg_2M3iVmUpxVbXxfdGBqILyp-QfX3mwfOyjS9qPfsatZVnGha0FJJL0JYg8tiX4FW5vUCQWpz6IQs3cs0R9R_VFKDWMbI-umLgVwFMZhtungPat_CAcvNVOgugCiC7GHvhimzU9gJvF7hekAVAiCytOYSAGtTxQme_Acvd7y4EBLTLvSb9Pe127UldVgdnAIwAz0bI8cbwE_x2HZfJzezfsH3LmCG1FQNzQ8RvtaDn9vImfQgbwJa8D6WdTR8Xqiip8fqjlxLyeXIHud5CZZqMGTf0Hug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
تولید آهنگ فقط با توصیف متنی!
🎶
✨
✨
قابلیت‌ها:
•
🔹
نوشتن شعر، ملودی و تنظیم خودکار
•
⚡
ساخت موسیقی پس‌زمینه بدون حق کپی‌رایت
•
📦
خروجی با کیفیت حرفه‌ای
🔗
https://memotune.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSVViLggRXcOyBOu2kbur7vgoliD_Zth_QIWjELnM9Ono49dbh063gkyluiev_iDWLU0VDoIPh9BhG7kybMVfOEIjqMeeivIUVtiqSWSJPXDkv1B5V2fd_I4pwKQQLfIwvOStIvQf9nbjcRm5HDOBhNbywVQAIKX9oSWfbjoYzsFjVsffqFyqiSSwF3mroSIZ2X7O93-UlDsWDmRXg2BHD_TaIDdja9OqqAzktV46TE-R8Bv9-3akvpbSVLcs9uycIynkbCIa-C4tiognuO3lZuPo9KBWLLyfZVIRCHjXRzBbq4YCivcxghUN8wDF65C03C3s1y2OThFNIKekD5URg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ویرایش تصویر آنلاین با هوش مصنوعی، بدون واترمارک و بدون نیاز به دانش طراحی!
🎨
🖼️
✨
قابلیت‌ها:
•
🔹
انتقال سبک و رنگ‌آمیزی عکس‌های قدیمی
•
⚡
برش تصویر و حذف پس‌زمینه با یک کلیک
•
🛠️
افزایش کیفیت و ویرایش دسته‌ای سریع
•
📦
خروجی با کیفیت بالا در مرورگر
🔗
https://stylizeimage.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=OHVNUlNuFmIEK8PAbba6qgzEXkndMwXEWVi8Hugiq8w7e49_V2Bj7GiwC8nZH-8_FpKVo6j93Ugj5V6kKb40U6d6HGj3syUlrKNFsaM09-SfRHPSQEgJvKFXAWaTIxrKrnQiko-vP9Cn70k9gjiPAZYYofKd7cJLExu_lZUxwbz5SfNoiGzHkN0g0Z3ijmz9qrWI43ognDXrowgv9hHh2ZsiWbcsAkoWhfOxw9Enp_XjR7CElv4y1rpcYn6zBXG8RUB7UKsUoEJv6XAyibxgMmwYrOqfadRiFiGYeXoDPhEMr1aYH9m991N2DvGAWgGZ7gKDIPJhvA0Aq8ikAc7AXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=OHVNUlNuFmIEK8PAbba6qgzEXkndMwXEWVi8Hugiq8w7e49_V2Bj7GiwC8nZH-8_FpKVo6j93Ugj5V6kKb40U6d6HGj3syUlrKNFsaM09-SfRHPSQEgJvKFXAWaTIxrKrnQiko-vP9Cn70k9gjiPAZYYofKd7cJLExu_lZUxwbz5SfNoiGzHkN0g0Z3ijmz9qrWI43ognDXrowgv9hHh2ZsiWbcsAkoWhfOxw9Enp_XjR7CElv4y1rpcYn6zBXG8RUB7UKsUoEJv6XAyibxgMmwYrOqfadRiFiGYeXoDPhEMr1aYH9m991N2DvGAWgGZ7gKDIPJhvA0Aq8ikAc7AXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
افزونه GlifAI، سبک هر تصویر را با یک کلیک کپی می‌کند!
🎨
🖱️
✨
قابلیت‌ها:
•
🔹
کلیک راست → “Glif it” → دریافت نسخه‌ای با سبک مشابه
•
⚡
بازتولید هوش مصنوعی سبک نقاشی، عکس یا صحنه فیلم
•
🛠️
حفظ جزئیات قابل تشخیص در خروجی
•
📦
کاملاً رایگان
🔗
https://chrome.google.com/webstore/detail/glif-style-hunter/abfbooehhdjcgmbmcpkcebcmpfnlingo
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HosIx2R5jzrv7JgXuM94chPspKeJraz1JCAjD_m3mCpBLgWlvGohY4FfN6gNtsXDdgTqMRJEvP52FUBW-mlODqMO1BX22cDqbwnPNt8PfAUeMbJd2fe1a4WRiKtJWtyrGcvxDzYWfeZEohvHuKjptrA_MlZpw_bLUyl6jCuJzkImZiecWwA9sjZuZJwONEQuPAx9DcerRxcyihGuZQX2mXNvV3hW0V3f9E9xmqBG3CRgGgQbD2GqlnupxAL1txjSdcVHIwM8Ei8ofpVW3mmye8DxKP87auZCiNMTGZsdQSXIB-4553n5_lrwqhmH2A0oi7GjZwUzyIHXMCoAwa5DJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNNV2XjCLoHVmTlwOhvWoIeIuj5YFddBmCSiYpfMPjJVSTor47kbftZOR3DwAxdRFbikC2WcEIoVGBUikf0DF6ctuSDD3nS2lzaEMDjH7qrjFcKMExDiMcXGTHW4OddelUWNceGrfgAxvtaQdKFwkKAeQWKbNzTLV3UDLf9D_VgHQoREhyYcBdUTAlp4WCSzLFPk4uo6-FT7ayPtWODlqWXpLbN1BZnM1H87QmSG3YAlRn7TC_btoVFe4zpIemOj38j__e4ckYnB6MdQaCQGze5ausl3-qWA60z4weP51Iwq8E3WryAoHbNdpePFmWAM9Ca7KkeTrdLxGpikZ3Pavg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_-96jrsVM8ZZpVrps0OZYWx5QnlX7H7Z4RIUfVE-e4_G-pw36wbxEOuPJJ_3STKJOjznF-u4GmX52gkYwNRYcDezW_wOvWjKS5UFrQzdf3aSFHxvqzJDB_dXd_FnkxT9or7mKmrFM-aUHQwnSQ8J4tfbP0A27RrfNp1QEd-UEqhBbkSessVFt6pbefKLc0ruKcoe2aMX1nR0Jjv77HhTFRLxBoNUjcTuvllnl9QStDtCcdUEkN-Y9QbP4DfuuET1rw21GWymZKdpAmXaQjkiEXMaJanOiBZOyeKykcfbJDHTa6ou6pSJxcT1D0DwzeAGXRNFkbwbOcAmjYGtcezwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد
شرکت Anthropic به‌تازگی مدل جدید
Claude Fable 5
را معرفی کرده؛ اولین مدل عمومی از کلاس جدید
Mythos
که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:
• عملکرد بسیار قوی در برنامه‌نویسی، تحلیل، تحقیق و اتوماسیون
• توانایی مدیریت پروژه‌های چندمرحله‌ای و بلندمدت
• پشتیبانی از وظایف پیچیده مهندسی نرم‌افزار و مهاجرت کدهای بزرگ
• استفاده از مکانیزم‌های ایمنی ویژه برای حوزه‌های حساس مانند امنیت سایبری و زیست‌شناسی
📌
طبق اعلام Anthropic، مدل Fable 5 تا 22 ژوئن در برخی پلن‌های اشتراکی در دسترس است و پس از آن استفاده از آن نیازمند اعتبار مصرفی خواهد بود.
این مدل به‌عنوان قدرتمندترین مدل عمومی Anthropic معرفی شده و تمرکز ویژه‌ای روی وظایف طولانی، استدلال پیشرفته و توسعه نرم‌افزار دارد.
با لینک زیر ۵ دلار اعتبار
🎁
نیاز به شماره مجازی
⚠️
(ایران رو چک نکردم ببینم داره یا نه
😂
)
🔗
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️
#Anthropic
#ClaudeFable5
#AI
#ArtificialIntelligence
#ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها رو یک جا در اختیار کاربر میده و دیگه لازم نیست درگیر دردسرهای مختلف بشید
🛠️
✨
✅
این بات به شبکه‌های ورزشی محدود نمیشه و حدود ۶۰ هزار شبکه فیلم،سریال،اخبار  و.. را نیز پشتیبانی می‌کنه
آیدی بات:
@Bear_Tvbot
🐻
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIAyFU43WueOgKTYGGt5rD05xTZY_eeWmwvqh_cZWHg-vhnZtnTrVR4yH4DeBII8VpHlYcD6toO2-mw4iYGOVWW20atckCzSaBG7Y68_-cqakTHqPVXNCarVd2QKogDyvmrRNmk5uAUZKlTQkHFOE2aFDfJZzOgQawZXUgsnm3EaEmnRdNrh7z2evRWv9Z35_0T-7TwOiwyDQiy90_RQLBB3HHAX52j454DqKxByYSnfRjwIVMxfk3JwojaXc7rmhpIes1YrZG5qaQ06kSBKeqckciEIIdRefMxf5XJACPToGKrqqNhhtVHxR0SyaTJkD0TfR8f4SHK83b-0KE1oYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مدل‌های پیشرفته‌ AI به‌صورت رایگان در Notion!
•
🔹
Claude Opus 4.8
•
⚡
Gemini 3.1 Pro
•
🛠️
GPT‑5.5
•
📦
DeepSeek V4
🔗
لینک:
https://app.notion.com/
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ddsLGM7ivTbW03TyIofG9uBnSYDlGf4LR0yWGCzV34ZGde0L_WoaujyOa4xNQmFcLEWdoatz7_SSbfXsqC-Zxz20RLIHLeotO3zBO-w6u8xdVlXonJLte1eNYzqK_RMEyYwqoIkfRV6HLVe8bzy1ApnSOG94rqH7SW6HOql_3HCvOyb0L7Q67mAE_ZdQ6NYoDInuWncbr-IuIZB5_hJirrTsLufxiCqEdy1ZNLUUwiu-bOfrgKe88DpdvgN6u4-PN4apFSgZHuIniSTB7ICutwIA3RQ3mEDWb03tdg5oY0jS3_6WjaRMq9gv63gcRycikN3kUx4S4ZRCqp1NA5Aa5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWPMGXAf-GydepCKA7wsAxynWsWKNo5enmthdSM1u0F1ywu_O0gNqV7vBPbIRtqoP1ZqS8hJUeMq_JiW26uSMte9JVYjesCHfi2DBAW7H9ytbINM_xg3bEczJk3r_8pKJNlNUxKyObhVjTs4Zi8f0eqx-DYyCiB26YMQUWX8Gu69wgtjvXA4emidWN8yQM0AGMQDlg1VDcL402im-2yH-hfsRb7diMc8GXI-lyTEFnaPOEeBLJZ1v31Abuehbc6aWgq6Ejbq7nn1I3FnGlGw6Ihs5nyOmDJ85cfv5xeuxobhm9dnZe84FUYcM53_X88s3Hi-S_c7CozDY-vKUFlKTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=k44POKY3HrDZHBo9_45sbIr0TKjR-YEkKwCyPWxvg8Sq3YIlrpnPBielQu6wdxnZ9t07PIU09ZTDYdsK8zdtSoXwgGKmbOtuL3R6GFfSM0waT-_Na_kHg1MQhKxE4NGXn-r8S_uDZVVdu1qHz9XZXRkODW2W2wyxOgmKhpBkAawTafb806gjDw-pUlNQ3j_cfvLZz8ydfZ9fWYPuaGd-WjMpVA61p4EzRjg0ObwzUrPzC3uxE514bx7crHZcBuUEWHwJ_LFUgsFtfUZgd2ZrNrWR22C6wOmz52UrL8k-lpnk2fyk60s6jBQ-HGiVSlbgEPUpBxWjLWwMhzR-tXnhXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=k44POKY3HrDZHBo9_45sbIr0TKjR-YEkKwCyPWxvg8Sq3YIlrpnPBielQu6wdxnZ9t07PIU09ZTDYdsK8zdtSoXwgGKmbOtuL3R6GFfSM0waT-_Na_kHg1MQhKxE4NGXn-r8S_uDZVVdu1qHz9XZXRkODW2W2wyxOgmKhpBkAawTafb806gjDw-pUlNQ3j_cfvLZz8ydfZ9fWYPuaGd-WjMpVA61p4EzRjg0ObwzUrPzC3uxE514bx7crHZcBuUEWHwJ_LFUgsFtfUZgd2ZrNrWR22C6wOmz52UrL8k-lpnk2fyk60s6jBQ-HGiVSlbgEPUpBxWjLWwMhzR-tXnhXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تلگرام به‌روزرسانی شد: پشتیبانی کامل از Markdown و امکانات جدید
✨
قابلیت‌ها:
•
📱
دسترسی در تمام ساعت‌های اندرویدی
•
📝
قالب‌بندی نامحدود برای ربات‌ها (حداکثر ۳۲۷۶۸ کاراکتر)
•
🤖
ربات‌های هوش مصنوعی می‌توانند درخواست‌های عضویت در گروه‌ها را پردازش کنند
•
📊
امکان افزودن لینک به گزینه‌های نظرسنجی
•
🌐
باز کردن سریع لینک‌ها در مرورگر پیش‌فرض
#Telegram
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jb01EhNn2ReTL1Vzsav3qCKcuScP1Via9DBcKg_eS2ZyS4aCmyVp2X-oOujEMk4Knwydsc2zndfa2a4dgmlxLQtdygHtO9qbkLqWNMWhUv3KNLzd0krR20MMAmFkKxNYOl4Z7zt1ZHUItPEMZf-UCZqe9JQPw43iE10tQvNdBYluzglHfs43weW4SMXzjn07RNPDnFl88WYDx5Si5nDUk2-k66_2QlraVsVnw-mMy2d4nsh43XpkrBvAKNEYmyV5tqY0S0uq8e3qbbTYpMBFXmI44RZVk0VQ1JqXlLtfNqQktnw03Qtb5vOXDVxiX2Bn7LGSj4CY0VzAYPzuVqsD2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
MemeDepot
کتابخانه‌ای بزرگ از میم‌ها و گیف‌ها برای استفاده در شبکه‌های اجتماعی
✨
قابلیت‌ها:
•
🔹
جستجوی پیشرفته بر پایه دسته‌بندی و محبوبیت
•
⚡
فید و برچسب‌های خودکار برای میم‌های روز
•
🛠️
دانلود بدون واترمارک و ثبت‌نام
•
📦
به‌روزرسانی مداوم محتوا
🔗
لینک:
https://memedepot.com/
#Meme
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔥
دامنه رایگان 1 ساله!
اگه دنبال یه دامنه رایگان هستی، از سایت زیر می‌تونی کاملاً رایگان برای 1 سال دامنه بگیری:
https://domain.stackryze.com/
✅
قابل اضافه کردن به Cloudflare
✅
امکان ست کردن نیم‌سرور دلخواه
✅
مناسب سایت، پنل و انواع پروژه‌ها
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrT11M0rkTnanvb2Z2qa2By1ubWgcI2VpImpYGytEg_M2nA6BffVwffXevq7tIssk92FJ8YO3siiSF8jz-JGTM1QJd0PHNxo9FtqSoDPtDaNxypTXl1C6lIlKTcuWbN_GkX-XtmKjqQwcMYhqyulBH6CfKok20h97T_btIzEMVfgwYasqsXMt2lEdRmzCB4WHRaiLs93gB04KxMEX8JoCTJb3Rh39-tlQXovhFUwMQaOnm-ID3lcqbKRnsOUEyO5Kkq82Arm4JZvENvuC_rtv0LpHIhBw14rRQ37BwcCugtcsWZqQMmG0baSzXv2U9F0MamfYoMmcbr6Ce7YgynTPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵️‍♂️
CloakBrowser | مرورگر ضد شناسایی برای اتوماسیون
مرورگر
CloakBrowser
یک مرورگر مبتنی بر Chromium است که برای کاهش شناسایی ابزارهای اتوماسیون طراحی شده و تلاش می‌کند وب‌سایت‌ها آن را مانند یک کاربر عادی تشخیص دهند.
✨
ویژگی‌ها:
• مبتنی بر Chromium با تغییرات در سطح کد منبع
• سازگار با Playwright و Puppeteer
• قابلیت اجرا روی سیستم محلی، Docker و سرور
• مناسب برای تست، اسکرپینگ و اتوماسیون وب
• کاهش احتمال شناسایی توسط سیستم‌های ضدربات
⚠️
توجه:
هیچ ابزاری تضمین نمی‌کند که همیشه از تمام مکانیزم‌های ضدبات عبور کند. استفاده از چنین پروژه‌هایی باید مطابق قوانین، شرایط استفاده سرویس‌ها و ملاحظات اخلاقی انجام شود.
🔗
GitHub: CloakBrowser
#OpenSource
#Chromium
#Playwright
#Puppeteer
#Automation
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vq4BYGr9Bf_n_skJ95Bc6a6E56WrxTQciqug42Jmhcl-eRX0TtcKvqPPd3wXR_cNF5hkvJCxm8v-YrnEDI1z__p0dILKth2B6u-sXifl4Fr2wSPlzP8wO_cXsn8j-94ymIxtHAzrKiP3GayY_MyGJK2zS80tJjtZEwbaWESf9iohbhGdmei6Wg341W8Xv2LqdGNzgrsJwZMLTNxJraWtl5pL7Ed_JeU6IVfDsJhqFGkdNLutp8B6EhzGEAwNzGfA6O7z5c_rceDDXCfhHKTjV48uIizALUzrM0Jh0_zXqf5yHQVh1XdVJ8RFLq1smYYEEJ7GL69A89qrcTgDrnoRmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpdndKoAyCixD_wbF5v6xtH9VXqtuGfsMcIqPllIzXMyM4Adrh0tGYrGKpk8imWXoxzmfbqsVGoOZ-vZxR8P9pyP9oTKAePWUOC9aKRtXzh3COWkAo-xHvUSRV4wUq_VIwjkaHr5vybe6fv8xaC-6HR5xcdQRZ5SBpwURPN53-LFcOqwfpBPUbXaBxsxWN-WVOrLTjiAUSadPR2l3HoA-0TfGobWNT78LX5q6WHrWxmY3zZduxId1bCKIfU3IngQnh3ZTgiHE1Jbt9BhIFET33Yjd3biA2vE4wnaLaQe4zWV1zfgHvxj78-xyLbvPGqn4_tRzhAgNDiCRp8MMzkNyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=g5p0K0WgO5LSUvfLPLIUPKPhTNGXtOsXz8jL-rTBtek_af7h1V2b9hTR2WCp1qVursi2zzTiM1kScHW_RldNObciibLd3QTeU8GMsM-L4_5LzmvuODQ5JYeq4O6NpeOiaVVNKekIQoaEw7SlIjbE7Dpm1G05lMeW3T1uW-ADQ1HvE3S5Wfz1f5nXMBIUe9ddzCxEY-Bc0cgcwu7dKidP5QLzTZewqiBc3wSY2ku0OXcAgJ4eleQGNRvgSeLVRoYgHK-JtSoIrimYzg51kdBdY5XXnvpTOuD6moLInn-kv5ofe303jjXK-NHykbGcSxPFNIw0bL3LAiGgwuAW46WW8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=g5p0K0WgO5LSUvfLPLIUPKPhTNGXtOsXz8jL-rTBtek_af7h1V2b9hTR2WCp1qVursi2zzTiM1kScHW_RldNObciibLd3QTeU8GMsM-L4_5LzmvuODQ5JYeq4O6NpeOiaVVNKekIQoaEw7SlIjbE7Dpm1G05lMeW3T1uW-ADQ1HvE3S5Wfz1f5nXMBIUe9ddzCxEY-Bc0cgcwu7dKidP5QLzTZewqiBc3wSY2ku0OXcAgJ4eleQGNRvgSeLVRoYgHK-JtSoIrimYzg51kdBdY5XXnvpTOuD6moLInn-kv5ofe303jjXK-NHykbGcSxPFNIw0bL3LAiGgwuAW46WW8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی ۱۹۷۸ ایران، فقط یک تیم فوتبال نبود؛ نماد غرور، اتحاد و جسارت یک ملت بود نسلی که برای اولین‌بار نام ایران را در جام جهانی طنین‌انداز کرد و نشان داد که می‌توان در برابر بزرگان ایستاد.
از ملبورن تا آرژانتین، از صعود تاریخی تا تساوی مقابل اسکاتلند، این تیم برای همیشه در قلب تاریخ فوتبال ایران جاودانه شد
❤️
یادگاری از دورانی که فوتبال، فراتر از بازی بود، یک رؤیای ملی
✨
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6297" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6sFVvtz6awRj0qC8dA2VJCixPFCbja6PwmtwbJTnJQksubI7s-dpIpqfcfzggq0BsU2hirjLFQg1wGkf9CZoxmpb-VEVsjfrAKlMMBa8tFMdXXv3i_R98-aHalQYHlTy2oKc0JXXRk-z2LsGrzSYYCZJcFnVb1KJd06i6Rv-Hyw48CuEe52pqdfUpvTMy0z-cJgjvFijK9hVCijyxLYiOS0hc9katL0CFbsbRZGMiNPUJf721qS_98tXZSEDMrMeOdCfe7OSYI6fxZc5zs7yqXBZCAY_QFCdBqfmOljuBpV3FkrHGJcYmbfJ1kLNqJ6jI3EKeeqKpYL-UTwVwSgdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hwcd2Bm9fetDjT9FrGtOnsEgb7CFshCnZTCLUNOF7b5SwMSQpvT_VQD3faS8bkCEtJzg5vf3J-_GsW7HqwQxieTvkGNy2xFZzhmBtif5EWBKGMfIy3_V7R6OEzRUNkPowWNrihRFWcRIfmLBK2cGwktEpsprKccch6TY-3XD6UPVRo_8hbp3RD1gdgOu4sIepJOQ7GsMhwFvQjfRdXy2qms6lF9jFOGPaZWVjE3gpUmHJTRMk1DDI7kVkxDkE7R3OanJ8t_tAP3hm-CaN1qCrLvn87RACR6JwNVfyzZAh6BomuPyota3HT9HBFtzD-yNhl0_w_6TXUOTZPxYWHmL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMMNLOIV2dDH6Pe-o38_gU8C2f-7cqsaWty7N6r1E8hcc6Xc0jgd2LFEMWXKoTWx_MAubK0uVoHoecNLnYT21EhKlFdE3TwbhT7R3w0gttbdgqQn57kK6h2HCJkg-K8y5mAucHzeI0R8a3kNGBaO43NmmLO2wHz9S0WOE_Gq7jhrs256wP8ghMDWNVKGlWZFeH-rF35wb48-n2QbZmvMLlRV4_ZLGEWn9dNGoVfKJKx0HYV-o9iM853uTsnj6_-NlMMRJmuNppth3rzVPLPifQwQlvJoGI7wTuxfeZWR3ShoEfbXs7P-Auc-kY1GZUObsi3J0KTtwKNWlVucJC4wdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcNwiTUZfBOwE97DkPifNme5e8Yby00eyCUhleIfV8fFHZjXouJv-KGpKzRctesAVfy3p4OgwZN1p6ibDYXPR0hz4ZZ7yEp3HiWuhZ4PD_ZjVLrB2A-nGEFXBbWScfxe42h45xvWnqEOj5Bn4tm-tuf2GkXR0o3TZlYQw-5Gz6grM6Wx8Sr_PYeAy-pB-FLkgUI1o-2h9ohjLQKmsd9OXVIxFKaRIrKpLgbXlEHzHukG5abIS5uuGB3DxQ4H9CNXlgA4a0sWVGefD-SxihANHwwCvJr_bAV-8fo8_schtJYxOtuEzfij1GcFQnq7RzI-Nc3npTbwvDnfe5lzS4FfiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=mFY8bEmrIlUJ5tIZLO_Ll1bA4S8CQBxHe1nVXr34Z-V9V9K2n-JNwCggiZtRfT-OmnS7n55Gr1sPTQjtw8CoHHXAjnlwXQ5ndsmszn4jH9WSUxYe9yZDzNp1UFuhLLfGzIjDjK_bFVGcQ4uPwmxGQqB-M0y1OaEfbs9cU52hNP9MiIanoZLiTorbj7qHQztjAGm0j3LVtcf-v2wd3eOdXBhdqYgtWswUz-ekN2nzmviu2thAqa-VcUH9oWaTdeJPklX7kbSuyjxuhzlTIkaYeq5BnckgYkx20EKL4LDDUjEjIHbGzNzUKuxo8e-at46vWmPZfqjDwwBG79I13eejTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=mFY8bEmrIlUJ5tIZLO_Ll1bA4S8CQBxHe1nVXr34Z-V9V9K2n-JNwCggiZtRfT-OmnS7n55Gr1sPTQjtw8CoHHXAjnlwXQ5ndsmszn4jH9WSUxYe9yZDzNp1UFuhLLfGzIjDjK_bFVGcQ4uPwmxGQqB-M0y1OaEfbs9cU52hNP9MiIanoZLiTorbj7qHQztjAGm0j3LVtcf-v2wd3eOdXBhdqYgtWswUz-ekN2nzmviu2thAqa-VcUH9oWaTdeJPklX7kbSuyjxuhzlTIkaYeq5BnckgYkx20EKL4LDDUjEjIHbGzNzUKuxo8e-at46vWmPZfqjDwwBG79I13eejTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=vJ0vim1EnLm9jxCC36sqLIWINA0q6ISZcRecsjjApgNfy7ip4_9A4f5cnr06cW7LxSZj1Q5KRun99su5QK9Bb7HJguNNtFVsziP0QSqqYVEbL06r3GtnYRT8QswXYv0qrvW9d9Ke9InW9y9oo79DOvU2Bru1agLIAkFuqdg8ubEvS5XbcXK0Ug5O3YM1D4FwYKarGnnjGMY8f7fSnbN-t-MmA8_3kHdby60V0QDqojWMf5wTbOaYY-468HD8bTvBHtd_gzEF3gYpnLyMyCTXN_8W5GNIKgN1kbP0VVZr2BhP3ZonfkS9Ur1bRmNB20bLa4lSffrBD0mCF2yuT5EMOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=vJ0vim1EnLm9jxCC36sqLIWINA0q6ISZcRecsjjApgNfy7ip4_9A4f5cnr06cW7LxSZj1Q5KRun99su5QK9Bb7HJguNNtFVsziP0QSqqYVEbL06r3GtnYRT8QswXYv0qrvW9d9Ke9InW9y9oo79DOvU2Bru1agLIAkFuqdg8ubEvS5XbcXK0Ug5O3YM1D4FwYKarGnnjGMY8f7fSnbN-t-MmA8_3kHdby60V0QDqojWMf5wTbOaYY-468HD8bTvBHtd_gzEF3gYpnLyMyCTXN_8W5GNIKgN1kbP0VVZr2BhP3ZonfkS9Ur1bRmNB20bLa4lSffrBD0mCF2yuT5EMOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo01_yDuW7AhLlRnswkZsPZlguirAnrnTXaoMUWcZgjSe9-3GxJhrsOfRE7Z1CHVR-xu83euPI80UnAX2ic7ItBNBHdi5dDgqwaW8LDlvkTjpSqDgedU4z1iU8Po8q70OcoUd4_tcO8aAjuEyLrDFrIcRG2o4hyoGBRZIeba7Oa_FDfm-dKUush9hfYlg6aW7DDh-MtLlE-uCja66xgGhjt1ng249b4WWZ44SRJjOBdMIQSjsiECfHN3kLdkvUzBnBcaAKFUye2hjNgrZJNGd1FPuzNxahkRKM3e-7fAFb8lyemchv-iO1T-t7rhGdXLPlfCGjKwdMW2H8O4vfWAKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=QvvFM79-OZQXXWm5rNTh_ckGyaR9V2c6vcwUfGoLYLGcUGHuDf0_P_DB8WKoC8XcIVvHFj2i8UttDy3Tvw9SX2mtwPU1SD1iXKO_ZE6aqDJ9u_jBLfcWF0fY0pCgvk9fHlSkCqn8Vp9vG2F82UZPx7i1ycTv2gAbBG3hnzbq2jsrbkoQEEhPWXY4Bvd0YlRe9BYZRI4pVm68vCr0g9vfVexYlU8XX8UpOhmG8Jw1LzN1EX7XoFQetNIMFA7lS-NHdt1yZ4kMxBkNRCkVwMTRoSKM9DICW_6acULHyIP2P3QJAjq_SrWBmsKcGmhjOywR3vcp9dg12mirwPnOAZlxYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=QvvFM79-OZQXXWm5rNTh_ckGyaR9V2c6vcwUfGoLYLGcUGHuDf0_P_DB8WKoC8XcIVvHFj2i8UttDy3Tvw9SX2mtwPU1SD1iXKO_ZE6aqDJ9u_jBLfcWF0fY0pCgvk9fHlSkCqn8Vp9vG2F82UZPx7i1ycTv2gAbBG3hnzbq2jsrbkoQEEhPWXY4Bvd0YlRe9BYZRI4pVm68vCr0g9vfVexYlU8XX8UpOhmG8Jw1LzN1EX7XoFQetNIMFA7lS-NHdt1yZ4kMxBkNRCkVwMTRoSKM9DICW_6acULHyIP2P3QJAjq_SrWBmsKcGmhjOywR3vcp9dg12mirwPnOAZlxYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR82hYcAUMqVl4_TJ1NXgpJg-orIE7uUuWnU24VnpbZNteLYBCfYCochX9ocTMK0AAf5Qr9HkK44t-gxJ_mqdApw10uMNo3H3Fr2qcjGJE4AISLwRs_SvSe-UeK6GcjPBoXuZn7TKHgPY8A3_fu5ZhttB5kooy6aSgVKpi_tUY5AgZ_ZKkaFbO1KOEHxDFUNDp2tfO5AmZ-vXYg9Ho7EYh7Hfg7Un60Z3aTlH0p6fCkEsI_NkHCeg9LnYe07uI12hEdHjaEH--vn5hbJDclXPXSn2SqRFwYsJyijREYmBIfyNkLWs0MGvKgE9z9O5UsrmfzkNjOiWmOpW-L3lGm_xA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzCq5jmBQRIIM1mx_-fE_8pbViOUVMDeVbFk7EPX_OfVFFDY-A-1qb6RE-BWc7L0jYUcLU_xtIT4pECi_ya2AgI1ZW63i9-tCg6B0DSTpuMNTDBxoiDtWou8AaZf3T2-rUR5lQWmS7ttmHxByJfCuBrt0ysm0mr0vBJeRXYMmpZcsz8j70FbZn5iJ2lTqgbkE-zuHXoQssZFFj9y2uvVsfGjcl5AFqwzWW2-AsHd1y3dXoxFnjEwMKoClkgIBV68YSb9Us22B_V1szJn2nIkSt326G673g1zXpdXflCxEM3dBmugCu_BzmHYw18goiUAmaCKkqN4TXpwAvOCH7YlkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=M1uhkiNY66tyBTj5kygUvDaP5aB1CwrIT41-AheIuO2jUV8Ok5819OP-AdvNKaJO9KyFAbom7CgRqFp5NZSM-5qbrH5cbW79LCDlAT4KS9qXp9BHpDyy7_O1o5dwyZJPGNBxoDxJ-nrN-34G0jS4jxaVqe6yCFqkhx1M566LrCzyAKfZaXBnFzIkr-kcbL0zCtqIi3WumrxNvQjezT59lpANG1jeiZxabLiS40RkOwwsASzGzxMHYKlEK0yu6650eVAzWYf-BeYUGc5DkyCHEp1OZFvSl_KtFvKM2XKHKNBoQOTHd-Y2EPypt1YVpAoQKoMZzXsfPILKPiuK26_tBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=M1uhkiNY66tyBTj5kygUvDaP5aB1CwrIT41-AheIuO2jUV8Ok5819OP-AdvNKaJO9KyFAbom7CgRqFp5NZSM-5qbrH5cbW79LCDlAT4KS9qXp9BHpDyy7_O1o5dwyZJPGNBxoDxJ-nrN-34G0jS4jxaVqe6yCFqkhx1M566LrCzyAKfZaXBnFzIkr-kcbL0zCtqIi3WumrxNvQjezT59lpANG1jeiZxabLiS40RkOwwsASzGzxMHYKlEK0yu6650eVAzWYf-BeYUGc5DkyCHEp1OZFvSl_KtFvKM2XKHKNBoQOTHd-Y2EPypt1YVpAoQKoMZzXsfPILKPiuK26_tBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=PIryWmUcywVOWeFO14eH0tQ7ahWAS5qCAzzz2jbaU6_fa1qB8ZLhBNNymTPLNH6QJCCkikwIivywoY58dBKM8kndZMDi0VV9c2RjhZQGkLiygY3ZA52LC2wM9L3jjyJCUNDOTXlYzpZtTDB27sLuDxiB9VUQ972smtfSNlb3pseHPiQky8dhFwg-aVySu4Cs0jwkCi8RQEQ6aQ9PgHNtGgs15UI_krLDLnYgNEnvsuTx7GQnVrq_b1_ktCQT7PeW-HDmYKAdSoOOM2Wky6fXma1i8qeeuLHnHklfzIBX-Aph_FfvO9TCMEQ9j6DwXvvxUhDefBarmU8oCRAtyJgM-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=PIryWmUcywVOWeFO14eH0tQ7ahWAS5qCAzzz2jbaU6_fa1qB8ZLhBNNymTPLNH6QJCCkikwIivywoY58dBKM8kndZMDi0VV9c2RjhZQGkLiygY3ZA52LC2wM9L3jjyJCUNDOTXlYzpZtTDB27sLuDxiB9VUQ972smtfSNlb3pseHPiQky8dhFwg-aVySu4Cs0jwkCi8RQEQ6aQ9PgHNtGgs15UI_krLDLnYgNEnvsuTx7GQnVrq_b1_ktCQT7PeW-HDmYKAdSoOOM2Wky6fXma1i8qeeuLHnHklfzIBX-Aph_FfvO9TCMEQ9j6DwXvvxUhDefBarmU8oCRAtyJgM-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=o8tOO6XTP3yYD0xtDhYy5b20H6y-H9FKFJAbq57DdMQ_dzp7hjxDUbwgyuXxwKFm87vai0TVy7jAGq0E_G52fqxkNzQP3Ub7rlHtUxaHO3FKPiRnYlh8n-aXseWISarr3Dnzunl8wgIDm1EOmYNyM84a9K9BFk1qri9KpzFD1NKFWavTFf7yoB15SEoBdnr263cGyNPkGskHsaaxtQmsbOdBy246YiBI8_W1OG8o0iIzOcjGj7s2OIXCLVMUMGlJGcYKxY5ANMNVKDmnGUZUvt9CqWausipPGW0AJac7oJoIvfuMB54aeRKQEEJ1sAglKAchtGtUwe0b6FUSde4SNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=o8tOO6XTP3yYD0xtDhYy5b20H6y-H9FKFJAbq57DdMQ_dzp7hjxDUbwgyuXxwKFm87vai0TVy7jAGq0E_G52fqxkNzQP3Ub7rlHtUxaHO3FKPiRnYlh8n-aXseWISarr3Dnzunl8wgIDm1EOmYNyM84a9K9BFk1qri9KpzFD1NKFWavTFf7yoB15SEoBdnr263cGyNPkGskHsaaxtQmsbOdBy246YiBI8_W1OG8o0iIzOcjGj7s2OIXCLVMUMGlJGcYKxY5ANMNVKDmnGUZUvt9CqWausipPGW0AJac7oJoIvfuMB54aeRKQEEJ1sAglKAchtGtUwe0b6FUSde4SNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6267" target="_blank">📅 21:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzthoKSYQh5cNW_07qm-a9D-MMmd8rsARf7bGqPb61XlrPNf8HL-FemQpZM7uMWzvqK_DDWP62z2m_PS90YWv19KCnLQgCRehCyXfKB68YPSs-tO7qFHIvYFK6rtpSu8fXCPIG0Y-n4e3QcvefW27NqlUjo4lMOaM31QnowNpfVjCR6TXYLOK51pSWnXpyV9gVhPMvls7JjMSf4wlhAPGOOtr7oZM0pWffXWGb5bI-yX5mSqH1vgwfvyEf_xBzb2PCdWxd3K3cvHCfuWu6nwMCoK2VDSlnlN8tgmkinNcaJkEulVVSm3UPjeVxEaUKPx_EQx101JwQS1xlIQz7Y7EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6266" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNCeL251Wz9OQdDIuC-vJFqqR-JudxIuCROkcRFMCQ7pOX_Ab9AO9eHwA85Sv4qW3-aLhh6Sh_Yg0IuwMhiCXKItTe-bg0aCzF0zPQIYMYBb0mkjRBBHG7lZcQke5Ga1dFdv4mShqGqYB3MvyU0I_sAOtLXE_h_-HD9hkIo2AXlFK1DJwG3nfZzOjouMcn0Nn993up5omS0Kjhlmi0YXK39iRKKthgCxLYoqZGTwI2nLPyFgATsly8G4_AcSw3BV8KgdHKRXn5BH1MPtB-iMIwu4F07qXFIqKehqbAPkbBHcJTCoLzUCShY3iHXK6nXqCj3jPDVXDXAbv6MKHZfr6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6265" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6263">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e875845.mp4?token=rR1JNt3tA75ivZ3fttC8BCSQi39IhHpCqLOv7qjU-STOUUfpkg5hU-6h0FNbygdul8JLoWsxbXpmOhj6Q-VU894r26Ssus8bSCmes383l4Ops4SZLbq9dxEGfUOBgcpGBlvsv0d7mtj7sf5_WxxcPz8wk8h32oyoPY583dZ-TUubcuHpPaf7x8CkpYBBrhPIbRn-QecGho3SU4zzJCw1w4kjmGlMhyHpfbQ4X3BmwuqzQobAxiwV0nyy5eH0-f5rqvuLHaKwpueEdanj1wrSQi21FVFTGsAS-CxKTRINCcZaeS0vmZlZfiiFYhWfbRKcgBQ_UN0x-9uTS5tGWNr6EYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e875845.mp4?token=rR1JNt3tA75ivZ3fttC8BCSQi39IhHpCqLOv7qjU-STOUUfpkg5hU-6h0FNbygdul8JLoWsxbXpmOhj6Q-VU894r26Ssus8bSCmes383l4Ops4SZLbq9dxEGfUOBgcpGBlvsv0d7mtj7sf5_WxxcPz8wk8h32oyoPY583dZ-TUubcuHpPaf7x8CkpYBBrhPIbRn-QecGho3SU4zzJCw1w4kjmGlMhyHpfbQ4X3BmwuqzQobAxiwV0nyy5eH0-f5rqvuLHaKwpueEdanj1wrSQi21FVFTGsAS-CxKTRINCcZaeS0vmZlZfiiFYhWfbRKcgBQ_UN0x-9uTS5tGWNr6EYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6263" target="_blank">📅 18:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6262" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کانفیگ ناب
🔥
trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6260" target="_blank">📅 16:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKc30ghoL0Tn2riltCCyAOOgwiG0XC6879G25LnpKUDF3jlYVNvb-ZOuflvPCUye9tZjByXxDMX6WRaTMeoKuYQ2JPwWs_ILKdTr2BZTlQyeBOX0R9gA9nzwjlWW00zjr41FDQwEMf1PpyR3rDRXtg2tzCxrzakXmHfvjdL_8kNAomrmgX20DTv5nZl765qpjs2aDFQGIGpQx_H62W0k_9V_Q8QDXb2r7m3XKnXQqpCMl3vwA4Yqg5aaeMJ1iMOGJFb8glQOJHDp8Yrt33siGbjsIaEnL_kn0ck-g9BBgUHfNhCblrwGzMyhfeYgEF7m-XHbWWM3P19LAjwWF69hDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6259" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=PUAspWafN3KxWvWeRahI_1FREBS4RnH_MpN0RgH6gYnPVy_R0DjPC1lvJVpzJho3rBYTwHKPbs2i4_rxQY24NBDk9ulNcBRrIZtM46H5DOBWk5RxM7zzCmOHqTN6hM710KkNl2cITYHMNhaoC-GPIhuHh4n3FKuiRLEVnCNJccCrDonz2hlViMTIWiFGG_rdl26H-XRptMYRoPYgkKqv8exLm3RMWg_1oGbw19yMm_Jxqmmx7S399AOcVq8vJgteA_C9cwMpsdruFkgrNgo5SbupdYk73euwJONG0flVPNqzNdaZnt5jC57JSAfjvbWboUfSEFp98eokoK_Miin9boKw58cH24BZSQ_kTheT9VwGg55SaI6fChSnY2H0jw2p7kY8rYMqZJRx68aJPQVfPeVbE_XavY9qUZ0CRGUK25kqWUqVuOJsUHzzv66nLA3FRxhUfY6Cu3sitgreJkzZix8XcSSTEhsTiivAX8ny6qg6QT9mQvpUtwZeiJH4VU2Y__Ow_CauKFWcZhPRMMrc0Uaan3CfDx1naoEkkYq_ivOaXEr8Ott0SnyLsEOdmw9SBJIu3z36vcZ7Yut0ZLzbcq28m61LxqL2rzUFECjFpoZmGgxo9a0XflTSgBd2Un7ga1DqukefqycfI2ehD2K6uL-FQUEWkr0iWNcypt5FvbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=PUAspWafN3KxWvWeRahI_1FREBS4RnH_MpN0RgH6gYnPVy_R0DjPC1lvJVpzJho3rBYTwHKPbs2i4_rxQY24NBDk9ulNcBRrIZtM46H5DOBWk5RxM7zzCmOHqTN6hM710KkNl2cITYHMNhaoC-GPIhuHh4n3FKuiRLEVnCNJccCrDonz2hlViMTIWiFGG_rdl26H-XRptMYRoPYgkKqv8exLm3RMWg_1oGbw19yMm_Jxqmmx7S399AOcVq8vJgteA_C9cwMpsdruFkgrNgo5SbupdYk73euwJONG0flVPNqzNdaZnt5jC57JSAfjvbWboUfSEFp98eokoK_Miin9boKw58cH24BZSQ_kTheT9VwGg55SaI6fChSnY2H0jw2p7kY8rYMqZJRx68aJPQVfPeVbE_XavY9qUZ0CRGUK25kqWUqVuOJsUHzzv66nLA3FRxhUfY6Cu3sitgreJkzZix8XcSSTEhsTiivAX8ny6qg6QT9mQvpUtwZeiJH4VU2Y__Ow_CauKFWcZhPRMMrc0Uaan3CfDx1naoEkkYq_ivOaXEr8Ott0SnyLsEOdmw9SBJIu3z36vcZ7Yut0ZLzbcq28m61LxqL2rzUFECjFpoZmGgxo9a0XflTSgBd2Un7ga1DqukefqycfI2ehD2K6uL-FQUEWkr0iWNcypt5FvbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6258" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aaf8OyAPb6H01zaVPi0pOrIa93Em9FMhc8YldL1yrTulb4UuqMRtJl70FfVcUf7zeCxMavnc3pnYUEYHXxGW9CIJSNPCzcaRP9gS7QeB9okcf_kKXIez0Srm1XUsnSqaYW3NEwwgEPfo_604eJvw9WoVpw1PZM-wq36wConL0was6lKHKYax4R4lj8b_iCQOn326RdSR14ofz5B479vRauRn8Xubz8UqxamGy8E6c2isulAHMyCITKXA6j9XNyeBd25pL3bRLahzmvCadHjfIa4oOkPZwtMNw0vtRIwcPY_vbaEsGTW2vgJ70waXrBPFACNgZGurFGq5ae99kCrb3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SfghrXd9Bi1XnZzKyVXhHGQvjonuWHCltZYBT8eiDqRu1SZx0qvwhFEg3REHbsoXWb-I3hAZ7RiwYzRS1QNY3dc1JXozovLBiCHQQM11pkb4zjG6ZHIMOLIwzdsWbWsV7nlfPYdmJMnuZwKNPI6nhETaNNv2mUbuFBuO7m7vLUvvsUThdOvVoZ3sIIR84UQBvam6g22bgn3c_vGywC89s3i9JFk_rBHjmEituI6CKny57TqrWp6a5LDFfx7p9QpFDLZhMVsbE4BUFbhULaVLzrAKAJtu4-fd199ZkPeed_sbNQn0-FBT8Nb-y9hnwsS4-dv7937vXFjk4pPU2duR6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6256" target="_blank">📅 15:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6255" target="_blank">📅 13:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6254" target="_blank">📅 13:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6253" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
