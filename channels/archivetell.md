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
<img src="https://cdn4.telesco.pe/file/Xc-3N0lGcuxKCxPo-FDotJKRFHFRyjDgVdYP1b2ItwLm5IlohQs0B83GPsbUXrXCOAQN1ntpp7ZIyzDQw66WiJVNlCWJ9VMFXyNnJog3CcHHuv-y2PzhfxsvFv8ux9NOXN-XWRjIoxfq3SR2_rjGt9WLuimK408U1jaKoUDd3fmS3j7W6oakDHUmLjT0QmjarJAzXU_uGtmVd4tBPspy_jrPDgONpD6JwuIjdIXvLcC-Q0jQp3FiKq9Qzkb1ERmvlVsCvuAg0Oxm7C9mTB8XQJMCNT6UfIwKdjp6Ajz-FjZv_tPWxbbqObZol9iyMZKh5xRVF4nJh36ZPhiS1EgsPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 23:20:29</div>
<hr>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcUvkG9F3Q7mnF-XBm07iaZcQOLvknkkiCq7vZ2cTlqzgsxgjBPMsgVCrgLZU6f3_74l7XOKADmXQftwpCnsOqkhLwKi9j969e9zZRORj8yXSrUBdGwEds0ssCKPPv8omxcd2mWcj0TekauIlF3n-7QBaHIV-NR3FTjh1RUTCSFaDe-8g1LVgTfXh5LpRmQJLbayfiRRHF9qpjkQPllLVoy6c9vHA9iP1BcjO9f4XFW7nKaOZu1zDwqnHLiBufCCkR_G9d0AiUFkmBnQttxLqDmrXGkOz6a5IxrPp-gPYT2CN8gtqT4JRQcZfGdcvy_0uEw6JG7tXaYZgp7gTsKLDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQH4QDOQq_jbNA1Dj01-IctKMTIZmwZhfPIMZZJWZwPGVkV4fUpzIQ1FutXCNs54_jkklkB1zSxXEu04N2EZ-gTaTdv76bQ5MBtvIQViA4pHR50AdnigACkyo49H_aA41IdJdssjqcopkwr0bdvwq0-TeMyivCaq4q3_pqUr3u4e0AcasGGF8-ClbzdsYT_uPmzu2_cqOpgdgxMuHpjXS1j1nZOaW-RyJo9vXiMZrT1G03nfRplPwJi3h4xe7eDCuTsr46Dg_mwMbGLIf_mzVM3z-pbtVzPItzZiJcO7Lnl5goq_79exyq3RriyO3EEBw0R1DzNxrBIzxxLKLTY5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7429">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STsyR4-87njJ33qQy-Xv_LZYkbsyPrfsxHmTT1VGTyp8AINUz5ITZcpdtRWaOJK5cE4q1Ptv0k3BGiGERUHQjS6SBnWPeXa8o9RC9PAHX6cKGs0aSDoRxwZna1Cizhma_Cx6seGpwhhDQqraE7NLwbabbO-IL1fWL4ntL9Uh0lrpvtfZekvFo4FDmJade1Z0xWjKT-XCmSSDfwl5FjYiOW_Q7ZrX9nihVauae5U0WZfhyzb_c77yBfmRVVMVp5LpW6sqfUT2JpysqfKQ4ulWQEJiFYrjEHB_K-o4ed4oz7uLi6DIFnC4sxaXUfxupcFlVbSt7meR46UR7cv8A2QffQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7429" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7428">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=uudTHH5lzITK9kA8F1Ss3g_9kAUbNLyNtPOIb4Apu0TtSC82Dk8ib8zQxYVNrZeZBy2uzu29WuqrXeajeonOdf4EEk9U8-cKe2Lfd-MR-YBM4zlvpQafUqhB6ZwOBIl32UTX2mWSodluWkaEPdMpeSmA-uM6Ski-arYkTqJY0_SEMgrOYRODInEMd0AoBuTKf8Q2dIGbXsoCVDSxdijTtcC61AhWYTf3aTscqqBzRAireO92EJn0ryNr2en2vq0fwUeMeUwFiyYLYhMuqf2CdpMhZgwSn8x8slPZoIt65EEmZJ5V9rJDJ7GbjbNpeF-owKSQ0LrW_68ZYvkYKvd0aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=uudTHH5lzITK9kA8F1Ss3g_9kAUbNLyNtPOIb4Apu0TtSC82Dk8ib8zQxYVNrZeZBy2uzu29WuqrXeajeonOdf4EEk9U8-cKe2Lfd-MR-YBM4zlvpQafUqhB6ZwOBIl32UTX2mWSodluWkaEPdMpeSmA-uM6Ski-arYkTqJY0_SEMgrOYRODInEMd0AoBuTKf8Q2dIGbXsoCVDSxdijTtcC61AhWYTf3aTscqqBzRAireO92EJn0ryNr2en2vq0fwUeMeUwFiyYLYhMuqf2CdpMhZgwSn8x8slPZoIt65EEmZJ5V9rJDJ7GbjbNpeF-owKSQ0LrW_68ZYvkYKvd0aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7428" target="_blank">📅 12:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7426">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEPGqBZiJGLDfqZW3i2etgm58WQTienLIfTW3axGIJQ9os8R-jissoHXzu6u95GGixpRVwj4eLNlTuxRHjNsFPZq-3dl17BoUu2AhuuSITuWPv923wNyEo2DPaF7uYlcs8FJeKt4NrOOAmVXOFgCWCHhldS57J7NIKkxxX5kx-oPISDUAji42VC257Z1LdBzh-iPAZmLh-xavV3C-qiwhUUOHGCssk2FLoL0L1YeTFSO_viBtNX8Y7hM5AoDfjwaAhxAJesPEaHbj2S6yLY-z9JXghD6bNKvBZCKFW6tPpPtuaHOEecHYkp_R0gsly2Bs6GSwWHpVQxvgdRGBOL2Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7425">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7425" target="_blank">📅 22:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7424" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGr17De29yC-mvAIJxr-8SIkPMQK4Bf0ACin0VBQYAq0L2xzOn1zjx7D0-U27XVkppndPxXXoyYUtYIUQYMRqhFW8U95oBDhTb3t_ua0lO1NPTJVE878J9VSZR8HAmFDFBNw1ntbTXBGpoCdHWU4G7Ae2bRHqEjFZMSBEINSWhPq-lrsfTkAkM_bssC2GjU9MrFnIlN8K93K7LBaUdddbinSn7OXfpw52x7Za-IWJJKsjOG9-PZye_NNyzNHyB2uQU7rW-_IwYmAnH7iuG_L6EVk5ss46LHCzCByEArXGneE8vS9HSl7orTNLstEvPWUrOoEn8afz4uL0ppkkd0VXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCgpcj0xLNd3zFGpFzLBCyKXbiop2ZHc6JG1_Ltah5bvDEdYpU_nMw7M4ZMNVPfsRzoDIzxNVfaG6v9jlibVRP3rsLQ05rrB6IHd-rLWSKkJ-s8Hrcrl9YPJ-q69xZGgkQwghxpyTm3QG9I8fAO3VaEbwhlaYc_LnpGQu37JLAB0Oe5N25qc9a468y31iX4NH3KgFGKRpE0L5Gs3H08yV-FKT_OopP7Sg57RVQ4zSIfv_eV1recoSiZxrKUDSQEF_tcUVJbFsci5aJeWYczUHZy6q-U1MhltIOff2yfF4DRA6zR4q5Fyv72NpdgOb-_-vGJrvmhmH3p7WxynAOfvfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mO4D2Gsn-xRAtZIrrLUGl0UBVHMCh_wj3-mE9p-D_TKqway-6tvbD-Stw03YZxFdg3Em5cDY8FTtLR2Y1T_CCGPhvnbzNQwZxP9bzUFbmAKg7jyudLMAPBnOJ6FLriY147Ye7k417BhnDNEDdG0Ew2loleJFZa2PxF4A6AVJtcaEI8oMqsFOv0HtrLwcG7poFnH-brKSD3qTuHDAd_R3nX2oChX_KbmnjJEyHWi2k_Q76oUI_oAVnkwnPDtG7oW0JKuYAL3Ge05RuMGtqwcuuOHSqc0eLf1sWsEhTtcUax_UTd3dlhL7JSg01XwQNpNn8K11VEg9WnLVXr38X9pVTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddmV48PX28BzXo7UX5D_8hGCzf1-Im5VOE_Gia3xhvABahUlt40syVzy90xILS1INgLHPLOPIgunX0eJ1CrH2CH8qWagM7lmHaAWYWXKcESjGg1ZPtNoVTiCULxsOyUOyexOW43BRxQnCbqtf94DVm_2iFbQu-KkPFdkdheq-ComoyzDvsqyGe7qRMVyU0DxwVazzE8enM55pXXryVNHmNaKOdpIkOXa6D4n9NT9ZodscaoMKBSjs3lSXJmt3emenF26VvapGk5X9kW3dOM2KN0ca2E38cnkiW53g9r3p6eSAKTjgCrVBKxzI9tFlWFwLq-yRyTvHWNi0q23jf_clw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlRYoW614wFJcsJZ4QWryQOoEZCEcplGTAuWA96D6fFUNC7_xaHLZza0B35HYYR1RDnVe1Hkmid9sZ10o0SnaCbKThpW90RFDjXVSWAzjt8YLWZuW_z6kiIP88ik09soLkJB8xy7oekFtmPzec_ELxb-j8mKYqa8nr1MTlIDxjpXbQBEjlWcBacdUjmGnEXnnl83tWHKOnWrajc5tXBKNijXwJ7G9DjFG-2NhD3MZATFmUb3ku-BD2VVos8CuBk1YrshFBNBIgzL6MO7i3CgjkE-TthfWECsl_rGrxDaGXXhiGFtHNzcuIW-3nSX6DDcXeudRR3vGFEPqUBAUHLITQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtkyNG2yOyC6LZFXwK2kvmc2D5pS0TdRlrEsWqZSScIU2F6Tym7QX9hvWhbauojuwBMHcDKzkS2ruXq--LGJwwhJ7TanXwAPaJuS5jalj9EPC3x3zR1kMUtpfM2x7XwCyr9bTCJaUBEOCsu3IpSUmw-JmHmo5J7MEURaji58tfx39RzfxV1AwbeddsWn2xeKOTS7taIB3zU6aybGYaM2hsB1L9DAwcVaSYfY3nqAPe-TyUQmNod9lAJbNL0rZ0mfgpiPoBoXs32XrVAgbKnLdWuaARSCvyuXZakjXUxd8uewECdR5lIperc4yv62riXjtoQSeDhAY-fLHRQhZNrpJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6XoImr7vafGIu5Knnm919w4iBm-3k0LCAFdIM83lskO1Be7zPJjKBQw8dtkPx2INu97dJ-bDJFzZvOGPpFAFp_h5Xd0bpofvfO2EK7MAIGyw20jC8_nk_5aPrrArRusYok0kmDgoBohgY4zDrzEKUK0ueCAAH6lDwbLxuBg7JBx2DQpV-HdDtEcxR2iwUzaUR5PT3gTJ_zHEQ10NnTCIMBnADmOcE080qpD6IP00GC3DPyj-5mijYX1E29QUWhBzlIUNThBs-E2JICK8-1hyIm6e1Dzk2aMfJm7wKVPLlnOV9HSJ3r3nj0lklhJIB0Nhv6niwOXr9_DkA3s93h54Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhJp3dXLKKSUapcGQignrzkICth4vx7PBaiCeD6pWkDQuYJpHhKTZgSSB8tL-rGM5jYg7LodegWAg8P06-oBCe04giiZGzIvs55EtHpYrfgKNlkNN7G9LL1Wn8hEwj1VsvPk7fmau_a60BCtjq9iGaXv34keiWlQ3mC-shyFrDvNHEEo7V3TPZLT_2adzpDV7sn1btEI_ZpOxnSZvCmHOSK4_PIGwotmfeD79X7_UtFuchKlfoPL5PDIhtp2gt3VBge1-TTwcGPKuUHzyq0r2akYExATrb4sWI0Gn1WGO8gEagA9HQy4QDaxLBU6qCpf24l_bPiQ_9mj5ju6I7Ut1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=uUywQf5npxgxbrzaWkUAGO9cbhTALr4gh85t55isBV1xkKWOX7oaiE_ek0sl-wNghYBVoiN6t1hyiFiOc_WVsZtWT-RXwzt_7Gg2dfezwX9qvndG3lmFCBzWhEGE0N9SWlJ60DnRLVJw_56EBz3vVEZad4x24kIKupxDXSWa9hVLTefY-ZfVh1OM_laL6pZnVb66CLzbG0hNL39UcOxKIf5ZBksQeLSlaMmvSfRW3i2dsB7VNLlupuqjAA34kG8zj8Hx3JVer39qRnFH8iqcP0gZ4V3Aq6xhstpjfKexW6lgQ3GXnec7_3x9MEgT3mMF67RufcuL6naPQ3IJ6VxAI0vZT2rOim0ASOkZxPYHAB_dJwXErGmbHT1T1ZtYi1DxIM4sH-IxuvhuxJTqOBUNjwyLuSN0Vl6WXTT6RlX6hpGKJVTTyikRDRBO51zgS1EwVy7cj42N57JywQLsi-klZTn190QRTr0FmtipwxTQKAhlUNrYjK1I_bM5jxBtMHfqv6giX6mBamDTgFeDZXshKzU7o-BAOcEfbXk3jyah7c327WQrqgd4Lf1CReoFIesR_HHupVz2cf2oMAvyPp13PY6rB8szQ6DzAb3KXi8n_OwdmDw5768cORDWvjRmX9Ju23KfqmhJOclE19ZQAbjCmLA_Yg-PizEpsxnCymOjkYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=uUywQf5npxgxbrzaWkUAGO9cbhTALr4gh85t55isBV1xkKWOX7oaiE_ek0sl-wNghYBVoiN6t1hyiFiOc_WVsZtWT-RXwzt_7Gg2dfezwX9qvndG3lmFCBzWhEGE0N9SWlJ60DnRLVJw_56EBz3vVEZad4x24kIKupxDXSWa9hVLTefY-ZfVh1OM_laL6pZnVb66CLzbG0hNL39UcOxKIf5ZBksQeLSlaMmvSfRW3i2dsB7VNLlupuqjAA34kG8zj8Hx3JVer39qRnFH8iqcP0gZ4V3Aq6xhstpjfKexW6lgQ3GXnec7_3x9MEgT3mMF67RufcuL6naPQ3IJ6VxAI0vZT2rOim0ASOkZxPYHAB_dJwXErGmbHT1T1ZtYi1DxIM4sH-IxuvhuxJTqOBUNjwyLuSN0Vl6WXTT6RlX6hpGKJVTTyikRDRBO51zgS1EwVy7cj42N57JywQLsi-klZTn190QRTr0FmtipwxTQKAhlUNrYjK1I_bM5jxBtMHfqv6giX6mBamDTgFeDZXshKzU7o-BAOcEfbXk3jyah7c327WQrqgd4Lf1CReoFIesR_HHupVz2cf2oMAvyPp13PY6rB8szQ6DzAb3KXi8n_OwdmDw5768cORDWvjRmX9Ju23KfqmhJOclE19ZQAbjCmLA_Yg-PizEpsxnCymOjkYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTNLAr3EposlXB7X0YK_UWjJ8kgPqjxW7VvArp0TKSEQtLr0RlzWaXy5JSvGVqI1vl3i01UtY2_SPsQ1Rr2DoR1PxkVIiF13fgEfLeMSYeIQYd6ZIkaO5WvHfR9vCgT1cCodBC54ZuRpWBN80GNN2zMXuFSEMvn5XOvuxqldufLh2GYruIBs6FG9qRkgJhaF55teseKG_SPxyq8SJWuKw9bOWRvr0HVIc31epqZXnFgiivkuIYzpOtem7T5dQlzbffE9A8HhfdmtpetcXkYU68FLRin5EgTV-ZjXhc4cR97-1ZlTcDO_nNJorBdcb1lTs9W9zDUltLgD3hXGWqAX3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-5DG5VZmz0ZANWkNYgilLb0yaIJOgidTZs7XaA5ECwtgRssfvRitYMjowpo0Vs7uukmtQ8YvPPU_l9PLALa1vxVodGO2eAdCK2aBJpllg-0Qqd17pWQVG9kuil4LNM-J9JluCsmmpwHwqO3omARDgp6iRCIyFw8YeDUpUTGwnwSrI6x0r5dZjBEPiXtRiTs_nEVEMCWuVXuKVVzfbu-c_MREQVxbwTrBFQ9eSGe_3SeSNPnHu0JPjN1uyaWgRoVoHxhO9u6hBN_2w8vI25KZuqYwe-mQWef4UtrrGSUXPr0iqUvxr_kxlVurR1QvYA7Uz32RjwKQ6jsOt7z8Dgnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7394">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url: https://www.fastaitoken.com/v1  Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471  Model: claude-opus-5 Model: claude-fable-5  دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7393">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7392">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_hZ7ji8OFh5C_-0jPNcSO6MLWZcba0KDlzXN3KMLxawB7uZWGBbTbOVwC0AelG7YDl5YKcgWbUfRzKUcD4BLhsBbzlf1B-Jxj8ft8A7j_wvZkvxOIVEz-AWY8xnSBbzAoyQPIjQRdAEU15Ya94G8FuTOtxmP_nhL_Y3QyRb7EQE5BR-CedDcSZAmnC4ume5zfULkcP-R_jW9yDB09wfM4GX4inlGJ2D5uyV3rkEPqttWsGSNvwLfe9Z2y_LLSk7tiHr-YPSK8_h3Pzzrd8C8QmBaQa-b8XKK52zsCNKhV0RSmqWDXxDHkHg6i8qLDFrUkFiLrAlhX0Y3Ak-zDgTDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7389">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMpWtaUTskmgxX86s43mZNRTmKxnt0up1MrsfIRD4Bu-vgj5jgw8_jA4CxNhi0fDWJFLGhkhoLyvRYtcw7kWJHMQZVOdBI_u58MHXBTaNQZjspnMb9k4Irmu7TOqzC8u9Ec-5-84p5O5nqmwWT0X-0HoF6yI0CqagY8KeGw4xegUG4tCuibaa582CRrg6toZxB0xA_YcBeO72fUc5ESqODQkHueLs7ysul8dE2MyoWmINTqyHC7C56HZDI1lKT82M2k43UWqPHhu__9Urx8Xo8AxgcDce4HKX_IVlhOATvUGzMX-703PS7s5_EOKpsm4SwP7yoAaWobeRzRdMQMIqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دسترسی رایگان به Canva Business
🔥
از طریق
لینک دعوت
به تیم، وارد شوید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7389" target="_blank">📅 12:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7388">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7388" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7385">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7385" target="_blank">📅 18:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7384">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjpHlL5UwS8G86CxyD8GBkvuJSqvmb-2_WgA_1gVe6jp-u3AcGGjE5cnbmBnBk-JhPGSF12ETZ9sRyroHruLg0NNVAy47rsA8Rzo2MBUkEoFy7saBeYgmViFtNL0UqHs4WKA4QtiEleEcJ5YYPe19C7sK0QmA5u0NGydMNq69bKtC29HU1OQ6UOz7zdgKjy276ZG7nRdFti5BBn0-KzhNpKJzJaVLzYQwH0ZXVmyyXRcZit51k2i8cUo9i4LnrXZoH1f9Tc7kXvv1AzMUrLq1_pPiW8HhlpsGE7zzME7q0aOmkoep-mz7Go_TeB4IlruJLn4K6MdZ8Q29Vf-4UpiFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
دانلود و پخش آنلاین موسیقی با فرمت FLAC
🔗
http://1music.cc/
😀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7384" target="_blank">📅 18:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7381">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوستان اپلود کی ضعیفه رو ایرانسل بهم پیام بده پیوی
اگه حوصله تست دارین پیام بدین</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7381" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7380">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7380" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7379">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPNM8wkTc13yqxakYFDDuCQCnBmuLLloFlutYwGK87vSTBtuZHJVK1jrqsdL5mIyHcpG84HIEWHkRzEeuwb6OAqym0ja44e9MxUPQ4FccA2Rmz1LZbOBhIh1TL_Wgt5qReQBve3vkhLLl1gU9FyAGJMh2QOXRoKccjxP9Nt1JKMdhKcjt3r6DGNk9T_KTRa0vICWEvLVukrKmbnjOQ6eSDbaswZGfS9WWhmbid7kSTARYcBTUTKTdrfILTV8Jx2GNr08EHJzm6yvlzsxbB7xZ0X1qYz2GhdrKiXpdHaNlXUez9t1O5akJxlbRKW3zH9HpEykmC_7UITOnISFOMiJbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7379" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7378">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=ZzWDBl8UDAtNFqITRVNTxMvfD6z85hio6ph4WG-RgkTEWDtcOsjFeqACq1mFjIgXxO3x2IrfkIS5aIKds7pLF1yNsbYSaMxPfky578Er5E1LBbfJCCLKk7zN4alX8AJb4ZBuuixM8qKHs1fySKBt7rDs9SOb1HPy3ZAKwXALmPl0ex-YY71_8W-RGcO5c_26_Sn3M0Faq-KV9cl6v_ErlT8KG7yu5NjFwA3Zs-7fqXkvy_HjI0cWL8n5qqyS_Clw-PjT5cdJjltNDc5bhSVZ3ovhT3aZFqZgvS1uM-qQx992PqHZO67ihHZdB4NppxsNR62ForJIpCHBKJZIc0PV3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=ZzWDBl8UDAtNFqITRVNTxMvfD6z85hio6ph4WG-RgkTEWDtcOsjFeqACq1mFjIgXxO3x2IrfkIS5aIKds7pLF1yNsbYSaMxPfky578Er5E1LBbfJCCLKk7zN4alX8AJb4ZBuuixM8qKHs1fySKBt7rDs9SOb1HPy3ZAKwXALmPl0ex-YY71_8W-RGcO5c_26_Sn3M0Faq-KV9cl6v_ErlT8KG7yu5NjFwA3Zs-7fqXkvy_HjI0cWL8n5qqyS_Clw-PjT5cdJjltNDc5bhSVZ3ovhT3aZFqZgvS1uM-qQx992PqHZO67ihHZdB4NppxsNR62ForJIpCHBKJZIc0PV3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7378" target="_blank">📅 15:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7372">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7372" target="_blank">📅 12:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7371">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7371" target="_blank">📅 12:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7370">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7369">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3-8AJrRZQOlLQ7amPeoLqtrdnsG291qNrxl9a5g7Yw7Xi7smDhUqHNZ3okwhY4mSc_etklmxjSAkL2bKgyp43k3nSvzePgCFVTvzJsDFd7to7Iytd-QZ3tdU69Eg-Dmry3oDdlqOgOHKKPgoLx947Mr-aUdp0igx4f-QW82rHty-LSLQvlfZrj32jTwEiZlm80S2ao21-7zdE9Riga0zY6MuTDwBcSlqHfuEzzs4UM0Lh3IchdIVZ400cWLO5U1QX1w1vCFKEyr5T5CQ__tJdGHJFAwuE3zajb5yNX6llTbzxInT4yUuuOVkOo2obFGgwo8PReavrjZKL1QLA3obg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک های Qwen3.8-Max
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7369" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7368">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=UU3uW2LN5Jt98yA3XO90bolChcDc-WdFh9dyLQh932mCI4EnC_Z4TrZMmnKmerpUsDdd1IrVbYcJN-u_AbIMHk_HaFXtpBCrEJcM9e0zUEuRZsZwLKik4fA5fGER3_42AcUbLuEAUuJIvG4Mma8KgeqjYbb0oNzblWPP3CXPYO2YgFVxrfId6JxeQHw5ipi9PQ2uuf3-CcF_hdXQNhCT45DJm4N8tl0VcVYGE7W60fpCd8Jv76wNccbrE1uQfMZklR6lCti1jG3mFeeSg1MzxSBNHzBAwDmC_zowvJS10jXQO3t6c7PjBljvWhMyP1X1f8kgL_pGDafo9SGjvFb2ih7ZEwXn9sngFkVU-6iRkm7iD7xwQ4_DeuB5P1H9weC4D0uzZUJSJ7JkrErGwEfo1e0vTlygRzYsBxXBcalHQzqxehDZk1xfOCPe-6QVfFl0HGouxSeeGG_dGSteVHIph0SuWEMljR94uWQ8_eYIshnuIdknRJebyAvcVQ-mrrug6Qdde2IIT7bMOBHo74s8_YtV1ur7HOzT4Dchh4wEo1zCGZ270F2G7FwWiw78ND5ony-jucB47dhyxEqAAbtyj8xgDv3a1rudkMvYCCCYsonJJXde7Ld6sA_-GpfG8NrbHJtUBc9ozfZCgnlMAn2sTI0-IqnrSxuoqqWA92zIJPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=UU3uW2LN5Jt98yA3XO90bolChcDc-WdFh9dyLQh932mCI4EnC_Z4TrZMmnKmerpUsDdd1IrVbYcJN-u_AbIMHk_HaFXtpBCrEJcM9e0zUEuRZsZwLKik4fA5fGER3_42AcUbLuEAUuJIvG4Mma8KgeqjYbb0oNzblWPP3CXPYO2YgFVxrfId6JxeQHw5ipi9PQ2uuf3-CcF_hdXQNhCT45DJm4N8tl0VcVYGE7W60fpCd8Jv76wNccbrE1uQfMZklR6lCti1jG3mFeeSg1MzxSBNHzBAwDmC_zowvJS10jXQO3t6c7PjBljvWhMyP1X1f8kgL_pGDafo9SGjvFb2ih7ZEwXn9sngFkVU-6iRkm7iD7xwQ4_DeuB5P1H9weC4D0uzZUJSJ7JkrErGwEfo1e0vTlygRzYsBxXBcalHQzqxehDZk1xfOCPe-6QVfFl0HGouxSeeGG_dGSteVHIph0SuWEMljR94uWQ8_eYIshnuIdknRJebyAvcVQ-mrrug6Qdde2IIT7bMOBHo74s8_YtV1ur7HOzT4Dchh4wEo1zCGZ270F2G7FwWiw78ND5ony-jucB47dhyxEqAAbtyj8xgDv3a1rudkMvYCCCYsonJJXde7Ld6sA_-GpfG8NrbHJtUBc9ozfZCgnlMAn2sTI0-IqnrSxuoqqWA92zIJPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم Qwen مدل
Qwen3.8-Max
را معرفی کرد، بزرگترین و پیشرفته‌ترین مدل خود تا به امروز، با ۲.۴ تریلیون پارامتر.
تغییر اصلی در این مدل، توانایی کارکرد مستقل برای مدت طولانی است. این مدل قادر است یک پوشه خالی را بردارد و یک پروژه کد کامل را تا مرحله تولید، بدون دخالت انسانی، پیاده‌سازی کند. علاوه بر این، این مدل می‌تواند وظایف طولانی‌مدت که نیازمند برنامه‌ریزی هستند را مدیریت کند و از بازخورد بصری برای تصحیح خود در زمان واقعی، در حین کار، استفاده می‌کند.
هفته آینده، این مدل به همراه یک نسخه سبک‌تر (27B) به صورت متن باز برای عموم منتشر خواهد شد. برای کاربرانی که از API استفاده می‌کنند، هزینه پردازش ورودی ۲ دلار به ازای هر میلیون توکن و هزینه خروجی ۶ دلار به ازای هر میلیون توکن است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7368" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7367">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7367" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7365">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7365" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7364">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axxalmcRAivTQghfvXI9hpfbv7Sb3ztb_jvsmYnwXXPDKK8pncExZAneJt9nShZEFolvLTZctrSNG7us8_O-e4YvNjVbtRO_GZ1xEwCncm2d4xBNki47TELVekEsY_kF0mWKj4QoTt3HNicMk8WtEYVCFoFOcWr94qKOkR1jQigmLV99QoWvcN5Jq3X4gC-djdWjMVeH7eLYeI6nm1n2GwwfSv26n7ltPPmU6V3ZfwjVpAuDMrxLMjGpGAtOOm2LgmZ6yCpCy2cQY0U2kjv5x6bbj8F0jwKtShYXMMMb7mfxo2zJDgeya_Hd4fVo-6TvldypSarBKqwqDAIRZzQbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از DeepSeek Flash جدید هم پشتیبانی می‌کنه و طبق چیزی که دیدم، تا ۵۵ سشن رایگان در اختیار کاربر می‌ذاره. منم باهاش تست کردم و واقعاً سشنش خیلی خوب جواب داد و هنوز به محدودیتش نخوردم
✅
حتی GPT-5.6 هم بین مدل‌هاش هست
😺
👩‍💻
نصب نسخه CLI : npm i -g freebuff…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7364" target="_blank">📅 22:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7363">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7363" target="_blank">📅 21:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7362">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7362" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7361">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7361" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7360">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7360" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7359">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ow1KATvjzWPoZow0MNGuRwWcMcJiOp2gfz6jsN2cATdz_TFeVz5x1RPv_Y4CCjk2eUuAdl0CmbPEi3132savQQ192Q2Lr3LvR974ASuaYG9TXiwumfFLumzEM5jlHiMMoUP4528_LOi9rsbp8NnuFOY9ZD92KxqcW7yWCO2dI8XrWgkOBpp5x0yBjrfNIQM39tUoB3uNkmNBKrQU9QecED_DcAUUuOo_dAaW6887RQ3EkNYSGw0IWGvZ4OhYt13hlazLX4NON2Ph9ay3pszC44NhLS3yxGbO1XsYkyIgrY5gfxSQes5V0upO9pm1-NtgsMkdksilHMTYRqR0LwN4pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 2900 کریدیت رایگان برای بهترین مدل های هوش مصنوعی
🚀
Fable 5 | GPT 5.6 sol | Sonnet 5 | GLM 5.2
آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7359" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7358">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یکی از اون متد باحالامون نشه ؟
😁</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7358" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7357">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7357" target="_blank">📅 13:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7356">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7356" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7355">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7355" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7354">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7354" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7353">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7353" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7352">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7352" target="_blank">📅 17:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7351">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7351" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7350">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7349" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7348">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5   برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این لینک وارد شید
✅
…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7348" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7347">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7347" target="_blank">📅 12:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7346">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7346" target="_blank">📅 10:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7344">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eD6egei49cZvtkbpQO4jirlRr7RiHhKZbqeUGm0sgmnh4kT6yo0Jaq07WQfXpurj6QpE8K9AMg0fTP6hdudGyM6JMK4TKnRNxabwm0hbqOuVLHTzh0yU8uwGRdA2G2OXsIdRVVbTy2sDZDAPR7B2n4M0CRZCt-HzayNmdmzTx-AF8BHzY8ypsC069j7SBc-z6hjDNu_TtggV1CXYUIl8Gk5N5QH4wmONoocuh4kGAyyi0Xbe9j4bNrw0GHm56KaLP8SJazDop86_o7V_G2FfBYK-Pje_BjlKAPvhtPfIAQEVl8aJ6_OsY34dcFVsW5J9NSjiE9qZEnw2M_JA9QX0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F83m8esDiV-Nd2ko3sJ0Y9HVpi7OguoZ7nA5SP3nRJCJMudHRrGhVZsMCgVVmRyhZ9-FhDELHLPvjMUWU5JJCW8QpvBr5tq-YtgLRN-IxApI1amWwtG8O3rEMsTxH8Uo5eN3OJWGOlL-DPuHiC7Ps9j_RwR8CTP2qy1y_gofxtbKsOBi5U3zgRuc10cZL0itT_NJpHgekO6pI2kp0uQRbienby2Ihs93W3XylsNgyLfBokDenk-tQQkZuCDSsMexzIN1px1PrCn9XWay6ExGRim5iPAdg-Z9VzvEnuUqfTERam_ntJe5PTvFsH4BuIVzw7vXCBqCCjej2MTt16kMUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7344" target="_blank">📅 23:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7343">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7343" target="_blank">📅 23:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7338">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lBpQc54aihZTP0D2vxqbzAE-xwgSYrRyMmas7wsF-PcqJEikx7wJrNavKvr4ejmnqhTJ767Ib52l0yx7r_sOmIj2pdAb2zIBZxTGE0QMePv2hQG6rhn-SSnAwePjxKLfGnnfGpYLprDbAEaKtks7eDL2LadeNcTSFBxQfVgFWg9vhrJ-2ESrUtTmNJpUhEO8_sE7nPcix2xACoS_AidB8Rm8IeRjcilpXT1Dyx5VkAfIkuFLGqBtsuxfXontHgP-FT7eD_ARYBFFV9jUF6aZ2dvNgR-RRh90kO3r-4TVVxvp3k606eJCl26xCvg5Y2qK437_zNatSS0uktQTgYKEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5FVAFbV8snhvUd7dGk7rSA1W3m2h6xenix2E0FxLoA-K-r7b-ZbT9FUSYKcK01ZarqOUZA1HHOMC-ug0nny7bIvw-DqKXEkZVhN7DuGk7TTkRCnt2tNbltrI4c1k5nGygGlfisJs3IBa3Qrvh3wtnqs05BHniFGkh25GX3AWPAzCdvACFv2YgNy6laoyxYYua5VIRYMdllGgkySZGTAn6QBshY3rHAaOiaR9XR4XXZLtduoz-lkJ0rQyUm1SXEwYH7BlRyHtrjYefmoOv3bqjFJ4gzFRR6M62x9qgWiI-CB6uUGlf_vtsS4haqG27gzc__GcaT88GVfw3P7CRXMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zm0ec06WEHZxdtE_qO3wy6XlNSVjezKaylGrr2jrtWME09shh9Em8EkR6gagDI9skR3VoL-USaBJaTVfYIizACWr1y48_FPN6tTPPneFEOOYVx8rLlLwqAL1whSGIoiMdaZHn_cSgciNVtTlZ2zJMktnRHdb8b_d4hKyi2mShsrYDVGGoJ3ykv0LOW1hVKwmu029AWFIZK6xpXTIr6jx70dk6o_5oY-h8_SBLckeNBHX7kQDCWuR6Sr9zRCn0l-ktwdn77n7ARuZshWQKqplEiQ1ZDZOexXV0ntiqWPND5ADKnFPm6KsojViSHE03BOr50KLM9yZ_Vjmo5EaX_hvEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuDBXAnrktv2LfSpuCHQ2i-uPCIWzmLJfGdg0FQcKoT4Ii8OM3VP5q8uBXVypy8HcMo6KUW8izi5u07qleE2IngoR58BO1sXPPhnGkNaVEmnrAU2VbvwZhW5DAtUwb6Q2EWGSTryErNBTkrpaG6CEkJriXCr6ayqKuaMDTPS59FQmFBpjsoJNvPloE72fK9rqW3_3pPEmZJ1kXYDnUgjYuTXwVBqhu4Yf-KqB7gwP_H6-2TdcvlSxzjOzYFHlfdJuz6QR5GMol82ipvKDs83ace1-iIVs2KNej5eVtpX-PKUTTxnuSEGUmLxHvpB8Z56MMAGjzQZjoSGM1oX_TiffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_L1Jk4z-wGXw_AbyGkuqh5ovRWl8gZOLTxkDvS-M6H1Kisn_5k4Je1qOFOzBk7vf-mNcO4vpg1pdr5OzfH0c2lHRiVh4gF-ouyHhiwoohw3-3mK2HSEnG6ouyMcCOEJdQLhwzuGFN7D1_89QIfk3hUXzrmGeNBm4bkvozsW_XB_9nv64Do5wtOnUTYDnyNJXPq1Brg7MWUPUN5nTsemW1O_NXTL2M6JDkjgYyRquYyToecyKa0EAgvMJSwV9Klf6QoMFiuFTiCHmvW9pcKzESMpXy2sZoJQypvUfy6pQWgF7E1f2E4O2BluHPKxNLhT0VrjbvffGfW_XIJ6HX45gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7338" target="_blank">📅 21:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7337">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7337" target="_blank">📅 21:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7334">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بالا باشین بچه ها عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7334" target="_blank">📅 21:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7333">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بالا باشین بچه ها
عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7333" target="_blank">📅 21:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7331">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7331" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7330">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7330" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7329">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ابزار تحت وب «بهینه‌ساز کانفیگ» برای عبور از اختلالات کلادفلر
🛠
🚀
بچه‌ها یادتونه تو پست‌های قبلی آموزش دادیم که چطور با اضافه کردن finalMask و cipherSuites تو اپلیکیشن PattNG مشکل آپلود رو حل کنید؟  حالا برای اینکه نیازی نباشه دونه‌دونه کانفیگ‌ها رو دستی ویرایش…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7329" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7328">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7328" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7327">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG: github.com/patterniha/v2rayNG/releases  ۲. ویرایش کانفیگ (
✏️
)  ۳. فیلد Address: یک عدد آیپی تمیز کلودفلر  ۴. کادر finalMask: {"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"]…</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7327" target="_blank">📅 11:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7324">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7324" target="_blank">📅 01:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7323">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7323" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7321">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7321" target="_blank">📅 01:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7320">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فردا شاید ی سورپرایز یا دو تا سورپرایز بزرگ داشته باشیم
🫠
❤️‍🔥
(البته از ۱۲ گذاشته ساعت)</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7320" target="_blank">📅 00:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7319">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7319" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7318">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7317" target="_blank">📅 20:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7316">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7316" target="_blank">📅 18:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7315">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یه پروژه جدید ساختم برای 3xui دارا که خیلی بکار میاد
دیگه لازم نیس آیپی های تمیز رو دستی اضافه کنین پنل
یه ربات تلگرام هس که به پنلتون وصل میشه، بهش چن تا کانال آیپی تمیز میدین، خودش خودکار آیپی های تمیز رو از چنلا برمی‌داره اضافه میکنه به ساب پنل برای تمام یوزرا بالا بیاد.
سورسشو شب میزارم.
تمام.
🔵
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7315" target="_blank">📅 14:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7312">
<div class="tg-post-header">📌 پیام #3</div>
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

