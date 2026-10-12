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
<img src="https://cdn4.telesco.pe/file/V1uvVkVjPhzIzVe_4cH2W2mzqx5_hUb8lnvVrUvX-cIEqPF05G6uOOsrlghlDZ4wSMPcayG3CmF26fvxeS1gZ7NYWLksjDolORfQ137kvYMU1Lz4NXJ2KDAPM6iBWWrfZSYlT1Xz0S5iMvZAf0q0yd8itJ0p35yNYNzLX7M0lgX-OXLIMz8F4Kq4zlVjOoqMw_TdtqZJGBUNylTA9Q9ru63nScS8cxVE1T4srZ-a08-vBkQ0xg5uaFMSwrAseE1boaIDgY0S6dW4RZ6Uhnw7FQWeET2jPIEdtl_8ZOnhfBtDt7tvp4N5Tfwn9gatKzkE9b8E02xhYjg7zX9YQMLxzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 03:10:30</div>
<hr>

<div class="tg-post" id="msg-468074">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFp8XJfHJAXq28VsYYekZakOwrZQ4mtBtrqWwdzlx4VKy6fS1_iQ8ZhcZqR3_YgQsrWsx4FU5P7tiu7F8S-txdxl2Hholp-4prkkMmdy4FYxkMHyWdZJQR9gRlOx4wlCFqIeLWbxjEaGR-MQJgpAiwjZAU0V3GdjzzKMJlWWx_4CemGxy1mnehNyJ7nolht7FggQ8FQlYvdJAt1_5TwfRJIt44bs56AtAx4wI6xnWbhruJS5VPwkReqaM6RWSfXXvCtTipsIPPGwUkp-zS0medBNnoRZRIEXWIPoZ8IAwHslzgIcHduM4TyOg52yySzAdEG12ugayHwhkRrq4W6dEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرهٔ‌شمالی: موشک بالستیک تاکتیکی آزمایش کردیم
🔹
رسانه‌های کرهٔ‌شمالی اعلام کردند که این کشور یک فروند موشک بالستیک تاکتیکی را برای تأیید موفقیت در ارتقاء فنی یک عنصر مهم و اصلی، به‌صورت آزمایشی پرتاب کرده است.
🔹
در این بیانیه تاکید شده ارتقاء فنی این موشک، یک موفقیت بزرگ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 298 · <a href="https://t.me/farsna/468074" target="_blank">📅 03:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468073">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S212u9Q53NXUjoB9rHw03vwwctRUw8UI3tA9qKL0PFmsPXRVXe5ZoY9cWiEfzDYA6QRHMpZnTloAQrCY0dd68xmRSizJPV6CNcKsOrj2Ig1O5NDpl9Rq7Z1FLh8BuF6w7lU9uj7YQLJ3Ux33th954rNhLTMKQD30rsOx2J354xqQTNGo8o4DoX2eOOiz7jlnaTIrDt9JtVffPQjbGHDjsLcU49t_ktyeG8HrFtOCV9rdKvKakBticXeYVSnyEu1bOMsC3UB9Yc4DLqfre8dIg9FTYH02yBtpW8TBfcq9ZHTxgcxIrRj8vcsoECkw3hl5PujQH4uXV7NWaeb5H6iIZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمایی قطر از تعلیق تمامی پروازهای خود از مبدأ و مقصد فرودگاه‌های ریاض و دمام عربستان خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/farsna/468073" target="_blank">📅 02:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468072">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwlFpm0dk5LlqWsYcx6F4DMZXduDC1_UCawLO81c2ct3-ymMnCfPjatt9p64Dz0q-JEaCrfjKpuf_4XVfJbDs1d5DITTpKYoz3jkwtfatbx-Kl7C4eXnZ0Q0R4-8B0CiWDN6EVyxA6vBnIeOztIfm6VPzMi8M6Dy1bvHqC_jWI6OJJxXnpi0yhZmdCpzdBBobyglZ1FWCnR7rG6KCqmxt10AtNdXp9zHjtzNNI_VTCJdNVDrdEmf9Dft869T9uukDW6BFSkwtOY7KMILq0m4eH7fx2_mMURZem8UyzKhWfFk9yko3k1OlqvWh1BhZAnpQpB9pN5SqDVrmzeW05VQHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: بعداً برای بازگشت به مذاکره با اوکراین تصمیم می‌گیریم
🔹
معاون وزیر امور خارجهٔ روسیه گفت مسکو همواره از مذاکره برای حل سیاسی و دیپلماتیک بحران اوکراین استقبال کرده و می‌کند.
🔹
وی با بیان اینکه اقدامات کی‌یف در جریان انتخابات پارلمان روسیه احتمال از سرگیری مذاکرات در این مرحله را ازبین برد، اما موضع روسیه تغییر نکرده و مسکو با درنظرگرفتن چگونگی تحولات اوضاع، در آینده دربارۀ بازگشت به گفت‌وگو بر سر اوکراین تصمیم خواهد گرفت.
🔹
به گزارش اسپوتنیک، شش عضو کمیسیون انتخابات روسیه در جریان انتخابات پارلمان، به‌دلیل حملات هوایی اوکراین کشته شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/farsna/468072" target="_blank">📅 02:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468071">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حملات رژیم سعودی به مناطق مختلف یمن
🔹
رسانه‌های یمنی گزارش دادند که رژیم سعودی در حال هدف‌قراردادن استان‌های صنعا، عمران، الحدیده و الجوف است.
🔹
وزارت بهداشت یمن نیز اعلام کرد که تجاوزات رژیم سعودی و مزدوران آن از تاریخ ۳ سپتامبر تاکنون، ۳۸۵ شهید و زخمی برجای گذاشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/468071" target="_blank">📅 02:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468070">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تلاش ناتو برای آرام‌کردن روسیه پیش از رزمایش اتمی در ایتالیا
🔹
پالتیکو: ناتو به دنبال اطمینان دادن به روسیه است مبنی بر اینکه رزمایش‌های نیروهای هسته‌ای در ایتالیا هیچ تهدیدی برای این کشور ایجاد نمی‌کند.
🔹
مدیر سیاست هسته‌ای ناتو ادعا می‌کند که هیچ دلیلی برای…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/farsna/468070" target="_blank">📅 01:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468069">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/farsna/468069" target="_blank">📅 01:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468068">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P14Q6jTLnJ3vD3lQk59vx2V4Q42TjDVLI0jq45gCKKM-XrRtIZ7mCgpxGqYQBUeyDU1Cd3WPInIKPbqz7qZTvdleZLcXSafG1vdTRNWmwT9wUht0O_L3A_TrbsJikddo8UN2c2uWGiU4lQJ-IrbcjhLT1W24DgdHvsD6mDiSixQkIgS-at0k9eHXYjrjIBSjm5YZI7SMIDrYP6hBVmlIwGG2dLAcS80ZUUIUh06ZGLquiWikCHZm1mAqLFspQmi-jGnobQ4526gLXEFmEwqnRJbB2xaBFzL-Vo8JmF_m8dwZKLNJ5q5gRN6RTh7MNUAwZmU4asMSix7yf973uwOydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ هکرها به یخچال ۱۵۰ فروشگاه فرانسوی
🔹
حملهٔ سایبری به سامانه‌های سرمایشی فروشگاه‌های زنجیره‌ای فرانسه، باعث افزایش دمای یخچال‌ها و فریزرها تا ۵۰ درجهٔ سانتی‌گراد، نابودی موادغذایی و وقوع آتش‌سوزی در برخی شعب شد.
🔹
حدود ۱۵۰ فروشگاه اینترمارشه هدف قرار گرفتند و موادغذایی آسیب‌دیده برای جلوگیری از خطرات بهداشتی دور ریخته شدند. کارفور نیز از آسیب‌دیدن ۸۰ فروشگاه خود خبر داد.
🔹
رویترز گزارش داده که مقام‌های فرانسوی یک آسیب‌پذیری در نرم‌افزار شرکت دانمارکی دانفوس شناسایی کرده‌اند. ارتباط این آسیب‌پذیری با تمام ابعاد حمله همچنان در دست بررسی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/468068" target="_blank">📅 01:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468067">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مجاهد خطاب به آشنا: خالقان «دههٔ عبرت» نمی‌توانند داور تاریخ باشند
🔹
مهدی مجاهد، معاون دفتر شهید رئیسی در روایتی از مذاکرات سال ۱۳۹۴ گفته بود ایستادگی سپاه پاسداران و دستگاه قضایی در پروندهٔ جیسون رضاییان، زمینهٔ طرح مطالبات ایران در مذاکرات تبادل را فراهم کرد.
🔹
به گفتهٔ وی، این مطالبات شامل آزادی شماری از ایرانیان تحت تعقیب آمریکا، رفع محدودیت‌های برخی دیگر و بازپس‌گیری مجموعاً ۱.۷ میلیارد دلار از اموال ایران بود.
🔹
مجاهد همچنین گفته بود که پس از موافقت رهبر شهید انقلاب با پیشنهاد مطرح‌شده، بر دریافت کامل مبلغ مورد مطالبهٔ ایران تأکید شد.
🔹
در واکنش به انتشار این روایت، حسام‌الدین آشنا، مشاور حسن روحانی در دولت‌های یازدهم و دوازدهم، در توییتی نوشت که این روایت تنها حدود «۱۰۵ درجه انحراف از شمال» دارد.
🔹
مجاهد نیز در پاسخ به این اظهارنظر نوشت: «قطب‌نمایی که کشور را به بیراهه برد و دههٔ عبرت را خلق کرد، نمی‌تواند داور تاریخ باشد.
🔹
انحراف، در عملکرد آن روزها بود نه در روایت امروز که بخواهد در مقابل طعنه، سر خم کند. ای کاش قطب‌نمایتان را عوض کنید.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/468067" target="_blank">📅 01:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468066">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ec01f669.mp4?token=YN8HngA7tpjRj0ka0jnvxr8A9i4LG3vL70ngTtclk6X8gSdOQLLfJ4uNNcd-yBS6DCF34z5XYKScYvKG2B3xPeKK7iztNXVBm5xSkTRL6QLKSUs8SDFA55-BcFyL6cXxMmbKIGmlUpng5l-Izl_pPfwKKBdvOj0IIqAHo660ZYpZ0HffzGSEpMmegQJXE0oq5cuLhgC7P3H9Km-QZ1M2c_ndOa5M36hFqu-nfo8aWwdyb4ZqyXuTfc_o6O8KW84lp2YroWA3DjgPA-Eij73paaLQMVavOKcPZ0qEFkZthdJXIYuPUSpRPbMurTmuobmJ7VO8LVDaQxDKmuMBFZYVKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ec01f669.mp4?token=YN8HngA7tpjRj0ka0jnvxr8A9i4LG3vL70ngTtclk6X8gSdOQLLfJ4uNNcd-yBS6DCF34z5XYKScYvKG2B3xPeKK7iztNXVBm5xSkTRL6QLKSUs8SDFA55-BcFyL6cXxMmbKIGmlUpng5l-Izl_pPfwKKBdvOj0IIqAHo660ZYpZ0HffzGSEpMmegQJXE0oq5cuLhgC7P3H9Km-QZ1M2c_ndOa5M36hFqu-nfo8aWwdyb4ZqyXuTfc_o6O8KW84lp2YroWA3DjgPA-Eij73paaLQMVavOKcPZ0qEFkZthdJXIYuPUSpRPbMurTmuobmJ7VO8LVDaQxDKmuMBFZYVKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: رابطه‌ام با کیم‌جونگ‌اون خوب است چون ۱۱۲ بمب اتم دارد
🔹
رئیس‌جمهور تروریست آمریکا: من ارتباط بسیار خوبی با کیم‌جونگ‌اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای دارد، خوب است که روابط خوبی با آن داشته باشی. اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/468066" target="_blank">📅 01:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468065">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBl_909zmMAjarnJd__Z3QYncmsDNOe4G_02O4QFc5D3zYrtnJdi0ArShP2kiEZ-pyVSfDlc7Xle0syvF3zTeBuyjAM3HvukqDCSckjVOAaCAeozYDT_YyyfGObXUYDGNsKIN3utbqijhz-FB7LReXPq_6ag6PkoegNzaW2I5Ubar9K8jrnluedlGK0Ejntbd9rA_5v0TqUoDrQ2rsKpCb0JUoVTAjZeVh8hfiuhfC3smVu9WNut4m1iTP-3C0QUkXDqL5X7Sf8W0dhzBvJIVv0erkm636VV3V1hzp_BWRFiR0wN2EeZyXBqQp0sKQVQJMFjmyGP08Lem2xfpWonYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
فرماندهٔ کل سپاه: هیچ قدرت فرامنطقه‌ای حق تهدید، حضور سلطه‌گرانه و دخالت در تنگهٔ هرمز و خلیج‌فارس را ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/468065" target="_blank">📅 00:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468064">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آمریکا دربارهٔ سفر هوایی به عربستان سعودی هشدار داد
🔹
ادارهٔ هوانوردی فدرال آمریکا و وزارت خارجهٔ این کشور با صدور هشدارهایی از شرکت‌های هواپیمایی و شهروندان آمریکایی خواستند هنگام سفر به عربستان و استفاده از فرودگاه‌های این کشور بسیار احتیاط کنند.
🔹
براساس…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/468064" target="_blank">📅 00:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468063">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e1e3a7b6.mp4?token=q3Rf5aWp-_s30Wf7X6Jxd_rhXJjXcBlQBxYVt9YKYIvly88V82gAssqtlkEc4OyfyyPJglc3DwmPP4s5hNmvZfb4xVWIP6hzX589ErVYduOVioL5oMQxmaLgXinmECx6exOt9HRgRIXmhuqV9A269ptXYrUzSng8akboWv1kVWD8xF-YJ0KBdrraXfqGUpKzagVJvkiU7NhEkrOWu5JJ74HcFTR11F4Ub0k6yNR9CxlNMcK4ixyUGM_1zExQAZGTktj00XQ2KG-8GhUOlYa1TUYC4GvG6HyJyI0yrJqib2CTBS9QkfufsSlNknm_D53U9-yOpr7Ymvt0_UpiZeE2Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e1e3a7b6.mp4?token=q3Rf5aWp-_s30Wf7X6Jxd_rhXJjXcBlQBxYVt9YKYIvly88V82gAssqtlkEc4OyfyyPJglc3DwmPP4s5hNmvZfb4xVWIP6hzX589ErVYduOVioL5oMQxmaLgXinmECx6exOt9HRgRIXmhuqV9A269ptXYrUzSng8akboWv1kVWD8xF-YJ0KBdrraXfqGUpKzagVJvkiU7NhEkrOWu5JJ74HcFTR11F4Ub0k6yNR9CxlNMcK4ixyUGM_1zExQAZGTktj00XQ2KG-8GhUOlYa1TUYC4GvG6HyJyI0yrJqib2CTBS9QkfufsSlNknm_D53U9-yOpr7Ymvt0_UpiZeE2Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الغرافه دومین قطری قربانی استقلال در آسیا
⚽️
الغرافه ۱ - ۲ استقلال @Farsna</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/468063" target="_blank">📅 00:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468062">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
توقف فعالیت فرودگاه‌های ریاض و دمام عربستان
🔹
منابع عربی از شنیده‌شدن صدای انفجار در حومهٔ ریاض، دمام و خمیس مشیط عربستان سعودی خبر می‌دهند.
🔹
گفته می‌شود فعالیت فرودگاه‌های ریاض و دمام در پی حملات ارتش یمن متوقف شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/468062" target="_blank">📅 00:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468061">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQhxIZylIdKU8g4N37GdPFwprEbJ0x5p8IreXKEF_BPuslQqvwb5W-w2_EbfGP_aao4LaeHR4hHow_dZckMTKu_-QKg916SMuO_AoU8tuvzj4SBtyh8EvHFjwt2jx3aQbbW_qP8Ai9JgDMwuFt-iOfQwqwOMVlbtwA2TZuH9D_ZR6UiAQKMd5PuGRrxTfg_WgFtVCTfI1eImE3-NPTKWpkiknfkeV2eJltDP9KjIkqkZVIFUtdDwv6RzeK5KJfOC3niaoYCBl25oGDc-1cdxFzr3uLtwees8e1qf5WhN42bDWSnnhU1wBnEX3ABRcWGabJO6y8Sf3t0bn6Y3Z_TJlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت‌اندیشی نابجا
🔹
روزی شکارچی برای صید بیرون رفت و آهویی شکار کرد. لاشهٔ آهو را برداشت و راهی خانه شد. در میان راه به گراز برخورد که به او حمله کرد.
🔹
شکارچی تیری رها کرد و بر گیجگاه گراز نشاند؛ اما هنگام زدن تیر دوم، گراز در همان دم با زخمی مهلک شکارچی را از پا درآورد و هردو درجا جان سپردند.
🔹
گرگی گرسنه به آن دشت رسید و با دیدن اجساد شکارچی، آهو و گراز، غرق در شادی شد و با خود گفت: «روزیِ فراوانی نصیبم شده است، اما شرط عقل آن است که به آینده بیندیشم و زیاده‌خواهی نکنم؛ گوشت‌های تازه را پنهان و ذخیره می‌کنم تا روزگار درازی بی‌دغدغه باشم و امروز را تنها به جویدن چرم و زهِ کمان قناعت می‌ورزم.»
🔹
همین که گرگ دندان بر زهِ کشیدهٔ کمان گذاشت و آن را جوید، در این هنگام گوشهٔ خمیده و فشردهٔ چوبِ کمان با شدت پرت شد، بر گلو و گردن گرگ کوبیده شد و او را در دم هلاک کرد؛ طوری که هر ۴ موجود در یک‌جا قربانی مرگ شدند.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/468061" target="_blank">📅 00:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468060">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZjdWvrvKdkEA4EhgmRbZQQML2Lznllg5n_tv1UNwjfXTWrjVB3Fmg90h20Qdm22HVngwkEXs_O_cXeaLJCvYiuin0E3KApB_Mb55KhETMBPCy9jtnEX_mIULTaKooXkHmJgrs7qEOr7F7guSKe_jRUfkmGxqkW3938dema0y9y7tlW3_gvkw7jlNm97ZSGA39ucsB1vW2-0UgS3zHd-K-Dd7t5YkgVdShib4d5Nu-4_7bFUPaqZXZhH_UUbaLJz2MFWw9MrpRxirAF5eB32chRTixeuy063s4ERVXcCOiADx-LYjxJvOR-gyKJvaSS5fac0qy-AQJN2NSWh6AKV_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/468060" target="_blank">📅 00:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468059">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPo8vLWzDrKmghYLRQZz45X2l0PUDEvJBCLwAeTp-2wPxFNSR4o_E7UxrdosHsWzdm7dsFg6z8GMAUfIJruP9HJirbau4ku54Ctp2g8w02yHOCOp-KO_ffEgpHc9teQ1a5n7wRFTYYDQVjZQaTdXP90QHGrwZPdddNMtGooGr76HdVXdTyoMixDYTZkYHfQiAniqT04YP2lS2Xr2EEratNs58_SQdl5bEW4vVKWKswSNZW3D4905eHB7tH4Dg4wVaSS2ClTMhzR9J3F4nPUZkmB8a9-_fKHcwlL41JPdinrLL02SU4N8_yGFVhW-Rw-Wn42UquK3LGL_qulLRcvmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانشگاه آزاد خواستار پاسخ‌گویی عاملان حمله به مدرسۀ میناب شد
🔹
بیانیهٔ استادان و مدیران دانشگاه آزاد اسلامی به مناسبت رونمایی از یادمان شهدای دبستان شجره طیبه میناب و یادمان ۶۴ شهید دانشگاه آزاد اسلامی واحد تهران مرکزی در نقشه ایران عزیز منتشر شد.
🔹
در این بیانیه آمده: ما استادان و مدیران دانشگاه آزاد اسلامی واحد تهران مرکزی، بار دیگر حمله به دبستان شجره طیبه میناب و هرگونه تعرض به مدارس، دانشگاه‌ها و مراکز علمی را قاطعانه محکوم می‌کنیم و معتقدیم، هدف‌ دادن محیط‌های آموزشی نه نشانه اقتدار، بلکه نشانه ضعف، استیصال و ناکامی آمریکا و رژیم صهیونیستی در دستیابی به اهدافشان است.
🔗
متن کامل بیانیه را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/468059" target="_blank">📅 23:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468058">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1bd45021.mp4?token=dYq4hBddyVnA6ShW-rL4gLLbolsFw7L-dHVh2sIWz_rVvVPRNStPXly030C9Jmj2qTJdV2SP1Q6gxkyzovRkflIPv6YS9UxkxtBEAC190L4-H60iHrSF8b9WFxCSeT-D0dK2UTk8VHckjPtlKR-49MyOVDYf_sGhkkF23Q8YM53PWHAJwzyXffDvgwQsPCL8Oo26k5MwSDX4-j5aE-il5OrVBi3mwqo4QFDRmPcHc44RE_ADaKXC-F5Y13r-6fTeE2sVUeZJr54RuHK_rMAWIqb6Uh5AnNGVimmSrYPY7qc82B-uPYEIYXV-SCEikGLolrE4apnHFkR7cE_S5JpE5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1bd45021.mp4?token=dYq4hBddyVnA6ShW-rL4gLLbolsFw7L-dHVh2sIWz_rVvVPRNStPXly030C9Jmj2qTJdV2SP1Q6gxkyzovRkflIPv6YS9UxkxtBEAC190L4-H60iHrSF8b9WFxCSeT-D0dK2UTk8VHckjPtlKR-49MyOVDYf_sGhkkF23Q8YM53PWHAJwzyXffDvgwQsPCL8Oo26k5MwSDX4-j5aE-il5OrVBi3mwqo4QFDRmPcHc44RE_ADaKXC-F5Y13r-6fTeE2sVUeZJr54RuHK_rMAWIqb6Uh5AnNGVimmSrYPY7qc82B-uPYEIYXV-SCEikGLolrE4apnHFkR7cE_S5JpE5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس اقلیم کردستان عراق: جمهوری اسلامی با حمایتی که از مردم در این جنگ دریافت کرد وارد مرحلۀ متفاوتی شده است  @Farsna</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/468058" target="_blank">📅 23:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468057">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeTncS1jpjWCerbPB5yeG7YgWtkMD_n8hLWpBMn-upLlcnvd0w_UeV7dTkJhdOegSAodqM0BCx7IdNNIgRNwZ3AMeeJS23wP0ZxvaDxyg05Is6VlneOsQEDiL1BW6iH0_B02nsfh2DaZ-FfrVIJP7COzQdLWqVKmkmloYgx0lHbKqykX3McfdstumETLhRVxtmGDNO-RbFYyNUs7bfEc_wD25gQJCqUDR_w3qQx412-HV-59Dd2llWSX_N6Lli9Kg8-IJdCGB4bRvkvLMzSDa37v1Vcez85lrMlvYWnlEvpLH_eYVDCnxYkwqfZjUyjy4vToG22Yymd14eZ4FzuuKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
این‌بار آشورمارتوف پیروزی را برای آبی‌ها سیو کرد  @Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/468057" target="_blank">📅 23:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468056">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda9d0682b.mp4?token=ZjuKmYyYVvpApWTel_e_6w3Y8w5g2BL997wsPaCWXrU2iMa-7u8xVsXEGN1YVINdXiHzL9cfduCl6Bu94E3-944_9uOC4pi9rId6W2Q1gjSGQBaGHgRFq3WqDdQ8Nas97T4YBzhysAWlqdlmMD60htCnQHWUtRgm316oeSxPluQZHn9M9ZmpRBtilqBKD_bqg7Kbimq5EhwI9jzcNQI6njCWUTOkrKr1ikJ3n_Elt_yoKW5VSMfWwa1KAiLQuhPKaMVKbM76FlZ6yfpTvONlYdqRrQrpEGP7CyZilSi3JJqQSre89YWev-wyzLLiCze2rd9cm6F7uYpvgaloVJ1mYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda9d0682b.mp4?token=ZjuKmYyYVvpApWTel_e_6w3Y8w5g2BL997wsPaCWXrU2iMa-7u8xVsXEGN1YVINdXiHzL9cfduCl6Bu94E3-944_9uOC4pi9rId6W2Q1gjSGQBaGHgRFq3WqDdQ8Nas97T4YBzhysAWlqdlmMD60htCnQHWUtRgm316oeSxPluQZHn9M9ZmpRBtilqBKD_bqg7Kbimq5EhwI9jzcNQI6njCWUTOkrKr1ikJ3n_Elt_yoKW5VSMfWwa1KAiLQuhPKaMVKbM76FlZ6yfpTvONlYdqRrQrpEGP7CyZilSi3JJqQSre89YWev-wyzLLiCze2rd9cm6F7uYpvgaloVJ1mYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرعباسی دروازۀ استقلال را نجات داد  @Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/468056" target="_blank">📅 23:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468055">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2073a26d26.mp4?token=YHvMvE5qkYrEg--q1ruWzByZ8UGIzl5amQ9QBVHlg2avXEfiwVgIdLjDhoiSrjmFdIjy77NQfFn-e1ikttBGPGT8tQqzpiRc70qB-mhx85cp09BRv3fC8Wu6QxljwPZ34REo0W2cnPZI7km2jWuAbmPBtSBLKde2laKL6r7BwdmRO9C4DIw09GNex54Sn4hujo4sTFwOSNQDKEXHkMPlsWEfmrk-eFS1dQ-ACF-HVKXFfWFvXDSttfRX_rO-4e1jE7x7N-JLz6t2PBiaLXh0DrlFKqZ6XMQ5M-PSwY2nJ8-9tw3LJmAN5wL7iYHs-bHvVd0JkA2M0Z7AO5BKnDMeBA7MgLcxJ9PdZbsipWk1V4IrGItETyD5i5jzOKV3fcZLjbAoJtm0fWiWsrK4QStEGDzO6MTtcmtXSckZICWjUXvPyPLTcXdNaGhrz-xV2bfdmU4qY17AKXQNTYEkf_EGMmuPB6sG-Pya5ocNoIdHblHtmNFGrAPniNYha8qqNhPeCZOQN3-22x_hGVDK3pIhBATAe3ko2O-vCeF6wqB6mERVCGea5XUAgnqo6hR9as041y2EQjhcDZFVD4el-F31gD07nHrWR0t1UyUNCzIlyXAhH_9M1Pbzb1jwOhachblScHOHj1SMazWYG4RkChj4O6xrRCvstD_POhrkbW97OhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2073a26d26.mp4?token=YHvMvE5qkYrEg--q1ruWzByZ8UGIzl5amQ9QBVHlg2avXEfiwVgIdLjDhoiSrjmFdIjy77NQfFn-e1ikttBGPGT8tQqzpiRc70qB-mhx85cp09BRv3fC8Wu6QxljwPZ34REo0W2cnPZI7km2jWuAbmPBtSBLKde2laKL6r7BwdmRO9C4DIw09GNex54Sn4hujo4sTFwOSNQDKEXHkMPlsWEfmrk-eFS1dQ-ACF-HVKXFfWFvXDSttfRX_rO-4e1jE7x7N-JLz6t2PBiaLXh0DrlFKqZ6XMQ5M-PSwY2nJ8-9tw3LJmAN5wL7iYHs-bHvVd0JkA2M0Z7AO5BKnDMeBA7MgLcxJ9PdZbsipWk1V4IrGItETyD5i5jzOKV3fcZLjbAoJtm0fWiWsrK4QStEGDzO6MTtcmtXSckZICWjUXvPyPLTcXdNaGhrz-xV2bfdmU4qY17AKXQNTYEkf_EGMmuPB6sG-Pya5ocNoIdHblHtmNFGrAPniNYha8qqNhPeCZOQN3-22x_hGVDK3pIhBATAe3ko2O-vCeF6wqB6mERVCGea5XUAgnqo6hR9as041y2EQjhcDZFVD4el-F31gD07nHrWR0t1UyUNCzIlyXAhH_9M1Pbzb1jwOhachblScHOHj1SMazWYG4RkChj4O6xrRCvstD_POhrkbW97OhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رهبر شهید انقلاب از عارفی که در قنوت نماز شب، شعر حافظ میخواند
@Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/468055" target="_blank">📅 23:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468054">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_UEP8oMgBDN3bLw4p2f4FNcf7eRWLZ3bsYbjSyY_PTNfFgPMkkWOaXTYZe0SEfRhDY9hP5r0Mxk40cSKzjPp-QMS7o6uPbNdaILAnSs9N_sUSsR6xAEMM94lJ1MoH_s3E5x_O52M0Fh3UUN8WE1oi-Uet7UN4LMUHM1LBKrH5Cp3o8uH5ZQ8yi5a4ICZ1z7Hv-mpyVDXFOfBwzxvNnL5m-Xaic8hO_2rlEy8-QCF_DAuYoZgR2r0BKDcOUVT5zT5F10VE_owDiWkGFKIRMQO806Bqr4Elaty1tzBduKNq3NB0E4DyQ9pUTZKvr3T3VRjEmMIbctfqoyu6cpTCR_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصرار وزیر صهیونیست بر جلوگیری از بازگشت آوارگان فلسطینی به کرانه باختری
🔹
وزیر دارایی رژیم صهیونیستی با درخواست از نتانیاهو برای جلوگیری از بازگشت آوارگان فلسطینی، بر ادامه محرومیت ساکنان اردوگاه‌های شمال کرانه باختری از بازگشت به خانه‌هایشان پافشاری کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/468054" target="_blank">📅 23:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468053">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797670d791.mp4?token=m6u2SQUw07Vvq6T0FphhuPk-nHuy_vl6sh4jwPvAKWrS7c1Ac6IAii1yEa5T1rkODK_XMPO66xDFcKUdyyGFkHuCA9bodUib-mbmZxOfhCWmNdswtJvjehqLdFdDH0axmmqplUR--RsaKqeamPhO3SDoPtfdn6dmKewgzTY02KMfBGRdQ6BFDLBwxX1osFy2o9dprvCbd9-BlXvApGIp224kTjdV5v-UNWaNhcdsncxCneS4cNTwB8l7kaVA7qHJ5M6B0Uf4hAkgM0xlZe2aHIOwiMOmMaa0uI2aWqtWFVj817rUQ4bSBUmLQaWs89qVuEeh-ljdTPRFu062UkWPSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797670d791.mp4?token=m6u2SQUw07Vvq6T0FphhuPk-nHuy_vl6sh4jwPvAKWrS7c1Ac6IAii1yEa5T1rkODK_XMPO66xDFcKUdyyGFkHuCA9bodUib-mbmZxOfhCWmNdswtJvjehqLdFdDH0axmmqplUR--RsaKqeamPhO3SDoPtfdn6dmKewgzTY02KMfBGRdQ6BFDLBwxX1osFy2o9dprvCbd9-BlXvApGIp224kTjdV5v-UNWaNhcdsncxCneS4cNTwB8l7kaVA7qHJ5M6B0Uf4hAkgM0xlZe2aHIOwiMOmMaa0uI2aWqtWFVj817rUQ4bSBUmLQaWs89qVuEeh-ljdTPRFu062UkWPSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاسر آسانی پس‌از خطاهای متعدد بازیکنان الغرافه مصدوم و از زمین خارج شد  @Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/468053" target="_blank">📅 23:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468052">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO76tpuQxsURboq-vwhtOlvEh6wc4kUDek0wlBWrSQEMuC9XO3jEMxWi_fzVst9Fb-8E50_4NMGOB7rqAcX3Om0pd5eFx5-3UyyZ5WhpaB30hSaxC07B8sGQB050J90aMfuEBRtqPOuV2oqeEqnhH5YcyshjiQ0NoiEQ0KeoHY4SY0sbNnnTJA47UIppyZLt8LCnZI3tM8qyw2OyfZlgkX7xPNSmzXE5hfNre5srN98nrbsr_rrKhEfoYjts1TEh-1AriYlV4U7lVviJnWd6VruxyQ9H_O5KG9aw1139ADGrT6Cy1rfcIlN_8n9YM0K3ic8AeDYwAM12GC7Zm9c8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا حرف‌های زمان عصبانیت، حرف دل آدم‌هاست؟
🔹
خیلی از ما فکر می‌کنیم آدم‌ها در اوج عصبانیت، واقعی‌ترین حرف‌هایشان را می‌زنند. اما واقعیت این است که در بسیاری از دعواها، آدم‌ها بیشتر از اینکه احساس واقعی‌شان را بیان کنند، به خشم، ترس یا دلخوریِ خود واکنش نشان می‌دهند.
🔹
کلمات خشمگینانه در کشاکش یک تنش، اغلب ابزاری برای تخلیهٔ هیجان یا سپری دفاعی در برابر آسیب روانی هستند، نه انعکاس دقیق احساس قلبی فرد.
🔹
برای همین، هر جمله‌ای که در دعوا گفته می‌شود، لزوماً حقیقتِ احساساتِ طرف مقابل نیست. گاهی پشت یک سرزنش، نیاز به دیده شدن وجود دارد و گاهی پشت یک حمله، ترس از طرد شدن پنهان شده است.»
🔹
پذیرش هیجانی و مطلق کلمات پرتاب‌شده در مشاجره، رابطه عاطفی را به سمت فرسایش و سوتفاهم‌های پایدار می‌برد.
🔹
اگر هر حرفی را “حرفِ دل واقعی” بدانیم، ممکن است زخمی عمیق‌تر از خودِ دعوا به رابطه وارد کنیم.
🔹
مهارت کلیدی در حل تعارض‌های زناشویی، عبور از پوسته ناآرام کلمات و شنیدن نیازها و ترس‌های زیرین است؛ پیش از آنکه قضاوت‌های شتاب‌زده، فاصله‌ای جبران‌ناپذیر میان دل‌ها رقم بزند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/468052" target="_blank">📅 23:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468051">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp3G1zGAdGdZlmPBAuoqQn0_Wu-peOF9Bvs4rR9-lrIaA3Z7ceD5b8bJBmbt95KXu-oWzqJx9qZU4NbjuSwUVb07cAHTxqOlINSp5YVC2Lj4Ks_am88H_0yTuKZPDpDcMQi0A79Rz_vmUX-Box_9JpWJc7xhoLC2uPoTjO-NECakmzYTS3C4gJvOYbNaxZSF0moU9iKecDMUpiikawo_XHaKSVNcqLMBBVN_RxS079cyUTh8un61j-On6CAJmZhyNwlmSpgaw-hyBxNMBo_0QgWFkvcluw7_KHFuMoRO0jGlDHPgy2aliyuqUEwMPaiwLfeVo8GO92D7kVtRgGO8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای انتشار فیلم قدیمی کتک خوردن یک معلم چه بود؟
🔹
بازنشر فیلم قدیمی کتک خوردن یک معلم با انتساب نادرست به تبریز، درحالی خبرساز شده که بررسی‌ها نشان می‌دهد این ویدئو مربوط به بیش‌از ۱۰ سال پیش و یکی از روستاهای استان لرستان است.
🔹
پیشتر نیز این فیلم در سال ۱۴۰۰ در شبکه‌های اجتماعی منتشر و اعلام شد که متعلق به ۵ سال پیش است.
🔸
بعد از وقوع این ماجرا خانوادۀ دانش‌آموزان برای دلجویی به منزل این معلم می‌روند و این معلم نیز آنها را می‌بخشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/468051" target="_blank">📅 23:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468050">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsarrRI-bI-ftxRv6Nn0pTA_2E4WWlEqOOP6bkQAd3y-jT0ESRulgONwl8klvV9YDD2CdvvKP2hZTl_ryqQA4_h1OjPhGo8lTBm-SoWS56YIgbxqcwPj0V1O4h-RR2imeasolc7YgeAjLJr_docOJnuFKj6mnIfvV3s7L-qrU4J-gOmbT5Y6VWE9fDasLEefjAVKbgWC-_ioSPvAiSTLaHquSFjZiHkBtwgp4at7azwdlGAZdtlA_beM91NP86EPraTXNgelfOthCy_MvQXda49ZaF105VL7ywiKDUT9cVwK9Oa9pmc11nsELFGCOO8ExnVq3eLp50fBF1S0glv-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  جنایت مزدوران سعودی؛ شکنجۀ اسرای یمنی در تعز با سلاح گرسنگی
🔹
هیئت ملی حقوق بشر یمن: صدها زندانی و اسیر در زندان مرکزی شهر تعز، که تحت کنترل مزدوران وابسته به سعودی قرار دارد، چند روز است از دسترسی به غذا و آب محروم شده‌اند و با خطر مرگ ناشی از گرسنگی…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/468050" target="_blank">📅 23:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468049">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4838d8be2b.mp4?token=B0TF1QfrG5N1Pmy0fC560MTLD6BjLzwpNN2i6TLiPFbvLmJWZF1Kvw9er8ihAMz8Sxn8A-lkK1xuOUDycmBpkqtt9JwHJkETztaLaF9EIc5lu5lMrXTB8dF0mpmb1req6GRR-8Dq3t0EmrtoIPpb2nVhmpO0mQ_qD00aJ04BVN49nLJQ2ARuVpOyXBL9ZfzIEschK1-N6MILufstNcxa87VjrkeYQ3DDX-OeeYB0nQyuH1_WyxNO6IeG0cGCmaL0w0mrTyXJ_gDoGg8SMbv7rhJk8f2vtBl-qlZKkGPSopnus-fUl2z-x5isTxdbFhgaKEFmX-0Z6KkDF2ZfWxAqxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4838d8be2b.mp4?token=B0TF1QfrG5N1Pmy0fC560MTLD6BjLzwpNN2i6TLiPFbvLmJWZF1Kvw9er8ihAMz8Sxn8A-lkK1xuOUDycmBpkqtt9JwHJkETztaLaF9EIc5lu5lMrXTB8dF0mpmb1req6GRR-8Dq3t0EmrtoIPpb2nVhmpO0mQ_qD00aJ04BVN49nLJQ2ARuVpOyXBL9ZfzIEschK1-N6MILufstNcxa87VjrkeYQ3DDX-OeeYB0nQyuH1_WyxNO6IeG0cGCmaL0w0mrTyXJ_gDoGg8SMbv7rhJk8f2vtBl-qlZKkGPSopnus-fUl2z-x5isTxdbFhgaKEFmX-0Z6KkDF2ZfWxAqxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم استقلال به الغرافه توسط گودرزی در دقیقۀ ۶۰
⚽️
الغرافه ۱ - ۲ استقلال @Farsna</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/468049" target="_blank">📅 23:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468048">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e4f6c8db.mp4?token=W1xHr5rXIOooUvtKIFIBZcysPVb9aUYoVbJTd4SphZoL2OhEY3GxIzvhlH-tAx-cw5wUBk2U5_CZYNeE41g8-9V2EwCakAZfF6KmDWUPytscJ79Rjl3fSCxnLEg_L09_Ul0gkQnnWVAccwfmVjf5EVU4NKdPDrsJEiQzQQvHvkOITWUQttzOummYR3DE2xDJH7dC2XElfdxsNyhkWGVOTkiIfUeRyKmVTL_zUkgSEIYFTLVdGOSPF5XvLzjZKxR-rKJ0jwBCVrkWM3NwimYU95Vin4Xi6psxxnyWMYBABfNLnK72tcOklyw2eCGg__r1cWIHGXJN2PhnRzqTG0hIXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e4f6c8db.mp4?token=W1xHr5rXIOooUvtKIFIBZcysPVb9aUYoVbJTd4SphZoL2OhEY3GxIzvhlH-tAx-cw5wUBk2U5_CZYNeE41g8-9V2EwCakAZfF6KmDWUPytscJ79Rjl3fSCxnLEg_L09_Ul0gkQnnWVAccwfmVjf5EVU4NKdPDrsJEiQzQQvHvkOITWUQttzOummYR3DE2xDJH7dC2XElfdxsNyhkWGVOTkiIfUeRyKmVTL_zUkgSEIYFTLVdGOSPF5XvLzjZKxR-rKJ0jwBCVrkWM3NwimYU95Vin4Xi6psxxnyWMYBABfNLnK72tcOklyw2eCGg__r1cWIHGXJN2PhnRzqTG0hIXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل مساوی الغرافه به استقلال توسط ساسی در دقیقۀ ۴۸  @Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/468048" target="_blank">📅 23:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468041">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iDEqvQ2CIH5XQslE_EfdMkLxk762yPgK_zdNshtqpBGLUA0c7DHXhzwqY7BQmglT-gFMGrhOo5Gqnm2pydecQNUC3JZ4vf8oYJBJOUAvEd-t2Qdo8KHSvY9JDws3IZj8WA9hob6c7F4U369jdpXpMqiNfm79s5nLyGDjc2uPFtn6loJL7obq0mxA2YtsaitSgYsUhUnXGHNld7m1xAfcYDBD8oRkIVcqwTmChL5NTigJzIDJJtT0Yd6lw4LtJqaQwDvU_OxcZjXS5_H7QzIfVmbqsm1_nlDV6uCvoIGvZZFy5RlNbWbM4NHs3TaE_T11yv8LXr9N_0mclEc8ol8NdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAQbU5iGt-rN1msCKYoxWZoOFqzLLa9UQAru5dy1oOy2Bae3WypXVsUo3J9vphtSmEQnSqeAHsYzubKEnvKQ1mM8wyhapjvjhwUh-JJvKjJRYJFcaoi5qjBdmHqeYwB6HVF238nXL8fHqQdHpqfAmXI4fhC_8rZ-ZU3RrAallCJWRQkRL_dla-3GnGztDBMCvgR7E3xwWdEv5HUWqtHG2y9wEsItdAswR8R9jgjVKmM8Q6bfPexTAEU0vnYiMa0EhPG34kISYHwu2nOG91ryfXAA5dKtjVOwKk28pcQGSwsP8wpDlOloeOHiJcG_-m2qelPxx_2JotSV5bhsoOhDDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IE1nQiV8W5ooo831C9wkX2GvKl6V2LJcBSZJ_0fV1vuMvzGGP-WhqMtnkeK8xQ3_v9tmuqXJGhmKoSB6rsmSP_CWyGeNRSWO6HSfC7skE3sskNdDCCAI6X7k1mKQlknR0n5zh_Qb9wFLiGJRqS_-chBZ1tRnfFPXmX5aegadqyhaWG0Lgf7kZAfFWlyDj19caGQ6Iz6GF43SGQsmKmrfMHphYuSkqApNgFyouARJZrfqbIa4JI6yKf2jS8JG6LnvBgT712Kw1PDhMYPJIHqW7CgJsSAIBYdFayZisnD_erlDm5aXzXL56ZPf_skfaHNGdU6PTBKq9VMo_lgfyO9DxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqLNlPWDLfnXOKhy66qhhPTiKYpRd43XhYWS_lVrX_pcAN8X5esR1ciP-1gvCSNRPJ8l_lke0PYJzWsRQqrsSrBxXk_Z1iE_5Dk9V9FI1Hts16MKtidHumbmEYoFDG7Kmm4HGKLoUbqNmWjyLRaIJf6YuE3AnIP7Q8Evy3njGfja2yFuwLZQPVACosrKM9YPlMHuagfhS1q9X9IQGCGDVX45OzsWckO6vK77wbg--Sd4YD1VmBuvZPifipxC0Za7C1EWX4_Aj_iCzFpx7Q1lpDjLobcctx-bKTUZRd-dqeP-b-01sqltVcTsjzfdNEWGVZbAUL3rwZ0KancPunUFqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUVgmQBMJgr5fBovk26waG8yUkjKROnXJh637eyT80Y3y_jK-bG5lC-Xb_W1VP7-hNy7Q_Vtn5vOlP7hy4j1pA7h0Chpsa_64rgKGdAYX68wQdQ3Y1OvRdKy1m4n-_GVzGp6OQ5rSe2OdrU2vbvpHQc4aJZOWE7QMkwzUC58Vf-qXD4xZyHJmTTJXFdM3_3f91loStN94sySGGYMMd-LL_UbFgGIjEj3oobj0N4qmflTSdo93b1Tanm-pF834PLTS6hjFcdIIgtW4hJdgLuhMECWb0aa24hSOrvYTkIDNc1YW3_21V6AsZ0tou-MJO9drfBOlSyCoEVpq_zQuQa9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LU6mGVDitCZM4-MVUpSW_cipCEO71sirz3iINAprEI5d3YW7sfod5VasjVaMSfYG_ijnJZJHWPpGne2unB-_8h4qM3fVNJsHXKmlWymeqfYED_roK41SdCt_5XpUxjf8p23Z0lKho_Y-iKDakxFHMR_mxmVPap_DGQJMO9JVQJaXOZMRArcpoEo8tJyeDX1kkR57MdWkZLi2Q0afRiaIOjfgUje12Hqijx0slKHBzBXESyzh0_2q5eaheMMLXie9S-PhFbyOt4xR1f3lsCpAjYzZL8nCF4r8kApROBstXaHn11RLyAvJP9JA2P65unkIk6t5ogcQDMB9EtkfQmnLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btADuFgq4Mca5gtAA-I-Q9_H2MG-oTyvrqg1Nlyp59lGDUSgYDUCcTITPtc6Trx7DM6fhhO2pyvNkWHhPzfCH8IyUxfVQNvWzJe0LbSsF-kPEn0dE9wGtKio6NfCSI237BwAaj2uCvBDQDUs8-L0deXb1bBDFvkluEBuQPziTX2lBPdcomUksmo7BRVGD0A6Tic2B2HvV3R9hfCIkldl5TVmhPW15BvwLu6YSWgxHZQb2axNmPsidKiGxPDiwnZQ0md6e0b4abKWEKJI1ZKr-sO7qx_o67TFYNlYC8HH4N-tDCxMB7nL1Y8LucTyCBLmK6LPj_LMtQ_bhDU0ece9Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رونمایی از یادمان شهدای مدرسه میناب در دانشگاه آزاد
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/468041" target="_blank">📅 23:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468040">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fe069ae48.mp4?token=dVmH4Th9WfuIExjpNXZuy9RTwN21V0fLdXQRSFuLZ3DCMDTw6w-WU6MlI36WSRnVjMRvjEPGHdqeXwZEp6InviEli-U_uKBj0UT8HnHfQ0pmqkpwBUY5dns0jc20LzAY2sW4TKwGPAXA5WJPx0dK62KRMqftPg6MLTnBstv8P3b1tbIWs4pYH5fUVWJmrAqzDC4AEp1nOaKXEECU4RJYxYsikLRjaF7hV1dDcA7ywmFg_ATrrfT9aQc-QbmR4rS-RF1m27ZyTOsaTQ8syuKLjM05-ibawVsjrhDJGGj5qYW7hunHmym-kkUJpLuNqBwi8T9usIGN0Q-yVAybk3uUow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fe069ae48.mp4?token=dVmH4Th9WfuIExjpNXZuy9RTwN21V0fLdXQRSFuLZ3DCMDTw6w-WU6MlI36WSRnVjMRvjEPGHdqeXwZEp6InviEli-U_uKBj0UT8HnHfQ0pmqkpwBUY5dns0jc20LzAY2sW4TKwGPAXA5WJPx0dK62KRMqftPg6MLTnBstv8P3b1tbIWs4pYH5fUVWJmrAqzDC4AEp1nOaKXEECU4RJYxYsikLRjaF7hV1dDcA7ywmFg_ATrrfT9aQc-QbmR4rS-RF1m27ZyTOsaTQ8syuKLjM05-ibawVsjrhDJGGj5qYW7hunHmym-kkUJpLuNqBwi8T9usIGN0Q-yVAybk3uUow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به الغرافه توسط آسانی
⚽️
استقلال ایران ۱ - ۰ الغرافه قطر @Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/468040" target="_blank">📅 23:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468039">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PesuimEXITbO_4jPw3oedpmNYXhCdYHfyYKcJISMGfRMIpOgWVTaAwdQCu2a1pvV2bxlRg3DLcu0Uv1h75t5D1fCDcshlllhi57KIwrJsoGyGY3H9Adguwg9oCcnMJh7evFwuyNLTPzAA1brQMGCWgavW78FAIfq0hAn9P8LXYWdc_dhTvaSWlEcWIBQCYD2hIkqW3if6xmHFAQqXxABbLH-Gb0yY7YshQCyare1hIIRcFkOlr3-HHQdTYEUHPop0DGNJo2nsc7_N-jmCpxr2dSULgEntt-1zpoCUbsOHHa-uKLIrBX36vx-htMmB3Yfw107CNvYOFhGl5PqXaX1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل آرامکو: تا تنگۀ هرمز باز نشود، فشار بر بازار نفت ادامه دارد
🔹
مدیرعامل آرامکو: تا زمانی که تنگۀ هرمز به‌طور کامل بازگشایی نشود و اعتماد به بازار بازنگردد، واقعیت این است که فشار در هر دو سوی بازار نفت تشدید خواهد شد. حتی پس از آن نیز، بازسازی ذخایر…</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/468039" target="_blank">📅 23:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468038">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌  حملات موفق یمن به فرودگاه ریاض و پایگاه خمیس مشیط
🔹
سخنگوی نیروهای مسلح یمن: امشب فرودگاه ملک خالد در پایتخت سعودی و فرودگاه نظامی خمیس مشیط هدف اصابت دقیق موشک و پهپاد قرار گرفتند. @Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/468038" target="_blank">📅 22:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468037">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f56d24fd6.mp4?token=aXBa97zfz1d1bp_OTJ0AwQN-KzN0rT40EtmjY60Mqsdtglht4RD7Bck8DHtU8xElQ1jqvsiH02gkku3izj-npK3HL3V0-s5nk3mhF5ufqf20Y0B0TLnUebsa3iQdjrKSXUHdjqY_QJDZ7rHHefceEUjAkh_7jYjb-DSLg7B8scyQyDWYWMvWuG7j4MI7EFRyoLAmz3_5r2wGHn7zdhuXiZIoEyc4Ahq-qnUiMUuULpTh2GPHsPqj9wKLCAl_i1leAwVDXjT9XPkB6r8FjDdK_PPin5uXWktLfxHMgzRQppmnXScDuXTr9HrgzJVfu78SpL9G3516kBB3rktxKaaCVgOGuple3-q0bYJYyJJh8SXuVQun1oYOvBQFNdoqFoLn5-uiSVGNd_YnHk5e8uJBP4Kn0tbY-2YNoDwfAIVDvq0-wJX5PxwgC6z19eQyUa65NZPO7Z5PRFGmXKUcLnxU9OLZ2gEWs5DgA-TkON7c3_mqG2B4zlnjfJpvjqK5uhxv_HgVR-oIjZ4f8hz1XBeWRAAh8sgf8QrrqAJJFD6pwnmtHPjRz2atJs5hBuocug7ETjBaA_2Ah7GWaxKSW8zh9FqrtMin6cCyV4XkGdKCEorkuYlAF7iGEpqMRTlqVFNNAf-dKynBDxgKqA8BpyD-uomLFgjjmF6nwdtddkPVXcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f56d24fd6.mp4?token=aXBa97zfz1d1bp_OTJ0AwQN-KzN0rT40EtmjY60Mqsdtglht4RD7Bck8DHtU8xElQ1jqvsiH02gkku3izj-npK3HL3V0-s5nk3mhF5ufqf20Y0B0TLnUebsa3iQdjrKSXUHdjqY_QJDZ7rHHefceEUjAkh_7jYjb-DSLg7B8scyQyDWYWMvWuG7j4MI7EFRyoLAmz3_5r2wGHn7zdhuXiZIoEyc4Ahq-qnUiMUuULpTh2GPHsPqj9wKLCAl_i1leAwVDXjT9XPkB6r8FjDdK_PPin5uXWktLfxHMgzRQppmnXScDuXTr9HrgzJVfu78SpL9G3516kBB3rktxKaaCVgOGuple3-q0bYJYyJJh8SXuVQun1oYOvBQFNdoqFoLn5-uiSVGNd_YnHk5e8uJBP4Kn0tbY-2YNoDwfAIVDvq0-wJX5PxwgC6z19eQyUa65NZPO7Z5PRFGmXKUcLnxU9OLZ2gEWs5DgA-TkON7c3_mqG2B4zlnjfJpvjqK5uhxv_HgVR-oIjZ4f8hz1XBeWRAAh8sgf8QrrqAJJFD6pwnmtHPjRz2atJs5hBuocug7ETjBaA_2Ah7GWaxKSW8zh9FqrtMin6cCyV4XkGdKCEorkuYlAF7iGEpqMRTlqVFNNAf-dKynBDxgKqA8BpyD-uomLFgjjmF6nwdtddkPVXcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراغه در ۲۲۶شب ایستادگی؛ میدان همچنان در دست مردم
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/468037" target="_blank">📅 22:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468036">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در ریاض پایتخت عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/468036" target="_blank">📅 22:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468035">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPW9U7aC0NdxKG08SjKF2G9Ho5Fe7ScisdZtu-OJejgvLT47TESLEplQCGdVedRbvxUtNoCvzoyDU0WjNfBPATLX62AlHRYC8nlpyUvBhpMeOgME9mNPJfcie3fmvyJaSiJVq4I4edjnKt0f0F5Dlok-dtqhE-SYI-tAqGTZdU0vjsP1Mr9HoDRDDAqWdCL7codY0IwPZOyc8ZpKeu3jnp4PamYAbx1juUIkmhMEM5zD1wAdlJMT1akDLZwdHJ7U8kJTzRjxYLH7Yo1YkDC9Gl1kv5O5YGir9DOtvT-XMoGDt6GvqOI8CdHUlKZCUnB-hhPg4hB-LzuUGPbn1yivNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی انگلیس وقوع حادثه برای یک نفتکش دیگر در جنوب تنگۀ هرمز در ساعات گذشته را تایید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/468035" target="_blank">📅 22:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468034">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6ffedcee.mov?token=AHhHCpPTv6JBn-DKYfRNUKy-XOOPC2t6xzKsuB_4w_DLZHqyHA5xEJQuYsVNFbbH_SdznyuPG6xJ3Yf6R0hJ2uGdLEuULVWkcaA1DKW5kCih1Z-8T1qAEgQum_aHorgXFpGXj4LymLKkfqpl7VZb2Gr0FkCAHl7_AwRmikS8UGUEUw_-NQoRNcl77Y2-znJM8ACo1827WpqokdXgWbxZ7FZBsVyypUqpxVccEs_igaQYBlMJtiKUfZnYnj9CAY1x-C6iyD9Rm6uwD8ut-UAgTu_Un9ztSN_aOpEa5j6HFmNokHxrLpA-hIcE1htAYXxuKPYra-v4a3ud3-z1CfAAFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6ffedcee.mov?token=AHhHCpPTv6JBn-DKYfRNUKy-XOOPC2t6xzKsuB_4w_DLZHqyHA5xEJQuYsVNFbbH_SdznyuPG6xJ3Yf6R0hJ2uGdLEuULVWkcaA1DKW5kCih1Z-8T1qAEgQum_aHorgXFpGXj4LymLKkfqpl7VZb2Gr0FkCAHl7_AwRmikS8UGUEUw_-NQoRNcl77Y2-znJM8ACo1827WpqokdXgWbxZ7FZBsVyypUqpxVccEs_igaQYBlMJtiKUfZnYnj9CAY1x-C6iyD9Rm6uwD8ut-UAgTu_Un9ztSN_aOpEa5j6HFmNokHxrLpA-hIcE1htAYXxuKPYra-v4a3ud3-z1CfAAFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در ریاض پایتخت عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/468034" target="_blank">📅 22:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468033">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732800d3ba.mp4?token=f2cHPyM5Dsip-birpcyDBbiBS9l_3QjRSW_fb3blxyO9sTpvUaNEfpPth_Ep5peAhI5d5wn98jAL4o8rKxEIeTZhCBDC-JR7FIKCKthkl5rag-hBI9hMXZs3yhqmk4VTtzvKmGtNKwZ5McRZZKT3VTXiFSOMO3KZ7m15p88ViEZoSrf-A0XNzFJJnhtWf2b-EuTnBfKsm2uDv_wcW_rATXGU0Bhrd1iF7lQfKSNGMNqyolT94wscZ_d4N0t_Bd-9zfl3lBpRAxEGDAxmXSP5UkjlMg5u6tnPf2wCFlco-1qnwYt9-4UcJEw6KIwWD_2yvHFD02JY6H5S5hZszVqQZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732800d3ba.mp4?token=f2cHPyM5Dsip-birpcyDBbiBS9l_3QjRSW_fb3blxyO9sTpvUaNEfpPth_Ep5peAhI5d5wn98jAL4o8rKxEIeTZhCBDC-JR7FIKCKthkl5rag-hBI9hMXZs3yhqmk4VTtzvKmGtNKwZ5McRZZKT3VTXiFSOMO3KZ7m15p88ViEZoSrf-A0XNzFJJnhtWf2b-EuTnBfKsm2uDv_wcW_rATXGU0Bhrd1iF7lQfKSNGMNqyolT94wscZ_d4N0t_Bd-9zfl3lBpRAxEGDAxmXSP5UkjlMg5u6tnPf2wCFlco-1qnwYt9-4UcJEw6KIwWD_2yvHFD02JY6H5S5hZszVqQZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به الغرافه توسط آسانی
⚽️
استقلال ایران ۱ - ۰ الغرافه قطر
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/468033" target="_blank">📅 22:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468032">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6404649e.mp4?token=vjspMIaYEGMghjCOIK0rfw19bWUuVE08miPX9CW_vzid2-yZt5Kep0DopdCYOBJrUwP-f5CQooyqJxxxoCArPX4Zk4sMBp1gTJsQeCwdigkIoqEvWjQSY9lm4j6XYzgO5F5lKaL67d-Z7OmZLe-vjVjIhKpmE2bDhxZZT1C1YSQvglUU2MEknbbbNLO8ZcwfLs-VGDfCC-jBtkAusEr5Z0g8OPuRfUK0GWsEbGeBn5EtnGD-30-KRwaPXRk23FNV3zt2uKXKN1VXQzBc_f1h8WRuy3CrIAJqYoey0l32yMx52kQf4DUUkOZcLQY92LPPJWI9XFlCeHpc_7YDCP5pfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6404649e.mp4?token=vjspMIaYEGMghjCOIK0rfw19bWUuVE08miPX9CW_vzid2-yZt5Kep0DopdCYOBJrUwP-f5CQooyqJxxxoCArPX4Zk4sMBp1gTJsQeCwdigkIoqEvWjQSY9lm4j6XYzgO5F5lKaL67d-Z7OmZLe-vjVjIhKpmE2bDhxZZT1C1YSQvglUU2MEknbbbNLO8ZcwfLs-VGDfCC-jBtkAusEr5Z0g8OPuRfUK0GWsEbGeBn5EtnGD-30-KRwaPXRk23FNV3zt2uKXKN1VXQzBc_f1h8WRuy3CrIAJqYoey0l32yMx52kQf4DUUkOZcLQY92LPPJWI9XFlCeHpc_7YDCP5pfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکلیف مبلغ افزایش کالابرگ چه زمانی روشن می‌شود؟
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/468032" target="_blank">📅 22:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468030">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: نیروهای نظامی که دشمن سعودی آموزش می‌دهد، باید با اسرای به روشی وحشیانه برخورد نکنند؛ این رفتار هیچ ارتباطی با آموزه‌ها و ارزش‌های اسلام و همچنین با فرهنگ و اخلاق مردم یمن ندارد. @Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/468030" target="_blank">📅 22:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468029">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZj4nS53LVW0PrH7P1fkJf5pBj2VqZKLZMU-HgKOa1CXt39jqGhiLMFONSqtumK7HwaHu8dc3O9D5Z5rbwJTdu6A8ZmWqD1fBbJ4SO7-r_4GNNOC4hxXcBRhB5cZr1AJaY07juQAlUraCoKIrZk7kEewd6QiC5BIo98wsSP0Hdr9W3Exi0Q--pgBxjIAj6JBm7eBo36j1VyHOM3DvPotFXvaR-pWSMJp5eoCsl2vWrGSUcHf8gBkxjX-Mfh9cE1yQLaxA06rEFH4oJIUBNCldsnvWgSKU9yzDg4V4Ljz90wl0BIRqigcAcRPM_d4Dv_pgTO7muG-5DueFo5RUeY40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ یمن بازی تیم رونالدو را لغو کرد
⚽️
رسانه‌های سعودی گزارش دادند که دیدار النصر و نفتچی ازبکستان در لیگ نخبگان آسیا به‌دلیل نگرانی‌های امنیتی در ریاض، تا زمان نامشخصی به تأخیر افتاده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/468029" target="_blank">📅 22:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468028">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDnSccDa-zZsWp5KVSJ-EEYWNXyQeDgkshlsefgJhG65nwtie4UYlvkkDzE-t9TEFdZG8jpdP9rt7bU7_-KmF6RJZpWAmid2ZjujxmPPphV3xHa4YEGDKbYOlskc3mrQEK_k1WLgXuCh0tXx1QV4mBtjWOACcsO3gdx0SuLo5-jYHPYxubLTE9iXsOzWsEV9Qt4USKLr0ru1axDxXmtwNFn3vkRzd794SJ8Xq2wgwRMD_sgdGbX9qPZdA7j0Cjq1dRWSAKOKJamwGgQ2XhfgEZzY8hj-5yP-OEJndRdr2HZzIP-nipqzRsr3L0QWpdI0CStgjfmF6vswLy7ow9ny5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌اله صیدی رئیس سازمان بورس باقی ماند
🔹
به پیشنهاد اعضای هیأت‌مدیرهٔ سازمان بورس و اوراق بهادار و تصویب اعضای شورای‌عالی بورس، حجت‌اله صیدی مجدداً به عنوان رئیس سازمان بورس و اوراق بهادار انتخاب شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/468028" target="_blank">📅 22:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468027">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c667e00cd.mp4?token=Xx0cxgA_eKeK_RBLk5jZ77c5L01ZF0ijh_qTDu-ArWa3T04Rlxnp_XY9yDBrPfpfoRDrvzzPc2GFMUKVvYeHvPw5JumDmH9hgJ7mxgi1rwwGw7LDNMLgdFwSjWMhGOfZXWBoRMgrSHxw2uohBmr-Qf1B_M-sWe1FRe0lB9Igxef7czeM-UOS9psCRUWcZXpRcei_zsV_FbiEqa6OuSmJ3yK9LTk4IX9iNO0wODekpAydjmDxUBasYPNd_ShYrzaVUVpeoFRf_sIW15f9oeZs6YhIjesnZx-oVs88H3q0Q4843oQruzDmo5mf_3jfHAqVlQo_uOYu8ohNdDRq9l4yww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c667e00cd.mp4?token=Xx0cxgA_eKeK_RBLk5jZ77c5L01ZF0ijh_qTDu-ArWa3T04Rlxnp_XY9yDBrPfpfoRDrvzzPc2GFMUKVvYeHvPw5JumDmH9hgJ7mxgi1rwwGw7LDNMLgdFwSjWMhGOfZXWBoRMgrSHxw2uohBmr-Qf1B_M-sWe1FRe0lB9Igxef7czeM-UOS9psCRUWcZXpRcei_zsV_FbiEqa6OuSmJ3yK9LTk4IX9iNO0wODekpAydjmDxUBasYPNd_ShYrzaVUVpeoFRf_sIW15f9oeZs6YhIjesnZx-oVs88H3q0Q4843oQruzDmo5mf_3jfHAqVlQo_uOYu8ohNdDRq9l4yww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۲۶ شب گذشت و مردم با حضورشان از خستگی عبور کردند
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/468027" target="_blank">📅 22:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468026">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0c9ei8ZNd1yAIYlKv_ka8DUGj_UO2DoXL7rCCUZrtnWfUd_pvv8QMkkfHMr66SUlVSsRyhytSs7MmmuVcRvzmgbP3Keo1_NZGDKyNoz6t6JEZmhDiw4ZIzk5ckrUbZLcpq3q58fpaFKxX297_wRIZ0_Y29aa-BZcHKLHsQBep75XM6HkBx8JEVUaujsg4i6Ag0ZmYSgM2EL6kdR5mFunraQ0HtfmzvI1-Du4vB_Y3hySYZ41spvKYfIv4G2sgdCGNDlJJVAv1pBDl5W-NeD-dqZPnchq21VO6QCPhXo_faMXOOOQVbPhF4Sd_y1x_Kng80Q9aI0Z0Uy3apPwxb3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو کشتی متخلف دیگر در تنگۀ هرمز هدف قرار گرفتند
🔹
سازمان تجارت دریایی انگلیس: یک نفتکش ساعاتی قبل در تلاش برای خروج از محدودۀ هرمز هدف اصابت قرار گرفت.
🔹
همچنین این نهاد گزارش داده که یک کشتی کانتیربر نیز درحال ورود به تنگۀ هرمز مورد اصابت یک پرتابه قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/468026" target="_blank">📅 22:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468025">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromانتشارات فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cp9Fqqd5qgBpyEd6Rp0OfILo3CPZ6gESxIDmNIXuHd2tGPd1lnBiMA4PvMbsmaWLC9FWgQ6e2bCTID5NgGJJaGSGVn2NDzA3eAGQL_F7DKvv2pPtmnJu6tgKmakrXdDLxiOkgauoliFH8GsRRvcGcv3uZ-nJoR56OVZpkUIvq-je23dR0FKcB6wi34ZfP09Vto8k-TlFcmi8gA1C0tFucvRQGhASDlCOVBdNfzQDM310XBR7TeJuHgsktJnIFFnuL_Sm6j52Y2RLSeQujJQRUpuQ36jaF0XRWO5hTrHZ13miK5fcPRdJlllY5zceCMZPbn4J5oAzaRDySHYfY2VNrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
انتشارات فارس؛ مرکز جامع کتب رسانه
، جایی برای کشف تازه‌ترین منابع دنیای رسانه و فناوری!
نزدیک به ۲ هزار عنوان از حدود ۷۰ ناشر؛ از رسانه و علوم شناختی تا هوش مصنوعی، همه در یک مقصد.
🚀
🔍
برای یادگیری، پژوهش یا پیدا کردن کتابی متفاوت، اینجا را از دست ندهید!
راه‌های تهیه کتاب:
‌
🛒
برای خرید آنلاین روی لینک کلیک کن
📱
ارسال پیامک عنوان کتاب به ۵۰۰۰۱۶۷۶
📞
تماس با ۶۶۹۷۳۹۹۶ یا ۶۶۹۷۳۷۹۴
🏢
فروشگاه حضوری: خیابان انقلاب، روبه‌روی دانشگاه تهران، مجتمع پارسا، انتشارات فارس
‌
✅
انتشارات فارس مرکز جامع کتب رسانه</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/468025" target="_blank">📅 21:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468024">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8de313989.mp4?token=IQGYrkRzYDvlXIVlCdi1Y6T-Hd6IBpgAqIgaiyiKo_QxBuDsyXVuAoJBHCzjqL8b0V-jplE2NezGA2xTTU8wRopwkFEk8IgO_ZLPD10AeIaZotl4DirUknnY0qkEFmNive6YHGfsCpop3nl7xaJ3-r9tEd-booT5WR-7_K27YYtN3CfmqPqbiZ4h0-hz6_vC7F6yAJVhmA0FB7q7172wmgitmsQ-MflaFSSbNvoLwT3zea7yCFt7VLxroHT2qBJkVARfTGrkh7b1KStusT9oSPwBm-MJtkOR37MNPSvDwYM0LVGjZPQgB9b_ojrMoXSx5dbn0cqOKqhTXAOoslZVGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8de313989.mp4?token=IQGYrkRzYDvlXIVlCdi1Y6T-Hd6IBpgAqIgaiyiKo_QxBuDsyXVuAoJBHCzjqL8b0V-jplE2NezGA2xTTU8wRopwkFEk8IgO_ZLPD10AeIaZotl4DirUknnY0qkEFmNive6YHGfsCpop3nl7xaJ3-r9tEd-booT5WR-7_K27YYtN3CfmqPqbiZ4h0-hz6_vC7F6yAJVhmA0FB7q7172wmgitmsQ-MflaFSSbNvoLwT3zea7yCFt7VLxroHT2qBJkVARfTGrkh7b1KStusT9oSPwBm-MJtkOR37MNPSvDwYM0LVGjZPQgB9b_ojrMoXSx5dbn0cqOKqhTXAOoslZVGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به حسن خلق و وفا کس به یار ما نرسد
🔹
شعرخوانی رهبر شهید انقلاب در کنگره جهانی حافظ.
🗓
۲۰ شهریور، روز بزرگداشت حافظ
@Farsna</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/468024" target="_blank">📅 21:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468023">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🔴
المیادین: نیروهای مسلح یمن به ۷ کیلومتری شهر تعز رسیده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/468023" target="_blank">📅 21:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468022">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در ریاض پایتخت عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/468022" target="_blank">📅 21:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468021">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyqiR2g-EYz3ZuDwa6K6vR1_r21YvoFY8QUlcCZJeUyYkZOzREw7CtKQ8sawNeUKiPEKDmJtNP_A868dHG4eapl1cAIkCpBvNw32k9KceMJcabnmdzC5vFYDb9JgRHYmKnRGldZ8kN-yDiDD36HELx-zaYAJFQcNKIOGL4ZEYbAZ6KnLKhzq9TfAfC5T9KpiqatIgAMrpVIusHMexW-p_0cupktSarHrk99O_adDAxtk_w_DfDrAew8mUUxKZP2qx5fn0LTrMLRQAxemIqT4Mln6so8vvc_lXvHLxWGxtNOCsjcSpjmFmbbmOlmQOUpi9PwPndX01lsjbiudU-idug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تساوی شاگردان نکونام در آسیا با نمایشی کم‌فروغ
⚽️
الشمال قطر ۰ - ۰ تراکتور ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/468021" target="_blank">📅 21:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468020">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فردا در کرمانشاه صدای انفجار شنیده می‌شود
🔹
سپاه کرمانشاه: از ساعت ۱۰ صبح سه‌شنبه ۲۱ مهر، صدای انفجار در استان شنیده می‌شود که ناشی از انهدام مهمات عمل‌نکرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/468020" target="_blank">📅 21:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468015">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZ2ejcWyw2rWCMm6w-e6Zi4R9gnDCR-UXYzdAVpvgsOo2aTbrcLev_4nHp5KEWGF5V7JMRaK0fagC45bWxrqVRJqNepnawR9B0lWrbDAKPjsRk-40CCWc6rZO1EBMn9-SRMJLuQiYsBsRIRazVS9c8bLvvsHWSj9QAV8pvVEo58-F_O6zCkfDsUq82KOZIEjy4WxswfNx278ELyLF9Ms16xeXulzEP__rPG07Af3vYqc6cw6XrkklCRUZV7Yb1tFaVb9fUqfkcf3DSM-v-YU2qtG39R6nNZcwLa8P-nuXKebp2C3qxaNQ2daFNMf_qjUyFqAr0lP1JAg7kABwZl5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IyZsDoYdIqZZHlANDNT743t5vLUeBs8Xl4LbulA8RvZN9ZI2IldKlNrjPZL7LqSoXJxCB5Gvev7zkR3-qtOSRD1pBwNLqblUS7tJXnkd3AI6eStHmEESzF0x56CXPntVlKK4Llzi-Ag2CMmOW_SZpPn3qi-kJtziDCW4m9ZR0TBO6-U8Rh0lApRya01SG9KTq4f0dexiy_A2KWRR_gYb5mlBgFOGKWOZhnoL4f0QxQSEgLPjhi5jXl5EvvF6Ny-TkuxYGz__83xPqfsK6hCGwA46puHj4q05r7K-TBumnSSlJtMTRrvCQUxZqNFQhQ9lXXYXLbpUFDoiFFTgz72Z7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLM71gxLrbvUfttfbwdz1fuA5OCrELR9e6h7bK5ZrHqEjZnHecMt9tAcuQNp1qgwoYHYelmmdMDQpqsoAaAksLIXXXWrlySUBIqG3xRJZFtNXFGiP5kk-r_gyE3AR9DCe_xyJkc_VET8POVLc9YfqfiTxUX2FpyZzKFcOckgLdJ95U0R2jUpaB0FJZmANTbV5D9KEeMoT1W1lRbTbCXJBljwGHZHXTk_dxFV2v3SylRnEzwn0BYLOLOzWHdQttFyQ_jPavKsYiOTxIlejJMlK6HMVjXczo9nMzNwKRi6GjvSwSFNN7964qvWbGy9_mYGSL7SfwKOEp204NGHrsP2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4XKbtgQPad4Oxc4yL563JeknAOjSGHJ8vx60lYrg72THALq6sJ1O-67fWYOcNk5NH2LRa3_WQZvT889EoDW-MEkrVSbbFjLQmDltvUIlPf2rvUCeMwkyjQijLWGT0ywOptizcgpqc0vbIT4vUlH11GQ6u7Se8Alkt2q6SZ2j8CulaA54Qg5j6u1fysMWpYXgzmYwxVx81zwI8-_7iuwCrAlMgRsL8mtsUeVvEvUl-ZzrtT-UlZOlEN8zwWNMXoWHz0pZqVJ85p7wwszvIxBZm9xmhO1NtTrBQ24KxXQQ7-FWJBjBU89DNMp5OKmSOZChQXXqtZmdu-QOQ7dD78RrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTvDJrwMKe6vdTqFIGswbIcOiznukhli9V9bs4uM_tcR59OBv7rzk3iCVFLjFzLAX-bh2W8bVZK3Cf3V-O9a8K6Ns0sJYkv9WL8GoNCY3QYyDFGBp1vlaD4tIDCqaxiZ8CZ8cwPL0scvdFJCAgEexEPOHign61-FFO1teLbC5Tn4CUpNVFHJOZtI2wTo6SU63NN11sWGPE1bntbge2YyWz28Cha3AAbINcK-Jzfai5VTbDmdo9juBfDnxte53HzCZLV_spcxGr522l2mi-ZekAE3j2TDxUfa9eSYY0RwS4eND9yMv3wj2Sj-DK3ubUnhsBsmT8Q6BFGiZ6Q2IGg0OQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت رهبر شهید و سالروز عملیات طوفان‌الاقصی در دانشگاه تهران
عکس:
هادی ه‍یربدوش
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/468015" target="_blank">📅 21:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468014">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80fb58308.mp4?token=CN7Fqsl2iV66pHHqww6Aq3TQ4ennfMx2aV81YkUHcAI5_N79xOr3qPTDEOFK1lII0BFv5R1MYs4lhR5bWdkFJEbquRw9pgqZbVIwm-7W222EYc0Kss9f8UGzNFk3Ir-9_mRyM4bqs_g_4_jojLJ7fh0xtKGMytGNFmVO9ZyvhB5rXOftB7pEDzf4NZaWDiW-ZY0nYutT-n8H5ViMsv26EYDsHea0xguEMW_MLrAFvkMiBSulBSB-DZPe6t2N00eDWfuWpNoFJHW1X5X2oKwKYqW0HvS_pFUpdMraaks_uunQDzlEocqred2XV0RiSMW5GzJbnnp1MS6zsZ00Qdtkmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80fb58308.mp4?token=CN7Fqsl2iV66pHHqww6Aq3TQ4ennfMx2aV81YkUHcAI5_N79xOr3qPTDEOFK1lII0BFv5R1MYs4lhR5bWdkFJEbquRw9pgqZbVIwm-7W222EYc0Kss9f8UGzNFk3Ir-9_mRyM4bqs_g_4_jojLJ7fh0xtKGMytGNFmVO9ZyvhB5rXOftB7pEDzf4NZaWDiW-ZY0nYutT-n8H5ViMsv26EYDsHea0xguEMW_MLrAFvkMiBSulBSB-DZPe6t2N00eDWfuWpNoFJHW1X5X2oKwKYqW0HvS_pFUpdMraaks_uunQDzlEocqred2XV0RiSMW5GzJbnnp1MS6zsZ00Qdtkmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عنصر عملیاتی جیش‌الظلم به دار مجازات آویخته شد
🔹
عمر درستاران فرزند عبدالقادر، از عناصر گروهک تروریستی جیش‌الظلم به دار مجازات آویخته شد. درستاران یکی از عناصر مسلح گروهک تروریستی جیش‌الظلم بود که کار پشتیبانی از تیم‌های عملیاتی گروهک را انجام می‌داد.
🔹
حملهٔ…</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/468014" target="_blank">📅 21:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468013">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b716719e58.mp4?token=doc9AMQEznevv7OPCYeQRl3kOWpQ_OEXXrPevmoPnvafKIWepazFGyz4nCnIgy4A-KBM2YBZYMxx-8lwo8s5bJSccMlEdi7bEo6c_xKLVkyS6l2ipbavzQacMfh_Oz4bd8NKpf10Y2X61xD4AHplhpxMx-pR7-Sa91qBOiooB-HlwNtJTIK_Z7EWuivapOpnFOvi8K6QGHI-6fWtLUIOnLj30g5JeQXciNptGiNwjiGK1QuxE8MHebzihQve3HGdsKZykTxYe5-Q7i52zmB8b9pXw3UfZT80nxBvaNPUbLLpFtwWeeltMfaW29wNX3xwuV6It2tes9FlQ5IVx4SHh1vTirP-qgpQifpsr3YtIHaIoWf6s9izThwDUmd_PGLXTYoBXvG-jbye8Tmb28u1ektxj_rBZPcBp3r9mrFZfyUWe4VtfowMd9gVwshctWaaqZLC0MM5un3VAb16Lv9CReKKxQmoNS4MC6B_giA4n3tXwr3Olhsix-P5EpWeEbpE65KXCR0_u45zU4_JwMefYVG0ac_Njp8qFyzQzvXW4qgzx94WYjPavwvpprmh2sbBFGZb8KlsxpsjBFLEBzUPcQ37HpbJ4UDaPJkfQdYoMcXbfncVhJtnKGbIU9xfNSEFrDUb5jmeE75fY3rBGmhhiJH2OqctQ5qthkFwahobkXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b716719e58.mp4?token=doc9AMQEznevv7OPCYeQRl3kOWpQ_OEXXrPevmoPnvafKIWepazFGyz4nCnIgy4A-KBM2YBZYMxx-8lwo8s5bJSccMlEdi7bEo6c_xKLVkyS6l2ipbavzQacMfh_Oz4bd8NKpf10Y2X61xD4AHplhpxMx-pR7-Sa91qBOiooB-HlwNtJTIK_Z7EWuivapOpnFOvi8K6QGHI-6fWtLUIOnLj30g5JeQXciNptGiNwjiGK1QuxE8MHebzihQve3HGdsKZykTxYe5-Q7i52zmB8b9pXw3UfZT80nxBvaNPUbLLpFtwWeeltMfaW29wNX3xwuV6It2tes9FlQ5IVx4SHh1vTirP-qgpQifpsr3YtIHaIoWf6s9izThwDUmd_PGLXTYoBXvG-jbye8Tmb28u1ektxj_rBZPcBp3r9mrFZfyUWe4VtfowMd9gVwshctWaaqZLC0MM5un3VAb16Lv9CReKKxQmoNS4MC6B_giA4n3tXwr3Olhsix-P5EpWeEbpE65KXCR0_u45zU4_JwMefYVG0ac_Njp8qFyzQzvXW4qgzx94WYjPavwvpprmh2sbBFGZb8KlsxpsjBFLEBzUPcQ37HpbJ4UDaPJkfQdYoMcXbfncVhJtnKGbIU9xfNSEFrDUb5jmeE75fY3rBGmhhiJH2OqctQ5qthkFwahobkXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیال‌بافی بسنت دربارهٔ فروپاشی اقتصاد ایران، مردم را به خنده انداخت
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/468013" target="_blank">📅 21:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468012">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b56ac4f14.mp4?token=X_rDMtOtiaE8HUEipD_dTsY-TAB6rlT9emVnc8PKAvMLckf8-Ds1uISiZH9s630SHT8NNk4QOULlSJrGdmMxsc-ECW4gKHiFDNked_vhf2oP4j29Sn3nYO8eKnJjsA6fU0ADKvgfkgaBK7TDr4FPiL2DMK80J9hAByXzU7vRuk9feFCQVrLUrtBDu-KeQNklsy7kjOYSVAe0oF49rbyZQhHgHEavcNZabr6Y0WYnAben53luvIwmpODo4bk72To3CIyOvEaPrLOsIWKEMOMrZWKiIC17x022Ue9C51W5amuCwIPQEvyaxLJri8AwRxJsTyOioVuSG0lRKdlkzFzfMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b56ac4f14.mp4?token=X_rDMtOtiaE8HUEipD_dTsY-TAB6rlT9emVnc8PKAvMLckf8-Ds1uISiZH9s630SHT8NNk4QOULlSJrGdmMxsc-ECW4gKHiFDNked_vhf2oP4j29Sn3nYO8eKnJjsA6fU0ADKvgfkgaBK7TDr4FPiL2DMK80J9hAByXzU7vRuk9feFCQVrLUrtBDu-KeQNklsy7kjOYSVAe0oF49rbyZQhHgHEavcNZabr6Y0WYnAben53luvIwmpODo4bk72To3CIyOvEaPrLOsIWKEMOMrZWKiIC17x022Ue9C51W5amuCwIPQEvyaxLJri8AwRxJsTyOioVuSG0lRKdlkzFzfMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از شلیک موشک‌های کروز تا عملیات مین‌ریزی و نفت‌کش‌های مورد اصابت قرار گرفته  @Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/468012" target="_blank">📅 20:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468011">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXEHVD3VIntRsr9Z7m0KQR1AlliopKEFA8uHCgfXvHESmq3SgqzgHx7WQbCocBmbgUjv96qHJHqhZsa5QeQHVEWKrOurlw7QKY-LrElJRtomcNN-4n_rGEFEdvLYD4_6K8Oojx7tApDAYzsG-fmzCDk_aFqzO_YB0gnyYn2a6xP5w7AwZ9rCrs-dsE-2bP4YOJU51mzdE6ex1u_ze_w0Ygu-pT9ULBsATUH2FO-hbSbrt1OIcRuP4hqywvn6nLVXNH7Mib1g34WQigJqRAVl1PxxGb1kVYf1SElxPze3DZgK8pFp8Ron_0eI6rzpaxk83zmOty4Ls3bynXRsmMijig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزيع‌کنندۀ شوکر غيرمجاز در مشهد به دام افتاد
🔹
فرمانده انتظامی مشهد: در اقدامی ضربتی توزیع‌کننده شوکرهای غيرمجاز قاچاق در مشهد دستگیر شد.
🔹
باتوجه به خطرات جبران‌ناپذير و در مواردی مرگ افراد دارای بيماری‌های خاص، استفاده از شوکر جرم بوده و با دارندگان اين سلاح سرد برخورد قانونی صورت می‌پذيرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/468011" target="_blank">📅 20:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468010">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda91c8550.mp4?token=I2Uj-ZJi8Jt0WKo-O4q6i0cDK7mm2RJtXCuRmGQOQ-28u4KvzBBeOppTW3EELYLWUwEHS4pMR_ITX6KomepX4kL37CbyCgYapcwhqvjQpxVQRxArtUHg2o3aihoBiZwkY1OHTODArJxn7RMpZK2Lp0b5h4ZTYQ9I-QN0WueV6pT6dTRWynpdgKPbIUy6byyW8q-MgQbylXXMp4-1Beqj9Svr3n7WdGG4_CItPIeZOS1uxThTh9B7lCDVBglvD-lvIHDpFrADA3w-h8mdTYXp0d7AYzwEgQ8j78z0VZGD5gsmZtpQg4pzqTuj83qS5_98t0g4ePy7gzuO7sFHCPJUsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda91c8550.mp4?token=I2Uj-ZJi8Jt0WKo-O4q6i0cDK7mm2RJtXCuRmGQOQ-28u4KvzBBeOppTW3EELYLWUwEHS4pMR_ITX6KomepX4kL37CbyCgYapcwhqvjQpxVQRxArtUHg2o3aihoBiZwkY1OHTODArJxn7RMpZK2Lp0b5h4ZTYQ9I-QN0WueV6pT6dTRWynpdgKPbIUy6byyW8q-MgQbylXXMp4-1Beqj9Svr3n7WdGG4_CItPIeZOS1uxThTh9B7lCDVBglvD-lvIHDpFrADA3w-h8mdTYXp0d7AYzwEgQ8j78z0VZGD5gsmZtpQg4pzqTuj83qS5_98t0g4ePy7gzuO7sFHCPJUsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگویی متفاوت با رتبه برتر‌های کنکور
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/468010" target="_blank">📅 20:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468009">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcca6e0aea.mp4?token=mBPrjKekN7RlCXW6F6Vny9EET6j6Ffjemwl8DhMA27t-jOQDhpfAHJFscYaivBgm_DDj0c6-POQ3ssTm8WEJlqHa-1SMPEYE5PPYI0eSmCyGtYDxOibXfIPEkz1xW8JJWUs0NrU1bcejVPElEQtR9nY8fPGjdL8WhO-1xt3CJvDQcO6rMl0dud73YilcRi2aqdx_farTDbdrG91393ufdfPM0lBf1bvhZBkmS2uHa-LgS7keEywdQzSoPnQLzBMWjzZUu2W9JGxMPY5bHTNS0zKM3Fees3bldIUP9hpA_zTMdcg_J6JU5CWt4CH1uG620qKQru1i8Lj3lELxkTTwI6WVMkSBtv1kolRB33bkVj7CZgzwu_sXFn7oHrGTIjOctnlzR0kf-8Y4AXkbdEd5s72q0AaD9MnhTyvQG0iOcwkUP0YpmEc9XJNyEv0mGUWmrV8uSomZ3sdnXUkViuN3Y9KLadx8joNabknzpq9uvWFis7eowRXpnC09sfFm2YLG9yq_ASwMb3G2-epNJgY0C_6L-dXyzvT-5cNwxZKtnFrQvrduMQxFnoeQMHAgVzlsNwG6BUhCAddFv3HaPDVZq9u-HxVo4pDc9rdrvDFnF66TnXotjpK1R-_rRTYiG6KFHftsJDgIzioazBLbb_qJncPziLtgT1GpzK37h2gAMnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcca6e0aea.mp4?token=mBPrjKekN7RlCXW6F6Vny9EET6j6Ffjemwl8DhMA27t-jOQDhpfAHJFscYaivBgm_DDj0c6-POQ3ssTm8WEJlqHa-1SMPEYE5PPYI0eSmCyGtYDxOibXfIPEkz1xW8JJWUs0NrU1bcejVPElEQtR9nY8fPGjdL8WhO-1xt3CJvDQcO6rMl0dud73YilcRi2aqdx_farTDbdrG91393ufdfPM0lBf1bvhZBkmS2uHa-LgS7keEywdQzSoPnQLzBMWjzZUu2W9JGxMPY5bHTNS0zKM3Fees3bldIUP9hpA_zTMdcg_J6JU5CWt4CH1uG620qKQru1i8Lj3lELxkTTwI6WVMkSBtv1kolRB33bkVj7CZgzwu_sXFn7oHrGTIjOctnlzR0kf-8Y4AXkbdEd5s72q0AaD9MnhTyvQG0iOcwkUP0YpmEc9XJNyEv0mGUWmrV8uSomZ3sdnXUkViuN3Y9KLadx8joNabknzpq9uvWFis7eowRXpnC09sfFm2YLG9yq_ASwMb3G2-epNJgY0C_6L-dXyzvT-5cNwxZKtnFrQvrduMQxFnoeQMHAgVzlsNwG6BUhCAddFv3HaPDVZq9u-HxVo4pDc9rdrvDFnF66TnXotjpK1R-_rRTYiG6KFHftsJDgIzioazBLbb_qJncPziLtgT1GpzK37h2gAMnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از شلیک موشک‌های کروز تا عملیات مین‌ریزی و نفت‌کش‌های مورد اصابت قرار گرفته
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/468009" target="_blank">📅 20:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468006">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WXXU0WlIrpvau8G5m4pGpHLnOFS8UHGB93vJZRs3TY64wOFTMSutZzoF5sfyiB_iomysh3rugXQjRWVLmbGtRkPqKLGvwLVtKv1mo4jfith7KNijlu_RYC2IkKKI4FSvF6wvm-I1i00kPR4Le5gcUWdT52iuTZ170y4zGPbQT7PU-W2I-IcENWNBwa3whhB5Yh5WN16JfQmp3OOngk9eRjDDaolre4ZIOVVq2n9rhrpxoog0L9Sw20IquwH_FVa4-RSnIfnj49tAfSva21IkhGBcg7ZLGxpk0x0Z3KykWr1BuBV_WbC_kclcRLU1x7XczjZtd0ITzfuPrxCsMNEZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nv4i_EbpSmkbmbVmP6NMm9Ss34ph25suj1ZHq3gVafoMHTU3upurBVFL6TEMBTsGjqVOzn4dPLHRq9OD1d81rduMT4f87cTZOJuvoareooxGKE2-NXSRn-IRwhiz2MAdcpzqPDYJ5VIx2bJEoq-vNyG2nsnuq9DG7ZZVRyq-a--d0Dtl3oDwsC0NnqwIgZR1IosJbgQnGqGc4qlKJJ7GzQgB0kfI07U10w22HBIHT4BSCyYtGg0m4Qn-w6Dy_C0dz1R1yGiPbIEInYHmjVDZG4Yr9c2FaM9_3HpYf8Ks_GLL00euoCBMGgllLYBMRpngNbXxZNBJS_T5SNflZCfW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DLzWUL1AhSzSrM4X6msPS91rGNkkkbQ-AqlsZoZI4QzUDEI1mnyMSz7zBuBTl5POta2v3ZHg5-7pdmj3ofCEIw197zm7XIoSDxwjFCXT9I7di1B3yILz0rI1Hw1Qc2ONehoZDPA4h6zn6nb3nJ3yKMYmHPT9lTx0-npsSt3C-BQBpn9go7y7pd3eqozF7vQ4JlnUYIWfAOSRaBiW9lnOC9iyKL6PsOXWIh17YNFANeYB7KB-6NWuTaT_oA84QtJQt8ExUpMzlkFnbWaf98V61mTa__SaW-rFCLMfNmGtELmtEr6ZBMRSVpU5b69hN5-dgb0j03G2ndbDWw3PMIAVWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
اخبار امیدآفرین ۲۴ ساعت گذشته را یک‌جا بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/468006" target="_blank">📅 20:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468005">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30f2ca925e.mp4?token=YOQSfGNIPZvO_ElIcILnU94nIE3IjtJmJh__8CBQ4BpDK57zI3om9jwtRwvJwXeGYf8AQPiof09AsLuDvKWgwdCLc6JiSEBG7ndB3q8bHm8ztmXh9dll93WAGQMplbYL1oJn1L97Kj0xuuPxtmBwcqKiLCSpCs77e3J12SiwKTCNQA-s4a9AZXxDioOHT6HGFqnLZHWTG-xlJQxTmcqGrFc3rtrVYOZZJtgDLeICIDrJZmYNxACsW5o3myCUibpko5n7pvQK4C2AdH57Uxumx1d2E8_VaryFHPr-689mQRcG_ss_kls8S_evAelgaDXIehO-ej86c8mcb4Vbi7y8dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30f2ca925e.mp4?token=YOQSfGNIPZvO_ElIcILnU94nIE3IjtJmJh__8CBQ4BpDK57zI3om9jwtRwvJwXeGYf8AQPiof09AsLuDvKWgwdCLc6JiSEBG7ndB3q8bHm8ztmXh9dll93WAGQMplbYL1oJn1L97Kj0xuuPxtmBwcqKiLCSpCs77e3J12SiwKTCNQA-s4a9AZXxDioOHT6HGFqnLZHWTG-xlJQxTmcqGrFc3rtrVYOZZJtgDLeICIDrJZmYNxACsW5o3myCUibpko5n7pvQK4C2AdH57Uxumx1d2E8_VaryFHPr-689mQRcG_ss_kls8S_evAelgaDXIehO-ej86c8mcb4Vbi7y8dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردمِ برنو به دست کهگیلویه‌وبویراحمد، اقتدار ایران را به نمایش گذاشتند
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/468005" target="_blank">📅 20:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468004">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">قیمت واقعی نفت در بازار چقدر است؟
🔹
جدیدترین قیمت بازار نفت خام فیزیکی دریای شمال نشان می‌دهد که قیمت پایه نفت فیزیکی برنت تاریخ‌دار «Dated BFO» به ۱۳۱ دلار در هر بشکه و قیمت گریدهای این سبد نفتی به بالای ۱۵۰ دلار رسیده است.
🔹
چند روز پیش  مدیرعامل دومین غول نفتی آمریکا، شورون، مایک ورث، گفته بود که قیمت نفت فیزیکی تحویلی به بازارهای آسیا یعنی همان نفتی که نقدی معامله می‌شود به ۱۵۰ دلار در هر بشکه نزدیک شده است.
🔸
ساعتی پیش نیروی دریایی سپاه فیلم سومین ابرنفتکش منفجر شده در تنگهٔ هنوز را منتشر و اعلام کرد تخلف و با آمریکا همکاری کنید هدف گرفته می‌شوید.
🔹
حالا آخرین قیمت‌ها نشان می‌دهد که برنت نقدی و نفت فورتیز، یکی از بزرگ‌ترین اجزای سبد نفتی برنت بالای ۱۵۱ دلار، نفت اوسبرگ و اکوفیسک هم به بالای ۱۵۳ دلار در هر بشکه و نفت ترول هم به مرز ۱۵۴ دلار در هر بشکه رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/468004" target="_blank">📅 20:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468003">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/043c9d1a30.mp4?token=oyfy3DsGP9tFa7rxRf_2y-VtrrLOhOVvpae-E0N75Mdg60px67hms56QpxZ5HaOxTU7Eye7HGuSepjh33V8i8cpdJ2Ypqaa-N0-uClaEG-XzSCcdKAzYhAMBXocgStA1SRjNpggpnGtXSS8ivKtWz46V6Vcq315sDADgm0VVbT107vhwJ27ZH9dkUYiSt-CrryQ3khjluI86awXYDwOh-yEKZlLhCEHpjAg0GHnvd26WsSm0yXSIaPltL7FZJw1vNEI-kQBLEXGMVLt69FEDDygk0lvcGlBnE_Xi4VVDRX4X1F7LqZvsTMk-k5IyaDOW8zqGOKHea12g4-mX3gvA4Q9iMHkOZQX_0NWPPXi4PO8gwTCoZQp4pFlK7aW1t9l6v3UjuLTJRjG22Fa4AlCRIgClpGdg3-X4EgEeNnsGRTz7zHCDJua8tsaqR_ey8LUjiau-AIgl4QON8iUW0AuRdKJwkZk-GXKb1qpJdoCOx7P-MKoYo2ZklBcz9TXdTgkUS0LSVJoA__xeRDUXm8MkZ25WYIwG21eDMOFRz7404jl5O-ZZzaEidTwdQHyH6Pjv7Qr2d2YqbF7ZRqiE9ioTvLOX2QSbCDLJbzYSFi18l8xtqzp4dwEYvWOEnvkOmWw2A1MoomIaXvvnrW1aSiI_BM9R6tRq6dm2XUqeHQhXG-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/043c9d1a30.mp4?token=oyfy3DsGP9tFa7rxRf_2y-VtrrLOhOVvpae-E0N75Mdg60px67hms56QpxZ5HaOxTU7Eye7HGuSepjh33V8i8cpdJ2Ypqaa-N0-uClaEG-XzSCcdKAzYhAMBXocgStA1SRjNpggpnGtXSS8ivKtWz46V6Vcq315sDADgm0VVbT107vhwJ27ZH9dkUYiSt-CrryQ3khjluI86awXYDwOh-yEKZlLhCEHpjAg0GHnvd26WsSm0yXSIaPltL7FZJw1vNEI-kQBLEXGMVLt69FEDDygk0lvcGlBnE_Xi4VVDRX4X1F7LqZvsTMk-k5IyaDOW8zqGOKHea12g4-mX3gvA4Q9iMHkOZQX_0NWPPXi4PO8gwTCoZQp4pFlK7aW1t9l6v3UjuLTJRjG22Fa4AlCRIgClpGdg3-X4EgEeNnsGRTz7zHCDJua8tsaqR_ey8LUjiau-AIgl4QON8iUW0AuRdKJwkZk-GXKb1qpJdoCOx7P-MKoYo2ZklBcz9TXdTgkUS0LSVJoA__xeRDUXm8MkZ25WYIwG21eDMOFRz7404jl5O-ZZzaEidTwdQHyH6Pjv7Qr2d2YqbF7ZRqiE9ioTvLOX2QSbCDLJbzYSFi18l8xtqzp4dwEYvWOEnvkOmWw2A1MoomIaXvvnrW1aSiI_BM9R6tRq6dm2XUqeHQhXG-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگهٔ هرمز؛ خط قرمز ملت و رهبری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/468003" target="_blank">📅 19:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468002">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c5bb9592.mp4?token=rZxPVQ8AKtS_boEp8SkiqRHDq7JA1cYuLT8fWTrj4Ji60WG2EDHUk2zk4xJaU0J0YeNCdaHrcGMiwwLbMtIolD0P1sQAT19saGDFhTlCt4Xg_qng8_kPS-TYz0PhMKuUc-JNDRyJfLin3UFrUoSKtNwNkMjBU_KsGss8iwx5p35k8vdTUVyb4FlnNwx1NHOnH2uuW5PbMrvh45_CIsFMAgHVpruV_szpn4LWqCrA5lBuNMFEXaV-d22EcrQn855xBjFg-WWxvhdPe78zi7pWsCvShrEctduBAhxICJJ-aqoAsjxhVgZdzpdEr4goFYHHpe3OkzXwk-X2w-_NQbN_ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c5bb9592.mp4?token=rZxPVQ8AKtS_boEp8SkiqRHDq7JA1cYuLT8fWTrj4Ji60WG2EDHUk2zk4xJaU0J0YeNCdaHrcGMiwwLbMtIolD0P1sQAT19saGDFhTlCt4Xg_qng8_kPS-TYz0PhMKuUc-JNDRyJfLin3UFrUoSKtNwNkMjBU_KsGss8iwx5p35k8vdTUVyb4FlnNwx1NHOnH2uuW5PbMrvh45_CIsFMAgHVpruV_szpn4LWqCrA5lBuNMFEXaV-d22EcrQn855xBjFg-WWxvhdPe78zi7pWsCvShrEctduBAhxICJJ-aqoAsjxhVgZdzpdEr4goFYHHpe3OkzXwk-X2w-_NQbN_ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراف مجری اینترنشنال به دشمنی آمریکا با تمدن ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/468002" target="_blank">📅 19:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468001">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52aa588aba.mp4?token=sPyaDbdjarUMUnt-Tc-AZuI8y6VJ-cg3V5sMF3Y4zw1Qz5nyCm3gB4XHVEg-kfTljHwUMJLZEyJ7I5XVBMExrNxxh7m_31ZLziEtuvhbwb5LzEn7dtTLiLcC0yHFHmpK8avLM_b33g948oUmsq3Ug7ack3XalZO7V3nDYw2taux93epE8KxddN2CtNszds60IBZqjpXmxB4JPy7_2zY88tXQLZmm_4ibVQcYkTvM0HP1ikXAOfc08VoWthcBuLTffEoWgUcWqK6ulCQZkWaO_0i0DlGOeHzLN4za6CwJRgefhcqNVS4SMMBZoQE_iNSi-iOanc0YWKvI_mufXC5B9RjMxP6Hl085rKMm_DD5h5ETHHsFHN6jdzgv1rfvIsrqm3ylo00_7Cmm_i4oSTKtJoL4KBgafslvjQ8gHwx2Vubxd5GzvACCrfDhlalWTNHLviB2jCNAyrWm3mMXIjmX7UWjIPZZizA4qwl5l4Q_gZTyWM3rvq-CMzzmhO2TQJjSY3WSVdSP5KRgizIrVZDA64MbW7A9zhXWMgkzGPMEsfnJm-Kg9oa_1EnVk00B-q8dqLCOnCzyBJ3OHmQXc-ZJPJfaH5_qEY5QYHw5VFqgJrKdyJQwHns-Wck5gzvMuA4VsAIuNmGpFepcF-5jLpMAJs_V1Y08SbIADftDZVlKmSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52aa588aba.mp4?token=sPyaDbdjarUMUnt-Tc-AZuI8y6VJ-cg3V5sMF3Y4zw1Qz5nyCm3gB4XHVEg-kfTljHwUMJLZEyJ7I5XVBMExrNxxh7m_31ZLziEtuvhbwb5LzEn7dtTLiLcC0yHFHmpK8avLM_b33g948oUmsq3Ug7ack3XalZO7V3nDYw2taux93epE8KxddN2CtNszds60IBZqjpXmxB4JPy7_2zY88tXQLZmm_4ibVQcYkTvM0HP1ikXAOfc08VoWthcBuLTffEoWgUcWqK6ulCQZkWaO_0i0DlGOeHzLN4za6CwJRgefhcqNVS4SMMBZoQE_iNSi-iOanc0YWKvI_mufXC5B9RjMxP6Hl085rKMm_DD5h5ETHHsFHN6jdzgv1rfvIsrqm3ylo00_7Cmm_i4oSTKtJoL4KBgafslvjQ8gHwx2Vubxd5GzvACCrfDhlalWTNHLviB2jCNAyrWm3mMXIjmX7UWjIPZZizA4qwl5l4Q_gZTyWM3rvq-CMzzmhO2TQJjSY3WSVdSP5KRgizIrVZDA64MbW7A9zhXWMgkzGPMEsfnJm-Kg9oa_1EnVk00B-q8dqLCOnCzyBJ3OHmQXc-ZJPJfaH5_qEY5QYHw5VFqgJrKdyJQwHns-Wck5gzvMuA4VsAIuNmGpFepcF-5jLpMAJs_V1Y08SbIADftDZVlKmSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای هدیهٔ یک دیوان حافظ از سوی رهبر شهید انقلاب به مترجم بوسنیایی خود در جریان سفر به سارایوو
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/468001" target="_blank">📅 19:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467993">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YS5e8hZzgYHXwT13jLW8bNXo7qJXHifTBj4Lm2QVclfW7Gzk9BrD7LRSNb0ykz_2KgWFwVrxG3OQDs9mC41xL_5ZBs9r_siEsoXulRxGlquqDjqbzU-OPerGWEBmVtGmCHKCvl2e3aH_shGxi_JzmVcRufRM2sMwhULVMHRMVqiddeOWGjBhuy0LTmZOXfgQQCc1vXf-W1QqvYapfH0VFLAwpv9Gn30-u1yW6lEshWg-fVgHCLuj6qvAvo3SYKQy4iZN75jkRphNG0ioCsjVEWMeCGPR8GW7pNdN52HvEulqUFTvehYIbuz9y0EImG0diEQYHEw0_dqNIG6r-2Pc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MDClYgAWlH1KvCixHN5LFLc1vxaeY9vzf61RqCePwNGGdv8Hc46pJqh2Tt_S3CVzvJWjgRNLKt_nJExFqZk7jcfSKaROqLSnhG3ehpgGYqNzW9IHwYL8e7VDyYnWht-iFWHLN-zmFr2e_QHvBaZcHJXameOCmGRk4w4NNJGDg-un8gp2hqoaKwduP7H9W79hJKkurpz58AGKzXcpzTt3CmyP64ecHumrZCFMIFIADSkX1yl6ovwIv_z0r_O6zmeEfDTq0i3_naL4213IeRL4ReWq9SEauemExew2_9sAScBNfB0KZY2dy7oBvaHZdfG-9em4Z5T681DJPnqTTzeYNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaETyfuUJ9gNfGSKJUCpVAslErtbZHI5VkVJ8Lmy71-BJe4bpKnHl8sr44XL26jC5042qXI62B7lkXp7pdwLaggq2nFqrfdjdeyhkotGhRSKhBvYlH4ccjFmXVA3aBo0FMt-Uz8WRRprfZ0Rho9ooo0ag1uynE1YZjfzmZNCcb5p1mPJJ9yoP4636-HyMZzaEYF-8sNAbqawGqWHQ6bFlgim1cEP_sN06_D3Os-tt9TFEkca0ACjewQMyHee8flPm4giKVPzJLmDzmF4PRzZvt0X_1llAFBmC0Jfm0HXwUbTloewLOpccjpsTZ06MeZptRc_ITOr1lQg3bRpc92Lcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTQdmbGpV_QqjnT9IYOzk4pjasuqvfyB4HuNtIeCTj2gZ1t1N-v0Obsemi8HcVpXjaCrED4zFdOllxQBE-y9x0B2BFC8LZ78OVIfd9DJ8dTLmwvvpIK3I8ybwBOL0NnsxWzNafk0hQePU5ByScPdOdGLI6LkMlPlnIgJN3366l6OG78xgR9tyWqfyBPubH77o_yRFL20lJ5mpZKXnO2FZHRwmEV4_yPgjyVHfGMIrFUGCAoFZZ6mNlerJfiWd-mRxYfujnEyxbx3buaZK2p8X9vzMz92QpxCGJ2SFpkSRZCZEWNfn42MXWySZ_0qiGmnxYphwclgxibDxjatVlFtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iatnE9SbMZAAW7rIVYlEGAsHBhM4VA735oAQimla8TYzzUFy3MV0eqjJykTaI8Gi70_tjwV_XveucTM5fbeIRGtgrCWmYnkYl1FeUngKmSRwrqJ2AzbvnVE1V8nKm7lRNeoEF64EH4ifIJfR2O2gWeUmo0732XiaLWSWM06pDEzJpYzZg7qst05csgiU-eG0xaUpNoVmqxTAUjtVloDjEL_3LrgU350Ad5FPSyhxub-b4Oj6qf_dCzz7GFQ5KkH-myNkrzW1swej71PXI5w_Ep8wnKn7fJ0Q1f75kRQJ8ZY5hDirz3GdeNqyS44NkIc55c_ipjPB2RvOrgipppmRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYVQDXbeTzHmTjfI87ya-I5j3KOayQtHH8_Apg0aYTtKDH2IwvevEBJpS16g_QUYOTgQV3l_kZIRAj-8T02ghosjbZi-OrfeAB-ISGtIehfmWRVpicS8sj8bVtb9q1knIJ_FC6qahzjwBiXGEAqOjjlrC2QJdani7VYxJ3vOdS5MyQnMLVI--dsHgcUHHK4r1_GO_F8g8AfReXDnDgctkXKyGRxumIDxVQKC3tSX8Pav3TFalQ-MMldy7h6Nx9rOy6zCfA9VsPZgRNP_XYYGPSgurJ5Iq3Gps1XMhUODqdlN3nZrBOEKz07CQfv0eE5yO23uLhmBjckyo79Dul6rHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P_ao1WwKFKQDWmYm2-Q9kGJHH27p8vU182p1eYGRt5c98uKaAI6AovL95vo0XdgAjDGe0zjSTlDcELd5hOyECGUQGDmQyH88gTkcROujKFVywwBG8oobIGsJjdyz-xb3idLqzEKw1TQ5cKRXwsDR3jeINm5Btnlt4xZW7_4uX2eIoQ3Zaaf3uim4eA0haMIkwT6jQTQMpN6pgmX1kbjEc2la4kD2RLmgEhOH_qZbyUGVrKE0SATbkWag4Jm6FyzyafsJzTy4qYpAKzpn_uDvH2CjJuSqwJF16iLJsqnLG0EWkoIHp5sHB-Oylyj-Njk14F267LplTuNvAG6b9Ki9fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
از ترکیه تا میناب؛ کاروانی که‌ به‌عشقِ شهدای میناب رکاب زد  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/467993" target="_blank">📅 19:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467992">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c955e2c28c.mp4?token=fpEm5eEcDz-Th4Vw0ozLaC6h38M4EC_GYidp3cOIIdzNg1PKOH5WOObx2ESTF6goKdcwKQ8Ao9qGQlJ1EXYg94iGXy75nZCtdOU4kaE-WQQ58zd9PdcDQwK0oSUzuwfyjSxQEkJnZVcCd4tsMoMZdsw2y5nc_D3EMnTu60Hy4dSQYXxJTG4YXMNrvnpihymQ7VVSicF5T2ZBcy3XLTXk8McpWHMgP72YaKOPFQbvkkHGp2FhlhfCqME-1lo0Mu-d1bQmfzqkyZqi0eQShMyYGoLEbNlcPBpDb6vzVvgKqhAIClMwsh7WOlI6Ff3-o-Ho5pZ5C96C2BVjWqdcAF6pkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c955e2c28c.mp4?token=fpEm5eEcDz-Th4Vw0ozLaC6h38M4EC_GYidp3cOIIdzNg1PKOH5WOObx2ESTF6goKdcwKQ8Ao9qGQlJ1EXYg94iGXy75nZCtdOU4kaE-WQQ58zd9PdcDQwK0oSUzuwfyjSxQEkJnZVcCd4tsMoMZdsw2y5nc_D3EMnTu60Hy4dSQYXxJTG4YXMNrvnpihymQ7VVSicF5T2ZBcy3XLTXk8McpWHMgP72YaKOPFQbvkkHGp2FhlhfCqME-1lo0Mu-d1bQmfzqkyZqi0eQShMyYGoLEbNlcPBpDb6vzVvgKqhAIClMwsh7WOlI6Ff3-o-Ho5pZ5C96C2BVjWqdcAF6pkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی: روسیه پس‌از اعلام آتش‌بس انرژی توسط ترامپ، به تأسیسات انرژی اوکراین در کی‌یف و خارکیف حمله کرد.  @Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/467992" target="_blank">📅 19:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467991">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0CoCes2-Ow-WKbphAOaZ30eZVcOa3rmEtpfDzB7HpGRQflv3a8gLsZmQLQaNVHTK97EP-Ir2mhqd8sZi3zgDWmuuekGdeoo3r-9_-mt--M9OvgQsOgp1L3nTc_aNiBjXrGSCsi1vKmFPP2FU0tmLUkUoP474upllC13ER_qVYvJzKbpKsz9DGrCB5FUXVH5HFTNG0sGaMS2Np7CxD9RanMgBzG-JwHYxYYWxm7TgEYT7e__AWpQVr47GWVrndBhdysUp6uTT6QlGiN2V8gvHK4vN51kJAHeIpLUrFI9qCzcDVMussWlTIR-Dp7py381L0hQPHs_GesgljtX21DecQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت ۱۰۷ دلاری شد
🔹
سابقه نشان داده که هرگاه نفت به ۱۱۰ دلار نزدیک می‌شود، ترامپ از «پیشرفت مذاکرات با ایران» می‌گوید.
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/467991" target="_blank">📅 18:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467990">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yd3FeUMsKSUGFfieGfCFFgr-vyiuXrp6KaWIl-RVi8tLM-fuEBU5slzuEtjbHrkftBeCk-WGTj8MyYmns1N23P2-3PQPRVMS4DE9bIGALbQ6DvKcO4zmAGiXrjsNM2LJTFbBD1RBFzM9jx6atYaijUeTwCrT0A_gdHT5ADPA7GtON9FN2nPRMXtNt2Or83JVRJB8F7eoICxV-JVcwohaU1Ag2SegKdNx-tydMLDjgL2YDWPnvxpHzXKAYXiGL7XOb0pbJqb-kjBHnIR6RIlHrRt3Wy2u4-TGyK30o7fLqEsp98qkmzX_4ptv4p4Z09oAhvZCbJqzXTSEc9Kph84iNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزبانی مسابقات آسیایی در عربستان زیر سایهٔ ناامنی
🔹
رویترز: حملات به فرودگاه بین‌المللی ریاض و توقف فعالیت این مرکز هوایی عربستان، در شرایطی نگرانی‌ها دربارهٔ وضعیت امنیتی این کشور را افزایش داده که قرار است ششمین دورهٔ بازی‌های آسیایی داخل سالن و هنرهای رزمی آذرماه در پایتخت عربستان برگزار شود.
🔹
ادامهٔ محدودیت‌های پروازی می‌تواند برای کاروان‌های ورزشی کشورهای شرکت‌کننده، از جمله برنامه‌ریزی سفر ورزشکاران، مربیان و کادرهای اجرایی، اهمیت پیدا کند.
🔹
در صورت تداوم شرایط امنیتی و اختلال در حمل‌ونقل هوایی، تصمیم‌های بعدی مقام‌های عربستان و شورای المپیک آسیا درباره نحوه برگزاری رویداد، بیش از پیش مورد توجه قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/467990" target="_blank">📅 18:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467989">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7559f0540.mp4?token=TjAwk5A8VHdOekuL14CS6mHaP0cPPfLHAzOWuabDKM2QRbLdx9ynJ_cJTdJNTjwocHhfw8iVrnmv3r256RU8auEtOjR1lWNsH-fAfGMIm2zURFFKPUxe3mSM435lYddLt5X4aB4I5NuOEqyDNBtX4pLlhLHWhj6H7gajssw3R-6GqiRgkhMDZ2SfJkYAiLbsX3aajPiXytazanQGL8Yx6QfYVDXfc2tGf4tUPce_T6w6j0wxBXWidMmPXuWItqeqdzDBRrDZ4TG8-LiGdDG9yZX83MkWg4Jg8qW96f316nfjA14_Bk4TlAaXMST6IpyzT-Mqkl_7BfWhAtnQ9iXG3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7559f0540.mp4?token=TjAwk5A8VHdOekuL14CS6mHaP0cPPfLHAzOWuabDKM2QRbLdx9ynJ_cJTdJNTjwocHhfw8iVrnmv3r256RU8auEtOjR1lWNsH-fAfGMIm2zURFFKPUxe3mSM435lYddLt5X4aB4I5NuOEqyDNBtX4pLlhLHWhj6H7gajssw3R-6GqiRgkhMDZ2SfJkYAiLbsX3aajPiXytazanQGL8Yx6QfYVDXfc2tGf4tUPce_T6w6j0wxBXWidMmPXuWItqeqdzDBRrDZ4TG8-LiGdDG9yZX83MkWg4Jg8qW96f316nfjA14_Bk4TlAaXMST6IpyzT-Mqkl_7BfWhAtnQ9iXG3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کودکان رئیس‌جمهور را غافلگیر کردند
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/467989" target="_blank">📅 18:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467988">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFvcNpK3pr4ceOcLMSW1iIbVpLVgBDt_MZ8e61BaCJZf02DUWGdO6IPKDdxZH9SFyBrJ1oDLS3Da0AIvBaFYXmvOW5z1FoJMFia40NRrs8qHqRotHP4mD7LqIXDjszxK3jlmvgFd5CL_CCyjtwXTfTvU93nVqT-_97SQarzvyar6WmWXyXtsNbXJqx8yivRPZ-VJv5FHm1C1b2oadH2meBMD9oz53qvO1O-shmAwPma7ZpYckRQm5zZNPUzXcNtFCELlj5TgHjZ_4hPn8C4RS19aYgPNbsHf-AYM_iPeyS-0bAFiYWuSdQh0pjtAtFyOPetDePjaM3DRvyILDgkqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج لغو پروازها به ریاض تا سال آینده کشیده شد
🔹
شرکت هواپیمایی طيران الخليج (Gulf Air) بحرین عصر امروز دوشنبه اعلام کرد که پروازهای خود از ریاض و به ریاض را در بازه زمانی ۱۲ تا ۱۷ اکتبر لغو می‌کند.
🔹
این شرکت پیش‌تر نیز در تاریخ ۹ اکتبر پروازهای خود به ریاض را به‌طور موقت تعلیق کرده بود و اکنون این تعلیق را تمدید کرده است.
🔹
طيران الإمارات شرکت هواپیمایی بزرگ و پرچم‌دار امارات متحده عربی که مرکز اصلی آن در دبی قرار دارد، لحظاتی پیش اعلام کرد که پروازهای خود به ریاض را تا دوشنبه آینده تعلیق می‌کند.
🔹
دلتا ایرلاینز آمریکایی نیز هم اکنون اعلام کرد پروازهای برنامه‌ریزی‌شده خود از آتلانتا به ریاض را تا مارس ۲۰۲۷ به تعویق انداخت.
🔹
درپی حملات اخیر به فرودگاه بین‌المللی «ملک خالد» در ریاض، سازمان کل هواپیمایی کشوری عربستان سعودی امروز دوشنبه در بیانیه‌ای اعلام کرد که تعلیق عملیات فرودگاهی در این فرودگاه تمدید شده است.
🔹
ده‌ها شرکت هواپیمایی بین‌المللی نیز پروازهای خود به ریاض را متوقف یا لغو کرده‌اند؛ موجی از لغوها که برخی از آن‌ها تنها چند روز ادامه دارد و برخی دیگر تا ماه‌ها و حتی تا سال آینده کشیده شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/467988" target="_blank">📅 18:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467987">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKJoPLxgmTaFTjCokZNVPAfUWE8Ju5rJySixpSThbli5yIO9QjKXsBFZuZj6r9RGmmgDMTjMuzKZzKn0Aw6bYV5yAGqMQlVYjrMAThc_r-Mj3i4uUZGCYd01Gkp4df43JCUiVmnQn_uOQzzHhjnDEsatj5RISdfoxXUvAo_ZGl7sxTftZn_CTJcq2Gng6y2j2u8QYVKqcltn1KhhEK_08Rdid0KszO7yCRT6m2ISU-djxKK6WKxIqwPUKPOXfQvb7UbaZHfnlZyM9ZXH_pR2iQpQ-IyG2kPLauLLRzYw1_e2Va444h3bJnDNnLW79h7qLeZrOQfigTR8dex1Ead2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: اگر نتوانیم مشکل مردم را حل کنیم، نمی‌توانیم جواب شهدا را بدهیم
🔹
کسانی که برای عزت و سربلندی کشور جان خود را در طبق اخلاص گذاشتند و فدای مردم شدند، برای این هدف از خود گذشتند که ما راهشان را ادامه دهیم، نه اینکه به دنبال پست و مقام و نام و نشان باشیم.
🔹
امروز با پیچ خطرناکی مواجهیم. جنگ ما فقط این نیست که با تفنگ بزنند یا موشک شلیک کنند و ما مسئله را حل کنیم؛ این جنگ را هم داریم، اما بدتر از آن، وضعیت اقتصادی‌ای است که برای ما ایجاد کرده‌اند.
🔹
ما موظفیم مشکلات مردم را حل کنیم. اگر نتوانیم این مشکلات را حل کنیم، مقصریم و نمی‌توانیم پاسخ خدا و شهدا را بدهیم.
🔹
اگر توانستیم در جنگ پیروز شویم، به خاطر بسیج بود؛ بسیجی‌ای که مغازه‌اش را بست، درسش را رها کرد، مزرعه و خانه‌اش را گذاشت و رایگان به جبهه آمد و برای دفاع از این مملکت ایستاد و تا آخر هم ایستاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/467987" target="_blank">📅 18:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467986">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۴۶.pdf</div>
  <div class="tg-doc-extra">2.4 MB</div>
