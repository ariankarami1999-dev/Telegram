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
<img src="https://cdn1.telesco.pe/file/L3hOSxpkBLU-WbFGbSBOtRKtNMCOzh0VHRtBD7MQQphIag2y9bPEiXf4wvMrV_S1z0FecnkCPypQIkFYxg3CXSc03CtZn2YtSET60bP_YqVxmY5HwgTNrVe5noIzcQvrHIV6FTl0V0uAJ0l4uVpWWim0qBu38ilhe8G60EJE-WqpJzOGhI5EB1t_LDa0oMgYW6EaerDHFH3ApCsJvtkRwMQXiPNkCOo4PXT5JC7qROCEN39DM-7MHclRX4PicTjtaZ87a_ilbEr6x9Ob6LM61Li_IbbPUs3qLnJEN_yS_WlmC1oKiRbrOh6eWOQVxmyEoebSvPTVHCbME2dpFbNASg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.36M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 09:56:35</div>
<hr>

<div class="tg-post" id="msg-76314">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
وحید جان ساعت۰۳:۳۲ صداهایی میاد از تو دریا
ما چند کیلومتر از اسکله سپاه طاهرویی فاصله داریم
سلام وحید انفجار های پی در پی از یک ربع پیش تو دریای شهرستان سیریک
صدا انفجار شدید اینجا شرق سیریک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/76314" target="_blank">📅 03:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76308">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tRbtIV0XvNx_isj93ZelxUgXv08NxHJIe7QhY7cX29CUY-vAPc8jPXJT0cJUh9JWWP4HVo1dluYsQ4LTCUUzZY6g6sjY6ERfBNO0sHAEHnCmn8uROl8l_SOUPiNdpI0dupJUlDav2lKk7_voVY0umt3U9Df677DVSLUyWEUYtx_RTNaJvNE8tGF-wyd6dYxMMJ73mERs__wNE01y1yDehkK67WJwLuGyLBaZXIaTv3dRLcz2EqIBBxtNLUwAFFYmfxgGUQWRTWAAnXZVvktzFDhycP4YvNEn0NB0uDrf02Uz9f4DTttTiBNS7kGkAtSEWjR0h84pkHju92t2IAkYpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d60822ba5.mp4?token=VHJhaoyYs3fCfklrGO-88bJfWGpEE5WyjQcOhx3RYJs1gNk_dsrbIpb5cijdjqmzA6_Yd0bXeXJ2z8s1cMKpO8sxErpiCSL4uGjtdi0BEcjJNfX1wMI0qoMvsuMjpU8Qt2Hlhxuu3rCzImeXh45BvNSNM9VyaHLhJYqU3hZ9OEjUEUfbqfbErwSCHaXQ88dz0ZN-mTdVvpMk-YRdzmPqKwrNVwjD0abLHRFAVnYOl1qFRjIqkyedM2ctzn1fAjX8SI6WcCmfAuxQR1KADQG4Y_jmh3UiGc25OZDWcBZwAt0dyVIl_5CsU8S5-7DMA7f_h3GUi55X0sIAzkdwTn2swQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d60822ba5.mp4?token=VHJhaoyYs3fCfklrGO-88bJfWGpEE5WyjQcOhx3RYJs1gNk_dsrbIpb5cijdjqmzA6_Yd0bXeXJ2z8s1cMKpO8sxErpiCSL4uGjtdi0BEcjJNfX1wMI0qoMvsuMjpU8Qt2Hlhxuu3rCzImeXh45BvNSNM9VyaHLhJYqU3hZ9OEjUEUfbqfbErwSCHaXQ88dz0ZN-mTdVvpMk-YRdzmPqKwrNVwjD0abLHRFAVnYOl1qFRjIqkyedM2ctzn1fAjX8SI6WcCmfAuxQR1KADQG4Y_jmh3UiGc25OZDWcBZwAt0dyVIl_5CsU8S5-7DMA7f_h3GUi55X0sIAzkdwTn2swQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف، عراقچی، پس حون رهبرم چی؟!
برخی رسانه‌های داخل ایران تصاویری از تجمع برخی طرفداران حکومت در شامگاه شنبه را منتشر کرده‌اند که در مخالفت با امضای توافق احتمالی با آمریکا علیه برخی مقام‌های جمهوری اسلامی شعار می‌دهند.
در یکی از این تجمعات که در میدان ابن سینا در تهران برپا شده، تجمع‌کنندگان علیه وزیر خارجه و رئیس مجلس شورای اسلامی شعارهایی مانند «عراقچی حیا کن مملکت رو رها کن» و «قالیباف، عراقچی / پس خون رهبرم چی؟» سر داده‌اند.
برخی رسانه‌های نزدیک به اصلاح‌طلبان این افراد را «نزدیکان به جبهه پایداری» معرفی کرده‌اند.
خبرگزاری دانشجو نیز عکس‌هایی از یک تجمع در مشهد منتشر کرده که در آن‌ها پلاکاردهایی در مخالفت با توافق و همچنین انتقاد تند از مذاکره‌کنندگان دیده می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76308" target="_blank">📅 23:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76307">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبرگزاری فارس، رسانه وابسته به سپاه پاسداران:
اصرار عجیب ترامپ بر امضای تفاهم با ایران در روز یکشنبه و آزمونی برای تیم مذاکره‌کننده
🔹
ساعاتی پیش، دونالد ترامپ، رئیس‌جمهور آمریکا، بار دیگر تأکید کرد که «یادداشت تفاهم» با ایران روز یکشنبه امضا خواهد شد. این در حالی است که مسئولان مذاکره‌کننده ایرانی صراحتاً اعلام کرده بودند که تفاهم هنوز نهایی نشده و یکشنبه قطعاً انجام نمی‌شود.
🔹
نکته قابل تأمل، همزمانی یکشنبه با چهاردهم ژوئن، روز تولد ترامپ است. برخی ناظران احتمال می‌دهند او با این اصرار در پی آن است که از این مناسبت بهره‌برداری نمادین کرده و آن را به یک رویداد تبلیغاتی برای خود تبدیل کند.
🔹
اما با توجه به مواضع شفاف مقامات ایرانی مبنی بر نهایی نبودن توافق، به نظر می‌رسد مسئولان مذاکره‌کننده کشورمان متوجه این لایه‌های پنهان هستند و اجازه چنین مانور رسانه‌ای و تشریفاتی‌ای را نخواهند داد. از این زاویه، سرنوشت امضای یکشنبه نه فقط یک آزمون فنی برای محتوای تفاهم، بلکه آزمونی برای صداقت و ایستادگی مسئولان ایرانی در برابر فشارهای نمایشی نیز خواهد بود.
@
VahidOOnLine
وب‌سایت خبری اکسیوس به نقل از منابع آگاه نوشت که دلیل امضای ویدیویی توافق آمریکا و جمهوری اسلامی، «ملاحظات اجرایی و لجستیکی» و عدم امکان سفر جی‌دی‌ونس به پاکستان است.
اکسیوس نوشت که یکی از دلایل اصلی امضای ویدیویی توافق آمریکا و جمهوری اسلامی این است که ونس در صورت سفر برای امضای توافق، نمی‌توانست قبل از عزیمت ترامپ برای شرکت در اجلاس گروه ۷ در فرانسه در صبح دوشنبه به آمریکا بازگردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76307" target="_blank">📅 22:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76306">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cpTUyQUkM9yl-jVaT9KUeV_jSXkGoSQ2z6UJFKVamp9NT7o8xx0ChWURbegMc6K1XX2IXT73ZDbSoJ4fmShdC2HI8pWZNoyJqLCChdjOvVJSrGjAXtBiNoOH7_dngtCWS6zkmagHRufISK2V02OlWIyi5RThjBHWnji0UlBXcZ-kQonw5kBxr8ngm3YhHcZeaHzU_fxPvqnKWOUfJ9yQFEOLehjgZDfAnm49ewgk--bAwRQrVzbgFCJLRe-TEiEN__vNW83__oiLP8Hw7puf1cnKHW-x74DkEd-rCTPiSLcnc1DA1XDIYzwAQva7CVgLElSeX0Q77vJ_nMn5R6E_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: قرار است توافق فردا امضا و بلافاصله تنگه هرمز باز شود
پست ترامپ، ترجمه ماشین:
توافق باراک حسین اوباما با ایران، یعنی برجام، مسیری آسان، زیبا و هموار به سوی سلاح هسته‌ای بود؛ سلاحی که ایران شش سال پیش می‌توانست به آن دست یابد و مدت‌ها پیش از حالا از آن استفاده می‌کرد. توافق من با ایران درست نقطه مقابل آن است:
دیوارِ جلوگیری از دستیابی به سلاح هسته‌ای!
در واقع، آن‌ها دیگر سلاح هسته‌ای نمی‌خواهند و چنین سلاحی هم نخواهند داشت؛ نه از طریق خرید، نه توسعه، و نه هیچ شکل دیگری از تهیه و تدارک.
قرار است این توافق فردا امضا شود و بلافاصله پس از امضا، تنگه هرمز به روی همه باز خواهد بود.
رابطه ما با ایران بسیار متفاوت و بهتر از رابطه‌ای است که دولت‌های پیشین داشته‌اند. برخلاف صدها میلیارد دلار پرداختی اوباما به آن‌ها، از جمله ۱.۷ میلیارد دلار پول نقدِ سبز و سرد،
هیچ پولی رد و بدل نخواهد شد.
در زمان مناسب، وقتی همه چیز آرام باشد، ما وارد خواهیم شد و «غبار هسته‌ای» را که در اعماق کوه‌های قدرتمندِ گرانیتیِ فرورفته زیر آفتاب دفن شده است ــ به لطف بمب‌افکن‌های زیبای B-2 ما و خلبانان درخشانشان ــ به دست خواهیم آورد و آن را
رقیق‌سازی و نابود خواهیم کرد؛ چه در ایران و چه در ایالات متحده.
ما مشتاق همکاری با ایران و سراسر خاورمیانه در آینده‌ای طولانی هستیم. امیدوارم این روند همگی سریع، آسان و روان پیش برود.
اگر چنین نشود، ما گزینه نهایی را در اختیار داریم؛ گزینه‌ای که امیدوارم هرگز دوباره به کار گرفته نشود!
از توجه شما به این موضوع سپاسگزارم!!!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76306" target="_blank">📅 20:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76305">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شبکه الجزیره به نقل از سخنگوی وزارت خارجه پاکستان گزارش داد که مراسم «امضای الکترونیکی» توافق میان آمریکا و جمهوری اسلامی یکشنبه ۲۴ خرداد برگزار خواهد کرد. به گفته او، پاکستان میزبان این مراسم خواهد بود و مراسم از طریق «ارتباط ویدیویی و آنلاین» برگزار می‌شود.
او جزئیات بیشتری درباره شرکت‌کنندگان یا مفاد این توافق ارائه نکرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76305" target="_blank">📅 19:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76303">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YMlITBsu-rgWqaPgNkHHvuv6UCJvcUYnqwVrV2IUzCvaQ3Z-pIwJZ3ghqI1iyliIStPMU7w566pbXnCDoGMSIKGbrzLwidpndrWRTw96Nl1wm7NBtYGT4-bj3xTWzKJPDDm-muH-OZrvHTKUmWZH6jCB8EfGmDxD9-lQZXIZdWWh4Ud8FKdp7ImvKhbIt2O61vMkcEnlaJJIHbVocoPOTP804idXTsl9B_xQeHFttnkCGAxSR2aaFG9q0mMZpzYFjLsUH69SIYHkdXv6kLd5TtUJQmpsTEPMxn1wxTtf9gsTWDtxDUC9cbiZFYF-eusHzw5wCqxaMJYt69eazt9Dmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oeosC3lj4IBnFz8Xdl2K7atYBGWy_6MG8ELV-KnfVsaOouTWUWZyWCdHrUF7Pb00TLrA7iyYikoLV_UbjDWLwVZ5NLH9mA3qwV4JGwXczKeYA726AwlBi1Wa1pfwj-iV2NiNpQQfsiqU05FLaoDHWuNo2LU59cH2E3O9iDPjBWBpRz6FWeOfC32ObE4efztfCvfNpqTFwpSgJiIHYjAAtX0jfP9lGhFaFAUcDppCxnaXpAbIiOyPgmL8G7PqUPt2q701ay6InlsdOAcMyBp747oikQf1h9e-yXbaoeDacwcucHVzTJ1xS9sh5pAB5_6tLH_1HuXnDQ5WbR8qtXjU0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام ارشد دولت آمریکا به رویترز گفت که دونالد ترامپ، رییس‌جمهوری آمریکا، در نشست گروه هفت با رهبران امارات متحده عربی و قطر و برخی دیگر از رهبران خاورمیانه دیدار خواهد کرد.
به گفته این مقام، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در دیدارهای ترامپ با رهبران خاورمیانه هفت حضور نخواهد داشت.
نشست رهبران هفت اقتصاد پیشرفته جهان، موسوم به «گروه هفت» ۲۵ تا ۲۷ خرداد در شهر اویان فرانسه برگزار خواهد شد.
@
VahidOOnLine
اسماعیل بقائی، سخنگوی وزارت خارجه جمهوری اسلامی، در نشست خبری گفت احتمال نهایی شدن یادداشت تفاهم میان تهران و واشینگتن در «روزهای آتی» بالا است.
او در پاسخ به پرسشی درباره احتمال سفر هیات مذاکره‌کننده جمهوری اسلامی به ژنو یا اسلام‌آباد در دو روز آینده برای نهایی کردن یادداشت تفاهم، گفت: «درباره زمان دقیق امضا باید منتظر بمانیم.»
بقائی افزود: «برنامه‌ای برای سفر به ژنو یا جایی دیگر ظرف یکی دو روز آینده نداریم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76303" target="_blank">📅 19:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76300">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FoTj0CQ84Ztmv6CpQ6PEsKDr04KH-jyPIXuZimBLF1s-erVht8VQU-Smi64dRYBWP9SAnjDo3iohAg3bUBxkB5IVp9z27V3vTZ0QdjEt6et689m0k-Mdox_OA8hYXNOM6ascY5kXxBYQQ7BCplu_-qiWVkRVRHNJAM3VErpTQHqLKWaYYKkqXl_WqlsFGK5a6qHP-r6OHqRc-YuqTgi4DSNXb939FL-lBJ3agm9DucR2i6b35o1UegKF9uinN30jr0i8qX3ODpdoBmCVj_e-juIWfVNsjroM88f-Bl7HAwq7jqYu5CKZPKh3MWk1iUL9aOvsR-emQej0Yith0b3rUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uxcZAfDvk3WQaHg__cow8-S5qHeW1234k8RE9iRIZsFP6pXThbwkE-a_3cYAqaHmC1TgmcNtkgJwHryCPkfaU2ycDuXWMo-zc4123uvBlV7LZj4q4NRGGnj3YmtOvuMBJ_gFt9_2OiYcHM0ReOwOJ5Y-wTH9Oof-USOG3fkCN_8NLqzVi9FI_lP7OWbaySLunU2h6Ztn5Xcwpo94Ix5Kg-NIfcsJKX63PPYu8pSUTmW5UBMlm4rDmGjkg0hpOz8YGieDcIgT7wVoNyTC1EsNgnAsGCpiMFdN8pPkJwRXgmnjuckp5cLodHUAfWPuW94QEFFDznVG4dnRxSBlEHg4Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نخست‌وزیر پاکستان: تفاهم‌نامه ایران و آمریکا احتمالا تا ۲۴ ساعت آینده نهایی می‌شود
نخست‌وزیر پاکستان می‌گوید ایران و آمریکا بیش از هر زمانی به توافق صلح نزدیک‌تر شده‌اند.
شهباز شریف دقایقی پیش در پستی در شبکه ایکس نوشت که انتظار می‌رود تفاهم‌نامه ایران و آمریکا ظرف ۲۴ ساعت آینده نهایی شود.
او گفت که پاکستان در حال فراهم کردن تدارکات لازم برای «امضای الکترونیکی» این سند است و پس از آن هم «گفت‌و‌گوهای فنی» آغاز خواهد شد.
@
VahidHeadline
دونالد ترامپ، رییس‌جمهوری آمریکا، شنبه ۲۳ خرداد، در شبکه اجتماعی تروت سوشال، پستی از شهباز شریف، نخست‌وزیر پاکستان، را بازنشر کرد که در آن به احتمال دستیابی تهران و واشینگتن به یک تفاهم طی ۲۴ ساعت آینده اشاره شده بود.
ترامپ این اظهارات را بدون توضیح اضافی در تروت سوشال بازنشر کرد.
@
VahidOOnLine
اسماعیل بقایی، سخنگوی وزارت امور خارجه، روز شنبه ۲۳ خرداد با تشریح آخرین وضعیت مذاکرات اعلام کرد: «یادداشت تفاهم اسلام‌آباد که در حال پیگیری است، به طور مشخص بر خاتمه جنگ تمرکز دارد و در این مرحله تصمیم بر این شده که هیچ بحثی در مورد موضوع هسته‌ای صورت نگیرد.»
بقایی درباره گمانه‌زنی‌های مربوط به زمان امضای این سند گفت: «درباره زمان دقیق امضای تفاهم‌نامه باید منتظر بمانیم؛ اگرچه این رویداد فردا نخواهد بود، اما احتمال اینکه ظرف روزهای آتی رقم بخورد کاملا منتفی نیست.»
بقایی ایالات متحده را به «تزلزل و بی‌ثباتی در اظهارنظرها» متهم کرد و گفت: «به دلیل تزلزل و عدم ثبات طرف مقابل در اظهارنظرها، باید در هرگونه موضع‌گیری درباره این روند محتاط باشیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76300" target="_blank">📅 18:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76299">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUONKIZEURe4N_vAzCLwcR5mEH7n-HWG-xBCwDeASPQALfWHpGPhk4fpXqtf5vfekTQzb9ksMbidas2c3l-LsiW77-mggJI1FICpWf7CLRbgbLXsPbzuat-5QH-XRfuz0OtAFpWipmw40jQiPF-t-HOTuiKvbPJpHK4gsty8-8YI5LVbV50TFSIOwAI9E7QaDvG1Y38f2ENe6vR63-6QI6fZunCXCD_SCyaQVHgJVNzBq3xUl_uGI2TWOFynnJxUUtUg85WOsq8RokvFe05WMPSbfJdvd6HXBBrvJI354QdeqFK_i9Tpxdp2S-pkO3lRjQoHltloh6LEsWzlHmYL9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز پژوهش‌های مجلس در تازه‌ترین گزارش خود درباره وضعیت شبکه برق کشور هشدار داده است که با وجود افزایش نسبی ظرفیت تولید، ناترازی برق در تابستان ۱۴۰۵ همچنان ادامه خواهد داشت و احتمال بروز خاموشی، به‌ویژه در ساعات شب، وجود دارد.
بر اساس برآورد دفتر مطالعات انرژی، صنعت و معدن این مرکز، در سناریوی واقع‌بینانه میزان کسری برق در اوج مصرف تابستان به حدود ۱۳ هزار و ۶۰۰ مگاوات خواهد رسید. در این برآورد، توان تأمین هم‌زمان شبکه حدود ۶۸ هزار و ۴۰۰ مگاوات و میزان تقاضا بیش از ۸۱ هزار مگاوات پیش‌بینی شده است.
@
VahidHeadline
پیام دریافتی:
امروز روستاهای خشکبیجار  از ساعت ۱۶:۴۵ حدود ۱ ساعت و ۱۵ دقیقه برق قطع شد. بعد از قطع برق تماس گرفتم با ۱۲۱ که گفتن قطعی ۲ ساعته کنترل مصرف هست که امروز صبح از رشت شروع شده و عصر به شهرستانهاش رسیده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/76299" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76298">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CXrjpGDSvQYo9Wpsj4Fy2RIeDkaOw6I6h0gOFQH_otdJ1-Qs_n09hC16LghpxHtlqV4nbzAZ0F9o0BdIQtMF1_0QkiL0EvtvKK77QE5h2F-MuKVZISgG8W4vQqtLL2Dhsd4U2Y5fowb-ytZmw9LooEwKVd75JnAPinZkTJgLHpIuQEwZuJ4egZ5t-tCg9xkWfX5Yds-JUhtCqTBp0h2stK4f6rRRhSZouYbyXM4K8lEr6y7B-75y1hgVpvQg0FCPfS_YzO28Wx0gYvLLm6gUJ7ziGw9jSM4VmNtdLVob5ANoCvR6aYNjQsr19WCVeaKkQYfVldJ1spkDHdbHiXyPbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه تلویزیونی سی‌ان‌ان در گزارشی اختصاصی که روز شنبه، ۲۳ خردادماه، منتشر شد می‌گوید که حکومت ایران در هفته‌های اخیر بر تلاش خود برای سخت‌تر کردن راه‌های دسترسی به اورانیوم غنی‌شده مدفون در سایت‌های بمباران‌شده‌اش افزوده است.
این گزارش به نقل از پنج منبع «آشنا با اطلاعات و ارزیابی‌های دولت ایالات متحده» نوشته شده، اما به نام و منصب آنها اشاره نکرده است.
سی‌ان‌ان در گزارش خود نوشته است که جمهوری اسلامی در هفته‌های اخیر این تونل‌های زیرزمینی را منفجر کرده و در ورودی آنها مین کار گذاشته است تا دسترسی به آنها را هر چه بیشتر دشوار سازد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76298" target="_blank">📅 17:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76297">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmCaDNh8znAxuHtqScpPqrve70O78Wzhj_r8e9tt76gwc0zukprGOweZ20aPasLb6oHljfd0qE62n3IE0U5mDHrZu9kPthZF0_Wi9g7n9KNvLi9BDTv2Vrp41cR_iQ0-Y5DRpCVkjJHDsTrQbKZffUaOggF6YiRp3B8iRA5r4AtK61tJjUrA2K4D8FjcdIBDZ0YnOc1j6ixPi2SayCsev8tiUww5bz9ssqdq4U3jTK7ZpGTH0HuHd9YX3Ii1c3zso3cmutFyk53NDOZml5vWEWWxinRNqZhjD8UgzPZOsfBrAOJXvUac3TUH9P9oJtnSpvQPAJSdJ-jNIi6tPwcfng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها و مقام‌های ایرانی روز شنبه خبر دادند که خدمات چند بانک ایرانی به شکل همزمان دچار مشکل شده و این اختلال تا بعدازظهر همچنان ادامه دارد.
خبرگزاری ایسنا اعلام کرد که «بانک‌های ملی، تجارت، صادرات و پاسارگاد» از جمله بانک‌هایی بودند که همراه‌بانک و دستگاه‌های خودپرداز آنها مختل شده است.
خبرگزاری فارس در این‌باره نوشت بانک «توسعه صادرات» نیز اختلال مشابهی دارد و افزود که «برخی منابع از احتمال وقوع حمله سایبری خبر داده‌اند، اما تاکنون هیچ مقام رسمی این موضوع را تأیید یا رد نکرده است».
ساعتی بعد علیرضا قیطاسی، دبیر شورای هماهنگی بانک‌های دولتی در گفت‌وگو با صداوسیما بدون اشاره به جزئیات درباره دلایل این اتفاق گفت: «رفع اختلال از خدمات بانک‌های ملی، صادرات، تجارت و توسعه صادرات در دست انجام است.»
حملات به شبکه بانکی ایران در سال‌های اخیر سابقه دارد و بارها اطلاعات مشتریان بانک‌های مختلف ایران هدف رخنهٔ سایبری قرار گرفته و در فضای مجازی و اینترنت خرید و فروش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/76297" target="_blank">📅 17:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76296">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b7_Fc1tRcoNoW8BBbXb0a03tUu5VNlspw0Xq2mUysNJNYrweEgVsnKc_dMuq8Y7Lxgh_1vsHO5q4zMPGDy9OO8BTj3l-X-pcOpv9ujxLKGA5xJU3p0ABPcoZPoGTEguMoxnTzPjHWFvSfZ_8kmjuqie_vn0cFb84CjpczWswuiCNTd4ew3UoqToQetxARBGUN6jIW3Sqxy9z1JqcP-8rNcdM8a2tl1sV6vkJwpPgwgj43OGm8DdbyB6bi_fc-smnuVdpXa84_mfjY27OmNghEFhQJl63aedYVbFk-4UTrN10lT_scSJ3EyrAJR7X6mFMN46eYBHcJupqpZDNh2oSgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش تازه «پروژه شفافیت فناوری» نشان می‌دهد یوتیوب میزبان ۸۴ کانال مرتبط با افراد و نهادهایی بوده که در فهرست تحریم‌های آمریکا قرار دارند؛ بخشی از آن‌ها همچنان از طریق نمایش تبلیغات در این پلتفرم درآمدزایی می‌کرده‌اند.
بر اساس این گزارش، ۵۶ کانال به اشخاص و اتباع تحریم‌شده در فهرست SDN و ۲۸ کانال دیگر به نهادهای دولتی و رسمی مرتبط بوده‌اند. در میان نمونه‌های شناسایی‌شده، نام‌هایی از نهادها و رسانه‌ها و همچنین برخی کسب‌وکارها و افراد قرار دارد.
پس از انتشار نتایج این گزارش، شرکت گوگل ۶۳ کانال را ظرف چند ساعت حذف کرده است. گوگل اعلام کرده که به قوانین تحریمی آمریکا پایبند است و اقدامات لازم برای اجرای مقررات را انجام می‌دهد.
در فهرست منتشر شده از کانال‌های شناسایی‌شده، نام‌هایی مانند نو‌بیتکس، و‌الکس، بیت‌پین، رمزینکس، گروه بهمن، ماهان ایر، فارس‌نیوز، پرس‌تی‌وی، ایرنا، بانک پاسارگاد، دانشگاه المصطفی و همچنین برخی چهره‌ها و کانال‌های سیاسی و رسانه‌ای دیده می‌شود. مانند علی‌اکبر ولایتی، امیرحسین ثابتی، بابک زنجانی و مسعود پزشکیان.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/76296" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76295">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rrQTaUkLoSro7NjVNaJyigbAYrYRHWym4FXAhkMbp5Uban8pQ4sFlLS1H6LweHTzKB2MLRVeK2AzHvRfMtcrAqXtXUGz0L4NJ3pi1UYG2P2p6AKjdrHO7KlRebHyLniAGqHN7O7caJYPqETFUcH2HMsP5VJRPJjsbbEOue5Q-QgbZnrrZH7OSuc6ShYSfk0ak6EFQmkKFGGOwajjLYrJcXCl3Vgk1pnUy0FSLZA7CGKBCA7m8zksJLD0WgTv49nyXPi5VjV8kWFhfaizizYnwY9dII_Amadf10KIE60gBkCtwaHr4eBesj4J63rx_DcCrEVH3uKOL73c06NRgnXmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور کنترل صادرات با استناد به نگرانی‌‌های مرتبط با امنیت ملی، دسترسی «اتباع خارجی» را، چه در داخل و چه خارج از آمریکا، ممنوع کرده است.
شرکت آنتروپیک، سازنده دستیار هوش مصنوعی «کلود» (Claude)، جمعه ۲۲ خرداد اعلام کرد به دنبال دریافت یک دستور کنترل صادرات از دولت آمریکا، دسترسی به دو مدل پیشرفته خود، «فِیبل ۵» (Fable 5) و «مایتوس ۵» (Mythos 5)، را «برای همه کاربران» قطع کرده است.
این دستور با استناد به «اختیارات امنیت ملی» صادر شده و دسترسی هر «تبعه خارجی» را، چه داخل و چه خارج از خاک آمریکا و حتی کارکنان خارجی‌تبار خود آنتروپیک، ممنوع می‌کند.
آنتروپیک گفت این دستور را ساعت ۵:۲۱ بعدازظهر به وقت شرق آمریکا دریافت کرده است. از آنجا که شرکت نمی‌تواند به‌صورت لحظه‌ای کاربران خارجی را از دیگران جدا کند، ناچار شده هر دو مدل را برای تمام مشتریان غیرفعال کند.
دسترسی به سایر مدل‌های این شرکت، از جمله Opus، بدون تغییر باقی مانده است.
بنا بر گزارش اکسیوس و وال‌استریت ژورنال، نامه این دستور را هاوارد لاتنیک، وزیر بازرگانی آمریکا، خطاب به داریو آمودی، مدیرعامل آنتروپیک، فرستاده و با همکاری اداره صنعت و امنیت این وزارتخانه، تنظیم شده است.
متن نامه جزییات دقیق نگرانی امنیتی را مشخص نکرده، اما به گفته یک مقام دولتی، واشینگتن پس از آن که شرکتی دیگر مدعی شد توانسته سازوکارهای ایمنی مایتوس را دور بزند («جیلبریک» کند)، نگران خطرهای امنیت ملی شده است.
همان مقام افزود دولت پیش‌تر کوشیده بود آنتروپیک را به تعویق عرضه این مدل‌ها متقاعد کند و پس از ناکامی، نامه «کنترل صادرات» را صادر کرد.
آنتروپیک با این تصمیم مخالفت کرده، اما گفته است از آن تبعیت می‌کند.
به گفته این شرکت، روش افشاشده یک «جیلبریک محدود» است؛ در عمل یعنی درخواست از مدل برای خواندن یک کد و رفع ایرادهای آن؛ آسیب‌پذیری‌هایی جزیی و از پیش‌شناخته‌شده که مدل‌های عمومی دیگر، از جمله GPT-5.5 شرکت OpenAI، نیز قادر به یافتنشان هستند.
آنتروپیک تاکید کرد فِیبل ۵ با تدابیر حفاظتی‌ای به‌مراتب قوی‌تر از هر مدل پیشین عرضه شده و پیش از انتشار، هزاران ساعت با همکاری دولت آمریکا، موسسه ایمنی هوش مصنوعی بریتانیا و گروه‌های مستقل آزموده شده است.
این شرکت ممانعت از دسترسی برای یک مدل تجاری در دسترس صدها میلیون کاربر را به‌خاطر یک آسیب‌پذیری محدود «نامتناسب» خواند و هشدار داد اگر چنین معیاری به کل صنعت تعمیم یابد، عملا عرضه هر مدل پیشرفته‌ای متوقف خواهد شد.
این دستور، تنها سه روز پس از رونمایی فِیبل ۵ و مایتوس ۵ صادر شد. مدل‌هایی که آنتروپیک آن‌ها را قدرتمندترین سامانه‌های خود معرفی کرده بود. هر دو بر یک بنیان فنی ساخته شده‌اند، اما تنها فِیبل ۵ با محدودیت‌های سخت‌گیرانه، به‌ویژه در حوزه‌های امنیت سایبری و زیست‌شناسی، برای عموم منتشر شد؛ مایتوس ۵ بدون این محدودیت‌ها و تنها در اختیار شماری از شرکای مورد اعتماد، از جمله شرکت‌های امنیت سایبری و زیرساخت، قرار گرفت.
این دو ادامه «مایتوس پریویو» هستند. مدلی که بهار امسال با توانایی‌های پیشرفته سایبری توجه وال‌استریت و مقام‌های دولتی را جلب کرد و در چارچوب طرحی به نام «گلَس‌وینگ» میان گروهی محدود توزیع شد.
اما اهمیت این ماجرا فراتر از یک مدل و یک شرکت است: این نخستین بار است که واشینگتن از اهرم کنترل صادرات در مورد یک مدل تجاری پیشرفته استفاده می‌کند. این وضعیت نشان می‌دهد سرنوشت یک مدل را می‌توان نه با تصمیم سازنده، بلکه با دستور دولت رقم زد.
چارچوب «ملیت‌محور» این محدودیت نیز کاربران و شرکت‌های غیرآمریکایی را مستقیم هدف می‌گیرد.
آنتروپیک می‌گوید توقف عرضه‌های ناایمن توسط دولت را می‌پذیرد، اما در چارچوب فرایندی قانونی، شفاف و مبتنی بر واقعیت‌های فنی. اقدامی که به گفته این شرکت با چنین معیارهایی نخوانده است.
آنتروپیک این ماجرا را «سوءتفاهم» خوانده و گفته است طی ۲۴ ساعت آینده جزییات فنی بیشتری منتشر می‌کند و در تلاش برای بازگرداندن دسترسی است، هرچند زمان مشخصی برای آن اعلام نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/76295" target="_blank">📅 17:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76293">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/an_UAM1nWHVevBi1cxDofmIkwMhpuNd7DfQcXyLs4sUgmATcFHEIHRHs5UTQub5eC9JN_iua_O0ddclPA7V7ae1XvT3skZ9gmxXfef57YDXjfbPSofyEj-IU-KH9PvshF0IbFxbCuUI0a6rMdEpj0Nlz7EW9JpwXBjVSskf7u4jKwqSorlF_hymQGfj-JK95VjAHm0p9rdBZk8wYKmNjteeUUnFKRivJN0kuYe19t2MgMJeL5d3Thg-EczanpRVdA8LZqVKPhhSZ4pF9g-jNJYUV3lNTV1JxFzKDGas1KZZG5KcOziZMnD5eqG_RgW1VW9LLksVoEG4o9lvFr0eQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JnTYM6kg1UeoJ_JJyKHYJtJeLIpKy_-2kUG10GzABnSrSDws6KTYepmnlvM1B9i9sHh3nDbN8jDk1pGfzF1wttX2qq5K71PONriPp18P8h3_tLIJpo1GdbuogePNnE0mJ7N2bzd1NIHKX7RZ1vk-XjFEL5-F_reeIpRbr-IDlypYeOEjkOKJvJEB8kivEerN0XTnSd-LJZOY5IxgWR28i-M6ayTphBQP_WRzwaSKiaC6QMc9B-lYyEWuMPc-slb-zl6RvF2eV1_NbJd4_q2nTH62f8zL2B7KASeGlkl9jTJeMoNePDtiNY7PXauxWPMxSEAWez8Nj2Bm94G9BVWbUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری رسمی لبنان روز شنبه ۲۳ خرداد خبر داد که ساعتی پس از صدور هشدار به مردم ساکن جنوب لبنان، ارتش اسرائیل به چند نقطه در این منطقه حمله هوایی کرده است.
ارتش اسرائیل روز شنبه صبح به ساکنان ۲۰ نقطه در جنوب لبنان از جمله شهر نبطیه هشدار داد که باید محل سکونت خود را ترک کرده و به شمال رود لیتانی بروند.
ارتش اسرائیل اعلام کرد این هشدار در پی نقض آتش‌بس از سوی حزب‌الله لبنان، صادر شده است
.
حال خبرگزاری ملی لبنان می‌گوید که هواپیماهای جنگنده اسرائیل چند نقطه از جمله دو روستای سجود و ریحان را در نزدیکی شهر نبطیه بمباران کرده‌اند.
اسرائیل در ماه گذشته میلادی تمام مناطق در جنوب رود لیتانی را «منطقه جنگی» اعلام کرد و از آن زمان این نقاط را بمباران کرده است.
اوایل ماه مارس یعنی تنها یکی دو هفته پس از حمله مشترک آمریکا و اسرائیل به خاک ایران،‌ گروه حزب‌الله در حمایت از جمهوری اسلامی به اسرائیل حمله کرد، حمله‌ای که بلافاصله پاسخ ارتش اسرائیل را به دنبال داشت.
درگیری این دو هنوز ادامه دارد و حتی پس از برقراری آتش‌بس حدود دو ماه پیش، هم ادامه یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/76293" target="_blank">📅 17:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76292">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVA7QMqWoXxbyV5m9Iuiw-xRqZFymi7NxbPhLM5azP9Ock5c18FilE2Ay86z2ZJc9ry4THcVikuJZu5VFyNPy1F_r3UKA4eKk0KJF1kvefdtkGwcfhO6WzEEAUPVElfv05-3qai9BNpG0ruvl9udXJ5FuVXLupIq-uZPa81G4lB8E-O3_TzHHGnxp3sMrLV-YAD6KVX4C21mVKwrRz97oX229eD3cEE_1r4tWcL8u-Os9J1R2xLZBRhZt4nevy3E06bvnWLrlRC79ptLmyIn75SPsEB2sOF3pSJv2mxcQzhPz45ZUQ3SX76jRTQkUV8Hh7SBB-itnIbSMhbbqN9G9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر حفظ و نشر آثار علی خامنه‌ای با انتشار اطلاعیه شماره ۳ ستاد بزرگداشت «عروج خونین» او، جزئیات مراسم وداع، تشییع و تدفین دومین رهبر جمهوری اسلامی را اعلام کرد؛ مراسمی که قرار است حدود ۱۲۹ روز پس از کشته شدن او در ۹ اسفند ۱۴۰۴ برگزار شود.
بر اساس این اطلاعیه، مراسم وداع با پیکر علی خامنه‌ای و اعضای خانواده‌اش روزهای ۱۳ و ۱۴ تیرماه در مصلای تهران برگزار خواهد شد. تشییع پیکر او روز ۱۵ تیر در تهران، ۱۶ تیر در قم و در نهایت ۱۸ تیرماه، همزمان با شب شهادت چهارمین پیشوای شیعیان، در مشهد برگزار می‌شود و پیکر او در حرم هشتمین پیشوای شیعیان به خاک سپرده خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76292" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76290">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq6t9-WWfP7uZ8YkmuT7WXrYLFiS_2ER8Rjaf7lv2k_DPSJClTVO3ryLhrC0EBO42Hp-rTzdm9mnDosAVwYPdUohQwAqIR7FNUXjt_-n9ba8BQKzhWjUe54HyuHFq5bw44WSkTl9lwsy_tgfft7P35QaS0RQbUh5C446ZlefxY9aBZAq-9eFWD9iDEyEuyK-gtYhVodR81Nlfk6c9RiIMrRixoTUfAE558qnoPOJ6IORMEc6ed8It2kYpSvLbBY3jJy7MFOLXXYgjzzxRMfRSKlA3LdMt3CgC-7N7qhTMrU_gCZQg39m6OggERj1J4es22k8yb5rAkW7TbCPkpOinQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سید آرمان موسوی» ۲۹ ساله، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ در محله مسکن شهر کرمانشاه هدف شلیک مستقیم قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله جنگی به ناحیه قلب او اصابت کرده بود و در اثر شدت جراحات جان باخت. پیکر سید آرمان موسوی روز شنبه ۲۰ دی‌ماه در کرمانشاه به خاک سپرده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76290" target="_blank">📅 17:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76289">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzJFi6wt0Po5IOY8WK3v7204nqzGbMnmkYDFKRI0FrJfDfaXwQO8NBIVjZph7WhsuySfDNL3wZepicqX9KJuzdJHNHib-Qv5Jda3iGIGoEjMfu1DOujnMCbNFbniDI2_LXjw4OLwuuO-5kLHV1t35bTCh3RHfsvo8kZfknyX_KJxHdGAjGaWLLRwIYcpB63EhyEhLjTqzilRBRBPslSzUIBvjkksiMDNkPeYlcU-PBQ0uDjzBAG7qHkh4xXaeCYNGeQhbVf2NP0UyEazXocB9vl9DYqnfw5jDYvR-wNA_7sRc19f2dMp2JA9Xl1lLFWlJsisoXNsxqRfcmSjnfQmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، در گفتگوی با «فاکس‌نیوز» اعلام کرد که با توجه به روند پیشرفت مذاکرات، انتظار می‌رود توافق صلح با ایران «احتمالا تا پایان همین هفته یا روز دوشنبه نهایی شود».
بسنت با اشاره به اینکه تصمیمات دونالد ترامپ برای جلوگیری از دستیابی تهران به سلاح هسته‌ای، هزینه‌ها و فشارهای کوتاه‌مدتی را به بازار سوخت و اقتصاد خانواده‌های آمریکایی وارد کرد، افزود: «ما درک می‌کنیم که در ماه‌های اخیر شرایط سختی سپری شد و افزایش بهای انرژی بخش زیادی از رشد دستمزدها را بلعید، اما ما در حال عبور از این وضعیت بحرانی هستیم.»
وزیر خزانه‌داری آمریکا با تاکید بر اینکه زیرساخت‌های اقتصادی کشور در حال حاضر بسیار قدرتمند عمل می‌کنند و بازار انرژی به خوبی تامین شده است، خاطرنشان کرد که با حل‌وفصل این مناقشه و مهار تورم، بهای جهانی نفت حدود ۲۵ تا ۳۰ درصد و قیمت بنزین در بازار داخلی بیش از ۱۰ درصد از اوج خود کاهش یافته و روند نزولی قیمت‌ها و کاهش هزینه‌های زندگی مردم با قدرت ادامه خواهد یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76289" target="_blank">📅 06:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76288">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD0BQBV3Zdj9cCQAYccdbO8WPlL24uKxWfxAoWILfX9X8ettb9Mzmrar6BAAlwnk9U1-I1IYg_o9cqqVKORfuXmg16KyEEwOIfY_8iDyaAaCivoqjZQ3cFXJrThaEcXnVTnB2ebhkVQY1ocfN3RYLvigseMZWgJyTs85PVp19rfV0D_PtAqKzIhJGq2Zd2Wc0Yh56bmhjyEMsfU07yNLA9q4mZPr4WgGSZpvNY8Ndd-PqryIVpEVAxm57Qr4QhB8-p2hMZKaK9KCyoKQoWV2Uc_S4zkjM7HgsSp8S2SHpHcHEYdcKqxkBUNUTCOVgsfCclLKvufeYSmV-xtmXQsmNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
فرماندهی مرکزی ارتش آمریکا (سنتکام) اعلام کرد که ایران چند پهپاد انتحاری را با هدف حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورده است.
سنتکام در شبکه ایکس نوشت که نیروهای آمریکایی در ساعات اخیر همه این پهپادها را سرنگون کرده‌اند و تردد کشتی‌ها در تنگه هرمز بدون اختلال ادامه دارد.
در این پیام آمده است: «ایران چند پهپاد انتحاری را در تلاش برای هدف قرار دادن کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورد. نیروهای آمریکایی در ساعات اخیر همه آنها را سرنگون کرده‌اند و جریان تردد در تنگه بدون مانع ادامه دارد. این گذرگاه مهم تجارت بین‌المللی همچنان برای عبور و مرور باز است.»
پیش‌تر نیز یک منبع آگاه به رویترز گفته بود نیروهای آمریکایی چند پهپاد ایرانی را که به سمت تنگه هرمز در حرکت بودند سرنگون کرده‌اند. این منبع گفته بود پهپادها تهدیدی برای کشتیرانی تجاری به شمار می‌رفتند.
این رویداد در حالی است که تهران و واشنگتن همزمان از پیشرفت در مذاکرات برای دستیابی به توافقی جهت پایان دادن به درگیری‌ها سخن می‌گویند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76288" target="_blank">📅 06:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76287">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MXXtAQKuirOIBWXZz2lhL4_GAEVP7PukaVZGeuhIeW50LBuDfIrsf4dSwlctjwA-wAaaYUwVk85IEmvjSvQbypv8VFApPfW2JH_Jh4-8plzZApnkqk_G1_W6gJ7e5XREaop12iTIoImKVZ_8M3GidV4HKAuaRDMho-F5mBMO3rjSWeDfyiwjJaQZVWj6uMLZEDqcVzWD1IH505-i_pdc8NCFhhl1nMmkaiSASkz6CQoUNUueLpmQJUXj3bWGBHnDwpkepjOGbYTFwvTegcRSvkaYwGnC7HfbwUzi5lkwE3U9fbu2yk2S9inS-Y-HJ2NFBgEO0vAZqF2Ab4DRcNHiyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه امارات متحده عربی گزارش‌های منتشرشده در برخی رسانه‌های بین‌المللی درباره انتقال یا آزادسازی منابع مالی برای ایران را قاطعانه تکذیب کرد.
این وزارتخانه در بیانیه‌ای در شبکه اجتماعی ایکس اعلام کرد که ادعاهای مطرح‌شده درباره انتقال مبالغ مالی از امارات به جمهوری اسلامی ایران، از جمله گزارش‌هایی درباره انتقال ۳ میلیارد دلار، «نادرست» است و هیچ مبنای واقعی ندارد.
پیشتر
رویترز به نقل از چهار منبع آگاه گزارش داد که امارات متحده عربی با آزادسازی میلیاردها دلار برای ایران موافقت کرده و بخشی از این منابع مالی نیز در اختیار تهران قرار گرفته است.
اما وزارت خارجه امارات تاکید کرد که هیچ‌گونه دارایی یا منابع مالی ایران از طریق این کشور آزاد یا منتقل نشده است.
@
VahidOnline
بیانیه امارات، ترجمه ماشین:
امارات متحده عربی گزارش‌هایی را که از سوی برخی رسانه‌های بین‌المللی منتشر شده و مدعی انتقال پول از امارات به جمهوری اسلامی ایران هستند، از جمله ادعاهایی درباره مبلغ ۳ میلیارد دلار، قاطعانه تکذیب کرده است.
وزارت امور خارجه در بیانیه‌ای تأکید کرد که این ادعاها کاملاً نادرست و بی‌اساس هستند و تصریح کرد که هیچ‌گونه دارایی مسدودشده ایران از طریق امارات آزاد، منتقل یا تسهیل نشده است.
این وزارتخانه همچنین از رسانه‌ها خواست دقت را رعایت کنند، به منابع رسمی اتکا کنند و از انتشار یا بازنشر اطلاعات تأییدنشده و ادعاهای بی‌اساس خودداری کنند.
mofauae
درباره این خبر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76287" target="_blank">📅 01:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76285">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kglp2GooS9Pjg1SjMlTFKSZhmfhWfx88JxRb3BK9Oq_zf_2L1SSySOLrMOSVM3HCi27R3inthBMZS-4uu7bsQo8jT5n2SgVMGCo5NMoKO93StU1KSqgDTpah7JCReN_WeCA6pWGgcIJLoSZe0NPcWTcfCDK3cKCWuGWDH-sedus0mBeHajrgrnCdlws3CgfzGvJ3GhlJRwBiePyG6q3NN_emTrYVYuotZzN0KLTUr4-ftnoUy23HvzpfAg3MB3LC3rwg9RvIkSmbkB_PUg_fjoZHgSsc49S6IcWlbS2ODCb8fTXq-GiOpM20pjPiiIZcRCguUsu5_NBlXT7UhSQjvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xay0_wZJ_olPcEOX9fL65EpPrMqDptAlFI7zVS-FH_W0L5SlU1mJUC_la0PJL4pvw6v6vI7s7ChwqrBaNf3zZTRDXPN3XUr5_TQ7VGtiR1dqyVRx0OFhv6JzNZKvXIG7zmCQyYDdyoGLV-krDAvReKvfC0KP27U8F0tYfaAxZhMsDFoCjt4H8V48VTguymeJdGJoU8rqHhGjuD3R5ndcnj5mEFqlrRzhYZL9JQ9ECKlqdwrbNsyTsPRn9zBgNyKqvLoNYj_rR3ArMYKHko9U2i11DXXECzaKZlckY89oukdRvjQPzQYBnq0WHGZMTgYMVzLdHCxdv3zDopUu0LacoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مالک شریعتی نیاسر، دیگر عضو مجلس شورای اسلامی نوشته:
خب وقتی در باز بشه و ببینن که می‌فهمن مویوم...
malekshariati
این طور برداشت شده که داره میگه قالیباف پشت همه تصمیماتی است که به اسم مجتبی اعلام میشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76285" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76284">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l3rixVvel_Q9ha32qTwriNmRmYdFfrUWkROOTbdRc2E_4oG1JzDKuQPzlLdtrAKykHvBIvdY02-UZ0oE-awWvnMjz2dsuFKwqrWSMBFfYnRl4Et2rppK9dOrOOkNTv-kt9H3LXUPpkTEgbStGooHhO2sMKBHy_daf7zgg1lCxHLoNsf6MTOePmzoSrGP_lfCBHLY1czyYvi-yJMvI-wNaPh0KN5sS6_fQeRQXeLEkFdTgXrcFIMqcGpEkkxET2vE-Hu58n32USWc2eCVYafzLKNlP_zrDcQotJj4RCMOrzHkFKu5Uow7IcRGUNTH3lpfuOgHULNsg4cXP1IdWhoy7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم:
استانداری هرمزگان: صدای انفجار در حوالی بندر سیریک ناشی از شلیک هشدار در تنگه هرمز است
خبرگزاری فارس:
شلیک هشدار به کشتی‌های متخلف در تنگۀ هرمز
دقایقی پیش مردم در قشم، جاسک و سیریک در استان هرمزگان شنیدن صدایی شبیه انفجار گزارش کردند؛ گزارشی از اصابت در این نقاط مخابره نشده است.
به گزارش خبرگزاری فارس از بندرعباس، منابع محلی از شنیده شدن صدای انفجار در سه نقطه از هرمزگان خبر می‌دهند.
دقایقی پیش اهالی مسن قشم، مناطقی از سیریک و همینطور جاسک از شنیده شدن صدای انفجارهایی خبر می‌دهند.
بررسی‌های خبرنگار فارس از منابع آگاه حاکی است صداهای شنیده شده مربوط به انجام شلیک هشدار به کشتی‌های متخلف در محدوده تنگه هرمز است.
منابع استانی نیز وقوع انفجار بر اثر اصابت در این ۳ نقطه را رد می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76284" target="_blank">📅 00:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76283">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/usv99qUwz8KIH39YUF7Dt7ET3z7h-N5lkvj-zzBK4aqptw8hWRYEfdLI9qY5yNXmM0Ksu02nhhG5g1BHUxZmK4IWClzBrR_Cf41XeHxnPbwFK8u-Vlnq_SJTk-DbTHmIOaavt7KASIGs6ZjcUYk7ae6h5LMmjVJHnFtlIMVR3LaUkZydl0OjWB5FmHPoAARQeC2LSFi4s4WU_gipioHqvL-w_58YqkOc_l7P1XuteYlQpbmmrQYMAgoX0iubQsHJSK98oVv9L_uNXb9JQUB2udeKTz306ZF6XS5Bkh80smZZzHgLwvcxtX-YkxNp_Syc-kXKpaAoLiDtaY2qujY0rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، درباره تفاهم با آمریکا به صداوسیما گفت: «احتمالا در چند روز آینده تفاهم‌نامه میان ما و آمریکا امضا خواهد شد.»
او افزود: «امضای یادداشت تفاهم بعد از گذشتن از آخرین مراحل مذاکرات به صورت دیجیتالی و از راه دور انجام می‌شود که اعلام خواهد شد.»
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، شامگاه جمعه در یک برنامه زنده تلویزیونی اعلام کرد هنوز توافقی با آمریکا امضا نشده و مدعی شد که پرونده هسته‌ای ایران به مرحله دوم و نهایی این توافق موکول شده است.
او در گفت‌وگو با تلویزیون حکومتی ایران گفت توافق احتمالی با ایالات متحده شامل دو مرحله است و «موضوع هسته‌ای را به مرحله دوم انتقال دادیم».
این در حالی است که ساعتی قبل یک مقام ارشد آمریکایی به خبرنگاران گفت بر اساس توافق، قرار است اورانیوم غنی‌شده ایران در خاک این کشور نابود شود و سپس به خارج از ایران منتقل شود.
با این حال وزیر خارجه جمهوری اسلامی با اشاره به اینکه نتیجه مذاکرات یک «یادداشت ۱۴ ماده‌ای» است اعلام کرد مفاد آن بعد از نهایی شدن اعلام می‌شود.
وزیر خارجه ایران در گفت‌وگوی خود خبر داد که طبق تصمیم جمهوری اسلامی، «آینده تنگه هرمز و اداره آن مثل گذشته نخواهد بود‌» و ادعا کرد که ایران و عمان بیانیه مشترکی در مورد اداره این آبراه منتشر خواهند کرد.
او در ادامه اذعان کرد که طبق قوانین بین‌الملل گرفتن عوارض از کشتی‌ها در تنگه هرمز امکان‌پذیر نیست و افزود: «اما هزینه خدمات دریافت خواهد شد و این در مذاکرات تثبیت خواهد شد.»
عراقچی اعلام کرد طبق توافق، محاصره دریایی ایالات متحده علیه بنادر ایرانی به‌طور کامل رفع خواهد شد و دارایی‌های بلوکه‌شدهٔ ایران آزاد خواهد شد.
مقام‌های آمریکایی آزاد شدن این دارایی‌ها را به دفعات رد کرده‌اند. جی‌دی ونس، معاون رئیس‌جمهور آمریکا ساعاتی پیش تصریح کرد بعد از امضای توافق، هیچ‌گونه منابع مالی در اختیار ایران قرار نخواهد گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76283" target="_blank">📅 23:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76282">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QDCzZWMAWvrfcpEoNWdPHjRVIK3mWETvAwV49mAh0F190Bp9EP9972AGdcfKU0k9Lf9dxBjrzKeBe3VaoZPVmo8eC4kibJSaqcRLWXqSPu0nUjE3YduNV_kgdS0oXht1_MH3S4XWO3JbgyrKelOnsRwhUjdoZdgbkgidxSe7ZrWS7dLilDawzjTq2WmQGOi_X6WuckvMQT2mb-bwo7-fc5WGuiKb7Et1oqSwhIr1Vf9c5-hmQwU6zNUZNQlnOpz0Roq_Nk-PlNPHJ9vlba2EZXfq_s-Fw-0e5ytL7D2SsKrIOsG7A0VlRAQG6MTgKVzf9tReCbBOEADUMN9LO9OXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف، ترجمه ماشین:
تعهداتی که داده می‌شوند باید عملی شوند؛ نه اما و اگری، نه عذر و بهانه‌ای. برای توافق نهاییِ پیشِ رو، راه دیگری وجود ندارد.
هرچه بکاری، همان را درو می‌کنی.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76282" target="_blank">📅 22:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76281">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ipp-xR5sPfs0jwnNqcInI96PUzZNtyrvR1-umLxc75vWw_a7Rbt9-49KpCQoa3np7nBdZyPqxGFaFm_ZOY5ZfejKTFlzyMnOlHR2TArt2s5uTT8reJox_TSFC0kNU3JkflIDTcajhVBkrCMbN2b4LtAXsWvylXP5dUMjrMbgQHNjmweUD2Z0IHtQm_hEKeWsLfIP3NJlvvtsMUyLr0FcJR4pJjjSFQ-Db_6ZKgDYSXKG6dmLmDxC8xItQjsQHWSI2JWjnTTehBtcqVNk-Qg9GbJeQbll7eaPkVQJ-tOV70Sbt0hokL_Q9iKrjaK210sPdY4K_nb5YjFy_Ccp_UrEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار منبع آگاه به رویترز اعلام کردند که امارات متحده عربی با آزادسازی میلیاردها دلار برای حکومت ایران موافقت کرده است.
رویترز نوشت که این اقدام نشان‌دهنده تغییر تاکتیکی ابوظبی پس از هفته‌ها حملات حکومت ایران به این کشور ثروتمند عربی خلیج فارس در جریان جنگ آمریکا و اسرائیل با جمهوری اسلامی است.
دو منبع منطقه‌ای به رویترز گفتند که امارات با آزادسازی مجموعا ۱۰ میلیارد دلار موافقت کرده است که
بیش از ۳ میلیارد دلار آن تاکنون پرداخت شده است.
دو منبع دیگر که از این توافق آگاهی دارند، مجموع مبالغ مورد نظر را ۲۰ میلیارد دلار اعلام کردند و افزودند که این اقدام در ازای توقف حملات حکومت ایران به امارات متحده عربی مورد توافق قرار گرفته است.
یکی از این منابع نیز گفت که نخستین بخش به ارزش ۳ میلیارد دلار تاکنون در اختیار حکومت ایران قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76281" target="_blank">📅 22:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76280">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DVWL-ykYlQCp-6jxt0C_Rv-iebAEzJXxhv1NKWuS1yn0079Eh_aeHcBMZvIeTkeoxPbVT5M3p-TpG1ySZ602FyMf8iba9HWofHMUms9BrCuzwyMchIeZr9Y4Xk0gR9_Ah_3-i__r5E_ffqN_fGQaD-WkDQ-amqxZefODQ4m0I33H4dkFAtQVLybo_qSA0H6QpG0SLgO9YKnVLjzxuf4MyXw6AzXMvtCVdubmpUP-mROk86t04dH4Mp1ZrueQUNpbh-fNxtHLS6gciOG3nWDdG7ke2-DnTGTZk6EJ77TtCuiONiqcI4-vic0UBddYSf7hBlZqlieWu_3AxvVv9jikCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس در انتقاد از
توییت عراقچی
نوشته:
عراقچی نه‌تنها مستقیماً ادعای ترامپ درباره «جعلی بودن» مفاد منتشرشده را رد نکرد، بلکه با درخواست از رسانه‌ها برای پرهیز از گمانه‌زنی، عملاً فضایی ایجاد کرد که می‌توان آن را تأیید غیرمستقیم نادرست بودن برخی اخبار تلقی کرد.
آیا موضع‌گیری او نوعی عقب‌نشینی یا هماهنگی با روایت ترامپ است؟ در شرایطی که ترامپ مدعی عذرخواهی خصوصی ایران شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76280" target="_blank">📅 21:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76279">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lm0Hrz23yllt-dENoWPecDjriayWwVZPBcztqOLe_lT6gAiUSrQB-jLwISMakCbUP0eBxhBCS6PJTtYVqqo-VZUjJtST8asDUBjzgr6ufg0aO7JsEda_KdzgT3MTJmXN2rT0sy89eZG_2PKSAZbwXZ1_uINbQ8-lgZ7p0TALCZ8-UrZSnmxCiO1MZomejYdqMPbx3o68cb06_qz0GXeJJPZdCZRdlJ3yJKQKItgQj_vEjNCduVybwj7-VHJNBtpK2rQA9yew5KmgrS0v2u1FYwe-8n-JBmTMPFzvEDEKTZXgd76Sq0CCxlkXpG1VUiMoRzE2ox9jBwWar5yb-Y2zkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی روز جمعه در گفت‌وگو با خبرنگاران با اشاره به این که واشنگتن انتظار دارد توافق با ایران در روزهای آینده امضا شود، گفت یکی از مفاد آن نابودی و خروج ذخایر اورانیوم غنی‌شده ایران است.
این مقام آمریکایی که به شرط ناشناس ماندن صحبت می‌کرد، اظهار داشت: «تیم مذاکره‌کننده ما را در موقعیت بسیار خوبی قرار داده است، اما باید ببینیم چه پیش می‌آید. هنوز کاملاً به خط پایان نرسیده‌ایم، ولی بسیار به آن نزدیک هستیم.»
او گفت که مفاد مورد توافق، اهداف اصلی دونالد ترامپ، رئیس‌جمهور آمریکا، را محقق می‌کند و «در پایان، وضعیت را در جایگاهی بسیار بسیار مطلوب قرار می‌دهد.»
این مقام افزود که مفاد آنچه «یادداشت تفاهم» نامیده می‌شود، شامل بازگشایی تنگه هرمز و لغو محاصره آمریکا علیه بنادر ایران است.
به گفته او، ذخایر اورانیوم با غنای بالای ایران نیز در محل نابود شده و سپس از ایران خارج خواهد شد.
این مقام افزود که مفاد توافق همچنین شامل یک رژیم بازرسی است تا اطمینان حاصل شود که اجرای آن در بلندمدت قابل راستی‌آزمایی و الزام‌آور خواهد بود.
@
VahidHeadline
پست‌های خبرنگار نیوزنیشن در کاخ سفید،
ترجمه ماشین:
🚨
اکنون یک مقام ارشد دولت ترامپ جزئیات بیشتری درباره توافق پیشنهادی با ایران ارائه می‌کند.
آن‌ها انتظار دارند این توافق طی «چند روز آینده» امضا شود.
صددرصد قطعی نیست، اما احتمالاً ۸۰ تا ۸۵ درصد احتمال دارد که طی چند روز آینده امضا شود.
این توافق «اهداف اصلی»‌ای را که رئیس‌جمهور برای این مأموریت تعیین کرده بود محقق می‌کند.
نخست، تنگه را بازگشایی می‌کند و محاصره را برمی‌دارد.
🔻
برچیدن برنامه هسته‌ای ایران.
دریافت مواد غنی‌شده توسط آمریکا: هم در محل نابود می‌شود و هم از کشور خارج می‌شود.
ایرانی‌ها دیگر خشونت در منطقه را تأمین مالی نخواهند کرد.
یک نظام بازرسی که اطمینان دهد این یک تعهد بلندمدت و قابل اجرای بلندمدت است.
🔻
پرسش درباره «حجم دارایی‌هایی که در صورت پایبندی ایران آزاد خواهد شد».
به گفته مقام ارشد دولت: وقتی ایرانی‌ها «به تعهدات خود عمل کنند، می‌توانند در ازای این عملکرد، امتیازاتی دریافت کنند.»
🔻
پرسش دوم: چه چیزی تغییر کرده؟ چه چیزی باعث شده این توافق نسبت به قبل ملموس‌تر باشد؟
-«ما به مرحله‌ای رسیده‌ایم که متن را به جایی رسانده‌ایم که از آن احساس خوبی داریم.»
-«ما متن یک یادداشت تفاهم را داریم که فکر می‌کنیم هر دو طرف نسبت به آن احساس خوبی دارند.»
-«ما احساس می‌کنیم کنترل ایرانی‌ها بر تنگه هرمز تضعیف شده است.»
🔻
مقام ارشد دولت: «چه تضمینی داریم که ایرانی‌ها به سهم خود از توافق پایبند بمانند؟ ما هیچ امتیازی نمی‌دهیم مگر اینکه آن‌ها به سهم خود از توافق پایبند بمانند.»
این مقام ارشد دولت درباره یادداشت تفاهم با ایران می‌گوید: «متن را به نقطه‌ای رسانده‌ایم که هر دو طرف آن را می‌پسندیم.»
به گفته مقام ارشد دولت، اگر آن‌ها بتوانند به آن پایبند بمانند، می‌توانند ظرف «چند روز آینده» به توافق برسند.
مذاکرات فنی ۶۰ روز طول خواهد کشید.
آیا رهبر عالی ایران این توافق را، به شکلی که شما شرح دادید، تأیید کرده است؟
مقام ارشد دولت می‌گوید: «افراد در طرف غیرنظامی و نظامی... شهادت داده‌اند/اطمینان داده‌اند که رهبر عالی از جایگاه فعلی آن‌ها در مذاکرات رضایت دارد.»
KellieMeyerNews
مقام ارشد دولت به من می‌گوید که در ۲۴ ساعت گذشته، همه از ونس گرفته تا ویتکاف و کوشنر و ترامپ، به‌همراه هگست، روبیو، وایلز و رتکلیف، در مذاکرات مربوط به ایران دخیل بوده‌اند.
KellieMeyerNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76279" target="_blank">📅 21:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76277">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W3ufXYLUdCk9Ha8eB6EyZXR99kdYk0ROe20pdTrahjIdbRnCMsJvEEz4J_KKE02bpRcN85gYfzF9sXFJ1CcSv2xxrquVxo07k3_1uX7G3v_dDYsq0K-U6WWmcCob_6dPHFEnphSO8p-A92Y3_7qlppdkzGCbky55Hl9rfb3KqXcfOdzR9NgGnXMv8IW9BT8ytqC0UNtIKPB15JiUJhjyXKXEXEG9WR9baHuxTgqj006Ab6Y3Ru_fGict9OFGAcrb-EfJejx1AkaKcbv2fwRlx_HwQEkUCi1_oP6wtVp0Vyh3rZ4KJSWTFfgE10erKIMGmne6ojrCfiD0hamaEVNLag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FDfjGJEyAC9rF7MlZGvySCWn_ieejG8jn6afwoR7jd6XIQWx00G4cpFEzlUw0KKBJ8V_dtWKz2CJwPbfN9tiV7P1tcNjHmfoOvzOk3T7uJxxWiI-fsQ34tTMR95to6eKRmxTVIOULhg7ys6yP-9yDRXt2zJu5bpQG6Z9VWLIB-vVNDStogdWfcdiqlttlMJrXH-sYBpOiBjkHDDNTRQpj6q1YbPaDX6bytTlFABT24ah1rDCfm_w7gq94CyTIpwvXUWDF6uaE1wJ_9nnTs2XlACiOdIkyZXyB1_tGcp7CCtTa8iHOoCbGjey5vMYKjS3dmpp-TepaX9QyPi8VBdtNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یسرائیل کاتز، وزیر امور خارجه اسرائیل، روز جمعه ۲۲ خرداد، با انتشار پیامی در شبکه اجتماعی ایکس اعلام کرد که هرچند رئیس‌جمهوری آمریکا بر اساس منافع واشنگتن و هدف مشترک با تل‌آویو، یعنی جلوگیری از دستیابی ایران به سلاح هسته‌ای، به سمت یک توافق حرکت می‌کند، اما اسرائیل انتظارات فراتری دارد. کاتز تاکید کرد: «از رئیس‌جمهوری آمریکا انتظار داریم این اصل و شروط دیگر در حوزه موشکی و گروه‌های نیابتی را حفظ کند».
او با اشاره به اینکه ضربات سنگین مشترک، توانمندی‌های ایران را سال‌ها به عقب رانده است، افزود: «اسرائیل باید تضمین کند که در آینده نیز توانایی اقدام مستقل برای جلوگیری از هسته‌ای شدن ایران را دارد؛ به همین منظور، من و بنیامین نتانیاهو به ارتش دستور آمادگی لازم را داده‌ایم.»
وزیر خارجه اسرائیل همچنین به عنوان درس اصلی از وقایع ۷ اکتبر تصریح کرد که این کشور به هیچ وجه از مناطق امنیتی در لبنان، سوریه و غزه عقب‌نشینی نخواهد کرد و ارتش به دفاع از مرزها در برابر تهدیدات جهادی از بلندی‌های حرمون تا عمق غزه ادامه می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76277" target="_blank">📅 21:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76275">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iBg3oR6N1YKzNJU3KdHN3QWmP7a43B9paIUUsgGHhBJGJGaaT6M9NuGPJacyK2Hq2qcU9LdvGgtc4zI13DTnDP-khXP1CtpNIjtHXb0VhpZwU5yJzTCF9g5hKjCsshoYsAiGOeXHq4BhkA7Ia1joihtQ55KXSnvjamXadn5VhilLchA3ZJqO4IawAepaOC2cJNOjvTVwCuNisCLpWey7gRm_NpA5zf04FqxRzYh6Gg443oi5y1_yUUCCXQTHhTYZP-Z_yMGPRJdR4U3Nmy6p4lrIvkrluqn9ODHlK32qIjuANXwCL5G4nmWTQ-a03IR2gDoxNVFS8au7AS1nuGM4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IWIwZlHQXoToYaF5xqtnI5aYEivYXABCoyz9G-A29GkrHGg1qt15-JeVRddXlGnuhbjiy0Hx8jK1MYwnuZKsCmHExnvOgSfbG83SsxXcIp77VH5Lj7KkjqoTJ_232O4jmMqBzCe7zJbFBJ-wzqjNTqTw6WnTcvyFBd-HAxn6o1zxRM1xOBNkfE7a0MLzdWdggmpYgqMayyGAz5P1VdadN6stzmjdmcrN8fhOqdtpgFR_kXZKratQyhczZf27T494WGtMfFnjCxf2acpBqAV85Q_YmCU7jDZFxvUXfPnsVsyL3FcL4_qzSZofq_nQACBpcLZEM5hLoeFeBIjlHFSlMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمود نبویان، عضو کمیسیون امنیت ملی مجلس شورای اسلامی، در ایکس نوشت: با مشاهده‌ی متن توافق باید اعلام کنم، نسبت به دو نسخه‌ی قبلی، خسارت بارتر و عقب‌نشینی‌های ایران نیز بیشتر شده است.
@
VahidOOnLine
نبویان سپس در توییت دیگری با اسکرین‌شات پست ترامپ درباره توییت عراقچی نوشت:
توافقی که با پخت و پز بانیان توافق ننگین برجام باشد، حتما
#خسارت_محض
است
nabaviantwt
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76275" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76274">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bbcCJS62JqeSP_oH9XMhvbFrcYnr6Xu-uMTsK7rMLC0F61Ykl7Zg5wtG3U9ZyDoa2DA4X6Anw_mHAiHepcO4mW6k1xuCAsJ-ciMAmlvnSqD79JbTSDvjig2wX0zDJqd-1ChrnINRGygwRn-GwEwL4fdtTpJMJehjth1CaxZIUInEQOXZI8RnAcjy8iIibKGDLeKL3SNbDGr7a_9g_xPIrM6EoGqQAnqKxoQrGlAjBwJ0u68cAP1cnPNbpToisbM8IdbJafbS1IVsDiVIXPYeO5mCfvDhoRHg6-gp_ZGIXYBJJPFWDywzVn-gaDUuFAoS8FedWqCjcfcTYeEmcHvGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.
سی‌ان‌ان به نقل از مقام ارشد دولت ترامپ افزود که جمهوری اسلامی با «برچیدن برنامه هسته‌ای، نابودی و خروج مواد هسته‌ای، آزاد نشدن دارایی‌ها تا زمان اجرای تعهدات، باز ماندن تنگه هرمز و توقف حمایت مالی از گروه‌های تروریستی» موافقت کرده است.
مقام ارشد دولت ترامپ گفت مقام‌های جمهوری اسلامی پیش‌تر گفته بودند بدون آزادسازی دارایی‌ها توافقی را امضا نخواهند کرد و بارها از گفت‌وگو درباره حمایت مالی از گروه‌های تروریستی خودداری کرده بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76274" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76273">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LZ55uGCTqJxCOsIgnf2PWzg8MkH3e-8rwk4GxKuksp1nRFxkax495Ft7RkzjykHEOyVJhzgcqyrAq4fwKpTAqJo-IRbbNWRlhV-VWDlgk04ar02E-Xa-KiOu8ZO0nkxXFcNfTAKnj1fyKUb2vThOmc13mFsOfZcB8zJqM4GbGrUMuJTlMi6u73niAgQ6h--mIexQgISmp_6Rj-aQKVOIP9LgXJIFOC8U35pyL7nQhH03bI-z2wyHQQp0pL8KsxrwPFfsqeLZK-ardtIMD_j0n5BcB1g3_Oimtm2xM6o9fLyyPsEcDIgfycdC_KUGpduaew5OLBoABPiDU64lnz4tRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس گزارش داد دونالد ترامپ،
پیام عباس عراقچی در شبکه ایکس
را «بسیار مثبت» ارزیابی کرد و گفت معتقد است توافق با جمهوری اسلامی می‌تواند در آخر هفته یا روز دوشنبه امضا شود.
اکسیوس همچنین به نقل از ترامپ نوشت که جمهوری اسلامی به صورت خصوصی بابت انتشار «اطلاعات نادرست» عذرخواهی کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76273" target="_blank">📅 20:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76272">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TBbRHYYswm7bqLkUlPG99WqaGUr3vag5OC71O9mVDXH6uz9MFGAf080I5JV_g5Spw0dLW4gxMyM3Mz6hSwf0s-GhXNtBFSZPf1jKbhIW_248Rowvzbw8nLJG_dtwqzlZMvJeihb-MlQ5alM9DsN98IIi6kB65gNyPvb_CA-DUkBPfsURmPcP8-JYCHqelzKpth8p6ZbIAEhRR8E2Uq6RVPAAmPOjpgQYdB3nrwOdxfqnNqz1rGmWPzhtHzdqZmojl-6nxKhStRXr3PaV_8bg-YNvzYMuhs1oN5hwvnJz95-1oF89HBFAnH-gNaR8BPsvi7h0r1xwJwbVNR36ua7D-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیرحسین ثابتی، عضو مجلس شورای اسلامی، نوشته:
طبق اطلاعات به دست آمده متن توافق احتمالی بدتر از برجام است/ چنین توافقی نه گشایش اقتصادی می‌آورد و نه جلوی جنگ را میگیرد
دوشنبه شب در تجمع مردم در میدان مجتهدی طرشت حاضر شدم و توضیح دادم که دشمن به دنبال نابودی ایران است، چه از طریق جنگ و چه از طریق مذاکره و کسانی که هنوز هدف دشمن را نفهمیده و فکر میکنند با توافق با امریکا میشود دشمن را سرجایش نشاند، بدیهیات اتفاقات اخیر را هم نفهمیده‌اند.
سپس گفتم طبق اطلاعاتی که تا این لحظه از متن توافق احتمالی به دست آورده‌ایم توافقی ضعیف‌تر از برجام در راه است که خطوط قرمز رهبری در آن رعایت نشده و نه باعث گشایش اقتصادی میشود و نه امنیت کشور را تامین میکند.
در پایان نیز تبیین کردم که اگر بخواهیم امنیت مان را حفظ کنیم باید بیشتر از همیشه آماده جنگ باشیم وگرنه با ژست مذاکره و گفتگو و تن دادن به توافق به هر قیمت امنیت کشور نیز در دراز مدت مخدوش خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76272" target="_blank">📅 20:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76271">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SMacAuLaCV34Q-O9NnP7Tp2vt8e9XrakJSJSUaAEkV4TfXhRBaQo8wFLHNZ__tCft3mJxsGJwUDZR1gTo_i7UZqsuG9y4s1_7ETvLwz98N3O3ZObc-Lg2YB2Pnj6kv0fY3z7S_Po-bIpI5jp1xZOYo1JAvOE_W6cSIGVbWpJ_aDUsILM2ix-5QjWQwWJoD2AJYQ3TfXjeSIA6QHRWD8IMcFXyyFtcHLsYVHok3YLAM2Ka-ERLYD6JXSbkza5_g17GYbH24d5JUfHItid9HANypEM7E3EoJIVByQn0StdAY9gspWq371rlMBBq-LDDVVuxd8cas7qaaCHdUkT1caakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف، نخست‌وزیر پاکستان در پستی در ایکس نوشته است «در میانه تلاش‌های فشرده میانجی‌گرانه پاکستان، ما کاملاً از کارزار بی‌وقفه انتشار اطلاعات نادرست که از سوی طرف‌هایی که با هدف خراب کردن توافق صلح انجام می‌شود، آگاهیم. با کنار گذاشتن این حاشیه‌ها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق حاصل شده است و پاکستان اکنون به‌طور نزدیک با هر دو طرف برای نهایی‌سازی مراحل بعدی همکاری می‌کند.»
او نوشته است:«صلح هرگز تا این حد نزدیک نبوده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76271" target="_blank">📅 20:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76270">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DpLtglAOSryKMpRNQ9iAAvVqKjKSUY2r5j6h-36f9wbCHiF8Wc44UcWWGpJNNMbnCj_VNEM7hFgvliCZznGCWV8Qwq9_1IgRb3jZV8besIJYWLSTjwQncWTXajkMHXIhqM38SLTnyzdepZ-3I_7V3p08kNzSE3eYHDlV6qow8kOsS80opghFjbBHtCwjYH-DL8y_SA-ScoL2IpG6x9SpnOGwF3mphe0y7QMZc-PX9QsNgvZw5wpG3mL7OzRQlBtQttzDHcT0LAFKk6IC_uT4H22DMDYhvzZGi53ihlNG8sgCjcdhKV9CVzBMx_QGBFEOfGHGvpXSKMXwzBr_HZ5WtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اسکرین‌شاتی از
این توییت عراقچی
رو پست کرد:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76270" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76269">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RygOPS5096lvL-U1ALxpbqLOMVs9Wz-W1qrqK8HeGeSaUMvCkVOwa-nIzyqBdw3ZeHN0aPv9BLunxEeBNZuzQIFGLB5Krd2_o3L9p3Yv-SqOfIk2aln3UUfkSphtKazq6QnyHkDWUL3R8DyslH9VfVU7e-CfNI-GxzDGQR0uLKQVVUn1pAZQE6PiwXnxK5kwtbe03_izWVba2pM4xTw_lttEFPeR0-RRpK9_UFxxMokDTLkgs4VygXOfLQAc-XLC7qMcKi-9RPehaJGs0rIS-crgX4xcOehfRSNYyqoGKeuIIY1TxJ2opsscgvErpLGO2w4B6gjlebdvBUz2o59Dkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه واشینگتن‌پست در گزارشی خبر داد که قطر در جریان جنگ ایران مذاکراتی پنهانی با جمهوری اسلامی انجام داده تا تاسیسات گازی خود را از حملات تهران در امان نگه دارد.
قطر در واکنش، این گزارش را تکذیب و واشینگتن‌پست را به تلاش برای آسیب زدن به نقش میانجی‌گرانه دوحه متهم کرد.
واشینگتن‌پست در گزارش خود تاکید کرده که اقدامات پشت‌پرده قطر، تصویری از شیوه‌های پنهانی کشورهای خلیج فارس برای دور نگه داشتن خود از خسارات بزرگ‌ترین جنگ منطقه در ۲۰ سال گذشته به دست می‌دهد.
در این گزارش با اشاره به حمله موشکی جمهوری اسلامی به تاسیسات گازی راس لفان در قطر در اسفندماه سال گذشته، نوشته شده است این حمله بخش‌هایی از بزرگ‌ترین مجتمع تولید گاز طبیعی جهان را نابود کرد که نزدیک به یک پنجم گاز جهان را تامید می‌کند.
این حمله همچنین قراردادهای چندمیلیارد دلاری با چین و دیگر مشتریان را به خطر انداخت و چشم‌انداز پایان زودهنگام جنگ را با کشاندن قطر، یکی از میانجی‌های کلیدی میان آمریکا و جمهوری اسلامی، به درون درگیری تیره‌تر کرد.
به‌نوشته واشینگتن‌پست این حمله اما یک پیامد پنهان دیگر نیز داشت. به‌گفته مقام‌های امنیتی خاورمیانه و مقام‌های غربی مطلع از اطلاعات محرمانه، این حمله همچنین تلاش‌های مخفیانه قطر برای خارج نگه داشتن مجتمع گازی خود، موسوم به «راس لفان»، از فهرست اهداف جمهوری اسلامی را ناکام گذاشت.
یکی از مقام‌های ارشد امنیتی منطقه به این روزنامه گفت قطر چیزی در حد یک «توافق محرمانه» پیشنهاد کرد؛ توافقی که بر اساس آن دوحه متعهد می‌شد از نفوذ خود بر عرضه گاز برای تسریع پایان جنگ استفاده کند و در مقابل از جمهوری اسلامی تنها یک تعهد می‌خواست: «به ما حمله نخواهید کرد.»
یک مقام دیگر که به همان اطلاعات دسترسی داشته نیز به واشینگتن‌پست گفت پیام قطر به تهران این بود که: «شما بدون حمله به ما نیز به اهداف خود خواهید رسید.»
به گفته این مقام‌ها، قطر نتوانست تعهدی از جمهوری اسلامی دریافت کند. با این حال، روندی که پس از آن رخ داد نشان می‌داد که احتمال وجود یک تفاهم ضمنی دست‌کم به‌طور موقت همچنان برقرار بوده است.
قطر در سومین روز جنگ، زمانی که جمهوری اسلامی صدها موشک و پهپاد مسلح را به سوی اهدافی در سراسر خلیج فارس شلیک کرد، مجتمع راس لفان را تعطیل کرد. در آن زمان، قطر دلیل این اقدام را «حملات نظامی علیه تاسیسات عملیاتی» اعلام کرد.
تصاویر ماهواره‌ای که بعدا از سوی واشینگتن پست بررسی شد، هیچ نشانه آشکاری از خسارت در راس لفان نشان نمی‌داد.
اظهارات مقام‌های قطری نیز نگرانی‌ها را در بازارهای جهانی انرژی تشدید کرد؛ از جمله هشدار وزیر انرژی قطر که گفته بود این جنگ «اقتصادهای جهان را به زانو در خواهد آورد.»
قطر در پاسخ به پرسش‌های واشینگتن پست، هرگونه توافق محرمانه با جمهوری اسلامی را رد کرد و گفت تصمیم برای توقف تولید در راس لفان صرفا به‌دلیل تهدید حملات و نگرانی برای کارکنان و زیرساخت‌هایی اتخاذ شده بود که شریان حیاتی اقتصاد این کشور محسوب می‌شود.
...
iranintl
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76269" target="_blank">📅 19:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76268">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gMYyabLZ12nfzR7-N-aQfioKDEzdP0pENUGZ3WDa5f2p4YUWNgkCZNOgEnUFnRXQUqXTbBmr6If6CHKwiEPyfZRfsVDQpGNyXgOsPYXdABzVykoO0oU4SjpijNpqNxFw4mqbuFifKDK1Ok3caaklnkvslJ7Cs1r1zCncOvIGUPe_8hByYwGT1TIBF5OrF9bn4kS8b9F4QbRq7dQEWfte9EdhrEerkoS8kjS_Suw20BV5alSc4ycZo411PGW8oZKyoji9faqsdNVZWUn6PoY7QNGVyT46VLrAJyM9QTwkysZB0Ynea3nrvyM2TYHT6g_eYskJIhBA6v_SzaHbSle97w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز جمعه گفت که در ازای امضای توافق با ایالات متحده یا حضور در یک نشست، هیچ‌گونه منابع مالی در اختیار ایران قرار نخواهد گرفت و تهران «هیچ پولی دریافت نمی‌کند».
او در شبکه ایکس نوشت توافق آمریکا و ایران «به گونه‌ای طراحی شده است که اطمینان حاصل شود نگرانی‌های ایالات متحده و متحدانش در اولویت قرار دارند و در صورتی که جمهوری اسلامی ایران به تعهدات خود عمل کند، منافع اقتصادی به ایران و همچنین به کل منطقه خواهد رسید».
معاون دونالد ترامپ همچنین وعده داد: «این توافق این ظرفیت را دارد که منطقه را دگرگون کند و به صلحی پایدار منجر شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76268" target="_blank">📅 18:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76267">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NuPAGBKAzhrCcwmt225K4WAJtlP0_WxLnteZa8Ivb7lJyDY_JOuSZ1cRX6_zTJLblzCvHqhnxRCmaq_x-m7QQX3jhCcuzitPRPsuwGU4L-73gYHyzmwV1pFB_HmVl6rAcKY_r023lLjuhe3DBPzTsWI1J4Y0BkgJVUt8TmRVf-MUWz4ILHGwNV3YHHXnDKNf-1lfpvQZN4hq0f7Dnt0SZam7v8h245WMNgx9IkbBUh4I6Nqhq1xO7UlMcYWjQQ-WWYP_kc4YN2V9KzZn7LphtlrKAxS8cBfVqKSs1nJOkFDMRu4tE_DqQ5xBNak5q1Q0qzhwXE5ixOj-CxHd6aLWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت عراقچی، ترجمه ماشین:
یادداشت تفاهم اسلام‌آباد هیچ‌گاه تا این اندازه نزدیک به نهایی‌شدن نبوده است. تا زمان نهایی‌شدن آن، رسانه‌ها باید از ورود به گمانه‌زنی درباره محتوای آن خودداری کنند.
در راستای رویکرد مسئولانه و شفاف ما، همه جزئیات در زمان مقتضی با افکار عمومی در میان گذاشته خواهد شد.
araghchi
ساعتی پیش، دونالد ترامپ،‌ رئیس‌جمهور آمریکا، از آنچه درز دادن مواردی از توافق به رسانه‌ها توسط ایران خواند انتقاد کرد و اعلام کرد موضع جمهوری اسلامی درباره توافق «هیچ نسبتی با واقعیت ندارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/76267" target="_blank">📅 18:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76266">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/012364ed90.mp4?token=BHcLBmCZSOti9y7tbzQBGsSD5INDi-pCvjGGAq72dVqmdmuyBd8zCoTebnYd4J7LfVsGtnOXqek1mgIo8nK8EVDw7xxmnaD0o33LwNwZ2Dv9KVQzWj1bs7yHqn_emfyF10K6IL-48FeAsdRFzDY1ySuXIZsniL1HEK6Zz--X_bVgHFZxdy5xtMxn76XKPx35uTCpZXol4-ye7sfxVYOJqO0ZWF7EQBWrtxzRluAaQs1v9SentIFy6SX9qubQW6BMJ5ygf6xZ47oL2uk_Qnls2_Y8raYh3OcrNZV4os5REjEy8JeYXaBjFlp-0AVp5BSjH1ZoNGxjYKNcbE2yz6X_VA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/012364ed90.mp4?token=BHcLBmCZSOti9y7tbzQBGsSD5INDi-pCvjGGAq72dVqmdmuyBd8zCoTebnYd4J7LfVsGtnOXqek1mgIo8nK8EVDw7xxmnaD0o33LwNwZ2Dv9KVQzWj1bs7yHqn_emfyF10K6IL-48FeAsdRFzDY1ySuXIZsniL1HEK6Zz--X_bVgHFZxdy5xtMxn76XKPx35uTCpZXol4-ye7sfxVYOJqO0ZWF7EQBWrtxzRluAaQs1v9SentIFy6SX9qubQW6BMJ5ygf6xZ47oL2uk_Qnls2_Y8raYh3OcrNZV4os5REjEy8JeYXaBjFlp-0AVp5BSjH1ZoNGxjYKNcbE2yz6X_VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: خطرناک‌تر از ناو، سلاحی است که می‌تواند این ناو را به قعر دریا فرو ببرد  رهبر جمهوری اسلامی تعیین نتیجه از قبل برای مذاکرات بین ایران و آمریکا را «کار غلط و ابلهانه» خواند و گفت اگر هدف گفت‌وگوها برچیدن برنامهٔ هسته‌ای باشد، چنین موضوعی اساساً جای…</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76266" target="_blank">📅 18:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76264">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fYKEoHjpiMB_H34b5HeZfkuzSnVUJx4Ujy1VbF_HU2VTFV0bLkLK16VEIneHe18gkEFRmNEcDlgj1sVSmO-o1prmjNkZYYKLML9DRIaINxY9lNevAETTItA4Qp3H2tJCi_vSby919dAc52F3cVTUb4ZAd4AuYTugZpTbUAw11GnxUMocd-t25P49qYiU5-E9oyf6W_DH9QbVTSnc4BxAXd5tFwueJZYFELNDEqFVTGrZx2Z8uqcnDqox9IQCkWFQ8y2cGolODh47JfnH4d7w_TrTeHvUEjpStOefrbbSsrUKJCS1CLkwifZKJtiJ3uhO3rpvzfwypZ7DWAK20xEw5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
شرایطی که ایران به رسانه‌های اخبار جعلی درز داده، هیچ ربطی به شرایطی ندارد که به‌صورت مکتوب بر سر آن توافق شده بود. آنچه آن‌ها گفتند، از جمله بیانیه ضعیف و رقت‌انگیزشان درباره داشتن یک توافق، هیچ نسبتی با حقیقت ندارد. طرف‌های بسیار بی‌شرافتی برای معامله هستند. با آن‌ها چیزی به نام معامله با حسن‌نیت وجود ندارد. شگفت‌انگیز است!
همچنین حمله پهپادی کاملاً دفع‌شده آن‌ها در شب گذشته علیه کشتی‌های هندی که در حال خروج از تنگه هرمز بودند، کاملاً غیرقابل قبول است. بهتر است هرچه زودتر خودشان را جمع‌وجور کنند، آن هم سریع!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76264" target="_blank">📅 17:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76263">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UMwO-K9dgUD5HeEHD8NyG00tEmTh0OLzAWA9aIsvpA8jNtRP_lqitchSgFhv0HPqOUkUw4UWrcBc5ANWmEyOp0EMf0FuygkdY3rj3DyjBNHUqe6DaRu0a-8CfcTSBQ4-P7BEGlTIF2v2XfIxxWdMXEUcNnXlLYfZ7y9LSn2N6gfCerJ5NFSxSYxzD8wYnD8vtm_jNwd6E5oSte-L1KyKQCaSc9Chy7Lvja72e5FfjoV451Vdt8L3qDHKlTsikHbJ7fNXrFCJjlbANv39bl8KeXTv_5n4D_CFhuesz6-PjhwJU0xySNnJhHwJLyv_uUgSdfUveySrMnAGXA7Zi0M0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حبیب‌الله سیاری»، معاون هماهنگ‌کننده ارتش، در گفتگویی با تلویزیون حکومتی جمهوری اسلامی تایید کرده است که از سرنوشت خلبانانی که در جنگ اخیر به قطر حمله کردند اطلاعی در دست نیست.
در این گفتگو که شامگاه پنجشنبه ۲۱خرداد۱۴۰۵ از تلویزیون جمهوری اسلامی پخش شد، سیاری درباره خلبانان یک یا چند فروند جنگنده سوخو ۲۴ متعلق به ارتش ایران سخن می‌گوید که به پایگاه العدید در قطر حمله کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76263" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76262">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPl2yTQ2fyDwZHTgBAsVAlhX0yNtd9VirSZryV5QjaxMoLfTNCTM3PbUg25XzYqIzDNGZfQprRYdbgLE1ArXVs3hYnCuNA0Dg68BFTczNIcR6nicJwvoH3ZyrmotgdYMygT_pmM7aIrFsSEP5mzcsM_Ch9TZa0jKZvSaTP8LT_rXIusHzNqHsSzVuR-4BC8ogJLMRsV2EnqF-mczEVBMIVR-DwulAItM7fFXtoRhkoXyHGVgqTyma7Ptth1oxUnqkvwJ4G6XfFhan34FiwV0BMvNWhYVq0vePB1vy29KL1akK9S2UyeE79H4Qg6qc8Ou23xrnTZoudsBSofwyDMDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود نبویان، نماینده مجلس جمهوری اسلامی، با انتقاد از پیش‌نویس توافق احتمالی میان آمریکا و جمهوری اسلامی، آن را مشابه برجام و «خسارت محض» توصیف کرد. او گفت: «حرف از پیروزی با این متن مبهم و خسارت‌بار کاملا غلط است.»
نبویان با انتقاد از مفاد مطرح‌شده در پیش‌نویس توافق، گفت در این توافق جمهوری اسلامی حق تولید سلاح هسته‌ای را نخواهد داشت. او همچنین افزود سرنوشت مواد غنی‌شده به رضایت آمریکا وابسته شده و همه موضوعات مرتبط با برنامه هسته‌ای باید مورد مذاکره قرار گیرد.
این نماینده مجلس تاکید کرد: «این توافق مانند برجام خسارت محض است و بخاطر تغییر محاسبات مسئولان است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/76262" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76261">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdjLad1oEggDEQUW1_vO6pB_zrqT8smbCDSnzClgzyya8X1WxuhwCYjAGD2IBeehWShbsfMfsz6cViBNrtalGgPFo9_jx6ewzolpMjv9OSHBR1Y0BowNRChO7eYLWZSiPZXyNZ6Ny-CvJhjauYgPDXUA9Hu1lZVV47AfIoqD7VCulwF4tUB0egpwe8ZfS9IOKntr3aWqI_zGYTJCwisqyieq1-sqDDJoQMkKSL9UptztzldT6OLIjnNOO7ld1BFm0S4fWZu55PSTbCulp2zLevgJj2KNHMZkWdxIlzDH-WAim1s7ZCDYqChQLHSmOaiavJCm0gKEzS8dJOu6kmL5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اعتماد در داخل ایران به نقل از یک عضو رسانه‌ای هیئت مذاکره‌کننده جمهوری اسلامی و وب‌سایت اکسیوس در خارج به نقل از یک دیپلمات از یک کشور میانجی و یک مقام آمریکایی روز جمعه، ۲۲ خردادماه، گزارش‌هایی از محتوای احتمالی تفاهم‌نامه میان ایران و آمریکا منتشر کردند.
این دو گزارش تا اندازه‌ای به یکدیگر نزدیک هستند، اما گزارش اعتماد با وجود جزئیات بیشتر به نقطه نظر حکومت ایران نزدیک است، در حالی که متن اکسیوس برخی از موارد را منوط به آینده مذاکرات گزارش کرده است، مانند تعلیق تحریم‌ها که اکسیوس می‌گوید مشروط به پایبندی تهران به تفاهم‌نامه است.
روزنامه اعتماد به نقل از «عضو کمیته رسانه هیئت مذاکراتی ایران» از تفاهم‌نامه‌ای ۱۴ ماده‌ای می‌گوید که در آن بر «بازگشایی تنگه هرمز ظرف ۳۰ روز با ترتیبات ایرانی» و «تعلیق تحریم‌های فروش نفت، محصولات پتروشیمی و مشتقات و دسترسی کامل ایران به منابع مالی آن» تأکید شده است.
این در حالی است که در گزارش اکسیوس آمده است که تنگه هرمز «بلافاصله بدون دریافت عوارض بازگشایی می‌شود» و «ظرف ۳۰ روز» تعداد کشتی‌های عبوری از این تنگه به زمان پیش از جنگ بازمی‌گردد.
در مقابل این اقدام، آمریکا هم محاصره دریایی بنادر ایران را که بر صادرات نفت ایران اثر قابل توجه دارد حذف می‌کند.
اکسیوس به نقل از منبع دیپلماتیک خود می‌نویسد: «هیچ تاریخی برای تعلیق تحریم‌ها تعیین نشده و تعلیق منوط است به اجرای توافق [از طرف ایران].»
به نوشته اکسیوس، تعلیق تحریم زمانی افزایش می‌یابد که ایران «تفاهم‌نامه را اجرا کند و در مذاکرات بعدی از خود حسن نیت نشان دهد».
تفاوت دیگر بین دو گزارش از محتوای احتمالی به آزاد شدن یا نشدن اموال بلوکه‌شده ایران مربوط است. اعتماد به نقل از منبع خود می‌گوید: «آزادسازی ۲۴ میلیارد دلار پول‌های بلوکه شده ایران در دوره ۶۰ روزه مذاکرات نهایی. نیمی از این مبلغ قبل از شروع مذاکرات باید در دسترس ایران قرار گیرد.»
این در حالی است که دونالد ترامپ پیشتر به طور مشخص با آزاد کردن پول‌های ایران پیش از مذاکره یا رسیدن به توافق مخالفت کرده و به طور کلی به این کار به دلیل سابقه‌اش با باراک اوباما در توافق برجام حساسیت ویژه دارد.
گزارش اکسیوس در این زمینه سکوت می‌کند و می‌نویسد که «مشخص نیست» که متن تفاهم‌نامه حاوی اطلاعاتی درباره پول‌های ایران هست یا خیر.
درباره برنامه هسته‌ای ایران، اکسیوس نوشته است که تفاهم‌نامه شامل «تعهداتی»‌از طرف ایران خواهد بود، مهم‌تر از همه این که ایران هرگز به دنبال سلاح اتمی نخواهد رفت و بن‌بست در مورد اورانیوم غنی‌شده را حل خواهد کرد، دو موضوعی که ترامپ بر آن تمرکز دارد.
به نوشته اکسیوس، ترامپ موافقت کرده است که یکی از گزینه‌ها برای حل این مسئله رقیق کردن اورانیوم در داخل ایران «زیر نظر کارشناسان سازمان ملل» است، نکته‌ای که پیشتر روزنامه نیویورک تایمز هم خبر داده بود.
منبع اعتماد تنها به این شکل به این موضوعات اشاره کرده است: «۶۰ روز مذاکره برای رسیدن به توافق نهایی مبتنی بر موضوعات هسته‌ای و لغو کامل تحریم‌های اولیه، ثانویه، آمریکا و قطعنامه‌های شورای امنیت سازمان ملل و شورای حکام آژانس بین‌المللی انرژی اتمی» و «تکرار تعهد ایران در پیمان ان‌پی‌تی مبنی بر عدم تولید سلاح هسته‌ای».
در این بخش از گزارش روزنامه اعتماد به موضوع سرنوشت مواد غنی‌شده اشاره نشده است.
به طور کلی، بر اساس گزارش اکسیوس، تفاهم‌نامه در صورت امضا شدن آتش‌بس جنگ را، از جمله در لبنان، تا ۶۰ روز تمدید می‌کند، دو ماهی که قرار است تهران و واشینگتن مذاکرات هسته‌ای را برگزار کنند.
آن طور که اکسیوس نوشته است، ایران و آمریکا بر سر متن تفاهم‌نامه توافق کرده‌اند، و این متن توسط مقامات عالی‌رتبه در جمهوری اسلامی نیز تأیید شده، اما «احتمالا هنوز تأیید مجتبی خامنه‌ای را ندارد». بنابراین در حال حاضر گفته سخنگوی وزارت خارجه ایران که تفاهم‌نامه هنوز نهایی نشده به واقعیت نزدیک‌تر است.
در حالی که ترامپ از امضای تفاهم‌نامه احتمالا در روزهای شنبه و یک‌شنبه حرف زده بود، به نوشته اکسیوس، چهار هواپیمای نیروی هوایی آمریکا روز پنج‌شنبه برای انتقال تجهیزات سفر جی‌دی ونس، معاون ترامپ، به ژنو در سوئیس برای شرکت در مراسم امضا «در روزهای آینده» پرواز کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/76261" target="_blank">📅 17:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76260">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3T6wJJJc0DJ-2Pm2JSqmfCLsNlxadMUDbJHN_5ax7bEDjFrbCo1st5Xl67heSFWJh5uM4tpr5rFcTWFVEHxjIHv2Q6mKH7ahtGVrMuNEgmZvdnQ_M8xrl0WmDQVraCbuON9YJqgh-NTri2LEPPydaxG2yf0jz57RC2zY2FNX1mT3EqJapl4HX0szXPxiswHVXAF4NsjhDVYCM_kCLpG7PduWN_8roG6JAW4TGTfjNwSViCWS3TBV1WPq6c8bVsyCYty_3F8sRdm67hYWWAAss6SBNsqWqYXFcfnBAotbx5lR0vpWnymZtDshbTphQvad6m7xoiS6wWxA4WcNtrAVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ به نقل از مقامات ارشد آمریکایی و ایرانی نوشته احتمال دارد توافق میان دو کشور از روز یکشنبه و در شهر ژنو سوئیس نهایی شود.
این خبرگزاری بدون اشاره به نام این مقام‌ها افزوده که طرفین «در آستانه» دستیابی به توافقی برای بازگشایی تنگه هرمز قرار دارند.
بر اساس این گزارش، طرف‌های ایرانی و آمریکایی قرار است در حاشیه اجلاس گروه هفت که از دوشنبه در فرانسه برگزار می‌شود، «دیدار کنند».
اجلاس امسال گروه هفت از ۲۵ تا ۲۷ خرداد در دامنه‌های آلپ فرانسه برگزار می‌شود. به گفته افرادی که در جریان برنامه‌ریزی‌ها قرار دارند، شهر ژنو در سوئیس که در نزدیکی محل برگزاری اجلاس قرار دارد، به عنوان یکی از گزینه‌های احتمالی برای امضای این توافق مطرح شده و ممکن است این مراسم از روز یکشنبه ۲۴ خرداد انجام شود.
یک مقام ارشد ایرانی و یکی از اعضای گروه هفت به بلومبرگ گفته‌اند که «احتمال دستیابی به توافق زیاد است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/76260" target="_blank">📅 17:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76259">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JbmFvOafLWULXtpVpopcN8rZKAfxp16R5quZw-iOFV2dM_4hISoONbKrCCrrFpbRPAD-rem3Ec9SMt8xZLlEoWsMvD0RArbWw3HjyMG_bMBzjUyZdxi__O245-fV7ieaJes0cC14ZhY_ck13xqXUrNQblDnEXrkePIxadYWmhXAR9QB73gd53oluMeNDvTxuiKvWKM-oPPh0zGTe1VNATTorwZ2vYGFrc9kWVIMEAB_aKy6gwDNQBUQTC8RLIc6DlQySq4VWrzhZzwk5OjStcrU3oingBlPkCKcFGBwEVSx5Gcbtthgn3UHsyAYUVBPAkMDCH5Q0WhzQSDlfxFrr9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، جمعه ۲۲ خرداد به نقل از «منبع نزدیک به تیم مذاکره کننده ایرانی» جزئیات جدیدی از پیش‌نویس تفاهمنامه ۱۴ ماده‌ای ایران و آمریکا را منتشر کرد.
بر اساس این گزارش تهران متعهد می‌شود به دنبال ساخت سلاح هسته‌ای نرود و در مقابل، برخی امتیازهای اقتصادی از جمله تسهیل صادرات نفت و بررسی آزادسازی بخشی از دارایی‌های مسدودشده را به دست می‌آورد.
مهر به نقل از این مقام گزارش داد که پس از امضای احتمالی این تفاهم‌نامه، مذاکرات جامع‌تری به‌مدت ۶۰ روز آغاز خواهد شد و موضوعات پیچیده‌تر از جمله سطح غنی‌سازی اورانیوم، ذخایر اورانیوم غنی‌شده و جزئیات رفع تحریم‌ها مورد بررسی قرار می‌گیرد.
براساس این گزارش ۱۴ محور تفاهمنامه احتمالی تهران و واشنگتن شامل موارد زیر است:
۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان
۲- تعهد آمریکا به مداخله نکردن در امور داخلی ایران
۳- رفع کامل محاصره دریایی ظرف ۳۰ روز
۴- تعهد آمریکا به خروج نیروهایش از پیرامون ایران
۵- بازگشایی تنگه هرمز ظرف ۳۰ روز به وسیله ایران
۶- تعلیق تحریم های فروش نفت، محصولات پتروشیمی و مشتقات و دسترسی کامل ایران به منابع مالی آن.
۷- لزوم ارائه طرح های بازسازی ایران حداقل به مبلغ ۳۰۰ میلیارد دلار توسط آمریکا و متحدانش
۸- ۶۰ روز مذاکره برای رسیدن به توافق نهایی مبتنی بر موضوعات هسته‌ای و لغو کامل تحریم‌های اولیه، ثانویه، آمریکا و قطعنامه‌های شورای امنیت سازمان ملل و شورای حکام آژانس بین المللی انرژی اتمی
۹- تعهد ایران برای تداوم عضویت در پیمان «ان پی تی» مبنی بر عدم تولید سلاح هسته ای
۱۰- در دوره مذاکرات آمریکا متعهد شده به نیروهای خود در منطقه اضافه نمی کند و تحریم جدیدی هم وضع نخواهد کرد.
۱۱- آزادسازی ۲۴ میلیارد دلار اموال مسدود شده ایران در دوره ۶۰ روزه مذاکرات نهایی. نیمی از این مبلغ قبل از شروع مذاکرات باید در دسترس ایران قرار گیرد.
۱۲- تشکیل سازوکار نظارتی برای اجرایی کردن توافق احتمالی
۱۳- تایید توافق نامه نهایی توسط قطعنامه شورای امنیت سازمان ملل
مهر به نقل از این «مقام آگاه» گزارش کرد که در بند آخر توافقنامه احتمالی، دوطرف تفاهم می‌کنند، مذاکره نهایی قبل از آزادسازی نیمی از اموال مسدود شده ایران، تعلیق تحریم‌های نفتی و رفع محاصره دریایی آغاز نشود.
دونالد ترامپ، رئیس جمهوری آمریکا شامگاه پنجشنبه گفته بود که به محض امضای توافق، محاصره دریایی پایان می‌یابد و تنگه هرمز باز می‌شود.
به گزارش مهر، توافق نهایی صرفا در موضوع سرنوشت اورانیوم‌های غنی شده و غنی سازی، رفع تحریم‌ها و «برنامه بازسازی اقتصاد ایران انجام می‌شود» و بحث درباره برنامه موشکی و حمایت از گروه‌های نیابتی «به صورت قطعی از دستور کار خارج شده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76259" target="_blank">📅 17:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76258">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de4GEnnJ_Y6KbjdTpesJBDDvmge3_-rrcdxOWecjQivKLoabo9n5pbYmsosMLmGpV4Ba5A6_oIjG7RCc7lJXRwO3EhMCie1LuNl4ZP-Q2DhVvsWZHcdDG69ecyXvb2HRxnZ9lhW71pTW5Qsz5PE5N-mA30Jqf_JWgZQoEx4rsJ7FtMiGWh-0S9RKuzD4tlf8kZCuxWFc_FbLOJzYyYJ6OgOV9WQJExPyOo_NX-bcQfMCrKuDRPDtw4Mr3oLcUYk0byznLEWdmG9oFm1ZH-nq8zpwuKFXTBTmB9o65-j2wd0Mx6k8ubcxbwg-UaE0vM2VB7P4SpLQ0ibfvu2FWok4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«امیر احمدوند» ۳۹ ساله، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در نزدیکی کلانتری رشید در تهران هدف شلیک گلوله قرار گرفت و جان خود را از دست داد. او متأهل بود و همسرش در زمان کشته‌شدن او سه ماهه باردار و در شرایط استراحت مطلق قرار داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/76258" target="_blank">📅 17:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76257">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SOSqy_ZPQP7fzLhB5DSphl9yiUt1LPgqzf2QVgYe5cQ_bM8FveXrolh-majubpyPEQ5caQiWZUw_yMaMAZuiAz4Rxkal7MIZ7LFrRZJezNOLbftwxxyyvqHg6CwV87iw2Tc3Ur0ojRyrsURjLE1HH4uNIFQA35F7EiYaDlVgf9JtbEMKJg3Nv34zok3HmIRovhjOzhtCf0xQV3Uc0QTHTUwQVi4shSQXffRYcjgH-4BnZE_dzgFDhMUF_zFBkjisW4Glj9SbYZ8rUmDZIen_eBP0Avtlo8eVoSCzgblrpT7EElLR0XQrg3S3b_Q5cNhMR0vsdQporq_gh1WoinSU0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش پولتیکو، اندکی پس از آنکه دونالد ترامپ، رئیس‌جمهوری آمریکا، صبح پنجشنبه در پیامی اعلام کرد که قصد دارد ایران را «امشب به‌طور بسیار سختی هدف قرار دهد»، رهبران کشورهای حوزه خلیج فارس و جنوب آسیا در تلاشی آخرین‌دقیقه‌ای با او تماس گرفتند تا نظرش را تغییر دهند.
آنها به او اطمینان دادند که یک توافق اولیه که مسیر را برای مذاکرات جزئی‌تر هموار می‌کند، در واقع در دسترس است.
به نوشته پولتیکو، این تماس‌ها که پیش‌تر گزارش نشده بودند، به گفته دو مقام دولت آمریکا و یک دیپلمات مطلع از این تماس‌ها، از سوی تمیم بن حمد آل ثانی، امیر قطر، محمد بن زاید آل نهیان، رئیس امارات متحده عربی و عاصم منیر، رئیس دفاع پاکستان انجام شد.
هر سه منبع به دلیل حساسیت موضوع دیپلماتیک با شرط ناشناس ماندن با پولتیکو  صحبت کردند.
ترامپ سپس در تروث سوشال اعلام کرد که ممکن است یک توافق در چند روز آینده امضا شود.
@
VahidOOnLine
این رسانه نوشت گفت‌وگوها شامل بازگشایی تنگه هرمز و دسترسی ایران به بیش از ۱۶ میلیارد دلار منابع مالی بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/76257" target="_blank">📅 06:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76256">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IV6UzJLOgj8B3HPJofpMmTCuxe8u3p5zx98sPzxzcNfITiRCjfvxQbiQIUq_bfRCATMVatljyxxf3jHqRYBlUDx4uK2Mx4eo2cZb6MZpuUsr9RjmN9cGPy0to7r9swHdXC7CR8-sCfLQFxQLtzFaVYI-qHt-LoGtjpDVOZJKizYRoG58Y4iv9Yy4p-yXzk1wS701gk36OOcPmHZVz6S6GMNVPYJRdODepmtqIPjnKNX4_wfi09smlYRhs1_OHcnUvhdk7ALGrwpONF-v1klkWp5Szu0XGTXvzd-seoRiDW-7Tf2Y7f7t7QCmj3xNqk2CbcLErMhodtxlGJlaVHNs1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گفته یک مقام ارشد دفاعی ایالات متحده، ترافیک کشتی‌های تجاری در تنگه هرمز پنجشنبه شب پس از آنکه جمهوری اسلامی ایران پهپادهایی را به سمت کشتی‌هایی که از این آبراه استراتژیک عبور می‌کردند، شلیک کرد، آشکارا مورد تهدید قرار گرفت.
به گزارش فاکس‌نیوز این مقام گفت: «به نظر می‌رسد جمهوری اسلامی امشب تلاش کرده است به کشتی‌های تجاری که از تنگه هرمز عبور می‌کردند، حمله کند. نیروهای آمریکایی دو پهپاد تهاجمی یک‌طرفه ایرانی را سرنگون کردند.»
این مقام گفت که علیرغم این حملات، ترافیک دریایی از طریق تنگه ادامه دارد.
این تحول ساعاتی پس از آن رخ داد که دونالد ترامپ گفت توافقی با جمهوری اسلامی ممکن است ظرف چند روز امضا شود و تنگه هرمز به عنوان بخشی از این توافق بازگشایی خواهد شد.
در پی شنیده شدن صدای چندین انفجار در سواحل جنوب ایران، پیشتر خبرگزاری فارس وابسته به سپاه پاسداران به نقل از «منابع محلی» در بندرعباس گفت که نیروهای جمهوری اسلامی به یک نفتکش که «بدون هماهنگی» وارد محدود تنگه هرمز شده بود اجازه عبور ندادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/76256" target="_blank">📅 05:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76255">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Oy0jXxYD6Dvqu-qOfd8GNTATDjL3LHs9Qm30dSPjNvKsxMXWZ8pRJnRDqEokZaIS3BozPgDg-uvKdSIJGEwbSNa7GamrgF-YcNasvBKVBsEUM3XaM1iNhfX2YgIwC7dsU551iF_JHEbGyrGzRJrsmdqIlqj9yf7-VyvyhIyTO8LPPLz097j21LKS9KWrlflNSGENiJRLjZaW_9TrKt69a_AcPc-XR4saWxQjPdvKuMpAOIr9U0LN0mmPQ6SPaftqMy0987CjIkSyAylZZNe_D9y635LH9Oes7Oy1VbwYHG8x646Inp0Q9GfKtbcOjfhCnj1Gx1xEpbUdHvAlPU_wpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه به بزرگی ۳/۱ در پردیس
شرق استان تهران
عمق: ۱۰ کیلومتر
پیام‌های دریافتی:
سلام من فاز یازده پردیس هستم همین الان زلزله وحشتناکی اومد اینجا، کل خونه شد گهواره
سلام آقا وحید
یه زلزله عجیب اومد همین الان دماوند سقف میلرزید نه زمین
سلام پردیس تهران زلزله
۳
ریشتر
میشد شایدم بیشتر
سلام  زلزله آمد لواسان
ساعت 3 و ربع خونمون لرزید . رودهن
بی صدا بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76255" target="_blank">📅 03:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76254">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09e8c7b7d0.mp4?token=DsY1JQUOu_dkcrNo5C3RScQc0T5s8iRi9LcUisTBdtLwq7Vo2QXNdZLjEb1cADS-ZnxKLo-Fti83pbsLEBsY4PzSiRbM1TQ8YFyLonEajzINWmZhMpQHoa4jCyAZK0B6__yE9CIWHn0L4NfrqUPkfcjCTKg9AEbFUyU-4V05GMLlq_P2EscXHu3O-hyCvf-jjvr9XYIYt_snh86Bn07tQM5CjFg0S6uueaG_9uAniMnoAyGcWxGSOtDRnQuQOsNlhBbq21ketkTRo8UoNfjgoBtAw5HAlpXp1qu-cl8j_ZJEj-zA2RvGN9Y30Gyoqobna89VFiOwXPUJDsGZh2gVGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09e8c7b7d0.mp4?token=DsY1JQUOu_dkcrNo5C3RScQc0T5s8iRi9LcUisTBdtLwq7Vo2QXNdZLjEb1cADS-ZnxKLo-Fti83pbsLEBsY4PzSiRbM1TQ8YFyLonEajzINWmZhMpQHoa4jCyAZK0B6__yE9CIWHn0L4NfrqUPkfcjCTKg9AEbFUyU-4V05GMLlq_P2EscXHu3O-hyCvf-jjvr9XYIYt_snh86Bn07tQM5CjFg0S6uueaG_9uAniMnoAyGcWxGSOtDRnQuQOsNlhBbq21ketkTRo8UoNfjgoBtAw5HAlpXp1qu-cl8j_ZJEj-zA2RvGN9Y30Gyoqobna89VFiOwXPUJDsGZh2gVGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امروز جنگ با ایران را پایان دادیم.
و آن‌ها موافقت کرده‌اند که هرگز سلاح هسته‌ای نداشته باشند.
چیزی که ما روی آن اصرار داشتیم.
این کل هدف بود. این ۹۵٪ ماجرا بود.
در جریان گفتگوی تلفنی برای حمایت از نامزد انتخابات سنا در ایالت آلاباما
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76254" target="_blank">📅 03:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76253">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/chGbuqThz9PDRKXjmajjBbJ2lbbS3WpiKfm_DVruZFqHlJK1A2uTMEu5_PfVSuPljO-2vBuoLioFdeA0IUnnyLuMtQ3y6_kE4T8datRbGqMdlbu6ZR-VPXYuHhgcn8swnoTMAT6cbK5er4eXArZ8UtIplMlIKZUs6jrkhawSFpljZBFJzxmAWepdnZhuqZi3UTaNJEMMKJLprs2yHDMKW3U3XpjARBlB8isnggi2T7boTyPx-oU44eeAMD93vghzTzbnrdFakUP1qxhUMgwkrNygchQjEEZDtZsZLeiifeOakA3LciWu0N2dLfX3ACNLGMerb9TDnnC9Xfy-y0xzXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه العربیه بامداد جمعه ۲۲ خردادماه به نقل از منابع خود گزارش داد پیش‌نویس مفاد نهایی توافق میان آمریکا و جمهوری اسلامی شامل تمدید آتش‌بس به مدت ۶۰ روز و بازگشایی تنگه هرمز است.
به گفته منابع العربیه، مذاکره‌کنندگان در طول این دو ماه برای دستیابی به یک راه‌حل سیاسی دائمی تلاش خواهند کرد. این منابع افزودند مذاکرات هسته‌ای بر سازوکارهای راستی‌آزمایی، روندهای بازرسی و محدودیت‌های آینده متمرکز خواهد بود و در همین دوره درباره اورانیوم غنی‌شده با غلظت بالا نیز گفتگو خواهد شد.
به گفته منابع العربیه، آمریکا دسترسی به بخشی از دارایی‌های مسدودشده حکومت ایران را تسهیل خواهد کرد و در چارچوب توافق، کاهش و لغو بخشی از تحریم‌ها را دنبال خواهد کرد. این منابع همچنین گفتند آزادی کشتیرانی بر پایه توافق میان آمریکا و جمهوری اسلامی احیا خواهد شد و گفتگوها درباره لبنان و امنیت منطقه‌ای نیز پس از توافق ادامه می‌یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/76253" target="_blank">📅 01:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76252">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ادعای خبرگزاری فارس:
ایران اجازۀ عبور نفتکش متخلف از تنگۀ هرمز را نداد
🔹
پیگیری خبرنگار فارس در بندرعباس از منابع محلی نشان می‌دهد دقایقی قبل نیروهای ایران اجازۀ عبور یک نفتکش متخلف که بدون هماهنگی وارد محدودۀ تنگه شده بود را ندادند.
🔹
گزارش‌های مردمی نیز از شنیده شدن صدای سه انفجار در فاصله حدود دو کیلومتری ساحل از سیریک حکایت دارد.
صدا و سیما:
یک منبع آگاه نظامی تایید کرد صداهای انفجار شنیده شده در شهرستان سیریک مربوط به مقابله با یک فروند شناور متخلفی است که قصد عبور از تنگه هرمز را داشت
براساس اعلام این مقام نظامی؛  شناوری که دقایقی پیش مخل نظم دریانوردی اعلام شده بود یک فروند نفت کش است که با اخطار نیروی دریایی سپاه ناچار به رعایت قانون منع تردد در تنگه هرمز شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/76252" target="_blank">📅 01:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76251">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ادعای تسنیم: آمریکا از اصلاحیه‌های اخیر خود کوتاه آمده!
خبرگزاری تسنیم، وابسته به سپاه، نوشته:
متن تفاهم تا این لحظه در مراجع ذی‌صلاح  ایران به تایید نهایی نرسیده است
▪️
پیگیری‌های خبرنگار تسنیم از منابع مطلع حاکیست: آخرین تحول رخ داده این است که فشار نظامی و دیپلماتیک آمریکا برای تغییر در متن ۱۴ ماده‌ای پاسخ نداده و آمریکا از طریق واسطه قطری اعلام کرده است که نیازی به اصلاحیه‌های اخیر آمریکا نیست.
▪️
به گفته این منابع، ترامپ طی روزهای اخیر با شروع به فشار و تهدید و اقدام نظامی و از طریق دیگر با فشار میانجی قطری تلاش کرد تا از دو سو مواضع ایران را تغییر دهد که در نهایت ایران تغییرات جدید را نپذیرفت.
▪️
با این حال این متن همچنان نیازمند بررسی و نهایی شدن در نهادهای ذیربط در ایران است و تا آن زمان سایر گمانه زنی‌ها و خبرها، معتبر نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76251" target="_blank">📅 01:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76250">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">"خبرگزاری مهر" وابسته به سازمان تبلیغات اسلامی، در پستی نوشته:
♦️
شنیده شدن صدای انفجار در نزدیکی ساحل سیریک؛ جزئیات همچنان مبهم
🔹
منابع محلی در استان هرمزگان از شنیده شدن صدای انفجاری در دریا، حدود دو کیلومتری ساحل سیریک، خبر می‌دهند. هنوز علت و منبع این صدا تأیید نشده است.
🔹
منابع محلی در منطقه سیریک (استان هرمزگان) می‌گویند صدای انفجاری در دریا، در فاصله حدود دو کیلومتری ساحل، به گوش رسیده است.
🔹
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی در دست نیست، اما با توجه به دستورالعمل‌های مربوط به بسته بودن تنگه هرمز، این وضعیت احتمالی می‌تواند در همین راستا باشد.
🔹
با این حال، این فرضیه تاکنون به طور رسمی تأیید نشده است و‌ خبرنگار مهر در تلاش است تا جزئیات بیشتری را از مقامات محلی و رسمی پیگیری کند. /مهر
"خبرگزاری  صدا و سیما" هم بعدش در سه پست نوشت:
خبرنگار صداو سیما در سیریک:
دقایقی پیش صدای انجار در سیریک شنیده شد.
🔹
منشا و‌ مکان آن هنوز مشخص نیست.
🔺
منابع خبری از شنیده‌شدن مجدد صدا در محدوده دریایی سیریک خبر دادند
🔺
ماهیت و علت انفجارها در سیریک  هنوز بطور دقیق مشخص نشده اما برخی منابع آگاه آنرا مرتبط با مدیریت و بسته نگه داشتن تنگه هرمز می‌دانند.
آپدیت ۱:۱۰
پست تازه خبرگزاری مهر:
♦️
تکرار صدای انفجار در محدوده دریایی سیریک؛ علت هنوز نامشخص
🔹
منابع خبری مهر تأیید کرده‌اند که بار دیگر صدای انفجار در محدوده دریایی سیریک، در استان هرمزگان، به گوش رسیده است.
🔹
هنوز ماهیت و علت دقیق این انفجارها مشخص نشده، با این حال براساس اخبار رسیده به خبرنگار مهر احتمال می‌رود که این رویدادها با سیاست‌های مربوط به بسته نگه داشتن تنگه هرمز در ارتباط باشد.
🔹
پیش از این نیز منابع محلی از شنیده شدن صدای انفجاری در دریا، در فاصله حدود دو کیلومتری ساحل سیریک، خبر داده بودند.
🔹
با این حال، هیچ‌یک از این فرضیه‌ها تاکنون به طور رسمی تأیید نشده است.
آپدیت ۱:۱۵
تسنیم: سیریک نیست. سمت دریا است.
یک منبع در استانداری هرمزگان به تسنیم کفت:
🔹
تا این لحظه هیچ اصابت پرتابه و درگیری در سیریک وجود نداشته است.
🔹
صداهای شنیده شده از سمت دریا و مرتبط با تنگه هرمز است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76250" target="_blank">📅 00:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76249">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rEzLDG_2gU3TbEX6eZ9XBmbyaZPXOXdauZ55srXTXYCiScREdWStWnes70ixWwY4hVborJ77SS91LvGSh0zpe0CP3OFa_YH2D7hyJQsKLFvZNhVerGmKEbxwXFzCi9Kvrxmy2K041NCtrfTN3kmpsa8lBWtT51qwegI7gLtJD3bnU4cMNuyXU92pkd9NpHn2-7mCYTZUKBByg47p99npE62YtWL7AAqpii-xq2dVlgESIYMeQE5Ffcs2sHPjktjs8MYVEVMZ37uAGnyAvdUjYQcX6rhXdwDr--v7CGt0pxG0-4XHOuYNN-n9afK21YVZuHZ89HgjeAssKIJlaWQFkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابعی در جمهوری اسلامی نوشته‌اند که: با میانجی‌گری قطر، آمریکا به شبکه beIN Sports معافیت داده تا مسابقات جام جهانی را در ایران پخش کند.
تاکید هم کردند که: این امتیاز توسط دولت ایران و کاملاً جدا از هرگونه یادداشت تفاهم (MoU) به دست آمده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76249" target="_blank">📅 00:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76248">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/efef15c7c2.mp4?token=E19v7-hvMbiqABQ7AUYijN1D-3toA2VEYbpxNlod8PNeNL_GZslWWnWfx-BQlfs4FAOrgNxw5VVFtSwwxcFdE0uCdT5KXhNoQjE5DiimnGfnHrH_sF3m7OclUI2PzEC3XpdYsLk8xdddFdfbeCsIvuEnNVcVj9U_cQ8ZDyLeIDYHHyfxWrQYKw2x-SmUDRdX8j2hcg0Hmj6xSPSlGBnZF2t0oXUZBLR4YjgP0OTA7f9bAMPlmMHBtrh_v1LsXSnJ9NOR8j9DBef2IaJlEsma4mDGTwKQTkZrU5DP8S0EjfIz6T6lWGzXwjb28gjP-jZejNO0A_H4bAIjfoYcX5v03A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/efef15c7c2.mp4?token=E19v7-hvMbiqABQ7AUYijN1D-3toA2VEYbpxNlod8PNeNL_GZslWWnWfx-BQlfs4FAOrgNxw5VVFtSwwxcFdE0uCdT5KXhNoQjE5DiimnGfnHrH_sF3m7OclUI2PzEC3XpdYsLk8xdddFdfbeCsIvuEnNVcVj9U_cQ8ZDyLeIDYHHyfxWrQYKw2x-SmUDRdX8j2hcg0Hmj6xSPSlGBnZF2t0oXUZBLR4YjgP0OTA7f9bAMPlmMHBtrh_v1LsXSnJ9NOR8j9DBef2IaJlEsma4mDGTwKQTkZrU5DP8S0EjfIz6T6lWGzXwjb28gjP-jZejNO0A_H4bAIjfoYcX5v03A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره مقامات جمهوری اسلامی:
من این افراد را بسیار منطقی‌تر از افرادی می‌دانم که دیگر با ما نیستند. این یک گروه متفاوت است و من فکر می‌کنم گروهی باهوش‌تر است که منطق دارد. همه آنها توافق را تأیید کرده‌اند.
آپدیت:
بعدا ویدیوی طولانی‌تری رو جایگزین کردم که اکانت فارسی وزارت خارجه آمریکا زیرنویس کرده و شامل حرف‌های دیگری هم هست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76248" target="_blank">📅 00:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76247">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rNifOMOyclVkCCTIJ_K77hk_vg4Kc0Qhnq_IiDeLqx01S186FtcVpJ1KHDyF3YsqMYqsV18GooBZytmBzNGYO2vEMNtn-uU7ldurYNnuAfRhja1NuveqT6fQGLPiQPHUSCtvQg0CtlEwDKwhjDDri3grZxKBDW2x9ZLuiot30iqbA12Zz7742EeL3BUjnbgORHr3bBBh-RqbcIMicld_hrG-HEFZLI2ohYAadd5DTqc2oKEDpOnGvLn8Mqmtt-wKLfA3nPm4_27kgbdLA0jIF1n2xHdPHk82Hv4FEy7Vpscp4Ct52eyHXWa6DGu1HXGNkBmu5XNaYmFwkZOOf1Ye9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی در یک مصاحبه تلفنی گفت علیرغم فعالیت قطر و پاکستان به عنوان میانجی، روند دیپلماتیک مذاکرات به دلیل اقدامات آمریکا تحت تاثیر قرار گرفته است.
اسماعیل بقایی تاکید کرد که بخش عمده متن توافق نهایی شده اما به خاطر مواضع ضدونقیض آمریکا باعث تلاطم و اخلال در دست یافتن به توافق شده است.
سخنگوی وزارت خارجه در این مصاحبه گفت: «ادعاها درباره زمان و مکان توافق صرفا گمانه‌زنی رسانه‌ای است و تا مراجع ذی‌ربط نظام درباره تک‌تک اجزای متن توافق به جمع‌بندی نهایی نرسند صحبت درباره شکل امضا و مکان آن فایده ندارد.»
آقای بقایی اشاره کرد که متن توافق از پیش برای ما روشن بود اما طرف آمریکایی هربار مطالبه غیرمعقولی مطرح می‌کرد و بار دیگر تاکید کرده که ایران تحت فشار و تهدید از مواضع اصولی و خطوط قرمز خود کوتاه نخواهد آمد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76247" target="_blank">📅 00:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76246">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cGOGwThGyXEICTx-az0Jb2i8BVRao5t8hzJVgvWZna0LpQI9gW49iKZPkhYqIhUIB5hvfQKby-xY49zkfL02h8y6hgXTh8PCXv3itEwfUJkrlygN8u__1iwCOeCb_5H63w7FZmfXA-5WYA9t9amP5Q2p_GQGPRat9fNUUNsjZz_3RYeqhd6XO-jO5whZGEPYpxHBHkGHODhNHwt0l_kmC0M5mROsjU-PYCxbFcK4v4rm9Vatk4HuCXPpWxVHu0TSi3f3L1TF1fNHIVgdPzNT1TENLgiXhSt01SUMPT4THzdaYR7sPpDlrw5s9JfnHUMOlM08hkg1GFy3pxfaIG2ONg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل طرف تفاهم‌نامه با جمهوری اسلامی نیست
دفتر نخست‌وزیری اسرائیل، اعلام کرد که دونالد ترامپ، رییس‌جمهوری آمریکا، درباره یک یادداشت تفاهم در حال شکل‌گیری با حکومت ایران برای ورود به مذاکرات، با بنیامین نتانیاهو گفت‌وگو کرده است.
این دفتر افزود نتانیاهو از تعهد ترامپ درباره شرایط هر توافق نهایی با ایران ابراز قدردانی کرده، هرچند اسرائیل طرف این تفاهم‌نامه نیست.
دفتر نتانیاهو نوشت تعهد ترامپ شامل این موارد است:
-حذف مواد غنی‌شده
-برچیدن زیرساخت‌های غنی‌سازی
-محدودیت‌های تولید موشک
- توقف حمایت جمهوری اسلامی از گروه‌های نیابتی خود در منطقه
@
VahidOOnLine
به نوشته تایمز اسرائیل دفتر آقای نتانیاهو در بیانیه‌ای که «سعی در کم‌اهمیت جلوه دادن توافق احتمالی» داشت، می‌گوید که آنها درباره «یادداشت تفاهم قریب‌الوقوع با ایران در مورد ورود به مذاکرات» صحبت کردند.
به گفته دفتر آقای نتانیاهو، در این مکالمه، نخست‌وزیر اسرائیل دیدگاه نسبتا خوش‌بینانه‌ای نسبت به توافق ابراز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76246" target="_blank">📅 23:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76245">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d148f37d4.mp4?token=aH5rjcWJZheCs0GnsIcOu8G90ZJsukhXbzyq-KPasHwzc2dWsGI3_nDWZ8J3TPY6moyOY7AB8AW-OnpF-5mmzkayG-dqU0-UHUAOPPtDVVeIXF-5xf_zbsFQVNby03VVDtSuQjgsNwbP2CcJbw5aLH1Zdl2bxDKcduPlXOAxSUu5AEQFcFmTlU3AY9GtEKUpRouMCpI0neYPRejzNkDvOQST8kSdXcjKplcbYdbVcK1fpGDq9FEWFIEzUn8mU8ImpmorJjcFnQQqxYL8z7_jG_Cqn1SLeRmcaE0oSbTUoJ7DU6Nn-syqp4WRb-JnwneZYqX74wtIgdZU3OAdD5zCjw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d148f37d4.mp4?token=aH5rjcWJZheCs0GnsIcOu8G90ZJsukhXbzyq-KPasHwzc2dWsGI3_nDWZ8J3TPY6moyOY7AB8AW-OnpF-5mmzkayG-dqU0-UHUAOPPtDVVeIXF-5xf_zbsFQVNby03VVDtSuQjgsNwbP2CcJbw5aLH1Zdl2bxDKcduPlXOAxSUu5AEQFcFmTlU3AY9GtEKUpRouMCpI0neYPRejzNkDvOQST8kSdXcjKplcbYdbVcK1fpGDq9FEWFIEzUn8mU8ImpmorJjcFnQQqxYL8z7_jG_Cqn1SLeRmcaE0oSbTUoJ7DU6Nn-syqp4WRb-JnwneZYqX74wtIgdZU3OAdD5zCjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: ضرب‌الاجل شما برای رسیدن از این مرحله به یک توافق نهایی چیست؟
ترامپ: نمی‌خواهم ضرب‌الاجل بگویم چون بعدش می‌گویید من ضرب‌الاجل را رعایت نکردم.
خیلی مهم نخواهد بود چون قرار است امضا شود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76245" target="_blank">📅 23:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76244">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e75104b39d.mp4?token=ovlRf_BIC7IBfIkZ8ERZ_mav-YRtBwpmIoFPiVaji7yhLz4798OXXJxD38ks86Skil1W0wkoxEmyVWHGS6ugo-z7JXr98n_wkgnse60lDaf9sXiZIKoznWLfSh2I8gZvRrPWXW0T2_TCQDqCO30KmmzeXZ_bhIUlTps_PEZItiVzCyRVEWhQNg_yU_kY1QHIp9s1fi19K3Jw3vKopYQ6vUG5kHRE-HLzdwmOp_BN-i2Lmn95354OmE7QbdwxqTqzRy-zB8gP9Zvru5ohQyD2R3PDqxBKwoo4LwFKXDuUrJiOCHT_53GS4q60sfqOohp-SQjNm2o_WfSB9c-uwBOfig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e75104b39d.mp4?token=ovlRf_BIC7IBfIkZ8ERZ_mav-YRtBwpmIoFPiVaji7yhLz4798OXXJxD38ks86Skil1W0wkoxEmyVWHGS6ugo-z7JXr98n_wkgnse60lDaf9sXiZIKoznWLfSh2I8gZvRrPWXW0T2_TCQDqCO30KmmzeXZ_bhIUlTps_PEZItiVzCyRVEWhQNg_yU_kY1QHIp9s1fi19K3Jw3vKopYQ6vUG5kHRE-HLzdwmOp_BN-i2Lmn95354OmE7QbdwxqTqzRy-zB8gP9Zvru5ohQyD2R3PDqxBKwoo4LwFKXDuUrJiOCHT_53GS4q60sfqOohp-SQjNm2o_WfSB9c-uwBOfig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: تنگه باز است. تنگه برای چندین ماه است که باز بوده، اما شما فقط از آن خبر نداشتید.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76244" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76243">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38fa98505b.mp4?token=FNkAg0pZHRwRaYtDDb-c8u-P8v4TGgfQ80DGjxfZU9miyS6xChfANEyNDlaB8U6AXeYWpvKqW_Ltazl270RtlfqAKmZsJzAlBbMBEYmgRTuYwEdDMtdMRqcmDOeGRU37vb51e_NjJrMpKTsGx_R6h-IVWlad7Gf4aCbska2TD5EYwNukLRs71ptRTyUYGPjc0IhZHp3TzJqQgFqQVYbhiKR_YeFVt8dTW3U-WywbsvMsGxwB3tEvdxJafjvroaLWt6_Y9WgEF-9dV0C87_2q6imYIceph3w6Cq_kBhyKf6G39iEQrjXdWP9S18oYIpxVfT0BS2U7eAsjscA70RgaVg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38fa98505b.mp4?token=FNkAg0pZHRwRaYtDDb-c8u-P8v4TGgfQ80DGjxfZU9miyS6xChfANEyNDlaB8U6AXeYWpvKqW_Ltazl270RtlfqAKmZsJzAlBbMBEYmgRTuYwEdDMtdMRqcmDOeGRU37vb51e_NjJrMpKTsGx_R6h-IVWlad7Gf4aCbska2TD5EYwNukLRs71ptRTyUYGPjc0IhZHp3TzJqQgFqQVYbhiKR_YeFVt8dTW3U-WywbsvMsGxwB3tEvdxJafjvroaLWt6_Y9WgEF-9dV0C87_2q6imYIceph3w6Cq_kBhyKf6G39iEQrjXdWP9S18oYIpxVfT0BS2U7eAsjscA70RgaVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما قبلاً گفته‌اید که ایران و آمریکا به توافق نزدیک بوده‌اند. هنوز این اتفاق نیفتاده است. چرا اینقدر مطمئن هستید که این بار متفاوت است؟
ترامپ: چون آنها ضربه سختی را تحمل کرده‌اند. ضربه‌ای که کمتر کسی می‌تواند تحمل کند. و آنها خیلی بیشتر از من می‌خواهند به توافق برسند.
===
خبرنگار نیوزنیشن در کاخ سفید:
از رئیس‌جمهور ترامپ پرسیده شد که آیا می‌تواند این توافق را به سرانجام برساند یا نه، چون پیش‌تر هم به آن نزدیک شده بود. او گفت: «من بسیار مطمئنم.»
او درباره اینکه آیا واقعاً این توافق تا پایان این هفته نهایی می‌شود یا نه، با احتیاط پاسخ داد: «به‌زودی خواهد بود، شاید همین آخر هفته.»
ترامپ در پاسخ به این پرسش که آیا رهبر عالی این توافق را تأیید کرده است، گفت: «برداشت من این است که پاسخ مثبت است.»
KellieMeyerNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76243" target="_blank">📅 23:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76242">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30b9b51ccd.mp4?token=rpKHTv6rRqMTA7ENg9wDg2YY5vIHQP2nbgUrXFOEtuWq-37FtAAeWHLmzW9CdonW5WhO2zhN7f87eTfAbF2gCxHFPbss_6CMs31WAUz6eCOe2YKiitthlsWfhU1JnWctgOWbRk7q1TI8e9bLQ_-c7hGDoS3zrj1Q3a9ZKTcNILwvzsd2qwLkotwq-p29xtbtZW6-uutXJSAACgwz9bu0gMJRpwiVuaYAoDhJApCiU1X_0w655yV2jLIBMj6KbvM48KfzAzRRDpwbFJvwnv-p7MLc16FOV1T9aSulOKKEkxE6dTd_TadSv26BT9pmydKXTLVdEzfDChzzzJLyuwjxbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30b9b51ccd.mp4?token=rpKHTv6rRqMTA7ENg9wDg2YY5vIHQP2nbgUrXFOEtuWq-37FtAAeWHLmzW9CdonW5WhO2zhN7f87eTfAbF2gCxHFPbss_6CMs31WAUz6eCOe2YKiitthlsWfhU1JnWctgOWbRk7q1TI8e9bLQ_-c7hGDoS3zrj1Q3a9ZKTcNILwvzsd2qwLkotwq-p29xtbtZW6-uutXJSAACgwz9bu0gMJRpwiVuaYAoDhJApCiU1X_0w655yV2jLIBMj6KbvM48KfzAzRRDpwbFJvwnv-p7MLc16FOV1T9aSulOKKEkxE6dTd_TadSv26BT9pmydKXTLVdEzfDChzzzJLyuwjxbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ممکن است آخر هفته در اروپا قراردادی امضا شود. من نمی‌توانم آنجا باشم، اما جی دی ونس آنجا خواهد بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76242" target="_blank">📅 23:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76241">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f82f63f23.mp4?token=mqNXI54-eRwHfhDs3Gt4zpN6ORcDz8gGcUjczESgYyO8IWC8LDzev3LiusHFwbLwwYiNOE1u3rJaH2_ZzbRhQ4RjKpsM4J83T4TjXCvZxdMk1kSrUHq4oMJu9r5se-UwDhy1XibFTfz4kwiOm3BH_KblD3ecXJxvWfcCe_FmXA4UwTpOPqb3_3MBcmzLq-z6MsnBiXSaQUOJCsEi_-mCqoh7b8ElWv2EMVn-53EUJylb-2KSLdnJmytJhhTPNuSTbLdalPnZhCnQMiHhOI6hTCjAegv3eObEijEcPkvDyJNixDyygAiuufSwoInadYkKXW0Pa7pUIvjJbUlkOTZe7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f82f63f23.mp4?token=mqNXI54-eRwHfhDs3Gt4zpN6ORcDz8gGcUjczESgYyO8IWC8LDzev3LiusHFwbLwwYiNOE1u3rJaH2_ZzbRhQ4RjKpsM4J83T4TjXCvZxdMk1kSrUHq4oMJu9r5se-UwDhy1XibFTfz4kwiOm3BH_KblD3ecXJxvWfcCe_FmXA4UwTpOPqb3_3MBcmzLq-z6MsnBiXSaQUOJCsEi_-mCqoh7b8ElWv2EMVn-53EUJylb-2KSLdnJmytJhhTPNuSTbLdalPnZhCnQMiHhOI6hTCjAegv3eObEijEcPkvDyJNixDyygAiuufSwoInadYkKXW0Pa7pUIvjJbUlkOTZe7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما به زودی توافق را امضا خواهیم کرد و اسناد تقریباً در مراحل نهایی هستند.
دونالد ترامپ، رئیس‌جمهور آمریکا در تازه‌ترین اظهارنظر در خصوص توافق با ایران گفته است که ایالات متحده «به‌تازگی به یک توافق بزرگ در مورد جنگ با ایران رسیده است.»
او گفته است که «ما در حال نهایی کردن اسناد هستیم. این کار باید طی چند روز آینده انجام شود.»
آقای ترامپ می‌گوید که پس از نهایی شدن اسناد، «احتمالا امضا آن شاید در اروپا» انجام خواهد شد و این کار باید «خیلی سریع» انجام شود.
به گفته او «ما توافقی داریم که ایران هرگز سلاح هسته‌ای نخواهد داشت، که هدف اصلی از آنچه که ما برای رسیدن به این هدف طی کردیم، همین بود. بنابراین، این یک چیز بسیار بزرگ است.»
رئیس جمهور ایالات متحده تأکید کرد که توافق «به زودی امضا» انجام خواهد شد و اسناد «تقریبا به شکل نهایی هستند، بنابراین خواهیم دید».
آقای ترامپ همچنین گفت تنگه هرمز نیز «به محض اینکه آن را امضا کنیم» باز خواهد شد.
او همچنین می‌گوید که با رهبران منطقه، از جمله متحدان خلیج فارس و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، صحبت کرده است و افزود: «تمام خاورمیانه بسیار خوشحال است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/76241" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76240">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سی‌بی‌اس:
احتمالاً اوایل هفته آینده یادداشت تفاهمی بین ایالات متحده و ایران امضا خواهد شد که راه را برای مذاکرات بیشتر در مورد یک توافق بلندمدت هموار می‌کند.
CBSNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76240" target="_blank">📅 22:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76239">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iKb1S2CT6Ywknj9ya0gvgpDGZeDVGQx3XPISm0jiPjPCukK3oxkuj7zNliGq41Q9dfSDw7FUmjgyWW9qKkMCpfvAQ9dvJuinrR-TUgMC8fuwPIYf6B39t7XC0uUYLdrjrZZT8l52KByg11XYDW4MO0axE95-2raxMl4JBVlcqSqGgxBnoyPlrTcMvS7jy6BLvcOQuPghkpXh02Ym9b9q5m1-1RMAMCnZX3PiATQ_02Uy-2FNMqrz4bSrFGHPEziiJSAgMBWHVMqvSjQuCKJIAgqN94BoYTvvdVw4o9XnxX2rRaxX-2F7W20gvLUp_8LRpG4U74ZaMy_7Yf93CEGfGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس در پستی جدید نوشته:
"بنظر می رسد با توجه به اینکه امریکا متن پیشنهادی ایران را پذیرفته است احتمال تایید این متن در مراجع اصلی‌نظام بالا است‌."
🔄
آپدیت:
خبرگزاری فارس جملات بالا که در انتهای پست نوشته بود رو تغییر داد به:
"البته بنظر می رسد با توجه به اینکه امریکا متن پیشنهادی ایران را پذیرفته است احتمال بررسی مجدد این متن وجود دارد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76239" target="_blank">📅 22:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76238">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vieaoy_txIs4eAIkZ9enq41iLVz2K116Qe4x4RgBkjlMk9AizCaLr09rnD6D2QYyOts2xrHBXBOvVVPhppAcDaRlD65ZLtEdFbD5QpKWAEQFFWtawNrz_uZvuQQNzm9tQCbzb8_16R1jYa7Awz77EUPIufo4c4tNBdAdaxvdjiwZRIby-m3LCsKNxueWBruK5n35XDltdDMTBDiEfTWd-iVe8S13AQa3D1U5hKm2JbcT-_kDMZ7L3lR_6kj3pNIpzrLAMa2mC2nDF72ghqXbbXWBk46DonVtGdRyubkKVWrNWj8DqUXxRF52RBCXrfKmRBmjqLEttI5ok6qt3OdDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحدث به نقل از یک مقام ارشد گزارش داد هیات قطری که از تهران بازگشت، موافقت جمهوری اسلامی با پیش‌نویس نهایی توافق را اعلام کرد.
همچنین دفتر امیر قطر اعلام کرد که تمیم بن حمد آل ثانی، امیر این کشور، و دونالد ترامپ، رییس‌جمهوری ایالات متحده، پنج‌شنبه در یک تماس تلفنی نتایج رایزنی‌های آمریکا و ایران را که به پیشرفت در تفاهم‌نامه پیشنهادی در چارچوب یک مسیر مذاکراتی منجر شده بود، بررسی کردند.
دفتر امیر قطر در بیانیه‌ای افزود که ترامپ به امیر قطر گفته است تلاش‌ها برای تکمیل مراحل نهایی پیش از اعلام ترتیبات مربوط به امضای یک توافق ادامه دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76238" target="_blank">📅 22:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76237">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نیویورک‌تایمز: ‌قبل از لغو حملات برنامه‌ریزی‌شده به ایران در روز پنج‌شنبه، ترامپ با میانجی‌گران پاکستانی صحبت کرد که به او گفتند با ایران «توافقی» دارند.
clashreport
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76237" target="_blank">📅 22:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76236">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iLN7fGUxREZdK0XoSRSgj0y216bJjXBIPo2_1AWMH_c1C4y4P1VF3_p9h7D4UDi3uiPxItSf64WpbPq8YcHTxxbPQkl8-YxHHrPYCDd9GjpGXBO4NS-CXHjqKPEAYcaEXDUDUZTNeidQ-Wjl1s1hhSd_cihkhyjqdh66QuKmDTcFJLiTsuQCYM0fLAE7jLQB6ajn8y5UZfjdQz8rQ1USdxfoZ5Ny6qq5omhP_Ui9o1emqjdaiS_xB5HgeNiUSlqMN5-BRflmCEIxVX1kIpHyzxyFXminuBFvBPsHzghNY7WhU-fqdjzHzAjHcrtD4L6N4n03v3kbqmOALBclbbWIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع اسرائیلی گزارش داد پست دونالد ترامپ در تروث سوشال درباره نزدیک بودن توافق با تهران، بنیامین نتانیاهو را غافلگیر کرد؛ در حالی که او در میانه یک نشست امنیتی درباره ایران حضور داشت.
سی‌ان‌ان افزود که این کشور از وجود هرگونه توافق قریب‌الوقوع با جمهوری اسلامی یا تایید آن بی‌اطلاع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76236" target="_blank">📅 22:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76235">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/loAeDLjGIJoFYNu40pyi74v-cP4xIoOYH0ZDsISSGAR7cbGOzD7D81FE6_YTUtQFgirpbQZ25uiUUDnfOIogCR8hLNHsFqjMQxIn3Rc0RA97rmo-9wqQyWZUlM-Ttlq84T8S8zOLp9IRaelngO5InEOyewcr1kscpzd3kfI5-LKit1MDFhzl_uM3ZZu4cwDY3tRw9f3W97hrchTtfDyrxxvS7HfEL7d-7mMt9VlKQdOLfkmOo8OFX9H0je8ow6R_7fYp6cV5TI4QV0IVBOjezvXmuPof60SKsR4xo4TkTtsNnHFztVxnW_tObyQ4FCO4jDDPEPzoDoag0LTaaXm_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران، ساعتی پس از پیام دونالد ترامپ دربارهٔ مذاکرات با ایران، مدعی شد که «هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تأیید نشده است».
فارس ادعای خود را با استناد به اظهارات «یک منبع آگاه نزدیک به تیم مذاکره‌کننده جمهوری اسلامی ایران» بیان کرده است.
رئیس‌جمهور آمریکا گفت: «زمان و مکان امضای این توافق به‌زودی اعلام خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76235" target="_blank">📅 22:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76234">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R_s9HGOFZArr_IC6e-jGx0ZVsRJDVkmz-wFd6xOj0Tw0nY-PxFeA6HUmuDT6BVPmTx7eJ2-6vdLai3_ASUrJ__x2yrDLnLkMye5Lt2Bz763iNIVnBN_x7KHVAXgPFr7dITVDq4sdsr39OGKy8Q_cMe4N3Ewa4OxN_MsEXeFjVBnKLkb6izA6ZmGxCUz0D06xDu373AtfpPoDkmCpftb1l5pMKl6eCc3vK-LMBiv13_3IIVB2NQXOqQ_rV_q0wxQdWy1WVI5XyxbfeWBLa2pKBtaZU_CBOMr3x2EbfLNHEI8ecIf6J0uu9NJJEr_6ui3o8ORHcmAXmeTzHyY9lFekZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از سه منبع آگاه گزارش داد اختلافات اصلی تهران و واشینگتن برای رسیدن به یک تفاهم‌نامه، چهارشنبه در جریان گفت‌وگو میان مقام‌های جمهوری اسلامی و میانجی‌های قطری برطرف شده است.
بر اساس این گزارش، مقام‌های ایرانی پنج‌شنبه به چند کشور اعلام کرده‌اند مذاکرات تهران به توافقی اصولی منجر شده، اما مجتبی خامنه‌ای باید تایید نهایی را صادر کند.
این منابع خاطرنشان کردند که هم ایرانی‌ها و هم قطری‌ها تاکید کرده‌اند که حملات آمریکا در طول شامگاه چهارشنبه، تردیدهای ایران نسبت به نیت واقعی ترامپ را به شکل قابل توجهی افزایش داده است.
@
VahidOOnLine
ترامپ: توافق تقریبا نهایی شده
ترجمه ماشین:
... نیویورک‌پست نخستین‌بار گزارش داد ایران چهارشنبه‌شب پیش‌نویس نهایی یک توافق را به میانجی‌های قطری ارائه کرده است.
رئیس‌جمهور ترامپ روز پنجشنبه، پس از اعلام اینکه حملات برنامه‌ریزی‌شده علیه ایران را متوقف کرده، به نیویورک‌پست گفت توافقی که مدت‌ها انتظارش می‌رفت برای آغاز مذاکرات هسته‌ای با تهران «تقریباً نهایی شده است».
او در یک تماس تلفنی کوتاه با نیویورک‌پست گفت: «تقریباً همه‌چیز نهایی شده است.»
nypost
سی‌ان‌ان به نقل از یک منبع آگاه گزارش داد مقامات آمریکایی بر این باورند که نشست‌های این هفته میان مقامات ایران و قطر در تهران، به حل برخی از نقاط مبهم و کلیدی باقی‌مانده در توافق با ایالات متحده کمک کرده است. این اختلافات عمدتا شامل جزئیات نحوه پیشبرد مذاکرات آینده در قبال برنامه هسته‌ای ایران و ترتیب زمان‌بندی لغو تحریم‌ها و گشایش‌های مالی برای تهران بوده است.
بر اساس این گزارش، ایران اواسط این هفته جدیدترین پیش‌نویس توافق پیشنهادی خود با آمریکا را از طریق میانجی‌های قطری ارسال کرد. این در حالی است که حدود دو هفته پیش، دونالد ترامپ با اعمال تغییراتی در متن، خواستار سخت‌گیرانه‌تر شدن لحن توافق در بخش هسته‌ای شده بود و از طولانی شدن پاسخ ایران ابراز نارضایتی می‌کرد.
با این وجود، رایزنی‌های این هفته از طریق قطر باعث کاهش شکاف‌ها شد. مقامات آمریکایی در تمام این مدت در تماس مداوم با میانجی‌ها بودند؛ حتی در روزهایی که واشنگتن و تهران به طور پی‌درپی در حال تبادل آتش و حملات نظامی به یکدیگر بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76234" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76233">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XowV3nKj16XwrVoAJsmWFRTRz53U2QrjjlwY4lRYCPIKA9mZMiRY1tN80TZDrnw-uAhpba2JJHUMVkrD3fCUh7iZfx_JlDcsehcPqn4r_2WTpYbiFc8u218OpxzCdqLANL5KYTmhlLm1JaUJf7ShTDPoe2AxUFF-2V7ITy-EvIbRAYnWLZRWkp1KOv579_ziyQmEu8zKntKoIjRWPzzxQRs8HbjF6sEbT_3X3RkOmxOvvv4zCkn71OkbVmUQmwb7aHWnwexTvIeuTOFUk9TTqXCIo-1ZKUqsX_eQFM_fohAKfw_YjbGRgYF3OPujrpDwVnIj5wRKS6zbSaHELR-j_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: حمله امشب را  لغو کردم چون بالاترین سطح رهبری در جمهوری اسلامی توافق را تایید کرد
پست ترامپ، ترجمه ماشین:
با توجه به این واقعیت که گفت‌وگوها با جمهوری اسلامی ایران به عالی‌ترین سطح رهبری ایران رسانده شده و مورد تأیید قرار گرفته است، من، به‌عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده علیه ایران در شامگاه امروز را لغو کرده‌ام.
گفت‌وگوها و نکات نهایی، هم در کلیات و هم با جزئیات فراوان، به تأیید همه طرف‌های دخیل رسیده است؛ از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران.
محاصره دریایی تا زمانی که این توافق نهایی شود، با تمام قدرت و به‌طور کامل برقرار خواهد ماند — زمان و مکان امضا به‌زودی اعلام خواهد شد.
دونالد جی. ترامپ
رئیس‌جمهور ایالات متحده آمریکا
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76233" target="_blank">📅 21:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76232">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzVhS_ZZ3MlmJK_NbShJx1-Lwl2pn43PEB9_xhiNa_MAopI3bp2IRTdWHdYq2TpQ9Z1tXO6Sev0dnQszfEcoLug8QozIn_Oj8jyj0hBsyeiHzfmwQehDN3LO2mTXO6FvXLwfvaxRMVJxSmE-PLMoUVewV3wBhMeYaU9Bzc21WurFDuTEjtv7iX2G9Y-Ybb-vNvYTuSe67ob-__kwJvF6XKWdxDumN3yaFkwStURsJC06jFSByARbH3Qt8YXI85eH3SSzdQk9S_GTFmkQ_9OrvA_Ukv6Re32oqSaqKLuNgFBUBscde_xX3fe9m-IzvesQB21g0dRqf8RUTRo-2YrbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، در گزارشی اعلام کرد ایستگاه‌های زمینی استارلینک در اسرائیل، قطر، اردن، امارات و عمان به همراه سهامداران شرکت اسپیس‌ایکس و زیرساخت‌های شرکت‌های «الفیظابی» و «مبادله» به فهرست اهداف نظامی جمهوری اسلامی ایران اضافه شده‌اند.
فارس مدعی شد این تصمیم پس از به دست آمدن شواهدی مبنی بر استفاده ارتش‌های آمریکا و اسرائیل از زیرساخت‌های تحت مدیریت ایلان ماسک، از جمله شبکه اینترنت ماهواره‌ای استارلینک، اتخاذ شده است.
بر اساس این گزارش، «ایستگاه‌های زمینی استارلینک» در اسرائیل، قطر، اردن، امارات و عمان، به همراه سهامداران شرکت اسپیس‌ایکس و همچنین زیرساخت‌های شرکت‌های «الفیظابی» و «مبادله» در فهرست جدید اهداف ایران قرار گرفته‌اند.
فارس نوشت: «ایستگاه‌های زمینی استارلینک واقع در اسرائیل، قطر، اردن، امارات و عمان، به همراه سهامداران اسپیس‌ایکس و همچنین زیرساخت‌های دو شرکت الفیظابی و مبادله، از جمله مکان‌های جدید در فهرست اهداف ایران هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76232" target="_blank">📅 21:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76231">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rR410CAPwjGv8F3tevWHeTplfIG7SbNBbJTBnNwj-cX-GVK1srH40j6WbGL0wjTRKZREbrBm3PT8b7J5_yaXcnNsGeRreqmXL0rE7RZoSgGhiyDGmKQ2i4pxGTxbLVLjykfgwtc6_LGQD92uWijiTIx3hr77jbiZC_jYtYmH9tpKqJd0vP5Xk37eyJcRkb7laQl2if56b8qGp8alz3J8Rht4_T09jVagiUu01yYPWqp4EA4kbx1r5rUSoan2xttAbigFYbQgkOcyKpkM-NWZkjSWe1r9DarsjAzj7tHCuRb3SMNtFo2zVDfAnxSOwQeIJ0w8Gk2iy0bBLTk4I6vM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع جمهوری اسلامی در بیانیه‌ای اعلام کرد «هرگونه خطای محاسباتی یا تعرض به امنیت و تمامیت ارضی کشور با پاسخی قاطع، پشیمان‌کننده و فراتر از تصور غلط دشمنان مواجه خواهد شد.»
در بخشی از این بیانیه آمده است: «بی‌تردید نیروهای مسلح جمهوری اسلامی امروز از آمادگی، توانمندی و قدرت دفاعی قوی‌تر از گذشته برخوردارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/76231" target="_blank">📅 20:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76230">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HbjIyFchXZ_-qr5Ksj7S-Qf7Ii5np3GASJS4R4UWapcIZcj8362lIeDt7fMDjkK58HmnuXhca7aasZ9pkIWd8E2Fge5153fCGvogIgjFqQ-5qdVDhxiSq1CLpcS77GxmsWJqp4HgZqGlxMHYWwTM4b0xpkhrJxLnKeNKKqQGY_OGvpY5mRW_ldfOH7_dD15TpckeVfaxTZciCODKiKUdPFn2UIOycMhfZoVzuJ6W41skGuQODG3vbHHZqmYKNktUdQs0a-R6XgDK8Iupnj0OqJ0uZReeP3s3GH70GRSPERFdbAc4aA9yMycam1RfwEngsLx6UB1NM4xjkEP0WyKl4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، در خصوص تهدید زیرساخت‌های نفتی ایران از سوی دونالد ترامپ گفت: «یا صادرات نفت و گاز برای همه برقرار خواهد بود یا برای هیچ‌کس امکان‌پذیر نخواهد بود.»
او ادامه داد: «در صورت تکرار حملات آمریکا، پاسخی شدیدتر خواهیم داد و آتش جنگ می‌تواند گسترده‌تر شود.»
فرمانده قرارگاه مرکزی خاتم‌الانبیا اضافه کرد: «تناقض در گفتار و رفتار آمریکا عامل اصلی ناامنی در منطقه است و امنیت تجارت بین‌المللی، به‌ویژه در تنگه هرمز، را به خطر انداخته است.»
او گفت سران آمریکا با «عدم شناخت ملت ایران و نیروهای مسلح» در دور باطل قرار دارند و با جنگ رسانه‌ای نمی‌توانند «شکست‌های پی‌درپی» خود را پنهان کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76230" target="_blank">📅 20:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76229">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WBX9Sp2WVjXDNyzC5Hkv7coFw4UmTPE_9Ui0VNrKChplPCe_IygTaTHJj4k0AzmIbrCizKaoTYO22Z04C6-eqi-oCb3n0ChGHKwOxiiEA-qnzKzJKe4n0EBJH1y2HPzgDgDSkRTAqJEz8D9m0Mfct5hT7WoelSaGK6HNVC90XAWGjhtLAplErREvauANwcwDT6V-w-kMhwBrq7s39Gj8o0zfKyS4y7CO8rwbxVVBezQG0r8goUXBYzSWCMMphgECAJaENlVBgHwTuP9-hsci82Lb5lolLIE2JrdkG2SYUut0aiwuRgM_lsNITWjrh-K4dDi0PEPDwc-zFeszVbyfZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
"تنگه هرمز برای عبور و مرور باز است
مسیرهای امنی برای کشتی‌های تجاری که از تنگه هرمز عبور می‌کنند ایجاد شده است.
این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.
صدها کشتی در دو ماه گذشته از این مسیر عبور کرده‌اند.
نیروهای آمریکا برای دفاع در برابر تجاوز ایران در موضع آمادگی قرار دارند.
ایران کنترل تنگه هرمز را در اختیار ندارد."
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76229" target="_blank">📅 20:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76228">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a8d3934df9.mp4?token=pZ3eECxx3wO1JkB3emJL7KNGXX0T241kihdrsbJvYNBOavkEOrYgex4-M_7Ml1rHw7KhlhWu1TM6hYdFW2ZYjOiXG_Wz0BjpSaOiBZe02qukpBkxUYT3bCwFiYRzVp3mbhbD_vznoO8bBEN7v8lgKW906jrvmDxzrVybAmlznptxEpJm20EqNM37K6Bjvbb1SIHJ6ujcV3baFV333_ZaaeaZrodV-hq_3Ur5dRDmVFSX5y2s-HkbHZGLiS_7XapBjR-QedGXs3Yv8Tjy9EJUp3T_EcweOZyWxl4erioFkRlxhn4yr3-SzfIA-kQ3E42JU5hHnZgGJA51LNPmo6wAjbjwN7p8m3QjKWH9AOO4qgPA0ueNRWXbQuPJ-QPmobbTJW4omMps9Wb2bgY67y7CmFKVWXgWQArn3RlmEx7aG9PLd5mbmUHBTW6ReAjJyOfP6arNVQJJQMOJFk8g3G-e4kO-nf9lRuJ59-pqNa1NlLZKKgtFTc5A8mCPEme-81tMr7iygmOsE0xN7G8onOse8moYWavHuSZgeinodSEtMSj0ZlVl6mZ0E3c8iwezQNN6AUeh1kUoNvD8L4hmhPbQkNI0ec48yc6dF8r4LelaKYy2UViA0zL0psxfNhbfyjs26HOM_5EpEB-3ZO_gaMhAsT373Ab3Wc9cCEPmDEkzjUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a8d3934df9.mp4?token=pZ3eECxx3wO1JkB3emJL7KNGXX0T241kihdrsbJvYNBOavkEOrYgex4-M_7Ml1rHw7KhlhWu1TM6hYdFW2ZYjOiXG_Wz0BjpSaOiBZe02qukpBkxUYT3bCwFiYRzVp3mbhbD_vznoO8bBEN7v8lgKW906jrvmDxzrVybAmlznptxEpJm20EqNM37K6Bjvbb1SIHJ6ujcV3baFV333_ZaaeaZrodV-hq_3Ur5dRDmVFSX5y2s-HkbHZGLiS_7XapBjR-QedGXs3Yv8Tjy9EJUp3T_EcweOZyWxl4erioFkRlxhn4yr3-SzfIA-kQ3E42JU5hHnZgGJA51LNPmo6wAjbjwN7p8m3QjKWH9AOO4qgPA0ueNRWXbQuPJ-QPmobbTJW4omMps9Wb2bgY67y7CmFKVWXgWQArn3RlmEx7aG9PLd5mbmUHBTW6ReAjJyOfP6arNVQJJQMOJFk8g3G-e4kO-nf9lRuJ59-pqNa1NlLZKKgtFTc5A8mCPEme-81tMr7iygmOsE0xN7G8onOse8moYWavHuSZgeinodSEtMSj0ZlVl6mZ0E3c8iwezQNN6AUeh1kUoNvD8L4hmhPbQkNI0ec48yc6dF8r4LelaKYy2UViA0zL0psxfNhbfyjs26HOM_5EpEB-3ZO_gaMhAsT373Ab3Wc9cCEPmDEkzjUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما هواپیماها را وسط تهران به پرواز درمی‌آوریم و آن‌ها حتی خبر ندارند. تمام رادارها و پدافندهایشان نابوده شده. آنها تمام شده‌اند... برایشان سخت است چون مغرور هستند. ۴۷ سال قلدر خاورمیانه بوده‌اند...
ویدیوهایی است از
این مصاحبه فاکس‌نیوز
با ترجمه و زیرنویس هوش مصنوعی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76228" target="_blank">📅 20:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76227">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKY1-kGSL67-tPSVAmnrS-iC4392czpBm8hNMZ_H1skXxJopw5mvxyh5uQuHeClbhu1CRk9Kg-Lh_gIK68oE8Nb32NrvVzAdZkoxgUmGdXdQGyiiRcLAvGZZUcF4wl4BUHys2_opDq78-w75MnM9Xar4iCi10be3wTn7LSQwz47eIG72U61EP5bhEoIX9OIODU6cctzqeDnVtDXozedO0aMQ6l4c4JnRmgRAgTHcsUAphjskbRTt5HwNzQdEkoOXuoKbb-4QrMHGf3xxCJogth8wXGzsHusldVWopaP7gjgo1v1Ce3Pda8oyqEhqO1hgKvBWB2DTr9TIDaipKV2M2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ به نقل از «منابع آگاه» گزارش داد که مقام‌های ارشد امنیت ملی امارات متحده عربی و ایران برای نخستین بار از زمان آغاز جنگ آمریکا و اسرائیل علیه تهران، حضوری با یکدیگر دیدار کردند.
این دیدار که در هفته جاری انجام شد، به نوشتهٔ بلومبرگ، نشان‌دهندهٔ چرخشی قابل توجه در رویکرد دو طرف است و در شرایطی صورت می‌گیرد که هر دو کشور بیش از پیش به اهمیت روابط دوجانبه آرام‌تر پی برده‌اند.
این خبرگزاری می‌گوید که منابع آن به‌دلیل حساسیت موضوع نخواستند نامشان فاش شود.
بر اساس این گزارش، رهبران امارات می‌خواهند برنامه‌های بلندپروازانهٔ اقتصادی خود، از جمله سرمایه‌گذاری میلیاردی در افزایش تولید نفت و ایجاد مراکز دادهٔ هوش مصنوعی، بدون اختلال ادامه یابد. این رابطه برای تهران نیز اهمیت دارد، زیرا امارات پیش از آغاز جنگ یکی از بزرگ‌ترین شرکای تجاری تهران و مسیر مهمی برای انتقال نفت تحریم‌شده ایران بود.
به گفتهٔ منابع بلومبرگ، تماس اخیر ابوظبی با ایران عمدتاً با هدف دستیابی به نوعی تنش‌زدایی با حکومتی انجام شده که آن را دشمن می‌داند.
از زمان آغاز جنگ خاورمیانه در ۹ اسفند پارسال، ایران بیش از هر کشور دیگری امارات را هدف حملات خود قرار داده است.
ابوظبی نیز در چندین نوبت پاسخ داده و در میان همسایگان عرب خود تهاجمی‌ترین موضع را در قبال ایران اتخاذ کرده است.
با این حال، به نظر می‌رسد امارات اکنون مسیری مشابه قطر و عربستان سعودی را در پیش گرفته که با وجود هدف قرار گرفتن توسط ایران و نیروهای وابسته آن، در پی کاهش تنش از طریق دیپلماسی هستند.
به نوشتهٔ بلومبرگ، عربستان که تأسیسات انرژی و پایگاه‌های نظامی‌اش هدف قرار گرفته، از اوایل ماه آوریل تماس‌ها با تهران را در سطح وزیران خارجه از سر گرفته است.
قطر که تأسیسات بزرگ گاز طبیعی راس لفان آن هدف حمله قرار گرفت، بیش از همه در پی آشتی بوده و اواخر ماه گذشته میزبان هیأتی از ایران شد و به‌طور فزاینده‌ای به‌عنوان میانجی میان واشینگتن و تهران نقش‌آفرینی می‌کند.
بلومبرگ تأکید کرده که هر سه کشور عربی به ضرورت همزیستی با همسایه‌ای در آن سوی خلیج فارس، با جمعیتی ۹۰ میلیونی و توان نظامی قابل توجه، واقف هستند؛ حتی با وجود خسارات گسترده‌ای که از بمباران آمریکا و اسرائیل متحمل شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76227" target="_blank">📅 19:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76226">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs9FCMCM4AvBHHB42IFrBJBftVqA1aFxGGWEjaN8ZcFD5gIbnTJOAe68iAE5Vbs51IrIR7azmA9hqWVHb6tpjr6d2n_n6ea4YTf9Q3VjnlmVTbkcdwsULGQ27P5ZhWo3SYVQGu4f4-1TD4jOJB1s07aZdBR3_OQdZTBGJXkGwjmb1KNNrLH-lwoTEvDD7NEIcUAJdV977NkpFMPeE6gzyvA16iW3YOcQ0pahIiCfJz4Kjqcff1mGGFrANoA0syoSSOgP3crUDHwJPHiL3VYYJAk3sc0hVUlxc0Zuk8ThDEoulFs_vtH-mPP626RCJqcWecV6kJRd24JAp7Otyop1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبری سی‌ان‌ان روز پنجشنبه به نقل از یک مقام ارشد پنتاگون و دو مقام دولت آمریکا اعلام کرد که طرح‌های ارتش ایالات متحده برای تصرف جزیره خارگ در جنوب ایران از «ماه‌ها پیش» تهیه شده، اما به دلیل «بیش از حد پرخطر بودن» کنار گذاشته شده‌اند.
دونالد ترامپ، رئیس‌جمهور آمریکا، ساعتی پیش از تمایل خود برای در اختیار گرفتن این جزیره به عنوان یکی از مهم‌ترین زیرساخت‌های صادرات نفت ایران خبر داد.
سی‌ان‌ان به نقل از مقام‌های آمریکایی نوشت: «دیدگاه غالب در کاخ سفید و پنتاگون این است که تصرف جزیره خارگ یا نابود کردن زیرساخت‌های انرژی این جزیره، عملاً ایران را ورشکسته خواهد کرد و توانایی‌های آن را تا حدی کاهش می‌دهد که دیگر قادر به ادامه جنگ نباشد.»
در عین حال مقام‌های دولتی به رئیس‌جمهور آمریکا گفته‌اند که چنین عملیاتی نیاز به نیروهای زمینی پرشمار خواهد داشت و «ممکن است به تلفات سنگین نیروهای آمریکایی منجر شود».
سی‌ان‌ان ادعا کرده که پنتاگون و کاخ سفید هرگونه اقدام برای تصرف جزیره خارگ را به عنوان یک «گزینه نهایی» در نظر گرفته‌اند؛ اقدامی که به گفته مقام‌های آمریکایی «می‌تواند موازنه جنگ را تغییر دهد، اما هزینه بسیار بالایی خواهد داشت».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76226" target="_blank">📅 19:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76225">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mtwESTIOkR0GtpT0oUX1i1CgEj58NES29ZRJ-HnpdZq2eVQ_afSpgvMdTauGcfyqil3JpNXhRz6xjE5fUX0XGyCc3VvM-1JdQhNcw7OVVuzdwpU3e6xKbNCiV2CkxyKrXIRXmT4qcmC7CoHi9naClCOcJ_qp892R1ZMZvvDkxyWZTuZ4K7GJo763UGETD17cCr5GNCDJoQ4tM5mR1gP5Fn9LkihGj0fBwI_1frRL-Kqot4skmfl8mgo4w9H5CkjaE6riGHQ2b4PTFCtPRC_NX4DQt45uLY8G3jqet-Q7nJm24BbWW83r5IcSFFlhDxNigrJvq0E-trBojkJtH4M04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف، ترجمه ماشین:
راهبردهای نادرست و تصمیم‌های شتاب‌زده، کل صحنه را به شکلی بدتر از نو تنظیم خواهد کرد، زیرساخت‌ها و بازارهای انرژی را منفجر خواهد کرد و باتلاقی بی‌پایان خواهد ساخت که سال‌ها در آن گرفتار خواهید ماند.
شما با ایرانی متفاوت روبه‌رو خواهید شد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76225" target="_blank">📅 19:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76223">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3AKE5xVFL3N1pOG93nsSSqg-NYT4OhwMTkkzW0Zel1hcvrZhJJcIPZYznX3YgL_9XaKQ-MBaLTz-JyrB0G6Zp6D-waynfphC2EGi_Va0Cby2kytEzbKokWsn6DPbZjRtyoy-mEfNh1WHXQ06oBmSweq6ya0bgxDOOZ5-0w8uY3TQYmlZ-gMBgFcZcmF5qrGEpuMyddXrFEhl9iPHtZNbfIMb3krxeYl6o17eSNZEm-0--2dtc0HLUE4BJ2hYhy-SfSGWT3KfDsUYoFES8jg_C8nkxicGCXLObptM8QGuVawN-nLCH2tQ14nzPaKwRwwB-MnB4xdxjhRhewisfmXNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقامات آتش‌نشانی و امداد و نجات شهرستان آرلینگتون در شبکه اجتماعی ایکس اعلام کردند که ماموران آتش‌نشانی در حال بررسی حادثه‌ای مربوط به مواد خطرناک (Hazardous Materials) در ساختمان پنتاگون هستند.
شبکه خبری سی‌ان‌ان نیز به نقل از منابع ناشناس گزارش داد که این ساختمان تحت قرنطینه و تدابیر شدید امنیتی قرار گرفته و کارکنان چندین طبقه از آن تخلیه شده‌اند.
در همین حال، سخنگوی پنتاگون در این باره اعلام کرد: «پنتاگون متوجه مشکلی در کیفیت هوای ساختمان شده است که تا زمان تعیین میزان اهمیت و خطر آن، اتخاذ اقدامات پیشگیرانه را ضروری ساخته است.»
او در ادامه افزود: «وزارت دفاع در حال اجرای پروتکل‌های حفاظتی استاندارد است؛ این اقدامات شامل صدور دستور پناه‌گیری در محل (Shelter-in-place) برای بخش‌های آسیب‌دیده ساختمان می‌شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76223" target="_blank">📅 18:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76222">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک صداهایی شنیده شده. گویا بیشتر در غرب تهران
پیام‌های دریافتی:
سلام وحید پونک سردار جنگل همین الان انفجار وحشتناک
۱۸:۲۹ یه صدای وحشتناک سمت پونک اومد
داداش صدا اومد الان، هوا هم ابری نیست، شمال تهران
سلام غرب تهران (صادقیه) ۳تا صدا اومد
توی پونک اشرفی اصفهانی صدای انفجار اومد
صدا میاد شدید ولی هوا صافه
سلام وحید جان
تهران ساعت ۱۸:۲۹
صدای چندین انفجار پشت سر هم
من از محدوده تجریش شنیدم
سلام‌ وحید جان
خیابان جلفا ۲ تا صدای انفجار اومد از دورتر
ساعت ۱۸:۳۰، ۲۱ خرداد
اندرزگو یه صدا خیلی دور اومد
شبیه رعد وبرق ولی ابری نیست
سلام آقا وحید تهران انفجار شد یا توهم زدیم؟
میرداماد همین الان صدای انفجار اومد
سلام وحید جان ساعت ۱۸:۱۷ ما سمت مختاری هستیم اول خیابان ولیعصر صدای انفجار اومد ولی خیلی نزدیک نبود خیلی هم دور نبود
صدای موشک و‌انفجار بود انگار
نمیدونممااا من از صداش خواب بودم خوابش رو دیدم بعدش بیدارشدم صدای انفجار شندیدم
من غرب تهرانم بقیه رو چک کن
سلام وحید جان اگر گزارش صدا از  تهران شنیدی ۹۹٪ رعد و برق هست ابر خیلی کمه مردم فکر میکنند انفجار هستش
آپدیت:
گویا صدای رعد و برق بود.
بلافاصله بعد از انتشار پیام‌های بالا یهو ده‌ها پیام اومد که صدای رعد و برق بود.
آپدیت: حالا بعد از این آپدیت هم شهروندانی دارند عکس می‌فرستند که هوا به این صافی رعد و برق کجا بود.
ولی برداشت نهایی من از اون همه پیام‌هایی که نقل نکردم همون رعد و برقه. آسمون هم همه جا صاف نیست.
آپدیت: بعدش هم برای خیلی‌ها که شک داشتند واضح شد که رعد و برق بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76222" target="_blank">📅 18:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76221">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15a23ead45.mp4?token=IjAFDBa1n2DBYsBC82YYjc2hZiPOhERalkbkmWORDoKQwnIXYhqRGvLagtJeEyH8OZX918rLJH60-awUzKGvFjQa-LFvwXtrgqunmxv9qOOwHaCbFsDpM_7lOhf-vHUsJKs3oV7kdFbNgyRMwJvVUj49PEPgD_C0LZmw3GML7w3mQuI95z0JMK0QeNdtRm_xAmXuWg-Y2VLmnMNl8ktI9eQx6sN_-rgMjtdtVVFObkvG_iicc43uOhrnBd3LBgdlcBrrbt87Ql7aYTfMJfA5pE9PAThrL3ybj6W9MWRJniO6wAzmSghpF5dYDaoIK5AqzWcQcyBQ-5hI4YxmL8wHXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15a23ead45.mp4?token=IjAFDBa1n2DBYsBC82YYjc2hZiPOhERalkbkmWORDoKQwnIXYhqRGvLagtJeEyH8OZX918rLJH60-awUzKGvFjQa-LFvwXtrgqunmxv9qOOwHaCbFsDpM_7lOhf-vHUsJKs3oV7kdFbNgyRMwJvVUj49PEPgD_C0LZmw3GML7w3mQuI95z0JMK0QeNdtRm_xAmXuWg-Y2VLmnMNl8ktI9eQx6sN_-rgMjtdtVVFObkvG_iicc43uOhrnBd3LBgdlcBrrbt87Ql7aYTfMJfA5pE9PAThrL3ybj6W9MWRJniO6wAzmSghpF5dYDaoIK5AqzWcQcyBQ-5hI4YxmL8wHXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'لحظه انفجار حمله حدود ۴ صبح به پیشوا در استان تهران'
ویدیوی دریافتی، پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76221" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76214">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jAxIDLllWdMBwL6Tf7lZMXRvxF7fO6pTm7VsW5mU5DhsjOrhs_ugRww3K3CDrEd2OregXRVPsTHIcd_nYDHo65q4PFbGGuvBhpkU-KW9Aq_fKEburgvUcL4mHlBaLycIWnrtl1DwfCAitC-n9Z8TUfRbhwB-EDfuFjYB-nugIOvAChuSEISal0wGkO3_sg83R5W8u7q6O-0tJ05q_OUZqCH1WOD00ratA1X4ARFnG89CqrY51dk0FrBD02AG2EjzDzw5Vkf1QbhdJ99lvko1jdisnIBK_iJo2ME8cBVCpukqsCgUqSvphZqKnH85pL_TINP8AU2n6myCSic3L7R6Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gggl86_oWyBV-F5cLSZwTGmJgoh3OWrcZvheUfqEIigShNIjLxQDRD4s5NAPbevKszyek3dsNre04qN-ffKtLOIj-mtQ53lFwOUYfHFD9z6qIj_lWvhmwlCpou229Cpl0SjVF4YfcgSPgI3ahNpwmVSPj1ultGoWUIllRn4SljFBSVQrRe6w2ThqsOQiHO1cK4kYnNSsh32pWE7gXPBGiHKEXz_XYBejHf56FYvFxS3izzv2pO5qEqlg9ZyrHWmFFJYclOlOCStjyv9sn0hDx6kY4QTw-tVjzsSm595cXWRq0uv-NLJeifVn2yx9fu_GijOBpUxkmK990V6nS4KKIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pqc-7Lw2DYaG3KHmskR8ePSRgyIM2KR2Y4h68ufaP-6mC9RAK4loAj-uH_kVhOPpGZEz3oCeuxguLUrMf69uIenMC_W2HX9l8891JKO1uSg-3qFywyNMmFXknAmutjZMHyKAbuPRXbkt4jQso83EtMoh1bAQs-lvzVo_vT74VSU7qp-7zBORIHOez91UP9pvTiXXQnzQnLmffkxMGxDQb0KHFXj1w9RLSbfeVL9MOcpw4r2r9aoGQrPSa5TlyUrxfqpTOfXkrofTqNFpmlj4bu5mJemQ8LLYIhDvyAR-F6JdTvV1MYcqcG5tN8crGJtIUxDNImO1cv60aF8DZqgefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MQzlUNFs_et2DURFjzB3hqmfONO-xw5zGTArpnU0_COZqVF-807tGik-mxhkGm1Oy_cg8YLJWgfuQmh_xqhF3wty-dAncENVmqXl3bVi_0RnwyZnvt7oa2rZK4d6rMlBG8TVGv8DAOonSGLz5mEM2tGC9D3vdzgxIzvZLZ-pH-7H7Bjot_5XOQ2J8aaDrNSzCZ_PtVcAEOBvnGJ_gJvQZv1jp2eAEP7EmKVyAzhvM-1luvxPHwlNaTtxIySL6-h4IsPj-Y1-gzCvERIOFwDtQqofW2HOEOyAupOcmZ7O_DqoVlkCaiV1NZX7BMDkieIEUf3YWKvuTwKBdaCbwPOXRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qCc-hQjbIBvtN-etbjdTq3TcgjlCc-bXZG-mhE_ac7g2NtbdWr1UYo3szQplNzCLRTIfIF5zG6tskstvWT7uQZml1L_aGCMOjFcr5X-5HCpFlTdD4Tub-hY0pb96QvjltuXWqKc0UMqTAfWoj_BoKzrtnddIvFCHhom0322vCHBlR7P_CZNQFeSCDFnHbzwfInGe3xcB8jC9OZMXwbyhUStv8Ezzuze6KYlm5ZxfeCN7Jb9Ht5OeyDOV4ZruNmJ6qwk0ylXHIqJckVYpNm5TL9KJwZxFPYd5FXXKj0zLr_MIzEj-bE6ZHCIz3gPMcTHALgQUurtv7BzYuIIf7XdT6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vfXEInAhY_7_zbDzXsAQUXK5sLrOSJT8rItuPtc0y0YZlinsgEsyJd-qfW2mvtN6szAe8PEB86FhYrMXcZRCabAQrpes84yl9GUlDjQyd3iaOOA0FkohMl93U_fBF1XhxGw-qnge8WsBFlg-62mmI61BTCh1frITshnAnOyY5cOi__H4Aaq3p3WqF_9XvN2eJCyjA_jdYKgt_k5jPTzu-cRVLAqgFN3Wp3-GcWuHRB_1nxRPAwjA9jdtSzvLBhgUY3-zhR0MJoAWUCad7IVc2bZBoq_bbMheloKNf-8Hm4cMAnAHDwRdV10-iaX2TWx3Tjw-Do6NPZ3roWN_s90d4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4acc6e36de.mp4?token=c_UnexHDH0YecN7XBQ7gON93tgqVmQhsWMCQZbU_Pefjd59_RFzZx6CtrRYN8pfIwzdhM9mWToNxnfqHa3nVAWjwnrfK2pRDGCxOxmrM48eonF3FsjwEHji2YYoB6l1XSD50mL-AMFwCaXXmK94ux0ruhVYewpbW-nyCE6WT5dGQ1I16ydU769WsDQ2e1_X1WykYRCbymew11o6lpE7gy7Sv0tVETS1IAIwTldquQRs_qp8cRkuYQKnCcEzn60WP_e68yl2RrgP6fDbsL6bbknlrCtFrsDKZN0iQ5U4YqzCRf5U1ceHvOCKRUwBcfIaZTHFDJ0bofAbM1JUxsKRh3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4acc6e36de.mp4?token=c_UnexHDH0YecN7XBQ7gON93tgqVmQhsWMCQZbU_Pefjd59_RFzZx6CtrRYN8pfIwzdhM9mWToNxnfqHa3nVAWjwnrfK2pRDGCxOxmrM48eonF3FsjwEHji2YYoB6l1XSD50mL-AMFwCaXXmK94ux0ruhVYewpbW-nyCE6WT5dGQ1I16ydU769WsDQ2e1_X1WykYRCbymew11o6lpE7gy7Sv0tVETS1IAIwTldquQRs_qp8cRkuYQKnCcEzn60WP_e68yl2RrgP6fDbsL6bbknlrCtFrsDKZN0iQ5U4YqzCRf5U1ceHvOCKRUwBcfIaZTHFDJ0bofAbM1JUxsKRh3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس‌جمهوری آمریکا دقایقی بعد از انتشار
این پست
در برنامه صبحگاهی شبکه خبری فاکس حاضر شد و درباره این پست و تنش‌های جاری و فزاینده میان ایالات متحده و جمهوری اسلامی توضیح داد.
🔻
«ترجیح من تصرف خارک است»
او در این گفت‌وگو تاکید کرد که شامگاه پنج‌شنبه حملاتی شدیدتر از شامگاه چهارشنبه، ۲۰ خرداد در انتظار حکومت ایران خواهد بود.
او با اعلام اینکه در حملات چهارشنبه «۲۵۰ میلیون دلار» بمب بر ایران ریخته شد، افزود: «آنها [حکومت ایران] واقعا در حال تسلیم شدن‌اند، فقط هنوز خودشان این را نمی‌دانند.»
او هم‌زمان گفت واشینگتن همچنان با تهران در حال گفت‌وگو است.
ترامپ در پاسخ به پرسش مجری برنامه درباره تصرف بخش‌هایی از ایران گفت ترجیح او «تصرف جزیره خارک» است، اما تردید دارد که افکار عمومی آمریکا آمادگی پذیرش چنین اقدامی را داشته باشد.
او افزود: «با این کار ثروت هنگفتی به دست خواهیم آورد، اما فکر می‌کنم مردم آمریکا دوست دارند ببینند ما به خانه برمی‌گردیم.»
ترامپ در ادامه تصرف خارک و تاسیسات نفتی ایران را با تجربه ونزوئلا مقایسه کرد و گفت آمریکا «میلیون‌ها و میلیون‌ها بشکه نفت» از آن کشور خارج و به پالایشگاه‌هایی در هیوستون، لوئیزیانا و دیگر نقاط منتقل کرده است؛ پالایشگاه‌هایی که به گفته او «شبانه‌روزی کار می‌کنند و ثروت هنگفتی به دست می‌آورند».
ترامپ گفت از اجرای همین الگو در مورد ایران نیز استقبال می‌کند، اما مطمئن نیست «کشور آمادگی آن را داشته باشد».
🔻
«اکنون تمایل کمتری به توافق دارم»
ترامپ همچنین گفت اکنون نسبت به سه یا چهار هفته پیش، تمایل کمتری به دستیابی به توافق با جمهوری اسلامی دارد.
او افزود: «نمی‌دانم آمریکا آمادگی انجام کاری را که من واقعا ترجیح می‌دهم انجام دهم، داشته باشد.»
در بخش دیگری از گفت‌وگو، مجری فاکس‌نیوز از ترامپ پرسید آیا از جمهوری اسلامی عصبانی است؟ او پاسخ داد: «من عصبانی نیستم. من عصبانی نمی‌شوم.»
او درباره توافق هسته‌ای مورد نظر خود گفت: «توافق من راهی به سوی نداشتن سلاح هسته‌ای است.»
ترامپ افزود که ایران نباید اجازه داشته باشد سلاح هسته‌ای «توسعه دهد یا خریداری کند» و گفت در متن توافق پیشنهادی او، هر دو مورد گنجانده شده و حکومت ایران نیز با آن موافقت کرده است.
ترامپ همچنین مدعی شد «کار حکومت ایران تمام است» و افزود: «آنها دیگر نیروی دریایی، نیروی هوایی و پدافند هوایی ندارند.»
او همچنین اشاره کرد که هواپیماهای آمریکایی بر فراز مرکز تهران پرواز می‌کنند و مقام‌های جمهوری اسلامی «اصلا نمی‌دانند ما آنجا هستیم».
به‌گفته ترامپ، آمریکا همه رادارها و سامانه‌های پدافند هوایی جمهوری اسلامی، بخش زیادی از موشک‌ها و بیشتر پرتابگرهای موشکی حکومت را از کار انداخته و توان پهپادی آنها نیز «به‌شدت کاهش یافته است».
🔻
«نمی‌خواهم نیروگاه‌های برق آسیب ببینند»
در ادامه، وقتی مجری برنامه از احتمال هدف قرار دادن یک نیروگاه برق پرسید، ترامپ گفت: «بله احتمال دارد، اما ترجیح می‌دهم این کار را نکنم، چون وقتی چنین کاری می‌کنید، مردم رنج می‌برند.»
او همچنین درباره تاسیسات آب گفت قطع آب «ضربه‌ای ویرانگر» برای مردم ایران خواهد بود و افزود: «می‌توانم در یک دقیقه بگویم آن را از کار بیندازند، اما مشکل این است که مردم دیگر نمی‌توانند آب بنوشند.»
ترامپ در بخش پایانی این مصاحبه کوتاه گفت مردم ایران از اعتراض می‌ترسند، زیرا به گفته او «سلاح ندارند» و طرف مقابل مسلح است. او بار دیگر طی ماه‌های گذشته به کشتار گسترده مردم در اعتراض‌های دی‌ماه اشاره کرد و گفت نیروهای حکومت ایران به معترضان شلیک می‌کنند و وقتی مردم با مسلسل یا تک‌تیرانداز مواجه باشند، برگزاری تجمع دشوار است.
او اظهار کرد جمهوری اسلامی دست‌کم «۴۰ تا ۵۰ هزار نفر» را کشته است و افزود نمی‌توان مردم ایران را به دلیل ترس از اعتراض سرزنش کرد.
🔻
«از کردها ناامید شدم»
رییس‌جمهوری ایالات متحده در ادامه گفت آمریکا برای مردم ایران سلاح فرستاده بود، اما از کردها «بسیار ناامید» شده است.
او افزود با تحویل سلاح به کردها مخالف بوده و باور داشته است کردها این سلاح‌ها را تحویل نخواهند داد.
ترامپ گفت: «فکر می‌کنم آنها سلاح‌ها را برای خودشان نگه داشتند. این مایه ننگ است و من این را به یاد خواهم داشت.»
گروه‌های کرد مخالف جمهوری اسلامی، از جمله حزب دموکرات کردستان، حزب کومله کردستان ایران، حزب کومله زحمتکشان و حزب آزادی کردستان (پاک) در هفته‌های گذشته دریافت سلاح از آمریکا را تکذیب کرده‌اند
.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76214" target="_blank">📅 17:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76213">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUqEsrCZoM-og2QN-aEq_MN6opgHTYeORnZ_XE9xtMNQRM2Eh3vmLne4Dv91_bHi1RJN5hs4VytjmvhVo0krK7G0tsFYP2mEERxQeTcQLKsEgvwxMR5dddVUqGpGsOoy4VWjzDn9qbvBJWBvBLS0JaYF_vJIu0IeW8M9y9n_6mIRF1dPkJrQW6Q-aST5STfhmY4JJnd1w8SqRpJRK9Ak269C7czFwaO7Z45BwXglO2QHnW6FElFiB8hBxECMzw_kAoCKgBcfx-zQRgoaIWB19Iz-QRcTsN8JnyT0Pg_o8xe7Tv4ma3EXSzOdomyrAfifKe3ynANkIL3xuszjj1WujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسکات بسنت»، وزیر دارایی ایالات متحده، در شبکه ایکس نوشت که جمهوری اسلامی ایران در «بازی با حاصل جمع صفر» شکست خواهد خورد.
بسنت در این پست توضیح دادکه خساراتی که حملات موشکی و پهپادی جمهوری اسلامی به کشورهای عربی به‌عنوان «متحدان آمریکا در خلیج فارس» وارد می‌کند از محل دارایی‌های بلوکه شده در آمریکا برداشت خواهد شد.
وزیر دارایی آمریکا همچنین نوشت که هرگونه عوارضی که از کشتی‌ها برای عبور از تنگه هرمز دریافت شود، با برداشت از حساب‌های ایران جبران خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76213" target="_blank">📅 17:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76212">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCnat4XpAzPq7rFoxU-_sCbCfg3NtS7Vnkj1sDLG7pF54RbMMD4AOZlBQCqGBE0mtRJtOZ4VYv6flzKZ6wc_MhWJPtBEw7YuM4tEiaNfKZXqq2YXv6TW3FcoRn9candS2NZD415pnB4aDUB6dTmArQgpDZga5hTJnaj-aHfLz26oTPzH3KbByVEaEgabnsssZzKqw56g7N5tXPPL0YunLiU2ySvC0vShhW-Gfluh7puR7uD7jdAapV_mBcXfvpXqCIyjAICVQej9z3thQxhioFVRNl4jO6IP8Z59ThJ_vFgdrKaVRYjyXIfqFNu_BgbAUmi4yN3-YvloTnbJLuh8oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا روز پنجشنبه اعلام کرد که ارتش این کشور امشب بار دیگر ایران را به سختی مورد حمله قرار خواهد داد و از برنامه ایالات متحده برای به دست آوردن کنترل جزیره خارگ ایران خبر داد.
دونالد ترامپ با انتشار پیامی در شبکه اجتماعی تروث سوشال نوشت: «ایالات متحده امشب ضربات بسیار سختی به ایران وارد خواهد کرد؛ کشوری که نیروی دریایی، نیروی هوایی، سامانه‌های راداری، پدافند ضدهوایی و تمامی دیگر اشکال دفاعی آن، به همراه بخش عمده توان تهاجمی‌اش، از بین رفته‌اند!»
آقای ترامپ در ادامه پیام خود نوشت: «در مقطعی در آینده‌ای نه‌چندان دور، ما جزیره خارگ و دیگر زیرساخت‌های نفتی را در اختیار خواهیم گرفت و کنترل کامل بازارهای نفت و گاز ایران را به دست خواهیم آورد؛ همان‌گونه که در مورد ونزوئلا انجام داده‌ایم، اقدامی که نتایج فوق‌العاده‌ای هم برای ونزوئلا و هم برای ایالات متحده آمریکا داشته است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76212" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76211">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJVtzi6WD7clXX3_qEHLqX4HPnaIdpq27hMohRiY7PbtZw6GEbkePeX_DEilaijV_13ESK_mOmSIQB25NfdxlKOe0yh2FviY8lg2w1Y1jSyWtbpx-ZQv1TLlZtq56Xg44clCupsnnVyXi9EiRhvZ89TCteFfBCLBLoiEOIeHO67qynbVJZsTgsCM-xFKGRJwjwaISPauxEdjv9MdpR61zwgUvNog_l7dwcHtDhJUMTtX2tdxPqZjO_EYaEqcGtsa2FAUnxqPwxa2RVQ3P2UgOC0-I-c3z91RSRj_rglYcP7uDQtTZl21f79JfSHojmepsDhJrv7I5gsk0ezlUGhntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل سازمان ملل متحد، آنتونیو گوترش، در پیامی تازه درباره وضعیت خاورمیانه هشدار داد که این منطقه «هر روز بیشتر به سمت بحران عمیق‌تر کشیده می‌شود» و تأکید کرد پیامدهای آن فراتر از مرزهای منطقه خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/76211" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76210">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJThC103_CTsGc__mbB7hlmdCPLP4Qm94mYAJuuGw8aYoZaJRhf5vXT5xx0mFlVf_c9KzeV3ylyfOBbhe5BEHfbp0ZVwfDcI8seuuUBDUlPMcZh6NZZry0aozdlAHpFcPKq3xWij6YW5UxmQ3GHscDNiGC4Q-EKjg2m4ssodJMuOGyM7GQZt5GxakJQzCxr8WjxMu5WZXfNLlI6HHrbxc_s6-p4nXg7v6NKkvKMs6wtaiiOyEiINHqt3qkQkBuivBDpngbq5n2nPZ7493kjJeg3t3n3GFtYqxbi2wV6qoZsFBBwJUdDj7OifWJYDThYUOd4IxRNJZ0mqOuli78K_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی با صدور بیانیه‌ای در واکنش به حملات ارتش آمریکا به اهدافی در ایران، این اقدام را نقض قوانین بین‌المللی خوانده و گفته است این حملات آتش‌بس ۱۹ فروردین را عملا بی‌معنی کرده است.
در بیانیه وزارت خارجه ایران بار دیگر به کشورهای حاشیه خلیج‌فارس درباره استفاده ارتش آمریکا از قلمرو، امکانات و منابع آنها هشدار داده شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/76210" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76209">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d46260783d.mp4?token=hFopCjNc0yhqRMGAk9c3EpgBUD30yd_pzIsvjO-vVIrCb_X86tSyKn3gdPMyGWDP49QAhq2T-HUusEmu9g7NP5GxGHW5D04nuueue9UK06h5gmB5DlcxTZSsVhgd3aJCMvfOVGE0QRfIzLIp7Vc4Q8on4YC4b_TQ4WVN2uuLARscuo-QU37N86OyglJaBpiPRk2a4f6WzooAuEGGhZ2wNZshQEYcw3W-ikVhhjmJnAU2XClwryv0tRZatc926UKypxEghuzr00v30ha9b5-L_4Gu6IAFqNMMFAHt1GQVXvL3TnNiAZKQ27-8OnFvxx4yJZPyJsHNG1fZphmzuNgPbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d46260783d.mp4?token=hFopCjNc0yhqRMGAk9c3EpgBUD30yd_pzIsvjO-vVIrCb_X86tSyKn3gdPMyGWDP49QAhq2T-HUusEmu9g7NP5GxGHW5D04nuueue9UK06h5gmB5DlcxTZSsVhgd3aJCMvfOVGE0QRfIzLIp7Vc4Q8on4YC4b_TQ4WVN2uuLARscuo-QU37N86OyglJaBpiPRk2a4f6WzooAuEGGhZ2wNZshQEYcw3W-ikVhhjmJnAU2XClwryv0tRZatc926UKypxEghuzr00v30ha9b5-L_4Gu6IAFqNMMFAHt1GQVXvL3TnNiAZKQ27-8OnFvxx4yJZPyJsHNG1fZphmzuNgPbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا سومین نفتکش ناقض محاصره را در خلیج عمان از کار انداختند
تامپا، فلوریدا — نیروهای آمریکا ساعت ۱۱:۲۰ شب به وقت شرق آمریکا در ۱۰ ژوئن، پس از آنکه یک نفتکش با تلاش برای انتقال نفت ایران محاصره علیه ایران را نقض کرد، این شناور را در خلیج عمان از کار انداختند. این سومین کشتی تجاری است که این هفته توسط نیروهای آمریکایی از کار انداخته می‌شود.
فرماندهی مرکزی آمریکا، سنتکام، علیه نفتکش
M/T Jalveer
با پرچم گینه بیسائو اقدام کرد؛ این کشتی در تلاش بود نفت را از ایران از مسیر خلیج عمان منتقل کند. یک هواپیمای آمریکایی پس از آنکه خدمه کشتی بارها از اجرای دستورهای نیروهای آمریکایی سر باز زدند، دو موشک هلفایر به اتاق موتور کشتی شلیک کرد.
اوایل این هفته، هواپیماهای آمریکایی به‌ترتیب در روزهای دوشنبه و سه‌شنبه دو کشتی با پرچم پالائو، یعنی
M/T Marivex
و
M/T Settebello
، را از کار انداختند. مارویکس با تلاش برای حرکت به‌سوی یک بندر ایرانی محاصره را نقض کرد و ستبِلو نیز تلاش داشت نفت ایران را منتقل کند.
از زمان آغاز محاصره در ۱۳ آوریل، نیروهای سنتکام ۹ شناور نافرمان را از کار انداخته‌اند، ۱۳۵ کشتی را که از دستورها پیروی کردند تغییر مسیر داده‌اند و اجازه عبور به ۴۲ شناور حامل کمک‌های بشردوستانه داده‌اند.
این محاصره به‌طور بی‌طرفانه علیه شناورهای همه کشورها که وارد بنادر و مناطق ساحلی ایران می‌شوند یا از آن‌ها خارج می‌شوند، اجرا می‌شود؛ از جمله همه بنادر ایران در «خلیج [فارس]» و خلیج عمان.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76209" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76208">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeM-cuW18_0Z37pDp67oJNMzHOJK5FOXGSrU7g0l3i0CuyI2DyPW_Gfdujg15_jJtBaSnm5viD4v9mzdhHKEYFvEcMoYOr3uHw0u9Iu4Z2FX7w9EGSbD5NXTh3Qfg1pS2xfyM2LVgChyl4mhS0eeoVT95x-IrJVwoAcYNAliS7x7IePeeThskRthv2Bd7AQrDE9lRS95Io_YPWyzwxg7c7u5fNJMyBQC6U0OAKwZ64Kzw8X5VI8YRZh_wqLRk08n5vrcMObcGxijkQnjwImxSgzMLJRCLiXCkUEqLCZEjGug6ONvX4yLu-7rK61_otK53eI5UhY2c5Kz2fliQg3-VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبدالرحیم سلیمانی اردستانی، عضو مجمع مدرسین و محققین حوزه علمیه قم، توسط دادگاه ویژه روحانیت به شش سال حبس، خلع لباس روحانیت و پرداخت جزای نقدی محکوم شد.
نزدیکان آقای سلیمانی اردستانی اعلام کردند که وی تنها به شرط برگزاری دادگاه علنی حاضر به اعتراض به این حکم است و در غیر اینصورت، حکم را بدون اعتراض می‌پذیرد.
او به اتهاماتی چون توهین به مقدسات، توهین به علی و مجتبی خامنه‌ای، توهین به مقدسات تشیع، توهین به مراجع دینی و هتک حیثیت روحانیت شیعه متهم شده است.
سلیمانی اردستانی در فروردین ماه توسط نیروهای امنیتی بازداشت و به زندان ساحلی قم منتقل شد.
او پیش از بازداشت و در تحلیل نخستین پیام مجتبی خامنه‌ای که به تجلیل از علی خامنه‌ای پرداخته بود، نوشت: «مهم‌ترین هنر والد شما این بود که مخالفان و منتقدان خود را بی‌بصیرت یا مزدور بیگانگان می‌خواند و هر برخوردی را با آنان روا می‌دانست! از صفات اخلاقی ایشان دو صفت لجبازی و کینه‌توزی را بسیار برجسته یافتم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76208" target="_blank">📅 17:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76207">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O0dKYMzylDtccoNF1l0g-afhwwRrzPgJ5uhhEq2JI9umb3uiI4h_hyJ6avqEOfh9LVJPDMOlf7GEP9i08080Zic6O17YrgSU5QnA1NaZy1jfVq8v0dKqc3ExE3Sx09TXq23qeQ6VC_yTFSKd0_BmEVazsVdsXjJZZkM5VRc-oHbXTctCnfUUJRjWJ_sjUi-YPnXIDOrBtASBnZ_Ss5Tj9W01EoNOtCqY5TRCykanp0fakQS4lewpbArN0Th6MEfmkP-SeKSmtK0L3svPY7dle_JZlAEylLuFbB5g3-1XippMcI0Yr5E5OT44QTGjzS9_xYnowTaLxZrQMtLGUAD9jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی از پیشوا در جنوب شرق استان تهران
'دود انفجار حمله حدود ساعت ۴ صبح که در ورامین و پاکدشت هم احساس شد.'
پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 506K · <a href="https://t.me/VahidOnline/76207" target="_blank">📅 06:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76206">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/769901b74f.mp4?token=GXpowU_vFZ6NLrkytyXXH_VGrv1tdaGsZCZgBqWuFHi7vzGbydgHvJNIma3OEcgorUwVFGosKaCifGQhUo_MfPxruCDHO-yGHIPENlfb4-CVUkOsJZe8s3-hjCVi_XBv8vlfATXj5Ziq-l7yyR6tEYAOuJ-UN56qGhOYvoUa8herVZlT02dl4QDTJAnegLJyPzgExoUZCDFz66GmNHAwDf0sFUISRS2pxINvmYvUQ_wa6_rjHj15E8bCHuaSqNhqAdwx4dm4f9Pi3mbyrxeoYLVYaF9svR0fEByAvc7ZeHnPasKXF_nrFLh0YfDm1G4FSp3sH7L42qDjXkOP75LHAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/769901b74f.mp4?token=GXpowU_vFZ6NLrkytyXXH_VGrv1tdaGsZCZgBqWuFHi7vzGbydgHvJNIma3OEcgorUwVFGosKaCifGQhUo_MfPxruCDHO-yGHIPENlfb4-CVUkOsJZe8s3-hjCVi_XBv8vlfATXj5Ziq-l7yyR6tEYAOuJ-UN56qGhOYvoUa8herVZlT02dl4QDTJAnegLJyPzgExoUZCDFz66GmNHAwDf0sFUISRS2pxINvmYvUQ_wa6_rjHj15E8bCHuaSqNhqAdwx4dm4f9Pi3mbyrxeoYLVYaF9svR0fEByAvc7ZeHnPasKXF_nrFLh0YfDm1G4FSp3sH7L42qDjXkOP75LHAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'نور یکی از انفجارهای حملات بامداد پنج‌شنبه به استان البرز'
ویدیوی دریافتی: 'فردیس کرج، ساعت حدود ۴' پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 484K · <a href="https://t.me/VahidOnline/76206" target="_blank">📅 06:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76198">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZXgv2enkXmbDynVJ9weUwGClxpgQdzYxmGTJ2uzipdyizQEuGyprExdJabEOJr-nor5wrN4qMCnhS1f0nkZQklrc5L4TilcPHbpcnKsmmDjmZtS5p8fuW2P29vtnCJZ3jhHB3BVhJ748_qFD5FMdI3jUOAxuaw0uiUNW6ucyIt6_Z01K1y2IGh1a3UM7DUQ4vT38h7myWDXkJ3rYorG28XDe-rqDvOpZdTLzR4KPq_Zd5zZsU-IVIeAz9uZwxem6DAkJt9Qk9AYEYfVYj5SzqKlkAA1Q3uh6ujPX-VCohJG2qxhyz-ex_4Kbi1yeYVWeu3AtgsRXorp23rxJzVsavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DubQ3I_YRH9Okt_1vtR4IJWD3I74w7_Pa-JVSaSDQnhBp7uaw6AKwIgvZIybzB1f-aYYU7AUyOqQ5_XASMEgZgX2LRG-K4uH9yrxZ76DBn89jzupwoNlCy-y_2jMXmVV8Kk7BIHkupkvpVZxcq4d3EzBAoKujwB_UFalpGmPHhRreh1Iiei-7N1NdRo5wBcurTM6cQ6vXbZMvV68FmZspZBvpSY6rcADWtvj8LNKQT8LfAtwIOvIM5uizG37gHFk8W_C5xrF8dfDlh86M37bO9l6SdB570kIUzJ3aV52L0d_lj5079k1-HfwM4m4m7VMalqSbu0UYH1jaGXu2_I9Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W6MCsmOulxfM72r7SbecG9qjI6rGXg8X1Q0YYhOL1g1yBqD5fGzyiE5KsywPOvUhaaP3LgisoxEaz5UvUW8CPhfNcBA-0pwcKSk1XdXbofVHh6gTdHJXZ6G-QjDMpTieDXmZnuIP9YBhjKIC_1Wuwgs1U0FUFMowIKfkZu-N5k0PYo3fY2Uee1IoYOqCq5g2TdJAK3vppY5S27aCtgR5B-vY-Zr1frgKmMK1SVfebRDsqgtZH45dSJVG47HpB9XY9jOnWTp-jk7T3mUcPadoTnA4hY3p_8nI6_JFfpcxLmDNZy53IiUnNpULVZkg9Vf54YABSx1CCfWu2i21iC7Ecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N_ZEk_0RLWKR4oLrgx2d7K3z4Xr2Vyw3GFm4YeV7LyWceaDAAogJO6puM3MFcVwJScHw7Lvn_VI_5tgulCNKNEBTQMtqyDFJLai_wldQPKauvx32q3C1GYS4HD2Yi3Fqmdo4DpPFizY4UIRP28B3JigxEHg7ZX5qGCaNIWyRLWZdbNRf-QUTL6XgBWEltibgnOtrt9wvkArjBRik0Nv03Ryf8Yf2NodICWjfLoKziTPVZ5HQTuQdMMU72KCQPTgcBvsRGhbeFi9_AJ8QJBQSce2i7RgxnyoB3m5oxQ87-i1Hk_J6KtvcFtM53YOQpUIR1lEYcbMMQeGeKD4yUATqPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e891de921.mp4?token=e4immQDwnGoCnFh3ajRikFc2de7x6kaFY18nCQ9uAhjbuDbKGVElxGgJ7d9CiT_QUfOKaE5wPHm9C2sStHSzgDDJxc637JFe9wGfVrZX4jxN-aHlamHMZm0OKHtL3Cm8UZRifY6TYgcALT2gGxXUw_7-U9wcBEoDKO75g0JP0OedbHRoLEPFpxwU4AHhZ5iP5YAc_2Mwy9JRuVqr9sf0IXJVESfZxNBigkgC8GQA1NnOUTdWN_HQ4MWeL1QkVcnRKwdX2p_JKDBObA-OmlWNdcfzLTWmvddRvj2QqueaMl2HZN5PUVVOsnEAMCvZJAPAM8svx3eVNCcP_VllqZhLVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e891de921.mp4?token=e4immQDwnGoCnFh3ajRikFc2de7x6kaFY18nCQ9uAhjbuDbKGVElxGgJ7d9CiT_QUfOKaE5wPHm9C2sStHSzgDDJxc637JFe9wGfVrZX4jxN-aHlamHMZm0OKHtL3Cm8UZRifY6TYgcALT2gGxXUw_7-U9wcBEoDKO75g0JP0OedbHRoLEPFpxwU4AHhZ5iP5YAc_2Mwy9JRuVqr9sf0IXJVESfZxNBigkgC8GQA1NnOUTdWN_HQ4MWeL1QkVcnRKwdX2p_JKDBObA-OmlWNdcfzLTWmvddRvj2QqueaMl2HZN5PUVVOsnEAMCvZJAPAM8svx3eVNCcP_VllqZhLVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دود انفجارهای حملات آمریکا به غرب استان البرز و
#کرج
تصاویر دریافتی از  حوالی "حصارک"، "کمال‌شهر"، "مسیر کرج به قزوین" و...
بامداد پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 467K · <a href="https://t.me/VahidOnline/76198" target="_blank">📅 06:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76197">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lU52tBQy4QGgr7I8H82sGvdxrWzgHcK4VITUOcgIkCGpp8FCK0R9ibAz_EoHR6R8-dFf-Q-0V_GgIyIQxvRcIimZXyIjV02381sBrBlI_wkaoAov2EDzof4iFuCtoSVfnIASTrf0Pf277iqL3qnxXAcIZj9XOS8LIh42UH9KL53fI9_QtG-bhS4aoBzSn14GIqavBd5Ccdh5KCgmfD6e7478MdAHrNdKaqX_traRJhr94JMCd-pW0_FVKR5N8gb3taLZpZ4gS_iEzdZtBvCMghoi382b8x58WUE7LtQlGRH-WGoXTjNJfQDuyUgdTSgcAEDMZhqzotyspAYDkn2Pgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی با شرح : شلیک موشک از استان اصفهان ۶:۰۳ پنج‌شنبه ۲۱ خرداد
آژیر هشدار حمله هوایی در بحرین صبح پنج شنبه برای بار دوم به صدا در آمد. ویدیوهای منتشر شده در شبکه‌های اجتماعی شلیک موشک از چند استان در ایران را نشان می‌دهد.
@
VahidHeadline
ارتش کویت بامداد پنجشنبه اعلام کرد که سامانه‌های پدافند هوایی این کشور در حال رهگیری اهداف «متخاصم» هستند.
پیش‌تر روابط عمومی سپاه از حمله به اهداف مرتبط با آمریکا در کویت خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/76197" target="_blank">📅 06:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76196">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/863187a248.mp4?token=i_zHCrIQ8hJKrHyS4Ehf9YFKvrJ2eho7N1X88iL_qyTcy-c0El-uRqDcPBa1ALE0hs_U-MJHzsX2RujstzB1RDKNT5rUwcELSjdR6ECdulzaddg_ecaq8RXzoqGaWbszPKv_kD2CzdSnNSvMcvf2lz17hunQklD6U6aV0FXwjcPV40ZAfQ_5zhGPZzoVbdPQusC44YDJ4zR1NoSjp0JZs4CL1latygGU9wh6fosSF4lGyWXzRWDn8ymsMNRKcVKxVMAe1YCloT-sutTBECm2GYnfDlzYCHcnPcPNMA29yC6LbNFSD9jf63ZzxKpEGe0SodDX6uBX-eSAfM-DmL0oKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/863187a248.mp4?token=i_zHCrIQ8hJKrHyS4Ehf9YFKvrJ2eho7N1X88iL_qyTcy-c0El-uRqDcPBa1ALE0hs_U-MJHzsX2RujstzB1RDKNT5rUwcELSjdR6ECdulzaddg_ecaq8RXzoqGaWbszPKv_kD2CzdSnNSvMcvf2lz17hunQklD6U6aV0FXwjcPV40ZAfQ_5zhGPZzoVbdPQusC44YDJ4zR1NoSjp0JZs4CL1latygGU9wh6fosSF4lGyWXzRWDn8ymsMNRKcVKxVMAe1YCloT-sutTBECm2GYnfDlzYCHcnPcPNMA29yC6LbNFSD9jf63ZzxKpEGe0SodDX6uBX-eSAfM-DmL0oKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'موشک‌های شلیک شده از استان
#زنجان
'
ویدیوی دریافتی، پنجشنبه ۲۱ خراد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/76196" target="_blank">📅 05:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76195">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ce876bdc1.mp4?token=QJKOyILAa-HUew8CjDl53b3dZML_0WISk6rGSxj17Q-grHSguYGPQKRT5Zwwe50FXx2rtV2hQL_d3P9m_loEary18BjlV-C5dnpGs6_WF8CMdDDOrgeljd9tqa2J3M0f0dWdon497RVQS6OuJlA-9rAuXXOp5XbVf77H_Jr1Zsn0eeD24XS9xDKrqqU2BBzdc_LYsqYU6grS-AML-T1IeYV9bzPHLicYPxKIL7gDZZs-VsNDvKggdVvo1pX59rXIIbTCENjofQXkcbu6P8xEqBzBUunvWK7_Td8FtUltFGM8l38PdBcsgkonxyoInwslyNj1DBxOLnDW2ER-hpW2Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ce876bdc1.mp4?token=QJKOyILAa-HUew8CjDl53b3dZML_0WISk6rGSxj17Q-grHSguYGPQKRT5Zwwe50FXx2rtV2hQL_d3P9m_loEary18BjlV-C5dnpGs6_WF8CMdDDOrgeljd9tqa2J3M0f0dWdon497RVQS6OuJlA-9rAuXXOp5XbVf77H_Jr1Zsn0eeD24XS9xDKrqqU2BBzdc_LYsqYU6grS-AML-T1IeYV9bzPHLicYPxKIL7gDZZs-VsNDvKggdVvo1pX59rXIIbTCENjofQXkcbu6P8xEqBzBUunvWK7_Td8FtUltFGM8l38PdBcsgkonxyoInwslyNj1DBxOLnDW2ER-hpW2Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان تبریز
ویدیوی دریافتی: عبور یک موشک از میان رد موشک‌های قبلی
پنجشنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76195" target="_blank">📅 05:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76194">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/056cecd324.mp4?token=VCcZytKBZh5Wn223-VkbBs7q6_db5jNgdTCRvqmzhKQSPobpgjhmehKLgT2uJu-9BKeyMlYvLKubfFotrXwBh-WM40wHL1UHg8drTah0bqXauIycUwjgJR_wnfYiwWQDDsln6IDBL_6_kvt0G5wpSzdGLBpMqoT_G3266Azl80vWt69skrwBcghvPHjT7LyDzDQsLH4jgv6F4ut6egMNFkBr1w2-EcVaRgaRNr4bk0arYKXIbviykBYBDwft2046pKd1NTody0s38Mqh004azeS7buwIkwwYhlREa4ocdSq4lMs6DQ3b6jtjKokgMHINjK_1u3JzRMEoQEVQrVK8Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/056cecd324.mp4?token=VCcZytKBZh5Wn223-VkbBs7q6_db5jNgdTCRvqmzhKQSPobpgjhmehKLgT2uJu-9BKeyMlYvLKubfFotrXwBh-WM40wHL1UHg8drTah0bqXauIycUwjgJR_wnfYiwWQDDsln6IDBL_6_kvt0G5wpSzdGLBpMqoT_G3266Azl80vWt69skrwBcghvPHjT7LyDzDQsLH4jgv6F4ut6egMNFkBr1w2-EcVaRgaRNr4bk0arYKXIbviykBYBDwft2046pKd1NTody0s38Mqh004azeS7buwIkwwYhlREa4ocdSq4lMs6DQ3b6jtjKokgMHINjK_1u3JzRMEoQEVQrVK8Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: رد موشک شلیک‌شده در آسمان ارومیه
پنجشنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/76194" target="_blank">📅 05:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76193">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62d2ba90a6.mp4?token=ePWtKJT1dypD2-FAv8C3-X8wWV1ZkiNjTqk2aTsM7lnVSAM_a08r4yvIZ-d1Rar6MJOsdO9_J7OMXnnFC5xzJi2p1uE0E301KClTnOUMPt6F4VN45Meki7mGXgFUS8YlHVtOejn7fvlet2hXY0Sf3wo4xRthXDKpuqVfl_bvDzN8ujiV_sVXfE2zj6Uxyrgoi8D0RgBuOZcSXOAnoPeRP3isBoQRSpnuXA3jy1w4agBuzdO7yIUwD7yYF4ksh29JXe_jAzBMWdwPhX77Dy3kOxcQKbOx_GUHxIHjUF-mHnDUqS9eaQC-c1A6Eb4SlLSS_l6enkdKreYfg4z_PhVDHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62d2ba90a6.mp4?token=ePWtKJT1dypD2-FAv8C3-X8wWV1ZkiNjTqk2aTsM7lnVSAM_a08r4yvIZ-d1Rar6MJOsdO9_J7OMXnnFC5xzJi2p1uE0E301KClTnOUMPt6F4VN45Meki7mGXgFUS8YlHVtOejn7fvlet2hXY0Sf3wo4xRthXDKpuqVfl_bvDzN8ujiV_sVXfE2zj6Uxyrgoi8D0RgBuOZcSXOAnoPeRP3isBoQRSpnuXA3jy1w4agBuzdO7yIUwD7yYF4ksh29JXe_jAzBMWdwPhX77Dy3kOxcQKbOx_GUHxIHjUF-mHnDUqS9eaQC-c1A6Eb4SlLSS_l6enkdKreYfg4z_PhVDHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک موشک از استان زنجان
ویدیوی دریافتی پنجشنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76193" target="_blank">📅 05:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76190">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/saVv5Wk6zI_kHT9hXoXAdamX_ilZt_vEqzQ_ebqJbpWuIuD8BMiHZ4ke8fRqdkeFRhR7JZPi9X2yn0HxtK7iU_36TD4okRQ2KPErhbnXq-yiY5raaSAkvwkUQqhK11NyAYbqNL-oOzXRFYtURPCtktl3tgtLFS842nVzZa2y7Eu5PX9g9nqxZ_MwlakIiCTPRQXOcl3pebeZNvyq7aKot5hSD2b2Pxb_edLY6R484uVzX1qF6OgijoMDrcOFLfn4EuqxUjyr-RBWlF-nQy6T4m_240AjM5EhBUxDvMqLkEptB6VYdAuCw-myjqN1LaCXRj0ksTPOf4eom_Unkpiqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S6Ib8sIHeUxmGiTJZCnY2UvWYvQLHXz5ttL48b8yRGKeC0v_TKt3cphJ06yuvndrnh6tWPbsT0xF9_28TA4cg6aZzGpC2EzdK_eWMeAJum1yMrZdMZA-vm1f8ez2wY9arQbhbk1v-HoQaOTUelfTGrAnSFDON7eSOLTJxTB07qKPIghpCm09JsRf4V-XVvvaBShma3ZUuG_43hhUwbmvD29GrOck84u5xd3SmeBr1ZJfIATukWCvZDKvL_Sc9tcJ4eZdh8ewlRou2Bx7fa_wLtQMOclCVZYAFBU__YGgtg1f-4DyALmAdcSORsZVIZC-PHddkFWw5JTzBUOeG2OIlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G9cnqh_kHNVAlna5V5Sidrtr4286KLciAxxncMA6pE2-mhTXb_nztr45j_VVjPFgdpSW1VqMqVwVOTTEV59VYpDyZC6__h8jbVxQRzps-va4pWYUudxDetyF4Lw5imd0OSoLaUwYy2S3UbMNtrFInq-aaEBrzk9JkthzBu7Web0k2STf2WHyC-FR0wdP3vJSB6s-HKJONqPqhLfkiHtOuY9ZtXKdfGiUIRS7pcouUhwZp-wDo7awAZV5d052DKRBScQLzoFR5KqGDEzkdd1v_dgdVTMmJOjIV5JNJQvXElckyf7EsPhfaaN-FQGIWtJnXFw2hniPjrxtLJTkBIr13Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شلیک موشک از زنجان، تبریز و ارومیه
الان از شبستر تبریز سه تا موشک زدن نمیدونم به کجا
صداش خیلی زیاد بود
الان یدونه دیگه زد
سلام 5:16
همین الان تبریز صدای انفجار قوی اومد
از ارومیه موشک بلند کردن
5.18 ارومیه  صدای 4 - 5 انفجار
سلام وحید جان تو ارومیه ساعت ۵.۱۷ چهار بار صدای انفجار شدید اومد
هنوزم ادامه داره
3 تا دیگه زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76190" target="_blank">📅 05:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76189">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dt_WahuohTtBdBHww23XjgJjAuEMkEJeg9ocgQbiHTwVgq7kmriBynYPzSP0oxXFo8qZmPzL66qV_CtxWl76oWt2AfM9tK5pjLTGiTQK2nHDN5x5-vyR2CYhewM3RQ7kqhIj6qAWX3FaPm9OZEK6EW8qzFE76DecVznwZiNu35yNLQp6WyFfUQU0YQJAPXpUhLHHt-Gw0B72cX9HonkMcHaLa-3Inzk3ZgrTkth6-xoZwMmJ1KS-9qZNYpWielExsUeRsa2C-q-YkpTwydt4cuVN4KJcSrVov4oqthkWR8E8kiBxOZPrH_T2ehV9UCimf5Dl2ACKBZlEWELBQyHl8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
ساعتی بعد از حملات بامداد پنجشنبه آمریکا، خبرگزاری‌های رسمی به نقل از ارتش جمهوری اسلامی ایران نوشتند: «ناوگان پنجم آمریکا در بحرین، آماج حملات پهپادی ارتش، قرار گرفت. در این موج از حملات پهپادی ارتش، آنتن‌های ارتباطی و تاسیسات راداری سامانه پاتریوت ناوگان پنجم مورد هدف قرار گرفت.»یییی
همزمان وزارت کشور بحرین در پیامی در شبکه اجتماعی ایکس از ساکنان خواست تا با حفظ آرامش به نزدیک‌ترین مکان امن بروند.
سپاه پاسداران از حمله به« ۱۸ موضع نیروهای آمریکا» در منطقه خبر داده است.
کانال تلگرامی سپاه نیوز نوشت که طی «دو موج عملیاتی ۱۸ هدف مهم» متعلق به ارتش امریکا در پایگاه‌های هوایی «علی السالم» و «احمدالجابر» و همچنین پایگاه‌های هوایی «شیخ عیسی» را هدف قرار داده و منهدم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76189" target="_blank">📅 05:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76188">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o2HddQTbYUFb8JnZ4zznvHGVBhK31EFxeNwFC-e8okSZEthrY-VFgVK3Ss3LUC8dpX24nAeXzJneaMeFyrL9xoqGlyp5lU_TXqfJeI3H_TZ-a75TCuvjgWb_PLJHU_063w2c8MqHmF75T-iDzWnj8TZdQFaqdIzQOpX4a5FBwI34uXmhh4UdLs76oVeMkPolCstUxipO3gNtLYk9fC6fh9340pxiNl5vg4jEgpjhoGdIxJMQk9doDGwognDGQHY1mwkpoDDFD-8D-p4uTwA_5uYzeG0Itar6t2fNIZ9_f5wEz3mVdoMjfGjHRzLAfPm5StyiIZeKovNac0R1MjIp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز به نقل از ترامپ گزارش داد که اسرائیل در حمله نخستین ساعات بامداد پنجشنبه به اهدافی در جنوب ایران مشارکت نداشت اما به‌طور حتم ارتش اسرائیل در سطح آمادگی بالا قرار دارد. او در عین حال گفت که آمریکا بیش از ۵۰ هزار نیرو در منطقه دارد که بسیاری از آنها در عملیات مشارکت داشتند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76188" target="_blank">📅 05:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76187">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c67229aee8.mp4?token=X2WJqwWcMyHwlQXl66oTtQN8r_qDDt-3LL3s2zO_PNlPPSoj4ej4g6BlCi5RvPlJ7-RZho_Sz08dtRrPq1dQremqkwdILP3zssJFQeJDksukTpRaSShLs6KQrK0baLrsmDwh7T70rR7341ZqXplSe97neMFCQUlOGolhHtpUoVRoFKKrb6dmdK2QSxoxHMSavOE8vg_CTLZ8pkf0K3m7xoRwGDdKRZRMGqzE40wPp3_vnpZUbv8OgkRHcs8qsuhr8zsncNgomtq7fYXcAlzxYfhHa9AmwhZd8A3oL2vFhrC-mm1f80x9CzYTzpwuMPOrUSDgZFzuRDwMRbY-15NfVg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c67229aee8.mp4?token=X2WJqwWcMyHwlQXl66oTtQN8r_qDDt-3LL3s2zO_PNlPPSoj4ej4g6BlCi5RvPlJ7-RZho_Sz08dtRrPq1dQremqkwdILP3zssJFQeJDksukTpRaSShLs6KQrK0baLrsmDwh7T70rR7341ZqXplSe97neMFCQUlOGolhHtpUoVRoFKKrb6dmdK2QSxoxHMSavOE8vg_CTLZ8pkf0K3m7xoRwGDdKRZRMGqzE40wPp3_vnpZUbv8OgkRHcs8qsuhr8zsncNgomtq7fYXcAlzxYfhHa9AmwhZd8A3oL2vFhrC-mm1f80x9CzYTzpwuMPOrUSDgZFzuRDwMRbY-15NfVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام: نیروهای آمریکا تازه‌ترین حملات در ایران را تکمیل کردند
ترجمه ماشین:
"تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا، سنتکام، روز ۱۰ ژوئن، به دستور فرمانده کل قوا، حملات دفاعیِ بیشتری را علیه چندین هدف در ایران تکمیل کردند.
نیروهای سنتکام حملاتی را علیه توانایی‌های نظارت نظامی ایران، سامانه‌های ارتباطی و سایت‌های پدافند هوایی در سراسر ایران انجام دادند. تجهیزات و نیروهای سپاه تفنگداران دریایی، نیروی هوایی و نیروی دریایی آمریکا مهمات هدایت‌شونده دقیق را به سوی اهداف ایرانی شلیک کردند؛ اهدافی که تهدیدی برای نیروهای آمریکایی و کشتی‌های تجاری بین‌المللی در حال عبور از آب‌های منطقه‌ای محسوب می‌شدند.
این حملات در پاسخ به تجاوز بی‌دلیل و ادامه‌دار ایران انجام شده است. نیروهای آمریکایی همچنان هوشیار، مرگبار و آماده هستند."
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76187" target="_blank">📅 04:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76186">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پیام‌های دریافتی:
درود صدای انفجار در شهر کنگان ۴:۱۷
شهر کنگان صدای انفجار
کنگانو زدن ۴:۱۸
سلام شهر کنگان در جنوب کشور صدای انفجار
کنگان رو زدن
سلام.
کنگانوووو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76186" target="_blank">📅 04:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76185">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یک صدای دیگه از کرج همین الان ساعت ۴:۱۰
سلام وحید
یکی دیگه الان
همین الان دوباره کرج
ساعت ۴:۱۰، انفجار دوباره
۴ده دیقه کرج کمالشهر
وحید صدا های جدید ساعت ۴ و ۱۰
ساعت ۴:۱۰ یه تک انفجار دیگه گلشهر کرج
صدای انفجار خیلی بلند و طولانی بود
ساعت ٤:١٠ دقيقه باز صداي انفجار هشتگرد شنيده شد
مهرشهر کرج ساعت ۴:۱۰ صدای انفجار
همین الان ۴:۱۰ گلشهر مهرشهر
دوباره صدای انفجار خیلی شدید به همرذه لرزش زمین
سلام وحید جان کرج دوباره صدای انفجار همین الان ۴:۱۱ دقیقه
و کلی پیام مشابه دیگر که نقل نمی‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76185" target="_blank">📅 04:13 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
