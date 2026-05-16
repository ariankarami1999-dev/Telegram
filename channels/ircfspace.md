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
<img src="https://cdn1.telesco.pe/file/bEXZLNMbYjNjXAaN9h-6z6JX63VO9E0RQp1OF4YLcyvKWz6AuMRsOGOVfnUJ9uKHM_NqAcTHZbiJGRjWnDzojfTaTfkJ3L0d_alTY1aB1OQvUWIP5aAgCFhMf1NVw-Qt7rjhtgtZ3hA3e0L9RyEy0H14K2fS02X4-WjoOSWIjDPBsOq2sssAM9Tv-Q0eC81dt5GHXuajvE8AuAFrJlNYa2Op0M4e7jy23aIvlHOa3LzYPSXJLm-mUJyV7HfpE0crmM5ViRDqJsGmtGdS41SD123F67DlR9QgVDkN8-vs9hfQCW5sWUupMDS9C99b_E39LWhEMGQf3-u2WFT_gKmvzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 02:07:18</div>
<hr>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZHwW46-n3kMX3HvgBeVVQAcfmNw-nmna9sY0U5sE6SLv8TT9RfYG8FnWQbbBtcjPXFcUG44ZokNqur0LPoo9_PDwT7Sbggit7xfL27pZH-FljmqjzIa6ipeAnB4FXAGH2Eh4vP7rDgiQWpwuJYcC57HW8tFONvfQQ4oyJNUUPySoogYK3V3cxneGLvnF1sHpbfYBpH9E4G5dLK8xbDYAAeV5IGHXYNT4dqKtsCESFRwV_elBb6-RpE1-p9smUdY6oUDm99SFflDoa2v0uWjkfNYPHPmcoM1lRE77SQo7M-MJc58Ag_0Wtuaa5TqRupJ_OlADLzqdgJoAD_VD-iUHzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۶ از فیلترشکن
#MahsaNG
برای گوشی‌های اندروید در دسترس قرار گرفت.
در این آپدیت هسته‌های MasterDNS، GooseRelay و FlowDriver اضافه شدن، قابلیت CDN-Fronting سایفون تعبیه شده که میتونه شانس اتصال رو در برخی محدودیت‌های شدید شبکه افزایش بده، امکان وارد کردن دستی HTTP Type لحاظ شده، یه سری از مشکلات رفع شدن و اسکنر DNS حالا IPهارو بصورت تصادفی بررسی می‌کنه تا نتایج بهتری ارائه بده.
👉
github.com/GFW-knocker/MahsaNG/releases/latest
💡
t.me/PersianGithubMirror/5051
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2345">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اپ
#شیروخورشید
بعنوان یک فورک از اپ رسمی سایفون بصورت متن‌باز ارائه شده و توسط گیت‌هاب اکشنز بیلد میشه.
آپدیت جدید این برنامه تونسته دسترسی هزاران نفر به اینترنت رو در محدودیت‌های شدید فعلی فراهم کنه و همونطور که انتظار می‌رفت، افرادی سعی کردن برنامه رو به حاشیه ببرن و برای کاربران نگرانی ایجاد کنن.
علاوه بر متن‌باز بودن پروژه و امکان بررسی کامل سورس و روند بیلد، متخصصین حوزه امنیت و افراد فنی آشنا با ساختار این نوع ابزارها امکان تحلیل دقیق رفتار، ترافیک و عملکرد برنامه رو دارن؛ نه اینکه صرفاً بر اساس برداشت‌های سطحی، حدس و گمان یا خروجی‌های بدون اعتبار AI، درباره چنین پروژه‌هایی قضاوت بشه.
در رابطه با تفاوت این روش با MITM هم توضیحاتی از طرف توسعه‌دهنده برنامه منتشر شده که پیشنهاد میشه مطالعه کنین.
روش کار کلاینت شیر و خورشید کلا متفاوت هست و اصلا MitM انجام نمیده، که نیازی به سرتیفیکیت داشته باشه! دلیل اون روش این بوده که بیرون هسته سایفون میخواستن ترافیک رو در v2ray تغییر بدن، پس باید از سرتیفیکیت خودشون استفاده میکردن (که در صورت بی احتیاطی نا امن هم میتونست باشه). در شیر و خورشید تغییر تنظیمات SNI و ... که روی ترافیک ایجاد میشه در خود هسته سایفون اضافه شده. در واقع اگه کد رو بررسی کنین میبینید این قابلیت Domain Fronting چیزی هست که خود سایفون در نظر گرفته بود، ولی تنظیمات و قابلیت تغییر درستی رو برای فیلترنت امروز ایران در نظر نگرفته بودن، که الان در شیروخورشید اضافه شده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q9Dr276ewI4moLjxK6ZVzM_WqPI8sFC_Xbnwu1zzITdH4wEdXQt9znqyOasyizhA3b6UgqK19EIjY0hbw8b4zZzP8OCiszryZfdzjx3OC6c8ApIltRjvYDpNVcvJ6NWf9qYwCHgi49M9SViZxVXOzzqiWArwdV2-J8Py3T3s5xHfOWoW-nbJWsLDcc5U-5mSNPoM1eW8SX-guCkebeQMQb_bK_dgii3FP2rSOR0zN_K7d3fx7RnvkOrnmtBwti341gXDGXLdle3KBU8FtFt3mjDeKxdaUGcIVoBFzuGkJwE0_S2qdMeA0WGfZtxtJfSIR_yRg4avDDoz27C43QiXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آسیب‌پذیری جدید به اسم YellowKey در سیستم‌عامل ویندوز پیدا شده که توی بعضی شرایط میشه BitLocker ویندوز ۱۱ رو با یه فلش USB دور زد؛ البته فقط وقتی مهاجم به خود دستگاه دسترسی فیزیکی داشته باشه. برای کمتر شدن ریسک بهتره ویندوز و BIOS آپدیت باشن، سیستم کامل Shutdown بشه نه Sleep، و برای BitLocker رمز یا PIN قبل از بوت فعال بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2337">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2336">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZQxPSqBiA1zjfRuzdUtqKfCjWpulIfbsfRjjmhrXEa7aOKLTRbNsGWcASRroIWP8MltC20p2lnAZxBtwCEPXbF4IlopWo-kFy0-IiSusLCAjxUav-ZqVfu2eUXq4L2ZPwxDKPVWGQxdL_hfuiA4bh6MSuR450n3Qnwk7R8510jQGucb0WoSK4xvvrE4m2jMZk32IA_U1Z2gR7i3llaVq1coZyMpVy9Yeb27moyaVue9EB1011sDe-v_Po5ai3UV8b68X9d56lnqfa8nrRt7bNnqrL3YCp16F_c_FJTGWFUF5Sz3NQGKejEqqey9xWCg9obW752eI_xMgBQVbr5Ra_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FzaTWsQK169x50cbrscaW7SK6Pu-Z-BESGXgfFUT7MkZj0yBJh9Rom-JpX4x_GX2zaFox6Lywaz0o1FbIaj4t1SK0iyvqOREL_ZZWBBqcqb2UVnXID7Pp7VDTaicge9r0WGZxxrZxOaggr0oCPM4Ti46t0qc2bxjOh7kFFl5SqT5oSk7O7xExm1_zBUSTuoVP6s6nLxXawEPv-PZg_WrlkC0A5inW3VHDNq6lsPwYDdl7lrsb5pzO3JNTAKEJIvtrZfUnRATrKVTgsDvRF9jh7BlJlj-oaXDuFXVNAsSj59c8VNeOQPQc7iajNZtKdqHYsnEKNBuYQCyYVNC_hJeMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s4PEMG68P8u3-9Xlvwm83DRx0vtkYvFybgRhsdGywEznE-L1zNj74-S_laIp8vWMQ7l3Ifey1zPoDq1FV7934taQpgOHEUskioZtd3GxEP_Cl7nPa3UQRRB5tv_7S7Hr6M1rG0vFiDe13f8XMU8SnAlCv4-qMNs-aKXU_m8lfxnmjw-uG34GTpvlTicca4PTws2O5VClZ6cl0w2Zyo-HjKAE6FOG571hJmfLkPr4zPUrhkS0WYBG9IfgRP2YDEhqTqcYDiwuuqQVE7SuxY2wVhbxlLu23g5XsnLIMHU9pdmfyPcnbu4Vz7GhuFbIevQlccdkymlPFJ-HO4-5LZjEQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fav8cK--YBwjkD7CxGsPYfgFHHodIc-9EFLSuV0kBRtb5cRjYVM8loJqknZMQ4eRFSJ241XzAM-VGcU37Nfgbc3RpuXox0fKgtcTAcB8qwsNN74laeOQ4Yo_mIO6P4fw8YrbJM_p5hiLq5jVmjkAVgiWduGAyGDIg7VZtTmz4OEgSUpzYPRqL_xeTyPnFPGBxQrUW0_8g8zIAtrgyW65GD4bsD7kQC1HfsuLegNIhpaxDg49NzM_UNak3_6RuzfOnapTMSG08a6DYL8dW5TRyLXAm3RyKdBtVg0P6yl4OHV15N_dt8C4JC8fHxWHM7_ke1eNtEVDRZoW_LbsGME61g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2328">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=qxNnW2y0Jaqt7Ms2oivbCgUN1EvGsyFYnY6d72LX91hsCYhOK2l-ReaXxZgu7RIbFA9pRD1LdLCiRIfzBaQcbyam8mTYIPShA5GF6YlMRc9OR00NhouEiSvQp_J1jvJMStmWRryotvJuPHdbsAocy27oIdmtPmdQtXA8Qb7gkvjr9He7_TLQzTm0xGKCFNBdFFsjm3rWtHZvCS-6QvphhAJGLqo9Y6wROoUUyyEChYR7Ud2tCYV7i-LbN5Ztr-ApSGo8nnjMxAH3_9Wamx2dGKbo1Mh4YvydGufl6i08WO98biRYgMW8n5c7_UO0YvdeoYh300s6dXjzTdU85b4N2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=qxNnW2y0Jaqt7Ms2oivbCgUN1EvGsyFYnY6d72LX91hsCYhOK2l-ReaXxZgu7RIbFA9pRD1LdLCiRIfzBaQcbyam8mTYIPShA5GF6YlMRc9OR00NhouEiSvQp_J1jvJMStmWRryotvJuPHdbsAocy27oIdmtPmdQtXA8Qb7gkvjr9He7_TLQzTm0xGKCFNBdFFsjm3rWtHZvCS-6QvphhAJGLqo9Y6wROoUUyyEChYR7Ud2tCYV7i-LbN5Ztr-ApSGo8nnjMxAH3_9Wamx2dGKbo1Mh4YvydGufl6i08WO98biRYgMW8n5c7_UO0YvdeoYh300s6dXjzTdU85b4N2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P5hlQL2cZU2bGdcKitDiENgpIRk_yItxCgIRHQFedDCZK1fj3RNSYSyz-5M1X8nblJDWrOXsp6uIZtiSwymT4aYDSqo2PkiiawT6uOIb4lgR_QjjaM_pFYX9cF08pDB_d7dPNGN10N69f43WgLNMt_pb0ucWNFY8UMUe4ubDKqpyD9xol7HZyDUnrVmtKxTiB22JfpEXbSwEvzvdtmn-HRgVfMLjEFM7IR1T0Dw6Z6RSHjheFMUPb7WPf2Zpx_Lqbd0H0BnfT1uxSeSQcnxOzVxmigg_7NIBvvboD1b5rhow6dKZn_0cEJ4R8kXuiYbPHoDLYXJHJfWiLR6AuAScsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u1ZeY3MmeJMgrI4CxodErVMpCx43bEmcctc5Ys5tRiq_0cMVF6S5e8s-2LEGn40WUy4yTM_Qf9aTYqdPwtv7QvyBh-CjrB2ygiR0uHj6I5jIlucUltIKJw0dhHdd8AwscNx4cPyBVKIb_PaDeXXkoMn7zG7oxgpu0vZMKQdvnnvS8z82nh7wzZ48CLoWwDIjz31HrgdlYO08zZl93aX4-H-cPBw7ap09093VnqtcPC92zQnwZweBxCldP4sJIO4utceu_xlGxB_vW9uKhCrm5bC0vZD8Ntv3hAVr_LaLuqBfiKQiV24kFNhUnU83yU4ZyhadOlETuDeIE3_rwLpqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2321">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WX7RiLbtgXTA3ZIFIoKO6Hr1e6zShDPrcaxxxEYhLY1wIASE-SJU9qb2NmUxXEZDJO_JYcZZXUtgvdjSb1jEVz_rgIxCzKbAyle_E0ao_ntmrrQRxKc6_SgPVkJ3zHHFW5w10JZZUAtHH0kVDeCyV8YyB1p7pcVXt4rsFh7lOsxhivNYUq7AjAhmaklATADqYNcKBa1WLfaB7yyx-3BHL4rM9O3u7x2CuAhqrBecjyDJyAUBmDKncqt9akWx4KL9g3-b4X-tXamEXUYS8JX4cnEUvplWzkFtOTvqys2iAEG2d-d5_mZF76Gpj0Od6aaJEzPUFviyL-DlValmk6z0tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tTImB6PhcUXGTT1I7ybYfYKOP4yi0AW0sA8MT2z2acQza-LDcVn-vtXj75nq3JupNgvBhvociN-lUWH0Jx8dgaiNusrnhy_Q_gHiDn8M4gAQUBr5rwAqDznBWz4FIuRJDon8M2yeou20BPyCurZezMv_KRuEIvQFg0yh27F0vwwsC4epoNXZU5kE27vXkyl23q0iOO6h6KiBsys-NTjsgsotuUsJi48kxvzU56QfM2WK-e3i7fL6EXqH3B4Vsdlu3kDrXhLAFQHUT5CEMHBYmwRgZBLT4IyXoQ3m2q2FXiVC05MLqNBInXrjIwsFXxQRzgCx4iKOQrGVfwNilWUAww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RJX55s0qgER2XNzfGsOBpBr_lDKRmj3pIumvxZTD1DUsaJGS7FR_VqbjD_PZCCJx0w46EiNDkTOzdegbnGmPGlYJwUnqcwLHkCaTpShCq9zR8rVHHE9e8YrFtIB2RZPcRGyafLdKM18S-Xl2OUFG9C3epMtgVh81Uey4_CAnryMhcudkzmImhRMzSn3W_9Z-rjw0hc7uNNAB8DCjGn0ZhiNjlJZO4A8_aJMYmO8QOAgORt1OnftuVOPfA4pfkJZUVSnPC97CLf7HtCOTDmOGr1mRHWs80tpancXedI-ygLR2x9P1gd4Y1Qf53PYcfJdLV8G8m0h3vAJbsN25uEk_4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uuf0RZF64dvVVx34SvfAKsrGTE06-Fkiak_rCXMKhsfzibItr-ywf-DZRn8Ti_LEzBSwEk1IScBGtu12k3zh1WzuJ2VWGC8cOrPJ3G29kfchsQVaBQEMQ_h-dPY4EyTX0oqZBKE9kn1XyZ9AfIh4CewnXkSNitVeFAjtY7Wh_cRe9wuHxHv3x556dmZpxyhIqxMvFVHiireZaMvrUs4TWdM3D9D6TBb2BgK4ikjmyqYF8J0f48tgoRxhltoQRaxMuJtsZ4XEtPh1o0ch8cIKQhrDCyQ136QbsxBtDiU1a9vf3Y7rJW-yIICfMb24u3-diJKDmGxldouTsFSMn8cTYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b-aJoa58FqpAMPClBJ69hlGo_V4lh90JWgrdQdywncjSvITEf7CoyMLxOwTKJvygq6MAjaX_yflnaC9HiKy-XryC7G_JAvrFnT1XlGGbk9uPFoWokOc_Dy3qk67NkvGQYkaZCv22bNYHvM1W1HnOb4iE61WE2Zb9IAzdFpBSZVKu9JmimKjVhoO6U4jLBWmVrhfxsoVPxQqiZzHaz9X98OZosKEfDS-QPygaAbNXnPQ9042nTZGK94AsqRTonNoPMtLWJVAMan1p4BNp57gHxOzULsYV3yKRDGivs-Jxzx95WHcp-LQbm1cDV7a6r3tVN1Ew6RhDrTtNB9o-LKFOVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fldsrJTTTS7HaTeCAdldCnmVWxnR4RrfRhhIshBOWi39OwRFArr6_7uG8XKF78GL2u-Mcgd9K3qUc9nQJZ6eQ-y6AnGWGbUhKUAF5A-8J_YWS9sA7Gmo414rjX85BapMXtnexfc-J3qTvkTLoZybC8C7KZSOqcTd4PECoPJlXbehgB4kd5tQdyXe2fxv5Gg7-i-d2wjyTninxpemF00y4QLa_EUzd8rX3_0efzauwQGGPoLnRycA3zJUXf_IMHsGnYQaaZWzEC217mcX9oJgdTooqCje69gkZ9oQ4dew5UKrSBWzrw2-LC96I1gGSzgk8rg1S6ll-U1urxHRMfy1Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lnhodwfkk9oXgQ0iE66yZGqu8hPJ5_dop-L3quhl0i-QXX56uilgODAgHIqJBVEajgOOkn-pqL2NOGzFVIEmQH2jo0TUhDHMv2NlHJxZmMsnem-JGYh6ghF10utIT4jpVFKPt2fygU259UJItsrNngD4gLG2eeKgNlCelehgWJbL7bNLLMMEzUIRbWqUSIMyBv6r_8YOWuN3M-N0aZ0HWyRIXlTxAo4kty-UIlH-FeK4rnPZX7FWtp6CL0fm4kOxjQlnDdrGS0ZycWKLqBQPVhIqW75kJJQ5449Su_YzR6DiVOUTG_pxnMO8inPozZ3KGQJVcIc26F3HlZDZAD2iBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2302">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rGg53UY_3PA9ZGmgZrogztHiyT_8P3LyzLYx491XMUqopihI1kvXNE2fybZgSraBMkVSCDynGI7-deoBe7phhqB_Inlz2XyQt8yNFt4emkpg-XRJ5JW-AlZZG86pwoMLCUlabLTgR8basa6k-g4oH6O8aqEJMRLMgZSdEfVClfRixfPIMHa6yDiq-P4n1iBgs-L5VuzZwaIR6MJOe0r6H7MWF-dqfs98uwBOi3DEmz5WZr9z6BJ12RH0hvJ7fNELr7ZqpTRvuzdZknUGvPX6Z5O72lp4gtYa7TFWyFACTLZ6P2Oki9nvhRv4Ex6EDGqY1PGFpa4SLt7m_w8NW_iEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gZobDVxkVkmNcTHNMVglpBBBaqkWwXadS0js5INxnZQKU8wmnmO2Lo3MR3pMLBIr6DkTc4MqxzwxCM-tTPaxzjjBqUiCDl3e_e1q6AKUh5jdUJJtLeBCl3LPFUe1_dQK7--xpgGk36txxlTan7g43sVfIfTy0FKDSSg885q2PpzuoyL6fKrjAw4hfRarXLndWBK1BIgJqRLeAQ_SRGhxI3RGW530eYsr071a10WsVTlkWdOmPos0X8H-iKBtA6DFN5quKUQAEa7AiPPf95b9s31cBMCkimiQHI-BoWrL8CVWOzAHqbV7aOI4sosZzsb4c7yQTYv6wN7Y56eez6Faqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NwIb6UMGJvTgpjSxZ-ruqKKVz724XKDQDmqEc-aLrQGSEj6Qs77aqFHzJhLxkYPEvcxzrIqfGxBQIB69mvyRw95lZsIl_c1aKr9fbEd3rSDgJlyxCvtqoWOPIOM63Nuw2odcccE0b0EE6gXI9Hj1zCS0RO84F8OarkIRwt42fzgLq8n_OTtpwdA86DL3G_BfyQwNcGycRjDI3xCghSCiZU6JtslS11-KaDzuJzaz8VasEM-gsCTt4lPY4hWVTi1AWFtSIa1XAMBpPmbA-qw4vOeMsTvtqlqv0gqEZfPDh8UPqaezwL6ojghedDYZhxAgjBCXSr107zN5u4XcRcwsqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">افغانستان تست خدمات اینترنت 5G رو در کابل استارت زده، عراق تلگرام رو رفع فیلتر کرده؛ اما جمهوری اسلامی تا دقیقه ۹۰ درحال آزار و اذیت میلیون‌ها ایرانیه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aodRrBwPVDQ3KW3HAec1co_1Ef1NHUaoCjiHekE8SXM_ay8RmdNy9I1JpxF7IQkGbrS1qxmJizQkC4WDMh7L-rUbIEOhXIgSHwNKkYmJ2BltDm2Xu5WPNKpkt2sd3MtC12-rCp_MtJzjVZTcno_vyVB8aauOa96h432m0Ca-I5wP_idulE3MYJ93b8zZXXg3zrG4awsHL0SftvsuWwS0-s4iKTjcmg2_2v-yLCiufeq8BO88mM5HFdJu_JYuFiFKf5Ck-6umD3cfFh7zphK7HOW4cpvTMpTOve4tHGtAWiAzV9MAAoQO-m712LZMwgeTf2hdpDT3fbLBVVuX5IyZEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جمهوری اسلامی ۷۱ روز هست که اینترنت رو به روی مردم خودش بسته!
روح‌الله مومن‌نسب (تئوریسین بارداری با ۲ گیگ اینترنت) گفته شرایط اینترنت به هیچ وجه نباید به روال گذشته برگرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WmJE6shhDyoBwpXOj69Rz34RhhvrzCLTbhnnYVBlrEP1jUIBUR2iGqlj5sue0IR52jd4Zv9hWo-qTVvqAMLkArmPIAH7pmjj45o-d6E1asuDg0-uLH9skrrke3dlMMueNNBbGPhtkCHltTrtBWhVkygl2HmpSeyxejKZZSitdOjwYSF5MJqAb5Y3HgbQlgbz67XIVKMex1IYghrVaf0006qxX9MnRxWf-KnIxyXMozPub6O-S1To7-n3RBLBAZkkfeOgdMMSVjezGVt2_oqpAa1RGWngkBYJaoEra_DQAUnap5PwG6w3XFuSqMzu59R38iCWe_qBeljen2KZBQJ-WQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fKXwRsznKWo4V5ILgki1bHPxPTCnppprZlV4OZim_EAtGwBfOJ5Fz8bgGk2r6tHrrKDP7uO-SR2pmqV4SjczqG5XA9ddgao2Venvlst98kDZ3EYVM2WBz1uKY-fDFq5z6USU8pHinK7qm9jDrr-ugdTLfNdUuJk0Inl8UJp2Jz-eZrYsS1XX7qQXceneYRTHSryNTE-qC5WvA-zbQy1bsRo2LsY0lSafSBKfK1aXaK4KJ4YBTj3bJ8Pn65iswLQRIvUtIuodkMJLNSR0f7EZskzQadnHepVHhIpy3uUKZqH4smWBvMP-BkLtJ-5zJDvYx7XJQOqc9EtgCSjTgW04cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uBKmvohvcLglYuxHBuEFyo1kRfhnRvpLR6dHDjifB2NcYaVQAFACJVyKWiixk5qmUUjaOUIA1PXdYA8Y4GKKsDv9kO7CHR8-TOBUiP1RmgPe3QvAKU7FXYDalzDI0W2qGrpJqb33GZ9qyn0JA2PUbbeJoF6aA8-QQJ_TmS2qG3YxtAiBaGHffPF13rBHz47es6hEOBK91285MGgDIioo0IKkzWg1Klh0JOu3Tv57Qa4CMCyOnd73jAfY_fIp8IIATk9rsT8QKvaQFQ5N3MX96lmEO-Ge1NenGfUSIlwj5f83_M9qAruzK7r6ZAcKRqezThhwXxiT349QkiWaOTPQtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lDtf2LBZZGOP8zvDye9dGlzv2KeRR-LKsBv9o5te3_kHCFXXY6c76KaaVwi47F4Atbv4ejxJJqW8P2dbK3qvDlUFFUXJvwDV4cTbv68sfFmG5LEyFUMOZX0j0n2fFZHYbwtPr-zNOx6dUrQ4wG3l1dGBsNEOcrwgbwvojB4lCLfZnUBDLByo69biqRfFfOiRlRuRfEbi9w7hE0CA_0YNZut6ehW7Jr3vHl_ohsRFt98pGOi-B6X16bGiBmQn-WxPs5uZGhDhuNbqttAY5MGohAVDIn3YtN5uJVFkGD4PwKjU1G42d2piiSwjsBWvrwJD7H9c_qXl5nYVnwFgwTne-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2292">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2291">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2291" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2289">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بر اساس گزارش جاب‌ویژن با عنوان "تاثیر جنگ بر بازار کار"، محدودیت در دسترسی به ابزارهای اینترنتی موجب اختلال یا کاهش فعالیت در بخش قابل توجهی از گروه‌های شغلی وابسته به اینترنت شده و بیشترین کاهش فرصت‌های شغلی در گروه شغلی دیجیتال مارکتینگ و سئو (۸۳ درصد)، طراحی گرافیک (۸۲ درصد) و ترجمه و تولید محتوا (۷۹ درصد) ثبت شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2289" target="_blank">📅 12:07 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2288">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m7BRbOHz1h9H6pobL-9Qu2hqHD-Q2msPYMaMIQ2yl5sqoGldULu6NjjaMLWBGAUPP2QPGsbtEKZR8vlYQF5ZR1s1Gvla0c6IA50JSd17n05crc58-IeKguYwsjA5vGZPXw7WVy5tp9xkHSoSIhCM_sP0H7s0TTwIVzDRuZDuUjxOlyuI4V9mCJ9P3jUEjAAGci3wPdXNP9OgKGOnfjFw6x2deoioS53NhbNakJ089V1WDi_nVEdBsRyOjHkWEcvjv_6kshDrT8Ro4YTuYs8eWro1Evx749rr0Z38kspoGnlNAT6B668NhLvd2rvn8Zf4lv_3uBDMhOc_tcp_AxtqrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2288" target="_blank">📅 12:02 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2287">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وحید فرید، کارشناس اینترنت گفت: ما تجربه قطعی اینترنت را در دولت‌هایی داشتیم که به ظاهر حامی اینترنت بودند. خود پروژه شبکه ملی اطلاعات یک قدم به سمت ناامنی دیجیتال است. کسب‌وکاری که اینترنت می‌گیرد از نظر مردم رانتی است و روی حقوق مردم پا گذاشته. حاکمیت با قطع اینترنت به جامعه سیگنال ناامنی می‌دهد. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2287" target="_blank">📅 11:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2286">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uJAK4BbXMfi4OYRU8FeSRAFB_Td7dlpCkGTK6J_Q1Fdo1wTT84AOM1f5kmkLy2dL44yV5gsPs1dZUPmLHjkxZe-1eB1WpvE47lc-VYy-2GfYYCm38tv8WTX9q2_9rTRMviFkLJcEfk-rITS1px0nIbxij6IgR5rhjYJJo4FyTfSYofQ8uiItfqvQyxa8p_7j33AWjld2dYWB-dBTO45CHMwVH9vQ1LTg7sWswF57arrdg2bQasedvfl02VZzD4TIhX0pNRE_jq4OR6q7ake700stdoiPyRQtgGPCF9luzAnU4DomX17IbKSHI3YvUUWEMjn7KRWl4haVtkmsMHsMKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2285" target="_blank">📅 11:26 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2284">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=l647V0HsYzEXxk3tuGBEuuo09Lz9rhFUQROOhCRCci-QN6rA4s3ERci66QApoCWOQ21N4-35Nd3paA4STJ77vFHsf2ajq4i1qhEVLkt9pg0YEq1Ul6xwWAaeRkKzlDdH7pPWp_6B6Q45q_EtbpwKwO1hQYxh96ZCrncM1NwxRyIE0Sc7K9wJLuSDF4vrmhS0Im5wlZIz0l_WWpOin8g4o5z6NKrF0u874ymTHTxW_6mDBld3rOAjUWf4JKMTPFgINPLzd36qL1nUpzj5mk5ONAWaTgYEWeA5gWw7Dlt0pl8USHWHrPpRXdiSGpMPfKLAEKhbK8_btC2367P0Fne7Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=l647V0HsYzEXxk3tuGBEuuo09Lz9rhFUQROOhCRCci-QN6rA4s3ERci66QApoCWOQ21N4-35Nd3paA4STJ77vFHsf2ajq4i1qhEVLkt9pg0YEq1Ul6xwWAaeRkKzlDdH7pPWp_6B6Q45q_EtbpwKwO1hQYxh96ZCrncM1NwxRyIE0Sc7K9wJLuSDF4vrmhS0Im5wlZIz0l_WWpOin8g4o5z6NKrF0u874ymTHTxW_6mDBld3rOAjUWf4JKMTPFgINPLzd36qL1nUpzj5mk5ONAWaTgYEWeA5gWw7Dlt0pl8USHWHrPpRXdiSGpMPfKLAEKhbK8_btC2367P0Fne7Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2284" target="_blank">📅 11:01 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2283">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وارد روز شصت‌ونهم شدیم. میلیون‌ها نفر رو با قطع سراسری اینترنت گروگان گرفتن و بازداشت‌ها و اعدام‌ها در سایه خاموشی دیجیتال ادامه داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2283" target="_blank">📅 08:16 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2282">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pAmg8-Aidf1gTYy0KMUrcO5PUSVRmhAxpSkvK8-zkgQRJvAZ01I41fmEGCcTyYeqxlOyy1llKc0piZMizNtNhG5R5LIwlimZ8IPb5BoLi2PstCqcDUvDPp6O9lpPiB16BMrCowvs_fXSql7_kAU1UDplr3O7WgEzW8PX5uaSLuzz_Epu8qqlsXK_0CwcvsAaJZJxKWSSD-LdNBPDM7jtuqJvQGYjJmFO9Ey5_LIz98nd1VQG2u34F-cLF-8aYDLR1nVTD-6rgtGTp1gikyTTlqy_NKiEJG2DY-e4LjqXGSVjlZV78Xrc7D3CPZJUb3rtomM3bS6GL0_MCgz1GnxuCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2282" target="_blank">📅 18:20 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2281">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DDp0VBKASW02cU1arGdnIwgQdHX3V2ArqgM53TDUFq48dba78Smthekaxr_czMJ5q1-wIaHb1wbDNzgUDwIlCaUeLocujJZuN8InkU0UnI0_Mokh0kpkVg0B26QwLULWtdTHOdHb592N1jyowl5e_ZI4wcYDLApk1H7FFaB5YoDig8ps3XM5lSJHPMC9ncYcUnTzwYUUIcHqYhNik6YXUGtgzDbgjcxMEIn1gq4zuDXEWhd91tSNTPzVKHA2In2wGX7KMC8OVROtIojAHXRHs1NDexNNgGhVbGJ6jPD2awq_sjzPVYia8Szaao1aM6pamVI1iAVtsDnNH-CZybXO6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2281" target="_blank">📅 18:11 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2280">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2280" target="_blank">📅 09:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2279">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">۶۸ روزه اینترنت بصورت سراسری قطع شده و در همین تاریکی دیجیتال، بازداشت‌ها و اعدام‌ها ادامه دارن.
قطع اینترنت فقط خاموش کردن ارتباط نیست؛ پنهان کردن حقیقته، اما خون با هیچی پاک نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2279" target="_blank">📅 08:21 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2278">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nkAJm5l9K46n5R88e1mFO3EJ1KMvdBH-WY1hJPTVmMDWdYmlr1Z7j94mTeszHq6bV-p9p6kQK-Nq489T9Zg_tG2tkKT490W1H2IxuLKVlI8GHGes7SQGJpro9-iI-8mzlOUNy9GnZcbAV3yzeHNaTEneRO5Wk8GgN6OqZtxb7foMIGlYZXvkypzODS7r6OgI7l09I976bMmYTj8YS8I1ELth1TN2V38ARePau13QaRuPfx5Ao7fQ-8Pa34TmDzpfv_mgU5usYtcMiL8Yd8hd0DsxzyU4biWp7RoIiBJcPID7YIP2MFK6WF4sKKchloVHqxmAFTKDwpw5xk3treDysw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2278" target="_blank">📅 20:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2277">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JYaF5RUhRreLfNNJ2vki4iOvmY6IMiRwQLjGTj9ls8wUN4DlwGlyUrivnsrmxUAkRJyrnkUWsvdI_H7k8JpDAuaXlIL3My1J2ipUxVGXGRsUjRTBSQz59i4-rWDYoJP4cvJdXeWuegk6Agxrp0EaUmCkMihlABIS_bibC4UfrWl7XM3gyWnLDVOod2T_V2u6dmbvnIDFXg3eC7xN8ZMh1zRNCLpinowQxgeGkOLbI400yXPg5NIFP-rmda0yLp2NSjELf_slEHVuL0_RosgpzSUH396FY5cu6T-x47fiKK-VEpiGjEzfK7T9RlNRg4YrlnmL-6EZStx5KepwStCd8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2277" target="_blank">📅 17:02 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2276">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y9fk44-fTbrUCQ38J9VkACylWGr91EmRHS7MfhG9I8DKBWXe7cVT_N5XiZfrPXrafhIPQA4Zg0EA6VS_Q6F2B3GZktzjklwHjK1KvNQnFO0cSpeIK71GdHQ8UbutQ90mvErTbxyXnU-bN939F29e5MSZvkR2JOxiHF3IQH_Iaym0CXYyjwHjTVcXZZTggE0vFd5eFno4KUrSgOBFZxU00ln5mosxmUxIaO35rsa9yvo_NqyRuvBhSv7aUyTiNLx09Yl1KHbTSB5P0wy6hIcE7BHNy6QdUQ9bJX9syFoBJUdcKL3WlnldHSSIQvgxUJXsVXgxdKvJ-ljAeB8_42NUmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2276" target="_blank">📅 16:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2275">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">توی خبرها دیدم که دستیار ویژه وزیر کشور گفته "محدودیت‌های اینترنت احتمالا تا ۴۵ روز دیگه رفع میشن"؛ بنابراین بنظر میرسه باید خودمون رو برای کابوس ۱۱۰ روز قطع اینترنت آماده کنیم!
😐
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2275" target="_blank">📅 16:42 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2274">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LxrAs3daBaobuWD_2GvzCF7q69Zv0-7tLfYQ7wdmISImRRrMLdctjThKqUJLP8FfTAk4wYXk5OStep-06W4KLuF02P5H8Q2FA1xRmniDhXkJ435XUHpg8XD2VXk0PgvLKnD4AmV-QP_ZqDqYUqOzUfQ4r7s05l4DCDdKv82mijeSuFQn4bG2vFjwDi-hCEDgns_fsaJVZVgxuDzpx2xvJ8DrdB_kcwA37vU42-B_yXds8X9C6w95Vw4eGgCF9wnOLMocOI-1Hqszfip3pwtpG2XM7rOnRWVqIY6Ti884BORzzUtmPA4e1FCR6KSUJL5Ozv1J_VvaL4ndxq1Xm9kh_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز خبری در رابطه با قطع اینترنت سفید خبرنگاران توسط ایرانسل منتشر شد، که روابط عمومی این اپراتور گفته نقشی در این ماجرا نداشته و "هرگونه قطع احتمالی دسترسی متفاوت برخی کاربران به اینترنت، لازم است از نهادهای تصمیم‌گیر پیگیری شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2274" target="_blank">📅 16:38 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2273">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZICs364OGwb84dj1d-gFxc4eGcGOzIT7jpotRak0C_23UXRfTZbW1_b7FOpxRSLvCB0-0iIHp3ooC6vN8w5pFxdcqhax3O5Nq_NfyQZOoycj2famrnCYNxsUpqcxIB2thOlBTfvoXRkP2JSJ_9gqXbRctyAbljtzt8xr0W5t7pAS7ramFXdAes-F6XOKnTPewSImkVJZOA1r7oPcLTSzdc4mC9ZP7Y2nIbWFSIpsATW41-CdLzOqS7T31lWxBrb9_cT26xOj1HVIx-jMeJer2gEA59JDZmut54jdstjjTUosAJjck47EPwdHmc0jdV6AHBXPaeyQmE_UoeEaDzzzhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع اینترنت در ایران اکنون وارد روز ۶۷م شده است. اقدام به سانسور دیجیتال، پرده‌ای از سکوت بر افزایش گزارش‌ها از اعدام‌ها می‌افکند و قربانیان را از دیده‌شدن، پاسخ‌گویی و حق ابتدایی شنیده‌شدن محروم می‌کند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2273" target="_blank">📅 12:26 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2272">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">توسعه‌دهنده اپ SlipNet متاسفانه از توقف توسعه این اپ کاربردی خبر داده و در بخشی از توضیحاتش در مورد علت این تصمیم، نوشته که "توسعه ابزار آزاد، رایگان است اما بی‌هزینه نیست. متأسفانه در جامعه نرم‌افزاری ما، فرهنگ Donation هنوز جایگاه خود را پیدا نکرده است. از سوی دیگر، جنگیدن همزمان در دو جبهه (فیلترینگ از یک سو و خشم و کامنت‌های تند برخی کاربران در روزهای اختلال شبکه از سوی دیگر) توان ادامه مسیر را از من سلب کرد".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2272" target="_blank">📅 12:22 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2271">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2271" target="_blank">📅 22:24 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2269">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iMWnpylJNTiEBkemi6ZXSnvnQCiNyD9H6jWSnCknFylZsKBQZyhjfO74ojdQBUuLRUVEZNVdqRMZz2UhJ4ua5QbyZRRXV3WBVB7bwI6ZMrH_DT2xiBnhzDG4uGR4Oopmzgmf9ea_-2Xn_NflPJcjGrA_diq4oDYZ_7QLBmZniU59ldAu6ineidT6OAxgFP7x9UxMjRpzctmd8r15NzKtfFL0QfF5_yPKmluB2hOYD9sE1ndYZzuLxq4Qyh9NCelYvu95ULyuT1uJlHW7uwvvF8PuPTOS7QQlMomeZPHbUx9D5lcaBijGXMs30NGSVDBlM11-hU_yFuYK5x2yOn7h7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبری که امروز در مورد "ثبت رکورد ژاپن در رابطه با سرعت اینترنت" در صفحات مختلف منتشر شده، مربوط به حدود ۹ ماه قبل هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2269" target="_blank">📅 22:15 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2268">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IdH3-JHa78kirKL5z9QIEyCiTX_4YL9Y303BYB73JgO3JAIaT9UftP1Bt1YzuphTBV9DzlMKMgK_VND-5Cu7fuJ5Fr6EPgMP-kV_J2P6c2HP3Rd8Joe0dDb4MtNCNcE-qU2MmuU1ynEMtTnCtAQ2X0BP2U8Z8oKrWEXTQsUAHSUUxXwqIN7IWAk1DecWbqy6t-4IN7dh2Mmn8PJ428SfLrlcM9TgDuNnj_UHKEVih-VGPdPj-MflPDdkho5Rt2UBx5U4HM-OWuLupki8lq6stsM1PtIjMFcRxwDTxMbXvSGW2ykqVuQ-vckMoSiZXxe5QE9zamIf2fOYMZelZAnJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیجی‌کالا خیلی اوقات در رابطه با خسارت‌هایی که بصورت مستقیم و غیرمستقیم به مشتریان و تامین‌کنندگان وارد میکنه پاسخگو نیست، اما در شرایط جنگی از طرف سرویس دیجی‌پی بخاطر ۲۰ روز تاخیر در پرداخت قسط اظهارنامه قضائی میفرسته؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2268" target="_blank">📅 21:57 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2267">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LWBOhNrK0mfBKloWDLZ_CxtK1MWdnBQdeK5ZuhO2mxDBzoy8GRC_JtlxtnKr1_vf1TwxUv9_sIt8U2hiKC2NuIXhVz04BicvCbsWgCf1VXAbOweqCUrXbFl9DPj_d7qh1AWaxDL1vsXtPuturZuPJWwZfnvnWZpTScPI2hCK5jD-t5ZVWScwRfqbnCZ3u1I5ATwIZKL4Abub4V4FZb_ocKItPa1h9K8nZ5jvf2AfPlj1Ktf55FXKhoFm7HSdwpq8oYtzMwKSowMXhY75UVwez9vPRb9sydHC95J7DcBrh5FB1p3bL4U85WW0KExlasbmOtwMGje9T2PdVr0y9Tl3ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2267" target="_blank">📅 19:53 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2266">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">در شصت و ششمین روز از قطع سراسری اینترنت هستیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2266" target="_blank">📅 08:59 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2265">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i3yIYBY1bmgLblyHE5VJxCJRSD7zYZsmijd9qgIzSJuQ3v1TJjflY7sN2doul6qCrSq1HL51oKR6O_v84B916dqlQJo-6yVaJqo8FRsgcuSgBlRxQ0rTGqqfp2w2zKywIc1iEXLpVR_z_W-Cy-iOjWGX8v06XmTNbvvCK5hk6PBp0iIuK1NmXmW8aqN4UZz7l4fDuQGAu0odHwCrt_AP_vifBG-pdXRvpNFhmQ29lk6qZBDfIQRXZgLiFQZwQlFRlnbwec_qDxa4HeSbyqkOsMI54UuCEXpjKh7v7newsO6obZijt_LRRqCBivHbCRijaY0HDnlWwUu05l8w6VqO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌بی‌سی در گزارشی گفته که شبکه‌ای مخفی در حال قاچاق تجهیزات اینترنت ماهواره‌ای استارلینک به داخل ایرانه، تا کاربران بتونن محدودیت‌های شدید اینترنت رو دور بزنن.
در این گزارش اومده که افرادی در خارج از کشور این دستگاه‌ها رو تهیه کرده و بصورت پنهانی وارد ایران می‌کنن، تا دسترسی به اینترنت آزاد فراهم بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2265" target="_blank">📅 08:53 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2264">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انجمن فین‌تک در بیانیه خود استدلال کرد که رویکرد ایجاد اینترنت طبقاتی، گره‌ای از مشکلات زیرساختی باز نمی‌کند و در عوض، اعتماد عمومی و پیکره اقتصاد دیجیتال را با آسیبهای جبران‌ناپذیری مواجه خواهد ساخت.
این انجمن از نهادهای تصمیم‌گیر، به ویژه وزارت ارتباطات و شورای عالی فضای مجازی، خواسته که به جای تعریف طرح‌های تبعیض‌آمیز، بر بازگرداندن کیفیت به کل شبکه اینترنت کشور و صیانت از حقوق کاربران تمرکز کنند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2264" target="_blank">📅 08:51 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2263">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GCEI7B9ibJOJOHjZDdU-AJt0yMrgnhKK_Xj7ZBguHbRmoro237CS_boCg6uHBKGth2Y0PmDFo65qvDV_FitlJ-aeTILi0JTs5tzZ2ILtZO2kV9bdW-KeNm2YKf3EyOgrfd2br2F9Q1Ts1m3M7aC2TBjwsDYqxadFNdXjYGceEMzt-rWSEj_SHA12Ii6VGe3cT3XbU_Ff0kIKJtp4xn-n1ZDNcUSbp7tsislIMV88X4OsxKk2Jr9BAb0LyECXHIGUywkxKiHsLVIDmUcdsdVwGIjvCyyjpxhIgM2C75jqeuNlX4ssr26flUqpaCeSECFGkXl-6D83N657BPYKgiKFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌ها نشان می‌دهند که قطع اینترنت در ایران وارد شصت‌وپنجمین روز خود شده؛ این در حالی است که نگرانی‌ها درباره وضعیت حقوق بشر در کشور رو به افزایش است.
از طرف دیگر دسترسی گزینشی و سطح‌بندی‌شده برای عده‌ای خاص برقرار است، اما عموم مردم همچنان از ارتباط با جهان خارج محروم هستند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2263" target="_blank">📅 11:13 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2262">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بلومبرگ در گزارشی نوشته که قطع طولانی‌مدت اینترنت در ایران دو پیامد اصلی داشته؛ از یک‌سو توازن قدرت رو به نفع نهادهای امنیتی و نظامی تغییر داده و نقش اونها رو در مدیریت امور کشور پررنگ‌تر کرده، و از سوی دیگه فشار قابل‌توجهی بر اقتصاد و زندگی روزمره مردم وارد کرده. در این شرایط، دسترسی محدود به اینترنت نه‌تنها ارتباطات و جریان اطلاعات رو مختل کرده، بلکه کسب‌وکارهای آنلاین، تجارت و خدمات وابسته به شبکه رو با رکود جدی مواجه کرده.
برآوردها در این گزارش نشون میده زیان اقتصادی این وضعیت فقط به تعطیلی مستقیم کسب‌وکارهای دیجیتال محدود نمیشه؛ اگرچه این بخش به‌تنهایی روزانه ده‌ها میلیون دلار خسارت ایجاد می‌کنه، اما با در نظر گرفتن اثرات گسترده‌تر مثل اختلال در زنجیره تأمین، پرداخت‌ها، تبلیغات و کاهش بهره‌وری، مجموع خسارت‌ها میتونه تا حدود ۸۰ میلیون دلار در روز برسه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2262" target="_blank">📅 08:37 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2261">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">روز شصت و چهارم از قطع سراسری اینترنت.
لعنت بر جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2261" target="_blank">📅 08:35 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2260">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2260" target="_blank">📅 19:31 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2259">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 44K · <a href="https://t.me/ircfspace/2259" target="_blank">📅 19:22 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2258">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Khu0NsLMJ86JcOzyrhLshj3_9XYEKK3n2smNjGEdYRWS2EpvAFf9V6IqBCaJrJ7EfwWaGVrZJs_nuhjDuANgWpEOXQRsJLNJcSp7LTBdn5FQGS_IReYTTLgI-gr4p7Vl2SPBE3TXeN89SuAkmtwc40qu9s1dwnCfmNBodyJXWMoB0Qfi2ey1V6TWVZyBUPxdMdPH6OmvnmFrka9Dn7cODuSX-R5cYPncHV7kce3rdOzSycr-Ch5vn4MnP73Fzku_sQtztMm0vw0KoI9kfguAZ9MPbG_3fN6GzxKqrRO6wdCl7mktush5EVrPdqFkVb2nllVWLI0dxFevm3VWjs9xhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با روز شصت‌وسوم از قطع سراسری اینترنت در ایران، گزارش عملکرد سه‌ماهه اول سال ۲۰۲۶ شرکت Meta Platforms منتشر شد، که بر اساس اون تعداد کاربران فعال روزانه این شرکت به حدود ۳.۵۶ میلیارد نفر رسیده و نسبت به سه‌ماهه قبل حدود ۲۰ میلیون نفر کاهش نشون میده؛ هرچند این شاخص در مقایسه با مدت مشابه سال گذشته همچنان رشد داشته.
متا اعلام کرده این افت فصلی عمدتاً به دلیل اختلالات اینترنت در ایران و همچنین محدودیت دسترسی به واتس‌اپ در روسیه بوده. البته در پی انتشار این گزارش، سهام متا با واکنش منفی بازار مواجه شده و در معاملات حدود ۷ تا ۱۰ درصد کاهش یافته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2258" target="_blank">📅 19:13 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2257">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2256" target="_blank">📅 17:33 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2255">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lBu8zHw-YTzM5mtKBKlibrxxOqC116m27yhHsbKGeLAJ_EH1yVk0H8pl6lPNHJfnwXjs0V3AO5wlHertg04KP8z888sGwE9T6XYLITumll-yzNaEPw2p6dZYNetvyUcA8i_WRVRVpHoELgMy96OkH7wiN46oXcPK5BhYNBf_tm_mAgxlWsO_VLeBwCjIdbOPll77Z5uS5uVBk-XjTj2CRlWoNMq_NLxTuzded0aXLGpydobnkgRBJWwuRL434ebREsRF7M3CeCd3hyOC24L_99E-4yZQGbm7Cu39f8EWCgsiG-38IxthaCIRS_4PDoSliKb9J6g7sIgtGSHebfCN8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن صنفی روزنامه‌نگاران استان تهران با صدور بیانیه‌ای تأکید کرد: دسترسی به اینترنت آزاد، باکیفیت و همگانی یک امر تشریفاتی و لوکس نیست، بلکه حق عمومی است و دولت‌ها موظف به تأمین آن برای همه شهروندان هستند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2255" target="_blank">📅 17:27 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2254">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ve_3FIa0VH_oNwa_MsvAgwIUVWkv-8RtbxpOhiNrEbH2YFnW9IKKdp1XYRVLTgOJjg9KnUjuIdYYpVoPiRKII_1OshR_MpG-N6JrTrA_bt_-pEMaQUrqgHB-oPZxV7OF4rhri_7RgyADCTOna7CBIrLLqbQ2MjGlbXDjZIDvmnSTjKxhGG_86xLScZBFzBCzN_teyFQ0jpM4AMYkIJnYfjtPd3U1xHhEgcPr5hHaYPYPIWY-SaFcChxxUCgTQ14ki2cFag818S7qA4LWaENs5u9lgNSKGatKLePAmm70kvXUO_MT3fo4bZliSe1Y6fblQ3FWnxuoqNuHLVz0ZozSgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ACOKtTVkuMHcavtY1dSarW1d4WR5y0AMNklrRvqCHOjXZAP7dxynqeKp8uOFTwLJCKUsjefLu7udP3GozLng54O1l-O9K-iQEyv2i8SMH7ggAoa8NZIiqFb6u-9KNZsEmbRLisg8RuiA1WzhK8OZcftdjAo6KTwgKdf2PFNuU3kXFw6kXv5c34BoxH_2y5GW25bbo3-9qY4OVtG6TNMJUGd56iVn2xwJQhiOG35OS37FBWrUHZhd-3hZ4oaUplf5IQHvaf9GzAG9bRJKMhXB4-GL0N0ttSXB1yi7pb5DSw_FDQe6qhdZnbYNzywHY_sPoyhzlLQ78dNO1QOlJNeDPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2252" target="_blank">📅 08:35 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2251">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VNzmelhms0heyyuA38mQB_nXsH7ZTYp4AaYBfGs1t9920Y6zaWjDFHO0r06dz7vEgt83-RykObhJ1kxRVbHOxwgq3RO_KKFfLpkcm-Mr0eFou8JCc3T4ZQ_QcLuNusvqHWiS2WApWUjj0mMqZi3P5Y41_2m_J-lOqut1LoLRyzkZafy6Vq0hcIyn0LhkscBPl94QXJp8GZM5f21jE-KdQIoqSDcYb1RPvMyM6R-nMFZJEK7Ykh0U0Dx72xoIZvaEYNIbw20gIIEYyq7pxQruFHPXx5RkkQ0cck09FC6VX9vfF8S__h8vf-LBjcgs8g3pe8p04ddTodUvtzxgEWpvIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l_GxTQMjjMnk_UpT-hP-LGQOYdvALJgyw7Lr-53u5D31Lm9p2sLBhZHjtLZyP4tNrCeonorHyAsmetGC50_uJjApGEQuWUyAFJv7uk8BWxU6x_vXhHCbDk5Z4WT7ReSUhQi3Y9Z0ufkm4J1mPAu_rlP88HB83xfHhyj_76CE_YeX_8mMfHO7Okn6jtKNZlxdDDAm350zUjBwRI5rTxTFfI2Y1iZwdlcVJ7c7jEbv3IC_Pva1gv1Q82zwlD9TIAUr5ENyZPlqvX2m-nSbN8GNZQsP8-jnQ-nMyUbX0zuVFoX7hoMTTSODa6JSfTHxyxlyg0LTZr58hw6FQEvHcc52fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2250" target="_blank">📅 17:46 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2249">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GNy91tdBtrBruwLACWlvfPGGB8-7GzKBMsJq6QSwzq3rUUz78F0tz_ascqoJrRFHkeYUXxPjdgbG97hCTKNDRnn889ku7m3O0qcR3qB83Z6aV_ABsxXukzdw99wxjfK6_-JnD8vd7EYvmxjq1W_w6JkcKvs9i8RR2Zu2R_NKrOPxzya6YOlsh6lM1BYGLVnOCDI003XBzOa5HcglwbDIVsHkDw3wGvPwLPCf1j8V3bNs3lK5ajTH8w9IdnrYadyHob5DKIqMgeiV2yAAvFsFBT4HSCvAvlSxFbcG1F5Tbyga3RcYWv6y7ivrXSPQJ7JbhJvoySRL6dJZPDktO6JOXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ADmo0UOOkF4QFGd_5MLwW0H9uV_IgpMu9YkSv_YK9_mwpyh1J-Ih5yM7BCkpp0tYMszhlWUwzmCLNgNemHbLVtyL9i-mlfuAU_i09KE5ucfu8e1AMyuNkU9tln4k38p0QQMd6-44ezwav--Yw883NUDGqbkiSfaUAfqCKvVH7MKqqku6jz_jHElQvbZUs5wdiC5Ul2Y-EEfO5XWyl7UyeDgtxKthpVtEnNugP2DOKVZww1zXlpwYpUZ7InRODig2-61x1pYBwmckRLER0plVNqTYzVIO6KRbCMyagaLGd63SPtnyZJlETwXGguK9Ru5Pba0Kb0bZQUqZn0wp5bhxtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">روز شصت و یکم از قطع سراسری اینترنت در ایران.
لعنت بر جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2247" target="_blank">📅 08:48 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2246">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XlF1pFqY0XQtGmMHNuSGbK2pY1UD_l9RE48F_1aCo4JcJdmMSoIJYHuW80lQyyQWCRYA-Acuih2c0NB-vKxnT5Gp5ynVmJORNmSmKDbmCJmofm0nwpbNvPS3SAlUPdwuhW1-XwZI02BDdqu7wQWvOdKyiZd-b1KpuruFhiDhYRRtFdcbbGDTeL98Q4RJIS2iqYcpDKamNz7hwdV4qn-nIW6PLjbOVvYEPM3WWif8UZOL_jKEqQaSIiy4asSPj5KPFsW8yQEe1yLsTEiD59dUvaRWN-GsvoWXhLdZfQ9hnUnGPEHps_yXrqyg1sm-gVscVnFI1QPTCF9skT116rdZ5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2244" target="_blank">📅 18:33 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2243">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رکورد ثبت رزومه در جاب‌ویژن شکست و بیشتر از ۳۱۸ هزار رزومه در یک روز در این پلتفرم ارسال شده. این مسئله نشانه‌ای جدی از تعدیل گسترده در بازار کار و تقاضای انفجاری کاریابی در پی اونه. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2243" target="_blank">📅 18:28 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2242">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/arRoa0gua9Q9OqMpd40ZN9N20_oaZ2Hup0NkKmDrn0X4l0QHioLPid6Xv7AFCF-qkUrayQjnLZdS7CNPBy4ym74bFi07w6U70Iwf3xkU70qKQOOsX5Vnj42uWWwq9Y-tygqNLd5I7lDp4suCDZPP3jG7ba77rOBxqXQdPb8K9Q47gT6pzAink_6KW4mAsvlmKWl-lnnBdb5_-jxyYaknk9ZJLXNeo6YT9tChWQBvbJAuw0O82_AZNo3nDlX2V-mR2sc3EtH5wKonojhMdH1v1rzE_eOK3AuRP1ZltY_xVb9gXytssbjQSkjq2GkVPmHlhm3TuPCo5Zec3sOXhvIM8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2242" target="_blank">📅 18:22 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2241">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AYchB8Mc4lW51tHYXpxV1aaiHJZWPm1um3V6aFbNzCLgDFF0ywj33CsJyKQ6TgdOyhtgbpR8frfWAXiXPKE0v0TuGYi-KKQly_xzajcuGCTo9gt1J1rPZJx1m59feaxkZMW1fYLl6b-LVcPL_T-6X7R2VyWaBmEPKEKkMF-8DvYPXHXrz3d2CFFhdOxEseSK-TMTOaOhdASVNqst3fp7xCM3VZ9j276XmvzpeWB7lqdTUIZDmzSg2XHtdPq0lNRtLWffvelqrtSRUxul2vHdMpOxfmLnNwOoqEwZw_VOrv6aihp4MzEteebo1AkBzki8XohchS7TCwPOVDP_wxOO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد روز ۶۰م از قطع سراسری اینترنت در ایران شدیم.
وقتشه اسم وزارت ارتباطات رو به وزارت پست، تلگراف و چاپار (به جز پیجر) تغییر بدن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2241" target="_blank">📅 08:58 · 08 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
