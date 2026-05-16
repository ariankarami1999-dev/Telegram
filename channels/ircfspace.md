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
<img src="https://cdn1.telesco.pe/file/QJ7AWJEnniHdkiJB--Uccq8HiYC-VD4T4DYDj2chIZbym1hYx9-7XuenchJ2S8EBYa8V7rfpSWPw_CASuTnABhIGKXNEiKgqVo0pErL2q8XC2eOc-M7l9rHAYWTWYXYeOb-w68NevThEvRR6Y8qfN4ij14kBn2DI0pG6fWonm8jEU0N0RMRMPPzFfW-IYVDLBlAGUnjVXUY19XVoDsc6E3_OjA7Y0uCNOzU_8VTSt_RcZ1lWuZqy6d1pP3Zwn3RLG0xr5kLnWFu1hWj-O2MxGd9Kl_yTorMDMdyY5B2ODDzj5sTv6Lmlewti7I0LilW7zF71P-cjVmG0SPJ0mfc-hw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 94.7K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 15:13:52</div>
<hr>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IhoM7ircuP1Ntq48rqO9idSKgqVmLDr2450KRn4v3t7e75Crm5xl4i1tgXyhe-cJIC5tuAxUSI2gnULHN9v4IDhb-bIFPEjdik3jLjzaaw-8C9rscTt3-xo6u4eNebwEog2qgjpf7AqoGxLuqMK-Hug1QRTikiUoX9gwmdqSffeK4Vi5XQKf0bLGdazUHFwZ-KVAfcsJ-DfpQZCbY6bgugY264JA2250YRidUuvJ7NXbY3eyFh7B78uo8_L3nRKlTFgy9T5oka8C-yDV1CrWOv8wLRJn-NRBA_LVBnIzW26Q9ldmMX78SAr4euC--9ORP5CdCqxMQclsCmX9o103OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZnyiOPFsU9BFvz3tF7UzTR0ZJWf5nDcY8HKijDiY226LsVz-Ewu-7zDJfuphB5dyYN8p3CfVBQ89HHOirn7a9_dSogx7czAFSgojx8N7LueeUcf1p0_SgGb-KzovU3pZ8TS8B_Y7IQjg-ng5dQemXWqzM2rRu0txHqIGS3rPozi1_AtoOZPFH-CZRXTt65D4OEexADqKVweQeXAW6RvOimL7wcEjKPJS_HTkl3IBtA57yk2WckwP1Wn-6jtC4_mBdOT9XEaaUnF9YTBJrU3UXRkp41154I7j6B7FGqeWgG519tRh4bhW82St8vADKMQOdmzncddJF5R5MU-Oqnz5Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelForge یک کلاینت L2TP برای اندروید هست، که از امکاناتی مثل حالت VPN برای کل دستگاه، حالت پروکسی با پشتیبانی از پروتکل‌های HTTP و SOCKS5، مسیریابی، پشتیبانی از چندین پروفایل همراه با ذخیره‌سازی اطلاعات لاگین، بررسی وضعیت اتصال، امکان استفاده از DNS سفارشی و تنظیم مقدار MTU برخورداره.
👉
github.com/evokelektrique/tunnel-forge/releases/latest
💡
t.me/PersianGithubMirror/5008
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q9Dr276ewI4moLjxK6ZVzM_WqPI8sFC_Xbnwu1zzITdH4wEdXQt9znqyOasyizhA3b6UgqK19EIjY0hbw8b4zZzP8OCiszryZfdzjx3OC6c8ApIltRjvYDpNVcvJ6NWf9qYwCHgi49M9SViZxVXOzzqiWArwdV2-J8Py3T3s5xHfOWoW-nbJWsLDcc5U-5mSNPoM1eW8SX-guCkebeQMQb_bK_dgii3FP2rSOR0zN_K7d3fx7RnvkOrnmtBwti341gXDGXLdle3KBU8FtFt3mjDeKxdaUGcIVoBFzuGkJwE0_S2qdMeA0WGfZtxtJfSIR_yRg4avDDoz27C43QiXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آسیب‌پذیری جدید به اسم YellowKey در سیستم‌عامل ویندوز پیدا شده که توی بعضی شرایط میشه BitLocker ویندوز ۱۱ رو با یه فلش USB دور زد؛ البته فقط وقتی مهاجم به خود دستگاه دسترسی فیزیکی داشته باشه. برای کمتر شدن ریسک بهتره ویندوز و BIOS آپدیت باشن، سیستم کامل Shutdown بشه نه Sleep، و برای BitLocker رمز یا PIN قبل از بوت فعال بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QkPH1gfGR6XD4tUyxMnPQb7u8ZMh0zjEl3Jdra-kOZeHkqNF3LhD9oVQHpZfvFQuxz-7bdMRal6sMwGaNebf4VKlUXg9QPXfuisb8iPqWxMIMVEKBjhtsuY75stILN2y02VXm1NInE7HObbzJrgS3JnQql1Yquync_quTz0yA7icX-FHA9IxSKeLQncJcdtwjaBaLdY28V9CbUJT3_ux2lQ58HD3wZjq1OORs9TAH2FVZrcYGY1JHdhWPGh7R4-6TcuSJQ-LvJ1wfoTY3PH8-KUZNP-VMqPeA8AiHLoiGUrAnOQ0YaTp5hopJ4SIDwYNzRmMfFEzGhZrODybrTTP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استارلینک مینی به ۲۰۰ دلار رسیده که فعلا اشتراکش هم رایگانه. کنترل اینترنت با اینترنت پرو و قیمت‌های کذایی یه توهم زودگذر هست!
©
imanraisii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lHhw7nytf-GS1CW2YXBk3_BwL70zCbDSwl76iph0sewgng40B2KMlQkcUgwPwtgTJRrvDbgPPz3sGWYE3kS4Q2ChrUb6KzZaUX7tqhHVjRoeCAGuWDfcE7cc1bCgD4VXsa6tKc7NNaknFmVqOuvcx58w-gpSvEOiF9pgAGbcrUJlDGrXM1b3SKGB6k1ajm_vx4t5UaVjUa8gUh82P4lFVa1_nqRiIqJ2GWpgT1okUz759fX-TDgl9sjgHW7yPQi20e30HeZwZ6AvJHaCIP4DRyNdNmBZ7rFS4HwvrXT16-cBvBFcjhgc5Jm5rkbtNfBY9j3TymLSNvzOmVlAt2YskA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هفتاد و هشتمین روز از قطع سراسری اینترنت، از جدیدترین روش ترکیبی عبور از فیلترینگ با ذکر "لعنت بر جمهوری اسلامی" رونمایی شد.
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X9pkMdb4Eq1r7hNQMg_0sTpFaJOc8XX3BdKm2tU27XcfKZCpkiMWT7YePxU823YS4z0RtlDPNoydOngIdUucW-YS5Xfn5NEw5HaqORI4xxys99gnB5dVlW8_yVfKYf9fj5U2e9zFUA8JcrA8BQmKAiPXofMBrAf6OTy0PV8ZZDz7oH71ar4_cj_HANIUpZdBgGkjhI_BolcTnCf4iMWyj_Fl5Dmrn8dca_v5zC8TypdMyL_rNTnsq1a7g1HGvTg4aW9TZf3XveiJi6Z-hux2t1EXgepC87PhOgIJsIb8lwpB1JTImYhTopL9xcOkfNC1Ny7q4TFKH6AF7fqyB-ks5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتگ از تبعیض بگو!
اینترنت غزه که قطع میشه، اتحادیه بین‌المللی مخابرات میاد محکومش می‌کنه، ولی وقتی که اینترنت ایران برای نزدیک ۳ ماه قطع میشه، سکوت مطلق! ۱۰ ساله در مورد ایران توییت نزده!
©
markpash
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dyqqQ8XPbS0fipfJRDVpsn08F9fVyEsDmK6drdoXbwyGLxWo0y4qjN24CrgqZsRwFvhOP77LXBd1M8yg04GsjvEUFNc3cgTt7jqbbBFjd-fyX8O-TF34MAI28NbQUn44wQh6x6Xx7j8Nn-t7lO5IY2-q4c8bT_nl2uzxhyt_Ue94NmsitO2lrQDDs6jKlffgucNpN7At2zlXUwE57dw7G1Rdz0J1yRnT0-d_x1VzsjpKcViRxVGDhsiRYr6Jfmp8d5ss_5DXBZXFhXTmk6x0yQWV4gRJDcFGkTsDpsxGEl2dolf1Xo4n1VzyE9ZCcLy84I3UjTvOm8Np5pzrgiLvQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد حساب این الاغ [توی ایکس] بسته میشه، داد میزنه که آزادی بیان نیست...
©
AminSabeti
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تقابل اینترنت و امنیت یه دروغ بزرگه. مردم نه‌تنها  دسترسی به اینترنت رو به امنیت کذایی شما ترجیح میدن، بلکه هر چیز دیگری که خلاف ترجیحات شما باشه رو هم به انتخاب و تصمیم شما ترجیح میدن. شما هیچوقت جسارت برگزاری همه‌پرسی در هیچ موضوعی رو ندارید.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2336">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ستاد فضای مجازی با مدیریت دکتر عارف در اولین روز کاری برای افزایش رفاه مردم و تحقق وعده‌های دولت وفاق ملی، گیت‌هابو فیلتر کرد.
©
pey_74
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qgFJnaMPCWD76CvMq6BxO50w99corZ2nGKAaTSBqNGcY6H_sgxbPWA6kY_C4_nnzA1poVOTsXZ0Ky48SG88V9q1X8R5ROOLyHI-XwRVLXwvT2Wd-3JSP8nnwj_90CizGSY9v9n4Tope8RqRWX2-OvclK_sRDYUC2YFepw9SRSWZNBNDpMz-UYGJBUKJTa_gkGX4x8RAudAlo5ELrIbQnrh7t03uRpDawrC4CgrGeZhOtnL4MsjFVwS6aAK6hH8TJ6PqhewEu5tWfEtkEL1PgbvIZSQyLJDKluWz0V0kggT3gKvW1PsPwbmJvfJx5cJ2VRG2sKnHVJrVrswP-rhr2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش
MITM
در آپدیت جدید از اپ اندروید
#شیروخورشید
گنجونده شده و می‌تونین بدون دردسر ازش استفاده کنین.
برای استفاده بعد از نصب یا بروزرسانی، باید وارد Options، سپس More Options و بخش Connection Protocol شده و CDN Fronting رو انتخاب کنین.
همینطور در قسمت CDN edge IPs اگر IPهای وایت‌لیست شده
Akamai
رو بذارید، سرعت اتصال بهتر میشه.
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/4954
©
PawnToPromotion, mahdavi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نحوه اتصال رایگان و نامحدود به اینترنت آزاد با متد ترکیبی MITM + Psiphon
👉
github.com/patterniha/MITM-DomainFronting
©
patterniha, MatinSenPaii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">روز هفتاد و ششم از قطع اینترنت.
معاون دفتر پزشکیان گفته "درصورت برگزاری همه‌پرسی، مردم امنیت را به اینترنت ترجیح می‌دهند".
وقتی گفته میشه هدف از قطع سراسری اینترنت و خاموشی دیجیتال مسئله امنیت نیست، دقیقا مطرح شدن همین اراجیفه که به جای نظر مردم به افکار عمومی تحمیل میکنن.
زمان زیادی از کشتار دی‌ماه نگذشته. به جای این چیز خوریا، بهتره یه همه‌پرسی بذارن تا وضعیت مشروعیت جمهوری اسلامی دستشون بیاد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gcANNejI9Ip9RKfVqNT-ybPAu0X753IAvB-ON1vMzPBzu860DvawEFxyfOVg1H8WBrKCPoLkTQ1gIUEBaOPRpqW4n3h3eWprBNoyknW8ifmnfxYj0bZLxUJH0ubNXxobI00youS2H22-hv9UpX7wM5UB5v0ZXVsGVrzmGWK6Qve2XtrIvOuq2XwozkhZ4fzn9uUXkYO-ThzXs4f94nS3rlV-xkY9SfUimiIx1U6U1UXz0iSDkm3v6mfhJjO4uWZgRhn3NNDc8opS8mJZtPrNYWnRsFxvwNviLPv1N2umciVQ3_X5owae4x7BKXk0mLSkHwx36a3rIQ0jsikSYwfK-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oq7Io8Wz--lqAW5cfqdgo-XV6oWKelYwz-qEhr7_uQWjFucNGgq0iRTznN1xczV8NoMIemsqvlxOODYlB2efRv8DlbT9e0bIhO0sN0Bh0NWb5bkCbpiuMNgvhcUc810qZkmyfKNc3uTb2BRRbQczVHPdu1bBDUG7y6Um-spPOehzrChZlR1lMmSyZMjSitL8lGTglC3UECKlKOssPH4I_U9zYXXr7KhZp7D1hmnWRlGqaUQ0YmvZGZCYZeToeCZzAn7J1Ah6wgUUMez9xwB3Ii9cfmgZIrhRGFUthUNP1BgyMjAF-d4Gqeh-SUIAdFPfz_JTX9a7pN5w0TPWHIHQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۵ روز از قطع اینترنت گذشت؛ همزمان درآمد یک کانال فروش فیلترشکن از ۱ میلیون دلار گذشت!
©
mosi115
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F9jGSY09X_OikP-ZEHZboUKi4XAXe4xPJ8e7ck-7QEQAzRjoy-x5SH47fA_G9BGLG18-fErfCZrC5nEzOJVGwHFipKXNUcgQGiKx6q1UJeNbFERAwDapeH8nDwBZSv9X5OJmj38D99Cr4ktA-kcXAdwoRJ3XgXqO4Ko-82MQGHcfXrYla2P85R8Bw-i_pSCKhia1ZuPjbBFiEcm7kT2hxWiZr1dKfzNbUnnEffGrYkh1jJKehoybkiXDCQ4OzYRXV8bsZ_zSSGsJ_yxw4-8aqg9G1_nxGrzuxv04e6fB-HMlbabcy_IrZPPrJ6rlCoqRFIIYS_aj4389h-ypdwF8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میاد مرحله‌ی جدیدی از
#اینترنت_طبقاتی
شروع شده؛ دیگه خجالت هم نمیکشن. قدم به قدم دسترسی برخی افراد و کسب و کارها وصل میشه، تا عموم مردم به عصر بدون اینترنت و بدون هوش مصنوعی برگردن.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سی‌ان‌ان در گزارشی نوشته
#اینترنت_طبقاتی
در ایران خشم و نارضایتی عمومی رو شعله‌ور کرده و به نمادی از نابرابری ساختاری در جمهوری اسلامی تبدیل شده ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2328">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قوه قضائیه در یک کشور مردم سالار آنجایی که حقوق مردم با تصمیمات دولت یا نهادهای امنیتی نقض می‌شود واکنش نشان میدهد. در ایران رئیس این قوه نه تنها حق مردم در دسترسی به اینترنت و کسب و کار مردم برایش مهم نبوده، بلکه چندبار شاکی شده چرا اینترنت پرو را سختگیرانه نداده‌اید!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=YVjvgPaIS9N_e8lCzaGpe7pLz2LiOYijLkADIG4mXlzGF0KcUJiqQkBgDpa9h0pgpGHfmO9nb9y3vCai7_F9A9gnNIv2wpioMRd5RWn812digiyWVal6xIqROnPI6USCmaMssdKKVZHzV3Ly8d1oddhEVJ5mFwX77fqFZ0yu4jkNH2UzORBnT_TVPTYtIfklBy4H-TvhWBrtCDy1-jxdgLRWUeY9fEMSsMq0vmqYPFPTlL50N6RXPukx5whKn1aHeM-GNyxl5xa4iBF8tuKgk8Y1EBE2fyJRDagj2-ATlp0ojl-vJ_AsjVcYRpZWC8yFaGZ-aA3kkT0x7_2tYcQQqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=YVjvgPaIS9N_e8lCzaGpe7pLz2LiOYijLkADIG4mXlzGF0KcUJiqQkBgDpa9h0pgpGHfmO9nb9y3vCai7_F9A9gnNIv2wpioMRd5RWn812digiyWVal6xIqROnPI6USCmaMssdKKVZHzV3Ly8d1oddhEVJ5mFwX77fqFZ0yu4jkNH2UzORBnT_TVPTYtIfklBy4H-TvhWBrtCDy1-jxdgLRWUeY9fEMSsMq0vmqYPFPTlL50N6RXPukx5whKn1aHeM-GNyxl5xa4iBF8tuKgk8Y1EBE2fyJRDagj2-ATlp0ojl-vJ_AsjVcYRpZWC8yFaGZ-aA3kkT0x7_2tYcQQqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر هکر بودین و میخواستین بانکهای جمهوری اسلامی رو هک کنین، سرورتون رو کجا میذاشتین؟
علی کیافی‌فر، متخصص امنیت اطلاعات: در جنگ دوازده‌روزه، نوبیتکس، بانک پاسارگاد، بانک سپه و بانک مرکزی از داخل خود ایران هک شدند. مثلاً نوبیتکس توسط یک سرور زامبی واقع در یک مدرسه‌ی علمیه خواهران قم هک شد.
قطع اینترنت امنیت رو کمتر میکنه و نه بیشتر. سیستم‌ها نمی‌تونن آپدیت امنیتی بگیرن، سرتیفیکیت‌ها expire میشن، ابزارهای دفاعی (فایروال، آنتی‌ویروس) از کار می‌افتن و هکرها (داخلی یا خارجی) راحت‌تر کار می‌کنن، چون نظارت و لاگ‌گیری مختل میشه.
©
farhad_mottaghi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V0e3WdtiNxst1OTVyMel9iaS7SBbmd9F82IPPujpucIR6ju3MpQlrKBgohLHl3Qgs9m73wzQgxNTL5cTWXgN7IlJjIsnkhe-5UipPNjoYrsryTGJCyM-kG8mFpdgvng4553pKC7aMARgxES16mJ8gG2PcmWBjT6usx5W9eogzq0isNkUCbqErcY75K4LNb1M6mw9m7GYV2zsgAWQY6Dw-B4YDegPH-3R0TO31NxRF58YTy3dt6r_f73xmkQjwYe4Rxm32kPCldQZCA4VLqAVxYy--Cxr4vMfFVGGMGkuVyixeDr0ynUActd4N11ol8DoWV5uhi_mNej1cfPt4divEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگهی یک دفتر پیشخوان دولت برای فروش
#اینترنت_پرو
©
mamlekate
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hc7jb_-if6L1u_OH6DadqXu_rEt5UH4GVlT8DW9AtwPBWOWjuXba3lxFjqonw6xNN1q-L7XluzIZCAvPD3rGRCNzHt1_ZFT0t_jDurkkfXqlvw8U5kNLEOvHrLIV8z4u3xHZ-DcRFYrPbfdkuA8Q83e92d3syp47E0lfzrx7it85v-_GOnalZXM2wD2KHA5lcJMktp5DidPmHBCbPkTMITm3SYuQs0zqBRf8M6bpEDHIRn_xGaI2QMsqnGOle01KcKt4-0rtcXHLbAf1-0iCMofeCbRX7Q6LYVr_RyyLB0dZDOA_9Aqz93CpMSMhehI_78kA0YyjCLuhdnuQnQr9Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تعداد کاربران اینترنت پرو کمتر از نیم‌میلیون نفر است!
تا امروز یک اپراتور با ارسال بیش از ۴ میلیون پیامک، برای بیش از ۴۵۰ هزار سیمکارت،
#اینترنت_پرو
فعال کرده و اپراتور دیگر با ارسال بیش از ۵۰۰ هزار پیامک، حدود ۴۰ هزار کاربر پرو فعال دارد.
©
aghplt
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BWOptN7oiYwOlrif0RHdAoAIX0Y1w6_0s4LzzB-tiPLSMU8FzydnRR-BW5-LOACkEFs5nU07eJ2POiZCcm3J_6s5Efbsf9B66A76c4hJRjmJpH0MknE1DHRu1wZ1UY3jk9P20s_KYDCMTnGq4aHH6BODM_aV44l4gbDN8qhjUVGlF7uO3U8YtrNMxnI3ybN0R1Gj73ml2m6SXBMPVU_brzWSsdAnWl8YQgoEGZT6y5nEzNJ4arhm4NgpcmEqQrHcG7AHiGd3WTCxaQxp1AZ5d7A2qVEMuKXX1m5FZUD1lzBoP6LUlZo8iusSDNOgCiwVnKCgqfMaEPMwlojcEaHJUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن مهندسان نفت برای دریافت
#اینترنت_پرو
واجد شرایط شد.
۷۵ روزه اینترنت رو به بهانه امنیت به روی میلیون‌ها ایرانی بستن و هرکی که کار و زندگیش به اینترنت وابسته بود به خاک سیاه نشوندن، تا
#اینترنت_طبقاتی
رو اجرا کنن. مدیونین اگر فکر کنین کیسه دوختن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2321">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بدتر از قطعی اینترنت فکر اینه که سالها درس خوندی، دکتر و مهندس و محقق و پژوهشگر شدی، بعد واسه کار علمی دسترسی به اینترنت بین‌الملل نداری؛ اونوقت حمید رسایی با حول و حوش دو کلاس سواد برات تصمیم میگیره تو اینترنت نداشته باشی، تازه خودشم تو ایکس وله!!!
©
NiHa_Mehr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ONGivaCOU1XqxvU3hKD8yPtbwIi3hfxX6H1DJ1x7CxuwrLAVPUI2yt6-sHz4_F_JPWZOWjjDWx1mlHnqnq9ollPNuDpODbAp7rvF5QSfr-AlfYE-GTA4vrOTGdYa8NbB_LhuBoF0el3Nsrn8rR5FEMztX6Eru7AZJjMvO9gbIo0oVoOlhLLS4gN22OwmVxTqglpvDkvl1314kEiFMzpd_LylYLaby8_Ci2GQo552FpI-IlDcYMLShw0pGsMRw0GVOQkDrlOztT4uDSM7JDkABlXuItedG-9VCZRdclS2vn94YSAPQx-1ue0wGv07lI5kP5p4-oCxWHHnRt3J1CtvIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس قوای سه‌گانه کشور در واقع ۴تان، که یکیشون به نام
#قوه_عاقله
نه توان قانون‌گذاری داره، نه زور اجرای قوانین رو، و نه در جایگاه قضاوته. مهم اینه که قوه عاقله قصه ما با
#اینترنت_طبقاتی
مخالفه و قراره نقش اپوزیسیون داخلی رو در این مضحکه بازی کنه!
©
nimaclick
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ez1aJTijDQjo94-9-dQ91WNUN6_tdh3ph8bKHwpJOBTKxDMjRqSgoYJOZpZFt6xbpCJPfCQOJd_a4tossQwkuUoSk_-RXItYw6AoDyQVQ-UVhSUcW0CmXnUqnJnbzgIJmZiVN210Nn6SYcF8SlnLuOyihtJ4BJdaaBgCLPK6aXDBpoSsPYAjYBeSREmqW3d6XKx0sWJDuGdXJGQO7I5GQsayGA_dnauQPyUUnR0PAN-lj8rwiFKgjSC8hrbrD2RMOWBZQ63KBcBQuUylp0SVaUKJe4k-kRwWP-Mp1eyDp2njB6O5u9ppX3uh7HNpIcMLWlFPjGh0mHt-Kwu8joQMwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای
#اینترنت_پرو
به اتحادیه صنف اغذیه‌فروشان و مواد غذایی باز شد و حالا با ارائه پروانه کسب و کارت ملی میتونن از
#اینترنت_طبقاتی
استفاده کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t1jr86IzowHMpv5YeGYN-iRLjXZwkvXpwzeUyK5TChFuPMrkt_wBtGpHNa6RbQFnxH1T97NR59QPd8Ghgm4HCThCEI45FVob9A3p6hOhG1yEkjBLZ0YBd31rc8GFHVe-_IzYuUcskaUQFQlobf1JI1hHSw_x4a5xfrj2xs8meMPe1-xRZ5B0f-if9DXfGpbPyIZK_IKK-GxhQ3z3TnHViY7VArhIzoTvaOKDD5WsqjeBp59t_n0-QKpfLBPybnWpdBvMPYe6CNWlyd2xwkl6V7DmmQMCsqc9zTw2epYUFTg7UN8-fJWUhuEhGWUuKUJCxgllFN3A85g7aiK9GsStqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
👉
github.com/MaxiFan/TunnelX/releases/latest
💡
t.me/PersianGithubMirror/4816
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WgVnutDgvZPw_asFBZQlM-I4pVVX6HDV1l29lJ0fqwrJMHXHmiEIy6qZ48rho0uKo3C38QiZES9dwIS9FxHMY3jSCV0c07FbbSciyk6jWzoVR5EBazWmd2K3WPDayqDZHm3FZDi4TX3tl5f1mykBgRrvIGcuaMxauSbprb3B-b5D8N5suerOcsVwtEUGLo9HHL1nWzhp5x8km_J186C0l1KZg9Kwh8Cbf2u45l7yEe6HgajWxPdjW2In_I2rIMyoIX23XHtkfcuIH4OaXLG2NelK6frrL_75qgtuDjBklGDUw7_ZS7LtpKnkVMPC_-ZEs8zJI2IJ3rAhyZbOI90dAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام "اینترنت پرو" را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VdVoCtTidMmydmn83y4ZeSVbay7RzesYGrwf_znGhfm4Av5XlDHBNz7oJ-j1PXu3-GUsTWq1AuA4PJfHRP1yR1dpLE08Mjuq-4RjU6ragZ2p-eaSo0jYzYxPe51dHE8WIKsBMW6IBG1Dkmz9a9qSi_1fe5OTFsQ-i1YUr0LSzVMSISDHCZykF-weqPFQJFELy6YxAP0kdbYNIQr8YUJN0pzO0pKjRdK9OIjJFI4ksgdxCXUSJ9ewyvf_NFDiFPGI_OpbhKqB7V_wsqd4bRFmXJuIz77FgXCMdhpypyO5uYhyuFJy88Jqdx4eHLIFG2FswEbm8TYCT0T-XQ4RymQ1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در روز ۷۴م از قطع سراسری اینترنت هستیم.
وزیر قطع‌ارتباطات گفته "در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم".
نتیجه عملکرد و تلاش ۷۴ روز اخیر این فرد از خروجی عملکرد یه مترسک داخل مزرعه هم کمتر بوده و جالبه با اینکه از بی‌خاصیتی خودش آگاهه، حتی بصورت نمادین دست به استعفا نزده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uuf0RZF64dvVVx34SvfAKsrGTE06-Fkiak_rCXMKhsfzibItr-ywf-DZRn8Ti_LEzBSwEk1IScBGtu12k3zh1WzuJ2VWGC8cOrPJ3G29kfchsQVaBQEMQ_h-dPY4EyTX0oqZBKE9kn1XyZ9AfIh4CewnXkSNitVeFAjtY7Wh_cRe9wuHxHv3x556dmZpxyhIqxMvFVHiireZaMvrUs4TWdM3D9D6TBb2BgK4ikjmyqYF8J0f48tgoRxhltoQRaxMuJtsZ4XEtPh1o0ch8cIKQhrDCyQ136QbsxBtDiU1a9vf3Y7rJW-yIICfMb24u3-diJKDmGxldouTsFSMn8cTYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nuS1h3Iy2IhIHQsoIDpuqKRh73QpzTiiiGqNqG06BU1FAiMKnLpZqdpKC4TzNMuMIDfTCSbMDyJT35RaKNtZ7GpeOEeWHE8Jaw015TUXawDHMHAQw95-9VwicVMjoFPGSj2NTWX4ik6itvdVhwgYvFFviFed1Ouc3xhixCR8kboetJyOW6T4uOohlW8UkJA9lttIB66GJAFaGc4qYwQQZiUmVgowu9BrVgCVdmTkY5LaJKPK-527LTmm8uwPcdtwTowPSh_WJKfgL7EjlJIKANbxqsTFEnWHnY69FzoGBalZACw6v5AbIShVhEs3srDyoRGIPrYsbAhQSPe71uWeWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده.
این ابزار طوری طراحی شده که در شرایط محدودیت شدید اینترنت و وایت‌لیست فعلی بتونه بسیاری از فایل‌ها و لینک‌ها رو دریافت کنه، بدون اینکه نیاز باشه سیستم یا سرور شخصی برای دانلود داشته باشین.
با توجه به اینکه این پروژه به GitHub Actions متکیه، بهتره برای استفاده ازش از اکانت اصلی گیت‌هاب استفاده نکنین و ترجیحاً یک اکانت جداگانه بسازین.
👉
github.com/ProAlit/aio-downloader
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uc55Nl6baGOD36sNZVREqaKGlYmdzaX5jqO0qln5lQw_M4gnVG4iy0b40FtLbmTRN6glSTOJGGTLfZyMyxTwz5FNSdLZCJypPbvDoE1dScvSfRO9o9uJvKtJo7qs7ci3yaI4jAZhSkHRoFv7w2z_S_mN-0jFjF5gkUPai51pe2A0KJQXE1or4WKpO1KPItC9ei8U0g6niqAx06fznpvmsFMmazMveOFhrBAanQRoHIc8Unfw0eiOUbzE9LDAt7m4by9pakSCsIwfo8Cs1y7D61rZPhSW5Dita0qayR97AnZaXVwFADZWOryMwoH3793EW5zjTittyVa_Dh6ijKpWFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h_ugvAJpFttOQ-HoiMSY3gxGd9XTYZMf4gvHEgZ3F2771IdOCY_P3ggDLTgsjqlc8u5A6IkVwByHHM4CTwNuKlS7d4j8Z1GqiYbjwvawELjMqTl6ywfPFKPaVM7t2X7OTQh7PSaqZWwP5TnA4pRDY9N9Db9kBUWaDPUaTd6tz1s1ROXHMzrQkCQhXNaSUZNgV_4PXXXACHRsVkd8swJ1cl9C5h_IACAihLQv3LsN85qy353HcMLSyhWKudTta3rlGodBhasmhx8dcFH74RB-lAyMQn4Ml3oee8_jQi7OgBvnwZ75kXsCiCX_7NQYAzRIlt2RoGEBldN4dwW4iv2dTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه رودربایستی رو کنار گذاشتن و بدون ثبت‌نام و بدون احرازهویت، بابت پیوستن به پویش جان‌فدا ازت تقدیر میکنن
😁
کی به کیه؛ اگر آمارش به ۳۰۰ میلیون برسه هم تعجب نمی‌کنم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">قبل از شروع جنگ و قطعی اینترنت درخواست فیبر نوری دادم و حالا اومدن نصب و فعالش کردن.
با تشکر از شاتل بابت سرویس خوبشون؛ در واقع قبل از نصب اینترنت نداشتم، ولی الان با سرعت خیلی بیشتری اینترنت ندارم.
©
itsmralii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lnhodwfkk9oXgQ0iE66yZGqu8hPJ5_dop-L3quhl0i-QXX56uilgODAgHIqJBVEajgOOkn-pqL2NOGzFVIEmQH2jo0TUhDHMv2NlHJxZmMsnem-JGYh6ghF10utIT4jpVFKPt2fygU259UJItsrNngD4gLG2eeKgNlCelehgWJbL7bNLLMMEzUIRbWqUSIMyBv6r_8YOWuN3M-N0aZ0HWyRIXlTxAo4kty-UIlH-FeK4rnPZX7FWtp6CL0fm4kOxjQlnDdrGS0ZycWKLqBQPVhIqW75kJJQ5449Su_YzR6DiVOUTG_pxnMO8inPozZ3KGQJVcIc26F3HlZDZAD2iBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NDYO8UEVDWrPekplfJ6InL8YGiyv378c8-OJtH3Dq0aMQUNSg0FW_sAqyAEnNklb7oFIxVfLEL-M_Z146GstBBvLXQi4EoK98rt1z6ot6N-gW_jEremBddKfKG9HrbxeczRmpK8dk2-r7zU3KK-OYqFt52WyCAi00aGPRhEVz025bCzuUD330fEl3znayt_GYMs5ZwdFVsmUgco77v6hZVNqbAbsQsxahSKiSlPgsFF12aIgFmq3zii-Wi2TyHSbPf8d5RmXjneNsQ6tJ1lo848p9JS2yH6x3u1WLpnpkYYgA5lJ2qEEjtG4WNFgPgJIegFLfNLXvqDqZzX0s1KL6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteDNS یک کلاینت متن‌باز و رایگان برای اندرویده، که امکان اتصال از طریق DNS Tunnel رو با دو حالت Proxy و VPN فراهم می‌کنه. این برنامه با تکیه بر MasterDNS و StormDNS طراحی شده و میتونه بدون نیاز به تنظیمات پیچیده، ارتباط رو از طریق تانل DNS برقرار کنه.
👉
github.com/iampedii/WhiteDNS/releases/latest
💡
t.me/PersianGithubMirror/4637
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ikDEpWnt8gTWrKR5MX_JlaMqIRmZqKxpMb8IC-DjDJaMNgoHXseMQVVc4VU8XtZcXqLnjREzJDpCB3wuhkYQwJCsWA2jFf_nYdy1_2Y2ZxNaeByxZHJ9q-XjvDr_uDj95FD71Y4tT5kb5YdIG1zFG7wwiJlItfZIb9_5AmoNtcmgrHpEHtYuHb0KLm25kWLCPYQfWE6NxaU7SRS4oGj31vpRs8qgDYd7N-JIYhdShxXhCjINBzrRsJlgaXlAhgazSP-PYqESQU0-dVN8mDCOQo6MKfEF5um9sNIXur3EF2mjEpeahx3ZdvTerL9Ml1RMsMe0HYaMvnKsiMPqZiugCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز که نت‌بلاکس عدد روزهای قطع سراسری اینترنت در ایران رو اعلام می‌کنه، یه عده میگن "خب شمردن که کاری نداره، خودمونم بلدیم".
ولی مسئله فقط شمردن نیست؛ مسئله اینه که نباید این قضیه عادی‌سازی و فراموش بشه. اگر فکر می‌کنیم راه مؤثرتری برای اثرگذاری وجود داره، خوبه؛ ولی سوال اینجاست که چرا تماشا می‌کنیم؟
۷۲ روز گذشته و هیچ اقدام جدی‌ای برای کمک جهت اتصال آزاد به اینترنت انجام نشده، کسب‌وکارها نابود شدن، آدم‌ها شغلشون رو از دست دادن و سفره خیلی از خانواده‌ها کوچیک‌تر شده. مردم برای یک اتصال معمولی باید میلیون‌ها تومان از جیب خودشون هزینه کنن و در عین حال بخش بزرگی از نهادها و جوامع حقوق بشری نسبت به تداوم قطع اینترنت، سرکوب، دستگیری‌ها و اعدام‌ها سکوت رو ترجیح میدن.
در فضایی که همه‌چیز خیلی سریع به حاشیه میره، استمرار در اطلاع‌رسانی خودش یک کار مهمه و همین گزارش‌های روزانه امثال نت‌بلاکس حداقل باعث میشه موضوع قطع اینترنت در ایران کامل از توجه‌ها خارج نشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این هفت کابل اینترنت جهانی در خلیج فارس رو اگه قطع کنید خیلی خوبه، اونا هم مثل ما اینترنت نداشته باشن، بلکه دکان‌های حقوق حشری صداشون برای اونا دربیاد و یه نگاهی هم اینور بندازن و دل ما هم خنک بشه!
قطع کنید.
©
ehsan_369
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2302">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rGg53UY_3PA9ZGmgZrogztHiyT_8P3LyzLYx491XMUqopihI1kvXNE2fybZgSraBMkVSCDynGI7-deoBe7phhqB_Inlz2XyQt8yNFt4emkpg-XRJ5JW-AlZZG86pwoMLCUlabLTgR8basa6k-g4oH6O8aqEJMRLMgZSdEfVClfRixfPIMHa6yDiq-P4n1iBgs-L5VuzZwaIR6MJOe0r6H7MWF-dqfs98uwBOi3DEmz5WZr9z6BJ12RH0hvJ7fNELr7ZqpTRvuzdZknUGvPX6Z5O72lp4gtYa7TFWyFACTLZ6P2Oki9nvhRv4Ex6EDGqY1PGFpa4SLt7m_w8NW_iEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gZobDVxkVkmNcTHNMVglpBBBaqkWwXadS0js5INxnZQKU8wmnmO2Lo3MR3pMLBIr6DkTc4MqxzwxCM-tTPaxzjjBqUiCDl3e_e1q6AKUh5jdUJJtLeBCl3LPFUe1_dQK7--xpgGk36txxlTan7g43sVfIfTy0FKDSSg885q2PpzuoyL6fKrjAw4hfRarXLndWBK1BIgJqRLeAQ_SRGhxI3RGW530eYsr071a10WsVTlkWdOmPos0X8H-iKBtA6DFN5quKUQAEa7AiPPf95b9s31cBMCkimiQHI-BoWrL8CVWOzAHqbV7aOI4sosZzsb4c7yQTYv6wN7Y56eez6Faqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pud0NfHmGAuTg93DWfOCsl9ehBt_PvLbaARM83t4RRLbVmVK5m4k3Nf5UEIZzPipgyineYVh_-if2gqdbzvxuLbYH7FIhnNH9wimBvRX11TWOUiqO5ee278frv_zB5mfKt3jJYCk4XDYAesJ22Eu4CeCLcBvUud_APCIywdPP9AYo49dzvUY16t42OYgGdnveqphbuG7ulBG0NQugJ7l8w8XDxlvMJLUkbCPYiQAfBazk3Nnj2VrOznZRdJJFbN-ox9OQ2Truqukil2APtg6YFYzaHMUtmYnyEK_1OsNs7Epvt-FpD0EP6eBM2BXazUtrpq0pj0fKCUJsE-uTFRCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۳ از اپ متن‌باز و رایگان TeleMirror برای "دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت" برای ویندوز، لینوکس و مک منتشر شد.
در این نسخه نمایش پست‌ها بهینه‌تر شده و مشکلات مربوط به کش تا حد زیادی برطرف شده، بخش تنظیمات به برنامه اضافه شده و امکان بازگشت به تنظیمات پیشفرض فراهم اومده. لیست کانال‌های پیشفرض افزایش پیدا کرده و علاوه بر نسخه Lite، یک حالت Normal اضافه شده که تلاش می‌کنه در صورت امکان تصاویر فیلترشده رو هم نمایش بده.
این برنامه فیلترشکن نیست و بر پایه دسترسی‌های فعلی وایت‌لیست اینترنت عمل می‌کنه، بنابراین ممکنه روی برخی از اینترنت‌ها قابل استفاده نباشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4599
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2299">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">افغانستان تست خدمات اینترنت 5G رو در کابل استارت زده، عراق تلگرام رو رفع فیلتر کرده؛ اما جمهوری اسلامی تا دقیقه ۹۰ درحال آزار و اذیت میلیون‌ها ایرانیه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/to_bSQswvCJBnrsBYPz5hX3CayFNXtK27FRiyF4-bLyE9zic6EL7H51-BwbOM9VYyean8h66xYjmaCuVM1EoMREriqFAXyMLoRNv0MTdK6eJKeK9MMUYMEuwNay0JNw6anguttI0xV7pLLLKmMBFeNYqFWUhyG0OUxmVP5Av6GJEm64VvYDmwI4l7ec1SDp6IavcesFs2KPua72xTpV_2JVta2SJxOqxWAfzWRKUr-VJ1jTyfo_7rwWWVwftq1kl9uGFwDGvvXIcW2FZ1881m1ov99Mf0T0__mnG-fP4AvjoGBwkb0e5CnT5gByxdqFV7-GfU9Hvj8ws1gzHIW-7Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی خاک بر سرتون (پیامرسان‌های بومی) که با اینهمه حمایت و در میدانی بدون رقیبِ جدی هم عرضه ندارین کیفیت خدمات دهی، پشتیبانی و توان زیرساختیتون رو ارتقا بدین و بعداز اینهمه سال سابقه، آدم نمیتونه ۸ مگ فیلم ارسال کنه.
بعد از خودروسازی، باید شماها رو هم دومین فرزند لوس و بی‌خاصیت کسب و کارهای داخلی دونست!
©
kamran_falahati
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2297">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جمهوری اسلامی ۷۱ روز هست که اینترنت رو به روی مردم خودش بسته!
روح‌الله مومن‌نسب (تئوریسین بارداری با ۲ گیگ اینترنت) گفته شرایط اینترنت به هیچ وجه نباید به روال گذشته برگرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kmvg7FikVZ4uFAGpOyLitTLie7xxjNgDtwL3qyJD3ZYoIyHDxN4rlfJzPpJL21-MN_PXxj_0TRfnt_sqWtBw0lb-GIYJ6xuEalClNLa4NHa7Pvgnti6YJWDCB-cieMgIs1gom4WlQGQSgTyg97JjlBu4ykfFNQPvui0riDT-yhpv8CP3albyTsA0TiUpa1tlnxMShaRNmwB1l795V7nlg79GxSIev17K67LLdzI70aVr9wfkGeRd0QYQu06uTf-vqctnqqFByD0ewwZ-jfb29FitUBvdhB8hwbbfHmAWeiI23vGuFHgT-ze9cfoeMlr5TRh-JC4skH1x6NmeWwmVZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان Pigeon یه فورک از پروژه تله‌میرور برای macOS هست، که از طریق اون میشه بدون نیاز به فیلترشکن یا لاگین در حساب، به محتوای کانال‌های عمومی تلگرام دسترسی پیدا کرد.
👉
github.com/MaroMushii/Pigeon/releases/latest
💡
t.me/PersianGithubMirror/4500
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DVEPc8AEOSmZWw8utS03o7EqrMN6LOZz_QLZEz4cJ0c79HPEXQtengz11MEvXVQfhDVSMQEP6OF-HyO3ajosf5Yh2N4dnRBl-ypSPsaYF1c84HtXoOcAesrngpw1P1nkl-b3Gh_MmQ4WIeoRGfq-akVGhq6HqbiWNQGtnkmpfFF8IGV3fRd9IOq7ZHHs9-3FA_RYbl7P6LQyjCR1ygYR6rUOW-utWqhqQzIHdKStSwxF4cDYoZJC2MNFldloAsHKtI0k9F09Ac51o5hux1omyw0wSNdWBdQrLhbBwUgqMpb8SRwjUrLLEky43YqaPuI_mcHDtIPk4TtrputxH7MSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Youtube Sandbox با استفاده از GitHub Actions بهمون اجازه میده که فقط با ارسال لینک یوتیوب توی کامیت‌مسیج، فایل ویدیوی موردنظرمون رو توی فولدر Downloads (داخل مخزن) ذخیره کنیم.
👉
github.com/iphoenixon/youtube-sandbox
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f5XJnXBrnElfodAVVwelpMOnQeSdsB5skHDae70bOKjrhyC4kdtkRte-au4cd5eSxQFita8L1tkIldd6wilRTH1BvXwk4WDo6OZ7qvFfjdgxCGfSW2D27DoXxtVkpCLy-3dSn4gNhO9klDw0I2K3mWv-VNhFOUxHRs5WSm_MnaKkrturVawsvUkP9OlFwji_cCH5byHvbU41zs2azk4xNN4wl3dEEsAwzBIXOaTgyBUpxyqQEBLfgsQrk4GwEaDgTTL6pHm776B7ZJS90znmpDwtELwlYGpYrwt7Y5DIrRfXSHKCD_udVDZs0LNxArit6NpjJpOVb8jtmqWaobnJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه گوگل براتون باز میشه و در وایت‌لیست اینترنتتون قرار داره، می‌تونین خیلی راحت با نصب این کلاینت اپن‌سورس به گوگل درایو در اندروید دسترسی داشته باشین.
👉
github.com/aleskxyz/Round-Sync/releases/latest
💡
t.me/PersianGithubMirror/4489
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fn-Igwq78KF-I-OQYlL3iENjwf717m0iFfnY3_Qzwqja_RjdxrWneUi4CfK6917tzlxPdvA3Ye3qrA62Cv2JWZBruhudhnlRfSxbtcuogZUMPk52np1nLlanvY8HX1rRuW1IjX2KyioUp1WlTWxK9XruqHz0wSB_jEmuCh4WBCMprPkQzNHco6gz_S5z45KlgIRGWykSjzEquAP5KHtQvVtQHLwdCRi9foMJDXFW1Wc_vFSYLY1KSWw_Eue0xisUjxYh8NAPvyEA2-LG9bIqcDlOJBasQoSry1wlYan2Yx_BJk6jMVmrdbHjDz-xzgYp4Ny2A7ILyeT6yT3F5dYLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید کلاینت ZedSecure از طریق گوگل‌پلی در دسترس قرار گرفت.
در بروزرسانی جدید این‌برنامه پشتیبانی از پروتکل DNSTT اضافه شده، هسته ایکس‌ری رو بروزرسانی کردن، بخش تنظیمات تکمیل‌تر شده و یک‌سری از مشکلات برطرف شدن.
👉
play.google.com/store/apps/details?id=com.zedsecure.vpn
💡
t.me/PersianGithubMirror/4496
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2292">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">۷۰ روز است که جمهوری اسلامی با قطع سراسری اینترنت، میلیون‌ها انسان را عملاً گروگان گرفته است.
این یک اختلال اینترنتی نیست؛ حمله‌ای مستقیم به زندگی مردم است. کسب‌وکارها نابود شده‌اند، معیشت خانواده‌ها آسیب دیده و ارتباط مردم با جهان قطع شده است.
در سایه همین خاموشی، بازداشت، سرکوب و اعدام ادامه دارد؛ بی‌آنکه صدای قربانیان شنیده شود.
اما بخش بزرگی از جامعه جهانی همچنان ترجیح می‌دهد چشمش را بر این فجایع ببندد؛ چون واکنش نشان دادن هزینه دارد و سکوت، ساده‌تر است.
For 70 days, the Islamic Republic has effectively held millions of people hostage through a nationwide internet shutdown.
This is not an internet disruption; it is a direct attack on people’s lives. Businesses have been destroyed, families’ livelihoods have been harmed, and people’s connection to the world has been cut off.
Under the cover of this blackout, arrests, repression, and executions continue while the voices of the victims go unheard.
Yet a large part of the international community still chooses to turn a blind eye to these atrocities, because taking a stand comes with a cost — and silence is easier.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2291">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">قطع طولانی اینترنت تحقیر اکثریت بزرگی از افراد کشور، یک‌جا و باهم است. اما این بین، گروهی که شغلشان به‌هرشکل به اینترنت وابسته است، تحقیری عمیقتر و نفس‌گیرتر را تجربه می‌کنند. با آن‌ها طوری رفتار شده که گویا شغلشان "مهم" نيست. حرمت ندارند و می‌شود با زندگی‌، زحمات، اهداف، آینده و برنامه‌هایشان بازی کرد.
©
DevYara
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2291" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2289">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بر اساس گزارش جاب‌ویژن با عنوان "تاثیر جنگ بر بازار کار"، محدودیت در دسترسی به ابزارهای اینترنتی موجب اختلال یا کاهش فعالیت در بخش قابل توجهی از گروه‌های شغلی وابسته به اینترنت شده و بیشترین کاهش فرصت‌های شغلی در گروه شغلی دیجیتال مارکتینگ و سئو (۸۳ درصد)، طراحی گرافیک (۸۲ درصد) و ترجمه و تولید محتوا (۷۹ درصد) ثبت شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2289" target="_blank">📅 12:07 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2288">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JPxPhv_pveUv2Q7t4BF-Uj-pFpA6r7zY9ZiVrdEMdk8w13RqcCU9oq1YH3lu-qpmpRTZgXZKP2ggoJ-wkKESMgx_iNt-NxCN9YpwUbiUefgjbOJ45jt9pbH9ctQy-EJYJZzXevzlUQ7EJ5Px51t0UpaNDEEYx6tVPCngCqGWQthMpado3-dqRx-aCIPEV1MnhQLZ536qV8tAqQEHiCVoVDpDhcnU_0uXMKmBUswjB4jDlD1xaJM92Af0rkjkHReIcpTZ5jLK8rebxTv5kJnNqcA5ZQXJaDY8nXKRWy2a3tmBtkMgSbkd1pB8xkKM39ejP7NQ4JKtd5LCHt-Y8MDSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی شاکی است که چرا با وجود اینکه که پول داده، تیک آبی اکانتش حذف شده و ...
در همین حال میلیون‌ها ایرانی پول اینترنت دادند، اما بیش از دو ماه است که یک شبکه داخلی که فاصله زیادی با مفهوم اینترنت دارد بهشون تحویل داده میشه و از دسترسی به هزاران سایت و سرویس محروم شدند. سانسور اینه!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2288" target="_blank">📅 12:02 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2287">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وحید فرید، کارشناس اینترنت گفت: ما تجربه قطعی اینترنت را در دولت‌هایی داشتیم که به ظاهر حامی اینترنت بودند. خود پروژه شبکه ملی اطلاعات یک قدم به سمت ناامنی دیجیتال است. کسب‌وکاری که اینترنت می‌گیرد از نظر مردم رانتی است و روی حقوق مردم پا گذاشته. حاکمیت با قطع اینترنت به جامعه سیگنال ناامنی می‌دهد. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2287" target="_blank">📅 11:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2286">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سمیه توحیدلو، عضو انجمن جامعه‌شناسی ایران، قطع اینترنت را از منظر اجتماعی خطرناک توصیف کرد و گفت: در زمینه قطع اینترنت حاکمیت هزینه-فایده انجام نداده و متوجه نیست چه میزان خشم تولید می‌کند. آنچه در این وضعیت تشدید می‌شود، شکاف دیجیتال و محرومیت نسبی و شکاف حاکمیت-ملت است. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2286" target="_blank">📅 11:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2285">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sBJMLo8Rvr_liSzoJ82vE61yP4z_sJ4ParWwqAW6xSmLs3_ku_MaeMi3kOdoKlMyrfqs2f35Z54Wprpeo4vYzrJRVqn1jMlwi_5EH7jgEn7blPN8Q6zqiS0cPNjCgR34BS3BWgwNyP2EELQnOlDuqJ0LCPNJHGerK_vtJD0twjmcXTmq6IBwd6p9zyqLUijo0hwd8RyTH-HCfOD0UKIqIC-oTTpyAGuTzQnTzgoUw0dB11jO9pMFQW6mzny340C_OUMN_-nmqosA8lI3XjiHFMzfn4FGXZkP2KUZPtVTxZrIWIBBgt3sUdg2XIW1MXE0OELzUysG8B6R2skZfaGNmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شرایط فعلی اینترنت ایران که روش‌های عمومی دورزدن فیلترینگ عملاً کارایی ندارن و اسکمرها و کلاهبردارها زیاد شدن، مدتیه یه مارکت‌پلیس برای خرید و فروش کانفیگ راه‌اندازی شده تا خریدارها و فروشنده‌ها در یک بستر متمرکز و نسبتا شفاف با هم ارتباط بگیرن.
طبق توضیح تیم دیفیکس، خودشون فروشنده نیستن و تمرکزشون همچنان روی ارائه و توسعه سرویس رایگانه. این بخش صرفاً برای وصل کردن فروشنده‌ها و خریدارها از طریق این فیلترشکن و حذف واسطه‌ها ایجاد شده و فعلاً هم برای تراکنش‌های رمزارزی مرتبط با ایران کارمزدی دریافت نمیشه.
در این سیستم، مبلغ پرداختی نگه داشته میشه و برای مدتی بعد از تحویل آزاد میشه، کاربران میتونن به فروشنده‌ها امتیاز بدن و تجربشون رو ثبت کنن و کانفیگ‌ها هم بصورت رمزنگاری‌شده تحویل داده میشن. البته محدودیت‌ها خرید بصورت رمزارز رو دشوار کرده، اما افراد خارج از کشور میتونن برای خانواده یا آشنایانشون داخل ایران خرید انجام بدن و فایل کانفیگ رو براشون بفرستن.
👉
market.defyxvpn.com
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2285" target="_blank">📅 11:26 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2284">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=Tnjn_9t9g_z2eSvMADaR6Ug1f9kzzm0XPWn0FJ-hoYIw8-raYSwbs87o4voB0rDESqeHTJ8vq3h-13cOPDurHM80G-Tjbe4iBAmlZIeTDX9Wg8yU2gETfCzytWgTRqnvRkYwLOvd8u6Eau4U6u2dWCZIR6KxtQQghbK04VHt4AtFX75sBNRTzZNpuamv8FjzNIyef5bm-8BjwUc-WAUhdtqKVVeZT2LSXglVZb42hf4DUsPUo7nAFJT2FYG_9OwzUJoAvpuEbVKb3tHgKuxkX9rhOPXI78mDU7Hi0txAY4x5jw1Xv03aEIDP7upbXX08XSOUzi5lQIUwe5o16aUsEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=Tnjn_9t9g_z2eSvMADaR6Ug1f9kzzm0XPWn0FJ-hoYIw8-raYSwbs87o4voB0rDESqeHTJ8vq3h-13cOPDurHM80G-Tjbe4iBAmlZIeTDX9Wg8yU2gETfCzytWgTRqnvRkYwLOvd8u6Eau4U6u2dWCZIR6KxtQQghbK04VHt4AtFX75sBNRTzZNpuamv8FjzNIyef5bm-8BjwUc-WAUhdtqKVVeZT2LSXglVZb42hf4DUsPUo7nAFJT2FYG_9OwzUJoAvpuEbVKb3tHgKuxkX9rhOPXI78mDU7Hi0txAY4x5jw1Xv03aEIDP7upbXX08XSOUzi5lQIUwe5o16aUsEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2284" target="_blank">📅 11:01 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2283">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وارد روز شصت‌ونهم شدیم. میلیون‌ها نفر رو با قطع سراسری اینترنت گروگان گرفتن و بازداشت‌ها و اعدام‌ها در سایه خاموشی دیجیتال ادامه داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2283" target="_blank">📅 08:16 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2282">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v5hT2RzAbdY59rwuTL6DaZoh4pNkEsl3oRPpiN0Z7F0F2AAVhkQ-NKuuL-SJUPDXoUZnPBcq0RpUzWR9w3G_CvO2j2yb-qd_BwhkTP702Tq0tpzwE8SGCd0A_LIXTHaUCSkLj7mZTvgXYDQ6GwtZqvdw-ssLLg5GjaQv9szC2s6qWZpVX4THQweD1b74qOxtHCBlHqwI9zzKLUl4BdMtE-MVtrw4Lke5agWMRtXH3vfR_wTr7eMPY_JMI6UOl_-noLlGpEtDO793-LWF1dlCiy-33sn4ZAa7IdJNuxpGXql19wcSZ1c0sQ8x7uk1bmL9i4o-pgtqpmipjjIbWuWWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از اپ theFeed امکان فراخوانی محتوای کانال‌های عمومی دلخواه فراهم شده و پشتیبانی از اندرویدهای قدیمی‌تر، حل مشکل رندر نکردن نظرسنجی‌ها و ...، بخشی از تغییرات جدید هستن.
👉
github.com/sartoopjj/thefeed/releases/latest
💡
t.me/PersianGithubMirror/4273
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2282" target="_blank">📅 18:20 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2281">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mnb86DmyfSYCvZO8yCiZiXYWL8pD9JOQwCKdr5KGcRk0zLERiblN1FDZaLc0oc2XpbBFlo-7C2_jgH1HhU-oAlz0C5ochbAxSE4wI9_iaHWKDQYtR-fTxvFoymPzkIiJRNqIxXE-WPb7vYVLcM-ygKPlea2NuYpO0liZTwsj2_O3qeEjM_OW6bsGvp5q3GhMiujme3jlJx7U_VNhrEzvF6o1LaIzVYrJe8uuUIn3SPNRn4-RpL_6-AdF0nI1uKxoFMdIt421MoXhLU9uKPSIeN1bOHnFHmAMgMXGG_w-JyowFs6IJRlX-BUdiYtPLljNy7DmQFxE5flhnoBkdIaL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای آسیب پذیری اخیر کرنل (
Copy Fail
) فارغ از اینکه آسیب پذیر هستید یا نه، آپدیت کردید یا نه و کدوم لینوکس و چه ورژنی هستید، همین دوتا دستور رو واسه محکم کاری بزنید و تمام:
echo "install algif_aead /bin/false" > /etc/modprobe.d/disable-algif.conf
rmmod algif_aead 2>/dev/null
ریبوت لازم نداره، ضرری هم نداره؛ چون به صورت معمول شما به این ماژول کرنل نیازی ندارید.
©
tiosus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2281" target="_blank">📅 18:11 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2280">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">قطع اینترنت به بهانه امنیت ادعای مزخرفی است.
پشت پرده اینترنت پرو و سود حاصل از این رانت در جیب “ستاداجرایی فرمان امام” و “بنیاد تعاون سپاه” می‌رود.
حدود ۹۰٪ سهام همراه اول در اختیار شرکت مخابرات ایران است و مهم‌ترین سهام‌دار مخابرات هم “کنسرسیوم اعتماد مبین” است. این کنسرسیوم متشکل از “گروه توسعه اقتصادی تدبیر” وابسته به ستاد اجرایی فرمان امام و “شرکت سرمایه‌گذاری مهر اقتصاد ایرانیان” وابسته بنیاد تعاون سپاه است.
در واقع گردانندگان اصلی این مجموعه و به نوعی مخابرات و همراه اول دو نهاد ستاد اجرایی فرمان امام و بنیاد تعاون سپاه هستند.
©
yasharsoltani
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2280" target="_blank">📅 09:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2279">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">۶۸ روزه اینترنت بصورت سراسری قطع شده و در همین تاریکی دیجیتال، بازداشت‌ها و اعدام‌ها ادامه دارن.
قطع اینترنت فقط خاموش کردن ارتباط نیست؛ پنهان کردن حقیقته، اما خون با هیچی پاک نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2279" target="_blank">📅 08:21 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2278">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YPfrbwc5r3zWpGWoFgyX5iHzm2zyCHaC_fWnwP2HiymjejGZo1sYGhnZWH0_mPVJMQ7zIU6CS8U6yC3W4hoz7Cgh0uxHywL3dSsBVQ8cfRkhNHiXF33bHk86UzwCXtmzKR3gF25pCmcSWuhqTrOrvYS8V3JOz8dJOZWRb9srAf9g2ZekzgzhZ7WLsxKqM0uxm5527MHl_2-dFqR9tRxvjVpFs7cEKCsk5aomEmHt8msucGByylknY7EI8BdcCUYX2yvjIEYFLS80uBn7uw7Ki9cI1k0XvMVGn10B3DfYKTk1WPWnmWNv61QyFyXkWsmobY9SukYQ2-Fp3vCZuZNfow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۲ از اپ متن‌باز و رایگان TeleMirror برای دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت منتشر شد.
در این‌نسخه بیلد لینوکس و مک هم در کنار ویندوز اضافه شده، برنامه چندزبانه شده و یه سری از مشکلات برطرف شدن.
این برنامه فیلترشکن نیست و به وایت‌لیست فعلی اینترنت متکیه، بنابراین ممکنه روی یکسری از اینترنت‌ها کار نکنه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4295
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2278" target="_blank">📅 20:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2277">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g3_yfcKynLprEQP_UudiZXXfMM68bEYfabAhee--w2NYPZGl26kMR6AjQWoSwzGwFz_-uLqQi2Q6z8AWU5CZGZt7Ez7gHuMY7ea8L578AvPwlJ9-TiGfIYi2p-0H4LEjR0bttE6D1ad5bDnQx-yZ9TAjVJWHH7CV0s0j8J90Q91yVzBmmairXs45UDM7qSp53MLOItekAzKYziRg3Aex2EkS04Mf59YAqr5DmWixOZURhqujS4FnzXBRj9Nuzpp9yvKRPY36u3meJSfqGfx005UwejRhW-PNUULy5Kw87Bgwh7JpRQ_Kcs__HCDNeBaTyrChT_W2LWRFMZzaDbUqCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک آسیب‌پذیری بسیار خطرناک در هسته لینوکس با نام Copy Fail (CVE-2026-31431) شناسایی شده، که به کاربر عادی (حتی بدون دسترسی sudo) اجازه میده تا کد مخرب رو مستقیماً در حافظه (RAM) فایل‌های سیستمی تزریق کنه، بدون اینکه تغییری روی دیسک ثبت بشه؛ به همین دلیل بسیاری از ابزارهای امنیتی قادر به شناسایی اون نیستن.
این حمله به سادگی و با پایداری بالا اجرا میشه، میتونه برای فرار از کانتینرها (Docker / Kubernetes) استفاده بشه و تقریباً تمام نسخه‌های لینوکس از سال ۲۰۱۷ به بعد (Kernel 4.14+) رو تحت تأثیر قرار میده.
اگرچه با توجه به وضعیت فعلی اینترنت در ایران بروزرسانی کار دشواری هست، اما توصیه میشه در سریعترین زمان ممکن سیستم خودتون بروزرسانی کرده و وصله‌های امنیتی هسته رو نصب کنین.
©
Bamdad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2277" target="_blank">📅 17:02 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2276">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a0l-Rj_2KC19zVGjWg5BOekSsDAbFlAYEdnFZY7CBoATOuaeDNMDN_RQPQB3T2jpGgGHLrapMlsuqNCjmdk7SYmn3VZhNMfcdprAMSAoNVVKt7A9CwDTwAtbJaLClzE7uZu5CN17UB0gzAlThYiT0AnDM_Trl9EYnOWDkZVB5muKhKxzAf5LzQTtmVsuQn9SlI3gX_iV2UgnGuWEGqvAJiiru1UWyc1xtsXCvTRVxdeTIrEadBf8s1caP88RV7JlDQAtYEjPhg0Dwn4kAsEAsNHPw1_vvjjm-kUb4fmwQEcsNurNYXiTqLQ2fDXO6HHFRReByyEa5rEPap6p3Faf8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل آموزش ساخت فیلترشکن شخصی به کمک گوگل و کلودفلر از طریق متد MHR-CFW منتشر شد. اخیرا یک کاربر فورک جدیدی از این پروژه رو به زبان GO بازنویسی کرده که مشکل سرعت پایین، لود نشدن برخی از ویدئوهای یوتیوب و همینطور یکسری از خطاهارو برطرف کرده.
👉
github.com/ThisIsDara/mhr-cfw-go
💡
t.me/ircfspace/2259
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2276" target="_blank">📅 16:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2275">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">توی خبرها دیدم که دستیار ویژه وزیر کشور گفته "محدودیت‌های اینترنت احتمالا تا ۴۵ روز دیگه رفع میشن"؛ بنابراین بنظر میرسه باید خودمون رو برای کابوس ۱۱۰ روز قطع اینترنت آماده کنیم!
😐
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2275" target="_blank">📅 16:42 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2274">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wAxX80RXo4CCIxqWlaouXuhLFlwD_cIwx9ufKo8etO1thegxbkdnp1fkckMmJG2fEicz0utgCuHPM8wEYVY9khHQnr8-un3ZMvTJvD9jTBL1Bmd4Vs94yyvH6Lv_nXE_-PnQlNSD1FGRJ7frj0n_Q17hpOqPgCN8Ve5RFfkpAPjLjsIc69urXhm82uMm_P0sd9-Lgv4_pUTthf-TT30m2-7kGuwWCxhvawJjQLbu83EHIIGiWZUtarK90HmvI_42D-GDqdqWAj9a7shsJyhE-uTmDW3JqMJPz7VcRCw8Ml3Buii8aj_aty2L0lqihzjSHACDk6OBWjItLodeve3WzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز خبری در رابطه با قطع اینترنت سفید خبرنگاران توسط ایرانسل منتشر شد، که روابط عمومی این اپراتور گفته نقشی در این ماجرا نداشته و "هرگونه قطع احتمالی دسترسی متفاوت برخی کاربران به اینترنت، لازم است از نهادهای تصمیم‌گیر پیگیری شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2274" target="_blank">📅 16:38 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2273">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UFjdqLVjGdKAthPtXT7GyWLjJBUE5kNmcNJHQijSFwnLLcMFwWZq_o2e6677YoxNRWFHlWFAz7CSV14uOW-p_dMeOfZPblPk2mdehr7jnmj8mvbbQg46NXgTa-gXplPd8wUc0i3dAjUCncxv_2mTXxehlpqaWouPAxoID4z9oXeP39Beks7TEjPjeprBDz8gctMxVdTqPnl2QNR7mQiFHRB_iz7Xo8zlJAYcsZhOvWTDb7ihEqK6-vsD3FTw0iMMJmP_r2GI2oGeVBYFPzru8urvLw1f4MBKqhl2kv-O47PDllmi0ISAvQZuMAnWJR2WdvsMLNSm-kwPacfVLJuCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع اینترنت در ایران اکنون وارد روز ۶۷م شده است. اقدام به سانسور دیجیتال، پرده‌ای از سکوت بر افزایش گزارش‌ها از اعدام‌ها می‌افکند و قربانیان را از دیده‌شدن، پاسخ‌گویی و حق ابتدایی شنیده‌شدن محروم می‌کند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2273" target="_blank">📅 12:26 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2272">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">توسعه‌دهنده اپ SlipNet متاسفانه از توقف توسعه این اپ کاربردی خبر داده و در بخشی از توضیحاتش در مورد علت این تصمیم، نوشته که "توسعه ابزار آزاد، رایگان است اما بی‌هزینه نیست. متأسفانه در جامعه نرم‌افزاری ما، فرهنگ Donation هنوز جایگاه خود را پیدا نکرده است. از سوی دیگر، جنگیدن همزمان در دو جبهه (فیلترینگ از یک سو و خشم و کامنت‌های تند برخی کاربران در روزهای اختلال شبکه از سوی دیگر) توان ادامه مسیر را از من سلب کرد".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2272" target="_blank">📅 12:22 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2271">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کاربران میگن ابلاغیه‌های مشابهی رو از قوه قضائیه با موضوع "پرداخت وجه و تسویه اقساط"
دریافت کردن
، که توسط "نوآوران پرداخت مجازی ایرانیان"، یعنی نام تجاری دیجی‌پی (زیرمجموعه دیجی‌کالا) ارسال شده.
با توجه به اینکه ثبت اظهارنامه آنلاین از طریق سامانه عدل‌ایران امکان پذیره، احتمالا تعداد نفراتی که پیام‌های مشابهی گرفتن اندک نباشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2271" target="_blank">📅 22:24 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2269">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ndfUNO33VaYd94l4S9qSep8AKlp-6MTelOk653Ti2ad0sq_6P_cMs8WIweVoDRyU2Qi5Ln4XeuecEhbxXwz1cun1JrQ4WamAAjIotOi6ShH_BPZZMx_3ZoIxisVcXFyAwF6MgPTqYu7ffIEeFA6ZaeycL6-fxUHVSwEhxzYd7Wq6py4o4BeDBEdWKLNoVKJ-kXpKPYDaXLZYJo-l81UZ4d-SpYqwu1mKKvNsXFahnI6qXxzNqlHnTUbdVObvzjyFCV1N1Qx4lrM0lt_QFlmLfqlRx0bI5_BBSPAfjl-qCrrnj20grXrLOlfp9ShsOIbwIVhcG0M_-AD3MsxohAH5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبری که امروز در مورد "ثبت رکورد ژاپن در رابطه با سرعت اینترنت" در صفحات مختلف منتشر شده، مربوط به حدود ۹ ماه قبل هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2269" target="_blank">📅 22:15 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2268">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SnOfEQwINuqsJUv2-PrrnAf7gIaz_mttYLegf_E7tU5OQs1eZvct3EQTmoASMX0R8vX4GEGoymYj3d8soqNlQ6Gg7Axia8Tm5t5_1FjHGPJVqZqM2E8QiwRSAGVlfTKACcJsbPEQ8L703Y7erOLaOhw5iV_lpU-bG_TE2UMgD826ssYGJRjPTrdCn3I_70S1u77fWqZk8xMr6BgQFe2glUdVqySDxtu0gTqszued7m7o7X123Irx4pCEkQBilk5Ccb-YjbJq3ZIk_dDrMay_JsW_H97kNQRolFLtxy9u1T1pO3i7vJsp_AtBI-o3zj0q1c-SJfEgqCdBT_KW6dpYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیجی‌کالا خیلی اوقات در رابطه با خسارت‌هایی که بصورت مستقیم و غیرمستقیم به مشتریان و تامین‌کنندگان وارد میکنه پاسخگو نیست، اما در شرایط جنگی از طرف سرویس دیجی‌پی بخاطر ۲۰ روز تاخیر در پرداخت قسط اظهارنامه قضائی میفرسته؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2268" target="_blank">📅 21:57 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2267">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OAL4-nw_sn_mPLjdJliLryHpk_QH96lxqkjViBL3UqGOTaIamSxB6UfdjC877-b_jwode8j3t9Zb06bYZ7_ROj2_Y8YT_lPrscFjuSB3VLbn3AObyHRZJayXH5Y6Ds1zYNkSuKWvnVgTcIRVyhY1HbMU3WJSQSq3Pn_MxVzMaHxYx5ZmCWJU9AkaHIS4XauABu2ObuhQAveJksH6gdaMNcszaLDenfNNEgjD2-ig84O1IiTJSkh64PPtKX7cKhfE-EeECQIQc-3LXDbOsUlEhYXYm9K8Mrp27FkLHf2N0RiSdYsPVyalyN45Ofof6rCjHI4w6P4-p6-8kjPPsPDWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ TeleMirror یه تلاش آزمایشی برای دریافت آخرین مطالب کانال تلگرام خودم و سایر کانال‌های موردنظر در شرایط محدودیت شدید اینترنته، که سعی می‌کنه با چند روش مختلف پست‌ها رو بگیره و نمایش بده.
این برنامه رایگان و متن‌بازه و فعلا می‌تونه برای دنبال کردن اخبار تلگرامی بدون نیاز به فیلترشکن، یه گزینه موقت و کاربردی واسه دسکتاپ باشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4128
۱. این برنامه رو برای کانال خودم نوشتم که در لیست بصورت دیفالت وجود داره، ولی هرکی میتونه سایر کانال‌های موردنظرش رو وارد کنه
۲. برای اینکه ریت‌لیمیت نخورین پست‌هارو برای مدت کوتاهی کش میکنه، که با هربار مراجعه یک درخواست به سمت تلگرام ارسال نشه
۳. به وایت‌لیست فعلی اینترنت متکی هست و فیلترشکن نیست. ممکنه روی بعضی از اپراتورها جواب نده، یا خیلی زود از کار بندازنش
۴. برنامه دیتارو از کانال‌های پابلیک میگیره و به هیچ اطلاعات شخصی‌ای واسه تلگرام نیاز نداره
۵. در حال حاضر نسخه ویندوزش رو منتشر کردم، اما اگر بازخوردها مثبت باشه برای مک و لینوکس هم ارائه میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2267" target="_blank">📅 19:53 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2266">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">در شصت و ششمین روز از قطع سراسری اینترنت هستیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2266" target="_blank">📅 08:59 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yw2bTTRYbwVKykTsGUWYMMbWsNLHib0z6SpXe-5fNuk9dY_iwhkSznEcRvPl34rPMOk3aT0QLpfYZn2Ye-gFVCsFOgLHBMs_TEWyO1TeGXkHUxoE2mfP9ArzYKSXYKNDHwgDwilJsbR47Yt-gBeGw2esByM5tBzYD-bCY9LKTNagS_aCCUMMYKOgEtNFni3YEf4e3Ul_hWnU7T0raUVEp60wiAv_iUXKU6Vmw0BfgBZ0ERsIQf3ix6enNx9Rio55TNavtTp3djecVru9aa4sdhpm4buqjw1RrEavaJibYGSHbNZmPqOAYMNyq4YlyTQcsO9AbansXbzg9K6KFlVQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌بی‌سی در گزارشی گفته که شبکه‌ای مخفی در حال قاچاق تجهیزات اینترنت ماهواره‌ای استارلینک به داخل ایرانه، تا کاربران بتونن محدودیت‌های شدید اینترنت رو دور بزنن.
در این گزارش اومده که افرادی در خارج از کشور این دستگاه‌ها رو تهیه کرده و بصورت پنهانی وارد ایران می‌کنن، تا دسترسی به اینترنت آزاد فراهم بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2265" target="_blank">📅 08:53 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انجمن فین‌تک در بیانیه خود استدلال کرد که رویکرد ایجاد اینترنت طبقاتی، گره‌ای از مشکلات زیرساختی باز نمی‌کند و در عوض، اعتماد عمومی و پیکره اقتصاد دیجیتال را با آسیبهای جبران‌ناپذیری مواجه خواهد ساخت.
این انجمن از نهادهای تصمیم‌گیر، به ویژه وزارت ارتباطات و شورای عالی فضای مجازی، خواسته که به جای تعریف طرح‌های تبعیض‌آمیز، بر بازگرداندن کیفیت به کل شبکه اینترنت کشور و صیانت از حقوق کاربران تمرکز کنند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2264" target="_blank">📅 08:51 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Abs0ZG1rS1450xi62Ldt0Pu2rbtioHo316UaTET7dfHP69FFZTxjlfXdA6kFy-eTzqzABr4QJmU2CpzjKfiy01MUM-qjJU7WattBEERzqnaf4QRI4KZsW5WD2tufdBzob4CC2jHAISSKrkfZx_sdz1iCMt7tIQHJRhcqez6t_BbP9V0DHJuawNXabKaGMfDdvccstoNihOJAL8p-AJZrmCxHNRLseqQgJ-iA4ffX5CvE8648x8l4sGxsRnC_fDm-Ze34ABBrs5x8RKhRs7ll8ZYGR5_w0Zu2s5sprKONZwk8nNEtPcV9kBZA2KEZRRRh5eQBTomyiYwwy1sKfnjVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌ها نشان می‌دهند که قطع اینترنت در ایران وارد شصت‌وپنجمین روز خود شده؛ این در حالی است که نگرانی‌ها درباره وضعیت حقوق بشر در کشور رو به افزایش است.
از طرف دیگر دسترسی گزینشی و سطح‌بندی‌شده برای عده‌ای خاص برقرار است، اما عموم مردم همچنان از ارتباط با جهان خارج محروم هستند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2263" target="_blank">📅 11:13 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بلومبرگ در گزارشی نوشته که قطع طولانی‌مدت اینترنت در ایران دو پیامد اصلی داشته؛ از یک‌سو توازن قدرت رو به نفع نهادهای امنیتی و نظامی تغییر داده و نقش اونها رو در مدیریت امور کشور پررنگ‌تر کرده، و از سوی دیگه فشار قابل‌توجهی بر اقتصاد و زندگی روزمره مردم وارد کرده. در این شرایط، دسترسی محدود به اینترنت نه‌تنها ارتباطات و جریان اطلاعات رو مختل کرده، بلکه کسب‌وکارهای آنلاین، تجارت و خدمات وابسته به شبکه رو با رکود جدی مواجه کرده.
برآوردها در این گزارش نشون میده زیان اقتصادی این وضعیت فقط به تعطیلی مستقیم کسب‌وکارهای دیجیتال محدود نمیشه؛ اگرچه این بخش به‌تنهایی روزانه ده‌ها میلیون دلار خسارت ایجاد می‌کنه، اما با در نظر گرفتن اثرات گسترده‌تر مثل اختلال در زنجیره تأمین، پرداخت‌ها، تبلیغات و کاهش بهره‌وری، مجموع خسارت‌ها میتونه تا حدود ۸۰ میلیون دلار در روز برسه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2262" target="_blank">📅 08:37 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">روز شصت و چهارم از قطع سراسری اینترنت.
لعنت بر جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2261" target="_blank">📅 08:35 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کاربران شبکه‌های اجتماعی از جان باختن حسام علاءالدین، شهروند ۴۰ ساله که گفته می‌شود «به‌دلیل داشتن اینترنت ماهواره‌ای استارلینک» بازداشت شده بود، خبر می‌دهند.
بنا بر گزارش‌ها، او که پدر دو دختر بود در اثر شکنجه در بازداشت جان باخته و پیکر بی‌جانش را به خانواده‌اش تحویل داده‌اند.
©
indypersian
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2260" target="_blank">📅 19:31 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نحوه ساخت فیلترشکن شخصی رایگان به کمک گوگل و کلودفلر، از طریق متد MHR-CFW ...
📽
youtu.be/L3lJZrAqqUQ
💡
github.com/denuitt1/mhr-cfw
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2259" target="_blank">📅 19:22 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2258">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s563G4m_d28vxTJUptBcUvPK5tt8x57oZos1U7Y5fdhcvvg8IV9CTT9UA7TrkYVbM75514IjdFL-uJYOnE0ZDhid7OsaZ6DVl3rgGwG7O5fHbhu_zEwY0zG2La_NQvYicYLi2VAQ-FiKHwo1UFa6rGt2LDG0Oh4v7x67DLYvjVLh8lK7CUDXwHv40do0S3Ru9I0btl8hAkBLAbl4bjC_jQWN6z5bpiOhVZs1pQrpjyoY29zoELMmSpJFnXx4N65dbncsjwENXWDu1NBxh_QfQEK65rn9_t_mHMhcbAdOBJIoQ5QnKBdn8gZ7vTvhaXUD6FKmWaFii74nMBVzUvbz3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با روز شصت‌وسوم از قطع سراسری اینترنت در ایران، گزارش عملکرد سه‌ماهه اول سال ۲۰۲۶ شرکت Meta Platforms منتشر شد، که بر اساس اون تعداد کاربران فعال روزانه این شرکت به حدود ۳.۵۶ میلیارد نفر رسیده و نسبت به سه‌ماهه قبل حدود ۲۰ میلیون نفر کاهش نشون میده؛ هرچند این شاخص در مقایسه با مدت مشابه سال گذشته همچنان رشد داشته.
متا اعلام کرده این افت فصلی عمدتاً به دلیل اختلالات اینترنت در ایران و همچنین محدودیت دسترسی به واتس‌اپ در روسیه بوده. البته در پی انتشار این گزارش، سهام متا با واکنش منفی بازار مواجه شده و در معاملات حدود ۷ تا ۱۰ درصد کاهش یافته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2258" target="_blank">📅 19:13 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2257">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بعد از ۲ ماه قطع سراسری اینترنت و شدت‌گرفتن تعطیلی‌ها و تعدیل نیروها، پایه حقوق وزارت کار بنابر مصوبه شورای عالی کار ۱۶ میلیون و ۶۲۵ هزار تومن تعیین شد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2257" target="_blank">📅 17:39 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انجمن صنفی روزنامه‌نگاران در
موضع‌گیری
خودش نسبت به اینترنت طبقاتی و حق دسترسی به اینترنت آزاد حرف‌های درستی مطرح کرده، اما خبرنگاران جزو اولین اقشاری بودن که به اینترنت سفید (یکی از
سطوح
بالای اینترنت طبقاتی) دسترسی پیدا کردن!
واسه همین این بیانیه بیشتر شبیه یک موضع‌گیری تشریفاتی به نظر میرسه، تا یک مطالبه جدی و فراگیر. اگر رسانه‌ها واقعاً به این حق عمومی باور دارن، اولین قدم میتونه شفافیت و انتشار فهرست کامل خبرنگارانشون همراه با وضعیت دریافت یا عدم دریافت سیمکارت سفید باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2256" target="_blank">📅 17:33 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2255">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r7hERY4jtes9zSuymxkRmbD4QIjNnDuFkscbTgK3fq9WcmlxcbBQYnGFJmtF-d_tEg2MY3-xDAhRTZxSxerfs12VX5sPEDhEEpWWD_xc3Fb3cI5X4wdiPSlnjjwhuVtslQIDEYC6UqUzmdnm4UZ-kB2sMHr_FDZ-wJO8M46kzNcikjOT7-VnrR3vKGfChnMbFPLYT2fnIE7S1RbsYWoUFS6kvg-vLmea6_jkYIL0vPt-RsLe29VcpRiKhf2Pndwd3QaYRhYa-Dkz-QTEuH_YHrQBtuloOvXl1DJegN0jzbPjN79G_gSErk3s4yhuC92Z0_GA8p_p6OkGG-HUCNjetA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن صنفی روزنامه‌نگاران استان تهران با صدور بیانیه‌ای تأکید کرد: دسترسی به اینترنت آزاد، باکیفیت و همگانی یک امر تشریفاتی و لوکس نیست، بلکه حق عمومی است و دولت‌ها موظف به تأمین آن برای همه شهروندان هستند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2255" target="_blank">📅 17:27 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2254">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rKmZhmnj0WiGLTgEvrWP4j4QKjEtqhYEIIU_9wiGfAi-Hp81LCS7DP0VQxKWmXJwxHmlEwxX6o00qdJcKu7JKTVoW0iQrOJZonM1ZZjuuzzW5IHb6DyhQuKu6pj-nyX4z61awloDBOMezP65i1U3ragwX4RoWmK_yk7e_cO-nxu0fZOrol3af1emK2kjOO2mw9qPr5AxBL-wjYX2Yld-HzicGVamzGcTgacJWpa27uSJIVD78qtO-7DK02Fz3LxDKVEwoIEhKfnzuvQKZJ_3f8cF0QcmdRnY6HLQD4wAs_5t1_5uZbmZLAMpycU0xS5raBJVyBnxDvPMD_-g3FXbEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایفون در بروزرسانی جدید اپ اندروید Conduit گزینه Personal Pairing رو اضافه کرده، که میشه یک لینک اختصاصی دریافت و با دوستان یا خانواده به اشتراک گذاشت.
این لینک رو باید در داخل اپ سایفون از طریق بخش Pairing URL وارد کرد، تا مستقیما به ایستگاه کاندوئیت کاربر موردنظر متصل بشه.
البته با توجه به قطع سراسری اینترنت، فعلا سایفون بصورت عادی برای کاربران ایرانی قابل استفاده نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2254" target="_blank">📅 17:15 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2253">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nmX9rEyjVdH4CMDG_hQRfjKgMlk2rmTpFsVqgii5tMLUSoItzAW4pI3CGM9tE5pAAESPmH0HGubRAQagKhmoZF2LVZQQaI7a4DPxrpuktFGPOZToQM8kVPAj8YOXuQ0imdiOwBX04jy_qAnoR7-uus6P8V8n189eSOf-FeiMJCpCyhFYp-cMIkPN-Y23O7xxPOEDjWNlc2sw4brn1paOUw6OTZRVPtIWSYaN5F4nWY9rTiu51GDsGO9uhIiPQwyw1HBcR0lPCB2PABt6tQh2UIYBR62HokZdSPfvK_dY82iDeFUVU_27RgRRVXEoY27QWQohFncMdLHOur4nhddYpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش تازه سازمان گزارشگران بدون مرز نشان می‌دهد ایران همچنان یکی از سرکوبگرترین کشورهای جهان برای روزنامه‌نگاران و رسانه‌هاست. جمهوری اسلامی در میان ۱۸۰ کشور، در رتبه ۱۷۷ قرار گرفته است.
©
dw_persian
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2253" target="_blank">📅 17:03 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2252">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">روز شصت و دوم از قطع سراسری اینترنت در ایران!
میلیاردها تومن پول داره توی زمین VPNها میچرخه که بخش زیادیش میره توی جیب جمهوری اسلامی و حامیانش. شیرینی همین پول‌ها باعث تداوم قطع اینترنت بین‌الملل و تمرکز روی اینترنت طبقاتی شده.
جمهوری اسلامی ده‌ها هزار نفر معترض رو در دی‌ماه قتل‌عام کرد. یادتون باشه بخشی از همین پول‌ها که بابت
#اینترنت_پرو
هزینه می‌کنین، قراره خرج گلوله و سرکوب مردم بشه!
©
Maroon
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2252" target="_blank">📅 08:35 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2251">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JdHyXvPik79wIvhjKCDGpSo4UdsIKJYFTJNS1GLDuj_cMEvV1r3aG7NNmmsxpJ3vbrlw7F_vnV-cQxcnrSfpbtkwoqa6R9OOyjyRKw03Jrie65VdfwJUzWD_0-gRKhkieF1aTsxuMFKwePfIJT5EQP3c5FUkAVUrw2jrLabtuRdaFIQih4i-1QZeOSZsDj7LQo9nK1cgfQlbGsjvu_8zuPFxJZ42cdkmAV5FRMr6teUqhcCRqektXYz2AZq1bpoZEcD4sVmUHbz1CvYwsaPrJ0roxZl717yiYgelxRhYmLkfYh8jMnoJy_B6oA1f2JMpL2qoNcYqPG9AqWrkLZCp7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلیمی، یکی از نمایندگان مجلس گفته: رئیس جمهور و وزیر ارتباطات مطرح کردند که ما مخالف اینترنت پرو هستیم؛ پس چه کسی این تصمیم را گرفته؟ رئیس جمهور بورکینافاسو و وزیر ارتباطات افغانستان این تصمیم را گرفته‌اند؟ رئیس شورای عالی امنیت ملی، رئیس‌جمهور است و باید در این زمینه که می‌گوید ما مخالف هستیم پاسخ دهد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2251" target="_blank">📅 18:05 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2250">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tjzc-zqZI46IHFIljG5U_QjfM83h-EJ9AscweDgehqFCRDd6UOxETSGYYdmFk6P4pFKUAWIUjqeF2fwQ3i87vxsqWESnfNOovTGAPAct45tiDt-pbaXGWk3myewTmVLM-HWVz-bKNw4iruST9Sy5ZTZqURDqWZ6DWrAEk2L9bhmB1bsUgjMvt8OjmLN2-D0W1iYu_2CX-9z_7HvYXlo3J3hdh9WHzOXsHtiwX538AzvK45BjNwqTJFH3Jc_wZJtE2j8l-SvjA8Z2iJTlJnL9VyF3fB_ugBJHzxu0jBY_qneomhDUnq-gj6ZY8YHwhmonoAgVJXVOe-Z04XI3QlyOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت ما را به عصر حجر می‌برد!
انجمن تجارت الکترونیک در بیانیه‌ای اعلام کرده که قطع گسترده و طولانی‌مدت اینترنت در ایران دیگر قابل توجیه با ادعای «امنیت» نیست. این انجمن با اشاره به بیش از ۱۰۰ روز قطعی در یک سال و بیش از ۶۰ روز قطع پیوسته اخیر، تأکید کرده که این سیاست‌ها نه‌تنها امنیت ایجاد نکرده، بلکه اقتصاد دیجیتال را تضعیف و جامعه را با آسیب‌های جدی روبه‌رو کرده است.
در این بیانیه آمده که حتی در دوره‌های قطع کامل اینترنت، حملات سایبری مهمی رخ داده و این موضوع ادعای ضرورت این محدودیت‌ها را زیر سؤال می‌برد. همچنین هشدار داده شده که گسترش «اینترنت طبقاتی» به معنای تبدیل یک حق پایه به امتیازی محدود برای گروهی خاص است و شکاف اجتماعی را عمیق‌تر می‌کند.
به گفته این انجمن، مسئله تنها دسترسی به اینترنت نیست، بلکه حق دسترسی به اطلاعات، ارتباط و حضور در جهان امروز است؛ حقوقی که با ادامه این سیاست‌ها نادیده گرفته می‌شود و هزینه آن را مستقیماً مردم می‌پردازند.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2250" target="_blank">📅 17:46 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2249">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YGyu-DJ3XlCl4bYzETU1x85xRXMSlW91_XiZeWpdQ3p2DZJa-4eojE55A-svbAATmx00hwcYI4Sx2j2gk6DcPqP-5A623PUj8CoVfaChZO0LZMwsnEELsuD-HSODFTyMroafypgABOXBWxCxXqn340WxvQ774ZyfnGXT_IqAvzFF483hIHJMhE0iHp2pxUf2RGPNu64WbGch8dWHwFj4kUPb2iSxTJvPr8cpxRpBEpEhx1cjAsB8Psfu9mJNGUyoVtvr-GJ7sFezqBbQtFrkSsbjwBaEvuZQ6_mRykxn8-rq6IvculD99cXfrxtO1g9MdggOgJXn3wmt28IGKPCbuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نسخه جدید CFScanner، دامنه‌ها آپدیت شدن و هسته ایکس‌ری به نسخه جدید ارتقا پیدا کرده. یه قابلیت هم اضافه شده که می‌تونی خودت دامنه‌ای که برای Fronting می‌خوای رو انتخاب کنی. همینطور پشتیبانی از Xray توی اسکریپت bash اضافه شده و نسخه Xray تو بخش پایتون بروز شده، تا همه‌چی هماهنگ‌تر و روون‌تر کار کنه.
👉
github.com/MortezaBashsiz/CFScanner/releases
💡
t.me/PersianGithubMirror/3624
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2249" target="_blank">📅 17:28 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2248">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oLIppOsTF9RG-62b4v8lmdF20pKq5W_sdUPhw_naWINbcTqlKByJWzKqQ5cLsJNgE2Wae9ou7CasEG2taRdlmylz_ajFxtnGj-v3SFVDdD3W8hCBtg8iPCk31TA2Hz4Qot_eKUMuFkbMUB_wvq0fMaRN9pWW0dUzBvbIso8b8N9ilo20vZeEAFvm0OYdHkevExzCKQbU5IccGZZLO2Ri8x9X5A5tt-U6kpUoQdBZW0BwWpxNe_TSZtrwmOFeoF6PhdVi29D9X5al0bthDo8CWmeGzeZ2713_NfJY1TanNe6bxvhsMKWBN3Ok6zVeVNF7ekzNqjYM6S8Qim_8U3Fv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن علمی روان‌پزشکان ایران اعلام کرد "اینترنت بخشی ضروری از زندگی امروز است و محدودیت یا دسترسی نابرابر به آن افزایش فشار روانی، احساس بی‌عدالتی و کاهش اعتماد عمومی را در پی خواهد داشت".
©
shima23972921
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2248" target="_blank">📅 17:08 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2247">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">روز شصت و یکم از قطع سراسری اینترنت در ایران.
لعنت بر جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2247" target="_blank">📅 08:48 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2246">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RsniGEWeAHZNseCE6l5v6Ulfe_CKW_FjpHFuo5dutd9PGobASupnE-m3lCbRo6auOTEn8hxkasJSa8xq6PLE05oHzmmEFf1JbTLyRIGA4IB7vH40ikHRT1imvLbGe9GB1nyh9yZQOyZEzG4iq14wA5ZS0aD3vKLxs8WpoyluqaQrNXmOdKveKrOpMVP-BQ_nzZdbNTefwRWqcBowuMT7SGmgBKQwEC4_pMJgxkNWIPKWg58FoQN617CjqFwFTiJgb-d1iQ63sspFDYkd6Tg2llqyj62eNbTh8mFRq0KjErh9XMP8aAUt2GP1YV9xEdPAjNAyTdF2_LOj2xq_8cDwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به واحدهای قضایی دادگستری نامه زدن که میتونین از
#اینترنت_پرو
برای انجام امور جاری و تخصصی استفاده کنین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2246" target="_blank">📅 08:41 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2245">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هیچ‌کس از هزاران فرد دارای معلولیت که از طریق اینستا آنلاین‌شاپ و درآمد داشتن حرف نمی‌زنه. قشری که نه حمایت دولتی دارن، نه جایی تو فضای شهری و نه سهمی از استخدام‌ها‌.
©
Mtherofcatsings
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2245" target="_blank">📅 18:35 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2244">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اینکه می‌گویند قطعی اینترنت «روزانه ۵۰ میلیون دلار» ضرر دارد، یک مغلطه است؛ این عدد فقط نوک کوه یخِ خسارت‌هاست. ضرر واقعی در نابودی  کسب‌وکارهاست، خصوصاً کسب‌وکارهای کوچک و استارتاپ‌هایی که شکل‌گیری‌شان سال‌ها زمان و هزینه برده. با هر قطعی، بخشی از این اکوسیستم از بین می‌رود.
از آن بدتر، این خسارت متوقف نمی‌شود؛ وقتی درآمد افراد قطع شود، اثرش به کل اقتصاد سرایت می‌کند و یک زنجیره از رکود ایجاد می‌شود. بنابراین مسئله «۵۰ میلیون دلار در روز» نیست؛ واقعیت این است که قطعی اینترنت، در مقیاس میلیاردها دلار به اقتصاد کشور ضربه می‌زند.
©
hiddify_com
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2244" target="_blank">📅 18:33 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2243">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رکورد ثبت رزومه در جاب‌ویژن شکست و بیشتر از ۳۱۸ هزار رزومه در یک روز در این پلتفرم ارسال شده. این مسئله نشانه‌ای جدی از تعدیل گسترده در بازار کار و تقاضای انفجاری کاریابی در پی اونه. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2243" target="_blank">📅 18:28 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2242">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nK3hwMnkKWkTl1xhxpAHeOCNWnOIuGocNuCtAPNkKlqkNJWa8-L5XztERfBdU7aAATvPqT_24qMPSQruMobQcYsChAUepivcl8O0g6O8mvjr_gyGPU34CcKqGG9eNu0Mf6r02qyIt4ZaPU4Rz9RjfrkNH_43LV2rMfg3gCQrgj2NwJjPShnx40B1_oRoF6DlHcxdLPGiVZxD77B85BZtJGBh3u_vVwp-VDJv6zaHstDQMp1YLGGV3Ty3pbrSRhwyVf6yXLnQACoVWjVC6kCwAKRKck9WDo1msRTVCaNBD12vgnN6R9HTJ7DR6jDFggc7UDFuwKuMbDd9HYN4jfieQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی وزیر قطع‌ارتباطات رو از برق بکشه!
۶۰ روزه اینترنت بصورت سراسری قطعه و بازار
#اینترنت_پرو
داغه، مشخص نیست هاشمی در مورد کدوم تلاش حرف میزنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2242" target="_blank">📅 18:22 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2241">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oF3fEF5cR_S27nDB8hz7TUsLvdCcyEbj2LZa1SjIczLBKnf9fcoA45nufFze6OMAhrnt71JPX6lg9Tuangf3dtfaPv2gnEHZL6z7WR3nrtQioUSZC9jfLFVjW7GbykP7TjRedOQG5LNrTEnVeSywwCY1Dy_alJlbKVm64m07v7BHcOcYBX3Q1vY49Q1ednK4srAL0_dMNPHCn7zXapGgVAPIQ6XnA5IQvynELArgGYRlkueywQzNC7F1uxihoJBUN5-60X4yN9WWFhnehbHqEJWShgc3qE7ojJ0xzhFF1XhjPLCB6WjCVgmYF4Iv8URea47N2o6RU4VPiowAR9QMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد روز ۶۰م از قطع سراسری اینترنت در ایران شدیم.
وقتشه اسم وزارت ارتباطات رو به وزارت پست، تلگراف و چاپار (به جز پیجر) تغییر بدن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/ircfspace/2241" target="_blank">📅 08:58 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2240">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به بهانه‌ی امنیت اینترنت را بستند و حالا گروه گروه پول زور می‌گیرند و باز می‌کنند.
این یک تلاش برای خرد کردن یک ملت به دسته های کوچک است که راحت تر خفه کنند، بیشتر تجسس کنند و مردم را آلوده‌ی بازی کنند تا دیگر حق‌شان را طلب نکنند، وگرنه امتیازات یکی پس از دیگری قطع می‌شوند.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2240" target="_blank">📅 18:12 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2239">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پیام‌نرسان "بله" خیلی عالیه، پیام که میفرستی باید بعدش اس‌ام‌اس هم بفرستی که بله رو چک کنه؛ چون اصلا چیزی تحت عنوان نوتیفیکیشن نداره‌.
©
aboIfazI
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2239" target="_blank">📅 18:08 · 07 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