<div class="tg-post" id="msg-7311">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6DXirq9D_4S1VvTiX-8Kp5UfdOKZ7PqFzbv6srTAz4Idj2xna3sBMFNkxS6OsUiEKXOLZ4ImUN5AS4pgKQCHtRBRxn7dAX8RqswVi4ZBE0UbePY28xm_fctg0zAI0gM0HusGYDlOrud9uw924ex9TseE3JkutQxSE7PzbfgIS2hkUYmxrswjMjb88kmCL6In2GUwcd3ww2MId6d26I0PhVgXKFPWmi4UQjOTsqWcFacptmWpeLQX3EvLxoZEr_LSfmOA6pd0RVvyCre9KNCUlp-61c4pi6aQJTq185Sg2lmqN7BTeHcY6yI_x-fZgfI03NfA_7QVAMPtGIy4J_byw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک ۱ ساله ChatGPT Pro رایگان برای دانشگاهیان
🎓
🎁
بچه‌ها می‌دونم این طرح به خاطر تحریم‌ها و نیاز به کردیت‌کارت و مقطع‌تحصیلی بالا به درد خیلیامون نمی‌خوره، اما اگه دوست یا استادی خارج از کشور دارید حتماً براش بفرستید تا استفاده کنه!
🔹
مخاطب:
اساتید هیئت علمی و محققان پسادکترا (Postdoc).
🔹
شرط اصلی:
داشتن حداقل یک مقاله در ۳ سال اخیر (در سایت‌هایی مثل arXiv).
🔹
تایید هویت:
نیاز به ایمیل آکادمیک (بدون VPN) + کردیت‌کارت (بدون کسر هزینه).
🔹
مزایا:
یک سال اکانت Pro با حفظ حریم خصوصی + ۴ دعوت‌نامه رایگان برای همکاران همون دانشگاه.
📌
لینک ثبت‌نام در سایت OpenAI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7311" target="_blank">📅 10:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7310">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm9eVW_akZf5s2bxxSWw1fSFnT5aVbMXEwIxye1rnSmOTG9V0gC9DyU-lSLG64D_C4ob54QRWRfa3EMZhUsKT9lbgiW4EliYtG9vthAWeDYQAEAesQpSC8rrDMmMV8zzKpVq6wQiWB5W7RzNdlLCmYx6N8g3WyIfQ4Aa59I2nmPPolhyh-AVykATXg0XU7XL6H_IP3UXoJoIYmRTTTmscZspp7uf4ftNT56hl6llkvtaey-jlLtBn-jjotcw3sJxmL6tXxT-pXuL9oLCV4yOPARrC08V0PF0uN6qclhQ8pOYYvvC-wTGvek4oa2mABMz1Ccbnz_qxqpm-iR-uYbXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از Grok Voice Think Fast 2.0؛ شاهکار صوتی جدید ایلان ماسک
🎙
🚀
شرکت هوش مصنوعی ایلان ماسک (SpaceXAI) به تازگی از جدیدترین و هوشمندترین مدل صوتی خودش پرده‌برداری کرد. این مدل مستقیماً برای پردازش سریع «صوت به صوت» (Speech-to-Speech) طراحی شده است!
✨
نکات کلیدی:
🔹
قدرتمندترین نسخه: به گفته سازندگان، این هوشمندترین و قوی‌ترین مدل صوتی است که تا حالا توسط این شرکت توسعه داده شده.
🔹
پردازش مستقیم (Speech-to-Speech): ارتباط صوتی کاملاً بی‌درنگ، که باعث درک بهتر لحن انسان و کاهش شدید تأخیر در پاسخگویی می‌شه.
🔹
رقیب تازه‌نفس: کاربران به شدت منتظر مقایسه‌ی عملکرد و سرعت این مدل با نسخه جدید gpt-live از شرکت OpenAI هستند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7310" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
