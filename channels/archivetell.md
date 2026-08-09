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
<img src="https://cdn4.telesco.pe/file/NnLM1jWH0iXRfg-3E8F0wtQeklMJoT43qnN2wZa4Zal7JJZjNY_WjoaI8C_WYAklT3eIh9xxAOwSkPBKNDkOwpuHtanVlWpkOMvj9Q0SOhlMRJqAYMgj4dAR6Ir8_8excow4OgmRK1aAxW2sUMDl8qP1UNKRiGzCFOOggiiOjSnm3Oun_BRRkmKWzDFzzXPl4-5TQgKX-syE5bHCSvbs3b24Vy3dFJjOcgm5FXnbnSb7zgmLjtk9MyP6Vr0K7RCiBm2RnC4nOvPkGar84R3D9jkeT1IqFQksVTPSHbqwq_uW5R4pULD3vurNqUrJr4z6P70NirLxNydgQXMYOHOlvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 16:01:31</div>
<hr>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpFIyL_Of2wPn0089cM2Iewgcz5QLZY_wiUyyGtJ91gm8wjXkKqPYdEKMTjTtXADrUF_kGNZiQrwDOeXmU1ZxBLDEnuUaHXfW4xZWF7dqzboBmQzfPxXP3DN_nR5xWGTAcjYJjQev3fRNtSPjEfmiuZUzAVh3yQcnVip4Nep4bJuTa-5DS02b30ceeYoOQm4F_yG4pixjnDdja0VK0vvJXbHbwqOjCwJZIBitItAhhn3JQcWzpEE0bJVjCHd3DBCBjzUoT300Bhc19tyWC4nKGqgONSXyOwl0oWLUfgaoFe9wpzzefT5hRyGbeepm9FEgs84hpbRc3XmPLcGmzgUcw.jpg" alt="photo" loading="lazy"/></div>
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
| VeGaS</div>
<div class="tg-footer">👁️ 550 · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddH5ynnAIZafFC-Nvaou9gaf26CB8asuqtOYP9YNiBac_kbUsiTVVrCYZjFUQeW3vWdD1xvNKmdDG7-e2apmuxfHmU1s11F5am5MsUGsiwd3AeND-XS4Ldi5t6hhJiPmZV7nHunvcgnO3o0LxQOSfnAdMG05bPBROjHso8Fi6pwnWHlmAdskRVM6JCVcdCmTpHLa_hEB8BsUIvnrl5gD5j-6iY-ToJ6GBbtGg9rvk3RNcXRrqHtpqe4RHQbfZB7OA-cQXf7Pi0iru0en3jQQGNiPKXuv232K_8p8YepZG6tB5geLrXRzUCmlFyJC9JJD7qcL0t3SBWHEBQ5YEgUBKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 903 · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=gWml938VHwDVoyoD3ijGr6hGGdCTqLv9G4TQhsHzTEaJ99OOaYeh3Pr-JL_UgcSuV-y_3eKV_hqRQjo5oRjro8Ey9TEzNsrgxKwIubxnzZgH4vgFSCK4JWcuH3zv04D8GcK6fHSaMNl0NmanlMyAFpC3CkVXIJ3RkVRQa4ztPIqoWRJOg7XpbUfU00LwbnL2d2Np6tXsjBpE13TcfHeQQ2_RU7z6mwT9QfX2GoVR876HqTCGhcI5CESztBnb2bfnCtltMefM2eF31idc5TzcfcHwtUSHmEyOpHQIZlI4AU22YjtmWxEwFYb2XdpXi9AcFQIuJGiRMBpopBLRqcUF8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=gWml938VHwDVoyoD3ijGr6hGGdCTqLv9G4TQhsHzTEaJ99OOaYeh3Pr-JL_UgcSuV-y_3eKV_hqRQjo5oRjro8Ey9TEzNsrgxKwIubxnzZgH4vgFSCK4JWcuH3zv04D8GcK6fHSaMNl0NmanlMyAFpC3CkVXIJ3RkVRQa4ztPIqoWRJOg7XpbUfU00LwbnL2d2Np6tXsjBpE13TcfHeQQ2_RU7z6mwT9QfX2GoVR876HqTCGhcI5CESztBnb2bfnCtltMefM2eF31idc5TzcfcHwtUSHmEyOpHQIZlI4AU22YjtmWxEwFYb2XdpXi9AcFQIuJGiRMBpopBLRqcUF8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYLzlijmZ8tFZQCCjJ4mbBDbeXxBeyRMcln4NNEA7vEYEKOj3X5D_ouR3Duib3nw4ObGqYmMZD9nrYRZhSwZcJH8SSvDPNG_7zmgVjnEeJ3fnuNd2IYS466hIasOUtOBgWkHvrhQSwgUYkxZtJPt3MCmdPX0ILg7KwVWixuPSY55m9z-pjmpkyfLY2EfdI9zl7ElCw7CvSB1l2yspI_pXWW8tdmPx_KaWNSST1jsXBr0qEgid5RRjqm7lfUsiO-g1k9m_uMtTIjG2hgHnKEHf1gx0Lg4-0w6nAlNLZEEa2iHOuX4eyi7PXSDMa7vCyXR9-LnufRoVu4CUianjHIwaw.jpg" alt="photo" loading="lazy"/></div>
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
| VeGaS</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=DISDgNE9JCBJ6jiGKJNLKBBTwEhQASyMpaRKJud5xFeI2GaCwwnZ2Y6miLvuzUc-InI24zqofHxNjgx_cipEMphCFbggTZnogteVWWv7B27OyDKKyesyX9_k9F3TZTADQDIaC6HwMo5QWVaUcl6zh6hrcOvxTRKct0_DHpn_9Uu0IfQtZHIL6rJArVuL-oJuL0GpjQfXxlMi7f0UMagNZ59qmrDfkCBc-3lLSePpPzj11tMRf7A41MxoOhZX9G-Hxtw1EepntOtOkPOlzK9xDeEWJ3hHbPrIHum2wu7vE02XxcRg6fKtNoJPhkNzc8REohqaThlOmCUUcBiXTHWccg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=DISDgNE9JCBJ6jiGKJNLKBBTwEhQASyMpaRKJud5xFeI2GaCwwnZ2Y6miLvuzUc-InI24zqofHxNjgx_cipEMphCFbggTZnogteVWWv7B27OyDKKyesyX9_k9F3TZTADQDIaC6HwMo5QWVaUcl6zh6hrcOvxTRKct0_DHpn_9Uu0IfQtZHIL6rJArVuL-oJuL0GpjQfXxlMi7f0UMagNZ59qmrDfkCBc-3lLSePpPzj11tMRf7A41MxoOhZX9G-Hxtw1EepntOtOkPOlzK9xDeEWJ3hHbPrIHum2wu7vE02XxcRg6fKtNoJPhkNzc8REohqaThlOmCUUcBiXTHWccg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ou3WoYeUpez1lwhTFjC4-2wkvApueClXj2xDSl3DevvPTt-MSXX3HlC3CCDBfnRMvsYRO9TMwMIW2jxrlh4_EWtiOpnpnGV7Mp5J1-dDd1vM6wk2_OHRA13tfnPY1Gxba3BsrzkHr25T2iGNM6vzUleY0X9Xja0N6dQB3ZgVSCahMAxrS_a2I_RmucxbZl5xUDt5FMyDsVzgwekF-7nK_tEX9zgfzeaV-1jRAGq4rsM_VLTQCIfRIvvXHVnG1qGzypJh-YEA96r21czvKBMcE0iVV-sOnd560kFVC7GA5hLPRlarVVk5Api0RNrST0_HsHXjSmLZlPOnmE8W1Ii4cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQH4QDOQq_jbNA1Dj01-IctKMTIZmwZhfPIMZZJWZwPGVkV4fUpzIQ1FutXCNs54_jkklkB1zSxXEu04N2EZ-gTaTdv76bQ5MBtvIQViA4pHR50AdnigACkyo49H_aA41IdJdssjqcopkwr0bdvwq0-TeMyivCaq4q3_pqUr3u4e0AcasGGF8-ClbzdsYT_uPmzu2_cqOpgdgxMuHpjXS1j1nZOaW-RyJo9vXiMZrT1G03nfRplPwJi3h4xe7eDCuTsr46Dg_mwMbGLIf_mzVM3z-pbtVzPItzZiJcO7Lnl5goq_79exyq3RriyO3EEBw0R1DzNxrBIzxxLKLTY5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7429">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPT08iNqJey0XA5rQ2RY5dGJIiv6lkN0hfA1r-9t7_FZBXvzfj991_6-tD1hzIoXCUkSNzQHGioVcnSzgAZuu1LoyVL9eKyBLNj4-0dIqCTDP36gJesx-k7ZdGJigFhYupHoZzgLd7YG6zIdfpvQrpTyBO1MM1ECMJiLQ_ohydc29VDgRxMYSq4FvYBE6rVwAn64IPnqZZMWw9NkVc-RWUiFGLC-USgbuNZ9u2j9CbVxQPvhnp20PUSy4Yqma9dblKNr6HtIrQnQNrmws2KdHjv5GHku2mSB0UBUyP0qGzx0-dMlEC26aXPx7n_vLYJhJf_S9IjppQiaLauasbPKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
🆓
دسترسی رایگان 14 روزه به GPT 5.6 sol و Claude Sonnet 5
​سایت و ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده که به ۱۶ مدل برتر هوش مصنوعی مخصوص کدنویسی دسترسی دارین.
💵
😎
​
📌
مراحل دریافت:
1️⃣
وارد این
سایت
بشید و پلن پرو رو پیدا کنید و تیک Free trial رو بزنید
2️⃣
استارت رو بزنید و با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
3️⃣
از داشبورد برنامه Zed رو دانلود کنید ( برای اندروید در دسترس نیست ) و تمام!
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7429" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7428">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=GfKiYLsh8wQQE7xy_o2yOAGMcIKIkWK5F-J87KdtGflmAMZ0JqiQrRaafych9R8YOW95neFtYUNKN5-FA0wTIm181KpHHzaf8NWgCyuyhCURJAs5vm-9OffZnLF4txkhzL8bVP6_vUOuHm-KLBq8-H5u7stg4Wr5nXvSxyMEo2o1g2oHg7Pry8uBfIGjQU3ZuYWLz-9_W0k0Ba2g3WeRGN0I9T2y0D2RPPL7x53bNw5fDm8VtSwew5_pusfQIjPAjkB3C0p6FhSzvs3vkjUfrci2hfs1dbMxhQaWGQ-Og0CXhD0m7RufDtaS5xJ0_ninpS5qAIl4mvjoQLQKZ2kvdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=GfKiYLsh8wQQE7xy_o2yOAGMcIKIkWK5F-J87KdtGflmAMZ0JqiQrRaafych9R8YOW95neFtYUNKN5-FA0wTIm181KpHHzaf8NWgCyuyhCURJAs5vm-9OffZnLF4txkhzL8bVP6_vUOuHm-KLBq8-H5u7stg4Wr5nXvSxyMEo2o1g2oHg7Pry8uBfIGjQU3ZuYWLz-9_W0k0Ba2g3WeRGN0I9T2y0D2RPPL7x53bNw5fDm8VtSwew5_pusfQIjPAjkB3C0p6FhSzvs3vkjUfrci2hfs1dbMxhQaWGQ-Og0CXhD0m7RufDtaS5xJ0_ninpS5qAIl4mvjoQLQKZ2kvdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چت‌جی‌پی‌تی رسماً تبدیل به فتوشاپ شد!
🖌️
⚡
ادوبی یه پلاگین جدید منتشر کرده که ۷۵ تا از ابزارهای حرفه‌ای خودش مثل Photoshop، Premiere، Lightroom، Illustrator، Acrobat و InDesign رو مستقیم میاره داخل ChatGPT.
😺
🔥
کافیه توی تنظیمات چت‌جی‌پی‌تی پلاگین Adobe رو فعال کنید و با نوشتن Adobe@ توی چت، از تمام این ابزارها استفاده کنید.
✅
این قابلیت از امروز برای تمام کاربران در سراسر جهان فعال شده!
🌐
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7428" target="_blank">📅 12:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7426">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAtST9sezIxl8_9yHrwF0P7PORejyjd267MzNeicLMAr6GXDPin_-VDMNjrO8v74qtr7jePJy3bLgS1AFrrkiPNIDY_4hlHmPPl8crxxJlU5QOVstNMZMS0GVRtLqaDw6gy9T6aPvqH1CidGRIXz1828ZR20IcmjOH8ak-XUCbOaDBzQ-Y1fyl3vqlNRF7tfCISfIlC1EKqoSguwkkJlQ4cfVoRQgPT4zDRkOyh_efSydH_ALaz3WSLJ_Om36xBV8Lq49cdYfR7q3fIqQ3lf7nRAiM-aVmc0Mp_RY0-aAklCp1GLfrP9KL3tlYyjRUvbeqO2xRaQ9PkQ1k53mkk5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک ساز خفن گوگل
🆓
🎵
🩵
با این سایت میتونین با یه پرامپت موزیک و موزیک ویدئو های خفن بسازین و منتشر کنین.
با لینک زیر ثبت نام کنید و ۵۰۰ کردیت رایگان دریافت کنین:
🔗
FlowMusic
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7425">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔗
📥
دانلودیار؛ ربات تلگرامی دانلود از اینستاگرام و یوتیوب
فقط لینک پست، ریلز، Shorts یا ویدیوی یوتیوب رو بفرست و دانلودش کن
✅
🔹
دانلود پست و ریلز اینستاگرام
🔹
دانلود پست‌های چنداسلایدی
🔹
دانلود ویدیو و Shorts یوتیوب
🔹
انتخاب کیفیت دانلود
🔹
ساده، سریع و بدون دردسر
همین الان امتحانش کن
👇
@DownloadYaarBot</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7425" target="_blank">📅 22:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBp5k4mHa7GvqnIZlaDMzr_e7TarG1fcRY-q7a_n6SMhr5vOS-JDJJ5SGFxyyAf5plUqPPqygBpi2fr3sSaK7MuaNnu5FrdMViMEHnDRbQRZcxKX6aEJBFl1EIO0Zxx3XRjmnHqurVrAt8W5F57YbDDD_aEUHg_59EYJV_04ohBX0KK2ctGMacwSJ0TysFY5uFE0jBft9LNfO4uUiXCP-5CONiYSB0vNLkTU7TXKwWdNl4CJY81OWekdB8O1nvVRVnaJHmtVomyGeVpep8WBxIHeqUZbJ2eTllRG0JpHDcltDRCxPZgVxZ0EytazZnyIpqv7KhGTPLiLl10W9X9QyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1500 کریدیت برای دسترسی رایگان به برترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.5 | Sonnet 5 | Gemini 3.5 | Haiku 4.5 | Gemini 3.1 flash lite | Nano banana pro | Nano banana 2 | Nano banana 2 lite | Gemini Omni flash
✅
1500 کریدیت برابر با 15 دلار برای 7 روز
💵
🗓
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7424" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByVTLHUpm-Ybwt6oNYfFXVyPXetndKpf51XkpN0XsOffI9ZvazqDfAaAEgZrRabtYWDIrlp9059Ayu6K6bwIaB-U52zptNN6IW0NL7o0g55nbXBysv2GozD6V8n6NEOC8Ykapw0NmjnmyTX41FZm0qH4T_QhipTw7wLmgv7ivzu-NmwNQsSIBqCtSw1lRplYwXGbLTaQ4E7gOTuTuRXmyGi7ycWly3nnbFt9F3fWjT_-upe5QYt0BBqxstwAs9URqECZ4ijJdDsKjAxE5QPvNH6yqKrlDLm5SNEZvUPdIyqyijm7E89kwpzlrnirTVE3exeMSnVu15PGIqTFQzpvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به Kimi K3 و Qwen 3.8 Max
❤️‍🔥
🆓
بدون نیاز به کارت اعتباری کافیه وارد
app.clusy.io
بشید، با ایمیل ثبت‌نام کنید و توی پروژه جدید مدل مورد نظرتون رو انتخاب و استفاده کنید.
😎
⭕️
فقط ۲ روز از این فرصت باقی مونده! به دلیل ترافیک بالا ممکن هست سرعت سایت کمی کند باشه
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETQ0m9WqJu703PNRXxASCvaEH4g0scMUrAM1DLp_sDnkq0DWsExfyiHUb-e93NLPfU2z6UCkN-QCvHNQ5S7aGh2h-NSin8tlPcz_yhaICFgVr6ldp2r8ejwFOUjbfQIQ3sp0D36-WIcckF5vwSaZj_jmBXx7a0UJGmsphE9jPf0I18pZUsPWnu72TtvRt5AyomInVXy1qRTRA5aRLZ-xLjKz11efYJvwQebRCYXYUFMry0v1tdHUDPX_QfeeFVB5vmFTKYQ2j3uEpBkiuMOzIRQVu6Ml7b8NhhZWvdutmSATcubeyJwIsgtN-5Wb1mNu-NGm8_id5F-O3KYniXwlZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان:
امروز از ساعت 12:30 تا 20:30 به وقت ایران
⭕️
🛠️
مراحل راه‌اندازی سریع:
1️⃣
وارد
سایت
شده و با اکانت Google ورود کنید.
2️⃣
به بخش Account رفته و اکانت خودتون رو از طریق تلگرام فعال (Verify) کنید.
3️⃣
به بخش API Keys برید، یک کلید جدید بسازید و اون رو کپی کنید.
4️⃣
برنامه OpenCode (یا محیط دلخواهتون) رو باز کرده و اطلاعات زیر رو تنظیم کنید:
🔺
Base URL:
https://api.aigate.shop/v1
🔺
Model:
muse-spark-1.2
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQwYM0w69wCjdrbdQzxs-PCwcKfYjfFW7dBnZqAZ8Hq--OVQ5iQCt3B0T600b3Ao_7LxZ_M2NF7J-ohUFJE5-Sy_6WVth8-M6AxGOPsJe4wX19gKb0tFc2dzzPTowvEu3LIUfvBkdPAexfqQGpRMPq9S5Fzq_kx_Z92pmWlu1Not0OpIVNRWZqPz032OWmTckVm3Yu1N4k92eJbedSwd-xLbmuv4jtkHriH9BQ9x-Ww4SufokAyySmAqviWZC8V8rwIGgrV3-5UVA7lyeVbawnNZWgmF1GJWfl1AJIwoBtry9THpEleU3WQI9BNoT04v4twDKV2t2byaHKq6rWuMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ‌سیک V4 Flash
به‌صورت
نامحدود
و
رایگان
تا
پایان
سال
6️⃣
2️⃣
0️⃣
2️⃣
به آدرس
cnb.cool
مراجعه کنید
➡️
هر
ریپازیتوری
که خواستین را باز کنید
➡️
عبارت
@codebuddy
را تایپ کنید
➡️
حالت
Work for me
را فعال کنید
➡️
تسک
مورد نظر را وارد کرده و اجرا کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebFaKEnvDv6vpyhD1GqAGuBW8WU0_Dp0rl2rgV93xdI5GJ9PF824P8zda_cAp6d9j5PSzg6rPCW8yhsHfOKq5YK9DMC41qaDVyp7w2_I436G74g1zv_qOQ_syoYHLsG5ZPXdk6zpz__ngjFNyVfHjfFwkUI5-6SdPDDM6PZbg32jsleU__hJDHsdPEHI80ipEPaFQYLsvA2BWp0vtHwkW-CYWcct-wN9v_qn9a6xFAh9gFJUh9idCybEYgUTRGHMqjCOUYVgiONXRF87Q2ZVF5Dmvgjl1Mx5EX6GPtEuhtK6CNCt6CjodGCXupnLky39SZB03P6fpqzeDQYr3VVC9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کامنت یه کاربر زیر پست تلگرام در ایکس:
من آدرس مخفیگاه پاول دروف رو می‌خوام
😕
💯
اکانت رسمی تلگرام:
مخفیگاه رو که نمی‌دونم ولی من رو می‌تونی تو خونه پیش مامانت پیدا کنی!
🙈
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsbRVXXtXStL5_DPybFwoxO5uUrR3ZBNC9NVY0mLRLxp_UQci046KDqgttId08FBo2xlLAtu8aM6d59D4t1fQ5RUL-RJU6TJAcKqtPhy4ePBGi-56EOMY64hhvlHFzfgBL3ljuicb8Gf9BhnEpWh0YaDRZlcFzzlD-lC9Gvgy92Ce6snTqUTuDaiWuut1EFV7No2yimm-GH0iSZMSZ6GTSQpfMLvpHim7fkJOf58kmrf282aoHP-dAehH5GKf2o-mtXp_kIYl1dXB2v4pAkBNXdwXBgYg3_AabuEf202kWsCyCjEMpm_xGYhHNNGIF8asbo675GijQ46VSj08uh3gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف فوری واترمارک تصاویر و ویدیوهای Gemini
🚀
🔥
دیگه نگران علامت روی عکس و ویدیوهای جمینای نباش؛ با این ابزار رایگان خیلی راحت حذفش کن
❌
😎
✨
ویژگی‌های کلیدی :
1️⃣
100% لوکال و حفظ کامل حریم خصوصی (بدون ارسال به سرور)
📶
💯
2️⃣
پشتیبانی از عکس و ویدیو با کیفیت های 720p و 1080p
🎞
3️⃣
کاملاً رایگان، سریع و بدون نیاز به نصب
🆓
⛓
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgq3lquD6SBl8ZBB_cyRXhi-Z3HMyoVRPwxaUj6e_0PAMohViyWmqLYjNfYIENHZzDq4oScUFGghyEU9Ev-OElc_w-5cgZv5o4K7_2taTh_PqXHjvIegdm9L1WIUOoEtnZTwOUwGHscXw4ijw_H5co7M9N_gWAq3evDawuMCfEe7ic2SPqNKvPotCnfVecW_UK5YLhQ2yTMQm-uvyIRZsCdtg8ATwH9h3XrZMIispO9D4QsIxCK89VUt9UztwN5xK-_Vm54cJATYuriN9e01LwHP1N1C88nT8xAtcHv9HkmR5_kgN-p4FEG4cGZ5luSNzUKHUaaxjyUCukiWKvvFRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت
Dola
مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت روزانه و رایگان
🔺
کیفیت و قدرت بالا در خلق ویدیو
🔺
استفاده آسان و آنلاین
🔗
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1iArd7d4RUdX4tUJY4DnanTTKEcMPVIHcPqwVI4Q6tZYSYL89QRopAKPE3o2vBGu0fD8qG904fRAmMmU3RswSVbBFZDyspajIhNDqDM0SKaugvgoZnbApoZOZ05FfXo4cf6n52zwyCjphR0c_WvKG4-tfD1ZpZlQPD2VftHe1d0wIV0rFRRIFxOTdbtdUiQ0cA8FcNf5-c99gx24zDJAFxmO5Gq4bhtCZ7p1O1B4NARjw6on8ZbYYwWAeVbs9b3BKCabzmdixRv3fyb98-RRBJswmPuUd1PCxqDM05fyMhsvfAMsIP-R4Poc3h1U0JwWNGbPkOg2fEAYxG6xg-Ybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
گنجینه API‌ های رایگان هوش مصنوعی
🆓
یک مرجع کامل برای پیدا کردن API‌ های رایگان مدل‌های زبانی (LLM) بدون جستجوی طولانی
🔍
✨
🗂️
1️⃣
freellm.net
بیش از 424 مدل رایگان از +30 ارائه‌دهنده با اطلاعات کامل شامل محدودیت‌ها
📉
📊
2️⃣
freellm.sh
لیستی ساده و سریع از سرویس‌های رایگان با نمایش وضعیت و محدودیت هر API
⚡️
🚀
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdVTiPHbae1A7re_L4H1G2GvDiUA6pq9O8cHENDW41w-YyqEoShvpayQz27dbb1mH2e_hB2H_7vT3sefTZeRBl1A11NOnRFyJyAxTQ8h9BAejdr1l6P8AUWvQv7jt8KGDzfVG0EsAmlgfk2ZPqnm6lm9pmQIv51DZH5FHODF1uZKlPzpZlQODllLcQDBHXjTv9smEdf6QnJDD_0VOQlm6Iv0bRyygW7gy71YLAwA94lss9b0Y31xFa9EAq2M0R-oVotMKCAyY93k_134aGEUbF9aOyz9cUWfzfHfHdzkRK1gnNeEEXoiCDI1GNEw3Ngi9PdBfYJLWyftR7b0N_reCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمینای اسپارک (Gemini Spark)؛ دستیار هوشمند و همیشه‌فعال گوگل
♊️
🔍
بچه‌ها گوگل با «جمینای اسپارک» رسماً داره هوش مصنوعی رو از یه چت‌بات ساده به یه «ایجنت عمل‌گرا» تبدیل می‌کنه! این دستیار کارهای روزمره و گردش‌های کاری شما رو به صورت خودکار پیش می‌بره.
✨
قابلیت‌های خفن اسپارک:
📄
اجرای ساختاریافته:
اهداف شما رو در قالب وظیفه (Task)، زمان‌بندی (Schedule) و مهارت (Skill) دسته‌بندی و اجرا می‌کنه (پشتیبانی از اجرای همزمان ۱۵ وظیفه).
🌐
وب‌گردی خودکار:
می‌تونه کنترل کروم رو به دست بگیره و پروسه‌هایی مثل جستجو تو سایت‌ها یا رزرو رو کاملاً خودش انجام بده!
😨
مدیریت ورک‌اسپیس:
خوندن و ویرایش فایل‌های Docs و Sheets، زمان‌بندی تقویم و مدیریت کامل ایمیل‌ها.
💻
کنترل مک از گوشی:
اگه اپلیکیشن جمینای روی مک نصب باشه، می‌تونید از راه دور (با گوشی) فایل‌های سیستمتون رو بررسی کنید.
🤒
شرایط و محدودیت‌های نسخه بتا:
❤️
فقط برای مشترکین پولی (Google AI Pro و Ultra) با اکانت شخصی (بالای ۱۸ سال) فعاله.
🔛
ویژگی Keep Activity اکانت باید روشن باشه.
❗️
فعلاً از زبان فارسی پشتیبانی نمی‌کنه و تو بعضی مناطق (مثل اروپا و بریتانیا) در دسترس نیست.
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBEIXTLz04XlIXQV4WlYHCb7fU2ato3_mmJQz4pMWFlNhKZvJzrte2N0Kn8kaBnURFtVTCoJIQ8MfSqoJJm07R7sSUwd1fjOWCuIcr3lEYwU-CGDBXxsIwZ2hKHeK7l3rKqoZc0olsa4j_zQSKc0CUTHCqQ1ndAUqycREP9_qKLUsmvNyGFCtrdrXUzh1AUYmdT9U9fL3ZY3_7bLljZVKsh2JXX7QDZkZBhp3PcZV5eqTFr6lHwtdnmA9i7hRhbtAw2AdnsuQFy22jxR8BC7uI-1ETGKmPOBWd-l9Pxg_Z-PtBhl4X0NfqDTK-fH78cli4-vC516IbZLcZkdCnRPrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌اندازی سرور اسپیدتست شخصی با OpenSpeedTest
🚀
🌐
〰️
بچه‌ها اگه سرور/VPS دارید، ادمین شبکه هستید، یا کلاً می‌خواد سرعت واقعی کانفیگ‌ها و سرورهای خودتون رو بدون وابستگی به سایت‌های عمومی تست کنید، ابزار
OpenSpeedTest
دقیقاً همون چیزیه که دنبالشید!
🚀
این پروژه یه ابزار متن‌باز و بی‌نهایت سبکه (حجم اسکریپتش کمتر از ۸ کیلوبایته!) که با جاوا اسکریپت خالص و HTML5 نوشته شده و بدون نیاز به هیچ دیتابیس یا فریم‌ورک سنگینی، سرعت آپلود، دانلود و پینگ رو اندازه می‌گیره.
📶
👩‍💻
👩‍💻
✨
چرا این ابزار خیلی خفنه؟
🔺
اجرا روی همه دستگاه‌ها
✅
🔺
نصب بی‌دردسر
✅
🔺
تست فشار (Stress Test)
🔤
🔺
بدون ردگیری
🔞
💡
کاربردش کجاست؟
برای تست سرعت واقعی ارتباط بین دو تا سرور، عیب‌یابی کندی شبکه وای‌فای خونه (LAN)، یا تست کردن افت سرعت موقع استفاده از تانل‌ها و پروکسی‌ها.
📌
👩‍💻
لینک مخزن گیت‌هاب و آموزش نصب
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔥
یه
پلاگین
به اسم
oh-my-hermes
برای
Hermes Agent
معرفی شده
🏥
این
پلاگین
سعی کرده چند
قابلیت
مختلف رو توی یک جا جمع کنه تا نیاز به نصب چندین
پلاگین
جداگانه
کمتر
بشه
✅
😍
از جمله امکاناتش می‌شه به اینا اشاره کرد:
✔️
هماهنگی کدنویسی و مهارت‌های codemode
✔️
سیستم مصاحبه هدف و پرامپتینگ برای برنامه‌ریزی و مهندسی حلقه (ulw-plan، ulw-goal و Loop Engineering)
✔️
معماری حافظه پیشرفته (شامل Dreaming، Pruning و مدیریت کانتکست)
✔️
سیستم حافظه لایه‌ای (بلندمدت و لایه‌های L0 تا L3)
✔️
متخصص‌های دامنه‌ای و قابلیت‌های تحقیقاتی
⚡️
تنظیمات آماده‌ای هم برای استفاده
سبک و سنگین
داره که می‌شه فیچرها رو
روشن
و
خاموش
کرد
GitHub
🐙
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JU3n6-hNMPLNL8Nc0w7HWf6f3-oclIaEv-BBBiMmNoFZkE0UGZLehno6FwB21RpW-tCFwNqzi86gzkAW29VvU_wVHksVnnylUEnYxMfscZWsxYqUxzckXwB3733INklVeWWgKZjF-JOJ8WwdDE30F0V5lLy9Zl-PRdht2Re8fYD5OZdxisJMUR7Fr-v8QB2Gs6ypIcsWxjRgu5djye8AfvnqtCFWRrpUFP1W7u_f92zPcs2k2rwgK5hBrXVnoGbZv0OoG3CteCrw-OAMIWEBp9yK6f9aI4DxFFaeG5TXdla6u4Qqd_M3-gF3DOT74JzaWYsuWStK8dBBENlKaaQmnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱ میلیارد توکن رایگان  تا ۱۲ آگوست
🚀
🆓
پلتفرم
InferX
یک کمپین محدود راه‌اندازی کرده و تا
۱۲ آگوست
امکان استفاده
رایگان
از برخی
مدل‌های هوش مصنوعی
را فراهم کرده است
💥
از جمله مدل‌های این طرح:
😐
DeepSeek V4 Flash
😐
Gemma 4 31B IT FP8
😐
Qwen 3.6 35B A3B FP8
و چند مدل دیگر
😍
طبق پنل سرویس، برخی از این مدل‌ها با هزینه
صفر دلار ($0)
برای ورودی و خروجی قابل استفاده هستند و می‌توانید آن‌ها را از طریق
API
سازگار با
OpenAI
در ابزارهایی مانند
OpenWebUI
،
OpenCode
،
KiloCode
،
Dify
،
Hermes Agent
و سایر پروژه‌ها به کار بگیرید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gT9_VBelnxBD1SA3k2XppAB6uq3cXMBHTs_sQTy_vm0mSUeqBf_y0fFY_k7GpPSg6q2TPv3bq298iM4a4Amu-s5QG2O23s2Ql3oiU69Rnu_NsJkqLWgxxL-iuwqAzpxY1A27EebIFfQdC8_s4BH8CLibQWMU7bQA0x_Ijp1SOh5qtVxvoihFYnAIOoiReMpkWPPAc9g_z88_AngIjw5NMNqm1Y__SoemSkwFEyoMeA33Zh8IFCOhtyBFu5aUUXipON0aE4vQ8p9BSX0P1LWEzUCsXMfH1TOEsj9fjuCkYpHYK9fhgdjYtOhP0OqSgNIVtzEKPAfqCFaF0A2bofLOxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی CloudSSH؛ ترمینال قدرتمند Web SSH بر بستر کلادفلر
🎶
📱
پروژه متن‌باز
CloudSSH
یه ابزار Serverless و فوق‌العاده برای اتصال و مدیریت مستقیم سرورها از طریق مرورگره. این پروژه با استفاده از TCP Sockets در Cloudflare Workers، یه تجربه کم‌تاخیر و سریع از اتصال SSH رو ارائه می‌ده!
✨
خلاصه‌ای از ویژگی‌های جذاب:
🔒
کاملاً مستقل و امن:
پیاده‌سازی خالص SSH 2.0 با TypeScript (بدون نیاز به کتابخونه واسط) همراه با رمزنگاری اطلاعاتِ اتصال در مرورگر.
👆
رابط کاربری حرفه‌ای:
ترمینال سریع بر پایه (xterm.js + WebGL) با پشتیبانی از تب‌های همزمان (Multi-tab) و تم‌های متنوع.
📁
مدیریت فایل (SFTP):
رابط گرافیکی کامل برای آپلود، دانلود و مدیریت فایل‌ها با کشیدن و رها کردن (Drag & Drop).
☁️
همگام‌سازی ابری:
پشتیبانی از ورود با اکانت گیت‌هاب (OAuth) برای ذخیره امن کانفیگ سرورها.
🤷‍♂️
دستیار هوش مصنوعی:
پشتیبانی از API مدل‌های OpenAI برای کمک به تحلیل لاگ‌ها و اجرای دستورات لینوکسی (مثل Docker و systemctl).
🐙
لینک مخزن پروژه در گیت‌هاب
🌐
نسخه دموی آنلاین
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_4ihX8FpknEOkDetNhHs9qI9WvAZe1extBuLgkCGo9kSCgI8OG69Scx9tzf5CCgxs5z44ncLC77GJWUVEsT45qsufOAIITwAqcWHmIud2VbWXZql_NNTkTZXr1Hcsvu0E2SKnLF4RDabM-5WJGd8qyEmOhaw6A7rLF-MuMx6fTC8Bf09Df26sszyAaByK0_gMUtN44rxAFf2nw1rYudbV8nA-dXNU-D4vGNJntDUKkOzddh75O0m_KSQ4I_0cylUcyukBreazBOj54sLKcGEmVbC0qByCX3y5ZHgxTe3hkAjhgCDICM4DGl2RqHIUsk016dUcIndOAIL5a3EsE4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=MUVDdaKmW-e86VotkXD6H9569tBRvFYbFhz9DeL_iUnk2oRSDAwyZHQk5SP67Bbw0ITBZMuy37CZWmX_Zje4AEo_44bcJPrhoQzT3OfmnLQVeVrX-fiMDO6jJzN5KVA3Hu4Q_VNdo9JAiPzqHr-nkNWIR_sPLznAmpz5L--jKdTPibIJsNJvnpaZUTBMYWiXrqG9R1jqIxSfemm1TBSGB6ZY0VTJIlP4x-5YukJhsAmLl1YRwqK731iCAy6Tuqhn7-uY5RFJCCB3WZ9D_kgbI8ifxJ9pGwsVMEn_Z_fVkWYsVZ6NHZUuhsiM6CaS60QSw3w47raAC3aZS0NyykjnSHYCzhGUEbzw7x6zQfmx9UhwYnTF8lcanyakzPFlUFudK78eiQB0Nc41HhoY5fadDuftTUmYRvQpGlciK6PUh9DQlWfnthfuZjyxiAC-Un6cqhKT6nu2jLr1P_nmUHn6f4Ygqz11yE7iJNAiozhO4cEQXJ4oWcROH7yZlq1zG8gHS1AhFgbZDCY_p1sxm_03u2gy-wcT9JjkA1tGrI3eBZ0ZRVxmcNnC0ZKrx2V3nknacZiK7ZjFkH715ZGgea6uk6LXNHcZKfKIXI6_u2TX2wUWfrAh82kvqnVZe4s8yQVn3CWvLWnHVesh-aqAR0pdIscU9hAgbgJ4mLGKLGWtlgo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=MUVDdaKmW-e86VotkXD6H9569tBRvFYbFhz9DeL_iUnk2oRSDAwyZHQk5SP67Bbw0ITBZMuy37CZWmX_Zje4AEo_44bcJPrhoQzT3OfmnLQVeVrX-fiMDO6jJzN5KVA3Hu4Q_VNdo9JAiPzqHr-nkNWIR_sPLznAmpz5L--jKdTPibIJsNJvnpaZUTBMYWiXrqG9R1jqIxSfemm1TBSGB6ZY0VTJIlP4x-5YukJhsAmLl1YRwqK731iCAy6Tuqhn7-uY5RFJCCB3WZ9D_kgbI8ifxJ9pGwsVMEn_Z_fVkWYsVZ6NHZUuhsiM6CaS60QSw3w47raAC3aZS0NyykjnSHYCzhGUEbzw7x6zQfmx9UhwYnTF8lcanyakzPFlUFudK78eiQB0Nc41HhoY5fadDuftTUmYRvQpGlciK6PUh9DQlWfnthfuZjyxiAC-Un6cqhKT6nu2jLr1P_nmUHn6f4Ygqz11yE7iJNAiozhO4cEQXJ4oWcROH7yZlq1zG8gHS1AhFgbZDCY_p1sxm_03u2gy-wcT9JjkA1tGrI3eBZ0ZRVxmcNnC0ZKrx2V3nknacZiK7ZjFkH715ZGgea6uk6LXNHcZKfKIXI6_u2TX2wUWfrAh82kvqnVZe4s8yQVn3CWvLWnHVesh-aqAR0pdIscU9hAgbgJ4mLGKLGWtlgo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8CSl2TJhwFlPCT5ybKOwxVBGEFBgiwy9BwktINIz4eScbzRmYY22OHWZY_W3qAXwAtK7geNMhzLmramMFPT78lnlbUg2JpSnhIODLNJ13JBqn5JXoeaD7HBVPrLq2I-dxsD13-LzEBe__E2beWob8JGw1kBFJ7vFohz4MtTykuX1i8F6w3-squbcY_7um9j9-Npq8IOLAFs4IZ7mCixb6W4abFT-R1QY1nlMkbf1cOU5VK8JhTUMvr589TfWy0D9poL0TnKqioBJCjAVeH_aDG2El6DQI-WgUqD_rg0mM2GwWFpmic7Cryx9HmTjNtIyxINEmsaWXfZQI1vvqf89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
500 دلار اعتبار رایگان API برای شما!
‏همین حالا کلید اختصاصی را دریافت کنید و از مدل‌های Opus 5 و Opus 4.8 لذت ببرید:
🚀
Api keys:
sk-2UddB27hnFA1z2LKWKnq6BQaffBLe86FU0htxAHm0Q9n5vjW
Base url:
https://agentrouter.org
Model:
claude-opus-5
|
claude-opus-4-8
✨
کلاینت های مجاز :
🔺
‌Claude Code⁩ | ‌VS Code⁩ | ‌OpenCode⁩ | ‌Hermes⁩ Agent | Qwen Code | Kilo Code | Cline | Roo Code | Open Claw
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J__wj83LK6lQ35KaxUYiS5Ig8hO6Tw7wgzNzDm7ErpBqmIDQj-gOVgLsOaNIDfi58SX3-7NCyEB4yxhXyGAv6q_Z9Ej4O0C6boRYOp-wrigGbOULR7Qr6Ss4h20nsFtL93-5jaQPRi_xAxtivPPvayxCyMyJ1RDzITxVZbi9bKcbgTLAZkcAPr-EJHNsQ1GW_fpYKuYKxw70P2sjwjQ6V8U9TX0gEhhIiTM0bGDOvzSSEPg2yAIYiHIIEJte-rHJHSkTe_QoBMpSYNsy2nhe-Wi5k8Yqn8XWX4dpSENn8sy5xHRmIgTpeOBj_6ATqodQvrGrshsutgdMUmbD4CaacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آموزش تبدیل کردن صفحه چت سایت Qwen به API
🚀
اگر در موبایل هستید از
Kiwi Browser
استفاده کنید
‼️
✨
آموزش اجرا :
وارد سایت
chat.qwen.ai
بشید و یک حساب بسازید
در سیستم کلید F12 رو بزنید تا Developer mode واستون باز بشه
در اندروید از سه نقطه بالا سمت راست از منو گزینه Developer tools رو بزنید
وارد تب Application بشید و گزینه Local Storage رو پیدا کنید حالا کنار این گزینه یه مثلث هست بزنید روش و سایت qwen رو انتخاب کنید
یک جدول باز میشه و آخراش یه متغیر هست به نام Token اون فیلد روبروش کپی کنید یا توی کنسول این دستور رو بزنید خودکار کپی میشه
copy(localStorage.getItem('token'))
اینی که کپی کردید در اصل api keys هست ، ممکنه بعد چند روز منقضی بشه و دوباره باید بگیرید ، تمام حالا میتونید توی هر جایی که دوست دارید استفاده کنید
Base url:
https://qwen.aikit.club/v1
Model
:
qwen3.8-max
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBjOKzcHg56rqA4m9uqFxDD7Sme2cqCtyG9TlBpJyGcQbf5dhbPD_-AobJQ9t3zuiVKZMXsfwTQYKaDgyBIec8pfOhQEg-D7Wi5DQOoifJE8oz1y3kv0McIXRkflXmmuio3KtR2Cu1PKPVN7dXd1dqVG7hBFgHB6RUmsKjhWrvfe93d4Sk-EPMXV_kCsfakoEmr8O5X3uEcPtT1AC7DmH48w-7VfMOVoqB7k_oBAcOzATW1NJlRRjCnIsvBY5_uyFgoTqpYRsXud1rfHSkRSiVFk8fdd7P3Fqdtu-BNZNXNCG14i4FuMN6dRAE6sJLIQDbQHovCErYCcxiAuDG-1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩
‏وارد سایت ‌
Cline⁩
بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند
این سایت
‏حالا توی ترمینال، ‌Cline CLI⁩ رو نصب کنید:
‌npm i -g cline⁩
‏با دستور ‌
cline⁩
اجرا و لاگین کنید و لذت ببرید!
💻
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7394">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url: https://www.fastaitoken.com/v1  Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471  Model: claude-opus-5 Model: claude-fable-5  دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7393">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url:
https://www.fastaitoken.com/v1
Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471
Model: claude-opus-5
Model: claude-fable-5
دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7392">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro
همچنین دارای چند مدل رایگان
:
GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3
به
این سایت
برید یک حساب بسازید و با تلگرام وریفای کنید و لذت ببرید
✨
قابل استفاده در
Vega Agent
✅
📍
Base url:
https://anymodel.org/v1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIWNOTryUh7FokqtcbsdZuQ1ZE0RPTGVuffqyb-7Kupj0WkIt8teqE1M6DkWnXwqgR2w3yT3JugMbhlQc2yCB2G9_OdVjLLfDVpcFuwyXaQgUJREO-6xn00NAp8Da-B2LNfDZ82VNUf4jgHOCeJRCkfIubWkAcuoPDpzpav1_h9F0BSft2VQPRfyE_RWy1u6YO-KGoUvYQpnlOq_fk0FQyJC7Nt9uqEebeLXmqfVC4bkWmuL9i8UEykUuI1hdZHioB6u0OGIBVvjoNl-IFgpG7EYHc3vlz8McP3k84Yr3gTbau67SAS9SNbZ-4Mh7lfbIwawN2CVoLoXutGn02elGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏100 کریدیت روزانه برای حرفه‌ای‌ترین مدل‌های ساخت عکس و ویدیو!
🎨
🎥
‏بدون دردسر و کاملاً رایگان؛ فقط کافیه وارد سایت بشی و با کلیک روی پروفایل بالا سمت راست، اکانت خودت رو بسازی و از قابلیت‌های بی‌نظیرش استفاده کنی.
📧
✨
🔗
‌
https://www.creen.ai
⁩
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7389">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaRxyrycVJdc7mg8xHTlCdUxlQ04midvBv2v6DFdLv-PjXDaLKBLnFKkUSnJFyF8P4wJuYditMWAnm8uNl1ybemDEBnJ89T_MflkESR-y0KmCXFXQgYplnEsAeFz2fjmmedvis3lo7aL_DLUqk0scOl6UaaOCyetMvHF3Cec45EYcAgftMtqoU1_AoEAIgDLKpDZZOND_KsrmhftC-RSYgA-meOxghintBUnXe4u2r3XGw6EjIw6AJkQ-F7FQjpWPcmG0qg9IEjU0c8odrgRjBiGJFiKGm5mJtU5-drh2S-h1_efZol1pi4oPHQ9oj44cFAkt9jTcjlQVKMv5BphAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دسترسی رایگان به Canva Business
🔥
از طریق
لینک دعوت
به تیم، وارد شوید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7389" target="_blank">📅 12:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7388">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آیپی تمیز کلودفلر
92.53.191.134
66.225.252.96
104.18.14.224
104.25.247.228
104.17.2.54
176.124.223.242
104.16.122.178
188.244.122.16
104.20.14.15
185.148.104.192
104.24.152.74
104.18.2.152
104.27.24.70
154.211.8.196
104.17.88.93
74.49.214.92
195.85.23.208
172.67.114.81
92.53.188.13
104.18.198.203
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7388" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K19woTx_WJnqPzibuhVoDebJsYYmYvZ4HOOWGD3WT-0PMJtJyeNQD_3t-UvnhdkTFjC36KU7lvjj0nfOun5dr0jAafC0rECtcfYvw26YlQB6N_ob9V2BM7yABUKd1n0ZBxUEV44M333ndk1vSrx56C4cVHQWZmXCon_gPAjY2wf2XEvmgmlaTrmtOIy8o5Bu-PB4r8Ji8LKtzfiy6mec2kOEa2-axs2C1iSbNXqSx_Pr9aa5Qg053IlbRZMtpE2k0EtWvYDFpMixMiRHUaERiLmtY0AYDyVCAu1W1XHnfyRVXsznJM5LXTIp0khaqwrwsUrI5v6-iKYbuGxQcAqntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تولید محتوای بصری بدون محدودیت!
‏دیگر نگران محدودیت‌های اعتباری یا کارت‌های بانکی نباشید. با این ابزار قدرتمند، می‌توانید بی‌نهایت عکس باکیفیت و ویدیوهای ۵ ثانیه‌ای جذاب خلق کنید.
🎨
‏
🔺
تولید نامحدود ویدیوهای ۵ ثانیه‌ای
‏
🔺
خروجی عکس با کیفیت بالا
‏
🔺
بدون نیاز به کارت بانکی و پرداخت
‏
🔺
رابط کاربری ساده و بدون محدودیت‌
🔗
https://zsky.ai/create
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7385">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2uDAFBZ4uaNC9SwKuaP8gcOELyncfvwrviq4vPpERqvTgJ7I729mzfCfDaipbBdMs9_LLmx4ORe5qk2B-He5Uy9DSXzcLIz727b0DaHuM1zDaTtG9ABihYBZ-Y6DkXULUIpLP6cOIN9wqkQtw2z1LSEoVXPe762Ldam5iDWytyyxt4Sl9Imkb9oUD97FnRR2F4EpdO987jBHV3jCuXk6G6rMos7TQM7WeTkbFlG9eZMbgyiM8x0LmqR5TdwINF9UXY9k6LTLicIfB3FvIMZzXbzH5DG9OvgeT6D195r-QSEtS1Q5wlfCbwM6kq7s7l3gwEU2oHOM4vu9hc-dVCWAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
200 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 5 | Sonnet 5 | Deepseek 4 flash 0731 | Grok 4.5 | GLM 5.2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://seekai.cc/v1
قابل استفاده در
Vega Agent
☑️
از این
بخش
هر روز 20 دلار بگیرید
☑️
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
200 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7385" target="_blank">📅 18:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7384">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjpHlL5UwS8G86CxyD8GBkvuJSqvmb-2_WgA_1gVe6jp-u3AcGGjE5cnbmBnBk-JhPGSF12ETZ9sRyroHruLg0NNVAy47rsA8Rzo2MBUkEoFy7saBeYgmViFtNL0UqHs4WKA4QtiEleEcJ5YYPe19C7sK0QmA5u0NGydMNq69bKtC29HU1OQ6UOz7zdgKjy276ZG7nRdFti5BBn0-KzhNpKJzJaVLzYQwH0ZXVmyyXRcZit51k2i8cUo9i4LnrXZoH1f9Tc7kXvv1AzMUrLq1_pPiW8HhlpsGE7zzME7q0aOmkoep-mz7Go_TeB4IlruJLn4K6MdZ8Q29Vf-4UpiFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
دانلود و پخش آنلاین موسیقی با فرمت FLAC
🔗
http://1music.cc/
😀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7384" target="_blank">📅 18:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7381">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوستان اپلود کی ضعیفه رو ایرانسل بهم پیام بده پیوی
اگه حوصله تست دارین پیام بدین</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7381" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7380">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipMDEV6sTwfdFFVHSz6YJmdTz_YL_Aa7QaoVICoK8qDLilWhIjPqMjm6ODwNTDvOwKntnvy7xbhm-K4mrudSqdpY7PvMa4Wejn0cQG-D9epVW_MY2Lz3VJJQ5xZQHgpzEMgsyRPSdsbRyyKoFm2dKHqD-I7o4yyZGbYnJtmd3VlWPs89cDfEpIIru5Rs51WfuYN29f_ovLw0rQ0tlm0BucifgCQhA_TaSHALxMFLxg-MCWv0p0bVSHqyDM3T78gCd-CwB5kOVUyY9_hdzpbfyhjMJZ5RR39wsDf6t_9YWksGr6g8Vk3u9-lu_Y1pX8soFHhkPjgZmmWaubhCo9iT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی رایگان به مدل قدرتمند ‌Qwen 3.8 max
🚀
‏اگر برای پروژه‌هایتان به یک ‌API⁩ پرسرعت و رایگان نیاز دارید، همین حالا دست‌به‌کار شوید:
‏
1⃣
در این
سایت
با جیمیل ثبت‌نام کنید
2⃣
‏ از این
بخش
با اکانت تلگرام وریفای کنید
3⃣
‏ دریافت ‌API Key⁩s
📍
‌Base URL⁩:
https://api.aigate.shop/v1
‏
⚠️
توجه:
این دسترسی فقط تا ساعت ۲۱:۳۰ امروز فعال است.
⏳
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7380" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7379">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHXsbx0Glh14aePFOAwKuZ4cO63C_mvR5W2r-dQSneiA7XY4mI7L1HxryRETwk-vNoBFeh5mbNvPZ5um6Pah5r6xn6LVJnN0kviHC-QXyuZMTZuTeSPOz4isMEsGNtBYAwXL4WNR27aAACeBzwOkIpaX1tAbaUyKhqBSQdcGuO5wFwwx8ALtFTXKaB46wLckGlfeFnKZDqiFF3YyE4MRZa_ryS3ja5E_QVZk2tQ8CACofNZfxRCeEzVWnEFjVnujdenC1A9-USB2kqB8mo4xbK2YYm1-T9uki-nG4PCmbQEloojxzouFTC_iJUFwYrdI4rrSS3GTFnnELmQzAUW28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
30 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 4.8 | Sonnet 5 | Gemini 3.1 pro | Grok 4 | Nano banana 2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب ( قدمت حداقل 14 روز ) داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://routllm.pro/v1
قابل استفاده در
Vega Agent
☑️
🎁
با هر رفرال شما
5 دلار
و شخص دریافت کننده
30 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7379" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7378">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=n8xSwkGo1F0jvFfC3iHrRVvZEMaJiaI0H1TSqCU8XpNc8rBai9FCoRwLVwr2Xkr9-KIDJOcWhyPuyr4GfLHxG6lcEinUY0sBJUlj1DTFHoNyGdG2zwt26VXDgsXfbaCr8DsT5kSISn9CQdCevgK4a4fhOEqfSfXYzYVwlQhcMV9PapeTzOgrN2U5iDd7PUgEpDICnqWo-0QPxr1lk7Sm8QrGbC_ujTpupokq8UUgWBvQ_YkB4k2PumnynAlxiy3hI9seeMH3fw7Gl1yWRyYQi5YCinEBY4dbSPCIYcWhImJqfT4fkYxmx7Mx48pg9JBRCIfH4jWRgsXXDnpV-fur6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=n8xSwkGo1F0jvFfC3iHrRVvZEMaJiaI0H1TSqCU8XpNc8rBai9FCoRwLVwr2Xkr9-KIDJOcWhyPuyr4GfLHxG6lcEinUY0sBJUlj1DTFHoNyGdG2zwt26VXDgsXfbaCr8DsT5kSISn9CQdCevgK4a4fhOEqfSfXYzYVwlQhcMV9PapeTzOgrN2U5iDd7PUgEpDICnqWo-0QPxr1lk7Sm8QrGbC_ujTpupokq8UUgWBvQ_YkB4k2PumnynAlxiy3hI9seeMH3fw7Gl1yWRyYQi5YCinEBY4dbSPCIYcWhImJqfT4fkYxmx7Mx48pg9JBRCIfH4jWRgsXXDnpV-fur6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
تبدیل هوشمند وب‌سایت به پرامپتِ حرفه‌ای!
🚀
‏دیگه لازم نیست با کپی کردنِ تبلیغات و بخش‌های اضافیِ سایت، وقتِ هوش مصنوعی رو بگیری. این افزونه، محتوای هر صفحه رو به یک متنِ تمیز و استانداردِ ‌Markdown⁩ تبدیل می‌کنه تا دقیق‌ترین پاسخ‌ها رو از ‌ChatGPT⁩، ‌Claude⁩ و ‌Gemini⁩ بگیری.
⚡️
‏
🔹
حذفِ آنیِ تبلیغات و المان‌های غیرضروری
‏
🔹
تبدیلِ ساختاریافته به فرمتِ ‌Markdown⁩
‏
🔹
سازگاریِ کامل با تمامیِ مدل‌های هوش مصنوعی
‏
🔹
افزایشِ چشمگیرِ دقت و کیفیتِ تحلیلِ داده‌ها
🔗
GitHub
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7378" target="_blank">📅 15:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7372">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">NekoBoxPlus-1.4.2-83-arm64-v8a.apk</div>
  <div class="tg-doc-extra">42.2 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📦
