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
<img src="https://cdn4.telesco.pe/file/D8SVRKDX2tCCo42UXZo82YZccSi1ZnzwhQC-jwFr-aYitVhesNp5M0ZartY1hZcWbUA8A3LFprTU__cLwPM7hJM_AHcIPwRdRuLRlTQguqdMjNylyvahdq9RCT1PEBk_XY-j3gxFcMio_FBRuJf8t0PQHa1qG1hGWq6CXL5u6oM685Xn0L5kveYom6t2Fu3IWffjcBqASEdc3nsxDeD2LsuaWgXqSXrGv8VOr-GkYejwt2B-n0m6YvWBBpGEaN43yVmJbE8ZHksyE9u2EoRNOLF_lZoJwOIvIL8EkUKdsP9qRAHl2meVUdall0vWMdIWM1994hpkXMy083AL4do06w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 947K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 23:28:45</div>
<hr>

<div class="tg-post" id="msg-145482">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ارتش اسرائیل: عملیات پاکسازی دو تونل زیرزمینی حزب‌الله در ارتفاعات علی‌الطاهر در جنوب لبنان به پایان رسیده و اکنون در حال خنثی‌سازی این زیرساخت‌ها هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/145482" target="_blank">📅 23:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145481">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (CENTCOM) اعلام کرد که نیروهای آمریکایی مسیر ۸۷ فروند کشتی تجاری را تغییر داده‌اند، ۳ فروند را غیرفعال کرده‌اند و ۲ فروند را بازرسی کرده‌اند تا از رعایت مقررات پس از تشدید محاصره بنادر ایران اطمینان حاصل کنند.
🔴
این تعداد شامل یک کشتی بیشتر است که از روز چهارشنبه تغییر مسیر داده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/145481" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145480">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
گاردین: رئیس سیا در سفر به روسیه از مسکو خواسته حمایت خود از تهران را کاهش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/145480" target="_blank">📅 23:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145479">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
‏ کانال ۱۴ اسرائیل مدعی شد
🔴
پاکستان و قطر طی دو هفته گذشته دو بار از ترامپ خواسته‌اند بخشی از دارایی‌های مسدودشده ایران را برای کمک به کاهش تنش آزاد کند، اما ترامپ هر دو درخواست را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/145479" target="_blank">📅 22:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145478">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L30w30cPBR-l224taXYouXbYjhRp-a3x_33bMcPkg0XC24WUamadIEXsN6-VFXdTIECkuJ-4P5377nbiD40vFid1ZZGcTI3u5HBVXAaU10w-Nt4N9OrUxN0bKe1oi-H0BFt_274FDJNb0Kl4BF0cGLqwHxQt_NujzkNZ-PO33ByVT2x_G2jI-od_7bV-vRrRCgPYieO4luGZyHUfx8PIo0GaK6e26HsyjDyyxAw2YJdNgLTyuPD08pAQOGUug-1fx45vSAKJIza8HEiQuAE6SHdVSEyPAZ_gAbs9F2krpfebxdW9LQiJ4Fgqe9tLkKq5mip6mbts_4YwcA1J8YY7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت نتانیاهو پس از خبر تسلط بر ارتفاعات علی‌الطاهر: با ما درگیر نشوید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/145478" target="_blank">📅 22:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145477">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH7rjFgM3YNVPGiG4KVG2ofZXctb3l_2Lu45oDEDgzKG1l-NnrM8mUrGXDYnNgyl8AiRwj3UW7J-tWnNPrLAAEsDyUJkB24bt8CBUAbOAqGx4BJEzslWyDcPBle_WeV3HK_aVq-UB1pvEsr9p572np6BIBhwCdE-uE0exzT8avnzuZF0rKzIcgXXTQSJ0Qh2AVPI81QTL09g02UTdJqdGcuNfNSJJjXlP3q1M3rvAb8-zu2lacDjYis-G-HmwZ5ei96Cs--65VTI3BPVQcs3I2_VjPeA5ZEp03_RZG-oOeypER5LduQJiuJOQs8qYZKTbf3gGOR2NgQdeoLSx1W7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به روستای المنصوری جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/145477" target="_blank">📅 22:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145476">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOtRTrRxftFW_wCAWH-u49d99ZQV0lw-wckn37A67pt4p8L3bixiBEOTjAVIu6spTSdPIlA5U48yrPNUK7OAdzIFluOsjSkxTwrcn4J8L7tq5L-I-3QGGz-eK1LZfKmPy8bUGwvxU-hjz3QOYax3Nxzf9sEGIFIpTxAqEixeJ00tvgFexDfAYwhVPE5zlENoyaYKf4EO2hYPQ0ymAGomjEuN5DenJNSvRwhoIepUmFGmFRJGvOKbPLj1P-usf9t9GX4W1M_rsZZ8hJ12Yb6SmRjMZurc_nKELPzqR-d0XyqJBZftm7mD4t81nck-wGgnXpThYka0aUK4ahVNtfWY0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه: امروز من نوه‌ای از راوول کاسترو به نام فیدل ارنستو کاسترو کالیس، بانک بیرونی کوبا (Banco Exterior de Cuba) و چهار نهاد دیگر را که بخشی از شبکه فاسد مالی و اطلاعاتی کاسترو هستند، مشخص کردم.
🔴
دونالد ترامپ و من در تعهد خود مبنی بر اینکه کوبا آزاد خواهد بود، سست‌ناپذیر هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/145476" target="_blank">📅 22:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145475">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a60eb3a2c.mp4?token=tLnpRKEZ53pYaYSK__OwjbHYiGVJpVksEV1-ygQnMlYO5-ka1oz4ojFfNYjfBqagxiHYlWQIElMRzIFOWm7b3ANUOMc_L2nB_EiOY5aokXTBovEJfVf5UibNz7gFGA5bFYXCMFd4Q5fDioL0fBLfP7dc8SqNa9Y9KigpjicBTWg9Kt24z2YAK1g23PvNvp3ScncQ53ebTpXKe7f_yshG011_gGJkHSGYhyAtUuhDdgL2aAlyvmfreVvr7i7INKlbI8pI9hx5AT3SfJNYoL2yF2rTIWbNios6K1HJypVg25r-duok8FdbkhKmkWph-mqu9BEIK71EfIJSWSqGgMdjOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a60eb3a2c.mp4?token=tLnpRKEZ53pYaYSK__OwjbHYiGVJpVksEV1-ygQnMlYO5-ka1oz4ojFfNYjfBqagxiHYlWQIElMRzIFOWm7b3ANUOMc_L2nB_EiOY5aokXTBovEJfVf5UibNz7gFGA5bFYXCMFd4Q5fDioL0fBLfP7dc8SqNa9Y9KigpjicBTWg9Kt24z2YAK1g23PvNvp3ScncQ53ebTpXKe7f_yshG011_gGJkHSGYhyAtUuhDdgL2aAlyvmfreVvr7i7INKlbI8pI9hx5AT3SfJNYoL2yF2rTIWbNios6K1HJypVg25r-duok8FdbkhKmkWph-mqu9BEIK71EfIJSWSqGgMdjOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هر گرم طلای ۱۸عیار 23,600,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/145475" target="_blank">📅 22:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145474">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nz2oyxHank9SufFrf7umgsHh5BVZVJvzpbtSTNabVThqdh68Lt_hsxcBs3y2_U_AoB4mpbj0W-jwSfZMO6oWCM3CZsCLna0AvKZjcH43qL5LmASVgt3vScRFzfRSx42lreLNIhIp9_fSEeQYCy5sZWKlUfDnjIaBol9GyLoFwBlWlWlQ_gQPo5dJ-ViD2rurZZ2RmXZVKrhUA5T3fYM3s8JMPzCQBhZXfJndpT8MwepwbT8VbtQLVx3188fad-VMjA8w3ggS7MCY7m9S8L1wdm-J32vMoPbi54Bgrjte4vFt691-oIQkJbXu0_1dBd9Yq6jiEf8e4nFArR20MDcLxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایمز اسرائیل
:
گزارش قبلی رویترز مبنی بر اینکه ایران به آمریکا هشدار داده است که به هرگونه عملیات تهاجمی اسرائیل علیه علی طاهر واکنش نشان خواهد داد، کاملاً بی‌اساس است.
🔴
نیروهای دفاعی اسرائیل (IDF) از چند هفته پیش در تونل‌ها حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/145474" target="_blank">📅 22:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145473">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">۱۸ نظامی امریکایی کشته شدن!   رویترز گزارش داد وزیر بازرگانی آمریکا سخن قبلی خود مبنی بر کشته‌نشدن هیچ آمریکایی در جنگ با ایران را پس گرفت و تأیید کرد که ۱۸ نظامی آمریکایی در جریان جنگ با ایران کشته شده‌اند. این رقم مربوط به کل درگیری است و رویترز آن را مشخصاً…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/145473" target="_blank">📅 22:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145472">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ونس : اگر به ترکیه، آذربایجان، قطر، امارات متحده عربی و عربستان سعودی نگاه کنید و به طور کلی به سراسر جهان بنگرید، در واقع شاهد تعداد زیادی از کشورها هستیم که گاهی اوقات حاضر به بیان علنی این موضوع نیستند، اما در پشت پرده کارهای بسیار خوبی انجام می‌دهند تا به ما کمک کنند تا اطمینان حاصل کنیم که ایرانیان به دلیل شلیک به کشتی‌های تجاری، مجازات شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/145472" target="_blank">📅 22:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145471">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ونس : هرچه بخواهید درباره چین بگویید، آن‌ها از آن دسته کشورها نیستند که به دلیل نپذیرفتن خواسته‌هایشان در یک اختلاف‌نظر بین‌المللی، به کشتی‌های تجاری شلیک کنند.
🔴
آن‌ها قطعاً مسئولیت‌پذیرتر بوده‌اند، هم از ایرانیان و هم از چند کشور دیگر
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/145471" target="_blank">📅 22:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145470">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ونس: ما می‌توانیم منطقه را ترک کنیم، اما کشورهای عربی حاشیه خلیج‌فارس به ما می‌گویند این بدترین اتفاق ممکن است
🔴
با وجود اختلافات سیاسی ما با چین، آنها مایل به همکاری با ما برای اعمال فشار بر ایرانی‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/145470" target="_blank">📅 22:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145469">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/996568e758.mp4?token=tCQjwsx_gw17aOGFJcnDnvBBgCXaR5iTIUfRiGBzs568jl9PT15K8WBatgUjOS1bu1kr9jzh90UzNTHUNCMGe6rDrVbC2eV2X9p7Tlex0-tLf1l47c_uY57u2VIxwkGQ2zT0xE5C01ji6U4Js6KGPq-ZL3humRmoCxqxbXDAypx1Rts-PKQgFBubgP00i1aPwSOW5EKylaAS57IChVQd3QngnyZSihfXehMHfeinDKYDbI8U6ev8hTBs0CNko47tTXWZnxHqGPKicFLksbHxfzftqd1zbmmzVqKa1B30FbrG8C80JL-Aj3JgL3NvxcnaXDnqGtZbrYYljHV6g_jzPSDhKpT90zcQA2e5BbnqcPedem5JzmTsJj0zGo7bhQZsb6W2yDr5GWe7vvgUoMuwz3KR_SksseEcModJiaxeD8zCyEpsDn-Y9KlD1veTLQj8Pq3tB6oFuq09QhVV9eoVSB-MqbcmXLhA9cl1jhEn5c04qwik0D0_1E57A5wQCFpFozzYr_4G6qILhWUI-7lC2Mf0ed8ikm2WmlxcGOeMdY9oiBxb7oioFQKQbZGPka6yB1_kGFPYViSnZwyRiAiksFkZIzxFyKC2Ac9T-K5v_rTtlH5DBkfGS65XByAIyGB1rNYONMrxbEwKZtv3AhFlt8cYLoyGMDGF9Vvr9FVMFoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/996568e758.mp4?token=tCQjwsx_gw17aOGFJcnDnvBBgCXaR5iTIUfRiGBzs568jl9PT15K8WBatgUjOS1bu1kr9jzh90UzNTHUNCMGe6rDrVbC2eV2X9p7Tlex0-tLf1l47c_uY57u2VIxwkGQ2zT0xE5C01ji6U4Js6KGPq-ZL3humRmoCxqxbXDAypx1Rts-PKQgFBubgP00i1aPwSOW5EKylaAS57IChVQd3QngnyZSihfXehMHfeinDKYDbI8U6ev8hTBs0CNko47tTXWZnxHqGPKicFLksbHxfzftqd1zbmmzVqKa1B30FbrG8C80JL-Aj3JgL3NvxcnaXDnqGtZbrYYljHV6g_jzPSDhKpT90zcQA2e5BbnqcPedem5JzmTsJj0zGo7bhQZsb6W2yDr5GWe7vvgUoMuwz3KR_SksseEcModJiaxeD8zCyEpsDn-Y9KlD1veTLQj8Pq3tB6oFuq09QhVV9eoVSB-MqbcmXLhA9cl1jhEn5c04qwik0D0_1E57A5wQCFpFozzYr_4G6qILhWUI-7lC2Mf0ed8ikm2WmlxcGOeMdY9oiBxb7oioFQKQbZGPka6yB1_kGFPYViSnZwyRiAiksFkZIzxFyKC2Ac9T-K5v_rTtlH5DBkfGS65XByAIyGB1rNYONMrxbEwKZtv3AhFlt8cYLoyGMDGF9Vvr9FVMFoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ماریا بارتیرومو از فاکس نیوز رفت. آیا او قرار است سخنگوی بعدی کاخ سفید شود؟
🔴
جی‌دی ونس: نمی‌دانم، رفیق. نه، فکر نمی‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/145469" target="_blank">📅 22:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145468">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754c0d566e.mp4?token=s9dA--EzXXAe4GAX-t5j-bMdjCmw3A3rtoy0WIXkC3-vm3DvNb8riE6oRVC8-cjAr9npboLt6vMOXl-vSPuqt_f-Zqu7t0PgesXs_wWAPpLnGEHOMKAqLIiOAAt_866Hc5nOwjtYaea7IVA3aukEt_Sz9JJBheheVbSpiko6G0ENyqEI0vnkp1fASuultQDvMqsxhtfFysv5T8b6o3-X-rKCjphZtRhV-17_f0_zLU46D0CRP_iYUV6B0Bq6zqfKjwog-hp_7Pns3EnzWxz71fAQMLZcDfgS5ynVEEjgCEIq4KZOAj1Go6x2gBjmVE8NuacjH6f1TGbAOWJl3oYEHiwWgXvZy9qe1yVbXOLuQMHnsGGbem4aZe7TBgteXHF4U1xvP3b4xe3EripIA6ecjVAYIGD1pvOrNNzNZj1zIMb0b1C-QjEUDhV0AMrQz1FAkateVCBm4bvntFsIGFAEV0bYquSnzjqDQ0NsLf1ks7oX3m-xNLilNOjIecN6ZTAvwSG_hj_K049ejDXU6nnTA51EXH-eQGNYX8Dip_fHaTTC9ZIjgnDt7LPUscIYyT7CRd3Xhqm2SzZ2bqR9ApTtAIjUCQ78P-XHtzY-agDXEvA7VQFTuG8zU4hoqJmYG7V-UX5frLmfwYnCX0eiN798MG_2szEZIrhz5WQIBOHNEM4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754c0d566e.mp4?token=s9dA--EzXXAe4GAX-t5j-bMdjCmw3A3rtoy0WIXkC3-vm3DvNb8riE6oRVC8-cjAr9npboLt6vMOXl-vSPuqt_f-Zqu7t0PgesXs_wWAPpLnGEHOMKAqLIiOAAt_866Hc5nOwjtYaea7IVA3aukEt_Sz9JJBheheVbSpiko6G0ENyqEI0vnkp1fASuultQDvMqsxhtfFysv5T8b6o3-X-rKCjphZtRhV-17_f0_zLU46D0CRP_iYUV6B0Bq6zqfKjwog-hp_7Pns3EnzWxz71fAQMLZcDfgS5ynVEEjgCEIq4KZOAj1Go6x2gBjmVE8NuacjH6f1TGbAOWJl3oYEHiwWgXvZy9qe1yVbXOLuQMHnsGGbem4aZe7TBgteXHF4U1xvP3b4xe3EripIA6ecjVAYIGD1pvOrNNzNZj1zIMb0b1C-QjEUDhV0AMrQz1FAkateVCBm4bvntFsIGFAEV0bYquSnzjqDQ0NsLf1ks7oX3m-xNLilNOjIecN6ZTAvwSG_hj_K049ejDXU6nnTA51EXH-eQGNYX8Dip_fHaTTC9ZIjgnDt7LPUscIYyT7CRd3Xhqm2SzZ2bqR9ApTtAIjUCQ78P-XHtzY-agDXEvA7VQFTuG8zU4hoqJmYG7V-UX5frLmfwYnCX0eiN798MG_2szEZIrhz5WQIBOHNEM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس : ما با اطمینان کامل احساس می‌کنیم که سرزمین مادری در امان است. همچنین با اطمینان کامل احساس می‌کنیم که مقامات جمهوری اسلامی قصد انجام کارهایی را دارند که توانایی انجام آن‌ها را ندارند.
🔴
مردم آمریکا باید بدانند که دولت آن‌ها با تمرکز وسواسی، هم بر پیش‌بینی هرگونه تهدید سایبری بالقوه و هم بر پاسخ مناسب به آن‌ها و اطمینان از عدم وقوع آن‌ها متمرکز است.
🔴
اگر به توانایی ایران در اختلال‌آفرینی در زندگی عادی آمریکاییان نگاه کنید، فکر می‌کنم این توانایی بسیار محدود است. صفر نیست، اما بسیار محدود است. من بیشتر نگران حملات سایبری از سوی بازیگران دیگر هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/145468" target="_blank">📅 22:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145466">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ونس : وقتی می‌پرسید «این جنگ تا کی تمام می‌شود؟»، در واقع دارید از من سوالی مثل «ایرانی‌ها تا کی به کشتی‌ها شلیک می‌کنند؟» می‌پرسید.
🔴
من پاسخ این سوال را نمی‌دانم. باید از ایرانی‌ها بپرسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/145466" target="_blank">📅 22:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145465">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5614d226b.mp4?token=etJC8ev88e_PoNoMFaoy5oIpVKik2A3FT3fApSzIQ8VIYXEQJaOFWUiSsHRzF3pMpam8TbujYlDJkU2Z30lb7JK9sNLUGwqB1gx6Y6HqA6HZFSity5IzrAVU9NygJ-T278i_RbeQxBICrwIUSNNE8nZ8WboE0HpCjXy9PSBplsGsdTDncVyrIeWCy2nh1-ksQffYelaOjLjMYMFAsJQar3bHGZ2BZX0HfagMGuiz0_FtP9b1ZkDwJBit22CUQkq0OWoOzGhGX-4pw1hoduJZQxNsPSgiLZn_6HAoLxRoCAgiLJQFS1aFUx18vi_Fcu4JL83F2KKM-z9BrmIlCYGmeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5614d226b.mp4?token=etJC8ev88e_PoNoMFaoy5oIpVKik2A3FT3fApSzIQ8VIYXEQJaOFWUiSsHRzF3pMpam8TbujYlDJkU2Z30lb7JK9sNLUGwqB1gx6Y6HqA6HZFSity5IzrAVU9NygJ-T278i_RbeQxBICrwIUSNNE8nZ8WboE0HpCjXy9PSBplsGsdTDncVyrIeWCy2nh1-ksQffYelaOjLjMYMFAsJQar3bHGZ2BZX0HfagMGuiz0_FtP9b1ZkDwJBit22CUQkq0OWoOzGhGX-4pw1hoduJZQxNsPSgiLZn_6HAoLxRoCAgiLJQFS1aFUx18vi_Fcu4JL83F2KKM-z9BrmIlCYGmeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
:
در مورد جمهوری اسلامی آیا جنگ تا انتخابات میانه‌ای تمام خواهد شد؟
🔴
جی‌دی ونس
:
من آن را جنگ نمی‌نامم. در حال حاضر شلیک فعالی وجود ندارد. من می‌پذیرم که در برخی مکان‌ها این تنش‌ها تشدید شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/145465" target="_blank">📅 22:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92f8eb7ba2.mp4?token=CPrwGebi0ErTlYQ8QH8emolGHi4zpHdpC-8fbFdb2IKN-ST1g2O1oBfeKDb3jiTyaEN1ge5NOlZyBzXfqb3v1x3fFcmQte6kRY1sF7M6M0rtkXs3KDUMAi6XfILJaHTrwtbcSwxFXmWa-JFKOMfTcV1qF9QYnnBgajk0x5LVlBPX3w2DOuvmRXlgeI2xQqiVtyFSio4Zah4jbStexecjJ8xwlNUJgTXfa8dw3H54lTo0WTHC--5ls0EWJngRMNODVBii7-i_JFQkxuhyqixkoanAAJdqWRh6kNjWRDwtpxkOnJIKmoS-WT3DAGmaL1jfQwZNQegrZkKS6OPmfkKfig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92f8eb7ba2.mp4?token=CPrwGebi0ErTlYQ8QH8emolGHi4zpHdpC-8fbFdb2IKN-ST1g2O1oBfeKDb3jiTyaEN1ge5NOlZyBzXfqb3v1x3fFcmQte6kRY1sF7M6M0rtkXs3KDUMAi6XfILJaHTrwtbcSwxFXmWa-JFKOMfTcV1qF9QYnnBgajk0x5LVlBPX3w2DOuvmRXlgeI2xQqiVtyFSio4Zah4jbStexecjJ8xwlNUJgTXfa8dw3H54lTo0WTHC--5ls0EWJngRMNODVBii7-i_JFQkxuhyqixkoanAAJdqWRh6kNjWRDwtpxkOnJIKmoS-WT3DAGmaL1jfQwZNQegrZkKS6OPmfkKfig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس : دیروز شب، ۱۵ میلیون بشکه از تنگه خارج شد. این به دلیل ایالات متحده است.
🔴
اگر ما این کار را انجام نمی‌دادیم، هیچ‌کس دیگری آن را انجام نمی‌داد و اگر هیچ‌کس دیگری آن را انجام نمی‌داد، با یک بحران انرژی جهانی فاجعه‌بار مواجه می‌شدیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/145464" target="_blank">📅 22:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ونس : ابزارهای اضافی زیادی در اختیار داریم.
🔴
برخی از این ابزارها توسط رئیس‌جمهور استفاده خواهد شد و برخی دیگر نه، اما من قصد ندارم دقیقاً تبلیغ کنم که چگونه در ماه‌ها و سال‌های آینده با ایرانیان تعامل خواهیم داشت، زیرا صادقانه بگویم، این کار فضای تصمیم‌گیری رئیس‌جمهور را از بین می‌برد.
🔴
اما هر آنچه ممکن است رخ دهد، روی میز است: فشار اقتصادی، فشار نظامی، فشار دیپلماتیک، فشار مخفیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/145463" target="_blank">📅 22:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/129206ce04.mp4?token=Jlxlw_H9QqLr5jKu1nnaTW5i3iSf6Z34F34tnXxTRLlmeY8_xd1HoHj0gg-n42r51WASbLkfbscgxFBd5KG4iinQij12tEdz5ItshuRjlMUQcr3LOz9m3py4IgpgxhfMt7HNTNT38Z2qWIXg7Z7vN210nPP-tOXt1E6WM9E_xOYC3QDo_yL9G3M_37nspvLZflKhDyT9XL6FsLFcMSOrjN4sDkVOaq1zzKWBlHtldagVy7ager9tgQzvX9QiP32pwevJKxs_NWnTNJmHQK8zXiSs8suMKvUgtGwxHvy14s7pOwym9y4V2Ruwwcr6uwgVK_zzdtyBIPNJ0z9gY1RoOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/129206ce04.mp4?token=Jlxlw_H9QqLr5jKu1nnaTW5i3iSf6Z34F34tnXxTRLlmeY8_xd1HoHj0gg-n42r51WASbLkfbscgxFBd5KG4iinQij12tEdz5ItshuRjlMUQcr3LOz9m3py4IgpgxhfMt7HNTNT38Z2qWIXg7Z7vN210nPP-tOXt1E6WM9E_xOYC3QDo_yL9G3M_37nspvLZflKhDyT9XL6FsLFcMSOrjN4sDkVOaq1zzKWBlHtldagVy7ager9tgQzvX9QiP32pwevJKxs_NWnTNJmHQK8zXiSs8suMKvUgtGwxHvy14s7pOwym9y4V2Ruwwcr6uwgVK_zzdtyBIPNJ0z9gY1RoOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: در مورد ایران، آیا این درگیری تا زمان انتخابات میان‌دوره‌ای به پایان خواهد رسید؟
🔴
جی‌دی‌ونس: من این رو یک جنگ نمی‌دونم
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/145462" target="_blank">📅 22:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51942fb259.mp4?token=pAr0T5qXsem0eEGbI4wLYn5TktFFU0ycdTpgP3VImFq9aZxRDB_rbEbUY2AzwF4mJsI5lyJR2afPrvcZxcDG56NvaPhmFLeVhfpvtABfMFHwSn6iPLWRg6q8075MKwbUCAWZkfR5Y4GUZ8QfQyhqIleJ6_4cIEP0AIn0Z46yBzpeM6SFG4-58RtrmVGmaziGLaGOA3q6dpdTD3qrzxI3jt93aOvJbuMZqkNiYXDvS3BnvcbydZJ9GB5k_0bHsdi7pvyGKrkTUzcwK6WmB5mfv_1r2UOkrwoIYAQfeH8kF2rtMxMIwgDbb1GAVXfiDwdpwqmSNYMvxBZwJQ5afyDcDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51942fb259.mp4?token=pAr0T5qXsem0eEGbI4wLYn5TktFFU0ycdTpgP3VImFq9aZxRDB_rbEbUY2AzwF4mJsI5lyJR2afPrvcZxcDG56NvaPhmFLeVhfpvtABfMFHwSn6iPLWRg6q8075MKwbUCAWZkfR5Y4GUZ8QfQyhqIleJ6_4cIEP0AIn0Z46yBzpeM6SFG4-58RtrmVGmaziGLaGOA3q6dpdTD3qrzxI3jt93aOvJbuMZqkNiYXDvS3BnvcbydZJ9GB5k_0bHsdi7pvyGKrkTUzcwK6WmB5mfv_1r2UOkrwoIYAQfeH8kF2rtMxMIwgDbb1GAVXfiDwdpwqmSNYMvxBZwJQ5afyDcDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس:  اگر به توانایی ایران در مختل کردن زندگی عادی آمریکایی‌ها نگاه کنید، به نظر من این توانایی بسیار محدود است.
🔴
این توانایی صفر نیست، اما بسیار محدود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/145461" target="_blank">📅 22:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/019a996d7f.mp4?token=QMV-g3GuCQCxQh3qhYUevH2IABD0UtbRsp8EW1al43qsjEN8akTI4_38RNJCNPeScUfY5m0OjisSEo_UXRR2yNKlf7U960p8pdixTVey73sCljnv2Wkyx0vuzO5CSiTXMuESVBA3RVTvtZswO9PoyXhSphKY8qAQlT8ourafbk5wSDg4iP8ZG6Mk5YP3fTjq-9llnzYViAx8VtPxidGjwW2zVzKHL4BtZ5dfqfLiaEfSguAqr96adVR2dPHb9xt27G6jP2XZ6BFBc3Y_9A43CPukEGrWbT8GlNNFaWtz09x3Fj4dWlXtEy2ov3TteBkWXEQnVrobKx-hDjQD5B3V8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/019a996d7f.mp4?token=QMV-g3GuCQCxQh3qhYUevH2IABD0UtbRsp8EW1al43qsjEN8akTI4_38RNJCNPeScUfY5m0OjisSEo_UXRR2yNKlf7U960p8pdixTVey73sCljnv2Wkyx0vuzO5CSiTXMuESVBA3RVTvtZswO9PoyXhSphKY8qAQlT8ourafbk5wSDg4iP8ZG6Mk5YP3fTjq-9llnzYViAx8VtPxidGjwW2zVzKHL4BtZ5dfqfLiaEfSguAqr96adVR2dPHb9xt27G6jP2XZ6BFBc3Y_9A43CPukEGrWbT8GlNNFaWtz09x3Fj4dWlXtEy2ov3TteBkWXEQnVrobKx-hDjQD5B3V8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس : همه می‌دانند که تاکر کارلسون و من دوست هستیم.
🔴
بسیار واضح است که تاکر برخی چیزهایی را گفته که من با آن‌ها موافق نیستم
🔴
او برخی چیزهایی درباره رئیس‌جمهور ترامپ گفت که به نظر من کاملاً نادرست هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/145460" target="_blank">📅 22:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ونس: ما تا زمانی که ایران از شلیک به کشتی‌ها دست نکشد، با آن مذاکره نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/145459" target="_blank">📅 22:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145458">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ونس: آمریکا از زمانی که من زنده‌ام، جنگ‌های زیادی را تجربه کرده است. ۴۲ سال.
🔴
و تا زمانی که دونالد ترامپ رئیس‌جمهور ایالات متحده نشد، تقریباً هیچ‌کدام از آن‌ها را برنده نشده بودیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/145458" target="_blank">📅 22:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145457">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ونس،: توصیه من به مقامات جمهوری اسلامی این است: از رفتار مانند افراد دیوانه دست بردارید و از شلیک به کشتی‌های تجاری بپرهیزید
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/145457" target="_blank">📅 22:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145456">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/817351e76e.mp4?token=s9dLoqB7QMpTJo89sGIX82TvE0tOPNk-NrpYZKQXmzbBcwvHBrJyl44pkHYhuxpPm2C8VjfiofuQq-NRbjUkEB9ymkA6kQ5DmUNkxOnRwkVcxMEbbE3yKQ9wwJmZnkXI9gUAXPl_WMCptztWLgQ8qfUAlfwUxu0r5MKRz6tfvXwwQI_DEUxIetIgWNdV5WwKKu-gppAlUwVT0kDjqvS8VMsC-DhbE-oqviNkDL6tFQJfpIGm-5AQJDd1633BodwN_Ziq-5e7xbIvjAA1w0Uj-EHpOcU1iNTqNLVYjqpNJ3ayttCX43Fa4y6iEoNigXC_NzBGdFq8pS6nbf1n0Xvomg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/817351e76e.mp4?token=s9dLoqB7QMpTJo89sGIX82TvE0tOPNk-NrpYZKQXmzbBcwvHBrJyl44pkHYhuxpPm2C8VjfiofuQq-NRbjUkEB9ymkA6kQ5DmUNkxOnRwkVcxMEbbE3yKQ9wwJmZnkXI9gUAXPl_WMCptztWLgQ8qfUAlfwUxu0r5MKRz6tfvXwwQI_DEUxIetIgWNdV5WwKKu-gppAlUwVT0kDjqvS8VMsC-DhbE-oqviNkDL6tFQJfpIGm-5AQJDd1633BodwN_Ziq-5e7xbIvjAA1w0Uj-EHpOcU1iNTqNLVYjqpNJ3ayttCX43Fa4y6iEoNigXC_NzBGdFq8pS6nbf1n0Xvomg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور جی‌دی ونس درباره ایران:
رئیس‌جمهور ترامپ گفته است که ما واقعاً دو گزینه در اینجا داریم:
🔴
می‌توانیم منطقه را ترک کنیم و کل جهان بسیار بدتر خواهد شد، زیرا دسترسی تضمین‌شده به نفت و گاز وجود نخواهد داشت. کشورهای عربی خلیج فارس به ما می‌گویند که این بدترین اتفاق در جهان خواهد بود.
🔴
یا می‌توانیم بپذیریم که ایرانی‌ها مانند افراد دیوانه به کشتی‌ها شلیک خواهند کرد و ما کاری که باید انجام دهیم را خواهیم کرد تا اطمینان حاصل کنیم که تلاش‌های آن‌ها منجر به بحران انرژی جهانی نمی‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/145456" target="_blank">📅 22:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145455">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
جی‌دی ونس: تا اینجا عملکرد بسیار موفقی داشته‌ایم.
صادقانه بگویم، اگر تلاش‌های ما نبود، قیمت بنزین می‌توانست بسیار بسیار بالاتر باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/145455" target="_blank">📅 21:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145454">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bb4cabcc2.mp4?token=rAaKtpvF_1Vxc_t2XfbUAR0YeD94SMxqajaIlBCCpnJl_leY8wHDq5amNfV8Q3AZg9rGKyY-A2DoD-56k6RFBZB02TBMGJJ6OlAmRMJKhahshyrHU-jBDNVg4VYhvDbfAbeFPde61e68YTCBE2FxaciAs2dtM9WXPiQaHkENTHz4ua4tmI5o_C913Tgh0IIfBbeHysRNMiD0rvw99rjT8Bmxv0PnAbEu0bsGfQhvAnBSxPBhq5quAsQawJ6CbXx_Wu4_AFUSWtX0O3W9U04vbCFu7uV7vu-sNWdmvkUcpYN-UAoKKqt-O-Q6yPBn1X_lEqtmGTpVwi8h7P3H0U6SWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bb4cabcc2.mp4?token=rAaKtpvF_1Vxc_t2XfbUAR0YeD94SMxqajaIlBCCpnJl_leY8wHDq5amNfV8Q3AZg9rGKyY-A2DoD-56k6RFBZB02TBMGJJ6OlAmRMJKhahshyrHU-jBDNVg4VYhvDbfAbeFPde61e68YTCBE2FxaciAs2dtM9WXPiQaHkENTHz4ua4tmI5o_C913Tgh0IIfBbeHysRNMiD0rvw99rjT8Bmxv0PnAbEu0bsGfQhvAnBSxPBhq5quAsQawJ6CbXx_Wu4_AFUSWtX0O3W9U04vbCFu7uV7vu-sNWdmvkUcpYN-UAoKKqt-O-Q6yPBn1X_lEqtmGTpVwi8h7P3H0U6SWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس
:
برای مدت بسیار طولانی، دولت بایدن ذخیره استراتژیک نفت را صرفاً با هدف کاهش هزینه‌های بنزین و نفت تخلیه کرد.
🔴
هیچ بحران بین‌المللی وجود نداشت. هیچ کشوری خارجی تلاش نمی‌کرد تا بازارهای جهانی انرژی را مختل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/145454" target="_blank">📅 21:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145453">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رسانه لبنانی و اسرائیلی ادعا کردند که تپه علی الطاهر لبنان و شهر موشکی اش سقوط کرده، هم اسراییل و هم حزب الله پذیرفتند
🔴
نیروهای حزب الله بدون جنگ عقب نشینی کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/145453" target="_blank">📅 21:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145452">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رسانه لبنانی و اسرائیلی ادعا کردند که تپه علی الطاهر لبنان و شهر موشکی اش سقوط کرده، هم اسراییل و هم حزب الله پذیرفتند
🔴
نیروهای حزب الله بدون جنگ عقب نشینی کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145452" target="_blank">📅 21:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145451">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
اسلام آباد: نیروهای امنیتی ما ۱۵ شبه نظامی را که قصد داشتند از افغانستان وارد خاک پاکستان شوند، کشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/145451" target="_blank">📅 21:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145450">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مقام ایرانی به رویترز: در نهایت افزایش نرخ تورم و سوخت در آمریکا، ترامپ را به ‌عقب‌نشینی وادار میکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/145450" target="_blank">📅 21:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145448">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rhd-uw1mdGo916hqwqydfBUVLAIfe2IGKDWuvuql3dhgtCU7nRk5Go8gaDWApf_5h57Nu1F6yOAhJTSYuaikE-6wIqaCYnw9GPzbqRRo-UuIbcxRxFFif-Bxy3-R1dHIE3QzrjqF9_x8zN608tzXiR1Er02NZBbI9W9mpQeu40ntcFoO598GTswu-7NdnZmmmdx60L2aoxH92C7hWY7zTuvthK9CKQAm9JXO1ijB_CRl-EDvqYO2XOa66-g7_12bqocBJqmrJ2tFe3XXvuMhk9ABo0ekIOHGiJ1S0yuUVUgrTi7F99rujGps9ROhAt68HDP_EfrKUwU0crwg55Cqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X7SqrvyQ3ON9X9fXpCqpqybGPyfVc71lLGnt3QsMX9BB_zybvKgnVWonpTEGI4sfTMb44VKnvUjuEr9PgfJgC-ZrnHaRtgwQcWb6bGCE7Vzt3kAS0_n1E6KBKKi0uPCEcUfOWrV9ypC5aVbq3oYEBFseQgaOpX_psL9UrN8QseokjRp5bm3Bmwm-ogwT_FV4fgGJhur6G6kULGZFKCHPxlpiEoWgAUqu5U2XYayEZFBkJoYUl8Yboy3pJG4G9t9QhaCqyXKYL3nyTtCSKKVey6_F84NcFLg1DLVmsDPLizfnqSi_qo62gT-Odfdp5aqdc4YgG3ypWrAyfM2tEZR2hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات سنگین شبانه اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/145448" target="_blank">📅 21:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145447">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزیر نفت: در جنگ ۱۲ روزه انبار نفت و پالایشگاه‌های فجر جم و پارس جنوبی هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/145447" target="_blank">📅 20:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145446">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
نیروهای اسرائیلی با چهار راکت، اطراف تپه «باط الورده» در نزدیکی شهرک «بیت جن» در ریف دمشق را هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/145446" target="_blank">📅 20:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145445">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhSGEPov9Ad6TJsGt9u1MX9URjTNHJxZbR7dPybjE1bsEu73JG3d0Ecm-G1h7xeCIhMkFozFriwwakirpT0iE_PiFl9sPy0iKqiKOU0UUqjSesqC60250wkbt0cTU3MJeMMPP4ZB8Adw1RZL08HtzjG_k_th8l7qh0RUqDGCuerLv8cEP-XG7NZ9lgk0cW9en2xtuPg3Pa9FBh3Z4msa8Yu4qo1qnchpmzDfykPElwqnIGQNH7hLHV_v3RXV3Rlb2s_kFfCqPTDXdfCrhjyVbI19qzeY1orsghzGdh_RnZ9cOgmf3jk5indX764PAQyED33HCck3WhW9Hq1i9Hzb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری های جدید علی کریمی که بازخورد های زیادی داشتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/145445" target="_blank">📅 20:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145444">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007137e607.mp4?token=HQEG1oodojoqQg2Jo1ZgW42e5D83xL_lTA3Y-r9vVBnt9sz9uXRgbrO8MP76IyoiJ7IL8575PCgdUJzq5cCkiK5YXAKi7W_XwPc5PEHjtQqqCoxxwIlkeK-7nsse3ms7HvnR3TvDHVzWLw_MG7jlUPNhzdBcD3_lGAV5RSe4D7J54sc1aUqdCxxqU7BPRcNqg_aMnAmSgTAe6trHhZ6RODVZwEyEgAD8yHKVAgdgAvSSuWaaObIv1OTybH6MwnJmJS4BpA-hjvJ5nT8kHojp1hSt7m553YxIjqPVx_tPFvWCsS6RnQf6G9WPAQE6kJmFLgf79fvx834IBhPu4tS2BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007137e607.mp4?token=HQEG1oodojoqQg2Jo1ZgW42e5D83xL_lTA3Y-r9vVBnt9sz9uXRgbrO8MP76IyoiJ7IL8575PCgdUJzq5cCkiK5YXAKi7W_XwPc5PEHjtQqqCoxxwIlkeK-7nsse3ms7HvnR3TvDHVzWLw_MG7jlUPNhzdBcD3_lGAV5RSe4D7J54sc1aUqdCxxqU7BPRcNqg_aMnAmSgTAe6trHhZ6RODVZwEyEgAD8yHKVAgdgAvSSuWaaObIv1OTybH6MwnJmJS4BpA-hjvJ5nT8kHojp1hSt7m553YxIjqPVx_tPFvWCsS6RnQf6G9WPAQE6kJmFLgf79fvx834IBhPu4tS2BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خطاب به بریتانیا: کشور شما خوب پیش نمی‌رود.
🔴
فراموش نکنید که درصد بالایی از نفت خود را از تنگه هرمز دریافت می‌کنید.
🔴
و شما برای کمک به من آنجا نبودید. کشور شما برای کمک به من آنجا نبود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/145444" target="_blank">📅 20:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145443">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB74ON7LzHx9-kgrQGTVdBlEaf3pAw-AfYNqRMi0rrBmEe3TCMcA2hOhvRmfZcoUyqYYaMVWKtRNqJ75L2z6DgUn6iG1RFSlPk5uDUc7H3E1W_irA4jcnQPDgQNS30OQmOpZ5cnckxtfcY4TKvxt8QIn3liQ1TzYidhaMrfmltNpUtITs4p8HbCiHbdjHqPJPTAmGFzJ3pW7luPi2VmxEz2nx8pQ6xQhQ9-dz5LneDbeRcKEmSbwYivllZgfbLs-8TpVJ_PNQQmiMnqoA-nHRVxbvDDrVf8KXi_AhD_rWCfBFF7Oh9aWcQDY3bfmpTI40i_2tiZQNM_xYR_SSQfsAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف خطاب به وزیر خزانه‌داری آمریکا: «قیمت نفت آتی عمان، بازده اوراق قرضه دولت امریکا و میزان ذخایر استراتژیک نفت را خوب تماشا کن.
🔴
قهرمان! هرچی زور داری بزن که در قیمت نفت آتی بیشتر مداخله کنی! چون کل حرفهٔ تو به این بستگی دارد. یا اینکه به تخلیه نفت از ذخایر استراتژیک بیشتر از حد خطرناک ادامه بده و سقوط غارهای نمکی ذخیرهٔ نفت در اثر کاهش شدید ذخایر را تماشا کن، یا به خداهای نمک تگزاس پناه ببر و دعا کن که چاه‌های ذخیره سقوط نکنند. دنیا پاپ کورن خریده و تو را تماشا می‌کند»
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/145443" target="_blank">📅 20:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145442">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کانال ۱۴ عبری مدعی شده سطح آمادگی و هوشیاری در داخل اسرائیل به‌طور محسوسی افزایش یافته است.
🔴
به گفته این رسانه، این وضعیت در پی نگرانی‌ها از احتمال ازسرگیری درگیری نظامی مستقیم با ایران ایجاد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/145442" target="_blank">📅 20:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145441">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سپاه اعلام کرد که هفت نفر را که ارتباط با گروه‌های کرد در استان ایلام در شمال غربی کشور داشتند، دستگیر کرده است؛ این افراد در حال برنامه‌ریزی برای عملیات‌های مسلحانه و حمل مهمات بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/145441" target="_blank">📅 20:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145440">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
نیویورک پست: عمان به طور پنهانی پیشنهاد ایران برای دریافت هزینه از تنگه هرمز را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/145440" target="_blank">📅 20:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145439">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
هم اکنون حمله اسرائیل به حومه دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145439" target="_blank">📅 20:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145438">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
به گزارش بی‌بی‌سی، دونالد ترامپ تلویحاً اعلام کرده است که آمریکا ممکن است در مناقشه بر سر جزایر فالکلند از بریتانیا حمایت نکند.
🔴
ترامپ این موضع را به عدم حمایت لندن از آمریکا در جنگ با ایران مرتبط دانسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145438" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145437">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل گزارش داد، «اسرائیل کاتس» وزیر جنگ این اسرائیل، با حضور «ایال زمیر» رئیس ستاد کل ارتش و شماری از مقام‌های ارشد نظامی، نشستی امنیتی برگزار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145437" target="_blank">📅 20:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145436">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
روزنامه فایننشال‌تایمز گزارش داد بازار بیمه لویدز لندن انتظار دارد خسارت‌های ناشی از جنگ آمریکا و ایران در کشورهای خلیج فارس به حدود ۱.۴ میلیارد پوند برسد.
🔴
مدیرعامل لویدز گفت برخلاف حملات به کشتی‌ها در تنگه هرمز، بخش عمده این خسارت‌ها ناشی از آسیب به زیرساخت‌های زمینی است. از جمله، شرکت سعودی سابک در پی آسیب یک مجتمع پتروشیمی در حمله موشکی، در آستانه ثبت مطالبه‌ای حدود ۸۰۰ میلیون دلاری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/145436" target="_blank">📅 20:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145435">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نتانیاهو بار دیگر تاکید کرد : "ما اطمینان داریم که قادر به سرنگونی نظام ایرانی هستیم. این وظیفه اصلی است و به زودی به انجام خواهد رسید."
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145435" target="_blank">📅 19:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145434">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d448ff03.mp4?token=nX02T68yqBjtu3zCqxGeuCzPqiEZkwpKpuJgZ1U7zLh2F2ebSRx7EFux_EUPGt7DKit88BJfhds2MffrdTV5agPF2DV4KCOTdPzPwYGv6HKlr41Yq79QmCGdSkRCHTYFQ9U5-ycyH7bqbnAk6xEfbhjSY9AF6USbptC7siaxrPAWEH6LNudSaW7t-WXHNcwr4JcOpgop1Vxd2wklZZFeGK6c8kQIN4n9EZL0iZCt7L3JupWh9r5TOuPB6NL0ciFQrW76rL4iZ8tRC6zUdW3H-V5SMj9s9ufjyVr8eeL-MLxwELOB_ua_D6grmdSoVpBGyEyFBfrSvFEiz_Uwp0IOtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d448ff03.mp4?token=nX02T68yqBjtu3zCqxGeuCzPqiEZkwpKpuJgZ1U7zLh2F2ebSRx7EFux_EUPGt7DKit88BJfhds2MffrdTV5agPF2DV4KCOTdPzPwYGv6HKlr41Yq79QmCGdSkRCHTYFQ9U5-ycyH7bqbnAk6xEfbhjSY9AF6USbptC7siaxrPAWEH6LNudSaW7t-WXHNcwr4JcOpgop1Vxd2wklZZFeGK6c8kQIN4n9EZL0iZCt7L3JupWh9r5TOuPB6NL0ciFQrW76rL4iZ8tRC6zUdW3H-V5SMj9s9ufjyVr8eeL-MLxwELOB_ua_D6grmdSoVpBGyEyFBfrSvFEiz_Uwp0IOtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر کانادا، مارک کارنی
:
ما از آنچه پیشنهاد شد یا از دوام آنچه ارائه گردید راضی نبودیم.
🔴
ما نمی‌خواهیم در کوتاه‌مدت به دستاوردهایی برسیم که چند ماه یا یک سال بعد از ما گرفته شوند.
🔴
این امر برای کارگران ما، شرکت‌های ما و جوامع ما منصفانه نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145434" target="_blank">📅 19:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145433">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
برنامه های هوش مصنوعی ChatGPT و Claude و Grok‌ و Gemini به دلایل نامعلومی از کار افتاده است.
🔴
تمام هوش مصنوعی های آمریکایی از کار افتاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145433" target="_blank">📅 19:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145432">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
مدیرکل فرودگاه بین‌المللی قشم از برقراری دوباره پروازهای مسیر دبی ـ قشم ـ دبی پس از ۶ ماه توقف خبر داد و گفت: نخستین پرواز این مسیر با یک فروند هواپیمای ایرباس A320 روز سه‌شنبه ۱۷ شهریورماه انجام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145432" target="_blank">📅 19:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145431">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
به گزارش سی‌بی‌اس نیوز، چند مقام ارشد آمریکایی گفته‌اند پیت هگست، وزیر دفاع آمریکا، در گفت‌وگو با افراد نزدیک به خود از شان پارنل به‌عنوان گزینه اصلی‌اش برای تصدی سمت وزیر ارتش یاد کرده است.
🔴
بر اساس این گزارش، پارنل در حال حاضر انتخاب مورد ترجیح هگست برای این سمت به شمار می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145431" target="_blank">📅 19:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145430">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / پرتاب موشک کروز ضدکشتی توسط نیروی دریایی سپاه از منطقه سیریک، ایران، به سمت تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145430" target="_blank">📅 19:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145429">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2894def8.mp4?token=qM0m7x9I4p2JwYHsAIdnCnXBlLIPuqPggDNFfDQNp4nP9l-FZP4f63_hb35bcN0xqXCKNJmEMFmVihPEVA24z_RyIkyCKNVE9LtwmZ3Drzz2szFLvA4Dt1sdcX9RJbBv-C5WRVoyVvkJwBT8kulCKFZHFYawIRM_zQba9pdxHPEeBxHmLq8p4JmXEh7TOK09SmyW2gMY73CJQIosSk-0zFuBF20TRm1OWl-p15pijZhitxnirUrmdBFvlLejMRuX03uculqbNddRl_A1sDkzV8-0O7ywd3xdemP08su6GRSGu50-VigyIZ-tmsxlGg8CixuDL7-Yp9GjTmOP_V7eug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2894def8.mp4?token=qM0m7x9I4p2JwYHsAIdnCnXBlLIPuqPggDNFfDQNp4nP9l-FZP4f63_hb35bcN0xqXCKNJmEMFmVihPEVA24z_RyIkyCKNVE9LtwmZ3Drzz2szFLvA4Dt1sdcX9RJbBv-C5WRVoyVvkJwBT8kulCKFZHFYawIRM_zQba9pdxHPEeBxHmLq8p4JmXEh7TOK09SmyW2gMY73CJQIosSk-0zFuBF20TRm1OWl-p15pijZhitxnirUrmdBFvlLejMRuX03uculqbNddRl_A1sDkzV8-0O7ywd3xdemP08su6GRSGu50-VigyIZ-tmsxlGg8CixuDL7-Yp9GjTmOP_V7eug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجارهای مهیب در پی آتش‌سوزی گسترده در افغانستان
🔴
وقوع یک حریق بزرگ در یک فروشگاه عرضه گاز و سوخت در شهر جاغوری افغانستان، منجر به سلسله انفجارهای پیاپی و هولناک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145429" target="_blank">📅 19:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145428">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
طالبان: تظاهرات نکنید، این در اسلام معنا ندارد و اتلاف وقت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145428" target="_blank">📅 19:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145427">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3352446383.mp4?token=Ou-lcDzP_dL3jtcxUQ5CAl85mU9yGcEIxl6DppgWxfN4MuSSx7tLFh6x86cAQCaBj3IafgPtmhYUBDSdVKaPaTNAbx71H_5Ft2PodtrIehPOfYmfNMkOE7f46A1LVvRi_cs7QzLzr0mmcFYNq36alWVAIk2YDvr9NIq_HlKSPd6oxAphP5KB1FfkM8w2CCd_3UNUZDWusp33c-zD_tDwyepUkGboti9wZVxlHgSl_57vrxqaOfIXn_cyl9Rg4y3jjRvVstG1OeqA4jrXPddJQ177wRe-xJtvw5VZ1IcLoqnbMOwwX3u-luUH540NoB5wD11JHd7sDLQ2GU1Lyk0i0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3352446383.mp4?token=Ou-lcDzP_dL3jtcxUQ5CAl85mU9yGcEIxl6DppgWxfN4MuSSx7tLFh6x86cAQCaBj3IafgPtmhYUBDSdVKaPaTNAbx71H_5Ft2PodtrIehPOfYmfNMkOE7f46A1LVvRi_cs7QzLzr0mmcFYNq36alWVAIk2YDvr9NIq_HlKSPd6oxAphP5KB1FfkM8w2CCd_3UNUZDWusp33c-zD_tDwyepUkGboti9wZVxlHgSl_57vrxqaOfIXn_cyl9Rg4y3jjRvVstG1OeqA4jrXPddJQ177wRe-xJtvw5VZ1IcLoqnbMOwwX3u-luUH540NoB5wD11JHd7sDLQ2GU1Lyk0i0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: چه رویایی را هنوز در سر دارید؟
🔴
وزیر امنیت ملی، بن گویر: امیدوارم بتوانیم مردم را تشویق کنیم تا غزه را ترک کنند، چه با اتوبوس، هواپیما یا کاروان. فکر می‌کنم این کار مشکل را حل خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145427" target="_blank">📅 19:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145426">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdcaf90290.mp4?token=HjOHFp9hb6xF67q7tloDeI1PwV55RBhEM3fRnU7Kswf7Ut5wxcUFjJqC--jU-daIxjQ5Ep3CdiNV0lmQ3CRNm0-z8Z_afpepQHWcdjZ9oH8QCKhrGd6lhDuvs5ElYIewv6qmV4pXlp6gpNvzQAstS2qQRMJQVQXm_EIGdDvDl5OlR9LagIv30gx6nr8IoqXrDpETLddVMwCve_bBVPz5nMnWQYVKkaCO1e-oxdufPkHOvOSEjPxDoDEPmpHWTUDj3eZe1AZVd3Sg1tIvCxr_XHgg9uA5lqQUBSG1HY-mxi6ZHXNF55Yuu9c5BSbOeYJeYecVYRWwRgbER5VSa4xRMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdcaf90290.mp4?token=HjOHFp9hb6xF67q7tloDeI1PwV55RBhEM3fRnU7Kswf7Ut5wxcUFjJqC--jU-daIxjQ5Ep3CdiNV0lmQ3CRNm0-z8Z_afpepQHWcdjZ9oH8QCKhrGd6lhDuvs5ElYIewv6qmV4pXlp6gpNvzQAstS2qQRMJQVQXm_EIGdDvDl5OlR9LagIv30gx6nr8IoqXrDpETLddVMwCve_bBVPz5nMnWQYVKkaCO1e-oxdufPkHOvOSEjPxDoDEPmpHWTUDj3eZe1AZVd3Sg1tIvCxr_XHgg9uA5lqQUBSG1HY-mxi6ZHXNF55Yuu9c5BSbOeYJeYecVYRWwRgbER5VSa4xRMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن‌گویر، وزیر امنیت ملی اسرائیل:
آنها واقعاً ده بار تلاش کردند تا من را ترور کنند.
🔴
من بیشترین محافظت را در بین تمام وزیران اسرائیل دارم و وزیر مورد تهدیدترین در اسرائیل هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145426" target="_blank">📅 19:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145425">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cacff7873.mp4?token=MNrFVler75m_TZu2WyZqky5obJE6TVCS386MLO7Wx7MhFeJFnf6H5SXYFVpzxjgy4C8WC0X6oxqWu1B5dIoDWQ5PShQ7CsZcY8QQX0cSdbV1nlG4tc3n6lW8Xsen9f90u5OF1hF-Zjg4WrECn1Jd5mE1URqsCpgZ5Bn8_8SMYEx-ySDVZ-9ha8gjXBdBddbc1d14TVwTiP8pV_Cu41JA0KACT8Ehr2ZRV2HdOnNIQsmCCKJNGqEaVonLv57TGBd19lA43Q2JpH4_5rq2Ig5XLoIsacYpSqS1IpmVg_HwwEifglgeLTxCx6_QU7Qw3qJIMOT3Kvv15pM7iP9QbskFFWucmukWblFTyHcs6Y1Se4G-g9mJPqDfMwr0BHO1UpiDLea3vcKlLcTGxzoHrRmF-7z8vEuGK6nnsKpXhNpIP-IRTPfU7dSr-_06Di0y2DzrqSrC4vrc77e8lC8XQNdvgYsNQDUwahg8tlFfSu4SW_EuTEniKHz1KGtdCHMZ_z63ApNF7Hlr8xztCvxp1Mb4EnOJQ6TxC3vTZZBe1M2n6TuIuwnRgLmUKpoMyTzQ04DBtD-jkRnKLaCm3Sd3B1mUoHKYhQng3qwPu9Ma8q873G5bMnH9YikG4pOc0swcub_s76G3bJsc5ofbz3LaVvMXkuNzMUHw5P8091_lDoUwv0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cacff7873.mp4?token=MNrFVler75m_TZu2WyZqky5obJE6TVCS386MLO7Wx7MhFeJFnf6H5SXYFVpzxjgy4C8WC0X6oxqWu1B5dIoDWQ5PShQ7CsZcY8QQX0cSdbV1nlG4tc3n6lW8Xsen9f90u5OF1hF-Zjg4WrECn1Jd5mE1URqsCpgZ5Bn8_8SMYEx-ySDVZ-9ha8gjXBdBddbc1d14TVwTiP8pV_Cu41JA0KACT8Ehr2ZRV2HdOnNIQsmCCKJNGqEaVonLv57TGBd19lA43Q2JpH4_5rq2Ig5XLoIsacYpSqS1IpmVg_HwwEifglgeLTxCx6_QU7Qw3qJIMOT3Kvv15pM7iP9QbskFFWucmukWblFTyHcs6Y1Se4G-g9mJPqDfMwr0BHO1UpiDLea3vcKlLcTGxzoHrRmF-7z8vEuGK6nnsKpXhNpIP-IRTPfU7dSr-_06Di0y2DzrqSrC4vrc77e8lC8XQNdvgYsNQDUwahg8tlFfSu4SW_EuTEniKHz1KGtdCHMZ_z63ApNF7Hlr8xztCvxp1Mb4EnOJQ6TxC3vTZZBe1M2n6TuIuwnRgLmUKpoMyTzQ04DBtD-jkRnKLaCm3Sd3B1mUoHKYhQng3qwPu9Ma8q873G5bMnH9YikG4pOc0swcub_s76G3bJsc5ofbz3LaVvMXkuNzMUHw5P8091_lDoUwv0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن‌گویر، وزیر امنیت ملی اسرائیل:
زندانیان تروریست از تمساح‌ها می‌ترسند. آن‌ها می‌ترسند.
🔴
من می‌خواهم آن‌ها بترسند. من این‌گونه می‌خواهم. این همان حکومت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145425" target="_blank">📅 19:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145424">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
به گزارش اکونومیست، دونالد ترامپ توافق نفتی با ونزوئلا را «بزرگ‌ترین معامله نفتی در تاریخ جهان» توصیف کرده و مدعی شده این توافق به آمریکا «سلطه انرژی» خواهد داد.
🔴
اکونومیست این توافق را جسورانه توصیف کرده، اما هم‌زمان نسبت به ابعاد و پیامدهای آن انتقادهایی مطرح کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145424" target="_blank">📅 19:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145423">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
معاون امور زنان رئیس‌جمهور: مصوبه صدور گواهینامه موتور برای بانوان نهایی شد؛ پلیس راهور مکلف به اجراست
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145423" target="_blank">📅 18:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145422">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDdWTYJIq3tr_sBHJUafkXsRgl7_5HiiJeacU-k5_GI7RnoF6jhYx6Xb9-lTJFDd8qyvX_HQnA1t7Ji_zinHnce8CvEvV4DHzS0lNG4LZidKEq2FTmEbCP5XTBKV0CsgnNBr3Z7jCrF2KooACvbaZrQXboBXYJg3j81h-b-2azndhyo1nJM8ShYnV0vVcJlE4uIxkXIQMCeTkX_3hQb4hucBQbX1q3aFyVvocUnj5mJRpzeWRtxK1tjuRpDTgPGFgY0Wn_cP7eV-TbnVCM9KE_rN00fjLiV9cSjQlCQ-z8GOtd-DLrMPyjDQhtXGGewZ_qDG38lAqGCaVE08-3i3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: «برای سیاستمداران کانادایی، مثل نخست‌وزیر کارنی، خیلی راحت است که دونالد ترامپ را «دشمن» معرفی کنند؛ اما وقتی اقتصادشان فروبپاشد، این کار از نظر سیاسی به‌شدت به ضررشان تمام خواهد شد؛ بدتر از هر اتفاقی که تاکنون برای یک سیاستمدار کانادایی رخ داده است
🔴
فقط تماشا کنید!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145422" target="_blank">📅 18:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145421">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCCIMiCPcMfVqT1GNN_6eMn8ECsru1Ci84seXyeqUnKq9E6D5jIwXY1t9OinD6eRWTyEVt5UpadEoivIl2HwA5HNj4Qnjvi0SRPMpTQ13IltjT4zfbc58Alyd2jdg07gkS0DDDKeTQbXS-WY2Ek3Sz0GW5xo61cB_QkMn7Xp460LBDkHdM5rZYnuOPKCmUq-dOGxanO4joJzBoXH8frA7XmmDjUPqXI3azjmXahy61t7Qdi4Iof2p-bVtqKean_JBLbsh6vZ30raiEiLr1YdMGN5grZYvXJ8prfynSDFEHoFsWWkot3MkAT4q1ifXtJWsABEp1BR9IcCcLAYnxnEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
افراد و رسانه‌هایی که مدام بر این موضوع تاکید می‌کنند که ما هیچ مهماتی نداریم (و آن‌ها ۱۰۰٪ اشتباه می‌کنند!)، در واقع خائن هستند.
🔴
آن‌ها این کار را انجام می‌دهند زیرا ترجیح می‌دهند ایالات متحده یک جنگ را ببازد، در حالی که ما به راحتی می‌توانیم آن را ببریم، تا اینکه من پیروز شوم
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145421" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145420">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: ما مقادیر تقریباً نامحدودی مهمات درجه متوسط تا بالا داریم؛ علاوه بر این، ما مهمات را در سطحی بی‌سابقه تولید می‌کنیم
🔴
فروش سلاح به متحدان به زودی دوباره آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145420" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145419">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXYEQ1NG6tmzjXgPgH2Usjkl_wMPiIHtUGr-oLsyXlYBbHWXoRkpW9tGfjmCLrdO15UYDbSW0rGbFhxeGypKktJKmGofmc1_j9HA1A-11j4ZCG6bT1mJNlrqs_XUfAYeGCMEVpN34KsuHOSPj6iofE_KbRLbBHVxWJNBmELEHwYAYqCx4IGhRm-RQfBsM330Q3TfanQS_4A0g0gRfTrSfJCJm697aLEqpCJ19eHgzEqwirsJlcYe5B1N8B738xCWxcd8j9wfw5MLio1puHP3bFD0Q0HtNNgyuP_pUmfhWq1W2qJX_Zdg1NWfWiYz2ocZK30RrsjZcgjg41BMmMkCWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ما مقادیر تقریباً نامحدودی مهمات درجه متوسط تا بالا داریم؛ علاوه بر این، ما مهمات را در سطحی بی‌سابقه تولید می‌کنیم
🔴
فروش سلاح به متحدان به زودی دوباره آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145419" target="_blank">📅 18:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145418">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rw-upLGKv8Gr7NYj2hSJGFSYWgfxLmMLziGd8FyySeCwmrIFg6hU9hjQqfTDn_Y4a3sK9cnNkEw8RdtTl9UMO9KacbacJ_YwxUho8T27vTJJNCYxVtW9wv9UazADdI-cbIM69OfNLaY73S_dbhcln8Axpjt-CVPGa34s2WqWP70I1ZbBK20hkwuoM-5U3IrsQM1x6z8N625m2pneh77Wbb0QRuBYpBnrnbn_E5VxWTHw48cLjABKIkBoSjQp_quAO21J_V4M9-cXs6St-DBPJmQPk7ISzbfDiFpRS9-QxbS4FPnGKZdldQIqoLS7y_uRkgv4R9ygGiCTW9j3kEL1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در هفته‌های اخیر، ارتش روسیه به‌طور بیشتری به داخل روستای کوزاچا لوپان پیش رفته و همچنین به گسترش منطقه بافر خود در استان خارکوف در امتداد مرز بین‌المللی ادامه داده است
🔴
رسانه‌ها تصاویری از نیروهای روسی منتشر کرده‌اند که در بخش‌های جنوبی، شرقی و غربی کوزاچا لوپان پرچم‌های خود را تکان می‌دهند؛ همچنین ویدیوهایی از نفوذ پرسنل روسی به روستای کودیووکا نیز منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145418" target="_blank">📅 18:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145417">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رسانه اسرائیلی: موشک‌های ایران به هتل نیروهای آمریکا در اردن اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145417" target="_blank">📅 18:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145416">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0432593c6.mp4?token=UOdqCNQGRlRdJ1FM0l3hfQa-ncHSu7KbmwPFyJuBMqb1pWGYywEJSZCxZh9sS4yHIGRiRpqBzOIkA-kNgcf1jXQeu4hTcXZuJRzOYK0GoWSiq8maaiHTkbGyfnpaB0EaSePQFUU9SMlP9l5iTWg2cdOBu80zBJdAE6L5cU8m6pUx0LrCExr-emFjgN1uPIF9epMNDaqJ2bDOhyV1LV_xp7oWGg9m844uCC9oG_m0eGth0lICm2HPhVoNcv4RAjUgEKXEWbuCOsGVSgQfdQweD0OzQ8HicMc_ZMk0ZsA4f8SAegSMo70OcPHQa5XIUy_y_6jWM8TvNF48g1sxh498eg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0432593c6.mp4?token=UOdqCNQGRlRdJ1FM0l3hfQa-ncHSu7KbmwPFyJuBMqb1pWGYywEJSZCxZh9sS4yHIGRiRpqBzOIkA-kNgcf1jXQeu4hTcXZuJRzOYK0GoWSiq8maaiHTkbGyfnpaB0EaSePQFUU9SMlP9l5iTWg2cdOBu80zBJdAE6L5cU8m6pUx0LrCExr-emFjgN1uPIF9epMNDaqJ2bDOhyV1LV_xp7oWGg9m844uCC9oG_m0eGth0lICm2HPhVoNcv4RAjUgEKXEWbuCOsGVSgQfdQweD0OzQ8HicMc_ZMk0ZsA4f8SAegSMo70OcPHQa5XIUy_y_6jWM8TvNF48g1sxh498eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری مهم از آخرین ویدئوی منتشر شده توسط انصارالله که نشان‌دهنده اصابت یک بمب خمپاره‌ای پرتاب شده از راکت "روجوم" به یک وانت در حال حرکت است که متعلق به نیروهای حامی دولت قانونی یمن (PLC) می‌باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/145416" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145415">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c92a85e0ae.mp4?token=fYEtdC5Y2vr-2_QNJjgZMr1afNq8sFG5lSGy-WXcvCvmY5Ve4PxXaNeyCpHTUzPy8xF4dvn5p8KdC9tIgwlfBFCb2xBibvFRw34mf2yPlwv4ar6jCV_DErpjUcLu3CW27NFeLquWbgKwogj0CmAwHae8U5rAqgwP60jmw3j9DcD7BO_9E6d2NeuRo96V9VYFatkPFKXyY7zMuz_HLszv-jpSEl0ffV4QVhejvYOXy-Uk8IWDSJf6JvGAXuv29RXMHm8ObB_gbpvG3gXNLqNGW8nN8FgfrhpuQshxOFWjoLuEJlkncNDu43PTeNSLEKUAKpazVacrbhJh3OqYTEpaKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c92a85e0ae.mp4?token=fYEtdC5Y2vr-2_QNJjgZMr1afNq8sFG5lSGy-WXcvCvmY5Ve4PxXaNeyCpHTUzPy8xF4dvn5p8KdC9tIgwlfBFCb2xBibvFRw34mf2yPlwv4ar6jCV_DErpjUcLu3CW27NFeLquWbgKwogj0CmAwHae8U5rAqgwP60jmw3j9DcD7BO_9E6d2NeuRo96V9VYFatkPFKXyY7zMuz_HLszv-jpSEl0ffV4QVhejvYOXy-Uk8IWDSJf6JvGAXuv29RXMHm8ObB_gbpvG3gXNLqNGW8nN8FgfrhpuQshxOFWjoLuEJlkncNDu43PTeNSLEKUAKpazVacrbhJh3OqYTEpaKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
گوشی اقتصادی a17 سامسونگ از ۱۵ میلیون پارسال، شد ۹۷ میلیون
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145415" target="_blank">📅 18:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145414">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان مدیریت بحران کشور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRX58hKgqIMTqJgsMeLfZ1Ve-UB-O7AQCf0BLJa7g66qRnoSAvc1hWAYWVbEN4vZ8-FmfyEgZiuk0tkorJ0YHY31pidJa6ghfmrQqjWROSc6g0t5i7s51GlabouK0cFfTwIuKLgg9xBCjtDcRTyh1CgTkbKiDimHvBsZ_762Ffw1ZauehR5Mb4mxiI0-YnH9jNXoEK3Xrx6MFkT_n4nt60HFXlE9UjjUmG4TgJ2GRaD5Y39E5doq4bJvTfzmijXCpjmzWpU9AGdJgAn-fMkdBF5zTqj1GwaQTFQl78Ec69nNhkoWNdHD3RsHap8OAAd4meiDgjFX5UFbSQRcRvABbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه بانک مرکزی</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/145414" target="_blank">📅 18:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145413">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
جنبش انصارالله تصاویری را منتشر کرده است که نشان می‌دهد نارنجک‌های خمپاره‌ای از پهپادهای "روجوم" به سمت نیروها، وانت‌ها و خودروهای زرهی طرفدار شورای انتقالی جنوب یمن (PLC) در نقاط مختلف خط مقدم درگیری بین انصارالله و PLC پرتاب شده‌اند.
🔴
خودروهای زرهی مورد اصابت شامل یک تانک اصلی مدل T-62، یک نفربر زرهی مدل BTR-40 و یک خودروی گشت زرهی مدل BDRM-2 هستند که همگی از نوع خودروهای زرهی طراحی‌شده توسط اتحاد جماهیر شوروی سابق هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/145413" target="_blank">📅 18:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145410">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daad725d95.mp4?token=BD__ohuxccMZv-4WiyFCGlE68KSmkKOavrWdWMM0RMKxC88G29xQqDGu-lisJkPd260ChHwsdr_jciUJlU8N0LEPpMBL222ymzd1CX13EEeLCOKE7fbIVeBn011KANhcfr3XNGeppZeBjoyFOZ9hRlQ2losuH4y08i6LB7BRaouSomsGm6CHOQgWkuNWSjfOr4lBOH7b31fUtx_soZqDBov0wT63NASWfQKT33axeRNXJtKJJOlpq6y_VJsyjLnhPN2vbTucTO3J5Q5YTUt2817iBwxsjOWtIctkaYoip7JVKY-mjVyZyqkGvBq3Cbs5lQKsJhk7YKISQlPPIqKOUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daad725d95.mp4?token=BD__ohuxccMZv-4WiyFCGlE68KSmkKOavrWdWMM0RMKxC88G29xQqDGu-lisJkPd260ChHwsdr_jciUJlU8N0LEPpMBL222ymzd1CX13EEeLCOKE7fbIVeBn011KANhcfr3XNGeppZeBjoyFOZ9hRlQ2losuH4y08i6LB7BRaouSomsGm6CHOQgWkuNWSjfOr4lBOH7b31fUtx_soZqDBov0wT63NASWfQKT33axeRNXJtKJJOlpq6y_VJsyjLnhPN2vbTucTO3J5Q5YTUt2817iBwxsjOWtIctkaYoip7JVKY-mjVyZyqkGvBq3Cbs5lQKsJhk7YKISQlPPIqKOUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی دریایی اوکراین امروز، یک عملیات تهاجمی با استفاده از پهپادهای دریایی علیه کشتی باری روسی به نام "نفریت" در شهر بندری سوچی انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145410" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145409">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
یه قاتل فراری تو بیمارستان شناسایی میشه و اینجوری با چاقو چندتا مامور رو میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145409" target="_blank">📅 17:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145408">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
روبیو: یه زمانی واقعاً این تصور وجود داشت که کل دنیا تبدیل به دموکراسی‌های مبتنی بر اقتصاد آزاد می‌شه و همه کشورها شبیه ما خواهند شد.
🔴
اما واقعیت چیز دیگه‌ای رو نشون داد.
🔴
کشورها و دولت‌های ملی هنوز اهمیت دارن. ملی‌گرایی هنوز واقعیه.
🔴
مرزهای کشورها هم همچنان اهمیت دارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/145408" target="_blank">📅 17:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145407">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46cceb2210.mp4?token=M1FTu4TxLXUpu6t3WgaqHl5S6K_uJzm3o5Y4ebWzK_kCSHjPesizUvBrpiGIAtDP2m26gcYLY1SiDmG8ZmJTXhfKcQzxFhrSwH90s-vKr1sqTzs89vuwuzaqD2nT2hzq6PkP687a24YZZHSyb79RBYMubRu9X0P08-Nnz8TVt8Wp2u4uf6SkB8MEYehA5S3nC7L7rSOV4Qm7xpedYoSgXW7v6PfYrr1yL9f3GRRKIBQ4SoGi_D8Xd2nHym3gXYmMsTUFacaAYGYLXtF8DU25AbV7gQ4D5ARxzldTHcrbK-f7kDrrCUUXTbz1Sa2WbhXYkZlu4YpKYSqSJb_VKvPO8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46cceb2210.mp4?token=M1FTu4TxLXUpu6t3WgaqHl5S6K_uJzm3o5Y4ebWzK_kCSHjPesizUvBrpiGIAtDP2m26gcYLY1SiDmG8ZmJTXhfKcQzxFhrSwH90s-vKr1sqTzs89vuwuzaqD2nT2hzq6PkP687a24YZZHSyb79RBYMubRu9X0P08-Nnz8TVt8Wp2u4uf6SkB8MEYehA5S3nC7L7rSOV4Qm7xpedYoSgXW7v6PfYrr1yL9f3GRRKIBQ4SoGi_D8Xd2nHym3gXYmMsTUFacaAYGYLXtF8DU25AbV7gQ4D5ARxzldTHcrbK-f7kDrrCUUXTbz1Sa2WbhXYkZlu4YpKYSqSJb_VKvPO8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: نمی‌شه یک اقتصاد رو کاملاً بر پایه خدمات اداره کرد.
🔴
باید یک پایه و اساس از تولید و ساخت کالا هم داشته باشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145407" target="_blank">📅 17:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145406">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
چین: به شدت از تحریم‌های مرتبط با ایران که علیه ما اعمال شده، ابراز تاسف می‌کنیم و قاطعانه با آن‌ها مخالف هستیم
🔴
از آمریکا می‌خواهیم فوراً رویه‌های نادرست خود را اصلاح و تحریم‌ها علیه شرکت‌ها و افراد چینی مربوطه را لغو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145406" target="_blank">📅 17:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145405">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه الجزیره گفت که پایگاه‌های نظامی آمریکا در این منطقه، از جمله پایگاه‌های مستقر در کویت، در جریان حملات تلافی‌جویانه شب گذشته ایران، "تحت هیچ‌گونه حمله‌ای قرار نگرفتند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145405" target="_blank">📅 17:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145404">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6R--X302rZCFfFPOweycmDu3kVY2S-iR-0_QqGvVlrL3FpnABAZo68kMbc-8S3e5Sujt_RbJklh_bQdgAbdS-kRcvENWUdqiFsTYXuXA_Bf1VOmxaelMOIWiWR5aZfl58YStPX-_0RClOUI4rU6nRCJwuRLNHM8j7ORQer9Phd-2ZyKNFk0txSZ5W8Pu9NQflbJlNHQfEu86-gVRJSgbTdqvuWVuayXbv7if0rlydB3lRffpel7apxwdPhdau0Y5lbUtHuqug-eFVuz4EfCv0Y3GgCtkB_tomRJaPlbWnJrRNsiLWoqSstbq1pk24zRCnrw90xWlzVgxQK8iELdHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان حمایت مالی جدیدی از بانک مرکزی یمن متعهد شده که هدفش تثبیت اقتصاد یمن، افزایش شفافیت دولت و حمایت از توسعه اقتصادی و اجتماعی این کشوره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/145404" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145403">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بقائی خطاب به بسنت: تاریخ فراتر از خاطرات حیاط پشتی خانه شماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145403" target="_blank">📅 17:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145402">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رویترز درباره ۳ گزینه ایران در صورت ازسرگیری جنگ
🔴
از حمله به تأسیسات نفت و گاز، نیروگاه‌ها و آب‌شیرین‌کن‌ها تا تهاجم مستقیم یا غیر مستقیم در کشور‌های غربی
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/145402" target="_blank">📅 17:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145401">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری/سخنگوی قرارگاه خاتم‌ الانبیا:
عملیات های تهاجمی علیه آمریکا ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145401" target="_blank">📅 17:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145399">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ojw9HwKM5966HvtKvGptfyTHX8tYb2qnqVJtgzIyk4GfFnymImirFe6cKvvCTWSZFqIgS_PFRSGD05_5WyLXH8krE-6gDCVeSvsgRz5Cz_tI5oN8qaNA03uunTHhjEX63VAujeU3vtYNoee0s93f7ZfnhxSIP0jzyFiwbHYTycHDkvJwOhFCANj5q3ZQE2iWi290eewJONU7Fjyr9vgmaivc_TUlWfIvYPFK-i3y0zN-tzQ-e6KKh8iKvlF-DahSihoUZTnJn1WDkqulzD5nBgo0FCAPxynVvPqflLwEG5MJmhXbrsGoul9GOtJfYCNwzF4BC5GT5cvZMTo7oDy70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAhcW_vsCZDZLwP9Vl_ux1p-c5-oXJMitLPFiC84MUEcp-P1Tjqctc0THcSbxQvNlf1FOlwDFZdN4yokccxfZf3vGi6h0k_-Q-MQVOMOknm-4EdEhYvGvTc9V1HYDZf2l9kvzLfhj6vHALFjaRb_47-9wjgKpqD1O_oWvQxVmI-_TsvrA1lyitDSi-_QxwibuyhIEWI8d5gTEeaNsVocOHggS7GxISJxVu6fNw61yn6dxhc3HZNkhoagjlEtMJzE99kOZPg23SPLUEpR6cowKlDCcKpXiGQWfVKCjXvpRRVsCU6-FQ0PdXmVq3xSYWtesGQdu-OuvrG9o0jRK_H0tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک پهپاد انتحاری هدف قرار دادن یک مخزن نفت در پایتخت لیبی، طرابلس، در نزدیکی فرودگاه شهر را بر عهده داشت، اما نتوانست به هدف خود برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/145399" target="_blank">📅 17:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145398">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c3ba818c.mp4?token=Y0slGFtZTXPD_eNB4vrSCH36t4cb2DKCslYSN9TDSZpxxJWzh_a_NTvEJ1JLjWKUSzjQ9o9iZoz5Rin_N7dMPXZs5P6KjRXuIfJORnwAv1Fj7Z1bdw3MbTa_znZHjQiGB3LwicBb5hlnWlSAiNxW-ply-CtkTAz2CIjaulwVnfOLBTi2Srx-KzjX8rsWXtZUzmpcBHvhpTGtjIXxbS_-3I2OEl5MFbQB3hslQmdassbvk6-XjOg5VJ0S3oVy7wptOvpLpErFSZbG8NHdCU1CAApOazfRfMj0vRhpgt2Ylw10HjQCnN5Eg8ycf9i99qwe96QOyqdvZ3c1PO0K6O2wCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c3ba818c.mp4?token=Y0slGFtZTXPD_eNB4vrSCH36t4cb2DKCslYSN9TDSZpxxJWzh_a_NTvEJ1JLjWKUSzjQ9o9iZoz5Rin_N7dMPXZs5P6KjRXuIfJORnwAv1Fj7Z1bdw3MbTa_znZHjQiGB3LwicBb5hlnWlSAiNxW-ply-CtkTAz2CIjaulwVnfOLBTi2Srx-KzjX8rsWXtZUzmpcBHvhpTGtjIXxbS_-3I2OEl5MFbQB3hslQmdassbvk6-XjOg5VJ0S3oVy7wptOvpLpErFSZbG8NHdCU1CAApOazfRfMj0vRhpgt2Ylw10HjQCnN5Eg8ycf9i99qwe96QOyqdvZ3c1PO0K6O2wCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بابک زنجانی: ما تا یک سال دیگه بیشتر زجر نداریم؛ یا در این یک سال از نظر معیشتی نابود می‌شویم، یا قدرتمند می‌ایستیم و از این یک سال عبور می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145398" target="_blank">📅 17:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145397">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سخنگوی کرملین در واکنش به درخواست وزیر خزانه‌داری آمریکا برای دوری از ایران تأکید کرد؛ مسکو روابط دوستانه و شراکتی خود را حفظ می‌کند و توسعه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/145397" target="_blank">📅 16:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145396">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7246d9a0a0.mp4?token=CFCDVKmWG10NMeCXsEvMO_CMHEhBTWOraFmYo_btCh0XnqKZwgLC-13SryulX_kpjdLC13ItuevkihgiS0ZDVIYqg94YFCYqpcNXSpKG0_OBSD7IY7RxbO73aVPXHa6CZntbeE2CI2JA3vQdFKqkTj7qfmL66m04vkXK50IHG5M4bmCDa7ZOWndaqcHky67nOyunjJgDiuNVEcPyf0ISyVxjpb9i-5DPESVhkvBuu9xzOPOjGdN_YChfkkqo02pbbBr_czkljfdDeWyK1_kK9ESgGhUoZJPIK2SbftiXHq1Vdi6mSH0IIQ-iWiW4Xnfzz45jkV6-1yVbM4ZXSf2jzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7246d9a0a0.mp4?token=CFCDVKmWG10NMeCXsEvMO_CMHEhBTWOraFmYo_btCh0XnqKZwgLC-13SryulX_kpjdLC13ItuevkihgiS0ZDVIYqg94YFCYqpcNXSpKG0_OBSD7IY7RxbO73aVPXHa6CZntbeE2CI2JA3vQdFKqkTj7qfmL66m04vkXK50IHG5M4bmCDa7ZOWndaqcHky67nOyunjJgDiuNVEcPyf0ISyVxjpb9i-5DPESVhkvBuu9xzOPOjGdN_YChfkkqo02pbbBr_czkljfdDeWyK1_kK9ESgGhUoZJPIK2SbftiXHq1Vdi6mSH0IIQ-iWiW4Xnfzz45jkV6-1yVbM4ZXSf2jzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خدمه‌ ناو هواپیمابر آبراهام لینکلن که چندین ماه در خلیج فارس و چندین ماه در ونزوئلا حضور داشتن ، به تایلند رسیدن و رفتن تا پس از یکسال در دریا بودن چند روزی رو در خشکی عشقو حال کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145396" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145395">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
معاون ارتش: توانمندی حملۀ پیش‌دستانه را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/145395" target="_blank">📅 16:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145394">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
یک مقام آمریکایی: پایگاه‌های ما در هیچ کجا، از جمله کویت، در حملات دیشب ایران مورد اصابت قرار نگرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145394" target="_blank">📅 16:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145393">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
بلومبرگ: اگر قیمت‌های بالای نفت تا تابستان ۲۰۲۷ ادامه پیدا کند، بهای بلیت‌های پروازی در اروپا به طور محسوسی افزایش خواهد یافت و برخی شرکت‌های هواپیمایی ورشکست می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145393" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145392">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نتانیاهو اعلام کرد که ۵ غیرنظامی لبنانی در ازای آزادی اجساد یهودیان در لبنان، آزاد خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145392" target="_blank">📅 16:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145391">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
احمد وحیدی فرمانده سپاه: انتقام جان باختگان نبرد هرمز را می‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145391" target="_blank">📅 16:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145390">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
پوتین: نخستین محموله نفتی از مسیر قطبی ارسال می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145390" target="_blank">📅 16:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145381">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va5H3dHRrmu6JwBcW6ozM5XGSm-h6I5WkihzFFqOf3pn4ZusCE_XjHXVlQIUspQGw7ZXT03SHiSn8ev6pBrmgm9xHr2E1Am7uBXUCISOuUhtwlDjHo3XqgefHe53Y9mcO2xznSekVsn1xMgKexNxPjMkU9Ije1Mt_BF9mm_G3oHlh4_EjXZCOxXkWJnsxSlBOYIcZpFsSdpAqnLaAXfDq82fPvafebJQHXVsbFi2t2YD5sHG9KQ4YUCD_asKBK0LxuQvgsKkBI6eBGD3PcBqnh3Mb2S_scvRE6VDgYkp2uDQA9OAtPw-Ws_tyZaRlpm9QVRW5BsVLFVtEUcOuQDvaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4abdcbc674.mp4?token=EilrMgDQ4Da5CUgOG8hmA80msN_bc-mFOS9A-Ihht3dxwTKwhdsltP05LEaYY_8_fmbzChwYb3FbuuqQKrE5JOKt_MF1F83C282hLtA29jOR13acdahyXA0WoZcsDx-xHJq0PMwfojK1x_Yk6HKkq_T-4SgMrbMUCHXo7GoG4AA19VE1N1DcObsu4_QPOgjDh81Hl7O3LTkpZlTSbh-PU9mUqSYpKJNN_RbRiGlNbf_l2BqpqpX0LTEP1sX-3ipgzZem76vnK8Id5p08VYtJxX-jwfr9L1aXEFhRI-F4aD3l2LIjXZvmKm7QEH1AGeXH2ZMnvFdFmOWavCvhHOdVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4abdcbc674.mp4?token=EilrMgDQ4Da5CUgOG8hmA80msN_bc-mFOS9A-Ihht3dxwTKwhdsltP05LEaYY_8_fmbzChwYb3FbuuqQKrE5JOKt_MF1F83C282hLtA29jOR13acdahyXA0WoZcsDx-xHJq0PMwfojK1x_Yk6HKkq_T-4SgMrbMUCHXo7GoG4AA19VE1N1DcObsu4_QPOgjDh81Hl7O3LTkpZlTSbh-PU9mUqSYpKJNN_RbRiGlNbf_l2BqpqpX0LTEP1sX-3ipgzZem76vnK8Id5p08VYtJxX-jwfr9L1aXEFhRI-F4aD3l2LIjXZvmKm7QEH1AGeXH2ZMnvFdFmOWavCvhHOdVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای داراویش که به رئیس منطقه برکنار شده، لافتگاری، وفادار هستند، امروز صبح یک عملیات تهاجمی علیه نیروهای فدرال حامی سومالی و شهر بیدوا در منطقه جنوب غربی سومالی آغاز کردند.
🔴
نیروهای حامی لافتگاری در ابتدا به عمق شهر نفوذ کردند و یک پایگاه نظامی فدرال را به تصرف خود درآوردند، اما پس از یک نبرد ۴ ساعته، عقب‌نشینی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145381" target="_blank">📅 16:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145380">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InhfP2uxZBnBOB9-pI62d5BWqvqlojt_vF_NwBPB-_i7zuIqQnMLipuW20BG3UZJtGXbYfZVZseSEdi4im7pxuZSnJ1HPfvlv3zcCVibVhWXjCeOfxPbFd72BbaOeePOOknyamuGGZq5dEg9hOaCO99e0LwPDgujHyQuH0obxpXHwJdLh8PJL2hM3w9kw8iejAlnk31WmDvfYmXZG0Fe71w6iC12I0milH3YIkiv81bjQkiVfMyPOgdTvNc2sVQHTYiUpqNabEuliL3p5o_D4_MlZ4bcLmSPEA5Gk4CP72dkFwJrwo47zbdMVSbKSCPJDEKdLPdWHYpDFaVlkXu11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش بی‌بی‌سی، دونالد ترامپ، رئیس‌جمهور آمریکا، برای مدت دو روز از تاریخ ۱۲ سپتامبر به ایرلند سفر خواهد کرد.
🔴
قرار است او با کاترین کانولی، رئیس‌جمهور، دیدار کند و قبل از سفر به اقامتگاه گلف خود در شهر دونبیگ، واقع در شهرستان کلر، مذاکرات دوجانبه‌ای با مایکل مارتین، نخست‌وزیر، داشته باشد.
🔴
کانولی پیش از این از ترامپ و سیاست‌های ایالات متحده در مورد غزه انتقاد کرده بود و او را "زورگو" خوانده و او را "ناپایدار" و "غیرقابل پیش‌بینی" توصیف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145380" target="_blank">📅 16:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145379">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
سپاه اعلام کرد: در حمله دو شب پیش آمریکا به کرمانشاه، یک فرمانده ارشد موشکی، سردار جعفر کهریزی ترور شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145379" target="_blank">📅 16:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145378">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ff31f76e.mp4?token=YHuPWO6ieHqU3QeOFRGDD6w5cXO4TAV3sED70Gsz9ybUa9vqvxwm_qz_k8G6jx4sywnhFvyIGSa38KZPnqayC-Z7YPofg8pn0L8muD_9Aw5nWUWcTYLcuIOOkXGuUYniKh0pub8TQehU_RTdOz9bhulToXA-SeVa5tZR2qhRnK4mFP7OqJvFc8N7AfUJzDW68AFGk2ygWFPjaR0PNXi4J4lM0P2kPw-aJ39ZjIynSd80UWtXg-2khyfM9HWX5h06CwrStl5LnaUUBvNI5XJUcPANG5QrszRnK0-TWu9ePifYsxZjII3EhwfrQx68ZPNaZGP6vg-cstol-3wimyHIxqj6zAcEe33LzLUVTb0v-JSH2t6UP7BjbIAai7K90UDrDboJReOHgCGTVNVAfVxVCdY6vgV88B5eL8yrXl2Xz_Rfni6_D10CXCxsa2Ea9fKXy81-NcgXl-h2GXFGOqOFxBTUIUciOxbVDpq8xmHCoqFFXSrI-_XvY1OEFDJOYpJoqcqrDd1dDuMmJQSXkB69nnldT0c2lzaxO8My3_jvO2VvQ7jo-NQOkS2_9ISABRKyxe_WXf4JLDOxGf07_Go3rH0LQRfD96-WjPAT6lyi1kUEsO7isV5S32wLcBNFPcEHMo5rHFeA89CptoL0eS6A7tpJIrJNVZSqlq4SVJ-l99g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ff31f76e.mp4?token=YHuPWO6ieHqU3QeOFRGDD6w5cXO4TAV3sED70Gsz9ybUa9vqvxwm_qz_k8G6jx4sywnhFvyIGSa38KZPnqayC-Z7YPofg8pn0L8muD_9Aw5nWUWcTYLcuIOOkXGuUYniKh0pub8TQehU_RTdOz9bhulToXA-SeVa5tZR2qhRnK4mFP7OqJvFc8N7AfUJzDW68AFGk2ygWFPjaR0PNXi4J4lM0P2kPw-aJ39ZjIynSd80UWtXg-2khyfM9HWX5h06CwrStl5LnaUUBvNI5XJUcPANG5QrszRnK0-TWu9ePifYsxZjII3EhwfrQx68ZPNaZGP6vg-cstol-3wimyHIxqj6zAcEe33LzLUVTb0v-JSH2t6UP7BjbIAai7K90UDrDboJReOHgCGTVNVAfVxVCdY6vgV88B5eL8yrXl2Xz_Rfni6_D10CXCxsa2Ea9fKXy81-NcgXl-h2GXFGOqOFxBTUIUciOxbVDpq8xmHCoqFFXSrI-_XvY1OEFDJOYpJoqcqrDd1dDuMmJQSXkB69nnldT0c2lzaxO8My3_jvO2VvQ7jo-NQOkS2_9ISABRKyxe_WXf4JLDOxGf07_Go3rH0LQRfD96-WjPAT6lyi1kUEsO7isV5S32wLcBNFPcEHMo5rHFeA89CptoL0eS6A7tpJIrJNVZSqlq4SVJ-l99g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لاوروف درباره اروپا: برای نیم هزاره، یعنی بیش از ۵۰۰ سال، اروپا منبع اصلی تمام مشکلات و بدبختی‌هایی بوده که گریبان بشریت رو گرفته.
🔴
اروپا منشأ دو جنگ جهانی بوده و همچنین منشأ وضعیت فعلیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145378" target="_blank">📅 15:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145377">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
لاوروف درباره ناتو: ناتو باید خودش رو منحل کنه
🔴
درست مثل پیمان ورشو که بعد از فروپاشی اتحاد جماهیر شوروی منحل شد.
🔴
اما این کار رو نکردن. اول، اتفاقات افغانستان رو بهانه‌ای برای حفظ این ائتلاف نظامی قرار دادن
🔴
بعد، وقتی اون ماجرا هم برای ناتو به شکل فاجعه‌باری تموم شد و از افغانستان خارج شدن، تهدید روسیه رو جایگزین تهدید شوروی کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/145377" target="_blank">📅 15:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145376">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5ca249cf.mp4?token=sBI7D0fgiLZJandr8w-HpUdr-pVmiw1J8VKtnYikrDn9-e_zWAcfaxJOwF4mjYWpWI1rZMjbsbPv2fizn28fRHUlhXomSeIL9OT3VOeUS2tPCw3RER3gsheUWnsfHuBocoaOpYycbx6wHeIDPJGB__RZmvkRgvFeCRSCMHXaxBGYjpCn8X5HLTk0YsAdkJU-iykq0DfCNhjZ-c-wH_a1tmKhlOpRKxNS62zC8QxnJy30CBLdZC2BSDVjIZP7_yZHlXQKKeIQlrFEAcnWnMMkGjPOIJxDbNkvHbfyrtZf7BV-Elfq1TS7SdQJ90KfQzWRDKDoJNbhUUMnVtFP9S3KoK6Y9ApD2fEve7eHyj7AM7liwWOeIuOXmpZ3CBFx5eh_dsevzXhYMVBsWhzMqXN0QGdC37rQue4kSx-PCd7O-pFZSXF2Pn2DcbtzQYaSSrowVICxTUs7_v8awOzMpGrwqP9i9kXGEImgXn-kYo_yvudH1JS2zufNzUTOpUKekUNEy-odG2fLldIa_5PJlW_Ar4WYunCFUHrdqmM4-FEk84ZJ3rQmQAnPPjITU-HewcTAbwSWywv-d0Ea_r9iUAJqA9vciVbI-dfopsKiQLNQJW1aThQxZPkmqgpCUPzZIOFoWU2O1J_UX-VfVhVK79AEw36lxq3GR2LxFlC-UATtZsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5ca249cf.mp4?token=sBI7D0fgiLZJandr8w-HpUdr-pVmiw1J8VKtnYikrDn9-e_zWAcfaxJOwF4mjYWpWI1rZMjbsbPv2fizn28fRHUlhXomSeIL9OT3VOeUS2tPCw3RER3gsheUWnsfHuBocoaOpYycbx6wHeIDPJGB__RZmvkRgvFeCRSCMHXaxBGYjpCn8X5HLTk0YsAdkJU-iykq0DfCNhjZ-c-wH_a1tmKhlOpRKxNS62zC8QxnJy30CBLdZC2BSDVjIZP7_yZHlXQKKeIQlrFEAcnWnMMkGjPOIJxDbNkvHbfyrtZf7BV-Elfq1TS7SdQJ90KfQzWRDKDoJNbhUUMnVtFP9S3KoK6Y9ApD2fEve7eHyj7AM7liwWOeIuOXmpZ3CBFx5eh_dsevzXhYMVBsWhzMqXN0QGdC37rQue4kSx-PCd7O-pFZSXF2Pn2DcbtzQYaSSrowVICxTUs7_v8awOzMpGrwqP9i9kXGEImgXn-kYo_yvudH1JS2zufNzUTOpUKekUNEy-odG2fLldIa_5PJlW_Ar4WYunCFUHrdqmM4-FEk84ZJ3rQmQAnPPjITU-HewcTAbwSWywv-d0Ea_r9iUAJqA9vciVbI-dfopsKiQLNQJW1aThQxZPkmqgpCUPzZIOFoWU2O1J_UX-VfVhVK79AEw36lxq3GR2LxFlC-UATtZsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله بالگرد روسی به پهپادهای اوکراینی
🔴
تصاویری منتشر شده که ظاهراً خدمه یک بالگرد Mi-28 نیروی هوافضای روسیه رو در حال درگیری با پهپادهای اوکراینی و منهدم کردن اون‌ها نشون می‌ده
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/145376" target="_blank">📅 15:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145375">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ: این فوق‌العاده است!
🔴
سوریه خود را به عنوان یک جایگزین برای تنگه هرمز معرفی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145375" target="_blank">📅 15:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145374">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J098i4VJGTXJHKmbAlHbiF0CuBC3YmZlkm4HzJDPD9qR2CZM7Qa3nUX-TRA2F4EyLiZM8hW9FaDh5KvYBSX1A3wvJEZtOxbVur0isgX82fMlpAPZB7SY6bKoWx93tCvdsOAEWwnYP4zrzWehGPdEK9fpKJkdwxg6mkQe0vvjSxfNGk9xliNQJjVJfsDHp_xxLYtzmVd5QGDZ3X0B2O-JTtkJN-Z8bZjLo_C7LBpyeylJ70G5r8yAh-BgJ-w1ZJ8Xt0EiYzsKsnZnkbdzwGNdloPFigkmABZh6f2nskwE8FNF28fuqeI8pwfYedfTT0gM2GbGn04w4lSucRuM4__0iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور ترامپ به طور مستقیم متعهد نشد که از بریتانیا در مورد جزایر فالکلند دفاع کند
🔴
وقتی شبکه خبری GB News پرسید که آیا ایالات متحده به کمک بریتانیا خواهد آمد، او به جنگ سال 1982 اشاره کرد، از بریتانیا به خاطر "بازپس گیری قاطعانه" این جزایر تمجید کرد، اما تأکید کرد که این جزایر "خیلی دور هستند" و اعزام نیرو به آنجا "سفر بزرگی" خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145374" target="_blank">📅 15:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145372">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d196d38e2f.mp4?token=g2g7b7xWrjyLoXY7oLGXZQ7XbfrI5cd-PgpitNsxkOWc1GCcD50I87UfMKQ2mJbAuUgsFqByUbsU2la6WrROCy3rTfidt9O3cvvWJDdydvC8yPYGj-rN_vwBR3lyQY-ynQ2cVlaFzSeWxR2-dw0mOcd4Op0AhOpE72w-u_mSyo8dMTjEP5IRjJl03QnXYIwcxomMC7NNC-H16iKUeOGY6I6RlYHR6od6MOT3qrZMUfcDPRI-iZrkOBKXI9vTXMmtCXWu93ufHXaNzaX8ZiMKakMkS8yODhIORW855P_mLps5YqaL0BbmDYpHIe4u2fCdEzjiWmg3j4jro8LprfqEFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d196d38e2f.mp4?token=g2g7b7xWrjyLoXY7oLGXZQ7XbfrI5cd-PgpitNsxkOWc1GCcD50I87UfMKQ2mJbAuUgsFqByUbsU2la6WrROCy3rTfidt9O3cvvWJDdydvC8yPYGj-rN_vwBR3lyQY-ynQ2cVlaFzSeWxR2-dw0mOcd4Op0AhOpE72w-u_mSyo8dMTjEP5IRjJl03QnXYIwcxomMC7NNC-H16iKUeOGY6I6RlYHR6od6MOT3qrZMUfcDPRI-iZrkOBKXI9vTXMmtCXWu93ufHXaNzaX8ZiMKakMkS8yODhIORW855P_mLps5YqaL0BbmDYpHIe4u2fCdEzjiWmg3j4jro8LprfqEFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به گزارش‌ها، یک فروند هواپیمای جنگنده مدل SU-25 متعلق به نیروی هوایی سودان در منطقه بارا، واقع در استان شمال خردفان، سقوط کرده است
🔴
هنوز مشخص نیست که آیا این حادثه به دلیل آتش دشمن یا نقص فنی رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145372" target="_blank">📅 15:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145369">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419c823c3e.mp4?token=bL_v63mpYZLRXuR31xsxWTK7LidbY6AFT7J54PiVYvTUFLkye6cqewy96th64gDAvxBnS2NqiuEs8D2glGn9DvU8KmltRnhWv3ygMvcr-HiBaTc2XBj81UqEx_bnKPosUlf5fCC_Vod52LYwlJBDd_VI-d7OYH7fzGE9qjIYRlhZy59rLk3fEqQ_nHLiQvq-KCDdAw3hjPvnWZJFtfUdhopWdNjY4R9s_0WpGcyIRF30QtayAaf_P0kjb91R8tb8dX8tocacliOTJTVvi1AZZCr02jwb02x3idU7r5OkE9_-PxL21sMOGsDyvy-uhkcdsmHxv6q4TQMDSohYnGK2Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419c823c3e.mp4?token=bL_v63mpYZLRXuR31xsxWTK7LidbY6AFT7J54PiVYvTUFLkye6cqewy96th64gDAvxBnS2NqiuEs8D2glGn9DvU8KmltRnhWv3ygMvcr-HiBaTc2XBj81UqEx_bnKPosUlf5fCC_Vod52LYwlJBDd_VI-d7OYH7fzGE9qjIYRlhZy59rLk3fEqQ_nHLiQvq-KCDdAw3hjPvnWZJFtfUdhopWdNjY4R9s_0WpGcyIRF30QtayAaf_P0kjb91R8tb8dX8tocacliOTJTVvi1AZZCr02jwb02x3idU7r5OkE9_-PxL21sMOGsDyvy-uhkcdsmHxv6q4TQMDSohYnGK2Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای دولتی سوریه در حال تصرف انباری از تجهیزات نظامی سنگین و خودروهای زرهی متعلق به سازمان سابق نیروهای دموکراتیک سوریه (SDF) در شهر حسکه، شمال سوریه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/145369" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145368">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee52f2348.mp4?token=mqZVSz5kEAo0HU9ekDVgcKKMymBgAXOJ5TXNcDU4dJ1LnKmTAL6Nt8EPWyRiNq1SIg2sFVZyRnmgkO6DbUXyOd08znBXwTno4ZnFeBF4oUuX2XJ_1uxJg_aksNas-ox5MAKnmLFglbJYeXLfAPhItzqqYJLXDw4SRQu_BbpTAUXjuymGFaX9y2gmJYxYDAxv7WnZJ3Q2ITisG4Gu9pDLmhts4SmbUg0AFnPA__ENJ8uWf1udKv2SgWplpOpS769EPwmovuJZr1Lj4qZfb7-T5txGVzoEqDMQ-BFSSjFItRPP_614XWViYsqiDkcirlFu-cUIt03Mh2ZbFF4XkgUzqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee52f2348.mp4?token=mqZVSz5kEAo0HU9ekDVgcKKMymBgAXOJ5TXNcDU4dJ1LnKmTAL6Nt8EPWyRiNq1SIg2sFVZyRnmgkO6DbUXyOd08znBXwTno4ZnFeBF4oUuX2XJ_1uxJg_aksNas-ox5MAKnmLFglbJYeXLfAPhItzqqYJLXDw4SRQu_BbpTAUXjuymGFaX9y2gmJYxYDAxv7WnZJ3Q2ITisG4Gu9pDLmhts4SmbUg0AFnPA__ENJ8uWf1udKv2SgWplpOpS769EPwmovuJZr1Lj4qZfb7-T5txGVzoEqDMQ-BFSSjFItRPP_614XWViYsqiDkcirlFu-cUIt03Mh2ZbFF4XkgUzqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به شهرک‌های «بنی‌حیان» و «القنطره» در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145368" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145367">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: عملکرد چین و روسیه در سطح سازمان‌های بین‌المللی در قبال ایران، تحسین‌برانگیز است، زیرا از سواستفاده آمریکا و متحدان این کشور جلوگیری می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/145367" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
