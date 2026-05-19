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
<img src="https://cdn1.telesco.pe/file/AxHGH008aAcbgTsajHC0-ByfktHnXaKD8ENhbLQSBW0QzOnCnCawtNbgVWCPTMmNupWHtLU2Ev6fyA-B13BUfPcGVWZujrkHH7K03VONH4aVXvZ4jv-e32I4uFWlLONlC_qroNU_GB5mpuVrDRbvB0JeAA7a2-seo2C5P6zHsrS3vXBp1TrFLzaC6-T5qFoYXvvI8FeYQ1NVnw_OaHYs3ZWKtFa1HA1cBbsJWDa_reaXFAm_CwP_ULh_jzR6vG3sFDf7qnf1dD6wBS83PXAcGAxOL7Xb7dSGwpmcC-07sUZhl5nK8h9X7AngFBSUNYTmcFZGv_jjrxB9cJ3O2OSzbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 128K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 یوتوبر انیمه و مانگا(الان کمی شبکه؟!) - برنامه‌نویسِ ایده‌های باحال•YouTube:http://www.youtube.com/@Matin_SenPai•AniList:https://anilist.co/user/MatinSenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 20:16:10</div>
<hr>

<div class="tg-post" id="msg-3200">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mN1DPPFrKikT0NH3ayZ7tTBdbfBmrqJewi6iTxGzAjn41mUAbMn9aIqQDP1TnxJN-itW-mj5ou60Rf3P8WFY2uxGM8Dw-SNsMFAGX2YXTF4p_HZbiHaG11x0c2sEIOCj99164D1xTGOELmSCEtAACiONX-aOidJoJbKTYG2bO6zB3fgfpxfmwPh8n53riIy1NNW_hx-I8b0IgX83sFTc0ObJBzd9BHUZrqVvGK9hnyZuLP4qlDqAMtXUOjnoxIec7JGUUVB9T-DNOQIdImFTbXqPySVwE5GkH-JGJpYryAeCz7FI4-OtGDTM2ZFf8oRM8kWLUc9X3XxmM1YJAK2Y1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر پنجره باز شد، و از کانفیگتون پینگ گرفتید، و -1 داد و اینجا هیچی ننوشت،
یا مجدد، WinError6 داد و بازم -1 گرفتید، یعنی اسپوف با این کانفیگ json(hcaptcha) روی اپراتور سرویس‌دهنده‌ی اینترنت شما بسته هستش</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/MatinSenPaii/3200" target="_blank">📅 20:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3199">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آیپی‌ای که اینجا بهتون میده، صد درصد کار میکنه روی شیر و خورشید و MahsaNG
❤️</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/3199" target="_blank">📅 17:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3198">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j0nv7N92tHvzJoYYQu89Sqm9hjaNiZjUW3zZdici3R6PDxjPsxu-hXqc1V1_cBHMGlPGSGISPwt5Yn9iu6oM71NJLu3mZTudMifJ83ZT6F5S9VBBoF261bLXabtggssIpqQFwBKpmUa8KR61kG48SOBMUi4_r8V-BmA_IjOnXkKw-ARe5-n3j8adQ-r58bNJtfOu425BiZHtGwWFqO56XCh4UfaGX9R7det6UgS6WUqXuBfb9Z-TnD0IrVgSnSgskE58KXLHPltlIPfyS2th4JLgr_2MxjrqPqMnMIKxPmtKNpUSte3rw3wyBQ6yy2nQyw89NIUjFRhyzUGCeV7n-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ رو هم چک کنید، اسکنر برای Akamai و کاربردی برای شیر و خورشیده https://github.com/mirarr-app/network-checker</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/3198" target="_blank">📅 17:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3195">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tsT3wJnpvUVePAgs8I5Nsfr35RtdnNytJtCOMK8SoDkb9aXZNvP9Fwka3JalIQjblbX1tLzVZch4bbN4CuKuzQNZzmxnG7GO8-xMOQJ9c3WSK73R8pzi2ObxiUALwWO6gKyNMW8K8JBamTLng0pYRABL1syfsTy2FS8XvUjq6giue8LvbTEgXCLp-ggXH3cSdubXrdvfqRcqEK1JJoQe5Eg35eshKSYU9endxa_iEHV7yIGZ36Mqy3jLb9rczfI_woZ6dyeW3NrD1l5d1N5gv6QXYeEq6a1_j8Aaz7uXaqbhqvAAfsCjQW_6bLjKXctBVxG4IDAKKYjo5HlPj4FgdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/3195" target="_blank">📅 15:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3194">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دقت کنید، اگر خود Spoof لاگ داره
و V2ray هم لاگ داره اما پینگا -1 هستن همچنان
یعنی مشکل از اپراتوره. اپراتورتون رو عوض کنید و با هرچی سیمکارت توی خونه دارید تست کنید. روی اینترنت خونگی هم به کرات دیدم توی طیف وسیع‌تری پاسخگو هستش</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/3194" target="_blank">📅 15:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3193">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">V3-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3193" target="_blank">📅 14:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3192">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V717aMQyF1SfgpYi9WPRH_uBNwDB14_tJvoD8QO00Aac49M06i1TI6XtqYx60O2kVRu3KZ-cAOo-Abj5cF7WJSfRO6WzFZ9oBXUxRo3Lx62v2hGzVFGmMyYM2__8vq04nFB_Xdqt2OnlQX_w_Qv2iMwOAP1iTHH4gTiNN8qHVGmpJ1ypEh04UxYwGunGDzTXV9AvZ1gqwPBpsow_XAVy1CoxgZ0W8ImPn5FQiDPZtDVYDn8fWpzXwB4QqMLzz9613dPATsWf5aeA1AQGIvj9_-cFe6B1DP7WkzK2npMmK7vAmOuGZ80SPsEybM6Cknt8bm_zGzx6FUSX20MXPQdt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا داریم قله‌های پیشرفت رو فتح میکنیم</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3192" target="_blank">📅 13:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3191">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یکی از دوستان گفتش که روی آسیاتک، خود hcaptcha پینگ نمیده اما کانفیگ‌ها وصلن روی Spoof
یعنی json شما باید همون hcaptcha باشه، خیلی عادی ران میکنید و پینگ میگیرید و بعدش کانفیگ‌ها بهتون پینگ میدن.
راهنمای کامل</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3191" target="_blank">📅 12:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3190">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9a90f10d4b.mp4?token=kitKIb3wn2oIcP2pHZMhHTcrIp_AI_HXvLS78bcid_KDoa70wFGpXVL3Iuxts5FC0e3PFolAEk2lTtczz-d9AUxuXcHs20i148E_IrG4TSmJuIpBdl3A7hNuUP_-8xUzEewZ5qc3RosKhY4tN9gHXU0ucEVmOWnvpT6rDICCrXjHpaptKU4LfoPYM2fbJT4Rz7BxHupl5Srfhcf5QkAk3oGL3aBZDHNx3nKpJiV01hzw1ricjN2V6Q5iLOFrgz6B_Ux6IL2Cfh0KKihUJc5VsIfCTQWo9jN3KdDqEU05gAdH27qBJyky4eI25t0SGhlB0otK3xXdm4uhT4Ra_MUaGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9a90f10d4b.mp4?token=kitKIb3wn2oIcP2pHZMhHTcrIp_AI_HXvLS78bcid_KDoa70wFGpXVL3Iuxts5FC0e3PFolAEk2lTtczz-d9AUxuXcHs20i148E_IrG4TSmJuIpBdl3A7hNuUP_-8xUzEewZ5qc3RosKhY4tN9gHXU0ucEVmOWnvpT6rDICCrXjHpaptKU4LfoPYM2fbJT4Rz7BxHupl5Srfhcf5QkAk3oGL3aBZDHNx3nKpJiV01hzw1ricjN2V6Q5iLOFrgz6B_Ux6IL2Cfh0KKihUJc5VsIfCTQWo9jN3KdDqEU05gAdH27qBJyky4eI25t0SGhlB0otK3xXdm4uhT4Ra_MUaGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3190" target="_blank">📅 11:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3189">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✍️
سؤالات متداول راجب SNI-Spoof:
1- ارور WinError2 میگیرم توی اپ؟
این ارور به این معنیه که شما نرم‌افزار رو با Run as Administor ران نکردید. اگر مطمئنید که این کار رو کردید و باز هم این اروره رو میگیرید، به سادگی یک بار ببندید و مجددا باز کنید.
2- ارور WinError6 میگیرم توی اپ؟
این طبیعیه کاملا. باید هم بگیرید. اصلا اگر این رو نگیرید یعنی کانفیگتون کار نمیکنه. همینجوری پشت سر هم تکرار میشه و این اوکیه. مشکلی هم نیست
3- پس اگر ارور WinError6 میگیرم یعنی وصله؟
نه لزوما. ممکنه همچنان Hcaptcha روی اپراتورتون بسته باشه. پینگ هم بده اما کانفیگا -1 بدن بهتون با اینکه WinError6 هم میگیرید. با اپراتور دیگه‌ای امتحان کنید.
4- اگر
Hcaptcha.com
بهم پینگ بده توی ترمینال یعنی وصله قطعا؟
نه لزوما. توی سؤال قبلی عرض کردم
5- اگر
Hcaptcha.com
بهم پینگ نده توی ترمینال یعنی قطعه و کار نمیکنه؟
نه لزوما. توی یه برهه‌ای Hcaptcha پینگ هم نمیداد اما وقتی با اپ پترنیها ران میکردیم، کانفیگ‌هامون پینگ میداد
6- با چه اپراتوری بهتر جواب میگیرم؟
منطقه به منطقه فرق داره. همراه اول به طور مثال یه جا وصله، یه جا قطع. اکثر اپراتورهایی که دیدم وصل باشن، ایرانسل و سامانتل و رایتل و فیبر مخابرات و مبین نت بودش و adsl خونگی
7- کی این متد رو میبندن؟
به قول یکی از بچه‌ها هروقت ثبت نام ایران‌خودرو تموم شد:))
اصلا مشخص نیست کی میبندن و چرا باز شده و...
اما تا وصل هستش کارهای ضروریتون رو برسید لطفا. آپدیت‌های سیستم عامل و...
فقط روی اندروید حواستون باشه سیستم عاملتون نیاز به لاگین نداشته باشه بعد از آپدیت
8- دقت کنید، اگر خود Spoof لاگ داره
و V2ray هم لاگ داره اما پینگا -1 هستن همچنان
یعنی مشکل از اپراتوره. اپراتورتون رو عوض کنید و با هرچی سیمکارت توی خونه دارید تست کنید. روی اینترنت خونگی هم به کرات دیدم توی طیف وسیع‌تری پاسخگو هستش</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/MatinSenPaii/3189" target="_blank">📅 11:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3188">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y1zKh_tN82lOsJdFeAI8GV-Tw_5byMgbViaZEBAy2jvwOrfJKr6WbuwmyvWnIG68uQD_CC83pLgypu-xnFj6Ss9RPsCPtrqP7DEh7vsPMua2Do_NJKwq43d7VwfUct6eFRiQaGY-p6oAlf6_E32HLPcZbMEmaSbywOMO4nM-PMe0xqpfprED-R-Ir3xm-BCtq05Xwn8Y16cI-r2Ao-Kq4E1Y1CccX6SiC53yXXIU8nS2fw1du4cGzMkOI4-tanHgnHjbejE8VyeJNVEQpouFZ2JqK0BSOsfqSw-TeYX2TvAcoveE_93CSwMJ54N8atIn7JAQa1chSmmpFAVErxHkNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)))))))))))))))))))</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3188" target="_blank">📅 10:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3187">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">Matin SenPai
pinned «
⭐️
کمی مرتب کردن مطالب برای دسترسی به اینترنت آزاد با SNI-Spoof:  1- آموزش پایه: https://t.me/MatinSenPaii/2627 2- آموزش پایه رو که دیدید، بفرمایید از این json استفاده کنید: https://t.me/MatinSenPaii/3168 3- و کانفیگ‌های این پست: https://t.me/MatinSenPaii/3183…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3187" target="_blank">📅 10:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3186">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شاید شبیه کلاهبردارا به نظر برسم اما می‌خوای نامحدود به اینترنت آزاد وصل بشیییییییی؟
😂</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/MatinSenPaii/3186" target="_blank">📅 10:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3184">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fbv2xj0t7suwRiyxGYN5TOeTTmDwFjESZrALqwBODz1IspWiyyESZ1E6bMhMwb3IxXXOV2IfBIjdKmffiqzXM9EiL6WWsJhvdXWQAi2p7PpmfZL9X1eu8sCgOzbqXNRxpH079rgD0sD6aYb3_yOY1fzOhUxKIfxhyDSQkfZzMFkEUVbw_TCI3xYlBR49BnECJCV6XSbvi4Be387PBwvzWNVsruuffvnQggLJJMLsAjFPNlxNNLHS72SutpYaT4zpn8gmsnNbjkvcZJRG-8o_MO515mYYmYX1J2XZwRaLxpzi2TKDH4wt1c1Fj4a_AICs0qlnsRxiN7SJRmRv4Ss9cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ULQmufkvPDGojuZejYbmTXUwHGctrb6F8ZYsHMc8l0iJHUMZN75REPi9XZyeEXLysJJfVrpljYlxwq4hM1-x1ogL9plWsgT0d_AHkGewW59CSElQ29UKG5dpcUP9TJ7gFXJYt_gqYcZHmzPj4REX845G9l0D3AoAfrxtXdm1V_kSK_gybCfH_KIJf088VkHX-aQz8HqsVTzpDrT4M2Kc2xYh4NSTUvowOzyuBcgyrEV8DeHvAD5i9VvQKy3r-Vsiwap4MZcy1Fhw5xT2-uNjwE1EtEHOCqq36rTYFV4COd5hrDjKyBdyMZRicsNZbC_XQBvMTASyilzGY5FZMcDrbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاید شبیه کلاهبردارا به نظر برسم اما می‌خوای نامحدود به اینترنت آزاد وصل بشیییییییی؟
😂</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3184" target="_blank">📅 10:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3183">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V3-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 40 تایی کانفیگ‌های ویژه‌ی متد SNI-Spoof که از سرتاسر تلگرام جمع‌آوری شده و همه هم پینگ میدن</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/MatinSenPaii/3183" target="_blank">📅 10:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3182">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اگه spoof وصل بمونه یه هفته قیمت کانفیگ به زیر گیگی 10 هزار تومن سقوط میکنه
😂
این خط و این نشون</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3182" target="_blank">📅 10:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3181">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خب دوستان نتم رو کردم ایرانسل مجددا متصل شد
همراه اول و شاتل برای منطقه من جواب نمیده</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/3181" target="_blank">📅 09:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3180">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">☠️
آموزش روش جدید و قدرتمند SNI Spoofing - اتصال رایگان و بدون هزینه به اینترنت آزاد!   دانلود فایل نرم افزار: https://t.me/MatinSenPaii/2617 آموزش edge tunnel روی کلودفلر: https://youtu.be/svYBcv4bSzo   توی این ویدیو آموزش کامل و قدم‌به‌قدم می‌دم که چطور بتونید…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3180" target="_blank">📅 09:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3179">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GgWVhsyAUkxVy6rKdt_OkRO_hKHfVsMZg0IIfys0GQ5Oe5TSjhZ1xSCHTk4qLjwq6zUKWAhKD2_YtEMtXPoAuAcH7hewWFcg6f3BzgfVrnoiUshHIh2Vtz2T_sXjuQH2I0V4zPzetJH5gtNEgMZ_xdZaydVTpMzrlCERzqbn09PQ6M7M-Ma-SHiiUtb8AK0JXXLg6UgHr-H-h-Y6wXEBCvxgY4Te2eGbdMGYnSp28vili711k7Cu0UCTri3f46NWOKhMKozhc1pcBq-T4678cqDRus3YJYSonkv5xAwxdLG_y-ZZhCub1Smsqtv-KdPO-KzACUe9YeSlWowHkLUAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Kharabam
:
اگر hcaptcha بهتون پینگ میده اما هیچ کانفیگی هیچ جوره وصل نمیشه، علتش اینه که هنوز پشت NAT هستید.
حالا چطوری مطمئن بشیم؟
اینو چک کنید اگه IP خودتون رو نوشته بود یعنی باید وصل بشه و مشکل یه جا دیگس
hcaptcha.com/cdn-cgi/trace
‎
و اگه IP خودتون نبود یعنی هنوز پشت NAT هستید.</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3179" target="_blank">📅 08:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3178">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">همچنان وصلید؟</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3178" target="_blank">📅 03:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3177">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینور کلا تعطیل شد آپدیتی چیزی دارید سریع انجام بدید</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3177" target="_blank">📅 03:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3176">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YL-TXEufqqXlIspNSsX2gdedSYZvrGFaeOAHzG2lMRp0THYIUddHhZORujGtwDyQdQ62jLXHVZy_PC5KiOY7hUi5sjlFIZwZqDj4YMWRQhlF_eYGjSM8W3WhbxKknmgiJHw6RgZo_1_8JrjC-liBfYsFSRqDi8wUa6yFw05JJTATBOARiotazURh7l8hZVDTC2bx3rO0foA0w8MrpHBPAOljY22ZYv7rNODVTh5UTfLOvvH0Mf7bxL1OUNuXoai5Jotn-thhornbIFCtDXXifqd3_lX3rHjzL5H6L-HrniUllL64CWm78vV-YARrQ9G61SlzMUVB8_CTfHDkGHVzXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینور کلا تعطیل شد
آپدیتی چیزی دارید سریع انجام بدید</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3176" target="_blank">📅 02:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3174">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Spoof-SNI-Configs-List-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">12.5 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3174" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">هرچی کانفیگ ویژه‌ی SNI Spoof با پورت 40443 بود واستون جمع کردم از کانفیگای خودم و بچه‌ها و هرچیزی که توی کانال‌ها گذاشتن، توی این فایل txt واستون قرار دادم</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/3174" target="_blank">📅 02:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3173">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">با این کانفیگ‌ها تست کنید:
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&type=ws&host=www.creationlong.org&path=%2Fassignment#1
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?encryption=none&security=tls&sni=sni.111000.indevs.in&fp=chrome&type=ws&host=sni.111000.indevs.in&path=%2F#2</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3173" target="_blank">📅 02:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3172">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یکی از دوستان توییتر گفته تامکت به قید وثیقه سنگین آزاد شده. امیدوارم که درست باشه این خبر
🔥</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/3172" target="_blank">📅 02:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3171">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">Matin SenPai
pinned «
انگار که واسه‌ی یه سری از دوستان، SNI SPOOF مجددا باز شده. ویدئوش اینجاست: https://t.me/MatinSenPaii/2627 جیسونش هم این: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "104.19.229.21",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com"…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3171" target="_blank">📅 02:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3170">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nkub6-57DQYH_MqLcN0_xYH8GCYrgSqumdFvW_hZ5XpTHCQqz57VcjVAqq2ytld5_HtepfamFytvQto8BVpB-TVDj22mLapjy6RjnsbQh--4kH25l0_1xq9g1y82_9udl174XKzOBnl5YJR89joVf6DMJkdBJll6RxAZ9DAUIUnmCuNA08lDjVcGBGblEgCohW16gxdtDhDsOYCeDyAbk8RrvrOkxr3S9C98oBqKzU9cMmCkyatSAD__R3lI4Zo3wKEFSKtFl7n5-jJifN_9iDpitWTOFj6m_kmkM43-cHzFbMaZt0UC78h6vqmY6mHu1bOXavqxhQ0Ffx4ULlQmcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها واسم فرستاده از اسپوف
برید ببینم چه می‌کنید</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/3170" target="_blank">📅 01:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3169">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انگار که واسه‌ی یه سری از دوستان، SNI SPOOF مجددا باز شده. ویدئوش اینجاست: https://t.me/MatinSenPaii/2627 جیسونش هم این: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "104.19.229.21",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com"…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3169" target="_blank">📅 01:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3168">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انگار که واسه‌ی یه سری از دوستان، SNI SPOOF مجددا باز شده. ویدئوش اینجاست:
https://t.me/MatinSenPaii/2627
جیسونش هم این:
{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
www.hcaptcha.com
"
}
پینگ بگیرید ممکنه به جای 229، 230 نیاز باشه بذارید</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/MatinSenPaii/3168" target="_blank">📅 01:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3167">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">thefeed-android-v0.18.10-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3167" target="_blank">📅 01:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3166">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مجددا، از تمام کسایی که استار میزنن زیر پست‌ها و یا دونیت‌های کوچیک و بزرگ می‌کنن تشکر می‌کنم. من قدردان همه‌تون هستم
❤️</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3166" target="_blank">📅 23:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3165">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">Matin SenPai
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3165" target="_blank">📅 23:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3164">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://guardts.ir/f/19995aceb6bb…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3164" target="_blank">📅 23:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3163">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k0RWgTvpesaY_JmCyjt69J3ucgcebBVWnJs9Be0pX7G6Tju7eB8gCYLN30frwevrjpUNvUFqiC0UtcZDSGUXgNTBrOYlgCOw7NW43AB4ljh529gkymRuHpmrM8G9mAriZ_u7X6byHKYDrNj06Y-D61TCMVAWWBx-bw9H6Gc553UA3ZdCpggSCS4RoC45bn_joBhYKp-PlUH6BrdHBi3u3zJQnRdJ3mcvJPL3sy0i1Tlf8pwHE1F6g6EicfStvfvayy4ZMSK07upDm-vAPJzepg0L8GPWzHtLuU7_AxbFEHhWQ0KK9lUgUe28v7qDBIag-TxG3u98_7-WPeg5BAfbqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای میت، من با گوشی و لپ تاپ خودم روی دوتا جیمیل چک کردم و تماس برقرار شد و همون صدای Echo گوش‌خراش معروف میکروفون هم بین گوشی و لپ رد و بدل شد. نمیدونم چرا برای این دوستمون جواب نداده</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3163" target="_blank">📅 23:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3162">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">MITM-DomainFronting.json</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/3162" target="_blank">📅 23:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3161">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3161" target="_blank">📅 23:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3160">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting.json</div>
  <div class="tg-doc-extra">17.1 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3160" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ورژن 20 اومد چهل دقیقه پیش(توی ویدئو ورژن 19 استفاده شده بود)
