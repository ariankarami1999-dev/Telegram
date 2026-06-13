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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 11:49:06</div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMXpnr7zGC8nsnSsh0atqw7XEUYmQNSWizldmHVyA3K_ilUZ9QiSrwDFNiovfpZP9j6O-4_HiYJWR5a9WhgTL-nGnqEvz31xcIjfMpigBTSsBetHCEGGxmDTE5OmKO_O4R4OdChNi5lmv9GT3rZaFMxvSRf-aESzX8woMxfnXpgrqDrtpBU2rDUjAv2x9fWOLUlyW9ex24rXyLTv9SvdoN9ERODgBCFs7gGMm0w0On19AL-gI-wMvcqFQnm-12g5a5keyUczTFmY_O3BC97vTWNXmYLhIeeogqbt9MYoxGsgXta7_OtSfKbrJpp90CQHVGpg0ZUSYa_E9ltjFpF21g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkHxyGTR9js7kRmmfUchWL7S7aUkurYbWOfzgE2r_TKTBktrQnhnz3rp67FO29GQvOCTvETDHehLZPdikpWjaANBdV5jDAT0S70WjEMkkgy5l9Vf2x6AD_oOGJ9JlI-5v329WKjzn4tVp0LcMg-uyKvv7sUCV2f_exPg5fpyr_ugfxgT6L9mr_kaM8tpCfx4v8ruaZZWlafxrjUXqxtnD9MZ0aG3oEGvjEQpS3tPLcPKWI6QWeHT_diXz9QHBoFjGvvdVKz2azmJm93wXFKFYbDoJZuhPIENfF3sKMC92-i3ymdGkWGk3R6M0wembZpW-LkT_W2k66wnZ7Yh0CpRZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTtWpiYoRERR7QtdhnHY9SEMWT9WGRmkOUS3hyrhn6gbfWyoUsjmeEuF9MIRU1dv5vi2zAGcH-wvBZ0-8vKI4G7VYhZY9XDKmFl2AMz0vy_RGNjZSR0dToeOVwLeAAyyPUTW_EZZ_xg_rP8GnAk9WSjkfQwyVFPBlgZ-C08SxoCHF0gVh7dFaMfFisrDr6Ryzdsm3vFm4CD9xqQhyKIDG-bFVyAswh00_4u2_8KeR6ZOjARWhIDF3PUwW9BbzaUoxdMl2kfwN1xqEM1PO8m7dVZpifqvqwJHljNYf-NeFx3LBxiJ7SLIV583QEejkHkj6po_lfxCpAf_MeAok3rFXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbLck7i8iS1V8cBcPzd7Yj5Rw1Bpy8Et63mQXPebVyUfSHT95a3Q4k9lh1jNsa55IpCaMNKOSvGWTxT1-33VDzRr46gmXwQGQfvYqfZ0K_ahx6sYjvfHepgVssIYjoBN_7DAF0see7ROe4c2q8mXKIzvIzaXXO-J6fO4HpkxOAUOmn97Jjy0G81QxPsfLYw5h6ubnEiTpPhLugktzh2VNdNQ4G9TqPCUkQuhUcV-QX1LNrtnFQ7TdK8pqgolsXXcM4_cGiGfZvIuaZGTk2CONOWoAPnaFzBUsRVGvIf3RfgXF_g1x_WpoEkFNsMZxPIwJw99asnrw-yHzrceL_DpFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5iTeRTZFpt-x4NLmUFhhFE5C5rZulY_FW8QRW8MoTT_4Gn-QgpJKhBZhGvPVS07qJoqWj7OUkqP9rcfSXNBuzK7-ZGH2ps8YrkIT7eQbNFBjq6y4gmK-aCz24WWLRIo7Fo43RmaxQs9cV9veMPrOhprkH7wKZEocuD7P3Be5FnSIZg7j1uWE0Zet1PKnEon1INFwcEMr1ISaFy-pnvRv1ju2VNhFw8xYUT7pRfPXhge-YoBQ-tmhFRt9iSCdmGS4oFZCudvUmwOieKuMIiTIm4PBSmpmO4UMaz5xBI-uqscjfl1H1TUwleUwaetPxgOMY8ul_huJGGSZMtbOfvs0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQkmI1aZfeLVyRIwPHAbc1qEYPbQBuCzcoq3LHC4gaXZudxTbWTIfiqZp4XCmMSXLDnxkY4msUCxNtMFgVnnTvYIeoKe3fgQfOOX1arG-s0XINymowZlolzP_hoeZrWiFuYb0owOum7vtCXdxYWefzKFdHMNZp8pVSjIAFgo9fI_mvF9f4x0mgcKdWk7Uwnszw9keEI7uz5aBs8JlvQSznM5RigwXGsCOkpASyTq6K1IKG9MmQHlI1dXf2BazMNTQPuwm0Ih10YZ8HGT2-L_Akyip2JHF2ycAP1N7m8j2mb347ajF2FJtJVLQ6mtfHFBOKIYov3lEwQf9Dhdkf54bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJsD4PrGFMjI3AazBK5urEx78HtcVBgGHY7Uo10FIaaN1-CChHzSLbCacHgAL0DcHWwueRsU8IVK20Lvyo_-WKkLUh5AptkoqjlCujyKRsG_RQTmme5tljOAf07xj0USCCcCDQ3JDhoZ9sZKTHzLZY_pCzMN5N_9R8HplO6CtzrwcF_Jvt7Sf5E8nEi4GgbqEHo8FBcbtVDMUlO3h6oJpVR7Uz9hdanAxHlVCWYZUg0AL-D0rSJXxR7wtIWhcGC8eOS4Txs3SBLAqzLFJtl102guNWXu5qO3JHitwf5IixTCoVhQ4WVk3EW6o7n1K-i7hnrQ2w3pMl5pls57XVHPPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9XHtx4H3QRlGm15rFNU2Nkfba61J_E2y2j9XGboyg1XQPMvmlQAXq_PqoQ9MDOg4ElP5vlYMtB_V_47uUGkRM8h1Td45L_DhRgB7B56maHRlEjLaB7KYRr5vdsOPlHiMyc02gBKYZXx3BbaXdlEBqqDHlZz91aP0eQ4A-ejP1cMxgsY7Spk8lCAvrBBl50zx6_nfNsbNQiNvvXr9QFB8j19mluA0dvrNgayx7ai7WnYabVTQ13W0FuHcsBkRklnVUnMIxDk3wZ9F_pUTVMmPoxsjixfkYoLs-Si4OdUZl7qEw80Vg4e2UsljdZVp54m5t4z1JFd2lYJGO93xb2Tjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOccW_7ti6klgh5pUJv-CkyaHZcrcB4myxL_k79y3HPS3szDUlyHbw2rwETu7_JySL_13wd0p68anmo0E-cQtf484JB6fu7ICbx4i1pB37MVazzcbBT8HqBc20GHXts3tA5cqAFxPh8731XEth1hbK4kB8tGuDklLeBzJcBsitqnrhTdmblSFyjrYlQ6VwcyeXxalXDynaPOEylXUaSsFWUz4x1uGB49-q99r4qKdC_rRvSZgWejsM9R6Br0GafT6JAckr1L1ldWUgeP0-zFrkZ-W-58GySjfRIY-iWNj-TBavV0SdVRrwVBCeSqe-2Jo_fq9z9BC0zZhWH855gipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPwJzKdPEZAuZo3XuMcXAGIp8ei0wqvqFI65K6xqgvc-IMZpaaXXIZDXPSf-1Q6tR8_XFdNbHXmAShoraHnmQ0us_yLlp3vc-jIbl-HfLgMM4H7YVp3bw6yHIUNp_jgZBdLClrlcI0CcqW6YJXcNxDfc2C9t1Kl3mOUeZ6WMObQ6CJM6ORBXj9kCj48h5gWgoJo0uDAzV-xTe4IgjlrqbFi9xMgsFieBeKdp8g-I8RWSwrwUhkXF_i_2IGRef5jzKs7lqZHYQ3EzY4bxSdJz0eF09E8S1m4deopK8awGIncm9czb9Z7AUyKWC3s2G9A0dGQCAZ0ZvCThFeHRSKOJuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAk3MExN3HNGP_nHF4t16GeYxFZkHgNf0Q9iRd3dYN-Iub_ON4tJyLEQavmba54hsd-4MiOgdh-7TUU8L7Elo4xiStxottNjMOJn_B9BCb2T0IKGkUaNePwU8jVyOpNNrM88DOLywEHmXj_9Cpivjk2HtesQBcVRcvZuer0byH8xQC2raL4EK3IwlefRUWbBa-E1inxalKBFFHoQjgpBVZiGEw7z16a8733CvFF2R7K9PoLNiOAeIfGQ9xhCteGqmcbK9HFnyefh8l8n1X4Zd4q4TUme-KP9FDLe-UoIMbuQV-lwclACFj6CUW0AuDubnmbIELSjYrJCwoIybSsNRg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=tsUMon_3uzrhmdX398JdrUWZFpbXGDBMxaZ-Pms6NmY0A6R9bmOZwxp5e4Y_NBWOPJ_cah8MB9kSLBURwzAg6Cm5d0FCzln2cFAdINdBsNiDz6LD1bxRDGrVHhs-U-GpW_iipXMAnYt7iJqv4k6yaFBDy6LWCr0-2J-o1AYdcposZpqbwAWcrQBnQ75018xYsIJVa96z2InxpPXFLObtSg67PvvT7Pti-6APdHGtlc5dK7Br6dRgcUWGNgxBuPz46tU4SG-rOyXlHjKeZXcLwgS-MEttxqMx1eo7k0wko_FVDVX040tN4YFsnummzrXJvup2kGbRP_inK2EErrg64w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=tsUMon_3uzrhmdX398JdrUWZFpbXGDBMxaZ-Pms6NmY0A6R9bmOZwxp5e4Y_NBWOPJ_cah8MB9kSLBURwzAg6Cm5d0FCzln2cFAdINdBsNiDz6LD1bxRDGrVHhs-U-GpW_iipXMAnYt7iJqv4k6yaFBDy6LWCr0-2J-o1AYdcposZpqbwAWcrQBnQ75018xYsIJVa96z2InxpPXFLObtSg67PvvT7Pti-6APdHGtlc5dK7Br6dRgcUWGNgxBuPz46tU4SG-rOyXlHjKeZXcLwgS-MEttxqMx1eo7k0wko_FVDVX040tN4YFsnummzrXJvup2kGbRP_inK2EErrg64w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeWNHgiitPRaVm_Wo911blZO0mr_SO1X3r71YpsEbAjo-Q1bcipa7S4-C2BPOgyO4AayF-of64lq1iTiKkZMmhjhWIArc7pEKXr8UV6VzZ6JiL48gXqM0dCIJLNukkdm3qzHl35Q-5lfDsSxWU5kBUPuVe7p9_WBHMUcp-NUXSiD9O_iUMXX6WIhi-Qlr-qa3eZggH6eLbF_G6qY-cf2LbkRmNBtcgPU1RhEvMKyBeyQI0r67DLUzifvuojEsHOJNoJ7fpPW5qIdZWki6Fbm78Xl2TqxIH3LzUHz6dFGMhvK7AB6wisk5XETfYsbd7Y3e1uuWfOOTrLhEoE9oRVsAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7Qo9WpwZ8MeFaFx7fUPCFCnh-QUzyiE9C2ckmJgQJfnBRqHsQB11lKABCviIaU04dNkYgiJPA0oxQBwQBq5dHBNO3z-voac023-6OUcihYXzobOmnWG4GlJ2AUsSb-9htMSC2bffY59UFCOfCCOrDM1FQBW-jd9wpR5_ZoaaKlP2mu-BYqptYIBAwSCtfh4djdBzWd5gx4lKsDrZSHzivJgWNZDk7E7GOxlGUbq7nnzGIxewwKJ3U9hYKC5MCe9o0qyEK9mVb7dKUOMzv7yOBfwb8x8FWRs2x_tqkrEJxUuDZe1bA2Carzhcksh4XXLGSiKSF3h0NbHoVaiGWJVLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzdY_lKk1oxG7VsgmBW-x1bC7KO97zMvMj6ltDs552Gp76bXGpheTO5ageHJEF0YXL1_vMk6SstuRfwqUBVyUq1l594LO4Z9jjqBX0BYu_TGxhznhnqKdEruYltDBLi0uptD6OpknvjaUCWtbZKqmpUu7b12Wjp6hHRiu4ZJWBATt8xyJypZFCJdU7UKM5sMqBKOwIKWZ0agjM9eiqokd-9-MGmSvebAd2r_PSC7WW9B375m3St1whqdjgHUFXFyu28OKqv44KW5cTT-AA8hhSx3nhPr_5ILUoxK9doeB84C8SVuw8tHlHE1D_f-Sn0G1TTADb_65hKaBMe2UY8UDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ET6JDV-1daIOt5FHtyGjKLVqTxfStVpdQf-NcsGERjeU7QKpo3PUiMIcnpHOCEo3DwOLaMs4_n_qMtcIE2g2_m6M8skyK42GoLf0mRn4RzoSM4IiKs_iDY5fHKyYYXSA35qCnouiF0RtHyH_CTOI5s-FWouNkaYobQgKlejdwAmiB8itXnjwHmmPl9R1FWwi9jNWPOS_pkWimR3DzFMj6nLjPyNzhXl6V9lDApIfGRdIr3IHWw40D7toK-aqAwqJ0pVFaP0ee0iTRVreKOgGpU_YpvECyvC-QE6hfrS2jaYwMUh5Hu3yuvrJh25JftBo4n7oN8TP5FtZulfpV_9e7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhnUMMdO9pHq8bRKfRoU6L7SYhsZ0U4rQxn_kwH8vk3bKoJbrZ7bnTzEoo5KnH8QxcM9yv49Kc0vZlxyaasKfYe1Z17DygKyRGh2yYlyd0fHRTo62-_a3QpLkN5ZssNOMsxra4Xg3P0RdEciPB3suPNC37IU_guwmFvR8S64o5kZ-9ZfrjtBL0_Onc5aOHAdQv0PJ-rNd7MoeaXqmGMnp0iaLxi3XsjEtMPez2uS9C1WVFykQjKX3CIUCZfLIQeW78PwZMKNsS79Qbp_IFvtiDaMM3_fgLkQFXc2KuIj4_UeTO0K4wMivwmEtF3exPPKruQLLGNNUxcNMiZQ5dTNcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5GZhQW8-WBCVUjF5vQk0VD6Eutr9qTlpLWjvqDRu9_6P82Lu2XEA6NIEuJ_QA4Lkzbn2Pb3ZokbYbcWoCGWqjHBmNbu8KzUwov9X4Ng2gXMUSo9YdzdL6uAlDbYRWYazAofoj2ZAPLbsgk5Zn4t1A1uHTLBNk1xVuelE3190ppmPUZGT8WYRMRBZWV8_ajQMFDBgsE8wcIfgAK8hRKlRgG4wanTbbaf54QN6vA5soCCzl3rJSs_6X7sazyEP4rss_K2oEtvBQwBBN6X9zvkbdzHS33LH5MmcAvHP8JejQiG1znYfCPgEfUgQjLdT5hL7TMKXzV4l4J_e57zkf8D6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFJUiWBuZWmLI5Ni5Twgpun7tXy-8bkMJnRftd3QQiGf3V019-RUe82pOb053qNBcmkAkoW1fo-agvSbGhAQopd9rNxULUsuidLRax-FXA0ifpXCBOHoC4m4M6zpyJg0QyzCxVDD8JnjdMaGMfeKZD2R1cid0T7qfJV3cCCyOjfeeApPG3noxfoY1bSPGK2tCUTqGJKyGYQFyroi925KIWvlcvs6YjhK1obSxvYsDQ_Bgp9dQIOfZMz3f-tjAKuxlnPy4aRnF7R8HL9v26Ud4fdeefeeqFs_FSf-_E-6fN-_ZPI9WmIW-qHfFwr7E3XcXsctkVWhbmH2Gi0bhIzXUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQ6rN1U2qzXP47ES-teT_bZieqWNn0AXq5yZjkrnV3EI9zE4XIFLRdVft-vp6aq9_u29rTzfOTRJnRhAjCjtN7J3qcaP_7tmc9AGphX2jJfx3GRbPd-BHxibVES3C2or1qV3eT6T6D5PAQDliO5uQ7V4_XIIgYq0cDk0rfU4vNgzNXkE2zKXQdcNcn4pOIXL4cv_nWsI6UusDrFc7wOYMco41BuX3FJa-TkSwT6uCH5xoV1fCS4DHrpj4XLsX6GAXOkXhn6dAPXezpHUYi-7aRX5jkvu6N2wNlJD5kQ6gPi8TUp_j0OjrF85RNsWJkWitbLia3-CwOyX_K1jDgLiSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXUWN62HxlIurOENexWwKnlm2nBMBZhSa-QE3RURm37UYwsbsyNbpKBGIv4TUDPUwysAKcot5mkYWZVKFnRzHDzfjex6BAI3vysxlPp9XN5s50SMLoMUwwz20dhveSO-VoXB_eV7IGW_eAjN0-ls44vCKoulzMPdx7rJZHe9AZKoEpoeY51Jnu4WihZff3fvJyw-sp9i_hM0nKNi8VF5TogOOKlmFXLL9esb1jBDJDQracFaA0WpTTmM0BI-Uaor9KkHoyEa1rnbK9sgA1zB_82tnhCaexcNcmv6_PYPtaGEUkhMrIRyZszSzVkA33JBMVlJhnxt2Zt-uEVVi67ogw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un0p91q4pomrzgsPq7ohKF1XfvBTQroV-UuC5OXMr8PAmZhzSArB-auMQKydkujtblZXo707L_SFWMZxBndTP080BdiFHFu91oi_Z7UBGnPN1KOlYW49cBlm2jcCZrHw8owbC0aoTJSX5UKUqWU5rg06Z6RcRk4EKtnVUtAG6l5jE2LBhE937nSC1ZqoYyzOsfNeLaULO2Xi1lA09lX6VsL7VSzK1OAeuZaoSjDoWCCh4TRoDoGoB2tZ4M4hl28Fsr-fjh1AT267tYrAo6dD2OGFrOhI_4T76fIC1tL2YTBEiPt3Sv2cGKd7D55MC5YdDYAavx0jKopBUNpQf_K2sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8S_EUtqtYs1uvkkZ_m2r2HPqJBFFjpnPPqNzdtmv8w34oVZtlncLjK_SWZTSv4tTuUTnC8D1SzwWh1OTDcSrRim8u-X3h_MjIzFRb-AsiMmQch1KKzjHUIllCM5CUePf2pvT3Z-tuGKTtDzE_tbO3ttnAf3DwPqVncqNg3d21puJuuvKGXS4lSli0FXiYZivWnwDzAmi8kcI-iZ5LaF51wti0SHTFzF0qN8ZG57T9pQt_95rFvjyIB2-Xdk8JZSgvETRNjhm068LDiKiMoaWvQLXGcsaeta-QdBLuofmgK4nSChsDsHr7wJ7CA3LL8WWm3K--NnnE6SwK3NdVph8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiWF3DqpMYL3y-_63zCwoPY_Sf4e6Z-jhEP3G3kni7gL-KHY6iCzcrXhAdPhwBTee4BUQJXaHi7lx0Jo3Q5_3kdcO2-Bt4tK20pg_1ft_CRy8yQfwFNQPImrLuB2AzaCNepiE6RvhAWFKszGNnhYdh6PTGGNoMvLtZIJJIkrnFO4RJyOlMxTm_ysIyAGW1icNKpSFElNCKOXokewmc6dPestbtwgUUbjsKuYnUu1-ZLbYLBA13HZkWZDh1Usey2ix_FmG2EFN-tundcfI4e2GNL-nWF6apKvFEuOCfDLciMiNf3XSap4aBFqtcIg7Ti0uCZONDl9GeU5HFdejmCvIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRkZDtbBbQbN7FgxeUZkcaSl7sNVX_EaeXSGarWFV5TTrbSitDuCERV9y6xkihG_birAJb-Gj1YCwFH4jeWC7eSV10-DED4xgD6sCxP9TwSADJqgCbsG6KYEKAiFGvuYNl0Jm2WYrIcgAHjFf2sJnI7vzz-PhwE9Uq9bOAazqQPgSmqmYSxC9flQ8tB479CrdansLYhpIx7wxAPtPd2dJQ3YbErcPeEC8H5yB7msod0dGFGBIYX3RcJaiVPjS9Mo4BdGWwDtczWKJEC_Dn5JASuB64LuTgqZSfCXSCFRsw9ZootV0UmK30PRpUToGrw9sYL7TPV_Ker9ZbQLyXDKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8XLligcz1Y97XoN0im8uwypoeNILsVuD8hIlr4pv9Gql_-CbjeK4WvRNJLzgIHZzxioJ1gxuYPkJIKf3GKJPn-BqjbLPD4UJtyRwHfZHEGj5xDlOOatAPw42pBRj_LlMLDierByeLtS2YXuEW2bRBBnPsfnk2Jv5Um7JBym-erazZxOfzdrq0vQlTOy5heGnWFVuK3aXKEjB9ihzuQe4KG8PK-xXe8_F6Rd4qcMybolVWRcgKAhiyv41pvCIZefCZHCJSFhywWSGFSyML8go6BpISSysgDLIzjS_a2f0bIKjXVsY3lpTLCkFSgzeyIlhw39edOh8kq5rvoc_4zydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtmOtS5k0gqTeEgSwZm87LNuuRUlbo6KfLTL2y4ySlcOu9QDRmOVyaoVY-e6t6uXl8Vu5H-R6yv60RnMgwKIC6cIqUHxTFoIbNsrAHBBsMzqqfljLxyznwCYaMAmvF1UJ5HiPgG_Yx19Vlz5Bjf9_kTfNaP5WkusSWGFMViejgDxbpozkAgbZmgwHHxsRaICqpUUKpx22rxvyt3yOfVCu7a80mLg7eg25958kIiHKRdZ7bayJgZftxTEGxo7dFt3NPq1pLdM6nxAZEGq7xo79ttAE0mlvbifrYoPlCa-Nj4sQfytn0vVP8LlF9pPXURas5KrXeyQrQnfSbWjnptJfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mY5SBSEfEKULSfko-FDnQrK2si282gw9QwhBlizOcq3qFRU0_h_1VypEQpv3NSK_E35a1JQ74QDnU6xuEus8EPP8KPFyhzxF27eR_AnoiTTvMc6ZH7lYSXTZ9Lr5nSLvNBb4zmuuiImvEm7bKgHe2tsCFdiybbzOp9V__DLYRwFDG_6B5jd0pUr6Ls3hsY2QLVE-ZaCORbDknhNmhcl_f4NeoDJA2lLVrZMzE1GxxK2bIkAf_K6komFboFaCF-Oz88UUssaFMj8Uzry4xtTnmG7EF3g7XYnyw5WrKRdppCrc0X77CB5Nc_6CMte2iKt1tcyX1dLwCiwMiQCwy-BBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kn-oUu937kot4BiI4J7fp6fSgDbIE2nFhB_yHkphFPzLhvrwv-MauwmEw4Z8X4Kumdu4dsP0MPFEaqn2vd3TNRKDNiHG--JvNHDwQW2debY7wfMsvoic1IP2vugL6A7L3QBlnHrr8UrOgestc_DAXh5u8iiGalkIa15CTKNpecPhj8cZ_SMH8zO5874VlPU7n5aDjmuePb7AXINCKPxllQYv-2pdNnbSC6yuxEa6K6XCzDWfApMPiHoRyyAFkt1TnlD4ezUQcnAVoztTyP4OF0HsAKZu5N-eY97w53zr8lyGUSsG-CciifhMeva80r3O1guuvb5rZmnvyqnuItyQSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ooq03nHMa56bdZh6U5SUy9wT4V3NoJhBz0kRcny0LZxZfLpSFtMLBWqfblOw_7OEbrFrUMlV9JRPOMYDk03rBWjXgCJn5HB97KtjEa-_xzBIN5qAi5m3UYFta6nJoeRXJA5gm7sbx4w24xvOG3-xqA8TgVnDipC7p-OZuxBPmLgD36h-om0YzJ9DaxOxEKssNIN1hnQe9T10QNqE0_kM2Ot1AiZwqx0yfviDWYroESOLAio3k9zawexUDb6-53ZX6AqpVSz6lFHYiks_B7Aw3ZTvqG-UMUzQEqsJANgeNq1M4dgA82iuCJULJI2fBouEJxTbt45Qmd7teSlUjhzmbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtlmkMfm4pqc_4H0dQ_BOMg5uQfJ0Dt8CTlXcpPiVpw-MIx1-f-N-_MtFx167QwsdCiga64mLUiNTF7ycICSEjoRW7CqrCZSwQFCWK8tsgaYj6NALWJhcAJTFGvtAvB-Z4CAYE2al5rBD02tWQppvXatcl4JUz1QCGB_I2wmrBbvHb29AWoZCn95zKuQHqVj3PNTkXVGY6EzN3mdhs_TvEo79O-lbuM7QJ0mHb4fnvIG9WDsYo9zsMmViVs2CP5jgwzbm2iMZU6MxXQ33SZtfQB4JxPTS_qikC01p8f7tbuL5alaXd52-ThYWfHlfMFY9CFuAwKtW4cx7q7xIVFujQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brBzWBnLFJpkcV3wvGq0YW4gqLqVfxOdVGklZW6xhfLb3BDp_YjYAfyEiAvma4tzVLCMhVOrEDHPHNfbePX5g1kwXgd5l1L_o0LUzJwPfYrdVlmW-owFHFiUf8yCd51Ac2CozDftrY3uwPZ8v4e8tc9MJfVhp_PZVgGUhopx9463zo96-1LsHKPkGp7BW2Nh9btgPdmgpgS8MpPH_a9rDnhKDov_RhT5iSetXdETl3X_012KMgYCw2YsihofVwU91dlza9bbfaEtqB_Vht1zhEf4AtaxmvZXZqVGZDigRxrMglAHKfKri-0so7daZpDWGGCGTTgrGaFTg_ft9Jt_Ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOzxrL15i1HSDJuL2P17NJGJrxH3oRukX-doTA9l0FNLVkjl_qb00g7l2WkO6ADpxqMhOHu6yNnYo5AmfqN4CLFl6-12tn0n9F1zzujb8Ly4PmoRcH4VVJZnGuPk1aBh1KLK3EIUl5Q1AitdjVqYJJf_1spA8941-5WtKCshjhvueOiYM0wbYYKMOPsD359ibnDLvWWPWv9OFWiizvKcENUPHHSYqHPVVsWQX86PEhUUhGYwydM1HcM41cHEMpxwAPULSC8JfrfkaOupjZxUsjEv3rYKjwN-z1uagBXLhnzQlOPFLyO8X0elXZ2s-ay73aBThjoiNHBbduh9gcZRCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpQ4yfSY8FobHWzj1khaHOnRZvgzgYN9tI4L7TItHWCpFGnaLqLO6jVA_QL3mDljUbgTi23i9cJ9EmlhdW4-lgtsNxu909bEqTqu-pUhtMh7SATfmbztmDc9DMyKZ90xpXSQY9BijFqhmQEkm_Vnsr5bw7B-X4LXNv_LLyUpdMCmK7i5zfVmmBizgfgaBE0Afc5Of8v95tixlYu6Yjs_FwpYh_QHREqLEj2Vt08EeX-NY4ia-KS_tR2WA3xqP_JZFNpUUMDNh6o2ZJgSI2AfQ6DXtmWl21ymgZiGrTlsrh3VX-qjAPgESLsr1770IRK5EaNGAixpxUTVtp-jj1DC1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmJHzQDRaE8II2gMwUcQWCWx3PGbt1C3YhYJt-y6J6fpap3Ajrrf3FNTOJAYUKzjgCtc_cARAbWPz7ZwdGGN64w8SQEv4dXJW0CRBue_SMmpIcdJIk1EqPN7PGfUbTZxIuBEca8SKkrN0kjKnIvdMhbAGchzP3ww2m-q6Gm7W4RxHgEorGGOiYkW2Q7MQthSMatJY8iHJviikUbqgG9d_1aHCL4swonLUxfWJ72JWRzRy-WBJdyUrDU7zp5TT9wey4U1IglIM0CPK4PDxmBPFQ_UdVBqAbdZlox8mfO92nBm4mouHL5hLrd50fMUe9n8kYD4O7IolN1HYc5kOtwI5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-1P3o6ymmL0iVOhuPeNpCSXoEzeQNDiIEhbFBhnwCDNguc3PZGJqhdb3jcfLxrAaAJuBu1RKaPVe_Mhu0IpFYjoyFx-uTbhTmuGfrAEX0TFlUTmJAwmR3vu5S7JMddUMJgO3KulHxDcoIiJ5MeFVKcK0z2Ct2f3KEe20Q-xG2Q2nsrrbub3lctWyr_2OWAjVVu5l_iHE66ZsGkFoUzpu6d1QuJhNNlNFCnm-yemebAGVkHKB0KWCJoXRCyAqT13K5BPELy37oU0aejh-W6B39AnOpu7eTCZxVH_OJ3fTUI6nXGfRorXhH4UKNG5U6vxyWfcY-oWT0mjtS8A55bQ2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/coDZbWudmGmFDxtYfR-WCwghZwWfntEZvlsbLOVCsIT09VR_eA2t6xgW-DKJq8lJBlbOgtz_DiEl5FGtfr--pMQ9vOZS73K83gRafMne0hmJ3xYBiFSXERYlQWQ6WL0ljmeCLW94cnvDNdqYCDvKx9w9G9PHd_GNU1paLPMjzeeTqCsl1Qspd_UJRcRCyTHUvVjr4O0PlYqDFikUTn3IsTsBIrUPimcKO_dsOHwIJd3g4tZblN6TL9UnUW1h1-jpqmEdnIi8X6obMA37OBDUe9X1zQJqxLBWk1h_P-qd8Sc8ORnTCXRfN39f7sIahdam0nMLx8djIH_JQOwU8vVjbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHQoiHQi_RmqPB6qBVHDyOXGWE6sruPSk6ZHswzNLqxni5Evtwtrv8GJfOBIHBNrLgbFANPPEiulS-eGC_eK4eHXeapZkt1axP-8M2r7QV-dYnvv0oWiH0VRvUGSpqAHBOECthQqfeq-LKp-hYdo4FPN6848Anz4awfELqadybtgwvhEkIjBGGj6cRzqHBhdEla37_qrqZvFofdCBfCQy7HdKZHi09QBUeQGt71NEN8MFtPxR0ejghxQVz5LN-3HbmWFLGDmfAktYl1nkkC6H2vJ9J3CybOT-QfYYpA71lnvBOTCfWAl2jEJQ2G8h9z3nDmc2P4erDuVgEczyB-7rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldu89hW7ZZrDF0fKqq1NxCFL901tqOVSAki1d7b-O-j_Yp7nwIiT2J_OO1gSzyZvpZo66jqiJyI1KnZPtVr-KpoqDP7tu8D4hmJYyhvAyrkui_-dkMp5Ezpvy7Eaog4YM3dX7_WdX8r65KAVSxYsNQ_SY6Ssb9iHT-o6F_yE76OZ1trp9hbqxhVFoF1QrZ0MZvUZS72-B3rZg3seOgbHke2kx-HWXu0yWXmxQGF796-i8ZvIIj5AXV66CLW98kYG3Zeup1kShppCBfGXdRBk99_1tAFRcTrur3BV4foFxpWI8eDwmnwq2mo7jVyMcwgiDiEvPi0qOHYybLxKP2YEUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmyT7Uo-Uvd_uJZLZzfRpgXzeV4_kGQtC_lcMLcphK6UFRqcexM5oirpBcy65CIidkuLBEAE5_WjHP1zIfpNjreV-UJoqVStO0FYpNtMifrEbKT2NrA2bUcgxcxZI9NS1yeKg15DjgVckBOlfP03pthYXQRmqC5c7su-p8MIeX2PH7M0hNB8qwRNZgqYo01MzLRxzn8RKeTZaFoPmODEq1cmQ2p2xzKoHLyM-Ox009mj_36XYvMRAMNKY7FuIbdBHT6cB1Zd_JANaq284f0B1LZdC5dl1VJTHCJK3EikJ8bn7B2_KjGDnBV736HKRyJ-87cZPl3B_J1mmd6bSbxeYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChFo9NoQmxijYSrWa7siPjWxnhgsr0Jik_oOVUhP_XCZoUrHac6qKDaA-beTEYjMGZLWlRgcN6NyC14Ej_1QZVWKxKgH0rzyXPRRWoqCFpMDcJROJVi56HC6I7K5oHDR1wALf9Aw69w9kZ6796BZD5CkyKXgC_vc3rulUZVU6C68_91wf1LQsocavAVxLaOL1RlxPxnBg-1BolJam5fdGHbh89E4eH9Uy8kypJO7tOUTk6Fw6l7tnPJZrwsFv2-cSUGIccSO6EeIvQguarnGk9bBH0sYstylHw9s185eSbAYYGGxkaRY9oVHoEBcWzsXQRoztBXlMthxSyvuUfhG8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiKRsHEv6HLI4uztyD121clwuVcSVVymqdeM7LWaOZSL8B5jVZ2evt_tOk0aTQSNwMcO6L2hAlxbasmg98kcu7OkrvUtH6UlzW9X2SNxJXhRe1NQeZAwdtnxeq5H-oaIT90ZpJFbFPq0QXFN6TPmO0KMc6qFemDU9GtS-pGjJ7oxJXBPUvYTHguW1VQC1gTTbSa1uqwe2AsH_O7loJ2scNYqHFEqQ0AF7t1j4RjmUKk63nISyrvNbD8aYbv2BwB9hpFQhGL5H5jmUoyim0sJykrMcHzemHqGsz6E1YzOcg0qrNBgM1vujGEtSgX255HLB9NiKofF7rnZlbT94Td8bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXS7Di9CJfDA63wpOMuSs5-vH1J7EujA4Z9W-OvSmTNEcfV9x09GN0FOh-uRgtiHCluI2M1xxHY2NRteQz8x0BvkFUMvN5Dyq5gzdeboPR1k5dQfRwfoaM5o_1u5LepxUwVbGehx4p0lzggA4tEygiNDLUumiZ-tfPceYWYCtkbYJAs6GfhrlCEEXYPNz9kl5wJGwIaB67FynDEnwP3Vjx2OTWeTRH8QIAzI8aZ-tihEyMJItcFCh6AvnVoQUH-o9KnEoAb52xeb_oN22iIjiNzhU4cvGAjNcZOj0vzK36GxYe_Rltay3gBV44tlERzDn-EQcxZrj4jnGte1-N1slw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WyY9f2X8x5S24WH4sWpqTuZ1qO0FhCnWhNx02qMQymnfNrl_-nl-YLIkhDonQ7VuT-nj9_VygFOOb_8gPLATuG-SFWJOA8PAwqIC8eP3Q3_EdbON12YQTLB2bNjIEUpm2aEp5O3_biJqRMnmVJ19eD-1aGYB-YHNKe5A5AtGgGp7fVBhEO2gV4ovgOLa0CLEeydp2XJyZZCFSPI3BVFBxodeJqAc9pyD0yz3Ddnu6EMx4L0jONL4mp8V0O3mx_pJToe5BLNxEkW1rj_uWuvYbiMGBrzGyBz_h2rVAPCBOvLhkxU0LkREDUrJudf-92kQb-3uA3yEp_qdVuoEBRs9WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5mohvWsuY1wqWSzbLETrEB4QOi8Eh4SZYNPBL7zctEKmUlizLjJpwnS5RKH7kQsES67IZebTTvj0pftKveIbj5qjzXQ0vRumg2qPeVWZtmgilq0F1Y-UiMcy1Q96qMIrh75whbh37DvNbUhq6_o1iFmrprrzhmXI6QhIE6oBYkz7nF4LGNovzFd2c6M8ZtarCLAXzffdMfGs8ZcUsGgO7iJFjQsX1ZbyjZ_hL76RrhuEL9Pd7ra1qPrlXu7VtT2-ywgY9lpLUh71Lz4xJtZTYjQjwMdg6ROlsPZQHLtVceWsNRdC-agOOMhxiKcLXtnOJ7hJgpxGu3sONdNV1cL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/POKwo2w8VQ4lWnfbqbZmm413FX5SqGVk0Xi2oe19s2XUpgz_rj-cEP9kbbDzgbvgYF0Bljg81LvY80vJvJ_SdMMP_aWfBMmOoFrqFTNl3UYF6qp74ncmTGHCzd8fmcYQIQFMW422hmxnWHnp4oxGAQugfjE3X2Ljy_Gk9iU8fvA6oqooPMyibowDk-YJE_hLBk02KE5D5QEaU_DeXuhjOjF0KZjg3OXnX0XM36Y9ixsOxtwkROuRVOi9Pk095Ai1_rwwO2-7UtvXx4JLfXd9_Fbpvp2qiX6DflyLf183AeUIqcfVGT52L1AdEVlx_D9gPjZPdL95U-jqXDUGDNP8NA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eq2JDgll10-sVKxs9pX0hmsq8Rq8dZgHFd0624Xa7Ir8WAoBVba8xdgFRhrQiO4sySkeOb4dligHSJQhcV5B4MGJFtbLrR4hZ7x-4U6mb4WTDsHkKBIM5jXuQwvdm6aMWCWqQoevgUA90j1Ha-5YlcEzIvak68JiNXKYKIpHX2oJNTujM9LqJbukME148XIhnm9bKCkISIGA50gG_J2GcLUPcq3xYG6y6_wRADVHtBo9yoWC2tFsBp8Ewb55WWAWgvz317Gs4Y1cBsxFT1zaF5wvqjz08yxE0Itlalq6UybOOyur9qSGXtEd0THr2PkfOQ_8ftCOCGHFqp6_x8B8Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuBJ8Bi51tTMSWz9WOHb39mDO7Qn-9XAVXu8Ks4W86jw0KUA6GpINMnfR-LLDgoZijtCOnTdFLSGPi2BfVsNH8lcC-O9F0PFfvRD762FMJd-l8TZfRCRxM1kZzmDbOPSf2ASFBWDmO1pZRSTf4a2dZtWZY_7jvUV3vPe6yP_Gb_G_f7XCdEp4DBg3OAiUO78IMeok34VhRNoI52vb83uX3tpmAWgKl1dKi0m6IRvxxm9omnf84w0SXhj9ujc1oUU6sr6OGBgfKUyOfKL0ELtpQKDIWeZAL6hlPJcJm2nYYz0ErE-UglkCEIAhmqscfs7SLPMVZDD-9oRbNMQkLuqpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMbbXtYlgVVslS7pyYigRgR6Y5mNIp9EJSRqwoDLYExNz9Dad_nRIRfURtzjHcI_A41QKNnQkIWaISuPUxWiNdR6ajWw9IsRI9jqTjuSzo8O8_SwDD51Uf6hEqwrEjPMFXY-9f1Z90wCi-AZUG66WFOIRX9w9z9XrBNLMRpwwSZc1gX4NPCYKIqRmDHHP3aCJHy23scEgE8yHuWEZZPUAIA56o_KiR6qJmF6fRuWKkyQzkvr8VvvNhUZbenvctDXb-0m1E3NYkr8a5bk2f5JWhVRCZBv1jxsaSQYp_9T20sTkHnvDqaOh7VDzC0MkDPzuksOFP6EVTVw-mC6X_XDkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgscIJrQz9tBwIYbW1u-osgpx4i3Ee9XCaUA4fwG5VtBLoa1ky9D4XnjYG41Ke58a_vCqgQIZt3WitgRsLE0OSlbhwFp5OIThrK-UXQm-lWgihF9l2daKtLU1nuL2TmycyxkwW1xlUt94XNmQiYkCHXaCikEzR-DL3xN8JKGkJK6XTzl8T0dDJSnovMHg588PiM2ZaGYWlyARw9v5bAAcsXVNgyVo8V3eijMkBQ2_3WhS2PvHAKenDy2IOqqgt40eZn5flj3qN6fT3t0XFMl2K3d2dWVYCjliLb_DXOlYJ612iQYSq-hyeVtnEW1HiglXo17c6k0I9vgJQTZu-Wc4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riCsIyzljGP6SDP8PD3hDbHrSbmrxJnCpxL42pCVR1XvI8hIXI6kKTBxtC6_LXk5TpDJKWUvWHg0_8eQ5so8tMdsSnylUi4yZG7OT5vfeYvmb93DcM1DWAmVtOjuvTitx4m9C_-xpLMiCJx2-qzPGvsG5gY59wmZazoq_Gs0cwTyve7S82--qWWfqjf_ejVf_zhFC0q2pnCQQ2D6etHSVjxTCv0l_BTJlyBdxQy04RQw6yQiefrlfyc2jZQfmUjH2jo4DWptv9tpe50Klvniiv7eIjgfczgln0iZhKm12Pszg-J2Cri29JWyVgnm7qaLGpedIQhuyp8nlUOr5HAH8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZjaHt6zQ8R9qGdNqtT7bAntHTkyZCrEViXSZ0rEC4ZoUMpUZoBxymv2VrTyBVhfUTeuTmVYXjad5wSjCG_YrriJjBOi3REMfhReS0sTEsPbmSLhSh1Rfg0m4Mak-GP8DYPOOl8t9FIWbTqSobI3rtRGXyIb5KAW8rF4OylSFHyjyKgVfKK79FNDsXumPhvtywOkd5a_hPdOuOPaprqnjuk1llWSwsxzkE9srodvuBkogks2Objb_LFZ4ni6HeWmO4ImdnjUA75o3fCx-f_t5Uk0HyAgDeyKtuc1SMYJooPnk57XCU1Uiw2NJoq_KA12tOecHtQq_9OGRK_8iMYw1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGVerKDMTCcoEtluA5uo3W8Cz5B4a_pcV5gneAm6D106ZgLobS73yuHAs6oasvMcxWKPYZI3Hii6b_3-yjHreBb_hbpWCrTjMRlr9eoCNLwu5fTzVHYOkR4sfZYmzpt9X5o6shhg8A3F6vcjrYO8417LWc5n54hjFTps6UOyzn8I3-haAy4EBD_lA1AhMp3HwMRAvqYS8M4ktK2AC--DdUCy7NUAb14lAwB9bYqtEQLZl8HPbeU7rfPh18YoTdLaX32He8bCXq8Klvm3uZ2ljvcAtNmQDPH0iJeJT7b_G_mludzfWP1jai96rX1JiHCBFCPY1eT_9pKV5lCcphJ0mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxeVrMqj5WvTxO9QrjksjopdcIImLyC_tcfmgktQ7ddo2hPUjL6vNirymZ06H44iVUeI5jrRbeAlaBp84W-CWXWeLeiLfGbMGDgXGwVpbAh0mvTcmTMluvw3z0ywAXdBlaoYFkfVR0Te8GvwuD8fuVdrNaZeaG31Umw6Px9POdISsGXFCTngrOxn6aMBiIM2E6i6loJ58ZK5SjHmDpmamf8ZQhumKbUd9lEZUiOtYaw-g2SpO6qzfTS1eCYB1lMAj-HBA_9Rm0pg3AQqGzZjBI5E30_HSFFp5Xypz5HuG7ON3L_NjOwh26mbgJgsbmqC1SI_XPaL9Dx86QfDO-Qp2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbjGBZITqH988d6jDmwdRo2A4yR9k9oHDAKGpG-V-J_QQPLmzdGURxXdtmCpw47-hFfBhutCIe5PheJDsH8jBm4F1pU62H1jtOrOJwJovndeMVbG4W9tdTGV13bn_9jQfXDDWnKLmWDoOM7upp4razpYNY8K50etSWA6mhvx05L3nXVoaYrycX1fWV0rACkQI3eMRtp8IpYNLWcqh9YK_ZZbcEp22Ff76OzxQakhAmuiD9rCUfCGKsBYZjWH3UKymVpPceA1gqc2H6zueAl95r4lTM-_Ru8FT9F0u_V7Tigpym-hQ8B0QVDcAVxD5SspGnfpXOY3BUBg6ADSAajFiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enUs5F5GccXQ5mzQvN490PCbPjc8WbK_C35IcRoKubXWvUbJdwuECTBeIw5AymecEnPGPjXjjmh0MlM73UJsgCY0RI0u9kQJIDefFHkPNEgcThQeO7kftYNZbz1btKOuSBR_tnklBkZhTANzL2GFjpVhgM9HZf-d6CtM7qOnZG5a3kAQZ7CuG5xxNUbXDYVSen3QzIjx1Yl2MZny4MAanaQ7LaHJxj1QPUnLpoTJgsJlNHk-ZEN5mApRpozUAziDNf4N5cExVw3uu0CQ_0_IlpPk-Q12_L3HtB_YgsLUvIJ6jk_x0nQuZsfqgid-s-PqjY_FsHv8SajXK5EyMqPmgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocUKeJ_0-r3q7FMvUeICPjNHyM3pECXac-qfhDUrChCFBcEWzw-xhNMI-t8Z-Q4jTcOXa4lvIfhT-C-vkYIhTHMSaio0q3UIl92SAvtQPbGEnsaH4h7tsCr22Hky7PyAmnHNSVIEyOApIhg0z-t18gJ_d__gy81xaVuUGVmCPPb7Ut_wbkmEEJDAWjfTEtCJNHh2r1ESNCblb3DheHMsoBlFxf44OLEWAlDF_K5wWwcVKGeZcrU2qcDPzcuXb7e97js5S8wbz9HzIwnJgrHTKSuYkJM5LKRQb_lGMDkjC7WsNnqxP80ph8c1xQ4dKycrGLP89NM9Q-9_1DGUt_Z9PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dchXVp8QeOJO4xS5zO2cw1oB1xZuiXIL3R8smp5_AomxCq0ror9RxBDqJq8hAfJ1OzJByrT6mBD8oGgWHDFdfzangc9we56AUSqteEAY4IUUwfeatxmRNj7hXd_1N0Fh7EyDBm_q-O4bzCRkDks__7EY-Xdbs6pbIRhARcf9ZkiE2ls3Q7-GeTkKGtT2AkNyNx2gkfhAM6VcTr_VR_rIVuRswUEm7vxujfmPVcUyRp2DxU3DQoNqXpgB9UvmhUUWQxxfFV4Py0ADMz3IrBrgTalKoQWuQKfHU0v9_tR3Y7O_rZ0hwUjNviykXo5q-C4jC06eMaRne1Ok-QIA_1nGbA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=J514N1nwzmxtmMweFhUDUSoS_M4XnOv04z86t0N5ehLW0u83IkgOt52AVLlnw91MEM-k5CerFq-K1oDR2hW_pC94xQDDW_3bWS44ljWXZZTreQSdodt9YlCi6d5A2OM73fFt40bPVcuNrdbuIt7Xr3VZlS8MVZs6f2ijVnYxPJTyuoa2mxuFKEv1UEctogYOlTQbNgH5aUOkohQjCqM-TMqDUOX4s6pUjQzI7iEHYQWWUI4I1sC4FBbxQ1giJotRXZ8gIrjSykXcg8GB_sUw3IieU3yxlo3R2RcCAo7Jny97jtaxrEPkIB536vgLsmFS70WMdFMKu7bx7EYBVezmtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=J514N1nwzmxtmMweFhUDUSoS_M4XnOv04z86t0N5ehLW0u83IkgOt52AVLlnw91MEM-k5CerFq-K1oDR2hW_pC94xQDDW_3bWS44ljWXZZTreQSdodt9YlCi6d5A2OM73fFt40bPVcuNrdbuIt7Xr3VZlS8MVZs6f2ijVnYxPJTyuoa2mxuFKEv1UEctogYOlTQbNgH5aUOkohQjCqM-TMqDUOX4s6pUjQzI7iEHYQWWUI4I1sC4FBbxQ1giJotRXZ8gIrjSykXcg8GB_sUw3IieU3yxlo3R2RcCAo7Jny97jtaxrEPkIB536vgLsmFS70WMdFMKu7bx7EYBVezmtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtaQfvgM9OQMiUb79aKQAKMMJYGQ2riUKtnvPx6s002QQNzL7icDjXPdUjdUf2cyY667ZwNK2G1pTL7bQ2dkUilVCeD-fdjvef6ttAjhvyHQLWDtXRu-j0pKOgvUB2MJJXfwYoTfEqOVRZLMeGjOvhi5Ap9-OPOZMX1f7yObOqZ8dOVPegwHC3bE-X-ODAHRoPgHeIYkQOFAnw3-nXiRJcnSIDzvqozAVLndFHr-IvC-zRzr_lEhiDO9Y2sD0LQn8PUhomHuuGEmun4YcQ0sm7116gzbRw4EMnfDczCbsFfyZOGtJDwuSZfccousLg4ihYA_BqoSJKCYymwukyTuVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOItwbTYq-ct9fgbgLoEe85e0CqFPMZ_L0xXzA3y-bai0OJFh3wVQrAYhgFxasaClM1sDe1furSYmJt_2ezzcaN9kkpCEZ2lSdGOKzESWmaQmUzML3dsxKuFLQkhSZqSllvHzKnvdxBli51pZvapJMtal5W8O4pzKePv91TsPr1RGaXbt52jVagublzQ5SYMxhqkhXStFaSddO-uB-gsRPoYYQvdrroZlEKNc3PW8QbqajkIj0epI0FEX9ovTl-MQetUy7C_bE4E9m1YwREfAw_WQKh030eBmsNypwJa75G6uxwUs5oJAcBPVyWyvByiwey1FIg6VoLrNIH9WGZZ-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NPVcZsmkr3gsDPJ_QveIdgrkfOp9ts34dbngB6Xtt1VSAu2ppkfNG7IC8zet8H56F-WHXZULqagcidfaLBq9nwJk8ZIvnCYF-eu6UJ4YhGWs5LxGzZth-jgSUJxfMVbMb_dyjffxlSuPj4eU9sdh701myszyyBXTwaH4dz0l7EJcOcv-BR23bZT6oXOajhRQg3XCO2UA7lEDpP3LfN7cqWwvYPN_hN9oj0gz-RWsWfR4anrGRcgkcq8JMv8VAcmDec9iGEy1xjq5hUkh3FQkLGgeEKLIkeutD1C2-eH6jNxBFQ-lcaktDtRBemdtw89BdewxDISjcwEA9itj55F0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fN2uinbDKxxyWwIQV2C9DdlEobsnyI4_itSTlKBa86druBKt0PvpEkuUkJVUpGXPAW9iCcO_4aTQ_9ouN7M1lw1aWwJlzg4f-Qu9N3Ey1pF1ImB5oMBrXTe4CaHGzF_hiOYL1nR7LpKPSAPrCYpFIYdv0KpU8cYHyv594RQF5bQtDVOkz9mHBOngUvmWb1KG3CNVL7Z1ICrYHvfBSXwzGTDZAlm7dgosqrQvDDN4iZuAo7s396cLIOTFcT1Q3c_j8WcRqUwFVZv79RxeLvDXaXbkrL59M7nS0-9QwndMWKdj1wToIGYu40urBnX8jl2k3rHqJ6pe-cDsqcpnofGkQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdEqZ5EByToN5xrpH6vWpordeiD-b0qSCaCCIzv8876ELxok9Oh2tNHFH93QNxIkvsLhBITDW3Mt1Fe0tEMzA7qluq-utCW_e-phl74A1wezg2cy2ckO9al3Ldi-Qn8s5IAlksz48LTv4tEJlr0z39IsrU7WHIohTKTZa_fXyVsVKm-SJe8wqSFwBKyTppMDVbnNuDpN3OxV0kk7LrHxAaYIHf44-GLv8Zk3e6EaBEqYHmTxyESRVf30YWURIdHtUXKrLBDp49Mpvm67eMxmGraXyD4183UJPjPV3MTTRiC7w8wvaM3SAUz_qSPJ1Jx-3Ri649PvwlHbPLfp4eDDjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_-NMrBmVS0G22VMRKN_sSEXRYeWaYRQvuhBxAuVcEu29QloeLZqA9tMLlpal6MWQZvL2sFnN_eldRlA3luh1mtjLAbWp1vUAzIKfyxcCgHfwN-T_dfkPUyPcBM-aEHph-a_AURRiBurRKs4Gliad8xT1gDcq3Xokm0SmQZHVDGPJUFCk8JzUqdYf6KL0bZewzWpqy_GWme9dAHSFlXb5SHVYbK4AkQ63rIm2GG87MCXHqaVB5ytrp8mxw9goAKvDipuJAZBbCcpR9nYEDomyIiTC-feQuZ0xWo-jF8y7RKrsv3PPBNN5EIDu-_hN4nhtPwjwwrIub9fWI4ey4NrrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adRAg1uiZuF0xl4jY3riZlGCrWURrrZMy6tnv_-DsZS6kft8JNzhGXLY0Rhonxf8dKzPi5r49YvMTReUCC5R15usRrMwN1Zed6f3LbYlvurIaCVqrYWjjWZq0JnQflsZZilDs4sf3um9zvrRgP8_ATeyz4P8D84tG5IIxUtNRroIyXcA3JbATJqUBMC0XpjY1NJbhJR5QtHrYymc0lg7thxYr26wD4H6nDEpDdmwY4dNEa7eG2LBsw8PfNfajCzaZ73JQdVpGGMQJn7ZeOS9Wb-JEeoz9AfE-Ats5UngChmPfmYlVsNrYg2k6Dp6NM72PjIArtdCU--Ppgi5XX0Qkw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=thwReEnYxm6yrfWqaRfZkJUJWdXivCKHtkF2FpDvRHeyO_3TsSmue7Sh6fAPpRZNTk0pX4u0VJM59MBPHiTAzMHQlKDIj0OECSAYWDo3AbU3oeebpkzMBSueFXWKzFP5dS6cMJ0rPHX9PfWKbbxVz6sFmMNtvWh8wzSpg8Af0RoM-_oXNIvxZEiK46eYiLVyz0CFx_A6W0A6R_LSiVKku8iPGE-UE55zA37eBniwkk2pMI5CosVVymkF3GNwMhu5_CbfPETgXM576ClA8E59N4javzppDICgINoVnrtw_pBjwer0thfTfSy9WBVDB1nuwfC7yk-rYW1hESGEku0yI3Uz_yfLKBW37Sg7iTHx1eOmPT4ncwTMBZtEcmK5lU8PkkJ5sLdM57V39GdELYpf1-ATEF8rHS4KKsq0jEFyj1pVlZRV2j2gCs-ZGQao1FaverRI_snjuabOL7U5FMfvJJc55dMzXUlunGspkR97i0eniGn_V7Wkh-8wi8O5SeAvKoQTB08tvAQEckaerBs-0XBNvl66OhOPuj7V_4tmfZIc-k2jgGx5-RdOCz30Gumygev9tJjRWwmIHQe2ZCFcPRiV6nYxUWyu-K7YJ9fPO8JAYqKuODAtsdV6kXqoxVBNcz7HSVKzEDLpiSqq8fh6D3aTVMvDcs8lPhgYjf5STaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=thwReEnYxm6yrfWqaRfZkJUJWdXivCKHtkF2FpDvRHeyO_3TsSmue7Sh6fAPpRZNTk0pX4u0VJM59MBPHiTAzMHQlKDIj0OECSAYWDo3AbU3oeebpkzMBSueFXWKzFP5dS6cMJ0rPHX9PfWKbbxVz6sFmMNtvWh8wzSpg8Af0RoM-_oXNIvxZEiK46eYiLVyz0CFx_A6W0A6R_LSiVKku8iPGE-UE55zA37eBniwkk2pMI5CosVVymkF3GNwMhu5_CbfPETgXM576ClA8E59N4javzppDICgINoVnrtw_pBjwer0thfTfSy9WBVDB1nuwfC7yk-rYW1hESGEku0yI3Uz_yfLKBW37Sg7iTHx1eOmPT4ncwTMBZtEcmK5lU8PkkJ5sLdM57V39GdELYpf1-ATEF8rHS4KKsq0jEFyj1pVlZRV2j2gCs-ZGQao1FaverRI_snjuabOL7U5FMfvJJc55dMzXUlunGspkR97i0eniGn_V7Wkh-8wi8O5SeAvKoQTB08tvAQEckaerBs-0XBNvl66OhOPuj7V_4tmfZIc-k2jgGx5-RdOCz30Gumygev9tJjRWwmIHQe2ZCFcPRiV6nYxUWyu-K7YJ9fPO8JAYqKuODAtsdV6kXqoxVBNcz7HSVKzEDLpiSqq8fh6D3aTVMvDcs8lPhgYjf5STaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haS8UfwtNquJUwFu5xSezhmg7VNQQiY8l-OWBpKBdIkfCileHiNhfy5DyYz5D4DVAkahnQqfPMisCnKMo5UkmxhUfOGBZDBhrsq2bxHqN5Hpp4C7wrB0I7OztrMmZw_7tLzs4-Ozo4dWRI_zdbLaIspPcz3dz3sVPRWDjVPIvTy4L3NaSWCWHfCQr8m1a8Nnmo38rojynZsiLY8YHyxRXXuePP55oMik4cS4ZhfKqKV2a_g1zn9W7X1lJqRAXByYIe9pnxNYOoBurVhK3pN8N-v3xunjTLkaw6xg-r6cDJ99zL98Ig3PRvKamj-UTEkvxalcx0o0J1PHNKIcAizASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BnyN2bAYfgm47kCQ8ceEko2XFBMFg39FWt__RQ4sOZ0a493koF2lzfVH7Q3rxIxnYC_ApUSxQfBs9CbBEG6AH7Mf2FcuT5hBHrYGnz74bzxbopnH5ngfkjfrHDA8Vgn7H9RNW-GAqYvgcrq2UDaFo8TO1lb47JoLog7N0wFWysm2S6I89vK9mYoXWqFniSS9voxiV5SePXJH3rv6coy9hEnvaw3vxmU9FEAhjAel8C3ZSoIF2Iph4NHfiTgTjtc7KEy_aMk28mEB4FSJMksS2i7VNa47LYTJKuawnjjoe5VT1vWiYo63eDUTrYRZKgkbVu-ejGukwhMdz2sHsbEKSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOu1-XMXQ2aQTWCVeO26__e50c0DbhZHJtnurhcmTzyT2xm6Vae2eI2XFVtzOacV-Iz8eLtQdlIqpKt8E8T83VoRJ5iHd_JQHSnBjoIu4_V-Xl2FVvnhVmSGVlAh13dyr96WORM_FaYe354rlcmbjk_qFVarigwgOyzCv3rK0Z7pdz21j5q1WsrzZm7McmdIWtPBdO3rD_LIvUNoydVRaB-KiMfrgNG1Kbs_CLw17GqcIKAdjB0MTmbV7sW097wa_qMybAzWE8z3BFsbrd-co8LprqU_VwL26W-LrIni04aJRMfDY7UvInRMZXFxqexfjdtC8jfWzU1PWdYZ9wrsgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iW5t9nSflP7_e4VL52k90yeb86-j6ShpRSwrMLinRvb2yLV-P5E1oDlXZNXwZ6cvSa6pS3Oegex8lAYKrIXLfz7ZfCMF1dW4mffqyZRpF2nrULPh7AZ-P6V0Ejhn3rddeFY5tPHi1b8s1aWfiROQ0VRTkGYZ7Ok8vqW7iEniH_u1re36dA1qZRma_z34FL2fs0e1Qi0Ag_3vzGMy6DYbZCYP8j-c20WUDIdKGWYXYBA6oCc7F0dZwbXJ80thZJJZIhxHqPrlbcHGg58gvFt_k-Oqibnm4gz6zs76uKX4rhcBcRMBZRnNM_m8QMKKy7EKfoAsp77q6HkUL5K0liDHNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvj-atkpbDS-6XLLMtAxapmVIkZ1igDJ7V7lst7oRgj_argJjznwmdRA-68UdqgLItzAJ5ZWsA6Xd07e_kpJ_RC7Vnsd7K8n_5RoDxFhKTMIQWl1ZHOPSsW2v6xQOy1MaKjIb6R2v76NYCRKrR6cJI39kgZpQfhVS7W60dektAryfaUYag0gTH03Og6VpCingaYV1lg7ofri__Zx-jUZKydmF_ziKbSD3WZRYzg5GH6oz5bTjvdQ0ifuTU8qv9UZHwpWDCQnRC5qu6JLwCICuZKJK7skj9fFfiqkHy502geGy8d_VhLKjGOIouQSYcHVQi5WKGOwNnvtY3pCjYIkvw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Ycasf3gF3RCH3cBVh6ABAxrwIlenCkBrJd8YvKPfHvoa8QVwlE7wbtijBnohWJEyTpu39s-Tu4vCLpVpVdQ9ws8HP4cLvs7wPJUSUxoWbysFBLgCkSIDs1PclkCXc9RXDiCN75E5CNDwnGQseTfEehoN-XecRXr4do2RacUnZmsyhUf3H4Dbd6vph1fZ0WjF1YQaIUGUNfDN2Ey0e5oHmarVXFcMp5R1hR5qwKBlCh_ZCyAVlLjcX_K9AlyH2j5y_YyViCq1mM1e7Wp44PAyJ-l9XuxbrWG3CGFqqVdONWyml8EBfKYrdouyfIjs6P_1C91mO3AbpNIrR69_CRESDU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Ycasf3gF3RCH3cBVh6ABAxrwIlenCkBrJd8YvKPfHvoa8QVwlE7wbtijBnohWJEyTpu39s-Tu4vCLpVpVdQ9ws8HP4cLvs7wPJUSUxoWbysFBLgCkSIDs1PclkCXc9RXDiCN75E5CNDwnGQseTfEehoN-XecRXr4do2RacUnZmsyhUf3H4Dbd6vph1fZ0WjF1YQaIUGUNfDN2Ey0e5oHmarVXFcMp5R1hR5qwKBlCh_ZCyAVlLjcX_K9AlyH2j5y_YyViCq1mM1e7Wp44PAyJ-l9XuxbrWG3CGFqqVdONWyml8EBfKYrdouyfIjs6P_1C91mO3AbpNIrR69_CRESDU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dq_i38BvhPFGxYba4CFI4UBo0QcucztgoUwvRr0Ok-beT1BHvGsmdKVHK9pA2aKCXztQc8Gp1IASc_wvh4Ry4joKZgZmWvZjwPruzYrpizqIP0nn1TYrPkHE36xJ-SYpVA6qkVu1OhYHIYhx26REL3ibXd5fsNa8U3Xca9MuEpKe5UZkhqLdjIFy1xmDg9vhynjcfVqYtqrfBUQ4bCaSNQgp6Pa6Duf9xV4ryUc0leKIxle6ZtQSYwAFH_15ZxMAaMmWor34CkScNh4qvCO41kXR2WAJKEkKhZvIjyA16-Y4KF1XZaeokhWzNyKwOjUt-Jk3R4UHkpiZ6lyf-FUPwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbnRk0-uYKQQk9f5nkWBqeOmgNidyZpghSomafJfGnoZw8iow_ACJjeQjg4Fy5804TmMqQscwFAGYpL9PsLg1Qv9m243f0pb52OqX5w9V84THQI-Mc2jpkipRfOTH26mm-M3Wmyg4duu2cEXZMNe3zWY2P2P5daGiniWu_8IrCEkxYjyvMpbLTTIvIzGMsFR60Vp0sMxmzDPrYnhDYkiqO0eDSauH1aMdTJY2NHulazJsO1smVYAtJJq6Sezm3IyJkhbaL6yRIU_Uk0m4Iu66FkVyv3-YjzM_JRP3qZ5Zq0Q1W7kBUhsW11pkncRfMy69RExqJfNoTvwJOa4yAb7Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8npflxv5dsBwhrRI0LIM82o0mKbbZsPgBhdQ-genq2B0uwXzhk9GVAZJHeXaVpHUp45P9dr_kggVpg_U3DcOGad6YZKS7KrttPiEH3NUV8tzSTRSzys7uHhnglOaHV8dJXsesFy3N-5AmM_vG0cEMZs9JLRcc-S9eP59tC3NTLfvgFy8DWdIJVt21TcRzncMQLlEoUoTLVJ3XETuvKrlcb8PkIlWEZC_emOgmi1x-jZTUI7cqPMZRIpBQXajfOG0JPWolMvbzFtTbMjPfCEVToinAzj9jGxxrbDLhMNf8j31tDbks7WCfub3E7s5W5jgdYs0TUahpuP-j1phdjqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ef09Zzk1Qf3xYfFZoZbSdiArE645xQBeDDFeAiydD5MhDemjqEyU6mOcWXIq9bOhcfS2bJfeK_qZlk4s5KIyAVdh7d_Wk1XpPBofsD_6h13mRepApcGd8n0pbq72UeoHeGiGQoFINOmCXLoPE-lu3AtamfU5EUGnFSXYn9BN00vdn_buw3J0ou47HDd_3qAvMU2beDrhH2noK7150wg4wRYZU9zh7ydAhGNflM4hmSwCBhJMSsCt51HT2PE7Vcps4ECWoDaC-qzHeFl5hWq_GhWae1vXqbGQkUr4bvrRbPMwE9l-stiMfTI7VPldcHkgYxKH-u0RrcghqDGdku8llA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VETYc0lydAIKcTN2mHVPewQVDES3CbTX2zVW9Nd2kvlqNUQ4_5TYYlvkwygum2I5kdNegEIqPTPula5_FB2usRVqoZVKoXCjfTNBneYWfu4Y88yBnpsfv6Qvaze2lXf_Bsi__s698WtTmUUO7254a3YkLwhGTnT0_hzl7Xk-Q2GV-asZCB49WMO8-l_3wKY8EyWr2r7yRbfnt96tLvngGAy3zdgvKZ5FXeJuCyZtjGKyoNc4A7Zfno-a9pw82xMMXlTiRfwVU_bG-lxIVqZXhc7LFWVVNkPTtizAA6FhoaNhyPMjaXRFnDck-FPqoxiFhWfjOg1pGPf-Uy3m8L8oLg.jpg" alt="photo" loading="lazy"/></div>
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
