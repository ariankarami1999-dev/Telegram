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
<img src="https://cdn4.telesco.pe/file/Or7UPYD8AEZ2xEtNngdFg29iJvYdkeO5AlOmsV6z-gMyLFevDa2yZdzIWSB3dW7hzFMy_ymwuN1wGFYrmdiYXJ6-aJgfuKE1bUkyed0etlMcx5lQ57B-pXFGv_iwdX2J2LQ9SkuQtrHH8jqVoiLiYjA_LJpvY7p0jFlSfl-7ZhIxw3ERfN8iYriY0I-frSlf-_UKXGu9Y5hKwYMjTpXH5PF2Y6HvLzKOgpmP6E7f5gnm6IEc--bA9dB8RGCwM1BNJBh5SgX1Z0S7oJzKthf-eEOK1OQiQRdumW243lsf0Twr5VRidkxFV8q0pckvBiITdi7xlWc-oM1eMePVi7OsNA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 00:32:11</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 287 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 331 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 391 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdHHMXo-NVwsLMhTulFOXb_h5lEkFpFPPI8GrqbeOjQe9M-jp7ULsIccC-SDQMW9cURWrHtuBa9N-fVrvCbQHZMrH89zyGB5UPBGEknimeK77aLmqjv5o5OqT2Ta7L77jfI2mwIjaEgBXjmsBzkXb8xurvRB919Wb9VqzhcVqtbwoqiI_IIkya4x3GrHaMYGiw3ZCxXshEbuq8DyGZklT734b9aMPDSS0ItuzPZ0da9LmgqRWJFT6qZGbffVrJUXUmTjXdutn25m9ycCsAZkUUMeSJ1fkcFKzv2o11Fna6JvvFgcyc7RzRciFa0E_J986-AOO0fhJEbdROv0L36FCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 511 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 623 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 734 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 831 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDPyuAD6yAVVG9uwTek5XclXgh-xtOD_PlspGsldOFa5aynas19XXjOq_gjenK30W0J59YhCCAV03fFbn-L0qCYMnxXH4eCOrs8QCwWXLe13YOgUngHJm3W_KGLINz1cL1Sm3n63KMq45eKlBRxYURc_V11IVkASXALe-oJFOw5gPBI2SlyVWyb8WsiYPhw94LuK7hfIdlw-urU2hCB3w090-6WXBlwkhoQcQJcpKeFp53SrAWVhCEg2zSou-vdvudRPJI6gUo0jFAa-wYwvpLfh3r_hlCErup0q9cpYYI7AlmcyOrGqA3UuunAM37H20Pw3ETNZ2m6GU9p4JD8MXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 866 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 981 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwGtzSeCIQHSwimJSQxAXg61TJMc7Pv78NBn9E_vwkRDnnbvFwSiknmy-VGrwWE03kBY2offALWNtKtwUaaJ_nrvSIVgoi87f41L9jHsc3UgjwawTClO6CBh9AIGG8bHkWb5uB4Rb3rUyy7Psv_TZMleysdCs_23yhogiN3vIz9hC4aCsfZfMFPgnpH91Y5x7YpLU-uWmsJXUPeDYLaytJIL0c-P-2k0mGq0XtGL_JeBYTJGaTk36tMc8nKVD2iwm8x8Sk1EwrKnJD0R5g-VbWMp158gHJ7kug7rgQhJnMlQ8s1ExkDEQcb1uMs_wupNu63gw_sd8cRHChHiVIJ07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 881 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 945 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw363SIdtnEpEa54froMfMa8MH25Ngh47QKxCIKYZ5RXJogvgx0SLBsaqYsAIQqnUxK3nDC9K67k6bdL7uDylXiz8deGkswL2uZdc6oafd9lpZe8siVMEbPnWrA-15fB_6lw2aiRAGpQRtTTURngnSyLFiAhiws9gRMuTqE1UmG2KB4rFLzBeai3BC7f7-axukrT8y_Kn8xSl1alKyb9jx-3mWxguEEiZKz-z-l27Vj6q9zW0S47_Rp26jUt0SezejxlYKyAetsbVMQM1RZbW792t2U4Ip2SuJuvfTuuWtDFfIZgKAJ2S9GgvBT2PbPy53cb_0ftsIDHmbLYp8E9jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 945 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krgEM8GNPgpJwZka-7CQertC84nRJY3NOltNjRd9WLFmjT0OdH1ThuNncITSQCGCCFzB_ytMFOpMy56yClUr4TM1POg4azdNdmzW_vqlQPZGHCCeLYwsB8jjR5bv00SeUN1Ce3g_fEvmzaLFPCvzWONAUll__o9NYS8jAkRanaBB-bv2BVKJqerNB-2wAu8x2rYHD9efYSYRteU35sNisSlQfvHBy9MjVfcAvEPTLZBCEn5x2_ZhxK1wVsJxRHAL2K0EV4nHznh8yabRcnq5y-2lbeAKCXserSnFnHKV9qQEvIzQQJSj67ID0tIcFD_5vRDt1amsrX2zxUCHL9HEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 871 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 816 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 763 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsGLBN_TtXjFOFUgh9-nGFMhmc4TI1LS-zTzGAjTaJO3gNHVWVkLRBNk6Kxv_2aqRXNpRBh5_ILePryyCoxrTjd18EqC2CMFzcFf0b9lNew4k6tPk0QSzq0dmnuBGPxjJxD5QlqWwEUZvhhHcwkLA0kvPWG1kr2_nuwNLgnHSEQuxAc2eVCVoOofHITnIEx9t0J3bFbm6paxj7SFhbTcGdepawd2XhBi8l3vIliUxC7v19U0QHI56HEiJTXQF0eOGOMnG_SdogZaj-LZez1PV5EcL1PzMDDAjGTLuCGvCrDOI2mmV_Z9FA_rUQom_mHzg0FekFnZgsDMjU3uxMWrKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 849 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 681 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzyOJ82J_OHAbi79gN_MJigCsGtEHUaQRAuudi_-jDsI1x8L-idwXDLHLj0GOEbcaxdOinbZCHEjHtwf3Y7kmpanTg_IBzKFDVGXQpcFJuiS90uZM78s-5dPUnX88DEqDr6ICm1rUm2kgdXc2ghmr5_WHaW9vmR3Ft1VqqO-th5DYQ0veRPe3qRry_Cx-ut9rp7sUWfrHLX_6SbDmxUsn6oiHszk4PTdQwq0kDq5ehpAKTIvJvnblXSWCGmSOdcZz4EsxMF6SijOds5HtMQm9gX7qs0X6Q-7HiYbGwpWwar48NushaGG4JS51FSt9ylRMdmStpER4LHaWaEVawzXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ak5rVrUOO6JY3tHIUB5I08HWhgQCxY60VLZZnKCv4DqAU6bdJ5c_YgO90XX3HhJoGKzPRL-Xqv_tZIT2_hTfXv3boElnFyx7Ki9PefQrvxfS1JpCPJEIdCDiYffpmwKmztS6ZYIqkvFFWnhJ4MONi2WMpBCwnsnYTbegH48Vn1JVxyTbwdF4tGqD-ZP-FZPWDCcqwg_X8mOvRq54iPXQClFU46BT4WLOSDvf968opuhRIeLUuO-dDmzzdsgJ0vPEbA5_DsFZB5ybqEKrBcuKdQk8KrkKYmmV7TkqsiL4Nu38Zyx1O5mGgoewNxBRkEsPzqcbZLZni8JMd9sC2U2sQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aBKRwg5bHH2Wj-P3ln3SEU09s1bMoA0M8kZZ42vVRvIFZZU0d22t5-voHEeFh5rLLJnN9CkeacrUJL-yt3JoKraC1P2ef5yI9zIjBdKlg0B-UmJssKoqKxxUyjcziwL560aXGSwY-tf007NgE6koltVaFHyeu-BNeNju2lDyjteXPUb3cL6YZzOBF7IDTPpQPeYaZCaQLQbn2xV9Uu1ohxpsSVmbNRZ8L66R2ssOxknA6Ax5hwmnFFuLCTR6K12oE4X_t77sYIcNWWWDu7IeI3RlYnbl7IcPv3lBbqb-poIwOgWfZCf4h9wgZzUSPw4v7FBcNvyBeHcJIiDs-uC36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3X52erGLMKWz7B4RKDLfrLHdR-0spLgbCg_uUmpmJLolloAyHtNDyQsTzlIhR3YHLuQmkEpM7JcPQkAV7qyEcnlRCHaRrbzf4dfgdYitNWAnslDEBflDa_2GB7XcGDxSiNCF1bK9qB_i9WBJ4qoOfRoM8JOSedf8DCqyR0-PAbkv4O8GNEipFjFLRNox5wthq8t-8IFmneuXl2wkjneDBvuuNAiqWdgVILCaI4_oHk5nX-ohrghx1miW8ye53d7t6XXKxN26bjfQEECyHbzSV7b-icjbyFXTqextwP__9hBONjq5oEws892Zsg612Vg1LqZBhItYm0Z6cyTtTk00Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZrW0jiJHRFxfhUxH5KQQYpHL2Reuzy-PjT7Bx712AQSnkn1ZpdE5qmimuCTDYit4COJDorMhZ1bNcLcxS07G9iSPM3uVwhvnxjebE0K6xVtKJPfD7h83rDNJgk96oYn4QgFwf9HLD1aM-jT0RMOnop3EOS92QYzTfjDIPYm_EBVxvnkz-gWjxuUehR8csFGnrYqZW8QxjpJ48BiNZKDAxH8duOiv-uyGev6QZFyiB0WGj7Bz9Ckv_IWO3Zdg_Z276bjAOyWzCjJyTGpvQA6LKNwK1TNTBqI_8XeoDm6y6f4kYwCK3rrBaK1OZpb1fopdRFAkvCf3J1KfSKCnsLQbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 974 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqZD-8X0SYw6Gx9RiLhpzE9CDPbr2wM-RIfYR4q4cWmajUt6pnWBYIetslPs79Ad-qNOlJ-22QXZWwQLfm2mfRMnSqO0URIozmg8uqzZ9CWnNv2IgNCdb2Kq5ZOxNXGf5UaIuavbWVlDPrAKDXb0sLUZZ69NWJdCl1Hdonf9pmohaMciNtlsmyhF2-WDb_iUKulMg6BB16bjPIyhuehd3EislWX2c81irgfbZ7MTRXf_OWtlhFgroZGVNvbO1Ifjzgn3IAryOpkdVt-Iuhu2XnEWTPU3Zsvuvvc77LaifbvXD7WpK_cD6WfBWnKCvbO52Gm-JyzBpqQi7KSXEvZD-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=ZQvkP6Wn_ye7Tb-1HiA7VEJ_IzREt8Xeu9Eg1SiCi5tHKg32ojwiOKBSJWCnBqC70n48goURXUzH4mwDVd-3LM6dnz4c_suyV__LIqPPBQ-qOc8wsVtqaR-0SrPGCPGjK0ZFYnFi8CiL48-zewkP5_7cpCN67P8xDe6TMBGoSYhZfRnoUZuJJBEgg7BDDiM2BYiuFWxuXRtNAziFMI4lzQynuva40U90GAPCsV3fjTYbyLv9-Pr677K4Gsu-gNJOZSXtWQvYurMP36HydwR6xtVVeLOjsX6ame-TEh1lRrESjLbnfyxwWaoBFRmD86YSTWjmo5L1qiwXor1rDFaz_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=ZQvkP6Wn_ye7Tb-1HiA7VEJ_IzREt8Xeu9Eg1SiCi5tHKg32ojwiOKBSJWCnBqC70n48goURXUzH4mwDVd-3LM6dnz4c_suyV__LIqPPBQ-qOc8wsVtqaR-0SrPGCPGjK0ZFYnFi8CiL48-zewkP5_7cpCN67P8xDe6TMBGoSYhZfRnoUZuJJBEgg7BDDiM2BYiuFWxuXRtNAziFMI4lzQynuva40U90GAPCsV3fjTYbyLv9-Pr677K4Gsu-gNJOZSXtWQvYurMP36HydwR6xtVVeLOjsX6ame-TEh1lRrESjLbnfyxwWaoBFRmD86YSTWjmo5L1qiwXor1rDFaz_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9mQGuS4HrnUIex9N1KpRhCGztflvrPsX2eEVugmsBCJe4JKwTqaxFT2ESmTzwuKRI5_Pm1VP11mPcAQwrzZ_SSyp7P3ZFzxPwdIszuqCPBlajtJHdTe3JNSq665P2Tv_k1QFU2SfLt4Jd3sHQltniWs-UgHDCiOpL965AV5PQEiViJmRyqdbAGb2_x_leLjYKE0CLxtL8pEIZOBOXS8ffN6jMeNVSiTG1lztVc-iezRgTE3OVSanmwvkckJbIiqxWIgR06LBaB0a32-5YMmprHR1twohDwe_AsHkYEFOEMq5W5VpSSMIr1dx5igApwzukHkOfeS9biSSVsk3tQtcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 928 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYqgWxOAYNvTB4TiUnwZzZZcG5dbTdGUzXNooJmkRaRzPpfX66IttcfCy6W6IehCa30XrE-BO8CPJX0IAfqay3QB1FaZyerfbIRaTzCAgpqCIL943Kxe-RgmA7ft3GPyz0bga0ahVioyGAvC0KdRznRbf2zrg3vKwNwrPDzTMWxFBHlmhjnX535FcMSivavfZi9FIgUZqtUYpX9uhV_uCFX360L4dcEfAXsAGaSJeZ6TOaqD4tGxGBBvg_J1N_27O8GEIi5bKVLKmf7wC5mIt9N7jWI2cqhoAAf-twFcaOxBd2JWvK3spz9KmdllWo-CX33VYslusVchkFjU1PK3OA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 777 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_QxTSpTu2J5RQDjgP_t4--dIMFluj6NsWHBYR8c7Kul_7PWNwM-idr6TX34IYcIyRnjHLAsC3HlQKnu7OqqTQstIiyO_k-5bpmVkvpPY_bpM69qrlrJE3Mkac0NAHRl19ckphDjZsa72qfpi4vy9UHh6xFeVL5BFx1vVB6DKiJfsPriSh1B8mweo3yQpoV29NHQTukSYL_GXwmOWODS75pRMNFDqvlXsGbahPoNuYMqpViB7R_BLn8FwnEZDIm2z22DJ2Cnroob07PT-okoKfhGiIVOb2EftBiEMvJSO9SV9zNfB1fSnB2R5-WdyqPshVOrBmSJ72M618AYhGJZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNjHGG67QtdMuGDsv9je67dlsJABgon2cFeYvy_sdi3dZGne5yRzowQbeTvuRhNe7g2TogbVbxHMFwOlJ72oYUpdRtKPmRX9ly9979EBhvm9Y6EJPTF-IKP2qHcLyEySUpJ_U4MdYTRgvLpKHZlWfgmmtKLq2a3DnwdIrj9jLZE_5wqYmwTwg-B3DcsHQ-ngCxyfh8-y6ss_lXR8jvhjnefweU4uHOIqEvMcSmXCPpFfMkHTGza9a0oKiW-bMOHfBBnUZ_2jLCI5l1NHRs27k2cprIGk-2p_9bu31k72B9TyOaZ8abZKmjWOEcIpvAG7Fk_xI5GVoncI2EXsH44PCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 798 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
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
<div class="tg-footer">👁️ 985 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GieLoODO4gi990KG00r2bz48bPFLLetOCGg7ElbhwzT4WnV4m3XtrtEWY4qvwvRkA6dWFuLkQzpXfenqi1kOkOkake_y38uLsKyQLP4TKPywoZYSPuSInVP7gqTb8yn08VhPFqwJ3WnDJQ9W6C24hFdc487Q_romzIDZTOltITZMlHCLESgmeB_1YDP_W2QIybpaSL87pxaBNJBb_xBJ8FdIfgzH3q2BzgC-7_hci66CMLDv3PUNdRwyYulsM63SDVM2wPmR3K8d6Peg3QyFNDR-2Ao4WrOjQRujCKLWzWVPVeomnUaTLPGIQI1FmbaG75bNjEWmDVDHSbDqgPLm6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 920 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOQ0vBW5JFupZVW7mUCuTGP4CeXfecR5U0RC6Be471rb1yZdl_6bqjOfgUneFBwGD2Rqt2Uu93Ez41FBc_mHBkwD8QT8DFKIbEk7PTjdssWQQCrz87K_jKQgQYtdpdMLcGqQQaGliUM8fB1xUIw-uw5C2VMFjj4SEhoK03IdgAtpfQmqNaqTSeUsIuItWWB8l-zKgjcLFY-O40KCrKXqs83JWkcuA7KszAIs9ksttpIyBYHPM9VK_spuqUl4uggaD7SwnsCddnOY-RcJ_R30SGh0WrcnJwWIQTASO581Ny7DaQklFFWcpQ0BHYOLXF0_WgIb7x46-hKxld9YPNAbFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 742 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZTQVvqJVP2if08KNQZORaoNxYye8RvJkVNIPCFEpilFwSOH00Nr2dZTfcCnJ_FVuZaBut07AFrPLiUTASfD1IumRuiM2D140dAiR6KT63pIpzyX2f5Xb4Gv-QhiRryP-h5_gR43eUgj-wNmlV3g_kYrgJ6XZmFRaOvqBRaoydrbupJRIXqnuIdYL6AiJc9n_J7xlnvy1y_6fZP2IBxkYUbsSIwtLtQg5kyzeQcVersBtR47gp4cuuEN_IR-RgQwwg0y2VpUiq53ujQ8_vJ3E85u0mmGk5CpkT0-4R_wnxK2KViODDYO1IImbftuhV0jDmGyReTI1mAHlaHVdJNPXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dc31Q7LXFUJQ-b5FSITf3NCUq_J7LAdvaFgGZdIicJm_jNcmsaH88FL3EdroV12Z1Ad3x8-gvL5fnR-djasjp-VzFw3q7gftAqG4YZrZ27XWavEUI5oVxHYpfM5dKEXdZ5_Xvwm0Xe0ld0bO3C6hnGo_Bb6xkrq9U685eXffOJF0UbuxpH2sLp5b8ThopzZnpkNEn8YCAeO0B_MXKeRrroVIsHONdxa2apIGQhidO7Rl25A6cL1UPYjuBgg1hXB4X4fGFvg3rIgsFz8SEg3vwrKt02GcRufd-ihC_4fWSNYohdXt6Vhvc-6w6L5meX6hxZ6dfmq_g4z3tNeIvABWAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 752 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aa0WcBex_lQ0RRyCmFqdOh04kpUEZhDVtNg9ZskuG0CuYzyFq-TVIBeh2SVjgOjacEPfWAunnzx4tfFlBx488rUkZXTrwfwW1kZMGbXHJGDOo4Bdbw_LpUyVvkY7AYrZ4kwz0DVedyETbQW2C-Rs9cDAfb88VqMyu2MWZcqAO-J10g3nAoe3YDkKTYHWVj3IoVi5WbmUDmGBKrE0H0A3SPdd65MqZlcQierLru6N0CToT7t92_Od83Fb60s8Thyd4fPn0XMt34NDg-O2m6sQUMLXaN7D59jLwpxkhfkWu4I4fed_uJ9t2k_hXoj_ND2dmksDmZl1pvNdLq4Dlxj9RQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
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
<div class="tg-footer">👁️ 810 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
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
<div class="tg-footer">👁️ 818 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
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
<div class="tg-footer">👁️ 720 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmRan73nSfU1W3-vpuytzJtRb_E4nb6ypWlTg-HkhVGdYd8iGiqZxvEdyx4wKLhvLg9VtKNvxRjRsBWV2o80jxI6wx0JFA0HwBa47VJq0F65e5H935O81tbmyNPhT-x18I2V33hql68xU2ryshQm45t-c7ivpT_EtVw_dindu4ijJofe406OzGu7kMZQKHNG6vavs47A5DEaNqxVxrga_g-XmQOzvOmQ8gQkp9FG-zTEFiuPkxT3bmrzdumd9gjbqcjsCCmbL1V4o1t6TkPt6RW63ZithstM2jZkDjYGiA3DDwz6FHGoEh_HPTOvzJdnFucI3P5RJzyYDtbIygys1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd52ypA52jL8b5AlRSFsULgUSJ87uk7mg_gpJtuGkj66BCIwjKn4ZwA6F_n7V2vxDjjEAMTf8xR-5IjE8NJVlqN533uWIGRMbPGb27TodR3c-O6e1zwgsReYxBVPC_TzdAZ3G0fhRSWaxxXEvBW45x82YPsSKxT2JBIve1tftLd7z6uaG5DU3_oAz17PqQ_43Hp8zkw8-yC4qpNLgvgR3U5SAeSkLikSk408HesP66mmseuO5W5WVNdVOwWTfsZjmsDqOHSEwZHNL5cflnSMz4HHr98Hm-VenfMNikXE54bdw-TDm6B2eASIqMcWWRxUo0Wbm9tIp0HNipDTsg6T4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7jpL7ZCj1BPgcTPZIFxd07sHFgkZOStOwpcYB7dM-eIvnNScpN7Lzs0XQa3JIFfrihskYasgP1FfUfn5qRSVsrSJxbJP_Ok5-wpugyvZd-7203XYZBtmdjvEPPpfcik6N488wmQW1JV3og0nVfInNdWaKSbkhDMBieVaWnw6xnP8JW3skW-0JOncPlMQzLw5Hc62EPGRK2Z5l4MUh-qZxbARKehBuEE6mCt-ITcU-4kAm_Oy4zWH_g0h0upphpFntlcKRH6vMPqXpe738v3OlbFkczthrUAe7oDUfW_1zxTGcWC7ZRW32WytARnYmt_q31-ZoKY1zFYm32UyRtj0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FsDnryaNotEbvtKEQJWki2tCmKBKgJBEGeOMzYlgCI8KPiUAv52beobE8n-AKZOW3XRcr6aDWMIQlAyywzowJJZP7-d6ommPWf24oDFtIn11O2CAH-3cOuCk7XikHKXipSn-9s7vQHrVzfuR6jU2KEQeiaPIkK4SdNAM5bvorkRCN6PnXaWu8OlzuTS4CNvOzoDxBIAbRueawNeLUJeEMuto6xNyUt3_61sLpvFw08t92T_6fDw1_KTXkkOdjN9RfeIVQY14b91tKn59qq84klsT90pBLpoZmASjiegnP1JybiK0z5oFHxP0kKprc05EDbalIDPwVkJBdgGyEo2YuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DeS0iDbZkmS75m_Rgi3U39IWu8c0qoc1Pqfa5h4nR3m8FKUtsFwEivGEljrQNoqPvnVc0ZtEWcoufb79Hse3G3NrFCApRc_QFxbB3nHC8cjAnRkcIOAR3K4yI7Qa-1MYv9nqkokjc5CcIB7ywnQu2tdZFXQuzL1SGa8iRBGZzN48qYyWzO_UPUVvqG2DSsjKSK2Wm5IKD-Q6NAKnYyAfBqtAYE7TIKOTgezv2FjGKhx126KKgGJeC8Btyyr1MA7koDU3lmXcuok_gY-FSpP6CLVKncB-bt-LB-mZxaDACtOgmw1FqU_hAmICx1hpLY8ooAEt82EG3DOenlP8ohwGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCBuqni2MKjYxJEK-DWkW8taPfx6XJ08KwXiWBOrsH8nQfhBV4KPcjb7Zh8S8aObtqZFBiSNMknRs-5eOIORih9Au-Sr1BkGrqbnfkRHbVtI_O2JqkvkifXrtvQ9xItaSQqsApZFCng1t9SeZUZQNNq3WKX92MnibU8rkBXsdfPILDys6fHLMWFr2jghSKuCMD_u5EgQkoNMVTXEmyNKxQm9melC55XnjRo6oKLYkQaoQ_F9R1cdJaJ5NkICkBiPh1QazCfHX0fySATi4ipr6LG7HhaBrDvsJoUkt6NOFyMwgKYE7IhtucJo8vs2c3lOg55mKGXFyub_8vQLBOBBFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_zcRSW6LBAjjnkiNJKWAcZqmfTuI4-7fkhq1bBk-emKRli-KxN3DPXu3ByAZN3kUrJzdQDAt8KKNtyY2ZsQr1WA-hx-MUBbJVNnylm43YF5AbpFhbwJVD-hmwJ40zzGy_6AQZsGge0l2cEzeJ8UwBd3qTuIrLkPbKOif4AeLbUUtYO7CTPxELo6Xd_SWMw8vOMg78bf30hMoEmvmlKjZnM-h1f0WGLb-7ro-kR_HFDMknroRZwn69Hfnk9mnQb0iVDJCQOkDOsFXeV0n-Ds-K4u0JGJZVARnpCPiMbQ0sfnD58NSZIBwsN-HSs0xlT_vzQ5AIxAMTUiIFqnmv0Wuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WiwbU_2dhDxgH77RmEN193XfshvMBzT8Hxam-y84PXoi3OfVYojbQSq7ByT02Y6GrSR08bl1IfFAHchK8szWqzar7qV8WTjTdidtRJKBj_xTBQRXycn-pHsGj8u1Th_OmmkOjqtNE0Iux0AQsg_pLG1ym0gw2GOTNCdiNbnGxvlHQkkpOgKwbmMpgNWg9uFdtQNiPnYcrgzLhJPEHAIv4tKbgLkbqZdU34VB0tkzfvvaEVUdsxVuXRzStYb0lDi15nX6fcK9zctC8zTYuEOx0fLGheDV8SEgbomJL6G2Fb-Xb4QRF2CelHbRMhZyRL6VIzQ68UtWyzCBSVKsE4nLsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbQybQ7djXH9RN2ET_fe7QK4hkw4WDNTc4Zu84Uf20fNWlbqmjuGWh8buzTzYK_UlHejpvtJsnVKp4Undy9qITr0TOQIqfL3OGJDjF-nCgEHnhSgb5bNnF1KTKoM8CzQxAh8FaxXDmeKR2fddRYdhyNEkXFGr8XLhB7AcBrM3kxY757YlrOydGd8aE2u1t_LSZqTBdPWgnoWbzpdN39hBIBYletzuZm27gzBeBDI_n5LpPwGo4pKIccrFHUI5WqWfeu-VYjq9XLV0ZKhz3BI7ESwzY5BruqCqhkOJ-MQd2COaUG-7tv_dOfn0H9oAOEAMDps0wLKBaYhKzymxo9V3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 578 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEgh9GdU_Aa0P3spv0R8pLAZHi-Ui62KFFNTDDBXu0np5HQ0Q3I8SL7B1CAI60pacVIlYpyYqG0iGHKFdL_J12_gYQz4p720fmg4Y2KVGCJxaa9Ni9407PBQzUIB7SK_6OmGOvX3KV-yvwCKrc7myPbPIo1Y3NB_uRCQP7jkKMGzmb1A9AIydhycU5XZ69658tT_DQnI7iJuXssI4DWqzri-_YLlVccDSEU0GW0br7LeRSx0nbHOs0JNF18o37mAmCrI9r-UAHokPOwj9mcT8JDb5088S_7f_Cqi2F0pdrik9EHnpyXzIF1FhRLxCE8FaT7SHBc-B-WdAvPIhLmZ-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 590 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1dpRuXrvmDyCU5YwQMFKJSuvXdVoA_BtNlnf4hqMwnPgJceb3zzAASxNhG8AnW-4a563vL93q9WdN5qx51gnoM8RZs99jmqA-l2yjHNVT9haJdTTU1GXV7rFD8LC1JZ6X0XWXGUmjt86FpyNbEsK1-wbeaNT34eA4oo6agoRhS_WhNmAXqCl-cJZ-wrDKcLPAewumK2NdcoHCKsKp1CTveIUoYScTeCzzb9jiGZ2YIgShh8yHLhcL31vYLCCaY6W85XvBOIU3v2hsQxESAMJTwM7z8kWD5LzjIRE7tCgswXCHHSOqPheRMD5w184Hw_GrregfEIEOiy7pys_MjjZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 699 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJJjc1PMaqmyTL7kOpucACeLYMjo4QnIyrnwclcc6sk07SeyGA2POn0aIXiMLTYGheNrWVmB-SNXZulcwtcUKGqmV2ooMDGRwtEW67uKvf2snYJd71X_i51CvhVBApNNIpp8XOVnvaQwvxbkDemkjJKdtjw893KEPySwLKWOgadMSlIoftxLY66r3gE67ViEWYhTTE1A2KN-Wyg4zR7B_CKU74GnCdMEZrpJSEmHsDM77l7MMEywZQvuvHXnP6xxJ7aianmweGitQTL5Gwufg7uRQalZx6CpC-mebt3L8ejxTeT6bt5oejWQ5pBpyw6_H23bmfwp_bd0Pau8L9oA1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLWMWLc_Bi-AJN7a15y8PUqKtDASTP13hOIYVckp1IOmBkA8hDhWUgcaMi9Lbn0TvAcyp2PeiPUwyqsdWE6SCnK4_PobNv3pWGUg4QG3JeLnliudU3GgaHUb_v_P5Hd0bvr2aqJsBayLr5fq9vKNDSFc55tYUwUfyB77ZbE8prBJNgZUT9wwepZPe1CVaLl6Shy_bpfAdVV4IdEOy1vLY3JJOmkOwK1x5tuZZdS4Rvj-jtbRoJ3V_Z0AN7NtcE6x07UTKKSDaORneYOVUTlTJKwPsyRM_rNvbrjY4q12_J3WImee5vZ5sfg1ZhxMP5XSrcmHZ0EMqKeHxcl8zEPZOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 712 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhsSXEF7exWYNJ8WO1gOqSv94J5veZt3AfMyWAJpWdnGzDHqbWOmU2k9mVrDxnynAc6fR-YfyGAlQ4SBLrLPPWUyxysXlhnQxmx8TyQEmMK7xcWCMVxmHV0P-dGIegAIKBGXQfYGpKQB6AqAENFprsCw-WOVvNSPwaAzw-GLTLa-Md4MFQWWexMkTFKpKPgGA40Mq6Sov8qXzlXfBGUjSXM5D3pUbhq7-5Zm5QKAkYohCtDUi21Jq-24Um40yLitYn958getyTUBSwF1kPzpz7CHCfwiYKUQ69d7hQvdFguCmYzQklFZfvDLFHVBLaMrlmr3IIO-9Vue67U9v1gffg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIFrT7pGuRWtQ1f5UCtO4HO_Y-pxJ0Yea2YTXJE8AI_M34m9XMS_xfubIYg969R6fl6_439P32ndyGe-eygYLXS1cRzIKv0LWTvILA-iwaAS_yQUwHU3cVg5j_LbA4tZ_G3y6Ema3cfkmQzZZCPcGz0pS0MCN5K1XotmDDcDJztHf3DELnycdi0eSVRBk4Oc5WYxLNN9kYrrqEMTzEsAeHOg-MQSCO9ig-uD1BmbL2bhHf7VTkRFBlEzm9WsFJKPerIYAQhOOgvxYUq08QEkzgt_LnnI0SLHhuY48Cmn2ipQ-UtIyztURye9ibKllOi3r9mqicH3Estyw8tUvZsmaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_ZPnfa4oHtj8_MbarwQuyizeGgeuHvKLCmEffnYTa0uCZodpOZK8zch-Qk1VQ_mG6rG9jBQ0BNiiRcmhZJPJNnf7OzEGJBsGJSZGlrctT0L7mvs0hdTIQ811TAktf_JScCrVfo4bc-uR1dnl10b9cLVbfOC_wYj0wlBQo8cj5vhPLHws77-7rbhPR4cZnTbltVjtbfnSeW0DitT-qYdEObMjvUtqqQ1a7OyqJLTIey_KGJd4m69AmvweROttFFb1KpGalwmJvLPiTn5Sfw6UZGWUMgb3TXJMBOL3CtaIA5c8TlzDo8JmpSGlZ3hoZ6OIsyjovak3UKn_z6OuYD2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gn-lHEBtWePmkC4TJLxefAJjyQuuLcljZnc9hM5HtLD5lPyFPnMwt8UoGWvXWNeY_nTdhCXI8W-yXuN9mUQbpZrTFmaycyFeeAa23WRmoPUvJZhfp0IF_45AMv579JbKOfF1z76J88OAkAvs-YDRYDQe36u9U3_0topylTRRtd1JYaKgKPzofaBVj8dUreGckXKeYXDP3K6XOrHCZ2UVktoaVSI36hCfgf84vkvCRSEkSPbKkTEuMlmiaJ7OGwpZ6yQv0g1gtYwxt6zhMbNwTswbmaCfpdMq6LwYGS0fOHTuSSZCkv9pzbAX2qeUTWCZB2fNDxBg3M2SQHc8qDPBDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J15r173xGYVk-u4tdQpOCZqZ5HCoWUwlnaWVrrpLBPwNpy1lzjsg2iDWAktEFBaw0JH8BIy8vYsvb-hV80eHr3eP7hZ2nCqPk9Lc4yo3uxEU8Lt9ZsQHWtdhf-DnRvGmHIF3X1JjSab7vNcggg9aVnZxk3UXbuJaEaYvH-7MzgGeBSduBuCtDbU9E1atQMWjJNmlvw-GJYrr8Xn8dz6cdwRI05f9WoG-M-LUtYFXsn_2eU-lSQHN6lK8zvM1X-AH8fRi6PZNw9H7-y4ZubWhVb6Y7N316FndF7JK6VBQ_37BXLgonQagIM8zK4F0bNlOozTH29n4xnC-tLVAsV1juQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNAbhik7k90iaXEYNnDeFPKEkPS33xYHP0uqvVlACiC2wSRTPproJ7s1pqDLj3Jjh0ca9ISuXXSXYQ70cpwXBkBuf80a4vCNyW11iwrj2xuQABCtADpXU4PYOeSJNmCUWiswwg-OfEPA-aYm9AN0K77noOLvp8ujl3ryCiBVmmPe2GiZKf2O_oLSxMOnYgnWD3DhkiukkLIHqhs1jEg8s-gewXmucUoyK3-z7q506qB_ZYSN-xkr8qhlRRO7ZqKPgyO3Ny62Y-bnNDih58NyNLOc5fPbGnD7tvObiEnpNUQFfbQAhgPCh20FHXpbUculN59IQXN7AM9x5M1MmJ_jPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWqde6_xf-6FARru2KVhHSu1qlR87ctbDHrzUBvoyi6Jg4Z3q3gxbnXeoQEhUt2cB51LkrZTxFJ_PAZBlOu3gqJ_iDSlJmv5vMgmTCIPEPIKThGSkmtVc7wEZp3n4SpyK3ore7n8tDk50eodHAomLoHvDkW-wna2KcbxA8hF7k1DcPuOZIhofyR4TgH_ULimbP8NKrztF3Xxze1-o6VmINCxfVwNJvmgSpW1F2XWb4LvmJ-UcQ843HamTR9zy6A23d97QqP0FOQAptflZa2lj0_APQ8zaJuwlL4e7Xpyn4Oir4tyKQ883H3LvkbjsP-Yl_eh1UCp2FTC6F2y3b_5Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtlgg_L2-38epJVs4o-GLOI7fdmYrn0SURR5LR5RAOh3eDHp_-zB85RdLSEgzaReak5JWdmgRg6u7Z9lLv9XlkUjYPmg-IHpTnAGZ1LfAeyrsUa1OuSNo0Sr1tKUKgqWWTAR1-soHRP2Yt8AzRJ_xNZ8M_exdVbSRebLxtQBihbJN2pE1CzaP4Jy5VVV_YgJDHUMEoWr84CvGqNV4onJiDVtvjKlNkTBe5LMskXAUowW7At6oLmUxMVCNhYOHUYRZfiiwNkrsGzf9HxcwB49i0ktcke_2iSwcukiw3tlN7CL2q3qveEog1oX9Qw2gyivfpFLMQ0_XjN2vuYtfEAxPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 691 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
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
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZszBkWJAp2637TOD1G-kA_trv2hsVY9hZWlX0DUPBLP82Allw2JO9z7xlPNVPXe-gc53hHDTQsmpBzjslFjYGkFFneknxF9YVIld7Jlo2Xpe5D5LRicjtcbDqXo58_AWced5fjdaQG53n5mdk88IBvNEGyzgLlRFc9xbGspuCmZ04bzcv4JJTnsQ4i3a7WkJTnP2FRfHLhJbxX9qmDyfe_8IJw2F9kjPqOa6beN3cj04AZ-PuAO1N01EOOW7BKjQk-AMEJ8XngCHMFfymmG_xwo132T3ljPzLgV3KAaKtqGnY0XmZwMuN4-b8yscLtjodIEAOMynQUzW_L_L_MRCxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZvzTILbXaIPvylcha6N-N8GG8i12h3l5TKLOfULkINFRE1jCvW8gZ9za7wvV3vNvyUVfV32i6C5yzcaxujVwNzW4p7zpSPvryliitzZn25U7WIKN_tKyZGvBqbO0muR-0etWCUiHdHwJljc2UWxJxAvhClECKQfrJm2r1L7i2ZGMAvbJrUsHhQx7uK-dctwQHUFrcTXUFyvgajuCOLGMfHrTXwMxXAzsDABJnEMIjmlHeArrk3cM7jixPfY-KzIBCa3RA9MVor-1FZLpPDRA0Aq3onZSDKX4EP5Vw0qP1HrTleoO2kpSVeEOK8la42C2iGPRQiCOYAd0SnflOmkkPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 811 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qaSZdsj9gn2Qo5QZrdwYeG1vLflo3XK4l-1srsQAorTzI8ZvLEsHmMC_tX1ULNhOoDb12oWXruycLhwUQ6ZfNdm5aQMZSuqgaESWGoCaSc_rQZ34tnwttOSYtYv8BvRRB6ZiTtOcHbcs9k6vtrFAtlFqf3vx9vnmqrA2uJ3M9KNCu3pYwdTJHU1aP9jm5PYJ9keAO1Cx_cCmTf4KycmBqO2rDiyG4AetRZOn0ELoWc04fVUYDDX-Fmc9CyejPKPXm1K3bjzYVqLnGoRZsfleQE2JQ4twNH0C554CRT7xuQHcqvMwU3X2KHhIch-MT_uV2gu2qgF5fVXeixsGD8qSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgXFYtCTDB9wDg_x9CxSzRKCi_oAMg0D-afghD9RtWyXM7_EUURPvTQDeGpGwn3X-sRfvLy3taQxrsa1dYGUUhDwpw8sDMXnYWXPCSNeop05lS9I8ydXH5oblEpAS89YucpcRKRtIJZPIWXa70z0e5aaL_OThv4oC6s5H63igYS3lQHnEmxtIGIperQ9xC8jATtVwxaCu1kwZSQL90Qs11G-mWe0LBqkLtlknL8PhzE1bX45idBd7LXTDHsZSJM4n-VUfqnjwieN_1rYC9AEO5Dx2sosejuJbucdp_z4kZYAET4utzoENSqtwwdkWdufszNDrOaH4KcIywn3YPTynA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ30zZGuTkc8pC4RLk7HXJepbZBGEYfrILRXz5mfl9ks70nLBG6lChn96StxE5_tDOs828yl5Buo6JSRbp70CLVdTAp_ro1TEe_vyZY7wn4YU8POGEi2h1mSl_BqcXTpwYu2VTtaCmh6nfaUbzf9d27aviodM8ngjCAQ86W1WwYKFc5xQmO9UYvEGmEH19Kv8hUOtCWb-pGVHjAs4blw4D8J1PzrqNxd8QEUBoPcQ_FPxMS3Oul-0o2VpYljgxEtJXmAvaqd_eMQF6-VC3D_ym_Odw6ctBn4flGT_pg07ZVP0LZCv1C5AZBIkICiE1d45Ai8Gekz5jsHQLThyuHPKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PRIGiFxBnsUXCcMzgpVCQmEodY0ceeh55zeHN4Gc_9liFv7z2fVJ0Qlm6e39bFEZUfXCTgQ0MrGTRj9DAol9pPVq3qIJuoP2PBfUYy_FfVDGXQdm4nbIUoCgLfWYkC2Xnya2bNMlD7gu-P77FgA0OJ3MAKbFNKV33wO019I3jvcth9rADNWnsSIpFjjNYPB60HKxv04syz1xkcOVHwli-jgQPjZsGTgvHduginDLZP0fX-4Q_6ENSDeXmM8BzxC-S7V8V2XmmhkjSWH3p7HgRH7dzKAJGa8McUAZnWzBBuXgS5YFneEN42-QsZhmQFtirjhEviDbEj9IN-Afm4vLhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/no_Q9xDm3iXYjbfwDd_MZvCvkpeRyxGklyjRzg-cVFVIj682ppi-Edx-3ihyHTntWS13HYbGIGeHasFuba8vtmq-Ny85lE_4qH2gcAFaqj1yLyo7Q_wFrMSJMWIe-2AuEuG1yTMvH-W17iT38kgS94zwtWJgBfmw5rHs7_bQ9X-bCm0z9TrKHVbcEIeO089vdhEZKdMic7bEA6SMfYnmXaU1a9P62FlipjqcgLERdGWzJHDZe9FiyZGden6SUuw7EM_VxofmZIj50TpONctcFfut7YfkO03CmK5QMcGiMZJq9-RE6GDQytENKGQAtg4Cws4HsgH2EMBSLhVfUlBz7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
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
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAfJY1n6Nd-HSOInajWTApcK9UQfUdRmL6-slnftdcvxaP-NGFO1ok0kiFw6D5bGnsTns5i7H7UqmCAunby1M2X0sbWNqJrZCeSdoR40Pzg0pGjq-oDeuUO98MNzTEzzxdIZrxvUWMI5T5q5LlNUdPJI02Q-CGdFN8LXKVgXOd9hiEB96dc5yV1Syu2E1_PFAT-VuTSaZJQhBoSMACQ_29ktLVEwnKmMeMpNfYh8xoY0UA90FMel1RjdazkVUE2PMi9w58NqmTlsaZVEssxmcLy4scQHeKL8CBEVj43cvdV31w3_oJzG5l2Y0LNSdrfeDuXrNsz-7S-MGLJ1qFXWKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj2BcX-tAUPi6SbRWuviJffryCg3o08QVgvsdn1smou7VUgA1MPH7Zp2Ju7_8l2Ye4Kbe6MT7rnetfSAdBgmJxNoNfMqPeJTCKOZ8wsy1aWY_W3DIcfZfmsJqDlxx9v9peNBZCV2tA14T5j9rfwYsl8wPhuWiqEcTIJE99D8h3fjHSLYdjfMgfc6QTpHjHl28dvYUBvw1V-fOxCPjTsZ_FdBrqTq6BZTsTyu2W45u9zT89NBFig-H43rwMxLpGwbGbY96Fv_iLYcaWBTDS-vyo-_kSkTkT4k1nBOlsNMwNdaZA4xIe2J8txCRgCNnDMpsw_PD426kQSVuyohM82cFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pr1ZyQpeDe2iC62h6FvWs2gqBYVZMJjkGiFvTBTscvaa-_U7uABeHhCcol3_xARNPSdsY3DsapJ-njduLF9rzZcKWy2jrMmVNG7dVDrkVqV7qn6TvStv5_qs6CGOBDOHuztnNlpekaT4WJTfEQn2I9veDfJo4US5WBC6VwpgNqiMyKoW2_rLbCLNH3RpGGDvS-rfcxHwwUrLLLbSkT1hqlPV6-nxjdnL4n1e1ulU0jpTZM1sp73ytJ7wRVXcwdZ8BEhSfRwSQvxRbtdkoNfMbU31G4UNCe-mcvQgocc7dAsviGt9njyqt4C-NpK6kwWQMUHS20EyUxbU3xx_D3d3tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HLg-poO-R0jG4lVPugVRiMMn-cpwhj_fHzcRBNIQxzBrapsXsz6PdH-Ln77ZePTs840ixCqQGfo0CgxBl3X_VOnhydQLDKHGFcRbosWjFEsEHyBRRHPvHRBjUNPdj1iRKrwOInW0IEsEimCpPNJzPt930HlRLjKi5B9Q3HD1Hmz4FSoFmGmeIjDhHhVWMVR_KEcOHiU6V6jg-on2zJqdlN4PV-K0YLuEfkFKWjGoEiQwNZL4i_3aEUbEEgmacfkgPdBun8NGBzqfo0-hIVjX4bbgjnmWft4GQIILlj-7TmV_4_n4lmVcV85w45G8pJgMP_s0IuTiL-BQ6qFbvFnk2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zs1Qn5QpmY9xSRFLy3eZfmZUGV5bPKpgxLsvBMDyqBt0iZg5Un69eiY3c--CaGMwbeYe4EEsAnxs0KTOFpgfKbJq9ujn9kpPvQfL787wSWJQNni5qBwx1OmxVQKtvnGvto1gXpVKGTK5NfrW3EkqQbrHKQESkT-2TWzTp8dwcYcRe3lkdKNgr93g8wi8tZsskVwj-B178AP5UV9OiqBiJ2Z1wm3aRCv-WbfAIlu50luz3idG1T4PLohB3E2_R6gYFfI-NBDCeNUlWZS2-8GLR6EyUv9AeOJb19E_r4uu_6yTE8ggCHlTIvCWJpicpy7CvjT9zYXgigC87_iXnQaBRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJHFo0GgmpEV-yr0pabh3-ZOoRESAYbnzimBqy8Z3ve92AnmkezIMEqTMoKP_LkqGyDayjq05vwv0lF04bxY38vw3QleRkTBdIqot7uU--WtAhydaJofGEf-YQN9V79qQ_5cHEHQdwhF7rWg_BhNuTZLm6no3EdeUCh1uD-dx28X1U0fqVSKpjWokPcJcuWEupergnfzX2FchLsaarbEQlc5eRXRs3HHP4FrlcDYSy7Z72vh_kogxuROm85bhoUJvMbWiiBAiA_oyita6atXpc75RXnMvQEVUZlfI7sJfp6_vnDNvVpfjPPZL9f-X6FC2IpFLBtKixGohESdFKd1oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7-ZvcfV8rQEwTZ-GJeYzlJEuQEo5-b_lpehavW2-9iSiniXJ5lU9NoI2DO1b2xIvXTF3QVFlwCYBs4JAl0HlitywLxgvYhIy1mY52F0eRkFBHVBGeqKW35wg_aUM4DSpFb00ca2ryzQHtlD-fEcFuBZ6POY482ZSFtYWOFI5AvFLcyJw36a6KmlI8ZnlcEa6jRoORYJizzQjqkv3edJXO-GovxM2ZFcw8dE281MOjyZuTg-VPTrrMg5W1osNshww8m-G-d2KufI68kN4ptWiJQXaBHBEBW_daLlxj7PimbPSwdojRZKYDngnko_fPJWcagd0BPybuIuE3EBoE-H4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btM5luqWPpiD7L8Q9gpEHWIEaqeD9is2_uKA3m-1ayoXSNc2tYgTiBg09oWAAznd6IV7iWDWthchQL9W4puMpVrGD_y-nxKr8gwahEin-qNIrkaH32FFMkkNTlz-Ca738Lb656d1RdpOfD6xbNE-BXdoGg7zNyrI87VA3JLBkj6P38ekg7ZrURkP_13W0ZsChfHPH0Qvc9yu-kuJ67kr0n89TthTdOADJ8-eaMs_Fu0ZDtHXJOn8UMHxxT2FfdAGjDd24wLtDV5s0ioVJUecn-hgkMuofXPoV0sUOqcXjmXPfxgHdl_xKkSzTzNxPwjQbXzsq1LvFPUGIEyEVZjSlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeUXWGI5N5A4fWpgs_MQ1OGlnmB_KJXJM4vWp3wbDkLuM0Kkalcs-vpTq8jQTQDYx4PxAKnmbC6_WNrBLPorck6PeDivp7AIKxQLKgC1JvXScxROVOCjaHwEscKNkAEw_nW5R1l93Gi_4rGXwLNMocRrmr8PjBpZmK-i3rILsqBQWAO1sEv6g7trZe6llBeYFtICxkhOaFFkMQ9eogGXFFFmo9TtHAon4465ZlUlvwpgdmN238RIzibWZcewcbBi-e9c_3a-3P0JfmVEHfKk0SRf_LwZwTBuRwC2az8F9k1Gax79i3JjTgYkvPG7Cq1XdGNfP07_mt0BFrtba3Nhkg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=hMWVqQyib8g5BeWls1Yu5yL6elomxqJ3OU6UBTcSNMjqcpqDoqSbJLQzRojeuxHRN3Cz_21MQrFcXn2Bk-1xiJhWBF992Ev1aWY0F5s9Qs9WOs85P2Z7i-M-XNOtjA-0QqW0EFROzCQyLsAw1PPViRlvdv-_xmoeRhRFvIrdrpSujmV0Rp0OwclD0v7GJjCXPpHCDBmBj963XN0MuS8HxvjLmukHrTPhxf-9bTFNLB0bpv2AKRvyYU96aSDN-bJ9Z8KqrRGnEb1hv_8g2fwbBwjTyxrJl0E4wGo1Psutb8m1iNR49v3HY1PgjXttJDvvl0ROqu5GbqZ_V2HGKTTW-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=hMWVqQyib8g5BeWls1Yu5yL6elomxqJ3OU6UBTcSNMjqcpqDoqSbJLQzRojeuxHRN3Cz_21MQrFcXn2Bk-1xiJhWBF992Ev1aWY0F5s9Qs9WOs85P2Z7i-M-XNOtjA-0QqW0EFROzCQyLsAw1PPViRlvdv-_xmoeRhRFvIrdrpSujmV0Rp0OwclD0v7GJjCXPpHCDBmBj963XN0MuS8HxvjLmukHrTPhxf-9bTFNLB0bpv2AKRvyYU96aSDN-bJ9Z8KqrRGnEb1hv_8g2fwbBwjTyxrJl0E4wGo1Psutb8m1iNR49v3HY1PgjXttJDvvl0ROqu5GbqZ_V2HGKTTW-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSslVJI98osBUzUBT_VPDd5K3pCLbxVBH161fW5FnljzggSSQnEu_1H07x9qS5gfXVANcQxd_MEly-v-9th96ok6QI3q0aWlabNXwjFCWSiFkdMC9BBfmMrZeFUpoYe1B97K_KsrpId4PAA5BxHJUeCn_Kuo2URb-1duUBQdfQ2tUQt3RBdwELEyMETrXem-exhXSEwmfU7THKoQPzJdfraqfPeS-3IBpZZn9HnrHeBr0YhZwCjg_b6kPhI_YkfnzYG89ExqX92-aKK0bcIzLQOBRes7h0m7Vut_Eg00UDTUWxRsy5wrsItUO_u6aWsmzWMdu0Dj3qVv-oiN2oHrwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvZLIvybTfDyGrPGtu5iPtYQTKl37NKShckAzOnsqzvnVRyxVBL3brBvlydDEnDuFSiHORykalYTJLcdfkCg26qzf9b1UeurVyygxCB1hnUIQxo2nWlPgiLe1SFLQ2CWbgP9HSNvAaoxfgWeCf7b75eUahk8XUeesBTiWkEwZGzr2ynHaUjTO5yF3nwQpxfc9X_-TyULD0aHd3r3Az_WHUfna0L-kHNLIvavpIGeJqX9c_wd4LjMwwE1yujnYvtvuniZnGeKE7lTZKU9OUt_3q7vB6w7TVNZ7iSMC8v0grAk__DLp7_K6TQ-q8OHu24YxjS5PvxOIh0-pyiUCzn65A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0HRr3uH-lcYYIt89ig9doeoZFWe3TxX4P9at4dNsODdOUYvPRzf6qRh1SJ4j7-jVEZcHsUK3eceTZi90d_W4aPsqP7v3C5fNqkIzVgn-7Gh0z7yMv4s1e4gcJgU4W5kDF7_yP9OWJEj9nAfmUJHwSjc18T5UhaQ8jGobqTH5sFsXxg_EanzinJVyrea92ZSz4EMQamx10B8kkRMgpKvQWpnQUMy92_aZD3X1oM6PgxpJVe3oicDPj05AsvNqGGeyFRKtlFB3maafs-flfjlM2zaEzy5l4yAnid0DWWHG5AXvxkVqtsmwOWQQugqGyP0Zio3KFcPfQ1y9jCBtZHMCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8CT3rW68IqXuxs093eTRwgwL9waGhkR_LNUul8G9p58Lz-4zIx09cj9YVQ8Yf32fua8Yf-aVV7r0omfWriZ679adsrriTf4Cs3pTmTyGYdFJ_5yoFlVtfyjx6iJULpd7djgywJ3GJr5FglifMEKLKwgzuPf6Ldzx_lyhz0s-bGyvfJ3ptMn2-ucfpAy8Y7dnBVloc_KJQESQ4M-mJA6bBlG6Ew-TYF3BbpJbFxNnlGN7GV4ASufrFaR68E6sH-9-I6DY756BGIC6x0FW_sDvfI0BUty7i7iVIv_CusYP6L6v-Aa_Wu-0RH8Y5nEx1qI_Tkd22otJFFq5VqjyR0tqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRwOxXEsqYOAHfCKJY1tNLdurBQziDLkFNq_caRGRfBIWAisZI1TCmMoEdtc3tIsjgbvyyksBwz5kzLqqgVsBsQKUpn5lXRB7kJhiN2cNnLrrn2ilTrYLeRgU-3F1TcO_0GVOXDaeIoeRAvqS-kMEZK4Y71CMdvJMDbq5n7xBPJultknNPF-XURwpiELIPYviw0jPLczKkFJqDeDWzAEoTU6g0bqnlxfCUOcjfj7my8y7LDG6E_M0nQ2sNo3l8E7zuZoYL3rMKfDZJjMtsCbn5qtYa369UpBZ7dcbn2pme0olicyP3_3A99j1qXhE4ys1w_--0VEQVYIeeJuu1cNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0gYckTVgpxm3xUnuC3ZnKQbNt9zJdNqkHJH9VSUgvUISZJq00vFzbempAip_FbfQpSrHkvfdUfd5NvncdTTdZ1j-6cq5_D0Dg1Ej_gLteDYO_pV7FukhbNppZZqqfQ2-umcK5P1d_pBOQ0w-USH9MoQzV5nZy032ErzysdJ5JOvWMofY3ax8AuAyW8UHLEwU7Wi4l3UNvtAhNNxVhUyDTXWfK9t0E1-XXvzfPk1NVC-2qYEd2B_gNJQBxWF1NDpwdL5L_SwCM1Vao6bMssrEpEQrHD-uC5V220PSXD_8QjSMyHb3urjju_AS6CEA7AJX0dqMu94_wJ4lZMCdHIL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgbaJ6qe2uYGE3y7pSo7WYuDRHypioCp9RQ5dRu5N1Z-xth1x7llTffBkCsjg1HZnY5E886zWdj9Hr_UtqhEZw1JgZckeoCQGYHnXCAfdVw5-3RF8mbk97g6VW7WgrekjKo-zioPT5q2HWjgQ6K3lgmX78WiMlS2WICOKAHJfZs9Hkp6mLUmnOmxBWfTRJADeZ8YwzmCCDM2qiUW_VQDxDfOn7uBsMfU-Odf83aaZs6oOPm-X_3NjlJ5wER7PCbMWkUzPaiOKw26NBTuuTkqnSNXadadtZ_wD-jMM-kX0ITVKu_BRCWDur76jgXhgnk0t3LRPRlYH5Gqn5IKZY8PQw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=VymaE1IpAFiOXcXN9cJCFFIBn4NtdRsrEuljRc__wJqdBcA2isFE-mQhcI3suL-jXjL6WwG071StrX7d1kv9_03NdsEqFi-aLkGit1aEwrk9RTo9tE_VnPu_Y2h7ALpbIzBMlkL2sgJrihzu7AsXJineiwDeDsiAldr1OaoVEMpiOEWQW_2BphOATlLAdB_CzQLchmejTHDUKJWPOFSLvWVRKzEhMXIhiavWro_NNM1pomvdQG2YbkDSlA1pBuAyRcZpKyTSxEv0fKWQaEnUfLvT25dna88IoEaLAXWDjxmboT4qG88KEoe-ROc9Pdeb45cebJ7n3-468yCAxrLC0rb3gCiJz0hyk0NVs7oga8CNQLnf5p0faljs1uYr9cYABvtc73qSe2UqkSViFET_PZhhJ-ixWTXGdQWxR4QbHYyQDLKfBS2XKq2ors_CUn3tRSiy7EViUUf9RJZi2KIABmtSj17o8SAaqhzRNhLvtuaYyOgSJn8nlK3rq3fDePEjlfIB3ig4hVkPrbrSRaCo7QxAdCeZ1Ar6P54LHpbEak_8uXoeWhcQo25aTe3M0z_oWvkjiISiLARo2ThtDd8ufE38-vNQWWKE5xsYcoQ0C-eK4qH3W8cKMdG1JmFxqvp387WnP3KlZN4q5uS8-GwZQUkD-5E4NUETz15zDwsctsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=VymaE1IpAFiOXcXN9cJCFFIBn4NtdRsrEuljRc__wJqdBcA2isFE-mQhcI3suL-jXjL6WwG071StrX7d1kv9_03NdsEqFi-aLkGit1aEwrk9RTo9tE_VnPu_Y2h7ALpbIzBMlkL2sgJrihzu7AsXJineiwDeDsiAldr1OaoVEMpiOEWQW_2BphOATlLAdB_CzQLchmejTHDUKJWPOFSLvWVRKzEhMXIhiavWro_NNM1pomvdQG2YbkDSlA1pBuAyRcZpKyTSxEv0fKWQaEnUfLvT25dna88IoEaLAXWDjxmboT4qG88KEoe-ROc9Pdeb45cebJ7n3-468yCAxrLC0rb3gCiJz0hyk0NVs7oga8CNQLnf5p0faljs1uYr9cYABvtc73qSe2UqkSViFET_PZhhJ-ixWTXGdQWxR4QbHYyQDLKfBS2XKq2ors_CUn3tRSiy7EViUUf9RJZi2KIABmtSj17o8SAaqhzRNhLvtuaYyOgSJn8nlK3rq3fDePEjlfIB3ig4hVkPrbrSRaCo7QxAdCeZ1Ar6P54LHpbEak_8uXoeWhcQo25aTe3M0z_oWvkjiISiLARo2ThtDd8ufE38-vNQWWKE5xsYcoQ0C-eK4qH3W8cKMdG1JmFxqvp387WnP3KlZN4q5uS8-GwZQUkD-5E4NUETz15zDwsctsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HDW_HnHTuTydErIVw9BEGIwUnTCJ22hEVU60Jt8CDYrifyKuPQW5fBYt7t3UbY7r2gSVf4qjjoFnNf0bflFL_kby9MzI-cl3akfIAibH4pgSI5WxOLlKPP8hIWnrzcM1sk1hEhBmSf4euLVtB2gp_QXyHCl9zhYvEcD_WqoTYQOMkU9x0jFum5YE0Goqm_h4EIzcsDslIcBNR6MBAJDKPSExP4FSInzHO1NVg7oEF_6d_v3xStg20097EZU5BeVtef3osUCiMSJKbrvlGrXCRO82-USh_n5Xiz2oqKspnTkQyTl4XR12E7RHDJ8G6FR_tiaPsKhkd-P0w2egp27jIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JCTIyk4J_qYaZbJOCm3n4Covid2eHcFLL6BQ1-FssrFGYq1lXK40YgHMoXU7U8T2wTbSb_UQOqhusvdEDU2I8BVvU90vC2DhV6GN1vppNkZoAhhykX3-FZl_xlTYnyC5MZxuTOaNo9BsekkB3GUBm6zuZBAA97Rb6eACrIp-GnQ648PFe5Gs7UpP9MHTZwc1asBVT133gGhMcg3-bYmNSOjXMI09VkydA5kfqMpxXVBOZCDJgSFUovrROO2cgZbDPHmiMYWV_ZApfjvga1YKtaotgbMJoJpNKSJUW_r0GS1avDJbT9Z7WZ31Q2tn8hg8DlZfcjDoD6uc14CVzKjuqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XC2EDGdkByjHBuU8xBt_IZw-oP15PwaO8fcOkNdx4c3UmsSC_OVdG4O2H7AQcArF-6KJmTIh5HlnUwdQyT9UEhMrviloeWLWpjgOssH2LHAoSWd7OLKRn4ZBZdjD9tM6d0_Vd_UbWtKask_b8CvgFWB1WIVMPHV0DS1q7KIH-TfKM5JZZhlBvrcXphZ2Zyyz-oUGZEdML3N3A9TvSlVZD6k0-VWM_0EBbLa3fGJYKBToGHnUDuhEPGcei-PaIq94o0K0j5c6JBHYT9uLdlL5fhs3gHoKMD_bqsrFn6zmvRrph_rPvthGo945L1lJU6BSfK7rzr8VyZqrUcR9Y7Xlgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czM3ftF7g3IMidBqK3JVtFSU_bRLRoc7-NcUuw3lMnIhqJbNSEOCltq8Zp7VcAqNcBVsuygHA784elCxPlQ3E3ZvFGMUQPdMRCn2FJPwfBT_QfhLAY5FS9LNd2BAS5MkMqqepdp6u3WTV_-nS_7FZR0S2UY8BLtBll2U1XQa9zbAcDlQeLK45V86BiML9gWhyTfgJl8UWX1MkoY2DinLF_f9tbbMsqvg8CLUeScsQZRHEcTbIrfMRk5QTftjHeg9AVB7hrpqxd5LZn0v_QMWcq23P3PoF3b3DmIwRjp3hoJbyzxvxL0THUwdVa62L1Si3NflpKLhkB7M5ODLY3Ukew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEu9fgdQ9U7jTVlSnhHbgmTun0GiM9MAQ1tZJsee4iu8E7jKwMRLjzUXPZgiWSf2XDFHb0QlCSEFhBNaVJ_24U99ZPnFVff8y8K4GGwWmsUNFtvIWt_OjyAQVojzyw6Z6RNy7s8oouDTEgeJW7ZcjfWWJN0JPwrLV4Z0NwCAjW6fTAAzrr0erS0af900CsJND4gySzial3JCzZGnTlNchARE2031OvnDlDpF6V9nAE_i8mpejorxuAl9qWjp98VyqsclWqIuKsCq2JM17n3-lySe3ruNa7Webgz1aOt62XQFRcaW_u79vE4sfY3FmdyMLMCjbPWcyhnkhpwZZO6qNw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0bmAr1HB7U1O6RMaDZuGvILRtDBcI16cjss2Ot-CsHgY062Rp2fp9ZW1B0seKk0Dagod8yUztLNBavYHCg0yNTtBtzO13m4ZMFWnur8TiA7E81ZVz8EaejsRzeIl3OFSishMBLG6DGPqG90CPGnOKKJ1t2_elyFjBVB-NN7_5NzZO1e0c3lan_jor7-cThokW-T0Mq6Qik6IqyqAZkJLCIueeeeMwE2yjE6qQnLBaP5p_fqzfwOgQFrhbjdFhnK_DLOgwZQjyV2MPr8FS89ubi-teG1j96D67exdtfP7Xoz58QfmKdICtKtiSbMef6AYZpX2HKyMiD9_7ewTfkUJMDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0bmAr1HB7U1O6RMaDZuGvILRtDBcI16cjss2Ot-CsHgY062Rp2fp9ZW1B0seKk0Dagod8yUztLNBavYHCg0yNTtBtzO13m4ZMFWnur8TiA7E81ZVz8EaejsRzeIl3OFSishMBLG6DGPqG90CPGnOKKJ1t2_elyFjBVB-NN7_5NzZO1e0c3lan_jor7-cThokW-T0Mq6Qik6IqyqAZkJLCIueeeeMwE2yjE6qQnLBaP5p_fqzfwOgQFrhbjdFhnK_DLOgwZQjyV2MPr8FS89ubi-teG1j96D67exdtfP7Xoz58QfmKdICtKtiSbMef6AYZpX2HKyMiD9_7ewTfkUJMDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNwakzEdZXCi0koqWlnAmKuMLuPH-kHokHiwGbjV8LNvipQIwQaTeIPtnsVwz4fup2dl6eO8BpGWqLShxquMDhYZTXV8IGxQqmkgAXhE0kQckG2Zb1b2On1KOQF_JMVfIJLYapsHZQ8HCsyZF6vKFoM_HSwlwWAcTKqwC0Yk8do4cYCoaCFzem14IQ36wQeVSZqxF_oYPWUpS8YvWcIJnm63-IriwpH4otHuBfA0KpXAN5AqcyIzQbBGY2exdh07CzIRlq12n5LwIPcjK17u13tGpKo7Kv5EAio4Dr_6ciVMmf_CeO2U6wdx5020C-O6K1n8XXuvZ1xRhdhMfJsu-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzQKETWHloNLnyUsXpRHKmltxfpx69V90htZOKhXZZykBXFNN827IsbnRWVom6nmBWCu2lIP-KvWkM-Uog-q-r_RJKrDsoBnrccEpoFT9utW6FVqMDgSk-waDx5h-R806k86NUgdMosWkrA036zGXYtQexoZmbHKgGm__CmciBCAbFOjT2acgGdDxGHwR3YG7gh2iOCBjlLo65_2nBBD-wo3Og9AjpE2IzWyUVbVP0IdngFphDfBYI9RFrRTx1KaIB9gnWcAJ4g5M0zdbcfbyJaLOju_K5nOHijvC3Y7GIRtNpdAOazUBkKpbqL_4VOtQfCHC2ygTRVsSTRcK1pKXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTO08nOHKqX-TSAQ3EMoZDQx1G7GTkyVi65zoxoC5wz_Z7waeMLWwdAEyuA_soe1_Zj5V16vjiT6HmB3Ugk1mHU5tj74PHaA_u_7XLt7txRDYXvSoN910NST6pUvLIR5MplB8ugCnTRgQvhZeKKpMH_TpeD5HyCyrF7pgM-81cr5i1H5WTBH8uZJuF4oosLoOUoD2dzIjE8ZqY3ZiYqsRNbdbupewAbi_FjoK4W_wlu8V_3KYGhGjzXD_Ijd4cXRL_mrhhI8U0e1M1y020cCzUB1p2t5VPTJVdv5Ny1Scf2js6k0x4Bje-RxeDyyNQQLakQnqbCQXU0ZO1Qzz2y3pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZPRd_AI50cfmNGt1zv23AoYjT2qR0_eH9f7pom9dmWVFqJNulYxmfDomKtRqI9gBLSvfhaF-PQnRmOJbJ85gGIX-skzL-y-vuhthvRPLf6mQUkr-f7QtZu4V7IvjyHLXts3Cm0F-PLNr1Fy2IdvOPdE-S8tZaQ_2_fJl_R82-XZIc5q4XCvd3-8-qRPbFS0Nmzrll8HYBuCdu5UU2FSjZ3luO2h_G9tpT_OTYXRqFa6XPsU-dF39d-Y33DO9_1nZyw6AtyGkilNTTrcOOIXSgCvUBK75_iZRo-9Rg_TAfuPrZscIfgVkS5nEh0sJWBvOoHC2-vPnQftxzdRoMJwJxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/chtYoEkQBEjGxC4PykWxh0ngrCSu_jfYWpIzZA00I7G0KqG-Biij0JKeZfQmRUfn9p641WSEuNTDIfiqg3tYFrbPG2PW0znrjAwI9OKN_5v194_UivPaM0916DLYpTLWc-uUqKzmZM8lIcpY0KnRJXECnKRGEjBnjpQFiBDryhVbiA5lsJ2dJwehUUrHpuUbaMukj2ZeBYzJGYEwd2hp0pLZKpqFCjKzgBzLkFnRBwJvKnn3qQo8vB9XjQ2AQe-Hs14zKtiUalbf61oxQX_kweQkx9vSG_hCpJTknUMdTke9HUA5PTDKOkASBbuyMeWyzDn-4J_cp_K1QWMqYdkFUA.jpg" alt="photo" loading="lazy"/></div>
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