پروفایل پشتیبان NekoBox+
با توجه به
شرایط فعلی
،
اختلالات پیش‌آمده و قطعی بسیاری از کانفیگ‌ها و VPNها،
با این روش می‌توانید به
مجموعه‌ای
از
کانفیگ‌ها
با
پروتکل‌های
مختلف دسترسی داشته باشید و در صورت
قطعی
، گزینه‌های دیگری برای
اتصال
در اختیار داشته باشید
☑️
🔹
روش استفاده:
1️⃣
ابتدا برنامه
NekoBox+
را نصب کنید
2️⃣
فایل
JSON
را دانلود کرده و
Save
کنید
3️⃣
وارد
NekoBox+
شوید و از منوی
☰
به مسیر
Tools → Backup → Import File
بروید
4️⃣
فایل
JSON
را انتخاب کنید
✅
تمام
.
تنظیمات
و
پروفایل‌ها
به‌صورت
خودکار
به برنامه اضافه می‌شوند و می‌توانید از
کانفیگ‌های
موجود استفاده کنید
📌
این پروفایل شامل ۱۴۰ اشتراک و گروه با کانفیگ‌های متنوع است
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7372" target="_blank">📅 12:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7371">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=AGZnTvmVPd_qrCwkhOOxIEw3T_t9RNNPkHpWMSbglP4QE-GooZDtfV5ZFo2tEYy_dNjy7jcFbn3nFYbqWuapzMFIoCGBovAMdudiN9qvTftXEU5OTx4hlTejR759DI3mFPHGpYf3kVdw0nkC4uPpRA6hm8iuI4lcSC9l8WA1evscRQtrv62kUsIbkng8e7wNHlf1N7EAR_wPvU0ABStyLuQrsiVLm6IkZOeWAiEVvDHLcFyYYi1cOQPbLX3dDTmCjKtmvAHF4w3DF0r7nN2UGLoFaXlkHvT28qs_Y7mmtBJ_no7vPkTpgsd8W-0NjZQ__9cOuvszjC52E5HYC5B89g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=AGZnTvmVPd_qrCwkhOOxIEw3T_t9RNNPkHpWMSbglP4QE-GooZDtfV5ZFo2tEYy_dNjy7jcFbn3nFYbqWuapzMFIoCGBovAMdudiN9qvTftXEU5OTx4hlTejR759DI3mFPHGpYf3kVdw0nkC4uPpRA6hm8iuI4lcSC9l8WA1evscRQtrv62kUsIbkng8e7wNHlf1N7EAR_wPvU0ABStyLuQrsiVLm6IkZOeWAiEVvDHLcFyYYi1cOQPbLX3dDTmCjKtmvAHF4w3DF0r7nN2UGLoFaXlkHvT28qs_Y7mmtBJ_no7vPkTpgsd8W-0NjZQ__9cOuvszjC52E5HYC5B89g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
کپی‌برداری از پروژه‌های گیت‌هاب با قدرت هوش مصنوعی!
🚀
‏تا حالا شده بخوای یه پروژه خفن رو از گیت‌هاب درک کنی یا مشابهش رو بسازی، ولی غرق در پیچیدگی کدها بشی؟ این ابزار جدید، کل ساختار مخزن رو به یک «پروپوزالِ اجرایی» تبدیل می‌کنه تا بتونی با کمک هوش مصنوعی، اون رو بازسازی یا تحلیل کنی.
🤖
💡
‏
🔹
آنالیز هوشمند:
بررسی دقیق ساختار و معماری کلی پروژه.
‏
🔹
مهندسی معکوس:
استخراج منطق اصلی و اجزای حیاتی کد.
‏
🔹
تولید پرامپت دقیق:
ساخت دستورالعمل‌های گام‌به‌گام برای بازتولید عملکرد پروژه.
‏
🔹
شتاب‌دهنده توسعه:
ایده‌آل برای یادگیری سریع، پروتوتایپینگ و درک پروژه‌های سنگین.
🔗
https://www.gitreverse.com
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7371" target="_blank">📅 12:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7370">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ربات تکه‌تکه کردن و آپلود فایل‌های حجیم در تلگرام (بدون دیتابیس!)
🤖
📦
یه سورس
ربات تلگرامی
فوق‌العاده جالب و خلاقانه براتون آوردم که روی بستر کلادفلر ورکرز (Cloudflare Workers) اجرا می‌شه و وظیفه‌اش اینه که فایل‌های حجیم رو از طریق لینک مستقیم بگیره، به پارت‌های کوچیک‌تر تقسیم کنه و بفرسته تو چت تلگرام!
✨
ویژگی شاهکار این سورس:
این ربات کاملاً Stateless (بدون حالت) طراحی شده؛ یعنی برای کار کردن به
هیچ دیتابیس، KV یا فضای ذخیره‌سازی ابری
نیاز نداره!
🤯
شاید بپرسید پس چطوری می‌فهمه تا کجای فایل رو آپلود کرده؟ ربات خیلی هوشمندانه تمام اطلاعات (مثل آفست بایت‌های آپلودشده) رو توی خود متن پیام‌ها و دکمه‌های شیشه‌ای تلگرام (مقدار
callback_data
) ذخیره می‌کنه و از خود تلگرام به عنوان دیتابیسش استفاده می‌کنه!
🔹
قابلیت‌های اصلی:
*   تقسیم خودکار فایل‌ها به پارت‌های ۴۸ مگابایتی (برای رد کردن محدودیت ۵۰ مگابایتی آپلود ربات‌های تلگرام).
*   امکان ادامه فرآیند آپلود در صورت خطا یا قطعی (کافیه دوباره روی دکمه همون پارت کلیک کنید تا فقط همون تیکه دوباره دانلود و آپلود بشه).
*   بدون نیاز به سرور یا هاست (قابل اجرای کاملاً رایگان روی کلادفلر ورکرز).
*   اعتبارسنجی خودکار لینک و حجم فایل در هر بار کلیک کاربر.
سورس
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7369">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j01cPkOkb3InLb7XQ2MU1pVYvlYTG3hrN4ZxuWeMwrukTHPZRTjH10RrlbYpeAiLEVe8ZKd9VniQuPWNkC9Zqnc51TxsBANPh63xRC3iqwOToYQmLnSEjrV5ZV1n9VTpyIi0thShOVQBkq2Rg_bKDE8SwDxadjxOr3DbmyZp1ZEKfmfc9ywozWu4f3lmMweKgVK-MnnwgHPEdk6s3oMpRltqoVTRtqoW3M-mUDnf7ONU7EBdF2IjqsysWAhX9qFl-teGZVxfkbulbdQ8bge6UcFCLmzh8ria4VfhfH3tkXSZso30m7w9D20fPlj9GpjiIIwzHKRKeRMvdbmdN5u2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک های Qwen3.8-Max
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7369" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7368">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2F8ep4ekMBWXa362yN3rhGFCPnjgQvT-OaNL4UddZuy8xpPX0EJwVO-6BoA1PY0297EF-Iz8gyJPUC-As8nm_3wAF_Dfv0UI47l9Fa13d9GYPYJG48oRMUUk0Ndojz1GD4T0AL-RNbUH48481pPrNV-_0oI-qmos0h8r87_tJG5q241zCQ7tzQmg6SNbmd-w83D2JVREFbNdEpvXzD6Rs2cNdP17CrwI_Pynn7xuyA8QRdlO2EicGk0-s5HVnWgyyVRJDXc65-OVLBdn727iFX9PQtXcTIruerAX8R0rUw_0-x8UEsHZsek7Rro8EXKIOZ04opvJe2aGflWZZDlgK5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2F8ep4ekMBWXa362yN3rhGFCPnjgQvT-OaNL4UddZuy8xpPX0EJwVO-6BoA1PY0297EF-Iz8gyJPUC-As8nm_3wAF_Dfv0UI47l9Fa13d9GYPYJG48oRMUUk0Ndojz1GD4T0AL-RNbUH48481pPrNV-_0oI-qmos0h8r87_tJG5q241zCQ7tzQmg6SNbmd-w83D2JVREFbNdEpvXzD6Rs2cNdP17CrwI_Pynn7xuyA8QRdlO2EicGk0-s5HVnWgyyVRJDXc65-OVLBdn727iFX9PQtXcTIruerAX8R0rUw_0-x8UEsHZsek7Rro8EXKIOZ04opvJe2aGflWZZDlgK5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم Qwen مدل
Qwen3.8-Max
را معرفی کرد، بزرگترین و پیشرفته‌ترین مدل خود تا به امروز، با ۲.۴ تریلیون پارامتر.
تغییر اصلی در این مدل، توانایی کارکرد مستقل برای مدت طولانی است. این مدل قادر است یک پوشه خالی را بردارد و یک پروژه کد کامل را تا مرحله تولید، بدون دخالت انسانی، پیاده‌سازی کند. علاوه بر این، این مدل می‌تواند وظایف طولانی‌مدت که نیازمند برنامه‌ریزی هستند را مدیریت کند و از بازخورد بصری برای تصحیح خود در زمان واقعی، در حین کار، استفاده می‌کند.
هفته آینده، این مدل به همراه یک نسخه سبک‌تر (27B) به صورت متن باز برای عموم منتشر خواهد شد. برای کاربرانی که از API استفاده می‌کنند، هزینه پردازش ورودی ۲ دلار به ازای هر میلیون توکن و هزینه خروجی ۶ دلار به ازای هر میلیون توکن است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7368" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7367">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">window $🪟.npvt</div>
  <div class="tg-doc-extra">3.6 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7367" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرعتش از اون یکی کمتره اما بستگی به موقعیت مکانیتون داره از بخش configs پینگ نگیرید.
