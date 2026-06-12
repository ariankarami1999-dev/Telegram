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
<img src="https://cdn4.telesco.pe/file/mN4m-epBkGk1PsZzmS34SDKNNbi9aR2MbV2QKpAgaqnMfWOI5-r1ySYkqLhyqGOMF66-C0dSZJLV8TjGaNpjkRVl9RfzycU6kmxK08QXU_J-nme_CSoTAn-rB_uuR9qzy5Q5y_Wo9v5WrPSd2b5bTQ07cRpvJoQJoTPzw09bvba9QB0SxjIwrDJ5VGo_z0Gp4aE3nYsT1CAfRU6j9alWj5gu7RCwxkzpR28fGF-foqCiJv9A4OCdUQqaMrOnBxSadDv5ku6Du6naDCPqgf7lv_tBsTRU3C_6PnM_yVP9r2XC3-kRvD_WTEcR-cBJwqaB3r02YliDaoS7-F8qiPcZxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 14:17:28</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 282 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 325 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=dgSxKcMqpPvJ2R_nEWT9LnCm6dQ7Z00iwsb-VCijWUabR2PY0ntKjYqlDtP7nZpGI93FppSFTh83ASvi6W8B4_qsdgq8Ig4nSzLztIT7SbGkrviDMuWSqv0Q8yeLc_ii5N9YMbS1CfFwlrIuJD4TzgVvTevn_AT0hHsGf8vc1RtQ7fc8lBdQNCaE_CRUhEfqhJfdPORf_hOpwMUrL0PskciPfGpc6pj2iZ7qcBRaNEYtlbsllEh5r3da-q-aZEuOfdF2OvGRh3f9Rl0Bo1d_u10c0C4DFJpW0_oWuyeTNIumYdQBHQZE01c_TG1Z4ta_BkDmMe3GprtG3cOBK2IEvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=dgSxKcMqpPvJ2R_nEWT9LnCm6dQ7Z00iwsb-VCijWUabR2PY0ntKjYqlDtP7nZpGI93FppSFTh83ASvi6W8B4_qsdgq8Ig4nSzLztIT7SbGkrviDMuWSqv0Q8yeLc_ii5N9YMbS1CfFwlrIuJD4TzgVvTevn_AT0hHsGf8vc1RtQ7fc8lBdQNCaE_CRUhEfqhJfdPORf_hOpwMUrL0PskciPfGpc6pj2iZ7qcBRaNEYtlbsllEh5r3da-q-aZEuOfdF2OvGRh3f9Rl0Bo1d_u10c0C4DFJpW0_oWuyeTNIumYdQBHQZE01c_TG1Z4ta_BkDmMe3GprtG3cOBK2IEvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 386 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbHGMgc9edUfYBx6PWqB5le3mPR-JR3R-ORLwRxKOx2rbapVXT98RzsMSVlVmwyxfMkWke6_qa0lXV6OsPEmMzyemdg8bVTCQhUT3UW4mVyUMMTA3-3lvhIW9x2MMHckyYWENiM2lJOtI0u5JaeOF4HMJB249aJjJr7aTZ8y7Wts9r0gMksRLZHO_zISCLrjkn-UReTxTLN5bgD4BQw22jcBcbOpok7CVON-QpbuNfSZr34-uyq-a4yeQ7Wimgs1jvK66_CfZdVvf1vd8QxT8qYhVep4sd0KwHWvipX-4bBZIay5gRO9G_ibU3u_NA_m7Da8-Efzwr7qMNjPMy73OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 508 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 733 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 830 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDPyuAD6yAVVG9uwTek5XclXgh-xtOD_PlspGsldOFa5aynas19XXjOq_gjenK30W0J59YhCCAV03fFbn-L0qCYMnxXH4eCOrs8QCwWXLe13YOgUngHJm3W_KGLINz1cL1Sm3n63KMq45eKlBRxYURc_V11IVkASXALe-oJFOw5gPBI2SlyVWyb8WsiYPhw94LuK7hfIdlw-urU2hCB3w090-6WXBlwkhoQcQJcpKeFp53SrAWVhCEg2zSou-vdvudRPJI6gUo0jFAa-wYwvpLfh3r_hlCErup0q9cpYYI7AlmcyOrGqA3UuunAM37H20Pw3ETNZ2m6GU9p4JD8MXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 865 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZFZj24JdIDcyIFBG6RPalHkkvFfH4Se4tMExCvp__rFvzLNjGmFqSAWR9BchW8OzrP2V03VRgpe-InUVR0YtooCbm9zWP2wPihpq08ve53FftJ6_pZPFWvLk7KtrkuLhDL1n-05TUdKDOiVxb8tjw810OFdrv5YNupilAbKsOmrudC_BzANsDMuc9qI_7iMp0NBKC-JNVZ31pU2sg0-TgNsOMlAQD6fvunQ4Oc9Tse1w51QDu6tptP1wjPFufDvyQHAwK-twVbjoYgN2cpSK1O0_o5h0YAWX8Nlhb7aWh0PoOJPUKIPpv5X8ASxrs-3Yl39JvjnqDpUcFkNzcP8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 980 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHMcyHOY5e3uIJHpXcFcUnvQv0yfCPg4OG37z9Em9iBWTo9X610mauI8s9WlMsoIDZp_llDGHXjMqfRNP9iVGmmQkRGm_QEOeVuVeA4McKXPnMVVN2n5WJw5CTuyqCw8ra8Gdu5xhEuR3SPanaadObrEwkB7ChYa8gqGR0owz36IYYI5N5O5fT66uF0hrDvLGXPNij1cK3UIAgG29D_SVugKrr0NEc0lykZ9U_6rzBBGFDLE78v5KuYBTRPgO_Se7oUYgYsi4z8YGXBG6gpXLqXKHJyOWUiBt8vTjQDWgiQsKaleEj-tpEe3Px7A-gWBC7MKRtwa0gfxP0R6Ayv67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxdI1A42TXmqmp1wgThncU5DwQ1PW2Op9xufeis08jnyEnI1hF3v2bXo5ZYh2uBGHbM4FfpTe5rxGOJTJ-zVIL2T-ebHlmtD3vcu-O6Devkt-IfGfhen2oX0j8Cng8fTkWIe2Cv90LFVDG8c_AtzbMUy_9i_I_j8X9O3gJpU1wBed7poDDgVJszcnf2eLcBE39fsDBsLplZWkcvJ8xXp7SxPhxW2SheGXpzZhOO_yswI3xZ_JJ5nwBHef5p4C-HtqbeTAgsVTmamcKZMpuF8PSjzsY0rppQC0_znF6aTPSlAHZJ1C8ohEYCTtY6phC7linT-a5fSg4xJDgXWetHziw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OL4VW7mW62W5YbpwZXCEdgebJsbMBxNeMA2bVNL0vCJcDdQ9E6Fl_6mfCXkb1SZBUx0NRV3VOpcW8xyWG4gSx7FMu2WzGqdZjK0agoo0mnHrV97Qp5J5t-zbe5fesFSX6sRFk6XcHH2f8CVAQUqoQAarPUJDr1AssQcZjK55w7iEGAaBPQOtIpl7y-gMXCFiRKmsi8YYeOOKkrduR-MqPGOzVa2QdRnDPxy6EoRSCl5Sx4_URb8Kf-K0RtR57ms5KKUBi_dAPlOf3CmwpfM8gHh22oXiimhhdrjoo61bKZbtkwoy6bQHrNqgLuuot1EUquw0OBMoPhpxhvA8-vXV8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 878 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJF8Ii8i51UHyTLSoEzUYNunI8f6aEVjg78jo9KESvr7nKOheiWqNBmMrwnq-iZDosSeU02M5za5ZZsy5vMNo3iS5fLtF_4m7VvISgibfv1-697V311_9J4pESh9CmLkPv6kmIQauvSLBxIbJgD0cI9taTe211p3w5SWaG8fgRU1YyOPhGBx8UJ4sGakFsCoshj69K6dCFvkBnrr4k8-_fcuHiu5Mf16u2t8w5GDP3ZtR4rB7QdF-dwoiZZtN5wNu0jzs7uwlkUeVSgmhw6RU90tmokl-dIMK5mcnQDyvE_2Ps7NhPZq_ovdN0axRbPnCoT6x2EDUM-5SmqeFgBFsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D28_UlI69WkiEPdzXuGMtF20jIJav1xOYnBpCKRN6zknTYaFzTYMXSbb1SSfY_jKAtjTbguMJksU8wjesV15SyzWQUVuzGBfXQRPyyw-eGFfSzPFYkc64wghhbobQjmExNTA5GmweXb_vt6Fc71AsWODB4eKB7rJBbfNTiYymx6OzH5x-ysgq9BGqnXJk9M-PSzCYJxALBeXFHJaj9LMHiKridiochusI3Q3oFtXwq9sl8SaMFzCMHwvuUk81x5HOWOBZB-r2FCTqDcGZQTO7g3l2eks8KCNo7fIaFuJ0XDK7X5eRsZxjAnbp4pak5g7sNjN1EMa6GhxlgdVpVerFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHN81s8B4PhqdaUhbdrZT46QtkEHejGyQd3CKjZXwbSkiswVSGX_NzxPSR6ragekOvg5mrUi-FdD52ZVcsDVLT644IvvLSLUa1-tugjXTxjg6qhTm8BnAnBKFZ5ap8zu-0k-TJUtHOlMSAsPL3-DZuETQuqs0p12Q6rmbZvtvLZUhlNEm4b0RQTFbp_Vo3mt2HpvjZeWrCsl973H8zoZBYbevBs0-F_emZ9CWNVnQX9D6N7So0pUB-_Z_vcydBH31grb9OCvCXeyMjPgovtwQ-cJGJTjBZ8elHAaxNfGT7wBn-fXRG8oc6tRi0Wp8DxEcBOhdlRxz0B9qmTcKhEMeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HV19g5XzYNK-CEuzg5k1BK8QACRCdxo271duSM7qOeW-oWTWmZS8KiNFQRgAmIHVd9ZNBpc0Y7knjk8G5ttP1J7tC3czFByLJW8pIAIUBPHmpUPuYFyNdNoc3jcSz1NdndYhmP5VUyODZZHb54ROjFNKyneHqnBEzeNhF4D9Z6wJpIHHYPbiifLFs8PLjC1MWjiab-eYg53kJ6X9_0XfdkRSxcKaPbZ4ypZZJscPmueu6rdVu3-QpqKnTPl9jQQlrloDBdw6cNKdZ8mgC-Z2pnLw6hQBK7ahK9z7odlYeOVtO9f2NXUPZmvESB0k3DdbRvAjEwS_6t4r-VD4nRWlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 944 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 667 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 886 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wu9rQBHKaLYx4MnIJGfgc3m9wIYZYegIw6PZ8VY4feJATTuv_xUtrpJqdJ8yB66BrqAMvVrdbz6j2qJdMq7kk1erZ2z5riUwrPTRGdp4USacxiTt8mNujcU0_etsXNmWn0m5R2hkmcwQtg7pxJ_4JtTgV25wc62halP6NIlg_IPsviCULJtKnAEie_W9EGEKN9dBMtRTtAnWRtnPYUgd8up1ZrDpEQsBauXbM4xdzKIDqjUfyVXrPREIgF5JMaqko1bbtZtG3XfaEgtRGSxu5iWGjDR3GsGkVzONeSsHXwLdV46GB3SMzvxiOEZde1AI2eWQnViuwXdala2J82p2Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 869 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 815 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3Xxu9PK_FpghXlZdVABpxMr68DW_yaon4ZAalSVrQ_hnL1yNc4SSLrelVl0Ufela8QYg6oJojgQY8ysHwty8qCsPUjLtAl8DyISxhsyFLHMKB8d2uVSkNtsL-8moIfqbh6uoAQjNcVHdsfizkAj3rLNYkTkmdMt-EBoFdA6h8EIarX52I3S92OVKpcpmY7KYbC7wgq8HiEBqm9Uy6TrJJ7W67F8DWTE3FhycvHxHS_KHc0dXenRrLT2KflJscmVrdTuAhqwXi-KaKeFDzn8J3SwNidsFf3p5FwweYnfmFzSDhwmco3QVpF4glrO9w0Agq9wLmAKmHfsXovwhEtZSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np0BB2ZgmcyT2cLGpNt_TwVhXvu2ja_v3szOs5uxb9F9kMq2jZsmRouzgIrTctg6-yiW7wGN7EC6ppEg3-_--U4eiNSXi60CeCkwPdx9gLAwFGXNBuDtEpOrcHMD-9oI6vUQS-VCbVUVq_T-nimuguBK7Wcqr0uc4C7iBuKzuiCNiDmcsbvG0AAz8SU1FpXbShS1x8CwlDCrP7h2CtYProzJ-rVkLBmxDh-qbVM2ehbIR6Wr2qo9EGuDBk6z8kVl4UhpPoVOb04daETKpZAXHnlctL6xJojCuTqBB4lYcJY1ohH1sgz7mJdPgT6NpkExReU7Vbisud0ZTD504QjK0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZqQQ3OF4eucWD4A1UsWhysrxihx4fZFW9FdkwbQPcNxgPrOVChFtGfWdxqq532lzcnY3fzEcmyTgYZUc8xAojaoLnqrRfobk-n8DYOz1vaY4nOfAU3QgyrIA_EZpt2sHraqh9SI82qq4BPCAlQ8b40i913zR-Q2hlkt7TffgWjd7kkF7s3ZE4kTQesF13LFMOWhejPXKGC7kFq95rEyrfbhVA-D-WbGLC8rRnywEhBRFegVVte2Oo463bFZO31T7o2brqrwWA_1cSR7jkF4-_CLz09zDqtddYwksp9d6vmN81HoTjmxCK5BDgaybMLT3vqZ0v6o7Jye2VIYhJdOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjsT4sapeCcYQfuxH6SwZLBFi6fTxRYBI1UQKpkLnHh6MSFYZQDHjqv_vzZx5kBe37mr_oMsj7cEQcrFp81T5cf-_ZpssBCbu4BkMeUzeTXsFk2lw6Ps7gzyP9o_SeqIlSGOyvWTXErwgQTa324SkMXwyFbcoZk-Bgt522YheHZq3s4lG_8R7crtejCY1okqkLsKbo3oJS6g46jFnGLE3prWNlGP3YL1hUzdufgzpC6rGe2jqjyO9VyzgBgdszq78qsnUsW-zq00nGImyC0NcDRRvk6WhKFtL_C4vflZIu5_yJcScItR4XbCwYBJN44tx8mRhUgl4jr6bUyceKR8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fk3LHqoWTRV63s3ZxdQzNmvIEQEfqdKFjG4AtPrjB_j4t96qzBd9prTyVxRRaEv469GTUN9x2XMR25Do_TpuzSu-_gL__Gp4ZWUMEBC_VSbIfAzymnYa05tADiuHHpgZmYYRF7Cxq95GHObBnufX5QaeFX9IOjU17UiGeCGz633H2f0BDgCkuuL5BlOscgnacLjed3oRqv-O8ZuUhDxRdWBHjA8mBtdTOi-iofI5Zte7XWVCj8yb_0OVf-F4od_UaJVNDd5tgPRv2KqytZTBR7lnY3FsULN75u4UYy1h3ad1xm_QHGX7dGSIufLtV4mBQEmIZP-nytDdHqybBUVmAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etHquUGh-W1efGN6qL6ZozYaYHPsODm33V2xm-VijZD7Iz6Wi4f4wJLTjAYdAA0iVcAXB8AGqWyXFY56jMTsXiNVdo9eApK__H_MLOj5_4EazMGcPQQxoMMSv3_heygIBHbxv9V9Kqc_WIjygXin9FJgyrKp12LGcUjzhVZkn2YyJhVxryf8OahrfHbxFevqQgyrRsDunoKG3Giw5mEp7q7Vto32DWuLQmWz_YKr3rzbXDuV_MMBxh5Z8oJK_pWO9fazXLifkeQ9abfykOBCG09Nyp5n4sHp5WrRt1mGUnyb05gHA3FvjAqBXBofxMM5pMYjgp6d1cdfMLVjbwUEfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoPUEu6hhWHZog8bN8M_sX9zgenfeNeaHVpL6N_c1HgYzwcRUMxBsJfTEB86TOZ9G8Xru8pSiywXhfmsOgC1lRL-hx6LQxC2f9YQQnQE8fJtgUE1i013VYxHgDXO4hZsYpJxZpm3_E-e6pzMZgMax8Rm0lvadQ842XY2if2WOkgEG2tmGV3o01VrZkcpNG3OqiS9x713U_TbicEbVnicYMV4KdxD1eNGNlAq-wscIGVwsCD6XERWWMNBD-w8UtjLJaKbCbS0g-arrahmP2LEjIRJ-rj9gecuZWj4yarRRiGtHybfhO4_dxxN8WFhqz0gTH3cedsYKeLqZeCPny4MpA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=q9PjOsMbvT-iWJO2w9cXIXk4z60ons1C-pf8iyt_oajmPgjJqNQ8058MTkVeYlBpQe4xL0YAsKgIkcB3wS_rKLmQthbEU6oa8HsD2AYZ7P6szW8AhmBQ102SouBM597XU1bGsM3nDtGAT3OCWrsV8iOs24-bl-G9De4z0uGT7vQxnWspUg4MYeht_stCuZWqEX_Gfkl9Gb70rmZUXROjEeIotxv9Lmwu82a-Kpo9eE0N_kQeGcdhVhAm-tGSQI0VvkmqWWwgd1MocOChko2InL1nRa49C196tChG7QJhzzwZTevtS6cy8HAEEQ4EuxTf_00sOMT6khAen6FVwwtjQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=q9PjOsMbvT-iWJO2w9cXIXk4z60ons1C-pf8iyt_oajmPgjJqNQ8058MTkVeYlBpQe4xL0YAsKgIkcB3wS_rKLmQthbEU6oa8HsD2AYZ7P6szW8AhmBQ102SouBM597XU1bGsM3nDtGAT3OCWrsV8iOs24-bl-G9De4z0uGT7vQxnWspUg4MYeht_stCuZWqEX_Gfkl9Gb70rmZUXROjEeIotxv9Lmwu82a-Kpo9eE0N_kQeGcdhVhAm-tGSQI0VvkmqWWwgd1MocOChko2InL1nRa49C196tChG7QJhzzwZTevtS6cy8HAEEQ4EuxTf_00sOMT6khAen6FVwwtjQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfrLj2ypTKNkRVdQOAXtxhfT6cQTPrN7Ny9TY7tgfl1-7SNZT2_2EPuCpp2_ORX120DoRx7q4Xn-TZ-CG3A1DDb6L-kmZTViDKeDuusWoovG6kIuIj8n0WwExhUQbX5SCXBoDW_AVpminGknc4RA6EoX5p2_ILsAzdUq9T6a6VrJRbqXbeZ9IUwI5rELC65Husr4nkVup_NGj-FBBh9KzwBWZey1lmc5EKwGHOrEpyutuTsf-xP48qaXhNXZQ0GxpUFCmPfiDaZ_AQL7pIJVfmcY2tJM5bYWjS53znN8KkLSXT2YBXf7XfPn_jZ1XZWc6KPxkPSJqXhoOpYfMzu5jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 927 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slXaHMr5nGLRv-HXERMEwQVzcsQ_5msV0bU44kNFvY7TE4Nt64jy5FKF-4PeE-Iq9g0ALJUDJHoCDrhxaGHILdd3YqLQw6UdZD5EBip_tfVTJWFVrw83X6W77R-gEuDkDlrLzbl89dcZuaJG8ZCsdstBbReUFlCwUhHVHAOs6is1yG3DGe2vPJ1VVV92hslYigvUmGIr_ESaHDCuyxZs39qH_6WSZB4X6GEe9Fa-oOZVxwTdkYV7yS_ROwmi0olLHYVaoFhlc5NYY1F9mhvYsqF9N86JotRp1QVPeBfb1KDRYslhvjbF4qCPfNak0BtJOIAENWgdAbXZkZL9ga9aUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFMU7IjCjkDZU5LAXQyb4c8OUJCASsAQUepo7k5FGKE_JBf94mqZeU_tS5Wa6U1MUa4ewyqrdjm6gS2nmKEUGxgfa6LSfpIu1hfV5vjgjbfCO094PV6Q4vm3ff3kqitM3j5lZOyoQpAPHfTCvKLLUZoNaeZAnuywuP_fgAvG83QHCCN2FO-ik-r-RcofpsdNuvX1BXZNnR-x-K1or2jQf_oYI82Gi_aWBmR10beThwh-pnUdXAxA9Sa88Q8kO6x8D3xuhWE2zG8wQs-3PHwQ0y8KtncQWjaGhEZ8or09tuQfv4sIRiSt8-XiGi83ixyTIVCUU4s1CXWQl8GHF85sWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnpR1p1-9IZ9X8i6IQLAH5w3bD35KT9DnKmBRUAy4RP_F70lkh1eYvrbW05-0emcsCQELPaVf0D52_regVIJ3w8brm6LPk_eKuIMu44kEm8TXwY0_fBkToGtkFNByLrOvMJUC-ZYRiF4_zb28IGmQ67rlcUYe7OenJDBYtF2AWYNxyiWaUPpeMHTOruHlU6r0NbkwhZaWVH2b-88ZM0H9CCu-h58RMVAEQGk9OnZfvh9YwJX5BuGp8NkCd8MV8v04QQ_h3br363n-lKcLfzk2WSGQUpbVD-2AhsMliRPrfebTGUgzbHcaVl53_qzP55hYBbbwGZF1AkHLKa-SU4Kpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf9QNBMTDJ1dVO2k40UthfQRqzS8ydVCGAztKFhLbnLS3fvO3jPsmUOZw6bgQo3ABRkL4juvkXIrI2EFnRsl54rbbBuHRFFPBbDbt1Klp5gAm_-gTMOWowYgBFHM7MU9DcHpNBu52rZqdfiNxbBpn0DjIJ52JbWGxXYAaGvNhj-dREk09yoyIGZmstOwKZ5Bmo7mlFa-e7CKczdauVysXTGPxedu1lVC2Wqi2ob2v9IoBQYk2Znr9zoFrzwF9fc-mrxIkAjxlZLqRP_r3i1yQPnn-YN0rheuhClSWadiYYEQULTkxuB4YlFPOddNbo8kNEPo1jzp6jdV963zlsaJtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOZkdDNvcIAnRCUeJIi4t1FJYN7QRPht_59xJ02PG8BllmFGaGlRTqMpUiE36z9Rbl6EoOUhqrMJEfzOqXzn2bx2sIqdWTqICwuVt3fXFN8ppZaxbuWWgXGMgL4tW3rlMfjR42klLoLzp31bjQtybfDopffx1itDJdtRhusLzgNpzj17996frvVmxxgNBX4rVll1R0NC9tsxxe76On5L6jrnNSFnYoHtWu32GDcWtJq9xrdeUNF9xwFtzIcESSK-z_OaR3mhSjNwdcfpom9tN7yeizH8z3uK7_BUwfZTWRgj5P0YKar8UdT7nNy-yaaj3OMGhA9mzK2o6UDmbTfgUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1m3wRrqVfF83uVF5uPguV8wjv6rf74Vrlls6JKuvnb222g_zD2721iYHCm_rv-O4ZDTRJ9qj66fgqLa0XVOkBZdlxjoWd9Sa0Bg_aQJhIcKl0d-hu_nz8EGgxshKjBUOqFSvl0LoN-sZbMwlhwatFaXTP_3JkGVUHkHsLyfh2bzWh4Cs8oNKeSw-k9iuG5PbiX8mYyQoDYu41A2tHd4zchtW8i29O_RrGrJ-t4ZSBjg0N2S1XNPnUKtzu3tN5puRxO0FFRB82em7pMwXj_mBTAvPkPQ7uqTk_ZjHYySH_4lYjjs2UTSVGsMXVVabylcBMFXKqoYCFtrgZJoJOYkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leAJAdWBmgkAX6_xrz7Ed-PfStiiemCLFK3tME5L5NZQHYL56A234ODllhDZbCGeFcOtnA5yn7Dd-IYhuubFOmBg4PPp1c11u3cBUFUXnGzBDzGO2uTPvhlsCjFmvKK8AUQVpFURCP8wajnwcbXSQcx18GNBlnCbFheLPmMU4yBoqjQd0ZD_5uqYhTs2LJbnMwFFu16NCh3ir-dobpaYjfcw3-P9uJ0qnEpGDTz-CdGLmBq5syNP3Tq92ujGP0qZ75UboBo90ZLihJv6VstDmOh9fvE_II1iU0pa46K3vatbNhIfOdAKWcOcgdgKOhClarp_Hq2H5SwLRa2kGojz7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5_MppOag8bEB4xIkCXYhubtyJ4Th-0fruJXW8Ekjt3WIIEhxxvFSeTj0TnqZ4-hCxDYwSFamg2kvKwzrTob5kj1lwQF7FkRpSdJ-MommWsm46zAywtoLm5OwTLlzzJrKYeBgCxwyz5loql_lzyJ2-mtRja7cuQ7uhGQRvn1BaR6vnvYuJUhTA3WHzIWM8auXZVUIjB2wtbc9dg3xtM8yCewYL-7UTb7soZ5b_EeoXPXOJX74vdLY-SQXjl19uwZVNEi8vqPL6G-ellUMBhbWMgR1Oi-p5-c8slM6SHcqsLoO3KwjBr_O5fpaPLdUdZpswLLVtxcneIWkvebhLHR6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0o1BQdAVMlhhAy7mDg0K2hdfAzHW_HKaIzYDgGMWQ8SM-a0A37s85sSM2kBvsf9MM7JQ4q_TnWyEAOYNiJA474e0c9oxXto1-RIBo3W--hIXllsfeKp39pzt9l9-dY51aNHYQSbUIH3YYW-IvnmV90a4liolpn29MPDO6NvRTgi-0-pUWuSnD1z9BhUbJ1ShHR19MmBR51ERkLiIleL_I_ogId_JQzl4Fyuqo_wn3ekGZ_NBVTKk4NgI9ZTgEMCE4mY9QGwTBvbzCdd0RDDwovoy_3pvzZpUmsubS2dS3dw1dLjTA2bkfbWArMO-tC-h3ZuJtPeXWEneD5xC9u8AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMTqUXGPgVp5b8keUOrJw-W0JulScDEYBMki0MPidnASJIb_fDa8eT0um-kLR5kqq6mwCwoySTYGRoDDO6QOYOdj7H5nkphDiMow312fS_HuLklvYOdlFP6gJUIpuy8doepe-wy8jP-C8EqLJEj3-W-b4zmWMM__-Uk58iV9fiF2myk0Dvn3iG5bAJfz8B18xrjg6cnlWttwqmm7dQyNd7VV0G-Pocm05BHpzrGI5CckwpsyaSDd7NMazMdRjoKDmXy8trwWweBPa3F1HLqT_WN4j1yKcxlrcDMGS4NrYyPOsCFhXN6gXVRCDe_cRTySyiIuQD1fKMK6Lc9ctxFBug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaC_8fgOdImLvg5UGCkLBz2JwhuhjRFHZssX90pOC3MmndnxkWKF3AEWK-bG-SPF99MSnbwQUvRueCNFMB2prHJeljNKZDEZZKg27RZQBo_5YicsKM6_mynu68eL2jw7PJEB9YN77cWPXCIX18CBDp4muBfiBusydX-XDcD3FlpHy02x00E62ovBZKL-ccbhsNbUHJ7A5_zophNQZvBGhU360JHK4pbl7LNdPYTw6aNt2ONVv6DqabBUlH7Qbc9VkVBBITy0geijf89fj7OgITG9HX7ItOT-WwDae1bAqZW0c08fsqQgfj6NmgpUvgHdHgL3lOp253mKKOxgFKZ3Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YODjn5k4TWnLKuOaU4k7wLW0N05NCUyhYXoDgj20dlhqLDJnZ3bvmC5M5_AgyDaggcD-lX4P_HD-CLL4jmtKKCxIIoKWiWU0rCUvpaEGc0vSFtwA-2LyzSoc6C27D9t3gzhHcYNLfkU-RC3tJzRUpwdwpHfYcSZ21TD8DFk9E7vr7r9oUF0GENkLTuG8hvBEmGadHmNV1qYkNDO7EDaWtn0fnP8f5befn-Sv3b-ChFO1XIOT4SkqgXlGE9p0PXlhIEuzHjsar18S80pAE0UCy5tiugPTaE_l3DnA9FMXT7I7-C0_q3qLzeggRMjaExyZhi_cix4NP-TIYy7VlALSAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSrH72zNnwqtaH6KOmtQHco3DgCEvZXv4e3ixrxXmxgaN-eoWiedGgWQQ9jh1t7n9hd-bN552o1twU5Kz3VQyICZefRov7B_2R8YwpTA8PDR51wVyM2BcivLRWzkhbukZWm3-DOlk5jBwh-1k58nviUPYRY6FipGxaRyyC9HMq1N0Cyfi61-Dor83GA9UF10mi0BQzw_lZVq1r11XwfgUu-QW0fn9xXRveSYVuHjwPebTuTsBhMvA_C6BEC2JZIAGUwXhn6SZpCm9QyDS1qvVB9WnuM27idmKkZ3TK6kzzJvxNnXsrwZYfkkbIIirOUXkDS4HpiYR5av_2oPrZVDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clf6lp3x7XC-ytRh8yE54og4Kvx4tDHg9gKiLkxwgVpaDz7ApxB03vzBxY-07zadAlTZoj5Xax7x4JtncULyxvBznXYaakRK0bWNsT4wvMqkRX_WHLOr6q1l5aQi_wsPxq8nm1z7Tp-A-LZZbd9eT7i_Zuk1GPFBRKIMbtQIr-pRHmBVOkHdxlIBGU3rVEVRBfasdYqRhwKkblq-R0hYii7OeL_bF24llajONIN3iliiKJqPBZF-8yfZL-XQViYMNtw4JMwwst2PwpwTC0EhEVWmd7NZfXPOWFKCMIBDmMu12gHbRdr5H5JlQOBQ4sfQeoy1TsnbVo3a9SYU8UugAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qhOg-uytYklWghqkrIxzfbq0YoqcrQy1LvMtmFoQbaUCzsJ6b_qEH0tlu1VRBlO-ZI2pUt9SpCWVP_ZrkSkHrrxo2m6pXgYis2woY_2WTCH0OmgNsxmPFXLP24lvv7ZXtoFTS-3YfeqBs7zIwqHSWm6c7EzodcnbN0L_x7lXccKvXspGdss_B01kC4jTY9K08GclY_Cv4-msDkdyQZEgnBBr8nXk67f7WMmS3-bOkbcS2FramTMQji2I7Bf6ej57ujQT_tgXOhRW4V93aveRa3xHop8K68tuFXpsZbYLX6BGZWjvcNS05c-ORM5uGyp_WdNLGtsozP-rulW6zrSCnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X91kQevp4t-NW9BB8uGhFGNvAqyFE1OlI4L0DZ8CUsX-e_3NPKJdoiaqtxNJ7lbhZCo6lK4UBo4jytzMD_Wm3Nkx3YPX6NAFAbZc5cZNFkn897MlthyfnnHjv_R2tSlyH9_7VUkdBelS99mnAiWpWccaF9rl5_UGVtHvXIsWaJaaaiEnZYSRgw0vpM9NSG6GUtiCoI4ex5koRFNgHzGeIPdcnIpSnlRYFaI1GnOZ8iZfTRKO7MsK7Q27SIVnSOlBWEsOqb0lF6VCSeaSpf0GNFjfD3UPnCxYXJFvzd2IRQXvf02hAzt2Q6zfCH6Q2MguJQfPNiNBcrAGKH1BWli6Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2y3x18AN0kurD1dOOubw2gdiYVUaRDcRrBfWXyNRCVjwQptaa0UKF6Lot5Epaw1aH6uZVrNo2P8wNEd7vR7DIEQThUG2Wy_3j7VZrsyhJEWQtQAtiAgxXhpM_A-H-f3QWTTZuRoZM7d_IctZLumZzA-mJ5Nv2V8qw0ETsHpvVSsb6e3fYJQKLQqtn0h_0h8mgMK0WDXUbsHpLrbr2zbrEuITt6FVMHk6fYu1xskPiILbtZgSXqEfbXXY63HVRu_EbBYEfGh2H07hVBxlPsYzaR847efbz3DbXDeciRN4brt58Ci9vENtj-ogClbnQxkWSVF8Q6bNprgEgaJ06ImzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5Byn1VR-4hFJF_e4CmHXxlFU5ttPKHxWaYwqv4zJvh6OqsKhRDf_n2UTlR5F3kBji78oI01m9eRK9uweIfPOHgcMKQuHaXWiDC8xQVpJN-64VaTXN-v7GLkrqjcHELovi-wueBYfXBX7L40v5udsaU_i80l9KRgv4bL_kqY89Jjf6KBEQnGpE2-ho3BlDiWrxo9io6bXCVLUzbcZYEiF3NsR6Utx60h1zGhQ_LbnTznbP0iryvAs_PVgOtUHgr4JJIDfKn4hsrUmELETGW0Ce3Wn_9jv1N6DuRXXRLbYAL7dTRhH_rRwGUv6LiG_VtaUXtPS0sShViWBEs5fPkRxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 589 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOUW2Aa754ql5uCC7xzKUYr2Ko9ZdtFUAGWNpHD_DqQlynlKTUlFoE8LQ9q5bT_fKejhFDR6_Xstzb_D9shX1tduHJhdVdcgo2DrseLXo4xum8nY5e9mWPof_4hu31VJsgK-cLQAPhkhBp9crHlTkuE6FldD2RTMHLI0csrN4M6-ZsfWE9V9cpk1ycYwJk1CSYnb2C1r61Fsjf6121HVJgc8jj9ey_lIQvxkIJu6V-2OjOVHqWxmN9tRrlCFwlN1jEokGt6wYZYrSAgxpgI54ZJ7l-REIAacnmIXJtjL3cxeBupF56WyL-ZdrFgq3UKvr3W6m0FixZxk4t0Qac5apA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqBHiKHwUO9wZwnhV0oYMK-QtyLk4IY30DRuO4u_MEh3T2AfnROMdy21sHbiPSdOHdeFiJRawepOwgSSethf81ym2V2EQnpsHVVbkm6KfKHL6JgimRYW-C3LiMn62gkPZgBosIwoVj4XPPzOX5qxrsgOwk2BEMGV1ADvedLW17TduW2a4BibDwK24gACK3UoV5NOl2eER0nnO8ficg0z7IA3VqkY1M-G7xO9nCrSiPv1jP7A3qPBwbRG11nWy-Iss9gVsGtmaE3aAM8Okg5rcFjMMYldmiqrxXE57nHLYnqNKWn2HBypqbvLVxN1nRFWI5DN8fnmjfZwZyt5hAEQBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 644 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFGk03xFy0sOr_Xkymwb6-HZWtlEhZnWNxauFBJ1ujFkTMR2lYuAP46rOaB1J6yH9kSqO33MwptpoGMTc3a-XS2xIzlQEMaXScULZbPnXTCQE8CazpUI64aZHTD5d8W4QHn7TAAp0Cis98jkrDV7drJwVOI2R2G609zKVIaJxKGNGl59qFSigsCRX_1qObPUiCgw9VDCIspTjzDGalm5tE5uqgzFOdp3_nEdbzenJZ8Dz-ONRLLZ7UlCMi9Gs119ZZltshseRHbt4zrnQFchiDQesgpNppzmrrEOdlAqDXQVHxM_vzW0qj1tPtrAcF_opDScMfUIdcesEvkIt7PXWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS9gN-AbwyARsP3gQzaF4hYwFGmphMlkecyAkbP6IDla_rwqsxLw9vllT_M6y6FVFR5putQMQ3neU5iLUdqnUfXQYUooFlBVHDezJUTZNweQulz6doKBik23U_v2xMchVREfhSyPHbdcnru40oLoEtHTtA7w0rBy7G6CL6sG4MI1Kesj9VQFHzT5UXUW2XtaB2VeopfQMlB-34ExS2XfNgwB6vea50i788hPOaRwcrZoUSSDfSt8bj-YU1hQiZiVoq-mj46YO3SS4ReR5bCrfg8lHoiEmPQNt-YjWs14E3WQO-sueQ6saqgfXjGIZ3wWROmuCbYn4RUlwf7oLpTUsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpzyyXze40oS7038N2ATeWmUZAaYyK9EbvtXPuqp9MdGEttLwQaf1aImXvcuWeZxm4UH9zVI44PcynwU5NTgh1sh5qt6b2M9bYmZ7gDTjfA9CsWV6IZsEWevv48g9It2Y3p72lTqI8nzez_Plv3Ec2iE-CEGbcNMYRRkjQOxsvgltYU5IqJL5_aXcmHwUqFTaLgFYkfQDY_K1KsZ7cZFfkaNOZteHVOi1Ak1c3rAj3NQIuTqBHKHLqgv8NIx_qohNcDxxYmPjv53RbZa-cKJC6jt4oICnEwo_rRhsTyj7ngmPGBLs6Z1MiypOT6s_a2GP3-M3EbAOgOlfv-R4NQ21Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGq-W6-ZRQ8wXyW5HPI4VUDE5sTW7PQPmfgqKdKciSHEyIH28wuzWv7mM5ctwhUT0O3Y7U16aZ_kp6fwnZLrSduCk-FC6MedzH0PzpdyJEaOTKxQ3dmb3LWRS1g1VW5DE8eMibxbovKnNqgEKxlwV9C-U76txkhMxZuB2d_NRxGnqUfTkkc82eiYgFFs3fAYunq8Xjs-q3eDmYvvndPK19sGy8Gp6_e7t3PZhqYo1bYybGE3fAZWQok8P2FbWHhDmgTotrR29mprXqPWTu-ld_uI5RJ8sRGfhR1rPVKqfZcE2lNxDEsDb1oyzptW_N6zDHafntMjTyAgJBZmmMuwXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXjo3qTh2XXhJ5r4S6zRLiZsfaGEkyt0qTafBXeuV0qW4P63NV0p0HeTTa0J-QXc1FRTkM6N38F1eSU0yzTQip_lruVZlqrPFlOIqA_4RITI_r6A3pqtk0smktRh-MvLlvADZ1e41zcsQtz1yQJHzuGJqZuwBrnByJaU2qm-fvt47HIr7eUTow61Ie0AGirm0gBzlTiRqmjCURxTlM1VKL_36kLJlZWpYfBmCVj2U7s-L9OmCrEZUXs8JQxfcv56Rd9uI33kmkN71_4LR9O3RCZB7RJMvqwLI0GJuFVsJyFhmhVHDYuwVYBPUUCbtRZBQg4McZzyeynLjDFGWl30tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_eSsm9q0fLM9NC_r1hpUy_nck68Ek8h20mQ8gCaWfBGiydkoeDdPZfkCaMz7me7hS2Ap6fzzCQX1IQ5za4JJL3fLQ9ImVNXQZDngF9GqITgd0bAvZp3QwIynOySL-P0B-_sk-l9S7H-OqEnYisBOtoaArsVx9aZ_e7CRwJRz5CE_p_l-r2s2esaEbuMCQTlKq6JA0YTcZ0NTBoI4ZsnuwZ1yzLdqsj7efHsI5srPkaSoJyNvWcoAtfAevG1rPX-QxsfDrf4pWU0BiP7kiw6zqeQ6Uk84Zw5Fikr_OVtn9dfLmjnAN8Jv8n_KKcav31BRT-CxYxJFQ97ks0SpabAQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-a7MXfpTzQNgIFoHz7y9jwkWM7Xly_-2x8WZxr-7u2b05yxM1f2KFTk-4osiGFQnGqvD26nRAPNKHCExqwZh_BErHfB_1IadA1t6rzl3o5C4gkbEUkCuUkUeg6j2g-SGw6gYHJtLlw_SnsqOLVlXr51wzZG5b2Xr2i3iVYegUJQC2EvNPZLPZMyV5hHv99s03FeXjrpQEISpxico9slfDqJRD36Q3TIUxm1-uuB4qyS1epefhHdF_ZYeGyNle2_5poaOQEeuHGNaJczWTlkt3XrE6V0On0N_YSgmD3aeIFKG8_a4PsHymaA6tJuP78wCUReZKONcKVeL3yGZ_pVpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT0eetC5mNZwTJLjztXnijRz1l9V-gy7AeADQ9vvxmoXfgDsr4_w4Ro-BGDs5NSGls5EE4OhAMbcIx6MG39kp28ZnJh22t4WeDn9ehfuQlLYmkH-0-YAwM2xNIXzMZTaQdw9wm-rxNcefY7lLxhuyC7svgRCpzKCO3fEiUDP2GobWUNM-z2UfWVP9VOEPfjgj0rphAqpujAzaTftWMH4U93-H2LHsjaYm9lxXxiruLiYO45MQd_Clq6RCYO9niS2kiUtZOYE9c1Utu3zUu9A01FSuKT2GD6OQ_qiJxwbO7TSwOXxSIl_ibXiqRW_CC2k9uHop3VZ0CHHvHfxag5Jog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sS-EkF4AE__4TTHJyvNLwFW2GKav-2vo_di-XC_ulshjAePPKmRXdDGFPaP9dmcIa7u-bZt7QnNH4Ywv2J0BOFkHAmcaIEyexDuGcrEhce5mEYtaDzP9SCFB-yliXTfQ7C3H1-prU0BvOnWuzcdCUoRAptHTaY5Rxeu7A50WGclPwp57HUNtz6kgRHUuQg3sKT6mySt4sblpDPRC443uy7SuKoxJ-fKxcjvYWXjyLI8eObPYQFiHTC0k2Vr4KPze9YPQJ8b_ViYtky_61-uMnvMirsQ5LFUZwvQw8255N1pf1cMrygyhQQDIdinT_uDZvrwlatz4Skv7c63l6VFRaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffmMTStFj6EQ_Z_Cn6ElH33yg2EhlMzy71adHUA1Edisdqztd7Ubz8PcDjJAl4mOjbCsZBqZbWlfiOQdb1KZ-7eMiMXoBU0YFfqo1auFUHU-V5-tT-pgL7cesuf8Gj0yZmJMtSPFt6GSrguyhZcXB_nL1kVXDtGGApQfAtXzcH5wj5zNEeUSX7ua6eb8VRlHLvtzQYsEhkXkDqlngOISd68wEzxKwuxJJoWxUbVM8u4-g9yx0F68f2HaZarPxtD9Wn4WqpoRQClRWeaoX99GQEh5p2je1_aLoval5PY1OYUJJYIbFm9B-IMclnthHDE1ITUIm0QSIW2xn6SSUs9deA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mcnoMTNBxTeJb0pfudV7GGzBb6i_3r7SjFAebWl4Q68XjEoESM-vuT0H06YPO39PtAmTZo8kHQz7YKBTsHMmFOJwT2BchqB6KzkF8gDS76KbuZHki4jYuLz14GKRAyKXM7TL7QMph_oPdfhYmsW2YUqyqIddar1LlAT9SDWvG8wxlwrm-mismW2hr8PxcsIYz6n4gUcmhDX5IjcNWkoxS8VbwCWLQP4dBUHNikaDg0q9FvrgflHEbl6V8-dOoY2zxNjt6ED6333VTQRmngBIGOnt2dke5pnpoE58KFqwr61zr_29nJXF1L-U138cah9Qg0k-bSp_yWMcmSye3isgkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjIjdpnvcOiRE08tr2OuadXyLDUfuJ5NdlSX2M8Mjqw3yeVvU-Ejiybam4DoDCFMT6jhhrEXPUkfbc5gPTdcNc2PAmscvPGTJnXRNaSfVjBtUauCAQEdbuqSSSAQ2hzaMaSjsqrs9FT0IJnOrey3Nfs4YvtsW_8TOgACE-4aj80W3JKCRLxrORyn2wyRcBkJI6RUGsgztUKV87uKfHKkBziXfk7HNLoSvXEy_4b4_O72eb5D7Kve7KF_R7YDKR6Zlk5FzhnIxSurp2AcWjPomA9Jef_9NhmRIm06ui-MMmzNY7I9QLFpZpXr89AvTPsRoNivw1oT2fg8rZ9JpM3gWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFgbL4hv9_Dmk3IbpzK6xm4BM8BPRjl3BSwmuGguZvFK1kAGll8Hku3wSuZDEj2Xx7D79FDN3jiDlWR-jRxE75S8tDJKn1jpacGShoZJFRsjAlWRyF_VTQBjWcWAnO0GW3wz2VcprN7G41E3A5rhjgz9u66ioZCH6c-fRLQGRa2G7QTJ6Wt6M3e8Z8Lua4twvhafjohYO5ZZSPhEEexxD3Pruq8johTYozb7Pwdg-i7lQraEbvZBaiVKEKP7Kc7lMh1JgmJyGRNDf5BpZVqL4YJ1YwMIHcTXTiX1GeHBfz9z0Ef-Lf_q9ZJgacZw7qcPEvysFL1jqyhIkq9c7UAg_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXepK9nTlGwzoocfb0-WnWxNsq4cg5Ou51y9QlvfWaw6PzWXt8T5E55ugCSyG3e2Dpg5jGnUXCOZ_VXj59vTt4SAeU5C6HwPof0FGR84wcSycl8s3em5r53AimYIlw19BjgUVUmUIcQ0jIyHJ3gj6siT1T9nHvp12m5wfGxFWlkRkquilArylzzukPzFfopqg8ZCGR5qMefHx6z93OIbNeXlJCUotzR1CkDUG1Vn7jShWJSH_bshalAQJWawuroBfnf8xdXNsGqoEmWersqFzOFwuRA3XP3phJtLGmCzJ3pqhVw20S2D0E74C_pSYH-yZ35c0ECnd6Syio_pDNt17g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3RZAh9CX-2Ahm0CKPvvbaq1fRH4YGqFgwBH0Fg25OaIXhbQT8rqS8aj6nZ0gsJWPRwORzTpN8nhPE_QeXMNbEP5_a4pnphf-_pAUwHr0bMqeU4sS0JTl2a13tbsH11TTmrXR1kQ6eWukj-O9tTkR-ZMUKoBHTmrMpkxxG7HLtVjaSmtYwuQ9QEVFtlg6sqqykAR4uX3ih5EgGLHsavkSyEJumKWT7fdeEA3fLHfI5AIHFF_JzUbZy4qCwjL4S8j5Gj0IRWGe10Wt-ErkzF6t3b51XPj5ZInKekd8bGRk2sWzUZqiDlYqhiTAku7KQoiX2cqA373tDyaVtL74RAb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ku6SCvKiZNPOQJhC3OTx9arZyd3mhkWPYpIe59-lIw-PzCHuJdNkplWwAu_zV7zROjWn5eK0tH77h9MwUXG-nFbsK_MqaA07IYuC34KFk8T47Sukq1NphzaFHYDEOfLfAmyLjmtSplJ1rnPAzUYCFXbF_otz4_MPUmx_ttKYW8CmfIIVkI4b20eDEPCTKXD1UxN_mah7jQBCYOdxhBoesyLmtMroW_S8FJjj5Iq5gtEsKf7EeUm2OAqooE26N4MNMs3IV4eNdcfBDmdi4BJEd1XkAqI2BxNd95-cN2ZE75KjUgZSQ2fsZvKVMjJtelTLMp_PevQyHGCemhhXEOHBHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWzUGnUm9uMyjF2FhBtpQCpm7L1uHg_BIh_DLZsfHQx_arYwDwpIhhlGjDJcdweReFOCt8HuyHi7sJIV9p4gprYLXpuYHcrtaI-18OdXSzbpJHq8SIL30es3UCEAjQV3Cs-QAMBLsFPRteuz_99p5J9DUF0_B7IADGXZuEUyYYrugFRjEW14H38EA8seA5vPVID4eOflyayTYwHIiEnuZGXzs7kqW8mbtsh-gT9KrC7FuxD57BUwQd_DPES7ajliGapP-J-EhlZHzV0GPvNb2z3l6xDF8G_GL5wQhg8c0n0juc7ZKeOQaKo8ODrpXwiXdPeBHthUAL8V8ZgcQAmrRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2OahigDNxEBRsQK8o8RzykNqJoDUkMAFpu2DSDN0QcmT1tC5owq13Chw6qsFFvhFWdm4_rzfW61VmLBrDwr5h8NHpzRE6ed3yDBOhA_yO0NOPI9efuUQ_0Jd2LTJvSkhhRaWoxVJhuxKiBs2x_SAN1decfXcPErzznN3URNA19LNnwDKjKMFKuDcBl6qT8ruR4PMjsIvnHHrGpXY4AS87RO9fCp-t4NXKE608qupz2eToK3DClroL68gtk0WqfA8lqQMeL-q5JToJsYjvDI-7Sqn-0JGNCfzudRqu9WxaCcLRAeSJRGIb3qQdUJtBn7dYRHOqxPs6tkdMnLUXtwog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2Qvf_GuZl6ecziDiyRmdUdBg06b80jqWg7dlRbNlhWuljbthFfhwtPszj5rHM83ci4yc79DuDdK5AblwaD79-5qKCH9mxigCJtW9hH2_yQRrMFMeG31vwKldWMFRXyhC0RLEn2lDb0ijgk-rTYUcdkSMqg4pEb8I014k88xrPNDeN7N5_awf2OwkQ3a_QPe3-stIv9GUJ_TQZmW4T8EKGWSBaieIL_xH2N7GuqrRnVQaYidBfHH3LKytVDtRpzsz9Et5_HjIc_VEntfLG3zuskJc6bf3zSabUsV-0ttJ9EEiRbMsZEUS55E5JkNz2eACdbZUSeMgYpKYKZBMpNSkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4mYPHILVsMxBiJc8cd1H7_AGKaZ0DURUPOTuE8GTDgVXBfvpDtsbiVIFWld93gQdaNUqst31ZR18bmeeiQWU3ND7k13QkOJhWRQlm5OimIPZl7xK3KKeJIDIHLqntM544TpmRs5Xr7Zd1cFsZ0h77K_bg3cHlT6bdgbCPm8ZmmNEVkhBY754SeIakhniqhZb45YUGPFj8ZXYsgTuVH79XwbCjv--fL5m6aBCOqbhiRNLhoLS97PE47yqQsnwDa6JfKaezT9OKxs_XmSF_B5JukVgqWydpwEGxyOHRMwI9z08Lpcf-kGhzHe-b6p6_cYYITr2Vs70wRXNc3GH-MIsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1VHXWSyRYtBe63tVboH58v7lhksV6e8bUYaQYazT_Fa_GYEivd-A3FnkW1aoYnyNwbdytihHDUookL5eE3bMM3vEGE1eqRij9lEagp-1u3eQlKUN0NoUqlcHUsf-Shty0e5n407sf33Y4qB0ynas1Q7TKRgLAEzGKV8T0b6Jmf-wbmTFdBDoeVnBzLE7hOrZOF_28xYaPgReOEkN53lA4MP5Inz3NJ_Kd306C3NppGTc0TYic83vzFU3aMcLHuxRU1lDa5TePCs1Asp_3AJWWXl_yQB0JGo0eldqwRH9PLEzXJa_rfSnOmwVhGH9TXf28bXw3jNU1RCv_M1y44mHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb6bmfGaum6D7_iTQc4z_d9_za-U1R7btmXMGRN2KLlbJLpEgwYWiHRycvmHdARNQ2Rb4XCaSgEB8p34OWgo8D868O4sr34j1fNq9wucVpgs99pTIm0boA-CWQu3iLlnZptHe0b_wnuV6AEvi2NO17aFQBXXvMr9432bYvw2E6Ufwg8VfBnS57kMMQxKrl2_LNiIFZ5RlnVzohOXSy9pyJFthBSUGIkD4qUhFBr5FGWTdRuneJNJCX7duQTYF4xgzOqRjdqfiuOJxjT_-ZG4nKS_8uEgXm9nxtnOADzE-C1qtqFqlKOn4bg3nSw1sAqNnjt2L4Gf2iAGEYnQfBKkmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7ARoVuz-bdLJ9mwGnHVEjlIqa_Ln8iGJz1ibZTqm5pKuw9P4ykg8cyngdhN-u_Qncb-vzWGXvaQH2dr1BrZOhvSoYSmChK0GOfX0Yd3TofkJcm-FcDEnvu2icspMOFGz0uc5esIoCuG-bbbC7wQ5sjXGlGz6a1AkIG4_87kyiYz75lJwAI_cqzZFdi1v9rsUE78lmpvJn1v2T27kEDk2Go-O2OMghLLvQ8n12CekSSfwzsFdXjEfjk3_rA9Z4wL6OOciQ2EIQh9xk6N7KxHu2taK_D32-D8uGxMVfUs74pW4oCbbqTcDLPd_CZ803NM2QScV1igaAwXmUhogNoIzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSpn7W3JLjTjdjb-aPrFyto8O0oLEclkPgzAkJisnCfsTT9x3TgtNqNoCoc657Dlhsa5rrpKRRcCVj2AfvHFMKR2axfr8ojN-e09bF36nym80aqOftMWFPzNXqHsN9k6njGg3vc3skltPLlyuH7soCVxOnDWAFUs02T02uVG-8zyTPGEPFW86Qwg9RT9P5nI0RJUmvxo9kXVM4oJYwbk8Bof8jKf_AskK6CEJpOW43tgLtlhY4FMbgXnRUvouAPyOq8PCoaAkhfITgyErn0Wc3jItI6El68tnPepiySeNaduxFxi0upggDEY8NbT6tqJy2e211qUKvCK01OUtW74hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 656 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2XjXbNr4GW4Zv3fd276aKnljXWTVKPbQsnQaYZCw1ae3WD2aTvj7Ryq1YgQUhnw_mFIMLmHeCKim9CO_xw1Xl2oJg9AdSIHeBTdKoqBtoaoQ0QNGN9kCYSK05Or3UWQE50lhUfGcGw_QhSXSOhNmx49Yai6Yfd_k0ZPr78tIc6yRbhPe4NJs0zrhoEhJ7C3kJz6G97wjkQJXjnakc4tDSQrEobtErqv_tqZXWj9f840QWAduOjJvyGsIbLPidR89Nk9SIEPewfOeJPQ5ZamC27Yu5DLcq4JD7djjo948ETBXXevtqX6zgG9aTByPMwBbuYofwS5MPOoxei8VSFyAQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Fqc0Vkb7kxwvS6QN-DVdmELy56ScuL1t0ViYoFGtTo8vXWjFasDAwyViPI5YG1irYcCy9htM4zddrjFVipwvoBdamL6GzfV_u6tosf7-ZsoiANST6snuxOd0BhaorOLn6wYXv34xwRAiFJS60GJS-Xlg4XNBN9gHxvyovDDzQ2g8bfP27vnfEPVSXHlYRQ4cy70a6CpOLIxeyfomHkGc-pGRJo_P-VGxNUPul2s3AOtDg_XGlltiKjCTnmHYApEcbczTteOJJFM_kKAl3XTSljYTeNtgMnoGzU32H0uc_2bVfiGYag6gl7POd0q7CMT_MfcmRhMOSOjS4ZoapNh8Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Fqc0Vkb7kxwvS6QN-DVdmELy56ScuL1t0ViYoFGtTo8vXWjFasDAwyViPI5YG1irYcCy9htM4zddrjFVipwvoBdamL6GzfV_u6tosf7-ZsoiANST6snuxOd0BhaorOLn6wYXv34xwRAiFJS60GJS-Xlg4XNBN9gHxvyovDDzQ2g8bfP27vnfEPVSXHlYRQ4cy70a6CpOLIxeyfomHkGc-pGRJo_P-VGxNUPul2s3AOtDg_XGlltiKjCTnmHYApEcbczTteOJJFM_kKAl3XTSljYTeNtgMnoGzU32H0uc_2bVfiGYag6gl7POd0q7CMT_MfcmRhMOSOjS4ZoapNh8Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceHsJdKdpnRC2KP0gHoZb2T6jpziJpC2RojJUI5A94Sv520B84irbe9wvMQRcy2grHI1zj3SDQnhTZgVuKPxsNoeSu89F4rzYzJiOhNWnlHUMfqpgro04BGn6OPvobM1m8fXLLjfz51NbNO_mfOCoeZqRuUR_55msGlWKVnW94YMP7QyBzKpXb7yOOwvNDd-zOOfaW6OGX60PSJJ0ldz7orbET5y3_f0bAa5TbvL56k5YzwlDXh4V-QX7uF4ilcxVsScXhsqerWQ19EoKw0aUXvtJQycBuM9XVlw9XNcJW412mMaIOevpY2gnTmHqns9ui9uBLGAiB9QVJxUglyJPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MS1qJk7c4pSW9DxR-ruWoMD0WY7WGfO6y2U_Pzg_ZtImYovj_5zsHUQMdt7LgYmGsC2F0niXE52f43hOO-sSWCN_sZIic_GiQohI6p-mcOC0IOqAk_vQS8YoXNTZRTp_6Om2zFa_3FWPCRar1HWIc4Z930mxu981SUGmZhcqR6VMUl345EB5uTEu1vi3qPJPzqz721nEGuEgyEIZxnWGLgcF0RQY1YEA23tbdt87CXnHTPgS3RnTzzXBB4v84Easu5Pvyc6TS-x3pn_d2xQaElUix_UeAOrVZjcribfZe3MA47qYdm8L8Qs5VI0VZGX77H_Qo1beCI95pcbPhJJozw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRfHHAJQo80rquS4hMQoi5qAsnzdB9mRkA8g2bvIVP0xkta0hDJYb47qz_xaG7BrmI51HxBTS6j65HFT7OT-rt6q-2QRaH0CrHyiiY3xtNmpsVRdkBln9l0haXNnnSy-E2Pk34Fwws5bDVMBTiELqtH6JFzP4YKEt04pXaKbQOchQ7irWlt2mHnlch1SPLS0OAN6Ki-eUOv3dRF0wFW4KKNtoYbsEqe3sRvqR0XukSdGj0O3qnMWxDAh9TL2rQtuts680MLl8F3OlraUjADQtZ0X4RRtAy7NBhQXkQ616tYEoPYuUyerZyZOeHZeM4bTVlqSm8OWF0GeRTuMKdv50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ge6b6B_XIEUGlmNUV7wpMa06EwTxsdY_iL31voRg_BdtbMn_1iSfFDOI_pTRJDe-3bXVboWxyURhkncptkf-aCLPkmDseQdm9TiMsrO6OLLRU-teN7O_ig21VEbVN9oQT8DTCmbKMKJkijWNYncC5VqN3SrYJ7A8Klx7r3fr9jYFFM41gmwidHPeAqFUh8RmEJzA_lrXpM7euej14GWPERfjP0AN4MFwi-pzAX86FYSUv6pBIaeXQBIKyE2-UmOxvxsYQM23HpuWAj1UL6pD4Tluw6CiDR7kEssfJMpkclC4ZfYHkmcrScsIqlS_oKSOCHaLM2zuUQiLlOG27S60CA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYUD8VX31Gg-XFddikd3pBEiFwPoS714HTbCOPNATEqtDhc3Qr7NI0QRp28LC598m5lHeEZmXvM6wnYOhuNKbwreAKSEeUkAXYZgyOwMrQRJ0K0hHl1Jcfz1uVWfnFlgYwIgtnyBg_2fMh7ebxT_hxgBZ5gdQZgfYahe0ktiETapt0THeMRcglR-WX6EwlkaE-7JqQ9stk0w2FxH_oTkuzR0OKw7e_53cWHRYce5L89bs58iEab0RlKjFTwUDEjXU-BqJj-C2WHers6-mfxtSlIJDNYgMmkN68FQwtHiojeJB4alseW8Iy49fwDlrFmtnTNpAeZAu5cVAbgj09pCYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HDo5FdX2uvCdQpom_EnJL-vN_4gQIArgKpG6HGBqmqlVGejs-zzhPICVxkLi2gp1ILiGtN4g7qFYRfC2FLeiEnz1umOws8V-2E6dj79g1K-KCiC7KLszNjM8j5yCb65fY3EWY1UX-zloxrpv4UDyYDV5wKxs6RgAnW80wYdEb1CZodWtkka_Nz57CieaKa8XK2Y6nbWYYeqeWXBrC0SfgHqp9WO7-IadH85514655vskH_PAUUZhbdq8H0yDQawUG72gsQmiH6LVHeAFilF7eYugegghky4LtdPSDb3CmTXxXsc_O_1TC2Brjvnmsrye5YEMyPbQW_F4p7Xlo6FTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uyOq7nHfhT97aGN4Z0dci1Dlib1IBIBQmyJWFKQ760Qh5v1556_kdP-_NyRYA29sy8wLFNsb0r_JoNkb9-KKVjzSueeXcGwG4yeA0ut1G10jyacsjOuHwmbSMhN1DoqFgTffuuqwWxj_frRlyYPRTsOOyuA1tT03DhFOieIcp_SCU58qiUUPraxXuYUg9VO1or1LLry4VUWBZZbzyOKN_Hb8D2gchS2Xh8NP6g8bXdUbarNL73sB0964se6LU4SlwI3xRdjPLP7D0tExkZ5xnbvajP7-3mve5PMtjRqJqaJL6kRIleFdX3e9B3gucbtRNBhtDzfToXNMDycruizu8A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=hbTrlwilfXIOevLO-LDnNwsRBmowA1VIss-yNRhnxmA7cs2Cegp4f1e73l2HtOjr4nK1BpKq_grHUxUmkIpjgQ15PF2SAi5rovrqBJ3WzFnqsrL3UoyAK9TR3QnBfXGg8Mcq6WPY4ro2gcAUHOd1kmm2AdwL3alyusJsbl84A77FTkmWgfMxNUYZ4jNF0YsnsOGAKDJt3Syx5gX8knHq_a0GWstOC2bGGguxdrC16z5G1J-PkpqlwKVyPntjT88XBXP8O0YIRWmzkjq0JBpoZkWO87MHG1XmWKJAUGSxOCsr-d7S_nIaPbPUTH14A0KHxThMBrRd7R8tN0tKWIG38GsziBW2MJuec_PO7qc0oTH0CKh8ERnAx0jGIfQzvGYNbBn9fU0zpGrDMuzdxhk7IZZTGLRaJ-fXrVArHWPwKXnjubZ6CZAWOg358iMizHac9sY07qHASjjc0F_9qYIq380jhpIudI_WEoNBaq5pSBBdGXstw4u-aG3iwyEUqU86xjmQKuoBofRVmukqF2smUrnMaHMBdXliw4vx3YmhLFj2tt0Pt9dQd_u1d-D_Jodf8gsdqt3tA5w2GvhtgUE6QgIFZSd29J0SiLtOnMj-3yn7A0ZPbxKgHWYSJLMVwOSydOkMCLP9OL2LevEfmsBkLN1KItBL3J25WCl-enh4WZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=hbTrlwilfXIOevLO-LDnNwsRBmowA1VIss-yNRhnxmA7cs2Cegp4f1e73l2HtOjr4nK1BpKq_grHUxUmkIpjgQ15PF2SAi5rovrqBJ3WzFnqsrL3UoyAK9TR3QnBfXGg8Mcq6WPY4ro2gcAUHOd1kmm2AdwL3alyusJsbl84A77FTkmWgfMxNUYZ4jNF0YsnsOGAKDJt3Syx5gX8knHq_a0GWstOC2bGGguxdrC16z5G1J-PkpqlwKVyPntjT88XBXP8O0YIRWmzkjq0JBpoZkWO87MHG1XmWKJAUGSxOCsr-d7S_nIaPbPUTH14A0KHxThMBrRd7R8tN0tKWIG38GsziBW2MJuec_PO7qc0oTH0CKh8ERnAx0jGIfQzvGYNbBn9fU0zpGrDMuzdxhk7IZZTGLRaJ-fXrVArHWPwKXnjubZ6CZAWOg358iMizHac9sY07qHASjjc0F_9qYIq380jhpIudI_WEoNBaq5pSBBdGXstw4u-aG3iwyEUqU86xjmQKuoBofRVmukqF2smUrnMaHMBdXliw4vx3YmhLFj2tt0Pt9dQd_u1d-D_Jodf8gsdqt3tA5w2GvhtgUE6QgIFZSd29J0SiLtOnMj-3yn7A0ZPbxKgHWYSJLMVwOSydOkMCLP9OL2LevEfmsBkLN1KItBL3J25WCl-enh4WZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGF2jvvZM_YTG9olrQwQBgIYcnJXDbu0ULLyXr5uPtDlEQVHbM0QvBKQLfLsIIWZg676TopJtyhgOt5aVIylJW5JlQsF5ohUxB7rD-IQdbkgdPcYzThg7orNR_GCZwiswpDI8M8fIDOEPMOYGXwlBruztfkrS3zCchnV_B8amfzhWwEKFjMTe-jelJ9Qw8Dw-RK3V8Rv3tnca4hcM1gKUU2n7sqx2qGQLgy7aPVsTToxaDvE4PvrTNxy8vRlbXV3N6OGaiSmGt1xLPJtQvZ9Cye9aKsbNzA8dFGWLh4VN6g8C--5DuqM2xuRLA6z-vU4a273e6ZkCNjx61GWtDFUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AIfREIiAHbBknOp25aUQM2nDl9z0zUiML5Ptq7_vi-PlthGmSaqsqa8qhoYab_l6B_mOLMllRz30KSIA-UYNoP5RaMohWbfPkYwYJw_lY6qW9w28yusI-QrcoPZUeJ3pMuf97pCebOkJ04EQEkNrrSh2RZxd85HgebE8EASzqN8yV72OHA-iQTNCGy01t0TLXUZ-ZYhWqyIQDExc_ySBKrYOaciTxSRaY6C0WZPsbcx58v-FR3FgUOoS4oeYBmF5McPB2ZJZljGjhLLp_VkjsiSFd95ziqGuZIqVtzsy4qkhNXxKA7H-T9Jhepp5_EmyI1WnJ1FacyaekyffT2atLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfW5s2iL3kfMehILiXnx0IR-A_WsyLpCHSnmKUF9nloMBQKsGeFPPtg2zo1hzmGZfAZqCTCCYAnTycRwcNrl8UVL2kYJSwZ4F2JAe-PF6x90LkYHPmt_soVtffaAUHMIRj_bgxGaxE8CWaM_xPZiHPAEq1oFdUW_c9iJkeYxpLRcQKmnNVPPSJx8AV94kXAdd2Rf-dyRw9Si1DssmqpX3DSSycodE6ehr0Ma166tLWKEDYoz4S3vdsfuWGQwyHdSB6WF9pyVpMGnT4TQ-nm6PVDrqrK9raTxZQ_TZG-zNxvZtTmzOXKdkTrnyIBQfxZ1t03LXrEv50e1xByjma9KUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhsnEnEHVKf4PoQ2rinhlUSiv9TVt-OvSB9l2_UXNioOuSd0wzmxBfIauSdTPUsH3_SgzAs1y2TqCKHfBolTGOlgUH_gKRw_PwuOrBcgynA_Cclt8J_qgQW8wlulnN_l8XAIq3wzLN7LSFVEEZ2qAaQFIsvNPnwNLPKhFcfVDg0nFBTG0UcYLCRMAAbXgFcKJL-deFg5CO_7e-chDO4flTG8Y0CyqHCLbsSLogjBHFtYmEpLB9sbcWZPqYD4Qj-2Vjfrnzo5rWLJKBHVOC5nN1E6j6MZGOuxpPdVElHzWPzc0O67RDlr3w5TZyWfZGPUtp4tI0AcDEE9MK5MVZIbEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzQfAGxE8omDuh2D10r6s7I_i5u9zgpnl66Zmb7hiEcyewMZkTHgvC0Wzshmy7_i2dMWImfzG-VB_oZdRrf1g-w6kg-B439M8yydDJKZTT5DhmjKKMaLwG4EIezRv0K-UMKMst5lEIKkAXHEKl93JiBJYxXw6Ut00zO03aVIgfyAawSdmILxmkdgymwbc1c7zz1ASG2OWKqwu28miDzWXnbfBP84-0ClnuFqu1JUeWdsS_HgNGABF6_JIs9-2VG29H16CDfTBd59dP918H5BwcYlMR2PcXt6CTb6i7OLat_ZVGqaf7oeuPrZQS18Q1MxZ8qkNIWXXht4Pu1K8GbBGw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m5EgUVdEdd7J0tUCyZwVTi_Hh2JmctglTz-qCPiq0VjmQzvXRcnMAhYYovULM9A3OicOCPcl0zvx6VsRUEKABYRT7gzd-OLr2FFbj4uQ12RZo3sWcE5Y1-CrI_E-y-n-WJ_VgKr-a8YrRWqhBqaPT6ABj_rs0VON5mBfwpAJKiUkKQkEo3rfjJ-1mdUArNX_uTVESa4IrZMmYI8k0GgYF5qZT1B5FwIamTtv0yCx_yRGkErMxSNaXWeKqZLoBdj7JIk8M04Cl8252r6GIrdgy9WwMnLwtXLAEfoUcPE_3CcQn0a1Bld_dAxr1Q8WB-4OVZmx4To84dKLQgl5zE1vUe8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m5EgUVdEdd7J0tUCyZwVTi_Hh2JmctglTz-qCPiq0VjmQzvXRcnMAhYYovULM9A3OicOCPcl0zvx6VsRUEKABYRT7gzd-OLr2FFbj4uQ12RZo3sWcE5Y1-CrI_E-y-n-WJ_VgKr-a8YrRWqhBqaPT6ABj_rs0VON5mBfwpAJKiUkKQkEo3rfjJ-1mdUArNX_uTVESa4IrZMmYI8k0GgYF5qZT1B5FwIamTtv0yCx_yRGkErMxSNaXWeKqZLoBdj7JIk8M04Cl8252r6GIrdgy9WwMnLwtXLAEfoUcPE_3CcQn0a1Bld_dAxr1Q8WB-4OVZmx4To84dKLQgl5zE1vUe8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW5NOviFAG8U-X5TNY7Dteu6CyPbivzKH24a-0rudk-WEnxsaP10CbeK4m-AJghAr8KFkHhroK05hBCMkXmFRdpveijfyR2RUHloaj-6sZGmtiscsatkZ51JGTSqZ_kTMRc_G7CwUAb7SYozN3gQ38mUT69qDQZsdzIY8y5V-zrb1O3Y0uJT__amdqILCi2yVG6CgA_fzXU52RgSGqSgEwFqpMnZslaP5GNbAm_xb_twJ37Gk6EH1DM5oHdzSJKwYe6Nkwk6U5Pa3VoESSO71viOYoPA2YfmLUdsgS-0bD2idhZso3gAn-nu0SS5apBVtN2RRPzRI71WkDdbvbEXfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn9byrCjetoEfEu4aoN6_pueXUReBfnbFBmhwv7EOzkH96vg9GPEhWIzrvuWchB4v6_i_E4jVFYduLFoC3AQkvLzBQ2Gb6otPGFj0a0xTnd7MeVrVJy0mm8zAvqDVQnNmh_EqizWMddzKgKZG_E93E9LPa20MqLO7vhha8yVMcN2Xb8lN8SZQyyjuiNvv-hy3xSW3gglM_7TtCKNHqxu7g2FDiniQxeAoZw6mpuwknbrrd3_Ks3pIBHHRC8c8wi0BWu3t52BvZXH71ApywR64_q6K_7wNKesKN7F5ClONfIlk_fVRG2dYJgE0JC5IRi6pGygej34f73mKPyb5LuDZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jUcZ23CZ5ZCqosKx-nRkhWkzXQrR79_7-os_SaV48oFMRCsVk0FucatGqE-wpEs2nY98V0y8lXwFdVxvdAIck6zBA68gWbdy0MeGOmlBB3zR44_9pCRThooOBW35PCvZoH8PK3lBz-zMf_DqZ2WJLig9NhX7E-JDF1ZMNhUHleD38H8CEct7exKb8zZmU1FsJmkJSAX45LAjgA-NKvNCxkTdrIRngizR6_qY262QV7rUZkYMb8RHEQgrCNmwbMhzfvTA5Y5KzEDHUWCm3UbJInltt2dVIHlCc4MV7ohKEKiWi_Ign4CINNeWugnX35VQUgxiU1Q0HZ4HrMlwfHqIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHQKuAnKU8qLaYmnfuLwQ7ojxbpPF99-QAY6Rwktl6PT1onM14G5meGf-rlaDKN0cNn1MEuwEG_hrCmUp54SlDb9bQy-jK83jYk9mxbCcZqlwi1qqmrzlTENh01gL8f_qeEXA1SRMDYvju7hPxDiNvyvnPhFgPnwTMxDXrRRn4rM4xMjhsuDTW-87vRZq4nt8MJi2gjOzjZkS4vks69BrWcxjGLPQqskLGM2hr2TTB-mZIiuiaAs1Jv9Zf4oux8j07PW7mkbO0JH5kKIJYFGNAzwqVw-qT4eRfn_EO_kyRmo_COeT-obeufT5d0FQTNU-h2aFT7bk1rrq8wYKtI05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TySugwF1F4M1KtlY_PJy8U6TstB6gN8D6AY6Xx6OCVnMdv4aU0vx_BvTEN_gEa0LYkyM0z1BlbLaWnsFHMX0p4cSLUwzvB3k8SOZ-YLmHVRJz_wAFMZ1hCaIPMhAhuz8oZQKOpMMcjCiYY_FzAZefVpKCSqNxOYwiSz7c9r9vroxiNMwWXhKAk8dKVOTOQHSl8j1R9K6LMVK7q6N6aaYG16cjrfbnqSFsNB3us_jRWRx7MuVhu8z1iezdxi33t1KoIg3ghhG3e_9VbTbMQs-VVo_aUSOhUEKdSI4Fflwu4rYraa5eOlbscEOhYFO-PnDOn8J3nhDeV9QNxH4_usXwA.jpg" alt="photo" loading="lazy"/></div>
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
