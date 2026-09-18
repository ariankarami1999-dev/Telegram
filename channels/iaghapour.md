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
<img src="https://cdn4.telesco.pe/file/hczexlfraoCLnNVOKmrsjiN2xQhXzubvuqy96zL-k7oqLDBhkgKh5Nf-gKoukak4sUc5_hdIlY9hsocmNQeYR-H_ADbcbzvc88zHpErnF9s1ck29XvNPly6hdqPpj1R3Xn7xoeskxtPEK2LP_HsFMzTFtAZH7T6w6x8ogzwgJHt-FYS-c8X--CuE84DlmYgcPfGsPD8jJpwT15n2aX2vkVM0tEPLFpUvS1aFk2OqJP_I7xypu9Xpa86Bf7X0f8eudsMCDH0zIEoeA54EINiYqxJV4Flz-dbkNg2AAHfTO1zPJ0Scomx2cUbI9cO4cVIfAaxY7i6stxs-Qy19XyEQDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.7K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 05:52:39</div>
<hr>

<div class="tg-post" id="msg-3025">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوب داده</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmTl3ZxVxUmgMHAK9a4FdOUowj9eWLivBZI9sEyD0ywxU1goTAKXCg1i_fQ1WGagZWX_7bKNOPqbfTJ9jcF9nopPH5EYoDHrXl3D5EWaug6HSDuPlb_lOCYHFP_CgqWLL0260sUNQzEd9mamERGqClUiUwYgV3OCnyCIGYRk0G2JzAsTDbL0z6bFk_-lRKlfvL7LNpGdF-PktznI-jprNM4JYCiwDNmMJY4C-afoU8vXCFy5H1A__NA2aR6ah7f_VOfY-mKT_l5_s2amjy9sLVEmUWpuix4mfx0hr3QGXQ6Rf8rx_jTC3a6SVjbilmFimmGpXgH6gUhbO2NRZgUbDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
شبکه سرور فقط عددی در مشخصات دیتاسنتر نیست.
در زیرساخت G11 وب‌داده، روی خود سرور از اتصال فیزیکی 50Gbps استفاده می‌کنیم؛ برای ظرفیت بالاتر در انتقال داده و سرویس‌های پرترافیک.
🔥
⚡️
سرور مجازی ایران G11 وب‌داده
🔹
‏ HPE DL380 Gen11
🔹
‏ Xeon Platinum 8580
🔹
‏ DDR5 5600 Enterprise
🔹
‏ Samsung PM1653 Enterprise SSD
🔹
پورت فیزیکی 50Gbps
🔹
تحویل آنی
💠
۷ روز ضمانت بازگشت وجه در صورت عدم تطابق مشخصات
شروع از ۱٬۹۰۰٬۰۰۰ تومان ماهانه
🛒
سرعت واقعی زیرساخت را ببین:
https://webdade.com/ir-g11-port-50gbps
📞
0313740
🌐
webdade.com
#سرور_مجازی
#سرور_مجازی_ایران
#VPS
#وب_داده</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/iaghapour/3025" target="_blank">📅 22:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3024">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAhoku84pml1plWV1uJdJbLzWGrFYGWFOJUJthxQIIU3Z2VW3DOdc_58ms6WmFtPPIhK24jtXdGLQ25jZVp-pSu5I9OHCxggqG9C8hHs6A7WSiGd_JyhYuq9Paq2FTqjutZict7NWCcYrOEmZ4aLEzzYQuiMmGXTqqfFax4Bx63vVvsb2_Yr3C3i9U04_vVk2i_u6L52Kzd2iJYJjIj68jZhsTNvY7hjQ6Dc8a0eEZYFzp4ZYnjWouMhPr1mwbSJkebmA3uF3CdVdExVl6VNQGoE_uYs031yMo7NbhERMroY-dC4SiSiVcFPT8dSA-RiW0HQ5_Fy0Zx0gGHAzTvZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دانلود فایل ایزو ویندوز اورجینال از سرور‌های مایکروسافت (با ۱ کلیک)
🔹
اگه از نصب ویندوزهای دستکاری شده و پر از باگ خسته شدید این ویدیو دقیقاً برای شماست. تو این آموزش، ۲ روش فوق‌العاده ساده و سریع رو بررسی می‌کنیم تا بتونید با ۱ کلیک، فایل ISO ویندوز اورجینال (ویندوز ۱۰ و ۱۱) رو از سرورهای خود مایکروسافت دانلود کنید.
🔗
تماشا ویدیو در یوتیوب
⚡️
دسترسی به تمام مدل‌های هوش مصنوعی فقط با یک API
👈
لینک سایت
||
آدرس کانال
#آموزش
#ویندوز
#اورجینال
#windows
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/iaghapour/3024" target="_blank">📅 17:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3023">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRiIk7a5KbXsMgogru-TueKgJYM4x8PNY42HSJ3WdLFBA3p8rA7EpzIFRVlhOZQLKauig95Lz9yxafvNeO8trpDq_FXwqFjzFbW0yncIXP9AcPBDBoeXvBaAe1xzcfscOZxaXQQ-6TFN7wsajfI4ownYnr4KPS7h3umFx23qaJ1giQUdF7ZGfAVsuYvpYfhHFGbTmmN0yzS-YHOeMKudBC0UpnIv8kj0jbaAhY3K2EeCvmo7V-NTzTOflvKfs2w0DQBnoN8P0nkTGoO0EYdr12diDwGKgVRlcgBGzrT4dc8PV7ZMvYiAunSuo57p4sNqxTH5Fu3byxP2maJ_HZh-0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
کرکر سرسخت دنوو با وجود شکایت قضایی دست از کار نمی‌کشد!
با وجود فشارهای حقوقی و تلاش شرکت توسعه‌دهنده نرم‌افزار ضد دستکاری
Denuvo
برای شناسایی و توقف فعالیت کرکر ناشناس، او اعلام کرده به دور زدن قفل بازی‌های ویدیویی ادامه می‌دهد.
🔹
شکستن قفل‌های پیچیده:
قفل دنوو سال‌هاست به‌عنوان سرسخت‌ترین لایه حفاظتی بازی‌های ویدیویی شناخته می‌شود و دور زدن آن مهارت بالایی می‌طلبد.
🔸
شروع درگیری قضایی:
کرکری با نام مستعار
voices38
توانست پس از حدود یک ماه و نیم قفل بازی
Resident Evil Requiem
را بشکند؛ اقدامی که خشم دنوو را برانگیخت و باعث آغاز پیگیری‌های قانونی برای فاش‌کردن هویت واقعی او شد.
🔹
پیام جسورانه در ردیت:
با وجود تشکیل پرونده قضایی و تلاش برای شناسایی او، این هکر با انتشار پیامی در ردیت به کاربران اطمینان داد: «همه‌چیز مرتب است و تمام کارها طبق روال عادی ادامه خواهد یافت.»
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/iaghapour/3023" target="_blank">📅 16:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3022">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad Hasan</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLm_Yp32tqj-C8m6rYoctO34DD2L9IQ58wt3_WTXzHKUhbA8m3htiYE6gqndlTqIXf2lcNbZUXp8ICrQFIldBq8lJ-TFh1I8TKA_WdN9npdMOKiIda_fO0YenkW6FpUFjmOaPwD1XyteeYHVFlB6cei8pOfCaZzsgN3iT7iSLP-AsrF1ILH90VemNfjFBnQAlwHeQFKzxm1PBr4KoFd09TLkxZ5puRHgez3r8eutwHZMGJXWeoRJVdJGH_2I5rwFV1wHWqgCXPTRbnJMGh8kkEabBS8lpFYFBupMtYw0yg0bC9bNTQexvtSN1dqDdIMQMOAhgI66vzrm8k6Am2visQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
فروش ویژه اشتراک‌های هوش مصنوعی
🤖
✔️
فعال‌سازی سریع و مطمئن انواع اشتراک‌های پریمیوم:
🤖
ChatGPT Plus / Pro / Go
🤖
Gemini AI Pro
🤖
Super Grok
😵
Cursor Pro
🤶
Claude Pro / Max
👻
Kiro Ai Pro
⭐
Telegram Premium
⏱
فعال‌سازی سریع
🛡
همراه با ضمانت و پشتیبانی
🛍
جهت خرید همین الان ربات مارو استارت کن و خریدت را انجام بده.
💸
@SubMarketAi_bot
📢
Channel:
@SubMarket_IR</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/iaghapour/3022" target="_blank">📅 21:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یه مدته زیادی رفتیم تو فاز شبکه و ساخت فیلترشکن و این داستانا :)
گفتم یکم تنوع بدیم و بریم سراغ ویدیو‌های متفاوت‌تر؛ از اونایی که اتفاقاً خودتونم خیلی پیگیرش بودید و درخواست داده بودید.
فردا یه نمونه‌شو براتون می‌ذارم، ببینید چطوره.
😉</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/iaghapour/3021" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1MgVCsz0CE6GU2x-4HhlQdDxou0h4Xqu8HGHKigflLJLpzcNXiYuTFB6qSwnsNK2NpDJwGprBhvI3u3Vnuu8QCkziLwy0ynciz4zf6r3dONTuxMBJ04cvNp6Y3esu6RDNm9mWbA8jfPowXzGhrUylaPwtSbJMfvj2jqUsNguI6K82TQ5_TUZJ3H3fQBOwu3_uRnykhDkwNLxfAlt4nv10yQHMVfI68jXjxJU691CXkX8eAt86vxXqmDzcKPDr8DZ5EHvlu3JfI_kUJUq_BaGvHje-Y_NjOiIJXOZQtdBa0_vaJbmVuPVF3DqWN9xwGwowK2WFVaondqWVtodvXXSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Screenbox؛ پلیر مدرن، سبک و جایگزین شیک VLC برای ویندوز
اگر پلیر پیش‌فرض ویندوز نیازهایتان را برطرف نمی‌کند و از طرف دیگر ظاهر قدیمی، شلوغ و منوهای تو در توی VLC کلافتان کرده، برنامه متن‌باز
Screenbox
دقیقاً همان گزینه‌ای است که دنبالش هستید؛ پلیری با موتور پخش قدرتمند VLC اما با رابط کاربری کاملاً مدرن و هماهنگ با طراحی ویندوز ۱۱.
🔹
موتور پخش قدرتمند LibVLCSharp:
اجرای روان تمام فرمت‌های صوتی و تصویری رایج، پشتیبانی دقیق از انواع زیرنویس‌ها و هماهنگی کامل با موتور اصلی VLC.
🔸
طراحی بومی و مینیمال ویندوز ۱۱:
رابط کاربری مدرن، شفاف و چشم‌نواز بدون گزینه‌های اضافی و سردرگم‌کننده.
🔹
بهبود کیفیت تصویر (Upscaling):
قابلیت ارتقاء وضوح ویدیوها در محیطی با تنظیمات ساده، سرراست و قابل‌فهم.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/iaghapour/3020" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsSWvXHHG75WlgzNq3ajUMvATu0NwBkg9mBhP9kExHYWdHU24yjJlkt9nKyNzvy7wxCQOPxK1-ph4BlY2oAfuR4qMrdRHoCx9Ti2LfpqHyAHDZzAP8fnapfAv3dUZuCTKEmQnbaejMov5hji51FJK5L3YlQbvaxrYIdae_yy7kmCJF3j3XiVHJB0tsFu_H2E0NZRZl0AUhI_mAzNiMakqw6OqIl6w3Urb719MkJ_M1o_6WpqNgCL8hw9sEAYyijxS2CiPEOoEYq7BI99fHZjH_2K_nOW8gFIc_oq-dEWfBvEjmQbLkfOxZj3HItKbzRcmcCrZIZSfk0SEnlaYC280w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام تعطیلی رسمی صرافی کوینکس (CoinEx) پس از ۹ سال
صرافی شناخته‌شده
کوینکس (CoinEx)
که از سال ۲۰۱۷ فعال بود و به‌دلیل عدم اجبار احراز هویت (KYC) در سال‌های گذشته یکی از اصلی‌ترین مقاصد کاربران ایرانی به‌شمار می‌رفت، رسماً اعلام کرد که فعالیت خود را متوقف کرده و تا
۱ دی ۱۴۰۵ (۲۲ دسامبر ۲۰۲۶)
به‌طور کامل بسته خواهد شد.
⚙️
زمان‌بندی مراحل تعطیلی صرافی:
🔹
۲۴ شهریور (۱۵ سپتامبر):
توقف ثبت‌نام کاربران جدید و انتقال بخش معاملات فیوچرز به حالت Reduce-Only (فقط بستن پوزیشن‌ها).
🔸
۳۱ شهریور (۲۲ سپتامبر):
توقف کامل معاملات فیوچرز، استیکینگ، وام‌دهی (Lending) و بخش واریز اکثر ارزها به صرافی.
🔹
۷ مهر (۲۹ سپتامبر):
توقف معاملات اسپات (Spot) و بازخرید توکن CET با نرخ ثابت ۰.۰۰۵ تتر.
⚠️
نکته بسیار مهم:
صرافی اعلام کرده رمزارزهای غیر از تتر را ترجیحاً تا قبل از ۷ مهر خارج کنید؛ پس از این تاریخ ممکن است دارایی‌های غیرتتری به تتر تبدیل شده یا رمزارزهای کم‌حجم پشتیبانی نشوند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/iaghapour/3019" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9K8t6IX3PsNPDrjBjHzqWOXazl1aTUa7zzOOgNQOGXQ7fjqgtXW3BHOnpZX8GMPPFq4wcr7L-DhMHGOmBx_-wxUiChaBLWmZ6a-NpXbJwF9NC3Z-mLmcEABAUUbxGMR0h--pdDvTGNx20adqW8XKhh7t98ULEYxFh4IQ5Gm2jAG4lu9J6br4mf6Qeu2OGvs_EAnhTu_uNohzdWIi1TFkTMoyULZVgUaLt3VUSqlZM7FY5TQVSfbq81Y3e6uGZc0eT4zOZts6KSl9rYn0R_tuIesslXIryEglvuOWxqzBadlpBvT-OSWunzxyan8mbTJHokQLIVO47R5tsrb6zOINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Subify؛ افزونه هوشمند ترجمه و دوبله زنده ویدیوها به فارسی
سرویس
Subify
یک ابزار کاربردی و مدرن برای مشاهده ویدیوها با زیرنویس دقیق فارسی و حتی دوبله صوتی هم‌زمان است که بدون نیاز به دانلود فایل جداگانه و با استفاده از API شخصی هوش مصنوعی کار می‌کند.
🔹
ترجمه آنی و بدون تاخیر:
استخراج مستقیم کپشن‌های زمان‌بندی‌شده یوتیوب و ترجمه پیش‌دستانه (Pre-fetch) با سینک زمانی میلی‌ثانیه‌ای بدون معطلی.
🔸
دوبله زنده صوتی
: دوبله هم‌زمان صدا بر بستر مدل‌های جمنای، با امکان تنظیم بلندی صدا، کاهش صدای اصلی ویدیو (Audio Ducking)، انتخاب گوینده و تنظیم سرعت.
🔹
پشتیبانی از مدل‌های AI متنوع:
اتصال به کلیدهای API شخصی در Google Gemini ،OpenRouter و OpenAI به‌همراه سیستم فال‌بک (Chunked) هنگام قطعی مسیر لایو.
🔸
شخصی‌سازی و فونت‌های فارسی:
تنظیم کامل فونت، سایز و استایل زیرنویس با فونت‌های جذاب وزیرمتن، استعداد و لاله‌زار به‌همراه پیش‌نمایش لحظه‌ای.
🔹
استخراج لغات کاربردی از دل ویدیو و امکان مرور کلمات به‌صورت فلش‌کارت در حافظه محلی مرورگر.
🔗
دانلود
افزونه برای انواع مرورگر
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/iaghapour/3018" target="_blank">📅 14:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3016">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cC8Ne0q9SVAoRfKcZMhWtb2U4_dQP6wUV-mTeAgK-nNZInfGNFBTBeB5msl-yi3vbGsf_YkrwOhdRLHB31MroT89f81F9oURaAxdmiukt7QLBpbcqIKcRVT6augL5Ub6zrJAu5hRd8rtEZk-q4NC_N3-UH1tL3mD0TLuVP_yAfV9eq2Q5rf6BRplTSstUUHfXVepaFmA-7rpMtH4y1EbUbdC_lDgQlLe8uIi8XYhVxfIdpUlRGeXui6N19r5D1tP6r3U8E03FUrXmvagD3MPDwo_yfCRlhZOz3R51hcZi73h9a2agmR9nG7xjyqqZVH3kr0qN46tKftRtfRARibHmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل سبک Zefira؛ مدیریت هم‌زمان چندین پروتکل
پنل
Zefira
یک ابزار پایتونی سریع و کم‌حجم (مبتنی بر FastAPI و SQLite) برای راه‌اندازی و مدیریت اکانت‌های VPN است که بدون درگیر شدن با Docker، امکان ارائه چندین پروتکل را در قالب یک لینک اشتراک واحد فراهم می‌کند.
🔸
پشتیبانی از پروتکل‌های اصلی:
پشتیبانی از VLESS (همراه با REALITY و چرخش خودکار SNI)، هسیتریا ۲، تروجان، VMess، شادوساکس، WireGuard و OpenVPN
🔹
لینک سابسکریپشن یکپارچه:
ارائه همه کانفیگ‌ها در یک لینک با خروجی‌های Base64 و فرمت Clash YAML
🔀
مدیریت تانل:
تسهیل ارتباط سرورهای ایران و خارج به‌همراه بررسی وضعیت اتصال نود ایران.
👥
کنترل دقیق اکانت‌ها:
تعیین حجم، تاریخ انقضا، لیمیت دستگاه، فعال‌سازی با اولین اتصال و تایید دو مرحله‌ای (2FA).
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/iaghapour/3016" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3015">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=Ytb2bLjgEVM_aDPrRkQPp2D2EifOCCrkGMF5tOwbQmLCRkHNvEe-i16_omPh43GCjfihv56zl7f5kL94ejLo5n4gMnUoi9dH6GJwznOlC4MyB8-FtaD3q3rxOsj5m-Qj4Lnl9c5Lp4aqTNyE-MHOHeRYUf3Pa5OJCWTeSqBrvLFupngpxFTzuttA5r1TEDR8M7ZTKpofzCQNgEAsYan_zfRkdUM10r0THvP1OyRJYoK2hXbwdrUDqeAzjOpCqPyheca_6oyllSF5t4d4RO15VWDv6NtHeBxtR3HMmAK9FfCcsZW_yD5TyjrYIJtvDWcWpRpgxgn3tczIPZU-LtFw3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=Ytb2bLjgEVM_aDPrRkQPp2D2EifOCCrkGMF5tOwbQmLCRkHNvEe-i16_omPh43GCjfihv56zl7f5kL94ejLo5n4gMnUoi9dH6GJwznOlC4MyB8-FtaD3q3rxOsj5m-Qj4Lnl9c5Lp4aqTNyE-MHOHeRYUf3Pa5OJCWTeSqBrvLFupngpxFTzuttA5r1TEDR8M7ZTKpofzCQNgEAsYan_zfRkdUM10r0THvP1OyRJYoK2hXbwdrUDqeAzjOpCqPyheca_6oyllSF5t4d4RO15VWDv6NtHeBxtR3HMmAK9FfCcsZW_yD5TyjrYIJtvDWcWpRpgxgn3tczIPZU-LtFw3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی (دوره یازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mahdi9226، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/iaghapour/3015" target="_blank">📅 20:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3014">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgRFoiiiyz_JvyhKFT4rlgW68K6mi4RabBIEQjaSYd7fsZvkXTzJ5M-QKe336qwFTWlqGWlre0pXGNidPXnptzFsSSpUs0aRE4giWDqlX5pIXsQ8oQX3iL6vYg4tVLy5Ze720hfrFGGWri9nfN2XnYrThADJQ-D79Nksq-q8K4z7C2p5LF_rey0MSnL36_E3o50KRVGZ3rLmlYC6IU4bGH-WKCqp33IPG2ywgh3mmh7u4ufku0iFNSuU7ZTni_yEKzCQfPDE0FwNmwOGtFL_CcRByLu70EnqYH4yB44wTBMnX1iR87TwtcnzD4WMs7S-N9K_1azolaKOdE_xzQkcGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی DNS Changer؛ ابزار مدیریت و تغییر سریع DNS برای تمام پلتفرم‌ها
اگر برای گیمینگ، عبور از تحریم‌ها یا افزایش امنیت مدام در حال تغییر DNS هستید، برنامه
DNS Changer
یک ابزار رایگان و کراس‌پلتفرم است که این کار را با یک کلیک و بدون نیاز به دستکاری تنظیمات شبکه سیستم‌عامل انجام می‌دهد.
⚡️
پشتیبانی از بیش از ۳۰۰۰ سرور DNS:
دسترسی به دیتابیس عظیم ارائه‌دهندگان معتبر جهانی به‌همراه تست پینگ لحظه‌ای.
🛠
شخصی‌سازی کامل:
امکان افزودن، ذخیره و دسته‌بندی DNSهای اختصاصی برای استفاده مجدد.
🖥
پشتیبانی از همه سیستم‌عامل‌ها:
دارای نسخه اختصاصی برای اندروید، ویندوز، لینوکس، مک و محیط خط فرمان.
🔗
دانلود برای پلتفرم‌های مختلف
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/iaghapour/3014" target="_blank">📅 17:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3012">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚀
نصب خودکار و یک‌کلیکی اسکریپت‌ها در پنل دوپراکس!
🔹
دوستان عزیز، همونطور که در ویدیوی آموزشی مشاهده می‌کنید، پنل دوپراکس (Doprax) یک قابلیت فوق‌العاده جذاب در بخش
مارکت
داره که کار شما رو برای راه‌اندازی سرویس‌ها بی‌نهایت ساده کرده!
🔸
دیگه نیازی به درگیری با کدهای پیچیده، ترمینال و تنظیمات طولانی نیست؛ فقط با چند تا کلیک ساده می‌تونید هر اسکریپتی که نیاز دارید (مثل پنل معروف 3x-ui) رو در کمترین زمان روی سرورتون نصب کنید.
📝
مراحل نصب خودکار:
1️⃣
ورود به مارکت:
از منوی پنل، وارد بخش مارکت (App Market) بشید.
2️⃣
انتخاب اسکریپت:
از بین برنامه‌های موجود، اسکریپت دلخواهتون (مثلاً
3x-ui
) رو انتخاب کنید.
3️⃣
انتخاب سرور:
سروری که از قبل تو پنل ساختید و آماده کردید رو به عنوان مقصد مشخص کنید.
4️⃣
نصب با یک کلیک:
در نهایت فقط کافیه دکمه
Install
رو بزنید!
✅
نتیجه:
سیستم به صورت کاملاً خودکار تمام کارهای لازم رو انجام میده و اسکریپت رو روی سرور شما نصب می‌کنه و اطلاعات ورود رو در اختیار شما قرار میده.
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/iaghapour/3012" target="_blank">📅 20:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp1XDz-gfab2WL4jcSQxiBS6m_JyPtQpCu0yNYLeUXk56ux-euRDK1E7vKwKm3X1Rh1PV5ZQDDBwXZZZ0oKhrp0g8nI9tM84eYN8h1RSXy3s-yggqgOHuyGxLBShAnEP1qiO189TK_G_VvwqZlh7sf4KUBzbVXUjg_V0oZx7OdxrmOHysiF17JkRVopMgVuucJLmaxndt1gpICvmdGmm_lyfu7G0xsamnvI-pn-whrp3qISP0uXHXsLnAV9vTdrnifJdq_ylW1IizS49vc_VO1c7B8OiCsudl_t6BQkXtedsy8I13MG__qn7M9T1anr1ABfNhpJyRbGQiXxwcsLu3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل idontScanner | جعبه‌ابزار تست شبکه و TLS روی VPS
اگر مدیر سرور هستید یا می‌خواهید کیفیت اتصال، اختلالات شبکه و وضعیت پروتکل‌های امنیتی سرورتان را دقیق رصد کنید، پروژه متن‌باز
idontScanner
یک ابزار سبک، سلف‌هاستد و سریع برای همین کار است.
🔹
کالبدشکافی دقیق TLS & SNI:
تفکیک دقیق زمان‌های DNS ،TCP و TLS Handshake به‌همراه نمایش جزئیات گواهی SSL، نسخه پروتکل، Cipher و ALPN.
🔸
بررسی در دسترس بودن Endpoint برای لینک‌های VLESS ،VMess ،Trojan ،Shadowsocks ،Hysteria2 و WireGuard (بدون ذخیره افشای کلیدها و UUID).
🔹
سنجش لتنسی، جیتر و پاسخ‌دهی پلتفرم‌هایی مثل YouTube ،Instagram و Telegram مستقیماً از مبدا سرور.
🔸
دارای رابط کاربری روان به همراه منوی مدیریتی تحت ترمینال برای تغییر پورت، مشاهده لاگ‌ها، اتصال ربات تلگرام و آپدیت بدون از دست رفتن داده‌ها.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/iaghapour/3011" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H31Dc2tmmNM_vb1gdzdMKDY5BtWmk15--zPfmfU3aAPTqWTOD4n3QrlZ3TjHUFLc2BLEzu68ExFvD7RC6QmlFUm0Ki4l-pEpVAglxlEoXObKZZhQu6v3zNRCeq-_YGxsS9Lug_JlFP5zPEvSTjBWJPz9iKLvbA_kLLKhSXVDyjQ0AvcfjXXKYh0iPZS3YeYgoU05jEw-dRfbpd7aFJMFtK2OcwyDAMyGsbsSfs0TmaKdEXXwaorxG1YkCf9V7xC3IRu2xWFmBRsOG3suPrZn4GZmSxLQ0WfWvhQ1oYYJUQl19mvaRdxmkVhCTekINZ3bjeX3KUapSxYXgUIZWBl3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
اعتراف مدیرعامل زیرساخت: ۱۰ درصد ترافیک اینترنت کشور به استارلینک کوچ کرد؛ سهم 5G تقریباً صفر!
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، در نشست خبری خود از واقعیتی پرده برداشت که نشان‌دهنده شکست سیاست‌های محدودسازی اینترنت است: حدود ۱۰ درصد کل ترافیک کشور اکنون روی بستر اینترنت ماهواره‌ای استارلینک جابه‌جا می‌شود.
🔹
سهم ۱ ترابیت‌برثانیه‌ای استارلینک:
اکبری اعلام کرد با وجود بازگشت ۹۰ درصدی ترافیک، ۱۰ درصد باقی‌مانده دیگر به شبکه داخلی بازنگشته و جذب مسیرهای ماهواره‌ای غیررسمی شده است؛ حجمی که حتی از کل ترافیک برخی اپراتورهای داخلی فراتر است!
🔸
تداوم فعالیت ترمینال‌ها:
به گفته وی، استفاده از استارلینک به‌ویژه در دوران تنش‌ها و محدودیت‌ها جهش پیدا کرده و ترمینال‌های فعال‌شده همچنان آنلاین و در حال سرویس‌دهی باقی مانده‌اند.
🔹
سهم ۵G نزدیک به صفر:
در شرایطی که میانگین جهانی مصرف دیتا روی نسل پنجم به ۵۰ درصد رسیده، سهم ترافیک 5G در ایران تقریباً روی عدد صفر قفل شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/iaghapour/3010" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3009">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uELEcaMSpqb6b8VHN_5QPLQQeZ4zGNG0Dk1nEcRewhf1KGnqMjM-lWq5E8EAxNH2SA3EIEL9LjHErQAY7PK7r03tmGfqGvKIkxTGdwUmJG08kaDhYJh3rjzrwFalVAcrQcvqIwSuesUJ6UpxENwUrXYU2_-5cM9pIyYouFavCQ73L1JsTVGc0HN1LZYmnoGxH8k0ENlzLmOi4iYgnnoXTzxq71-XhLjgHUXPw7jO9f_96yMVY4zCM13eTcBfy7R3MkZIJfv4MASc_gVxTyRfyBhcl3f_k-C0-zjPLMTmdK7-Qo6J3frS8AkdYjt9K1T3eOhCo4jebXZhKs8Ron_Uuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رفع محدودیت‌های ترافیک IPv6 در کشور
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، پس از تذکر اخیر وزیر ارتباطات اعلام کرد که محدودیت‌های اعمال‌شده روی پروتکل
IPv6
برداشته شده و اپراتورها از امروز هیچ منعی برای استفاده از آن ندارند.
⚙️
جزئیات و نکات کلیدی خبر:
🔹
۹ ماه مسدودسازی بی‌دلیل:
ترافیک IPv6 که نقش مستقیمی در کاهش تاخیر (Latency)، پایداری شبکه و افزایش سرعت ارتباطات دارد، از دی‌ماه ۱۴۰۴ تا امروز دچار مسدودسازی و اختلال گسترده بود؛ محدودیتی که حتی خود وزارت ارتباطات هم مدعی است مصوبه قانونی مشخصی برای آن وجود نداشته است!
🔸
وضعیت ترافیک در کلودفلر رادار:
با وجود اعلام رسمی شرکت زیرساخت، داده‌های لحظه‌ای
Cloudflare Radar
هنوز تغییر محسوسی نشان نمی‌دهد و سهم ترافیک IPv6 ایران همچنان روی رقم ناچیز ۷ الی ۸ درصد ثابت مانده است. انتظار می‌رود در روزهای آینده با بازگشایی شبکه اپراتورها این سهم افزایش یابد.//شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3009" target="_blank">📅 14:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmR5RFM0A-7BrGCKYoZmYphMGKQCr_HBAhGzGvtQDVFSM2DnqlX3pGhGTP6o50nh206RXes-2MdQMzt7lx_WDJMDgHP40AB2IgBSgGR5vhHw9aQmLYraACqKrb43Hil9BHnUhz1nSCDt_JOyBHlAnM-p_epeUn_V4SslY7DHZ178qBDlL4OpSEFs0TB0MvCm9TcKyA7YcXK2-4eey6B1MjRgaXXn0CLDz0aD5ETUxDlKQ4C1baWd1dRlFyqwjhR2cFmKETECogPSj4fZg3UDeu0F53_Of0XGo8_mm8aHgO3j0FsRCe5FIRvem_-iJbEwSB_WeU1-X1h_3_8uZXENag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی + پنل مدیریت و فروش «مشابه شکن»
🔹
تو این آموزش قدم‌به‌قدم بهتون یاد می‌دم چطور یک سرویس رفع تحریم اختصاصی (شبیه به سایت معروف شکن) بسازید و با استفاده از یک پنل مدیریت حرفه‌ای، کاربران رو کنترل کنید، اکانت بسازید و به راحتی فروش داشته باشید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#شکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/3007" target="_blank">📅 18:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شنیدم خیلی‌هاتون دنبال ساخت یک سرویس تحریم‌شکن اختصاصی (شبیه «شکن» یا «الکترو») هستید که حتی بشه ازش درآمدزایی کرد و اکانت فروخت؟
😎
یه تحریم‌شکن که گیمرها بتونن با پینگ خوب و بدون دردسر تحریم بازی‌ها رو دور بزنن! درسته؟ :)
منتظر ویدیو باشید!</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3006" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">💬
راهنمای خرید سرور از هاستینگ هایی که معرفی میشه
رفقا سلام.
بعد از
هم‌فکری با شما
و بررسی نظرات خریدارها و فروشنده‌های عزیز، به یه جمع‌بندی نهایی رسیدیم. برای اینکه هیچ سوءتفاهمی پیش نیاد و همه چی کاملاً شفاف باشه، رعایت این موارد میتونه بسیار مفید باشه. این موارد قانون نیستن بلکه یک راهنما هستن برای اینکه شما با آگاهی کامل بتونید خرید کنید.
🔹
۱. ملاک قطعی سلامت آی‌پی:
تنها معیار سالم بودن سرور در زمان تحویل، موفق بودن تست پینگ و
باز بودن پورت SSH
از طریق سایت
Check Host
هستش، نه تست بین ده‌ها اپراتور کشور که هر کدوم فیلترینگ داخلی و محدودیت‌های خودشون رو دارن.
🔸
۲. داستان اپراتورها و فیلترینگ:
اگه سرور تو چک هاست اوکیه ولی روی نت شما (مثلاً ایرانسل) جواب نمیده یا بعد از چند روز آی‌پی مسدود میشه، این موضوع به خاطر فایروال‌ها هستش، نه خرابی سرورِ فروشنده.
🔹
۳. تعویض آی‌پی:
وقتی سرور با Check Host سالم تحویل داده شد، در صورت فیلتر شدن آی‌پی بعد از تحویلِ موفق (بعد از چند ساعت تا چند روز)، فروشنده تعهدی برای تعویض رایگان نداره و این ریسک در شرایط فعلی اینترنت پای خریداره.
🔸
۴. ارتباط سرور ایران به خارج:
سرورهای ایرانی که تهیه می‌کنید، باید ارتباط باز و بدون محدودیت با خارج (ترافیک بین‌الملل) داشته باشن.
🔹
۵. وضعیت پهنای باند و ترافیک:
فروشنده موظفه کاملاً شفاف بهتون اعلام کنه که پهنای باند سرور
«اختصاصی»
هستش یا
«اشتراکی»
. همچنین سقف دقیق مصرف منصفانه برای سرویس‌های اصطلاحاً "نامحدود" باید مشخص باشه.
🔸
۶. مرز پشتیبانی:
وظیفه هاستینگ تحویل سرور خامِ سالم با شبکه متصل هستش. نصب پنل، کانفیگ، ران کردن اسکریپت و رفع خطاهای نرم‌افزاری سمت سرور، به عهده خودتونه.
🟢
و اما یه نکته دوستانه و مهم:
— بچه‌ها، ما تو این کانال همیشه فیلترهای سخت‌گیرانه‌ای داشتیم و
فقط هاستینگ‌هایی رو معرفی می‌کنیم که دارای نماد اعتماد (اینماد) و سابقه مشخص هستن
. هدف ما ایجاد یه پل ارتباطی امن برای شماست. با این حال، وظیفه ما صرفاً «معرفی» هستش و صفر تا صد توافقات خرید و پشتیبانی، بین شما و فروشنده انجام میشه.
—
یادتون باشه هر هاستینگی ممکنه قوانین و شرایط فروش اختصاصی خودش رو داشته باشه که لزوماً صد در صد با موارد کلیِ بالا هم‌راستا نباشه.
پس حتماً قبل از نهایی کردن خرید، قوانین خود اون سایت رو مطالعه کنید و با آگاهی کامل خریدتون رو انجام بدید.
— چنانچه خدای نکرده مشکلی هم پیش اومد که نتونستید با فروشنده به توافق برسید، می‌تونید از طریق همون نماد اعتماد به صورت رسمی و قانونی شکایتتون رو ثبت و پیگیری کنید. این مسائل از دست و مسئولیت کانال ما خارجه.
🔻
امکان آپدیت در روزهای آینده وجود داره!
دمتون گرم که با آگاهی کامل خرید می‌کنید!
🌹</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/3004" target="_blank">📅 20:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3003">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPYdWRB1CxWu640VfAEZveKjSSLFZfHBE7dHRtVtRCkPkP3WqDJON71QARSy1cjLKKgkkucSVCCBl5WrtHTJfLYlf9RwwJtbQIMWXWQUJqMiqojFxU0r5_HA0ZudNUaWT0dXLf17JMos668iyqQVjrzxGs0MQ7-UE1z4ldp3wg-ZKJRRqrxv6x2ozOtmnY15qL_60uqScE87GB_2586m_sg60PqV6tV-OvB30U2rmc8eAYGN0yRPppftOpzcyJqEIS5LzSiubP92zbcKA3csEmAaMuC9ItQVt4nQfubqcPWjGuNpAvciCacWgmHuv6OcD_JEWOqY4w6jjt0egF_lMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دستور وزیر ارتباطات برای بررسی و رفع محدودیت‌های پروتکل IPv6
ستار هاشمی، وزیر ارتباطات، در جلسه شورای راهبری شبکه ملی اطلاعات خواستار تعیین تکلیف سریع و رفع محدودیت‌های اعمال‌شده روی پروتکل
IPv6
شد.
🔹
نبود توجیه قانونی برای محدودیت IPv6:
وزیر ارتباطات تأکید کرد اگر مصوبه قانونی برای محدودیت پروتکل IPv6 وجود ندارد، اعمال محدودیت فنی روی آن هیچ دلیلی ندارد و موضوع باید فوراً رفع شود.
🔸
همگام‌سازی شبکه با استانداردهای جهانی:
هاشمی اعلام کرد شبکه ملی نباید در تقابل با فناوری‌های روز دنیا باشد و مهاجرت به استانداردهای بین‌المللی مثل IPv6 از الزامات توسعه زیرساخت است.
🔹
پایان نگاه دستوری به فناوری:
وی با اشاره به شکست پروژه‌های دستوری مثل جستجوگرهای بومی، تأکید کرد فناوری با دستور پیش نمی‌رود و سامانه‌ها باید توجیه اقتصادی و رقابتی داشته باشند.
پ.ن: سال‌هاست به بهانه اختلال در سیستم‌های فیلترینگ و رصد ترافیک، پیاده‌سازی کامل IPv6 رو توی کشور معطل نگه داشتن و شبکه رو از استانداردهای جهانی عقب انداختن!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/3003" target="_blank">📅 18:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3002">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPw7RId9cGkKdn8WUhE8HANBsyXeC6_3lYnCB6UQgUUqDX5SRBU9k4y2D52W2SM3792hAYU8TDwp9kAn_UuOk1tJnBarwv4C17xACVoZ2B1UFK4dfsyCSGRacsb0_pzbcht-iT18GOc6aIF_0XtDR2aGcESmyL_uEf-f279LNS5IJMLU_Kc-_5se5JAzV9mLOEdmjsfpKkJZnEEoYvu_sldwEu4baRlNPy_9VfK0jnjz3uVxqoxeWM8Q8IrIWAkd1LzxADjSsyuzpiJSTJj0BPzgb_Li3iJPRecDj3WivPbMiFXW4O4dqoqs0jGK5ehZ8J1RIOzFlv0U06prznBRyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی اوپن‌ای‌آی از ChatGPT Sites؛ طراحی و انتشار وب‌سایت تنها با پرامپت متنی
شرکت OpenAI قابلیت جدید
ChatGPT Sites
را به‌صورت بتای عمومی عرضه کرد؛ ابزاری که امکان تولید، ویرایش و میزبانی مستقیم وب‌سایت‌ها و وب‌اپلیکیشن‌های سبک را صرفاً بر اساس توضیحات متنی زبان طبیعی فراهم می‌کند.
💬
طراحی پرامپت‌محور (Sites@):
ساخت رابط‌های کاربری چندصفحه‌ای، داشبوردها، پورتال‌های درون‌سازمانی و ابزارهای تعاملی با ارسال متن، فایل‌ها و دیتاست‌ها
🚀
میزبانی و هاستینگ رایگان:
میزبانی خودکار وب‌سایت روی زیرساخت OpenAI، تولید لینک اختصاصی با قابلیت تعیین سطح دسترسی (خصوصی، سازمانی یا عمومی بدون نیاز به لاگین)
🧩
المان‌های تعاملی و شبه‌وب‌اپ:
پیاده‌سازی فرم‌ها، فیلترها، سیستم جست‌وجو، جداول داینامیک، نمودارها و سیستم احراز هویت اولیه
👥
همکاری تیمی (Collaboration):
امکان کار اشتراکی روی پروژه، اعمال تغییرات و به‌روزرسانی نسخه‌های منتشرشده با اعضای فضای کاری
📊
دسترسی:
دسترسی برای اکانت‌های Business، Enterprise، Pro، Pro Lite و Edu فعال شده و عرضه تدریجی آن برای کاربران پلن Plus نیز آغاز شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/3002" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SETmy0_Yu_7QBhPwSZBEJRzDEzNfUMB2njLcZizF5AqB3k4XspXByRJ_E-MRhGw3kQGRmgcCYztS1VN3qRdk0VuB-eBuKLNxGZs0DxBN5SX0xNoU2h7IpRTH6nGTjXl3u7kwuZHLb9Aioi4Z-0tD4jGrdt_efog7uSghcUUzHEm5auLr8eFqQo2F-y_DFV-uTFZ2ojZSZ1WpEqWvLnl-JmFrBjgmkpIOOenTxQQlrPKR9TbS7GXJrZ34hpjAPE8Wk4zZeaGwglHCVdqKF-bt8CIJoW8fwvzaHWpR2ZEApmJln6YAXpRV2usj1cZofvAjxFYfyde15SOthfEc5qGRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
بکاپ خودکار از پنل‌های V2Ray و تحویل مستقیم در تلگرام با ابزار bkup
ابزار
bkup
یک سرویس سبک برای سرور است که در فواصل زمانی مشخص از دیتابیس پنل‌ها فول‌بکاپ می‌گیرد و فایل خروجی را مستقیماً به تلگرام می‌فرستد.
🔄
پشتیبانی از ۴ پنل:
اتصال به پنل‌های 3x-ui، HM Panel، PasarGuard و Rebecca با دکمه تست آنلاین اتصال.
📤
تحویل خودکار در تلگرام:
ارسال مستقیم فایل بکاپ به چت یا کانال بدون نیاز به دانلود دستی از سرور.
⏱️
زمان‌بندی دقیق:
تعیین فاصله بکاپ‌گیری بر حسب ثانیه، اجرا در قالب سرویس Systemd و فعال ماندن پس از ری‌بوت سرور.
🧩
ابزار Reassemble:
قابلیت چسباندن پارت‌های چندتکه بکاپ‌های حجیم ارسالی تلگرام در پنل وب و ساخت فایل کامل
💻
مدیریت وب و ترمینال:
دارای داشبورد گرافیکی با لاگ زنده، به‌همراه منوی ترمینالی برای آپدیت، حذف و تغییر پورت یا پسورد.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/iaghapour/3000" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=TUxqnQqVRrZV-KfDsvWT5-KoAjFBdy-EBGNerqV91j8uKoDB_Xk_ORT7Zu8HWWs8EIXcvWA8MIDLCz-fv5nuhNEu9yTv-1N9xqifkcChgI2n1oBJyzU18aXBVPpt0NJlEtxtB7LqnMT8tmYqdJm0HnNN2_KPID1Z0tjy3TiB_kv0b4g16XcN4NBOQHMhiOZtPXL09gcQSZFJwc9IwOfTAWD1wFLTKXfIzedrmJrXD9pAXS4wg9wRPlDjXYkT9kbdlUho9ixvMhGhdJmvGvEIiLV4eNlFLBB7oEZFrk7KuhPVllUknLx4twsdpGGYhxq7fcgmWBRDIFV9dpa_y4mDYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=TUxqnQqVRrZV-KfDsvWT5-KoAjFBdy-EBGNerqV91j8uKoDB_Xk_ORT7Zu8HWWs8EIXcvWA8MIDLCz-fv5nuhNEu9yTv-1N9xqifkcChgI2n1oBJyzU18aXBVPpt0NJlEtxtB7LqnMT8tmYqdJm0HnNN2_KPID1Z0tjy3TiB_kv0b4g16XcN4NBOQHMhiOZtPXL09gcQSZFJwc9IwOfTAWD1wFLTKXfIzedrmJrXD9pAXS4wg9wRPlDjXYkT9kbdlUho9ixvMhGhdJmvGvEIiLV4eNlFLBB7oEZFrk7KuhPVllUknLx4twsdpGGYhxq7fcgmWBRDIFV9dpa_y4mDYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی اوپن‌ای‌آی از ChatGPT Images 2.5؛ تبدیل اسکچ ساده به تصاویر واقع‌گرایانه
اوپن‌ای‌آی نسخه جدید مدل تولید تصویر خود را با نام
Images 2.5
معرفی کرد؛ مدلی با نورپردازی طبیعی‌تر، بافت‌های غنی‌تر و بهبود چشمگیر در وفاداری به تصاویر مرجع و ویرایش‌های متوالی.
⚙️
امکانات و ویژگی‌های جدید:
✏️
قابلیت Sketch@:
امکان رسم طرح اولیه و نقاشی ساده داخل محیط چت برای تبدیل مستقیم آن به تصویر پرجزئیات نهایی
⚡️
کاهش ۵۰ درصدی تاخیر:
سرعت تولید و بازبینی تصاویر دو برابر سریع‌تر از نسخه Images 2.0
🎯
ویرایش موضعی پایدار:
تغییر دقیق بخش‌های مدنظر (مانند متن تبلیغاتی، پس‌زمینه یا سوژه) بدون دست‌خوردن هویت اصلی یا افت کیفیت در مراحل بعدی
📁
قالب‌های آماده (Templates):
تسهیل ساخت پوسترهای تبلیغاتی، تراکت‌ها و عکس‌های صنعتی محصول
این مدل برای تمام کاربران در وب، موبایل و دسکتاپ فعال شده است. برای توسعه‌دهندگان نیز در دو نسخه ارائه می‌شود:
Flare
(پیش‌فرض، سریع و کم‌تاخیر) و
Sunburst
(مخصوص خروجی‌های بسیار دقیق و سنگین).//دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/2999" target="_blank">📅 18:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiHmfE1dKUT3NlA7I9y1X7hq0W4xVRMYr9UOD4ArE7n8a2mvAdGpyzfkMSRIVn53Hh4tap6A8So41PW6_vgROkgLwgSMS-n-vgXKlA69F_uzaNOdG1eTLHZaZlZUPaegMX5Y4AeH4CC6giSBsU4kYREGtRaWgI2vymv0omnkIu-CQ3UargCj795X18sZQNW52I0WmzvB0LN88A1FAZNuHeEMcNXcDKyR5RM0wye0GsJRSSxr8RgkhWaylIR0XZTNoFBGlWqvlK1oAxOE02R7HleQDunAq6BlFttVAqC_YBrP8qhEkRI8LFlKnV3nAUgRrn3MbnjsUDad-F9C6nWbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
راهنمای نقشه ذهنی کلیدهای میانبر کامپیوتر با کلید کنترل
🔸
این تصویر یک نقشه ذهنی از کلیدهای میانبر عمومی کامپیوتر است که هسته اصلی آن، کلید کنترل (Ctrl)، قرار گرفته.
🔹
هر شاخه شامل لیست‌های دقیق از کلیدهای ترکیبی و عملکردهای مربوطه است که به راحتی قابل درک و یادگیری است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/iaghapour/2998" target="_blank">📅 16:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.  گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/iaghapour/2996" target="_blank">📅 20:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=gBRtccDAkx_Gag68jM1032Ryk08lU4opilgU4Ynlc2Jg8WRNGnHIAsWi8_fvw-UZqPQysGYq6QQ-k08hiPpcKqA38OuaYVCwyt9P2ptZQ2LYIMlEY7Iz0s3-5eaf2v04c2xdc3-wOxuBMAUvP0ETZpwfBXWxev4Gay6SRDzO0a7IaicW4uC57YujJUIXB5q9T2Jhge2QVqDte5PoJPJhi21kTHeGdmrxr6klrSwzNIlhIMLL0I1g-fonDakk82zcYaybfayDKjU1_zrEO900PJXPzFfr7vABK-7rBi8zqarRcZ18EW6onTQcrbj6RoDUiQ50juHe-SAcjfzAdgwwGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=gBRtccDAkx_Gag68jM1032Ryk08lU4opilgU4Ynlc2Jg8WRNGnHIAsWi8_fvw-UZqPQysGYq6QQ-k08hiPpcKqA38OuaYVCwyt9P2ptZQ2LYIMlEY7Iz0s3-5eaf2v04c2xdc3-wOxuBMAUvP0ETZpwfBXWxev4Gay6SRDzO0a7IaicW4uC57YujJUIXB5q9T2Jhge2QVqDte5PoJPJhi21kTHeGdmrxr6klrSwzNIlhIMLL0I1g-fonDakk82zcYaybfayDKjU1_zrEO900PJXPzFfr7vABK-7rBi8zqarRcZ18EW6onTQcrbj6RoDUiQ50juHe-SAcjfzAdgwwGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره دهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mmdoo-yt، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/iaghapour/2995" target="_blank">📅 18:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_OPpM7dWeu_88hZGTVxwN4_2Bg335DNb8Md4qNYvuOozavCmZS0ZBPwQ0rEJx_n8G3Yj1Jda5VmgUFblFmsyf7y24J1S2Pjup4cesvMiquB60V-6p8b_eMLQLvD9Ov6BdWOmxvsjeZtIbgLr3_ySXZZDEKJQFrlLh5jsYeAZAEwOxNaX56O3k-Kwm_t80356x0_pfmoZC0Ead0SJk41uqGsvyIKP8moZ96BM5Wws88hOt7VEryIoLv091ViU1AM-rh3hOUGveT1d8_ArIBuf0VFAborQ5Xk91kXxmeauxK5_Z1j8g5sCFdosTvuHKZny8A_Fe0c8I24POAgvKYWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نسخه 0.12 مسنجر سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور خودتون یک مسنجر بالا بیارید و با دوستان خودتون چت کنید.
👇🏻
تغییرات کلیدی سانگبرد (Songbird)
:
🐘
پشتیبانی از دیتابیس PostgreSQL
🪣
ذخیره‌سازی ابری روی آبجکت استوریج‌های سازگار با S3
📥
پشتیبانی کامل از استقرار به صورت PaaS یا CaaS (
دیپلوی آسان در Railway و Render
)
🎬
ورکر مستقل مدیا برای پردازش و تبدیل ویدیوها
📴
کارکرد چت در حالت آفلاین (صف‌بندی پیام‌ها و ارسال مجدد خودکار)
🛡
دسترسی اضطراری به پنل مدیریت
👥
عضویت خودکار کاربران جدید در چت‌های عمومی
📦
قابلیت Rollback (بازگشت به نسخه قبل) در اسکریپت نصب
👇🏻
بهبودها و رفع باگ‌ها:
🔸
استفاده از شناسه UUID برای کاربران، چت‌ها و پیام‌ها
🎨
بازطراحی رابط فهرست چت‌ها با تایپوگرافی بزرگ‌تر و ظاهر مدرن
🔧
ارتقای امنیت با رمزنگاری اختصاصی تامبنیل‌ها و فایل‌ها
🚪
رفع پرتاب کاربر به صفحه ورود در صورت قطعی موقت سرور یا اینترنت
🔗
داکیومنت پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/2994" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2991">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lig6nJzra1HMz1LXywJWsg_XQsIgBmVe3pNQJPwQmXmULwWQQPEyhNZ428lmoGfL2SmFH_RcbLrMNmoNnu8rAGGWFWSvwzBxJK2VtlTmEEXmAEaaKnNWIr0h-MZL-YMwXWsvC5aLoYS5jNax0WYeauXx0GmNcFcf1akoXn2IlOwesmoqzChf1XCljsJpqR2wo5qeam53CLoLHbwTzDu51ULsPgvwpeCIM0bC2_yWViNlLOa5vyHofX-cv8Oos2pCCRXiAROFTwVhUA_lfSMQiMdJSKvmlLixbh_x-bQikTcL3C4h-PRBmk3IM1N9B0nd-c295xwADjpmKmNIR7WlZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uyGBiOnJOIp91tTDbFM8obeMfm87biSY_p0y9S8v21_MT-n5YTvqtiKFkB72AdEHHIr2QYmRS0Zl3po8QgvYzAtTfVdvPvhkO2pkNd5JyTm_QYclRF4ZmCnzOqxFKMQmqdifLf8ojJU-f3-U1qheT0UsLEo_OQ8pvzmpbITy3-kR3g21DfJCwEPWDqX1OUGIn2A99lTWKHg4g-5G0so0qGDvrlQmbW6BF3dY0oUc5XQm_26XEDnqoNRKDdNVioihDmg7F3r8gK0SHvRX1geEsSIqHWAxTclIG8ySorjSaENr5AyZT36ELpME63ohJZQu9BqvEXfu95q4u3o5J5XXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhdGcaofT7G_dbWLUCbUiqfqtjzSLlifd9ycJFrb2-F12Stn0YaP0bcvS9AJ-7mR_llmbqPjwdNF7Se-p1WxGILyKpzVw-z8ojJHlrhFNyDQmo3NarGra17Y_kA5sAI6NIX4Bg7AQ7YCaF8GyRGa_F_oI8eVgbSwqz4jmAH1vebdH-EHzbrbmE23JdQPcGg53fo_1fJ5OC38zSMLCeAmGOdA0gudwog0yrUYzIAMwnefw5fifhvyux5R_wqBpCPF3iOxuS7MyiauBi6Z_jUvnUfRiqNXFpv3llx9nYJiSxi3rofC8HwW9DtnTvIe9vgzBaF46z4jpDo_xsP2HN-IUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
رکوردشکنی تاریخی قیمت آیفون در ایران؟!
اپل رسماً قیمت گوشی تاشوی جدید خود یعنی
iPhone Duo
را در نسخه پایه (۲۵۶ گیگابایت)
۱٬۹۹۹ دلار
و در بالاترین کانفیگ تا
۲٬۹۹۹ دلار
اعلام کرد؛ رقمی که با ورود به بازار ایران احتمالاً به برچسب نجومی
یک میلیارد تومان
خواهد رسید!
⚙️
چرا پیش‌بینی قیمت ۱ میلیارد تومانی برای آیفون دوئو دور از ذهن نیست؟
🔹
مقایسه با قیمت آیفون ۱۷ پرو مکس:
نسخه پایه ۲۵۶ گیگابایتی آیفون ۱۷ پرو مکس با قیمت دلاری ۱٬۱۹۹ دلار، در بازار ایران به صورت رجیسترشده در محدوده
۴۴۰ تا ۴۵۰ میلیون تومان
معامله می‌شود. بنابراین پایه دلاری ۲ هزار دلاری Duo با احتساب هزینه‌های رجیستری، سود واردکننده و حباب هیجانی روزهای نخست، به سادگی مرز ۱ میلیارد تومان را رد می‌کند.
🔹
چالش بزرگ eSIM در ایران:
اپل در آیفون دوئو درگاه سیم‌کارت فیزیکی را به‌طور کامل حذف کرده و فقط از
eSIM
پشتیبانی می‌کند؛ با توجه به عدم فراگیری و محدودیت‌های گسترده فعال‌سازی eSIM در اپراتورهای داخلی، استفاده از این دستگاه در ایران با دردسرهای فنی جدی همراه خواهد بود.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/2991" target="_blank">📅 17:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjEQvLEbgAQELDnL19solq3PIHeLAgJhwKzmeAqMxl8qCwXrJBmrL1nFXrt9iVZoc1wuEeinrLtElrK2cBChJXgic2-x8LOTPO09Xeanp0o181KMIML9Txw7DQwkcgkPZGoGXQ3n2ovliBmACnV9JmJbxG4hp2JiUlGOt04tYN4-jYvQ9xl6SryxOP89AtbWI2_Ole4-mHGf0OaExH9tRkXzzeQYjPWfb5qdtAuIPyF9PXrZVgh3_3BwAU-uDdoYLlbgpkZ24ExsogafAE3pHEvYw70n1Il5-JKjlk1TTqfGUmum1HT0LtKVZRMB6tW8XN4ZqXsnapSA2MhNNh9HRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بازم داستان تکراری؛ اینترنت داغون، اما ادعاها برقرار!
🔹
از دیروز وضعیت اینترنت رسماً افتضاح شده؛ پکت‌لاس شدید، کندی اعصاب‌خردکن و قطعی‌های مداوم. بهزاد اکبری (مدیرعامل زیرساخت) هم طبق معمول اومده توییت زده که علت کندی «قطعی فیبر نوری در ارمنستان» بوده!
🔹
الانم ادعا می‌کنن مشکل حل شده، ولی در عمل کیفیت شبکه—مخصوصاً روی اینترنت موبایل—هنوزم افتضاحه و هیچ تغییری حس نمی‌شه.
✍🏻
جالبه که با یه قطعی سیم توی کشور همسایه کل اینترنت مملکت فلج می‌شه، ولی موقع افزایش قیمت بسته‌ها همه‌چیز سر جاشه و وزرا توی صف اول توجیه گرونی می‌ایستن! اول یه اینترنت پایدار و بدون قطعی تحویل بدید، بعد دم از گرون کردن تعرفه‌ها بزنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/2988" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxzIssfYRSQ-SbbvloJz9Yuj8VQZiSWMmY0ZmkyXDgozikfdG8MRmz6Qr9GBt0Kp7XWP5GuDML5HnPRbz62z8iXDdHFfHZ8KagJFOLxS7Z-sJP9s5vRBK449Mbr1VkaSArSC7OYAjATRUE-bOWgS3MU3xqJQ675tUcYk8CJf-Lwxf6znhhnt_Z1R8qmkLGFvES9yzUredTgCxrtJyjEhlT1ukqAUHHuuaI216hvVZCulw9-we1ruAG2SrspC-NMQFO3_n68cmRYbj9KOqJJZQCp35xK81xgLohmRwcZtl9nLq_EAZuQ2tfgk-6Be7jCHV-uWkwq7DZsiX2ZNnl6xfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
زنگ خطر امنیتی؛ لو رفتن دیتابیس حساس کاربران JumpJumpVPN
🔻
دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اگi از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns || ircfspace
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/iaghapour/2987" target="_blank">📅 19:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdjn2gyVy04DzRMwPbjAHOsn_I-jSn2PiFloJFOGszCYWADqWdaAx0xsvIS3fuQNfT7pxCT-x-ELT3JZi6LEzwPuTcg4eX75Z8gXeZcXiwx2ctzv8AHZqKTkin0GM1qho0a44lwNyv3BQFrPm0cQmEm82FMCJ4z0uq-Ts84gnSN7yZ4cWrTB_ixXucNT26H8hTMUExh43mXt-XqHFEm4NrsikNZnRlLm8LwSyMu3ENVZkNk1HXbpk-o2CgHrav3IFzxWmHInKd1c-ofrd5orTkkCtFYAqTvfc8AqPam3a_T8hg_3e1C9TEPHFgq9e63otWhlYnxdPEK9WEgQx88ycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بروزرسانی جدید برای نسخه اندروید oblivion منتشر شد
🔹
فیلترشکن رایگان
oblivion
به صورت اوپن سورس و امن برای اندروید توسعه داده میشه و میتونید ازش استفاده کنید.
🔸
هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
🔗
دانلود از گیت هاب
#فیلترشکن
#oblivion
#رایگان
برای دور زدن فیلترینگ و آموزش کامپیوتر و تکنولوژی و... ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/2986" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">SoftEther Code -- @iAghapour.txt</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/iaghapour/2984" target="_blank">📅 23:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SoftEther Code -- @iAghapour.txt</div>
  <div class="tg-doc-extra">3 KB</div>
