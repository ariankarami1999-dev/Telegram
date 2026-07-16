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
<img src="https://cdn4.telesco.pe/file/ETp76c6biJqfO4-WKWsg4UcrPlENKBpSujwTBGKHzVoQrvcAYFqozNcLeLmJbkKEnmR60IOEEASsiuCnAc8ZDjCUz8XBbNoY88rNAQi5IQ3HqW_s0sB7BGlMN30ibF5whCieic5sQ8aDmcVeZAi1tmxqb3Jee3199BPGVmFQqpq4YUq8oPU-g7M92ki-cONUWbnE1eZfqIbnXoioNeRH0bVbIlBxglp9RfYoEkx6zVuLD3hWkEIWRw2WLf9FNGhO0kWv0q0arbS6kPyQdOlyrv8RppdGLfCPQLUAvrU7FkHXWzddfodyZl0sR7vHVBHiDilCLabArTzdLU708NqU0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 00:59:52</div>
<hr>

<div class="tg-post" id="msg-134872">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری/انفجارهای مهیب در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/alonews/134872" target="_blank">📅 00:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134871">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b324f9f1.mp4?token=QhbBSADcXTM_flaw3EbTvPg9kzBwjjKFZDXmI6B4pPVssmwHdUXc5w8Gc4JrHuYSVUYCL6qjE1yb4G--NgrfzOzUnLD7noTSSf__a2IcTuqVW84ES7j-IBblxRlYDoYqrYKcv_5vgy0G2A3S77BAe_V2BdSP3U6TDh26XAcbU6gBBxoeCuf5XALdc7c5v-5CAl8hb3-1vB4I4l64Wb3jyW6T4YnHOv7iDzDW98FYzIpxac5Td3BNCSfaZVu2nRDTA4WPMrJ1oJCmu2onpTEDScXXZKz8O7Iy7R8vNDFPDemHv7goAQS6kBq46ZvaKlIBLWzu3Eti25BzNM6aKteGpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b324f9f1.mp4?token=QhbBSADcXTM_flaw3EbTvPg9kzBwjjKFZDXmI6B4pPVssmwHdUXc5w8Gc4JrHuYSVUYCL6qjE1yb4G--NgrfzOzUnLD7noTSSf__a2IcTuqVW84ES7j-IBblxRlYDoYqrYKcv_5vgy0G2A3S77BAe_V2BdSP3U6TDh26XAcbU6gBBxoeCuf5XALdc7c5v-5CAl8hb3-1vB4I4l64Wb3jyW6T4YnHOv7iDzDW98FYzIpxac5Td3BNCSfaZVu2nRDTA4WPMrJ1oJCmu2onpTEDScXXZKz8O7Iy7R8vNDFPDemHv7goAQS6kBq46ZvaKlIBLWzu3Eti25BzNM6aKteGpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام: تفنگداران دریایی آمریکا از یگان یازدهم اعزامی دریایی، در تاریخ ۱۶ ژوئیه، عملیات بازرسی و بررسی را بر روی نفتکش «ام/تی وین یائو» در خلیج عمان انجام دادند.
🔴
تا به امروز، نیروهای آمریکایی مسیر ۳ کشتی تجاری را که تلاش کردند محاصره را بشکنند تغییر داده، یک کشتی که تمکین نکرد را مختل کرده، و سوار بر یک کشتی شده‌اند تا اطمینان حاصل کنند که محاصره دریایی مداوم آمریکا علیه ایران بهطور کامل رعایت می‌شود.
🔴
تنگه هرمز و آب‌های اطراف آن باز و آزاد باقی می‌مانند، به جز کشتی‌هایی که تلاش کنند محاصره آمریکایی را که دیوار فولادی تحمیل می‌کند نقض کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/134871" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134870">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
شرکت ملی گاز: صدای مهیب احتمالی امشب در نوشهر، مربوط به تست و هواگیری گاز خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/134870" target="_blank">📅 00:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134869">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/134869" target="_blank">📅 00:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134868">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
بخاطر جنوب لبنان، جنوب ایران رفت</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/134868" target="_blank">📅 00:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134867">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn0rmS3Oc1UH1tWlXM21SBgn_AYr8VLTgIk4sDv5geXnuHjPnyqAEPoUwTbEeVi22wTxapgTAk8t3wpLtgI7TcvLshD_oH_toZSRtWDRi1zm5wkklho_lKct71fMBRgRuLuxPLLNTXR9NANplxPgBS0oJ5MvrUZmL8lXX7nj5oh5ydVjtWcfQ8fu3WXZ2HjUrHoNrIyex6uC407a0VVQZ1UFi32_aSd6FDP5UGtEkm4iUV_bNjKey2AafYUFzygjXVMLczMl0k2v66EDqysSPnQ-8IUDbhxuu9EZKmKlyTsqlc70SWoAvspPMYyVf-pcdDWLrV_H_FLmMWjLtf1KXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌اکنون / وضعیت آسمان ایران و منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/alonews/134867" target="_blank">📅 00:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134866">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGSrVJchkn2C1svHn7q1t57cZmz0ioxQfR453_iSf0Y4F3UvkZMgY5Mvaabxgvet8wpSN7w11FbUrnfdBzYPKTuG2ebszuy7ZzCcsTl5BYhitK-rvZVa6TXAcb-vvUTmRQ9q5kTjvSS762DpyMkWBLYhaM3QrDfV9GWFQCQ46CzBDXNsMrOhkKd1Ged6aZDl0UUwzTQaM3Q9M1rapCVD0CLjqa1hWJml-6zVJ94CXagT0QwwZ7xaxxSh7GE6Tu4b7v_Lc4qaolW3QoO3QnMDLH7uJzvFDDyxajyqD3RXqbHLmP7v7LyYfx-NOVkVzdPHxMvaKLfjfiaLCpC9f_S8Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق داده‌های وبسایت فلایت رادار، یک جنگنده اف۳۵ در آسمان امارات کد اضطراری ۷۷۰۰ اعلام کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/134866" target="_blank">📅 00:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134865">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سنتکام: ما آماده انجام هر ماموریتی هستیم و در حال حاضر ۵۰ هزار نیرو در خاورمیانه داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/134865" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134864">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFfhhAueEI9I8KhNINYj2hdVwFS_jpNCHvmcqriSczFDvzqLgXFUuH9F9XmZFKPvBRdlfobc0vAYJoDke_mvzyzq3UiNymkZqZmU7by1c6_O2ZKTmHbJbDUH1z4syIGCaVaxfdKkMM1FSkA983PhqpO5fukY2UzipiO-5DAaulShkz9fVR8cp2UduPUQptTlBV-qCubFRBbvH3iBtF-hH6wYRAvfIweAVBxWVCDr1gPWPupYR4VU3OcksK2r20rZK2amA2A3H8uMDV6gpcOnsaAE75utlxqna2uhX8w1Urkg8HOwjMmFwDlHS4nS-QnEq88vdWBz6NUTLH1x0UYC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت موبایل تو بعضی از نقاط دچار افت کیفیت، کندی و اختلال شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/134864" target="_blank">📅 00:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134863">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر
Settings > Privacy and Security
شوید.
۱. مخفی‌کردن شماره تلفن
وارد
Phone Number
شوید و این گزینه‌ها را تنظیم کنید:
Who can see my phone number:
روی
Nobody
Who can find me by my number:
روی
My Contacts
بخش‌های
Always Allow
و
Never Allow
را نیز بررسی کنید تا استثنای ناخواسته‌ای وجود نداشته باشد.
تنظیم دوم مانع می‌شود افراد غریبه فقط با ذخیره‌کردن شماره شما، حساب تلگرامتان را پیدا کنند. البته طبق توضیح تلگرام، کسی که شماره‌تان را از قبل می‌داند و در مخاطبین خود ذخیره کرده است، ممکن است همچنان آن را ببیند.
۲. محدودکردن آخرین بازدید و آنلاین‌بودن
در بخش
Last Seen & Online
، گزینه را روی
My Contacts
یا
Nobody
قرار دهید. بخش استثناها را هم بررسی کنید. توجه کنید که هنگام تایپ‌کردن یا ارسال پیام، ممکن است وضعیت آنلاین شما برای مدت کوتاهی به همان شخص نمایش داده شود.
۳. محدودکردن عکس پروفایل
در
Profile Photos
، نمایش عکس را روی
My Contacts
بگذارید. برای حساب‌های کاری یا عمومی بهتر است از عکسی استفاده کنید که اطلاعاتی مثل محل زندگی، پلاک خودرو، محل کار یا اعضای خانواده را آشکار نکند.
۴. جلوگیری از شناسایی از طریق فوروارد
در بخش
Forwarded Messages
، گزینه را روی
Nobody
قرار دهید. با این تنظیم، وقتی دیگران پیام شما را فوروارد می‌کنند، نام فرستنده به پروفایل شما لینک نمی‌شود.
۵. جلوگیری از اضافه‌شدن به گروه‌های ناشناس
در
Groups & Channels
گزینه را روی
My Contacts
تنظیم کنید. در قسمت استثناها نیز فقط افراد مورداعتماد را قرار دهید تا افراد ناشناس نتوانند شما را مستقیماً وارد گروه یا کانال کنند.
۶. مخفی‌کردن IP در تماس‌ها
در بخش
Calls > Peer-to-Peer
، گزینه را روی
Nobody
بگذارید. در این حالت تماس‌ها از سرورهای تلگرام عبور می‌کنند و IP شما برای طرف مقابل آشکار نمی‌شود؛ ممکن است کیفیت تماس کمی کاهش پیدا کند.
۷. فعال‌کردن رمز دومرحله‌ای
وارد
Two-Step Verification
شوید و یک رمز قوی و متفاوت از رمزهای دیگر انتخاب کنید. ایمیل بازیابی نیز باید رمز قوی و تأیید دومرحله‌ای داشته باشد. با فعال‌کردن این قابلیت، صرفاً داشتن سیم‌کارت یا کد پیامکی برای ورود به حساب کافی نخواهد بود.
۸. بررسی دستگاه‌های متصل
در
Devices
یا
Active Sessions
، همه موبایل‌ها، رایانه‌ها و مرورگرهای متصل را بررسی کنید. هر دستگاه ناشناس یا قدیمی را ببندید؛ در صورت تردید، از گزینه
Terminate All Other Sessions
استفاده کنید.
۹. قفل‌کردن خود برنامه تلگرام
گزینه
Passcode Lock
را فعال کنید و قفل خودکار را روی زمان کوتاه قرار دهید. اثر انگشت یا تشخیص چهره را هم فعال کنید تا در صورت بازبودن قفل گوشی، دیگران نتوانند تلگرام را باز کنند.
۱۰. مدیریت مخاطبین همگام‌شده
اگر نمی‌خواهید فهرست مخاطبین گوشی در تلگرام ذخیره و همگام‌سازی شود،
Sync Contacts
را خاموش و از گزینه
Delete Synced Contacts
استفاده کنید. همچنین می‌توانید
Suggest Frequent Contacts
را غیرفعال کنید.
۱۱. برای گفتگوهای بسیار حساس از Secret Chat استفاده کنید
گفتگوهای عادی تلگرام در فضای ابری ذخیره می‌شوند. برای مطالب حساس از
Secret Chat
استفاده کنید؛ این گفتگوها رمزنگاری سرتاسری، وابستگی به همان دستگاه و امکان حذف خودکار پیام دارند.
۱۲. کد ورود را هرگز برای کسی نفرستید
کد ورود تلگرام، رمز دومرحله‌ای، QR ورود، اطلاعات بانکی و فایل‌های ناشناس را در اختیار کاربران یا ربات‌ها قرار ندهید. تلگرام تأکید می‌کند که با ربات‌ها مانند افراد غریبه رفتار کنید.
برای حریم خصوصی بیشتر، بهتر است نام کاربری تلگرام، عکس پروفایل و نام نمایشی شما با شبکه‌های اجتماعی دیگرتان یکسان نباشد؛ چون حتی با مخفی‌بودن شماره، امکان تطبیق هویت از طریق این اطلاعات وجود دارد.
⭕️
حتما از تلگرام رسمی استفاده کنید و از Google Play یا App Store نصب کنید همچنین اگر تلگرام غیر رسمی دارید حذف کنید.
#حریم_خصوصی
#امنیت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/134863" target="_blank">📅 00:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134862">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
گویا پل فلزی بندرعباس رو هم زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/134862" target="_blank">📅 00:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134861">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-poll">
<h4>📊 به نظرتون چی میشه؟</h4>
<ul>
<li>✓ تهاجم گسترده زمینی و هوایی آمریکا</li>
<li>✓ توافق میشه</li>
</ul>
</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/134861" target="_blank">📅 00:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134860">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فارس:
حمله به پل خمیر شش کشته و زخمی داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/134860" target="_blank">📅 00:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134859">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
برق مناطقی از کیش قطع شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/134859" target="_blank">📅 00:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134857">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjiDdns_BwCEtuO_bMVDQ8USU-5pRUIVTkMkrArWlric0FofMhNAvOqqK0zursFcmUkTGHUpgPhHVijF4uf3pNZssOacBvXz5PTheQTWocqS_rt2JPLenZDeei9VX5WCUbnJgO81cRJfju7zauJKea8ROWKBUtgm9yKKXi2hsZc-f0Zyjzz-7G2UZeVdVa-hhd6UycYNleZa8Lem-jVyh86wh3eQJ4kWNqA0ESaK8uCSu8-LMKISgHRLHvfsGoa7qn0po9PiuInz6bb9dA4xYInfcI-eFiu1GJMJXTNSdSf0CzVBy2gR4IWs5igsJyucqWc8tDNPVgudRiypPte2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukkv3Hpag9uOmHhrRK-19UHz_d2s8shPD6ZF_kyirniMfqS_OS5NJ3bgZxFvoG0H4ylXEkJAbURjGkEdUmZypeZE7czcT0T2T2ERoX1xxpLcmffhvJjH63U9dS8HKfmqTenBFS10KOOt_lDpDvvz3YBd6uLRDORzIcP72eSd4Ui_fim76SugwiFydeO22ZLbhwqFPAgmE3_OwS_GQZ0Wu4qsGsFb-Qi0KUotB-URXfmNvca6MgqOWMof4_vrn5nEoockJof8IMm8ddFIIbaILfEc-WIBWyxRRxNYNh8MT0EtNS8E89rche9Xn-yxMc8qCEn6OgOOsdl8JDtca_BdYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پلی که حملات شب گذشته آمریکا آن را هدف قرار داد، حامل بزرگراه شماره ۷۶ است؛ جادهای اصلی که بندرعباس را به شهر لار و از آنجا به شیراز متصل میکند.
🔴
این بخش، بخشی حیاتی از زیرساخت حملونقل کالاهای تجاری به مقصد و از مبدأ بندرعباس به شمار میرود و همچنین جابهجایی مسافران میان استانهای هرمزگان، فارس و مرکز ایران را پوشش میدهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/134857" target="_blank">📅 00:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134856">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-3eWT4yXWYWoM1B38lMKRcdfAGCY2Fy0pZFLD4RwbWRTC0C1SX4Xe_2Hb4qRfCjR4_2k-cfZP1bUTVNz-CMWOUwHEbYDIbnC_qix8-Id7eusSslzSMs8P5rGzea8qspuGYMYwkjjsheQefOH1YeccpUgFVJqg1mCjEDcFwKU5GTC2jQ4Pyoi9zkrI523AZ8-TfzL5RbRUrvEffNICrr1vTFotQzgJITd1FZQ9tVMknyCFZEITISLgPkiYm8hMVzhW6gpqjmXLNXQEXUnGz9bpSLytJQHE77AlonKGZeQcP2AaiZ1VGAiDlWTrtBHk355mTRHzTaAygS9RjyAlrZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/134856" target="_blank">📅 00:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134855">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX6V0itlGpigBlM-Ag6q4tdtV_CXyvBAcYYlv0PfK3XNPyGUPNv3TX5QEsvX5Gl6kyOgO3bgV6Ih6re5lqy9KBUpXoCWdwx0GqBzUUZkiyehq8cy8YQ49guNwWwb1_TvzQ-AjMmwx0u7qPs6wsmQY65lRlv8YQ4tUt3IsiX9VxKhIPgz1pIBeiocmqs9sZovmUQNJaZfetierj8B8D6Uvz30KbM5eTzpkIzAaOt1TAvG6IMl0DjLyzrFPidg103y6_xWb7SeUDQYMaMVEOhRTN09Yq2w5RYwX7GbCuyxcjbm1zwlqCK7-0vPFM-HQZJCshC4ntNh7VTZsWxhR3uTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین تصویر واضح از پل‌ِ بندرخمیر که مورد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/134855" target="_blank">📅 00:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134854">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭕️
الونیوز فقط در تلگرام
💬
و توییتر
❌
فعال هستش
🔴
سایر شبکه های اجتماعی چه داخلی چه خارجی که با نام الونیوز فعالیت می‌کنند مرتبط به ما نیست و پیشنهاد میکنم که لفت بدید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/134854" target="_blank">📅 00:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134853">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/134853" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134852">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری/صدا و سیما: دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی آمریکا هدف قرار گرفته شده و ۲ نفر مصدوم شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/134852" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134851">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/134851" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134850">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/134850" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134849">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری/صدا و سیما: دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی آمریکا هدف قرار گرفته شده و ۲ نفر مصدوم شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/134849" target="_blank">📅 00:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134848">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d13ca129.mp4?token=DY4-qOfgPNH9xaWSI1Kn1uh54qgoQaNaha8hUXEUqZ37Tfa81OY2xJqizabLuhFOvi922Rc97ckMCYSFUNS2esYZEx67-xy7UXsngX_blOLkcplENqZbsPpKRDy_MfJp5Y22PwIq2sxs7lwBzvwX1i5EQnRay3RiFGLb-VrObSt7vVISpsQ20bh1zZm9oQXfAO2jg_9W82cZ6xgOEwlTPLayY2e2tF9QbKtTccvoOWMW2GPMc6iAlRqsxvOG78YILoH7c4Sm6YN_i3R0I_RZ7y_1TFkqJ-4z6Sb2tLTO_F01LCAgrgkrNG7tcW-AN4xRtPzWufnYUEGnNZDQeFWabw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d13ca129.mp4?token=DY4-qOfgPNH9xaWSI1Kn1uh54qgoQaNaha8hUXEUqZ37Tfa81OY2xJqizabLuhFOvi922Rc97ckMCYSFUNS2esYZEx67-xy7UXsngX_blOLkcplENqZbsPpKRDy_MfJp5Y22PwIq2sxs7lwBzvwX1i5EQnRay3RiFGLb-VrObSt7vVISpsQ20bh1zZm9oQXfAO2jg_9W82cZ6xgOEwlTPLayY2e2tF9QbKtTccvoOWMW2GPMc6iAlRqsxvOG78YILoH7c4Sm6YN_i3R0I_RZ7y_1TFkqJ-4z6Sb2tLTO_F01LCAgrgkrNG7tcW-AN4xRtPzWufnYUEGnNZDQeFWabw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب عزیزم
❤️
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/134848" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134847">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فووووووری/یک مقام آمریکایی به ان بی سی: همانطور که رئیس جمهور گفته بود این هفته حمله به زیرساخت‌ها، پل‌ها و نیروگاه‌ها انجام میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/134847" target="_blank">📅 00:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134846">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
راه‌های ارتباطی و زیرساخت‌های مهم جنوب ایران رو یکی‌یکی دارن می‌زنن، ولی حکومت ملاها مثل همیشه نه جون مردم براش مهمه، نه امنیت کشور و نه آینده ایران.
🔴
با این اتفاقاتی که داره می‌افته، بعید نیست دارن برای حمله زمینی برنامه ریزی می‌کنن؛ جنگی که باز هم هزینه‌ش رو مردم بی‌دفاع ایران باید بدن، نه اونایی که خودشون و خانواده‌هاشون جای امن نشستن.
🔴
آخرِ همه این ماجراها یه چیز کاملاً روشنه: جمهوری اسلامی رفتنیه و سقوطش حتمیه. فقط معلوم نیست قبل از اینکه به زباله‌دان تاریخ بره، قراره چقدر خون از مردم بگیره، چقدر کشور رو ویران کنه و چقدر هزینه روی دست ملت بذاره، اما جنایت‌ها و ویرانی‌هایی که به جا گذاشته، هیچ‌وقت از حافظه مردم ایران پاک نمی‌شه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/134846" target="_blank">📅 00:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134844">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری / قشم ۴ انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/134844" target="_blank">📅 00:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134843">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd604b00c.mp4?token=VVGDvKJBn9Gw5uBAxRqVeHEluNN4H-j0l_mGLrkwVj9ufHyyLQwEHLThRQ8sFHFPwv_6THfW1NpZTDs9YE8on9ZHzuVwXjAQNdahCOXg5BLzrz9i6HqxejXnprT92WX_WXHPHN1LUMSsTgq2GgpwLPhppKHYGQdSe15ht_l7JF8T88RXRAUf--BP9jdZmiGL9Dc9AnTp33ML30J_7P0b3j6DGszrLSKf3TWJpkWVUzdccGuc3wd-doA_Am46vcTv7sgAwfvIF3ieOo-iVZ32AVWbnhup3CCuOqzQmmfsdJgA612Jz0K1q0F5yovHksikyKIE8xvlHvX1Y-a5Wjwz9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd604b00c.mp4?token=VVGDvKJBn9Gw5uBAxRqVeHEluNN4H-j0l_mGLrkwVj9ufHyyLQwEHLThRQ8sFHFPwv_6THfW1NpZTDs9YE8on9ZHzuVwXjAQNdahCOXg5BLzrz9i6HqxejXnprT92WX_WXHPHN1LUMSsTgq2GgpwLPhppKHYGQdSe15ht_l7JF8T88RXRAUf--BP9jdZmiGL9Dc9AnTp33ML30J_7P0b3j6DGszrLSKf3TWJpkWVUzdccGuc3wd-doA_Am46vcTv7sgAwfvIF3ieOo-iVZ32AVWbnhup3CCuOqzQmmfsdJgA612Jz0K1q0F5yovHksikyKIE8xvlHvX1Y-a5Wjwz9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پل لار - بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/134843" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134842">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سر فشار رقاصه‌های پرچم ایرانمون داره نابود میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/134842" target="_blank">📅 00:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134841">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فووووووری/راه آهن بندر عباسو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/134841" target="_blank">📅 00:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134840">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dv2tbnWgJ4gR6kxO4bSLI1BZ9z3IqYY8ooTb0E4DfXoGfSzRvjv2hFyeem09NlzAdiLQ15Tu0VZsQB-7P9qktY-sfWv6dDy52xXPMznroa-U-QRnNvnz2jWbibR-tlhUXVtBX-XVXQwdIlCbR0sdNi-lLX7NamnvSN7zNhEph0YMDQkysby62AW9PcbXdRPB0y7CalAjmvqvnjXpJFhAeS1SC-NaZlWbblw1Oesm1qPglUgUx1I3go0eYs1IbygyzPwq8V2139Nxc8xQhpFtxl-VGse-PSazkjQgMF5hKTkxevYE_aIefDxsbR16W4PKV8NK6HjQR7cvp96dl0085A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: آرزوی شهادت دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/134840" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134839">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
صداوسیما: صدای ۴ انفجار در محدوده ساحل جنوبی قشم شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/134839" target="_blank">📅 00:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134838">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری/سی‌بی‌اس به نقل از مقام آمریکایی: دستورالعمل‌های مربوط به حملات آمریکا به‌روزرسانی شده‌اند تا شامل پل‌ها و اهداف ارتباطی و تدارکاتی شود، با هدف افزایش فشار بر ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/134838" target="_blank">📅 00:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134837">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
مقاومت اسلامی عراق برای کشتن ترامپ ۱۰ میلیون دلار جایزه تعیین کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/134837" target="_blank">📅 00:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134836">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
فعالیت جنگنده ها بر فراز منامه، بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/134836" target="_blank">📅 00:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134835">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
تسنیم: آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/134835" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134834">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
به لحظات ملکوتی قطع اینترنت داریم نزدیک میشیم.
🔴
خشاب های VPN خودتون رو پر کنید.</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/134834" target="_blank">📅 23:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134833">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
تصاویری از حمله به پل در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/134833" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134832">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
پل کهورستان بندرعباس هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/134832" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134831">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
تصاویری از حمله به پل در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/134831" target="_blank">📅 23:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134830">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
تصاویری از حمله به پل در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/134830" target="_blank">📅 23:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134829">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مهر: دقایقی پیش، صدای حدود ۶ انفجار پیاپی در حوالی شهرستان حمیدیه شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/134829" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134828">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
انفجار در کهورستان بندرعباس.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/134828" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134827">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3efbf07c20.mp4?token=enJBJ-oPFKHOZwhirBGdv4R1QuCP6I1b10GXL1GfYa1Uc9Ct8bJzSguBUaCEinQzaUlbCnsknIT8W8_ueFIW6dABcMGgRaYufAWfLm9Rtq4s4Kvngd3aJhu2_MkMlGKioDETw_2cnyBZC7ZjiQH28fJ9l2dey-662sD6V5k4y68HP50nhNPA6kYDhW-QdM48IawsrtiRXOK-yV_M4EpQ9-p4sLLiNXRArPAps9cAVwTGu7Ax-C0UdOHvYWwHbfWXgut--0AFbG6fq-tlj_m7qySmpGbhJcYUaJ5aN02QesF-Ql1h1JgKdE65JUR_TctAewgwGONDUrZwuNr0ZX18FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3efbf07c20.mp4?token=enJBJ-oPFKHOZwhirBGdv4R1QuCP6I1b10GXL1GfYa1Uc9Ct8bJzSguBUaCEinQzaUlbCnsknIT8W8_ueFIW6dABcMGgRaYufAWfLm9Rtq4s4Kvngd3aJhu2_MkMlGKioDETw_2cnyBZC7ZjiQH28fJ9l2dey-662sD6V5k4y68HP50nhNPA6kYDhW-QdM48IawsrtiRXOK-yV_M4EpQ9-p4sLLiNXRArPAps9cAVwTGu7Ax-C0UdOHvYWwHbfWXgut--0AFbG6fq-tlj_m7qySmpGbhJcYUaJ5aN02QesF-Ql1h1JgKdE65JUR_TctAewgwGONDUrZwuNr0ZX18FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حمله به پل در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/134827" target="_blank">📅 23:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134826">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری/ طبق گزارشات، یک پل در بندرعباس هدف قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/134826" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134825">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/134825" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134824">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری/حملات شدید به قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/134824" target="_blank">📅 23:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134823">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری/ورودی های پایگاه زیرزمینی عقاب 44 ایران جمهوری اسلامی ایران توسط آمریکا بمباران شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/134823" target="_blank">📅 23:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134822">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
فوووووووووری/حمله زمینی   ️رشیدی کوچی؛ نماینده سابق مجلس: حمله‌ زمینی آمریکا به ایران قطعیه. اگه تا الانم حمله نکرده به خاطر گرمای شدید هواست
✅
@AkhbareFouri</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/134822" target="_blank">📅 23:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134821">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری / حمله به فرودگاه ایرانشهر ، استان سیستان و بلوچستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134821" target="_blank">📅 23:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134820">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سنتکام: پس از پاکسازی مین‌ها، گذرگاه‌هایی در تنگه هرمز بازگشایی شده و در حال حاضر دریانوردی در این منطقه ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/134820" target="_blank">📅 23:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134819">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سخنگوی سنتکام: ما آماده انجام هر ماموریتی هستیم و در حال حاضر ۵۰ هزار نیرو در خاورمیانه داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134819" target="_blank">📅 23:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134817">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507e824d84.mp4?token=AyfrSQl--JyKPc5csiH5_YnbMtygF20lCfsKAFTcc3dZNRm4p2FCjNFSrLWpwwAFjC3EbE5CB6kEP-a4rlomFDvFvGL0K4Zo0M7_BLnjoJEyYHtRkHrTLcW7M9WI9OBE6eh7ccBX9wMZlb-lqaMbVRCUgp3fM2BK_3KnlDhY_6KWfcgVZy0w16V8CKtZ43BujFBHSjNWN8m-D9Qgy4Y5xzo2sc9nJEkgkbpJ7olXyAr5Y6ad_yj_dgYIDh_AcE8sSKSr3iLOWdf78VbfHXlc_2y5K_nxkRaFRYAgnDncKt2X6qtj6vMhqo_lEvP9kzRU-RQNr-cP9FTdG39R0P4Phw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507e824d84.mp4?token=AyfrSQl--JyKPc5csiH5_YnbMtygF20lCfsKAFTcc3dZNRm4p2FCjNFSrLWpwwAFjC3EbE5CB6kEP-a4rlomFDvFvGL0K4Zo0M7_BLnjoJEyYHtRkHrTLcW7M9WI9OBE6eh7ccBX9wMZlb-lqaMbVRCUgp3fM2BK_3KnlDhY_6KWfcgVZy0w16V8CKtZ43BujFBHSjNWN8m-D9Qgy4Y5xzo2sc9nJEkgkbpJ7olXyAr5Y6ad_yj_dgYIDh_AcE8sSKSr3iLOWdf78VbfHXlc_2y5K_nxkRaFRYAgnDncKt2X6qtj6vMhqo_lEvP9kzRU-RQNr-cP9FTdG39R0P4Phw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده های آمریکایی به طور گسترده در آسمان بحرین پرواز می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/134817" target="_blank">📅 23:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134816">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
صدای ۲ انفجار در شهر بوشهر شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/134816" target="_blank">📅 23:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134815">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1bc0ea2b.mp4?token=hSplCoue1PWoKbxvphoC02lOR6IBYQclQkC3KLFOGOtqTviJloO8qJmfHP62P54j--lr5YCOzj9ogJ58VkGmboGoFs5YMVYlS3xFB7BGGSyMnnZzLARkwYwAx6tEuoKbcB6i-LXOE5YkaIwQnsRT-gJwTzFz0pelWKU-3VCnb1emJsGPu3gXlbfUxXWpYIMyr-UDEYNCehB5UBDlPW1nZV0pqajejpAExtG3L0bqCGfbw1ykkfEZEesNKi392BPfLsj0LRcJ0UCADbi9Tq0b81YoJ-MtRvyeeDcxJYDzXD0RBj0oUnbPsEFIxfJ4FWZD_PC1eh8US3xVKtcuuB1hgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1bc0ea2b.mp4?token=hSplCoue1PWoKbxvphoC02lOR6IBYQclQkC3KLFOGOtqTviJloO8qJmfHP62P54j--lr5YCOzj9ogJ58VkGmboGoFs5YMVYlS3xFB7BGGSyMnnZzLARkwYwAx6tEuoKbcB6i-LXOE5YkaIwQnsRT-gJwTzFz0pelWKU-3VCnb1emJsGPu3gXlbfUxXWpYIMyr-UDEYNCehB5UBDlPW1nZV0pqajejpAExtG3L0bqCGfbw1ykkfEZEesNKi392BPfLsj0LRcJ0UCADbi9Tq0b81YoJ-MtRvyeeDcxJYDzXD0RBj0oUnbPsEFIxfJ4FWZD_PC1eh8US3xVKtcuuB1hgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک موشک از کویت به سوی اهواز در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/134815" target="_blank">📅 22:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134814">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
به اهواز با موشک تاماهاک حمله کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/134814" target="_blank">📅 22:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134813">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
چندین انفجار پی در پی در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/134813" target="_blank">📅 22:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134812">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
چندین انفجار پی در پی در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/134812" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134811">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
اهوازو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/134811" target="_blank">📅 22:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134810">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
مقام یمنی: عربستان ۹ دقیقه پیش از فرود هواپیمای ایران، فرودگاه صنعاء را بمباران کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/134810" target="_blank">📅 22:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134809">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح: امنیت کامل تنگهٔ هرمز هنگامی برقرار می‌شود که آمریکایی‌ها نباشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/134809" target="_blank">📅 22:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134808">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
صداوسیما: شنیده‌شدن صدای ۳ انفجار در غرب بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/134808" target="_blank">📅 22:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134807">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزیر خارجه اردن: هیچ پایگاه آمریکایی در اردن وجود ندارد!
🔴
وزیر امور خارجه اردن مدعی شد: روایت ایران مبنی بر وجود پایگاه‌های نظامی آمریکا در اردن نادرست است.
🔴
هیچ پایگاه آمریکایی در اردن وجود ندارد، فقط سربازان آمریکایی به عنوان بخشی از همکاری نظامی بین ما و واشنگتن حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/134807" target="_blank">📅 22:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134806">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3f23f983.mp4?token=rkdQLyHJ3cO6OE1zIl-wjR3OFUltZai5TJBnRhRc5E38hgp9grigq0D6Ok130JMl0VxFPK8maLRl2odR5RKfMeNSA-Pffecmz8W15O-psXwwP23KHOKidxaLO-pvwXXlWTBcZ3hEdOc2-1hzIoGAeQpfH9I4GsUZE71DjSoAUGx3JgVL71qqB-uKzHdM6WcYVw3v8Mju6LXbXinXsQKRH-j8FXXID6BdZEy2qUh6-RpJDys99cSp5yEd46DK1ROGPnzBq2HlwrqbQxG0326nOtnGNmncsbW5PlMC1FHetdOvzelHdPX9VtJGsfKqLpKhzrioFJUtFqdwQbfMr3rsYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3f23f983.mp4?token=rkdQLyHJ3cO6OE1zIl-wjR3OFUltZai5TJBnRhRc5E38hgp9grigq0D6Ok130JMl0VxFPK8maLRl2odR5RKfMeNSA-Pffecmz8W15O-psXwwP23KHOKidxaLO-pvwXXlWTBcZ3hEdOc2-1hzIoGAeQpfH9I4GsUZE71DjSoAUGx3JgVL71qqB-uKzHdM6WcYVw3v8Mju6LXbXinXsQKRH-j8FXXID6BdZEy2qUh6-RpJDys99cSp5yEd46DK1ROGPnzBq2HlwrqbQxG0326nOtnGNmncsbW5PlMC1FHetdOvzelHdPX9VtJGsfKqLpKhzrioFJUtFqdwQbfMr3rsYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلد مارشال محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای‌عالی امنیت‌ملی رفت.
🔴
مجری: چه مسیری بود؟
🐸
محسن رضایی: نمی‌دونم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134806" target="_blank">📅 22:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134805">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
گزارش انفجار در چابهار و کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/134805" target="_blank">📅 22:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134804">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpR1RN2CKX1QyK8GAzazDpF4JT692xO06Xd4y4BMdwOks25MstwCUn2QFaClTqbE6errP-Im6iNzjOd4xF6UEFbrrQS6ZtzTKXRDtPYWBqHPjh-2af1-EmJRJ6EllZ6a6H2rknA_q-bFu18Tw5ddPC1EXnFJ1rumR6e7onElqugA0Poz6PpWgRp_wr5B3gOgM2nhbWh71-Z97td2V5VeKy-l0AHup5Onk4Z72hByK5uZ2q02dpgm54cUvB32DM_sYPdVO4dmU6203Tqi3DdKfyKnCMAydUniraOF_oFEn6y4_0C96m4tNI4v3SJiOeJGlhZfO7BFRyBv9zFfT2HxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: موج جدیدی از حملات علیه ایران آغاز شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/134804" target="_blank">📅 22:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134803">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
اکنون کل ارتش و سپاه در نیمه جنوبی ایران تحت بمباران هوایی آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134803" target="_blank">📅 22:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134802">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
قشم صدای ۲ انفجار به گوش رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/134802" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134801">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
انفجار های متعدد در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134801" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134800">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کارولین لیویت، سخنگوی کاخ سفید:
در حال حاضر دونالد ترامپ و جی‌دی ونس در مورد ایران دقیقاً بر سر یک صفحه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134800" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134799">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
انفجار های متعدد در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134799" target="_blank">📅 21:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134798">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134798" target="_blank">📅 21:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134797">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سخنگوی کاخ سفید، در مورد اظهارات جی‌دی ونس، معاون رئیس‌جمهور، درباره اسرائیل: ترامپ قطعاً موافق است که بله، کشورهای خارجی قطعاً سعی می‌کنند افکار عمومی آمریکایی را متقاعد کنند.
🔴
در این مورد هیچ شک و شبهه‌ای وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134797" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134796">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سخنگوی کاخ سفید:  ما مردم مهربانی هستیم و بهترین کشور جهان را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134796" target="_blank">📅 21:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134795">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a427bd448f.mp4?token=LhKeuherjIsNPyo2R0lJlN8xUmm3d3aJpaO8AKrc0KsgcxDHabsU_xfuXvZt1L3eHWUyZseTvwYyAbMKrxjyqtDLbso9N4iiu1pCruOqqY80H2rpVuufu5OyRA9s59XI-Aqah_874M7buPfuNRYmxpTyM9twg6K-u2Xsc_qYtAC0IJO-yqneMpwcKxcR6dGoBCBj2dG9oWCUo5Vf0x_Y96f4CTSXRCwOOxT51FEpOFDS3UVLGfwUO5FGxRTvCVl-XVvTX-Mpp_DNXDYZKj9M7r9f3WbTkgmOVPe7ScQw-f2l0_BXzC3TMyiZBFAAxB7xQKJnIUgbiDE4efZ4QU9YRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a427bd448f.mp4?token=LhKeuherjIsNPyo2R0lJlN8xUmm3d3aJpaO8AKrc0KsgcxDHabsU_xfuXvZt1L3eHWUyZseTvwYyAbMKrxjyqtDLbso9N4iiu1pCruOqqY80H2rpVuufu5OyRA9s59XI-Aqah_874M7buPfuNRYmxpTyM9twg6K-u2Xsc_qYtAC0IJO-yqneMpwcKxcR6dGoBCBj2dG9oWCUo5Vf0x_Y96f4CTSXRCwOOxT51FEpOFDS3UVLGfwUO5FGxRTvCVl-XVvTX-Mpp_DNXDYZKj9M7r9f3WbTkgmOVPe7ScQw-f2l0_BXzC3TMyiZBFAAxB7xQKJnIUgbiDE4efZ4QU9YRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی کاخ سفید
:
این پربیننده‌ترین و موفق‌ترین جام جهانی در تاریخ آمریکا بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134795" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134794">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سخنگوی کاخ سفید: هدف اینه که قیمت‌ها ثابت بمونه و ایران هیچ‌وقت به سلاح هسته‌ای نرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/134794" target="_blank">📅 21:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134793">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ded96abd.mp4?token=DUP3aLpEjCzu5LVU79a--vIfhd-Fvr_nEDLt5KPcH4Zju4rJL_WxMHZA_Cojhvt6GXPdcQZIAizstnvmuMs6mqejodss7ZT7iZChyBDi5iFdylahohO5lO-BS0teJToqwT7cf2yxRxnxDV7mQTjURp1k6wYn6OYgVVaDvmWvNyY_AW0v12PJC3km0LkKqWuoFRkcW38B3LXzzUylqpkSr3GlXC2b3bUamATW8DN6c1MiDly-8JNC0D39CwGGKj183R0pRZ3DFnTr8qkQ1cpeCxnE1-_g3ONpZtqAwP0UxJ1Ro9WbmxQ_6d5C3cC8iB1lWy6uhjsEhd21axBqajiPJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ded96abd.mp4?token=DUP3aLpEjCzu5LVU79a--vIfhd-Fvr_nEDLt5KPcH4Zju4rJL_WxMHZA_Cojhvt6GXPdcQZIAizstnvmuMs6mqejodss7ZT7iZChyBDi5iFdylahohO5lO-BS0teJToqwT7cf2yxRxnxDV7mQTjURp1k6wYn6OYgVVaDvmWvNyY_AW0v12PJC3km0LkKqWuoFRkcW38B3LXzzUylqpkSr3GlXC2b3bUamATW8DN6c1MiDly-8JNC0D39CwGGKj183R0pRZ3DFnTr8qkQ1cpeCxnE1-_g3ONpZtqAwP0UxJ1Ro9WbmxQ_6d5C3cC8iB1lWy6uhjsEhd21axBqajiPJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاخ سفید درباره ایران:این تنگه برای کشتی‌هایی که به بنادر ایران رفت و آمد ندارند، باز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/134793" target="_blank">📅 21:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134792">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=IMfgET8XsKAHQ5OqvhDyTksdC3qtWS_FRRUUQbp0wpZS0L4KoMDL6cp31pLaWryRKqjufckl9j0sPvX8YQb17JO3Sas8TqCgct8FTlxqW8wawy4-utCmLwU1qu9FwBKd3-EzS5eZJDrnveNmzbYmKt8byA8mJooQrfCW_QcvF0cLNRtSY_0Jc7ktQ4Vg39eG3nQtF813whxNtcOErTaWBs3FfJRIVBopD5Bn82cdUr2Ebjvk7yFjMPJo6VZ7GFG6ij5Jx8ATHFcQU64T4SEft_Cm6MVmo494Njwk28z9d458T1ajQHG0Qd3Qlny5BW5Lh_AG8tUmCJIeyrRUOlQtKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=IMfgET8XsKAHQ5OqvhDyTksdC3qtWS_FRRUUQbp0wpZS0L4KoMDL6cp31pLaWryRKqjufckl9j0sPvX8YQb17JO3Sas8TqCgct8FTlxqW8wawy4-utCmLwU1qu9FwBKd3-EzS5eZJDrnveNmzbYmKt8byA8mJooQrfCW_QcvF0cLNRtSY_0Jc7ktQ4Vg39eG3nQtF813whxNtcOErTaWBs3FfJRIVBopD5Bn82cdUr2Ebjvk7yFjMPJo6VZ7GFG6ij5Jx8ATHFcQU64T4SEft_Cm6MVmo494Njwk28z9d458T1ajQHG0Qd3Qlny5BW5Lh_AG8tUmCJIeyrRUOlQtKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی کاخ سفید: ایران همچنان با ما در حال مذاکره است!
🔴
کارولین لیویت:
«ایران همچنان به شدت با ایالات متحده آمریکا در حال گفتکو است و ابراز می‌کند که خواهان توافق با ماست، زیرا آنها از سوی نیروی نظامی ایالات متحده ضربات ویرانگری را متحمل می‌شوند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134792" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134791">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سخنگوی کاخ سفید:  دلیل حملات اخیر به ایران، نقض تفاهم‌نامه از سوی ایران است؛ آنها تعهد امضا کرده بودند که به کشتی‌های تجاری عبوری از تنگه هرمز شلیک نکنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/134791" target="_blank">📅 21:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134790">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزارت دفاع ترکیه : کار روی سامانه S-400 ادامه داره؛ هر تغییر مهمی اعلام می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134790" target="_blank">📅 21:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134789">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
کاخ سفید: ترامپ روز یکشنبه آینده در فینال جام جهانی فوتبال شرکت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134789" target="_blank">📅 21:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134788">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
کانال ۱۵ عبری: ایالات متحده در حال آماده‌سازی برای گسترش حملات خود علیه ایران از نظر دامنه و تعداد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134788" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134787">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سخنگوی کاخ سفید، لیویتِ : ترامپ فردا به نیویورک میره
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134787" target="_blank">📅 20:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134786">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9a850642.mp4?token=S2iP0nd3Dm2BXTF_SfrTf839GRQjwUGoHVEGWU4shuGRteQ-j08ThJUZeYs7jRYkShinDXSSoMKe9hJ-0xzygGOYMqcbyXcNl5o5DlQDW2oxP40pUtV0Sv9PXhMVQ-CqWplFOaQx5jLgVhTGRFFpen02jLt7zbO6ZyzFTHIwOiRsoBiPWwbHmvZ-xiZ2hLY90iMkpMVLrcA1uTtcMxwMjvJSJ4WB1fooWqqQxh7JvBDBqzLPYUePQFH6jYQf6p0a6KGqBXmdSEXks5eZrMrVQikWGlupVhnDJ7_Syo8zuDYVRQtkEOeCCs5T68adumZqsKFud75E3WRy7za1OJb0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9a850642.mp4?token=S2iP0nd3Dm2BXTF_SfrTf839GRQjwUGoHVEGWU4shuGRteQ-j08ThJUZeYs7jRYkShinDXSSoMKe9hJ-0xzygGOYMqcbyXcNl5o5DlQDW2oxP40pUtV0Sv9PXhMVQ-CqWplFOaQx5jLgVhTGRFFpen02jLt7zbO6ZyzFTHIwOiRsoBiPWwbHmvZ-xiZ2hLY90iMkpMVLrcA1uTtcMxwMjvJSJ4WB1fooWqqQxh7JvBDBqzLPYUePQFH6jYQf6p0a6KGqBXmdSEXks5eZrMrVQikWGlupVhnDJ7_Syo8zuDYVRQtkEOeCCs5T68adumZqsKFud75E3WRy7za1OJb0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوریه اعلام کرد محموله‌ای شامل موشک‌های دوربرد، موشک‌های ضدزره و پهپاد رو که برای حزب‌الله لبنان ارسال میشد، در مرز عراق توقیف کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134786" target="_blank">📅 20:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134785">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
پرواز بیش از ۱۰ هواپیما سوخت رسان امریکا در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134785" target="_blank">📅 20:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134784">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سفارت آمریکا به شهروندانش در عراق هشدار داد که در پی حملات پهپادی ایران به اربیل، در بالاترین سطح آمادگی باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134784" target="_blank">📅 20:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134783">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی: تفاهم نامه  برای ما تنفس بیشتری داشت؛ میلیاردها دلار نفت فروختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134783" target="_blank">📅 20:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134782">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
تسنیم: دود سیاه اطراف شهر بهبهان خوزستان مربوط به سوزاندن لاستیک است و هیچ مورد نِظامی و امنیتی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134782" target="_blank">📅 20:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134781">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
قطر: ما گزارش‌های رسانه‌ای اسرائیلی را که ادعا می‌کنند ما با مشارکت در یک عملیات نظامی علیه ایران موافقت کرده‌ایم، رد می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134781" target="_blank">📅 20:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134780">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
کرملین: هیچ درخواستی از تهران برای برگزاری مکالمه تلفنی پوتین و پزشکیان دریافت نکرده‌ایم
🔴
به تماس‌های خود با ایران ادامه می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134780" target="_blank">📅 20:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134779">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a807ff4625.mp4?token=FtkZin6DSIun60DgrgxrIayRcR3UQ_LOw74a8GtByirC_GY4XvLMFNMDNAx_IPekzH4Mn2M42hggeQRgqkdz49U6F5I-gRf_u4jelX2OQgrKa8EPtYmBaKCWbr1ExxCgsJuCN5sO0Zf19SRy8pBU_atkxHjn_CI1BblT8qpKyyFZO6gxmWVwL2ChZyJZHdK8JSGPTB3U-JYa7Ym2vmF0983u55PBrrUqateXUdfA7yfTqav8JBn0C8PUxj97ZMCyr3Kx3h7ki6_kUZpMu7af5-SLim0MzmR5Vdpalhm5n28bV2UkWPUlASddRqwbu-bEa083rSE5MqfjtlKAOOz3FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a807ff4625.mp4?token=FtkZin6DSIun60DgrgxrIayRcR3UQ_LOw74a8GtByirC_GY4XvLMFNMDNAx_IPekzH4Mn2M42hggeQRgqkdz49U6F5I-gRf_u4jelX2OQgrKa8EPtYmBaKCWbr1ExxCgsJuCN5sO0Zf19SRy8pBU_atkxHjn_CI1BblT8qpKyyFZO6gxmWVwL2ChZyJZHdK8JSGPTB3U-JYa7Ym2vmF0983u55PBrrUqateXUdfA7yfTqav8JBn0C8PUxj97ZMCyr3Kx3h7ki6_kUZpMu7af5-SLim0MzmR5Vdpalhm5n28bV2UkWPUlASddRqwbu-bEa083rSE5MqfjtlKAOOz3FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت: تصاویر ماهواره‌ای نشان می‌دهد که یک پرتابگر سامانه موشک پاتریوت آمریکایی در حمله پهپاد شاهد-۱۳۶ ایران به فرودگاه اربیل عراق منهدم شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134779" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134778">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3aA9rrFC9CPQJO3Rn1NT2mVLSJbt-_fC-XB54SpuC5CfcKp9yaxzYzFljfxFoMsola2DE8Bp9GZBNdTmRQUcJdqDB4KMS8DQfVAqpUr1ZRqidd2IbRpa9RChApB_58SgkMMA2ato-okxAKlHGV73hTUyGpk-i41vOJkPV14a7BfVWk4r9RtiMapLoNW4vKzdU2JFyR5JIypDD4ayZIG6QvMdgkLtp-hO1hkqdy_BsYivmMuCNQnbyMC6-DLcwgNIFzoya0s0Uyr3hJRpq9Qus-8OicTjrprqzmoyx6jyoH0Xm6jc9ikU1hQHy-2TG4PJXAyZOBEyF5GpCYb1Y8Eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در اقدامی جدید برای شکستن محاصره عربستان، شرکت هواپیمایی ماهان ایران از ۱۸ جولای پروازهای مستقیم بین تهران و صنعا را آغاز می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/134778" target="_blank">📅 20:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134777">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رویترز به نقل از مقامات پاکستانی:  ناامیدی وجود دارد، اما ما میانجیگری بین تهران و واشنگتن را رها نخواهیم کرد.
🔴
تشدید اخیر تنش‌ها، سفر هیئت ایرانی به اسلام‌آباد را به تعویق انداخته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134777" target="_blank">📅 20:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134776">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSOfWpFZnShnQKd5mKAPyivd5rSPM5uOeVfu_sFfsW903OkLVGQUf7lys7rTUfeL4hUs4yle9C_RwIejQ4nLkl4vkBuJ2N7lM7rUOW56YUiWzk-_TQqflrXxswOksVL_34JK8XnM1GyD6bnzZCqVrokH75mURoxfzJoWDu6y_W9c_OfxkAm1U7pNOxlwaQXWrbGPTq2AHfJ02i4RcGYiCFIbuydk1np-2xZ3SRkjR-9NQ5X7Byfdh76k5XqhG5kR3vYhXK902YZyNhusXASFsqCVNwmL0DwjuqHZe4jwCjCHmoDIVPjHYhGxfOSmcKTJ9znycSekMZ0_2-KsiRYVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر  بعد از حمله سپاه به دبی که آسمان‌خراش‌های دبی را شفاف نشان می‌دهند.
🔴
هیچ آسیبی و برخوردی وارد نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134776" target="_blank">📅 20:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134775">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
عضو کابینه اسرائیل الی کوهن: حفظ تفاهم با لبنان به صراحت بیان می‌کند که ما در سال‌های آینده در لبنان باقی خواهیم ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134775" target="_blank">📅 20:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134774">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzXwNSMQf8GC2JsAmaQxVDJQo0mpQb5pKEEIKqctNR8_7Hh3danVXugHc2k48xdEK1jrhTgQ8EvtgHpR7W4iKASrbHahPgm8descdZMEeMUnnlb_sEWdX8IFb5qqHp1PNYCavY619ca_n7P2IbIY_1kLtCUNjfyDlakXcHX32UCJvq_35Hi5ynXzJQxycrivyYSoLU7jB5ia_AFH-dw-wvG4EQJQiQnHKzNlZ0w2EJExsDYxqXcDWKczYryvvmOJqbowBJNU7mpO9B6Ge63bAu0bMYK-IocAPyduMprneeCmDgvgyGZaJ68JS5JevlEG1Dj9MuQUTBJmO5-kMi7GHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام وزارت دفاع امارات به فایتاکس : هیچ انفجاری تو دبی رخُ نداده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134774" target="_blank">📅 20:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134773">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رسانه عراقی نایا (نزدیک به حشدالشعبی): صدای انفجار در منطقه فاو، در نزدیکی مرز عراق و کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134773" target="_blank">📅 20:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134772">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری/رویترز: انفجار هایی در دبی و ابوظبی شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134772" target="_blank">📅 20:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134771">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
روزنامه آمریکایی نیویورک تایمز نوشت: درحالی که ترامپ در تبلیغات انتخاباتی خود متعهد شد به جنگ های ابدی آمریکا پایان می‌دهد، اکنون خود را درگیر جنگ طولانی با ایران می‌بیند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134771" target="_blank">📅 19:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134770">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saZrvoSR532OeiePrwNMMDv4uIi6WvY7KvNAr7s1Q6yYTMBI0hURsI9GzmBvhN3xZx4eSPIx-doNfQX4_WEAnv0d82eH_qAHfz5RRPnImPuQEusQ2X5uplImj2jsyO6uQa5wIiBAJcO2BD5gdbPyLJP1P_O5DWnmAdv3U0LPvTwqFVFUqq-e-lryCwO9Qme4os-WSh-0IN0K5BCUTgioBkVzMOHBwStX6xzwOYFqidLaJN6oUggZH610Upn13MUmAsRW3pYo2uIPIWQH7VUtmOHOS4beWa8YU1MPhb6xe-1k-XAZXe_UiCAg19SEwXSHTwShcMN3nrUh_Kk9K4S_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده در حال آماده‌سازی یک برنامه انتقال برای ونزوئلا است که بازسازی پس از زلزله‌های ۲۴ ژوئن را با آماده‌سازی برای انتخابات دموکراتیک ترکیب می‌کند، گزارش‌های ABC می‌گویند.
🔴
پیشنهاد تایید نشده شامل حدود ۳۰۰۰ پرسنل آمریکایی و تقریباً ۳ میلیارد دلار در تأمین مالی اولیه است.
🔴
این برنامه بر بازسازی زیرساخت‌ها و هماهنگی کمک‌ها به جای اشغال نظامی تمرکز خواهد کرد. مهندسان آمریکایی و متخصصان غیرنظامی به بازسازی جاده‌ها، بنادر، سیستم‌های انرژی، تأمین آب و خدمات عمومی کمک خواهند کرد.
🔴
واشنگتن در حال بررسی یک اداره نظارتی موقت برای مدیریت بازسازی و جلوگیری از کنترل نهادهای چاویستا بر کل انتقال است. این برنامه شامل الحاق ونزوئلا نخواهد بود، اما به ایالات متحده نقش مرکزی در نظارت بر بازیابی کشور می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134770" target="_blank">📅 19:53 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
