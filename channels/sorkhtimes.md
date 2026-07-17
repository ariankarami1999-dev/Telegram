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
<img src="https://cdn4.telesco.pe/file/NM4LKm_TT35KGAKay00z_65i18_5thHJYeslnpWmcOV0QDSmhzbKvs7NDT4NbPQf2TRV-upzo-YgQO1mFYqZ29_mDhiNt3OMOlvDXweqzpYUdS_PrY2Ljp1zbo45cm-h_G5p9pDtJwNzzKesQHzndi02XONcjn8s62mV7k6xAaKKE3l37NoWLZeu9trezyaGissO60fq2DXsXZnGpBn3A3DZAkdpBJ6NGIxAU88Ii1zNeEN3gDBDotNf56VKgYZgb_U_jfOvS5al3nuy3VeI9AGRu-WqRBnb-yaUdePUlQHrhnL1_6aFrkrLwkP5rXHY15xw2surgsnMfBGLwsSw9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 04:27:25</div>
<hr>

<div class="tg-post" id="msg-135989">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135989" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/135989" target="_blank">📅 01:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135988">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGhNcUId5ZBBqexty8ohXSu3lJzkntAzFLSZIm4BK9rFDWR0Dkr0Z_yue0gPNzaq7Wq_CYW1JGGJyUfLkhMamkkUR1m2HBGPUP9l2n8lUexbbT6pt6Gt7CzFTno3qBQfIPbxVlt39E2Jkp-Dq9fMU6du8IH7dURmVl0ek247Y98n9tmNPwQQ74ODimjtgIbB59NTyqG3wI41XhynZIKnV7brwiUr-jnES7LZy75tVcvO8fffx4bPVRCfmOZTr2DMI5metv_OGbXIjdARI7TzCAsrlwlTU5ZRLmnbUy7j1B6Psica5i3th_74OwmuL_-njrFIsfHPU2MwGi16A120Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SorkhTimes/135988" target="_blank">📅 01:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135987">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/135987" target="_blank">📅 00:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135986">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/135986" target="_blank">📅 00:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135985">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
کوشکی و اسلامی توسط ترنسفرمارکت بازیکن آزاد اعلام شدند
🔴
از طرفی ایجنت هر ۲ بازیکن با ایجنت جلالی یکیه
👀
نظرتونه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/135985" target="_blank">📅 00:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135984">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/135984" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135983">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
✅
یه خبر نصف شبی فوری، شنیده ها:
🔴
برخی از کارشناسان حقوقی معتبر به باشگاه اطلاع دادن کسری طاهری میتونه برای پرسپولیس بازی کنه و باشگاه داره مجدد واسه جذبش تلاش میکنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/135983" target="_blank">📅 00:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135982">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم : آمریکا رسما حمله به زیرساخت‌های ایرانو آغاز کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/135982" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135981">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
آمریکا پل کهورستان بندر عباس را هدف قرار داد.
🔴
این پل، بندرعباس رو به شهرستان بندر خمیر و سپس به بندرلنگه و سایر شهرهای غرب استان متصل میکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/135981" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135980">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
آمریکا پل کهورستان بندر عباس را هدف قرار داد.
🔴
این پل، بندرعباس رو به شهرستان بندر خمیر و سپس به بندرلنگه و سایر شهرهای غرب استان متصل میکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/135980" target="_blank">📅 00:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135979">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
آمریکا پل ارتباطی بندرعباس و شیراز در جنوب ایران را هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/135979" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135978">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم : آمریکا رسما حمله به زیرساخت‌های ایرانو آغاز کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/135978" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135977">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
فووووووووووووووووری
⏺
ارتش اسراییل: آمریکا در حال نابودی زیرساخت های جنوب ایران است تا به راحتی به آنها حمله زمینی کند و سپس به مرکز ایران برسد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/135977" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135976">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
🚨
حملات در جنوب کشور شروع شده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/135976" target="_blank">📅 00:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135975">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
🔴
موج جدید حملات سنگین آمریکا به جنوب کشور آغاز شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/135975" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135974">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmAlTus75WOFwjwKC3ePAxQ94igaPTJBHZShox072lop2Rq3oW0moN4ETH9sSsbtdZfS7gXK2KvmF8iMvNBlaRJe4ypYbunV5XDas2ys5Mz6oLxf0vjtJS8KxhNVSGbYMy5C1vVoxFoyynlaboNmp7AQPYeGMpkgnEmvcDegtqagEnTT5VwvZUAVetr_p3bFREMWiLjSTC30xv3tqb7XDc5dl3t0DYP3pZjJgUPjJENwYfmFRLfyOMR_jWkUI_y1BiNaZmYCc4IDy-nW-Z0s-QoZHiCqsSOf6hNMs8emG5QEw9dhYg8bMHRainPsKORx7-svbxK7hOE1JavCtVrgHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور رضا جباری در تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/135974" target="_blank">📅 23:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135973">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTFwfa1i9IDryaJfE03IjcGgI3leV5ICBpEVq2F-4-FfjFCchfM-BKf4c8dDimcl1hvSUi6gk64JjqI6DGhOmMycjg88s1ug9Y_483-3JrS-Ct9GQPXaoaBExm-AQQpZN6WX6P1wIhMZx6lFdF6g80MtZqbeyCSa5U2UhEY61VkV4BFvUKSe43FpME_HeWXbuOslRe4PLGu2eq0g6dPdxJH1IW_sgXqyf4XisA7o38kEA8YDcSZH6MFwifDK8Rf7vG2CwLlBKoEz4BnrLXsHedHEhCfpqmzjf8leKWqUm9a0QwyVhrUyH8VIHg2etSF2yobrAYwMNzytD4y-uZcLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش تصویری از تمرین امروز پرسپولیس
با حضور علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/135973" target="_blank">📅 22:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135972">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/135972" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135971">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBMJYUCoB008B2j_lHaplfv9iih5zVVrpU-4bOC3Ex-VsbDwD7glcmt8ZPqKyb4laQ1yYJ92vFyAbjuhiFgIZ8a_uPrm5oBjgaDz1ax4QMLiDe_glCS6xbpJ0CFWooB-xKgmJWabJgwPvDj_mEcaAqYpiOmRJoYjH5IaJFISXDO1XfG8Wjc9PYHANr5BXtrUZ2YKgQA03suHaT9NOygFdxnDlrvWO6UVvYkSIxpdvgJmyLv6_aZIEH9MjCxePwSksEMkHVeyYQxALtKxaIytCMyYKJjq628py5Wppjx6rZ_5riG9ghiye-ohVdseG3vqi0lisYpERuauNpbCv5pw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/135971" target="_blank">📅 22:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135970">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
صنعت نفت آبادان با برتری 2 بر 0 برابر نیروی زمینی در رده سوم جدول رده بندی ایستاد و حریف مس رفسنجان در دیدار پلی آف لیگ برتر شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/135970" target="_blank">📅 22:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135969">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">#شفاف_سازی
🫦
📌
ببینید دوستان لطفا به مطالب جهت دهی شده توجهی نکنید این مطالب رو رفقای اقای زندی میدن بیرون که باشگاه رو تحت فشار بزارن، همونطور که چند روز پیش گفتم و امروز هم اشاره کردم باشگاه خوب نساجی نقدا پول رضایت نامه ایری و طاهری رو پرداخت کرده که بتونن…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/135969" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135968">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">#شفاف_سازی
🫦
📌
ببینید دوستان لطفا به مطالب جهت دهی شده توجهی نکنید این مطالب رو رفقای اقای زندی میدن بیرون که باشگاه رو تحت فشار بزارن، همونطور که چند روز پیش گفتم و امروز هم اشاره کردم باشگاه خوب نساجی نقدا پول رضایت نامه ایری و طاهری رو پرداخت کرده که بتونن با دو سه برابر پرداختی شون به تیم های دیگه بفروشن این دوتا بازیکن رو…الان که باشگاه با علیپور تمدید کرده و زارع رو جذب کرده،مدیران نساجی الان زیرش زاییدن چون سپاهان سقف قراردادش ۴۵ میلیارد هست، استقلال بخره هم الان به کارش نمیاد، فولاد هم بودجش در حد سپاهانه… جز ما و استقلال کسی دنبال ایری و طاهری نبود که بخاد پول خوب بده الان به گوه خوردن افتادن مدیران شون ولی با این تفاوت که الان افتادن تو فضای مجازی و دارن کصشر تلاوت میکنن تا هجمه وارد کنن، بگن ما موز میدادیم کیلویی ۳۰۰ حدادی خیار خرید کیلویی ۲۰۰ اقایون جای این لاشی بازی ها بازیکن رو به قیمت بفروشید که اینجوری قهوه ای نشید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/135968" target="_blank">📅 22:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135967">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
قرارداد علی علیپور تمدید شد
❌
قرارداد علی علیپور، مهاجم باسابقه و ملی‌پوش پرسپولیس، پس از توافق با دکتر پیمان حدادی، مدیرعامل باشگاه، به مدت یک فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135967" target="_blank">📅 20:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135966">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKEF5gFyolum1JOP3Ub-2UoH6Htw6zUC97EpIOEVoJffuAC8SsYvcGHLn5HEzDjcsTAfE-kEBpjAfRnKSv3HTZexMQUjvUopMLty_cQGSRZgVW_dxtvTmE1ttzPirtW_VTfxGG1Ek43-BJ01N_OHd7szYxpfOv5BGp245TPu5N0kDyjfTgPZ5pOE5u7aOSj5SJ0j1DXj9NRpYIsONC5b0bVLoTMMgXjwDWGccFTxHCJJKSykgbazLqnlCMluhgFCr67PEIBhNxidzuIz0CPV7N9GZRxasJXc8Z7UBRLr7japEU2mdS_aAJfHk-v13K-UuPkNW8nvmKzoGuV9M7G5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه پاکستانی
😀
اکسپرس‌تریبیون:
❌
بعد از از بین رفتن تفاهم‌نامه بین آمریکا و ایران، پاکستان تلاش‌های خودشو برای کاهش تنش‌ها و ایجاد صلح بین این دو کشور متوقف کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135966" target="_blank">📅 20:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135965">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/135965" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135964">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/135964" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135963">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcKQrcyjVumGYuT6JAvOoTK64STyVZ_20qIfPMG5IwQFdG-c0QRxOVn-UhXd4V5UHtWMeJKkzxRKQxGgKx4BlSetxJgfWh3b_FtW2IQ1UXNDwagjKrNaLQ38FlMEK__1erRCeJ2dXMKs7VxuX1RvEWaoUAPNk07IUtrd9p7s3ov_oy0hUWYDQoSoFdUZuGG1kfn1CDtmOiOD3XkD0-5u91BuVGoplMZizWb_f41lFqhNLRp3FuRznZPbB4IIzNw-HzCavKz_mPrkpMmH1YbOLJPA4B39fMxYhR7-8_Z-vY-TKBMEC2DKp6VOT3lRaBk37xdh3PWlpxCD8j2i1AzJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/135963" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135962">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyTHCf2mNOFsT3yxXTA7aavxZjcHtBJT_E91Wr3PicUwK3WQsyM4qRKaIryFzuMcXG8u4iWCYT0gjnVB4CENHNw7iQncZRAMXmg2EUM6s208QPYFxrZRz8Erv-U8zVuu5bvXBeq9DkLvZtXCvRx5AB2sapqULWVeCQPN4zmRV7uUggeOxGV1_JRiaEtD5kRF5NuBcFJc_BrSmzPPGjrgKTbYUn7b74RrnWn02rIgSs7VUCF_ZmVZNrNkDLox3YoqJGnDYmhoISkABEiLsnFJ-yiv8IIbCr-ohGinD5RFzjZrgFuuF4V4ZXFJETWs3yIB3roEgEoZqK7d4UR-xO5zwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیم ملی والیبال امروز تو یه بازی جذاب 3-2 مقابل آلمان پیروز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/135962" target="_blank">📅 20:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135961">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
❗️
فووووووووری
❌
فرهیختگان : اگر میلاد محمدی با باشگاه تمدید نکنه ، مدیران باشگاه از مدافع چپ جوونی که با اون به توافق نهایی رسیده‌اند ، رونمایی خواهند کرد
🔴
گفته می‌شود تمام اقدامات نهایی خرید جدید تیم انجام شده و این انتقال برای نهایی شدن تنها به یک امضا…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/135961" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135960">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e071e1ff46.mp4?token=B8eG4mhb300iXezVwD1eURbMZQsoH2wYnXiezzNAJQS9rm7RVwYqzS0jTmoOXMfzgIce_WBTLjc60NhucVHyO81sUwnp7xl4guArF1Zp9SqXn7NvwBOABqMr9kpi04cRGpVVEqQYnENKXpeFcjmkbmSmQc5VetkGZOmSEqfUVskwXae2wyRU09qxsDOJtl2BXvOcp0rse0h95M0XaIuUeY3xwBDo-8asaYzHmT1bBbXZaD5NvY85gdVri42zBp8HY-pnJCGAEpsrlXo3d_lqMGdGLV2CbVyqQNLfnFOAPTGu9TBHM-Gky6nUWDz_pngWNSg5DSbOmg_Lvig5WN5YllD29FbMVNgS4BYPutV2PW8jtl51ZoWWwzyq3VGdbOYlGcRQN2nmVHXsYigEW3UDGhLm1IOwif8yXEvUkxA3ZXU1BUAgobrvgJXyHmXd8zAwONqTvbWqPsEUqh-ljA_P2f0HiWejXW537PxKezgO1ejCWQxYvFTE4QgfEvO9mDXbzlAE2Dwfk1A0Z4ewfu1jr8WAi0gb9Ww6b5KbKJix-jTNqyotLhhs4buQeXSylYMJ_-3ktNuTEJBg5QldBC8t0Z1hByLN0e5cvf0QbH-6QBzlOG4lrzg1cnvu0J8P-HKMq14cGR1p_AShEsMkoMi70aCTEg-CkRLsOxIKSMIQ3zk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e071e1ff46.mp4?token=B8eG4mhb300iXezVwD1eURbMZQsoH2wYnXiezzNAJQS9rm7RVwYqzS0jTmoOXMfzgIce_WBTLjc60NhucVHyO81sUwnp7xl4guArF1Zp9SqXn7NvwBOABqMr9kpi04cRGpVVEqQYnENKXpeFcjmkbmSmQc5VetkGZOmSEqfUVskwXae2wyRU09qxsDOJtl2BXvOcp0rse0h95M0XaIuUeY3xwBDo-8asaYzHmT1bBbXZaD5NvY85gdVri42zBp8HY-pnJCGAEpsrlXo3d_lqMGdGLV2CbVyqQNLfnFOAPTGu9TBHM-Gky6nUWDz_pngWNSg5DSbOmg_Lvig5WN5YllD29FbMVNgS4BYPutV2PW8jtl51ZoWWwzyq3VGdbOYlGcRQN2nmVHXsYigEW3UDGhLm1IOwif8yXEvUkxA3ZXU1BUAgobrvgJXyHmXd8zAwONqTvbWqPsEUqh-ljA_P2f0HiWejXW537PxKezgO1ejCWQxYvFTE4QgfEvO9mDXbzlAE2Dwfk1A0Z4ewfu1jr8WAi0gb9Ww6b5KbKJix-jTNqyotLhhs4buQeXSylYMJ_-3ktNuTEJBg5QldBC8t0Z1hByLN0e5cvf0QbH-6QBzlOG4lrzg1cnvu0J8P-HKMq14cGR1p_AShEsMkoMi70aCTEg-CkRLsOxIKSMIQ3zk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل چند ماه قبل پویا پورعلی به پرسپولیس با پیراهن گل‌گهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135960" target="_blank">📅 19:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135959">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664e6b20c6.mp4?token=YcGvOLFgRKi28I3KI-BNTjeKMD4FrpCljO2fXR2DmB9q8o_u8S_-XBZuAlEZ6gBCLH8x35gOD6RXI1aPKRyt4fkzR9ET1X1ykqkJRhN0qiGN0ES0PHuh852x6M0qU0wvUDTbOdwgNQNaST8ppy5je3pUXDi6wYqDSMdHjjLKKpFqfN1Nwnmmk0_yCW5Nb5DTr0j-eSpFpVJxBHMiqA0KCC2iVJ9OECSLKR96vl0QtsTXC-x1X6nrPm-wSBpdnkT0e2_1BK3pLUDUrzzvYeZV1W5gpgHNTeLukWCnuxraV8VPK-K1hbNINTerswIUgZFf5XswQwo9yro5N36y_RDwIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664e6b20c6.mp4?token=YcGvOLFgRKi28I3KI-BNTjeKMD4FrpCljO2fXR2DmB9q8o_u8S_-XBZuAlEZ6gBCLH8x35gOD6RXI1aPKRyt4fkzR9ET1X1ykqkJRhN0qiGN0ES0PHuh852x6M0qU0wvUDTbOdwgNQNaST8ppy5je3pUXDi6wYqDSMdHjjLKKpFqfN1Nwnmmk0_yCW5Nb5DTr0j-eSpFpVJxBHMiqA0KCC2iVJ9OECSLKR96vl0QtsTXC-x1X6nrPm-wSBpdnkT0e2_1BK3pLUDUrzzvYeZV1W5gpgHNTeLukWCnuxraV8VPK-K1hbNINTerswIUgZFf5XswQwo9yro5N36y_RDwIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب علیرضا، پسر نابینای ایرانی اينجوری با گل آرژانتین ذوق کرد
❤️
🔴
گزارشگر اختصاصی هم داره که پدرشه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/135959" target="_blank">📅 19:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135958">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135958" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135957">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
اردوی خارجی پرسپولیس در آستانه لغو
❗️
❗️
در حالی که تیم فوتبال پرسپولیس قصد دارد روز جمعه تهران را به مقصد ارزروم ترک کند تا یک اردوی دو هفته‌ای را در مسیر آماده‌سازی خود داشته باشد، هنوز شورای برونمرزی وزارت ورزش مجوزهای لازم برای برگزاری این اردو را صادر…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135957" target="_blank">📅 18:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135956">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
ورزش سه: تارتار به وحید امیری پیشنهاد داده به عنوان دستیار و مربی به کادرفنی پرسپولیس اضافه بشه؛ اما امیری فعلا دلش میخواد بازی کنه و دیروزم داخل ترکیب پرسپولیس قرار گرفت تا خودشو به تارتار ثابت کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135956" target="_blank">📅 18:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135955">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eda321934.mp4?token=buoiHGUQNbLJSgu2kKMDDm5_05vN4fldYMriVsiDFDQ-h0sMAkld7dzkH-2JHGhE7p_FujoQTiezIOoe3d_dsDT_kF3KUtQEbCVSW22msnepZoTCiC6n77LB-TN26sldR834MpXjN70q_59eZCcdpd-ljS_w3FrCt1kxgE3tCdEmIgNBNQO4HHrB-zbimOzL_ADihGHXHDX2llzThj18aNA_OCVEGzwG9Hsl7pUMTQOeq3P2HyxMaNRH35YCKy6UVITzI3I0rvkLsqaL_DZuQUSIx3uYiVa50Ax2eK5d0tkSRum7iID4JGuoGbbiCGCreZNLYDxX_AC-IlM_WYPMGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eda321934.mp4?token=buoiHGUQNbLJSgu2kKMDDm5_05vN4fldYMriVsiDFDQ-h0sMAkld7dzkH-2JHGhE7p_FujoQTiezIOoe3d_dsDT_kF3KUtQEbCVSW22msnepZoTCiC6n77LB-TN26sldR834MpXjN70q_59eZCcdpd-ljS_w3FrCt1kxgE3tCdEmIgNBNQO4HHrB-zbimOzL_ADihGHXHDX2llzThj18aNA_OCVEGzwG9Hsl7pUMTQOeq3P2HyxMaNRH35YCKy6UVITzI3I0rvkLsqaL_DZuQUSIx3uYiVa50Ax2eK5d0tkSRum7iID4JGuoGbbiCGCreZNLYDxX_AC-IlM_WYPMGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فوووووووری
:
🔴
ماشاریپوف و نازون از استقلال جدا شدن :)
🔴
پ.ن فقط از استقلال ی سهراب مونده همه رفتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135955" target="_blank">📅 18:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135954">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
✅
اورونوف چهارشنبه‌ وارد ایران خواهد شد.
🔴
پیشنهاد ۳/۵میلیون یورویی الشمال قطر صحت ندارد.پیشنهادی باشد هم با میلغ بسیار کمتری است و از قرارداد مالی او یک میلیون و ۴۰۰ هزار دلاری با پرسپولیس بیشتر نیست/قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135954" target="_blank">📅 17:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135953">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
قدوسی در خبری فوری
❌
احمد نور میخواد برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135953" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135952">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqfH85aJXy9tq-hngdrWafcxPYKo4yxO9R4qHgg7EcvO5oAvUxsRPkLWprDpBVk_Ud2zwPH7A1w26VNk6AtF66p9NKEtrelCepg8S90QGiSaSv-U-kGDNRVOB1lzPsBYmVMqvf73dOr1kq8gC3EMBAbbfqQYgM6-KuMBcWr5iDzCbBi0mJKrAALug-m4FR9uWc46SdQDRTZpzNRsahKia9WW9mYCgmrSUIQpC53Gln_96HM7to1PoepSH9Nk278FcMc0q3FNh__v72MmfJFbT2oGkfVb_TvGFJ_O5Rxo_ZjKiaNWv8NyMh-hlpfiX1vesR9go1LV21UN-3hzLmdatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ابوالفضل جلالی بعد از پیوستن به پرسپولیس یه میلیونی شد
🎉
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135952" target="_blank">📅 17:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135951">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
✅
سامان قدوس در فهرست نقل‌وانتقالات باشگاه پرسپولیس قرار دارد و سرخپوشان به دنبال جذب او برای پست شماره ۱۰ و جایگزینی با رضا شکاری
هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135951" target="_blank">📅 17:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135950">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
شایعات؛ محمدحسین اسلامی در حال مذاکره با پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135950" target="_blank">📅 16:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135949">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
کوشکی و اسلامی توسط ترنسفرمارکت بازیکن آزاد اعلام شدند
🔴
از طرفی ایجنت هر ۲ بازیکن با ایجنت جلالی یکیه
👀
نظرتونه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/135949" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135948">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135948" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135947">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135947" target="_blank">📅 16:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135946">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZUggKjPd7AdwQiXe-0lb1XWWxa3QluuLOGyJXEfRuia-49v_dnEhHFa4c_3fXSLJQj7FkgUrHvV-TYMfsj2p1HSlk4vC89sTvjcTpR1OSkDm93y-aeA1NJJsvCjEQ3P86ngytAuvQfheqxK-_Q2JnjGy_X23QA7T_azYxsv3mhZeIt_Oc24ZJguTRFMz-1Bc2yL8EjaVKTUFtmehkY86OeR4BW8QA97RZKu1ayaUmahL55pZcBlTZj8VRhvgtI5KhafP9BGlBGwOajMW80VPfkGbzxjhk3_LIL_MWK1qOegB4iKIBHMTwp7lHh665-x8Fxsi2gTQJNIpXsBCtzGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ایجنت مرتضی اومده مرتضی رو دوباره به لیست پرسپولیس اضافه کرده ؛ باشگاهم هنوز برای مرتضی پوستر خداحافظی نزده
😑
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/135946" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135944">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj2VLl3glEhawEWtaFD4Fhw2DYiUD0I3rrbkSEKUXeTRuQSwFxtntaFQ2V-X3xzyFIqdyH9kfcep68VoqrD5alQh5hjkiCrSfIwdQ_GtuoklI_UmUeBOCxHY9yEEcffrs3J6QQKkh2KsmPjqD86bten_t0-gyj9YAjjGl-EjfEGrzP_Yx5ARKmcU37tk40qI9fpMzLlXmMYVs4CKof5MZhIrFxo6hom6UHbEfo-XtOMPqhFkn81agys8to1opdBf59iHX4zEHkc0GjszgC3SvQaQwvPm9crbtSnNW7EiYhWTJMlmSzl6x_BRoe9zlUcPc5GltIZqmFUAs64tGpJDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سامان قدوس؛ بمب بعدی پرسپولیس؟
🔴
🔴
ورزش سه: پرسپولیس برای جذب سامان قدوس هافبک ایرانی اتحاد کلباء امارات درخواست داده و این بازیکن در لیست خرید سرخپوشان قرار گرفته است.
🔴
🔴
قدوس که سابقه بازی در لیگ برتر انگلیس با برنتفورد و تیم ملی ایران را دارد، یکی از گزینه‌های جذاب پرسپولیس برای تقویت خط میانی محسوب می‌شود.
🔴
❌
باید دید مذاکرات پرسپولیس با ستاره کلباء به کجا می‌رسد و آیا شاهد یک انتقال بزرگ دیگر به جمع سرخ‌ها خواهیم بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/135944" target="_blank">📅 15:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135943">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
✅
عملکرد پویا پورعلی هافبک دفاعی جدید 30 ساله پرسپولیس در فصل گذشته لیگ برتر :
🔆
21 بازی ، 1 گل / نمره متریکا : 7/03
🔴
سابقه حضور در گل گهر، تراکتور، ملوان، ذوب آهن، فجر سپاسی، خونه به خونه، بادران، شهرداری جویبار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135943" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135941">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abNRloxGndf_snvasInb6FDNVnx2d8QPyK6pxg_xaK2YqsuHKk3q7uVX-IDtapt_8g8cHAOzz4zLOgKmHtOlLp_G1Tfr2-szqw7ns9sJ1fGseWzaJP11PvuS7HTKnY6HPxkAweLxibb5qhEarG3gvFtcLfQba5Gfq7VrlsyoxCB82Kk5v2EzesvGh9qdWoEiuzCloWPjQItPv5E4eaev6SQ1VUDdcN29VTdLF3MlaTJC4ciuYI9MafLVEdh0kbLiIdE7h0elSJLk5MkuwlwAwUZnzfCA8SCHBPBZXa0hSH86QENoWWz9IwpRDtrE9lsZyoUz7PENbgxL6t3NO4KoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
فیفا قضاوت دیدار فینال جام جهانی ۲۰۲۶ میان تیم‌های ملی اسپانیا و آرژانتین را به علیرضا فغانی سپرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135941" target="_blank">📅 15:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135940">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0dw4KDUtBr716mDBZN8KHaLJSm-9Sv1ogQeeTq0iHpVqYR-tUgSRTXmGKxyqRze9ac6d3ccr5AIsbZJMYjja3VfVlS4-yzWH4qhHQ-3C5XUDQN7BOWhUk2GDt2JFeKK4tC4fR6Iu_TRtPcECx4qE1X2GJrk3zUHAhEZNhq8HSEAZRvS02RJnm_Aea3K540VATN_ZYVJEQiwWkNWJ1185PrdtnByhsOBrMF5jRdfwDi0rfZtMVhCGbXKczjyRh9-30dm82CEU7t82qrDsDae56aIWgfoHnYsFSFLM9t1Sg5aWTfIlyAui2srYXmM2s6Qbnnlm_OCc4YImcPlCB0_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز:
مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135940" target="_blank">📅 15:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135939">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙷𝚊𝚓𝙼𝙰𝚑𝚍𝚒</strong></div>
<div class="tg-text">تو دور زمونه ای که فساد حرف اولو میزنه کسی که وظیفشو انجام میده باید قدردان خودشو پدر و مادرش بود...</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135939" target="_blank">📅 15:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135938">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompourya</strong></div>
<div class="tg-text">دیگه نمیتونی زحمات یکی رو بگا بدی خیلیا به وضیفشون عمل نمیکنن</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135938" target="_blank">📅 14:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135937">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وظیفه اشه  دیگه دمت گرم نداره  مثه اینه مادر به بچه اش شیر بده بگیم دمت گرم مادر که به بچه تازه بدنیا اومده شیر میدی
😂</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135937" target="_blank">📅 14:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135936">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahidreza. Sadeghpour</strong></div>
<div class="tg-text">وظیفه اشه
دیگه دمت گرم نداره
مثه اینه مادر به بچه اش شیر بده بگیم دمت گرم مادر که به بچه تازه بدنیا اومده شیر میدی
😂</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135936" target="_blank">📅 14:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135935">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دمت حدادی گرم که باج به شغال نمیدد</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135935" target="_blank">📅 14:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135934">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamed 65442</strong></div>
<div class="tg-text">دمت حدادی گرم که باج به شغال نمیدد</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135934" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135933">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamed 65442</strong></div>
<div class="tg-text">دم بانک شهر گرم</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135933" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135932">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🚨
❤️
پوریا پورعلی با عقد قرارداد دو ساله به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135932" target="_blank">📅 14:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135931">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
🚨
شنیده ها: امروز احتمالا ۲ رونمایی خواهیم داشت
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/135931" target="_blank">📅 14:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135930">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
بااعلام سایت ترانسفر مارکت؛ باشگاه پرسپولیس بابت رضایت‌نامه محمد مهدی زارع 800 هزار دلار به باشگاه اخمت گروژنی روسیه پرداخت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/135930" target="_blank">📅 14:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135929">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn9Ugye2giAlK3I5-nfPJYPDnq0zUAdUNcEb7f7Ky8yv4dnOQq9C1IzR_Rhb-CK3NM8s-5xhpVeVjbMbIPvgIkLJx7XcpeXXJebfmuJfJ8HJn84nfeo-5RHnOFO1pGQpvGxk8-poNFG2Lr5P71DPZGb_43KTCDhlhhyJnz6TnhMFOIr3E0y_dMG2wbJCb_Kq0E81yoCopGZepQiE71GGLaFCS6RMuUQe6Wij17BjFHKEpCatERgPvj3_KU6yntDYITZgeMrH_szc8TGvjQCGL1md-4VZYZar40g4gr2kcVrh63JhySyE02PkbJLcDI-uWw5jCU9l_hypr8B-sFpNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام سایت ترانسفر مارکت؛ باشگاه پرسپولیس بابت رضایت‌نامه محمد مهدی زارع 800 هزار دلار به باشگاه اخمت گروژنی روسیه پرداخت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135929" target="_blank">📅 14:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135928">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMnkAi6m4IV47w5ZD4Bg4XEDKLHHrBHXYjZFqxBj4HC1oaSCWuHXbaHsO3Qh9fKuT55d9B_Vvw78rDyx4kdo1aDK_qRsh3yV-ky_kFUdu15lKldNaqfz9GL8gMFrEoW87wBiywHi1JxtOrmHZMEjqj-SZXu0BVoLNjulo53_YYIEEn75h-RT6emkipK24iWDkL4cuI3gFYcZs3cQrvLlcWf79OLl3K_GSFRJmGFTFTbTC77tckhicXWBncU7GeGDNsGF3HkOg6v8yvq3R_G0gnFRSgzf9F-lvp4TYJvWc0TixnBI30QYMVbsADlLKFqfijlvZtnuanTHmYtAEeDg9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» مدیران باشگاه پرسپولیس با نظر مهدی تارتار با این چهار بازیکن وارد مذاکره شدند.
⬅️
مجید عیدی
⬅️
محمد قیرشی
⬅️
پوریا پورعلی
⬅️
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/135928" target="_blank">📅 14:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135925">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
فوری از فارس:
🔴
انتقال پوریا پورعلی هافبک گل‌گهر به پرسپولیس تا چند ساعت آینده امضا میشه و به زودی رونمایی خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/135925" target="_blank">📅 14:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135924">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
✅
شماره پیراهن خریدهای جدید پرسپولیس
🔴
مهدی تیکدری: شماره 11
🔴
مجید عیدی: شماره 20
🔴
ابوالفضل جلالی: شماره 33
🔴
پوریا شهرآبادی: شماره 21
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135924" target="_blank">📅 14:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135923">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
تمرین امروز سرخپوشان در سالن وزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/135923" target="_blank">📅 14:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135922">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">#تایمز_توئیت
⚠️
تو این مملکت دستت رو عسل بکنی بزاری دهن طرف دستت رو گاز میگیرن، همین زارع رو نمیگرفتن به خدای احد واحد خار مادر باشگاه رو یکی میکردید وسط فصل….
‼️
نساجی برای ایری ۱.۲ میلیون دلار و برای طاهری ۱.۳ میلیون دلار میخاست
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135922" target="_blank">📅 14:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135921">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
❤️
رسمی؛ محمدمهدی زارع به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135921" target="_blank">📅 14:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135919">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmvFRKoaSMZIIFgiAWBjARrzqLAGJHwKdF0E6HgclzzCOnkEhkIHjOBjoDHM4o4xvfnqFlDADtuBKHX0aYEm649CSIDS8Kn-X4AjTzVBWKF6xOrxIdExCol_tcNC_JTCGjJ1VxPXGhl1hjyaBqe639olSFq0oqw5l3oii5xizRsspBq0Njbbx4fsVnQz-SJ3aTk1PjmufzkoX5LXcPWqT5TsuuChVOMVT5jfNrHbAzDMVxacMOY2ThXkG2LH0FTukr20JEAuKjx7-W0kK3VHWj5M62DGW2DkD91qaHAVvbcrDA82BMEQcgkhMYiW8xdeXt6Xpy-NGhhcR72P9jTj5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
❤️
رسمی؛
محمدمهدی زارع به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/135919" target="_blank">📅 14:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135918">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">#تایمز_توئیت
⛔️
❌
با یه مشت دیونه زنجیری طرفیم، باشگاه هرکسی رو میخره یه عده هستن فقط بلندن گوه بخورن
‼️
قبلا میگفتن بانک شهر گداست پول نمیده الان رفتیم یکی از بهترین دفاع وسط های ایران رو خریدیم (زارع) یه عده دهنشون رو باز میکنن که با این پول میشد ایری و طاهری…</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/135918" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135917">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">#تایمز_توئیت
⛔️
❌
با یه مشت دیونه زنجیری طرفیم، باشگاه هرکسی رو میخره یه عده هستن فقط بلندن گوه بخورن
‼️
قبلا میگفتن بانک شهر گداست پول نمیده الان رفتیم یکی از بهترین دفاع وسط های ایران رو خریدیم (زارع) یه عده دهنشون رو باز میکنن که با این پول میشد ایری و طاهری رو خرید یکی نیست اخه کون گلابی اگر میشد مغز خر خوردن برن زارع رو بگیرن ؟! اصلا میشد تو بلدی بیا بکن یه عده فواره گوزو پر مدعا نشستن بیرون میگن لنگش کن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/135917" target="_blank">📅 13:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135916">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
❗️
فرهیختگان : قرار بر این شده است که  باشگاه پرسپولیس قرارداد هافبک مورد علاقه تارتار پوریا پور علی را امشب نهایی کرده تا این بازیکن بتواند از فردا در کنار سرخپوشان تمرین کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/135916" target="_blank">📅 13:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135915">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135915" target="_blank">📅 13:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135914">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
❗️
محمدمهدی زارع در آستانه پرسپولیسی شدن!
⌛
انتقال محمدمهدی زارع ۹۹ درصد نهایی شده و فقط واریز مبلغ باقی مانده است؛ پس از انجام پرداخت، از این خرید به‌صورت رسمی رونمایی خواهد شد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135914" target="_blank">📅 12:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135913">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
مهدی تارتار از مدیران پرسپولیس درخواست کرده با توجه به شانس کم پرسپولیس برای جذب ایری و زارع،اقدام به بازگرداندن مرتضی پورعلی‌گنجی به تمرینات تیم کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135913" target="_blank">📅 12:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135912">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
تارتار شخصاً با زارع تماس گرفته و خواهان اومدنش شده؛ باشگاه هم میخواد از اخمت‌گروژنی تخفیف بگیره/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135912" target="_blank">📅 12:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135911">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
❗️
فووووووووری
❌
فرهیختگان : اگر میلاد محمدی با باشگاه تمدید نکنه ، مدیران باشگاه از مدافع چپ جوونی که با اون به توافق نهایی رسیده‌اند ، رونمایی خواهند کرد
🔴
گفته می‌شود تمام اقدامات نهایی خرید جدید تیم انجام شده و این انتقال برای نهایی شدن تنها به یک امضا…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/135911" target="_blank">📅 10:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135910">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
میلاد محمدی همچنان تمدید نکرده و اخبار قطعی شدنش کذبه اما توافق داشته/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/135910" target="_blank">📅 10:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135909">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
تارتار شخصاً با زارع تماس گرفته و خواهان اومدنش شده؛ باشگاه هم میخواد از اخمت‌گروژنی تخفیف بگیره/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135909" target="_blank">📅 10:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135908">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
#فوووووووری از طاهرخانی :
🔴
زارع در آستانه پرسپولیسی شدن..کار تمومه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/135908" target="_blank">📅 10:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135907">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
✅
یه خبر نصف شبی فوری، شنیده ها:
🔴
برخی از کارشناسان حقوقی معتبر به باشگاه اطلاع دادن کسری طاهری میتونه برای پرسپولیس بازی کنه و باشگاه داره مجدد واسه جذبش تلاش میکنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135907" target="_blank">📅 09:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135906">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
احتمال گرفتن رضایت‌نامه قرضی زارع بیشتره
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/135906" target="_blank">📅 09:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135905">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
حدادی : پول اسکوچیچ رو میدم بازیکن با کیفیت میگیرم
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135905" target="_blank">📅 09:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135904">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
استانداری خوزستان:
🔴
پس از تهاجم دشمن تروریستی آمریکا به شهر اهواز خساراتی به منازل مسکونی اطراف وارد شده و شیشه برخی منازل شکسته شده است.
🔴
تاکنون این حملات تلفات جانی در پی نداشته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/135904" target="_blank">📅 09:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135903">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raFOmxK0I-iQ-FdKHF17__DQ-7sfwv4IVG3trynK10BQKSZfyaeOQHPaDIK6C66nYZGd2zjL95MDyXTg4ZHg2EoTYfM32OrS34Oyx7xL-FKUD5DbivlNW9bW6xBiBbdgpGmfijX7CmELlT_7A258fYMy8BmFA00XNppHe0RsCqxRiFLHsk6Fuxv0N8PkoUgJYDjZ47fJs4PY0Ikq1xCRl7j_7ZxZHbiei8qqm8UELwB06WFXo2dpWJPCNG36KKhcGtHXH4_PB9vw8BdGMkDo95RBU2YLaz-Yi_RUD8Qe8SPTIy0goEEfiVMNcvJmNPOtRHlAzwGsdWjbgueWWuDg1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبح بخیر ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135903" target="_blank">📅 08:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135902">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135902" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135902" target="_blank">📅 02:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135901">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsKcDtIq9JH2zCOZ9h8G54FQN9dZG76-aB4a5CZ2w07LwScRfHAmI7IHOtqR5w1PZAr7VcCRYSfxHsbHNEGWKmnZ4jc8fUPM8K7HLhyS1A0gn9g7i0088LscPrWDNocDFxxzdJagvnF-KCxO87d8dQQxN_JWmAYpi4HrZBrTHf2p3hrIpp4Z6N3ka-e_kPq1yfEwObfoMGxtRl9yCWKhAvMwRqOmXEOLRbb_PwfTn_hX5XAHwQUfDljg1c1T2mioZYbE4UgolzMeR60Rq8DC1KVT4sn6g9IE6bZiep3mN89AC19fkvordZkfO1_NsXNGn8ruBhcDlG6F_z4McN7diA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/135901" target="_blank">📅 02:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135900">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🔴
شهاب زندی مدیرعامل نساجی کسری طاهری رو گول زده و گفته پرسپولیس پولی برای خرید قطعی تو نداره بیا با ما امضا کن تا شرایط رو فراهم کنیم بری پرسپولیس و طاهری هم رفته تفاهم نامه سه جانبه امضا کرده و بعداً فهمیده چه اشتباهی کرده/ فرهیختگان
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/135900" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135899">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
وای چه گل هایی زد آرژانتین ..گل دوم هم زد ..و انگلیس داره می‌ره رده بندی و آرژانتین داره می‌ره فینال ....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/135899" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135898">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
بازی شد یک بر یک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/135898" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135897">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
انگلیس گل اول رو زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/135897" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135896">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
صداوسیما: ساکنان اهواز شدت انفجارها بالاست؛ از خانه‌ها خارج نشوید و تو خونه بمونید.
🔴
+طبق گزارشات شما گفته میشه برخی مناطق رو دستور تخلیه دادن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/135896" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135895">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
❗️
طبق گزارشات مردمی، شدت حملات امشب به اهواز حتی از جنگ ۴۰ روزه هم بیشتر بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/135895" target="_blank">📅 23:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135894">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
نیمه اول چیز خاصی نداشت جز درگیری فقط و تو مخی بودن داور   صفر بر صفر تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135894" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135893">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
فوووووووووووری
❗️
جواد خیایانی: رامین رضاییان به لگانس اسپانیا پیوسته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/135893" target="_blank">📅 23:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135892">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
قاب سنگین امشب
🔥
🔥
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135892" target="_blank">📅 23:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135891">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
⚽️
@Tipster_Mafiaa
@Tipster_Mafiaa
⚽️
@Tipster_Mafiaa
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135891" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135890">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l04-_C2Zl_yin6sn0DYLzQhPkboSTGu0omuN6ghbpTO3TC7QY-5HvaEd5lLDmrbKjKT-1NMacwlPS8wpMOqjcqxk47MwR8zRSXaE_CBDr-huzMTt1sJplGbhNfjpJrCX_uSVwz8TLLZifld7VpZPA7SnIvao7F7pv-5-qR8fiVmvfG9y4Vdc7LjtgCWz-vZJz3BWkBgEFkJv2RkoYvMy4Yf1VOsBQ4KnVDNPGdn2NsItYuY8i2kuM8w7keIy9KPhpeO23IYkb3BImYWieQ_s_K0U5hoIvS_Lak3yMGhDf-PzFOiA0kkqfiAGTImW3ZyU-pgP-OyG1DTQYabgRviDqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135890" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135889">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔹
🔹
آغاز بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135889" target="_blank">📅 23:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135888">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a436b0d04c.mp4?token=tPSvZN8LMU9UaFusnK9JMJr-sEKowelqC3udw3Z5ZqM_Di-XN6_IJT8JrMhlcH03DBukvcdY_V1RC5Hn0TqgdMRebSJTfUdgT4kIi3vybk6IQhoT_fLulBC0AIJOSfyJLYvAz5qKqQraBxXwUCu8Kj9DnqNp-l8CJdOBvxIzqb6CT0Z7cgt3B12DLWXQGILXVm4rTZ51BtZ38jVFUY_2ecQ9hABrd2UJULazxmyt8v-6dTBwVmPq-D2GewO8UNgar1quyUuli1Ibffc8y56v4NGjFYmdRvZv_0vQVBpbdjCuRn0D1TTUF5vH7teAarB2SUp7I5YsRfonKvMbTOIX_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a436b0d04c.mp4?token=tPSvZN8LMU9UaFusnK9JMJr-sEKowelqC3udw3Z5ZqM_Di-XN6_IJT8JrMhlcH03DBukvcdY_V1RC5Hn0TqgdMRebSJTfUdgT4kIi3vybk6IQhoT_fLulBC0AIJOSfyJLYvAz5qKqQraBxXwUCu8Kj9DnqNp-l8CJdOBvxIzqb6CT0Z7cgt3B12DLWXQGILXVm4rTZ51BtZ38jVFUY_2ecQ9hABrd2UJULazxmyt8v-6dTBwVmPq-D2GewO8UNgar1quyUuli1Ibffc8y56v4NGjFYmdRvZv_0vQVBpbdjCuRn0D1TTUF5vH7teAarB2SUp7I5YsRfonKvMbTOIX_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریم باقری: اگه جام جهانی رو 64 تیم میکنن ماهم به عنوان تیم پیشکسوتان تیم بدیم بریم
😂
😂
😂
🔴
+ خنده های علی دایی رو
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135888" target="_blank">📅 23:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135887">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
یاسین سلمانی ماندنی شد
🔴
با نظر مهدی تارتار، هافبک جوان پرسپولیس در جمع سرخ‌ها باقی خواهد ماند و فرصت دارد خودش را در فصل جدید ثابت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/135887" target="_blank">📅 23:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135886">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
#فوری | ترامپ به فاکس نیوز:
❗️
حملات علیه ایران هفته آینده گسترش خواهد یافت و خاورمیانه برای آنچه بعداً رخ خواهد داد آماده میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/135886" target="_blank">📅 23:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135883">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
کی میبره؟
🔹
آرژانتین
❤️
🔹
انگلیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135883" target="_blank">📅 22:31 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