</div>
<a href="https://t.me/farsna/467986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۴۴.pdf</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/467986" target="_blank">📅 18:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467985">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رئیس سازمان بسیج: برای رویارویی با حوادث نوپدید نبردهای ترکیبی، باید شبکه هوشمند و سریع جامعه‌پزشکی را در مساجد و محلات مستقر کنیم
🔹
هر مسجد، یک پایگاه پیش‌دستانه امداد و سلامت که نه‌تنها در زمان بحران، که در ایام عادی نیز مسئول پایش سلامت جامعه و ارتقای سواد بهداشتی مردم است.
🔹
ما در این بخش مسجد را نه‌تنها پایگاه اصل انقلاب، که سنگر سلامت و کانون مدیریت بحران‌های اجتماعی می‌دانیم.
🔹
این حرکت رجعتی‌ است به هویت اصیل ایرانی اسلامی؛ بازگشت به من جمعی که در آن رنج یک فرد دغدغهٔ سایر افراد است.
🔹
در این گفتمان، مسجد صرفاً محل عبادت نیست، بلکه قرارگاه مدیریت امنیت و سلامت است.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/467985" target="_blank">📅 18:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467984">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzbCHAD_BreV0Cf4lV1rDOplm9hKMfoJO5t6klh-A8D58yDftx3LdSJ42v8q2Ot9Y6LQj1Ubtj80qu2aUKf7j8Tf2NUsxc_OiWus3aHK-uhbhTskjelVLN-jM1P415HBk8fQYvIDd78KLNSxwdZO2DHZ-1G2_HddIHYKZQ-CEvZpBa1R0OuB0qznarykguW7uFT-u0bEj8FEjox3SmEYR8ELU3l65sZ-9k24IMRPHj3bt56emloyB4_-AHHZokPSKspljUt8y_PhDlRVFe9Fpd9VB60wge6fUngmuOmDtGjtr_x2fs8Zy5ilCWCWz1CjoXYXe9basY1XPYbvrdAMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمان جدید ارزی برای بانک‌ها صادر شد
🔹
براساس بخشنامهٔ ادارهٔ کل عملیات ارزی، دستورالعمل اعطای تسهیلات ارزی ۶۰ میلیون دلاری از محل منابع بانک‌ها برای واردات کالاهای اساسی ابلاغ شد.
🔹
این اقدام پیرو مصوبهٔ بانک مرکزی و با هدف حفظ امنیت غذایی و تداوم زنجیرهٔ تأمین تا پایان سال جاری اجرایی می‌شود.
🔹
مطابق این ابلاغیه، تخصیص این تسهیلات مستقیماً از محل منابع داخلی بانک‌های عامل صورت می‌گیرد.
🔹
همچنین شعب بانک‌ها مکلف شده‌اند پیش از صدور گواهی تخصیص ارز، مراتب وجود منابع را از ادارهٔ کل خارجه و دایره پشتیبانی ارزی استعلام کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/467984" target="_blank">📅 17:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467983">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqm-8h8ZPqY_yVvi5CfbLMH84f0ZlK8HSfEEDvrGBTRsHwYOIOmHHzoGaRltrvr7Zn0t9QPb1LAVdeWSrdXaAu5yike8FIXpHjjrkrazRj9E0m0ahjrkKEVNDlsOP80tlu_ltdxBMMNkcCF1VMTVazPc0FL_gtNVnEk8-dhDMOXEYUPdFcv9VLu0-oefcl_JBjJfAmuOEjIOYRQfpW5NXLN_S7RjSVDGLRjd5bh3ViCwLBnUSo2Ke0eKBJbCr6pqWEH7AG6SD2Tr32NjVoChu304aJ_RoW9Df3OlpZCRXTw8V6hZturhC9bw9F-Xsyv2F7lyHL940iLMsyz1FCMLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  وزیر پیشنهادی دفاع: تقویت پدافند هوایی را با جدیت دنبال می‌کنیم
🔹
مهرداد اخلاقی در نشست ویژه مجلس: اولویت‌هایم برای اداره وزارت دفاع در برنامه پیشنهادی ۱۶ مورد است که یکی از آنها باز معماری و بازآفرینی وزارت دفاع آینده است.
🔹
باید تلاش کنیم که از داشته‌ها…</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/467983" target="_blank">📅 17:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467982">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d9550576d.mp4?token=bM7iFJi_29984LIwVC1uyfnoJgXZgKWuwYVjabiDDKpdwgGk1vsX9awM_tmYBpWSTOQwd9k5PwBxiuwWPwgGm9UjUOUEz2j12IGo-p9t3h4_dnjQRy0i1OOTymYqGwnj2L_ywOWuh_FXqyMoG5y9CEgObBYAq7MxSU5l-Tq7mCQi5GvcGqOouBRo3NQfVHafPKWjJIli9NsxbFe6IyVga2FmdGQdoZx-BRMFLmXE0hL56fYJx0j6NMJyrHl7WtOJUritZ8Uf-QkKhTSa2zf8b-cO4MFbMh1X57FNobReGMt7x1Vy_ClhfH-JKPALWD9TvSuD0nxV8XFH41TUjwyvJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d9550576d.mp4?token=bM7iFJi_29984LIwVC1uyfnoJgXZgKWuwYVjabiDDKpdwgGk1vsX9awM_tmYBpWSTOQwd9k5PwBxiuwWPwgGm9UjUOUEz2j12IGo-p9t3h4_dnjQRy0i1OOTymYqGwnj2L_ywOWuh_FXqyMoG5y9CEgObBYAq7MxSU5l-Tq7mCQi5GvcGqOouBRo3NQfVHafPKWjJIli9NsxbFe6IyVga2FmdGQdoZx-BRMFLmXE0hL56fYJx0j6NMJyrHl7WtOJUritZ8Uf-QkKhTSa2zf8b-cO4MFbMh1X57FNobReGMt7x1Vy_ClhfH-JKPALWD9TvSuD0nxV8XFH41TUjwyvJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینستاگرام حامی رضا پهلوی شد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/467982" target="_blank">📅 17:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467981">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTNXE3huYfxnSPcElVbcHCNd_2mbCsD1i5i4sn47bbndXw52fJ80G4Rw0zLLU4qASaDi_eGuBIAG17kxDwfSDdIDW20RKVIt4bcTvhfQtcDlQKG-cg-TM-r2G2lmbBUfwOOoe4CklKCqfQk8khTdarhjMwlWQDzFsg8NTcmuOyJGrE1jprgti7uD6Zg5ATfTZNtAkpOcF5GoxozJ8880clq_CbS_-HEpelBCkCceT9BI0lny6sAuPKuLtVsz1IDkyTyL08yFAy7SNg5MF_Q8WqZjLOKseXOCRC_U9I4GmO2rKtDDeA9jfjajMKsjy0v2rQVeStRTV35ocC1Yk3cgdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: روسیه پس‌از اعلام آتش‌بس انرژی توسط ترامپ، به تأسیسات انرژی اوکراین در کی‌یف و خارکیف حمله کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/467981" target="_blank">📅 17:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467980">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfwkdiSVwqgjlnaXNPRMETobwdt4QMFEUHisTI-bbUea5T6YVYWdRaHurlHS3QFC4dIeUD8y1JXnY7yuq4QOScHMzK1qquoBrTdSt9U2BsQT1zoEM6ADoNjllqwzN_19qzfE54IFlSPNyGO2NjPkh1RPNMUKhcL7gLqDpl1bq6Mpl_w6sGPAs0zog8HCU0WxTv2aMHEZa4renOHipMHULKT2fJKyFgm0VMpoiGVBUYXsaHw47dcY0EuPHClS-2GdFsJwVIBDkz3ilEVVGhicSFq8fvtg2W2UBoehPoQif8xal6kbsThJ_Z_TyGAY_5uddua096U1wAfAg4uCCZMjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت هرمز علیه دشمن کوک شد
🔹
زمان در محاصره، کالایی کمیاب است. زیرا دشمن تاب‌آوری شما را هدف گرفته نه صرفاً خاک یا ناوگان.
🔹
هر روز تأخیر، فرسایش را عمیق‌تر می‌کند. بنابراین بازیگر محاصره‌شده نباید زمان را مدیریت کند؛ باید آن را به سلاح تبدیل کند.
🔹
درس تاریخ این است که در موازنه‌های نامتقارن، پیروزی پیش از میدان، در ذهن حریف شکل می‌گیرد.
🔸
حالا باید دشمن به این درک برسد که هیچ سناریویی، نه فشار حداکثری، نه عملیات محدود، به پیروزی نمی‌انجامد. این، مسئله مقدمه صلح پایدار است.
🔹
حالا تغییر الگوی تنش در تنگه هرمز را باید در همین چارچوب خواند. ضربه به پیشران کشتی، برخورد جدی با کشتی‌های اماراتی، مجازات کشتی‌هایی که AIS خاموش می‌کنند، فقط تاکتیک نیستند؛ پیام‌اند.
🔹
تنگهٔ هرمز حالا نقش یک ساعت را دارد. هر اقدام باید هزینهٔ عبور را از سود پیروزی بیشتر و ارادهٔ حریف را در محاسبهٔ شکست غرق کند.
🔹
خطر اصلی اما پالس مذاکره در لحظه‌ای است که  ادراک عدم پیروزی در دشمن هنوز تثبیت نشده.
🔹
سیگنال گفت‌وگو در این شرایط سنگ مفت و گنجشک مفت نیست و می‌تواند پیام قدرت را مخدوش و زمان را به نفع حریف بازگرداند.
🔹
در محاصره، آزمون و خطا تجمل است. ایران باید زمان را فشرده کند، نه آنکه با تردید آن را بفروشد. صلح، وقتی می‌آید که حریف به عدم امکان پیروزی باور کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/467980" target="_blank">📅 17:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467973">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pb5NORyF6Kocoe7LN3RJsCmanfZ3tfE-1BdSx0K6u19zpiIaZz-meu_0cVxdF53ogQXsX5Izd4OEUzQScZ2ETIPPhcr9_nje-rD0qrJfLN3LJWTabT-OiS0Fqf3FDPCDfYp6QiY-Iz4_sZmAoprdLSEsftG2jpPKZ9FyQmA38mKywuR1iSW7jX1ipupCkUSZ8lUzbEJXHlFc192o0mUTwhiLq2cxt8XWsgqW_1g3EBbxqF5wCHD0gWfPIeh6oHKpinYI1QcWC8PX6aZbSfiBm7aPqk0LBnkRpbQtn6ci10xwf9ZzgBqhBHxuQ9mpoxyIsYktKJ-1cyH-9O8h8yQiqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qoZBoZjnrwuhKl1nmgDWD9hbq4Bd_CoedkglUsstv_DvUnaP6fxH4lott8BQRZzqQCjFaB53cvnKvucYVvc7cr2TrG9_rWDRoh3iekNA-hmvXW2GRTortCUYJE9FkZShDp7YkgJ703jFiH9vZ2v20--fxVdNRwbeAKo8t-xhIDw4L4fZOPmOK9z10q9joV3YMZGf3cwlmFRpF_5RDsryxx7Fkq8V2d69pwR5WGacqqmT5lNJKYMUh9hqOEO7ij76h_uH-HZv19Oa8Leu804kNLesakx44ECYfi9VaPi_tMM9KLj3CjsORmabAwvzZzoOwqmb-q6ZVUxxd97itWYYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5L09LnwCzutoRAK9iow0i0EY77N_J6JDyag5BWW2OA0r7tNYBwifVk98x8GYxpXicQ-9JzCdrJ_BrZVNQ5SvyVn4Hz3Tmtwj9_4cIVslzZNwCKzX_EWn7Txt_ChNGny_VFerabBBgnfmJBT2O6yN1rfTuLOSDukM9rZdm_lWL-BeSPiJTr38LwC5MpSwFUP9mq6_IMS7uuSI0pKHd3OMK6Wa9O6MVsIVACsBDaArbKHDlI-C-QQ4GrnltaQiIvvTRK5Tn2R1w8oW6wBV4cEDDCPwZKlR3eeV0QXGBKWKQ91uajehrbrUlmRDemHuAZKPnKBS_swAkgne9mESfR1Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjDCilnvUshb1LSSu8DybdTVmS0PT-Jk0uI9WWmHFw7zecY4Bt8r9B8ugUQ3tktAFRP7IwhHggRtT0w8zsCZw798dukRJ0maENQjEZrRElW3zyke2Ere-Cg3PYYmgie1qPdUwMR4_irYVEKmkZ17qhYNiI8Ay6NOgdUjlNwmN8G7rYKUZIgtWPnp0Lk47XqHwVmZIAIo2jh4ca_zAdug-nMnHHqypOIkftacpkLW9IHWhhX0ygeUm7jaWoz52Cyy1uG4qAQk-DnR7y8xo0SF44IMrswsOhTzfJHnNci5zS6Vaq2WN76N2AVenmRXzIJQar_SfInmXXD2G5f2jK_pig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTI1eB9lRX1Uv1hFltXXf8byg_Q9wsmZc2NeP1VSvROj2fii89gBMAxg0EXBB8_BpFvM5R9qVgahHikWolwaaFTVDMPHrBWoKjQ0wbDZWMU0jH7w_PENEkV1x6N9xxjtdYk1pfXU8JHb5MD0nykw_JgcNcjmMjVpGxrI2npu-ztq6Ef77k3G8fOC_h0rOcbY6avhzOCoafWzw2PijiDko-v_mKnldTHrAN32fFyOBdhBw6fu4_6ef1YQh6XBGOeWuR30RgKQPmAuJP_HAMGpN-ASxZ2vzfl5ar8_Ts4DWQbaMTwDvUouM_TDAJZNQAQv2wj2xxk8goVhKf6wdFVlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyjHLbxcUPE3s_jjgT_v-16SyEnQv_Dik7FgX0sgm9DBwxxTpsWpGgX_77xHmslxXelekJP0VIEoXbDF6_OOJoSJow1ajlCFToxaMlCOMtdfmmenMzIWmkdnVXD3-v7t3H2NEbF9W_C0wGvxs_QBsu7WcLEnsnueX9Io5jZKX69a3_zayE5L1v_73Zb7NCxtsMitdn-tauuL2GZLn3D6kSsvusyiGdL5GGIEKTCoJAiBajKcDOl2Czkv2DLPJjU3R3IlOxb30EDMlT1-ALiMM5YJmqRA-VybRJ7NEyyAqO4qiKxl3DITkwl_FSo-IR1ZiSBWFO8oabl5wd1bD8C61g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otVVRxYKfgT_OMYwQECAp4p-xSBiWIMwejOBHnf_QRkTsWsTKGquubAkiYKJ7LT9UCl5-4W6P4ogjx33qz0koj_SkYPUkKDzZiE6hTAYOAIyQ3Arf6kLjjcLIeCVracZyrPvoDBb05xx1FS02CWxQxMH8oYOVVy6XM_GpwnPXPy2ht768Wv4DbxVd5w0HR9YkhZq9YMPRrOnRtgg5BPcoDwIsA8edN3AGCRlUMP4HA_5IRP86lDq19q4ZhjtzobbrwvtKedLe3536hsam8l1MbtwaGLEIknFAX49zvMwgR5kbugg6hQoONdOfvdf2chkzMfp-_axKXr2g373RO0j-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جان‌فدایان باشت کهگیلویه‌وبویراحمد گرد هم آمدند
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/467973" target="_blank">📅 17:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467972">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/221c7424d4.mp4?token=U5ycJYiEREqsANznlkzETOHrGorHrCSiQvet4pbH2cum5kMxdQuxNQ1j71tobNUZwZA10tWdiCFidjBqmcrEA-74VlgGwjHwXsaMM7l43qXTMQpOby2XV_KDw_J1nUKXyTOLjIID_29pX9IpwOpPjWT1q2e7UZjo-NXtACkCGo9kp8cl-SDrXE2DZzvpdI5iOJcnwkE__5dYZKAti3qPc5wO2zQ8i1V6GhBzZeypQTByfadD9EXMu-ZN1-BQowTGcj7CCxCLa-N-vAbN-xzNBo4Tp8tgEmsh_r1jhpOYoj6ioZovfrSYmuxXsJDn6drcCFN5YANB-LgtwjjTOVZfBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/221c7424d4.mp4?token=U5ycJYiEREqsANznlkzETOHrGorHrCSiQvet4pbH2cum5kMxdQuxNQ1j71tobNUZwZA10tWdiCFidjBqmcrEA-74VlgGwjHwXsaMM7l43qXTMQpOby2XV_KDw_J1nUKXyTOLjIID_29pX9IpwOpPjWT1q2e7UZjo-NXtACkCGo9kp8cl-SDrXE2DZzvpdI5iOJcnwkE__5dYZKAti3qPc5wO2zQ8i1V6GhBzZeypQTByfadD9EXMu-ZN1-BQowTGcj7CCxCLa-N-vAbN-xzNBo4Tp8tgEmsh_r1jhpOYoj6ioZovfrSYmuxXsJDn6drcCFN5YANB-LgtwjjTOVZfBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه: سومین نفتکش سوپر تانکر طی دو روز گذشته در تنگۀ هرمز مورد اصابت قرار گرفت
🔹
روابط عمومی نیروی دریایی سپاه: صبح امروز سومین نفتکش متخلف از نوع سوپر تانکر در تنگه هرمز مورد اصابت قرار گرفت و دچار آتش سوزی شد.
🔹
این نفتکش با خاموش نمودن سیستم…</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/467972" target="_blank">📅 17:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467970">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLm1DWP_tLtLKkWvKZXyDMrQA0DOdTUvRo8NEm1M4-HLiq5D2nNI8646CuYF1obdjLZVykNRxpp56PmsP-Vnf-bS-atA9J-1PDpxfXmLYIzl8Yc9xjxLs1U3tbfOQ3JE_Y9i-IjLAB5gRW_ORlyxvvAPeUMUUJsFDhS2qFMYd6qpJu5unWI8FheAvmzbk_9c74Jm6KTQnY1SM--pL8RcxHfpKsZQlIh1YGofod4bHhLiViOgcKMt64kODV0kDeWCR096tKH0QsZ1xd7pK0BWR8sjpfDBX-Y9lN3fI1LNavgf_l-yK_Erc4lW4tzhXIhAlWRhkC6egZws1OaHCMBV0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سومین نفتکش متخلف امروز به مین دریایی برخورد کرد و دچار آتش‌سوزی شدید شد
🔹
نیروی دریایی سپاه: یک نفتکش شاتل حامل ۷۵۰ هزار بشکه نفت خام، بعدازظهر امروز با بی‌توجهی به هشدارها و اخطارهای نیروی دریایی سپاه، تلاش کرد از مسیر غیرمجاز عبور کند و درپی برخورد با…</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/467970" target="_blank">📅 17:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467969">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712d3833ba.mp4?token=ogUZspZ5IEyl9bkDGUosIYg--oZOdPLdtaxyks1BbXCNhUaCHyqFtTPiQl1smm4V1T6H98zmoSdcslwmrEABh9caUm8pp3GnxkweKU97HqYIXmZ8z-JV4rc21T8oJYIJrmF-VtHLBT1TKx-d0qfQg1S3yTW8xShPfS7FsOcaW807tOh5Y4SMjDPkPc00XC85fVU3ce-3MKQJFukP2yDjn8U-_6-fbOSAYNN27cBvECM9jXSRBE62LWJmNhZc5EkvC3HeqZUzvNAcj6yg3jZwUipYkXB7tvUwH07f0oNIvzN6TfwjJIw3kRkgl35E94g3WsyNz2XayHr8li2Uco2C7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712d3833ba.mp4?token=ogUZspZ5IEyl9bkDGUosIYg--oZOdPLdtaxyks1BbXCNhUaCHyqFtTPiQl1smm4V1T6H98zmoSdcslwmrEABh9caUm8pp3GnxkweKU97HqYIXmZ8z-JV4rc21T8oJYIJrmF-VtHLBT1TKx-d0qfQg1S3yTW8xShPfS7FsOcaW807tOh5Y4SMjDPkPc00XC85fVU3ce-3MKQJFukP2yDjn8U-_6-fbOSAYNN27cBvECM9jXSRBE62LWJmNhZc5EkvC3HeqZUzvNAcj6yg3jZwUipYkXB7tvUwH07f0oNIvzN6TfwjJIw3kRkgl35E94g3WsyNz2XayHr8li2Uco2C7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دادگاه رسیدگی به جنایات منافقین: دولت‌های اروپایی میزبان منافقین مکلف به استرداد متهمان به ایران هستند
🔹
بر پایه رویۀ قضایی بین‌المللی، کسانی که متهم به جرایم تروریستی و اقدامات خشونت‌بار هستند مشمول پناهندگی سیاسی نیستند.
@Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/467969" target="_blank">📅 17:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467962">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnpicYsjLgknsmEHOKnT3z_fEElqLeSfqwWRrobNgFgNNik_c6psURsKxnXgyJ0xhoiUWyn9FC8010Ur9E7N4Ae1x36GSDLVmaJhiOuE8-vr0tnqsMWKG-rxcdgEXE_-gIq3eCF_PR8gGYI6T2h27gEXagkkMYByppmRxXNzgWqe84pvJqZWeOUpZ4AZ1B2il9VpYe-tQUprb189q0dgfaZxq030CbK9HrLLPfuimq_UCIj4VsavOFtzQspFdPKW4Z_09kL9B2M-btPSoLKxu_Vnsf96L-0zGKRQsDN69UPvfoBPaGQoyTAt2kaITdWaK419YmikCx3vqUBmC4kIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCeSfaXIsxOUU_N7wQGRGpIkYJchGzaZRNC_k98j9RXJJkC-5msPYbi0MrA5vS-77IHyskDcpNI09w2BK1kQLBHCO_5s0UXiE-bwoftF7wJIfkPgNzLZttsHWn4e6MTFd3jz2CGkbgxx4EvII4TYUaQypFlgu0dPpS0lkWYWvIyH8iU8dknuGWhh89s-Lc0rKg3nLRiAZZnC0QqCl9QjGmNCQ6sYQSyfj9EWNzpCv9Jcgwsnhi4xRt5xAIbkAFoqp05Z4tKicuDkH9sSEulmP61V2SsFVh5pzBsOBZVLgVDSg3hI6xuf2KjEgFoFh6E_iY-5guyQD0AXN5h0h0lLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFoXqIEkT5Eo9uvaeSxIUjoknY7zBEIcZsVCbgjMfHRp5phaazWuZJWMO1KAFVmQ8Ae6StO2TzVDynKnvRwr8uwhKcNhTwh2e1MHYEi0GDHgLfNBYKyfZ5IzEx4Xr78zxVQ2bplXGgZ_KlkfXd8dSzohPhvQYvcgCx_iq7Mj60VzsEmn9T6Lysn5OIOIcqp_TEWY0d5rsJoepoddgyGba1AbqGANkzcEXCfXmX1IyxvxJhJsLocUtKaOTZ44RMBP7lvkEQj198KYGxNV5n4YTZC_Xy1ze6U_pPpj9O3qDy_JNkhfFnjAcVmjNx9of1jsHtiVhM1n8FQbXZsEErRuLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mb6xV9L1dizQk0Devs7zfswIjSmOT2IPn1TbABFQdIe1YLN4bRfGuUjZXFCPhJF5EOaDDCv2TxujmVhoCWEHhya0-5TjG_8xmNHC2a-Avo_YfxGhPt4xMb3uZ62PEjK7zQDjfnGKlSsJ8e3JiPWy3Th-q4pOTy0WRwoeOlJCavgUfRanxFPPVZZ21yg2VGAgIpfmZvng3YvSAkq1ImKIFzUb0yDJoxJrcu1p3SB6twaYLRQduQuK0TXjw4qPYle78iIlkfwDmFefaRfaUDDfKnVa-LMsEX8zmAqLuN2dH1DpNLiCMbztYecafgBRCZUWWGCc9uQFuLCBD3uf7WnBlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTGodcKHxFou8sR_l645F-dAr3LBSMe9EsdCLshQxtCjd4JtjNMPdPhsFwQ6c0yjhriOLCQbKv9UxjND0x6YHtwN5CevZtItkV7MhsSJ8eUvbqpUor37fsHVgQP-6GP-5H7XHzRAoAZS8W0YfJonpliAnZ0-T-kw5o9Ag3mFCEv2AAgN1l0bVeuLbhMdc7axpizPNfvcwKyWBsN8MobFuYgxYxMUEcGA2ATS5nCDjafpEub6P-5xz4wkW7SIgZvaBtXgA5OXkQfb8xF_6CK7TU6gYr4yUlg7_LojUdXzEHxcwoH7W9D1LwbfOZwLxai3LjTuwiAwPWmeoKjiWi7mcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8oTU8RbueeVxCjccpTRgIiEuRdtgSRDgUj6sHW5lba4HoO-hUwKJNXc7tI43N2LfrHNPy7a7HxA_4aWFeGd3T_SLDZsVwp3KiNE1bjYvM5G_CzyOn4GM4KjQLjfiwAvAgdE1YmIEgNgCgYZJTuSOaFgB1fDxFVP4gtr-DIxrjV-by3RXDvI4SMy6F5ZOdbpT8aUVmv3lrMWyxu3HmP0ZLfdHds4uDvH_YQ9Am7XdtGzFtHJRKTMgNzluuCrebjFiov6XdjedK8esHMlvutKXHRYVPsQJTquoNTkLqyHdWoK7PeJ18_xn-KvE6-2p5dv7S5PCOVNeRm9jtAZlB5K-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMzxLMy79McyvBec6AJ92iH0-y4VHqNyj7RZEiOwUHqJ74_2OiMPkPXVhdvB3IGO6_PWNYz_WeetFZyNFthYR-4RIjen9Ht-D2q-jcCDHBk85rUMAUvnansVfPuObB8OLuaGAReZ1b72bEuIW9rUr5jztmWhADFk0dyE2ol9nzGubj4UaA-E8vad-OPKvjKQpf2M_T60C9dRgXdjaFVH8NkwWoxqr2e4a4pEEeUxrBf8DE77rHWtWajuh0pn6wGF-IO0FCZriGArpwRZXKCGZle2qjlySvy1Q4OGTiu92kCp2zWraf91z3qP7fDav7qfOkWccf4Uw2-l-whwq1GYMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کرج، شهر اقوام و فرهنگ‌ها
🔸
۲۰ مهر به‌عنوان روز کرج، شهری با پیشینه‌ای تاریخی و فرهنگی غنی نامیده شده است.
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/467962" target="_blank">📅 16:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467961">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbARstdho1OYz_Q5QHWY1SEY1dlW8CCu1TAcazOcF0fnBIjv-TBC0XOuVRFxc0hlI-kq0dWevr3ph0t9ykwtM4rh3RNhte5VN8Dnx32FwDfp1dVWXRHlPoUUqUA1PX8VAjZ86z3G-WkeadO0Jot7AYW8O_Hc1CS9cQafsY-4e29Y0o9cWJvMeSpopCmVsEdwDa2QR4PKaxmQoLhEyWE218_Orxxa2g3ezyNx2Lp96-ZMpk53lRcVTUTyC-MK__vhZ8WMntaSH0riyACRTyq5BmKt-ShbPGVUAXoc0bMinKHiGFT5PuztomdXTb-r4m9MILNIHxdPYIyl8ikVun1WYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی: دلار باز هم ارزان‌تر می‌شود
🔹
رئیس بانک مرکزی: روند رشد نرخ دلار با اقدامات متعدد بانک مرکزی کاهشی شده و این «روند کاهشی» ادامه خواهد داشت.
🔹
دشمن در تلاش است با «شوک رسانه‌ای و اخبار جعلی و دروغ»، این روند را متوقف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/467961" target="_blank">📅 16:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467960">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZn4K57hiStGmY_WE9v8eYHtupDvBfgGUn9taEDbv386l3oh9EKAvonq0U9xWeQJawbx5VQHmfTOCOv3lg33p04Oj2H8frBlNh_K6sJ2xWSDDMhWUYWfKKkVNVicsItwZvYFpy9Rhh_uSm2oCsfdBK-mxWJsJw_dn3ltnMACXM3pWN82g92Zo2fTLzidi9GBZcfO_JM0_bizQeNKouKGkkpy_Yrkbz_ADC7NPrIB_mJYuhdrctnmQF9ax3NFg3yH23WprR6CP0Q3Ei00psDHtq4EXFbRIlKzuUOJw_FCCjbFpl0HzslCAQE5_ecaxQfZ12ef1w_Wjf_gi6W0867MNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشهٔ محاصرهٔ دریایی برای فلج‌سازی شریان تجارت کشور خنثی شد
🔹
رئیس سازمان توسعهٔ تجارت ایران: هدف نقشهٔ محاصرهٔ دریایی این بود که ۷۵ درصد وزن تجارت خارجی ما در حوزهٔ واردات و صادرات که از طریق خلیج فارس و دریای عمان جابه‌جا می‌شد از بین برود، اما اتفاق دیگری رقم خورد.
🔹
از لحاظ وزنی ما فقط حدود ۳۴ درصد از تجارت خود را از دست دادیم. یعنی در واقع بیش از ۴۰ درصد از آنچه که قرار بود تحت محاصره قرار گیرد نجات پیدا کرد.
🔹
پیش از آغاز تنش‌ها، بخش اصلی بار صادرات و واردات کشور از مسیرهای دریایی جنوب جابه‌جا می‌شد. با ایجاد محاصرهٔ دریایی، مسیرهای ریلی و جاده‌ای به‌سرعت به خط شدند تا بار مبادلات را به دوش بکشند.
🔹
از طریق کریدورهای جایگزین جاده‌ای و ریلی صادرات و واردات کشور انجام شده است بطوری که در واردات کالاهای اساسی هیچ مشکلی نداریم و صادرات کالاهایی که صرفه‌ اقتصادی دارد هم ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/467960" target="_blank">📅 16:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467959">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a7aab48d0.mp4?token=pMqajnRFJeiCFegeF5m0VupYUoVSSfLE9vzSC6WnvRtUv68HYuWjVw5-4YR87EKSb1bkXXvAa6ubuenu_SKvdmaHn3EoJL8rDy0-FkLsSl_dh-NEXvNBOG6vhKIZgcsrdcI-J_l7Jn6WpppAbNiMKKiwWJJUb5ohIP5LGFLGjVNW19A8y6sLJciwhYUmv3QQE_mUhSHWhB6X6r3wRhf0eOBJ12oik6659QgQQOeeYbsILhN0Uqd5E-kzXZdA0ErSZ3L7P7fPMzq5wIOfuqTzEQc8Xu99edN8ezW0sxvplyKZnfhleaiut24eckDcpX_kKTPm3zoWzOQZxKRKJv_Xaxw6M5zw1qSVdX0mTKdA8wsvtissHmVmBTUdm5slJZSa96qxbEdz_0t0cKHTDgxRjT6p5eGMHnLJ_nM36JmzInCPvz7B9v70ji15Ra0iiNE3qEqdRgI-Tg0YJ59q5OEk7QekqxRKLf7GdN8jkh_C7nE2wcNgFitqKu5Dc0CDNULe-CTXj5J4S0j8PssbGiQaNWaG295EOAMQpFdFrP0fNgXQEjew1j7PHDAkVPIbBkM55AfpLPmCvxO3SlFPBlrn22o6h9z-bk2xAa2beVxk1-C2m6SrM8D4xvNaHg3aanIgUzimP7cJM7WdJWzmD4KXQ7q5vnGd9iXMyFtAjLUbI4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a7aab48d0.mp4?token=pMqajnRFJeiCFegeF5m0VupYUoVSSfLE9vzSC6WnvRtUv68HYuWjVw5-4YR87EKSb1bkXXvAa6ubuenu_SKvdmaHn3EoJL8rDy0-FkLsSl_dh-NEXvNBOG6vhKIZgcsrdcI-J_l7Jn6WpppAbNiMKKiwWJJUb5ohIP5LGFLGjVNW19A8y6sLJciwhYUmv3QQE_mUhSHWhB6X6r3wRhf0eOBJ12oik6659QgQQOeeYbsILhN0Uqd5E-kzXZdA0ErSZ3L7P7fPMzq5wIOfuqTzEQc8Xu99edN8ezW0sxvplyKZnfhleaiut24eckDcpX_kKTPm3zoWzOQZxKRKJv_Xaxw6M5zw1qSVdX0mTKdA8wsvtissHmVmBTUdm5slJZSa96qxbEdz_0t0cKHTDgxRjT6p5eGMHnLJ_nM36JmzInCPvz7B9v70ji15Ra0iiNE3qEqdRgI-Tg0YJ59q5OEk7QekqxRKLf7GdN8jkh_C7nE2wcNgFitqKu5Dc0CDNULe-CTXj5J4S0j8PssbGiQaNWaG295EOAMQpFdFrP0fNgXQEjew1j7PHDAkVPIbBkM55AfpLPmCvxO3SlFPBlrn22o6h9z-bk2xAa2beVxk1-C2m6SrM8D4xvNaHg3aanIgUzimP7cJM7WdJWzmD4KXQ7q5vnGd9iXMyFtAjLUbI4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  سخنگوی نیروهای مسلح یمن: مزدوارن سعودی را وادار به فرار کردیم
🔹
یحیی سریع: نیروهای مسلح ما، یک عملیات پهپادی موشکی علیه تجمع‌های مزدوران سعودی در مناطق رأس العاره و السقیا انجام دادند که ده‌ها کشته و زخمی برجا گذاشت.
🔹
همچنین عملیات موشکی علیه یگان‌های…</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/467959" target="_blank">📅 16:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467955">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWVgf_9W4uD-4e6_DNmepl8pupOFKfAfU3p4BPYXsvP_2uEvSwZYKUkclRh-3-LgUBtxapdMw7cviwzTv5nMwkWpcN9eYHQ81ssR8qCARYKN9EjDAIFxHQ-GBwTpvVBYHF1gKwYWbL_fY2DpQgylnIPmfAEIf5UK9c4VYUUAV0OZHDmxxBxvYw60dvU7vDQUkVILcS4qOT-jIM2pBlFlBvKqdRRJheff35CqtO2Yo9VLeUap3IqA3UvhqXWXc3nNEZ3ZYf9p2kRGEtds-Q53O6aVriJyhLiUcSrnXrDmcED88NHHML1jSK4jMD3SL0txipTyPX3qUvTek0CRuJRp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Idsc1s9lyR4-8ju60KLoYsRujjNL8Pvmr94_Ti9VCbiQpPmdzFj6ikNHMYeZUraEv0bhzDqXL6i3B8E0QxkFpzWBxdzCrV6Xhvs_QPZBJtJ12FNccIiHUfeo60kR0StL3v8yTl5qJ5C9swpfqY7X4LGrKR3IUNz5W3h4nQlocAA4fvx8rIc3RRBxzVXKDFqZ0yJTqj2_cfQj4cL5KJQJ-BKDAmbv2DY2NNIV_nfp0Phx17mWM8nmPh43_ueXzNkSGRsu48Txz56xqdsG3KPaF-H1UfV-_zllp9hBRp0ElmNmBAaAxaCFxYidokGB8h8znXSN_GaDhzx2d56kJWYAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTpi8jzjloTv_Podh5gDuVUD2zBY-8uu7oVSFuHcjLwq2mBYVAm8TStB5vzVJURcEL8S-HYKw0eR6jk5fWVzr340mO8DqkhqwF-7XRvH1C4y1fkJpcY6JdcDMVsrLEzbER_B3ELDYRClhkiLAdj2GVcbKlfwiA0_AnPNKYk2Wui_R08fc0vJ_c8SsLxYm2z__WOYPpX9azEeFdn_DBy9u__0T3giGz86YuNZbU85NZj5IuQ7Fpwx6bB0u9hnny0WXBlh5FERwlfyWYraePoRPy1hwPheRUu5ZXFMga_dSHZtLxFy2zYipnt3Q45OsbvnyX9aTSEL4N09qmuCJUC6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ylu-9qGh-dazltoUeU8xsjHh5BU5FHYq09nXt5EYrbwAcJDMvT-S2A6f50Pe0o2tWtk0ML4f0EJktffvyl_PN9etGJZjdu8Vci-IFdM0vQd1Cg_wBajgipopxXNnypZbX9rCY0DPUnzdjAlWC-SmKjX4PYdZ6XzwRiEs-h7IJoJ-V3D7cEpN30UiPfMLh5e8Nk3VxbKAsnAu2fm6MFe-tf4Ow5GJ_l_muFyPyh1ZOWTv8HsPRu1cHBUlHjnJ4kAsC56HICphgBlNrbvvcrNqqszIaZiOFlANkS0EZ2mMJmQqNfIDt1-M4TBZrNR5l3mqGXmhvIufNYvnbAn94Ona9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از حضور رهبر شهید انقلاب در حافظیه شیراز در سال ۱۳۸۷
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/467955" target="_blank">📅 16:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467954">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KB_hX_XwOhUshHzjYdEii5JQcTchx5BQ_gLrrNH-W7ZFCLuKof2kexLG6RAauXkVvME21oJaYoBnMrW8otcwYVOlqlcQMPQrjB-7PyaNTeLnkI9k3ybhU1GdianlSyu69BxOwjaLPy1mCJiL55EDypK3PAb2dJYobuHSjLaNcV4eZYo7pN24qndvlfcChfAv0CMvZHrPdRyYeLiqtYDQS3AxzhJAt4Qpimz-s86Fk4v5BqJAZpXA0hHl2YuxBuAfnWzceJ8S75by82pvy3vJGs4v7HlSN6TWMNFsxt-de2YV40D3uEXQRuKJIU06XwFUFuopoS_jlV2jyMgnVBAstw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفر در وضعیت بسیار وخیم است.</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/467954" target="_blank">📅 16:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467953">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دسترسی ۵ پلتفرم رمزارزی به خدمات بانکی قطع شد
🔹
از ساعت ۱۶ امروز دسترسی ۵ پلتفرم صرافی رمزارزی به خدمات بانکی و برداشت غیرحضوری محدود می‌شود و کاربران این پلتفرم‌ها امکان واریز و برداشت وجه را نخواهند داشت.
🔹
طبق اطلاعات رسیده به خبرنگار فارس، تصمیم برای این اقدام در کمیته‌ای در کارگروه مصوب کمیسیون عالی تنظیم مقررات گرفته‌شده و بانک مرکزی با ارسال نامه‌ای به بانک‌ها، اجرای آن را ابلاغ کرده است.
🔹
پیش از این خبر ایجاد اختلال چند صرافی رمزارزی در بازار ارز و تصمیم بانک مرکزی برای مسدود کردن یک‌طرفه حساب‌های بانکی این صرافی‌ها منتشر شده بود.
🔹
با این حال صرافی رمزارزی نوبیتکس گفته است که این محدودیت به دلیل پافشاری این صرافی‌ها بر حفظ حریم خصوصی کاربران و خودداری از ارائه اطلاعات آن‌ها اعمال می‌شود.
🔹
این محدودیت سه روزه خواهد بود با این حال احتمال تمدید آن نیز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/467953" target="_blank">📅 16:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467952">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU2g7rz9pm2cs-lBnxXPwYzbepIYpv-p4GMm8Klp4vHIJvKwXFnIEy8laq97fz0hx2eL0pHRHDlgRKSznGpPIJoDSWiE7yG-uV4MkJrPktICGrKcfb0VbqFsBSUXs_9-awzPWBAys9VHCEHqLz4r7mGVYNOtOtR7mq0vwYbXuuDaNVid5RHLUK9njPuA4fX5b_mgmGezwZNIof89g-6L77yI3OjZG3nD4CAQwBDl3BWJKBjnZzvgV1SXXK94kB8H4h6HnkP0pe2n5jlmRvB8WQXmFIaZE2AlsIkfUFbDJa_HtWojOT53v8sGURy4xF4wMRqrWldfTnMYdwZ3-1H59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌وال‌استریت‌ژورنال: تلاش حکومت سعودی برای تبدیل‌شدن به قطب هوش مصنوعی اکنون با خطرات جدیدی روبه‌روست؛ چراکه دیتاسنترها جزو اهداف [یمن] هستند. @Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/467952" target="_blank">📅 16:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467951">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9198aee7.mp4?token=L381Jgqxbrxu_tQhdYC7QU0dYu8JmJHbm0YWQlzHhTE19KM8ZRyz4wXhpZ-Xg32-9CZ5LJkvFBwUpYwhHCkVKmOmPaS5TBYmlaYWgIqEzaa3aJsmIjawv3HQe5qKNq8Qkq36a_MlWKAUN6Sx5fjz5XR06Z0Ri3li5XbkT28wFDto7uAQetiDxRsRB9uvdnFbULIUKc81nAGPUdR_MR0W3nLh4jIeMTDKnMAZgPtrESPXWpfVf4ui4zPQmOQLp9N3D4C2wWg_ncQf_yKsNTJ2SxeajmqtXAPjwR68TP38dsO3PDo9VPrMxJkmBfOqxl3h_W8Z8gadoa__FuppoNYmHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9198aee7.mp4?token=L381Jgqxbrxu_tQhdYC7QU0dYu8JmJHbm0YWQlzHhTE19KM8ZRyz4wXhpZ-Xg32-9CZ5LJkvFBwUpYwhHCkVKmOmPaS5TBYmlaYWgIqEzaa3aJsmIjawv3HQe5qKNq8Qkq36a_MlWKAUN6Sx5fjz5XR06Z0Ri3li5XbkT28wFDto7uAQetiDxRsRB9uvdnFbULIUKc81nAGPUdR_MR0W3nLh4jIeMTDKnMAZgPtrESPXWpfVf4ui4zPQmOQLp9N3D4C2wWg_ncQf_yKsNTJ2SxeajmqtXAPjwR68TP38dsO3PDo9VPrMxJkmBfOqxl3h_W8Z8gadoa__FuppoNYmHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
انفجار در شمال فلسطین اشغالی با دست‌کم ۱۰ مجروح
🔹
کانال ۱۲ رژیم صهیونیستی از انفجاری در مرز با لبنان خبر دادند که بر اثر آن دست‌کم ۱۰ صهیونیست مجروح شده‌اند و برخی از آن‌ها در وضعیت وخیم قرار دارند.
🔹
برخی منابع صهیونیستی ادعا کرده‌اند که این حادثه بر اثر…</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/467951" target="_blank">📅 16:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467949">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
انفجار در شمال فلسطین اشغالی با دست‌کم ۱۰ مجروح
🔹
کانال ۱۲ رژیم صهیونیستی از انفجاری در مرز با لبنان خبر دادند که بر اثر آن دست‌کم ۱۰ صهیونیست مجروح شده‌اند و برخی از آن‌ها در وضعیت وخیم قرار دارند.
🔹
برخی منابع صهیونیستی ادعا کرده‌اند که این حادثه بر اثر انفجار «مهمات باقی‌مانده از جنگ» اتفاق افتاده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/467949" target="_blank">📅 15:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467948">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939fb64b57.mp4?token=cQGqj6Dt_n3xCuXhqCIdQKAvHU6AruHqzH8JwGkPrp_PtKU3mX_1o5TFLwpU2HyTwcH6heDCPJXPG4QnjiF_FWb8SH7x___Q4xFWF6w7jUbF4W7L_cazVnYCHjRdglBFrIBN3hECvBHy5MBR1jLss3EF7QcQocGii-qZcfnxeZ-MwnTjEGrrFyr1nICcEQIjDL483ExwlmJFOWp3u5cm2tUY7_lRTEqyMBcUdySp5Wv069fKij4vGp5MwqXK5hohVOiFjk-8G_8GrppzXybRV7e43z6TSbZUUp8_09TvdbWtFE_TaNNxJj5Ouvqhp9naNlA53m8YKp3o58VQjuuZXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939fb64b57.mp4?token=cQGqj6Dt_n3xCuXhqCIdQKAvHU6AruHqzH8JwGkPrp_PtKU3mX_1o5TFLwpU2HyTwcH6heDCPJXPG4QnjiF_FWb8SH7x___Q4xFWF6w7jUbF4W7L_cazVnYCHjRdglBFrIBN3hECvBHy5MBR1jLss3EF7QcQocGii-qZcfnxeZ-MwnTjEGrrFyr1nICcEQIjDL483ExwlmJFOWp3u5cm2tUY7_lRTEqyMBcUdySp5Wv069fKij4vGp5MwqXK5hohVOiFjk-8G_8GrppzXybRV7e43z6TSbZUUp8_09TvdbWtFE_TaNNxJj5Ouvqhp9naNlA53m8YKp3o58VQjuuZXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امانی: شهید ایزدی ارتباط عمیقی با گروه‌های فلسطینی داشت و مثل فرزند خودش با آن‌ها رفتار می‌کرد
🔹
حاج رمضان هر سال با گروه‌های فلسطینی جلسهٔ افطاری برگزار می‌کرد و با تمام گروه‌های فلسطینی ارتباط داشت. @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/467948" target="_blank">📅 15:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467947">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وال‌استریت‌ژورنال: این روزها بن‌سلمان میان کاخ‌های به‌شدت محافظت‌شده‌ای که مجهز به پناهگاه هستند در رفت‌وآمد است و توسط یک تیم امنیتی گلچین‌شده محافظت می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/467947" target="_blank">📅 15:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467946">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd2cb0f3d.mp4?token=VKQmMr3p5J3DD5bJQNckI9Fy4lWkDhOHIwuFj7lNaNbgFAcaxk9N-0yontWeJ8SWVa-c7EJhhS23nTK54i-hrhDEq3wQFFqISlwJHuJqzk819DUwsFg3zFuVCWwlOkzEnrZpFfC6JbMAyA6FSSvgNb3v7-DL3j23LfAgietPAD-mJPJNRUharNM1eKsrwxcxN6qv6q72cvozB8JxU2bC9w2M_fi301ZDjyoOZVcQuBdMqgclD8Y4lUQvRbXcHr76ezprjLVrPzktE57Aopxxb2qmJSU-_Ys9xoloAR63YnWY7VyrQs4rIAmhMMTZYUkle4qxMn4CW-e1nSABTgiRjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd2cb0f3d.mp4?token=VKQmMr3p5J3DD5bJQNckI9Fy4lWkDhOHIwuFj7lNaNbgFAcaxk9N-0yontWeJ8SWVa-c7EJhhS23nTK54i-hrhDEq3wQFFqISlwJHuJqzk819DUwsFg3zFuVCWwlOkzEnrZpFfC6JbMAyA6FSSvgNb3v7-DL3j23LfAgietPAD-mJPJNRUharNM1eKsrwxcxN6qv6q72cvozB8JxU2bC9w2M_fi301ZDjyoOZVcQuBdMqgclD8Y4lUQvRbXcHr76ezprjLVrPzktE57Aopxxb2qmJSU-_Ys9xoloAR63YnWY7VyrQs4rIAmhMMTZYUkle4qxMn4CW-e1nSABTgiRjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفیر پیشین ایران در بیروت: پیجر من قبل‌از انفجار به‌صورت فینگلیش نوشت «یک پیام فوری دارید»
🔹
اولین‌بار بود که با چنین پیامی مواجه می‌شدم؛ روی صفحهٔ پیجر نوشته بود که «برای مشاهدهٔ پیام دکمه را فشار دهید» و به‌محض فشاردادن دکمه، پیجر منفجر شد. @Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/467946" target="_blank">📅 15:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467945">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147c7ee345.mp4?token=lm5jdjyqAJVYkJ2BOyUNwfprdrUJT6fNod_F0mNz8CBV5HbOuhLFb0oe2ORsvLJURcDMbqLKEaSZ5EoGg7aGl0-lr_K6NwsqARSkwd0wvOiu_V2Aml52V6uznmo5DQu2801Q8sihDl5lo5rCY_X7HlhDyFeqHo3KOGM0iTPmCV0imWCJfsisuUhtXyZEkzVgy8ZNTY28uJyE6SXUz5bvAD_iJqd95W7vOuRYNlSosl8Gwuxsfe4Nwp9rM9bLDPz0m-nTMTNtwqVirytlFzZNuXSgJ9woY_le14X2TyYLdFMKAA_DD6eY_Is6jYRzCSw4SI6ontLlsDFp7j-IY8Ws5RavMaL-_SBx0DiPBbsMYlLs6bzVwjSAj3pCSXEJ5ezULARlLQE4xrAwvWGWKQURbgSzefWrdOi0TxRhKNk6Ukq_Sy30O7AcHFKND_T3XyUWTnFdEb7bgF66F1RLQTLIIp95PgJ7HrE5W44fL6K7GrB6-6EdUPcCufPuAkd84GzfS1g0WKGQrwl3gXCzVU3_TuEoJjOkh8TOKhj9RZsx260tv8OpzKCem7AXls8fPgHepIemff9JXEV_kh0ahBySmhONp9zf9cqMlzkpiDsBuKXy67kGgQ2YbAK-Weqvpgh2KmDSuGIKEk95XR7PWQMcTjoBdsi7CCrXk1jKRaXuVh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147c7ee345.mp4?token=lm5jdjyqAJVYkJ2BOyUNwfprdrUJT6fNod_F0mNz8CBV5HbOuhLFb0oe2ORsvLJURcDMbqLKEaSZ5EoGg7aGl0-lr_K6NwsqARSkwd0wvOiu_V2Aml52V6uznmo5DQu2801Q8sihDl5lo5rCY_X7HlhDyFeqHo3KOGM0iTPmCV0imWCJfsisuUhtXyZEkzVgy8ZNTY28uJyE6SXUz5bvAD_iJqd95W7vOuRYNlSosl8Gwuxsfe4Nwp9rM9bLDPz0m-nTMTNtwqVirytlFzZNuXSgJ9woY_le14X2TyYLdFMKAA_DD6eY_Is6jYRzCSw4SI6ontLlsDFp7j-IY8Ws5RavMaL-_SBx0DiPBbsMYlLs6bzVwjSAj3pCSXEJ5ezULARlLQE4xrAwvWGWKQURbgSzefWrdOi0TxRhKNk6Ukq_Sy30O7AcHFKND_T3XyUWTnFdEb7bgF66F1RLQTLIIp95PgJ7HrE5W44fL6K7GrB6-6EdUPcCufPuAkd84GzfS1g0WKGQrwl3gXCzVU3_TuEoJjOkh8TOKhj9RZsx260tv8OpzKCem7AXls8fPgHepIemff9JXEV_kh0ahBySmhONp9zf9cqMlzkpiDsBuKXy67kGgQ2YbAK-Weqvpgh2KmDSuGIKEk95XR7PWQMcTjoBdsi7CCrXk1jKRaXuVh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امانی: قرار بود پیجرها بررسی شود و برای همین عملیات را زودتر اجرا کردند
🔹
نتانیاهو پس‌از حادثهٔ پیجرها گفته بود «کاری کرده‌ایم نیروهای حزب‌الله از جامعه طرد شوند» اما حالا جانبازهای پیجر در لبنان احترام خیلی بالایی دارند.
🔹
حزب‌الله به‌دلیل مشاهدهٔ بعضی…</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/467945" target="_blank">📅 15:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467944">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/434a367fce.mp4?token=LjodfcLGhrA5HKhVLtX2KAFGxXqpJc9gzwVjTGcJbKYYY7755GJWBYx9NAbM7ZacDu2focoYureSYzd-Rip_utnv1o7ZMQtH7g-8N-yQ6DRvTg6aH4J5xZe0-nV_543l3iT_Lj7NltzrzlsgOUhfIP-XEoKJ1qEwLE-xTHPJq8c1OznDtFfo_bfk-JDksH2662wzCMKv7zoIXWRaxtt2bRBhNk9u79cVmPZaLVuZkGT7k-uYBQe_3comjCEBVT5m_FU_EM29uC4WROxkn_pUgW3HT6BHHzcyGr3KvrovK1BAFSP0An8Rg4o1mXYdVFP3uvXJkmaSD5Plf-YY0Lf2HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/434a367fce.mp4?token=LjodfcLGhrA5HKhVLtX2KAFGxXqpJc9gzwVjTGcJbKYYY7755GJWBYx9NAbM7ZacDu2focoYureSYzd-Rip_utnv1o7ZMQtH7g-8N-yQ6DRvTg6aH4J5xZe0-nV_543l3iT_Lj7NltzrzlsgOUhfIP-XEoKJ1qEwLE-xTHPJq8c1OznDtFfo_bfk-JDksH2662wzCMKv7zoIXWRaxtt2bRBhNk9u79cVmPZaLVuZkGT7k-uYBQe_3comjCEBVT5m_FU_EM29uC4WROxkn_pUgW3HT6BHHzcyGr3KvrovK1BAFSP0An8Rg4o1mXYdVFP3uvXJkmaSD5Plf-YY0Lf2HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا ایران به مغز دیجیتال آمریکا در منطقه حمله کرد؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/467944" target="_blank">📅 15:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467943">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAkGrty_K1GKyl8xwJcGJ_Hjc2Klg-YRfQ_KhQ8gZuRnoRmRjUcyLeU5N_2AeDJ8tov-tl2kjt6hBE_95nbRGhkYbBoCzAaA8HCG_MbJpvq0Sziuqewh2ENCsF4Q45_rWphHwHgz94zapwY9El04QZZnCSLVGm1W_mng6GWZlWsTOxGph93wwETaZNXg0oOSOLDutkYs8S9tmAL82snLGIM7fvRU96zEy92HKtEEFk95_GslOBat3fTlx5v-fM0TZjdop26KDu09fqWhS49HlIaaq2XGZFO_5zgtBywN-yLMJ9vGxq7JDmGHbdsBIsB86ZhXpBKZ0r_SAy9Ft5SpYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجاهد: هدف آمریکا از مذاکره هسته‌ای؛ «مشروعیت‌بخشی به جنگ» است
🔹
معاون دفتر رئیس‌جمهور شهید: مذاکرۀ هسته‌ای برای آمریکا ابزاری برای مشروعیت‌بخشی به اقدام جنگی و نگه‌داشتن سایه جنگ بر سر ایران است. در این منطق، ایران از پیش متهم است و آمریکا خود را مدعی‌العموم و قاضی‌ای می‌داند که رأی خود را دست‌کم بیست‌وپنج سال پیش صادر کرده است.
🔹
غربی‌ها در بیست‌وپنج سال گذشته، هیچ‌گاه نپذیرفتند که فعالیت‌های هسته‌ای ایران صلح‌آمیز است. آمریکا میز مذاکره را ترک کرد تا به دنیا بگوید محل نزاع با ایران مسئله هسته‌ای است؛ سپس با همان بهانه تکراری، حمله نظامی کرد.
🔹
مذاکره هسته‌ای بدون اجرای تعهدات پایان جنگ، چیزی جز بازتولید چرخه فشار، تهدید و جنگ نخواهد بود. این مذاکره نه‌تنها به خاتمه جنگ نمی‌انجامد، بلکه می‌تواند به مشروعیت‌بخشی به جنگ مجدد و تداوم سایه تهدید بر سر ایران منجر شود.
🔹
راه پایان جنگ، ایستادگی و تحمیل هزینه و فشار به آمریکا برای اجرای تعهداتش است.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/467943" target="_blank">📅 15:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467942">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee4ce1f7eb.mp4?token=DjNa6BTD6a6ejGvp2ml0GTBTTl-lLNzmyrNYQ2VIp1uOHMzPWdh4hrK6MbffbvcEgYGX-IgTVJ1vnz0RfxoRX453Bpa_hzh8UgDGfZf1CbYFPdmJJo8SiR8U8d_zllkJPo5i0-laAJ0EYmt_kaotCj_A1GC9v1Z0xdFMtn6gPQqVu35NOL7Y5x_OnxUTLI3T1g9YEVf0ltCydjBNxGZv-sLWEHl406AkWsHd2vgplmcOvcofneOh9EHO7B9sYGQPaqPPUYQIx6BYTUiGm_W198azHxr_GiTgi3hpSpYB1_9Xh03jy777jGxGwe_HVXT39mLDsw42Neq2m99Rxg0HnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee4ce1f7eb.mp4?token=DjNa6BTD6a6ejGvp2ml0GTBTTl-lLNzmyrNYQ2VIp1uOHMzPWdh4hrK6MbffbvcEgYGX-IgTVJ1vnz0RfxoRX453Bpa_hzh8UgDGfZf1CbYFPdmJJo8SiR8U8d_zllkJPo5i0-laAJ0EYmt_kaotCj_A1GC9v1Z0xdFMtn6gPQqVu35NOL7Y5x_OnxUTLI3T1g9YEVf0ltCydjBNxGZv-sLWEHl406AkWsHd2vgplmcOvcofneOh9EHO7B9sYGQPaqPPUYQIx6BYTUiGm_W198azHxr_GiTgi3hpSpYB1_9Xh03jy777jGxGwe_HVXT39mLDsw42Neq2m99Rxg0HnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جانشین فرمانده نیروی دریایی ارتش: متناسب با نقاط ضعف آمریکا تسلیحات جدید ساخته‌ایم
🔹
دریادار بمانی: در برابر تاکتیک‌های جدید دشمن، ایران نیز تاکتیک‌های جدیدی به کار می‌گیرد.
🔹
پس از ضربات ایران، دشمن عقب‌نشینی گسترده‌ای از مرزهای دریایی ایران داشته و اکنون در مقایسه با جنگ تحمیلی سوم، در بیشترین فاصله از مرزهای ایران قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/467942" target="_blank">📅 15:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467940">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0930038d1c.mp4?token=O2H1dRKW5DZ9kqIlx4Um2jq-prSc_uSdLVd_PVlltpqnAGaeD_kqb8EN8wUdngoHBvZMDb7XzfQMTpvnvpiRfbmh9LPiOY83oDqX2Atdyh_8EWVZDgvsB8rGAdr_awIo0qB6K2wZ-Np7o02o9wOUlTSkFM8uUDaK2QN2kY8e0OoonGkwqLiQ4CWYmfNcn15cgsoubQs_BOa6OB0exeiM5tqJfgv-yNLIV0qhYW-yNSfiQywRSNKbvRXSjnvax7Oq_ukwuT_eBS97MdoWS5o2fMdQxWzpqeD3VacL9q3dXplFJHwGgNeZColnZpQ5BY9-TOBiSc66jr1ae5dR3ccf_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0930038d1c.mp4?token=O2H1dRKW5DZ9kqIlx4Um2jq-prSc_uSdLVd_PVlltpqnAGaeD_kqb8EN8wUdngoHBvZMDb7XzfQMTpvnvpiRfbmh9LPiOY83oDqX2Atdyh_8EWVZDgvsB8rGAdr_awIo0qB6K2wZ-Np7o02o9wOUlTSkFM8uUDaK2QN2kY8e0OoonGkwqLiQ4CWYmfNcn15cgsoubQs_BOa6OB0exeiM5tqJfgv-yNLIV0qhYW-yNSfiQywRSNKbvRXSjnvax7Oq_ukwuT_eBS97MdoWS5o2fMdQxWzpqeD3VacL9q3dXplFJHwGgNeZColnZpQ5BY9-TOBiSc66jr1ae5dR3ccf_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امانی: پس‌از ۷ اکتبر مشخص شد اسرائیل موبایل‌ها را ردیابی می‌کند؛ برای همین حزب‌الله به‌سمت استفاده از پیجر رفت
🔹
بعضی پیجرها از قبل وارد شده بود اما حدود ۵ هزار پیجر جدید هم وارد شد که در مسیر واردات، مقدار کمی مواد منفجره وارد باتری پیجرها شد.
🔹
واردات…</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/467940" target="_blank">📅 15:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467939">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68241bb1fa.mp4?token=uTknrRcwKZPNu3x-tG7J4Y4qxSn3RyN_qOj3dKPmitvapG0W79E3cWFAi89lk6KvfjJr3xbB1hOoHkK0_j2QM9PGTkMJApTuZETG-AuGWBEuc9qzhCONKT20S2H6zXqU-D6youUBp1XNzj_WVHQ66dZaRhe17NZCLUVwNsDm8hOaW6RwehAnkS4zHzMLrimoL3EUZMi1G5hjdP1VrbIK37L4lnxv-O9t3kQwt5s9knZRMMX1kjTvqtYmzw9ztbtnzxmDh9auVSoZN1YovBSV3ns4fasOXGaoD_q1xi2udMq32XrMkIrg1Z4AYcgNolfFQF_Y6vZnlxBVULrC2F2J3TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68241bb1fa.mp4?token=uTknrRcwKZPNu3x-tG7J4Y4qxSn3RyN_qOj3dKPmitvapG0W79E3cWFAi89lk6KvfjJr3xbB1hOoHkK0_j2QM9PGTkMJApTuZETG-AuGWBEuc9qzhCONKT20S2H6zXqU-D6youUBp1XNzj_WVHQ66dZaRhe17NZCLUVwNsDm8hOaW6RwehAnkS4zHzMLrimoL3EUZMi1G5hjdP1VrbIK37L4lnxv-O9t3kQwt5s9knZRMMX1kjTvqtYmzw9ztbtnzxmDh9auVSoZN1YovBSV3ns4fasOXGaoD_q1xi2udMq32XrMkIrg1Z4AYcgNolfFQF_Y6vZnlxBVULrC2F2J3TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امانی: شهید نصرالله پس‌از شهادت شهید هنیه و شهید شکر تصمیم به پاسخ گرفت
🔹
سفیر پیشین ایران در بیروت: همزمان با پاسخ حزب‌الله به شهادت شهید شکر و شهید هنیه علیه من شایعاتی مطرح کردند که «سفیر ایران به اسرائیل فرار کرده». @Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/467939" target="_blank">📅 14:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467938">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2ab366dbb.mp4?token=dufVRJIeeUVYXoFHAJPYdcIA5MYWIePZRK3daRLAZQOYzbrKQusDyJY24BA4Z0jkgWLEMhH_Ogjz02y9hzvgYHpyR9pnx9RK1UigTUu9wJtMWq1YO_OaipPJAsSpD-w1DuqphXIlu47Sodj8osUZgPuMUE-NpZs7deex0pPAjkuKzD0pO81yr8hbwLGajn36i9y4zYLW2HoXQIxmBeUssly96lldfy7qTN3r52FuulZHA7YOn39p35xXWV9r2EC_u80QRqpBernrqIMNbJkQTkpdVfXuxp0S-srX-zmWYJupTs7C_-iTHN2ThiynUQAd9jIvxyYT3t1loeEvu-URZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2ab366dbb.mp4?token=dufVRJIeeUVYXoFHAJPYdcIA5MYWIePZRK3daRLAZQOYzbrKQusDyJY24BA4Z0jkgWLEMhH_Ogjz02y9hzvgYHpyR9pnx9RK1UigTUu9wJtMWq1YO_OaipPJAsSpD-w1DuqphXIlu47Sodj8osUZgPuMUE-NpZs7deex0pPAjkuKzD0pO81yr8hbwLGajn36i9y4zYLW2HoXQIxmBeUssly96lldfy7qTN3r52FuulZHA7YOn39p35xXWV9r2EC_u80QRqpBernrqIMNbJkQTkpdVfXuxp0S-srX-zmWYJupTs7C_-iTHN2ThiynUQAd9jIvxyYT3t1loeEvu-URZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  وزیر پیشنهادی دفاع: تقویت پدافند هوایی را با جدیت دنبال می‌کنیم
🔹
مهرداد اخلاقی در نشست ویژه مجلس: اولویت‌هایم برای اداره وزارت دفاع در برنامه پیشنهادی ۱۶ مورد است که یکی از آنها باز معماری و بازآفرینی وزارت دفاع آینده است.
🔹
باید تلاش کنیم که از داشته‌ها…</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/467938" target="_blank">📅 14:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467937">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28da4e7be1.mp4?token=q1ArhblwEUK2-saPTZANv6iQc1I0xLDeNN8Z47mwL7zFig5g2nInCJa5V1zAphbImZoK5VLfDn2lZ5K1YWf8XaZR49UFlUEkV5Fvi3XqxvvI_XuY4UuN1BRT9EAHuve_hjF7X7uqv-gE_s3q0EOV22gRl6Rt8gLvagunfu39UUyYjjY2Y3OcsbpCRxcrBwjROaPBagQojB0yH83ycIXVLeCQBQIDGtoOobUusChBGTEfe4-tULWdUitHaRy0Qd8Uw8adM3x6NjJNwM9w2COMihqolds-L5syuWriMrf1kcwuxJXxlo5O3X3lCknJ8AK0MqWjGtE273N40B7Amjxl8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28da4e7be1.mp4?token=q1ArhblwEUK2-saPTZANv6iQc1I0xLDeNN8Z47mwL7zFig5g2nInCJa5V1zAphbImZoK5VLfDn2lZ5K1YWf8XaZR49UFlUEkV5Fvi3XqxvvI_XuY4UuN1BRT9EAHuve_hjF7X7uqv-gE_s3q0EOV22gRl6Rt8gLvagunfu39UUyYjjY2Y3OcsbpCRxcrBwjROaPBagQojB0yH83ycIXVLeCQBQIDGtoOobUusChBGTEfe4-tULWdUitHaRy0Qd8Uw8adM3x6NjJNwM9w2COMihqolds-L5syuWriMrf1kcwuxJXxlo5O3X3lCknJ8AK0MqWjGtE273N40B7Amjxl8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفیر پیشین ایران در بیروت: حادثهٔ منجر به شهادت شهید رئیسی و شهید امیرعبداللهیان مشکوک بود
🔹
اسرائیل از فروردین ۱۴۰۳ شروع به گسترش جنگ کرد و به‌سراغ مهره‌های کلیدی رفت که شهادت شهید امیرعبداللهیان و شهید رئیسی هم همان زمان اتفاق افتاد.
🔹
شهید نصرالله دربارهٔ…</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/467937" target="_blank">📅 14:41 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