و روی این ورژن،
Github.com
هم باز میشه به راحتی</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3160" target="_blank">📅 23:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3157">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">moein.bpf</div>
  <div class="tg-doc-extra">4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3157" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یکی از دوستان این رو دادش:
این برا سینگ باکسه اپ ها هم میاره یعنی لازم نی از مثلا سایت گوگل میت استفاده کنی با اپش میری</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/3157" target="_blank">📅 22:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3156">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">متأسفانه جمنای و گوگل کولب باز نمیشن چون ما تحریم هستیم. یعنی از خارج تحریم هستیم</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/MatinSenPaii/3156" target="_blank">📅 22:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3154">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">با تشکر از
@patterniha
، برنامه‌نویس پروژه، علت ضبط این ویدئو اول این بودش که مقدمه‌ای باشه بر روشی که برای یوتوب می‌خوام بگم، دوما این بودش که حس کردم این پروژه به اندازه‌ی کافی دیده نشده.</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/3154" target="_blank">📅 21:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3152">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">certificate_generator.bat</div>
  <div class="tg-doc-extra">56 B</div>
</div>
<a href="https://t.me/MatinSenPaii/3152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلهای سرتیفیکیت جنریتور(ویژه ویندوز)
و
کانفیگ MITM (ویژه اندروید و ویندوز)
لینک گیتهاب پروژه:
https://github.com/patterniha/MITM-DomainFronting
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3152" target="_blank">📅 21:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3151">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود
این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.
لینک داخلی ویدئو:
https://guardts.ir/f/19995aceb6bb
لینک داخلی V2rayNG:
https://guardts.ir/f/7ae1503cd755
https://c224731.parspack.net/c224731/v2/v2rayNG_arm64-v8a_v2.1.7.apk
لینک داخلی V2rayN:
https://c147793.parspack.net/c147793/v2rayN_windows64_v7.20.2.zip
⚡️
لینک پروژه اصلی:
https://github.com/patterniha/MITM-DomainFronting
لینک سایت Regery برای سرتیفیکیت جداگانه روی اندروید:
https://regery.com/en/security/ssl-tools/self-signed-certificate-generator
لینک فایل‌های مورد نیاز:
https://t.me/MatinSenPaii/3152
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از متد MITM، تحریم سرویس‌های گوگل رو دور بزنید.
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
💰
دونیت</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3151" target="_blank">📅 21:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3150">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یکی از دوستان توییتر گفته تامکت به قید وثیقه سنگین آزاد شده. امیدوارم که درست باشه این خبر
🔥</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/3150" target="_blank">📅 21:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3149">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عالی بود
تمام 133.9 کیلوبایتی که برای این ویس دادم ارزششو داشت
🤣
🤣</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/3149" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3148">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirmohammad</strong></div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3148" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3147">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">rdnbenet-windows.zip</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3147" target="_blank">📅 19:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3146">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W0sQhDQktlI8AyoWl5olzkns6iNwE-fWMWUTeAtWNb5_WTwSvpuPdLoNE6JeOhGxjgHaap54cRMhBzEH4wkAbdW8aYJg42hiWAORRHIVkDdxjzLYSKRA08JW6dICw6VuO_ywgYJ1uW9zdYTSY2bf80WiX_QOCcCOIVAO35jowpLHQRfFmLe-N2jS-mMJUTMFA3UhbHIIv9BJ7Wd36iy8iz_3z6E5o1Yu8WuSrLfNcpQgaGr3820YgVs8I66c50i8q3joXKe74wTq0xWqHTWhVsSA4Fsvj1LDLVlGeLhTeeQtxWbZYPGaobGhPk6Cwk_z3JUdg8ns6a2a8R3pTa8v7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه متد یوتوبه زیاد ساده نیست، اما خب قابل تحمله و زیاد هم پیچیده نیست. اون شکلی نیست که بتونید راحت برید توی یوتوب بچرخید، اما خب محدودیت حجمی و... هم نداره.</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3146" target="_blank">📅 19:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3145">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رفقا متد بله رو چندتا از دوستای متخصص توصیه کردن که اصلا نه انجام بدیم نه من آموزشش رو بدم. بر پایه‌ی سروش هم یکی الان دیدم نوشته بود و واسم فرستاده بودین. چون حتی سر متدای ارسال فایل هم اکانت یه سری از بچه‌ها بسته شده بود توی روبیکا و بله</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3145" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3144">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خب با این اوصاف من آموزشه رو می‌ذارم. چیز پیچیده‌ای هم نیست اصلا
دوتا ویدئوی مجزا میشه اما چون خلاف قوانین یوتوبه فقط اینجا می‌ذارم</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3144" target="_blank">📅 17:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3143">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-poll">
<h4>📊 اینایی که میزنن دیدن نتایج ایران نیستن یا حال ندارن چک کنن؟</h4>
<ul>
<li>✓ ایران نیستم</li>
<li>✓ ایرانم. حال ندارم چک کنم</li>
<li>✓ دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3143" target="_blank">📅 17:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3141">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-poll">
<h4>📊 بفرمایید که،</h4>
<ul>
<li>✓ meet و drive بسته‌ان یا یکیش بسته‌ست❌</li>
<li>✓ هر دو واسم بالا میان راحت✅</li>
<li>✓ دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/3141" target="_blank">📅 17:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3138">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گوگل میت چی؟ :)</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3138" target="_blank">📅 17:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3137">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nNOR-0C5YHXvkdc-v3hQ1d62abciT6LyFZKgEB8b4rR-kGmPaMpeMjA_aRHX3UfLZBNpfzZ4vGGsmbhfyV32OPX3KrWG2qP6_GP9c2py1wx3KJvYAHm8eoAtWo16PMvzFKQTxEI9Zg-pf9cZEd3-fl67TOth2uAMZt7fvbGjsZ6iPuTZi1YUYhLAhmAN_eRBvA2tfPY_Kz3UvTd9Tfo_OY4taX9sEJeE6EQjjT1O1zkvup3_nrW-1F2VpIIJ2EFtumY9LNz-WjBMVZgpZ1hme9EJg7GIEQJn7K6wqwOGjqg0qNLHZYjlZl28QKQP6V5TEVBayAe5Uw74uuZRdyv5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان، drive.google.com روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3137" target="_blank">📅 17:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3136">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دوستان، drive.google.com روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3136" target="_blank">📅 17:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3135">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوستان،
drive.google.com
روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3135" target="_blank">📅 16:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3134">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بذارید بگم که چرا از زبان پایتون خسته شدم برای توسعه‌ی Back-End:
اول از همه، magic methodهای افتضاحش. یعنی هی باید __init__،__ str__،__ repr__، __add__، __getitem__ و هزارتای دیگه رو یادت باشه. که این باعث میشه هی دست به دامن ai بشی. و همینطور باعث اینکه خیلی وقتا نفهمی  چی داره پشت صحنه اتفاق می‌افته. یه operator ساده می‌نویسی، و یه magic method جادویی صدا زده می‌شه که اصلاً معلوم نیست کجاست. وقتی می‌خوای دیباگ کنی، باید بری دنبال این متدهای مخفی قبیله‌ی برگ(!) بگردی. و کلاً خیلی implicit و غیرشفافه.
دوم اینکه اینترپرتری یا مفسریه. یعنی خط به خط اجرا می‌شه. تا نرسه به خط ۲۰۰، نمی‌فهمی اون خط مشکل داره. باید کل برنامه رو ران کنی تا به اون خط برسه و بعد بفهمی "آها، اینجا یه typo داشتم" یا "این متغیر تعریف نشده بوده". یعنی عملا یه کد بیس بالای 5 هزار خط پیرت میکنه. از اون طرف توی زبان‌های کامپایلری مثل Go یا Rust، قبل از اجرا خود compiler همه‌چیز رو چک می‌کنه و بهت می‌گه کجاش اشتباهه. همه‌ی ارورا، یک جا. ولی توی پایتون باید خودت خط به خط بری و ارورا پیدا کنی.
سوم اینکه type safety نداره. یعنی یه متغیر الان string هست، یک ساعت دیگه int می‌شه، بعدش list می‌شه. تو runtime متوجه می‌شی که "اوه، اینجا یه list بود و برنامه کرش کرد". Type hintها هم که فقط تزئینین، اجباری نیستن و موقع runtime چک نمی‌شن.
چهارم اینکه performance خیلی ضعیفه. برای یه API ساده که ترافیک بالا داشته باشه، باید چندتا سرور بزنی بره بالا. حالا همون کار رو با Go بنویسی، با یه سرور راه می‌افته.
پنجم، dependency management و packaging اش یه فاجعست. pip، virtualenv، conda، poetry، pipenv... هرکس یه سازی میزنه برا خودش و شما باید به اون ساز برقصی. requirements.txt هم که دچار conflict میشه خیلی وقتا. Python 2 هم هنوز توی یه سری از پروژه‌ها هست که تبدیل کردنش بدبختیه.
خلاصه اینکه پایتون برای scriptهای کوچیک و زمینه‌ی هوش مصنوعی و ماشین لرنینگ خوبه، ولی برای production backend واقعاً اعصاب خورد ‌کنه. و من رفتم سراغ یه زبان compile شده که از همون اول بگه کجا اشتباه کردم، نه اینکه وسط شب production کرش کنه. مثل گولنگ یا حداقل حداقل تایپ‌اسکریپت.</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/3134" target="_blank">📅 16:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3133">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">WhiteDNS-1.5.0-x86.apk</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/3133" target="_blank">📅 14:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3128">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3128" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر از مطمین نیستید، ورژن یونیورسال رو دانلود بکنید.</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/3128" target="_blank">📅 14:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3127">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t5fj9xdlbfgqqAEzjySFKVmjQSR35tjSlfuwntqlA1EtHEcPvvHpAM9mkjO-L7Dx5WZbem9c7fLr2uZ5qixPQauw3Mas-eD4FpXB55qxKQwrUX3URyNbx9dNkzhvuDc9OVTdfvDXRtp8uK-RCBONcAX3vTNv1Vnveqea0oldWTvkLlCaK5oW_QtkiEJy3tGb6hOQapTuDl1OK6fi9flOkyUNuOtbNjH7s1puEVb_2-52liXDnW5gCW2FjXOsfBXfh1-zn1GF7TCfiJZfAdzKhmtS97m4ipvtJCv6S1Q9wvD4c9pCtmnUyITFv6mGfdSsLRlu53LCwvsSHqjm_OWG0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچین موردهایی رو زیاد واسم میفرستید دوستان. مسئله‌ای نیست؛ من که چیزی رو اختراع نکردم که زده باشن به اسم خودشون
😁
صرفا زحمت جمع‌آوریش رو کشیدم. منبع هم نذاشته، نذاشته. مهم نیست که.  هدف، وصل شدن مردمه</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3127" target="_blank">📅 12:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3126">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">با گوشی هم میتونید باز کنید دیگه اون Index رو
یکی توییتر پرسیده بودش</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/3126" target="_blank">📅 12:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3125">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یه چیز جالب توجهی پیدا کردم که راجبش ویدئو بسازم. به درد خیلیا میخوره
ترکیب یه متد حال حاضر هست، با یه سایتی که اصلا هیچکس نمیشناسه. انقدر گشتم که پیدا کردم
برای VPN نیستش. برای دسترسی رایگان به محتوای یوتوبه
سر کار هستم الان، تموم که شدم واستون ویدئوش رو میگیرم</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3125" target="_blank">📅 11:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3123">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fy4UrSmaYmnl36nqZNQ9A7Rr4asUeq_sgGdS4HKiz48D13-fT6BXFX_nWRoZl00vfMlAIVhvVln0IWWUEfpJZxtzXa2izP7vMa3xmqsdCP36Ils-QTdIljyPPC5yF8qruJ3ne5yFLJxGH8oYatuBpo0oS9zU5dqVJWRnBoLrT0XlXcrjspTo9sknRKCt_Hxm_PVgJRpKboLlVzDJqnH2Q0b7MXmLnfU21E6fK-hqvPUOCASxXd74YuUw_wNM0cL6MtT6UBcNVNWL1oaL7mFK6KdDOYhvXXRt5knnLIN61MsOKv3uEta7jfb2mol6Nfp5_q7QZ3-mhs4b8qRNl1fmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SDKvJ8HasnlDWrkRCluaTvTb9xXMUqSHrUkh1ivZcNjCbhoHyNkVtpN09k3Pc76Wcb8wOMDnWFe0HLHrjDPF8jhMJ3tf5nA2rXPotMMOB28ETp_IVlTT29CprUnNSRQREFNf5kOh2ALHBz7FHxk21ugjxM_6yoTFtpBgspW6hqYO7pSV6wCxJ3lq9AS0R5AfCz6gdMxcrc-0MZEMwhVOP_JF3iMojAvB9gOYWb3_gv2IJHGYIFP4SQnmqC4KawSIZqzeNitPrLRTloPWt3omKLB2i-u2u6uHns5tbsp4IpZsSQzVet9n0qyId8wUBntYYnEFhDJTFLkf_v1clP9PPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فایل رو روی سیستم Extract کنید و بعدش راست کلیک کنید روی index.html و Open with chrome رو بزنید</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3123" target="_blank">📅 10:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3122">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">cdn-ip-finder-main.zip</div>
  <div class="tg-doc-extra">723 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3122" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3122" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3121">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ej15YZe2AtjEjG8Y3BIaUPXOYVJv0-k2u7_sQt10WNTq4M5086pPEesdjnjMwSSjRhhQ9ATmGZ3wXBilSuGqGDs178X_aIl6dJdRgfcZC8Zjz01p-W3QkRqkFNFcoCp21rzC1eF-xjFk801rzH5SIholfqxDuwqp35KTsDdnxk9MvRkzzde1W2LGdeXDQIBqJmLMmYSPvpQrF4X5fGjsM8lgd7XQCSgxMQ0NNyM9sr8hWr4gW1WQ_CvsNdcl_uqIZLVn5QjHK-EZTw2hejKVI5zMP6SMFPlS-HTJVEWXR2Qwc7Texs6r5_EGPTmQGqqbDmam1q9eFdwGTJfIklbIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفر اسکنری که دیروز توی کانال قرار داده شده بود رو برداشته، و توسعه‌اش داده و تبدیلش کرده به یه اسکنر پر و پیمون تر. این هم پروژه‌اش هست:
