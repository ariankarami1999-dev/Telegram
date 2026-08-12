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
<img src="https://cdn4.telesco.pe/file/WhhBM6f7AkA7Y29iNqYOcm5u7-34VwaAw3uTeaz8iFB6shMOp7MkHoIINx8QghLj1j7sJw3rKpZATo5lFn8bwo7PKXa_eSTJQwf7Ae9-aP09ngCkYAuKfuX8t9LdonEv7EHIUk1jo4ZmOBVFaIQwiWOa5BSjs4IeHdjl3VHMc677p5FV_61ZRk2krC4RkTTzwbHvZ2FhAZSSE9ppHI5qrCSKTXsDefXZdtcEc5BKgRHFb_Q4TpoJY87-a2E1CzvzJ8WRdM0f_axdmeKv4aJBvy-RfEKveve4K5gAWFH77dLQNkU89r3ZyDrsc87cAPw2jE4Cab3FQSWZZAzH4xsDKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 445K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 13:06:38</div>
<hr>

<div class="tg-post" id="msg-20874">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سازمان بین‌المللی دریانوردی:
نشت نفت از نفتکشی که در شمال شرق جزیره قبلیه عمان به گل نشسته است.
انتظار می‌رود نشت نفت از نفتکش کارولین بیزینجی به عمان برسد.
بادها دسترسی به نفتکش به گل نشسته در نزدیکی عمان را محدود کرده و عملیات نجات را به تأخیر می‌اندازند
@WarRoom</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/withyashar/20874" target="_blank">📅 12:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20873">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بلومبرگ
:
سامانه دفاع موشکی «گنبد طلایی» آمریکا نخستین آزمایش‌های اولیه خود را با موفقیت پشت سر گذاشته است.
به گزارش بلومبرگ به نقل از یک مقام ارشد نظامی آمریکا، این مرحله از آزمایش‌ها شامل انتقال داده از حسگرها به رهگیر و همچنین ارزیابی سامانه پیشران فضاپیمای رهگیر بوده است. به گفته این مقام، آزمایش عملیاتی گسترده این سامانه برای اواخر سال ۲۰۲۸ برنامه‌ریزی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/20873" target="_blank">📅 11:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20872">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تحریم‌های آمریکا، صادرات نفت ایران را محدود کرده و باعث شده بخشی از
مشتقات نفتی، از جمله قیر،
به‌جای صادرات در پروژه‌های آسفالت‌سازی مصرف شود؛ تا جایی که علاوه بر خیابان‌ها، بسیاری از کوچه‌ها و جاده‌های خاکی نیز آسفالت شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/withyashar/20872" target="_blank">📅 11:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20871">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مذاکرات ایران و آمریکا درباره تنگه هرمز به نقطه اول برگشت
خبرنگار الجزیره در تهران:
مذاکرات ظاهراً به نقطه آغاز بازگشته و توپ در زمین واشنگتن است؛ تهران ممکن است به این نتیجه رسیده باشد که نحوه عبور از تنگه هرمز نمی‌تواند صرفاً بر اساس خواسته‌های آمریکا تعیین شود.
@WarRoom</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/20871" target="_blank">📅 10:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20870">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97fd9de97.mp4?token=LcpIBDzj6l7kUUNwS3CkYdP0L-wt5sTCTNjb5Us708Fd6hhJbFgOy75SkgXMuPQsUF-KqG26X5zI89tPYklWwRmDxI0dKGHChdpVqjaPOw5sBlHaAlVNZCeW5WHryx8wBbNtd0ap7F2Oab0piZJQrqjAY18vwL1ZMmsgexlqv1rv_BdacqCE-ORr3j24X8oU2AtfC3SYOseAPxdYmrPTN9erGOOA8sdSTxYrOkNRusCN22O2BfKbJrMgfqVItzloe_vvCIDN1CeZaEjGeW4zlN7zzmHeE5BKncJsRW_bmXgrox3dfuryCP1ub-6yCu_IlY0urohB0XwcIfnD82mQtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97fd9de97.mp4?token=LcpIBDzj6l7kUUNwS3CkYdP0L-wt5sTCTNjb5Us708Fd6hhJbFgOy75SkgXMuPQsUF-KqG26X5zI89tPYklWwRmDxI0dKGHChdpVqjaPOw5sBlHaAlVNZCeW5WHryx8wBbNtd0ap7F2Oab0piZJQrqjAY18vwL1ZMmsgexlqv1rv_BdacqCE-ORr3j24X8oU2AtfC3SYOseAPxdYmrPTN9erGOOA8sdSTxYrOkNRusCN22O2BfKbJrMgfqVItzloe_vvCIDN1CeZaEjGeW4zlN7zzmHeE5BKncJsRW_bmXgrox3dfuryCP1ub-6yCu_IlY0urohB0XwcIfnD82mQtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ : «من از طریق سرویس مخفی و ارتش اقدام می‌کنم. آنها می‌خواستند من با پرواز دیگری، با هواپیمای دیگری بروم... من هر کاری که آنها بگویند انجام می‌دهم... حدس می‌زنم تهدیدی وجود داشته است. من واقعاً زیاد در مورد آن سوال نکردم. تهدیدهای زیادی دریافت می‌کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/20870" target="_blank">📅 09:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20869">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e3f3981e.mp4?token=M6GmPjMr1Mucu3THQ_SlZO8S56nMvrvlCSqqzT98dJw0q0mJj2SYwHeQ8tSz8irs8ICOaHk98ltfwOaLpaRJEdNjuotrmWuwVILeDs4le7rROyFUjjP33x4N3JUoZqysi8HFfhPJSH3ERzkfZZM27dsuGQdccybqxad1F9WQXNLi1BUYIGdhynrIs2MZ5AbVYU9kSIftxr5cM6_mGhLuBZaLD3iV1fnJDKjPMbZ7ptJsbtpl5hU-TwUC4QYEqGLX2-EdbtO_E7UI2-p9L6tlyRCkIt0j-6zTewMjO3buZQe8ipWzMjDEwmz1yTZgfxXyxbYoimMaElQyo1xoxzr9bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e3f3981e.mp4?token=M6GmPjMr1Mucu3THQ_SlZO8S56nMvrvlCSqqzT98dJw0q0mJj2SYwHeQ8tSz8irs8ICOaHk98ltfwOaLpaRJEdNjuotrmWuwVILeDs4le7rROyFUjjP33x4N3JUoZqysi8HFfhPJSH3ERzkfZZM27dsuGQdccybqxad1F9WQXNLi1BUYIGdhynrIs2MZ5AbVYU9kSIftxr5cM6_mGhLuBZaLD3iV1fnJDKjPMbZ7ptJsbtpl5hU-TwUC4QYEqGLX2-EdbtO_E7UI2-p9L6tlyRCkIt0j-6zTewMjO3buZQe8ipWzMjDEwmz1yTZgfxXyxbYoimMaElQyo1xoxzr9bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
:
من به ایران اعتماد ندارم، چرا؟ مگه فکر می‌کنید به ایران اعتماد دارم؟
من آخرین کسی‌ام که به ایران اعتماد می‌کنه مدام به من دروغ گفتن، الان ما کاملاً کنترل تنگه رو در دست داریم
اونا کنترلش رو ندارند، ما کامل کنترلش می‌کنیم، مال ماست، شاید یه زمانی کاری بکنن و اون‌وقت کارشون تمومه
@WarRoom</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/20869" target="_blank">📅 08:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20868">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ
:
تهدیدهای زیادی علیه من هست که شما ازشون خبر ندارید
هر رئیس‌جمهور تأثیرگذاری تهدیدهای زیادی دریافت می‌کنه، رئیس‌جمهورهای بی‌اهمیت تهدید نمی‌شند
فکر می‌کنم شاید من تأثیرگذارترین رئیس‌جمهور باشم
@WarRoom</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/20868" target="_blank">📅 08:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20867">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ
،
درباره نامزدیش :  دوست دارم دوباره تو سال ۲۰۲۸ نامزد بشم، ولی قانون اجازه نمی‌ده
@WarRoom</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/20867" target="_blank">📅 08:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20866">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ درباره اینکه چرا خودش با ایر فورس وان پرواز نکرد ولی خبرنگارا پرواز کردن : نمی‌دونم، اتفاقاً فکر می‌کنم هواپیمایی که من سوار شدم بیشتر در معرض خطر بود
خبرنگار : چرا؟ ترامپ : چون فکر می‌کنم همون هواپیمایی بود که احتمال بیشتری داشت هدف قرار بگیره
@WarRoom</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/20866" target="_blank">📅 08:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20865">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edfa0f08c.mp4?token=uU_8bzRxPach-5ObQ0U2cRfwx5ArERwiXofctXT2PqVDPtmdwxAvx_MRfAzF5CHKw66nxNQQUrPdEFvIJPhG_FSFLccFRRV98a322hIsC8Vv9tDO2O6mOxNcgl0h_1p6ZUzmjslxrsjFCKztjuR61S8_J-S1UOnSpQaJ0B6Yn48WK3CBByi0eV9-7Z0bpMyqx-iaM8J0EeOnBlIj7v5aOF61gMh4KiCYIUSlPMoyzXXCAVMaraZzI_9HJxTT6_KmoK4QzcJCfpmGX2wcqblQ7B7nTb9bmlwPC69R7AXdRzMdvGlyRG_tp4CCr5P4X2L1Ojb1StKCGgG3wp2hxgnrLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edfa0f08c.mp4?token=uU_8bzRxPach-5ObQ0U2cRfwx5ArERwiXofctXT2PqVDPtmdwxAvx_MRfAzF5CHKw66nxNQQUrPdEFvIJPhG_FSFLccFRRV98a322hIsC8Vv9tDO2O6mOxNcgl0h_1p6ZUzmjslxrsjFCKztjuR61S8_J-S1UOnSpQaJ0B6Yn48WK3CBByi0eV9-7Z0bpMyqx-iaM8J0EeOnBlIj7v5aOF61gMh4KiCYIUSlPMoyzXXCAVMaraZzI_9HJxTT6_KmoK4QzcJCfpmGX2wcqblQ7B7nTb9bmlwPC69R7AXdRzMdvGlyRG_tp4CCr5P4X2L1Ojb1StKCGgG3wp2hxgnrLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
:
اوضاع ایران داره عالی پیش میره ما کاملاً کنترل تنگه هرمز رو در دست داریم و نیروی دریایی‌مون فوق‌العاده‌ست
@WarRoom</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/20865" target="_blank">📅 08:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20864">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">زاکانی : آقا مجتبی داشت تلویزیون میدید یهو تو اخبار شنید رهبر شده
@WarRoom</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/20864" target="_blank">📅 08:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20863">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87bdfe17b.mp4?token=OHWQRoyQZhScSpFsMez0EwCR3Z32HvRzrhiPx3Z_GVeDjLu6k7SuFhnnRiEmDvLGKlMF6n_kdgfANqZ9xtFGgkry9y0QAPVFpavU9riJq_Rz7EXYb9rd91yxPMhd6UhjSCDnsLDhSuH3L0bzXJiEviqYxxA_tsQ4CrHOQWpJJGHOweonnIBpruq2EYmB1Ycbj7Dlzvo0aUOMMdjIWtW-H-KbpE9f5SbPht-M-RsEPUIq9nvp-3z6UoN1eJnHA8tVyAEXSMh1LRTYQuP1vOQCzc7vGlRc4_Ip2yVsH1Mc_gKeyZEsFcvL46V6arQt1ebDv3hRVwsUzkvnidIuQdzyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87bdfe17b.mp4?token=OHWQRoyQZhScSpFsMez0EwCR3Z32HvRzrhiPx3Z_GVeDjLu6k7SuFhnnRiEmDvLGKlMF6n_kdgfANqZ9xtFGgkry9y0QAPVFpavU9riJq_Rz7EXYb9rd91yxPMhd6UhjSCDnsLDhSuH3L0bzXJiEviqYxxA_tsQ4CrHOQWpJJGHOweonnIBpruq2EYmB1Ycbj7Dlzvo0aUOMMdjIWtW-H-KbpE9f5SbPht-M-RsEPUIq9nvp-3z6UoN1eJnHA8tVyAEXSMh1LRTYQuP1vOQCzc7vGlRc4_Ip2yVsH1Mc_gKeyZEsFcvL46V6arQt1ebDv3hRVwsUzkvnidIuQdzyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در محل بازی‌های میهن‌پرستانه:  به والدین نگاه می‌کنم، آنها به فرزندانشان بسیار افتخار می‌کنند. و من به گروه افراد حاضر در این اتاق بسیار افتخار می‌کنم. عشق به کشورمان را می‌بینید. کشورمان هرگز بهتر از این نبوده است!
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20863" target="_blank">📅 02:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20862">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">چیزی نیست رعدنیاهو بود غرب تهران
😂</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20862" target="_blank">📅 02:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20861">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارش صدای رعد و برق شدید</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20861" target="_blank">📅 02:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20859">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بلومبرگ
:
دونالد ترامپ موضع خود را در قبال ایران سخت‌تر کرده است و این امر، امیدها را برای دستیابی به توافقی جهت بازگشایی تنگه هرمز کمرنگ‌تر ساخته است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20859" target="_blank">📅 01:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20858">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گزارش ها از درگیری تمام عیار زمینی میان حوثی های یمن و نیروهای نظامی وابسته به عربستان در شمال یمن.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20858" target="_blank">📅 01:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20857">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آمریکا 2 هزار گیمر رو به‌خاطر تصمیم‌گیری سریع و عملکرد خوب تو شرایط پراسترس ، برای برج مراقبت فرودگاه‌ها استخدام کرده
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20857" target="_blank">📅 01:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20856">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ab5e54bb.mp4?token=mRzir3BrqEAy9wQJ07jWQxGy6wF1rQbhrc5Bz3Vb-QjIZWT6XVs-5XNlrY5-XVSj2XArh7OYN_Y04-K_py3dXBky_k489_cT_SQeVAOPahqCa_uppux9frsjAwNJVprhcJWfC7JR9Ug4RkYqosU1bzegNBBU8sBDzZ0HBBdqL5aDrmBfG-0I0wLwqFPRqRUgG4LG_2mUpP1tNcK5Qd0SAH6AKB3M0Ia3e4PRVVmIVxhlCQeDx6ivFpicH4zfuMCO0mnkaiWCRoLuAeiEXbvL1HHAMJfX0ucOysYHVCUuZ8ma3ZgRe2eWQZp0h4ypRUrPQ84Gpuw2FUpKSLBk7jyI3nTZiw8F5FjhTDbo0um2rcOgUAdi8YfS7aBC7fidyLAktHKTIH8M9SA8f9HWm4PkjGiyjcXIUU1HmCoLg3Qj0wSdZw3ROKJXXJ1ZoA0spdQUtpShLvuWFv_CxnFmFvzaYAOAptHGhnR-KLvTsXAuhyZGzNlg9rYJeDkV6Or40qmpteEluuguNlTJtG4E-g6I0bt6WLAH3-Jnq3rB9w2qni7fBs9WWVdMJmN2xqbY1TtRK4njcrr7IQUebRs8KWDvrSajILLhg9HSuHJzU5MHdHrCPEkFNuWs9Qs7vCSolsR84I4-rL2hBEBDRssRT20nZ0YJ0W7D8I4QZXO50VaZ3dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ab5e54bb.mp4?token=mRzir3BrqEAy9wQJ07jWQxGy6wF1rQbhrc5Bz3Vb-QjIZWT6XVs-5XNlrY5-XVSj2XArh7OYN_Y04-K_py3dXBky_k489_cT_SQeVAOPahqCa_uppux9frsjAwNJVprhcJWfC7JR9Ug4RkYqosU1bzegNBBU8sBDzZ0HBBdqL5aDrmBfG-0I0wLwqFPRqRUgG4LG_2mUpP1tNcK5Qd0SAH6AKB3M0Ia3e4PRVVmIVxhlCQeDx6ivFpicH4zfuMCO0mnkaiWCRoLuAeiEXbvL1HHAMJfX0ucOysYHVCUuZ8ma3ZgRe2eWQZp0h4ypRUrPQ84Gpuw2FUpKSLBk7jyI3nTZiw8F5FjhTDbo0um2rcOgUAdi8YfS7aBC7fidyLAktHKTIH8M9SA8f9HWm4PkjGiyjcXIUU1HmCoLg3Qj0wSdZw3ROKJXXJ1ZoA0spdQUtpShLvuWFv_CxnFmFvzaYAOAptHGhnR-KLvTsXAuhyZGzNlg9rYJeDkV6Or40qmpteEluuguNlTJtG4E-g6I0bt6WLAH3-Jnq3rB9w2qni7fBs9WWVdMJmN2xqbY1TtRK4njcrr7IQUebRs8KWDvrSajILLhg9HSuHJzU5MHdHrCPEkFNuWs9Qs7vCSolsR84I4-rL2hBEBDRssRT20nZ0YJ0W7D8I4QZXO50VaZ3dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ برای شرکت در رویداد
Freedom 250 Patriot Games
(رقابت‌های میهن‌دوستانه ورزشی ویژه جوانان آمریکایی به مناسبت ۲۵۰مین سالگرد استقلال آمریکا) عازم شهر ژنو در ایالت اوهایو شد و سوار هواپیمای ریاست‌جمهوری
ایرفورس وان
جدید شد
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20856" target="_blank">📅 00:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20855">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گزارش ها از هدف قرار گرفتن ایست ‌و بازرسی نیروهای نظامی توسط افراد مسلح ناشناس در شهر مرزی خاش در سیستان و باوچستان ، بر اساس گزارشات داخلی 4 نظامی در این حادثه کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20855" target="_blank">📅 00:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20854">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">محمدرضا نقدی، مشاور فرمانده سپاه، گفت که «این سازمان باید برای انجام عملیات هوشمند در خاک دشمن آماده شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20854" target="_blank">📅 00:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20853">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پرواز بالگرد آپاچی ۶۴ آمریکایی در نزدیکی قشم  @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20853" target="_blank">📅 00:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20852">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFM_EigLFctsNOdx18c30WHEIgzCu28WClxW5MT14gHf1SF7c8_yRHGV8WBo34CeFaKNeGH9TrMuQrswC5yCSBIoPMmZUjs9fd3hC-drYmKC2s1FR88k7l2XHr_6oaSDzR0pUyYDo4cTp6Jg52Op8Eb0mFeclLZZ0ZcAFEilcNwr36lrp65wI-R2_Dso5sYnhSjmfxedhfl62U5CnKO1UHYw-ijkjIDijJHR0mpgdG5jf1HUx6uAHCd1Z-AGp2rDHgX14Lv8rk1JJgCPVY6syZ-JpaYIwFeEunfDrBjZK0iIr1COwxa4eUD8B5ZyIj7zZUwxBGydkJkx0Z7dEncU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل: مجتبی شش تندرو جدید را برای رهبری جنگ بعدی ایران منصوب می‌کند
با وجود شایعات فزاینده درباره سلامت مجتبی خامنه‌ای، تهران ادعا می‌کند که او شش تندرو از رژیم را برای رهبری جنگ بعدی ایران منصوب کرده است؛ پیامی نگران‌کننده برای اسرائیل و ایالات متحده مبنی بر اینکه رژیم در حال تشدید تنش‌هاست، نه عقب‌نشینی
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20852" target="_blank">📅 23:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20851">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">باراک راوید , آکسیوس : امید به توافق میان جمهوری اسلامی و آمریکا در حال محو شدن است
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20851" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20850">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEpKnGPJtpjWvYHo8UBUXeXWAFoCusjhuPSbSE1rTabgwE-HJ5t3J7MGcJmYOQfRDunPmd_uIz4oEznHcUJJAFRpjDqrla9LoBA24ZnJ0FZ5GVGUAb4-SrO7G7oD98_Qh6AN3qr-licKFCuSAELaz8wty8IWc3T0QHECYGdQXYWJ8vCMrOF931i9GZP3-EESPs-bClrC3YcRrzUD-_rrhb3q88TK0kx9SIgIgU1rOxSMcrDYe0Hz-2hqeWB452GK0QkMvNlL9j-wTBIC0V_dka3a4L-xUjmp9SFSMhGWw2JfEA_PT1X0nLw7vWsJqpYDOGV3GyFGUckKwOxwSe6kVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد نیروهای آمریکایی امروز کشتی باری «ولا نوا» با پرچم پاناما را هنگام حرکت به سمت یکی از بنادر ایران در خلیج عمان متوقف کردند. پس از بی‌توجهی خدمه به هشدارهای آمریکا، یک بالگرد MH-60 دو موشک هل فایر به اتاق موتور کشتی شلیک کرد و سامانه هدایت آن را از کار انداخت. سنتکام گفت تا ۱۱ اوت، ۵۵ کشتی تجاری را تغییر مسیر داده، ۳ کشتی را از کار انداخته و ۲ کشتی را سوار و بازرسی کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20850" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20849">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA B</strong></div>
<div class="tg-text">یاشاار
جون هرکی دوست داری زارتان زورتان و حذف نکن از ادبیاتت
من هم توهمی دهنم سرویس شده
از وقتی نمیگی برکت از جنگ رفت
🤣
خداییش جدی میگم</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20849" target="_blank">📅 22:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20848">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سازمان دریایی بریتانیا: فعالیت‌های سپاه در تنگه هرمز در طول 48 ساعت گذشته ادامه داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20848" target="_blank">📅 22:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20847">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دونالد ترامپ در چارچوب قانون اختیارات جنگ آمریکا (War Powers Resolution)، با ارسال نامه‌ای به کنگره که ۱۹ تیر ۱۴۰۵ امضا و ۲۲ تیر ۱۴۰۵ به‌طور رسمی اعلام شد، از ازسرگیری عملیات نظامی علیه ایران خبر داد. با این اقدام، مهلت قانونی ۶۰ روزه برای ادامه عملیات نظامی بدون مجوز جدید کنگره آغاز شد. این اقدام به معنای صدور مجوز جنگ از سوی کنگره نیست، بلکه صرفاً روند قانونی اطلاع‌رسانی به کنگره و آغاز مهلت ۶۰ روزه را فعال می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20847" target="_blank">📅 21:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20846">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20846" target="_blank">📅 21:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20845">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">من با دیتا های اپن سورس تحلیل میکنم پیشگو که نیستم ! هیچ تاریخی هم نمیدم فقط احتمالاته اگه انقدر حساسی  پس از الان رو نزدن حساب کن  ! اگه حرفه ای هستی پس ویس هارو گوش کردی کامل روحیات منم میدونی و دیگه سوألی هم نداری که هی داریکت بدی</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20845" target="_blank">📅 21:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20844">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به نظرت قطعی شنبه میزنه من میخوام با بچه ها شرط ببندم</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20844" target="_blank">📅 21:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20843">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSajad Mousavi</strong></div>
<div class="tg-text">به نظرت قطعی شنبه میزنه من میخوام با بچه ها شرط ببندم</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20843" target="_blank">📅 21:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20842">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش ۲ ‌انفجار یا پرتاب موشک/پهپاد از سیریک @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20842" target="_blank">📅 21:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20841">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش ۲ ‌انفجار یا پرتاب موشک/پهپاد از سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20841" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20840">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ اعلام کرد که رابرت گیلمن، سرباز سابق نیروی دریایی ایالات متحده که در سال ۲۰۲۲ در روسیه زندانی شده بود، پس از گفتگوها با ولادیمیر پوتین، آزاد شده و به ایالات متحده بازمی‌گردد.
ترامپ گفت که روسیه موافقت کرده است گیلمن را بر اساس «ملاحظات انسان‌دوستانه» آزاد کند و «هیچ مبادله‌ای انجام نشده است».
ترامپ همچنین گفت که اولین درخواست گیلمن یک «همبرگر عالی» بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20840" target="_blank">📅 20:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20839">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ : ما بر پول ایران کنترل داریم و کنترل کاملی بر آن اعمال می کنیم
ترامپ : سلاح و جنگنده به اروپا می‌فروشیم و آن‌ها در ارسال به اوکراین آزادند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20839" target="_blank">📅 20:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20838">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اسرائیل و ونزوئلا پس از ۱۷ سال قطع روابط دیپلماتیک، توافق کردند که روابط کنسولی خود را از سر بگیرند و یک کانال هماهنگی رسمی ایجاد کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20838" target="_blank">📅 20:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20837">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797367122e.mp4?token=BvEpAfeAfl63_KiiVEZtAZ2O4zpjQeifPPwvO7SMHn4BqOSNVtrwwaNpVWSZ_F6IuiutS9mOCgZpYa4Uf69LlUzS_cZ2TtSLUeIF6l1yEvOtULIfF6-vBSsRMb-2PRZq-GNhMBxzRuc0A_Zkq-plmkZ6HZMYq0SZ6LzZ9trneLKal_kfx2P6U7CKATWIV9tiKp_ExU9plHB5dKvdTuN7kAV9om4DOdIC_LFbiywoLszot_Sggh016Zn_8eNJ9HimbT7fQd16WVlZEEPFbflD7FncHiyY2GJWbl_jZw6Gt0-gLmHx2CtU7M9FBqMvn1xOEhy8oCLUEY1GrmrKSNLRHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797367122e.mp4?token=BvEpAfeAfl63_KiiVEZtAZ2O4zpjQeifPPwvO7SMHn4BqOSNVtrwwaNpVWSZ_F6IuiutS9mOCgZpYa4Uf69LlUzS_cZ2TtSLUeIF6l1yEvOtULIfF6-vBSsRMb-2PRZq-GNhMBxzRuc0A_Zkq-plmkZ6HZMYq0SZ6LzZ9trneLKal_kfx2P6U7CKATWIV9tiKp_ExU9plHB5dKvdTuN7kAV9om4DOdIC_LFbiywoLszot_Sggh016Zn_8eNJ9HimbT7fQd16WVlZEEPFbflD7FncHiyY2GJWbl_jZw6Gt0-gLmHx2CtU7M9FBqMvn1xOEhy8oCLUEY1GrmrKSNLRHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز بالگرد آپاچی ۶۴ آمریکایی در نزدیکی قشم
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20837" target="_blank">📅 20:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20836">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رسایی : چونکه نمیدانیم اسرائیل کِی حمله میکند مجبوریم جلسات مجلس را مجازی کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20836" target="_blank">📅 20:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20835">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پست قبلی بی بی پاک شد این پست کارای اداری رو انجام بدید
https://www.instagram.com/reel/Db6BHf7MYhi/?comment_id=17896725462373851</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20835" target="_blank">📅 20:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20833">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نتانیاهو : جولان سرزمین ماست و برای همیشه متعلق به اسرائیل خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20833" target="_blank">📅 18:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20832">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دونالد ترامپ: ایالات متحده می‌تواند بزودی و با قدرت بسیار زیاد به ایران حمله کند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20832" target="_blank">📅 18:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20831">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یوآو کیش، وزیر آموزش اسرائیل:
صرف نظر از اینکه رئیس جمهور آمریکا چه کسی باشد، حتی پس از ترامپ,  اگر لازم باشد به تنهایی اقدام کنیم، به تنهایی اقدام خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20831" target="_blank">📅 17:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20830">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-FeAdLC1AziYrV_7EOHY_IJqcP5Ve3NaUOmJXKWGZLecI2jW3eiq-och1osYGh_GIiopGMTMCWyVtPoIMd_Fxh7ccpr_EoFY0Edker0DhKH_hjMrKJs1gjHV7NiuQX49GPbiPohPwFQrSvWxyY--3GMVkOLhb7skJT-e25QxY2RGM_Dn1lm1HG7DmUp76T1nBNGNPNZC26qtT01sJp__E3NVMEvTHZinURXEhi_xCsI1XfNLuA7Mu6UKqVCKj9_d4itAuHmj4SU6v2YBnsl0XVb2hAXhpdG7ao3Db_bJZAklJeICWeG4pFSwlJTl8QdErEEfIJUNZA0olCw63l1Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه اسرائیل : ترکیه این جسارت را دارد که از اسرائیل انتقاد کند؛ اما واقعیت‌های میدانی چیست؟ هزاران سرباز ترکیه و ده‌ها پایگاه و موضع نظامی در سوریه، عراق و قبرس مستقر هستند. در حالی که تجاوز نظامی اردوغان مرزی نمی‌شناسد، ترکیه ۳۶ درصد از خاک قبرس، ۵ درصد از خاک سوریه و ۲ هزار کیلومتر مربع از خاک عراق را در اشغال خود دارد. در مقابل، اسرائیل به‌طور موقت تنها ۰.۱ درصد از خاک سوریه را در اختیار دارد؛ منطقه‌ای حائل که به گفته اسرائیل، برای حفاظت از شهروندانش در برابر تهدیدهای امنیتی اثبات‌شده ایجاد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20830" target="_blank">📅 17:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20829">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">به گزارش رسانه‌های اسرائیلی،
یوسی کوهن، رئیس پیشین موساد در نشست «مجمع جلیل» در شهر صفد گفت: «ما بارها از سایت هسته‌ای فردو بازدید کردیم تا این سایت را درک و شناسایی کنیم.»
او مشخص نکرد که این بازدیدها چه زمانی انجام شده یا دقیقا چه کسانی از این سایت بازدید کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20829" target="_blank">📅 17:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20823">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">روال هر روز پیج اینستاگرام در ۴ دقیقه ریکاوری شد
😁
عرضشی عر بزن
🤣</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20823" target="_blank">📅 16:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20822">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qx1bqZ49iNa8jbWuI8eiVHTx7ONHVeemqqsItpJTKtxstGtjttDKM-otYAVgP3i5jgsEmFclk4ur0-lJYcgt4a36Cb_NBjRvtmaZ8_pORWXYbPm4FQnkZ2gPozzuybJ422Z12p86OVNmyCNMMkZZryK8r9zy5mz9V1ybtF6a6CgHCfHi8r-oM2xQUq4yA_a_z8rqygROKIz9Rhuzy9GxMgW-0Gi6mT1-Y53DrMmbv-cD0HZlLb1Z6LF1-91cIsF9cLjW59upZMZJvxDSaQOVqL9a2l5Je2YaG-hGo65BANyqcc0aw5V3AfnbPmQA33OObyJozhQ16OJJbiEvIlquaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی بی دوزندهیاهو : آتش‌سوزی در کارخانه نخ اطراف بیدگنه،  ملارد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20822" target="_blank">📅 16:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20821">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دبیر شورای عالی امنیت ملی ج.ا : ما در یکی از حساس‌ترین و سرنوشت‌سازترین مراحل تاریخ معاصر خود قرار داریم , در برابر تهدیدها، از حقوق خود و منافع ملت‌مان عقب‌نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20821" target="_blank">📅 16:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20820">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وال استریت ژورنال : نیروهای آمریکایی امروز به سمت یه کشتی که با پرچم پاناما حرکت می‌کرده، شلیک کردن. ظاهراً این کشتی قصد داشته محاصره بنادر ایران توسط آمریکا رو نقض کنه. @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20820" target="_blank">📅 16:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20819">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وال استریت ژورنال : نیروهای آمریکایی امروز به سمت یه کشتی که با پرچم پاناما حرکت می‌کرده، شلیک کردن. ظاهراً این کشتی قصد داشته محاصره بنادر ایران توسط آمریکا رو نقض کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20819" target="_blank">📅 16:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20818">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزیر دفاع پاکستان به بلومبرگ:
نشانه‌های روزهای گذشته حاکی از آن است که به توافق صلح (یاشار: بمباران) نزدیک می‌شویم
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20818" target="_blank">📅 16:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20817">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">روال هر روز پیج اینستاگرام در ۴ دقیقه ریکاوری شد
😁
عرضشی عر بزن
🤣</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20817" target="_blank">📅 16:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20816">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آکسیوس
:
به گفته مقام‌های آمریکایی و اسرائیلی، دولت دونالد ترامپ در پشت‌پرده میان سوریه، اسرائیل و آژانس بین‌المللی انرژی اتمی برای خارج کردن مواد هسته‌ای از «سایت ۹۹» سوریه، مرتبط با برنامه هسته‌ای مخفی حکومت بشار اسد، توافق ایجاد کرد. این مواد شامل «کیک زرد» است که برای ساخت سلاح هسته‌ای کافی نیست، اما می‌تواند در بمب‌های رادیولوژیک به کار رود. اسرائیل پس از سقوط اسد با نگرانی از دسترسی به این مواد، ورودی‌های سایت را هدف قرار داده بود. عملیات انتقال هنوز انجام نشده، اما مقام‌های آمریکایی می‌گویند به‌زودی اجرا خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20816" target="_blank">📅 15:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20815">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وال‌استریت ژورنال : خامنه‌ای با تغییر مقام‌های ارشد امنیتی بر ادامه تقابل با آمریکا تاکید دارد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20815" target="_blank">📅 15:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20814">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش حمله موشکی به اردوگاه گروه‌های کورد در شمال شرقی اربیل
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20814" target="_blank">📅 15:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20813">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzM0AvsKTBU65iyzCJJpw3MosZqds3LBdNkj0zy83oOlRFXkbz99A0aqjDpwI9-Jo83mcJC0F_jffrpmPEEUOAi01ixbIDYOG_SMkdon0rVzsZWJvleAjvYmLwod8H_M_bb-M0bYlt4R1IlE7ATa8x9N_NinUvm9JMKg2G3kbNcxyaxTq6eZCx4rH-IbG90cwQ8O-Paf2jD50GZiQEdxvtWwGFKjZS1jxeZEIRUrSs71RWXJJwNQnEA8yfVq--4NWnniv24Q6d50RewpjzBxYePegS-YVq3EHCPGBPriIH0__B8jATjOfpkR3p8F7Yqsjcs22w8TFbY5oSZHsfNa8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری رویترز، سازمان حمل و نقل دریایی بریتانیا (UKMTO) از حادثه‌ای در سواحل المخا، یمن مطلع شده است. گزارش شده است که یک کشتی باری در دریای سرخ جنوبی مورد اصابت یک موشک/پهپاد ناشناخته قرار گرفته و منجر به تلفات جانی شده است ، این در حالی است که یک کشتی سعودی صبح امروز مورد هدف قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20813" target="_blank">📅 14:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20812">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سید محسن رضا نقوی، وزیر کشور پاکستان برای گفتگو با مقامات ایرانی وارد تهران شد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20812" target="_blank">📅 14:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20811">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رسانه عبری : مجتبی خامنه‌ای، از احمد وحیدی، فرمانده کل سپاه پاسداران، خواست تا برای «عملیات تهاجمی قدرتمند علیه دشمن» آماده شود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20811" target="_blank">📅 13:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20810">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ درباره ایران: ما سه راهبرد داریم , همین کاری را که الان انجام می‌دهیم ادامه دهیم؛ فقط به همین شکل پیش برویم و ببینیم اوضاعشان چقدر بد است، چون تورمشان ۳۰۰ درصد است. پولشان تقریباً هیچ ارزشی ندارد. حقوق سربازانشان را نمی‌دهند. سربازانشان در حال ترک خدمت هستند. بنابراین همین روند را ادامه دهیم، چون این وضعیت پایدار نیست.
خیلی، خیلی سخت به آنها ضربه بزنیم؛ یا در واقع، راه سوم این است که از نظر اقتصادی آنها را شکست دهیم. البته همین کار را همین حالا هم انجام می‌دهیم. این تا حدی بخشی از راهبرد اول است.
بنابراین از نظر اقتصادی، آنها در وضعیت بسیار بدی قرار دارند. نمی‌توانند پول قرض بگیرند. ما کنترل پول آنها، یعنی آنچه در اختیار داشتند، را در دست داریم؛ و مقدار آن هم زیاد است. آنها پول زیادی داشتند و ما کنترل کامل آن را در اختیار داریم.
من بانکدار آنها هستم. من بانکدار آنها هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20810" target="_blank">📅 13:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20809">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ : می‌خواهید یک گورستان پرندگان را ببینید؟ گاهی اوقات به زیر یک آسیاب بادی بروید و هزاران پرنده مرده خواهید دید.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20809" target="_blank">📅 13:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20808">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جورسلیم پست : ترامپ از حمله گسترده دیگری به ایران خودداری کرد ، با این امید که فشار اقتصادی بیشتر می‌تواند تهران را مجبور به تسلیم کند، بدون اینکه منجر به یک جنگ منطقه‌ای گسترده‌تر شود.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20808" target="_blank">📅 13:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20807">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSs7NlUoDR9M3YxIsGdRCF2lXVuk6QCmlodDubyhR1hG79c4ONkBi0_PUH9f1zjIrApIg0hr2LyuC0gQErUF6uqSYtW-TyeCKvaYAoVjl776vTN0gKdQPxI3Ndr5dXwvHWGW7I7BYCwx9b9nbsiu0UE3OAuPuLlFSoOcgznwRJblu4ecNnTgxjeNFN7A892azpVZsfC_q7J7jBCqqyPmQgRpg_kP6e2aOEcVrpr9RC9yfOlsPb3NcIg5l9NMNjUPn-pcQX_fpJMminw_JrNggISP32IkRxygO40EOuX3xRbiGfsWfNXe905QI0VlORDpi_IavsKuwHlPmlGnZsxgNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی درباره وقوع حادثه‌ای برای یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است. مقام‌های مربوطه در جریان این حادثه هستند و تحقیقات مرتبط همچنان ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20807" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20806">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t15ymLEUkHuSTe8uAFgKYdyP3J6K6jxQGsqDY9ZYwQpNTqySB_lrilRCTEBTskH_w77m6eM2c0_DDAS-UwYF3I6KTPVJHy20gbEab0KgAeNzKcefPJMhQUwpdXKYdRbWylLYcYVrk8mnJSesuD5KSB1seE6UDJEXp2CglQPHUGlQUTocth2nmiaSkomEgDSEGK2jIW7TGymzCwMZoxJjmbl4shfRpfc5gyZdGp6QE5oXuswXXZxBXK1HyFeZwfy2e00r_lHvWtEKIX7wcklvJQr7CUj2Px1pJ-j_su6LXtPZzPUCGLGDaejrFDJxhjoGWGTjTR0noi4yweDul8UkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان KC-46A پگاسوس نیروی هوایی آمریکا از پایگاه‌های مبدأ خود در غرب ایالات متحده به پایگاه هوایی مک‌دیل در فلوریدا، در شرق آمریکا، منتقل شده‌اند؛ جابه‌جایی‌ای که می‌تواند نشانه‌ای از آماده‌سازی برای اعزام قریب‌الوقوع شماری از هواپیماهای…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20806" target="_blank">📅 12:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20805">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دادگاه جنایی دمشق حکم اعدام برای بشار اسد صادر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20805" target="_blank">📅 12:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20804">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">https://www.instagram.com/reel/Db5HBuLozsg/?igsh=ajBqMW82djZrZW96
استوری که درخواست زیاد داشتید رو به صورت تریال پست کردم</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20804" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20803">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارشهای رسانه های‌عربی حاکی از کشته شدن ۳ نفر در پی حمله حوثی ها به یک کشتی در تنگه باب المندب است
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20803" target="_blank">📅 10:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20802">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqd6sQkOWNcqi4mc2Swfbbt-_UAG6HInqncbLjlP2ZXTcYGIKotG4ibxvp5rEbM1IcQJBv5eG95-C7G-pUWCD5N5GBEHsRbF41UW4C4-OYrmy7Bt7E2fexOVRYi2C21hs_9grXbcC6ZJZ_9wz-Me2MsCUJeOuBWFN8fiUuGoLQo2_yGGq-YwwZv_g_VrAIP7doGY_-j5jXOKdrxhEwmqwv0bDwGT2QM-9sOBxTtKi5AeWVXwgSs8IWsGGbhcA9jgaxP_mivYMVqX4kzMaWNWTmGRWivEPmPc5iEKfyaC8ygR34fXokYV7YTp_uufQTEnuFRD6Y2JQRrqCMH5dsh28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برای عبرو از ۹۰$ خیز برداشت
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20802" target="_blank">📅 10:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20801">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ: ما بر اساس سه سناریو با ایران عمل می‌کنیم: اول، نظارت بر وضعیت نامناسب آن؛ دوم، اعمال فشار اقتصادی؛ و سوم، حمله نظامی قاطع. @WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20801" target="_blank">📅 10:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20800">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏تام کاتن در برنامه مارک لوین در فاکس‌نیوز: مردم ایران باید آزادی و سرنوشت خود را پس بگیرند ‏سناتور تام کاتن با تأکید بر حمایت آمریکا از نیروهای آزادی‌خواه گفت مردم ایران نخستین و بزرگ‌ترین قربانیان حاکمان رژیم جمهوری اسلامی هستند و شایسته آینده‌ای بسیار بهترند.…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20800" target="_blank">📅 10:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20799">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏رییس اتاق بازرگانی ایران و چین با تاکید بر لزوم پایان محاصره دریایی بنادر جنوبی ایران گفت : «چه با مذاکره،
چه با خواهش
، چه با تهدید و چه با جنگ باید این محاصره دریایی خاتمه یابد» و افزود: «تبعات محاصره از جنگ هم بیشتر است.»
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20799" target="_blank">📅 10:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20798">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رویترز: تعداد کشتی‌هایی که از تنگه هرمز عبور می‌کنند، به ۶ فروند در روز دوشنبه کاهش یافته است، در حالی که میانگین این تعداد در ۱۰ روز گذشته حدود ۱۱ فروند بوده است. این کاهش در حالی رخ می‌دهد که امیدها برای دستیابی به توافقی بین واشنگتن و تهران رو به کاهش است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20798" target="_blank">📅 10:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20797">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: ما بر اساس سه سناریو با ایران عمل می‌کنیم: اول، نظارت بر وضعیت نامناسب آن؛ دوم، اعمال فشار اقتصادی؛ و سوم، حمله نظامی قاطع.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20797" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20796">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bdb30a06.mp4?token=QpeW1WJ67IT4uEAOR0Y8f1XoOLAh-oI2aBP-4ul4KaxZ5KyQaOTF_Nd7uME2peFDpQU5-_t9kLS2bt0r6M8CWYrGd31mjdmdz1EhLjXgLUJN1ta-xTXkBnmkL25IiBjdkw3_fQa92IbDBPo-J6Bu_J_Rp1ETtkZs5BDyYRtroZLqoLj6ohZ381MJTQamSF3nKFcu8qSyFp6X8FKpi40A1gOTynH9SnWn56aon5ILmAyIeeA93xCBvYiesWT0gv5BhdyBdURhr7AJgV0yoZ5va3km3yF4moHtgKRuUeEG31sKmjqXYAfHly-PYMjp4Rkb8NVZegE8WvOEXLGoi5p61BqUKc1FX7D9lrgUaWNZuCrz0GdLjKIvg45DYloiRHF4Ebs3C59m3cWYRH1qYo38eIRNk79_M3hw1M3DXMVVM-S1eZZ2tJXBTZVbyhF4cVkOyMQl173QoKMyulqoXmM6VLqhrxgsygngVgkXDgtVhwPdA7ZTMTjJzbtoVVepAmZQInpinFFgnMamaY7zztGNEk-JcT1WdOImvGPoYjiHz5Yu_Ni82TzhtiBMcjZzU3cni0rj09d7FqSK3QoUHurzC2blokklxihbPj4FjcJQFxA7YrCdZwD0aR7r6s_q3NKVaPeSpKLRrvXc0KLgZLEqzSIl-uRerHyOi0AUCszsrec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bdb30a06.mp4?token=QpeW1WJ67IT4uEAOR0Y8f1XoOLAh-oI2aBP-4ul4KaxZ5KyQaOTF_Nd7uME2peFDpQU5-_t9kLS2bt0r6M8CWYrGd31mjdmdz1EhLjXgLUJN1ta-xTXkBnmkL25IiBjdkw3_fQa92IbDBPo-J6Bu_J_Rp1ETtkZs5BDyYRtroZLqoLj6ohZ381MJTQamSF3nKFcu8qSyFp6X8FKpi40A1gOTynH9SnWn56aon5ILmAyIeeA93xCBvYiesWT0gv5BhdyBdURhr7AJgV0yoZ5va3km3yF4moHtgKRuUeEG31sKmjqXYAfHly-PYMjp4Rkb8NVZegE8WvOEXLGoi5p61BqUKc1FX7D9lrgUaWNZuCrz0GdLjKIvg45DYloiRHF4Ebs3C59m3cWYRH1qYo38eIRNk79_M3hw1M3DXMVVM-S1eZZ2tJXBTZVbyhF4cVkOyMQl173QoKMyulqoXmM6VLqhrxgsygngVgkXDgtVhwPdA7ZTMTjJzbtoVVepAmZQInpinFFgnMamaY7zztGNEk-JcT1WdOImvGPoYjiHz5Yu_Ni82TzhtiBMcjZzU3cni0rj09d7FqSK3QoUHurzC2blokklxihbPj4FjcJQFxA7YrCdZwD0aR7r6s_q3NKVaPeSpKLRrvXc0KLgZLEqzSIl-uRerHyOi0AUCszsrec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واشنگتن پست:
در پی تهدید به ترور از سوی ایران، دونالد ترامپ هنگام ترک نشست ناتو در آنکارا، ابتدا مقابل دوربین‌ها سوار هواپیمای قدیمی «ایر فورس وان» (بوئینگ ۷۴۷) شد، اما سپس به‌صورت محرمانه به یک فروند هواپیمای ‌کوچکتر
C-32A
منتقل شد. در همین حال،
هواپیمای قدیمی ۷۴۷
به‌عنوان هواپیمای فریب با شناسه «ایر فورس وان» به پرواز ادامه داد و خبرنگاران و حتی برخی کارکنان کاخ سفید تصور می‌کردند ترامپ داخل آن است.
در ویدئویی که از این عملیات منتشر شده، ادعا می‌شود
انتقال ترامپ با استفاده از یک کامیون خدمات فرودگاهی، احتمالاً کامیون حمل پول آرمور(زره ای) ، انجام شده است. این در حالی است که
هواپیمای
ایر فرس وان
جدید ۷۴۷-۸ اهدایی قطر
، هواپیمای رسمی جدید رئیس‌جمهور آمریکا محسوب می‌شود و با آن به آنکارا آماده بود و در این سفر، نخستین مأموریت خارجی را انجام داده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20796" target="_blank">📅 09:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20795">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0m3qlF4GKA_iLUbBWsFj0GObp1qSV0FkL_wkp10wwI6xg2MAw3ugIr-tDTZSZZc1KB21LMfF_uYBvZ33rCx6HeCQOu3tXbXvD_tvbo8pbRty_gpf-Fj25Ax1XrIlbTDyqlMdW9NPirNTu6og-T-IUrgrOgvqxJVtIRoqBrCGh3qdzbeMZAMQr158s_yiFUKwIeUJmeLvt6X1WqpFMgU8oAkfXiVmNcQaEKFt0oxDvbgspYIHGc-T3ZT6Gq4n7cPhMnt48KhYdH4AamUsz1pxcYPe0U4BoFYDLiI6wYdpTdpRlgNRvnuNHzrE15SRlIwj88x7tNah6hiK0HnMPt69A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ آخر هفته را در زمین گلف خود در بدمنستر سپری کرد؛ در حالی که یک سامانه پدافند هوایی کوتاه‌برد
AN/TWQ-1 Avenger SHORAD
نیز در محل مستقر بود.
(سامانه AN/TWQ-1 Avenger SHORAD:
یک سامانه پدافند هوایی کوتاه‌برد آمریکایی است که روی خودروی هاموی نصب می‌شود و مأموریت آن حفاظت از افراد و تأسیسات در برابر تهدیدات ارتفاع پایین است. این سامانه معمولاً به ۸ موشک دوش‌پرتاب
استینگر (FIM-92 Stinger)
، یک تیربار ۱۲.۷ میلی‌متری و سامانه‌های دید حرارتی و هدف‌گیری مجهز است و برای مقابله با پهپادها، بالگردها، هواپیماهای ارتفاع پایین و برخی موشک‌های کروز به‌کار می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20795" target="_blank">📅 02:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20794">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ادعای وال استریت جورنال : مسئولان ارشد دولت و کاخ سفید به ترامپ توصیه کرده‌اند که تشدید تحریم‌های فعلی و اعمال تحریم‌های جدید علیه ایران، ممکن است موثرترین راه برای وادار کردن این رژیم به تسلیم باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20794" target="_blank">📅 02:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20793">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1faa6dd22c.mp4?token=tARqKyFHHIp6nrrHF42A2xU-xujNQkhAjBp16savpy-qMx61NQUcJMhhQdwI97BwtAFWD5Y08IHGQEpDh9xZwWsi7c_jXz_caSRAY9A2zo9ht6j1LNyhvdvRf_R3WlZGlznxReBQ_CxdZWb2_mgxcBnHhn2th0zZ8ogP__y3ae1h1bUCaE_yA5blqxt4ohuxFySCERU0H_nZQPmuAIvGw-E00nd6GM7EjX-qm010AHxT1R0j3C221uWXV02qObkq2NMRSutse2JD3K8ni-728lh2PhoAE74rIayu4CLlhER5hJwnnktUm7p1p0yWJjqv3WTNlcwCFS2hTDDDep4_coAu0tciUtb_9PuFDP8rSoXhfeDLBHEozhkKbm0sOe4mMi4cflYJB15voJwhaY_3nuaCBSRR-Ps8raCGAcUdjfLcv5BJnvChnCY8A0aAcWTwy5SNaUhzgrzCrQY-ysMfGi57WUEK2aSNbza_YxRJAnklnnsjZ9FZ0jMiCxCbnaneB4yBYoHn_F-Gs4gA-zbRc6XQQ3eorkhw8u_WeGZRlPJJol6EdOx__xrMTA48KKMLkYv0o01riLph4BlhIiJA1vLIW3hyjYba55r6QmFz0nxngTvYj15C2kvU-dNeLplbeKtECW8MU80BB86JJnuCvnplf0bN-0O6eZkuTjcj8fY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1faa6dd22c.mp4?token=tARqKyFHHIp6nrrHF42A2xU-xujNQkhAjBp16savpy-qMx61NQUcJMhhQdwI97BwtAFWD5Y08IHGQEpDh9xZwWsi7c_jXz_caSRAY9A2zo9ht6j1LNyhvdvRf_R3WlZGlznxReBQ_CxdZWb2_mgxcBnHhn2th0zZ8ogP__y3ae1h1bUCaE_yA5blqxt4ohuxFySCERU0H_nZQPmuAIvGw-E00nd6GM7EjX-qm010AHxT1R0j3C221uWXV02qObkq2NMRSutse2JD3K8ni-728lh2PhoAE74rIayu4CLlhER5hJwnnktUm7p1p0yWJjqv3WTNlcwCFS2hTDDDep4_coAu0tciUtb_9PuFDP8rSoXhfeDLBHEozhkKbm0sOe4mMi4cflYJB15voJwhaY_3nuaCBSRR-Ps8raCGAcUdjfLcv5BJnvChnCY8A0aAcWTwy5SNaUhzgrzCrQY-ysMfGi57WUEK2aSNbza_YxRJAnklnnsjZ9FZ0jMiCxCbnaneB4yBYoHn_F-Gs4gA-zbRc6XQQ3eorkhw8u_WeGZRlPJJol6EdOx__xrMTA48KKMLkYv0o01riLph4BlhIiJA1vLIW3hyjYba55r6QmFz0nxngTvYj15C2kvU-dNeLplbeKtECW8MU80BB86JJnuCvnplf0bN-0O6eZkuTjcj8fY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تام کاتن در برنامه مارک لوین در فاکس‌نیوز: مردم ایران باید آزادی و سرنوشت خود را پس بگیرند
‏سناتور تام کاتن با تأکید بر حمایت آمریکا از نیروهای آزادی‌خواه گفت مردم ایران نخستین و بزرگ‌ترین قربانیان حاکمان رژیم جمهوری اسلامی هستند و شایسته آینده‌ای بسیار بهترند. او گفت: «همان‌طور که رونالد ریگان در قرن گذشته در برابر کمونیسم شوروی ایستاد، ما نیز باید همواره در کنار نیروها و دوستان آزادی بایستیم؛ چه دولتی طرفدار آمریکا در برابر شورشی ضدآمریکایی باشد و چه مبارزان آزادی‌خواهی که برای رهایی از دیکتاتوری‌های کمونیستی یا اسلامی تلاش می‌کنند. همان‌طور که پرزیدنت ترامپ اوایل امسال بارها گفت، کمک در راه بود و مردم ایران باید آزادی و سرنوشت خود را دوباره به دست بگیرند. اگر مردم ایران به آینده‌ای بهتر دست یابند، آمریکا امن‌تر و جهان نیز امن‌تر و صلح‌آمیزتر خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20793" target="_blank">📅 01:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20792">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTvNGFBfCRO4FTdV-OR3j7Z8piPi4dD2-OudV1VVfO1eNThKFfPn7ObAUzwN0H_jwePdeClcPE3tXieGcyowx0T6FNbf6qHCo0OjGrrQdOYVNjYgRoTcx8cvv7LST9fVd_JbEOZEaqAdZk2epcictQW2gvoZMhOPKp3A7RrrvEK4U5mhvXV_Mh0skfqpEOLfuZMYw7GBASXBAEMENGsCh0dCLjABYz9kdbkXZIId3fBxc91KrdOIB_7NPEguVTjty7b0R8Jc8HdQz-dENFF41Oyh9tIwXTN5f61BoS8_7UT94krHYX7rMSF04mnIF489Xp5McPwWwAXukOUF301NNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۵ نفتکش مرتبط با عربستان، که بیشترشان نفتکش‌های بسیار بزرگ و خالی هستند، در حال حرکت به سمت خلیج فارس هستند.
ترامپ همچنین امشب اعلام کرد که تنگه هرمز کاملاً مین‌روبی شده است. باید ببینیم میتوانند عبور کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20792" target="_blank">📅 01:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20791">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اتاق جنگ با یاشار : کنگره آمریکا در تعطیلات تابستانی قرار گرفت.
سنا از ۸ اوت ۲۰۲۶ تا ۱۴ سپتامبر ۲۰۲۶
عملاً در تعطیلات است و جلسه عادی بعدی آن
۱۴ سپتامبر (۲۳ شهریور)
خواهد بود. مجلس نمایندگان زودتر برمی‌گردد و
۳۱ اوت (۹ شهریور)
رأی‌گیری‌های عادی را از سر می‌گیرد.
حالا اگر آمریکا در این فاصله به ایران حمله کند، تعطیلی کنگره از یک جهت می‌تواند برای دولت ترامپ یک مزیت سیاسی ایجاد کند:
ترامپ همچنان فرمانده کل است و تعطیلی کنگره به‌خودی‌خود مانع دستور حمله نمی‌شود؛ اما نمایندگان و سناتورها برای تصویب قطعنامه، محدود کردن بودجه یا اعمال فشار فوری علیه عملیات نظامی، امکان بسیار کمتری برای اقدام سریع دارند
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20791" target="_blank">📅 00:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20790">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20790" target="_blank">📅 00:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20789">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کامنت جدید برای ترامپ (کارای اداری)
آقای رئیس‌جمهور، فن آخر استاد را اجرا کنید
🎯
https://www.instagram.com/reel/Db30SjjS-Wl/?comment_id=18183518170406206</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20789" target="_blank">📅 00:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20788">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏
رسانه‌های سعودی: اسماعیل قاآنی، فرمانده سپاه قدس، به بغداد سفر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20788" target="_blank">📅 23:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20787">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عراقچی در تماس تلفنی با همتای آلمانی خود: تضمین امنیت تنگه هرمز مستلزم توقف اقدامات تهاجمی آمریکا، به ویژه محاصره است.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20787" target="_blank">📅 23:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20786">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: رئیس‌جمهور بعدی بابت کارهایی که من انجام داده‌ام، اعتبار زیادی دریافت خواهد کرد.
لطفاً یادتان باشد که این من بودم، نه آن‌ها.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20786" target="_blank">📅 23:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20785">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرنگار: آیا پاسخی به نتانیاهو دارید؟
ترامپ: من امروز آن را در تروث منتشر کردم. من یک پاسخ دارم، یک پاسخ خوب. بله، رابطه خیلی خوب است.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20785" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20784">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6383d52564.mp4?token=NZwn0UmDhaq5bX37_p7q2pI3veFixGdxR4Fs26IaHxtm6-fsvZ4KOfNqIBtO_MXepeX3WAKMPT-8Xmca0IvhdT1FklpzhGVZyRA52g0gok0-bfEag-CRnRLl2ZVj1RLerb11PL-a-3yqMfQ77G2jU3hQmB89kgRJr43AaEs9hcVbTYTkGV0BgtXMfFHKOEy3YKss48xCY9CwlWkP3FvUGv8iFncDsTpKC8VA3laMDLRdggLVF0qxI92m4FniiZt8Dd_arpd_G8KPiZ7k_HvvsnLJaL1jgq9w2hWP8D8AO1KmALaHYZkiBD06rZa03YYXUjUVPukWgLXfX36edSxfYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6383d52564.mp4?token=NZwn0UmDhaq5bX37_p7q2pI3veFixGdxR4Fs26IaHxtm6-fsvZ4KOfNqIBtO_MXepeX3WAKMPT-8Xmca0IvhdT1FklpzhGVZyRA52g0gok0-bfEag-CRnRLl2ZVj1RLerb11PL-a-3yqMfQ77G2jU3hQmB89kgRJr43AaEs9hcVbTYTkGV0BgtXMfFHKOEy3YKss48xCY9CwlWkP3FvUGv8iFncDsTpKC8VA3laMDLRdggLVF0qxI92m4FniiZt8Dd_arpd_G8KPiZ7k_HvvsnLJaL1jgq9w2hWP8D8AO1KmALaHYZkiBD06rZa03YYXUjUVPukWgLXfX36edSxfYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایرانی‌ها صدها هزار نفر را کشته‌اند.
حالا دارند تاوانش را می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20784" target="_blank">📅 23:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20783">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ در مورد ایران:
آنها می‌توانند دردسر درست کنند، اما ورشکسته هستند. آنها پولی ندارند.
ایران کاملاً ورشکسته است. آنها حقوق سربازان خود را پرداخت نمی‌کنند.
تورم آنها 309 درصد است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20783" target="_blank">📅 23:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20782">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43e103fdf.mp4?token=d7gEpRK6tjY4e4-8jZAhmKySnAD487Aj6jaUlg9rzkljBB6dcqOIWrJm6uX54K5kjhCGW9W7Bk2CRwuncTUe19DmeSzPMIK5gOn4fOiIIJrZP1JDTyGT1Fjk8TeK-GsoX90jDtzoppQTxucR-ofIFjjQY1YT2jvDmno_fFhU69t3LIXqKrRFNPZjFWx2cWO-IHvqA-s2IygR72cmbKKf1q0vf-1733zkD27fIu1bmX9riLabM2eXEgEkiINSedilZtYG5AINhix4GQZnIPc5e9Eqo0Ev7lhDPdrwrGcGhjBISNpDInAqwbt5U0ckJXlORJdtc1DnNfmMnJytrKEPyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43e103fdf.mp4?token=d7gEpRK6tjY4e4-8jZAhmKySnAD487Aj6jaUlg9rzkljBB6dcqOIWrJm6uX54K5kjhCGW9W7Bk2CRwuncTUe19DmeSzPMIK5gOn4fOiIIJrZP1JDTyGT1Fjk8TeK-GsoX90jDtzoppQTxucR-ofIFjjQY1YT2jvDmno_fFhU69t3LIXqKrRFNPZjFWx2cWO-IHvqA-s2IygR72cmbKKf1q0vf-1733zkD27fIu1bmX9riLabM2eXEgEkiINSedilZtYG5AINhix4GQZnIPc5e9Eqo0Ev7lhDPdrwrGcGhjBISNpDInAqwbt5U0ckJXlORJdtc1DnNfmMnJytrKEPyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: تنگه هرمز کی باز می‌شود؟
ترامپ: الان باز است.
ترامپ در مورد ایران:
همانطور که احتمالاً شنیده‌اید، ما تمام تنگه را مین‌روب کرده‌ایم. شاید نشنیده باشید.
ما ۱۰۰٪ تنگه را کنترل می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20782" target="_blank">📅 23:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20781">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ: اگر قرار باشد خسارتی پرداخت شود، ایران باید آن را بپردازد
ترامپ: تشدید شدید تنش‌ها همچنان یک گزینه است
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20781" target="_blank">📅 23:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20780">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرنگار: شما گفتید این آخرین فرصت ایران است. حالا چی؟
ترامپ: خواهید فهمید.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20780" target="_blank">📅 23:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20779">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ درباره ایران:
هیچ اتفاق بدی در نتیجه اقداماتی که ما انجام می‌دهیم، رخ نخواهد داد. هیچ اتفاق بدی رخ نخواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20779" target="_blank">📅 23:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20778">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIw1ekjzukl7nS6df8X7sVqItXofeolu1XY93L-fcF3MXEAUMH5T5xrhKhHJ2bkgSPob6zd-xZlw8mddLfhoNpUWU-8KgBvuUd8rgfWeE96_c5I9Sp0SM_xFlMX_NHQpJcG4zG2zLWPODvS_pPyfpPFOrky7I8lETYQ7-6jeC2KKD-C9a5yjNSE3MTCevitC3bvOHVqkqP8qlv14L7dTgblLN_y8QiBGHNlpTTYl_vHGYZc0yl3wcEjXFWqEZkZtEObZEMaqtzSNe6l6dplfAHvfhfj95xtoUFemVtCrgFI1BhGqd-GEQnwSFpV90W4cn-WW0FiJuoiHbKkcOQiakg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج ماه گذشته به آن‌ها وارد شده است؛ درگیری‌ای که از آن‌جا آغاز شد که آن‌ها نباید به سلاح هسته‌ای دست پیدا کنند. با این حال، چنین…</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20778" target="_blank">📅 22:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20777">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20777" target="_blank">📅 22:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20776">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJMuBw7Z1lqQ1UHyizvkJCBUPU-3gldOzwb3A-mMNmQEHLD3AIr78zV31gQXlw_hkZ_hCYYVOF2jSSz3VvfQaL7Di5QCCQP5-QZmwDXs9p-zbgv1zNuY68H_tgmDw7cBfDrNo4S6azUdyJWLT5xfxWK-XEkkW7OmMxUBr0_y-eb56KAnEpAdxttGbOq7C5toFVNBhXBIzNV30IoVirM5lChNy8LTBsC42UdY-8cqfoPP57pYb-vuHynmfWGY-zbENbmfORT82Pyf0EQmbFmDxunONgvypREcz7BoW7VKVgBK_lyEBD1pAKvxgbz9js504Qli2hOsQIpXSv7fkbDI1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان KC-46A پگاسوس نیروی هوایی آمریکا از پایگاه‌های مبدأ خود در غرب ایالات متحده به پایگاه هوایی مک‌دیل در فلوریدا، در شرق آمریکا، منتقل شده‌اند؛ جابه‌جایی‌ای که می‌تواند نشانه‌ای از آماده‌سازی برای اعزام قریب‌الوقوع شماری از هواپیماهای پرمصرف (احتمالاً بمب‌افکن‌های بی-۵۲) به انگلستان و سپس خاورمیانه باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20776" target="_blank">📅 22:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20775">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏کانال ۱۳ اسرائیل گزارش داد که این کشور به آمریکا اعلام کرده به هدف قرار دادن نیروهای حماس که در حمله هفتم اکتبر مشارکت داشتند، ادامه خواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20775" target="_blank">📅 22:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20774">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c44f7cd8.mp4?token=QXoLbXHcRXLU-HIy7mzTPbgYvqKbSoxrwShOXAwxtT75IDsInCIJrdxuPJ-6NEmKSgTCWWwefPraUX2jnNVTKTrIL0LKWzmRd96aVKIZFx5avqTIAqv_Rduxq8mlZIFP0njzZ_is-Xniv_4sVka1lSfAvio3hpc3upgtDaDc6ESXkqjGPYvA7K0aCvxrb5ovM2bsPhjBWqmF5Qv_Rg1HSGK7dGJredqWhAPhLXsjNc9CSPg7qI7N9NN52HNEosE-NjAGXmjgC6lumZT795m6iwfkotFnBZ0gucpUyNcnxMkIUCvVTAM-Cu3lStpyAj9VVpz7M03vD6M_hyXcH538nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c44f7cd8.mp4?token=QXoLbXHcRXLU-HIy7mzTPbgYvqKbSoxrwShOXAwxtT75IDsInCIJrdxuPJ-6NEmKSgTCWWwefPraUX2jnNVTKTrIL0LKWzmRd96aVKIZFx5avqTIAqv_Rduxq8mlZIFP0njzZ_is-Xniv_4sVka1lSfAvio3hpc3upgtDaDc6ESXkqjGPYvA7K0aCvxrb5ovM2bsPhjBWqmF5Qv_Rg1HSGK7dGJredqWhAPhLXsjNc9CSPg7qI7N9NN52HNEosE-NjAGXmjgC6lumZT795m6iwfkotFnBZ0gucpUyNcnxMkIUCvVTAM-Cu3lStpyAj9VVpz7M03vD6M_hyXcH538nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده ستاد کل نیروهای دفاعی اسرائیل در کنار فرمانده سنتکام: "ماموریت ما این است که بر واقعیت تأثیر بگذاریم، نه اینکه تسلیم آن شویم."
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20774" target="_blank">📅 21:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20773">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20773" target="_blank">📅 21:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20772">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">جان بولتون : کناره‌گیری از رویارویی‌مان با ایران یک اشتباه است. ایالات متحده ضربات سنگینی به ساختار نظامی رژیم ایران وارد کرده و سال‌ها طول خواهد کشید تا آن را بازسازی کنند. صرفاً به این دلیل که نمی‌دانیم اهداف نهایی‌مان چیست، نباید با دادن یک پیروزی سیاسی به این رژیم، برتری بر تنگه هرمز را به آن ها واگذار کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20772" target="_blank">📅 20:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20771">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/544e884864.mp4?token=ZLNrXwwOQ5m4dhbfEIMnzumzlu48T6XQdnHXgMMAtcsram160WAUckduLQ2xZ7I1J5VQHX1NcTXeNXXbcXQGJiILET3qSDUKFhDJKwdCemLfNs8dM9CH8NuRMEuZ8ysqT2X1sHpcSneq1NE-fGpKLPdO_XVmXWEwdMHppfdNxyys2km-4jI1qv-VBA4l5xSZyzahMyQJoisCdALq9DcHe6-nLbQIJzy2yyhlMx_VhN4aQHeMsJCzt9z584AjnvnJINQ367eoYKj8vnB7iYbLyAiKkht_W96FbkbtjCoS4LX9a26wyPOCyk50fEQphOT2hUFHWpdOpMYZrUj7-2z4Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/544e884864.mp4?token=ZLNrXwwOQ5m4dhbfEIMnzumzlu48T6XQdnHXgMMAtcsram160WAUckduLQ2xZ7I1J5VQHX1NcTXeNXXbcXQGJiILET3qSDUKFhDJKwdCemLfNs8dM9CH8NuRMEuZ8ysqT2X1sHpcSneq1NE-fGpKLPdO_XVmXWEwdMHppfdNxyys2km-4jI1qv-VBA4l5xSZyzahMyQJoisCdALq9DcHe6-nLbQIJzy2yyhlMx_VhN4aQHeMsJCzt9z584AjnvnJINQ367eoYKj8vnB7iYbLyAiKkht_W96FbkbtjCoS4LX9a26wyPOCyk50fEQphOT2hUFHWpdOpMYZrUj7-2z4Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه مشترک چارلستون رسماً به پایگاه مشترک لیندسی گراهام تغییر نام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20771" target="_blank">📅 20:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20770">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjyI7FSLT_lU3_0QVfaPUfu45OKnmya2dO0kFAlnLjeej_YPdGdwWOFNUNLhz3ZBrFOAm73K9Tl4fSLyvyBAkvPYUn11Wn06kJNKpMZAVZadl06vv1L_aL-2_4ooJhFhGUl4ymveKXdP0g-sXlqJr8-6rTMzGpLFJ1Ug41yutORCMzwCjDma4fk9G4j503m9p7bHeMRwGz9w0UhsXMBU_AFPE_n9j5HfEqfSVHiOE14ueVvz9BNiuxpZQFIsCZq2kiLWdU64Ywa0c2wLBdFg_PHL5Kz2fITzh_5F3SLfz_V3Op08Tb2yWPjshZGE5Rk93g2JOID6hrVYP950cE2Hyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج ماه گذشته به آن‌ها وارد شده است؛ درگیری‌ای که از آن‌جا آغاز شد که آن‌ها نباید به سلاح هسته‌ای دست پیدا کنند. با این حال، چنین موضوعی هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود! اما این ایده جالبی است، زیرا حالا من نیز از ایران درخواست غرامت می‌کنم؛ بابت تمام افرادی که با بمب‌های کنار جاده‌ای و درگیری‌های متعدد، که به آن‌ها شهرت دارد، کشته یا به‌شدت مجروح کرده است؛ اقداماتی که در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد. این شامل خانواده‌های کشته‌شدگان ناوشکن یو‌اس‌اس کول و هزاران نفر دیگر که در نبردها جان باختند نیز می‌شود. افزون بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته کشته است نیز غرامت پرداخت شود؛ چه برسد به ۵۲ هزار نفری که در پنج ماه گذشته جان خود را از دست داده‌اند. به نمایندگان خود دستور داده‌ام که این موضوع را با قاطعیت در همه مذاکرات آینده مطرح کنند. از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20770" target="_blank">📅 20:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20769">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مرندی ، مشاور تیم مذاکره کننده : جمهوری اسلامی آگاه است که نیروهای دولت ترامپ در خاورمیانه در حال آماده‌سازی برای یک حمله برق‌آسا هستند؛ حمله‌ای که ممکن است با همراهی نیروهای اسرائیلی انجام شود.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20769" target="_blank">📅 19:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20768">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">با حکم مجتبی خامنه ‌إی آی، علی عبداللهی فرمانده ستاد کل، احمد وحیدی به سرلشکری فرمانده کل سپاه، کیومرث حیدری جانشین رئیس ستاد کل، ایزدی جانشین فرماندهی سپاه، عظمایی فرمانده نیرو دریایی سپاه و طائب رئیس بسیج شد
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20768" target="_blank">📅 19:33 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
