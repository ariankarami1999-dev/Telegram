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
<img src="https://cdn4.telesco.pe/file/Hv6kUFaq0ka-1DMYkyQXnYK4kMwn0D4BghdVQBh1dnn3MnlJmA54cVtodKbQYh7oLPXHItaRzq5vxOO2fPiwNFf1rzoSm8Kc8p6sVT7OvJAymazMJZOibF6CWCNXWNU4_gTxWyPMcbVzBGxXuc5asys7JjvvIo9EfnPeO8cnNUH2PxTsRw3kQf5_JmWYb70pHoiRSftI4vE4f4nUPQOIun0xP-QLYLwXr5reojHxauL6L17elShfYpuMaMvUPZe9-q7Ggh3tVfurilG1axcJrgm3i_5R-97K8xH5Nx2QPyaS58LoBjwjnm_y4AAFS9OLR1JwkIkeosa1MRgebhtAIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
<hr>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6dJuyYHqRNfxmkeOKQXdDr7zoUFOeAjf7lN9iCaNCYzzpUMqbTWQVPT5AZhv1InAQFGXP01emxMyPpPjy0lWVzpbPwyRoJZm_O6l2woA836bXMDWjDnjylTkHTCZffymGYqZQzUpN1Amf3EAz1-YuRgA_M1RyW-31nsY_NxWZQVJe5YIF_qmw53ft1zgerhmOqWYXfgKRzEehYWXOIwPt0eYwHWcfHemncl9A_kutSZ5RxrtkbiPN_Hw9Ks9mh6pmOKQ1WvjNvh7EaTNZ6Dc53UkNGQSG9M3uTF-0Q0XeB-CMVNnhycOILZC5Wi_iLgVOcLerXhe8ypo_yzUF4NrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
کاربران رایگان جمینای فقط فلش‌لایت می‌گیرند
⠀
‏از ۹ اکتبر به بعد، کاربرهای رایگان جمینای فقط به مدل فلش‌لایت دسترسی دارن.
⠀
‏
🤖
کاربران رایگان: مدل‌های فلش و پرو حذف می‌شن
‏
🤖
مشترکان AI Plus: فقط فلش‌لایت و فلش می‌مونه، پرو می‌ره
‏
🤖
مشترکان پرو و اولترا هر سه مدل و قابلیت Deep Think را دارند
⠀
‏به گفتهٔ cnBeta، گوگل سیاست دسترسی حساب‌های شخصی جمینای رو چند روز بعد از معرفی مدل پرچم‌دار Gemini 4 Argon تغییر داده. خودِ Argon هم فعلاً فقط در اختیار سازمان‌های امنیتی و شرکای گوگله و به کاربر عادی نرسیده.
⠀
‏گوگل گفته زمان دقیق اجرا برای مشترکان پلاس رو با ایمیل اطلاع می‌ده.
‏این تغییر در مرکز راهنمای اپلیکیشن Gemini اعلام شده و کاربران AI Plus زمان دقیق اجرا را با ایمیل دریافت می‌کنند. سهمیهٔ مصرف از ماه مهٔ امسال بر اساس محاسبهٔ هر ۵ ساعت یک‌بار تازه‌سازی می‌شود و سقف هفتگی دارد.
⠀
‏تو هنوز از نسخهٔ رایگان جمینای استفاده می‌کنی؟
👇
⠀
‏
📌
گزارش کامل تغییر سیاست
‏
🌐
اطلاعیه در کانال AI Copilot
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 315 · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIve4QABb6AleZxHagHrrgY_Y5Eudss2M4IF2fLL_90LSbK8QEsOJ7Z6cMSBl2LExjsUvA2kMvIFk8eHVoqo13R6cVZ5newkZjRx_L9E4CouFd1x1tG2xgNyVdQebvSW2ZZ3GNr45F36u1h9Wlx6BstWsDt6rxmc4frb6HW5MXKtr_bGUnIWEEchZz3DFvDlSrOKdvJQSX-zcigJyWeRlOyV_1LgSmIQCQdAZqqGRRixJKzRKdHiEbhcPOvf7Uk_LzNUhmvu-aAzC2H85GyNybLhDLf5IPGVZmpaD9wQFMH2v3uufH1SkQ2lB1ORZo39MNJKjCvxtVC2qGedCB4YcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🟠
مدل‌های Claude 5.5 به Antigravity گوگل آمدند
⠀
‏در محیط کدنویسی هوش‌مصنوعی Antigravity حالا می‌شود از Opus 5.5 و Sonnet 5.5 استفاده کرد.
⠀
‏به گزارش سایت appinn، دو مدل «Opus 5.5 Medium» و «Sonnet 5.5 Medium» به فهرست مدل‌های Antigravity اضافه شده‌اند. Opus 5.5 برای کارهای پیچیده و طولانی طراحی شده و Sonnet 5.5 برای کارهای روزمره و کدنویسی است؛ Sonnet 5.5 نسبت به Sonnet 5 بیش از ۳۰٪ سریع‌تر است.
‏نکته: برای استفاده از Antigravity باید با حساب گوگل وارد شوید.
⠀
‏شما Antigravity را امتحان کرده‌اید؟ این مدل‌ها را تست می‌کنید؟
👇
⠀
‏
📌
گزارش اضافه شدن مدل‌ها
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 932 · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hZb185HkmbVh6nxojS6hqkuRvrTWwQH-FReHgO7dZRr8V9sVHDaDRQf670tCD0u7IbakLTpfxUk98XZV7gqabKwyIGycx3EJ3-ntA5Bq87dr26BmoE3WZy_NxkXnwxIykWmEGQU2AYJodNLlECxUhovd9xeMTwnD-N3ItPViSg9MZNPn7ZvSX6aRtx28d7l4TfOdyBLFl-MASIsT0Pv9-hFM-CaR9rQ4sWxu7I5VYr58YRXZsecoabevxHOuboAZFm4nju9zD5NpHa_WuyxPZdtJt-RR0baoqGCtrlsYfOIJzEW0qWLXtfIOmKgMRgEiS3s7wOF8qzZVUSsB4JGJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
مدل GPT-6.1 Sol اوپن‌ای‌آی رکورد زد
⠀
‏سم آلتمن می‌گوید ۶.۱ Sol سریع‌ترین رشد تاریخ مدل‌های اوپن‌ای‌آی را داشته و مشکل کندی‌اش هم حل شده.
⠀
‏رونمایی در DevDay؛ هوشمندی نزدیک به آسترا با یک‌پنجم قیمت
‏کانتکست حدود ۱.۰۵ میلیون توکن و خروجی حداکثر ۱۲۸ هزار توکن
‏ابزارهای جست‌وجوی وب، جست‌وجوی فایل و استفاده از کامپیوتر
⠀
‏به گفتهٔ آلتمن، این مدل در ساعات شلوغی کند می‌شد ولی حالا «باید خیلی بهتر شده باشد». قیمت‌گذاری‌اش هم برای توسعه‌دهنده‌های ایجنت جذاب است: ورودی هر میلیون توکن ۲ دلار و ورودی کش‌شده فقط ۰.۱۰ دلار.
⠀
‏نسخهٔ Ultrafast هم در راه است که تا ۸ برابر سریع‌تر جواب می‌دهد، البته با قیمت بالاتر. نکتهٔ جالب: قرار بود نسخهٔ ۶.۱ آسترا هم بیاید ولی به خاطر نگرانی‌های ایمنی فعلاً متوقف شده.
⠀⠀
‏
📌
گزارش عرضه در DevDay
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 984 · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/anwphxjQ4onNZKSYFq21oCWXw06dtCn1Z6zAg_gdbayeN42hbHMCzJlkc1TToDPkwmET6kBsTYeg-4p1LBsWRK5CdJZtPP5imll-gHp4VujGuzx40WjALAWCH9ICMvzx5scWFncEu4U3Zi2V7ywqxZHGKznzbEC4SWil3TVpsuC3U4QTQI-KUiGnSFj-XgSmRKg52HSqcDXQiGEajXju28ynqJm0kzHaroe1EvBhEYQROI7tATBeE3qLkJwQb-RCVFaehDim49GzZMgggz5RzhM_Pff88LH1frLnkr14nS_cZphLck2VJuJHZ_6youcrSW47nZrk0TAsEhsygf90qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔢
مدل Muse Spark در حل مسائل باز ریاضی
⠀
‏متا می‌گه ریاضی‌دان‌ها با کمک مدلش شش مسئلهٔ حل‌نشده رو پیش بردن.
⠀
‏• شش مقاله در حوزه‌های احتمال، معادلهٔ موج، نظریهٔ گروه‌ها و جبر
‏• مثلاً رد یک فرضیهٔ ۲۰۲۴ با ساختن گروهی ۳۸۴ عضوی
‏• و اثبات فروریزش در زمان متناهی برای جواب‌های معادلهٔ شرودینگر
⠀
‏نکتهٔ جالب اینه که توی هر مقاله مشخص شده کدوم بخش رو انسان نوشته و کدوم رو هوش مصنوعی. البته خود متا هم پذیرفته که بعضی از همین مسئله‌ها رو گروه‌های دیگه به‌طور مستقل حل کردن؛ پس این «کشف انحصاری هوش مصنوعی» نیست، بیشتر یه نمونهٔ جدی از همکاری انسان و مدله.
⠀
‏فکر می‌کنی هوش مصنوعی کی اولین قضیهٔ مهم رو تنهایی ثابت می‌کنه؟
👇
⠀
‏
📌
گزارش RuntimeWire
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpOdGyIzDD4eZvAsI0AIfHf8GH2HaW5CgKsSYUyBHCx2NjPL1azXLigTOzo5jsJc-jM3Ehio6QT-0x41MdUUzeOPKjjIeljXvPdlOswf2jLdh9hbYVZbqIZCQHm47_pBzq1gFjt51YHbuNCdKYOVy0a7-MOQ1ZGTvGuG5UsvkZluUrwb9pZS-GWew27maZ-ETrcpcagJvX8MrFfpND4Uw21NniE25ke8Bl1sVquXXZY72tT_DMudjWjqh-79jlB_QETAnFVgh40s3soLEA0Im7ctggs9E6BlcK0VzIUFFt30vv-dweMXzzIfm4uiXb6zw9wwIZmj00-n9o0U4h97LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📨
ایمیل موقت جیمیل و اوت‌لوک رو با temp.tf بگیر
⠀
‏یه آدرس جیمیل، اوت‌لوک یا هات‌میل برای ثبت‌نام‌های یک‌باره می‌گیری و کد تأیید رو همون‌جا توی سایت می‌خونی.
⠀
‏
✅
نه ثبت‌نام می‌خواد نه رمز؛ آدرس رو کپی می‌کنی و تمام
‏
📎
پیوست هم می‌رسه؛ عکس همون‌جا باز می‌شه و بقیهٔ فایل‌ها دانلود می‌شن
‏
🧩
یه API رایگان هم داره، بدون نیاز به کلید و با سقف ۶۰ درخواست در دقیقه
‏
این آدرس‌ها با plus alias و نقطه‌گذاری جیمیل از حساب‌های خود
temp.tf
ساخته می‌شن؛ یعنی ایمیل‌هات مستقیم می‌ره توی حساب اون‌ها و چون رمزی در کار نیست، هر کی آدرس رو داشته باشه می‌تونه ایمیل‌هاش رو بخونه.
⠀
‏
📌
سایت ایمیل موقت
‏
🌐
راهنمای برنامه‌نویس‌ها
‏
🟢
سیاست حریم خصوصی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOagb_vLCD5vpB4SSRC_OiX4I8w4iTtrOBGQiGkByFRt0PFvbT-m-FzLdiJVh2xGSJM6SOorhWG5oW2roF59GNf7p4XYO05bhNn_up_kadv9jKu4unMttJICdF0Jwn_xyFT5rSY_EkD77CLKOHrOSb5bJctKe_txZ2q1bwpWG8ZTJDZFe7EwYlcjPnFOvAH30lYdsdE1O0RG30Pdj6d899i0HRdeL9_xWrKaQqzCbi3yLNtFdqRoqeYqvtRke3o77cWr5sbtvF4mvqVPR8_0d0ANUWGtmX3PDMS-1QlT1FpHq5ILPTpVJMCnsT-LoNiSRPka0e0YHbDWWH-RlXUSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های قدرتمند هوش مصنوعی
💥
🆓
GPT 6 Astra | Opus 5.5 | GPT 6.1 Sol | Sonnet 5.5 | Gemini 3.8
✅
با این سایت میتونید 7 روز مهلت برای تست مدل های بالا رو در پلن Max دریافت کنید
🎉
🎁
⭐️
قابلیت ها :
🤖
چت با هوش مصنوعی
⚡️
تبدیل لحظه‌ای صدا به متن
📢
تشخیص و تفکیک گوینده‌ها
📖
پشتیبانی از ۱۴۰+ زبان
🗣
تبدیل فایل صوتی و ویدئویی به متن
📞
تبدیل تماس تلفنی به متن
📝
تبدیل جلسات Zoom، Google Meet و Teams به متن
⏲
ثبت دقیق زمان هر بخش از مکالمه
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By_mwIKZaErkyMbaLhDbfIUboxJa1JABxg65vS3m25bRyz6ahKF4PpcA73mvLTGEJ7fI1W2Wls6n-5UfjUCHQjZWOmdYnYMcmi_Xahm3xUXaJdQPyAbkQtdAc4CPt53cz4xvAo00YtdY3Kb8eFYNJ-hRgfLnCD-_ZOYewMcr3J8sLBjsi3nCuzx2bx-7NxRlhgiheWkDxni_BhsfYGfi6p8s_zf8jqK46wzSxVDe7LzjUYJYG02_iRaJ4UDZ96DfmfgXpbxSyIRmbTCYmHFzCKD_K1a438_kXqvAqJEa8dE7L82QsvzOBiXxDAFSCw2jYj_sWoqyLe7WH6f1OrlrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raZv00khQQ8-Icw1KDxvCo2vTva60AwnI9WB5Ar9mN8DzwpmPo_p0wxf8MvR4pH9Eo5sz1hmqCngM47udaSDXN1fLnUyb7A_4RZR0w6Vbst2caMS3LCQyMpSAObDJbE0-evVPkhiBb331-hczgoqe7s0iRzOjVjXDeibq61h5w4KdtVGnp65lwOrtLTCNuriUg-8C93uijHA9pJw8l1S3iUATCI5cCEuF5HQn7I_C4MU_dKJVO9nLC6yHqKQCLp6C_qhfxoeYDD9bEvRV1xh57IUvU1KvHy45QQzSUFUr6YGmEW3MKiEC9gnzQkAlNqzcHJIUmSSQNm6eOR9z1pjcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⏰
سهمیهٔ ChatGPT امشب ریست می‌شه
‏به گفتهٔ مدیر OpenAI، ساعت ۲۰:۳۰ امشب به وقت تهران سهمیهٔ همهٔ اکانت‌های پولی ChatGPT ریست می‌شه.
‏
‏این ریست ساعت ۱۰ صبح به وقت غرب آمریکاست که می‌شه ۱ بامداد فردا به وقت پکن. Tibo همچنین گفته مدل GPT-6.1 Sol اوایل عرضه به‌خاطر بار زیاد کند شده بود و الان سرعتش به حالت عادی برگشته.
‏
‏
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB2QqxVFB7RMLmVskE5jhQ5FEF4ZVeQ-E-U0RXSlEyD7QG2AliE6Fs94Mx-HcoD52oBQrIrDK6J90KPlQPDqhDE1gB2sXTSSIJm0FjQRiDc1v3NpcRflj6s3xq8HcWhJP2k-bZXvSfw-pXo8T269JWxKYw9ZvTq0VutQnBiSTnqwE0Kda8DrA2qNGUNB3lKuCIiJr_GzCAikdx2CNoEeDhML2ZMkq2XoV1dNA-6upxxZu_nsRRtpQzP4Gy5y8TXpjxE6eOdynWlD0lCCa4j2mIm09RBNf3qGLw2EobHawTajpcbchxR45PI9hf90L67w27wuOYfwdYIkogjX75PWig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
ابزار InkGist برای خلاصهٔ صفحه‌های وب
‏لینک هر صفحهٔ وب رو بهش بدی، تو چند ثانیه نکته‌های اصلی، کاربردها و کارهایی که باید انجام بدی رو تحویل می‌ده.
‏
🤖
مدل‌های Zhipu و DeepSeek و Gemini پشتیبانی می‌شن
‏
📚
خلاصه‌ها تو بوکمارک‌های ابری چندکاربره ذخیره می‌شن
‏
🧩
افزونهٔ مرورگر بوکمارک‌ها رو با یک کلیک وارد می‌کنه
‏
📷
از صفحه‌ها نسخهٔ آفلاین هم ذخیره می‌کنه
‏
🏠
می‌شه روی سرور شخصی نصبش کرد
‏به گفتهٔ سازنده، متن صفحه اول با Defuddle به‌صورت محلی استخراج می‌شه و بعد برای خلاصه به مدل زبانی می‌ره. پس حتی تو نسخهٔ شخصی هم محتوای صفحه برای سرویس مدلی که انتخاب می‌کنی فرستاده می‌شه. نسخهٔ نمایشی آنلاین هم روزی ۱۰ بار خلاصهٔ رایگان می‌ده.
‏
📌
مخزن گیت‌هاب پروژه
‏
🟢
نسخهٔ نمایشی آنلاین
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sujCjJhGW-Wgi0ukNMBwTLMNmXTWUW1LbusKahT3rS66qje974nv37f3-jjs8AmBhApYGoxSNsg-ZUhMVcioTHfVHZP3FDraTsZeEsXpkMNR7lO4VbT7nlU8eFGVEEZERYtu2lyor9pfXjUAeoOHhVrtr2CvuDkGcVrCJQpLjPimQWri6Gc28L1DXT4hzhOMP8GE7dW6viHOjZ8aJ2ZCPoMMROdfy3Ggul1CcRF2n5bEEZk7vUDbr-B8Lk6Ie6paU7HaTJuL4F4Ln8xd320SPqSWPvMPlsWFOc_bgZVQudMAwO180-ugB3x4Iku1kzEaSy5DvQrG_ed8DXGQd60Tdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kL-SFW0AlQHkfbMdDSjaR3tcd-h0yWPRtrnh7C9ZEh49dEby99Btqf1f6jOxcMhiqMCkG-W7HiwWKW50pWkSrjhVtxrbPRD-NrwZXQf6uE7CJi0Sj9A4PP_alWqTDZ269Xb88rpj3rNExTkstfwP9cRxPtEbICLfzYnH90lvx-XkdpYCjnIGWC6wu7AvGDYj0HbrxhCV_7378SDL32445O2WyckbH4H9_3vgvZAVeX6gtsDqwAF8Uo7Yg65QtM3KnsnNHYdpVEJ-Gg3ZtwxQA-x69TFcHSyAemRXL8RjwFfSZ0Rtj2qWA1HlQ3LZxdWvjvjTh6wO0jaLAsJTtr-FhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه
‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.
‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد
‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد
‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه
‏به ادعای Anthropic‏، نسخهٔ Sonnet 5.5 بیش از ۳۰٪ از Sonnet 5 سریع‌تره و هزینهٔ هر کار باهاش تا ۳۰٪ کمتر شده. این عددها رو فقط خود شرکت اعلام کرده.
‏برای Haiku 5.5 هنوز تاریخ دقیق، قیمت و شناسهٔ مدل اعلام نشده. حرفی هم که می‌گه این مدل از Opus بهتره، فعلاً هیچ منبعی نداره.
‏به نظرتون مدل کوچیک بعدی به کارتون میاد؟
👇
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2DDCa3BFHiLJp7i1iLc-sYgfwrB1F2jlreAD8z4mtThafjfpBXMFFnk-5JZJpkjV16cEPRh1a-O9bD123yE_tne7auOxty7Q2HfyeLAfFLN0xkcvglG5ns8A1gK0JfP_GNhq_kyIAng_6eBCTPT7_PnrKTYicyIteUhUjbvihUbzNXzAHOC-qkr5Qm8_eRIpR-Rf8Rw8sDsqudyLoGQ2wb1zFcONHkCqq2J4QmjkSbYWMu_qu6mDkf1TA9yHvKyzmFcJdHVx_y_74gZgZfVEu-PuYg0rS_dnHQv1Nwegp-tN1lfqCgSEKyNsHTJogrAAwZWwy1GWJKxBWLm9sbO_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Claude Sonnet 5.5 روی اوپن‌روتر عرضه شد
⠀
‏به گفتهٔ Requesty، مدل Claude Sonnet 5.5 با قیمت ۲ دلار به‌ازای هر میلیون توکن ورودی روی OpenRouter عرضه شد.
⠀
‏بیش از ۳۰ درصد سریع‌تر از نسخهٔ قبلی
‏هزینه تا ۳۰ درصد کمتر در بیشتر کارها
‏پنجرهٔ کانتکست یک میلیون توکنی
⠀
‏این مدل دومین عضو خانوادهٔ Claude 5.5 است و به گفتهٔ Requesty در کدنویسی و کارهای ایجنتی نتیجهٔ به‌مراتب بهتری می‌دهد؛ قیمت خروجی هم ۱۰ دلار به‌ازای هر میلیون توکن است.
⠀
‏مدل هم‌زمان روی پلتفرم
B.AI
هم در دسترس قرار گرفته است.
⠀
‏
📌
اعلان B.AI در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwLJxcm71aHILOg6B6GkhUJ4MnphiNq2i3M6tYv53eXBP4JPp0DCZDEspaNOr5vVCMlw6Y9uVpaHrsN4FrEsaadBZ1fRKWfDt-sCUdgViKxNduiqsGF2rU8Zwe5oZJxncQRd00C-PK1p7QLohCUeXNwqqdH2Ss25kuMQQBBEoVSbWmAkG35d2i45-hYdxlXSU_nv2ru1kbVt8JUr7rzGJC4EmEp9878eLmyS9sStDxCzQQXUUizbYMeUR4Todw1jFiu-5nxEGJMdJpWO7PF4vElZx3Owi0NKeLyJysuiYrK-IfJ3kcOjEz2c4nExXmt2blfDqg3yMeAaLcqQ69d86g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
همهٔ دستیارهای کدنویسی توی برنامهٔ ccgui یکجا
‏اگه کار با دستیارهای کدنویسی توی ترمینال برات سخته، این برنامه همه‌شون رو توی یه پنجره میاره.
‏
🧠
موتورها: Claude Code‏، Codex‏، Gemini‏، OpenCode‏، DeepSeek Harness و چندتای دیگه
‏
🫧
یه برنامهٔ دسکتاپ که با Tauri ساخته شده
‏
📦
نسخهٔ مک، ویندوز و لینوکس طبق صفحهٔ دانلود
‏
🔄
آخرین نسخه روی گیت‌هاب: v1.1.0 در 28 سپتامبر 2026
‏کد برنامه روی گیت‌هاب بازه. ولی ccgui فقط یه رابط گرافیکیه و خودش موتور نداره. برای هر موتور معمولاً به حساب یا کلید API خود همون سرویس نیاز داری. کدت هم برای پردازش به سرور همون سرویس فرستاده می‌شه.
‏
🐱
گیت‌هاب ccgui
‏
📥
صفحهٔ دانلود برنامه
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOc5wI09gBF2309NB1g3OQ0y3ZR9qf-PwiISwzVtlOVUTR_VgXv7vKXVqhNWXRriQ0dINMldkIFaZr6qTx1WzW5Vq0PqJ4bOzepN5iILI2IsZjK_rglkTTi0yN_b7WxhGHpwhycUoun8mqJ5UxOqrcYfD1KDtszeuU83VJoRRup9jDFxVT178Pq7WpqCEyCTVWCT5w_wJ6c-raELOzEN7Ua5VakFa_VgdCDpFZSBYhIWWoHOd5kndm_ObnfYcWUL1iS3Y_cE_DWC2JAaugi5svZI1es6yeBdkdQsbh5YaWY8BP520rjzpAmZGNJ9JSxkikUIpz83A9oy3nckyIHUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCHpw1esN9NyTbcsWq63vnuh0RhVeQGFTFOsF8Wgb_r1zCKGO-eFRXA6ZUIIxYF7KFHRLHJMmCC7VguUh_vu4oYsLPu_WErs6eLZQdOKumYRXZqyF88iwSMfo-7xYJd1pq1t1ZI4kyry7eDeNXfebz-_2P4SgHKy7mLwTABVkBaRgLqGQxkHhyP01afeSZfYaeXb8lmikgk5b5pWFpC9ZbOVbM65888YT0KL3bJDvwOIpAkkAxHMQva3NS__zAx71ghoKjCWpB2ouS-9J3h1uI0uAxqKxbKxVX4RBuZz6KTi47Nv6cheZgfhp5OHIBU016SGqNa-w8wGP0FTpEL49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2avPMb21Tx_9c55zHs2cjnbDqKKCp3DXBHSRx-CaTndCKXG67cBNAR1Q6yNkp5jD6-_xFTGwFqv-ARFdC8RzvBdFcVXDaslkk7nldNogOaKizsfS8ToTJU6DxGKT-mv_v2SuE_0N_ugBTdbfaDfurU8-RIrpQmeIrYI7iHEX66chRC3lmKXEFNe91o_JwJqSAoxapcLQ_FpSNJTtZwLY87vS80uM1ybI75wWxQBMBXsfDEZ00B63LVMfTrWQtJDv9RPrUwDBhtPSjscJIn_LXFx9skGpO49hZUCEpfyR3z1dj2wzRlzj4upUW-XdgN1M7impCXItLi48kpMYIoB1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIVaYpAnRpWADoFQ8DcdIjcID0Z64OJtrYuu7luH0eTMUKUAlNwYGwPLD4QB4xPjqo2qzUG7vnyZR9B-3Lcx6nnH7iHYdEVMKmP6irSObG0QWs1Ov-Owa9_cO8zYGbNXCKfDlgIJtYicm5ipNKTzotylJIDxAieRrszEC0pBHnyxgEeJekmg5_FP4Y5SHQNY2QS9k3ISMPMBWxUb8EJMZeQaaGBB_ylUXjUQ9Bz1wTpcSiVFGleD2wkDIDKb0e62NC46Zf26szW4uve4Ir64rWh56387nMxqvLKjY0L7ziWMXRoPRTfP7bZnHE9Q_DWZ2at0z_Aa5Q1dTpTe5roNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6mJmOvYnixfHrlGaqWWyrgsgnErJ2Tiv_WTroB5Z76VYuNND7irlDpqEDKx13NKOS9n4lepseU5G17J6T10RG6Sc8yOw9es0LuHw6Y9KPkW5TcEJREkMF4Y6pDegGEUyWAEP44R-P9G6BbW97vgDQosTsIStJWi-tquX3kG0-XyIB-XEEmZ1bEZ646uvUH29vn8xYvP-G0geO8g1JhHr34atx42nrLCtzXhjsNKffTfQosP4xtgmlQ5c0tH1akTOjiFkX4h33h1eW2bI3YoeA3Y4AYiaPwcA78KGiD2JKmoQjuxBtzX9RRuU1xI6b_8AUk663Fw2jPskUHGNpdGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tDlizwkZRcvmM5NnaBqEBBqKWJaBV_Dr8aV8mrRNtbL6Ztn0UDsp5VmF-ooHUhiBmq0UgnRkF1bxfuX_-Uo2eXE7JuIIyJrtQHZ9EG7AN0aKcx1MblimIOvb-2iBJNG6pAxXs4440I2AYZ_sHCU2c0HUEIJVSrzvghf19POy--cSHIna5ddP6k1mRJHeRVifU-yttlI8iNDyha8_MDki0_dlUV1JbAcK7tBvaTFj8H7snnFAhKSwOwqKMCEPW6gYOKLurvn75se4iDaEvguIXDRKBPk-8Tsf_kqrLHHsCoC-u48y3_HT9Ital3ApqfUqKyk8_vlyti42kA5kPU-eAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFHOA8UaPLXWSeraa0GAO39FMhbJhxZ-TZg3itPpWLwMLJ2bUyUSPZtZSLQhpElM4rL-WxARS0p6w8cj2NOrWSQ6tco0RM4sf3EsMaLoti4t4zmUaTknX2mWYHzOIy-_dC2MMYLsS1iWtzqNM5InbWqRPzqm8ANOAUmVbIcs-aszblYrqD7NYeqZHAUnh4keIuT8EXKi6PA7YV5b9MkUi0uwhpguP_oOjPSRuhNVLCsR-PKBtL1L7cCYHJC8yPDi5WrL_lR-Qf6ovKupZGY3PmqtSSONLR6uoNFPIKmt5lSPqt6RUDUpXb3yjV6FqftDJYV1yXcOUIHbJt9gImIHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
اسکیل‌های Gemini برای همه رایگان شد
‏⠀
‏گوگل قابلیت اسکیل‌ها را که قبلاً فقط برای کاربران پولی بود برای حساب‌های رایگان هم باز کرد.
‏⠀
‏
🫧
با اسلش در کادر چت، دستورهای سفارشی‌ات را سریع صدا بزن
‏
🫧
جم‌هایی که ساخته‌ای حفظ می‌مانند و از ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند
‏
🫧
فعلاً برای حساب‌های شخصی بالای ۱۸ سال است و انتشارش تدریجی پیش می‌رود
‏⠀
‏اسکیل‌ها نسخهٔ ارتقایافتهٔ جم‌ها هستند؛ به‌جای گشتن در فهرست بلند، کافی است در کادر چت اسلش بزنی و دستور دلخواه را انتخاب کنی. گوگل می‌گوید جم‌های قدیمی‌ات هم در مهاجرت ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند.
‏انتشار هنوز برای همه کامل نشده و ممکن است دکمهٔ ساخت اسکیل را نبینی؛ چند روز دیگر دوباره سر بزن. ساخت اسکیل به حساب گوگل وصل است و حواست به داده‌هایی که وارد چت می‌کنی باشد.
‏⠀
‏برای چه کاری اولین اسکیلت را می‌سازی؟
👇
‏⠀
‏
📌
صفحهٔ ساخت اسکیل
‏
🌐
گزارش نئووین
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUK2kDVO8t_WcvJ_GPYURlLzGj86R0kbMVeY9rmeNox3nIHXjyUZqbqEjjM4wsH3CNvkfmHyhE9-me1ZPMDEjtJvG-mkEvOoN6sSD_W5KxOM6PZwfMIV4TGKZV72Y4ezQKROSlNh2ZFPWmrnhZKhTN7RF5qRQRqWZ1TWYoAwgPTl49UQ6vHcl5BL3nQS5AiuSagDsHF4mulB2mdWQEjfcWJeRwmt42oD0Y8NmoB6nDqwxAoRySqGcpsFwhJNQq0rvTQEGtQC9e0OVizx3o9jRdm75OIzOHKJIN0lpU3wfuzvnqtJcdssGqLpXAOBTAD5Fq930jzvZlyJbnp1X-PBEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
آخرشم بلدین دیگه تو Routing rules بزنین کل سرور از اوت باند warp رد شه
هسته و پنل رو یه دور ریستارت کنید اعمال شه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cW5269eIeyp39dzsMMSO92oFn6Qlc1DpFkSJg-EGpVEsca9NYQbm_T6krDFh805IwmdtbRc_b9M8ylo4sIpL0NdLcWKv8PZTITZ_DbzL0GhVIROfsDb9JM4B9NpBXGcosXk4RopO_U0kM6Y-Grc3VupLu15jzYYMXtxwPUHL6dmw3gLr3CzQCwE5hluSzdeiaGXLBJQVPPNSEbHUZelWdl-Rn69K1QKmkt_SUi6a97AfSbPHE7OsxBSCjEGWOdmTOSPnv-lwyGsal0oyMLJWIgJgP0qVloAfSZTHtbsSUS4zQoKoytPUnqpUjRg0euSTzf7HPPMefTIj4LupcgefqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZ6nYoU2gTx4yvxnVsJnVsLu7OU7OS6hbqHKYDyRf41gvJzArx6AF4eQNN9lpZ0mdIjUeTMgy3k1zJDKqaH1GDxzVzK2GQmS92e7X58h5-SQyUopenndMGDEibDYjIie3G4Cu3vuk8SFOqBI5EnJNsjWrSUCTzvDIfNQhQWrLfyVkhgEzmtplf8IkY_s974KR459uxE963T4X-Fr3lAYuYRVPY5pzaEzA6lPH_78qYJ4tllCFBa5hshI3SLgwfYAqoE3yHJujaatraT_YjHf33qzKXC0NkvN_67ZPka1-brHB3NfTLwem4304466ZPbMRRV_jrwYZBkq38Mvdpyc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9X_mfCT5V0JTRzoKrIGWQr10GghpbrYFutsdBrHtUNkUdKdgukhzQF7ceELwGVLQf-wm36e7lpHLb-A8ZwRPGWJUFzcCMdziN3AMt76gER-VCEx9M1xv0pUz_4aeGfHqXmMfNofpkmzvToX_iPfS4dvR6B98nYfTn6KlHzDv9wu2C2Y5pZK90zTgn9yNGyisGQjnkt6-6vv1S4E3t_KJSwzLQH6HhUW8eK4pxPfOElrockLLrwBiBHd_PQUXPnOq_YT4v9Yofgq8P0lRwithKIYIT2wXXpxfO7TWcgTyGppdsxA7tWlF99VWd-mgM8O2MqYqlovocsD_HmL8lDJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuG-GJaHt_NJpk8c6bv6Mje00bVapjUlnmqS60e6VWTA3i6f64mEsHgEG1yPVvsJM-L5uy1icfrLQYbk8UWeWaJXir1dasB2bWSLgL5O7uLlQiZVFFbW3vnuZuCM-bVlgGI24S5k7WAcB_7oBNgQQeJQsP02MDEoLqKztM7Ve-IRQO26zJL8azuecvcLLW_wi6i0SwPM3Zztr23gTVFDFsPLeyGiu39JqUalmM0BW1VXG2a0gUaw6wbEcdylpntVM6R_PBnSV_8GzYB2cQ1HRL4QSg9t2QrSNx_ZiHcSIYeRk0dTyyvIHDTbx28jafnykn7ZrDc3gNEpKrfMzO6C6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UuFBIU8rwFgi9b6S0SjCPZbNm4YW45Ygu_bM_iA_-pzZ7oKkVYfB1kln309ALQW1CHJM7JT3qbiwW49s1giUYgCtdWBAR0_DbwbzazlQFMeZpESIFJlAHtT3toxS9LgVlFJRH_ilT9OJSaTVhX2Nz10z_6Iij6Ac33P-NCwseUxX3NWJScS7qBFgCYMbyf8tPB99zUWQVyyTm6MrYtGB2vi-fArTlFWkHg-Z3WHnJIzlK3JoccmPEvPNVOJQCvV8URzWEjs0270-LPbhqr37Pya6PnNNENB4ux-blTB0f9E18NENp4PwNqoUr3gskbKBn7aRMbWbqKdmUcl2pIVqWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I77dTJCIyAwC8CdFm9V3Y-Ve7bvRxgwuZ0BeCL2c50kgulVPMeisbmd9dUjpmOWNUDU7lKN3kw_470QHjrJyAGuAQ6JagSltga4-qjGlRY76Dd8ocGEG0ZB895a0_EicLSxy51VEw2wICRZz1BgsJrWGQ_0vPqwZdaIFM0chb60wQegGIL3kaBtuOteTI70Q0vJWS5xe3h0eJILrwiHa2RqdXRv8QZj5NH58TyD3Q8qPhuvOPpng6WPa7K7DAM_k7M2B9a4Mq_YJrq_NW9Kb4LofKWOBVTutkecCx75xvNYttaaTw0UdqOvH5fMbC46UEsPM0QJarrT5UDlt9y-J5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOK5-FSuLAuchLSGL6hygzpbn68hJSS1Z3J4MXCtlc49xaZjzrGpojZ8BLnaBJsrcsTFOnKvITv0p-zo0Gz66Shasd2RZRGbJQGHZAYg5hSlDUz-pvr_nbBYhgl0utMjkCP7QWXRpKTtZ-gkiNoMRul54i9ioYgNNZQg7-I0QXtN703zqrsHFV_fGOTT-MTUNlKXpiQerOxS9dqEr0T-1B1Lzl1Ls-PazK60a2A5MivHdp6y0cwVEavgqlBSjq9x435OVRE8vFDA-EBqQvy7dy3j4ofAcVn7YXcF0N8klNug0FoL40K1F_I4EdV3J4QQXaCFf5Ld2mNu6tFkOxO1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره
Exploit
با نام
Relapse
برای
Jailbreak
کردن
PS5
منتشر شده که
Firmware
های
7.00
تا
13.60
را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNTc-AyvvfYLgPy-AFVYozUNEcz-2SNsqPVUmYTdNhGhTOUhqmtnxZIsyzUEae0EEoNaBU2q-RTJiCV2irC6yvRybdWQebTqbCPHSwYAKc2og12_p18BP7u6mGeQjhwie0BckX3LP7K77QN0x8QVY2r-RPNBfInFsksbKmAzGIBG5oivZwGrfVDyz5FgFJ-6AEw0PEoOQ59Om-feEnMQIq4jpJ7eD7jcGqOBYBrQ6N0o52p30bYGctIkIArqNWCS7wAgaONQAPJNAbJZIP_oHFmy02DPoW7R_LmTc4JStB8Zv3rxbZizHKo1tSr4JahEWMrGhkdJPUswFSBgDFCIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های زیر
💥
🆓
Opus 5 | Opus 4.8
✅
با این سایت میتونید 100 دلار API برای مدل های بالا دریافت کنید
✅
⚙
پیش‌نیاز ها :
اکانت گیتهاب 1 ساله + یک اکانت دیسکورد
💵
هزینه مدل ها :
ورودی 2 دلار خروجی 10 دلار بابت هر میلیون توکن
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ark322vEK9ZavD2fv4CexW9ytRxdPEERUtJQQJm7K640NNNQ6jmHlcNeEaUfNv7t0GmvSf5RbxdUPPmJi0UaM9PtTRrAfQ-HhOLohgDiYU6u4AwNza3pq7ENu71ZW5DhZfGx6vD1l_k3uvhRbwCnxufLtLq5UlAFxJ0dnH-Nf_DMGfgX3LgF_vjsTPe7J_Qp-n_o9CWuHfCshcTCx5mmeZJPXeYTzAVoPkL7cc12gi9OE7-HIB5IQqWSok7DfK3-tl0m4dLvgerb0Sgeyx3MaRte0g22Z0OWaPEcXseF6mgNmJThNb3P7PspeVWg4fmKFNMqyqfY17dYflPGwezC6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلودر دسکتاپی deviload برای یوتیوب
⠀
‏یه برنامهٔ دسکتاپی که yt-dlp رو پشت یک رابط گرافیکی ساده می‌ذاره و دانلود رو به چند کلیک کم می‌کنه.
⠀
‏
🎬
دانلود ویدیو در MP4/MKV/WebM و صدای MP3 و FLAC با انتخاب کیفیت
‏
📃
پلی‌لیست، زیرنویس، SponsorBlock و تفکیک بر اساس چپترها
‏
📺
ضبط پخش زنده و رصد کانال‌ها برای دانلود خودکار موارد تازه
‏
🎛
ادیتور Devil Cut برای برش، ترنزیشن، سرعت و تغییر نسبت تصویر
‏
🔄
کانورتر با هدف حجم مشخص برای دیسکورد و واتساپ و ایمیل
‏
📱
فرستادن فایل به گوشی با اسکن QR روی شبکهٔ محلی
⠀
‏لاگین یوتیوب و اینستاگرام داخل خود برنامه انجام می‌شه و کوکی‌ها همون‌جا می‌مونه. صف دانلود تا ۸ مورد هم‌زمان می‌گیره و خطاها رو خودش دوباره امتحان می‌کنه.
⠀
‏با Rust و Tauri نوشته شده، yt-dlp و FFmpeg همراهشه، تلمتری نمی‌فرسته و رایگانه. ویندوز نسخهٔ اصلیه و مک و لینوکس هم بیلد دارن.
⠀
‌‏
🐱
مخزن پروژه
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏
🧠
اکوسیستم GLM و راه‌ های رایگان استفاده
⠀
‏مدل GLM 5.3 شرکت
Z.ai
حالا یه اکوسیستم کامل داره از جمله چت، کدنویسی، ایجنت و API
⠀
‏
🧩
روی همون بیس GLM 5.2 سوار شده و همه پیشرفتش از پست‌ ترینینگ اومده
‏ به گفته خود سازنده، بهترین مدل اوپن‌ ویت برای کدنویسی و ۵۰٪ جلوتر از نسخه قبل
‏
🪟
کانتکست تا یک میلیون توکن و ۷۵۳ میلیارد پارامتر
‏
✅
صدرنشین بنچمارک
CyberGym
در کشف آسیب‌پذیری با نمره ۸۴٫۵
‏
💸
قیمت رسمی هر میلیون توکن: ۱٫۴ دلار ورودی و ۴٫۴ دلار خروجی
⠀
‏
⭐️
برای تست بدون هزینه،
NVIDIA
Build
همین مدل رو با کانتکست یک‌میلیونی و endpoint سازگار با OpenAI می‌ده
روی API خود
Z.ai
هم مدل‌های
GLM-4.7 Flash
و
GLM 4.5
Flash
و
GLM 4.6V Flash
همیشه رایگان هستن و وزن‌های خانواده
GLM
روی هاگینگ‌ فیس منتشر می‌شه
💥
⠀
‏
📝
معرفی رسمی GLM 5.3
‏
📊
قیمت‌ها و مدل‌های رایگان
‏
🟢
تست رایگان در NVIDIA Build
‏
📥
وزن‌ها روی هاگینگ‌ فیس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VdzYEeXy91LwX2iE5NwH3AxcLPNQBv5VY8nOOUbVqSTX_3krr4YKkSIGidT_MXYT1YaLVlfA41po0ZqgkfQUY4-6TVGN6LzmUJl7SEJ8YEaWGCBH27KwLcbFTgeCALzu9kwKmpncxCLpWZpUxbcBcy9K7WxPI7FxL_aAZxuTJWeq4Z7G5UeZUPRfgziqOYdJ4fEQbxSs2cg-6ROb3iV0k_kyL2qyrQ0qubJ1T-p73_8sF5C73ceba1C5T6geQXj7zX5iHd2sVfPsD8riCJNuPvXAIlcGgazISLQ2uWc8krSKdKSF8ZpJWwqWQo2A8m_ykFcFh4xmMbUTLym01enQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cV17mXro5wgxdEt9HSNQUlZRO4bIveuS2NNfCm48s-phMrFZsSzwmWlEATxC9XOgVL92o-WAJZDtYLz2NjLXcR7jayI7iYSnE9SYmzy6iwnSn8d7OTEZlqQ41KT3f-rTGg5nGzJP3pq5cUXdhC0MDAWnDI9rK709KaAXNU3zR4VjFcTLkqoktA4UWHSAFuDOiMe_3DfSt-GA4RF1CLwVc7BRFndlI572i8D2nTi6nWukkibe6RNa7lI-jri-KxWHt6vXwbyMPxZ3KnmL_x26EsJb2GSGIvFm2oShPM3Uive06bXDN_ZWHRBToD0k-kFJ92-h0DZQS95OWkLZ7B3giA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsdMroU3EwHbJdSx_tyG1CjQmAPcob-_HkRkOpOCqqxCK52UH9hMPUiQPexcibfbRMPmdjid3BQFEGzI6i1DOQNpmLoI9RF6MciGuaRVCcXLSrKese7Ljd0I7K4ekiqYu-hu9YWK2AFLUDm6tKdYf7HTU6jAEzMcIZQkRH7ELLVGES1CExXg5smjj0UA3NtMwCkhx_fTGkr5MMHSp596YZP6qmAk4jFswVPvi2sVSORrwuGmnxCvVaB1nPb5QfGHGjQxPR3B02plITmDXFibfyY70FnpAlQMqNemJVcE1i_ljFU500ZyrLQ9saGjDsBEx79-wOpyYvN53RQSe0J4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BeboUhlc9kLEg2VQFfYB4GwSKveZFh47U1GB7_7Sm3SkPToJIS2yG-s7H9aLaz20FbNtxQje2iVTJpSXctFPAqZss6MPg0PKc6CynFMXa5gbIFTenYxzBcWulq02GnSbQ-2CBmGKmeKQCDdo-AAbK-psC5ZXF4NgsyxteCurMsMQMkGJxXOWnNKU2gf1H7QwFuDJvkzkr6B3F9RublyDc3N9A9fskvAbqnUiJqm6b5bLl6qTAskj8OFTPxqdoiTBEUphPJmwnRbNcgKkXSC77z5TGdu2TEQc5v3-wG-bf1rSkD1oge-CaEQd3R_syFlc0GyDw6MXm7veUJO2bVWN6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBU5-aPMNIFcNCmvMs09j999sZ1y6V4JwdrTuoAauULpb1UbsFaZwKeZhO_q4T1Gv_DPDAnZ5B9lxt9ekKPcBhYPk3JteQoKe2ZN6Oe1aXW0Q33_cYb13kgH9tsq0vkoQjkdt22VS_DxlnvprYfqEw6oomeo3K9OzpxiGGHcxxpukHPgJtwFB40yyseFFMhe7LlnTg8Tj1vayRssTcibHOr0OvFQUlJaWgLAF8v5rVIun3zjnr_y4qze2koxFPA_X6cKv16_HgJkVrpKROAlGlWHeGCR_OY2zO-tI7RofOPSCi34pcH7TWqQU9uLPTyUlRgPe0KvZGDE7ek0OcsemA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azt61zMiD-tA7S5KuG2Pc1L0lY7OIbtliWXKlTjljm1E8LUWQ7-_-xnPHtL64XFkMr6o8tmPnlQZwcyLc60EqzfWK69FzG_UotIGceYykVrEZZO22fR3a06hrz6juK9y5ARi-Ix7Fk4T1adMzpccNtN0LXLiHoyQoCLC5BcA8WebfRpDsPupMEevZOc7DcItR0T87goG9rMRV2YkqBW754Q3zs0d3uDo8A9F3vf5FsZ9SZ37XG9Jy1pA5EiKjSD1whfSzw-Ahx6sBPanvMr7HMHGqaG9rZ-yBjRB1Br652IqUwfWfbDzr5p1TgyCIcmYCA9Biuzu0nvXA67oQ7JQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJsDvNRhIA23OjNdypOojLsB74OXtAHG4S14TPQciyM86LcT0lVZx7s7gojt4e_9tCMrPsEp3I47lgB_veiy5ZKhjy_VhJH4Xsg2FcJ4RkaAbhlCfp3RAuP6agzHWC5uSMrc6EBOSDDjAWNGttSL-vaSEjcNmR6KQPc21w6T1kS2XysDei3yRc1ta0U0Orrlaee_myOxQc_N9Keuh9rNANUj6FilR9JrzTLXEkRF64fvLaUsCPFpq3JYjn-dAOoGefDLyc4dunA3-NaUdVbO8ZVfyq3Z5yVxTjcaNS0_Lqx391tncDeIeJwz2D2iGUAw_-33VTfBZh0KOlnLoWf41Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkFqcpzkMy9774UdDTJ-jUDwh6k3t8drb9lKsinuLV4A2ECJiY3_E5IABw9c-1jdwshc9vuIY9kqReKaJPUTYnJexAXu8LJ27l-PZjz4tr7i5s5lJh9mUW5R0GIUwFLCbLDo4yU6s2H63-wd3NikuTRLwBUyGRDe-phncLsTFlim9bJjzdM4D5qLIxZtH0kbBVP_ODZ9YC7tBKo5ccrA91OGNO7FoqZDSQrh1h7jjLoxty8ktgOqTqpzIJ5-Je1FhW5yXW__VcOYyoGdQTkj2xUDqyO4wXfr1y88P1cle7WAfFhXxlSrXUHKNMP48hLOQl5XMO0984xak5hHw5iRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLVKAgoPbVQ0AltUKU8sEnM5aEzjOj71sZxcEkNixHkA5yu0VKI4ZVtRqRjXlmKg8k4Uddo-nH70_As-G0qPM5QW8pKOeunLXtYg1oB3vgSi5zfZjuVIGEeGKGIQ37UgA7dPUmdvaZ79loG5vOWIg4GLpd_UXppYKs-bU_s03WemZJJPVH2PLEFvf2BVMwen2uM1ijFV4czbUgViN60hxnItlBuH-7o63AxKz2Wj54J8FkuAuead2hr9fHx9bN9eAlILmPzKUYaJFyrar0ikioATuFR_6TMp-WwIRjCEk994Sr6D-sDFupffQ3wVYitiitsR3-Q7YifoDK0UWN9F6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
ادعای نشت اطلاعات کاربران صرافی والکس
⠀
‏لیک‌فا، سامانهٔ ردیابی نشت اطلاعات ایرانیان، از دیده‌شدن حدود ۷۵۰ هزار رکورد از داده‌های کاربران والکس خبر داده.
⠀
‏
🗂
داده‌ها مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱ عنوان شده
‏
🪪
نام، شماره ملی، تاریخ تولد، تلفن، آدرس، ایمیل و مدارک احراز هویت
‏
🏦
شماره کارت، شبا و مشخصات صاحب حساب
‏
👛
آدرس و موجودی کیف‌پول‌های رمزارزی
‏
🤓
حساب کارکنان و بخشی از داده‌های سامانه‌های داخلی
⠀
‏این مجموعه تو فهرست فروشنده‌های دیتابیس غیرمجاز دیده شده و لیک‌فا می‌گه نمونه‌ای ازش رو بررسی کرده و صحت داده‌ها تأیید شده. والکس تا این لحظه واکنش رسمی نشون نداده.
⠀
‏اگه اون سال‌ها تو والکس حساب داشتید، کارت بانکی قدیمی‌تون رو تعویض کنید، ورود دومرحله‌ای رو روشن نگه دارید و مراقب تماس و پیام و لینک مشکوک باشید.
⠀
‏
🔎
جستجوی نشت اطلاعات خودتون
‏
📝
فهرست نشت‌های ثبت‌شده
‏
🌐
سایت رسمی والکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxJI2OF9XY24Q4UJ9VisHtCQ-g81rZjBRmAkMFwlTp18_cvG1FvFh4cAo2Wywb5RRs-7KSHdEsy0dsQHEEm4Z3F6R5Xnm0JgohhhkAoD8sWpsSVmMQTwuJEgPLItwryBH0YLRH7MwgVcKSmD8vvPPK6_NsOB9ouIxekN8G4p1B4v0j34217lyUXCUXqhpHqFVXfpjwzeShONx3dC-slbeq_9-ndapQdqM_fiMA89nlLaoUtpeAcXcbytcIzSFkSsd1VweCI2tTRYHXjXHQpRPWrUplbiT2NH2B8ln656_YeWI8PkxqucmnoBLlmcf20pxZ54B-2E0SWdYbOMIinokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
اسکرین رکورد با Recordly و ادیت خودکار
⠀
‏یه اسکرین رکوردر دسکتاپ که خودش لحظه‌های مهم رو پیدا می‌کنه و روشون زوم می‌ده.
⠀
‏
💻
نصب روی macOS 14.0+‏، ویندوز 10 نسخهٔ 19041+ و لینوکس با محدودیت
‏
🪄
زوم خودکار از حرکت کرسر، اسموث شدن حرکت، موشن بلور و افکت کلیک
‏
📷
وبکم شناور با تنظیم جا، گردی، سایه و زوم واکنشی
‏
🎛
تایم‌لاین با کات، ناحیهٔ زوم و اسپید، متن و عکس و شکل
‏
📤
اکسپورت MP4 و GIF با کنترل کیفیت و فریم و سایز
‏
🧩
سیستم پلاگین با مارکت جداگانه
⠀
‏بک‌گراند و گرادینت و پدینگ و سایزهای آمادهٔ شبکه‌های اجتماعی هم داره، یعنی ویدیوی آموزشی رو بدون ابزار جانبی تحویل می‌گیری.
⠀⠀
‏
🐙
مخزن اصلی در گیت‌هاب
‏
🌐
سایت رسمی
‏
📥
نسخه‌های آمادهٔ دانلود
‏
🧩
مارکت پلاگین‌ها
⠀
‎
✈️
@ArchiveTel
l</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPR196FOcjvGgZYpuI-8E8wN828j9Tsb0ThviGCqSWeIrgic1GnbOuIJCjjCiKEaVegsiusczHxcODg83qrf9duaV48IuyYkb7OWEdeKMQ2YB5eVANJ8fPI-ePUyZSHMavkNc77DssKyUF5tRGNtVEtQZiknxHUTYqjJqwIyhECNstajKVaEnAR15G8_WHn1y6HfwfVB01_RwpgDFiIh1TUaec0XcJlk1ak2Mc_jxhQvWzekTQ1FmOIE1h639fDgtip-zaIbTSqX2S2AotUtmGpfZR-qXI8LZXm4n2J73BzFdXVWo80mlILwRYvYLR6jOOu8uHLf_upCKrrmHkmM5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به بهترین مدل های جهان برای چت کردن
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این سایت میتونید یک تریال ۵ روزه بگیرید تا با نسخه اصلی این مدل های بسیار قدرتمند در درون سایت چت کنید
✅
این سایت یک ویژگی دیگه هم داره ، شما میتونید با مدل های GPT Image 2.5 Flare و GPT Image 2.5 Sunburst تصویر بسازید
🚀
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=N-km2IV_ONbKUaTmA__vj4g5nPClrcJPiHHKM3rXB-Pj_7ZEIbE-kVNWZKms4szOVNA7QrOuysmv-s7cw5RDRH8FH1Xc9-Qd7iv-tn6P3PIHxH78QBqNmM4DQ5_Ysc4VAAEiOQ8UQIlW-0THlN_t2EWdiL0B1SJifmgggCPU3r1oFifC3oFWoSlHBKMPDUG5-r-zkI_t2qyto4WdBSEdk-me_CPYRmFfmoYszwzpBSBeEGvmQ82aQpwAjRr9HMg23-HAPPEe7j_bdwZ58_TqQEzI9LzzzMniHcTN1MEH3GVjOgscQYfUpguVIMvnHqaYktZNr_50VNZq5EqYU6fnEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=N-km2IV_ONbKUaTmA__vj4g5nPClrcJPiHHKM3rXB-Pj_7ZEIbE-kVNWZKms4szOVNA7QrOuysmv-s7cw5RDRH8FH1Xc9-Qd7iv-tn6P3PIHxH78QBqNmM4DQ5_Ysc4VAAEiOQ8UQIlW-0THlN_t2EWdiL0B1SJifmgggCPU3r1oFifC3oFWoSlHBKMPDUG5-r-zkI_t2qyto4WdBSEdk-me_CPYRmFfmoYszwzpBSBeEGvmQ82aQpwAjRr9HMg23-HAPPEe7j_bdwZ58_TqQEzI9LzzzMniHcTN1MEH3GVjOgscQYfUpguVIMvnHqaYktZNr_50VNZq5EqYU6fnEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
کتابخونهٔ رایگان Melies برای تکنیک‌های سینمایی
یک کتابخونهٔ آنلاین با ۴۲۴ تکنیک سینمایی، از حرکت دوربین تا نورپردازی و رنگ، هر کدوم با پرامپت آماده.
هر تکنیک شامل:
🔍
تعریف ساده
🎭
اثرش روی حس فیلم
🎥
مثال ویدیویی
✍️
پرامپت آماده برای کپی
این مجموعه رایگانه و نیازی به ثبت‌نام نداره، ولی خود سایت Melies یه سرویس ساخت فیلم و ویدیوی هوش مصنوعی هم داره که پولیه.
اگه دنبال اینی که یه حس یا نمای خاص رو توی ذهنت داری ولی نمی‌دونی چطور توصیفش کنی، این کتابخونه دقیقاً برای همینه.
📌
کتابخونهٔ تکنیک‌های سینمایی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMXbJmEQH7cKhHzOzj4jSbCeZlbb9XNrDKWgGf4aW7ce-_AgYKzTWEv2fYIlCyfDFZF5VbZhdCnhYF9lRKDr7BRMioRxueoCYH0tVo83R7nv5j5Ils2rPJCtj9CrpG9zpoRHE5canJofV-g2xY4aqAfWACK85ou1frDQkqjdfR_TbzJ2OQe2H3QlkJBz8SB7D8zej_JlW33NSMF617Hrbk_z7iUQnOgNWqrOZKTSZXjs-fg-x-cFTL3CS_WMTnurRVSRs--BDarmP0coF1odnEORQ5wJ-_YNNipBnVEV6faJ2Mwa_O7o6704oaEiqFmaibyjWKTXDPVySMHL7CWjhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆕
مدل MiniMax M3.1-Flash-Preview بی‌صدا منتشر شد
⠀
‏مینی‌مکس مدل سریع تازه‌اش را فقط داخل MiniMax Code فعال کرده، نه روی API عمومی.
⠀
‏
⚡️
ساخته شده برای کار روزمرهٔ کدنویسی، از رفع باگ سریع تا پیاده‌سازی یک قابلیت کامل
‏
🎛
در انتخاب‌گر مدلِ MiniMax Code کنار M3 و M2.7 نشسته و حالا گزینهٔ پیش‌فرضه
‏
🎁
ورود روزانه ۴۰۰ پوینت می‌ده و روزهای چهارم و هفتم ۱۰۰۰ پوینت؛ یک هفتهٔ کامل ۴۰۰۰ پوینت
‏
⏳
پوینت‌ها ۳۰ روز اعتبار دارن و روی کدنویسی و سند و تصویر و صدا و ویدیو خرج می‌شن
⠀
‏قیمت و سرعت خودِ این مدل رسمی اعلام نشده؛ عدد ۱۰۰ توکن در ثانیه در مستندات برای M3 ثبت شده. روی API عمومی هم M3 با تخفیف دائمی ۵۰ درصد، هر میلیون توکن ورودی ۰.۳۰ و خروجی ۱.۲۰ دلار حساب می‌شه.
⠀
‏به گفتهٔ PANews از ۲۸ سپتامبر تا ۷ اکتبر اعتبار ورود روزانه دو برابر می‌شه و سهمیهٔ Token Plan هم ریست شده.
⠀⠀
‏
🟢
ورود به MiniMax Code
‏
📝
سند پوینت‌ها و اعتبار
‏
💵
تعرفهٔ پرداخت به‌مصرف
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeRHPVueHT98codu5hmu1UN0IZoQ6F_-lU5e7pvcbrv0_BxhZO5wE_L6I__uUQi7yTnvIQQZsi8t1kI0nLDF3vc293_bSgzAjiLznEZaMBU3-rtwqiLOB0m-qA6qtJ3zFYBL3gry-_rqo9k1O6spJJT2SJCADe6f3LxxaO1e3NrOG-_1vePM13xk11_-w_hjc3BfRHUoQkKUY2aYpYnarcKfJ4DE1iWOXmZy2FljaIBzPRsaZmSCtPfYApkjWxmCb8GYYgiOBK69O1w9jiPIWYnwaqHVNPt7f4AI6qs6Nt3JZ86wWGXczyUpiO1twHK9DZ-S62dN52O_xk-Nnyg-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Railway.new
یک VM لینوکسی رایگان در فضای ابری
💻
از حالا railway یک ماشین مجازی لینوکسی به شما ارائه میده که از طریق SSH میتونید بهش وصل بشید
💥
برای استارتش فقط کافیه داخل ترمینال خودتون دستور زیر رو وارد کنید
⌨️
ssh railway.new
⚙
مشخصاتی که این VM در اختیارتون میزاره :
• ۲
هسته پردازشی
• ۲ گیگابایت RAM
• محیط لینوکس
• دسترسی SSH
• Python
• Node.js
• Git و GitHub CLI
• Chromium و Playwright
• Railway CLI
• چندین ابزار AI برای کدنویسی
🤖
بخش جذاب ماجرا چیه ؟
چند
AI Coding Agent
هم از قبل روی محیط آماده شده‌اند؛ بنابراین می‌توانی
Agent
را اجرا کنی، پروژه‌ات رو به اون بدی و داخل همان VM کدنویسی و اجرای پروژه را انجام بدی
⚡️
🌐
برای پروژه‌هایی که اجرا می‌کنی، امکان ایجاد
Preview
آنلاین هم وجود دارد
👎
تنها عیبی که داره :
شما فقط 60 دقیقه فرصت دارید ازش استفاده کنید ، وقتی 60 دقیقه شما تموم میشه به شما 24 ساعت فرصت این رو میده که فایل های که باهاش ساختید رو claim کنید تا در ادامه بتونید ازش استفاده کنید
❕
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfPIHlrOz2Tud4cDZmdRdP0xT1Km1-EZELKCbV1Kb7VNltFHD-LfPNElmuCL4S91Bwk612R131LVVqHN_xPTJeCJ5kDlYt8_5gFgEbFhqPbEEZ0uqVvim2ndsIlYjaHU3xhcLB9GK5oWIEYVO9XCGafHDPF4jv0LWNcvgKgCdJRenEwGy2aChvaiullep4AIYCsJiVXwmxXMcQ_twiMbAX3DGAQC2f-EZ8mjAXeHwW7Ao7feo5kCbV6yODeLac5SRGmDf21uU-Uf0zTn_0p5N2LU7KwmZBjxucGtWyexfpKpGK8HkkHZUY0ZJQYyNSR3aZrIu70oTZo585D3rvRvyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حمایتی
‏
🏔
آرشیو Afsaneha برای افسانه‌های محلی ایران
⠀
‏یک سایت متن‌باز که افسانه‌های شهر و روستای هر کسی را با نام خودش ثبت می‌کنه.
⠀
‏
🗺
نقشهٔ استانی ایران با SVG خالص؛ روی هر استان بزنی افسانه‌هایش میاد
‏
📨
ثبت افسانه بدون حساب گیت‌هاب؛ فرم سایت با Cloudflare Worker خودش Pull Request باز می‌کنه
‏
🗄
هر افسانه یک فایل Markdown در پوشهٔ استان خودشه، پس با رفتن سایت هم آرشیو می‌مونه
‏
🎙
پشتیبانی از فایل صوتی برای روایت با لهجهٔ محلی
‏
📱
نسخهٔ PWA و حالت آفلاین، دو زبانه با چیدمان راست‌چین و چپ‌چین
‏
📖
حالت مطالعهٔ بی‌حاشیه و تم‌های فصلی مثل شب یلدا
⠀
‏فعلاً فقط سه افسانهٔ نمونه از تهران و فارس و کرمانشاه روی سایت هست و نویسندهٔ همه‌شان «نمونه»ست؛ یعنی آرشیو تازه راه افتاده و جای افسانه‌های واقعی خالیه.
⠀
‏
👇
اولین افسانه‌ای که از شهر خودت شنیدی چی بود؟ همینطور شما اسپوف‌نژاد؟
😊
⠀
‏
🌐
سایت افسانه‌ها
‏
📌
فرم ثبت افسانهٔ جدید
‏
🐱
مخزن پروژه در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plryoB7RASbCzQMA5cmNJg4a_uj5mMt60C0bqRpewPT2Oiqq4Dw2kYfUionlnBrSafG9Bu6HYHcRgUSHsLQlOGonCvL6eHMiwnmYUCMGhFbFR6WI4IZgBSYqArq_SOKW7xLZL6gRyVrclOdVgzP51YYndFJZ7SVe_q66ROyA2R7PDnH-eQM8pFVOqJHTvFrhTK9x2blLXj-vRYjShntyWFeQjWzXgCgphGqz3143BhTJ9YqV6CJ1JL1jEGsxRC2NTUxhTjPhIQky_KL2kEJjx4TSf9AJsFMeLXpgG9UXvrje1ATmmzeUo7YsM4xw6xPqTp-G4EBj9jsK7FCA93wUEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API برترین مدل های جهان
💥
Opus 5.5 | Fable 5.1 |  GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 Pro 0813 | Sonnet 5 | Gemini 3.6 Falsh
✅
با این سایت میتونید ۵ میلیون توکن بابت تست مدل های بالا دریافت کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLDg-4OdRlt8Xqz6Wc1lbljEgldAUK2O5tZ-c38K0OMkJldx7BpK-eNQI0AQN3yiwNNghyP3F8mUCmXVbNayNkxiChe4Jxiv8Djp8f3XdaYRT7N3DXc2M3HbXe-lJpDxs-1X_tm-mxLX9jejFizgi9UZcWfruc3DhYQ5P5KJOUWDH1rW_xO1AE1dNGfo2AaHi4bqWkfX-Atqnab4-tdqgntenMiiK8la44g6xSYws1rHkEZSkZ_MSDFNRJHlfu2Xh4J_Msg3xfHcJPopCbLVZp8NTFqIcZlTyvaAXj4UKnTRk1Fd1EmneKUzVqbVO3fxYpyIKtUMHIpQBe3qaT9zLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی زیر
💥
🆓
Opus 5 | Sonnet 5 | GPT 5.5
✅
این سایت بهتون یک پلن تریال ۱۴ روزه حاوی ۲۰۰۰ کریدیت میده تا شما بتونید این مدل هارو استفاده کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_bC-m9tfOfl6SkBZPiOr93aOOZzt6rO0LwBVEwpMEKJGiQXYAmOEybRn1sA0-qOQvYaPEUpD7jrONygY7avpRaDjHSrMfgdqFJZHZ7WMyScxvDC_lxjQRlIEv4VTol_IaYnq0WMYqIrLvOYMxA5eslrkB1bamejdeP5rrIBqtBTpKPORhMXPz1axbTWMT2SxyR8RePbU1iW8l_f1Kk_A97x6U--k9x6hmE2nO0Hg6rkyEGWcORXDZ4av8NqNQDPFiJBuFTu2MnH0X87zZGS1mdPR67Oea5O-FgbSu91w3NLv8PdVbVrZS7-saMp2gIfwb_4lM2EcpCa4KfjvUblDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ادعای نشت اطلاعات JumpJump هنوز تأییدنشده
⠀
تصویر فروش دیتابیس کاربران این فیلترشکن دست به دست شد، ولی هیچ منبع مستقلی پشتش نیست.
⠀
💳
شمارهٔ کارت ۶۰۳۷۹۹۱۲۳۴۵۶۷۸۹۰ آزمون Luhn را رد میکنه
🏦
پیش شمارهٔ ۶۰۳۷۹۹ مال بانک ملیه، ولی زیر شماره اسم Bank Mellat اومده
⠀
آزمون Luhn یک حساب ساده: رقمهای یکی در میان را دو برابر و همه را جمع می‌کنی و جواب کارت واقعی بر ۱۰ بخش‌پذیره؛ اینجا ۷۷ درمیاد، پس شماره ساختار درستی نداره. ساعت ۹:۴۱ و محو بودن دادهها هم نشانهٔ قوی ماکاپ بودنه، نه مدرک قطعی جعل.
⠀
اندیشه معاصر نوشت هیچ منبع مستقلی اصالت دیتابیس را تأیید نکرده و شرکت ادعا را بی اساس خونده. بررسی Tom's Guide هم سابقهٔ نشتی پیدا نکرده، ولی ۴۸ از ۱۰۰ داده: سیاست لاگ مبهم و بدون بررسی امنیتی مستقل.
⠀
پس ترجیحاً از سرویس های بررسی شده استفاده کنید و اطلاعات کارت را داخل فیلترشکن وارد نکنید.
⠀
📌
گزارش اندیشه معاصر دربارهٔ این ادعا
🌐
بررسی Tom's Guide از این فیلترشکن
🏦
جدول پیش شمارهٔ کارت بانکهای ایران
⠀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geMGO0ZPFG-tjCw6g3DVi_6fVT8hJR-na3cPbnvQvXWCjc1GWQ3snq2J0uT0ES2rUEPBEMVwWliLGQJ-bT9JKvTvzN9AYREJJ5aXTwMlxZBsCbs7fvIPHfBW48YC6nTuPhba_bCLTkUQlkWwvwedCSWauD5BmVfGBVI7CHjGBNAUNF5eJY8hJz5IKdTIgoTkPcN9uuvv4ddpuVHrCVwJLz6oXH7BIIlo6zL8xTBF-qNWOLErwwYw3Zodr904uIke1ttwUldi0DALJeEfYP7vQZQngkVMhd18drxAb8HyWwjqHlf5-PQlcdiWLQ7BfwovtNUoOI3DeA5n7OZ5vyMOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های SI در یک بنچمارک سلامت روان، از پزشکان متخصص امتیاز بالاتری گرفتن
‼️
- اپن OpenAI نتایج یک بنچمارک جدید در حوزه سلامت روان منتشر کرده که توی اون، چند مدل پیشرفته هوش مصنوعی تونستن امتیاز بالاتری از پاسخ‌های نوشته‌ شده توسط متخصصان سلامت روان کسب کنن.
🤖
مدل GPT-6 Astra: ۵۷.۳
💠
مدلClaude Opus 5.5: ۵۲.۴
✨
پاسخ متخصصان: ۳۸.۵
- البته جالبه که متخصصان بالینی در واقع جریمه‌های کمتری دریافت کردن. طبق توضیح OpenAI، دلیل پایین‌تر بودن امتیازشون تا حد زیادی این بوده که مثل زمانی که واقعا با یک مراجعه‌کننده روبه‌رو هستن، خیلی کوتاه جواب می‌دادن؛ گاهی حتی فقط با یک سؤال یا یک جمله.
😁
- در مقابل، مدل‌های AI پاسخ‌های مفصل‌تر و کامل‌تری تولید کرده‌اند و همین باعث شده در این بنچمارک امتیاز بالاتری بگیرند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDyYftdpkJJCcUWtGu4dlhbi-FR1d63VS-DWwrV25GUKniNTglc-7pnWVP19Vm1kZVZlfgUmjn-ZRg0iPCf49h-Z-yGve8mrplIRTTWCzgu0gloiY8g-zjO3xpWo9bmmQbDl1XhzcuALevJrsIDWkIXLpchda-oMPRIUKICFXllMJ3RsbMn56fuoVSca9IBF61qEVu4H3JoxH_J0Ol-mc-izqgXalt1ls5bewzE2OrV1PAlncHnivk3R4k4HDJwNaL47hmv0lNm10_TVSM9gXbbanQM3M0uNLrMQv6V1mC6vXAjMisOsUhfhUUDAXebUgJiCH2jm7D2iP6pIvWKdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
مهساNG ویروس نیست — ماجرای اون عکس چیه؟
چند روزه یه عکس از مقالهٔ MVPNalyzer دست‌به‌دست می‌شه و می‌گن «مهساNG ۳ تا از ۵ لایهٔ امنیتی رو رد نکرده». مقاله رو کامل خوندیم؛ اینطور نیست.
اول از همه:
این مقاله اصلاً بدافزار بررسی نکرده. فقط رفتار شبکه‌ای ۲۸۱ تا VPN رایگان گوگل‌پلی رو سنجیده. پس «ویروسه یا نه» اصلاً موضوعش نبوده.
دوم، اون ۳ تا اشتباهه — ۲ تاست:
تو جدول مقاله، «Leak (29)» و «DNS Leak (24)» یه ماژول‌ان؛ دومی زیرمجموعهٔ اولیه. کسی که شمرده، یه ایراد رو دوبار حساب کرده.
واقعیت از ۵ ماژول مقاله:
❌
ترافیک رمزنگاری‌نشده
❌
نشت DNS
✅
نشت ترافیک کاربر — پاکه
✅
قابل‌شناسایی بودن (۱۴۳ اپ گیر کردن) — پاکه
✅
ردیابی و Advertising ID (۷۶ اپ گیر کردن) — پاکه
✅
کانفیگ ناامن OpenVPN (۱۰۷ اپ گیر کردن) — پاکه، چون اصلاً Xray استفاده می‌کنه
یعنی نسبت به بقیهٔ دیتاست، جزو بهتراست نه بدترا.
اون ۲ تا ایراد یعنی چی؟
🔹
نشت DNS: محتوای مرورت رمزنگاری‌شده می‌مونه، ولی ISP می‌بینه چه سایت‌هایی رو باز می‌کنی. برای فیلترشکن ایراد جدیه.
🔹
ترافیک cleartext: مال خودِ اپه (مثلاً گرفتن لوکیشن از
ip-api.com
)، نه ترافیک مرور تو.
یه نکتهٔ مهم:
داده‌ها مال نوامبر ۲۰۲۴ و با تنظیمات پیش‌فرضه. اپ از اون موقع بارها آپدیت شده و نویسنده‌ها هم ایرادها رو به توسعه‌دهنده گزارش دادن.
✅
کاری که باید بکنی:
۱. بعد اتصال،
dnsleaktest.com
رو چک کن؛ نشت داشت، DoH یا Remote DNS رو روشن کن.
۲. سرورها دست آدمای ناشناسه — بانکداری و اکانت حساس روش انجام نده.
۳. خطر واقعی، APK تقلبیه. فقط از گوگل‌پلی یا گیت‌هاب رسمی نصب کن.
💡
و یه حرف با کانالای عزیز: ترسوندن مردم ممبر میاره، ولی اعتبار نمی‌سازه. وقتی یه مقالهٔ علمی رو نخونده تیتر می‌کنی، به همون کاربری ضربه می‌زنی که ادعا داری ازش مراقبت می‌کنی.
اصالت مهم‌تر از ویوئه.
پستتم ریپلای نمیکنم. اینکه خودت اپلیکیشن مود شده خودتو میذاری چنل معلومه چقدر به فکر پرایوسی و ترکر هستی.
📌
فایل کامل مقاله
🌐
صفحهٔ مقاله در NDSS
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zwh5nEALaLyZQmm_OdFG9DEsp2MPWNTiblxh0gKWVmA8DpoyIk4Csty6mOMaRh1rXG9Jd-XFqR79JnI8bvJDRRak9YgEkhLKsvurqHLA9Mb_ZiQplzUMJ0QKZaZwvq-raOo7zJvaQPG9tKocEnywi0jVnDlw4IdQ0_Qej_PFzC8NaXCMk7yQvykSjsayC2tWJCP0O-WwlmSTGIZarxuwL9IoXUQtKnvP0Oi6W3Aua_vBBp107lNs6C3g1NCQWokFRvqL_5bT98zeTgjIB6b0-Vbm2jak1wvWJECu2SgmR_Lxjd4cPguoZ-Njktho4dMmnQT9Q7ID8uQj9I6WOyru6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">500 دلار برای دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این متد میتونید از سایت معرفی شده ۵۰۰ دلار برای ۱ ماه برای تست بسیاری از مدل ها دریافت کنید
✅
📌
دیدن آموزش فعالسازی
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSUklSRxQM6iGuYWHgLtRm2hgxrSkjhv6eEbUkKJYGZT9O_-T7xm-W5iEczPutgLUcbdJSLdOgr-TDpE-kjWSV_tCpYI0b_oYtEdCBefExSrhp5UXyuLSoyHUe4LPpxSpJGjoKTolt73wZtXkJxEKaNCLaOIqPNfRcCxDenK1vx71ECSbhpG3MlGNqDbOqY7LfPE86VeRRYCUJa1v_CHmIJLbgtg3qzCv3Ic8fB8-VVTa-A69lA2sASeQsSPuVQHyaMzzoC8Gy8X0PV3z1zoPi0hpOccmYjtVeG3zTFegYaZePANyvWqAirRxw69TXwfxHc3Bl7e6PSqgVf7lZ0fRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsCL7Fc0qyILfxS7ZEEqhYBOlAOo3TlSFavFt3643Oelb2XVYQ5duLFSte0EGtMchHLMLTQ_HijQcVgGp2-CVDmRJcUe7EU8_Pe-rwWRPdIV2kjmzkYICjJVSmr92UODcFNiZNze9sOF12M4XKjo8tQvVhoacPAPq0x1ncQ7j09x35BfaN2elzq38k_8g6gjjawyfHK6IH0EtNjtGR4_0rjnUViOlN77OQu4GQ7YJu9o-f1uxLEXM9PLRMf8pBDsM0NqH6BGgXJ-ZXnsuco34EF2r6KENAHWQJKNuPDsUS5Z7j1YiwzFP7VqM7iSDEFTZmSmCkz9WZKJz_bhHkBBZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌈
کنترل نور قطعات با FullRGB بدون نصب
برنامهٔ FullRGB نورپردازی قطعات رایانه را با یک فایل اجرایی و بدون دسترسی ادمین کنترل می‌کند.
🤔
۱۲ افکت
: کالیبراسیون جداگانه برای هر زون نوری
🤔
پوشش قطعات
: مادربرد، رم، خنک‌کننده‌ها و فن‌ها
🤔
دوزبانه
: رابط انگلیسی و فارسی
🤔
فقط ویندوز
: نسخه‌ای برای لینوکس یا مک اعلام نشده
💡
نکته
: موتور OpenRGB داخل همان فایل تعبیه شده و نصب جداگانه نمی‌خواهد
📌
صفحهٔ پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJ613Cg1G1PHQWZbmWxIinzkB5kNLOdCGQSI-SizOFT8AS4jnyo9oMxy64DsAAQeg6DvOlKF721-h2l2HWc73Wne1qWTYV_ClktjsZOqOblSK-BehbmR8DrG_cQu0bwD3iljacQs8XI0XS_X5RArFNpNG__Ktqij0z0ztnN8dhNExeRr312DEqT9-_H5nXFPkazaaYO-Pdnnh8ulOXH9fNy2QzPL-Qh-yu0G1lYbqH0FiwK0INNkVE0kt6_IqND6RBwEQyQaFWX_6INfmXaiC19xOTPOzZODHX2gk_uhtnN_l8GXEHKIP1Rv5driL_QS7Xfndbhx2qvnh2WkMay3cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧩
#حمایت
| پچ راست‌چین هوشمند آنتی‌گراویتی؛ خوراک بچه‌های برنامه‌نویس!
‏رفقایی که از آنتی گراویتی استفاده میکنن این ابزار خیلی کارشون رو راه می‌اندازه تا بتونن فارسی رو درست و حسابی و راست‌به‌چپ بنویسن بدون اینکه کدهای انگلیسی‌شون به هم بریزه.
‏•
🧠
هوش مصنوعی دوزبانه: با فرمول نسبت ۷۰ درصدی حروف، متن‌های فارسی رو راست‌چین می‌کنه و کدهای ‌LTR⁩ رو دست‌نزده نگه می‌داره.
‏•
📦
فونت‌های ۱۰۰٪ آفلاین: وزیرمتن، شبنم، ساحل و صمیم به صورت ‌Base64⁩ تعبیه شدن و منتظر اینترنت نمی‌مونن.
‏•
🛡️
امنیت کامل کدها: پنل‌های ادیتور، ترمینال و لاگ‌ها کاملاً سالم و چپ‌به‌چپ باقی می‌مونن.
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7BbI-3A_lFXodVfAK7hhhB8L5ijVjN0IWsdBqb5Ckmrw2_-RfxwSlsEQTD_4_Suf9RjSFyPJ7UO8WnXu8RDJhJ-DbzA0JdA6732yyNMFmx2yTvyboJt4Wq7mqPeVWwR5vqbJ83MspxqLQeaMIzDyp7H7ZpRSzFCwi_ViTKXPdkEM8ZshojYQWOTL9d46aMjE6FXSKJdFrQ9lShpW7j471mykl64nd9vA6wBXdkvWbxioXdIhegrBRrK-hOCIbsbpUF298Fs77m8as1jtzZBMSPsxN85VVVCabOzy0b0R8zI5_56E4D4ZW7KbLvAVCT1l25yz0nUQgM8BNi-TV9zHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoxQw4kx3aCIuRQTN7TY6Jk0x9ebq2yRI5jDbcRPNAqKBxCniXXIHB9BJUZpUNSlXItaob1c_NthDuxwTS5UsicFRUe0DvDwC1gGYk246sRvJas58-dZhTBVD8I299sNBHOTlaIfjSu4H1aMNFrbrS95gaEVhfIrEI2DqWMlmkQ0sDkXxN-vZA550WgtYd6G6P68TJc7tjtWwtunPIQeMWHi3DxyHlgHKH91T6yPnFOlHDrI1cRVdKwMVnMp7I8id5Fc1st2ApqNQtOy10sfmtldzJ63xM5PLkN2BDOB42fHRLzoTa_KfdUA5hBK7ZgFwxSijoRZlZLreX6e8koizg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
در
یافت رایگان ایمیل دانشجویی اسپانیا
با این روش می‌تونید یک
ایمیل دانشجویی اسپانیایی
به‌صورت رایگان دریافت کنید و از اون برای
وریفای برخی سایت‌ها و پلتفرم‌ها
استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell
| METHOD</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
نکته مهم برای کاربرای Antigravity
اگه اکانتی که باهاش کار می‌کنید عضو یک
Family
باشه، حواستون به این موضوع باشه:
لیمیتتون در حالت فمیلی، به‌صورت
اشتراکی
بین تمام اعضا محاسبه می‌شه. به این معنی که اگر فقط یکی از اعضای فمیلی مصرفش پر بشه و لیمیت بخوره، کل اعضای اون فمیلی هم‌زمان لیمیت می‌شن و دسترسی‌شون محدود می‌شه!
💡
پیشنهاد:
برای جلوگیری از این مشکل، حتماً از اکانت‌های مستقل و خارج از فمیلی برای Antigravity استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbxjKePIQU2paPUKCRL704ab0pWiUPgplZQ2dN3nSPDIDdLY-jSBhNRtK0MoSJ0r7vbLM8n29H7YANODQZrMhuy2HXqSmaZYmAf9tWtsI4VOovqm6_ZeocmtUOsoWRnAA3bo4IMZIwWIChPMgPlRdOLwLRGm0HSM5Es7kOsOhRpZFjtMcLct-L8i4ViN45DX3RjB8qzDprPproLn_-DtPt2tngKNqV8dqI5SOfJ4BlW9QXdC_OL-3JRnfOZqMZA-qnZ-Uz9jfNkdD0RYDLNvPGRDolRRLP6nVPMAdA7VhDROJE8lmJWnMWgHdlktjb-VoXDujBN0-zEWizFzTKyb7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
طوفان جدید گوگل، جمینای ۴ به زودی...
💎
کوری کاووکچوغلو، از مدیران ارشد و مغزهای متفکر گوگل دیپ‌مایند، بالاخره سکوت رو شکست و تایم‌لاین اس آی به شدت مورد انتظار
Gemini 4
رو فاش کرد!
🤯
اگه فکر می‌کردید هوش مصنوعی تا الان پیشرفت کرده، کمربندها رو ببندید چون گوگل قراره بازی رو کلاً عوض کنه.
⚡️
چرا این خبر مثل بمب صدا کرده؟
🤔
پرش کوانتومی در منطق:
جمنای ۴ فقط یک آپدیت ساده نیست؛ قراره مرزهای استدلال و پردازش داده‌ها رو به طرز وحشتناکی جابجا کنه.
🤔
تیر خلاص به رقبا:
با این تایم‌لاینی که DeepMind منتشر کرده، گوگل رسماً شمشیر رو برای بقیه غول‌های هوش مصنوعی از رو بسته تا بازار رو کاملاً قبضه کنه.
🤔
یکپارچگی بی‌سابقه:
حدس زده میشه که این نسخه خیلی عمیق‌تر از همیشه با زندگی روزمره و اکوسیستم ابزارهای ما ترکیب بشه.
نانو بنانا ۲.۵
هم احتمالا باش عرضه بشه شایعات میگن
۱ اکتبر
میاد تقریبا یه هفته بعد
👇
به نظرتون Gemini 4 می‌تونه رقباش رو برای همیشه کیش و مات کنه؟ نظرتو تو کامنت‌ها بگو!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRlKHp3nKkdirTo4JlQ9TFZ2miJKNYqJLgdGhWbqBqEXUWprqWyg-CKkP6r74G9POiYI5URYbyAh2PWrD3yEJiPI1-fOjOAsz5fA7ecjqMWuYL37S7dM4aDz24BSs7ISM9fvxMM1llm8SbBmL8-hgwaVOBv9DtgEa2wIuhvU9mkfs3qMIB5W0qeL4atDNDrB0H9EpvvqPePmU2bPjnYVJYVuevW1e2AaGFcPPsFUuNO8ujKpGtCHf3iBdKAt7ECikm9lrjXZGWnkIw2zIpTBngouD5pO-VBDYW9AVPkUK3BIMa5CGgq8daOvfsXOooWae5zNLqn-LmRaqow6AeUfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت
| کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی
به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک
: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
داوری میان گزینه‌ها
: چند راهکار یا مسیر پیشنهادی را می‌سنجد و برنده را می‌گوید
🤔
شکستن حلقهٔ تکرار
: وقتی دستیار یک کار شکست‌خورده را تکرار می‌کند، متوقفش می‌کند
🤔
نیاز به کلید پولی
: هر میلیارد توکن ورودی ۴۲ دلار و نصب با پایتون
💡
نکته
: مجوز MIT برای خود کتابخانه است، نه سرویس پولی TypeSafe پشت آن
این پروژه یکی از ممبر های چنل هستش.
جهت ارسال پروژه هاتون به دایرکت پیام بدید
❤️
📌
سورس پروژه در گیت‌هاب
🌐
راهنمای رسمی فارسی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gaf_f2pedaPGCTuPr7Bi_0Hp_lBUTE4s2pPs6lUhvtxu8ofTCugsAVLdj3AmGprqnT63QgS8CyT3RAsAQcgP9BRPGpHiegIlTKgoirulIIRhs2bo4MtnvZHwDhum92f_GoRWB6WVx-Br6G9mlGL1XgqnI6JgQZq4usWHNfawm8lZ_7WXpo_zgpv-yQyV34QUxCHJDaiKoN2HRW_rJW1znoyW7Q-f0qpb_k-7F-byxIEuoII_bcsIwvYCz9ULvT656PIajZl0AJrxIxeIetT6mlYE-LZ_gUtK--W33WQOEnem6NaMV2oO4PnPY5CkhhfmlOYdFxXa7p4E7j79dVbT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ابزار Perfect Windows 11 برای بهینه‌سازی برگشت‌پذیر ویندوز
با دسترسی مدیر روی ویندوز ۱۱ اجرا می‌شود و از یک منو هر بهینه‌سازی را جدا روشن یا خاموش می‌کنید.
🔺
بستن ردیابی و تبلیغات
: تله‌متری، جمع‌آوری داده و تبلیغات نوار وظیفه خاموش می‌شوند
🔺
پیش‌نمایش پیش از اعمال
: فهرست تغییرها را ببینید، بعد اعمال یا بازگردانی کنید
🔺
پشتیبان‌گیری خودکار
: نقطهٔ بازگردانی ویندوز و نسخهٔ پشتیبان رجیستری ساخته می‌شود
🔺
خاموش‌کردن هایبرنیت
: فضای دیسک آزاد می‌شود ولی راه‌اندازی سریع ویندوز از کار می‌افتد
💡
نکته
: مجوز MIT دارد؛ استفادهٔ تجاری با نگه‌داشتن اعلان حق‌نشر و متن مجوز مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqeWlCOI32oMna_2KNpD_FKaHHZ1k-AUtRwe0XEDp11OvCnkCPAo7LqEfS-e1JB1cSOSsnaIlH4LydbRR6QlzUuL1JTJBGlfWxJHo7GDu02MHMPLDIcbVCRQjMAVdl88Of02Z-cn5NPtWYFTVE5r---difLDZ9PsuD_CPB189fm7nmnf4CDuCse96EeoiMavYT5aC44OmS3sEGjY33Q6AoPwuWp20YGI1jRLCVhszVDzXiOX_bGbhrc8YaMYQS2ijLuhm4qE9ArPOw2Zbw_iumI35rJE38wPi7B4DGscnV9zFqpmne2Ci3kyvg8pO_Q7_cSM1oajmBxYIG1XfEfD9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧮
مدل Laya که به‌جای نوشتن جواب، تصمیم می‌گیرد
یک ایمیل و چند پرسش می‌دهید و برای هرکدام گزینه، نمره یا بله و خیر با احتمال می‌گیرید.
🤔
پاسخ در ۳۳ میلی‌ثانیه
: زمان اندازه‌گیری‌شده برای یک پرسش روی کارت گرافیک
🤔
بیش از ۱۰۰ زبان
: خودش زبان متن را می‌شناسد و مدل مناسب را برمی‌گزیند
🤔
دانلود مدل و اجرای محلی
: بعد از نخستین دانلود، روی دستگاه خودتان کار می‌کند
🤔
نیاز به پایتون ۳٫۱۰ یا بالاتر
: با دستور
pip install laya
نصب می‌شود
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با نگه‌داشتن متن مجوز و اعلان‌ها مجاز است
📌
اجرای زندهٔ نمونه در مرورگر
🌐
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UkSWdjLftut1VJWUHGd2mFtquf8DUwFS_uzkc_NpttlFEjQZvD5ua2CBGKYjXvwMKTm7QRCfrU2f4W9xyPAsY2NeX0sAsiF-5LInBeFJAg9gXLORcNHiHIcd0J-XBWUhchIIq4hHYom6TnY2w04lCjRmNqO7ZKCvxmKLA-dTtInCtfzLDehQqIcOIfwDmWnzjt_n_pld3GfeP--iO5zHv4bKeNAgkHG6HNS1XvRxjYrVfXENQeG9W7RoWqNp60Tz0pqEU7r44Szdd36bsZxLJtU__0YQ9Ifjp_vQTxy5FWnwB0d2dGcs7QB1ca0qzIREZ50j9GNYHGpEMUW_2VwW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3IQSlmV9BzGZQ2hQNEjCYf6aIM5CWrPAMhGbf4lqE6ITfIu0tae17x5_Qtzac5mt12quCxc49BRo6BgAU4TeDmN7lHYLJ6DrzvwyLDkHczOFMTyWOqavVlhKT78YS3MZRpPHbYwuqZ9MMde2a6gS15uLJHzRYs_btrSXGlDZuE8fzlcS0_IFrpXeXnOkH8cc33XBcDrV_pouiflkeI-JkLSuMQYJu1MtPi1EEV4EKOPugGaMXhq9iUBNBmzATn-aWKXDNwtDXhOFPZS37G74kDi_-3q1CrRVGf_OpGN1-hbzfBeClYQjxDOSaD8Z8sgzQUSsoNKPWnMT_YwtIR7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYGr-A5RBi-KUEfyOHZgCDgroHTrSPUHS-izlW88h9tN8_iQGXMbVnvR8amZpk3XsCZFXv6TpzYZFEbZ4zNXXlbcMuURVD3Poqu1kKDZ3Ubw-B5Vzvm2-FpgLB15XR6wvb933saVB7zNPKwTGaQPSLCsI2WZgdjQXl7EHhWSlgxXVwQjzzHxRUoy6oy1NkMNLjkc3Wan5zdgm1v_K_20E0D-lkAjZCJYPXy7P0QtaTkJm1rNyKWA-g05K0YnUSYuBd9Wcye_24UywsGECgUrZ0Y1cWA7CCS3v-keOiyPpPTCHLG474sueJGj_Tjgukz6x13jb3Ej6lFm1HDERguWmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=ehkJF2cl0m8___-prWg3l1tXAKVuj8n1_XdRPsg_DZytODT61iP_-3tO3sz9u_ka9KEvq9DS3s044-0xK-453yrJS2eZJWmINidZ3q0gtUtr_AKtUnTU3n9JDXtVMoP3Ssf_MFNjK7QAmN9DruIL1a_D_hKX7UBVFRe1Z-QwgxtpiL_o-RbszFQYOsCC03O45ajtZFVNS7g7N-Gj-k-qxs9JVc2ULOUvXJRd5vcSrmh0O2JLYvolEp0rduO-1vmX35IfQaoKEzXRZpLEy5vIvNIEbdjMoITKFfC0-zwDTWs4efcZNldboSkGu-aVwzPwl5gKbRs2lqtQaZcxjdk23Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=ehkJF2cl0m8___-prWg3l1tXAKVuj8n1_XdRPsg_DZytODT61iP_-3tO3sz9u_ka9KEvq9DS3s044-0xK-453yrJS2eZJWmINidZ3q0gtUtr_AKtUnTU3n9JDXtVMoP3Ssf_MFNjK7QAmN9DruIL1a_D_hKX7UBVFRe1Z-QwgxtpiL_o-RbszFQYOsCC03O45ajtZFVNS7g7N-Gj-k-qxs9JVc2ULOUvXJRd5vcSrmh0O2JLYvolEp0rduO-1vmX35IfQaoKEzXRZpLEy5vIvNIEbdjMoITKFfC0-zwDTWs4efcZNldboSkGu-aVwzPwl5gKbRs2lqtQaZcxjdk23Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
مدل مخفی Space Bunny Alpha رایگان شد
مدل مخفی Space Bunny Alpha اکنون روی OpenRouter و OpenCode در دسترس است و فعلاً رایگان ارائه می‌شود.
🔺
پنجرهٔ متن تا ۱ میلیون توکن و خروجی حداکثر ۵۲۴ هزار توکن
🔺
پردازش ورودی متن، تصویر و ویدیو با تلاش استدلالی قابل تنظیم
💡
نکته
: رایگان‌بودن این مدل روی OpenCode فقط برای مدتی محدود اعلام شده
📌
صفحهٔ مدل در
OpenRouter
🌐
مستندات رسمی
OpenCode
✈️
@ArchiveTell
#Ai
#هوش_مصنوعی</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci5BC1Qo4Ao3LKwRnn9LUYSLLsXUG-2mbT8Sfgp6WG-e41r98BoJ3U6d0tRWERF_XlzLlRvwylzcBBAOxr1I2LZXDITOXbOhGeEpKSRrTRUMhLEOf_KROeSvXQTaro1PQto6EXauTSUvshSbrQjv123Ao7hq2Ku6mWbKE8mrBo_brypeYMneOTsGH6brW55DEjFkZZa3f0NI8C5e2YaM84HSF3VdWvrRaAjHvGrBB9XnwJ8bY_LYHGB3uH8Ea9MOcDsuDTri0SwIpgI5gNo8akM2JfGgdb9nhG2tPVIkmstmmfQkuQaA77Od_k7HY-Cv7_DcHIMIG_0x8dTZWPRqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWsTE_16MuTStO7dxRgdeu1JW6h4Ugzx1Sz-o7zuZxYTQ2V_L-_FSxhIEVrqnw2h7IpOfLEGOLRwMii22gR_gV4khj9iPRagnda5YiZSlfc60aeCETa2vmANcdkeOfezCpWva7-QSV64e7VZUw_8beYHmd4b31ArXRCXzEllzq6s6bf8WupyvW69ieIQSvYVETYn9pLljOpO8rloo1ejSN4KTqIvwoh_42b7xuNkCYozHACw68M9AB9nbtDd4iSCbKNJCpijSIV-1uvpEU-gQvr2wi3lAhcuuZtUQXwgpiVWE485x9LEfWG6kJfTBNYtD5l_L8fa_Rg9KcpDBx8c-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✈️
نرم‌افزار TeleDrive برای تبدیل تلگرام به فضای ابری شخصی
فایل‌های شما را در یک کانال خصوصی ذخیره می‌کند و ویدیوهای ۲۰ گیگابایتی را یکپارچه نشان می‌دهد.
🔺
پخش مستقیم رسانه
: ویدیو و صدا را بدون نیاز به دانلود کامل پخش می‌کند
🔺
رمزنگاری انتخابی
: نام فایل‌ها، محتوا و پوشه‌ها را با استاندارد AES-256 قفل می‌کند
🔺
همگام‌سازی آفلاین
: فهرست فایل‌ها روی دستگاه می‌ماند تا جست‌وجو بدون اینترنت کار کند
🔺
نیاز به کلید API
: برای اجرا باید شناسه و هش شخصی تلگرامتان را بدهید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با حفظ متن مجوز و اعلان‌ها مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7856" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7854">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY_hT_l0OYvz6UKFh4AqvroCe11yM88Xxu3XLxmCfNEQ_pEUlibSHMNgh1P8fjhVG4ahSR104K8c-jIkxjxQLhWDq3YvhynEf95UdkVBkNm5DqOZCE0qbiJDWOkO-_Ynw5Lp6wzk5k3NQrTYh8MUhz_n9Ks654bUaYkvU26JW823ZevxAS7eRH2jSVmPxyysItKK6CX26kCLW-a7O2tNVxV0d9nbdtpPB4pHH_r7u-lqLWv3uL27wBP-Akf6t7Fsh5K2mQJgxAs2YyMEc8P5T7ZtgA9hsB1oFvgXQ_zVg_L8W6eTOETCavT2G5uqzlZItNtLHSjeLcqzAYdz8c5Y-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=YxD7kR8y8jGC5I4eG1qBa9S5BwrcLpyvkypw6N1NW2QkwiQyGAIQzOmYg8BFshiwOUqza_zDtPEzPV1xh6McEF89ewrm0tbx7odnV5u2XyxyR6QiQ7dfw9SM4BNMtNY5is5ArFHyjLadLxd9-qYLMrSyubmsSfSe8CJVtHB-i5aG-1teXjOHNxKJHbPXqrZOM8DdYN5s1ZceR6Ro3goHLjBSHuerq4R8gn2UUZRDRzft0vGkLu5IjePWbURKw9IF6jpi-0x75YS5S-tCm0CLxd6BUCkv2QLpbeMXeCuiov81e0v9c1eyV0XaHfvdcBCqwrt5jt1KSs6JntWfLLL_uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=YxD7kR8y8jGC5I4eG1qBa9S5BwrcLpyvkypw6N1NW2QkwiQyGAIQzOmYg8BFshiwOUqza_zDtPEzPV1xh6McEF89ewrm0tbx7odnV5u2XyxyR6QiQ7dfw9SM4BNMtNY5is5ArFHyjLadLxd9-qYLMrSyubmsSfSe8CJVtHB-i5aG-1teXjOHNxKJHbPXqrZOM8DdYN5s1ZceR6Ro3goHLjBSHuerq4R8gn2UUZRDRzft0vGkLu5IjePWbURKw9IF6jpi-0x75YS5S-tCm0CLxd6BUCkv2QLpbeMXeCuiov81e0v9c1eyV0XaHfvdcBCqwrt5jt1KSs6JntWfLLL_uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">چند API رایگان LLM که شاید کمتر شنیده باشید
🆓
💥
اگر به دنبال API رایگان برای مدل‌های زبانی هستید، چند گزینه کمترشناخته‌شده وجود دارد که در حال حاضر دسترسی جالبی ارائه می‌دهند.
🚀
🔺
Atria
بعد از ثبت‌نام، 100 میلیون توکن رایگان در اختیار حساب قرار می‌گیرد. مدل Atria-Dawn-Preview با کانتکست 256K و حدود 50 درخواست در دقیقه در دسترس است.
🔺
Routeway
چند مدل رایگان بدون نیاز به شارژ حساب ارائه می‌شود. سهمیه فعلی شامل 5 درخواست در دقیقه و 200 درخواست در روز است.
🔺
Selora
یک پلن رایگان 14 روزه با مدل‌هایی مثل Claude، GPT و Kimi دارد. سقف استفاده 30 درخواست در دقیقه و حداکثر 5 دلار اعتبار در هر 4 ساعت است.
🔺
ShareLLM
120 درخواست در 5 ساعت و 600 درخواست در هفته ارائه می‌کند و مجموعه متنوعی از مدل‌های GPT، Gemini، Kimi، Qwen و... در دسترس است.
🔺
Vireonix
بدون ثبت‌نام و API Key قابل استفاده است. یک route به نام "auto" دارد و طبق محدودیت اعلام‌شده، تا 20 میلیون توکن ورودی در ساعت ارائه می‌کند.
🔺
OdiRouter
مجموعه‌ای از route های "free-*" برای مدل‌هایی مثل Claude، Gemini، Qwen و MiniMax دارد. البته پایداری مدل‌ها یکسان نیست و بعضی مسیرها ممکن است با خطا مواجه شوند.
📌
جمع‌بندی:
برای تست API، پروژه‌های شخصی و ساخت نمونه‌های اولیه، این سرویس‌ها می‌توانند گزینه‌های جالبی باشند. Atria از نظر حجم توکن، ShareLLM از نظر تنوع مدل‌ها و Vireonix از نظر عدم نیاز به ثبت‌نام، ویژگی‌های قابل‌توجهی دارند.
✅
⚠️
سهمیه، مدل‌ها و محدودیت سرویس‌های رایگان ممکن است تغییر کنند؛ بنابراین قبل از استفاده جدی، اطلاعات به‌روز هر سرویس را بررسی کنید.
﻿
✈️
@ArchiveTell
|
#API
#AI</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBzXSUMIqRWahrvE3evV52eHzGvtHihbNldwrgG2ztm5Ugae3kuUMNB5sbIz-Pfe-lxyn94omBTUS1bQRdq1rkLuY5kDbu7x4XYCa-ZIbpmjz0Oh1tCq3ez0vdr-7g4v5lshoZ8onvsEJIEkDQn0aYOKMIbDT3LoDonN219AY7IQbK-EWD5qkRzoNG_ud2bAjO4DDvNav6y9bHEKIH6JRJMoeX0ue8DlqTv6v0kZ0BWeSqSM69TPfomWocuQ_I3cff4JIK-eNN7grVEpha6A7KBEWwctXzznrS37E8W2wXY2YkNm7eJSPfOpQeUHvr-ZGa0_dcidQuzXhE36yiscDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onelAAhyBzgv2px8DnmcisPhSifIg2cCRv8Qj-H8uyN0ey1PBkL-NLhZ_tayOk3dQP8rdEqoqTLKFd3jJoUfyyVPyI2hXwDKtdUb1Tz6PueB-KYDS_d7vW1MXfntik5l4BpmVIa7grvEh_320rOAlqK8SQ6ePzqQtiK1j_EH1WodzlZFKdkdVpvNjiDtf_cGn60YDiEcCmt2tPgnO4F7O-6BSejj1txr-8v2bRDgbWfXdKdNSFRvvxLCg29htbGRkJvIP_H-3u5fzVLV5HG2-PT2pBQnP1IwuUKJmx9JQEIes8elMiz7FbK3g0epBYYGnVepTEzZY-UFrB35cDOIoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tX7m7SVCGuRBmdW0hb_HPab4pvmz-_wQR-o6l4UN5U53UzReD4-J1hLtX7rfKl0ttjaAs2DiEFONZSKbWPfwmb3o0Kx0-ZmPqz4zC7CkA2vD4kTVEJ0D3ccNH6MBavqNtd8vMDQJnDRgCb9PnRTydfd1ME-wSdH1OywN97DaTdyP8Bx8wqEZRcrTzHEgllJiekVFB-OQBwtjRfbiALA-hZZS_4hVQ7UwGx52M_JbwCYMb4Lz94KzUZYFahxUWxzM_DYcknoc2G_LsQ5qbE6YFeYHBknvp8gqMdoyavPZYqHaWK-AlhJYUKv43hJ4-Hivqg-VNpkzTuLwwIBfDi9cKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VsXuKQKqrddCrrMUbT8WAobGBwiRlIO6CPD2YGo-OHV6RbEikCFPccodJqEAnpKgRRu-pjPRooSi8XIMHZASp1EdVRyz_cDCF5nanwsK0AA4yQtOh5fivBiC67efgt5ZRdxpiqjgPJnJg-TAaWB5mSy3aNMXYXdw083KxTuP7SNpXZjdPd4QMUQAFqtU7Om6jDYfiYxGzIDrZ5sukLnFv2rBGmovEi69Q6UQz87K-WhHgeGe1G8FARGVhl_hZ4eMyNGiSxqjWfcT223rDpfQEOQcrF8rSe1xfWMc_fE2h19Kq6MYAKf2HROwyWZZgzZBta5Rq77U6Ib65LUzsNlqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXTAPhKjRMuoBNGpS1kzilGe1PfbY03hlZeEMOwlF89FDXo9QULJTPVw-V2XitRlCCuNDviYB9YNwTz_7_3mwPIG5e7eeDZ5NXLmmSxaNIgHoWca1S0nehSxR744Ot5gSIWeUkUGU04ePx2jSL9GQO-EHRsSqq6EFFLK9J1XkRkCimjFKZ6nquCyF6k4MDk30cgg4cET2DODhxQpeRaEXd8AslKjrnbR1enif3JQR1Zex2vM4H36nQIa_QPCTxKhrBp0eTX46mn8wAjGaZRHpwAugiEpJynzyCDtJHAIUv_-jsGbZkMDn4e8gu0P0bo6m-a5qPLNDaZUpens2B2eoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-l5QNgFDeD6Ocy11Iub4WNtFGbena4XQNLv0Q18O5tA4bnhz9aaKTpEtosgNhEoSIkd4kxTxZAEdzkuQ0DfJxrXq4tdg598BRU-h3eX8Ad_aaCkh3PkirMnVYblu6wkVzxArHCukYYKf7GHvl4MPuU-vxtg0PF8yDoqAVLPjt9QIYS2Gn0tI56clRG9YmJGT7DVTjx1NFgv1Gc5i4zalc2wzVP36sKcFnzSVMlp6VxToB09NFlgc6mM3sswVEweQQGK7kzfWZLfmglpsueOjb20unCbaMKE4QlWA7SdgnU7ef8LMejsSM9ZJSbT7QoX5kVc5eqXLLq-k1Ak3namjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXcPsY4kt73rmETcaOf2djO6VVgS16kE_F0kE98PB8lSuZIZwkcbpcZU8W5CkCA4XwB0myS7dsV24wwrtw5KavvN6sA9ylwAg6nMvNfVn3jUfA1oxKFIVZp8JD7zwao5bl4qAOOlgq3GfzMag_LgRKdjumOFKCkCTUxyDFZbXPo1aiJZtrv_6E3RkOHBi_6H5RYxAoqwJJLMXGtJgX3qXSY0L3Fad2R6hQjV_7VC-DOmaFuBY31Ja0K7Y0gZND0hXNx-YFeUbim75tuOAyDzPiVPpOdno94T_pjKt1jPJ4zovANoLrNtQwgIiWXEfG7eJ1k4kNINrGXURvkZe0PcTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=hd0tuH__FkJyYP5lJddiRNVBYrPIqCrqgNCkyYejLN4sCRxxJcMr0DQeajrAhEGnX7L3EFM23Kd_Z4o3xYF2YB_4Tm9Dz5RyEZKgU8-AJ67JW0vsLybjL4e-2F_FW-zmR5URuKKBa_ls9knX1KqamT8jdy2LAZDdIgB8PxS64WanrYykvf0hEViRIh9q_q2GEn0O2EqoaDSMrokE9QBE3GSKFmkN6e4L25tEnPOcrFzWM5wbFMMRB7rhoJcEPJyFDgUZmeTM2Rv5Uh7dyo9pYLHaXFcImdC5IkK8twX4zOujRjXKH52AW6u85TBietJ9p02ZwWA8NdlARWvkpRu1Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=hd0tuH__FkJyYP5lJddiRNVBYrPIqCrqgNCkyYejLN4sCRxxJcMr0DQeajrAhEGnX7L3EFM23Kd_Z4o3xYF2YB_4Tm9Dz5RyEZKgU8-AJ67JW0vsLybjL4e-2F_FW-zmR5URuKKBa_ls9knX1KqamT8jdy2LAZDdIgB8PxS64WanrYykvf0hEViRIh9q_q2GEn0O2EqoaDSMrokE9QBE3GSKFmkN6e4L25tEnPOcrFzWM5wbFMMRB7rhoJcEPJyFDgUZmeTM2Rv5Uh7dyo9pYLHaXFcImdC5IkK8twX4zOujRjXKH52AW6u85TBietJ9p02ZwWA8NdlARWvkpRu1Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKWBnAZ2HRFP75OHooZIdf95rgjngnwXLxnz7aZDtAEreLhnY-M6TDlvGuc2g_pjmg24CpBSv42L-WScPaO_Ue9j3FeWuHjm0uGuHUVcM-dRuHo55eE3XZWR9M0Twl1_WGdtb79itKSzzz72y1IZ-z5SSrONB_wgmJyeVSfKoToFKSmKXFj67PI-7ZdjekUTvFGkVbf_KvR-v91XzREFvl9BlbEd-b-G5hyQ_B5upA5Hvv6GXVFrKmAMLaAbFwAb9siZifOivijkf5A-C2STA7xBdQVnUkHO95wwOj379XiJL3s1tIdtGL6vl5tEwQW7HbW1Vz0_LnKnXtayU_8SSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود آپوس 5.5 منتشر شد — شرکت Anthropic، مدل پیشرفته خود را عرضه کرد تا با OpenAI رقابت کند.
بر اساس تست‌های انجام شده، این مدل از Fable 5.1 و GPT-6 بهتر عمل می‌کند. همچنین، 20 درصد ارزان‌تر از نسخه قبلی است.
این مدل رو
اینجا
تست کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7826" target="_blank">📅 20:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7824">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXWqtbpcPReBgld6iX9Zihusy-hSeuNptQ5B22FlvNkddcnRIJU0Y9rBUiznbn6RujxUBaRoWwdLzzzCXMkZ28f88JQVjVaGWwqJ9LtImM5kGj11F6PWBKn4zkONou7jNMyLDgZZauqewBrfXVwuyT41p6K_3XV9RNBR23jq6BbUxLq8tx_PRSSGhW6PBhoGv3HWmQLPnyYSuwHwOeBIUyIF2t3ilP-RjVEbIwqOePE_cWLGpgujlvrW9ZboFet8PC1mgpUaApgdPBv724_Ql3Tj6qQIsIayGRuQf31ofvHVbAQZ0HTP5-bDG25wSCtHI9ohCQqq2MoVwVyP0ZORsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
10 میلیارد کلید API رایگان MiniMax M3
👾
📌
مدل‌های موجود:
🤔
MiniMax-M3
🤔
MiniMax-M2.7-highspeed
🤔
MiniMax-M2.5 و مدل‌های پایین‌تر
💎
کلید API:
🆓
sk-cp-jqkYZKrokpSo6XdjlPb7cHA2kZfLdhdZwgtX15DsiwBAbFjb221rKvZtuZvPk0xEy7AaEZnD94ugiuDisZ8U1sLs5qfzCAHog6ti5fjjUsqZprpRqiNzdBg
⭐️
Base URL:
https://api.minimax.io/v1
(سازگار با OpenAI)
🍀
✍️
همچنین با موارد زیر کار می‌کند:
👀
🤔
MiniMax-H3 / H3-Max (ویدیو تا کیفیت 2K)
🤔
speech-2.8-hd / speech-2.8-turbo
🤔
image-01 (تولید و ویرایش تصویر)
⚠️
نکات مهم:
🚩
سهمیه هر 5 ساعت یکبار ریست می‌شود.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7824" target="_blank">📅 15:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7823">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8lqV9kj7ljlowqWOBjKmKxVxwJbxVn4hyPzvAKCWOe2xHCqi9n5IieBy5L_sJnChejgFsEGjeI4K1RN-kqFvwI10CcAIZ5GqpdNm2VOKrptxd9YzidOoWCkd7Ig0gjLaaG34B7BUeiOJKaTO-PssfFgmeZ65w86jpA4hIK5R6LOrfItGaP_bj-3YJJOtX8bmtQK6LIDCa3ptK4V1kyUYznnUWRpjuUaDV0y5zYmsj4kQgVamDofmz878T8hK8q0Bep08PpgOwb2jjL-dIeECQWzzGG-SSYLKZz2KcH95yYoquil7_hd9Lape7tR-GcYqYpJpnwFeZ20WPy4nRY0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙
موتور Agent Executor گوگل برای اجرای انبوه عامل‌های هوشمند
هر عامل مثل یک فرآیند سبک اجرا می‌شود، پس یک مجموعه سرور میلیاردها نشست هم‌زمان را می‌برد.
🔺
خواب و بیداری زیر ۱ ثانیه
: عامل منتظر تأیید انسان، هیچ منبعی مصرف نمی‌کند
🔺
چیدن خودکار محیط
: مخزن کد، سرورهای ابزار MCP و مهارت‌ها را خودش نصب می‌کند
🔺
جعبهٔ ایزوله
: کد ناامن با سقف پردازنده و حافظه و شبکهٔ فهرست‌سفید اجرا می‌شود
🔺
هنوز نسخهٔ آلفا
: روی سرور خودتان با فایل پیکربندی
ax.io/v1alpha1
بالا می‌آید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری مجاز است و اعلان‌ها باید بمانند
📌
سورس و راهنمای شروع در گیت‌هاب
🌐
صفحهٔ رسمی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7823" target="_blank">📅 14:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7822">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_XUmT3w-MUnfrWJvk_Jt7LY9YtfPQq_BEON3g--LwriYFeOv83aDTg3fJZmN6JCQCujAsSB6zpTMfJUUxdFnlp9czBIrVjBDiDiA4iRFE8QfBKNRVhr43jWZA7hGqko9XkC1iVSP0JvGFyIoWLoCNOjpp_b7qwxVJwbK9YxVw6qXRfdkLdD6QHdSvAhokfRSJoH3B0jmO1qxpzRAUjXLDymIJW_EoKGdZqja4ojdvFgBV1cWs4EisIzNtXcv0qDI7s1pD7VN2HDtxRDN8V7Yzhd8hQnEazLyRp2aSegA4ayBHmNxs-e_GrD0dEbKMvsaHKrpB0NDeG6uRKRiubc6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🥹
2 روش برای استفاده رایگان از Grok 4.7
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
Grok Build (رسمی)
نصب Grok Build
ترمینال را باز کنید.
دستور زیر را اجرا کنید:
curl -fsSL x.ai/cli/install.sh | bash
به پوشه پروژه بروید.
دستور grok را تایپ کنید.
وارد شوید و از آن استفاده کنید.
💬
نسخه 4.7 از Grok در Grok Build پشتیبانی می‌شود.
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
2️⃣
XPLabs
به
platform.xplabs.ai
مراجعه کنید.
لیست مدل‌ها را باز کنید.
؛Grok 4.7 Free را پیدا کنید.
آن را انتخاب کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7821" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7818">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBiEMFYciNOoFOf5diD7fkhkiQgnUsCdidN0CFkav0ZKgUZ8FNLQJ61sLfFgA_3ZuF8zvNswnk6Z54-I04cxxIC-siyVNInOMVpAnU9hbqpR9ttrvK5aeLwnRd9_PALpnDGaNSb8UlLPmXC6ZqBtLFS0QPbckdE0GADfS6BoDC7zYuCOpqOPPGFBdtgZy7_NefrP42vYbVpqu7ukGqFMesJIylxFB6-pIq8Up8QkGKdpG63wDZI9QorUwQCvRSujBp-kQ_rT6Fpeh_ctQFQJ3BOyfkn-ZXFET5w9lwL7lHE5Py9grMaAjGyrO4oHdhWCbOQYd-crIxK9BlmaYtYF7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEE2RrIzBILgE2wTKoGeZEHOXyIqawT4h_SLMIBJHEOnCbRpk_vecGlBlKTfLl7-6Qth2UpczGdjgY95VmqglIQZaVvTCSL-MWy11lsaIiJEgrEJIwJxxxAoubw8aBB0wnlyQvLR3MrDxuIGENll7XToQt18ZTy_jkvTe5XTQuV0h3JRK2pjo0jQBaFpzQ79CGpie7Z-gAEKyAKw3Sl5UFuZM8O9tMMUj_bPGk6jk40mXuNqk9QT7ebPwT1vmYClRq5Y03Uqlv3XY64nmEIQssS-P-UtTehalcopTCBB8gVJNknKTfPxFfeR9lb6jPo990d2t_jz71jNVzUHy7hpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FtAGr4lHdQ5sHj4aAWB1QCBUyP6J8jgieUTf1g0jW-IJepnF-pzn0PnQ4yFuaWAxQ6sAnQHCqjfGuDeV2JI1RdaKUI1Th4V2cz7LcrMvN5crVA3d6-0ARtw99VjjNQeihU5h-7NhOV8yqH6cCuJOiUjb9gGFrGHoleBDByT6yv3DX7B1cOTSdhMLpjntW7GOqQxM9G1k1vB_Puv6d1PGQp05ojWjFcRnZafb22Z7bH2V_4XdiuXQg7mjDa7FrFRggba4ej03J-rBUJ-qi1tszMK4_3SGMzPWr1O-tVQkGP2tdCiSU1aNB3q2xnaPjubsvz3_6OzmtJYs16vBCjgnoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
دسترسی رایگان به mimo-v2.6-flash-free
🤔
نام مدل: mimo-v2.6-flash-free
🤔
ارائه دهنده: Xiaomi MiMo از طریق OpenCode Zen
🤔
رایگان برای مدت محدود
🤔
صفحه مدل:
https://mimo.xiaomi.com/mimo-v2-6
🤔
OpenCode Zen:
https://opencode.ai/console
🤔
مستندات:
https://opencode.ai/docs/zen
🤔
برای استفاده از OpenCode CLI:
curl -fsSL https://opencode.ai/install | bash
🔥
تنظیم مدل: mimo-v2.6-flash-free
⚡️
میتونید این مدل رو در
MiMo Studio
تست کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7818" target="_blank">📅 10:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7817">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8osNz2u0q_-lWM7aFPW1MQ0BUtSG_Ug387tRnrz5fBYUutqDPkNzzfsjqVlvhdFG3AmUFd15yILOZkHH8GriTfdCMFKDwtMLylxKc5pv2b7rwRsAZMtbKSQKZP37iK4B6TzPVazeoAOzoMC5xc9AsspzoZ5iu-8RM_Ayi9KxzxQFzpaDL7-8-5CffMQwehPBdV_W4NumsVhgzi_N661VE4kT_r0TZyuk50Uj8tI3GxKEXSkfh4jGfI0lFfzARGQdzlLivmNZoGrqSTNpj8wfeKVDZ-ZfDuA4sw6au695UVRBr6Fj7X-4eGN39oX7Fcr39dZtVQU1hKtFgFzBX7TgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR_lmOb0sSLOHMn_030jp8VTVh3Q2Y20rIHExSHaSnArCMUFWF7yb54EWBRP5iE74oDw7fHYU_Y8Ig4HSozmeYjqPZBmhdVEj_lqFGLz_p2-mJGHHC8RiI5KTtORMEMVodJBY53dMbfL_veNznf05DkuaBmHnS6hM6N2Rw9WjPHbtGvDXJ9um_12kpeqUc0zy80e2_aGtDGniiu5Av6VSDIXoleOR2awCNz65XK9LviqBpS4WHfAtG1hAGP493A4qPGpCPJTu_aFzI4NnRUAIXjdgKrA8dCf-b783KOuSablAjt9NGWVyrNsTToO2RcKxvVjXebBMIaoX8SjtPg6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد   درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7816" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7815">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد
درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در API منتشر کرد. سه نقطه پایانی (endpoint) جدید در کنسول توسعه‌دهندگان ظاهر شدند:
؛ mimo-v2.6-flash، mimo-v2.6-pro و مدل پرچمدار با سرعت بالا mimo-v2.6-pro-ultraspeed.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=pn1ROh0Hdjbajn4kPOHM0dyie3cqBDm9Dqbm-ijz6SLYe2gnev07YluCTqc7yYfMEFhrAPOdBBeHHxLu4dnV5H7XrJKEwYG-wIB_1sU_p0_4JRQcQJ8fyMt2xZ9fUW77DWkPcc8QtedRZPl4U0GjMCV4dq5I9d3HB6ps8bfoJIK90uuQDdiJDlVAOOKlVLXGD4uNN-PEGWLcEPsIqJhtpkMWkF6FZtwgOPOe0lCJ6xoxbjCjasYitBCMqQEQ9CXs_l8ZqSjRRjvuDRjM0DKFakxB2LOwTqUKJ2DcKrefK477M1Q5t3_FNiXao4tUGSKnZIay604V1lG3MPr98AT3xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=pn1ROh0Hdjbajn4kPOHM0dyie3cqBDm9Dqbm-ijz6SLYe2gnev07YluCTqc7yYfMEFhrAPOdBBeHHxLu4dnV5H7XrJKEwYG-wIB_1sU_p0_4JRQcQJ8fyMt2xZ9fUW77DWkPcc8QtedRZPl4U0GjMCV4dq5I9d3HB6ps8bfoJIK90uuQDdiJDlVAOOKlVLXGD4uNN-PEGWLcEPsIqJhtpkMWkF6FZtwgOPOe0lCJ6xoxbjCjasYitBCMqQEQ9CXs_l8ZqSjRRjvuDRjM0DKFakxB2LOwTqUKJ2DcKrefK477M1Q5t3_FNiXao4tUGSKnZIay604V1lG3MPr98AT3xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7813">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.  یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7813" target="_blank">📅 22:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7811">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⚡️
یک خبر خوب برای طرفداران VS Code و GitHub Copilot!
اکستنشن
🔀
Router Models منتشر شد!
با این اکستنشن می‌تونید مدل‌های مختلف AI و Providerهای
OpenAI-compatible
رو مستقیماً داخل
Copilot Chat
استفاده کنید؛ از OpenRouter و Ollama گرفته تا APIهای شخصی و مدل‌های Local.
🤯
🔥
قابلیت‌هایی مثل:
🤔
مدیریت چند API Key و Failover
🤔
تشخیص و فیلتر مدل‌های رایگان
🤔
پشتیبانی از VS Code Settings Sync
🤔
؛Import تنظیمات 9router / OmniRouter
🤔
ذخیره امن API Keyها در Secure Storage
با دادن
🌟
دلگرمی بدید.
🔗
GitHub:
https://github.com/web-elite/router-models
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7811" target="_blank">📅 22:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7810">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqUY3HCrggaKCvU94fIJp4jxlepbF5WioJxAOkjkOPYocNqiiiqaeD91_2tQxy9AuKSh2RaTLuQ0dDMn-b2qogm6TFZcU46kkuWsdnT5GRCZfDltbfa7FUvAkiy3z_Qzt93riw8VOab2UInoP0BmUe-BAPfTWuKLSxGS4oDOgUW4uW8gO_eY3jBhQtK3OTnO65g_yaE0PofkPgNAuJrfCjb4mxJcXaSMmfzRLVvCA3fpeM5lF2KxNqRIbtdSEYGo5jEVpIVfAgNT0JzlDPbExq_Y6lDVDMNoPdtKJOKCP1AQP3HhlXElVTT4Z2sP8dUUuBYmaH8p9sVf7CAut_3tEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥹
نسخه 4.7 از Grok منتشر شد — قدرتمندترین نسخه Grok
🤔
پیشرفت چشمگیری نسبت به نسخه 4.6 در تمام جنبه‌ها
🤔
عملکرد عالی در حفظ متن‌های طولانی، کار با کد و اسناد
🤔
مهم‌ترین نکته: قیمت بسیار مناسب — قیمت همان نسخه 4.6 است.
🤔
با توجه به پیشرفت‌های چشمگیر، نسخه 4.8 از Grok به زودی منتشر خواهد شد.
🤔
برای
تست
اینجا کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7810" target="_blank">📅 20:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7809">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CV14DxyCUPWaME-WrBQ0aikq4vNRm3q3aP1f3ZCtyRWKLkVNnHuRxzUwVrkgCfVYcmT9dxibArT3J1MCpB31_DIxduIgBEeqt9NHKL-1TJHoGSSF5dzJRExTz9zj4UJ0x4AjI2LMuo2z10-NT7oPGVGXJqPc8cEWaC2L0bEZXJ0YnC8uRznwIlMGXG7ISyEpbA8ENZ2xSoS1iXh9aD8gLq1JOLfpDW-nvJTQp0hhJuFXf8ixHfEVBygBfpd2R_sPpnNvvzo0D8dGHpUxfYgcoD82pYKNNIfw5SY3nv-NuvPbi042n82cU9N5Rb0s-t88YHovEyqhBinjBBjb4J-WdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
500 میلیون توکن GLM 5.3 Flash
؛AutoClaw دوباره توکن توزیع می‌کند، این بار به طور همزمان 500 میلیون توکن در دو روز
21 سپتامبر: 200 میلیون
22 سپتامبر: 300 میلیون دیگر
درون آن، GLM 5.3 Flash، Deepseek V4.1-Flash و V4-Pro وجود دارد.
🤔
دانلود
AutoClaw
و ورود به سیستم را انجام دهید.
🤔
بخش Credits را باز کنید و روی Redeem کلیک کنید.
🤔
روی Claim کلیک کنید.
⌨️
انجام شد! حالا ما نیم میلیارد توکن داریم! مهم این است که آن‌ها را در طول روز خرج کنید، زیرا در پایان کمپین (23 سپتامبر) از بین می‌روند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7809" target="_blank">📅 19:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7808">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdQsEelCQFZNZNG3CQ-tjlHOOyMzEvvwWMq_EyssgdScS0H1a2wUNtFTTZkSudwUWCTdNXuJebpwqgYSwClO_YROpMcWtmqYneqO6FCHL36B1D0mwYSTXZU57JCpurLxA_Z_lcrUMdrhDifq8WQypFy3Ez1vODWYsTXs41tuzb85fAvzFfD7pCPep79QtbjdlwT5nZ46CiKMu7kDWtyeLs7R7OaVJVN5-CNqhchWi3d9bhuc28r2zu-2d_okDPBlt-nG48a1Cz8MDpTLQXBLj5-2yTemCUKXxNYYUSBHJdO8J3YtFGpiRsohp0Kvq35M4FgP0jaJl06RT-mrZAlLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
مرورگر Sigma؛ ایجنت هوش مصنوعی داخل خود مرورگر
مرورگر Sigma روی Chromium ساخته شده و ایجنتی داره که به‌جای شما توی صفحه کلیک می‌کنه، فرم پر می‌کنه و کار رو تا آخر می‌بره. هدف رو توصیف می‌کنی، خودش مرحله‌ها رو جلو می‌بره.
🔒
مدل محلی Eclipse داخل مرورگر اجرا می‌شه؛ طبق ادعای سایت، پرامپت‌ها روی همون دستگاه پردازش می‌شن و آفلاین هم کار می‌کنه
🧪
حالت Deep Research برای جمع‌کردن منابع و خروجی ساختاریافته، به‌علاوهٔ چت با هر صفحه و ترجمهٔ سریع متن انتخابی
🗂
ادبلاک داخلی، تشخیص فیشینگ، رمزنگاری سرتاسری و پشتیبانی از افزونه‌های معمول
⚡
در بنچمارک Speedometer 3.0 روی مک‌بوک پرو M4، سازنده مدعیه ۱٫۱۳ برابر سریع‌تر از کروم و ۱٫۳۰ برابر سریع‌تر از سافاری بوده
💡
نکته:
نسخهٔ فعلی برای مک و ویندوز (149.0.7827.117) و همچنین iOS و اندروید موجوده؛ نسخهٔ لینوکس هنوز منتشر نشده. بنچمارک‌ها هم تست خود شرکته، نه مستقل.
📌
دانلود
🌐
سایت رسمی
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7808" target="_blank">📅 18:46 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