https://github.com/hossein8360/cdn-ip-finder</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/3121" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3120">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ایرانسل:
95.100.69.108
104.83.5.203
92.122.166.146
104.66.70.133
104.121.0.17
104.83.5.65
92.122.166.168
104.83.5.82
92.123.104.67
104.110.191.57
92.123.104.7
104.109.250.232
96.16.122.74
23.40.63.69
23.73.2.161
138.201.54.122
144.76.1.88
94.130.33.41
95.216.69.37
185.137.25.214
94.130.70.160
94.130.50.12
37.255.133.30
104.81.104.13
92.122.73.138
96.16.122.55
104.81.108.51
23.72.248.214
104.126.37.185
104.83.5.201
92.122.166.141
104.83.5.216
172.237.127.6
104.81.108.10
23.73.2.148
81.91.145.2
65.109.34.234
81.12.72.218
185.143.232.122
96.16.122.66
88.221.168.138
92.122.166.175
96.16.122.82
96.17.207.149
96.17.207.151
23.220.113.51
5.160.13.85
142.54.178.211
63.141.252.203
96.17.207.135
2.23.168.144
2.23.168.254
2.23.168.250
2.23.168.96
2.21.239.29
184.86.103.210
23.36.162.202
95.101.29.30
2.23.170.80
185.200.232.16
2.16.245.188
95.101.23.82
185.200.232.34
184.28.230.87
2.16.19.136
2.23.168.174
50.7.5.83
2.23.168.47</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3120" target="_blank">📅 10:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3119">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S829jWWXoSMBcC7F_fVKpBxVJjq6hlaW4qSyv-zKKQ8lJ8hzlsvZtiLkJM20NZ-53u-qpqXQTt6mT9Mvo6-GzeSUa--vooDGPNm5ItImXO-hD8Jcb-imiPrzQa5HY9TM60HBIQt8uJOnSpEE8uPpvy_eD157PLJnnv3Sd_mbCsSMSvm4UT7iNKqPiBxH3Dz2dWbQBm-WFgknqZxKxAA2-0euBQ0SGgqjHoUdzL6xrVCytUNziVGMWD7ULUwyGiS0pF9qyaXVXJjrklVi3PoWGDh1BR1emhfFMslRHIgreqCrCkHsKEUsrKRTksnr7kJe1RTjFKMC9yfh_BzY47icTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همینطور تغییر APN به
google.com
رو هم امتحان کنید. گویا روی ایرانسل بیشتر جوابگو بوده. من خودم روی همراه اول فقط با همون لیست آیپی‌هایی که دیروز گذاشتم وصلم به شیر و خورشید</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3119" target="_blank">📅 10:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3118">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یکی از دوستان این نکته رو گفته بودش در مورد وارد کردن آیپی‌ها:
من چندین دفعه هم با سامسونگ هم شیائومی تو برنامه مهسا‌ان‌جی امتحان کردم
و یه چیزی فهمیدم که خیلی عجیب بود اما درست بود.
هنگامی که آی‌پی ها رو پس از اسکن، کپی می‌کنید که داخل برنامه وارد کنید حتما باید آی‌پی ها هرکدوم یک خط رو جداگونه داشته باشن
اینجوری مثلا
20.68.81.211
20.63.74.811
و اگه جداگونه نباشن و مثلا اینجوری کنار هم وارد بشن
23.96.52.41
86.52.17.76
و...
برای من متصل نمیشن و این رو امشب فهمیدم و با برنامه MahsaNG از سر کنجکاوی امتحانش کردم و در کمال ناباوری جواب داد و متصل شد الانم دارم آپدیتای گوشیمو انجام میدم.
و برای این که بدون زحمت خاصی جدا جدا هرکدوم یک خط رو در بر بگیرن، پس از اسکن کپی کردم، تو تلگرام ارسال کردم و از تلگرام کپی کردم و تو برنامه وارد کردم و درست شد.</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3118" target="_blank">📅 09:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3117">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3117" target="_blank">📅 00:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3116">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nQulPWcq4Llw1JRi4E8vnUAg8Ce0lkm6Cp6jCcE_fsKSEeINt_30jgKI4eFC6-iak-PqYe7HNg7HqwZ9nK7TI0wpdOm18Cw4FpJxC3Ve6H9PFUeIn4tl7HRFJHQ2Hvy28bVWHtbD3iqguyMDsOQMjq1OR7JvzPIu9fCTTQ2sqIToGO2YOqXH__Zm8Upg5685V2QfvFx_bN3tg5KBivxTGTpqGr-25RY6rAB1QqhUnWVTdAaG2JGEpgqHK0vcHUUwAuoC4Odgv7Tm0OO_xcu1e9Wf2vPLv_crmivn75XTXud-SwNPgSRK07JeHwhkpoEF55TSI0ur65_m7PrII0EtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جدی جدی روز جهانی ارتباطات رو تبریک گفته
😐
تمام آدم‌هایی که شبا گرسنه خوابیدن و پول اجاره خونشونو نتونستن بدن و به فکر خودکشی بودن به خاطر اینکه کسب و کارشون نابود شد سر قطعی اینترنت از جلوی چشمام رد شدن</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/MatinSenPaii/3116" target="_blank">📅 23:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3115">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حس میکنم ضبط کردن ویدئوش ارزشی نداره زیاد.. خودتون اذیت میشین
اگه تا فردا دووم آورد می‌ذارم واستون</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/MatinSenPaii/3115" target="_blank">📅 23:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3114">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حدسم اینه تا صبح بیشتر نکشه که ببندنش متأسفانه. بله آخه دست خودشونه طبیعتا.
فیچر تماس تصویریش رو به راحتی میندازن سطل آشغال. یه ماه تمام کل دی ماه تمام اپلیکیشنای چت بسته بود اگر یادتون باشه</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/3114" target="_blank">📅 23:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3113">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این ریپو رو هم چک کنید. متفاوته:
https://github.com/theermia/BaleTunnel</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3113" target="_blank">📅 23:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3112">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🍷
این VPN بر بستر ویدیوکال بله‌ست :)) یعنی یک نفر بیرون از شبکه محدود یا روی VPS نقش Creator رو می‌گیره و تماسو می‌سازه، کاربر داخل ایران به‌عنوان Joiner وصل می‌شه، بعد اینترنتش از داخل همین تونل WebRTC/تماس ویدیویی رد می‌شه و از سمت Creator به اینترنت آزاد…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/MatinSenPaii/3112" target="_blank">📅 23:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3111">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
این VPN بر بستر ویدیوکال بله‌ست :)) یعنی یک نفر بیرون از شبکه محدود یا روی VPS نقش Creator رو می‌گیره و تماسو می‌سازه، کاربر داخل ایران به‌عنوان Joiner وصل می‌شه، بعد اینترنتش از داخل همین تونل WebRTC/تماس ویدیویی رد می‌شه و از سمت Creator به اینترنت آزاد می‌رسه.
https://github.com/kookoo1sabzy/BaleVPN/tree/main
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/MatinSenPaii/3111" target="_blank">📅 23:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3110">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">thefeed-android-v0.18.10-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/MatinSenPaii/3110" target="_blank">📅 23:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3109">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.18.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3109" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه‌ی جدید نرم‌افزار TheFeed برای خواندن اخبار کانال‌های تلگرام در شرایط قطعی اینترنت(کل جنگ با ریزالورا وصل بود)
کانفیگ‌های این اپ:
@thefeedconfig
لینک پروژه بر روی گیتلب:
https://gitlab.com/sartoopjj/thefeed</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3109" target="_blank">📅 22:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3108">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m9e2Ktsgkfz9IYNMrZ1rTvZ1-aayEdDYU2-FqrKLgco0iQ3mAzSo9T2JGiKr0hqPFHifLFo2wAi47Tl8Agnyt8MkRL7BYKAtC9Gr9hU4cBoiPIDqRV2NjlIycRU7qyq1TljsXiw6-c3eX1VVoF8LcZe6GCM_gm0TnCa0tK59RBLZXSBHveY3O9lUyRx0ftpQ0-T0DJIpgCDmpx4_Jn6YRAE8AzhUXtZS6Kl5zrknRvwvNQPBdJTE0IDvSqXtF7wYsDJu21Na66U_9y7tnNeiqCAT3j9nZvgSwJhkh1uEydXgJEkNBu-KAOVOsmGKWaEZ2VhJ901lFlWoP2vYsq8eNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیزاین با ai
:)))
دیزاینرای حرفه‌ای هرچند قرار نیست بیکار بشن. مخصوصا UI-UXکارها
آیدی طراح(پرامپت‌نویس؟!)</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/3108" target="_blank">📅 21:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3107">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b2PSuURFhESrqcVS1owAiB8PtW0hn1GzKRTYRWOcrPfyglH_ro3tXQBW4H9ZBTfnSfsoc7E2FAgOUFy5cYtbSya_Ocx5fRXOHDNp9K4iVODXas080l5FzNJ7JrkqG2MDIrpopkd-KfyX0x4KxdaJ3KaQ53500bgqRfDbVd9tQCsUeEp6X6N8-Rhc8ztj212B_WCwjpY7zUGlcoNmWAeb7e3udusJkeeFL_NGL-2qNZOUtPWC1eDyDm8VF2ycxYpwis9DG06NpePKkUYbCQFSV71TjA6XCFK-D3KRfcITg_9rPEzUKyJH5wc99NDjwJaF-6yTncHyWAFq69wcAkS5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان این اسکرین شات فیک هستش و ساخته‌ی دست یه سری از VPN فروش‌هاست. یه دور بخونید از روش میفهمید یارو خیلی هم عجله داشته
🤣
لذا خواهشمندیم زیرا</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/MatinSenPaii/3107" target="_blank">📅 18:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3106">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">CDN-IP-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3106" target="_blank">📅 16:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3105">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hw-NyPgjB8VPZu7E6-PkqPZ6JcNOeVq9HAhmV41oolNImqIIgwQvsPxGIurVEbjK6BZ4xXDBIgDz7Vt6nUv4pQd0GNlD2hDPLIfxpurvkLu_6fXArZ21cBOGgWZStOZQdLwLLGH-o2hYT0Mf6qo5_TJyFbMsZqNfeXnyp-T-FNlXplP5joeqcVU_x9S45d90kyA-n1PAsQpcdopGO3H_eGcSbv3ZbSOiG5wK7bTe1iFXUd7f1W8MU3JKBDl6eYMv1xHIcQ7CJm17gwK05akc0cLQaaAsRZWSw19CiqbTK6TZ9FZj444op73e7DYuOWqKphu9DBtmxfe2SP-WeEFZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچین موردهایی رو زیاد واسم میفرستید دوستان.
مسئله‌ای نیست؛ من که چیزی رو اختراع نکردم که زده باشن به اسم خودشون
😁
صرفا زحمت جمع‌آوریش رو کشیدم. منبع هم نذاشته، نذاشته. مهم نیست که.
هدف، وصل شدن مردمه</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/MatinSenPaii/3105" target="_blank">📅 15:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3104">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CDN-IP-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">4.7 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3104" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">هرچی آیپی CDN و ... از اول اومدن این متد توی توییتر و کانال‌های تلگرامی گذاشته شده بود رو جمع کردم، دادم AI تکراری‌هاش رو پاک کرد و واستون گذاشتم توی این فایل تکست. یه تست با اسکنر بکنید و بذارید متصل بشه.
صبور باشید
!</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/MatinSenPaii/3104" target="_blank">📅 14:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3103">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اگر با شیر و خورشید وصل می‌شید، گزینه‌ی Share proxy on network رو فعال کنید. سپس به یه WiFi وصل بشید و کانکت کنید VPN رو. بعدش با هر دستگاه دیگه‌ای اگر این کانفیگ رو بزنید(با توجه به عدد و پورت خودتون تغییر بدید): socks://Og==@192.168.1.147:46597#ShirOKhorshid…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/MatinSenPaii/3103" target="_blank">📅 13:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3100">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MahsaNG_16_arm64-v8a.apk</div>
  <div class="tg-doc-extra">59.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3100" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آموزش اتصال با آیپی‌های CDN از طریق نسخه‌ی جدید MahsaNG:
