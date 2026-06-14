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
<img src="https://cdn4.telesco.pe/file/g2KPvoJEb-pbzXPAtaYx1EHnXJraooqUVCQSIoT8dS0KFly5_Yu0HThFd1FklMz_udiXm56n3er5B4ZYsZ1Fn05p70wV5FW15EUnU34XVmcpPXSxAchkI9_vSiMGiVR4DFFHBMSrZblJewZca-iLoQkz2iTR6DB4nUj2dy8wXQLPqjTY8oUUYVE7UHXjh0jqiUQizo0vTOUEGphy7biNZt_mEhlzJcwypb1qx2mPfs05H5nfZ5M0IzWgn_GmPEXbfrZl1lsyXk33-qFqCEgvs0Cnh2a4_gfAflWlmIJaK9HlzdkopT7PggJJ-pN5WYaQ39OF7OyGOe_RxgYmFMehRQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.61K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 15:50:01</div>
<hr>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 210 · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ1YdhqOPd08WL2ooZXs09wfNKWod0shur6oPS9d1JN1R0THFLOIrJXfGEnrB38HpI9Ub34dk8yLI7UnUUsr4z2Stnr9Z7ZdEIKxvAwrjZyW-IV2mHEXUnTJ9ZqvzM1R-P8Wo7yr4_ROepHNcjAP6apN1tfEEyeC1zLYJbaiqr-LAZlJBaNbNIx3L3MITLuZMwqEZAl3Diwr9GRgIrCziqsoUkZreG8Es12KYrjGu9in97Urm_N6Mkzr79Nt1_jCevQsAo10vKZiZbmh2_E2CL5guKbRlFQMCRcPlr-xxfMIiexVUlGXV3YhV54mf-KGtxF5rY3xbgiGJD9AKSXqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 716 · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 837 · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5E5MttT82gEWfuWLBltRURoswNrn-6SID5VKyfBdNyRNAGZxTqVUBVeUodwPrgmceJ_96rPaYyV9oVGFjbQAwK_Maek6oXu_Kq9YCdYK7pTabaTPMkjs0c7jow32IIr1nHuoH3ggSS8qhNOefDMIfCAeMHpr_wbfMWIV7J3jk8gB6Zrv2_lBLhWMZVPQH1AvZvIXbB8ST3aFO24feu-4eQEeVfvaLPjealQO3fPYP4aqqkUV9B_cTl038rusaFhUVzio3ZABJ-BB8DexpQ0fzZDpAprHpFhAMotmkQw13k9WGA8SKgYWGX1CNJ0FtUUcuNOPIQNiYaVmWrem9oGZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mo6u7WMjr3fxVA0wunLDUTFPFpg9zDQUtjBuqOq9F5baNX9SrfNamsRLGG5070GR5eh3XnSFB7N4DX6Qhz6MqYG0W7tzQn6UOWKfsFahtES5Mt-nABuiaeYvGM59DttDLHXVacgQnkVTIWB9YeRCIiG755tyMWZQzqbx0MXqZOch6OJB8grPVB8yCo7Iph7XvMy8phmD8db1HpL8qajmIChW9nee0H5-0OZPOaxU5npkAjJMHTLAZn6_u39k-i7iF3yeMZiDNOobtDafq_RCqZu_ZeAlz1DpljhPCH3jO_-WdDFJnfUJ_U1R_enNEt7rOdjDr-lO4ML9N7eQMp-ePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DR5fud7uFOW1cQckANpKGgTuaMGXJY9GKzoY4zjnr8V39IfOP6JrtpULFEvuXaEi5j0PPkeESov7XIFRSkL9aP_DnD7EZ9GK_yfzvAHvSGF1d1QwFqZd1dBK0CI9zz0-G-lwuXWJ-ATx51jixFJd_4J98yrgwZk8GP9lQg_Ej3qWNspE3aKGJjcpCuXQicKST3HPw-9XDDsx9AdfzmgiC1-P8ydb3DKJAqwhSDzR1G7AFTppyu8ehBuEIsKKX7mXd9EwlaUO_OX4_t2r3X3V_yV2RWXMhMqmYNaMHO1ydOGsyCC4cHRpt04nX13FLDg0ZWDZigz0KliGrHf73vmG_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=vTTaTDmgQQY0OTHXWusCr4P6qQRJ3rDcyAmGrqQN2DAp3UPj5VVn8-g_cv135yF5b-ljisRHMgD4nYulNtSIRzA7yfAF3bPoKWmJXs1Uvqnxtid8Tsn2orroJoh7T2Z69DhYAieJNB558GDHzCcHN_Sg_YsWxbHjk-RPt7tx-eb12C5h8wnNXYM5c_fNrcW5V2nWNJpjpijFCycR4R567rqqlrSHPDJo64DSTq2e6cvs1Ouc4JxyHCdnvH9rUuWRzgWKeEih0PmdZgLcWKxBB8_oDi5PbuKigac25Oa8XIavmIuX2yf5m4FOV6do4stZYV9VyfuhMau3vdWA7ceFXhn5d_L3GaBA7Pq3OO5D2zrmNZ5oRxOyI3Z-z3-30R4vL10SosyNI1QLEhRvZvN14Jqrjj2rcVLwmyTdJ1c8NYcjTKstDnHnU-eUygL_PQQOSscRdEkHITnPP2QIwnbGK2keuAJox2fVJdX_GtKXP9TcHKOCBMRlJUZfwMN3DkWcVbFMZ53QRQj0qhsndSu7A1wXT-Gy-83jO7P8oH-6JnKGpDUSiH6OXgWw2c2DvFQ8KjUaXxD2hgbN2AoCoNGpzKBfgRPQE2tkCEEWs_rBeHg5qbU4afqrIXOj9OQ9uJ5IyoZmrDxV1VcNK9_MF-oEEmHniZWXynqJisNyjhJFRy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=vTTaTDmgQQY0OTHXWusCr4P6qQRJ3rDcyAmGrqQN2DAp3UPj5VVn8-g_cv135yF5b-ljisRHMgD4nYulNtSIRzA7yfAF3bPoKWmJXs1Uvqnxtid8Tsn2orroJoh7T2Z69DhYAieJNB558GDHzCcHN_Sg_YsWxbHjk-RPt7tx-eb12C5h8wnNXYM5c_fNrcW5V2nWNJpjpijFCycR4R567rqqlrSHPDJo64DSTq2e6cvs1Ouc4JxyHCdnvH9rUuWRzgWKeEih0PmdZgLcWKxBB8_oDi5PbuKigac25Oa8XIavmIuX2yf5m4FOV6do4stZYV9VyfuhMau3vdWA7ceFXhn5d_L3GaBA7Pq3OO5D2zrmNZ5oRxOyI3Z-z3-30R4vL10SosyNI1QLEhRvZvN14Jqrjj2rcVLwmyTdJ1c8NYcjTKstDnHnU-eUygL_PQQOSscRdEkHITnPP2QIwnbGK2keuAJox2fVJdX_GtKXP9TcHKOCBMRlJUZfwMN3DkWcVbFMZ53QRQj0qhsndSu7A1wXT-Gy-83jO7P8oH-6JnKGpDUSiH6OXgWw2c2DvFQ8KjUaXxD2hgbN2AoCoNGpzKBfgRPQE2tkCEEWs_rBeHg5qbU4afqrIXOj9OQ9uJ5IyoZmrDxV1VcNK9_MF-oEEmHniZWXynqJisNyjhJFRy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=DulBwb702fkGrkdEippizyO7hmSyc-c7fxa-6jxLOOr9Qd5W-ObM2hDPZBnfcWlvut1DwtdFOCjsByZBzQRDsy_I_KPgSp_UoshzKgPu75HOAOrKJPJC6BWEkhzeTPs22dJ0031f0UYBvnafl8FhyFmvpmYkc3KhK7kYss65oOkJ8fAC5qBiHdP0ERcxoifqAYOHjRxiIkXZZmh_0co8B8YMwmYs_BNXJIo4vVE0jl-tGwYdRXl4L2sAXPx7VPDK9LLEHlzUKHSRKnSL2bSNNW2x6bnE-E2E9T7m_EN3BSaf_0m7G6XRD9qmQ9Pdy00kMDGY_TLXOY73pVJPXTGgmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=DulBwb702fkGrkdEippizyO7hmSyc-c7fxa-6jxLOOr9Qd5W-ObM2hDPZBnfcWlvut1DwtdFOCjsByZBzQRDsy_I_KPgSp_UoshzKgPu75HOAOrKJPJC6BWEkhzeTPs22dJ0031f0UYBvnafl8FhyFmvpmYkc3KhK7kYss65oOkJ8fAC5qBiHdP0ERcxoifqAYOHjRxiIkXZZmh_0co8B8YMwmYs_BNXJIo4vVE0jl-tGwYdRXl4L2sAXPx7VPDK9LLEHlzUKHSRKnSL2bSNNW2x6bnE-E2E9T7m_EN3BSaf_0m7G6XRD9qmQ9Pdy00kMDGY_TLXOY73pVJPXTGgmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHnL1JhKRt-Aohn6WExz0Ssm2OhnazA9B5SJke7Mk7j81tbRepiQP2GC6lAgSOEx8w-qfy3NmCifh41U7ycxhTTgwYDhpfCo14k37QxC3in-KWZQqFgWOCvVColEd5uvd6Uiiz2fZLONobGuUMWVENjx5Jm8uGa4xsQQfpYNfVImh8Drvh1muqjcm7rDELj0hCiVgylWYm56igt4IsANG1gCj9qh1k9LxbhuQYM2sD2A-A4jemvwfMyxXn_zHFClwtgVbvDT_WzhA0L3yS-lLkR4ZmMQU7ni0FOjfno-fF7RTkypVQmYyOiApDs7kuTNrxks0Ud0a3uzEzvg3Qvv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdbME9k6KuddNAWkWxqT18VJEWjxIQz_zMcPxvQdXITtZqPGwgf2duDb4hMRjg_wcZMxxR435IJOhVgCoXZ-5cN837jQODRnk7sC1O6YPc2yRYcq3Y_BotolFiV1MhaFESZRc1J4x6NESF3zfLhVn2FZfx8_1u01LBgwjApFueUVuMp7OVP_D1UpnEBT9RZQdQMHn-nyNki-YCp-H5Oy4iJPybtMSjSr1VoFqfUl27Ey1VmOUUUxaPQQ8kpE0Y4s4LT8VpU1IrdaUxyQWOUaz7zmsyVZMoi1Vk6dssG1WGPaH5KjzyDaOdExAYDHMp902W0oYV5JhFX6Pb4egd4deA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N5i-j_l0eXzF9E0k2QYdtZjGiV8Sg3xuagUxiNFOqKydr_QwmOnNyKyc2FUqlTv_5Drf26h7dk6NAx92wYweDfMglNLHrNfr5WOWmPHr1loh4yqm1mLFl47nHS6dzy91ZpEfIlPxG6XUfm7x_7PQfLJaqX9ye0J5GvPlceQ1cc4-BuVX8j0sLdLK6X5y7Ru2wa85gaTjToopMM9z7YqNKSbFxxt31eCWy6tuWfbd-35AMifXijpOyiZ9be3hXUv2Z1cXvbG7WXUR5uMGdK-feDvYMrHZPlDWs7rXjvXgOwMzezvV2notiX73efKyR80Wli7aGQl3drdaKKGHvB-2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lU-5i4GZPWIUuIKL877bWJHIrpGlPDfkpj3ckK8f85GcX2fBT0fOGwtxAEE9JKOArTRu6w_YPZntC-uSqSeNC32QUjKFfd-9eDgcQAwPN5R7BSuwLwfHeZFozp3LzjpM0rmj1FXMyPzXdXcETa62WkmqYdpwd9wMux5GvluNeQGJUwxUacH0RRzSswFC3tbHspZQ-kB0tfZ6ccqZL8u1aHncRZEanQ6Lp5ggN4dJ9WOuycS-dsHluvwWTpUC14YA03unOD7IGf-5JOeQlqWarO9Tv17_btC4YJXW7FyKcHQJQK9eUkLGio8Eys-aPqNS1k75wNND_hzCmfI13XyEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XR2YVX9FKdGwz1frr-AdQI-BuQWXANF_fYNGxFjniViP13mP2gLvojd6M0-Wg88Zf55GQ2mk-wVeV_3l_zqvF4c8zK8LknEoe47FS0-liEAFLm3Of1WgY7hdaCNLyvRV8hLj49eIB2Un_Qv8rMYnG7rLmQoIpxC9KBSUWmCdmWtAOqkNP-x1QeqFJ2FoCZvVjF-sabctHFcuTLYq9_h-nBx2isCmWjHt9vmbmxE7ptTSWsU3Zvo700XpZFNEN2UzLtB05cNWNDGraELje_s8RjVWwKtlcSCctaq0TkWU6yyk6mFs01C5087XlR9siYVngDnvYUwBzpLQ4bGYJ-Z1GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dw01GjsP_svTyZ7bwO0cYfSKq_AYji7K84an1Ln7CQfxIGa2dOt_nNiGyuXCIEEv62C7JR1aoMRx0Y3bEHhrm5dxqXGEXc-C73yfLqTpWn2YxXT8wZ-efzWycRgR3YTofiARyr7w-azkyw5t79nV8YDRLGk-WAuNIAzj5bmPak8ezjGwsqTyMVNMR4xRU9vn2r5Dd587LYHjf0-6UvbKPpWTuhisEsWg57aO0lRgleXK_g04F5exPjdGcjymcr--ef9q71nk898nfE4k4oAQ2Ejj8rf3Q94n1b8WlXXSM1ACodvWmfAC_KhybvfOT7T93GHnfN_U1w6iM8AoYR0Tfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edn7LLKXafwQNq0ZcSybeN2NvrPFa3uf-iAz0Fm2lFrSjLIUIp-OJvGVZuGQ7s1GdH0ignauLigylm1QTCW40Gv3lqQJ8ireuQHLua4l2LXFpVIg8SmKyU9EzGb5sfvI0FYbj6FUpJBYRMzf31BdoBHi7ZuBS9FYpF-Ku4vd_P6dvlwQn6syZcsuSFugzzJPeu6EVmZmVy1TWXn5Qmut8i8u5Pa7nawInXaESQTTcbzrKPMXsqmN92UTPrf_wcYPKS-1Im_9BuFYYC_R6D9iMO4ocMAlUA4IIb51f1RmHmGXv7ow6JtmD5HYFkKRTy-gca0FYfkHRqHiyEC9jD8LCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9IH9_q2itHxlpVGaNelq4FnmENsgMZsRlPerjjaMS2VjTcrDxxUOKIj0prumjp72nX5k4e125yGwVNH8C9UBFzpRVpzvSMvBZMaiYtnIaU6xePgpxIfgQB2TLI6h7_EaOFmCh-IytqNwH3p36A6vhdBRrwbttbTCJmiy4tupbw2ZoJSRGzrigA43Wc8_cuyJmX0cskM8M2VWZDAJiELf2qUm7kEdRkVfhQUju2D_etvuUy2ygixL6GfCO3zZxzJguprG_i8EYY7JSbwZdP91DvrDreeXWy8P_xt0ltZAlWZcuBMAOwK2k5QxBa-BsW6hYR6K4l4l2fT4AGMpEQhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Icg6zaAQZM92yFm7v3qlwzws_XFFg1c1CDZ3yr2JizWNvBykxiGnOVPfwQVzUVLevaJqWvj61pOS0hNupMg1dATlqMnjAVLXyF6gtQOzGhzwz5L78RbXDHMa5oznqGzU24kgAsmfKGqm-AI9YH2k1N45R6TYPlV6jv3AGQgpHcrc3R7aBf3px0zuJUUkWJxCdkuXDG0RCqOQv5qOCaPbPGby8QKy0YsOb1sePXgTZhdBt3WGLn2fGIbUxtNyrkHUHdZh41xPwxbG3ZrdW7I5_QkBVOdG4za7V_18oV6UjMOyUGa5kyC4OwxqdYCUMIPZniyObTxYVqZAsyU5P6T4LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vf3YqHGCo6clCnvgB5q0RJSmXpyG01AeWC6GnX_yY5Vw8X-JhzbN5pgK7T-ndap7V-D6YKHGGSxRR4qGP5o7NHjDc5AyiYcG6OQBTNdLiC7e_QMz6CIQfBtivJkSuPO8HltxJu7Q2lSXmJJ2S6aJWPm37FIt9bJbKjy9uWd6hYgR6FtqcfvAs1SeGerv4WhoNv-Ns5WpBGhP2w2Y1vpUsR1jo6XoGPY9UVDNoAiJjNg6Wu9Qx3FF_eH2D30-CNcmpgLkwwEsPseWQ3VKjZi0MV4KpOsqnvcDw6On5fyN5XGEPLEp6Oyeef0LwKaRnT9j3lAplGOwu_18upWFr6waFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1KWbHs211Ba-kuW-yKGgZoSnxfi1T-t1a5zpLSnTLMTU9muILlehL6UKT4Zdj2nVRzzbBxAxUEnqxwxHIu-WUY83I5yDoJYHsKUTaOF4KXGZYooM015TAySbXxLMFkNIyRaYjIdYCtgh9eH9qiys3wasYZtoClFtGKNeuKVsqdAZGhO6QdPLdQwbztiA117kL_B_ZjZeaTHqycr87wnN3HzGKFCN0bhhvU7obhu1kqe1CFFZmxA-SmMc0sNwfNijpeV2km-dEHJwodTIY0MBr6spCzgPvKCaBuQMIaybxphBX85oZR76IOLASCXz3WWTwFirtPX62-66A6WWUVGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PktFE-ion6-NnButAnpCgFTb3ujFc0fbYU2HAGO-AYo-namwta19IHj1yy3fe-1sgqnuL7uAx1gR_9ml4KJtpBaL5u4ZI3-STec6LLXJxHsxtLdVF3cabIwtEsD7LTgvWKs5lKGIlWPJUxSCM4uuNlyyNEDRCQPpFtUdC7k4RKmz7UPn52JU0PnnkyJdW9I50iohXEj9xAQ4sW5dwVF_uiJT0WhV5_x0PCimUMvmUWtd7QaR_4NEOLuMbnT0EJS_HajArjYCnIz1kjCdlVguE0rr6LHuBntZJHp4iX7J6rvYil0dUnPpWtYPxUvG5In5WS3y2NViylYphDY3vEkgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=U4zVCfdIYUnnsFwadqlqCMMVv05yBjFfCKmaZR56NxTvZCKP28AXYaVPnNdOsTiFNIMmg9gwn1Xs6aKuZ3ly_ArZJ83Vr8f5bK7MR6Lj3spOxmAb0oZ73U4YcYdzH9xmKMKZRm6Ll5PMyPkUxUnlpoiwzFLSi05l1JCpqQi0eW6BuwNBGTKpKB0GWoHkU1LCwUEe1pYZ-6h9SQEvW66W0eFxDsqyyPoiTBg18NKPO_Uw7xEsSHgG7ztz26Aa_4KO_VXUkeJLCH1fhodOp2Hx5UDJh3p2kaSac_5fO-ALf1b-4JGN30T6D24LAx2iYGErHn8syfqQ1SRAA0ZnkxVgVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=U4zVCfdIYUnnsFwadqlqCMMVv05yBjFfCKmaZR56NxTvZCKP28AXYaVPnNdOsTiFNIMmg9gwn1Xs6aKuZ3ly_ArZJ83Vr8f5bK7MR6Lj3spOxmAb0oZ73U4YcYdzH9xmKMKZRm6Ll5PMyPkUxUnlpoiwzFLSi05l1JCpqQi0eW6BuwNBGTKpKB0GWoHkU1LCwUEe1pYZ-6h9SQEvW66W0eFxDsqyyPoiTBg18NKPO_Uw7xEsSHgG7ztz26Aa_4KO_VXUkeJLCH1fhodOp2Hx5UDJh3p2kaSac_5fO-ALf1b-4JGN30T6D24LAx2iYGErHn8syfqQ1SRAA0ZnkxVgVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3fuVp8Phs95QcRFEyTS0sbXUp0hvdJCutiAk_KOGS6LExFyjgdAY2eHzeZ93OMdxQkZi3DgLnVfNofjyGZLVgebnAAl5hD45gHDrAK4I3nShzDjGv10BX5vdBveZYPzQfmDNaHtZRk917Mx6vKXgrnInjNznMbLnGRWXB4uFE7n18sWE9nJ0myIV1GHkxJE9LggYzdCjTID1OPdbgTAhjFJkB4Ut25bZXnY88SW1augFkdwFEat6GduLrFkHnooPdS-4eu05l7PPinXm8QKFbe84eANHIzt934cfg06L2KZp6kTRrUWp6_k98dxLNpUa-yW6kKsGZrHJhfeREeVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmTmHZYSHpNWZ2cLy93CsDUCLKPChqkEs6H5ZOak8c7azGeY-eBMqW-BgcvS3wGmmyTvZp2cMvfqiediy4kUrn3x9RmLYjVSefWZsnJ_VUGu4_BeuXqm7YXAXd7TSGcagEdEPZ3Zgrx5Hyh1zZFbF9zne3Cmb22J2NFlrSFn-xSCKscCsvSxaz2ll0Fc3GhibDCeZzecq0pVq97LD-vh8EaaGztgT-LikM34vMgs49-kFxxrIv80D7mgjPGMOuZgCXHUIYEhCetBoquoZ-RbB4OYU10fX2ieEXplMn46iru6Y0D9RMyie6xPvwLqcnMtbNIiVQNskG_p-RlFl6x71g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szerQo11IZF3QhHEESSj-87iub-2WZ_RSNkf_t-ToXOD56wHx9p12ExYTmj9QWtJ8XOt2al3mFgYLB05YUN_uwrGpR6Oe9ygMJEU4yJH2UIUTR5MvhZ8A2pdSJuhKQeuV9nV_1uus6mxRfyuHw_4S56QY2SJD3o11lVtU_No9WSsfesLWtQk-zmOnJQnAErP-7PAn3ljAAyKuaEtnl5zguyWghvnMOfaTEqgMNr8beyKeq-brq775An1sZma9anJ2K_KRL0MG8Qicv-6cJpoC-Wx2xkgXDmgmj50vW90fpsLhGOff-1BPfZPQcHWNHiiDhXipycqRXA-Aw7HcWXdVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS5Kiu7EDFs4GSQhzy2E521MDVLuGaded2gqxnvTxHhgZMEds8qAcU95kdv494ixfHdn69NkJsl0ecgZPf8eIUIdhe1VxpJZ64kkpIP6k8QD0BOXGbSkn7FERHHJrz3xCbfLqaCe5mB7PBRM426lkavGxBdRg7V20zS7OlpsyIa5GIpSxpq44RbNxrDbAJPJ4cg-2g_YwKUK-QbLdtXK_FGWbbc21flI2pvsofA9z0ebvTd0th8njamrSve2rkq-aTeh1OxqUPacHMB-LSV7WYV47qnanvZet5yCw6U7mW6dkRW3vYRrYiuAdSuyyDwQzyK-ZHqkt6kVMarMVxQ_5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=LhkmlZCYXHhc6P47ePRZ4ZCKkHKxnnBJeGdOrCqPams8fcwCrdssJysHV73LJ0cELR5JT9VU4SY2HgF1VQbzsXWzrVzO89ap4cD8LXkvdhWkK59_fa8fSobwWLaQ8IGu_JW84t7Mg70nKVJQEZIbaYUvrTZUDjqffGkk1wGGC9v_z5lSSqUxkzS_XZztnREU9Uul0kM4uE3thLcYGtwcVSDUyQ6bozOGYEEpeBu2qkv1HZKv63cMBd_WnMXIVQXHd0s6IA-WTzsxJlpiZSkpOOrxiil6uixtnp865tDY3fzBxsB9uNwfYCnt-3uYj_aXpFXyXcfIoucIO8haRvwc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=LhkmlZCYXHhc6P47ePRZ4ZCKkHKxnnBJeGdOrCqPams8fcwCrdssJysHV73LJ0cELR5JT9VU4SY2HgF1VQbzsXWzrVzO89ap4cD8LXkvdhWkK59_fa8fSobwWLaQ8IGu_JW84t7Mg70nKVJQEZIbaYUvrTZUDjqffGkk1wGGC9v_z5lSSqUxkzS_XZztnREU9Uul0kM4uE3thLcYGtwcVSDUyQ6bozOGYEEpeBu2qkv1HZKv63cMBd_WnMXIVQXHd0s6IA-WTzsxJlpiZSkpOOrxiil6uixtnp865tDY3fzBxsB9uNwfYCnt-3uYj_aXpFXyXcfIoucIO8haRvwc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/offyXKVutJeeQaHqGTyDe2X9AYaWtqcd_upmTI8GCpsYmYoaqa_VuQN4O2tKf02acp6gkR-pI7UTWe4SoyxJmsOm_QnxCYD2MuR3ttaEjWNMj6TUh0DG7XaAqhkyWHvX5zY1Y9aKdYCt5CWXO9hD_fdoF8LIP756te2FrlGzWsnce2yULPkEA08avDvxq8qyQ53BEZUZNUmBh_aSeeRGpYhbn0x2-MemiIJm9AWyu0YVqVuvpj-8GNEH-XjWQeM6fgXzsmSf9WW7ubSyc_lWjABKL4X6ItS9oxZ-hOqe2_z4hSozdDAHriWb-WvvF01wmz4E4oTZasI4J02Z0XrHMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFEL7kTIy_2Md0CUrxAHEbc3twvApFlI4FarGcWrU0dAXrglxepAlJtRi-8Oji9cg7Ww5Sf-fOInieEAfFMEGe1jeBJCD1okgOXKIvTduFmwzy_j6wmgQ3FvEBci8iN-fQKbt7fTJdWLjFSjFHHPl9eHdkvzU7TnwQ0QQw4fY8TDeElxf3eVEDKwApZXLmyK_0EY77lf90vPGa8O8g1O5tkc6Bd8e7rieSgx4vRkazUn8xfYn2zg8avih0bRbccXjqKedSlhF6f8CtyOWAX63r9xKMEme23xIO3zAgl-OZdy3uZVp1T6rGdC7JbxIOGtMwCgMXGoibnIMFaDqw-Z_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRKEIiXrN8gK59iPP0F-u7xeywMi3JI_g1i8CXsnCbCio1nyL6yuBjr5jwey1b_7Hr_L5W5TfFrqHM95W8Mn5i31XBKqKMZdjLSO6gFs9OPoewxgYawHnbFgdWdMWlwjtdqdZoi_j3lmQHnXdHa3609VGCd1k1NiXfpemQI_kIoCEwNaDzej1JKQoMBivqWS2RRfBVDCJOPviXzO759STvmbdw9KmPZ-VkgghBCRQT69ucv5OA8-YIdw5Eg1O2FfL9axpQpixsNbeyjWJUI5VpKcE3GZ4zxhxf_3_vIrmeA_fAhVVjRTXOGzwF9NhrhqG9_HAg_Ux-g78ouEAbx7sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogAQFpdqFg8yiq-hyqqkNRxSz0elyZAzuGjEf8vDFd2jS7P1YI_6rE2Dxv5fqT9FTOPv8sIvFz1ArKOi8wqgqwMrI6MHKITWRvTwjqMDpfHI8jWHhwRozY-sHMjRlo8HeOeyUIyjJq-eGwmGQU15J7HqzmiL7GejacXt1fVT9r_C4gGBZLKXLX4-HTrz7HTU121M6KyGjj6c79PceyDdJ8l9jaLYNHgghmKzvhjpu94dGQvJraw2Xq8BRU5Q3HN7ZkAhIqV_TMg9C1VsnSNOPKh9iPyZSyNX3C7Nw59NaV_Dr1lkYz04flPb8z2FurLOaQ-gsDFYlqXmFGRhxITy3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=HIRnPn9XmeU-tks1TDG3nH7TGsYmZIg1_1WeZVT_6HNZvWxrLEObJ-KgXpVOZpD1Z_3RNXsZfNVxVHjeIzdhUuK0uJPqkpCzNW9wYrRKRZgxUEt7vxQg2Ib4JiKVSULXx_bgcLKD-laCsPMpowpmdGitrLN390bANDaopHSpUNua6edUXfWQRv4lVt607HA7tllmYqvA8KhToaklwptFxki7rUxYeu9IgHLtqcIgh74glU8cud8fxEPvTjo-PwKKGwf4fqca3PRiHAbvyA3VpJR4TGiiGkXvfAYExrC5o3iECOgPFlyf6L3GCyz8FWYzdqCzbvLDEKyzHqghNrpuUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=HIRnPn9XmeU-tks1TDG3nH7TGsYmZIg1_1WeZVT_6HNZvWxrLEObJ-KgXpVOZpD1Z_3RNXsZfNVxVHjeIzdhUuK0uJPqkpCzNW9wYrRKRZgxUEt7vxQg2Ib4JiKVSULXx_bgcLKD-laCsPMpowpmdGitrLN390bANDaopHSpUNua6edUXfWQRv4lVt607HA7tllmYqvA8KhToaklwptFxki7rUxYeu9IgHLtqcIgh74glU8cud8fxEPvTjo-PwKKGwf4fqca3PRiHAbvyA3VpJR4TGiiGkXvfAYExrC5o3iECOgPFlyf6L3GCyz8FWYzdqCzbvLDEKyzHqghNrpuUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRuvirWuNsbOgTk_l8GsjZKbIumuI1XEjesd-MZfo179YcHYMc8IY_oP323sPGPGBSLX5k3_TpN4-weCfE4kajMuMgMcNpdR2nTmxdmN_dqWpddo70dDde8ejF1sxnL5hacvQ32qGu-bvC2DCl-s60IkzoBlgfYTPyOozglhWC6unctm84HMxtVsyyanTEHsFBgCP4EArTD48nkHr0VSbIud9XZkhkv6ibpF5LUeMkjiXNW_wehEkIPVnQHiKCPiaU3RNcEs3fKxYmXdy5EXHjg-adwHpkWkkTwsCyzxcaz2ks9b3hK7txS-fidQscIEuug15-ecHvyyXqoFJlfVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iwg6qx5kYq_vVJl-xcRApqLScW94fYj32LsJmnPbdCGzwunWe0FMgBm0pRliavZTeZL0JLwKA8XLparH5_fZVOyl2DUyWA1H0w1aZ6n5ZUb3j70sFTizpvvihrlkoOSAAdM431TMtyijgiipAfrxvTycQSDNJaoJOUQYXhwNN0mLgC9nN8z6OdGNZ9J191QahlnzsP84PkkagKcXnbjr0UBXCgLh48daZ5Ru0TkyYFQRdKXh0M3fFbvXUUvt2LksqdyeZd07_h5WAMrlrT52lhz6zyjyltqcpreilQx7FFTd7K8BFF7UpBSRUw8Wv6KCZjWonlHIPLFiNQ3lnB7mew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWaxnBAJl3r9F8vnbBqK8F1ijU2hxVCyU0eFIDGDz9122-2uIAK4ui6bkqeT65xrcGvD4k86Rbg3N5y7QdRhJmqFnmQZUPwb0TZ5_V5cV1eW5NP5tfQsPrLGiG-zJdceUz0xTigBesdd1QJXXWqxpbXlO4jBVwU45SyFFOErAo2tASF4gi9NIyE7NVoaxTjLc0BPLbnPLwJJ2M_3sEv6_0XspyXSo7yBLeeF9cuht1WzQZT5gtG-453NoR4lg3R10p7fEFpedfdPcup2aetwdcLipF7z64_8YBgl2sctYadR_bWNsbN4giYT1xcQC9xsIjmxHyKyuK2RwB3-rUgwCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPy6P6soO14zavD2KyutotqmS-ICji-ITDz7PI4dXi3xHnpz9qtp29t5a04bJkpsf9wpxYKMQK0n7GJ2kcIcrQc0BiZ0WJoDzLtCOcVgmb039GP1kjW6qjAzm1ijtOgWmveEwvEClPffEs3ICWMEypFBvJ0qAGMzyJoRM2th05gyNyIsNxxOftGxWMHKROwJnYhzWqc3xCFZWDq3IR8Di8Sp-U35HEhAQzJ82DrHWfcqHRD-tVrhpUQWPgru36AAeWx723UXr_qr3t0o11Ijl7mXo2YlDIoSnnpwbVq6H-yQMz7r_opmhQETzBgCZ4wxSmyuqgu74Vr8FJxkeAowNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/foA6_F7p8A5WTGxv_X7AF1WAppYIybdE9_KsEi752uSG2aW3ieh0U731azCbr2WHe4LOUTQB--B82miQJm2RFMMTwc4BSsvxrCP9hEUa5MMNIdBm2V8tDKAiMP41D3L27qZZaTCItORTXt7yObxG3hlPx3jr9aarmScRdJOQk3u64ZYVuQRFnJiPx2fmRWx4EoqdEauQFuhMCoClbjYGJ-kdlnz_KyL7MLAfmVgUrBRWmMEPHMt382L63rZMJrdEbr9A2wtpFAYQJ6zVknskzr1fYRvh4oMoaHs-r9jLTtrMq4RQMIBQ7zrqNRA1Ruc5fu8aNKQjD2DCMhoEb1lWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzAqsAgO3Am_T-HUpP-HC5Nk40i2LVZyLcl_Lfd2i_PDkOCAY0_76BFNFRMKCVO2vjBmPaWHlkrGQCNbgfveKyLn0-ZOP-MA49PGA3fHen_zcowAMEh9h1y2kownLYqY5yCXwHCyrPeCeUic4mOqrU19rymfrn4Oo_HHPmb7yHV41583uvNtyIcC5EJbjHkc0GxZlwyai2_wfGwqAlcewnzF7s4ypAd1gjg5r5bJfrpzr0MfX95-ppzLmMDwBjDPJnDA9K2Z3T4fh9ZxyEUJ5ax6BtHuQ2MG8Y9HyiXmMPC76MnCzyswZaXFDHeYMlSifvG-JCfgf9ww0-I7J5KxOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=Er2siFRX5jjI-tOGT5PWe-sWFQmer6UPosK7CeIRbRRxa0tkZHd9aJKfGuHVSmnaqlMRik8EEoB1X72Bv_3SLaKLxJv2FiIS_0p9sYHZLot3BnZJ9vOhehOyCj5xU8872KAUwWgyr2RlkaTd3dqRXUnASpEfLBnE8bI1-9Ikvo775Q_R18evtQR1yC5QYavqErmA4QNYg2GR8Oe8RoxXh2VdQ_8T9pkSbsFfvyUFRcyNtPagfHDA1byvxOnnm0uvEbqkdJTYR9rnBniiccXEJBuc89cfDiIJiXKqMD6VUdRg5Is_QPuc_ssQvVSN1hQkBnx9vN7To-jR6b3ueLpUJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=Er2siFRX5jjI-tOGT5PWe-sWFQmer6UPosK7CeIRbRRxa0tkZHd9aJKfGuHVSmnaqlMRik8EEoB1X72Bv_3SLaKLxJv2FiIS_0p9sYHZLot3BnZJ9vOhehOyCj5xU8872KAUwWgyr2RlkaTd3dqRXUnASpEfLBnE8bI1-9Ikvo775Q_R18evtQR1yC5QYavqErmA4QNYg2GR8Oe8RoxXh2VdQ_8T9pkSbsFfvyUFRcyNtPagfHDA1byvxOnnm0uvEbqkdJTYR9rnBniiccXEJBuc89cfDiIJiXKqMD6VUdRg5Is_QPuc_ssQvVSN1hQkBnx9vN7To-jR6b3ueLpUJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbWpsG21fApJ5VNb__c_t9kC9EDURbdcawIP1_lk3JUSoGvgnfL6xvlhQYT2_8192LzyYR-8-gusfLHhjLyzwnrEHKbYSvunu3Zmp4i35_gJdxWLkM3aqPscq2h-vICt5El2C6UKHPCzmppLjvwHFS32UaWWJeqGAcVH_Zbieg0KjgiRdvSjGbzCxA1x_QMqWMRxH8BUQkKaB-gvR7UdKB_FhOAWdMDcgd6RwrUeSus0dawW_cV3siGeo8UOvD7jrika7UyXd2P7fu-yaJ2d314oeCraHK6y4vIP2_j50Y2Pv8Mq9vrUGlF5W_5SWAQ16_qiwIWJyRXQs9qk9q_NYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHtsJXoq6pWRfnrpiQ_AXuXSoj6nTLnd_uiwkt90FzXmFAVYvhUKEQQ8-a4MeBQzGxvuTXQmyfhuO2KFg05N2Cw_XVSWHKo9z9sN5PAY0PhZf--oEqlPQeUoY0JLjXe4GCZcWbocStrbrSqPf5Vwnqe60sn3IkbzTeWi3_Bhx6qF2RckYjvN8_p7r8DmakO8vsfPvhB-mR46no2KN1FIgzp4wtVnnNfqq9ADGsJgpB8O0ngfsXVbQs_E9GtPqioMRA7O1C85ltu6Zajb3RwFGWsmHqXe3DXDYu-d8vSM-2xQirQcrTNo7uAXTuykDMfHxYzFspor47TwLRiDLg6acA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEFq01_nljhhqNF8pCQKG-8S0x195bQQi4cVQoXOjk-3sDZlbFSaGTpWlc61g_k_-48uMrH-lsrU5q6QLY9WlUvpzXH558VidRY2H24e8MylhiMLQGduDysXaXbS4KWoaVUXEukByKlC7f44UcbbLFPLDmaj48P3kk0cmeWJ82i14BY748WOvX7LKzlF2dv8e1ODEOLMp2cs_8CYZUl_U4Bd2wnTdNJAh6eFOJ4Za3bOb0Q84lI1HOED_0ZI_tYR09o6mfx7LfkLH6I5c5CBDiTCyLpXF7hEeczQrGPfPTkCnvv0AjIXfgUAzGdWmTqCdRpXhfw4qh8FSaEFBg_MqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hy9n9uym3dkgyvso-AI2bXjKyI-O040nvdYaouWttcwfdLAqN5_EZ62CE5Jh4s59DVE3Kjt3Mju2AW3FTr2nnzqvbjydUwtIdO2XvweJB56Qfkk28peAeVo2z7UzsHhmKCQMzLVFInumD-xZhbrghn_YQgc76UP8IvAtQ0d30z_jxnf9eOEycbNCv8HlbAK-JD1NfvFlB09SQuu0gxiTT8aF_DTHSQagVW1ZgHJiY8GsyMj1PZfYa_opODTfGwmSFPgnIyVHlZaZJIT-X6lKPqncdR6-BaWeo0lUj7xakCkeqLqnZfW9t1waUYn-_Un9qvPEZVwDMrRfv6oixGVSdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=AXEt47OC4gtet8Br0Ortt-jhHidRZhJnYfNNSbLalZGnKk4snUmQTW4o5AcxusXBNLtECIhAiN-_u6rYM_Z3Ueq-BXLmhCMXElSOAvXZWa_HdZ7Jr2hZPk0296EQfkFOiM-TfYnxsyGu5Xw4TY95vZ_Ut79nyCQxnRx9wDENP8zh8DN-W4TvZZIAmC6wHaVuvyzTvghOnhBYkgLXYNf8hEtbV-R-EKgrnqOsnm8erN566zmCgmOP12ZpxmSgY_YgwPcrUEBNrTxafJbVophjTMLsLL3qfpNbdHEJ1q-jn1irbnvqu1a5qPLaqHad4bkeO_9Pnh71CEV6QpsXSlbqFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=AXEt47OC4gtet8Br0Ortt-jhHidRZhJnYfNNSbLalZGnKk4snUmQTW4o5AcxusXBNLtECIhAiN-_u6rYM_Z3Ueq-BXLmhCMXElSOAvXZWa_HdZ7Jr2hZPk0296EQfkFOiM-TfYnxsyGu5Xw4TY95vZ_Ut79nyCQxnRx9wDENP8zh8DN-W4TvZZIAmC6wHaVuvyzTvghOnhBYkgLXYNf8hEtbV-R-EKgrnqOsnm8erN566zmCgmOP12ZpxmSgY_YgwPcrUEBNrTxafJbVophjTMLsLL3qfpNbdHEJ1q-jn1irbnvqu1a5qPLaqHad4bkeO_9Pnh71CEV6QpsXSlbqFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i99-bCeECQ4LwHrQRP92A0DhlDtZ0S7Uy4lZ66EAJ20Zzi1aJoF-H5hdmctcsM33LSBrtvttLCtCYym_mUdkBC4efVdYcz64tKJSRr2suj_UiusiFa-XS1Vvwfj80wFV7j6P5RuaMj8u-XFgWqcxqtf82Hvw8Z4GLPoaW65Y-xlGc5U8-ZMUASPTOJGhVLaL1iDYSbWTTiSPpKhFKl22yne0OlsxI3jPBxroa-8F75JnZwjpSnYZw9gkxDnnWp_POFczWcE8_M9Mb8Q6vYegzdRYcWYHWw29f3Y5GkpbpzMoIoWmUIJUdhxCctYMQsWzVG1IizsQPOYlN99F7Ef9Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3CbSgIETjqPJRLBMAzjvbJUg_yuxKLATzTc5pJgj446ZjwK_ed0bNF2IOFNEXn93HL37UG87hXjB7d6KyAqQ6lD_msMKlwKm2Mb-B6pTyJzE6boxCi5aEPASYr7Ul4kdgCVRxQepKPpDWirpijkEYSK4PExkFrNaVmgHQwHBXWg7eQncT696qRLNFYKdZd-0LFuIFk26hD_B1fw4Qcu8jlkLfFsBeIRf1kG8Yt_y2ezVseXwv4QvKNdF7BDFL6VjM0ZRU2yuDw_ElQij1EdvRZ5dDmQmtBcCpgnnO17_lnPeI4mkve5Rlk5fd5RZPk-jWm2c3AuT0c1e1Yq-PSplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dfx8KLMcOc-f22k3idVEK32nKlU7ec5nizJacGCmAupjXKcyNnYL04ZWeo0FaLZ-3-aTt0jmMRzcmJUdYFiuW-CHbB95RWp_aFQK2ncMiom3Zj9-m-k9jinvD-jdMk6OPdoPKPnaBfCxU-HYLMCoUBbp4nwUTDrUA9NyWokeJiIpq32oTcBWSOx8nonn27N25ld1r9WBFDbMcUoVDwzrsgpz5Unz9aKgOlNUnRycVJQO22OKbuga6X-i3S4nQkQxKPNC4TAEP_tfZbqxexLgvrQCAxJffg4xC7V4-w1up_OddW8CaezoFcJEPhzeJyxUb4FhcQsuZWcJdA07RI_Xdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q5PE9YQL73gogXt3bkM-mtC4Z0rropXD97GvGXEnbVjnPL8FYFkOGeqf2M89K59AbRCHZHqWjUxMkA-u6H3EGaOIz4f0azyT1YyyLOErCNYNfEJQI4V33e4Oj4RzVwLZlAe2RGvBUJgKx82OmhQ0vUQ6C8PJapF8g3_hPqfEsmjus4H0Ck2HZ8fZK8K3nTwg-zBN06gnOQd05UQ5vT_DFM4UtXWJIgih_xS9RTEXhrSBUII_WtSOLPxpnU3bOIXgNgTVcCA9zyw4Wdm_aubX0LrSExRnpEYJy7x0J-XSPtFaAUcAgqtDNaPUrInTYwLXmSztFjj2GmC5Wjvw-Ig8ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=kwwe38fy4LkAt7azkFKYUJaY1ugadOGPNRlhFUgrxHwSSuH4RJ46Wp6KnLSc1e8Y9l6dxVicYZGH4MbxP43wFWI0jL6K7BEuLvzPwzsO_3NoMBf9FyleN5SRA1Qv_RjDKUlDQx2SKI8eLWr-TFS5feBOS9Jqk7qvmbRYWDL_s9n2VB6kfpwBZoCXbXg9rcmksJtySkCSvz6WuTF2EgBdc_XfbtWyQzqZTj--V247zSAPkxUN1pOFJJvv_yH4dP8azsOP5zQxU-gZjzRKWHOmqS_gBfugC5w0uzzzVFb4838ss9dm3wyu3QkLHyaMUD3fQnfxxQ2fnTPst8az3plakg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=kwwe38fy4LkAt7azkFKYUJaY1ugadOGPNRlhFUgrxHwSSuH4RJ46Wp6KnLSc1e8Y9l6dxVicYZGH4MbxP43wFWI0jL6K7BEuLvzPwzsO_3NoMBf9FyleN5SRA1Qv_RjDKUlDQx2SKI8eLWr-TFS5feBOS9Jqk7qvmbRYWDL_s9n2VB6kfpwBZoCXbXg9rcmksJtySkCSvz6WuTF2EgBdc_XfbtWyQzqZTj--V247zSAPkxUN1pOFJJvv_yH4dP8azsOP5zQxU-gZjzRKWHOmqS_gBfugC5w0uzzzVFb4838ss9dm3wyu3QkLHyaMUD3fQnfxxQ2fnTPst8az3plakg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=INkCGp4ge_Uv3flnNB-ys4T7aW3tUXYHX2txVRXfWTJUoWpOLBXI5Y5aenTtrRY-8f05Su5_ksjL7sFwUD3j3eBy-EsYPFPKhIDyrcxe0EUsHJpaJSoXLXoUOJf8HvdxbEA3yXeBPFY49TftTy8gmT3Yribuz7ZO8Xw4q8KewfhhuBSv5KdIkdyd45bUXuNA1jvzc5_5IUC4pS_BXeK5A3BsuXpfAkk-dlbA9FtgvLv1sXPNAUWfScAFpK08T6FC6sNBWZht20DmNODtihK4fNf5Jv4zAkhK2kH3jMQvuKfgt7JDr0lBCiAIP9vu3ZeJ6oDDiGmejJN5HFQH7NKeVg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=INkCGp4ge_Uv3flnNB-ys4T7aW3tUXYHX2txVRXfWTJUoWpOLBXI5Y5aenTtrRY-8f05Su5_ksjL7sFwUD3j3eBy-EsYPFPKhIDyrcxe0EUsHJpaJSoXLXoUOJf8HvdxbEA3yXeBPFY49TftTy8gmT3Yribuz7ZO8Xw4q8KewfhhuBSv5KdIkdyd45bUXuNA1jvzc5_5IUC4pS_BXeK5A3BsuXpfAkk-dlbA9FtgvLv1sXPNAUWfScAFpK08T6FC6sNBWZht20DmNODtihK4fNf5Jv4zAkhK2kH3jMQvuKfgt7JDr0lBCiAIP9vu3ZeJ6oDDiGmejJN5HFQH7NKeVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFm4u5oTHN7NqYKeAWeK5aBBlDkLNawnVStU1ywC512auFEI_ntS2ckQSs1Egixu6pOoWDHbHZCcRToVMp1zZqMkHIqaikG4xi2fyA6aZIcFspNJfM4XFFeum3d58dxbe0Q5z5BL-RG3UkgyMur718hhZ4OZOPPyarSFeSuX7IhxyHiTqR3ojxnTZhOdNpJlLHjQsIqOfgh34VrvXgHr2QnsszA9k2p62iHwG5zSDs0t7j86UIRGOjp8-2_Ktdfg1G19nQqVaSCgK3URrgdxIp-Wfu-1B22Z2n5-DZyA4aR3fZbWACEsA7A-ZawmJpHk-unyPt2OIIFYIyvEnkPz8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=fQgye-imbHJgUgDwMbJH8fxPfTILKaSpTz-HSI4nmLgnf1QD4Cq6klZya6-cXy-Komy3WnzLm_ME8K4EzE0apXTHzUfS_SJwZANVtTe26cQSHnRj_z4WDIIEUwSHqYeaRlJZ-gTVgr_P6UjQEPyhszQmaM_Nb_Wq0ocbhEgQQnuX8ocoryQVVoc-RkbAievGGrnyV5kqaJnz9eijNc-i9F1rkrsYDHLTSLylenlXptka07S4P07A3UH48g2UlHOVmIesm1H2MU33beQ-KWiPPKgZ4ejRpP2S9jVDBpeJTdKqhYn9elbP5UgR6-XvvGu_syiHUHcBDAP1f5-3begvnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=fQgye-imbHJgUgDwMbJH8fxPfTILKaSpTz-HSI4nmLgnf1QD4Cq6klZya6-cXy-Komy3WnzLm_ME8K4EzE0apXTHzUfS_SJwZANVtTe26cQSHnRj_z4WDIIEUwSHqYeaRlJZ-gTVgr_P6UjQEPyhszQmaM_Nb_Wq0ocbhEgQQnuX8ocoryQVVoc-RkbAievGGrnyV5kqaJnz9eijNc-i9F1rkrsYDHLTSLylenlXptka07S4P07A3UH48g2UlHOVmIesm1H2MU33beQ-KWiPPKgZ4ejRpP2S9jVDBpeJTdKqhYn9elbP5UgR6-XvvGu_syiHUHcBDAP1f5-3begvnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwyMTKWqzNhMvxbtfciyrugHqIexikEUWmoS6twWGiw7LHaCj-1wsCM5A7EkW-gvHGY8EygNmEZOhTm7x_Mt4Hx1JHav8EFH5NY5SNlHy37Ac7MTjZxGqZp0UOY5wD7zanXrWiMWo8kj3YE4T1JfolxPig2pVJ7CKFqUFUfJJbu8z3LyNTaeL3rYENJdDc8H2VhpCruUbii3EwUWrUp-humoBIy9QDn-mGHFS3zIX9XphqZb7Gs0EtMv3VPKfKX7SjTVRzwaXQiNPF8NVVzXW-Ziz6guMuy_Xe1QBy3SE9rNEbUMVM0eZi-njXVZz0HVq0kTx9ONYZIchc__eoj3EA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgVU2XTCho0gEfGdxf7XRFs6_s72OGofQlOXrbY3yz3E4ot_pGYizoPJ7zFVcF-bspSNdKCSjUZc-O1kwEZ_zjkT-egoL2Xq3G9r1E_9Uje54Oiz_qXlEdWRCldfy0bw8yQuXPj2CBSlCl3uQ_H2WU1iwSpaYVasq7v60l5Mt_xJBz2ZG7a59AcNiicLKr0z4RYU-R1uwtrKBJMSE8A5Wott41s-ggm6heFzSFzTvSqFN6MXLIR_OOqqxPzPoTapuFZypHGDts4MRSQxufm8ewIff29UFjGHa59uScnawTi_Tex_gCY8aa-RxVHb8NfibE4TWDN8F_tMdmmMcTiIhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=j5P_QqGp0LoCV9KxptReZjWKNDaKa9Zz9IVDQVPa-3dlclODF1lneD7OjCh_TJGB5jBiLIw6tPlvQvgxON4W84XwEGFbhVdjSd1doOTRPiSs6gcv493_3Hx9jvEuZ1I-bBAc-jvYel0vCjhzrPe1-NVQBeLjcRxkEcgmA2ftp3wSziKMZQ_cU4Tcz4GlkxeNR8t34P2gJAoqu0TtxwGFgIvupcdC64vWN5w9RkHYTlLH9aceBIzmVnDNsWuG_Lx8dmV0nDmgp3-pfWAVbRGSVBmyaTBYKQVIqoG0-FNtDMf9gMFDOwz3E7ZXr34_nWGEiqFZ9R2wmvCH8J6uXliwiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=j5P_QqGp0LoCV9KxptReZjWKNDaKa9Zz9IVDQVPa-3dlclODF1lneD7OjCh_TJGB5jBiLIw6tPlvQvgxON4W84XwEGFbhVdjSd1doOTRPiSs6gcv493_3Hx9jvEuZ1I-bBAc-jvYel0vCjhzrPe1-NVQBeLjcRxkEcgmA2ftp3wSziKMZQ_cU4Tcz4GlkxeNR8t34P2gJAoqu0TtxwGFgIvupcdC64vWN5w9RkHYTlLH9aceBIzmVnDNsWuG_Lx8dmV0nDmgp3-pfWAVbRGSVBmyaTBYKQVIqoG0-FNtDMf9gMFDOwz3E7ZXr34_nWGEiqFZ9R2wmvCH8J6uXliwiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=jzMtA9EKydBI406v5Yu0TosaBsUjxoI-53gz2sModmlnAdVa0jlOcGcj5H7k4Wy3pp-w7gAm-FzDtLz8bMAT3rG7dXwoEQdbP4gr2Zbz93tkU24_dNOel26VJyV2nXYuTwU9bBAZMdE9CsYiF3_e19BlrJGlCpAuZBsKuD7GsGnpvvzTw-Dx0mm11jVxM_rUII0ue2i4KP2DyorUwFLmv8E2HDlW793Pq2y4NBLBCIMphlLlwillNnOJh5NOVWBnjeYZLAzj86l6FnMoBgWBdlC6ZqNVr6mrgBJOC07UONf2teNagx4wxKFdWXJtWxrDJypNAG_0G4fLHGG0FNymfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=jzMtA9EKydBI406v5Yu0TosaBsUjxoI-53gz2sModmlnAdVa0jlOcGcj5H7k4Wy3pp-w7gAm-FzDtLz8bMAT3rG7dXwoEQdbP4gr2Zbz93tkU24_dNOel26VJyV2nXYuTwU9bBAZMdE9CsYiF3_e19BlrJGlCpAuZBsKuD7GsGnpvvzTw-Dx0mm11jVxM_rUII0ue2i4KP2DyorUwFLmv8E2HDlW793Pq2y4NBLBCIMphlLlwillNnOJh5NOVWBnjeYZLAzj86l6FnMoBgWBdlC6ZqNVr6mrgBJOC07UONf2teNagx4wxKFdWXJtWxrDJypNAG_0G4fLHGG0FNymfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=HCt_V-nDIKRoZrq09PkZ_c2orcRrlT502BR9yTynScRT_b2nUNn4aMZ06Whlm8e9mWPrYG8oFBm2oRWnHTgIdDiEr4mpn8JoLpx4l4XmOT0S2udTN9qZUGyX5uNTCIWl1SjPZCRIXS_byzn-dXrfEloAytAbrdTx7lP6uqPFa8YMqGI4qCDVSP_oJ6buGFgpDPHDxpp2eD3jm9KPSXM-u4mOzl62xCSrxsdlFhwgU5vrcrOxxscl1m4JjFIU3tQlW5GmpBFzA4gfZ4wRAut_ecOB8ED77pRhTS3aQS46WMLwTA8reDwLwy161xaULESwzjpZBGxp8BM_Ef490q4kTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=HCt_V-nDIKRoZrq09PkZ_c2orcRrlT502BR9yTynScRT_b2nUNn4aMZ06Whlm8e9mWPrYG8oFBm2oRWnHTgIdDiEr4mpn8JoLpx4l4XmOT0S2udTN9qZUGyX5uNTCIWl1SjPZCRIXS_byzn-dXrfEloAytAbrdTx7lP6uqPFa8YMqGI4qCDVSP_oJ6buGFgpDPHDxpp2eD3jm9KPSXM-u4mOzl62xCSrxsdlFhwgU5vrcrOxxscl1m4JjFIU3tQlW5GmpBFzA4gfZ4wRAut_ecOB8ED77pRhTS3aQS46WMLwTA8reDwLwy161xaULESwzjpZBGxp8BM_Ef490q4kTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6267" target="_blank">📅 21:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWnC_cyNAy1T46rlX-KYbYIBAE39ayXKPdFoIsDXQf74N9Ue68n6mklV9LWZCAufCZf33toh5c3EEWngtCDqklncOO0m7-dubDExy6d912PArq0CYL02hbzT9iaBv_ckQk4zMnSxfar-6T1buTEC6ehPeEGZQ67XiLuL985M3tiWk5mXUvAb6kKYARmt1QneIsriYJJjBshqjMO8kdsAArm99CNNYwrkO01keGBVuHgqpY3qberuSwGc9xSIlNzVyi-mn5PzK2Se1Wp9I5fMVbTwVOHXvEI0JTlrDAlgBhEpttlSw89_D0LkgBV1F-omXevyF-yfB0We44mglayU_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gue8IMX81_EjLSQ7v5uwPEQa5ds7voZthjb89QLo5E8IO3XtXIRuEZue08TQyOU1ZlaKlDAopy59R1w2YsTlMLTnH5e4cMQWUpVx7QMMB9frahlNFy5b1fXvjFb1rw8qtAMzmhk7wcUXxS71T7uspXGzpVCwNNKCmf9_z3lBTdBBtj06MG_asFCUt0hkfrK8_a7f8ZoQoOheaA0Xqk8H7PLJxwtm3p5j5z7vBhTs9o5_3GLsXNaIIg0J-luztYFtDlp6Lj96LDdio7p-dR4Eu-FadwXRpxsLYqF3mZ1u2nJg43ZjNyz4xjDdvUGuFnMGBKvkLPheF02PQDVX4xffSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6265" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6263">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e875845.mp4?token=iHc_CwqFPjRtUKc3JlenrSfyjzCzQ5Ha_dwp0bxNc9C-0J_KCyKjYVEaXmFHJuoSx6COGEp_rXBAS851nZc9switru4EtSlHu5uiUgwZ_rCcLMGlEASHO7Jpn4mJwmnTZY2d_JJzRz1NDIUUDQipgw01yGFRgxTayPmp59k1nusbaRqcvImH3MlAa3r2Wvnm1MIEICO6TIsxhJ6CI7zmyUyEuiB9zZDjhSRZzFvqreWn4-W1LLbWbhS6MwZvy1kYxnKazcJzY-3z1HjAaRNDo6eRyrAawojfpooyTjIjY47PP9nuaf5YgHRcs90fcu2ogTXw3xZ-usAZ4s1wlAkiQYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e875845.mp4?token=iHc_CwqFPjRtUKc3JlenrSfyjzCzQ5Ha_dwp0bxNc9C-0J_KCyKjYVEaXmFHJuoSx6COGEp_rXBAS851nZc9switru4EtSlHu5uiUgwZ_rCcLMGlEASHO7Jpn4mJwmnTZY2d_JJzRz1NDIUUDQipgw01yGFRgxTayPmp59k1nusbaRqcvImH3MlAa3r2Wvnm1MIEICO6TIsxhJ6CI7zmyUyEuiB9zZDjhSRZzFvqreWn4-W1LLbWbhS6MwZvy1kYxnKazcJzY-3z1HjAaRNDo6eRyrAawojfpooyTjIjY47PP9nuaf5YgHRcs90fcu2ogTXw3xZ-usAZ4s1wlAkiQYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6263" target="_blank">📅 18:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6262" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کانفیگ ناب
🔥
trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6260" target="_blank">📅 16:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qym8vpe90XxNjzY7bpKbAm2lBqVXHz6EiCk_I8vmw0agNIjnshij8oBLUOjA3oRx9xoXTqcbQDo9hlW4OuatvzfAj_raGu0Frc_5P7CWGDmQVQkCPxFtWL10VmjYzJhJS3HS8JPlLVUV-BrVHyK6_En-gh8kmLSWrTQa8Kte8FkZKMzE0Xx7-fHavKb6gS9A6De3CtGR6yKYWf3h8HwQomfpiqwfAdnMIMzK_QJWpI7uQ32PVICAUlNcwZy0krWMspgno13qIwZ6HBfF-tvXisJ1bxVWNvra03je5WBFMcuukTwb-WNtl7QPOYrF8Kwk7GzRQF1SwrD47XUsbBAz2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=oQsfYYXFSOPxtJHoFNtjW6O_HgwPA7-GzZ8OcKF9lU2I_YlJF9sIajsJCwkoA0gaYB3qyWai8-Tz2z2KbzlaAVGzpn7Wh7t0nn4P7DrhVEiaMbs28vc2PZFnTBFHgjiOWjsciPaqiKsTVGeOK_onYxTGKrpC8OiuLq4HDG_vME3HVxPvEAOCK_uc_HakNoEMD1fZijauniVUfZyDwEvh3MbKKrekLS5AEhhWwxN7CnUPqxZ1RX1Xw6HLbNzOGfQZBzSMGmEY3BIvOQd6swz0WoRBTeg6twWYlRh6iudSOeU6r3dBowFSXAksvBfMnM7BNE_Ch3h7Z-cswr5_7HYf8LCW-R5K9WnJBMgZWpQmEee2Ie10ErJ72FrWESAgmIkboB6ev7D0H3EDAqKVQjY32z1bZVUDyBybCnJ9pHS_sdSKpILycUBtt4vEXuu-QRnckdpamIbWGqMEq9ADZj000S-p5h8vwfzzAbeu-hCLL7pGxGfVyvBMfWnR4jgkiioSX5Wod73U1D_2DDud6JMphXBmKI9eTTsJlO80Lj-aZqef910OQfYajXLVsGsBvy_NHjHCrWeI58A9CEjEU6BxD2TFTtX-flw3f52jkaBw1OUAG-jJ7U5a5IVUrOEs8DO1OapK6z7cBJKGuNgawFhzPJ_3U3IdVHqwH8RJ5y5biOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=oQsfYYXFSOPxtJHoFNtjW6O_HgwPA7-GzZ8OcKF9lU2I_YlJF9sIajsJCwkoA0gaYB3qyWai8-Tz2z2KbzlaAVGzpn7Wh7t0nn4P7DrhVEiaMbs28vc2PZFnTBFHgjiOWjsciPaqiKsTVGeOK_onYxTGKrpC8OiuLq4HDG_vME3HVxPvEAOCK_uc_HakNoEMD1fZijauniVUfZyDwEvh3MbKKrekLS5AEhhWwxN7CnUPqxZ1RX1Xw6HLbNzOGfQZBzSMGmEY3BIvOQd6swz0WoRBTeg6twWYlRh6iudSOeU6r3dBowFSXAksvBfMnM7BNE_Ch3h7Z-cswr5_7HYf8LCW-R5K9WnJBMgZWpQmEee2Ie10ErJ72FrWESAgmIkboB6ev7D0H3EDAqKVQjY32z1bZVUDyBybCnJ9pHS_sdSKpILycUBtt4vEXuu-QRnckdpamIbWGqMEq9ADZj000S-p5h8vwfzzAbeu-hCLL7pGxGfVyvBMfWnR4jgkiioSX5Wod73U1D_2DDud6JMphXBmKI9eTTsJlO80Lj-aZqef910OQfYajXLVsGsBvy_NHjHCrWeI58A9CEjEU6BxD2TFTtX-flw3f52jkaBw1OUAG-jJ7U5a5IVUrOEs8DO1OapK6z7cBJKGuNgawFhzPJ_3U3IdVHqwH8RJ5y5biOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6258" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbZq1QG8I7F_EGhgBoy_e1KJdFe7IYda5PaCvDvyZe4f1cDnTgPHn6Jzx-pFR35sUYrILxYMxlhtj7Z2UYXuCcQfCLbQplW5l95rOlrK7RFMsIyeEmvTLlwxuueKbFtT6dT4E7IqhjiEVGef5yoc3y3SU-h2MRyBbgJMpfoAfx5DgzwR2rfM5Zenvzx7uHLGYxixfoFffhkWTBAiv-KYZ5cLFcsuo5YYAQWkqjpifo6LTsZcixZwIeuZoySZUIJvt95__7d1uCUQ2biHyrM2UPtS9LHc6H0xEwojIhA5rhGYnJdl664ZLz8aS6dMxMHzaEKOIZEVP0epHR99TmtNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMXnKHBMYY9OqpGHlRg7jQEYw1WxEI4Ed76yL4QjM7ScGla_w1x89WgL-fKoVT2CSf_1VvCy4hAJOVzDvsQeK_VFYcBVYcm0Pmb2JxANbUaKfAlIxeCc6oT-fCEbMY-plFKxhJ6yWbO7oEGAVlXJ2UZDt6ViBhmBH6Eio1-juWg0Bg8Wa7czRxCaQkimo62OGZgxMmHReDR3MpWYs0JD9JJhfmDfeFfg_NSpDHcBKffRj9FdcA0_qMdRuDzYtawcEKQanklY4g71uj7sUaB1hxe7_NxmZoePEYAxCfCyHSBxFFAHzke5eqIjB41A11lSZcSLmsA_3L0YTaowodYJNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6256" target="_blank">📅 15:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6255" target="_blank">📅 13:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6254" target="_blank">📅 13:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #3</div>
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

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید  اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6252" target="_blank">📅 10:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3I1tGfIBZYLhNIr1q9TcEAJog3RmDHKQ7bAfSm5EQ9ZqHehCReZxR7PydpuxKvuarU9DGTOYjLuqOZngcZ_c-Gg4oewD3dMeXXsmeiLtBUuNKl3DotJAZzR0mdtdjvrlFMOJuldQzsyIrhDQmVYA4btkVbnaWZ2qq93wpnaO711LtprXAloZG4RaI2N7HUOFVGD3NW7koBlpKvkIAg1c6CtrtKjcI7ydJnhAdVrMjKPTU-7qCEWfmfA-5u7_LMIz-cZIFUDsx4zcyfjxqO9CFJNYZWoWLXnXqwzzxdkb4L1k8Z7ii2C3eTMForuQSV5-lxtmStXhc9X6bJj3VlOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Unlimited hotspot shield vpn method! |  7 days trial
/gen 415464440062
trail→
https://get.hotspotshield.com/trial
zip → 1216
Browser any
Ip usa
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6251" target="_blank">📅 10:39 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
