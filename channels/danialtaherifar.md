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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 16:54:32</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 213 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 266 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 325 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 475 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 607 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 718 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 815 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWc0HpEUKI_Xb1EFvqwXPKAhekP9CapJMUlqYwbyOYy4sUPM_bR_o7jIYFSLFm7x3uheEy5Otwppvw4wvjirUTf49Ech6bL1zyPhhA8PTRY47Wx9Bseui4W98Sz4gcoLTeUi6OkXnaEx3N9ab9I6Yrw9bPDAWbuMRwv5hmlPf5UZXT5WV-WRjsLJ16ZM7zHNjbixkA24umUppY2w-R3r-I5XJhplxLgXv1rxPA7-zQUx4OyrE40JhtUDsztzKpF7EINRXN_8ox49d-CdPePqQ8BN1D52YEZas03tFja8ewXPM4VZ5QAU0Of9_q1BogcsJPJeLce5cr62GM2xz7xIbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 849 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 967 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 907 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 960 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 872 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKv4cLUwrBP-ZHaF6S71udgjwOIBvsptUsSmi860zOwuZR6I8N9y5GH0xm-x_PQevd5SzeSTld9M-jPSxQnCGk7fPosN1grUgmRN_N_pVLg3v1x6-hVwzoowKhyCjfbjW88fzOTHHkoblfOkuOr7rJXLxbuH3S99hskkgJ_cYCNIRPSljxdpV_Eox24tesVThZOaF82fj5d1Yc1ZQSjqpmINGhUuCxdicfgoIl0pBp4Qi1F12Ha9MhVsd5r3s-MeSPLepKD51A5C_xLKG42eIcH-x5-cHW3sXQfv8wtk0G08_2gVO3cpz_KnsSoALbF2AdzY1cMJY5tmNKPWshgz3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giJhDH9t7EQikCriKCEHj37-GN_zF-vXv8GgpsqzarAdqHvxb9eW2rd3ERZL3a0i-6kXTiixCzZiNJ-L3aQKZIzjoi8oi8wagyrJClu0rcK8jj4iww2zS176IszQ86PEWgsKC-fOijCLSX0m6OmfPu-sJACCmjEywYqQnIGbR0d_BJEQ1QWXgjORiXxTTW0wnRK4IhnuYPLQzdLpFO0CvsclY53biY9ifih6akbB6DdoqcsJSluq7dKoksMC3FEa73YQ4JY2IdKrtrMztPgtEe2qvd0ZXmSUGdIx2DGQ2NIgvFTbPMeD0PEl0QvXvYSYzd5_uuQl-jT68zmM-fQAEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaVnct-0FOI19NCKAgcIhBIpdxrfkcOHK8Nb2xSYRLPCkw3L8DkRaXyD2erPDQKmVpqIC8dQfNf_nGGkWZ9A0Yzkeoh3KIVqoQg8zMCnR0Iic5i6qfayA20o-rQ962rZFqlN6tteHI8Wks4fUvvOJIZriNWuXVbeFmw8ZKU37wxiNq1lmJFYkWa72n20qsihFRosZvDyJgE5daTontkXdXuNI2r4Ct4Jfs2i2LntYQnCjGJaKj6zxSqWhjANsQ5nQ-fTrLFdF1d0h2x4-Lmvs3fH3hS8kSt7aL02xOkHKSVUugmOoOy5CXenjNJ71HvAdZi4aPwC9LBdmdN4KlBGag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 846 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GObrVSHmO7wgJTOQOL2si7T8UCCAbPIRUs01bzm0XcptWejTMgH4Ybe-BA_xO-qPFkeAVPGnfV64TGdKrw2O8dUYo-wK64UJevMW27c43ygTKWz2pkQ8NWZAoWWWgS11RmpBEn9ilHGvcgLSKf9HgMUcuKm-0xjQ6yl-hCkZSCs1c4LLmKugoXqWNvjmg8B8ZvA8IWB8FDR_160z5U1x2OtxgBeJZvvBPotQyBTcFH0aLTZddphLlsSdvn7HanPgqnJYDf4z_tr8pcJJnYOSQ4cxQXJyv2A72ZwoS4q_Z38m_rA2kd9W_2LheAWFeoV78wt_5hjnnCUDqv68OjlU5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4EZpxQpcNlZET8gRSrNtTWh9cjU0lmH7iMRca9Qfq9dWiX99O0y8baMhIK4NwKRTCSVmjUZi1mH_ANgRHZFlFqj9PJmvd7Nzb-Tc41t4Rlyd70e7Z1n2nsR8ah-apAixMVaXKklCMAE-KHGNS5DFIg1SHx7EPdju4WhcDwjBf6CyOEviLCfxEBTbNsEKDrD6-k5tht5ojzyrNmP-f_5oMJ9ylNBpkPF9m3XWTHZZAZiEC50G0Az3e7izR_gJ7Kq3FeEeVCKmQIBkm0uwut-LzvGABLyEEm5_I4sD2ax5goACj5AtaVUuBE9Pkzln793j0M5HniGBkksA5re0mGsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/my93Qf3O8Xj_C_K32FtvOb3zuizsH_z0R6hMX68Xw3p5RJDgCj7mlwZ4vFGN3hElGV-hiqoqpwxIbV3NIOK4WgPKoc-e4XGQyYsrdoUtKE3zsNx4D9mzVNK6AZJz2QsL8-qIOanp97cZa1JqlHEnCAl6yduw5kgshxSjAwPgmnsarEOod5KOREOCSwZVU9nSqyZhqZegQHuZxLcpNsqrSoFzMDbkxZCKgwAqyxqcGGA8Sa2B90cge_d5gGDgfsrdOyicUlYr6IrpOgLdDRSVOPt9OOJ9j_9MT6Yd_y4D-_vOgfltCEvGD54OP9q877AESVo3Ns0xGCakYepyMt3DZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m24KMcTcYUaE-H56hP9azpYRjs5yu1LfpTl9kLG-h7zn202vewQzUzKl4XQ3qQblWSVGca8_MaiUYi7gR_VyBnehi68gbV9yhyNTEjzsbStCXHrby26N6uPL-vjfuZFOk0vq-kwUV1VEstratFWvuCXpGdZyLyZiuXJGjHi0jTVohyJGmLHs4zBBO1q4zM_FbhrybSpGWfPhEoQSqC6_ykP1cAJtoEAgnyU8Qx7SjhROEQcR0d_pMk_m1rz6jVh6-4ZIo2L6VSVJk910MuEHH_5GACbR0YkyZ96MZca5DB978PwWZhJwIeYQ96gEav6YXRsqsErfPSwwr_tw0etppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2ets7jnsrxellwUPGxnE58PIv3exAmWWIHRnrioLuprHaKC0xy4YywYv8PDxHDPXPFtAXVLFoGL9PpYeUpwTtVubzzxANnozjGzcRoOZaKThjXBLbaEIn7ok9096PQLBkKkOJo6XpOC17wx0OR8hjxQ2PN4-S_HXs3v85mEnqXfu-UKTr7GomLSww-uADYaGiFJ1ASchfVpjmEomSlYh_lz7yHJq8Q4PQ_FLcp9ubBhL6LJBkwDYTwFVtlPJH5iIw1VGcbKpNjAGPAzxHOitG1JEuDCKv4BRUjwx6fJhSA-PDiLJmCn0oCZ3cUucln-2PW_VoyaYQLo7NDx24WxSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfSrpi164c71DZBcU86xE24gfguSxxIP88C8QjPlrH6d4-GMa5fS5c5GCqXf06-KUK_n5vc_58LxsWYbjk67zw34u4lsVIz9e8znOT3kfatKGJ3f9Zuul7qYrFzLlv_RXu35do8fAc0S6sajsAZEbXBnaT28xej6utogEVL52IQWp8rSE06OCUW3L6xzOQeiok4pcR27suiPfHcIfgYaZW1x-alz9SpymrjPWdGrBFLUuaTfGn1MqO6i-r2LUwnWc02gBtez0uNtNiHDyhgOyBU1RWTg2m8qeNNd0dqPxZJhQ6mJFykim7vCdyyk9amZJrsHtmLwf7pNvzQJATpcjw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=tkTlXtodynXBw5LqUJJjfLDyXvHj_L7dKT8U-81rijt37BjBRt_klR5RgPNcVoY_nKP01IuDXQX30RU0RLeS5vjO_YCzrLPTDnLGgBbVO75TIc_LxQ_LULTnFr7PbgeXcVtV_sUu21CMoUrAamTQlGg8V1py7sAyb8GLFum5jYD0WtmEaDAfuvSq0mbdX-DN51uyDywcAYG8ELcgQkSZFBaM8I3Jfzr5RN4w55yAlxZIRBaQRWS6IY1dnIkrGJau8iF-R8NvgIN3aZ75ZabPGvlpqzuvFa_BMiHR7EPGql5WkE8gBpVUI_7rwgigaMz9aiIc9iy1hOnF_QO0RECL2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=tkTlXtodynXBw5LqUJJjfLDyXvHj_L7dKT8U-81rijt37BjBRt_klR5RgPNcVoY_nKP01IuDXQX30RU0RLeS5vjO_YCzrLPTDnLGgBbVO75TIc_LxQ_LULTnFr7PbgeXcVtV_sUu21CMoUrAamTQlGg8V1py7sAyb8GLFum5jYD0WtmEaDAfuvSq0mbdX-DN51uyDywcAYG8ELcgQkSZFBaM8I3Jfzr5RN4w55yAlxZIRBaQRWS6IY1dnIkrGJau8iF-R8NvgIN3aZ75ZabPGvlpqzuvFa_BMiHR7EPGql5WkE8gBpVUI_7rwgigaMz9aiIc9iy1hOnF_QO0RECL2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXbGJ63ZBeYHZiJKeeiDI5Ye2VOd70D5Y60xfzrzoQr2hjTZewOSogXwJMl7rnYy68tMigis0BMpgVI1zvTDHchfmVIDxiUwDAEtph-iDebPelBIf_h4vANbY61BGq-TXJBOxQ89AT8WuzBRca6LecJaM6CyjnFDh6GdCEBums9fJyLYokw7iT2EAE21BWELlLHCoECwmTr1FqmHhYuObDeNT-Juj7wk1aRN46Qv5oqjwIcL1UPgvOWIpQeYM00jS5uqYLD1VXcmw8pv1zJYpZGhmVB9O8P4K9qEmoE8VZz-OhjzxAzGfu47pr5ZlYwfTxxsuqoZCjkxQG_bZ1VTrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcJTB7YKU5K5IcestpncWjXAauNL9_SP4mqbCVe0KxI-uJACFmBWx6dojXTvZX86_dSZ8Nm9lDiZDcQk_uz5oqrWNTmIuC3LehpUVtX0qWPG_mxVhNpY5OlBh71z3G4vxGIfVDTvvIFnm_UULSOpxTe8coFxfwy2iCLVqr7asCadSpEBqhUd69BSJtCAooS97yI0GFd28To6nJ0KhLAk1Yd7jN9lTs6kAa-4VuZYDLlaGBnoIY0ARY3vA5qa0XCV7HNEW468L7RNSya700MNgjRpa4RuuXwSxK7pt7z7rEzPm6ESac9sG4_hRbqXLfxfZIXzsg9MrB1Mm1q3B4Cq7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o2Phdao8QKunWbeP2pkeF69ieGfytwXh-dXlcjEQz5tLFNQSREYO-oavwXhlpRMfvjF5R4TbjbrEGfUQ2gbJNc_fEmFnkdaYUF2h8SK8h3wGwACwv8TTlkAL40VAZlwScpzntHN9z9KU7o_DzjUPYmx5qNt2ATiGxnW1gOceoFHYmXdDm0IYyom7ylInEWLschYAM6D1RcAu0pZXX9YOtpDVAYeIyXP1R_Y2l9LTkt3NYWenIQ_5yuQUWEUdoYG2xIky6O4not1bYXedylZffTx_NoUYPg72b03NcJsSIaDdSWyaV--zyH749Yetz3MqC3X1vhBK28e82JNUxm_Paw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNDlS2-OIsz8k_UePaopTVtqDntRn_zC4b0K__Q_WiP8-OkDTzaN1-BcQ09fCYtk1mREv1lQeByhf85r30F3eoTdbjbNTcuJx7CWiIR3Tq6JUgiDkiSbO90Euah-HRljAL9zbpfkE2tZ6TP4lRytm4ctt9EHKHvR29FQee7o8dTlOjDeuW58HG758n2STJf6_leBXfi398G9AuRgJrlmJEPlcnF3eVUuKawRpxsMG8bW1GV2bTbCKZjAHP7SwCh-nk2fbS6ztmYJOiAI3-QzGkAMbc3XAhIr4Vux7oszWpOIiB_vOov654chRPgNK83vDAWSCXF1HDaoeQ0YIEfJGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-373ebTjJWTW43rGXfQJLi1LnOlnG5loDysOsjSpbFCS_4bhwf9YFZ12NLI3YjkywAJWn5sHtwDQaU3z4HLTIEAGp66Pq_PtlLWNVmtV0izdSuiOUXjfBi4319z3c4T9STeAxDo2cX5YfqwrKLkmzp8GTysZIq7p2VWjUWlSOryc_ifjRpl6Z3MgiLVcqqBn3-D48Nnb5KOXGVLRwt3nthTO9UsfgkimKxU9K6QEs46cmUK_eSbfzGRcFB90i1E5-c_DyfiqgoQsNTlbSiQC5JzkPXw78CvQJVZ6aYqVoZXR99Si15Qya1KdvDgf5c1_ScezOk2DQWVNE9qWwk87g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMmMdhXPbJjH8cIGLUpAS-nQ6yW21H5kRfvqbc5YjB9YnItb2ifAqjjYH05pYlMLR6NiITv_4jorTrKRJ1QvZwDNchIXFS0vYYmADIJlRIzeWyDiNK98GlAU8262sFxHdxEojcYImmqP7wV91e2lBwgNScIJ6-HJoJAoYvINfRlV4WbRakJUi3n1XSA8lY1X-fBojJN3Ul0YVKkd8it80WrGHrXrtYSZhtY46sDuOvjJ0j4coAMvag31KgZBLfOMxNT4yE0dH4UXGt6rzbNjVxPmwnt7RHP7SeDBCcsQm1Yqic9hJr8gjnl1iOPRqGhrl7WVVE3r5lrxHXaIN1wKDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LS3Knu4U1Rek-dNvZkHaooP7e1DBnF7lDpCOJa53KMIMWy8cHyzWByw-b28cB2hNQazLgx86mhL7bwpZBEJg1QywJ3tQJX4HPRq0l4FaxXAWM0S8VrrkuiXENVzvSCm4-XNukBJrRNnvD4isrTKk2h2JtyzPopm9PC4tesWDuu8L87FmxenvmVl6xvYh0x8tltbYmbydjKZyr-3phpQUIbZ9Cv4xPnh1NCNPOMP8QznD_U2QkMSbkMKAKct7SUPMKXtU4oT186CWBBsYaAYARBPmF27eZ3i4S0oUk6PgKAEUa7gqaz_W-ZcKlbkm3IJvcM8vgzylSRv52ym_ueWpog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvRotV8fqxoQK8J_YVSwFsMM3uJoBDB_x-8usb_fFd4DBZcXNmvgmy8Mx9bHOwRpEIC3EBgLt-la5wQ4gdxsznaWlZmm6SSu-VYjlqs9UPWJyIaZwaBje788w9H8xnYRHtKCYZvBS8yTWhlH8PbQ5YGSyb21ob256RvtUe62lDeCL4dz6mNfHm757KgTJ7bADF0R4zAYUerJA74dHszd2D9J0IA14e_iJIgPWJ1RwiTJId_jWIlxFtTApzO9xD8GgYComOf58OXhXJ9rthc4j18Kae3NQP5-MbHqNbuyrB477Sr_ZnNOdRWakDeeacx4rIORv3g0NSuCoS-3UC2R6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5yJQqPAL9yM1jlnpS9VSpqbZiLLsxweJPIODF0Z1SfjRe4oz1VjHQBzjM3EwP0uyCrMD6ueIxMu6ygYkJGVkrARu87wIBAM4as6IM6LlUtjHWuMfdj8rElzXBuH2uwHA7hK6KgKz3RvOKUEmCIt9_w_ARuLIjfIEGN8rdHoCjp9ByuJQa8Zc_TFzg35PJYlRpW6LA4R3Q2EYRy_Sby_-RPXK0PRzIAdHOaIcVi9u76N_L3pv_Me_1iQiQ6Bdy21sGJBbPOL-8hRwYEB0wa8EJvqFspZHu8mW1IDiveUh_4tbBP7-TiWPjIPHrM4ro4VLu85s9M8y26nLYHWDvcOSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyJm8O4Zag0UpqmNPtM2YZGEj5SsSujqtex33XmVEHjMf6Z2z8iY1GBKvWqz_tsw7KOYO-R8HI4pVWxKaG9l_4iZUnxsZ8hezma7NI_AMUDFiDPPdNwSGhdnmCDOxEYdDgaFUWkxDZ3KphmIY8IqPjHuTRhzY7mbrLBDkktpvCWx7m1B9M0Z82zaAtbj64XU7Na_ROYj2-50hQeO07ngy-be9tZuJnuis5GzuwwuLPPto37am3PfUiSfwZRujvrUFmg6KhDUGQHSksbFjvOqG5Bc7KqryQDbmJ5i-cgRUlatyQIWTvsWip1u7BpvVStXltqfSh_qgvpdMLx_uFdSiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuVyTOGApNa7_pXfTD6JBGDz-tdUTwvayCZnAEwAMVmInObrYx5jNeE06o7vv1TSRhSnJum3uvJ8ejVDTmI69rs4IfzsEB9JbX8_jLQBcGYy4rqFtD4t7ub4OGyvTolBywezyGO5C5Uy4ntPVpUt9Ja5woW41GGMiIapdpqSgEpU8iLLNSGl-fvSUkPntbPqN05rseeBUOjVEFr-zz_OYegx5E5gzgKzI3k50YEekocKimo4XWzLolgv3Sr2XQS31C6_KYoLaqhs-70idU_wnOb3T3m4RZC4SFXEsP72PUK_jqWFSAuckq7ToYZfLox-uNB_1GK3aW2XRl_JH5vTeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzbAFQ70WohT3Ej2dJ0YfDy08MY_lPcjT-SeIbToE8mKaNYOBJ-AzULENkKPgVyn5_2OUJVVbWDYRNfJ25yLNRAq8NRTd1eCESpxFg8KOn22VaeN6HG1kmRn3CO8Gj5GvwCLjdFn29k8uy1Q4pAPc5h4lWHkWpUWPVhNWDnM6eUyaf3c_PjJU6NTgKYxob_IeBJvYpYcDQxH3OjKFdKwSoEBjOfCnjoTiXBA4lwmvjfhr3KVHet5hzwlvLZLNJepQyEznUI84JmrspMSUeeLWOaD2CJb9VE_OTdMeK9Ri6BJ32LDYA2l5GPzKiNkoLPJgr7ax9JMXam1ejO9FJ_vIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KEdPUprjF8JgjRyabjzhE7hqEP_HprKFdieR0u4iOwyoI6_vOnqfeaHaQXFQNlfEU1jhtn1xeUcpURapVQcIVdn7HcUfOJrLutqS1bq4NdI2tnqXghc_9m7tIIMoTvu8Lz4HgRMupZrLu7lNAJuuKR4vc-Sqm4hpUf9Dwq3yWhlUIEHj0-D3_pom-YjTNCULm3P5bEreEuS_apFSFSNrDmiixc3eNWy7OF2Dlvtem0gB6CccHD_u_Ino8GNy05JNEdAL3P7pYzF_saUl5vIpRXn7n2LGXLDSBJesnWJCXahlVWWzFmqbG4k6Kz57fbULsJpPFIEXFmOXoM7wLYTvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWsF7ziNQbloyEBGz5E3shhROy4vZjtYM1MJQr937yJZdbCZ2PFGEqxVwDj29DasO554DWbBZzwE70eoYiE2EkuOi8wCCj9GbQW4ncgX9wrZFNfBIRjEjFRVBaZ3EY-JQcSILyhDyVYmBov17PCKH4MWNqyIvonN0mAVahbsIVgp-DZIPZFd9l_3BBuUk8t6oL-ObKbDjeMzUpoiaFHUEvttBusyM-r_wK6638YskbSy0qH4vTrsoESh6trehhelPvX5_YO-KglIshqv7toe0ka5WuX5Hzpn4vm8VcoTpFAg2Dl8Jnnf1ZA2XvXTAMcTBz3pElewu3A7t8Z_-zAP5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WyfDX_OlgvhfbA2TsfNeSto5pYI95yqF2GmcOUVp_aQMgsSUR6MVjOBY-HSSPu8nuTgMUZlXaUpUGNcL76eBD0iUMlIzCXbz4XVJ4xOxzUpTmUT-mH19_dAtR9clVWzGcL900eURkjbf4bvzcnQWNMckXWaBwK6SJrDgfZKeniwuNmamtPHgAJBtAPlqPDwFkVhNWjmzpW5rfoA-uVa0EofsUP7dxy4xy3mRWofriIFUxpXtlnmvX0WIzTQl6hAy9Sf5h3ykfq-FoT9HsjEvsxpMCdvpx2ostIF8r02510NstRQTkpplWbwVxo4y5xfaFLvUUlj8_ApJuCcFnaDZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0Ts5Vc-AC3VQGpR53AkJtAEVkuU2344h1Fsuqm-6sygl36NmNPECd5gkBJSqsNajasooYLNqWnXJ_qwGXK34cY0x7M5GBcMB8DEKFH-0VlTftFyG9B8bJ3C9ZohpYWo4Co6Pl0REH-8DaEM1qwJLbf5zNDe-c1rHwlULsQtXphmd4QY8kDQjk0EntvpirNVMkvDhkKUsNoU-pr4dnOaKHMVQGpCh7JlRo7_li5X2e2jcu7du23LSmBuju3E3DCGYq5TtXP13zfHVb8wOrrmrdg0ZTv6sUm2Dle-0ImLYjvkANJm6CXWhgWDS6sHORzDdB0KTUxYnPyW1ukUpPaaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUiGvNk4vZSDaG5zODxb0m9AMGPdXJ9aIiIhfUUGDgxLjoGEVukVllO4H88v0L1xqWuNntEzp29kBWdo_VNIlNImJg9Wf68orjhmjfeLzFMtcTs6-26_l5GnVxXgRnWoSE28fS6iIxzFLY6UcRS21xGZw9rvp2cI1q-u4HhGNToUsx9qJm911_02oLH8SjTsBXpyWgKr4K7NPIHu36p8BbRBiDNK8gBChkjeJnSlHybzWh68x6rSECBv4oKnZzRd0YWOBDrjXw8v1_78fc4ralJSmH_JFJNxKzXBfLA31jbO1SKg28WjVJzHD-ZyeU0ng_qCMHUcDHG0M4qYKS_rnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rt28UHn1V89mjnh3KN2nfawWVuVeNBs4B8UPRGBcDRLxbjG1omaR3tVPu6P6nII-BO2n36VO8ySWcwbHLwPY_CCKBs_s2ZhLWZmTy4qMGSG5zdmtFITBoFtlHoJonBpuhI5Ijln0dXO7C09nSI_jzXHG651krVusZgNI60tm439PcKWxP8vKMgC1ba-A17aZoKnrA8hoRe7-3FXn6yD7JfcbuVKyegK6lkTo2XBZ6E_lUBCIoOGGjqre2CtatSemwV7s9BI7yU8euiPS5rLq6uCQX7aeMdZNsDS_NCRYt_pjBpM51muXTBUj3vUbVNC1YjFVksnNMktyAByxUnc4LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axIumbi_jBvZY5dioFHaD2_4mhrS11YUPUfnmwUOSWxRKEuNrEePdLlLGzCV0Qgg9O59MfkNYByz0A24-UV0_M-fj6OgnSfZle9g7qoHeu3V6GS8gv3k9hrzgpz7UA1hEEE6hNuQG1CN0P5oRW4hwZB0HAkPlsaSDP9zxTGGYfu5CxMHz7J9XiPO8R77j0kMSOz50CRzBE7Sw8-PBo2hG16GR7OnJkRSRFdT22AT1deWPI8aUpyFi1nThBRe6qJ_ddB008Z06RJy12XMorPnvmpeg8GCLK9y91DWgEFEnMJlgaeSyU-T1leZ1ihbWxMM7BfMDkW4owaG77_D_uWXJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHIlK4bmbogjLh8X6fWGdS5NB1DgxsdP_Q3nvu5Cw5EyWs7j2tUQkIgi6kwNP6xz7UcH82EpAwQ8QtV-Js3lK66TaPYKeCeGBwwpHdl9Xv37n-2khspv6HhPLnA2S18I7BMLuthiUvREYghqt1U5RdBQXo7WQQOPcDFb6lNkXWpmrcCK7BaTYQKj1mdLXMyGM90-RQlF4LAxjQVudV91hTMUDn-UVPGF91FiFgYf5tTOaFpZ0HTkuXparFN-SLIjJX-4p9ujnLKWKwauqEY3ZD3hq9tus9VU3g4UNjSI4ZqYJpOAs79dOgA96uYK8iple9zWA9po4giQOFOT9vNvxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_Hn_wzX_D4Ov7YDAxulAChdna1zj-WqBkv9Anu0c9iFBobNxNGcu08l7FEgaTbX8Imf71hfwZPQnpJUrWblY4C-V-NeBbQMx2milzIGWD_0wt7GakK4tC4eIdlP73QGtEJvjmzE8zoh4kOUFbWplabWyWzI8pnf6xI4zi7hpnr-ol6kvMc6nYHmH_cC0795YZwLsqMxwY4tyxmTxOJ9e61fJyld7HaITaQe30sAnOpTiB-r1whsffJWYKhxoBKaXrRixk9qIvO_bGOgky21MAXPZkXmU03WAm30U5rXhdw6KJf1S5mtQZTpbDYYvxegoyHdbTfpDIk73u7cgc3QHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGQiygOPh3FuhOIi8Yz_-V2JJNXbomOCjLkdfR-CIJqBrnFKX3FEUcC5eh2Lw-lDTRlpYconSt7jZZCI2Y7TkOD5JxrX54V9TKCjJZer3nLLLa0H4XPoe0C2hdphw8ntNdM-bwrAoBICsV4eaMvR0HXpTJmVpX3bnPWvoSIkU0ZUuV_kS-ETZ0fCswPglTFNP2WXCxKP0o1gJOsTLtx8D5kj4KfL_gQVkjNNkkZesb_VtbRjoiJcO6Q_tA4Jm1J_Ia3f2lt6_qQwINlBeAENdwuvYYg-6LBpWCXdYddBPwgvM4LOJ7Ttumthb1cNE7P8Xp51uej0pH8K--5CuIeDOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCGirZi5wndVERICahi11xDHSnek9eMVIXYEfCpk3VVRY9Db43Yw-QF3U06e_lD5ILbOkmcQTxCZlqVqkdSsm7ne32OJQOgRgD6GTkMAZIzTJ02MFEsdm3Ji_rDqj1tRcoDS3q4IWlLPx6hpZO2se_9IJtTtMw1lOh-cEmBjJwb2AfHaSn0AX54EBubPQmxIUL9I3NuSsnbeHu1ST43hpNMtFRTBxgMNCZAeGuP-jDVkwSjG47RLZSIJLx8AiWq38Sbif0zciHvXSIJkZNv6VYtROCf1YZcDszCyOt93sOKunMEEC2SqBww-fz161W20oONgE1c2eGxE_jy8WLm4Vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CURFa_g8IJ6hVbgCt35XT_yzCDZsJcqysglMwGgIAxgboJT12l45RiBdn4ptDdrXhQHpm-p7XJsDCTwuXrORqlIwmnZgfKB8odPRREj5_Q543dVpAWiJ7LbD3dbGSvTSEQ9AOx3OdIJjE7sHNlGfQT2f980juzywNAfog-NYV0EixJBUMIQsIhuiLCrsbbDwlaJpHLolsnzzwjCPwp8I60E1G7KwR9-QM2keMmlHL_jW6qCf05B3ozh-07iG8vvOqQRGjQzXN-zJQiuKop5uhNE4tMwj6d8AviVcEGoRDWKqKn5OCv2SONvlcTWTYUKhu3C4_0TL93wET6yXR94nww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mbnvjj19NHzHPgZJt-sEWgUj3yabBSSzgsZ6BShsNS1hEzI4mmpEYz-DnDyH5Z4sAXpfwlNvWnzoIGvu3wcodc99cUW500UgJvWWB7AliYsMK4CZj2ZB5krCElhANpzUIMcwMy30DamKVG0y8g_b0481z2aitcqNTNGQzvWIBCu6zH4Lk3MhdDPyewHdLa9K5DJfGahE12VWmDjmCkrf4blZNK4s_3XWVpO_oaFaKMo-BtakB8w5cEWLRnx22hl8kQh0npwb88FY65ssmDfW5ydANhDjTu-DpnwVUUc3JhAk8vioM9jh0lIDEe_2tzEx_BqF7hQoNTmXzDpWXvCHOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJWWSFUgaWW793l2pTZtBo7X5582Um3PJPM5QiEqoSPpo_Tk8deMuEcAVG-1INjwGwaMblBp81PNADpJ1Wcya8khqn64aSPq2QZuLz7LnX4JfFENoXSPxTFdkJzWwZFGO8LnqN7MPBDoadKcFEgkLhRd6cLyYbVjtQIXSjf3uQhcaPyPRsOPSmDgX6_tlKsO8YTIBxfU_4A6X-im-v6DGr8YTVb7cQ41C2Svy1PmbAEo7G9BeK_QtbvugUHNgKmgoxTPDehoQ7y_P6nlFbtDQozrb99etLyspy7S7oFld7y9IGElafTaSv7WT6U3-_8T1dcOnPlglg1EahJVopJGWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLjlQ2m56bm9mnjFCM3TrUAHCX_t2EE_L63YR0gL_57vdcy73VbsQA7QweGdUOp5IYBksdS1dLcQVfddDUxRxDBd2eD5TOspomUxBkd5af05PcgVmzEHl7RtyaCHtY8ruVEveDG8tlAJLQuaNQfJhgulxIRPjNkNpSR0P4kTSl1XEKBF67jvnEH_dB3gy9jasxv5rEVMfp9pS6oWbXnPeOPAH-AvcMIGWTMKWD0GEbU5c4MM5eUg0_d1Zz-FdG38ameugwk2edbCUlQqZDo7UeAjEr-dsUkZ5LeP__Mr-zc7WsDhrm6ip9-gQc3_MNXzguuLTxp8giscY18nIQ7p8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6H7KHGifWzSEcjycgaoGCSjmALz8gAZ4wh8dUc_Wt2E_kcwhIJ0uL50CwuqRxQNb2Mwm5G0GoKb1P0FNTZG6IK5C21l0aNAyKUnP8BsbsZeJMXjpUr3NSAds5u8vovqJAbJwfh7_RbJIsH8f-bOvKxoUHz-kn3Gy8kcnbrysDMb3df8rm4Tt5duCcG8H04DHHVski79rgf-ZR1QKmSem22yPWv96UizKbInF6fpbcFHOs0lkBP1CVgfa9f4SGiu58gmzvFJsrC3TUXJvXg8Ex-ZxjxguWwF15y5qnH6WEed9XnNIawi_gWj-1lZ4bOzIeuSXOGc2U7_CGH-NCXgFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFasguKEZkJp5zKdqD0Fpl5eF5Zi21oIHT1c26v97Rf6rpJG34-ieYVMGfKaBU8X9c5rmKX19wKLithuIWugM3lnkYZLVYGGVY0tgmosrlYw-YDVp-1BoGqcLreQU9CUB1lvcgMjIP0GdrYl5qS3-qONyB1VZEYx26m4WT6KhzMsiy9ALGUoL3RjElfvgcuuAXXZHisy6exPLgKWeEmhSXhDvpcHoitWvJBWVgBdHCpZP9BoG6Tq5s23RgG5zHKvg_vIW6Q9wnxCAO4-Nl9sNY1BVEuVbI6hYti89WScAQzcYAnroFWzji0Fu1r0qE49V2ieDmQOih5zBjhNo2QjUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6oQHXNB8na1GOjlQmys83TROr14oXSr6x2OOE5uExxhXd-z9JjfpOeJXWZs8cUPjTsVtm2OaOeGrGeoNUHEMuNTa4K14cKWD0Yrc0EWIBqQIqy9dv3t7yq_HBjsHJDYsu_h1BqpsIyHKkvNQJ6QKtq_R6RfQGrUfVhI89INe04wXcbWHPNDdw28J_90moqLdrYfEsezFP2y5MtoVNOHrci_asEVNeW6dsCVH2jdjbTrWG7cLicilueYJMxCElCtGuVm9JVnF2a3dz5YvDjyHJj-20meg6h0dCiqh-FONsyvX0ZjbH_nuOPOZTDbQTZvOWufl4P6zevpVZaebuTBlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BL06V-kMjdZQKBjum0LHu-XP4-nw_QKJX4ths2_A8ISxQw-UDFhIC9c8HJSrRqvemTHZItqcDpDD142O9lo4V4d8JbZugN7SgobRvFyLXTl4iWb74ENjV87Nl-OcoMZ2aXYgm7K14q4e6tzD8QJZMljc4DsvyJb9xQBU08etbIdO5V_HmSP9-VaTI3gHuYlM3f2ou4jZrZw5UPALAsG4GzyP5wagL6LaZ5i6aB1Uyth2m3QDmJ-eBqrZwtReDLXO57HkmOjNQjSLaBhKiUl7s1612_ykCRMLfHpHXvGbVJ617i8KHa8i31vmqhPNEPJBUQARhg6iZz-4JgnihNa8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pBal4rs38qi4mfvwUvCoA3Py2gd_haq60BbAOt24X1Ip9_LKuLs_-947ywi71zc5doU1-u_XDrinQo4HvZmxOdPuNrvs0TbMytIf9xDi_Xj3FoKJLeWqO0fIbfWZZfx2AR40K14Lr000NxrV3lP6Sh8tdq0iWcLi-yess4ZS0FZnJXSndXcDrKU1C1l3vJNfeLmiXDonn07BATUCWc4tUCBBbebXi_ExdUsT3VgwWo-QvG5X43pr6RfgDxCl8Sq7NJ8Sf1wn9yHrXRjhUjhaWCHvNfmciVSFvNdQyRVnxxO0q0705eeIbSlZo7HkPOljI5Z-QuhMPM1ihuQ2Mtaquw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDNz2T-blcacPUEKfYpqrqhq25IMqksdOI4kjdjaDrwM9CHDTp8Hv_fq4Q-5QkopEyTokL4m9f_oAnClvHEIVKn5DiSJrNPnuaeYswkB8oDEGqvP0gt5uMPIASeIe3gKtCPky3wnfkLk2lfufpro7MIEExY3l2sGy65QQvmtqqPf1gUhoZX5YOZODdOKeEo8o44Mi0HdjYmJvX77AV1oWdxn64AyRlX2__VNLVWEJ4mjJv17l_5KljD8ybM157omK5tAuY6HCB666f_fqr5gjwQc3PWrnSu9gdCcCl1Q3KfXVWUmzZd_7G4ncn0BoOgALRiD4RpWlDW8E4Dd_4zqiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ECjdh_4JuNE2nSI7cENNH8QaJJLW1WSchZ_u2j6IsIHdJr_eCFl4hUExgxHAxNNLYKiGmFngy3aXlfkxjRWE8exjwWOThZ2RRJHqenyWNTek9Lu90QeDUV0xeD3NLXbezbEIaVUUl7xrkIU6pAZhn8rz8F3KBo-ZqsFPK2Ex6nLKBExglnuJetjyGAVBA_kGkzeAxa7vR5CWkS34V80sYvPsG6jWpbba7sNPD0O2uzIh85VilaO7xqWByspkVq5wBvuvl7wcuTPao78yLx7aBryl2i1a12enbY5pi_wkxBMIOpyHOiD64aDAlj-TUM6bOGBWgwgbY4Nkl5u2t7htOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEf6rhVy9axIZJuWFWu-8uQ7KJZsLI44sTX0peOkVBoj7So_kU8IAoabTqZFAa1Ud6pLvv0hliL46KH8mfGiiRdFAp8OaMt78Sj0dBOBfFcRseauLNWoQeJck0v2VeTrd0e2QSkrycUHjqgx62pF1IKuFtzOQGfC7JDp0Qro9sA7QkAgVMottyEmPAK8msBG6gkMI5JXszVEgyfXP2yUktpr0WZWBQ9f3DkSAGUVjUo4j0lcE-U7N3N4Tn9SXvSYK0IdrTTEfISo5nyiGKWd_5u1F0gUQTcSuC0nyWLRASxUi7MXHJBgSJp3RxEdKYD5SZ0JKwU9UkaLLx50j6lYQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDUiS8rVyNYUDhSpBh5kKju2W2C4L_9uZtZrVGpsbfP2FNDecoEq5T4HjMeOZdn26iJrdiuEOoH7Yl66owCrT3NyRiVZCcRNo5JZFkhZod74QTPM_LhlKZkLPwhqpxDLz6aUBbwGgObGnG0WG_IZnMwMAq2Q8gQCd4Ybs2PiD-R74hNbXVxzfCXJ3ook5Ryuw3NsXzHMSvTKhTzJ1Z3EzJQidNjVAIQWFM9CYyjL_zebmo16kOppRK7-wWjb0UeKeVMtkXjki0fRxduItdPJ7Cd5nPcp1g9obQEJfPAgl4WiO9-Lhm8UzSrTxowrHBKVq9UL4VUk4QTblJ5ifn14UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1z6TmycDAU9_wtcDc-NjX0PcKcMqNR9LNea9sZkHg6RR1CWQSbS7duMBG9KTwsq2t8vKLBwpDt-jkGzJm2l6NMv_6x3eZJneeyQVrfGeosW3S--Lz53-Xm8Fmd5v_7uBn7meec3s9SvBu1hEXFJvw3yqtf5jGqoMiphLyg2UI4OK8YhLFJkQ7W0mcuGPmECcBDFgmaFuWshOmFrHv8jd96XyQY9n-1lNcffkhX3l34vgzokG8pOh0CVV60-PxLDa36TEhJQqjHvg97sOaH8hW5oLtOPXjC37DfkhnQFSqOhrlEIO6YxKuSNOgTxrendxKwKJ1NrvVmUQOdgRytRmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4iiAZzb_BAF5ei0kf5keRinpNWIcrT6YksO9VZOZcdD_AFulEccNim1tYCcWKGUQmkEraK7De4xip4Wl97Ums7Ygfa4UJuVvvMixDmMJBONjHHmyrUZ8ojp6IZgquA2fpgw7oVzEYYD1t27YA3cKoIQK3-QVaDB449_t-z6dggwMR5zYKcZQ9m0_2z905fPuxlx8DXa19Fvng9usO6MCZAf6mUS91Kw_lfPXO9cF2R53cNLpzlwvFGSQ0qCkw9dRjiti1uXcmjjzMz_LcGnWtihp_6FlVq1rJbHxwZx48Ma6GEWX2fDkBsVW5VJpKLZtKQE1Dp8lX6XlraddofxLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ba8JLK8EiiVSEu6X0Cn-z2woC_GB171rkHhxdXTc902zO1C6rS8QRvQNKyWscIa6Oc9EQG2EhM1SbIHHkU5qmtQRqGM_8wT54iSDO_5jp_JzX2Wmwl32k3EgciNl08N9shBcnIL3LMIMeeeikqmsiXgRqXrViemQKRHnkdOD_cvYcwMbm6WLcVHQ8w0pIGOmaSgr6I38iTmEGjH60z6mcW4bY8fZgwT7E3NHDJ3tzjaqcCgS1q8pzoG9BH0lwJLbc4Auf8lfVIZTU74ic04WRR5BAi80SeXR5-ZL-3HLT7PGbHvtYPZ-qUIii3OWuZ2fjuofk0oAcy3HCgqQUoVQjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMRQSEkF7BBIfsUc0DOlForoizXNPERT_U0gDG_zFXc8gj_SdaZQhhfKWrE0dYLT2TleclTYtnDLDoyekthCruRJvyBnOaPVOaqMDbwJUjUlyF7EmsyuYh_in_GgXTxPI-JmrVOv6uaoVlXM1egYpUJ5rZPWtuEpG7aHHpCTUZ894v22w9QnkhA69zULwzHbQSKkT4kt3P1uO2kFyjRHWazlq75XmjGwbJfh7wG1ZFk9uKSy4lqfwvHKWYeZeAcYxhnEqU5Ou7bSuBdkZnKdpxFynoeQ9_Nj6wEDjJEW5RZkxg_8uaZy5o1d8e_RnlMi74ioLzMDomC2B_kL3KF21A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ck7jjwvrGuBJWG83DsrtoKvkkTS_x9E-9uho9wXvrPqbQwsSDp6PwLKqPo1kaSvGYMPNzr-Ijeqg10UoHqPpXH9dvwjK_5j08hJGGoxqt31Co5veT2xa5cR10B67w_Umj98RNTq7dLZMWSoCrm2kjCOeup42z_c9MxGM-1TGTzwDtFMT6o7CDYRlX3sC-PGUNgKmtT2x63jk0ygIn6eTKFiV78uCZJlLAeITWMhcBNIdJ5EUuJ4j-Lf9M7kJob4L4a3e_SYXPcz6dpl-2FQXtNTuCUIhu3-gywD9ZCsWOgmdaFt8y8LD9BYa1vfSVQIbilhZ6R3XEgDk7xCbD9G7rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9HQg3vPk3QY2TkGN8X2iVj_e9jhN3FamRgH4_nOiGzatc6Km1LOurJX5yiRUGg2bHsiUIqxdYmhh_mbdl3MDXsaGd-7xxNSN_vtIYIHIVv9-gXaxh_K17tZ6KG1TCp6x4RuMTyX2z8fMiGrNUcFUmTW_dxsnDky6LTgXJ7ToZsJVo5XQE17G0sH4J7YquT1EnJEs0-25FKenOBSSTP3OszUAn-53ESO0PGu0N1xWIvwooRrjDxysegivIAZF50H8negTH8n4P7fez3KqY-4vjZ8qLCNZ_7T0IQTA1vpKHQaqx3-m3qwXYDwzn3owWtGBDDEqZ_a4VO0069XzYM_gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ah8saxyJgF5yOdzeWyNL9vomX9v5GwUbmU15fg6d8BEt20EMLBHGk4R-AgbfKCdjeabxdGqVhX7Y4-Q2XUwCaIo8nYUiKxlRwTYjP1-3R6hp_Q971MyrUxSsbbt0DAo5RiRipqPt64gMFIn2HZnVs2W6RmZOpG88c4ecuMIqiErHGu6BELMXem5nxn0QlXcRo9If_9PAH4IlyGg8AvysLSwO0WirglA6Gd192OHOSkxV88B_PrmifZN2NctTaQJoI4MmI8oPvzHyScBtQeCBxQM2HxCzgfM-2u5f1V4RsGdpBa-E8_M0SfkQOqXpp8__vNu4Sgib6n2Pq4uGz6Ekgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1Bw6lT8J2i6oHiI5lEf0fn-7KOFGLJFvezntIxCjGu21JJHD2mgPny2l8zGlCUDjL7B1xekx68Ict5eYwG87kwN5KefioOs8efGrq3MPt-5ydLtRqdKyzAMzhTxyNcb5K5K9DPtSUZw9JIGwdGz871V61XVXIeMsWX3WfHfDDqPo8_emZk41FvV9A1Od9mxYIEGziOmPqWEluW4xEzAk3iVOpJ4BB0hbYbRctxoIe5jvdXOn5QnZC0MVHArcJCgINs_s3YStXkuduwmdQOiJJ3y41Vc6v5FSvxKLXvbhsICSClg0pPmbIBXtLWX3okCRCaDAPmIPLgVWsHYRE7FQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EolTi1XNXyK_K_r5KEsyNsUhT7zFgEhhf5B8AOvuCWFTHUwvAhXNc5_B-rfo9CcerWVxoiTQBUdv1V4DrmqNMGkWGqYOeHzpOpCZM3D9wMrqhoNKnsA9d8gVwSQyzK-XzRCZ4foDjE_2J7hUbX77XP70scbZPs3EJ1WAfBEBqpHZNxGIjfUSTgcwBZ2u8d877HKTl1G4MLUki8WNpIuF1kuW4V4t2o89hvwTYSn8wLwRbNh4VghawA0YKWYOJi-DwPpY6_pfou83QzrJTeG7dciRy8SWa1ZCmgAyKadbXjAxjfvT0AyM6a5tUnhWeRJa6VOFbydSNtmq0yQOF98Gjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrzCf63Q9WpGGMyWf65wmRTEyfUIxY-FZnXCKlk0qqM1K8RTDfvFH_261KxoE5Mt5gwuDQoc5ozCXpqvdDiP_l87SqwSGQimwIZkjuZY_sby3ZQwKvKrpaQy46Wj0aRDTO93_L-lsD4dxx6cq9uAs3zTx-j1ZcJguYC-_6a19J6Epxj367AGbJvfeeIJiBRwGz1fMarAs-3EjhyACX8j3luat_Y4oPNR-mJP6cwVHo_FlBimX5DWb6CEkoWJJsx7KPnDz7So5wlm7s6GKf0pbm3Rggb5DmXPb8dSaQeEiY9xjDbfcuZNCtg44OaToQDPZIT-zymX9he89DcgD7bmFA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=huooLKE0rc8krkks6ozV76pwg9IaQuFhvaEM4nkdimZVmBf3iQ3BEPF9mgE_9GBkGFTkGChwgzb1StFUs2nQTowJCWaydsz2HW2m4SVTPNIcjxbKq2Zy887A43cRsHuV-U2N3wXawDy72JR3oWz5EmV7qWSmTCyZGkROzr8wK3mizjupIVKWajH1YenKbc2nLB8L3wCpV-hzV7tzZdBj8L6Dwb2Km6o18pzjo38cdcnhqqab7ySjnr5kWSdA-tQwLAf7ZBhCZ8GOF-FuxVP0P-LCPn8E172iRNLVOmG3K-TbH7w8G2gt-TcvqNEqMc_56RwGxIarmdb_dmnp9y179w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=huooLKE0rc8krkks6ozV76pwg9IaQuFhvaEM4nkdimZVmBf3iQ3BEPF9mgE_9GBkGFTkGChwgzb1StFUs2nQTowJCWaydsz2HW2m4SVTPNIcjxbKq2Zy887A43cRsHuV-U2N3wXawDy72JR3oWz5EmV7qWSmTCyZGkROzr8wK3mizjupIVKWajH1YenKbc2nLB8L3wCpV-hzV7tzZdBj8L6Dwb2Km6o18pzjo38cdcnhqqab7ySjnr5kWSdA-tQwLAf7ZBhCZ8GOF-FuxVP0P-LCPn8E172iRNLVOmG3K-TbH7w8G2gt-TcvqNEqMc_56RwGxIarmdb_dmnp9y179w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lff9achxxHxWTfiOHqhCKd6CcbzzTIsRb47Rr-yWLuNmQzQp30-fQLH4j3CydEzKItUGjolfTyGVAsggfbvNU1NQp7iMSQJRw8E9wDXKZgr8HNpphkHJfn10pNpMafujumxM0WiKuTvvGFO70AbvVtO2bTYipjbRiB1A6qG6J0pL1g4DcyrV38scfDLm0LTJMhKu1rAfEfAq1fPypSyBxIiXL1UjBNidXf7_i-yKMY6YQQmk7BY_k9_HEKGBZQqELWtIThO40JABE8MYddPjaeY67jgXMwW0Bc9kFe4KvZlRW_IEGMOb7v9GlwGtpI7xHXXn0h-jgJTTTFWjHam46w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPSnLophG9Z6FrpqjfB9rnkj7jm7wYndDAQA3tnhtrJ8SDjo3IimdLn1u0G8gFSkpMlHyS04Fl94-2uMfELiOx0Op-IGSyfgR_GyeD80U0agYRne4bbsUIJFbjdA6yh9DmWeL0VOPv02iwRndLglKrRfCunUZmJt43444uWyd3VoiwjUBgbkBolHfVHLIgO4BzTuGtdAIS-9IbnHRZnecmKiHp4pdM7spr1k-jleT9Jaxx2A2x_nJUbWWoR5T3ewmUKEebToFcLylouUwc7scGFwi7SemSbT6DmDldXi95Q7CEJAF1OumQ4Q5Lex4jpdnjF-vSfpRsXnj8tx6fvJRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sc4dqSiBYXgtLVJfklxETcWGQ9e5F4gMGjzp0cmJM5owUXbgOgDDjFfgAqJcn37X9wJQq80MnDY8SHKz9JgJOSf1dvY7y73lhKHCcdGsk_-EBWAxkBzqlkEznF17RaPSc1esnZbODYuc4qVllyeld1KRQmTuDOS1zuWQYq2SrbRHaTDpAUQtskbjZpmA1ip_eZSFDdgiGJ-QW0Wk3yhC-dLufF-R1D2NUrri38F6POuelqfR0SWrr4_6wLJsnGCgCsGWmD4iW4ykug1xohGKbI4a9crnaUVNqTeAVHdsXSK0OkfNqkpfqGpZG82CpB1GtSnuAxEG-wezX7_WZnMqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6B5FgFiUmqHcQJxNBRgfnesF953OYrwGAcem3ahSs6o2Emp_DES6qvJNM1d9b7iUn_yT3lPniy5TqkLyF1xrWk_kiZsp-rfGeIUMlGEpDYdsNMemwH9M08PRjJxXEQIvzcPMiUXAYc173jfk496CjaxhTaWUd4SallKDZaJkQeIGHs2mrS18RpcBRQYRSJX6a1brvvI9a3rcKrdpKiNUE3YmD5K62hWCS_Bmghyh2QlPCxnAxhmFFDSex56us4RYSbKHv0Hw1XQ9r5nULSgsDR0Olm9RtR9RhF4LGC-3oo4l8BFL7KpERAk3t7AziH-n90wOq0heJuu8KMCR5bG3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sBeR4LenxAiygnBa-ODaOAm9blQ9CWW45T-VsVmAg1rbfSOf624WuZOEYUFri4r5MBXFh4aAyKFOT-okcZbdRNgy6I85QmBarMQ7PSQmT1Pu2Xbupz8RNCGbkTQRAUXFv4CCXeIH9in7051Y_0nqlGTzAhQMXbaIjGegOxWt6843LJNDjtLvvTeJmXmDSORh61vGR4cYkebSINXq0rhvYKWFtEuRdTDCoTi9n09v1-d2PEkx2jKNDV8k2CPaTQc16hs4NZmARHzKrr0HWtZwWrXSzr3Q-u59toZlrOD87JC3DT0bNFkk-COTG1BCJBw7r8VCR1BeRb5DQ9OJbJCGvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjMuGDClh7t7sM_N_TJAZU-fcJXlwRu3u6uW9TZcr7HwdHVEjDZvbhlEaH0acModZiERTSzf9HyVSv1aOqdV6fPJIfxKKuIUYFoiF3I5ZJ8yBIVTSu1lFt0sBfu9BheBdwvVh-BMdD2Ex3xyLtv5EkkS3pY-ExBNryiKf8rqlyQ6kfHLDjrCymTxLFyPunAdBvZJ0RbpGRHVI6O3fmUDur6W5n0iJdSoOC0fEMmJHoFAnTaDLOet5UefIjb835vPXvDoxFroxL_ZokTERksS78mBCeVJ96aH4Dkh6VIaA_0jySswDy04YYeB1Z7UX9WoFebDMPS2e-JNPgzpy30qOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O6ptCiBFabcsy8F2dktOylhAVlFkgTLnc9qivmcPP5_bMv2HQKym_Od3cEPPhN_LY_t-ArsSiTp6JLSmZOBhnqPX0F-9V1burew1Yq9jHD1Lda7h3TAqS5EQDGwqA9jodZBQ2Pvro2tWhcpJix0v7wRDPyOLVD8Zp-oYUmokk7pzeK1vP0DKboQTaKlclT5JufDWFGEXtJZI_r89rw2TbYD4aalu3JBsudObImJJLh4hjrUqpXeQQaxLa2HM5ZwbXgdghww5fDZeUm3EY9_DtUP5Vps6ATCXG_Ne2kfIK3zeR9Ggr9Ww2doS0bmmXyxEQtgxP7_e0uqDPdpRQBVy4w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=IYI-HH7-nDqJbVHqjGwu520RTBZ0spaUzTD5ZIMnK-5MvnHuwtLbUqS6hIl5VBkerG9QcLAbLmvtn2fu38k5nTbWyjPOtUSMTsTKDXon1LPEZjmTSyAuG7t78iTDRQyAWL5TLJPE17BgcaiSfGRU7iVWrxSdBMMbuo33gxkw-MPf8vKeiL1A1yIt5DJ6f_167LjWUcY-toEDGRAFp-YUsNwV_cYuCnwf2CrdtP5PTKBI4aktqtO3HSwca9h1ZI77hYbhpmlvrD1KOIY0p44UwcmMl7wWEhZT6W8OSyqdL0QHItf063hOhT4dD4bvvosCPb_QkYnJL1DD0F-Qi_gwXT7VZVvIKd-RSz1AtGGvA9wsysRolnoyjLOsizw9OD9AIt-Pud8ETUz2x_JJwgqyGC1VF8zUXeOb4yQzqBnZTdRrzHYmRrmMs_VpA6mFQQFh9YFvr86cgVHk--anaTu_SnVUsEluRNl-3cj2hFClvJhghaRN4w80Yui1RXnMD6tTeL-8Xfeskauuts8-QPWNm-g6P2zJmm-tNenSy7FZOzcQo4CtehzN9KGnr2VsQiVxJ9W7U9FTZlQj-feiimvEuvRul2mcXRRnx3u2ZPFfcP7U97vD17EuxPe7_SuzJWw62UXcLJZE5cuW9KuPaPfllvWL-XaWGcW4xNDQLO1uJYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=IYI-HH7-nDqJbVHqjGwu520RTBZ0spaUzTD5ZIMnK-5MvnHuwtLbUqS6hIl5VBkerG9QcLAbLmvtn2fu38k5nTbWyjPOtUSMTsTKDXon1LPEZjmTSyAuG7t78iTDRQyAWL5TLJPE17BgcaiSfGRU7iVWrxSdBMMbuo33gxkw-MPf8vKeiL1A1yIt5DJ6f_167LjWUcY-toEDGRAFp-YUsNwV_cYuCnwf2CrdtP5PTKBI4aktqtO3HSwca9h1ZI77hYbhpmlvrD1KOIY0p44UwcmMl7wWEhZT6W8OSyqdL0QHItf063hOhT4dD4bvvosCPb_QkYnJL1DD0F-Qi_gwXT7VZVvIKd-RSz1AtGGvA9wsysRolnoyjLOsizw9OD9AIt-Pud8ETUz2x_JJwgqyGC1VF8zUXeOb4yQzqBnZTdRrzHYmRrmMs_VpA6mFQQFh9YFvr86cgVHk--anaTu_SnVUsEluRNl-3cj2hFClvJhghaRN4w80Yui1RXnMD6tTeL-8Xfeskauuts8-QPWNm-g6P2zJmm-tNenSy7FZOzcQo4CtehzN9KGnr2VsQiVxJ9W7U9FTZlQj-feiimvEuvRul2mcXRRnx3u2ZPFfcP7U97vD17EuxPe7_SuzJWw62UXcLJZE5cuW9KuPaPfllvWL-XaWGcW4xNDQLO1uJYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xb_Qz_bbJHJMFj0AXjfxCudF2B7jz7ZL30mLhuYA6R2mjaRUmrZ-YIUQ-_AfynM746MDHmBJNFxIaMHQqc-QhNSdjBxC3nr0NY-ey_kAD3DBBpMH51YMOY0ahIqcWgSgNxAPPNuNsXunvul252mxXCuFAl2znvsBo0Nj10sZO1xFad2bJDgfKlsCwJ_SmYK8zAce-T5CGirMXC18xdpyDr5pMEIyRRXogfKmO6CyCisPsX4su2WVWWlmIbQg8NRJuG0ihdB0_QNaayDwus3mvD_yCVuRB_LKl4lqOi1no3LbLvfpZ_Y4Ib8Uak70cq9yb39e1qhQOBzi_cFhMvDreQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c708bcDc1SgvM3USrgeiA53zt5r5wdoKyxb5mf8HgMVJachVZMi1FTbgaFa_wM_0RWTij3YfY4sZRFGSh4eenPZHmd0yDVc0x5b9YGvWcBljPTWTk8V46cnfP1r0-Am_E-ZD9qFEwPQ9FQnnWdM33sYySn4bijGJ-EfG__bWCfZolD7ozbApN9fBypfbS4OYp4wl3W-9rr9yldXgdHJcljid5-hZnDvOrvv6_F1bCOWhe8y8XyHpcvqjCOlBqBUZn82znKe82nGahCEWGOJSYD5BjOeBcba4I52Y-v6NLcAmg48HBgav7mQK2LA8tuj2gBx_XlFS8vJWTAAHN0bL7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZJ8Gfgah6F_jzdmIb5m7tjVhKMIu4RyuWPM8iFQ-JskiW2RnUHjnDJmIsiqEN1LgggCc7uSggJOP7n5mXXrysS2QNbz52eWLx4yMSEdLbgXPPfmUjxk16Ux376y_sTEuhOOAjZJ0QbXbDRUQDAVXW2A9ezV8iWfQVIVD5mma0Qjpl38VgigVk2xI9Yi92fUmapjtdWGoE1FbTdCyTuJdakck9Ct7Q3yh-Ur_4ixJ6uiR8kQ3lgRxy0Z5bstezgXdRCxjeRelYrUyotN3zsGEghM-s9I0MLZb0YHekYxVfz-iXdNtuXjKLCplBsIOgoG8-95tJHWiW7f7agmKbDb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tVnioMO0eRfnbDnz1h-AFYFoj30R31A_y4i1oQGtWp5mMAywjtMgrLQjqEYMbQbIhiDr2DsRVFMCZEXgLSF91MKSB0ATXrOMu_Eb2vUjFGrSLIidAR7GkxsdZ_yBQr4FlFciNAXJkdU3xhC95baNSMIBlVrBrMuPFOfupCFa2VqYTtung1H8Yv_djzk1fUgRBxKVC4ueKXJeq_0Nb9qXJdDSjfdsUEkqXsUuPrBn4HgArJVml8T3YY_wjNTO_-xtFxJvMCTbYXxJfk3v8wN3WSPW7TA7cHhd9pfD1oFfI5N-IFdIij_2r2S6QeW8qv4a8XBZ9b6Q0zNdwiceqAaQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bwkyKiSGeeMGC3SbDmgzIGwUF3X0Oqh3wAqreJFwNjdSHEBf6benwonuRgc72oF4XRu6MjZRiDs1mxUMGyQ3ZkgKtU09rT09T86LbkpyXiIqjuNXxOz1cwxT69ZmVxxKfEE73ZCLJ0JSurfngob4Gpp2ONaWasz2fBlh75TBBedTwfsi_BcEovc6IjPPE4FeQmXiAz_wgd2PZv2xost2sffqW3fuRzKi1lIJiLPwt7RDxaL_Z7bySmdTL45cbpRbXrHdSX0uWzH1sqe4sYkppTenjHKtayNB1p2ocqwKMDfwlritD3zscKhMFM9dBSY0mEHxeTWduMnYZRDpiqRfaA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TFF5gufWqlWukIUaKOr0xkbK19J5gJEk_Hw5TAAQKkuMzuCcvfdUVLK99NmGfkU9y5cb7eTku53FigwSRxKN90iD5kJMTSFk6g698P-reYK7-8wVWap_j3OiXV2YTA2c8UKKd_KKZKOffyRxr8wc1YPmo7rwn8q4AqRp1S1CuvjLavNzZa_yiK6M9mnAXz_qYj3BxwBKGkQX__cqNSZVeXE_4pyXxXdENRqpxQggOfbKBA9EPb9AUSqxcyCB3hbulK7JHZeSgmAvOzRACJvIPJ-jY1Z0Ef6AeCZJAKvXxKrLCO_YRb9ycUkqPyh_hqEm7MWiJy2vEFSfo4yKAENE3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TFF5gufWqlWukIUaKOr0xkbK19J5gJEk_Hw5TAAQKkuMzuCcvfdUVLK99NmGfkU9y5cb7eTku53FigwSRxKN90iD5kJMTSFk6g698P-reYK7-8wVWap_j3OiXV2YTA2c8UKKd_KKZKOffyRxr8wc1YPmo7rwn8q4AqRp1S1CuvjLavNzZa_yiK6M9mnAXz_qYj3BxwBKGkQX__cqNSZVeXE_4pyXxXdENRqpxQggOfbKBA9EPb9AUSqxcyCB3hbulK7JHZeSgmAvOzRACJvIPJ-jY1Z0Ef6AeCZJAKvXxKrLCO_YRb9ycUkqPyh_hqEm7MWiJy2vEFSfo4yKAENE3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBrIeCJ_U-Mq9jyEqG4MGSBRYd1wHsBe4gW3Ya4aJAr3LVpnHOgsF5vT7facx2eFIfSSSY3eaUfJlkJFOC3xYMHJmmCdsKvqlPMH8nzYhrkq9BrOA25xeYfADYTy3MW2kLgIcm8vtSXFCm5iyL6h23AlKLLT0SRg-y6o-8sEiKdn9tfdJ9mSpNKNSM9ExkkhEpecWDkfWgORJKrja-vTg6i1Mf5VgqyQjEVa4dEVRYLoeKZTzYgVG05XwEC39gpM3zCCfBj4nCC_HQc5tDmdmoJcEuq0bUAOZvK2oRRb9hDNbXM-5qWF1cIvnKNuqaPrmB-NxCWRX-tZNEseie7IFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JymH-dkeSbp-1Dnq2p4HKbqh_CcVbUFrVsvQ2wkkv-Y2d3dxVoYSAzlM0De0R_ywjXoFv5t_bod2GNY52OmbQ_VMRT1ENI_wSX1fqGTe-Iu3devrNTiwMP_6h4zKm68yW92r1OaGPT1iysiiacuCztYT1RFcv7Ovt3gIusqlnPbKt4rXOUljhm7Rq-6f1-0kS1JBsiRrGF9G2ZuBMEc5O4t9T4gZVyvngo0qpoN1S9gnD50VUwUuU6FJMDDIovnALOjCoZDZWIUZU1aAJtwIpucPnM1AhdKN9Q-MsgU3hzsIWdbSePPB7l-7Vw_1fJUX8htcUbilOuyK7zvujnJ7cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKdggW7_hhvOSe2r02bOhHGiFmsV_el_XSsnzGSiPl6Zo4AI1TQ9zqH1wBXLpI5qVCY_zywSboVduLtk8zrihdAkCfyShxD6y5JCQ2TvC8EtzfbF22uLuowKx-XaQHd6PF2GNWbyXFcu3WPPwevht09PFhPd1pKr_GzKlZWZ45R3NQtxdCicP_xnlPoOF50vJxowtiMTHi4u6Vneh2JlaIsbpARFZp5v126fvAIo1rWLUMcu8fkn3djcLy0Hx_Oi6JUey_BE6kTOEp-OtoG6QYImLxjNvuzj4Pu6h2TEl5oRvQcIQBN7zU4JMyhvDBd6UPrEMDDaH3Qmm2ePTiSgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqJRCo2K7ffypcGkgCHZLNbV57TI4vv3PGbDOSFSWv_1zBz7yFp8UCPRZkbtEvxyd9eMbALcVFMmEt3hEkP5wuKbTZ8_RxnliDpC9Rr43sUWeE9Eu2l_4hbuyOBimq5QVMNPMlSTwHZ8RtCnGpSeaDDnlSjleNXlYyE7qp4rEAO6CuZgeaAXiSZEmDI6iGyFB_c0jkqmAwmdO77uOnvMubMgopU0jVQvdVMR6YN80a6wZkPo3e8w2I6EZDM0k9UqzRU2N7xMQo3eYfXJY3akg7YITscIyMRXhz7jLG46sQOX-PrVUkdxfcXcIm-wodwzsH_asm0Mx2mSwdJlq7ElvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iJMaCgXWVnClV1zR8D3CNzjPDIEXL2l89ApSs6ncREKzvxZz3yEHf_5Z-kspBvuFH_bD5Ty1NVfe29Dr56TuP0dL7eFMs9uweV30g3EP1ipwvMg0mfekgPDu0qgkFGS-1DIzq1jLW3w3M9F4rTg4MSwAcdJ5BX9DM_5rVPworHdFWN_9Ifmkuu9jcQw2J44gZnNzWGT2fW5Jx4ssstFTQa1Gd7oNNkp6GhF2gjwovPutL9WRigjZnHS60nVoa5wu_UB8IRqfaHY81bY7X0HyuX2cyUv8PpuGmQpebBq4kuWlnTOsxcmAN7Aobu94PutHMfsabWu-TZG35JsXVRXCBg.jpg" alt="photo" loading="lazy"/></div>
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
