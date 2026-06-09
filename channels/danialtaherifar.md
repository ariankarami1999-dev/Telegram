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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 03:18:49</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 226 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 277 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 336 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 481 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 969 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQwusuJPQ8bXQyi9bsG6oo86k_692V85aq_obFBf-88zgP_gLqDjPuP-2UpHyTjZI1Pqshgg3R0yWhVwrxqY5o0RrwDKWJV__PMOhX95K5KO7tPDydQ1Lj_ZIx3afpdRlfl-wbdDl0AdRjP74RT5J9DrrGhFiV1PJCCOa-JdFv7yv7jkvVBqnioRdwcXua3kMDJCVBdKOpVRgqc2sKgjmOTX4bmyZvG80WD0OJE0W5upbZwPPjCPtecMy-eBU5iC58jRjSkEQxPEwDrk9bGRHPQ517imRcwJHtIs6PF0eto6MCE1uMfukcuaZ2SwAWVL_s5fT_GyrbVTQvitIJp8Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5bCv8M-f1reZC8d9NvUC9QFXpb1IzLWcH6p4Fbl8X1I5PZ00Xv_mVfZxEv1gCEHoPMe5a24l0FWNyImITm6WD0Bcc0J_Y0xSRhyxzAU0UQ-7crfdpqFtJ00pU7MoAogc4iz6MBxPrs29YVsDTEa7tWuceg5q8tkJxcGNE6YJK8e_268Kn4jmKbk8z4PVZZ1MOG-EDctfYwO4P9B-OyYmE0287cThz4nKubz9b_epeDENxk97JG3VfRg0ynRVT1Q2zHKKaKL_Tcc2GUCJ0wPkNHrpNsJB43p_c4UcpsQiglU9G1BlWGiUN4TLN_GO-ZwDLK6M-uYzfLjzVizKF20Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 963 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CatVxCJhjU1hdm_KDqeUjNdNJnbrXV2NmJKNaP3xYyy6g6qcLQMu5KrkAKV5BxSY2ZBbKYh5gvIZJqo5c1UqsjsxNP-uibG_qXztOqUDO2KF5PdJjVR32axKKIEKHWXoqqIqX7yxxfW8-5TlHxbB_SeZN7eO60V8o8KkqkBVpz-H_DtZT7qJZh3BZBh24Or_a4yaU7U8L1Yd4KKYMaHH1B4Ccszkpv5CopU_PyJmdqQAlaIcamRvBsUBRmgjDR02uEZW6IlpdVrVHrSjvyweCrZGqJkaQZuGNjM0r7LeAjYL_YGl4L00fShRqDjPIaqwjzFokwP1SrY1NDm3f2vzvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JszXCD4-K28bU0iUuHlY6BlyvszfPx_ZXWsBDUQGB6BksFc9IYvk0ni9R6dw4KUMgg92jdQREcUB8xzzW1jUHUcfdB1HNW3MTHH1zbBOcSfj0PMaqZlC4dregod8uS57cdKXSBEoA8nwD77Y1eITerNesWsXSdM9jC2mzTpbQQ1mOyCpEw4dLkMPMtHtUaDzVkCQswrOrU4R0JC3udAZ0EAXpiJWHGoT5YuJYdCrZaRxxPNVxKYXIpsYPswaxRjnycRlCvivP7BchcWsHn4ts0OdZspaqwA_5WQOcBfORNXRFzITp8j262Rmump5cyFxn9x5HNAFrwb56nZV8grqmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntCq5gA6UMMRgTysjpgkafCM3CLaGrJALc5CTAHocv6j0Z_ILnreRW61Gnka0mcQGxIp2dGgd3ZUHxxG-__GJ8MOlolcIyT92WtVwZmynchMHM19oVytKhM9mBFPLz-7y7VTzkGULUBucBdXJhUvPNqKZkS9C4PuX8w1UT6YDZofYSWmxP9A1VBNOkx6OslP7p7-pfWl_jv2rz-VCQ35aNYk7gDgmHo4666jvAlQlpYx-aPeFKyAQfoqKWD2kYg7yqs_-fTbgYMglGo-USktDpohD77G0b7Ch2Y4XcC7JBVQF_BXuyicp_z7NjnjIoR20Qp6VPy81Ql9lGNqgviSag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm278i21QqG_-ilEYEStw620qLT8k1-ShiUJ4WdfhxZXe6vkdEoJ5E7ijbmmgm3_Hib_DbF5aksarLtjDknZbTolG_DjNQIpac_-Rrf6ELzBvaQ8jOEnWmb8P3w6eX7yPjxua_yi1CHygAUTZ-NkxDTqwPitM59wSJFRL-6bq2nzDEYKNllxks9oiCn_tswW43H-IXVchLQ1z0oqtQgsyWWfaQiIVFky9YZWvKNjcCArC88ssPdb4g0oOhmy3FTcEsDqBQib7S6M0K8-himbLQpGRv1tatU8ZaogA2gllL7019WxiPQeqKA59gmP-YPdIUl2x71GnZAJR5Ag7fQSwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4cyFTDpRGCI2xmjTgcwf9N1MLwTExwgyKdHgYZYr9wNODXXEtUV05Ry6L4EjYcBNOSt1kUqeyrrPbffUonGySwC39tI9W31iwqln9b4jf8F3on6iNxu1b2BknDqwjpSP0nEeqBHS5MaAWC_hjWXFUwRbb-R2nLxdVVnHMPnVvSh8G-H-IRRPQWxBHK5Jopi_mERH94FCMSzRfZPiDChq4Ak7hQBTFnf4Ayu3Tv4iMnEwjXA8eU4GYxOEI1Bsuaz5djKNdq0KQO-JRQlcJRiYGehuObNKvlOadTCa3d87w8jITuFb3ifmHavaixR2Y7-1MSdaxrllEql-rjrG0BnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1IobnMv5-rRJqkKa-NzS1u7YpSZQq-_JtfUwapbUp0NYR2CmDFqCiamSlnMUYEjIu4jIKAKxg7Wr-i_ypUjWfeWOIloyHYibjgo_KuaBKwRLS5OL2yjev8L90a_bYaIXbSzSJNONhy2gwwXrxaJ2X-645bMgc484p60Gmq0-MPqwuR5hwpHJ3MC0b7-0w8V30NaU29E-oCMrJ2cM24qWGo_Ynlg22Duqg_yDwX8PbEuhvIyQ4b0IbwUgpQkO4mwiBxKCsbYKw-0ytlcMO4kcrrc9eleKn9eCLAwaJmRbXaX51cNm7o30DabCRjGirVTEYwfgJy8sPYnAhoyIV4xJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnvEJlQavruaHVMchXViHJkVPpWsbweezXAQtihKBG6HsK0NEjKU7NO4RJGfgopJ5JiBJ4Bl4TueoAJBqKetY4lw1qols0B86itTC8-I0hGO_vOhYlW7JTRGdIu3insms9YrLxTq1lwFom99uOzbaz0UGKXNQlykKJYwdBfy2grjljsBgqKSKDLUZHZeF0eRXdQxQzOMsuomMpdyWuMTqvZmj6E_bz4BvEaEzLtk70SPvgvWM38n193GDL5swFn-r7jxTz9pZPuaOUQb3usBfaLMfC2uWqON3TJJ2JpQaXbqATHuGNf0KHIGlaKlb52VbKH_VklOX8Ncnx_cztfVYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERUe-o365e6kI-VrYvCowlEKFyTO_bRogRPk2SV0Z6B-nhsUGSYQELA2UFriJP-gioAlwdyZxQPZFa-9Pd2Oai2q9-50rgzUJL-WkEJlW-C1I3i0dMzC4R4GxoGC8jRWQIrSSrGlkQX0kOTbsAg2w07pFqCCOiRs595EZlwpdbUglC9P7WxkvUwqv-sfYG1WhkkjCBpLprEL7ZUN7ICAYKErVeKUar9dIMwCJG_9zfq3H7hDIxicG1xB35WWxUdxtZGMEV3NESCx-150N9I6j7sxBa1I_HJp8TUjXYP2d-R5JLlZsexW2KGazdgcH27W0LhrLAABolGx5iSpauk3mA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcmcdX61UP5pzOVKesTvR5pod0a6FjrmTqRkbr7rImbR4xJrPY5hdNyeE5XAtFuatOmVvRJv_XdXDsiWj1vVU1ED8j6VZ46i3jwEq3ZENzFdoq7eBA61aFCsb6wWTH19ZBtMiXzosbyzz3vNI9nXrDvh-7y_iSkwsl0nuy7MOnZn9N8-B_yAwoX0EhQR2sRlSGs14ER7TVztBaX5lYoCFjGhOdI1U3Jzbl6C6ugAvM98KBK4ISO6Uc-FDIQM-81pi_XtmLZorUcITc1H1S0_-YD-SSFaZFkYd5brLxjbFJln_wfjGL0s9u0QfmiVIeVQwVfbqMDzdNAaogEo6E2PaA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=au14-KkDwRwvvL0zL5heIZzsPYfyufLD2i4WFy_mqCWJk5aln0VOpg5S9vxpefOEDVQbRjSnbAUzTojnPFipK4FaVIxR0Yxyqpp7D7z8hZkEak6P_U53mWOghzrPJK0x6pUMhJgFmix92jVUpFSdPjfxFGmOwd8rQsrigCiQHi2_Q9rU6NGKSrajcgPxM3_2xw5PYf-5nw3IDDzDI-vyUZanzwRQael7pyax46ct3fKjFcRULkwBlQJwSFvvkdrEWokefHKnt5HVWuEGE8vKZUAPwsF7QMnPoJo4Ggq_UQcW5PL8-f6NuxOEmN6PwWtuwCi7CWG9oOSHFRKL9l0Tww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=au14-KkDwRwvvL0zL5heIZzsPYfyufLD2i4WFy_mqCWJk5aln0VOpg5S9vxpefOEDVQbRjSnbAUzTojnPFipK4FaVIxR0Yxyqpp7D7z8hZkEak6P_U53mWOghzrPJK0x6pUMhJgFmix92jVUpFSdPjfxFGmOwd8rQsrigCiQHi2_Q9rU6NGKSrajcgPxM3_2xw5PYf-5nw3IDDzDI-vyUZanzwRQael7pyax46ct3fKjFcRULkwBlQJwSFvvkdrEWokefHKnt5HVWuEGE8vKZUAPwsF7QMnPoJo4Ggq_UQcW5PL8-f6NuxOEmN6PwWtuwCi7CWG9oOSHFRKL9l0Tww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxNxDIY_r_lYN6iyC7BZGInZVRVdeIp3jX1LSGjIdHomi8xbn6EQzdUb-oEOLMwv1Db0cAcqTWWkEXB_-rovkDA4Lpyt8I2LSNMgO2foV25sQU0aDDxphxINbIzsEMTfquFpAMQ-l-_c3iCN_EfGx6Eg22ehqDUIW1SZWfJzcZeqn-zhUuF3LWEREfAP3I-u1U0c2zWYi812zSb-3DCt3KU142uRn5bcixXLuueYu2bwVZMCFybSyIkk6P2MNxbRd_4mwWdfksMvixYfbC0e0a_Y7cSlHbWVylvpio58GaKa1Cu5_UL06rKtfZIwxlMR7K2PTeb0ieOqxjKZ8EEfIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIqKovItIb7ycqNSH6hes5gt6wPAxa9z1vkxP_A6wcoPVSauMNiPNy0kMobyi4D51jSo8hT3Fvx0fa0KrLgS7fT0Zmgjmi_6TuXR-bWgcgwVSM69iORI-F6u09vArDpBhbcPGXfqvfdYhObTaoHmzHmhUJ-9-pm7x8zsnrlpaUsR02HszHyRJNfzDNiF29ptt9DLhjBuZgFeCOfBt-Tavm0pyCyjfihQKNKfyWx_eT80XHTfCFBc97CiPv8XIa9W8XO-VCm6r2A3kSvB66s5eGMkz2JL5Nafxhd6bzti1_xXvEUbKpVnIdF4jmcgWiTQTOUL7wuDW-ITuFd1WyWNKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QcqwOlZqAUOc-QE0D9FwG247wsff9BIVuVOgxstfY8KrZhTUk2UpGtFYhLt7OFacSp5VqwEjo4ljq-_eain7iYAjoZgXVIdV2Fej56SmFuBslJ0RL8kp7R_hUJ_E0FWoGNczBisXH7HPLO7RfV5RaDZtIlA3klD6tUrU0c0d8BWQRCM66z8iW0_cFBJbTZOEl_G98aONprsUM5TmluaDKp23xzWu8Zwm-DtnBeePOcP8LPiwAbo7uaroc7mV8kh3LvKosfvLIw4IyjLnh30trusmJj0AlWuqePsjHJJL0JqxSMSg4XA8H0eVLzPwd7nR4FT-3nKPu3DT9nI_5kUJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-uyTy_5pG4LHrLg4qNNfuzH4TjBUNEDgoyqDw-R5suPOwS7MEhd7aLQKwnzNgeNbh_90lZm4o3wLXn3YrlOOXZ0a3oBvFiv7Zw3g5HubkLu15XtbW6GsRsp-v6lWhUI0NRxiY2hGfzKVGx17zM2u4wr9nzQf8n9Un4LKNmlYb6m0d9-VkNqEKM19vSlSWlhljUh_dQIVH6ytg3Y-M6kbkZ3P8pnyGw5iPROsVuGqur1jUiPqqOp1wsiDGFsNEfKMgKy4TVCLIqQU6FIceboXT3-wi0J60tyWI45wnlVGGliUl2gdWcrUVugbYsT1RIcHZTar1ETQrH5IGbbv9BK5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPksVdHVxf7PhDCJIV2kAcstCX3Q8Y91AX5m2oYklb5eZeSF8Wc_NGMqkivTzTrj57kak-o5FPRvhOc5qAHB9vSGC-2_nUv66wMnRADdr6L3Xa4TbSR3ir2YohDzDmAzP-4dhUushnBqL8i0fWptYtnIOFjhE2-oq5maP_XXEQz_DT1Od7nCh43aXyJhOVGyBzBL60tiA_mHgLG0vFNRNaj6maVdRaGaGptphMzjJR7bAc_pA-chRR4QO0GeOMgl8KuafEnx4aV4K_5tHmRJP_O6s_KRUubfNVUrSnbn7ou3ZneLXhj2ujvLwJ0scoIDJtPEgMij7FXWKKc7OhqtBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXgEGpn7Mr9JqtTywOq0bmA7NDWMtpi6MWg1sp1uyDDBv8biwJcjvFfDanRXwDDMrdHm3u5itrA21hpFIa9PsgxgBqkdiRefhbbNvmWgdWE_C3F22Rlrjhu2drYfJL0KFmt49c8IQ5m3TjR1KsJtEegYCUFcMffK3TfrJIz9NA3aSdRcKukHCKg35vIz-kUP7DweHdyP3m459FIUvO0M4DT2ZzK55LOonhMGYAVAIPXciRg1NcaPZrul4eJJ-nYxEJJXooFAtnemETDhjspG7L-6LVUEQF7POuBKjG-Zr4jlYSWFZDhJFtxdQQMouwgXFMHM6mUboK3fozMvf31Vkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTUhVBP0QgI9_uDyW4gflfZ3Rh1vQesSS36DLg3jZrb4HC_PeFP1R599xi542wwNlHNNkJ7HdnS4Sxl7g-3l95d9CRJEyDNnWjj4LqNdCPJC031JeWBP5tfUlYJpUEWK6wRakZqpNH253wqWU_beyDOnbEoaKtUMKoQ5cQhsdMVgCu_JcqgO4G9ITTIUHQRYIz3RUsMoMmU2uxXWuzVVlPMB-lRlxU0kr-k1RvY3kYPg6uDzTcOujbG21aulG7KyK2pEGH5VQlKTF4_PdC_dzVjPTQBxq6Qy8uqwpqB7yfBSkaxBa2lXhZ4MWKMLLjEmtWFg8WpFZZQCr1gIhbWXNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FVvtctow66Tc-hNuJwe8OG4e02GNdqdz6DjscQXAsJ0pS9pokMmbcuDVE-sRGrhDe3FHZ_KQCRXUDvoJZA4KDccjJjtoeIXnytUgi6Ao758b09LrkQLXNGZam7l-kSjoR3gBLHApEvdLTgOMEzSyeFMw3fujwsWF2EMyxb8E_gOO8gGZLHJLeHAmhj8wuV9SduCGomIzpwXspdbxmhSr5nEpAZh2zIwIz3atVzyspZizIXpFXtWj6qm9synWgsJLi78e7mYBmx9QP8HZ2YNpx1Dis6jwfECj3wKJnljvWzSsh44mWXyepDB_x7ZSPjXcNmYXemVB1ujPwpCYpW3_hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPj6p0Mmi8ZvkHez4FcwyuKxef6h_KiZFEtS2nVFx_qkzyLQx28b2r1LJ3razVAujpOOPqmHEoZB--H1tJC8HBEoemjt1Mr9wvw4zWMceFFlyikZsZcWZbv1FlC3vtKuISGttvpz0o_nSCpCtP0VRQPOmo7aUVNP0I05OQTPyfKlTDZ0JjP14D411TQaMU3o0g4fGvnqrtRWbrj06N1DEJnfPrwwKHhtx6LS906kzg0bFp-4Hcb1qmHXOmVrS3SXF6_qK10iBaIYUFFza48RUhzm4rw314PSjBkOhonWdDY-3KmdhJnQRc4Eq-sdkY61Sc5fCBzkJXBgSSrWHtQViw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgOSxkhB3p_sS0EghrAOzE4BVU1Sl2tes2bhrBvgWS44FRBi_-xx7u3UY1r3E-uZZC9AWAK5IA7eW2FZ2MozJ00EtY3gd-WD_GMiaLymA8uO4N_7HiMqXI3MfD532yTI4XaZfNcRTnljWAooFmjiGt5b6P4hRLpIE0KsXva8l77UkC5bYV6mfQrjHjefxRPJLA38dNHDrDYd6Cd3GyvI-B2JvrTfYQq8wPxdOluneast-Xt9LkdXfjSoTvsZlN0xSKrOIo0osd73U5J1DzHmd6DxynAWLgITnzk0vawK7DqpQUIQqaj0JTzO_3_A17Dozbs-rfnxMR-StcAuMSndCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfExRkL5CFfqo0aRzRHChozW3q0MZoD3ma3-xFh2w8bdKL0oqloocukf2WbUExs8XYx8dZNNgeJd7gFEg23K30P9OsfLqz2qJxFQMFiISD0WEfFX8SR49Jr-SqJnpjhA9g51M8_RO1H4ff7hYOZ122AhZ0gKwGFArOSHuomF9_EPh8_j4zfUczqw4dzKxKH29LkxygbpZWvKOu66d9lzkP0yLZQ8ghs1cN6WAfRuQX32eRwemrGxoipplYLAw4w0-dQ37NOf5AAuJfQSvgbFq4gt588s_7yQjhRGRbu68udAbWBaxge9_qEvEwthW2V9hwbUMeyj5kBmRQqEsEFXwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNZbAMaDy0AAPDV4_TL9pDP_g7Yz_ZVhVWkdgRGzWD39OS3-G3Wf41TH718YKbz77fDy8lqoFdf18CvsunWgY9gp-jotJBasqsHQnLT0og91ImxYRIsmmQimDo8v2cNlByw1U9zbRcdMqrdw_hYY3wD21zRZyvCqZy18ksIUF6fd7ASW4WYuydrKFxxHRwDvGXRCCy_fOcVvyVSG5OkO0NIMWqJAfI06Johgvjnyn7TK8elN2ar-i9pfV1cR0grtlHX-nMVs9mSYakqXrK6nf1YM67Y7-EuYVm8MVX5ofW-EBi5QU1Ar0MNbUUnSku5DPyhq-5-isSYlARb7ggdOSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTWHH5Lo4M3DIspyC23AUy0KSUxIDgGTTkrWo-IGnF_wuraJGAld1RnSmlp0yhZbFCM4W7NZHde45BUg26RfvMXtu39vM0jUTKGPagn_3Go2Lv3cmwqW50JeiuThCiR7dfrhbb4CrNOGMNQm5ivJMgMZ-QqvZopoMGfbxyL_PKcMbEL43_sY5O6emoC4ZJUvih2Cj8vc3FOzglTnmDxbQQKBO7Ocb-dR-2HD7CEDjfu7za_gi7u1UHc6XOtBE147LcndpwZmOf2ahNGfMHn3QfKxotgVYBvvK4upYzu1a_qd3M6JT76aDbp_uFeL6cELwt9rKmqHkcI1E5T7R_jvuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWuw0iTXTiCkSp0dDXEefNUtQUzLTzVT2AMuqkgbiHPyyNZCijkXHtvYWqH96dy2PeaK52PpxX1ofsCYggBiLlxV3vJESiYDFUFQVpWfRTjj-NwXPnzQWa24EENENpOmouaWYwJ7k35gLPGCVFxZVf7J9EZUKu4T8LUka1u4kZ--0mTap3l5HcLaA6ytfKBEQdA09Olw3k_jzOfv5YQFtUOORSNMLGUA4WQkoAU2Ytu8vWfCZomFRDPMNqV-xYYDmPfKtUqNKLsVuKnHhV7xXR7ric0ISjq_F5zAfIqCl3jtUcL6woMMSCnsElz2M0zSXjKGJP0uVVAxXcojgJzUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oyP7tF463ziYzJKYTLD_DP-yM2lj77xJ9bjbi1ngC30ypgoNwPmj0lr9Vz1KtArhQkfDavPe3YLwLQF9iQv1Oj7-1Ig88AV_pHHufHAa1Kf1qKyAGJ0XIzaJKKcaZ6JcPk9XsLacCYb3a5vbR0mVnW5Ed0tyzLW9VqRLktF7UsRjegKSyAocO47_oE94h6C51nVVS7fLFY9YPEkoQl5tAjHyoQuhG-p35W9GcZsjFeaqWqJIrse6zie7tCWnzkwMxawE8hHxCIk2fYM_fRr3yPNEXTu2yfF_ETWzULI6M3z6W6rh75riPJfKX-NdLW7gNYHxCPQn5ow2oxz-G9Kc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nadr3s-OlkddzZy-aNCBTnB74FBZ6tOMChK3mMa4IRGnozl-SGIsgqwEFF2SBi1nEU4xZAWkeQRh3TwEkotpWsutrQ_fV2kzcVCl6onKxvB0dV09_QX0-ygZ1LMPR7RuLWiCdSp-PXApYpzzeWz6uTQ8yj7c_dMTquqIId0sBppsbwseC6mrnRR2x3ZdONtWWO8HIJuLomKIGt51y_7iydICOI7gCLOxAUy7I1NEvS-uAfnsQMlEsj40babQUOgeE8sd_U0f0yU73aYbH2u_vawfLMLfh9RpCB4eEhYpq98ol3Fu5OJf613AtiVbc2uCLoc6OVjwovTkGUPc11KP5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eO18-gHNH0imDtATPH8Jq3gI87SAwP8x62um7cy14HW_R8MG9GIAa5WK8ESAEYqTFSt68viAuuS4Ri0YILWDQjtnCzkBujZ9aIPcc8Yk1fqAHPSy_1qgmTCv7BmPeeFE0LG6qO_yeXlwuPW74-byLJJro3UA7Wma6U5iIwu5CstdA_CMSQIqo13Ad88EeDSz-xWA93ERmOC1ooDXNi4qF2En7a_h_m2_kWlqQUmSfy_mRcr5wpM0_wQxnsl1eN1rJn-oJtJ4_M5mlhZAyNCZflv9D2RNdO3Geli4NUqzZLf-ydBCdwQsbewkGBE_WebjECVRx2S5nWiw7_uk30F6bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ackm7uCJsGVtWNzn87ArUzZBWiV_gA_m73aXukLnVhfedL87B9aqULfVxx6MezXkcZoFDgWRiQM108mQq-2wm0Y2WWTySV_ANAkcx1yHF8Zp8kwHQp0edU1ZYN3lZHzSeVUo5OVWFZOcmvWfi2Jvjvl85g_wX0prnG4gchapIapZpchnzno3I2A38FYdqC7vCQ8Mspc1kKnuQte3Bbz6Yd-fcHhoODMF4arddkZ1WyoFEc5zylNy821BGZt9MQKPabinkADI_AYdbm8-grxJEOhlwihOu-a0beK6RSI3KSsChYflS9cNF_nCttRYWTdVQknkUDCMiKphK86DHuB4kA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwn7PcLB26jt4SMjpKEX2Gw_SXLsvT8sRbFxWDc_A7BjunWk6vYBDCu2UoRXnIdoSl6LV-flR9ZP7FJQpy74rHoPuBg5PYyBbmZjYbHDKloPxDFx1933CKnRhMVDypHvPYal05EPtoxulCXTCP5dl4VGK0tqZ__X7O4RsZscWG-Zn5SkA0I-Lk1YibFNiWKYODhtJov2ZKInXIW4MVK383jc_ge0vCjPuWBWqz88Q_yn03Yi2paHQ2bnjRERcLVMBu0jAfudXo9N7GGEsTfeSpzMHc-Vst2KRico-BrKgMvlWRBYSZPZLowE_Dy2LAdY-0E3RG0nzgmukLuIWA66OA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0Ke6d3-hKhe8chFEn152P5x3np09aq5sCNGkpvhq48Zeq1UFZ5osZbsOxHJQ9W9Ey8l--kcWzKj17lDAVc1kOdJBkD5uN8LMgq62NUMQi-zp4UV7FBKN-BPvc85jD5UrbLkNBpQPkpW0Qd_yOuzQSAFQnL9uYxPtQYMRRzUkkrwyrAzHph6TtYuxrGpv7bXHuUM6MG8M9B1f0MXYDK-QYJ86keR_wrF0PDsPzigxbo6vZFQD_Je4oW-Fyp2c7WnGM_r_e5S8_jhzhPpPHrfgBeRdRGgoS2Ncfx1VxTjbwoV9xy2AoNkBQ0KF2bO8GGZ-2RbCtZ6Vnilrvuh6OJKFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L07xAdwpM3CPu5sEtpUGtCg87bmTnL3JsyG62t2gWmw7qe655jwrCav19TGv_W3hRurfNg-NQe439iuSlHPldmjBxV-SYsljay8OXJT_PyfcHLWcrz18zM5lYF_HGiS0wUw0vOu7TAAjdj_i3I4dR1VkZJo9ncNJg7TeO4tgQS5uT0RO7vRm7HAplxeF7uIa5rFvoXSKu42jz-qKWhKJommUrORu5aURRb49R1FDRb4aPtpZR-UUgIBK9LoWpFTHM2yKAdEq1je2-_bYXC45k5istsj6R4f6DFMm6lK5zgtHmwmj6jD39ULv_sFfwIlDeAGMIq3outOvvkUnp2A2tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLAF2VxOUJU8tK7Dp5-hKeyrMJYhmHrDhk_HUVHQLxfeoloFkbGYxAEiKJl2v6v7-R_w5k6Y54IFs6zPwpCc79CdEcadJvJxmPUqdyIG4UPL178LSxD2kea6Ge5uZHsiN7BG0xA1fX7HWJ0PoX-84sVjHHgsC31KwQ1vYKB8zeOxmGSF4Zbv4KNLZBOi1EFe3GmQ-kfuT2jfU1G8dWaRJ09aug1whToBgeqNy3WMmN3L_PBlxADWptYMOU5OozNubDbXzPEk0vZmcgOhCvUZzHbiieICSBwcBInQ2zJRDiLw2JvD8pMCC9hnoYqLL0ave5pW9a1q6OFSrONol8awcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pe4tOPK4nZrG6y9pfHgfyIRVAIc0-b-4r6FD6fY_APJ2Vk0p02K4KeTfNoqCfgxWyNXeIDDit8RQbo8av_wu7vaoCLuJtKx5ImSNI7eEIMLCsjrdBwrS6ETsp5IgOeGOgm2my7sWu_1Ke-S5fqsfGYULni7VWnl2acRbdEZ3DKaLUyEW1vPydiKVXvkMHvoEz5MI0_ZkDvMZObt3ExBsM6CdGGkWo8-7FiFLbsq60BmYvDAGi7nsFaVuPvvVTzq9qWL0uIC26_x1G9TOOvZXMZn_jApO_QTW5HVPsTB2EanPG6cI_2rFJiZVB__9sbu_XyUjpz4le4auQzXGMjnn5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJwp4k_UCLBqb6FiaT7w8HxdCZcZ3fqDk3mWRdOlES7wFENTspkfRgvVeoNmxuzg_-mV18HvsywkzEhSH3hhCQPjqB4pPB20rVhKbU-k-GvXmRXjdAEzCM7Zw1cklZO7X0VJ9M0FXnJrm7lFNEvFZpjsC69laz9AJBVJZ7dbMYwDWB4ebPuOOhjRV5o2IcyDNyIR3YLogqSk6y-OgIw_9oxal34GofUfRL8B-HfQhK8sqz5D1YP_Lr7mBaPt577TA0WW-sEfTwCuUsg8lHynL8X0g3nC7vIWAYaINaEgfOBq-dSZic9vTWJb1XUCWXFJCsNVJ6XfYYtTMlAsbEV6Sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eT6Qw2_DazgW7BRL3O7V6RGZkNzxlSKaoEw5wO6TLuMsAzI1JXnZOFvGe4O-Obw8F7ao4Ll2dkDpZW_piffJNNzHXGLVbpJTpK_JRvbcgKnnYxVS9XCYPUghyiagE3CIWV_FnKcm2fjy6fsgaIKZg2XkD3N0sSxUdvNcDbCG9AnLc7oqCdEYIb5fE4X-WQQRuqBjQ5CMLJpTmdB8DSCHhbe8WMOB5RcCxgKGkA8HCLZGx8LHGxAELt5Zp2AA0Af4FxDcH8S8JQ0DlmQaIZ2lIW9V8GZz-zLqUzEompGtUfaSeFmyBkM3S2JpoAefGF1lIhakC8-JLUVRpabaJgV4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfkCeomx73VQlluQMrGHMK_LyEsO29lwGhDOVQiayXpIX1vPb05wzEI_KNbAuNoDb1_6fz5tBACeh52vBmMPWYKTm0rHSbdtQc5dRA6zccJtxPOI0uPUUBZO_mCN7p9rg1N3UuJqjyioPEm2QnlIL86rNlyI04V3AuQBY-XD2-tJur4nll_3GWIfTeeIhdypjzQ31h6v1sDIaTIwUys4NaejWiv-hBjCjtKuCj2fWuOJUSXMRTaV-zW24ZxjhggMWnZ-efvl-EIahkp_-2VHDWA3BKTdwVfyI76Mwyo91I1eDjvQfo9LxVD7_WSYwlCk5jt4AXwTQky0o6IqxPtS-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJzeqEFx9T7X77E867-NIm5uiLF5-B-RtZbYvTXOySRQsB08QhF97cBLMVFCCTS2fZg6dgva7Kj9fIxHBxozTQW5jFhSBBB1u2Bv6Vk6TFkL3xkk-T_mu1F6FONw70YrgKEVtzB_NP1CxdeI6ZtmIQwwROH7sOtuAof_iZ9An8RXmSGoLeU37cqA_-CnIVC1lvuxgWUOYkH88AAsXhLGjvb3ToNYt76PfjNdl5jcYEsVUujWBvGTSHGJ_gqzP6LvR4A89KC1LvCYh7YWyDMnHHzxJEtmw7yHUgmCr-tLlzVkQPstCD2QH7H4GW3eC-OGEJGK6ZP7NyN1IY_Qy4mJYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSn5PutRQCQlxG9veor3q7pyhfvz60Ynt90Mqz4qQ8YC2KkVliSJIYbL9qiDNWkbvYWfm25FzxhFiKQHGhSr7kHuZ8XJnqHOBXMviPaCZBFPKzPczbbJKgB7NXhsFOaJfzapa7x7rkF282W0_sz_D96JpOm_miytaGg4ZyqyR5D7M2oUtjo7lQHT4fstaF7XIzYr3NTQO6YisPvAaHWofenZ9apYddXmEdJ6eQ4irEOuO9Pr73ExWkjhZW-_KkkzMd7czpcwGDv9OhfAwVrrpgqaD5dEDj61R_AjFeRhFC5U_o4TzJpFVncDlMsV2U3del5DYsXc7YFqrKkkjmXdrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uND3tfMftGGklBcxRUf8MOV9oCAQ2WIcWnGVc0lfONmB1aLkiY8kUfxyXXNNg9w9oKQCXPpQKNgvVoIzvsr8ikwUnVykZI_r5Gog7lxapQCePUeIbmIxkkcQcZTUiytYDl3VJjSr7nZLjt6kF0jX0XGk5ifgUS4gjxzc1Xok4llqqoRWQvDEKNlVPp4mC91MikokGy75zZ9fJDieFbKJVSPQLrXmLtPMqgKzwImNJWYOrz9YfjdrfnoGcp1cX3TMl9ETFk0WDN06w1_5Grl6MLDzd3rcCBOLnPpyUvnGysiOHHF4bksL_c9V4LaDOZxW-a0T4lGwF5ypYgI-SvfHow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgTjsb-D54UTGPFCyzTHEr_I-_uT3lHeHseaGmfVjApL31IUALLu-RYj7J1NYfHkpgaGUrfh7QdbX0_8IeSo9RVFLf5BPQ9SBgakBJ2x7sGWyMd4ESYVBLFLNXAimfOOqX1RreaYZ6dxLXPQatj1Uk2hrrVHZfAlHt5umQ2ve-UwrUiYTzideroDnd6QR6oJS1EpxOu2D2S_V0i5lmPa4UcIjCF14Bqmc71lt8BaSYkiZ2iI1KjYt8j85_tUXqD7OCs_uJwgd3WTnxHj2OCWShjbIHzmKBwNMriWwtVQpmD-xV9yUDjbob9rvDsRfMyQsH4jyxJywlN1SoCaxhyk1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4BKcXez02X035PLarzv4WWdJsMn-j5AIhR1EkOdPHqwTkn1hKgjLzhfq6H3PzP4DMfGTEd4O8Gv7A1x4xryw1dcOWGReHjTEW9gr5a0x3ZaObIYEQ6Vqjn4t7PksMhLtjxy2PjZlsSxkQKwk681HGeHhbN7UXqNUgVe2zh2SopC7EQBWePdxLyN7JEHFD6Ocn9hE7NAniOcoOsd0Og1mYz2R6zZFPqS_CinYdunOqYlOQGuPzShChEgHSJDALip0LG5PQ4ltwKn7qSPy8I-nhRWHfIBG4O-vKp4DBtaiPb3BgfNoMzOodr7foJY9amBrURLB74FHzG1yUBS7r6i-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0p3gsP0DM5K30BIw1cswoTXxdynYx_O7xzuYXGxv_f4xvHiW16MSPlZwFG-5ng-M9b8bnabaYwYfh4wxuW22QYuEaMXNVdLDctymOHtcQU_V4qmrpJGUcnUqADzTOVh0GHCC87DBJJq5M9a2cV-DldOpZHEsGM4RQQMcQVfjWSiH5nTgcIaRxkCerVnXMydsNtdB91FG7eMJ7uT40Zbmu_JedKF_nNRj4ZuNO46gXXoamsF81JjvXHqjXs2HwnJLn4dZX_Lv72Z095jOirh7MqdhEPKyS3aeDfUlvu5W8Aprwg7P6jCOleZMFgPWZtZQLcD5AduE69Zq-8Ey3nNfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uydV2iVaF32sinhDX228KxoJW85pPIbD35njZcZWYKl4bNjF03gc61apMZdQu1u-4AjDIGz5-5BRUpneXVDSEay4RNsKSzj_sepwAu1lbeWvWIPIqZHBHWmRuoAIyBfPQq-Yr0pzlmVHbKUJ86iXGAdZ-pi2VPC7q3IfHQiOiTR5o2n_1VIbE4mEWLrTcfmd9yYBud9G34G26IujjYaOGFKYs__26GNs9iQyAbW008hWktvnPMN9XmJf8ezIAqkXq2YHtAzNb5J0GW3ycws7--LXTMA4leTKfU3q64aChmLKBGXiZvp9xE1plzHDjFAUuN-c2Zf6p2D-1Vqln1tfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvgrYNZOdBEvyVoLsDg4POwtWgDcftlrQ_6j-3YaRfQVkeUJZYqxFGrluMyiOvxLVRO9LulkqTOCyxOhA56fJg16_gKfuV8Z5sIQcU1fh8u8WrDUdNaFC_4LapA-WKzXRZfYFqIiLT0mdLEJz61s18z5pEDVikmDd_TLOpqnhrnFzlpdAN959pUk8qpGjeJ7JspwLc1j8LJHydjIcwFaZWmIU-J5hUyeKUpklM6fPZKF37HpzkyN45mkXZLqwp-SOU190_UvKmCrHKhKf6aldADAwJUKAqYYvLx1LP3U9rdOFk06B_rM4EUBKeu7cMJzYcx_KZ2zAeevaELkRyniIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pz32uxzJk84nqx4RrAXOnKyUXYiGh7zDm9KxMS3qpZxOCIhYXCgUXcN8dDzoVshLTG4jV3-pz-UymiWS_c06yZoGJlQ4SaWEqo82tHsmryzD96-xcXgP4rYEeIgXfR7yLiIHzLPeuUrzT46cP7L2lOO8U9GY122JrWPcS-r6C3Ez5mVyLy_xraKusS7cu5iE7eoMe1kSbvKkbb5VyY9HGeZHCWPzx7r2FFZnDF_cG7f-Bp-6FbtBSdzYneh0wDatwxxuQ6fViKoARFnRpFkjAIwTfb7h34QUcJm-DlliSF-odQqkRe3TVm3kkB4E6D6YagTYNqJbJmYPq7NEbrHbNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKmIyEE0Tz8odOUsUizjsNHYwiZ05HY5flE8cegGVOgZ_tmTk4k7EKQA7ijqOuKFf9lrE8b_NB6I8dteQqWKRWpNap5S2IKEANtAHLdHiu7GR_GbR1A1eNw9jwAxsxxE4omEdwadmdT3EryujpxwlvyOQA3Po2mLKzDLrI_8in_Dc6DICz-H6d4ZFxiGHtTsaai6qYPrpqtoHD_8--tDkIPnZcNkufr-6yCMr1NiFrRjrkuf4HQvpdmu68tKunQa6ccW6nLJZjByRoyq-KBIkmjrvLkMvqFrOMLOWmxtB5Sc7rSj4lpiaTX31L5ajcY8OrOGNK4QxcKEeiBbmLvK2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKTOJZ5GBquMfivdrUzLNCu6WUp_lL7ej5Awlz-uVIIq6zrV5kh8S_0OoGrKG7qS6cF8hGBxScRbRySxoFKAFYglUR33S5Cj6Tc2pJamsvlO_1mVFmF5xw-EkOqgXxfxI9kvDCRBWf8XtvyVi5dZnZY4PFZ0C3ZzphXY73dnw5eLMuZig7-LloAybjsfjQLnfccu53mK6_nO_KFIo1DHk00YgZXrHEWC0wGYPpfF9PToZ7rWvg6oEFXGCy3ezIDSYcKKbBLoRwIvk-spZCR9QO__aalIeUPdZiAGHbR4o7P_mIfrmvo2TfK98y7ZVHzPvHfGwbPa7JIlHdwdq0nLWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ8jdKHtTvBYowkXPLiiuUnrjxLbgqm3j4hc1-t-IQAEMtA70cH1XjfQO9eWEvJjlIwqoW8sLTTViZqoSndRDA8kppMBb0pkJwd1orw2mSHYw-SMcJcDemZoeSdQtvfsWWYg_j8PXycCN3mTd3Ran2utddOtsT-QJcImH8_x86eZkSwpw63iGi5DD4J9fm2sYJa2xR2PbFTPUt3oinNdLWMiCfSFbJJb_sDJH3oudpBVtkE9aMpIwvw9QKzsFXKYgdFpxEkAvnCYjhU1eumn5H6w-KYWkF0iqbjNLXsbq3zIAwAqx-p5cTfVY7WSTgaAz3Da277Ksv1IRERLs-mHbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7O7lUseA016w_asfcJ5c3Rakpz5wquN-XV9ZlflVWceaRpr0MkmZaZ1wscMV9m-xLvKQJGcVL4mHqFr27r0tmv9b5Qm5b6_rIDmoKOmYYNu1u2BlRPmbBissdCFJ6M4RBrIwzplhVc1j3h4PXMlNOCpBXV0xlpcoJVfMiz3dp4AHwtcBwnHzwyvmMlt1T3eEjta3CHw-ju6reYpFAMl6907LVDlRfFPHyOMdzWCzpXimxAxqOvtluW0Au1vFKaf9ZKQ93ncgeqwIqakb0TKaAzaUuM7_-qAEbQhducHezSFru4wp_68Nak05waQokZjlpW--3JZSvHuiEfaVQk2PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPiIAp4HBKk2qho5H0GU2kTwtoVvSwKv96M7VdgfPg-_NEyD63goRHiOaspYa_dc8AF6XKX3bDZA_o0Kty-3N_sJaLTgWBnd4Eki3cLAwA6mpjnb-UMdpnv36GPoatsR3FY0kr-GewNa_T2lKgAefS7rLu4er4aksUDDrectNFsI9SlnrgI5BLlBbQe3OoampDs9KLGA95ml-b3D6-8Ca4Kg_9kuAu3G9-lbh9MP2Z2it4uMt8xJFitiB92_3R6HnuTCkwtogy9R0kumdlSFRKOZ3vPNlgA8iGw_l_pPGpBVtoaC2QqOkYnJLfBS2HyaYcpoc3QB974uibD_VzN2ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owr2s-R7NLzvF6crLnmMnU9OrcnpP3V1Z8BpSLPPVidiIZM198yN5XPDUJNat0RmuoGCYS6-boqMTS-znpZERDwz-w78xCrGb8D4zE9Dy9EhYSDhPqcn35pLJ_te57igpFzhLCIg5-pWFS86kt1fCnBuqOqiQmeViD9-1GbZa4lmjO0kziN64btVGwTzl_bBsJZIfE2prarzIjudp68jOoLF_MhXGwR8TAURlRQdpuVKdMKdcG6ZO_en6yz4o0hv1XznjFHHF6Dh6Y8X64NRl4aooC5dwhzhvmzlAjsJTekp_Y-ZAIUFTy9ZUqAnWvHbnB3jiuYIvd4hgIPRezYluw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDN1FY9tsVWufKE4VPgAk3eJcLg1lXA0Io_EmGTGvgZrgrGGX8ytNExQgEp-mbUaBUtUkgALEJPMxF9TTgIaekbmBetZDn-hnFMzLAT4ORL4yyzp59XKO_eauNMODSCoAtIDVglzlU6Whb74q12nZlUILukbz3CIsmubKFefI5AebNnUJ6P7KIlFjY3yP7lrrZNaBsRQhLIPhddCq5VxOp96hjBcKyjSF3VbyssILtTvGPZPpM4Isa216QzRFihMxdA5ldkFzAwA5182BPrP_GEIu28Vgk4tzGRYw6DHiGwUE0Ia7d1nxA5aqGg1SieaciN3RvCVOv8QYD-oAE9RRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URtyfoF7QLz_uKuhZMiQESI6vKgoJobtESQ6kGLzPK_S_dPgTzhI0kEOnylTU3Q8s3RvfiL3D_c63UjAiYJazOz77ZrqwudQ6zNnfL4zj-mwFEG2cNKg1vD3HvMDQ_7-sIJCYJ9f1iilIFknwXLOU4Y2tG7s2d4Tq6ehqtwq-orpwt5eP07aDFY3CRv93xN0-Tir_T2zUdWqwjOejWoAnkc5UIWf-ZAdVXNN9Vn5QTBobnzg4HaWbSEUJMiYlnqOxthB0A7ZAOWgdiEh7lOt824kNWsHMjC_8BkQzw0rRU1fi4dRqOmdl6BrpAggFABo7NqbeBcYVnwJv2fW4A4tSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNiBs6rDAAsZ0m3ty26xmVNxXeuq1spZZgO3FG3flI28BKXlYFi0WeS94FZ-BdwLYqnq2e9Llk3VkgAOi2YjyyeAVkuvQJkE_90A___tND1WKkUsxUevwZ14ZxOK-XW4IbofUD_0EyfvrC7vHbSrYcsDJ6fYi4xaMuWFhLeMpHrXLQFm3btgXMpDZh7aaHJXx7uNkKY9X1--ZeYNSPUlK3aSeSPLqjFu6grxSHMSncQ6DHsdnCJd0AObNhH3adMOdcOQnBTzmtwVLvykdqd_RPLMsbU-X7v9WQi6v3L-AsJ9mf-hNn_9CpcTezwdT3GXMrpwcp2gpXAi1rIwBoYwWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdNrSrKbnDCxabC8USnXU3H1mZbc3YHXXj8TbXWKegJgbsBV1qiYDszJ_TUqu0Fw0hWlEQgKXuj5-LiuJnhoNLjoY51E6YOv1UCcKulu8rJ0umgxpaLfQOJ_2t6WhI_LK44yvIc94SK3k2gcu8vNTYkKn7qjIv-pbQuZRZJjVOLvpkLVb_s53_uLha5GyvaSCbIkv6gD5MBwTa9DdW7mQxwQAZJBahy8wEKd-v2HhTq_aQi8zcl2S3ImkIflz78DQFcvaKG9hAzLF7gwbckEeneGnqxS7tFOaOuTFJXOYBsrIC_y66Sj5WiehE-f3elZ_AiWcTDaLUghmUBwXBcxzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDBhedHuUg0dXFyaumj1vDWDfUvCV3JvTMql7ynNLRVO6h4XVnE-9DHyswcbgMYmCiwXSE-I-N2W8y4VtcWMvuqHMOnmE_yA3rqtnLFIDSeMpn8gEXBYUewwqyVkFxBW9Htefi0UkaBa9vA3sNR4fzqWIGyAGev1aZMa0ipc_ZbufGHjczLg_PbG0TCU8Djkkm66dFKuYnRD_0E4EBbQCZtQ0gm7lIZ5CYuPnqG7BpOdx8AXX71CtdKuwZ3DqsLFZIxXE2O-_5GjHORRmYLesu6yNpGjwtDIvQ50F69jkolE-XKxsehEf4dRXpHBgbwDOuyRBtwlC-qhC1iVzTr36g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=dMZVxU93SG5rJ1s_OeNEEfnc2QAWduIseSbJfpl0yFhojA_DuuPQOjBS5J4-NwIMXsFru21WkUFrHwFI5GgE6dC85FvjsA3RgEk_LK4DIhCOgAXzwLOTa2NYbEJcxhEoyiI2xcvLf422TCyCfls5s64zJfvvCUHU8_Cl9zXYH658KXnMi1OF6_MC0Clv7sOe2PO1rgrIiikw88RfkMoQwDp2iJr26OjDaIZ86LtqYF6YHzt6OAhdsvwGQJEo9fRHDWasn98uLt--k1klR_T3worIcGIn7e0INgWgjN9v6sLqWUdFvKD9devXCQxiEqx57UssvQ_p6vFbS0CYY3IILw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=dMZVxU93SG5rJ1s_OeNEEfnc2QAWduIseSbJfpl0yFhojA_DuuPQOjBS5J4-NwIMXsFru21WkUFrHwFI5GgE6dC85FvjsA3RgEk_LK4DIhCOgAXzwLOTa2NYbEJcxhEoyiI2xcvLf422TCyCfls5s64zJfvvCUHU8_Cl9zXYH658KXnMi1OF6_MC0Clv7sOe2PO1rgrIiikw88RfkMoQwDp2iJr26OjDaIZ86LtqYF6YHzt6OAhdsvwGQJEo9fRHDWasn98uLt--k1klR_T3worIcGIn7e0INgWgjN9v6sLqWUdFvKD9devXCQxiEqx57UssvQ_p6vFbS0CYY3IILw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0JC0CNBJ29Pfs-AfagRbe5iBLOz-FjQMw-WijlMr-561zuJtb11JGc_RQrxh-ch7wlKfs53G4kUQhyAaJP8p5boumnaS6VY1sC5ys0Lu3-EQVFETQqFGWEJNcIARH4rLWROwVruIbPfo2DWTElXPpM7bEnBh7D5yUHGMfLI8yPv_Uv9YAMaTijD_iUuv917n9U5EkXNw8eqZtkOGOdbnoUKlPMlPgsmczodVpBn7AEAx7npVTEGi71W70M3FkUJae4oS3BkxIfgvKOdioUBv5GTMRzLi1zdtgiPpBuw8b_Gbd2OOopLzALuvh_j3AoURqFqf2T1-a3JMObM9mz9PQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe2lqhwObIU-nrqydOBQ9qoQWYVPINg6_w7ZipvZ6gDbW4Of1rlPCJTqeLKkxVZAt9h9Vx9JUykyz4ahqSWI6GyUrLvsSwnS6iO-VAsZ65Su7XJdy3wBEmFjM6guniSvdidlYVADlnDPCKxF09Ui_VdN5Pp8ZzOnFC0JB58jj7EZGnHLgx7yZs2iiwIRz9Mv8t_p53G64WJJ1TNeOqy5rCwjzkq51VRSRNLI-X9fEhyYNHQW4gr1pdoi5DddxhLT2dPXJ3EE1mJpnVJkOYrm5Qi8HAQUOmJCpzu401ly9mUYy9jAs_j3XMgBaS-240fyciT2_CHf9ez0CZaXxBtbDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BpnRTHN_cAlcfQ6BXfAInxMM1uqOLvU-HjzZNmwy9b8bY8xy6oCB9kDWMjzcT-rbhUCaavW2h7_5WvBlHXSyJYiXSCdd-yxTe0nCFA9ILn80pqVLLh4KJy3E9QwvtijExY7EwsHI7sFXMQ16uBnLSwfE1RgSGz58MWlt0MftDgMSM9R30gZPRmhg1pzxUD-ddryFuQI8uigmfs2KkjJX1i2ytmNXW16NWlRgcXz2SFmy17itIMeofpZvPiEwZJZpHtOaFIUDoSNCxfliy1ixiCG1ATlEFVkW4WsVcFIpwMXdtzMvdiEZrseYI1B3tcsxTR6ylEe40U3e8JcrTzqXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EfKrGGyzzKpTumjR_bpHMrDtUkeDNAJSIGCNWL4ELjl90l6s65duCsYTYbfFhW4q8YGx1nf2CXNBe8YY6BYRAvBjuEaqSXTWUS1P1vVLC76j2HtzNdSpm1XexFhEHZJjZJwvf4guu0SD_RuFc9a0GFhskITFzIyotqduPLuwT42fM1sp8rMWFZr3OuKNyudyx2FhTbCO22A6swwcFp1-5S-woMnPC1_NWppXN4uOQ3_TYqkHqRHzzg1iHNc79eUzddAuacvC9UGKVXl1mqMj-v2jR5QIcBnMBzMqqolfSab9rduirD6pxtZKaC07ldXdGZdYLs3dfsy0kpuN4MlzLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNONRt4XcNDDRZgY7O3TdIxqC5JjGN063lDyyihEPgO1NBc8OI1UEygKJHuOmRcUlfnnYWe5yqq1BXZKHnyA1DbFor2kk2whhEa3MorkmPFD90WzchxqxQFVuWDaROAkhaAnQXUMIxu4BX0oJuVBU9KwkXKDAkqyyzNybniTUF-KabFbkG7XxxSE8hEvERs48xNQfaFTgTo_J6rYkDDUW4fCz2MGV5vc_G2kw3B-GPsWgCf_30DVfTXFd8-edTh_dXORnlNTGVIg-c1iaMQqOSU96K1nOTbUBbvpD9AOnUbOw1iHHtJ0rIs40y-Pp_3BQ_HNOA-tPh1m8fpWavaTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3fcwm_46iDyhOh8By2DMDNiFGzVxD3PC1MaIxql99PQAWo_Wql7LkHnNYsB97VxllDzNnyadnfE3dHWa_w2AJNa9kTQmqKtFbk33zMX40AiH6_MN6uclkT0bGy8NhGU-Ayk4o-2JvenZAhMzR0r4XWeD07TlS-y7Rm58kuP9eJy7ucjjgpVph-aZqk7nGZBWSE_ul1aERfMzA-u1lFi691iWpJz0d-k0zNte_3897u6chTsMiEVKinYs_54sZvbkwzD6h-NZDbqunAcFOLTAmblg8kk4vSBOfzUlKggJx-tG2fcnm47DWvxwH5u0y8ey566Dmp2UpdGVXXdb4Z0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQr_TfEunmC1S3JTDkxt_Wn_eOR2J0pMrfgO5H9-X5MyJY6B90DEeZCKdoP4UBVpR1_W8Xf2oq_jGqyN6XdEjVy4PFP-ENBkBwEcP9WrrVvdT_J-uMoeUJLtxBsIEv0L5p2Is6jyR5ihzXj7nAUvCpVrs6G6wLQXpA4Uo8pCPhrsTZafeKuvtQaspywo0BMjuJb7SqMC9ftol2JloPXP6-D3KZCoD_JlJjUgbII0gCEuRDFsZwFKOupdy0XGiFTEXo3wiime_QS3Db0_7Olb_fBMk_0lFxMGG5hQoYI6Y5Lzce-rQpnWItSUiZvKDJapTUkwZHyXATCmxe-OLdcV5Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=pSnOgjJXcNQwEhCfyHupZmfZ8smGHA4Q22q6JgozR9UyX4v99i65sCDEKVCUh0gmF5f1eBBZ4vVHBjECDKw92eokgjtjVSIevyHPLeMiwXxgknx3HyhQ5EewBSsXTUEU0Tha7VTmmmrQRcLZKPcDnT6Ku6VPUNKHgTtyNQd4og7yuKplvAX1s3KdbTmIpHvnthkbJzyUIr7nAi7ZGAvvURCpysBULICH--C9PSU8T8W6CJcwfzeYXiKYr2R2Ri8eYsmEC-nb0WGwKAmZuELGSFKj7SR0ASv0kmHMHWysG5lmnf85CQrrm8SEFlFQ0BHKJs35WDqylSszfP6RH9Jk1KIiRKy_EvSZIPPO_cS56_uuar18CB8ToF9sodBaQRqrQpXMhWzSaUuD3Ch745TOnxjoWgPrzTn7QWmlMipDXSrW8Z87op-OeuGlg1obrjLQuEeGl-35PpfFtO2BvFJOb5KNDk8vQ9lwagKN2dmcoVbj5TpUfoGDXqpY1scjdilrctMuht1LxZtxJeGi_EAMZVAN44RBrBVgYI_Nh1jhIyod9QYnOgEK0DyH3dCzMZc_pJPm9lFys-ZmQ2o-R7DBxfH37UbLm1G5KEFwk7TBfX8akJD9x2YfmOI5jcI7Y-qH7AZxeJ5yTeTRbgawSfBdW9X7vvRSlQK9LMoVymlZq2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=pSnOgjJXcNQwEhCfyHupZmfZ8smGHA4Q22q6JgozR9UyX4v99i65sCDEKVCUh0gmF5f1eBBZ4vVHBjECDKw92eokgjtjVSIevyHPLeMiwXxgknx3HyhQ5EewBSsXTUEU0Tha7VTmmmrQRcLZKPcDnT6Ku6VPUNKHgTtyNQd4og7yuKplvAX1s3KdbTmIpHvnthkbJzyUIr7nAi7ZGAvvURCpysBULICH--C9PSU8T8W6CJcwfzeYXiKYr2R2Ri8eYsmEC-nb0WGwKAmZuELGSFKj7SR0ASv0kmHMHWysG5lmnf85CQrrm8SEFlFQ0BHKJs35WDqylSszfP6RH9Jk1KIiRKy_EvSZIPPO_cS56_uuar18CB8ToF9sodBaQRqrQpXMhWzSaUuD3Ch745TOnxjoWgPrzTn7QWmlMipDXSrW8Z87op-OeuGlg1obrjLQuEeGl-35PpfFtO2BvFJOb5KNDk8vQ9lwagKN2dmcoVbj5TpUfoGDXqpY1scjdilrctMuht1LxZtxJeGi_EAMZVAN44RBrBVgYI_Nh1jhIyod9QYnOgEK0DyH3dCzMZc_pJPm9lFys-ZmQ2o-R7DBxfH37UbLm1G5KEFwk7TBfX8akJD9x2YfmOI5jcI7Y-qH7AZxeJ5yTeTRbgawSfBdW9X7vvRSlQK9LMoVymlZq2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQbyKsmcfKMMZ8qLDFwDnI_3KCoecHRJqNp3yh4cU6aeSkPa1W7XQL-7m89-cFgpdG-g3y5a2CZazssz2ZRWIx_7LsVfZh8a2U98wNvx1BgdhBa1D5eqDd468Jprrc3VnZVys0rqlkqSDpQWVNCgJrisOMpR2JT_mGvbBaaMa5bVk_7uj_JeI1pMexdpeQ0OhdlOq16_7AxCl2xW80L5wS2tbMH10NGxODijyXB9KJh2Rjpx1nrndfdx1Nc6xYkI5IIkzcOooIJc8Lbn0FMNSRVWaTOA42oVbpsh4WDMx82roymWLKv6lR_6vZwR_PQPn3XxGZeEmUZ2rZ1gJ5bkDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iVOcd85xoSXQCaL77PgsVtAHHN14E7tF7H50TL9UiHVOSt0JCqoWswjMlx3d0vhgyprVB87WZ8TSqDihDR5h4gRUL-1BBtg07dX7NXQ0plNsC_yLeDVE6AcDzcmTBe_lZ4PLCs6hCSyGXZf5IpcSYXEmvUwsa5wNgra-_DC7902n3Jm2q4v5Nfb_aCfCbu5UIdbVRSalkqx7Eae-Q1cNx9mOmPKEyH2aqO4MeHIgqmN7gWXiGTA6i43QlvNw0GGzanQwQfGpwyBVoZJYuTUXTy1sohlS8Wl57DIfnT1GUQDBeF2D_rdLSVTPjHrP2xeq2xu3GZSadUM9nB1agOsZtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sU2pbrLLZyy0-Sg7uS9gnKcGB9rw52jtyjWo0BkZn7AUIXff58O9nQMT2iNlctSL3i4ViLnY7w8HdRAWkSKdrR9rPE6RQk-60cyn4hgoVg5KQVfZjm0v7gqxImMcZSm2YxixpayQ5gAK-XeJL4ypr6UkbRsHnCwJIGcg0ePDdaIRHMhdFhoMjoY_TEx2wEPOYWyA-dqsCBXwbvAvW50lKXD6V2TVsG6p9AmHgBCIvmpscJ-BmNiBr4jQbeAmIu3BpA1Z-uOIeXSt4W1kjXJsrw3pSRPj7EDTfMcxKU9sStdXt5kposvxdwKLuqpp6HhuR8mwm2xkN4Pexir0UihOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8lb3hAtkzsL3DmQ7azjlelB_bbOYxZ2xtISPiTjdiuptP4GVlzZdqm4h7ZUupssUxawW51JpJ9OzQBxaQ0tDRZOv_8nkRETIMeZiflwfDJ5gFqHPAjk4b_AF-y0rAZEnOzpmyKAuHqMT-gI_o_Gw3WV00I1rab7vNFLWerQNcq3v9MK7ZeVFRKdzbOTZRWLkJu1UpSVP1KnkhhagWm9ZfuBP0h0AiQdwo-StDCAIKXfS3WwAGHqkzKXZcMimCwuSqGxGDEMkvwnwV1dG3yaPX6eQjlKhb9RU6OVh9ztJsfll5bn_pFElsXCnUfhnXwndQHdrXtrt7_7cHU2cctpHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaaOKQ83YNox3fKkAf28N8WkBvyOKCP0ed-wJVRa0UgA1arlpXTLIk3fwaUzOsARZ54DEU2R9Z3PQt25A3GFqODM1VcmwP9ElKwR1_dkRfC-4SkmowkR81MrRl5XBQkGrgeqXhZF9DqkMeTTQOpFhoCHY_rmcBk4BTfSsVLdXLzar5dS3EIakEmnzB-P6Uzaw3O1IRDyuouXscq9IsaBrG3mX_ARiqyXDJCy0G8FH-btNkmanCdtfXw6ly2pxJGw7o37PUctBre9KsNjmn2xd-pQzfhlJ-DVt45wQGrD1rJ47uTCnhzXNxTo2t_sN8LlmmniIcKyq9o7lNl7fXT1EQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0WRs56vhay0NtSm4l_YmdrwAYjbOrUZ_5N6cHY020Adpaoi6euYkYria-CmtJoaLvnKEnVnm9Fq9LTSI34USvMrifj1TA6mTLszLbjeBNM-zGo02OV40ynZCZ6hwRfP7OUNQzkYfE9ShxRDlSwBpz03TNXRu7ugjXr40NO-soEOJgw3LumHYB3V-obGPHEf_Ai5zHTh59uR10tZCI-ZINGtO7i9-i9TzmdU6c9tccoqtkXzVV3L459PtWlG9nQ1oFWEZ3uW9GzBoitNIPgGIj-WPx39MgYhe4Mo3pfUmaQzGAOxAUQUJnQW1BndfSLtWIhIXwmRPdehJoJU-7vTQWwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0WRs56vhay0NtSm4l_YmdrwAYjbOrUZ_5N6cHY020Adpaoi6euYkYria-CmtJoaLvnKEnVnm9Fq9LTSI34USvMrifj1TA6mTLszLbjeBNM-zGo02OV40ynZCZ6hwRfP7OUNQzkYfE9ShxRDlSwBpz03TNXRu7ugjXr40NO-soEOJgw3LumHYB3V-obGPHEf_Ai5zHTh59uR10tZCI-ZINGtO7i9-i9TzmdU6c9tccoqtkXzVV3L459PtWlG9nQ1oFWEZ3uW9GzBoitNIPgGIj-WPx39MgYhe4Mo3pfUmaQzGAOxAUQUJnQW1BndfSLtWIhIXwmRPdehJoJU-7vTQWwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYBs4w-lsLzlrcHHQh2wv7cafWGqi_GvlfAguJEzf5fGTLcBcLzNbHNenxjq71Zbki6bUuilK4D4cWnYhF2EFLv2M9dmQGBqARj4Gx3-1v7kf8hESgSsmU7JMTZcJINFaky3-vC_3H7z8vW5bTIGYfFEq76zTlZVv2tjKlP2WjNvwAvZoxNFfLGmr61f_sc9RFqSVhrZvjIVKJf8fK31upm192vZXX-kCtcTLWagX2F-8gw3tqtojZfsWfkwyTOXlnKuCs9ft5lGvaownQfWeyO-gpls0o1NKL4o9hvyzvOuJOqwwQG9rx0sv--N3VgBddNSXFxSsM_A9SmcyWRzmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwtl0bJvbx_iScLbDS7F_hNfu-Dp2j_G_4M0MW4GzKcwsV-1MSqYWiqjadNiGeEQ9q4D66oh1QXwDWDoeB_UPVFNBgHD1OVDDr0jrhlp7ACrwhSt8oDylm7Hud7BqY1B9zS1PHzM5jbPPSN9rTxFaUV3haX6TmJSn51GgTYj6muNFQ-E9vHRyhS0OeYEl637zq5vyj5hYjajf07l-40uHvb-WtaI7VVVrwNbrDmEvT_Mz-zwtHt5Vkk7b5BVplbRpxTWD52x-Q7suCIER0TdqTtxQomLqybPQI3wrwtDFu83LQ7GSLH-Wnaai6Pt9-F4J2gWwR2OLh-TkEPbyhxo9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kl1NzrauajAuGIpvM0sNm0Pbd8NDRTq9qDiBBpB_HVrVGQgDEbXpUuANffqWQMzEcSYAkEdbhVhGgmkwvJvMnP4ChvcC_TshkOFzEKLkGe0VIABIBcZ43O4zpmykpQNm5OBlIAxO8K5AnaxSTkLYM4w88yRj5ltPYlUqqYv_sv7r1ZaTFGipNbKMUHSxySW2GzRHRt9Oogh1CBP8vQZ7YszYQ7fh2jERKnWnKTIloS9PZPFecZBZvStgST1tELXXjEvK_nWMcf_k0BQU8S5v2DC0Qhfq0ZqVoB4lgoPr5CjxDHrteGL5g7r2Qpb5X5rCTMvIo97QYRtzl6rwIWgHTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-ANf1TRK0AzM205G4ryIrkY49rMt6_Ew2-GVIeZtFOtqqop-esiwUxoVVtDfnBesS7qpuEwsoeASBE61TYhHX_QdYY6qJEX47Utl4mFynxb1AfzjFp8Pwt6mqN3FXtNkLPr8Zh2kFSnLCNRIus-sHQvAkkjyoWFdGxwyYsmpM00k4AFSL5m-ZcjRL28fynTTAOI8WO8hMCeCsxVLkrtsslp0eZrm_nQzZrJtovr6g5ScYg3zhkRJPlA9VXrQW5ceR0or65OPsNE0obyiMxSYZzQp8LAi1jbvI6lt9CtUxd4ki2uNvRvrG4AsUjY-bK8OemoPeT_JQsTkY4Qb-R--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDyx_W0736JbDkzMH7ExPv_4OiqNoKs76vIrYNGdBb7swY5GBHLueRimAduCBjV2FZp-LyWO5VV-HaJjCiTCUpkHn0EowQxKU-a-2yAZZuBRFtwOkIJsg_hFhac19yzgOKWLxwJpRqSHMCgVMDtPVBihue33CZugAkK8GZwgqnMO5rty3UMdnI6mNINJJ1aj0131aZ9H40t-xAPh4L4wjHNlU2QW909mtWfObKsF37lExVU2KlkGbXwboHHLMJDtF4842sskLhs4QIpwpgnOWgxMIyjlaSfxRxmVbOzmA9ImtyE4xuSSCFRxrnhYIb0kXR982DY1JYLvw85RQNm6yw.jpg" alt="photo" loading="lazy"/></div>
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
