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
<img src="https://cdn4.telesco.pe/file/K3YVK4BJ-JC6DUD4KEk_geJkgAcOFrS-HMVFYp0xfHB2Fjrz9x3NYjKJhaDi4LBbIUQA_H9-iIedkf_R2rKQclh5JfFzKm0VcGfTc1NOUOqGtz7NvYGyimX5z5UhURXJw6FHYaJInFIl5AR6VklZodg5cTPmzN4D6AOkyP83WWOxYAcqXWDp9T_hjxEIEpU9GlfZAfKUBhgZ8BmxJfyMRn67VLcVuAMx-RvLpmjD6H2AxlS-SsASVB4DqgbVvCmJKYlTfmcl1aup3gkKdPR9UZBosPkshf6NLOE2v3G1zexE2RgQQ4qtQvAM-ftBsG_rmWnJhpPQxha3sQy4PeWBaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 01:58:36</div>
<hr>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 261 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 453 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 479 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=gQ1QxEAr98bZbxe6sd8BxFPWBZP5xAlXVjF1sQ3yGGXWZmBZ5RSBlq-u9qf1M4NYKyDRsDeXlv6CXf43Uss4QRNB1be3LSxRZBW4ggydqHcMdevRRvSuyyNbW2iiub9CPWXpGT6YznZOCIDtw-gS6r-bf75Sk8OJp6Y9byXXz8wSc6VSMA1hzCZC-XFh2dGMuSIf4sONKYNxvYAbKRPkFdUCF0ajhOkxP-DJZ48WS8JtdXBXS6z1g1o6_xMD_ePvIhkcrnBc7M7xQnn91B9SXV9q_uY9VcbB56OAQyHOqc9G6gcRt4ifI8VoW33199gAzTKMu5y6y8P3rvzOtCWLKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=gQ1QxEAr98bZbxe6sd8BxFPWBZP5xAlXVjF1sQ3yGGXWZmBZ5RSBlq-u9qf1M4NYKyDRsDeXlv6CXf43Uss4QRNB1be3LSxRZBW4ggydqHcMdevRRvSuyyNbW2iiub9CPWXpGT6YznZOCIDtw-gS6r-bf75Sk8OJp6Y9byXXz8wSc6VSMA1hzCZC-XFh2dGMuSIf4sONKYNxvYAbKRPkFdUCF0ajhOkxP-DJZ48WS8JtdXBXS6z1g1o6_xMD_ePvIhkcrnBc7M7xQnn91B9SXV9q_uY9VcbB56OAQyHOqc9G6gcRt4ifI8VoW33199gAzTKMu5y6y8P3rvzOtCWLKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 523 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnzlBFxrT1pYzPiTOzySwy4B_MO7_-ughgllmJiZHCmqkhBUEogF3bE8NwgD8KO88h0DKSYSd2d_V5Cn21GTwhDrh9_nN-U8zEWz_dopzSvY5hQWUd-XyRO4oaKhscjvBdBX5SYf2z8WDhy8CMnODcJRRlHy03-B5xV3bnKNk4fSe-gdIGNprPHoenEiL5OtrHIP7PmateFt5am763PnGv65-Xjx7lcE4a7GnPEBV4SbsrxPbD1Dm2eZ6hjtrJFiEyKsmbcv6R9Q-8QxOAl0BGmbOsJkmDa2CbKd8qvfYZIKV2ijEax7aSQa-RAVXkDCTRQJnf-ypU1nlOBZcXySaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 552 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 648 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 758 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 871 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhTlYzmjThBxRn-cE6VocxNCA8kFPRGT070LCwfu-cyVUcsIyc7BiB6OTtKN2LicD4oZrSrh5DEeVKCJjkPYVjFhAczCXQ-eaPxKRaV3wJFBJFB-D_kw2rh4mdX5UbasIvGeYDsPM-0fPF2LL3SCDcT2Z89pOux9WiKzFJRMumhYJGZR6Gf7DbwA3l2N9mQdKMe5kvEl8kMz7x0-YnZQmV0ykYhTO5S2-8S_t4UgLBlCpNcHb35EY0EiA78jWu41XZKZxngYsE-UQXHbH5_AIiv4rxw64yiQtSROuKoqC6lGrxMrexiMBGO4thFgEMw0hXriCd5fvClgF6E92T94bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 910 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hICuOhg749QQhWHn9hvdtfS4ouvBMhIhxjzSCCgV3jE8LghJ6LvqcOWgkw4ZEIjETHjLo2fXxffbW3ZLGd_i6d9UknWe2POBj9bWHgyQ33p-zjk0M0fQ73mWwj-AbmF8srigBG868F4eY_rvkP7i_t4NbTb97wqDybV4S3JmPmKSR2JW_I46TBQ4whyG2qp-BYE4X_cfXRkU2LIpWmtwkigG8er21RPMB0rFTpnjxPIFiqbOHpOEqXEMTX6GTD0v__FSB-tKm-YWng8A4BTIsCYXNKK7aypy4hNbTG7ghLi3khKzIDrD9fDRWp_JBMNGdOxvSAVjtUYJuaYRKruJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmZVI7uHGAiAmZuY6urqlRPfVqtagjfgRk5wcqRXKEUGHe7DF76LjQElu9RXOhHPqplfnpalN_bgP4ScbxPsNVvapTxuC5SnckgjCMJSyo0MAABzbXD8kJuhcExWm5WOnM7fOqyahl-HfEIZA-U7ev5Y-9TOEUhg_OtnCzTn4nQp26YH1IXxvshWJC2gMXZm_F2w_vYTQhIyajAZUc7oGHIdgK18nQGmaH3H5kWj-5VPnU0PLXMrH0WZfsKnhTy8m2zsqZ5BmEE8k_6X1Sgdy2oG63_f-LSpwrxPMXnJsfSiJ6Vf1cm-pbUqHm-_5aoOiQ-8Ru4fTh8V7vgYv2juoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8UyeZBfioNyxtkOCpZtH6TrIkFCkOMokIbiKflanpWf9-lLzEtr-xAmMJKqBWm76zyt_bXFcpKq6UGK5K0EucmKrZYA-giZ-fmiZ-QN3e7dcMH8VzTyVxh-EXnwx32zgRQSCVoYH1uSjl9ioEBxdrlKUT8nz0eXuEH9zymnvuFkeZJHt1hc3TV42Hj488bd-rEJdBt9IrId6YpyRi3YImZZwjT_QMCEn72ROryz7V1yaPC5wceJZqziIb7L1zzKoLl21fVXi-nBOVaQqaA9930ZnbRrVBP156SMi-5wJKtU5iREzilVoZ9FMyZ9fuCDdjgVxJhaKMbcZjtu5JiadA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brsAxerZJe4c1i3ChaMrnGSVrAYw_rTlFtBHFoEuZVoLH1RAsF9Znz1O6hxyT6Y3AZNA7HvU180c1flckAX_5HK63_B01EWkdN_XlqvTbS74Hm89kyae-gF56PTLvjqbB11keak78yUpN2gO24QXlprv93urac9Hw94XDJuLIUZRaiyQoFUElePGL8DGHTuMnoy-6TDqKGGJqFITHr8VZ-Qiclb2bPh_G7ih3R-8UhEt4L3vDmfprbAzD_nCREJn7qLlax1a5kD1oLv1oeTzdvIZoSDKiAZOv6jvgB-SDEMzTWkcZaEZGJvnYBMyq8oZ8OfLjsVaHMIs73g7fXcwyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 997 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 892 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 953 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYWvEh3aQQjBU_TjQbiYM4tYMUwOsNQZgbVCstBv3xgSc6enMqzYYmlm8duM39defbRz5kK5cECsZa4Jkj4ysQxI_YLZmvYJ82XfMbkwsuPBXb3NOs4dwvGIQ-vjGO431pb8ryAdjccd9pNN-lGLB-vEAV-izOzLW0GNx0bSIF3sd9ZyZ4ff8-UizqapM1kkEw6kvul4Fb4U_Z-M4L4LjN5Hj7prX79DCojOGQ0MimzWl3LqYkutgc4XEEc3YFqiuTnuPclsepyz4QKVcjOtkjkB67RjqfSF4kVdroBs6K1FvgkR2qhNALplNtQN5MhVuFyhVXuYEVe6WVcMg-we4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxxUHALAS6R7XNz8Qsd9F6rcG6Hs87pacEfsTl7aFiF7bIpFWXcZKyf6n7bvVjOoUvIEU23bpANvHsbPCGDZsmcauo6d3EKerRIuE4Xt7i3s8g8m86S6tf9VRmxLDZvDmA_TbSvXtoYrlkunf2SOEzFATWkKv4X8VOhu-tOfs_MfLm088F5JFPGIvwVDp7SnsrtZbQoM4LR_22sENwOjxMd9W9SAN_7WY8eNjH3Kp_teOOs_Tui3MzgqIn9kSQj9kulVBPVIFDIm9nw2hyizfrfm98SRDWsR5B0X4zNNezRjlKcOtFm0N4zT_-WLxNQ-O0fLFr6YBSWJDpdkOVoqug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihgXlEu6WwGglmW88lkJTawGEPyYgmlrq7ZMNkpSPojfnU2WGJM3MElsU9dggxl36s6kyfAI1NX-SDgkhCPdzecAiicu0u84AU6Ov6DI2W39EhVbUkN9g-uYL3zTACiXrgnUGB_Mq3hsRlmS9uIUpZFj8tI7sBBN2u2CSomJV9E9LBLcEdHb-qLlsKMxUWN-j6ElT_bobX23oqsiRusNcperUi2ZW2CIKL6pMDoWrbpVUQbCd9zc4onUNahL6jkPHfTJ4YzkQT2de3m9DvthS3FZiVkVNoX9H41O0LyvPWlGLTpfI0X3VTnPEaO6aXZuQW_mDiHBK5Yr9bPblvxwqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL9bYXlG05OLhLaLrBaFAPk8-tkMmkXaM05vCzZW5-hShR-Y6mbQuc0ZLhLil5k60tp1Jyb3m25RHSfMpMTM948hyPpnbvo3EugxzDFsTxLqhw0CL-oeZ0qd6IsjucYiaSe2bf38hy3_m5pDojUq76jk23KzJiZfZvE-Ff47BWoNtHIXrEEEbHetYrFyTn61LVz_WZL-i7w-evez4RlE6wIBHgRsfwlt1J6t8BMiJBBqaoW5Dm-qcxM9YKqlecUhr7T8zDfLV2QYBWkD33BaDAYpICprsHedvUqrdOp8Bj429bq5Q0TvILrzANEhL35KWKcVZuHXXj5LrbDONfBthw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 947 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 824 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 892 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqVFr4li2i6h6--n-95JbdFzM57yQs1NjF00GmDNQe0CHz054FilJjb3UMxMz632yfJryenIFZAfs9ercBL1z2HWvoiv9cIEk0HHR99HV4CZiMPQBIyO-hapNlssD-_KB5WSQczFuow1k-DH6Zm_72CBqyy5dnPOxg1a-mviFuFNZFnVBsdjzKQx6YRgJsZZ4jRH4ea34I8uY_uiC2inJwQ70n28q_xYU8iEU6qB75GsJVJfoESMh3fpuJIQ8zY_-GfMQTJs2zvPWwDIklePOZuRTqv2Z0Ut7_Lch7c6Mr5bnYXhu_syKYM9uT_O04ZOpilpCsueM_WjZ7oc44HqCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 818 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 766 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqlUVZbLlkMpdDOZk0Mvls9rkVCMQxNE2AElUSplp0i1LB0wRtfce89fmShRWFGJoLwiluC5795YETeTMsxafkdI9W6SEBtcRUyo91CF6sjH1ZsI6KJGVoSpFmPKdppsdav91jI_FAo9Jm9XDL6emal1S6Ur6DdbDSic-eSIiHNd5YknY08ZuaFSwn90ac6ffX74laNtus7jBwsLPCS51gE_oQSN61Jy_cNMi_qIoRQpkTygSVwOI8hDu-Fki1XQGcrmnu2h2BzZCYdJnc__TIWe3YRK_7J_GhJhqgjtdcLPjNkxAQMWij3JNnegUo7oZLQ8r62d4UVQLDB3r0wL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 850 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTGQ_ZpGCbhFISExjY4H5w17MXTVfWHZJoyn3YiZzvlO5jv9eooTe9NTkAOdstruH_0GwdwwCHyPkquUt0__7xJkrtfGLJ7SKRCkeKeSWJrGVr_TD9IPLgoVMnqv2uFGCcszR1Bbw8lmiUO6VKkCE2eZj18cEvDIZmGaIwvzF4SJyT4mzolxnpNnERjsswr4XBpcvUmCeVFXtpFBbu03KyLV4Wf89krykLDkBzKjf44FV9hCVvz1Hq9Zt3F-pe00OvJ26RuUoRj6bH0UntRipUn7BR1y_oMd8s_U6TiqP-4l4EZoYMHCGhYsqtpddhynV0rw2fIxZo5fWYBxV5hdlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WiwCC--DcBzBZxH3IwYNX_ZL5jSczSJfS-_17DgNjTHhxzc9FbXc4BW6kIsS5n2qLPDJyUNDQ8ltOozdAnDwvHlfGzUo4HDnDmAmz5yMZVcB1QXtoTSLlWyA5blVMmIMOCHJFAuxv1sLsv0-55r16lETrwgijxw8-jEMCzUnTCVAnBJCiTc41LLowYbLizhhLMLhjjQD_rDYjYDWW2_H1J5LGngw1ww93GPYMY5LooolOvXC0bC9RF1P3YR7Zf_c1EI6Ue8QVz4z3I2aZx3emRR5JOE8ABu49DDYcWrYjkwHnJua8_JhbdJposOGJBdNcEYo7_6HlhVl3BQJNPl9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTywrJvKjf4I-zo4uJg9ufYIdhwa4K803TwAMVIkrHlnZgrZH1QrI3GE7W7c03N4TZdadacPCi2R_M7qASF1L8VFa3o6nBDDL-FWjqEaHvYaaBo6shvKG5eQlyc5riWpE-p33_FRDHbHs0G7uwq1Q1O0sYWzXsWb4j1G0W53wJyA1UmB2sB8-GsNB4tOa2ZZIHUxJGl6CA8XpNCbpvt-HI4pV8bZ6uksunAM2ot1vAZtd09SuBW7cQGtIgPhgBHaBhM96Ul01eY0gsAuOXfzhNM7aNYDpr9e5fEDqDcyOB612Uin70XJc09PF7HpPwOKh3vyzcSSZduNOA4gix9pfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qw_4s-FPCTjbMrfKczdhlZMsxamNfxGjMcC5OMfzcfhxZeoqiZ_NynS0xD-fheYC14zcFOYilPsgeWQrgLbdqa6KhxbgFwvsDWrgjDEdVR-uMw1Y3a6fdoj_kGQcov9gI-ywe4EcZuRgEsuCyQAuKxQbMoQuRYT03lgabFzUrF2rhDOZvsZISm3ocByaHJFbC9WWBFBeem_vQZk_63dQN-Qc0Ff0tcAeGWghEmjrrGTOjM7VYwD7nP91-h1L8K4ynrDHjR1m7FF8eoXPATMuxN1oEKzALfEmPqE8xsBXaTqTJii8n8JSF1nLa9vMLo8xSBzKDnZmh3jYu5MaCjAlRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxdVFvpaThQcdyAt9q9BlHA1Hw3eDgBTcVYqz_5OCBkz2uKQk3z7fBQhzKzHywzKp3J_v4mUEgTbdcjoDeH8P-u6cjypqEOe8FgaKLc3MElSe3AghQpqCtn1iWfYN5llFKhdEps8YAm-oRZtwiJ3lf1G-Ysy-CsSZbb-ZKtYA_O-Fktri5xhR7Zc0zjL2SgZcnCyRk7qkLU81fsGFl3DmNJgqdi4hQjU6spsM0-cMFlFZVx8X2qb2-ktIzYNghvrtsyAKS2gBacH0wOmmAGMv_1EKOxUla8e_uut0-7Y1QpH_HqMuC0mM9g7L4DCChDFP4cZU5w4rX9GCkrch7sI4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsPcOlcV7ewrL6HEhltvhRqeJRXWv6tAlphIfLL6lQO7nkV0Jd8UNx4pcKz48spn0k61xHIKAZtiUbMLKSDB5UI-dK9visSw6ugEEzIzdCdXGCvHXLmmnniufcsFgFwlbcrRSBNBaP5LWjN6pet5ZROZPk9NH6BXKNA4rD2-vEeXvdrVDe-LuFjH5sYUffCkltBOp6kketIRZwivDEKFCuRu9Grhm6x4ddiYjpVzPjLSy9dZ0LlhxCe79R4kHlvwCKA6Df1UKjFummhQ1BHYJOPp-SGKzEduaxN2ejXR7oTCSEMdzaUqupVrUt3L9_8w7jclXg_Dk5ksMHh9ghyGWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=ZKSofBu37GOuNB6OIZJudYFzAXWz8uDoI0jx-nM7J3KJcffQrvcA7qOYX8OwMCTmajmScIZjelY_v8lE3BWFE8q5RBh8lZLAQJcvO0eDwDIEgz8I8Dc8cCBqYp3rvfQl0qhCogt5zDLiOphlg4E6CQ4BemVM3pC3Kypq9K1d9V2NHJH_-DHKMcHhi7Ewe2oES5Ze_Lr0YzAoblvvlxjSsUZhYtQkOL6M-RQT25XC_HM-g362ttu-CrDzeHvJmPToFkdsfBcmPJRTTVP52HUlpJxZ1jbKudYPuLDCiM-_vdwMfFnu2sHSYS78f1MKssdDDforynHOMb_D6J57ngmaGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=ZKSofBu37GOuNB6OIZJudYFzAXWz8uDoI0jx-nM7J3KJcffQrvcA7qOYX8OwMCTmajmScIZjelY_v8lE3BWFE8q5RBh8lZLAQJcvO0eDwDIEgz8I8Dc8cCBqYp3rvfQl0qhCogt5zDLiOphlg4E6CQ4BemVM3pC3Kypq9K1d9V2NHJH_-DHKMcHhi7Ewe2oES5Ze_Lr0YzAoblvvlxjSsUZhYtQkOL6M-RQT25XC_HM-g362ttu-CrDzeHvJmPToFkdsfBcmPJRTTVP52HUlpJxZ1jbKudYPuLDCiM-_vdwMfFnu2sHSYS78f1MKssdDDforynHOMb_D6J57ngmaGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkxu-jOdIKAIbmq_1nN9fbGRTZk8pD_kS0-YDOB4OTcg8IUBbqsdlUM4TzZ7u1KxtKFfubsYFQA92QWBakwzeL8M2lnruzhqGioWuHKNiZOE29SJzLcpDz7e6L5BG1vnudH-m18cM3EPwBTvEI4Qb7Ukf1CuZYniT2Y9b2v9twbWea5xApAgf_3oQa7KpZIOjGC5dRfLn-RcdF-ChOvZCxE8nRbRG9fIu5qxaSIVhNXmFmtOJeAf8YFZae8j4gMZKk32VPe1Uv5ZxdA1fSWYFoC0deFIzRxUG30JWBpipth_k6wjUexGhpPmRi_SBkgZxIl5An_556wu7El_y9QSlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 929 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6xXIXZWBKa_FLeXZnfPdgYyHgQvceAfXdGIeIBgzYphl3TC3gU30tJ-MBknL69SHk7oiguFGb40bXuwDn-059baPFXvJ77k9OWMnJYhXBzCPLFk63taQRGmdQruAH8y5UU2tU2ia04N9oCmQVXc8bl2xEj1Q8VX7R8GsVxkuHIQW3vrlhwHPzTuyY-nST_uki4ALl9s7WxIrd56nf3JnaYsoRkVO0Yjucyzyh0C-KF8b20rl63v23sUUmpptVh58lKzG8Yv_tjGGQlxQsAxe12oNIZGAyKI8OB3o31jsPnWXOPYk4dSzkIPSAHqIbGMSSLjHZQMQVo0dCkNMzLJJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 778 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dy8GyKKsFyZE1UJXkJaa-YpQZFgzlaoKbPpROuljLVehi0BGoT8TGh_XljiVYn67qucxySU_7kpM1RTv_Y_5OCjajhQd6c4FemU7RDzHR49sN6JdLf66NVveyOQlBeywby6dJoMGl_PoN_xNTaH6pAUQpE22StCLrNRVVdgH3M0XsveKK8vahSJXYPpjYZ7zQqBARGHbxCFMaDwMSSmVgEzgT2IYsD0ZjjdE5G_gMEAbU1WsctdpsI7UDaiUjuCmz7s2OR06lTtFOCCveiaHo7ZC2RhikkT37y_E40_26D5dwKRWYavefGfQCx7FY6NaySET0QkuvLxYvrTwjr59-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1YmSF1sLy-dbJV_cD9E1vUT5FEfEUzeDolnPwmPwpbmkmaWCv9uNRkkpYk_ANKY2Ba-xBGSE_EA4zEMSMJ2BppD5cfrd19W5ZUobnOqcT5iI1FxTmRG9Uj3060Zc66G5EvLcizDe4iw-GcpXaP5EuZ9IXf_Zo1CFQY-IDyDIs_G_3wk-MsjgFyfdwmrvEVmN7zKWtVtA5opRySY70ih3FT2Pe4k6cap2S2Pf8Um3Tct-V71ANJBvmF8mTn_0-KDI4cTMQcHymIdvjNvfISWcLv_N9eIbrIF41HwlwJuQHm15fcyIygsHIGuoQeptONJglQKRxQDqS7i1H5o1I72ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 799 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 986 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khOiQBqLDlG4qwei-VNJHqp-0Za_K4vpYlg-J0r1excX5b4uaU66XcglGVpi-VRQg7AJNmz7KtZp1srKcKvv2HsRZ3rtQIjONoO8pZNLQ1mR-PpNXN4GnjGSla-APaj5AfKduTAaA2LuHaY9wW1hu39DFM3NdHgkW02AneFUCffyadCGHLbwlrv0ZwpF-JZ1PSxljwr_qHEWXY9jk-7-P9mIyTH5PHbZgncXppTcMZp6NuQ9jRvSqSDXmG6Q0rYEREufS52tMgxBYjrBx8pxknqOiD4Y6obS7h_pPbjF-l1XLYwpYHbf5XsJ6zIjgUlLWnz0BsKYNoEit1_SBRUA_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 921 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDzBgRHlqgc_tvyUB8SGJIQRZPiLqVmqDP3nfg0BP5vMvD2c5DP6o0oaMpE-b5J1Aw6XAOhHDOcc4eMO3yXMpDcsBALUtq0IZa-6k_rmtaaFRvx6g98j7Kqg8cz2ZdDHmDXBO_yVAEhRx46nUg8J-ZhMyYYUWSkWCUdTxv7dT8LDNDjxU8Sq2lX2M2bVMa2KKwJfIZmZcrRxU8AJVs5BOpf6vLXd30Nw72llPeETrjaD_4Hqm2_cGHFbi1Fg-4tPpVOkBScFv6LXP22OWrSl3E2tzDgA2Fz_gHlJol873H5_lsScyak9mIJ9nWK5cwyKlephkFBGtfyMeR3Z4zjEwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 743 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_Z7FxU5RzoeOls8cXj7aksvgCZa7ghPHrKuukI4OQmyPvg5ipNoYTS8zIFjjwHCLGBymAirN7Cq40HW37tpnCDQXnIxApl9EbkVV9x_8a8ylGDzb-tA3-Wmb_6zqy_ZOUnM8hUdmbGXFMLMooNReURmancgl01JZleAkEfJi2htDG_p4S9TxfSUKWySgBncz0-ZUzJieTlRzL0fnC-jpbckMogmFNQvq6gGcQC3f5lOIvsxSReZk2ifYY3GjxS5-BnqRSM218UcqSROAZ1Gc5ENYsUe3MTTYo0ygyLN4WViLGYGFrunROlxmbrVrsmYBtYHCKvcriZnMmOE-CJ1AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UjeoPpkAM_0TT7gGOfqgGb3Jc_dGKCIuXDA4_tSW1p-yp4LHemeJMZG9QRNboD-L_KyC5i4ae-cat178wYIZG6fP66mrxXRpOMbbuZcv4TK3erby8OtaIPlA5O6VRQr0TlvZ1RSPDQHp5NkKrdHhqrxiZ8P7bFNLP7p0erEPd59RxeVI56qTFf1qmUi36DWrGcJapDEso6u-Ud9yWhENR6P3Yj_AyjAElBsRCUC9EJPw2gpohorA-HOHE2d1_8niAjNCBGD7_T44F9hFvFwGFRFOiMtEtAOETIFcLudoupy_EZOOgKTyueobWe8T-0wqjrBUd87UHMy22dSPIvfkTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 753 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVJM4vmOigvT2Xfw1ny5B9I81S06sTOZM1D4YTQSYtdQHQ3665UxgnyqJ6bn411GujHVTHT2HsHsbVf2oEgrUS2D4geq6a2SlrGLON66nTCoJXqKWZk45kxiyrTCq43ZkPMabSksY9U_ZVDu8ykUuOzOqvCYom2wyIV6MtGLImyYqRb1OJAI9T9_AdyCUkGAOiReS50HjD3q2TFYo4JtWx98d9cZnf-9CPsw_yo1AbaKbjgKPKVG70LtSGqWzf34QMpHGLVeEvpUrZyIT0tggpa-j6rBdjhdqs4Ga53mLPmzt1cqoxMfGrNkGaM3KUmeBy1LaHy2Y_LrtKyx-l3i7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 665 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 810 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 819 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 720 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP3OUBypgc5HV_ZE5IHLImAYmqAQ0DsJGt-5WDZtJLPTLqPkfN-VDPBjsTA_vcosbO6ug36yFNpgcjiYftV3DbO_4GCHtmE7s76lCfkFMF64z0wRwAOThN5r9eymSw1eoxJ7-DeeBobO_wg2aLY0v9eJPkK_lby0PKtXlsIVfXlPYsVAuZnvPKaKy8YA22YILHm32CAQVoo9_aO5C1bqoC8nPSmalkWBatMS2198IZ-9s1qyRSoTIu4sO0r9SJjuz_vHU3tplI2rrecihnsEXfE2ZS8vFBhfHGjpdCknk9P83h8aATfVPVyHbE3qyd5WDBwVPmV1KlM8uSlWzSUBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuO_-NXikvZ4leoY1Xe0HCzf5MlEzCA8mtM6FbxrSFk5D4kSEa9Gu9XiZyKEdhGNhaW7kp07ETPhuYOxDnUc10x-yhCi-MHqoi_GbzvbssLBolqvJnxtBbSKAhCXMFNWS2gCIuRxBwq9-iPPFLKjCUggcwKsYsfczLH5ZqiL3aPdOfjiON6EQb2a8JdOuW4ACCSe_eSb2_ho94QnBSCv8MvG6ASXb_IZYRDalMU3lXBL80KuKoJHDTpPeIhpmOxglTM8FdawIk94QaqT5VGP-3t96remBKSvxc7vfQi7Npyv4-nAv9AEZUR8iemvpxUw0QwZ3vdPxi0o8O8BdrNQeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 603 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJ3j5psVWWHrurie6FS6uQ1yqKULDdvfj8xSSCSzJBQYqpBw_u8xvbHUADGtNqIVb7V84_jrRvqPOcA3GU-sXns1PzueOEdGUkJPVhKGLIj91pLelHb1jCfjs5_9oRmhhaECVQLzRkxqdIBiQ8VIXWP4K-9mDJF3f5JTXqi6ti3DfH-99VleaCptvJKDasQ-f_DcLANPa2gWW2D7YqL8OPzrkep270c4nFQCDP87f05zGCS61Ld9AD9MuydFHG7Vnu0paOIURpEsCoZxhp5yNuFe-UKeaznGfpkZ4erlmNVKCWIJMAsZbV1ZaWxJwgXIPeypb4dJcT_WhjKmVRcs6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 695 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvUzE_jHvo8KL7VegG4eA0Yq-62o8oIDy_Yl5TluQjPGwv656U4YB7GtYJvNcYJLtD3jhtopY3DTa0kAW_fNe3d_-SDR1Uh8bQXoAE6ykuBfKe2aZcq459N_IXm3tKk3KOtTApPQjZouGVxFKjozWjxA2R-su1A1Jd60580GnQDdzqtWzKk6wm_L3cOxmMzFtVqddAg7Brp6qEa42Ge1ctyZQfhstgHIbWdZAvK2zolFY2Tft3-Ejd1hRSHDkivDWQHYHGsZTu_Mufl_3lp0lXetK7U38pdVeqY78NOfGHeIQsSE0i9Ikv3WIFcNTwyK_5PiGawGWjAy7C73DOXSyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKHt_DqZSm6o3j8sz0kiMSq2nmzaVqoZjuSMulqwoXPbGWE9zuqnb94ToLe4bOVzVOCzip5s85pkWuttTNqlN1XeZOxI_nPjMiQuRcS5q-8ArGsLLICnT256LBC6KKEEyxDaYuCXaP1RaM_EM5CeojnVJSp9bhsgqXkH1OKW6wGFx_8cUBgjYjTzkhbeZZyxBa_NosUefIuJxAEeJ6rRX0jF0LzLnRBp7xDIZ7VnA5k6qnfOu6y49JK0iTngNGP0Hc_daOsougvmqnk8m3VMlsaz9vc0JtWPTrafvM7MbV2lG1LsbTQ_-alOtbBRsFVKwpCW4MWeUYqX3O3Az5AD_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGORA445tedPuVNU1xxKzSAGKYHRrWXDG8ASW3Adwr2NDLMu9rjTVPWmaILmbcnchvvmPIdgrckltUSucN8abPU-pZhHEPuDvrSbnolb_ynUQybryjTBVqmB1THe8yi7Skow6zPfIxTFzXaSBXaNkJxDRRhWYbzthMgBFm_kXgJ2h-n2kohkfqD_V8x0_eyluy4piXmUOy7OcLelkLOA6w5dmgCBUwNa03_LSozQqLmZdpFP17mIxEOx3nia3UxTbS_NV16_X3L0XBtliGq4pBrCy7PqGNABea9bNkHFcX5OLzsG_pXLRiE3HslQ_oEPCypVNg_zNfSbrnp0N1RMbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bn1AKwKTr1YE7sixgVRHHHvetO8PQ1JOJlKZxTpdzAXg4kvCoUk3lM9CwGy2S-RFeG9C_VeyoiK7Y8VpEE7xkbs3hMO26f2kvGBNmzi9yoa0u9sJtlliRTpcYrO9zqmngHemo6FXYBfiyYCYZXm4KHaila3yy4fZJG78QGWvte16S0lcqhPU4IPAlwXfQI2EcS5YKxL4MvuUuQY3wE6XgUcUAaIYXjnAuJuNNGQAcHbAkDvIOQjVn1GCWdT17TEx2wWSXIUGdnjrh6c52v5_RCo0rjzMNm7JVw0ZQFUaETzCz7Fmoq9DOfsTEKKNOc1kAwhYg7jf6n3bki5piniy3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PcAYjK2UpID9yxfSkLADtYzZ_fKvvuVGgESd2WgYK2eTtq8Y_qbIhx69QsU7If4e3fXV_0JDF1XBFYieMmc7ZJnNmA4WLkb9vKtEkTF7Uq31hmFY0hQ0PkpgxmvSmXjqaBlbPwu-lmph0pZpQ7pnwIdC4woMA5S2xI0CPcMQPP-kwwZi-98AZCa2nmGZpqAumMMOnMFCzrGQ-gptr6YreRXg1vwwH9c-D4ji-SZDLOUbiVp60GEL6nXNw3m_RD5RpHR2d0nw8b-C0fSr83rJB0PyAly0sFUR-glxiN_VLux9lrJRgjybe3WQN9Mbe4D4DKtJwbLx6BthYHE5xQm6ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7lEwrONluFvT2hSlNaiYeplIDuLXeUtzE2zG8uqoOWkBhyy_mXfeu6IxQI7_otzljhldSheaE7V2vHjMw5FOKJ_xldyDo_VZu2RMbXutWKSz_vv9A_PbBENgSTBEO5QG3cG8FpO5prsCPT-0PhYGJppdrOXoR1wMnSCz9ZBBjli_7G885b5BcAC8vFGGwSfuLcPLbwPDGvDWomqPSlyUvYVwLQWJkQCyp1JQGoKuX-_TmjPjBW1rqbjiTc9V44Zbu3QppsnCjbFt7DrcobADkt7Bn5O4vpXqYsmrhN-2caJLZBhX7JrEixleiJvMEj8PXz94xJYXRtSmp5qG6hiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 579 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEoOkqeyHAuwGTQnH3A9lh_ayPiXtciB_xjBrIpqQgakUeq3kL6APrF_WxUu6xJ1q_ncsSfuab32Je9HGo8FC1rfL6d1NRL8Y3tAl2QIn3XDXbAAs9l5LvqMXBygSnLK2_GeUVH2DqklTKYFIQlqWEY3b17lWBXgpSh9jkqqbhjp2lqkCeusyQn9eFiMCLXLDjTvWG89QbHNuWwuasvJlSLi8nqDsVAZhoS3748tasVD6KQfYKVT_n-fkto5Ep1qxLwzlsRPxzcFa352weoduhy32rDpoOIoWb14jpumJneQUSNe6GbN52cn8JzJZP1W0bbUBS0akxNAQWbRy7VUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 591 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_BfttS_YA3UL66VSidiMXnEM1gDXczSk_ZuO-alZaw83cOuxMTRfIkqw9N1OKLayto9O43jNkSWWH5tQ8u4mYc3vVUov20F9hcX_GbwZrqGYC4mbfwNEmNtiKK05kzLjDMvcKJZFJVF8wyKGfuPN7JeE4YngAB5SWegOP6xk3TtBnUU384BPLOU1NQpELDgw1l3Opg40b30XOLC_AYzZodV_wPHYzH8Vv-vSJrljvoZ3GsJ_VCSACsqtIzkJxCxTKdNkBXo-6EFI8ElmZ2WKN2TtU9Tuy7aI3rJbHrBNAPcKvl8ZIKmameVhQAu2Fgud2RqD1U737ycHIGAAm1Ihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 700 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpEfQgH5KrAGqiuHcaMKP-kCPkVcPZBgoymiEUosCdYUFdcNCHaypylQ-RTh9mAYrfeKYAc9Rk41Ew5uXvtF1WB1gr2a0_whAeDKDroAbWFsnJBlx8hwyb_WS7AHvTDA-ZD2Fd18e1PqmQIsEhNSsnuTEdvqKn9YsopOeVk0stXYsUFa_54aiU8vE77yoBimNDF0l_8lfxLVdUK0zkmDUS8iq2ekfvO8dCHHxJS226B67dp_SrZVpJXFlLOCcYTpQ5ppIcio9474VtiP3CvkCSoCZ-GXTpLXlbzhiRQr87-iX9ppK6rurMH8VY_sl7-C6uj9XYPvBQ9hzyrej63LXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 645 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTtsY42daD5flq9idUafUcVkEZnHgKpkILqCUiS2Wq_8xkluxA5RIiwNb7VzKNkErn2D5Ui0TAxhLasGtyEoL3-0UQ-0KdX-VpXgmiANokanctwUE2bjaMtlVaCACe8pUunMfG-Uh3RnFIEqAFXJeG0U3KPjs3b6Kn1XGGh9BLBRdFaol3qx7agF4m4mxUtvSsqoBAwtvNNbNSTxF__5Pzr-8FXrfaZnWl32mFJGPbBn11HbQo5c_7-TG0CtCEoYgleDVQAHXJyX0mKASo4gX843NB4lLzfFBMFXhFfBI393ru3yy7WPNqVFiQiJT00ie6i2hpPDcj3lm1O1YOnOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 713 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFvzV3Mu5-C2Q55N4yx-d5QLxeZBLFWEfo6rugetPsjVJ7k6xcU_V884EYHKZzxJcTWgHac8ICXX5H7DDjEqLrEXib8S70GCQwjzO7ILs1tOB4oVDeKV739zEN1AQtRrrN3aKFbK2mw99ni9dMKQ9SYiPdbXJqQ81gGjIGcQ3jXdOCS1pIRnWYlNgtKwyaTbwloUau2XkqsCq-sMbYuHo8AvTMMt1CriSLhAalQRCWMS5bsZxb3kZJHhRbMaPD__QlcdHtNQKqZ7kOq_SYtERvWbAgVyS_qcM3Sd19Uj_826y7vthNTU_0SibqRhNdWkAHvnCN_FfFY8vyhzPaNcpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_4Qb6MM7wFN4lFDR0RJhKMWXckfzfWgr3wheFuSPfMTv5boJB2tJqjbPEOXy6koVu3uPcXseYjb2B2w-r2atjzoaKntgofnC1leVf4rltQPWCHYHHIkYwUnTROG8vRY3tMZjzq47xO-jz5Sp3fFkWdBhWwuq-dnSaZWxsMLQEc13QkptLS7y1HAyUpOZDAmb5aOkimJH_Se6UGm8TtBOFcsiQSBaqgLdxhDGfQ9nWiKjQ5XB7j00Vkxp0rvG7asCgyUzl6bMiUIccnLugTId3aVrwVJ13VN_VZVgLMpdl5hVhROg1GbUFAfZs7ufgEVr546NaLR0TeFd0muzspthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfvBgaBvSQQ4wFuLmWBwADXaTEzhM5p6SOCq28k3aU_xSyuuo8t7wdXmjSEAXSZnz58sxhe-2zLuU-cSTK9okkXakvgs5WT3d_EUFrPJFpoq6YPW3sz2WhjsQ7_ruf33PS09QKK1rPZ-7EF14m2HbsK9fdAgYEnoHYW4dpQHPpIlvPhM0d1C9b2AcmnCf3N6LHFdvnDAfVosnnCfXr17L3_5vNwIxt5aF3n1wvWuXomOVtmXhpwm4hFb4EDj2ZeEJpgYPQAkHbwUUpD0l3GyhfWz-OyQO3WG_067ky7x8JtW9_fK6y_N_8GkhsX4XG7t6dkMZeMd2UuCRO7z3o6Hdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUXC0yU7zoJZoKI0-OiYF4Wvqr41r_vfqpHUAKAriX3gqWcEIooYfKBTpzVl6EYp948YG6IQMfVNCj170-RICYPvdBuSNVXDCIB_vtyAdexe19yNrsXdLlb9qcFBjM7bYAtDZlpkA60enBU1XemtdkSZdNuCVQVwIHncaGv94zKy5DLXIh0lwHtX_TsPTg-5sB7ZdHou-MMFfaIlDUTqA3-pQK6dC7lz7f80k5lVwGIkzVHFxtp6yZ20yCQudHsCTpvvPrUgOzyxgqpSOaQ_myewLSZQ6LzkuqTw5-Pded_q3ge2luhJi_cKZiJ1gbzOiP4OzALFxKnCTcQ_K29xuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZsJZwbtIqBPVJiF2zNCb5EfOHNMd9WkO6nk5Hxp4Mu2uCa5uLjQ6T9GhqEJVfUMrgl4ojvynTr1ZiMaOuYfZy9VR-qh15N8xsBA05qOc-Cp6o_2c2-AB442e77Fzw4epX4a3Nw-ci9LJzQToG7q8LPIw5uzUkwb1c7hKej98MUbTmzCOUgDo7ZBJhCwdmCMhTZdjqda1ZyY7aEd13S6Ik3mr6B1Rp57xMP3bInvwmoV0fftSbaBZG8YzbIMda82SGvcE01rTop8yQkXPFr9J2wTsgnXWCcWj3CBPEGOFTKO5x-eSp7yPfIjxW9mA4DKscAchpY8kEJXcUBZtOUEMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 544 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0rbPFj-EsiuUBYlYoeLUuDqdO_Rn_jYrlJkc3SxfgLazu8tAqDhOI8QoN8YCd8_BXSGgCSl3nlJbOerbCEXEbiHEu-Oxmu5imaGv0zvpL3h_uk0YrgIdmVCTT--i92ioI6-i8apQvbPwiBDtFgVXqEUkUR2AGlY3eB8RL8C-0o_ntoapdX73ONMpLR9YYfGT0q3bBHwdLoBtJNfhHp7WpkXdQt9nOfBFz3ITC5F5LSfTnqThU73OpnnPDW54GPYIKRefq8SY6oe0xvLCntTCBLXVNFUw4dAGw-aF4D_vyXhkjAZ3cws9ul_NPGk0yvLQCjkhxw0r0w3yz7cLslC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 543 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhQwBc9LgLwPW5tMKMJP_f6IPE1O7ottpvJ6cvF_7UIU_VLfJczREqK-cDjW84CKdxN3pH45jiWYb8V8ub0zUkUkxBmHoTRLQqaBYyU26IyMPSm2WalLaiKm9vW3Emhi_L-8o779bw0QZoA3CL0aAi0CivJTx5aIrU6Xto59yoOX6A9Qe9QksFRHswFI8E_Ix_0yyaq8KUT2DuVaXqhAVeZhtomTq8VpQoPDBD71nPp771lI0NtuiFSYr9uxv7rR-ydyHutC_GMGCvvNd4V_bxh3fBmuXk16puYe6S1s5UJqfLrjs2QoUvgFSojK0JGEkCRSjHnzSo5qZ_laU5Ca-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxyCQe2v3glwKLrhJIhhEj2eeb_GymBfP6YBEx9UG3IiUNayCPyY7K5MFml0M87BdqlLJAoYMMGTYjoDhJTucEdkJ2CqyX9m9d4IHaWW9-3s2odFx8ZQ5yzAZgaF_Uq0cTwke4_-YqHIgh8EXijsoUzARJq6INCJJ7NmAdlOitPKf1PthpASOWE3V0qYrd-bbcnEaxb7zcIXo3DfrItF2RdbjDn9imAUbgIfHHQDaeHLuVR5eKLEahO7h1m7KnKTd-VLMSIi1_JaQbUBr3Yn5zwdqxqAMqCJhaqdmWUJknX8mmcVKK2ES-VtXGp6cEyt63cOliBNA-_rgicD-j4tuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfxcz0hJW-_WDhmcMTLDBSMApbnsx8-Yuv1gnOStbgIRRMOFT8Dcis7fS6vSvsoLfNnR22Qf3eDwLFAjWi0Lit_Sckn4n6DKmAwyJCF7clU3DLddz3FlXxeF7xl3rihHQ8g2O_wddfwkbTX1hqPDz54A1frg3DS0B0sG7aZgHF5DTIOaGBWaKow37AOgFKbAk8uBFvhbowo_-nGcOqj04p-80Z-v2ay0zIwutqu6bh6G4T_r0_8hM2oNPse5xoMWJ4Sh_ZH43TYR_FqxzUX5adTnTEpGI40RNYxceOAiRmke6GX-0lzjiG9GRJ0Bx_5Gxw7lGGbHf5R4KS059bhF8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dU2EzTgPmomIclQolo4i1-Ur--5JMGMo9YTa49nnZg7-QnrO0wFwQTNGi__-RqFz4MKEL3oC4QFjcEvcZ16g5JwcvuesRPRb1CNDPKZlSIKCjWnZouEZMkstye_4W1TK2xC9nO7nHmGyQy6JOSOm1BHioCawE60UbywyFnKOC6ZgHpD5Ox5mYywFeggzE1Ld5hBKxRiBUq8cBQa5Z58bwyMtr1r1-NVq-hdFE_43FceJqK0bcF0N3kOv3Gc8dIaBvGOTmkU90k10c9qhCG7at07NpoYVog695EDqoP3jzNVIY-PFWcrb1kEPuyZCnQDwcYFCtqQUuf4w3Rzdyg3yWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4-n79zIriXhjm4sNWovx0YYkUv5a7VN7MiAoBOIvGR2GhzBhDxxIeiQrfkLyXgcOTksq3f8qP7JxNcwN6-J61vVdKTo5ExvzNxK159zkcwmlvJwGMXWTmuhwLqQk6XTaPqpGhjwd6eSvU2HMubCAo6jj2gUa6W1Um8tkLTM1eh4mW1HNel9YrjJXffhPOFCqjg2gZuLwia4kcHz7ycaRLJu6wWrOGq9bvBwJTJkaWftU9nE4sBLSCHQEr9o0bUTcCr1S4HN8Ca31UFUV8k_Lsb58T-25SicJhUYLIaCF0ouIK8jmjHUn1jyS3R4nU3WEEO6UUXz3vNRRHOCdpfi3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IRoJBbKjzZdsL-B9uTzlHCzQ4MzHtiLVb8My_9mawppP7EXVYx3xzhXMf5Tdnnw_hbwv1gFs-fj1ADk-X_gnR5ZVrVFd9qARKCOUHT8jnb_byXarR6NosSgGwLO6MWXGIxyrG38gz_lX77ociDJkilFkg0M8n-fjLQqkLq0Ukk-bo1yD15dqeLwdfa8tPmSU_2t6WOjYUajwU3Uelus_3rQ9tnNxl881H2e7qpKDpT2vOoRQvySmwmGqCiU7oCjkd5QuWgK9rE3yB5FzFgDsoCiz8JbaTDgNxUUWxeXOW5IbFRKLZCsCylq8IZ-cq_UHhzhKUJtI727jIZKB2cifuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 803 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIk3-2D7MYbF-HABNESmQUU3OaI83e-MPuKHigYRDs0vSz0U6UaFTEP3GnOt8mjDYUy50pe-SpXCaVtUNd6VSWorKOeN0TBkkjlLBaDOCjsbSxKuEHxxsfipeu2VzvBwPEGw892yk9A-hy9ICCFAmU88tKMXDIKXa_fVmMcGHOKx4NKY9jErR9Wt_O8CoZ_08jq4YNbEkUHYKErQtLMYSDdnvwfqOk1z0Bbu9IBILus59KSn1GQTE1MQhrelsUCWUdgQkq1vag6LFEB-oXfKkbJzkSr2QIFOKFt0rV3k8g7Hu2RkMSBZo4gxMUYGiap4wCCB9R-NNk_2e0r7pTAOfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZfZ8VxvgMKARJ6yDPqbOowGXC7g6NBOP1UOfrEyina05sWp64jk7oQXVUfRa26A4aWRNo2YvDhsBHGDdV2Kb3qlUVAN_eCnKjzQWhjGP1nmlUcG2JXlJhjk3bA_S_7st6sclDbf5-DCVrBq7roBxz7BGkMsUiMRoO6cPlbsXEzgOj6ri2hP01ZLRzzj54BcWnoRdGdsfNryVi6XSSDZimoT_RHdhi7k4VweacIVorp0zZUPpv4OyF7OY6v1147M8ZkWiBb5VRB6Uw-kE-xtfJ_F5nhtct7-LNheqRY5mGU179P6IaE8F9eFLkaxni6_6wnmvI1lZblZTCw6tTGVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2Ns5KPSq3lNnF-SIrz-mhE3GcMIQPFVsADKp5HMRyNCwz7gXdu6iny-_N5dfuoq7uqkho-PkQed0Cr6ncwfl3OXRXSp1lYJd0Wjh48eUyF9BnFU-PIv43u3GrFj7iNz5Ybfi-COpAGvjSYYxYBgemNOxJ2YEs_DI5syT3Njq6LZd-zINFdx1fUBTfYiYvPr6pJldNwcqLg1jpV2oYz1hJlo75SYBBQMr2LSVNv2QkIuHKdGl3gCAfzItZSWjHg7JRdFL44PcVvjgfdTGsmK2e2Iqg_HywSrM5jJ9TlWXR6hY3SaP7eY53TaKYOtwRqQoTPeU05ZNKV1qnWBB40A4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUmREcEGmht9YL-efYsKJqCAu4W5lb6YNDlVp-plA_-tx097zej7gZJZu1Xz9yrUhuUQDxo0acvoLeo4qtDTn5UqVYyBun3f2cohz7mTLq0NL-bXW4AFtdq_Q8_WzvxWR7X6qCzQhSluH04hg1VdwJEdfSCHI67ekdMZbnSMTUgdBrJVG73Kjc5xIGIR-3OaO85ee2dqsYryKuO3fqddVwMORRXmKkGDt6IDQZ1cJ7X5ha-RoaJey5i6huN1Kx9AWifLqmcl3-c5-oqzYeA0OrLejr6_ehdboY5IJePbXOPTiFOIWZL0ZlPg1xI428n31BKjjHB--esHelXrnfFvGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 716 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIgluXjMIDLfbQX9Dh3-j81ZBX-iHUa0I23QySvmERPTO81GTxnqM5VxyVUILPRqqusPSxbDdOCwvubDUudT_MYeXprT3zcFlWQcnso3EyXi-5a-rSDtWLvF6VmE-cxBeedxB_iBCQnGWlf7FA1fJyXEML1_D-KN53P4jzXjaE78qZ61uM6AczAZEOAXEzo4fnNGXzEBE1BlfBn7gqpjJNJ5WBOfXjeizF6VjdPHt3U8VylPH-DD787B0f8lqMtutLk4DRCLsfiB8kXJu4z_IYGPMxvPz4GFNVO40xa9MRzJ96M7mtBpzjOt9cye8vSOhcagkmpYGokjfQmdYIOmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7Q2o20CAR6GYR8OtWqzvOLOw33dxMGz78vFVaEJzRrYoCxjM5SCLB7LwxyqsCWR_Dr1wiWxJG5rRrzwtyvag0mNPwpiEHvxkXNnfsv9eu7jdh5xnxRlwQv9wSRAaEHndYm2sxSdEIcIO6GaUYAeIsFjqqINYWr1RJ6CGPRFwfkj7_8iSilIFDG5AHbsRm0zw282TJOIo3Fqk6cazS1UbOlbk0ZdHY3ae_hk-mxi0b6TQn6M8sTB02AirzGlRB2vvkyOxaF8rtJtCHx73ye-mXTqLivDZKtsS5K2f7-v3HYTVJzjXzhlVsB77ncJvyy28MHerQZfmrhxojhwTnf0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 769 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ig2TDSMlg1RWmDJA4DQOI00reuMSMjNkn_Kkhp4mrl2WELrXmwN0U3OLNzpjlLcaiES4WEbA_dGZt9jbUbN3jCFC1ZRxwE7WhPqyrIMryIVOVO_F_sC1E_gxvRCJZa9WWiCmNHTvdbaytMAyCkE3fMxt1ZgG_NGo4yxcRALlrx018hrDCBe_X6lDlzkJ7bvRxUATEezq1EpYtYvSHVX60j9XJwLqjaA-t7-6I4HxHXPRcy9Prq9sMjn4a5lHOZRP2hzttO_2DfEIQ4nD5wu8N6XT-gUKT-_TK3RZfLQxNxyLjdONMAYWLgzD2AcHRuWEv-e8SH3Weo9Bv5vGE_VtYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2aOsyLmwAZltaArNfREmG3Q-LqXs00Cxr5vCG1oy-Y_5idrl-ZHuCRuE0-4qaJoQRo_Yfc-732hfm6gBWPQY-VQANVmgeQPTWCsJeFUkXdxNUWwy0ugwv3k-dd8hTZkAkfU_iOp2Fk-_JGmmWFYvFCpXfODtZdq6O142YfTguwuLX92GlJ58VMUmr5zL1BuWRS69I6YFbYIa3I12hKa4rJ0diLUbG2Qoa_0JNDH9fmgJdUO3WgCiCRQgiKEQoTmwBBs_4z-B5zWLvkYmFByt79QtNr46K6VZy5cOIP7lKaCWM0MHCdAxmWSv3zd8IWBpQ16y8bEkG-suEdtuqLUZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1aUfNj5AJ5B7kK7eddWXuEw0UJkSN1sR9YqMc90Lcl54D8DP2qy91ydiIsKor04XdgjdloOSuiTY5OfSAAoZL07vVRmkflt-0jOvhbAy-RvHIGYK_EYtP2ziluRQ7tO50O2-zaPciOoeSCklnBT3F0WoKnPYQgza9oP9jfa0bCToFIUewIJR8OP6pLc_6NOWdwG9sXXFO3Ol-Tp8zukAOH-DPNreo_gyF6TX6ypAwt-RPPSHR3A8ChA_rHxx7rYQR6pC47gN7P_GDO_Rk4P2vfs_HftxAn8_0C7kA7bw0Chx8GrvJC7ZF8suiht5q-qRHus82YN3QbsGYETZ5bOsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFkDsiIoFl10tX9TMpfjpNYqIHmkcQAV8TwvLYE3kvdzmqNT2Ow0Hu3Cb7GSNGiWPNywXUccNI9ly7BWrWVW9sb7iPb7eTOTMc-73n71pnyObbK7hABWa8Ab1VFmoM8WYgsPSNHcAlkw0Sq32Mz891t4ZkvwYtnxd9FbYyA8-Fn7hR1QO2Tq6C9k9LClHhSgNuxc4VEyYvoKELLJBQGJeNeuwIjfQ1pEnM8ixs_zoVUGkM_IvExs5DSUVU_WfwDX9GUq2NjgH94CfnaMxC-qZ0EX_jfPN3eIDrSRqrHMjUtnLMue0apSn6RkqcRe_6YreK6Xh3VuUK4uRUr_koCQhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukPmms0JPNdSU3Y9e9uYuXwIP5EPv1ZXlWYiFwmgOhAT4ejRmkFvf4tpUeygLlhAZIDofho-UlhiOmCZ1onLFoITonGFNNv598zigCpy3uAnzORswCw5bPX--y0Ba1ePvjZV46XDDG_sMnoWSTDQPmXhxQiRIUoqiZ9dlnxXFoUNIj-VXp_GaENSVMG04jqz9xs7NMA2W8ug1oHrEJJ25pnuc1vpp5ItHmDDxTe5AGYdbXbjGxnoGVr3G_USvwi1yJFhAAShiUEEYdULDhtrTdcC7v_Cg9W7ktM3BKiTizJeoVNqECpghOqQHwUpPNJx6VvMISyuoe_jHkGYUJneAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3MVk9Newq6w2uM8a7MexwDywCy8rtLZMbfViaoM-BFkqGueo02Lsm3NwLp8I_FVATXlTkHvGyxAY-n-Seyz_LGjJPe6ZM7gnAfQzOmMkBZ-NUAy9-3_E5xYpTYgvtNmkowNYRujsnzYJxbFnLcAsv-tAboG-ClbQPjicSpINldxmRrvvnguwbCXA8wn6Zmx-b-tSkloh7pORPsq0jUZlK0VzBAAk_9_sgM2hVODEyobuCkwaLP66SFSpSc_b7GYk-EdSzHHav0xLBdaQbukYK6sc0EKG8gzF499dX6R0bKpVZf0OWtHN33kAiVeDR26XH4pGSwL--9Zol2brBVM9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 701 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=hFmFWtM-Lmo7RtT0kCn7nbjnDUoELVp_OOR_NHFw0Zv_A-V5nF9HzlCOb7F0gW16kegy6R_nxrXzLSIxc0SawyCR6ln94S4Be-i3I_FLVvlA9BWMBYYLxCfaLpf1jW7pT9t6XyqSFn9LA0RJl8mDkj7hRu7N5hvJQ5roTdxFUrT3_aE31QFHJQRtnbYdzYvy2rQP_fG66DPxXIY8G0iZpe99EvAQvKGqzz3DDgc8BMbn3Gk5N3SBRT1G0xc5I9jf6Rz782366a5ceF5z2UD1WQoYthAfcyKiDkDa0Fq8YE9KoUIGOCgWLiPRnTLWW1AiE5Cpz_mLxLPqd8HApLhmbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=hFmFWtM-Lmo7RtT0kCn7nbjnDUoELVp_OOR_NHFw0Zv_A-V5nF9HzlCOb7F0gW16kegy6R_nxrXzLSIxc0SawyCR6ln94S4Be-i3I_FLVvlA9BWMBYYLxCfaLpf1jW7pT9t6XyqSFn9LA0RJl8mDkj7hRu7N5hvJQ5roTdxFUrT3_aE31QFHJQRtnbYdzYvy2rQP_fG66DPxXIY8G0iZpe99EvAQvKGqzz3DDgc8BMbn3Gk5N3SBRT1G0xc5I9jf6Rz782366a5ceF5z2UD1WQoYthAfcyKiDkDa0Fq8YE9KoUIGOCgWLiPRnTLWW1AiE5Cpz_mLxLPqd8HApLhmbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDx45OeUtGi_YY-P2PxHQw2S_4MhSUx5o_0KIUHd27tai_dhzGMX_oA_NQyno-TCIRfHlMBx9ZoxjvZhz_4Mp9WoR4WP3s7e7vd5LOKUgOA0zjeU4yT4LqcrYM8mWU0Rc4l8Ba3oospcPL26HRLAgmOFKBEiVvB6g3FBOdbOdpc2IjFGTf798x1LUBSbGKuL5TmvQggUD6Q3JbYPgd8TiWIX3_ipxTLiQdrEIr4n0wtRiLXRrtNRENqAcIG3syo-5aenD3FTms8ysXRlpApRR85FftmAkqykHU1R-4idg2jedy9D7ZregJKCJuFOS-0vd6Mzc-ybYt0Qzl3Dz0FmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCWUqWgElN2Ty6AHkeaFohgh7iLNjewB7KHtlO6MA-0y9FpueVIQOmJe-_qgJUdfvA1mCVXCk3ylaTTiq1YLBIvT4kuoqRbFDeG52fkwbkkiE4NUtO7YprnqB4rCSGyNSncwQOCjElHThDUPuMbHEEKmmR-YeQFk0TX9kEbhRYFI_d87d-LN-7iT5R5hbyhsRNqf_d4pTDA5dnqQhyU-fR1J6-CQYgcSS0KTfRFFHRO78vuSAXmLM0x2dGLHPcsA8oZA2UrL7wnBP9WICGN0ksMa4nXfqcSNmeTh2UVCuxJqPwTP5NlCz7iGZ526iVXtsjAbQqcCMs_My0IoRN8dbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOs4RQCz49dhMAks4tadEUMfD5efMxgpjq8wk3sWb2RFQRcjHQTgOC0_PnFKXDp_gaBlGqrXoEQcykimPa2mW2B4vxqdHit8Iu9XJ-MhN8W0dUglkfDd9M4xoSW4g6bXJtfziFqrU8ne5mqtYVcfEhjRWNb-hqR06aMOTFmtl6GZvO7xaod0_KmyLZT8_AM39Knfvn_uABryzYWOvV_jME7nQlOKMUABzcL0FLsti9qEqnNmXqtQ5R-WL-9MK96abPzudNsmk8FtUKLOJVUJPYGprz8JiWQLky00kGhN0cpMM_H-Ah5D41mQlXpyrlAKsJI8vPy1pc2DNgTfoYmVEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCJnWtCgZZNByDGQEYDylshb9ZYSa4CcCgVs4yFsyw9Sqrr-O0tjz8Gti4Fa-PB5iG1q5X68yWpo8CpYOfo3fi0ATMv6L9opK3fyklxc3VNPuOVjQ8mopr433Ca-Hzvc8e5XseNmhKCFfz5xt2s5Eg-DLCGwUJ15wKsieBBxnA4puvvj0RSOwJEjbsu7iJ0Dbag7WhW0fsRWdCP6vqfRyRf9zN-ERZKP6rY1NyPrNp_vTO809lARmorzt1ZcMy4X0FNSrdWhopXnEgB4EPlphs6yFuM_daWpqZI8FG9h2GQXSI7pE6elm_p7e52fXvlP7K3kJfJkaGn-a42hNyU84g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l49WzinUFJr1Ov1Jcfq_5AdKYoTuh6UkUck8OoeZUWwH3PWDWkfEwdc7Zy_p3cUsyBuJ9VB-Ap2bSPpqGghnuNq2erp8mytcu2tx0nhazm-hK8-uzbe4E7sxax1jD-rSHzHgoz07zmdmEWJ30ZLcCT02n_3DLdXTNhwLO_sFAGK72DSb-YXMXrBttebbSx8Hk5rg1fQrlMy5nKNyCjbtS9yXe3nNTQr2noPg86c4m0VOJd6QxfbKsmuFr9WuINP7wkK94yowv1lFfKvxQ1okErYEPMpMulSGk_nzbAsKvUlTnN9P3X7OVcVSuD91eKADPgaMYRsiYRCJ3e1JQSFd0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VcEZ4rzyMXOGWWE73cZjj_cIa4FPZO_IufrDU7jAnrnabgxU4TyZCpBYqNKghinKN1Eg5PeltaXhleSVG8UBa_1FuqR4CajkNdJKWd9zsmQZwLNCrkM_RQtT9Jy_OtJE0sC1-JMzZquF420e3KDHlY0QPbeTN-OLvNMraC2C1O6PpCCjcRcpk3PzvsWbM7Yme7O8hGhSFwuUccnNV0SWss36OLuK9HcNyBFigKr7wHpnT2GkxbiU80OTY6-H_G4nksipU8adxxy4iN2V-PzKFYkVkUKxNvxoaAunM8y-SIWzhorGjJcFa2BGY8vfcKcj_9NFfKpI27An9pTqVOMxbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mUdvCubINHDyQjRI5n0UlZ9eLugrZXKiGw0BMxk6rPnEwzkBK-5uMPau5obhvH_jKQSqjISuCtgbCh41j13g40r353xpN-fKdiyRkNKhf-xDX-m-AxWQKYXwLPJEW3sfnPBDzsoJ0oFXk0TFDW6gNygZmlCQBOxdCvJpplpOx234GUQhClXke549O6i7NJqJEhg9vZv6w9cACwg6FPxDnoiUNlJwkVIuDZejXWsIK5IXSi5EzTCyCq4zhmZh-HxsuAwiJ1AtlW0iEAY6OerP0FHVF8-wg0AJkVnkJo0xMqdH41cf96Y6QfRWGW0jpk_PC4ZbfCyZRFJijHMtlXhasw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=USJJ6AnaMSVNcJFdBzq2nrbB29TDm55DgJ4JNqiiQgo_QJ9BiE5Pn-st7saHEzxrgaqgqMaznxCUcP2S-kjzYppMLukff-uHzP9KHY_wmGdNBexCWVuJxYI82Pgr6dvOmWu_XPdgko65V3ocdPaKgnMc_WlEW65WmMjmpGt-T8I7br71tdl2bLMANTKOKgn-Hu0ZN7mqaRZftPbo9wOxNj8O06b8-ApSaInr1CDkhaBKRSkZCWV4arJZNGl4WemYcE99wERUQvNqbxOoLuPaIxlIS2KW8oEWQCKFVqAN9mbMBwYIE2pm2Vi5veG3nlgak2UUhCa6rVF0tdAr2vzcYVBS4gXaAFfkSu6bVgcqBE53Amu2rHBCLvEnvgIRYsfQT35oLHxIJDt0Fx1n1xVAzNIebb5_gCw54m8VsXkkpziQ7XLr6zW8UIFBvyxIaOOVnwN8w05KGyVKTXBiecKVS2z8FG9jm4YZ9B8zolBq5uV4XP170JOc0ZQ3bKu8vaPmzSoWQL-keB1W9pEarMmz6rOrSSWqtkjsZdp2d8DVjG1anThNBX35BopR-vMLZL8N9iSjfhhyTOnLp7b13pX9ydtIziAP87DZz-GLjeyY9wR570kqhvAII0NBVrVr3qxKxZjifhEib3T9rKq5a9iKYDH5gvlB82c3TnDI6sAtVEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=USJJ6AnaMSVNcJFdBzq2nrbB29TDm55DgJ4JNqiiQgo_QJ9BiE5Pn-st7saHEzxrgaqgqMaznxCUcP2S-kjzYppMLukff-uHzP9KHY_wmGdNBexCWVuJxYI82Pgr6dvOmWu_XPdgko65V3ocdPaKgnMc_WlEW65WmMjmpGt-T8I7br71tdl2bLMANTKOKgn-Hu0ZN7mqaRZftPbo9wOxNj8O06b8-ApSaInr1CDkhaBKRSkZCWV4arJZNGl4WemYcE99wERUQvNqbxOoLuPaIxlIS2KW8oEWQCKFVqAN9mbMBwYIE2pm2Vi5veG3nlgak2UUhCa6rVF0tdAr2vzcYVBS4gXaAFfkSu6bVgcqBE53Amu2rHBCLvEnvgIRYsfQT35oLHxIJDt0Fx1n1xVAzNIebb5_gCw54m8VsXkkpziQ7XLr6zW8UIFBvyxIaOOVnwN8w05KGyVKTXBiecKVS2z8FG9jm4YZ9B8zolBq5uV4XP170JOc0ZQ3bKu8vaPmzSoWQL-keB1W9pEarMmz6rOrSSWqtkjsZdp2d8DVjG1anThNBX35BopR-vMLZL8N9iSjfhhyTOnLp7b13pX9ydtIziAP87DZz-GLjeyY9wR570kqhvAII0NBVrVr3qxKxZjifhEib3T9rKq5a9iKYDH5gvlB82c3TnDI6sAtVEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCtmNKOmzYmIRtB0EeEjgsfeoLp6-YHpDtaxCpYI_ZF8yXYevfbeO4YETbl2Dkuctz16LSLmnk_vYMGHZtwWZ7X9nO6Tp1Z61A2oFNxUsREZZSyHNOo8MozBcVvwTTPnD-SRBXB6mdF7fc7xfMLO3YdMNaELW9JYKFOo1LHDj0IEZ0dhiZUxCLRUG9iNcvhphvngtVa60oHBUwR_SmitvvvKoXkegHSZYAiD5BbUJ0MD8hy_l6bWpobAf1HRZ6gHBz3XoBZBzrOBQ0oES4vKfFzbTbsSHOM2zDK1i05QADLd0TnoQdjEScL86xgbQmvzRrGPYDCkktzWaqXgS5feDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRodbMV5aGlx46vQM840bDrWjiy06gG6_18MNpR5MWcaofrGxhDeOUG8F6OnXZ0X4Ff_K6XYgdHHIB9l3c4BlsFI4q1CBIFsJ60rV3NJNwk29IgWfdNOyKPoOZDf82E8L-c1kUZZ8T_bW1dksF1CEEOKcN66cLlS8Qf_XULmzSimCcol4viIkuZGiGtacbU_XGYjRcJDEN-f1aWFEsGG0Xv6xD3v8yXoJAXLogjiUQzhheXtOTAr7x8AF6M01WHRvcwhsFvB4GtwZQ4enx0uekpTwh83gqZefScgytfhmwSQH2yLcK8hpkCLqx4uvAcsl5zrpX0ZGUofoDeFkH-JfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PDSsZHRKD-PVk3LlgM-hibSw0D2bI2ElU-q2SRH6dvEDsWVposlWBax-AUoBTnTy928QfTL5A9pjwsyOneJevTgvfO_to6VBHH39jETwZ6Tdv0e2kBo20wIc-Bri-Ur6Gm3szoQdJ8A2Rwvuc9vsRFwuqa8xeFMLcNKj6P0FcPFL4OYtaFs4rUhEonJ_AjIyCmhRmK4knW2w8QIxdYzW52RpT6bXfputAfaVerdioo7KJkwO0yQrd4mSNJ-ajyvXVah9AAr_a6T6akxTj0ExSxu25oLVRq0Rm8SdS7JEf_qq1pIwRWsgD9nc94OTXwo7Yytx32dca_VtU2H5b6Y_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnJqn9M81VOkUVlDp946UC0UN-QplbEHPl8rToA5q1_u08AqLmSMG2WZqZUsFU5CNP5Vbh75YQmO5uAkfab1qiA9KwfgKAqAcXqbGr6xWcx1G8AgRIHWUMN1JGypb9V7ZJGw94x7xnjoeL9bpBJ4sJ1PgKoDMgjARszv5ww5yJhWkxzTwIUElQxI-qkrB_CSqJCskqyjrS4KxqgmDbZ4gYIgnt0wnnV3QSWzAG3vwHCo9MP7hZCavJDoGqV6acNcEzmHADeZlpE9X57158VQd4qe6wP6UI0la-eAVLvElVttS-N59yp5gZNpIWkT5g5e05AkgxBoSnpkvBypEZaONw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHSqcSFSURv2BfkpcVRyCP91rSme5N1Vrd-sA-nED4bdtrWTovV3AugQU7MuSQQMn4or_XKrvey7_NCKRwWckkLOjttoF_Hi4FqjpzsDzhT6NTA-as8oQjJQB-UbY-dX-l0wFYc9xyxe2rY9-0PMcgrX3dvyLM-R1aRPxdRf_3dO661lyvZJpdRQ59B1VSMZ4Q0zBNBv_vcec3jhEIyviuKX_mUgk10wG66O_QfnMQHSpjjf1BNJ2_M8wqozoo0Qhx_2K-iINpgrPNEZN9pumCa9382jNDXIMlTxx1mcAkMd4Gvgc92XOrjQOwNZNnK2AGZ4EQueII61sHMJkeQr5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m3fqQdYODYikCEfa6eygi80JyX8PcJrN5Txc7-UzEIn800YDW4Ux_kZucuXfaAvBpzXFy-1OhWNHxIuDkmkDnHEl56HxVetRZfccZB4yin6-MzcTwAOJ_uKjhs4J_5cfppafyFyVaktDJ9TlCQYDwG0icC2mSHu62TA0p3gMg-qw1Nf-5JHG8JcePioQETi461n-UnLSwDEDVvJXxqN08VBDsWNRvX2FUTtxZpMbemPrRHSlZzpFb2rLLwrCS5OQ4Hy6b9zzSQ_UUMKkntiLb3ecRH8jZb_zfzAtUCCUIbo7zMD8z_lrMRBHnvaMslDtV7kDaEveszhwsjOluAEzyuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m3fqQdYODYikCEfa6eygi80JyX8PcJrN5Txc7-UzEIn800YDW4Ux_kZucuXfaAvBpzXFy-1OhWNHxIuDkmkDnHEl56HxVetRZfccZB4yin6-MzcTwAOJ_uKjhs4J_5cfppafyFyVaktDJ9TlCQYDwG0icC2mSHu62TA0p3gMg-qw1Nf-5JHG8JcePioQETi461n-UnLSwDEDVvJXxqN08VBDsWNRvX2FUTtxZpMbemPrRHSlZzpFb2rLLwrCS5OQ4Hy6b9zzSQ_UUMKkntiLb3ecRH8jZb_zfzAtUCCUIbo7zMD8z_lrMRBHnvaMslDtV7kDaEveszhwsjOluAEzyuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChkbQA5zPxZTVYAxN4WWQnJCQZw-lBwsgmZDUJ3-T2vSkaWfQXEOC7I_luyC-KBJuVjpIeFvTB_QgeGIpLsNxacZD6HWAlYGZEhZE4WcdCcgWpQOyWfiYVb-6Xk1D0Q54iupHLxAUfQqz_ek9jTJcVh1w7d4z6F0-YylBt_wG5QrVuFyGjdxzu2UZxZtupDmCquuPGPBZSaBdfb9bf7FjZoEJHGEromMVgDOeJRBzenvCN_dzB8xjaClZGsFD3lsSCCh16_I6YhTpVMk6SHPyh7dxDKLWX4ub762-S-IBefyy5QG6iwn9ttGOOAWL6XZHZJ9v66Vl_mxDtrEC1rxZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6ew4vo9pJTZJCTugr25dUmuodgGi2dZ0xl_9lzhmT95eDAOwT2B96Jf_5GerREOdJVeMFJw6lFwLb864pTm-EwLC-BGvP7n7nJsmNuE80kRzbE-P-pfMgpTPrBZpYarxMMDndIOzG2onmXafrWCwowNGRrGpLocwfa4Hd28RE9vQeqGhI8A0GbA_E7K9zWTY5nWjGjkNSvNWjvDKC_p9x12_DaRa8n5j7Nl36GSq3MZqWlehLk-42wQM8lpUgYuWqqXaX6nj38jZC2oC203aLup8M7xOOIoo6lEUr6-KE0mH0OiG2BGfP3cfgxvZedPV16Y477k-_-I8RflSzE-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
گوگل: بک لینک ها مانند سابق دیگر اهمیت چندانی ندارند !
🖥
گری ایلیس میگوید که گوگل برای رتبه بندی صفحات به لینک های بسیار کمی نیاز دارد، شواهد بیشتری مبنی بر اینکه لینک ها کمتر از هر زمان دیگری در تاریخ سئو اهمیت دارند، ثابت شده است.
✅
گری ایلیس در کنفرانس اخیر خود در مورد اینکه چگونه گوگل واقعا به این تعداد لینک نیاز ندارد و چگونه گوگل اهمیت لینک ها را کم کرده است، اظهار نظر کرد و گفت در طول سال ها اهمیت لینک ها را کم کرده ایم.
⚠️
اما داکیومنت ها می‌گوید گوگل از بک لینک ها به عنوان یک عامل مهم در تعیین ارتباط صفحات وب استفاده می کند اما در آغاز ماه آوریل، جان مولر  توصیه کرده است که فعالیت های مفیدتری نسبت به لینک ها در سئو وجود دارد.
🤔
چرا گوگل به لینک‌ها نیاز ندارد ؟
دلیل اینکه گوگل به لینک ها اهمیت بیشتری نمیدهد، احتمالاً به دلیل میزان درک هوش مصنوعی و زبان طبیعی است که گوگل در الگوریتم های خود استفاده می کند. گوگل باید به الگوریتم خود بسیار مطمئن باشد تا بتواند به صراحت بگوید که به آن نیازی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/danialtaherifar/812" target="_blank">📅 13:54 · 04 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">shape-of-design-@danialtaherifar.pdf</div>
  <div class="tg-doc-extra">1.8 MB</div>