1- وارد نسخه‌ی 16 میشید(نیازی به هیچ کانفیگی نیست)
2- اون بالا روی حرف F میزنید
3- گزینه‌ی Psiphon Only رو روشن می‌کنید
4- روی Psiphon Setting کلیک می‌کنید
5- بخش Protocol رو می‌ذارید روی cdn_fronting
6- بخش Aggressive رو قرار میدید روی ON
7- توی بخش CDN Fronting Settings، آیپی‌هایی که من بالا واستون می‌ذارم برای هر اپراتور رو قرار میدید
8- روی Save Psiphon Setting میزنید
9- برمیگردید به منو اصلی برنامه، روی دکمه‌ی گرد پایین سمت راست(اتصال) میزنید
10- یه نوتیفیکیشن Psiphon tunnel connecting میاد بالا. اون وقتی تبدیل بشه به connected یعنی وصل شده
توضیحات:
1- نسخه arm64 برای اکثر گوشی‌های 2020 به جلوتر مناسبه
2- نسخه arembi برای گوشی‌های قبل 2020 عموما
3- نسخه‌ی universal روی هر گوشی‌ای نصب میشه فقط حجمش بالاتره چون تلفیق تمام نسخه‌هاست اما حجم نهایی نصب شده روی گوشی شما همون دوتا بالاییه
لینک‌های داخلی:
1- نسخه arm64 داخلی:
https://guardts.ir/f/ee1f60ae6d33
2- نسخه arembi داخلی:
https://guardts.ir/f/9d474d75a4fb
3- نسخه universal داخلی:
https://guardts.ir/f/7af85b518302
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/MatinSenPaii/3100" target="_blank">📅 12:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3099">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompng(Asal)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai.html</div>
  <div class="tg-doc-extra">21.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3099" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📍
