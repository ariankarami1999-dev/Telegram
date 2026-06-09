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
<img src="https://cdn4.telesco.pe/file/XyCVh3uVJlz5ewMsILytBzNj3DMTCOJEQG_RsPw869z-_7uSJIB_TxSO8HmLWq296l4imSS0Qz5c__IVkYk0pqGczH7ZnsfNbu6NPlAsFizFPOhOj35WrU0KJtS4Angt6zJJZwzG4iYcM-nTOpNErNRhZY_AwxG1WZce_E0YLzmMLJei8cuWFMOPC8b_H4-uohHVS50Iiz1pumDyflXgPpkk_cWf5XqDwwlr59qnr6aPHvkcfemHgSJoMRf3az-T8ajRhHKpngGv1o3LtP3p9Y4nwamcDFbbz-ZsqcKOYH7agoNoa1kSGjBsF5lgtmuLPw-8NYDNM2LXM1ko_2E3Dg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 21:58:03</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 219 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 273 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=EnI6hMkmtLb8xT2CMlxwJ6TVky7zHWlwLceBGnO4RZMyYmPEugCQ62XGZ_oNDMVD-QbKM9dM6ap4_vrvtwgs4dyvWRh-Hz1iTijVRgErnSNqPryWxCB964VmJfQ_ezQ9UOJtY-eWpfLHVbT2ysizDa5D-RyR6UM_NNpHSQRsQERF2TVicLw8BUFJQDOIfj-o-6aopZYGYrgDjfsz_LAgQerW9ZFgjReKlg3iX8pQD6axUTqG2NHqXOHRe1P7Ref0CaJHzEUUGK1oGLHiRJv_D2LDFHRntAfTRdiH9y8ODUsaqQJMQXvlrjFE3pkkbkkZJ7JF_iyxn657htQElnRg4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=EnI6hMkmtLb8xT2CMlxwJ6TVky7zHWlwLceBGnO4RZMyYmPEugCQ62XGZ_oNDMVD-QbKM9dM6ap4_vrvtwgs4dyvWRh-Hz1iTijVRgErnSNqPryWxCB964VmJfQ_ezQ9UOJtY-eWpfLHVbT2ysizDa5D-RyR6UM_NNpHSQRsQERF2TVicLw8BUFJQDOIfj-o-6aopZYGYrgDjfsz_LAgQerW9ZFgjReKlg3iX8pQD6axUTqG2NHqXOHRe1P7Ref0CaJHzEUUGK1oGLHiRJv_D2LDFHRntAfTRdiH9y8ODUsaqQJMQXvlrjFE3pkkbkkZJ7JF_iyxn657htQElnRg4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 332 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLbzEAgpFUaWYu6NFA41EHWksrsTmqMDGm4y4pwMOrJTdg13a550c94vFkxdgzT_gXfstb3oJK_nXK3CRx5MnMeGdnB00e5G1agorni113AaB4VG1bjP3eLEJZIfOtbyP_R1y0nvTKqwX7kdBuxZ0UFMJFpzSvmUQTmxUKxRzrHljTF5xWih81mu2OTKV_ptgmmUzLJciGw--BBxAoecDM28bg3OmkWrAKjjkJx4-BwIa8vZqbeMdEiscu25SeJoYgmDZndemLqZiACtARx9ltGmXd0FKizTVodWEn3PgpBHqrNScTsUqLMXXnhwYdoJ-P3qh_mq7_X3RMHps9gtOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 478 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 608 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 719 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 816 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWc0HpEUKI_Xb1EFvqwXPKAhekP9CapJMUlqYwbyOYy4sUPM_bR_o7jIYFSLFm7x3uheEy5Otwppvw4wvjirUTf49Ech6bL1zyPhhA8PTRY47Wx9Bseui4W98Sz4gcoLTeUi6OkXnaEx3N9ab9I6Yrw9bPDAWbuMRwv5hmlPf5UZXT5WV-WRjsLJ16ZM7zHNjbixkA24umUppY2w-R3r-I5XJhplxLgXv1rxPA7-zQUx4OyrE40JhtUDsztzKpF7EINRXN_8ox49d-CdPePqQ8BN1D52YEZas03tFja8ewXPM4VZ5QAU0Of9_q1BogcsJPJeLce5cr62GM2xz7xIbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 850 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sE64oOSKhoZKQEr33YwvDBGE_n8dKCLDXqugPnlF1j_o7AG8O1-ngR7Ya2zwjbcla3hvXNXiQHJeSKmj3myy_3SMXhUk4Io9zuNzIDHL65Eaow95Ydh2rmlhyIkZHXXfVdB2Q9OsHJXrrQwVtVoMo7QYJ4WhDcBJYoDUudtzmiEXc-mi0DRmaIJsQbPful_BjQB5I8AifxRJWL835o6l_j_h8EOkwySLdwPrRcIGo4Ofsy2kdA2RuRCX3Ep4bYb8pWBx35JevfFRAVHo7RYT0F3WACGnqLzLKgPTb_MEuAMocRp76DO6XHF5SbG15vCWSAzjInUBZbqSkAdkgJzrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 968 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf20aaDoq54qn-MVHtLFx5KEf4ZzqTTSAZpzVFo9pWFKGSGD-uobTxvXq5cJDGFdduzI-F-Bwes5GPhtKRHllnYUDbUvbLtSaUCLPtIWK8PNNOHsBOxjK7BRvKCrFblgKHNEbdTi5EsMPlQtawxEIJfaZBNeToqS0LmZ284K39mT0wCZHdm4C0icu7hMcb7UD_T8vO_j3GOaaYRaQdMcmiPqmB_MSnNCDOg22nmC3WInncmLPP8mhgbbxu03ghyGneb_zOFVxM1l3EmRyeA-ld97VIV7nbbkYEOEJ1xx9oudDc9KsiPSGrER3voh-pbv6EucIr-5XNW95v0OTTAb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKeGU8awJCa5AMbxtk6U_4BsxopTkkZ1rnKEjn7lIhhT3T12jPPrGlnEM6mx63X4wm58fXzDaO13llQmAECw8-R5_bct2J4OJJCS5bYEBCKysKagGTC9-bHqfarCEBhxQctlJ0gS3nRx93LhSvSK-XM2dobTfgzfq0FgfSRGxMkpeXPSX6oqZIVNndhvPxxU05_yweFIV-pX8ESIIRh4QxMaP44FrNNXgzdbdMYfYveWbkAko1g5QtdKFJ3SLcPwR642g-BpfsO3zUSkVdJ_2OZzk4QWfbLQIrAftzJEUd5ZCHNb0ZQynPCyXAFGE0HI3M3HOYdh_DuhZg1E0Bm4WQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4g7Zc-fs3udd3dyzTzmpRxrGe8Xa8h2lWi0RGHUsklit9e_mvTXYKRu6E_hgtFtEgOErcthMrYjL525F4jQYBu_Qu2sq9EfT74zA1eGwd4lONzscBxxNqslPt1hGu0RnH7BP5efrszQkxnhFZYfYBV6w1ey7dVrZrUfzlifJXlRz9qvpJQvI4xwwT0G1SIqQEM5WjMdV47HagV4jIxpOn0sXGyHo1AFoZNLqv6tUL8gTxrVtf5J7kCxoYle6NeVOdOwr0YAk5uQNQ6oepbK4mj9zTUXbFgkV_2kyWXYMfebD0NdzjiLYbz1ARKthMjW1vuEflcUIjcjuMw5PuOJGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 908 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 937 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-8mf6RnsgMnCAB5FkQz9Jh_IXCFN9U-SLMfjot8XMYvIu0blXCWsC7_LBQGWAKVo7lWLpXFn4sYk7ZfPmG9v04V14SL3B77dNhh9f-HmVn-dxg-0mod4Y65hsbl0pDbcuWbjL2uQIhQ9E2Jusmf9R6PRYZv6yUCJG4RBFIbOwozfVs111UEHy3uGaGWASDbI5oVS2fcxJEL8Suwt_ckPPSVbWZIf97eDY4n8gwMAgxfaGu5JkzLHlE9GmKbEOVKMIrELXcZWhIpqYMMGCoEpcha4RzAU_qk2ta-l3bChmpeqh6wUwyi4LlnME-uxZU5zO_w_WWHbN_qJQG7ReS-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eF0jj5-hykQaVmogvTK2s6KCDMcW047RmwjAxBK5h-G8XSeOVtk-pWruMIIHx6_uWGjbxCPKOjLz_MnHhqTYEKoFl4stihXD0ZjV6NK_J4KlvvJ6p6n3cMdMXC-kv9l2KX3i93hV4okUrW7oKG2Ppf56KdkTAavDL_VxWAaV0Lz4xTJ92LDwyHS0Q_8pPZkSdojPq_UY0rQz83Fpt_foVPssR9_6b5jWkGdN-CIW9Ug5gtSVRkmkb5zrDXP5QION5ikxr21Y9l7JhnEVzxe87b9XlRlt6sU6jV9sX7GIaQIcn7Vx75LeVWj0OJg5mTshqQN-M13Hm_sVe9Z5-msGDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cv3ByLCvZzWLMVft5YnyMgjSyqRCncE9bW8AzeVfktXK3HhfndhFFvIePmn2klbY_JfotLVSM0Bg1gAKwyQt0QpopXIpI-QdcIsmo8EwwA208oUVtn9rYQX1rhZTtuTEOV_kvNGynf1qfjZZpJPgp6fRJbz8njQbqDT85lVfJ-dXRmFPVVFGNuuJ9UklrsusRPjPiSjsTj46E1lxCl4ohmX901KB594ckOh9roKCsJAzG_rvTzTAI68gDfbs_4UW7fWKB6t9mAjjjZqyJCcfesUGf-9IYIiOmCUlC8PhSIrceMCpmL1qOpH3w7CLvsFC6fxfgDMgsiSeyqPqCPs8Gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz4myqclG5inDk8CwHDnJ5iIBXzqRIm3m9jb-WShIClAWeKs8oMWf6fOvVIQh7aUh8pz5RXZfRn61j5zVFERInEgz4mOPIeZdrqmunanvFQTM1ZHNLkRlOvFNxhEwiSqfFz4RARVeH0hSwG6H5oCYGSrsMaXEFbWxJRwJOat-LLRpA-0mHSbw__wep4bz-njqNcuZDghXstjFPvL4tvcaOije6eYThbifuPD9O604iqWHtYRtp9wQ91ArBZXGO36Ku2bJL8kOTsbsInK3WHbdzX1hhmtvEwkW-HsU1IX4Soe6pYRTPbnP_hroo9TZXUz8USvGp8gDArwKKDsxN218Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KV5OfnKaKyrfJFLO779CqUQn9Th1GIgppLZZ9RQbUWOeu1pd5zhl5-M9rSDtfxvGDRzpcne2Hnc_dh8f1bt0z5-V0RnnNSnvwGlpZVHhtCUOUZ-ibNRun2sfFIewwFlCfn-0IFCBQQYeulrxM_oJfJiKYV9YVbEgWsOpn_xmCwRZYPBDpwzDu0dAwVQCRwqpPsnqGKNz-SaoV_D4lUuQk5anz5x14tx3K93-6gj0lTAbGLza5jbaxLr4SD1je5nFhGRuOJ1ADLmbfPIrA8OEMC0Ct3vHEaxphI0So_gKEDt2E_RZ1G7vv6KPxXG7iTq-LH2q9NaP8fpvkxL1WkNr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 865 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 814 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1KE1u4HuvbMqHQjgftyBdDK907AyihVrF1kXYfYmONujqUrLwPQINIphfF1oLQ9yth1nEhNu0uDvWdFlwzIFdyH92JEqB0VvbLQb8L06lFGkYuybF_mglv96jfZyQET-BNulqVCxFIN_vuYENyzzovsdVtxNTmS0PPYbKMx6T6X1cSq_AJFCi1IcxwslPr8SdFhIaJ36zwdK3TLJY54xT-0Sx5oo-3glG-4yGoGmHFKJobijD0gn7uyxCT93eqfnuG_3fgrd4NIUNMn3EwhPowT5UjdLgfqnr6LvhJKdXDQrho-KMKLiXCfmpGMA9-lscEnDAZhZmXYwMQBS6HCjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 847 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 679 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ri8r1PvydV9UE7fUVn09tuUPvJMPtHXSMgp-3rl7Erbp9w9BkXpy3l-CI9k5AjC3woS6CG6P24SQTqPkFNs0vV10nTlehzdTaLZLOlpPq_BX7nFITdgDAJZHM3dTr6q98fMWu2laaFk7BPdrccwEJK3kdR9l4iVIYQFkpDX8RfJl4NZDVaAohImTqi46LBTlUXCekIgJFr7k3LsdHjoga20O-O2B-yVi9SA5eQpyBMZDjNlrbqlw2bPTtz7n6Pys_cJnidqBIvlHazgftn7EJyD9zbtWvI4VTAKxZ8VNrLPOp3L8K5o_2HtgUCOPKsmAI0F-wkTVzKR42w-Z_XXj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbL2MP00YZVMV4VT2qT7JyltOlXBOUJbp_UrYT_Wz43he96vg5avOhlddyVNc-2dXNfaXyRC-KE_Z7oiBkeGC7Vc6qWvH66g38-_Mo5iEe3XHl4Qu70l0qqrHCAzRdvgFzv57U6AaHwn2rUHZpebv3g3TzEE40KNzvkvVryI4kKn8ytEhF3gR80LDp_f6f0d0e0o3o7o1qiht9GQkBVCz5EPtbe6WdMHXUKsZkeMCN17qZCQU5hRht7FWeTBeCiKdscuHyfl8FY6DY1K3gYxGovWMsyiKREHKO7GRucZGedSfoK4kjEVD3D1Rsj9WVnUoxs8S6IJMhWhpRWu0LS1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u43PqlOBylewxwLg_iIQyxLP2iW6OW_1272SMbFRCApxn4VlC7sCN5vJteEbG1g37tDd4J8UJtBxU6SGGb7A99FjLeQtnVBUbsF_qpcz0Tq8tMpvoKwcHZSUMjL16uJB1ILHflBjxKAVElA4iLsKaJQ-DI5bItWZ3_MkZevSp_dJzKXnmwKBV1xlWkMsqOV00Qmdas0laAL2OXb0JJPg3gWJFJxBD6TjusjZd2A8Zei1_wxVS69v2Jnib4hZHHb_QT6__tswcrJBwOeFYoZKCGs5GV6k8hWZcFLQFp8jKWUhASFfRbdOcuXA4Pr8Og_OE4XN_XVPlAy5NjRm-5nGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHyk22v795D0F58wLFhUdIxGJoFv8x6tXlMVJlo-72ZWn1c1J1D5AsH6CTFIKPjVOIi8hbhDc8L5tS6BPiyEYtLGlqwmxkyqHyrtCTJwSM1ktsJn1U5xi1lkpKjfPSGyQ4ycTPOCBg4pWu--k3xJ3I4xNr_bu5VP1Ycmq9pG0evOCcaFSSAudvifePDKzbnOAjOgYrWAFaIPylmjg64RKrC7rCUAMDw_ZiMaNCt0e0vdc0lQlRsKMvI6DtmLL1S2pL-oUpeBqvg4QRyjKaG56WFsUavol4055SPipVATEtpZcRFGia6JxaJCccW6q7gkZVqbcxEDDKFXGQqEB60EGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZ8LiVsfycb3fgpkIcidwDZL0441McNRAATXbnTk41Qc-DsCx-oYTPHbr8sAtmPXUh-08pkX69haaKX2WjyUQKvrD-b65oEsO6eHVzKJ4Kmh4H8mkD8HOdE-v3ZHIi_SiS5zIPVMMBJwJg6ccIfbXf2waH5FYnCXmlCk00xIyipUpd0ac6r1qpfHPNPkADAreEBWt93ezY0qTbzwHDtwC842tqL0w7JD70dgN42QWclGeu3H_JOPyU3-TxRwJ1rA-zUJq_eb-SNJciQGueHkst_Jc_unGA8yFNd1Ed35MQjYBc-I8LtBTTaCTJbI6WhOg4hZNCdDNSxgFdm_ELBI1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdxfNpfNrTB4oslo0bAeoj6n8WXuAalUv0KT5VUL5m-LKqLPYc-08RBiZO5XnXC9jXbLyS6IuO6GOjW4_aoeLZ4QZY-iWPUNNj0fLvE5yplOIZkODmevKZNcOY57lTkbJMol2HgN3-vQGFcUslCY_gHnuKFzu-s1-mvXXqCW8ZVGaYIaC5ec0Y_eKYuaKy5z9JRJiEPBlie6klNHLA7RhgsI76A_C5JHvmp8m3-PVczvaidjKfvRbBSFihD8DrGzIvK19SSXk2IleY2mm1wk2zkEAJwXqYcSB8xjy8vfK3yfe_5HHylvSDDYHcvbFp9ClyXENKnd6iWlgH8qkGP8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=qMGsdyO4lXkXNSuzT_ayLBqtxJ_ix8qkzWKN9EsDdOtRh_sIadFqTj3M_2YvuDl6B-Kdw8PBMGjKCdo_QlE_jZQRHjgeHSW7JAMSfjeO5K25epvBFegoZT0z7tG6BIzv_t02AxL7ggadaLqoJfSHM1mPtmoJWYaym9wXq03p3HZSJngR4BZ6wAtsbWi5f1GdUuy2XX-oL9ZXLgT3j892Fbk2yPGcLwvEFBPYbx8buAZdniFfJcl9BKJlqkgZoleZ-1F2gGOlRU00cx0f1ZlTq0xLXWOaY_RRugaPHxNKtA8RR2vJlKdy_Oq8LpRTVm-bURK4biRhSkfhDkhgp8SCqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=qMGsdyO4lXkXNSuzT_ayLBqtxJ_ix8qkzWKN9EsDdOtRh_sIadFqTj3M_2YvuDl6B-Kdw8PBMGjKCdo_QlE_jZQRHjgeHSW7JAMSfjeO5K25epvBFegoZT0z7tG6BIzv_t02AxL7ggadaLqoJfSHM1mPtmoJWYaym9wXq03p3HZSJngR4BZ6wAtsbWi5f1GdUuy2XX-oL9ZXLgT3j892Fbk2yPGcLwvEFBPYbx8buAZdniFfJcl9BKJlqkgZoleZ-1F2gGOlRU00cx0f1ZlTq0xLXWOaY_RRugaPHxNKtA8RR2vJlKdy_Oq8LpRTVm-bURK4biRhSkfhDkhgp8SCqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAcvbqatMvrj0m1P5j61jZTKVBmIBHJsrBj3w7t1kpHBDh0wl1fyQvbBoIgtCFg1WU_b2oeh048Gdty-HOWgzitBqhyutyghGGqzJ7WjD2QW5vDwdO8tRDirBp-coIYjgNXyhLAiVk8f8QS2tBPkMA7ORsR5HWV6pVWfvjCpvsaK3tL_fgyKswKwFB-mWuz9nOegM-Uzka5tra7iNghBjDXz1HYxhvlloH88iO1Wp5SH2_IjI-zC9DzCVrlkSz-23ABB2dbX-WO0iJ38AccM2kgV7vqYJB3oynfGEwQ9e4GKxdoLL2ffMJIId0mmZv1-PCkLWlYEm0mlcnt4gduBGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 926 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN3TcWoSC2mavY387u_65E0LRR0nLC5xKbcgmRTbYukmgiy_t4MbQ0fYtF-SaxYwUC0QmPKhxz9rB6QLHCralQe5doausi-kz3aAYaFozAlpmkWJtEN3eAiUgAfwQba9JS18XgKfO5m3xAqvacb8nUJarB23JAo2M8g1CDielrFXl97g_Gz2cwn3--bRa7zW9d15g_r473qw6DlVxIptYrukUJsZhT6Jv_SigPhzXvNHIbIxICfReBPqMcu1BzJ4yTmKaLW-hyRzrdLEGbJalKyO-3mh_52DQd2X8zSHDsg-dhHDZMws_1JiWQwarXiWqC2VgNBnP9H4O8Ox9ePCYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 776 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsmdB-G0l8W-CvysugOvL28wLGh3OseCgELMuD3gMTorcyKa5jo3EkokgAga2rT9E0KTx8FDzqZyNQeNf_Sh_nzNOxhF5sF4LymOW9juFrV8ViBbb3NhbDamSB3dggFHYhWdNj8x98kFwd-6wKDhse1p5-biE-Usp60_QXNmMae6oxJjidXKoReQwmlFw2m1SfwB8C72GFSdd5tHcyFiVJUYkQA4K3mf5L3j0MzXFihNUGLepTSFgRMUDb0XiqiqfKQjwEAWRDLNTXyMVrm4RPmP0XeT-t_JsP7Tk2NBLhepoDXtAi3IY4HnyaGTjIV9f1qV53jgPFOkBIhhoTfmcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSg9YJyvVpHS3ui0fcEJI71bn-oPHBHm-2YV3Hr5MIddb_XzEoP0HVSUuoXrChNJQjRztrlZfkbGAZ-_Z02SY6D3RVrsz_BaSilYb5qkiExQTSjHs8u07V-GJMQoHN3S3KaMlkqsp0WGYc8162aRIuuukjhXcPWq94zYgqmgrlbUDVe02iE2rkbeQ4jClS7-Oa5N5XBCDx2xerfVekD_VpxYM9Oak8LX33nDGg9rfGPBWEkS99wtRbMk5PYgwghttNBhWPi28eNSUrREQS1-driPxmPD6hQrhaD3DiKGCJt14Q935mJEa4VqRMPXQhI8xmPCV2LzJpJITQkWnyKOVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 797 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 984 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdYOOoMNAU7Ek5fBwrX4_HWgE7YwbekRH7QG-2TKJG17lBmKR_XCFquPzDjgJqsEPvjMTtDBz7QlWliMva-S__whTP_ibRVB2FbDOC8YSvgSP14V8ljSyT_l51U2GUWoAs_fkUfu9rlT_K5ABlV7i063Md2MaouC-8w755iZQV5SP4fLyemRUlFRYvjefGKX6ku-tJGHqrrOWXYTD1IE5Fn3573hwphlKYF31JItdiaOLmQcO8YpW3IxGP7lr5PYi1hhHiDFl_5usuGcdlZnvgZdmyC7nXV92AVt89h47kCX7AyJVasIoLfXwPxB_EQau2cHrQhiggFmBfG0S5DVAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 919 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdPve_0vFxe1EkRvCq1q8ylLxYWyfw2_9NoO2ogWR_YziDhQpXNjJCCmXY_I7XA4PnKamL9xidQGZO1UmXdQjf0tBgxqMarApMsL144i4RqziJn9ZY90-z8gjGBSThLm8ePGLM60j146dqeEn_k49Wv4g-ReeM-Dft-AILKKxNSSsHMEYQ0K9dc7maaXyIHL1KginlM9nov-3CPSzdnJbrrmgPXxKBCSb8qm_W0NAMIpr7oRXP0d7Eaudm-LxDMPF9osdicwIRvJT42uQj1OICQt5PT2VKJjSzeI0VEwllGpJxxdfb7BCwyHCvJS7hFuHct0ZO5MHAaRFXbX0wfmEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 741 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XmjMM0B-K_m1INT1DIhc1cYr3ELwxfhF-NDoQ8n9R7Q3aU6IuBDGj5simmvD8Od-motk8ZIT2oqFGMylAXdpoxUjiYWCRORyz1NcJCSb4nNGo3d05cWRaWyerX2hN_FPI5WfFLffPELtOvWZw5x971YU2iVpcrRWC3Zpt8K_7z6-d31VE52k3TVStO0bZSmn9xVy2hcQ49gktx2vS84jRN0Hqds3WTggdjjTKKQaI8qyw_4DUgdpMLF1VwjixaWiLDBiyZkGR2xDza63DhplJz3NijvcV7qbrz3zjFD8CL_Pb_6Z3ibGpBH7TnKMqxiR0nsr8xyUtajhJastn7K9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F75KqrlGsFBzqfzteofBDvHL05HmINMElQobUHkphA28HzPQVAz37seP-3Sf0bSfV67W5TP0WCWXzLjeLaY6UGIL8-N0HnD8bFS4mIGI7zqaJRW7BWsb7bPbHBt0Lstf9_8dpFMEZgLy-vvvHrgVXiAge-MpCYTNyjvuj8Mc2fTavQLHh8Wy6ZiTLQjt6hVdwovNXhuej1s7q9DuNJwSmjcMEFQhwKaVTb1-OeGe3JShNfje2_suc8s3DgPXkjCsmIMaZ1YLqhtH-2suQgl1V2QaKVeosBvjYio_2KSphpG9Jf6s7kJrqqaEXBmDtjzkLevwhIP-D5eCbfm71Hqo-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 751 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmPhUDw0tz7zh1h1MA9pxIHAybhzll4FcaDLY65SmHwl5sWz9N3P2V3SYokg2_WBMgoHZF2NXqL7qxcxGpjZS8KnO0QyVKvgBErC5QKf4ODldzvKGRQu0dWneVRUl8COqTo_VDl1_LuSVM_9zTYeTzENfOrbO7fpXn6FM3lY0qAZGJyVioYeZaPeHCiqm0s_hiDp7006ti7bMb-hj-Pue_X8Taw6vJucl266T9ghS2FJbcdLWnMjDifseXIcjJsirdunhWu_n139hufrwKo7WCkZ1EK7AtT3_BrdHr42V2agK_FdJgYjTE2VxSNjsNSrXaYgUAfaYXUvE0-tBeXNsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 661 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 809 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 817 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 719 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyJmOg_8rLSru6u18xLSn6pu8OOVuS6G5s_fMfEBHdzDDDc4FVoX5jK3At9P4T8g8Us8B4hq3OtOnDVUqYth16HvjlwL0iFKJzizoIMRZeUCLoRX1ODqlGr-LBMKe48Upv1kZM14CbcpP3BkkcwgiKmRGm_tA0Jfr5CvH-sLRDdGbXoZ7PVn5ckWjAd0E0uPgbfatcqYWesp3nWOWxvjqRECbyAbcZ2ZRkIYbVAdgSCQWU42gVQaUTxS6io2HmrBhTL-_jwpb12g9GraNFRdh95XqdF2ylATD4KvvCpeMBtvx2n6CtYxyg0u5E6KujHE5SZtx3oJDdJaf1N7l-cbOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXdbQxhFILV9Pk1eDaGsqvdbepBL51bfKZd7gAUet_RnutBTOm0vG_tM-4Yg4WROO_VPM1nmC9XvFNU5GYqTIt7aqg4eoZ-sAcivLqv6Qe4NR-kbI6hGNrPaP8_Myu1wsHCXb88RJv3PUXn-06EvJhd0ed6DBLIT-5_i1Fi8MGfaD1zwN2rif_MmkuLk0pgV56VpWqDLxeaFk8w79UzFNX-0opLOhpu3gQM1ffrJysPoFWBnoUaF4pAJ-sE7-9PEql3Uf7qQbf7PLU8x-6AlgVgyihYnLhrNdATaP22kIZsB-s5yq433pD_ILyqzzb0MIS2VeZoRMQ_H_bqCDbH2PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 602 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlVq6ZbIdA6yQHH4nJD7EMoWzD-EAjQj1hThkwGIfJCTiWyCDfuokN6F-4zF7w8dD1BBoFCtmPXFgnI5Zvy1FMKc_3om_Zh3nVg-B3dBcI0o_Ux2Z1GPTXtfbxpZGGyg5pwbTYaTZ9HwkkE1xmw35HEQW5wKHfXe2MnpqCYCnflYluWXq6uiDsL7Ck9wV5T9LKnUyAubDdSs0WtUx32utsstHAc4Y-A-VwD8NkOJoB9eZBCHFHFkIQhGg5RHgYm5P6_3V4AcDGEqRYkHbJ3bx-86j10e0vceOpys1JaY9vq021KaRjVVyAVtVBT99Gvmi5w7dkSfsIr45aQCRPAoYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 694 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 638 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otvZ-rVXQOCTCrbjD9ghGBLfjv9MunL4Zi-ZCLiB_8XJm8ZAkCGO9zudx6cOrRGjYyxkWX8aP_97usJ33kwZrXNL0THTmL9TeldYHsm8WdJ0OzX9OmQoFH4RX6j7Hp8uXgla7GWS2R9VfJMPNMj7CHmEMvydN_bzi_r7ha0wpgWgjKngaGRmsD0ZRLRyDFfzGyt3Ji-7MgonmuqBw5bDU5oOMyNnyV_D-eCDR7diPZGG5kkAkF3IUkGg6AfFNDRXA34VTwqWKKyhP_HKl4mMP0mikKcQfTILCVe1GTibGzj89F0DDU678D28fE9D1JEbVzZ4EyoMtdENmLMHeBrcvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2NZxYNrjWGNVDR6U275cmHvXEemGDZEGPzcGiQ-uYQzUvorrDED4nDQoSUJXf4PjCmUkQzBCoE5fM8VdrzG-se4Tl0pXaktV7NuEkU3t05iieuVtUX4dvKs306Yg4SvMp0bfETN5s3F09tgCIyGjGE7IaIz26ikbSN12wd1Tg7dwu09kYRaHPIx_0-PHpMcBf3kwiQ3zxK_Uxj4__ynXbq6HWdiIdF9swzNP5bCgtGlcDxbf05mXHfzyvdFSHfwaoyyKmeyVgXQEk8Yb8vj3RBJE4Cq8-yaEflPjCl8bsK30VCEKSscdRFo5zmIP_jy0NUh1C9ExFLKGCVqZdlYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsAAy7NZlGSX_SYvzDIgo61VIhdvAONYoKnv6TcfKilj5mdMi58RG4sZl1-4VR09MAfE73P2yjS6Uko4foAZ-OUReKQ9ENmAMSh_Bk03S9GSylsxwnKMEC_VVlplCcNqsedsNQKKDM09DR8BFUNTzY_lDaFwxsvEQ3v-kNRyS9GoAW3RK9KPelb20X4HwepKZQDEHKv3mci9z1eBz2W2JFIJLMBI5kVYp13je-_zKshrD3Tue3d40U8Yz2Mgigx62Alai_fJHIqTQyl8Y-xlDcjkVnYf2qzse1VyCJemS510E4cllCvxBPz6_LB2rawgVAPtpmpNd1OhV1LTPGcRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-vMZ2WjUtzOkLWpy8BsXsBr4l0SUc1x4X47rRaijt5mg-XP3aUkm_JcezM9ErG98ClJ_BHffBj75KKBoOHN-JS_lX6Ube_3f6AXC7xJsVufYGj1qtVaYH2wWmDXr3-5632EqfXoqfpaWUbDTCgkqwt9MCR-ok5avSZwkB4A5R3NbiycgmSbtsAV1We2UdPZ8IklU2jycIFuMsrgoe5axZR-yq41mDsX3ZfP7O_ju_UP70V67S3CHUaJIo1VAz_qd7d0HpgWBCNc8tgcKrGm492VroRmkGaKGPMPZMG2bBTo4GnQ4Vx07KUTzERaCK7UKo4TYnfU_4kgwRO4QrZHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzjhMXyW4Ly6Y_xpEZtPH1x_QIo6MNFA-yJKRV9_NwPE4axucKpIwg2Xf5vKXnzoFg4BRb8f-4Gsp5XOJZadD07AfFi-8qq6N42f9bX2BrvZDDutn9Kj3tpP0v8poxxE5Q-QLYM8VwdkqMJpMjYxPIGdNFlyZROq9CReqJEROqDyGy4Z_U9XocBUM1xqFnSnWBkTfTZYp-kUTxZorjqZdK0bctlPvJDO9sCN-q5-0uif_9wUKHSVxp2rxrMYGrinQXPEK93E9d-gB4chH73zMnBpMm2REJqo-XBfLA6VVlN8mhzBaQfK0hafo4tso3ID-u3tY6oZhq-JW6kwEmYo4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKs4-NpoWY35Q37bBeizFVPAQxsklA8-ZBu0ujyX0vkSiNTAMYGp5JumCmIoHKkaRIKuRm_k-SQv0oXB6kEc5usFCTtBQUSdmZGosCp4FFs6v6a7m99UOpxOikrzk3NywDesJxPZWoElgZuXG69tE_Gh7o1QDj8CPBHhjR3Km5wcZfpUPBxOKL3sHBWWMZckqOssuSciLXTGLTeCDT7LC1ukdQlNFbieJv9I_Lft5qCBUk5E1AHAAPlGgYmd-mho1Wc3kkIR9qYEJETOETHU1XdSltzrdnyCiMV418geBbii2hb6lOLyW9cK3R9_gZVj4eyZNU09N7rfGYlnMKWJFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 577 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0rLFoX-210KUCEkRI7b-odEDKa7AXKupJGEyCf4gqiLJsMgt0XYe63fpfZ4_GwPJRuwAW8q1OTNU6FCl4-5waRf3AKDwEyIe2Za1OqNxbFf38kKxBNdFvVlm3-xEVHaJJhx6RHcQOV20EeEb1-VEmYXQfVhWTEWWtvjkDyQ4nfQCIP8anxegLJJDvkSmEgQUPLwTnmAd3CcW4gK73fvsU3ejTwEFvsxhPLPCk3dwHonzs8jLdKuvgySJUWe1Cqa5wMSAhXYISgRH2WgfcsVRRmcgxOoQNgKnzFg2zXUtXbQKJBC-3TImmAV4-BXQEnBlL2Aqp2htvCvjxFDTz8HdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 588 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyVF1jEa6kVUfmNaDSI2Wb6Cd1fuO9DJgZbfbUgWCebjXSd54bIHZ6YyQl42UgDQig_Ri1aKDAn6879RPt0MgH7it5GMQRi_hXxjQ3ANfVWOfqCqXA2TjbFGwM8UasN0PEnVU1wOtEjCIJ9H46L3TAyPWqpjHHykxlCLMlLyGZ84eIanM1GZI_h5OLhVnkWqsEie1uTmo4b0tsj0rsiEucl45Iop2mcA7MpP5dmPrce5XeQ6Vis4Pi_WGxDlkdcHfS88Q_5o-k4AeT98mM3Lm3BJDGeu8RqDnE6WRF23rjM4bjlrC9WvbR9Jfzw47JFGVp44v6EpZXcwD94etLE4yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 698 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzXYKuDn3HSZLnk482woE9YfWSIAiH4sgMr8luI0TbvQlkyPfCTGapdptRlRfTSCxsGrIPCkbl6-27CybjTItzBGCjw_FpglgPmZZThUJwQzHftaR07_J9nLm-7yYBdSVUdB8_y_xk2wacFFCWOKWIomz2R9U58lBy1xpgXkevk29Ts2XrUHqPjiyapYc5eQgKcsMqsLuZGQe3G7ECnGHH0FAi9V6UF5_7pjCCCkfK-OC_Iv0TS27QdYMIOtaGwXIdf_kQpi_U5hB-UIR1wJgUOGnoHOiLo2Q_MdV7YCFJ4b1jQqeNnKCPc_9Tstb6rTt5YpKeW80rpdbZk4N4W8Aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 643 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA2aGIeJnupN_8XscZ_twSGp7yWlgcmP9dpHCaDU7AFoigA32gikJw7q9gFbTqY4OfXqHb79NAh5tVvXNn9VF8i7vhU5D_hNMe-HoyqExkwYHgT9SGQu4NPr8s07RF8P4qGKhBwRcNkRRXRaUSk0X2AuUDbS-1B1ahQk8k0HZ9jRpJ1K-boy6zFaladi8vt8VtZA2XI4eaYPCzJy9E8reJekV_gHVZWYd1J-jCGTaQVF1oGeya2NCUw7dnNmlzFg6zOeN4SaEEtC6OeBh4gyg3aZ2r3WoW1U3g3QSB01L9zq_hTJiAVL3feJHrd-3p2PUk1PD3b1R5zdR0F6eoTOlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 711 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnxQekKmAtdI-EhO_lReghHs_RvKPG8Eps_yQnPpPz920xAisDTURukGjZrrzGTMh7adnlvWWFhGFmIn5guIxndXVD2k0sDbHAyUaspE_1sD6gocIwvA6hGPv26ODHmE9JDByjejokGaEpmwy6dNynASRJT5lhtiLcn-q2xFqDBXq_pqD9zfmbj9otWvK_TfRSCGGAu2NusryhqNgNRGpo82h7OnYlNy88naRJQDFobCmN9ozqUz17n1SjPN_pvXj8fl-O9YHV0YLN2v-7R28MhZrOiWes57YUD44i_VqaZqS8E58xVDGPxTcax-zyCjYmndZHzWOCbASM14-e4XDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5G6BWqHaW_Abm0FlV0PxpXdVXHGRSw1Vd12QVvJ5kNcvPL9S90gXll9v25OtAC2v7QnSz54laPpQ8diAGzk3X9pH92D0asIBb5wikviGme7omnpFFNLTXz7O9rSSS4npXJDkCxttd015wpdbxHvHFeq3kv2poxW3GzHTClU2vOHxSsqDphKYagx5toti0HZcFOyGzEtdKFdyLZJWfmTtuA6jy6KjdIvXJtKbPn3WY9911btHRmxv9s2TmOkTjiSNao-GX6xXYyE2QLze4a4qieBFAscas10fDszHk3-WlznUa01SWPwYIR5STa8a9h5NErASqfLtqeTEEd8mL03ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ejtEzEUFl191-fBF4RCYmo43yld3OgiUl81GGM4j0H6RoEjGddxPkQAjWKIsNUg2HjZDsVUfiPfoI4KwZ_H-4rDzbxrcW2YZeMfPAMFzsYIVLKh6RupYUej3ESzgFlejoW4nmDwKC_vJUufHFocezrixQUaeIh-8OxjVSKdfiiCoVznLPZTfK68rD0s2oBgo-RPfYBFAlMWQjJmMYNjXHVGwJfqZgnLbhBNdoLojvuBqdy2LU7YxXJKDsgpy-bnrkqVKGOR3nPN_k7qRAcw3lb7QdV52PxwNJnVAeR99zXjBjppMxJBlitlj-XosmQxzgCa6f-6rxOqhdV4RFzvXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1wUFhi6JQ1ZMLrhqjrlUp2A1gvHDHGbziGpUxcgwMEzfWuWs4-bDS4YyXcrqS1xc3hkyfEqe4uJx05oKo1NtZ76_bdp8bmrdDeV2DVXwmyxwXqNyst72wp3O3BNlMQ2waFnq5Kynuo9CKAD2ZGk8HfqlSKkf0mzhXgZ_Tl1kps0jtyReVp-N8wePxx8wHIoeBpgZ-15V7OQUTIGOsfDBFWeGT6stDQsfIIxwmTOJwKR5AcaaLyK1VcpPqdctKAKy-92phgHKING-WJzEPvzrIel3eOBkeAPVxxcQOO8Ebyp_KxkrFxcqOGSWxKNo7gqolIlPMX0fmhnDaJRRY2WJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 665 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl6raxV9au2NzmaHwCWBmXfqAXEoSVAjdYW50BkWCFGKsoYlO5vQC-HFAi_TANN2WoUjU8KiioLtJtJJd_SSG8f-OyxcvIxGAbW8Yg0gbqwTWCU9OPrxMicBLYjo8SYcTKrwlUCqZh0ouhK6v60-WcPbwtD6Eeibu6iWhZVDYw28_uxnSKHS-dbJ5N-0kQ1tiZX2pPlagZZ-caH4H-VXROwt1j1P2CrXboE8pgX6otqrMKoouPRZ3PpAvwaiDR6AMWRljzNCNLnvGaVBpyNSpPSGsRhpQjAn3yaXfjC-3MV6z9xb-NbJnJ5V72Gh1QdhQTncjmQ9szKKgBo4IjiCDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 543 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtqfAb8W53klRjjVT-rmiaZKZ_zSOHc9yoXm0DuOOQp6b3d4c4qwPyTsV0YzEhrbXTxF89Y_PNkxnhEIh18nlTMQEke74mmRyZluXkyWhAZaKE1S_tl0UrjtOtyQRSa7BkkYWJ4YzUBO0CZeyyKAGeQRI1-d0evgAZOqLXMG_k8yqzXS1UqQrxP7GXImOI_fX01uwP6869Jls_YjUrfIwHLkaCy5BKRhl3656xuIcj83enIVv2LDDrIEmYSpPXRsYkXJHXHWdn-j415FTvdtlto6aDYLHgtXjtAlnIPYcME7RXFeFKuVnkB-keOcZ9XIPefq00hX0F8HXPcxDDBP0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 542 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOK0ElARHU92sc632WKLJuYsYDwYuZ9XDusWeRQI78Ti0Tf7EeTL6b09Okq2DEkj1w_GzfKNHp-KJ8BcOTjn63EaWpNnefya2tOirY3xLj8jdtS6Ftf1sDucvadNdH0zrlHttjq2-2v0dsiMhS0Rup9EVhZ0e0fhQtsKETAGzNWP5wArCudGsPnqFm2qmIqi2kHM1tds4U5YFF29k5RJ-_xX3FIdZb5fg3Inb_ObGNu4AHFAqsmWIFsfPE75rO6NZ6Y-SHuwWEYcR8kiYOMkLB8fgwHm6wXFGE74zRL35vMJw4IOF09UN9LeyKOT_q7dltCn_RP39CZUv_agX9G1nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 667 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USeW5X-QaOFF2FuU1w--pqlsuyUSQ3h6LpGESIaKVV4YWQfcxSaAqO7cI-hNfnkQGJRTxnntVNjZulrFjsn4hvptUrvVi04gW8X8oOZP21H7i0sAtR3OohvZ9sPSuJ4bGQVChOSJxbR0VWXR8FJEsnesn4EDuEFZbeFt0ls782tffyOzcmb_Oda9UITUbjK7inFaTZSgvRobuHUye2RWOpoX5xai57LmOoOeltgGuEjaDLI7Nu1-W_1SyWGS3VFp-alf1dlGCo0fbZZ9t-HXIr3MSSyrAWQQ6nIJhSK1vecgbs2eVcl4WeSHqT9l-LmsAJoCrP-Y56kQgkcRUnvm4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 681 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 873 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IshBoj3odZhUOG-fZTW6JopcsLyvqa1bDXyAj1DgLd8M0uosbxZ36XDEA0jPhghYCu5j9AqSGJ0ZK9vpg-Cs8LLS9-taKZoekwXrCenGsZhuV2Jy6i9yzJuSApw-NZYxEXHZFTCWS5Oo5KfKQHzmdwm2haPyxxMkAdTO8lJOiZRkAEw6f1THMt0W0q-Rutayj2A8CLYYTCpqbxFepare_I4YEn2oszRObLEyGLEt5lhVsgsETYPJqTed5aqWi9LxfjLrAG-QVhsUQy8rBWwpcIuj_1c9Me_IRQ57de94D_bg0hmpi4ybpw84vDF2JyEGbiRghtn8FHG071NZPkvp2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GDWb2-bd3bkKR4o56PKgl_Z_Ntv1fCiWW6v4YJ1XBE0U59kWolxgaGBFJcafjk-icG3VDX2xL4vgnrctSuSFSsr0fHBkmn0yPR7N7UzIOBM69oKdJL4s45i1BV4vdHUqAlnEItHoDDcqBmv7TnehT0-BlHj3tF_-Ww4IsDPe7DTaFa--D9cUaZ2PepkV_rrKCLA2J6QXCMqhruvKg4uogwRwvp88KSvmRXptkoSndW4kvbBZT4T_QgQyDYkPE35hsYQUIAkz0rlSiP9a-OMdHsh6VkmBy_IFU0Nl2h9d_KWb6Gt97jvHKPaPQqXkh2T0d3THs5j90jJnnqAkE69_Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 810 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0bTSYBH9jg9vfZRZTngAa2p1fAuB2ovCkCLJIdbennIm2-aZvJMKpowIzXeEm85WqcvMVj6WWfhToRAvOpztAZR36xLTL1lM2fjbvQjuzJXmAYwgDS5NJe27C-aBZBGaCW-DOdttVfY56kRJG8yYHjbh8jGTY7J3fr8CsjxmzyJRCZPMN85Ho0tyEOvrPn1c_l-co0dAiw4WZF3MBSTbEwKWpLlOzfMO8-M-X0DYo51KqjwqVMMcGkhYYuM7ELdv4DK7BfsW8s2qm__aQelZvR6n6ez5GVxdZpU7IBvRtm6lTBqnPbLde9ENiAIoqQKJH9lq9Ww13Q-qMSEPLFpBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIN3xTIaTFE91wvheqnuNb6Nnpr9bRboZMKtS2fZgRMZYYm92fCaMUxcKWxL8sHNpynk_q6EYuOh2bVoJ0hweZVJeSMLgMc-EqovgpeB4jlAGXNYEmOXNz1INihBP5q60M3wTkwzBaHZ_lTiYqU_ZxPefO8ZbP9aPuy9GvLLF3Q-zPAl5Qa9O2uwgAJZwOndJ-60wer5O_sWZPKptBSGFkeo3jO7AVKYaYLfAA3qqI1IjbyDHbU82Y3rb-Hi5x3bBSJMEJIfNFHr8kKbxPrtFzkspB-b_zXcFb2cLPiUV4_kUdnY6wH-oMFVsGj5bdflBOz1wVxqSBuqWg1lu-UkqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReJQ09XEm5xAvbnQSyKxwh4pywsXTa06ts7w96A01pKJ-2fVfIqKtFX8jTMFpQ2GSHevAGkJpRcUDSqfMPAoXf6hQS-k6tx_JauFfP8DbNTfG6rGV_yHxpXQT9J3qj8yIb1JARAzQ7GSCiwBJl5uE58bxlNKrFG078bfHb-fJQIk0zE0CVkkiYicYTQwfrh4v_DylJbquOhmeyNR8QoVJbxCU4Kz6pBY-xtwvNn6mIdwrEPxR8eGGCbfHemkYCgjr-NT_UpcNIx0q8FhloVJ7QBCo4EME_StK1K95Z8gmcFpixyBCv19q9p1wgLVrA-FAuC7FAs03VCel_8g2ykp4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 584 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uXOezM95Tni-DAEW66m3QlJugMSSgHfh7BkdcplNX5wS5-uUXJyVh78ClZbMPHwrV3LEYUKtdjxg4PIautXAQt7P0ooxLXdi7-fmDNomUbdfYJhsj1Oc9cT-dkDQGxWdXK_AkuchrWt_nq-t7F2rD39iUi4CKzlz6iWxrVq-cu648Mw1m-LPR9OaJWk3Kx2JfJVut-iHRCobD9dxOWHwVygf8kk15gPkFKVXWNhi99qMyH7Xh9UE72JbbOY0-6x8uLLWdTNUstAP84yk52e_6r4JdrqSnGUtQuXzPX7zol9l6Hyq4LRAH98ddTXG-wW5ODSRrgBy-L0lSfdlZy-9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lQbFLkcj2spqmqxCQq_L6bfuoc8XAmoy63W2xEBEFd0j-HbVVhmGMXWPptllPfu7W8DzlRDkXfypOu_b9qog7KgzxPx3iUrC10uoZCVr2LZt5WeMdWXVNlCiDU6Gldb8B68ilZ6RoKCU5d-0o-AAg2nFZKSnNehyAZyWAfaQcgEZhAjQ2Srh3Allv0EhLBDfs5s0_rEiRSXiQBoSDG0DV9CqSR0tYSS0lqeZ1L1XYSkbKGrot9m0_6ePpCzpeV8v6Tf_JaRLWB2r88K-voZVhqDONzQGtr22KrWzKObKcJsOnz8sQZIyXuvtlbQ8PSvDqVfOx0hMajbucjIyg9XY0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 673 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 901 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfO8wLIy3Uc8J41iWmDXbxWLYWRTEJuHVCNc3OtTmiPtVZabnTYPHJv9qPP_189LegMIw-9U3WxYi6hfbn3AmSStK3Hjc6arN3cFXFp6FQ_I7JZwUmGalZ1H0lZB0ctHCQKsPv-L-cMvZmkpDCFOxb5k1I9OmsOdjJBzBoMdBKD_PW02U-E67tPuVib-9M8Ms4MkY4v4EoLVZQtYLv8xf3l39mAuc9zM-W57Fs43TzMFcgwMMnaxedEa_hJ9eIOvmQJ1TermOea-9MwAgKP6sGosz9HbJ1U14eWPk9vuZswKRGA3ln5lyXNqN4n-oikUwIwONH-mtUh3X-U5ssxkiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5Nzslp5yKkiitX3ulEUmkPuKISajyh1ggBDPkGhxeNjoas4PsftN_XB_MZc6E_j660Z6DWsvtKYpoPrEGpOVO64l-BxCbvfl4nSZFH3lCsJB6aLQUmcQZ-tu8zSpNagocUmPQlXHksA5-rDRScug4oGGAsIsYc2J5Ie8xubvfsMyMzQe-JDGnxcIxF_347ELwbGtvz5tsn9v5XyLf4ORrpLsLkKD9WfgiVUsNhHfv7nRDBQszm455nQd-DflzDP69pty-kMeo-vvnZBureXrcLw22cO7nDotRxofW5T_7ba-kAb7ASmQu2LeJTZO8JNiKQ-2efsLfXKvV5M3tNN0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1eN91NI5YVWdPbNELfAq0e6KLVZ5LrG3oMlfCi12qARq-QtAvJQA3AOyF0JXCr-H06dMsyEffb91V7oLMq3QZ58gNib7KnZW4hF6dk6WbNHjEDUUHKSXiSBa_n6rewxZqVgavw4cVQFGpwDTPrrbCg4FYToKxsA745_X2kbJr6a08Dn2Y8HwABrgGloAI_IHtdlehPkx3DSBBhHVZ8ExnHoutRifDPKCnANSGPny3Inm0AAt7OJAYuROTHa-VH1htDhMXsShMDbMhxqHJndUiKk5j16dShfEOhA9-KJDdx2d5H5E5xgwViF_ywcu65UTgNLV9WV_oXbuelhmP6AKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khYyfizWC1xvFKuILwakj8nOdk0EmsONpYTjKRGRReuNlBnsvQAk82sd9iVCQ7mzI5xYuzs7DrnNYQpimXqtGYVjVYi72MzkzCvfQG3446p1JblOoFYRAfA4jiiqCQXXSwNayAR6b1cC79ZetsXuTu5-hnrpmMTsxu6M1gJZCoElbjgOfwpqAcbthdcTRiyuz-KsW0TgRdR3-NZWWy8jDjW-wk3zjZVo55adEP6X7HWQ75VKPXp7PsCXoOPBkzG3zzRzFhACdKTatbPosxtIyX1FB_6Z3_KHCx6RQH3foEjOT9Y2EEdLS-qBLesMXBJnTHfXISlYMoR11q-rUqNqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OG1nGxsSbL0weyhViOHsONiyD9SR_hQTatBuIebqCY_J_EHmgd0e3UR1pM_JLj1kxSjRmjV9li0hU5pNG0ThGySsk3rPFAm2Nbx9JzAyKlMP4tgedkYDzRRmXwLAjmGMkBV3WTlEHSRj1pyPDkZzYknCZttYyMeduqD2xpcYh52tsQIHLvke_fa_iJfMaHQskuEPOxwXFQDCUhfwXEWgQFdn1QkDLgK8K2Rw_FSoEbebPTPowON8y4FDu-su66-8BYQMOclrmpCufv9aQIkwecypRPy5HopoU1fRtHnbFu-YlOZrV_gUXGYrHtNpDX5BDwHzq3uO9hR15qBC-XgshQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_JbWLcPHB4uHZErY2OrpQQKZPYykNe6V1UqJagHSZmtX7wDtWHQHXcOUmpcihEpCChu5HlMx3Js17j84_d63XRotMOCjNUtkbDSNobc1NpGvd_S-wyo5ZBvFmvXdXoxJZoHxPc2gFHkepjddq09wvQI7Rs-9TgsRufTNHMTzJRl-TRSKPFBMekl8G32d7TdgM08cKc3BV3Q7scOiYv0kIjM_IHzt-gr1m_FDe30DVKmyommmFH20dxGDRHAhyiYBvVwKwPsz3Y9Q8LnfTStGJCaFuzuhcLXJQpqB7TQtYlmwMUPChVa7Lnd2mG1lI9EFZ5S4j5lUDBJXC1MMuylPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn3iRheIDKXVlBEN9dBRJd7NEp36WiJvQ17QZ5X_tq_i3ZltljeXvQyd0BfaLAK0qCF646Ll7D_8Ncbuz8ncoFzyY_2K9gnxrGrRQgTqUSowbyeQJky4P7ZLKruFicE-NTsIZuRkiXsNI0XlRxmjdKP2AJuLmFadSk2E2wI2Z4gfqB2HTTmdSm3-t9Q-u0_PdwQQXiHWNg45XifX4RR86ZB5HTyvIyBHvWapAXcjrPDV13FguD2JqhqZfRe3gkWny61DeOl4G_wWD70__JmNRcqQUna5hJy2iIT56Gzy7mKXyypZ5P6M-88Fo6GDmrVFcd1nDduBnRXQ-SHocu7vjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmcU5-vdXAuxpC2osi3_XTulvYl7zyMrHGFuWdEyRERoGbd6sOrK-KPHyapaI_xu6QXIkZ1Xcn9xQZYcELx61UigUEaHxbhStdBAZMG7BVyHhsztRYYXFG1iHcTHATsu1037Sp2mqUvkP-37LQdfO3PX3OE-Ae8qNPMLcPeWfabsZ1yrde3SaEYwhq1MJlkLFhjj8UCAZL9GvVY_RxaO1n3ox8kqxhLQoVbciH0nJxC5AjS3Pb6lFOqynE9wBdInZ6Qdv62VWdoBTu_847h10f9dk8Bmj0WDiexInF-m0Z0BMYeuEx5ahc9IX6lDGXkyxnzDwyJv0rwONeU9FdC8kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 655 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfEdLPh8uwsyJojz9-FlA8FS7ha2oU1eBNc6vrHl4eXNGYe6JByZekeLszSs7UOJT1SK11IigYdxWPfnayAWd2B225mLJ3MCDGzCgsD7VyMPUXQXgWcGWKRHGnD87pFCTTjQMJoILvRsfAm3cdpcIcJy6TBzCd7hv3fim2c0ceoTk_00yNpiAc8DFe1Z9LtAK0GJJ8YfrAfiQSRHosbIErwuUYfgdOQC9vn6NvBMiw6P5-URvP5CiFbWzQbeQPBvvzFOdgMSAdAMDsNhYlrZuL2G79u0Pi-VTYnJlKRsaQ0dRD9Bfw1QkDdq6ged1naB33Nu5nxaeyVDMvqqeYxvww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=jCMrDwz32kDtwiBLlpSKC6GPrXYj5HYN-B7h4P2wuqsVQCvlm1u2-_w78PvD38ZgUzjNmFSUYNJWWoLyvZeqGk3BnPFt9-Qx8OyUUsjTK-XU3zWahbYT-HUfCnSqdSK-Mt3vzw-44nFMoyxtFxVjNX7AGtoZMZ0RxwRC-eFJCj47Ftn0f5EeDrdBMUS9LGz6Mlq475zSI2-YtmlgpNRkE1ga4Rq7J1QQihUJGNrvDqjW76mnlndMwywHF-JcoakJvYlFmanLqeRpIUUNkf6FC_rnsIaTMsjB0P2s9GMM_JkkssW2V-Vl0BIjlXwMUwx7FPSypixSn54M9yCNS31qSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=jCMrDwz32kDtwiBLlpSKC6GPrXYj5HYN-B7h4P2wuqsVQCvlm1u2-_w78PvD38ZgUzjNmFSUYNJWWoLyvZeqGk3BnPFt9-Qx8OyUUsjTK-XU3zWahbYT-HUfCnSqdSK-Mt3vzw-44nFMoyxtFxVjNX7AGtoZMZ0RxwRC-eFJCj47Ftn0f5EeDrdBMUS9LGz6Mlq475zSI2-YtmlgpNRkE1ga4Rq7J1QQihUJGNrvDqjW76mnlndMwywHF-JcoakJvYlFmanLqeRpIUUNkf6FC_rnsIaTMsjB0P2s9GMM_JkkssW2V-Vl0BIjlXwMUwx7FPSypixSn54M9yCNS31qSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SspFbmhONgQrgcnUHnKp-CZaxMq4gZ2bq1aQ6NmM_sMn2S9247QHRXkfZVNSnhbxuNZ9gaqK4V5RrMYEbDS_qUuqeehL0UEEjULJ6wH74Bzv3WDGVXM3tZxGhNNX2sMtvpN_T7ATvInxx_lSZ3i4L_4_oFcvZ2d8RH8lFXb1iiUgV7oGP9HFJAhyLEjo207MnneUXwMqikKUJI86y60t1CR3FmcYbtgwon8865vI49YCpfg3PJbttsRI1bzirBQsnowXF6yU3sRQ1Js6jZatuVx8RD8UAm_dlp2R_DYR4IeW239RhKgKgFDXZrKSW3k4FAnqVeb4qJJ8L8AA3iZnfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FB_ILL2ejvc6AMtHNtFeYzf_zl83ZcWGZcktspRW82VeK6-lbM_ZxXHDXUgCmrdocAqLVSjuy2QQTipui7DpfF1OUmLbA73wjjB_AvjHnhxD1WpRkywGvVFBCCHH6rc28TunE-VoUorzn95tspUplsaG3pMLS0g8DWjOSMP53MNIiVzSy-PCyZ_aWUFVjok190Bia7L1Kom43ZflWAYeNWCGcNpN-M-uckFTtNHcqYi7B8E0ab9TxRHLQWTsqS55MY_3o6KjhFhKp-ZC-9Wpe10yA73gq6Jq275G239U0WVu65gvfQ9_eO02lA9Ghtt8ep0Bh7GIXb2BqcOunt_chg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bprTxfPQUzlwWGV0TCwOzwayBCF6sh53kPMjHVKGJOnneiwO6PbQtqpU-lYCY5WWZ1OcYm4OuC5fEOsvM1gqM9Wmvs_ToEcKk0ebRxjprwc5ITazROsgmkDy9KA5YTdQ0h6uuDNzdkj3wfN6IwXrzeigjOCUkIPsvMETJ5GpmKPfAglYCTdMe0tW0tZG_O_YAFn3iUuEp0ZbdGRhOshzeu0bovLf137h0-JfCx_Kcx-6lnO_5UMB17Y0I9PqDTQdbr2smp1t5klC7bN4f338dNJ789MDIqQzfKrfAWu5_0Sk2qrHBJUk2ZQfuANXfAqcE1SeTXmzjqyfONVzwlTXww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3R-xJf8FlvpoEgDCxExGgTPsDeqL70BacngI44jim7Fzb3DGnbbFCSHfBe_loS5RRHKASLlnWFHITZdHvqGYcq_qrZr42H2LMqeuGKUfuWilRzDJYFycuWE2rHupZKh-2P4yj7n80q2Fj5gMYM-144mD2vycSplHKlcFV1bowUc5V-BzU0LRmzHbcF28P3YELWWceYDSe1eC-bpS0plFRrjomOFsR5OyqavdJKo23vjuZomP79pK1PK-EN25m3vzeyixZGI3VgglG5LncArMDtyshyRrokchEGfIpy_pKbbpcb3jkoxu_lxVYR5X35U6RqjmiBlgOH1Syqx7ugM1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6OmJVnSrXpj0R4MZBJitcMX8Thge1Orz4IMVrwzSjiBXaNhmuniIKBW1M0XQ4XJ4kXENt5L7LpoGwJhaHWyYGeFnvrk6t5IYGr6ww5un2yAHnhhA6Nl_zEi7zyY0RYFyCMZDx0SD9z4UeGX6Lo8m59YkArq3QNB3IRyBAvMkfw7tf04fs1MJPwy5tPOX3EHbCWSS9Wi8zueJQhk5NgUk9MA4ZQYgzb2BVFmm1L7ewmbyCPsX6WEfRIOeEF-qKcYCvCR_X8HmEhOELWN0ALvA89fOJfODkMCZzirJmv70MVM5Fq163g77sxDLuiD5Dkkp3F-BUtAl5fc__sotQxKIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xaq064HDycRX1XQ8QW2euZIDFq8-fkdDpa4cf49Ve-tmwstODy7o-zGb2iE_HH9LWs4iF0m2_5yujREkgThyXqv-OAMW4TQfmGrrZsnAV-UqaUD_zFRgcI9-Gt2ZyefYKgi88CzylmVwep6y4jRGQproiZ6L2OFRR3Jblrb313I-wwpru9K1EDhL2arRB-3eDq0d0nwsQ8xdr2DxqDRtIEUte0U1DKAilZymB7RKDCu6osqF6SWZJsrQ7foMD1x5q4ilOiss88Md9vfM5BzWFoK4KO0x3v_jIAI4KMoYwVyR9d8nkEYdrRn81_eZ63IUC9SE5zluCZkOr7oP3i9EzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHk-e4Pe8QrmRh8wJr8J3FMkwzPJlLQnG-wFhPVItgAVP1elWNqp6Xt1h_FBsqyq3TyniDhRzInLcNjX3mZVJ3GwrqBtGo6YyPYP6Q9bFtcvln9sbjASaQ5U_a24RXmxGOlTTC1epug872mDbU7eKujYg3LczhFcXllWarG4i93fx3JiOiRtKaBWCvA2rNEV32NqfSFw7urxDJbxV-6qyv-E_L3tfxIYzqtL_yrFV5gCq9kDxMs7IEpsCaurahx_Hw1h4HWVTuFcpqpjKeSZrLLINyiPaV-Gry0eXFUqD2kbmIKpUPhKsIM7zNL59ZFLmn88zSmHwJwEA35LS7J9Dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=m96lWjskKBTDxa9g7nxlRaxt-kbar0Jy2Matm4xyDQS3Syk4LjDfs5iiFi64ssRldieBUYRdqZ0fYxhYq6utToh7hDWFzBXeFhpfluczYmd1zJJOYaXONp-1o98CouBygfyPdTDoQGR3O-hYMlnXUQq_qBR66XNYvA8tktpY_qesHXoX-dwxu9WWxAdTBvDyTyTVetf7H7cDAf9By4LMz44dcQIa82CFQdVGbn9GIsHfIiRHoW2EP1Xiejo2k_625r2N8KePFLl-tfBekISXVMpZXE2MNtCXBNv-w8UoSDeHt7xdZICzYrpFVVjuYjjsjjFHtb4HFA5dhaFCOrUCMmtGxxZl5IxzJvx-tIQFCpHua3qXlb4IcoRDBIU08ae5kPm5Tz2ahLRaSxz2tJEc0g4T6aksqQo1gMIapk6488vhpKdhW2vvs3E0QMYgzl7fU1DOjBuIYkb45El35c9ewpbp36JB8nIFQhqbc07M9RUSxi5PK4-PTnHqWDdVfWC3b_Pdw2GVCSa2s80-xP4TK8ISMX3PwsYazqPUB9vZgVeCOzWPvIWlCon3tvnA8hwShwu3AUecVXTH82k3Sd3FW9I_5XbLSP2C9UcTndBt7y_WlzFdbfP73LSgC3t6q_3g_UjyISf2yzFy8gqIjdlbp9U3CNHJzZeRKosxjuB_QlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=m96lWjskKBTDxa9g7nxlRaxt-kbar0Jy2Matm4xyDQS3Syk4LjDfs5iiFi64ssRldieBUYRdqZ0fYxhYq6utToh7hDWFzBXeFhpfluczYmd1zJJOYaXONp-1o98CouBygfyPdTDoQGR3O-hYMlnXUQq_qBR66XNYvA8tktpY_qesHXoX-dwxu9WWxAdTBvDyTyTVetf7H7cDAf9By4LMz44dcQIa82CFQdVGbn9GIsHfIiRHoW2EP1Xiejo2k_625r2N8KePFLl-tfBekISXVMpZXE2MNtCXBNv-w8UoSDeHt7xdZICzYrpFVVjuYjjsjjFHtb4HFA5dhaFCOrUCMmtGxxZl5IxzJvx-tIQFCpHua3qXlb4IcoRDBIU08ae5kPm5Tz2ahLRaSxz2tJEc0g4T6aksqQo1gMIapk6488vhpKdhW2vvs3E0QMYgzl7fU1DOjBuIYkb45El35c9ewpbp36JB8nIFQhqbc07M9RUSxi5PK4-PTnHqWDdVfWC3b_Pdw2GVCSa2s80-xP4TK8ISMX3PwsYazqPUB9vZgVeCOzWPvIWlCon3tvnA8hwShwu3AUecVXTH82k3Sd3FW9I_5XbLSP2C9UcTndBt7y_WlzFdbfP73LSgC3t6q_3g_UjyISf2yzFy8gqIjdlbp9U3CNHJzZeRKosxjuB_QlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8TsZfVGdUiWpCnGKQB57NIuc01C3DqjAc-hJF3n-yFlQDadv2UiGwM5S8i8U7tc3Fd8hvVodjlODOfufJK2_hiyWLkywHhssYCltVio_OVuW7F9GYb9Vq7OkBsox2cR25xBbzbOTPVlt2j6NZlsuwnooUCZtCUawT2TaPDh1qj8vairbbCNWm_qFVTUf46zBloiYvtpjT3XbfaTffNsFI97ZLxiF3fNNG_7led6qsuIkez7BOXlnKIVfDniGfmy9u8xsoLlvJV752Q6FSQJ4nRnyjZaKkajq-VOg9VNAbmqTcyhD9HOAgN9a1ThPMhgT36yxbz6H01KrInHX1IcHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j4JCSd-CoyqCWlnJcZty5OZVx7lRIncESxpmFbLIyFAyvrpLJRelKrM9Vz6dvZ6-het8Sxqieu60E_EAbjQ7cpKcGEXc-PlSjzCP2uxsscVA68cDR6Ed2P70CQk8HRTLdhXtnuGel2vpdzVRVUDmQJUbcJ2mLEGnUY7vwRvue0MGeq_83wN4-L3pI1udyqu9OtKx0_JZUZAjAjH-dA1fwldUdVAbGbmmWEciRwdIu1b2E0Pxr3iI3a3B3ZAX4I70zJVli3uX8KzvsGoYlojtNyGPkYyA8kyVlzCTvVkQwlANlVO4DkRG1wM5cX_3FuncSUujuDLtTTnZ_Wf0mTt5dA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbC5X3yvGkrbJlQjFgL_I1cDewCP_3at7rI1TKo_vp-MJb2sjZfcY85UtKH5e8XvXX0DD4I4he17_SVdaFLlOcZZ7GncMX3nIQ4aIMvQrGEHb6KznW37rEbw2l_mEFWllsEkPl4RzxLsQlHv-kk063OXUOMzvacWixe6Z82IyJ48zYFOfkj8Haas6saNs2XGQbHLeKFgLbcpKouzhVVfjCkE1_BnFs9EXl2majBNZcdtHzoqVPAbRHeeefM8mnz5iXEtKfGMbYXFnjr2KrOP54d3xWy7UyZKa8m1vuLMQT4ynQYw9B6G11IwdXkFJ0E8DFwE92iH642r8WwavnzJsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGsLFYd3TmGNe9zOEOQOqtUBlx1Iqs_4NRNp-nDepkoNz9o5HpD08x8SALEtHZlC_AUcxrfro_ErJ6OPMHmpJ7o7fBFDqzAQ8rOn8OOapnhOIfAEmHPekLwMgP9VDjUu9dxBc3NLgiBwb3nPUB65zkJlkLiN1uclAGQuEAtCvo0tGEhr2z4gzhT43VOpjSo8GKjepC1eSMAdI-JXD3wBkK6KxsHwubd0xRli9cfgJHqpVzPMlD9qcmcl2XCdJlJYp-WQgu-syujvMQJVHsuqV9tkDazRdEi3mGK9eiDLjgRMJJrx-8rE2_Kxm92CcSjxc50VIdz4XBigkgObHJqC0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Me9y6LaZnrGlQqmXvo9B9Uz26_hZWaf0nXngu4kF_CgRAxo9LiR4KOpIgsS-xZgqO0uP7K0GPdDT2PbhyaqGotaX5Xi3qi23MmYp53-rSSy_aj-Z1BjRuB6mmhLA0uuKkmpS8jCgyiPwvb3jJ4PAKjGp7NIOOoeAgQ_d-uZ9UKmZsh1BuFkmhj_WqIDCsD0WFu__AlI9XgjalPr-e-6Bozi5OuLo0XQq-XhWYUl96qdxpPWtbZhiuDYw-9zNcgScKKd0pLnmVjgGNcB6-PoSxM6WPFgyTxO0AH4gywcaPoRFAWw6RFM-UJzi_Qlr1ZsDEUgCFX0WyU5bHVSQ5h7tzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0VbOqUYuYxusAez4LVEyd-D99v4W8I35jNdCo0gM9QDiUpG0rillpC9f8moY76T7V-BBP8ja7NCAYvYPMnEZyj1zGAtKsBe67LHU-C30a2gGHfddbvPmBTuhChsBEjjnepvEqEuP2Tr6SfnJnuPBcIWhuK-I0c9A_aFl_5nrspMT7UhLnuTpElLlQX-fM9y28vmmUrV7PY-b3ZhpqUx56g6m3fm4o8kw_ECJ-n27pj-ybidlaCmhfOigWEMcAw26vs20K8mve-rBTn8xgKleP2BNHg7i11OEUO8ArkITZFVjtKvdeTBvnpHb_k3WGdfyF4zCrILvn_yFlsbMudZRqGI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0VbOqUYuYxusAez4LVEyd-D99v4W8I35jNdCo0gM9QDiUpG0rillpC9f8moY76T7V-BBP8ja7NCAYvYPMnEZyj1zGAtKsBe67LHU-C30a2gGHfddbvPmBTuhChsBEjjnepvEqEuP2Tr6SfnJnuPBcIWhuK-I0c9A_aFl_5nrspMT7UhLnuTpElLlQX-fM9y28vmmUrV7PY-b3ZhpqUx56g6m3fm4o8kw_ECJ-n27pj-ybidlaCmhfOigWEMcAw26vs20K8mve-rBTn8xgKleP2BNHg7i11OEUO8ArkITZFVjtKvdeTBvnpHb_k3WGdfyF4zCrILvn_yFlsbMudZRqGI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXz1jRqK_NQyPJ1cu1Nwy_LIsLP6ex-J79nT1B62d0SXrfhuMCMVezpKsOtmHzOe5f7FgpB25l7tkscenHMElM8JXPtxfm0Q8untGopjpTPQlOHGadrHTV_xlgf_ThR2srnWpYHOEvhO1Vr4mAtpo_-bBYe3YsEKXIrROzOM37i_mJFlwGQaGEVtU2YFnbTMGyfSvjRJDN9jCZ2BJPeQ_HdOBUeYqNmOzWOQ-xWDImNY7xRQJ3DxJL6u5xR9ghA9QzXzBaF3DjLmHZPSuGyG9f9cBjrxcLKuG1qzssCzM_b2YW7bztYGF-jFaCJ4vNzGH-nW3ce_bHwUD9QqRBmR9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMiSZjWurOcTenuGjPS_ykzCkHxoDwvsv4uBmATK_eOQvdfwEt_8N4wGYHyeUUwHfsdCPM0Utd3JPZuGV9veI4TRdx9ApnqyTZqow8iR1D7L5Wnjz92je3Lk94PGJxQDQMCwvPPCd7lrn8mbHO-lWkGVSbkfEE_yloqWKm7uaZyhsfk7ZhigLNynGfzD-J-Xde4mVe1kLHT3tVYozvWSxClxE6Lg0fbd1eGVN0zuCn4e52-xQW0Y-f3traG3PBD93d5tBPxm-MlDsjLT7zdUg4AOaWWQfjE-toQkr445up10PWrE1r6ZxfL9VyM9IQ03pNIqcZ1qTC1aCGXAz_HM4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
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

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MY8u2o_eR-NXHun5wseXeeDGMogBg41SNXHhSze8InQJzT9EfmS-vrMed34OeM99AA5N2ZtjZiP-o9XjxY51S0W08-8QjeBSdWgXoJmZO2AFsbQ_08g7_iCAYA46KxB9klpqd1-jqXpnLEZNGyzkPiocM-XduVmegxtJmJslA4SsrzJQTGqb0Jf02H9Ot4Fls2WeRhfpQbTE1vPF85mFjC-BCaG6fpRabZ7Wfe4HSONYTV0qsdiSfa45LZX8j93xRrEcMbDpoKep8vK3TNB16P1wYOXHEyy5yu4fCQaKVhQyKKfy-zS84cVtAW-HsF119cogr8TuqzW8T7ys2DSnFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KuLLqmn9e9joGELnZm4za4gd2HPwWbFCawOv_wgHIaX2xp80wpO4O7C7FQCL-AG8_Kysaw7j0inETZyJSXfKrXUgV8D3Nhyo-S4CUwIgs8k4VY37d0zqMrhj1Q-G6QtguKor_7-dM2SKLj91eIPSyFVBnzAeSN9cxiMq9wU7k6JcIRlOF7A3ZYctD6OsYWEhGMXNkuadMoeskbj-pQwRlYxuRX0P5m4OpKXGkmsbxhYDzmxaRgKFkbITASiw7Vd9Rbfgat4-Tbq-J__tdpflM2U0ELiBySaEc3bhrVO1of-gj0ty4O3yV3Ycuhx9bjZClzEtjvV-mSWQgpgaxE80cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLh5wXkJijClKcZvwn0HLb88H1HLEjKsyG9YEk8tPTh4FV_gg4gMCJML0s1-__CEJ_TX7_rc8pEC2OBIDRV6jeEv8_Vg5ZcGCSqSTdJzCjeKtv4Z67i6EkY-hd70i8rrhX6nfSQNC61e1jya0eewYpaOq8XF69wyimw9oeSzB0DNqgigfvCjFrZzEd8KLw9PZg_ogpIEvjjPoMNlaA0fxrsiv4RZKlrp6rpk7MoCH3c2NDa6Q34Dc1ThnkPdVujNRwCORK0OrATSNO1ZbdusOgDPraejRbJd09zl93ms6Sjfpcp27l4o7FpgaPXVDm21AM5Ydk-qSb3PrXHYg24VuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن استراکچر دیتای قیمت خودرو در گوگل
💢
داده‌های ساختار یافته جدید خودرو به وبسایت های خودرو اجازه می‌دهد تا موجودی خودروی خود را برای فروش در گوگل به کاربران خود نمایش دهند. همچنین کاربران می توانند در این فیچر جدید فیلتر هایی مانند مدل ماشین، وضعیت فروش، تصاویر خودرو و قیمت آن را بررسی کنند.
⚠️
در حال حاظر این فیچر برای مناطق ایالات متحده در دسترس است، اما  در نسخه موبایل و دسکتاپ نمایش داده می شود.
♻️
به علاوه گوگل در سرچ کنسول، گزارش جدیدی از این ریچ ریزالت را برای نظارت بر مشکلات و ارور های این داده ساختار یافته جدید راه اندازی کرده است که این گزارش موارد معتبر و نامعتبر را برای صفحات دارای داده‌های ساختاریافته برای نشانه‌گذاری فهرست خودروی شما را نشان می‌دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/danialtaherifar/808" target="_blank">📅 11:47 · 26 Mehr 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