</div>
<a href="https://t.me/iaghapour/2983" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دستورات برای ویدیو
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2983" target="_blank">📅 19:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN2ZANQgFRZACVi9cdIvkXG9Xg2bwcH5MEaTL0dl78qalpZ3Eh6zBureFizXOrErZw_mo6_cR4XghQGUFX724BUt_Ea3-Z6Qj12P_CwuzpBqkTIGgDE_5bN-LpfbFdIHk-Y_aCCni_BGS8ei9Ngpb97yxX3Zp9QtxB431SkteAP4T_JIM9Tct3c-quxZvGjNjHGDeotLfJg8E3ano2l7fvwVPAaWj29JT_W9ZNrnNujIG03h-AcXXgHBJsi95cAvCXo1sudJQF6xgQG4B3sL1mqA-xgJJhrPCjctFfmFD703n8uS20uDVYX9Bq61Vzf8pMEPPH4VY4B8D6h5IKqCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🚀
🔹
توی این ویدیو قدم‌به‌قدم بهتون یاد می‌دم چطور سرور SoftEther رو به همراه یک پنل تحت وب اختصاصی راه‌اندازی کنید. این پنل قابلیت‌های زیادی مثل مدیریت کاربران، اعمال محدودیت حجم و امکان استفاده از پروتکل‌های مختلف رو در اختیارتون قرار میده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#سافت_اتر
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2982" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2981">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⭕️
دفاع وزیر ارتباطات از گرانی اینترنت: کمتر از بقیه کالاها گرون کردیم!
ستار هاشمی، وزیر ارتباطات، در صحن علنی مجلس در پاسخ به سوال نمایندگان درباره گرانی شدید بسته‌های اینترنتی، از افزایش تعرفه‌ها دفاع کرد و آن را با سایر کالاها مقایسه کرد؛ پاسخی که در نهایت نمایندگان را قانع نکرد و منجر به کارت زرد مجلس شد.
⚙️
محورهای صحبت وزیر و استدلال‌های گرانی:
🔹
مقایسه با تورم سایر کالاها:
وزیر ارتباطات مدعی شد طی ۵ سال گذشته، با وجود جهش ۲۰۰ تا ۵۰۰ درصدی قیمت اکثر کالاها و خدمات، رشد تعرفه‌های ارتباطی کمتر از ۸۰ درصد بوده و در نتیجه گرانی روزافزون اینترنت مطابق واقعیت نیست!
🔹
عوامل توجیهی افزایش قیمت:
افزایش هزینه‌های ارزی، مصرف برق و انرژی، هزینه‌های نیروی انسانی و نگهداری زیرساخت‌ها به عنوان دلایل اصلی افزایش تعرفه‌ها عنوان شد.
🔹
کارت زرد مجلس:
پاسخ‌های وزیر درباره گرانی بسته‌ها و عدم توسعه فیبر نوری نتوانست نمایندگان را قانع کند و به او کارت زرد دادند.//شبکه‌چی
پ.ن: می‌گن «چون بقیه چیزا ۵۰۰ درصد گرون شده، اینترنت رو ۸۰ درصد گرون کردیم.
جالبه که هیچ‌وقت کیفیت خدمات رو مقایسه نمی‌کنن، ولی برای افزایش قیمت سریع دست به دامن مقایسه با تخم‌مرغ و گوشت می‌شن. کاربر الان نه‌تنها بابت همین اینترنت محدود و کند پول گرون‌تری می‌ده، بلکه مجبوره‌ ماهانه به اندازه همون بسته (شاید هم بیشتر) پول فیلترشکن و سرور بده تا فقط بتونه به اینترنت آزاد دسترسی داشته باشه؛ این هزینه‌های تحمیلی رو چرا توی آمارهای ۸۰ درصدی حساب نمی‌کنید؟!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/2981" target="_blank">📅 17:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arQTiunNc8pZ8nXSW7HfYtymDa0SUofBia9euEq7aPzsy9v7l6Nb-V4YLln8o3nN3iTiJbz3hFQDoRPD0BuplfaXYPB3YhvlfDXQ9DmLLPCUyTXV7mggsqf7zDqfAjvUq9cMBE6Uim8jb1KjRDR6ot260bv6WqttwLEB16YVYcZfCOxQd4s_6g1J1PjB7gF-lott0LbZNCNeAAGrsVYQrvpaUBASh4yDrDT7IbXb-8SeiDYFBHqNQTf-Xsf83ImR-LGjCCK0MWfMEKDOq8o9hxbPRGTlyDu9FugXTmayaaDEQtloAtDSjzviSbPfvylUwtxOftLW7wAInikurQHDTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی EMS IPAM؛ سامانه مدیریت آدرس‌های IP و تجهیزات شبکه
اگر برای مدیریت ساب‌نت‌ها، رادیوهای وایرلس و تجهیزات شعب مختلف هنوز از اکسل استفاده می‌کنید، ابزار
EMS IPAM
یک پنل متمرکز و گرافیکی برای سامان‌دهی و مستندسازی شبکه است.
🔹
مدیریت ساختاریافته IP:
پشتیبانی از رنج‌های /16 تا /32، جلوگیری خودکار از تداخل ساب‌نت‌ها و نمایش ظرفیت آزاد/مصرف‌شده.
🔸
مستندسازی شعب و تجهیزات:
ثبت موقعیت شعب، پورت‌ها، توپولوژی و ذخیره راه‌های دسترسی سریع (WinBox، SSH، RDP و وب).
🔹
پایش مستقیم میکروتیک:
اتصال به RouterOS از طریق API و نمایش زنده وضعیت اتصال، سیگنال و پهنای‌باند رادیوهای وایرلس.
🔸
کلاینت ویندوز:
باز کردن مستقیم نرم‌افزارهای مدیریتی (مانند WinBox) با یک کلیک از داخل پنل بدون درج رمز در مرورگر.
🔹
تعیین سطوح دسترسی، ایمپورت/اکسپورت ساب‌نت‌ها و پشتیبان‌گیری خودکار.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/iaghapour/2980" target="_blank">📅 16:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVzSJudjD6LLFziG6SNmqM3mh0_mlbtc-X-tUe23hZns3_TzQ2AHxkE9ZM3lxdOzZN1QWxmyiPtgXPJwrr3sokSxPRNkLwMp9W2zw2wxHIYY1AiIdguo5rxuc5g4LVZOg5-JgynflQUb8b1y-yk7rvVS2p0e3KwJ5D6b_yeAExHoM5yPHlXKZQ8W4Pr2Ha-tUnL0p9AoTzpGXeI5Y0arXB6QufQcJJCNQuI9Hr6HXfACsqRvw_46-xar0YkzjE-aRCV59GIL_R068XbdwAY9WP525_Jkhlj4uMYW7JX8NmrnsJg0CAwJ_B1xMRCr3KQRou8E9gQqKVQp2UyzZHEcNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نرم‌افزارها در پس‌زمینه سیستم شما چه می‌کنند؟ کنترل کامل ترافیک با فایروال متن‌باز Portmaster
اگر زیاد اهل تست و نصب نرم‌افزارهای مختلف هستید یا نگرانید برنامه‌ها دور از چشم شما تله‌متری و اطلاعات به سرورهای ناشناس بفرستند، ابزار
Portmaster
دقیقاً همان لایه محافظتی مورد نیاز شماست.
⚙️
قابلیت‌های کاربردی و مهم:
🔹
دیده‌بانی زنده اتصالات:
نمایش شفاف و لحظه‌ای اینکه هر برنامه دقیقاً با چه IP، سرور، در چه ساعتی و از چه طریقی ارتباط برقرار کرده است.
🔹
مسدودسازی هوشمند ترافیک:
امکان بستن ترافیک‌های مشکوک، ردیاب‌ها (Trackers) یا تبلیغات به‌صورت موقت یا دائمی با یک کلیک.
🔹
ایزوله‌سازی آفلاین:
امکان قطع کامل دسترسی به اینترنت برای یک برنامه خاص تا صرفاً به‌شکل لوکال و آفلاین اجرا شود.
📥
دانلود از وب‌سایت رسمی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/2978" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2977">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwhXv0g0jliQOzRIwfMBOp53sE0OEgjhP2mNMwPCLTChjkxEvp7xRtfliqEyBt0VWHj6VPt8Jcmpw-fH-uIOva27fMFmT7RRqvmdn6_MjjmdbWsohVjgVmNMFiIUu-QhpKNb62iJbn0ANTKLgKC6l_8h_bhlTpgh5kgiLtQfNLtP9H95ziZcLI08OOpH_F3FjCKhtnfa5S0oc1fD9ETkP_YxiP4WwCm14TZsnSCzQmmZVjzJMwG6d9Xyag8BCIfZQ7SS9VumO0TSDKNJZPM9PPwtGkntPH7lGwgEglwWk3M3MJzg_oOF4nQnz_qVtTgKBtwXeIv2ORGJnSdCxVKMsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بحران لغو گواهی‌های SSL در شبکه بانکی ایران
🔸
تحریم مراجع بین‌المللی صدور گواهی امنیتی مانند Let’s Encrypt و Certum علیه زیرساخت‌های ایرانی، سیستم بانکی کشور را وارد یک بحران امنیتی تازه کرده.
🔹
تغییر آدرس به جای حل ریشه‌ای:
برخی بانک‌ها (مانند بانک ملی و بانک ملت) برای دور زدن باطل شدن گواهی SSL، اقدام به تغییر دامنه‌های اصلی خود کرده‌اند؛ حتی در مواردی بدون ریدایرکت خودکار یا اطلاع‌رسانی دقیق، که مستقیماً کاربر را در معرض صفحات جعلی و لینک‌های فیشینگ در گوگل و شبکه‌های اجتماعی قرار می‌دهد.
🔹
عادی‌سازی خطای مرورگر:
مواجهه مداوم کاربران با خطای قرمز «اتصال امن نیست» در سامانه‌های رسمی بانکی، حساسیت عمومی نسبت به هشدارهای امنیتی را از بین می‌برد؛ کاربری که یاد بگیرد این خطا را نادیده بگیرد، طعمه ساده‌ای برای حملات فیشینگ و صفحات جعلی درگاه‌های پرداخت خواهد بود./دیجیاتو
پ.ن: اگه فردا روز دیدید یه «SSL ملی» راه انداختن اصلاً تعجب نکنید! چند وقت دیگه میان به بهانه تحریم و امنیت، همه کسب‌وکارها رو مجبور می‌کنن برای گرفتن درگاه پرداخت و ای‌نماد از همین سرتیفیکیت داخلی استفاده کنن.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2977" target="_blank">📅 17:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2976">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i31WxoW-guHcctlwZhR8154XjQx146PxTLjo7VFCQHt3V7R81HBPFDgOnxGTM9sSL7KL46veihJFd0JRy2y1AoIla2LydpKx1gsQmncvrN_tx7rqJKtTQeY2YeAbakQLeydL-SvLbTdaZARnSp_IjMOOMmvPZgOZA_dp6m6_MWg6Q1qlCTJg9RTkVQpTvfioR7XxwgS_Z03HymKLhkWRexBsU2KOI2tYb-5kB3NblcANt7M-NvHPYXDwa1MQqxRPXClCdd31r8JSZuAu2PQu0n6oYmdjX6rDVg87D9kVX-QzacS2UmUnuEbCMgM_qJ567Q61X-SPvvQZs3s48_X-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی از «آیزا»؛ دومین آنتی‌ویروس بومی مبتنی بر شبکه ملی اطلاعات
دومین آنتی‌ویروس بومی کشور با نام
«آیزا» (Ayyza)
رونمایی شد؛ سامانه‌ای امنیتی که با تکیه بر هوش مصنوعی و ساختار شبکه ملی اطلاعات، امکان شناسایی تهدیدات و دریافت آپدیت‌ها را بدون وابستگی دائم به اینترنت بین‌الملل فراهم می‌کند.
🔹
موتور تشخیص هوش مصنوعی و سطح کرنل:
توسعه انجین اختصاصی مبتنی بر یادگیری ماشین و بهره‌گیری از فناوری‌های سطح هسته ویندوز (Kernel-level) جهت پایش دقیق‌تر، واکنش سریع‌تر و بهینه‌سازی مصرف رم و پردازنده.
🔹
عدم وابستگی به اینترنت جهانی:
قابلیت آپدیت به‌صورت آفلاین و انتقال داده‌ها و امضاهای امنیتی از طریق بستر شبکه ملی اطلاعات (اینترانت داخلی).
😁
🔹
اکوسیستم امنیتی یکپارچه:
ترکیب فناوری‌های EDR و XDR برای شناسایی حملات چندگامی و روز صفر، در کنار هماهنگی با سیستم‌های جلوگیری از نشت اطلاعات و مدیریت دسترسی‌های ویژه (PAM).
✍🏻
حواستون باشه قبل نصب با آنتی ویروس معتبر مثل کاسپر اسکن کنید آیزا رو :) تازه با اینترنت داخلی هم کار میکنه :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/2976" target="_blank">📅 14:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=Pk4rmMCuOOk4_ueFwjpRIwBd8h4OkDw05nKG4KUxtB3acbSiJt2NAZcU1B9TpkRNq6OpzuINR8YVr6q_8xQAlk2zSPW1Otjoba8jejcGCwljcQ_po7MXnu_y06KXFdtzrCIO39q5NkkgynrUNtAu4jll8lJ1wZU2GD7_2lPOckd2AYCkN8OJcQ0dYrjPC7x1DkWzKRjGLBMASQM2jLv-zPPbuZcTNT3KaLI7laEWnvettqzLEQvvuyW6plKhiU7t-Rx-2w4UxMzcEQWgd_FCPJRB-q_1qGo4E75s0gtjXlAxog8j68kw2S-JaeOzB6LiVJWIe0w3Gz6bW2nRhTWQeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=Pk4rmMCuOOk4_ueFwjpRIwBd8h4OkDw05nKG4KUxtB3acbSiJt2NAZcU1B9TpkRNq6OpzuINR8YVr6q_8xQAlk2zSPW1Otjoba8jejcGCwljcQ_po7MXnu_y06KXFdtzrCIO39q5NkkgynrUNtAu4jll8lJ1wZU2GD7_2lPOckd2AYCkN8OJcQ0dYrjPC7x1DkWzKRjGLBMASQM2jLv-zPPbuZcTNT3KaLI7laEWnvettqzLEQvvuyW6plKhiU7t-Rx-2w4UxMzcEQWgd_FCPJRB-q_1qGo4E75s0gtjXlAxog8j68kw2S-JaeOzB6LiVJWIe0w3Gz6bW2nRhTWQeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برندگان عزیز قرعه‌کشی
(دوره هشتم و نهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 2 عدد اکانت هوش مصنوعی ۱ ماهه برای 2 نفر مشخص شد:
👤
برنده عزیز با آیدی AhvanSalehi-f3r، مبارکتون باشه!
✨
👤
برنده عزیز با آیدی abolfazlghasemi1-q7t، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/2974" target="_blank">📅 20:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E75CwN8p7XOdzVIobP79C4cNpGPuklr_W27TRlvNmws-Ae6_kiiu6-QVEqy6Bt6d7Dk6wGaNNXE3z_YPcnP2N5yyfFrcHkzNWjuFXbTwQk153qI__zG6zbvWUy7pzbDrCtu_Eord2DkOJvuEw3f-pCd5obC0s9mVX7FMjoRLYT5BYTc9rbzbkx2QnQM01f6LMO4HizemRa8Vfsb6Z9uT7WGN0xdNZ97HlcUwXMg4u69KSe6uS3nsGFqyEK0q7CFmuOPGtuWUFpF0pw5_MhJTSrJe6EHSZqeYZjEMBSreNNR0w5WR9PdowGOAa-qHR97994FHySS_74p0xJFaJ0B_-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍🏻
وقتی خودتونم توی پلتفرم داخلی دووم نیاوردید!
🔹
سال‌ها اینترنت رو بستن و با فیلترینگ شدید خواستن مردمو به‌زور بفرستن سمت پلتفرم‌های داخلی، کلی هم بودجه خرج کردن و هر روز گفتن حمایت از پیام‌رسان بومی!
🔸
حالا بعد از این‌همه وقت، ستاد فضای مجازی خودشون جلسه گذاشته و گفته ممنوعیت حضور ارگان‌های دولتی توی پیام‌رسان‌های خارجی رو برداشتم، اسمش رو هم گذاشتن «پایان یک خودتحریمی عجیب»!
🔻
جالب اینجاست که می‌گن: «برمی‌گردیم همون‌جایی که مردم هستند». خب اگه مردم اونجان و خودتونم فهمیدید بستن این پلتفرم‌ها جواب نمی‌ده، چرا باید برای ارگان‌های دولتی آزاد باشه و پیج بزنن، ولی همون مردم برای باز کردن یه اپلیکیشن عادی هر ماه پول فیلترشکن بدن و با قطعی سر و کله بزنن؟!
این یعنی همون یک‌بام‌ودوهوای همیشگی؛ خودشون توی اپ‌های داخلی دووم نیاوردن و برگشتن، ولی زحمت و تاوان فیلترینگش هنوز رو دوش مردمه.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/iaghapour/2973" target="_blank">📅 19:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2972">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.
گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به هر دلیلی آی‌پی روی یه اپراتور مثل ایرانسل دچار اختلال یا مسدودی میشه، پیام میده که «سرورتون خرابه، بیاید رایگان آی‌پی رو عوض کنید.
واقعیت اینه که این روال، نه از نظر فنی درسته و نه منطقی
.
🔹
تست اولیه حق شماست:
وقتی سروری رو تحویل می‌گیرید، همون ساعات اول کامل تستش کنید. اگه دیدید همون بدو تحویل روی اپراتور مدنظرتون پینگ نمیده یا دسترسی نداره، کاملاً حق دارید به پشتیبانی پیام بدید، درخواست بررسی کنید یا حتی طبق قوانین هاستینگ سرویس رو عودت بدید. این حق کاملاً منطقی و محفوظه.
🔸
تفاوت خرابی سرور با محدودیت اپراتور:
وقتی سرور روشن و سالمه و روی بقیه شبکه‌ها یا اینترنت جهانی کار می‌کنه، یعنی سیستم مشکلی نداره. مسدود شدن آی‌پی بعد از چند روز کارکرد، ناشی از حساسیت فایروال اپراتور روی ترافیک عبوریه، نه نقص فنی سرور.
🔻
ارزش منابع:
آدرس IPv4 منبع محدودی در کل دنیاست و هزینه جداگونه داره. هیچ مجموعه‌ای نمی‌تونه آی‌پی‌های سالمش رو به خاطر مسدود شدن‌های بعد از استفاده، پشت سر هم و رایگان بسوزونه و جایگزین کنه.
👈🏻
ریسک اختلال روی شبکه‌های مختلف توی این بستر وجود داره و همه ازش باخبریم. بهتره با آگاهی از این شرایط خرید کنیم، تست‌های لازم رو همون ابتدای کار انجام بدیم، و اگر بعد از چند روز استفاده آی‌پی دچار محدودیت شد، مسئولیت این ریسک رو به پای خرابی سرور یا کم‌کاری ارائه‌دهنده نذاریم.
🟢
در همین راستا و برای حفظ حقوق شما، از امروز تمام ارائه‌دهندگان سرور که در کانال ما تبلیغ می‌شن، ملزم هستند تا ۱۲ ساعت بعد از خرید، امکان عودت سرویس یا تعویض آی‌پی رو در صورت وجود مشکل برای کاربر فراهم کنن.
بنابراین حتماً به محض تحویل سرور، تست‌هاتون رو انجام بدید تا در صورت وجود هر مشکلی، بتونید توی این بازه از این ضمانت استفاده کنید.
// قوانین در حال بروزرسانی و قابل تغییر هستش.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/iaghapour/2972" target="_blank">📅 19:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2971">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8wRG9QeoyEdN7SJBtdKhGzBXjv9Q-AYb4nZNBh-l6CB5BEWwm59nqYSm72JZqi_SvTlfb7F1TxKQ9W8REUML0ZlWKH-WQeXKSD-OCVH8i1UQEY8J1ZW3pL3GXKXBHAtjAl7sdNaP9MubsYLeUV9Zf-YniEkUd0XeclpWzSgjR9XFjINOGlFm8MSv7TBMQo8LUVJGZka3Ufi5MH5FkednX3Ybgb4BDN3QW0zVQkEzWEfwUuM5Nu5hAHO7Lu3Q28BADF05ec28uo5kkdun7jGyZHKUrOa8uUohIy0H91gEnYn7d29ENxEbtdW2vS-_yXmzLhwL_T7BJ_Nb-llKwa0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
شکست قفل Denuvo بازی Mortal Kombat 1 و قدرت‌نمایی هکر Voices38
قفل امنیتی جنجالی
Denuvo
روی بازی پرطرفدار
Mortal Kombat 1
بالاخره پس از گذشت حدود سه سال توسط کرکر سرشناس موسوم به
Voices38
شکسته شد.
⚙️
چرا جامعه گیمینگ می‌گوید دنوو به سخره گرفته شده؟
🔹
طوفان کرک در ۲۴ ساعت:
هکر Voices38 نه‌تنها Mortal Kombat 1، بلکه در یک روز ۵ بازی سنگین و مجهز به دنوو از جمله
Persona 3 Reload
،
Star Wars Outlaws
،
Metal Gear Solid V: Complete
و
Prince of Persia: The Lost Crown
را کرک و منتشر کرد!
🔹
جانشین بی‌حاشیه دوران پس از EMPRESS:
برخلاف رفتارهای پرحاشیه و بیانیه‌های طولانی کرکرهای سابق، Voices38 صرفاً روی بایپس و حذف اجراییِ قفل در زمان کوتاه تمرکز کرده و عملاً انحصار دنوو را در سال جاری به چالش کشیده است.
🔹
آزادسازی منابع سیستم:
بازی‌های مجهز به قفل دنوو همواره به‌دلیل ایجاد لکنت، افزایش استهلاک پردازنده و افت فریم مورد انتقاد گیمرها بوده‌اند و حذف کامل این لایه محافظتی معمولاً به بهبود روانی اجرای بازی کمک می‌کند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/2971" target="_blank">📅 18:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2968">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWzwrN8yWXP8bLVdQvjJF4JtG7hsXje7EOXfdr_IZf2T18uaIxpFI1JKFXD0F0oiYZomx2R8t9t5lCTD8fBSo-6vD2LKk0WXbKDXkXQ3YMk5QlVlPVMXjMZXW3Nq6n86TxIFC6wj53j0R68GM8hPp0P8zAt_HcG_hd1JBhEWuv-Zvq_c2KAsCSYf2g3TzeAygFV9bRQgLJ_NBcoEHhAOGFAi5egQtm4CZGfLPPUlUggPWsrQRz-xGnjv6cHQcLsTQYCBbnI4coaXaFOsHwONnZ9zYjVXdXwra6NCmE6-PT9U5AWwZR_t2RaVjL5Y9D_LKhyrhtijIp76BhSlVCHpNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بهترین پنل وایرگارد همراه با مدیریت حرفه‌ای کاربران + تانل
🚀
🔹
تو این آموزش بهتون یاد می‌دم چطور یک پنل جامع و سبک برای وایرگارد نصب کنید که هم امکان تعریف و مدیریت دقیق کاربران رو بهتون میده و هم قابلیت تانل زدن پایدار بین سرورها رو به ساده‌ترین شکل ممکن فراهم می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم قرعه‌کشی اکانت هوش مصنوعی داره و فقط تا فردا فرصت دارید! (شرایط: فقط قرار دادن کامنت زیر همین ویدیو).
👈🏻
قرعه‌کشی این ویدیو و ویدیوی قبلی با هم انجام می‌شه.
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2968" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWdcKIXCNPF-k2Wd8TIM5XRk5PvJXkq6tQbNb4OAOcopLd27Qkx1LT6jtQl1lc9wfdKhkpjiT3wVBHVwyYp93C7E30WOqjFExbF8RlXf_fCNkHKG84EMkFlHJ5hTmc20jUk7McjB3Vku6i2WepayG3dO1i8PoKgYT3Dims9yciuw_JqHHJL0fOhtg0-3eJ5CKDit3_MhyuefgQvXmukVIjyHSVaSoWMmKCynkOgQk9yFZpSHUueiChSxW9_DiSQ_hRI6vjGz2Ggt2lpxa5Y7IXyeeAkDTdyAvimLTiQ3ju_z3Ozs1TCWvMJR2lBu8FosTpxKd2Fi6PtNnrOZIoGScg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مایکروسافت از Project Zenith رونمایی کرد؛ نسخه‌ای اختصاصی برای توسعه‌دهندگان
مایکروسافت پروژه جدیدی با نام
Project Zenith
معرفی کرد؛ نسخه‌ای بهینه‌سازی‌شده، مینیمال و «آماده کدنویسی» از ویندوز ۱۱ که بخش‌های اضافی و نرم‌افزارهای غیرضروری را حذف کرده و تجربه‌ای نزدیک به لینوکس برای برنامه‌نویسان فراهم می‌سازد.
🔹
تمرکز ویژه بر هوش مصنوعی محلی
:
امکان اجرای مدل‌های زبانی محلی با بیش از ۳۰ میلیارد پارامتر (+30B) بدون محدودیت و افت کارایی.
🔹
پیش‌نیاز سخت‌افزاری سنگین:
طراحی‌شده برای سیستم‌های قدرتمند توسعه با حداقل
۶۴ گیگابایت حافظه رم
و پهنای‌باند بسیار بالای حافظه؛ نخستین بار روی مینی‌دسکتاپ Ryzen AI Halo شرکت AMD عرضه می‌شود.
🔹
بهینه‌سازی محیط برای کدنویسی:
نصب پیش‌فرض محیط‌های اجرایی (Runtimes)، ابزارهای ضروری برنامه‌نویسی و اعمال تنظیمات پیش‌فرض مناسب توسعه‌دهندگان.
⚠️
با وجود استقبال برنامه‌نویسان از یک ویندوز خلوت و بهینه، محدود شدن این نسخه به سخت‌افزارهای گران‌قیمت ۶۴ گیگابایت رم در بحران فعلی بازار حافظه، دسترسی بخش زیادی از توسعه‌دهندگان مستقل را با چالش مواجه کرده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2967" target="_blank">📅 16:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2966">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=UytBJT1L-bDW274iAwig6Yli5Tq29PM1mqmNWCYZSiiFKePUykH1lPSIi7h2OZFBxew2b053KIXf_z1OSCHA8VqmxuDNpnrxDDDdg0PIFmbLGx3WQL9-ll-blky6XzepnfKpjmqbRhj7jSIzan2uIC0OBeEazRFHBL4W-xIiy9Jg1p_4eV1aB4gJV6fLxe6EZbhCbvtSWQelZuu9hRmADxvv9IrIaEEvq83ilHbRU2GRrAZZEKE_g-Z-eydHqv9-NB65EWw7YYAskGbslL7HePis6vxqfP3-9s01TjOaBRRwONFwjUWy0JX3F2iTeumdnpmQgaVcBArWXzZlmndd4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=UytBJT1L-bDW274iAwig6Yli5Tq29PM1mqmNWCYZSiiFKePUykH1lPSIi7h2OZFBxew2b053KIXf_z1OSCHA8VqmxuDNpnrxDDDdg0PIFmbLGx3WQL9-ll-blky6XzepnfKpjmqbRhj7jSIzan2uIC0OBeEazRFHBL4W-xIiy9Jg1p_4eV1aB4gJV6fLxe6EZbhCbvtSWQelZuu9hRmADxvv9IrIaEEvq83ilHbRU2GRrAZZEKE_g-Z-eydHqv9-NB65EWw7YYAskGbslL7HePis6vxqfP3-9s01TjOaBRRwONFwjUWy0JX3F2iTeumdnpmQgaVcBArWXzZlmndd4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی مایکروسافت از MAI-Image-2.6-Flash؛ تولید ارزان و سریع تصویر
مایکروسافت نسخه سبک و کم‌هزینه مدل تولید تصویر خود را با نام
MAI-Image-2.6-Flash
از طریق پلتفرم Microsoft Foundry در دسترس توسعه‌دهندگان قرار داد.
⚙️
ویژگی‌های کلیدی:
🔹
سرعت بالا و صرفه اقتصادی:
۲.۸ برابر سریع‌تر از GPT-Image-2-Medium و با ۷۲ درصد کارایی بالاتر؛ ایده‌آل برای اتوماسیون و ابزارهای تعاملی پرمصرف.
🔹
ویرایش نقطه‌ای:
اصلاح دقیق اشیا، نوشته‌ها و چیدمان بدون تغییر در سایر بخش‌های تصویر.
🔹
ثبات کاراکتر و محصول:
امکان بارگذاری حداکثر ۵ تصویر مرجع برای حفظ یکپارچگی چهره و کالا در خروجی‌های مختلف.
🔹
اتصال به وب:
ارتباط مستقیم با موتور جستجوی بینگ برای رندر دقیق سوژه‌های واقعی.
💰
هزینه خروجی تصویری:
۱۹ دلار به‌ازای هر میلیون توکن (در برابر ۳۸ دلار برای نسخه پایه 2.6).
هر دو مدل هم‌اکنون در مرحله پیش‌نمایش عمومی در دسترس هستند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/2966" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2964">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0cMT2DeZX90eahYdAR2IZ82k0M1QvKg5g7ePidjJhqioJqTAfxysv6BaLzPPzO_wRJMvg_PY7LzWQhtNJHQOrBFxF9E5dOJl6BQrVP0L0e3o1LqqCc6rneogbrPalPRF01n7-Uk99roX78Ck1YIdYUHeqZ8Lb6hVjt-yTBOBViPIGhccuNcmWfCvttjXFwkAkpDrwxYRbvgxOX7MqWGWa80iGalerQJq6GClIL7SCw9w1GiB7RsJkuF1tpMZXaDwc6FUxnokqGhzyTLouPQOko-GYQFPJXiWcHaFUvpxflrwf39isgcXYZ7LvzV-wtcCVmhLWxxl8GXCu4sdgK4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل «زاگرس» (Zagros)؛ فورک چندهسته‌ای مرزبان
پروژه
Zagros
یک فورک از مرزبان است که محدودیت تک‌هسته‌ای را برطرف کرده و به شما امکان می‌دهد تمام هسته‌های معروف VPN را هم‌زمان روی یک سرور و نودهای مختلف مدیریت کنید.
⚙️
هسته‌های تحت پوشش:
🔹
هسته
Xray:
پروتکل‌های VLESS، VMess، Trojan و Shadowsocks
🔹
هسته
sing-box:
پروتکل‌های Hysteria2 و TUIC v5
🔹
سایر هسته‌ها:
WireGuard، OpenVPN، SoftEther، SSH Tunnel و PPTP
🚀
ویژگی‌های کلیدی:
🔹
اکانتینگ یکپارچه:
اعمال سهمیه حجم و محدودیت تعداد دستگاه متصل به‌صورت سراسری روی همه هسته‌ها و نودها
🔹
کلاستر نودها:
اتصال امن نودها با تایید Fingerprint و مدیریت هسته‌های مجزا برای هر نود
🔗
گیت‌هاب پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2964" target="_blank">📅 20:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2963">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🧠
رونمایی اوپن‌ای‌آی از پرچمدار GPT-6 Astra؛ ادعای ورود رسمی به «عصر AGI» و انقلاب در کار با کامپیوتر
اوپن‌ای‌آی با رونمایی رسمی از مدل پرچمدار
GPT-6 Astra
، آن را جهشی نسلی در حوزه‌های امنیت سایبری، برنامه‌نویسی و تعامل مستقل با سیستم‌ها نامید؛ تا جایی که گرگ براکمن صراحتاً اعلام کرد:
«به عصر AGI خوش آمدید»
.
⚙️
ویژگی‌ها و قابلیت‌های محوری GPT-6 Astra:
🔹
توانایی عامل‌محور و کار با کامپیوتر:
این مدل بدون نیاز به رابط‌ها و APIهای پیچیده، مانند یک کاربر انسانی با موس، کیبورد و صفحه تصویر کار می‌کند؛ فرم‌ها را پر می‌کند، رکوردهای CRM را تغییر می‌دهد، نرم‌افزارهای مهندسی (KiCad/FreeCAD) را اجرا کرده و کدبیس‌های پیچیده را مدیریت می‌کند.
🔹
سرعت و بنچمارک‌های خیره‌کننده:
🔸
در تست OSWorld 2.0 امتیاز
۷۲.۶٪
را با سرعت حدوداً
۴۷ درصد بیشتر
از GPT-5.6 به ثبت رسانده است.
🔸
ثبت امتیاز
۹۸.۶٪ در آزمون معتبر تعمیم‌پذیری ARC-AGI-3
و امتیاز ۱۰۰٪ در بنچمارک ExploitBench.
🔹
جهش آموزشی با زیرساخت Stargate:
نخستین مدلی که با بیش از ۱۰۰٬۰۰۰ واحد پردازشی آموزش دیده و برای اولین بار، مدل‌های نسل قبل به صورت خودکار بخش اعظم نظارت بر آموزش آن را بر عهده داشته‌اند (حرکت به سمت خودبهبودی بازگشتی).
⚠️
ابهامات و حواشی مهم پیرامون رونمایی:
🔹
غیبت بنچمارک اقتصادی GDPval:
در گزارش‌های منتشرشده، نتایج آزمون GDPval (سنجش کارهای واقعی بازار کار و اقتصاد) دیده نمی‌شود که این امر تحلیل دقیق بازدهی سازمانی آن را فعلاً با شکاف روبه‌رو کرده است.
🔹
سایه بحران‌های امنیتی پیشین:
این رونمایی پس از حادثه جنجالی نفوذ یک مدل داخلی و منتشرنشده اوپن‌ای‌آی به هاگینگ‌فیس انجام شده و مدیران شرکت بر حفظ لایه‌های نظارتی سخت‌گیرانه روی ایمنی Astra تاکید دارند.
🔹
عرضه:
دسترسی سازمانی برای بخش امنیت سایبری از امروز آغاز شده و طی روزهای آینده برای کاربران Plus، Pro و Enterprise فعال خواهد شد.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2963" target="_blank">📅 18:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2962">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA1puEXj3F0CvS0rB4XcnEJxQZ17ovTZKswzTnBkMNLuPKmdJ8PRDNcwhJQMprHTzGkA0KsWrOhACrjFJ4sKbUMEYCMMebvfQIyN9TRKZuxbk7ELPnxSCOsQFzU-RTog1aC0YWVXBcIxm3lN-_CkCyUEH8kbE6vcA1qwYbatKSG7NBvlKlrR7guTuiqw6Gdol4eHFJcbuXrC7Sr4ANIXAOH_569iUvsxJV5IXbdmLcm-h6N6hyE9_-kREBbOCDTZbWwuQTq6i-J0ntn5-UKtD_TedETFt6INHciQTf0T-1dw26rKLg0FyjTvESKv4aGBrdjhaXqw2031Z4Z9yJjwTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏛
مخالفت زاکربرگ با طرح نظارت بر هوش مصنوعی در گفتگوی محرمانه با ترامپ
به گزارش نشریه
Politico
، مارک زاکربرگ، مدیرعامل متا، در یک تماس تلفنی خصوصی با دونالد ترامپ با پیشنهاد ایجاد یک نهاد نظارتی ملی و فدرال برای هوش مصنوعی به مخالفت پرداخته است.
⚙️
محورها و جزئیات کلیدی خبر:
🔹
پیشنهاد نظارتی به سبک FINRA:
این طرح که با حمایت دمیس هاسابیس (مدیرعامل گوگل دیپ‌مایند) و برخی مشاوران ارشد کاخ سفید مطرح شده، به دنبال ایجاد یک نهاد شبه‌مستقل ناظر (مشابه FINRA در بازار مالی) است تا مدل‌های پیشرفته هوش مصنوعی را پیش از عرضه عمومی، از نظر خطرات امنیتی و فنی ارزیابی و آزمایش کند.
🔹
موضع زاکربرگ:
مدیرعامل متا در گفتگوی ماه اوت خود با ترامپ تاکید کرده که هرگونه ساختار نظارتی باید با رویکرد «مداخله حداقلی (Light-touch)» دولت همسو باشد تا مانع رشد نوآوری و سرعت شرکت‌های فناوری آمریکایی نشود.
🔹
دو‌راهی دولت ترامپ:
کاخ سفید در حال حاضر بین دو گزینه مردد است: پذیرش مدل نظارتی مشابه FINRA یا انتخاب رویکرد صنعت‌محور و پیشنهادی دیوید ساکس (David Sacks) با حداقل سخت‌گیری دولتی.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2962" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2960">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1KzzZtff0rVViCUOcwq0OWiK8_5DOVl7QCtxMGp-D9K_VLWVzN1rb3P43HancEB_EH_CVnmpB-y8reg42B6BmoRxryqWo0acxmlzJ9Z1_OE4y82ARPcCgt_JA6cfO7yhu1DE6_sdv93yGSup3iqn_rd6sy66TAWuyvRqehZMLxHiCSghZY6B5DOQ9fp9Mx391tH3pP54gTiSb6QuyXk8UeavI71c2lo-ESmQTdlnyhCN8YiOsAM7EvXWSG_w0WaHRcAg-NX72NW1yMlOdgDSsHDePIix3nLpsKltpfE311m8CEFiqCli9QzP6Ic5dgl05P2Hg3M4VILtLqlDgLLhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
توصیه بابک زنجانی در الکامپ: گیر کلاهبرداری نیفتید
— بابک ولمون کن!
— بابک خجالت بکش!
— بابک حیا کن!
— بابک شعور داشته باش!
بابک زنجانی در قالب هلدینگ «دات‌وان» (با ۲۷ شرکت زیرمجموعه) در نمایشگاه الکامپ حضور یافت و از چند پروژه رونمایی کرد:
🔹
توکن و بلاکچین «دوتو»:
وعده پرداخت کوین به رانندگان تاکسی اینترنتی (بدون تاییدیه بانک مرکزی و بدون لیست شدن در صرافی‌ها).
🔹
سیم‌کارت و شبکه اجتماعی:
معرفی اپراتور مجازی «دات‌وان سل» بر بستر eSIM، پیامک انبوه و پلتفرم «مای دات».
🔹
پلتفرم معاملات طلا:
ادعای عرضه طلای ۲۴ عیار بدون حباب با ۱۹ لایه امنیتی.
⚠️
ابهام در مجوزها:
بانک مرکزی پیش‌تر اعلام کرده بود فعالیت‌های وی در بازار طلا و ارز فاقد هرگونه مجوز قانونی و نظارتی است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2960" target="_blank">📅 20:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2959">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDm32W0amgzyTXLgLN10mjf-u-tTwRnbmAxFDkXRfSoB9QkMtLQFH5Kjl_a0a6DCclWCCEXpFrcpVd1x8HaoHDDLKLLFljnD-wtkSwrn4Bvtpfb3fzmSS-8jAIlMxo1G4FL8ySzIGEaWmunTj0gSiLa2L5vsWf1K2Xcy8pdEhVfRNEnrnB3MrvZBl8QjhXTb1jvB6ogAnCjWCEOIkvVaUTFvSWxIS1VXH8wpFU4_W1lddWDSWvaB8ysT1b9OiHkyRTqlUgZM3XAA9H8JZVuFkT5xlqyDcvg3-woc-NFI8-izrRIxBDtxeIqqKSaZeqqXL5c5P99uy6C091SQI2ssXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
خاموشی هم‌زمان چت‌جی‌پی‌تی، گراک و کلاد
سه چت‌بات بزرگ و محبوب دنیای هوش مصنوعی شامل
ChatGPT
(اوپن‌ای‌آی)،
Grok
(ایکس‌ای‌آی) و
Claude
(آنتروپیک) به‌طور هم‌زمان دچار قطعی گسترده و سراسری در جهان شدند.
⚙️
جزئیات اختلال و سرویس‌های آسیب‌دیده:
🔹
دامنه قطعی:
دسترسی به رابط‌های چت، APIها، قابلیت‌های صوتی، تولید تصویر و بارگذاری فایل‌ها در هر سه پلتفرم با خطاهای گسترده روبه‌رو شده است.
🔹
اختلال در ChatGPT:
نمایش خطاهای مداوم و از کار افتادن سرویس ورود و جست‌وجو؛ این اتفاق هم‌زمان با انتشار پیش‌نمایش‌های مدل جدید
Astra
رخ داده است.
🔹
قطعی کامل در Claude و Grok:
سرویس کلاینت و کدنویسی Claude Code و همچنین چت‌بات Grok در وب، اندروید و iOS به‌طور کامل از کار افتاده‌اند.
🔹
علت نامشخص:
تاکنون هیچ‌کدام از شرکت‌ها دلیل دقیق این خاموشی هم‌زمان یا ارتباط احتمالی میان این اختلالات زنجیره‌ای را رسماً تایید نکرده‌اند و تیم‌های فنی در حال رفع مشکل هستند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2959" target="_blank">📅 20:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2958">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⭕️
قیمت آیفون ۱۸ پرو و ۱۸ پرو مکس لو رفت؛ افزایش ۱۰ تا ۲۰ درصدی به‌دلیل بحران حافظه
✍🏻
احتمالا با این وضعیت دلار و سودی که  دولت بابت ریجستری گوشی میگیره که در اصل یکی باید برای دولت بخری یکی برای خودت فکر کنم بالای نیم میلیارد پول این گوشی باشه تو کشور.
😐
بر اساس تازه‌ترین گزارش مؤسسه پژوهشی
ترندفورس (TrendForce)
در آستانه رویداد جدید اپل، پرچمداران سری پرو نسل جدید احتمالاً با افزایش قیمت ۱۰ تا ۲۰ درصدی نسبت به نسل قبل روانه بازار خواهند شد.
⚙️
پیش‌بینی قیمت‌ها و مدل‌ها:
🔹
آیفون ۱۸ پرو:
بازه قیمتی
۱٬۲۴۹ تا ۱٬۲۹۹ دلار
(در مقایسه با قیمت پایه ۱٬۰۹۹ دلاری آیفون ۱۷ پرو).
🔸
آیفون ۱۸ پرو مکس:
بازه قیمتی
۱٬۳۴۹ تا ۱٬۳۹۹ دلار
(در مقایسه با قیمت پایه ۱٬۱۹۹ دلاری آیفون ۱۷ پرو مکس).
🔹
آیفون تاشو (آیفون اولترا):
ورود به بازار با قیمت پایه
۲٬۰۹۹ تا ۲٬۲۹۹ دلار
و احتمال عبور قیمت قوی‌ترین کانفیگ از مرز
۳٬۰۰۰ دلار
.
🔍
علت اصلی گرانی؛ بحران و تقاضای هوش مصنوعی:
🔹
هزینه تامین تراشه‌های حافظه ۲۵۶ گیگابایتی به دلیل توسعه سنگین زیرساخت‌های AI در سطح جهان نسبت به سال قبل نزدیک به
۴۰۰ درصد جهش
داشته است.
🔹
هزینه تمام‌شده قطعات (BOM) برای یک نسخه پرو ۲۵۶ گیگابایتی حدود
۳۸ درصد افزایش
یافته که زنجیره تأمین اپل را تحت فشار گذاشته است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/2958" target="_blank">📅 18:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تو گوشیم فقط چراغ قوه بدون فیلترشکن باز میشه :)</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2957" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvJHxiZZDTYNnWc2RGr5HscaqaZD03qOmGSdiPrreGYZaPf3o-7G01h1ViO5vOm7ooqFoav4BplFJAPXSXw-F64MQxLeFT75yif451mYUDrjBfPEisuhUqgcyNB0exTdcqx5ZD96NXa9gjE7GI2OCMP36pt-O0J9PGZ5fRogJ3Stqj5Sj9hoH3Gv26S3u16LNgyAa30vaBqKCMn-Z9-0HiKsf4HFcED2F03F5yTqWyNpO3eTCMRP6CCt36j1b1UudMeqHAriiCUYYxRJVS9rYqgCFMwb5HQcwOsvjRCvM8dAeOeXhVZePN-Aqilb8gMm8IuDD65eFLIK7KmIzQ2jYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پنل همه‌کاره فیلترشکن (انواع هسته + تانل داخلی و مدیریت با هوش مصنوعی)
🚀
🔹
تو این آموزش یک پنل فوق‌العاده رو بررسی می‌کنیم که نه تنها از هسته های مختلف (مثل Xray و وایرگارد و OpenVpn و L2TP) پشتیبانی می‌کنه و تانل داخلی اختصاصی داره، بلکه به کمک هوش مصنوعی تنظیمات و کانفیگ‌ها رو براتون بهینه‌سازی و مدیریت می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/iaghapour/2955" target="_blank">📅 18:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2954">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🛡
چک‌لیست طلایی امنیت اینستاگرام؛ ۷ قدم تا ضدگلوله کردن حساب کاربری
با صرف چند دقیقه وقت و اعمال این ۷ تنظیم کلیدی، احتمال هک و نفوذ به اکانت اینستاگرام خود را به حداقل برسانید:
🔹
۱. تغییر رمز عبور یا فعال‌سازی Passkey:
استفاده از پسورد طولانی و ترکیبی یا کلید عبور هوشمند.
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Change password
🔹
۲. فعال‌سازی تأیید هویت دومرحله‌ای (2FA):
ایجاد لایه امنیتی قدرتمند؛ حتماً از اپلیکیشن‌های Authenticator (مانند گوگل یا مایکروسافت) استفاده کنید، نه پیامک (SMS).
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Two-factor authentication
🔹
۳. بررسی نشست‌ها و دستگاه‌های متصل:
مشاهده نشست‌های فعال و لاگ‌اوت کردن دستگاه‌های ناشناس یا مشکوک.
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Where you're logged in
🔹
۴. لغو همگام‌سازی مخاطبین گوشی:
جلوگیری از آپلود شماره تلفن‌ها و پیشنهاد اکانت به مخاطبان دفترچه تلفن.
📍
مسیر:
Settings and activity > Accounts Center > Your information and permissions > Upload contacts
🔹
۵. خصوصی‌سازی پیج (Private Account):
محدود کردن دسترسی به پست‌ها و استوری‌ها فقط برای دنبال‌کنندگان تاییدشده.
📍
مسیر:
Settings and activity > Account privacy > Private account
🔹
۶. حذف دسترسی برنامه‌ها و سایت‌های متفرقه:
قطع دسترسی ابزارها، ربات‌ها و وب‌سایت‌های شخص ثالث به اکانت.
📍
مسیر:
Settings and activity > Website permissions > Apps and websites
🔹
۷. عدم نمایش پیج در بخش پیشنهادات (Suggested):
جلوگیری از نمایش حساب شما در بخش اکانت‌های پیشنهادی به سایر کاربران (از طریق نسخه وب اینستاگرام).
📍
مسیر: ورود به وب‌سایت
instagram.com
> بخش
Edit profile
> غیرفعال‌سازی تیک
Show account suggestions on profiles
©️
پس‌کوچه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2954" target="_blank">📅 17:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2952">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVV1kw6c8GnomoBn8b-DSDq9XAi1xXBFmfuwkjs_3MMTGqjvIjyzNg-IOgXfwSqMCjG_CNFE8SeUAMfAPGAEVoQgKrUYPbUBU_SNUv8ikguVnZC3Vn_XuSqjgh6dc4INscZTDAI09Ql4sNlSUOiDIt-uq5NrRn6je022pNux2K4ax8PA-Juukadz1IMMJR9lPysIvCm0TlI2_kXT3rwnkPWx4M1AGN80feGUCybg5_5RdF2_rSB5L-f-SgflfhfmlA2HL8zKqQGgB439EyoH1k_eea3e4gnrI8f_h-0jurVjz2MJVOm7CPRIQEnxt31Ds1Rt5OrjnQt8qsHouYByGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جایزه قرعه کشی تحویل برنده عزیز شد.
سعی میکنیم از این به بعد با حمایت های شما هر هفته قرعه کشی داشته باشیم.
👤
آیدی pinkpantheranim عزیز، مبارکتون باشه!
✨
راستی فردا هم یه ویدیوی عالی داریم که تو اونم براتون هدیه در نظر گرفتیم!
🎁
💚</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2952" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2951">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFcbLHBJobAa7vgezkjX8HpmDbg4HvHkyugpLTLvRds0l8-Fk-86lvJC5yyRnzfO2uS2_A1stnQ-uYN-kVJlGCQkYFXuFFBPl6DWbSYhV6_AbIBgcCL9ykt7mRpODlZc1p3yQ19wxnNrtJNcluP6yQUott_L-muMI-7V13w7U4lBS_z01HwIMhVz9Ti4NHSh6oiUHRXqkJQcjGJiJfKzRS8r_oOnHhoQAS8_jdHftGuSiQ0SgPg4Srs0aKxLA74yawdx0YPcisEa8xImC80ET063TfsWpIvzmkujCSiP3iBJLx9S4U3h78TGF2vbsIXxiEe7aY-bpxm0slrwm0Gf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنتر ها است.
در این طرح شماره موبایل + شماره ملی + آی پی به هم وصل می‌شوند و بدون ثبت آی پی در سامانه شاهکار دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©️
Saeed Souzangar</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/iaghapour/2951" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2949">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnpBsoMZEXu293nD3gVFdvGpWzMI9Yzx48Ez-mUuSwu7N_4hDDZCks0HidgSpmRG9_6pOwtOb1k9vREpx9fZzf700qNgSvqZ25kVhFCiNdYVmWxKpYQYoQH1n79gxSH13H2UqcrOxHkFAy9t-6bo-Uns0cUSCtlNazqbwPD1UPfzzDD1F7Q6rtDSL1uYwtO8QcY7NWdlbIbo1bfPiBtF5mx-BEQEXKq_KxlLVnvP4_t1VkHldmR240glLUwIZ3Go7X3d8rXjqwtDqwpeLuTytvoDoQ1_LlP6O8ve9o4mLa6qFy1pRzW9PHhqw1hq7CQ2jUDOEECX620VQa_l_PZdZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معاون وزیر ارتباطات: گران‌فروشی اینترنت احراز نشده است / فیلترشکن‌ها منشأ اصلی حملات سایبری هستند
محمد حاتمی‌زاده، معاون حقوقی و امور مجلس وزیر ارتباطات، در جمع خبرنگاران پیرامون ادعای تغییر حجم و قیمت بسته‌های اینترنتی توسط اپراتورها و چالش‌های امنیتی شبکه توضیحاتی ارائه داد.
🔹
عدم احراز گران‌فروشی اپراتورها:
علیرغم دریافت گزارش‌های مردمی و بررسی اسناد توسط سازمان تنظیم مقررات (رگولاتوری)، تا این لحظه وقوع تخلف یا گران‌فروشی بسته‌های اینترنت اثبات نشده است و نظارت‌ها همچنان ادامه دارد.
🔹
فیلترشکن‌ها؛ حفره امنیتی و اقتصادی:
استفاده گسترده از فیلترشکن‌ها به ساختار شبکه مخابراتی ضربه زده، باعث نارضایتی کاربران شده و ریسک‌های امنیتی بزرگی را به کشور تحمیل کرده است.
🔹
منشأ داخلی حملات سایبری:
به گفته وی، بیشتر حملات سایبری ثبت‌شده در کشور از طریق بستر همین فیلترشکن‌ها و از داخل خاک کشور هدایت و انجام می‌شوند.
🔹
محدوده اختیارات وزارت ارتباطات:
تمرکز این وزارتخانه صرفاً بر اقدامات و مدیریت فنی است و ساماندهی کامل این فضا نیازمند همکاری نهادهای امنیتی و نظارتی است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/2949" target="_blank">📅 21:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2948">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFVtGAiOgzsjr0DFG6el2hC_DcQajrvJ__MhPv6zDqr36a23mPils8ahvunS1g3uxEVfZh0mxk1DfhnTI2BADljPO_QBJqGlXKfBpDxQhtNxtAOO02YQjChfA2kXmVzyscKLLXy1RcAnwBr-ypIO9KXMDsyMl4ygoC99qnyvLNGYQZ8lX9urZRw5kX568atOAQ3tzeHplGdBmDqm4et9R3AVJlHvg4TkxZWoNx4MQbZlC42ZJnJDrWuCOaf32KlYgxBNXlU9rxN3G4WUFZW8ulFy6CfJkEVNcYYYl1SvGWEdI644Ms0dqm8Bf69zjG5KMRHTCjt7dfrd0XSROQu82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌸
تقدیر و تشکر از یک همراه همیشگی کامیونیتی | مارک عزیز
در روزهایی که دسترسی آزاد به اینترنت و سرویس‌های پایه برای کاربران و توسعه‌دهندگان ایرانی به یک چالش روزمره و فرسایشی تبدیل شده، حضور افرادی که بی‌سروصدا و بدون چشم‌داشت برای رفع این موانع تلاش می‌کنند، غنیمتی بزرگیه.
امروز میخوام از
مارک
عزیز صمیمانه تشکر کنم. کسی که شاید خیلی از ما اون را نشناسیم یا از حجم فعالیت‌هایش بی‌خبر باشیم، اما مارک همیشه حامی دسترسی آزاد به اینترنت بوده.
مارک عزیز، از طرف کل کامیونیتی، بچه‌های شبکه و همه اونایی که نتیجه زحماتت بهشون می‌رسه، بهت خسته نباشید می‌گیم. واقعا مرسی که اینقدر دلسوزانه پیگیر کارها هستی. دمت گرم که همیشه هوای بچه‌ها رو داری!
💚
✌️
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/2948" target="_blank">📅 19:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2947">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⭕️
موضع دفتر رئیس‌جمهور درباره فیلترینگ: دوره محدودیت و اینترنت طبقاتی گذشته است
سید عباس موسوی، سرپرست معاونت سیاسی دفتر رئیس‌جمهور، در گفت‌وگویی مواضع دولت پیرامون رفع فیلترینگ، اینترنت طبقاتی و فناوری‌های نوین ارتباطی را تشریح کرد.
🔹
پایان دوره فیلترینگ با پیشرفت فناوری:
با گسترش فناوری‌هایی نظیر اتصال مستقیم گوشی‌های همراه به اینترنت ماهواره‌ای، سیاست‌های اعمال محدودیت و فیلترینگ دیگر کارایی فنی ندارند و دوره آن گذشته است.
🔹
رد کامل اینترنت طبقاتی و تجارت فیلترشکن:
تداوم محدودیت‌ها در زمان صلح، ایجاد دسترسی‌های طبقاتی به اینترنت و شکل‌گیری بازار فروش فیلترشکن به‌هیچ‌وجه قابل قبول نیست.
🔹
تفکیک شرایط جنگی از زمان صلح:
اعمال محدودیت‌های مقطعی ارتباطی صرفاً در شرایط اضطراری، بحران‌های امنیتی و جنگی برای مقابله با تهدیدات سایبری توجیه‌پذیر است، نه در شرایط عادی.
🔹
رویکرد پیگیری رفع فیلترینگ:
پیگیری موضوع رفع محدودیت‌ها در جلسات تصمیم‌گیری بدون ایجاد تنش و بر پایه اقناع و وفاق انجام می‌شود./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2947" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2945">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=Gn-iQEN-fbVTwk0gCzV01d_xJHy92yETG6MOhUGk2fYFMUaRromSUqZJCUUiksGry0PcaVovLKWLxTx4bVdf9HKdjT7hzni3dZrm0kZdd8gDo7J-LBtBRDK8uNBYeFiuVV9sIel2ohUl8WiK3BGQi88euv-tBXbf0BiDqfybMJkxq4Ike5FI3HwPOIK5ryBHIZkF2gJRw8rVflmWu4UfsElCEPX-EY22qwdcEE0D2qLeoIIyWQO6ZpRBZSX2L_16vmyOK04pH_T3MlowF0ImJU8Wf44RyI8FsCRhLfCbqCPuonG1qpEbuZ1khhonOE3nT5fXWvWeSzS2bm8FUA5UjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=Gn-iQEN-fbVTwk0gCzV01d_xJHy92yETG6MOhUGk2fYFMUaRromSUqZJCUUiksGry0PcaVovLKWLxTx4bVdf9HKdjT7hzni3dZrm0kZdd8gDo7J-LBtBRDK8uNBYeFiuVV9sIel2ohUl8WiK3BGQi88euv-tBXbf0BiDqfybMJkxq4Ike5FI3HwPOIK5ryBHIZkF2gJRw8rVflmWu4UfsElCEPX-EY22qwdcEE0D2qLeoIIyWQO6ZpRBZSX2L_16vmyOK04pH_T3MlowF0ImJU8Wf44RyI8FsCRhLfCbqCPuonG1qpEbuZ1khhonOE3nT5fXWvWeSzS2bm8FUA5UjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره هفتم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی pinkpantheranim مبارکتون باشه!
✨
✍🏻
با تشکر از اسپانسر عزیز این قرعه کشی.
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در ویدیو بعدی باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2945" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2944">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎮
ویدیو مقایسه جذاب GTA 6 با GTA 5؛ جهش خیره‌کننده گرافیک و گیم‌پلی بعد از ۱۳ سال
با نمایش گیم‌پلی بازی موردانتظار
GTA 6
، مقایسه‌های فنی میان این نسخه و بازی محبوب GTA 5 نشان‌دهنده یک ارتقای نسلی و عمیق در استانداردهای بازی‌های جهان‌باز راک‌استار است.
🔹
جهش چشمگیر گرافیک و جزئیات بصری:
بهبود محسوس در طراحی چهره، فیزیک و انیمیشن موی کاراکترها، سیستم نورپردازی پیشرفته، ارتقای کیفیت بافت‌ها (Textures) و ارائه پوشش گیاهی و محیط‌های شهری فوق‌العاده زنده و واقع‌گرایانه.
🔹
انیمیشن‌های طبیعی و گیم‌پلی واقع‌گرایانه:
طبیعی‌تر شدن فیزیک حرکات شخصیت‌ها و تعریف استانداردی نوین در زمینه تعامل با محیط، اکوسیستم شهری و واکنش‌های هوش مصنوعی NPCها (شخصیت‌های غیرقابل‌بازی).
🔹
پلتفرم‌های مقصد و قیمت‌گذاری:
نسخه استاندارد با قیمت ۸۰ دلار و نسخه آلتیمیت با قیمت ۱۰۰ دلار در دسترس پیش‌خرید قرار دارند.
📅
تاریخ انتشار رسمی:
۱۹ نوامبر ۲۰۲۶ (۲۸ آبان ۱۴۰۵)
برای کنسول‌های پلی‌استیشن ۵، ایکس‌باکس سری ایکس و ایکس‌باکس سری اس. /منبع:sargarme
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/2944" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2943">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRTXdOwpAI5aWLobVp06PQkZSsMr6JG7PEtiLKRnInGYSMqpgIR7TB8hk8nlnly-qmg2cxVJK9Yw0QpNagb4wZTBPLJEkQRjU6iRnQd0JjVzGSzJtdA0Sb_gmC8KG1IHocdjkWqcwCdWZjcdbqeWMydiY02VFZm07iQofbB8Qhox9tsEcROgY9CiW_MUpH8Sdx3rWCLceFs298nq_87GQXd6IQoApFvDsvCzkRcYx2q7e_l9_2WMGfpwN2MRAa3zeGvuy-3PM9Vskg-tuMHUelaMjgNQWSw2gsv6w1mi7-xTKdpOJiyHRUUcUvOk8A7zmoXOByleA9SlyKM_UFRHeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی PingTunnel VPN Client؛ کلاینت ویندوز برای پروتکل ICMP
پروژه
PingTunnel-VPN-Client
یک کلاینت مدرن تحت ویندوز (WPF) است که با ترکیب
pingtunnel
،
tun2socks
و آداپتور
Wintun
، امکان عبور دادن کل ترافیک سیستم از بستر پکت‌های ICMP (پینگ) را فراهم می‌کند.
🔹
مانیتورینگ و نمایش زنده ترافیک:
نمایش لحظه‌ای سرعت دانلود و آپلود تانل به همراه مصرف کارت شبکه فیزیکی و سیستم لایو لاگ (Live Logs).
🔹
امنیت DNS و بهینه‌سازی ترافیک:
مجهز به فورواردر و کش داخلی DNS جهت جلوگیری از نشت DNS (DNS Leak Protection) و مسدودسازی UDP روی اینترفیس TUN جهت جلوگیری از خطاهای ناشی از ترافیک QUIC.
🔹
پایش سلامت و اتصال پایدار:
بررسی مداوم تاخیر (Latency) با قابلیت ری‌استارت خودکار در صورت افت کیفیت، به همراه سیستم بازیابی پس از کرش و پاک‌سازی رول‌های فایروال.
🔹
قابلیت Split-Tunneling:
امکان مستثنی‌کردن ساب‌نت‌ها و رنج‌های آی‌پی مشخص جهت عبور مستقیم ترافیک بدون رفتن به داخل تانل.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/iaghapour/2943" target="_blank">📅 18:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2942">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grGPDuprMrL4bW2LsMMy1Fzw0jLDOMfM-aGiuw4Of_f5nZV3EDZKNBBkh1HLMkXVHuSABd4o8GxEtV1T2ZFztvyP4fOdb_Z6IhUwWb8kTEBFThQbQmagXyivCAwA-KS9dsNAEe9nUGeHKWygIB80Gi8S_6FOem6pTQ4ASHDBqCOvz38ApcnjLRR21N4ixC231iH7EfYxZ9IA0nVhkgs56eEqp0cmrdsqzuydncG0oS3xX7Wq8p4IxHUQEfNIrpXgr0VbpXm_gC5VhFseP6CNXSq3pxVjcf8WM_qcn5L_eENauaHCC8OKGeHVEY-Z2Lq0aO57cBHx_IJdHWla4XCsVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مقایسه WiFi 6 در برابر WiFi 7؛ کدام نسل در سال ۲۰۲۶ ارزش خرید دارد؟
با گسترش روترهای
وای‌فای ۷
انتخاب میان خرید یک روتر جدید نسل ۷ یا یک مدل مقرون‌به‌صرفه نسل ۶ به یکی از دغدغه‌های اصلی کاربران شبکه تبدیل شده است.
⚙️
تفاوت‌ها و مزایای اصلی WiFi 7
:
🔹
پشتیبانی از فناوری (Multi-Link Operation):
ارسال و دریافت همزمان داده‌ها روی سه باند ۲.۴، ۵ و ۶ گیگاهرتز که پایداری ارتباط و سرعت را به‌ویژه در محیط‌های شلوغ به اوج می‌رساند.
🔹
افزایش پهنای باند کانال تا ۳۲۰ مگاهرتز:
دو برابر پهنای‌باند WiFi 6E که برای استریم محتوای 4K/8K و کاهش تاخیر ایده‌آل است (در مدل‌های پیشرفته سه‌بانده).
🔹
سرعت تئوری و برد بالاتر
و
سازگاری کامل با نسل‌های قبلی
دستگاه‌ها و تجهیزات قدیمی.
🤔
آیا خرید WiFi 6 هنوز منطقی است؟
🔹
بخش زیادی از لپ‌تاپ‌ها و گوشی‌های فعلی هنوز از پهنای‌باند ۳۲۰ مگاهرتزی یا سه باند همزمان پشتیبانی نمی‌کنند.
🔹
برای کاربردهای روزمره، استریم و سرعت‌های معمول اینترنت، یک روتر باکیفیت WiFi 6 کافیه./شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/2942" target="_blank">📅 18:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2941">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgmSbiaWnCoxAV19sw6huVTutwHdsSy_onAqS5-2Emrr9SEzscBy9AqQ1dWHThgKf82UsZ6h0YXFJzNT9xBeyLisTcNcuzFrm91rzNkZ5BKsp6QC0tDKAjaI_SW2tXdNZOGms82gisyhX1jbzMdRp7TVqWVk7LUKflWGd0zn595PiJ1C9Rja1F-fsZMst5tftNl2K80hwPLjt410DMRIPGsX42h1FvMTnuo6CQSiI4RAzhLggyKhi239u6CCvpu1DexsasYnCVLbMcfDDROItvyAgvlU15SL65AK9kLfBBIJPdKumHB3ogaet7mp8oW9yE2jDof2DdRLWrh3O_g15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
گوگل در حال آزمایش هوش مصنوعی Gemini 3.8 Flash
بر اساس گزارش‌های فاش‌شده، شرکت گوگل فاز آزمایش داخلی نسخه پیش‌نمایش مدل جدید
Gemini 3.8 Flash Preview
را روی پلتفرم کدنویسی اختصاصی خود موسوم به
Jetski
کلید زده است؛ اقدامی که از احتمال انتشار عمومی آن در آینده بسیار نزدیک خبر می‌دهد.
🔹
پیشرفت چشمگیر نسبت به نسل قبل:
طبق ارزیابی‌های اولیه کارکنان، نسخه ۳.۸ فلش عملکردی به‌مراتب بهتر و ملموس‌تر نسبت به ۳.۷ فلش در سناریوهای مختلف ارائه می‌دهد.
🔹
تمرکز ویژه روی مدل‌های اقتصادی و پرسرعت (Flash):
در حالی که مدل‌های سنگین پرو در دست توسعه هستند، گوگل تمرکز اصلی خود را روی بهینه‌سازی مدل‌های ارزان، سبک و پرسرعت سری فلش برای کدنویسی و توسعه دستیارهای هوشمند (Agents) گذاشته است.
🔹
سرعت سرسام‌آور چرخه انتشار:
پس از عرضه نسخه ۳.۶ در اوایل تابستان و معرفی نسخه ۳.۷ تنها با فاصله ۳ هفته، اکنون نسخه ۳.۸ وارد فاز تست شده است.
🔹
رؤیت در بنچمارک‌های جهانی:
شواهد نشان می‌دهد که ردپای تست‌های آزمایشی این مدل به‌تازگی در وب‌سایت معتبر ارزیابی هوش مصنوعی
Arena AI
نیز مشاهده شده است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2941" target="_blank">📅 16:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2938">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJa87jEeVGzZQAg60Wby9LgbAhZvgQARwQ2OIJVGh5j4C3BzxWhYOCX5d7HmIPSwLAg8i6pP3PEQY30lvenvYZAUrkhBTZr84eOongiI8zRWP07hf09gd_alhOhtbnW8ZqZBTedEwsU1bOZ0YrebABaboV_fKZbJ-cmvDRgB85Vcu6OigOnPwJl0oYdomQLpcj9LLdtGqLdkXlmQuhehmbaZ-jILL0075ro2M-6iG3EDRfkInQyIek7H-1fj12kX_uSDkBSP72g8MP6-iKdftJpMBMYFa-uT9Ai_OomdRAE1_pI9iAsN38_ITJcVCUi_qqJRC0R4tp6o0JREowO47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRlwYOvpPjB0WoULKKZ3fK9b-VIQ_4czJcOzn3TAIH3088ceyYamM8jPa9gvEw_KhLQ0wpL0tQGUC1o9Kl_8OQTlsYvX9SYDhp6iYNlKmaX8fbZqRhQ8Vy4coF8rVgjnliQ8EzVK1loxbnVwttJT5GKJOcAb0eYm3AkpoO8A3XQVq7S4qp6NsDXhfLLGVUNYt6EraYGduIFGvNDlzdBdPGZQjkufhC9xXUzIC5ZbJu5NmxdXjeNJTs2MWqdf2SFZoXGMYTUMST27JA5KiKMv89iO7AsxTtIkPZWCV7x2BpVrw4vmjHTT4vDB_8OsGSpndSWAn_O6Dpnv6cWqOLuQag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎮
فناوری DLSS 5 انویدیا پیش از عرضه رسمی لو رفت
تصاویر فاش‌شده از نسخه آزمایشی و اولیه
DLSS 5
انویدیا روی بازی‌های کامپیوتری نشان می‌دهد که این فناوری رندر عصبی هنوز تا رسیدن به استانداردهای مطلوب فاصله زیادی دارد.
🔹
تغییر رویکرد در آپ‌اسکیل:
برخلاف نسل‌های پیشین که تمرکز روی افزایش شفافیت تصویر بود، DLSS 5 با بازتولید هوش مصنوعی تلاش می‌کند متریال‌ها و نورپردازی را بازسازی و فوتورئالیستی کند.
🔹
نتایج عجیب و غیرطبیعی روی چهره‌ها:
در تست‌های اولیه روی کاراکترها چهره شخصیت‌ها دستخوش تغییرات سنی نامتعارف شده و ترکیب این چهره‌های تغییریافته با انیمیشن‌های حرکتی ثابت بازی، حس غیرطبیعی و ناهماهنگی ایجاد کرده است.
🔹
افت FPS:
فعال‌سازی قابلیت رندر عصبی در بازی Control روی کارت گرافیک
RTX 5070 Ti
در رزولوشن 4K، فریم‌ریت را از
۷۱ فریم‌برثانیه به ۳۵ فریم‌برثانیه
کاهش داده است.
🔹
نسخه رسمی DLSS 5 برای پاییز برنامه‌ریزی شده و باید دید انویدیا تا چه حد می‌تواند با بهینه‌سازی نسخه نهایی، مشکلات افت پرفورمنس و رندر غیرواقعی را برطرف کند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2938" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2937">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovKC3AaLdlHbJfj8Xxp48DN6XyIh0Pq_EiEJX6vQizUv6yV2LwJFidqj8MxvhCO0_F7VhGDTf0fRlepIpF3vCVeCK8aFrjgQ-hMApfiptuvbyD7o_Ufk1ol78T6eq35a6QrqlQMriQ17pxNnBhBRGH6XfJH3C9SkBiz92uEoYDp1fO4w_XlRLoc-T_NLOKULSk0FZsjYRAHp9_RV5HeLU6BTVrELxS3DfERJtEgers1zLVdPMgJl0HkiIm3fLZA6ga4AeLImnr0xYel-q8-Tig0yaqpWPp1QYeRB2NkrrGCjuwN81TTIPBX4fPRYWC5KbKhQELXFMfiJ-7nKGAowgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
توقف کامل آزمون زبان دولینگو (DET) برای تمام دارندگان مدارک ایرانی از اول سپتامبر
بر اساس اعلام رسمی پلتفرم
Duolingo English Test
، از تاریخ
۱ سپتامبر ۲۰۲۶ (۱۰ شهریور)
، دسترسی به این آزمون برای تمام متقاضیان داخل ایران و همچنین افراد دارای مدارک هویتی ایرانی متوقف خواهد شد.
⚙️
نکات و جزئیات مهم این تصمیم:
🔹
محدودیت فراتر از موقعیت جغرافیایی:
این تصمیم صرفاً مسدودسازی IP یا موقعیت مکانی ایران نیست؛ بلکه تمام افراد دارای مدارک هویتی و پاسپورت ایرانی (حتی در صورت سکونت در خارج از کشور) امکان احراز هویت و شرکت در آزمون را نخواهند داشت.
🔹
تاثیر بر مهاجرت تحصیلی و اپلای:
با توجه به پذیرش مدرک دولینگو در بسیاری از دانشگاه‌های معتبر بین‌المللی، این تصمیم فرآیند اپلای متقاضیان ایرانی را دچار چالش جدی می‌کند.
🔹
پیشنهاد به متقاضیان:
متقاضیان ادامه تحصیل باید پیش از هرگونه اقدام، فهرست مدارک زبان مورد تایید دانشگاه مقصد را بازبینی کرده و آزمون‌های جایگزین (مانند آیلتس یا تافل) را در برنامه خود قرار دهند./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2937" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2936">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOQzKhV78DOVA2ufW5IczYWZl06cyTZRTgt589JEfHo5Fr0I5lYibRl-lFH3u8sKzrG6bLFrA7MS3s_boaoJOHLFpFldINrz4Wc2ZZ9NxqoHu_kZcuBEXGsgOAAw8Rfa3Gy7Wnt07QlzE5Z6mhCitqApLpUzqkfe9wY5ky9HXQpElQfZtsYpCaCPs9dohVtBCCbaBcStB2qPsLcfYtCKAuDPXLkav17N_SJAYnlly_V_4EqGGlxEsfRHdhahzNvAAOl3nRLbeKiTZs4E7nZCZKjM1s1qe3ItAR-XYFByr7Pb7zzO4prfnz4loG6fqBqHj2vxIk3OEmDlPrw0KnB_8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل مدیریت نمایندگی و ادمین برای 3X-UI
پروژه
x-ui-reseller-panel
یک واسط تحت وب مدرن است که به مالکان سرور اجازه می‌دهد بدون دادن دسترسی مستقیم به پنل اصلی، دسترسی‌های مدیریت‌شده و تفکیک‌شده به نمایندگان بدهند.
🔻
امکانات اختصاصی ادمین:
🔹
ایجاد، ویرایش و حذف اکانت‌های نماینده
🔹
تخصیص سقف ترافیک اختصاصی برای هر نماینده
🔹
محدودسازی دسترسی هر نماینده به اینباندهای مشخص
🔹
مانیتورینگ کاربران آنلاین و آمار مصرف ترافیک زنده
🔹
پشتیبان‌گیری از دیتابیس پنل و پشتیبانی از تم تاریک و روشن
🔻
امکانات پنل نماینده
:
🔹
صفحه ورود مستقل برای هر نماینده
🔹
ساخت، ویرایش، حذف کاربر و ریست حجم مصرفی
🔹
باطل کردن لینک اشتراک (Revoke Subscription)
🔹
مشاهده کاربران آنلاین و حجم باقی‌مانده
🔹
همگام‌سازی خودکار ترافیک با پنل اصلی X-UI
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2936" target="_blank">📅 14:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA4r2QYHhx94LTiUy-3LbmmekG8WRvmjVOCIt4mpHX910eFVuRrYicXqbGmEH21CJc_qoeLWmXLCWfbHEJXnQ9LAO8vp4202WMe15KXV-sa0wFCJsO_oXfYmxAzaxkdCkYkpbzdUylY94OGwKoJpZ71dEmw-xbOdktfFHoJ0-NGPLhQGCh2DrZjOwdDKMv18P91PP4QT0uh_Wuep5otoNf_VMqkN_NkkqARqfoUcTrbmBesGNA36bYFCmFFwd19mgQoWs9ibshcCxDjh8-Y5yeKtyIUvWa7mODxqeqn5a5puo0SNh4QkPW7Ke1HceKz7e5K-MPtDSWgR6ibsu9nDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ربات فروش خودکار کانفیگ تلگرام (جایگزین ربات میرزا) + آموزش راه‌اندازی
🔹
اگه دنبال یک راه بی‌دردسر برای اتوماتیک کردن فروشتون هستید، این ویدیو دقیقاً همون چیزیه که بهش نیاز دارید. تو این آموزش یک ربات تلگرامی فوق‌العاده رو بررسی می‌کنیم که تمام مراحل تحویل و مدیریت رو براتون به صورت خودکار انجام میده و از تمام پنل ها پشتیبانی میکنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#ربات
#فروش
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2934" target="_blank">📅 18:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuEUaGjGfvdcFcBso0cJIWogxat3YTXPM9fJ1gblMw4xAeoV18G1JThhNjfEwSGSpCiXYU9s7EhmeLqYVgU5bm1Ad4ugQK5ALC6xrZW6uWTqWhtf3PDS0WSs_QcCh3-alcGxcp3Qlt2SAb9pla8C33Rdg_oStuMlKrqfrcWtoS1ZqTsYeM4pcQkdGzy9QrKYCVR3L7ihT_PB03V8wxYLJ80RPzEdxq3xKrccmeu0rjaRcpYQZ3B3eRX652kCc7CVBQionXWMm1bPTADtE9e1K6N0gvA_peST3J7KH2tyAyelY1pRNXvAJ4Ba6CV_CFExfkqX6H9giBrgM834X4ll4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شناسایی شبکه گسترده افزونه‌های جعلی فایرفاکس برای سرقت رمزارزها
محققان امنیتی شرکت
Socket
شبکه‌ای سازمان‌یافته شامل ده‌ها افزونه مخرب را در مرورگر فایرفاکس شناسایی کرده‌اند که با هدف سرقت کلیدهای خصوصی و عبارت‌های بازیابی (Seed Phrase) کاربران وب ۳ طراحی شده‌اند.
⚙️
روش کار و جزئیات این حمله:
🔹
جعل هویت کیف‌پول‌های معروف:
این افزونه‌ها نام و رابط کاربری ولت‌های معتبری مانند
OKX
،
Rabby Wallet
و
TronLink
را شبیه‌سازی کرده و بلافاصله پس از ورود اطلاعات توسط کاربر، کلید خصوصی را به سرورهای مهاجم ارسال می‌کنند.
🔹
تغییر ماهیت بعد از جلب اعتماد:
تعدادی از این افزونه‌ها ابتدا ماه‌ها در قالب ابزارهای نمایش نتایج زنده فوتبال و بسکتبال، تم تاریک، پسورد منیجر یا وی‌پی‌ان فعالیت می‌کردند و پس از جذب نصب بالا و امتیاز مثبت، با یک آپدیت مخرب به بدافزار سرقت دارایی تبدیل شدند.
🔹
ابعاد کمپین:
کارشناسان موفق به ردگیری ۷۷ شناسه مرتبط شده‌اند که مخرب بودن حداقل ۴۰ مورد آن‌ها به‌طور قطعی تأیید شده است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/2933" target="_blank">📅 15:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2931">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDpbbhIGRqaWsnqjiF1N9K8N9UC-iZ6sx9Ij6F2PbUgHiJutZOhcPVfPfYj8uAzt_rMin5rdN9Ylxj2R-kbKcrt-GZyM8DsYpz098c4-phu8sYCApV91B-GJva0K8tWXb78Vbzwys-f4AexEX6ZMtfF-7fZt9N97eqLmbLn3Skw81h9PPsgBKH9ZYPj315NlN2wZXv_7gmJCNY5ZEIGHdZ_BF8x9XWACVc-z1ewDx6CzEhDygw1MzEhFRJktteIBmFzRWEB5cL-9XKMwEv0AtbE96seWbK5d0gRYI_YMWrP81lVJ9ip7RfDk7tD5iUKSm9TPTlVJuXiSSAt2jnv8IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
لطفاً برای هر ایده ساده، اسکریپت جدید نزنید!
✍🏻
دم همه‌ی دوستانی که توی این یک سال اخیر با کمک AI اسکریپت‌های کاربردی نوشتن و به بقیه کمک کردن گرم. ولی یکی دو تا نکته هست که باید بهش دقت کنیم:
۱.
فورک‌های بی‌مورد:
لازم نیست هر فیچری که حس می‌کنید یه پروژه کم داره رو سریع فورک کنید، بهش اضافه کنید و با یه اسم جدید بدید بیرون! با این کار فقط کامیونیتی تیکه تیکه میشه و کلی ریپوی نیمه‌کاره و بدون پشتیبانی روی گیت‌هاب رها میشه. اگه واقعاً ایده‌تون کاربردی و درسته، بهتره همون رو به صورت Pull Request برای نویسنده‌ی اصلی بفرستید تا روی سورس اصلی مرج بشه.
۲.
تمرکز روی نیاز واقعی، نه هر ایده‌ای:
لازم نیست هر چیزی که به ذهن می‌رسه رو با عجله کد بزنیم و فکر کنیم حتماً به درد همه می‌خوره! مثلاً واقعاً نیازی نیست برای یه دستور ساده‌ی Iptables بیایم اسکریپت نصب آسان بنویسیم.
۳.
مسئولیت نگهداری و امنیت:
ساختن اسکریپت با هوش مصنوعی شاید با چندتا پرامپت ۵ دقیقه زمان ببره، ولی پشتیبانی، رفع باگ‌ها و حفظ امنیتش کار راحتی نیست.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2931" target="_blank">📅 20:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2930">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⭕️
طرح جدید «نظام‌بخشی فضای مجازی»؛ از جریمه ۱۰ درصدی درآمد تا لغو مجوز پلتفرم‌ها
پیش‌نویس سند «طرح نظام‌بخشی فضای مجازی» با هدف تفکیک وظایف تنظیم‌گری، تعیین مجازات برای پلتفرم‌ها و تعریف حقوق کاربران نهایی شده است.
🔹
تفکیک وظایف تنظیم‌گری میان نهادها:
مدیریت اینترنت، کلاود و دیتاسنترها به وزارت ارتباطات؛ پرداخت‌ها به بانک مرکزی؛ ضد انحصار به شورای رقابت؛ صوت و تصویر فراگیر به ساترا؛ و اخلاق و ایمنی الگوریتم‌ها به سازمان ملی هوش مصنوعی سپرده می‌شود.
🔹
ضمانت اجراها و مجازات‌های سنگین:
شامل اخطار، انتشار عمومی تخلف، محرومیت ۱ تا ۳ ساله از تسهیلات،
جریمه نقدی ۱ تا ۱۰ درصد از درآمد سالانه
، تعلیق و در نهایت لغو کامل مجوز فعالیت.
🔹
مهم‌ترین مصادیق تخلف پلتفرم‌ها:
نقض حقوق کاربران، رفتارهای ضد رقابتی، عدم احراز هویت معتبر کاربران پیش از ارائه خدمات، خودداری از ارائه اطلاعات به تنظیم‌گر و عدم رعایت مصوبات قانونی.
🔹
به‌رسمیت شناختن حقوق کاربران:
تاکید بر «حق دسترسی به شبکه»، ممنوعیت قطع یا دستکاری ترافیک بر اساس اصل «بی‌طرفی شبکه (Net Neutrality)» و رعایت رده‌بندی سنی و حقوق کودکان.
🔹
سامانه حکمرانی مشارکتی:
الزام به انتشار پیش‌نویس مصوبات ۲ هفته پیش از تصویب جهت نظرخواهی عمومی از مردم و کارشناسان در یک سامانه هوشمند./
مقاله کامل
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/2930" target="_blank">📅 20:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2929">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHFq_Y7EV-pOhxoiLAwTFKN7x4cLs9LYkGjtOamDnk0RFouu4opH7K8eVhv7kIO0-GtLLL3Ff9u1gemKgWeLfSDNEsWZjp-sN-MF23vdiP3o8fdEbLRSkZ3T3IY7gCuM148QqfMFk4a3g36PLUM5hyFcuO8VynHVKazs5OwKsvl7NX_DmFp1Sop0shRaSDXp0q4kKDaeu_WMwvqbvjh1JCdZ-cBEPcg0ydA0cCDaZFgE3NOpavybtlM7qAgLzvDpl1DtPwumgEozpFr3pgNKWWDOcHD_kzehXhL-duYB1ZmNW6DP76n1Nsm9EzvmpsOLlIA67n2q_41z4gZU16QJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی تانل سبک و بهینه Netlink Tunnel
پروژه
Netlink Tunnel
یک ابزار تانلینگ سبک، بهینه و کاربردی است که امکان مدیریت کامل و سریع تمام اتصالات را از طریق خط فرمان (CLI) فراهم می‌کند.
🔹
تشخیص قطعی و پایداری بالاتر:
واکنش سریع‌تر سیستم در شناسایی قطع ارتباط و اعمال Reconnect خودکار.
🔹
مانیتورینگ و آمار ترافیک Live:
نمایش لحظه‌ای حجم دانلود، آپلود و مجموع ترافیک مصرفی.
🔹
گزینه Optimize:
ابزار اختصاصی بهینه‌سازی پارامترها و تنظیمات شبکه.
🔹
پشتیبانی از پروتکل‌های متنوع شامل TCP، TCP Mux، حالت‌های مخفی‌ساز TCP Stealth و TCP PCK
🔹
پشتیبانی از اتصالات وب‌سوکت WS / WS Mux و WSS / WSS Mux
🔹
انتقال پایدار روی بستر UDP + FEC (تصحیح خطای رو به جلو)
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2929" target="_blank">📅 14:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2927">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ats_ARyhCey8YggbzbBAtJ-cjAGUaqTk78GUs70XyDL0w63hYwI3Ef2HfuF3TxdlQRiwGYvXvRGwdZefuWJ66tnvgYtGKIhrdbGTfiMKPaMnIqGqcngemcN3gg-1rj8eso7tpsvP5HpK-uxLHXEHV8Ih7wf-O7OR-JONKJYg0M7cuFUcq3cvOt5l2N34N8uiAMfRqNwApIr1bB8YNLw4oT7u0HNTlFwtqc-BWHPeenRsjjrB8Ne0MhTZ8g32F4atSpXrD360uWKa9exShpEb0ewGswjf4zRZ5pXFUs-QA5_mMONbyGJf1gsQN-QfJF7F1iV9Kv6XdbTRy02lmSUcvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔐
معرفی DayLock؛ گاوصندوق دیجیتال و ‌امن
پروژه متن‌باز DayLock یک سرویس اشتراک‌گذاری پیام و فایل بر پایه معماری «دانش صفر» (Zero-Knowledge) است؛ یعنی سرور هیچ دسترسی یا کلیدی برای خواندن اطلاعات شما ندارد!
🔹
رمزنگاری سمت کاربر:
تمام داده‌ها مستقیماً در مرورگر شما رمزنگاری می‌شوند و سرور فقط کدهای نامفهوم را ذخیره می‌کند.
🔹
پنهان‌نگاری پیشرفته:
مخفی کردن امن فایل‌ها و متن‌های حساس داخل تصاویر (PNG) یا فایل‌های صوتی.
🔹
رمز فریب‌دهنده (Decoy):
امکان ایجاد یک گاوصندوق جعلی برای مواقعی که تحت فشار مجبور به باز کردن فایل‌هایتان می‌شوید.
🔹
قفل‌های هوشمند:
محدود کردن دسترسی بر اساس کشور (Geo-Lock)، شبکه اینترنت (ASN) یا تنظیم زمان مشخص برای باز شدن پیام (Time-Lock).
🔹
تخریب خودکار:
قابلیت حذف برای همیشه پس از اولین بازدید (Burn-on-Read) یا پاک‌سازی خودکار در صورت عدم فعالیت (سوئیچ مرد مرده).
🔗
لینک بررسی و نصب در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2927" target="_blank">📅 20:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2926">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bn3w5rqW-7byR2vTpq8tKWs5-rAxFi-u9lvaJMrMB9WUdPDh8rtz8YwGyZqkX47VSdMhPkG6jHYDA1yIIkHXwRpxTv0PM2YDMImnaIOY7_3WJETcKRI8dgdtoz484Pk0W0zloWmsA_BMHeBvzsJ5_-9hEU_To6gBRHeyFtcgXqRQiFo7hNHYpv0sv8qXGaTpdpMg02mqwKixTHrlBSEYx_WAKDOWL2rF_vYngpAJBLNyrxeVMIWLSnvEILsRA5ckzl9WkfBhKISPyq013snRG1PWm93sZrXbl1SX7lYXkTWQi3IheaYwJivE6HjZoacEnnRUH5ZWaTpTgHHzUrDV6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتار آدم های معمولی با هوش مصنوعی
در مقابل
رفتار برنامه نویس ها با هوش مصنوعی :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/2926" target="_blank">📅 18:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2925">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkAwOyA4vAsUTH_f_r-tbXC5mn-npaN3L-c8ERMb3q94oLfO3_9jjCq-qqJQTMXQhr52o3Zlj7qrQkiXvzjKtNYXkYuMVDH7fPx5sN7Lj8sPujmB0dpzvJEgzgF5XfyrIOl9jc1y2Bf_feOrfY72stpq8Ua7j_X1x7ASLRDXACYKpAgh7AZ9e-t9RFQkd7dsLyueaZk_bHRhLGXB5GIkElyMLip_hKi0el3NbPVAD3yLTocgWyE3qtB8pkgsK6nqjwRrNnMwkxL-TfRRd04VPA7eMBnZOpvhvRvxOe4dTPes1GIUFlmnwIsg7xmNW1uM0r98J02Ro1A6pj_Jnp67ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
آپدیت بزرگ ۱۳ سالگی تلگرام منتشر شد؛ از فایل‌های درون‌متنی تا پیام‌های خوشامدگویی اختصاصی
تلگرام هم‌زمان با سیزدهمین سالگرد فعالیت خود، آپدیت جدیدی را همراه با قابلیت‌های کاربردی برای کاربران، مدیران کانال‌ها و توسعه‌دهندگان بات‌ها معرفی کرد.
🔹
پیام‌های خوشامدگویی:
مدیران گروه‌ها و کانال‌ها اکنون می‌توانند بسته‌های خوشامدگویی شامل متن، عکس، ویدیو و جداول بسازند که تنها برای کاربر تازه‌وارد نمایش داده می‌شود.
🔹
دکمه‌های تعاملی درون پیام‌ها:
با به‌روزرسانی
Bot API 10.3
، توسعه‌دهندگان می‌توانند دکمه‌های کنترلی تعاملی را مستقیماً داخل پیام‌ها قرار دهند و امکان اجرای بازی‌ها (مانند شطرنج)، آزمون‌ها، نظرسنجی‌ها و سفارش کالا را به‌صورت زنده فراهم کنند.
🔹
قراردادن فایل داخل متن:
ویرایشگر پیشرفته متن اکنون امکان گنجاندن فایل‌ها و آهنگ‌ها را درون بخش‌های مختلف نوشته فراهم کرده است (با نوشتن بیش از سه خط متن فعال می‌شود).
🔹
افزودن امضا و پیام به هدایا (Gifts):
هنگام خرید هدایای کمیاب (Collectible) با استفاده از Telegram Stars، می‌توان امضا و متن شخصی دلخواه را به هدیه پیوست کرد.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2925" target="_blank">📅 16:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2923">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🛑
یه اشتباه خیلی رایج و خطرناک: «هر اسکریپتی که اوپن‌سورسه امنه!»
سلام دوستان عزیز
✋
همون‌طور که می‌دونید، هدف اصلی این کانال معرفی اسکریپت‌ها و ابزارهای اوپن‌سورس برای دور زدن فیلترینگه. اما یه سوءتفاهم خیلی بزرگ و خطرناک بین کاربرا وجود داره که وظیفه خودم دونستم حتماً در موردش باهاتون صحبت کنم.
خیلیا فکر می‌کنن چون یه برنامه «اوپن‌سورس» هست، پس قطعاً هیچ بدافزاری توش نیست و ۱۰۰٪ امنه. اما واقعیت اصلاً این نیست!
متن‌باز بودن فقط معنیش اینه که کدهای اون برنامه برای همه قابل دیدنه.
این ویژگی به خودیِ خود امنیت رو تضمین نمی‌کنه؛
بلکه امنیت زمانی وجود داره که متخصص‌ها، اون کدها رو خط‌به‌خط بررسی کنن. اگر کسی کدها رو نخونه، یه بدافزار خیلی راحت می‌تونه جلوی چشم همه تو همون کدهای اوپن‌سورس قایم بشه.
من خودم همیشه قبل از اینکه اسکریپتی رو معرفی کنم، تمام تلاشم رو می‌کنم تا در حد توانم و با کمک هوش مصنوعی، کدها رو بررسی کنم تا مورد مخربی توشون نباشه. اما یه مشکل بزرگ وجود داره:
👈🏻
اسکریپت‌ها مدام آپدیت میشن!
🔹
یه اسکریپت ممکنه بعد از اینکه تو کانال معرفی شد، تو همون چند هفته اول ده‌ها آپدیت جدید بده. بررسی تک‌تک این آپدیت‌ها برای منِ نوعی واقعاً غیرممکنه. این یعنی ممکنه اسکریپتی که ماه پیش کاملاً امن بوده، تو آپدیت امروزش حاوی کدهای مخرب باشه (حالا یا عمدی توسط خود سازنده یا به خاطر هک شدن اکانتش و...).
💡
خب راه‌حل چیه؟ چطور امن بمونیم؟
۱.
هیجانی آپدیت نکنید:
هیچ‌وقت به محض اینکه سازنده یه آپدیت جدید داد، سریع نرید اسکریپتتون رو آپدیت کنید! حداقل چند روزی صبر کنید. اگر تو آپدیت جدید بدافزاری باشه، معمولاً بقیه برنامه‌نویس‌ها زود متوجه میشن و گزارش میدن.
۲.
استفاده از نسخه‌های تست‌شده:
سعی کنید از همون نسخه‌ای (Release) استفاده کنید که روز اول تو کانال معرفی کردم و داره کار می‌کنه. تا وقتی اسکریپت فعلی‌تون بدون مشکل وصل میشه، لزومی به آپدیت کردن مداوم نیست.
۳.
به اعتبار پروژه دقت کنید:
پروژه‌هایی که تو گیت‌هاب ستاره (Star) بالایی دارن و افراد زیادی اون‌ها رو فورک (Fork) کردن، معمولاً بیشتر زیر ذره‌بین متخصص‌ها هستن و امنیتشون از اسکریپت‌های ناشناس بیشتره.
۴.
گزارش موارد مشکوک:
اگر خودتون برنامه‌نویسی بلدین و کدهای آپدیت‌های جدید رو نگاه می‌کنید، اگر مورد مشکوکی تو آپدیتی دیدید، ممنون میشم به ربات ما پیام بدید.
در نهایت فراموش نکنید همیشه حواستون جمع باشه و به هیچ ابزاری، حتی اوپن‌سورس، چشم‌بسته اعتماد نکنید.
🛡
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2923" target="_blank">📅 20:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2922">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBNU60aC4_apJNH7FinMqgXxhdcft0_BXTL--soheVBXFj5qUBCBaz9rzyO1TJUdi9V6uye7R263zXQKsDKWGj8pDYOhh06IYSvA-InS2yo2HJvN5TGF4W-mUOSyemQfZz6vRlBLqFOtYD44wfVCSkg1HyyfGKwi1LqWHapV3fHzBrSYNG57IhJTuG0gy1f-RgiScNws41crHBR0-0eFdsJDQdIpFcuLIeeAOReigYEXumyXvnQ23JJK9j73F6jHGE6_QT9FwkvTQRCs2wbtSX0IsSs8tv7fVhWVyLXmhwJ-J869u0NRBM-8eJv1heRf91f3S8Z29SVaCD3ZvOCZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اگه سوال مالی داشتید میتونید از آرش بپرسید بچه ها :)</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/2922" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2921">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2V87d-KwDRAROO1nJfx8B8ORaKsCSK-sv5DLXB13DDSoW3JCSQu4sfeBKin2Y0tG1-Y5HHGsrld-FSl0wfxFE_k7pv8q-4NG3Jd_Z5Fkt77hY5K5YiVrie_rhgbrdZb5W-dnS6qK3VrTRuGWRh5BT3wnH3Lw9OV-zxEpr2zo4CWrnL0tAoNaWyGt_mcmo41LEcJ1egNJo7dbA5QNDDB1gZHQQqag-phAnNxfNyKwx_0OE8jJwWosiy-opQDb7UyUV7GSRvtThaz79d7A2e3udM3ZmcTIUsZQ5zLbnZBxpoIgHf2tsouIrbbP3A_N4e07gkf1CYj9aMo8WqHdN4_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
وضعیت اینترنت این هفته
🔹
بر اساس داده‌های Cloudflare Radar، ترافیک بین‌الملل ایران همچنان حدود ۵۹٪ سطح عادی پیش از قطعی است. برخی مناطق مثل مازندران، کرمان و آذربایجان‌غربی افت محسوس‌تری داشته‌اند.
🔸
اگر این هفته با کندی یا قطعی مواجه بودید، تنها شما نیستید.
منبع: توییتر سایفون
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2921" target="_blank">📅 18:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2920">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrwPjxM89XcOunw9ybn9ZV13ylNjdMwQryXEjP7qJ8GEVOjmCtW4mXng4xhgQlNd_hAiRe9g-1h2FYhqS-f4OSYOZecKSPTxS_dMRCaktOZiFRuHXC7KdV4VDtASXsw1HnK7s1Tjcm4WUKwgJErl0NSa7DsyuKnYidrjNyYvTxSyg9aq4j9Pt65-VIPJsI7fAf9OvpG8eNWtIgG3Z02t2o3l1v7UABnCX49iVDZ7N06VHhShPVKnm6IzOU6n-oUPzA_Itn5ZjczbI3ZMViA5vuJw5HXQeTDDip_PjACV84nrW52_n83ZeOQIWilN8dOxhMxkSE6liAPGc77REc0Afg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت پنل و شروع فروش در ۱۰ ثانیه! (معرفی ربات پنل‌ساز)
🔹
تو این ویدیو یک ربات پنل‌ساز رو بهتون معرفی می‌کنم که بدون نیاز به هیچ تخصصی، فقط با زدن ۲ تا دکمه می‌تونید پنل اختصاصی خودتون رو تحویل بگیرید و بلافاصله کارتون رو شروع کنید.
🔸
این ویدیو یه پیشنهاد عالیه برای دوستانی که پیام می‌دادن به خاطر شرایط خاص یا مشکلات جسمی دنبال یه راه درآمدزایی هستن.(می‌تونید ربات رو ۲ روز تست کنید و بعد از تحقیق و صحبت با پشتیبانی، کار خودتون رو استارت بزنید).
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#پنل
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/iaghapour/2920" target="_blank">📅 18:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2919">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25ab5fc23.mp4?token=HlVivsG3pFDxJAVDnmPN2jIjWHvdoFWqnMemBJzZ-lZeLhS0pum0r6zBQmE6bCGUXxOD6dKlrbJCjWIXhBRJRurPHGgRE2WmKqOt2yu3QZaM16p6-TSzDJFLuL5FOpoA0uPRmItwzVrMOyABjxJejeLo5kAqIxZRbi4sUHi0iZNP8y0iQhOFQuQNnK0zJ8DmjpwkDALDsDsyeafwMXqyAYE8Kh_iFaRHHrDWbAbQevoTzREcT4nij8GcWg4cwCE82EdkqTEHrwEwq8Z8H6YsC4SEwmi4Q8kaIMWdiBfn4soqqZ5n5Dgzz0aOI2Ms6zqw68-Q1JNSoDLJBa8VhUDw8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25ab5fc23.mp4?token=HlVivsG3pFDxJAVDnmPN2jIjWHvdoFWqnMemBJzZ-lZeLhS0pum0r6zBQmE6bCGUXxOD6dKlrbJCjWIXhBRJRurPHGgRE2WmKqOt2yu3QZaM16p6-TSzDJFLuL5FOpoA0uPRmItwzVrMOyABjxJejeLo5kAqIxZRbi4sUHi0iZNP8y0iQhOFQuQNnK0zJ8DmjpwkDALDsDsyeafwMXqyAYE8Kh_iFaRHHrDWbAbQevoTzREcT4nij8GcWg4cwCE82EdkqTEHrwEwq8Z8H6YsC4SEwmi4Q8kaIMWdiBfn4soqqZ5n5Dgzz0aOI2Ms6zqw68-Q1JNSoDLJBa8VhUDw8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
علی‌بابا از مدل قدرتمند تولید ویدیوی هوش مصنوعی Wan 3.0 رونمایی کرد
شرکت علی‌بابا (Alibaba Cloud) رسماً از مدل پیشرفته و ارتقایافته
Wan 3.0
برای تولید ویدیوهای باکیفیت ۳۰ ثانیه‌ای رونمایی کرد. این مدل با هدف رقابت جدی در بازار جهانی تولید محتوای ویدیویی هوش مصنوعی عرضه شده است.
🔹
پشتیبانی از ورودی‌های متنوع:
امکان ساخت ویدیو از روی متن، اسناد، صفحات اکسل (اسپردشیت)، اسلایدها و صفحات وب.
🔹
پذیرش چندگانه فایل‌های مرجع:
قابلیت دریافت همزمان تا
۱۰ تصویر مرجع
،
۵ ویدیوی مرجع
و
۵ فایل صوتی مرجع
برای هدایت دقیق خروجی.
🔹
حالت تفکر:
پردازش هوشمند و تحلیل دقیق‌تر برای دستورات و پرامپت‌های پیچیده و چندمنظوره.
🔹
حفظ یکپارچگی کاراکترها:
توانایی حفظ ویژگی‌های بصری شخصیت‌ها در طول صحنه‌ها و سناریوهای مختلف با خروجی‌های بسیار واقع‌گرایانه و پرجزئیات.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2919" target="_blank">📅 16:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2918">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vay55Ds7kaJCIjhKOAK0LOQqZ3MCQznxHjtLXtHx4CsVAhNVEH46J6uBH1_Z_ERlGcD6Uvhx_2wHKtvKc1bv_ttRARomkvRizeU9XUeW38RMNGwOV9JlJt8nCwr0uRvSvhMTbfa33qVF4pOCDWv3IPgzf66H6RYTfBOgKF-D6qAt-fQwD5vPwDudFC0Y79-ul9PMAZRaJgBsUt2RL--sSPkHsYPJYjxQYuM-oGCKNQgS4G8V-j1jzlJSB93VqWVBWJfF0_NXZAadcMwY0_pcONBJ2221xG_FRujlHQ8qhwf4oZckck66NwVhX2Az23d6scdrbfz-WYaQg4yEbn2j_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پروژه استقرار PasarGuard Node روی بستر ابری Railway
پروژه
railway-pg-node
یک Wrapper مستقل برای بیلد و دیپلوی مستقیم نود پاسارگاد (
PasarGuard Node
) روی کلود Railway بدون نیاز به خرید سرور اختصاصی است.
⚙️
معماری و نکات کلیدی راه‌اندازی:
🔹
مدیریت پورت و لیسنر:
کانتینر یک لیسنر از نوع TLS اجرا می‌کند؛ متغیر پورت (
PORT
که معمولاً ۸۰۸۰ است) از سمت Railway تزریق شده و اسکریپت
start.sh
آن را به عنوان
SERVICE_PORT
ست می‌کند.
🔻
اتصال به پنل اصلی با TCP Proxy:
از آنجا که پنل مدیریت خارج از شبکه Railway قرار دارد، باید از
TCP Proxy
استفاده کنید:
🔹
پورت داخلی:
همان پورت داخل متغیر
PORT
یا لاگ سرویس (مثلاً ۸۰۸۰).
🔹
پورت عمومی:
پورت تخصیص‌یافته توسط Railway به همراه دامنه/Hostname عمومی.
⚠️
نکته مهم آدرس داخلی:
دامنه
railway-pg-node.railway.internal
تنها در شبکه داخلی Railway معتبر بوده و برای اتصال خارجی باید از آدرس TCP Proxy استفاده شود.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/2918" target="_blank">📅 14:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2916">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXKQOKbYNLKnuURpcZgkascZPeevKvEDDeEYqgSPGqzMDg7LPV03HOHjXJKxMzqhh9QfJD9Rv0j45YGw-9CGRgTRvbB_1cKpOdMxiRk6Wr0wjR_3Sn0NKfKmUmw6s0hwUgiO3qQa8Lib2n6qGlt8Qdv8aGdH7Nc6tKHCaam4ioYMFf1MOzLj495I_-edU-n3AT5gPlZyevkIEw-3mnFlYyhOxU3rKn0EM0oQEfor_8bHbzFHColl3OTv6MuKfsOG_eIkVmZ9G-EBOBW3T7Ud7JJDOJIs5H9VBsiUMMhDpqGEJNIeyc-UDt9iZWReYRPmdcrLO8G_AADfgH-AyzU5Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی tproxy-server؛ نسل جدید پروکسی‌های وب برای تلگرام
این پروژه سمت سرور یک طرح اثبات مفهوم (PoC) از سوی تیم تلگرام دسکتاپ است که روشی کاملاً نوین برای عبور از فیلترینگ ترافیک MTProxy از طریق مرورگر داخلی (
WebView
) ارائه می‌دهد.
🔹
پنهان‌سازی در قالب ترافیک وب (HTTPS/WebSocket):
اپلیکیشن تلگرام فریم‌ها و رمزنگاری استاندارد MTProxy را حفظ می‌کند، اما تمام اتصالات TCP را از داخل یک لایه انتقال مبتنی بر WebView و در بستر امن HTTPS یا WebSocket عبور می‌دهد.
🔹
چندین اتصال در یک مسیر:
این سیستم چندین ارتباط لاجیکال را مالتی‌پلکس کرده و در سمت سرور، رله این جریان‌ها را مجدداً تفکیک نموده و به سرویس رسمی MTProxy متصل می‌کند.
🔹
استتار به عنوان یک سایت عادی:
دامنه سرور مانند یک وب‌سایت کاملاً معمولی و عادی HTTPS عمل می‌کند؛ تنها با داشتن Secret اختصاصی، صفحه پل ارتباطی پروکسی فعال شده و سایر درخواست‌های عمومی فقط وب‌سایت اصلی را می‌بینند.
🔸
سازگاری کراس‌پلتفرم:
این ساختار محدود به سیستم‌عامل خاصی نیست و هر کلاینت دارای WebView می‌تواند از آن استفاده کند.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/iaghapour/2916" target="_blank">📅 20:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2915">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LE7fLwGlrigW_gNf8QpOwVhFFVk1vyw65Wlhnk8Bcq51j1E0BXbdh7m8kE_qA6Ak7N_ffCODdoLwRZrJuiECfUyVk3HfDbuIo0540WL-LXzq44L5JCVdtQashWB4zibWAgnW6ciFAGIbgCW9mtLSgkIYfGasVJrAavDg2v5s6VYfl_7ssOrkOIcZ3y6IZ1oowKiH6X0Iog67MNhqKmT2rJKxJDJPSZmJS_7wysGPm-bkBoju9CajY5Rm_qrvIAFBAzaZ8c7TfTeBtniqytbCg8gAEFHw4SAaXxtwNQqgqt3l40Csk3Dt0uumLtFoCbqg2G_-qYGCe9f6R6qa40Pj7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
حدود ۴۰ درصد از آهنگ‌های جدید ماه ژوئیه با هوش مصنوعی ساخته شده‌اند
بر اساس گزارش تحلیلی پلتفرم
SubmitHub
و با بررسی بیش از ۱ میلیون قطعه موسیقی، نزدیک به
۳۸.۵ درصد
از کل آثار منتشرشده در ژوئیه ۲۰۲۶ با مداخله هوش مصنوعی تولید شده‌اند.
⚙️
آمار و نکات کلیدی این گزارش:
🔹
سهم آثار هوش مصنوعی:
۲۳.۲ درصد آثار کاملاً با AI ساخته شده‌اند و ۱۵.۳ درصد شامل قطعات تولیدشده با AI بوده که سپس توسط انسان‌ها ویرایش شده‌اند.
🔹
عدم توانایی تشخیص مخاطبان:
تحقیقات نشان می‌دهد ۹۷ درصد شنوندگان متوجه تفاوت میان موسیقی انسانی و تولیدشده توسط AI نمی‌شوند.
🔹
هجوم اسپم صوتی (AI Slop):
پلتفرم Deezer اعلام کرده بود بیش از نیمی از آپلودهای روزانه جدید آن به موسیقی‌های هوش مصنوعی اختصاص یافته است.
🔸
واکنش و مقابله پلتفرم‌های استریم:
🔹
پلتفرم
Bandcamp
انتشار هرگونه موسیقی هوش مصنوعی را کاملاً ممنوع و مشمول حذف اعلام کرده است.
🔹
پلتفرم
Spotify
از سپتامبر نشان اختصاصی «AI Persona» را به پروفایل‌ها اضافه می‌کند تا شنوندگان آثار ساخته‌شده با هوش مصنوعی را به‌راحتی تشخیص دهند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/2915" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2912">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RajIjoK5qGlTU-TbKM5xgHbOn17VaQNBqxx99pyxE2ldUmWhAHvg0ZlCuesOuEiREyxetn_VZutkN8QSvV338C2wVfyLFVAwg0aLMJUJW7TRQYrURjZzjKbMtVG8vzTJ3UD5Dg1vo1xaiQucbUH-UiQ_wFrx6By7RgPwOIipV2Y0cgNKQ7GGkRDSQKXs8lPlLSOJsWKqSuYf4ALOSno5aknmL9DX1JPxt5Co93-mLpauSQtwfpJGD579rHRA871Xrkx_uzRWP-BSNzGeaqRKaUM63-uNQKn50hnbgvTSsqL5awfuInOnbVf6xkI3Ds4h0ORnXS-OSv8Qem3Nkqh37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دسترسی رایگان و آزمایشی به مدل‌های هوش مصنوعی Qwen در سرورهای Hetzner
هتزنر امکان استفاده رایگان و آزمایشی از دو مدل هوش مصنوعی
Qwen3.6-35B-A3B-FP8
و
Qwen3.8-27B
را برای کاربران خود فراهم کرده است که می‌توانید آن را به نرم‌افزارهایی مثل 9Router متصل کنید.
⚙️
مراحل فعال‌سازی و اتصال:
🔹
۱. دریافت توکن:
با اکانت خود وارد سایت شده و به آدرس زیر بروید تا یک توکن بسازید:
🔗
آدرس سایت هتزنر
🔹
۲. اضافه کردن به 9Router:
وارد برنامه شوید و یک پروایدر جدید از نوع
OpenAI Compatible
اضافه کنید.
🔹
۳. ثبت کلید:
روی گزینه
Add API Key
بزنید و توکن دریافتی از هتزنر را وارد کنید.
🔹
۴. ایمپورت مدل‌ها:
روی دکمه
Import from
کلیک کنید تا مدل‌ها به لیست شما اضافه شوند.
⚠️
وضعیت فعلی:
در حال حاضر مدل
Qwen3.6-35B-A3B-FP8
فعال و قابل استفاده است، اما مدل
Qwen3.8-27B
با خطا مواجه می‌شود.
©️
aleskxyz
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2912" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2911">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💡
راهنمای ساخت اینباند در پنل 3X-UI روی سرویس ابری Railway
نکات تگمیلی درباره
ویدیو بالا
☝🏻
با این ساختار می‌توانید بدون نیاز به خرید سرور (VPS)، پنل
3X-UI
را روی کلود
Railway
اجرا کنید.
🌐
مکانیزم عملکرد پورت‌ها:
پورت‌های ۸۰۰۱ تا ۸۰۵۰ (وب):
ترافیک از طریق Nginx روی پورت ۴۴۳ مدیریت می‌شود (مناسب برای WebSocket و HTTP Upgrade).
پورت ۸۰۸۰ (مستقیم):
از طریق
Railway TCP Proxy
مستقیماً هدایت می‌شود (مناسب برای Reality و gRPC).
🛠
روش اول: ساخت اینباند WebSocket / HTTP Upgrade (پورت ۸۰۰۱ تا ۸۰۵۰)
۱. در پنل وارد بخش
Inbounds
شده و روی
Add Inbound
کلیک کنید:
Remark:
نام دلخواه (مثلاً
WS-Inbound-1
)
Protocol:
انتخاب پروتکل (
VLESS
یا
VMess
یا
Trojan
)
Port:
یک پورت بین
8001
تا
8050
(مثلاً
8001
)
Network (Transport):
انتخاب حالت
ws
(WebSocket) یا
HTTPUpgrade
Path:
متناسب با شماره پورت (مثلاً برای پورت ۸۰۰۱:
/in1
، برای ۸۰۰۲:
/in2
و...)
Security:
تنظیم روی حالت
none
روی
Save
کلیک کنید.
۲.
تنظیم بخش Host (ضروری):
روی گزینه
Add Host
کنار همان اینباند کلیک کنید.
Address / Host:
دامنه اختصاصی پنل در Railway (مانند
your-app.up.railway.app
)
Port:
عدد
443
Security / TLS:
فعال‌سازی گزینه
TLS (Enabled)
⚡️
روش دوم: ساخت اینباند Reality یا gRPC (پورت ۸۰۸۰)
۱.
ایجاد پروکسی در Railway:
در داشبورد Railway به مسیر
Settings
⬅️
Networking
بروید، روی
Add TCP Proxy
کلیک کنید و پورت کانتینر را روی
8080
بگذارید. دامنه و پورت اختصاص‌یافته را کپی کنید (مانند
domain.proxy.rlwy.net:12345
).
۲.
ساخت اینباند در پنل 3X-UI:
روی
Add Inbound
کلیک کرده و
Port
را حتماً روی
8080
تنظیم کنید:
حالت Trojan gRPC Reality:
Protocol: Trojan
|
Network: gRPC (حالت Multi)
|
Security: Reality
حالت VLESS TCP Reality:
Protocol: VLESS
|
Network: tcp
|
Security: Reality
|
SNI: یک دامنه معتبر (مانند yahoo.com)
روی
Save
کلیک کنید.
۳.
تنظیم بخش Host در پنل:
روی
Add Host
کلیک کنید.
Address:
دامنه TCP Proxy دریافتی از Railway (مانند
domain.proxy.rlwy.net
)
Port:
پورت دریافتی از Railway (مانند
12345
)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/2911" target="_blank">📅 20:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2910">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDVWYQNJi0b5O7UG-ArAlHwvT9wRpKgw7VVVwScl5y2ZxvIeKgs9d34726PuSSHHL0IHDvjCmE3Rev09jsHo3o4NSlIJouWssx8zBOg0pcy6jDUWuizxz6kSN1suaRdqe8XwJriQMyOYFmC1SPRu8JYo9zGpZ6N_XhBMd8wfAjRJcAVd4_mk3AKmhSjPr1qDz3JJ-C__v6ema2JGCZRh4SKR6w_MHjUw9MESGo6T_7MouTteytETjgiII64hwZplirvPoUSk4smuufcmXxzsslOTcQM4AwKgTW14rlVGEHhU9XbLYhTopubQ1SPMJaxy48Dy1Ons3am8P9tywmpxKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بزرگ‌ترین آپدیت تاریخ CPU-Z منتشر شد؛ نسخه V3 با ۱۰۰ تست سلامت و سیستم اعتبارسنجی جدید
نرم‌افزار نام‌آشنای
CPU-Z
بزرگ‌ترین به‌روزرسانی تاریخ خود را از سال ۲۰۰۱ تا امروز تجربه کرد. نسخه جدید (V3) با بازطراحی کامل بخش اعتبارسنجی (Validation) و افزودن ابزارهای مانیتورینگ سلامت منتشر شده است.
⚙️
امکانات و تغییرات کلیدی نسخه V3:
🔹
اعتبارسنجی استاندارد:
بررسی سلامت کامل سیستم در کمتر از ۱۰ ثانیه با ارزیابی بیش از ۱۰۰ شاخص مختلف (درایورها، دمای CPU، برنامه‌های اضافی و...).
🔹
اعتبارسنجی پیشرفته:
تست استرس و خطایابی سنگین و دقیق روی CPU، رم و کارت گرافیک به همراه بنچمارک جامع سیستم و سنسورهای مانیتورینگ پیشرفته برگرفته از HWMonitor برای بررسی دما، سرعت فن‌ها و فرکانس.
🔹
حالت اختصاصی اورکلاک (XOC):
محاسبه فرکانس مؤثر پردازنده‌های مدرن و مدیریت صحیح اورکلاک رم جهت جلوگیری از رد شدن تصادفی تاییدیه‌ها و ثبت دقیق‌ترین رکوردهای فرکانسی.
📥
دسترسی:
فایل نصب نسخه جدید از وب‌سایت رسمی
cpuid.com
قابل دریافت است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/2910" target="_blank">📅 18:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2908">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de89d4765.mp4?token=SQYqI_-CY6A3uRq-ZHnRuj1no_IV2kthBgXP9emWXRBYEr9ZNQgR6jdQfjKSDGxRm7iL25bg3OK0HSCZDsoJUwfaV0Vw5UqnEF7vupl0vuG9a3SKJlpIDyaJVo5LT-M-jWpiHo_8OqX2q5Ik44J6-T49-ck5l9Ui0KAnF_0y_XJMdlVQFVrHjHTXq_u-RTe0OLgVN-K0523F3r8oxp77xdiSLyO6W02OrgchO911fC18fGeoltTkfLVqYFed2pPMZObrwiLaB2dckX7d4qWdwIdvM7lgsCYuIMimp79chqudSiexPhCuMcwpDiTeU0xsL-5SyabUEQKgFX5Coi57aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de89d4765.mp4?token=SQYqI_-CY6A3uRq-ZHnRuj1no_IV2kthBgXP9emWXRBYEr9ZNQgR6jdQfjKSDGxRm7iL25bg3OK0HSCZDsoJUwfaV0Vw5UqnEF7vupl0vuG9a3SKJlpIDyaJVo5LT-M-jWpiHo_8OqX2q5Ik44J6-T49-ck5l9Ui0KAnF_0y_XJMdlVQFVrHjHTXq_u-RTe0OLgVN-K0523F3r8oxp77xdiSLyO6W02OrgchO911fC18fGeoltTkfLVqYFed2pPMZObrwiLaB2dckX7d4qWdwIdvM7lgsCYuIMimp79chqudSiexPhCuMcwpDiTeU0xsL-5SyabUEQKgFX5Coi57aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برندگان عزیز قرعه‌کشی
(دوره پنجم و ششم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 2 عدد اکانت هوش مصنوعی ۱ ماهه برای 2 نفر مشخص شد:
👤
نیما عزیز با آیدی nimashokri5515، مبارکتون باشه!
✨
👤
حامد عزیز با آیدی hamedsalamati2286، مبارکتون باشه!
✨
✍🏻
با تشکر از اسپانسرهای عزیز این قرعه کشی.
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/2908" target="_blank">📅 20:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2907">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVOvdAFgF9WCP-4l-GNp7mEQfamXInoCa6Z2j7TwQerh8Fp-cY-9RitotkoIPwAjHfs4YfKmXG5glvxNLkXZI8zGCu36_MPZ51VABAX9pXC2uBbcjl0zcHKYNCgaDmmoyOezYlRT5rREP20z8eUgasHWeQQTyzsjQXx8gLFFfZLu6Yoh6oGskGAskYNZ55VelQYcu-YSaI0qNHELAp7E3YvcPZjXBu3qNYMa8sjJ9eYQJ3_IuqEWkV3bFYgYsy7bKR5R2qEJKhsgoQWp6Rl2CtsxB1JMx0_awk3BFoDGVsZRFme5169IoS7GBmfQWJ0XqkLcxgXdWtgtC99GV5pq3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
تداوم ناپایداری‌ها؛ دیتاسنترها گرفتار فیلترینگ سخت‌گیرانه و سامانه «شاهکار»
بررسی‌ها و تایید مدیرعامل شرکت ارتباطات زیرساخت نشان می‌دهد وضعیت اینترنت در دیتاسنترها هنوز به روال عادی قبل از دی‌ماه ۱۴۰۴ بازنگشته است.
⚙️
چالش‌های کلیدی مراکز داده:
🚫
فیلترینگ شدیدتر:
دیتاسنترها با محدودیت‌هایی به‌مراتب سخت‌گیرانه‌تر و اختلالات فنی مرموزتری نسبت به اینترنت خانگی دست‌وپنج نرم می‌کنند.
🔻
بحران سامانه «شاهکار»:
بزرگ‌ترین مشکل فعلی، الزام به احراز هویت دستی کاربران در سامانه «شاهکار» پیش از اتصال است که این فرآیند را از ۲۴ ساعت تا
یک هفته
طولانی کرده است.
🌀
سردرگمی کسب‌وکارها:
تیم‌های فنی هنوز درگیر ترمیم زیرساخت‌های آسیب‌دیده از قطعی‌های طولانی هستند. فقدان تضمین برای عدم قطعی مجدد، شرکت‌ها را میان بازگشت به معماری استاندارد یا حفظ آمادگی برای بحران بعدی معلق نگه داشته است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/2907" target="_blank">📅 19:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2906">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4KyZjh_UtlPqMsGZjyOgHBwmaJjH53tGyjDQ7rYVjuMztdIcMhOvgFBm_eRyHwX5yV8EVgH2D50jJhmYOvH9Y8NbWFotH20Bg6-qVLvat3wcNwY2RpPwJyqbmYNTmjegx_T9KnzmPZFO3jIPhGmKfRMRa_9Qh4yXk_8a8mQv1yVJFqcJzw6ElyH5nyQhpBLNqQ498cp9YW1ZCe9m2ik2QaKU_5eZGxUuM4WXMwa1_rQ4A6JbObdbU_Ihl2By2u7pFtLXms-iYySIC3juRZv2Gveu6Zz-QbvSVhtTQzTkdIbMkmUSf7PZCZ6QIIs4qEgPIYZzxrZMrHxQ-X8iXRAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی Tor Node Manager؛ اسکریپت ساخت و مدیریت خروجی‌های تور تفکیک‌شده بر اساس کشور
این پروژه یک ابزار تعاملی است که به شما امکان می‌دهد روی سرور خود نودهای مجزا و اختصاصی Tor را بر پایه کشورهای مختلف (مثل ترکیه، آلمان، هلند، فرانسه و...) به‌صورت پروکسی‌های لوکال SOCKS5 بسازید. این پورت‌های لوکال به‌راحتی می‌توانند به‌عنوان Outbound در پنل‌های
3X-UI
،
Xray
یا سایر برنامه‌ها استفاده شوند.
🌍
تفکیک نودها بر اساس کشور:
ساخت نمونه‌های مجزا از Tor با لوکیشن دلخواه و پورت SOCKS5 اختصاصی روی
127.0.0.1
.
🔄
سرویس‌های مستقل Systemd:
اجرای هر کشور به‌عنوان یک سرویس مجزا در سیستم‌عامل به همراه فایل کانفیگ، دایرکتوری داده و لاگ اختصاصی.
🔍
تأیید خودکار موقعیت جغرافیایی (Geo-Check):
بررسی زنده و چندمرحله‌ای اتصال و کشور خروجی Tor، همراه با سیستم تلاش و ری‌استارت مجدد خودکار تا زمان تایید قطعی لوکیشن انتخابی.
📋
کانفیگ آماده Xray Outbound:
تولید و نمایش خودکار قطعه‌کد آماده‌ی JSON برای اضافه کردن مستقیم به بخش Outbounds در Xray یا 3X-UI.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/iaghapour/2906" target="_blank">📅 14:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2904">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrzTB4LyZsW4drfN6TTW3tAe00CYWFT_11ouAbauw8UMRySciUIdYE-CnZd1Prej9ommH2daDbiCNJdB46L9RbCkounzg8UEf4I4ExQAwNR4wQWB8Q9zbfwn2iFwR60uFpbpUWEDPp8ZIYOUGnm4_dLHsFUknv26LYOMjAD1rCdL5W81uY86znfBDq2OJdlm1GjTn95Z6vG7PrMOoBLdz1PLVgs6MLGSGroCnSKayz1ZrVbYabw_upCTOlcetYiqyx176OiA6Ov4lxQFFGJVxLe4_52GimVCinvtJzpSA6sHgnFhMlK9p3ZTBYIzHd-fLkyiMvuu_o361Des1pF9zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت فیلترشکن شخصی بدون سرور و دامنه (کاملاً رایگان!)
🔹
اگه می‌خواید یک کانفیگ کاملاً شخصی برای خودتون داشته باشید، ساخت فیلترشکن شخصی بدون سرور و دامنه همون راهکاریه که بهش نیاز دارید. تو این آموزش قدم‌به‌قدم بهتون یاد می‌دم که چطور بدون سرور یا دامنه، پنل X-UI رو راه‌اندازی کنید و برای خودتون کانفیگ شخصی بسازید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت فرصت دارید.(قرعه کشی این ویدیو با ویدیو قبلی باهم انجام میشه)
#آموزش
#فیلترشکن
#رایگان
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/iaghapour/2904" target="_blank">📅 17:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2903">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZaMrw-yLnfAIHUtd2uOUSJUy7II_e7Fb54OPEKJ9NvDKtlDgfgkYtT9sXBURb4Siw4bLoxNHjQKZYn1VCAQslh6jFfaMHVr2Pl-IKNmoSy5gEvireAyw8WK9CUCQMEK_B7PmQlj8hlfolVfAx5TLpdemGcH3p3YhagYYs8PCbUAi-Xq-P4QM8-CghqsrwIhw-2Cc8kQHQLssdSj6QSthQnlD8-pEsfu67XhGIEPbWI81jZY3jFrsXuBMTWQ3l3e2HELRgOwZprRYaYAfk8dJ47ua37ZyP-RAESV1-v-AegrjzkPkw5grIk3-jVfGGeMPSIEwFRsYYXu25t4So2xGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش استعلام سیم‌کارت‌های فعال به نام شما با کد ملی
بی‌خبری از سیم‌کارت‌هایی که به نام شما ثبت شده‌اند می‌تواند باعث سوءاستفاده‌های حقوقی، امنیتی و جعل هویت شود. طبق قانون، هر فرد حداکثر می‌تواند
۱۰ سیم‌کارت فعال
در مجموع تمامی اپراتورها داشته باشد.
⚙️
روش‌های استعلام:
📩
۱. استعلام سریع از طریق پیامک:
— کد ملی ۱۰ رقمی خود را به سرشماره
۳۰۰۰۱۵۰
ارسال کنید.
— پیامکی از
CRA.ir
حاوی تعداد سیم‌کارت‌های فعال شما در هر اپراتور ارسال می‌شود.
🌐
۲. استعلام کامل از سامانه «دولت من:
— وارد سامانه
my.gov.ir
(یا اپلیکیشن دولت من) شوید.
— پس از ورود، از بخش
دسته‌بندی سازمان
⬅️
سازمان تنظیم مقررات و ارتباطات رادیویی
را انتخاب کنید.
— با انتخاب گزینه
«تعداد خطوط مشترکین تلفن ثابت و سیار»
، تمام شماره‌های فعال همراه اول، ایرانسل، رایتل، اپراتورهای مجازی و سیم‌کارت‌های TD-LTE را مشاهده کنید.
⚠️
اقدام فوری در صورت مشاهده سیم‌کارت ناشناس:
اگر خط ناشناسی به نام شما ثبت شده است، بلافاصله از طریق اپلیکیشن یا نمایندگی‌های اپراتور مربوطه نسبت به
سلب مالکیت یا سوزاندن سیم‌کارت
اقدام کنید./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2903" target="_blank">📅 16:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2901">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxiRo45shI-OoaRVznRi_Q8wF1lg5S13BpAAyCc9QFF32O5K5hStu4sQK5ywsxDg4mdK-zcBWD3t9HW1_WkPWC4GPhmn3JLfcNPey__x_R68RVtqV2rA_iznWwaWjfvOhwKUwiyS5YFXkaJE_SMG9mpFf55mex6OKpvazOE0vQ7_E1N-YDQFrCCBnoxyLlGDA-9wcd-_DCk8RjbEuZXbA1OrBslbj5H62esWKxyKksA2xpSYZ6IKcsLfR9-XiUxP3w2n6ZSepyYpQYkLXGgBBvhAIuq3tfFRsEFIEPT7-ZY7xV4PE-xqBLYTmeil0DOBUH7kgNvkd4OpagLiUX0-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
فقط با یک سرور، 3 لوکیشن مختلف داشته باش! (با پنل 3X-UI)
🔹
اگه می‌خواید تو هزینه‌های خرید سرور صرفه‌جویی کنید ولی همزمان به آی‌پی‌ با لوکیشن‌های مختلف نیاز دارید، این آموزش دقیقاً همون چیزیه که دنبالشید. تو این ویدیو قدم‌به‌قدم بهتون یاد می‌دم که چطور فقط با یک سرور، 3 لوکیشن مختلف داشته باشید و این کار رو به سادگی روی پنل 3X-UI پیاده‌سازی کنید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت فرصت دارید.
#آموزش
#فیلترشکن
#ثنایی
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/iaghapour/2901" target="_blank">📅 18:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2900">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3GnKG8Rrcnci9QRXOB3z85ShQKiTRcWYuAyMQXKykUWQR2owrEgb0mC3en3QcrMmvhDi1erEeFyoVUsAaDhXclTcZapf5G-wVh27IRx7PlL3vdH83U1ZlMC7BxxwihPewThMeIbb3NNr1dPL21nZS2Vb5hQpn3VaaqnlPlZB_6t6p7M_t-PrHrvbufFlYH3ztF6x1WmJCFJDFtSkg3KflC7YWsU6R257g4meOjb4uh6o4h4_3YCrJmW_iO3Vv7YbOs09U6jethCd5JVDwuVd5hmMPLIna9Zajaq24jprUyICtmWAYNVWCRfF848ZW-C0ETx-EXxiyz1XyfiXSJ64g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تلگرام به هر کاربر دامنه اختصاصی با پسوند gram. می‌دهد!
تلگرام رسماً درخواست ثبت دامنه سطح‌بالای اختصاصی (TLD) با عنوان
gram.
را به سازمان آیکان (ICANN) ارائه داده است تا کنترل کامل زیرساخت آدرس‌های خود را به دست بگیرد.
⚙️
جزئیات و امکانات این طرح:
🔹
دامنه اختصاصی برای هر کاربر:
در صورت موافقت آیکان، بیش از ۱ میلیارد کاربر تلگرام دامنه‌ای بر پایه نام کاربری خود دریافت می‌کنند (مثلاً
username.gram
).
🤖
ساخت وب‌سایت با هوش مصنوعی:
کاربران می‌توانند وب‌سایت‌های تعاملی خود را روی همین دامنه‌ها و با میزبانی مستقیم تلگرام، تنها با وارد کردن یک دستور متنی (پرامپت AI) بسازند.
🛡
استقلال از واسطه‌ها:
این اقدام پس از اختلال اخیر دامنه
t.me
توسط ثبت‌کننده پسوند
me.
انجام شد تا تلگرام از وابستگی به رجیسترارهای ثالث رها شود.
⏳
وضعیت تایید:
پذیرش این درخواست منوط به سپری شدن مراحل نظارتی، فنی و حقوقی در سازمان آیکان خواهد بود./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/iaghapour/2900" target="_blank">📅 17:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2899">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSRUm-EWoLftgzKUpRzJj5YqlFLzdZxHRy5xqy8845ZK5pJChB0QG_OveHdRQEXGTOFPtog_kTFKgW30volUMLsiIjjPKdcQHzxioRKfSQmCklFZ5uJTBN1-qH1H1hh0yhL1AO0I2FJvgobTm6JiCdAxKdgmCfUc8lQfCsTVBA66TI2NPQqymchLo69sE9LIvItAFWUlBgGUZSAmWbJRebodqHUqvzGdgaAmx7XEYHn9A4BEJtbneDlgBz7SQHfl8J3QLlhhoUGOXhmng72rit3I1tcIFvXgL-i_uyAtHrdO33eqR9GKzP49wYf9BR9lxi9zxGqwg0z4ZJWKhfU8xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نظرسنجی ایسپا: بیش از ۲۰ میلیون ایرانی خواهان استفاده از اینترنت استارلینک هستند
بر اساس نظرسنجی جدید مرکز افکارسنجی دانشجویان ایران (ایسپا) به سفارش وزارت ارتباطات، در صورت فراهم بودن شرایط، بالغ بر
۲۰.۵ میلیون نفر
از کاربران ایرانی تمایل دارند از اینترنت ماهواره‌ای استارلینک استفاده کنند.
⚙️
یافته‌های آماری و نکات کلیدی نظرسنجی:
📊
میزان آشنایی و تمایل:
۵۶.۶ درصد
کاربران هنوز شناختی از استارلینک ندارند.
در میان افراد آگاه،
حدود ۶۱ درصد
تمایل دارند این سرویس را تجربه کنند یا به صورت دائمی به آن متصل شوند.
🚫
مانع اصلی، قیمت و دسترسی است نه قانون!
برخلاف تصور، منع قانونی دلیل اصلی عدم اتصال اکثر افراد نیست؛ تنها
۳۸.۲ درصد
به دلیل غیرقانونی بودن سراغ آن نرفته‌اند.
نزدیک به
۶۰ درصد متقاضیان (حدود ۱۲ میلیون نفر)
اعلام کرده‌اند دلیل وصل نشدنشان،
قیمت بالای تجهیزات
و
عدم دسترسی به فروشنده مطمئن
است.
⚠️
پیام هشدارآمیز داده‌ها:
آمارها نشان می‌دهد در صورت کاهش هزینه‌های تجهیزات یا تسهیل مسیرهای ورود به کشور، تعداد کاربران استارلینک در ایران می‌تواند با جهشی میلیونی روبه‌رو شود./شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/2899" target="_blank">📅 16:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2897">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GigKKTC4eBP9ZxKaGqmG842nfCfNLTrk-lpQ51F7YTYmsmc1RcXzHRcAkaJCQToDwzsRl4Bqpah2fXUTRU9oyUnz8GJyJKfvtIp7A6kx02UszXgsiaBgp3I_wYcrUThNHgvLDvGeMxHIznecbmktJnNsd9MFmwVuMAgMmW6acBYnus27wKUPCBb4oyOnvmNesWBDiw-GTmzHaCfVep67BJgcazNPAs1prirU3Zty8zhOaPZX377HsQyPe5Hcb2u0npUN-U1k2og6qFABr-sr5XRbwuzh7Ffmg6dyharBBhi7bEA22WP8LSHi1MtC087_yla65S4mg3q_v8oHW--Maw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدنویسی در سال ۲۰۲۶ :)</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/iaghapour/2897" target="_blank">📅 20:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2895">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E8CNlGy8-AjQDzEHhflXRb91K95J9XoomoE0_4iMtoCaMSaHgjkPMBFbfitTPQlI5FSOYjvrVbpuTeWMydBDrRvn6H5NpzP7wCACRwlOt1eIAo6L0_GbtMGqb_UokJ1K9G8Dw1f_bDZ7-vI_knNxRWS0r4XpHUVxky_oBVVGUqPUoObRw_wkwvp-HaWtkN2HKytk13RewmJbdlRr6gcAUHQ5QVl9jZkJudhDeWLSzlkRQNmOL723T8RNGzKQ-ylhZmI4tlWOS7PcsIDmYji_I4otyDzvYwkUzMka6dVbEX-tOCA2eROSaxmEXIg98MfwWKElIbBSeYeju5cUPXTObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmrZQ_UF-bULng5zOd8KkaLhJBUx-8WZDzkCbtlZVeFaE9TVHx--VPc2Ob7iBsEtb4Nf7TSU1AxMnPCwIv2cZDAnmazOkloP3_7KlFVQVqw6LrY2GLK2l3DNdM10u6qZa4N9qvKn5HxUSbie1ZWeiext2NU1V21UXllCUMbvMTOzjmUWBdEmub6M6sxjhP74flcZNjr1cNC5--DdI5EOeKJgNufZgFnLd5RzUlJnLt0ebAOtsKWFoT2yFX_CMsUC9eVl5QkAdOYUofdzHm1eJGyYJmIuqDiymTxwJKJQpSbwmgymDPn9eCoilbTCyLvPKI0QnAFCB4OhTZxnJJ-FYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟢
جایزه قرعه کشی تحویل 2 نفر از برنده ها شد.
سعی میکنیم از این به بعد با حمایت های شما هر هفته قرعه کشی داشته باشیم.
👤
آقا mohamada8562 عزیز، مبارکتون باشه!
✨
👤
آقا birang_ali عزیز، مبارکتون باشه!
✨
🔻
متاسفانه یکی از دوستان دیگه با نام کاربردی پایین پاسخ ندادن:
👤
M4hdiGaming</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/iaghapour/2895" target="_blank">📅 20:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2894">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIWH7u2nCMRrQOIbmIPiYQx1E5o6bV5xil_m5jIBXS8c5Xdns1FYDiNjaJ6Y6H6pRYzOvu6l_dxhRYO_PlBkU-Wtws9TFWKs6AN0KpfaJjVPeHjy9kOy58rExe6oJxjyA7XRFZkeap8aUhxtIoDhW9mZK8VOunFweuVinsPsJzxQDBeY31pUfgpHhh_Zjv_wRsIALoh8T7cRFk0PmI19smZWBoCy7NdTTgl0DIUPItnBkAvRYFIMQKU_r3Tdg5pxMriMirSRZYjjiV-Li-TTPVa8STq_6NdSLIqeHwhmEp6FiTevaU7PxO800ylE3iyLgS3Xde6N4ODNkSyFmOyReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
امکان شناسایی افراد با سیگنال‌های وای‌فای!
پژوهشگران موسسه فناوری کارلسروهه (KIT) روشی نوین توسعه داده‌اند که با تحلیل امواج رادیویی روترهای استاندارد Wi-Fi، هویت افراد حاضر در محیط را با
دقتی نزدیک به ۱۰۰ درصد
و تنها ظرف چند ثانیه شناسایی می‌کند.
🔻
نحوه کارکرد و جزئیات فنی:
📡
این فناوری مانند یک دوربین نامرئی عمل می‌کند که به‌جای نور، از امواج رادیویی برای تصویرسازی محیط استفاده می‌کند. فرد حتی اگر گوشی خود را خاموش کرده باشد، صرفاً به دلیل بازتاب امواجِ دستگاه‌های فعال دیگر در محیط، قابل شناسایی است.
🔓
این سیستم داده‌های «اطلاعات بازخورد شکل‌دهی پرتو» (
BFI
) را که به‌صورت عادی و رمزنگاری‌نشده میان کلاینت و روتر ردوبدل می‌شود تحلیل کرده و تصاویر محیطی و هویتی می‌سازد.
🔬
در آزمایش با ۱۹۷ شرکت‌کننده، مدل یادگیری ماشین توانست افراد را با دقت نزدیک به ۱۰۰٪ شناسایی کند؛ به‌طوری که زاویه دید و نحوه راه رفتن افراد نیز مانع تشخیص نشد.
⚠️
به دلیل حضور گسترده مودم‌ها در کافه‌ها، خیابان‌ها و منازل، این فناوری می‌تواند به یک بستر نظارتی نامرئی تبدیل شود./تک‌ناک
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/iaghapour/2894" target="_blank">📅 14:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2892">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqE85RqvlFaUs5_VKGhn_nrnfMvGYmfodur5MXhJ1VN3FGC1XkAq9DvrVqsYYi_XS0XLQt01Ehc9PRMq9JVQx6fxKbCA4tEPUTxeZhMMizbyMIRcJDTnbx02zdvQxAN21fXhMFOhw11yDmtqPCfm1pY9zB4m4JkfzsB7s-0rYEMd1d36r50QjCCZbFMkFqfWMXObFxsR0gyp93rcPzCwxuV13_-TpBO_AM4kK0Ykxy5DOQ22XU1KwFNhLAwdwM5peFQIHK8qjsAAvVHdWpVYnBy8ktRb-yzK-qE2VhdoGP6UzqyuRQAI_mOJkUjdk8CXRkZqAxc4Wr9YyOsNfejxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش بهترین تانلینگ شخصی با Dragon Fruit Relay
🔹
تو این آموزش قدم‌به‌قدم و به ساده‌ترین شکل ممکن بهتون یاد می‌دم که چطور سرور خارج رو به سرور ایران به هم متصل کنید و یک تانل پایدار، شخصی و پرسرعت (به‌عنوان بهترین مکمل برای پنل 3x-ui) بسازید. البته میشه با کامپیوتر شخصی هم تانل کرد :)
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت فرصت دارید.
#آموزش
#فیلترشکن
#تانل
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/iaghapour/2892" target="_blank">📅 18:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2891">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j28DgooscLUrVmDLO-30_aMqKV8FHE0NGyW2QGFfTYQGfgGzwDEpLMBvx7o1ENdzd3h2G916h0I0-h8-4oGznFf8_OeWhIl3Gg-1FCTLbw9ub7ucZzBzfo0YICKQDNuQYDjpmaK-90AbL7XDm20EsOAHl43LlL5zkoTRN2xjpRxujP4cYGgO-zbr0Qjd-BZ90ig9gzTNDHbjkbDFV3WTejnpPp4pRnyVY3CtPwOoiVKWfm6Zrk08oOO6ZvvpvsDFe9Z4Z4Mcq9kc6wOGXIayFfk9gWMw4vT97Yq7phYm32aUiMq2QRMyjr3GNtcQAw5BDRewsRNJORE38pJay5IliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍🏻
یکسری نکات درباره تبلیغات تلگرام و تبلیغات خودمون رو قبلا هم گفته بودم و خالی از لطف نیست دوباره هم بگم.
⚠️
درباره تبلیغات تلگرام:
تبلیغاتی که در پایین کانال، زیر آخرین پست نمایش داده می‌شوند، توسط سیستم تبلیغاتی خود تلگرام قرار گرفته و هیچ ارتباطی با ما ندارند. معمولا این تبلیغات نشانه هایی خاص دارن مثل ارتفا کم کادر تبلیغ و یا قرار گرفتن علامت
ضربدر
و نوشته شدن کلمه
Ad
در کادر.
🔸
استفاده از آن تبلیغات کاملاً با مسئولیت شخصی خودتان است.
🔹
درباره تبلیغات پست‌شده توسط ما:
هر تبلیغی که در کانال منتشر می‌کنیم، فقط برای همان محصول یا خدمت خاص نوشته شده (مثلاً اگر "کانفیگ VPN" تبلیغ می‌کنیم، فقط کانفیگ بخرید نه دامنه یا سرور و یا خدمات دیگه).
⚠️
لطفاً فقط همان محصولی که در متن تبلیغ ذکر شده را از تبلیغ‌دهنده خریداری کنید.
✅
فقط از تبلیغاتی که ما به صورت مستقیم در کانال پست می‌کنیم، استفاده کنید و همان محصول مشخص شده را بخرید.
✍🏻
اگر تبلیغ‌دهنده محصول دیگری را به شما پیشنهاد کرد، این خرید ارتباطی به تبلیغ کانال ما ندارد و مسئولیتش با خودتان است.
ممنون از همراهی شما
🙏</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/iaghapour/2891" target="_blank">📅 16:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2890">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستان عزیز، حتماً برای ارتباط با ما فقط از طریق ربات اقدام کنید.
به نظر می‌رسه یه سری از افراد دارن سعی می‌کنن با کپی کردن آیدی و عکس بچه‌های تیم ما، خودشون رو به عنوان پشتیبان کانال جا بزنن و سوءاستفاده کنن.
پس لطفاً برای ارتباط با پشتیبانی،
فقط و فقط
از طریق ربات رسمیِ
ارتباط با ما
پیام بدید تا مشکلی پیش نیاد.
🙏🏻</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/iaghapour/2890" target="_blank">📅 14:41 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
