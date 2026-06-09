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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 19:46:14</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 214 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 268 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 326 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 477 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzYCkYOwPe8J-6biy-RkYjmDS5iMkp_SoZ20fp-5vUA3jQae6YRagc_7fiQXI4Y2sjjbf8pm7HzoTdBh_KfwUnZXLWTJeqL5kFuV8gnbs-v8hPROce0l8NE8nR7c4rE5dPP4VBEHpeV3cE-WklwSmcXnb4p09fqMC4ej-BZv7_upBTcGg2TzDDR5X5zaGuJEXdFWtWZvOoqKjuoeJ2hi5xSQu-tM2GLY3__aZNv2Hdn711Rwq-h713DfjDO9CilHJkqkNNPp4f1BFG4ZoOF5cBazP3E3kqupJ0cbXCSrW7cFoauq8PpacXumkLHULTEfnff_NyFEzRpeF9tgyEah2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVT6NWun_C4OgXogex7UmjMve4HvDvY7W2dsxpVhE_LudtZHIU2io6EN3fSBEvx1r5D6HlFCdZzm_C9vzYKFUkLnOmNbaFeibhPGKxYuoUsUtiPecZpZKNiEPZjd_34d4J5U7VJ_Psanx9An8gSu1O1oGAwsA86xt2rPGYhT-GB_PTzsb5CUEg8fUs_5gdIvjKSMLIe0DJF89-6Lub66yksfxNxjLf1g670jJ5YOnl1fR1rB5uqDRu-jsEH5lDEO85tVqwVJSW4mJosRypOXOW3PTas5WXxu7IJndpinHPjpXJegEwVFb1RmhqvWgRF38WR5RGaOveDUcJ5O2YuqTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcG6HECAiOe9K_2wvyj15hnuxaSJqB3Lz9wkqczNOiH92Tj4bu5MPCYs36Ibr83Zft3ZD2DVgCrC6_NXKEiuWOYl81_x2EqjOEt8bKfdIHn8FELggpEnyHGsV_GeydzweLdsnVePqlonYquiC3a5vh0wFvk1Qo9DZZUdqzfrHzBicVY8C4nFfpPThvUjmbmUXx8W_i99iUDJL0FMoLceoAIV3iuSw98kojww3ulC-8oPk5-lKnJ8Ht_xKZKGA4VCeVTXD1nhKlxW2av86s0sBgdI30jiHiKZ-n8Hb4P2kEkZmOQFVavfTTa980p6lZW4L9_4iSR3tFAlDK4BGlSB8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqIbRz1-3MFM2hfqroo3stotf0_2nqp6pPcppMWmbIIJwP_JWSBufqbSzYPRqFYwnAv0fo6yZbiTj4-7IlA1Eb6yheT9hQd935JW2t9wCTP2hMvjOmQUXXLF8BLwZn2ZTR2Jj16y2ugVVSVDRLkMLbibf35VzzmCYNHi3daPbG0phD7KbxX5rXDkO1fQDaRRiHi1tDqoVSAIsonEM1Uaq9545uO9r8B6yAzYra4xLz3alONMG6n6QZwkPUoGvnxklhj9ELHMvFFyeoubCzQkNzUWXvtagjra98pYpf6Oekcx66NNIKIEH2tRSNJauRbwr3vS5SH8XWSiYFndXjEu0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UpzoQcUu_uaOo82c6Tayelz8JpKlXLD0GUJeu45mt4QROJjk2NQNfBgCYY14MzJ3zBSZPpKnqOJ5O9Ff_SgIXD7FLdyj6evc6UydYH_6GXssyNNbP0HmSkOWTqesjH2Bx5OeVnp9x8foI5cRU2Jt5dt2VSO_x1KRRdCJbl9wpuaGa2kcszRrVEjDsvlYNnaXG8YdNMX8XIprXrbm_GUB6cp937r88xgiwI4LJqULF4cNnKciboDtQoPSVWApEaGpxO2qtVPKqC0O6as6UO3-e-eyhvnCQ5yzidTBUfvacsO9RqeNWGvYabjzrA1hrQ9H57O_pYY14DTS7dyX5H1bhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBCl0lxdslVYAiD70XCRUic84D3n_gQDBj-oVlZs5wxpRETaBingplejYWYRp2oEOG1fHUwZtIRBZPyHR5mmqEdCih_D7I_fk1Aan1y6T3oHl8MZ_ffZZmccFhggqKUeYY9XcitbnlM0CJb74YtK6cyh-c63lRq-onQsd0oAq1Wc3NygtNPK2h0I24qzVcoJlZ70imb6vMo1SGxUrNdZsNOu2kb8Kqbui5QgH902k2V7M_Qkkso8luvAKgxPiOfBeffx0VqmfkoXobgxAuziXW0fRMR9JJzGnv7QcDK16de2zEzw5sFUvVbZY5WQl611fU0qKAP4tzuizQyUcHLRrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4eKn5ip0oHyRh94NPOlMfnzdcMz5IXS6AdNj_bVTIwVRO7IA8wvnHlXZrKnrZtHWN9MHnYHVDJj3hPChAht43woRQaCTUb71tZbicoB0lhNoU0eJCGeBCldHOHkAeW7WjZiIC8DE-ifa4TZaOnzIbLPy-c9TE06_-7IvN_troVwgtoiSwO8absDs9z7kudhDT8H70XrwQL6lmuYnv7RmxBg4UBAyvZ41wOw6oImMOVLk1ZgxVpndCQjfT1gwloxX5WsCC5zaBQzM6wB1zB33JSEFMUKJ03JgNbkU_Snh5ht9B7Xl3zy9OqsLNHQMJOO2tFkYWEw6n9aRmayo1uYtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4Pev8qqmxQVBsIP3JQb9xys_uG5jlwZCOagk72FCgWNBq5woKM_wRFcfTjuPNV_2kptrM_rP4ALm8KMOLo419dYhFs8MsS9uNqW2MrxFbPzG4JRS2liMVydUuf20YWLb-RiqrNGxCUSNBhhdsM1SsYa9zZnIM2gkkNEAzI6EeruBwSwrepsDI9ootI5jNuK785f6rwLpu48f9Q9cR_1D2YNokF6vlxMgNNR2pr-diGYi1OVT4CsJXVkgpPwKWVKQUVHXu6mjmsiv4UDJajijXb50ud_R_cP39DFJ1fZGlTKOHEc8lRwn7LScjAfDJ8xz53oHulqlVh2b6cOVFlF9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VI4G3IrUNFjAM2difXRz-rjR-ImUSJXoIwYgKmdaC2VNwBKszXs9jjQE207T_sbLZSwSN5aom725lY4XzVqcnzQtMmD092dr4NvRxLjqLJaMJJdMQk3CJ1DYkCg-EBogI_jWyUbsTniqyOihLgcMM4mTiYGtZgIHjiu4Ws5bclK4i6_Mw8I74wf4jMwYrK-BldmMx0OImCNqz--S-qxYtEwxb3PbRK8FI_CFatCU--TkK7jzIYAxQutBZxnSKZ0ob9JSC8zeYB5q8hfzUX6yruA23NmGAArKthfbkY72qlDnMxJfWAGop77hp_SXNksQN1RVzxV7f5F7IP7Wt14vXw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=nIGVIarIz7GIgU3Z2CocbJzXY55l1NMQWyC_M-g2qqogQpUj9hwugBRtVN28DokE7voHrx1pPTRa3r8od8ZQvuDtHPkB6faB7Tv6-D4JTMAhSo_Wwl-_0ECE4l9WinWKMfj3GRP-GZYn-oKgusHNpPL7yzuRT0NXqUub9qF9OJlMzrormNeeIbtv4-3SRyn5FutrhCUTLc4msp7bIJIWz2qCItHVApPk31y9lLx7LMRz8xHNmZnLokM-34cTAjrv4uSyRWmbEHTKqkV13HD6Xx5NXoE8ItY29mJHcz8cvbG8lfUPVyKpNu1Kg2MoxogpPwTYivEQuUUdRNaUyngghA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=nIGVIarIz7GIgU3Z2CocbJzXY55l1NMQWyC_M-g2qqogQpUj9hwugBRtVN28DokE7voHrx1pPTRa3r8od8ZQvuDtHPkB6faB7Tv6-D4JTMAhSo_Wwl-_0ECE4l9WinWKMfj3GRP-GZYn-oKgusHNpPL7yzuRT0NXqUub9qF9OJlMzrormNeeIbtv4-3SRyn5FutrhCUTLc4msp7bIJIWz2qCItHVApPk31y9lLx7LMRz8xHNmZnLokM-34cTAjrv4uSyRWmbEHTKqkV13HD6Xx5NXoE8ItY29mJHcz8cvbG8lfUPVyKpNu1Kg2MoxogpPwTYivEQuUUdRNaUyngghA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z59qIQG4R_tNXtII5jsuxWsLgnybo657CW6-l_0Bys2Hoy_kKS6k4V7q5xI3ZHLDzmzZVkxN2YlF9Q6lsfYWHzUpN6T-3h64fl8704TWihFUhwDbhuYSsk7nKPmSxUpc4brR3zCrJSXoE0ATbrQPODXdJ-hpZeJwAM56WZV5U-klxgwlVQlYWagK-fI7mLyYyspISlNyapoaOLrfzq28NxXdpYf6Ou70bRdD9TJpMIaDmHQ_O5-BN9Tkx3Ar6mEyVZHpRZ9ujopZfXtQhjQAIUoHdFqZVkWGEWdBPwN1dj340v4Kuu8DzNdZiYOmhFJM_GU9cIgk4CcihXjDOIQAJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV6ULBGTD-rZI0GkaVNY5gojy7PltRjPHO30vaEdn0IrvWcQCdhVP_8geJnYeZmP_lUdJdZdwLlZpxl2ujdPT5h9tuMS_kSaH4QAj3Vz21DgNQ_1rF4RPQOXJD5o7CUR2ub50IH8ohBvR_siYq8_N74nicuqFjsRNlSFgwN8z3SYV-xymzKajlw0XsP3gpgREZcHi7GaQhg_dUx91NIF16tgmhmKaeXWEXVELOOXfo_Pdf2Nf4xCW3XPwZnhtrb_AfbJV8WxAUaWKFmAZsnh-MVLHP2TyMG3dRXOvujcEoKxMNPc638gmWb4kbnKlr1Mrl7HFRhYYrj8LfvF4Uko9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uym5XEiDNFAibiKuulvfnhC0L6MUPn54SizEc_vQCAWJeYjArgSNru-taC30TAQYfmbXaxKY0AKgzQJCXBcBG5f4fodiJ3Ia5GAO3AeJgsX3THbggVoD2OirIJDNTO6rpxvbRRO_yzETSdm9letpejLwA5e1cdD7wb38J2qg-8R4wx2H6N-kdmGoPhqqcal23OqbgxTZwvMkxj9FG80t_8klwsXw13IljBlrILLTZuaAnc6p8MxSvGQdvNH-zBLf5KWuwXg-SN1xCWHhD0giF4-xXXCaWhbIXIcjDLgiSkugKQutVqrdjrfZqeb8320dXAvzg82JtKp0jn2XVQZt7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNyzSC2b028obUbHGkD7rqHpZLWX1Ws6o-_-hmPufudpeJ5oBJ-7PS3BL5sEW0ks8GPW3ZZA4vwYpplvfCLacafTCVeQ0bMGrj0SBr82k7hv_TjCShNk8XGaf9-HwxYAbHFEEv2J227TI6TrRLWVmuUP8bKMK7_YUyDi2_UQ99gyJLVY1GcvO4Y80ij_Ai30jpe9SyOW_Aaht-viXfaFfp7rkFtyRT67ojiBgycYqAkkD4PgwMBEEkUe6s-65Mer6WpqNjzyh1VeCPoi5SzVeRaBPvr2DSe6qVzuHNf4GcLRja4xvnc4LPvTuquk9KkI_nnYP16GcMXnVM9eyaFIQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbC1kGA6qA8mw3GenvANBALQnSggzS3eU8Id9SyvX11VyS_uzILcKhpTm1ugid-xdaf1DyWEl8pnZOjk2RR2hZrdkEIgU756r9hjZ7jtp7j1Zv1gGtVZLL4AM8LwvOsqF1spY_uf34sMDw6Hw-aLnNc7eIRCNSYpn4rOuVhN3Oy-H9yXRnAxzHhZ1cAA7nfS4hp7gve2ULvpZ2nLie7g3I43eVp8RV6lqHsDH_1Usm4bLwGaUUkxvJ5mH41WKK9ssd6RwKMQVW526NKtMuumT27ldccyPuHgifm_5VR6iPXS__pal6sQnkXD1TVFGN6LZt5aDcjVtGnXrv2J4oFhuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vj-b30wzgjI_oVdnUsNWad6PK3RbFcm-qNBWOxRekvI6XHUDo7c8j9dbfmFbhzQrHBSpLtwyODc-ojzWyPj9sXPMZYIsDnC-NrVWL_Q2rXnzqVkTReL92mlEh7JpHjemUVI9NbK9srBIUWKn82UslEORtOIF7-8LniJrYvVlHKZ1jS3gYxNwaoO9CJRce1LCqLheUQ88wjVzi6aysvNGffbgD8MZKiYE12CZ11JXM-aiyxqlFyMR3K-XV9Dq6P_-4OVLGQwIupAfBwYo-6-0Eu-NmRTrjvOQG7RDQ6Vr3wgiSmGfb5-dCDn73siCtInUo2I0K7Lm7fwMDbo4U3JLyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/naXNPyUerrPPJoQeCHZctP-iw0KnCw4OELtU6SHE5k7MDlg1EgRDHBvypMJXY9AE4-DsdW6PoppaJzPCqYF-NUDaD3wj1fHX14DXzY1o-BusiL40Q2U0NJuu9Klx53KVWtcSs7nFPPLvhKEIVYl5kbfldPvEtnF4qDaUJZzknmZ_XQwAxk-sSMnnc85G-IU092OZCiNPqbYgKtdrca4KrHkU44QxacCh26lrsoe3ZDZNHJTKQg6gLpjIonnJndyASvArBVm3V2PLIjneKJOWfdByfeCbvLSIizwVKm4Txgukj2EKZa5WE0SOuduRYQ7NuRBB1o-TwFoHBfA5hNMa7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOuyoKRcvWjLREW4J24MZROlp6MKwdiCR0DPSfjxkj0Xp7Y4Vm99KEB3X2AaWfiVb52WYxbwbkI86LRDbtL3xqjXiOYzBwqrr0KnyTXMVxS6_2B62UZQXKNnVB2AtjYMHo16kEIMWgSZjUrswBybmA_kfoLyZ7iQbWQ4ghsYyda6MoYBsX977NS-1SJOXn_ag2Wcap9KMDNIHEiVdebK4BmFVW00kAlDbMkYYB3yzUzIe-w0SaZDcq20uw2J6ZQoha65foREL0EawelVlJdSsut-t7-wx91iNK6OJeLgabSqmC5iEC7TA5tf_en1stLMjvh9nVLDuofVaujtTotMnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyQNhWShg-B-ozQl1T6Vn7_wWvCXoXj3hsIjBjoa6W1qUMleea0366xC4YMnI9-7nJMxTKFbi8dD7eweicSXhNhQkx64AKsUYXlEagJEpMCI5CUBzq5nGRvGBioEsslYkrx1Syge5R2uyg_uLZU-DNUd9IOyaJety7jjB9rL15Z7u1Lucha2_MziVtIAommokkqb90JsimU1zlS7p9_iap2jIE0NCDQkArvdbSWdpVcnzWJAbOX1lZVHv846vPK-AkILeCHqMjW04YscqqreaQb-FOuwLwg3Avj4cxS2AChB3MTvHsUt8CcNL_DdAwjTpAnk95GF8q1bMyaup8bVrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4aVuyUwsd9go2vKMHSGBkr7f6j9DAbRZvmFDSwPvxiHFzFeOw2FB1rhZDOXZZrY-H47_hIHSj5K5ml_37e_PTZKRFaU7ivasaAB8kqWDFoGGMnHhvh6mh--YLCoSGS8o35hINrt1yWwSDRoRV7TzJNpt7lqrBJ6wicpRuIr0Et3AxGoM_LzFORxyOXRNX68LJmJNTJK2Z8MkmcaxvDSAzAXEchPGDbCiE27R978y-0ULYlJSioyHjpP5ByZKJlF3PiWVFwZ8WLMyNICnTXkV4wA4D_ZUeq45ku_Ssd15V4cY4kwoIoVu9QVKPKeXEWe0_IOqYt-2eI48s8-vbE8fA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpAOjbipwRAK8far703qlFG_lHVuXcFoSxyafOoSpbk4Yr-paqEFdVwc65M_gX52tESyr8L89fNz4Z8uqvLBl-BGJ7va2un8Cerft9XIAybtoepWRDNwyxZoVRbYCyMpendd_FAbnLjskHc3LHIMBVLvJG4CrDmeYgzxG-FGwyUak95V5aKZzBGCXMCES2OveBL4VNOd08m2kvsmjpPwEEhAo_Y145cpRdoOAtrlBNYdN33GIl0TYnX2Q_anaKXI1A28zDKOFPe_CFWrDmJ43bGaGLis2jWgC1wFyaKlH4ZXfyPse05jjQoysE1I__ElWw9nKSlOFyrQyRF_GGQHCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDZe6bJcaFqFJYvbnELQR11yKWV5Ot9IVW3QOL7kxrUU51cFbLs_2upmIzc6vMztGpAwwFLnIUJ6zcOCAkj74g5eRkOoL0paaSieNm-EO7InizNRU-JXlKbUwn_owLDiMrFnDdnSrXprzg-Yb650oPipepMxTSJV5rJUuHMnfIY043JJZAMc7TbIhCuoC00aEZAdCaDWPT5tUjrpMNwAeGSaOIOJDPo3P35be_abG0dEgGfa0peOsTUEWSLbN8sKv0w394KhCAnSxnzwbB92_eTA387pnCeFJTh0W2BSeAF57qiE6ejh3sEqmSHwQaqSQ4vRTHy-Gzmjc-2eCjnssA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQJiolMApbOtApgNFosYd-8mOmR_HVquJEB8mWP-pKYR8v5czkazluKD_OTisixluxwidfK_U7p6ETxsjJcvkwNU0K2F2WUyzozCttCHHx_HJQ-W5EqE27x386xCj17F7sS3W0LLdxYGC88knj0PO4IqprlPV5Haqm1OG07oYzZHF_Fx4GoNvSg2O6TftqZPXvtSZICyYHZpl6GHNb7xPvD_NFsr4dX1YlgX68X5pou4JqTmXCHEDObJfGlPtw8HG9PGxq1x7-fpFK-5s-yBzy2YiZCGigGa2sxPir1I55qLQ6oVxQ_xeyiAXMVXrbyxRwPk9IANOZaGDazpPbFoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XiOos2CN3znDnlhnhriHAkjVXhpxZyOzJqTcGcqQVTXuOVarG6dn135_1EEL-Tu5xJJifRhv2HxWosWvCOi0ggPgq3_ZHPJvLDpIA2bYhxyklyDa6y3MusZWc9enEvhCegRZuTfzMni6Hok4t2TAF7bsPcHl0BLsptrMI-Sz_d-DMlLzFwym-gNWy_j5mVOSbFSxyW9FWYGTmA8ZoMBF4nZCnZjNgI7rsAXi2hU3LTxvrrj5OwVlc77WWLVO_HX8SdbjlAm6Rpqr98vnhuGgYSE_4rGx1M0ZNSA4WzPO7ayT2EqrPRapzwX86SBmxj2oTt0Cbo67_wDvPD_h1i2cXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r6_KKcIcSu6bHfEm_peEfwWVVtnabg7FTNLvahSDjaw_8QHHRYvtQWwPojvmlTW81pML3-z1IE2wXs3FwpkZNsbZNn-VhpWKhD0fEyTp_hs0yyxAmYR_14T6ykr2fOB9y97VfqIz8sEO63TzoL99Il-Ipm3l2oRyZ7l0rY7JDxR64AHGau1pUipOqke1SFtvvjyu-tZFDCT2Z2uX4GgO9GO4kQ8f-bCbQ7miPG10nnUCxhJE6C0SMIgy6jk4cf_FKDMpAaaz69UkexTgx1SrJnu8qpxvwFg6zTelNk0z9qqWF7Pb_VbxGC4U-pjyhgQsdKSJN1XpamZJWf1VeoURxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bx6XA_DQhslSQywrIUx_zA2lcwiL-8gU_ABFbAa7vhLuR3N-Ey_XxDpoHF1FEFTUgNmxMhzuBfgomt0Zow1Heqb937vJ9zsrWHLp_NQkCJAFY1H8ASYvW0kq8HBDI29gOdK15ySY6kDl9skAZq7vnlcbr_6FmpNpG0xvRpMW8yGU2DayJVU7oHcCW0CifBobAr6YONCSp3uqAoP_icWvDY042tXLjz66MoTKhe5KwwET6fa3zDEcTaxGYdqX3zMRII1xfknyMmJu70g6bQvDMiecLR2tnDfozNq3XdYfoxyvyQ9VQXCFHmCG8R24202S2K9rDw8lDeNIumyQOWOJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nmgcD8_6SbBrb8fpfkS4Crt04XjkYyDoXbpPNE56CbhWnuvqve1sFWlTm51C7XUceUoo5l0hCoo3NVnWg_SEr6IbJixip_RvPMaO0JcqgtkFGUggmuQoOEbp5TSdtu9T7R9ps-8MNpYZeQt92wUuXMnaPPlRDvzIewdH6kvDD9u6GcnnDoHoyz_-T80FlQSkKdjxVhYHdZPKQjVsSIysBAWYzHrI3yqHjoYoUzUXAffw4BvrO2kMYsxp32m4-t3QETR4K-xt7B-ne4ahrlt5kM5hNdceONDK9rc02BtSI2CtkL4rSrwa0BCIALc7oBHmpcCvDNaF7pbGu_KPlcwfkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH9QBEjiZyo8l-KdGfch4ERHKFFN7OP0_PM_I2KIqFejxV25e1rrns7jEDXiGeczDC3O9AIIah3gX1nycydQQZ7VGCoj0A5BE9QbgNeyR1qgXOJIaYb65DedsGd7YeN-3LglWkWO6oJfSfCpyvuBvf9BYFNVqfCWPAvQDzTzH3YaicZtNMtURzBUYHm6XkqXGSg1aBHVFQ-nO4rj3MSqK60LMnZJmda6YsOvn7ThAr4GNkE_wLYb_dQuKspin1AtDXR6kEw9_nzLVcxrGVcq81KDcQVGOcotE5Beg71oIjMgo4RMR7ZU67BS1d3w85ut3tGDmX_8rDYppGl6Ft41JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsVBe0WlS-GY0RbG5P7uDxPBB7VBdNShe16EiaQ7c3sxSmmRypgIKZNIPu6o3ZjiSPMCtWZnGnhQW-rMpI_-DvcwTFHHFDx1d1r-ab9gaWxgLZF0l2p4CvrSqs3mqfia6pZY1XKE6Q29VJAZAjUm8Pi45YNOABRhaXFlC0Gs0vmut5yZsl6SZ5CbpARD3OKeoiO3e3x4ytzThxJWjRBFCf6eDHoFrkZ2gjr-t0wcbPWYuj5TSDz1Ah0x7bunfkv29qSsQfqqpoJfDTLTRvgXYX6k03-1mJBUbmklJHpjyyZSLvWF6oJ1oM-0GHRTBl0P8nQA187u4KQAZ8mIGPPWyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUoNsoEERv4xqrHtuNGqFKBpGAeTxcmv2Gwqjwa6kcVbQEDgvg9SVseJ8gbq6j4IFQ1024r0KzynzCyIWzwCpoUCSsBVl6k_9_ubPhnMQOwZeHnJx0QK_czovPFOY8dJS9hLTihqafWZpcuW6ljUN6eW555XN2pBrHQr9vkrjT4YZoHvSMc2c5GoFrexA5Ti6UD6Cy5EjRI5apAhWUOW8AhuDv_LUvY6Dwsk-HFVZ0syP_EejFugGCjNlc5Yl1TKGSpZpH_6-3xO3pSttFVxACMGyOKiMr8uGe9yyy9hQ4sieO4xbGyaVZ7HPsVcPHjjiRDvPuExa8jf3FTod6v4Wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kePATWrfpoIiQZe2dNxiwr3KmOZ2otfQaWFijcjH58orgC-kglNiEI7Eckd02k2QkuG973cvGR6s8UJcFoPVKDoTEn3b7eVZrBxMGnRbLTTWDpmICfXDhOQ4CtVOfi-uP8jyhFbqu8RNNetS0sIK--ZcW4rYGtrR6jwObBK0y1Nz9F8hSyq2SqFEf3bG23MkfkVr7l8LeIkQ3fFazfsREo-8eCIXVvqL9MCcI5_eQFSmOxx4KlECuC4xNM0JZj-TZ59ABd0WC3zITOmLjZk0FAIXNH9sw3WDkAf80RDoZy31UtEsH4IZZ1W0GfNtp-yjC297LD33YNQdI4dHYLtnSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNk6rf6Kds1ZifwAzkgl5nxKQZ7yTwg8VpybhoLZ0O8V6Kyn3I5tibXCHMZy7ZDEIIbmEHgBbTFTBSlRa5NRPJ6KGm_svaz8rVceoB946gxyrV0WEXzKB9iBr3IQ7Nb1XWPCoE_zLFERliEdxiCUVjs-_rND4CCrY6W1h7WArVNraQLQQP3wk1UA13IMQNSjVfcLcNiM1rC2mL-C8af683qEwblz44398gO6JAE-o_YNygfCh65fpbMP_gOXud3B742Zl7JCwi5mUEWCfrSOvXH42ZsCmKn26dD5EMTPOcPSv9lShPH-Z7_HGiNiTeGXGCZwy49A_rlDlfnQzyAMwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca--rCmD1-iCzWJSknUOe9MYmXQUtEcKAkVXLcgSO9iTB2ZlHHSWt15V7NuVFF8wzS5OzPdsTUPcJDbtgvfzQUe3YotT0WknIt0oTgMy8LqCDq1AnG3I_Tinw8DDzkovfdnyN-iVEGViPxsXhRC0H0co-J45hK_1PIl3QKima-_C4e6QSXRVoz93ednB2vzaxou9cLxnfKMZa3DZExf5TEGxjPD3s_3PFoELpODicVr6kmeLDbhATIHls4wZ0Ek8rk_NqYsMjc-sZtj_gOa8VCQqZ2QRKAptRzmoZ3w5mwajnsiuXUUEvWGrWq3yaMtjlJ8A4Hv_pOBeVx2XYIzkGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKygs_1IuJzDQcGgi4u6AwvIilOpvR_ni-wPE5rPrnDUgqzDHiJp4v4-l3TjEjGDmgG00CpWLT4Iao2eeYb6ASILhbQc0BKF9RjYK-Vm-BSAlrZ4j6nFUEVOhvX5sXHYbeBnIaRMNzH6_DE6b2HisBY5_QvD7ktcd_mozyToVJWEUBybO68AEacXewctqtcgujBNELFyqPSCULUXXv2hxDsdfgEs2c_wQwkyNmGnoT-5EqM2YPz5oNDM9boMcmGwn1Tt-VoR4qjk4qe3Guli_nlsZefLdPxpNdLXYR_F6oah8KN4lfAL1rQPUBVBDHFnEmxerK1_iO_fwqO6c377_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hiO7ipt1fVaRiYGbX1SGHqCYrz4TPYYOvg9Mak25h8XiSdvb0hOlLNEhtahiIioonwiyvU9rpoCKW8ralcRNmKclqyWw7IUvZkTNcnskPBCSxnTvXf4J-ihUTEDl7sQiX9ue1MxWOc2u6Mhk5IFUPCbuvglyIbMS5UvRYE9PzuNHEe0SxkhH_0T6pzWtSpD_lrgx-s-RsALWcgpn1DI-Ig_n5qN7ijxNrpoAPUTu9Jr8Agpbo2WSjAQP2yhWKCVfpvu0uXBs3T26YLCJQVZGC6GYrbCu5mUktUxsMr0C10DjU2VZxqkGDJBjsjgphjMVKjq4LWIgt2NjDk96-gb6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3i5m3Kb_wk8vQXve-4lOtg2rwXkk1T8EVqO4zG3r_AqpCvszgs_KNAHgP46U9ispPCKaqMoVRbqMpBE1sEcnnSbRAUXHBDIbm0foxkQKNetnGzBVfl7b4HxHKBpvc9V4_yeEeA8hK77asdp5boZC3VGtnHvhnS86mnEfnBT9iHYCUsARRQWMRN5DOMw1VJcjsOUCBjBWzPX9i4_m2LSlL97n_RqlboALef4TVUr_nPx3MwG3sCIb4X2s2KMLAZMf5KryBYA7MKsk2WW_x2fGLCmnfEiCm3ryopTJaRUhAcrwNKMjW7dWFhqBdFG-8kuhR-VjmUI5iFOMuwIfduRhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0gNxYjiGrNfvrMKJTbPm2VRDsm5pgxC2A139KRXc8Ifv56HYIxa11g40D3rhMfCi9m8VmpTSgUT5b91C7-AgXfksUhFzJfWQJDFaPkzH9xzPTAJn4k4hyEspPKyjMgkrmVEZ2IDrpK7lmc1FO27ds3v-nc9NF08S9N_2kojf8bFRSTkw9lBZgAkmXp5jF6OkIqYUloLPVlTFcIoQ3EkoyVfIeHxvocWSWwDk6UrhpQwaA9GshxvGFoukMPb0mmT6Ewrt7cRKjnivJSKdugoQ4ugFVI7UJbWEu-fqj3wpbFzyfbgyJvYQR8pH-RIc-9BPgSygAERXLxxV0b2h80_VQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHPb-x44ovrKE4ePW5jlDXeEXmgiBcz3tt5Vj2PDYs7cWkSVUPy84LB3ikAxN8oc-8e0a5snVEuPfENGg168q19VUnZStdEXBrQlt34Q77ev85nvT5TnDjAqU9Rm3G8WiRYIdT3G7Q6_vXXS8dtvcSKWz7NLBkGiNGleWfDjZJBhPtgSrLXQcR-521MU45QI3AT1pY6PkIdxsTWTA7ia25GJqs_5Nr910rQHpAc0vY_9QBfM_GO52BHhxoNvtDTj5f08ltJkkoIVZRi0W4YHwNOkNTL4p6gs2uqOzC27FG8jMJxeR22r--IP4gAaCl0vgw77qsNe3X0FOm8V2-QecQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPvhjb3Z9VNdCy8IcJrA-UpuZgDNabDtUFHU2JFAp-kVmMvZqoUb-WGcTFKsetfExcQ6WJgsk_WNNw2wOoXj2N2uoHv14Jh1gYb4DnB2l1q3DP3d_4-tCnZrbHytZN_0JNigOd_agMa4HGFmvL0Vs_yoFSFXYBgNriKuJ5xJBlRyWs9jQuXXYPL_EF9xGvuaio6RpQ-RWbjcbXHWtcnkEfVTtkdolpeoQ_D-BR91j3CmBkMjgMboJDNU0Y-UZ0bXvY54Ouerrxg4AGuodJ9XaUKSgrJFOaRe_exN61vpaAwMs5oZ1R1JUC-9fPQfBKhVLx9MMIF1WmtVvGVFCCO3Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1xrQ_qcY9lB-ql6ikzuvihhvpBbNJsT-8ANDvBWGu0pgyO8kZtwcvtcvfwUnIYB8jO6EHNhCOny5WF4ADZoqCM3EzGnUNM8GzrVaZOEOJ84RVKcTzSWTBpL6zJNGdCU0J4zRsoZg59kn7XtdlNpGy-Ho6fR8DmmTC0zSpKy5LkWMQNaFHHaPq5w71fPs8Z_6AUj3MEloFBqsZCuuBokAniDSkiagTkrQHRJZ3iCqLJP1XMsmcttoM67pQCaTv-vjuXfVppyzESDmeTJAeLn1Nl6xHE6M1_z5ynIlac89w95IUaox86fK9Av9U7X_sDK78H5psZ8UhiUXfBc48-9Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Af90YqoliGzGLatElBcOvV7EME-ZtkrdBEapEz4_BApUinLtCNQpYheEo5-_krqVhRQTyp3qBswkjPgJubYJkzLvgSV32BYyeW-JsI5TpJ1atMu_t_UFBYEwV_t5w2PivtEMlXpk6pi1W0kkYIaHrAEYg5_VC165vj1jeY9HRiXpWVDut5n3R0k-CUxNz0W5Nr1P3-QH6U_DqVnn2N4WluoYwPqAi7Bz9JLD1yYEMBGAp02n3A2RDvUuhZ6E_VjQ7lR1XtquSzdecqiMGadmGrhFj5DP9ZU4Y6Qms_Po-wPDjMUnSogGGm7Q2RzI8hJcQ4yqtznpDKKcAN9621czGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSzxo_GWcH7PoHW87_KR8xKYCvynJ7yQpKpTvTgORX9Bhr0ZQTTQ8mp-twrSigP9pMAcYzIQ_StkBtHwXS8jtBZcHQBb15txfzjytm2l2p35V5ndPovku_5G2gHMzzz8esoE5exuVP9p_-qimAAS3wJCSFN-kZDGe_HcLFlT72ZiGjBVTmBWeAx1dfTitbPmJnaW5JscxiBdhrObtYkk5QQ00wGFlSWN_bIJEJ2H0YdmIv2HpnjcOOcwiaV9KEFM6MS_WNlWpp-d7V1dD5mCriJAPSDN_9c2_bAZfuQWvdETRqBuwiEhUbv5-VGYXikjY3APjpxNbrZoOH9GDjV8YA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBbm4oKH0X8M5ZHdnDgQg52HRnYk4GS6yInl04aPBAW-t7oH5057WummYEHvh_zXtGt3aqtDV68pakRJmIjTQYbakDHq-BMDUhDJTlWeNnqp-axU0xyf6YDCgQZq38uTcMl_trYs3Z2QqMvyB2gv6yEsGhPoW6EPY-Z4N3yCoxEAjUKnL8CpW85d6KI2EJKNgXHZtlwb0UD7mkpX9q3Bt6hPi13I1IOWHHVgVL7FXfOj2tWUz1Af2d2uVmunkMH7CrD8LmDOtxcI7_NkwJngH4pa6pFbaAO0RDz9ZjeZyJnhOgf32RgakgyTZJaIXtigW2nhCjq1av3SbdJF4HBwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vt3I7uGqFkZlaMJ1pjAZfHl0muBW5mK0nnbNokFFkURNef6zu_-nL2npu9aGOfhFvX5EZeoWTWVPabtbhikiiGYqrsUTFSKYmPqSLnVZkDa1ek-KZ0MNrLDjGdkB5nFaDdLq2j6fd1At-mxHxgpfuZrLdVB77u_zOk7H9jAi_QK9_oeQ2YyA9X_CP48pwN45-a9B3jeZQDoS80f804heiG5_4CHN7SiS-oH7sjTM7yvswiTYSbQzqVoql4H0R_gktTeN-vQy8tYO3reSfvy9WrDftuRgbZPXzMr7PN8oonQRynNABmQpJ_Bp7679lItGZvToc-lqk2nHIUt0n-YbSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBOJsLChrYbVJk_8hKSwlCqr9BPxzlRCgKu4U_BNalpXD5V32-EZOX8dO3jvs1bjvlCx92CuzVdGrKqHLhe5dIjRuf2wfmPJErcOOmu0NfPyaFPU7gXFqyqHyLm-9N-dAhM9Gnd5vRLI4DXGKkx0kloVEWYXNgeKd70PAUUSisSiOVH1hYwmBxSHt_6epMY-QeVLP581gg4ohXwpmsfEqFI1JP68id_k6kdpq8fsvHjuWT2W22waVAnwzUV9lqLZ-K29tUP3U_Fllbp5invw1MTiXbtVgFWAMDltJn5Wb6LFxqLPaXgzzLWcl3jetKPrL-ht_2qFkxwVbUYuDOzS2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LbWOdNTVBwESsLx-htyafGf0HMaEz8hkUmq4ccvKw34dt-ZgsUDdcb-a2MwMNJS55pRZfvQIVCpLOWKb3-BiZvfVCr5bqjAdV6EZNJrMmXxtNFLmxr6mg6Vsfs8CdOTH8V0FKKfctBbO_HKE423uXLRXsmELVCvUK6TEphbYcZOjPstH-w5hF_ElsXpR8ypDSFnE_M51oMyuJ9qrEn3J2Jup7BJvtQwB2J5JdVMzEZxNgDVMHNk4roHD7NMIqiK3NHKDay4zEm2niF3FfByijeYTkdXioxIP5IC6n5QSxx9aP6pV6VNb2IGcTNz7hBZQunXP3b9yogBwj-3l_nHw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QdjXQNXQaDBRAr4sqlPrVE99o7VQvH2iCvvmzEocOjZXjmmqg5W80Jo8IxcK8s3LM9uW3iMyj302hdLQYgFNgcXrkWuAormyJsKayU5S0eFP1lXB4b7L6nXR4IMBGSwCVsQwHb7OE9rbKuKaQP2MxyOvRnwbFeQPL8_AmTIxXREp6c6K-m3A4NpdrQNnjWHB687PP1xR1-GVwnpvK03GE_W3n8N-grDB-T_FYjtuYASQnuv0cf_GnY2TBEjX2kscqm0uoEJX4YOzX1iKDErizu749zJvR0dvh8rBtr9qDBp_r3kuepwA0VEfkjtS1dl0BJ6au3TBxmye6wCOjBpQqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpvwZc_OVAucNgLSeUFkgRQEF4pnNeiY4sYhyg7euXuJirQ9bjjkgBgMk8Blo8WReyzSEEmc4Nv11CnuzqfsvrlpsYYmKBC9taeFll-PJXEhI0fYcQBa_sSPZ823Ur5uC8QlqFS3QHJEyCMxfDtqLoYAT2nRULiwFptB7xnR6L6-ohzlcs7uTiqwbQlT2cop9ZiD8CrOd-n5hCwhRXgueJ_Di0UQb8ORBSJmTbUOA-j7WCpAnUO0aYTMb2BsYC1YE_voj1MRjIrJXCDa1qRrlJveCuq6LH5n3durwW2JeCqQ1pENcgTQ9ZGcBr3gRWB5arFtIShzQqyBxz--M651-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApD_kS1BE_UC8g5alBEOhtoOKBATohTw1J4B8OIAuaDticVKoimkz-OratxhxFoQqBTngokt2VKyhA9rQYD6saovJqsCEKXssYntUUZ9NhreSYJDWnD4SLXRw57mlG0_F65Mya--dGbeVJznlG5rSCP1X6OqXiVzW-ErrbmPvUBj7XNa2cfPOoOMgyeKhpAPETVWaYwcLis47XpSD79eKHg-KDbcOYEWR6wqKkMvrXw5_cWa0eaW5_HRycRL9ZT4rRwOmK-YE_dtNGuFOhpU3Az2HM-jBTGyI2VOZIDIXl3C6ff1ulpnKCuqx2sU2ux68w1CBUWaRr8gSDtKzRm7dA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzyIt2ztx87REWN11zL0jNEzKiVusPCUUooqp807kxXSmNXjJXmIXeJ-cGrVTm8Wstz-voKO4IeDoe2F5QKvsidoqejIHxtW1yQnnwUCI6BJSzRpN49MIuGXF1b5IUO43kT6ImjX0FRDFoZKjc5BTAKQZ8QhxzjxJDpASvQ4A42FgUVkRqzKLmrFYMsIpEQrAJV1b_TdRmAoasnv5GD4_1_r_obWRzFQZAmdSmywlpZI24mhb3zS_UCMVP1k0s4CQHa4tygjyH3As5L6XSyAUBE3ITsxCGiuxm59723Z6q9QfFD3kAIdWFKJliGuUrbuzaI7L6SzITds7iSoIqmmSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlQ9eM8c3OjIFBNhzPRDG7OSvySzrlPXDwws5b1Oe87O17849MlJLiSPMP5cPj_4tZdrvp9YsdUrMERFxu72FX1T6jnbK45RDM0tfnGYRKsIhnf83yj3CQk8uR7pZAHWtTQ4KCy1zWMWvc-HMtvrBmmM4vd6lQB9UM78nF5ThB8A3p-87rOElDM8Twdg_JdoKrOlhRq5piwieDnz33OC0yHF_0ZBSKIEVysVJMx3pevl1kx8bdSUS0RUFT4oMujEKsbussrkF2-54NXcox3L-Xmo6xejFMOMOBIcsBtOJBUryYkllj9KXssGs8TFtgmIh4YxNa-dyTIDy1BYPT-3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBDpfVp2HF9WZAWEWOnrUhEYtF-PtnLPkv1gYmgxijkpJGgpnXk6r_Kh57JSUlSzKuSvyvyNxItuXzr8doHKUcrS9I-m_WkN_6-0tdEOBTqQDBar-Ap2iHMtjRAKwkk0aOQvC8XaiCDtPZtj675PhRgxmhODszY0YQjowwQWmfRaUQ7OLMpK1UKqfX8mAZdnZDhCnXRIHMqvJXukKLNx7ijFHjRR8p6MLKMCJ_UiUfBGpVJsqr9VMd_PKz6LXogyt7IkmBSomQzQXAzxzm_dz2hau7c8ZjvEhQ_OFH7LWeoAoB4Nw_uXVz0Hu7prp0VWC0elkURZRUVnSTNKhwE6jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzPDV-jxuPeMuZBMYPOemKNuu3Symk6O71hMFS7I_476QzJU7JiPMQIVbDOfeBPswdUgIQ-573EZenPNR4OJ4x9yZq7_LKOmN4zjQqn3k557-M8OdQz8YH09qO2HlG9XWlhFArjA9_VXFJm7CXellofhPK_jXsOWMDoxYmGg4YxKYGMUWCv1RV9MUUi3fIcJWfzJ8OSkx1zW0G-y4RD_X-n1EbZM6BB-ZMXw5t5c_fIiRduQtbMFkUFr3uUZj6UZ4jXsRxyf41s_bK4JMoAoogo7ET5sit3PlpcNyq_qltAIZOvjEbquKi_NvYCg6aTFNkOfd7Z1etBdmKS27u0G7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDauVahTW-DLFN8yX_5Tw55yORl_i6f6WXSbhN_s7MW871cf6yO5UBXHacauAzORHqF42N98q3WQScMuSU0oCUhhHzonOY2d5Zp0gFAZ4RmZwEpcalW9qdoio-_2I4CHlUlVOgedFimsktD-cZVNVWpz84nFl19UN-EFAF0uRPFWYWbMus7mK-E4bgYZhe0Fvmz6Oyic_ffZeS-6LLe1Fm653h2kY9pzTsRg2q5if53lHUXskj0zlN46A2LbH5zIzIkwYZMjpABTl2LEwaR8k5D6aWwxHl4p0n06AaiAPJOOa6HTMadUABXBierFbpBWSEpYoDbRse-BZztoZGuFEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkOm4fxa-Dz_qtJTsPf0ty-Aq4qg4YbZFvGuIcvsQZk8C5JdaYr1bbeMRzICj0XRr13FYxcmNb_Zf43LL5ZnRzkjVHKRYMdPYMG6yVst-661R2ir5BMcY3_REPisGfImSjSdSHCKPWvUeFU_vZRukPVYdAxuTtnGjCTfGDy_KEGhImV_aJFTu_vSGLuwTAhxlHGegj8swHFxjqDTkhT1d89vQWFmeH8XlUyI4xWjjtnZIsbCfOup0BPVQcl86mlgNFtPUBBNezxOX5F_aG62lATWkNoINwH8VWHwNA6meOlL_2OHlbKLxmcvdZnq6DZXs0MSrvUJjp6bfwfgehn9qQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDq_CTlW2m8Eh6-OtCdK17VNenZuT0lojldxiJFKTTCs1lcy8nVbr2zVtFttgzCNWarI9XyghN84-rkzoFluubCBF3Uha03PsxDHz54k84SszAw9XTCYFlfQNcjy4LtNFeLdFH4t2Z6w1De00CzeIuS8DJ84-xXhiiI9kiuZVPlZgM9sJzpxfgt9uM-yla063doSnQfNbS0Ub_AgiFrUSUZR3jKAeU15YbyzumlDAfj-CY8thHyuElFhy_h69sTQyRDZlsZQlTeBjfL2cUJRfCuOeLe7DSJRS33hhTPkxmbEUnVF6uEhu4tY6I4lbqgpGlFWJmW9bZegmMBjVbaZTg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=PhrzwgDfMMQTf0mcjrm4QC9KOQYvo4wGxShBz3y5gwptdUCpxdcRmstXzNzIm9rGUkIdUwJl67z-C9QUFhbrLTXo7GlBR9EXt1DywiEaM_vUMwI7JIib0pYbnrLjIn9fsUPYyFwIWJunHjUt0MW4-0u4rGiQ8d7YuKVDIEr4FWjjAC8aIfZcC6Gus4qmDJz8tBaXsjhCVmKu81xooi87YA0T3O5xgYqKf1nErJm38WD_mWC3tLYEozIk0kEeD8ITEImndWZP1jpfMk-aYtMHCkHUkw4DI3NnfpJQLd60cKATW4r5LZJqCGVr2EGeg0_rk1bToU7TOTnJP_ggmhQXsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=PhrzwgDfMMQTf0mcjrm4QC9KOQYvo4wGxShBz3y5gwptdUCpxdcRmstXzNzIm9rGUkIdUwJl67z-C9QUFhbrLTXo7GlBR9EXt1DywiEaM_vUMwI7JIib0pYbnrLjIn9fsUPYyFwIWJunHjUt0MW4-0u4rGiQ8d7YuKVDIEr4FWjjAC8aIfZcC6Gus4qmDJz8tBaXsjhCVmKu81xooi87YA0T3O5xgYqKf1nErJm38WD_mWC3tLYEozIk0kEeD8ITEImndWZP1jpfMk-aYtMHCkHUkw4DI3NnfpJQLd60cKATW4r5LZJqCGVr2EGeg0_rk1bToU7TOTnJP_ggmhQXsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHxQ24xB4KgaTo3Y9Nl0KI4IqhOHNm8RC1Xm52Wl_0hiVQgSJKb7cUylG8GujJ0W6hJA1NrZCRfVfN9FRFF_zodJqEJ_k8tKUx-R6uDZGxBnFAgojGZTw3S18oRbpHKRSZpcUZ99EqxR-bR0uacS9hwX92N6C4TzVI6PcKyNfZHI5cVr0ZRghBnkKodUieNgfTyuH9CGdmKrHpsFgg6MgWzLzliAT86N-6pWl2Ul2Li3_IPcZjrEEMSiXKnDj-24OWZrXA2unP72qgaPoTiOAKiRRWFvVGIIcPFy4_X-k8nMF_uwDdgl76GanPAOX843W9IuuJjDqCPg1LqeJVD31Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-Z1L4v3J1ref_UTKbVjxRtx6ZS8HUxaowfA8Y93wcR1K7a-EBspG5XD2jagT0OObUaSj4D0JvZ7bCLaHSqDLnc5PdCf4wJE9QvCVxugiWEVE4MGe1lq863BilUGYXD-YYSY8EbVhyfmC0Lq79UB3w_WRJKAPIp6N3B-Ar0mOxkXyjVoX9DevqgjxogKXAlhoPhZyiokXLD5jiGqjNWr2cZyFjCoKB-zVZKto76d_wB49id5J3mgkiL0cOku5gfz05OcUqMm_gamQrQWcCRYQm-Al1w67p6CajHoZVBCrt-LcfVjqquKznX_xD44_JDLV0CHwdr1KjqNXO1jrsBMzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dy3jwwScBy0QCHqRaxCEQQyAhyGU5UDNhAFYNMBLyH9hlOEqYhYR7IWInoT7yXMJkgzha_-a1h9DNcULSI3JqeFVzTldpXZMlesQaSh8XkQfBOeS7mA2XHPJyMF15xMUeRmL8ukjiy0EiQNHtiifKgl0Yln6_pb_JAu0vd-tYalxcWbefFRb2zav2o0JgXILnoRrNEYzhhnWLgB0XyFSWBNJ0gARtj--zMuKy8Tm3vqNzP72FaFdtsBlmzYAuDflHC02VA01zo-y62nW1wygJ5vudgXOhqP6rlmfMWQkPl8ZvhzJP_cLCBGAObuIbV32i5W3xGwcJYBJi9SwUlIQHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eW0IzmoaLVIyZfhnGmMkIL0WMxBqPh2XXAw5Hx3-P_qkSPNdIt6yikynrGD0FJMXaBIlcuY7BpzU7eNFdDlwaMhM7idr4g_BpGAI8wAgC5khaszQwBAgooTTg61h0LitZcJebUFslryJxDstItPgeXNHiq0KmB-TpbsVP9zDiNJhnHJyvVg4cCUh8dDlUAn8lC0a84mjhYEX-wmd_ce6ls0kh9uHAYk_a9EjyLrGAHPUJENZ6DBa28zB48hG9kQ_F1u8rakfRHK5qmdz_Z-Gkgz4opmiswnMQEHArDFQlOAZWwczCooqeC2CmW5UT_30KivHBh3xIxmEY1h1nDlmPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/crqGwmO5B4vHq28e9hP4dyICj-MvaEpkHGn9X2b8r8R8SdU3TIglEcS02QGw-hBof8mf5NND90RneKjzkOEgWMSFl87EdWfVI1pzWnbenKfA9B-Dl4p9acWbKxqa2tEe3PmTA1VuCqjmHjjrO1c6wlSTmvoTTAHa93VfRrvNfTcWc0GbS6i-ghWZvPQunPw8VYOTU4saE5Fe4f8YFMOQgKBCnmf7qxpF0jCeXkRj3rQoZMLJknZK9q6H890k2juuqXjH-6p5nWRqGNR7sG0YmXpVf1SEhLlyjcTaBzuMlVyICPX70YgzLMAI5MJ3BRgAodZCjDQCLgIQ192wwcunRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bC0E_7eQnkGXCwv5ZxnUela_GtF9VVzOP7fm0o32d4gmreoYIEJemc-vcINREj7Yk_k4r1IZtQ34Q9N5u5LCeIOvcg-QrZ5U54yUCIZE0fQ48cKvF71FfI3kni1wn2HuboaelMG4xiSqemLNO2yV13SMVG9T_B5GjVSzjYtgVUgEfmlK9v6p5dQm6AXwcLyTi3P4ClLTmumOM71bJyYb63fZ8qgRL51jpU_k70eWN9rg3APfNI2hW9zcH2xCyQjH1s6fYC5z-lOAeS8IkZUf70-V4f4k7cg-5e4ie0QP5g69x-9STYMxjBNTjA4DyrLXVBi6HWFBKFrw8k-803aJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kp2yJ1v9yOixrkFCcLC6qYQdef4C10IhedWeKvSmKNbIQBbViexmpTvMnUTzrD3Gj0ikaLDgDF3Du-18CVf2weveWRvAXRXackDG4fdI3qaGU9cEeKjD1L8Mz2wX8qh1dH5mf-cUEgoiKRakKHL29RQksfBBrbbUG6kPkZwrbI1NjvPzydXacZp15kRxLn4jlp28IhUi_miMo362Y6RoSCa_icBLuQSCUatxH4B7uj7QfDCdOsTTDcUdQdAhKUcrpvy4RPRPCIA4vx0SwN7UNBuW78p60Y7oiJnJ0T98ST5276JSiGPGz3l4onMUnqFNnhlZLazRKaB0KMEy9ik0UA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=cNkgYdb8NSXqk49yV6w_uqf7HQPED73JPgV82VJuPV92wk3FODEIhKSk6e8lOAWD3gSsWXIiDvddC5gFB110aotcWzK1bnpUr2cM-9hm0p5wm7v-23PQD3OI6mAGOpNbJBw3LntaEIzRL45XLnpALCI6gDiDkX99NBBxzSF5ljOFxjoFZyYkoX5JC-hW5tw4qr9RYTGGtfv6QfWU_o8DMfqJL8RvFaKUNFkj07IiAmQp16PMIrCi_TMnAj1fUORP2QtLismusWsoNy5S9Z9hkCnS2QMLA0tJ_1xPkGIsJi3jXUYDcgle46MrLAGGRdj8yajsTyRsrIt3JqcDxrzEIZMsdmSjsoYd-xy-I4WBKXpoqHTETQX3nk3GyhY8ZWD9o_AI0vFmjCMrr3piepB8OmC-LamJoLRvNDUbYdyQ-6TAodtDijDO3EntxnI3RIpiucAWRH8BX_X1i3-DtxiNN_vYPHH3Ni6RIi_hW6G_6xFcpvjEPQU8AEEHH8_7zTnScMQXlM5xT-LcAFMsE8t6P3gT2dwno5z_8zuZQb36sZ2YuofgEjHyZF0sMfh3cCuxk54276Eanb2jIzi3OMLLPCoNzegid4CDAPQLzWhCO007mwAmYDCLNzoP7J5HYcNO3AB3hSaax5N_qWW2LKlsVb7E5Yu3UufI0D2SdDde2-M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=cNkgYdb8NSXqk49yV6w_uqf7HQPED73JPgV82VJuPV92wk3FODEIhKSk6e8lOAWD3gSsWXIiDvddC5gFB110aotcWzK1bnpUr2cM-9hm0p5wm7v-23PQD3OI6mAGOpNbJBw3LntaEIzRL45XLnpALCI6gDiDkX99NBBxzSF5ljOFxjoFZyYkoX5JC-hW5tw4qr9RYTGGtfv6QfWU_o8DMfqJL8RvFaKUNFkj07IiAmQp16PMIrCi_TMnAj1fUORP2QtLismusWsoNy5S9Z9hkCnS2QMLA0tJ_1xPkGIsJi3jXUYDcgle46MrLAGGRdj8yajsTyRsrIt3JqcDxrzEIZMsdmSjsoYd-xy-I4WBKXpoqHTETQX3nk3GyhY8ZWD9o_AI0vFmjCMrr3piepB8OmC-LamJoLRvNDUbYdyQ-6TAodtDijDO3EntxnI3RIpiucAWRH8BX_X1i3-DtxiNN_vYPHH3Ni6RIi_hW6G_6xFcpvjEPQU8AEEHH8_7zTnScMQXlM5xT-LcAFMsE8t6P3gT2dwno5z_8zuZQb36sZ2YuofgEjHyZF0sMfh3cCuxk54276Eanb2jIzi3OMLLPCoNzegid4CDAPQLzWhCO007mwAmYDCLNzoP7J5HYcNO3AB3hSaax5N_qWW2LKlsVb7E5Yu3UufI0D2SdDde2-M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KOZVGtERfWWLb4Kmeghs4iqX9SNGXh8aKaneyegADoLv8phzDloCZxDp2SZJPm1x8Qm4JVDfDjCvZ-tfX8MpG8LZ8J4y1FtyoPwDCuAiW-tNn8L6yPD1gFfCNgrMwAdE-JkaMNP2OuNVyzHdI1zxwFLoPdtQ6PA1DzLU2_tCgj5pssNkoR2rP3aJd6DNOkWDppz6mZrE_vt6FmpmzX5CHXQUvXvR9CH8GvTs21C-mW3ZKGq19OfyHSTeeERQzpDhYf668mGmTavU8cRZPoCdk_CudlaWnAZ8C1QnimzRIMHuqP0qlXBO2X9SSnk5gtU3xsvAWD1r0ee2R9KGCtH7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbeFVVZKI94cSCb9iHZJctIYY0_MgGy3GJ5m1o98O8o_ZvOxkPZocnhbqFKTLgYJPlOpc0rLor3gW7ypUneKYe9Lqqzz4mu8nJNFTL50Q8xG3rm2L_106_OuWkpEotvbw6Bi8L0Y_ktoDPfUD00XWSldZKUlJQ4f1hVM5ckKJBn6pxCjZa6twg5QcwIo8E_JMtzgYLDVGHpNCKw7dbaH8YQWVRU_x7i7eYdj-n5T1XxJccw_E8gADRsl9g1G-24sU0gIB_jRqbW8dYLfqmiaYFo2ABYT5ciWR_ukW8cwHzrvRLiXTxMZsalGxHHr7QJQfm1cMhx_KpqmWOof3NshiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AFdVqgDNPZqQTvd4jyWPqRKAO-ePjgkHbVC-c4Ippz4HtorHQOi4WbdtfTx8RbcgcS0NOx8YHsMh60XcwjccJwerSeqFfE948Jz2weFbx9CLGFEEp0SjcKriMDutUkHoVAVN1kBgN-vjW7aZMiBIo-t8ubktDK6Rbr9xvM5Bnej59gSUX0XlSrOlq00Gg4nDsn3wnXekJz0dJTjXTpTL2Ynms5xvkbIuFf0EnIepmqjTCPx3ZouKzZjfFRzuDOaMTimWtl8S5Dm7h1Om9TpGCjtS-J0L-6KOvTB4sxeMJF3FBk2lMCGlIAICc_RlDFhMY9JEY7CML1dp0sR5RInlWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6oP-gdn4TUNaWMyapthH__hX_YEcKKQhc_kzNZvUiWNrVC3UPwsRChTDjS9q04XmDmzQwmP3XNNBxHgqlSGRwpex1oNp_AzDCuzAP1M9vQc3sJK2jsqqBi4vlz2-Nqwmk0oPUwprYE2RdYTZtfquJnWCxYhb7-oL80Tx1DpHX2u5aQc_jcCFTC9vyYxX3Y6-G2l_AzBBr27nrJ58vqw0PWmkDnUCz-8wLMQNagBRuo4cxvNavGblkIPT95ztVIzDHIEJgFLlkVHkCxJlz4W_HgMO0YBoP6H87QQskM-kc5q76-zpOhaAAJ0VD8nMjv1VmtXJp1f7jhrUHy2cabMIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjMA84lXvVoA3QRFq33R0ofrJCEJA3JsYUwdzKY69TcGrTmoWQofaBNn3fFpscwVmjHnm_PqfKKMS8hy4V9IKWQnalxvv7-QhVEDCIXOKpHWMFTrAOOJA5W1a7Kv8tuyxHsQ7SUnwZYhFORc4tqgSnCgAkzn0mnjCB0pV59C0a4OGM5txjs5dWICRuGWpWrxcGnNd7eDSWX73UaY_sO-xe5ffjN7Ebh4ebUyfcB2EP_e0FypMpQjW-lMzb3r4GxQrYXCTAsidNK2RtSjtMo_jNdTDGn-VU1A6Z6FS09hFroq2oYJha6MELYMTmyKKftLgQp_AkPuQ5djkNceE__59w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUWbP4PaKb4arTC0UuGxfl87eozWRowupeybnzmiK-MxkhZQrTZ4v0ODJ9IXjRK0pCEpmNE6UI7V9zt8dKV8dTw4BnmtemXptiTKuvvG9L9WTGed4mYLMJI52SfPEAbSqyN26Fpnq_Nez64wnEqdOE3RovM5NF7lthwPd35tMLC12nXMRgUr6RJtTgEAF5xAHkFBF5Fl-MHBKIF658k-2tf7eze2ysfbZT71LySjy3cXWBOcdAT3Q7PUtpxQr1vQL8osnQOk3nSQxVv48MoHOU6zj9CY-pf156yaaj1MibfZ66aD_EMsGZ1anNwbGRQjPqDJthurAyn1llGreEPmJIms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUWbP4PaKb4arTC0UuGxfl87eozWRowupeybnzmiK-MxkhZQrTZ4v0ODJ9IXjRK0pCEpmNE6UI7V9zt8dKV8dTw4BnmtemXptiTKuvvG9L9WTGed4mYLMJI52SfPEAbSqyN26Fpnq_Nez64wnEqdOE3RovM5NF7lthwPd35tMLC12nXMRgUr6RJtTgEAF5xAHkFBF5Fl-MHBKIF658k-2tf7eze2ysfbZT71LySjy3cXWBOcdAT3Q7PUtpxQr1vQL8osnQOk3nSQxVv48MoHOU6zj9CY-pf156yaaj1MibfZ66aD_EMsGZ1anNwbGRQjPqDJthurAyn1llGreEPmJIms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRAB9pdhQOy2pv299V5slDRhwvJz5g-AVtJ2I1b9Ij1VDo_8ztVHIv5uew15dg-vCIOZgZ2D3xTp9TVBzABRQQGqajjZx167i9Qy0AwddxXV5N0nT4bum0BFFiEKZdLluC4fSQxmY3Rmk_8sgdC5vl_evh0iLM90qtETEnuWh6WXCLKkcOvpNP_HETJ9oy0fz9XI34e3leweIPcrKkYbOI4kNmqGJIq2QaimfolzRmb424gHqty9yvgCzeK3nERipfarMjvd9ID-1cvDJetgDt0SiRbKs8uR6qNpxb4sO1Xqmw91QsAMKbDiLoQpdB2wxwXPddaNHf3LWGBPfZZ52A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5ekZz1FS30-r8EK7e-mfoPUg9OhlAxHs8zWaOO_Ol-jHDR5NLJ_xnDQIMjTMpTguML4XQuWU5gZr8WeGgcx4SQLc5g12Xuajh0PMJeb6fL2OncDBAfwK812oOlp3dwE7IsjYlBRYDBnD9tEbOg0h5WWfC5DT_xfJRU_FzB8dBHoS-JGgb_XrjN8kFSSmYsoAX3y3-PfczUomxRtldAMSuRCgrLy7QJNi3HjXcJHIwg-yP5BrWRIQS0Zh-R9zhxMB_QOcbCDxcCe2spXgIATI_IUlPdPPhY363hs4HeKqK1QTBSJEwQDHx8aM2ACYijIRPEjlxy_zVV8s67K5Qg2Vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nBPd_O_uMWWg0StDp4Rrk0rpwOWws34OytZZy-1gPjUbSM01LSj-QTHSJoDLao65I3QGAjvr-73l4MU-Lo-TJw_ouMmc8B-OGJGvNovSf0_5bn5kJGnwJboieuWQbNx7SXWU4otKl5r4Kqo_NfYU0syYEWZfRj4mBTozpEMkw5WZU08QoRZbahdNTBTw5UNv5Dp44vrebETYoMGNVQjgXpHF0y2Lhj6CbS2vMDCI15V10Umi49Ur5t72al5oyH3WtqYOaN-msNMoTEaCAeMV9P6JEihOr4bjyKcqOB9DG3BO9Fp2KxZ5vhnU58jWfct6BBi0aglgMB3PSHyii54mbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1K8ze8xfIGxTXwF_IepxHKj89b05K-UA4UUEmUcr2McmkJmlEnqI6YoA7_4srGzOm1SrxOBman3kZaJOnPPme-sRfMUmog_jajMGBoGHYdnO_3FJX0XW-l4yf33UpRUsXV0ze8aEKuBHvTNGH-N7KzFQPwPuzHR73-GifFhzXPYxs8Kmvn89ogN55TelVYb2LW6UElF71sbHB0asNPxGVczMnpr5O_5TEqBvsfo9OjRTegcrTSLW7v1OTmxbUtcAyw9XeAtL560ERTEnhYjpPdUjX32WQvnGmGCiWYdNgETD5MUT9jfMmTqNYMMoZIslYVq5aDGUTTpb3vJD_2OcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BbN0csjrijCeyQnCqPeSDizlhVtbIhSqmxFTywGDHjrDmS9C1vtk043dYtRCNi9mc4eppma6xrd5cOLucyW2X4Ia5CEUJVkFMjrzssJHDErPHwuEjEiA-ZRC3-mWJRuKCg5n5YXnm6Wl17STiRQbR--E8ke9MRXnNM6ykL6nw7N_o2pWtKydAXNivQkQPv6dfL-MC3RM9_Cv2KqoIsb1_W6W2Q10dFE3CkOyLShSFaxahVVCqgPjUxlQTDrfNOO5Yhixuy2rknOLd8_kzjf48Ke8lS3-MK7RbOq_P3Y6ckrYBbRDCWeLmj7apuTzaT1EMQ5iVpsoOvHRJc3UdSkiCw.jpg" alt="photo" loading="lazy"/></div>
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