🇰🇿
-
🇫🇷
-
🇩🇪
pass :
@ArchiveTell
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7367" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7365">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">window🪟.npvt</div>
  <div class="tg-doc-extra">4 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر vpn ای که داشتید یکم ضعیف شده و الان به زور وصل شدید
این سرور موقتی میتونید استفاده بکنید تا استیبل شدن سرورای خودتون
pass :
@ArchiveTell
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7365" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7364">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axxalmcRAivTQghfvXI9hpfbv7Sb3ztb_jvsmYnwXXPDKK8pncExZAneJt9nShZEFolvLTZctrSNG7us8_O-e4YvNjVbtRO_GZ1xEwCncm2d4xBNki47TELVekEsY_kF0mWKj4QoTt3HNicMk8WtEYVCFoFOcWr94qKOkR1jQigmLV99QoWvcN5Jq3X4gC-djdWjMVeH7eLYeI6nm1n2GwwfSv26n7ltPPmU6V3ZfwjVpAuDMrxLMjGpGAtOOm2LgmZ6yCpCy2cQY0U2kjv5x6bbj8F0jwKtShYXMMMb7mfxo2zJDgeya_Hd4fVo-6TvldypSarBKqwqDAIRZzQbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از DeepSeek Flash جدید هم پشتیبانی می‌کنه و طبق چیزی که دیدم، تا ۵۵ سشن رایگان در اختیار کاربر می‌ذاره. منم باهاش تست کردم و واقعاً سشنش خیلی خوب جواب داد و هنوز به محدودیتش نخوردم
✅
حتی GPT-5.6 هم بین مدل‌هاش هست
😺
👩‍💻
نصب نسخه CLI : npm i -g freebuff…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7364" target="_blank">📅 22:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7363">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏
فرار از زندان برای ‌Gemini 3.5 Flash Lite⁩
🔓
‏
⚠️
نکته:
حتماً با جیمیل فیک تست کنید، خطر مسدود شدن اکانت وجود داره.
‏
برای دریافت پرامپت کلیک کنید
✅
🔗
لینک گفتگو جیلبریک شده
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7363" target="_blank">📅 21:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7362">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7362" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7361">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7361" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7360">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGDIRHGZXp417l3rzP9MNjVF2t6Z1wvBNVCgMbJwidxu98Tb-BoJjO__SWwc5Wa7pBcQ8fWwZfP5Dlq6GAVhmBBuVRj4iBj5XwJe_eSGPqocN02RUXerk33wFsqNc1nU0m7yhlQTzKUG638BNPVn_UaGZXytEWMfGlBYDBDnCgVoJZf3dh5xOBNbUGlC63axy_MoJN0fvDMd35dy0CicFL3e07FPws-CdW24-okBU3XdpecI5diWEJnHZM_Y4lmKUBRfQORdOyINg1wUoyz4uFD8Epa3gWhyrI2B5RCLfoBUZGu07qw6WIvuagAsaxR-1gVOasCb0TPS0u6a8zx0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوبِ بدون تبلیغ و ردیابی با Invidious
📺
🚀
اگه دنبال یه جایگزین خفن و سبک برای یوتیوب هستید که نه تبلیغات رو اعصاب داشته باشه و نه گوگل بتونه رفتارتون رو ردیابی کنه،
Invidious
خوراکتونه!
🔹
پخش ویدیو تو پس‌زمینه (حالت فقط صدا)، امکان سابسکرایب کانال‌ها بدون نیاز به اکانت جیمیل، و محیط فوق‌العاده سبک.
✅
اصلاً نیازی به نصب اپلیکیشن نداره! فقط کافیه برید تو سایت
invidious.io
و یکی از سرورهای عمومی رو انتخاب کنید تا مستقیم به دیتابیس یوتیوب وصل بشید.
📌
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7360" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7359">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ow1KATvjzWPoZow0MNGuRwWcMcJiOp2gfz6jsN2cATdz_TFeVz5x1RPv_Y4CCjk2eUuAdl0CmbPEi3132savQQ192Q2Lr3LvR974ASuaYG9TXiwumfFLumzEM5jlHiMMoUP4528_LOi9rsbp8NnuFOY9ZD92KxqcW7yWCO2dI8XrWgkOBpp5x0yBjrfNIQM39tUoB3uNkmNBKrQU9QecED_DcAUUuOo_dAaW6887RQ3EkNYSGw0IWGvZ4OhYt13hlazLX4NON2Ph9ay3pszC44NhLS3yxGbO1XsYkyIgrY5gfxSQes5V0upO9pm1-NtgsMkdksilHMTYRqR0LwN4pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 2900 کریدیت رایگان برای بهترین مدل های هوش مصنوعی
🚀
Fable 5 | GPT 5.6 sol | Sonnet 5 | GLM 5.2
آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7359" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7358">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یکی از اون متد باحالامون نشه ؟
😁</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7358" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7357">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها: •
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه •
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان •
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب •
📝
فقط پرامپت بنویسید…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7357" target="_blank">📅 13:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7356">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFbf8zp2gJQl4Bc6wKjnL-seUYcjJUWuGpYRygaqbu2I6ZEs8VQAhZiI35ZAxvkjS4zEHvjXCQkY7CZ92z7Zi_WRa5eZfZD56_ZD6ADoLy5_PVfZSrRRk5AqmojcdYOs7VQ8J6s7U2qI35ChOPo4DD6jm0MIsNn2hfQNkBKZTry6Tj1lU9v2jKF1I-vFhGav9W4bpK2gMywiXG6Ox_I8g6PPk4YFYVhFnxB97FANTOF7b1JbPXPcNfcIdswKaGndwAMiwZfzq8d9V6NrE3lRsScWkuKk9Zcg95D0ZIl64JmmGi21HXMoxBpS1RDvgFFzUUBXBtrGkRcQjkQpBYwcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پز نیست
سبک زندگیمه
🗿
جهت دریافت کانفیگ پرسرعت بر بستر کلودفلر عدد ۱ رو کامنت کنین
😎
😂
(شوخی)
متوجه مشکل آپلود شدم و کلی چیزای دیگ
ایشالا رونمایی میشه فردا بصورت کاملا رایگان</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7356" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7355">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBTU1PZZxl-mW3h7RQyAKKa6VMUe1ck4AliGD8XttX6_EczRPiYApu5YZE6sKdQsrJAbPELXMszli_kP6srHpcKk-22bhCwcbHtdNqdqQ4nEWUDZq93GTVDjlYlWC56ZdoZLGlCbRcDpY3Rj5RTHCt--A_S0lwwLbArfGg6gUeO--IgQ8_rNPSAFdvfnLLNiqseFZpuBIlMCV7jKs5aAtegpbrvD2f_4pzeuxoBdRHU4UTRX0hqT0pRXWO6GelWBiZMAI_Ld6YrvGFRyljqWkRfQPbjgOpul69XKhSdkmv4uYkiZ6wj1T75S0OasVRc_RsJ42ACfRbt-HgNDCD7gsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
فرصت طلایی: ساخت ویدیو با هوش مصنوعی گوگل
🔥
‏گوگل تا تاریخ ۱۴ مرداد ۱۴۰۵، امکان ساخت ۱۰ ویدیو با کیفیت بالا رو برای همه فراهم کرده
🎥
‏
✨
ویژگی‌های کلیدی:
‏
🔹
تولید هوشمند:
تبدیل متن به ویدیو در چند ثانیه.
‏
🔹
ویرایش منعطف:
امکان تغییر و اصلاح ویدیوهای ساخته‌شده.
‏
🔹
قابلیت ‌Remix⁩:
بازسازی و تغییر سبک ویدیوهای موجود.
‏
🔹
رابط کاربری ساده:
دسترسی راحت از طریق منوی ‌Tools⁩ در ‌Gemini⁩.
‏
⏳
زمان محدود:
فقط تا ۴ آگوست ۲۰۲۶ (۱۴ مرداد) فرصت دارید از این قابلیت استفاده کنید.
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7355" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7354">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIDtVL7R8WyOfyd8wTuloDfYl_DboGCBVccjLNPCF5D0UA7M1YYr1K08XuQoG0at1-4Ql4u6Q_67KFqik1uRBCYMIRDbwSUIACLTGWk5Ry7zUc_uaX1P54fnTYK9X_cJirQPMVvStgS6jsc-mopyoE7bDubbxYA_H97si4OnHmaxS9kTBVUHHEYk-kihM-eDVPAzdYvKATpZv3siykJP43mVXd5AkE1ch1YW4nl9KqzCbYlyqmnGs6IXqcsGlbCaP2StCdicgDf8FutncmmMDLahafW5AUKq6uftgttQLYXCoIk96PfQ2swrHiXRTPGTALkZdepZag2V28OLkQt1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API مدل Deepseek 4 flash 0731 به صورت رایگان
🚀
وارد این
سایت
بشید و یک حساب بسازید سپس به این
بخش
بروید و یک کلید بسازید
✨
محدودیت:
هر ۵ ساعت ۵۰۰ ریکوئست
‼️
قابل استفاده در
Vega Agent
☑️
Base url:
https://api.p0.systems/api/agents/v1
Model:
deepseek-v4-flash-073
1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7354" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7353">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wB7GsAz2jFqfJdS0t7NVpGM1evPqEvd6QLqDpah0NGm3D6KXDKNl1AR00t_EZwrrETdNgmMX_PQq9xS3DdembI10l_SJtfd5Zle6q4oRRPKDmXQaWJ8o27dcb7o9J-fUZu8D3H2UwHr4OBlcQIAkFE4d-zOvrc-LNIYWhEQplYjw92MoU8plaF76dkSJsQgUP8lbXGjdzvOJ2No10AluwFGTPDk_j2NgUHiFL7TTVOS1AVxQQoS65omOvgc0a0YHsxUbjtcqW2QHO-bAHoXrf8eFXkyKZEYKWuemhIiAudHHFC2X8bPVnLeJ5zuW01fk96svSM5P4lSFEp-uNBLLSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر خودکار و مداوم IP در لینوکس با IP Changer
🔄
🛡️
اگه برای کارهایی مثل تست نفوذ، دور زدن محدودیت‌ها یا وب‌اسکریپینگ (Web Scraping) نیاز دارید که آی‌پی شما به‌صورت خودکار و مداوم عوض بشه، پروژه متن‌باز
ip-changer
ابزار فوق‌العاده کاربردی و ساده‌ای برای لینوکسه.
✨
ویژگی‌های این ابزار:
🔹
تغییر خودکار آی‌پی:
تو بازه‌های زمانی که خودتون براش مشخص می‌کنید، IP سیستم رو از طریق شبکه امن Tor تغییر می‌ده (Rotate می‌کنه).
🔹
سازگاری بالا:
روی اکثر توزیع‌های معروف لینوکس (مثل کالی لینوکس، اوبونتو، آرچ، دبیان، فدورا و پاروت) به‌خوبی کار می‌کنه.
🔹
دو حالت اجرا:
می‌تونید بدون نصب و فقط با اجرای اسکریپت ازش استفاده کنید، یا اینکه با نصبش (توسط فایل setup) اون رو تبدیل به یه سرویس پس‌زمینه کنید تا همیشه فعال باشه.
⚠️
نکات مهم:
* برای اجرای این اسکریپت باید پکیج‌های
tor
،
curl
،
xxd
و
fq
روی سیستم نصب باشن.
* از اونجایی که ترافیک از شبکه Tor عبور می‌کنه، ممکنه سرعت اینترنت کمی افت کنه و بعضی سایت‌ها آی‌پی‌های خروجی تور رو مسدود کرده باشن.
📌
لینک مخزن گیت‌هاب و آموزش نصب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7353" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7352">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCJmiVzOkQbz2aY2CgnhSh-KTWf6CZykpA9xJ9QUFdWeceGQwbGGrW1Jbqzf2c3iUNyq3qotbG2xIBEaW1m-Ook37rl8mVmz6L2oLzkBWo4aZg0g9-qDfgKSYxFCiOD2O46bVaPbkaAgX8ezduXvVvDlWn7W1khDwYWBEDbfwlAE6Lu3BdBBJaaZem6hHTeDIg_AHnUAF6IU5MtDTZ_UPsYUtQZBJ2o6OnvjQJtH68VwgkKmJEZ4Wo128hLLcc9gBfjigF5-eRwUr1nl4z-4qRPFLynCjnnfpI6TGXryjCSphjNIz07fKaYb6sU-4Wh6lQRglcfr2G3ePIC99ERp9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Deepseek 4 flash تا 12 آگوست رایگان شد
🚀
میتوانید کلید مدل رو از این
سایت
دریافت کنید تا
12
آگوست بدونه هیچ محدودیتی قابل استفاده هست
⚡️
قابل استفاده در
Vega Agent
☑️
Base url:
https://model.inferx.net/endpoints/v1
Model :
deepseek-v4-flash
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7352" target="_blank">📅 17:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7351">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoIByiL2SsqiEVROZPkYQ13n-VXy9q76FyzPHBCQiE7pGpLcF2abTJ88vcWoV_82Fj7mq0L7-PPTCpkE5rsaZqALOH1SE4-GtdX7z2JG2KO0P0YeHUBvEwVz2mJayjmnoReZFIVGNLObPua0qOO0o0LW9Ocf2qZ8nrfUmsrU8j-6zXxe7e5RjFNXz6OVmrUijnM4ZZk7J71250zWCxwnb4CZeAEKVBZYx0fz3P5LkIoHa6slrni2YEkzAj6tiqZXMu0Wu-Iw2wTCQYKZJwJ1fiPBQBQVsyZGhGTQemrz-ZP7QGYAyATye4-nUgev2qm3BzZhbR9QBUDKvIrz2K4MNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان
Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این
لینک
وارد شید و سپس لینک ربات تلگرامی ایی که میده رو استارت بزنید برای وریفای
✅
5
دلار اعتبار برای مدل های پولی
☑️
قابل استفاده در
Vega Agent
☑️
روزانه
5
میلیون توکن رایگان
☑️
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7351" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7350">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ArchiveTel
pinned «
بالاخره ایجنت هوش مصنوعی خودمون رو برای اندروید ساختیم!
🤖
📱
بچه‌ها، یه مدت بود داشتیم روی یه ابزار خفن کار می‌کردیم و حالا Vega Agent رو به‌صورت اوپن‌سورس منتشر کردیم! این برنامه یه دستیار هوشمند و همه‌کاره است که با معماری Local-first طراحیش کردیم (یعنی هیچ…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7350" target="_blank">📅 14:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7349">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpNqbsQfQ0l7z2_k9LrZEQjzVCXZTkgNLbxFkjDckGPb0i2yJ195Oue_5lCvX6IaW8obC7mP-wel7hOj2DMj8TxE1VuUL0FT3LygpR7YfOuMf_k8vLFPrA5n92JO109MzF5P7KDuygA-JXg3CeMQR1OvdbjtPbDkWH6RP4vf8ljy3wbtNoSiyD4Kr_QX8SGgtCFbpSA2SY2wFiiR-xsxBc-PesjZhtsITkIXLW5cVkBUx9gdpjI0i4qQHkxLGE8k8VSkwWGY_1CWrq0fq5U0-ZmsGaZnexDc5WOOyDHhAr5rEL3LQomkB_zunjb61Z0GXGutPe9RMAP9QUh_p7M-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 8000 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7349" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7348">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5   برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این لینک وارد شید
✅
…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7348" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7347">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_mpN_C8um2WVTZhVf0oMfUMUGhdJ9IujkvVS0PNjiahrPKdc_Z8Es5lcxhGav3onLgqpYYGELlllsxOVrVcky1H8qmUm_gKb667zvAUWhaZforAjm-RnEn0bH25s2-bCzL_gCytwdqcbQzR_jnboa4ctgzoY81rdYIQ4Bn52wJCpWh6l2B1KHU5wY2NvTd56TG_Q9hWgF8OIU5aLxh22TpJjLGZZwVRH1nLXJC_60cCcyYJleyxCoG3D3iwTCt0Itqh4q7W4ur4fB-I_r3lv8rjAr4MVlFzds3iUEArKNQ-0GIOSKkMkfqoCZ7mfmGgXWwFl1OslXKVOaFjCa2Bog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این
لینک
وارد شید
✅
قابل استفاده در
Vega Agent
☑️
روزانه بین
5
تا
50
دلار اعتبار هدیه
☑️
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
50 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7347" target="_blank">📅 12:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7346">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWs2veM857M3Oc4VKa_jneD-u9iUr_CihUVl_BXq86Q-d9hgo8pbrPtmBUv7tkTjAgVzhG46x7ex_7HqIpbgNg5SUMKfeCIMTofTjQrDchRxKG35VOIaxd7JtLpYcJtzS3SSMwphhX5aRQwKKWDqC1DQpAK7NDxd4hTYzh2ZT-ml3y5m1UbcPdI--dB4eMDBbcEnCNPM_cSiv9k36Vl7w1bxBMNfHhkw6uh2hGir33LiHu0ZQ2UjNZrTOs4V5b1f2WfhqN83d8VkMt6ePChygnia9MnhwKWmxSAhs1eM0HSRx85uTjvLxVvAlG8TMY9w-dCL2MhaP0NzXbZEibVTnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 1200 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7346" target="_blank">📅 10:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7344">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eD6egei49cZvtkbpQO4jirlRr7RiHhKZbqeUGm0sgmnh4kT6yo0Jaq07WQfXpurj6QpE8K9AMg0fTP6hdudGyM6JMK4TKnRNxabwm0hbqOuVLHTzh0yU8uwGRdA2G2OXsIdRVVbTy2sDZDAPR7B2n4M0CRZCt-HzayNmdmzTx-AF8BHzY8ypsC069j7SBc-z6hjDNu_TtggV1CXYUIl8Gk5N5QH4wmONoocuh4kGAyyi0Xbe9j4bNrw0GHm56KaLP8SJazDop86_o7V_G2FfBYK-Pje_BjlKAPvhtPfIAQEVl8aJ6_OsY34dcFVsW5J9NSjiE9qZEnw2M_JA9QX0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F83m8esDiV-Nd2ko3sJ0Y9HVpi7OguoZ7nA5SP3nRJCJMudHRrGhVZsMCgVVmRyhZ9-FhDELHLPvjMUWU5JJCW8QpvBr5tq-YtgLRN-IxApI1amWwtG8O3rEMsTxH8Uo5eN3OJWGOlL-DPuHiC7Ps9j_RwR8CTP2qy1y_gofxtbKsOBi5U3zgRuc10cZL0itT_NJpHgekO6pI2kp0uQRbienby2Ihs93W3XylsNgyLfBokDenk-tQQkZuCDSsMexzIN1px1PrCn9XWay6ExGRim5iPAdg-Z9VzvEnuUqfTERam_ntJe5PTvFsH4BuIVzw7vXCBqCCjej2MTt16kMUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7344" target="_blank">📅 23:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7343">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7343" target="_blank">📅 23:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7338">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lBpQc54aihZTP0D2vxqbzAE-xwgSYrRyMmas7wsF-PcqJEikx7wJrNavKvr4ejmnqhTJ767Ib52l0yx7r_sOmIj2pdAb2zIBZxTGE0QMePv2hQG6rhn-SSnAwePjxKLfGnnfGpYLprDbAEaKtks7eDL2LadeNcTSFBxQfVgFWg9vhrJ-2ESrUtTmNJpUhEO8_sE7nPcix2xACoS_AidB8Rm8IeRjcilpXT1Dyx5VkAfIkuFLGqBtsuxfXontHgP-FT7eD_ARYBFFV9jUF6aZ2dvNgR-RRh90kO3r-4TVVxvp3k606eJCl26xCvg5Y2qK437_zNatSS0uktQTgYKEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5FVAFbV8snhvUd7dGk7rSA1W3m2h6xenix2E0FxLoA-K-r7b-ZbT9FUSYKcK01ZarqOUZA1HHOMC-ug0nny7bIvw-DqKXEkZVhN7DuGk7TTkRCnt2tNbltrI4c1k5nGygGlfisJs3IBa3Qrvh3wtnqs05BHniFGkh25GX3AWPAzCdvACFv2YgNy6laoyxYYua5VIRYMdllGgkySZGTAn6QBshY3rHAaOiaR9XR4XXZLtduoz-lkJ0rQyUm1SXEwYH7BlRyHtrjYefmoOv3bqjFJ4gzFRR6M62x9qgWiI-CB6uUGlf_vtsS4haqG27gzc__GcaT88GVfw3P7CRXMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zm0ec06WEHZxdtE_qO3wy6XlNSVjezKaylGrr2jrtWME09shh9Em8EkR6gagDI9skR3VoL-USaBJaTVfYIizACWr1y48_FPN6tTPPneFEOOYVx8rLlLwqAL1whSGIoiMdaZHn_cSgciNVtTlZ2zJMktnRHdb8b_d4hKyi2mShsrYDVGGoJ3ykv0LOW1hVKwmu029AWFIZK6xpXTIr6jx70dk6o_5oY-h8_SBLckeNBHX7kQDCWuR6Sr9zRCn0l-ktwdn77n7ARuZshWQKqplEiQ1ZDZOexXV0ntiqWPND5ADKnFPm6KsojViSHE03BOr50KLM9yZ_Vjmo5EaX_hvEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuDBXAnrktv2LfSpuCHQ2i-uPCIWzmLJfGdg0FQcKoT4Ii8OM3VP5q8uBXVypy8HcMo6KUW8izi5u07qleE2IngoR58BO1sXPPhnGkNaVEmnrAU2VbvwZhW5DAtUwb6Q2EWGSTryErNBTkrpaG6CEkJriXCr6ayqKuaMDTPS59FQmFBpjsoJNvPloE72fK9rqW3_3pPEmZJ1kXYDnUgjYuTXwVBqhu4Yf-KqB7gwP_H6-2TdcvlSxzjOzYFHlfdJuz6QR5GMol82ipvKDs83ace1-iIVs2KNej5eVtpX-PKUTTxnuSEGUmLxHvpB8Z56MMAGjzQZjoSGM1oX_TiffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_L1Jk4z-wGXw_AbyGkuqh5ovRWl8gZOLTxkDvS-M6H1Kisn_5k4Je1qOFOzBk7vf-mNcO4vpg1pdr5OzfH0c2lHRiVh4gF-ouyHhiwoohw3-3mK2HSEnG6ouyMcCOEJdQLhwzuGFN7D1_89QIfk3hUXzrmGeNBm4bkvozsW_XB_9nv64Do5wtOnUTYDnyNJXPq1Brg7MWUPUN5nTsemW1O_NXTL2M6JDkjgYyRquYyToecyKa0EAgvMJSwV9Klf6QoMFiuFTiCHmvW9pcKzESMpXy2sZoJQypvUfy6pQWgF7E1f2E4O2BluHPKxNLhT0VrjbvffGfW_XIJ6HX45gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7338" target="_blank">📅 21:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7337">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">بالاخره ایجنت هوش مصنوعی خودمون رو برای اندروید ساختیم!
🤖
📱
بچه‌ها، یه مدت بود داشتیم روی یه ابزار خفن کار می‌کردیم و حالا
Vega Agent
رو به‌صورت اوپن‌سورس منتشر کردیم! این برنامه یه دستیار هوشمند و همه‌کاره است که با معماری Local-first طراحیش کردیم (یعنی هیچ سرور واسطی این وسط نیست) و مستقیماً با کلید API شخصی خودتون (BYOK) کار می‌کنه.
✨
چه کارهایی براتون انجام می‌ده؟
🔹
پشتیبانی از همه مدل‌های معروف:
از OpenAI، Claude و Gemini گرفته تا OpenRouter و حتی سرویس‌های لوکال مثل Ollama.
🔹
مدیریت مستقیم فایل‌ها:
بهش دسترسی بدید تا فایل متنی بسازه، کدها رو ویرایش کنه، PDFها رو بخونه یا فایل‌های زیپ رو استخراج کنه.
🔹
۳ حالت اجرای هوشمند:
برای اینکه کنترل کامل روی تغییرات داشته باشید، می‌تونید روی حالت‌های خودکار (Automatic)، برنامه‌ریزی (Planning) یا تأیید مرحله‌ای (Accepting) تنظیمش کنید.
🔹
مرور و جستجو در وب:
خودش تو اینترنت سرچ می‌کنه و محتوای سایت‌ها رو برای تحقیق و استخراج اطلاعات می‌خونه.
🔹
امنیت بالا:
کلیدهای API رو با الگوریتم AES-256-GCM رمزنگاری کردیم و کاملاً امن روی خود گوشی ذخیره می‌شن.
📥
فایل نصب (APK) و سورس‌کدش رو تو گیت‌هاب قرار دادم. نصب کنید، تستش کنید و اگه خوشتون اومد حتماً با دادن ستاره (
⭐
) به مخزن ازمون حمایت کنید!
📌
لینک دانلود آخرین نسخه از گیت‌هاب
@VegaEnter
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7337" target="_blank">📅 21:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7334">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بالا باشین بچه ها عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7334" target="_blank">📅 21:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7333">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بالا باشین بچه ها
عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7333" target="_blank">📅 21:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7331">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqmMamsIepLPXjJRzwoW7fqSLf4fIkqkTjwx5gBnpunxwB1iEex51TuSSiORPVsavhjRVo_uDvJNMJN5KB07rewOLmETfu6nKo89cU_6WRzwC8ChQPihVKvfaY1GJZkcE4Ffol2AGvFYb5knUSV3IOwhFJuzG2d3dhzOzMayOiwQXUo0LgS47L-r5LAqhyhQOlp_d-IcbuktuXHfYUxXaKcqm-sD4PAHuJjVgAE9heL8w6fhZvQlKgGoVYSBLfpBCkfKBccWqQa4lrXofIMd5NgWY9Gp9GYj_uHFxZkUnLoxEOM5pwOBgzArWe-75WGPpHdn_6xegtbjuRnDinziww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت ویدیوهای حرفه‌ای با هوش مصنوعی، اونم رایگان!
🎬
✨
بچه‌ها با وب‌سایت
Dola
می‌تونید روزانه ۴ تا ۶ ویدیو باکیفیت رو با مدل قدرتمند
Seedance 2
تولید کنید. علاوه بر ویدیو، این سایت ابزارهای چت و ساخت عکس هم در اختیارتون می‌ذاره.
🎨
✨
ویژگی‌های کاربردی:
🔹
تولید ویدیوهای حداکثر ۱۰ ثانیه‌ای.
🔹
امکان دریافت خروجی در ابعاد و سایزهای مختلف.
🔹
کیفیت تصویر بسیار بالا به کمک مدل Seedance 2.
🔹
دارای ابزار ساخت عکس‌های خلاقانه و چت‌بات هوشمند.
🔹
سهمیه رایگان تولید ۴ الی ۶ ویدیو در هر روز.
⚠️
نکته مهم:
برای باز کردن و استفاده از این سایت، حتماً باید از VPN با
لوکیشن اروپا
استفاده کنید.
🔗
ورود به سایت Dola
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7331" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7330">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTF28QbKRlj5MInCwllBCr1bHUKakbgt7b5rmqxF0BJ5Z61h2ArnHm_eexZLJ3XwX2350FZXCgIhZH9pqFl1gnJcylSXbtkMeI6hD1Nn0t-vsuwRrwkekf88Ij1ix43xqHLx4M5oXtDy2OIkt_KY8pReLxpvY1EHAw-kQMWY4u4Jj30WPnss8sPn0sbUXkSup5SmiQNjBK7koEqlkSTPwWu-Z_UfRSdyxn9xJ1WScpe-O8NaMTXHtBzZxKfcWns2Y24eNPR0fz_1X3U85EqywkkrefdxLzlMhXc4x5ACdjX16vM47EiHUEzULESqIA0ZtG4O8juVLuu2Xqd_-J0vVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Türkiye'deki İnternet Kesintisini Aşmak İçin Güncel Yöntemler
🇹🇷
🛡
Herkese merhaba, Türkiye'de yaşanan son ağ kısıtlamaları ve internet kesintilerini atlatmak için şu an çalışan en etkili yöntemler şunlar:
🔹
IP Spoofing (IP Yanıltma):
Şu anda IP Spoofing yöntemleri filtreleri aşmada sorunsuz çalışıyor. Xray/v2ray yapılandırmalarınızda paket parçalama veya IP yanıltma tekniklerini kullanabilirsiniz.
🔹
DNS Yöntemleri:
Bazı ağlarda özel DNS ayarları veya DNS Tünelleme (DNS Tunneling) yöntemlerinin de erişim sağlamada işe yaradığı görülüyor, mutlaka test edin.
Lütfen bu bilgiyi internete erişimi olmayan veya sorun yaşayan arkadaşlarınızla paylaşın!
✌️
#İnternetKesintisi
#Türkiye
#ErişimEngeli
#VPN
#Turkey
#InternetShutdown
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7330" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7329">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ابزار تحت وب «بهینه‌ساز کانفیگ» برای عبور از اختلالات کلادفلر
🛠
🚀
بچه‌ها یادتونه تو پست‌های قبلی آموزش دادیم که چطور با اضافه کردن finalMask و cipherSuites تو اپلیکیشن PattNG مشکل آپلود رو حل کنید؟  حالا برای اینکه نیازی نباشه دونه‌دونه کانفیگ‌ها رو دستی ویرایش…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7329" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7328">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gffZhUxMoRcPrSaLyHwZXG--Q_Ak3JGQXoQM1kQs4M3OaVz3kXcWnEr8So4lVe4ELkf2c3lpNStlK8d0PgjOn-m7PLdKY9dMRxEFCizduARQ36iKrrKXB82pu9e_nG_61IipDVwbLxQIrYWNvxe1QP_FYVi0I7KhvXPYYI_Ju_mgVIYU2NInZBW1SBAgqZ0xP1TGy095BwetyqBeilHq76APIpUxPbK4WCPb1Grkn5mfUHxNkXo2tDNGVqB_FdFCJulxQsVDuGO0doE95Ea0ejV55zPlvaOL2sBrRCc57zOzCjuI84wbROVbg8fjJUjYDdbz1X1yRdYg_iRePmq0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به هوش مصنوعی‌های فوق‌سریع و قدرتمند در یک پلتفرم!
🚀
‏با این سرویس، تمام مدل‌های برتر دنیا رو یکجا در اختیار داشته باش. همین الان شروع کن و از قابلیت‌های هوشمندش لذت ببر.
⚡️
‏
✨
ویژگی‌های کلیدی:
‏
🔹
دسترسی به مدل‌های پیشرفته (‌Opus⁩, ‌GPT⁩, ‌Gemini⁩, ‌Sonnet)⁩
‏
🔹
مجهز به سیستم ‌Agent⁩ برای انجام کارهای پیچیده
‏
🔹
۲۵ درخواست رایگان برای شروع
‏
🔹
۱۵۰۰ کریدیت اختصاصی برای استفاده از سایر امکانات
🔗
https://app.clickup.com/login
‏
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7328" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7327">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG: github.com/patterniha/v2rayNG/releases  ۲. ویرایش کانفیگ (
✏️
)  ۳. فیلد Address: یک عدد آیپی تمیز کلودفلر  ۴. کادر finalMask: {"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"]…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7327" target="_blank">📅 11:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7324">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFL-BfRzBXfNULTKGbevmugAaxNKsTwis8CKVvstEirUa_dgNMGc7wlX9Pk7i5Y9GEYHpdASgiS--r5Jkhdu4aIX2uz7tY_uQH5g_ehMdLX3Wk4lpWyiBD8Yy0lFrUSXyj9cvKlq5wMPT48a7A1imDk6rB8-lgiWQsx-YU0NzSx2Ba2zKSlbojLHoc8hEni9xjgwzJWdN5Mx3uCYDzR7l5o05CPlLF9mxxfkoHMtC7eeDpB2Gl8yx_DdcG910FnM4sv965GpiyJBy02-6itAOtyIZcgDbObMEmCeU-h9-Q11QXv0iLVSBYXz3iBUeEryhibK1chYyhOH5_U52dKTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vRonLYfPPh9ALXqYos73MsSl-F2U7S3IizSdcV4xrSedKqifcDa63MT9cHpti-CSEG88u-igMht0A06vMyI65FLl-jPE8g5PhYC4ty7PMqjuDlGZ2uSWjKaxj-eX5PxS411umfaIXAJ6aMBp3qCrXYdV_9pCFwlLM4Lkk54rsO69o8_EVohDg41fyDfmmR8WzkLpkw650XDnGRiv029LaI2zNxs5U6DJEc4aMiXKhOzz_m8_mT7IcSn8iYDiF1E_c1cZ-WbUsHbRHdIEpEVRZfC48uzGWIbLUwwFgopZGDqqf50xPVZfJw4yJTUsuyHuG0nYcC7N4piQkU20ynAxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mYq0uG_SUiArtNLL_HkvcIaF5KBEgwLcSIkfMruLWMTdedZcfBoV8Tt9iwszVNvjOncpD9CYRtRuGmXl5fqj3knE9jXfqKvpg0Z1z-sRP7-HOBF7Op06fh84tDL7Pwa-1ZgJEihjZosZEXTtn-bThDL8FgY4tJlwnoQ-DOl7hTjdhCgfQpbnHZAB8Du3Z5_3qud7OQckyeTbhJDkJMfE5Dnir6vEaWxa8lQCBwlpdO9r9y-74drd-siM4rhB3jUpdg-e_iSgeIh2WMQfDTTP0lVFSv026R1PObVlE44l2vA7kSS5Dc2sf3hXJRgWLGPJNjdcRhbIF6sDRUtQPsiHyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG:
github.com/patterniha/v2rayNG/releases
۲. ویرایش کانفیگ (
✏️
)
۳. فیلد
Address
: یک عدد آیپی تمیز کلودفلر
۴. کادر
finalMask
:
{"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"],"delays":["0"],"maxSplit":"0"}},{"type":"fragment","settings":{"packets":"1-1","lengths":["109","1"],"delays":["1"],"maxSplit":"355"}}]}
۵. فیلد
Fingerprint
:
unsafe
۶. کادر
cipherSuites
:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
۷. ذخیره کنید
✔️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7324" target="_blank">📅 01:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7323">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PattNG_2.2.6-P2-fdroid_universal.@ArchiveTell.apk</div>
  <div class="tg-doc-extra">68.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7323" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دانلود نسخه یونیورسال PattNG (نسخه v2.2.6-P2)