</div>
<a href="https://t.me/danialtaherifar/811" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">The Shape of Design
امروز می‌خواهم با شما درباره‌ی یک کتاب بسیار جذاب صحبت کنم که به نظرم هر کسی که به طراحی وابسته است باید آن را بخواند. این کتاب “شکل طراحی” نام دارد و نویسنده‌ی آن فرانک چیمرو است.
این کتاب فقط یک سری از ترفندها یا فهرستی از کارهایی که باید انجام دهید نیست. در عوض، چیمرو به بررسی فرآیند طراحی می‌پردازد و در این راه، چند سوال مهمی را مطرح می‌کند که همه‌ی ما در یک نقطه از مسیر شغلی‌مان به آن فکر کرده‌ایم.
شاید بپرسید چرا یک کتاب طراحی را در یک کانال سئو معرفی می‌کنم؟ دلیل این است که سئو و طراحی به شدت به هم وابسته هستند. طراحی وب‌سایتی که برای کاربران جذاب باشد و همچنین موتورهای جستجو را جذب کند، نیازمند درک عمیقی از هر دوی این حوزه‌ها است.
پس اگر شما هم مثل من علاقه‌مند به یادگیری و رشد هستید، این کتاب را از دست ندهید. امیدوارم لذت ببرید!
▫️
این متن را Chatgpt نوشته
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/danialtaherifar/811" target="_blank">📅 17:35 · 13 Aban 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
