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
<img src="https://cdn4.telesco.pe/file/JnpM3YVN64uN6jPkbTswR9taA5G22TE8y8I3sAfvxEdY6j_c1uaoaU22rPRc1lOE2MZudya2H31X3V639shbgttLARl0clpa-YAHxYnqmSR3NSTKAH3ocM6WQgkZ2ViVd1mHZ1Kfxq0nGU_qumRrQ9shkixIMNjU_y-q2lqyKngGmyQ-rhsIPV_gTZexlhMmrodpd2ffcIpu9ZMN_ONxOfZxlQF7JLHVWUIlIakRDt6RI9wmx4fywRS9daTdvbDUvDKtcIaWDK4ipXqLFdJSDLe3gaqaOd7lnZ_Lw1aqqhpxL-MjQBMREYBHA5wKbrkZCdO2UtQUgP4Gs8wIbX80xA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.78M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 15:32:00</div>
<hr>

<div class="tg-post" id="msg-464346">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jxrc9To-ryJe0DT4GzkZ5iMQoW9bePPJ1QT8CNJFvXT9VxeWenoB32XzBPVzgtyobLbFVVYfgoLVE1XoHPub5YQHdm9QIowrp0jDMUj53vBGJfCCUOM2pc3PWPD4lygx3bLqDExkAt11kt87CHaLONj9GdB2sHHQoYJprrbrjFA1SRRYFkbnfkfBJTcx0PQ9kfsvbXhzbEiu7DjS5QRoEZDxg8qyGuNt12x1qNvlzUJzp2GQndTluB9BfIO6jGPdcP3LYp9pGLZdMbHvjK18PdIMcc1G3MBAZV5Z1ZHil0bc8uLxfF38iBR4kKSLH0OXq0XUAhy69Y7JxMhR3-YDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درهای هلند به‌روی کالاهای شهرک‌های صهیونیستی بسته شد
🔹
هلند با هدف جلوگیری از مشارکت اقتصادی در شهرک‌های صهیونیستی، واردات و تجارت کالاهای تولیدشده در این شهرک‌ها در کرانهٔ باختری، قدس شرقی و بلندی‌های جولان اشغالی را ممنوع کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/farsna/464346" target="_blank">📅 15:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464343">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آیا اصلاح‌طلبان جنگ سوم را هم به ایران تحمیل می‌کنند؟
🔹
در شرایطی که ایران ۲ بار در میانهٔ مذاکره هدف حمله قرار گرفته، دوباره همان نسخهٔ قدیمی روی میز آمده است: «صلح، مذاکره و تفاهم»؛ اصلاح‌طلبان مخالفان خود را به جنگ‌طلبی متهم می‌کنند و خود را در جایگاه مدافعان…</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farsna/464343" target="_blank">📅 15:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a3edf75e.mp4?token=WKIxPljhfYkRjuwFcjjBMuDzLnfhgTR0ifFYb-b-Od7x3oylKb55oaJe-thefWwtbfHdsMnRhychwvaEHaqW6Vwa_5UXWPNn867U-nv5MVvmauBIe6pS5bv3p8kGLsrXaSxbc6jGquKo26saHFLoe9IY5NSoyz06jriJ83gWlT-gBhrTvmpKNOGWMdTEnsMIqj7Azmf4u1ZDTgkGmw42dtzwahXHocvGsiFtwUJkTIDsjk7AXUwg_LaWtzs_uPclcRXoBeJwHSXuPOgCW6hinHIKaumLYmOpkUxXrSsZgY5cotsr8FESSKkFtb_r4z72xtNaAv3UPqzQEHwByW8HlGRM9Y-GyHy6NDE51vn0FMvc5WvttZ8Fsc0ZmGVkcM-1IH3h0AQDV_XDoBGvXMFUb2eEizvnHJR6JstmYQUeru2aAB5ZOqBSqiYdN3JwSIW9EQv6fTe0GeGQsnfvgqkNvpkVN6QorG9Uun8vilIVi6mqvCt-swd-Wz2SxdScv1DFqg2WSghZ2G6RDLpsXkCjdS0KCVi8eMeWzMQLbVbwjlLN4dXwZ9u-5FyqwlxnUeUHnCmGEe6cRSM5v049eqt9saZW1tYzbiiglXEvwM7YNGl6geC68GgRty_4lmljoZaRqqxeb3d1bXgNMSo2bwYqCj0sfh_QoVy5m2JFCOpOKCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a3edf75e.mp4?token=WKIxPljhfYkRjuwFcjjBMuDzLnfhgTR0ifFYb-b-Od7x3oylKb55oaJe-thefWwtbfHdsMnRhychwvaEHaqW6Vwa_5UXWPNn867U-nv5MVvmauBIe6pS5bv3p8kGLsrXaSxbc6jGquKo26saHFLoe9IY5NSoyz06jriJ83gWlT-gBhrTvmpKNOGWMdTEnsMIqj7Azmf4u1ZDTgkGmw42dtzwahXHocvGsiFtwUJkTIDsjk7AXUwg_LaWtzs_uPclcRXoBeJwHSXuPOgCW6hinHIKaumLYmOpkUxXrSsZgY5cotsr8FESSKkFtb_r4z72xtNaAv3UPqzQEHwByW8HlGRM9Y-GyHy6NDE51vn0FMvc5WvttZ8Fsc0ZmGVkcM-1IH3h0AQDV_XDoBGvXMFUb2eEizvnHJR6JstmYQUeru2aAB5ZOqBSqiYdN3JwSIW9EQv6fTe0GeGQsnfvgqkNvpkVN6QorG9Uun8vilIVi6mqvCt-swd-Wz2SxdScv1DFqg2WSghZ2G6RDLpsXkCjdS0KCVi8eMeWzMQLbVbwjlLN4dXwZ9u-5FyqwlxnUeUHnCmGEe6cRSM5v049eqt9saZW1tYzbiiglXEvwM7YNGl6geC68GgRty_4lmljoZaRqqxeb3d1bXgNMSo2bwYqCj0sfh_QoVy5m2JFCOpOKCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: جوان ما نباید از مسخره‌شدن بترسد
🔹
گاهی انسان به درست‌بودن یک کار یقین دارد اما به‌خاطر حرف و حدیث دیگران اقدام نمی‌کند؛ باید در برابر این فشارها مقاومت کرد و از کار درست عقب نکشید.
@Farsna</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/464342" target="_blank">📅 15:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uM_X8XKubodIaH14YP0ZTEGujEVHJRZVf7jSBf4KBfAQaKVd-guX87B3XiHhtzr7VHOuMk3Gfdsgnj-Dg9pY4A0TwL4byoYYMH6q_UvkqE9WT4aFytmVHryr9dyCbb3CWVNiCVm8wEs8C9fwOK2yFQUpymqYXzwls8oLfyg7_rqZ2ZTejgzywAF0oIo5mrxnmBG9sLWX9EuqBXNpl6ZTPBBkiWA53NIpvmWYR2TIWUVTYP60zmfSQ41Yy7yJj-2RlogVym60qm9zotcwTdnNdjITFblRBiLGocQc3xWzIGpN2yy8uQMcRT80RXSpP8NcCDinwebOvE1W3nKECCtohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کبدی‌کاران مردان مقتدرانه راهی فینال شدند
🔹
تیم ملی کبدی مردان کشورمان در دیدار مرحلهٔ نیمه‌نهایی بازی‌های آسیایی ناگویا مقابل چین‌تایپه با نتیجهٔ ۵۹ بر ۲۱ شکست داد و راهی فینال شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/farsna/464341" target="_blank">📅 14:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkrUdPzLFB-axttSQWpJldGK40_m_TNsUXoO1l1MrX1cIgKCgJAgucAd5krYtJ3YY_-azLAIwR0yHedvZqOFqNno-fzNn47lPMm6ZOezjAsA3NW5vZ0sQIpz0lbpIVqa0Uikl_b__ETo0sVi-TpUhuMget0E9WaMVGEWzo3LypKbEVfI0lPWje1-jlqmJEq9DL7hGkPPxJouk3OBfdnNvLvrzrbGLd_hAXJOdZjl87Y2bGimDttA7f9dxPU8CSQh2WoAb_45VzGLZJYC_Lb4nT-CIkZeDSiXgosyKmfmBWFcL-ubE0IiOGSkJFCYvwCq6dIJcP6oXV3-cIdk0iWAuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناتو: به اقدامات ترکیبی روسیه پاسخ می‌دهیم
🔹
روته، دبیرکل ناتو در مصاحبه با بلومبرگ: ما برنامه‌هایی را آماده کرده‌ایم. ما تمام گزینه‌های لازم برای واکنش را داریم. ولی آنها را علنی نخواهیم کرد. واکنش همیشه یکسان نخواهد بود، ولی ما قادر به دفاع از خود هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/464340" target="_blank">📅 14:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464339">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b79fffe84e.mp4?token=h8dz2hxuEqg-UXa2tUC8yb-FPdMDqHK5USCw-fD5We6mQbLmLaQ3PZqdrdmJTQ-R--olR0prLSA2YXxIj4qqX4zX0aCA8Pq6Dd-jUth1zNIjX20Li0IkHUL5l-LkVYuchnK685MJdMlQHYs88quwqDqVzLVR4nMFriUU4REZIoOwgsJBTZ0tI_ebG5-xiokMiyi8Mwq4yoK36AX8CME6z1axHgjMIl49u-NTogaWS4-lO1ZT5rwp6oEAHAQCODpyTxyBEXnyLCM3M0lGgRGWAovxrKTebjY_944Ls3mVCM0NDMnXOpnLY3bBrrReGCLWXszaY-eSpMKU2OIFDfQUEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b79fffe84e.mp4?token=h8dz2hxuEqg-UXa2tUC8yb-FPdMDqHK5USCw-fD5We6mQbLmLaQ3PZqdrdmJTQ-R--olR0prLSA2YXxIj4qqX4zX0aCA8Pq6Dd-jUth1zNIjX20Li0IkHUL5l-LkVYuchnK685MJdMlQHYs88quwqDqVzLVR4nMFriUU4REZIoOwgsJBTZ0tI_ebG5-xiokMiyi8Mwq4yoK36AX8CME6z1axHgjMIl49u-NTogaWS4-lO1ZT5rwp6oEAHAQCODpyTxyBEXnyLCM3M0lGgRGWAovxrKTebjY_944Ls3mVCM0NDMnXOpnLY3bBrrReGCLWXszaY-eSpMKU2OIFDfQUEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان دوران قهرمانی حمیدی با مقام ششم در ناگویا
🔹
محمدرضا حمیدی، ملی‌پوش ژیمناستیک هنری ایران، در فینال بارفیکس بازی‌های آسیایی ناگویا با کسب نمرهٔ ۱۲.۶۶۶ در جایگاه ششم قرار گرفت.
🔹
حمیدی پس‌از پایان رقابت خود از دنیای قهرمانی خداحافظی کرد و به دوران فعالیت حرفه‌ای خود در ژیمناستیک پایان داد.
@Farsna</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/farsna/464339" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szwKkbb7to2QDsAQ_HrxMfB-ZhPBOone1AEAls7wra4_5MawdYflygcl1TpYZzkH98hmSawPF4AEqJTCR_ftl_zGJ-TFSMTcfiixLLB8LKY69_09mXHKKfJKyeQW3yhAJvdF7RgX1gpGAgdKS6aD0b2EfOAZAtLc5D_MkCbX_RBdQtnhMRXIVTJK98cpzfZdAjAIIVqLjiF3vXGsKUtJHiBIRWcYCT4FaVhrXfT4O9W_pkAGd-aD_ZaDh7i-5VFXRG-K_Xj92TC_yeniKEzQHPl-4XuyPrQkaRj1jooxntQUeNZE53D5Ozse8X_r3-9n6mIedFShEsp_kqYghygvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال: بن‌سلمان خواستار ادامه محاصره دریایی ایران شد
🔹
وال‌استریت ژورنال گزارش داد، محمد بن‌سلمان، ولیعهد عربستان سعودی، اخیراً به مقامات آمریکایی گفته است که ایالات متحده باید محاصره دریایی علیه ایران را تا زمانی که تهران به امضای توافقی جدید وادار شود، ادامه دهد.
🔹
این موضع در حالی مطرح شده است که کشورهایی مانند قطر و عمان تلاش می‌کنند زمینه برگزاری دور جدید مذاکرات میان تهران و واشنگتن را فراهم کنند. قطر پیشنهادهایی از جمله یک وقفه هفت‌روزه در درگیری‌ها را پیگیری کرده که بر اساس آن، توقف حملات به کشتیرانی می‌تواند در ازای لغو محاصره دریایی آمریکا علیه ایران صورت گیرد.
🔹
با این حال، به گفته منابع وال‌استریت ژورنال، دولت آمریکا به قطر اعلام کرده است که ترامپ قصدی برای لغو تحریم یا محاصره دریایی ایران ندارد. یک مقام کاخ سفید نیز گفته است تحریم‌ها و محاصره دریایی، آمریکا را در موقعیت قدرتمندی در برابر ایران قرار داده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/464338" target="_blank">📅 14:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6075181b.mp4?token=ngcyRvGmDGVwOYGtVwzQdpEo0ujrDpSCSwp36HUOm6r8I6MgeJs9RVDSxktvKzJxFXR5atqh4oP97fyxoGbNgBDvjK-ciJT-ocrrmNa-Ytas5HQhJTRHqvl9pyqh3funC1anxlcR5plqIVLOeeGcCp9G5vEf3hmvpzTNO5jszX_hr68vPN5--ELXXkOqOv4JAcT8_9XwYIijfkgIbVSraKL0Voj7rn9R8_STmtGh_DfmGpBZJd12N0f2BQoVYC0icETLlLJle-iiBDiAWfsTywm6Ih1WudL4HGbQ-8QcmIyMsOO-C1Ry-XBXq-1dQn4tW94eEsFuc4dUyTkfefIw4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6075181b.mp4?token=ngcyRvGmDGVwOYGtVwzQdpEo0ujrDpSCSwp36HUOm6r8I6MgeJs9RVDSxktvKzJxFXR5atqh4oP97fyxoGbNgBDvjK-ciJT-ocrrmNa-Ytas5HQhJTRHqvl9pyqh3funC1anxlcR5plqIVLOeeGcCp9G5vEf3hmvpzTNO5jszX_hr68vPN5--ELXXkOqOv4JAcT8_9XwYIijfkgIbVSraKL0Voj7rn9R8_STmtGh_DfmGpBZJd12N0f2BQoVYC0icETLlLJle-iiBDiAWfsTywm6Ih1WudL4HGbQ-8QcmIyMsOO-C1Ry-XBXq-1dQn4tW94eEsFuc4dUyTkfefIw4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۴۰ هزار جان‌فدای تهرانی امروز با موتور به میدان آمدند  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/464337" target="_blank">📅 14:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464336">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u555rcsQaexKyMSxKG9PhioprFlZKvVX1mjrOy0KrybV3k8BWIZEFsmoNKY3v9BtEY2uKimFdvUsge3EdAYRlfTeqYB_F4XDTFouhdR3n_QXNI3qQXu6PFzLyY-QWQ_vdBnOWuOVrqPgtzesPff-3Ejb8O8ayc3NuH0L36ihLUce8lvgKnQ7316TcZ7AWzBQKrjwAoNiYexEbEHXrsBPBbccuLnMJKpt_FEIOBEKwMvd_5iaWgEFbIkEuUKoS9zBe9QYmIfOJIObxu5O7nOPv6mKre0zrnB1erPXomb39zul5jliCGkau-mqQS9pATJNLLQOmTumF-BfFczTbTVEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس
🔹
همسویی با آمریکا در اجرای سیاست‌های خصمانه در خاطر ملت ایران ماندگار خواهد بود؛ هر چند راهبرد ما در این مورد مشخص است؛ پرواز در منطقه یا برای همه آزاد است یا برای هیچکس.
🔹
اگر ایران امکان پرواز و دریافت خدمات فرودگاهی نداشته باشد، هیچ کشوری در منطقه هم این امکان را نخواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/464336" target="_blank">📅 14:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464335">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597aef5ec5.mp4?token=FApN4xGwemgFSNQjMCPvrw-6-juBDp0PQzyQ775kjjaa2ru7CkInjUe_xMLI81txMLV0_NAW2DZISDswADOK4B_MU1idc7DY1eUvSiW8zbaLa0DgD-daTC7FwRF1izLNrfellckZihPK0iMIC2F7nDHVoKw47CONjVg-Qy44MF7lIcHVJPDZT1XNxQ8hWWQheJU8pbUH_TOMyWK281MGZ6Ob-Q1sCJYnkAZTC-yzlYqcLe0Qfyny6IkO9WFN0RHIIBjOlU1PJsMFX-Xcfx4Zl2yFVGnw4pRvXPXcAZ-NhZaEFiDmyS7a0udZjsnelp11HG5suEuiXJyRbXvAa1O-XTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597aef5ec5.mp4?token=FApN4xGwemgFSNQjMCPvrw-6-juBDp0PQzyQ775kjjaa2ru7CkInjUe_xMLI81txMLV0_NAW2DZISDswADOK4B_MU1idc7DY1eUvSiW8zbaLa0DgD-daTC7FwRF1izLNrfellckZihPK0iMIC2F7nDHVoKw47CONjVg-Qy44MF7lIcHVJPDZT1XNxQ8hWWQheJU8pbUH_TOMyWK281MGZ6Ob-Q1sCJYnkAZTC-yzlYqcLe0Qfyny6IkO9WFN0RHIIBjOlU1PJsMFX-Xcfx4Zl2yFVGnw4pRvXPXcAZ-NhZaEFiDmyS7a0udZjsnelp11HG5suEuiXJyRbXvAa1O-XTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تفتیان به فینال نرسید
🔹
حسن تفتیان در نیمه‌نهایی مسابقات دوی ۱۰۰ متر با ثبت زمان ۱۰.۳۳ ثانیه در جایگاه چهارم قرار گرفت و موفق به صعود به فینال نشد.
@Farsna</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/464335" target="_blank">📅 14:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464334">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLDSkM02THX54iFTE3ZWaNw_p8KC4OeFZnm8vQn9MdHLORXJ4lYIft86-NLApbOUdH2XkyVMMKUxYZrdU6dHy-Z-4UnzV87tOTUMOwMm47YbS0HxIZOhtkXOzWYhHDo7XBZgoW8xKTkqqNX8ZoCudvu-3dftcj6dZwF7ZLbF0iE0FoDgNO1qplfr7ND3sFgFDWiqFIS1aNWzPAxvQKvzgOkhq4a-PyaCkAfjhdr8ePtea6xjI0A8Q8n4SCL7M6f8jvXOgIjaEIn06i9wO3Hv_ji-Sb-EqVzmJx8gHj2nm7ujl4icMdHA0ARZpVON4C16u3u5S05tOY8AIo2RTxfaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختران کبدی ایران فینالیست شدند
🔹
تیم کبدی زنان در مرحلهٔ نیمه‌نهایی مقابل چین تایپه با نتیجهٔ ۲۳ بر ۱۹ پیروز شد و راهی فینال شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/464334" target="_blank">📅 14:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464333">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsYy5VOlJteRkZMbqmBiAwpzlrwYIAYkDIf_E3UK7COkWWC5jyJxGRyTyNC4fRvS3JqIgN5tjYkvoY_FHaEMiHx7GY5FhgnPl_PA0I2WX00aF-IX1OPWKJki6EP42PUEDdwSyjSSykGHWWlFRHOeV1gnKRbDXMOOQgrF9tdAcF36PzZ8ydu_AC4-nmhqqckjPrefcSZmHabS9JSXeE3SJJ9VY42EBxHXs0syolKgjhMh9rbKZ1_CGmwypLMvJ_s4gR6NBw7qH6Euy20biLnVbOo8HWdbF_1mn4YbLNVVyZvUNPg7NGsjM0ac6KF0eq_a21BoXt3YGP7_D67SGuJxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهمت تقلب به دانش‌آموزان به علت اشتباهات نرم‌افزاری
🔹
آشکارسازهای هوش مصنوعی که برای شناسایی تقلب دانش‌آموزان و دانشجویان استفاده می‌شوند، در پژوهش‌های جدید با خطاهای قابل‌توجهی مواجه شده‌اند و در برخی موارد، متن کاملاً انسانی را به اشتباه تولیدشده توسط هوش مصنوعی تشخیص داده‌اند.
🔹
بررسی‌ها نشان می‌دهد این ابزارها منشأ واقعی متن را تشخیص نمی‌دهند و براساس ویژگی‌های آماری و سبک نگارش، احتمال تولید متن با هوش مصنوعی را محاسبه می‌کنند.
🔹
در یک آزمایش، یک متن کاملاً انسانی توسط ۵ ابزار تجاری از «صفر درصد» تا «۱۰۰ درصد» تولیدشده با هوش مصنوعی ارزیابی شد.
🔹
خطای این سامانه‌ها در مورد افرادی که انگلیسی زبان اول آنها نیست نیز بیشتر گزارش شده است؛ به‌طوری که در یک بررسی روی ۹۱ مقاله واقعی آزمون تافل، به‌طور میانگین ۶۱ درصد نوشته‌های انسانی به اشتباه تولیدشده با هوش مصنوعی تشخیص داده شدند.
🔹
به‌دنبال این مشکلات، دانشگاه‌هایی مانند واترلو کانادا و کیپ‌تاون استفاده از امتیاز تشخیص هوش مصنوعی ترنیتین را متوقف کرده‌اند و بر استفاده از شواهدی مانند پیش‌نویس‌ها، تاریخچهٔ ویرایش، روند یادگیری و گفت‌وگو با دانش‌آموز یا دانشجو تأکید کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/464333" target="_blank">📅 14:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464332">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D36hIUy7lxQeb62-S1iQ1vRMjpey08cyc5oY2c2IV9tOJxnIXBDAekLltbzG_dqQYEXbPzV0UtwRR169-uYASzAY2IFkuqf7tQZf184EM3BeYZP6MjRen1beR8ftUMlhQsr_usZ56cQWo2PxrcL8MI3xICk4Wa1IaiVAgKR-ndN0zCnJ7MaAKmr_fCIDeERt8DPRCv50FjhL1LRHMoV-JHkOc4uuZxdUw6Uwr0zdM3hQcCAkMa9o7U1y6qXNMsACa1-HtRs0ESHODmNcbZb_Ak73jGpsTza4MoXH_S1L4SM539GY0hDSe8z8GitbM2rJzY_R3EfaQjurTgXmgZF2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علائم کرونا با آنفلوآنزا چه تفاوتی دارد؟
🔹
کرونا و آنفلوآنزا هر ۲ بیماری‌های تنفسی هستند و علائم مشترکی مانند تب، سرفه، گلودرد، خستگی، سردرد و بدن‌درد دارند؛ اما تشخیص دقیق آنها تنها براساس علائم امکان‌پذیر نیست و در موارد لازم به بررسی پزشکی و تست نیاز است.
🔹
دورهٔ نهفتگی کرونا معمولا طولانی‌تر است و علائم می‌تواند ۲ تا ۱۴ روز پس‌از ورود ویروس ظاهر شود، درحالی‌که علائم آنفلوآنزا معمولا یک تا ۴ روز پس‌از ابتلا بروز می‌کند.
🔹
از علائم کرونا می‌توان به تنگی نفس، درد عضلانی، گرفتگی یا آبریزش بینی، تهوع یا اسهال و در برخی موارد ازدست‌دادن بویایی و چشایی اشاره کرد.
🔹
آنفلوآنزا نیز معمولا با شروع ناگهانی تب و لرز، سرفه، خستگی، بدن‌درد، سردرد، آبریزش بینی و گلودرد همراه است و علائم گوارشی در کودکان شایع‌تر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/464332" target="_blank">📅 13:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464331">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJzEVgTN5knUPjPK8pBYtc6VdbSMsONyDJHM5vOvYSDqhLLMei1Klml9NRVHJYVoHGkQXZWkDDHKI-T36SWroAvPCLBYXKw9WP36JO8DluQO_F7oHGcT1z5Svbgp4tFTQAlO2Z_TpjjkGPOvtNipvnE4D1IBnQ-YfWUZGaDeIBY9VydLp7fFFQmk7gMPFqFQRWXXfMVfi6a2VV3UlBGGHxEB2vTgNYjBvZvF9Wus1zJV-96mbmknmhddWgj05cay--OahLBYV5fjlmvx24nNjP_8dt9RN01ov1gkVJ1FmvOGUg8GDk5elZEo3B-3HyXbnscNO9SbOHTGWkkMMt2IQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:تمام شیاطین در برابر ملت ایران صف کشیدند، اما درس عبرت گرفتند
🔹
رئیس‌مجلس در دیدار با خانوادهٔ رئیس شهید سازمان بسیج: تا زمانی که جان در بدن داریم، تلاش و مجاهدتمان برای پیروزی و موفقیت جبههٔ اسلام است.
🔹
در این جنگ ترکیبی، اقتصادی، نظامی و فرهنگی، از تمام لحاظ و ابعاد، به تمام معنا تمام شیاطین جمع شده و مقابل مردم ایران قرار گرفته‌اند.
🔹
دشمن با تمام توان آمد اما به برکت شهدا، امام شهیدمان و همت و غیرت نیروهای مسلح و مردم عزیز توانستیم درس خوبی به‌دشمن بدهیم.
🔹
به‌لطف خدا و تحت رهبری مقام معظم رهبری، ملت از خطرات و فتنه‌هایی که وجود دارد، عبور خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/464331" target="_blank">📅 13:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464330">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f9304a3d.mp4?token=RhayQ1d98mBQJSL636N_cak4CeIBVW-YrC2ykaBanw4qBpHE9E3LaxmCRBToxLgKv98GrYDrpqE52TZ6kQaT0L-DYSDDX422SApu5RFSplRkYJFVLvmeJx51CNtOZL7IFhgT5YGhyLnWl4HvMabIAj5qY7vLp4j6Ftngz4LvtfwyfrMlSysHWdMe85GwEs9Wb0FZk_dNIXPH3ciQJtI-s8sRN8f7omGAwrPl7fPHUTPUpnE4pwLTo1l64-PI9VJ49WjzARKIxm2ZDkUevzXjsP2qs_vLWHJsrFmxKT0MOoY1HVW-9g7BhU8uqnflmuuEl8k4rhGj0d3-0e6DaccUmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f9304a3d.mp4?token=RhayQ1d98mBQJSL636N_cak4CeIBVW-YrC2ykaBanw4qBpHE9E3LaxmCRBToxLgKv98GrYDrpqE52TZ6kQaT0L-DYSDDX422SApu5RFSplRkYJFVLvmeJx51CNtOZL7IFhgT5YGhyLnWl4HvMabIAj5qY7vLp4j6Ftngz4LvtfwyfrMlSysHWdMe85GwEs9Wb0FZk_dNIXPH3ciQJtI-s8sRN8f7omGAwrPl7fPHUTPUpnE4pwLTo1l64-PI9VJ49WjzARKIxm2ZDkUevzXjsP2qs_vLWHJsrFmxKT0MOoY1HVW-9g7BhU8uqnflmuuEl8k4rhGj0d3-0e6DaccUmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌زمان با آغاز سخنرانی نتانیاهو، سران کشورهای مختلف سالن سازمان ملل را ترک کردند  @Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/464330" target="_blank">📅 13:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464329">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YR9vvRI8LQcXFmGC7gkPVvYQ9GSVpXaWTb5zPUkUaNXS7V9rO_Z9CdqX7qXZS789f8nRM71ShIR7mY4SGFKD4cCUDpRBgWjQZHj_o3r0UEXt0XiOiwaFJI2PjF__46tyo_Zr_hVNpAOwTbO4q68NXXApl945UOszGSSIPcp1rjYcsVjuOyj43NkJlPIXT2IwessPbqQfTnp3dJ-moSfD7KrrZ6JgPkZnMq7XB6OwwAQjD8SiuSpeyiYhoxeqYswbPeXaSHRdhhsbWTJQJhmKC_EV8Dfea9aYyHInMkZRKpTTtkSXQJdg8nX1_Po5E3GSy9tD7xsZp1F2RMtCRAZJRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد ناطق‌نوری درگذشت
🔹
احمد ناطق‌نوری، رئیس اسبق فدراسیون بوکس و نمایندهٔ ۷ دورهٔ مجلس، بامداد امروز پس از سال‌ها تحمل بیماری، در ۸۹ سالگی درگذشت.
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/464329" target="_blank">📅 13:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464328">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFlvcbRYa8Q7xZfagGYX_LuNe6Oa2_okoxPsdbhv4W0DqVEQzgpZYSC5Htl9Y2FcLFjUy--9fQyLlroYuyVx4NA12NGYgEYJklHLtWQ_22XNCU7fV1obN6Nha7tdf7m_wV_lstp4FlKS-pNhQHK9mP1MUT__WMtTaWvK3FaDvuQBWQf0LYl6C3Umggcmc_GRjPIrl88Dp-oF-F__Hrugi63Pnj2H2tstyh2lr19Reb9WSTwjeJT-vE3gXjwqzi-1O12NMFyAgbLCQte4fIQVgpY0PKvDgsXGj_esnPS5Yd7aR-tcMi1hRJutwJvoBZKTihF_r5-hsshKOcV2Ai1ugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسکتبال ۳ نفرهٔ ایران به فینال نرسید
🔹
تیم ملی بسکتبال ۳ نفرهٔ مردان ایران در مرحلهٔ نیمه‌نهایی بازی‌های آسیایی ناگویا مقابل قطر با نتیجه ۱۴ بر ۱۱ شکست خورد و از صعود به دیدار فینال بازماند.
🔹
ایران در دیدار رده‌بندی به مصاف فیلیپین می‌رود. @Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/464328" target="_blank">📅 13:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464327">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrAH9NC7znmI8EbWF_wWaVI8nEm4PtKJFU0EvAyDjSGdZj2DgpCxRJkXblqTntevBv45SFlplun6G9l84nu3mz4Gb-PCuv6eZZJvYpJ2871X9ihhF8hmSs_L_gfmRkaFNW9aPb8T1p6hx000KcEgs850phuaaG1bWtx6ZTm7AsqHOdVRUOKQmQ1kVKZsRTgLhzhNy3RTZmSTgaHUUGMLRlEAW1mkZgqXMx-MYj8QI7FwxuO2HNVLuGRUfH16pzpznYF7qS5xXD7o0HjiBB7wqu7o7dC43rlcMej9eSWiAZZgKSrE75GWRUV6WEv_zvF7VNEbL6e4HoMayvcZNXEBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پزشکیان: صلحی که برای همه نباشد صلح نیست؛ سخنان دیروز رئیس‌جمهور آمریکا نشانۀ بارز خوی قُلدری است
🔹
ترامپ باید بداند ملت ایران در برابر زور سر خم نخواهد کرد و متجاوزان را پشیمان خواهد کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/464327" target="_blank">📅 13:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464326">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دستگیری عامل آتش‌زدن مسجد تهران
‌
پارس یزد
🔹
فرمانده انتظامی یزد: یکی از عاملان اصلی آتش‌سوزی مسجدی در تهران‌پارس و همچنین اخلال در نظم عمومی در اغتشاشات دی‌ماه دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/464326" target="_blank">📅 13:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464325">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تازه‌ترین اقدام خصمانۀ آمریکا علیه خبرگزاری فارس
🔹
در تازه‌ترین اقدام خصمانه علیه رسانه‌های ایرانی، آمریکا با اعمال تحریم جدید، صدور گواهی امنیتی (SSL) برای وب‌سایت خبرگزاری فارس را مسدود کرده است. این اقدام که به اختلال در دسترسی کاربران و حذف تدریجی اخبار…</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/464325" target="_blank">📅 13:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464324">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/928b856951.mp4?token=G_f01vRnL6yQQmVozxfa4KTgmowSkQxuiwfS4HSobTW4HT6rlBfjX2llbGYj3-CuLnnd_si0Cin0nEEH-xnIi6yHHBl4a4vqFvZbmMIDztjsTc_iR5FYP1qrqA6NKq97Io8IWDOe8nSEF8Eqh16mzWew5mJX-ieFFtsIpi9ExQE9puHwSyTxHsZNzTa9WUBk4tYBUy5bpoJeaRqFHIN49JJeUwEFhNtcR-f86Z6TZv_lrECHAqliyfectY_meeoq9P0ySZuiVZdlvbKjlzPZDr5mYffHWorE6jttaM3f_OYUAiB1_zUgpt_k9lXtXyOViSJyF47QPKUD6fQdgw4EFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/928b856951.mp4?token=G_f01vRnL6yQQmVozxfa4KTgmowSkQxuiwfS4HSobTW4HT6rlBfjX2llbGYj3-CuLnnd_si0Cin0nEEH-xnIi6yHHBl4a4vqFvZbmMIDztjsTc_iR5FYP1qrqA6NKq97Io8IWDOe8nSEF8Eqh16mzWew5mJX-ieFFtsIpi9ExQE9puHwSyTxHsZNzTa9WUBk4tYBUy5bpoJeaRqFHIN49JJeUwEFhNtcR-f86Z6TZv_lrECHAqliyfectY_meeoq9P0ySZuiVZdlvbKjlzPZDr5mYffHWorE6jttaM3f_OYUAiB1_zUgpt_k9lXtXyOViSJyF47QPKUD6fQdgw4EFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا  پیروزی برادران عالمیان برابر قزاقستان
🔹
در مرحلۀ یک شانزدهم‌نهایی رقابت‌های دوبل تنیس روی میز دوبل ایران به مصاف قزاقستان رفت.
🔹
در این دیدار تیم ایران متشکل از نوشاد و نیما عالمیان برابر تیم دوبل قزاقستان قرار گرفت و با نتیجه ۳ بر…</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/464324" target="_blank">📅 12:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464323">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آیا اصلاح‌طلبان جنگ سوم را هم به ایران تحمیل می‌کنند؟
🔹
در شرایطی که ایران ۲ بار در میانهٔ مذاکره هدف حمله قرار گرفته، دوباره همان نسخهٔ قدیمی روی میز آمده است: «صلح، مذاکره و تفاهم»؛ اصلاح‌طلبان مخالفان خود را به جنگ‌طلبی متهم می‌کنند و خود را در جایگاه مدافعان صلح می‌نشانند.
🖼
اما هنوز به یک سؤال روشن پاسخ نمی‌دهند: دقیقاً قرار است بر سر چه چیزی مذاکره کنیم و چه چیزی بدهیم تا دشمن حمله نکند؟
🔹
در ایران هیچ عقل سلیمی مخالف با صلح نیست؛ اما واضح است که تکرار کلمهٔ «صلح» جای پاسخ به این سؤال را نمی‌گیرد که طرف مقابل با چه امتیازی حاضر است دست از فشار و حمله به ایران بردارد.
🔹
اگر پاسخ، پروندهٔ هسته‌ای است، این مسیر پیش‌از جنگ نیز آزموده شد. سخن از تعلیق فعالیت هسته‌ای و حتی صرف‌نظر کردن از ۴۰۰ کیلوگرم اورانیوم مطرح شد. نتیجه چه بود؟ حمله انجام شد.
🔹
پس در شرایطی که عقب‌نشینی در موضوع هسته‌ای نیز مانع حمله نشد، نسخهٔ بعدی چیست؟ چه امتیاز دیگری باید داده شود؟ و اساساً نقطه پایان این امتیازخواهی کجاست؟
🔹
با این حال، بخشی‌از جریان اصلاح‌طلب به‌جای پاسخ روشن به این پرسش‌ها، مسئله را به یک دوقطبی داخلی تبدیل کرده است: یک طرف «صلح‌طلب» و طرف دیگر «جنگ‌طلب». گویی صرف گفتن مذاکره مساوی صلح است و هرکس درباره نتیجهٔ مذاکره و تضمین طرف مقابل سؤال کند، خواهان جنگ است.
🔹
واضح است که این دوقطبی‌سازی خواسته یا ناخواسته مسیر دشمن را هموار می‌کند و می‌تواند بخشی از مسئلهٔ امنیتی کشور باشد.
🔹
جنگ فقط با شلیک اولین موشک آغاز نمی‌شود. ایجاد شکاف در داخل، القای عجز در برابر تحریم و ارسال این پیام که ایران از درگیری می‌ترسد و با افزایش فشار حاضر به عقب‌نشینی بیشتر خواهد شد، می‌تواند دشمن را به این جمع‌بندی برساند که فشار و حمله هزینه ندارد و حتی امتیازآور است.
🔹
وقتی دشمن احساس کند جامعهٔ ایران از درون دچار اختلاف شده، بخشی‌از فضای سیاسی کشور دائماً از ناتوانی در برابر تحریم سخن می‌گوید و برای جلوگیری از جنگ آماده عقب‌نشینی بیشتر است، چرا باید از افزایش فشار منصرف شود؟
🔹
اینجا دیگر نمی‌توان پشت واژه‌های زیبای «صلح» و «تفاهم» متوقف ماند.
🔸
اصلاح‌طلبانی که این نسخه را پیشنهاد می‌کنند باید صریح پاسخ دهند:
بعد از ۲ تجربهٔ قبلی‌شان، چه تضمینی وجود دارد که عقب‌نشینی و اعلام آمادگی برای امتیاز بیشتر، جلوی جنگ سوم را بگیرد و نه اینکه دشمن را برای حمله بعدی جری‌تر کند؟
🔹
اگر نسخه‌ای ۲ بار نتوانسته مانع حمله شود، اصرار بر همان نسخه برای بار سوم نیازمند توضیح است.
🔸
و سؤال مهم‌تر: آیا واقعاً متوجه نیستند که دوقطبی‌سازی داخلی، برجسته‌کردن عجز در برابر تحریم و نمایش ترس از جنگ می‌تواند دشمن را به فشار و حملهٔ بیشتر ترغیب کند؟
🔹
اگر متوجه نیستند، باید از میزان درک آنان برای ادارهٔ کشور ترسید.
🔸
و اگر متوجه‌اند، پرسش بسیار جدی‌تر می‌شود: چرا همچنان بر مسیری اصرار دارند که ممکن است به‌جای جلوگیری از جنگ، زمینهٔ تحمیل جنگ سوم به ایران را فراهم کند؟
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/464323" target="_blank">📅 12:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464322">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پلیس‌راه مازندران: جاده‌های کندوان و هراز بعدازظهر امروز یک‌طرفه می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/464322" target="_blank">📅 12:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464321">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9S4zuXWs3MHYOqlAMUCiaxr9kcx6PgmCZK9Oz7pJmIKDm59k8cRIEK0qoEV38FM8RhoGpuk76lsLDk2fgHdiMh9x2dHwpc2e5pLfWcOlGMnaOFif9hPi5ezVNXULj9Iyccnpt6DNhrAQh9VfZIFbY9vV6oEKftW4WQoYL74ktIzXhNHzVCytvWliYxA2BTwn4LWuQnDkocm1YUlmvnHCHw84luBU60e3n4QOBRIbIEtgK63pNWghHFsoyvnv9oyS_IRffrCUAII-pYzYEOTezLfIm_Hn7o3-_GwfQTZpsqshnrZTCNpUdn5suBSl90zr39OkcBWBNltF25DmeEYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه: فقط ما گزینه‌های پایان جنگ اوکراین را تعیین می‌کنیم
🔹
میروشینکف، سفیر وزارت خارجهٔ روسیه: غرب در تلاش است تا با مذاکره، وقفه‌ای در جنگ اوکراین ایجاد کند تا رژیم‌ کی‌یف دوباره مسلح شود.
🔹
اما فقط روسیه گزینه‌های پایان جنگ را تعیین می‌کند و هرچیز دیگری صرفا بهانه‌ای برای مذاکره در جهت توقف درگیری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/464321" target="_blank">📅 12:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464320">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTpv2L9Qq1bH1TcOsUdnB9tZ9rXbZ1Xy6csYfZe6eggvpy0JWjFZttMDkcCcsb2hiC6dVtbP1ctBCiivPVm27Goky4YBTjYvjeB5MtlPcAkx-k6r30QfPRUQL0JrSc2vEEbuU_f9tCU9BlvJi8cemFTuA-BANcqlgM7MWB_dB8fulpEVW8LukEEm-Q3a4ZfzxDcKScc3L1bSVGHNB8oyibHcDasYwIjnhdfwkjpTwnDaLTHqFqAgfUczrgqmKkT5SVTYIq6Sq4KUgoS5QjZd9gsx1oopbVeUVX_hnpUmnaa1KkTfNpedEuiTue8fzJPCLPvOCiHqXudKW_HRSQYuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۴ ریشتر در عمق ۸ کیلومتری، سفیددشت اصفهان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/464320" target="_blank">📅 12:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464319">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fa08c9f8.mp4?token=ODo6NaNzXgQycq-LILbYYe0-FPNmwgIy-05WskSo4HPKHjkXob5T87XA8GXTw-nviBM85Z8HryScxkdHg5D-mHcAYRQbIQE9xzRynON8lBZVmQN2l8gHmNYwxbfzKk09Ay0HtspAhrJgKj1lhF1WxdFiLmLMMCAD3Y6yejHBlK_7gEUbrApWUy4EppCLWGYQdWEtC3-ceDPkfCxk50_TIWyuusSyx5Sf9mCq46Ibt_JktKdPgQuwLHFQ-OlasCs7T45UwaaVMF4Y_oc6cpmwbJ8JH9QtMovZuGeP4TSNsI-4I5r9jp0JM8Y-kQqXIdK3zEO-_IUSTisRlb-5-fo4MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fa08c9f8.mp4?token=ODo6NaNzXgQycq-LILbYYe0-FPNmwgIy-05WskSo4HPKHjkXob5T87XA8GXTw-nviBM85Z8HryScxkdHg5D-mHcAYRQbIQE9xzRynON8lBZVmQN2l8gHmNYwxbfzKk09Ay0HtspAhrJgKj1lhF1WxdFiLmLMMCAD3Y6yejHBlK_7gEUbrApWUy4EppCLWGYQdWEtC3-ceDPkfCxk50_TIWyuusSyx5Sf9mCq46Ibt_JktKdPgQuwLHFQ-OlasCs7T45UwaaVMF4Y_oc6cpmwbJ8JH9QtMovZuGeP4TSNsI-4I5r9jp0JM8Y-kQqXIdK3zEO-_IUSTisRlb-5-fo4MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران طلسم ۱۶سالۀ فینال شنای آسیا را شکست
🔹
هومر عباسی در شنای پنجاه متر کرال پشت با ثبت رکورد ۲۵.۳۷ثانیه در رتبه ۹ قرار گرفت و به فینال صعود کرد.
🔸
امیر مطاعی نیز در مرحلۀ مقدماتی ۱۰۰ متر قورباغه مردان با ثبت زمان ۱ دقیقه و ۶۶ صدم‌ثانیه در جایگاه هشتم قرار…</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/464319" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464317">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بازداشت متهم مخل نظام ارزی کشور در پیرانشهر
🔹
رئیس دادگستری آذربایجان‌غربی: متهم یک پروندهٔ ارزی با ۴۲ میلیون یورو تعهد ارزی رفع‌نشده، در پیرانشهر دستگیر شد.
🔹
برای این متهم همچنین پروندهٔ فرار مالیاتی به ارزش ۵۴ میلیارد تومان تشکیل شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/464317" target="_blank">📅 11:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464316">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8066ae876a.mp4?token=QQQcfwlLG56wF--PCQSQog0HY-DuHuRENHmMAY5tXMpnW0WoHCKew4qJTkOK_aH7ixb8wSc_ZZ9lZrmlP2vnkE5vRoVkb1XhAh8pUMsNNFWB3gOi774wrQ_MDOa5MOg3Re0gObE-bfKBCD6a1z9I_f79tgT7C8GXBL5VZWWkjj-xKi2yi4yC3uvD399QFw2-tLUya7GL6Gt1td6y5xtlyujTXfmMLqc4U5Hdpw7S4gZlZF08K6hHIEwLjzFIwSRDkWzpCglItbKyFGXT2cVOh1Ip2g4vODcLdOdEI_oKY4hhHM0cV6lH8QfUCHg7xoUBakcjWSmKb0yKHI9BQ3-F2p8XHgcIsLuiet039m5853Ox4GMp81gc_TMtc2p-7F7HLH6AkSE6ruu4otZ-NOsflEcVN3cgpLWY4CIk9NZIHhFvzoN78Hvc4RhBmlhvw9ch1No66zVHENfo4P8kUq5iqpYGNxU6JaqoBZZQHfoteEAT_I0DLD04Jj6at6tXcR1gIgnD0KEFJ9nk7E4hwp0EPUvAMrVuBOwSRRg8ag7c9Im0zYxSAXYRH146uUFdOP31xA9XPm5aARKSHhOiEIZ7PYoOBaW7lBcm-194B4zw84maFxdJrMwo1L9MF7kCjbPIcJoImbXxH7zDDiVlqolvknXr3Y2XfMcgGXJfbfngKVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8066ae876a.mp4?token=QQQcfwlLG56wF--PCQSQog0HY-DuHuRENHmMAY5tXMpnW0WoHCKew4qJTkOK_aH7ixb8wSc_ZZ9lZrmlP2vnkE5vRoVkb1XhAh8pUMsNNFWB3gOi774wrQ_MDOa5MOg3Re0gObE-bfKBCD6a1z9I_f79tgT7C8GXBL5VZWWkjj-xKi2yi4yC3uvD399QFw2-tLUya7GL6Gt1td6y5xtlyujTXfmMLqc4U5Hdpw7S4gZlZF08K6hHIEwLjzFIwSRDkWzpCglItbKyFGXT2cVOh1Ip2g4vODcLdOdEI_oKY4hhHM0cV6lH8QfUCHg7xoUBakcjWSmKb0yKHI9BQ3-F2p8XHgcIsLuiet039m5853Ox4GMp81gc_TMtc2p-7F7HLH6AkSE6ruu4otZ-NOsflEcVN3cgpLWY4CIk9NZIHhFvzoN78Hvc4RhBmlhvw9ch1No66zVHENfo4P8kUq5iqpYGNxU6JaqoBZZQHfoteEAT_I0DLD04Jj6at6tXcR1gIgnD0KEFJ9nk7E4hwp0EPUvAMrVuBOwSRRg8ag7c9Im0zYxSAXYRH146uUFdOP31xA9XPm5aARKSHhOiEIZ7PYoOBaW7lBcm-194B4zw84maFxdJrMwo1L9MF7kCjbPIcJoImbXxH7zDDiVlqolvknXr3Y2XfMcgGXJfbfngKVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواپیمای ایرانی محدودیت هوایی آمریکا را دور زد
🔹
روز گذشته هواپیمای شرکت وارش به علت محدودیت هواپیمایی کشور واسط برای رسیدن به تاجیکستان یعنی ترکمنستان، مجبور به بازگشت به فرودگاه امام‌خمینی شده بود.
🔹
حالا خلبان این هواپیما در ویدئوی منتشرشده عنوان کرد که با همکاری‌ها و بررسی شرایط، انجام مجدد این پرواز به مقصد تاجیکستان موفقیت آمیز بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464316" target="_blank">📅 11:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464315">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la0gieV_6Z6yRNfACQczYbMGBatxpHo-A21ZHLZfc-l93d0JmfF5moznUuv9p26az9rZ_32U9H9XEYjjEKX5uOwY_azW_iCKGIZatqhI74XS21-zJj4o9JJElhSDnVGbJuYCxThdowJEryEAS6GmoI7PZdTT6LEAOj2Sn1H8504MHLmwfqekssm7n2UY3UpyWiFf_NpcnGjaIhB6tGxsXKQ0UFu1lXbWW6sKJdR4xmcG9HvbO_3PvrRBV1ElxDUI8QYbfL-ywNN_0eriH7osSCnQZF3nb_YpJpB0qC4zj8wLe0eYxnTBKCCbpJzCOOkaZSEI1EEhJ6QwmtR0E4-3-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبانیز: جنگ با ایران تأثیر ویرانگری بر اقتصاد جهانی گذاشته است
🔹
نخست‌وزیر استرالیا در سخنرانی خود در مجمع عمومی سازمان ملل متحد، با اشاره به جنگ علیه ایران و پیامدهای آن، خواستار اقدام فوری بین‌المللی برای پایان دادن به این درگیری شد.
🔹
آنتونی آلبانیز تأکید کرد که جنگ(علیه) ایران «ضربه سنگینی به خاورمیانه وارد کرده» و «تأثیر ویرانگری بر اقتصاد جهانی» داشته است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/464315" target="_blank">📅 11:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464314">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lv227mFqFgsgsgdloU4p_UCM9NhbOQNCIV0bxQ1tul11rsnTWXFImnVeoxjwW2h5iHDQFQC6rjzVn1lKPESEHMTUup64HSjN7wNDGWXZ4dl4X99fHs40g6c8whUS5xn_rNm1yL-qPOEjF9xomIRnBMVYfqMlv3RpZGnsIjuYxua1H7GxAb2I8mHwC73jyC23YWGHmItltLlWU_KVxUWW5wqDlaHby0Lkz21_1mLX4MnXEZvji6df9-fn3JIzhD_gWlcEE0x2KNp2bWGCASIiKhBgkRbq_Si3b2DJlwfcHKspqVR1XltXg-xpdBAW_mSf8V0SYY003q0TclbAZHAeeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
افشین خانی در مراسم آغاز سال تحصیلی مدرسه استثنایی پویا تأکید کرد؛
✅
بانک صادرات ایران در کنار کودکان استثنایی خواهد بود
🔻
همزمان با آغاز سال تحصیلی جدید، افشین خانی، مدیرعامل بانک صادرات ایران، با حضور در مدرسه پسرانه استثنایی پویا، زنگ بازگشایی و آغاز سال تحصیلی این مدرسه را به صدا درآورد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/464314" target="_blank">📅 11:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464313">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLqC7S8r9Jb53TOpFZb3Xw_6FDuA9-IN_Wo2uKP7ZsInsjjp_9IS6oGHwFUJFVRlmrwCQz_-H-SQILl6S2cEHAqgQoguBRkYXqeju2egcPiECp-uWk8SUcT3SwW-7tvqF58pAD6nD22mIcIcFM-etE0hcntei6IKbgusgOoXnelVm0GYhowLvl12vf66iK7F0Uk8rYRzcW1_86p7z-OPHb3CC7zVfNLf8EdrEHJsEwPzuslQ9kb8AvaTtCAKw5FSAjqsdGpxgu3LicQeBCOQXH1SGngoYCrB99xFkmqdLsUr2NKdus_Z6UgGZ6ZVAdAn8flgWDei3XWe1M_aDoe2MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❇️
سالن مبله برای ختم
❇️
❇️
همایش های آموزشی
❇️
🔹
۷۰۰ صندلی
🔸
پارکینگ وسیع
🔹
تهیه بسته پذیرایی
🔸
هماهنگی واعظ و مداح
🔹
گل مصنوعی به نفع خیریه
🔸
سرو ناهار و شام در سالن
🔹
فیلمبرداری مراسم و صوت با کیفیت
🔸
دسترسی آسان به بزرگراه
شهید همت، شهید حکیم، شهید فهمیده(کرج)
📲
۰۹۱۰۲۲۷۷۱۹۹
☎️
۰۲۱۴۴۰۰۴۰۴۰
📣
امکان رزرو شبستان مسجد
📌
آدرس مسجد
🔻
فلکه دوم صادقیه،بزرگراه شهید اشرفی اصفهانی ره ، جنب بوستان صبا
🔸
مسجدجامع‌امام‌سجاد(علیه السلام)</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/464313" target="_blank">📅 11:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464312">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/464312" target="_blank">📅 11:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464310">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb50f1dd8f.mp4?token=TjIzxhoUWTYit5BMkW3AuUJkgLuagGz5iJbHKOF88dt_kv9x0m2URg1w7SGOPPzpLxWwkiQSzOa4ElwFTfelFDvAInHZNYLsa56-3xTjiLRSQgClKT8lHoRVXrLZY0BNhL5QJsJzX3TfFnxwtcbSQWk1EjsLBdZvalIvzFEjpbJi9He2q_sdt8S6KjBJMujp9IIfa5Ul38q9YMR-7N0Ym0Aq5n2DWAFSDewchtgc2O9rdRSnRcBLI9so6vcSc2CGgRb_bpZtaYn3J5rOQI9qj4-y9sbam8FZ-_FjIhWc5xu3-D1Tu07BE7-Wm5Qa52_O37EV_FFstCL0IHc3VUfnZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb50f1dd8f.mp4?token=TjIzxhoUWTYit5BMkW3AuUJkgLuagGz5iJbHKOF88dt_kv9x0m2URg1w7SGOPPzpLxWwkiQSzOa4ElwFTfelFDvAInHZNYLsa56-3xTjiLRSQgClKT8lHoRVXrLZY0BNhL5QJsJzX3TfFnxwtcbSQWk1EjsLBdZvalIvzFEjpbJi9He2q_sdt8S6KjBJMujp9IIfa5Ul38q9YMR-7N0Ym0Aq5n2DWAFSDewchtgc2O9rdRSnRcBLI9so6vcSc2CGgRb_bpZtaYn3J5rOQI9qj4-y9sbam8FZ-_FjIhWc5xu3-D1Tu07BE7-Wm5Qa52_O37EV_FFstCL0IHc3VUfnZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات پهپادی اوکراین به زیرساخت‌های صنعتی روسیه
🔹
ارتش اوکراین بامداد امروز چند تأسیسات صنعتی مهم روسیه را در شهرهای پرم، ورونژ، روستوف و اولیانوفسک با پهپاد هدف قرار داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/464310" target="_blank">📅 11:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464309">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKjTstHw9iUxYd1plhlQVx9QJPyZLntCSy-7X6AqNsoacjjfQr9Ul0eIRLQZAEmOvFpvW2kPYNJmrzw6aOtFvJZo1lrv5cJ8Y091EcNWKcvYy7EVpoWDsrhkhRRBm-1iSblgcHSYiBwKMVxyQf_psiuY5JeYVRQMG61h6nJ4xip-F9CdVoA9pb2mH6Y7H-XIG4jASBaPGXjMDIiFb78NFwI-wwJfNOs5xjS1TFs4WyhNyAvsZS1_x7B2wXgHw4EXobiCsWmFNlTNPxOT4P1aBK6K-AG3k0E571dUIOBHV1-qmeNt1upfEvHmca2soltqgvZoFi2qsbmbVWVSd3sYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محیطی‌زاده دیسکالیفه شد
🔹
فاطمه محیطی‌زاده نمایندهٔ کشورمان در مادهٔ هفتگانهٔ دوومیدانی مسابقات آسیایی ناگویا در بخش پرتاب نیزه، به‌دلیل استاندارد‌نبودن کفش‌هایش دیسکالیفه شد و از جدول مسابقات کنار رفت. @Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/464309" target="_blank">📅 11:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464308">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fee158717.mp4?token=Bn8CGjnVgQYAYusivf-5izKXZEhRENk6pr_piFqA5OA_cG2CaF1VrtTIP_Sh0pNQqvk8MKO9-Z3uCRANh6JnXKMkJWjBj7ToCwD_t6LrY31M-KaJNp9ZLrT_R_P2dBluNfTTmZQuVe1nK4S-RaNL49Sws6qvE5RBLblt1PLD8Lwz5PQW54xLLyJ7TYxABdchkZJtaURqkVddWMqlN2Mo5YXZiY9yNeIn3xEG28vcnnItDYWkqaCpeRphG49JwU9o0vBwZykpO2_aZUsMR_-ggUKf-Hvf3CqturqGwEEeR71bBiE82Ii5RSMa8yc7bNNC1W2TNWJ3f8txS0asK1yFio-46uU9ulBh7KgxH84uM3FbBLPxK6z2-5YQJepxu5-JKZs9Rb1x8KucUg-4OwxPvadQajkOaTT9Uhn4EPpbm1GbeW5OHvdczIXe3hmEHjQSFfcuOpYM-g5HNkVEIA8y_701x3ClbjiqdiApM7BhtE1mzziOlVeN6VRgmCBCka8KhIfjHJB2xd3dxCIh7KLjjkgv3ICBBtWAq0g6xJEZL_MCv59oXjkEOYcfk9NmfvPYeJ-cdg5obmVXs3x477V_c8xsRcJ0iN27xMi7PEo_U2UaIxWK_Atyy0XHnQFomOVrmDym-fJsSjMqITpt_puIdL_gDuOEActPQ6XjCF1AIt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fee158717.mp4?token=Bn8CGjnVgQYAYusivf-5izKXZEhRENk6pr_piFqA5OA_cG2CaF1VrtTIP_Sh0pNQqvk8MKO9-Z3uCRANh6JnXKMkJWjBj7ToCwD_t6LrY31M-KaJNp9ZLrT_R_P2dBluNfTTmZQuVe1nK4S-RaNL49Sws6qvE5RBLblt1PLD8Lwz5PQW54xLLyJ7TYxABdchkZJtaURqkVddWMqlN2Mo5YXZiY9yNeIn3xEG28vcnnItDYWkqaCpeRphG49JwU9o0vBwZykpO2_aZUsMR_-ggUKf-Hvf3CqturqGwEEeR71bBiE82Ii5RSMa8yc7bNNC1W2TNWJ3f8txS0asK1yFio-46uU9ulBh7KgxH84uM3FbBLPxK6z2-5YQJepxu5-JKZs9Rb1x8KucUg-4OwxPvadQajkOaTT9Uhn4EPpbm1GbeW5OHvdczIXe3hmEHjQSFfcuOpYM-g5HNkVEIA8y_701x3ClbjiqdiApM7BhtE1mzziOlVeN6VRgmCBCka8KhIfjHJB2xd3dxCIh7KLjjkgv3ICBBtWAq0g6xJEZL_MCv59oXjkEOYcfk9NmfvPYeJ-cdg5obmVXs3x477V_c8xsRcJ0iN27xMi7PEo_U2UaIxWK_Atyy0XHnQFomOVrmDym-fJsSjMqITpt_puIdL_gDuOEActPQ6XjCF1AIt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۸ پل آسیب‌دیده از حملهٔ آمریکا به هرمزگان افتتاح شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/464308" target="_blank">📅 11:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464307">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbkPHZsvsUXmknwbPaiP-uAxguT4zq9Z490iDiHEiy6WL19d_g5q55IOMwdaZ4PfNkUfgf4qmIj_zDTnmG_0QsThAavuRdceMGxi7qYHyDC8GN-8GJM20a4-UaPL9WxnV2UuAj9Pwhdft7mTdEGqXnXcqkDvM-0d4fQI0VVBQbZcJ7dKCv8oG7Oj_7VEcfM-H1SU3hij6gOXF8qxGupHPnpi9401gwyG3INr-QQWCVu0463KJaSlu72XOEjDmMG5mUumMsngBfpRY1HHjRTwjO4rjPUJn7BiHwjB73rXbmk3ny87_pdnTpOQpVAl90CAdSDppAjsMgL9M_vv3jWyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردشکنی قیمت گازوئیل، اروپا را نگران زمستان کرد
🔹
کمیسر انرژی اتحادیهٔ اروپا: محتمل‌ترین سناریو این است که با قیمت‌های بسیار بالای انرژی در زمستان روبه‌رو شویم.
🔹
اتحادیهٔ اروپا به‌دلیل افزایش غیرعادی قیمت سوخت دیزل ممکن است سخت‌ترین زمستان خود از سال ۲۰۲۲ را پیش رو داشته باشد.
🔹
برای افرادی که توانایی مالی خرید سوخت را ندارند، تفاوت چندانی ندارد که سوخت در بازار موجود باشد یا نه؛ زیرا اگر نتوانند هزینهٔ آن را بپردازند، در هر صورت قادر به خرید آن نخواهند بود.
🔸
کاهش شدید تردد نفتکش‌ها از تنگهٔ هرمز و آسیب به پالایشگاه‌های منطقه موجب شده صادرات دیزل از کشورهای خلیج فارس افت چشمگیری داشته باشد؛ روندی که در کنار اختلال در پالایشگاه‌های روسیه، قیمت گازوئیل در اروپا و آمریکا را به رکوردهای بی‌سابقه رسانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/464307" target="_blank">📅 11:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464306">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هلاکت ۲ نظامی صهیونیست در غزه
🔹
ارتش رژیم اشغالگر از کشته‌شدن ۲ نظامی خود درپی انفجار روز گذشتهٔ یک پهپاد انتحاری اسرائیلی در داخل یک پایگاه نظامی در شمال نوار غزه خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/464306" target="_blank">📅 10:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464305">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9NnMgy4qiFSxjfehZdo6OXYm3GIT1RjoEshYTe5OPg8-rk-JlPGGPBqKQjX0eW0oOlVDoBM2Ppv_9ZA7KqPw5A6pNnoQZ4pthF-id9mI0FumQrXUqkPR3FbxIgeTPQ2PiZ6KGoIvLXrxj0CqOYbvostm6O5ZpU-OYhtE9l3D0wBCJ50297B49oRcSzFCqSAcuE3CNwTcCoRVeoy4OORBaasNGMBkemr7gD8-QpN7rTqsFbbH7CUX3opsSPf4tjARux7Gqlnj2CGb8NSeTlKAPzUT4FC49yGccOHgDQxZbxmAdpzIgWMYujOsnoVP-ydPehgdZlAHgGfBgxGtO2GUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جملهٔ خنده‌دار نتانیاهو: متهم‌کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است!  @Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/464305" target="_blank">📅 10:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464303">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c36a16014.mp4?token=l88GdT5vj6DwxdMN4kZzlVNnLp_uPwHE7xbLyUDWiCIMXkEfm5aI6gfDYwtW9hxvkztE2daC1uukdyslS8SCfeCVhpxQ-wS-wSDkC93nXaZ9jMXvOWnP23QGoT85qEDA4UhLnJbufH9p5QpwUk7VRUPdgcvSZmwv55SluKmeAjLBjbczJk11Ad6A15VHhQNhSAWMfdw5T2ERj3Bq5JZlgukBwQXRunetFij3gRyQCtYpxQIM0C2VQRRUuA58GhbJ6uYDRkxvEPLFuzpq9MGtLP7MVSEJb3CcVR2nUIG3Sy2ADvE86eCJ37kJe3ySLO464MflB35DcmJI6jxcvdsJug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c36a16014.mp4?token=l88GdT5vj6DwxdMN4kZzlVNnLp_uPwHE7xbLyUDWiCIMXkEfm5aI6gfDYwtW9hxvkztE2daC1uukdyslS8SCfeCVhpxQ-wS-wSDkC93nXaZ9jMXvOWnP23QGoT85qEDA4UhLnJbufH9p5QpwUk7VRUPdgcvSZmwv55SluKmeAjLBjbczJk11Ad6A15VHhQNhSAWMfdw5T2ERj3Bq5JZlgukBwQXRunetFij3gRyQCtYpxQIM0C2VQRRUuA58GhbJ6uYDRkxvEPLFuzpq9MGtLP7MVSEJb3CcVR2nUIG3Sy2ADvE86eCJ37kJe3ySLO464MflB35DcmJI6jxcvdsJug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الفتی نقرهٔ پرش خرک را صید کرد
🔹
مهدی الفتی در فینال پرش خرک بازی‌های آسیایی ناگویا با اجرای ۲ پرش، نمره‌های ۱۵.۱ و ۱۳.۹۶۶ را به دست آورد و با میانگین ۱۴.۵۳۳، تنها با اختلاف ۶۶ هزارم امتیاز نسبت به نفر نخست، به مدال نقره دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/464303" target="_blank">📅 10:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464301">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0966492ed.mp4?token=ujiU33QFziv-9hPMYisY2D05SZIb5XkruxIzdwHdXGCiBUu_bMhPBcFYbBzcJ0N_HzGA3r3xl1mJowziCcyjkP4tjcYZfFgwL767HacMJI8mR3bvkFDEwEFRDpPFdIqW4E8v8O5XT_lHlla5wwhZ3gc1eruf18xj57q12vuqAUF97iy7YvjU-1lScTR8SSpgxtZs5FqGGSt7sCtMyTtCGpsKTLN4R7pt6rRd_Rdom9_uOp0jhUJbkqtgDUsEOiIhKSY3psjv_9e8y2VGhDhEYnaWQmpFjHasHdkf9XxZywnZOovdqnOfdITmG9RijqgMbRp0LkNdVCCJrudLFVdleQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0966492ed.mp4?token=ujiU33QFziv-9hPMYisY2D05SZIb5XkruxIzdwHdXGCiBUu_bMhPBcFYbBzcJ0N_HzGA3r3xl1mJowziCcyjkP4tjcYZfFgwL767HacMJI8mR3bvkFDEwEFRDpPFdIqW4E8v8O5XT_lHlla5wwhZ3gc1eruf18xj57q12vuqAUF97iy7YvjU-1lScTR8SSpgxtZs5FqGGSt7sCtMyTtCGpsKTLN4R7pt6rRd_Rdom9_uOp0jhUJbkqtgDUsEOiIhKSY3psjv_9e8y2VGhDhEYnaWQmpFjHasHdkf9XxZywnZOovdqnOfdITmG9RijqgMbRp0LkNdVCCJrudLFVdleQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش ۹۰ هزارنفری کرمانی‌ها در رزمایش اقتدار جان‌فدایان ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/464301" target="_blank">📅 10:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5d959261.mp4?token=Jhu6Mb7LIkjd787pdHXqLf9LEZj7rQXWPtJJKnk6mFik_X4X2ncZ9rNEiT2WftpXFHdFCQ0LV1-xXdJ6PYCGHOXVbglKZncsuVphL80naSnhVwhCezx6mTxNt8ReY7uYyAdumP_fx3yAtEvdJvpqYpJnOQQEDRc1FNzUrxJ1TQTQrsbHaz9OntR0zBA3lIQpDx391pwrIjcFD-7n2P-Pk73LZnjDZSdbvSRuLtwGU0WGlM45cNEpBQ69awEkntxBmAfSY8nnd5EzzI36iN6gIx-XAVadqIp_WbfkwKgD1wdWJse8lzUY037sHALl3jjuGWz14HAVkmkRW9m0E90vAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5d959261.mp4?token=Jhu6Mb7LIkjd787pdHXqLf9LEZj7rQXWPtJJKnk6mFik_X4X2ncZ9rNEiT2WftpXFHdFCQ0LV1-xXdJ6PYCGHOXVbglKZncsuVphL80naSnhVwhCezx6mTxNt8ReY7uYyAdumP_fx3yAtEvdJvpqYpJnOQQEDRc1FNzUrxJ1TQTQrsbHaz9OntR0zBA3lIQpDx391pwrIjcFD-7n2P-Pk73LZnjDZSdbvSRuLtwGU0WGlM45cNEpBQ69awEkntxBmAfSY8nnd5EzzI36iN6gIx-XAVadqIp_WbfkwKgD1wdWJse8lzUY037sHALl3jjuGWz14HAVkmkRW9m0E90vAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۴۰ هزار جان‌فدای تهرانی امروز با موتور به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464300" target="_blank">📅 10:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464299">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRiEqH7tNNIFuc6gvST0c_YL0Qd47Ki7TFVt0CrTWkpuKae9hlgE_sti6uIgMo9QDUwG_GAzhXKS9gCgaEHj9i2g8AQpWAkaUjSwfE1aAzjFuhOOkGI2n1gnrFS4jgr1thMhc2LjeRUWpl4yoHkzpsKJKuDaUz2YSJrxlwTfOvIV0Fyn8bhp-2S_yx5NabNV_cxGEOHInxdfVg5i3LEBj7Bm7iByzi2Qd3aauRkC0Go2qIbA9rhN4Uyit3jKnouoZGDHhmwHFopBsLcPhKUlM33y2wMhIkCHhvw7vyXdIjLiszTVGQiU4Cvjvm-sYcv-jZyVJJIvQWvaZLhE1Cn3LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاره، معاون سازمان سنجش آموزش: تا ۱۰ روز آینده نتایج کنکور سراسری ۱۴۰۵ اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/464299" target="_blank">📅 10:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464298">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab147d9ca.mp4?token=BV6ch3hhs5zLOYYfS5nV2ZKOqGJgGiT_7tLxwK253au2wR1HvyQHNXcNNywxoPSmS2Hn2LHwssXoNJDmFeJw7UAjO2xA2S9vckyrUqaWgPiWilhSSPRHam8z5fec3pNo4Tjb-d754TfSHsek38vhTvRsbgXLtmSSb67GoUZTC9DI57jj_W4m3zv5ZsbtbCLSnaiicxCxFJo_O7z83HtOpNr-g3YPGyfWn0-3EL9y9WFuyIvNkx3Li1lzP93E1pfuql9oHv-ZAxD2WK63Q1JY4xY_Rgh0eIjIldnSEZxZrAXWm868O8YhByaCU37TU_L6pFYOBIYeaHcRpCH_Y_zdLU6QUuL8pJgX0s04z5xRquJzwKBPNr5K7rF3oPBxv8TRy78RHh7d_I4G2-pIB5sfJM3XhW6ZX0p4USGMXNQ16M4_MdRaBM22wWPTo7HMPGA4irLTOgMmfUMhRrPwvNQxpdBj7-xj7ag391cKGXb5a9lU5d0ovrTfYrnzqvfrsqaHxoNBCFiKqSfOJdEP-QXPxpteLzwO_luLZmHkMGkmz9iKwleViVMzcG1G4lrz5wBbFeOr47hcwgStuKT8Nxpkbrbq663jv4fZ_hnZjQw1meS8ryvvtU03uUpfsJyhfIdj1fLftl9MHGjal1vSFgLYB24Yzq9PagoJXjOMRh2VFW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab147d9ca.mp4?token=BV6ch3hhs5zLOYYfS5nV2ZKOqGJgGiT_7tLxwK253au2wR1HvyQHNXcNNywxoPSmS2Hn2LHwssXoNJDmFeJw7UAjO2xA2S9vckyrUqaWgPiWilhSSPRHam8z5fec3pNo4Tjb-d754TfSHsek38vhTvRsbgXLtmSSb67GoUZTC9DI57jj_W4m3zv5ZsbtbCLSnaiicxCxFJo_O7z83HtOpNr-g3YPGyfWn0-3EL9y9WFuyIvNkx3Li1lzP93E1pfuql9oHv-ZAxD2WK63Q1JY4xY_Rgh0eIjIldnSEZxZrAXWm868O8YhByaCU37TU_L6pFYOBIYeaHcRpCH_Y_zdLU6QUuL8pJgX0s04z5xRquJzwKBPNr5K7rF3oPBxv8TRy78RHh7d_I4G2-pIB5sfJM3XhW6ZX0p4USGMXNQ16M4_MdRaBM22wWPTo7HMPGA4irLTOgMmfUMhRrPwvNQxpdBj7-xj7ag391cKGXb5a9lU5d0ovrTfYrnzqvfrsqaHxoNBCFiKqSfOJdEP-QXPxpteLzwO_luLZmHkMGkmz9iKwleViVMzcG1G4lrz5wBbFeOr47hcwgStuKT8Nxpkbrbq663jv4fZ_hnZjQw1meS8ryvvtU03uUpfsJyhfIdj1fLftl9MHGjal1vSFgLYB24Yzq9PagoJXjOMRh2VFW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرجی به ۱۶ نفر برتر نرسید
🔹
بنیامین فرجی در مرحلهٔ یک‌شانزدهم نهایی بخش انفرادی تنیس روی میز مسابقات آسیایی ناگویا، با شکست ۴ بر صفر مقابل حریف هندی از صعود به جمع ۱۶ بازیکن برتر باز ماند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464298" target="_blank">📅 10:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464297">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuDmO6PUR_5gVJTU9wMt9PGwDOVGpy8j7uZl80iLiB9VybnyTLT4bzeNG65DtfhgPTAQfR4ZZ5fgmPDmxqvpfw0pizQhDRxd6dKoilqzmq-ZrGTxy5MZ3Td7ezBBl4ctYRm_9h1cwQOole3CLWeTCJvSP-Wtjofwkl8FtAM9hWmhvz_1mqXjyJQl_ZLjm-fe35jMdCORLppg2L04rrnMrRzr1_0IKBUaJHLGA4qL_Y6Z9yS-QcIoOeszcMHdDn0vICDNgiaoN9k4qqv7QlUKyCnvZthMj9VCoHRjubYpIEsRiWjfgs-1fkIxU59g3opmD5spKxd0zOxDc2iWtjS0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ افراد ناشناس به اتوبوس نیروهای الجولانی در دیرالزور
🔹
منابع محلی از حملهٔ افراد مسلح ناشناس به یک اتوبوس حامل نیروهای وزارت دفاع دولت شورشیان حاکم بر سوریه در منطقه العوسج در حومهٔ غربی دیرالزور خبر دادند؛ در این حمله، ۸ نفر کشته و ۱۱ نفر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464297" target="_blank">📅 09:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464296">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_WhAiyA2QsI3gu9Nr2I1lrVJURwcgca44NRj8QYobH8vIIqKHmON73Q2CS9KzSmt6fQcNqRnFFiTw80SaQh8QfLC2EKkFc2Fqy-x8jRmEmAFxMmoWl4ILHvfaYWSwwrqCgM0wKV454jOolvl8z-w5RMO3X76_7G9LAcc_zbVFhyNnGerIm6EwiIC2hyLN_rgZvp8VWTAAHcadRNms_7Y4qNPq7yoUBA4MQ4Q25eNNgmEs_kgLYm6JPY1BG-rcBuw2GB1qnhlWAU-fM0IgzKpcSsaWXVeVTvb9irhLP9saRo6NfAJ2h-oYHCgyrCwuuYNzxqWGILKeudGTWVNJ0WvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسکتبال ۳ نفرهٔ ایران به فینال نرسید
🔹
تیم ملی بسکتبال ۳ نفرهٔ مردان ایران در مرحلهٔ نیمه‌نهایی بازی‌های آسیایی ناگویا مقابل قطر با نتیجه ۱۴ بر ۱۱ شکست خورد و از صعود به دیدار فینال بازماند.
🔹
ایران در دیدار رده‌بندی به مصاف فیلیپین می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464296" target="_blank">📅 09:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464295">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnWOKq1MwPmGgdT4kl8H5o8cg0JKrl_fQODK21QZ_Rc6zk10tLLi2wEoZFrkZTARmmI29bbQr-pHhl2cfmU9tlubDg2suKay_sSkXrctrS1VBgBTFAZmUQf9cya8j7zxyXCrlStFbFkw6IVfbi3WO4Sgx1Wxm3ZVQuA7jMc8XpegIXVHUywhUtlIoXRCiNrSjmKnIRTlpWvWFTVOPVBBUovsZTQaOzoPFBlolmCh2H6urpyKafmhrhMYCUaYd6FBWl3qnnAIesD8mmrjXiQPlQwnYBuNrPQN6bccDgg6mHFFAh24AbKMC2h28pUEamUblHXMUjzLhDF3Z_m2_nCOPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینهٔ سفر نفت سعودی ۱۰ برابر شد
🔹
هزینهٔ بیمه جنگ نفتکش‌های مرتبط با عربستان در دریای سرخ نسبت به چند هفتهٔ گذشته حدود ۳ برابر شده و به حدود ۳ درصد ارزش کشتی رسیده است؛ نرخ بیمه برای کشتی‌های عازم بنادر جنوبی عربستان نیز ممکن است تا ۷ درصد افزایش یابد.
🔹
با احتساب بیمه، کرایهٔ نفتکش و سوخت، هزینهٔ هر سفر حمل نفت عربستان دست‌کم ۱۰ برابر قبل شده و در برخی مسیرها افزایش بیشتری داشته است.
🔸
این درحالی است که بارگیری نفتکش‌ها در بندر ینبع همچنان از سر گرفته نشده و تهدید علیه کشتی‌های مرتبط با عربستان در نزدیکی باب‌المندب و حملات اخیر به زیرساخت‌های نفتی، ریسک استفاده از مسیر دریای سرخ را افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/464295" target="_blank">📅 09:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464294">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvBTOkSkwOuTACdBtzlT0eh9OSvCumbuIIZjAShfjNelN3OUkBlIa0N9pK61f6MMT_0KbTM961jBMcA-aaYXNcMRyQ_n4dQQaW45RGPkxTSRkBQRr8275PGtJFDvfpXmdhcfjNzzW8Sq7v43nLpZRut23k82JuXZTKoCi36vEn33tsB8f87mVrUsGqIqxeO_YDnUt7c1y79J_tsMDty45yatPCO9DrP2Bm0nrKXaw-EC9rXWapDCPVyU7tG2Q8TMbSkycfmEco1S0hpzF5Q3nRrqzJ3vt-NXbi4YlyHDhXteXOn5Acd4LUfmIJamEoj1UICkECg0ofvaj7HwAqoEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشاد عالمیان به مرحلهٔ یک‌هشتم نهایی تنیس روی میز مسابقات آسیایی ناگویا رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/464294" target="_blank">📅 09:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464293">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ac963e738.mp4?token=mCX7aDID9JJIRjBO9um1bd9-Ms30wR-iJukw7Derw0hx9XK694tiJqpD1kPucfC-VSDaaimZUANTRZRkEC0RvHYqf-Ak3jjDPUoFqzK5VNgEftF5tw0xu2GSWiDK0FHRQzImmRkDj8pPIEQUvWuh9H1yOGIRuBrea-E-p7svbaTN772tSDYS6Yfv4j7s8qfasOaMBudhDKCmkXK-5-lt3ewoqAl-atXJseGqynhEPruyCyVQtgO7_PYnfD0JLk6Ypbubi5pOjJpsD0wjKt_sD3YD6BtJjH4gTg-SmrBG8_QbBjEDzWm8rcmPx_u40Om1EzkiuolRrFc9pqWIuzfqGZv7KHOl8SfNTWSu-5hQe1KVH-GyrZQDM3I9OY8JOxw4VEpGgMW8fPGgxAoeou4O5wjz1sYpncm3ZZqRR919kCtDb0khCkWR13WUBfxPaPn0ZCeR-VYWKZ9iGfOypdtd44l9TdM6dwyv9K8TweXwHTWj25_BVk7y7bIkCNzqWvsYkiSYCXyVGjQMuai1fCghdQCdVzTB1pEf3WURK1sF59r0n0BBW-B_3VTY5ss-9Z9-ACpvrQ9P2ke-wj7Bhxv4CLXUrKw3kKD6PMDqTrINDhbSt4CSrvVAx8Ixa4SscNWNpaK9Ui8MplvTcmo76r8kY6c9YWkfMXhTQnJ4KOLjg-M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ac963e738.mp4?token=mCX7aDID9JJIRjBO9um1bd9-Ms30wR-iJukw7Derw0hx9XK694tiJqpD1kPucfC-VSDaaimZUANTRZRkEC0RvHYqf-Ak3jjDPUoFqzK5VNgEftF5tw0xu2GSWiDK0FHRQzImmRkDj8pPIEQUvWuh9H1yOGIRuBrea-E-p7svbaTN772tSDYS6Yfv4j7s8qfasOaMBudhDKCmkXK-5-lt3ewoqAl-atXJseGqynhEPruyCyVQtgO7_PYnfD0JLk6Ypbubi5pOjJpsD0wjKt_sD3YD6BtJjH4gTg-SmrBG8_QbBjEDzWm8rcmPx_u40Om1EzkiuolRrFc9pqWIuzfqGZv7KHOl8SfNTWSu-5hQe1KVH-GyrZQDM3I9OY8JOxw4VEpGgMW8fPGgxAoeou4O5wjz1sYpncm3ZZqRR919kCtDb0khCkWR13WUBfxPaPn0ZCeR-VYWKZ9iGfOypdtd44l9TdM6dwyv9K8TweXwHTWj25_BVk7y7bIkCNzqWvsYkiSYCXyVGjQMuai1fCghdQCdVzTB1pEf3WURK1sF59r0n0BBW-B_3VTY5ss-9Z9-ACpvrQ9P2ke-wj7Bhxv4CLXUrKw3kKD6PMDqTrINDhbSt4CSrvVAx8Ixa4SscNWNpaK9Ui8MplvTcmo76r8kY6c9YWkfMXhTQnJ4KOLjg-M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمدی: برخی کالا‌های ایرانی با تغییر نشان آن به برند خارجی ۳ برابر قیمت اصلی فروخته می‌شوند
🔹
عضو هیئت‌مدیرهٔ انجمن صنایع لوازم خانگی: قدرت برند یک واقعیت انکارناپذیر است و نشان‌های تجاری داخلی توان رقابت برندی با غول‌های جهانی لوازم خانگی که پیش‌تر در ایران حضور داشتند و اکنون رفته‌اند ندارند.
🔹
از این رو بخشی از خریداران تمایل دارند حتی بدون گارانتی و به شکل قاچاق، برند خارجی خریداری کنند.
🔹
به‌همین‌دلیل محصول ایرانی به مناطق مرزی برده می‌شود، در آنجا کارتن و نشان آن تعویض شده و سپس با برچسب برندهای نامدار جهانی به متقاضیانی که حاضرند ۲ تا ۳ برابر قیمت کالای داخلی برای نشان خارجی پول بپردازند، فروخته می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/464293" target="_blank">📅 09:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464292">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4WlJ9vOhTRvO3kmS-1A2d6VPPfKbG_56EjxoCqHib8KBUG6z3EY4ur6e9WCi-bJ89lwnCInfw8stcBEXw8bGAP9YLn8qtOwmJiKAe-cGkCpCfJHKlQxsQqXZtAeL-ctMRysiqGUChDfncXE3K73KG2-DUaWnFMSvQ-wLRfOIcvJfPn4KX_Zp-iMiHg0-1t_kzjMjDE-hwEl7Yjauq_xrbRHNwq7Nk7YLW2KPKe4doL2P2A4jfGgyHFmkqr_BX9ZLFfkyyGoORk0m1xm325ZA3ustVsQa-PTCxMJwBmBRfN4HNbu0SBmUCcofUBnak0D1I-iDzjozcD8GJFWo_pr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محیطی‌زاده دیسکالیفه شد
🔹
فاطمه محیطی‌زاده نمایندهٔ کشورمان در مادهٔ هفتگانهٔ دوومیدانی مسابقات آسیایی ناگویا در بخش پرتاب نیزه، به‌دلیل استاندارد‌نبودن کفش‌هایش دیسکالیفه شد و از جدول مسابقات کنار رفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/464292" target="_blank">📅 09:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464291">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8hPfYxxUHeG5oLRV47JS5fuHgI6aC76e4BGPgdFOGwMI8L6ZRLMfih9sTFn0DElnM2VrWYU2W6vlJHTSMuUBzESA9HOnD5lGfT14lOBRD9WFB1uIllqCN-JpIFonCjJFP3_e324n_i9gx6PdDK29Nyu8PxxnEMK6wp2aG_1qV9tSnE_X1ZnL4rgeJ6HqoXTXe8TcFSR2gkRFcEWOATp_dPNWb4GSEMET32ZVroLjAi75LlJbB6eiayQCQ1N5jZCNbcbCqRGuHMqX-927D-7sibBI-qOUgGUNFoMB4KMgmdeUOoQR-VE3hKBMs5fbYx4NPIAFcgezOkb7yFbEbcDfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جملهٔ خنده‌دار نتانیاهو: متهم‌کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است!  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/464291" target="_blank">📅 08:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464290">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b73b98f4.mp4?token=PKXHxhqTOA1xPZBt7MHqc3zwFVrzs6RGFm6Qz_Oxq6yTmeVv-0CYKAfmle1TG8hUYUNkIED8CgTOrj1b_gWV3acn3qUUHrPK1wg92jRymxyD8AydaWcgItlBZeF0mhMaCWhL5gAl2ntFBeB3NR9LP468E2YnDke8P1NQJio4zQbJr0-WOuKFUxplw7SJsz7Ea2mpE-DIYQtDfa2_nsMfD7ga6niAkiV1MOjKPzJBWw1755rpHuhxFgjpaD92HAMup6V_2NsaGk7cI4c2wt6csSKWxc2Mc8JyPZWLdu7bN9vCq_t2AprYhoDW4Ss9sitTxiT_JzrRqXG8NWHZA3qCRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b73b98f4.mp4?token=PKXHxhqTOA1xPZBt7MHqc3zwFVrzs6RGFm6Qz_Oxq6yTmeVv-0CYKAfmle1TG8hUYUNkIED8CgTOrj1b_gWV3acn3qUUHrPK1wg92jRymxyD8AydaWcgItlBZeF0mhMaCWhL5gAl2ntFBeB3NR9LP468E2YnDke8P1NQJio4zQbJr0-WOuKFUxplw7SJsz7Ea2mpE-DIYQtDfa2_nsMfD7ga6niAkiV1MOjKPzJBWw1755rpHuhxFgjpaD92HAMup6V_2NsaGk7cI4c2wt6csSKWxc2Mc8JyPZWLdu7bN9vCq_t2AprYhoDW4Ss9sitTxiT_JzrRqXG8NWHZA3qCRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایلوخانی مغلوب پینگ‌پنگ‌باز ژاپنی شد
🔹
در مرحلهٔ انفرادی مسابقات پینگ‌پنگ زنان آسیا ستایش ایلوخانی نتیجه را به هینا هایاتا از ژاپن واگذار کرد و از رسیدن به مرحلهٔ یک‌هشتم‌نهایی بازماند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464290" target="_blank">📅 08:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464289">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e5b48ca2.mp4?token=hV71cZtgxFtzRrxoHKXrX62yon0im2vKmQN33wyYq_7KGAIxBv3ST4DM7Hxa-UMk6mRSrpaf1GvQveSuv_8Ka1Jc9x_UGoq6ZGmhHWVsxtpWyHR9g8HFqQjYBHjpWC5BZcEl4v1SE-q8bj-MFv2CoiFDarpG-dvWu8Jq58P_O2igkGpPdx2bcUdwnbldQiZ3D6t_kLvGBqqwNLstYdZ4Q3hdrBR_CdaKQ5DgSyEpwt-itIQiKliWQ2r8MO-HDYk8I9RlABgRYM_deTemellpRNCqNhN6TREl87WHJowZ_xLqt6Ihaedoj6ALPuG-fJDj8ZN97Bb-5Naq4nKWsUi-vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e5b48ca2.mp4?token=hV71cZtgxFtzRrxoHKXrX62yon0im2vKmQN33wyYq_7KGAIxBv3ST4DM7Hxa-UMk6mRSrpaf1GvQveSuv_8Ka1Jc9x_UGoq6ZGmhHWVsxtpWyHR9g8HFqQjYBHjpWC5BZcEl4v1SE-q8bj-MFv2CoiFDarpG-dvWu8Jq58P_O2igkGpPdx2bcUdwnbldQiZ3D6t_kLvGBqqwNLstYdZ4Q3hdrBR_CdaKQ5DgSyEpwt-itIQiKliWQ2r8MO-HDYk8I9RlABgRYM_deTemellpRNCqNhN6TREl87WHJowZ_xLqt6Ihaedoj6ALPuG-fJDj8ZN97Bb-5Naq4nKWsUi-vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمپول‌های لاغری ممکن است به چشم آسیب بزنند
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/464289" target="_blank">📅 08:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464288">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/828d529c11.mp4?token=jXm-nTYLHc4JLt-51e9DWIZ3QJK9kQK_h9-YevjGSFS9HOEn_TJ8Ie2kF-CcIP6a-dWELN0dvrTCJf66A3oLZN6bnk7Bbq_3wp2wMRmiNNoykJv_d99uzbA9k3SjkBfj7gS2DrIzGU841hm97kdoAJSL39HKhlgqD1G9P3paTMZnf--_K1Po82yPRjBrz7ChqY-QvAog0c5RqGdjQSQjyPlidBZYWNAo6tZD_YP0AKHJnuVXesJUilxxGHS72Ax3kr-5bY5h145CFptrpyYnqJHzbz7RNenxJEuzEqL7K8Vx-H2GlyJbECo5hWf9Vap9RTu4_9UMcmFMA6TAVLDE3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/828d529c11.mp4?token=jXm-nTYLHc4JLt-51e9DWIZ3QJK9kQK_h9-YevjGSFS9HOEn_TJ8Ie2kF-CcIP6a-dWELN0dvrTCJf66A3oLZN6bnk7Bbq_3wp2wMRmiNNoykJv_d99uzbA9k3SjkBfj7gS2DrIzGU841hm97kdoAJSL39HKhlgqD1G9P3paTMZnf--_K1Po82yPRjBrz7ChqY-QvAog0c5RqGdjQSQjyPlidBZYWNAo6tZD_YP0AKHJnuVXesJUilxxGHS72Ax3kr-5bY5h145CFptrpyYnqJHzbz7RNenxJEuzEqL7K8Vx-H2GlyJbECo5hWf9Vap9RTu4_9UMcmFMA6TAVLDE3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدال برنز برای تیم تیراندازی ایران
🔹
در ادامۀ رقابت‌های تیراندازی بازی‌های آسیایی ناگویا ۲۰۲۶، تیم میکس ایران در مادۀ تپانچۀ ۱۰ متر با ترکیب وحید گلخندان و هانیه رستمیان به مدال برنز دست یافت.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464288" target="_blank">📅 07:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464285">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PngnEIJJItAodKzgkxT3RMfGIyuMdhQzLpkqPJhrgqvYEQqnQXIcgj2YAR_Qm_tsw6I-I6qNgTiv-vQ7QCaulWtT4DK7xHgs1hXA_EeBnQqsi68P1GXHd7ajPzCsN-6oeX7kzD-oj-BdLxKAAZId9mVLxRK2FO1_4mEYsbEx5Vm6BYOF_CWrvnRgQWQwgecMXFFQHoQxdxX95l_MSnEzJfq_cvGvG2agGzFMm5SPvp9dsUNzCS5KDRmG55KUUIpt3fanSeZrvMKyaw8CHyqj-knDwBqy_IB2CPZ5uHl2jPLUtH69lXeTs65sHMMH0WsI6GOEEc1QKh9StBeZMP93YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDlduPLE_vmvLUc0l3xNJ0x_lmcR6dGbcdfGA2mB_iC4Zy5ZYekzdAYVE-2LPaOPe0NcHFZFxNgZf1plSD5As0Ac6Iyy1d2u8PM31kRoxZsgF43gGhXnJX-_ae-aPE3gt3dz3d6Fx-WLzZLO2tYuC7l4SuDWeFJuWW-8OrLeqgQc9GjVs0hQVKhgEqRhywIY3An6PEg1FMOq4Ygrc7myGR_xK2IATitkz1oY2vsgp9VIB1i56WnOD3AzfXTOuV-_KJaeefaOgIRqdvLS_alMn9Iecoj33mSS9ePU332WNkNPgtRKCsyTyWtOXZZCDOyjw_QwMtNn2nhADyR3urX5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCF3au7eYgp-HLpmkIw-Att2THz0WzpJX2WOy99AyizVCloYP7LDUU0N8aUE-ii7-yLXyZzOEEJ0x2HgykxjVZ5uyU2ziZJu4RFbg0ZmbZnqhHu40dmJH4ePFEn6avAIN4YSTIvNCX1gXvSSo97UwuGpWi2VLaKK2AP4ZYa7hmEGJIgAaP7UVWUeVIuXkQ51MytjYvzyZOv16dmo-sYpTUViQMq8ll5BgdlLh_NiivwzShDebOaX4CfGYK5gYuXfTcleLqPo0KRYkamZw1wRwyoEifh64rkE9L2rsdA4Ty9W7AsJiEXXBXLHl5UFegeCC1Om3uF_6IHsskrZxFBd8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار عراقچی با وزرای خارجۀ پرتغال، قبرس و برونئی، در حاشیۀ نشست مجمع عمومی سازمان ملل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/464285" target="_blank">📅 07:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464284">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6OGjuYNGCDi6HIxZALhJfMSZm81WfyZ1_ukb4B6InqVCE9HkHGATM7qQnmuh81Ci-k8ZM469JjrioNpS66BldLjmtEQ2WomhXHoq_wiJ5_Uv9XN0BNMY4LNMi7OShf8XdQeOUxVAToE9LtCpya7fpmF8oFF6jHOfuctymBCj7ysXxLILniJdRcxl_Oc4SlWpw5eIYk-I1bhnA82hR6W56_niEPz3hkWaYFyLmquXT2L1xEkmgtZh1KRlYRUd9fDR5FoWnVEk6C07tTDfG05nWA8nD1b5Sdk9bgHROCG693GhzSAzCJQsyKq34eRkfYmaAoNUPBbJ8PI48Hu06zFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفای عبدی پس از فاجعه در ناگویا
🔹
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد.
🔸
تیم ملی فوتبال امید در آخرین دیدار مرحلۀ گروهی با
شکست سنگین ۴ بر یک مقابل کرۀشمالی
از بازی‌های آسیایی ناگویا کنار رفت و حذف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464284" target="_blank">📅 07:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464283">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAjWRLd0-MlHK7oT8IrZSKW7snoiIJgxaSSAhCaUWy7isbHJqZ-5F62Nx09bSlOB6dvnrQbd8sqeFMSV4pJMIHmnPs1esSt5xZcrxQ4Y-QjABOFEZRxPvZ71MQkiSd7i8FFPrT5pXI4ekDDOcYBZP8NJ-FhokojP3WsEaAH3U_-F6g23mdOkRoIklBS32fDfYIHoKjMBT69fW4vd-Fe8mUnj-GJ8wFZZ1yX0zFG2HHQpWfAzhAuU6zuWtm0N0REr8TsbTFPWl2cS82SPOanJAgCuSGdG-WbpSuBX-Eksedia5JJhcmVchyUPfHwX4bfmUZZRxLHuZVbv0rgfmt1Ngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: قطعنامۀ ضدایرانی شورای حکام آژانس شرم‌آور است
🔹
میخائیل اولیانوف، نمایندۀ دائم روسیه در سازمان‌های بین‌المللی در وین، در یک نشست خبری از اقدامات ضدایرانی شورای حکام آژانس انرژی اتمی انتقاد کرد.
🔹
او گفت «شورای حکام در ژوئن به ابتکار کشورهای غربی یک قطعنامۀ ضدایرانی تصویب کرد؛ اما کمتر از چهار ماه بعد، علی‌رغم وجود قاعدۀ «ممنوعیت طرح مجدد یک موضوع در بازۀ زمانی مشخص، و پس از گرفتن یک تصمیم» قطعنامه‌ای جدید ارائه شد.
🔹
این صرفاً نشان‌دهندۀ شیوۀ غیرمسئولانه‌ای است که شرکای سابق ما که اکنون رقیب هستند، رفتار می‌کنند. آن‌ها بی‌کفایتی کامل از خود نشان می‌دهند، و شورای حکام هم همراه آن‌ها شده است. این قطعنامه کاملاً شرم‌آور است.»
🔸
شورای حکام آژانس بین‌المللی انرژی اتمی اخیراً با تصویب قطعنامه‌ای ضد ایرانی، پروندۀ ایران را به شورای امنیت سازمان ملل ارجاع داد.
🔸
پیش‌تر وزارت خارجۀ ایران هشدار داده بود که استفادۀ ابزاری از آژانس بین‌المللی انرژی اتمی برای بسترسازی فشار سیاسی و توجیه تجاوز نظامی علیه ایران، اعتبار آن به‌عنوان مرجعی بی‌طرف و مستقل را بر باد می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/464283" target="_blank">📅 07:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464282">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مدال برنز برای تیم تیراندازی ایران
🔹
در ادامۀ رقابت‌های تیراندازی بازی‌های آسیایی ناگویا ۲۰۲۶، تیم میکس ایران در مادۀ تپانچۀ ۱۰ متر با ترکیب وحید گلخندان و هانیه رستمیان به مدال برنز دست یافت.  @Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/464282" target="_blank">📅 07:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464281">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مدال برنز برای تیم تیراندازی ایران
🔹
در ادامۀ رقابت‌های تیراندازی بازی‌های آسیایی ناگویا ۲۰۲۶، تیم میکس ایران در مادۀ تپانچۀ ۱۰ متر با ترکیب وحید گلخندان و هانیه رستمیان به مدال برنز دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464281" target="_blank">📅 07:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464280">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مدال برنز برای قایقرانان ایران
🔹
تیم کایاک دو نفرۀ ۵۰۰ متر مردان ایران با ترکیب علی آقامیرزایی و پیمان قویدل در جریان بازی‌های آسیایی ناگویا ژاپن ۲۰۲۶، با ایستادن در جایگاه سوم به مدال برنز دست یافت.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464280" target="_blank">📅 07:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464279">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">بازی‌های آسیایی ناگویا
پیروزی برادران عالمیان برابر قزاقستان
🔹
در مرحلۀ یک شانزدهم‌نهایی رقابت‌های دوبل تنیس روی میز دوبل ایران به مصاف قزاقستان رفت.
🔹
در این دیدار تیم ایران متشکل از نوشاد و نیما عالمیان برابر تیم دوبل قزاقستان قرار گرفت و با نتیجه ۳ بر ۲ حریف خود را شکست داد و به مرحلۀ یک‌هشتم نهایی صعود کردند.
@Sportfars</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464279" target="_blank">📅 07:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464278">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌ پزشکیان: هدیۀ ترامپ به مردم ایران موشک و ویرانی بود
🔹
رئیس‌جمهور در گفت‌وگو با شبکۀ آمریکایی فاکس‌نیوز: ترامپ مدام می‌گفت می‌خواهم برای مردم ایران هدیه‌ای بیاورم، اما هدیه‌ای که آنها برای ما آوردند، موشک‌های هدایت‌شونده، تسلیحات سنگین و ویرانی بود.
🔹
آنچه…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464278" target="_blank">📅 06:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464277">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پزشکیان: ما آغازگر جنگ نبودیم، اما اگر بخواهند به جنگ با ما ادامه دهند، پاسخی قاطع خواهیم داد
🔹
رئیس‌جمهور در گفت‌وگو با شبکۀ آمریکایی فاکس‌نیوز: ما به توافق رسیده بودیم و چارچوب تفاهم امضا و مورد توافق قرار گرفته بود. همچنان مایل به پیشبرد توافق با آمریکا…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464277" target="_blank">📅 06:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464276">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rd09bc-cuchPq8aLT8m4FhHKjigg-be0g8Ddxt7X8m0G_3t3-zXnaz4KofyKa_yMrCb8pJLpg3iynuBRC3e-zuTT2C_DZ_HWbQSVGpxj3P7XfSG6cKaF-MMpD_wTzNdkfLvEL9XyS7ednmvxdKJjJWn8ek8gSLBGhUxTUXaW8DC55n-fZ_PK9FtlOFGZWkSSRerv52xRIoScgfPNqn2t4yA3ZIFjHXRwi8SX-FVd3qck5zV9HW6zHDPI1tOhrnOlmi2dfEF-dLmyn7lNDzNtI9NIqFr7Pi3rOeqmQyRdp7vDfE3oCzlt9AzeTdZjfiKbOoI-lRwUcGwevaDLErppug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: ما آغازگر جنگ نبودیم، اما اگر بخواهند به جنگ با ما ادامه دهند، پاسخی قاطع خواهیم داد
🔹
رئیس‌جمهور در گفت‌وگو با شبکۀ آمریکایی فاکس‌نیوز: ما به توافق رسیده بودیم و چارچوب تفاهم امضا و مورد توافق قرار گرفته بود. همچنان مایل به پیشبرد توافق با آمریکا هستیم.
🔹
به تمام تعهدات خود در معاهدۀ NPT پایبند خواهیم بود و اورانیوم غنی‌شدۀ ۶۰ درصدی را در چارچوب حقوق بین‌الملل و معاهدۀ عدم اشاعۀ هسته‌ای کنار خواهیم گذاشت.
🔹
ما خواهان ادامۀ جنگ نیستیم. این آمریکاست که باید انتخاب کند آیا می‌خواهد به این وضعیت پایان دهد یا خیر.
🔹
ما تنگۀ هرمز را نبسته بودیم؛ تنگه باز بود. آن‌ها بدون هیچ توجیه یا چارچوب قانونی به ما حمله کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464276" target="_blank">📅 06:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464275">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9061ad4a.mp4?token=neSdPobXmCL0NPxHOlRiNqql-XTsbSPHD3pqywNgBUJtKe7kxFePMh2KlGswbK_XR8o_i0khNFWOkBhk0qOySvES5GVcSaAqaKdP2Rm_D7DjlBXQeXpJgyC8NYDhF1YH8JazLXXqjRI-rZnOLjhlAkIuGlXriGuaF-w0kMzU1B3t65WWVGwxE1Xx43G4nyT_qXned3SSANnfFFmvfV3qxWlSWLQdbmK-n8pTkh8iNg7yJoAlesQJo2dBNvesM7Aks7R3R0sATGvC6MmoMcmVIrAGW8e7gPCeMIL6ovtqNf_QWvvhXp5W5MFp7oCWY9aEFdU__WNB_3hoCCot5u1Zfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9061ad4a.mp4?token=neSdPobXmCL0NPxHOlRiNqql-XTsbSPHD3pqywNgBUJtKe7kxFePMh2KlGswbK_XR8o_i0khNFWOkBhk0qOySvES5GVcSaAqaKdP2Rm_D7DjlBXQeXpJgyC8NYDhF1YH8JazLXXqjRI-rZnOLjhlAkIuGlXriGuaF-w0kMzU1B3t65WWVGwxE1Xx43G4nyT_qXned3SSANnfFFmvfV3qxWlSWLQdbmK-n8pTkh8iNg7yJoAlesQJo2dBNvesM7Aks7R3R0sATGvC6MmoMcmVIrAGW8e7gPCeMIL6ovtqNf_QWvvhXp5W5MFp7oCWY9aEFdU__WNB_3hoCCot5u1Zfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدال برنز برای قایقرانان ایران
🔹
تیم کایاک دو نفرۀ ۵۰۰ متر مردان ایران با ترکیب علی آقامیرزایی و پیمان قویدل در جریان بازی‌های آسیایی ناگویا ژاپن ۲۰۲۶، با ایستادن در جایگاه سوم به مدال برنز دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464275" target="_blank">📅 06:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464274">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb8090fbb.mp4?token=uVuvP_RN7-C9HIG7vG_80D0wqBbDBioEVa0IRI2wmT66gPUcmS4-4BGpSMDH68n7P36fLY2COGoWudxrQG2pceT2P1thRCmQszgO6qAF_kNOYj0XuhjA1DR6xoiaixczkt7XdrrF4Wt7-4dQzUMy0VG8bKz2JXjdJqbZ-uhCFZ1FUDSWKwp3cgP62xEe7XpuB6AwU2GjrFIpkwUr5gz5RZS5ayPqgECBZ3mwnyeVgISbBnhQjYgH7ErrhzdmlPTY0HrvvnwoFesOHHp_LUqIYTUunbL7IgZDVk75dlhb2XI9og2XLxMrxOpCRvhMSIpJ8Xz8Blia-D01dpjZtgdajQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb8090fbb.mp4?token=uVuvP_RN7-C9HIG7vG_80D0wqBbDBioEVa0IRI2wmT66gPUcmS4-4BGpSMDH68n7P36fLY2COGoWudxrQG2pceT2P1thRCmQszgO6qAF_kNOYj0XuhjA1DR6xoiaixczkt7XdrrF4Wt7-4dQzUMy0VG8bKz2JXjdJqbZ-uhCFZ1FUDSWKwp3cgP62xEe7XpuB6AwU2GjrFIpkwUr5gz5RZS5ayPqgECBZ3mwnyeVgISbBnhQjYgH7ErrhzdmlPTY0HrvvnwoFesOHHp_LUqIYTUunbL7IgZDVk75dlhb2XI9og2XLxMrxOpCRvhMSIpJ8Xz8Blia-D01dpjZtgdajQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی در حاشیۀ نشست سازمان ملل با همتای پرتغالی خود دیدار و گفت‌وگو کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/464274" target="_blank">📅 06:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaQAiukP_uzyNe_sDNKmNXa9o0ag0WxipUA6AR9zXXuecJ6Sj9And2nBHmaYcJQu47OaVZ8KGRyu39N-BeBPGL7amb9Frm6xRG_xNkanAIEdN-epXx53Qul_snHK1kEmN3XlJPYFBt1ZoZz2uNBk15oBgBtnFWp8WA2ewb1mlFZn0lBEdwDS0FxcDek0HX86TLX6AQrMN8g8Lm7Chz38lBQMlyFvGgMyUuIgsp-0KI4pNlMZxpy6Ddr6L2lNNPCwl5D5KLrmZQxWk6K9ZBOFwbI5lG48xfgjdAQaIOhGq3ID0CtH7kcWJ7mZuolywPjIS79h9-tMrorKS5mDaxybNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش‌های ایرانی دزدیده شده شناسایی شدند
🔹
۳ نفتکش حامل محمولۀ ۶۰۰ میلیون دلاری منتسب به ایران که به ادعای تانکر ترکرز توسط آمریکا ربوده شده‌اند، شناسایی شدند.
🔹
این سه نفتکش در اردیبهشت امسال واقع در دریای عمان ربوده شده‌اند.
🔹
بر این مبنا نفتکش مجستیک ایکس و تیفانی در سواحل شمالی برزیل هستند و نفتکش لنور به تازگی دماغۀ امید نیک را دور زده و به اقیانوس اطلس جنوبی رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/464273" target="_blank">📅 05:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464271">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvuiUCX4r2VZYbjrl38x7QgSNnCTZRHr-xYJxPTAbzcvfCvRUFlHNcwHdAk8cHTESBlDmP38K1onYs2-FKoXZgSd63a8MiPem5fTBqJI-eP5Ac55yxafFdOTWYkDaUOVHHHTmQUHIBvEjJRLLxpYtFVaS9eOM9XxeAlu9MWP82X6PPtNJSiEN7dgD5v8_JLSALAfm-jmn_XOxGaa-my3_aopi7UgLPvbaiVIHjIkgwS2gIaz9ZkjiBf6eYfTR06UnIg3fp8Mypma61gYdxRnbNSkyQIJxpw_3oeqN5cERW_rPXi1vg4QAfdV7D7fj94j7fVJtCld6MpSv3_TMOuRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjWiqnF1o2dvCkXI8UEafs-NdFXJZhwGLwBsRiwTVF3WsEE9oBhy2SYBdNEM3LD7JT5X4-hhhwCKSREogvubmO96wVlZWxEHo4c6ZcGB_ojVsTYWJdMaqS3Td8BvfXC6oIN6P2uAK-CFhtNW-RJ-kAzSI9TMOFjsAhB8pp46X7r97w4zE8TnkMo9IUahoD3PNWRCxfYtjAwtzfro9EL8CK5C4C3opXDA_ZZBROi3TnSYZ8ui4H_izctjflaXLLSDfc1KGPeFfRVLKkMp0NuQA6I52yQbbVS7isZmCyl7PODwzwmo90IE_C-afXdvP-godY78Hj3CMgK9a6Z6mUxnIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❤️‍🩹
هانیه خندان، داور بین‌المللی تیراندازی در مسابقات تیراندازی بازی‌های آسیایی ناگویا با پرچم ایران و نماد کودکان میناب حاضر شد
@Sportfars</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/464271" target="_blank">📅 05:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464270">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/764d1162f6.mp4?token=oz411r6-jz0nF8YWSrGi8CvMYmvbNz38IOEiQwKSwA9Auw9sC286fLK5IaPEMrlYe6EXlug1Hy4TW7h0qCAFvBdRSknvQOU6CiIfgcdQYGA2zJ4uIkCM70Kn66PR_cTGnJ14OcQtFTZoriq7abaUiS1nAlfXbzH7i8p__SdbfWdOHuQSlsPXUGoSMpkHgkN5iwgr_ccKoNna_8QqKdMpXP74wURk1n-35530Qph3THp9_5_Ey-G1fMAS51DlrYThy4LnScyH1JYKd9mGIrGlBJNd2EfcNqvsiIehHJjkcvyQZbnehZidhFtKNDmQPBFyKXdQ9L39W7uQDfgxOMYxgAIX2SaavoQUKKXR1HjwVeVy4ckti6b19LyevomW32WysVWmyUxz7j8afACX0J3VXZ5sJtimBp_Y514xKGs3O-VBGEyw_ln_ZzhKLCfWKtjylzY4F6ECMEyezKCSHfyCHQBlMFET6OCmcMZ8clU5ezSqiJVT7wA6XIKIYnPFDdtaxYwR0G2ks8ZxqQ1V8q_0TRL-tUChgYpK6MXHrv5zrVzD2Htz9pTSVqTHVmASkYDSRTCXHUF68gzjgYNSJ1GgiL_CMELpNWXNegEHj0ESMN5PckEBnMTgT23VrglbJiX-0fIWJR2ZXlLATE5KQf7CdhwlIPzghcMk-FZIQ2vgCXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/764d1162f6.mp4?token=oz411r6-jz0nF8YWSrGi8CvMYmvbNz38IOEiQwKSwA9Auw9sC286fLK5IaPEMrlYe6EXlug1Hy4TW7h0qCAFvBdRSknvQOU6CiIfgcdQYGA2zJ4uIkCM70Kn66PR_cTGnJ14OcQtFTZoriq7abaUiS1nAlfXbzH7i8p__SdbfWdOHuQSlsPXUGoSMpkHgkN5iwgr_ccKoNna_8QqKdMpXP74wURk1n-35530Qph3THp9_5_Ey-G1fMAS51DlrYThy4LnScyH1JYKd9mGIrGlBJNd2EfcNqvsiIehHJjkcvyQZbnehZidhFtKNDmQPBFyKXdQ9L39W7uQDfgxOMYxgAIX2SaavoQUKKXR1HjwVeVy4ckti6b19LyevomW32WysVWmyUxz7j8afACX0J3VXZ5sJtimBp_Y514xKGs3O-VBGEyw_ln_ZzhKLCfWKtjylzY4F6ECMEyezKCSHfyCHQBlMFET6OCmcMZ8clU5ezSqiJVT7wA6XIKIYnPFDdtaxYwR0G2ks8ZxqQ1V8q_0TRL-tUChgYpK6MXHrv5zrVzD2Htz9pTSVqTHVmASkYDSRTCXHUF68gzjgYNSJ1GgiL_CMELpNWXNegEHj0ESMN5PckEBnMTgT23VrglbJiX-0fIWJR2ZXlLATE5KQf7CdhwlIPzghcMk-FZIQ2vgCXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امتحان الهی یک نوع حل معما است
🎙
حجت‌الاسلام پناهیان
@FarsMaaref</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/464270" target="_blank">📅 04:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464269">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نشست اضطراری فرماندهان نظامی ترکیه، پاکستان و عربستان
🔹
عربستان سعودی، ترکیه و پاکستان در نشستی با حضور فرماندهان نظامی خود، دربارۀ حمایت از ریاض بر اساس توافق دفاعی مشترک میان سه کشور گفت‌وگو خواهند کرد.
🔹
بر اساس بیانیۀ وزارت خارجۀ عربستان سعودی، این کشورها قرار است پس از حملات انصارالله یمن از آنچه «حق ریاض برای دفاع از خود» خوانده شده حمایت می‌کنند. این نشست «فوری» توصیف شده است.
🔸
برگزاری این نشست در حالی انجام می‌شود که بسیاری از تحلیلگران در قدرت اجرایی پیمان نظامی میان سه کشور موسوم به «پیمان مکه» تردید دارند.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/464269" target="_blank">📅 04:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464268">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دو پرواز دیگر از مقصدهای ایران حذف شدند
🔹
سخنگوی سازمان هواپیمایی کشوری اعلام کرد فرودگاه بغداد و مسقط پذیرش پروازهای ایرانی را از آغاز امروز انجام نمی‌دهند، و در حال رایزنی برای تغییر پروازهای بغداد به فرودگاه نجف هستیم.
🔹
اخوان تأکید کرد که لغو پروازها…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/464268" target="_blank">📅 04:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464265">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XshJ3CJR7SrCQg7rA97f6JyLnOhZSBJHK_AiTynGxIplyPIKroezBNs7P_xYqLFjKbTNmBVOt1u8HpjoQueR9UpQCjF9Wd74voQzR3pQQEiPlv_cwLUnDU6W-Dfw5nni86OldwReITxXEe_svDTTZsYBKFKlelRTHKAXo82qeWP4l97zVUD8dAa1h0O3e_oaTa8pZberIAYBCFwDuQ8HrGUo3NFA1IGyIHqCGA7n_PqbgQx1uyHXPTY4AZ_zIVAyXfcckh4LfHOfUe75jM-BckZvdro971R3wN-X7KBZz3hG8BUD0idhtJGexxZd3QbGb425DSVHuSMjPZ5xLf8pSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27db3e2672.mp4?token=vWZkCNIOnDaOieFS0oPsbcsGFulhGcaLTsdGdh57d1VBTnK-SkPThtYFjNK3Nsz5FQ0c2jlviSu1JU8Pq1GjkZpGEpfjsZqdGxmuRQYFMp7QboYDK7o9sho5JG10ptR9r5RkeC_f07kRuZDqX1X2Y-XcfU0cpfgekbbXZPQnsl1oSob68BdH4I7bQrWQiDaS0w-9pZduBRAv5ZyIGoBZlESroXw4R_VgQavzh8rdVqkJG35PYRi_omWaZh553yT4P20n9f_SiiWazkbDGVOHSGHEtcvrdyrIaoOySZgcOdoZmO_4OEMpBbr1S3odNmu3rTGZvrsx1Q1V4Bv9tr4EhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27db3e2672.mp4?token=vWZkCNIOnDaOieFS0oPsbcsGFulhGcaLTsdGdh57d1VBTnK-SkPThtYFjNK3Nsz5FQ0c2jlviSu1JU8Pq1GjkZpGEpfjsZqdGxmuRQYFMp7QboYDK7o9sho5JG10ptR9r5RkeC_f07kRuZDqX1X2Y-XcfU0cpfgekbbXZPQnsl1oSob68BdH4I7bQrWQiDaS0w-9pZduBRAv5ZyIGoBZlESroXw4R_VgQavzh8rdVqkJG35PYRi_omWaZh553yT4P20n9f_SiiWazkbDGVOHSGHEtcvrdyrIaoOySZgcOdoZmO_4OEMpBbr1S3odNmu3rTGZvrsx1Q1V4Bv9tr4EhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر رژیم صهیونیستی تلویحا از برنامه‌ریزی برای آشوب و اغتشاش در ایران خبر داد
🔹
نتانیاهو: «می‌خواهم یک خبر خوش به شما بدهم؛ اتفاقی باورنکردنی در ایران رخ خواهد داد. روزی که چندان هم دور نیست، حکومت ایران سقوط خواهد کرد.»  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/464265" target="_blank">📅 03:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464264">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎥
عکس حاج قاسم جلوی چشم نتانیاهو در سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/464264" target="_blank">📅 03:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464263">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTh58vV7Cg-ENca2npkGq97mxbq1Q1996uUgL4T224zQ9qpZPA-LKceOGnauCX9hkrSi7PPWKR_8iDBrM4ejEltZw-Lw0DOgnj78PnywEu5x5LoiWNaFpzO5TflRhYQHWRfqBW-p68UyenV-CRq49WHpvCoM8VdAq2wx94VwbQhqJG2-ccM9Dfqvqct8vr-ssLmYf4FIkllx2cGEKLpXWrU0hSHW7z52yQckiaNENU5ST7Z6ITi7WIihJ8WUv-KrrhLusygQCWv_wqt1YJTyqh0_OEs_Pf6BE24w5MCARbcqgao9eqgHKm6LXfwlpJDRrY_7vLJQZ5ROMmBdVe2M0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری بیش از ۱۰۰ نفر از معترضان به نتانیاهو در نیویورک
🔹
پلیس نیویورک اعلام کرد بیش از ۱۰۰ نفر از جمله چند چهرۀ سرشناس و مقام منتخب محلی، روز پنجشنبه در جریان اعتراضات علیه بنیامین نتانیاهو، نخست‌وزیر اسرائیل در منهتن نیویورک، بازداشت شدند.
🔹
از جمله معترضان، سوزان ساراندون، بازیگر آمریکایی، بود که همراه با دیگر معترضان حامی فلسطین، بود.
🔹
بر اساس اعلام پلیس، «چی اوسّه»، عضو شورای شهر نیویورک، و «الکسا آویلس»، عضو دیگر این شورا، در میان ده‌ها نفری بودند که توسط پلیس نیویورک بازداشت شدند. پلیس نیویورک اعلام کرد تعداد بازداشت‌شدگان از ۱۰۰ نفر بیشتر بوده است.
🔹
«داریالیزا آویلا شوالیه»، نامزد انتخابات کنگره نیز در میان بازداشت‌شدگان بود.
🔹
معترضان در طول مسیر شعارهایی مانند «فلسطین را آزاد کنید» و «بی‌بی نتانیاهو، جنایتکار جنگی، را بازداشت کنید» سر می‌دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/464263" target="_blank">📅 03:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464260">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28eef03fb2.mp4?token=tr_HW0eFzV04tQ1Tojj5dFbzyiqnNYZNpj4lyvESHTbwnd-3CxdsgBWH2t7VhVtl9Ocj8MzWn15-jjbjIDDsDmjiNPIlUhNBVwQjtnb-fbhZtm3le2fSSz-H4Wc-vlSFaXcvXoZyeNeaBvus89_DfCT3UcUpvJ0u33mVjYZB4y3-XMMou65aB7X3C_m4WlJ8xgnV9xo6Bs-_qcNsetgaKT44LlxpEitHCh6A5ReNzGbLRoI9r0MHnQRey4KEGqqOTnTaN7IaDigIt6YdVuarxqHvzPN25Hs7D2BnfGW7rihYUv-gm-LKXyHh6PYzHtT7g0CWDy_VapyPRPRJZ4Sgfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28eef03fb2.mp4?token=tr_HW0eFzV04tQ1Tojj5dFbzyiqnNYZNpj4lyvESHTbwnd-3CxdsgBWH2t7VhVtl9Ocj8MzWn15-jjbjIDDsDmjiNPIlUhNBVwQjtnb-fbhZtm3le2fSSz-H4Wc-vlSFaXcvXoZyeNeaBvus89_DfCT3UcUpvJ0u33mVjYZB4y3-XMMou65aB7X3C_m4WlJ8xgnV9xo6Bs-_qcNsetgaKT44LlxpEitHCh6A5ReNzGbLRoI9r0MHnQRey4KEGqqOTnTaN7IaDigIt6YdVuarxqHvzPN25Hs7D2BnfGW7rihYUv-gm-LKXyHh6PYzHtT7g0CWDy_VapyPRPRJZ4Sgfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
دیدار عراقچی با همتای مصری، در حاشیۀ نشست سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/464260" target="_blank">📅 01:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464259">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtqqh8Eg5EaeSTapwdym6jigimcTeQFxjw-CgjCvtM5XQJ5aspNX9jPX3WEiStRPkY6YRaP-ArzohPLqYSuDb0pwriAZlA9Ne1earJpu9EPmQ7SQx6PBDK39AJt4lf5EHKRfnAYW3heuhJL7cRNpUEop3X8y6CSdYJHZo9wyS62FD396CvXzw85SgECyys2tj0gOYd_fFjxz0vQGxf8UTAebs-w0L0vcprutJ-9EVJTiO6mS5NlWEHFeaCaKdxOpBc9nQwrJD24q0jjlQU_Yjy43jOkOhZOJThv9-VpS2NmCFaazCW5NPIPiByYLAGoe-6-jYDwJ5q-Jblk2osoWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار فرانسه به ترامپ دربارۀ ممنوعیت صادرات گازوئیل
🔹
مکرون رئیس‌جمهور فرانسه به ترامپ هشدار داد که ممنوعیت احتمالی صادرات گازوئیل آمریکا موجب افزایش قیمت سوخت خواهد شد و این تصمیم را «بد» توصیف کرد.
🔹
مکرون گفت ما مستقیماً به نفت آمریکا وابسته نیستیم، اما چنین تصمیمی باعث افزایش قیمت‌ها خواهد شد.
🔹
به گفتۀ مکرون، فرانسه کشورهای عضو گروه هفت را دور هم جمع می‌کند تا بررسی کنند آیا لازم است بار دیگر از ذخایر راهبردی برای کاهش فشار بر بازار استفاده شود یا خیر.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/464259" target="_blank">📅 01:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464258">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d59a9154d0.mp4?token=RgN1u21Ngqrs-i9J6EiYzu6ZFlUEl6OtNo1agB4pzX4zq5Y6fn-QJmcEw31kiHCw-u6Nzf3UEw_7uVY9ltAQxbX_wopBWpyHcoCP6OEwr5jBnLOaYCdsQGHccVaLWAb9bPC_wuhJLs_sEeFnH6EPDMNMJR7B9sk6AjNo21kZ5eeYJdLf0zSZDv8VNv1Uioig8u0NttWJnDxNh9KdRcXHFFC0-WP3o3xB3YM0v1FuCfVHHOW7uOT5cVS3jzqgM8L3ItgMGwg-AYES6OzemR1ybkC2cnEGgkXn_Jb-hAIn9mTBaTSBt1UMLcKA89cYh_UI9pkyOyNEK5ANHU5eXvZz2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d59a9154d0.mp4?token=RgN1u21Ngqrs-i9J6EiYzu6ZFlUEl6OtNo1agB4pzX4zq5Y6fn-QJmcEw31kiHCw-u6Nzf3UEw_7uVY9ltAQxbX_wopBWpyHcoCP6OEwr5jBnLOaYCdsQGHccVaLWAb9bPC_wuhJLs_sEeFnH6EPDMNMJR7B9sk6AjNo21kZ5eeYJdLf0zSZDv8VNv1Uioig8u0NttWJnDxNh9KdRcXHFFC0-WP3o3xB3YM0v1FuCfVHHOW7uOT5cVS3jzqgM8L3ItgMGwg-AYES6OzemR1ybkC2cnEGgkXn_Jb-hAIn9mTBaTSBt1UMLcKA89cYh_UI9pkyOyNEK5ANHU5eXvZz2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شهید حاج قاسم سلیمانی از فداکاری و ایثار شهیدان در دفاع مقدس
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/464258" target="_blank">📅 01:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464253">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UC4cCozRHKtL4c6HiGSNly_0l0lrcI-McmJJYYClO2SsBpb6I5rN4UZ7f4t9ioDyxZqAM1uAEIIEXmHX6uBejxaDZmJOvxf8byOPC8hPFBF_0EYY7zdyb9H4pLsIZWPjGHFUKZtRmcm5pounJm0LXNSKOB7X4YDJjvcdhZjam3cNXb7DPbBxmmooNirhSKzfEi3gPtSASJHLrqGJXnRJMt12lmnptMkJedFCPUHsoE_c4xaP72cP-savglxeXL0oGFcfQoyTECv66tBSUfLC4dLKrillffrxwYQoghbCPjXhEsi-DLEcKUDYrq3xeHi2h4wQOLP6Jmye_5s3h74ajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GsnRYPqIme__kgUHQ16gA4b8zk3-_eHdryG5189N_RfMR0KgwWcDM3rKgvAklplSmLRwwXfZwnNrBx26t04JgVnWGcb0-THNEpE9m30zu5mYcg1CFlLlx_hxqacal5zja7P905bnpP4ABJoN-yfy7GrCpAsLSmQXdQXOFgj7tPOFVt4v3B6FOkE3LrxFitjInPHEE1c3mDxG2cIZ0XCO2KFaSZUesiQd3jylzmSXQJdV0eVakVnUzRmDfrx0LjIe6KZIb0GNnr2HVxjv1F2bH72wl37ss3Nl2JcJJBE2TR6Tb6zECiQBpPSFeZmHiKYkbiRMEju1OYh8MuCNE6qGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1kTkVsGPdyc7sEnqIO83Voq4N3hrE-DU0wE14V7gLcfQlcX5djV81S_Xq3X8_35FY4VhxtKGI73Qqd28RtAZ12IGRKszqiWGEiUFvk50A-xQ3kg6P4YBwkz8Ks77rrOB-zlZl62CP8eWJoIA9uQ6-wTxRFnsmiI7Pq1zKKt4PwSoz7SmM6nGIJEhSeuqAqpfbt1GdMY10fF5U7E0-S2uYn6ioI04qAgdvIlojftv-39uKdnGLzyUbhVvpeatstEJa_rUaTQKskJsIQShzuLC3O7WqjntfmQCetkZ01ve-UsXgvZToQXNnNSXqL2wXFjmFPD9eR1eCdYnjKG1aKeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jl8oPOfmUt1m2RKfPQTCO7UXSllRlvn-65uhboYUL4SP3M3BX6X1HCZawQut3RTLl1UsuM9vvKeqbJtfW1YECoRFmVYqMjLh41Ay-aLYBprYj9mfDeJ_BICB3xZM-NqoAhlUHb5BE2UapJjVryPQe2Ix3mSe8TBZUMyVy_GVZlbGBgR3ZXE557O0-6YCmdduErgKxqEmI5_g5pVV6AUhbtTFlRzN90nOYLX5xN8l6EpgzV7J-feP2VviBU0PKqwyZMkFjGGtntl9MkzEI6FXSAZkj90OpyC9f7oNypbA3-4kQDVu1KogOElEXA81OXcqv_HSmE4mPXDmHRY_sV95hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fIlMALo1_gVbCgE77KvheXtR7pu5f3NcKspP6V1RU5JwHTSLK4XLT4ohUZ6-vA-6k1KneuGgAdnhHJG2ydFkuOH8V08nL-GsU6iKvWpJildGuW4TSM7UOoGymMghGrRUIJAWkaJ44ZC5gpdYlu4oMDPmWy52d93JGjUt0TpSJx5dHFgRJ4V1Tq_Std7zWUIzlwF9JfXJIS3Hj5v1NCg1gbn1VC57Xv7-_X5wi6Go6mFwjb1R_wphC3pVA2czGGxa9sxUCVDTyf8jXYT_1dRgQbe3PBQ_Srr9LlRfCeb2j2ESq-80WsHXMZzYiGENDo6N_0QomYMOX0SXjOTcVXF77Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم ترحیم آیت‌الله شبیری زنجانی(ره) از سوی آیت‌الله سیستانی در قم برگزار شد.
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/464253" target="_blank">📅 01:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464252">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5594361bcd.mp4?token=IgIkHGUOTAsuhZ2ban-Jig4Kcgnw53jir15spP9lTTjgGE8kXG_KlB7OVIFs-L7y8ZOl-280ujLecTjWnr_Uoi9HI8N9p25J-kp2LueBL41HgaKr5FY0wxfx7dHPbJ5HVznFVzKyVWJqw2INfTDMBa4KlDA3ryEM7AUc3KQHI6hNQGUlwRB-bIPB-UYzT1kkFx1jYMNFtkDYXHSpCRB6Hh7HClsjuGu8yQdlSFcval0ncuJJXW9mVxydYdP_kroFOVXfpWlPDEUED-2mw_NYgMDS27SnOTWF-qHkcvZq8PdV5FgJ7VX2a5JZZWwHT4cWopTq8bZgPFzl676D3SzqfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5594361bcd.mp4?token=IgIkHGUOTAsuhZ2ban-Jig4Kcgnw53jir15spP9lTTjgGE8kXG_KlB7OVIFs-L7y8ZOl-280ujLecTjWnr_Uoi9HI8N9p25J-kp2LueBL41HgaKr5FY0wxfx7dHPbJ5HVznFVzKyVWJqw2INfTDMBa4KlDA3ryEM7AUc3KQHI6hNQGUlwRB-bIPB-UYzT1kkFx1jYMNFtkDYXHSpCRB6Hh7HClsjuGu8yQdlSFcval0ncuJJXW9mVxydYdP_kroFOVXfpWlPDEUED-2mw_NYgMDS27SnOTWF-qHkcvZq8PdV5FgJ7VX2a5JZZWwHT4cWopTq8bZgPFzl676D3SzqfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحه‌سرایی پرشور آهنگران در جوار مزار رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/464252" target="_blank">📅 00:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464251">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLwTOMbq8gxu6QtG1RMwufXkXzXkvfDG4QOjKapw4n7A3mAbQqnu-cANZMm7aYpCirpJ_HuQ2pq-mQE6lX5P00QxR7uePNRo2b7q9lm8YhMm5-ByOoeJ_KYzLSxhagyx6BArmwMu0ufHc2S5_0u99r_WXwYsERh0NCwUowGeHOECUII-P3iKxnVKxNL6QF_uRtK4EKXahB-pKMltKowEzDXG4wDJfzSnjso5EfVm9XnnLhq4TTnblArc-AmEJK7f8-GYitkW2hKbFKtw5pTypCtcqZSI9L-3O0YlQ__0Tze_jIeJ51MPnb31UpnwfZt8ujMn06gt3RisHxQDktiVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پزشکیان با نخبگان و صاحب‌نظران اندیشکده‌های مختلف آمریکایی در نیویورک دیدار و گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/464251" target="_blank">📅 00:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464250">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEEpR5_oPYN5ANgtJPEdbi2_eeAFudz4Ew31zSjwKGj34W_cZ_HBlq0soqbSzGfJ-0uOayZ5bz9E2jD-_nZZUvKZ3Z_PYv7wV76cQPNlDl4uYQGUWlT5CxdxtxjxW7fcXaBQA77MBwZyRbGgsYHZQYOu-bO6I_hIYosGPoMlhP3ayVtLqhbXy7qJZacTj5mFBGP2Z42WJg6Du64aQq_8kL8QLhqVKbC2ft96UnmtlWilkxrVgF7i0qCwjdY5VPdfjnWLc3suwzXkhEkXZIbB3M2LwyaXJUl1zutsr0RBVw0mNRnckYqnQ_aX9BRoKPATWxqvtRRswSG_MSdJ5GVEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: آمریکا با وجود نیروی دریایی گسترده، نتوانست تنگۀ هرمز را به شرایط موردنظر خود بازگرداند
🔹
شناورهای آمریکایی از محدودۀ تنگه هرمز ۴۰۰ کیلومتر فاصله گرفته‌اند و همچنان در بحرین مستقر است. این یعنی پیروزی بزرگ ایران.
🔹
این وضعیت نشان‌دهندۀ تغییر معادلات منطقه‌ای و افزایش توان بازدارندگی ایران در خلیج‌فارس و تنگۀ هرمز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/464250" target="_blank">📅 00:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464249">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSMM76rWEBprBd8u-msGznaVFTJFuddEG-xE_cay9ZZjxVtNGwetkkw2acUdTqcJ4W35QbpQLhhPJVyE64BpWip7SJNoBQ5stMmbZAws-sv4X2eYHaGkVKTu_h_XKeP8_30GPt_5YA-FKVMCvuJQRVM5ATsVaIA3qGNi0jYwF9WdWIqDMGg7ZwCfCgYnajaXge3lJ_eXDeaVXRyV9OV1_T5OfUJkDRaJc3pWpus59UUhrWnSlIkKRyy6LP9LF7liLWSVGRVapyxgvUd38Cmn7PpJwYX-voJvzNo5aKs3P1e6GkKBH8abjob2cIM5ypAX0H9EBEAF-jTOdKvGrinmmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط دزدی
🔹
مردی هوس کرد دزد شود و برای اینکه این کار را حرفه‌ای یاد بگیرد، به نیشابور رفت؛ چراکه شنیده بود در آنجا دزد ماهر و باتجربه‌ای زندگی می‌کند.
🔹
وقت وارد خانهٔ دزد شد و هدفش را گفت، دزد ماهر او را پذیرفت و تحویل گرفت.
🔹
سپس سفره غذا را که پهن کردند، مرد دست راستش را پیش برد تا غذا بخورد، اما دزد جلویش را گرفت و گفت: «با دست چپ غذا بخور!» مرد سعی کرد با دست چپ بخورد، اما چون عادت نداشت، نتوانست و دوباره دست راستش را درآورد.
🔹
دزد به او گفت: «فرزندم! در این راهی که آمده‌ای، اولین قدم این است که دست راستت را قطع می‌کنند؛ چون حکم شرع برای دزد همین است. وقتی دست راستت را ببرند، باید بتوانی با دست چپ غذا بخوری تا سختی نکشی.»
🔹
مرد با شنیدن این حرف به خود آمد و متنبه شد. با خود گفت: «به‌خاطر به‌دست‌آوردن کمی نقره و سیم، عاقلانه نیست که دست به این ارزشمندی را از دست بدهم!» پس همان‌جا کلاً خیال دزدی را از سرش بیرون کرد و از این کار دست کشید.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/464249" target="_blank">📅 00:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464248">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ولیعهد کویت: ایران از تنگۀ هرمز به‌عنوان برگ برنده در جنگ استفاده می‌کند
🔹
ولیعهد کویت مدعی شده که ایران از تنگۀ هرمز به‌عنوان یک برگ برنده در جنگ استفاده می‌کند.
🔹
او بدون هیچ اشاره‌ای به تجاوزات آمریکا و رژیم صهیونیستی علیه ایران گفته که اقدام تهران «نقض قوانین بین‌المللی و قطعنامه‌های شورای امنیت» است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/464248" target="_blank">📅 00:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464247">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyVBi0yEIM8WMphN5pdMXU0dcKGaDYWKJLMJnQTXwzX29hRMowf85AdsJ2fAtEaSHLhToxol785IbAG5A2nvou5SyBin3TfTDsnE9dMSN8yVZr92zBhYr-nU7ngR3QmL3f1cJajm2CukOLPl0msAHyNEZTBF95GLmBAOlV8m9HG__OQo3KyCyIA3PhBd0oK2ebu3hSEi04CbwCkjc1c2vs_tt06Frr9g3xitZF7Evtp9LTbcvwfD2uEgY5QAAMBC78N9hATAuEVVzBQdFgrjPDac12rn8dOK2azZgpMLfUneAL3QKGO8g0u0_0YAvUOKUfiVIxPDL9S_w7RBHeOPMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دیدار عراقچی و وزیر امورخارجهٔ انگلیس  در حاشیهٔ هشتاد و‌یکمین نشست مجمع عمومی سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/464247" target="_blank">📅 00:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464246">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tttAD_5EI1iyHsg-lUJJ-9HijIVqIb1p8L2L96fZMs0MwYAc-g9F9eQA5_X8rEv4e9q_MmtzQ6HWDBuO0xxj_7kxDNNVCSpAJobppW8DI9gRslC4KFMFP2h2Jkt2HLaPunOfzaS7unEpJAdgFC8o7OWnTBfM7YdspDhRWflCDXDAL_OD8YYgFk5nvuD4TUo12BrfL6tJcr9_bUto8t-MB3XRcxEV5VAoOJXaLLQXraitkB72Mp8vHUKF6ny0RQlQwfZB6fJKom3kEbbmp4c2m_dRUxJRvU3jEpvLUPqu3qO1G6-j0Jv7R8mrZ1NoZa-Kog5ODAONTq_1LxNbWouSpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند
🔹
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.  کدام پل‌ها مورد حمله قرار…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/464246" target="_blank">📅 00:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464245">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9464a14b0d.mp4?token=DxuUygCo4E-E5g1QSHWposjZQ1tb_b8jXe8koAC1LWlkohAmeKlYZ04mJ-62y8NXTTYjaL1E6Xzn9cnldaocQRm7aybnYeg-BM2szJP9O6GbStwLO68892CqyE5UnKKqitpFNj2DYoqDg4i6eaBXcbnGG0i41NsNuW4M8y2a8NrHAQPgKdTF7Ei7UW1arwKOHIGtamjnpqAPcgIbTm9JkX8qdp67DIA06fotn7RsEZWkh6HgKmTk9w0iQHNognl3ewBfWDPFPapk1tvN8dRtjeiQ2EEf6cKHkdCXrBy7-eHiZV5GbzLYJuGOay43CWviScDvlBfk8W-fdNmUAtUCUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9464a14b0d.mp4?token=DxuUygCo4E-E5g1QSHWposjZQ1tb_b8jXe8koAC1LWlkohAmeKlYZ04mJ-62y8NXTTYjaL1E6Xzn9cnldaocQRm7aybnYeg-BM2szJP9O6GbStwLO68892CqyE5UnKKqitpFNj2DYoqDg4i6eaBXcbnGG0i41NsNuW4M8y2a8NrHAQPgKdTF7Ei7UW1arwKOHIGtamjnpqAPcgIbTm9JkX8qdp67DIA06fotn7RsEZWkh6HgKmTk9w0iQHNognl3ewBfWDPFPapk1tvN8dRtjeiQ2EEf6cKHkdCXrBy7-eHiZV5GbzLYJuGOay43CWviScDvlBfk8W-fdNmUAtUCUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسیرهای تنگۀ هرمز همچنان تحت کنترل ایران است
🔹
کارشناس شبکۀ ۳ با نقشۀ تعاملی بررسی می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/464245" target="_blank">📅 00:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464244">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎥
مردم در میدان انقلاب تهران یک‌صدا فریاد «اتحاد» سر دادند
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/464244" target="_blank">📅 23:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464243">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727c2319e4.mp4?token=YNitUCIpQxEzLcAQb_lq0YjYmb0wG-Lm5wqLGBSULfYN2ulkxojx2YFYmjN5HJs-wzTTi9SF3FUzweIUr8CUEACaZ0bltVVjZBOHtmsxYN1qQ5GkPIIjCKFGopnuLAR7YoQFBp1z3GNplAQZ9TFaNUr0w4clAW6N4hfnwQY7hgNJK4KYLTuKVi7pS40z7dkAm_a_DhKj8YfQBP4xwMikvDl2IabCfxRnZUc9PECUtF33wMHo1YHW64NUTy0r3Ich9ircu8zSIR65WMlosAgcc3brMrD97TDEoJnGB8O9n4tLRoCTFZwhPncEPMIhbREIJ8EvGqi_vi9LxCDj9LTajA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727c2319e4.mp4?token=YNitUCIpQxEzLcAQb_lq0YjYmb0wG-Lm5wqLGBSULfYN2ulkxojx2YFYmjN5HJs-wzTTi9SF3FUzweIUr8CUEACaZ0bltVVjZBOHtmsxYN1qQ5GkPIIjCKFGopnuLAR7YoQFBp1z3GNplAQZ9TFaNUr0w4clAW6N4hfnwQY7hgNJK4KYLTuKVi7pS40z7dkAm_a_DhKj8YfQBP4xwMikvDl2IabCfxRnZUc9PECUtF33wMHo1YHW64NUTy0r3Ich9ircu8zSIR65WMlosAgcc3brMrD97TDEoJnGB8O9n4tLRoCTFZwhPncEPMIhbREIJ8EvGqi_vi9LxCDj9LTajA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم به سخنرانی رئیس‌جمهور در سازمان ملل چه نمره‌ای دادند؟  @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/464243" target="_blank">📅 23:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464242">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e7fb8772c.mp4?token=oqpX8__KO0oA8ZDjMPBukTL5YxHZxtvDmU7n7BSVi_2P3HGS1MRPZMQJj_Lf9RBUrN56jQ8ZHD5ILx0mmDPK_Vyxyu7Ed7x-9hilTgtKcZ-xNYW0qQeUn2WlWaIWQmYt01Kyi_gb4BA_X0_qFTzA5X7FZ8c-7jTA3oM2AoNC9j4xMBVMbdVEUzof70sGEBGZW5CODm_AbwzQIRNdyHINyv9239Ms1telIrI2CsyqPBgc4xLf6Uq2d7-xvu808tpqQejXs0jbnmGHxW1c6pJ2N9CZzzx9kXiXcvBZwcXN6AY5wfSPqJMmoNlLlHS5lg4HTVVvjDsuUGfDnmvYsBQe8lI84fVlnF1YV0gqVh52PLazh-D3Bem4Gjjc2sf3GgV2xzI9Uk0iyazWyGDKFYfSmKgaGb2a86OgZRau7T5nfys7WrSGbY7vLlU8HsGMmeBAfyoiNOXTAmQKS2jbqS5qd8yGm_8EbWJUEv0MTKHyzBugRt5ZUvXRVrU8Sr1uvPo9o7J68DHQRu8K_99uWL7TeTKIHdxPE5-Oy9Axx9dOKZRWrX-FMItY7Pgj5yRcpt9MBYE0sZdQqg7gc61ct068Dcy92yP-WnS5yjR2woSIAKpxev20H65jcx7gZhF1I0p2jMivV7uCG3uJUib2XzMO--zpKMRKPmNZRRR7-GR7JCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e7fb8772c.mp4?token=oqpX8__KO0oA8ZDjMPBukTL5YxHZxtvDmU7n7BSVi_2P3HGS1MRPZMQJj_Lf9RBUrN56jQ8ZHD5ILx0mmDPK_Vyxyu7Ed7x-9hilTgtKcZ-xNYW0qQeUn2WlWaIWQmYt01Kyi_gb4BA_X0_qFTzA5X7FZ8c-7jTA3oM2AoNC9j4xMBVMbdVEUzof70sGEBGZW5CODm_AbwzQIRNdyHINyv9239Ms1telIrI2CsyqPBgc4xLf6Uq2d7-xvu808tpqQejXs0jbnmGHxW1c6pJ2N9CZzzx9kXiXcvBZwcXN6AY5wfSPqJMmoNlLlHS5lg4HTVVvjDsuUGfDnmvYsBQe8lI84fVlnF1YV0gqVh52PLazh-D3Bem4Gjjc2sf3GgV2xzI9Uk0iyazWyGDKFYfSmKgaGb2a86OgZRau7T5nfys7WrSGbY7vLlU8HsGMmeBAfyoiNOXTAmQKS2jbqS5qd8yGm_8EbWJUEv0MTKHyzBugRt5ZUvXRVrU8Sr1uvPo9o7J68DHQRu8K_99uWL7TeTKIHdxPE5-Oy9Axx9dOKZRWrX-FMItY7Pgj5yRcpt9MBYE0sZdQqg7gc61ct068Dcy92yP-WnS5yjR2woSIAKpxev20H65jcx7gZhF1I0p2jMivV7uCG3uJUib2XzMO--zpKMRKPmNZRRR7-GR7JCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رستاخیز وطن در شب ۲۰۸؛ روایت اقتدار و مقاومت کاشمری‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/464242" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464241">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpGbleDLXPi2COZx1JPkzbnq9vKvQdcEh2t-DJQLk6ReoMzwceu0vY1Gl2m-iLZyaqpEFA07mTvp0o40iTlUaSF6QX1TbJHae1uLGIhJFHeTjvNDrUDStVYQsQ0GYQZ7ylI4t1Y2Iuugd2mA-atAwSCKSRf31F0abBr1alkToNQMvhBsX3HC8811q7me35iT7CdWes1Pa1dc4nlK6Y6iYEzdnqXJ2hwIYaX_JzGh8IGUrFuyl7wztSRuVjEC-5o2dIqSs3tiSLlRqbm_8vrlAKHS1XccfnOt7xCPQj1Ewu91O2l6j-dLamUA8Lh3WJ_s-l0oOA4GEskgz995NDdYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور در امور زنان: پیگیر وصل شدن کالابرگ و یارانهٔ زنانی که به تنهایی مسئولیت فرزندان را برعهده دارند، هستیم
.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/464241" target="_blank">📅 23:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464240">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1e3d63db.mp4?token=ph7NEtBAC4FqffOg4IIyeuzBzTf6-w0IxwpRFjAwiDxSr_E9w3IBlmklQOM6n4fDSDknQA-ykc3jXbsV3E7Tchgm9PnCCcY-wmAAjilRj10vg6bgDn7rkAwtB2WFWqlppkA0-28oVs4kspeyIIaE3gYzwNYmG3SfAw-683qIP7eqMeod03jc4D1-wcgKuIqmkhkdl3XWMgzj2_RtMhoIPCymGwGsklwuUfGnIUKE5RObDEkaQmua8ifh06svQAYOui4mQeXIWbUPgWrA9S1iStaiTfEg5-DsLJs6vxITgiDyL4-X5LE3Cu1cSKnKW5tL55pI2UiZApwgfNzzdBjuig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1e3d63db.mp4?token=ph7NEtBAC4FqffOg4IIyeuzBzTf6-w0IxwpRFjAwiDxSr_E9w3IBlmklQOM6n4fDSDknQA-ykc3jXbsV3E7Tchgm9PnCCcY-wmAAjilRj10vg6bgDn7rkAwtB2WFWqlppkA0-28oVs4kspeyIIaE3gYzwNYmG3SfAw-683qIP7eqMeod03jc4D1-wcgKuIqmkhkdl3XWMgzj2_RtMhoIPCymGwGsklwuUfGnIUKE5RObDEkaQmua8ifh06svQAYOui4mQeXIWbUPgWrA9S1iStaiTfEg5-DsLJs6vxITgiDyL4-X5LE3Cu1cSKnKW5tL55pI2UiZApwgfNzzdBjuig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احمدی مقدم، رئیس دانشگاه عالی دفاع ملی:  صدام هم فکر می کرد ایران را یک هفته ای از پای درمیاورد، اما ۸ سال در این باتلاق ماند
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/464240" target="_blank">📅 22:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464239">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQhzIEzDVGT6Wcm_6tF0qPjKRTOFuK_gCX2LqmXwHyJR7z0dDiXUt9SwoXr1fz3B05Fc3vX9gXNP2z5ZkI2Owi9q7TSQM_uRd5RyyYTLtYvo06Z3owutWVxAXZ95-OHVxpyDokESXI_Yu4PaB8bEIWIE6DmwW4TpHGNPprGPXZnr2KNs0drl4gAnwyBy_ig57uSzL98ZE6CGLS5vtV7OD0uPuQb9aHwwiwl1qaPJVwK-b2lQu_p2tS4nZBULPc_prraOHj9dLqwKdc7ThIa9HAzuPPhROOhAiR8RPCeRzbyZujFdxo9rKW3i4s8tjd_BpKzCk30nquJiXqdlUN8EQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
غریب‌آبادی: مشارکت اروپا در تجاوز به ایران بی‌پاسخ نمی‌ماند
🔹
اعتراف دبیرکل ناتو به انجام ۵۰۰۰ سورتی پرواز از پایگاه‌های اروپایی در حمایت از تجاوز نظامی آمریکا علیه ایران، نشان داد اروپا بخشی از زیرساخت تجاوز بوده است.
🔹
دولت‌هایی که قلمرو خود را در اختیار آمریکا قرار دادند نمی‌توانند از مسئولیت شانه خالی کنند. این مشارکت بی‌پاسخ نمی‌ماند.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/464239" target="_blank">📅 22:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464238">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
عکس حاج قاسم جلوی چشم نتانیاهو در سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/464238" target="_blank">📅 22:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464237">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsppmZWc5uL7nM7etlR5uRuztL2GwXDubuYkbV5r-37IVkgiV6LxIXY_HLC-DzHmPc3UT-NPrNuw5bTcKW7gjxcVsPx2fYhYCqbO3aBr_a2wQQQUmAACon7FB8VUyhwi69Z1KGb41mXViSz2nhp03Xy_UV6Mj7E3n6u3UZGDUU-vdw3YzdC4QWNgKlZ4hdW_QPjMqelSzdnVdt4V5xILkKuyWRmnn46S2msjHbdF5raEMK7--25bIsdL1gk_-_aIju7AsTyfHCVj64zN0Rmd-iA-c11spkfVu0EehExxqDpx6htmD1RZu0bUxMVJrwR_0p5qVyT1k8fjkzFipsoaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات ارتش یمن به عمق عربستان سعودی
🔹
سخنگوی نیروهای مسلح یمن شامگاه امروز از ۲ عملیات نظامی در خاک عربستان سعودی خبر داد.
🔹
یحیی سریع گفت در این عملیات‌ها، یک مقر بسیار مهم در ریاض و تأسیسات نفتی آرامکو هدف قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/464237" target="_blank">📅 22:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464236">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa14fb258.mp4?token=KcA3qAxDo-_XEZ8URlwu6Fr9-tQA7xSbxYkRoYAl2FeOzICJ8qUWKKRWtqmaxytKylGmFvlSJAIrBYyABpswiZ_kJ2EBNhFTPawS_dUHPrnfNAqRT18DBEa-pukH-ku8RZCMmBvcoTHqi5Xh74Jxp748bAMoDbnBkDhh7SAnRQcotDpSymShEKMItDFBEUKNSjU_YBAi3ZsAotj1gQqB1dxMjP5V_TipmOnjgEwbAD9SsZY1QQaCl8zT37iyyYzauNW0D2J-fNlCQRvajjQ2FdUvBG0wD3-w6pYRQZCYQFRXPM3EWQZhQ3eSXxo70HkTaq5H7H6wTKe2ROgYAHm_Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa14fb258.mp4?token=KcA3qAxDo-_XEZ8URlwu6Fr9-tQA7xSbxYkRoYAl2FeOzICJ8qUWKKRWtqmaxytKylGmFvlSJAIrBYyABpswiZ_kJ2EBNhFTPawS_dUHPrnfNAqRT18DBEa-pukH-ku8RZCMmBvcoTHqi5Xh74Jxp748bAMoDbnBkDhh7SAnRQcotDpSymShEKMItDFBEUKNSjU_YBAi3ZsAotj1gQqB1dxMjP5V_TipmOnjgEwbAD9SsZY1QQaCl8zT37iyyYzauNW0D2J-fNlCQRvajjQ2FdUvBG0wD3-w6pYRQZCYQFRXPM3EWQZhQ3eSXxo70HkTaq5H7H6wTKe2ROgYAHm_Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستاورد جدید محققان جوان ایرانی در حوزهٔ سلامت؛ داروی درمان کبد چرب التهابی
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/464236" target="_blank">📅 22:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464235">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb318597f.mp4?token=YOlPNz7sNKCkJt5irPqRoNW10RxyFLk1mqI0Cg7947jOwZWcW5vbdXgZ11Ta_P5zxrbxfy6ikr3G7CGsxwh5c-_MDZYw9bCfiYgwVWtNF2rf2X3uRNtl2UlzbwzPSOlD9D08okevW6DKX9oRVE1xzhl-vZcGGPyv1TnuOuIqP4iLZvXQGhhMNtWNO1O83923_UFSLKB399hJK25rziO69OBUhPrW6zQY3yMsp_h8udKGRXG0QhNISzfBjST7t_YXPKbSjOx3XyYnSkUKRUnEKIKruJG-b4CZp202bGCYqBH2cuDGzwG1eT9hQF8tZdAHvVkC0hrx3wcEIquPRCcBKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb318597f.mp4?token=YOlPNz7sNKCkJt5irPqRoNW10RxyFLk1mqI0Cg7947jOwZWcW5vbdXgZ11Ta_P5zxrbxfy6ikr3G7CGsxwh5c-_MDZYw9bCfiYgwVWtNF2rf2X3uRNtl2UlzbwzPSOlD9D08okevW6DKX9oRVE1xzhl-vZcGGPyv1TnuOuIqP4iLZvXQGhhMNtWNO1O83923_UFSLKB399hJK25rziO69OBUhPrW6zQY3yMsp_h8udKGRXG0QhNISzfBjST7t_YXPKbSjOx3XyYnSkUKRUnEKIKruJG-b4CZp202bGCYqBH2cuDGzwG1eT9hQF8tZdAHvVkC0hrx3wcEIquPRCcBKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار گرفتن تصویر شهید سلیمانی روی میز هیئت ایران هم‌زمان با سخنرانی نتانیاهو
🔹
رسانه‌های عبری تصویری از محل استقرار هیئت جمهوری اسلامی ایران در نشست مجمع عمومی سازمان ملل منتشر کردند.  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/464235" target="_blank">📅 22:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464234">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee49a98248.mp4?token=DShJxSRcsJZfieKe2CZQQvYUr6ejG4Rldzz76XMrlQKXiFEp8aBwZSJqVKL5OrM7Ho0zjiKWXbDD61Qma3iECTC-D_P_X4cFeLv5IiwOxk3ax9tUZecg-ZBamo5pu5wHWUIY0rEbyfetWrc7Erk0oahCpoyFe_VvX-PXhEjGG2SMMb0AosO3Fe4b7KRwFkYHE3dkGq5ugO6N54gC0tQ9vl3twX0v5fdzSYwbaNHYLx1hSOq4BmiVjtIee6coMPryPiFkHbZMDVi_nRaPPMzhBgiRI_GaomIKK4t2hXdNDyil724VcqnqVuev2TJ50J9ZKlNYgnn232dowKGDLECpNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee49a98248.mp4?token=DShJxSRcsJZfieKe2CZQQvYUr6ejG4Rldzz76XMrlQKXiFEp8aBwZSJqVKL5OrM7Ho0zjiKWXbDD61Qma3iECTC-D_P_X4cFeLv5IiwOxk3ax9tUZecg-ZBamo5pu5wHWUIY0rEbyfetWrc7Erk0oahCpoyFe_VvX-PXhEjGG2SMMb0AosO3Fe4b7KRwFkYHE3dkGq5ugO6N54gC0tQ9vl3twX0v5fdzSYwbaNHYLx1hSOq4BmiVjtIee6coMPryPiFkHbZMDVi_nRaPPMzhBgiRI_GaomIKK4t2hXdNDyil724VcqnqVuev2TJ50J9ZKlNYgnn232dowKGDLECpNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جملهٔ خنده‌دار نتانیاهو: متهم‌کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است!  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/464234" target="_blank">📅 22:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464233">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDqMl8tv5LH1t29Tuc0S7RTsJ2baRsY6GpBTua0877w4wrwbQjzxFnt1LPQpWX7LtnhyG16RSu_8PTfDGA6969FKQEeON3_SxSM25LzkwfqODSp2X5vZykKrUARyYg4KLRp6YM9Doci7xpa2GkTcaqrD1S6SFFQn9SbuQdQVEDJcaTEQtQTwUFdHXzcLV8ouzM-9rQTMQ7NHHow4GipgA81wSk4Z8m-i925m1KqpqbI9I_UJ8vHNR9fgEuC-q-2psazegwDR7ixnJUGZDYFhge_bWnuAvDL5IcO5MJIFvxNgtwuqFhAVruKjqORn1ARGPeLAgQ6qIaB9UVTZZoJ1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنا بار دیگر از جنگ علیه ایران حمایت کرد
🔹
سنای آمریکا امروز قطعنامه محدودیت اختیارات ترامپ در جنگ علیه ایران را رد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/464233" target="_blank">📅 22:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464232">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e8ded099.mp4?token=Zbu1uciT31hAylImG8ngo0eYMmqBFuUa0bvU2Gzohof2IwqpcF-E6XSi4rViFqJzVA8xpP-PLj-u2OfxDrJDek5N--2ytkzMkjUNNM-XOYvTWd1GSyJJ0YSEDlfgHg7xLYdlhXM8MGU6FbcAzS2EDAv-jt14-qlfOS8s-wERiUElsoGDbo8H0Vi4re7g8FBFfaneQGDMbpfbl3pcTeRK3_coRhRDcJ_t_ZxszcVTV1eMGReGFhxY9_YbPrITZiIdsflt1Apl5o2CuSOglyzzso1-xRbY43dgQLbIBpiwy_lfCPVi3YlJtgB6lvVQKxwj6E8FZ_pj--kGiAmKQFpoYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e8ded099.mp4?token=Zbu1uciT31hAylImG8ngo0eYMmqBFuUa0bvU2Gzohof2IwqpcF-E6XSi4rViFqJzVA8xpP-PLj-u2OfxDrJDek5N--2ytkzMkjUNNM-XOYvTWd1GSyJJ0YSEDlfgHg7xLYdlhXM8MGU6FbcAzS2EDAv-jt14-qlfOS8s-wERiUElsoGDbo8H0Vi4re7g8FBFfaneQGDMbpfbl3pcTeRK3_coRhRDcJ_t_ZxszcVTV1eMGReGFhxY9_YbPrITZiIdsflt1Apl5o2CuSOglyzzso1-xRbY43dgQLbIBpiwy_lfCPVi3YlJtgB6lvVQKxwj6E8FZ_pj--kGiAmKQFpoYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاتل ۷۳ هزار زن و کودک اهل غزه: اسرائیل مرتکب نسل‌کشی نشده بلکه از نسل‌کشی جلوگیری کرده است!  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/464232" target="_blank">📅 22:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464231">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3bd5cad7.mp4?token=MdbqtJBCDMQT2nU6rFij14Z4wpJCkE81ndjsxd3FZjS57copYJ1bXLwqEILYhxtSb_Q0sp7SkRQtGMd_SLvN6MfOPY3PlXjjtkseOmXYc7FeKFqXY2b2yc2DCVA7u4XQLRP73XRLgQh1URPUOXQcsapK43AUsYAJ4TvKvUMn_9hdUTn6FBwULssnoc5kC2SLiTEbATkMjrTAHM-4KRa7UC3jRDSkVQuL0RWXvONwmL0zTLMSG-4o365YXMhmK1il3jY066G3E7lsFfjSGeUlvEHtTtItdPoDW6PD4C4cYu5E-xhBrh1byIjEG0nUkbz8eMmRIPVnduwV-u7Z8KLoZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3bd5cad7.mp4?token=MdbqtJBCDMQT2nU6rFij14Z4wpJCkE81ndjsxd3FZjS57copYJ1bXLwqEILYhxtSb_Q0sp7SkRQtGMd_SLvN6MfOPY3PlXjjtkseOmXYc7FeKFqXY2b2yc2DCVA7u4XQLRP73XRLgQh1URPUOXQcsapK43AUsYAJ4TvKvUMn_9hdUTn6FBwULssnoc5kC2SLiTEbATkMjrTAHM-4KRa7UC3jRDSkVQuL0RWXvONwmL0zTLMSG-4o365YXMhmK1il3jY066G3E7lsFfjSGeUlvEHtTtItdPoDW6PD4C4cYu5E-xhBrh1byIjEG0nUkbz8eMmRIPVnduwV-u7Z8KLoZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر رژیم کود‌کش: ارتش اسرائیل، اخلاقی‌ترین ارتش جهان است!  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/464231" target="_blank">📅 22:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464230">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njIXv_T8mmGpMfFpD4upJp4NH4xOw9W6nAg3XyUAVRapwqRVcYcoR0tP3xLUtmNfFxJm87bWsIeL-n_r79pW0UcX8-9B3bmy3ZsTD3hZQlznXwXzlrUJsbVDPWgDjIA21GoVflNK-6qXfb3V-abkRjsehxpVdTOvNd3TMEHIoqCHW4nMbOZnsMyQCMqwoG-xfg7dEdNdS0C_E-rGvKo-wTm58m44dD_RDaGoPf8s33nDOQfXa_LiDMekDanG39IsW-sfFvc834sPtsSbYZf67u0xzzeB5T9OpeI4yowqXVipzPAD4KAwoefEvaFMzEgrU9AuLltHSBEpE2_YVZ_n5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایندهٔ امارات پای صحبت‌های نتانیاهو نشست
🔹
درحالی‌که هیئت‌های بسیاری از کشورها حین سخنرانی نخست‌وزیر رژیم صهیونیستی سالن سازمان ملل را ترک کرده‌اند، نمایندهٔ امارات درحال گوش‌دادن به حرف‌های نتانیاهوست.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/464230" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