🚀
📱
بچه‌ها فایل APK این نسخه (Universal F-Droid) روی تمام گوشی‌ها و معماری‌ها به‌راحتی نصب می‌شه.
🔹
پست مرتبط در تلگرام:
🔗
مشاهده فایل و جزئیات بیشتر در تلگرام
💡
*دم توسعه‌دهنده‌اش گرم، واقعاً خیلی زحمت کشیده! اگه دستتون بازه، با زدن استار (Star) توی تلگرام یا گیت‌هاب ازش حمایت کنید کارهای خفن‌تر تحویلمون بده
😁
⭐
*
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7323" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7321">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7321" target="_blank">📅 01:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7320">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فردا شاید ی سورپرایز یا دو تا سورپرایز بزرگ داشته باشیم
🫠
❤️‍🔥
(البته از ۱۲ گذاشته ساعت)</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7320" target="_blank">📅 00:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7319">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7319" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7318">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9atrEgQ43hK5lBiOiSxAcG5gSeQlkOABSt4TqqgwoVeVnRHu8fWc7xqzm0jw_l97Yvedszc6MITT4dsylEAvohcVkvO1o86I1uOc8QbZTKgglnhjq4k_8QwxeUvUbdLuQfAfWFloPDjy6KYRoO4nV8_1Ek8_d5wzXW7suqLO68ML602cbgDwEyQdZPVvzdHTZS6Tkryt9yzULHGQ9SIItlKewfrdj5FNu1GY2b3IlFRoKLyAQVRjxjkUoJOBbKwkrNab8DYu_d-zlMqyyVoUiRZWkrpqpcF4oLSYydyz1JEWRNx-2cXNkERwKRvpGMY9AQa-Vg8rbOxkoLsezz5cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش شدید قیمت API مدل‌های GPT-5.6 شرکت OpenAI
💸
📉
شرکت OpenAI هزینه‌ی استفاده از API مدل‌های سری GPT-5.6 رو به شکل چشم‌گیری کاهش داده؛ اونم به لطف بهینه‌سازی کدهای سرور توسط خود هوش مصنوعی (مدل Sol)!
🤯
✨
خلاصه تغییرات قیمت‌ها:
🔹
مدل Luna (اقتصادی):
۸۰٪ کاهش قیمت! (ورودی: ۰.۲۰ دلار / خروجی: ۱.۲۰ دلار به ازای هر میلیون توکن).
🔹
مدل Terra (متعادل):
۲۰٪ کاهش قیمت! (ورودی: ۲ دلار / خروجی: ۱۲ دلار به ازای هر میلیون توکن).
🔹
مدل Sol (پرچمدار):
قیمت ثابت موند، اما حالت جدید
Fast Mode
بهش اضافه شد (۲.۵ برابر سرعت بیشتر اما با دو برابر هزینه).
🔹
راز این ارزانی:
مدل هوشمند Sol، خودش کدهای هسته‌ی سیستم رو بازنویسی و بهینه کرده که نتیجه‌اش کاهش ۲۰ درصدی هزینه‌های سرور و افزایش ۱۵ درصدی سرعت تولید توکن بوده!
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7318" target="_blank">📅 21:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7317">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vm_9R8hxflDmMj6Nu4Iy-qtllZDcLIaGZbxleKAJlDUOJYT5FH6Yo4SFsUWL36dNLD70oCUpumTlqKT1i8XrfGG0oDjWc13ujHQYHYazHkeiyvJ6V93MWSowuaaf2hX0zKyadEAn5yERKmSOz2vJtfvgiefrZY9V5zQqx7JSt8oZJFHBmHySwcumrqIFTmjrXXnVH5osAKOKntQbMHIP_9FtZLjkpT_0G8ejoeDmpXTKL10uCsbc8viw3dJxJBOPeOYm-CPOzNh449-inc3WnAne0QR4tIRcnqv1wTFXAIPzQ-EKzERDg_ZgEejbKKlGem7pCiVgNeHN7fxojnIuBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت ۱ ساله Pro سایت
Beautiful.ai
(رایگان)
🚀
🎨
بچه‌ها این سایت یه ابزار عالی بر پایه هوش مصنوعی برای ساخت اسلاید و ارائه‌های حرفه‌ایه؛ فقط کافیه موضوع رو بهش بدید تا خودش کارها رو انجام بده!
✨
نحوه دریافت اشتراک آموزشی (EDU):
🔹
مرحله اول:
با فیلترشکن وارد
صفحه
بشید و روی
Claim EDU Offer
کلیک کنید.
🔹
ایمیل دانشجویی:
ثبت‌نام رو با یک ایمیل
.edu
انجام بدید (می‌تونید از سایت‌های ایمیل موقت مثل
tempmail.id.vn
کمک بگیرید).
🔹
اطلاعات دانشگاه:
برای اسم و لینک سایت دانشگاه، از یه هوش مصنوعی بخواید اطلاعات فیک و رندوم بهتون بده (سایت گیر نمی‌ده و قبول می‌کنه).
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7317" target="_blank">📅 20:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7316">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJcRqrI8jrmQMXqW-H-1m2OIxy8xhL1DJyoOXmV2P-efQ9Gy28wC1GPSEx32pFLQ02RQssZw2AQi7C_KxcIgqgn9INfaF2SSopB7HUmCgScxr7c4oL6mgP9W-Or84aXYWfl5YgAqruHoP_M52mHu0_SgiCojPmXeKY36ToPNtnbYzHkYACV_e-lqxt7IJxNK6NF4HqZ-AamD3HsvRcUxwcCGJ99jWjepCq7cih9rpXmC3e0NCRoX4MdwJVQchtdSY0ikRtZgYNj8m3Rg3W8O1B1dHJFJ6VJsRfghlek9CUoK1Vr1rGxA7fev_RkoaEKDmJYYFyGd4WRO1gYz921vAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی ابزار PDFx؛ ادغام و تفکیک هوشمند فایل‌های PDF
📄
✨
پروژه متن‌باز PDFx یه راهکار خلاقانه برای مدیریت اسناده: ترکیب چندین فایل در یک فایل، اما با حفظ قابلیت جداسازی!
✨
خلاصه ویژگی‌ها:
🔹
ادغام و تفکیک:
چند PDF و عکس رو یکپارچه می‌کنه. این فایل تو برنامه‌های عادی پشت‌سرهم نمایش داده می‌شه، اما تو برنامه PDFx دوباره به اسناد مجزا تفکیک می‌شه!
🔹
کاربری آسان:
مدیریت فایل‌ها فقط با کشیدن و رها کردن (Drag & Drop).
🔹
دسترسی:
دارای نسخه وب و دسکتاپ (ویندوز، مک، لینوکس).
🔹
دستیار هوش مصنوعی:
پشتیبانی از مدل‌های OpenAI، Anthropic و گوگل (با API Key کاربر).
📌
[
لینک مخزن پروژه در گیت‌هاب
]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7316" target="_blank">📅 18:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7315">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یه پروژه جدید ساختم برای 3xui دارا که خیلی بکار میاد
دیگه لازم نیس آیپی های تمیز رو دستی اضافه کنین پنل
یه ربات تلگرام هس که به پنلتون وصل میشه، بهش چن تا کانال آیپی تمیز میدین، خودش خودکار آیپی های تمیز رو از چنلا برمی‌داره اضافه میکنه به ساب پنل برای تمام یوزرا بالا بیاد.
سورسشو شب میزارم.
تمام.
🔵
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7315" target="_blank">📅 14:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7312">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp2Y_a-XNhAEywC1648uROZ1Bd-ZAqQ-z2Z275RaX76v9svViy5gZOseg2fCO-SOqRHMvtP8aBfKeg4gO8WGD9t8tT5ZPTXovnAR9fygjx3m3QFP-ewVicUxkl3g5TsXGbRSeLfng2LQRkWnzzG5PifRdtQhENbWqm1YB-3H47J8oldv7JG2cvGlR00K8obMiil2sb9n36tQ1V39QSF2qzpnzG8UIiTMmgOwH34zhz3XUsrwF5JiQEG6lSP6bwTBkYjz5XGbxZhwrH7iTJahZvRpndY8dwXcN8GxQDTxXXL-sOWE8T05oQHaGT6NRc_N_o8CwJid0OXwaVoB9XFXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید پنل 3x-ui (نسخه v3.6.0) منتشر شد!
🚀
🔥
نسخه جدید با تمرکز روی امنیت، پایداری و رابط کاربری بهتر منتشر شد.
✨
خلاصه‌ی مهم‌ترین تغییرات:
🔹
ارتقای هسته (xray-core v26.7.28):
(نکته مهم)
ساختار
finalmask
تغییر کرده؛ اگر قبلاً از این قابلیت استفاده می‌کردید باید پروفایل‌ها رو از نو بسازید.
🔹
امنیت بالاتر:
بسته شدن دسترسی آزاد به فایل
openapi.json
، امن‌تر شدن توکنِ نودها و مسدود شدن دیفالتِ آی‌پی‌های لوکال.
🔹
لینک‌های سابسکریپشن:
تشخیص خودکار نوع کلاینت (User-Agent) و قابلیت جذاب چک کردن وضعیت آنلاینِ کاربر مستقیم از لینک ساب (با اضافه کردن
format=info?
).
🔹
داشبورد مدرن‌تر:
بازطراحی کامل صفحه اول پنل با گراف‌های تمیزتر برای مشاهده زنده مصرف سرور و کانکشن‌ها.
🔹
پایداری دیتابیس:
اضافه شدن قابلیت بکاپ‌گیری زنده از دیتابیس (بدون نیاز به خاموش کردن پنل) و رفع باگ‌های ترافیک.
📌
نصب و آپدیت با همون کامند همیشگیه، اما
حتماً قبلش از دیتابیس بکاپ بگیرید!
#3x_ui
#ثنایی
#پنل
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7312" target="_blank">📅 12:12 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
