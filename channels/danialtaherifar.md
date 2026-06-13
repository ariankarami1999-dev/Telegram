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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 08:27:04</div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SowONhEcfcwPkl-YshJRxklrzvxL8SmLMI6BvwgQoVMLZbDcpZ1oU1FfHI-8SRaaTvNiym1VexbxmUK7FY0y-ZAIX7rOIxekwJPYGrSUwMipn5cuPGl33jDjHJZDYU5KdblbI9HLeyyB2PriC0oqT9KifMHtb1crgLE2HVsR84XZYSIsI2lxPqRgvWESxW8aisNJy1WoXbnZC36Yq0d01tk4F1hqzTyDFQB7z5kwjUWYB3_k7rjWaAxm5LNpzajXzImSdrXW6YMSgooz6R_UEcjJneravFiZJCRBznwMt-Y0eAn_cYssTwB2uZgiRKY10zZ_FagH7YJykD-wN7j6Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdpwWVkn8fdBRrd0BtTHrM9_01BXsEZmC5IAMO7DzVkFj5YNFjKXDPKOpyJagilWZG9NktVbj6YQ0trKlOOEJsIOcZeDzI8gJ0dZlzDHn8BXEyWf1HjApXBUcQFZfaKUNtghdpxT2tFkq2brZ16vS66qn3fU-HFPoNP7PvffW6QWhq8L-QG1Wvysqas4zLn39Mgu3aSmG66OfmNJ2RqVGKtt0e8Fn2QMRS8I38Zoo5PTdo2wPkjSAZYev6qXvcKmB_44-4hrnTPotzIHwK1vHNqGv8orkw3Ud4t_MGfBgQYoVSUzv2ReedhQqPCJBbvPgbVv5fvpujG6Mn5TA21clA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXafsKXvxuLyu8spKFAxgR5dBEW50OPwu_BhNibGtM2pvHxgD18vCSNWrNFB0KLEwzoJrlVPkCyJRIuNSJEkqQ_cFNdPnt25-mNYkumSflPccnnic3mK3Y4bxo-Gq8DmRGCVuAs94u-rDsk36Pn44khcQUy4Y5tHaznjiil8_aEKzbBjbNm5e_zIitUmVeu00G5o5lmMCfhc5DETh_gwRt5R2dvLxx257omweRQPYnyBcLqkAoXsa8uLvr4kH-HuX-avuCOsmE8ulZFyesDdS3t-uVkOEKyWg6kQGEDHVyw4PwqiDSpCCDug7-Q4AtO3kh9k0bka1_CLQH-hmAqhtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHaBKuczTKT2g1EkZZ1vqyHRChK9csoYq-Eoq_RL3sjNClz-kiJNSVUKtlSqoUnWRb-ODSKEZacsBVVB7uKAjuGBfDVpNrJiZUhQwayiceIVMuWx_FfNMV47ZyqnB2HUUaxubnMT2Sh-8znxObof5uYElMqYqYryRyL0b6ztA71NTNOamkn342YWEDgiHBjJVZxHULMEghyJZZ6k4M-2D5WSzJWfHpeW7ELV1Og-g6F8tdMrji8jfdsKtzOzjOl8FvF1fy-SmFA4BeoJu6l1ZNL04imA6MWndZSFJjaDdhIlYpN09L_QnJF5G5a5yS8JP_vXfPqrbdKu_r-lnzW4pA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 822 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYWkpv8E2jMiY1UviN5kR3h-SFGkADIGDaCeM7cnUi9EHh-VvPzV2LSh6ze2ihK0CLTZyB_6D4-BUkUOV6b5sKHrfB71E7N3cwdVU-WYi3sfu3Q1QABer38y9n8Xggep2MlfZqdzUPaxMAIrgpyEl1s7GVnuGV5m7VOqCdqYeQTYh5cWtrWBseMRAvheU21ZjctJVSnRYI2sTTyhMllgZEJ4ZJrXm2LSg22s2EsCltwnEXbLOnpdO8stM-Xb_OYjWPhr05XjygNJtpwa32yA_KJeA6Q6w3gD9vBRLL29o5iYHCxOE9TcZmrxzjPxL2Sj74QF2RDD9BCmiwxrj7BDYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH7jJZHtoZHUo0TUCkQjloGRnOm6dv6ICJBgTzMAyomjQSK2OUxbACvUDO2VMCaJ7mPAZuCeXqDuiit1YSeRA3B9b1b73mgu78FRSP-oj-UFDnyqNY4O8zfXU_fKaugOjd0dYFmB1YsKBgz8oAzrXp5xt_YAVqeEdLf8T0A4dL75CgkRkI7-qfiDPpld39gbrlClOobxDYmDCTeTXn-8iRFVZ5Om1kxlDpQlOLHw4bsWeWXVc0qo-Lrm6QhDXQ1ypKI6nrI0GjCXRGFrXOiXXDUN8EWpXrEl60DwzTX3p8-iSiNUIoktsI2UEwr8ee9QICdg2PnYJLq8JmhLFCyfSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEUuqUpBElYTyxQAVHAmCfis-quG4fWcBdQFEwhh9sWHhM-jpYFQFfF5KLbOEQbH9_6mxUqA5huId0zEHBAr5quCQiT4RnXTAorr-p3lYL_h_2wESMxMqsAzRE7z6puTCHZs2g4ZTxbIxdkP9nHvR_7DC5hIUw877OQgioMUCfZRnh98XPCQ4xQvXa96DB_zfurPXwQhTFIw33hNgoVpB2hYtZlMvErtQYDJlRBZP7ozKYkLoEMg61_E-0QAAwkxsXrOl5iujOuvyWbeAr6TpWGLUt2nFR225vzRiF5-zZ6G0OJdzMIx4DVDELvc0Ax-FJaRErYSJju7hyG2P_nT1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RGxSfghXI3zWhXWnINaGKwESifLFY2KzbBe_0A2mieMRa5drqGyPQ0NOsdyTBX8c2cZMu_QAJzUHietwvWgWDIpNfKgvNdXMwBGIcE04va157BG56pnkCULlp4x5W_Nvfo7xlEKcyOvOx4D0fsOkARn3pOeyjImu2sYo4usYn0qDrtIkMkGnInmeI9n3pWQ9CBzq9JnxJf7GteS9pPRrELXnXQOR08Pu_dnrRsDHwiRCP9c1uo4SezX31oa4BHaw6a4aNcPKT8DDjU5dg6tX0D54mhaszsabcUnOXBOVHUcWgZF-sf5Upjp9evTa933HRqVsB4cfFlveNZFmyK-WwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVoiVIpXvSiWnjw0tQ-IKwOTqkvCiIMhuhHNkf2fAkm6C5lH7WdJowCjuke582k3q1GYiELbov_LuxpRipJifZZNpC-g19ck6mzvLX0kcmRKBic0xBsIBLIqC-4DCZ2Mp9x8wsFlJ0Igj7EYR5B9kxUh-B7uI2v9BfNaBn6W-0_UvXrQLyEN9Cxd-pzoRR8qJ_jIGlFxr5TYu8bzhSx6LIgy3R1bfd3bB_lDc50voyWJxY7xoBXU0hygEk79JSFAF2fDPwOp5HGYOwwP19FtDaFtETpm_hcDMfKgwSvY5-U4ZmvGaJLzgG4Ncm7SU3WZiKiI9anNQe8hCkEZMt4erA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_X3hbRrifS9b4H5Q_4yn0T7_J1S-wJgtBudHygYdcITxID79CKa29goIaJterNI3fRVSPGP1QdYZnlUtxPe5fOEbL39ZkzSI3sSyQI2AtqU-P5lWdNIlW957JN6jm536zyDj-UKhqkSxuH4mQck-ZXylcRwTuGk8WK_ZsXvMvbsFPvCuqHUgPspTGFgEBr2RQL5jLWAzNQHuWALKTwpachyBEoLk1Qhrz1JH2dyrgR3sIbppFJn0oW7GBhy3c8zzcPuDcvYOtylVXcd24iMRIGhRu5JZHlQsU0BnHIkRIIEP4t-QOfARg6zPFo5vD-p1xt86BpgeWo77-6_v4LAOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBp1WTAY0LCT7mVJ_h1-S2CyEp81yFm12kkmmKx_id0O52CeTk_B0wEld1FA3LQssuL_PjQLUoCCuDETXKGObUl8_9_gTcf2d1R0MtLkiIMcXqh9x1J139euo7_VOPT7_5kNMhFqXKlSe1WZ2YYnJhLA2X148GPXO4ywSKpcYcLmSgSUuOXbik-BVEDXlItOaqeQ1ZtdGPvCWRxCYCDG66IpmprS2pnR3kl0VgpLJpnRN6aVZoLmWNC5_1A3h3UmV2gVtm036t1NC_swcC1rrw-KprDyQpQzwDpYAFhUr2rRxiPXkmVf7GPozZYLJPP4fO09sPmVz3aelf85apYG6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf0CTDAp5dUMh896sYSzDHmbW1rrhcHMBpKKuPACwo-RxhBV6UHW7o9Rhzd9q96hIdY53fsTZz5r7LVKwYOOaJodRbMKYEQMbgiMFrgBHaDLDBc7GD9AKiOpSxgic1dCUUsHw4ZyMD-Q5MMstEi66b0MmTcdTfmn2-mwW5U89u9YnAW9Mjr1xzIf2A5ndzwfyi-eTl2J90qfHbVFamz3MQ_8a7b85wCNOt1n5iDrKczZQDxvsjSaVkt8Cv_kfHz0r490vfREsfvnbK9BRNXf7zEBu0hkn-u93RZKIqygyObkLHajx4zSpP_ZmTTm1kjnzVYPKeIuQF0_QOeK2au1kw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=ULrYdpvKytcHzfHJ6R8EfiMaUZpN7NxDUUlLW6j6a8tQU-7JzPfH2hO4a8kPXtfSNh7KkTQeApMR2Sw7VIeGmjn7FI_MqytrRky9C76I8Cvjr0XuUxFkB4nAMAazKAvesYIaYE6NV8W25vuxfcWBvcXzhkFu0sUksQAYCgkSgnD6_TYFcDWxTCYz8vwTCPZ0BJkGjFZ-tOXOwrRwYv8noZ0W751ZLH20hp8ILRauWDs6GoX_NrFryxDhobSm-ETa_RnoLfKnapuci7nACJ91THqdCTCk56qCr85trkS7HL-gT8ajEkyw1ymyzjiO_FSYufw9jwWpDZFiwHbtNqPBxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=ULrYdpvKytcHzfHJ6R8EfiMaUZpN7NxDUUlLW6j6a8tQU-7JzPfH2hO4a8kPXtfSNh7KkTQeApMR2Sw7VIeGmjn7FI_MqytrRky9C76I8Cvjr0XuUxFkB4nAMAazKAvesYIaYE6NV8W25vuxfcWBvcXzhkFu0sUksQAYCgkSgnD6_TYFcDWxTCYz8vwTCPZ0BJkGjFZ-tOXOwrRwYv8noZ0W751ZLH20hp8ILRauWDs6GoX_NrFryxDhobSm-ETa_RnoLfKnapuci7nACJ91THqdCTCk56qCr85trkS7HL-gT8ajEkyw1ymyzjiO_FSYufw9jwWpDZFiwHbtNqPBxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGrW0OiRhlZ5ZEsbx7WyWidEB4ihuI-_6o8sJC73a4VpooFfIxbqEgzqJAnUACVdV6cRTtaY8celkX7qvEVcWMCM39Na9rGVUxVFJYg-4A6ywShtZNI7dXlffYyZGaJhtqumpO9g8lyhnQv9nQcYsRQvKoKD03zjImBrGubLEM4GQHcf7uQCIlHgjh7ymeD_8WornjCXju3UCNLWdGBdcz_8JmfGDIQT9baOv5dr_kKH1rVTKnza5ShWohW72XgDc-MYqd31Uv_6JZdvll-dW8jWR0Fq21mJDRrOenazf30plFuIaLbfc5xO_iVblVF4IgrGiOo6fOBrmtpKOTWMdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAOK1wY73kHjInWPUp9U4rTiVABz4XBoIdF-qVh93Tmbu71XKikc9LiHYU_6E-8BK7IU-9Tz1BYkHAyIhXHnovOacAvBDQY8GpMWKyUFkxDxTVFqmZ4BshBIPJ2wVUmwNXomRr85E_Jd-bQt2zSOvi78MU1vp602mhxV7iWgcra8CS599H0hKF-btQ5yrqS1XMF5p_xPPBjKpj3gET8hR7dgWV6n1q5vVA_YWMuPs6D0oxZ-U5R0-zJqXbtuHnhTc-c8SUmr_aIyc4PezYnxWk190vjCswI6rH_QP60XlQTpVRTYddb1R3M4WcZHlJOkEgM7YuucDCPc738iRySk3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHrHxo_N816OK37W96scnk-476SUKN1WfwKtb-qKA71AXLNUTMo_aY3f7jbPMEsSn24X-INhrknRRI_h1DrNC-8coolaOWPnrJqlloWzcaTuuElv2uWYjdLSAzUjP5fCaM57KpSLYc3aSAcWFkJ1YMZwTgi8UhiUq8BHQN8WMJZMTs9-Zuff0mYf99VbnuLhVukIlym0fwlWTjAVjDZwjRy6rd84IVJ0DNRvhBeW2RxoqRmwM4gJLAG3PEyd_6fiG8RHXRJtyngRqJ4-2wiu-VVcNxijl1BgnV4mBlhoOZwedkRKB1UhokxA3j5QzDooi0p5YSPom1XWvEvR6ekzcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0NaoGaiVtHsu07nqY-v-so_IDhxYl022Fw3QPadpCP-I6AVT6TCSORZNBz-otMXVp0XtsoS6gH4nTW3mGDpbPvNYZ-PZs7eefRDg-VZUoAKtWZGW2mNPl18f4qRAsW-imaw7YNKQmc6ekmB_uS0Rcvboxc2iiDiZuHCFi_P7XKblZA0Fd5XoM1Yu5JOA-aqtKU9dtUhkBL4AZf0pdk7I8kZjKdrQ8pYNpjgv7DXL3o0TRFQOfH26G_Ao9OkFqMqINos-HthtRm803dbPDYogY0B4o5OyxBL_YpfF-juPYqGRIoYxyEv-LtQkjNLW7zpSUkGSPfeT2mE-1E09JmUGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEj8hgf9i0j8MHsM6lL9wgVTdE9FoTyUt0Y4WSUQPohTu2t8qTuM1NIovjq7dOtaQ0ymn0vGS9oeAY8nPyJRSlPnO7OzIStu8A1Wk7B9ROdMzfoZ6C-EnQcbSE0_ftaU9-FhR2urB6qHuKf0ZTLowfDrwqUy9WPGn1Ic7KmqlaVobfwTp3AMvjrznaNAlKWNLnNDak0mB1enJU02nENO0XLBJ7aYz-BR9sKGPKhKCqmJPu2SuCle9l8ZK77fa0I15-PWkLk-Grt5xguiegJksjvH-nUR8EiXn8uwL3i0Z5OH4R-LKAdZTasEaH4t4bfEBkD9nuUCjrLSskDtCylRVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXYUu2sPaoCjNguZBziTm14XpU6Inz7onGHo0YbBL6fbbj9gDZ49y7jobrhtkaFP-MJ9MTmSB3cA4mqqncNrdCYuwk1a3Pc3wNnYkpSOP_V7juh_sR1mVfxHHs6ZUfaWbpylg2l4xDiqekHce0Di9colUUEdm6_KK9agxnUBkwE0ws5YC387WtUA4b8SUtuwAO3pWosWNcKmkH-gLVoKapPKDFhB2A5zQ5UvYTwOhuDJVWJuLhgv0ZGrx2lziTuwzZgSk3WmW0oPKvMCR2e_XL7CYierwysH49CtZWbyfrxvWk9e7b5N39HJITLoCEbt1Cd_s-VoyBRSUud3RlSesg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJoUz04h2vmUhxJtrn_jXe6iqRWo4-KOrYog4JmPtc1mwPB8sLCz9w6TroxeRyNexevmfRKxysbNyxroDHjKQdahq7xjGXvWCRhAi5ECCcAk4g2miPm12HYwurleDGvr1bLgyKt-aMfHzC4dtlmA-MTTK8G6pVALrh6ovULwcdzz21TUDdzEeDfTDl1BN9WyS4Vn2n0g7feUh3O7arsOtK3aGRfSLU5WTCiA16fOUZ8bmW3AP3bc4poNYGuc-Ywv5_JuoQgnoA8AdOFauuwQGIDcK_7TQgitT26LeBvzy7RU--DRjweZNj6OsXD97HxhMsDlgBEITty3R8aC2BIaVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogHGxYqRfpd1QVjBHn7_C03gB2JDbXF-gAHN8xRL2IqPqguT9z2sDL46FOMZJaoYjw3xr-nX9SWRCVDZpttU-uKh167GkNxhd5XquDv_x-MR1zq0r7CMFJdrppwievXz7_9geEgwomGE7LbCYRvxE8TXDU7QthYBm9uyPMS_jNcOEDuACbwnBL-dSAL0RVE_UDQQkDon1LwLNlRE7HcHMzhIQysuW9F9zwYY0bG0sEJ0wMRlDHot-jjqJYIxFzjSJnsWLJ2U6SPtGKe8VNmM1ODi-EK0b6n3e3OsDbvp8pmohSn-hEVmVx9XnZ5gIUS5rVUg3py7B-05SQtWS68ZAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHLqBlQ6xA87CanInpUsi6QlZrpP6mz3bfgOM538SyCd6vO80ojWD0nfm-kN4IjjzPRrFhaExpPaNsPJMYPByE9qcH47VnQVu89YWM7qq4lxl3LukDq4ZzjVRgPtNLn4nuTly_J7HXnMgFQ-HRHTkKnZJbGnL_Rcp7ydaA1Gs9vuIB0gFXHOKsWWpKx8ywU3CBlezu5j0OdhdE5Vi2OujUBrechBwZvL3efVjHBLJO-njhc7o9OEawaht66OIvXDMtrlBN-QaA_jEhfVnwjaY-PkM_HEJJ6wG1eung8qCkxMzwqnQkKQIFuqaiEPO1_esVmPrCHqpT0z37P7-9srAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0CkXmEEOEJBkhf7Ununv4GrBS37CvuB9nZYxVb3XkeWnyPexlPONhooQCr9AoJkSY9b9GtshhusdGx0N_fP21yEv2HXaWwmstvGxS5USzAerryWTlyYYF9s1oLyxuHG1oW66uMtfqm7pAtRELlq55c31CJrKRifOlpS0KF72_1Pc8RzJRBuMup5N1Do2vsK3mVgNijCZsxSCBy7ex9uV2ylpqJ6dR086IkspYroQYMexowC_AFTzZh8nBfIJfVBz-7TxBq84hrKgTCt6VwQChDcWiBWRTQxPNkGKQvCgl8ZJZUxXCmQsOdYeXVrGO_07TNSTUMhOfSaZ1lKjSe5uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3eK1f37FO3cqsDOOrEobF_JId5w5N45h4rut_ueYX0ocUaSVpxOoin7Ceeh7JGwRyIobWC-GIRLhdRXmmu7A4ukI4PgYP2VxWNj-rzdEsc2iRFdu11lzYasYQdFHWLCe2I-neH8D8JdI2_u9GCK22uTVrwe9labwGJDy4awg6JAfrs97Gj9bna1vBBJnpZJM7pGrtAXMbuHkvSYyYUckz7BG4kTlKhl9VOG9plXytc8udiHaYLCnfNhYWnGEzwELxeeOrNsHaXaRaaskwnSTZGjKJM9X-TdmeqRPGfkMa2Un8fhF3EsWnU-UXInp3mfUgkbMVEugunjTy-yvCdkdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfTFUQBcTwhg4s6-eni279pRpJB8RfaHHOu9e08EG0z9pFj4mz56rhT8E85V6fARM772grSrdHBTjXlX1uLAdMvUjafeRWd8hU8eNE3nzcvcXha6p4_i91EGwXuPuSvkrwecd4TR7YoL5w9LLdaAbWXjn8EpbJ7PIRt_xqfv8UEvcz2VJlnTlKVfIbIrsnsfPIVkteshhgGdwlBVASywE-2lVQYNS-CQkkAz4rWVc1zbhgzKOPSMtv9v2RomGCpfRzotB-AN5RH6ZpxGgIWGVNj2XPqryOj3PB1eK7YS8T56UY8WH1SoUFUQaltaQfiqjqeUBMg5kAGmfg74O5tzHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/enrv-Bv_dkyUYzZ4hekVmyeMoDqF6cV1HAYJz7zloySr-kjL0HGn9cUOKuBtvZuV_FiXVWDXhpG3KAdgep2ETA2T4o0-_4BtKR1F2s14nMSV2nq557D3maNxmNr7jCKStC1JPb82xWa0UPpGsD0ZUfSliGvc0-LQeS30oIjsObpoJI50jeCd7ZzIVp9nmHfF4qUlB2xdp-hMwkVjEYHafiKJkGjXASq9ETy6zHmb4rYV7Y-OXt4FE6doMynFhXTJxL4OtteyUmhWi7heCo028NXR7NZoa_Ntl-Dv0qb_8JMjh39cjFWPY_OkNMiBLbzxGQyqUgnKdjWSOjx6uJGKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pX7zyETv0pv2dMd9WjfBKbX-Zgtd6bjbNYiOfN_ZNeqU-4lmL9-U2wTRLkep6kjrditHLQPguRjT6JeFmnz9gNdvTbZh2pH_FwuI38F9EfR35lvzXpcEwI238o7rs4ydC04lLDK0G559KuAd3cC13VHyIQCZxCuEYbayNg1vAPst6_Sz5gk7xfSgTaBW6aDOSZbWzW2dDDJIykSi9X5aWvjImiAYv8-RGOsEe-zwwRXiml_nVhMiEPNlUkJR79ZncIXbkhyMYzxdC2whjy0l8xYoPIxQQIuCek-vZK1hof23_CeYlZFBAN2u7Q2HvW-4uhSPz63kKZegEwTOPyW70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YM6fph1c2kaxgbyiR5kkvvBKLeSfZHm7oEYjnuNcUFtA992gdd8YlVj1jrcD31XMxWIWNmCgDsQXP_0m2Lq7Kf2fckWc9KualMGd6N59OU4lyVohalXKJd01VWuuCb9YdEt6WDKbJLqLzmBwx8SSOEEEljYBTp7unPZAwBGFtf7SkAon5gdSqq4WzfIJcz41C2gSOMKRJskavlo6omTfCLRLXjZdTuPHwJAQTA2yjxqpgSlu9t_tYYI1GOhNNFjYkEfG_Ay-ntS3uVTIxPRHsun9aftp0I9kkyTdNYFMpdIOjSlevPDmFfKitzVtd36ghEy1FTTVFZJpWF7MKAu_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BpfmAVBfdeW_maR8xe0uriwcmxBLZ3fe6qVgWM3952F3AX2W6yrE_lzYGRzGNQ-ksV8xlqoXQ6d9z-CP4LNyA9wt3uVRoD1N2sdRZ_lBPFv7E96W2jOATU44JCVcviL7D6prNr3umD5A1jg79trJKwPJYVDqG6c6LxS6jK1UkutZwCKwBHvFgo5UUaZu0jxKkypSGGNQ1qMFpUYpVFuEscBzPkWxGeNsK5ikFPPP6P-YPyzHh5jHDYVoNpQuBIv8xVDKa3qjI1YxaQDdQg0waQszRm88Eh04Z-5o5xmi7WYw7aA2qtu_DuJW8pw0k_WJqlEEyTZDKaaI7SHd7erTKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dedEZhbB6DVwoooGTDBoZMNHh1gEoBjmK5ILC4vntdznCTntbI4dbrsAOW_SxdnSf6pt6lfA5BbzxMe9mhJo-vygktdz6B1kBCXPLcNIY5829XGVRbQcnNOtNCnq30kOdO3WVURR31Oq4q86FOOhsAZmA6B2kHecujXNaloglkwo_Bm-cm57yKXj_TrBDw98AAXBlo3jqzRI0ydpNf-bEvKizormFzo70cghaWS4e__l478suW_v9Dvx4Z4_5lF4SrmJ8SJDUU_kL3x40ny3ZY4cgr7zP0IcxRy_0uKb51-T57qCotvPeiFQkbPZRwfbXnTgPjApFofKeEOa4OOpvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeYxICTfJtX2APhGrwd7zX189fY6IVJt7bJdeYk0UPTFoJLsQ15JYhNAxXDmc497P2ZUiZGYHniZYUwWsRqgR8s_o_o9NtOwv1fA9FBIGfC2Xa7Le74kmnkOeY3xgOZbw_mwHW17g_o_zjTvHs1aM7GlDyPRED_5bisahDqRPup1rq4oseJPUdASFdyp5anyR8d1HXS4VV7ksKHeM7qS1UdFNnbjVCZPoq8Bldg0niIt0a4FgkKyHf87ugTLmKNNY4WyYEGDZ1aGehyOt53ccwWG207-_neA666s9ok9ce9yv6wek8LxSr9q6xgYY9px3vqsmeXI2vTm5SpwNazcaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kms_ZSU3mjiqAaIBnP6iw5TCNbLpmA5u5gx3TCypTAOp7ZIB_S_lOo6ZVFUTuNJiwrP8zBbWQlUfwrU1dyl3noCRxtkXmk3qEcrOR_v-d-HX4VtHEujnmnwFPGrvh94o7O1h6kp1YpVnO1XAcQGBFwX30Q6JDzECpUN1G28vQ63KjjFnUn1avWwPSid07UxPmUW2EMSiuW52UBP2F7RUYdVL8_ZMFiLtGK10RMAseYkxM1sd3s1PAI2MW9M_RTKNmzk6i-LdzoQp5L-Zu3qT6MUPJBnFcySYSyyqJvigxs7OvmVFBlXaOJi8yDaTSyGAzpEk4f5tE32E6DfFIjV4pA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slPeFNYT6oStADPNh_QM6WnRSw5oB0mExh6KDT6E7DFkGiA4CCrPzGgaH2_ovfN2B4a9dfb_-O0g3exVAeY1x0MlvWLuiCI8f7oVzXEcatZFkrOncKWA4pax31gnNklwUXsQmE-WnUX47hIK3zh2GnI4RRs-_Xd30Tkcy1AbRxWT6KSQ18bEEIqorzvCbXg5uTfxW4TccMzsNhDAdd0yFUhdoEBO2h7XSLdcfI-2oDjwIjilMbVwC8jM2-l5rsRlNulLJzrj6d0yNy-AQf1JbFxCdRHT9izEAsGiTnPtOrRq8QaoVincLcBPhk-o9tcDbVj6OfKs_1UYcQI8cysXkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRCt1Hr5KvoiCRmasM5CXFbh--QIg5M_AXc09EHLePLq2srpCJOgMWEG7uLzNO1iW118vxmpUp1S8VVsgYU57mJG6P9eUugbWG_ce-DQoWi8zxSgDU_HSGNGB_HupNzKuz2wr6PytvhaLt6JE75N6s-sC0TpXaPBQV5vqYRGsCoebPViYFadiphNie_JeEfDNnKpGWIPXr9j_G3V0KJ8B_wI47fPGgc7t_2Ukqr3f9YION6dKwv9rSVqjghLrIPTQxpHCziMkxr9Go-2q2nB1fidbJEuTz0Uf7X6Da4iTJB7USJoTWx31HX-6BfrHVIzn40cbMwZkMWGQy6LJoUo2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BK04vOfqLGY2v57Vm31aAsgJsbtn0O97OBWbu20dLfYPXbNmQ0qzUeIbrK8v7BF-bUTXwA87Xv4bMat0-RccYQAz2JZCKrcuLw0ireKJmw6i3OTu2fCa7HCjKzlh9vJzNOBcwAwiLN-pah5AeESwI-hVzE6cPmWB6GTIgJRIyOQHtsmL19YoITQXNmbwkxf2LHCHRp7Jj-E__28ieg2jjTwC4uJjJus5mBuKT34dvu3-xPAEvQyGP4ViDMeUTOM0f6IjFTvUfzD1PgjeH3PsN_kTbkujNPJ-FetwVPpmKWfE_emdQWIwab8HyrO745lNqnwtj80-_eUJWXP9PxqqOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTzmgNOd8oJiS5Am07hae7ujsmjX270PYV-S5tgKpF_d4oEF3obb9XRH0HzabrrUxP9GBfu67JhL0s3gCpqkgQTMWDvVaGYicbb4dPBxgOu0s4dM5iIV2VavrPRgK_OtTNYXWOUiff94GMCu4kB8fEZe33CuS9mC1qZouWKOndlfh64a4J2TihYiNCBjA4VkZKxUlzqFhpNOmcLC90XFc62sinStVwnScTIBZs3xfGSeggXOL7gizQ4WTC02TGnLhw0qiWCHTej0RKwzRNyh0C30JrcKprv5_6TDEo01IUsagsJnnGYccaE1x3D34VoN_UHIXPfAFgGS0Iy81pzREw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJdebaK8zr8zaOmBCuwA3stUcqzpoXNg-xSX9xp-q0Fh_X1AJPutLY-grjwY8j137t1QCyHUq6Hz5ZLs7_cEOWw4OP0z6RCHyXunHKiFU98chv5I30NmaGVrBqZKMmBMBXT97DyncLTCcdxxSFvkmPoZo-iH2KKq-_gyCkVZn85Cwnlj-6V5BDQP-Xwu59oTPXaaYbiJeSJl_1GXsqKpykrE3TSOwBVzhAKTG2UHPBjrCBxFp5Jjd9771r9VEGOmtS66yPyav62XljL20ud-e9REqH9rmip7UEdvZtjKAdRP6Qbm2iqH-c3p54dU-TD0fWVB1hPMaCcbKuPlgVOjCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fe00uUTrncSWoaKvOSiIfYGBaf_JrN5ByDLbjkM5GDgCMZVh6w5UHLTLFN09OaaVdKtJ1Zqp1jn-vg5Q-CtyUhNu2213mXTeVArpzWv9CcLgFjsI36VpRSqxj-REewS9uzzoSVEv5y4m8yl7bMtXvMLtKDoDVwRiZMZzk0kmV6I6PBob0YjqT_HuCgX7xGhiq-7Gb6GoZUbDqHCtEHxhRekrbfs4EnFwd3yG-hKboPE_1_yYyWK_yn5JhQNqaOlRqNxTIpfSsC7pzmhCDtaFhXtCO_viidNMNqQOf9qvNJDhB-ys88WcYCpfk5-OLxrxl9YdkObtS5a2rg7s4Jhgvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok64hKUu70UICuNLqQmyW78sTGVDOt3R9hzPuNOqqBhZNOniH7iKSm4ayP0wHIJcMrSoUQaqDf5lv36eFHjcRmhFE2AAS8R-0nuqzX9vDaKljYERo4nwymliOe0mO2jtxTce8uQ4QffnUn4LcOIHAjPoiHTcAaf6y8IVJWfw9cYpxdsubGwpb1z3vCkv3Jqfq699bzKTDXSNFudSerHPsQ6Un6jZoppp95GTOnRpP7zalaMeOgtUo-XLSxgAHhxElNJKFc14fSyXCN303F5E6Jf77dmTfrtDodc5GMchzYLNDsd5CEGSZmJd_o1Y_iFRsQ8CFLseSGW_PElnPP9Ncg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2amxNPTM27mPnVheSgl68PlXh9rY5wvccs3wsieT4RVIKHCHogWNxY2760nztcmdDurgZIRQGe9Ib8DbhVkEPZMdb1MyxNTJcrXlYhlx5og_DsFHK-EAW76TeEZGapk13Y8Y2-zwyFso3OHEoEzxtFLi87MJ2xYCgosOmX0CPl5fgCxtQJq460-7AxtJBzbPWQtghz00iDZQaxUJ3hvn11vjRhboMa8_Qm-QmSQrr6L9l5wpjd9wT1acTejbmkkuFrC3GxC8GTy-hBXTt7bSrWIBCntdSElzyzrpVjbJJGyGKhf11iJOhWUnBnHlLk37GT2timazhRnQ7YfMPuBGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVbld2QardoLa0Fatwa9WfQ4X_MuxkzP-pqQ4hkoo801SMbeUQaMhSUbMFwXW8q3ZiYODY-ttPB9odNoCSSlk36WkJLDK1YPPBycQkf4sjWXlwZap07lkqgSrHhZ1D3BsUIif22pLxJb5PCy1Ul24a7mFNxczK0I3fC2d40X_aNyn3MgXxYQZiQHV2OlHB1ZB2Oi5_UloLh6s31M7HV4IPJ1JecB32pSwIg8SMo4KRe8-3gLEwYG1PXVTDGlfy35QkC3jC1rwCb6eZVni42CDiebchmSHq0XZlLpwAvFxJB8n3kuGHYYFo6MGQv452WRevJNpfKt7nCSv9FI22J3vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaNfj-Lz5-U7ZCCO2ShfoI6bbSVCY8o3EjhSrH9JR1zYzqWjTfiA-Uncrt6SbVGMgFCmH921aX35Qm1zvIrprneaofhHFmVFHIbSeeiQ4kjGSeNgoym0ee10dWvemvnDea_kxQ9BXtMCGqGoWql-mguf-qWBDFvuhlPABstxpLTuBXECYzEp_fuucW_5kvA5k4LTOWe1_r4hnurZ2ShSBD4ET1xm9mFC4Epn-Wu3WeLpnl0ehQ-IbFeMgUtUjQBfKuPFNmKIF_9OeWma9ueFXNYwx9SFLtshQl2LBwchcs5bZBp8uG-VES3GEJ0yt7YBFmy3in0xFYcS2Sn_oKxsTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bJUXGL4rgvFRGmGuX-ziXMbu9_dTa4vulFmF6ilKeL5m4IXic1_qylpFND6MyXZciOVlFvn6WSe4CNiSOasgTfnND-iYHNqFYKtBFhigRhgz2AL8HnXK9cOK-4NqoQeOBsROwu4UNPy_ua1QOzQNLHjNYELbeCp6-ikSEFSfyzYdnUrdZJJDNe7eyfaClRIxYKQ-iaDcgrUekqN57h2XW85HlMVOvXHdwWdam1wf1xEXZ1AVulVX2QmIEk7TBK-1o0Z1nbenJFONFnGu-bf-7nib0AExRSKzo6qHQFZRl3sf_F-toiTadXfH1FKaYf4v0-t78VUw7a5vns7v95HwNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKr8taAljmQ5kO5wYMZKhD9mO9M3GeRhCEFAuLoCWSpPfBirwgjeeU2JD4pddHT_ORp4s366k1xdjmfwufWOyHHWxBXMovehSbmP_UH6craztWdqQvsXPIQ3bh_7lxNsxU4d_wS907uV07jbEIjavdPsiR5Deacp8ST1xFKjM8hYRWqvpeOvNm5N3xXW-DAr09rSBvE1J_diX7j-aXrXzYdu_iPAR5eM1v6Bhp3V9dj-yWaVjGykzJzKYL6eVZC9FlLhU0Pb2j4uO94AGSL7q60WuMh72-rsJPkuO4gNKUZWr68V3-cW5I7cnXLkYyzENYPgRJR8HchiBAmX8c8FPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzOSeCt4uYZRRYQvwYdLF6y9pTJBDtelUUJcwqB_GLqjiBJYE2j1g4-qNUnlzOZRtobo-k_Opokcp6pxsUwMblES_jS7rUWK6fkWzuHc7Q0bpf1L8DvfOnL1fQCQiSm66ElpwOJxKRCXWpyC5H9H4QtBO2N9i96HyDEgTpYyNEOIVEf7cJsW3JSmI4FE8DDi3vTLOayyZIjEho6rbnbm9qZwV7FC13qlGL95UGmYeWkRA2VNNXQZ5pr97eW0NTrmRJ_jhas3Z2k_z6s3hTOfIkLtd0XraTwLe13CBLaTvX6AoslA-84vRCt_ofx3G0uawJL9IbyhvZOXQVKvcyxjpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KOeW3L31PAzaoGzgf9rYNLMRu6-5H76dvoz-KNhNlzXDmvfd2ogOXQuHf0Vh-fcla-9cjqBnO2appO3KIfb-mUb-m_JNsnPb-7GqSW3ptagkc2COv8FzoMxltkHFgHmhB5z5qPTsiTvlT-WtefVUsYfCJo8xf-ulDPQVgpRPEBqz8ePYZveu6Xv54rd7zRYRP-qUwSwZMxKt61y5ScUmdLirpvKabWDiNZ9_0TplIJApeEDR5EtgMuOcz4WB-C8Tlr4Bu9cbEso1ykTansr-8S3OBDVvGl2fW2ZAWKnx5NB0lX6XR3zuOYnCAjWEOvZ831Fqrn_RnHq3HmhJZNnF1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cI-f1Wvzpg1lpF_fhq3f8ck-vnfaD0ck8rwzSOsO995AmMGKuOgoAc2dMAPMZdSGYUVYJV-YgZ_NaycYE92i_lNDeanQSHnM3czOV5R4mRNvtHnOBiO8cwEKtcyYU9eyV6md_w3KMBdd08FersCSB9fevTf0Mxz_GBIlWSEFv12laPWchyCWqi_k2W4Jtgicc5a49KMjJC1gAgQH4WbD_RootbPZRyER7pK85kAXFHAKghOHfntqlIOPyDVXNt4ahDHLbH1HuS0nA5X6STi2l3fHTy_bbGDSyoB3fxRm8pccGmJTvGMuu0tUrqEqaYC__eOQVstelDLbdH6QvQJAcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5qzqtVv-xeX_qOGjWxdg9q8jjid8XOFRNv3vp19e5pFn82ZESA1mkM087JGBlnYMzk8jL7WVHdnJ3A7A0lbJdQ6-hRRsmKjGeLy6I_DwLxGc7Ze-mrOxh-bwxSdaVARO11aqLRU4VMJr24NIUG6mjOmHeUN9y9KNi71RDMNIGfsu080UJHSkUr8HLUaJvlRp8pv3YH3WwOhCqZpTq9Ad2pofQAuVMNtEUUzw1NMfKOYE2yLoDtcDindJUQUcRGas7_bPiIv81MAqK5bZl10U_duHzra1msTMxRO1_zGq37y3BJ5A-es9F9nfsaE-CPskq_nVzeGjFRgUNIVBF9kjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAJ18MfuOdNjiPfASqHhm3QnmOHMwrXdTPETN3Kq1rBGtS761X9pamuNDNgSBLIeJ2xLXR7RDANHkYSzBrpSPwnHLHWrx6PtB1Rp0pnNEAdej-ORWgILibPOKDd65T4jEvLYWjjhzet2D5wDaeHuvGcuXy8FPDdhz4CF_APS94TltGZEzVGfkjeSidtvg8lNItV4bpnTaXz2H5MtrK20CFAbP2pz3z8qZZ0QEc9Qz_hIf5OkAXpyESfPmVVfVyg_K5kQ0EQINCNkXofyt6gEwqSgbagYGJi9LMfO8EFOKmqnTuvdR0DOhb1Qw82aErysPfn7Fm6pcTw6GcAbAO_Kcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3Lybq1llcsIASMZSLUgRf_bVzT7C-pTYbRWplZDkrHtGDaAdTMnedOAkdysqwMDYyzH-AyoE88xVc0EWsbwJNvugaty8cfwsexuvFgAzv8j-QFiKB2_7ws_WqN8lQY_QGKO1OcKBHuVQxZwL0XwFIHnnDhT65R2DGd8p1w19jhk8Mg6IJoHmaMkJuPXn8YFUDlXKXDe6RsxQEp6BE2aRr7Xsk7kFdUajWVgtphESzjTU0XBkLw_vkyPzWsKtz5Hs15ftyPjMKj7fEwEg3WOwfkMea51doVX0TL_p_VLiz3YRvSGvwVCQ1Op1OunJdzYz8elXbirZfJytpFnQkxIqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J26_pq69A6AarVCdZZbeO-ti3xUFxJTm8zfKV96jC1ZbKbRx52sCUoCmjUSFuUe4hGaO84dQZLjZAPcPNREL9iwCtySS54yPBYGyRw7eGTJBx6bR9a0yjME1U3WkVIFfV8DQxqK9eG2NIf50QbLo4jlyhEjy5AAhlKWR9AhubSQjHkdYv91XKTrq7Jlfm1WWjMAwnN5N2PtqXAzaoZSNuIcAIVuvEMJr58pPEi0WyWz2isufFDleR1UCWcn1HfhKd13sF76Rx8QeYuFcIaDdrdhvMKbBg54oVd8F6QOaRi0nfW9tJzALtp5P0qnicGlz0nAXA7-qoI5off8Or5KQvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ida3eN7_kY_U0i7jWj0rKAsCoF0BhF2EJmz4jSYGCC_ALwWMBj9bX0cf0kVd9YO4-wJ_VumqqsLiDRQmwK5NOrEztBNx3pTasvdNDG83Xyrh22I8rDy8aOxW4SCilS5o-aPF4U8aIPOiq6aEamCPsakSZ-M5wDxSXLZBBWBDPYFjasMuJYnoVxDfjT4ci-0yoGThyAr8ktsi6ePEZ_LahLPHFB5usu4j5x-JSp3FKRNoqSeJRFr5L1RaVVWjQsJcqa6x1IVl5qrthpZ6h4jsVW5XXPETahUGwTBgzlBzRY6C6JQpoXRbCUCQgfLgnQJi9x8UnN7yEErBtdZOE1jL-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYyOJWJX5Ybe4v1rre1ptWvB2vqWCb5VdV0XRbhp8PRwUX8Sr7LYp_PeBQ-PPMv6DWgFwGOuk8G2mM71foY03uGEVXxUtQQxP7gq9Ny9a-RzWl0OMnVZbJ2vy4un3jQNluYX8ncEYVqGtVHEBovxAA4uUaV-MvxzmP46zk6_ghN1aiEuS9MSVXr0oIHJfjDrC4pLg7t_4Lnr_Hv_VCcJLqj9eA_MoqQ1d2rpfrvcXTjgS6r70gGRVlZfMY04f17YDquos1S6QAe_Y087ETAR7LEegoQ5245_Iou3dbd1mDo2sI1ZriU6yRIsNPtWFCzllk8yeSPMrb-PjnQsgcYcNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAglzxT8DlbmYkL2nuxwf-f7pCEzIJPrEfPk_QtwapebaQVNmP9LRbyyT9Wuvta9S8EHkutqInpkOUGJ8Q_H1Rnj7EcG6wQhj1XEWqSGjp3oP8y931WPEyvo9VIuH7dNA-RndkAjQ_BRocHAdvP6p7vDprDiGDnM5AUBMR6M316lhK15kxAWwz-4MT4de9_BjysHtGxcyNiKoX5ueoRdJc8YsvSuy6tXaJWr_jnn11fCn9k14ONBKmmMVzmJVRsWAEtl264C4NM9IlCwYOK3EZeyE05sU3hDUiLqJkOjCquKzgxO4orKf9ttbrtegJCI1IwBWfqbg4arVuKfsYu_9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F68Nr8SvB1J4mSmYUHauNwcz2YUt7s7RvuUGqo_9ermcQVm-Hvg4CifMBlnxHXUlpjboK4LmwKN0yxoB2xKe2P4xF0qhtiukYxZrPfvjd6NUZbMIDfUmYKv4PrYBHbLsz6RPjixOiBGgyaxGhF5I43NbshVMvXE2YgQ8qGJtV3GkDhmTKEdsKf4f9d87hg62bo5UErxy0GoCut-9K-0vNb5-OFbKizfGbZqYJUdntdI7g2Xj4ufwlPhEOaGqHqoQlIY9dfIX5XjvRuJlMZAa4I-2xZlj-ngzF4ekQkqH3Ok4zuPMcELcQ_WUGM4DcrUtaNbHfwjTGBi-5PHy78hT1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEPyMrL_-dun57IQdcBEhsnikV0yWSdjE6oimhnidm8uAHBP_vEZxKQk3rS701PEOh2qnl7nNjKPASHzWNJfuPcEqiJqQYSWCbx7-dWHbI_-2FILV_OGuesPGPMkF4jg3DLyEYPToj_wJ3_x_NPaUGv80OXpEHCOLfmh4QWLUH3l3XabnmnTAIS2SLPvPgsrGd-jBuHsj75ffomYbzAMJGOHG-xO34FUQLQbMsreIL3_Vb5MsSvHUNDYvqLrmnaGGJIwVnL_zZOn4IY6z1nzKN_pFRpu_SruLHMutCfgwim8j_DOmXXNiZ0Lo_diu69e_kaExSDyUCgNAXTjPi2Dew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brJQLS0cz1Fwo9vYYQeg70v90bU5AwChq_jmCeuC5J-zMqZib0pYFBGiCYwGGw891iUqEECC8FP0VK8rSxsZPsuJse4ebfaJMRSEhIxmUV6KH-Ad1mMsy3XOjWjM50tjScTo015xrOLUOeA7bolsQv2TGb-FZYD1WMDI5l_xsUkhK-Jb-pp6V-BN88EVw1herMPGfSFkXbid3WCOjGuFF5Af8fQB0hf7mnRIl8zhjoNPQqiXl51UF7V6GHgMexVduPnLs93e4W2mSqV_DTKUa05qm36zgxnIjW7M2qDorPM6wlBybXOnXN8bWy2bwnbkoG9CNiebwQ8paZpkhYHfQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-6oz_BD7JmHpbisK8IU2E8E0IZglTHHEK3p38DLEjzGk2OK5v5KNi5iUDeYvnL9bPCPiGEKjNq9WR3P71hLEdmcS4VWVQgGmN8IIOUQows-LIC7Jf35So6GoVhlRpw50nYqiw6CX1hLeDCqy7Cp_o89OTAxvDZQdg3twonxoj616Qd1vovvt7Ay12HfiQdUyM9Y3KTBSFJkIzhKcQtGMdJKlhqfxBLq47kfzzeEVYafmrg5WGx8aJC6hoIXLADMn13_MII2bkNNkVvj-KGeqZc0w-ic4l31aAHQatZ58yHgSmuvlmYn_3mOalS3cPFbGDiJLgM47dqdAm0eY8JwAA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=ssU6Wf5H8t6lNQpe_ZmST8yiA3kKBPsLgHuE4MNC5GXycR9ih29VuvWHN3Hz9S28xhDxn28b4V2dXGx9H9ya_SWqG5aqryzbtwdw632skjENJwkbhi-rw5n1OzvTxLCGvPbIalvYKX6GYbmI183uaJj6y2M8QOwjB3GnnxPUGQEmd8qexq4url70Na7irotZjkAT0acoFpjz9acLTf6z_EftiXTcNbC22bkxq58l1ckY7Xy5lHXVteN411xRbj9oGPCKQlUO917A0NgrrLcwkG1ym50Rp4DheI5xmArXorxk61IJo35Z9GOJrtTp9emoQMovuKb1UhvQ3xa3XEdDvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=ssU6Wf5H8t6lNQpe_ZmST8yiA3kKBPsLgHuE4MNC5GXycR9ih29VuvWHN3Hz9S28xhDxn28b4V2dXGx9H9ya_SWqG5aqryzbtwdw632skjENJwkbhi-rw5n1OzvTxLCGvPbIalvYKX6GYbmI183uaJj6y2M8QOwjB3GnnxPUGQEmd8qexq4url70Na7irotZjkAT0acoFpjz9acLTf6z_EftiXTcNbC22bkxq58l1ckY7Xy5lHXVteN411xRbj9oGPCKQlUO917A0NgrrLcwkG1ym50Rp4DheI5xmArXorxk61IJo35Z9GOJrtTp9emoQMovuKb1UhvQ3xa3XEdDvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwAG1YsvJgrdzAUpv5FHcx12q-U1GRExMhAwRd5ZuORnX86ASEQh2839zuyK3hNsb4lQ25zkAZmRqzRJBeBuNbvDeS_gieN-B32FWDd5qslK5P6zu7Fq7T7O4gZINlS1DuorQTJrusm24OMc70dR5-HI8XNkow33N68IoiurJi8gg4kg33dl-gIj_xnvjUG-dooyd0qyLPgbL4zE0NrKgEk-7XK0lh8ZMujkzUKjjzfEkyURfSEC2SaOXnZShl63sYio6mvAbO42oEq2FSwCa8sPddvUJ623ZBe840L0MxegbQqGKC5P_9rBO1IhZC61uWK9u9JmqgoQvHYaa6nv2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOyrFxngE6WwPaUGBHQRjvQ-VDNAJgT-sMrEWHnn4MeMJ9MV0Op_BT2_ouWBiKaSivwn8S4cSOzz-jCQ2PEX9I1LiU8MzBcom0q5ybzBDLwdK32ngzKshyOIBnggACCjrAurUeelvDSD4f74DdHCu-Cpfpt25UrXnGZkOp709QCtZ4qUAO-aYj50Oc6NrB_uYCzd3O6uhRnSayFKtPebu_g_fMzB5sepHNvm5U_3njPL35-AxlzpUw-2wN6OAwClQwrL6kDySyV6KZuGUV764SEbQbwF2cXkoHZrdkVd-6WXkIjDw23eYFkA0T1M951CaBrcrnTcyVDuwj9AZJGg0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/okbk5IPkx6uh1vjNyih2HW-c_i0ZEm5yv5mazCXrBJ3EIGLSGyZm100sjKAH7-EYGy6jmcLzrbFYv1Cw4Bw_IXQnT-MpbXK8sd4Ydpm7PfQc1ViEcilWwpt4shrD9tmRbEjge6hN_zrvXmZ9K1HVVej18-4bgTZyMUZ2VnJBBJCNLK3937fOoLqrnaiWoATG0zh00o9QcNeja_JtP0_XXLbwyXhkGwuPvggpsRd9flPgrbQkIiDpDq3OQfNvD-_Dry7QfcAUVNw05ryR9zplYUK_tKycmTv2XoNVyIh-AQmFhhMTE8vIOh1jnpOec4aYMP-SgMkqG16bc9xBJ8xW5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ckGUQ6NerxiGCbY4y_Lrb9Xiol3KcXfo_WcXdrAPu8RmFjcG9aMgt6xzZaTvOI7CM6kQP5HPblYNHcUcsz3l9tQ6RzD_T-OPAthf1EZDupuSQHsRRPIuGfaEFZL_VIUtEo026HuVC_XWhG2DvITKN3Vm5LE3lEXhr0h9hf3prE6Hb7cQYuVXRS03sMX9pTRi2onPzQ6co3yixfXOUOMFPqAlY-bzNOUCIqdFO3ni2wwcpg_soRHPUF23LwvT6TO1LrFZgr28ZzVH_xQrCw82qL7FWFAMuqeDLFfWzvEmOER1Niq87igMUC-fzIiHe5r6sjB48MnU4nhmRK5WDQOM7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUpuP3yoX4l_-AIFMTN8g0HjJDq6wLPOfLZfOZJ3Hh-xc2U-p9t0NAnLLC10c4xTTZfUrelHXM5pbJowvD3jTCRtC1MtW8iCt-rK-CupBV-A_dlZuVZ2qjttyunV7v1-26-gqFSOLyu4KfMwv_t19gQh4ZwiMfRFkmQxqSQX2xTCPj-OYddiRmIjontkKUmsu5xjIws_XBHNRI4vy5L84wzuni2vNzjirEJqxYxrxZgtU5qinVYKbPV7aQzKd--ul9QWuEBgUd0kBSELqocVDPwVFaD5QDoFsJwajUy5dOzNbuPowo6xGfyfYsT9a4XW6KBUJvNSKWkkXobxGZJzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZlXa-L63-C2JD3dap3JQS6MAAOaTodyi8GiaLH-UyIWCLszDCEYh4M0IHWdH4sBIuD2SZt6RM5XSXdtjE-cvDT1avggtO2nvIjsUK_CcN0DbB4oAXvOTnMAxTwkW_ts0ilGNq1g13HFOermJXIKOR8enTgfKcGFeKo7gPDxH0GfnWWN8zyScUt2lxnHwDx-bcnRqjCFi4bmJuV_ADVgJ2P_sKMdn49irygeZusa656g2DVmI-xMgQutMHWWeZfpORt_OzDTzSbRt3Mi4ItBxSE0qvofDA7t6ugALPr8ErjVY_X5owK5eOhrWlkCwjEFescVojnYEetVVvnnZXrRAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9ZUytrb2iypmO9UG_vvSUEKsDYV1FDq0GTyNpDKMakFQE3cp1fn1JCmzO4LrHpyOUkL47EuWXxPhXfxU6oZrkQZZYDMzJTQqxAjVgtOfh23-VazZI-iynB5rwC79sY-QGhETyw-jWNZOaQVz62WEfqdzgAEt0XsUqyPBEBXM_EVtODgpbiHpMVzh1vGRqtLqtYbzaKcV4gn5LQidyIwjEcWiCPvvygdOr69_a4WQaHwNSbqfaQdeXSv1kms21TgZDmptWhEcCXTiDDgY6ZdigkwU69XaG0vvdoFeRELe4y9IOgxZB_8Qg3FXQ8eoGywS5gm6Fma8wypKWRB-_XGsw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=MdflIecqYPOtOtQbbDF8mYAXgKVkbz590tgSJElo3FqcMjPjmVz_TDitvn4Oppz77u19e5DzWj1rLNy8BT1mRRDiXamuinCnTUikaOW48ZRlHwOxJXF8DaHr1h50iYGnSJnh6oYWvb5lTlB-_1J5P8dl4zGNeeJZ85cRFFGODOyWrb2PIyayNq5Fnu5u_nj5NSJYHxzidJr-2mBGI1jrIqDcac46HzvB7NzZ9Mu9KA2j_OfS_3DJXYvbKVCJjuen_5Z8rgWU790St2MPjMz_hG-QsT924496spPwj2oak8RJboehuw4dd7vJCIPkoC-e9XF5UG84qSWAPPbaWO3t9BqKwoRaNQTzy-2GO0csPl75hnCMDaq21VqqCC6S0UKzU5WXuKlJcueAvMPEtkYvl27qbufULg-AnoyNMAYGiMvuvro6IQIzI-VpvgSq5KkRS0d0DiZep5ABSM5M_Oq_C3r5uK9zykVP0rAp5jrNK8PMofshMG8AvVQXFG8YCU1mNs9V6Y9ZlviCf64lcRPUru_ORFsFgCJTD-WPoIinRP-fjPEpe-qoC-pxTf_ShwL1CVdtl-oCRH3vJNnS2M6gP9kO0QtST8GXFBFcmEESKVneEZ7G8J7rf08t-MQqP20JBIb-86d_Dwu6BZC1vlbeQjMEnLiBhtiZT53uDi51wVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=MdflIecqYPOtOtQbbDF8mYAXgKVkbz590tgSJElo3FqcMjPjmVz_TDitvn4Oppz77u19e5DzWj1rLNy8BT1mRRDiXamuinCnTUikaOW48ZRlHwOxJXF8DaHr1h50iYGnSJnh6oYWvb5lTlB-_1J5P8dl4zGNeeJZ85cRFFGODOyWrb2PIyayNq5Fnu5u_nj5NSJYHxzidJr-2mBGI1jrIqDcac46HzvB7NzZ9Mu9KA2j_OfS_3DJXYvbKVCJjuen_5Z8rgWU790St2MPjMz_hG-QsT924496spPwj2oak8RJboehuw4dd7vJCIPkoC-e9XF5UG84qSWAPPbaWO3t9BqKwoRaNQTzy-2GO0csPl75hnCMDaq21VqqCC6S0UKzU5WXuKlJcueAvMPEtkYvl27qbufULg-AnoyNMAYGiMvuvro6IQIzI-VpvgSq5KkRS0d0DiZep5ABSM5M_Oq_C3r5uK9zykVP0rAp5jrNK8PMofshMG8AvVQXFG8YCU1mNs9V6Y9ZlviCf64lcRPUru_ORFsFgCJTD-WPoIinRP-fjPEpe-qoC-pxTf_ShwL1CVdtl-oCRH3vJNnS2M6gP9kO0QtST8GXFBFcmEESKVneEZ7G8J7rf08t-MQqP20JBIb-86d_Dwu6BZC1vlbeQjMEnLiBhtiZT53uDi51wVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPkwDlC6EqTpo2en3Z0m2nnzuJY8PSco18BXG4KYCfATN8-U85sSRmFOnmRammhJkrGLl51hjoNGKRTgOWbMQMWmvWY5rnOazTEuhoAcasrZvPLcyJbJYtzP5rgjZ7ue7YhqwYYbkB060O2X5eBYo9-Q7I7eYsJpd2xIfDS4p3J2H_ITjueOE17i9LdC6rjk6KgKPKwZyQgRhYRe5sUNpHXogP_zDSVoaj-pfvT8dWYiQYd-JOCEaeLbHaTn7zOCcJrPrIlYmdo19U5ON0YkQ1Kz3-dXjf-eHcjUWqM5RttZeFidVa_GurTX5fnThsL1cp0HfhFqL8xQD0BMcs_6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqkknBNla7f1Ci0QEReP58F_SII8ks7by91zglRXosx-yGI6fqnvw6o576aPmX2C7cf156Tvcx-H0GKVLglPHMXZIqRy1R1OL6nOUjKGV_3HKgdJYzasMFij40fU21WqWESY67gPMLUzKdZ46o54M4a61oYNPifx2-7iUbq4Orw-qlq9fEpdJM_pLHcW9LGnxBgOhGOg9AdCnKqfAGn8_hBdwqwQIkL7swRJjNMqCoNibbArgngFQ13DG09T7T-C9oBQJM2Y9_pKmLIyCVKwEEvyZWdiATl6tvLqT4bgbhZoT2FL_n_7wQrgowX933qWE3H-lZ4FhOOG1jlTOI6quQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9dn8Ho2fFup6mw3kxA314jCIXR9FbGa7BuQHmSiasCR9cTwvZnqsFQcNN82guwi_q0dbPuvuSToMtu2aJGoxXviIpii-xVHYspENs0ptNiEjBsK1UBACLdEh3a8N0MUPOVKw6EnM72aQlmkNg2QvuCeDsyajtoZeTM9rv0KOUrkQBhPS31nahH56j1dMNfu5xQuXNyjnv3zKXdYnJLu5jicdwt9PZSouUayp6XrlYcWathQEhqf56VpokW9acXcXEiVruY_v75wsoWK2_9Qs_6zzJb6jk5DW8FI8ZviTXWUuRSQFRhSltwK-ZpINxKZ0aBv2tskFwhaOkSmxcbD3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLtGu9-SU3AVfWKTC1T8G5QX-WqyIdwAWB9mHwa6qjdR_Tw_aQvMjEgL2Ew1nJTtKMVJuiTkVCZ-m-4kI66CBQRoyToslAUC-NOSeok54Aa7WCNlmxxt_jcZV7nYQ9ggRc0DidSRvf1S2jGERcsa_1lUJaOxLFtQx52CGxPwIhSqpN5EA39Dqj0W-XJfO2t0fVaIRD-olbNcJ7CcCCqd8TIWG2Co_Roa7ORxoG6otP7ixK8w4VVRZ56DFOaGGpWdkVuNIVd5Xha61WvWckSPisvcxoKs3QXSBExzXcEeT-x0b5SZbQRdR8MUViHo4pvWFQH2nfHGBgeONaC0-r4Zhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufhilwnx23-F3pEa7I1ekdMEekbAyRyEkcU1fWie22XAfQDCmmpfvZO9pudGmv79joiOsP7sw1D7jDFFwdd3Gwie1MN8AzSHn5j25BeRgTNRDdlyYt2LxC93ikZI9XCAVXWloEGI3eGlBTgBrPmFNjpJlL_8Ba2E2ohRti0Ez5nSU0D9sg72gBkQJLZW86ngmzDx_rxEqGUInIDqlx60-CwL718aeOyLpQdlZxZRa0Z4uthfT-OMWGx0-mA5d904DGOptk93akhLoYIpzC2udGkYLUr4vwgoyEzv1HR8PBYgPKFP-Uk800K9oJg_vqxSxDdHYyC_atP_5RTGX_AevA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0apfqnUNFB6ateqmKtw8uruuRy9FLGM--oz6quJTDOIWgn-XQOUl2AzRZhJfYFcTsz11d-ZaQoQm1w9SuKev302hztWSlQjBwpIvsbUHffb9Q8dG_D7of12Im072zZMMyRmI-Uu50FZw1V7pzICVHWDPx6ADWjc4_hxQhUpPMmMRcP-xQ0t01EKXETLry03i1RQq_8aprpvfkaNQLuQNIduMdGPAcIGn7kHwxwbop8xoVFk57OZe7JN_HVelwPpyaipEtDomaqC-KhCv8OyncNok52rTYryEUHWqvCJkJEG9_s3-kJuBCcCGEM2NdFs1F-WWes_rmXAqYPCS6xpnYmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0apfqnUNFB6ateqmKtw8uruuRy9FLGM--oz6quJTDOIWgn-XQOUl2AzRZhJfYFcTsz11d-ZaQoQm1w9SuKev302hztWSlQjBwpIvsbUHffb9Q8dG_D7of12Im072zZMMyRmI-Uu50FZw1V7pzICVHWDPx6ADWjc4_hxQhUpPMmMRcP-xQ0t01EKXETLry03i1RQq_8aprpvfkaNQLuQNIduMdGPAcIGn7kHwxwbop8xoVFk57OZe7JN_HVelwPpyaipEtDomaqC-KhCv8OyncNok52rTYryEUHWqvCJkJEG9_s3-kJuBCcCGEM2NdFs1F-WWes_rmXAqYPCS6xpnYmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsbQExa9Owpux-4SgWKxlqI70CB_hOV-K0yGgI7oSE2q0ckoO8IZ50wnrDxA73Z6WgDDUENogm_zJGGd-qrneZKbeCMO4NgMlrxlevANJK2gtNAXrndZEIyJviToXbRNmVChjupHv2XA8mt-rjFGL33hS2BsF_PF4HwzCHsmA45bDzL81EJ6POazXnLGGrfz59AGcxSW4dm_lKDimhl9UwkKl3apcG4-oaeMce3fUJjOxpzbNM5Us43ZiqCl3MGDfOtArUot2WQQ-SCKXRlMrMg4rbW7zRRDwsERjRIstoNy-akU2zjjqhMpDVUzhEh0BeTbaqTqerbEydhKlB2xqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mwk93Gqxo7Ia4dIQDdpzw7SYeGmcvPPtecXvmt8xGYhL39pv7enSQHnOz91IPzUi8gdfrxwlLhLHMy-cqf9GZDIrPSUIjjSSEaACb7PE7rPK2eyzKarIejLIA-w7I1tyj1Fo2CXEAWMy_J0qRZYm8pGTH3hIa5-S3HTCtVzUjp4svmcSLiYJPlQnx8VnkFn8dZe1A77cf32YceHYbR_nD8mr3rL5Huzkqhh0YloamCPucYMqzskfmgmXNnxhppT8D3mehB0aQCSwLfqOprQU9mQeK7f0VHdRpXhE5vxJdsulGFtSsaqaShH0UoE4cR7mf4POZDf6l1MIHTfJcfCsuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UcwkUu_Z_ZxcXerzNgj564QC2GWt6phmPEHHCLZnbvGqtjqnXcfepnne9x31uymh_bTkEFGnKY9FlHOXm7qNp2Xtj78NlEi3VqSptRj-NHt6GQaOYaEYznI4jESKiL8Z6urLZpiZ_6JymGtIUjOblXNppKhytRnY6umNvjX9JtmW8t30rGrnHejmnH8Znr2CoTGqk7_l3uTFBBIMNtx1lAJ-Zwun8HDz_CE1A5H4JATmzN2tzvILfkmdE11PrmnLI_oWQGlxG2BtNRAfMaHKSbSrBIiC6L0K_Srl_EbDeKvhC5XL562RjVKBe8du-dm3JM4b7f3Pi_0_4UkYbprC3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WhpUEVqqrbi4V6GQ-IKOWmnfBCWjvnGDqTUJwv_WA8GMje1PNtwOQQRhWVPOhQYm5nDDnbzAxjsLmoHjC83z72xqi2uyXeSqupDFC24Ve7nF5KGYn1j2o12Id2tYxFhzwIjgrFHSgy1AYrJ3Vc8u9hmWB10vJ03DkxWJvirQ9bWiEt8YXuTs7EeRahnVkNtKGxeKMcFl1CZi6o8ncGzr2U1a1vzXnV6wP3R2IhoQZyKfY52PNw2B84ZnB9ziNONeKRNjjyvi8ArpZHi8KC1-5zZuJbUvvkrVowMAxZANsVPrnnVuWtlRjJQxivUlVZLWiuSMs1XSWMKSBTMInyxWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-MSvnpVZc0_tisEfxE1_kkBXMiIZnapo5cvofYiko18JdWoEkzItsI3DzkAW03bFMS4ogamyrOrM7JTdZeN3ym1C90otKPUx8FgtYD8kmRQUMM2Pand3cdPd-mlQDhJU0XdWjxnErfLNcsU14p4qoxnTRKD90mIJgX7_4YqK37FMGP14XPjSpigoBReBe1dUkLenizjm-vgnLZvW70STlR-ZTkHv2qyK1ebrTf8Jav_hxPtypygVdUwUuCDFce8LBhYnw69Prn1xwKYtnHxDpeFXpDuVZx4fJM1QJUTZ0jwQPtrie4Etm4xMsJwYGBgv200qiEzVs-HTqGzAHXAwA.jpg" alt="photo" loading="lazy"/></div>
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
