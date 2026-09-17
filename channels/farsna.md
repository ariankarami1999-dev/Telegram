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
<img src="https://cdn4.telesco.pe/file/O3qqrC_VM5RdPJcUjat4xUugGxfuysmQvU1ou6z5q1gHTt_1Y5B8vGHxlxocbX05x7GXzNNlcOk9oU-64XOe2ebxHeaSscWf03NmPrujQWo7UuMbraMDhOSlWlg6EhKyiZT7Wct-9UK1Z05Sj6zlqWCN5F4X-jQQAdo9lFqcLH18mKrfIFAep6bhJfiAmCXprVMd1dnLIgBLqczxYc8b_t18W3QlkUpaHS7FqmRDrqgJop__ywuWgytNogpcSCBSwdqt99a-uBTU1eo5YagceRxGUg5V-5Dl0T1U5h9ea_9oDhOxdC6obm71T4AnKwaWPpVK4stsm2GrA2mPB0Mfzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 13:03:18</div>
<hr>

<div class="tg-post" id="msg-462626">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSHM4FvYi2Fo0hykC3z1zYpI2djdR5ROK3dVgeiBjBsHKHJYMqzBRjZY-6RFA68UKPVltInPlW4ww_ze3KLP9S-PfWCt575d7jfcDlvj0K7Z43JMDAqpU6GBm0vL-M5a4gbpgi5AbJdLdJQVaIw3sv6tmaCdgdjiu_mUNySdXD1O0VK9gGpQ5c7nFD4UkMmjOWHLKuAdi9N8UpZBUaFxbpuNDd3BhOVpUPIt9DPMQ5_uckxytTc8jSrMyl-RvLNSQdLGJdIM17v7IwVuV0rgq3JuRvcLr5NKAjHFJzICD9X16THerB2UawcKzURhyfHb_uwAcnfTmx_skk8uUYkSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال نتیجۀ شکایت پرسپولیس را می‌داند
🔹
با وجود اضافه‌شدن شکایت‌ باشگاه‌های پرسپولیس و آلومینیوم به دلیل استفاده از یاسر آسانی، باشگاه استقلال همچنان قویاً معتقد است که این پرونده سرانجامی برای شاکیان نخواهد داشت.
🔹
طبق پیگیری‌ها از منابع مطلع، باشگاه استقلال…</div>
<div class="tg-footer">👁️ 623 · <a href="https://t.me/farsna/462626" target="_blank">📅 13:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462625">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd00601681.mp4?token=BMqw7sgHJTztuHBP7pas-iSHRup87dZQkKyi5uaLRgCsJMhEBYJFKGlBEtArtGZZPxd_C-Dz1IW2pkIYyMG4g-1kbPefBVb2gqS69YakGCQ3uQpmhLRdvutZdicBiCftNmfR5qX4OE6MQE61UeQHnBXtlSEck3WcOFTN_Ueq8CL9U__hPNgbwSKsIJZGIcFGWEfLehJC1geeGis_ZUEnfTBdQc9DJDcWGNKpzw4XX5kwfouxyxE6Av7foKoEyvTRbG9E_4Ol-ZqGzssVf67fwZEjbAW9GanywzcNk0JMG_hQWR8vGNOT9XtY0ePfG9Iy50B14U88LbFkMb4x0dZZfYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd00601681.mp4?token=BMqw7sgHJTztuHBP7pas-iSHRup87dZQkKyi5uaLRgCsJMhEBYJFKGlBEtArtGZZPxd_C-Dz1IW2pkIYyMG4g-1kbPefBVb2gqS69YakGCQ3uQpmhLRdvutZdicBiCftNmfR5qX4OE6MQE61UeQHnBXtlSEck3WcOFTN_Ueq8CL9U__hPNgbwSKsIJZGIcFGWEfLehJC1geeGis_ZUEnfTBdQc9DJDcWGNKpzw4XX5kwfouxyxE6Av7foKoEyvTRbG9E_4Ol-ZqGzssVf67fwZEjbAW9GanywzcNk0JMG_hQWR8vGNOT9XtY0ePfG9Iy50B14U88LbFkMb4x0dZZfYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور احتمالی فرانسه: ترامپ تصور قدرت ایران را نمی‌کرد
🔹
رهبر حزب «اجتماع ملی» فرانسه و بخت ریاست‌جمهوری این کشور مارین لوپن: بهتر است ایالات متحده را متقاعد کنیم که به جنگ با کشوری با تمدنی کهن نرود؛ کشوری که بسیار قدرتمندتر از آن چیزی است که دونالد ترامپ تصور می‌کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/farsna/462625" target="_blank">📅 13:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462624">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDZLYsz0IDVsRtPc0XCZwX_oOTR-9sRNCFP5qkwQnNSS95Nq-uUH0-Yo201UjBRt2EEw7PgYl274mrTemQbAy4I4sCStc-WLau9lnIpcUpt3KFFCTdSIq1CBB_Z5dNs1gt-6_PCi_QcIRC1539C1Q7pE9FxIRqHi0HXUS5ILrDGKvCe6a-oxFRYDgoIdFPaA-KNLrPkPfCMR82_LdCdhaYQQi_bhHhpf2DPQ9YEV4Gl8PVHhsPqvEB_nOH0RGPSahQJuVz7p7KdYKWwW0e1X98t1iQ7d_s-LVRqhE1pXxW5qi4iSe7xysXDAjcuhr0etDFsOjN9tmjTnF4f6udP2fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ کانادا را به آغوش اروپا فرستاد
🔹
کانادا درپی تشدید تنش‌ها با دولت ترامپ، درحال نزدیک‌شدن بیشتر به اروپا و آسیاست؛ روندی که با استقبال اروپا همراه شده و حتی پیشنهاد تبدیل اتاوا به نخستین «عضو وابسته» اتحادیه اروپا را به دنبال داشته است.
🔹
جنگ تعرفه‌ای، تهدیدهای ترامپ دربارۀ گرینلند و کانادا و نگرانی درباره اتکاپذیری تضمین‌های نظامی واشنگتن، متحدان سنتی آمریکا را به بازنگری در روابط خود و کاهش وابستگی به این کشور سوق داده است.
🖼
فکر می‌کنید فاصله‌گرفتن متحدان آمریکا چه پیامدهایی برای نفوذ جهانی واشنگتن خواهد داشت؟
🔗
پاسخ را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/462624" target="_blank">📅 12:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462623">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AG0ZBGJPYdycRBqv2Zzzn9cTh8l3wuBf3EeQsbWzVAAt-mcKn5HE8U3EGR0alxabqmGyHZiTevDFCnF7KkDpLFvvNWZk376Fc9ymt7wYipfgWp_1jpY6lv0XikhX8CIL5VkE_2mPq8zTGeMwsgD2ysQLIZJISux2hnfh-Xb43uUsFMU7jidpEpwYjBWJDUJ2aQNbwkUaaH_IhHatRTTJm7gnJD6NTITHqQ8qZB3a5eCnwVy1Y6zSb_9XGrXsFLvVFFUOZ7wTi6sgvm3XLC6JzC1-x3hfV4_51abheHLKRnXPg_Mc0oHdHVaIoe1IPkk17PytImFz2bCmnmFrlfNaCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهش تازه: زمین دیگر شکل سابقش را ندارد!
🔹
ساینس آلرت: پژوهش جدید نشان می‌دهد بخش سنگی زمین طی دو دهه اخیر در حال تغییر شکل است؛ مناطق قطبی با سرعت بیشتری بالا آمده‌اند و هم‌زمان اطراف خط استوا بیشتر فرونشست کرده است.
🔹
بررسی داده‌های ماهواره‌ای نشان می‌دهد سرعت بالا آمدن مناطق قطبی از حدود ۰.۵ میلی‌متر در سال به نزدیک ۱ میلی‌متر رسیده است.
🔹
ذوب یخ‌های قطبی باعث سبک‌شدن پوسته و بالا آمدن زمین در این مناطق می‌شود، درحالی‌که انتقال آب حاصل از ذوب یخ‌ها به اقیانوس‌ها، توزیع جرم روی زمین را تغییر می‌دهد.
🔹
دانشمندان می‌گویند برای درک دقیق تغییرات زمین باید هم‌زمان تغییرات سطح جامد و جابه‌جایی آب و جرم را بررسی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/farsna/462623" target="_blank">📅 12:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEcpX1QC5A2tONux8L4s85H2xZ7lKgMZvJGbRbjRCcMkR7Ot52D44pSiDZ-JYu-FRY5yUTzrr1tM4gchPVLNGigSZDGGfM8BHR-Y8bZy5DXeUbmyTRXiz3D94R7oRvVg5OQUmTjtT20KPMse-GSzxeYUBfg4h-jB4L6Msak-zmtOEHP3J5ZxZrCYiaTOlMN-PqgmJSoyeyFusGKD06GMEcLnlig6edLF2C8OG44TCOP9n51mWbohapZecvNCFJHG4rBKGul0XqtEQOTqVqdzP_h3TdDtNmW4FOXXFFbbtlLJjGDrXvJRLeLkrJSl6GcvT9OAaZ9mZ18tj4meBtPxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان غذا و دارو: واکسن آنفلوآنزا هنوز توزیع نشده؛ واکسن چمدانی نخرید!
🔹
سازمان غذا و دارو اعلام کرد: واکسن‌های استاندارد آنفلوآنزا از مهرماه وارد کشور و توزیع می‌شود؛ با این حال، در حال حاضر برخی دلالان اقدام به توزیع واکسن‌های چمدانی در میان مردم می‌کنند…</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/farsna/462622" target="_blank">📅 12:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462621">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36a94145e0.mp4?token=t1pQMR1LYxP_FGGfylbsqB1NXGGc_2hxd1zohJff1vd6sbMPcDO7Th1ei7ugvERaZ2YJNUo1uyl1uBqLXqePo62-eL74D9aj2QMRb_BMBli7gkQAK-hQMp_s7Q0ByL_aYOj1WzQfArMFBOYpkZ2v1BwRBgO9GXTBw2UC4mXlADLVQOR7BcVNXNtaxFr_Kr9Q0rd0dzVAcdi9bZ_oQRWEap1kMjU3J8GHnYv_voKQtmW-ACDNq9v3vIZg6ZmQtK8Mz0p0DQC3szL6em1Ok_Hm8X8JEcMwLQsdj1KKvwKOa0Q_-4s1q_Ru0JC0zv-rXsCRD-WIgQ_CL6_7o0wxQJ9AQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36a94145e0.mp4?token=t1pQMR1LYxP_FGGfylbsqB1NXGGc_2hxd1zohJff1vd6sbMPcDO7Th1ei7ugvERaZ2YJNUo1uyl1uBqLXqePo62-eL74D9aj2QMRb_BMBli7gkQAK-hQMp_s7Q0ByL_aYOj1WzQfArMFBOYpkZ2v1BwRBgO9GXTBw2UC4mXlADLVQOR7BcVNXNtaxFr_Kr9Q0rd0dzVAcdi9bZ_oQRWEap1kMjU3J8GHnYv_voKQtmW-ACDNq9v3vIZg6ZmQtK8Mz0p0DQC3szL6em1Ok_Hm8X8JEcMwLQsdj1KKvwKOa0Q_-4s1q_Ru0JC0zv-rXsCRD-WIgQ_CL6_7o0wxQJ9AQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پلیس فتا: در سایت‌های خریدوفروش آنلاین پیش از دیدن کالا، بیعانه نپردازید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/462621" target="_blank">📅 11:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462620">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDW3aIT-tGEifgrL0125B-MN0hsaEcsQUrTl1GNcg4A-gjwag6ThP4YzpIJ_bfQlwTFWOwCOWGGpGRA0Cy8kEaHLefwh7kSBxLuafnMdIdVq_gIpfGIE3S5GJ0b2DTbABDlJ6Te9zh8fZDRyn4cxCnJHm_otn-jOXIg_6bbnlngv8zHCkkGLNM4j52sc0qqgbELySqP0B3Fq7llFaQzsHzdyULGdmWY9AdHByY8Of93965swIeXEhD5EyjX2X4fnhLpf6x26nbDT7ddMXRScApGTpcWMRe_5PKiwHMsdUJn3hdHS0ZThct-pB4ZUcjlcftnQqgx4w-VO6XB7ltfl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خصوصی‌سازی: ثبت‌نام سهام عدالت نداریم
🔹
سازمان خصوصی‌سازی: در حال حاضر هیچ برنامه‌ای برای واگذاری سهام عدالت به جاماندگان یا افرادی که قبلاً به هر دلیل از سهام عدالت برخوردار نشده‌اند، وجود ندارد.
🔸
در روزهای گذشته تبلیغات و پیامک‌های جعلی با موضوع ثبت‌نام…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/462620" target="_blank">📅 11:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">دعوت از ۱۸ بازیکن لیگ به تیم ملی
🔹
حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی‌عیدی، امید نورافکن، مهدی لیموچی، مهدی محبی و امیرحسین محمودی
🔹
اسامی بازیکنان حاضر در لیگ‌های خارجی هم متعاقباً اعلام خواهد شد و بازیکنان حاضر در تیم امید هم در فیفادی بعدی دعوت خواهند شد.
@Sportfars</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/462619" target="_blank">📅 11:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462618">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDVmDejc_NtnO_xpVDRXfdAhC9Zwp3W3CDIjriaouN9Uf8PaGTJbFxbq0k-bK_5bS5NAWZ7tkSkji9xw0Pmj33GiCY_A-8-ee4z6GcexeIwDCfdgy0Lhs_3n7Kbfc5JJnkcjA8cWx7nJs_HFUhkvFem8m3zUBQXjWDBmYMTyusJ2xKF9dnu05oyqM-DNGOoA_YZ96dzt4yc3KV9G3OxGsw-SCJC0y0IX1LHFtd9cpL167Rn2_9is8dkbiumgUNYut_eBH_TgQGzrA9hAbJtpJWXgxkX9EbzWbP5hGAUTgV7vnhH1CiAVposQ_AgfE7KQffAOPiywV0AMx7yXa_CqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا آیت‌الله سید مجتبی خامنه‌ای کلاس درس‌شان را تعطیل کردند؟
🔹
حجت‌الاسلام محمدجواد قاسمی: آیت‌الله سید مجتبی حسینی خامنه‌ای در سال ۱۴۰۳، در نخستین روز سال تحصیلی، تعطیلی جلسات درس خود را اعلام کردند؛ درست زمانی‌که جمعیت کلاس‌ درس‌شان به بیش از هزار نفر رسیده…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/462618" target="_blank">📅 11:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462616">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc48f9072.mp4?token=heKHOGyKe_cQDSImSEjLlkPvUz9UFUTrqeaC_6gWi8__y1X-5ZNIhNmf6vY97cVUHANEQoRx4Te0bOpuaEr84KUnBkLh2ljfJ0HT_JNrfFxWLhvW2u7xCRuKLChXpJ6u5gm_zLecct6k2aRAWF3ok0Wso0LfovlGV8DZVtdWqGwsST1QXaSpVkk5C_raOMOBDcaFBkJsD_zy_wiYV1ncV2Vq1q98bTBCqXbCGcltWgNM1ptjxtRAvV54P3IGiSP7lJmwrORovWiPONlchwEta6zUWyDPXhA7IBNjq6tbERHQogrquV_3gwenvauK6KktArBPcpA6zQnIbHb4PLg4A1fjq6nZ9XsVE14uiufJVWMiIBpCSjoGd6loN3rSknoOHW3FP82bpvoZu0O7uVJmnCS_8GHkUuZ5wtip_B9EWFhmg2bUnxxRxvC_uzGmY7h6XrPRoXFq4a4NK-i2n0ep01l7ebh1ygWuLO0Wm6zQI6MHAoc6ihWKNdFJFPJ-ZM7ulN42lNOqpoah4J7zXOlkvAOOAfO8ieD25KPyZ6TcT6wzL2IFvv_a-wTBKuWIr6gxPl99SBgpWhHmcfqXTuybBGJBAdbWykv904lvhAGQfHe2V749IbPisqiHImuJfN6pCqY2J3nZzwbOBJUA1LNZ_q0P7zyvLbUUxobl-TRQuK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc48f9072.mp4?token=heKHOGyKe_cQDSImSEjLlkPvUz9UFUTrqeaC_6gWi8__y1X-5ZNIhNmf6vY97cVUHANEQoRx4Te0bOpuaEr84KUnBkLh2ljfJ0HT_JNrfFxWLhvW2u7xCRuKLChXpJ6u5gm_zLecct6k2aRAWF3ok0Wso0LfovlGV8DZVtdWqGwsST1QXaSpVkk5C_raOMOBDcaFBkJsD_zy_wiYV1ncV2Vq1q98bTBCqXbCGcltWgNM1ptjxtRAvV54P3IGiSP7lJmwrORovWiPONlchwEta6zUWyDPXhA7IBNjq6tbERHQogrquV_3gwenvauK6KktArBPcpA6zQnIbHb4PLg4A1fjq6nZ9XsVE14uiufJVWMiIBpCSjoGd6loN3rSknoOHW3FP82bpvoZu0O7uVJmnCS_8GHkUuZ5wtip_B9EWFhmg2bUnxxRxvC_uzGmY7h6XrPRoXFq4a4NK-i2n0ep01l7ebh1ygWuLO0Wm6zQI6MHAoc6ihWKNdFJFPJ-ZM7ulN42lNOqpoah4J7zXOlkvAOOAfO8ieD25KPyZ6TcT6wzL2IFvv_a-wTBKuWIr6gxPl99SBgpWhHmcfqXTuybBGJBAdbWykv904lvhAGQfHe2V749IbPisqiHImuJfN6pCqY2J3nZzwbOBJUA1LNZ_q0P7zyvLbUUxobl-TRQuK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ۲۰۰ شب حضور خود در خیابان را معنا کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/462616" target="_blank">📅 11:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462615">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎥
پیکر شهید مولوی گرگیچ در زاهدان تشییع شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/462615" target="_blank">📅 10:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462614">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMXc9I-leZ5W-X3W7nZC3-NJ-eRxmJMHfD816O3Yev4gB01W1mSW-Lm6eaPejL0zG2IHGo2QyCnFVStPyIDIUYBaNdRb56jkUq4xdWmfyzxVK-4AM2slDTezU76wW5PUGbd2Io5AO2zx_cb9SS64uv1Tk12eSZcowGJaB904cM0plFq2CFTl12Qjzyo6rGitwfCAfLpppIOufu3OwgHhBmOX5Er0E49MgzAq0-B-SsZ-yXXqPCaruiLUSB87NgcYhEBEZp7WenRP7g8-H0LAqkxED6s4Gb99lt6_fe52CpUqddC4vzukC7Fcv_CCyIAnXoHt-e_dXS1HyRi-9mehFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: حرف‌های ترامپ حتی در معیارهای جنگل هم پذیرفته نیست
🔹
این حرف‌هایی که با افتخار بگویند یک کشور متمدن را به عصر حجر برمی‌گردانیم، حتی در شاخص‌ها و معیارهای جنگل هم پذیرفته نیست؛ چراکه به هر حال حیوانات جنگل هم حرصشان حد یقف دارد.
🔹
نفت کشورها را می‌برند،…</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/462614" target="_blank">📅 10:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462613">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La6MRxMm6Z1irzNjxOvroSnowblRng50cTYsSmkSkSS5LsDW9oNvMj4lvgmhh-0GQRwqy0mG3O5pZiudoByvfWVmGPs2YTiAYPU4EGZQGQ5-YXO5dOS0IIVyjhZfoZjcOiUXtAxzzfNBYri4UR-t-jKd2K2378pokYjnNYBeeSVDOWh1zwZBtV4AJhiY1RDFAAvTX3cM7-aE4sIuYKrL-AJU22B2o6X3MhGWqQrZ4aU8D2H-ZyixbQoQmJRNQX0vS3YPil-YyBGADH2cilz9bkApKVxZ2BKs2X1GM4un0GtOd2wCYNNhWSKJ1C6Dwn7FiSr5hT26VsSuRvniv3ASKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادی که جایگاه و نسبت‌ها را کنار گذاشته بود
🔹
حجت‌الاسلام محمدجواد قاسمی، از شاگردان آیت‌الله سید مجتبی حسینی خامنه‌ای: رهبر انقلاب در سال‌های تدریس در قم، بدون جایگاه و امکانات ویژه و مانند دیگر طلبه‌ها رفت‌وآمد می‌کردند.
🔹
جلسات درس ایشان نیز بدون اطلاع‌رسانی…</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/462613" target="_blank">📅 10:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462612">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVDB6Vnm-MRB0B5p8k3ZEXIRinR4mQy0OjibthEu6xI_M098J1zps4Wdc2E6gqbVx8kioPZfNSbWsgum5i9C3skin3uJHRSyTeRpfMoVwLnIW9LLSYHoopvpbIjjSvXUmNKohTZ1RT9II4FL7lnnUXRi8HIvu-wzYlEUNpM4s5i1lhqcKqZ--1VVh8HSyBxrpweXLj4YMx3U8t2uAFCpKqBuU6fU-TTpiEZ1SOL_wlmJqPj9Z1XQ-Dvjc7KaIiKuCSbwN4FZoOYf23PzrxxRLi7Kv2K6tDh0zMoGwXedQ7RQAdoTNJELknZa_kn8iYiPw2XW4LNbDGVTHtgqJCNMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: حرف‌های ترامپ حتی در معیارهای جنگل هم پذیرفته نیست
🔹
این حرف‌هایی که با افتخار بگویند یک کشور متمدن را به عصر حجر برمی‌گردانیم، حتی در شاخص‌ها و معیارهای جنگل هم پذیرفته نیست؛ چراکه به هر حال حیوانات جنگل هم حرصشان حد یقف دارد.
🔹
نفت کشورها را می‌برند، رئیس‌جمهور یک کشور را می‌دزدند و زندانی می‌کنند، ۷۰-۸۰ هزار نفر مردم بی‌گناه را در یک منطقه مانند غزه به شهادت می‌رسانند اما هیچ اتفاقی نمی‌افتد و باز شعار تمدن و حقوق بشر می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/462612" target="_blank">📅 10:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462611">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🇮🇷
پرچم ایران در دهکده بازی‌های آسیایی به اهتزاز درآمد
🗓
بیستمین دوره بازی‌های آسیایی ناگویا از شنبه ۲۸ شهریور آغاز می‌شود و تا ۱۲ مهر ادامه خواهد داشت.
@Sportfars</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/462611" target="_blank">📅 10:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462610">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1zpPgRMIf9VpP1WjNBQGBzxGtM8ZRkbMnPDAJL9EaH5wUiHhgNKUqirFu14EQ9548T4c6nXSF60sY7gyAziCFyxRR6yq1vVPYRAwXmuaAi7CPQ9ClfX6a2IRfgkSgKD9U9L6o0IOF8UNR3wbyTB4x7TkQ-Hkkfs8B8vkFSrP5GL87CGNEmgT3JyQZJOwK6auvnT-qjHlLTX_cmo6nY_UMNRqzZFeaNhBDJDRvYNQyYamOIWwwWSX6uWOM4ggnmtf0SpUeOw_q8WABOukXCOVgMkMWxN12PdWMhKt0uPf0ROM_6LR3PsZvjyIHfOZ497k4OdrwoZdNkSHbFn5KiuvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادی که جایگاه و نسبت‌ها را کنار گذاشته بود
🔹
حجت‌الاسلام محمدجواد قاسمی، از شاگردان آیت‌الله سید مجتبی حسینی خامنه‌ای: رهبر انقلاب در سال‌های تدریس در قم، بدون جایگاه و امکانات ویژه و مانند دیگر طلبه‌ها رفت‌وآمد می‌کردند.
🔹
جلسات درس ایشان نیز بدون اطلاع‌رسانی عمومی برگزار می‌شد و طلبه‌ها برنامه کلاس را دهان‌به‌دهان به یکدیگر منتقل می‌کردند؛ به‌طوری‌که جلسه‌ای که با حدود ۲۰ تا ۳۰ طلبه آغاز شده بود، چند سال بعد به جمعیتی حدود ۴۰۰ نفر رسید.
🔹
یکی از ویژگی‌های برجسته ایشان، بی‌اعتنایی به نسبت‌های خانوادگی و استاد و شاگردی بود. در جامعه می‌بینیم بعضی‌ها به‌طور کلی موجودیت‌شان با همین نسبت‌ها تعریف می‌شود؛ من مثلاً بچه فلانی هستم. من برادر فلانی هستم. من شاگرد فلانی هستم و... اما در شخصیت حضرت آقا اصلاً چنین موضوعی بروز و ظهور نداشت.
🔹
اجازه بدهید یک مثال برایتان بزنم. خب حضرت آقا، غیر از اینکه پسر امام شهید بودند، شاگرد آیت‌الله وحید خراسانی هم بودند و سالیان متمادی در جلسات درس ایشان شرکت می‌کردند. اما هیچ‌وقت شاگرد رسمی آیت‌الله مکارم شیرازی نبودند. با این حال، خوب یادم است که در جلسه درس اصول، به کتابی که آیت‌الله مکارم در اصول دارند به نام « انوار الأصول» استناد و از عظمت علمی آیت‌الله مکارم تجلیل می‌کردند.
🔹
آفتی که ممکن است در روحانیت شکل بگیرد، این است که بعضی‌ها ممکن است دچار توهماتی بشوند. مثلاً اینکه چون من پسر فلانی هستم ،دیگر از فلانی یاد نمی‌کنم. چون من شاگرد فلانی هستم، دیگر از بقیه اساتید یاد نمی‌کنم. اما این مسائل اصلا در حضرت آقا وجود نداشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/462610" target="_blank">📅 09:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462609">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
شما این مدال را گردن چه کسی می‌اندازید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/462609" target="_blank">📅 09:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462608">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGSWDscDuv8ZS9-Xa2qJiGbRvP2tysv5V_PlybjtB1PTF_hoor40VUd0vO9lkB8h0ocBFs9FiRChYHyh85NQzagQcLmaLy7Yiq4q88sPnUOfdQv6D8n7GaC6t7vV5IWaUNTvdpqF6w5yZDF4Kawuj87DmAfs_UUQWNfoKXTyDsPBO3SswmZ0vtdJ14ulmV-T8p0UQ2Qps1bgyezMmNz-6lgKJmQEQd4cV270P9tprCELh1bOkqpyzF0gBTIHr3bBUvvnhEgS-6zvQxqqBmIUP05aSx-xvUcWjZOA90Iv0lvIHPRQ1Y8S-u1OfXLdlnU77RJjC3ls4DZGhe5gG-M4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/462608" target="_blank">📅 09:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462606">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_36Pz3Hxnm9IZnjclWdDmgbuEG1vm0-ih6NRvC02evFqqntkDL3XfiM718mOr17r8JC1ZjsDvZx-UuQZ8ClA7jMNQhskk9kWV9fZrSbByeEHkTPLVqZMyvdZJru9t5HgDVZEG2DdACMbjnSr3GLbixYXZsXL5xX9tINZaKG5go-BopWT485-9Sgu3vd0ZbC8emL3KksMarc0itd6js4TkwVMJU1Pyu0IDaSDOGJ0inw31kc2gUdgA-rBuMCvYM_REem3rtKnQBOWRAr7Ft_IUkXD95PzoiuaTTaWpYsbpyyCKvGcgIoV8e-gWE8HRzOA6ZlKfqN1EnYD5ymvl38fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسبی سلبریتی‌ها همچنان روی موج زن، زندگی، آزادی!
🔹
همزمان با فرارسیدن سالگرد فتنۀ زن، زندگی، آزادی، بار دیگر کنش‌های گتره‌ای سلبریتی‌ها بروز پیدا کرده و افرادی چون تهمینه میلانی، دیبا زاهدی، بهرنگ علوی و زینب موسوی با انتشار مطالبی در صفحات شخصی خود، به استقبال آن رفته‌اند.
🔹
این طیف از سلبریتی‌ها که بزنگاه‌های خطیری از جنس جنگ تحمیلی ۱۲روزه، جنگ تحمیلی رمضان و شهادت مظلومانۀ کودکان میناب در حملۀ دشمن آمریکایی-صهیونی به خاک کشورمان را مجال مناسبی برای سکوت، انفعال و یا موضع‌گیری‌های وسط‌بازانه یافته بودند، حالا به شکلی صریح و بارز روی موج رسانه‌های بیگانه سوار شده و به تریبونی برای نشخوار مهملات آنها در باب فتنۀ «زن، زندگی، آزادی» تبدیل شده‌اند.
🔹
واضح است که امروز و پس از آنچه در جریان جنگ‌های تحمیلی اخیر به ایران و ملت مقاوم آن گذشته، دیگر حرف زدن از «زن، زندگی، آزادی» صرفا کنشی احساسی و هیجانی محسوب نمی‌شود؛ بلکه به منزلۀ همراهی مشهود با ادبیات سیاسی بدخواهان این مرز و بوم و تبدیل شدن به قطعه‌ای از پازل پیچیدۀ دشمنی‌های آنها با ملت ایران است.
🔗
اما علت کنشگری‌های کاسبکارانه و همدردی‌های نمایشی برخی سلبریتی‌ها چیست؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/462606" target="_blank">📅 09:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462605">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8OBxM_pszRR4pU0CSfc0LTYCT_-Zu09T0tFNHbFftfR51jW9bnbf4q6SxVIzbhu11Fsc0czBd_Q0mobTD-oiVkBrdk2ZypmNx-C_guv4RZK8IxjiUn74djuKjgOucTsylGvH0x-Lxs5ECAQNhXnUZxfvkmUME1pX7PErBips7Sapcn2uGZhUrIW7LBXKFGRHGjWaRHLrqtFkrn_jXDv-137xLEhrl-aFvGLSOVoOUvrtJaj7Y4mdu7ndDsqMuZ-RU5v3s1G_C8Foe3tp0DdXsuShctbXwCxITlQwVdCsToHZOtk3bmpP5OMH8W2HjjE4FtGpVSgLxLz0NjmUQJK8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با سران کشورهای حاشیهٔ خلیج فارس دیدار می‌کند
🔹
آکسیوس به‌نقل از منابع مطلع مدعی شد رئیس‌جمهور آمریکا، قصد دارد سه‌شنبهٔ آینده در حاشیهٔ مجمع عمومی سازمان ملل با سران یا وزرای خارجهٔ عربستان، امارات، قطر، بحرین، کویت و عمان دیدار کند.
🔹
در این نشست دربارهٔ مرحلهٔ بعدی جنگ با ایران و راهبرد پس از جنگ گفت‌وگو خواهد شد.
🔹
همچنین نخست‌وزیر رژیم صهیونیستی، دنبال دیدار با ترامپ در نیویورک است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/462605" target="_blank">📅 09:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462604">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کرونا دوباره در ایران شایع شد
🔹
با افزایش موارد ابتلا به کووید-۱۹ در ایران، پزشکان و متخصصان ویروس‌شناسی بر رعایت بهداشت فردی، استفاده از ماسک در فضاهای بسته و پرتراکم و پرهیز از حضور غیرضروری در مکان‌های شلوغ تأکید دارند.
🔸
علائمی مانند بدن‌درد، سرفه، عطسه، آبریزش بینی، تهوع، مشکلات گوارشی و بی‌حالی در میان مراجعه‌کنندگان مراکز درمانی دیده می‌شود.
🔹
میرزایی، پزشک عمومی با اشاره به افزایش مراجعات، می‌گوید: شدت این ویروس در مقایسه با برخی سویه‌های قبلی کمتر است، اما بیماران ممکن است چند روز درگیر علائم آن باشند.
🔹
مرکز مدیریت بیماری‌های واگیر وزارت بهداشت اعلام کرده درصد تست‌های مثبت کووید-۱۹ نسبت به هفته قبل افزایش یافته و به ۱۱.۷ درصد رسیده است.
🔹
علی ملکی، رئیس آزمایشگاه مرجع کشوری کووید-۱۹ انستیتو پاستور ایران نیز می‌گوید: وضعیت فعلی نه به معنای پایان بیماری است و نه بازگشت به روزهای همه‌گیری؛ بلکه باید کووید-۱۹ را در مرحله مدیریت و مراقبت مستمر دنبال کرد.
چگونه خطر انتقال را ویروس کاهش دهیم؟
🔸
استفاده از ماسک در فضاهای بسته و پرتراکم
🔸
تهویه مناسب
🔸
رعایت بهداشت تنفسی
🔸
پرهیز از حضور غیرضروری در مکان‌های شلوغ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/462604" target="_blank">📅 08:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462603">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی با عاصم منیر و وزیر خارجهٔ ترکیه
🔹
عراقچی دیروز همزمان با حضورش در پکن، تلفنی با عاصم منیر، فرماندۀ ارتش پاکستان و وزیر خارجهٔ ترکیه، گفت‌وگو کرد.
🔹
در این تماس‌ها آخرین در مورد تحولات منطقه‌ای بحث و رایزنی شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/462603" target="_blank">📅 08:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462602">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKDJwWNdWo5LoDX5biODA2CQcUqmggkdeu8YMlArtp2rdNj1Ey2IbVJVgTal6LuMQ7NlrvprTujP3AYi3ARllkIIAOXr1_ISjSyNgD1RwBRtFDgOaoV-NDwVcLunUpfSTqm-vbnmjqpSjEay_NCi3GmMtdYNjWy27G3hrEGGlOF463GSIXT61AoMX_5jOav4zjNJunuyNNqnhNARHkYo3M5B2KvoJUnyajVoQQN0ploJiqo_BasIgskNkHzL2FbICxAhw8FAyo6I1l6bTEwQZi5xvLM-on4khlzDCcZdH_Jj_7fUjektEu6HVmmPAbYgnL24FUA9q_kJXShJrNxKNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرطی که شهید آیت‌الله خامنه‌ای برای دیدار با شهریار گذاشتند
🔹
محسن عسکری، از شعرا و مداحان نامی آذربایجان: در سفری که شهید آیت‌الله خامنه‌ای زمان ریاست‌جمهوری‌شان به تبریز داشتند، شب شعری برای شعرا و مداحان ترتیب دادند.
🔹
آقا شرط کرده بودند حتماً استاد شهریار هم باشد و ورود من به جلسه قبل از شهریار باشد.
🔹
آن‌شب، دقایقی بعد از تشریف‌فرمایی حضرت آقا، ورود استاد شهریار را اعلام کردند. زمانی که حضرت آقا متوجه شدند استاد شهریار به جلسه آمده‌اند، با نهایت بزرگواری بلند شدند و به سمت در رفتند و از شهریار استقبال کردند.
🔹
آن موقع متوجه شدیم که چرا حضرت آقا چنین شرطی کرده بودند؛ اینکه شهریار به پای ایشان بلند نشود، بلکه ایشان به استقبال شهریار برود.
🔹
عین جمله‌ای هم که در اولین برخورد، بعد از سلام و روبوسی با استاد داشتند، این بود که فرمودند از آرزوهای زندگی‌ام زیارت حضرتعالی بود که امشب الحمدلله موفق شدم.
🔹
بعد با نهایت احترام، استاد شهریار را بغل دست خودشان نشاندند و شعرخوانی آغاز شد.
🔗
در سالروز درگذشت استاد محمدحسین بهجت تبریزی ملقب به شهریار، خاطرات رهبر شهید انقلاب از وی را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/462602" target="_blank">📅 08:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462596">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZdFj2bUaqfYlhf0aR9SGJwkzy3bmzcV_VUhYEbc42_yyBI32Y_1-zyTBjC5751_SjjIlYlsj4T7weQVT4uSM-FwyhgkfCx_QshKQwU-aXUOQKS_SlKvIB6JPysPFBqUZ7yBX1kD8axzYLM7gYcO4yrIXxsQ7ErtJd4brFyGk8LYcY_8F0TSrSScIHVe8wxvA_u_4hvX1910Dbh60evqoP_hw2RTyALEd_I0DblB1cgFjp4XvVuOShNJbfpGtJ4cV44essfEONkX9HJgE5gSQtUOAlVJyA8TDZqpVXprwKbBw24qWcpiGkQ9yRU-cxX8Tc4tw2fACGnUvn2mddoNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAjC8gef6CkCCZYqZhpWEfI6J_WNgE1XPEPCYgrd2ERYGSGcl5bozJel7SJrR5iFPZq_dskeawU5UwOiNaMlhfkgXLChEYW8R_dFa7OlfHI66Xi-GEFgnzhLfXocEu-envWeHNVhsYJ0wsVZI2NvAoBhusRB1s3XPcvsiT2Xb5jOkWLmFnXqycWjVEqXnd1R5e_hrp7piaTXphEyAbfVG1sqDXf_eSN5yrEZ9SnG1cZCn71MC0YXTi4xNtSBoUIaO4AKW1qwiUSb8tuDvynHr5QBmlzLXIVTsNz6f0qCT6aNHhiZeCRK7ipFGgW1PNOrM9eHwe05QUQ8xr7klPrUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dICbHg7S0JgabYCONkGGBrKSOvhLZhXbRyHXwsR5yG-PIYBUi9B_zJ677-uWrU5Lf_qnKbvPSTOpcYWZG36qeeWkq0Iam5yTAsw-x1hUHtvwC6Zklk0L7Dz0WXCzCRoFFCZXifP1AHKzCb4byO52qZd-oK1NRydPODnqeDA_KdxSBF4noN0zwZ0cheDNcVJpOIwppN9qdF4IEjaCFG6nBNch42xK4NTeXdQe4o42dOUjpTupnuxznsFFf49_6aIusg-IrmK_xx4-jGL5qcvXykemH756HYdMeXLa70SRUtqVwoIDzd0Onz8Vl8c2mQTPgl-Zqhig07b0eDzK2SF_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WdHHvDO0hWVAyZacfUHYVojyEgiENfmclsuNFf1_JqUsG2ZjBZV8w2dP_lumirtC9cmoZ0BmjsMZrwCNyh-KbfHwTZnTeELufpo5hNaoOoOaeTfIoPhdnaYvY6Kg6RefgFytS7iuvcLDeEEfMd09T9LHN5J92Uw8wH6pWUE8CBDldIBUaOmToxyiJxGjJ8Y7Sbt7PLMg-T7883pSHoZk42j1tWHUV5ciza-RVXMqFq_204pUP2ZvfhLMTTFRjwGNNWEeSHDmC9xoHrF9TIbsb7ew8kX-ADqvH1GcBwqXythFhSll-NxzQIQv--VnC3lBCy3Bd7FwJgfReM58Zi2oag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9E260FIG8kJtRcJJozWRp_naj3TU20o-r089SQH1Y7lf_o0KeO9aW88fej1N5aKdzmuaB3vA2KeFmOUKYoQErqecg8T0NtkEPao4h1b1K-FsYBkLys9c8RwKLJVGjw-bFDkyrQDcMUEVtwEFKxRXOve124ZHfa6UG5b7OFmPpfLMkNohU1prPc2UI91NCfykFKRBLroEq3E98eSWydiPSrNyYvcY18jzJbOQICOIJyKQA3hquSFdh1UIxTLUtKCDHl7-BweLrLMiLbGbnQVEAXk0Hy7dCCzent74iG3owSK-MI4ZJlXsO6KbZv_AoIycI9yNPTvf7l5K5JSRJVGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KP4W_fhVS8EXmRAuqDehUsIpFninf_cTR94_-T8eqiivi6-zoWrK4HE_UUMmNAOvRogtVKeY96HyZRBtkOjuWR7_hKPUnG_qYVqJJr04NALekICNVc-jUoLGsBS-6QEju-qU3LymNrEwdNLpHQlXlyhXfwbIOmnFU199yo-nPOq4nToSgxYglmGz08qn0dlfNQ78IoPUTJz8uBe4qMDRTjNIYuk4dGbyMtbFGGN6SMQI3OCpnQUlyEcT_36y8gw4ZOugpIFVn8ZXgcJbmC55YJzQ1DXLHzAEBbpUu0QktaDoq0tkkdG2Rsm0zsRrQwLFuSlNtfr4WwgXXxrv-PR25g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
میزبانی دریای چالوس از مسافران در آخرین روزهای تابستان
عکس:
غلامرضا شمس‌ناتری
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/462596" target="_blank">📅 07:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462595">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هوای تهران امروز هم «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۶۵، و در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/462595" target="_blank">📅 07:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462594">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmvPYgqn3jW5wcd3IHmInEOr6kjH8xvykRl7RO0StCgjZPC88S-MwNC-016PH22rEXZmHuM8z3Rb7CkIAuWoVhUJo8jVdbfPh9JtBE4rF6EAJvnI5UCx9pvkUv08SAlaba3E1kgyMXMKNcYZ1gh2KVdlsjmsVWmQL07naY2TVu0mwVUHWt5ij9U1EKyojtJyHQJ5jOxjfSMxw4iyU5g5GIMK70NoC-NwMTYERmuA-DYN1gv6k4k-hrWPm7Wd0UidYmYV3GnSfRW5GCieWc-z1LgVdODlou_ipDpAH6eK9nmVb4JRucDnp6QgbOYZzlhOWVReQd0loFsTVEmvTaXsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موانع بزرگ قلی‌زاده برای پرسپولیسی‌شدن
🔹
در روزهای اخیر شایعاتی دربارۀ احتمال جذب علی قلی‌زاده، بازیکن ایرانی شاغل در لیگ لهستان، توسط پرسپولیس در نقل‌وانتقالات زمستانی مطرح شده است؛ با این حال پیگیری‌ها نشان می‌دهد این موضوع صحت ندارد.
🔹
قلی‌زاده که تا پایان فصل با باشگاه لخ پوزنان قرارداد دارد، چندی پیش با مصدومیت شدیدی مواجه شد و تحت عمل جراحی رباط صلیبی قرار گرفت. این آسیب‌دیدگی باعث شد او ابتدای فصل و همچنین جام‌جهانی ۲۰۲۶ را از دست بدهد.
🔹
از سوی دیگر، قلی‌زاده در زمرۀ بازیکنان مشمول خدمت سربازی در تیم ملی است و در صورت بازگشت به فوتبال ایران، در صورتی که نتواند از معافیت یا کفالت استفاده کند، برای ادامۀ فعالیت فوتبالی خود باید در یک تیم نظامی به میدان برود.
🔹
با توجه به این شرایط، حتی در صورت مطرح شدن بحث بازگشت قلی‌زاده به فوتبال ایران، حضور این بازیکن در پرسپولیس در نقل‌وانتقالات نیم‌فصل امکان‌پذیر نخواهد بود و شایعۀ مطرح‌شده دربارۀ انتقال او به جمع سرخپوشان، فعلاً مبنایی ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462594" target="_blank">📅 06:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462593">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdNdNHteDeUucIeuJ-5F2XyUGSex2p4JQtF80lNaAhv9lJMTFkUyc-2Ym7a2PD9CxHFJeyaY7n0SwZm0RKVcUjPxP1HTfpzaVZXPeOdQ4HamVYDN5j6NxsUyRgBOCpw45AGlWkY6IUUsnMYTWbotbyEEycHTo1Uwcjx_QT_cZTa4AewvPGO41l0nRl7a3-V5Pp1jkQu5QhmAjKGyhBsC_xhUsZ6aVUYgI2rLoSURChM-ljqh6LKHZnnXFuflHY7YTt7SgjocY7ASITwpFbCB2c84r3zlV1-mKqWDaYRcqBI2lA20TN3d-_kWOSS59EnQkxnzPm5wLJ0ZbjFuWG5kww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی موقت با پروازهای ترکیه
🔹
براساس نامۀ دفاتر خدمات مسافرت هوایی طرف قرارداد و دفاتر فروش، پروازهای هواپیمایی سامان از مبدأ ایران به مقصد این کشور، شامل شهرهای استانبول، آنکارا و بالیک‌اسیر، از تاریخ ۳۰ شهریور ۱۴۰۵ برابر با ۲۱ سپتامبر ۲۰۲۶ تا اطلاع ثانوی لغو می‌شود.
🔹
آخرین پروازهای هواپیمایی ماهان هم در مسیرهای تهران-استانبول و تهران-آنکارا و در تاریخ ۲۹ شهریور ۱۴۰۵ انجام خواهد شد.
🔸
علت لغو این پروازها در نامۀ مذکور اعلام نشده و این تصمیم به اعلام مراجع ذی‌صلاح کشور ترکیه نسبت داده شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462593" target="_blank">📅 06:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462592">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDkn8BTdCYlt720LWRpg1o42YCZD8anPNgMylPuS2k96nyXT2OzD0pIeHgL67ol2kXAaiCMHqTz86p2Qexal6FWSaZZNpIXt_LYNTOVZnhBCE1nx45yI4p8pBxb8zMtPK-OH8QNDq8t2527rMpdlQa9yf7pd_c346MKqiKiGoYVyE-xUdrN4Y2QOgqcJFMHYhrT7N7-YySGLxkjthKsC3LPoXYmi-D1dymSWe2A6u45BzT6OteL1Kto6M2rKwjn0zEldSYm1mU1qCbtYGMyhLnaYKTLpP0D4n5yuFsCrQA2k0611ry8Rnph9w0PHrVX1fhRnDyIFSCt50YIOwx68uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۳۰۰ هزار ماینر غیرمجاز از ابتدای سال در کشور
🔹
مدیرعامل توانیر: از ابتدای سال تاکنون ۳۰۰ هزار دستگاه ماینر غیرمجاز در کشور کشف شده که برق مصرفی آن معادل ۱۵۰۰ مگاوات است.
🔹
اگر می‌خواستیم در بخش نهایی برق این تعداد ماینر را تامین کنیم، باید ۲ نیروگاه به اندازۀ نیروگاه اتمی بوشهر کار می‌کردند تا این تعداد ماینر برق‌دار شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/462592" target="_blank">📅 05:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462591">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bjbcr5mHzfe9tJ5WC4At0RltnTnDM-ZgANUY6PQTejWDgDGKGSqAhMJafGQbJ6XG0utjPP5r-s__ht63YveTdxj4UD04oxloTjik3yc7qQ9Gu68JILzUA7JYEGqRPONk_uQMXx8eiE4N2EN09fbAHzEWljAUp9Bl4vGnbfXP8qykq6moaNb8VfMd5gVGwL4GzJiqMFbFmjpgRgwOz65I--A6fFqfWlDly5LkMDQtblh6kDL8Tn_BxBan_swvb8fnYWL4Aw6HuIlpZmZcRjfhh4TetoT7pNC2wFKtyGW_52Kha4JO0Ts8RMGtWf8zzkYGvNw9oq-fFDgqrwgd3DV8tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات موشکی گستردۀ روسیه به کی‌یف
🔹
به گفتۀ رسانه‌های اوکراینی حداقل ۲۰ موشک بالستیک اسکندر و ۴ موشک ابرفراصوت زیرکان به کی‌یف اصابت کرده ولی سامانه‌های پدافندی آمریکایی پاتریوت فعال نشدند.
🔹
همزمان گفته می‌شود در استان «زاپروژیا» نیز ۴ موشک کروز کالیبر، ۲ موشک بالستیک کی‌ان-۲۳ و تعدادی موشک اسکندر به این منطقه اصابت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462591" target="_blank">📅 05:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462590">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462590" target="_blank">📅 04:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462589">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0VvnRFqWQ5q5E24ybjqZBBKtpa-2EOLKwy5FMCTbrLO16-j9mHkJUfhySu-VqyU_8ksqcrhrmihlGIJTI-s0c9ApjleUbY6-6ZMRhsRSKZFMbs9ncqfDySivUcIMJ6AtQ3CXhpy1G0CA33BdDTvDCrEl7HBLfWRCyyEpUrSim61oPBduiLXKHq_QqMlf0HSkrQxre0wUqK7FrCr_-xoDCvomtIsf1JYLNcOjC2KJU7_etScFZUOQ9dh6sVcHZ9qIjiVQHGK06gGrGwKAUjrDlxs6gBP4SfoXSzomHUQsjQfT02bUjVb-UOZ2uL9xFj53ZSK48QxjGn1NPv5xBHvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی پس از سفر به چین: تصمیم‌هایی که امروز گرفته می‌شوند، بر توازن راهبردی آینده در منطقه تأثیرگذار خواهند بود
🔹
رایزنی‌های موفقی را در چین با شرکای خود انجام دادم. ایران برای شراکت راهبردی‌ که طی سال‌ها با چین ایجاد و تقویت کرده‌ایم، اهمیت و ارزش ویژه‌ای قائل است.
🔹
تصمیم‌هایی که امروز گرفته می‌شوند، بر توازن راهبردی آینده در منطقه تأثیرگذار خواهند بود و پیامدهای بیشمار و گسترده‌ای در پی خواهند داشت.
🔹
چهار اصل صلح که رئیس‌جمهور شی جین‌پینگ مطرح کرده است، اهمیت کلیدی دارند.
@Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/462589" target="_blank">📅 04:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462588">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21a9ef573e.mp4?token=uoImqNj1ua6IQSVQh2r5eYz8zVv7d1d_7L4Iwguac1re03HD-EPg2eeXJuK1b8CqycBTm06IElQ1mirNEhVB3tekM1swTOLtw6bL8TBik-uOPjOqs2_IVpGZ_p6_khvB7EfGrFZ91A7CVinas3SfjD-LKbx7xDkX7FjLh7nK8cKADy2ot6GkkMdvGInNeDbQAcev3qEc4uzDz-IXWRFuZGl6VBBPBICNU9BzgpbwO0OxGr9YiQHaH15z0odfzqEFbyewzVXXnkGC5EAjzp3nwmgyeAfbFe_gvv8UWatEQ7-Yp5ZmNUZCA9RwUOBBJdDwLl7yM4hIFNCwnVJGfW96rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21a9ef573e.mp4?token=uoImqNj1ua6IQSVQh2r5eYz8zVv7d1d_7L4Iwguac1re03HD-EPg2eeXJuK1b8CqycBTm06IElQ1mirNEhVB3tekM1swTOLtw6bL8TBik-uOPjOqs2_IVpGZ_p6_khvB7EfGrFZ91A7CVinas3SfjD-LKbx7xDkX7FjLh7nK8cKADy2ot6GkkMdvGInNeDbQAcev3qEc4uzDz-IXWRFuZGl6VBBPBICNU9BzgpbwO0OxGr9YiQHaH15z0odfzqEFbyewzVXXnkGC5EAjzp3nwmgyeAfbFe_gvv8UWatEQ7-Yp5ZmNUZCA9RwUOBBJdDwLl7yM4hIFNCwnVJGfW96rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر کارمندی یا کارگر فرقی نمی‌کند؛ محل امتحانت همانجاست
🎙
امام خمینی(ره)
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/462588" target="_blank">📅 04:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462583">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUzc6HOu5RnpVuPq8jKCbCHyoFir1rGsbbUeHMrmk52SfmdpUEXOCqDR4kf6tfKc3S-k_JUGbJ_EQb4Z_rAI0tVaxC_Vgn7RBP8OT489fsqyQSVDkVg-SVorgwcAezMEMT9kj71GXCQPgO6yU0uR2l1qaxSayZ8wzKV7IgjBcKdLhwgnuE1zmO-1zcOwa4rK44v40v7XOlQmAHGq_wFx04JwX2rK0QbYi1vszD_mjbbhaGKBlIY8gsU5VQXu02UQCZYJg3GtDsP9hDnrvhVD7JMg3u7hWS9ghqtw0oGVDafE0FhpHH8pJnWHyGbAeT4bp0x-FDAWQ3o2T5_oD_Yc2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O6LAyao2ewTFFAlU7qvLRotL9JkbB_woXqn_7PIrrmnRLgZCsZR52LcwF6jU9weEqpeR2gK31UyrIIsvXaFvx6H2jHOC6wXeuhSDDRyAT674j3C-tYoZE6TgJe0qAUntVlJzZBHHJSlPhDV8d5fNF_haTtTrVHnY8Q7Ve6AHJkO9QYc4MkbrqLiPMAWJHP8plnnnjG_FC867NBnJubGq73wYLlv8LmhUgD5Eig_SpwWhPkrAM2_F5qh8rgpkFAoZHjRcoYEvxo8Ss0Ap9TdCPWlp-94c3iX-nMgWME8MQBp4ty_TZm1sSHLY54SwK4hAT8aVh8J0TK3gZwfQncty7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Su3Af9V9CAsbKjXv4aTEes0yFeogpsu5hN_e2NXgoUE4MShG1P3MRgCPvGXTxm2F5LZTZpogwmjcjl7jGW08s2zCn7qzuT2QzgrtCUfgXx7u6Bb3ojx-36NNwy0hlPg0OpB5vvtW6tkpfy20boDLZ22DudUH8PVxqGkOyUlRSOYOMCix10oRfx9WdbM0e2xFwIgWpVyRe9xXwfTskZmKnNy5t1qqoPhMmdAfKcVeL_UsCQRWtzVotkYGJIjEl2158fWtEKcpXwMLzx944FC1KmygfYDqppt5Syh5aqKF22zQ7iOoF2fU839l45WIjF0RojByYbFnzjbB_Qhg-fjlqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTH8s5HDPPV3iYlSczBeGNOjMABGX2wo1zg7epjHGcZuVImq6_L-mRI72Smqb7UeujKOBQ_2MLvvi7CaM16AF5qaRsfOjxo6uOrOCQtnKH294TN5KMP_tjA9Ze5LE3Qi9WMFINh9FRlNY4ris_CWxPhbwT-ez8kmjmXBMG9hVX3EGQCcJsqCqcsZKbWJoFvO_-aUNNBK39dhNZTGnzVFoG83sc2QGAjFIVOP4CkOo0mtxyYt1FJUXpjXwbC4HqtsGHU2EbjB3rhs-kz-IOZTZmqLM9NgITMtwEwXh-RfqwWwsT8wsVfolKAxeA7ZK0IvRlDZ1VM3SkQxiGRa5GDW1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oU7tIcYDvmDJzQnH9BHbkeBcXLAIuef8n82Dm0ObJKzNL94A3PdUP9KjFsqatm9RGtUESa95jLyQ8524Q7qTKhP7LoPVM2DZvn4in02vWm90cMjm0EHMgwEM68isZAaL_YQm45eaS-MRFA5_VIilb0QqGGXRQoNJoHBsCRAbv-u9Liu48VKI2Jmdo5rhi_Qi3poo-1-OYn-fpTsaiSkMdMihY4IUUAHgztBxflpwCefaMkKUtFDitpie_vrulxkLbAYAq568ih_tx-G8dUbbYu6Uwb-eGhncRa1MN1UoRH0yo0QJFG9Y_Sex4k13Vd3iZzv1_KjzvjVnyUbuqwXPqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دویستمین شب حماسۀ مردم کرمان
عکس:
مهدی امین‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462583" target="_blank">📅 03:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462582">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c651f359b.mp4?token=Q38WeyDMKjOtUNdxWPSEP68e3nBucZGo8nF7bczfoKVjS9U2XV_ZcAhP0iSbT0vgYpUZVmcLof4HjkLyeBN23cGNdrVic_ZWVx3sgpQmdb6THNPZP0Su2oosNArooeWkef8j_dqpEv-kz6SztD98MzlKv2GMnvKbg3DvP5gEcPUKTrAqymSmX06L2iZLnG27ktiseUykjxY4FZPTAlJCTeydVJ5z4WNPdiPcob1EAOwqur4Ylg5idGxhtJT4UoGsovuHOmqyjyZIocJmbjdABbtDT9KNC-0wdbiQsBap47hBSPGRzUtIksQuBTY5B_sPvK9M59iMNPzFcTW5mXCuqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c651f359b.mp4?token=Q38WeyDMKjOtUNdxWPSEP68e3nBucZGo8nF7bczfoKVjS9U2XV_ZcAhP0iSbT0vgYpUZVmcLof4HjkLyeBN23cGNdrVic_ZWVx3sgpQmdb6THNPZP0Su2oosNArooeWkef8j_dqpEv-kz6SztD98MzlKv2GMnvKbg3DvP5gEcPUKTrAqymSmX06L2iZLnG27ktiseUykjxY4FZPTAlJCTeydVJ5z4WNPdiPcob1EAOwqur4Ylg5idGxhtJT4UoGsovuHOmqyjyZIocJmbjdABbtDT9KNC-0wdbiQsBap47hBSPGRzUtIksQuBTY5B_sPvK9M59iMNPzFcTW5mXCuqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر آتش هوایی و توپخانه‌ای اسرائیل
🔹
رژیم صهیونیستی در ادامۀ نقض آتش‌بس و تشدید حملات شبانگاهی به جنوب لبنان، ساعتی پیش چندین انفجار در شهرک‌های زوطر شرقی، کفرتبنیت و نبطیه فوقا به راه انداخت و جنگنده‌هایش دو نوبت المنصوری را بمباران کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462582" target="_blank">📅 02:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462581">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آمریکا به‌دنبال اعمال تحریم‌های جدید بر روسیه و ایران
🔹
مجلس نمایندگان آمریکا قطعنامه‌ای را تصویب کرد که راه را برای رای‌گیری بعدی دربارۀ لایحۀ تحریم‌های جدید علیه روسیه و ایران هموار می‌کند.
🔹
در ماه آگوست بود که مجلس سنای آمریکا با اکثریت قاطع، لایحه‌ای…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462581" target="_blank">📅 02:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462580">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حمله به پادگان گروهک‌های تروریستی در سلیمانیۀ عراق
🔹
منابع عراقی از شنیده‌شدن صدای انفجار در منطقۀ کردستان عراق، ناشی از هدف قرارگرفتن مخفیگاه تروریست‌های تجزیه‌طلب خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462580" target="_blank">📅 01:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462579">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9389bc570c.mp4?token=jx3t_1GZiWsGXw-pv56xOEImEDLzW3qzTcf9gYj0MSGQImA20BXJ8l-2J6FmgofN2a4x5M02H7W80aiivY-TgmYfSre1UX_xDjrjNMWNmvsm_N1wdC_3GLO4le7gMcog1IuisrsQ2FYIbyH5Yp0r3Bd809zpEuKkifvYlwi8KklgTcwPMjtecqVLsf0n65ZVnJ5CwQXelaQ-Sd6wm75VuOP7RX5mjDjGqbXUC06E9OeT2dcInkcM43ds3hm3ANvDdLkueMGHmPfJH-5K6NPmjl22ayrqj5HJM8OSg-iT-8fsl_--WOTxuFPcOdJBFjtuuRIN0mfsDw1a--wS7rFwng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9389bc570c.mp4?token=jx3t_1GZiWsGXw-pv56xOEImEDLzW3qzTcf9gYj0MSGQImA20BXJ8l-2J6FmgofN2a4x5M02H7W80aiivY-TgmYfSre1UX_xDjrjNMWNmvsm_N1wdC_3GLO4le7gMcog1IuisrsQ2FYIbyH5Yp0r3Bd809zpEuKkifvYlwi8KklgTcwPMjtecqVLsf0n65ZVnJ5CwQXelaQ-Sd6wm75VuOP7RX5mjDjGqbXUC06E9OeT2dcInkcM43ds3hm3ANvDdLkueMGHmPfJH-5K6NPmjl22ayrqj5HJM8OSg-iT-8fsl_--WOTxuFPcOdJBFjtuuRIN0mfsDw1a--wS7rFwng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
شب دویستم میدان‌داری ملت مبعوث در میدان انقلاب  عکس: مبین علی‌کرمی @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/462579" target="_blank">📅 01:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462578">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حملات هوایی رژیم سعودی به جنوب غربی یمن
🔹
جنگنده‌های متجاوزان سعودی بامداد پنجشنبه بندر المخاء و مواضع نیروهای یمنی را بمباران کردند.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462578" target="_blank">📅 01:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462577">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYr4jTyb593FuEO7DJHCgreuhHz9THrE2yg8PkEKKtBetNirnxrqt3T4Cr_H8vzTn4Oi6tkDtSqTEXkCp5E9JUaelD6INHpR2dBFtWXg5L-ydnXa_HQ-qdA9psbFIzUIA3uafklzuEFT34WP6wKD-E7c-YHbOk0vMr4Xc02kWxD_2ujScaJsFio7lcrOGio7uhYfX9uHJwmcj34TCyBQ_hzu0EnCNLFEPB3yrUmovjEXpyTZjUeEHFva3MWQZwXsx10qdQ57eDTV5cE2xRvuXLhmzoLUmkuuN_c42O8z8h_vgUyNT5jj_wRXtW1S6Cr_eBRnYdbsNfg_4mEvKsixtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای دروغ سعودی‌ها؛ سناریوی ساختگی علیه مکه شکست خورد
🔹
«ادی کوهن» روزنامه‌نگار و تحلیلگر صهیونیست به نقل از منبع اطلاعاتی غربی فاش کرد که حکومت آل‌سعود یک پهپاد چینی را با هدف جا زدن آن به عنوان پهپاد یمنی در آسمان مکه مکرمه به پرواز درآورده و سپس آن را…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462577" target="_blank">📅 01:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462571">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0vGhDDSAi3wqqy7YzV3x-xdCIg0FzUjeIfZrZ1Uwmk6kFzSsgPFib5FoT6r-lssQyUUa5jdl_D2H6Cf0l5-NfaPdfpK6JrIGaMSEtK-cWmOm6VVxU8gaMrI92AtXRKnBkP0svlZZtxYwmnyKoT6GZ0t61gLTriadrO5GN-471wbx69Nyn3xZibQ7Im9gKl18I5kuY9ayC5k1upvQ__qQjN7IM4bv_OGXfAOCmjx1lcutUvIrmCTs-9zcNOI0HX-yS3-6_Ujc7o73WD-hbnLx3uBJbIg-3js-H-VIejrrZLZa1jxisoBsFM1qx31AJLyjU_-7z6WT2h3LhmpZPijlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWsX78A1LlcMJ6Z5PA2IOuPQbloJtGGpOc-S9kYX51Xnhj-HLVVaN-_EPqAhm_DeSZjZBiCDwFeRrgRwTUpiz6jcn6Xdj0RrW6WFyFFztkKBvh27rGUXC_PKLDY6-PP2qOwlNLLH6mxKyMBAjqHqAOx0v2etutxnSt5-IITC5wXhkq76CEKB4QltonE2iDxcigVUt0Bg7MA60J23vzjvx7nmalNTe2Vp4tqW4TNlnw3vrNHpD2cdzFhXEquKdfEWk5cFDs766eSfoXyQqbdC8mXQOkYZEcS15tGytFo6lXUxU8PqFhE3QioK7NyMbdA3XUR5zxvBRDRdUMmn_zAzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bodFAP-SYn4NI98FgsrbZkBeR37KSOedYZztgpsIh4w21xrrTD4tLWpBEDmMcwGNwq6j3o5uAe8DrZ7W6qqJDzz3W6_sJBrj1ZGzHo9YFFIGQ4h0fnBMmQTDYxNyjBAtHxvc9uE6BtuASO6ZQNuhtiT6abd8U-8aAi7r7pyTSGUuvQnJGtGMgqc6ThU2Ynv_8RJpfv70jhmAVWCQJ4mPFXkpT64D7T4QPZQLOcwCmqwQncCGFBwm8eossixpkLD_d5Ff5pmosDSGqS3xSAHNO4CBY0L3nWg9gC_KNqWBOxTLwI-Rpi6ZHhT5E0TxCJVsQkIJZjjLFagmtU8ADq7xcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-U8ebTw1kM6Nc0O4e6lnKNJTszYNFzdw_JBq8k-Rr2zw9BjN8ebvV8hDFHpRCiEaZ_BDNfvHCHMVy_UYbf_nozT1iTF04SFsCxZTuAiNnlO9NZQ8XLaKHFoVwR7beNkcb251Z6y-deAvuZ4VZ1kNhBxi-NphnWjx1wXTYQNa7gNVx4DwF7ncSI3dKDU_2rcynapUHP3kvW-NdsPCJJFHyS6i2E3u_B9BbjnjkUo5-n_UTYjVJy0RifJB8YNh4LQGKqjCJor5teSxjoGpFuoByzrWivnayn7EqekCnsX0h80dpIvEHZw-frGEbHBNAMT_QAFQO7i6ECZ1WXBBCrQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKKbS_dkBxg9H7jfmSQBpvyvX6udB1m0mfSPEdtqW3pBu7j4KZQD8QhITWOx7M5uYn1cFOwhBeYWUmQESJYJ0_tnHmuFr1_jaHWv6DGylSf_goYBTBP2f0vkJXo1kh9DwG671BvTncErl3ORuE24Zm-WklcHQ6dwklbm3BzGkv44_WjviU3U_Oq0SD1Zh6_z5IjmmjB9oSJLRGuMrukPuMj5lj9J8W8UlQ0N4CgfG9SEydo-Fk9pNDQVDmT3bzXgD_XBrfeyGDL1nwci0wrYfhr8aaacuhawL_9DOxcP_HGiM1GNN1G6Ojfns3CZd1R7p-lJhFgFzlEE8n5eSi3rRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muZ6gLeN3TeQajFo0MuuHqSp21E2fiFjn3hw2VNTMOfgQj8kGdlmZ9H86k_-afJ1bohivs8GcSh5hT9-tmn12ss3bauMziP6oDYJxRu0dbYaGJlUCNFL7ZX1dr5PHzysSQ8JlUjGb9TI4jMUejQ6Hl3RP-pFLpnoQsr4x5i57Nb5H6Ixm-ERnknQ7ClUcitte8fzSMunuaQAJwRKp0yhDSkbUes8Go0u88RnCqVcosmUjOjJQZX5_rCWtjh1GeuPLgJ8NDGhCt13Q1EHskl0eqKOC21t8Adg91MfaOzX9cYt7tfAwjR09lNoz0E8mpT4q7uW_0rFUO1Wq7AycvxMqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شب دویستم میدان‌داری ملت مبعوث در میدان انقلاب
عکس:
مبین علی‌کرمی
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462571" target="_blank">📅 01:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462570">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1941af2d61.mp4?token=KtEjXdZy8jVEp5jFYJobvds8dKsfCAseuih5R7VdJKd5V0fh1EJOuU1PgmfQ5nOExLGAvx2hQkqKXOHrztZC2nP6mfju3o5hrmeHs7ELdiyf0z845aS0B2nR2deEQ-6o559oRhFJgp47SIZYjfr-zf9i7MW3EbrSs7MSnH_DdkBHmMozxF-L98oGeB_80RjenKg_SCSPs45D6mBm3NNCUH3I57pINDlXqOWDRLurbQNvFVClCadS5VMjH64_iZ9JPnUbuHop6P9qJhjmcl39oGdvdV6sBn7QnvwW553B3vagfh1XhmbJhSQ9wlPfOtNT2wQ27jk3sGW0KYcxAiXA8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1941af2d61.mp4?token=KtEjXdZy8jVEp5jFYJobvds8dKsfCAseuih5R7VdJKd5V0fh1EJOuU1PgmfQ5nOExLGAvx2hQkqKXOHrztZC2nP6mfju3o5hrmeHs7ELdiyf0z845aS0B2nR2deEQ-6o559oRhFJgp47SIZYjfr-zf9i7MW3EbrSs7MSnH_DdkBHmMozxF-L98oGeB_80RjenKg_SCSPs45D6mBm3NNCUH3I57pINDlXqOWDRLurbQNvFVClCadS5VMjH64_iZ9JPnUbuHop6P9qJhjmcl39oGdvdV6sBn7QnvwW553B3vagfh1XhmbJhSQ9wlPfOtNT2wQ27jk3sGW0KYcxAiXA8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرزوی زنجانی‌ها در شب دویستم میدان‌داری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462570" target="_blank">📅 01:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462569">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03139156bc.mp4?token=n48Y5IW7QbnNfJWZgyxpRoC2aBz1kqD8UO_HpHfEDlFtoy-2IKdufB16S3L0O5PBXu_ep4Ea9xUo7ksUOCsBZ270VZ0UPesQ--Vg84jqYG1ZnBRXTAgZq6A4thRevadSqo17KPlzzUZEuHNAHakYoCcPT4Qh6A3qWnJY2LUwP2a3o9DI-BdzEStk81FCczbr26IZtg2rEBZdgxo5Yxo9crXizSAhg1YEZbx-xbfFuqJI-lpb4u21YoiihtLW9Z-AlrmBqt_Lg6xbFFKA1CpqB5j2vhf5TprxrKh5apqWixOtkI77oc_6VoihM_vd_EGvwu3eX5BFM9FccDeqkrwxHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03139156bc.mp4?token=n48Y5IW7QbnNfJWZgyxpRoC2aBz1kqD8UO_HpHfEDlFtoy-2IKdufB16S3L0O5PBXu_ep4Ea9xUo7ksUOCsBZ270VZ0UPesQ--Vg84jqYG1ZnBRXTAgZq6A4thRevadSqo17KPlzzUZEuHNAHakYoCcPT4Qh6A3qWnJY2LUwP2a3o9DI-BdzEStk81FCczbr26IZtg2rEBZdgxo5Yxo9crXizSAhg1YEZbx-xbfFuqJI-lpb4u21YoiihtLW9Z-AlrmBqt_Lg6xbFFKA1CpqB5j2vhf5TprxrKh5apqWixOtkI77oc_6VoihM_vd_EGvwu3eX5BFM9FccDeqkrwxHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی گسترده در یک انبار نفت در استان کرکوک عراق
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462569" target="_blank">📅 00:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462568">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJsK-cI8OfHi4WXOyDD2CjXrzbtaYrsJRA_5DUFPafjuiVUgC6TRIotT4gGuzpLsIz7kLYj1_mByIzsRpo0R1TP6gjstW_L1OQRdHCq52eQQFQSoN7sb0KAUlmyL1rShADoLQCWm6X8T7pBNb7kQC5VhoKZQ_JiNg_THmiVuVD8hRPKbHb7O_-lv34f-Lca17HOdQKPNzVUZyw9RGF-uC26pjJ5SlUuBI-n-jbKXzK7fiJYJUMQMJry7veBI3cbCkk217--XM88GjqyzdjhqWNiAWncBR0aEwNulJGAUe7QkyYUvnDCZoAyd1GXoPHr-PspnAotd-j0nPPehkx7VWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از حضور رهبر شهید انقلاب در حرم حضرت عبدالعظیم حسنی(ع)
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/462568" target="_blank">📅 00:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462563">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SV0T_iQwThEksZxkYcCD3fCyzDJCFmZxi_62LIXKsdi1ftG6gGkm0frXAuSsUXLDw_mnEdCeWTqERAhVCzO_1HldR8heQFBCxq5cH8LFGo3x0YsLqjcPnWfCANPv5qmkXL0UDMfztBZj7EkxRph_XVuWuGgqVRVKr9-sgULcx8g3QGIFiWhqQ6HLLiywHGveiULAbZU1Jb8iH0MeigCF4qAvYGuKhLRDeXsXVqcz8P0dpxUBsdpyhRCb8dTRDGF4oKRJX4Mp6Cu46fIpZo5XW2mZc2r2vlRiTlFlTUmeMktoDT9L65hnNXqZBrQpCupRSR3wNK1WP4W78VP-C5eGrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e0W6TW_A_5VvoRPCNpSy5TI1YVoBzwH_meftTxQsnY3iJ5HF1JmpzvumiHXd8_xMPS6wH7YoCB8A6vyKSjGzlzcrQnq7FrMXbweO3bio1NWdhyAR-Lwr4DMz778S8JpEbLoKMBt3TRaDa-OSGHGoRi5livzkU8Elq-XC-fwrU1MIrqTy1xirf6J_gWdBxdoBHSgOfwsNYOsdrHYkjIHL2FYmrd9Knz_oDZoStX2gAV1B8ybS_QzB7lxmwN1--3DgbmwQad0ybxtICAo58ow9dxY37KfhIZVjcdMNpFJA9_WNkN1MyLLfR6ZcjwfxwtzMBxXDU-HJSFP9t5nNyc3StA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijVjI6z9H6u8tEk1p1_JYAF7Du9D_JUA7j59TG74XmqE0N3XN7YT_pqA42-kX8snNOWlXI8oV0ebj0QrEiGBTa5kIeUC-0_R6mkTe3xWFSkPd9CAAEAdLlm2xVsTHLknT5v38aCfIAggdx9NwsHa4ktEU9bxTskYTKrkoIj5TeUXVQvwZFbO1S9YZD7ASXN9IeiSrIBsxlLh96sRnt79Pi7HGFZPQgxzzRrcm265V9Qr8hexmFhgVGnRa34NK-Nf5s4ddUSzcv8T9Ry-qKfxuaRN8DtbNmfCsyijpHBX3q8f8IKpIB3CisK9ZmtJs_bbpQUglwVNbtKQh2MhRT-EhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUS3uFa8OyWUt75x_gM18WbUUzR8KoRHxVNRF2wSKiVKeymupuG4ffyiYYRQMkiIM1g7_mE83G0IeovkQ5FtGesqWUyDJksmUHPY5yl7ghMqreAmie52KUmrJ7PxT0JDhL0xkjtpt0eky-6CsKeXU4SH9DdRLE67mLVYt5yQ3REed0QLvJdAi43ABGNbyziKrBs1TITwYrc8mV3APLE50fpNzk9W69L1GYi3pe5Hybbf8dL1B30xoGjSF14yL9SXBNvY3p9wmU9hZWRl8K05al7YKjVKkVSUsow4mhNsqlCuO5-gQBMjhz2qOdrVB0wVBPBiHvef-WJIRa-hiJjFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMg-HLajDHcSvs8E2g66F-A9b8r5KAbb3xC2i4erY_u8MVXgUFhxe76Av2tK1knRBtmuO4M_K-FvncX0A2TyRon83Q3jP0VB1d3yhWThgrvMbpASCmE0zkMlJef4XwrSUN6hircSjZFqJr9Ge6KewDp25wUtCqWzTX5cNwi9CPKgE8VWh1bCweYFFfEjQD6A4IMy1aq7x5rMn090rhJjm-8ABfONmhoz01myajg2gPapBThqN0KUHlsnyrEb2rLyIAvQ6SDMNygbyp-vTW8sUR-8KCmN5pF242zDnvqVAfR6C0k9nnI5O2qksZKtMqdkM-OtEehCUm5Md26mcYbaag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۲۰۰ شب لبیک به امام؛ ۲۰۰ شب میدان‌داری اردبیلی‌ها
عکس:
سیدمهدی پناهی
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462563" target="_blank">📅 00:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462562">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رختکن داوران فوتبال را دزد زد
🔹
درجریان دیدار دو تیم فوتبال بعثت کرمانشاه و نفت‌وگاز گچساران، درحالی‌که داوران مشغول قضاوت بودند اموال آن‌ها در رختکن به سرقت رفت.
🔹
به‌گفتۀ داوران، تلفن همراه، حلقه، پول‌های نقد و مدارک آن‌ها به سرقت رفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462562" target="_blank">📅 00:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462561">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyoFd1aYVJtpOirw20rdoagxPMGvrpjjZ107jI_d70Kb5IDJZMBIBvt4PUYuG-Uj9iHdC_gIaRObTW0ryJ9g2TantJ9tMwIWMD-SGAEt51CWtDbZm4WPuo17SGfoXHIvfVuPBm2LCDLAwCcH8c4N4Kw9RSu8xEwMqRe5xFoZY2UlkgNckUjcwGkfGegHhuaxSlgLWA16Ma9GburU4VUMdfVe6Am3jYQWVmAmBeflczjmH13uLs7sJkL9YGqdTJYw30YberM-txkh4pCqO3RB6eOCSxRWeyG8xtQwXDAqXO7ZCEcCQ_1-dNHh7biP2GHfmn1uCldXNtL1zkOkEBdNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس، معاون ترامپ: بحران انرژی جهانی تا زمانی که ایرانی‌ها به شلیک به کشتی‌ها ادامه دهند، وجود خواهد داشت. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/462561" target="_blank">📅 00:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462554">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tla83sCv4Jj6kdQ1OxsxuXUrwKZlDAfGBKgrXKBO7OOsJCqJpubWnldFvp1xTwaS8s98LAOpyMylhvnkTiir547YVHKOdg9Hsathg0-ZPRR_tVxLZQysSEMvGkgZQsSnSVbk99AODY6tpfeZ9t54R9houXHCXyVlWfPZo8uezYBUKibJvC55jnU64gwFOWfXTz1r1pde2VMisSsPgVPuQM8RIMDkl3SevF_V-1p9CWpfVZAY9sy1hGUhjDdVDLxWqs8R35LXdQqedJCaHWyXMTBN2hDMU67G0lpL7hrZEIGfpPndduMBULfB4gYWY4u2kIS2SVSdGFJU3HhZt-Kphg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUFQ6xDh4yG2HaCbewQfe2RUFrPz8vZLeNS76U0IoIpXDdNJMGOXx4ANvAWAcN5Dn6r98dDOABapL7btmVsgQ4Br3pPVirpT-sHgnkdQhc4xBWYH6tFPs_xGtvkvsW8Je9aSs6hahEtmsTGEsFBAV5MKVzpvw_9JH67u61cRUTV3PDlQYp2ZjsQ8zmNod07aKGnVpFE_ni3OcB9M1UC-Y_7YdcuImm0LpFbMFjh2GsMHXdjLlxef9rNw5a5T-K0Crid9VTRhK_bc_PQ6VS8O3jffOlcz7d7qwkU4rBq2MTURfcC3bhYp6kI-E-Reupchh5j2xNotzIJfbv68y2IAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8JjIPCs4_YQ5qKrbE1ayQVveAlMmgeA8f745jgmotGOxlYV_gz_k9gtf2F1Bnpa6GnOOslQTRae3-9lIzmBAvo00fIJPxf1gbrXlxDa4btvJ_s3PoC9aCuxD8NRC_wT4x4uhX5uNumcPU1E8VEWwjp7ZhGk9XsdT3vwuqPzoaKPfpLZbBD7RYwVbAuQe9ovoA3Xy98XIybvELQyVpRKZ4qB2WZ9W6bl2zW30gXw71C788JqxPkdiGEQjD4IwPZt7R61rK65Q0fSK5hhh3JF2seTjP9NxwqkdaXeyi2HkhYxGakoZ1AYBtFceBPdtc1kPAEenZjC2_3VL8MQ7YIVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m_RRsJbjYXTwhB7JNMApdqi26rOgwcuCTXTG6-Voc_jhIJ9CRGMmeAGtgLQk6jr5rxIMQoWoHpAdktdBX5UQwClXxTa0c2E2SvEdsiutmJT7NOqBZSqrMCK4umIWw6-PAGfsClBqWvHcyoB39v4WuMpK2qa85nhiwSrHpaemtf3SfID5pY4l8Li2DBB6pC3AUigKEmpyEPjokDXPVIELj-6LaWisJuW710kQ5xjDz0M5jj4FzA1Mb_D1D3I9KHs5bTdwgy-HxOZR747d1CvxiVq3D5h9-K1oOAPPs3PBO67xdwA0cPOxxkmgyKPBk0RGY7H58z6HBABlRrTEah5C_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQJWYJtOnT6mpaQz4NGybnI6peP8H-IdFB6SxrXcwEKhbU916w5ydByri6Wti6a-4Xop3TIlwxa40H_hogiWf2uKse2tc_yISzcH7AbbfIuy1P5q0m8tJ5O4QSXjOkdcMboAWJnr2b62XW0VDC1MoBeLQen7MKwED3ur4wcTtPhW7eC2aMca5sdW1HSHC5vpdmYSvLjYS8eg_Vfgv3Fo6fDnw39_yubNmlgehCLQGSaW-zLN7akVyzyeyiFjdikkj0bLw3JBG0OhHDK-Rwcy6rm09xJ141z4JtukGrogAzrSRYDgM4VHb9LIX4US2UVV0a1qMME8P2CenrZxU1XUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CB8FXdGlKvUepeklu1hfUN_RU634KQPDpFcSNAF1HcMdtNWO1Xz0fDNwtOqLA0LBc4thIZw8NSMqHzOyrOmi4M1UCYAydaVJPcMWgQwmbUPHZZCqOtk030EDe64h5KuOYQLeFgGstf4IUP_xxWkMtQ_1-RbRqKx0xW2YhuZ-LeKdEwyss_GjvD5fJUU3dk8a2YllW-6tzD6_3G4eLWvvxJEhV2YUIl1TLpjtFOND1BByRq5hPyPHx_jMa4rDuurQA4st3FF0On2XmAJJmdnIbCHncY3GybV3v34mIROJPPGoRLL8_1y44rwutVWiJHvvkxRDFLxZscTfMHXTSGmKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PhKuPBCOpzqLvjc2HGuQPzDNODcQpEAPTweU_YOAAYElVklTRxq2q2jM43n9oM0Sk8uR-9I-kCCGAKsWqVcFc0hAl-DRFXcoopvjqthd4PDYJV-zMKm681Vfpw6MarhOtOCqT-0kEWmI4Hc4OjIVg9Wt7NeUR3P4sW98gvU8GIjYtbA11iKR-QaMwsxnysaV6uONvxkUR_3XdCgwseM_xHiSoe-syWS-LHkTdzEGVJQcr4A5GqraWHI5kqQSekEVnvjViDGK_EbdbPedv8Q3JW9CVwwvR9mOL8kAer3YjKTxdxS8S8kdDu49ZLfv0RW4IPcN1N28uziXjXwbQGXaYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تولد یک خواب آرام در دل بازار سنتی یزد
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/462554" target="_blank">📅 23:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462553">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
۲۰۰ شب میدان‌داری شاهرودی‌ها زیر پرچم اسلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462553" target="_blank">📅 23:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462552">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XToHQE_Vvha_pk3rLLY41LHl7AlEIk4Rg_07FD--EZ8oex6Aa9jBXe7C1zFLzkQjw7cTQ-aMtz8-UxWsAT6AeoBUG1VEAqPO8mY7X_NJQlGEsvYUiCVNBCXWqcVkKs9xVeGKJxjKHL-1s7WwXuA6XTe0W-7bCAa1CztkCelxMMl6ZiM9gOo78JbGLdI7J-XyVWa7UcIA5mQH5BRo6KbAJY19ErS-EhwV7eL_9_cs9Pjq3aUQ1p0EjQw5pqpWqRCTYp17QnuaHF12gFNQ8mUNOZ3Bl1hM1hdQzKBEidGpHvoRO6_dD20StkoS60eHDuGYPcc_PsHjI697UcY99FHBvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مجبور به ذبح مهم‌ترین وعدهٔ انتخاباتی‌اش شد
🔹
فدرال رزرو آمریکا با افزایش ۰.۲۵ درصدی نرخ بهره آمریکا را به ۴ درصد افزایش داد؛ این افزایش ترمز کاهش تورم در دورهٔ دوم ریاست‌جمهوری ترامپ را کشید.
🔹
۳ سال است که نرخ بهره آمریکا تغییر نکرده بود و پیش از این ترامپ برای جلوگیری از بالارفتن نرخ بهره و تورم که شعار انتخاباتی او بود، با فشار سیاسی رئیس فدرال رزرو را تغییر داد.
🔹
جنگ ایران از مسیر شوک انرژی آمریکا را در دو راهی رکود و تورم قرار داده و حالا تصمیم به افزایش نرخ بهره می‌تواند اقتصاد آمریکا را با رکود سنگین مواجه کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/462552" target="_blank">📅 23:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462551">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034d9b10fe.mp4?token=VO93uFF9BeFnWgzMz7vjPj-wbcoJe_gtX88_BTwsZ26YtiQSgd-NuyKmUp29loKutSdrf22uUr3FnP8gXEIJ_sVi0cPluZo52Q536xAsiwP1XG1vgNGA_tC2MmCnSivlFCjITK6yXj9l5bZrzgqdWAmvwwGNAy2mVttMf8Wh_MfafLCquyKtgt8L9XFhuVajYhPK_3MXXSzBkBYGLkHlg6BrfM-4XVs7Ng42s7gikA4izZ5Yo80Nhk9T6ugqvQyTDRMOtlyb02WWgHrB8iXarnASsVeK4TU4A8ymN8pLtSYbcR1H5Mmz0ONHZYamuAH97RfcdbwKw0-5PfgujkOSsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034d9b10fe.mp4?token=VO93uFF9BeFnWgzMz7vjPj-wbcoJe_gtX88_BTwsZ26YtiQSgd-NuyKmUp29loKutSdrf22uUr3FnP8gXEIJ_sVi0cPluZo52Q536xAsiwP1XG1vgNGA_tC2MmCnSivlFCjITK6yXj9l5bZrzgqdWAmvwwGNAy2mVttMf8Wh_MfafLCquyKtgt8L9XFhuVajYhPK_3MXXSzBkBYGLkHlg6BrfM-4XVs7Ng42s7gikA4izZ5Yo80Nhk9T6ugqvQyTDRMOtlyb02WWgHrB8iXarnASsVeK4TU4A8ymN8pLtSYbcR1H5Mmz0ONHZYamuAH97RfcdbwKw0-5PfgujkOSsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۰ شب عاشقی؛ زرندی‌های ولایتمدار، هنوز پای وطن ایستاده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462551" target="_blank">📅 23:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462550">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1a9988eaf.mp4?token=BHbPJ0H5oOYK7wZXCTimPnZxltLdp5yKCfl20-gy30YDEAqP604i0jS7yIcwENv3VWG-JlyKTicx6DMRbLNB4sdEu1W23APqrwrsOhHVrXer4ySILMfo9kPWC022DoPDpHpMK4jPNdoapgWhrx3-ouVDgAQuaBNp9_V_MhSOZvNtN_IjNMigQv8OiTvY9HxRmutDlTERmGF6qukiqkXJfkq1dDO4jaSpZN-thvwwxssoX0ZEwNOvogdpvkZYuLtKz2U4SaC8kgfplXUU0NNN9cVaUJKDffE_HrOoJhypEswVyAeIi851KpthpHhfs1Kw5vuER_c5nqSZ_TwvtEUUQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1a9988eaf.mp4?token=BHbPJ0H5oOYK7wZXCTimPnZxltLdp5yKCfl20-gy30YDEAqP604i0jS7yIcwENv3VWG-JlyKTicx6DMRbLNB4sdEu1W23APqrwrsOhHVrXer4ySILMfo9kPWC022DoPDpHpMK4jPNdoapgWhrx3-ouVDgAQuaBNp9_V_MhSOZvNtN_IjNMigQv8OiTvY9HxRmutDlTERmGF6qukiqkXJfkq1dDO4jaSpZN-thvwwxssoX0ZEwNOvogdpvkZYuLtKz2U4SaC8kgfplXUU0NNN9cVaUJKDffE_HrOoJhypEswVyAeIi851KpthpHhfs1Kw5vuER_c5nqSZ_TwvtEUUQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم مبعوث کاشمر در سنگر خیابان با ۲۰۰ شب مداومت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/462550" target="_blank">📅 23:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462549">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c378acf0.mp4?token=jAwPpnfrBnqhSjbM16JMbN9eE-sGwE8523_m4O97ww2UqJN24oYSiVFNPejeARnEwdV1pUlZaAcQPthAykYbJj0u8A3P0vV2WCPFuLeuDT8fMM-nZRCl8J6hRhSDHKb3FnHNeKXsb9mPsHFPyAiuX6Gyd-Vd0_gxHlUNu_qdPMsJTkSrHOLqjceL_V_bvUIQeP6RXaHAooXH5mhOuwBXmHmCQqaUI5D3Qu-HOqSGPcHZGaP_XvT7UqIuR-P9uk8-CcujF97xhj-ZsQQy2PZxnfBQ3p-DMOrrxt9U9TFGbsAJYO3dCLTOoX7Yk_t_hoIcZ14-B2v3sL8LOCWZ8uqsMHk8yOynhkYECKbYrcxV9N0oshThWO_4AQFocCyLURRv4Z4lLL57D-5Lds6Jsdi2Bz4r3viT0yNBJzVU2DRwfbmpnoa3oKGQHCtGXm8N5Z-jPgo6IekUmldD3q1AXorLlaPxai6u83z_Mq5AxuSmDrjdeYVvWfpaZy3e7tiJRVy69Lb97kY5L8vD8mxHYOyuNVat8JwYAvg0jV8EmyVfjIYwNOxqQeprPM7JCS3RZ3eAcEdn-lsBxLoCWpDQN2ApPJ5A4Rtm--tRMKZjL-W7ugqq1NN7dtXOytnCORRGoMQi6zCTzyDyEa_DhRQziXg-MX3k2nqeekedDWMcD0ErUoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c378acf0.mp4?token=jAwPpnfrBnqhSjbM16JMbN9eE-sGwE8523_m4O97ww2UqJN24oYSiVFNPejeARnEwdV1pUlZaAcQPthAykYbJj0u8A3P0vV2WCPFuLeuDT8fMM-nZRCl8J6hRhSDHKb3FnHNeKXsb9mPsHFPyAiuX6Gyd-Vd0_gxHlUNu_qdPMsJTkSrHOLqjceL_V_bvUIQeP6RXaHAooXH5mhOuwBXmHmCQqaUI5D3Qu-HOqSGPcHZGaP_XvT7UqIuR-P9uk8-CcujF97xhj-ZsQQy2PZxnfBQ3p-DMOrrxt9U9TFGbsAJYO3dCLTOoX7Yk_t_hoIcZ14-B2v3sL8LOCWZ8uqsMHk8yOynhkYECKbYrcxV9N0oshThWO_4AQFocCyLURRv4Z4lLL57D-5Lds6Jsdi2Bz4r3viT0yNBJzVU2DRwfbmpnoa3oKGQHCtGXm8N5Z-jPgo6IekUmldD3q1AXorLlaPxai6u83z_Mq5AxuSmDrjdeYVvWfpaZy3e7tiJRVy69Lb97kY5L8vD8mxHYOyuNVat8JwYAvg0jV8EmyVfjIYwNOxqQeprPM7JCS3RZ3eAcEdn-lsBxLoCWpDQN2ApPJ5A4Rtm--tRMKZjL-W7ugqq1NN7dtXOytnCORRGoMQi6zCTzyDyEa_DhRQziXg-MX3k2nqeekedDWMcD0ErUoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پای حرف مردمی که بعد از ۲۰۰ شب میدان‌داری خسته نشده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462549" target="_blank">📅 22:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462548">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9e37f33a.mp4?token=Hwbpl3NqNKSXwGBVGHspaNnJHsXw682tmhSrBRPPn8Yq36wMC5wx1KwJ5BA8_BmpudTHREqa-jWfqFPDbMBp83DXZ7huIlVcgcWx6lY-n1VnbL2eJctwQNLZK03zpVVbNM1lvFqDIT_1E5ZnJuPZTq-SIvv75-M6faIAVedVpeQEI-XcA7FvRNS4F1YlDj7VBkGJ5cK5pHjMc5DmvrdiPzqlTfbFCo8YJufDI_AnriMb5j23BEwmcKzr3aeisqRW0749FQau6q-QDiWX1lahZvc0qGTF-Rie__wAfZsSzDo_uT1Xd_pMiSoSP2nsXYCAD1QiHtXFwFfKfTlWrn6UaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9e37f33a.mp4?token=Hwbpl3NqNKSXwGBVGHspaNnJHsXw682tmhSrBRPPn8Yq36wMC5wx1KwJ5BA8_BmpudTHREqa-jWfqFPDbMBp83DXZ7huIlVcgcWx6lY-n1VnbL2eJctwQNLZK03zpVVbNM1lvFqDIT_1E5ZnJuPZTq-SIvv75-M6faIAVedVpeQEI-XcA7FvRNS4F1YlDj7VBkGJ5cK5pHjMc5DmvrdiPzqlTfbFCo8YJufDI_AnriMb5j23BEwmcKzr3aeisqRW0749FQau6q-QDiWX1lahZvc0qGTF-Rie__wAfZsSzDo_uT1Xd_pMiSoSP2nsXYCAD1QiHtXFwFfKfTlWrn6UaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۰ شب میدان‌داری
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462548" target="_blank">📅 22:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462547">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkrxQdQqKaDyusJ6ftS99MupEm3f5tfBIQXF592jn2CoH406WKTPegdM3S1PwfjwCbTP-MHTRtuw7Axj3pCsW2pwtg1qCy4KQJCkV4e28n3JhHJFLMNfzkyDy6YpO2rDs_eItvy43FkmVlRQPDOsgLUP7zswNbram_y_D6yGSM-x9li9QE-eQtFffRd59K7YTUn53eGi8KlYTUPAL4zKrhsNVo9kFucecQDfzPem_cO02e02u2VmME7Txdhb52mn9Yevh2gnH5j8JJBXIL0Sk4ppE0AyNrMLDrnJFMrnCrXFTD_pjAN_2qpHtinWntyZ0Hal1ojLQRSMuHG5sUjNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹ خبر خوب از جای‌جای ایران
🔹
«بستۀ خبر خوب» امروز را از گوشه‌وکنار ایران تقدیم می‌کنیم؛ روایتی از تلاش و امید در سراسر ایران.  تخلیه و بارگیری کالا در بندر سیریک ۴ برابر و تردد شناورها ۲.۵ برابر بیشتر از پارسال شد
🔸
بندر سیریک هرمزگان از ابتدای سال جاری تاکنون…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462547" target="_blank">📅 22:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462546">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc463aaa3b.mp4?token=g6bLgvTUnphhq0elqtpK6KY95EVf9KtDwD4cJsiOUK3AFGCJqAcSFe_DrZbCK-dAuGWn8qpBig90IhveBe7yWDTJtTbAlFyLut5UOeE5BrBItcQzFZUIBAdPZ9dADWrjLibjHAGlXPIVWewE3z9-QZT2DRYaweZCsxsVGBgxkDvG6cj1wyV9K_Mf1iT8JzmIpXyOLlRGMHpTKeNmvm_TEWNWK4ghPJ9o4s5IsqZ4EUwSR_87NR8cU9zGEOEkDIFowislmW0_GvAafPF3JkQtl0CmM18q49mQJd8UIJ70FeJjxcZ1qsJtcdYnrY9ymBWMHsKftrcOxFLsUFQDZHl_OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc463aaa3b.mp4?token=g6bLgvTUnphhq0elqtpK6KY95EVf9KtDwD4cJsiOUK3AFGCJqAcSFe_DrZbCK-dAuGWn8qpBig90IhveBe7yWDTJtTbAlFyLut5UOeE5BrBItcQzFZUIBAdPZ9dADWrjLibjHAGlXPIVWewE3z9-QZT2DRYaweZCsxsVGBgxkDvG6cj1wyV9K_Mf1iT8JzmIpXyOLlRGMHpTKeNmvm_TEWNWK4ghPJ9o4s5IsqZ4EUwSR_87NR8cU9zGEOEkDIFowislmW0_GvAafPF3JkQtl0CmM18q49mQJd8UIJ70FeJjxcZ1qsJtcdYnrY9ymBWMHsKftrcOxFLsUFQDZHl_OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور زنان مجاهد شهرکرد در شب ۲۰۰ تجمعات خیابانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/462546" target="_blank">📅 22:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462545">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acec655234.mp4?token=frtg-TzprxkZGAx1mPEVgsO2kCU4Z8MjHoDLtR8SfnNxk9bl0KxHH9nM0B32oB6kEjvRoXwxanEG2pl1WB63GHuMTcIViNPv8VBYuwkX1ctvO6wkVT5YM8YuVQ4iiFgo1BR1_mZJ5fI7TLWjd6HiI8rfO8dupuXyu9d89RNlkv_cmwESMjgqjJlVLoKj8PqJGjdBxiglg8Oz3oZdaGifW04sB_v1P-rAfRiT_umt1NUniyYRw-PnxOnWx3nIH0uwHGTEdgThdjVbadeA_SxCPBMBT2f-HYZw82wtTOV29u2OhJaRNlPjdBOjDYzUf0xoRKH_ZFcmJtYE-y4QaMG5lnh1MxWLN6ewFmb7IGQF-NAa-PaNIRyoW-LfRtwRm_7lYbwCJ0y4zK0alujnyDyYwF2kydVaXfuT6g-9bgAvqy_go4JGkQcWmb4yQD01XlkUVduQbVpxGEZAT1nXzacMOFNzlS0jfR4yRa1AixFtFcI5tdGRB426hzFHW4-gelzKImcI4I9IR9yra91Mn49u2sCW77D7yiyKXvRySIB7kF1d1WcZm42LKU5hEhGEXqsHJS7F4xmhjRnHcgQxx-IzgX4yfBD7-VuIYN1fFyZHVyHsx3314Ks-BseD6JpqWpxwKTUtGGFr4ISi9xEbIn2vcREwOAKoU-3LwBnuM0oLJhI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acec655234.mp4?token=frtg-TzprxkZGAx1mPEVgsO2kCU4Z8MjHoDLtR8SfnNxk9bl0KxHH9nM0B32oB6kEjvRoXwxanEG2pl1WB63GHuMTcIViNPv8VBYuwkX1ctvO6wkVT5YM8YuVQ4iiFgo1BR1_mZJ5fI7TLWjd6HiI8rfO8dupuXyu9d89RNlkv_cmwESMjgqjJlVLoKj8PqJGjdBxiglg8Oz3oZdaGifW04sB_v1P-rAfRiT_umt1NUniyYRw-PnxOnWx3nIH0uwHGTEdgThdjVbadeA_SxCPBMBT2f-HYZw82wtTOV29u2OhJaRNlPjdBOjDYzUf0xoRKH_ZFcmJtYE-y4QaMG5lnh1MxWLN6ewFmb7IGQF-NAa-PaNIRyoW-LfRtwRm_7lYbwCJ0y4zK0alujnyDyYwF2kydVaXfuT6g-9bgAvqy_go4JGkQcWmb4yQD01XlkUVduQbVpxGEZAT1nXzacMOFNzlS0jfR4yRa1AixFtFcI5tdGRB426hzFHW4-gelzKImcI4I9IR9yra91Mn49u2sCW77D7yiyKXvRySIB7kF1d1WcZm42LKU5hEhGEXqsHJS7F4xmhjRnHcgQxx-IzgX4yfBD7-VuIYN1fFyZHVyHsx3314Ks-BseD6JpqWpxwKTUtGGFr4ISi9xEbIn2vcREwOAKoU-3LwBnuM0oLJhI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم خمین ۲۰۰ شب پای عهدی که با رهبرشان بستند ماندند
🙍‍♂️
ارسالی مخاطبان به
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/462545" target="_blank">📅 22:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462544">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
لطفاً صدای ما
بیماران سرطانی
باشید. هزینۀ داروهای مورد نیاز بیمار سرطانی برای هر دوره شیمی‌درمانی به حدود ۱۰۰ میلیون تومان رسیده است. با حذف یا کاهش حمایت‌های دارویی،  خانواده‌ای که درآمد متوسط یا پایینی دارد واقعاً چگونه باید این هزینه را تأمین کند؟ خانه و طلا بفروشد، قرض کند یا درمان عزیزش را نیمه‌کاره رها کند؟
دارو کالای لوکس نیست
و درمان سرطان انتخابی نیست. خواهشمندیم مسئولان برای
حمایت واقعی از بیماران صعب‌العلاج
و جلوگیری از توقف درمان به دلیل مشکلات مالی، اقدام فوری کنند.
🔹
دولت اعلام کرده به خودروهای بالای ۲۰ سال بنزین سهمیه‌ای نمی‌دهد. طرح خودرو فرسوده هم که تعیین تکلیف نمی‌شود. خواهشمندم در این طرح بازنگری شود.
🔹
هفتۀ گذشته با کارت شخصی،
سهمیه بنزین
۱۵۰۰ تومانی‌ام را مصرف کردم و تمام شد. امروز برای استفاده از سهمیۀ ۵۰ لیتری بنزین ۳۰۰۰ تومانی مراجعه کردم، اما با کمال تعجب دیدم فقط ۱۳ لیتر در کارت نمایش داده می‌شود و ۳۷ لیتر از سهمیه‌ام مفقود شده است. این ۳۷ لیتر سهمیه
متعلق به مردم و حق‌الناس
است. چه کسی یا چه کسانی مسئول این اتفاق هستند؟
🔹
در منطقه محروم
کنارک
،
پمپ‌بنزین اصلی شهر
بدون اعلام دلیل
تعطیل شده
و این موضوع مشکلات زیادی برای مردم ایجاد کرده است.
🔹
بعد از بیش از ۱۵ سال پس‌انداز، امسال با همسرم یک خودروی صفر خریدیم اما پس از دریافت کارت سوخت متوجه شدیم خودروهای نو شماره از سهمیه بنزین ۱۵۰۰ و ۳۰۰۰ تومانی محروم‌اند و فقط ۱۱۰ لیتر بنزین با نرخ بالاتر دریافت می‌کنند. سؤال ما این است
چرا باید خودروی نو شماره از سهمیه یارانه‌ای محروم باشد؟
بسیاری از ما نه خانه و نه دارایی قابل‌توجهی داریم و خرید یک خودرو به ‌سختی برایمان ممکن شده است.
🔹
لطفاً
تخلفات ایران‌خودرو
را پیگیری کنید. بعد از ۳ ماه از موعد تحویل خودروی ما، امروز از نمایندگی تماس گرفتند و اعلام کردند باید ۴۰ میلیون و ۵۰ هزار تومان بابت اسقاط خودرو پرداخت کنیم؛ درحالی‌که حواله ما مربوط به طرح عادی بوده و
طرح اسقاط برای خودروهای فرسوده
است.
🔹
تأمین اجتماعی
چند سال مبلغ حدود ۷۱۵ هزار تومان به‌عنوان
کمک‌معیشت به بازنشستگان
پرداخت می‌کرد اما امسال اعلام شد با احکام جدید این مبلغ قطع می‌شود. این در حالی است که همین مبلغ در شرایط اقتصادی فعلی، کمک‌خرج بسیاری از بازنشستگان بود. اما عجیب‌تر اینکه در شهریورماه هنگام پرداخت معوقات حقوق فروردین، همان ۷۱۵ هزار تومانی که در فروردین به حساب مستمری‌بگیران واریز شده بود،
از مبلغ معوقات کسر شده است
! اگر پرداخت این مبلغ اشتباه بوده، چرا پس از شش ماه از حقوق بازنشستگان کم می‌شود؟
🔹
ما جمعی از
زائران ثبت‌نام‌شده حج تمتع ۱۴۰۵
، نسبت به
ن
حوۀ تعیین تکلیف هزینه‌های پرداختی و عدم اعزام خود اعتراض داریم. هزینه حج بر مبنای حدود ۴۰۰۰ دلار محاسبه و در آبان و آذر ۱۴۰۴، زمانی که نرخ ارز کمتر از ۸۰ هزار تومان بود، از زائران دریافت شد. پس از کاهش ظرفیت اعزام بسیاری از زائران بدون آنکه از سفر انصراف داده باشند از اعزام بازماندند و وجوه آنان نیز مدت‌ها مسترد نشد. مطالبه ما روشن است زائرانی که به دلیل محدودیت ظرفیت اعزام نشده‌اند باید
بدون پرداخت هزینه اضافی در اولویت حج ۱۴۰۶ قرار گیرند
. در صورت عدم امکان اعزام نیز استرداد وجه باید با لحاظ ارزش واقعی مبلغ پرداختی و مبنای ۴۰۰۰ دلار با نرخ روز انجام شود تا کاهش ارزش پول موجب تضییع حقوق زائران نشود.
🔹
لطفاً مسئولان فکری به حال
رانندگان استیجاری شهرداری‌ها
کنند. نه قرارداد درست‌وحسابی داریم، نه حقوق کافی، بیمه، عیدی، پاداش، سنوات و
امنیت شغلی
. با هزینه‌های سرسام‌آور استهلاک و قیمت خودرو، ادامه کار برای ما بسیار دشوار شده است.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/462544" target="_blank">📅 22:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462543">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSin7Qg5-o8HIKj4zpEvNfpQLfGYQRLI_iPaHqEM7-RnEglLPt_WnX1m4g_4Ryhx9W1_epOHzY4WagK2heytotPY1zxfDAoNl80vylyyNWKsVo7932de5aNa3UGPfbjGLNWqA1mNMzNP2HRwFVLEYATLRtxal62oLCoUT7d05I1mWeXomtum4TM6KYmlV5FXiIFL2HkhnW1Lu-1tvpB2w3FBgoBwPBytBhNR3mGmX16rK43Z5haAxsQMTgNFRcqVK_cdfeeBcbwzPgD-J3YJY-J2JqpbgKDbQMCbp_n893YiwD-dtQ5Of18V0fniuFdX8W6nYWF6HdFSMNOh0PcCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامۀ تجاوز رژیم صهیونیستی به جنوب لبنان
🔹
ارتش اشغالگر رژیم صهیونیستی در ساعات گذشته منطقه‌ای میان شهرهای زوطر شرقی و میفدون، نقطه‌ای در اطراف بیت یاحون، شهر المنصوری و منطقۀ حدات را بمباران کرد. همچنین توپخانۀ اسرائیل دره زبقین را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/462543" target="_blank">📅 22:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462542">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8032dc77.mp4?token=CUMv6rmX1ev4FfwFPRWIa8h_TUSnoajgFiwFHcODXLMzJCmYdMPEq7lVhXdbE12622y2WZxGx8FcBdRzSrZB6pi48Nylm9AQwzt6LFiJ167jecYwU4idJNRY3bb3FQvonCrX-qMs8Uof-O6LqV3Vy0xD7zx38QP2dwC-3Ga60M_FLECu-ztt480caYlphNry9dtIe03NqEJLni3Ljg93u7-C7LiqPoZP6_v9Sz0hSVhd4RIh19DqCVI5fox7lnl_x5pCzIDbZOqeJKedA1CJgkVp6sGylqZi8Sfp8ZecTBchBYumwEqazIJjsKVgrTl2iXdpXQyWIZG2J6GwDKRsAnuJVmGm50fZvvwWSFx117TDcT24VwJ6ZTgO3hvLlm5OZCF4NIef0mhb3G3DoHpt1R_Y029duPnCoPpBAse5NnVJZuxrlbS9eHqYqNTJbXchGAa28mU1qRoiE4Kd63H8QopzSwtq2R5c4Lrq1LJ4yAhv97HHf_xaeqs41abddxRYt677aFrMfpp3yG2rjOpJ-hVHpT-SC9z4EZDBhqJOV8urY2uOlRmGAX0CHo20NlNoFQJP1MCPF9NmaRVLf_JNoEcGTFdiGhgExh96EBCeJJFPGmBt0hPq75xzwoCXTBjX2RKQCFeS3Dkc7TYUQsUZOqtAmOaU_VNXScOl_fg8u7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8032dc77.mp4?token=CUMv6rmX1ev4FfwFPRWIa8h_TUSnoajgFiwFHcODXLMzJCmYdMPEq7lVhXdbE12622y2WZxGx8FcBdRzSrZB6pi48Nylm9AQwzt6LFiJ167jecYwU4idJNRY3bb3FQvonCrX-qMs8Uof-O6LqV3Vy0xD7zx38QP2dwC-3Ga60M_FLECu-ztt480caYlphNry9dtIe03NqEJLni3Ljg93u7-C7LiqPoZP6_v9Sz0hSVhd4RIh19DqCVI5fox7lnl_x5pCzIDbZOqeJKedA1CJgkVp6sGylqZi8Sfp8ZecTBchBYumwEqazIJjsKVgrTl2iXdpXQyWIZG2J6GwDKRsAnuJVmGm50fZvvwWSFx117TDcT24VwJ6ZTgO3hvLlm5OZCF4NIef0mhb3G3DoHpt1R_Y029duPnCoPpBAse5NnVJZuxrlbS9eHqYqNTJbXchGAa28mU1qRoiE4Kd63H8QopzSwtq2R5c4Lrq1LJ4yAhv97HHf_xaeqs41abddxRYt677aFrMfpp3yG2rjOpJ-hVHpT-SC9z4EZDBhqJOV8urY2uOlRmGAX0CHo20NlNoFQJP1MCPF9NmaRVLf_JNoEcGTFdiGhgExh96EBCeJJFPGmBt0hPq75xzwoCXTBjX2RKQCFeS3Dkc7TYUQsUZOqtAmOaU_VNXScOl_fg8u7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور جان‌فدایان و مردم انقلابی درگز خراسان رضوی در راهپیمایی شب ۲۰۰ تجمعات
🙍‍♂️
ارسالی مخاطبان به
@Fars_ma
@Farsn</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/462542" target="_blank">📅 22:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462541">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697ece007e.mp4?token=E1TC0hiyDCo37-wAdjCW86dzEiOVkvt6-2G6Xg6NEc5-NpUhAfZOmzNgnlikL0AFdTMQtCW4ma2j3Ee6GP9R5h_wcbEC7cfc9815QJ9w8jmTh1CiRkGeYpR2rQEOE6p7yuG_aBosxE-RMCeAQC2ZF1MMmirkvgpZLCq7eWjrwcX29u-2T8ss7fOuHwjKpzScsI8riRhDRCiCiM4APUZPJAPHce9_ucD-bag0YmlV0o5maPsk0vTpd9nsrNiWamtiG-Yf-aChlOIeOZ6wIlxPU6JODKnIGGKLg22cqjQBJmy4WHUNLhITV4bKYuUM-od5Li4NhYzoISiL9a2rFZjnFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697ece007e.mp4?token=E1TC0hiyDCo37-wAdjCW86dzEiOVkvt6-2G6Xg6NEc5-NpUhAfZOmzNgnlikL0AFdTMQtCW4ma2j3Ee6GP9R5h_wcbEC7cfc9815QJ9w8jmTh1CiRkGeYpR2rQEOE6p7yuG_aBosxE-RMCeAQC2ZF1MMmirkvgpZLCq7eWjrwcX29u-2T8ss7fOuHwjKpzScsI8riRhDRCiCiM4APUZPJAPHce9_ucD-bag0YmlV0o5maPsk0vTpd9nsrNiWamtiG-Yf-aChlOIeOZ6wIlxPU6JODKnIGGKLg22cqjQBJmy4WHUNLhITV4bKYuUM-od5Li4NhYzoISiL9a2rFZjnFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان‌های خودرویی مردم کرمانشاه در موج ۲۰۰
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/462541" target="_blank">📅 22:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462540">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba163c954.mp4?token=MEzD9_7m8H7coYyjAgvU2R1cOOz0xPntyPFvos5cKBSWlGiUPCNMly3tKMUJ9KT_QLjgA4AyNNXDJJ0hV1qHw8kjHr95--FfLvmdg2TdemyWAjaWkL5Mi4YCoYjmCbgsCHKv6WH2AIpXwmaUGdQg2c0L1_yKFaep3LPhB2R3KjPlyku1PHm2urqqS2EycdBazT-Hz-rGoAFtQKil71k7f15L_2QVez3mCJ8ejmVNfhQd6qqMbQppv2axZY3hTiGgUsNpg54TZeDxzNiXw5fOlePyS_fIcz21XddF9Wh8wZZhKhbOfFL342RmD8FCttgPtUvTa7m6jtMqokBzhrnk3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba163c954.mp4?token=MEzD9_7m8H7coYyjAgvU2R1cOOz0xPntyPFvos5cKBSWlGiUPCNMly3tKMUJ9KT_QLjgA4AyNNXDJJ0hV1qHw8kjHr95--FfLvmdg2TdemyWAjaWkL5Mi4YCoYjmCbgsCHKv6WH2AIpXwmaUGdQg2c0L1_yKFaep3LPhB2R3KjPlyku1PHm2urqqS2EycdBazT-Hz-rGoAFtQKil71k7f15L_2QVez3mCJ8ejmVNfhQd6qqMbQppv2axZY3hTiGgUsNpg54TZeDxzNiXw5fOlePyS_fIcz21XddF9Wh8wZZhKhbOfFL342RmD8FCttgPtUvTa7m6jtMqokBzhrnk3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رئیس‌جمهور در امور زنان: سن طلایی بارداری و اشتغال یکی شده است
🔹
امروز به‌دلیل شرایط اقتصادی زنان ترجیح می‌دهند در کنار مردان کار کنند.
🔹
سن مناسب ورود به بازار کار و سن مناسب برای فرزندآوری یکی شده اگر از مادران حمایت نشود، یکی از این ۲ فدا می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/462540" target="_blank">📅 22:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462539">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8198d3da4.mov?token=LloZS9nDisx6c2TUPUYXHuVaOMycof_xprRj6OrWRr5PhT1iJSw8Quu8VoUzb9nD0wLYVaI_3z6OhLILtBF2gdSM84Gm-_RQbu_invPW4ltScJCoJXdqLj1M-Q2s5QH21nWowNoPiaiqW3xYbOJBMhSnOzdnDBm0EgjbGkUncqLnaA6LHAhpz7WiNw9psxEyD9HOfOhAGPgmahi7agRnBts6wD4CrOmVk1opw_aBb0q7EHeL5rttcXz4D6oFgeQH9yiHHWGkiTTWVnsuetNcVaZ1SCgX_DKYV2xc1Vy7S-tU0kI1MlYpWe0_0puqvjwfZe1PeCYCMWQlrFH0UeAkCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8198d3da4.mov?token=LloZS9nDisx6c2TUPUYXHuVaOMycof_xprRj6OrWRr5PhT1iJSw8Quu8VoUzb9nD0wLYVaI_3z6OhLILtBF2gdSM84Gm-_RQbu_invPW4ltScJCoJXdqLj1M-Q2s5QH21nWowNoPiaiqW3xYbOJBMhSnOzdnDBm0EgjbGkUncqLnaA6LHAhpz7WiNw9psxEyD9HOfOhAGPgmahi7agRnBts6wD4CrOmVk1opw_aBb0q7EHeL5rttcXz4D6oFgeQH9yiHHWGkiTTWVnsuetNcVaZ1SCgX_DKYV2xc1Vy7S-tU0kI1MlYpWe0_0puqvjwfZe1PeCYCMWQlrFH0UeAkCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۰ شب گذشت؛ اجتماع شبانۀ مردم جنوب شرق تهران ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/462539" target="_blank">📅 22:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462538">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021dfa4acd.mp4?token=p4py4Yr-yfEs8OKCMZJXo-Jr3PE67WwzxImRwPwrcBYZu24TejM2-xHdhU33bQxLtnONjosZS_ZkxUAg_XGlVEaL0stx0VGbmAQeH6FsnnfngizeEUYg7qIVlSQU0Ai7St3hFknQhSVNmBvD7N77rb-ZC0_zZoLFRoPRFcyGRwwTWmicDrI8u-HFe3O94jfwmzghR7OYdVfpPGOnKEkJ23mKAN9eOgS0Aqk7CohDEHZuewS28JSuh0hL5s_X1LXH3My8ed_h1vu98Q-RAY-i5i4cUDHym4ssyefSkgmg4TqQMpPLJTZC02_LJmgKhgYHr8o7BWsH4zFXSxn8JqCIKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021dfa4acd.mp4?token=p4py4Yr-yfEs8OKCMZJXo-Jr3PE67WwzxImRwPwrcBYZu24TejM2-xHdhU33bQxLtnONjosZS_ZkxUAg_XGlVEaL0stx0VGbmAQeH6FsnnfngizeEUYg7qIVlSQU0Ai7St3hFknQhSVNmBvD7N77rb-ZC0_zZoLFRoPRFcyGRwwTWmicDrI8u-HFe3O94jfwmzghR7OYdVfpPGOnKEkJ23mKAN9eOgS0Aqk7CohDEHZuewS28JSuh0hL5s_X1LXH3My8ed_h1vu98Q-RAY-i5i4cUDHym4ssyefSkgmg4TqQMpPLJTZC02_LJmgKhgYHr8o7BWsH4zFXSxn8JqCIKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از تندیس سردار شهید حاجی‌زاده در میدان ابوذر
تهران
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/462538" target="_blank">📅 22:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462537">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حملۀ رژیم صهیونیستی به حومۀ دمشق
🔹
ارتش اشغالگر اسرائیل با ۴ گلوله توپ شهر بیت‌جن در حومۀ غربی دمشق را مورد حمله قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/462537" target="_blank">📅 22:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462536">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9585b17f3e.mp4?token=VDHUzvW6XogrxRfejmFxUr6zPlAnco9a3YQZK_xmmVW7JOB0KpnGIXKE2P1S8G0S1ey5_lGjqfr7Y8F3OFu3ndx1AF2JWWolcRLB3MkutmwemX-T54R15EIcZ3pSRG86IN8i3ACQLfLFmAm0bhq_awaSTDkeLjfbL-eXoD38H6KQ5Ipjv1VPxo9pBeuEa089JkYIDbGcofdvc1I_okjT5w-CnhPLgalcb0SEFT6WaDTq0um9Y5pidwYIvr250I_NRs4h_luwMZ0pU0QnKx20j4K0iAUSwmKXRFYEqvJtMxoh3OZ12N6DfxkMMNtcuw_TalndZymc1Ph-5RnPlHt4Dx_0Tb788K8CpX4YqsGY7XOfzqC47xfIk1jZV-HkLK1lIhgq2KTfrgR1D9KSEPmiOFXF18vVU7JZmnNtBYGXYL67KD6WTRDbZvSeQwUh4vNfXHZ1Q2D3VHSg78HPPuOz-QOeiXAFE90ShzuMrFsy5xezHD8jBgh8cZsK6imzDsfvE6cG572_8aBPhX3LZxqIxfAodHNuUgeB619xz56NZFCE51TBU-GhI8-H_PBRxuwLlmKmYz_U6E5Cl4BUjfAxpGtTz6zOnpX2j-RxXU57Jbdpixaq9ogafGMxhhHaiiJX1gjAWcmVGi3oEXG4bvyyDyGj96qG5qBDvP4BN2-vqAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9585b17f3e.mp4?token=VDHUzvW6XogrxRfejmFxUr6zPlAnco9a3YQZK_xmmVW7JOB0KpnGIXKE2P1S8G0S1ey5_lGjqfr7Y8F3OFu3ndx1AF2JWWolcRLB3MkutmwemX-T54R15EIcZ3pSRG86IN8i3ACQLfLFmAm0bhq_awaSTDkeLjfbL-eXoD38H6KQ5Ipjv1VPxo9pBeuEa089JkYIDbGcofdvc1I_okjT5w-CnhPLgalcb0SEFT6WaDTq0um9Y5pidwYIvr250I_NRs4h_luwMZ0pU0QnKx20j4K0iAUSwmKXRFYEqvJtMxoh3OZ12N6DfxkMMNtcuw_TalndZymc1Ph-5RnPlHt4Dx_0Tb788K8CpX4YqsGY7XOfzqC47xfIk1jZV-HkLK1lIhgq2KTfrgR1D9KSEPmiOFXF18vVU7JZmnNtBYGXYL67KD6WTRDbZvSeQwUh4vNfXHZ1Q2D3VHSg78HPPuOz-QOeiXAFE90ShzuMrFsy5xezHD8jBgh8cZsK6imzDsfvE6cG572_8aBPhX3LZxqIxfAodHNuUgeB619xz56NZFCE51TBU-GhI8-H_PBRxuwLlmKmYz_U6E5Cl4BUjfAxpGtTz6zOnpX2j-RxXU57Jbdpixaq9ogafGMxhhHaiiJX1gjAWcmVGi3oEXG4bvyyDyGj96qG5qBDvP4BN2-vqAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
جان تازه در رگ‌های فلک‌الدین خرم‌آباد
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/462536" target="_blank">📅 22:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462535">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d53337f51.mp4?token=ZalulPoIs4FEZS98ScDl_w4r2x8vs2RJV23Om5LAfvdeWlsztEg2-YCvfmaWBnGeI7psbRixG2gEl7yInaYnSXJnm3KOu0hUJ27yhn-FJXLd5HlBOYsgXwtHPgD2dzM4yaXN1gNWW78yhfUFcgyF5ZqljnBmG7_9a412aEZ17FJeV_6CyY7oFnvY5YfbJoTILVNfOzkjZ_0wrhIhf0Uj0Shi6IC17n85ZrPrxwVWiHYvn9h36RONCbkVXBrWnpaxVsoguozbV7zSWbP867Mo6usxXeik01va3ao3nFDsgMY8Vxe5R6ZL142kn3CYbXeJtyRo-srk8Tf32giJObWbUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d53337f51.mp4?token=ZalulPoIs4FEZS98ScDl_w4r2x8vs2RJV23Om5LAfvdeWlsztEg2-YCvfmaWBnGeI7psbRixG2gEl7yInaYnSXJnm3KOu0hUJ27yhn-FJXLd5HlBOYsgXwtHPgD2dzM4yaXN1gNWW78yhfUFcgyF5ZqljnBmG7_9a412aEZ17FJeV_6CyY7oFnvY5YfbJoTILVNfOzkjZ_0wrhIhf0Uj0Shi6IC17n85ZrPrxwVWiHYvn9h36RONCbkVXBrWnpaxVsoguozbV7zSWbP867Mo6usxXeik01va3ao3nFDsgMY8Vxe5R6ZL142kn3CYbXeJtyRo-srk8Tf32giJObWbUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۰ شب حضور مردم؛ میادینی که هر شب شاهد یک روایت تازه بودند
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/462535" target="_blank">📅 22:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462534">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9322fee6.mp4?token=Gtis9Ahf1GO5-v1SqVtWtJpovfOkmk-lUoNNp2TZ1sZdAxx0fN6jehgkv-6_qbMTOwCbDS6TD3cjTGSBGBF2WBsGhSxlW-oFkkTBxYd7vRYTxI2nPnbM2SYnroQYwBw_ehtjAx3dfAxll3QeZj781OIXtslHe6tfjOvVi2cBtVbHJF9nODSxw0kfAN_X5c_MMlfmsP35P2kI4FCyssW2bKxsJB-Z6FtmTCOPr27v8KJqrShtjTX55ZiM3RB3M0LK28rdu78FX2NStKy7V4FyR5F_RI_393JIr3eZ3s8f-Pg78jZ0es7c8Xxc4wYSR9uVlAoYfRrenxh8IK_tAINUzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9322fee6.mp4?token=Gtis9Ahf1GO5-v1SqVtWtJpovfOkmk-lUoNNp2TZ1sZdAxx0fN6jehgkv-6_qbMTOwCbDS6TD3cjTGSBGBF2WBsGhSxlW-oFkkTBxYd7vRYTxI2nPnbM2SYnroQYwBw_ehtjAx3dfAxll3QeZj781OIXtslHe6tfjOvVi2cBtVbHJF9nODSxw0kfAN_X5c_MMlfmsP35P2kI4FCyssW2bKxsJB-Z6FtmTCOPr27v8KJqrShtjTX55ZiM3RB3M0LK28rdu78FX2NStKy7V4FyR5F_RI_393JIr3eZ3s8f-Pg78jZ0es7c8Xxc4wYSR9uVlAoYfRrenxh8IK_tAINUzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از تنگه‌های راهبردی تا بازارهای جهانی
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/462534" target="_blank">📅 21:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462533">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0z2qWEUPXPQs-cfBt_YKUVZ9PVakNNgaAGxLayogCxiwF_UxBIQveoGlwnLiglwck05I2jYW4RPquJC0_t89mpWMkOCFHWnsZhHkX9v6BkFSKhvkwpugxKSracq66-EWOOruv81uP5tnLuvCMeOF73bqUWcSUekK_gtVOYjRNNUubZE32XoW1xvyJRb7L_s_DLS8hYhkROsJz4NRvKpe8ApK0mytIJ4T7Dam0DsHt8d-TaBytkahJ2Vo__xVBAd0lv1zKw3AW06LvF_VIu65XpZCrwTsa0L1Xvwicp8AKvJqSN4lrdZ663-Albysh_7b6YbnAqsr5r2Qo9hgRzAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای دروغ سعودی‌ها؛ سناریوی ساختگی علیه مکه شکست خورد
🔹
«ادی کوهن» روزنامه‌نگار و تحلیلگر صهیونیست به نقل از منبع اطلاعاتی غربی فاش کرد که حکومت آل‌سعود یک پهپاد چینی را با هدف جا زدن آن به عنوان پهپاد یمنی در آسمان مکه مکرمه به پرواز درآورده و سپس آن را به قصد جلب محکومیت از سوی کشورهای اسلامی و اعطای بُعد دینی به جنگ علیه انصارالله یمن ساقط کرده است.
🔹
کوهن افزود سعودی‌ها به دنبال کشاندن پای کشورهای اسلامی به‌ ویژه پاکستان و ترکیه به جنگ علیه یمن هستند به خصوص پس از آنکه آنکارا و اسلام‌آباد پیمان مکه را نقض کرده و ریاض را تنها گذاشتند.
🔹
در پی این ادعای کذب سعودی‌ها چندین کشور عربی همسو با ریاض نظیر بحرین، دولت لبنان و مصر در اقدامی هماهنگ، حمله پهپادی به مکه را محکوم کردند.
🔹
در همین ارتباط، محمد الفرح، عضو دفتر سیاسی جنبش انصارالله یمن تصریح کرد: یاوه‌گویی‌ها درباره هدف قرار دادن مکه از سوی یمن، کذب محض است، ما از کسانی که پرده کعبه را به جفری اپستین هدیه دادند، دلسوزتر نسبت به مقدسات هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/462533" target="_blank">📅 21:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462532">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bcbf379b.mp4?token=CT4xNZhZUXu4D8gcuk-n2G6YJQVH66U_RZ6FJ92pPLUn7zL1BX1pb5H827i4p-rdB7tKy0tgL6_pY1AijmhhGd8Qoexb6Y01be2ARmMG7izET60VqoqZsj8M-3sjEA5ufBKGfhDwfw4NQaiUUFoqxoA4EMWaF6GpU91YcNMN7hYgV6Gkf0Zyjej-hYri8PWBCGvJadtpmFex6nu2W49T03RE_Tj6dP1WUhk6qOdm6WoVTprxsVe9PRqX_NE24GP00FbZTn_aMJRnuepjmEIGegyB9AAqB4j7GS_M2E8Hjwyt-KpzfNLAxxbI4PCtxkfJZLqYITtjRlci3ZxbZUToobocGnDOCI60pMOA7Zppif24e3lozz2xzx6hHutLz9mPTM6BrHEQgYdO_P_UvD4qx0rIO54IH1JvMwUQS0doXmwSAJAUxKsN6mexQdAGoaBb-YCnN1RP9ZyBLQ42KhyygUjFhiLDGKgT83kDyYK8FBCPEMAVo0mTVtiqvL_fLbM1NKHLk83WSLd2SAfOg1NbffEuOlapETGspL1ZQDi3rrbuXmiVzkJXhvIfaB9lYjuGVwAuGn68skIVIlnXdsv5v_qjyfTNN946sh5aq0gvWB66K6FStfRfkbXaBVr6vO6WZpifuOpEl-KuB_4lw7QYKjpZcq0WipGk4GjZp3z65sY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bcbf379b.mp4?token=CT4xNZhZUXu4D8gcuk-n2G6YJQVH66U_RZ6FJ92pPLUn7zL1BX1pb5H827i4p-rdB7tKy0tgL6_pY1AijmhhGd8Qoexb6Y01be2ARmMG7izET60VqoqZsj8M-3sjEA5ufBKGfhDwfw4NQaiUUFoqxoA4EMWaF6GpU91YcNMN7hYgV6Gkf0Zyjej-hYri8PWBCGvJadtpmFex6nu2W49T03RE_Tj6dP1WUhk6qOdm6WoVTprxsVe9PRqX_NE24GP00FbZTn_aMJRnuepjmEIGegyB9AAqB4j7GS_M2E8Hjwyt-KpzfNLAxxbI4PCtxkfJZLqYITtjRlci3ZxbZUToobocGnDOCI60pMOA7Zppif24e3lozz2xzx6hHutLz9mPTM6BrHEQgYdO_P_UvD4qx0rIO54IH1JvMwUQS0doXmwSAJAUxKsN6mexQdAGoaBb-YCnN1RP9ZyBLQ42KhyygUjFhiLDGKgT83kDyYK8FBCPEMAVo0mTVtiqvL_fLbM1NKHLk83WSLd2SAfOg1NbffEuOlapETGspL1ZQDi3rrbuXmiVzkJXhvIfaB9lYjuGVwAuGn68skIVIlnXdsv5v_qjyfTNN946sh5aq0gvWB66K6FStfRfkbXaBVr6vO6WZpifuOpEl-KuB_4lw7QYKjpZcq0WipGk4GjZp3z65sY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۰ شب؛ مردم اهواز میدان را زنده نگه داشتند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/462532" target="_blank">📅 21:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462531">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d17ef81a.mp4?token=fMm1WKWepBlVxiaDycEpeMs_8o297-NW7S6ZwssfCN0VRCgqK3oQb09j3WxqGMmSKF6hdcOiWTOX_GdVfltGfR3xJgApywbs0D478Ng-4bWhx4oSc0D4aN_PrjPMlGlHTx8dEsXgpRSSl0f30qSbfW5QYL1IIdHh7O-Qzxt3ldxx0c85KaqsCcVClpdrTUa1Nh77voE5M9H4kD4ZoJhEtMyzGJO9aqVGTD7UtXpj_k0NnEqDq49S_w_qZ3KMvXFiZ9W8mxhT0S_CKLC5GzSvJ9XpSHUvCNe4c_8azCKYua99mD4BFZFb22FWggDOF1qCxZ7tCWz_kJ99eGQdkw3To5v-ms8TPKXB0tEBiTQZoT84NNbKVSHOQXcKz0jUTjnb29omR-NmG-8wxTb74RLPZbHdl-RW4DOSZ1nzPp9IUCU85NhOeJvt8ZCzhfaZIwId0yvOUlH-yqFQFHjXuESEH3Spdnqvwpb1FclKmpWNv4lmoOKVqgs6SpFPJJrLrBn6ts2HqMAbnMdx34dIoBYD4fop04ML_TgQcjOQm9OdxxaTF7psNcO12be_9rnE4faPl7JeNMWD3iZ7Seytwkez3C7Fuiusx5J_T6Ds-YhIVMiY5EH8Hex3BRhp9y1zbpNyQrY5wtgK-iEfOY3o58xMpfJeDoMDZ8U6MorWAYBnhFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d17ef81a.mp4?token=fMm1WKWepBlVxiaDycEpeMs_8o297-NW7S6ZwssfCN0VRCgqK3oQb09j3WxqGMmSKF6hdcOiWTOX_GdVfltGfR3xJgApywbs0D478Ng-4bWhx4oSc0D4aN_PrjPMlGlHTx8dEsXgpRSSl0f30qSbfW5QYL1IIdHh7O-Qzxt3ldxx0c85KaqsCcVClpdrTUa1Nh77voE5M9H4kD4ZoJhEtMyzGJO9aqVGTD7UtXpj_k0NnEqDq49S_w_qZ3KMvXFiZ9W8mxhT0S_CKLC5GzSvJ9XpSHUvCNe4c_8azCKYua99mD4BFZFb22FWggDOF1qCxZ7tCWz_kJ99eGQdkw3To5v-ms8TPKXB0tEBiTQZoT84NNbKVSHOQXcKz0jUTjnb29omR-NmG-8wxTb74RLPZbHdl-RW4DOSZ1nzPp9IUCU85NhOeJvt8ZCzhfaZIwId0yvOUlH-yqFQFHjXuESEH3Spdnqvwpb1FclKmpWNv4lmoOKVqgs6SpFPJJrLrBn6ts2HqMAbnMdx34dIoBYD4fop04ML_TgQcjOQm9OdxxaTF7psNcO12be_9rnE4faPl7JeNMWD3iZ7Seytwkez3C7Fuiusx5J_T6Ds-YhIVMiY5EH8Hex3BRhp9y1zbpNyQrY5wtgK-iEfOY3o58xMpfJeDoMDZ8U6MorWAYBnhFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معمای عجیب نفت عراق
🔹
ترامپ چگونه با گروگان‌گرفتن پول نفت عراق، دولت آن را کنترل می‌کند؟
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/462531" target="_blank">📅 21:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462530">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e516ccdc77.mp4?token=o4jqj4uDBuDOQt3JYHfTTbb8M8HysuwkDZtkUEn_afITFAe4adLowM-jK0LBkKdUBYlYwMv6K4OK9IBFh3tFK9gg5YHgUfkSH_360nFcHQRa5rTnLh8LnDSkyXQBH1EwK0Tu57CYZvlviCo_B2ATCPp2optOLB_c-hdwndahN76gKU0g3cRdsUSN7BheN1iTpEDOmZx0_j4AbkLZf5sD2ZEwfUd4Dm7W7j7bodajpciIG9wuf1u8cTl2bDWMHtHReyLI-vOP7wds00s0j43VfnCa1vXmrix-Hk_-9eff0zC0-OCwIsVo5jQjqaqWTb5M9YN9uqJHBjWUcWwKgkIdMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e516ccdc77.mp4?token=o4jqj4uDBuDOQt3JYHfTTbb8M8HysuwkDZtkUEn_afITFAe4adLowM-jK0LBkKdUBYlYwMv6K4OK9IBFh3tFK9gg5YHgUfkSH_360nFcHQRa5rTnLh8LnDSkyXQBH1EwK0Tu57CYZvlviCo_B2ATCPp2optOLB_c-hdwndahN76gKU0g3cRdsUSN7BheN1iTpEDOmZx0_j4AbkLZf5sD2ZEwfUd4Dm7W7j7bodajpciIG9wuf1u8cTl2bDWMHtHReyLI-vOP7wds00s0j43VfnCa1vXmrix-Hk_-9eff0zC0-OCwIsVo5jQjqaqWTb5M9YN9uqJHBjWUcWwKgkIdMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در آژانس بین‌المللی انرژی اتمی چه گذشت؟
🔸
روایت رضا نجفی، نماینده دائم ایران، از رقابت ایران و آمریکا در آژانس و اتفاقی که معادلات رأی‌گیری را تغییر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/462530" target="_blank">📅 21:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462529">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaZgN4XxYXyc3ePPRg_jWdO9w78IgCchFXxpK7b8KVarKCSmheeRboD-etVdDKOCmXEIvYRj9u6Ud2f-grzDWvtwUW6u_iTu3twVmmvpjOo3D7noNAcl63g_IWsEjlC0UQg1qVQDRNCJSk3TjrisOUuSJ0euWY_zmQXQYy5dwNdP2h7SUc0gpL29vexooqavR2QyuMwbkPwgQs5IyFYWydXzsaf5hh4Ed4S9nPn0DTKGUs8yqx4s09DsDByTaBFx909fpR4QNiSeY1zQkHZ2E1Z9eaK47sT7m_3V5c5IzOAGiPYgmbludUOB7db3ZIT_kU4ncc_G9OQjS4HLVL19Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس به تاسیس «تیم ب» در لیگ یک نزدیک شد
⚽️
پیگیری‌های نشان می‌دهد مسئولان پرسپولیس با باشگاه بعثت کرمانشاه به توافقات خوبی رسیده‌اند و اگر اتفاق خاصی رخ ندهد، پرسپولیس با خرید امتیاز این باشگاه در مسابقات لیگ دسته اول شرکت خواهد کرد.
⚽️
باتوجه‌به فرصت…</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/462529" target="_blank">📅 21:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462528">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af5db818dd.mp4?token=PaB0Ik9GT67fRIH-G6I64qn2Suhic-bEKyDdaUvFEejNH251Ij9T10HHnKJtnnte-2BO5wr5DC8jxb1gbuzwLgI5BbKJ8V4M4Y7e1EKv6zIhHRvg66mKS8MIwj531xLIujooWlfWhVke5Sf8uk9PjnZ_8FKDcXsIpg67YoBQzAdSh8n9ID1l5N-t-UsqxzLX6p_dcaQAVsQDvpHm82ywS95ARG-SfbqWM_LdlRPDP4Sh1fhax6KaY0AvXtyISM4OvEPWyCM9aZQ6hcbp66sy3ilS6qyrHCR0Gr2dd8rd3uGNFAonevQkwAsZe5A6iy0ON-t11-2oC00TvUgi78OV2iglQlx2Vdb2l-07qr7Bp8wrUjr5oCYOwdBxbVr0PVFHvYWWdudd1A3HzpvZ3k_7qLcGOQE_h25PLHqtMp3MBYSkYDVfU3uvQoL_Vr4f6iZ8rrx6UIdurfFrAQBdCkwskBHhWgpKJDV2aUlhgnQsyFyAs7EiK9Hz7fiaozp14QOJkwnbF1gXCmR7eYINu0O_ZnF5pf7LINlcsLyfGtz3Eeh-XkwMUSIAKDKNA7FqYCe_cKVQQeM8P2lsNxpKywyHcGxGgt-ZcCy6RqZJ5pxGkFrdy7s4S1BgZMpFT7TvgGxCUezfFNybmW1-t9tkUVJur1wNTFqTd4lFc3upSdT3YXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af5db818dd.mp4?token=PaB0Ik9GT67fRIH-G6I64qn2Suhic-bEKyDdaUvFEejNH251Ij9T10HHnKJtnnte-2BO5wr5DC8jxb1gbuzwLgI5BbKJ8V4M4Y7e1EKv6zIhHRvg66mKS8MIwj531xLIujooWlfWhVke5Sf8uk9PjnZ_8FKDcXsIpg67YoBQzAdSh8n9ID1l5N-t-UsqxzLX6p_dcaQAVsQDvpHm82ywS95ARG-SfbqWM_LdlRPDP4Sh1fhax6KaY0AvXtyISM4OvEPWyCM9aZQ6hcbp66sy3ilS6qyrHCR0Gr2dd8rd3uGNFAonevQkwAsZe5A6iy0ON-t11-2oC00TvUgi78OV2iglQlx2Vdb2l-07qr7Bp8wrUjr5oCYOwdBxbVr0PVFHvYWWdudd1A3HzpvZ3k_7qLcGOQE_h25PLHqtMp3MBYSkYDVfU3uvQoL_Vr4f6iZ8rrx6UIdurfFrAQBdCkwskBHhWgpKJDV2aUlhgnQsyFyAs7EiK9Hz7fiaozp14QOJkwnbF1gXCmR7eYINu0O_ZnF5pf7LINlcsLyfGtz3Eeh-XkwMUSIAKDKNA7FqYCe_cKVQQeM8P2lsNxpKywyHcGxGgt-ZcCy6RqZJ5pxGkFrdy7s4S1BgZMpFT7TvgGxCUezfFNybmW1-t9tkUVJur1wNTFqTd4lFc3upSdT3YXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش بزرگ جان‌فدا، امنیت محله محور و مقاومت در بهارستان تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/462528" target="_blank">📅 21:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462527">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af808b6067.mp4?token=uNuc2muThSsJf1SRUuEnz17uM0pvbrcRhj_hFmrvmNbrcbbEJKx9_O6RyS3S92Eb6Ddjg4ASVG-IqAp8wd8jzTaq5btz0TJUMRQYYlL_4KmE1zSfwBiQK7RIOVZ1qaUYYoHfU3tEW8RTiOYtNUhom-R6AC9NlYKZBGToyKFvsmcJLCmOCap05vCcE5isl4LRBzOOdPuS2XMsS3BzIyzIg2qZRKXMBi8tkcDiiUDcGMZFHMU0kJtiXwqMAj74t0vL98411aJ20IHq6HrDO8Iaw2Umzot7Yn5lZ8fdIO5cmWj6sKQlYL8z2UFgYxKtShzG36FtWmkxdqfmp2g_RJYPvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af808b6067.mp4?token=uNuc2muThSsJf1SRUuEnz17uM0pvbrcRhj_hFmrvmNbrcbbEJKx9_O6RyS3S92Eb6Ddjg4ASVG-IqAp8wd8jzTaq5btz0TJUMRQYYlL_4KmE1zSfwBiQK7RIOVZ1qaUYYoHfU3tEW8RTiOYtNUhom-R6AC9NlYKZBGToyKFvsmcJLCmOCap05vCcE5isl4LRBzOOdPuS2XMsS3BzIyzIg2qZRKXMBi8tkcDiiUDcGMZFHMU0kJtiXwqMAj74t0vL98411aJ20IHq6HrDO8Iaw2Umzot7Yn5lZ8fdIO5cmWj6sKQlYL8z2UFgYxKtShzG36FtWmkxdqfmp2g_RJYPvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر سرنگون‌شدن اف-۱۵ سعودی توسط یمنی‌ها  @Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/462527" target="_blank">📅 21:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462526">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14cce86436.mp4?token=LtqxoUsRLxONmhWGuBSnVzW9c3QhlH4t5RfL1dQYEqMJo7zpYF3O3T0GM1rd-FBdA2o5SturKg_WCgEPEFKXXc1wpMZDWFIHyYk5vKhTvm6MF9VfpB-PhKalEcyvTYquSKwICagXUnjCqOCFpuxXOqbjRsDcSRS6j49nK2R0Wcz9HSeQftDfm0Z-qgX8T3AuFRwN6pQTswik6m8nFj9M9iXPrPalZDQ0B_in4mOY1rGkUVxiUJ3mFQt7mWT1U5w4aQWNlbJUg7ZRo8KSM7UvCL8PTB9buwH18hQCUrNqnO2dc_eUrT5dWBXoHbZNPexMSpJ7BW8jkof8Tccg7D2ruQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14cce86436.mp4?token=LtqxoUsRLxONmhWGuBSnVzW9c3QhlH4t5RfL1dQYEqMJo7zpYF3O3T0GM1rd-FBdA2o5SturKg_WCgEPEFKXXc1wpMZDWFIHyYk5vKhTvm6MF9VfpB-PhKalEcyvTYquSKwICagXUnjCqOCFpuxXOqbjRsDcSRS6j49nK2R0Wcz9HSeQftDfm0Z-qgX8T3AuFRwN6pQTswik6m8nFj9M9iXPrPalZDQ0B_in4mOY1rGkUVxiUJ3mFQt7mWT1U5w4aQWNlbJUg7ZRo8KSM7UvCL8PTB9buwH18hQCUrNqnO2dc_eUrT5dWBXoHbZNPexMSpJ7BW8jkof8Tccg7D2ruQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام خلج: تکبر با حرف درمان نمی‌شود؛ باید جایی که نفس می‌خواهد تکبر کند، خودت را بشکنی.
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/462526" target="_blank">📅 21:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462525">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj8JtYuSmWahsAMEHYvQR1ldTUW-P0ZNYus06X0epJb8TpskcrJOt35p9v4nqIFZdjkoJ5pQCU22myO7vInRZywSr-VUoaCt1tkhubx_3BQzfWP7RGZWi26JtSO23oj5njBrPRLTHhmgPYcuPlV_HamXnXwUWXa8D2gUSubVpSv1R3ifA-GUY9LV6WXGHdUQHQLRcgZtjBtaaTtZs8ltrYmrNWQH0ATnHYyO_yFY8JgoFiFR2I5rtOixX6Q-mFice40iKe73EUmVS_nNCO26hH2CQWBhUf1lp5CPGxtePsdEIcUn3je7VG6daeERVGxwD1-cvgCR7XgQWvFamtC5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پویش ملی «برای پدر به عشق پسر»
🔹
به‌مناسبت میلاد امام حسن عسکری(ع)، مسجد مقدس جمکران، پویشی در جهت ترویج «همسایه داری اسلامی» و با هدف تقویت و نمایش وحدت و همدلی ملی برگزار می‌کند.
🔹
با ارسال عدد ۱۴ به سامانه پیامکی ۳۰۰۰۳۳۱۳ می‌توانید از جزئیات این پویش ملی بیشتر بدانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/462525" target="_blank">📅 21:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462524">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5375928a52.mp4?token=JnqXwMqAGv8G_a3M9nuT80wuL9uTUlOgvP3RPyNwMvesBi77MN1P5BLg81szcmNHLpiLaTzEmgnrmr4VkzY3jNoFViTpbY8NqmwKHspF6kU2pV7LWSCpJwg9jAHbOl9is6b4oweyPSgmpd1XQhgxntmjQcz65_ekULOVgb1fcKmADuSzOLCgSst_hB_M3BhMTELLjtEKl3YsqTUiAF967Oo1jYmYNZZWeTu7liwU43YiQfvyoNGd30bMaSoK7Jhq28NSkhrUs811JpyIk0Iolg9zl4cRfHeZtPbHXGk-FV8Te4N53p480H3gM-NA1k9uzAdEsW1LnuygHU_dtUlwUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5375928a52.mp4?token=JnqXwMqAGv8G_a3M9nuT80wuL9uTUlOgvP3RPyNwMvesBi77MN1P5BLg81szcmNHLpiLaTzEmgnrmr4VkzY3jNoFViTpbY8NqmwKHspF6kU2pV7LWSCpJwg9jAHbOl9is6b4oweyPSgmpd1XQhgxntmjQcz65_ekULOVgb1fcKmADuSzOLCgSst_hB_M3BhMTELLjtEKl3YsqTUiAF967Oo1jYmYNZZWeTu7liwU43YiQfvyoNGd30bMaSoK7Jhq28NSkhrUs811JpyIk0Iolg9zl4cRfHeZtPbHXGk-FV8Te4N53p480H3gM-NA1k9uzAdEsW1LnuygHU_dtUlwUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید: انگلیسی‌ها به رضای پهلوی گفتند برو و رفت!
🔹
اگر غیرت داری بگو نمی‌روم، بگذار تو را بکشند!
🗓
۲۵ شهریور، سالگرد تبعید رضا پهلوی از ایران
@Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/462524" target="_blank">📅 21:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462517">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWmokbUE4iEehMZPMhrps917NwyppAz8frTgMJ9VD4odilk3ksAYeFGBH8IMbcfvOqBB7wzNb88BjK_Qph7kZT22v5yZO8kv519gfB1bUmMaK4Uc0oybzUZXF3c0szZGqmtcYk9U3h5G-TL9kaQUbVkFRJ9W9Q9Oidu5gzdAxIH1yeV9oOEmKgRLihUspoZlh08ezmzj4_qp_pDAncLkjREzbkHA7Lh4wQVuKz5lhjgde4UbVmu5qe4Zlzn6aQmvHvfq-TJoxTMpa8twnV_NhO4CyZl0vMDjIyi3AELUMuoPcFsuMHPrntyy4dEg8E6Hz0qbc1kU3CrdfaCeEnkLkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-K-1C_37vvDVVum2VkrMObu_5dGbZvja-lW1j1rBZbFbvdYphne_UAld1FwSy3EiEus7Oz6RlZEkwJGp5zSjK_1gy1YvxJobBk_8wLlvAk5iNddzgA5p8Q2KpifnkEMyeqhSN-Tf7tA7ARksw96gmtRu6_Dbrttbh0s2EZgo19URci2DzPV790FwDRfwTBS_tInj4AormTy6XbBRQEfDYS3nE4sV-Fw49F6mghGJPc-726vqyclpEeOtWCmWqAvhV69GD3s4xD0giKexYuSBh6XSmtZ4e4Le0cEbQiOaBAkrmwFDZ8pcHuzV3MRMY8OgaVcYvyDZFQr4tni3HsX_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPBzotEpEiED0owQllCv1BT8d12ohTcapSV3u500GnKUQMPuEvXyBK9Tqf0CKzwAKH391erAJ4nfDw5Re96QHZUy2P5YV-_5RrEkBURCd6p-kNV_RIzoTAToxSCxJr58NYzeBRPq7D-j5gyZRlYF1cnHsjoruiDHopCIVCBogSkEcPOQHqB8P1vYfJu36xPd6_tO7-QbD_SkLUQFeaL94ujWcj15CacpAz0LoU_v_uwb5AzrvKwqi2LDpLRYkFcNkktGJph5nbeIzUweP48CKPjAj-05-hEAGrRYLKj2FM-jCiiY4g9yES-WYRqw1lLJJk_dYj3eQl4BySWkEDujvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLJzQqRAnpsW-_Arr3ed6xQ-oXS9Ko-rvvgO9wrNrAzxxqLjWDgoAeGPEgZ_uRLH4XS9ZskfDVpBhf7jmDoB7rJ5BxZrQ_jhVpegboqWO2sTSkL_n0gnA2uoLPVdM6WV-TqKLaMqH777C_HRBJh6fu9Xw9SIXM9FAPJY2RP_aCU6P_gKarpTlSKpsx1K-Der_QxfgKv-JfTnanUFFOd0-aqlrOo0zUIE8G5tKpFQfMjvwI1dmvHwr3TPC2cgXxuu4_3C2tTBIk2jKTswGMot3pWAfLIfaIabvjaS1HWN_10iy-5tiKyKuJ1jdk1dn_aHVfHta2t_d_My3Csc1VNMnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufNDycMzo0rynfG7fplxGg0VY2_7k2_nVwbeNmw1oAeX7POyPnZnFTvuMsW0LLeMWUVTZqhejxQbHThf9gWeZIQBZ3GpSnX-qdrZ3Uu1S188unfZqnh78S08eimpRf2PaL8PJLOkp2nH4YGYdnAkz3lGDMrFOa3sWRdaqbW6-8iaUuvErA_McM0VNhB8i5F4H2WPpRsNK5GLqr4058kt7U7KnvYWknP22kB8qsoTlJtYMEpmYXM92lmpyFh7n68KqMD7x4EqWIEWpdHwdG45S9_N15gtp9FJswI593qjkiFt2N-KZShgMciOkmcTz74VZJLnCTqV-Cl590VkiqEcBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_BRLbdUa3SaILHpgjYkft-rTdY0MIcQO-QgR6ToDwKsto8ld8H6XBfSn1bjUrFp00qjNy_-YSHnyA1WDQKBGva-lVdItZjk1Zfwo1y5u-4VqOERveKNhuAVSBfvWg1vsPsP1jt84wkUNZsbmDbGEKCMq4HdhLJKf0NS3IfUCq5zEGTRB9Ij-2S1U4GR4SmhkK4GfjUk1UjTeicC4IWsk2KHcBE7psH1uNBr6i2KxCZDU_p2-nmqS0jDkhwGnI3osTKXDBBEQGIht07qM2hYwAUbq1y6RlXEB0Ua_R6o8u14Mlevne_dzLISEalB_dvUt4nk8uLi-dx0ymmi30nruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBE7exWNjxH_1po7tmakL704Kib1b7hUqoiAVBg0hcH-3m7XUtI9vWKE-7lsTcIYrysnSqa9vzkoePh9k-0xizDJruCiL-RPuBN-IqrRwia1pB-GmGnGlU8vgd2Wd7bzZAoylI1l-JQ10_3Apfbor68kKVr3agC9zSME4xlLEj9Y_ckXYjcoJCdD9OKdiW6zvnr8sP1Ejtb83Cqv0Msxel84QNfomIl2UCPin-7LAoN2ArFTkOgt55dMcg75Vr016eLgL6_NomMfqHbEN2UGIKjY8hoV0jziN17OkWGy27L__GeOF9cua7zcDNXx79BTmhqcZxqrYytfizUDiGXHQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
موسم بادام‌چینی در باغ‌های خرم‌آباد
عکس:
نگار ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/462517" target="_blank">📅 21:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462516">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcd104da5f.mp4?token=o1F0T355M-gX64gG3VjVB73XrwApQ7d_s0F1r-TQSzZDiGmGiycuZ7YE4_9vwkNvch5JgNShAzHVHsfRxMq2uaA9YRcQP6QedXIpRo0v7Cud9qIElI4GvqiS4CyVdiijytjIvvSrX6ETzcgm-tmdaIBiZvmj6T6EbCz9KbXYG9ufjSS5HWbMkqdUEAgSABLJ-ArqE6-UZzfDBEMC5jKMCfudc6tKuCD6pgGqdteBcbrJkAYTn5usqzgwluhGyLw3dqs6cYJDUE24XcsAqNHMIT6vtKPviqlDMBENL6f0XjTfcyySahlD6UybGbFrvd-aW-xSAqmBkkzhCfetNxg67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcd104da5f.mp4?token=o1F0T355M-gX64gG3VjVB73XrwApQ7d_s0F1r-TQSzZDiGmGiycuZ7YE4_9vwkNvch5JgNShAzHVHsfRxMq2uaA9YRcQP6QedXIpRo0v7Cud9qIElI4GvqiS4CyVdiijytjIvvSrX6ETzcgm-tmdaIBiZvmj6T6EbCz9KbXYG9ufjSS5HWbMkqdUEAgSABLJ-ArqE6-UZzfDBEMC5jKMCfudc6tKuCD6pgGqdteBcbrJkAYTn5usqzgwluhGyLw3dqs6cYJDUE24XcsAqNHMIT6vtKPviqlDMBENL6f0XjTfcyySahlD6UybGbFrvd-aW-xSAqmBkkzhCfetNxg67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آهوی زخمی پس از یک ماه درمان به طبیعت قصرشیرین بازگشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/462516" target="_blank">📅 21:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462515">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089c9ef32a.mp4?token=ehOPjH9nsfLcKMRnnh9Q0FXHDiJGwZTIIR8kwdhfxql-DIDjE2fYpps0lYlqMTuHCICfYPfUfwlF5eutJdCZevufQar2IMc3uWT-tGDEU9Piv2QoHMrkApstndAqn3Jm9O-HTIEYtD0mzWy1f_6NbRGvnCPgXGqF0NA9rI9mhADRU_csj4kjpqENG0qP8Es8hY8flvqKAVimXshj5st7Xq3LnyXAq2xlYq62LhxGO4rmY9HUKPoW0YAwebnPTgMkWfkFIsgr8bAJmiRdhn0z9EZ0ht42eKJixbyjf_eXT1_hPjGNMn8_RtrRlQSJk1JzULqRAoBMsdnRwzSLbTJLgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089c9ef32a.mp4?token=ehOPjH9nsfLcKMRnnh9Q0FXHDiJGwZTIIR8kwdhfxql-DIDjE2fYpps0lYlqMTuHCICfYPfUfwlF5eutJdCZevufQar2IMc3uWT-tGDEU9Piv2QoHMrkApstndAqn3Jm9O-HTIEYtD0mzWy1f_6NbRGvnCPgXGqF0NA9rI9mhADRU_csj4kjpqENG0qP8Es8hY8flvqKAVimXshj5st7Xq3LnyXAq2xlYq62LhxGO4rmY9HUKPoW0YAwebnPTgMkWfkFIsgr8bAJmiRdhn0z9EZ0ht42eKJixbyjf_eXT1_hPjGNMn8_RtrRlQSJk1JzULqRAoBMsdnRwzSLbTJLgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۵ هزار نفری گردان‌های «جان‌فدا» در شهرری  @Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/462515" target="_blank">📅 21:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462514">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389a3dbfe1.mp4?token=D2QjZhyndp8ckqYBjSQF7xoSRYunz2zAAuIBHY7LjBGpOtYP5r2B53pTTPtHYO_ak4JMf2WwdR88M8bXzALAZd3Pm8MyT2ttkLSyXmgGy_hUFcPttQmiDQKAcyZzqmHW2ci8zWUPLAD-2ZC-C4JPyY2xjaKZ13pD3Dql4O7cpqPMGwjQQ5lOw9SuGIB71xwbrYu88xoFMqLTcTMjUIeRAgXM384fzHB1o4IefKAlLh-G1Swugpo4oR86uetY4mbIilPuF6g4XQ5-Zdq-9JmTL_eJxqFMth9DfTDumdE_N7lYokUIvXGiaL4Vj2jraZu1kZQyhnDT7AJzTPKUQugSfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389a3dbfe1.mp4?token=D2QjZhyndp8ckqYBjSQF7xoSRYunz2zAAuIBHY7LjBGpOtYP5r2B53pTTPtHYO_ak4JMf2WwdR88M8bXzALAZd3Pm8MyT2ttkLSyXmgGy_hUFcPttQmiDQKAcyZzqmHW2ci8zWUPLAD-2ZC-C4JPyY2xjaKZ13pD3Dql4O7cpqPMGwjQQ5lOw9SuGIB71xwbrYu88xoFMqLTcTMjUIeRAgXM384fzHB1o4IefKAlLh-G1Swugpo4oR86uetY4mbIilPuF6g4XQ5-Zdq-9JmTL_eJxqFMth9DfTDumdE_N7lYokUIvXGiaL4Vj2jraZu1kZQyhnDT7AJzTPKUQugSfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا از قدرت موشکی و پهپادی ایران پرده برداشت
@Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/462514" target="_blank">📅 21:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462513">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c39512b85.mp4?token=RgDeo3rqplo3_qZK6I5O8KrjIQtvovt0M1WbLN5rEnC_9MvddzuyttyM-Hs5x_6wPDY_CByy-WZDEwWP_BR4oXHKGfIT-8jPsXwmaARM7Xh-fikRdW-zM9vVYMTmPjs9JJabRO_mRluP28lXerrY96J00rUvi0p5pnY3BE_n4-1nVtX3z_s3f0AWw5i74hFegxdeHyQrblZDytugNBDvYOmbVihKECEnTi52wh5_ibm0R-frWMrlRFeUCKkXPcQ-IDFYOP2Vo-f9JdhP9BF71qY4VbDb3hZJLiPIopPy76_S7u-I6iFWADxpTBFUJdLXyY34Lp9unVjPVNBaOLzeKxRhoZKnzBVq9HNCo-ZjL6oz-76YrpHFfyezTP-xMJnz7coajgX-RkoGd6YwepQDabh1ZsqZR07TSnCv_-dZYTPA1lWjj0yKf8jpu5dx1m7OY6H9lT7GlEr-jBevGp4l-2vMk5ePMd-qdKVTEArBCSLnyRvxfeWTYVYQpmk8lyHZgn3-0IOj9DI2fKXn4kMVWUyKMw7eDE_6TlvZjdn3blS4n8YjGyWusAWtuwf1IlnthPRLmzOA3atXtDdooFP8hEil26bi0CVc-Lgjt1xlQzOzFZmb3H68NQxtDbb7VuDf-3lYqRrx91IA_eQaBpErONvQ9p7wZE2xe3Syxa_6k2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c39512b85.mp4?token=RgDeo3rqplo3_qZK6I5O8KrjIQtvovt0M1WbLN5rEnC_9MvddzuyttyM-Hs5x_6wPDY_CByy-WZDEwWP_BR4oXHKGfIT-8jPsXwmaARM7Xh-fikRdW-zM9vVYMTmPjs9JJabRO_mRluP28lXerrY96J00rUvi0p5pnY3BE_n4-1nVtX3z_s3f0AWw5i74hFegxdeHyQrblZDytugNBDvYOmbVihKECEnTi52wh5_ibm0R-frWMrlRFeUCKkXPcQ-IDFYOP2Vo-f9JdhP9BF71qY4VbDb3hZJLiPIopPy76_S7u-I6iFWADxpTBFUJdLXyY34Lp9unVjPVNBaOLzeKxRhoZKnzBVq9HNCo-ZjL6oz-76YrpHFfyezTP-xMJnz7coajgX-RkoGd6YwepQDabh1ZsqZR07TSnCv_-dZYTPA1lWjj0yKf8jpu5dx1m7OY6H9lT7GlEr-jBevGp4l-2vMk5ePMd-qdKVTEArBCSLnyRvxfeWTYVYQpmk8lyHZgn3-0IOj9DI2fKXn4kMVWUyKMw7eDE_6TlvZjdn3blS4n8YjGyWusAWtuwf1IlnthPRLmzOA3atXtDdooFP8hEil26bi0CVc-Lgjt1xlQzOzFZmb3H68NQxtDbb7VuDf-3lYqRrx91IA_eQaBpErONvQ9p7wZE2xe3Syxa_6k2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی پویش ملی جان‌فدا: در پویش ملی جان‌فدا تقریبا همه مسئولان تراز اول کشور با هر گرایش سیاسی ثبت نام کردند
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/462513" target="_blank">📅 21:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462512">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ7Gq1nUKFLT04fp9DnZDQcrreANO_NbBCWu0K_n_jR9LSfaiG1WoEzHln7w972FAX8RDcOU-0CE84ATWwZGFi5jpxAfsOJu9hifa_wG2KRDHNzsS_BAsUQ5Igr25D5Sfw9CCgPgSmcABSFqMtrksgIlgG5vJOF3bsJjVRzu7DIjKDGbwQ_bS-FgV05PGCwg7KycMwnYJ6RFET3ObaMq-tvuka5xOB9naWjM0MP9jB9bvhgt_dFH9082Tz0Yuzj3dNdp3BFj0U6J4EhJn7dDuHUIAOttELfSwiRG3JtYbrwRUqHJs5ksfttiawMYHHC7dqnn_rny2GbK_JeDzutElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکاف میان ترامپ و هم‌حزبی‌ها بر سر ایران باز هم عمیق‌تر شد
🔹
در رأی‌گیری مجلس نمایندگان برای پایان دادن به جنگ علیه ایران، سه چهره جمهوری‌خواه دیگر به مخالفان جنگ پیوستند، موضوعی که مورد توجه رسانه‌های حامی و مخالف ترامپ در آمریکا قرار گرفته است.
🔹
به گزارش سی‌ان‌ان، مجلس نمایندگان روز سه‌شنبه به وقت محلی طرحی را تصویب کرد که بر اساس آن، از رئیس‌جمهور آمریکا دونالد ترامپ خواستند که جنگ علیه ایران را پایان دهد. این طرح نیاز به تأیید سنا نیز دارد و حتی در صورت تأیید، باز هم ممکن است با وتوی ترامپ، رد شود.
🔹
اما تنها چند هفته پیش از انتخابات میان‌دوره‌ای، این رأی‌گیری یک انتقاد سیاسی جدی از نحوهٔ مدیریت جنگ توسط دولت ترامپ محسوب می‌شود.
🔸
این سومین بار است که مجلس نمایندگان به ترامپ دستور می‌دهد که نیروهای آمریکایی را از درگیری‌ها با ایران خارج کند. با این حال، دموکرات‌ها می‌گویند این رأی‌گیری مهم‌ترین تلاش آن‌ها تاکنون بوده است.
🔹
این بار ۷ جمهوری‌خواه از این طرح حمایت کردند، در حالی که در دو طرح قبل تنها ۴ جمهوری‌خواه رأی مثبت داده بودند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/462512" target="_blank">📅 21:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462511">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a37ba4c21.mp4?token=Yz6yz60twU85jX7NhxxJKwpxypZH-CGmE2Bf_KmC8Hj8umKZMf3aOzfxIz5pCLW4MKfiJpiMf8rtTQbTwmo_wHv3RKuLr6kcI0NrN11eBFQrPGDSCP5dcMup348G8VpoUHuoVswvVcCy0svaa2Kl_9bfT4Iykd_AAxfs_etB9SaouEQXfyuUQdse6BTtaS4X8hDGnAtfELIY2-JrsrKAoAEbp0gPhBYHgYVDpe8Yaz0mqBvKM6QCqz6rxlRninR9mXDNaq4xPBKrjMlCA8TSm63zM68vBal2cayDmJuX_5pL2lfE6GDvFIGUhKfbkuLaYDeLhGLPZM9eYqrFaeITng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a37ba4c21.mp4?token=Yz6yz60twU85jX7NhxxJKwpxypZH-CGmE2Bf_KmC8Hj8umKZMf3aOzfxIz5pCLW4MKfiJpiMf8rtTQbTwmo_wHv3RKuLr6kcI0NrN11eBFQrPGDSCP5dcMup348G8VpoUHuoVswvVcCy0svaa2Kl_9bfT4Iykd_AAxfs_etB9SaouEQXfyuUQdse6BTtaS4X8hDGnAtfELIY2-JrsrKAoAEbp0gPhBYHgYVDpe8Yaz0mqBvKM6QCqz6rxlRninR9mXDNaq4xPBKrjMlCA8TSm63zM68vBal2cayDmJuX_5pL2lfE6GDvFIGUhKfbkuLaYDeLhGLPZM9eYqrFaeITng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قریشی، تحلیل‌گر سیاسی: نگاه فانتزی به صلح خطرناک است
🔹
این‌ تصور که به هرکس در منطقه یا جهان علیه ما اقدام کرد گل بدهیم و روبوسی کنیم جالب است اما امکان‌پذیر نیست.
🔹
بزرگترین حملات تاریخ سوریه پس‌از سقوط بشار و عادی‌سازی با اسرائیل اتفاق افتاد و تمام امکانات…</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/462511" target="_blank">📅 20:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462510">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39c85ba54.mp4?token=TYMQaix-n_XPf3cavyrVAi9A7K3QfnZ1_-RsNvqFsmuyo4MTlwrY_lFze3_ItPnWQrJ694HmuZgznHi1akmzHzjMZzXFDw9L_ZV1nH7T_F_rY_QaF8f3yAD_x9op5oYt4fEhkrSwSohRRAWVXKHBzimDGlecVwgjavdA1mbJDLYlUXV25k5UXr6vD12fjJQcT0jBqAJguHRuIMP_dcD_2eojRuXpyHgi2Bt6EwZ_x6yQuQ4nyFk7-Mqb3ngN437_UKCYqKCv1I4vxS9jnTTD-FhCtAkQrR4qYA1VQIe5JlVX87k9djPNpgGCapyXgMvPfkbt5ag6k8ITED9Hs7wbxIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39c85ba54.mp4?token=TYMQaix-n_XPf3cavyrVAi9A7K3QfnZ1_-RsNvqFsmuyo4MTlwrY_lFze3_ItPnWQrJ694HmuZgznHi1akmzHzjMZzXFDw9L_ZV1nH7T_F_rY_QaF8f3yAD_x9op5oYt4fEhkrSwSohRRAWVXKHBzimDGlecVwgjavdA1mbJDLYlUXV25k5UXr6vD12fjJQcT0jBqAJguHRuIMP_dcD_2eojRuXpyHgi2Bt6EwZ_x6yQuQ4nyFk7-Mqb3ngN437_UKCYqKCv1I4vxS9jnTTD-FhCtAkQrR4qYA1VQIe5JlVX87k9djPNpgGCapyXgMvPfkbt5ag6k8ITED9Hs7wbxIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بازار فردوسی سنندج
🔹
با نزدیک‌شدن به آغاز سال تحصیلی جدید، بازار پیاده‌راه فردوسی سنندج رونق گرفته و خانواده‌ها برای خرید لوازم‌التحریر راهی این بازار شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/462510" target="_blank">📅 20:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462509">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رکورد تاریخی عدم بازپرداخت بدهی وام‌های خصوصی در آمریکا
🔹
موسسه رتبه‌بندی فیچ می‌گوید که حدود ۶.۳ درصد وام‌های بخش اعتبارات خصوصی شرکت‌های آمریکایی طی ۱۲ ماه گذشته وارد وضعیت نکول شده‌اند.
🔹
یعنی شرکت‌های وام‌گیرنده نتوانسته‌اند پرداخت‌هایشان را طبق شرایط قرارداد انجام دهند.
🔹
این آمار جدید درحالی‌ اعلام شده که بازدهی اوراق قرضه ۳۰ ساله به بالاترین رقم ۲۲ سال گذشته و رقم درست پیش از بحران مالی ۲۰۰۸ رسیده و بازدهی اوراق ۱۰ ساله هم دیروز به بالاترین رقم ۱۹ سال گذشته رسیده است.
🔹
اوراقی که با شوک‌های انرژی سرمایه‌گذاران را نگران شعله‌ور شدن تورم در اقتصاد آمریکا می‌کند و آنها سودی بیشتری برای این اوراق درخواست می‌کنند که تورم‌زاست.
🔹
حالا که قیمت نفت آمریکا بالای ۱۰۴ دلار و قیمت بنزین و گازوئیل رکورد زده، نکول وام‌های خصوصی شرکت‌های خدمات درمانی و صنایع و تولید در صدر قرار گرفته و در ماه آگوست ۴۵ موارد نکول در مورد تمدید سررسید بدهی بوده است.
🔹
فیچ تنها عدم پرداخت اقساط را نکول معرفی نمی‌کند بلکه مواردی مانند تمدید سررسید بدهی و تعویق پرداخت بهره، ورشکستگی و انحلال و تبدیل بدهی به سهام و موارد دیگر را هم از مصادیق نکول می‌داند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/462509" target="_blank">📅 20:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462508">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزارت دفاع عراق صدور هرگونه گزارش اطلاعاتی دربارۀ قصد عربستان برای هدف‌قراردادن مقرهای الحشدالشعبی را تکذیب کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/462508" target="_blank">📅 20:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462507">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ao_A1RCU6CUNLOODo3NKpb0Ej9SuilCTS-L9CreuznlLrL7fYK3FqwD6cYGaF027pjrHPm_P_YroL2t0VyunJsgGuHR1N1u7d7dZyz6ia6OTR0OV5fOxTTVIONk1VoJ5t7NbNbZLLgssD-LNDUyiHCpd7M372OOSWEL5CC8GnJkGJZGVgKo1VhwkkgfSesOte7Nuz1sf5F5wgoAftM7lTYak-tuzOY1o6Itnvgws1pAO9TXObfxUJ85VCaVTVczD_PI1R0n29KE0-IfOT8g8CHcyg54lOPCfH7PO4nhaYXhdxuorlmPvv6V4LEuDHbMqvtS42KTdhnwb_vfRWv4kfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس ستادکل نیروهای مسلح: از میدان رزم به شما مردم خبر می‌دهم که حضور مقدستان باعث هراس در دل دشمن شده
🔹
این بعثت مردم، یادگار امام  شهیدمان و ابداع مردم مبعوث شده است.
🔹
مردم عزیز ایران! از میدان رزم به شما خبر  می‌دهم که این حضور و اتحاد مقدس شماست که موجب تقویت روحیه رزمندگان، افزایش قدرت‌ ملی و هراس در دل دشمن شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/462507" target="_blank">📅 20:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462506">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: جنگنده‌های سعودی را با پدافند فراری دادیم
🔹
یحیی سریع: نیروهای مسلح یمن دقایقی پیش موفق شدند دو جنگندۀ سعودی که از پایگاه‌های خمیس مشیط و طائف برخاسته بودند را در استان صعده رهگیری کنند.
🔹
این جنگنده‌ها با استفاده از موشک‌های پدافندی…</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/462506" target="_blank">📅 20:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462505">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49232f1f4c.mp4?token=RyDUg_GthW1K-R6FBACpb3K0JyP5xew0dIJTRX3x3RJgHdApj9pqK0fvvNS9AX4_cjy2_bWBZDZNNyVH76e9Z9lXnGUfmdZYyz_5qUdC4VBJideMUPghXOtBck2t4w80VIsnLObAvKmNMd1xxQ4Qo-ISOKQCRwuggBHneBJ9YqjYbvCuJQGYuuOun9tjOeJ_AvZcP2vXtG_iPb7X5pVAoIWsHQb-2A2t_YwbneJQE7viKYp_szlapsen94Wtgjzv9kT0f8XvfvfJq_QL7TvVmRY9UtjDTG_YcSAFXynoSIqymLgD9eJlFW9jhjKXHECrcXyBBwJAl8vrtfifVJ3S4ZwFzAUYeT53j4iJdP6OT-4zpx4QAVK-FfjtxQpL-lKCyBqVgBDOAt0tU7kTru8qhztH8FUfHtNrXGO3a6YspHr_x1uD4yIB5vDZrGScKsy2FAT97Dkp94NddneZotxt95uPA2wNja7ZUG2gfwWWzCQVf2bDwHBTTLhomIXY194wFkBspbLj8D7wp7K6veahhjbCtHh9e02PcoVA9RIkDwfYy0A6XPjjgbEXW6HWC-tVZ7wdaytmxumsXhpvLSRo4xqABGGXQHzCa3HqoapGITHX_3Dgzv9z3jqr15NZlWycVAEn7hRCmZ2rYZo6EyGisT7i6fNkNTp1LNpDfRNtifo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49232f1f4c.mp4?token=RyDUg_GthW1K-R6FBACpb3K0JyP5xew0dIJTRX3x3RJgHdApj9pqK0fvvNS9AX4_cjy2_bWBZDZNNyVH76e9Z9lXnGUfmdZYyz_5qUdC4VBJideMUPghXOtBck2t4w80VIsnLObAvKmNMd1xxQ4Qo-ISOKQCRwuggBHneBJ9YqjYbvCuJQGYuuOun9tjOeJ_AvZcP2vXtG_iPb7X5pVAoIWsHQb-2A2t_YwbneJQE7viKYp_szlapsen94Wtgjzv9kT0f8XvfvfJq_QL7TvVmRY9UtjDTG_YcSAFXynoSIqymLgD9eJlFW9jhjKXHECrcXyBBwJAl8vrtfifVJ3S4ZwFzAUYeT53j4iJdP6OT-4zpx4QAVK-FfjtxQpL-lKCyBqVgBDOAt0tU7kTru8qhztH8FUfHtNrXGO3a6YspHr_x1uD4yIB5vDZrGScKsy2FAT97Dkp94NddneZotxt95uPA2wNja7ZUG2gfwWWzCQVf2bDwHBTTLhomIXY194wFkBspbLj8D7wp7K6veahhjbCtHh9e02PcoVA9RIkDwfYy0A6XPjjgbEXW6HWC-tVZ7wdaytmxumsXhpvLSRo4xqABGGXQHzCa3HqoapGITHX_3Dgzv9z3jqr15NZlWycVAEn7hRCmZ2rYZo6EyGisT7i6fNkNTp1LNpDfRNtifo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ اتفاقی مردم را از میدان جدا نکرد
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/462505" target="_blank">📅 20:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462504">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8Hz2xWoYcpOs88qBE8Fi6lc4iN05wbbMVzeUrdYtEWMk6-AS_uD3NGQBX2GrkBtJauaihtCVXjZzm2UPqStLT6RdrMe5rRHomQPsEog4XZ4fQYDRslUexuNTMOGZUmLcM55kJdJZJ3MhJ7CWvvTmaGcWSNyeoiITmIoLplUC9J7BcKmZdT5dvpkMNITIhYVOPbTKgZ55i6IyFnd3u7ji-z9iocLy6ywCTQfam2fc2LoBuBhgd7_UAgZI5wIGM1HFFbAGulxKvUTsmhNJkIpW79alwZA0Jzw5zaCPqG-rd0t6hDWpf0fiCE1jjApJM4fx5Ipqa-KLNTJ6srK93Ad7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: به‌هیچ‌وجه به آمریکا اعتماد نداریم
🔹
سرلشکر رضایی در دیدار با رئیس اتحادیۀ میهنی کردستان: باید به موضوع گروهک‌های تروریستی، ایجاد امنیت در مرزها و افزایش همکاری‌های اقتصادی رسیدگی شود.
🔹
باید نسبت به تحرکات رژیم صهیونیستی در اقلیم کردستان عراق هوشیار بود.
🔹
به‎هیچ‎‌وجه به آمریکا اعتماد نداریم و آن‌ها باید اقدام عملی انجام دهند و اطمینان ما را جلب کنند.
🔹
بافل طالبانی هم در این دیدار ضمن استقبال از ارتقای همکاری‌های اقتصادی، امنیتی و دیپلماتیک، بر لزوم حل مساله گروهک‌ها و ایجاد امنیت در مرزها تاکید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/462504" target="_blank">📅 20:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462503">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7770270e1.mp4?token=Q9GcQ1NOa1fK_lRbnlYIBDIPi0cvgl_0FzcW-zLnNaHBGXBNADwTc6HN6M1xr79ZJvolnsbCMHxAJS4Cx2yzOTGp-XVOYoQOii3Tus1y4QuSA9L6uZnztoqplsbD0MpI7XG3rGnuSYAmyvATvLVkWRlJPTMT_9QKuMnZ30GQ1VbrrcP-J63DrWSmyyNVLdqO1YLx0GJPSzx-WPI76G5F3CtqanNpNlnCc0qP0hZTNJGdAp65beHc33qxx_jAxQ-IeRB_mu40pvj2Ub4cz8joIu_ghMl6zwiD3Dtw42yDbzx8arnkTiZMK6Kl7usq1auf0RTEmUcFpdfjYaYhT3wvgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7770270e1.mp4?token=Q9GcQ1NOa1fK_lRbnlYIBDIPi0cvgl_0FzcW-zLnNaHBGXBNADwTc6HN6M1xr79ZJvolnsbCMHxAJS4Cx2yzOTGp-XVOYoQOii3Tus1y4QuSA9L6uZnztoqplsbD0MpI7XG3rGnuSYAmyvATvLVkWRlJPTMT_9QKuMnZ30GQ1VbrrcP-J63DrWSmyyNVLdqO1YLx0GJPSzx-WPI76G5F3CtqanNpNlnCc0qP0hZTNJGdAp65beHc33qxx_jAxQ-IeRB_mu40pvj2Ub4cz8joIu_ghMl6zwiD3Dtw42yDbzx8arnkTiZMK6Kl7usq1auf0RTEmUcFpdfjYaYhT3wvgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۵ هزار نفری گردان‌های «جان‌فدا» در شهرری
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/462503" target="_blank">📅 20:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462502">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4HcOM8nNtGaOKhXRucBkbxM8sNInTCeND_sclPFnk-5b3ED3HjNc3Iun0D2Q9gyImwK_Q0-t9NZ5e5BvyQSoqTT-6SD7d5mmdvKtoDYVLb81R7HB2MYQ2tN1LNew2AgV_rAPszDKovqL1qJMJ4-7vZ_P9SbhnAtanfloX_dE31O_y_u24D9dO2_mR0yiAWpewdOlrGL4oGFtrIfX089sf41jJT-jG64KOqrxQqNYoQNyUI0bDuHIQILLJzVaQbcGzFIoVtqX2XmRbde61lmarwHI2GSDnWxOOcLRyeVC57kc7tCgw-TPI3nvas-_EfoSaDQ_UbgVaHIrmNNRb9yXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمک ۱۱ میلیون دلاری آیت‌الله سیستانی به آسیب‌دیدگان جنگ ایران
🔹
هیئت اعزامی دفتر آیت‌الله سیستانی در سفر به ایران، از اختصاص و توزیع ۱۱ میلیون دلار کمک مالی میان ۳۶۰۰ خانواده آسیب‌دیده از «جنگ رمضان» خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/462502" target="_blank">📅 20:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462501">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXwa-ttpT2hmGR3z55amg77rY0nqS4dhehaKIOmpQP2m6YnQlwcjRRjeorawl7N1ukqULLmYPINxJC-V-ouwTkkk6vN1epWY40oDVWojif-MbOQvk1_lamqnqm0uyH91JkTzfC1tAVQpE_SFwSsJDevx0Z9TQDbJA7-JMEWlZD-YVJtwQaKow1erRRCtaiBYCDmoCih7JmTzfTrxd2kGJuH2LCs6IXpVWuXJMvaF8F0TMX_ZkImZiqnRy621TMnT9BGxDNTq0YDkKnO-AJ19NNgrs9VPWTN5aT8dNz4ZQMFH11bznxKe5si4k7UfrlPSXh9Uxzr_-41m7XRhoYJflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ جانشین رئیس سازمان نظام وظیفه: بیرانوند از یکم مهر باید در اختیار یکی از تیم‌های نظامی قرار بگیرد؛ البته پرونده ایشان در حال رسیدگی است.  @Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/462501" target="_blank">📅 20:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462500">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51468d3e5d.mp4?token=n63992A17IGBm7MSfyyypu_9eHRBAzF8DAWnX84n2bIC_xkHzB1KcDe0wUKTXwJSbqfeWaHHRpdNV2AVrsbC-yiFI6VYKmzDOnGflDTbie3VJhN5oXuS9TNeC9zckDY9CfuD2Ium03cMbCPjNjSFQlqYBCwHrKpdpW9ThpkC3W3QJz7QrpKCKxSssimdBOH2RckVqSC7SY_mun2upLu9tPTyjRTuPJ4ySMVrNj7P_QYlwoD6bIPAjSqFlMRiMIxXaU6KjPAIaXixch8nKXkkvVBCI0zqyr714qW7AwW17d5wbWpZvhj1OvqTQVPXqchZh5wPa1bipf2FmDm-rY_A7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51468d3e5d.mp4?token=n63992A17IGBm7MSfyyypu_9eHRBAzF8DAWnX84n2bIC_xkHzB1KcDe0wUKTXwJSbqfeWaHHRpdNV2AVrsbC-yiFI6VYKmzDOnGflDTbie3VJhN5oXuS9TNeC9zckDY9CfuD2Ium03cMbCPjNjSFQlqYBCwHrKpdpW9ThpkC3W3QJz7QrpKCKxSssimdBOH2RckVqSC7SY_mun2upLu9tPTyjRTuPJ4ySMVrNj7P_QYlwoD6bIPAjSqFlMRiMIxXaU6KjPAIaXixch8nKXkkvVBCI0zqyr714qW7AwW17d5wbWpZvhj1OvqTQVPXqchZh5wPa1bipf2FmDm-rY_A7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جانشین فرمانده سپاه: دشمنی که درصدد بود نظام اسلامی ما را دچار فروپاشی کند خودش امروز در وضعیت نظامی پرمشکلی قرار دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/462500" target="_blank">📅 20:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462499">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d6604c6b2.mp4?token=Q2zB4GfHfXYR8p0dax4BTCltnfyd-q2AhCJRLGlozt3x-Swvochg6ERIcUYINhSvkJHvKUyrWbbImmqs0v3UOjK2vqFq8dZXpyDYQlpu2hIQlEuVEW_yP7DYEJj45Pc5DA8EmFPDsMggXU4_28uknAHUeSlmTV47CXQ6FetYhOu3u3AtbWTm0Ngtux9KwwL0nVXguUKxTXYkJ-pUlnmTxB8O8S2NVi3Uc725EcxSQpgQFqLdUVTduipoi0qsoQsZ59qA0OpVmr8Fn_D3W1pLDpPBtK_tDcvNGA1LAJjxxO2gGdEeYPUKtxl4E2hZa4DNYCE34l2jhbZnPTPVPgA9bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d6604c6b2.mp4?token=Q2zB4GfHfXYR8p0dax4BTCltnfyd-q2AhCJRLGlozt3x-Swvochg6ERIcUYINhSvkJHvKUyrWbbImmqs0v3UOjK2vqFq8dZXpyDYQlpu2hIQlEuVEW_yP7DYEJj45Pc5DA8EmFPDsMggXU4_28uknAHUeSlmTV47CXQ6FetYhOu3u3AtbWTm0Ngtux9KwwL0nVXguUKxTXYkJ-pUlnmTxB8O8S2NVi3Uc725EcxSQpgQFqLdUVTduipoi0qsoQsZ59qA0OpVmr8Fn_D3W1pLDpPBtK_tDcvNGA1LAJjxxO2gGdEeYPUKtxl4E2hZa4DNYCE34l2jhbZnPTPVPgA9bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قریشی، تحلیل‌گر سیاسی: نگاه فانتزی به صلح خطرناک است
🔹
این‌ تصور که به هرکس در منطقه یا جهان علیه ما اقدام کرد گل بدهیم و روبوسی کنیم جالب است اما امکان‌پذیر نیست.
🔹
بزرگترین حملات تاریخ سوریه پس‌از سقوط بشار و عادی‌سازی با اسرائیل اتفاق افتاد و تمام امکانات نظامی سوریه نابود شد.
🔹
کسی که دنبال سازش و تسلیم است باید نمونه‌ای بیاورد که کشوری پس‌از تسلیم مقابل دشمنش به موفقیت رسیده باشد.
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/462499" target="_blank">📅 20:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462498">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahVYB4f3OGwSHSyescUQ4B-rEJUvBSCRELl0OoyX46RRRXu0rzi80QYvyJWWKlQIa0kVf1MyyuSuxZ2XnLetchBEt9c1e5mdN7omBuTfMo0bqxl4QA_7tHGqf5XuHCo22dlGFAyj8XdaPwDlnVrTxUQDox0XXpKCQNP2Tfs6pI8bvLw-gyastL4kDTLqECCdVgiQgioNFgrrAm1kpS0ZihkZrcjhXO-_9HOeVboGXmX2mOdIwyGgEkcSxqexujH391A-12f524a-Qd0pRKnbO3gqNsJhaOa1F7l6MgcodMxl23lXrqME_KzeV1zJd2QGGbkuIaXuZMM2eEEUVYIXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گازسوزی شدید تاسیسات تازه هدف گرفته شدهٔ آرامکو
🔹
تصاویر ماهواره‌ای نشان می‌دهد که فلرینگ گاز در ینبع در بالاترین سطح ۱۰ روز گذشته قرار دارد.
🔹
مفسران تصاویر ماهواره‌ای می‌گویند این یعنی که یک حادثهٔ غیرعادی در آنجا در حال وقوع است.
🔸
ساعاتی پیش نیرو‌های مسلح یمن اعلام کردند که تاسیسات آرامکو در ینبع را هدف قرار داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/462498" target="_blank">📅 20:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462497">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe4a3e84d.mp4?token=qhEe5cHAfn5iZ-9Svrqofwzq1QKD8XX0fQM8W0HHkV3fBrtuZhJMMSHRI4gk14TXim_p5uaPJTFN-Myuyd4gJtXNf198bxl2ArgqSw-XnW6KXyuyY7r5TtZBtTQPpJhfsjreDq8aGs1cuXdqaJKoXI6tkdO-5LvZOYZFgPhka-Y8odKuO-zR_sTP9wff8I13rkJeUny6RzGPEUIbO1ZVBydjPN4hWaLBzOSEGfarjx_DoB7yGENo69CpfQi8PZoBe3htoTdqAi0OWl6VpgOqYkSu8iMQ602HZLns-pHjQdAFI6IkLXoPdm3sNxV7wnHF_nVaakI3rlQcYaFJ0JxbQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe4a3e84d.mp4?token=qhEe5cHAfn5iZ-9Svrqofwzq1QKD8XX0fQM8W0HHkV3fBrtuZhJMMSHRI4gk14TXim_p5uaPJTFN-Myuyd4gJtXNf198bxl2ArgqSw-XnW6KXyuyY7r5TtZBtTQPpJhfsjreDq8aGs1cuXdqaJKoXI6tkdO-5LvZOYZFgPhka-Y8odKuO-zR_sTP9wff8I13rkJeUny6RzGPEUIbO1ZVBydjPN4hWaLBzOSEGfarjx_DoB7yGENo69CpfQi8PZoBe3htoTdqAi0OWl6VpgOqYkSu8iMQ602HZLns-pHjQdAFI6IkLXoPdm3sNxV7wnHF_nVaakI3rlQcYaFJ0JxbQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۰ شب است که در میدانیم
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/462497" target="_blank">📅 19:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462496">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCIFICk-JJFMfjX9Agi8LPsCrThIwIQAVbzT6kDczZR0PGS4Xhm1CG1SbYl-vnitbVehalu8yWowxR86YFn6kE_3dg0s5WaoVfKl0d91yxx18EUrmkfvynLvd9YZQcocH6puO0iOVMEyNq5aWPziIuBEjSuACIAxS6AxwLEn3HT0iSlQH61Fch8a590_ahFuWROvPN2FEUkX7_KiqYY1X_ockEviavjkM9bQa-35Drlh4yZlwh7D-sST-39s8zdTVFnKmWdOjk6sLUxm-bCQCRJdEZcQU5Qj3geBf-eVNNZJpkTVLGArb8-s1W05JkOTyHYorFB-JyVwoTaImD-9tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: برابر مردم حاضر در میدان سر تعظیم فرود می‌آوریم
🔹
دویست شب حضور شما در صحنه، در کنار ایستادگی و جانفشانی نیروهای مسلح، جلوه‌ای از عزم و اراده ملتی است که در روزهای دشوار، ایران را تنها نمی‌گذارد و منافع ملی را با تمام وجود پاس می‌دارد.
🔹
دولت در کنار نیروهای مسلح و پشتیبان مجاهدت آنان برای دفاع از کیان کشور، با همان جدیت در کنار همه مردم ایران ایستاده است.
🔹
تأمین نیازهای ضروری، استمرار خدمات عمومی، حمایت از تولید و اشتغال و رسیدگی به مسائل معیشتی و اقتصادی مردم با جدیت بیشتری دنبال می‌شود.
🔹
در این روزهای حساس، بیش از هر زمان دیگری به همدلی و وفاق ملی نیاز داریم؛ نباید اجازه دهیم اختلافات، ما را از منافع ملی و آینده ایران غافل کند. دشمنان این سرزمین، انسجام و وحدت مردم را هدف گرفته‌اند.
🔹
از صمیم قلب از شما سپاسگزاریم و در برابر صبوری، بزرگواری و اعتماد شما سر تعظیم فرود می‌آوریم.
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/462496" target="_blank">📅 19:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462495">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVndIJ3vF6pGn1Fi8l9CfgSQ4yqF89LNmdW4W3B7taSJKQ9DVixwbjKSuli74Zdlv3q6nxOoJGhH6H5npvW6dtuEAcx1q3b-_ZcGLRf_1FDPqWfnpASh3_0O_YFH0gicVX1RBXsN1Ei5ZUIHTtClDFEEgopx4sX62KV18yXTqJDUZb8-ZxCR4RKZ47jQJNZayf_9rzwclIdMInktaa8VBPvCjeLPIh-EMBL4Yt582FFl5GlFhgBbLmroAIfDxPsEhNKx_a3duxwyVtGnxfwlrahcoDcoHndyCJKL8HnspWYYSybs4fbrrzt2vGA0L9AEOkarfCopBjONFQMJzp9m5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی سپاه: آمریکا به ویرایش تصاویر و ساختن روایت‌هایی به سبک هالیوود عادت دارد
🔹
بد نیست نگاهی هم به لاشۀ آن جنگندۀ اف ۱۵ که در ایران هدف قرار گرفته بود بیندازیم که قطعات آن با فرغون جمع‌آوری شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/462495" target="_blank">📅 19:38 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
