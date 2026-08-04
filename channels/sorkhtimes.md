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
<img src="https://cdn4.telesco.pe/file/bEKebfLH_7V01P_vfjHsq8LZ9BJq1x4NSFbg8nZV_PziNV3Q85TRgoOSgK5lixHR3UAjxo2-xN9pAgfda6UYIP2Zg5YXUidGAq73CR06497hMzqu-gzDxDuANHBT9FQP39ZlfB-TY9ZXd6uAWpdG6qZinnYyZUhQYHarg9S59-mVQ2p5vw8mfUzvMtdrFKbTXHOrWKqQJvs91ax6BiHQ7g74P1IQyfEI5e75Slx2lWQWgFSbMKZECzRLr8EnDI52xs47kYnCWXwST9aDL7ub7LL0hsfzeugfviHjAX6R_YZ_zYJCO5nD6L_HCMMh1-Dk5p7S-4mMxqTomzxOpU78SA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 15:06:30</div>
<hr>

<div class="tg-post" id="msg-137318">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
❌
طبق شنیده‌ها: سید مهدی رحمتی سرمربی گل گهر سیرجان موافقت خود را با فروش امیر جعفری مدافع چپ 24 ساله این باشگاه به‌پرسپولیس اعلام‌کرده‌است. رحمتی در این پست قنبری شاگرد سابق خود در خیبر رو میخواهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/137318" target="_blank">📅 14:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137317">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
❌
ترامپ: در حال حاضر درباره بازگشایی کامل تنگه هرمز تا فردا با ایران صحبت می‌کنیم. این آخرین فرصت ایران برای دستیابی به توافقی خوب است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/137317" target="_blank">📅 14:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137316">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_E7scgOt6DknGfyBtoh_-5DbGGzbHpMBd-0LJZRcMPxDOrfyAuIMkj8BAk8SpbQkMp_o3iK823z1tFwg3TCybAoUhKKLzsNEIsC_BSOiTZqOzK0y59xm4BNMAWOfLhH42HJnI1EVDvVQ595jcy_CwWaKuZnRvkFWKoruG__eXy3GvRzWMWXh0OaTMfMCtX6zkUytAJ3s2LISEqPcG_2peD-MHC1xhO-1YrAYruZ4pvsoRa4cIfKqodXZHsPH8tzkg3TF0JQxsnn79TM-Rj1Eb4-63KnOzeAKYg8KkP5Z8KpCdv9aiQVPHhMYEC8uwST1H2rdg7zV7TkLs64qYGZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد برای صعود؛ شبی سرنوشت‌ساز در لیگ قهرمانان اروپا
⚽️
دیدارهای امشب مرحله مقدماتی لیگ قهرمانان اروپا با رقابت نزدیک مدعیان برای رسیدن به پلی‌آف دنبال می‌شود. تیم‌ها در تلاش‌اند با کسب نتیجه‌ای مطلوب، شانس خود را برای حضور در مرحله اصلی افزایش دهند و همین موضوع می‌تواند بازی‌هایی تاکتیکی و پرتنش را رقم بزند. انتظار می‌رود جزئیات کوچک و عملکرد ستاره‌ها، نقش تعیین‌کننده‌ای در سرنوشت این مسابقات داشته باشد.
⚽️
بازی‌های امشب رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/SorkhTimes/137316" target="_blank">📅 14:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137315">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
10 باشگاه لیگ برتری صبح امروز با ارسال نامه ای به سازمان لیگ خواهان تعویق 10 روزه لیگ شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SorkhTimes/137315" target="_blank">📅 14:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137314">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
🔴
🔴
ایمن حسین مهاجم ۳۰ ساله تیم ملی عراق، در انتقالی آزاد با قراردادی یکساله به پاختاکور ازبکستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/137314" target="_blank">📅 12:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137313">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
آخرین وضعیت ایمن حسین ستاره تیم ملی عراق در ترانسفر مارکت که درحال‌حاضر بازیکن آزاد است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/137313" target="_blank">📅 12:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137312">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
تندیسی زیبا که باشگاه پرسپولیس برای امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک ساخته بود و‌ این بازیکنان برای دریافت این تندیس حضور پیدا نکردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/137312" target="_blank">📅 12:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137311">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
❌
علیرضا بیرانوند این فصل سرباز هست./ ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/137311" target="_blank">📅 12:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137310">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7jvDHPxxVsbDhkvGcSE-HP8J7-nksSVOIjPgMMXdJ5lDNunacIFVugTv-biAppN6x-yvps3n94rJItdgf5lEt82ICXM9N9raFWhoty4LyDcKvn6w0351uoR04IIZbl5oEePxLBEIMzzqwZPdltD_8U0HFb05kioIG7thpxyB-vdw_Qh6KL3f_iYVLsp5R-wy7K6y9PF_4JECM3Y1NLzVmdX9xPX0V2CJEbHkoF0EeQqGJJUUyegOqUv2CQedITLRoOic38uTepB-JD1abSAdHFmZEPmUz-AjwUA37iM54ZH-iuXaU7v6AiedwIBBl3V4VtCFdI-aJTW044XwXFz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تندیسی زیبا که باشگاه پرسپولیس برای امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک ساخته بود و‌ این بازیکنان برای دریافت این تندیس حضور پیدا نکردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/137310" target="_blank">📅 11:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137309">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⚠️
⚠️
⚠️
مدیرعامل باشگاه گل گهر سیرجان :
⚠️
⚠️
امیر جعفری مدافع چپ مدنظر باشگاه پرسپولیس قرار دارد اما تا این ثانیه به صورت رسمی با ما مکاتبات نشده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/137309" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137308">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
✔️
گفته میشه که تارتار بعد چند سال بالاخره جاسوس تمرینات پرسپولیس و پیدا کرده و بدون رودروایسی کنارش گذاشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/137308" target="_blank">📅 11:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137307">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووری
📊
📊
خبرگزاری RB اسپورت روسیه : مذاکرات پرسپولیس و دیناموماخاچ قلعه برای حسین نژاد جدی شده است و امکان توافق طرفین بالاست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/137307" target="_blank">📅 10:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137306">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❤️
📸
تصاویری از شادی بعد از گل علیرضا همائیفرد پس از باز کردن دروازه حریف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/137306" target="_blank">📅 08:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137305">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔻
🔻
🔻
ترکیب پرسپولیس دوباره لو رفت؛ تارتار هم دنبال جاسوس می‌گردد
➡️
➡️
➡️
فرهیختگان: سرخپوشان روز گذشته به مصاف تیم پیرامیدز مصر رفتند. اما جدا از مسائل فنی، موردی که ذهن مهدی تارتار و دستیارانش را به خود مشغول کرده است، بحث لو رفتن ترکیب تیمش یک روز قبل از مسابقه…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/137305" target="_blank">📅 08:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137304">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74903f0977.mp4?token=Okrtea-ilYGrWBUuowoD2hu6HC4Ks_gdcgQWAFdfofUDAqwDkXAlQt94fAJ5c6HKi_mo8fWtyDJFE32L-XNFlI7tkVjGs6GW8VCOADQKzou5YMFnDtSB29Iy7nwXmBPWoems25Hy9puM5itUHJbHIIB3dc8QkDYn6yhqx0eLOUregxoPXQ210hydCXiEhlZwcd5AOAdtuNENvBCawHkOg3Pz-3Yee0eLNUdHk33Ac866TpwAotYOo7fvggw5Fg1l7sOGt8G5zRgcqDfkhto8awDY4WpADOvHD-zAGxsmLXBuCXjKbVKRY6AmqKj6Ck4_RtER_09PoGqMm5gBamFimQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74903f0977.mp4?token=Okrtea-ilYGrWBUuowoD2hu6HC4Ks_gdcgQWAFdfofUDAqwDkXAlQt94fAJ5c6HKi_mo8fWtyDJFE32L-XNFlI7tkVjGs6GW8VCOADQKzou5YMFnDtSB29Iy7nwXmBPWoems25Hy9puM5itUHJbHIIB3dc8QkDYn6yhqx0eLOUregxoPXQ210hydCXiEhlZwcd5AOAdtuNENvBCawHkOg3Pz-3Yee0eLNUdHk33Ac866TpwAotYOo7fvggw5Fg1l7sOGt8G5zRgcqDfkhto8awDY4WpADOvHD-zAGxsmLXBuCXjKbVKRY6AmqKj6Ck4_RtER_09PoGqMm5gBamFimQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
فرا رسیدن اربعین حسینی بر شما عزیزان تسلیت باد
🏴
⚡️
الهی به حرمت این روز همگی حاجت روا  و عاقبت بخیر باشید
🙏
الهی آمین
🙏
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/137304" target="_blank">📅 08:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137303">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3J67Qh4ZarltHTQCBENHTjSgHcKRghI2CjMG8sbrBnG5RHiO1dDACNNDGcIv0sygZGjVPLDYGCJFUQyJb73QPEP_MqdjX4Kx62eLESDXZbuSWWQPqpSroPgChokGdgrWhIffY63cOp7MIe4DeJOn66SQr8_NhoP8QgE46DAJvqR2t7MgcQD_fGgLW7VUwPW39_hTSAwzwh8D1AGrkRs4a7H7qdry7YMQhGthhRIR4e1DSuUTXm9bxTFn4DWhD84GuL2z4DxeLDP9b1U4Opqbkchk0gsZ8zc0B1Q5UvSocF7_vdLRd85b1mId2VLjfyW5x_EwNmUWvt2SGcUxf0MZG8Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3J67Qh4ZarltHTQCBENHTjSgHcKRghI2CjMG8sbrBnG5RHiO1dDACNNDGcIv0sygZGjVPLDYGCJFUQyJb73QPEP_MqdjX4Kx62eLESDXZbuSWWQPqpSroPgChokGdgrWhIffY63cOp7MIe4DeJOn66SQr8_NhoP8QgE46DAJvqR2t7MgcQD_fGgLW7VUwPW39_hTSAwzwh8D1AGrkRs4a7H7qdry7YMQhGthhRIR4e1DSuUTXm9bxTFn4DWhD84GuL2z4DxeLDP9b1U4Opqbkchk0gsZ8zc0B1Q5UvSocF7_vdLRd85b1mId2VLjfyW5x_EwNmUWvt2SGcUxf0MZG8Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
تجربه‌ای متفاوت از هنر روپایی و تصمیم‌گیری با Crash Kick؛ جاییکه مهارت با هیجان گره می‌خورد!
⚽️
در کراش کیک، هر روپایی موفق ضریب برد را افزایش می‌دهد و هر لحظه وسوسه ادامه دادن بیشتر می‌شود. هنر اصلی بازی، انتخاب بهترین زمان برای برداشت جایزه قبل از پایان روند صعودی است. این بازی با ترکیب هیجان، تصمیم‌گیری لحظه‌ای و مدیریت ریسک، تجربه‌ای متفاوت و نفس‌گیر را برای علاقه‌مندان به بازی‌های سریع و پرهیجان رقم می‌زند.
✅
جسارت ادامه دادن یا هوشمندی در برداشت؟ تصمیم تو، سرنوشت جایزه را مشخص می‌کند.
📌
همین حالا وارد ربات وینکوبت شو و هیجان واقعی رو لمس کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/137303" target="_blank">📅 01:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137302">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
باشگاه پرسپولیس با وجود باکیچ ، خدابنده لو و پویا پورعلی گفته نیازی به جذب هافبک شماره 10 یا شماره 8 نداره و بدین ترتیب حضور محمد جواد حسین نژاد در پرسپولیس منتفی شد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137302" target="_blank">📅 00:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137301">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
گزارش تصویری / پایان اردوی سرخ‌پوشان در ترکیه!
❤️
تصاویر منتخب از آخرین جلسه تمرینی  ارتش سرخ در اردوی آماده‌سازی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137301" target="_blank">📅 00:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137300">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eI7PFh0ZOpBAiiGc08lKELe3sS1NBXWYXH69i08n2MLkOqNJoUXVRJEh0Ib8Pa51SEAW4kK4Km2kkF7HHxcVHhmlrbcE6leoc74DxjVdxSjMRtbMi8loHztif0ZVqy5Yv5KhryA-X8sRGxhNZ_mKP2TWeAAVhjVC0bCnm5lIOstoyUcMlSknOdRX_3S5R3J4GczA6KCz-AItiDWHwPejPMK9NuOhKh-gktaJHiiuL2UTpwLKv0Bu-S7EJrLhyqGxiPnRJ9dOt5A3w_FXIBobEuq0AMy6XxNTkZQSjEL4DcGUz54I2x92foX5vXzl82gW89sP4dcFpG3jujVWFHabhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
با تصمیم مدیریت باشگاه پرسپولیس زمین شماره ۲ مجموعه ورزشی درفشی‌فر به نام شهید ماکان نصیری نامگذاری شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/137300" target="_blank">📅 00:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137299">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giFB-8jFMLhi4X7fGeeWjDeD0QfZsV0ye9G6VyIjtGG_Uv65xP-uip0MUt7Gecn5hx5ItYWp7vPKQjJnFhkjzGeYFrP39QVprjt3HiQPdKs2Es83kcnsptsU6jxA9CNgdbKoS8o8-xVCqE8fqNtzqxa6E0mryQwsXGfmIwQHwGiBFmKKixbVjqTTp7Kqj5rHJqUZTvUezxVAK9M-T2gHop-jEojYdfuV-xMn-NP2Zy0GiYhtFsGLYqgPq6l-CK1B85XeNUhnc5q94BCbwgbFGyAE5qIlKVGyNhYgtRAzscwGvQ2JXirbbXnHaAAUUfRG_Q1udTGcX5WzeM_30uxqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
با اعلام ایجنت رامین رضاییان، این بازیکن از استقلال جدا شد
🚬
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/137299" target="_blank">📅 23:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137298">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
احتمال تعویق یک هفته‌ای لیگ برتر به دلیل درخواست برخی باشگاه‌ها افزایش یافته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137298" target="_blank">📅 23:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137297">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
❌
خب ظاهرا پیشنهاد استقلال بهتر شد و پستای استقلال برگشت
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/137297" target="_blank">📅 23:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137296">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⚠️
⚠️
امید عالیشاه به ذوب‌آهن پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137296" target="_blank">📅 23:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137295">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e24FcE0KkK_Pwvjo_MwzJ54ZpVop8XMIqazPH4L5U0uYN_LVNxSiSYxjTwUp4VXMDySBEvf_rK7b7JBIw8yggeBQnxNH29HaBi6SE6ktFskjTURfDhxJZSogjdQOWneDfsSwvACTNMsz7WWUTrVVVa6IX031IUsu4iwittIPrKK_c5_YxnoT-OuXj8x4OKvkkQxnM-1e-JK6WTwAkAK8dDd5kFiY25KruBA7sp34407TbZTTBQYndxfwOuKxkaYmnYEu4nrklssns6uDppMwV0q1xXUljigFRlC3qLu0_aQG3hUG0CpisVi1UURHUQUuo6Ui65SJvlxMhV82OaGQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
احتمال تعویق یک هفته‌ای لیگ برتر به دلیل درخواست برخی باشگاه‌ها افزایش یافته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137295" target="_blank">📅 23:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137294">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🚨
📊
فووووووووووووری
🗣
باشگاه عصر دیروز به جمع بندی رسید که باید برای جذب قربانی اقدام کنه
👀
مذاکره با قربانی و ایجنتش که رابطه خوبی با مدیران الوحده دارد شروع شده و امروز با جدیت بیشتر پیگیری شده است.
🎤
حسین قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137294" target="_blank">📅 23:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137293">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
✔️
شرایط ایری از نظر حقوقی متفاوت با کسری طاهری است.
✔️
اینکه پرسپولیس همچنان دنبال کسری هم هست یا خیر و اینکه نساجی حاضر به انتقال فقط ایری می شود یا خیر نمی دانیم
✔️
تارتار بشدت دنبال جذب مدافع میانی و چپ است و ظاهرا گزینه ای جز ایری و رزاق پور ندارد.…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137293" target="_blank">📅 23:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137291">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
فوری/ ترامپ: به درخواست ایران و کشورهای منطقه، حمله رو برای فراهم شدن زمینه توافق، متوقف کردم. ما کاملا آماده حمله بودیم اما حالا مذاکره می‌کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137291" target="_blank">📅 21:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137290">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
قرمزآنلاین: دانیال ایری، رزاق‌پور و محمد قربانی سه خرید پایانی پرسپولیس
🚨
🚨
باشگاه همچنان برای جذب ایری و رزاق‌پور تلاش می‌کند، هرچند فولاد فعلاً با جدایی رزاق‌پور مخالفت کرده است. همچنین با درخواست دوباره تارتار، مذاکرات برای جذب محمد قربانی پس از کاهش…</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137290" target="_blank">📅 21:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137289">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a103c22f7.mp4?token=vVTOJXXgvBWEQNm7lURUXzDA2aoo9N6Pvr5qt-J8jE0dBT-2eg3mZxYb8A_urAMA9ofpxxPXJsfhzPfPe6mRIN64tFPb76jV8nKxSsdfV1KDfu6wuFPgu3jzxPd0awfX9hBOeHU25PlyJpXnQJfl1-sdM8YAf-nwqGBUA9eBZr58zvgz9zfsESyUVskAj9MltBRquyE2w8YOCaigyE8EGjlohRQQLUH3uHDpZf5FRchWiu3MBIUIgAlzM38nwiR_6UkpUhbeKeO_VsT_k1MM7OEytVgwRjDi9IOJD7CHEHFVIe9CJJFJnMnNhKtk8bpoHspnwptApWwUs2jGChbP5XSIG1R3l_HF16RyxMJkyNTDIVpgOEF-8uZu_7SpjPO48zdBGQ6U75tNvob26RGPt7F5DwDjOU0qEwMiLFkxyUmaJL5Y3ZgHfUvt-93xbRg6xGA65bsTRAm3iWCOaZNtX0Lroj5LrK_EzoMkYFX5ggdqcIo-1DB2rUQPHmJ5X2HN7Tz9B8nre4AnrinaL5lCbVs0YnpgJ8EmUqRXD-WqrWbE8BFI3HXHoWD7DJpAbYYZHb1w4v-RWunuT345Bqfq-rKHc7kp8ilDxggB4FUyHOP86omRdyEjqTjc8FycgQ4c2YU_lGP7rG-YAS9pRaarVPOmu6sFmS2euIombPgU2As" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a103c22f7.mp4?token=vVTOJXXgvBWEQNm7lURUXzDA2aoo9N6Pvr5qt-J8jE0dBT-2eg3mZxYb8A_urAMA9ofpxxPXJsfhzPfPe6mRIN64tFPb76jV8nKxSsdfV1KDfu6wuFPgu3jzxPd0awfX9hBOeHU25PlyJpXnQJfl1-sdM8YAf-nwqGBUA9eBZr58zvgz9zfsESyUVskAj9MltBRquyE2w8YOCaigyE8EGjlohRQQLUH3uHDpZf5FRchWiu3MBIUIgAlzM38nwiR_6UkpUhbeKeO_VsT_k1MM7OEytVgwRjDi9IOJD7CHEHFVIe9CJJFJnMnNhKtk8bpoHspnwptApWwUs2jGChbP5XSIG1R3l_HF16RyxMJkyNTDIVpgOEF-8uZu_7SpjPO48zdBGQ6U75tNvob26RGPt7F5DwDjOU0qEwMiLFkxyUmaJL5Y3ZgHfUvt-93xbRg6xGA65bsTRAm3iWCOaZNtX0Lroj5LrK_EzoMkYFX5ggdqcIo-1DB2rUQPHmJ5X2HN7Tz9B8nre4AnrinaL5lCbVs0YnpgJ8EmUqRXD-WqrWbE8BFI3HXHoWD7DJpAbYYZHb1w4v-RWunuT345Bqfq-rKHc7kp8ilDxggB4FUyHOP86omRdyEjqTjc8FycgQ4c2YU_lGP7rG-YAS9pRaarVPOmu6sFmS2euIombPgU2As" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حمایت تمام قد حسین خبیری از حدادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137289" target="_blank">📅 21:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137288">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3VYJupt-WKmQNrvTqGVIybLt9oPHSTSYv0JqAGI6TKFRlogZ0X7y1kRW97GIAC3WfG-hENf43PW7lahJcLZSgeLqf4vO6W7Y8bgsrSnsSMWT7lPAUPnLkYLDAz-_hfnr0s36QAnAeLJSX3oBdgKLTL3-w1cyMj-EQLef1UfDoUE0EMafacKSgvra-KMfDA_rdi7szhUyjt1jC7K_Yj-QM-yc_TfROHRajTHYyTiuISjYerR1dtDyUHnAXcwWLwT1YVgmcCyMdRp4ijymjgx79BWrpMFJgUwCcPZ8IFu6v8s1Y_rTYV-JJzefhZd3vY0snx_UiyyNeawcc7CPsfJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
فریتز در مسیر قهرمانی؛ جودار به دنبال شگفتی در فینال!
🎾
Rafael Jodar -
🎾
Taylor Fritz
🎾
تیلور فریتز با اتکا به سرویس‌های قدرتمند، ضربات فورهند سنگین و تجربه بیشتر در دیدارهای بزرگ، شانس اصلی کسب عنوان قهرمانی محسوب می‌شود. در مقابل، رافائل جودار با نمایش‌های کم‌اشتباه و روحیه جنگندگی خود نشان داده که توانایی به چالش کشیدن هر حریفی را دارد. اگر جودار بتواند ریتم بازی را برهم بزند و رالی‌ها را طولانی کند، این فینال می‌تواند بسیار نزدیک‌تر از حد انتظار دنبال شود.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137288" target="_blank">📅 20:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137287">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKcLHkFaEw0d4jqbBlKU9urYItrGpi8NqwARKQilIl-7O_9LQtbsdguD6qNX6jBq91I3GID6mLlLvDY5h8aEX5tLDIU1AtC8tiOc2Pr0AkZbDSfoR_a-96mWOphZIBT8NVk2lRnzUGD7kSiMLfWT2ZHhWn9gKhW7bk64OUDrkSyvuDEjDy_WdHwykADiV08sLkgMDXEiAjrtyDVk_tfdUmH0k1C3vEQ5lXY05ukrbI8OTaKeKepzsPrNpL9rKapk9r-2Tse2E1Feqvu7vTxia5361GdjkqiSb0QNH_vJ1a8H159BS1n4de8Y-_91bP5SOpDS1mB5Qxz5b5uNLg30ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش تصویری / پایان اردوی سرخ‌پوشان در ترکیه!
❤️
تصاویر منتخب از آخرین جلسه تمرینی  ارتش سرخ در اردوی آماده‌سازی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/137287" target="_blank">📅 20:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137286">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔽
🔽
ویدیو 6 تایی شدن ارزروم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137286" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137285">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
❌
دو باشگاه تراکتور و پرسپولیس به دنبال جذب محمد قربانی هستند، باشگاه می‌تواند این بازیکن را جذب کند که با الوحده امارات به توافق برسد.
✍️
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/137285" target="_blank">📅 20:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137284">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔄
🔄
گوهری گزینه ی گلری پرسپولیس نیست/قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137284" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137283">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3zBVLJYbdOhtoAR1sFDLD1xqHN6cLgurqHgVbWqHdIRmWCw5pc8AYSlVmGve1jg7eljfVCvKn-GIg6txv8sO7WLwdBAKkR5X8US2VsDvLjKSeTsx5wsSH-K28x81OSiDpoDeqTyLgvUYvTKCdNwLsmYKMv6gSusJZWLHvm2b7o-opJCVggKMrye_REkZtXh4j8iA3BAJCMEsFS5wB7FmH951U_AbRh8sA_4563kKBUwCSUyFqcvmDnl_mXbpNeCTHid05JVF7CPoE7oayD18j2wcxsKLMywACHFPEKlQTzzXzkAxpI_inciDf4xwguvS31eMsT1HivAVIvyk8c4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کاروان تیم  درحال آماده شدن برای بازگشت به ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137283" target="_blank">📅 18:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137282">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
مجتبی حسینی: پرسپولیس هیچ مذاکره‌ای با من نداشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137282" target="_blank">📅 18:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137281">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
❌
حسین خبیری بزودی بعنوان معاون باشگاه پرسپولیس انتخاب خواهد شد
🔄
ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137281" target="_blank">📅 16:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137280">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
باشگاه پرسپولیس امروز بار دیگر در نامه ای به ملوان خواهد جذب فرهان جعفری شده است
🔴
🔴
در تماسی که خلیلی با مازیار زارع و ایجنت این بازیکن داشته تعلل در بستن قرارداد و فروش این بازیکن رو مشکلات مدیریتی ملوان و مشخص نبودن وضعیت مدیریتی برای مذاکره اعلام کردند…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137280" target="_blank">📅 16:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137279">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
❌
حسین خبیری بزودی بعنوان معاون باشگاه پرسپولیس انتخاب خواهد شد
🔄
ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137279" target="_blank">📅 16:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137278">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🤩
🥇
تسنیم: صنعت نفت مشتری جدید امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137278" target="_blank">📅 16:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137277">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🌹
گودرزی بعد از پیوستن به گل گهر: پنجره استقلال بسته بود؛ شرایط پرسپولیس مهیا نبود.
⏺
از استقلال و پرسپولیس پیشنهاد داشتم اما استقلال پنجره نقل‌وانتقالاتی‌اش بسته بود و پرسپولیس هم شرایطی که مدنظر بود را نداشت. در نهایت گل‌گهر را انتخاب کردم چرا که هم با مهدی رحمتی کار کرده‌ام و هم گل‌گهر تیمی بسیار خوب، ریشه‌دار و آسیایی است.
⏺
یکی از دلایلی که واقعاً گل‌گهر را انتخاب کردم، حضور مهدی رحمتی بود. خیلی دوست داشتم دوباره با او کار کنم و او هم شناخت خیلی خوبی از من دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137277" target="_blank">📅 16:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137276">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔹
🔹
🔹
نتایج پرسپولیس زیرنظر تارتار
👀
13 گل زده و 0 گل خورده
🔥
🔴
پرسپولیس 3-0 شهدای رزکان
🔴
پرسپولیس 2-0 خیبر خرم‌آباد
🔴
پرسپولیس 1-0 آلانیا اسپور
🔴
پرسپولیس 1-0 پیرامیدز مصر
🔴
پرسپولیس 6-0 ارزروم اسپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137276" target="_blank">📅 15:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137275">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
❌
دو باشگاه تراکتور و پرسپولیس به دنبال جذب محمد قربانی هستند، باشگاه می‌تواند این بازیکن را جذب کند که با الوحده امارات به توافق برسد.
✍️
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137275" target="_blank">📅 15:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137274">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
🔴
شنبه بازی دوستانه داریم،پرسپولیس و آلومینیوم
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137274" target="_blank">📅 15:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137273">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
فوری؛ رامین رضاییان چند پست خود با پیراهن پرسپولیس را از آرشیو پیچ اینستاگرامش خارج کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137273" target="_blank">📅 15:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137272">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmhu5dQdgRyJSByau0c9XVMwYPgunfBu31NKCTmDVgtmto_7GrClXTUwZsTYaqzADDydj1-urdHcs4e1uiLbC260FX-zSVQk_Zl25mAXRcwd8yNAwp7PH3WN0dYssLxPeNTLJXNLeT_sBU6RSDLROqSto7BKvWkm_H2omOLfhaFPo-xJ-lcEG4GxCokLHXODMw8EgbEOp5X13zgf_tjdNnOjE8wu3CnNgPV9ONELd1JlftUfuhHt6zG5J3Fa7JhR-i4ebEocpdZ2y2anqk30sxchmG_MsaQabv3CREK9kukPzS1Lt5fQz0_KU0b-8f74wnaEj9ZdLimvA5LqPJ852Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
👀
بازگشا سخنگوی باشگاه پرسپولیس: در حال حاضر باشگاه پرسپولیس برنامه ای برای تغییرات احتمالی در کادر مدیریتی خود ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137272" target="_blank">📅 15:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137271">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
❌
محسن خلیلی از سمت خودش در معاونت ورزشی باشگاه کنار گذاشته شد و به زودی جانشین او مشخص خواهد شد //فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/137271" target="_blank">📅 15:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137269">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
فوری؛ رامین رضاییان چند پست خود با پیراهن پرسپولیس را از آرشیو پیچ اینستاگرامش خارج کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137269" target="_blank">📅 15:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137268">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137268" target="_blank">📅 15:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137267">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
باشگاه پرسپولیس با وجود باکیچ ، خدابنده لو و پویا پورعلی گفته نیازی به جذب هافبک شماره 10 یا شماره 8 نداره و بدین ترتیب حضور محمد جواد حسین نژاد در پرسپولیس منتفی شد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/137267" target="_blank">📅 15:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137266">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
فووووری 360: رضاییان از کیسه جدا شد
🚨
🚨
با توجه به حضور صالح حردانی و سامان تورانیان، سهراب بختیاری زاده با برگشت رضاییان مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/137266" target="_blank">📅 13:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137264">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
قربانی چند تا استوری بچهای پرسپولیسی که تگش کرده بودن و درخواست کرده بودن بیاد پرسپولیس رو لایک کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137264" target="_blank">📅 13:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137262">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InjTXt0_-93hrpUuBviXuIkpI4OPAvU8VEss682N_zVJgAgBpmZB30ELrFBjjrLsWIzBQJU_DOFeZ6TCzAZKJ3Ai3eRccZYanbHrTX8lU1B_VXOyX4q2V3c2NnDmRLqoKkR1MM75PkyJOqDevWhh61ulQrod43Q4wZ1T5ltgXCLu4vHZ9Mgeq4UwR1roFCKlvu0VVDHvvvWW4gO5HUrjEXvUh1-Kno4p_uN8A0W2G6hTmP9J94w0rAFhy_1jCF30zAuky3hL_gO-MSOVvBQz384Jimb8LXDTooBqKX51cB7TLVXpLhEapyoAORFbHePNHAoQeHvQXKIzpukKMqMG-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➕
دسترسی سریع و مستقیم به اسپورت‌نود
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
🔗
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
-
مزیت روش ورود از طریق ربات:
👇
• ورود مستقیم به سایت
• جلوگیری از ورود به لینک‌های اشتباه
• کاهش زمان دسترسی
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/137262" target="_blank">📅 13:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137261">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚡️
⚡️
⚡️
مهدی گودرزی، هافبک ۲۲ ساله خیبر، با گل‌گهر به توافق نهایی رسیده. این در حالی است که چند روزی شایعه حضورش در پرسپولیس مطرح شده بود.
🔻
🔻
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137261" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137260">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
✅
✅
پرسپولیس برای پرس و جو از مبلغ رضایت نامه محمد قربانی از باشگاه اماراتی داشته اما مشخص نیست جذب میشه یا ن/ قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/137260" target="_blank">📅 10:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137259">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
🔴
کادرفنی خواهان جذب یه هافبک بازیسازه درحالی که هوادارا برای جذب محمد قربانی فشار میارن
🗣
🗣
باشگاه هنوز روی جذبش به نتیجه گیری نرسیده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137259" target="_blank">📅 10:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137258">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
پوریا لطیفی فر با بیش از ده درگیری موفق در وسط زمین و هیچ پاس اشتباهی حضور مثبت و قانع کننده ای از خودش نشون داد همینجور ادامه بده پسر
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/137258" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137257">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
🔴
🔴
🔴
پلن های پرسپولیس برای گلر دوم:
🔴
موندن امیررضا رفیعی
🔴
جذب احمد گوهری(سهمیه لیگ برتری )
🔴
جذب امیر عابدزاده
🔴
گندمی گلر دوم فصل بعد باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137257" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137256">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
فوری
✔️
فرهان جعفری نتونست کسری خدمت بگیره و تا بهمن ماه یعنی پایان نیم فصل در ملوان موندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137256" target="_blank">📅 09:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137255">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
به‌به بازوبند‌ کاپیتانی‌ رو ببین چه بهش میاد
©
🕶
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137255" target="_blank">📅 08:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137254">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5n3DeEk7vJBaEKIHg0Kkq_BKu7F30UjOQgSkuhumbuBW_kx4PLPNwhPFaYAGSFvgrdymzi5aqFSUZc2J7iy9hWcsJMUrnHXuuu4SCY6K5N63RMAwVySBTyJp6kMcDJXacbR67AOXYnsHAHVqxplU56I6wOviFvpFWloX803kAyfqD3P2FkTDpL9lbE-G-Av83etcZdIV05zGmE9fa0K5ZzssEgtcUFOOJWvN2hOGI92pRf-webPt7CGfOVZOl_FWkX64rElZ5ofEXzdnmlav-LdBl8Y-dBTkuUv7ThbQwgTEfilQ-DD4Zz1rok2Fja9y41HuuXgx-2solq9sx6MzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137254" target="_blank">📅 08:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137253">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAlP15b0isCbleuEDvIA19lg-AHwDu6N2bhgfPD1Bw4JvYPqik6DOleiBIc5CKhFZOcfCYzS1-seJVTJYR8QYMdN1BXVJy8jKlT8gzOUhZTwH31j2BXnNRiPC0AETbpiiIaKC0ejxoyLm1C9FrlKsfR3hF_Mhs4ZXDAfKWcStKYdvo9rZ59Ul5ycWIYkVrfJQPXNeqUEc--S-pASzQJjZUtAfIArfjFFzxqtvSBxA7Y0rTvEZ_mBaLkKGTeuzo_qLCTC3pSOwLnUI6RrkOte3Nn4H-ZyHbIxD0Rupd9WXAIEa_OLySkejr0K7i_19mZiUail2o20XoK-fu7Z1Xx88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
👋
گل رو پیدا کن و جایزه ببر!
🧐
وقتش رسیده تا دقت و شانس خودت رو به چالش بکشی!
⚡️
همین حالا وارد سایت شو و حدس بزن گل زیر کدام لیوان هست و شانس خودت را امتحان کن!
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/137253" target="_blank">📅 01:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137252">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
🚨
طبق گزارشات اکثر سرورا و vpn های رایگان از کار افتادن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137252" target="_blank">📅 01:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137251">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
تکمیلی :قدوسی : تارتار گفته بیفوما و گرا برن و سرگیف بمونه اما خلیلی میخواد سرگیف ملی پوش رو رد کنه تا گرا و بیفوما بمونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/137251" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137250">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
طبق گزارشات، اینترنت ایران امشب خیلی ضعیف بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/137250" target="_blank">📅 00:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137249">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
فوری به نقل از منابع داخلی ؛  اینترنت بین الملل به شدت ضعیف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/137249" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137248">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
پرسپولیس دو دیدار دوستانه دیگر را تا 24 مرداد خواهد داشت. در اردوی ترکیه برابر ارزروم اسپور و در ایران مقابل فجرسپاسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/137248" target="_blank">📅 00:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137247">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔽
🔽
🔽
ایری یک قدم دیگر به پرسپولیس نزدیک شد/مذاکره نساجی با جرجانی
🔽
🔽
نساجی با درخواست مجتبی حسینی مذاکراتش را با یاسین جرجانی آغاز کرده
🔽
🔽
بنظر میرسه کار انتقال ایری به پرسپولیس در آستانه نهایی شدن چون نساجی علاوه بر جذب جرجانی چهار دفاع وسط دیگر هم داره
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/137247" target="_blank">📅 00:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137246">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚪️
⚪️
⚪️
⚪️
شنیده ها: استعلام اولیه باشگاه پرسپولیس از فیفا درباره جذب دانیال ایری مثبت بوده و مانعی برای انتقال نیست اما پرسپولیس برای اطمینان بیشتر، یک استعلام دیگر هم گرفته تا تکلیف نهایی مشخص شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/137246" target="_blank">📅 23:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
ورزش سه: دانیال ایری درخواست جدایی از نساجی رو داده و باشگاه نساجی هم قصد فروش این بازیکن رو داره و اگه اتفاق خاصی رخ نده ایری پس از کش و قوس های فراوان پرسپولیسی میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137245" target="_blank">📅 23:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
🔴
کادرفنی خواهان جذب یه هافبک بازیسازه درحالی که هوادارا برای جذب محمد قربانی فشار میارن
🗣
🗣
باشگاه هنوز روی جذبش به نتیجه گیری نرسیده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137244" target="_blank">📅 23:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
✅
✅
فوووووووووری
🚨
انتقال ابوالفضل رزاق پور به پرسپولیس به طور کامل کنسل شد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/137243" target="_blank">📅 23:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137242">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
‼️
نمودار ترسناک و فوق العاده غم انگیز... کمترین میزان ازدواج در ۳۰سال اخیر  و کمترین میزان زاد و ولد در ۷۰سال اخیر! سلامی تلخ به پیری جمعیت باید کرد... از هرایرانی بپرسید علت این فاجعه را چشم بسته عاملش را "اقتصاد فاجعه بار" خواهند نامید.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137242" target="_blank">📅 23:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137241">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
❌
رزاق‌پور رسماً و شرعاً منتفی شد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137241" target="_blank">📅 23:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137240">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
🔹
🔹
نتایج پرسپولیس زیرنظر تارتار
👀
13 گل زده و 0 گل خورده
🔥
🔴
پرسپولیس 3-0 شهدای رزکان
🔴
پرسپولیس 2-0 خیبر خرم‌آباد
🔴
پرسپولیس 1-0 آلانیا اسپور
🔴
پرسپولیس 1-0 پیرامیدز مصر
🔴
پرسپولیس 6-0 ارزروم اسپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137240" target="_blank">📅 23:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137239">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyTL8i4fkudgC9o-D32YdN_fX8Wb4QhErg7u7iTmtqSA6g0AZlXMt-7zAieqMwz-hdr30oPqsrUrhLDGjoU2hHZqtr8fSy4gn97l3V4z2gW3mk9ObmZtIEh90mfSeRWZzGlHDXzaBY0TRciyKfeG9J3X6SRaYPSRg_n8UG33yfwZqYxYTZFCEcCWcf7A1YHxQDkwjscLEcm1OEY0pZlLJBya_JQIyeOsnLfXvFi_HZ4HEMVpdNIii6q1xjXxvttRbowz9cJ1maWvTP7aIdhbDsZ3boIZs3KyQ61BMuSQTkde2P777BXWMaJjmJELP2WR27f3EpM488UFK7CzxmvlQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
منهای ورزش
❌
بعد از هشت ماه نرفتن بچه ها به مدرسه
❌
فوری : مدارس امسال از مهر باز نمیشن!
❌
+ عمران عباسی، عضو کمیسیون آموزش مجلس:
❌
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
❌
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز…</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/137239" target="_blank">📅 23:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137238">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbj1R3_Vf84Ih_sY44Fe_KBnIXnT9qjIJXbK3mVYgv5E2ZnVu6jgpyyteQ0LG_kbYc3XUz9xcHgik1tOIJZ6TnUeYIYH6uNrNXYs2zTLw_zsvXXo8rpZB1HcrwzDAYWEMaQAD6Z4FcdLPr-TFOYygMkCDIF3LRaw-Wempp4s19c9bmCBQKj9R6RaA9CMYTM3kxJWb9-eF-B6YMjs5P66RnEW0YUhMhKJo7_pEeDlVQG6EeaCKO467ArktX4j1-Q1oP_SxYEePnSsewr94TyXZs5pwMdOFKOcy1a7Iba_1fwa460qHMlODZ2QE3Mrb9ZYLMH7f0WpubR5R73DzAZB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
لهستان قهرمان لیگ ملتهای والیبال شد
🔴
لهستان  مقابل آمریکا 3 بر2  به پیروزی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/137238" target="_blank">📅 22:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137237">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIF6qxPCrwY1bLs4Me6YYSEh1ck7ll9NUcp4IwcDdaoxPI17GiE_-KS13ypRKjtT7bsky7YLBFHo70YVWCJmcwqvbeSVLZbo0DAZVKkpuEADyRNoNHSGIYcgd0c6KFAwXSsSdlSVzRrPn6xbRmz1rkMEGurvwlh5bWJ3X3urJKW4Xif1Hgy_RtwldXabXk7L2DQqSzNJNx0ebJXFrwHIFAamqXcZC1r3FX4Y2SwW8Htkq7T8LCaYhEzrY1PklsbfBRwqnhMzrZ8jLjfQGc9CQ2FVmDagqiukl3bImQWODZXCnsOm1yDkeM7LYXaatu2FFXCZGHSjVRvHQ51BRCA6Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎾
فینالِ نسل‌ها؛ فریتز در اندیشه جام، جودار در سودای تاریخ‌سازی،
فریتز و جودار برای فتح جام مقابل هم می‌جنگند!
🎾
رقابت رافائل جودار
🇪🇸
-
🎾
تیلور فریتز رو با آپشن‌های مختلف و بدون خارج شدن از تلگرام همراه با
ربات اسپورت‌نود
پیش‌بینی کنید.
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SorkhTimes/137237" target="_blank">📅 22:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137236">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
❌
رزاق‌پور رسماً و شرعاً منتفی شد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137236" target="_blank">📅 21:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137235">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
ورزش سه: تیوی بیفوما تا این لحظه نتوانسته خودش را به تارتار ثابت کند و در نزدیکی درب خروجی باشگاه قرار دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137235" target="_blank">📅 21:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137234">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚠️
⚠️
⚠️
قدوسی: خرید سوم باشگاه قطعا در پست هافبک خواهد بود ولی تارتار هافبک خلاق و بازیساز میخواد و خصوصیات قربانی بیشتر دفاعی هست تا هجومی. باشگاه قراره به زودی در مورد قربانی تصمیم گیری کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137234" target="_blank">📅 21:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137233">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
مهدی تارتار سرمربی پرسپولیس: از مدیریت باشگاه خواستم که سه بازیکن جدید جذب کنه تا تیم برای‌ فصل‌ جدید تکمیل شود. در پست‌های دفاع میانی، دفاع چپ، هافبک تهاجمی بازیکن جدید میخواهیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137233" target="_blank">📅 21:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137232">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8Xe6xrUhfURjGLgY5RDURDLAu1owB39ZkWuAcC8GlnP954BucB_h7W2urgfLHkRd6H4IfNKBRVOA-Oyx1a-pt3kbRfR3g613PSEZ3vkdS0Uq0Xv9VEC1-2QBR3g7q-qXuEVfIslWMY13ZUazu3UVEo7cb-HXa0NQD3p_HxHXHYDSnqTTVx9Wq-l6EMinY-wvGpaNu5VLy70AErbolUgaJCX2zDRTLirudh05KC3XtpYKIv-uCbbUaoC-5jnbzk1-Cj6QEPBR9r3E7A0bhZDeh21_mZBNvxzjJVAJrGRidFpoYjqQYUySgKIW55fzGq_fErStghvbHoGRsJdeHR9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهدی تارتار سرمربی پرسپولیس: از مدیریت باشگاه خواستم که سه بازیکن جدید جذب کنه تا تیم برای‌ فصل‌ جدید تکمیل شود. در پست‌های دفاع میانی، دفاع چپ، هافبک تهاجمی بازیکن جدید میخواهیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137232" target="_blank">📅 21:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137231">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AW6rSt_1hCkRfNjiKOoyt4hDZvbqYklX7e4L4CeJXO_e9pqDeEVYsavCenhtxWcQl6BCdBUI_8NNvyVNqtmv94pdRw1sVqz6cmtG54W-iyicCc-18uFBp1Gq30bYtPAyaAIFqG0wWIFqafAGIb4b64rinZLi5-lH4sFiJvQl-c-ZAF9jlPJKTsnjNyMpcvohtK-GJbEw4Z7b_SdHkKTlQqRT0T1bGvVuTuTFE96ak7WY8QHLVtqg7vlEtIzYXvpYb1MdLBVKM2CEfhQ9HtFP9eNduBo0RBMX-4iInBAbhq3IGQ78ZDoJA95AO6KfekaYFQcoZQpau1CCVfwqRNxp1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
به‌به بازوبند‌ کاپیتانی‌ رو ببین چه بهش میاد
©
🕶
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137231" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137230">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🏅
پرسپولیس الان یه دفاع چپ میخاد یه پلی میکر…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137230" target="_blank">📅 21:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137229">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🏅
پرسپولیس الان یه دفاع چپ میخاد یه پلی میکر…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137229" target="_blank">📅 20:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137228">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⛔️
یه عده گاب میگن حدادی وعده اسکوچیچ،هاشم نژاد،حسین نژاد،ترابی و دانیال داده بود؛اقا بی زحمت یه مصاحبه بیارید که یک نفر از باشگاه چنین صحبت هایی رو کرده باشه من نامردم تا آخر فصل همه شونو نزنم
⛔️
چهار تا کانال کصشر برای جذب مخاطب خبر فیک پخش میکنن در نهایت…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137228" target="_blank">📅 20:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⛔️
یه عده گاب میگن حدادی وعده اسکوچیچ،هاشم نژاد،حسین نژاد،ترابی و دانیال داده بود؛اقا بی زحمت یه مصاحبه بیارید که یک نفر از باشگاه چنین صحبت هایی رو کرده باشه من نامردم تا آخر فصل همه شونو نزنم
⛔️
چهار تا کانال کصشر برای جذب مخاطب خبر فیک پخش میکنن در نهایت…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137227" target="_blank">📅 20:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137226">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏅
در مقایسه با رقبا بهترین و پربار ترین نقل و انتقالات رو داشتیم ۱-۲ خرید خوب دیگم داریم، تیم تا ۷۰-۸۰ درصد پوست اندازی کرده، تا تیمی بودیم که اردو خارجی رفتیم و برخلاف سال های گذشته با تیم های خوبی بازی تدارکاتی برگزار کردیم.
🔴
واقعا موندم هوادار دنبال چیه،…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137226" target="_blank">📅 20:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137225">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
هم تیم حریف و هم ما با ترکیب دوم مون به میدان رفتیم، یه عده خود تحقیر دنبال زیر بغل مارن، در صورتی که تا پارسال تو بازی های دوستانه اگر شکست میخوردیم تیمو به فحش میکشیدن…عقل ندارن یه عده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137225" target="_blank">📅 20:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137224">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
ارزش تیمی که 6 تا زدیم بهش ارزشش از استقلال، سپاهان و تراکتور بیشتره
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/137224" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137223">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUssPBA5j4hqWk-fnOk3l0-0KayWYyx725VgHYqm1BCudrSq--algpMk985D9EUZWzF3kcSn2J-wnoAmOmqQa5ntI-ZUIbw-3-qRFnIV9Y25zPWiVpyBvq3kmgz-sDUKg2CbZmXUPXQrsPOjFo6FlPRf2Xw5RSA0i65PVnPFKcEaBWVPKfvlNue5kxuq0yBU12_G9c3Evr3hdZY17ULV_GDEfF2Atsd2sO99SaMZJoWs36reW_N4SGlg0qpNE7YeQB8qs-nG3tSjn8l5tOUeTcCVjHrkNIkl1pNECUdIpfFEta-YDh3fP3KrtfDaEM5ZMJqkRwxYWOWceLwdL4bC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ارزش تیمی که 6 تا زدیم بهش
ارزشش از استقلال، سپاهان و تراکتور بیشتره
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137223" target="_blank">📅 19:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137222">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ4qpFbkhCHA-Zpq5fwft85M5z2QqdW1_88hnb6ykPgbPjnmR0gmBe3uOw8Utsb2kPJnm_m5-Thcagdiq_aBDp0FzTfEPkqFNciQNceZWKQKklC6VZbQY0H3hYmxF8_dJO1FOrtJWQHuwmDDF8UDnnbRrGg4enTo-8OmTmzrSGK9piy6jEl4BwwHWbbO_p61-Del2Eotc0cHqqIupqdnVNAdMFu7Uby7eV7VNJF5IefXZz_FU9tq6GOIDCPMvuTdnw9DlOhqzxgkPI_gJQ7y3fMRBpGA0WgHsz9yu24xBaxVX6Tq6u5bJe46N2UUVZvllAcxKgnQrMCwEr72UtIZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🤝
مهدی لیموچی، وینگر تیم فوتبال فولاد مبارکه سپاهان پس از مذاکره با باشگاه، قراردادش را به مدت یک فصل تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/137222" target="_blank">📅 19:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137221">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb3e-emLY4g6xGo_qLVlBq75leBFb0Q50C8TFRhPeXTFIazBsgeD2tCewGG7BiNAUseNnU50HW7GWXGodh0uWwJndutKUbGNWzwN4hFZGfu96mQyI65r2NMtbW4le-pUz7okUoEYZR-POQyZZs2TiDap0HBAfb0rk6Gk5ApsF70BoZxYJQzgffHdGvoo6g6JWdvuNAdi3fO-bQmbv4S9F-sVGh4dnNb5AWndfQ2zxKF9FnZ6318drfjvfi_O8FjmU4Xujh4L1bhdr5OvvPswIXdzJyEwrIGCzK6W1SzyEKRc_8gH6jLVqG_vcPR7uZfDq6z5gY8J5nFCiHlPzucJug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
تصاویری از شادی بعد از گل علیرضا همائیفرد پس از باز کردن دروازه حریف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/137221" target="_blank">📅 19:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137220">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_xkUg3Pp1VQFboa_omElYBTZB6-e6sjZkzb7ISxwp4HzWsOPTHOuXWzNPTktqytyq7u1OwNj-lpQ8fkFra61zn7vcc_cPQUO-d7UcF2yMTsLIoH49YC7vYobv2zXU-TMm8XyP5ipWIWb02-H5ueIlshFgiZGFougn7pCgU2DheOUzGQv2l5IM_spJB3gPNrWyl0ifD0k2KHGW3OmMRBF4F0XVIKCv8f0xPXeAusPyuxXBw9hRt6J9uRL3olX31tLHQQ2m5QEsCqG7pPyOC_rRyBxjb_MGdjlFufeXE3CuGJYm1T4wzXUnX4WXtFEFIRh4c5995WNzNPB7C5QFGVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✅
رسمی؛
نیلوفر اردلان سرمربی تیم فوتبال بانوان پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/137220" target="_blank">📅 19:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137219">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
🥅
گل‌ها: همایی‌فرد،شهرآبادی،صادقی،بیفوما محمودی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/137219" target="_blank">📅 19:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137218">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
پنج بر صفر جلو هستیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/137218" target="_blank">📅 19:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137217">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxAZ_-Xl5ZPVVzpq0BDepXQ02wD5vEPSnDhB9g5QGCicsZaz80sbQF3-E3s87zkZjrvKFsaGzMUIo8_96VRb0yAmA0ODbsqjReLxdRGFVcsZEplj4lqvUUFMocU1KWQjFKsM-9bs0FjgumYffVh8K0dGzCQUIXmtE0o-MejUiA1wRnpWKACrBzd3uFUs8_X23cu5YtpLTUq5-s4Jx34j4J1CC2h7i0mqui05AmTfcL391mXgauL98xMxosZwnAoLnmfN8KDT9FNAQOg8u9Evi4haLlrMkiCkLVXKZiouYkSD4HXFCeof_1W7X-VMldpBuPj1b3akQmkYP4Ex75vTjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس تیمی پرسپولیس برابر ارزروم اسپور در آخرین دیدار تدارکاتی اردوی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/137217" target="_blank">📅 19:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137216">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">▶️
تیم حریف…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/137216" target="_blank">📅 19:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137215">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKEfsz5SkjUDISEVoWrhKRx6tC-4DezSerYE08jgKLp42y3AqEvkc_MOfnMCnEEyhmztEwIBtaGo2CfDXK1FelcAnlENC9eFagKGNYNSPu07AmFAGOSEvWh086sIchPLyu5JmeV6jbiBhxp3tjMaQ0uv1O0CFr5GVAS8A8OogG1rnEJ-D0eJUEtlEK-Su90LLFNUDeVnjNuGYBXPYPEtNRP18_uhVx6FVbj2dVtre7Kmx-35uIxU_K5W7KRVYF4npoftbVfVxGGo7HTPSSJHFR9vz1NDtFljZ4nEOwrObOXLAsUwo3nCtM5J0AaGLz5gsMq4exKKXxVykfBlwp_cuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
تیم حریف…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/137215" target="_blank">📅 19:12 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
