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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 01:32:36</div>
<hr>

<div class="tg-post" id="msg-76351">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22e031404e.mp4?token=QtcGC1R0fOyGsScmrs9cPvxQ0NyqsmhXeLG5Rk58gmX0FK2OprlFW8CwX14zY1EGopcelRR3x8dmkqbF5Fb8wAHAvh-fBRCBH_xpwBnVFKtS9nHAlj6GmJRuRo5Ax3GvZ97DHYNci8tgPKOUtq7XsottqylR1BbXHXIVXM6rwSkyiDNUTXLUWrOd5VaV4mxJ20gyEzS23lsB0rA_IRriHaLn5-xrgDGrf-hKc1-3fI5vdarjCDjsbDIM1QSbU9hl4OT74GaoZalIE6hWLMQdi0SpsFMyQWmYD40olwPGwoTyYJrIBQpK4J0rZGTeEGC5H2gS8sxPNeSWDZ2S4zvG7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22e031404e.mp4?token=QtcGC1R0fOyGsScmrs9cPvxQ0NyqsmhXeLG5Rk58gmX0FK2OprlFW8CwX14zY1EGopcelRR3x8dmkqbF5Fb8wAHAvh-fBRCBH_xpwBnVFKtS9nHAlj6GmJRuRo5Ax3GvZ97DHYNci8tgPKOUtq7XsottqylR1BbXHXIVXM6rwSkyiDNUTXLUWrOd5VaV4mxJ20gyEzS23lsB0rA_IRriHaLn5-xrgDGrf-hKc1-3fI5vdarjCDjsbDIM1QSbU9hl4OT74GaoZalIE6hWLMQdi0SpsFMyQWmYD40olwPGwoTyYJrIBQpK4J0rZGTeEGC5H2gS8sxPNeSWDZ2S4zvG7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر توافق و توقف جنگ در شبکه خبر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/VahidOnline/76351" target="_blank">📅 01:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76350">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hVYnMHpxc9i9pbpOiYCFUqYHZzVoHP8OjFo5vM0iGmFAH5rdHTYNLUXuIJSs8UuK8JdNxdBIiaAcTFms1ewy99vlxKJneSad5hdIsPUdvlhFjUAzz8tO3UM5gwibSWtk79pt58hN-1u2fSCSSCBqlzM3tSBIOvyDcwaRNK_FMM_ru3tiCQrwXm143hRq8ZZ24QBv8HCve8HoQE6sxufBI0re9Rusb943f-idv5h5ZDNLTrjrapphyA89p-E-mr4w7QKqeDkYHGJgsAd26AgXYJ79eQhjfxchfFJvz35NQcg7KLH9Ue37xAjKd6DA6rC6UDX9gF4q-KJeBRudBavnjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: تبریک به همه، توافق نهایی شد
پست ترامپ ترجمه ماشین:
توافق با جمهوری اسلامی ایران اکنون کامل شده است. به همه تبریک می‌گویم!
بدین‌وسیله من به‌طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را صادر می‌کنم و هم‌زمان با این، مجوز برداشته شدن فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
کشتی‌های جهان، موتورهای خود را روشن کنید. بگذارید نفت جریان پیدا کند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/VahidOnline/76350" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76349">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LWqbBZOBNzLrUunFEo6gzDQh4mJVfrYrXvbAJ_wFbMaznC__g_tFJz4W0hYuKqTgFv2jU-T58BpGnmfeau_oT6GrQhP7ryZCT0iTzntyNklgl72CSCGp7QYBdeDxGhZnQP_RgTDrYhUtjpK2RshOEDRLv45dAwN-YOCPkZ8wNIaNdu29wsnGG_hgdhVTeJR7IfOPup-uqctZxNi5jS-X0uKA-SZcpCpUbW46Eqz2XchRDoM7A0blaHRtg5S4Ls7fg1EZ7N7firEabSoDQ9L-DD55Q3-FYaxscdo-8V5j5MrDiqFBmbh56MhxYBVdOJ7cn2wzG1PyUNUnMhuqOQdgDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبر:
نخست‌وزیر پاکستان از دستیابی به توافق و پایان جنگ خبر داد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/VahidOnline/76349" target="_blank">📅 00:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76348">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I0MoJ7Hra9UEnXQKfh_a5NAaTGjyK4mCb2mHNAwkSRzmctSU4DSGgpkpukdmIl8zZK__azZRdoMLFUbgNVQkchTmBjoPSwbeMBb2IG0WGbjh09DSbBEPD-LwPJb-p-vXS061H8L9RNWkkBbVCu3ADqfuGoiPgd8FLmNWNAXJ_W9S-f-aO9pDOVh49UNVAICqLpPsE6p_3QAKwuz21IGThmRTbEvpGd6X-G6FiBD82lQ-apbGCP6R02jgG6UgiDpxVGJEfMc2uidK_c0ZScHRnQLtJsUBMjkRdjj6YhzmVw1I9GL5Ut3_pACoDaJmpMWrg9X6osaXKEaB3lgd3HM2ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
نخست‌وزیر پاکستان: توافق حاصل شد
مراسم امضا جمعه در سوئیس امضا می‌شود
پست شهباز شریف، ترجمه ماشین:
در پی مذاکرات فشرده، خوشحالیم اعلام کنیم که توافق صلح میان ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شده است. هر دو طرف پایان فوری و دائمی عملیات نظامی در همه جبهه‌ها، از جمله در لبنان، را اعلام کرده‌اند.
مراسم رسمی امضای توافق روز جمعه، ۱۹ ژوئن، [۲۹ خرداد] در سوئیس برگزار خواهد شد.
مایلیم از ایالات متحده آمریکا و جمهوری اسلامی ایران به‌خاطر تعهدشان به یافتن راه‌حلی دیپلماتیک برای این مناقشه تشکر کنیم. همچنین مایلیم قدردانی صمیمانه خود را از برادرانمان در این تلاش میانجی‌گرانه، رهبری بزرگ دولت قطر، به‌خاطر حمایتشان در دستیابی به این توافق ابراز کنیم. به‌ویژه از رهبری دوراندیش پادشاهی عربستان سعودی و جمهوری ترکیه نیز به‌خاطر مشارکت‌های عظیمشان در این زمینه تشکر می‌کنم.
اکنون که توافق برقرار شده است، میانجی‌ها مجموعه‌ای از نشست‌ها را در این هفته تسهیل خواهند کرد. این گفت‌وگوهای پیش از اجرا، زمینه را برای مذاکرات فنی و مراسم رسمی امضا فراهم خواهد کرد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/VahidOnline/76348" target="_blank">📅 00:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76347">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cb9bbe1383.mp4?token=BrJcnax2WOTBmyOkeEdMP-wUW8CWbWeCzIqOf9uYoGMky8z1WGkQB2zYM7U__nvulDuz2u7CNZz5SLpbkx5QBwf1oD-rodku39LUFZWqcnCoHdojw_LPQLkrK9RHfS8u5x-xc_6j-sa36X315S-V03uNNOXz3pBYOUGeJxauj1BwnQfJ1waBzeM9BzLF34gHlUXHFXJZ6WTjqEYnxdnZQEDviUbmheiSl5E7MQkFqKMV1UXzXBGVyqZrU2PkzcZiUfJLaqEUHngTrZ39tQN24FGg8X7V3plfgP3pTrPiRYVi7hZyGohnSxDSif3A0Rz6EgGNghlhYvjHq9W3T4NymA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cb9bbe1383.mp4?token=BrJcnax2WOTBmyOkeEdMP-wUW8CWbWeCzIqOf9uYoGMky8z1WGkQB2zYM7U__nvulDuz2u7CNZz5SLpbkx5QBwf1oD-rodku39LUFZWqcnCoHdojw_LPQLkrK9RHfS8u5x-xc_6j-sa36X315S-V03uNNOXz3pBYOUGeJxauj1BwnQfJ1waBzeM9BzLF34gHlUXHFXJZ6WTjqEYnxdnZQEDviUbmheiSl5E7MQkFqKMV1UXzXBGVyqZrU2PkzcZiUfJLaqEUHngTrZ39tQN24FGg8X7V3plfgP3pTrPiRYVi7hZyGohnSxDSif3A0Rz6EgGNghlhYvjHq9W3T4NymA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی منتشرشده در شبکه‌های اجتماعی نشان می‌دهد جمعی از حامیان تندروی جمهوری اسلامی کفن‌پوش شده و در تجمعی مقابل استانداری زنجان شعار «اگر چیزی امضا شه، مسئول باید کشته شه» سر دادند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/VahidOnline/76347" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76346">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KGcuIsXtvcRVCdjgJpHppRhNn3ocCdFsALRrU52JHOMBfgJeWWXT_fG8jVX9cJx0S7m12sxTN-vZSl412Z13Io1MqX5hLVlLLIwxexcluqQ_SAd-pJJtt5_2KGKHoK9SeHtUm2M3JxeHkKxGPfSKovyRSDi1RsriLCBPej7PnVdgKuGqBhXWookC-oZiuxOcdXR5vbj35xXFWOD4vp1RzWysMWGMq-nVJ1W6wQWYdqHLtqYbRWKXEHCVLlNGKldLIQ-wkNIKpWcuhSROgZ3jkqYffFrpeEXuEhU0UQSCoqIUINToM85Tqc3K6G3Wuz-fONLnTl3VcCSwncQ6J5KR6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در گفت‌وگو با
وال استریت ژورنال
گفت توافق با جمهوری اسلامی قریب‌الوقوع است، اما تهران هنوز موافقت خود با آن را تایید نکرده است.
ترامپ افزود قصد دارد به‌زودی بیانیه‌ای صادر کند که در آن اعلام خواهد شد آمریکا با جمهوری اسلامی به توافق رسیده است.
او گفت این توافق، در صورت نهایی شدن، یا توسط خود او یا از سوی جی‌دی ونس، معاون رییس‌جمهوری آمریکا، به‌صورت الکترونیکی امضا خواهد شد.
رییس‌جمهوری آمریکا روز یکشنبه این توافق را گامی بزرگ در مسیر پایان دادن به درگیری نزدیک به چهارماهه توصیف کرد.
ترامپ همچنین گفت این توافق شامل تعهد جمهوری اسلامی به دست نیافتن به سلاح هسته‌ای و بازگشایی فوری تنگه هرمز خواهد بود. او افزود عجله‌ای برای خارج کردن مواد هسته‌ای از ایران وجود ندارد و این موضوع می‌تواند در مرحله‌ای بعدی دنبال شود.
ترامپ گفت: «بعدا و زمانی که آماده باشیم وارد عمل شویم، مواد هسته‌ای را جمع‌آوری خواهیم کرد. به نظرم طی یک یا دو ماه آینده این کار انجام می‌شود و عجله‌ای وجود ندارد.»
@
VahidOOnLine
نقل خبرگزاری فارس:
ترامپ: به‌زودی بیانیه‌ای صادر خواهم کرد که تایید می‌کند آمریکا با توافق با ایران موافقت کرده است
🔹
این توافق به‌صورت الکترونیکی، یا توسط من یا توسط معاونم ونس امضا خواهد شد.
🔹
توافق شامل تعهد ایران به عدم دستیابی به سلاح هسته‌ای و بازگشایی فوری تنگه هرمز خواهد بود.
🔹
ایران هنوز موافقت خود با این توافق را تایید نکرده است.
🔹
هر زمان که آماده باشیم، مواد هسته‌ای را تحویل خواهیم گرفت و این اتفاق ظرف یک یا دو ماه آینده رخ خواهد داد.
🔹
من خواهان پایان یافتن حملات هستم و ایرانی‌ها هم می‌خواهند که جنگ تمام شود.
🔹
من هیچ‌وقت به دنبال تغییر رژیم ایران نبوده‌ام.
🔹
بازرسی‌های بسیار دقیق و شدیدی از ایرانی‌ها به عمل خواهد آمد.
🔹
در این توافق پولی به ایران داده نخواهد شد، اما احتمالاً تحریم‌ها لغو می‌شوند؛ باید ببینیم در عمل چگونه رفتار خواهند کرد.
🔹
محاصره دریایی اعمال‌شده علیه ایران موفقیت‌آمیز بوده و تاثیر آن از حملات نظامی هم بیشتر است.
🔹
نتانیاهو از این توافق حمایت می‌کند؛ این توافق برای او خوب است چون تحت هیچ شرایطی اجازه نمی‌دهد ایران به سلاح هسته‌ای دست پیدا کند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/VahidOnline/76346" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76345">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k23bYUIstp4ZdKnNQGO_WI3SGgN8-pq6mtUTd6XGtYT7wi8wpcjaxqCo3KwaGk31jOpBBPAwhJXMoaNzu5H4xbr9F0HNrUjx5j7-uyQhxbpckZDb4CVMp-Gig-m1IMERM4PAnVj34tlE5W0lwtKbDuagluKwpTafTB7Rz84ZSpwxGruoR6ZzWmaSEOggLCf3IR9zjf8aDm_r0Tvq0Qy_Ny_A6-m6OHF4GG6XTUfteSGMkNEC99IlX0qTktUEXh0e2ZdzAS8wwxPIFFWJEwK3z-vrvtU4_9sGD8ViAGrGbY5-8buutY55GGjMH96sNdj3Ih5ZsnV5a8UJTLCYRL-tRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «کانال ۱۲» اسرائیل، بنیامین نتانیاهو و دونالد ترامپ لحظاتی پیش به صورت تلفنی گفتگو کردند و رئیس‌جمهوری آمریکا، نخست‌وزیر اسرائیل را در جریان «پیشرفت‌های کلیدی برای امضای توافق با ایران» قرار داد.
مقامی ارشد اعلام کرده که احتمال امضای این توافق «حتی طی همین امشب» (بامداد دوشنبه به وقت تهران) وجود دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/76345" target="_blank">📅 00:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76344">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پست‌های ترامپ، ترجمه ماشین:
سناتور جک رید، یک «دموکرات» از رود آیلند، وقتی گفت توافقی که ما همین حالا انجام دادیم به خوبی فاجعه اوباما، معروف به برجام، نیست، دروغ گفت.
رید یا یک کلاهبردار تمام‌عیار است یا بی‌کفایت.
توافق اوباما مسیری به سوی سلاح هسته‌ای برای ایران بود، همراه با پول نقد و همه چیز؛ یکی از بدترین و احمقانه‌ترین توافق‌هایی که آمریکا تا به حال انجام داده است؛ به همین دلیل هم می‌گویم «دموکرات‌های احمق»!
توافق ما دیواری در برابر دستیابی ایران به سلاح هسته‌ای است؛ درست نقطه مقابل اوباما.
جک رید را استیضاح کنید!
(توضیح ماشین: در متن اصلی چند غلط املایی عمدی هست: Dumocrats به‌جای Democrats برای تحقیر دموکرات‌ها و Obuma به‌جای Obama.)
realDonaldTrum
ویکتوریا کوتس از بنیاد هریتیج واقعاً فوق‌العاده است! او موضوع را مثل تعداد کمی از دیگران می‌فهمد. متشکرم ویکتوریا.
ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز هم به‌زودی برای تجارت باز خواهد شد!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/76344" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76343">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iMPr40c5cY0SsWJAcNWCgYPf9R_KKqJv3IsimHFQai6FFpJ_OpOolPMMYKC6OVhuOQp3EqwL0ol4qxcyht4P1xH9reY5EosA23DnHd2m6CMm1-lSji8uxUmdRIN4utjNlRO51DidQc3wCbe4j8OWO4iBlsqXyBus-xrU877b6Q9ywZp7jpWwoStjyXGWd4TAs_hyrUfOnDdE2O3bgbqahLUCjLSfd2ATes6yHoGV8VRdeGHfByJXZ-ckNu_13cWp8mh3vxMT116fjsPEhXKWbKXEtRYz-hg60yrJsKCfqR8VhkDo3Z9gl54Am6tAmxAGX0Crvcjc4VXyzo8agi68wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، در واکنش به حمله اسرائیل به اهدافی در جنوب بیروت در
شبکه ایکس
نوشت: «مجاهدت‌های رزمندگان لبنان و دیپلماسی مقتدرانه جمهوری اسلامی حاکمیت و تمامیت ارضی لبنان را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی اسرائیل را بر هم خواهد زد، بچرخ تا بچرخیم.»
قالیباف تاکید کرد که هیچ‌یک از ارکان مقاومت را نمی‌توان «تک و تنها» قرار داد و حاکمیت و تمامیت ارضی لبنان حفظ خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76343" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76342">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nXWFyMoCq1qNG2MUK8Dgr1CRLapyS6spy0edIlxc962CeuyQiCwPuIF3ke78IU_mmdJ5dybH67ByyK_uN3DdrCVC8bK5NeJIaI8ZUFd44EXenlBN-TWB0z28mFYHHNtpR6TUalyIPKnDQwl1jqxyZWLjPGGYBqq1ns_GVnk_diF9E6tS8SZA1ZR7UpU0HKYN9EjEHgMYkB2Raqx_0OXZLMGR1Pux23GSpChw51a5jsa-hLoZv7J2z0Oh9yQm6xMOtN4a8pu7Hj88xWrO4SCJa-SNtepTvfCymgHWWvudzGw8xyOz3sAgCPbqQ_WDfCdGqJmyG9v9k02bN62XiBf0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم و صدا و سیما:
پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است.
این تصمیم در پی شرایط موجود اتخاذ شده است.
سازمان هواپیمایی تا این لحظه هیچ نوتامی منتشر نکرده است.
خبرگزاری مهر:
هیچ نوتام جدیدی درباره محدودیت پروازی صادر نشده است
🔺
مجید اخوان، سخنگوی سازمان هواپیمایی کشوری در گفتگو با خبرنگار مهر درباره برخی اخبار منتشرشده در فضای مجازی مبنی بر صدور نوتام جدید برای محدودیت پروازی در فضای هوایی کشور، اظهار کرد: هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
🔺
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76342" target="_blank">📅 22:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76341">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/201a6972d8.mp4?token=rI9s8B3MliyPgBuTzw7ynUbJl9Q4cTLsLoFpS0NuAhiH3bPXy_kLREuuEmxfRNbr4gl_uTrJngKx31gbk0rmdsVrmg0IB6p5ipvPhRibkU4PHQDGxVWILDrqlihMpZhY02vXjcInhVbn_gQA8V9JpYXm42useHQx_9KCOhGwA09pShT9uYX2SNjMuPCrEMR0NMDXZ7zwxUlnma6Gx0bSdCF5WpDUknmT1l6-6irN8JhYrudWMjHPhrfp1D8f7ovdkMPBl7wgAZsCym0N8moJjwSSTInOZ_fqo3K51G2xdbCS2anNq91JuJR1cjdSeQ1fKfVTt_lUT-OTxcQIE9wd1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/201a6972d8.mp4?token=rI9s8B3MliyPgBuTzw7ynUbJl9Q4cTLsLoFpS0NuAhiH3bPXy_kLREuuEmxfRNbr4gl_uTrJngKx31gbk0rmdsVrmg0IB6p5ipvPhRibkU4PHQDGxVWILDrqlihMpZhY02vXjcInhVbn_gQA8V9JpYXm42useHQx_9KCOhGwA09pShT9uYX2SNjMuPCrEMR0NMDXZ7zwxUlnma6Gx0bSdCF5WpDUknmT1l6-6irN8JhYrudWMjHPhrfp1D8f7ovdkMPBl7wgAZsCym0N8moJjwSSTInOZ_fqo3K51G2xdbCS2anNq91JuJR1cjdSeQ1fKfVTt_lUT-OTxcQIE9wd1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شماری از حامیان جمهوری اسلامی و مخالفان توافق با ایالات متحده، در تجمع خود با سر دادن شعار خواهان اعدام عباس عراقچی، وزیر خارجه حکومت ایران شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76341" target="_blank">📅 21:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76340">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gPDuAIbqu6NfzoUQc3mjoOlidUTB-nbTO68_hXRUpqDUbhMbSJ8BQVxNJOu8YBjWyoqwYNTpu7AwqXEivpurPegE1HJ0eKbdmxuvAfcZzeVDfpRlyA9sWhi62JFsT43epUj53spK5-od3DF-VRPQMTwpovZmJg4uHAswtOLbnP5rRsvW2zhMzqwwQcs0X5mT8CaClnyTGjUnDaGRFxyIHgcm5x3eFF2lKZRc66xySuF9M-yvV5Q6NWMpGaukvH_MDVX0aywEvBHZBbKCNuQrQr0Fly2E9pRr5YHQzFDGypNY4duwKuRw6zusVE7JBjtjBQCei4F11FnKePIskcHW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"‏پاسخ رزمندگان اسلام در پیش است."
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی در جمهوری اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76340" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76339">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MP81C9seSRtE2lP8_hw1jyHmFN4FkPYKbstXaS116gL0kdz8FG7aMULvJ40JKul1gLE8loio-bSFt5k4HgLgREypG8xHi5LwV3pM4_C5GxYfJFeC8jsn1v9r8QVmS4sWeDibmGhQef-stGCPzqdDABLQuKhpyX5Dx0SbhRTRPw9NnllGC9hDcGDOYmN2_MgYeKMzz1pbacyyYmjcScMApG8XGj4NS95oMD8BA1HwRQrbejuVwhTkzp7fuu_dWD9jDunMZYQAytXa4IYqGTFyGhr7BWqDUtB3tuM6wH5Xc6a_7fBbZdLwzoF_IjD_TgobniAqEvh34FRR4qbuvsOAew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب تصاویر #مجتبی خامنه‌ای و آدولف #هیتلر با هم عکس جعلی چهره رهبر جدید جمهوری اسلامی (دستکاری شده با هوش مصنوعی) رو با استناد و افتخار به سخنان جعلی و چرندیات هرگز گفته نشده آن جنایتکار دیگر منتشر می‌کنند. عکس دریافتی از بابلسر، سه‌شنبه ۴ فروردین Vahid
📡
…</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76339" target="_blank">📅 20:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76338">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXbYBQjctftdS5TNR1BVRNKOaWDNliAxDByoLQGwrbe5wYyWg-8FjFbelgAQpv4Ryma93uD6IfTUoAztOGqJzgWk39tZ30fY16QGWpq7FwiqqbaADa4IiUHn3jC6KIVS0tjxrZ_aNrRzdxDCos_uVK8rKNbZDF6N5SDiLWL0bDkdmi3uLHsJj9rSU79rWyc63oioYUJVteg1OpR7jFp8LFYIPDH2cJtIHety77pTARlWR92sdWp72ezumaeyLX-76qeJP5BzHe6qjgJNs_V8KwV6cHn4i2IUGj-3DcUW1v-ebt2DzGYGQjxjXdVlLmsuHKZPvJ2QI5TgNeSSmcU13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، در پی انتقادات برخی حامیان حکومت از محتوای توافق احتمالی با آمریکا، روز یکشنبه گفت که روند مذاکرات بر اساس مصوبات شورای عالی امنیت ملی و دیدگاه‌های رهبر جمهوری اسلامی پیش می‌رود.
او در دیدار با مدیران رسانه‌های داخلی افزود: «تصمیمات راهبردی کشور باید در چارچوب سازوکارهای قانونی اتخاذ شود و همه جریان‌ها و گروه‌ها نیز خود را ملزم به تبعیت از این تصمیمات بدانند.»
در آستانهٔ امضای تفاهم‌نامهٔ ایران و آمریکا برای پایان جنگ، اعتراض‌ در میان حامیان تندروی حکومت به متنی که به‌عنوان تفاهم‌نامه در برخی رسانه‌ها منتشر شد بالا گرفته و تجمعاتی نیز توسط گروهی از طرفداران جمهوری اسلامی علیه این تفاهم و مذاکره‌کنندگان برگزار شده است.
در یکی از این تجمعات در تهران، تجمع‌کنندگان علیه عباس عراقچی، وزیر خارجه، و محمدباقر قالیباف، رئیس مجلس شورای اسلامی، شعارهایی سر دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76338" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76337">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c24456e9d.mp4?token=mQYCusf2fc6Df_fPEHOV9L9OdoKIVqxA7ewZo45oEd4WI0VDYgxZanWcPH-aWuEKOYbBKDy6hDluLflIFIsnqDGOIROvQkkd6mubHE4JFa89-lUcMGMf16aWzy0TecYLYkvSLbL174is2W8N63Wu3B1et3sgWE611yMvbZUHXgkRARQwea_4Wf3ywOSwU_v6a2XF4TzHva2_OL9np9cENy87ZcaGyjrETFbfGgtdCPA9AtTzgOHgGa7ubPClFCVPw2ZMVVjxlINuk86oWdCGBcZb5hxaQY6jmfd1E5BAzdl5dRoi9EMivhOKS9gFIy73CsOrCwMgm4K4gZ-E6qWn-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c24456e9d.mp4?token=mQYCusf2fc6Df_fPEHOV9L9OdoKIVqxA7ewZo45oEd4WI0VDYgxZanWcPH-aWuEKOYbBKDy6hDluLflIFIsnqDGOIROvQkkd6mubHE4JFa89-lUcMGMf16aWzy0TecYLYkvSLbL174is2W8N63Wu3B1et3sgWE611yMvbZUHXgkRARQwea_4Wf3ywOSwU_v6a2XF4TzHva2_OL9np9cENy87ZcaGyjrETFbfGgtdCPA9AtTzgOHgGa7ubPClFCVPw2ZMVVjxlINuk86oWdCGBcZb5hxaQY6jmfd1E5BAzdl5dRoi9EMivhOKS9gFIy73CsOrCwMgm4K4gZ-E6qWn-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: به نتانیاهو گفتم داری چه غلطی می‌کنی؟
ظرف دو سه ساعت آینده یک توافق بزرگ امضا خواهد شد
به ویدیوی بالا با هوش مصنوعی زیرنویس فارسی اضافه شده، متن دو دقیقه اولش:
«بله کوین، عصر بخیر. همین الان با رئیس‌جمهور ترامپ صحبت کردم. او به فاکس‌نیوز گفت که معتقد است یک توافق بزرگ با ایران ظرف دو تا سه ساعت آینده امضا خواهد شد.
از او درباره حملات امروز اسرائیل علیه حزب‌الله در پایتخت لبنان، بیروت، پرسیدم. او گفت با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، تلفنی صحبت کرده و از او پرسیده: “داری چه غلطی می‌کنی؟” ترامپ گفت به نخست‌وزیر گفته بود این حملات علیه حزب‌الله را انجام ندهد تا بر پیشبرد این توافق اثر نگذارد.
اکنون اسرائیلی‌ها، به گفته ارتش اسرائیل، خود را برای احتمال شلیک موشک‌های بالستیک ورودی از سوی ایران آماده می‌کنند. رئیس‌جمهور ترامپ به فاکس‌نیوز گفت از ایران خواهد خواست با شلیک موشک به سوی اسرائیل پاسخ ندهد، چون این توافق در آستانه امضا قرار دارد و انتظار می‌رود امشب امضا شود.
همه اینها در پس‌زمینه تازه‌ترین گفت‌وگوها برای رساندن این توافق نهایی به خط پایان رخ می‌دهد. رئیس‌جمهور درباره حملات میانه هفته گذشته هم صحبت کرد؛ زمانی که آمریکا بسیاری از مواضع ایران را زیر ضربه می‌برد و ایرانی‌ها را به میز مذاکره برمی‌گرداند.
شاید یادتان باشد، کوین، من با رئیس‌جمهور تلفنی صحبت می‌کردم، در حالی که او در اتاق وضعیت بود، و ایرانی‌ها با او تماس گرفتند و از او خواستند بمباران را متوقف کند. رئیس‌جمهور معتقد است همان لحظه توانست معادله را تغییر دهد و دوباره ایرانی‌ها را وادار کند این امتیازها را بدهند.
رئیس‌جمهور ترامپ گفت اگر آنها امشب توافق را امضا کنند، او فوراً دستور خواهد داد محاصره بنادر ایران برداشته شود و سپس وارد گفت‌وگوهای جزئی‌تر درباره برنامه هسته‌ای ایران خواهند شد.
اما دوباره، مهم‌ترین خبرهایی که اکنون می‌دانیم این است:
رئیس‌جمهور ترامپ به فاکس‌نیوز گفته معتقد است توافق با ایران ظرف دو تا سه ساعت آینده امضا خواهد شد. به گفته رئیس‌جمهور، این امضا به‌صورت الکترونیکی انجام می‌شود و حدود یک هفته بعد انتظار می‌رود مراسم امضای حضوری، احتمالاً در جایی در اروپا، برگزار شود.
باز هم تأکید می‌کنم: رئیس‌جمهور پس از حملات امروز اسرائیل به پایتخت لبنان، بیروت، واکنش نشان داد. اسرائیلی‌ها در پاسخ به آتش پهپادی این هفته از آن سوی مرز به سمت شمال اسرائیل، مواضع حزب‌الله را هدف قرار دادند. و رئیس‌جمهور می‌گوید از نخست‌وزیر اسرائیل پرسیده: “داری چه غلطی می‌کنی؟”»
TreyYingst
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76337" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76336">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MCw1RhOoAAUxxJ6_BTNUYKnvU9SRhTbczjQLqCkjX9nCS860_raSgNyfsAxIABuaTTsfBcHmOFwn_U7xgN4MMNoEPTbEiOfxfYdIhnlOwo-SYgIx7u1TcrGIPkrbWB-lfti_-375wq3k1U7jiuIgITrM5HBrkdwVQ1m8Te_YuHUZGu46yW-LhRBscWPAW_2HyDkpX6YTXTkbyAFmabG8cLNekJsD5XAUq0B4wkUuCSuPR-1bTy-BDpTF4haiRZJFDB0T67peJWRvd3UP3hfNaFRCDT9C4wVkUanlJ9WBeE3ZmeN7SJKz2VlNUrf-Z7nzL1kngOBRnaUkqIM09oS5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی، فرمانده نیروی هوافضای سپاه پاسداران، در پیامی از حامیان جمهوری اسلامی خواست در مسیر تحقق آرمان‌های نظام، از مجتبی خامنه‌ای تبعیت کنند.
او نوشت: «ملت بصیر و غیور که در خونخواهی علی خامنه‌ای مبعوث شدید و در راه تحقق آرمان‌های بلند انقلاب اسلامی با مجتبی خامنه‌ای عهدی تازه بستید، هوشیار باشید که از شئون متعهد بودن، تبعیت کردن است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76336" target="_blank">📅 19:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76335">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FmhaNtnAdrp3rBycerby8GQRQh6k34hnEHMN-r7McjLgZZJfWN64gUIYviYyputDM16zoByhdx-PNurEGWxG-tnVYwzUzASUm-_e9RcBb2SPbLcidyidXMx7JzpJyvxeOiq4KxG5pAyNpTmCczmKjGPGacbc58BBt_l3dCGlIBElmD2n7bxgRbIPjqTktbiPfyDKU8GGD-SN_KT5em3E6VXHovgAJpt_AFm7DdARSuhFpYpCo2TaXLYfl3ckpJXMX9PhrZEsKpJ5NHLvQK3D-S6cfLBUHbOsAQIpOwkB5R-S2Fot0iu4YdAdFQRNVK81XnyAXMpw4UZ-nIPHWwMvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: بیایید خرابش نکنیم!‍
پست ترامپ، ترجمه ماشین:
حمله صبح امروز به بیروت نباید اتفاق می‌افتاد؛ به‌ویژه در روزی خاص که ما تا این اندازه به توافق صلح با ایران نزدیک هستیم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در پاسخ به آن انجام شد بسیار کوچک و بی‌اهمیت بود؛ هیچ‌کس آسیبی ندید، زخمی نشد یا کشته نشد، و نباید این روند مهم را مختل کند.
ما به توافقی بسیار نزدیک هستیم که صلح را به منطقه، از جمله لبنان، خواهد آورد و همه طرف‌ها باید عقب‌نشینی کنند. دیگر نباید هیچ حمله‌ای از سوی اسرائیل در هیچ نقطه‌ای از لبنان انجام شود، اما همچنین نباید هیچ حمله‌ای از سوی هیچ طرف دیگری، از جمله حزب‌الله، علیه اسرائیل صورت گیرد.
این می‌تواند آغاز یک صلح طولانی و زیبا باشد — بیایید خرابش نکنیم!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76335" target="_blank">📅 18:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76331">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PaY8Pm1CPw4HokTcjcnSwpJ3M0TNiDSZealgAL9Nw33mWC4ZZ0LNpsqjCvXTta_gjbIjZNsKBb8mH-19dSGlYE9Ny3Gh7vET7XS4UjqstMnBgIDtH5c6Dy3_0wBHiv9vZw7nW9QniSse7yoDrr5YKFo9ORzECPDaa65j5qG9yce-VADFCduH4nUZBpAz7Fyz6DaSuafp6rM-SlFMmMLXFKypNRLPjdDfKzZ-GfFcwswTIjm4oIZ2neohlnE3ZAAQzv3SERz6COhdh9QSCh9zy5GRmJL3UgljbLB6NDSzje-4SzSIEUUjtG55tiVpoXHbbIDKGyzWpOAhGPsKVOatSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aBvNwkSs0EumHMJIgVf69l0o5t4cBwoTQ_CdXkb5WeIM-r7pezJeNHN1jtMLsmlB92m1PYi4FIV6GZE2AX6ZRm7-24pd3gYSlHsPyn6Qxz8LlRPWyh6dx_ENdhJFS2CKlKfimuXfktz6mOqqKtmqdMml1kTrn4KiEV-XByaZp5kmIREa-xcg9nbLHyXM8UEyL24HweSlQc7ks11ROxg-L4fNca2Fo5Wx4xPXD5bbHWgi2AsnSanwZnpPxa36WureuNb-96sdQD_dQMlhnDhvDyUvCV7xPJI8yQb65oj9y9RSVtNjEJN33PX3InutwjrgScfEPt8vBB7L2r04TwxwaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gniCyX_xMeTC4J_bevEZRFn6Nv_T7dluxjlJOwsONtG0bKAa-_ez7UikZwO9iY1MGLDLrt80da0u8zailVnmKAv4O4rHDJu71OyxFdBarvE6osOo4NiFYADtJLJASZytAbdogGj-aJsT3YUQAp-Nrbc2tK59utp4RM3HIA2Nf5ojuPI4qAO-EUPUC7wtNV6foxdj6NBIOm6PR1zjfxbl7dgz7S2IrYrXvKGLKnZKk57e1GxuZKPoMH27qqbxiTq25wx2Aocfm0WxLHpbNGtDV5AWZoFdu2zeS7gqDgggzwHTgQ8LwNnm29KxD7euJSgENVIrUBUqIa_9ehGCUvey_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XqlWrqfRtjNqljid6jaUiM_-FD8n_w87ICjgd_2EM3FgDht4G6IMegTnjG7tPab0eoEjrdDaISbyq1JqIybdxuhDzWUYeAjBdxw7IPcmOPDkDNI3PaJ2RIltxP4gmQWVkG1zhGXAC15NAeaYaYRPP7E5-ZuRaBE737b9xbLRf4vMLASdVji4HRpeHXVNJYVH23GLWZKqi3o1BN7VbpmQS5zqzbjCH61DViSLPr0HSKaYsVSWwQ69ULR8EcBS1vJO353m2eHuhzfwNimZPKYsirlEGFWQZFNjQaQsQqdVGZQkt1Sr7-342jibgeb95wTuuB7AR36DNccuPGaZw0eE7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدجعفر اسدی، معاون بازرسی قرارگاه مرکزی خاتم‌الانبیا، در واکنش به حمله اسرائیل به ضاحیه بیروت گفت: «بدون شک این جنایات بی‌پاسخ نخواهد ماند.»
او در گفت‌وگو با دفاع‌پرس، حمله ارتش اسرائیل به منطقه ضاحیه را محکوم کرد و نسبت به پیامدهای آن هشدار داد.
ارتش اسرائیل در بیانیه‌ای یکشنبه ۲۴ خرداد اعلام کرد در واکنش به شلیک پرتابه از سوی حزب‌الله به شمال اسرائیل، اهدافی از این گروه را در ضاحیه بیروت هدف قرار داده است.
@
VahidOOnLine
محمد مرندی، از اصحاب رسانه همراه با هیات مذاکره جمهوری اسلامی در پاکستان، درباره ادامه مذاکرات تهران و واشینگتن، در شبکه ایکس نوشت: «فعلا هیچ مذاکره دیگری در کار نخواهد بود.»
@
VahidOOnLine
نظام‌الدین موسوی، سخنگوی پیشین هیات رییسه مجلس جمهوری اسلامی، در پلتفرم ایکس نوشت حمله اسرائیل به ضاحیه بیروت در روزی که قرار بود تفاهم میان جمهوری اسلامی و آمریکا امضا شود، با هدف بر هم زدن تفاهم انجام نشد، بلکه تلاشی برای «تحقیر جمهوری اسلامی» صورت گرفت.
او خطاب به تیم مذاکره‌کننده جمهوری اسلامی نوشت: «حضرات مذاکره‌کننده، به تحقیر تن ندهید و در شرایط تحقیر، هیچ چیز را امضا نکنید.»
@
VahidOOnLine
ارتش اسرائیل اعلام کرد ایال زمیر، رییس ستاد ارتش، پس از حمله به بیروت در حال برگزاری ارزیابی‌های مستمر از وضعیت با همه فرماندهان مرتبط است.
ارتش اسرائیل افزود بر اساس این ارزیابی‌ها، خود را برای احتمال شلیک به خاک اسرائیل در ساعات آینده آماده می‌کند.
این نهاد تاکید کرد در بالاترین سطح آماده‌باش قرار دارد و برای سناریوهای مختلف دفاعی و تهاجمی آماده است.
ارتش اسرائیل تاکید کرد شلیک به خاک این کشور را تحمل نخواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76331" target="_blank">📅 18:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76329">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UMniGdI77C0QBAIhXqIXfbpdv7gKM7NvqczVYr5n9ajET_LaH1g7LXWW1_ftKtXhvStBl-d6y49hmhvomYrc-WpRF3rkdWlbRvMGRqyrIVKq1e_UhVi3qRlrSEefp_YXODBi3klRWFVejhg9wzby0BtSdI25rbFMt8K76cSUaqofvI3eEnGo7gxrPJQOGRvGcnv27UspHerekej9Ey0tkN9Vd16DU3rIlwAO2sqq3hAKJThTMBWtr-NKrPRBWVG-4V4NXc3yHUu753sv41i30IiNPljxq-GXwS9LRtomXuf020WPufQh_T7XmHX1PCVWX3RKti7ZPVjeZIth1DR8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FxkA3SMCrwjY_NOkvgoZjfP6YY7yVoQ2tsgiEBpplK_15E3GteIyVz18871r5JibKli8SZbtm-TtCYDvNJEiwkPaTIc0-6UynVsWFgKfO_k4XONVyuaS5N5VrYk8JtXeeM7R6qfdRel0FD5ViQUVtJ_DsnvoR8mSVOTdaW8NoCmxiN6bL-Em1GjK8C4kFiYW8mot8ayAfrKXXGl9dOAY79T5CTx8kE6AtLWw8m-1f3n-lE6D3Dv6W6uB1Irl4iHuE3NwmPizK2R8Nc_t6q-KuVK_2mHV_xEPJTd_fCgLjqDlZjl6-13HiT8Oz5y4DHxkXzbG9h84QKveyJsi6G15fA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوهای توافق با آمریکا، اعلام کرد پس از حمله اسراییل به حومه جنوبی بیروت، ادامه مسیر توافق با آمریکا «ممکن نیست».
قالیباف روز یکشنبه در پیامی در شبکه اجتماعی ایکس نوشت حمله اخیر به حومه جنوبی بیروت بار دیگر نشان داد که آمریکا یا اراده لازم برای اجرای تعهدات خود را ندارد یا از توان انجام آن برخوردار نیست.
او افزود تلاش برای کسب امتیاز از طریق چراغ سبز نشان دادن به اسراییل نتیجه‌ای نخواهد داشت و سیاست «پلیس خوب و پلیس بد» دیگر کارایی گذشته را ندارد.
او تاکید کرد: «اگر اراده و توان اجرای تعهدات خود را ندارید، سخن گفتن از ادامه مسیر ممکن نیست.»
@
VahidHeadline
حساب رسمی وزارت خارجه اسرائیل، روز یکشنبه ۲۴ خرداد ماه در واکنش به اظهارات محمدباقر قالیباف، رئیس مجلس شورای اسلامی در شبکه اجتماعی ایکس نوشت: جمهوری اسلامی «مثل همیشه دروغ می‌گوید.»
وزارت خارجه اسرائیل در این پیام با بیان آنکه اسرائیل شلیک به خاک خود را تحمل نخواهد کرد یادآور شد، حزب‌الله، صبح روز یکشنبه «بدون هیچ‌گونه تحریک قبلی» بار دیگر به اسرائیل حمله کرده است.
در این پیام آمده است حزب‌الله به طور مداوم غیرنظامیان اسرائیلی را هدف قرار می‌دهد و حتی پس از برقراری آتش‌بس نیز حملات خود علیه اسرائیل را متوقف نکرده است.
قالیباف در روزی که به گفته دونالد ترامپ قرار بود توافق پایان جنگ میان ایران و آمریکا امضا شود، در ایکس نوشت حمله اسرائیل «به ضاحیه بار دیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را. با چراغ سبز نشان دادن به رژیم نمی‌توانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب قدیمی شده است. اگر اراده و توان اجرای تعهدات خود را ندارید، سخن گفتن از ادامه مسیر ممکن نیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76329" target="_blank">📅 18:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76323">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bTM60r3Mj_AMuGICTYl7KTAez6Y3zWGS_T_6XRhwrt2qNP8IeAj1AF0Pa9t5edZQX6op7_UFIVHWR4yzo4lzFnci7o2gMnBwHtyBpw-SoENNhMtfE7Eb7AWSBgzSWPHX961qRZ3hG6SzdsQ57Nuth7zq823kGwoh0Eiwk4tOaQ2c8lkHrVlNDtOGnqdJokM2dL_ML2JNsS7PtZGShGU4zVXbRV_nkskNEZxH1kQ1yuJ8sh3m-Of9B7w4AhE8NW6oZSgiuiPJO7SwAeYf0DINyFgbeMMc_Fq4Qm2R332lsoOj4xbyi4fEk_x7td-K8QQrs-0qpcXKLFfwq7vj70Icrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q_FWlP-bZ1doh_QbBfAUCZVPMuXx4UcdDMHCLfWjrhkjtYzbrk_LbP7j3lDyIexuFJkdQBiutayTGDHDyIn7t80GVrXfFsmkOQUhadvkmM53PCa-NbEar4BSorNpOGmu4OznHWFGQ7Bt8gEN2Cqz0ybLXij7IZuzOLpI4rczElSXJsLmJhnE05tCtHeiSyZmDoXGwleZcn99wi0yqT52dyRXJ6mT5MA9IuKPvtVJEa-DgWAtnHTc-UNuL62PeVDsCziMC63Ls8SthoVM768xBhzn_-aNtj1_D8Lcuuskpg0Vh9UcQIJUOv8gP12FhKlRTtOHjo6uq16nvnmUsq49pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MR2CXa1fhcNLaHSvbwjlFb86sVwdhcD_UJnpXoT_DpYEOjubJS_dSI2EIW2xH7QRlwWgyMnzJE3W9OzzZZc0VrfP6q64i5TnZinUHp7SPkuQMKsC98ndRwOswlIQTTXrt-RXAEjBaLa-067REHAO8TSlXP-Ahs1flaDZL2sGE55fKyfwYuVOAxVXdLqtALWl6tOIugzO31khhoQlUbE0LheEOqZ6n1CyUKMING9KTCQ3CMZkvsNj1d4xGWGg3Cf9biGSvUPg0CLY--6dGnFdP-V5CoGusUVGhexoSzI6jBhmLBhxMogHy4bfRPNySP4Qo7sfXSJOfxXZRgwu1C4HCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FqesJph1Q1gkHaR7egT9Y8t14LOTciwqT6fMHD_Oe9KtCsgD5-oBRmF5TW6RAPOSKsSBIa3uucYKIPZJa3DR9A5c_PoeAs1-rLlhocF2bhLkWnWcofT6tcCummbMdnKP7e6lMR5IQ5QYbpBA1Xif0I_YPSwTK4uctHss6IM4EdM5zZC8d0IRKSZHtxLWng6GroAZ67vcdm5YVG5DcyvM0B6rIInBUkPOl2CfcTmKS7TsgFKV2B2LBGoQRxVClny25_sL_uMCS7cE0h4XsI4NCxWR3-RJdjx1PQPGsc9IXjiqoi2GB1zC8lfcPt37MhGk4WgEqEEObhdIZRiAA8Blng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50b9dacbb2.mp4?token=U0voRN-BLdIX9MnsruGEsoLAfzjw71ZJ9yTO-HTnY9a6IgfYB91-p7ZL_S-yPGmOE1aTQOz8bjfHZzXbrxklUY5fLsd_RPEcn3C69u9uc-LIYafheYq8HUQzgy4CHglR7e2wGAPmQ6oIJmvgG836Wdtg_G1vZxypd7ky8F-DiLWVGEQxJd4l7UPTaGsknvqbibwJW6meQe6ae-XjFwN_6WTL_muP0thn2RMGj4yz-IzFORQS8bGMYktzk2SQrRcxfrqxyH7lKZbFPYo8lMK8riLuyV4I_zW37xIfOcwGjTNN7s1AgwI9AROp4u4sPii-eGDvLOImZLwc5LfUirfFSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50b9dacbb2.mp4?token=U0voRN-BLdIX9MnsruGEsoLAfzjw71ZJ9yTO-HTnY9a6IgfYB91-p7ZL_S-yPGmOE1aTQOz8bjfHZzXbrxklUY5fLsd_RPEcn3C69u9uc-LIYafheYq8HUQzgy4CHglR7e2wGAPmQ6oIJmvgG836Wdtg_G1vZxypd7ky8F-DiLWVGEQxJd4l7UPTaGsknvqbibwJW6meQe6ae-XjFwN_6WTL_muP0thn2RMGj4yz-IzFORQS8bGMYktzk2SQrRcxfrqxyH7lKZbFPYo8lMK8riLuyV4I_zW37xIfOcwGjTNN7s1AgwI9AROp4u4sPii-eGDvLOImZLwc5LfUirfFSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر نخست‌وزیری اسرائیل روز یک‌شنبه، ۲۴ خردادماه، اعلام کرد که ارتش این کشور سایتی متعلق به گروه حزب‌الله در حومه جنوبی بیروت، محله ضاحیه، را هدف قرار داده است.
در بیانیه ارتش اسرائیل در همین باره اشاره شده است که به «اهدافی تروریستی متعلق به حزب‌الله» در ضاحیه حمله شده است.
اسرائیل دلیل این حمله را شلیک از طرف حزب‌الله به خاک اسرائیل عنوان کرد.
ساعتی پیشتر ارتش اسرائیل اعلام کرده بود که سه پهپاد روز یک‌شنبه به طور جداگانه به شمال اسرائیل پرتاب شده‌اند. اسرائیل گروه حزب‌الله را مسئول پرتاب این پهپادها اعلام کرد.
ارتش اسرائیل روز یک‌شنبه همچنین به ساکنان چندین روستای دیگر در جنوب لبنان هشدار داد که محل زندگی خود را ترک کنند.
خبرگزاری فرانسه به نقل از سخنگوی عرب‌زبان ارتش اسرائیل نوشت که ساکنان ۲۹ روستا در این منطقه باید به نقطه‌ای دیگر نقل مکان کنند. اسرائیل قصد حمله هوایی به این روستاها را دارد.
طبق این گزارش، اسرائیل صبح یک‌شنبه ابتدا به ساکنان ۱۳ روستا و سپس ساکنان ۱۶ روستای دیگر در جنوب لبنان اخطار داده است.
@
VahidHeadline
شبکه العربیه گزارش داد علی الحاج، از فرماندهان حزب‌الله، در حمله هوایی یکشنبه ۲۴ خرداد اسرائیل به ضاحیه بیروت کشته شده است.
دفاع مدنی لبنان نیز اعلام کرد در این حمله سه نفر کشته شدند.
العربیه همچنین گزارش داد ارتش اسرائیل یکشنبه سه حمله هوایی به شهر سجد در جنوب لبنان انجام داده است.
ارتش اسرائیل پیش‌تر اعلام کرده بود در واکنش به شلیک سه پهپاد از سوی حزب‌الله به شمال اسرائیل و آنچه نقض آتش‌بس از سوی این گروه خواند، یکی از مقرهای حزب‌الله را در ضاحیه بیروت هدف قرار داده است.
@
VahidOOnLine
خبرنگار آکسیوس، به نقل از مقام‌های اسرائیلی و آمریکایی گزارش داد اسرائیل اندکی پیش از حمله، فرماندهی مرکزی ارتش آمریکا (سنتکام) را از این عملیات مطلع کرده بود.
جمهوری اسلامی پیش‌تر هشدار داده بود هرگونه حمله اسرائیل به بیروت می‌تواند با واکنش تهران همراه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/76323" target="_blank">📅 17:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76322">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBMpbuNviTszpJpCXJgDvrvZudWtitCPu4T1KkZ4aarxz99DR33EDqaU7pfe3dQxocw9670czrnkZcfCQ2wzA0Gv8z2E7jMfxrbDEztGiTzTAm5MngdiB2gnqlHhkvksSQp88LeRk-PzSME-3zxyG6og45nmidYc1VKdPl1Qx4f7U_j20TDlyNOQU-Nc0sVbY8Nsq5PlHAHebUf9jr-F3phBvccpLPed5-WZ-VHfhMSGM7IjXfpM1fZgW_UERc1BToaaSp1z_auu65e0hezpmihS61quOKHksKS1cgyPi0hNXsxfNbjFtfVtplfGdeT57A0fALAkLfVjSQ7kA7p5PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یائیر لاپید، نخست‌وزیر سابق و از رهبران مخالف دولت اسرائیل، در شبکه ایکس با انتقاد شدید از بنیامین نتانیاهو امضای تفاهمنامه بین ایران و آمریکا را «تکان‌دهنده‌ترین شکست‌ سیاست خارجی و امنیتی اسرائیل» توصیف کرد و مسئولیت کامل آن را متوجه نخست‌وزیر دانست.
آقای لاپید نوشت امیدوار است که «گزارش‌ها درباره توافق با ایران درست نباشد» و به ۱۳ مورد اشاره کرد و آنها را ناکامی و کوتاهی‌های آقای نتانیاهو دانست از جمله اینکه:
«او یک روایت بیش از حد خوش‌بینانه را به آمریکایی‌ها فروخت، بدون اینکه نقشه خطرات را کاملا برایشان تشریح کند و در میانه جنگ اعتماد آنها را از دست داد.»
او همچنین نوشت که آقای نتانیاهو «نتوانست آمریکایی‌ها را متقاعد کند که تاسیسات نفتی و انرژی ایران را بمباران کنند» و «مسئله موشک‌های بالستیک را در توافق یا حتی در مذاکرات بگنجانند.»
آقای لاپید همچنین نوشت که نخست‌وزیر اسرائیل «برنامه مربوط به کردها را پیش برد بدون آنکه واکنش قابل پیش‌بینی ترکیه و نفوذ رجب طیب اردوغان در واشنگتن را در نظر بگیرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76322" target="_blank">📅 17:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76320">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tjIz2SLWLq_-5wD0SibXDMbjC5S3gvPC4CtkN5W1WaEX8SB3t8CY1CPiz9fwe0tI_AwvSpbB5dYACsqGsMebdqwoSTeIaGFp0cDoK0OH1ODPA74KAXyvXWDWzRn1me_RhE-sTPhXf9AV1pd3qwod1yGbm4LD6kanevnuR7DhyGtXUnH-K73okZ2_ammYVkKzlahofyRFe4YNtjkUuWxkt5W6BV_NaIiyLrAMJQt4pfo-sOIm5YkhFYlpph42v467Wuo4V5mzlJgNEe_e7HFdQE6M0-bc_TNF-e2NYaFGlb-46GAa-ajmJgiqjNWKbEM6VmyIqOaDt3qCoRDS4oShKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TPhRQHRt9iiisCYY7QOTjBLG87h5C5IlhA1_oLFVmDf56dpCwWjcu5LOXeqbNmU8K1eBWiSW4uPGm_NVop3f7ygdKfreRc3rGJxgNuYznQYi55Lm__IJlA6HZSXJKo3v1WMwbEF0fvCnC2EylcXohL9ha86UmrU8PUS6o7LbltLxUOR1Hk9jVY6-49jeCHhcE6eseFuPfOKxsj93jJ42wkiA4Qz2e950Wx_gieLCSKcylavefNSSTjLeHoo4vXAMheOMf9QihEYfTZUxPhBULcyBZtA-dLXjz63qCiQkv24LPTDnMHIfFfzWjZVfQ797n4Kpmpy7Z1e5vkROOqHjnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در حالی که خبرها از داخل ایران اشاره به ادامه بررسی متن تفاهم‌نامه و نامشخص بودن زمان امضای آن دارد، خبرگزاری رویترز روز یک‌شنبه نوشت که دولت دونالد ترامپ در تفاهم‌نامه با آزاد کردن ۲۵ میلیارد دلار از دارایی‌های مسدود ایران موافقت کرده است.
رویترز خبر خود را به نقل از «مقامی ارشد» در جمهوری اسلامی نوشته، اما به نام او اشاره نکرده است.
به گفته منبع رویترز، دولت آمریکا همچنین موافقت کرده است که اورانیوم بسیار غنی‌شده ایران در داخل کشور رقیق شود.
این‌ها دو مورد از بحث‌انگیزترین موضوعات در مذاکرات جاری میان ایران و آمریکا بوده است: ترامپ بارها بر لزوم گرفتن یا انتقال یا از بین بردن اورانیوم ۶۰ درصد غنی‌شده ایران تأکید کرده و همزمان بارها گفته است که پولی به ایران نخواهد داد.
مسئله دادن پول به حکومت ایران به‌ویژه برای دونالد ترامپ حساسیت‌برانگیز بوده است،‌ چرا که او خود سال‌هاست به باراک اوباما تاخته که چرا در جریان رسیدن به توافق موسوم به برجام با انتقال پول به تهران موافقت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/76320" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76319">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3bxJ-fdhh-EDaVygs5BoM3qelorAs2UUkN-iYEuGbhZuc66XxqItYWklBvmk2wlB8xVtDXNHnjP6Aa8n2lsRPTXrQUIbVl3ix7WjMYSsOg3x2BA8UgPByNnlA0cRNxn04wAnlhP-ikhaXSVxVtKTknOMcWxGrMSEdkYGP6i3EclW0Zb6m89gEShNiWdT8XvCecj4tkB90aDShpoCBj2vqb_OMUCcQAsjjKQ128nQenAV3WWmC3yMSWJZFH5JvGrahvTeKh5risIUE-8jsxfFxwJWNFdo-dFCb4xAxPvetmKvzvs3WVzCWPw_qMESq4FNd3DWTWvPOa4s9gLNLkFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع دیپلماتیک گزارش داد مذاکره‌کنندگان قطری پس از رایزنی با آمریکا راهی تهران شده‌اند تا با مقام‌های جمهوری اسلامی درباره کاهش اختلاف‌های باقی‌مانده و نهایی کردن تفاهم احتمالی میان تهران و واشنگتن گفت‌وگو کنند.
رسانه‌های ایران نیز گزارش دادند این هیئت قطری به تهران سفر کرده است.
این سفر در ادامه رفت‌وآمدهای دیپلماتیک قطر انجام می‌شود. چهارشنبه گذشته نیز مذاکره‌کنندگان قطری پس از مشورت با طرف آمریکایی به تهران رفتند و درباره متن احتمالی تفاهم با مقام‌های جمهوری اسلامی رایزنی کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76319" target="_blank">📅 17:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76318">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3bec2d43bc.mp4?token=NqMCviQ1RkbRI24-MAy7S-SSrveCMnig2NZtgWdDeQzXO8xCNfePbN3Z5FTIQs2yzsGnOQw3V5xjPnCKiU5EtZschFS1mRqd4tTF0ZbhBQb11hF2bDZWICvcQeSF6UPqz38CRTKazDDeIIH3CgQmrFSAWU7kRP3EK6ZdPk7zfPx5mgcERLsQZUrAeIuATUdmKKBffD_aLQbJxSwXsD4J_4wER1Tv8v8oy08EZM5k4lmO7JysOFs2QM8GMohCPrcW4ZT91-I5T8JCCJf93d52ubQGCTuXkSWriX_fm3vzijZWWlvMCMTNVLR3jjDvXtDikJKplL2YwGlFhtW5wm9UjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3bec2d43bc.mp4?token=NqMCviQ1RkbRI24-MAy7S-SSrveCMnig2NZtgWdDeQzXO8xCNfePbN3Z5FTIQs2yzsGnOQw3V5xjPnCKiU5EtZschFS1mRqd4tTF0ZbhBQb11hF2bDZWICvcQeSF6UPqz38CRTKazDDeIIH3CgQmrFSAWU7kRP3EK6ZdPk7zfPx5mgcERLsQZUrAeIuATUdmKKBffD_aLQbJxSwXsD4J_4wER1Tv8v8oy08EZM5k4lmO7JysOFs2QM8GMohCPrcW4ZT91-I5T8JCCJf93d52ubQGCTuXkSWriX_fm3vzijZWWlvMCMTNVLR3jjDvXtDikJKplL2YwGlFhtW5wm9UjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: مقاومت باعث جنگ شد
[اینطور برداشت شده که داره میگه نپذیرفتن شرایط طرف مقابل در مذاکرات منجر به جنگ شد]
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران شنبه ۲۳ خرداد در شبکه خبر و در پاسخ به پرسشی درباره علت دو جنگ اخیر گفت: «مذاکرات علت جنگ نبود، مقاومت تیم دیپلماسی در مذاکرات علت جنگ بود.»
این گفته‌ها که در تعارض با موضع رسمی نظام جمهوری اسلامی و شخص علی  خامنه‌ای، رهبر پیشین جمهوری اسلامی به شمار می‌رود، با واکنش تند رسانه‌ها و سیاستمداران جریان اصولگرا مواجه شد.
علی خامنه‌ای، رهبر جمهوری اسلامی ماه‌ها قبل و پس از «جنگ ۱۲ روزه» گفته بود دشمن هر جا احساس کند که ما ضعیفیم، حمله می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76318" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76317">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DO8Q6z3fApmGcxDHtgEm27Dc_HlgXl-kHWuqJg7CnYrXj3wIv9RXbhl35swjC-FQbrBskdtHrBr4-NKyJvTqoegdUOiOcNftgbmG-kQFzMZCCk_GhjES0vDJ0sANxOyrpRZRTFmQNmrXkarPqERxkD-E3U5dr_Eyl5eT6YlrbPprzZBg-QSPp1kQZHJ18qseCr32uESA0hGX6vN3v_XB_OdyumkFL_H7KB3z9F8feK6XNR2cxYgvqFs7Y9vlnnbPqQFTDB7ivX2fDZ3F-0roF-JKYTNUmunaEF-Z5j31Rrx2tsfwgAK-Ux3xjbuVQskd7qPQxeOqYWCrKwns4zAVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی در اطلاعیه‌ای مدعی شد یک فرد متهم به تلاش برای نفوذ به مراکز داده، یک هسته چهار نفره در جنوب شرق کشور و ۱۲۶ نفر از آنچه «لیدرهای میدانی شبکه خرابکاری خیابانی» خواند، بازداشت شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76317" target="_blank">📅 17:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76316">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il_qMMo7aqKE68HsdOz_thHLqMOFElErLc442LeiF7swcepLDO0Zf47GZTxCIXlJqna4I-NnZwE6amVKFGqoxdDNcivmbOp1quxtLI1ogiLjz1eCOH5LYlI9XC-_woKU-uvOjFUk2a7gKozCPWET-DWY9qZNRxwFEKAunyJBwKuytk9wx8NCRlveXGg_Glgxp0ueis814mnCXVawaJuLHdZ0Dn5qM2B0JKMgQJMn3kpeesIBmV-FSmih6NSfK6R7m92LwAcdD7oFJU__nl1un5ucMUq8KDamdIMQHt2pP2VVCnT1AOMkJYln6dPekjG_m7kMjqHSXUkyOrg1jI-RxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود طراوت‌روی، نازنین سالاری و مسعود احمدیان، وکلای دادگستری، به حبس و به عنوان مجازات تکمیلی به دو سال ممنوعیت خروج از کشور همراه با ابطال گذرنامه نیز محکوم شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/76316" target="_blank">📅 17:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76315">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT8VwBnTZ6S5MFTSN9NuAOID6u0bzzuvL8Urkyb7aVjYUDouev0T_JHSb2huCXAfn_elaScu9Dec5RRmu0KfdEXfK2pnprl_Y2g8hc1fCVUgLWJq8BYo8ya2g9gWy7IPQGHcPRBJagOPnHz0B6IgrTJR566TcdJOUUetp8M8roMU48EPMF4etU5qIQRPevDoc3joxZR6R_G7pcnasoaSJyDXPFxr0WORufHuOX_cX38V-J7JHT1kWx4oYJnc2BUmhxWv2OKXVCKDAJiIqBcS-X4kuwCoBc2xUdQ2Nr1aR6lZoxL8w4cBB0YnKAFjP7GzFlAsGRKuFL4B-Co_4wdE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماموران اطلاعاتی و نظامی جمهوری اسلامی در استان گلستان با یورش به منزل خانواده جاویدنام ابوالفضل میرآییز، اقدام به تفتیش خانه، طرح اتهامات بی‌اساس و تهدید اعضای خانواده او کرده‌اند.
طبق این گزارش‌ها، ماموران ضمن بازرسی کامل منزل، بخشی از وسایل شخصی خانواده را نیز با خود برده‌اند و آنان را به برخوردهای امنیتی تهدید کرده‌اند.
ابوالفضل میرآییز، ورزشکار ۳۴ ساله گرگانی، در جریان اعتراضات دی‌ماه با شلیک مستقیم ماموران حکومتی در خیابان‌های گرگان جان خود را از دست داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76315" target="_blank">📅 17:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76314">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
وحید جان ساعت۰۳:۳۲ صداهایی میاد از تو دریا
ما چند کیلومتر از اسکله سپاه طاهرویی فاصله داریم
سلام وحید انفجار های پی در پی از یک ربع پیش تو دریای شهرستان سیریک
صدا انفجار شدید اینجا شرق سیریک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/76314" target="_blank">📅 03:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76308">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tRbtIV0XvNx_isj93ZelxUgXv08NxHJIe7QhY7cX29CUY-vAPc8jPXJT0cJUh9JWWP4HVo1dluYsQ4LTCUUzZY6g6sjY6ERfBNO0sHAEHnCmn8uROl8l_SOUPiNdpI0dupJUlDav2lKk7_voVY0umt3U9Df677DVSLUyWEUYtx_RTNaJvNE8tGF-wyd6dYxMMJ73mERs__wNE01y1yDehkK67WJwLuGyLBaZXIaTv3dRLcz2EqIBBxtNLUwAFFYmfxgGUQWRTWAAnXZVvktzFDhycP4YvNEn0NB0uDrf02Uz9f4DTttTiBNS7kGkAtSEWjR0h84pkHju92t2IAkYpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d60822ba5.mp4?token=jkNKO_8qwQjoI7pNPVmpvO1QT0jJsPuty8svzVOMZecGX11T9VEU5GWLqq1_ByvRLvi7Vbn_8HiAjBCBWzN9Bcu8ssUVmkgDICEoNkfxS8xC1tiMRlCZFVKj_FjFa-Bqgz8Cw9o54eEcIM7jxq2JIOAlucCkUeZ3bSYrdyj1MYLhLCxGsWUzhh7FjOnt84q9O1Hm3Bg7iSJ1ZISsq834jyTyhpAbje_sCW6tutlJ-Mz_QuK7lthBzddZOunEmpgynY24LB23onquFLOMqtqc1WZjITaIoqv6mWW5S2C16wh-Dt8kbRoS9nsjnVhFIGNLw_d4PKMIBWtvfGCicWNHog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d60822ba5.mp4?token=jkNKO_8qwQjoI7pNPVmpvO1QT0jJsPuty8svzVOMZecGX11T9VEU5GWLqq1_ByvRLvi7Vbn_8HiAjBCBWzN9Bcu8ssUVmkgDICEoNkfxS8xC1tiMRlCZFVKj_FjFa-Bqgz8Cw9o54eEcIM7jxq2JIOAlucCkUeZ3bSYrdyj1MYLhLCxGsWUzhh7FjOnt84q9O1Hm3Bg7iSJ1ZISsq834jyTyhpAbje_sCW6tutlJ-Mz_QuK7lthBzddZOunEmpgynY24LB23onquFLOMqtqc1WZjITaIoqv6mWW5S2C16wh-Dt8kbRoS9nsjnVhFIGNLw_d4PKMIBWtvfGCicWNHog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 518K · <a href="https://t.me/VahidOnline/76308" target="_blank">📅 23:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76307">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 475K · <a href="https://t.me/VahidOnline/76307" target="_blank">📅 22:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76306">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PzysuCcDLULiE-vEg552Q7IeKbdAa0EiiIkWvAa4QfBYiiPIERVvalWmn_h6DzLmxEarOT9Pc5nd9cYivoYXdlKgTBF_YABrNDImIu0nCSp_XhqBoMcBKTTnbRAQwUG1V_Pai9zWAhxR2040aIzj98lSv1OpZDJfM6ArzlH72EprKG-1k9oj2URCGHwXRcS8evCEGCoAoSzDhBCCWxo9nPszpXqQZeci4bKFTprmUchfw_9Zj-b7nV6ZDjABSgd8CjcvnocQvqNn26vhsVnJ3Cr4QhZSz-1hNNh_kup9HQUAoTiuRDjfQ12r3a1KcBFUpd-skxl81Y2lk1sAE_bV2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/76306" target="_blank">📅 20:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76305">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شبکه الجزیره به نقل از سخنگوی وزارت خارجه پاکستان گزارش داد که مراسم «امضای الکترونیکی» توافق میان آمریکا و جمهوری اسلامی یکشنبه ۲۴ خرداد برگزار خواهد کرد. به گفته او، پاکستان میزبان این مراسم خواهد بود و مراسم از طریق «ارتباط ویدیویی و آنلاین» برگزار می‌شود.
او جزئیات بیشتری درباره شرکت‌کنندگان یا مفاد این توافق ارائه نکرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76305" target="_blank">📅 19:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76303">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LmGB_EMdNGduLhInUhVAmJq2CB4YUMyDCgaO9qRJMSSBvrFww9-vy2su8u3mWBf0MHeEe_EifOOBqdPY7r_gPM1shbVpQW8IrD7Iu7l53rWjI9vp2iZCwlAmjS2n-hbRGOliSu7_NeOGLwertafSLL1w7pw5No-xcJ4UCSGf1qHD-cRHKa3bSptVdgp8KpC3xDf2KT4OTuMniCmQOrC4bb6JhsVfEbUsBsQHOtsPEttwpCFRGCc7wOIJ8HCtQGjsZfY4aD8j--no4F1ou42-qA0Q9buztEsyTJLKHnkWhokjp4X87ljF-3jbe01b-L-gaKHaxmzsLDUpajH2YolXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LFTaSqKWOJxN1YTcMSOLyP7isN8dNtQh3SocDR8zCiZNqb7EvEFC44oYdI48kA6BswDTpNnwrZVgcwOCHD6kHXGl6V2802jF6jH_MjLwbPevUpi3cvBil95L-YX-DF85IxNac6KGeEKkT0hVtJAfCkVhGkx-vzBK7vwHGJQgdbeTc1JYgMwSNuMThIycmV9knMfXPVGWIrRK3lCa04fJWUjSlrZ2fmtiKw6BNmwfrqCtsJ7b8tKYGRnigObwCvmVxqcSzY2lqnrmiF_MeXBkyOr27qdTxtL6ztokZVl-GOZ3OkgDyipdLB74oxwkS4AKUX0l6H44-SDOzI7CVfPw-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76303" target="_blank">📅 19:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76300">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L1yVMaI2CitF3eZ2cvYHj3GFHuDFNH1X33-PMOmNRjukPAv435HzQ8LBlDXLq9nzk5g6FP5DwEjqwr4eeTUFO6v3kPgbwDFe52gIIMkiH-tUUAmuh2pQsN3p9l7117Xqe0efgUFvcRo0Pozp1BRwFs2FtD5d41YTOo5v1BYYU-dO6Fb0-7o3VunTqizvRuV10l6P7DkGtx59_2dFr71uQNXuoMJVAhsgOoCulggXly5dDlmexTx_LkoxT7eyuFipWqPAxqxFSEDJagZ1Vn1Sho408qOT_RLmT0zzEPiW0gIg6MoquvAWOctqd_mROvPIP-P43C-aCCBLLrNi1hPyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kPufGSxjzlfh6Uel--n8HDhoQQLRDnszCMFdy6kr1lITAzCmALsTxTIfp0-mOAWJJtQ0VRgL3iJvS2SGcP_jsWIMPspvOGOHgfOMBWoefkTqsP-GzDHfH4JwQYtoc7vWZzvhsxoVdtwpgPi5UnkmATtjiHw0TlNwYTB0336Ygd3auVlIxKcFFNHedjsr0ohw49Z1Qm9f-M7mmdHR6aRxKWVJQY3W74WLqOPq5hDNEPfuYZY8Mr_7J1JxnOlwfNqv9vXc-kIi1BuaXDLf6nqtEZbWI1cqFNbsUtEs6zf-21MjrDunJ7kPNRm11JPOUW8yUBkSz0DSF8xBqV6-ouHzLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/76300" target="_blank">📅 18:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76299">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5XAv6jOjWaB1gwUvspmoq23rywnCYl7CMnPNcknh6QIzbnWxT1RuCW2qXEkhA1ljzInamS2iDKRrdLgks24PH6AsgfOTB1SxCznUAx8ruiRgLFu0x1BIjyWmQ2mRj9K6hVHV0vIC-pCUuAZvfds8AyMo1vNH3WU5nPecH38gvHAQ_hyL_lSXWPlw-3teTtzvTo4GLoLaMgmepaxGFzTvMU1XiJjU-JG8ZAoUxUpWL6hxWGvxeL-s5_xOuW203ddKASdY6TuSBbhv8G4wSB1CbOnQzpKCeV5djV4nKdshKSzV3LNnCDNFac87PtqovkWFIEB9GW97wjdwv5xnNxbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز پژوهش‌های مجلس در تازه‌ترین گزارش خود درباره وضعیت شبکه برق کشور هشدار داده است که با وجود افزایش نسبی ظرفیت تولید، ناترازی برق در تابستان ۱۴۰۵ همچنان ادامه خواهد داشت و احتمال بروز خاموشی، به‌ویژه در ساعات شب، وجود دارد.
بر اساس برآورد دفتر مطالعات انرژی، صنعت و معدن این مرکز، در سناریوی واقع‌بینانه میزان کسری برق در اوج مصرف تابستان به حدود ۱۳ هزار و ۶۰۰ مگاوات خواهد رسید. در این برآورد، توان تأمین هم‌زمان شبکه حدود ۶۸ هزار و ۴۰۰ مگاوات و میزان تقاضا بیش از ۸۱ هزار مگاوات پیش‌بینی شده است.
@
VahidHeadline
پیام دریافتی:
امروز روستاهای خشکبیجار  از ساعت ۱۶:۴۵ حدود ۱ ساعت و ۱۵ دقیقه برق قطع شد. بعد از قطع برق تماس گرفتم با ۱۲۱ که گفتن قطعی ۲ ساعته کنترل مصرف هست که امروز صبح از رشت شروع شده و عصر به شهرستانهاش رسیده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76299" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76298">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R0jEptEof1fImD0gby1uYxWt6uFQBCPYwGXbxM6PW4yr5oEqgleMKne7GPT8jT0C36PlE8MNtvm4V0k5MW4N4JItAVsDo7zImmdJkQ-IDMTiFjnY0D-KqMXH6MsI5esX8vXaBZQZxOktemlWcexghkuAH3ZC3FXHlchhjOSG9OiiGJK84FzCmY8iLIFB8P39_rV3dYcogx952H-tlHwG-9PDsoR51Bv0TvxYHOKfH3tZc5qhuDmUgA1ZnTPtY_B9zTtO7dPQ1J7UPTdCJAvdXwIhbmrrgTedY5M4qMbqX7EDtdkFIvPgHKoIjdmtDBsp_-n-OB-3Djb_mIx3fdHwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه تلویزیونی سی‌ان‌ان در گزارشی اختصاصی که روز شنبه، ۲۳ خردادماه، منتشر شد می‌گوید که حکومت ایران در هفته‌های اخیر بر تلاش خود برای سخت‌تر کردن راه‌های دسترسی به اورانیوم غنی‌شده مدفون در سایت‌های بمباران‌شده‌اش افزوده است.
این گزارش به نقل از پنج منبع «آشنا با اطلاعات و ارزیابی‌های دولت ایالات متحده» نوشته شده، اما به نام و منصب آنها اشاره نکرده است.
سی‌ان‌ان در گزارش خود نوشته است که جمهوری اسلامی در هفته‌های اخیر این تونل‌های زیرزمینی را منفجر کرده و در ورودی آنها مین کار گذاشته است تا دسترسی به آنها را هر چه بیشتر دشوار سازد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76298" target="_blank">📅 17:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76297">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtgLhb0mOeZuXmJRkf0kHqqWVBDMYrfPkLzlEIgzbseAOROWJxvyfhKVododit2BxMgWpq5u0FaDBb6DOt1HAXfUkRMuNfJJHBJOefsZv02R2zuCVJmSxEqrBS5rwCvZEiuIyvGjjw2GFJ2KS81etSvYi3Viek28eCS4rhQ8oLnT9VtYCp6ddViiKvCZxmd7zPbgaTKHclDFzRa7bkvsvipGsTp2dJ7gSzY80twcadbkgLWwruv84iEG5sZZlNXyRMHGm4RqSQkaHyCJxLDGB51zp8humBSf3tWzSikyEXhHw8TDGxjbDd1iZvehDh2HJ9l4sKtzpmmanQDUgd15jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها و مقام‌های ایرانی روز شنبه خبر دادند که خدمات چند بانک ایرانی به شکل همزمان دچار مشکل شده و این اختلال تا بعدازظهر همچنان ادامه دارد.
خبرگزاری ایسنا اعلام کرد که «بانک‌های ملی، تجارت، صادرات و پاسارگاد» از جمله بانک‌هایی بودند که همراه‌بانک و دستگاه‌های خودپرداز آنها مختل شده است.
خبرگزاری فارس در این‌باره نوشت بانک «توسعه صادرات» نیز اختلال مشابهی دارد و افزود که «برخی منابع از احتمال وقوع حمله سایبری خبر داده‌اند، اما تاکنون هیچ مقام رسمی این موضوع را تأیید یا رد نکرده است».
ساعتی بعد علیرضا قیطاسی، دبیر شورای هماهنگی بانک‌های دولتی در گفت‌وگو با صداوسیما بدون اشاره به جزئیات درباره دلایل این اتفاق گفت: «رفع اختلال از خدمات بانک‌های ملی، صادرات، تجارت و توسعه صادرات در دست انجام است.»
حملات به شبکه بانکی ایران در سال‌های اخیر سابقه دارد و بارها اطلاعات مشتریان بانک‌های مختلف ایران هدف رخنهٔ سایبری قرار گرفته و در فضای مجازی و اینترنت خرید و فروش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/76297" target="_blank">📅 17:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76296">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f0kxkWk5DBwZVxDc9dvZnl_AtVW6ZWivdNAWtv7Tez1iRrBKbn7UjgzskqRuLV0ZUqZR7zVvzDAXhmDGSv8gOi_UPHXiZC5eWbu5CPlGB2s88jy8N_YotKS6PSXqSa2hLUfJyhWqxrOmcWnj8lt4ZyduqUwWtIg9CzQLQxm6EJfwaXUxx9ELnIV7rOHfJx1TGfyT3QLyzvvmtGWdEMgMNKGl4yWr0zuWiMAa9NJNUH8jbKO0Are-Tx5tbXDaHgSKjg32iAkNZ2LnOqxaMFiQwt_-J6N92F7xvrqEmwG6j4QlWhGCo5XIdsYtaXnkPjV5Amz26fkplubQ89EFn5zTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش تازه «پروژه شفافیت فناوری» نشان می‌دهد یوتیوب میزبان ۸۴ کانال مرتبط با افراد و نهادهایی بوده که در فهرست تحریم‌های آمریکا قرار دارند؛ بخشی از آن‌ها همچنان از طریق نمایش تبلیغات در این پلتفرم درآمدزایی می‌کرده‌اند.
بر اساس این گزارش، ۵۶ کانال به اشخاص و اتباع تحریم‌شده در فهرست SDN و ۲۸ کانال دیگر به نهادهای دولتی و رسمی مرتبط بوده‌اند. در میان نمونه‌های شناسایی‌شده، نام‌هایی از نهادها و رسانه‌ها و همچنین برخی کسب‌وکارها و افراد قرار دارد.
پس از انتشار نتایج این گزارش، شرکت گوگل ۶۳ کانال را ظرف چند ساعت حذف کرده است. گوگل اعلام کرده که به قوانین تحریمی آمریکا پایبند است و اقدامات لازم برای اجرای مقررات را انجام می‌دهد.
در فهرست منتشر شده از کانال‌های شناسایی‌شده، نام‌هایی مانند نو‌بیتکس، و‌الکس، بیت‌پین، رمزینکس، گروه بهمن، ماهان ایر، فارس‌نیوز، پرس‌تی‌وی، ایرنا، بانک پاسارگاد، دانشگاه المصطفی و همچنین برخی چهره‌ها و کانال‌های سیاسی و رسانه‌ای دیده می‌شود. مانند علی‌اکبر ولایتی، امیرحسین ثابتی، بابک زنجانی و مسعود پزشکیان.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/76296" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76295">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LFGCOqMV094BAj3rByjkYmEjX_VOLB_KktIFf8R5q_hvuzUWtr6Gip_Jxwo_bXcf381VTkIPTDD3HD0T7K7X0tOsfvHGhRoiq97Yp_xhesNssDN3ebEc98MEWV6UoCcZcil755MkLWZ33mdpQgZWg4u-57pgnz0ZtpKGVoWQMTPDsqiKixiSDKm0AcaGrcghPTWDAw-sB_Sg3CpQI58s23QaKGWfPR96i7H5fp6RYVtm50HapzOv0coteJaM-gzJCiK1KrX_ETCmFfXC9bXgy5ecWY3iVVZMdspQ14MFOIaIaOCeXKDZOzjWfQc7EIDzILRGqfewPoFuIcJpYL7Zug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76295" target="_blank">📅 17:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76293">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pnjHSIJKaT7lxhnGyjtNgsp9Lo44AN2BRgBDH9B4_x8ckSYNG3WVIt53uMTY8gCy3C01RYZ0YSiXBFDRPBTqwKiUR-RxbQY3FDxcDqiW2B0cZngEwFF9hRBKvkDqmbmaARyb9JZ1BKJ8k0Bjg0f1BfLMikxbXqyGUuqWJR5lXcDc0mAEViNrdEfgfIxRi1JYkQRuCBETvYh_rBE-25D6K-pZ2aNolMzQ16PI9_9qg9pNGeTu4cN79h9DyW1L49KlSI-_xyYkJrt5OreQdOs-D-MFUIfTdBYryd9o5ZRXWfaVHIWKxvnhtJx6ls2FH1IiheB11S8_7brvNjU65oLnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SvONj0xTs6b2A6ESelhhb9XRbZ_uTgypLpTD4vDZILiECYdpFDP8T46WdFTTJx-Beco4ioW735FszfaTyuGIhOq9_z_zjVTGuX--bkGk8sJlaYBygZvUS-l6kX7wrlD8dT0nihy0VMvjV6DF72TmOX3t5z11Vrx0I92X6oCTlMJdnQEDZ945dkr0QSG6vqcDGTiXPipg6lmzxrv-D_JMObsH3QnPCyAVDY8NlDxnr9b-JQHSrmiv0y2HqlB7J7gIlf3tu4uqv1kgdIOSTe4OpSYJ1CLdKdOUsgke4Y4hM4TES8CuF7t36G12jNM02TITwCnZAByPL93NPjT1a1o7sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/76293" target="_blank">📅 17:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76292">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Th42Xqwtoaea3kbiNqjdXDnBBMu3bcqWvSPi3Mferd4JGuVRKdff88uSNgfZAOY6TdXnS-X-uFooh1mEUTo55z1TXbDTlTfAaYPAtkV2viJdkMVEGr7mjqkdWG4HO1_gaqzsc2gz87HnYWqyI1hEDWsnkksTkeRRM2jsZZgMc9-TklT18LCnplXz69_5SMN3_wT0GALGmGrJ1pXEnHD7WrDN3fKTGa3a7NYBOAw9_-NvfPqNnoC33mQg8tLCWDLi0K9MF1SoXmVw98UliOHCwdVr6EHipmDsCNeHrB2jHXncKDt0SBoLZ9fXhE5FMH4z8FlMcm8b-u6CVln0CLaZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر حفظ و نشر آثار علی خامنه‌ای با انتشار اطلاعیه شماره ۳ ستاد بزرگداشت «عروج خونین» او، جزئیات مراسم وداع، تشییع و تدفین دومین رهبر جمهوری اسلامی را اعلام کرد؛ مراسمی که قرار است حدود ۱۲۹ روز پس از کشته شدن او در ۹ اسفند ۱۴۰۴ برگزار شود.
بر اساس این اطلاعیه، مراسم وداع با پیکر علی خامنه‌ای و اعضای خانواده‌اش روزهای ۱۳ و ۱۴ تیرماه در مصلای تهران برگزار خواهد شد. تشییع پیکر او روز ۱۵ تیر در تهران، ۱۶ تیر در قم و در نهایت ۱۸ تیرماه، همزمان با شب شهادت چهارمین پیشوای شیعیان، در مشهد برگزار می‌شود و پیکر او در حرم هشتمین پیشوای شیعیان به خاک سپرده خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76292" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76290">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5L_Kxd97QDH0iYlQZ_StYBHnHBRPpCRCL13ebhK0zOIx5i7CzkIFUkoAmAuQ7u2EZXFAa-a7DhQZancuFKKsIUsz3eYDrl-HZUuI2GdbhDsjDMhJ_fIhVTzO3CrUDJ9pRDYjtd47s8nb0OiabDi8hjkDOcrzccbvQao4DnJ9Eu7mMNWU31t4cs0PlA61zuZrY8C3MxxEIZ2o8YBwZ4P7O72ORZDvAyRdEC0tGLBowtzJOh-WGjAW0tLMcmnSOGJbjeQ-MCpjJ22h0eD-GPyW2kD9D4SuS0TAiQpj9WYOhjlImkiWczF3RIIlpB1qjWUwy3mNhcx2F_Hk1BqYQd4sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سید آرمان موسوی» ۲۹ ساله، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ در محله مسکن شهر کرمانشاه هدف شلیک مستقیم قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله جنگی به ناحیه قلب او اصابت کرده بود و در اثر شدت جراحات جان باخت. پیکر سید آرمان موسوی روز شنبه ۲۰ دی‌ماه در کرمانشاه به خاک سپرده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76290" target="_blank">📅 17:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76289">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzJFi6wt0Po5IOY8WK3v7204nqzGbMnmkYDFKRI0FrJfDfaXwQO8NBIVjZph7WhsuySfDNL3wZepicqX9KJuzdJHNHib-Qv5Jda3iGIGoEjMfu1DOujnMCbNFbniDI2_LXjw4OLwuuO-5kLHV1t35bTCh3RHfsvo8kZfknyX_KJxHdGAjGaWLLRwIYcpB63EhyEhLjTqzilRBRBPslSzUIBvjkksiMDNkPeYlcU-PBQ0uDjzBAG7qHkh4xXaeCYNGeQhbVf2NP0UyEazXocB9vl9DYqnfw5jDYvR-wNA_7sRc19f2dMp2JA9Xl1lLFWlJsisoXNsxqRfcmSjnfQmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، در گفتگوی با «فاکس‌نیوز» اعلام کرد که با توجه به روند پیشرفت مذاکرات، انتظار می‌رود توافق صلح با ایران «احتمالا تا پایان همین هفته یا روز دوشنبه نهایی شود».
بسنت با اشاره به اینکه تصمیمات دونالد ترامپ برای جلوگیری از دستیابی تهران به سلاح هسته‌ای، هزینه‌ها و فشارهای کوتاه‌مدتی را به بازار سوخت و اقتصاد خانواده‌های آمریکایی وارد کرد، افزود: «ما درک می‌کنیم که در ماه‌های اخیر شرایط سختی سپری شد و افزایش بهای انرژی بخش زیادی از رشد دستمزدها را بلعید، اما ما در حال عبور از این وضعیت بحرانی هستیم.»
وزیر خزانه‌داری آمریکا با تاکید بر اینکه زیرساخت‌های اقتصادی کشور در حال حاضر بسیار قدرتمند عمل می‌کنند و بازار انرژی به خوبی تامین شده است، خاطرنشان کرد که با حل‌وفصل این مناقشه و مهار تورم، بهای جهانی نفت حدود ۲۵ تا ۳۰ درصد و قیمت بنزین در بازار داخلی بیش از ۱۰ درصد از اوج خود کاهش یافته و روند نزولی قیمت‌ها و کاهش هزینه‌های زندگی مردم با قدرت ادامه خواهد یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76289" target="_blank">📅 06:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76288">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76288" target="_blank">📅 06:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76287">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76287" target="_blank">📅 01:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76285">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E0IMxhfecgj60gkqj6Zk2tJZysrWZL9tNFHjphLUXfQTYCVHoPRGsj8HciHlOJU3iFXPYrO4t_I0VYwzIhOKGP3yEWHuDzDg6ll7Q_y0nVil2UjzenaRnOX01Mq0zEqCyTdy4TDyQ-48Sg4vjdk3Zh8NMm2D7ZH_V44xu1K3AImI5gXzic6YgovbjhVUDHWXh6sNVVqajlmRSiB6tbjyxKUKpEsSB68oJ_kgKWYyfF4bkqnVlryNeUpvJBWAdjtFLI7D_QBlS5WoxbbCaeKsKVkZCLe-Fa3aS1pQR8gcBfOMWc-bQ9Fhk9QYj_uR9FI5n_tEjNIlEYMC5-RzgJ9f1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ln2bs0iMwTSumFpCAxfp7Bcayp5j3YqcUV1WNO7aTw4iJImMZ92OYLUoILAPN6Oe-SHww3WybLmko2vtpzTaqDfV2ZOW3vUkY-fEQDrxvw66RkvhSkI9B6hXJ-1aEYwaqabBhKFP8bVQUlNrAW5BPgStndKOqoFfziDv5uGCZi8gYL_cBDjY7zB5E-iI1rk9kXGZCfJSjruXz2-duttAh19O_Yw8IP_McoNaXRw44U5sT9bA3WS1qGb200YpMbLLvs-ST1jlsaoASf9o4zjgTgYhzKZ8qAlro4WYJpB4OTDQzEMW0Uh7IKqGhT1ubMk55o1VnmB-J1zKla5WP3P9aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مالک شریعتی نیاسر، دیگر عضو مجلس شورای اسلامی نوشته:
خب وقتی در باز بشه و ببینن که می‌فهمن مویوم...
malekshariati
این طور برداشت شده که داره میگه قالیباف پشت همه تصمیماتی است که به اسم مجتبی اعلام میشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76285" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76284">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V4Hv91eaBlnJY6VrUOgyPP3RhdS66bN2jcWOO691wuf2RX8YGeuTMWTOAIv5LgfoHVMuTGhCGq8JSaKvzhsvtNV8yrukEgFZtRPZau5VTZq0lX4sUpFRRgj6nb8RrxpGc8fiBr63ys6u72Y_XqPkWAMvy5gzlXNn8sSDMQZlTFNd9kCnSNOM4DvkpReTh5gITgPOCIJ2bDFry7YevRwBPCPz0pmfrJ618K3MTBKqX1x0RX0E1inO2rESHnsvH9USRIbp6dck4sPdnOOn60gO_BOVT7372cZWPjG-BhhyfFuC6Mhu638gWT0kM0dyN-QbCgk7AUyzF4PbA9VVlJg1rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76284" target="_blank">📅 00:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76283">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bsKPYuyMqaWrSev4xxv3oUa3kfNqN1heNc60topcl7Gbw_iPwPwHvY7XbIc9r2B1loIout_0ErboGV6_y6nz5marXWSX87ZaiM6As55PGNhj51-czMs-73TggUOpNniDppT_viSjWEfYRjxiXJc-6Ad82pQ_qjhqegPxcBG_oZNj5wqMCNQu7OuamZMUIDWM4tcLfjB0zo_2J4xk1tgG9YnBAF8DQYmRU29ubG2s55EEBZ0aOF7fZOsDfhlNVQazYxgX6ZTKn-Y6lJj0X-447Q8HEOqV8ubN4CLq9149eSF-oIQ0NMPIlIRoNUhIx0Gv1e73bypUXZUGdAFqxm4zTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76283" target="_blank">📅 23:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76282">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QDCzZWMAWvrfcpEoNWdPHjRVIK3mWETvAwV49mAh0F190Bp9EP9972AGdcfKU0k9Lf9dxBjrzKeBe3VaoZPVmo8eC4kibJSaqcRLWXqSPu0nUjE3YduNV_kgdS0oXht1_MH3S4XWO3JbgyrKelOnsRwhUjdoZdgbkgidxSe7ZrWS7dLilDawzjTq2WmQGOi_X6WuckvMQT2mb-bwo7-fc5WGuiKb7Et1oqSwhIr1Vf9c5-hmQwU6zNUZNQlnOpz0Roq_Nk-PlNPHJ9vlba2EZXfq_s-Fw-0e5ytL7D2SsKrIOsG7A0VlRAQG6MTgKVzf9tReCbBOEADUMN9LO9OXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف، ترجمه ماشین:
تعهداتی که داده می‌شوند باید عملی شوند؛ نه اما و اگری، نه عذر و بهانه‌ای. برای توافق نهاییِ پیشِ رو، راه دیگری وجود ندارد.
هرچه بکاری، همان را درو می‌کنی.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76282" target="_blank">📅 22:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76281">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PwXLkO-1GyFWwIQdP3OQZSZpd7PnlaRHABJ_pWZXCwrD7RccrCP-j2kWwUvMcUvdlBzc_yK_D8_D3uImg2nt81S9JZ-TkYGkqd3GMK8jzWue1ASAniUdh2rwi7UVZxjEPrOZm7ZeRj8uUZ2XaLFyQXSmD_zgkqdG2iE9tXs2nOw7aNrO51Eehs4Z3vcrgiyZhV1MIPtS3Ix7kWNHlvYvyMTF42ZQxwnjQJDbxdj6LXEB-Q5TCTf_SB0bHMgSslVzCbZMdZJ8VOxcGskdm1_NXxYwXw3Int8hQ7ljXVa5RXUnSq5ZoObycsks6qHfjYYwfWzDMHzh_A46S_-WRCkO2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/76281" target="_blank">📅 22:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76280">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/umZmgiF6geGnkx7mYaSThVfiypPljRgfp7i_OtpMEZVYj7xrd9YzaBcV84QATG6Eb-cP7k9dsGdp52eDDqkGlQCVGSW1bihhCoJssMVP-d-NPmtrktXGhuaogvFN2BWfgXv7aJvTwC5j2PCZMtqw1yG6_2zI3wPVaxdu-XZUe4UGl0PclLvf4vp_8LHXFZxS_Z6g7MUJf3OR4r59GO8_zDFxUXOn0vc1ui9XKv1GgRgMvqvCpn6p6Phg8m3wSWnp4e1IR1GhxG1hAiT9huBDojW0YbSrsUNjr2c6sp65APOam4nxDM8E9Phm_F76FiK9BFPJyo5We9kCyZce5loN6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس در انتقاد از
توییت عراقچی
نوشته:
عراقچی نه‌تنها مستقیماً ادعای ترامپ درباره «جعلی بودن» مفاد منتشرشده را رد نکرد، بلکه با درخواست از رسانه‌ها برای پرهیز از گمانه‌زنی، عملاً فضایی ایجاد کرد که می‌توان آن را تأیید غیرمستقیم نادرست بودن برخی اخبار تلقی کرد.
آیا موضع‌گیری او نوعی عقب‌نشینی یا هماهنگی با روایت ترامپ است؟ در شرایطی که ترامپ مدعی عذرخواهی خصوصی ایران شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76280" target="_blank">📅 21:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76279">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GqqDJfvIMvrUV9P_5I1kQk93qR8IJHFjTM0EMOcG2m1FKusuZsfHA3BuFzKIK8xDCd6YDV-ptof0XBwyVdHw9bXXxIOoNzRDWoWyIXK3jfC7kIh9ujWx1oedvUmk-eLKUo-2V504U6Yy1Xy9KdOchm4MzoypWmM6UkjO3BIXMlnud2xrLHnQ9PG3PMN3SmStM7fkAXDKgocw3BiSp7FjOzulLlklDtSD0_xavfUMp0Tevlck8a1lYMFo89uEQYn82wfACq8UfvuB_uuU5PwG8PMevyiXFmnjYNvOjpysfJo6TGBWWX5faav7IOdAmY0iu05bvPRTejip0zK5FiQkuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76279" target="_blank">📅 21:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76277">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iYCobVv_Q1U9U5n2C4CR6cfZ2QMswW1zoDxJ5S2a6jq5G7aLYn735tdbxsB-8wsfyEMI6ab9WP9WJzPnwNCCSbI0g3Ee1sYhg9ol0xshjauG5Kr7vNBRjI2AfAQIW_T2w4L92vhyQ0H8ORIFDMYCnYf2_FVVC5xrQdwx5oBIbeuo44shFc5y8DO5qhi7LkvAr59X1gwQWULnXECV3SywEDj0mdU_a4nh3B_9UQ_-ldgF98QnDwNmF0Tvkq5XEK4IQA8wtStFaWGmbpliQXp29-zAv8vvD9vkzfUwh_FV5YvgRdhWYIaBaEjZMNYYrMvNin7x8H62bC3Zldbi7h17NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O5j0jlsqeVa9vnmhfSZzSkXXuzQXslgbcFBl2dLPg-1E_6snP5HcrfRmLoSBPzUDSbf131gnXSmtGS_kucB65Dl7qo1HRIlQpdilkRidmJIoGkRq0-5l9gP8AuVMYaJv7UfsUt8zEBvNnlien2UWFBkzpUS7GZSWNiLOkJtLjhaebbtURyd1ppUdg9_kkfVbr8JUXLqInZS__kFE85Vng_rGc41fKc6_DWll2CXNF3apk4q8cRIKYz-W3108sBdqsjUJujeMtp2MpvJJIfCYEpdVdWnjQLqzp9T619OKUx5bWekXKpfLVSbEHhQ78HiHCaVijnsZOBVM14aw0VoqWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یسرائیل کاتز، وزیر امور خارجه اسرائیل، روز جمعه ۲۲ خرداد، با انتشار پیامی در شبکه اجتماعی ایکس اعلام کرد که هرچند رئیس‌جمهوری آمریکا بر اساس منافع واشنگتن و هدف مشترک با تل‌آویو، یعنی جلوگیری از دستیابی ایران به سلاح هسته‌ای، به سمت یک توافق حرکت می‌کند، اما اسرائیل انتظارات فراتری دارد. کاتز تاکید کرد: «از رئیس‌جمهوری آمریکا انتظار داریم این اصل و شروط دیگر در حوزه موشکی و گروه‌های نیابتی را حفظ کند».
او با اشاره به اینکه ضربات سنگین مشترک، توانمندی‌های ایران را سال‌ها به عقب رانده است، افزود: «اسرائیل باید تضمین کند که در آینده نیز توانایی اقدام مستقل برای جلوگیری از هسته‌ای شدن ایران را دارد؛ به همین منظور، من و بنیامین نتانیاهو به ارتش دستور آمادگی لازم را داده‌ایم.»
وزیر خارجه اسرائیل همچنین به عنوان درس اصلی از وقایع ۷ اکتبر تصریح کرد که این کشور به هیچ وجه از مناطق امنیتی در لبنان، سوریه و غزه عقب‌نشینی نخواهد کرد و ارتش به دفاع از مرزها در برابر تهدیدات جهادی از بلندی‌های حرمون تا عمق غزه ادامه می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76277" target="_blank">📅 21:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76275">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hYIKIiIN1qd27fWGvpHYq4G-yLZbPAj42woBolZkZwGmgwtTb9a87UN2qtxBKSxgkh7MncsscH7PI3EuutJtF-q0bJjVlYd9ctbqQLhqevVKkwUm9CRTM5Zh_SoIXqH3jrQPj-2_Dr-VqKkqTXG8zjoYZFQhGGxR1iFXYd0kna0ukq0ErSpC_q-KCrOaqn3LcPl33Gm7KLMd5AP3EBfBxuTGDlxSRW16l-pkKo35t3EtoXnWhx7oaUNd75bd-7slam_A75rhu9YQoe928IDRjUEoQag0xo-vkHs9l6UYL0ZNiLqWdzEPrmrz2w2ADissmQEeLBqxrIR5VvYNt5IjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rdw66_H2Cf8TFvSxcRKQIEAgdlF2gC99uSnesrb9ZbxcN9YNaBZRJ0POYwRMHeBUkcBephA84Cikw2TrdJpTMNAgdZtPaKWZ7JH4SMz6EmL7gF_hoBe7UHod-ZkUQQaO7xo6FVn4e_B9xf2HrnH9OD2n6b3MO6vyHuNFop0rTKPKf6Msow7nLdJBUFUT4mx8aSyhpUfXhF_mIXfAt1GNqisT36j8HNQXpgE8kC8PMmTd3dctTTkSzJOS_VAwQJlAob76v0rrb-TD3iMM3gomPol27cVkghmSG4CMM6bCRl2LknK7mImYS2rGxsj4fEET_P2uOYMiOrTGJzBqh1Er8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76275" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76274">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NNZDOYZRPdqQS7qhgmGJmv2Ii4n6eLPgwa0dZXcRlK-8ubLZAplcSd-01RwmaBHJmO8FUp7KRLwOgFrLviUTbMLwoFhhQ0w2KhMJc0vwOcVw57Nnfrp6A3trMTmIpObjbbLKwiKEFgniNu5UlQ2sX1ZkkGhBlefwxAnoCjGJVG7erxaPUEEnm8XO0VL-GlLEpabpbT-QAJs6pnxDpLYt47s0CHqx0W3hktPUH-mYV4jE1zUod2A49SO6QzJSzoc2QVjZROK6jJX0ySpWcUDsqvG-3u2x8ikQTdE6ykwuYyioKPhplH4-OBrMW602F0V4nxy5wTc7e_QwFZsQA2myNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.
سی‌ان‌ان به نقل از مقام ارشد دولت ترامپ افزود که جمهوری اسلامی با «برچیدن برنامه هسته‌ای، نابودی و خروج مواد هسته‌ای، آزاد نشدن دارایی‌ها تا زمان اجرای تعهدات، باز ماندن تنگه هرمز و توقف حمایت مالی از گروه‌های تروریستی» موافقت کرده است.
مقام ارشد دولت ترامپ گفت مقام‌های جمهوری اسلامی پیش‌تر گفته بودند بدون آزادسازی دارایی‌ها توافقی را امضا نخواهند کرد و بارها از گفت‌وگو درباره حمایت مالی از گروه‌های تروریستی خودداری کرده بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76274" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76273">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G7_BalrWv57b0Z6lRw2ZgT2aF1WW9gaRks0G6ayt6oCtXMwXBURh3psY_mx-cZVvgrp5pXyb50C0UTfmIj_QCV3xsFGZpSrpcAkGkkng8Z0jliY3sWbLWgxBES2A9BkrtDDWbFtTquNGGxyk8TGBT9ln4b-L82lYrRviWgbXocvgzxKJtnpY9CnV5pwGAqJpzyeB67w8IjVkrdmt0Gbkw7L9Az8j9Nci97OmW-HSN7LPX5FS7OD_Nownh8eH6MTYYyR2Jr8VzEJcu84aihwfkud4HO2SRNVMWEfFeMCAHX8TBS-c0TnydMA0sDs5g36iCQltw56DrweYmfqIRUh03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس گزارش داد دونالد ترامپ،
پیام عباس عراقچی در شبکه ایکس
را «بسیار مثبت» ارزیابی کرد و گفت معتقد است توافق با جمهوری اسلامی می‌تواند در آخر هفته یا روز دوشنبه امضا شود.
اکسیوس همچنین به نقل از ترامپ نوشت که جمهوری اسلامی به صورت خصوصی بابت انتشار «اطلاعات نادرست» عذرخواهی کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76273" target="_blank">📅 20:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76272">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GTr0svh-Q0-z3ygyEc_i9c-27g1ws7nr1LPbWDGL7kpuB82hHHqeD1kcCfl9E0r3h_k8ueJbpulbWpFAeo11r3bOcOKS1dNzyHtIjGkVOlb9BlDhjw-qSN2WepFBY0vgLwrSjo0fjHDdqCCifU_egcF1X8TblSs4GAZKQp5cbQ_3S_i3MwQFnxN4_eOyLdE7mzDa9_GM9VEvNIZiXpked3OATEHaLInlD_P6fQO4iyxCKNIgJaP9uz5PHmdgILPLpSCxrefiG3qdar_wqCa2lezUmwkipCx1xRwnEDRmsdW1wlcQpxIbkMx9zdhrP0EQ_12LlyF-F3p4iU87pOEM5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیرحسین ثابتی، عضو مجلس شورای اسلامی، نوشته:
طبق اطلاعات به دست آمده متن توافق احتمالی بدتر از برجام است/ چنین توافقی نه گشایش اقتصادی می‌آورد و نه جلوی جنگ را میگیرد
دوشنبه شب در تجمع مردم در میدان مجتهدی طرشت حاضر شدم و توضیح دادم که دشمن به دنبال نابودی ایران است، چه از طریق جنگ و چه از طریق مذاکره و کسانی که هنوز هدف دشمن را نفهمیده و فکر میکنند با توافق با امریکا میشود دشمن را سرجایش نشاند، بدیهیات اتفاقات اخیر را هم نفهمیده‌اند.
سپس گفتم طبق اطلاعاتی که تا این لحظه از متن توافق احتمالی به دست آورده‌ایم توافقی ضعیف‌تر از برجام در راه است که خطوط قرمز رهبری در آن رعایت نشده و نه باعث گشایش اقتصادی میشود و نه امنیت کشور را تامین میکند.
در پایان نیز تبیین کردم که اگر بخواهیم امنیت مان را حفظ کنیم باید بیشتر از همیشه آماده جنگ باشیم وگرنه با ژست مذاکره و گفتگو و تن دادن به توافق به هر قیمت امنیت کشور نیز در دراز مدت مخدوش خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76272" target="_blank">📅 20:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76271">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/awQmUDq1DGh_pKZDMzkQ2m7koWATdl6WF69rWbdTK0FqJRymBhO4fro2eG3s_qWhFI0NZdKso5GbGfZwQTDcy_b49AyEZ_Z26tS27hJn8MxHWpFd2x-P5jl9592H5tBanaq-z00NfqwrmTtS9Z2VX6HliAVI69TisQ8oi4m9-JYi9QjanDYIQT-dPgrjJJXmCNvsvGAIncPAHSXcX1mcSn2_xScS8ySyEW4tpbnWq-VYXnhuK6NYT4gKTkqYorRHeghCBfUm2UQGrsvysA_chP9fcNXY5787dCNPIBM6plEM8zu6ZHmkBT4RyXL20afiRK80a2mCx362dXKY70QqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف، نخست‌وزیر پاکستان در پستی در ایکس نوشته است «در میانه تلاش‌های فشرده میانجی‌گرانه پاکستان، ما کاملاً از کارزار بی‌وقفه انتشار اطلاعات نادرست که از سوی طرف‌هایی که با هدف خراب کردن توافق صلح انجام می‌شود، آگاهیم. با کنار گذاشتن این حاشیه‌ها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق حاصل شده است و پاکستان اکنون به‌طور نزدیک با هر دو طرف برای نهایی‌سازی مراحل بعدی همکاری می‌کند.»
او نوشته است:«صلح هرگز تا این حد نزدیک نبوده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76271" target="_blank">📅 20:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76270">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xdviv_EJhAtSmC9TU5ppZRllv0nsRO3ndfgVegIf4QfHirDFINLS1kkFh5Ldhfr0oOBfa_nyDtTKPLLB7SH1iLoGG_zs5RO5C0U091mP1-J7JFbaH9awLW9RhvjoUmzAqvS0WMPbfj3QxL-qVw-Sjy8E8baz8kHKKZHMz3tBSuwjn-Z20ndV6vy4zCA13KPSAuYnRbkuB7QtUqvmJrhSX5atnxPbGgTnaCfL3Zqrejjh9Z_DWRkGNeQ6O4E0Iqg8dOH04BDqNAbvYqjlkGjrzGQoFvzwnzQAD0BMYY0RQRx9qX6lOAd7ce7jlRKZLeII6QEK4mPIa1pv---UXeROJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اسکرین‌شاتی از
این توییت عراقچی
رو پست کرد:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76270" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76269">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pgt2mHVLWo2YbiUkfuHa5JJb6VbBFpSSFIpXi5BFcUKT4OHm6NuqzFBX9f3XSo3n3aMrA1R4MTU96Kgx6dXERA-cWecP8Wd7ZBGCOnu23TntMcSii6t1FDxRcaClRL166JtnQ4WWwix-7wMTKuLHbtpFNJZ6pXlgUPUB6rGet2VY509E_uf7hivyVhCaHzZACE6stPdXsLxSLs83xwQ74fG6MEm17AGTrl9n5OF7WLe6y5QCLUfImLIP4jASKNjFO2PvqT6eWlyfN8CO_kqeiBGsB9KLmtztmcitjEVPFTt0ghvd6ELM6CO3X4_niJJB6dANVbUB8-VBGAotH5JSBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76269" target="_blank">📅 19:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76268">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NIH0wZpU-hSTOfEFlNtYKXi9kSFOdk52QzItUVZvk6RELxOacU46vEF2fZa9WYZSIcrz0rikeKl2AkDNogG07TY3lRMXZCJbnAB_JEz9DjMcKQ_e3rtDeCPe3_qUK_syHgUAK5312sFDwfyPQT08qvpZg3cwCaSFp7SCfFPgXPzT_ste5EI2lEOoUNUMPMP5zHMaf-pKv1MZT1iW9-No8X_kn5Hd2EHPLqnE9ALAT6IWY7Wx8GNWKzmIiqn9QKP8WyyHV_wu3aifV209Pild0hxqMXj5uo5RagYYwstnwJrzwvb8NMiQ5aP5KF6FTIJGL4Nw_TgEnHGRnWprcEPuoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز جمعه گفت که در ازای امضای توافق با ایالات متحده یا حضور در یک نشست، هیچ‌گونه منابع مالی در اختیار ایران قرار نخواهد گرفت و تهران «هیچ پولی دریافت نمی‌کند».
او در شبکه ایکس نوشت توافق آمریکا و ایران «به گونه‌ای طراحی شده است که اطمینان حاصل شود نگرانی‌های ایالات متحده و متحدانش در اولویت قرار دارند و در صورتی که جمهوری اسلامی ایران به تعهدات خود عمل کند، منافع اقتصادی به ایران و همچنین به کل منطقه خواهد رسید».
معاون دونالد ترامپ همچنین وعده داد: «این توافق این ظرفیت را دارد که منطقه را دگرگون کند و به صلحی پایدار منجر شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76268" target="_blank">📅 18:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76267">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ddO43AnQ29UzTiTmDYcXjZkR12L7n6tvCQDgiqgPy_3TfEajGeHPrXjPJZii2E9KHOtRvjN-2nUKZSAFfwE4nDfx1pBoSxr8WJnqa4BjzSKrhHg1RY0h8FyWASGEZeQ7RpTQtaQoyPPEdlYK_XCGAQGiXOOwx2VaBukLxjbHg4OOk56CdaDohH_1l3f7YaCwKMmotluJ_LrgilPqErlV4N0GLrR40KvMX7wvIcKw66KC_rgg_RM_JcYfc-Y79JvhrpsW7ZXi8LPmWRItzAT9wlVmAbgMzMtmVvje3tH9Py5B0mgl73JlB9oP_VPaSMdeXugOm6ZlckiVGuB5z2pSqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت عراقچی، ترجمه ماشین:
یادداشت تفاهم اسلام‌آباد هیچ‌گاه تا این اندازه نزدیک به نهایی‌شدن نبوده است. تا زمان نهایی‌شدن آن، رسانه‌ها باید از ورود به گمانه‌زنی درباره محتوای آن خودداری کنند.
در راستای رویکرد مسئولانه و شفاف ما، همه جزئیات در زمان مقتضی با افکار عمومی در میان گذاشته خواهد شد.
araghchi
ساعتی پیش، دونالد ترامپ،‌ رئیس‌جمهور آمریکا، از آنچه درز دادن مواردی از توافق به رسانه‌ها توسط ایران خواند انتقاد کرد و اعلام کرد موضع جمهوری اسلامی درباره توافق «هیچ نسبتی با واقعیت ندارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76267" target="_blank">📅 18:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76266">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/012364ed90.mp4?token=lVIHwrxY8ptWvd7nwnqa1Slq91C6rkSnrZXxy1G47oMSuclQ6_M6RJnQx6Jz3GBBthQq5NnbbU9bmC6dU68sdD0VdqMrqwnveSBaElMa3lwAwzW4bAu480KLZIy8evozO_OBu2gjaqOa80ibxKqs3HGQUX45YB6cvRP-X-jtaX1769jAVkFf110vOjJX_FCpRA-qZjFQamYc2ODouCilcnI_lzTysgn-HzHa6DhjwayBgf-HkKUMP34Ec5EZioIdavC5Rjnhqrti1y2r6YXxYlT9Xv9GhuREdXGe10aDRmLtgGU_tueHE2LMDQjk0Tu7wGlh1XzQcwSvA0tmCqzHDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/012364ed90.mp4?token=lVIHwrxY8ptWvd7nwnqa1Slq91C6rkSnrZXxy1G47oMSuclQ6_M6RJnQx6Jz3GBBthQq5NnbbU9bmC6dU68sdD0VdqMrqwnveSBaElMa3lwAwzW4bAu480KLZIy8evozO_OBu2gjaqOa80ibxKqs3HGQUX45YB6cvRP-X-jtaX1769jAVkFf110vOjJX_FCpRA-qZjFQamYc2ODouCilcnI_lzTysgn-HzHa6DhjwayBgf-HkKUMP34Ec5EZioIdavC5Rjnhqrti1y2r6YXxYlT9Xv9GhuREdXGe10aDRmLtgGU_tueHE2LMDQjk0Tu7wGlh1XzQcwSvA0tmCqzHDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: خطرناک‌تر از ناو، سلاحی است که می‌تواند این ناو را به قعر دریا فرو ببرد  رهبر جمهوری اسلامی تعیین نتیجه از قبل برای مذاکرات بین ایران و آمریکا را «کار غلط و ابلهانه» خواند و گفت اگر هدف گفت‌وگوها برچیدن برنامهٔ هسته‌ای باشد، چنین موضوعی اساساً جای…</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76266" target="_blank">📅 18:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76264">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a0QyS3-9o_bpuH5dL6CoSiLamI2zItuDtb-O4ziGWZs2zXu4Y4gs986qmmjtq6eojnwKUwtlJ0iG3LbJ_qMEROmIj5BhUMRMOpK5LlW8WB5283TwdYIsY7TpHgl64QTCiv76547GmlNN-kZSCun3F8TmqR2nN0gltlESQZdlyaeNPOpKjK0gXxsPz7bqPRdzCvpKV-nYnS2fYyV_PZxftNZMZeBufaKJDd49V1A50tj0YNvbynqyzKXRx-Piy7NB1ZaBLnrCrbaRyKV1llquGpsCBiQLE0GyIS5puo4gdEI0_Zb13DetdF5D4czMAhc2kNbi70caSxEFG3U1y-xjXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
شرایطی که ایران به رسانه‌های اخبار جعلی درز داده، هیچ ربطی به شرایطی ندارد که به‌صورت مکتوب بر سر آن توافق شده بود. آنچه آن‌ها گفتند، از جمله بیانیه ضعیف و رقت‌انگیزشان درباره داشتن یک توافق، هیچ نسبتی با حقیقت ندارد. طرف‌های بسیار بی‌شرافتی برای معامله هستند. با آن‌ها چیزی به نام معامله با حسن‌نیت وجود ندارد. شگفت‌انگیز است!
همچنین حمله پهپادی کاملاً دفع‌شده آن‌ها در شب گذشته علیه کشتی‌های هندی که در حال خروج از تنگه هرمز بودند، کاملاً غیرقابل قبول است. بهتر است هرچه زودتر خودشان را جمع‌وجور کنند، آن هم سریع!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76264" target="_blank">📅 17:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76263">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a1U7z-mSZLsWqdkmsJ8uqOCIvGrO6smiYsobHEMzno2mFuPkwThrROvr2LW0WN51_ZXy2L_smDIE9NTI-JVitAXoRcuE-oJC2RtKzsd4AKNA_-A1s7_LAQyOs6KTH8iUTEzPZ985uAZNyT06PTW3Ksv7rv1lIwCnzue1bcz66feEyDlMHD6IEkWJB2t0qgCeLLhKrACdeDYNr1U2EGibE2qCSVoliipw7GUcJDZVVyeMmIJjRZD6MEZPtddkhMfCgjm9-rH7dr_6lHRCOB4FiJIiy2e_TRBxBPqdOky01cfSaxDH-OSWzqy5uAd4oYjWta5wl3oB9xsJyDLbCOv22A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حبیب‌الله سیاری»، معاون هماهنگ‌کننده ارتش، در گفتگویی با تلویزیون حکومتی جمهوری اسلامی تایید کرده است که از سرنوشت خلبانانی که در جنگ اخیر به قطر حمله کردند اطلاعی در دست نیست.
در این گفتگو که شامگاه پنجشنبه ۲۱خرداد۱۴۰۵ از تلویزیون جمهوری اسلامی پخش شد، سیاری درباره خلبانان یک یا چند فروند جنگنده سوخو ۲۴ متعلق به ارتش ایران سخن می‌گوید که به پایگاه العدید در قطر حمله کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76263" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76262">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g182ubfr9sJRcc2N7f9FJKOrUMGuyJkDdX43JaLygynSSKNwVu8WnshdQWyloiD8q8VZAeYQkrxEByHjwZkYeRwLUjEAvWqz2oZ6PDPWLiB3Ha68Kv2bi5LoVGKVDMeKOjc0mf6QdSVfEBnkd6353jFwNjlowN91Yr0YlduRi3dDsLXsO5ju97dDwCq8fryxj8IRnOgdTZM5rDFdEDRJ5PkH-D8EXossBddWHL4uOK6dOYjxfeMsCVdFeB9FnQLCO0f6G4qBeL8erxzajZ3noytzUV1HP6ou-rZjKrimo1p-yltx2MtnN4wtn-DQoB2d3-qhgOzjZs6xyhfC5ZVjJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود نبویان، نماینده مجلس جمهوری اسلامی، با انتقاد از پیش‌نویس توافق احتمالی میان آمریکا و جمهوری اسلامی، آن را مشابه برجام و «خسارت محض» توصیف کرد. او گفت: «حرف از پیروزی با این متن مبهم و خسارت‌بار کاملا غلط است.»
نبویان با انتقاد از مفاد مطرح‌شده در پیش‌نویس توافق، گفت در این توافق جمهوری اسلامی حق تولید سلاح هسته‌ای را نخواهد داشت. او همچنین افزود سرنوشت مواد غنی‌شده به رضایت آمریکا وابسته شده و همه موضوعات مرتبط با برنامه هسته‌ای باید مورد مذاکره قرار گیرد.
این نماینده مجلس تاکید کرد: «این توافق مانند برجام خسارت محض است و بخاطر تغییر محاسبات مسئولان است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76262" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76261">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pn-kbJyVD9nY0vSAsyqcnDwJtJyHzZ_9PRTSF1eod0I1xij8RLljTNsa7BUlpOHQVjW5Cyf-w7oWdT84cava15APVnll8M4v23wraCRsfuYiPubBx9QhygKXkUxxGNkSKRvcPx42oJ9I5jsrWjr13k-d1vyt-H708Y31TeQnumA5VCrreNtjZ1gWVtTK7Zu1g708UAoeYmgmOSD7fknuuaMn7YRXVwbHAwDjssJxjb29CJU1e6vaKrK7AmeSzuFVGe6kY3gUZEs0T3UWesc_kOJIxi2bwfgCrKJsC4h_tajPXgIurBTCc_rerbJGaADPrW2YFRDypgAHlE3rsJRfaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/76261" target="_blank">📅 17:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76260">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4H-8ahpN61koBi9Pkve96pYx-hJ3caG7bUJCGMU1eq2YBEHtuCAmvGh3abNAsPeTns83U97UJ3qHBGU_bJ-Gt7UHLTs9MPlN-TohPcguAnspjeGkJyIS2C4y5sakkS8UvhWUj817Nmf8JXKXkgtNMSBWP6BrQtRA61HHwz3DHH0t3yWlxbb54jnpah3glB8g2Gj5AUX-SBeVRCzZc51fMbuG_VRC_37TONrhglpo2XZLAPaj4HTK8jVTiG0ICWPMjnWKqFAuf4KeQYyq4vHzaNfHowItrqrA9icF_DBgHBz3D6eiryogD_w_Mab0TSYmPXJwTihyB_pb1kTPzNtNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ به نقل از مقامات ارشد آمریکایی و ایرانی نوشته احتمال دارد توافق میان دو کشور از روز یکشنبه و در شهر ژنو سوئیس نهایی شود.
این خبرگزاری بدون اشاره به نام این مقام‌ها افزوده که طرفین «در آستانه» دستیابی به توافقی برای بازگشایی تنگه هرمز قرار دارند.
بر اساس این گزارش، طرف‌های ایرانی و آمریکایی قرار است در حاشیه اجلاس گروه هفت که از دوشنبه در فرانسه برگزار می‌شود، «دیدار کنند».
اجلاس امسال گروه هفت از ۲۵ تا ۲۷ خرداد در دامنه‌های آلپ فرانسه برگزار می‌شود. به گفته افرادی که در جریان برنامه‌ریزی‌ها قرار دارند، شهر ژنو در سوئیس که در نزدیکی محل برگزاری اجلاس قرار دارد، به عنوان یکی از گزینه‌های احتمالی برای امضای این توافق مطرح شده و ممکن است این مراسم از روز یکشنبه ۲۴ خرداد انجام شود.
یک مقام ارشد ایرانی و یکی از اعضای گروه هفت به بلومبرگ گفته‌اند که «احتمال دستیابی به توافق زیاد است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/76260" target="_blank">📅 17:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76259">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QbT23vlMoCj-HcCDcR8WfUloaZK8-GL_MZXthHFY9tCoYJLT5IVvElZUEvQry_KrpKeaQXIutajlachI4nGyz9Zbd2zOrwLCuzcjzGS5xdRIqNlevimCqBF9NfSeWa6Z9o3kurlku4ggfMcrQfTH3P0rBIrSiE4lVdSx9GssniV-CpAf6TBTNQc-JgDRGAdshI9cjrsMHvNsOeq4XKEgyqAPAa0PN9HXt_H4Cn5cHwFyCGGgZub3w_vvEonvC0sowgy8xh1IzYrvobDnrtkECruvRvJlug8LwJNDkdY6_9A9UMtjpSCZM1dhSlPsp9iylrcTJscf65cGh_pqMc02qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76259" target="_blank">📅 17:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76258">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea9qTUcNkajekC0pNclNd_yCVH1yQClAolrW7w1-4j52CMJ6QaSiYT_2Br4fHH80N4N0nBOdyhbogzEHADrFXq0P81mBaAuNG0P8M6B2sb6b6FK8mX363lXifUgXuCzufZugXhcDzWorotkT04i5NYpQnm_5NaSLVnVz5gQ_IDKNpj4ngrXMWROSf3rZkfSFbIaltXdqtMo7fBXOb9uu6saj66Yru6V_npdpQHinZ8CNXoNAlWf_8ltDnerOu5_unnDlnAjc7W4-5WdXfNoQIIWKPO3ldIYJbvtr_wC9lzol8oxLhW4Q2wEDH-131ZeQTNcVbM3lo21yUZHtkQmfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«امیر احمدوند» ۳۹ ساله، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در نزدیکی کلانتری رشید در تهران هدف شلیک گلوله قرار گرفت و جان خود را از دست داد. او متأهل بود و همسرش در زمان کشته‌شدن او سه ماهه باردار و در شرایط استراحت مطلق قرار داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76258" target="_blank">📅 17:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76257">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/76257" target="_blank">📅 06:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76256">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/76256" target="_blank">📅 05:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76255">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/76255" target="_blank">📅 03:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76254">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76254" target="_blank">📅 03:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76253">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bg3UhtKjafgLY5ar7ouJwQdUAOARsaib2-DnVI8LtMey3aBuQRu4UNw4Q6b4z9bdSxdlZzV_qHY162H4twGDGz7oXXp7dIE0wiUHp4hrgNUNar-tIqSxxJWBlIyYAYWpgmhTt1Gakj-S6YrxpQh0G-_nlQf2PTfCfMcRx87zxwz7nd0LtwbY_KJutqpYcAoHOqTBNdNyKBg1uGibsbtwz3hnVWcOGGY_zcNDWBDHzf7Lh9EPhVhJH3BwpMPlpFieGvB-uqx_5PtEabEWdaembIuQHQno7BAjZpAoxiBpyZ0kMnc06DjpkzhEebnaj0ptA9HD2H1ZjZRUOzDMNNtLuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه العربیه بامداد جمعه ۲۲ خردادماه به نقل از منابع خود گزارش داد پیش‌نویس مفاد نهایی توافق میان آمریکا و جمهوری اسلامی شامل تمدید آتش‌بس به مدت ۶۰ روز و بازگشایی تنگه هرمز است.
به گفته منابع العربیه، مذاکره‌کنندگان در طول این دو ماه برای دستیابی به یک راه‌حل سیاسی دائمی تلاش خواهند کرد. این منابع افزودند مذاکرات هسته‌ای بر سازوکارهای راستی‌آزمایی، روندهای بازرسی و محدودیت‌های آینده متمرکز خواهد بود و در همین دوره درباره اورانیوم غنی‌شده با غلظت بالا نیز گفتگو خواهد شد.
به گفته منابع العربیه، آمریکا دسترسی به بخشی از دارایی‌های مسدودشده حکومت ایران را تسهیل خواهد کرد و در چارچوب توافق، کاهش و لغو بخشی از تحریم‌ها را دنبال خواهد کرد. این منابع همچنین گفتند آزادی کشتیرانی بر پایه توافق میان آمریکا و جمهوری اسلامی احیا خواهد شد و گفتگوها درباره لبنان و امنیت منطقه‌ای نیز پس از توافق ادامه می‌یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/76253" target="_blank">📅 01:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76252">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/76252" target="_blank">📅 01:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76251">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/76251" target="_blank">📅 01:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76250">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76250" target="_blank">📅 00:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76249">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qhm05NZ_zyNMuc__R4o2hUIvuRmkX2hVOOc0GKJ8idMnqOlplbyIPogyWx1GisNGM6Dcqvii-b0q8r8UZZv_v_ggw0unM6aTYIpMlmH2xqYJdSRmmfodqkcLMlO-lz3BRoonExmNh2PUKuyCob86hZH88LGoNaMYr6JYMmFVtFEUfyU11FRuXues42zFJXT5VqZdScnxB7qIlE0ZykKLn2_uWCUhmaSOOeX-fNeKxuV-5fxgUII_ksnRyH7ufk4LU8AH3kTzU7YQKHCeUTb73Du7misJYZvKqeXkOzLPURQnMZUrtA3OvMNuNXx9Ttz1AA7CG5xAn_xp6J3AJ48tsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابعی در جمهوری اسلامی نوشته‌اند که: با میانجی‌گری قطر، آمریکا به شبکه beIN Sports معافیت داده تا مسابقات جام جهانی را در ایران پخش کند.
تاکید هم کردند که: این امتیاز توسط دولت ایران و کاملاً جدا از هرگونه یادداشت تفاهم (MoU) به دست آمده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76249" target="_blank">📅 00:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76248">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/efef15c7c2.mp4?token=ngawWq_s_cy2WQD7n9O66rEwPFs0MnS_ICCSaFTM9v24EhLiq3-cQUk9egRVWPjopcekwo2M_2Fg-074hbCP-HxDwyKqYnEV5bnxXEs27ncv1Sy9dsLzyCj8E_aPflJhSFEMOo5B_jSaQmpwuz7PSsCs4Uea8XNVxheboBVFrRx_VH0IwFNAziwIrAPS2AyJCjaDy2DqLb9e-MFKAFQSLxC5Rwg2e9XAoSZYWJNch3SCvIuOiQDXNxCpWWPg-pOMRNM66MPpAzb3UUyI1gM6ivGrQoaWhUp07fq35b2QMHVr2B6Lns77OIcIqG8xwMKsb-H_6pdkce8JJjor1wJJnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/efef15c7c2.mp4?token=ngawWq_s_cy2WQD7n9O66rEwPFs0MnS_ICCSaFTM9v24EhLiq3-cQUk9egRVWPjopcekwo2M_2Fg-074hbCP-HxDwyKqYnEV5bnxXEs27ncv1Sy9dsLzyCj8E_aPflJhSFEMOo5B_jSaQmpwuz7PSsCs4Uea8XNVxheboBVFrRx_VH0IwFNAziwIrAPS2AyJCjaDy2DqLb9e-MFKAFQSLxC5Rwg2e9XAoSZYWJNch3SCvIuOiQDXNxCpWWPg-pOMRNM66MPpAzb3UUyI1gM6ivGrQoaWhUp07fq35b2QMHVr2B6Lns77OIcIqG8xwMKsb-H_6pdkce8JJjor1wJJnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره مقامات جمهوری اسلامی:
من این افراد را بسیار منطقی‌تر از افرادی می‌دانم که دیگر با ما نیستند. این یک گروه متفاوت است و من فکر می‌کنم گروهی باهوش‌تر است که منطق دارد. همه آنها توافق را تأیید کرده‌اند.
آپدیت:
بعدا ویدیوی طولانی‌تری رو جایگزین کردم که اکانت فارسی وزارت خارجه آمریکا زیرنویس کرده و شامل حرف‌های دیگری هم هست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76248" target="_blank">📅 00:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76247">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OcULDKnW2bHTxHHDUSgPo_bMfw3gjv-CXUSxhcoUZluiuHtnt_ZzvmQsZcHvIKELYppeN-ivWHHkotdVuTwQRsMD7jqlc_7GlecMbx-2Pp0uKWAVdcQJehFf1eBWYAcVVb-8oiNqIv19sdwzSH8aruh-MhY2J_5sgCpNXd3rn5NLBd0yMHC7EYaGO8As23WDzr4NM4zG6s4YkSi_Y5mPGN2tjomskr9QstGsLN9TqvSuKaCR2kpUCPWfbbEypoQ0DDNLkFF92QIW9z5TtEfVCF-3Qmhq7dfSYr60V8oOFHv_X4ytroXjJDV7GLQSJ_dtLfha_LPDQmsZ6llHbePmGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی در یک مصاحبه تلفنی گفت علیرغم فعالیت قطر و پاکستان به عنوان میانجی، روند دیپلماتیک مذاکرات به دلیل اقدامات آمریکا تحت تاثیر قرار گرفته است.
اسماعیل بقایی تاکید کرد که بخش عمده متن توافق نهایی شده اما به خاطر مواضع ضدونقیض آمریکا باعث تلاطم و اخلال در دست یافتن به توافق شده است.
سخنگوی وزارت خارجه در این مصاحبه گفت: «ادعاها درباره زمان و مکان توافق صرفا گمانه‌زنی رسانه‌ای است و تا مراجع ذی‌ربط نظام درباره تک‌تک اجزای متن توافق به جمع‌بندی نهایی نرسند صحبت درباره شکل امضا و مکان آن فایده ندارد.»
آقای بقایی اشاره کرد که متن توافق از پیش برای ما روشن بود اما طرف آمریکایی هربار مطالبه غیرمعقولی مطرح می‌کرد و بار دیگر تاکید کرده که ایران تحت فشار و تهدید از مواضع اصولی و خطوط قرمز خود کوتاه نخواهد آمد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/76247" target="_blank">📅 00:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76246">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/olN0uTZAv7MraC6I7C6vFNT8UNx7Ggpm5LvWoJ6JmxJsfZ9NG2HzJNGYwMKPxymbXSIZwkGyFUvRc8r3VpwCEXBxrvsUxvAgxXO_9y2u52ApL0qOcayVi2UK2gQgzwDFWZeB6-0M6ywnKa1L-a_UvCogQ3iw0WIGYoHBnM_eoZb3l0Q27weNwNoCSkgBq6Y-WDD7BzXgoB9NnwGvOvOVGQ5rcylJ856XoNso6u7dtWQKVSpal6kXHQUDnT7zAgoSd0yM_sdAX86GXs1YDrBWY95GDcpRaq8n-7pYcC_aeVH-M7NO07J_RqkKML6RgNpbxaPyMa0JIMNWq4_oUS_flw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/76246" target="_blank">📅 23:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76245">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d148f37d4.mp4?token=mRHPmUP7uhN4l3TR9ncOHfxO0Oj7oWe97G_8BrFnfy2wzncVSAvBSb4BgqvkxdcOu0SomerCliBOOlXXoefBG71ZZdOAhmRNl__UVpQyP1xkmIn93xrbu7irtEk8prjV8MDG8EJwjltVlrTTW7U3nRRw5VMVki7PGGkZlgKHduU5TMvX9WNQKG_dL-phrq3qY60hetUD9TBmwAED_lLe3WZrROt0NAcnY52rovDpHoTGLq2JIz52gB8DyL5rblwoLz1OOpN4alpbPAlU6ex_4yQpcy41v9jAU8ZaO8cW4SzMHyHzPSHox1FOMYFOBH48Yzk4Orpf4dl4_1SLwTgZIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d148f37d4.mp4?token=mRHPmUP7uhN4l3TR9ncOHfxO0Oj7oWe97G_8BrFnfy2wzncVSAvBSb4BgqvkxdcOu0SomerCliBOOlXXoefBG71ZZdOAhmRNl__UVpQyP1xkmIn93xrbu7irtEk8prjV8MDG8EJwjltVlrTTW7U3nRRw5VMVki7PGGkZlgKHduU5TMvX9WNQKG_dL-phrq3qY60hetUD9TBmwAED_lLe3WZrROt0NAcnY52rovDpHoTGLq2JIz52gB8DyL5rblwoLz1OOpN4alpbPAlU6ex_4yQpcy41v9jAU8ZaO8cW4SzMHyHzPSHox1FOMYFOBH48Yzk4Orpf4dl4_1SLwTgZIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: ضرب‌الاجل شما برای رسیدن از این مرحله به یک توافق نهایی چیست؟
ترامپ: نمی‌خواهم ضرب‌الاجل بگویم چون بعدش می‌گویید من ضرب‌الاجل را رعایت نکردم.
خیلی مهم نخواهد بود چون قرار است امضا شود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76245" target="_blank">📅 23:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76244">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e75104b39d.mp4?token=GrBX3ebNVM-1L3gaWGCQ973Kg-wZFCFoA3R3Lr9Mxem_yS_YWqz6aJgv69cgYkkP3t0q7dOvxt9lFhy0gjNp_wHQBXPv4CVCbURUEEHYWK1y9v1LusJ1fmwq3ra7ATx0_ukAsna-nKJjJDrUON2hB8dJyFmi2zXAjAr_2F8Crg8hA9hNc7Na8vjsjEZVVLKOl5RkAeO3zKARqVpVpMpa91NqicXPs6ST4ouVjsmwIKBKFlF3-E5Y9azQersmunZN2D_eLu_zDkx-7OBNejDM_yWnaCG4wpunC7f7ncxzk0Hwg5c4n-hTGUoKP9h93fRd1QlUiDAjz62z2tC9-uBxcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e75104b39d.mp4?token=GrBX3ebNVM-1L3gaWGCQ973Kg-wZFCFoA3R3Lr9Mxem_yS_YWqz6aJgv69cgYkkP3t0q7dOvxt9lFhy0gjNp_wHQBXPv4CVCbURUEEHYWK1y9v1LusJ1fmwq3ra7ATx0_ukAsna-nKJjJDrUON2hB8dJyFmi2zXAjAr_2F8Crg8hA9hNc7Na8vjsjEZVVLKOl5RkAeO3zKARqVpVpMpa91NqicXPs6ST4ouVjsmwIKBKFlF3-E5Y9azQersmunZN2D_eLu_zDkx-7OBNejDM_yWnaCG4wpunC7f7ncxzk0Hwg5c4n-hTGUoKP9h93fRd1QlUiDAjz62z2tC9-uBxcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: تنگه باز است. تنگه برای چندین ماه است که باز بوده، اما شما فقط از آن خبر نداشتید.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76244" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76243">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38fa98505b.mp4?token=FCOfbnMhW9YwL7-D-1MfWQW95pEb0qoNYcyle3kpVXsjGCn_so-VMNk_QTC4OjQto7HvDCkuY8LGPizc46ibTohk-RtZPWBI6ovzX9fDFKVPjx1nX1bgSNxXhkkV0ec0nPHueG5igJwXNOIip7fsi25G8rM44EeeJG_jUQuoQ_q0u2VrFIPMjtd5sUJKzKvW_bHIAbuA_MR0jXFg2YpyFbE-Kz7uNDIP-bCQxwNSXb3eaHknbxj4viE4Bwtp2FlTF9qunknfXe-f5fDzZweENGGWUnJB_lkxaIBeR5kbJ4XUqie_00re-UCfvimxWLhMJmR4tgOiAPB-zy5YvqZ1Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38fa98505b.mp4?token=FCOfbnMhW9YwL7-D-1MfWQW95pEb0qoNYcyle3kpVXsjGCn_so-VMNk_QTC4OjQto7HvDCkuY8LGPizc46ibTohk-RtZPWBI6ovzX9fDFKVPjx1nX1bgSNxXhkkV0ec0nPHueG5igJwXNOIip7fsi25G8rM44EeeJG_jUQuoQ_q0u2VrFIPMjtd5sUJKzKvW_bHIAbuA_MR0jXFg2YpyFbE-Kz7uNDIP-bCQxwNSXb3eaHknbxj4viE4Bwtp2FlTF9qunknfXe-f5fDzZweENGGWUnJB_lkxaIBeR5kbJ4XUqie_00re-UCfvimxWLhMJmR4tgOiAPB-zy5YvqZ1Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76243" target="_blank">📅 23:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76242">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30b9b51ccd.mp4?token=fjAjnFJ79ID3xjGNzpG58DpNEm09V7mNOeyIHn6U0eML9REzk-TC7PNYN1f-KOpL-r3HsSD1t0v1iLvJov8fJWEspRS5skZ354Wvh9fPlhM35wMNLRhCvoDinLmfpaA_HhDfBVtPNKoEwpmg4MyKXfv5GJ1egrwWePY6SjCFEKrENjJi5J9dqmvvlmBi0Ql32XHdaVUKFGmyI3kCky-Fek6a-aJ0yhjgB47DG0q2YxzZWcZhCkZHS5SKOvp0-QIQjvxb6emz3qptiFr4uT-FvHVq7EUpuk77z4dUjYfTsQfKlfbyWd5BEOySVZWTLFBEC8hKbSTK8uhoFMvckXICPg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30b9b51ccd.mp4?token=fjAjnFJ79ID3xjGNzpG58DpNEm09V7mNOeyIHn6U0eML9REzk-TC7PNYN1f-KOpL-r3HsSD1t0v1iLvJov8fJWEspRS5skZ354Wvh9fPlhM35wMNLRhCvoDinLmfpaA_HhDfBVtPNKoEwpmg4MyKXfv5GJ1egrwWePY6SjCFEKrENjJi5J9dqmvvlmBi0Ql32XHdaVUKFGmyI3kCky-Fek6a-aJ0yhjgB47DG0q2YxzZWcZhCkZHS5SKOvp0-QIQjvxb6emz3qptiFr4uT-FvHVq7EUpuk77z4dUjYfTsQfKlfbyWd5BEOySVZWTLFBEC8hKbSTK8uhoFMvckXICPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ممکن است آخر هفته در اروپا قراردادی امضا شود. من نمی‌توانم آنجا باشم، اما جی دی ونس آنجا خواهد بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76242" target="_blank">📅 23:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76241">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f82f63f23.mp4?token=VCqG6npvEgi4NEnNeYmNx4E6hioHc2opmaUHakyOH9MvmbmGECiDFhC_ymkPuHXzdktFGvBRJmiVYiIhnGkwRmOJtUG4aagzDFh-BsvU2u63NgX-_Wj8HpsNGEgTRUuIjx6MLiiKL5mQTUdqE8npEpZIb9ow6SkPXZcWJhppeNSrtMWhR8cFxhgfO3osI01WRcUz6VVjX_vXYJHGOe6Ce6EXuFOZtpMGXJd4VgVW-YaEsZHw_1bDVxWYftD60aSK8wfbK3ysBCgGg2m1F8CnHIRp1iBzuccG6BHk3TWa3MOUldQPYHeep8JldpC64exUlWyWMtdxAhjTxWYRKCRkWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f82f63f23.mp4?token=VCqG6npvEgi4NEnNeYmNx4E6hioHc2opmaUHakyOH9MvmbmGECiDFhC_ymkPuHXzdktFGvBRJmiVYiIhnGkwRmOJtUG4aagzDFh-BsvU2u63NgX-_Wj8HpsNGEgTRUuIjx6MLiiKL5mQTUdqE8npEpZIb9ow6SkPXZcWJhppeNSrtMWhR8cFxhgfO3osI01WRcUz6VVjX_vXYJHGOe6Ce6EXuFOZtpMGXJd4VgVW-YaEsZHw_1bDVxWYftD60aSK8wfbK3ysBCgGg2m1F8CnHIRp1iBzuccG6BHk3TWa3MOUldQPYHeep8JldpC64exUlWyWMtdxAhjTxWYRKCRkWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/76241" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76240">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سی‌بی‌اس:
احتمالاً اوایل هفته آینده یادداشت تفاهمی بین ایالات متحده و ایران امضا خواهد شد که راه را برای مذاکرات بیشتر در مورد یک توافق بلندمدت هموار می‌کند.
CBSNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76240" target="_blank">📅 22:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76239">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HJY2_tslFegptlE7oCV_LXDOMTdpcGSArLxLS5XfauhRJkMe0_8b8Sh7U9tH8f8jUXGnQ2Ak1bE4iqb4E0msp7pW8YeW7TZJrH5MhQxr1x8oqms6wScC97wqjRY3WRlQHUWKQD_Vd9QJO5YjoTljirdQcvyK56Qahc18bS5Ybgp9kuDA7Gu3yf6kVcP2pLkzGno7Hj1Ac0u-sjb5R9KprB2OF6USiwxPlF4fNEyikhyaXEZ_bUTg5kSnoh6uHKI71tIuZoDO1QaMLJwuDGyAn2Pkfx5p4gxdVVlTb9OkW3tKff-HhxTzOgkO0n_CFkz7ba1KrdY0WcB1WK4DV8uKpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس در پستی جدید نوشته:
"بنظر می رسد با توجه به اینکه امریکا متن پیشنهادی ایران را پذیرفته است احتمال تایید این متن در مراجع اصلی‌نظام بالا است‌."
🔄
آپدیت:
خبرگزاری فارس جملات بالا که در انتهای پست نوشته بود رو تغییر داد به:
"البته بنظر می رسد با توجه به اینکه امریکا متن پیشنهادی ایران را پذیرفته است احتمال بررسی مجدد این متن وجود دارد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76239" target="_blank">📅 22:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76238">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QVklxA6HpPCPej7aGL8KZQNqrW_GMQDSy9LQXhQR3G8PytHBjksS-3LJS3ZUEVJ8LSyQLiD0OFUTK2i8xSi1KMA_tat3hfMKP5cehUgk1SYwHDPzkOe1uTxCANUG3YOPfTFvoE8W1ZBs2suv0vtcDrA2PNJVmuHT6ePkD3KvFSPAYIEqo-jG9kZVmuEMW-4OHFBjhp_PZvqP2uyhJEjAn6cwMCEIfnH_MoVkmvPsgiSPHVZLEEqAZPUa2HkHQbqaB_iRn4JKechGQRR_jXSY48ODtrST1SlmeeZPX0jDfE5Irvplpz1hAKYvgzJmrVdF2JMknD3nIYH9sPPtYPpzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحدث به نقل از یک مقام ارشد گزارش داد هیات قطری که از تهران بازگشت، موافقت جمهوری اسلامی با پیش‌نویس نهایی توافق را اعلام کرد.
همچنین دفتر امیر قطر اعلام کرد که تمیم بن حمد آل ثانی، امیر این کشور، و دونالد ترامپ، رییس‌جمهوری ایالات متحده، پنج‌شنبه در یک تماس تلفنی نتایج رایزنی‌های آمریکا و ایران را که به پیشرفت در تفاهم‌نامه پیشنهادی در چارچوب یک مسیر مذاکراتی منجر شده بود، بررسی کردند.
دفتر امیر قطر در بیانیه‌ای افزود که ترامپ به امیر قطر گفته است تلاش‌ها برای تکمیل مراحل نهایی پیش از اعلام ترتیبات مربوط به امضای یک توافق ادامه دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76238" target="_blank">📅 22:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76237">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نیویورک‌تایمز: ‌قبل از لغو حملات برنامه‌ریزی‌شده به ایران در روز پنج‌شنبه، ترامپ با میانجی‌گران پاکستانی صحبت کرد که به او گفتند با ایران «توافقی» دارند.
clashreport
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76237" target="_blank">📅 22:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76236">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H3Oc5awU2AReYCfzF956X0Gn1Lo-AqlboXM4YCxlzeiaLkoqAq48rnE5eyiwWXWm571w2SeC2FDPKluxJc7HmQA8CKi-GwqatXLR6cyDpbHgoUTu6Epxn7oHcr5s6XF4QmTNO5wEt9MpfGGOgAcv8pBDvgNmMQEoMXbKxGZHnZxRpY1V6L3nD7ASO1MhPK4dFOrz-rrD6ruJy0vIdCv81Wksy58EZTXzeNxr4jW2RhSCuvTBSCTEhBzvZggoLtjSDK1wqYgYjixvtsSdVlu_RPYKDV_GPEOYk6QmD_WI8xb6e_WIjzBjdNCdHVt_HRBswqcHDh5w4He0cCii_b6Ldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع اسرائیلی گزارش داد پست دونالد ترامپ در تروث سوشال درباره نزدیک بودن توافق با تهران، بنیامین نتانیاهو را غافلگیر کرد؛ در حالی که او در میانه یک نشست امنیتی درباره ایران حضور داشت.
سی‌ان‌ان افزود که این کشور از وجود هرگونه توافق قریب‌الوقوع با جمهوری اسلامی یا تایید آن بی‌اطلاع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76236" target="_blank">📅 22:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76235">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hV_VNMP1z0zqWWBPPD4uhRsp0eHQDln804ZIrsjFwP5Gcv2wKrhuhLVxRyFJjif5T7JuI5bdzNgceORx0x2Dy6DSsQhthBX-CjGh6AaWt8VKjmMpqecjchY75dcHZvlUiPjvDNjSlu3JTa5z2W-pEMXYuqXoWlmo0YRX7IXLlB9cN2fhEBTnyc29xtHF2-fQ3LcmTsP58EoovrR0SPE_CXk7zeatpLhVnjr8nldM6IP_ObbITeCTmreOe4gZ0kjeFpzp4yi-2YHVX4efkaC5Z7ZQo9YJ606QlTPe4bEjhDQVuci672r_GALfdZa7RXv2b1A7dNDT1T_Kltk_wfxd6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران، ساعتی پس از پیام دونالد ترامپ دربارهٔ مذاکرات با ایران، مدعی شد که «هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تأیید نشده است».
فارس ادعای خود را با استناد به اظهارات «یک منبع آگاه نزدیک به تیم مذاکره‌کننده جمهوری اسلامی ایران» بیان کرده است.
رئیس‌جمهور آمریکا گفت: «زمان و مکان امضای این توافق به‌زودی اعلام خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76235" target="_blank">📅 22:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76234">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nRi0ZEMucvhpxjz4G40ma_HvUG0RY0YfPBdjtqkrqCCF8_dWp4Md1UAkjBa9X30bO6U74GbUfVIcjl7mklibEe8h_uDZCKvwBFsSx1wvbORZxOaQUUMb8ba_S4WAVZJFXXMEEcTWiX_9Q19fw6288mVIWUsmVaV98VE5E4qaKnr14mTYieVlncQaPtsZ7xRyXZCKowAP5bNatCJ4fKHLHJA_Zj0cLaH4Yed71Oc_mGfu_tuVVTs0YPnQXpD-7RSlebl7uH40GmCHutJ9Phu6TBj8E5WrySEa8WFLCKTWLVpKxlBPmAKIr4XYW53-frYfmDdau_IMv_-SQywSEmEEbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76234" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76233">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MSsDMgezoU46m5RNYHyHfhuzC97MYuQTpiuerYph1VCmwpVyJ6xSNt73Dsv3yJFM8k7vqL-GvIaKubLz7ekckVAwMFoTS_LoloafFIaiP-Qf2idUOhm0WV2ydD4UaW1Vad8CaA7dxYuyyViucbS2tQFHNdeqWRYi5b2RReoF50lICMSv6n9PXfjpTgBmwxNK57xjkEBXhsFNHYMIDHmGreklwW-a3QDaFWXr8PyWwfFrQbTcPiiCIpxN2oTlaQg8n4LMw-OovJmpKUxPKXJC8TYi0xe0MCtVymv_V_KMooRZBa1ljKNKvANQbLYe8MF8ZltnQYnErz_QOFEfqZvFxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76233" target="_blank">📅 21:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76232">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw3rHTlFA2U9O6kzDs0hrZvx1A0M65bowIdwjBY49VlF_OAqkgckB8KOYM8pTAQbSZIK09yWW-1Ty4iR0u9J58_jTMwh41n4p1D9kJzh3fs7rEyGqTDQQQxlh6bHWIBQu8hSitRGUcj_hvsL84sjNHWN9GK-bB7P54kU31RpTeRPoiwBXBOvbhmtW5UYQ4MpYljQM_ahALwZ_9lNhOlIpCfa-tXFssa1N7YUNYs8U-CEU8xE82Y_WIzyaL1O6NPozyGO6wW-YC-pd337yKmsFK0gXn2FEsFa5Ibq6m85lWNoLMGSU3p8Mc8uWfYwHblLv0yDAa4hU72P5P72ECYFmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LzzheIa29S4KV1VScWZXDt98qxVqPe0S5rtKIqprNH29ZhyYaPhFRAGKPAiT5M5H1dAGKWKxjiteSertu06gAaouoFE6kUXRWEDtdYIRztfoUI_Fca6K0OJQ_00_GNItRgeeY3kxHDGE9Yf_aAKKq7j0kg-cOJduITMeJzWmkqlimU1zKuQKOHCmSamhp2RjlDoUFiF4b2sIFj550Slw9v0-XD8m1k_B2x-bC8E-OpZOMfd9Ep-85OeOPoqIVoFhuW3l57ZqMn_ECUXUz--vcIMzFc5E-tgEW4r7yN9ofPvKX31uxA8n-Lv0yMyaI-sVWDeI4ECCw-PmSXtD57Ad7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع جمهوری اسلامی در بیانیه‌ای اعلام کرد «هرگونه خطای محاسباتی یا تعرض به امنیت و تمامیت ارضی کشور با پاسخی قاطع، پشیمان‌کننده و فراتر از تصور غلط دشمنان مواجه خواهد شد.»
در بخشی از این بیانیه آمده است: «بی‌تردید نیروهای مسلح جمهوری اسلامی امروز از آمادگی، توانمندی و قدرت دفاعی قوی‌تر از گذشته برخوردارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76231" target="_blank">📅 20:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76230">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OA929wUZvwbfWQqB9kCvt8dz5EAnQ8TD4G9e1fQsOCwVmq1o4JA0tnGPFmAYFwdiNHmBg1T-xFdLMetwHPNvYMBcT19eNlkMOaenYLYtwZvOM7kYbNnQ1Od8dH3COGBuHr1QNdLuUiVilGjQXc2Wh9YkCdtTCDkTRGOu-mIAfY6hrP2fCJpXaJpk_BFX_618ukzeeLNrbYjroHrQ55WgiCsWI-hyBfqbBSWqpWmh8wjyrEOEar7fRnn0Psou7Zebc5ZgCcUPVOAKLK8bPdEWa4iy_f3IkNmwM8xCEf6cKGFbvY5klVW_DGmNHBvX4ZqKtXgYiZiWuv5rqPneBhj5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، در خصوص تهدید زیرساخت‌های نفتی ایران از سوی دونالد ترامپ گفت: «یا صادرات نفت و گاز برای همه برقرار خواهد بود یا برای هیچ‌کس امکان‌پذیر نخواهد بود.»
او ادامه داد: «در صورت تکرار حملات آمریکا، پاسخی شدیدتر خواهیم داد و آتش جنگ می‌تواند گسترده‌تر شود.»
فرمانده قرارگاه مرکزی خاتم‌الانبیا اضافه کرد: «تناقض در گفتار و رفتار آمریکا عامل اصلی ناامنی در منطقه است و امنیت تجارت بین‌المللی، به‌ویژه در تنگه هرمز، را به خطر انداخته است.»
او گفت سران آمریکا با «عدم شناخت ملت ایران و نیروهای مسلح» در دور باطل قرار دارند و با جنگ رسانه‌ای نمی‌توانند «شکست‌های پی‌درپی» خود را پنهان کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76230" target="_blank">📅 20:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76229">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cz2zUL7_2bia4l_QGsy_hoNiYQ9ZATOlKbgsZ4D5rWcMlbIGon1DlSbBHSb5eNAFzA-cYLRa6_zBIkRwTgH3OwEoMNNMP21GfNvDP5GTtZplOkKwkjs7BP0ruaiYMwDa-tG7UR0zjw7B8XyydJWbCl8Ku13dYYteS2lp7iGBAJly1aHF7PA0G-cW7KxBtJAglM9O1Bdm0CzYrx3mTgjcBlZbZKzNnnw2tqkohk-ZtyZslHIFg-UUIpyJ59qC-wwJm1KbS2t-1W7aVx11HCPHuFdB9ONn5jbzU-vrq_U9FJmJN1WlNDSuouA8isSra3t2eAFiZqSHU5biL4vbTmXxOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76229" target="_blank">📅 20:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76228">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a8d3934df9.mp4?token=NYuWS0l1aRkx5xplE4upF4YLJxMm5syHdKQM7V6YGHVmZvPjAa7H_5kCcYoun9g3RchKP_C_A0lpVlcKJdefTLGLDqyUthLVGRb5rsvA3SknS-X_ErTo6ivXS5iqxUVn1t6JxvNIKA1MEAzolur2m-wXcaIj4jU5CfswZAUkLklz6Zb8hV6DkhR-R8blxOD1c8PfipzK5u1DMiKuii8cfD9g6xKeHpQGRBZ8Mw8UpieDlyNAg-Ym7SwQl1H1EQSCyo1bN7aG1Xz3F7Sh1Tn8mKGnRbWzTta-yBbw3JU7vXh13DneqrLZ2pyQZHVJPXBmMVlTab2jptwF3Lu33XmJzy5xq3wv56o2NFDFiCQ0b7tq5Piv0XVXhu2Yo3IZVwtEeGysMbLyK2wVnsNnWOwLZQCobaXXjWMP8Cpd5YAJSb_kMGReSF0F78x6PgprPfGn63dRLzgNpZouKRjirXnW0muVnQkl8lMsY6Z-ruBQtf7EKLhIFY4Wtkb9SXeLTb0sPUqjyMRdrrKr4yJ7c0yFzJR-0HKexGmfV29IoRQ2_BU842wh_9Fv3Nuuck4lrOoG8TiFPZ6HTJg_XivStJzzGM63loM6RZ8yYXYROpbVei-m4GiBEocwhBhyPcTKxa3_Le5BNbjDNsugx8IcKvL0TmtXdiPF3GXwPbh0WmjvWxc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a8d3934df9.mp4?token=NYuWS0l1aRkx5xplE4upF4YLJxMm5syHdKQM7V6YGHVmZvPjAa7H_5kCcYoun9g3RchKP_C_A0lpVlcKJdefTLGLDqyUthLVGRb5rsvA3SknS-X_ErTo6ivXS5iqxUVn1t6JxvNIKA1MEAzolur2m-wXcaIj4jU5CfswZAUkLklz6Zb8hV6DkhR-R8blxOD1c8PfipzK5u1DMiKuii8cfD9g6xKeHpQGRBZ8Mw8UpieDlyNAg-Ym7SwQl1H1EQSCyo1bN7aG1Xz3F7Sh1Tn8mKGnRbWzTta-yBbw3JU7vXh13DneqrLZ2pyQZHVJPXBmMVlTab2jptwF3Lu33XmJzy5xq3wv56o2NFDFiCQ0b7tq5Piv0XVXhu2Yo3IZVwtEeGysMbLyK2wVnsNnWOwLZQCobaXXjWMP8Cpd5YAJSb_kMGReSF0F78x6PgprPfGn63dRLzgNpZouKRjirXnW0muVnQkl8lMsY6Z-ruBQtf7EKLhIFY4Wtkb9SXeLTb0sPUqjyMRdrrKr4yJ7c0yFzJR-0HKexGmfV29IoRQ2_BU842wh_9Fv3Nuuck4lrOoG8TiFPZ6HTJg_XivStJzzGM63loM6RZ8yYXYROpbVei-m4GiBEocwhBhyPcTKxa3_Le5BNbjDNsugx8IcKvL0TmtXdiPF3GXwPbh0WmjvWxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما هواپیماها را وسط تهران به پرواز درمی‌آوریم و آن‌ها حتی خبر ندارند. تمام رادارها و پدافندهایشان نابوده شده. آنها تمام شده‌اند... برایشان سخت است چون مغرور هستند. ۴۷ سال قلدر خاورمیانه بوده‌اند...
ویدیوهایی است از
این مصاحبه فاکس‌نیوز
با ترجمه و زیرنویس هوش مصنوعی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76228" target="_blank">📅 20:27 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