اسکنر سبک آیپی برای شیر و خورشید
-فایل بالا رو با مرورگر باز کنین
-رنج آماده آیپی رو انتخاب کنین(با میتونین دستی رنج‌های آیپی مد نظرتونو وارد کنین در بخش لیست بازه /ip)
-بدون وی پی ان اسکن کنین .
-لیست آیپی‌های سازگار با نتتون در انتهای صفحه در دسترستون قرار میگیره و میتونین وارد شیرو خورشید کنین.
@p1ctok</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3099" target="_blank">📅 12:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3098">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef65e3054f.mp4?token=ZJrfOxJHeTf1D9f5qZAXqThFX0S5nlRvYIGlDwXO4BMw4fpOTg0nux0EGk4rZd5ziZsdRXuIPTqJ2gbiXJy-yhCXv-URpxVD8FseNaIrMTCh5xr33WqDjl-U7kJjt2KyQOyYvjquxFhqRjG61_-6qH8J-aGraf52WtK6OpUAZYSsSNekdmTHfHHoRsrqyqYa1b9AOV28kEyArI-_h-La6zQmsIa8jTFW2M5G0S6mtMkC8F5RwnkR8OvAAsP4uA8vSUSkswCMMfd4Amxzql8XjUpEUgxnnjR_TZWpm6_8kpOWWoOnKSeifiExPqSFZAvEg8fY6vjn7NzM64Qc9HPbn77gz8zi_kVM7fUUZCBVBSIMLrUmrmkyevM8-B5mEBC6ZDEySkqVv80vqX12frysjoy4Qn22WjGqqtkcSvluygXNc5hjG98yESb0AxIR5HTPuGhmorhv80i8WNJtt3zbsImre54TdJshKFykmhW7e1O2ZN0lX2v_RXmQeFpUWiAH3sf2retvc3aJoSnzg6Us2xukT9-MAIwFXgAYDpm4GyPaR9RgFuy_Za4TefYbRJ9rwaLq45oO9N7xcHg48Bkl3cx1tAZfCvKeqsj6xlZsQp2CVaXfAkWg89b0lhB7XGQvFQlkHMm41YLd3Kk9jx1RxDSdjhtJnKySJ3hmRjs1vqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef65e3054f.mp4?token=ZJrfOxJHeTf1D9f5qZAXqThFX0S5nlRvYIGlDwXO4BMw4fpOTg0nux0EGk4rZd5ziZsdRXuIPTqJ2gbiXJy-yhCXv-URpxVD8FseNaIrMTCh5xr33WqDjl-U7kJjt2KyQOyYvjquxFhqRjG61_-6qH8J-aGraf52WtK6OpUAZYSsSNekdmTHfHHoRsrqyqYa1b9AOV28kEyArI-_h-La6zQmsIa8jTFW2M5G0S6mtMkC8F5RwnkR8OvAAsP4uA8vSUSkswCMMfd4Amxzql8XjUpEUgxnnjR_TZWpm6_8kpOWWoOnKSeifiExPqSFZAvEg8fY6vjn7NzM64Qc9HPbn77gz8zi_kVM7fUUZCBVBSIMLrUmrmkyevM8-B5mEBC6ZDEySkqVv80vqX12frysjoy4Qn22WjGqqtkcSvluygXNc5hjG98yESb0AxIR5HTPuGhmorhv80i8WNJtt3zbsImre54TdJshKFykmhW7e1O2ZN0lX2v_RXmQeFpUWiAH3sf2retvc3aJoSnzg6Us2xukT9-MAIwFXgAYDpm4GyPaR9RgFuy_Za4TefYbRJ9rwaLq45oO9N7xcHg48Bkl3cx1tAZfCvKeqsj6xlZsQp2CVaXfAkWg89b0lhB7XGQvFQlkHMm41YLd3Kk9jx1RxDSdjhtJnKySJ3hmRjs1vqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
آموزش کار با اسکنر آیپی برای اتصال از طریق CDN با هسته‌ی سایفون اپ MahsaNG ورژن 16
این آموزش رو فربد عزیز زحمت کشیدن ضبط کردن و برای من فرستادن
فایل‌های مربوطه رو هم در ادامه قرار میدم واستون، و دارم فایلهای MahsaNG نسخه 16 رو واستون روی لینک داخلی هم آپلود میکنم</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/MatinSenPaii/3098" target="_blank">📅 12:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3097">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تمام آیپی‌هایی که روی همراه اول جواب میده و شیر و خورشید وصل میشه(حداقل 10 دقیقه صبر کنید، بعدش که وصل شد دیگه خاموش نکنید
😂
): 184.24.77.42 2.23.168.213 2.23.168.174 2.23.168.7 184.24.77.32 184.24.77.5 184.24.77.7 184.24.77.16 184.24.77.36 184.24.77.21 2.23.169.111…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3097" target="_blank">📅 10:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3096">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تمام آیپی‌هایی که روی همراه اول جواب میده و شیر و خورشید وصل میشه(حداقل 10 دقیقه صبر کنید، بعدش که وصل شد دیگه خاموش نکنید
😂
):
184.24.77.42
2.23.168.213
2.23.168.174
2.23.168.7
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
2.23.169.111
2.23.169.105
184.24.77.11
184.24.77.29
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
104.78.170.186
96.17.222.31
23.41.37.129
23.2.13.227
23.222.126.108
2.20.255.113
2.17.251.98
23.2.13.152
95.101.23.27
2.21.239.21
23.211.49.252
88.221.168.5
104.103.90.156
23.79.20.249
88.221.132.162
23.59.235.208
23.60.69.118
23.46.188.71
104.122.212.92
23.219.1.4
23.57.43.195
184.51.252.135
2.22.6.68
23.217.11.56
95.100.69.108
23.40.63.69
96.16.122.74
104.109.250.232
92.123.104.7
104.110.191.57
104.83.5.82
92.122.166.168
104.83.5.65
104.121.0.17
104.66.70.133
92.122.166.146
23.73.2.161
92.122.73.138
92.122.166.141
96.16.122.55
104.81.108.51
23.72.248.214
104.126.37.185
104.83.5.201
104.83.5.216
92.123.104.67
104.83.5.203
96.17.207.151
88.221.168.138
96.17.207.149
104.81.108.10
23.73.2.148
92.122.166.175
172.237.127.6
104.81.104.13
96.17.207.137
92.123.112.7
96.16.122.75
96.16.122.70
92.122.166.182
104.109.128.153
104.96.143.134
23.73.2.141
104.83.5.202
23.67.136.200
23.67.136.202
23.65.119.52
92.122.166.236
92.122.166.234
92.122.166.237
104.110.138.190
173.222.200.5
184.51.252.36
184.51.252.38
104.83.5.208
96.16.122.146
96.17.206.214
92.122.166.197
104.94.100.73
104.83.15.66
88.221.213.81
172.239.57.117
104.117.76.40
184.51.252.4
96.17.207.30
96.16.122.83
96.16.122.150
23.73.207.11
96.16.122.77
96.17.207.155
92.123.189.82
96.16.122.82
96.16.122.66
96.7.218.219
96.16.122.137
184.51.252.157
92.123.189.41
184.86.251.12
96.16.122.154
184.51.252.152
96.17.207.12
23.79.48.162
151.101.0.223
151.101.128.223
151.101.192.223
151.101.64.223
65.109.34.234
142.54.178.211
2.23.168.47
2.23.168.96
2.23.168.144
2.23.169.207
2.23.170.80</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/MatinSenPaii/3096" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3095">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یکی از
بچه‌های توییتر این
آیپی ها رو یک ساعت پیش منتشر کرده برای شیر و خورشید. همچنان متصل
🔥
184.86.103.210
96.16.248.183
92.122.16.5
96.16.249.60
96.16.249.9
23.12.156.115
23.216.77.16
23.62.61.53
23.39.148.245
23.210.73.133
23.44.201.136
23.205.46.167
184.30.150.142
23.220.161.217
184.28.165.4
23.46.230.133
88.221.168.204
104.96.158.174
184.51.252.4
172.234.199.15
104.85.26.14
172.237.145.27
92.123.103.24
172.234.159.58
185.200.232.43
2.17.100.200
2.19.205.42
2.19.205.50
2.19.252.134
2.20.169.70
2.20.170.91
95.101.111.144
2.16.245.188
2.18.69.150
2.16.106.4
23.58.222.107
184.25.28.31
23.47.124.134
23.50.131.147
23.46.190.18
23.58.222.147
23.56.162.186
23.44.203.68</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/MatinSenPaii/3095" target="_blank">📅 02:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3094">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دست از سرم بردار فیلترچی</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/MatinSenPaii/3094" target="_blank">📅 17:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3093">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گویا یک سری دوستان با تغییر LTE(4g) توی تنظیمات شبکه گوشی به 3g تونستن راحتتر کانکت بشن به شیر و خورشید.</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/MatinSenPaii/3093" target="_blank">📅 17:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3092">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/MatinSenPaii/3092" target="_blank">📅 16:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3091">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MVPLM8oiqL1G7tLXfeTpx8hCdzeJw4Rq5RHWGlr-tTv2uds5gipLn48NwunjT8V5Oa9TyEDEP6wzlkhgpe1sU8QcMhsz5Ho9cCSksvEsqAWIk9VuE8sZs6mTo8G0J4TO0CjpFeLUG19yVCQJdK1YCjFrVMdLQDdDpviUUyoWdod-WfHzAjHsMBgSWOwUlZbsNi12l0qNEcpwWOA7XyqEYF3PT-v21p8F7CR86nMVlxbDSEZQKdUUnyJfDbVkT9E0Lfp8FWL4bC1Cc-bknhYChphLoAe8BigHjFKpldxrP8HWYKugMOuUUHl_4rwfuOQYlnuXVE0-ztX2CddH6l9gcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست رو یکی از بچه‌های توییتر واسم فرستاد و گفتش که از دیشب(و تا الان) روی ایرانسل با یه کلیک وصل میشه روی شیر و خورشید. اگر کانکت نشد، مجدد عرض میکنم که بذارید هواپیما و بردارید، آیپی جدید بگیره: 184.24.77.42, 184.24.77.32, 184.24.77.5, 184.24.77.7, 184.24.77.16…</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/MatinSenPaii/3091" target="_blank">📅 13:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3090">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3090" target="_blank">📅 12:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3089">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این لیست رو یکی از بچه‌های توییتر واسم فرستاد و گفتش که از دیشب(و تا الان) روی ایرانسل با یه کلیک وصل میشه روی شیر و خورشید. اگر کانکت نشد، مجدد عرض میکنم که بذارید هواپیما و بردارید، آیپی جدید بگیره:
184.24.77.42
,
184.24.77.32
,
184.24.77.5
,
184.24.77.7
,
184.24.77.16
,
184.24.77.36
,
184.24.77.21
,
184.24.77.11
,
185.200.232.49
,
185.200.232.50
,
185.200.232.42
,
185.200.232.41
,
23.48.23.186
,
23.48.23.133
,
23.48.23.195
,
23.48.23.178
,
184.24.77.29
,
2.22.21.152
,
95.101.23.82
,
23.215.0.164
,
23.197.161.35
,
184.28.230.87
,
23.220.128.221
,
96.17.207.142
,
23.50.131.18
,
23.36.162.209
,
23.219.3.212
,
23.223.245.150
,
96.16.122.59
,
23.2.13.138
,
23.2.13.144
,
96.17.207.135
,
23.220.113.51
,
96.17.72.41
,
23.203.185.105
,
2.16.27.71
,
2.16.244.11
,
2.17.147.89
,
2.17.251.98
,
2.18.190.26
,
2.18.190.27
,
2.19.10.30
,
2.19.196.105
,
2.20.255.113
,
2.21.89.66
,
2.21.239.10
,
2.21.239.21
,
2.21.239.23
,
2.21.239.29
,
2.22.6.68
,
2.23.176.166
,</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/MatinSenPaii/3089" target="_blank">📅 12:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3088">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AlR0NaVe89Lw0LnJGjKYhlMCD0jixBSuZce0xfymoQwr-kxPfxcqkt2NSt28ejTcI8WGpeKPDXj8VvLc3lAb61DE-pq7AYersGmNKXrH-DASZ5e63kbIj2x3w5T1AtzZ12WcCAbvGpkAl63NMwnyPIMPUUFjk1Ai4VkAYdT9Bvgw_WjH1i8lk5zEuF2Q8zPYy4Ia4GypCxzHl0RzYDKAVi9EleqSz9vB7uiTGQhxn6fuUMLsIBeYaEje4erAuuAtUErl5Ogyn7eKQ668bXazrirxOqqKegiEqYTMjH5yTQAEtnYKIrWqjcYMN8rGIcnZHBPN_PCpKxJm8zmboXg2Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر راس گلر
:
روی ایرانسل تست شدن، مناسب CDN شیروخورشید.
23.65.119.52
23.73.2.141
104.110.138.190
104.83.5.202
92.122.166.236
92.122.166.234
92.122.166.237
96.16.122.70
23.67.136.200
23.67.136.202
همینجوری paste کنید اوکیه نیازی به کاما(,) نیست</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/MatinSenPaii/3088" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3087">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q-wb78YLRahFQAHDZwywGqRNyF5X0D8wMDFRHD0SQI80TRV6nUK-cR8Zo12mx2vzOUOjqwXPPKizLkeoiXN90Z9A-aeT-Y0WnrRHZz9gOQG_Vd7GTRQBzCfvXD-JGM3xorCgLA9Azn8pewRyqUrytOMb3u1cZnUkdB4dve9T0ziItlEYyur-lN9nQBEditheAM-Z-DAqRsUDC6i5Dn2ESG2JWoOZGKFhilPQZuipbDYewlZglNd0FaAhbwg5dTyLVAYzS1jBidtSKPdBjggWW_t75XTbj6e-SJkh7G73UBEKj2P2IU5GkkeHwQhFn1qaHwrKunwigpwxynTm2OUqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلود اپلیکیشن‌های اندروید از گوگل پلی با اینترنت داخلی
از طریق این پروژه، میتونید ربات تلگرامی‌ای رو ران کنید که به راحتی لینک گوگل پلی شما رو تبدیل به لینک داخلی میکنه:
https://github.com/ZethRise/PlayDL
این هم نمونه ربات پیاده‌سازی شده:
https://t.me/APKNitoBot
✉️
@MatinSenPaii</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/MatinSenPaii/3087" target="_blank">📅 10:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3086">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">9.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه 1.0.3
یک آپدیت متمرکز بر پایداری است. در این نسخه پایداری اتصال بهتر شده، مپ شدن تنظیمات Advanced اصلاح شده، تفاوت بین SOCKS5 و System Proxy شفاف‌تر شده، و احتمال حالتی که برنامه Connected باشد ولی سایت‌ها باز نشوند کمتر شده است.
WhiteDns Windows v1.0.3
- راهنمای سریع تست
لطفا برای تست اول این تنظیمات را استفاده کنید:
1. برنامه را باز کنید.
2. وارد بخش Connect شوید.
3. گزینه Proxy Mode را روی System proxy بگذارید.
4. وارد بخش Advanced شوید.
5. گزینه Transport preset را روی Balanced بگذارید.
6. این موارد را بررسی کنید:
- Compression = off
- Base64-encode data = Off
- DNS listener enabled = Off
- SOCKS5 authentication = Off
- Packet duplication = 0
7. در صورت نیاز ذخیره کنید و سپس Connect بزنید.
اگر سایت ها ناپایدار بودند یا باز نشدند:
- فقط همین یک مورد را تغییر دهید:
- Transport preset = Stable Iran
لطفا این موارد را گزارش کنید:
- آیا اتصال با موفقیت انجام شد؟
- آیا یوتیوب و سایت های عادی باز شدند؟
- از چه Proxy Mode استفاده کردید؟
- سرعت مرور مناسب بود یا نه؟
- آیا برنامه یا سایتی بود که با وجود Connected بودن کار نکند؟
@whitedns</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/MatinSenPaii/3086" target="_blank">📅 08:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3085">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اینها رو یکی از بچه‌های توییتر جمع‌آوری کرده و منم واسه‌ی شما می‌ذارم. آیپی برای شیر و خورشیده، بخش sni رو خالی بذارید. خیلیا تونسته بودن وصل بشن باهاشون: 2.16.27.71 2.16.244.11 2.17.147.89 2.17.251.98 2.18.190.26 2.18.190.27 2.19.10.30 2.19.196.105 2.20.255.113…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/MatinSenPaii/3085" target="_blank">📅 08:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3084">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اینها رو
یکی از بچه‌های توییتر
جمع‌آوری کرده و منم واسه‌ی شما می‌ذارم.
آیپی برای شیر و خورشیده،
بخش sni رو خالی بذارید.
خیلیا تونسته بودن وصل بشن باهاشون:
2.16.27.71
2.16.244.11
2.17.147.89
2.17.251.98
2.18.190.26
2.18.190.27
2.19.10.30
2.19.196.105
2.20.255.113
2.21.89.66
2.21.239.10
2.21.239.21
2.21.239.23
2.21.239.29
2.22.6.68
2.22.21.152
2.23.176.166
23.2.13.138
23.2.13.144
185.200.232.50
23.2.13.152
23.2.13.153
23.2.13.186
23.2.13.201
23.2.13.227
23.33.126.163
23.36.162.196
23.36.162.198
23.36.162.202
23.36.162.208
23.36.162.209
23.36.162.215
23.37.197.128
23.37.206.186
23.38.49.97
23.39.249.249
23.40.63.69
23.41.37.129
23.44.10.10
23.58.222.147
23.59.235.208
23.60.69.118
23.65.119.52
23.67.136.200
23.67.136.202
23.72.248.214
23.73.2.141
23.73.2.148
23.73.2.161
23.73.207.11
23.73.207.16
23.79.20.249
23.79.48.162
23.192.46.51
23.192.237.208
23.192.237.209
23.192.237.222
23.197.161.35
23.200.143.71
80.67.82.179
88.221.92.177
88.221.132.162
88.221.168.5
88.221.168.138
88.221.213.81
92.122.73.138
92.122.166.141
92.122.166.146
92.122.166.175
92.122.166.182
92.122.166.197
92.122.166.234
92.122.166.236
92.122.166.237
92.123.102.104
92.123.104.7
92.123.104.67
92.123.112.7
92.123.189.41
92.123.189.82
95.100.69.108
95.100.156.147
95.101.23.25
95.101.23.27
95.101.23.82
95.101.23.168
95.101.23.170
95.101.29.12
95.101.29.30
95.101.29.54
95.101.35.73
95.101.35.83
95.101.181.125
95.101.200.63
96.7.218.219
96.16.122.48
96.16.122.55
96.16.122.59
104.83.5.65
104.83.5.82
104.83.5.201
104.83.5.202
104.83.5.203
104.83.5.208
104.83.5.216
104.83.15.66
104.94.100.73
104.96.143.134
104.103.64.7
104.103.90.156
104.109.128.153
104.109.250.232
104.110.138.190
104.110.191.57
104.111.202.158
104.117.76.26
104.117.76.40
184.24.77.32
184.24.77.36
184.24.77.42
184.25.52.200
184.28.230.87
184.51.252.4
184.51.252.36
184.51.252.38
184.51.252.135
184.51.252.152
184.51.252.157
184.86.251.12
184.86.251.27
185.200.232.41
185.200.232.42
185.200.232.49</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3084" target="_blank">📅 05:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3083">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نمیفهمم چرا هر متد جدیدی میاد و هر راه جدیدی باز میشه، یه لگد به گیتهابِ بدبخت می‌زنن
انگار فیلترچی می‌خواد ما رو تنبیه کنه
😂
داره میگه دفعه‌ی بعدی گوگل رو هم فیلتر میکنما، حواستون باشه این سری عصبانیم کردین</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/MatinSenPaii/3083" target="_blank">📅 04:55 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
