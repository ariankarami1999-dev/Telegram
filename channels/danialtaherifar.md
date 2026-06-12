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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 20:15:04</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 286 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 329 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 389 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 510 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 622 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 879 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 944 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzNCPvrphaVOCtvrZh86swqh5R94JEISywMrS8GVNrjBm8UcqEhVsMf9iLepLACLxa_ZvXjtFVj5NJfKNX-bfhtAKiGnp-IJsr_zfnMECPrDqfjpjfqsT9rsxSMZAcZT6fg63JWBpghFZblxTiKosgWzpLMDeqMHNynD31p0u6kJXfFAHxZj1KNuF0Wab9ukN5rqVeFd1WRTbB12Y0XTj9Sl2EcyYD5g9v2EOmQh9soqZoSaXGpx4R1hDZyoP_JBfrEOnjjWq8JBopEFu4jlzrGvA5L9xPsiRujzggtxh1ewKrOOQu6bpUR6b0wVvajI10BNryqHrH4csTrXi8ZJ8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIXaKDVjrNKmU0HEX4zmPJ6H4QIqO-87-wyeX98yStBHGewYC7vtUoALwdv5pZi9vwwZuG29qRzK0-zSzSYpFf06R_OxHsUquknxe373vtYnYCa5bWUd8WbPB6giHBKsxXrp-Xy-PVmxdlDx7BZnY2ppkP1-7MQytNijIYfYCEYKZXQfG3fvfIsEi74Tb-5ZbVweWC04zQCx1MTy-pUYXOXfzOMYp4fTTtc2s0J3pzTewyYHOoY1dyKoa5NYcc-xVkHpurvnAwzIM-G3KSm7y2G9RwHhv8lkCs3Qvey94xBp6te2Akjq2InOkY2vMz3ne7fMfCC9twZ-NXn_ZadIsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2dvMkg99TxRHRYkA8AlwAyQDAbSRsgYSetUhD49jz-ie6Rj_1KFWHNI0f_7FLTzX8d8n_wbaAIoq-jIGY2Mo6fIEPsVjffUAygaPUSvDAG5VjbFUkN3EnLEkwN2dwlTjn4AqycI2Ak2rF0Pi_RSXAtX_vUIiR-TAw8sIxuXwd9e5F9vLHAzVvaXuQOgZyInhafRVQGfxNC_Y4UWUe-K-pWXVurmIF3NqUxnEkFKdXktuUWipL46P1lxJQYD0MmqLc-EZG4ICSVyYDqxVf6aWCCZsatE2tQOEB9J_6n9cjmpQMo81Amjb1Rb1aocdL-dDcpEmc5tAzQB2jfgPIwlFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 848 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 680 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpByUcNhtjoou_rez9cpHLOtFWbQKCZ1xu8Ioa8mXV8mU1ruek_xDS9qsB-6eHrYYAD9qrzHhjP3o0pDegYviuNuc7IgVWUOhXPlxp0lYR5FL_hloQO9zxvZHa_DgOhOpuFFnVOqBUUduJsTV9V9GvSljExFWM_biA8OyD83X97S-WQMUfFUzNyJ0TFoW1fxzqesglODYd9kLdDZhEuFvnNSb4na66YRfq9f2mW0lzD-g18qh3k1arA1c1PUcKv5UtDQ2O4uL5-nWBoLRlO5M_jjn82X2NZa0C_09RLOoKjzySlRY-Kv4eXr4Svox-lZo46ojM8olUQa2F7LviDZTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cE4YtkjwtxpMHUYq4scstB3cQnjuSA0lNmKbrsQPcKQyk1VDCAJIYuSPER0rUo_16K-OIXmJlPrOSs_Sy1EdbY14BfVxjVmtv5Bw8ktOwT1TDbsrUbhsHo-sZena9Og7w5xFCPJsxpH12dW_XM-olYp9S-hgi_AvzuG3zOCKvDPR3-LFrQkQo7LKqcj5I1ag99vuQ6cAFNAG66IAtCGqEWtRxlALf7wHQe75hSOo_zSpr4-9kCGof-D7TJ5_TLlhFPmrFkfprV6ZOMbz79OdgKolzyS5duyDPcGzs0of-bQVJb1OgH5Dqtb5DzXk8dmAUr1TWjm_HVJJiplA9RwMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X46nAQ74VJBHulgBZsiMDwPNXq8gr-4r6CyliGo-tdRzhjx8YSJ6ub4RrjDqblh0Kc_HhWMtqasXjGr7Dqax3bdywsaCwN7f9XE9ynG_4KWIM8dd5stqoKNVHUjo16J_15cEL50pjKtcbyDaCptuY3mU5HaMbUIdlHWv2FCGmA3iXfILYwvv7Qt8WHbYyL-7rd5M4BQMbpW97eQJCFO2y6bFYEQUYtQ3FaV2DV56PBuIpQmL4kVJq5y2rrL6dUeAp4fbJBt0Adu87LwgOPA-H8xQOi-7aJDIRAEydTppleupvqtbYXGTgFHHq0M_CGaz5JqDSYmCnRhf5mv59ggs0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMEoOjuVSD9kdTqILlfWEuwXuz3qmFG4VPkULjCwOtBvKBk0afyw0t0nqR440y-Sk46oUqp_6pDc07HLvHa8vVpnp0KxkHo7FH1aGwQofsY4zatN7NJXlGu7pUwLWDbK8sce00Un0SRNDWIW79UDC4WST3yKk67fQetFa-AtjjJnuKGphnLOnmjsFOvUAoa9j3y9pQikjjFxozT65IHEZPJyQx00blyGq8NkMHvi1IsmsQoNTmP_JYs3C1Ly2pteq4B6pUzU24QQLyXvTr7CFaRrQjY8aiB1Rn_Y3UF4R_jVOEKV4xOaZKWM9x7HGeGNV_qqRi8B4AH2MVC9uTSMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLeNSBO2N8LUONi7nSc0ZT8CwNcim-kL27jn86uw4VfLxISHwFo7LuP0XFkitzaQqj0z2h4OIKbj9jl7EIlSU-YcTya2MULrV1esrIpWJay7XKClxsVL4xk6oH_ysd3m8zoXiJPXU52kbCaG0xLff7Nzi48QtcdzLgh6p3tYWFkH3oUFSGwPl2-QGzvPhplo2hj8jw7S9LGqD2rsoHaHljuPpDqpRnLERqxbSGHkgqUKEBp1gi97SFCm35x9qv2hOgv4PMNALXqZ2NhVFlHKgj4l9nIyU04aPm8oB-r9D9Ju88fX6Gq7Gr4kX1V7vCpO724Gkax0Nb3a_3aUb2A-jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTqp78NQvbS6b8X6a2BJxmGZwMRCQHEyg9SA1qge8qDQFJXEqYXqoZElQ0X7ksNyudnAVTlKnlbXAT8daklX4vIXOEvu40ksBKJvtxq5DnHSohZQoynpRLl3tjunPrzs3RSEduur0VfKEOUBL9nP-sCpCWROUbyPQ34eUyCFUzBcCzTGD_WCMmvY9jEQWp1G-HjN9F4V14buTurWZC2AjUzdGhwOA9tEL828Us4zRml_VlguBu-DUB0H-ME0ymKpbVWj4GiEtUOwbheHrLHUqdWzZ7SM1AEvgOznmdNG42spapqrMpWdjrFN0pB6zYXuIeD3WeeRfTeQrjcG6ApuvQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=dI9eIIlQ2HbcbfbhCfoUTRRZnI37B-7Kiq-VESQTN-X6PPZx2Yh3F9LXM5N0Z1CvuEgJfsYMKlweTN_STZCuXROl0hjnNjgu_cFgMuYDmRSJGrXNcX6c85k0cXsLtrNt66ZcG_Ku-ovG6PwvJDmSQiVWM4ZjujiOMC1Fi89CaCEn-Jzhf0Mx4KV42BhTZQaNBN820pFfANZhzb0ohqfoO3N-hOYTej-yU617OHC_omP7IRTdn51WD8Xbey7MUdBVIkWY_u7E-cXfiX5FVT5xQ6zvSIpVdyzMm_eanKQbXYCsHTy9gI6uML514z6cjh68Een0Jx13Oo5zSTECfvxsrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=dI9eIIlQ2HbcbfbhCfoUTRRZnI37B-7Kiq-VESQTN-X6PPZx2Yh3F9LXM5N0Z1CvuEgJfsYMKlweTN_STZCuXROl0hjnNjgu_cFgMuYDmRSJGrXNcX6c85k0cXsLtrNt66ZcG_Ku-ovG6PwvJDmSQiVWM4ZjujiOMC1Fi89CaCEn-Jzhf0Mx4KV42BhTZQaNBN820pFfANZhzb0ohqfoO3N-hOYTej-yU617OHC_omP7IRTdn51WD8Xbey7MUdBVIkWY_u7E-cXfiX5FVT5xQ6zvSIpVdyzMm_eanKQbXYCsHTy9gI6uML514z6cjh68Een0Jx13Oo5zSTECfvxsrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlpXTReA902WuUiO4CfzO-9xWEBgmaGyiaWndu7S3YFozjN4k8snVYU_bW-IyBUAwb8XPQZvjl1KFevGape_u7EHq-JPATibfPyKHXFXd5GwPhqFYre3EEMdyISrVRyu8jKqg28LQNOBYmOAwmET0Rb15KxxuldSFks0F6UVM7gWyUAFsc9KcxabXfJlStWrN_8Bg1d5hMe-Vz3u2ClG6ErBAghETR7KkFEM8wKeDgICe0WeQqgpAKpvSArClRJljhE9iJPbIx_ljh1G6__ghfKyw_cmLwAd1q6sxyE9ce78UgnpifDYBwQwX-4ilpzl9ra0FYu-qeuiYqwD9nLuDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO9LU58ofoftl2Bj7XlHKDxIlXlZF04Z2T2pF3FqNqSYPGksJcUHV2kdI9dkbBYcDDK0UGmaeWvls69bzMm5oMyu5no0FE1Yx202AxyNcoASiiL1L2veCceyrIp8YTCrKTroHMfpZzSg9QkoRRIxd1uTnTMNEtrrBOFxqKerl3c4xWPIb-oO1dOvgutR6iYXph7E3WW38gxOpkMm6YsCj1Wh6exQuDb0CnT3JxkGflb3GlDLDqdyoFyfATjVEkr5g8lWhuwLDyRRlbF2SRSCA5-baEInuDg0jVCMvst0SneTCRD47ZrsWedJv-X5xKsfICWaXqs4_eUvupmtfPTcxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TdsQlwnafPW5Y3qQYb-XHwrbVrYQZwb2P4yyWNWkYGbdXO5ZeMov1Xomq_4L7n5DqYB6t3X1D-9BccR4k6e7s502_PFMDFM_WebEDXSg76i63zFbuhZr0SDOgZcGtjkw1EZskrQvewiiXVTaUq_xHgaOfs_zZIXtqCSPFFt7vYveRf3FJdIpRJ2ZxyFiFRgzWq_Z_RgLoBKCXsgA1fMZtyJZT26FdVbPwPDSLdQsgZpvXlub0r69qzvtA3LGWNdNLrpo953JC8qdHRiZ0R9xQVG7NIgGYZe7rfPoX3BNM0FW5mNjZbiJ0hQSia6JJ8r4OtZKS_ozMGELe8LwchbEpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAUkbJUEs49fG3seqLTk275tAhpCiw-9E4d3gPdK-1CEiGEDuY9l-ckowmjfSSksceTzuOLkFYdWkF63lr9A7ioA_f2nxzHLxlYA_DqR3QHuaIthAQGpBDAAlFe7Tmsw54UlAYa1El3Rd2idpLdnXc6_pr3K-MEHVooJB_VXtOQRxffghYn-dBJB7SwuFGDeLr8EBNT8RxRSllKje0WyGtR7ipEqF8Caf9YSgpY6kSq17gzOVXZLA76RyKpWq8ixkNIK4hopGqkv9Joy9XHVlIr4ussactOC2Cd_3ki_iln5MAjBHInw2CAvSIdRh3_X5U_W1uklU4l91OKGzeIAKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4iOXYRHqii9_z4aBjDjSsP-Z40CybX7c6XUOaOOEqOSC_gPG1o5IRdzQfGuh-CNTt7Jes34OPpR4I5Mc_M_fR-OEDEcupvKks9_4mlAFvra3GXoe1hVwuqUbhEi2SltzgSCFplN1xJkt5VF1fu3n8r68hp2gZtlCVlKl0r4wlUlTesWyN9N614nu14RxeEYgAVMkWHRLP3rY6S67DdEc8WGPFHyMHXk881SMX1IZ8Vn998srdzhKbX87ehqW103VFCAZ1cdWIB8Az0dg3ylwu_spAO-FNj7X8S1i1BlUPb34ZSesh5B8WQj80K45JTccODZ11f9EkC_XUEp0glfKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB5nQdSvsrWPhlNxCgR3GBBUcFG373CdKx7BxxADW64cuER9sS6CXG7wpTCDncxy9XCeUbZwRPbHXVuENhJCdZnKMpLDIzhd0BNxPqg-Ea0jMy7nIruBi6F4g8G3sMwpw9Sn3xjaQ4LqrwArgGGMOdY6-YJS8owUdTxdSU9EHMFdbAncJpQmqVhBy6tnF3W05Tfk6yDZrA4lxcQOPrZwcdZrVaSzx4lb0DbfyV49qOvziseE1mVI2HAbrF5c5-1bJaKnKYqlkAaHUM2rF8TADMSMLqQzykYIPLpAC4g04mroWNros6a77dKJ-RGOGr7TQshfcxdb2B-BcvnegrfbkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hl2U_qOscFiXJzjMa6srhUBoABPJhtCBTqFK76UELWQZjd0WXvH-N4hby8i95jetxknxbGE86Ocv_b1P9IakIsZqfruUGUOla8XPnGCjFmjWxFgonYU92_Mj_6dlOInS68kFhYkwl5VElhq2QLLPcUyq04AzQjV70J0Qu17SwtV1kbOhW3wyN32cIlm1PijFYCiWbwlFeXbR8cUPT1Jr9OXw1g_4kWEC54XN8E7MirfJd91JpcqwDoGusWSDD4U2V6uHBEkyi9xWWLC5BDwQC0h0lbjERlPeywVSQOW6T70y4AvUGyHv-ouXY2-2YTCX79nfhd-sltre1lWuLGphFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOpM8W04upl72bE_PzU7B3l_kPeWajJ44vOsfdMKXfI2v5z387XWI5Ktjja8best2stF5UW4amsavytAGN8HwxtBWw-NYqiB30XxIxyBBtsreJWru9eaigSKIcqiGGTnE3ojEsQ1kTMIdK-4XVW5ZTRBhewW6fIo8WL7IoiuVqL4euxW6OU2Sn2LbI8oSB4ibW2XC6SsZggNQ7iFvf61l6q60i2fe6p_fvK4rhRQFA9OhCpohmS51a2ebUdoA8UK3KpO10W8D7Rl7B-OCxvP0lMBQDAV_pnJL7E7RpUVccj9ZS_kOlxJtdz_D4CIAbCbJ7GbZ5g7miHaCnbKeCCddg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX8fwAgwcXrW5nSkPV7Mbd0ziuWfz71OebvDpPndAG6oftBPqnUt7X-7ET-PSj2l-Mh0bbOuTfK6p_Bx_r268-cJgbv0cZmRLkwaKlTD17f38CVr5q2edWFFOca34d_j8quc6tDUSKZ7ti2ASILNCdVwHIj2l5p6ABtvrs_nA4Nz0ALaZgYitQEQ54uwu_J5JRHikErqlfmzXXsoOVOT5Mbn3j2S9jSKmuZIG-ULj2j5LhRJpKIxwFMi2Hy_GNYxlmAQL9nTlLgMBzAp7r-5c8TcJfHNefHSRkAAx9QR7SxV2pKZaA2V_cDrljOTgMf_d2qDrSjfOwUA56SKKIEXdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY7FSutIlAdS7jbJiBSyuI5QeTg-Uts_tcTL4wrERbfD9hUo6YS5qzHCbpN9A1EpOdnLEgCbm9pLfjC69NR01snTJZRVo66a8RvomX37s8anxHUuRfmUcdYDJL8zIpg_IKivQLJovzrlBaN2F3i86ev-PGjPWS_Q0ZYipRiG8XK3kiOzTVH1Q4sU5RkstHtXBRzanwIpKQpj990FNgAPFANIv3s3CmhbAUjQPWqSqBEIQrpUUC2H-s5k7MpNtKs5CB3g1i0-RIUNxur1Aw2VLtlfLNWdHAlVrLfnQOirlgS0hEIvpOLd8CYHHZjum0CMgnGw8g3RWRjxBoBghm1Rnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjX67xf-TJ8QrxKcjOUL-kWSZQJ0yvYp0C4tuQDsmXMlL-f7Om4E4kJqoZQFdmWcFeYliLE5LaKQ0fGVOC7acTAzjqHVGTIt7w6ig-eBAxtv924zc9hG2MVolGLSTzHinEJ5z3SVNuuffN35jzgRJ3ZuF0TtMUCGPJegLSHXKkJE8fOhN5tqZipZLuPYJN0KN0UhR6HPK5E8O1zqUwiB1maWzgbbqZGntLQx96LzMRVL0_i5w3Qr4mRMRy-9rv_6DAF2pv3nhJDbtpPWM_-Dxvjex_bx6gORu-96YrLCOCPnprvOpygyhjLrH1d8YJwr_W83vrTs5PuFyK-tQBZq-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzFlR7UZNhOISNmyq7dZIjD3NlNnAwzQIcnxZYChoTqvL8TPA1hsB86q3VhbxNepe-SkTmci6Suz8yEKrLUqKcROs_Gx_S-Bz5wlo4k2fDB3L_xaWIQ8OY66fRr0Mom40ePvyA9dx6Hg31FqUkzb0fQZ_T6chvl7Nid1TqEjShKeIO_e40L5v8jFukur9f6dooN7Nk8j_2u_ECgiHn-9JGQJzGoX17rl86WgYzFvkOA13a-cD-acpuwtyP8kLOOorpVlb56atZgj-v2iBQ7hPbkxSLfNh029qKLSxOitnTxk8D9Fb9KbfruRMZvnUjSAvKkhuRcGP7kp60ob5RYI6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ix-sqvDSMXufSs_fmgN150uaj8k0lf2j3ZNLWDgppNz7qnm7cOrhGT25KW6tIUsCPJmHx9yqF2x61h67kfGo5F8RhdPpu49zeGB4DYulxthdP0OsI6oXg1L7K2wPNPoW8NZqhlRtYkhINxMr-TBUWSYLw1fM93ZLIhnQSPCi-2rBmj1lQjV78Ircq68j1Cu2lOpckHudgaeE_fEMYaz71Eq0VP5tZihOZlbMDH7lbmimeE1vrdWHdyFY6cGUNRv3bBLjfT7UddcjGLzKJH7ZmMHKbaTdWmX-HMN1Dkh43Pl0JDVN1flE306BHr3qAQD6fGAQouCYCU1zPiy_Hhw2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZUkL8YhXMAnrXacR2Y3jOiotBcAs4ERiYraUI-ULrDeRswnWfKeUEE01N86gzHTgdeaHM_lkAly6-ZkH8wedSz_JkNnOUT6Mm4BWZ_0JHNYEnuZIBE_NBo3JxCBxdTmfeopdqe4ZNBMBDsnXDTHUZ-OM8BoznOMMNuAo51g9ArQabVMrDmG5KWtZr66myeraqSBHFj94ya-8U8Zp80N9uj6UTSet5y8uXtzk_kRP2JMVmYcsyrw2hthwoR6EMiiT00GtBooAHl7ST8a_zoReKMTLQiDVWBYcEAJ7wCPlAHgumsGlQK8nJrWR6pE7PzGcP2c42WK3ecTGGFFeyPCMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D89ApKdMFXyaXaexX0LFLbhWwQ-vym1ulFKJewASt0XaeSxPmsJ6qhr2Atrx2krwEj5ECn1X9epa6oRg9rCl7Zy5oQpKnniu8bPb_2eWu157UmagBkXSLknxYFL2FP76z8Jxslu2azziqs1XDnCq4g7LNjh5oHY0ZPwAN_oSIoz3Qs2YVIxWQguze1E6z4Qcnabu_Lqi3-PQkuidtTQHa5vEyCLJQY2dZK_lHkbMNc3-cpAes8aQ2w6eOEyNSQsPQCMMA9qwszeb2xWHQfqe298q42yM5_pV-Qwm3JG8jxtRuZLsXQcY8Pp2Hd37pCG8kER1JptTgv8Z-qBcwqQdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FleKXz2oyST1qUaUxin2jn3_oEAe-x7ozBln4Pv6DohmxlHTV_tGLyPYYLuxPjomWH-uo04h41j3Qm28wGuucTgWMihWoTDCJKWTrSqGr2QNshwHdpZ67b5O7jxPNNmwhFMM987IFNamNfFQFWFt0TklF6ce_WwVDxF3u5Th9lAglveITzb4bwzli-l-JaAVxjZJTGETGtzYoPxuH0I3MQkFQKQ6YcMFeqGdmj_opURODmsTWpL0gYgZ7t4oXVr5iLfmvPDKTrhHizaBb4o18gyZ7xNNaXqDici3IwYDV9O2DoLCyaUaHjmelCjJkK8GBhUaYO5GrDvha3qusMV1Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-M1XLer9aEmy67AYbGw2rEELhyhrrYhUYBXw5008t6y8U4xqQ6qyYY-Mdi2c5QgAma_SeuEfJYwx_8dgcSL3sh020T-HjIewfrKZPPdnGEDZj2_jMJ5fMbUnlbAKMc61k9rjfhTsxnhMb7-jYNRWUjdE5XqNaOZQZMnTpyK_cGOcCY6ZPr8Wtv-Jk39qcfpudXbw0xgkWNxXbtVUCzL_zstb0IzC3ifo59UN8L2lWn4q3nuGUWDw2j54YyApsnGbXt6WUUI0I1_0naZa4KiqdPrO2W8Q-Vaeot_dY13RztkUupiaZOj3epUey8ePux5xvYyxhLgJHucz4xrb-znMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgjeVH1RdOK3w7Dc-S9hh_kThohRCw8eQd7l3Y2pXFn7KOqVIUIUHsWj1Vl_GNaKAgfF1MWG4dyBn1WUkoW3OJ5OmSrCcIein3nfvW71LNSaDyz35y9lI87bFLCGdSAM_cFDH6nPkgFJxdhhqy6GsFhrcvIRKA4dUos74db9-_lEn3dFCqQlGDOFIc01mQisGTduLomI3QCg1nFezE0tOa-wep8TvuZ00rWU9A6AYZiZLaqivMbd3p4r2cfWxNbr3Y3TOWjv1e3rXSvrlqbKd4R2h2Ul9yl8QVzKMTgyKJpI1kC7IK9-r2IMJe5VqliZBQsrphzsXTvhlx8S4Di81g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jx0El-W3Yxc9VeD52uNi80DVChyIGikJ39IT2Vquqz3clP3R6eF775-1XaIyMUf_GSqiFMpbnL9aMZkSEinfk12qGaJZGekTetIiGSLfE84YF6kKfA9XW8sx65IrCS-zuiPetW-KtMDVCiDwUTy7lVD6cKEj8uYuJrFAMNsUihjfFj6sxs8UQiYfN5KFCzx08U0An5cpnqUpsz_2A9TjE5k_izxJ9Boa9g_y7E31DxGU0o85gEUchLPctKkhcqnj3PVX4s0QuDn7QwbgZzefPO17iI9pponHhXuWZlQZMmIM_v5_0yx2ZvXrTLWMoQECe3VwokPpXLls92bMYizwcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2pWpJEO2vk4CH7SCQO8gVejB7yYaSZ-62n1K38TOB63I0GmMtcngBVpAyNl11UoU0brVmoGqHm8mp1L3ZgFCQaghYCqY5VSutI7iSiEqnkAHxv6NpzQybQBgRCwEcW4-M5QdKQ_CihOiy6oLareFglZOzqx1WxSsH6Hc5bcuxbletEbpzP6o3Ba6DQhGJnFxGkL_0fqBEOoB6ri7hER9GrYbfBC8zlLwTSRZgoHuuZaB5vbCr_RzpTve9b0cNvaNfdfHbMSPVeEFgdmXtQowQlQUVcqUeDgCKQfZoyOSYZQcHgk_o3YohSWpm2vfxFaVEYc7wXWAmMywiLBN6Q1NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIFm1OWoJT8V1aN-b2e8ZNSbLDGVc0KSR7sXsKRUy5JkaApG5Xj7MyswGh9pqdpBXNzP_3vRd3TdDoOxJPxuy84yzCYOgUHIEP6RHuIgXyKWcYTa0uukT5F6FrlNB8FLx7zyGisU4x1Bb-MpXz48zqvsz4gEe3AhhuVMCTKSCYzL7L7x6v_CRAjJWTVX5VQbZ84P3ZSqM1U1bF47nIbmyvxx8vOD5UC-k8OkKxOcWjVy5H7P0spENcC-H52ihDOw8916HPILDrBuKQSb6XECHLvgoLAqB5_oWp03jMSwrq-SZtguIVTOSMAo5TpPaVkKVulNl-Pi3910a0MBuqdzoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V38Y6R1p4P7tv8qPDbKTPLkJxxbmW1wiDZmdjrxTrD9p-GJZnSAS9ouV49AZV0438X5sVeFl_w1KDVC5yf8_CEyGCZvqfPSJi5CIA4ISCDls_3bD7pgU4BBq225YBl_7IPK3i11dDi0i2CHRh9ZJOyTgo1l_oTRWVP0aH4B-d5USPyzc5WSt8fPHW7674yCDvVORr9HtffixJqrWJHFvaS2nAPqmOBRWGvelqfAm25hXqnqOy0J5tTaTufbnJVtM0UUYeasGKLPwp00uWbrgkPhTvEhrwhegIc6SR9krImZy_LZzKyZ2TtVeHlonbtoh7W42C9D9NqxD9-pfobeC5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eydhqr9WCtIsiWXv94jbaz0_yUzwYKv8SDLOTfe72AWjOqrwGUuNTs6D5ZFXOnt5W3wf-Tlo2yXnqUUf49qnXrL1zDJcEkXhPZVw2d-ZIusPhHxro1dAQXaIvwJcXSz_JLS4jGdU4_ZD6vlxiuvYh9nSLWbgsuDEyLJ-VCDtqiUh2u7a0PXrPkK_w0i0ErdXxe2K3sRp11aCP3fSFaPRfR430lTzITudL4E7WGPELSk2ckryWBzanf5lIyhyJkR9XyumqwRtc81N_hk3DDLip8XVzEXeIRXT1j8_FoseJ_L54k8igPolxLTOTDtFkeuZ_kLDai0L-8xXd6hYsUPQOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkiJpaEC5j3CHGti156XUNh8RznmS-dyH2_u5pAK7UpIq0CRBx920UJg0A6N09UbuM3PNu6_p0uNuH6jPpTYu0mcBROWumaNwZvw-wIuKJeX-nS87InBN4YeIhL8wdXg0_cM5assC2Rx91XPIzbcOdECPIg_BJHdIX11qD01dEir6OhVmkbyk8hu3OrPoXOFMuNXStxlgTRAYY1qmWYcNeIlQzBw0krMxoPOy-1rZuGN1lAmKiSiO-5ZltLYbPOj34ExyJarpVJQgMt1GRSJu5YJZtIRQFjsLF53hiYo4xIOGygcITTgtTHs46yuVxrUAk9aHYq5eo1zqxJj-bwsHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdL6WWnty17OVUKkHTiOniGFYp5z3WWKIZ4w2X-0MCod8Wsv67toGysf781kfrzM-JKcISczjZ1b1Sp8Od9d_yHQAHpQJu6HMXanaJ3egwXnlfF837Jzt4asKi9QmPJGSRAhE9mvFoL2C5MvvAD4eAI5gPHl7b7FCkhAznKPKLlpqAZcmsSJNsTnmBJ4c4uc1d59Wc0_JRGvS4AZaUEGx8OuclPR3MiDpmmFVn9tgP1PzAf-_QE9p5_gydsNcb2Rfo_dcBLF_9hCO-NQO_B1QBuJrA8UaQnskQerP0BaUxzjeUbbNsPKmNhqZkakDYKgQegR_wII8ezyfGFofaOcYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DSX84n1ROCRsOxYFmVnCD_PH_5M83Pvdoj7-cvgKr78uBR61Qp9qBY9uIdTL7aM84QDjurhXQtynwn4drLmp6v9BbksDl7WQ48QzslDRAgYZ4-g82PhVJq-Uj3tTDrApUmlX3WbT54x3wBKFMhu5NiHxjVldEaV6-Lr1nm6YkxFFe1F-HZtOKXmapHaGdUPxyCOPYRmVVNIJ0Kzm911t700am5Uj0ZTc7Nmwq2nHL2Db6UD8uHQq77QVKrLMdXPHU-4piWQKQNokloIa_kP1erg-0v_IsmrGVlbSAMuvCCxR1_sClfVaQ-800vkiStlI3LLSfAAbMQfXl-3TwE_CRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUSC5LXA9PSq8m3hViClE1QZlkQrUst86TY4mo4JBQC3vYikiLr17bZ9HfXgAle4HJ22Q5PMyqrOD8jttnfby92oTdFCht0ut2yWHxqMS-gfWJ6l5PeVVHV2cYkMccJouSfwY9IlEyRtNzxc-LR8dsYtc8CSKebG80LgCswvgasy-LIlabUnfmS0xpyW7szheI3U033oy4oapzmOCMlw4CO8ChW6f9gyUfR4JT3_6l6IgjGuN8Mhc_JX7wneu7qVDXo9xfIlJHNU6UnM-wPMnNT8zM7LUXAiiM1NoJd9DSKyYD3T9y2do4vHP8atdqhJBRb65DVKf5WHy9T_Yjwg4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJJB73QKtjQ7bykT13pQ0oZnrAbLIo8IbIzlFanBxPSLtm1hdwnzHXx3hKdC6xkjp8cWL29Smeecuph3K5Sf_FGj3p0Omutrpnbdh9Bf_NcEZ5VMFkSjuVz-WELvncGs75y0miQLxrNLHLrzytrTNC4XbrnBLy5k3pipup0C4lVy7hMSoQcmTNtX-gf17YZjeIos5IBOss6pLOd1WcFBVVMoPpPrKP5o2_omLFoC5DVALutxdfg4lWyaltkNmvjls6OFgUu9TObwNwWXyByuRWE44trvt-2OZsfg8niXKEu9eJFwrBWZsCsj94RutGPH8-Z2ehG6y-1iPT4kvVuJBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTpqO-GJ0q0XvmrNBX7E3ocYdEmDgBbdugq6bTA6N4HUIWWqtuAtAFSL1rSwwn58MRSaaKXujZFrv_pabafZAdxceT_OqJhMKxhBBLm3xFk-SNtdES-CxNmR-4IyAJFXam5gtVbO7xfT52D8CZ_QAG4csTTMveiC4dzUVAnuKqh0DnESOJzUerTrQ-I9FIMO9ZMrRsayIDz4xJfmHBMqWigIxAYQyRD8DNru-O75O8ueLBjK_FKw8vXxmFTOpqtKC40BDrkNuDADPAjrHzuE_ilJ2Ax979tVMd-nUJFRBDIc6WclKjDwzpxW25FvGlNkTY0nApQ4roo-6LxgVTNkFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqCgBaxDmflgdDeEbyDzz7cMNpcSw7Jq_6t4wKBkVqV7McxGn3yjfpwfeiN7j_2tb72OlrGDHHTh6cYxSCaYIsZhsg-rfkiZAjQj2P4Xo4hs5h1oFzzhO1BLeO-DV19mfYnYuc98cVKXPp-RPNRWG-WHjBQxYbQPzyKlcUOrsivcXe9lfOwlnzxssCplbvRbcdXwz0AKw8zG5tEFp7REq8IxEl1WSHdeFq4Ta9WJGV1ZlL7RCCh2H_aB1BT7ZUoUvyWGCPMiXu-VRzHc7013D3Z25hBYqzqQ7E1B-x6uiv-5khipIGlKUMfuUaAmAdymwhpCeXLp0yRa14shVfbSgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EEEMBOk1gKkT73lCiCrCQ1hHkx2WhFoQm2CPhetbt5JteDeoHGcKLmjjWKzpUPFQVx2djj2siu4XYKyebmUVvavqz5-ii3dhVvxnoZkEUp6ggF3C7bqh6DDn5SBSPprGyEZcJuszFyQ_-ay55Zw2tfGtySc60hYfrLs-FrNNpLQyHY67v2a4OFzxf6gygjFIhUbY4ELOVdliWeiIwoLd-T6YYnMiBt3QgdWxtwEeI7RMtYSmulaabbEZFyaDBTfx5oWLsp97GZFKs200yLJqdxK2MyazmUBUH4V91WvqVd4VvZIGeV-DbyU5KhlYCMv5n_Z-meVAnJ4-PIJioBf4jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZD7DiqI5ajMhbGmfh0CbwPdV_TRTPxoLOQgOb_EZUJjb0wmZwAlhQuZckW94ndBMg8LYzIELWzbTpQPzqmLn6-6tjHqypeZyB2Chfrx91sXe3d62IHyGshJg8lmr8JmVIOvsiB5WOjFj4v4K3DNRrJFAkqKoyumLBxIRjl0dJDNvucMm9HzCjNoNI69YWBXX0X8wWYcHTWo8Wey1QUCtFdFSFCqf3ya2eA2tTNotr2wKiLqklJ4tMnXLjBILx-mfz_cZtlRUl6WGLnHfYIg3tuvdhrFnwXte82dDWc8zaqkP4vehLIfhUoviCGsQbSrv_fyEGZdby37fgIYCka5zIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLF3_hZxXywYPzvtmFPfdGNEuCC9yn-dkOqM0yE2h7AchGplgk-g7RI_xinqO54_5Oj1pp3mC33deGzZ-sa0F5lWbGcMKm2egMucNkW9acTpFJ3JKMIRqM5LCIGtIEeQD-b7TycXyktWA_7PS78F-Q4aaUk9LQyE5Tcq89j7PMw9wdRp3XBYDEapEMdV5qCOSbuxKw7M2HQAx1x6KSas9BxJbsK_G-7zzQETsoAUnxfVXJjIgaPIow_mZXgclJ63zXWBZ5bijfafBm2cE13XS6l_sVF2tALDp_5owzPuYXdarqQMvprfkkTSj_MchsYd-_7AeVlZUiXDkvm4gI1nNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JOMdTTp6XQz3HADUlt77AKTb3JwDhYlt40b-RRKCwNdWu2W3ctXc25TUAxCfKs10gyrgXnKqoqRnWAQw5luaCvXWonRYVQ8bxYToaa4WrJUwGMYyntZDN6iV2laT90mgpIKl2BQh83x9ncFvubWOMeCnnGtdN1Em-TMKZISAi9NGOcCKNYhMYsyoVNSbeNcDlc7UpP98OQEAgbjO7bsM05ryGlbeh7fw4VM6DHrafNT1bkmLLV7RQ6ZthrEv9Yfm9JYuo_O6hjE8Hp_hnmMTa-jgCBxE8QGRedR5kmS0QTqDjUjVGTG9qtzQppp9CISbJ_-ha1OrtPU1-i0wwcdyqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwFN7axXoIzDbOudpNK2O0IhAEQiSYwCgQQeITAsrgpW5aza_xdZqBZ0cRgUlWKOjpX_iXyhFcuUbk6DBm5VqqoLK-sAoppkRkpsq_BMPVqrkFlKR9ZbHAGlZFmpsAU-PsQaQ4VM8kCJHur8Lz8KE8Y3uc1MOZAfoXuQhaqFO0-zQutElLxE7GQhNNTGmf1ojBlS2clOdTJ95vcrl-1sL0RiHdL8SytAIWkn5c1m1WrtLDHDyV1qoAgt_nK4C9IDiKlQqYoE7K5jj24iLp3eOYwiKmX8GfTyXXHyAb3uAVznBVBAcOFYcIf7oNVorlk7HSFXkeMQ9hBLfYfmRlnz2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXv08DaH_yni4EI_Lv8UEsD8JjuCMEj1usoWbGDVK2FySxCeuc2JJB64F4yAvSWrSukrl2EO4w0LMbmyjGcJgTOBNQv2DwuNTulZbvYa_kKEHQj4tuJSWmeBS7tUOf8xXq3ACDsd8m4Gf9x5HAagDYImEPe0yMvG8_EnnsfgbwTRSsTuKi5huhmxGS8BLezADbmFJsNMiAVsPumz3NWRT4oBq-1V1ttdHT8jFX_skp2mxXWe20Oenzxc0i5BT3D2w79dThSx3D5meCoH6mXawS47HeR5oXmjXnRZwgL3PxtAByweTqjpgoov2el4FV86LTayp_IvuvnDGbiFKXbUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9c9EOX_WCDP-0m5TcBOURfYozloGC2-EqZyUYHfL4RA2yCr7RjPMlKpCIVyOCaPnVJ1AfgnUZYvVjFzhwl6vRTRZh4Oy4JmbP0nvwq5uNV5sXxLt3ZO1qO72KZQbmdeD-zf2se46KDXxgf7dOb_KOdi76SLgrKMNFPMxypVSCOfw_oEgKr8T4wpDwqkuZvpldlBJzXVm3N0CDwWJevGHEPCsVn8B5rVy5JsVnnwvq_o8g9eJwlreFKe4Owa7RoHkDA84-NvjMiiLo6NnEe9zSJs29i-As1PUHafaWUq-7sxFlmRq5DoedPRFOH3fALJivzWVBrJmU5QyqYmdxcqOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-VlD-wew7Ns9S_14yEMlBtokuLqMx8FEpoQ3RZ_s1y_CMA0gIcDOyyuESGTQCjvzgruIR0oItKQYh9ujNlVd8JgD3Gu6g00ODSn2i9JteWOcAwmLBwZlRgYZsVCpwHK5jFx9XB-QngemUCxaomsC9_oP9Gn5uZRFEVxsQ4LwAHOgNWfvNczKJx4K95lOpRWYjPSjJP7HHSozrscNNFFRlWxbBuNH1aoEa1ymPFBtQQts_l_8p20j15SCAaE72gv_OxBgJ4wYA4m7yWAsvw_0BuvnKvTdSWqQXoGiFnfm5PByJ2RgrduKdjikRkcXmhUzwN0TwLtAadTAHNTWEJ9sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ld4MY5fTKJgr-AQwHV5Hd7XtUVTNpxFchmxvaol2NbRPF0F0gZXVtAdxMsH2hIi9pwfIte3VyUnr4f6sI2LG37S2H80x0Rsw8neUUBxy1wnEO0Exa0CtqewdZnDDoljYFu6w-nVBtn74uAyYbohwNnhHoRq_RKqj_m_IxFGUgrqNdMjxWjVVA2_H0HtXwogKnDmjwwQ6KF4OzWjtcykVAbp7sCadpRStlU-1kB2pp8SFRv6pWzRLT_jdpnXsKCKdMWg0KzSQVemBeWIGTsBH80OBE0o8BULbtivRZRjpUBrir0yVgvSNhcw34cT53_0IgdjYKcMRo7ABrB2TRXECKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRRB3uW6A8rseWv8WIcSxtjYgMUqnENsHnIX27xFS5XJZuPEtwtCCz1Dhz_Wg6_deatu11ICTv5IaPtv5HMlgLTGmFQN3fZU5YPdZ-FKHfpfUe8EmAECcwMUmijU_d1wyoL83ZshjSX3tXXIU0LFnPlFhymG9ehgfqxT_ncs-oN7kRr8xmpLhk3tgRmhcx3FqofNoESsZrvoIFKQRwjtPAVCIH4-1Aub1Iem6RuCoqs4f2tcDyt6FLjSS4tgLnPhroNMiJm775YJQzCsOkP0BisgVKIbZn3_-jBciKokntmQxnpE4ZyMd_eMWu4YYdRLEcXKALxrJgwqcT8vxDp9QQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFfuZSw4u32c7C4wE6zgWDLFg1iTs4Y1p6s55BWZl40hwICFLYjtv659Ly6ktsQk5SrIOf5qE3oJfSi8yM0kyI4cK2MQe331Kc9rN6jwNLW2WZ7paN2svcFf-OgOkAl-T9MWKqrA_lH2LI6TlFJEyBNN_rBLqVkMMlpPRkNkGnSd_CwhKQ6OeFbs08WGtKYtVUl3Rq0UvtKQC6Q4kGB_vhj6DjVwkZi83A3vXuY3Uszpjcwd_pu_u2EcTPZ7etY-jeG2MyuYwdaYwEixtZwsWql0_nnHO5ALdvaQqPey-cijXShkCC-2FWYwv7WvVZaXVY1z4FAnbIvW62zRIDIt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXWccj3UltsLoSuWlvBkmLaANJsNPhpGdTM1RI9HuNf3m0eFWiKVAG9UmZ6HJNyvxfLEz1atY69mK3CzMRe4qmw04UOePpK91fZQeWJAtrseSsU5IOsareqboApsqtGZW6KsnrY9o17z-arC7n4I7FslS6NZCO8k5b_h5giMHR5iE0EjS4q3h8txzzqGnC0lP_uu0ywIfOehJzOFGwH82LXdabA5BholC2cZUF5Nn1Zd0ZUiXobrNyrsMNBoNigZilgN3oejZ12CHXoA7BNmNZgfseTPmfcoNITx_rlWMcTTC_XieNYMQjHIlirQCjfkp1cSNo3RgJQ364Fx6MKmbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eySklZtrmVFzDvwsXtlGtJpxcXCZiMV-4SazWkyUfHHnNYZenxvzCYXmXMCb-ZwNyoQO2P00MzzNq9aFBqBH-4WLE0OVKFdACTTHlD5FWo3AwFC7eNqj1qcwooYd3ZS3mN2ZmQYstvHTK9ynW7T9V0nF3pHwXAEtpGH3RTn0-EgoXW4ulefWoLylZuDlymyrmd7E57Q6OZwfxQq9YVBshjaQByaHk3jqeRuJQoOodJz3GWu3Bo4lTfi8I_VY-PIgrbJMhR0Tx-6gWnxD0_xsd1HVLpwpjFAEnHwLDLic7gN4lqcCvTs8mydO2MWNCliwFe1vvcp5ZD6jvWiXW2MHWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIvFSw24aQAdyGEOil2fgZ_w_oDmN_pjYuBZX9N-sVH45p-K8VJitPudwjZOsw1nwxaldxDPPTn7R9zz7683xEd2iBjS1zpA-vwQu2lwBLGlZAKPFeM2uGqNyjI9lIOkvzBmBHqE9TlItrwMI452QhMndwq99_UztRBH2r4o1PixmOjTN8qN6Gf2CYLEGwnCI3zqhttIt9V297zv-CFTsQklw_O2jnCqJMUVgAx4AQ-bbnBG_auI9J7S0wDA9iJ5VeB9aHFWYVKk-KKB5w7F7k2SPKiZYZOmX-qGCVjc6z-MA60ZZus9-e7AXWYJJ2eJm3p_9CQ83fh7rHP0uaUCCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI3oSZ-GJn9YgWS_omQ8H5BLy2z6JzqHDIg0dNzhF97rIhmGvskTN1qO4tch8OE9L7Rd2uwQX8qpzVTMqrNaM24TIyLeLhYJ6RHR_-XzKXbN_sXVQbjNtYmgZnsHnf8cwTL6PN-rmdXgqi3HRLNxs-eZV37HQsSMRFOjWVEzV26F_FoSEam9usyYxOfGxPdgPsrYvVL9j9f8C60N7ooaf46erfXDy3TJiG3vwnVzJQpwW5k5sgaPGU82hT2aTb2Z-pIPDLyTpxjmvv5_11VmLbzjI69VC7ZYOLuWx1T9_oAeXDPWX2ggBbrvhiKC8XaHg3KI-Vq3c1MgFkBLPE6WWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9tl7jVvqExZ5qGt8EYNskgfPr9xvGcdvi66RYy6RQ_2PjOY3aQAFPDgP0xwM9eDS6hbsAArav5iyrV8tjsd0N9_hKGjzUEg7AcIH3siV9sZl62Ooi_QScSb_hWwo1RgTyzjuoRsdXIBDhWfuXfRx9KVkPiraImLk4Vwgyue5_6SwGuEzJJ46PoV1iqgg1o3-wWW7XiPYOaZKzg_o3wVNJ1ZKFJpq6A9tebzaN8amcXEv4PaVv5S4hca_KEGoWMu2BdGSMgsaSbox_94oBUqdbNQuU3v0SgHEyOIKj0ElXdgOsuZulaPUb5ooahqr2507SC3gjTJyxOe-S3SIn6dqg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Aszp2PbdWffDsDnqS0UywS_BW5hzZVhMqhg-J_F1Yf4FikhtVglP3jd708bdWEngjzpQnMSq4-AUu3Zi79TYzVk9bMWjc_bdhmtkbTrTPnI9WK7DrlUaG0YUVZ7veR9IUN7pmrn-dHn9FbLoSo005tcZEfocPhp9wvhWv3NIzSFV8JqEPrg4y12pQLdLzirYsGDp9CxeyGj-fhd3MD1p1DC_Ayoes8Jt9ApH6ha8FnY9ZlcxdgRAhTj4Gi2sdSR8VeuVZtWlb8M6wB0cuATnHehSoC70rv3ZZtl_dS0oR6T39b4nbUB0a7QsjUShzTmN-VMcQKuIAxVP95cH6gUz8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Aszp2PbdWffDsDnqS0UywS_BW5hzZVhMqhg-J_F1Yf4FikhtVglP3jd708bdWEngjzpQnMSq4-AUu3Zi79TYzVk9bMWjc_bdhmtkbTrTPnI9WK7DrlUaG0YUVZ7veR9IUN7pmrn-dHn9FbLoSo005tcZEfocPhp9wvhWv3NIzSFV8JqEPrg4y12pQLdLzirYsGDp9CxeyGj-fhd3MD1p1DC_Ayoes8Jt9ApH6ha8FnY9ZlcxdgRAhTj4Gi2sdSR8VeuVZtWlb8M6wB0cuATnHehSoC70rv3ZZtl_dS0oR6T39b4nbUB0a7QsjUShzTmN-VMcQKuIAxVP95cH6gUz8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYhuIjH_2csXhbWIQzm7RhPCBU_8ixwnn-DVKwwf4WlpbtgfjDjJdcoOnbXLw4p9IuYaGZD0MZPyLQ87a-9K4pgKG4RdlWteWS-Mbdem5BnZC037Yy-jzWnFl9uP1cGn1icRzXYvHwhERmrARfr1jE5bN_p1Ni1_IUjLQi_cXFdy5-CkyBvFLaBL2WrcHVmyWK0d8pH6ZYqJf1lvwXjv5ReWY362UHznuEQqQQZRjuohV7J_US5V9Lizyzv_a0-5V-yaVVLE5-0pCEtG67hW7cku06u70y9DtmpQ6hQCr8bl8rnDlRQoC4Gprmc_Ei4p03YzcrLWycmeasr5d0VSkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naKIvZD7czvy6OFPfgKcXcsuKXBHpdFv5rBlZAI3_u0M09D1ZFXSY3pzC7wJJi2iH7OMrqZ53PciLTAe7Gt45gIhOJPkO4cCFpOfFfeMaoKaY_MHLKLBNq2NzjWVFOsH81C2FMhUAqZHyt0wTrHLj200N65O5Aio0kO1rs9YW43ORCRlgPPndTU_HQUl37m6i9okW4Y3rrhFvBz-rqJpdoav1DMgIOEQfc5cW3GT55G97YX_gDxJAdoaghwA6Yii38cAlJJG8bFbRkoapRxjVU-42GpRqAfu9ydxERht4FxK360hYc5y_nxmqlpgGwPLmNox_oimJyjiC1Dxt7ZEgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWWrumCBeSVwBMHM7KjBPfhreF2vhbZsp163Fk624Kl4wfBZKu3qxQvMkK-VFJpePvlXrLZjx1wgJfA472gMRLVLfUZVJM9yHoKZO5rLzNWhvHkEvRo5mMHcM8x3ZqHf82IpzxiJ35RE8JVWbUhgYa69RXMTIS4K7DePj33SUbRnEZfaMhcrIDMCprJEEBIIElHwLD5MkAUCO2-UOzNYBCzQT7IPiZtjtXD4IsXw1XkhWcZiyB-biri5pWFvaXu_0z7VvPsNm1_zzCb747J9TfMfz_-KQrBFVO4lyCD_prugcH7uhhHn20nlJWotjbhQZLN5dLpDxIlH1n_oqXvbIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I5y0dNa7H8SF3DCBpjpGn3QiaQ3UZGF6L76j-3_ZDvmtduhedyDYX85Qz73ihZ20lHTvi-WuJnHEnWI5Gu3mmSxflR7Gs9gtoBP-XbaQK0hqX2iW8OdQoKej2mkdWCVlDgGdWu8tYbpxZM-6pEZ8N5P1ww3bbONoDH_-uw-x0efgxfARCyTC9QMy6ELuDzVG1juOcdTcoyEw4TzClVjokg1mbLDvhKvUtC3-ppXKol6FO7jQXSpb7CPXlRZLRCaQnT6fqrtyAStP4uJDXxH38vIyaNwq6iwZdnVZzgc1MOCcffejNsfBoQlZQP0F507uGSkF5ztz8EO5uuKTjt9e_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iAX1C_yBPb0rFXygFui3ANnOLXT85A31mJi9F5irphL-Xr_QDJnD4Eg5MeuNiLrIV2keWBx5WBnKp1a4gqmXpykE4eZd5TL6IS43irQvAdvwODmXiBMkRcmS_0nWBX_XKpkOKj4DjV4DWs0JwNLgFXc_w4QHoSNpEynpZvTORx_S6zvSB_FHSFMuy1DTP9Kkl8s-aAZS252CgKqGNHxfhDEM-g27VJDPIK-6yA1Xz0H-Va1PpfRdoTNWMPrD62zXhHDjiBdvMB7w3Ss6dnNb91O-YpDkAjcYm2C7B9xBHw3wVN5Pn_N6fmeeJ34gVWODR7T_2O55GDeJ2syEFAnfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hnl-32EgIE_YjwOEQs3cQVnXO5LZImZGLfRPT90YcSFJuaRbPzEjsYfT2l4--VyexJX9OzWrkAo3ilxA6er1_-d1AdFX5K-EuU6_vPEIDcvURb0l2wX3BhwqVtHnlA0UD_su7tGb0Ccehq-zY_PP3F63ZrptHdpyogVieIZeMcLqQwpxeAUWXgk3N6NgFwCkpMQSQ6bD7xBpcrlaXaYSOTi6kXb5Cm5A33ue8-49VB93yugaYi2gQM8JToOArDCew3CIGgaZI9qKvGa35Vr5YPXh3z8GH-blkpWTIbW-ziBI469w31receH0ouAxzauUvTWpGAez3-WrhFBtRmIhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQdh7BT7H6DRU08K0jGfZi_kalexocmG14x648nBxyQtW34rQLGI43xVfwJEqE1Yhkf_Wb5XA7WowUUCGLtck4NIAl30dY8hjnwPXD6IBrRY9esQq23pXjtE5kRg9wUfHRoasBGI1jV37KM2a4rDnAhDBsYlKsPxqRfOgVnI2KSL14tOnwFywve_6sbGWMmnZjD3A3dAQtgqPqZXYWO2XlSNPjzj3lE79R8DhtYsfeuWwVqK6ts9JRCdK527-csHrkTJUhejpNbrcZ7QYe8UEkP8TXEzZVkwzNJIH8BDajuvpgfVyc9Byb537qmUrdKwNnQO4i2w-lgLqQIuzL5Hng.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=j0wKk2efYPw3SBonvizmv5qcZ-qfFxahGBzrrVRLr3iscFQWnGwBKnznVSPcReDO7vFkwA5dj-AgfejH1mG5GLqM_BlGPfIcLP0StXIkUdu2JN-7yfjtmNTGX0fyHVCRkWE96UAwJ1BHyZVNHYQK5KNIX5jjp9R-uRIo1BtrAs8HpIm3qabvg3y9Dd8gMdtQQzhBfFlsTxJeOI7bgST1DUX9S9TZg7WD77LY3KvgAkaearS2BHBC2xFc9lB2vAt7Jxn1QZZCNrTxa8sORNSSGMl7lEtgQJmrfW6kgc4yZ71OACKycP3EsAG3Cot-kw89JBk__SSHuA_Wc5eYazrPjKGdDxgZkWVqffo5CiK6BKZUj9qv3D1IlEnYm4nIRnzjnqHc3c4-pskyThF-6uoSF8zS4quFY3fyJvK5NSVQwDZ5F61Qr41voM3FyVhmOZ1Lr4iIMF0w-CVPf8TIdNmgQqcWIWuWsX1hBeY4aKxzhUzf1tHtAo5UDMomNgmXp7KeuIZekQcPhx5hUiq4G5KGUoSy7Ii9WAFslmBhNNIO_X24of2orrPnBbUQM14ruNCn0MFpQj3_NWSU9JJTeplmtt-kBw0bJj0eE-MgpXZsxqAv-sQJYoHB8v4Ihyz6LIdTX_t-apRZJnPypVl15hIMXp86w9Dp42QUWMsY35xnpxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=j0wKk2efYPw3SBonvizmv5qcZ-qfFxahGBzrrVRLr3iscFQWnGwBKnznVSPcReDO7vFkwA5dj-AgfejH1mG5GLqM_BlGPfIcLP0StXIkUdu2JN-7yfjtmNTGX0fyHVCRkWE96UAwJ1BHyZVNHYQK5KNIX5jjp9R-uRIo1BtrAs8HpIm3qabvg3y9Dd8gMdtQQzhBfFlsTxJeOI7bgST1DUX9S9TZg7WD77LY3KvgAkaearS2BHBC2xFc9lB2vAt7Jxn1QZZCNrTxa8sORNSSGMl7lEtgQJmrfW6kgc4yZ71OACKycP3EsAG3Cot-kw89JBk__SSHuA_Wc5eYazrPjKGdDxgZkWVqffo5CiK6BKZUj9qv3D1IlEnYm4nIRnzjnqHc3c4-pskyThF-6uoSF8zS4quFY3fyJvK5NSVQwDZ5F61Qr41voM3FyVhmOZ1Lr4iIMF0w-CVPf8TIdNmgQqcWIWuWsX1hBeY4aKxzhUzf1tHtAo5UDMomNgmXp7KeuIZekQcPhx5hUiq4G5KGUoSy7Ii9WAFslmBhNNIO_X24of2orrPnBbUQM14ruNCn0MFpQj3_NWSU9JJTeplmtt-kBw0bJj0eE-MgpXZsxqAv-sQJYoHB8v4Ihyz6LIdTX_t-apRZJnPypVl15hIMXp86w9Dp42QUWMsY35xnpxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYQBdYQxNezbAEAxvVZo5PMmFgJAxM0_XPtWww12UPwG3XZMsOS7RgblrvVbLrJiUqmZLZa-dOSmH3PVDr9DLEggaeDO1ka8avxVn676Mz1Kc4jr9IfkKXLxVfoH-LqEf9sstRZ9cnn4oiGn9PkiJRXqlAPJ4MeBqt58eN6QareEAsJHSR7G7i6lyCP7pcUiW7s9-Z0mdWvpZEDVMqHpF6jdHTHZdvkZM3YefNi2ooMClbUjGKjfFaF6ockVrqj8j1FXSVQ1PDZFxY39wcXM9gUJE4X2pnhos6pejTxZVN1cerA2uyn8tVkP8kfWqgX0htHmY5kc0XwKko_Uy8LKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUOcWS2rg_ymRsqNoR2yUPuX47VyrWvE6U7uXWUXkc75vkG7Ow-zRLy2JSaUo0oqEFUqaCWHL_NtGUA3pj4TVPiETOeMeeoL0Vgt6FyWKk7bGRrvB84l6_d7tv4muQ54D39827WxYHT4ub6bGtZku43fcIsianvWMs8sPtfJW2E3TESEP8yqpQyCtAVqqwhBqDYYZkVg8pGffNr37CGHdvKOne8axIenti9lwRInzUK3Mdlq1BUx9quAr6f9XOpezPZaEmqU-BCMTOOW8fEkgaFT0cxdCItPdPWdgp1DNSH-9jsyHbkpwuMfSPaDnufpikpuSLxcNrkN3c4BUMJwSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JBZ7r55hDZ0qpkF18foOdzBEVtlB-JgvajTs0ODMTORMp_eclGrX7dw9H69WEqQGlQCRWFzS_1tOdLdqTy2d7ji6ZqIrZY3r_rlO1etW4kLaL26ldaIvSeCDBJWuzczfC_XuYkvG-g0PmpR8DBhzZonFt9lmdKLPqTCHq7hXzdTxNi2Rdb9fs1RfHKNCbf1NILF6lvZBuvaBQllfF-E-072RJ6yeFkBD2GQn81ok_w_75nvh3JKnLhIioXfDUOuoWscrlXzzD4XmpXe8E_kMblkvfJoEEr95a467crHFTCusSB6bYXfkqO5O2tx6a-3j53fqyM7b5aCRN5UjimWtkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-nh77MYTA_XQr9dhpN-cnIuv9NJXJHG0DIE0pdFhej3WCLol_ahawrvchrVyEGpvoxe8McDND325-mI1v0CdvXdZcNmeLwrJrFstVevkBP6-VCxSEx_0kr0-asIV6u9ikVvwSPEUle7PFeHHWXxBpuRSU6QCM3DH70WHHxACFbpE7W4yt5w8L6kZh9DmVwsticIvukcdHbe2xT1bt_p87DMevexPlhFcbY7MfSuEYVNxJ2dlEYZ1ZoT0lEUKO6CnDZ8c3jnYDK9X7gQiv_8a7E40IT70j3iW6NpwnSc_IKl_ISOqlGA5PYh693XQbvr0EyKhvKFU3AjSr8CoyZRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ouESnQ2u8AanDoDUcUJwEjYjsGWllgcPFxajlGbrDvcFvDZqYtbak9d8B7Yl43tkLoOFsDCmFH22hkhyKSQSIUzSab5GU6kyr-I6KgMDgUZEqLhi4mJkgeUI_tpmNaewILKFHOfVyoQIH8uq7bnTctjIPYQgunFqPR43dxOBpK9r9zaMuv34CZabmyoBcgaj48JWk2QqjWUa-Ilt-sdMbu8FGawecSc4PUKXp8Q1jjymcoanSb0aZ2Fvdm-mwTQzApQkVBbkBz4brxidJGqmZKwNk0QxLKaoUC1O0FmfXPjL_N4x-SsHpqwYEoyr6syBMG5Na6Pj7FcjhvfrFUC-Mg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0W_B8zzjhwNBQ_6noKEYClQYLx1-_hkaeIWdY4vluq8sJpe1ijRYy9rV6Xbodoyy4gPF52I6_VxbAR-5AbowDufCOA5OIfdchy__M-2HKeOinC_LFLyNHY0xwMUP8pbkY1lZLrrdAxjZ2FHtxTWWn6_aWeLcRm2IPx90Ykol_VGGA9Ul02aL52TJUoRnyqgVA-rqoLIzySdmuD7voA5JpZbcHgoxWRYBRv7O_UUL_qLb9VboG1TH1T1LXxxOl4yusy1jWpsJdx8o3R4LLhlQXuUtAU8XBHAgX-qQqSzJu6g3Zm6Ean4cgW_zV6AmnJsDgVsoYZUwWGdRcJYbdmDmLHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0W_B8zzjhwNBQ_6noKEYClQYLx1-_hkaeIWdY4vluq8sJpe1ijRYy9rV6Xbodoyy4gPF52I6_VxbAR-5AbowDufCOA5OIfdchy__M-2HKeOinC_LFLyNHY0xwMUP8pbkY1lZLrrdAxjZ2FHtxTWWn6_aWeLcRm2IPx90Ykol_VGGA9Ul02aL52TJUoRnyqgVA-rqoLIzySdmuD7voA5JpZbcHgoxWRYBRv7O_UUL_qLb9VboG1TH1T1LXxxOl4yusy1jWpsJdx8o3R4LLhlQXuUtAU8XBHAgX-qQqSzJu6g3Zm6Ean4cgW_zV6AmnJsDgVsoYZUwWGdRcJYbdmDmLHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mvts3tcPMNrKfRldn7JQT7YfqeB_7N1Lb7VYqxuZACnuvLYedDsVyrXgWC4XCLRwgpvajvg2VC2vhBv-YxzQ74CLTEyJhx_95zE_miMPdeH30J2ptjEQ4aBOiDscdSxVCI6TDIqFGbkgxpO1y_i0AcjltHc5vtOxlD2vWhdR_bwL_xom27TF_ciEHepNLDmFyPD19T6sgXZN7PUcmtSz41opAR4r2USlxsXSLH9ibbBDhP4Jqxkh7eJM4ogwHCOZHXcFGYn-i1B19j5COwjesttpBAugkaLonb4k1aLYsIUBmePd64uMuehnZD2bikRltXypA4Ng_0-98mVuxtyLcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lksPQAh0H3ICkmsB0OK5IIU4oK-JKfvUx_OtwFfomZxLIV19Usa9KlnQCq6D1UGB4hscJ_PugAKny5KRkd8Zv9sn0pxiFjCt5WTiZKPvVx6YaZ09Lc9jh_-qzSIKYqtdZe00Sss5Xx4Mo4zGGVt84uWq9Mi6AXqnYuYe3qJlOuOTM9ERnGjk-wwbO3Rt9g4GiIfQ8t9vOiCphVSFYiCvZyEploi2VBKO6C9pJz2XDaDWPllwLnhOZidr5GJOMifqxyfM-tegIEfN60El4KmeuypmPtPMrNjEt9vxgmMnaxFwvABFmr6vvlzoCYw5eLsl5N8mHPPqTiyLo6LEAPIq_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hY1ChimtaFOY0dgQKZcEyQPRtp36GPYc1OOXTzEvDKzDCE9jcbgwTWQnIsjRm8-lVOdPf6XVOM3h6ClrcQyVETNNtEr0xtuJOVVks6VQp96HUT6JFQSnbAgRt4KcbAt-oW4c2f0K3g--VDixGP2-exCwycVLdZWMzHGLGWrmO00evAw-SqSCtua8KEv8HmBYe-Gbi4_74f5I6oeeY22XcbP2mABJlLIPX6V0sR0fAc2g5B2eOpSJ6mkgFtVySu0qwnP0_Fug4OYYT42SC2OZizHR4YWugl-EEh_9x3zr-ClscMvlnxDnFtFGqB5gWvsfE4hGp6kKJUzRZBzsDsXLlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PNjbUPkqxki-Cg5oxxcnQ4SJRwh-zcDj8BedGrLUrbhkk_FRUQiSeH6oxdSpf8yv9qbbnWFZSDR14dMI-0pgDRllcALgPBb9DnNUpUPxB1l1Vvw6WLMpKGhA_bZSEApDIsL1y6wDQWpwDE24EXJ2Tq-C1yckknvEK3f5qz5IJ8ZyBV7z3WT3LRo9x7h6wtZKT0bwU578yfdXmEZWfRyoWDN0n4uIzKezuJUqmhnC5HM5JD_c7uqc4LfpNyAktPgg7y6EqXmtA05xTbzCMVkbGsnC8tnkSjdLyMqPFjZFg391eZKq5JcthfR2qNyv-HXNJHO8YvGLyPzWyR6HdgT_tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frbKABOpa-ykU7x5eZ53EO5sy5P4NPMFuki9Nu2N1JmTovQqmNpS2OsLk99-Nx5lr1VgD3tdMhxXmLoqWpxMN-qZ1UJL0vmcCSnyGZKp_V4UNKWK6nLEMIfpVz44X_SbD1d9o3RCtZTxoM9Ovk4wujxfVSQXcMSmY0OsMNUQ1Y_aK0UpV5nENZWRp8w_F2183DHxykMHw2XaEIimIRXjH2Z1n2oYD72htZUCHxZdY4AUP5dYYsFTmtT5mU6K1vLxQOjkc61A6DHxR8oHwY3QWIqqIDFuzxXYknCVVrbOJDodG-hufSEcHL2k0R2_7_iC-IQrQJjWazq5rDDbW-Ge7g.jpg" alt="photo" loading="lazy"/></div>
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
