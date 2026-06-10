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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 10:30:37</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 235 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 285 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 342 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 485 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 721 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 818 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMqvcXr1y6NaJ2PuJIkZ0Rryj2EA0ik0CwvlQINTTPIUr4H4utp9vMZbcLf1z-FaFu8udpc3V_6aLCyyn06BnyHHF8uzZmUBqDjQ2_g5PLALdXrJVzoU8-QA_ruirIhhZvAKD57GmOdmIvpPwaLr3MsRxNjka5SUpdak5ZK8Un1MOKol6Rn8-dJFca5SoooWZ9g2BI7MHAaL9SRkl1zWgi9omocxGLOgBEGp-6E7P6qMGfep9EQUiIfdYm9xiDd27EpGDjhFKjFnRSKUxy6237xkRzarbtmtp1D8lbMpHwCf8oM5EtGb9K3vJ5Xs78rxX8Gt5qMnjtbz_0p3s8Gf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 852 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 971 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syPBXAWR9fwS-FeIaiy_UAa3FoI8mgeu4ffOhAr7Qemng2egYYqzn1qYRxKeLvFGwy9uqMG9E6oLXPy0a77fhU5F0ZhdB4j2RgxiWtlGNNojKuDqi80fCoEc2CCAc6oqFh_8i2wfwy04_SAcyjgtK9KFDbE2XEg20Qb66y62vwOd751RXN3ifHPFjk2i6x2RLndJDmL56tx8kBKLQjGEaWr8aNLywfLyoAkUHb49det9iUQoqWZ40jvGzesTlqsNpKkz-dKFY1PTInbKME1oIcL2GYz9TtrZMqxKLml9BkFNbyxuOjI1P7gU-FyTWgmLM9D86je-oVeOS4qa9GvadQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 910 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 938 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGNd1ORBHTRxdqX1gSjY5goIyRbgsnqbT1piA7qqO6WsvdawHtP7tIeMu54yi4tk8MaefH7aYY3YUS6vItZufL0Sowe3amdQyu1DwJ8Bfd0aM_GRLisC21j5NyIf-Ge4wRYvlrh5QpiLqZsTQmxoXbL3zSXcG0enZUJa2tmj-lEMli98VRxGjhY1lPFLDEpS2-ck6s1U3D03M1zlFjyyz8W62-mmWX2Nj3RlbyBsuxU3RqVwWG45-ufCmihGMhvTNdb4ODXdGKBaV7spuWAfb3T1E2qJ953wRsOdV18yFetSXZXJFSwnf-_OJy5k0U1jo1ov5DPQIVkOhTX_vRTdvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-K87IU50sp2KrI7fxoAOv8ndCmhRNiBfhteLohKUoTWxC8ez5r2dxxTYiyaMo7BoU6N1U8pome9SRvss0_zdeEQtZBzx_5X7Fb4uPQufolXdm_jo26AT_IwkbhHhQEJ_zrTqMFEsIq5jm191BiffHG9hxUY83pnW_RcMHqZgScC1bBJMQszi3dPJk8Bn50170I0EQd7VEIvpntZY_RfWPUM_uTBHbI16mQpZ0itmeSewRad5uX7Zhz8nQjFDgupR-KWyh3kxP3dy0az4dFz2vK_KCSWfZi6N0Y9WUBr_ZdR4OCPsF6uzMnQ22Ww0zHMp09lJt8ivUJYl4rdqZUvGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOI1ZSC6glhMbE1O9nHL2GF_gP0Ny7dDNhZ4taqFaa12Ix-vYdfg4lLvURwCecC20lkOYpfzC2_H8EXC3W9NCMv8gCiaqdcpyCdg_unoJTVlBWFJaRJQjsCfL_B5j2DXolhjpOANIqi9qhpaLZgAHsxwTuDifqj14ToftwLtxFC2WOvVJRrVzwi74zt5R9wOFMD4rZ7MCsKrVAauFoCOL-2Liu925JNvZRUj1a_LD1vdsc8f1mgD2rJegfLjwF7QLoax1usdIhEKV9491NZZHfPEpfrGZ1oUXqAzfBiFsECvjxRHvCVtB-4epMC8h_pN37de5vfVJ-7367Dr38Zt_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqqe6WSzlAv8G8vi01gK1SmxOSl6uXF09BZYAx_XXsxmKWSz2YEzkM9kKr70-SUrL00l_1Tv_H-lr5H--sZksOn24ryZJ0ZGLspGhf6QHYud6ghEcYnASO8GrKpIph8fDLrDyKoM6NloHZXI9RcQKWkbBjkVvkc7-oQLd8bMMgZVKekHZj9limgLCU31Wnz9KF7jka_CMyk0YuwYpHuL_pQNrB2t39AqKK2gaOxA5MnBkjq6GbU9YgS4H0TIjeylM8m72ApoOTr1AyR1rj2TIyiwuVUXFdhZOK5LZhlpOzN3DEi6mwF8zQ3WjABAwpErTdMA8zXszM-0-I9-pLYocQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDB23Gy6tPu3_rmi1G8dawwByTkfA3Eiz6CbbC-ZWwAwSXqqd4lKPOWiA2XabqjqXRKGB4Salx-VuywPtvBjmRA19LroR_y0EtoD7YofcKAg8dnuZEWQav456mPr1Q3xr6gaL0p3Dbq7KctRZIb8NwWlU3U1qFRB35l9EXYuqOBQEs799omTCiUcWP7N2NBq-DU5rnZBmNYRycd5h1wrrmLaB9JqI-gGs8H-FvAuF_RBFkBxWvrvL0vcSEr6PPbwavaHoqxSc91pwCzbImrYIsIY9nEtrfh5LKypELW3b-I-9N8zHdKh6yWfttsmqXaQRINbLyPM1L0Iksoj_GNZag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQCLbLnJMl6BkekpGTC8bgT-5DOegYfRPR5uzyuFiDX2e9o9dM-eoYzDMqwFRY4v4wLPCW9kxsEeg6k-H5tCZErknbt4wQphqiDos4sALA2kZAx5eINLU9ewEgZKZTh2FdAtOu3vSby_11Eau7DXssb1R8gv6Sczc2A3nazT0I401mlaNLlrIJbXOiO3KMdM7PVbhCsUiDE4OWSgCsJ8JdE_feuNi3ZfyLOZWpBcAAf8x1TsEZWwJdhvAPe7ztCbZhPI3AZVmMB0lNa7j5jaeNvDQjcTYI8Jrg1mJOpXrR2jpONVXkqTZvsPMn7CyiE86SX6CmaZU8eQ60baWpUDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ix4FLF1xiQSazyzLf3VIKQLHMvN5Hdn5byaQ0e-0WK5bitHKKlArNJM2iR5hJN2t_CScEJwhOy4JqXpTwOPyD6mXGnMk71X2iSv1AhetObW9HEdcoFN9lkUnl50RELqmHUcTgr9uvp1mpqj4RfDa0PpsXQjuqtIHxznA5haozaxFdQALjFp-ldaFvYvtgt3Fv72jUO-Rv1_jwbvzDnJVVe7ngv8H1abKcp8qWC64wJ-t1Ap2ssf7H_DQWHQajQ6ri048FnRp8ZNqdZkEERwIf9FKj-bSPsucleW63Erp9uHlAfWxOs6YIbfg2HySwkNerSpWfymlRBvpTodWTUaRsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrAN2lrJUSLQPa7Wtttr87NHBEKiezQerm_Zf47t__wL6xp5DENvCS07ZSlS5IeqA4xCGTFs77UFim0YLJSbYEDLF22fTmX998OCQq1mVnK4mPL_NjLDLCeQIPwxq7yEVn6mqSCT8ndTkquNJP3D1qF6B6glNYdTNYLC9qIQGMvt_A1kpoPcNo5TvmLBVt-h-qU2NgiP3A735PqZw4Td_s_MBqhuObvNgBEgx6JpO4osomW4ISZM3x1TziOUb3GW76e4A2LJpi5fwt5Ef9oiqIsZUpRT9IhTNGiWcfPmEY3do193u0SwKn02UbJsm_GhpipkkE4G1lYPn59ZUoz9GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uh7c2gOl7IOwdfatrO4-ecUIth01LopNw7roeUqA87C2gvrqvuvivvn7GTd0wLZNdZxk0cK99wSaFykr1cOSgbDRJRbmzeBgDVeOeLscYtejTJEZ9R56eU1tLsVhiQJOgX1rk85I_Iy7QpZmp1iMKNjZVnbYch-XRt2P7XEdCz3ZuuNx7zasURrMMfJca5RmrH_BoBNQNJ16SIlIbcU6tA_mNYgdtB5VAMMU-ikX8TUWs1hhCvGWrLzwdXrgi0_dbRjnDzYGPjp0ETaT-_MbvesHCPq4DYEIkz1AvY5xyWg64L6PvYQLMlwsciBJVgtJtu1QUUlDmWQX2jBqKT7-TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhYAIIT8Y4nWh1pgdidzqEX4OUWOrIWnf6NnBmjV4Ekz9K-It6B6Zm_-PRpeFaH5NIOU_b_QNRk8oNAFSiCuohvxpC7eMMTlYWjdbnxV1uupB6cKu1q0LTSmceoIz6V5FBMketmCgkFMtsVPALQV3T7Lt1kFVVHscA7hdi2IOKGs8FS9lYxiWWbOBeOG2bZUtbpmh4yvRzerYI3EkKi1wdkv-NYADKj3TPkdg9DCQRe849eHStGxyq2bFINiY6KHVhMAweN0g4xW98trpdHKjldYF5YfDu2KlLi_wxwONFl4onBCg0bvHXDhpTf0O0_FukVy8jTZSVRokqY5l6IG5w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=FPti7cFJ9rNdrAvbxpxycStB1XeUAT3j7IdUgoKJiow5fa8yr90R0obB_JKikPspEP3tk9xDdGor0k8B567OD6KFuYyQE2quUN6-XNqbn_W5mHTeoWVZiLCSwuTOvn0Xfn1PognMe3bLVAXPY_q0djeIu6ZjxcD5lvH8XAmwIZaaR6KNnSndOiT6Nv-GMgJNBRFiLxBWI1P8_ORJYuptXMtMf6ZwJGF4P7P_b19Rfs9hk2rnho6FzbVMFm5LV582fdeqNqflFDZE4b7Wp6SMlrEOs-rFVvsniRIWyiZWXnUuG-9sYBERMb3Lui84p7RHhu1CGYtl75e_4UsVE6tCzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=FPti7cFJ9rNdrAvbxpxycStB1XeUAT3j7IdUgoKJiow5fa8yr90R0obB_JKikPspEP3tk9xDdGor0k8B567OD6KFuYyQE2quUN6-XNqbn_W5mHTeoWVZiLCSwuTOvn0Xfn1PognMe3bLVAXPY_q0djeIu6ZjxcD5lvH8XAmwIZaaR6KNnSndOiT6Nv-GMgJNBRFiLxBWI1P8_ORJYuptXMtMf6ZwJGF4P7P_b19Rfs9hk2rnho6FzbVMFm5LV582fdeqNqflFDZE4b7Wp6SMlrEOs-rFVvsniRIWyiZWXnUuG-9sYBERMb3Lui84p7RHhu1CGYtl75e_4UsVE6tCzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNKLo4YcYf8y7qCaUu24hTI-1wkeNNtEG62PV92UcTZgNnulndEi11G2AG9JW0DtpqGllud8xzJrWw-AbgcJC8udeISkvVgN-eJyorqtQcw94H0JuJN9rQw6YlDOviVzwZfIzqotMiHd9A18cieKi6rg-g2BFcRjF8CqJ4mIvWy6BIzsOwO7uppv4XZzlDs6FMImgl6PxOuGRbdwKzdlkPcL_0x4pLbTpCCZiPGyIxPBmJNMXvwiROEMaoGdSiUr3KiH3rKFPQeIOq_oZdy7GsFuboxzu9YnDBQYV0SyuuSUXxufsOALT-3PxqRZtDWKpYoWTfa9VIpjyJSGrAYHeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tidykxv6xMKzNCLPwBBCcExgNm5nuPqTjKrtPai7NAC7Ke7BM9I9gkTgG9kdcbeSi-1YwwUJ9FyTlh9_OyYuPiOG2tRvklVFH-cZLiEY_Lr-6r_fZvLzU1qJK4HWiZtcH0YYtgS9P1aKi2b6JHyzJXm747vGI0w-gtca_gix9NT3TDBhpPSqT_3LQtKsiJ-msyZmgmh7yzCeJIVpGa_AD8EbcsgxZ-zLzhwKqSZQQv6Sc8KyLdfbDvIR6rxklPqo_ps_4pjat5_7SLFsvX757m_oTdLfK1rVMBTra0wvkrWgXrCG5VESHQNpRYmV1Yd6tNLzZPQ9uHPZT1L-0RicRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVpz6OnErAG8hiTM5B4jGKa6yRr4MKk5yAHLKYlfd2dfHocPzZX_kEucGwNPXJzAy0SifPvGXR9RHmwwNz1uqgQ3VHeqCz88RUFQwQ31uT6_YW6SevdvO_oI5q73c1jnu412fqoYHNr_j-ErR0Q_SYo1Rd8_9H95nQwaMQkCCOfiTHw1EHQupnPUJzbXhv-b9d8E1SJLfs8GEAfdWdsPuam54EgNj9YZj0G54PQ_MCNQSG9MAiXR1W0Rov8Jvuifpaaumkw-uqxt3qGk_HRBzGfA0-t-QqeNrS6x2N568QO3TLWzkA12EL_QMSIh6kw9jGkQhJ0yZ9ZBM0cLpWmdaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q87VWcViZhKnF2AoeDmzkc87jnKkrPjgSI_U0yoD-IwvfrBh0RQvI2QUjceauqXViVCLcndYxyBHiy8Ai4GuDbzoTnRUMrEtXg5Qtc90gHbMgccB6Vy5pHemBim0LfdEfZlu3d5Cq-bEmP639NvJ_q_iYWWZtGyBC2VrkeRW2-3eP5JYfn6lpUxkjG_6MFW6ZzjEbHOL4kkuF1exyt5e_Y-OClBCWqoDgCFmPWRu4z4f4_1F8tj6RfwQtwJ73HI1MMo0fl3nRJO_7JYe8ACGN3NHxdKLEeVk0A8T8yR2CaDq8i1H3IfbYzRWIDCw9Sbq4DxuTuY_wWfwylkqDzVmOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5l-q-jDMpJAMPrXF9tQr_eihIhaGu-G0_dIerDXS45xe_Tbc4_vay3wnr-oEuO0xn2DUyOHkssVL0Rcg5qHXPWrcEtYY3K5LD_SnPCe42qgHzAlI2-zkSHXN9m07KX-iNBvN7ppGWGz3azXaoPhJBfanaNX4Wf6k6_HxO4YLjDFpvq4L8WONyr26_bH6cmTUEaB-PiCK-8RiZAeltdVS3RjA-Y6nbherwCIvu8sKUeqi6hngUOW7YQFsX7bkOok_YZT6tIU8LFUeme5wURXUjx-wjzud6aq35JhVZGsQpkXALeN56lDgJdUzrlG1mX2BZxzQFBVtQa2DHaqQW1H6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsGe2NwZl3e-cLyMM2dRr3yiwp9gO95010QshHLwjMs9SHWXxAUFteXRSo3kLGZbpk4HkcNA1GuAuG8-VCc2bVUQmzm2w5iS1pOgGsWLyG9t2Ax9vtDXoOvyEDyEel8657wuVc3tYbznTJiLWNtnjEtzN6sNLehhWwU1XSCmIJfTEaaYNseeOEIXs4fmwA1tnIExQ5vVGNZTu7cBv6qT7PskqA1OyRZTf835U48UMbGrlY8yL5IXtDAU0O-ZstY1146Sj8dr8NKJiA9atyYQNZe7wN1nOx61wG_WrxeuIjKj8vUr7YJYLOs8dKMv00C5oYbDas-zbCmH4YWGYKl8RA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KODa6pdTLHmKT3Y1r_fZWKe197T__K9ON5zuzW6-KZgq6fKRpKMSmwBC00IFw9HUC_fXV0EUd4VE9KGouEVmUWMRDYj5rfL__P6df64dkGKVcvHE16A-bn1TphzRZbnWuTWLxZzyM_pr_wU_O0K96ps-Fp-7mLNOmTiTD2N8nz0UpxwV4hAdIJY7-2EP6UZUAOIpEXeIMBXeEIgyjN2EEmCgtx3VRYRkjmaJBkyKzTNvC8SBQN-Ni4kVPkAZZXd15R6NVW9qVLCLDx6036R-VeCM4UG-XrHdSgFQN70UaeqbVHKOHFWSHrfFh9KQ1DUBDCCugWidn9TWHYQeA9AkeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G52d_QaUJXQg60i1EpIG6nN16XgBhklw0r94hLjOvyEO3aK1W-T_pyQXc39ABstpIC6MlTc-P4HJkC5Q12R8moPXPxQuCXtsJYR0qCuHGi8rrg4QfOMWRbwq0wAzaXh9qB9vOpZrDBY9I8al0CjqKWM0KGKLDwoe-Yc1OwgXrcza5sIm-4pm1Ylmu-6s-Iekp3aLN0NILxSvxlEveTotN1pdyzDCwwA25hJKV6ORVBz9n6KnqnHDhxI9Lgv6TIJPtMuUYtr9Bz_4WKJuv1KAkiizKkUFlTAUw-FODQSFwi58U5g2ZXy4znYPkQi1L0fu7_8IfA8hpj3y4CoeUCuy8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vv086qHP-8i2n09BAi3CXEH39GabM5uUBJofMJHnj6HBDpTzEkhMOXbhIiY4uNdnswExMAD7wvdUKdjah4IvQ2_imAKxrqf0a7xXWMtHmqJYc-MTvpmsUbnS6UxAJqiYKs7zwVAEDfZEMePADS6mYcAcINPgqizIYcb0Qrl0wXQZ0QII6d0KLW2P7ovWKWD_AvHErBbb3Sq2QyypUpm4giZA9Q241LCM-m1l_diE_Fhs8apMQhFdSj603RMh8xyLcmmF-oDbJtWv8imWwQvB7HXRy95hXfrfJkBviezNi3k07X4wy916nEgTnVQWUAI2a8HacL2tsnXm1BFxD9TUNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYjaoys3dkFf0uaa5wZszSZMIu0_UMTme4vT10B7NpmBjsfiRaTXKtMW8NujcM3hC3Gc8E0BNth3LQfNnbniG3DuHBVIKakdSU0Fi9nVkmiQlMwC6FZVbynEFEFt5cWSafBsGz-7YWH_9e3v9PX0GfITGFAc76dUf-nu5KoYdOHv6eLIoa3vHZMY7hg2AV78ptTBYcz7PRnEyOkd16VRd6f5WseCp_mpK6YoXP2x1MD8FKcv65HHUIVZDHquQSfHmUfTom9FE8eXfSv6_1kwLRLKqOdIgIM0uqThcn5vlsp8FHiL-y6X8VYKyxyzUHdwRxKYJZnD375pyFW9DJlrjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZsBNwPgFp3R9IL6YAx5-ofWb0ElnG7tKMuf6SJyEiXGznNlAS8J2JuVJCJ6QZMD4xd46fUmv4U8ya_g4NIxJfnN4HQYSmGZoQnKPIEj5JyyePVSpOhM93X3JUQ0HW4gnZiBsUFL6GeA5vqO9ccwbJQbMxL3qNA0Eui8NUpIKdOu39EEHsLqEY2cPC61Je5TWqckDhb7cjMlG68pkAb3AaqyV_KrYti5Zd6vKX6U5Bt1qLy8BApeDjaPM2l6Itr4akjauLePLb5gmj3gI_x8NjDXC44wy0jONqdm1Oe9azG7w8SdETYk09nK_kXMtry8AAZsgXH0HoAbE-bKOFdDZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdtJ3-jmPjB98z6_UuFg_fN4Mxuis2WvDsnXtzaiuUIQThjRDNiN-8fbg4TRuBGnmzBQmvMTU5q2IjzGXFqSLayTkaPPLUY9jixFtHJuIvn4yq4ADxmlN7qrxbjUTg_47YGye4a1G8dPYzLvrEmIMGGsgG_rHX8iXcgAVJ_HtcPoEBWnuthkOAQPyHSCUtV2UY4lrWBAbs-bTaXAECtCeVgmLL5zePI-Q3XNyLc2QmQFqXBuuEdrPSjMgHX-Xs2w_gEefbqjRCWBEofAU8xxZQkWIkCJM60aoUWaE-x67EytCV44jlzWWqgjkIH8sC2qNzrQGDY2Xp2P33r5-U07TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ix90NX_ulla5Ma7EjQ08XwozhFyPi22OYQrbD7CI77BLq43_7MwJ9H7-gvpWWPzHuw_nATu3VcSFZttBFWAVW6HbI-rt0luEpU_vxYePf73GXjT7rrZHbq1v2wokzqTmax4H3-WuTWCPk5oq-cmp0JRYx7vHOhQUJYcTMwEdWMAYQdftV_LtiTAMMC8RdecoPgv6QxfdVmjMSJ4SYWkRzfd0Wi3HMc3i4oklMFJCULfiUfl0hqhZmMgEQKyUgu6O5wUG42Hd52qleMWFtwoukRfZW9u4EvC1q0Duebtdmh9xq1c-jfzz4JlW2EKLHtU2EREx0mVWNxswCYOZbfOOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cV00nXTuwWehfYgOkIopQexXrwisuKvQS-8soS8OjiG3AzOUv9J-y_o_U7nlN_P4YDKCRQhVheHdzWiviKK0-ySa6LvF_BPxKRaNMBB7Weu5sPSFI33TDXNIyoU2Xi1PTH1665k9hRuhLtj9Oz5Gdzrb-YXTvxX8KG7TPmAmgwMp41ByEowS-5rHukb8c677wHrCY52JxRu_KzliVHMzRzzTD9BjeMlCErS1x_DjC8B38fPUAKRQJKvfTW3XK5u743gichq7lkJVDpAzkglrM7gSpNNV84Gd0xUyXgqj_dREF4SJHzGvAIxTcu_GELOr_zI82OBBW_bUvZwhy0THtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZhM9I88oVwM0mS3RXWkbqIV2D60OtqzU3z7T0_D0_b4cUjvWaK7al94cPUmlp0qPf_mZvu7Oc2245Ip1QpoHcVzlF3STY6-6ums-VNjaW7oGQJKkMLmzZg3u6bMkYX__S0PyWqHAtTdMzQqq6Fw2dIOtr7c3ep7TRt5qN1oXZGQ3qqDxnqlGSd1qRuRwdt4raURhryY7pcdLH4MLOiYCSWzq3RjwekqgX_utNXO78Z52okhmHw0PlaEBNy4-PNg8r0tLBFRM8cYXTU7ex8z2ChDwlPaTI65-olSH4QBpeQ3M48fOoWoLjbr5kRiUAje2WsWD3UEXSytB0t-XaQDqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4qhn5lOLen2eavYl6_iA_n0pnSmkHiLraUeteXxHedLXEC8hplQ_TndNSzMOTxuXLJSA0wy2MH2fzpEFPVMI8L7QQAw9xfBQXs8A3tOxhqFhEfS58-lHyZV-sNcKJvnCAmW-EBZSImQTHT-Xauujq1tbq3exUut_X_ohy5RlsdBA0KmKmPyv7cqoqORC1vsco2H-caSLsZ9_xlYnRk32Qo6LZgeLssAQh8PGctuH-xy0C6NT0UueVmL-7xtrLI0C7s1utYR2FYdTiwkfdqf_IFO07QyJnOoCxPMTODJvjZlyutP781siB0d9txm0T-mk_qm9em6t95Y6kvQVuMUBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRU9R-XZuADjH4EybVguL_60-1zWY6-bY2Mezd3lEzWiji-ZbNZxblLM3gY8CF9pW6v9py11E7YbIEQWZid_08FYXEZb8KA_wVYP_XLdZs1O3z6Hoe-ykr_awsLsWbDAS3QKBNBDSGDa_y9sIKsoZnt1wN2EO-EEH3ulnEQ8d2iTDG4N0TNLm4RzfXlTA6_UQNPzge58HZ5ns24YrLdPV4X7yOp3UP0iDKqFS6IMhiZzX6fewEeAcowzPc_MtV0P82_HaLnZZ5PCZMEpsfU1hIfQ3bgSVyH8nKzf0J8esz-eLgzk27ZMBYMISEzcC7fSw2Up3p37aMEVujcDqw68Og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pklie2VNfUWduXRHy0Ku1apohmg276M_piaE75o2ZOiCdQvtiXS1SSR4AazzdNHFhW2eqvLjwGngV1PJSVO_DCTOthOW6B5TFb31dO69cNUtCf0M5RL7FTbZ_tawL_yZR2P-E3YAt-nPzjOngmdG1mnHHChiZ5r9EeuR_CUomZls5MgkuKv2eegMyCqOE504UL10pPXznoQbmxKlht90D0lavrghbkXB8vCYUzAIpoVrjo2uv_LH2RolXw3zTj25aUOsKFRpQaXm3cGvVoKRsmCxSAhr2gEGWMRuD7zCYM4u6dbhTW464L4QUB09oXlV1CYX24LP8w8gtlxJE40A0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx6KIYOzCJSIkyavV3XAkadKsAsRg_3zzbZW4vrVTtK0gedIlcDk5klPaOMB9TLy0vjbUAsCFJby07VWatI0iGURYGBKKRxaqae9F3MtOjEyUGk2XmIdThF2arAhqK9GCt_bheHI1RaDbYeR19bKQcC3UYViau9qBVA6CKVFqILRgabvuUn4BeKkzscrBbYuvg0kPXp4t4EeZO1NWs_C8aix0boFejdgZKsy7JaOH_BjzrsSGFP-xo0_94NMPvWZYb8zFWf8_-Gks5WYQPfT4I63PjUtxRl-j2RpFwJ1jtkQqdKI7BpGzop2m9Mwpw-BWwCss1bI0PpKSjRAEsW7AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9R0815CeXESxDcEzAMIrJq3O-FyvVeSACTJOqvHruIEBKe8B3lh8sJkkutJPaL3FZLwB6ICkoQRrUMiYeKhspm3dRcjOyIRaDdTAowL86Z7N25qIzpV9nRwd0ftxrDVq-vQ5kxdMO04TD5KRk5D0cmTFsoF7RPR6qWjo6MU0DsPwoBUDDrXkM9iUa2i8XMl_DqjLOeBcItwQ3q5T60NHFsWplnuauw6ogBPyS2SSmdUoZe2meHsO8BF-czxluM_h208WdvRUWrKOC_K375NBUIikiDTWVY65wWm-BOf8AzQZhQ6oY2nDmJffl-rGeriJy3K1TkIKvSmOVRzS-4NjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOti_fq3oFkHvZ3s8IuarAsAmarG7HnJDr9Gh5iZnudcEyhPbdOUnqFFuFZ8lI16CHyMRBccVBQQr6hDEII_QCOK6pOMHjfO_AXDiPSLJ2U_FBTXVUEW47FDc7Cir4MBtn3V_qve0y51yYxfhvX5zLE4kHNzp8xwE_KQ8iU-v7JLkE2vwqYLNGal_FGVW5ZW9vt_narIyxeU3mPo5d2VcX4rFh4FulW6ESMvPxJCPoXu169DE3QqcC6ICdhE9B_jnTfkk4KdqFc5bZWvRo7YJwMcV5oZ3VREEEkFkwKNdkRYaaoa8haLvWDQ-ifuJ9rGERvI8zLNDU18qLB65gJsfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_VWDDWWIT72H4a_ytNBik7V5lplrX9bITIF5Spsn1o1OqPkK9CV73pClO79tAvgkWe7edoAN9dQX_MR16r5G4FOBfakURgRTeIqVeyuQ-v1U60toCaJP-0y33ksMS8pBvI8kPCdezv6vfIPP1TmaynMizSkYgv0pntF1NYAG46lcXK1ijZS6QtIvUhZBFroxyCcabwr9qD7HfR5cL_9FYajOJxvwLKhOzwpC-IaEKUEScunLtahojQ1qb_4PZ1zvR_1DkVTdmSDvMOpv-W8OwPvSNCsQV3AFx8JIrHE0mPf8v2Xp9qOZg1IPqbaPKuXV6rAl9FQGFNCDQSAoUrH1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NubFS7liziegj0lqRw_k1Sid1iSMoW5u6cLkhNry9Kn40R1sasoakENgK6YZpM4I3rD2GzVZT77iLvzgyXcUMJVm0pdkb_nHWBBbcwWBvpScN4InaO0r2pR2_hZSXgUAvU87JsRnpFKOb76ZhpnUiasWXGlh2OrptSgGYa7zl_fj4e-eIfbW88V_VLYXrl1Mm7sD5_Cl6F9SE4LbWoP4Ubrc4mn63UVW3q0fi3YpHC38yWhHCCordWAng39y0-WebeFiBqvNumbGrrAwMnA7OZgvWOovaNBCCHKDVDcQQeXa_oDNkRMApao4E_umFkzoqgbwPMw9-quzjKNICFD3Qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFNpieUdCrKK_vkw2C1jJTaLX4zS0YAM4R9jv_wbSHzXYhGv-DitJlDGqooj8c9AcFqnB6ysR2YlkySPwthbeHZsHPNrr1RKJS9gVZGqeO-l2KVW1ArARoY_CoyoksIEd6V9EggqrQ49ggqY0Y4er7LL67j4gibXtr483Eu7TXy8D_NVVpfxUeunvH5EbUZ6vhFN3FGFkGkJS54n5wuCLQgKUWjzSQCs4Ir0V-zzvxh5JjJIYlnX-QWdlDn8JgqcLBQ_lpUbkFnG61S58bBQZT82LDn_XKBij2QFAoc9yIdPrG4REk825PeG0RFimwjAETZv4d5UTC-A9F8Nb2th2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EHFD_2ZdVjWuHcHsbl9VtB8CXTdI6W4nz2g50GNUzexLHO_7iuy7wlv09m-aNAWpN700zwHoEx07yxAbcEaXHe1dJgv9ebVcUM3CJuxum6550E3HBAAewdyjI-0EJCDxpxhwGIbsWlIpXGHV5pSG3rNuZ5JKGV40lF8PIRl2e6W2bQJrt6PH8eeFSkFjwwuWC2QANe3VVC09DxEOKo7Cn0d1Ch1FJySPpbAitBmXVd1ScY3h_MfY3m05HTJVhTlVcKh-w1IewBfcP9-3B6BlUjiGV2isPDQFhuZY0IDieHxVFpWIQFI9hVvZ66DzIgls9ZXDn1iQH0SDc1r0aWkU-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvBmTmmYelCx_py5Doh6bfIk8SacEefjFt4R1H6bJpLc-FpoadjWQD8RqALQ-kQzSrFkCF43-dSVeNVmw8l40uJwfmLvJOpTYI59El4pc4e9BhD5aSz770dix0dC662kuMnbxLt2zr42WE22TTEnfoS5JvPfGUPkNg6qXsePvgr-GK_X8Rjt2HpMVk_vdaof71Jgu_KTh2PXe00xVrfm6TqQJHucxZvBcJxDPE-dI74dMXKGP_lf593OpuW7Gya-vdAo1acdMUbuT2ByVT-nRC46GXjaThTmqTTAsHAjNDqIWIWDt_RfhrWNj0RWWFxarIoMKC1dui6z6eLhaBK5uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8KR1z_UsCpE2z5AHiANSozJujaugT3bgImIhR2Vk1UD1y_hKUWd479FnPUFMrZIJIYfRld78XLvZBwL3kqWqpibYKUsFQs20RqOKWVG8nA2jReyF-lP9yBSPgu9qMZgFTOGWG8IRpWTySyrPscGpUbkUq7JMxOFFNYjkgZ6wH0RiIpbfQTbTrDJfHF3rce8txw5YILU8rG0_oiNX1CiIsgFF6Nk86NuZr1GnMB3Oyu3IgrygwhgcFEqyOlFEsBYukG-9Ycrzqjbi-EvDDNOCZa-H2SHmNAcIVyOGB55uU0vaZRibIndULxedRDXD_uKW1TYncK7NOJEuEu5AXA-MA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlBYMsr1Wc7uooYvFLgh1uD4n-rlaoyn2daSxy-KOHHh4mCKoRDHDt0_PZV8Uz0Qf2Kaqoi9Tj2oWlM2L81KBvzDg8SrGiqZTRzobhd2LJPcYsNFC_qV2XCv-MTAjA0nLJqceNKAqksf6x2B7GCBRBILTEf1fsPeMZ42sfVLyGbiKSBnWysv-6Bvcl1T75gRzy-XnrmyzqwW9cQGbXYsd1h_jugFC5zYzjWjCM_Fnw83sPFp5qkDwDKqtHVto4KTk2UeWxVwEHU2jGUMo15fnlk4FCfbM5fS1Wza0wxp0Rkq3dK038jzlJmysv6Og7XnG1OAYMGVPf--K8aS56rTHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrByXsJWC-zyhk_R1BJNdbRPeP9ynOndjHBuXk7leE6K8gJF0bqEfVphwRTdosXP6D0yxyWfOc1lMgw91Pkj8FKi6N72v40WGxTqY_Iqv5gbQCDiVQ_DeNZOrsWBqqgl0Nt-6riMrDYCV7p1zgNS34DP_M1ue2BiMia2Oo5SXkXQfe8-mZimeWln_5_zD0zCIOaEWWHYqx-r9qOAHihKpGKJM1gKXYidL12wiTnSxEI9-RsZBqV62xFWdwjrvHS4Jaam5q9rcd7m8YrOOU8US6ro_FlcOonMiGGiT7Z0WeGu9N-nPx3GoRvxNfrFgK0V3NxzYPoMtmf1AfC6v-VFmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMiVoq5VR-SWPm3NHGZpDZWz1vtGQuzqOauuJ4DNk4HqvyPT0LmB3Bl2TeYkuTGlPfBHtynGITZjF7F_gABzGZNaCL85p83sJkl2hlxapROMNJP_kZkGVyMKKRR2mYVJsxPGY-xGTbMkj-DhZGEpPTiu5tilRsdRQNCR6-8k-eT8WYgWEyxg9HBHdjcFFO7KOvmgGALjW9TTkW7j-6bUoAgyd3iqn8oPVjS6ZxGBEJt4gW97y0FZ27dN3LQIXyqPKvkCCtHKA5YFQbee0l7vhr9u0TRjLCRvYJEtiouKy7ErN0IDI4iZTURiE5Tm6kJwNqYikAsJgHjFptn1EvVrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/seBA2VtWnXBvy-MkSUUWa42wsa6YZ30RgzS1_tjn2BKFwpMaFCzPZP4ZauKIuDhan5TiiOadnEaD4x4K5EjYVrK4F2q9Idczo7Y3Jp6qh5a1leOerHEgXtCqbtRYUAWiX3-W39ebohSkqrfFPZOcwvajHoVuSlK32M4RnQEb_sPfYl5N5p9yVjemVo4QdiA4fFJ0OVCGI0uS2Ydm-8-UXfoOHJL3ljnTr55nZx0asgXxPbtcT7U1osRr5C6o3EiN-Bw7J6MnvEycbokmffu6nNc9FG-kMiIUbtAaVvoEGQfAHsvgGGt99tZZbOvvciYHFk6bZU-AqL5yA-gnHl1b-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KROeenbbhLQYIjXXZGCT7kT9b_s2jPB6Mxi9H1QapRiFS7u-19M7RqCpN2Hgvw1iYS03Emzr9wOR2A-VYzUkT2kFwjoI7uNnbqvTMOpXBvDKx_P3Gn2a5J99F9q1Rv7A_lNkb4i7mIsz_qTxP4SmwFYOVetDdI_R4oNhXT4r1QDVgQ2aGFuBDHdaEfOqDwA5dpTlVtYH6teLIKHYUA8WD714GK1MjNT1U5MtUE8AQcIWE9hNXTraU-MsjcvyuOARfzRVMfUSlAawyrPwUMukVTeZd4Z8Arn6FymHN8zYD1J4KCkR0gegaXYCe2R7ZuaTz0ozeX7HOS5nyyhwII09tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jl3TW-MIOl3XMwupjmo_-lRiSKQyRX1PXHhKpI6gkDaYxykwyAfcrtWGY-eELRYPUF7qYP7-yrwuvgEhzK89UCsgJPejTwiy5yK3LjvhlWz5OJjR28XT0GEaL83pSfZ9krc3OsRCd6HfsyAv5mdcTofkF1uyFTkyHiov00xPVR_PDairO5QcD3yG2XK2hoAzsz9l39xzH2eEo2Vu7HBOoqio7REDh0Vwjb79NwLYebMA97B3EQ3blK3hzwyuIM-gOCM4s8rMCiu43HA6yDlZSmuOB0qe88epb__otKvQ5eqCEYwMdfnEIgGsUYCDpoRH7njRbqUxqRbdE27eJ78nFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmCx_2m6-piQup3Wq6c87gyiaejr_V3k7RHcw7er6cAGwJdTuPaoHKBXfN2RY1HfS4ej7XeieDDCbfTgaZrkoMrBOL32VLPcNcnwKYEgh_E8hVe3vlW_NILJTz9yCDDQQWQllWnd2v-WEeGF5YBdDmrLqB82c3TZ8tGhwEOltTPV3q-HrR5sBBYw1BAqNFu9RGy5cNtzFRp8xwFEbpyoL0yPrF0detiDRtzclqyYMQZAglXOoWnd4jw8BQlY79l1-R8duC-ufO0tUgOdXtzwE5vNoGEXqfFKlCVJSeDyNQGWmPc8R9VB6hs1BMPcm-o01fTFQ4iID1MlkI6rcXBf0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPp_oq9nikiQTrwYtlhHguSv_Tb_z0KiMikvrW47eN-2OH_685sAM0vqPabQ3guW64fOdBkI4qgAW7QcfGuR_2taZ1j2YCQ-W-i4CeUR99Bs4YKcuCI4R3WWWJefzM0ktc2FOlxrOpJqRY3wMNBQnWCb0VFCay3zGu16ba48MnkZGq8o1uEcnsFqPatPU2Pk2QugpIbfYVF86j_Zn68y03LHMKHnYZvPtNOcBhjOamj3xFPbjlPQ6UaGtcxBGr8hr6etz1FXfg-4ME5JQzzpnxo8DznYJM1j8RJ1dqCLyoSaOSCk-qZWCmDYIge95P3dlP7IAB5yh8U8p0CuoQykkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6Wc44MFJS9vKbIw3FJUIvhmDOPFIaFOMj4Yu7O_HpbQqSQIsh9M7kEzB3qa0GEbRjbKOpVU8MI8sA-e5t81RfW0ijM29FW6APSu8DgXs8jmqReJ13-ZC-PHBQyhBlleXUiW_aKOeUkmwEVU_IfOqHfyLdV0pl3RvoXx2jpil5xMym-t-KVY1zaPNjZfQi6DWtVvCIpvZL97-De4-hEfO3Xhw2Z7S3T4c_dsdNy00XHH--FLZ4CPz-aGUrhTet0Lf3dV9RwXGzL2NHm_MsHvtJr1aaAp2fE_MhpXANXWsvt2s0BlDnwxMotgyt5n-0Ei7TfNkv2ZVS9QJGpCl3fRuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOXGw8v5LF32cz_tMy_esaYhDk9SXVAylsiKu8n4jrPGBy-pfp2sWK98ApnyXuVi_35etJ9NiLtmNntDWd6S4BDYDz3ftyLoq4iRvgwNxN-fEoP5f8q5RJVB6evDZfj1YOMSoPfhKYqTygompf7Vh_cMru1WPx5y3v4Vmr5PvsFmhjO7kkpd8de9N3rC7QLi-mLOiUs2Y3WNA-ie1FOhbm46eE-LgO-vQq0fc-uxjO8dZPG1ZqEb9-kmkgfp_SZfUcXjDXlLFw6g3DVS2j2FQ6O0x0MC1nym0mr0ArgnPb48hMPmL2kWA2GDaMikhEkSAnl_n8X8bmTFdTjDW5SKSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaprPVk7yJlB9zA1Em8oXVEgI9MWzfrAy_EUGhX5f3L9C2L472fXuu1N0BlcYc-fCDKQ7e-KK6obz8u_Y55DZebEHh2UyYiC-NKWffrI6hnkHCezj-sszz5247y7HVs6l-RQXbrlPIY0pk0DtGPDU_SMwIU6o_WGvohKnXAniwU-HSbGrcJfYBnwzLSQvN-ZWKIBgHi3qYdCMfBcGNe-uEEfCt5MsjH8nIpMpRhQumbwaoA2NWBeQX78N9MWhr1Wib4eBkKz18ESvdeEHfF0bnsQkl9LQsrM9pOqaYDn4-qe5hxfWN8CphSbOiISm2tFLP81kUlKzJs9WgWR3YF7rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-JYNK5z2MH5V_zUV1V2ylMVkwME870CTVBq_D24AIsSAzfeyJeEvnd2P9JevIKtAlvW_vWJHdGfb2C5d7nEon9bx4qfza8Vtz6agRqI8j8ekVintiePUWCPf_nU9w8wal6enY89nJZtlRdjQX2_reqyxbmiXC95JSdZr-lTXtzHwsyEzKb9d8ECrNU1RFduj4Z2muOXl0A-1uglvEssDoMv-C-vG4FnMlDgobddJG86h_1bWL3iDlrSiItwhytQssEEIWlO9kAS-hEzPetrDyKyAJ-Cs0_AMRGmVy4xpD3EYF4GE5O_POCGrUkTCwqlFDp8HSGKps3lPHd0rErYuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G9LLKmrgkaJjEf1AfSMzOgSxBJgIGfXsbmmEKSX3VlXARGcypr8hwxWsVL9r7SEVaw4nPoQKNNc3BQMuQSatbglwKIhfZ6ZDvr9_dohzkSW0m5yA05W82k_F-eWhbl22tktJEJygC3rmN59NZgIZd2s1VbwAKm4op3dyF69us6WK1eu7CL71O2AFlKiytes5TTI04cI9KiU0uojNlNxDHpcey1066-HHYk5ocFBQus7wPbeva-GEunWulw3IEGxXo-uUEakZwVGcLfdmfxfcVA4aLZDZQLThDYBYiI14p1HE8v45swxt-CKxJSH3qN8kmAji3VVGZZN4xQ86GFEXFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sq5LY8tjbpthOkZqhn5hCZAI4JZ-InsdgeVx2pzkIRt6ENEF6pSFOrNXCrLhmJWd0OfJapWGeNNqRfeWHEnZiqA0lx0JFiurUJ5hBvpHEK80NF6h_DiDnXxLlDyVFh22p1tnet637PUFsONxNT4ZY9vGtpKiaaCieUjSQrXZl4zvWmR8AR-S5k7DEgz18LswYB4Jh5FVXTMLlFXHa1nZnNgvvBBIpuTdvxfVjYX1XOjO1eAwy97bS9R3UnKCbZDcTPZ8wodEr6Mzya_EMEl_U8IJJ8MMRAu_OU5d078TZOEMjmQXxQ6wu4mplmTYdkCfaWgnszLgcJzDnQfT9KNW_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPKbFawfo6QxFhkm2GH-JGE0WXI06Esta7N5u11NAmXb7GnGbhiw4t2z_vflsawDTUWAhu3LlBSgYK9_EmrB1sGrtw-XdwtT_VobJxMELO8wI8gLmo0FWiBCH6ycqRs3K4xYmBeGDeDcM1OKYuLNhEwi0OZWTYZuIU2g2AwB9A_UklrE4Zk9rvMOEoqs0gcgb7GvGQ7esfv1JCVxt2DiB4DfKn4Vj6DN6LVC-4zYfzM5ZxWcj0WEnDtIYTTo9n-2F8Pp28JLW3NDh5Vk24Pi3b2nHdegqmZPq0UpkVQ7bPvLkPzMZw9Nh4i-7lFkoL1F1EWdm7nZ7mqLVlnvOt_BNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poHbKGG6fXkGs38MfPbavXNYvsdNOY-YyJ5nSeYnjJwQsIRk9bqZ8Gkg3FwK8-98_OW5i1QMYaNV8d-BrR8JQ9PDGqoYZFmzDDNQhAzSTPH-O1YiXr7_9gr-nWHlYmPTIu-63fXT4vvNKhz-nmpYstzXVG6LKN7slAodQGuXwc-Eu8cJ-C4TS22tbvVc87BGCXk7cp-hIkLejbSMiNh5scwy_8o92b2rQGA243qYPfdESNAOjqkfKgKULURtW016ZF_YxOOYFjRnhXl21p0wQmjGFjXxjb5DxihXzKaeANguyXYeuUFY2wReQJpv24xsAmoa2p0YwDmmnX-wnqvH_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoJLvsFvyTl10_NqXseHC8Y3dQ5rxopaM-degm0z0gZttVkrieN5cFPO1fgPZtXoCc3Dqk0dmj8fT27tjUcE46dJuptps_EhnT8qBZEWyfW5kk6aCW4pR3nFxZ2HaQLEqm6YCc4gebyl_BqkO5ecCOeV7ZVaeIqYHNY56m4XGTWIApXQ5_34y1cJgqGnkz9LqRo4fNsOQ2JkCZjRGsDP5C-5d_SO6mPCDQsgxt6nLK9sSbEOsc6Lltehqy8ndxKnUu_7G2ePAkpIRjtDF64P7SyzKH5MvslcHoSSaLwbSLmgUc7_g9mNv99aECI4pd_vS_BbC9Sofj-yj2vHGtFfMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGTA8gUH3WczCyhPYDZZsCOBNT-i-x9zj8cWU3ldyZkFB2hk6QGwhE3sg0pVx_WIN08wH_OORYZuhuUnAodSTSr2ewQfnz1JUXKyZdZvh6XtzdpnoncrQNysgq4nfJcnqr3N1FlJShOn9HLVDwV00YUs_DwOcn7UclO4bvpAKFWymZHQhg4co-9gsQu4FqEcOMJf-xfZaJiVA7zit7TcDr43FMAhV-D6jYTvH3UsanWmXh7fXz-s6XhHLrMIQ3xQvZTAMyaoKSf77b-A8WEyxT1FbdmYWVmFtQvOfKeQTK9IEU988fum9lnzp_uepoi4FpskDdW4-bXazZh4V0zs9Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=D7FdcS6Q4o5qGn-73wEZjT0gyJiVmkI-bTIUhw16f-BA3kZrdZS_f2gCa5wMvMYWtontF4Ur2zYo08VmQbKLWW21y-Gy7cIWzDTpAxB6UX-xNG0fVhmAx3BUPK2_mMfV_SliIAKvcblUI3axCyzKo5CmpxsuOBigCDMrIUUXdPAw8-ouLNAaycbQbnY3h4C0jQjskXWwUitugrVkSWnEaPzvSvEJQxmSwLwSZrk7ZD6zpz0h3QvYStKUDiTyT_zhqy28lBuKZ9hvpck4IgP4q6rTp-_xnrI8aW_V5h9FVF6Nk_UejCg6AGkh4s0xVrQdf34b_KjM988OdWkiVmeLKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=D7FdcS6Q4o5qGn-73wEZjT0gyJiVmkI-bTIUhw16f-BA3kZrdZS_f2gCa5wMvMYWtontF4Ur2zYo08VmQbKLWW21y-Gy7cIWzDTpAxB6UX-xNG0fVhmAx3BUPK2_mMfV_SliIAKvcblUI3axCyzKo5CmpxsuOBigCDMrIUUXdPAw8-ouLNAaycbQbnY3h4C0jQjskXWwUitugrVkSWnEaPzvSvEJQxmSwLwSZrk7ZD6zpz0h3QvYStKUDiTyT_zhqy28lBuKZ9hvpck4IgP4q6rTp-_xnrI8aW_V5h9FVF6Nk_UejCg6AGkh4s0xVrQdf34b_KjM988OdWkiVmeLKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMZrmwMoBcelTUOYrozRWh-Z3bCJqNFyT_4fKpAXhRVRBahKh3iQbkhYaaOm-rnFeCXNvUX2bIDT5jfyzqFe7wvNMNnegdoDvPa6hNu-tY9oCvt4NL-JdaWaMzYoKVvkR77w5WK-PFsOPyVi1UdbXlDEiSW6w-sXHPglmhbuXYlAGSdfHeCVndKnhPhc9wy8hoT0i0RCnzOZYSVyqH3XnjRJW8iYMjy9GoaYTA7CJF6KeFOmR03T_uOutQ-vbdoJfG_q5jwq0D1UrzCO5Bpf99f7IoAHdw9XKgsY5h4CKWzf_ACDr6RVsZgAJLHQsB6zd6Qs8dXWqJVd3xM3zlHm3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8QxVD9DS24xJ0bRNqNewJo9PLpun35329kNZrJh_XGwky1i-N-qlteliIo6F2e4QVHe83m0QnwFIvxF3dkWj5n65Hm3DhLAbKTARJqsWgPCziuTecpCJS34wXo0HtpsPOa9WJyqKqjZo8XhRQ1JvOSwOTkQz9r8nUl7At8NubXBKTecN6ganumdnruLz1k0bZOwlRjxa2Zxm1QHOOCSf1pt9fnkWpttZiguP7b89jwNKRyu8cVWE_cswco3NX4Au5YvlAdb740dcwRdLv6RhzmW8WKTmfI2C9-carRUGGJZpddj2CBlejEr2NsNBp8GdI6iyw-WFbo5-SbDK-dmGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5GDPpVvUqv_IZoHpQ939e4zsr_rU3FIVdl6Db9VWmID8AmLbJflPf9axVvJKlkAoFIA7NCXYwFNkjL-svsQvfF7fhMoOKh7P1Y1JhGWTpqrzu7Rg4HsKQhGiYncZENEjs-XSlcwytbkzTryIsPylPNLhap0_Z4yrfRcgT_g89weLABx3L-VuKPieLpgKspLh26PwK_NGw2z-hmY5dC_2qZI2ECozxD4UYbjauwiuVQ5Gi7C01MzikfR8R_RdiIIRoihC0XEhIoiTKn5fE0HXYC06AFy2C3RyZbtMxQ5z4LA2STEli6SZuY8VoxuLk-bTtnT1Jr22TSQZaJGTDjN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtFyIjlw8nHUgq8iSAy45OgW0WdKr8taT96LwZ-mPsNnhdWjjwYc2B67FPmRZpIYG54tEzOjtkALfCS4LgsQCVHd8vyOtc6xpuLO9Al_ifDb0FN9lvW4tBEm8GICRsQoowoxjlxFst2rOanUHqy1XC8QBPCxMq2tq1HYJhuT24HY8Nzyuot7Os5jY_htiuAZz_Umjac7wys13TOfWkBgBLlS_0Km-I9s17rEGneUCCsmm9scxhD6RbD2_5h5Yk2PKJ_hWTFjpkf6NlZAEOopRxWaY6IUk6aUdRf2RcC8DIaRhPG2C0361hVqlcjfxSUTYFbCCnNMPAMwHumVnE-U4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3vxs07yUVP0I2ThpNHz5tE4eqxq-SyN7I_-VQUEvvZqwLBtog3BaoTn6A0RjxuEzuAv3nYQTV6A7mFIPP-rpWwccsSe452Z-gavT8xDnD-U22uVfmkgh6h5mJnhc15cpcwpOX3rFwJuGvS7GeRvpRJYKsa8PPagFQKct1_SXFBfPQz9Z-0mKGr3HZhmLhK_5W0uLVO_urj6rUTwI3Dledn9i4EvtjMmwsiKhDBcG6fmUlXy0NFo6Ua7kFv0Z4Xb2aEZg2KSHwnhokbHKUJqIPkEIvd6lAe1EUjN0XGeDLHBBgkzV-uMKtNblROjQDXUIepaDERjhKRCoMFsemlxuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1B8xGqypioUnDYgbgk-g_ihnZOAZGrDHzv49lVvA4Q-unDCtog_QE3vYXBLzD4SMuieaiaQ2ysiPfF4l_IskCBJtad0lKDf1cvc5UX9hd7S7Trz8nzyBueJxY2B-W3MIUtkIWlY9FaJIUnO9qWRqDW67o_JI01zWLTA3meBKdWixXLO1e6DMRMIaK06xgLpsWDS_NnBXZnoZwCX4DJvmysqSTHh4kgP2LV_LajJVr7mYjuGmulFvtAJjXm6-0Y7JCpI7F5FTE4Twt6dX2DNKiGYCit5NKyM19WlV1lxYL7txQSjP8Ep7WAgTQjh36PxZRPKVFP7QySshkb5YMmc6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZg2S6G9wmp0yFMpHquRR5UHLGDDDuPadq3s0uiKnG50CnZYTxb0mSHHw0miiVPMtPqXdiDUG_jFwPk-JIHU3Gcq5fmt5P0UJKOkF8uF_duhEr3d17LP6pk_zWR5Lqe_At_Hoe4XRyfs6pE5mLnKvnVARW4p2lSdCcZSCyJ4OGJ83_LMFOfVmHJTaTkxPaN4fD3_yC8dnGtJFuwMKDqTObLG0DDonsnBGLFezpvtOX5IuRdXKxeiReWKSDjbh_AxGb8gqg-aqNw5D2qLCZy1ReBFLg06i5l0_rsAitaC1zuDzOUQqlidSHxk_gBgVMMSg8Sbzk9zFtqGVnpF81rKNg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=MZdmNsvs1R5KbOfOAh-c6goUfhIyMVRTlFq0y-wkh7nJ33qqfjlL9fbqehX09OmSFtiWBYjgFao-YoDQaMRgoUj0LwYLsLC5WNcUIDC_KNWRG70T017d4nrx-AT-Yu-RKuVhc6WXY_15IS3qRv3fpwIc6U4lPx8WVyHy9ShAQV-kiKc9dU7QBzsijamLKegCEzSBg3zhwmlO8oVgYVikdlfDmemuRKcSZs3XvhV8ka8idQJ09k5ZNl9yrJ7myTiPrG0G-aJ4UJh5VJnf_c-mN3DwfW3SvBwOruvINuPmeyXeI4xeMjdwpEGruBj-3X8tkiozR5T-ruMHt7swYAWgnB-MPpVHZInUElF0E3vUyD7XdsycYOtoTjq_1VK9UzqSu8SPT8znuyZFO-YUwsEJ7KO7CbiU0Qd0UAhmVVbIEm53HTNaAQ64vDdsHPwXMCJTX7hanSaRIczi4VNm2QL8wztN6mClnCXtfEDg37ZawYgqZp9pK1L-1CRYfTo45g5rp5Eyx85EJ5wPpHMndIova7YorL9EoUIe4AX0GAXhOrf-KZV0S6yK76ZRniK9OiM-mPhfxSsQDCwEmVUa6eQUdbV-0ehIzShk-anXCVn9--yi7Nt_lSdp4qwsKQTUf7WsgzG0aI0DkBzUjgv5Z4F5oTJYjSLmWHu-fgZQ-D29iKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=MZdmNsvs1R5KbOfOAh-c6goUfhIyMVRTlFq0y-wkh7nJ33qqfjlL9fbqehX09OmSFtiWBYjgFao-YoDQaMRgoUj0LwYLsLC5WNcUIDC_KNWRG70T017d4nrx-AT-Yu-RKuVhc6WXY_15IS3qRv3fpwIc6U4lPx8WVyHy9ShAQV-kiKc9dU7QBzsijamLKegCEzSBg3zhwmlO8oVgYVikdlfDmemuRKcSZs3XvhV8ka8idQJ09k5ZNl9yrJ7myTiPrG0G-aJ4UJh5VJnf_c-mN3DwfW3SvBwOruvINuPmeyXeI4xeMjdwpEGruBj-3X8tkiozR5T-ruMHt7swYAWgnB-MPpVHZInUElF0E3vUyD7XdsycYOtoTjq_1VK9UzqSu8SPT8znuyZFO-YUwsEJ7KO7CbiU0Qd0UAhmVVbIEm53HTNaAQ64vDdsHPwXMCJTX7hanSaRIczi4VNm2QL8wztN6mClnCXtfEDg37ZawYgqZp9pK1L-1CRYfTo45g5rp5Eyx85EJ5wPpHMndIova7YorL9EoUIe4AX0GAXhOrf-KZV0S6yK76ZRniK9OiM-mPhfxSsQDCwEmVUa6eQUdbV-0ehIzShk-anXCVn9--yi7Nt_lSdp4qwsKQTUf7WsgzG0aI0DkBzUjgv5Z4F5oTJYjSLmWHu-fgZQ-D29iKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INSOjeGovamKujVF91ZyqHdujDHsqFJCOUEAeEbAzMJSC7n6PuenJ0lDI2tx6cTy7_uxv4S_P6EOI8XCclPcp5_Q40NAg-r4SRF3-aKBpC4Rgr0FobNHSX1ZZqH3dFuDS5x4PgaE7MiBUMVnjZLBFoIK8sf29Blne4xBywYpAtbGdlceyLvh6mwq2Jnerv6h-GCkithwmJTPmTi_16aIZzoXksmlnhs6xjY_roebsjr0Lc4YV1H8SooiMr7Q6ysoJ6EjKDkrF35iu4_ZNTBX-g8F5DjVFo-YPfb21iYs4R9Wd9o3aUP1FycDC0cvmUq-p3Ej8K4LYBtlO9OKd7rm7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RhbvAEJ8EARdyGWOgrTMOfQ4sw8wOguYcwWhR-9MhkZTLPZMv6825BBbJI_Q7OrBcpDgOxz9sk-X-I1Wy3kLeFkVPa0eRRn_lm3D70srddT1KVaVNy7P_32WzbrCQOFeFuLUE7IJcwDdPOHI8IWAKsEekquna6bzv8hlUvS2uBQUHpXyQinuHKz-iCMc2DChe9Q1gittOGfHZreZeRdHCrlEiedvHPhcW7awEh-iBTetnCynYHRTl8satiXdcXT7QtS7CeYXpsLk30xfUyvd0fx7JcKMt8OcK1vjAvf1tsCtfGtAPVtZ4mpDK0_EBy64ZIvpB8HSbKjELMIhl6dU3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6wo9r--qaG4c5o8gAif4EZrqYZnDv-e3ZEBRBSi3psi-TRMudhb7pEwNG20V-kOHvYF0pDJpXwgZF_9yNMnJ4hdaLcH2HA0WzXnCMQZq1rWCTrESzWsOSL0-o09sDthN0V0AFCiqhYlpyh9HTwreGEntyfZ8BsNgjYv7psNJrDtphJbPmhC4ExJJ5vqALcSR-ALauL6nVatYqN4hDzvkXXEidm5YZSTxUytPnqWau3LvRwkoUmBWBjFf0zl3P9Edf9mgYK5RMzHG3xl2juQ2KK5HqP1_JNXJHWM56OMHOR-gl57bEsavXH4J9wBOq9DiRsNSQDUj4sLFsckNpFzNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uCGrw1BBlG5WzExZfysa3DNs9HnIMcqEXBqR7xrk7bcnKc2gs4PwdrcWph7aUUpKC8oszhfMeOjoZ8jcJ2Ixb6X-OmXTsDiKmVxbc4JCbYlsDnBgjYqaF144XCZEPcmQ8YIOt8wi5HJqSwxxcAwXYTGIESFGYDP4Jt5ZcieXKTnQB58ava5wwDex_OL-cX6ZHpeY_aiCLfbsojTmsOskzoKYAA-UUb_V5IKX9CwQtIN46bJRjFtr9TJ4CDCMHRZsKFpbOjpU9MGtaSQjCNgtzIjV1F7AroGmVvzihoVrOQIp70tWvRabJvbLx_aLhEWWqTzjhiUWQxtyVaAxf5S1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3CbsA-3cIf8GJCc-dr0EaqAD4mF2YTaI0NqwQXqwrBgH61wDIAU0C5KBxlebW21bkMUi2sk6Ufc8UfbGCDCwxV8wKn__RlXzPV2RCDLsXTvvHETxH4DeHWPqi_U99IMFSL7Prrsx8A3O45BZ-l_MG_u4aG3s234s13dJQnAVc581S73TOohADj2nL6Jc8f8eMp9bCoJ2dh_uImTr8qbOaYtJp4oqox2kqh_tjS8nACibRql4aQQaixPvq8m5GyM2S3rTVU7c-zDBKWF9HpahqzgBfV03ZI8xIQlBcv0UuCO0Y3DhnNPJi5NWDaplQADiYBY_FKcBoh-9OTdw1rVew.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0QjOTyLxR9dyzY2EDabiZGtQHfw9_8cvhYKDiwqCY1-ercdMPB7MSb6myMo3BL_KHhMEgnVaWlI59IpUk2tvV_-ZwwUgIzx1-GyOqriSRyfKKcLTa_292Cvx7l76ID948-OHt6P7rHeyhZNocv1tDJQT6i4n60dUPC6-3Q4KIgsmeG2yGibzOkUZpFutvNKsK4Lr3jOVU2Vp_yIBswvqdrtAud4qV0o4pVJjYoJkB7FeGUHJ5bneLJ7LEqA74_FsgBmM-FfDFwzLYydNablIhLq9dsKoMbOawcORvpR6BcfeH7u0FTLyPMUG9g4Fz5KYae_i09oxeJPpWpyVV9CyHPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0QjOTyLxR9dyzY2EDabiZGtQHfw9_8cvhYKDiwqCY1-ercdMPB7MSb6myMo3BL_KHhMEgnVaWlI59IpUk2tvV_-ZwwUgIzx1-GyOqriSRyfKKcLTa_292Cvx7l76ID948-OHt6P7rHeyhZNocv1tDJQT6i4n60dUPC6-3Q4KIgsmeG2yGibzOkUZpFutvNKsK4Lr3jOVU2Vp_yIBswvqdrtAud4qV0o4pVJjYoJkB7FeGUHJ5bneLJ7LEqA74_FsgBmM-FfDFwzLYydNablIhLq9dsKoMbOawcORvpR6BcfeH7u0FTLyPMUG9g4Fz5KYae_i09oxeJPpWpyVV9CyHPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvMWjQHiRc7We3RkHv0B45RcaOksPE5aCDW1JFnfkuqQmck6OM-1N66SjBWDtsZskPY5oOJdmgwPhSkhLYk_ip3-bVazOUC4Lk-T2mVwMZO72kL_aBdkfykSzESWbSrWFBgLSnagpq2bWgAlfjK_637DO79BFJfnINSHNfHrjMJff6tJXxGVFA3Z5qqj1ftfj70zGRbtT2B66dyqpLV9_GeJVTK1GGx9X3O8HngY5syqtsWRI1gmO1KDOP7zDzumbt42990y2f9iXq3gIrG-khmBKey1iZhrBfsuVo3MCtdkLMzJl6A9oM03Mqb9_XMpDCCCkyHRCqY2auxssbc77A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYjnL8AncQrJ95_bllbUhMvlFgutFFEaqpSoSoj3LZQTxhODqjBBnJrO71JKe7hBMRkLMYD6hQ2ee3Z_C2jN4_ZT4YC2Sg35HIT5Frd8cpekCOIpDmr3bRBAUFlX4WLNANwwT2xdPH91NgPPoVMYas_q0WoLsGKtsmfTe9YqX_8oZHQAC8IeSzb6LYW1ROsQQs_ksYyqPJw1vjO_YOb7RtGzKUJgWEo-Un5RBJFuEwJiWcJ4SihX1cj9tp_rVBT7cdGvqfeulsAjvLpKgdaCOqq2NNn4sN8H1NHA_B1ZHRqp7WhDlvK6GWeRmPxuetmgv7nv_V3WNErXV3hEcR8sfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPSxkJNfcKIJSM7Zk2rTG1gLd-W4oQWOOybFKdCMxzM2WWrDSGqwqGYlgMqDnqukidSLvhZfZIJcICKOtq6-nlEZxLuCCkJ5l5jg4OnGEHQgCQ17tG7seZUiJitr9-7FGV0HhSFCL8l1wcDrfCmU98o_gf4unSfAiyWiwNkBB3wwrUuabpm4S9lDn2mX-9L4kkMaWD2EwGyCay_8p9bIqf_MuPFXDu31jNt4QEbBehL8yDFgI3QtpI_aR8zHOVa-VJAgq_yU8lKrFgIM-tBQ_N4vEajCH-DJfOSp-FiNP53jSWDPDRWE8gUqSYF-GaVbWXtA0gxifKQ4VXJxmIhRMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LywW0RoAHFnG1vWy__szSOFLx6JQuJc31EET5f-r4VyzF8pwgAISiHvpqd83zbP9Tk3tAT6Xty2rGSA8p0zKy8woOvfgLeintIZEByeiZhz5YSkNqVmrU7BDw7cCv4yX4StLYxNkctygsg8iENq1IAm9UmOnXLbOHKr2t1jlDBJxgdgM3oHbkgMdUGHp8DQTatgFeo3BY8ZyJ1r2l6gDSnqpN9c560S8JquzkSh56xOUI8I90o9kgxGuGnEEzlfLP93KyqAXP4aGluRF_gM5doc9NZaUCA-Bdmt63H3WxYlWhX4z4jWVRV4yF5paP_1WM8CuvZNrV0mtRUEhrH476g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NG1KXG79Zdot4JAqn7fArZThKhB9iixoK6g4hnbcGWHPaCMrD6o9Ed9RpHGaDWe3GUf2k4JZZV2DJVN2wQOBx4-unyq8_bHblnJ97j8QaAFSfBqDWhSFiMOHiWFo-auq8BHQi81Go_7v2poUJzsAJnFRmgVhXpnyWSRZLY_I_-_-uhvqc3niFp81qLOkKYiTJ7poZQnLHmheX9cXmovKHFlosqEvOA8g4u7Qly0wLOOo-ue5ywZe1WvoThY8nYbOmuV_tOPwjIFvMwcMO2fqAXroCTgMpdwbADE6ZqF3Alvr5rf508yb3UEgWmbQeqILD1CO2Ssl4RndwlLce0nRxg.jpg" alt="photo" loading="lazy"/></div>
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
