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
<img src="https://cdn4.telesco.pe/file/rWul12Ata86GN2XQjK4lBCQbd9nFe9YMS0ZqGAuIO0tsY_0XowaZm-cvBOXgVqLhDCoZpiTfrh7Nmo4oUwK2YD1V0rqGEmKttVltQhZykw7xBll-JnJAHaomy1aVSalWESM6yXnSWBSjpJNFysKW2vpIp9RBMfDCg1DeTqEkhyO_vS1ILeE3N2FQgQAqpU1cojUCeJcMJo1Rw-e5xbp02MRR7nss4Sh-i1nq6pVZqxykbLuGzuv80skPV8oUWJukD2q__xQrNK7aVYT4YvrWWjgkD56b5fRS_D1sh_hCUodBiTQlGqFiGWHl6Yq5c9y7z7lGrsMKLbXl4QNOGE0dkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 19:03:51</div>
<hr>

<div class="tg-post" id="msg-455156">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fbbd8f7d2.mp4?token=JmFBKtbRz3ZuojmtCLgDOUQy4ov9-Q4ozjzbuuKZHqC4oEM3EP7bVCr9ngYXyNsV6J_duB4Hml6D9IU1mL5-lzLVhMWT3LxNQUKnIEj54Uje37SxTpz7-fF9URANDfQLNvtFARe5K8SLQYLzTZ_D4r-9uH5BY9QOFYO8tAuRq_D7AgXyugFY0sd-n6ECvTaE3XzJlbkbfNQ8wasGSWtRgXqNVtKqySFOH-1w6FsqUISMt9Z-4wQtqkCI_oqHtDAiQ2Xjh6T69Knbsg7Thxz9br05Y-L9c7oc-T8hpYyU7zbYrCUJ5xrHu1Q1aJs9fDbC7OVR187L-GVHZNB-1W9PQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fbbd8f7d2.mp4?token=JmFBKtbRz3ZuojmtCLgDOUQy4ov9-Q4ozjzbuuKZHqC4oEM3EP7bVCr9ngYXyNsV6J_duB4Hml6D9IU1mL5-lzLVhMWT3LxNQUKnIEj54Uje37SxTpz7-fF9URANDfQLNvtFARe5K8SLQYLzTZ_D4r-9uH5BY9QOFYO8tAuRq_D7AgXyugFY0sd-n6ECvTaE3XzJlbkbfNQ8wasGSWtRgXqNVtKqySFOH-1w6FsqUISMt9Z-4wQtqkCI_oqHtDAiQ2Xjh6T69Knbsg7Thxz9br05Y-L9c7oc-T8hpYyU7zbYrCUJ5xrHu1Q1aJs9fDbC7OVR187L-GVHZNB-1W9PQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع سعودی: انصارالله یمن با ۳۰ موشک مواضعی در بندر المخا را هدف قرارداد.  @Farsna</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/farsna/455156" target="_blank">📅 18:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455155">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c2022554.mp4?token=Zwbq_fh2v6PWF9KFB9OzcgZfNglFbsh9_B0toyt4fwADF1zOdLMjdaF2f6xmxonRgdk9C-htI4CsNP2HqVVKnEoRFu82n4b92LbBaQztBwXTaT0mfsy5DE2TV7Nut6ZGZUGOiwWd1ZDwZrf8dUSFCMiXiB30GP3K3weDSc9DWvQHzGVlGXG0cdQoz_3DvwzQs2yeW2Lj7cjcuiWpHi42tEBX8rTrkAMnrpFwzAJ7A-Dsk2ueSSMMMWFIZ8mOU-FZPlVIPZ6W0FQbq90Wh5krvKl6YcisRTRQWFMZWXY19dyrrSfa67blExwOLJstMr3jrtA5qVmGYSKNikC_CMcoJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c2022554.mp4?token=Zwbq_fh2v6PWF9KFB9OzcgZfNglFbsh9_B0toyt4fwADF1zOdLMjdaF2f6xmxonRgdk9C-htI4CsNP2HqVVKnEoRFu82n4b92LbBaQztBwXTaT0mfsy5DE2TV7Nut6ZGZUGOiwWd1ZDwZrf8dUSFCMiXiB30GP3K3weDSc9DWvQHzGVlGXG0cdQoz_3DvwzQs2yeW2Lj7cjcuiWpHi42tEBX8rTrkAMnrpFwzAJ7A-Dsk2ueSSMMMWFIZ8mOU-FZPlVIPZ6W0FQbq90Wh5krvKl6YcisRTRQWFMZWXY19dyrrSfa67blExwOLJstMr3jrtA5qVmGYSKNikC_CMcoJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان یکه‌تازی آمریکا در صنعت هوش مصنوعی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/farsna/455155" target="_blank">📅 18:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455154">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌ سخنگوی فراجا: در پروندۀ قتل رجب‌زاده تاکنون ۵ نفر دستگیر شده‌اند
🔹
سردار منتظرالمهدی: در پروندهٔ حمیدرضا رجب‌زاده تاکنون ۴ مرد و یک زن دستگیر شده‌اند که یکی از آن‌ها عنصر اصلی دخیل در قتل بوده است.
🔸
حمیدرضا رجب‌زاده حدود ۱۵ روز پیش ناپدید شده بود اما ۴…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/455154" target="_blank">📅 18:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455153">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
منابع سعودی: انصارالله یمن با ۳۰ موشک مواضعی در بندر المخا را هدف قرارداد.
@Farsna</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/455153" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455152">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ca6e5f69.mp4?token=YSJg0vaW-agmDKxIkHihIZDoPuUwF0wn1dcZEX6J5bssm7hxJk81rEcagtbAA4PHOAeV4DG2CCKzYP_fvumiT0x-N5wEJmgKW8W4I4XBxgfPGJTkNkpnZYuQj3C2F-za6pRfHRlUPP3BA0q5Ff6q6faJ6vtVNEaaGiK7_fgvDp_b0pLXMMdYt2exF-qZ9CHMGJH3W6CYiUlNQwwM4MpHnikLAzsyt2ckkNhlt1h_Pjd7NGgIhReCTHiM6VwWf4S_gJOO1KHnZ93PzF9TPsLbBIZKbzWXtDjh88Ow7r-n8t_I0xO7vBEQ7KZQu4m2p6BTqtJe_xIonSpgtr-4h4QDIocHcIrKGMPbXutWGdCY5bG_I6zxbmSW3j8BUEe4LC-1EtiWdsJW5-xNc3U4Fd6RnY27IwWSuptBGWqEjjsrrii8ZD8x9wQrAdz1PJJ3PFO5X17EVdK8geA1AYqCxGrUT3FeChzuVMyUIu6Ztm-23IPCgf6DyI9Mewqk1BSUmtJBCxrWH8Y4pLQE4D2QC3WNg0CG0wpHgkgImIRVAfRGNrwU3fZRVGgqQhQXvOgKlMzAKIXtLznxODhR0yrxt-An7XsaPdTwReNxI-tDS6m4VU-g8zqHghyMYzUwvLOTE9y4wE1Kx7rYc6FszIG65oPE4o9cJAGqq_dg9KyjbXdW2cU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ca6e5f69.mp4?token=YSJg0vaW-agmDKxIkHihIZDoPuUwF0wn1dcZEX6J5bssm7hxJk81rEcagtbAA4PHOAeV4DG2CCKzYP_fvumiT0x-N5wEJmgKW8W4I4XBxgfPGJTkNkpnZYuQj3C2F-za6pRfHRlUPP3BA0q5Ff6q6faJ6vtVNEaaGiK7_fgvDp_b0pLXMMdYt2exF-qZ9CHMGJH3W6CYiUlNQwwM4MpHnikLAzsyt2ckkNhlt1h_Pjd7NGgIhReCTHiM6VwWf4S_gJOO1KHnZ93PzF9TPsLbBIZKbzWXtDjh88Ow7r-n8t_I0xO7vBEQ7KZQu4m2p6BTqtJe_xIonSpgtr-4h4QDIocHcIrKGMPbXutWGdCY5bG_I6zxbmSW3j8BUEe4LC-1EtiWdsJW5-xNc3U4Fd6RnY27IwWSuptBGWqEjjsrrii8ZD8x9wQrAdz1PJJ3PFO5X17EVdK8geA1AYqCxGrUT3FeChzuVMyUIu6Ztm-23IPCgf6DyI9Mewqk1BSUmtJBCxrWH8Y4pLQE4D2QC3WNg0CG0wpHgkgImIRVAfRGNrwU3fZRVGgqQhQXvOgKlMzAKIXtLznxODhR0yrxt-An7XsaPdTwReNxI-tDS6m4VU-g8zqHghyMYzUwvLOTE9y4wE1Kx7rYc6FszIG65oPE4o9cJAGqq_dg9KyjbXdW2cU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از شکوه طبیعت در زیست‌بوم زاگرس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/455152" target="_blank">📅 18:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455151">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWA8jVm6nz2tJ6zIriQQs-lSIbp0ZBJeA7IszYpHrB9Mdn5fvvOiH8QcbT90YLVOSMD7y40AQDBED-ovYrh7Pp1YLgSp0NMdDaLnLexavmY3WflxeCxM_JJWBGsL_1vJ1vWERaj-76fXTEcqcoIJxy0vh0LORPzvuRnU87KBbz9_51fKRaL_qGQ3UrjnuNfJwuQrMAXc2xYIRXzshZJSUOnI9Ir9Sxi_tkLUle6EdlJf-EI3E-c3SNERNPELuS21cHka35ebwJu8YROyq48wfVDXnRaEo4PWj3N4QAiCZvdniQYmxuNj8DPkyDsgoUtYbUW-2NWX2MiOsGSKTL9kXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات متن اولیۀ طرح راهبردی مدیریت تنگه هرمز
🔹
سلیمی، عضو هیئت‌رئیسه مجلس: متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.  براساس این طرح:
🔸
عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/455151" target="_blank">📅 18:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455150">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxecfvbeiFF7GoqLfdoHqv102unNwBQUTTqiBep9lDzyxZEoT9jVXKTNxtIcMX_HNZxAHBENPMtd0AbNKUHHeYhwEcLx2DhFjsEGdRDvHA629yylDWl4-IDvAjdUUxrLo7812tIsO1eM3kNe9ZnxNiC2ICGqRfLDEsfKzU4_1F2YsbXEn4AJBTy0Gjh2zsgc0bdh8hj408UmF46mz0z11QR-zfL33_iypRGgNOuPUvVc8ac-5_YxSUjqDVNQKHEvCVf6HaqTXnshTJIBwtyFzBw7GljSXiHnenMCctYIOBOhU6iQr69MGV2Ay69bsQn42oDzs1noM4Nut1hALkL3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخصیص بیش از ۵۰۰ هزار تن ورق فولاد مبارکه به پروژه‌های انتقال آب، نفت و گاز
نخستین محموله ورق فولاد مبارکه در سال ۱۴۰۵ به کارخانه‌های لوله‌سازی پروژه‌های انتقال آب تحویل شد.
پیش‌بینی می‌شود امسال بیش از ۵۰۰ هزار تن ورق فولاد مبارکه به پروژه‌های انتقال آب، نفت و گاز اختصاص یابد.
این ورق‌ها پس از عرضه‌های متوالی فولاد مبارکه در بورس کالا و انجام تعهدات این شرکت در زمینه کف عرضه، بر اساس مدل فروش توافق‌شده به پروژه‌های مذکور تخصیص می‌یابد.
اجرای این طرح علاوه بر تأمین ورق موردنیاز پروژه‌های استراتژیک کشور، به تأمین نقدینگی فولاد مبارکه برای بازسازی بخش‌های آسیب‌دیده این شرکت نیز کمک خواهد کرد.
@farsna</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/455150" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455149">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKwswDugGQpw_VjwaVOejRw4XFU2gHDaR2xL2GXmw2smKmqUwECtcK-HVI_FZEwdU-JaEHDkuVMrUZjNpHpVSfSPd1OT18BnR7KmVN_2jYUb1dfkS0WGs5AM4yeoT17lpSjuDEGAYQd_7y-HV1u39ChwWODwTr6aiyGl5sNTEPUc0Wnb4I5mYY5PndEVNlpc1KXfjfNLFttO65pSwG-LjULxSk8obUwTrdmNVS4OOdXDcHhGM_v8Is7yCGee1uXSBNi7HlqBroAkM4qfGTF88sp5ge-kvomMHBAKFUixEzQH_hkaVKW9qxaq_GlFnqMuEsp8XyUT5lbY65U99ABauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
شرکت گروه پتروشیمی تابان فردا (سهامی عام) با نماد "تابان" در فهرست نرخ‌های تابلو اصلی بازار دوم بورس تهران درج شد.
🔸
به گزارش مدیریت ارتباطات بورس تهران و به نقل از مدیریت پذیرش، با توجه به موافقت هیئت ‌پذیرش بورس تهران در جلسه مورخ 1404/09/12 با پذیرش سهام شرکت گروه پتروشیمی تابان فردا (سهامی عام) در بورس تهران، از تاریخ 05/06/ 1405، این شرکت به‌ عنوان ششصد و سی و هفتمین شرکت پذیرفته ‌شده در ﺑﺨﺶ "محصولات شیمیایی"، طبقه "تولید مواد شیمیایی پایه به جز کود" با کد "4411" و نماد "تابان" در فهرست نرخ‌های تابلو اصلی بازار دوم بورس تهران درج شد.
🔸
سرمایه‌گذاران محترم و علاقه‌مندان می‌توانند به منظور کسب اطلاعات بیشتر در مورد شرکت یادشده به سامانه اطلاع‌رسانی ناشران (کدال) و سايت بورس مراجعه کنند.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/farsna/455149" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455148">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/455148" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455147">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ffc69a97.mp4?token=cajEFLJGP_5zH2QNZh81bdVK39qHQ27g402Z9jXoq4BtX246Q1WOvHkZCvhOD0oo_5Qcza3JrA-OnOee3lkakR4e0LDIoBtvIcgzgvjEtFp_co-GklG0wPdruJEzffECYVHzSRfmeMybxf3MuN3PgW-5MfSiw-3_J2k8VyFN5EjZjRG9K4zOtrafiJKwWPtjUpIoZBtmCBhGgvUEVAQG42MYAmL2KIiNtGCArYxsfsbqV8Gik32JHe0G1qTc3BHmjFY2k7TKMXKCEAW5kyDjWjN4hJeOerAOv-OyHT333Z_5Ju236zgGtbAVRsqAjArD6KslYP3TVf46USvUT2yI4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ffc69a97.mp4?token=cajEFLJGP_5zH2QNZh81bdVK39qHQ27g402Z9jXoq4BtX246Q1WOvHkZCvhOD0oo_5Qcza3JrA-OnOee3lkakR4e0LDIoBtvIcgzgvjEtFp_co-GklG0wPdruJEzffECYVHzSRfmeMybxf3MuN3PgW-5MfSiw-3_J2k8VyFN5EjZjRG9K4zOtrafiJKwWPtjUpIoZBtmCBhGgvUEVAQG42MYAmL2KIiNtGCArYxsfsbqV8Gik32JHe0G1qTc3BHmjFY2k7TKMXKCEAW5kyDjWjN4hJeOerAOv-OyHT333Z_5Ju236zgGtbAVRsqAjArD6KslYP3TVf46USvUT2yI4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت مشکوک یک هواپیما در نزدیکی پایگاه آمریکا در جیبوتی
🔹
یک هواپیمای ناشناس و سانحه‌دیده درحال سقوط به‌سمت پایگاه هوایی چابلی در جیبوتی است.
🔹
ساعتی پیش سفارت آمریکا در جیبوتی با ردیابی این هواپیمای سانحه‌دیده از مردم خواست تا اطلاع ثانوی از تردد در اطراف…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/455147" target="_blank">📅 17:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455146">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎥
تنها خواستهٔ خبرنگاران و مستندسازان دربارهٔ جنگ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/farsna/455146" target="_blank">📅 17:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455144">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d573febfb6.mp4?token=k09U8hSwgzHJXbgn2S0YXPfSNvhuCwzsEU7_ZJSBKXEyxNXzS9ZX1N1LEKs4SnP7l06QU-LCF2g5duontldR3D-UVn03rdD-K9ZWNajrneccTc1tUcXM_4gZ6YXIeemlwE9YIByXovh33KCw3PGI8WFMS4zQoE6-PO0E2U9OD5jqjVDcxzWJT3jew_lz6FHXJuaLG5u_wkxKL-M6BvdvMhh7umpffHmr98e5hD3zz24rucrJmzmgzvB4RM7a5sEIXokbMOjyNerTNCX5qi83jWnNnH6dX9_uG0HqcRsUezT_X-nHqNeVz7-6aBKkFTK5i9ey0Y46ZIdbnKyCDa9d0avt38GXseqU8BJC5ERdWKgnjA2NsBCx-wwADt6DZotLRgRD1HfVkdDgWrM55CADbi0vhMQr_RlR0cFgPDwIe2QUmit63XaGzExoop45QJHlMgosMifHxATaN75mqt36eQHT0dBCb_9j7__Dj7Q25iCFE1q-xw13kYI-hp6BO20nkWjOGy6CT5Gfu1p1GzwsJUiL8AwbKzTdSdLoTdaBzOKb-EpR6Brw9HaVWzowEzYbUuAAiEtZFrfZDKUihTcp3sEi7f4QpTPk3DybyJXCNzDlgxhydOOaAWg0uuSM4FEiHTdlC8uM_zxm_mrybRHXkTHWjihuRgquV1UIdRWR0qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d573febfb6.mp4?token=k09U8hSwgzHJXbgn2S0YXPfSNvhuCwzsEU7_ZJSBKXEyxNXzS9ZX1N1LEKs4SnP7l06QU-LCF2g5duontldR3D-UVn03rdD-K9ZWNajrneccTc1tUcXM_4gZ6YXIeemlwE9YIByXovh33KCw3PGI8WFMS4zQoE6-PO0E2U9OD5jqjVDcxzWJT3jew_lz6FHXJuaLG5u_wkxKL-M6BvdvMhh7umpffHmr98e5hD3zz24rucrJmzmgzvB4RM7a5sEIXokbMOjyNerTNCX5qi83jWnNnH6dX9_uG0HqcRsUezT_X-nHqNeVz7-6aBKkFTK5i9ey0Y46ZIdbnKyCDa9d0avt38GXseqU8BJC5ERdWKgnjA2NsBCx-wwADt6DZotLRgRD1HfVkdDgWrM55CADbi0vhMQr_RlR0cFgPDwIe2QUmit63XaGzExoop45QJHlMgosMifHxATaN75mqt36eQHT0dBCb_9j7__Dj7Q25iCFE1q-xw13kYI-hp6BO20nkWjOGy6CT5Gfu1p1GzwsJUiL8AwbKzTdSdLoTdaBzOKb-EpR6Brw9HaVWzowEzYbUuAAiEtZFrfZDKUihTcp3sEi7f4QpTPk3DybyJXCNzDlgxhydOOaAWg0uuSM4FEiHTdlC8uM_zxm_mrybRHXkTHWjihuRgquV1UIdRWR0qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز خدمت‌رسانی موکب کفشداران حرم رضوی به زائران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/455144" target="_blank">📅 17:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455143">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4gkH5h0ubla3twwmjVQhzT1iO6yTAvFkeeVu4x8VxCAxotfgJ_H8S8P2QQYBmhU_BWM4LlZ1-NnCrAbg5wM2-8KzBmUwiJM3znLO-z7uzf_d2AIMNlm2ZN2_X-WmzWv85Shkj9gUI3EFZWsJCPDyaNEotN1D5aLeEBAPp6CIgmUsXTT3Lci2Gq60dIhQQDcYRFaMVxIK-zscm28pXcRMJGOW_rLPUzveqIDCx_rIBbrg1XcexnuTocq3-m1qLhePl2faw3s3wWyRgNy1Ph9NmHt5y8elhJN4C9IJUtu23WieXHABwe0NDuzc9k8A0jbNLoInX0HAYVYu40I6g9HFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکایی‌ها برای مهار شبکه‌های اجتماعی متحد شدند
🔹
رویترز: نظرسنجی جدید در آمریکا نشان می‌دهد اکثریت مردم خواهان نظارت و مقررات سخت‌گیرانه‌تر بر شرکت‌های شبکه‌های اجتماعی هستند.
🔹
۶۱ درصد آمریکایی‌ها معتقدند دولت باید نظارت بیشتری بر شرکت‌های شبکه‌های اجتماعی اعمال کند.
🔹
یکی از برجسته‌ترین نتایج نظرسنجی، حمایت گسترده از اعمال محدودیت سنی است. ۶۶ درصد آمریکایی‌ها از قوانینی حمایت می‌کنند که شبکه‌های اجتماعی را ملزم کند برای جلوگیری از دسترسی افراد زیر ۱۶ سال، سن کاربران را احراز کنند.
🔹
این حمایت حتی در میان جمهوری‌خواهان، که معمولاً نسبت به گسترش مقررات دولتی با احتیاط بیشتری برخورد می‌کنند، به ۷۴ درصد رسیده است.
🔹
نتیجه نشان می‌دهد نگرانی دربارهٔ کودکان تا حدی از اختلافات سیاسی معمول عبور کرده و به یک مطالبه عمومی تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/455143" target="_blank">📅 17:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455142">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI4n_1lCYNsITjAyG5hpBV2XjZ2-U7N5gYP864qdohmruyzt-_V1F96cD6tjYCp4jIO0LGGqbWiudgzmPdMpO25auuMd62ZDfin1ZEGl5Gjsoi7HmiAwl3kWfc4PZZmilrJeoofhNEwvtmB9cetDlBdYjCBeKv72KZJTwbXQ2nJUnLNWzekUy2bHsdcJdeZQE9rTah3_eVH8_CtwqG29SFS-eBIylY2KSxOHyV5_dpgNgSQO8M2f0dm_YP6g2puknW_x7KaaS1nHwooizxmcDZaUlwvLTvyD7rg_JMatcmGcqrzv90M0XsXeV749cKhauwryR459tleASyViIRfufQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله آملی‌لاریجانی: تنگهٔ هرمز به شرایط پیشین باز نخواهد گشت
🔹
رئیس مجمع تشخیص مصلحت نظام: ملت ایران و نیروهای مسلح پای تنگهٔ هرمز ایستاده‌اند و حاکمیت این آبراه با جمهوری اسلامی ایران است.
🔹
به‌هیچ‌قیمتی عقب‌نشینی نخواهیم کرد و تنگهٔ هرمز به شرایط پیشین باز نخواهد گشت؛ اگر خواهان تردد آزاد هستند، باید به شروط تفاهمنامه عمل کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/455142" target="_blank">📅 17:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455141">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqg8E3VZo9aX1vPNlmTxTw9UgwlSsmn5e8xD5M4KfTiUDuRxO6uaqTucr8pUBgSQ96xzxNtE58TAQG9dhieA1cuS6tuvAfk6T_i8dTahzvDzbplU91IZlsp1_rum4d8N0SjjKFr_ZFmtbSjvRW5IJvvzZwfYOe1SMZ6m4Gf7XL9HTAEcIxGNrjUz9gY6JCHMOb_PvSKYkmxkuXLoOtmLcxJSCr09pHmmitwnY1GpEmFM8IO0Zs4dxBQr9GqtCNh1MTy8UOMQ_DqERDjfPkXwyM5BZx30_NxpDveUl5JOnrPu1ksA8QYbRQpZeesq7SiRbmaZyHtC3vJUj_jUMbgolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۹۷ ماینر در یک مرغداری زاهدان
🔹
تعزیرات حکومتی سیستان‌وبلوچستان: ۱۹۷ ماینر غیرمجاز به‌ارزش ۳ میلیارد و ۶۳۰ میلیون تومان در یک مرغداری زاهدان کشف شد.
🔹
در این راستا یک متهم دستگیر شده و به ۳.۵ میلیارد تومان جزای نقدی محکوم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/455141" target="_blank">📅 17:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455140">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/up2j7DYryUieBusadkrMKeI4OrL10HkZRXXBtx2N-tVey0SAD0_7n-orpFvgOzJ6CQBT9u4bWU9V1l0W_XO17LjjKBoaUqfq7Wenjy667eqWfUZ2yaRVcOvvYPJQ9d3D0vp6rkE8-egFPaCYHjJSOESsSJgziRbFutlpPF2UwVgWo8UShTk6gj1d_IXqy-qi34Z_erGRPMrJa60pOXpVlKNGnL6vdYw61WYBSapNtiq7peKP5OrRF3osQ9UiAkdlob5kF7doKkrcKJF005qVJ1nKfkO16R6CNQjM091VMZOk33ebK-gtwjRDyKu5VZ-dU5L6_EUUlr_q0h9p1j4fnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏀
ترکیب تیم ملی بسکتبال با ویلچر مردان برای حضور در مسابقات جهانی کانادا مشخص شد
@Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/455140" target="_blank">📅 17:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455139">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a549d3423.mp4?token=M6rlQlBbY0kiuq0lekehYk5u_H3jlQgDu4jU-o7chCZVd8ojiVBm2qrdvR3IIGpb6TogZV6XvBF0G7-NF7LJGxZcen0JyxBPgE9F0n9pDX_xu9YWCesa7BfHWG2zWB3wk82gdhsM3CNnx99m2qhOGCxoZVbJWi00HZTA_h1OdgYK2m6AlCxa8mFIAYxLuezRYDR5nI-NG_vv3B__huzl_6SYG-dL92H0KoAVzicxAqR9qYek_35b7eR4RUt7YFjbY5M8ajfMdZRdGpwsQSLu-Hyz4zo-ICuwVkdi4M65EoiZwpeZpqONrV11CNXuD36YnN6Kl5wunypyZrQjXp7zCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a549d3423.mp4?token=M6rlQlBbY0kiuq0lekehYk5u_H3jlQgDu4jU-o7chCZVd8ojiVBm2qrdvR3IIGpb6TogZV6XvBF0G7-NF7LJGxZcen0JyxBPgE9F0n9pDX_xu9YWCesa7BfHWG2zWB3wk82gdhsM3CNnx99m2qhOGCxoZVbJWi00HZTA_h1OdgYK2m6AlCxa8mFIAYxLuezRYDR5nI-NG_vv3B__huzl_6SYG-dL92H0KoAVzicxAqR9qYek_35b7eR4RUt7YFjbY5M8ajfMdZRdGpwsQSLu-Hyz4zo-ICuwVkdi4M65EoiZwpeZpqONrV11CNXuD36YnN6Kl5wunypyZrQjXp7zCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوک شبانهٔ تراکتور؛ ربیعی رفت و نکونام سرمربی شد
🔹
محمد ربیعی در فاصله ۵ روز تا نخستین دیدار تراکتور در لیگ برتر، از این تیم جدا شد و جواد نکونام هدایت سرخ‌پوشان تبریزی را بر عهده گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/455139" target="_blank">📅 17:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455138">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d143b9e96.mp4?token=livNvHoPmkWcsbjZZRIQMbY3vx1GyVqIfWIOqp-y33SN5JQZnri0rnlc8J661fxTuBWk4G4wm7qxQiybRgJvmpGJWK_4SLRB_bpV6b9DdBmmWb06LWQ1h3KJzj1aekA1qXngNA0Jp8mL7yVFQBQDDRUfWmvhemsar-Aye_V__BKMGMu7FeXCrRhIyKNPIZGDj8pvjovZuClvrUr-78cJAOrGBjXgsEOKu12qd8I-PuRvPbCsUtKPoEKI4i-YW_-5jeJUoCt0N2OM06Hghy3ntR9ubm7-GFbeDB7sh62_rA4EuHx3t6uRXETa18ix1jJdSEn-ruJ9J4N2kFIAEyiimw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d143b9e96.mp4?token=livNvHoPmkWcsbjZZRIQMbY3vx1GyVqIfWIOqp-y33SN5JQZnri0rnlc8J661fxTuBWk4G4wm7qxQiybRgJvmpGJWK_4SLRB_bpV6b9DdBmmWb06LWQ1h3KJzj1aekA1qXngNA0Jp8mL7yVFQBQDDRUfWmvhemsar-Aye_V__BKMGMu7FeXCrRhIyKNPIZGDj8pvjovZuClvrUr-78cJAOrGBjXgsEOKu12qd8I-PuRvPbCsUtKPoEKI4i-YW_-5jeJUoCt0N2OM06Hghy3ntR9ubm7-GFbeDB7sh62_rA4EuHx3t6uRXETa18ix1jJdSEn-ruJ9J4N2kFIAEyiimw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوتی که در بزرگراه باعث تصادف شد
🔹
در جریان دیدار تیم‌های مونته‌ویدئو و پایساندو در لیگ دسته دوم اروگوئه، دفع توپ توسط مدافع یکی از تیم‌ها و رفتن توپ به بزرگراه باعث تصادف خودروها شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/455138" target="_blank">📅 16:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455137">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f605262cb.mp4?token=MSW-cC50s-BSPtQDyVrbldgY0H8AwCpR8CcrKEoMMrZUndCwKBiDCI3tZe0Hd-qsr8tFDlHRsvGgJUjAfnnEzYLQHCmLQTyaEwkWGoJ9abOhVW0y7agPxZFBXqUkpcU4P1dWUBLpdpmWUgleSu8bb2QaDmdM8djBppAdtDGQXaLMu6sbLhvb2HMwrjoesvY0Q4Sc-ZyikIR3bJaAswrpDFCQcRrFNl5M1RUu6-nBRDDjynXwt4PAWl7E2PVeVIvcjriKsdWbh-B3TFG-y6dYhgJwSNFdodS3ujGl5hmtbjtBkdKeHFEfTy4zUTgFj8zTNOTIRmQUuaiRrpTcWcQzwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f605262cb.mp4?token=MSW-cC50s-BSPtQDyVrbldgY0H8AwCpR8CcrKEoMMrZUndCwKBiDCI3tZe0Hd-qsr8tFDlHRsvGgJUjAfnnEzYLQHCmLQTyaEwkWGoJ9abOhVW0y7agPxZFBXqUkpcU4P1dWUBLpdpmWUgleSu8bb2QaDmdM8djBppAdtDGQXaLMu6sbLhvb2HMwrjoesvY0Q4Sc-ZyikIR3bJaAswrpDFCQcRrFNl5M1RUu6-nBRDDjynXwt4PAWl7E2PVeVIvcjriKsdWbh-B3TFG-y6dYhgJwSNFdodS3ujGl5hmtbjtBkdKeHFEfTy4zUTgFj8zTNOTIRmQUuaiRrpTcWcQzwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصاحبهٔ عجیب خبرنگار BBC با یک اشغالگر اسرائیلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/455137" target="_blank">📅 16:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455136">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c08f1d721e.mp4?token=ZcrlXeteVXREcdadkhl6K0MxSNxCdPa4Yy6Xy8o6zJm9eiLyivGrUmTmhvM-U71aErHL6qJNMuslePVWOxeSx-XJAHB2gJwyl1gromInjTdlZeQyymTD545t88DH1p77L_zW7JmfErfqdR-7YTWgqueNr7PeSej7tiiQ4tO-BDyKh60MmvJ5OIh_RhWwzN4mQwafeMvecXDCpJWlV_GjHLuIs6b6cUsnP7toetIpEKkDL9Y5wf_9Q4r3zewhWW8wSfWHUvPSmbLeKysW7blslBglOiaDPNZ8DbEKLqMi3oE4xJPhjaONn5k-6Sh9cIESegRSRmG56SWJpFO8CWWb8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c08f1d721e.mp4?token=ZcrlXeteVXREcdadkhl6K0MxSNxCdPa4Yy6Xy8o6zJm9eiLyivGrUmTmhvM-U71aErHL6qJNMuslePVWOxeSx-XJAHB2gJwyl1gromInjTdlZeQyymTD545t88DH1p77L_zW7JmfErfqdR-7YTWgqueNr7PeSej7tiiQ4tO-BDyKh60MmvJ5OIh_RhWwzN4mQwafeMvecXDCpJWlV_GjHLuIs6b6cUsnP7toetIpEKkDL9Y5wf_9Q4r3zewhWW8wSfWHUvPSmbLeKysW7blslBglOiaDPNZ8DbEKLqMi3oE4xJPhjaONn5k-6Sh9cIESegRSRmG56SWJpFO8CWWb8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چین در محاصرهٔ طوفان دلفین
قرار گرفت!
🔹
تلویزیون مرکزی چین از وقوع طوفان سهمگین دلفین در چجیانگ خبر داد؛ حادثه‌ای که با وزش بادهای شدید همراه بوده و وضعیت اضطراری ایجاد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/455136" target="_blank">📅 16:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455135">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpoPhaVKOm7TnzWCZ2vLhtaN3e2KAkB03URuDEBOO-r8bgLE4RVFJa-9Yu5awr1SHNdDflqDc7z23O_j5wD8M57EAiRHE8LWWDUJHF6XSx6mVMn1hGRgQm9GomSa4cfchBAixGFB9PCw3qPVhbe4J7pylQf9exvqeT4P0s0V3iYptt4QD3Y-kM9ql9BfwGB3EJCNgzHSxc_HF-Jkkq7njHUjAqG_a1XeRMvvPhsW3j9S4WYZEdmISAofDefEU9JvYPToHWChqcDc_2RDyTD7L_BAysUSI2YPELCMDkrby8pjyixHOToPc2SZXFF1j2FvIq6rUAPDK6Mxxi6TfeBJKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق دمشق و مسکو بر سر وضعیت پایگاه‌های نظامی روسیه در سوریه
🔹
وزارت خارجه دولت شورشیان حاکم بر سوریه اعلام کرد که دمشق و مسکو به یادداشت تفاهمی جهت تعیین تکلیف و آینده دو پایگاه راهبردی روسیه در طرطوس و حمیمیم دست یافته‌اند.
🔹
این وزارتخانه تصریح کرد که این یادداشت تفاهم بر آغاز فرآیند «سازماندهی مجدد» حضور نیروهای روسی در سواحل سوریه تصریح دارد و بر اساس این توافق، قرار است پایگاه‌های نظامی روسیه به «مراکز آموزش مشترک» تبدیل شوند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/455135" target="_blank">📅 16:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455134">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e35e5383.mp4?token=CP4NtHJLN0E9YVFPyJe28oiR79YPoxuOZUoLcuLIqAKaxYJcY16pIapFt1N_Bz9hqCwvpqLVBB6rpn8n4eO4dQoyAah2ugFXNkztYzZhYS8ALhFZSrYscpVEl5i3pUbET6D19A0RxveJx56Rg3_n3qf0ZBU_za_Y2d0Pon1fUoi-wqXV_G9akQ5RnxIQjMVt_8fbHI5mjiJf-NMHOp16PKI7ut2HcbBZ8gM3ATLMyIk7VIjkB4MHc4kCdABYs8rrzn4UhFG6yanYAuD2ePBw9WPojG9xYMaERN-pRlQ0uN3M0NSD9WehImQY-AJgIjNa2Ua25HXRe1z7xyCQtxbAsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e35e5383.mp4?token=CP4NtHJLN0E9YVFPyJe28oiR79YPoxuOZUoLcuLIqAKaxYJcY16pIapFt1N_Bz9hqCwvpqLVBB6rpn8n4eO4dQoyAah2ugFXNkztYzZhYS8ALhFZSrYscpVEl5i3pUbET6D19A0RxveJx56Rg3_n3qf0ZBU_za_Y2d0Pon1fUoi-wqXV_G9akQ5RnxIQjMVt_8fbHI5mjiJf-NMHOp16PKI7ut2HcbBZ8gM3ATLMyIk7VIjkB4MHc4kCdABYs8rrzn4UhFG6yanYAuD2ePBw9WPojG9xYMaERN-pRlQ0uN3M0NSD9WehImQY-AJgIjNa2Ua25HXRe1z7xyCQtxbAsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایران چطور برنامۀ ترامپ را به‌هم ریختند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/455134" target="_blank">📅 16:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455133">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02de7fa7f.mp4?token=uirMSRVim1pCgKOTj5vR1Fzm6Y_teYYbptyp66DJIxtg3JzsSl1B4iBG68iEc0LGTeJQR9WTPQenmwoRWwMlOnADhSYrr4hOWJ0-SYkM6wGwtpqa7GzDvmv3HaGLbQObtjWYnL2-8tarLTON8v2uBXhnF_qtdPO6Yw-Fwf-YLYVkSNh34XLl6PecNAW-446wRLQ-pakn6l4eM8Vzc04NQ8BqN_haSN8ooAKs2ksqWXzK5oSb7Lr4AikFGHfl9QSGG2VFGdCLxzh9N-ssi70c10hE2PIQiE3vhLC6fYUyCGOBMjuZIBNDEZHjxRBftrSXgfEcQQuZp8GpldEErFkEAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02de7fa7f.mp4?token=uirMSRVim1pCgKOTj5vR1Fzm6Y_teYYbptyp66DJIxtg3JzsSl1B4iBG68iEc0LGTeJQR9WTPQenmwoRWwMlOnADhSYrr4hOWJ0-SYkM6wGwtpqa7GzDvmv3HaGLbQObtjWYnL2-8tarLTON8v2uBXhnF_qtdPO6Yw-Fwf-YLYVkSNh34XLl6PecNAW-446wRLQ-pakn6l4eM8Vzc04NQ8BqN_haSN8ooAKs2ksqWXzK5oSb7Lr4AikFGHfl9QSGG2VFGdCLxzh9N-ssi70c10hE2PIQiE3vhLC6fYUyCGOBMjuZIBNDEZHjxRBftrSXgfEcQQuZp8GpldEErFkEAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشته‌های آمریکا در یک فهرست جا نشد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/455133" target="_blank">📅 15:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455132">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d050cf1aaa.mp4?token=eO2ybgnaqs4OfLRhs2LhuYofXZwYC8VCj3lv9IcqzBdGzIDjQoR2wNCiWzt6ONRKaSi1di7zxFa4qaBsOkvvjs5MFiPByzH4R7zwEN5THhoyZoFWcnwyZ57-pEB9kkMPdQrux-F5L_IJxarlbSen1FBlkD1LFaYbtybyNvydh1Pec0xWg-IbovlZ8k3e1ECRmZokHAv1cCI_qh0kBjw_dvC3PWBam501Ce2KBE7XeVOvGdD47m4UTHGIugSAWuQJij0apwHahieqKZs6SWvXVIYSS9xLs2BA7f_cYiIRLOb2WMmmSTbRNAA1G90ryeya_AQjhs60TRk0rHDVQMj1DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d050cf1aaa.mp4?token=eO2ybgnaqs4OfLRhs2LhuYofXZwYC8VCj3lv9IcqzBdGzIDjQoR2wNCiWzt6ONRKaSi1di7zxFa4qaBsOkvvjs5MFiPByzH4R7zwEN5THhoyZoFWcnwyZ57-pEB9kkMPdQrux-F5L_IJxarlbSen1FBlkD1LFaYbtybyNvydh1Pec0xWg-IbovlZ8k3e1ECRmZokHAv1cCI_qh0kBjw_dvC3PWBam501Ce2KBE7XeVOvGdD47m4UTHGIugSAWuQJij0apwHahieqKZs6SWvXVIYSS9xLs2BA7f_cYiIRLOb2WMmmSTbRNAA1G90ryeya_AQjhs60TRk0rHDVQMj1DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فرزند شهید لاریجانی از واکنش پدرش به ردصلاحیتش
🔹
محمدرضا لاریجانی: درباره حوادث ۱۴۰۰ ایشان می‌گفت آبروی هرکس متاعی است که خداوند به او می‌دهد. ما موظفیم وظیفۀ خود را انجام دهیم.
🔹
فردی به ایشان گفته بود حالا که این‌طور شده، اطلاعیه‌ای تند بدهید اما پدرم تاکید کرد من فلان شورا و فلان نهاد را نمی‌بینم، خدا را در نظر می‌گیرم این‌ها اشتباهی هستند و باید تغییر کنند، چرا ما باید پنجه به چهره انقلاب بکشیم؟
🔹
در ماجرای رد صلاحیت، آقای اژه‌ای مردانه ایستاد حکم صادر شد و دست آنهایی که پرونده‌سازی کردند رو شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455132" target="_blank">📅 15:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455131">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJYmRhZUKUE8OXXHzas00q-LcYPwJ4NiJHZiH_SWbOCUan5gL3znzrhL5JUJ79i5O17caUEewDqbSmRqqe8x2kngXEcaWNFW3PYOY1n3ZdY063BaKo48bjG3HNig_WebEvNXVoPjmxqARqFERo1d2YcU4U_Fvy0wvkBGzZZsSQEvXaAqrfCZ_Y8Y2u6Pxj2tK9AnHvX6H4k6kY4agK2dY7HaqGpmKoZlfQa2GDULIV-AmKrXnsgRaU9-yEmb1WXZA41UhsreCc5kINLeLeRuvS2uUBd0YPA4oU8nUiZTc6vRg3d20BONIDInIs0P5S6k6tPikeIsZOblcV0Y2iYk4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای ترامپ به نفت گرینلند باز شد
🔹
همزمان با تهدیدهای تازهٔ ترامپ برای تصرف گرینلند، یک شرکت نفتی آمریکایی بدون دریافت مجوز رسمی، تجهیزات حفاری خود را به سواحل شرقی این جزیره منتقل کرده و برای آغاز عملیات اکتشافی آماده می‌شود.
🔹
شرکت تگزاسی «گرینلند انرژی» قصد دارد با هزینهٔ حدود ۶۰ میلیون دلار ۲ چاه اکتشافی حفر کند؛ این شرکت مدعی است منطقهٔ جیمسون‌لند ممکن است دارای ذخایر نفتی به‌ارزش یک تریلیون دلار باشد.
🔹
دولت گرینلند اما تأکید کرده که هیچ مجوزی برای این عملیات صادر نشده و هرگونه فعالیت اکتشافی باید با تأیید نهادهای مربوطه انجام شود.
🔹
انتقال تجهیزات نفتی در کنار تهدیدهای ترامپ برای سلطه بر گرینلند، نگرانی‌هایی دربارهٔ ارتباط این پروژه با برنامه‌های آمریکا ایجاد کرده؛ موضوعی که مدیر شرکت نفتی آن را رد کرده است.
🔸
گرینلند از سال ۲۰۲۱ صدور مجوزهای جدید نفتی را به‌دلایل زیست‌محیطی متوقف کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/455131" target="_blank">📅 15:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455130">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCGOOJCo5d8utfWEWfvFnZPSF0v4oYxK2OgVFJy514cmTpokyA1FnH3Jy1nKcIhzrYA3JnlKSERvCx0dKHFU705RTozfGMn6GQ0hRAcdwgDB0MHeq1vHlOrXoN4vA_OrSo4_wvO5YRP6X9haHjJtnoExBjAnxLvMms2LmM0ata1qHoYbCG2e-WvYxJCjkPO_YzKYkeXGiUaBFEO8vWicgNjUXQSL-N0EzdG4wJHyascMNAdP4kbu7h7eh_eVz0JLtYlQqG3ry181hsXxzAlzvwXrOpLYhskqgHa64dGTfCCh5GMdPvfJPSEsaFsbFkjHr1N9LKoH65yTW5thaeG-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت مشکوک یک هواپیما در نزدیکی پایگاه آمریکا در جیبوتی
🔹
یک هواپیمای ناشناس و سانحه‌دیده درحال سقوط به‌سمت پایگاه هوایی چابلی در جیبوتی است.
🔹
ساعتی پیش سفارت آمریکا در جیبوتی با ردیابی این هواپیمای سانحه‌دیده از مردم خواست تا اطلاع ثانوی از تردد در اطراف این پایگاه دوری کنند.
🔸
پایگاه هوایی چابلی میزبان ادوات نیروی هوایی آمریکا است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/455130" target="_blank">📅 15:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455129">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrJJagGtIkO3hR_Q_kLEI-IsRoq_sBMzD7Z5_rADh3TJe2D8lgmBCBT4u_qw5dEHf-IZzIRne5c4pbTWqGK-3sHecGNwARD5XLmnv6O_CinE1ij8vVmqGtF48NLHA6njf-emtpJN8_kvSedp3FiDfoA_v74r0blpjY_0sfumO7zlP1mlinepjLpjJlXyLlFY985EbQU3JmreZGsyC7RufM9RWOZjUnsi1UjGKdRHyGM1ulHkeJXk36CAyFXOBiGKy0lCBG58rBQo6KXA3LlgCebwVgGyMB4ZbqQzK8M78HKVz4W-0nN6bCQ7NTneliGNf_kD_aRd5FtvePapGNFftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضاییان در فهرست پرسپولیس جایی ندارد
🔹
در روزهای گذشته شایعاتی دربارهٔ احتمال بازگشت رامین رضاییان به پرسپولیس مطرح شده؛ اما پیگیری‌های فارس نشان می‌دهد این بازیکن در فهرست خرید سرخ‌پوشان قرار ندارد و باشگاه پرسپولیس برنامه‌ای برای جذب او ندارد.
🔹
یکی از دلایل این تصمیم، شرایط پرسپولیس در پست بازی رضاییان است؛ چراکه سرخ‌پوشان در این پست بازیکن در اختیار دارند و نیازی به جذب بازیکن دیگری در این منطقه احساس نمی‌شود.
🔹
همچنین رامین رضاییان با توجه به اینکه بیش از ۳۶ سال سن دارد، در چارچوب سیاست جوان‌گرایی این تیم قرار نمی‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/455129" target="_blank">📅 14:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455128">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcacf87c4c.mp4?token=bQ6e7XRnGH6aAQetYubg_25GH3b9Wwu-SJwJgGKb2aXg8URlhLm7y8jzRzkFkKjmkQqqRvDnF_NwaRnHRtkN94q4T5_qY27itVnIBv8yBrOm2AqT9npov8VrdTkJYa_WD2gbSK7set3FqNXxhLHpVQHgYtjklQMLoGfqV6xsHU-v2h-xnV1hOvl9UYmswdJORrRrTx7w5xfp1fBiS-Y75ZizoHkn5P9ShWmesGEAWAs-jNDtyy0otZFGtWDdDqeCVSiDBcCDWOfvraueYtzyIVnQehvlGWUlpbGulgZXmjC5lHAIP_C-uSbdmlBwOTOx-nYFdkOY40wknBX3F6RrIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcacf87c4c.mp4?token=bQ6e7XRnGH6aAQetYubg_25GH3b9Wwu-SJwJgGKb2aXg8URlhLm7y8jzRzkFkKjmkQqqRvDnF_NwaRnHRtkN94q4T5_qY27itVnIBv8yBrOm2AqT9npov8VrdTkJYa_WD2gbSK7set3FqNXxhLHpVQHgYtjklQMLoGfqV6xsHU-v2h-xnV1hOvl9UYmswdJORrRrTx7w5xfp1fBiS-Y75ZizoHkn5P9ShWmesGEAWAs-jNDtyy0otZFGtWDdDqeCVSiDBcCDWOfvraueYtzyIVnQehvlGWUlpbGulgZXmjC5lHAIP_C-uSbdmlBwOTOx-nYFdkOY40wknBX3F6RrIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دشمن آدم‌هایی را ترور می‌کند که گره‌گشا هستند
🔹
برادران نظامی در سپاه و ارتش کاری کردند کارستان؛ با ایستادن مقابل دو قدرت اتمی دنیا را به حیرت وادار کردند.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/455128" target="_blank">📅 14:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455127">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
رئیس‌جمهور با رهبر معظم انقلاب دربارهٔ مسائل اقتصادی و نظامی کشور دیدار و گفت‌وگو کرد
🔹
پزشکیان همزمان با شروع سومین سال ریاست‌جمهوری با حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای دیدار و گفت‌وگو کرد.
🔹
در این دیدار به‌تفصیل دربارهٔ مسائل و مشکلات کشور به‌ویژه تأمین نیازهای معیشتی مردم، شرایط موجود جنگ تحمیلی سوم و آیندهٔ پیش‌رو، تحولات حوزهٔ نظامی، راهکارهای ناظر به تأمین منابع و مدیریت مصارف «ریالی، ارزی و انرژی» و همچنین تعامل اقتصادی با طرف‌های خارجی تبادل نظر شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/455127" target="_blank">📅 14:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455126">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آزمون وکالت ۱۴۰۵ اواسط آبان برگزار می‌شود
🔹
رئیس کانون وکلای دادگستری مرکز: طبق قانون، کانون وکلا مکلف است سالانه یک آزمون برگزار کند و آزمون وکالت سال ۱۴۰۵، ان‌شاءالله در اواسط آبان برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/455126" target="_blank">📅 13:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455119">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNTjjI35JUytUVUuEHS5iGIBFMfppoGq2NzZx2pSEx1akgcuwEez5BiJLbJB-FVmfqwuDhfHkW8sbZGYJBCwYA8PQDM23ARgrEL1KwPm8l6KDrz67ZSEX6qizJ3ZM115qAS6KT9XPE14qssFoAf4EXkNIM8gCcY2jdRrXsBz8qsVE0DwvPSc5iYldlHxdguxQFkg3UGdzPgrS2k8_JpuJzOceC7WqZ3S9pqTcujCQmOpdNCPqUsF7VbXSfeXQ9V1lFzxFu-eYsJpQosfV6RDYKntnM1XbIFMLuY8QM7J4qhtx-EQ55uX6SM6zsZUsLYcJXwmsz6bXCt-OWz1ubGgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSxvaCVd_CXx_LUxilf3ldD_NZRfWqQYvZtcIUgqvX13X-G7ujME8MwU3tWG0OgUkEbdlMv07Qg1HWzGIiDkYdFKzRqXrowFOfgBmJvDeDMJEY21o48uR2eu-gktW6AMEDv9fpbv7KpCfkt_bI3ND3kwvu0ATQPEduG5BAiSwQW74zr-qeeQb5LOhqfdxkPsD6shwaJ1gGwBM4TCr21wgmyqiJ4v5Vg7Sy3W5Vv7Wv8fxR5aw1eMhNXDouIby66rCm2Cc2Xok56FOgdgmzn80GmjJTPMNjOGaE-smHaTLvMhKMcRGlSOJTXsapfdj1aCgqr1dis17HhzPM713JxWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHZYhX5BjCpjdkL7f-cTkPpnHaZ7Uh6aUMN59TG5NswVOtTxnRd5n2oB-HQgv4MIHD_DX9PqxZDvy2JUkHQ0WoVMEFZrloybSF3eBNm8vmkmxtovt9wONV2P-NnzsRkHxQdCDOhWoyNlw0wMX44G8jyCac_z9yeab7Zghu7eSrxZO3uH_vmde0PgB6FHQDnsSymhgFVQcJN_s13QFi-cwb_tpBgAClRApGJ7Q0eF5jLS0hmVg9lPEIwWwXtIQVbc_Sb9n6bT2IMCHxAvRXcB96xWxUQwlPuOzzjAV-efEepZzbt6uA2Vb76-slZssu3cQHkvLeH6ujYzUlL3aPS1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwN-JQioQ4VBtXT1GyvXy0pF3meb3mYottX-mg1eIvL8LfuXtAkyd0hQFxyZBR8-AkgZ_UGLfp8qlSorHgB4b0WmwEMt7UbdYN0l_2ikYKFjuyyb2TkbpCwanoLp1M6ixzkL_aBSIhsBPGZgyK_GE_pxyBgNyMN9roneyeO3sZIuAkwxeDb8v4hTHH0D-p1xVBWZj2pBo8HJsvCOBC-c1kLhgEKCHfM7HfoEZW5D2qSsYizBojtTYaYpw_AhALOcC6PrfPNbzx6noxBa08ry148GZstVsUeF2km4s7BMCa9f73rOIWl9rebrlpVVGw_8FadGMCklMlmCyUdu7JatdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KXQqVIN2zwaa9Y39Kg7Gc9jPkDATDymzH3ykQKZ7wYXj7S_bKlM5-8X9x132iXcxkz5rrCG75CH0i8qqiTJ59pcs5Jy4MvdYekQU-iOHTV73oTTy486PcA3yJRwS7D3QUNcHGkOloUlr30AojI9O2B9CafWj5LHj93Xl1zEbzNvKzMKelj7P9T2nlZZoV4dK6RgTxGiMJ4dhQAuIdIRNpxjrusAYbtMwvDfmNbwSPDk20hHQwAe4VE_5uV5mTTgYxm2U1Qq0NeP-jc2RZyCq8Yj7r_e5WDzzdIK5Y_UiEljhwJxrTL6hpQFNlkMIDAP2uScCtMVmw644yJEEBs3mOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/siXGLk3T5ajC7cKIWZYA42pX2yyAznqEFhxqhO1qrbYsBPlKSQhihV7E-iJF3xeLdPeQqYhTxupxdPqOMNTh-cpeSkPYOO3K8pkMNomIjFw-laYLnq_djizb5u30b7yo9l-tKiLqNWvHzMWQhaaR_lGNsxEjflo7Jr486pTG6ToWiM_vsHw76v0b_zI0UkeMyRtVRcwhlwBsGvCf-CKl4RodTFuZ01Dk3ykEUBZtj8pBEOETZzQp6S-Oq2JRwYIAYi0Kpk6bimt06dtQuf0s2pE5l0L7OC8QUGsAhBWTFRXKGldxR8L3ltI1hRWElDfV87AUjYfakyze7j8guzRd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AngV0Uqcg48LbMpg_ZmTHxvS1jg7377AnC3fL8PWU75MmpvO1epHqsArvwrVuHhH680P1Cf8WfgkSJ1_Gl8TbJpRXeYTtflN2Qcqv3K1JdoO5xCeFXqTBYPfbrHva2WMoM2lj9GO7zvk9fHbpzXALHcH7C0ult8NVkpQ-NklDUa5pL7ITMJcOjY827Wi-v3hslBbCBXyU6nczMOufiQJWmaTnbB-kYuQktvMCjQuYQWGdF8Dp3g_o9cVDN1K_gu3XO1j5YVgOg_0OpoO9nEMTYIEBHTG1Z-6ytWkHaOHhhkxi9xadCOzVCIVfqyLuWARLmGQzBIWalcP9aUEDQyZww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم محرم و عاشورا در آینهٔ اسناد وزارت خارجه
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/455119" target="_blank">📅 13:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455118">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmKWaigs_Ve47epQaXPhMtmXM6UJby0uVKT1i5eSzJCA6Az1nncvAtGyGngIrgsZtUN21Qor9sxOlI5eZ2cRsLJeOB_MUN1OvgDQPpyfoLwsHtIjwzgg24sggmx8BEuYAI8X8YJ-EmgekcHgrV0RuDPTfsMthBktZC9WtOyFTzKgzVlQrAyOj9WBk5-o4bC0FR0wQHuj8aQIjoBmQfVButLYGG1KFdKrqmfdU2RUC9LIfEvChTpvLi9ucqaMJP3FFd1U3TbF7Ysc52Gq4tvw4FDQwshXMK1bPOhyL04yvuPNm_u483Ec8P5YT8avQmRvAtjAOwPDn63qmU1bBs13RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نجات لنج حامل ۵۰۰ تن برنج از غرق‌شدن در بندرلنگه
🔹
یک موتورلنج باری حامل ۵۰۰ تن برنج که از کراچی به مقصد بندرلنگه در حرکت بود، در مسیر دچار آبگرفتگی شد، اما با وجود حادثه توانست خود را به بندرلنگه برساند.
🔹
پس از پهلوگیری، تیم امداد و نجات دریایی با تخلیهٔ آب ورودی، سبک‌سازی شناور و تخلیهٔ بخشی از محموله، از غرق‌شدن لنج جلوگیری کرد و شناور در اسکله مهار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/455118" target="_blank">📅 13:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455117">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcb47fdfd.mp4?token=jaIpdSbNwDHc0MLDU5WgkNYWO4SVjj3a_ScnjwLwxo9uBrF1qDcYC7enRboFqybPhMdLxRjWsWbS_g9LFkBP1GWZrX3hdyuN-Ss9VuKhgkh-_OGX-fePjLueCAUySQE1BmKi8IzDCBeCgHcPYNpP2LOobN1PjQNqhGK_a-pbmZPpgU-nhpW3kuEYtsugAgV-dZ-uqdjRqiaLhCsQiUFgNoBEQXBlpxFsAQv3zvbgfY-q4u73W8QUnOdVpCEdA39s_6A1yT6efanIjrP_X4BMnyiUzLM2ZPWq2J2hCupjuVqc1Vl-FqJxceTbfvzVoPeG4JxTOHSdohySwv32ctyyZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcb47fdfd.mp4?token=jaIpdSbNwDHc0MLDU5WgkNYWO4SVjj3a_ScnjwLwxo9uBrF1qDcYC7enRboFqybPhMdLxRjWsWbS_g9LFkBP1GWZrX3hdyuN-Ss9VuKhgkh-_OGX-fePjLueCAUySQE1BmKi8IzDCBeCgHcPYNpP2LOobN1PjQNqhGK_a-pbmZPpgU-nhpW3kuEYtsugAgV-dZ-uqdjRqiaLhCsQiUFgNoBEQXBlpxFsAQv3zvbgfY-q4u73W8QUnOdVpCEdA39s_6A1yT6efanIjrP_X4BMnyiUzLM2ZPWq2J2hCupjuVqc1Vl-FqJxceTbfvzVoPeG4JxTOHSdohySwv32ctyyZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی زمینی ارتش: پای نظامی آمریکایی به ایران باز شود آن را قطع می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455117" target="_blank">📅 13:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455116">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حملات مجدد انصارالله به مواضع مزدوران در بندر المخا
🔹
رسانه‌های یمنی از حملات مجدد انصارالله یمن به بندر المخا که تحت‌تصرف ائتلاف مزدوران سعودی است، خبر دادند.
🔹
بندر المخا به‌دلیل موقعیتش در ساحل غربی یمن و نزدیک‌بودن به باب‌المندب، اهمیت ویژه‌ای دارد.
🔸
پیش‌تر…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/455116" target="_blank">📅 13:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455115">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItRMP9lhoTpzewA6zdBlm049EK9qq6ohiDl4H-ZoR22kgNQUAljG1tpQfVs_LzWjLHKmIOTLhMSLhTiL8YSt97Bm-RyuJDh1IsG_J0mtGxfCuzhKzvuMvpYOY0bwIeoH_btAFHE-_IcpsskOY-NASUQ3HceWl0Oj3Ewbub2uLLv5ETWn3v8YryrLTAS5e9Ka5h0BtjhWXjvMQpxX2kfS64pUPVdkVzgrb4zVx4zTRfpAwJKYYYBY3LquqLa3zmG1BNn5H0T7WHtor4WDrq9Zfy-d_cW-D_g25YWdvLsjSIAlN1MNk8OaDxVT1L4DJqT3Y7m3V7eYPDzCxiY2pU6aKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک جانباز حملهٔ آمریکا به جنوب کرمان
🔹
ایمان انوری از پرسنل فرودگاه جیرفت، که درپی حملهٔ جنایتکارانه دشمن به سایت راداری جبالبارز در جنوب کرمان مجروح شده بود، سرانجام به درجهٔ رفیع شهادت نائل آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/455115" target="_blank">📅 13:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455114">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حملات مجدد انصارالله به مواضع مزدوران در بندر المخا
🔹
رسانه‌های یمنی از حملات مجدد انصارالله یمن به بندر المخا که تحت‌تصرف ائتلاف مزدوران سعودی است، خبر دادند.
🔹
بندر المخا به‌دلیل موقعیتش در ساحل غربی یمن و نزدیک‌بودن به باب‌المندب، اهمیت ویژه‌ای دارد.
🔸
پیش‌تر یک منبع یمنی به المیادین گفته بود: صنعا این معادلهٔ جدید را در داخل خاک یمن إعمال کرده که هرگونه حضور نظامی یا تحرک نیروهای سعودی به‌سمت یمن و بالعکس، بلافاصله هدف قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455114" target="_blank">📅 13:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455113">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfS__wTKL2nzEQodJKwdRV4juyrpdXMxA3iFinjQzqJ5Z-jA-kKG41X9v69wQ72cLAh5z0PLdcgr-gEvzES6PJrJnATfSCR85pCmtDcWN0SrbX835DOYuq5IQa9GYHVy_5L7GbFJvFTSx_tHeHDnM4uvf1qm0nQrzRwcPwV4fTsI1NSlRCvGSA5D2sM1Wp7z0jhmQy2WVZYpwKLGDyK4TaCL7KtjqnjiU3GJdZlNcUBL-KCUigTQYyBLx04Fzck0hhwsSEMUWeDBnKDWSUkVRbhi6423PuJuFyKyjwCuRLE8gUlSNAMNktwcKPMjWJoUZ8Zzq4x5jMBVJ3GpnW5pSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: کالاهای اساسی را برای دهک‌های پایین جامعه با تخفیف ۵۰ درصدی عرضه می‌کنیم
🔹
شهردار تهران: یکی از اقدامات مهمی که شهرداری تهران به‌دنبال عملیاتی‌کردن آن است، ارائهٔ تخفیف ۳۰ تا ۵۰ درصدی در کالاهای اساسی به دهک‌های پایین جامعه است.
🔹
در نخستین گام به‌دنبال تأمین ۱۰۰ قلم کالای اساسی برای شش‌ماههٔ دوم سال هستیم که این رقم معادل ۵۰ درصد از ظرفیت کل سال خواهد بود.
🔹
شهرداری تهران علاوه بر ظرفیت‌سازی برای خرید کارکنان نیروهای مسلح از فروشگاه‌های شهروند با حکمت‌کارت، این آمادگی را دارد که خدمات جدیدی را برای این عزیزان در مجموعه‌های مختلف شهرداری تعریف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455113" target="_blank">📅 13:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455112">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp7B-97oY_eWRDoAvyyzdYmYDdD5UIfHf4BOD7crW_j_JFsAvL4dXlGq_vL5qSFN3F5oUxcpVm6liGq9Z7j_huJQvtakvKhiYy7r7eUwNXHi2q3OrhtKQIO_CQE3f-1WLxnoTzeGB2PJ6S_CB8aec91J9sT-H1lwUb0aW_lWG8T-PWRcsrZHLdbmOurPSeNx5ZeDEWsv2BoQ9YS58RHU8si_U2lGGyQTFoT7vquTkqG9vvCsXb-lyd6lVoFEX3oS8TcSyho05fxLba0AISBe1IHLWEvqRw57br_tvVZWjKi-Q9x0F_EYyVtI_EPHx061gkZy74NqpERLbevmFZcXaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود ۱۲۵ اتوبوس‌ ۱۸ و ۲۶ متری برقی به تهران تا شهریور
🔹
معاون حمل‌ونقل شهردار تهران: قرارداد تأمین ۷۵ اتوبوس ۲۶ متری و ۵۰ اتوبوس ۱۸ متری برای ناوگان اتوبوسرانی پایتخت نهایی شده.
🔹
در صورت تأمین نقدینگی، پیش‌بینی می‌شود تا شهریور ناوگان به حمل‌ونقل عمومی اضافه شوند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455112" target="_blank">📅 13:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455111">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaYzhYa_tlS7JDaJL_0LztGr0VZfUxwde_RldBQ6u86EpOc18Rb7lG-1tJItdASXeKlP-d_GbQzX-QVlQCSRC_3x6IcHMr77HNQJwJBVB91Kur3mP8VJFGZWFgucUsDfepK2zPdX8BML8gwczOLDFAy6kN_0jQzAoqSfnzOtYcvKe-vhtdUJ-lpd2SuqLYUJQX1zebq8DS3xqacZxW6KVRxsuxHuXtT2fJfIvRHj23fz4DCCHEvqq7LBBoGnLOLdEd0La1QyqHuP3ZpOsaIHB19GproML6Qv8mt4Cx6bN-ua0X9-JWfFzU3tcZEgpuk5OipcZwtLXiqFOqYToUe4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۴۰ هزار واحدی به ۵ میلیون و ۵۶۰ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/455111" target="_blank">📅 12:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455109">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11c9456f6.mp4?token=emF8xPRYHQHjoFtzT8BrHsyFAYOZpyHrxbdKneSu4nRZ3enES0HHM7GNxp2p5CZEuyW0j65IC-hfBHKF7r2CloCecmgNllm_mt0eTxNYHn6sOJpASEPAmCcQWUXcVX3Jc1ugvKLg8kisauLxQtevqjdDLrjbtOxcJIrWyxem_Vwyp3cBY7w6lPlvIBn-u__Wjm7YvMam_CSE9HLAp04w2j6iM-VAYsN5wmgf-4Ov9bNVpICx2RALo5_1vxZH04rwEavsd7uElnHpP1eFjp73cN7CCC4b6jQoIRk7qi_Q0N_OvUGNQMYDS0HLkS9BtTWmJkKgTVm4GCQcYKCnDG-6lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11c9456f6.mp4?token=emF8xPRYHQHjoFtzT8BrHsyFAYOZpyHrxbdKneSu4nRZ3enES0HHM7GNxp2p5CZEuyW0j65IC-hfBHKF7r2CloCecmgNllm_mt0eTxNYHn6sOJpASEPAmCcQWUXcVX3Jc1ugvKLg8kisauLxQtevqjdDLrjbtOxcJIrWyxem_Vwyp3cBY7w6lPlvIBn-u__Wjm7YvMam_CSE9HLAp04w2j6iM-VAYsN5wmgf-4Ov9bNVpICx2RALo5_1vxZH04rwEavsd7uElnHpP1eFjp73cN7CCC4b6jQoIRk7qi_Q0N_OvUGNQMYDS0HLkS9BtTWmJkKgTVm4GCQcYKCnDG-6lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس فدراسیون فوتبال: در همهٔ بخش‌های فوتبال باید از هوش مصنوعی استفاده کنیم
🔹
تمام کارهایی که برای داوری و VAR انجام دادیم توسط متخصصان ایرانی انجام شده است.
🔹
سامانه فنی هوش مصنوعی ما برای داوری‌ توسط متخصصان ایرانی صورت گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/455109" target="_blank">📅 12:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455108">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/591ff6e1cf.mp4?token=pEnfq-jjeJX0W847Gdo71z-OqwV9dZSNmZxC8FAZ6BaB2u92GFTg2IDb_sottW34SaNSE9fGZOaclUlW78SQTZ0_wzfUFdzGq8o6s57mTDusjI7jqYfD2yc1j1NX73sFaZlRzvxYN3GRlp2twGUfSWa6UNK82kkwgJ-G3vlv9yNdXOehFLGcLD9B2V8rP8_GvuxsoyZJFL3zVTJKP1F9SYwCsxZ_q5VhEL79XZSt-vzqMn6vVC4ccRnTSvNlkb-3WgTtv8N-VVwoZMl5cjb0QV5Hvmb-F4y5VxDgGybKlZn8A3MSDoooiQNXsbYwCUGyeR-yO2GI7k7u2irCyWLIvTug3xrBj2D7YVyFmymcmHHCvugucp2MLh1q5mLDS78jiNaiPcnk4oGABArVwdJahinkvYlj7_9VittZnq2nWCuEuJBhIfS10B3oE7ZW88ZXONS94gsqY8MrAbVuC5zyWT6n6suf4zhth14k6bb8WNw3N2BoPdxmq25y6dCu16QwmeOE3lQ9O9Xq81VrzgYq9-1tjBQeqVzpaxFlw1XRoveqeqXWJGX3VvNW9LuGpRhI7aYFdfcQ3QVxtdTD9UgQ2SAV1d5OYQk4q5SOICEbNm2sIeL1at5aMUTHa7_QPd9IVf_B-lYI_ejOT0cF_oYbzOpwVU3UstTX-_aooPOZ7iE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/591ff6e1cf.mp4?token=pEnfq-jjeJX0W847Gdo71z-OqwV9dZSNmZxC8FAZ6BaB2u92GFTg2IDb_sottW34SaNSE9fGZOaclUlW78SQTZ0_wzfUFdzGq8o6s57mTDusjI7jqYfD2yc1j1NX73sFaZlRzvxYN3GRlp2twGUfSWa6UNK82kkwgJ-G3vlv9yNdXOehFLGcLD9B2V8rP8_GvuxsoyZJFL3zVTJKP1F9SYwCsxZ_q5VhEL79XZSt-vzqMn6vVC4ccRnTSvNlkb-3WgTtv8N-VVwoZMl5cjb0QV5Hvmb-F4y5VxDgGybKlZn8A3MSDoooiQNXsbYwCUGyeR-yO2GI7k7u2irCyWLIvTug3xrBj2D7YVyFmymcmHHCvugucp2MLh1q5mLDS78jiNaiPcnk4oGABArVwdJahinkvYlj7_9VittZnq2nWCuEuJBhIfS10B3oE7ZW88ZXONS94gsqY8MrAbVuC5zyWT6n6suf4zhth14k6bb8WNw3N2BoPdxmq25y6dCu16QwmeOE3lQ9O9Xq81VrzgYq9-1tjBQeqVzpaxFlw1XRoveqeqXWJGX3VvNW9LuGpRhI7aYFdfcQ3QVxtdTD9UgQ2SAV1d5OYQk4q5SOICEbNm2sIeL1at5aMUTHa7_QPd9IVf_B-lYI_ejOT0cF_oYbzOpwVU3UstTX-_aooPOZ7iE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس فدراسیون فوتبال: در همهٔ بخش‌های فوتبال باید از هوش مصنوعی استفاده کنیم
🔹
تمام کارهایی که برای داوری و VAR انجام دادیم توسط متخصصان ایرانی انجام شده است.
🔹
سامانه فنی هوش مصنوعی ما برای داوری‌ توسط متخصصان ایرانی صورت گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455108" target="_blank">📅 12:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455107">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bc7ea0515.mp4?token=NChukZJEEzwhXVdVitW2ZGX-H3SdEGb4fNFq6WNF9T5BntIWzQAEaggdEq4UEKXEPRYNVlZgcM5eZeGmyyo2gZx2rwAAzGBcUZkr88jpqOALImobWEzKd8md8I_ZxLVMqBK8zvk_lrGgCEqlpxWqF3Nf1WgVSJdi_pYL6LpcgZh7FnR988TQrNusFQ0dEMQ9sD9lbFcy7hKgJZktphHcMpwZSwDyKN0TmbPoEzdn_Y451nk5WLD8OJNV5FA11DMk6z7M4a7iVMPIqfEL3QL3xnDK9NDw9_KFdzAE1sReNH2J7da0_WMJrRbECRcMxu_S966CyAGlNNsB2lyMh9y1lSU0DMg-0HZOLR14aJqKbQrwAXXMnfefvRkgmty4yIHfApHHdgprOGapVe1Kvqi72Go3ycCLaAQURw0EoVxR4s6UhWB_qiilru5YJW94gPIaVLKLtjXIl0HssIyRGPqNQwjrALppE9UDAmrMBebE3Yx05gcAgCMDDZYVx4IQvNJ1EK2azmHnt1y93gR3zcinNRhQ-U1LlhrYwwDyoWRn3KPU0OF_vsy1f4TMSFiBvse4lpGwh5QqztXpzZeSNiMfDraFsXkIb5s5xhJkBFZ9Xlquwr1bmAZOj-MtaYpNfjDeY_l6YxpVO_kp_VEwobjsMEKhNC6lbGGHmoEl1BqwTi8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bc7ea0515.mp4?token=NChukZJEEzwhXVdVitW2ZGX-H3SdEGb4fNFq6WNF9T5BntIWzQAEaggdEq4UEKXEPRYNVlZgcM5eZeGmyyo2gZx2rwAAzGBcUZkr88jpqOALImobWEzKd8md8I_ZxLVMqBK8zvk_lrGgCEqlpxWqF3Nf1WgVSJdi_pYL6LpcgZh7FnR988TQrNusFQ0dEMQ9sD9lbFcy7hKgJZktphHcMpwZSwDyKN0TmbPoEzdn_Y451nk5WLD8OJNV5FA11DMk6z7M4a7iVMPIqfEL3QL3xnDK9NDw9_KFdzAE1sReNH2J7da0_WMJrRbECRcMxu_S966CyAGlNNsB2lyMh9y1lSU0DMg-0HZOLR14aJqKbQrwAXXMnfefvRkgmty4yIHfApHHdgprOGapVe1Kvqi72Go3ycCLaAQURw0EoVxR4s6UhWB_qiilru5YJW94gPIaVLKLtjXIl0HssIyRGPqNQwjrALppE9UDAmrMBebE3Yx05gcAgCMDDZYVx4IQvNJ1EK2azmHnt1y93gR3zcinNRhQ-U1LlhrYwwDyoWRn3KPU0OF_vsy1f4TMSFiBvse4lpGwh5QqztXpzZeSNiMfDraFsXkIb5s5xhJkBFZ9Xlquwr1bmAZOj-MtaYpNfjDeY_l6YxpVO_kp_VEwobjsMEKhNC6lbGGHmoEl1BqwTi8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرعلی جداوی، دومین جاویدالاثر مدرسهٔ میناب
🔸
علت اینکه تا به الان اسمی از این شهید منتشر نشده بود، درخواست پدر او برای باخبرنشدن مادر باردارش بود.   @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/455107" target="_blank">📅 12:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455106">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMFEMCJ-oReBPm4yqtX5UjvKjStOV37oxrd3HzZjUGQaU5RPO8Mof8oNIqWdB9Edb5ogt7S9TL6Ut4vjq0WaWHzvSpmnDrlEiNC54wYlanqyArQG7HebfAxCVRefltNOYzDTaBZOG-6sOj88xqMefDm1kjKrAY4V1MATm7UBBXfr2-KSSFn2pcVveBjXmfMw7LxH8N4ULEWiNddAdsHOeXSjr_QrxZgYRqoSLrC5RWkOcyYv1Wkf9xVKzUFYfSJ3KWdVu4svs6BHjLwBJETgB2i8d8aVVQqKcfqmVl9sYZ2-xwQsPPgXyI5R_ijFzbVtBArCJa3WYktJ5L1K0KTONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخانیات پای ثابت ۴۰ درصد سرطان‌ها در مردان ایرانی
🔹
معاون بهداشت وزیر بهداشت اعلام کرده ۴۰ درصد سرطان‌ها در مردان و ۲۱ درصد سرطان‌ها در زنان ایرانی با عوامل شناخته‌شده‌ای مانند مصرف سیگار، قلیان، تریاک و چاقی ارتباط دارد.
🔹
دود سیگار، قلیان و ویپ بیش‌از ۷ هزار مادهٔ شیمیایی دارد که دست‌کم ۷۰ مورد آنها سرطان‌زا هستند؛ قلیان هم برخلاف تصور رایج، گزینه‌ای کم‌خطرتر از سیگار محسوب نمی‌شود.
🔹
از سوی دیگر، مصرف دخانیات در میان جوانان روند نگران‌کننده‌ای دارد؛ در گروه سنی ۱۸ تا ۲۴ سال، مصرف دخانیات در زنان ۹۰ درصد و در مردان ۳۴ درصد افزایش یافته است.
🔹
پیامد این روند، سالانه حدود ۵۰ هزار و ۵۰۰ مرگ و نزدیک به ۵۰ همت هزینه برای سلامت و اقتصاد کشور است؛ درحالی‌که متخصصان، دخانیات را یکی از عوامل اصلی بروز سرطان، سکتهٔ قلبی و سکتهٔ مغزی می‌دانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/455106" target="_blank">📅 12:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455105">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxzdU5WCsJu8N1zsbhRY2EtZnDggFXgOnC4MO8Ag_rYX-QlhL8F84T4e9POkH5OQseW12WTHYD5Bf1KzDsJqyuF8yLD1L-QgyOU7CAyIIgEnzYSbCp475_qoZDjIczd3Zxcy5cRB_GcwoNeLjZQEXGOtIDsomGB2sPIhHGPmGTF-JDO7vVZTpJgshZ3HSrfccpfGDcRRhn_cteU9k7JMiuuJtdx2ujYVsdAoqFtXYCV_ks3laAJogdww3W7VFk2Qo-i1HBR5Gi8HnhWmk1pikUUZmk_p1W1ZIeHeDZ76Sn2oqOekOkrHHE4VaMt-wvtM4j8Yzt_8XRYdcBLt8CtpmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
موافقت صندوق توسعه ملی با پرداخت تسهیلات ارزی به صنایع آسیب دیده از جنگ با عاملیت "بانک شهر"
◀️
مهدی غضنفری رئیس هیات عامل صندوق توسعه ملی:
◀️
صندوق توسعه ملی با پرداخت تسهیلات ارزی برای بازسازی برخی صنایع آسیب دیده از جنگ تحمیلی اخیر موافقت کرده است.
◀️
با توجه به درخواست های اخیر برای بازسازی صنایع آسیب‌دیده، صندوق با درخواست پرداخت تسهیلات ارزی از سوی  بانک های شهر و تجارت که عاملیت بازسازی را بر عهده دارند، موافقت کرده است.</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/455105" target="_blank">📅 11:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455104">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmMTAXdbfahif8OM9U46xr-urq8jby4z4raQjGGRSGtBb2SH0x-YjkQQ-17a3scpw8UtCAnTOnSRbuzdPCDVFpFEiHFOachv2kE5nZEfTODHMYEDwPl1oNwcrKraDH9yJxP-t7-duu7z2aV8eDTx2ActgGMGIiKLHOF5SeAb8zUMEtQJc3X2daLiSTOjkyCoXaDjwEgoc4KlICVPYefeAGgSvckQW7Sg72MAiuoeJIXIzkh8YcFWRFbbl4Te9mK38RkckhdCZFPVLv4dsz_ifAerMZlnKUTLLS8hmlnbH0jJdoKEyfQTgnIBH8VyNbk-mIGj9Cs-Upc2YP-fhxoEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه حال خوب بساز...
💦
مرداد، قراره هر بار که به پارک آبی اُپارک میای، یه تجربه متفاوت منتظرت باشه
😍
از بازی‌های گروهی و لحظه‌های پرهیجان کنار دوستات گرفته تا هدیه بلیت آنلاین و برنامه‌های ویژه‌ای که فقط در مرداد تجربه‌شون می‌کنی؛
اگر دنبال هیجان، تفریح و ساختن خاطره‌های خوب هستی، این ماه بهترین فرصت برای اومدن به اُپارکه
🎉
🎟
برای تهیه بلیت، همین حالا وارد سایت شو</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/455104" target="_blank">📅 11:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455103">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/455103" target="_blank">📅 11:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455102">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0jylYTTeZ36BjL_8E9fjViyWimY2t-1XxEO7glKo7RQZ_sCe0Qb-uKbMbQWMGVHxCIQ7vi5nH19Ef8eOtT5WkG-0N5B2aepFJMoD9ZDpoEYgwTIjm9UAaBMu8QrN7nKQqgZ4TA_E7wW85fgZxRCu0nxfCD_w2ilZFdKW7OKkEz0nnOG2TdpLGVvcCqYXqw3fJXwUtsyHJt1FnzsNpZH1HgxX47TqlB51K0QmtfDjnWEgcfVrFradCxDOfOYNffV8M-4FGP2Y0-qUac5wLKN8B6dftMAqWpnXphqgKgKhxTm5z588XmCcESQtkg-yuMlKq6cckBF8eNqZZX2pPYZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: تا آمریکا رفتارش را تصحیح نکند، تنگهٔ هرمز باز نخواهد شد.   @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/455102" target="_blank">📅 11:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455101">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌ سخنگوی پلیس: نفر اصلی دخیل در قتل حمیدرضا رجب‌زاده دستگیر شد.  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/455101" target="_blank">📅 11:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455100">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">متهم متواری مخل نظام ارزی کشور در پیرانشهر دستگیر شد
🔹
دادگستری آذربایجان غربی: یک متهم متواری که تعهدات ارزی خود به میزان ۵۱ میلیون یورو (معادل ۱۰ همت) را رفع تعهد نکرده بود در پیرانشهر دستگیر و با صدور قرار تامین کیفری به زندان معرفی شد.
🔹
علاوه‌بر موضوع عدم رفع تعهدات ارزی پرونده فرار مالیاتی به مبلغ ۲ همت نیز برای متهم تشکیل و در فرآیند قضایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/455100" target="_blank">📅 11:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455098">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎥
معاون امنیتی وزیر کشور:  ابعاد مختلف قتل آقای رجب‌زاده در دست بررسی است و نتیجه در اولین فرصت اطلاع‌رسانی خواهد شد  @Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/455098" target="_blank">📅 11:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455096">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niVf7A9hb4qujCeHRJjyQIlFx0paZoKjvKiv3T6FqhUOIW5DG5TCjcaNaYIvRLB1kCuC6PT8uSFJzkLyX53T2h3gHZ_d4uP1Iv4nJ2G9XEoC63DUFM8PAtcdgD0DATc2jS4oKK0CsAIffJoSz4n98nNlQ85iKfvc9c65OEw9zNte0aBDOd1cjRCEl_gszMrs0ZaljOwCDWZqRYUn-3GE78zUuG98l4SUi-YoT4fCBkiivfwflFOwztcg_iq9m9CKFNfivZuNK7IKWfAnBV9WXj_Zb5kFF5wUzAV8wSnZQP-kJnjUD235B2z3LUGF-l70dWgztY6-_at9UTtTgj9oxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۳۳ سلاح در مرزهای آذربایجان‌غربی
🔹
فرمانده مرزبانی آذربایجان‌غربی: در عملیات‌های یک هفتهٔ اخیر ۳۳ سلاح جنگی و شکاری، تعدادی خشاب و ۱۲۲۹ تیر مهمات کشف و ۱۷ نفر دستگیر شدند.
عکس: مرضیه موسوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/455096" target="_blank">📅 10:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455095">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎥
آتش‌سوزی در کارگاه فندک‌سازی شهرک نصیرآباد تهران
🔹
سخنگوی اورژانس تهران: درپی آتش‌سوزی در کارگاه فندک‌سازی شهرک صنعتی نصیر‌آباد که ساعت ۷:۲۰ امروز رخ داد، تاکنون ۴ نفر مصدوم شده‌اند که از این تعداد ۲ نفر به بیمارستان منتقل شده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/455095" target="_blank">📅 10:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455094">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0FFtn1g5FKn0Pb6RQUBIxh03mKwmBhEvd585pFCY4IrgOOAKuJoGQaTYfWV4p5ItnBrzJVqdB4HOgbbJYihNrOG2fHse7CZLN8D2JCpkVeM7T1STQwAspIEIjjwkzP7yIeTi9dNMP1Yr0f-Wx2B_OqNFw4Wu7W7Qm2iW06JwLWjhw7NtwaLQfm6iz6w_5stkWiHxj3KKbMcP5Mv2IyFATGYdyUZafre-E8o6r9ogfb5XwiN58uovZP-y2lzdfaGFP45iHWa3M7O0cAONl83C86qkxtVIPrEFjFPKfjDk6ep4lMIInS-20mAVmfEgLLFai9ROdHhY2LBsYH--hjTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: با توفیق خداوند پالایشگاه آرامکو در جیزان را با استفاده از پهپاد به‌صورت دقیق هدف قرار دادیم.
🔹
این اقدام در پاسخ به نفوذ پهپادهای دشمن سعودی به حریم هوایی استان‌های صعده و حجه صورت گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/455094" target="_blank">📅 10:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455093">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz0KmcS0Jp59fX--Yjk7sSYf2UtMliLw_raNzT8LQlMHH9I7Sdm-smL9_qWbntguSUPcvp2_yNR_u40FF6KFEzczY-ZvjHN3PbNsv_2Xi0SOtGnMGCyrgKVDWk_-2RLAIuH1qnCTx8VTmrMpBq_32XKLvaWBTGaVhyCHGNShq3ewao2ScoJbY7CyL3neqh1cI-onJQkO5pK2CNCBA3FMWMISfAK6lkHvwwikwGYJDJQo7iAPHOuiDIqQ8YFF_Q9mfRrSsJfvUmgV8lyOfUr0di6U627JU7kEd5bx-WiSuCzMZGPYMN78L300EfW8fU8zcT7gvh4ee25j3vasKq2Vwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پادگان ۰۶ به فضای سبز شهری تبدیل می‌شود
🔹
رئیس ‌شورای‌شهر تهران: قرار است پادگان ۰۶ به‌عنوان فضای سبز شهری مورد استفاده قرار گیرد و درحال‌حاضر برنامه دیگری برای تغییر وضعیت پادگان مطرح نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455093" target="_blank">📅 10:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455092">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIlnGXCx1sgnHAfqVLPNHzyChuqeu-O7tSKZf6yfRbDH2UMa1RLJme4Z8IzxCl9koj7V6PbsMHeLGe3-qiC52tZANP1urKC0RJKirLcuTn8jxnmITCmZu4_n3U7o2jyHS-u4J8y8GFendwCOsPItfZ20CkGc4KtTWeZtLQylerAtZQj96LHiKZkcxJ146VUqImfJ3YK58x4M_nIvWvVly8VrQ1mfxHFSansHWfkIGkVrgjfIMsVIUQ3iytaPDlijYL-uP2RIsz_Qp4l_GBmTgvJbT3dHSKdUW59upZ-ACj1D5Bodd755oyVH2NrLLjp1MJkwButao4vUctxObZSr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام باند بزرگ شکارچیان در چهارمحال‌وبختیاری
🔹
سازمان حفاظت محیط‌زیست: درپی شناسایی مخفیگاه اعضای یک باند بزرگ شکارچیان غیرمجاز در چهارمحال‌وبختیاری، ۴ سلاح شکاری، مقادیر زیادی فشنگ جنگی و شکاری، یک فشنگ‌ساز دستی، ۲ کیلوگرم باروت، یک مین ضدنفر و تعدادی از آثار و بقایای حیات‌وحش شامل موارد تاکسیدرمی‌شده و پوست پازن، قوچ وحشی، گرگ و پرندگان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455092" target="_blank">📅 09:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455091">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAFMfmUExZpPtfloM2pvoOM3f7t2m-K060zsomHo1X4ne9hkLzu7Sl4arOhTcJecUA77yOA732nRkfYOP9Y5Pe5oRzxKTiha7z1_1XYa3UicKiQX9RCBGXC_kK72QNhzptHWl9pPhn3jEc0MqAxLi745E3MN3OBRPP2XPNJx0doBzQG_F4_Kaj8juqUZthsdol8T2ozVBKxt_f4X752eFFmrrIL_YswBsF2KDZpyg7uryf-ljHdwwMr1fV6uyQSwhVu6RkT2SzdTeklKAYeZ6vdUGO_eOaZLPj9TdEsWb86VXJ9ccBJ6zEBRbw_aq_v2wG9MgU61vDp5AsQjeXDWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوک شبانهٔ تراکتور؛ ربیعی رفت و نکونام سرمربی شد
🔹
محمد ربیعی در فاصله ۵ روز تا نخستین دیدار تراکتور در لیگ برتر، از این تیم جدا شد و جواد نکونام هدایت سرخ‌پوشان تبریزی را بر عهده گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455091" target="_blank">📅 09:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455090">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb9d5ae3b.mp4?token=XVGzaJ_81VB_xPsRtpxHjUKKjUgE57pbN7Vw9OdlI_dj9rt8WpYQ9Xh6e3zZvqnoUILqgmJq3nRW5blv4WiMbmK6wo5jX720aZfTP-KvQykwU0W_bM6ytoPD7DWEqIVD9u8eiHUVZDdsw_9cxQ2K5QO88lp5Ni99YYX4NTmza3xca8UJ6uPVZOvZkAGcFzpWWxqms5qfUMeuvnlckhgb9hM94aS61XEMSFoBXd9N3heICST-RgRDWFqi6H4TWQJAek0AZy3DmaeLQkts3A7ad5zjGGp5Ax8P2Lvo2JegnVHUpVUMlvsYrrG16_lPxaGO0InutMZmCGyyHCvtFG7Kyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb9d5ae3b.mp4?token=XVGzaJ_81VB_xPsRtpxHjUKKjUgE57pbN7Vw9OdlI_dj9rt8WpYQ9Xh6e3zZvqnoUILqgmJq3nRW5blv4WiMbmK6wo5jX720aZfTP-KvQykwU0W_bM6ytoPD7DWEqIVD9u8eiHUVZDdsw_9cxQ2K5QO88lp5Ni99YYX4NTmza3xca8UJ6uPVZOvZkAGcFzpWWxqms5qfUMeuvnlckhgb9hM94aS61XEMSFoBXd9N3heICST-RgRDWFqi6H4TWQJAek0AZy3DmaeLQkts3A7ad5zjGGp5Ax8P2Lvo2JegnVHUpVUMlvsYrrG16_lPxaGO0InutMZmCGyyHCvtFG7Kyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در کارگاه فندک‌سازی شهرک نصیرآباد تهران
🔹
سخنگوی اورژانس تهران: درپی آتش‌سوزی در کارگاه فندک‌سازی شهرک صنعتی نصیر‌آباد که ساعت ۷:۲۰ امروز رخ داد، تاکنون ۴ نفر مصدوم شده‌اند که از این تعداد ۲ نفر به بیمارستان منتقل شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/455090" target="_blank">📅 09:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455088">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34b23b31c7.mp4?token=i9PiFW3vNEef1PXmekMOLuHTM48sIkDjmp47z3k3e961P_t__xpMrg2lzHQFh0-Y2-U6foRuKPGeHC2ekLpQRaXAmiHfGlrpTHv0dX9brzKYpmnddforaQoWFAG6CWuwdUFgtVKbdxflG2hoqePz66Ljbtx5lgia841FVuYRj6ZiSuNwttbDMEOWdaBWXwtpDBdFkmeAoXGeJhZLiKtptfIAlyA7tTNwcOaEC-AhGZcndMrF7PDlqdDqaclzurU5fv5hmSjEn9cxCp_bpkGZM6TzBsRsYC9Rmc1ncO4Onk7aHOyPlwGWzirZ0iVu_oz9vWZalVq4CAkUR_yu6PcCHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34b23b31c7.mp4?token=i9PiFW3vNEef1PXmekMOLuHTM48sIkDjmp47z3k3e961P_t__xpMrg2lzHQFh0-Y2-U6foRuKPGeHC2ekLpQRaXAmiHfGlrpTHv0dX9brzKYpmnddforaQoWFAG6CWuwdUFgtVKbdxflG2hoqePz66Ljbtx5lgia841FVuYRj6ZiSuNwttbDMEOWdaBWXwtpDBdFkmeAoXGeJhZLiKtptfIAlyA7tTNwcOaEC-AhGZcndMrF7PDlqdDqaclzurU5fv5hmSjEn9cxCp_bpkGZM6TzBsRsYC9Rmc1ncO4Onk7aHOyPlwGWzirZ0iVu_oz9vWZalVq4CAkUR_yu6PcCHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی‌ها در جنوب لبنان توسط رژیم صهیونیستی
🔹
شبکه المنار لبنان گزارش داد دشمن اسرائیلی ارتفاعات «دیر المزرعه»، «کفر حونه»، «نیحا» و «عین التینه» در جنوب لبنان را به آتش کشیده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455088" target="_blank">📅 09:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455087">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اما هنوز هیچ خانه‌ای تحویل نگرفته‌ام و هیچ مقام مسئولی پاسخگو نیست.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/455087" target="_blank">📅 08:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455086">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6nLSGBgqXUAxPkLtf6hxCYsVfDgHoZadQBOf9RYILhUytJManl1dOVKHn5iKOnkZYop_5k_ZkunVr29dLaqdkkVRXocjq09XCYyLMQLJc93mTkLvFTIdJr0U78f_38s9xbtaCA_bEQ1-kNiIlsk07VE2Z7dtEJwfUzgXuE0ZWbEGWJeBRbNS_kUer-w6gIr3ZPVBGLdkiReV_3MPdrbfhxye_3aMZkxSTtB0xyl_y31omEfb_cfFejkskI3AojMzvEz_Ed9XAT0aVruFQ1Of7QNN2F_ApTEji3W0Me8PwYjkAYGJjfOFwZAiO5z5yySlHsjpeA21S8pCJfzwa_AIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتودرمانی بایدن برای سرطان تهاجمی پروستات
🔹
سخنگوی جو بایدن امروز به شبکه سی‌ان‌ان گفت که «در چارچوب برنامه درمانی سرطان پروستات، رئیس‌جمهور بایدن هم‌اکنون تحت پرتودرمانی و درمان هورمونی قرار دارد». او زمان مشخصی برای طول درمان اعلام نکرد.  @FarsNewsInt …</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/455086" target="_blank">📅 07:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455085">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7mwjZ2eDtjmon7J8-zqb3QQd1_yThQIEb6BPNguQ0zY0kJxUCyCiBrorpoelc3UK-yMCHx7nuaA02wzdj6WeqtIEo7wF-ZOSkXcxEKBDvrCpT7WIu5VwHF8QfWH7ttMJ0QqKBZEkZtjblPUwbYk4CRcQQT9qw-LUi5K41vLz7zJLjFTXcizY_9iZbor2YR9fxuZXRoerEoOEy5MlxNsO5qyVvLbJUJ76rvE4t_lNZWgSHgoh06M76EIBjTkrkBH2siJoTadaWxo1fiySfC1TlOteq-mk5DL6xbYzgVwyvJD9p-ZgM8L1UjPiWBi5_ygckeKh4c91Kfy8b9NpNYeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تاسیسات آرامکوی عربستان منفجر شد
🔹
وزارت انرژی عربستان حمله به تاسیسات آرامکو در منطقه جازان طی بامداد یکشنبه را تایید کرد. طبق منابع عربی چندین انفجار در این تاسیسات گزارش شده است.
🔹
همچنین ماهواره‌های ناسا از انفجار در نیروگاه گازی بری آرامکو واقع در جبیل در شرق عربستان خبر می‌دهند.
🔹
پیش‌تر نیز پالایشگاه جازان آرامکو هدف حمله قرار گرفت و بیش از ۲ هفته می‌سوخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/455085" target="_blank">📅 07:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455084">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">منابع اسرائیلی: ارتش اسرائیل خروج از بخش‌هایی از غزه را بررسی می‌کند
🔹
شبکۀ ۱۲ تلویزیون رژیم صهیونیستی اعلام کرد که نهادهای امنیتی این رژیم موضوع خروج از برخی مواضع تحت کنترل ارتش اسرائیل در نوار غزه و تحویل آنها به نیروهای بین‌المللی را بررسی کرده‌اند.
🔹
یک مقام امنیتی اسرائیلی در گفت‌وگو با شبکۀ ۱۲ مدعی شده است که آمریکا «گزینه‌های زیادی برای اسرائیل باقی نگذاشته» و تل‌آویو را به سمت «مشکلی در غزه» سوق می‌دهد.
🔹
با این حال، این مقام اسرائیلی جزئیاتی دربارۀ نقاطی که احتمال خروج نیروهای اسرائیلی از آنها مطرح شده یا زمان احتمالی اجرای این اقدام ارائه نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/455084" target="_blank">📅 05:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455083">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پنتاگون شرکت‌های آمریکایی را برای تولید مهمات تحت فشار گذاشت
🔹
روزنامۀ واشنگتن‌پست در گزارشی فاش کرد وزارت جنگ آمریکا در پی کاهش شدید ذخایر تسلیحاتی این کشور در جریان جنگ با ایران، به شرکت‌های تسلیحاتی دستور داده است تولید و تحویل سلاح‌های مورد نیاز ارتش را به‌طور چشمگیری افزایش دهند.
🔹
اقدامی که به گفتۀ منابع آمریکایی، نشان می‌دهد واشنگتن برای بازسازی ذخایر مهمات خود با یک چالش جدی صنعتی و مالی مواجه شده است.
🔹
به نوشتۀ واشنگتن‌پست، معاون وزیر جنگ آمریکا در یادداشتی خطاب به مدیران صنایع دفاعی از آنها خواسته است حداکثر ظرف ۲۱ روز برنامه‌های خود را برای تسریع تولید و تحویل تسلیحات ارائه کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/455083" target="_blank">📅 03:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455082">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJt5O1pGvVzQ8BClNMnPk2eMMJHKC0Jawy9_loZrcjmkgwfvRHEF3O6B-BPzVD3hYnUjI6foR7zXLEMo0tTIAM4RANzBObyWjbWLkkBZYsj1VbZUz1PDy5ZkGGZUmBRReSom7uKhYhGASvuH6eK56KW117R2nUa75uTtwDLe09Vb8GDpH2uUWnMo6ckuFjavqjlLtluV2iVN4dxeHmp8yruncjoyev7IeFJHwnCf6iJ_-1VJySOGS447oSBQMfsK6rCxt5Kp3Rk6TWrgO_LK-Q0Why6eCUbgavdv8MsoyxV6LGMYowidBE60Timmt1rjSltupFKvMd-kEAbIoFm-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزلۀ ۴ ریشتری در هفتکل خوزستان
🔹
دقایقی پیش، ساعت ۰۳:۰۸ بامداد، زمین‌لرزه‌ای به بزرگی ۴ ریشتر حوالی هفتکل و ایذه در استان خوزستان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/455082" target="_blank">📅 03:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455081">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joNa6-ZuGWk7SBmbFp6_C0N41c_vQIbtlxo2hSiyqSZ7LWSL0-kOFFLP-2rlYyNZQUX8UfDuNxd6A53s3CrLS11dL0-qAHIujM3Eu3siZsFm8MJiDMDK2arjCVrLoDU5AMv3o-WJoJEP3rASoYKoLk18ndriqlqTCSD6b0swF_i__cINxvj46LX6lEZsiPjRcMb2cIn8wAgv_InuvdIgn4KT7sLKPsJUsGyQ7-ysq8FgQMhpXOSqu80lPkav_Wycua0dLke7mBxnbgUPTxk-okHlryKyPcf8MJoLQhcpCWmDwDN4TVsnbQKQR8DgWNjoZxcZdgNHZmUNyf7qhtM1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه: در مکه علیه ایران ائتلاف نکردیم
🔹
هاکان فیدان، وزیر امور خارجه ترکیه در مصاحبه‌ با خبرگزاری آناتولی گفت که ائتلاف سه‌گانه مکه می‌تواند گسترش یابد و علیه هیچ کشوری از جمله ایران نیست.
🔹
او همچنین تأکید کرد که ایران «هدف» این توافق نیست. فیدان افزود: «آن‌هایی که به کشورهای امضاکننده توافق حمله نکنند، «هدف» این توافق نیستند».
🔹
فیدان همچنین ادعا کرد که مذاکرات درباره این توافق پیش از آغاز جنگ میان ایران با آمریکا و اسرائیل آغاز شده بود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/455081" target="_blank">📅 03:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455076">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fktZx8srXo8xioVYcs4TpdORuEhw0q_ynNTmzAfqEBsdIb7-186U-BPAA_SpxnbV_YgVXq_VlJCxSjxdu2ldJV6_Kr5vhVz_amazdZ50JYOfPQKurw4ur3OyAN0Zq5GsdPrREpLf_L0K0SlBmXEC81dOpI0GQfjkO6ZMtH-TN_I80wduMyHlvTPh5DrKE-rOvtAowC7BZHnMv4N9UsGTjmMSxzC-JXYYudRJK6lz7ZaB_1ZXVIJ5ChZ4BGYa6uImyp-730XXu60iY_IUqqNjmylSAe9tcyLh5RyQfN_tEZugVgXlynVmQdaqbx-8kVUR93FaeH_-d5Y4qCW5Lp4UUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvyPnJNn7CTLxpTkLs7jZxVJne6dQcDVsM3HyvYH1LDoeDXVyzar3Vsu8SW209Ee6TM08Qpjqxc6sitTwoZ7zicA9KO_ILcS9TYPs774cmO7-uVV-coAntX2YaBvuTfiCmeSSCYzNgVdV6rzHJvBLXdoO-c5UDopTGESTbqWDhws_8TDtUdEOw1sz03ELDIjqntR0QmjRyyLEfKTIjU4YKLbHK2GOPvjdIsOtdh1gUu1QzUerwvYMJ2NJe_MK9uusVccJNto8vN6thr1IbIV5oZRL4acroLL1hUQvb3_WDRqw3tSU23KCgONINLJINWltHADan9DimkaxnzinQxWog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YCVFxNr8X8KCunM0R3P7VsMRfRW9GyaivuEJql9QmEF_Xktok1UBzKmnvgxL9d2S-BNSO-3aCHFPX2dnZ_sH9KittkY2YJiW3Vl9oC_rXBqkcXrwsK0c5eK7rtMBa3z5jXUTognv9KFkk-SLPHVOpjrME2vKWXHu9wJBuwMWqRip8qarJkf4h8lO6xRbgWmsatum_U60acdUlEKkQTgR4G8TnSygO7t69vKsDFirkuvVGkJQd4Lg6tniLO8ZL_QWA4Xnzx-25IsBneA9lGxHlRQk3BdYeV8zLJZAg-I_DL5zwoYDyr28YPMNReY2jiaZA65bczqA-ejKMzqxihaJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuUY_3hIR_PQVbcmbdeSxZS4izTytx-gePrcerpTMn3n7ahc7lGOlkyfuCRhtG8Yee24Owf1GfINBXDkCAwsLpHRReE76jBnJlY5RL9a6eBvnLenfCNFNBRiLWkqlT-kWwoAAHkuKj1hN3SjRE846JtIDZf26pF80cpDiFAJFbwPVv3gddMkwXCy2otlggY6T7sE10SxWey9pA2S023nqyNkMAK4lEM9oPum3-syFXSSyCJymIBekPZTRfvQ44UvSXEbG2x23lhbWUwPyvp4JFthNkPnVcQgQGWbIx2RJ9gXr0ZcBiUYY7-Kb3scM9H8qYEk0aKfqWM9gNFK93FhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vm4Go6imW264IjbnAJRQd_ON4bXBIXoqrsg1a1Qa8ZJnqxXtg6I_ZDNyOhkyW44INiQ104HbzZzm5X7abA7mV82ed-OT1YQXGmU9EP9JVwY1dnzKPa7nfSEJH1TsuohZvoZnCZbUIS-ZC4TWlkpQxZ-5jyImufDv1Cr22XiOlNYBwI0Ng3d28jH_JbTDk9KoYL-4Tn4iWH_pxtavhs5baPWZSu2Cc7Scid0KDcFcCkU4rZgoVCUR5NaJLMvSMAAgG1c1i0UwvfSwMNTEmB7078o_rX8IwUdwTLdeOSH1JDvRr0KMsHXQK0k3pY-SxHrQu4yg5phmwFyX6vIcbp2k_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۱۸ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/455076" target="_blank">📅 03:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455066">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o2EM5UNjokTXliXkbAX1z7bvHLYT_-RbCOvsEE9uo4CISJOGClkZExdA_BJ7nvB2S4SDvdUZhqSmPqjgzDafSXjskloTWiNl3ArGK_dwF8FEBFcZts84dGHsa231EsheoGTlkeQZrcxAD9p_O-RperEeVhpKmKiqVT16Xu8aCqwcT_GSj7xdA8E9wZydfWImk0P4cF6SjjXB15WdK8hBspUHDOgRolWka0xKL8Sv71-ozSCsyQgKrFPWoJtYnlMmey_pct5RndC6X2iwlumsZuHbPW0n-Yeo4QJGPwg6UKrMr1deMH4vMJ2a3WHTuCDi_-IogcSSflw_pH3iYJS9Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMmHOY2JrIABhkSpgRD_7gxB5GGW5K7G50HFnkgSEfCoI0hJeiAdtYOOzlW3lWLwfRd3tlobotp6FzePkY_j2PRF_zlyoUGpNt1Hk0M-BCVqbhD66NAlvRJnTMZNu8S8Xg_eyy9LHz-1PqJRY_r1y1Q95CnvWx9aYHAZeTlIWBKjp28TDEpW7nti95Fv1p_ywajWr1oPUDk-ISxQi_YhzywWrKfFFTbkfTuuRDC0PS15eIj6yQK_sPuU5NysFtKH33cg62xFZpsGoigAhB_PmghEdZHqsU5p5MTOroCm40vSz7FLtxVGaC-eRcDpxgEV8oclTeGWn8uh0-bgBBFzDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4moAC8UkERj9F4Sc6oOJMMfPk5twYV925p8-tEImik5PU0ke5C_X0XHSxKZwFi1CU8m2LirwDmVvxB3-tp-mBCle2dkKLZ1tTutLhRvcAP0eChHh4QMfAicOF8TJue2c8_qEgqp1SYS24ehyrKvpStfJHGIWD53sH22yCF2BgxaDcTzk3lPhRlqNwYbcaOGUFQiE9Yc6nAmZnB5GYE-f7lPzcmxY3fJgQBYHcsCOY7oEdP3Chsa-gIArJ-VmFWdT2rakykg_OHn1WnQV1BtISTVz_iE37xIpZemge6yuoab6a6_SF0puY3hKlYjlkuGCKuGn0B9AXUr93LVL0gB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWLMSj3QcU8zJeuC9kjyVrP64HmrGhxI0ayiR8QfG6-v14PRTC-VflE1Ag9HXijcQyOUX7iYefYv8Uiil3dftf3ooqGq4T2v9RWdcaazpLBv6uWW_TZLYT1iKQl6n39n0W6VdqR3GmCWrhpYZs2P1Qpu6G8E7iQNgvbAI_2V2wiaJUoVp2tt4O8jNYW_RQMsmx7HPI_AdjADas_K8DNrbJlJc2j1veD0HOYzzk0ZbDGbqIuq0jYzx2oZERfGqdlBDI9u4-uffbsSRx1pmnWrvDO6Ewmg574R8rcqPSE_XvNe-z29240Pn0D3EP8RCc2br28RUPvMl6vwNXitNH6aMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTPFFKwJldyj_LCqlRboQvJxW0hlWTITlmQqGKx-DXuJlOoNP4cOSjojFdFk8Hde3hpVP_WENBciYQjs8Dj7d6qALCxgCIEKG8qiqohCsDKbeYHjKpcZtokq7PqIEBXXFTAGRxArCr7LjvoNDx69ovI3swxBurXBwNQeMh1bMeQipMbFO5_l5J1btZv4SUBrZ4dIgUw_0xWvOz8KKCtcnDOdn5Mwb3ig04lEkwwZbkOgiYtT4KJ56fd9SrSZk-hhHhUmf4cilXIDMURihkGu3J4zFKfrYcwWRIkcmV2h6pfI5ln0xT6xXbUZzcm98UFPFjYH_XorF6Hwi3phGlZVOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emNTHr0wrdE7b7uHI1MLxccFzND4uVDw8Xlbk19vkEm86kA85hd2JccbuaoiK7K0zeOaFAoaWImIrII__se0rE65Po-bgb0tu5vd6a3UXwD0_vhi5DC4xVHO71fljG45afvRAD-LfMmgSWbMI3H39MceM5SaLBO_fmm70HUoq-VkYldOc9SsF0PbgczILem6iy6VFcL8ydYnY2jd73FcdcJGeBbr3m18vGBPr3oWcu0DaLIY8ZR-VzYsF8lsDrgQwSQUumbDqmuC-dbu_6BR6wJr4xiIeLatz_FUyyOHzh3VGMjB7E7t0kFxcmB57jI2wzN0PrXgvKY5tRK4oghOdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UK7l_RrPfdZAnzj7in8mEVjpCDQC5BunJLBPHzl708IeRy0E-TVTRB6WSLdlW0cn6K6Y4JO-7TihHdkFfGWhKj4TodFHpBmlQqZ2iAn0iTqnau46sOz1qz7oj2uJZ0i3nCsTJ6BCaClV13Z24FU20ZagWRtgB52bzq7P-7DM8zmMwyJ2dLUFzvZVx2PPygRJzRkQtooR2nxbUDG_tiE0oAAF3VnHJjSkvhz1XakVcwVLUTj7pwwipNr_cjVWydOyi-c-5X4d_ZYelAzWCKKx8HQXuaX5CPIbfQ3kDxqQmBsKVWdgyVytuEx03nphSqchxCEAiHXEodRD5Iwjtk-HsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1F6-HE3XXApGji-VlGed9s4lUswnlll_lH7ZrzShoMB0DqHTfNAFktF8WLxB3DXIG_gc-cO2NlpFFvMDdy1ELx-BYmzFc9N5mGMgX07jT3t44Qt0TklfgLVuKEgUJW_lEry9u2jEbwvr5-FsEiUcSEpwpKRSXUC1j9OzyogaUHIUI4d0vHNXAyUSnDna0NCtfueddJa1AqhZMHOshCPeuWtyGvrxI8fFeOybieQ86KaUkFk6oEapjB40FI8YMNMl4iGMbctXtQJZHfL1Dyc4abfrlihbXXDUD__iOvGd__CY9WggesT55xijYxOXvk_G8ZC6KNJkjJvSrsoSiFyFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m99un8xEirRnmDMp0viwYeXIml3_J5Rp_YgB8rQVqEoqisTJ9U5Hst9j-Kr_Cq0tN_b3U8W-QyCbA0Xybnjs7wj7HKjJJaIJfndKMif2FnpXmTmgF2pxlSlvS7aMYEEG_zKKUQyHYxviT-FWAZLHurO4qGATluuWaBie-WWQZvP28VPnMT88Z56tYiq5faxUcY13oxOqd2ZICZbJrSqUEv-bsUc-sgb9Qx_QFXSlExHUs5sA7SLE5LB9WuWbT_KcQbTAxb18lbTx5TBLwZWYkBtXgoqiYuyjiwHMiSoZ4_IPM2S5Ryw01b9gSLXSj50tbqAvBsfWK0Mpm2ScjqoJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ix0R5d4WYnLP0Y437H3Sq2Eg6SOiHpJkkcpujbiEmT_0DmoH1hqHnyXszSlUR0eONr1IsAyGUfGUj-yC7XDbjnavwSErb3lTL36HXDMW4wqG_x2XV_vc4ydfB_6W3a64EJVDoGGhZWMEJ0KUhTuFPwabJNcgiqubTHeeaymLHEPR9DrLwGvneILtEvA-9Z430ecMvj_Zr6gMorlIc1olz2BYIJetZwUGv4-IIv2wXUTXUTun0WeAduXNEZY4Qsbgup8HEGVpB784u8J91582-jlhrPOv_b2VW1w53_9IlESN2nV0o_2TdCc2pmJnjCrga6BihYFGWIFLFvGMmgm99A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/455066" target="_blank">📅 03:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455065">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ7eI3gF2PD7K4K69GrJUyiPcPpoaUBXPXD3r5e3nJEvGAJmjJ0aDmkr6bWFwfzKHCP-m8uYaDC394H0ocK_HQRkenejdfU7ywT_49MBp3USztxsVa4X0AJ3VLeugrNYKWbRzHABFtJQZjRQC73A0AI7-W6iLTbbmIGSRKX9uIhY3XLPj5h5Hs5Z_Xr3jpQlm79HAT39vo9-9m_orSwI2HY1Rj-eaXUvfQVCJXeDcWZ0XFJL1ekUr3oh5rN5gZBdepCaZ1ylLn42-Ok6q0XHy_itnX0CG_LiGupAXHymAcj-r3V7PIaPHLORQd0ZjiDAJz7pMFc6kHdwebL4NuU3PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنگ‌فرش خیابان‌های تاریخی برچیده می‌شود
🔹
طرح سنگ‌فرش کردن معابر در بافت مرکزی تهران، با هدف تبدیل این محدوده‌ها به پیاده‌راه و کاهش تردد خودروها، یکی از پروژه‌های بحث‌برانگیز مدیریت شهری در سال‌های اخیر بوده است.
🔹
حالا آقامیری، رئیس کمیتۀ عمران شورای شهر تهران اعلام کرد با توجه به سنگین شدن بار ترافیکی معابر و با تصمیم پلیس راهور، مدیریت شهری اقدام به جمع‌آوری سنگ‌فرش، و تبدیل مسیرهای پیاده‌راه به سواره‌رو می‌کند تا گره‌های ترافیکی کاهش یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/455065" target="_blank">📅 02:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455064">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یک کشته و ۱۲ مسموم درپی مصرف مشروبات الکلی در نیشابور
🔹
دانشگاه علوم پزشکی نیشابور: پنج‌شنبه شب ۱۳ نفر با علائم مسمومیت شدید ناشی از مصرف مشروبات الکلی به بیمارستان ۲۲ بهمن نیشابور مراجعه کردند.
🔹
روز بعد، ۷ نفر از آنان نیازمند دیالیز شدند که پس از انجام اقدامات اولیه انتقال بیماران در دستور کار قرار گرفت؛ متأسفانه باوجود تلاش‌های کادر درمان، یکی از این بیماران جان خود را از دست داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/455064" target="_blank">📅 02:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455063">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDrhPOFUMW9jxed8luGEw5_Pyr639fIE4kNkIuwKDpSEheNcqMkjslbslD209t40RWt9d3AqrffuLksX4j-x1p0Z9OY3tQcUnT8340WQD2O0OlZjWbQCUmjlKnFleg65q25smXWdexCcCK9Yv9A6xd9HM47oNVAoQ95bcP9ZgVjzOZCqLz2AtWsbE4X0JVCor7f2siJzxIKhKgBiVgY_ZIM9LrnonmXVQ9JGcyrUsWunQrhL0V0SUrPgpn-PHP2T1dvOp9Xr4Jlw_b0OkvcgkqPCq94f-Ie9d1XCd3F6HzdsTO83nJL109Jh4tfD7ywp1fjkL3cjkTXCxyKLc2rJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودروها روی دست خودروسازان ماند
🔹
پارکینگ خودروسازان پر شده است و قطعات تولیدی خریدار چندانی نداشته است.
🔹
مرکز پژوهش های مجلس می‌گوید که موجودی انبار خودروسازان، در زمستان ۱۴۰۴ روندی افزایشی یافته و حتی کاهش جزئی تقاضای فصلی نتوانسته سد انباشت کالا در انبار را بشکند.
🔹
در سه‌سال گذشته حجم کالاهای انبار مدام افزایش یافته و از ابتدای ۱۴۰۴ به شکلی بی‌سابقه، از میانگین پنج سال گذشته خود بیشتر شده که نتیجۀ آن قفل شدن نقدینگی در انبارها بوده است.
🔹
بخشی از این وضعیت مربوط به خودروهای ناقصی است که به دلیل کمبود قطعه در پارکینگ‌ها معطل مانده اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/455063" target="_blank">📅 00:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455062">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEyqFJn5U003H74fCPPqvwi3yUsd35C6Z3hCmw2hvrVDlQ9q9EvI91BMiv0zgLMwXxPscvaa9rl3lynHT-_KTSOCvByJRP4dQnrelH2TAXhtnMOlRonQeemiqMVvkF2cWuXUajwQs07_wbHl3yOPYjUS8PGJ_SkuelsErsz40eOk3aMP3eNUboHX3uAzJPbLSdTwZwiRwON6lZPDHelqBzt5_6OMaQQTJfyK0gZy9Jty0KKrYEvEgD-FtOPCrRJpTaQeFpzJa1i8ziG7FX2MW-Ys8Ax6Oj__McGZH29hMizxJaC-MdO-a0YGiq1_7E-V1UVAylTdKUtWn0IuHG-Dww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران دست چین را می‌گیرد
🔹
بخش بزرگی از کالاهای چین برای رسیدن به غرب آسیا، آفریقا و اروپا باید از آبراه‌هایی مانند تنگه مالاکا، اقیانوس هند، دریای سرخ و کانال سوئز عبور کند.
🔹
طولانی‌بودن مسیر، هزینه حمل و آسیب‌پذیری در برابر بحران‌های امنیتی، انسداد آبراه‌ها و افزایش نرخ بیمه را بالا می‌برد.
🔹
کالاهای چینی می‌توانند از مسیر آسیای مرکزی وارد ایران شوند و پس از عبور از شبکه ریلی یا جاده‌ای کشور، از مرز ترکیه به بازارهای این کشور و اروپا برسند.
🔹
در مسیر دیگر، کالا از بنادر جنوبی وارد ایران شده و سپس از طریق خطوط زمینی به عراق، ترکیه، قفقاز و آسیای مرکزی منتقل می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/455062" target="_blank">📅 00:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455061">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حملۀ پهپادی اوکراین به شریان گازی روسیه-ترکیه-اروپا
🔹
بلغارستان ادعا کرد که صبح امروز یک پهباد اوکراینی به خط لولۀ ترانس-بالکان شلیک شده است.
🔹
خط لولۀ ترانس‌-بالکان گاز روسیه را از مسیر ترکیه به اروپا می‌رساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/455061" target="_blank">📅 00:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455060">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9172d880e3.mp4?token=vInyLctBI9BGwINA_Z-RKRqWvCk1NfryNAXhTidm8CgdkwKHP8MBGAEHooSxA1_VQem07pxRXs70BpFLJBLzgNmV147nDY6dKTycBlM4ArAI0fiZZOEjjtu6EeebcVWXxtxzdtxHuEXpg_QHLkbaU_GibJdUSFNkAR6eoTiSEujYtf_l7X2zk_Xg--jgWTt2siWv9V8kd7YNms-93-SXDFMtgGFvFPBTctofa4NekHoBpvTGrN9vBLpx1yg7gkj4M3TCbPNvsxKOjyzLQ66sT8dZhtVbr_qU3-eeMIzaTnCVlkreYvjF_R3-20Hdlv6HYG-2wLrXOLUYtM_Sh1OMnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9172d880e3.mp4?token=vInyLctBI9BGwINA_Z-RKRqWvCk1NfryNAXhTidm8CgdkwKHP8MBGAEHooSxA1_VQem07pxRXs70BpFLJBLzgNmV147nDY6dKTycBlM4ArAI0fiZZOEjjtu6EeebcVWXxtxzdtxHuEXpg_QHLkbaU_GibJdUSFNkAR6eoTiSEujYtf_l7X2zk_Xg--jgWTt2siWv9V8kd7YNms-93-SXDFMtgGFvFPBTctofa4NekHoBpvTGrN9vBLpx1yg7gkj4M3TCbPNvsxKOjyzLQ66sT8dZhtVbr_qU3-eeMIzaTnCVlkreYvjF_R3-20Hdlv6HYG-2wLrXOLUYtM_Sh1OMnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از حملهٔ سنگین دشمن صهیونیست به ارتفاعات علی الطاهر برای اشغال این منطقه با سو‌ءاستفاده از فرصت آتش‌بس
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/455060" target="_blank">📅 23:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455059">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1be5020de3.mp4?token=O2Oa9pAgd6yNcIc_WDE0TJhwEzn7a21YDAdNWu69-vW268xOz81A2UZOWkBgILGA2ojfqCwTBTVU_hQa9Vj8oNe91wEvruUboWEyd3wHDwzrqcRQygBS_TOK-GRyveurVq70E5kr1qRgyErcvXcZuv2KKHpSTG-oB4zevRDZFO_iEvl8WAW-j19BIjAlaXwrSsO9wfCXS14IsNAtxfc0D7RNFbut3E4MLwPaRzSe2meUJ_Rm4IExUMSWXAatMJC83j1rLNvMAvvnuFQiZh9IqPcthYZaLbIBkbvdN29MKRasFhJFVj0Elcr7NQZkmOCf2hH-84bS7STT8sAjJMtTHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1be5020de3.mp4?token=O2Oa9pAgd6yNcIc_WDE0TJhwEzn7a21YDAdNWu69-vW268xOz81A2UZOWkBgILGA2ojfqCwTBTVU_hQa9Vj8oNe91wEvruUboWEyd3wHDwzrqcRQygBS_TOK-GRyveurVq70E5kr1qRgyErcvXcZuv2KKHpSTG-oB4zevRDZFO_iEvl8WAW-j19BIjAlaXwrSsO9wfCXS14IsNAtxfc0D7RNFbut3E4MLwPaRzSe2meUJ_Rm4IExUMSWXAatMJC83j1rLNvMAvvnuFQiZh9IqPcthYZaLbIBkbvdN29MKRasFhJFVj0Elcr7NQZkmOCf2hH-84bS7STT8sAjJMtTHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستادگی قمی‌ها به شب ۱۶۱ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/455059" target="_blank">📅 23:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455058">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d26f3f87d.mp4?token=ncNAwrsT77a_Dl0ICQPeSJzHJzTxeRKUips9LLT-kGyhEUTUPwNQk7QRhz2_SxWCScRCTCxmTeY2aNxQMMqQSEa3SRnOUEOcd6otXd2G1FYCFBkY0Bl-UQPnR37da0VgHDcGYk2A0TUMTb6Ydm1RFR3OdYfd2IM43L6YjtadyalUTT5X6TUbSAfI3j75sp0aZowbqJ8ne-7gCb612qxUHq0XVUmLvPyLeQEvI1X8VGEQPxeRbwd9IRWB48MxyjwjrJMCTOmrbOuknslHPyGN7mGbMbav1AAJJD73pK4mbJlakAS2iwS8lZK_dDjHEBKdhuzayVZ2ARDM_Xj_MCrN2B25enbPkdAmah5F9hMtXhZuhzPsmB0FpSweJTMX56BldvYAmzZG0V15yDoPFAbFL5Jbw7Dwu96nc9489qhX1lpmli6enqBcWF3bPFDTaT3Od25SkAFHirWacSU5yUowf8PZbNWLgZjgF_gkdqa2ifNQv1nKEsOgilB2jdt1MiJBGRJPfUHCLy4Sf955G6uQ7lvGCzXIQqcsD567E1mE16Vcb8W0tkTb-JORf9M4TRBf6FclBdDtL3uUxYTa6HnRgVV4d1JVa4gBgiwYBMz4BJdjXwD5L0Dp49Y64DlLVCw6L56JKCHKyBLErmg31DH4_o68QFbCwZYL-2GGG9crtHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d26f3f87d.mp4?token=ncNAwrsT77a_Dl0ICQPeSJzHJzTxeRKUips9LLT-kGyhEUTUPwNQk7QRhz2_SxWCScRCTCxmTeY2aNxQMMqQSEa3SRnOUEOcd6otXd2G1FYCFBkY0Bl-UQPnR37da0VgHDcGYk2A0TUMTb6Ydm1RFR3OdYfd2IM43L6YjtadyalUTT5X6TUbSAfI3j75sp0aZowbqJ8ne-7gCb612qxUHq0XVUmLvPyLeQEvI1X8VGEQPxeRbwd9IRWB48MxyjwjrJMCTOmrbOuknslHPyGN7mGbMbav1AAJJD73pK4mbJlakAS2iwS8lZK_dDjHEBKdhuzayVZ2ARDM_Xj_MCrN2B25enbPkdAmah5F9hMtXhZuhzPsmB0FpSweJTMX56BldvYAmzZG0V15yDoPFAbFL5Jbw7Dwu96nc9489qhX1lpmli6enqBcWF3bPFDTaT3Od25SkAFHirWacSU5yUowf8PZbNWLgZjgF_gkdqa2ifNQv1nKEsOgilB2jdt1MiJBGRJPfUHCLy4Sf955G6uQ7lvGCzXIQqcsD567E1mE16Vcb8W0tkTb-JORf9M4TRBf6FclBdDtL3uUxYTa6HnRgVV4d1JVa4gBgiwYBMz4BJdjXwD5L0Dp49Y64DlLVCw6L56JKCHKyBLErmg31DH4_o68QFbCwZYL-2GGG9crtHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاشمری‌ها امشب هم برای ایران در میدان ماندند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/455058" target="_blank">📅 23:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455057">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b866be118.mp4?token=PDyjHQIE81-w4TVSES1d6790_-vPVhZN4tsuNS3p__esUsZP3MZ6N-yRuuW44ZYsoJ1mH9C9o7DFdHViDICBmPV_wlnLSLvSDi2SP-5hbX7mB4-K9JfPaMFEnxKCdFMj5Muet27gj7znfM841G1Sufe6TTvKKmFwpnzDC4bkHavQq4y5UjJoyAvqsbe7XwXo3_fTuPcxE0vffeI1v8mAuLP6fCWM9fE40omqMn3xAeQmTYF1vnS-do1ENUUzFDF3Fg3q-VscOYlCuR1Ltu0ex4ie0mECotS9krzLD5ai4IFJP2G7WgRS95hh4_THQtFPCp5C3l_Zx16SfJluBCYDLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b866be118.mp4?token=PDyjHQIE81-w4TVSES1d6790_-vPVhZN4tsuNS3p__esUsZP3MZ6N-yRuuW44ZYsoJ1mH9C9o7DFdHViDICBmPV_wlnLSLvSDi2SP-5hbX7mB4-K9JfPaMFEnxKCdFMj5Muet27gj7znfM841G1Sufe6TTvKKmFwpnzDC4bkHavQq4y5UjJoyAvqsbe7XwXo3_fTuPcxE0vffeI1v8mAuLP6fCWM9fE40omqMn3xAeQmTYF1vnS-do1ENUUzFDF3Fg3q-VscOYlCuR1Ltu0ex4ie0mECotS9krzLD5ai4IFJP2G7WgRS95hh4_THQtFPCp5C3l_Zx16SfJluBCYDLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور نونهالان و نوجوانان در شب‌های اقتدار شاهرود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/455057" target="_blank">📅 23:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455056">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe93a4df4.mp4?token=fd7ghwSW27xAVTiO3SsAM-jeWxatcjcFH06mRWaoVITSRtPNYO6UdmyRorOQ48bJYJOTEyT53O8asyNTGa95RVBVy9_UgyNinzT3njWOw47LN20rocmF44g-8BMntPhM2bksI7HWKgWhRYFNcPpy2gkjqF0GlOJYu2b0M_ffnfu1deF85p54cORvXaRSo-n503PjE24hCMsjVsHeeV3K_xAtsPOIYf9D5WPug2-QjI3jn_xXuABIdYaldODjnHacohFTz6e7xKeoLTQ1EoZuTI7B3IP_4cCsSvwMt_LDNK1m5He5RzEvwU1zqwxpN8ZcTVKzqoVOClZmkXWNBTjESw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe93a4df4.mp4?token=fd7ghwSW27xAVTiO3SsAM-jeWxatcjcFH06mRWaoVITSRtPNYO6UdmyRorOQ48bJYJOTEyT53O8asyNTGa95RVBVy9_UgyNinzT3njWOw47LN20rocmF44g-8BMntPhM2bksI7HWKgWhRYFNcPpy2gkjqF0GlOJYu2b0M_ffnfu1deF85p54cORvXaRSo-n503PjE24hCMsjVsHeeV3K_xAtsPOIYf9D5WPug2-QjI3jn_xXuABIdYaldODjnHacohFTz6e7xKeoLTQ1EoZuTI7B3IP_4cCsSvwMt_LDNK1m5He5RzEvwU1zqwxpN8ZcTVKzqoVOClZmkXWNBTjESw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدای حماسه از زبان یک کودک بختیاری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/455056" target="_blank">📅 23:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455055">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003243081c.mp4?token=XfaWLUGtVE4ePbk4DYYwpxfzZIpvsEWZbCzL1B1vx-87M21tUalIULV5jbEYkJrx8bdlpxe1jcLFLwDsh5I1kkaw5x71hK2rrFHzgFB5HKxSLebyVaPmYqpIq2630sRlvke9aPtYGHp9dvZM2eBnEcmxEdQqvHCKv6TxH-thhJgQ38YZ9gfDQ34RDaBXxrNbHKEJy8dF_qQsQ6KqOQNZn6BPtEWTwYB3OniPuuU26Fx6GYQ76NKDEWVCspzjB7Zwz8SV-wCsTtMG-FOHEkgGcHeJGagswjgP_iLop29wkekC_bhrBB4SZ8o3NovbwmjtnB0zy55Epd34CCF0KlWUJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003243081c.mp4?token=XfaWLUGtVE4ePbk4DYYwpxfzZIpvsEWZbCzL1B1vx-87M21tUalIULV5jbEYkJrx8bdlpxe1jcLFLwDsh5I1kkaw5x71hK2rrFHzgFB5HKxSLebyVaPmYqpIq2630sRlvke9aPtYGHp9dvZM2eBnEcmxEdQqvHCKv6TxH-thhJgQ38YZ9gfDQ34RDaBXxrNbHKEJy8dF_qQsQ6KqOQNZn6BPtEWTwYB3OniPuuU26Fx6GYQ76NKDEWVCspzjB7Zwz8SV-wCsTtMG-FOHEkgGcHeJGagswjgP_iLop29wkekC_bhrBB4SZ8o3NovbwmjtnB0zy55Epd34CCF0KlWUJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا پای خاک، مادر و فرزند در میان است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/455055" target="_blank">📅 23:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455054">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bcad59215.mp4?token=vvSYdMgscO4sucaQEBz_smPt9LNKMyIK6nUkYEF64QU0_51iLA1qxmGqbc52-w8UuuqwZ3KTYevQIIHkCpI7cbwzIdZQiaRwSi8qYCuuB6y2hztDWTp37KwWLsherJPEWg-bNQZ3ej1-RU5QMpxNBPBBwgIN65nasVweCvaaUHBMtKtxFIp046mMy_yV3mNTyV26aeynT-vxFEgBhKNhiehLKFfiS-hiz6CqH6CfJJBkJWOSMbmo40MnXDMq5bskQwjRSr2ifUNxHG7pGYCChEwyOYa6jsY31h7PfUfgDG9m0uVia_lMnTA9TMOKMvAjHCyzK84CD7MiyaGLYnhhuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bcad59215.mp4?token=vvSYdMgscO4sucaQEBz_smPt9LNKMyIK6nUkYEF64QU0_51iLA1qxmGqbc52-w8UuuqwZ3KTYevQIIHkCpI7cbwzIdZQiaRwSi8qYCuuB6y2hztDWTp37KwWLsherJPEWg-bNQZ3ej1-RU5QMpxNBPBBwgIN65nasVweCvaaUHBMtKtxFIp046mMy_yV3mNTyV26aeynT-vxFEgBhKNhiehLKFfiS-hiz6CqH6CfJJBkJWOSMbmo40MnXDMq5bskQwjRSr2ifUNxHG7pGYCChEwyOYa6jsY31h7PfUfgDG9m0uVia_lMnTA9TMOKMvAjHCyzK84CD7MiyaGLYnhhuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۶۱ «قرار عاشقی» گناباد؛ هم‌صدا در حمایت از نظام و رهبری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/455054" target="_blank">📅 23:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455053">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c9db54a9d.mp4?token=XmHb1T_7d8oOCWGUTJNPyw5Z6DhjmQkqqtnFlaC8Wd7tWRT9bnPGG-6tgF6m_q9l91hmeb33gzTf9PokQ-Lwy5XTFXCJalbpfRlBvkTIi-mSJDdjAwOxsiYUcW_SSSP607mU7ZCJA-vosttUly3xFidrueXocDCyxoncFLMWHMP19Blpc8OKzmTu9huv3HVJrQW-waCKV6_nzsmbarX2ZWNoN_qZ-M6FP9HK63loQkHafxj3nJ3zpYboh4IxAm5dduzah-QqijjeUNRISBS6aPVIkmGyptv49E1PNFpN04qbrUq2-Nt9d6tq_KhpoAniJ3mFE5s_Zk8yJB6ZfmTy0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c9db54a9d.mp4?token=XmHb1T_7d8oOCWGUTJNPyw5Z6DhjmQkqqtnFlaC8Wd7tWRT9bnPGG-6tgF6m_q9l91hmeb33gzTf9PokQ-Lwy5XTFXCJalbpfRlBvkTIi-mSJDdjAwOxsiYUcW_SSSP607mU7ZCJA-vosttUly3xFidrueXocDCyxoncFLMWHMP19Blpc8OKzmTu9huv3HVJrQW-waCKV6_nzsmbarX2ZWNoN_qZ-M6FP9HK63loQkHafxj3nJ3zpYboh4IxAm5dduzah-QqijjeUNRISBS6aPVIkmGyptv49E1PNFpN04qbrUq2-Nt9d6tq_KhpoAniJ3mFE5s_Zk8yJB6ZfmTy0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ما می‌جنگیم و سختی آن را هم می‌پذیریم؛ رهبر انقلاب هر تصمیمی بگیرند ما تا آخر پای آن هستیم.  @Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/455053" target="_blank">📅 23:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455052">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b96583e47b.mp4?token=hpA9qIsWSR6d7EnS52Qdc9O3VJgJYTTlBB7EjyU7M8TBfiMBScr3Tyf2WyJ5PLQcbBMX5UxeF2w_bPi8p79itXxtLgO2Hq0Fq7e7jFD5vZuUiz9D2ghjDTryhHYdBOjmI85Ibz-2iubHHDTMboscXaLoVwiMNZwG5p0ge7vilsx7_ULwwbdro4THGCgzXmSNt9s966_Z9N-ATIAn8MOYnxnNY2ZOhroVp88QCe9_bZKIYo1SN2ufRqNNefdvFaXaMdxBq-ty6kgTbQ8RQx0qjfMj58pAjvix4EDPdkjszn3ilkYS4pkp6TxKCY4H0FtzXds4_IO63UZfev8o_JqpvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b96583e47b.mp4?token=hpA9qIsWSR6d7EnS52Qdc9O3VJgJYTTlBB7EjyU7M8TBfiMBScr3Tyf2WyJ5PLQcbBMX5UxeF2w_bPi8p79itXxtLgO2Hq0Fq7e7jFD5vZuUiz9D2ghjDTryhHYdBOjmI85Ibz-2iubHHDTMboscXaLoVwiMNZwG5p0ge7vilsx7_ULwwbdro4THGCgzXmSNt9s966_Z9N-ATIAn8MOYnxnNY2ZOhroVp88QCe9_bZKIYo1SN2ufRqNNefdvFaXaMdxBq-ty6kgTbQ8RQx0qjfMj58pAjvix4EDPdkjszn3ilkYS4pkp6TxKCY4H0FtzXds4_IO63UZfev8o_JqpvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: من از جنگیدن نمی‌ترسم
🔹
شهادت شیرین‌ترین آرزوی ماست و تا پای جان ایستاده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/455052" target="_blank">📅 22:56 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455051">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584735f78f.mp4?token=LumU7Fwbg5OAI-7N5_KgtMflofeSZ-pTPxOhh7ONTlQFJ_ly9dGogC30IajIhSUWROSKp4K2wGJb_RqhC0FbobbcwrrvojmmceubSjofHTfFU9_bgOFf3XQGVYNixbw3QR03IKbhFHvnq-6DNIVAyQE94hJyfQFus7MNML1sQxI0z5GIvEap_Tf4i4DUelEN5rXf9fo1PKBICmgSCleh_GCiWowolbEVHQLIGXXKmvsv_8ZpApYksyHvbe43MrhvQJk2egpIbI38oQdkDJY_6uMYwWtMi2WkW3AfmN2AVWmmWNt9umtlONoJlJdbAHP3vR2zyqxzUXwk0sVlIVWr4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584735f78f.mp4?token=LumU7Fwbg5OAI-7N5_KgtMflofeSZ-pTPxOhh7ONTlQFJ_ly9dGogC30IajIhSUWROSKp4K2wGJb_RqhC0FbobbcwrrvojmmceubSjofHTfFU9_bgOFf3XQGVYNixbw3QR03IKbhFHvnq-6DNIVAyQE94hJyfQFus7MNML1sQxI0z5GIvEap_Tf4i4DUelEN5rXf9fo1PKBICmgSCleh_GCiWowolbEVHQLIGXXKmvsv_8ZpApYksyHvbe43MrhvQJk2egpIbI38oQdkDJY_6uMYwWtMi2WkW3AfmN2AVWmmWNt9umtlONoJlJdbAHP3vR2zyqxzUXwk0sVlIVWr4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: من از جنگیدن نمی‌ترسم
🔹
شهادت شیرین‌ترین آرزوی ماست و تا پای جان ایستاده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/455051" target="_blank">📅 22:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455050">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حملات گستردۀ ارتش یمن به مواضع مزدوران سعودی
🔹
نیروهای مسلح یمن اردوگاه «العَلَلة» در الضالع هدف قرار گرفت. همچنین گزارش‌هایی از وقوع انفجار و حملات پهپادی در عدن، تعز و شبوه منتشر شده است.
🔹
هم‌زمان، اردوگاه‌های نیروهای وابسته به ریاض در مأرب نیز هدف حملات…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/455050" target="_blank">📅 22:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455049">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e11600a04.mp4?token=Z3_gmiq-uCmENPAQrFuIvOoq5NZSMBEySjS_qJL1kV1ciEvMSusKXn0D9Xiofb6JM5yN9Wy9lFMfDzCal66dR-KqIoCeGp6Wo8b22n73DX_lPPmQQg1pFzqb-3gFpMVCFNRJE2-KMneuDhUY6otUT_Ny1Jz4wFfIN85v-dYj0aCN2qyf67MhqKMB39c5lMuBXJ6mPN3Cd2ZwztwXU6mRp1I0PysiHUMlcsXKSkb58ylhHOA01nqTEhcHsTL85DppZe1poavVrqYwaQfBcl9UJaCZVdTiqTUJt2b0JBQR9Ve2NQ-FS0-kTjG-PkAJPTJE9N69sALbGixNH8VWl6aocQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e11600a04.mp4?token=Z3_gmiq-uCmENPAQrFuIvOoq5NZSMBEySjS_qJL1kV1ciEvMSusKXn0D9Xiofb6JM5yN9Wy9lFMfDzCal66dR-KqIoCeGp6Wo8b22n73DX_lPPmQQg1pFzqb-3gFpMVCFNRJE2-KMneuDhUY6otUT_Ny1Jz4wFfIN85v-dYj0aCN2qyf67MhqKMB39c5lMuBXJ6mPN3Cd2ZwztwXU6mRp1I0PysiHUMlcsXKSkb58ylhHOA01nqTEhcHsTL85DppZe1poavVrqYwaQfBcl9UJaCZVdTiqTUJt2b0JBQR9Ve2NQ-FS0-kTjG-PkAJPTJE9N69sALbGixNH8VWl6aocQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: سال تحصیلی آینده حتماً حضوری است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/455049" target="_blank">📅 22:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455048">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335d4aa8a7.mp4?token=JcOdnwBLMpFoRWz9diRmPCicFZgB3thLtlWGZ50wpGo6nh204hid6GrgbDN7DdROpFBjSMcdLHvnk0b4E36yeKqyRt37nBCPRD_Ofd-pJG6vmWtGnVqbyU9ixEo3khADxTmpUziK_FENJB1szDrC49RTJGDh_FMouG349eqkyU4tnXYWLBDjQqgvREme_XvGf60jWkKqOPJY06Bq-LhvZX0NsAsu2KUDatigRn2vys3YgPtAU_79xieTcyPJ_-KsGxBlEb0mOnuttsyVS21H0hLZiqLWQXTFYubyATa0B08D5qAri_3dOE2JuWOgsgOMs3fL4JqCagqYntIqqaEIiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335d4aa8a7.mp4?token=JcOdnwBLMpFoRWz9diRmPCicFZgB3thLtlWGZ50wpGo6nh204hid6GrgbDN7DdROpFBjSMcdLHvnk0b4E36yeKqyRt37nBCPRD_Ofd-pJG6vmWtGnVqbyU9ixEo3khADxTmpUziK_FENJB1szDrC49RTJGDh_FMouG349eqkyU4tnXYWLBDjQqgvREme_XvGf60jWkKqOPJY06Bq-LhvZX0NsAsu2KUDatigRn2vys3YgPtAU_79xieTcyPJ_-KsGxBlEb0mOnuttsyVS21H0hLZiqLWQXTFYubyATa0B08D5qAri_3dOE2JuWOgsgOMs3fL4JqCagqYntIqqaEIiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تشکیل تیم کارآگاهانِ زبده برای دستگیری عاملانِ قتل حمیدرضا رجب‌زاده
🔹
سخنگوی پلیس: تیمِ تخصصی و ویژه کارآگاهانِ پلیس آگاهی تهران بزرگ، برای شناسایی و دستگیری عاملان قتل فردی به هویت حمیدرضا رجب‌زاده بلافاصله بعد از اعلام مفقودی تشکیل شده است.
🔹
از رسانه‌ها…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/455048" target="_blank">📅 22:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455046">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40344d8430.mp4?token=dB-ZMmukqnVvfWzrjXAkWewQi9SzclEHgVj5u6wvJOehWiNKrDQgKn_TPz_Eit_SeH7N75TE-6PSPU3S9vaykobQ9fAa8xVUSZNa2zlAG14QiS0tiE0Q_CrmYD_zGl6XERkuC4zIEt5kcvAikUGsxtXBYXHCZFSth0Y4rwuj80Xd_UjER8Hq64zJZysFYiA1FFTBFylg9HU8vz2as5JRwYo8hJ-G4bChuecFxv0cmOjLPr1AwhopZAV8A0W-f882FnvCQrYHSvMt4L5Z07bP25mAFrkN-vRuWFgWlzgTzxYKUsQULSZPv8F4nm_PREup0WrTmHehqOoMVwDB7JjwVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40344d8430.mp4?token=dB-ZMmukqnVvfWzrjXAkWewQi9SzclEHgVj5u6wvJOehWiNKrDQgKn_TPz_Eit_SeH7N75TE-6PSPU3S9vaykobQ9fAa8xVUSZNa2zlAG14QiS0tiE0Q_CrmYD_zGl6XERkuC4zIEt5kcvAikUGsxtXBYXHCZFSth0Y4rwuj80Xd_UjER8Hq64zJZysFYiA1FFTBFylg9HU8vz2as5JRwYo8hJ-G4bChuecFxv0cmOjLPr1AwhopZAV8A0W-f882FnvCQrYHSvMt4L5Z07bP25mAFrkN-vRuWFgWlzgTzxYKUsQULSZPv8F4nm_PREup0WrTmHehqOoMVwDB7JjwVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازیکن جنجالی قلعه‌نویی در بلژیک دبل کرد
🔹
دنیس درگاهی، که دعوت و بازی‌نکردنش برای تیم ملی در جام جهانی ۲۰۲۶ با انتقادهای زیادی همراه شده بود، در بازی امشب استانداردلیژ بلژیک و بروخه در لیگ بلژیک، هر ۲ گل تیمش را به ثمر رساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/455046" target="_blank">📅 22:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455044">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egzhNA5XKQy34nWzLjJdSna90SWRb1lE5_3HvrwElA6_sPR1Wbgt10EUjSitPKLe8i44JGtK1jxKBDeqQoY9PqzI-AMtVuUKwtVxSoYVJuNb3swaCX5qzlxJOIRQA9aEc0W2gKyo_HrMkxD--XrgdL3UGnOeyPLFar0I9zmyqcC5qjiRy3k8H9SCDXchr2QzIZCXnNCgdr3r0zLLQkGCzeNLbKY1vWH0ZZUNOJZIbqXis_2EwTmCC5V-S6yf_MGPcL5t7nlZrYM3rXaLRSmqnPmldWtxSBkU0h15qoraZp9qKHJ2ecYgcgHvTojAd5Q1EnBUMtcw2lFLJZ803E00QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWD3gXBRVdgDvG4pmNur-mQ4PElSfW7Y7NF9yQx2uyd91Z7iifv3W-GgaHQQa3pB_51Wlu3TDPiC8U3pdYvG6m5TodrF043hCpcgjotK5TQtv0vZ6CV1fRmGCz2Vhhwujp1PciwspUhCkPOl19ZhOwPP4srDhXrdsN5aRgyan9l7JudBqSn2tD--ku75FJyX3M8icZ9ADYVU7b1l8qXsHqwzNglINdgcBERemE_M1C1_HqQftMKuczqCInFRKscRg40emtP1r6Nta-UiL1dOsnjgz9lgwNA5c3cN2uUL__LEUpijZF-DHMVcATF89h5_0_5gJtu6KscuXqaDJMYb_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت عکاسی که قاب داغ میناب را به جهانی کرد
🔹
مرتضی آخوندی، عکاس هرمزگانی که عکس هوایی معروف و دردناک از مزار کودکان شهید مدرسۀ میناب را گرفته بود از نحوۀ ثبت این قاب غم‌انگیز که برندۀ جایزۀ «گلدن شات  ۲۰۲۶» گفته.
🔹
او می‌گوید: در مراسم تشییع تعداد زیادی از عکاسان و فیلمبرداران حضور داشتند و من تصمیم گرفتم با استفاده از هلی‌شات، تصویری هوایی ثبت کنم.
🔹
هوا بسیار گرم بود و نور زیادی وجود داشت. از زیر یک درخت ایستاده بودم و تلاش می‌کردم تمام قبرها در قاب قرار بگیرند تا مظلومیت این بچه‌ها دیده شود.
🔹
به نظر من این موفقیت کمک خود بچه‌ها بود؛ آنها باعث شدند دیده شوند و فراموش نشوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/455044" target="_blank">📅 22:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455043">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8bd81f6b.mp4?token=pDOaJ-GNQ4aPJu3W_0EPIvxnWaID57aVe3Mv-Me7DnA64qS7UWFEzsY7r8kVQDgDOrIma0aWZbQY0kRIuaNoDd8bm56s7iZtd5ITfp8IU9tbzzISwd6EQhtm8biEg_BbPF6Z1DE5HknknQJLpZb-ZVQ0knRIke_Hg51uO2P8Otn0tNBHbJojZhhZFpToDpOVZ0xQ-Hu_1ApeqBxblMq4uqNMMc-7W63Z_VpTzRSHmBRZ9fs_Jx0jcpGU77OerRP4PbTw0RctWoAwWlDVtE4XXSL0cHR1xcB7H6KSbRG54E--Tv9MIMESOk9NCHgaW87iXjcTMbzUgBu1cHhpgh6RpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8bd81f6b.mp4?token=pDOaJ-GNQ4aPJu3W_0EPIvxnWaID57aVe3Mv-Me7DnA64qS7UWFEzsY7r8kVQDgDOrIma0aWZbQY0kRIuaNoDd8bm56s7iZtd5ITfp8IU9tbzzISwd6EQhtm8biEg_BbPF6Z1DE5HknknQJLpZb-ZVQ0knRIke_Hg51uO2P8Otn0tNBHbJojZhhZFpToDpOVZ0xQ-Hu_1ApeqBxblMq4uqNMMc-7W63Z_VpTzRSHmBRZ9fs_Jx0jcpGU77OerRP4PbTw0RctWoAwWlDVtE4XXSL0cHR1xcB7H6KSbRG54E--Tv9MIMESOk9NCHgaW87iXjcTMbzUgBu1cHhpgh6RpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نسلی که باید بیشتر شود؛ بچه‌های دل‌وجگر‌دار
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/455043" target="_blank">📅 22:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455042">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32de040c2.mp4?token=nC-DxW5gKvsJiZmL-d3sCQ9KLi4o0SNTS8HyISxfO11EUQmzWNSCSIksPE43pQtNUdWvjYD0As2tePVY4ygjWe-_R_JAY56MqQWLW7Twb093mO5wNBowJze8GdquV0LoKQrWR_leV01y-N0Ydgr7-LJ3RRx3ulII9avupsvT1gHqZMa8R5DWxdaUak3UmYygc9FY4PQsly9NsIMw-a8njvZv5IjPaaYrwMQ-LE97tEcyXIBPTEr-R5UdsyKD8YkzFcobyASSE9REIWAu4Dw5F6atHjTh01cY5ytZ1lwofNUyo50erXVSSBdYUxBO6c8SPY4w9sAWX9uSCvwW8xbEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32de040c2.mp4?token=nC-DxW5gKvsJiZmL-d3sCQ9KLi4o0SNTS8HyISxfO11EUQmzWNSCSIksPE43pQtNUdWvjYD0As2tePVY4ygjWe-_R_JAY56MqQWLW7Twb093mO5wNBowJze8GdquV0LoKQrWR_leV01y-N0Ydgr7-LJ3RRx3ulII9avupsvT1gHqZMa8R5DWxdaUak3UmYygc9FY4PQsly9NsIMw-a8njvZv5IjPaaYrwMQ-LE97tEcyXIBPTEr-R5UdsyKD8YkzFcobyASSE9REIWAu4Dw5F6atHjTh01cY5ytZ1lwofNUyo50erXVSSBdYUxBO6c8SPY4w9sAWX9uSCvwW8xbEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی خبرنگارهای نوجوان، سوژۀ خبر خودشان شدند!
🔹
فارس این‌بار میزبان یک دورهمی صمیمی با خبرنگارهای نوجوان بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/455042" target="_blank">📅 21:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455041">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OboY-SRz8hWadNq8qjokiBix3qOSikrFjCmLZqG5hXXu8stkGj3SC5hore6HoavtxWic1reeGFEO3x0l93cDVuw1l5KYZhSr1mVg55KbUyNO8iNWdVKaQqi64qyJWw3dClmHJqBS0QNfkjRjr5RbxVEUZo6L96kR-dqCOJ6Uzd4uL_NVUCWhEKKLJWVgThDc6NQryVFLHGNbRjwc3bjLlffGOxEGrnGbKKk8MOIYyPQyOYXQwWuB2zHcPQdZwl0znkCISpO_v7vLLYnaxTXrqw2-gIodppn7SVbclrLT73yW4ldJHpi-4gsGqIdn03jYa_CbeHCJUbzp17AymZIWpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفر فرمانده سنتکام به اراضی اشغالی
🔹
الجزیره گزارش داد برد کوپر،فرماندۀ ستاد مرکزی ارتش آمریکا در خاورمیانه وارد اراضی اشغالی شد.
🔹
وی قرار است با مقامات ارشد رژیم صهیونیستی ازجمله رئیس ستاد ارتش ارتش اسرائیل دیدار کند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/455041" target="_blank">📅 21:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455039">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e64ea390.mp4?token=kbYGCHSRAWMZVaPhS9gfYUpLT5xtoODH1SJCUuO_JZugar-ZlA67jWwLMHlP3sZlqg-7bv4d6mvJOH5cpEIy-KwOVXngdAjDr-XGatG5nKau0bPku6ZeH52Na_NSMlEw0j26tTjjmn0Krkt7eeV7VNjvf5YaKGflQvNzuBpkmGCd2scshNe4PP40AWd6QSZ5elDFXQgNpl8b47NQuPlOV_miXsKpdJzeIGVYd3H41wO3hUcBKfVSPxMC4TaioOX0XvrDPTbjsIjudIhsZdnqcLFNgVYWEiZQmm01edOvltb3aQV-Wc7FHqG06nXQuF3akR-36EIdU_rSt0bbJxOjMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e64ea390.mp4?token=kbYGCHSRAWMZVaPhS9gfYUpLT5xtoODH1SJCUuO_JZugar-ZlA67jWwLMHlP3sZlqg-7bv4d6mvJOH5cpEIy-KwOVXngdAjDr-XGatG5nKau0bPku6ZeH52Na_NSMlEw0j26tTjjmn0Krkt7eeV7VNjvf5YaKGflQvNzuBpkmGCd2scshNe4PP40AWd6QSZ5elDFXQgNpl8b47NQuPlOV_miXsKpdJzeIGVYd3H41wO3hUcBKfVSPxMC4TaioOX0XvrDPTbjsIjudIhsZdnqcLFNgVYWEiZQmm01edOvltb3aQV-Wc7FHqG06nXQuF3akR-36EIdU_rSt0bbJxOjMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: ۷ نفر از مدیران شرکت کلاهبرداری یونیک فاینانس شناسایی و تحت تعقیب پلیس اینترپل قرار گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/455039" target="_blank">📅 21:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455038">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShKP8yh7hT4Y9GzxvSsSYUO8FCN6QY-1StSnA8AJ_O5pqKxkMsGGiwzd0bsaCtcIGyJjwqN63bWuRfnwgD457YaIHi5ENok_vg3w9jc00uE0vqaotDpeZ9QMmjnlIQnvE_OwJYlvyGGVJed8-dJMsrFc38a4MYj5VkCbHk4Y5-7UL8Swld2dbuvk4Ujl_8ybz5SP8T92U5Z_wKjcmF_sHam3326iEnHhbHeiE5o_uLcN-rvn42i4KsYSIt7e8WpW8R7xpYM0Mqu_Jiwfcmlthn6teSxjmxmHnQA9xbSUKOu1JWCvUOVfKaav1RcsmIN1eKY1ZQlr-5MI23aUOBsxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طعنۀ همتی به وزیر خزانه‌داری آمریکا: پول‌هایمان دست خودمان است
🔹
همتی، رئیس بانک مرکزی امروز گفت: آمریکایی‌ها مدام اعلام می‌کنند «فلان تراستی یا صرافی رمزارز را بستیم» اما این ادعاها خوراک تبلیغاتی آمریکایی‌هاست؛ این‌ها هیچ ارتباطی با ما ندارند.
🔹
پول‌هایی که جابه‌جا کرده‌ایم دست خودمان است و درحال استفاده از آن‌ها هستیم.
🔸
۲ ماه پیش وزارت خزانه‌داری آمریکا ۴ صرافی رمزارزی ایرانی را تحریم کرد و مدعی شد با ارتباط با بانک مرکزی به دور زدن تحریم‌ها کمک کرده‌اند.
🔸
وزارت خزانه‌داری آمریکا امروز نیز یک صرافی رمزارزی ایران را تحریم کرد.
🔹
بااین‌حال رئیس بانک مرکزی می‌گوید که امسال حتی بیشتر از دورۀ مشابه سال قبل ارز تامین کرده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/455038" target="_blank">📅 21:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455037">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1791af6861.mp4?token=SQrPVuc1Ld8qIC5Ak0w5DebDzm5br9kQqRck8rO483t9D2rjls_jf4oir-bGgaurxUSkCDFBgel1XPg1WKnjl-fD4aBcwKyFLp8XAHByCUt72EKsb62oWipPx6Ix6zLZQrhe4KY7Ffav8UP1qfoxPOXj07dm11XWnl71Ala1posUzh4bHmyCZLUT6s62Sw9jhNXDU1XtXkoR8nD-Xr7TmqLu5WhfWenXiQ6eHTsZrNC5kzPutP2D9uNjFN2lm_i_VYGc83ZqubNHdGJkKFf9KZHlYGIVQXgglDGiitS9My1gjcRfhIKEeTDce7YETp-AYJ4SuwrgGIXvMJ9rGV4KiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1791af6861.mp4?token=SQrPVuc1Ld8qIC5Ak0w5DebDzm5br9kQqRck8rO483t9D2rjls_jf4oir-bGgaurxUSkCDFBgel1XPg1WKnjl-fD4aBcwKyFLp8XAHByCUt72EKsb62oWipPx6Ix6zLZQrhe4KY7Ffav8UP1qfoxPOXj07dm11XWnl71Ala1posUzh4bHmyCZLUT6s62Sw9jhNXDU1XtXkoR8nD-Xr7TmqLu5WhfWenXiQ6eHTsZrNC5kzPutP2D9uNjFN2lm_i_VYGc83ZqubNHdGJkKFf9KZHlYGIVQXgglDGiitS9My1gjcRfhIKEeTDce7YETp-AYJ4SuwrgGIXvMJ9rGV4KiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر خبرنگار میدان بودید، روایتتان از کدام جلوهٔ ویژه ماندگار می‌شد؟
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/455037" target="_blank">📅 21:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455036">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044924ce02.mp4?token=mR625RG-0eFIHraLV34oTQr4xH-yq6Ir04qkhKL0Vo7r6ZBH8j_K5qr6GYRjY-LO4eFamY1TCPh3RUusfB7Wpo3VVzzh27sTk2e8NBQFXQ0oseiTdYxm8f_rpyCmfmluMkAaKWJ-f4UoWOPLcuLbRL0S2xsTP22CLU-NV-8AWtNktUiYbVqolcmmhSozcXNY7sBSLjtVkrGlfxHdjR4itN5T-kGQdw5CWB8r7F1ZxafgmAyInmX69Ha_LPFYxxkmak9Sr4HD1B8wvMUAhjMpmYrBMFTndecGUzIa8L0INlN5yOTbLxwm6zzSBHsalf2Art0scdkgfI3kJ67iaGcyNaTD7GdMKb5YUy9YEUBSBfUfvP4r4t5DRUQc38gA1LIKQwEfzprI18BUKn3O0R4ECGgWis892wKRuQAdYV-7Kesn2Erdbe8ccJlEF0iUlPzuvqsLSz4Fvzvjs7t_YzNtg-3UhKwJB3hA9Ao8cgg1kRp3lAkbEr39bujPDMa6Yja-vpgiLvgW6OFkCVqjdKOaCa3CN-jXUm6aX-JKLnAiUgAIUdmYexVpfagtjMugNMJpSWI5lnIBS4vBtnjZVLtW6_W47LpO0IsdyXbDbBgIQQvtzvLSeXeD4B7D-_S_c-A_lTypIuiOiDpba3tHn_GgnBxICqpXmUKYiuVEdD9XE18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044924ce02.mp4?token=mR625RG-0eFIHraLV34oTQr4xH-yq6Ir04qkhKL0Vo7r6ZBH8j_K5qr6GYRjY-LO4eFamY1TCPh3RUusfB7Wpo3VVzzh27sTk2e8NBQFXQ0oseiTdYxm8f_rpyCmfmluMkAaKWJ-f4UoWOPLcuLbRL0S2xsTP22CLU-NV-8AWtNktUiYbVqolcmmhSozcXNY7sBSLjtVkrGlfxHdjR4itN5T-kGQdw5CWB8r7F1ZxafgmAyInmX69Ha_LPFYxxkmak9Sr4HD1B8wvMUAhjMpmYrBMFTndecGUzIa8L0INlN5yOTbLxwm6zzSBHsalf2Art0scdkgfI3kJ67iaGcyNaTD7GdMKb5YUy9YEUBSBfUfvP4r4t5DRUQc38gA1LIKQwEfzprI18BUKn3O0R4ECGgWis892wKRuQAdYV-7Kesn2Erdbe8ccJlEF0iUlPzuvqsLSz4Fvzvjs7t_YzNtg-3UhKwJB3hA9Ao8cgg1kRp3lAkbEr39bujPDMa6Yja-vpgiLvgW6OFkCVqjdKOaCa3CN-jXUm6aX-JKLnAiUgAIUdmYexVpfagtjMugNMJpSWI5lnIBS4vBtnjZVLtW6_W47LpO0IsdyXbDbBgIQQvtzvLSeXeD4B7D-_S_c-A_lTypIuiOiDpba3tHn_GgnBxICqpXmUKYiuVEdD9XE18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یک قاب متفاوت در نشست خبری رئیس‌جمهور با اصحاب رسانه
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/455036" target="_blank">📅 21:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455035">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزارت اطلاعات: خبرنگاران نقش زیادی در ناکامی دشمن در جنگ داشتند
🔹
روابط‌عمومی وزارت اطلاعات به‌مناسبت روز خبرنگار: خبرنگاران، سفیران و مرزبانان آگاهی , پیش‌قراولان خط‌مقدم  جبهۀ رسانه‌ای به‌شمار می‌روند.
🔹
خبرنگاران متعهد رزمندگانی هستند که به تعبیر امام حکیم شهید، اثر اقدامات‌شان اگر بیشتر از بمب و موشک نباشد، کمتر نیست.
🔹
جنگ تحمیلی اخیر نیز رزمندگان حوزه رسانه‌ای کشور، در کنار سایر رزمندگان نقش بارزی در حفظ و افزایش تاب‌آوری آحاد جامعه، انسجام آن و ناکامی دشمن و سربازان رسانه ای آن‌ها داشتند.
🔹
صدای صادقانۀ شما در امیدآفرینی، روشنگری، حفظ و ثبات امنیت روانی مردم و جلوگیری از جابه‌جایی جایگاه ظالم و مظلوم توسط دشمن سفاک جنایتکار، بلند و رسا باد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/455035" target="_blank">📅 20:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455032">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d13RmMlvHe5huolkd7GZEBqgNLVe-iUsOsp7G6limExoxRIuNu0zmIfuS9qRwu_k7l6XTpYDqhfToYaPnr9YmvHXxKF1RQmivLWMGlGFcDh37eXLtjT4YK3fUK4ee120868WBzvt0vewm7tHGcNCB0aIN10LqB00V-lYJMUVJLDMdt2K-vQGTLc21drUXEyEW3rEAYE14AgjZBBnYHzzn3LY1OWAsupGAG6xaJOidph-DMsjODu-cp0lbSK-P9sx2VTjseNNExp1D488fEVGa7rTZDNfzVeW-SP923pzRL4i1HwMOhV-OGYodq9e_n80wMlfXWilJNf8c2d4MXEhdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXH01aoAtHSXc7_4m0I9wbEgS1Io9ZWy8B-RaNWW-53Rcye2kaFUs0tCRvTzoZTgGbLDMyq3j8OVoKCsPtqaZr5kKGF8SET7OshBLk7XNjbgBbu3NPPceZ0atR1Jq9JS5Cngu94uceGFn27OZ9ranAnpeaf32mh2VaMam4NJefYcjt2izR354MeiU8dr5plHUDjkvCrnHg-yZAXsW20s8hGMTAeF0Ydh1NRd5gUOsiAOmtw1I2Y_TnSFbnYQutH5ZWC-M8tZTqO6Hkl1loyPENeBRa9mB_qidPrivM4xWI-2oxBoTzOtjWtI26BDu0FUOuolksF3fX3EI5jx3TTGCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a871cc9019.mp4?token=GVLjuwW88h8m1KXarPiHjSa420cpjHPrGf1obFOwCw1fFOAn54xa7Xtm5W5_HAhjdZEA8Gl0EIAFwzegZijn81k5-W2gwL8Z-LKH3i6l-XXHKlM1LnpMPYh1eAsgJFlBh69t2BtR697of3Z1t9DVPhMIeL0D_TFvw1rqBvFjbEtUVc0TIax1gA0D1KbVgsCWQKRd4qRmCbYo_i4NMlzCRKuBCfCHvI5z7hRy-ZmDlw8n6ebPF6WoXjTh834dw_YWegNzJOummN99qD3oEBn2A8ID9dt_bA0nb60KqzUPySZ-oENz_uKjLNaFw3RnRDBAvauLjYIOyBzEnkqIrzfv8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a871cc9019.mp4?token=GVLjuwW88h8m1KXarPiHjSa420cpjHPrGf1obFOwCw1fFOAn54xa7Xtm5W5_HAhjdZEA8Gl0EIAFwzegZijn81k5-W2gwL8Z-LKH3i6l-XXHKlM1LnpMPYh1eAsgJFlBh69t2BtR697of3Z1t9DVPhMIeL0D_TFvw1rqBvFjbEtUVc0TIax1gA0D1KbVgsCWQKRd4qRmCbYo_i4NMlzCRKuBCfCHvI5z7hRy-ZmDlw8n6ebPF6WoXjTh834dw_YWegNzJOummN99qD3oEBn2A8ID9dt_bA0nb60KqzUPySZ-oENz_uKjLNaFw3RnRDBAvauLjYIOyBzEnkqIrzfv8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واژگونی تانکر سوخت در بغداد
🔹
در پی واژگونی تانکر حمل سوخت، آتش‌سوزی گسترده‌ای در منطقه الشعله بغداد روی داده که در نتیجه آن چندین خودرو هم دچار حریق شده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/455032" target="_blank">📅 20:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455031">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آغاز عملیات اجرایی نخستین پروژه مشارکتی شهرداری تهران در قالب طرح جدید خانه‌ریز
خاصه‌باف مدیرعامل سازمان سرمایه‌گذاری و مشارکت‌های مردمی شهرداری تهران:
گودبرداری نخستین پروژه مشارکتی شهرداری تهران در قالب طرح جدید «خانه‌ریز» آغاز شده است.
پروژه مسکونی فجر در غرب تهران، با متراژ مفید ۶۴۰۰ مترمربع، بر مبنای الگوی جدید سرمایه‌گذاری، احداث می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/455031" target="_blank">📅 20:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455030">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDXHZ3BNpbSnY61dYgEoFiFNiIKmPFZKJmumfc7pEIQq50wtODeRi1GHYGq28D03LEWpD-jFsKTKbLC3nq6WZU3LoQKmIPv9q6julL7zI9si1lb2xacCENsz_nyPDmO2GDbHGgeIPq-mNwaJ9fajKQmRvDsoqs4tIzj7pJh284DY5nji7RnORBDZ2oIT70-Y-ZZg-bnzLLoQXnYgq09RY8q8HN4wh6RFTvyI1INy_QICwvHAH7gsruCOjPXAZhdJS_HJc_gtACXzLZZfn_QQ2ZNNT-najJPgeRdv2UjfmfLD6vuQAtvxujG3V1CXgZO3U3UU4IYcvADQOGoVvYhh_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پیام تبریک مدیرعامل بانک رفاه کارگران به مناسبت روز خبرنگار
بسمه‌تعالی
🔹
فرا رسیدن هفدهم مردادماه مصادف با سالروز شهادت محمود صارمی و گرامیداشت روز خبرنگار را به تمامی انسان‌های فرهیخته‌ای که رسالت خویش را در روشن نگاه داشتن چراغ آگاهی، پاسداری از حقیقت و روایت مسئولانه رویدادها معنا کرده‌اند، صمیمانه تبریک عرض می‌نمایم.
🔹
امروز، بیش از هر زمان دیگری، جامعه به رسانه‌های حرفه‌ای و مسئول نیازمند است. در روزگاری که سرعت انتشار اطلاعات مرز میان حقیقت و تحریف را باریک‌تر کرده، خبرنگاران با پایبندی به اخلاق حرفه‌ای، دقت، انصاف و امانت‌داری، از سرمایه ارزشمند اعتماد عمومی پاسداری کرده و به ارتقای آگاهی و مسئولیت‌پذیری اجتماعی یاری می‌رسانند.
🔹
بی‌تردید، خبرنگاران و اصحاب رسانه با انعکاس صادقانه واقعیت‌ها، تبیین دستاوردها، بیان دغدغه‌های مردم و نقد منصفانه، نقشی مؤثر در تقویت سرمایه اجتماعی، ارتقای شفافیت و پیشرفت کشور ایفا می‌کنند.
🔹
بانک رفاه کارگران نیز رسانه‌ها را همراهان امین خود در مسیر خدمت‌رسانی، حمایت از تولید و توسعه اقتصادی کشور می‌داند و تعامل سازنده با اصحاب رسانه را عاملی مؤثر در افزایش اعتماد عمومی و ارتقای کیفیت خدمات برمی‌شمارد.
🔹
امید است در پرتو الطاف الهی و در سایه تعهد حرفه‌ای، اصحاب شریف رسانه همچنان پرچم‌داران صداقت، روشنگری و امیدآفرینی در جامعه باشند و با روایت مسئولانه واقعیت‌ها، در مسیر اعتلای ایران عزیز و تقویت سرمایه اجتماعی کشور، نقشی ماندگار و اثرگذار ایفا کنند.
🖋️
اسماعیل للـه‌گانی
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/455030" target="_blank">📅 20:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455029">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/455029" target="_blank">📅 20:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455028">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZD3MuQF6I2pjclfm51lPWoOv5wYIkLdGv1HUVP7EiQ_bTQjSh1P0sxi7gMLgZUNlrBcmqWvledCJkPdS38julllkH7RW_1R6At4Lyrti_vH4HI1aM4ET6tzGCT6tr-p3kqmGBSd_WqNS40XWm-b2EfMx9BTOhBmN536cn402JGWRbS9cKKyQJCYNIotygec3iyQOGpK3Nuw9udu4phNjQ1gGeVQl5usspDmszhWgMsZ1NQOy3UskTph4PiXHp9YYlBZxbY8SlskdXQW1IvIcIGFgFGqLbCdA1tKHTyqH-InXJcbGCmKjy7S-kPcq219saFqg3t339AyQLUB52izlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج نظامیان آمریکا از یک پایگاه در اربیل کلید خورد
🔹
پایگاه خبری المعلومه عراق گزارش داده که نظامیان فنی و مهندسی آمریکایی مستقر در پایگاه حریر در اربیل عراق، درحال خروج از این پایگاه هستند.
🔹
طبق ادعای منابع عراقی، بخش عمده‌ای از توان نظامی که در حریر مستقر بود، به پایگاه‌های نظامیان آمریکایی در سوریه و ترکیه منتقل شده است.
🔸
این پایگاه در طول جنگ بارها هدف حملات نیروهای مسلح ایران قرار گرفته بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/455028" target="_blank">📅 20:33 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
