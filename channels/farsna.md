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
<img src="https://cdn4.telesco.pe/file/Yzk6RPVhL5yOaSdJb8QLvb7GKq07cqtYCycJOHmquRGtWh2gGkvC2MLiZk4F7Sc8uN9s1hRy6zqA0QcEBc6oR4ubxL2fejGNV3h2kEjBjWcSz4qIFmRxh4fAAz0z4GumC9geHnk7qhz5xo3bMUV-hppL5DLRoZL52FU-6ZxM3OhCkaczOPCAP6Jic71czu0Sd2bT5eH7uKcB_br7ACvyi6lyRIto0v_WLpDANSuvy6F9cghSE8lEdxSieMfFpnKfhtRrUT7IsMurEy22BaQq39rfEmLr0lraaF0c9zgHNWMkEZ3vf4ibzgEKeM084X5ZSiDeuBkT3c0U8UEL6qv_ww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 00:44:35</div>
<hr>

<div class="tg-post" id="msg-453941">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2ZCHyGl3qiHdkiQ3vpSOQVQxlcaoscEVeN0fm4yQ669Sexpoj3h9CrmYJqlknsGzXru4y77AkTegn9iCPW0JnUhvCEI6gwwQACmsLMfnvhuz-dGn85jcxSHxWMRjMY8pw2NLYJbD9DIqtP9CINEBsR85TSJeIB_nwsenmxjA5Z_nt_o42SxWejUsx1H2FdoKa9GxZsvz1mcvKfwdB0_F6GFhIC77_soH1hDxBTbk9zgjznghNeDd3i77YWwHK71G4vuRYSMPaYtyZGWE2zTQjkqS1op0jd6EpHEzPD06FK_wAm5H-vx6iXn2a7UYQmr7NJA8zXt8THz1w0eY3ShSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرساخت‌های آبی آمریکا هک شد
🔹
ایالت میشیگان روز شنبه اعلام کرد که ۹ سیستم آبی این ایالت هدف حملات سایبری قرار گرفته‌اند.
🔹
این حملات کمتر از یک هفته پس از آن رخ داد که مقامات مینه‌سوتا از هدف قرار گرفتن بیش از ۳۰ سیستم آبی در این ایالت خبر دادند.
🔹
در مینه‌سوتا، شهر براهام برای چند ساعت از ساکنان خواسته شد مصرف آب را به حداقل برسانند؛ چرا که مهاجمان با هدف قرار دادن کنترل‌های عملیاتی، سیستم چاه و تصفیه‌خانه را از کار انداخته بودند.
🔹
بر اساس گزارش نیویورک تایمز، این حملات حداقل هفت ایالت را تحت تأثیر قرار داده و ممکن است دامنۀ آن بسیار گسترده‌تر باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/farsna/453941" target="_blank">📅 00:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453940">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL1quL419-EPlyZ8XtwfcSqaETQ4X_VL4g63UQjT03Cg8Jn_MLM7RLPi6ugj3HD6PtQK5ywBC0nmz3fyzbcSNj9HQAvv2DOyXsGVigfogI_njuYEuNajab3WQ6y5whK8BgSIGCD9KzECrR-fTHxiGOnMABjkPuHVRKwZV4wbwZnyYiHFw-IAXkWayf5LNh8blFDJAf-OdJwoecf_JOd6y-Spp3fC2foxvPj_14xDIQoKunZcRYtO8Wq9cMiKwCFEIiJreVFAeIoTyi4qYQzrTVGQWEPaNBQZX6xmyu-Nv3K3wxMd5gB7htyEOLIm1c-jAiZRsoMG3kJizeI9-_NhBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی در گفت‌وگو با همتای سعودی: مشارکت کشورهای منطقه با آمریکا و اسرائیل، با پاسخ قاطع ایران مواجه خواهد شد
🔹
هرگونه تجاوز، اقدام خصمانۀ آمریکا و اسرائیل یا مشارکت و همراهی کشورهای منطقه، با پاسخ قاطع و متناسب نیروهای مسلح مقتدر ایران مواجه خواهد شد و مسئولیت تمامی پیامدهای ناشی از چنین ماجراجویی‌هایی برعهدۀ مسببان آن خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/453940" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453939">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f692ea2a31.mp4?token=dmFKsFRmsOKQ27FDw0Zks8ythHEs_6eLE9KwYw4SXBjlnhLuUPxBTHY3ayfdMUUklvGq3yZ507JlKo218tZsGLNNXYw0bN4Oawsf0RxYbSbGShxl6MQE9ZLWwJR5cJwAN1pOivOr3Lgr2o3TXqbHgyaKpY8xBm31NCeZXNRxCmuzwj4-aWOuZWvqMMAbGCK9ZAWrt6_QB8KnnVlBqudI6BLlPgZJPGKiyR4DYueWHUyRNMLzMj1W0Ud1tKwg1UuThwZnuxE7wTqt6GrYws649QM84ckEo5oqKJHl82qdm-P2deHP8FC4Cz0PrQWH3YLcDoL4mhRIyns5ugv1MJEgcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f692ea2a31.mp4?token=dmFKsFRmsOKQ27FDw0Zks8ythHEs_6eLE9KwYw4SXBjlnhLuUPxBTHY3ayfdMUUklvGq3yZ507JlKo218tZsGLNNXYw0bN4Oawsf0RxYbSbGShxl6MQE9ZLWwJR5cJwAN1pOivOr3Lgr2o3TXqbHgyaKpY8xBm31NCeZXNRxCmuzwj4-aWOuZWvqMMAbGCK9ZAWrt6_QB8KnnVlBqudI6BLlPgZJPGKiyR4DYueWHUyRNMLzMj1W0Ud1tKwg1UuThwZnuxE7wTqt6GrYws649QM84ckEo5oqKJHl82qdm-P2deHP8FC4Cz0PrQWH3YLcDoL4mhRIyns5ugv1MJEgcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام بی‌آزار در محرم‌شهر: ترامپ عمدا به راه‌‌آهن مشهد حمله کرد تا مردم نتوانند برای تشییع رهبر شهید به مشهد سفر کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/453939" target="_blank">📅 00:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453938">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40631b97ca.mp4?token=USNN9zyfKnxEI7dGD9CfkPIAVUsjvWXm8KBPLtKFmiVaeAPf6u-qKOdzcKRoYqQFRfd81G5yx2pLnZW9OkKh4EZH67h_YZHQuqJqO8ACssqU_KIgh_f6Nu0ZmXSKPBs5mMsJSgyHLs1vbVfKu2sORsNPdQdBwSat6W_5cWrC-cyZLYF312uHw47nJ7jlCAshRDdqscFfmTWmaOV0fv59TW93sL0vi3Tj76v3INhQ-2Z2T1D_nXSObd5efi2PZPESnpo-O4TOt47ITJ2bwUfZ64NRQ7-CzcaQz6SDcHMHLAxSgyhh8_G6NdpW2fu6Izz5NI8SWJvR_QBDrwDQNP9G8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40631b97ca.mp4?token=USNN9zyfKnxEI7dGD9CfkPIAVUsjvWXm8KBPLtKFmiVaeAPf6u-qKOdzcKRoYqQFRfd81G5yx2pLnZW9OkKh4EZH67h_YZHQuqJqO8ACssqU_KIgh_f6Nu0ZmXSKPBs5mMsJSgyHLs1vbVfKu2sORsNPdQdBwSat6W_5cWrC-cyZLYF312uHw47nJ7jlCAshRDdqscFfmTWmaOV0fv59TW93sL0vi3Tj76v3INhQ-2Z2T1D_nXSObd5efi2PZPESnpo-O4TOt47ITJ2bwUfZ64NRQ7-CzcaQz6SDcHMHLAxSgyhh8_G6NdpW2fu6Izz5NI8SWJvR_QBDrwDQNP9G8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نامه‌‌ای که دختر شهید مدرسۀ میناب برای پدرش نوشته بود: تو همۀ چیزی هستی که من دارم
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/453938" target="_blank">📅 23:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453937">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1f0c3713.mp4?token=j9NXz9VGWtNBA5wWujJjttqqbXjhPTVaQhfGx0wV1Qu6BQKLRMC6n-uksXtg5Ttq1dy4sxBn6vde34GcMnvXoT-G07Etq-2RiMLbo_YGUVSTFUXDDraUNfCXyM9-_qi7yizdnyC1EbIr-JsIa2YUaMK3KHOgcKryOw1rokNyitqxtRiKGdcLtbT7oD-aZecY8sJfOX5TMXUySinVe_dssSlZ4W7yVwYkfxAc437lxb0OFonfoVuiAL980ToFWh6EoiK_1Aq1KKmzCTo4OyYCswrLgLBeGCQSj1zp16E2SZlOLEaBqYRPlV_hixVCZg6dvrTGfe1nVeb4UCOaDN8A0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1f0c3713.mp4?token=j9NXz9VGWtNBA5wWujJjttqqbXjhPTVaQhfGx0wV1Qu6BQKLRMC6n-uksXtg5Ttq1dy4sxBn6vde34GcMnvXoT-G07Etq-2RiMLbo_YGUVSTFUXDDraUNfCXyM9-_qi7yizdnyC1EbIr-JsIa2YUaMK3KHOgcKryOw1rokNyitqxtRiKGdcLtbT7oD-aZecY8sJfOX5TMXUySinVe_dssSlZ4W7yVwYkfxAc437lxb0OFonfoVuiAL980ToFWh6EoiK_1Aq1KKmzCTo4OyYCswrLgLBeGCQSj1zp16E2SZlOLEaBqYRPlV_hixVCZg6dvrTGfe1nVeb4UCOaDN8A0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم سرخ انتقام در تمام مشایه برافراشته شد
🔹
روی عمودهای اصلی مشایه با پرچم «یالثارات الحسین و ابناء الحسین علیه‌السلام» برافراشته شده است. پرچمی که به نیت خون‌خواهی رهبر شهید انقلاب بالا می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/453937" target="_blank">📅 23:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453936">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f15c065ae0.mp4?token=DHetGt7giBdxI_UyB05ZhYxFclTNsOJJ6ATk1dEoYFckfpybT0c5Mae4pjrULEAnr9_tEOH2S8VPFaPO6VXQg1iN6DRSMOkldY8fn2UiW53O2ZMeiHHtwGzqLMT5Ak5w7uHWp73dICWMQqJQ8YW28Q1KP-fxoEEfoXeDBqj7c9MH9aoeESxlHUiaKUspsEC3uVi6smQ3QmOVnUT7nH74eMsJwHXrigSrwQl5U7eP9DUl_jDG13OdVGb4FJ5ND_RZ1GyGNgL4tAhJfuSla9vEalMFVbe4KBElhTyEBM5RWisinSag_MywFRdWeY7oKCs0oA_YdIb_7ZOlW_7XQkhe5w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f15c065ae0.mp4?token=DHetGt7giBdxI_UyB05ZhYxFclTNsOJJ6ATk1dEoYFckfpybT0c5Mae4pjrULEAnr9_tEOH2S8VPFaPO6VXQg1iN6DRSMOkldY8fn2UiW53O2ZMeiHHtwGzqLMT5Ak5w7uHWp73dICWMQqJQ8YW28Q1KP-fxoEEfoXeDBqj7c9MH9aoeESxlHUiaKUspsEC3uVi6smQ3QmOVnUT7nH74eMsJwHXrigSrwQl5U7eP9DUl_jDG13OdVGb4FJ5ND_RZ1GyGNgL4tAhJfuSla9vEalMFVbe4KBElhTyEBM5RWisinSag_MywFRdWeY7oKCs0oA_YdIb_7ZOlW_7XQkhe5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط مرگبار هواپیمای گردشگرها در پرو
🔹
درپی سقوط هواپیمای گردشگران در جنوب پرو دست‌کم ۱۳ نفر جان خود را از دست دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/453936" target="_blank">📅 23:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453935">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3Q9ZLwUDpY0ARTVX_IKC9xS6s0Rzj0Ln7tAJRtx4z_pQkKgADFBOXvu2QwI_FduE68S8qccIgaz6jt6WPdGQ8c6BYn-1Q8pfMiiEqCBR9qai1zr55e7bQ3uPXaEbWXIcYMNtmfjYJMsUwb_kuTeQUntWYfxRcGkVqOoyxjm9G9XpH0LgR6OYUCtzXeNmWldIv8PQYRAG2g20mulf_yYUPQLJ1S9JpswnhhwdlzXvzabfICpeCx3wWSxQubLmNJ_phc1uF8FbSVXJw3mkqMJNGuD9HyBG9crkhYLqDGcG_AD2NgZnvpd3r6GbAEHr-89W2AVpT_E-3vmnMV7DZvSAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: برای پاسخ به هر ماجراجویی آمریکا آماده‌ایم
🔹
وزیر خارجه در تماس تلفنی با فرمانده ارتش پاکستان و وزیر خارجۀ ترکیه: نسبت به هرگونه اقدام ماجراجویانه از سوی ارتش آمریکا هشدار می‌دهیم.
🔹
جمهوری اسلامی ایران برای صیانت از حاکمیت ملی، تمامیت ارضی و امنیت کشور و پاسخ قاطع به هرگونه تعرض آمادگی کامل دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/453935" target="_blank">📅 23:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453934">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e584444a0.mp4?token=HJ6GwHfwlMQv2Mut7xERABCdB18mchy9TsSEjQCLr66cpDQ5PVEDpan7TAVDfxPnEmoRTG9v0wDuR26LyVVkublSJW6-kO-CpkSbntTFOQBMKWppx5q8q9QXiggfYwhLQhsYwAzZXZdKJ3TIR-ThDgHvVwKhJmlVvjUK52rduX0Mrk0hw4G9yR8L4K2QK_Pw3n5esfHD9WcnVYfC7l_4TlhSJeClZq1X5INE--QO7NufR3z31IhAylJfqEuNXR5WDMnM-UpkzqSSCZXRWuBJYByI06hE_cfA4agjy32o8OexrKAdpdrl0tm7nB7UlzsIB9j00-DN8IwmY1IgdQzvZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e584444a0.mp4?token=HJ6GwHfwlMQv2Mut7xERABCdB18mchy9TsSEjQCLr66cpDQ5PVEDpan7TAVDfxPnEmoRTG9v0wDuR26LyVVkublSJW6-kO-CpkSbntTFOQBMKWppx5q8q9QXiggfYwhLQhsYwAzZXZdKJ3TIR-ThDgHvVwKhJmlVvjUK52rduX0Mrk0hw4G9yR8L4K2QK_Pw3n5esfHD9WcnVYfC7l_4TlhSJeClZq1X5INE--QO7NufR3z31IhAylJfqEuNXR5WDMnM-UpkzqSSCZXRWuBJYByI06hE_cfA4agjy32o8OexrKAdpdrl0tm7nB7UlzsIB9j00-DN8IwmY1IgdQzvZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: خون‌خواهی باید یک مطالبۀ همه‌جانبه علیه جبهۀ کفر باید
.
@Farsba</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/453934" target="_blank">📅 23:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453933">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/267e6e4867.mp4?token=bIuctBgAf7H6nwth3UQrc6ZfNb9W8s6g1d34O9uMrwce4bOu5QTsaXeFHAzuBk9h90sLTrvlpF304Hx5CZoOjPfN1WQxu3q5MxlrVm7_im4fQmPoqp4RPgbOtiQJL2sgBKlEL8lNl0lFZKisV-ju8FoUBH7ew1foIyXr5lDDtV0lTUCoV0SdKti4EKA-6qzNpLD2q_u7OggFFNfIlUjv2M26lCe9uBWBIFBwPBiUjn6pYyNfB4vZM28b6x7YGIG2JvgRQnquTFZcAukLUDNH7mEfLaEs9HNHKhC42GBgCKXTPjMEWB-2a8kJVwjS_L0CpxKPXEbcPTf-W1ACPWwGtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/267e6e4867.mp4?token=bIuctBgAf7H6nwth3UQrc6ZfNb9W8s6g1d34O9uMrwce4bOu5QTsaXeFHAzuBk9h90sLTrvlpF304Hx5CZoOjPfN1WQxu3q5MxlrVm7_im4fQmPoqp4RPgbOtiQJL2sgBKlEL8lNl0lFZKisV-ju8FoUBH7ew1foIyXr5lDDtV0lTUCoV0SdKti4EKA-6qzNpLD2q_u7OggFFNfIlUjv2M26lCe9uBWBIFBwPBiUjn6pYyNfB4vZM28b6x7YGIG2JvgRQnquTFZcAukLUDNH7mEfLaEs9HNHKhC42GBgCKXTPjMEWB-2a8kJVwjS_L0CpxKPXEbcPTf-W1ACPWwGtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هلالی، مداح مراسم محرم‌شهر: دیگر وقت استراحت نیست؛ باید برای خونخواهی رهبر شهید برخیزیم
@Fsrsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/453933" target="_blank">📅 23:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453932">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">وقوع انفجار مهیب در جنوب لبنان
🔹
منابع خبری گزارش دادند این انفجار در «شهرک کونین» رخ داده است، و هنوز علت این انفجار مشخص نیست.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/453932" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453931">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113c60f2a0.mp4?token=IwXjMqVvNcs7-unEX5uzz0t8emWDgFwBN_Or8JiU4OU0l62uTjIujY835dG9CFSnu-DMsMYgkgchHAtKkSY6BkpEcQL3-fMAgi7jv7mMNFZwSsogPKeUCszUI8FYKdw5UGqoXAjADG-Z0NLux9FznuyShYfEy64sEZ8k6IPtp5BXmkwGS0LVFKp3q7UObIdGpWPmErOey4mGXGPBxCAoiiUlk1jY9SoPoAodxaP94GMgK--_97pVchFBUw1AcAQZGoPXGQtgBEDA4un8kHcFuaJqzpiXPSSzoIaysLD5U9B-E4hrg5TzoLG7Nou0jMJxxswQpBBRY54pEMkAA4IJyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113c60f2a0.mp4?token=IwXjMqVvNcs7-unEX5uzz0t8emWDgFwBN_Or8JiU4OU0l62uTjIujY835dG9CFSnu-DMsMYgkgchHAtKkSY6BkpEcQL3-fMAgi7jv7mMNFZwSsogPKeUCszUI8FYKdw5UGqoXAjADG-Z0NLux9FznuyShYfEy64sEZ8k6IPtp5BXmkwGS0LVFKp3q7UObIdGpWPmErOey4mGXGPBxCAoiiUlk1jY9SoPoAodxaP94GMgK--_97pVchFBUw1AcAQZGoPXGQtgBEDA4un8kHcFuaJqzpiXPSSzoIaysLD5U9B-E4hrg5TzoLG7Nou0jMJxxswQpBBRY54pEMkAA4IJyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزم ما استوار و این راه رفتنی است
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/453931" target="_blank">📅 23:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453930">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
منابع عربی: مقر احزاب ضدایرانی در سلیمانیۀ عراق هدف حملۀ پهپادی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453930" target="_blank">📅 23:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453929">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc184633a0.mp4?token=SB4sfH97rEbG40EFpfPuGYiqA46_MX0_meaOlAuWhfk_YtYWD-i4EVQTH3RjKZy2MYqfQoSj6m009BjpRr38TndklcdTxQ_MxbyCbsU9ukd_iQGOBbpGhjSuXn0Alvb_pS_WKNwhjW0c8d0xIAZaINTjexkIQAw7XtCwxnEdANchOKtQwAUtJbQGXlOS5lMo0JWp3K1P_LkyDA9Lva1GJunzkNi904iNie6qVq-VmCEH3Xud7e_V0-WBb0FzzjITqdRxB8C-jIqg7oycq3HAnqHUKHc3Ll_GRZgARQ4-a-FlvGjAyLTrAQpYfwPUUxLptSF6TT4iFW1pPMDJpWTom7WGxexifc3dSRPMT8u5V3mVJgpLFMvU52N6aawwcqA-ZruqSqZx4-rKkuuWFF94HxHvKkahTvUFw3UDTbNljufUO8H4BEhZlpJmbkDYHBA5NOqS_0M6g4adWYzQsEyPF4j1VZDVfwjpXaiwgvkOSZAo9wfqCJO7_PuKmtcS4TXVROZsobxC-klsEvGJQrFwwVC2T7RAZsbfT9S32EjQINmYKhfggXDKtWZ3K3MOctdc4282Hxg-8DLlNtrQCtJr7oqWvaBg8E8IHAEcHCMQ-ToaZvjUmPj3-vCqzYiIZn-kufjsQLKKRe0xaXiveILB4IpecOIS8xhq5HySKYJbkB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc184633a0.mp4?token=SB4sfH97rEbG40EFpfPuGYiqA46_MX0_meaOlAuWhfk_YtYWD-i4EVQTH3RjKZy2MYqfQoSj6m009BjpRr38TndklcdTxQ_MxbyCbsU9ukd_iQGOBbpGhjSuXn0Alvb_pS_WKNwhjW0c8d0xIAZaINTjexkIQAw7XtCwxnEdANchOKtQwAUtJbQGXlOS5lMo0JWp3K1P_LkyDA9Lva1GJunzkNi904iNie6qVq-VmCEH3Xud7e_V0-WBb0FzzjITqdRxB8C-jIqg7oycq3HAnqHUKHc3Ll_GRZgARQ4-a-FlvGjAyLTrAQpYfwPUUxLptSF6TT4iFW1pPMDJpWTom7WGxexifc3dSRPMT8u5V3mVJgpLFMvU52N6aawwcqA-ZruqSqZx4-rKkuuWFF94HxHvKkahTvUFw3UDTbNljufUO8H4BEhZlpJmbkDYHBA5NOqS_0M6g4adWYzQsEyPF4j1VZDVfwjpXaiwgvkOSZAo9wfqCJO7_PuKmtcS4TXVROZsobxC-klsEvGJQrFwwVC2T7RAZsbfT9S32EjQINmYKhfggXDKtWZ3K3MOctdc4282Hxg-8DLlNtrQCtJr7oqWvaBg8E8IHAEcHCMQ-ToaZvjUmPj3-vCqzYiIZn-kufjsQLKKRe0xaXiveILB4IpecOIS8xhq5HySKYJbkB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۵۴ مقاومت مردم تربت‌حیدریه خراسان‌رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/453929" target="_blank">📅 23:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453928">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21cff13888.mp4?token=cmbqyqa4WdhIARQCOt6UF5FTVrzRgX_53_IwTN18Cpz1VQ1aRqg6H7NGdHjV4yw3ZLxsE0nNJrkI6psgJpOCFGxRsKYHBMiZn9oGUwK0O8WKTZ0cUP77MsvlosZ5eCGUMOGLJUh8CXxddFYafBUG95FsQbFlKFxrxylCOZu-3TcReAnRhKNGI3KAhyrXnYENKPMcHRGc2TeXt_JGjJpz9IFM4-x1yVxmol5x4HvZiCee-bwh5ZiXwUEefydE78sX9VeYZ1EtWB7ybpSx3HLEO1lCYUcxL7_prdQ8X6wSwMRpIZ3w_SLIu7_Vd8mPqtGaYSBbERlQwIkmbXZTGbhhjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21cff13888.mp4?token=cmbqyqa4WdhIARQCOt6UF5FTVrzRgX_53_IwTN18Cpz1VQ1aRqg6H7NGdHjV4yw3ZLxsE0nNJrkI6psgJpOCFGxRsKYHBMiZn9oGUwK0O8WKTZ0cUP77MsvlosZ5eCGUMOGLJUh8CXxddFYafBUG95FsQbFlKFxrxylCOZu-3TcReAnRhKNGI3KAhyrXnYENKPMcHRGc2TeXt_JGjJpz9IFM4-x1yVxmol5x4HvZiCee-bwh5ZiXwUEefydE78sX9VeYZ1EtWB7ybpSx3HLEO1lCYUcxL7_prdQ8X6wSwMRpIZ3w_SLIu7_Vd8mPqtGaYSBbERlQwIkmbXZTGbhhjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمود آن رهبر مظلوم و شهید «مثلی لایبایع مثل یزید»
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453928" target="_blank">📅 22:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453927">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2cfbb5665.mp4?token=Sn60pSIortMEGb2vQEKKjC8LrqO3c_yOG5zItUWyBpp9QnrUiGQK9nlM9PKRQNo1SV5jJzXiETaYc62yKRC08TA-k9cNnGNqnNy_5uz1VI5BS4wyw9XVMq0MbaXZUfMg1CWGXwHzWTjJXtjn_MlU1s7X442WC9AzmsrjBsdJ-ihFH-jMBeeX1tXYPQ2ILKiuQSCYBfWOwv4854TyZjx5H9J-CfOt6ripTfGx105KwkfSsRaUeATFktWZqePHEou4IkR2u337kDd-XVA8vWv9I48lMgwEZVC3441DBQaICynWuz4LwF6BuG43C__mub0opeVUZGZhglGQ6_5ZVLBLTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2cfbb5665.mp4?token=Sn60pSIortMEGb2vQEKKjC8LrqO3c_yOG5zItUWyBpp9QnrUiGQK9nlM9PKRQNo1SV5jJzXiETaYc62yKRC08TA-k9cNnGNqnNy_5uz1VI5BS4wyw9XVMq0MbaXZUfMg1CWGXwHzWTjJXtjn_MlU1s7X442WC9AzmsrjBsdJ-ihFH-jMBeeX1tXYPQ2ILKiuQSCYBfWOwv4854TyZjx5H9J-CfOt6ripTfGx105KwkfSsRaUeATFktWZqePHEou4IkR2u337kDd-XVA8vWv9I48lMgwEZVC3441DBQaICynWuz4LwF6BuG43C__mub0opeVUZGZhglGQ6_5ZVLBLTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازدید سردار قاسم رضایی جانشین فرمانده فراجا از مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/453927" target="_blank">📅 22:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453926">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d147c1534.mp4?token=dILK6PDxJP_JiWUqWp4eP6Uqs6wjluKFIeLofeMdWGzA310ft3Cf5aMpfX0BegAN8uSWPEyqRP_q3SEQrGw_OXQUtThAv4JMkNFEcQnUEhskJsPlbtp29j_wwSKkZ5pRwUfHX_49NEkcw_bQo4lbG-db01WL1mvpKwQr1d6kj9pfif42X_sg8MXOoNDKty5GN5JxiS_OMkfXx1v3peg96vBdIdcuZD8CGtj8SYtiq97Xx6daJjcq4XEW8aY0jhl5XrlVXkqujEYH2x7U16tpoiapcHkzShFyj9rSqVzH9hrnF6pAV04CXJ9fx7ZriYVJnCNPS4H0ZgF2geEY9Bt7mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d147c1534.mp4?token=dILK6PDxJP_JiWUqWp4eP6Uqs6wjluKFIeLofeMdWGzA310ft3Cf5aMpfX0BegAN8uSWPEyqRP_q3SEQrGw_OXQUtThAv4JMkNFEcQnUEhskJsPlbtp29j_wwSKkZ5pRwUfHX_49NEkcw_bQo4lbG-db01WL1mvpKwQr1d6kj9pfif42X_sg8MXOoNDKty5GN5JxiS_OMkfXx1v3peg96vBdIdcuZD8CGtj8SYtiq97Xx6daJjcq4XEW8aY0jhl5XrlVXkqujEYH2x7U16tpoiapcHkzShFyj9rSqVzH9hrnF6pAV04CXJ9fx7ZriYVJnCNPS4H0ZgF2geEY9Bt7mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار «مرگ بر آمریکا» در مسیر کربلا هم از زبان مردم نمی‌افتد
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453926" target="_blank">📅 22:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453925">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌
🔴
وزارت خارجه: دولت‌های منطقه وظیفۀ قانونی، دینی و اخلاقی دارند که از استفاده آمریکا و رژیم صهیونیستی از قلمرو و امکانات خود برای حمله به ایران جلوگیری کنند. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453925" target="_blank">📅 22:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453924">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
وزارت خارجه: تداوم محاصرۀ دریایی و حملات به اهداف نظامی، غیرنظامی و زیرساخت‌های ایران، مصداق «عمل تجاوزکارانه» و نقض منشور سازمان ملل است و ایران از حق دفاع مشروع خود استفاده خواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453924" target="_blank">📅 22:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453923">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
وزارت خارجه: تداوم محاصرۀ دریایی و حملات به اهداف نظامی، غیرنظامی و زیرساخت‌های ایران، مصداق «عمل تجاوزکارانه» و نقض منشور سازمان ملل است و ایران از حق دفاع مشروع خود استفاده خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/453923" target="_blank">📅 22:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453922">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a618481cd.mp4?token=TQBj1-t5CWAfEYs_HJGTq7gv_OTpYMoGukVq83PLsF9gYWQ24tTpmMOTTMO2gqu3CJ6olo2NYQ1IluOhYq5CPYw18bud9BUQ8JkvqGgHKALgWALn1_BtG-IfdJF7D21mcYknrDVcZ8pGh6zlFv6PvG683eah9mSoEsdLrLfcezxdbMU7bwn_ec4-k1ldbf0FaYqnutCoHtraBy81KITtuRe9U32GnhL_58zAedOq8tjTVSB9qNqp60M15EfOyl1jBQ_TkOmRVsOT9DpQSJQyVkJZFQacIddhPpEVocx8wP-f95uDHuUj8OCNjAGbLpB3GvOCQYBAZRdgsSlcls0lCh7UTxZrlWkqbNOjNt051d-GXH06iBGDO-xSeQOow8xPJmK2nav_GevW5MWkICJ7XIxe-PGTq4CKxvvya2SkSDOsrCwZq66hpGGuiGpJgrZjckfZYQry3qjkWWnFRMQRp58mFQrpQVCo0uy9TeqoPAoKcjFvTiMsTZA2N24tGO2cCVYfFnU5eedMppH6ZqBQHX122zlY3HiH0jf4ZUg7X_Yvdx8ET11sBTfWzmIk-FUnu9l8YADdyYq15BKEixij7KUuuIRzFNd3AJTNiaMJaOEddNV3gmmFoWCnDlKA2Ry2tDxSMI9uTP3Edu8_xmHnTqhxNRpvCOTwMBeafUvBDKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a618481cd.mp4?token=TQBj1-t5CWAfEYs_HJGTq7gv_OTpYMoGukVq83PLsF9gYWQ24tTpmMOTTMO2gqu3CJ6olo2NYQ1IluOhYq5CPYw18bud9BUQ8JkvqGgHKALgWALn1_BtG-IfdJF7D21mcYknrDVcZ8pGh6zlFv6PvG683eah9mSoEsdLrLfcezxdbMU7bwn_ec4-k1ldbf0FaYqnutCoHtraBy81KITtuRe9U32GnhL_58zAedOq8tjTVSB9qNqp60M15EfOyl1jBQ_TkOmRVsOT9DpQSJQyVkJZFQacIddhPpEVocx8wP-f95uDHuUj8OCNjAGbLpB3GvOCQYBAZRdgsSlcls0lCh7UTxZrlWkqbNOjNt051d-GXH06iBGDO-xSeQOow8xPJmK2nav_GevW5MWkICJ7XIxe-PGTq4CKxvvya2SkSDOsrCwZq66hpGGuiGpJgrZjckfZYQry3qjkWWnFRMQRp58mFQrpQVCo0uy9TeqoPAoKcjFvTiMsTZA2N24tGO2cCVYfFnU5eedMppH6ZqBQHX122zlY3HiH0jf4ZUg7X_Yvdx8ET11sBTfWzmIk-FUnu9l8YADdyYq15BKEixij7KUuuIRzFNd3AJTNiaMJaOEddNV3gmmFoWCnDlKA2Ry2tDxSMI9uTP3Edu8_xmHnTqhxNRpvCOTwMBeafUvBDKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وفاداری گنابادی‌ها به شب ۱۵۴ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/453922" target="_blank">📅 22:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453920">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAO2ynybnv2UgWwssQtQorttWV2ecoAarbXSJrNPYX9-pFcdNGSiSNDxqnG639hloPrBTg8-d98VRhgFEhG9CX7LgODFnhV8kYQ1GmW7fxY0SAUuLi7rDFNsrWAGoJclNNgH7vheccKjHQkjkPHBqwzqAXINaPexriUjoEcXJ2dM1BKXIeETJ8fwgGRq4RzVXZHu5R2vhClhOXCIfQ5thx6OI6o0N0P7lueFtytOxmEpZIn_o4QT3_AZIOqri6aQwJctJMCCvTM8C8AGVBCD0Zc4IcQi5WJWPWpEDOAYfoOl-vJpVdUPB9eC8u9yDB9Zy6TK2Eg5KBqNOyewulCyKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا مجلس نباید لایحۀ رژیم حقوقی دریای خزر را تصویب کند؟
🔹
صفرنژاد، کارشناس مسائل بین‌الملل با انتقاد از ارسال مجدد لایحۀ «کنوانسیون رژیم حقوقی دریای خزر» به مجلس، گفت:  تصویب این لایحه در شرایط فعلی می‌تواند پیامدهای حقوقی، امنیتی و ژئوپلیتیکی برای ایران به همراه داشته باشد.
🔹
پیش از تصویب کنوانسیون، باید ۴ موافقت‌نامه در موضوع تقسیم بستر و زیربستر میان کشورهای ساحلی تعیین تکلیف شود تا منافع ایران به‌صورت شفاف در اسناد حقوقی ثبت شود.
🔹
تصویب کنوانسیون پیش از نهایی شدن اسناد تکمیلی، می‌تواند در آینده مستمسک حقوقی برای سایر کشورهای ساحلی ایجاد کند و بر روندهای امنیتی و ژئوپلیتیکی منطقه خزر تأثیر بگذارد.
🔹
نمایندگان مجلس باید با دقت حقوقی به این موضوع ورود کنند و در صورت لزوم، لایحه را برای رفع ابهامات و تکمیل اسناد پیوست به دولت بازگردانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/453920" target="_blank">📅 22:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453919">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4049471be.mp4?token=rEntAWwrAd_32dnyDG2bwGT7pHLAakLmNMbFyNYb7Ve87JXB02xbuPsnRKpR5dUMRxw1thMOMJyOsY1L2TxwillQrwMCWIeeB8IsEAwihTkEg8jhJoYv0CjJKFR5M_VznURtjsRbQR6YqVMEFUe33PtF3HNOj_Rbd3Htl2bGtlTYZEKrh1kkN1iVyPSELhOiXLsbEvvfc18mt_1S-kxFLJHfi_FN5cFu4MnJxA7T5QAjVgdqKChWhPtdB_aBsWXcYNmYE9y2eOiE30GpHc-0mFQLilIPBK2kAhahcK0ZPiL5gR7M2DeRFYIRHcR4ZMnOVxCQwQOE0zJLQJAIMIJSDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4049471be.mp4?token=rEntAWwrAd_32dnyDG2bwGT7pHLAakLmNMbFyNYb7Ve87JXB02xbuPsnRKpR5dUMRxw1thMOMJyOsY1L2TxwillQrwMCWIeeB8IsEAwihTkEg8jhJoYv0CjJKFR5M_VznURtjsRbQR6YqVMEFUe33PtF3HNOj_Rbd3Htl2bGtlTYZEKrh1kkN1iVyPSELhOiXLsbEvvfc18mt_1S-kxFLJHfi_FN5cFu4MnJxA7T5QAjVgdqKChWhPtdB_aBsWXcYNmYE9y2eOiE30GpHc-0mFQLilIPBK2kAhahcK0ZPiL5gR7M2DeRFYIRHcR4ZMnOVxCQwQOE0zJLQJAIMIJSDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابرپرچم‌های سرخ انتقام روی دست زائران کربلا
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/453919" target="_blank">📅 22:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453917">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a52f306e.mp4?token=qeCS4LTqg-QDw1t3SHg0guNNgAYEBqjkTblgZQcvVfd14XFhaaT91iRZ6Wk3vdm1UxfGsbq0FnR4A8jVgZfSMMF1lvxK3_YjdKhREvu5aWSg-Mek1KfrYoNh-3A9g1YLs2LM6ps5BrBseD1tMELCFZVtyeL8X1k6NfmRkn3dQlwOV2RLb8yBQ7NNnAQ-AaBIFaOcI9Qh1J2zmbNiX9j-LMhyual66GPjAvpwPCRiND8ZFKQvTxIlNdCwKyJbQdTB3sq2lXWWKGTNLkSDha3lKprB2fnW-e64-1n6LGSuMDTwC8-Hg6dJzn5rqWZF90YOrkz9WlCmTZH_7poxcP64QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a52f306e.mp4?token=qeCS4LTqg-QDw1t3SHg0guNNgAYEBqjkTblgZQcvVfd14XFhaaT91iRZ6Wk3vdm1UxfGsbq0FnR4A8jVgZfSMMF1lvxK3_YjdKhREvu5aWSg-Mek1KfrYoNh-3A9g1YLs2LM6ps5BrBseD1tMELCFZVtyeL8X1k6NfmRkn3dQlwOV2RLb8yBQ7NNnAQ-AaBIFaOcI9Qh1J2zmbNiX9j-LMhyual66GPjAvpwPCRiND8ZFKQvTxIlNdCwKyJbQdTB3sq2lXWWKGTNLkSDha3lKprB2fnW-e64-1n6LGSuMDTwC8-Hg6dJzn5rqWZF90YOrkz9WlCmTZH_7poxcP64QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق و بلندشدن ستون دود از پایگاه‌های تجزیه‌طلبان خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/453917" target="_blank">📅 22:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d264eaaf.mp4?token=ZqT6iGEqCRUfktDv1CbAbpoMFnkDJJ4Vv-M-43Xz2WHlO6pTQs8CR2nC6fc5oQefAjeOQ3AfSzjGqsgGYLlKOwYBxUI4Fhyg9VVB8quiFmUg3DiLuOnPHnLesjUDh6T75Xy5NvVuIGzUEItlU3a7GtCLmeVm4CzWyRMteXPYcwglAN7R5lG9WdIgrWahCKavvXd8usVg0TR02lDHqOHgjNwFFH4-U_X2g5UOPOSkMYgBvM6PJpwduZzxzOa9txD7bJ1TBndJrhx-K4bPtz87cmSGPQ6bbDeNKl1X9-p3lA8Dz8RO6SzuI6BLG1VoTQ3bwVw_XgGf5dYf6AAnqpg33g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d264eaaf.mp4?token=ZqT6iGEqCRUfktDv1CbAbpoMFnkDJJ4Vv-M-43Xz2WHlO6pTQs8CR2nC6fc5oQefAjeOQ3AfSzjGqsgGYLlKOwYBxUI4Fhyg9VVB8quiFmUg3DiLuOnPHnLesjUDh6T75Xy5NvVuIGzUEItlU3a7GtCLmeVm4CzWyRMteXPYcwglAN7R5lG9WdIgrWahCKavvXd8usVg0TR02lDHqOHgjNwFFH4-U_X2g5UOPOSkMYgBvM6PJpwduZzxzOa9txD7bJ1TBndJrhx-K4bPtz87cmSGPQ6bbDeNKl1X9-p3lA8Dz8RO6SzuI6BLG1VoTQ3bwVw_XgGf5dYf6AAnqpg33g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم سرخ انتقام روی پیشانی مشایه اربعین
🔹
هیئت‌های مختلف از جمله هیئت سید مجید بنی‌فاطمه و محمدحسین پویانفر با پرچم سرخ انتقام رهبر شهید در مراسم اربعین حسینی حضور پیدا کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/453915" target="_blank">📅 22:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2691e9f69.mp4?token=HA63jaIk8qtB6Ro6IcpAvm8iwapsykm8RpSjnhUn2l955puwgXxbAqqfhsfpPk2hBzpXQYf3QFNiVW9qNRUIQeil7Kt6ZeQNsjCzhh1VjJ7UwGgtHWVHTCXd5OIDj4lOh6VBTeRqZpXWBR35HKFNHw685VjA4h40wvYXuCrQ4PeQs-aJikDxA8cwzjdNsli4fB7zMDoae0u2icRUpA0evnvkoJgsSF_QzmQyZkA98Ksv_rBiAH03MGBjUoh864tPz87gaJfclmac5mV6tC28TBnacQ4WDOKSQ9L6wCC8H_xQz4eoUuIw8qfYaiqntx8Z3JIkG3ijDGWM0t_8yQ5Asg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2691e9f69.mp4?token=HA63jaIk8qtB6Ro6IcpAvm8iwapsykm8RpSjnhUn2l955puwgXxbAqqfhsfpPk2hBzpXQYf3QFNiVW9qNRUIQeil7Kt6ZeQNsjCzhh1VjJ7UwGgtHWVHTCXd5OIDj4lOh6VBTeRqZpXWBR35HKFNHw685VjA4h40wvYXuCrQ4PeQs-aJikDxA8cwzjdNsli4fB7zMDoae0u2icRUpA0evnvkoJgsSF_QzmQyZkA98Ksv_rBiAH03MGBjUoh864tPz87gaJfclmac5mV6tC28TBnacQ4WDOKSQ9L6wCC8H_xQz4eoUuIw8qfYaiqntx8Z3JIkG3ijDGWM0t_8yQ5Asg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار در مسکو ۳ کشته برجا گذاشت
🔹
خبرگزاری تاس روسیه: درپی انفجاری در نزدیکی یک کافه در مسکو، ۳ نفر کشته و ۱۵ فرد مجروح شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/453914" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG2PlUB9X-MVRC8zE0Ybd0JgJbc0c8q3JKoGZ79ksFSNvx8eEHcP3Vg9SUYKWX9SRYn5KHa7-jMXrifAymSIpphamodUvPgFgx_amzwhch8nwgzUcZkdMxT4ALtr2MeO1VRTsn7oVORdy_usbaRMPO461Se89YF37s9H87hdrJu5ke8b_TRqgaaVX5cukYiMl07fw6ky1sjVsiyrBo5zl5sZV6wUnBKCJuqEhe6eDWmEgm7RFzD9WWTE0cfQewtSyHprpOLuU0hHgizXZyWaY_6ooPgGgwsO2yVWzh8qYxQV8QfEVIEejux7NBpjRshCR3N2dN1vb_DNf3jfiHLHBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوچک‌زاده: با لایحۀ جدید مجلس، مجازات نتانیاهو و ترامپ حبس و جزای نقدی می‌شود!
🔹
در لایحۀ جدیدی که با عنوان «لایحه جنایات بین‌المللی» در مجلس تدوین شده، به قوانین مجازات اسلامی ازجمله حکم قصاص دربارۀ جنایتکاران بی‌توجهی شده است.
🔹
تصویب این لایحه بدون اصلاحات اساسی هیچ کمکی به ما در جهت رسیدگی به جنایات رژیم صهیونیستی و آمریکا نمی‌کند.
🔹
حداکثر مجازات پیش‌بینی شده برای اشخاصی مثل نتانیاهو و ترامپ بر اساس مفاد بند اول مواد مختلف ۳، ۴ و ۵ حبس و جزای نقدی خواهد بود!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453913" target="_blank">📅 22:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e869dead1.mp4?token=iDtBAlAg6O-mpI5d9TrVKfLUZ3TaaZk5kUkV0EsgcA6bM3w9Ivypc8rho68Kp6QrQPB2YX1Xt2wtvSNP0hRSJN0tHLrUQrPLpYaV0YmEJaa16RJMgrteU01BiDLju8efX2YwAVogeOQx6E_hEaly0KAmquTJUKtWH7FUOTy6ZacxqaM-Igw7DKcwaf0n60cnivv5hF2ohuKnKMUo7AECdqGWYq_gcAB82Gk0O40ef6COHWI1kvpJ6NzFy4uT1xaNDjnIgv8wCHU-WqpK0KUKTOzcuwfUTCKCxhJnYKwXqBnzvQKTcHYqZ24m30uaILUdbJTvf8yEfTLvci6m4ZUNVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e869dead1.mp4?token=iDtBAlAg6O-mpI5d9TrVKfLUZ3TaaZk5kUkV0EsgcA6bM3w9Ivypc8rho68Kp6QrQPB2YX1Xt2wtvSNP0hRSJN0tHLrUQrPLpYaV0YmEJaa16RJMgrteU01BiDLju8efX2YwAVogeOQx6E_hEaly0KAmquTJUKtWH7FUOTy6ZacxqaM-Igw7DKcwaf0n60cnivv5hF2ohuKnKMUo7AECdqGWYq_gcAB82Gk0O40ef6COHWI1kvpJ6NzFy4uT1xaNDjnIgv8wCHU-WqpK0KUKTOzcuwfUTCKCxhJnYKwXqBnzvQKTcHYqZ24m30uaILUdbJTvf8yEfTLvci6m4ZUNVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداح «باید برخاست» پرچم خون‌خواهی را در مسیر مشایه برافراشت
🔹
پرچم خون‌خواهی رهبر شهید انقلاب در موکب مکتب شهید حاج قاسم سلیمانی در عمود ۵۳۳ طریق نجف به کربلا، ۲۴ ساعته توسط مردم برافراشته‌ است.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/453912" target="_blank">📅 22:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453904">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrNkxJciwg_ZSz44IdOMqzAchfZpwzkAodK501oIff5FYctKSsZzPHqyEmwT95aJEKlrHPZGtjLwKFOdrSmvs2g7URfWXLwlhIipHsQNN1vJmhyAXtsE8WGxljxj3kV1Sywsl7e16F9a17JH8MezuGMGyftnrmDOqb0Tv5sVBGCJMTCc-tkiYkNDP_09hf0VQSVB5DJfACWTJrgg7aVYf6R-6Lt9MhJ6o7CRsdHA6ICxOW2Bcmh22RHf3Dc2xkAdT_mhA0K6ZjSPYOoUNxPMhcuJ2cdXVBw2eBiEK6WO2tmG6WnIe_g3d3bexhou4JWdVNB1T-RP3ZbH2_iyXrN8aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gDfMeaNAJMS7iU0R9LgyBW_FUfp23WGSgoEo27KNqOiaqjjVnLjokeYzyl7wu750rC3jShZk1AgUlDDIkWS4yNHMip2WhtLo32pGArqN3B0jwg6_y1-PgEKNkPBVqoK-d-yxtGrZZJE2tDu1Wh_F14K2_YYcusttWPQHgiayss6GHjK9zyR5qqhzNZLG-kSsawxXEbDYz7Wo2hE0wGjeioxJRVSwqAEkNC7do8P1Phb3QPlkfnu0jmVhkg2lf0LbsZkxRgHpXahydVHQLREZYZGBvANnSfT8CBCYj20CoFQHytUPcbUIl1prHZEf0qOLlRiBDALIqHkc5eCh0v6zhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hAI233H2mSZf8sCZgKMSQXqyBMYIBvfYANmpNTQNHU5PmyV3jy5DLk70UX-TM4PZPUhk2arzpkdpg_0ndYYsKUKyebjOSH5556P7sFdugkTMb5JGPDwAsPMA2BfNrTuBIs-MhKulHeGYq4tlIqB6BT_ZXWYyskpxo4UNvPOh0Nd65Emg43GslN2ubhT8eiGv21fhIITsxM5w9UBf2FVkTHKQiIR9530XoWzbxGFszTGNzHP3Fv-CY10XQJtJKFA8Y-l67MI3jgwKAhQIKr0zbHRb7sJhfLcHa9knAui5LIkYyjEZV-nL7DYmSnrt-voUax4Kk0_gm2hrEdQG7PAZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iU6nbyJze96Bw2whqwFoflSGX9wlSQVtNGGPmjVL0dhIOXsQF05_07Yu-PCIqdXlENw_fVczDyFEjKIXOLi6KhTaGZP0uaig3vnnq1OIU4rgy5WFe8TPpjGl7xGgdMzGdNFmRuSdf2YjJ1o1yrPizYsYSBYChuLjNla1SVlveZoe565HTKjXCxKmq0YteSlga-GouGwvnCEqz1H8OaJ76fluJtoNFlfp-nmdn3O1TChkdfRWlveH9ge_59RaEg8idVPh8ype-DyYyy9xnDV0NPddNKhtbbDZ-syticp71y4h5RWU9fMWH0E0o6Ar2b0iWnwRQ5jPVBqnc4gqrreM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lryFK70gRVTNb0bjCgPMDUBy3EzZnpvY2CMWeOwO1cLJsbYumjuYiax2HPyi_VNHyo7TWR2Im7orJWxMCV1BusHsxz4IVVjsNJF-Fjudqu-Ds3mhO0rEahQP6-7N_t9D1qovCJkotixV_UecuJeqiQG9UsFtvgeiBCDNF3qr_uyMhS573T1iIOYycmoH5M2W1LJpEVUaLclDZKvwMHwPL4-ijrVVO4kZb4YnsvSKQ8-y4Yy7PP2SVaL47f59ik_qXb-skeMOD4mXaOBACQKeR3yK0R_Faoo5SssEVSdNBcEcuEyAQODMv2OOz1Flwe3mjfybgQJFNbKtfzys5oBbZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a8KxHObi_JMzHcUrliwlpo7NRKt4H10mmxKHeKCZVMVTjgW1Bi9I3R6Ka7su0ycWvNeP3xxjNdhfKuQnTUhiJ3Sf6SAaTO1gi7ct64vEfZ-SBwY92-RKzXUzF2Sxc0A1cMItM2l2t2wwtVfyZ_TKnlRRW1YeYeWSP5PVVi3ETQy27MJrSxPkbRRsnZvN4TxxiFNgm70Jr5ZZv48xPOSn0RcL1jknnmyVQdjKZ4fziKxrhBqlOQLe3VgVP52TWiyYTDPfIOgO-3RRZuwsuBahZg-DrBsv41g3Kv2wIydqQ9dNkNTS_qtVKfk5XiweZe6O1sEKQpL8V4wTGbrIgXEd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAGWA6pxNDP7r0kn0NDmAyQYmUYQmSHDBYyDvupO9xjZVPSoMTYEHYqT-eXRDHuxecIXYnjTOP3CMq9FdJfRwf9HG4enzbbSDvEnY050yM889srIF7URXAmh_465B_6ER9oADhAVQMgNnxJhRX0lQIkODXIyDK8PPFA5bp1blKN8OZdJW2jAvMx584pDfSz7IIjMIVgfZRpc113yQIjKGO-SgoIxO99VkMltwORWXTcROixSVSqbZzyVhD4QEaRBajgC8A7bhKSNM585_R8-UHI9LU6YoOP6RfUhfuEUheaXBCaIix5PddRHJUYlyqwLZbp12ph1kTUfQ4uiyrUuWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نائب‌الزیارۀ رهبر شهید
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453904" target="_blank">📅 21:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453903">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">40 Rooz</div>
  <div class="tg-doc-extra">Mohsen Chavoshi</div>
</div>
<a href="https://t.me/farsna/453903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
با چشمای پرخون با
ا
ین قلب پاره، رسیدم به خاک عزیزت دوباره
🔹
قطعۀ جدید محسن چاوشی به مناسبت اربعین حسینی.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/453903" target="_blank">📅 21:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453902">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd77f123d.mp4?token=q9Ebuc8XX3yni4U9WAeAV74XtyaVcAv7AousKy9of_NlV64LvE2w4-Ztc5ion4gK326hNc5iLqia3W2JrqQuNE_pU74RvzZz0Suuwu8BcgP4ARir4lMAWz8oFanJEZCTJXr-iwWoKYPSOKRncU4Q8hjQpj--1-xrvf9cfOY09Vr30NJ8XNJnQ8xbtcMJHeO1VErShj4zrzNVs0rTKa94HuxnL-w6JgqVqjuzz7owGmfxuRJGWt_UIgrrXBFIx-QbVi-7JIZTecweBjT1_0KXWOAk0h0GREgalM7Cg6-q-qKgW_0K1jHl9_OU7Fxc-TDTsXnhNpiffMx0ZaPur5pdcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd77f123d.mp4?token=q9Ebuc8XX3yni4U9WAeAV74XtyaVcAv7AousKy9of_NlV64LvE2w4-Ztc5ion4gK326hNc5iLqia3W2JrqQuNE_pU74RvzZz0Suuwu8BcgP4ARir4lMAWz8oFanJEZCTJXr-iwWoKYPSOKRncU4Q8hjQpj--1-xrvf9cfOY09Vr30NJ8XNJnQ8xbtcMJHeO1VErShj4zrzNVs0rTKa94HuxnL-w6JgqVqjuzz7owGmfxuRJGWt_UIgrrXBFIx-QbVi-7JIZTecweBjT1_0KXWOAk0h0GREgalM7Cg6-q-qKgW_0K1jHl9_OU7Fxc-TDTsXnhNpiffMx0ZaPur5pdcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاموشی‌ در استان‌های جنوبی کم شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/453902" target="_blank">📅 21:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453901">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2057c351b.mp4?token=NuOnIfZXxZ1hcEHPnD5vf0gHmEs_vdCvC3tQlmj6n_uLctLslTTWG82Kp-TQjVuVxaEb3CvRq5B7SKIteT8sRv4a1ZRc-hIu9jAS44Sat8_vvmHk0jsHAkkDqq_EDdi-ueZVptuDDUej7syTqkWNlxA277M5_lcmFJUYJkRHDLDSXkLUZk1gMHCJBrbKyb-aYgc6LIPBq_zbUa4ExFUjBMb7RSa4c07XWi7VvW9kA51o55Yr_9oylsxn7ZSXm-1HHAbtUoBFLOZLIKj8iTXIM_M8gsS6L0hGAjQZNGLkjWHPe3cmHdPw3_4hT49A3T5KdixOmkeYQZR54zHrxZvClw85IvA37gNeQWPe7GMoSZliLFWDpYQiiB69C2IBmv6Xrdue_rmrZEE7grALdBymwxAVIlJTPGwgCQqkm6ZGSc5vJr700OcZG3RGnitUYXrNMjGN2pHYLqMXw35ERHR40T8q20clU7HIeGQwPr6gV63gEhmDSHSmeBXmzbN6LQFR0WLW-rup-VTFHzNMbY1_LkHEYzEqwvX8wHJCojcm40QjJei8KI3W6cGL3WNzrJ4MeEKEYwLX6cfidfCagSEW0eq_QjCnn4J8B3TV6i_4CdMNtu50xtepoFu-jNxQ719AuzDZGoM9ey5yHo--vubHUv3k2EvKUp3P5xG3bej1w2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2057c351b.mp4?token=NuOnIfZXxZ1hcEHPnD5vf0gHmEs_vdCvC3tQlmj6n_uLctLslTTWG82Kp-TQjVuVxaEb3CvRq5B7SKIteT8sRv4a1ZRc-hIu9jAS44Sat8_vvmHk0jsHAkkDqq_EDdi-ueZVptuDDUej7syTqkWNlxA277M5_lcmFJUYJkRHDLDSXkLUZk1gMHCJBrbKyb-aYgc6LIPBq_zbUa4ExFUjBMb7RSa4c07XWi7VvW9kA51o55Yr_9oylsxn7ZSXm-1HHAbtUoBFLOZLIKj8iTXIM_M8gsS6L0hGAjQZNGLkjWHPe3cmHdPw3_4hT49A3T5KdixOmkeYQZR54zHrxZvClw85IvA37gNeQWPe7GMoSZliLFWDpYQiiB69C2IBmv6Xrdue_rmrZEE7grALdBymwxAVIlJTPGwgCQqkm6ZGSc5vJr700OcZG3RGnitUYXrNMjGN2pHYLqMXw35ERHR40T8q20clU7HIeGQwPr6gV63gEhmDSHSmeBXmzbN6LQFR0WLW-rup-VTFHzNMbY1_LkHEYzEqwvX8wHJCojcm40QjJei8KI3W6cGL3WNzrJ4MeEKEYwLX6cfidfCagSEW0eq_QjCnn4J8B3TV6i_4CdMNtu50xtepoFu-jNxQ719AuzDZGoM9ey5yHo--vubHUv3k2EvKUp3P5xG3bej1w2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ام‌کیو۹ دیگر تولید نخواهد شد!
🔹
آسمان ایران، گورستان پهپاد ۳۴  میلیون دلاری آمریکا.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/453901" target="_blank">📅 21:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453900">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b760780f56.mp4?token=byh8RH9nGt-2tssu9k59ORTIHc2Ia_WFTkkzAZi8cx8TseupGn3BcbPwE_jW2B1Jz2_zee2TRX6CDldyDyIh0e2GFUIg882B5xHStmuUnn7K0HrpWrJMQv3kfimCcQ_MkyoQVxCACzzenxKhBVc1oCAOG8iRnm_epCIHAPeHIsprvifnfIwlmyypXpTeIitHrisb_LRleNG16PAWa8kucJ36sYB0mEkQMzIDNIPjysT2TD5CDq0Pg6yym_67-Uf-mb_knkLRj5X2JiJGcSkjnDkyGJkK_7J_xkahgp9EjZHv2f29a2JY1mhJFMiSgWkykgUfSm6mdVG9hlOz7SMMvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b760780f56.mp4?token=byh8RH9nGt-2tssu9k59ORTIHc2Ia_WFTkkzAZi8cx8TseupGn3BcbPwE_jW2B1Jz2_zee2TRX6CDldyDyIh0e2GFUIg882B5xHStmuUnn7K0HrpWrJMQv3kfimCcQ_MkyoQVxCACzzenxKhBVc1oCAOG8iRnm_epCIHAPeHIsprvifnfIwlmyypXpTeIitHrisb_LRleNG16PAWa8kucJ36sYB0mEkQMzIDNIPjysT2TD5CDq0Pg6yym_67-Uf-mb_knkLRj5X2JiJGcSkjnDkyGJkK_7J_xkahgp9EjZHv2f29a2JY1mhJFMiSgWkykgUfSm6mdVG9hlOz7SMMvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری زائران اربعین در حرم حضرت عباس
(ع)
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/453900" target="_blank">📅 21:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2312d74af7.mp4?token=sfMkAOFHglas-XNsw3UpImNrbCt0GsAYEdw9SxCT2uiora0lR7RVKsc1aDy9Y-uX1GDxCrF3gBgN80Ux-N-xf_QdNd1w7AwtnQziVks78xat6EYp_PYprDi9soe4H22h7k_dpIqFMpbWYeInOZWYs3lzRuSIgSsonLBPfnISiTN5qYTcaVvUQtKkzlrj5weIIuWG5ZPr8XK22ickMpqWjh205wSnNL_3npJQn62svrHwQznVkRVc4ZKp-t0EV2Do5pA4bhuCt0_8Gj-k2ufeyR1Asotxm7QJh-6tbr1AMrgCaAvW572dg_en45A_p_J100JmHazbHGUZv2XjFd5cs7DbBqN1cGumubTLoVC1VpIC8K0uDXHXyxga2j0LXzBhR8gVRFzAw58dF1YT3AYPB-3uy-9I3LXrPAXHmO0_uY1g236362iTOEvRSlK7MHYkKhCxpUNBCx9t-UNWDSbHb8eOSIF5WIUZBWEmeRciJ_CmJ2O15qf-KZ3-MF-i96lDRb1-BJOmZkpxGgUvvRLEE5OW0OBqLpttQeGHgpgFYgvptPsRSWHLtQ-H7hVGg57QoRWrOy99wL67qO6KJ1xskA8GsAPSCck10AmVXhTEx9KfgUbOfobFRxcXJzmhsyrAi8PC08qyznBlLohpM-AwftYRR46orB85QainkQBJKmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2312d74af7.mp4?token=sfMkAOFHglas-XNsw3UpImNrbCt0GsAYEdw9SxCT2uiora0lR7RVKsc1aDy9Y-uX1GDxCrF3gBgN80Ux-N-xf_QdNd1w7AwtnQziVks78xat6EYp_PYprDi9soe4H22h7k_dpIqFMpbWYeInOZWYs3lzRuSIgSsonLBPfnISiTN5qYTcaVvUQtKkzlrj5weIIuWG5ZPr8XK22ickMpqWjh205wSnNL_3npJQn62svrHwQznVkRVc4ZKp-t0EV2Do5pA4bhuCt0_8Gj-k2ufeyR1Asotxm7QJh-6tbr1AMrgCaAvW572dg_en45A_p_J100JmHazbHGUZv2XjFd5cs7DbBqN1cGumubTLoVC1VpIC8K0uDXHXyxga2j0LXzBhR8gVRFzAw58dF1YT3AYPB-3uy-9I3LXrPAXHmO0_uY1g236362iTOEvRSlK7MHYkKhCxpUNBCx9t-UNWDSbHb8eOSIF5WIUZBWEmeRciJ_CmJ2O15qf-KZ3-MF-i96lDRb1-BJOmZkpxGgUvvRLEE5OW0OBqLpttQeGHgpgFYgvptPsRSWHLtQ-H7hVGg57QoRWrOy99wL67qO6KJ1xskA8GsAPSCck10AmVXhTEx9KfgUbOfobFRxcXJzmhsyrAi8PC08qyznBlLohpM-AwftYRR46orB85QainkQBJKmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایران این‌گونه تجمعات انقلابی خود را با طریق‌الحسین پیوند زدند
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453899" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfba2ec58.mp4?token=acSiFMRz_2Ow4jmTkpEOsK7cpb699uF-A7wn4gnXb_KnV9uPIGHYYBbiz0eXNouxDPctmFVwJLGz3CDuKfohaP5d3rpxLmo-CjmPlutKrTCXwjOToz0C59wXcFpUEmW6YJJxbha6qeKrTCX8i0zSFjkY1LqtXeQXaVfdKBFuBwK-r5YXmncJYzEg5oZRMhdhtU1tRzju7VYUgvoE4GnWAHlw-jcLekSZj43lfXsNHs04cZPvVLgLsqxjeQ5LV6Ckm2vb5kkaCKsTxtWWSokh7fA69un4_VIzAPddXm2BauqAX1b-jqxrYVJcOzqrQP6_jTfs30O5eArUsXWBeBfnYk1NN26OK6xogY4aI1jfrP-sZjniICduuZJf5HM_vYxaJ-vn9JPUDIdxhiptH6_cGkjTyV1oByLzqzYKHaec390TXdTB-xTGYQT3cKRd2gEHBmeoFrLpTxzckAazO1qQ1v_OCfpxfINrFEJOd9oJdQPRS_QOXCA3djLXcj3plpluKyI9kEqxqwJXT-ShpJDuQvqDMOqjVxvZWePiypODOz0DTXqy4x0WzGwaNfVasKHBa0HZGooBTyV40DCGSe2pMFy_ZzCHRznWO9MWbQwUspXEgV-mK4l6lVE-AGHLKz5ECkaNeaEjA87sD8va8GdlkBLc8jmubCqiw4nBqT4KRqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfba2ec58.mp4?token=acSiFMRz_2Ow4jmTkpEOsK7cpb699uF-A7wn4gnXb_KnV9uPIGHYYBbiz0eXNouxDPctmFVwJLGz3CDuKfohaP5d3rpxLmo-CjmPlutKrTCXwjOToz0C59wXcFpUEmW6YJJxbha6qeKrTCX8i0zSFjkY1LqtXeQXaVfdKBFuBwK-r5YXmncJYzEg5oZRMhdhtU1tRzju7VYUgvoE4GnWAHlw-jcLekSZj43lfXsNHs04cZPvVLgLsqxjeQ5LV6Ckm2vb5kkaCKsTxtWWSokh7fA69un4_VIzAPddXm2BauqAX1b-jqxrYVJcOzqrQP6_jTfs30O5eArUsXWBeBfnYk1NN26OK6xogY4aI1jfrP-sZjniICduuZJf5HM_vYxaJ-vn9JPUDIdxhiptH6_cGkjTyV1oByLzqzYKHaec390TXdTB-xTGYQT3cKRd2gEHBmeoFrLpTxzckAazO1qQ1v_OCfpxfINrFEJOd9oJdQPRS_QOXCA3djLXcj3plpluKyI9kEqxqwJXT-ShpJDuQvqDMOqjVxvZWePiypODOz0DTXqy4x0WzGwaNfVasKHBa0HZGooBTyV40DCGSe2pMFy_ZzCHRznWO9MWbQwUspXEgV-mK4l6lVE-AGHLKz5ECkaNeaEjA87sD8va8GdlkBLc8jmubCqiw4nBqT4KRqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ استاندار ایلام به چرایی ازدحام در مرز مهران
🔹
با هماهنگی وزارت کشور تا صبح فردا ۱۵۰ اتوبوس و ۱۰۰ دستگاه وَن اضافه می‌شود.
🔹
از بامداد تا ساعت ۱۸ امروز، ۸۵۰ دستگاه اتوبوس در حوزه مسافرگیری و جابه‌جایی فعال بوده و مجموعاً ۲۶ هزار نفر توسط ناوگان اتوبوسی منتقل شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453898" target="_blank">📅 21:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453891">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2d2Sv_qaAIDJ_-nDQAWRFw66b0XWi7hBlLgbrZ-GwG53FKIrJ2OMkhZKgN5LvMhK9fACwS675zGZtkxytOHEOwNy8xBP7UKbkuZ_6ROuwoQFaX3ugSTORY83SIuBiESD3oVWmHJf-42dFucwtC1iBNFK16ZyqPt2DIX1SmD0Ffu6V8SW0JYN8VCXp_FFkYYo7mBptdYD7Qp36PQfnhhMhLiByPe8XqgoH00zenuXrusOdqz-VCBXffY-v8ptLoO7MpbhGgkob1Lern0X5MuonfNeTeb8uyIwt5ooVfDXzHqqHLLg7LTC03yAy5HHOK7b-AZrHtx7Hp8RdFfjHeAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KEMZ8yg-T9oSJ7CRbvuIvr8cE6HkLakd3UQ0VwdNHmhnGLKP_mCAqlwZlKFjC0BP_LXhALSgOBq452qVd17k0TOQpm-c6CU-ZkPrCOuRua1ZON9UqSWg-Udi7hjVeT6A1yTOyi3q2rJGVdBvYfdIEF714zWeBcabWC_WzTtT9vvOBykpUXIE_jWeAoX72jNj_CdYESH-91Ursj64FSQ7BCveGH2u2Nks-z5L2ph39GqnHCOuYYBEGBz5hrrh8eyl4DHp20ESmnt83mbd3NZP62fMUNcmeEK2ha7G5uc9xetjAdWnTCKLjpYLFXT6WzbZhT2ih0sWjy2BeIlyo6QKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqrhIczTPCPtJFuUiw6lE36GfWAvtO4FRkAd8vq0G8QRpGzZmb0u0kN41tZkJs5C4_emHFezyNjJChPWq_XHyw1eQCK6gnV9JUUHbdNP_y3sQlFPe3uUGhw8yvP7nhy8qACfNn9kxRHUaiUh-Amwpt97R3kzDXzPNb5JFLLUHR5YpA-Z5M8TzBwfcnQc7_tNnYbO-Bnz-2ejz-yi6RW8LDKZUM1C6Bc2Xsl1dXTo1lNiNB8cdbA-dpFrFEmf7XcRCcQUuetOvLqfNsRZagKIV8tgdr1ENj9KAQ9anMAgwYOjQ5GVPb8qSqyufqXsULiUNasoKYqMcC-y2cez8rxj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cjv1Czl7LPuC9QISmoFE6U6fy9yz7SDIItuCYUZFnyVXZQnC0APXX9ZTe0ocY4-TQ_dqhujfNSbkpX-QGseD456Knv-yq3Y3t3J_gQfV1_WiBa7uG-rJdHNuD4siHKveNA-JakhfDcm5yrAwYjNXiBppEBKZ_TwWcFWMfKHFCgWVfbKuHTlIrJ6xYksUJKiDjHz28zIy4zSRt5Qr7hjc5LY9gVanbk7mUDFziQ-jXUfHmcWO0rVMIBWokIHxiL67NiisatMelghNX79fJkNDUPC5lp3MTVefVeHzgKb8DQ_W-fEE3KLg_cocXjabm4v3ZJd9ZsEZ3T183HLCgD0XJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/his0cKzr2wq5eUA0NdMJoRgE6-KPxuVWK1PrL2T8kZGf8JckBXwqP9dCEp4Aq6dwdKUYO3uSbaH-VcPvg18_Wja829LTj9eWVQVUFeR5GHta3BiZ9Wbd33EO2GCbpUdGh2J_AC6LGPf7_-fpvCdXDAlAy0SD6Sm0Ab3AMSG64qh1kFPmRw2drY2JCNkquUkVmfHYrnWpQxqShZQLP7cqr_OjFBYuHHyvX4q6lVPZ4pUICM5Npe6GJ42RFnDFPBGhUqM54xQoUoZNnK8wQFWoDgokMxsfmwNpBpQZpI_D__AaI9yRqDuuSDAtJ5vyD9dT5N8X0UM0Tl0NsLEEP93-uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHF_bv3Sxg_PNbR63eWel0h47p4OjhBH9BDXzH1GXTscaG6KtNv19OrSZ89Dz0-E1GZvnOzDhH3B_i3Njx0JfDcCAeX0Fh5Zr1mfAeCOfWdIdaFXokpmCWeOgZFkyCS59AKaUw93RoVPQdce83RGncc-8cAwO6fy-q6rCQUiC3us4EdU_bG7RL1PXNdYP5DNx7lX8ChNFd5CycSTJlU7DsdqH6REylzSeAEdOSGEQqCwgeevC9RzBj15rcI_Pod2eUXGWRNIM1JDCmMFnULXzq1ka3p8B0SiUSF7ClsMsyQwjl8egOY2eKpC1el2gQcEpN9UXhq1d0PWSdEZd1eTjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aAYxrl1MU9Qu6va3vHrs_UlwHN3pWqE0cpRcIF05nzzTnbPfVzqBBLVUZWx9svLLKjte0R-LHvNUZYwa9liOjxNbesiVF_R8RCq23mRSYD4_XkHywHwelLC54711falJ_6FoYDo6ZO3vYzox1ABfWHRoFw8WdrxN43RkBAH-_mloE4agoqwxLDYNRxTcZ0wthPdsSSsnKD9spP2kXcTRiq9O7vrKO1las9pXQ5RZQ2VBPI_bM3DbjWJt2XgrccYGrTocOSTCX1EToEnwNQ15IYMFp4PltTS3FwFKBRVJWJwOkkyvO4MHpHgfIxNAUv3PY-haCfuymzCluBMmUmDXTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آئین پوش‌کشی؛ آماده‌سازی مسجد جامع کبیر یزد برای مراسم اربعین
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/453891" target="_blank">📅 20:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453890">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baf2f5ecb.mp4?token=BXn1pQnqptSJRr_QnVCz17b9_e9zl4qpOPePoBQljB2Ho3VOSo8YfyLRpZmICcnuSCVjInWlZJ6pFlkUJzeM5CB4S65Fb2_f1CW493k6Cxz1NmCCARcVFB6XQDU-3Aer6WOhQeaK346EhSMlbeVJvM4JRBHv-oi4QRJMEGPWmMv4piVO655kmQkfeopvzbJBrVAKgtkGmDJWtZ0xCEH2cRxe68SkhMZl_XB3VPcwNMfP4SpuPEqcyHn7oplJsZbUkG94j4Uo1ug6rwArxgZttWcRpmsjDzu1WMiNMKygjad0RZgk-Ud6Hxp1o9EFacDekV12eiauFwzsfp7B5s7azGSq6crs7NZD6U5xERyfQrtaI3EbpLN8HpjhwKLHxlawGXAw-yHtW0ukEVuyICoanpoNaiNzUqKKbB2BNTDuytP2OlSPzO6r2iUj9sljuJhDHEwlNPFhM0z4KGx9eNR_wO-PREdYslSdfMp9X_kiVyUZ3J3hjhlbcHZt8Jnx_5trz1EhMiaTuA8D948NRdducO3-3_KXkwiMVxxO459wj32Z26gpNTnqRVVdvZZ-1KiqHWHcUKbN12WXo3Omr5n62-le9PrGbdFIS2e2gYLJH_ZIdJrfWLFVn32mqLIk8rta2xBr83NF7k_ui_0B-2vre_7tUSNG1o-iuUIxTdwzU14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baf2f5ecb.mp4?token=BXn1pQnqptSJRr_QnVCz17b9_e9zl4qpOPePoBQljB2Ho3VOSo8YfyLRpZmICcnuSCVjInWlZJ6pFlkUJzeM5CB4S65Fb2_f1CW493k6Cxz1NmCCARcVFB6XQDU-3Aer6WOhQeaK346EhSMlbeVJvM4JRBHv-oi4QRJMEGPWmMv4piVO655kmQkfeopvzbJBrVAKgtkGmDJWtZ0xCEH2cRxe68SkhMZl_XB3VPcwNMfP4SpuPEqcyHn7oplJsZbUkG94j4Uo1ug6rwArxgZttWcRpmsjDzu1WMiNMKygjad0RZgk-Ud6Hxp1o9EFacDekV12eiauFwzsfp7B5s7azGSq6crs7NZD6U5xERyfQrtaI3EbpLN8HpjhwKLHxlawGXAw-yHtW0ukEVuyICoanpoNaiNzUqKKbB2BNTDuytP2OlSPzO6r2iUj9sljuJhDHEwlNPFhM0z4KGx9eNR_wO-PREdYslSdfMp9X_kiVyUZ3J3hjhlbcHZt8Jnx_5trz1EhMiaTuA8D948NRdducO3-3_KXkwiMVxxO459wj32Z26gpNTnqRVVdvZZ-1KiqHWHcUKbN12WXo3Omr5n62-le9PrGbdFIS2e2gYLJH_ZIdJrfWLFVn32mqLIk8rta2xBr83NF7k_ui_0B-2vre_7tUSNG1o-iuUIxTdwzU14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌هایی از مراسم تشییع و اقامه نماز رهبر شهید انقلاب بر پیکر شهید اسماعیل هنیه به مناسبت سالگرد شهادت او
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453890" target="_blank">📅 20:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453889">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32d2e8466c.mp4?token=IlfP73Xm-G7VtEAu6oP7_Vm1OfCtN9T8z0kKl5ZRzjpBSI0pkcMW9xKNG9JLt19X8HxQhfwYPbIEqBMm_Vny1nw4UHvovdMAzkdTqwIYXVhbkNbVMjHKhFo_Qywa4FCN7QiaQpULgRHELwbZM4T8_T5T1f9q03HGGBnXbj8hI2V6sS5owWlFy8dx40IOe-E_VgIi_9aK0w8L_mLulPL0NT5prejS_lj5Yugw6xFhPznBYomC1-V7XGKO9KH8rD_eRI4AQFvMgAyarJ_4wZ1V0_hKfLDv-zE0FJ1IiBrYqjxJoIYmc_CSOZqBDvkKnJjJng6Nhp-_DrA8H1nePZ6e14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32d2e8466c.mp4?token=IlfP73Xm-G7VtEAu6oP7_Vm1OfCtN9T8z0kKl5ZRzjpBSI0pkcMW9xKNG9JLt19X8HxQhfwYPbIEqBMm_Vny1nw4UHvovdMAzkdTqwIYXVhbkNbVMjHKhFo_Qywa4FCN7QiaQpULgRHELwbZM4T8_T5T1f9q03HGGBnXbj8hI2V6sS5owWlFy8dx40IOe-E_VgIi_9aK0w8L_mLulPL0NT5prejS_lj5Yugw6xFhPznBYomC1-V7XGKO9KH8rD_eRI4AQFvMgAyarJ_4wZ1V0_hKfLDv-zE0FJ1IiBrYqjxJoIYmc_CSOZqBDvkKnJjJng6Nhp-_DrA8H1nePZ6e14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلوغی مسیر مشایه نجف کربلا در خنکای قبل از غروب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/453889" target="_blank">📅 20:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453888">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a7e74c10c.mp4?token=aJAYCfG3O8wBV7nSp4vRvkTwle_SGJj_J9DLc4SaVIbw1oJV1VLtmG1FaLqamlWq_m2Wr7_zBg99D94oX0Hs9brllMp7WJbT4TIxhkIz1kUnyPt2P_ri3uu88GTSDnUDseI4-BBWFSo0yP3s3xRSK7dbtRYlReU0tLTCQ9AwVWdQvWrxaRTWqlq-ZFdcUoMDZJISESWY57r0O_NV2X-MHldv3Kdr1aw55vkFGT-AbsBhtxGXZXIvWz4Kc0pkE9EG5K-AqIIp60eCmjAAzGQbgjC4xGSamrWwhEB2m3JKYiTyUNPFbM2Y3o0WsobRQqsPhvYm2C8SNGSvCzUwvYQ-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a7e74c10c.mp4?token=aJAYCfG3O8wBV7nSp4vRvkTwle_SGJj_J9DLc4SaVIbw1oJV1VLtmG1FaLqamlWq_m2Wr7_zBg99D94oX0Hs9brllMp7WJbT4TIxhkIz1kUnyPt2P_ri3uu88GTSDnUDseI4-BBWFSo0yP3s3xRSK7dbtRYlReU0tLTCQ9AwVWdQvWrxaRTWqlq-ZFdcUoMDZJISESWY57r0O_NV2X-MHldv3Kdr1aw55vkFGT-AbsBhtxGXZXIvWz4Kc0pkE9EG5K-AqIIp60eCmjAAzGQbgjC4xGSamrWwhEB2m3JKYiTyUNPFbM2Y3o0WsobRQqsPhvYm2C8SNGSvCzUwvYQ-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیگیری تلفنی پزشکیان برای پرداخت حقوق اعضای هیئت علمی: این تاخیر ۱۰ روزه واقعاً قابل قبول نیست. کاری کنید که اساتید بیش از این ناراضی نشوند
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453888" target="_blank">📅 20:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453887">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfb546460.mp4?token=s1GSMbdDW3jWPGfb7GYb2AVsTZsAj196FqCk1_TrIg4AGiyhb8DLGsxH09Zx1rDXRLPtApPEG6O8TziHE8X_AdzZH1cByhRjT84TzMK4pVv6EML97wrfHrJurqAETpWuRGd9Jw87HwAm5scoISBKLiY6usGvzWEzZ4Qk2nhNzsAP0VTeLThavKTU2We0lYpTQXwMYbmwnAaJ0DCAYs4mDWTxDWOFtg7zdc4wt3-nOSaRtQt2U5IzQ8U3NFrAaI13nPCqDD5Rrxd8BUihVATRlrOEJ1ktw0aSvCC3o8pLcwXCTvnWK8rl19_ThfR3tVPBoTveUNw_cLKtxAtZ5tDOaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfb546460.mp4?token=s1GSMbdDW3jWPGfb7GYb2AVsTZsAj196FqCk1_TrIg4AGiyhb8DLGsxH09Zx1rDXRLPtApPEG6O8TziHE8X_AdzZH1cByhRjT84TzMK4pVv6EML97wrfHrJurqAETpWuRGd9Jw87HwAm5scoISBKLiY6usGvzWEzZ4Qk2nhNzsAP0VTeLThavKTU2We0lYpTQXwMYbmwnAaJ0DCAYs4mDWTxDWOFtg7zdc4wt3-nOSaRtQt2U5IzQ8U3NFrAaI13nPCqDD5Rrxd8BUihVATRlrOEJ1ktw0aSvCC3o8pLcwXCTvnWK8rl19_ThfR3tVPBoTveUNw_cLKtxAtZ5tDOaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع پیکر سرهنگ شهید یونس حاج‌عزیزی در تویسرکان
🔹
خلبان حاج‌عزیزی، شامگاه هشتم مرداد در جریان حملۀ دشمن آمریکایی به کرمانشاه به  شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453887" target="_blank">📅 19:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453886">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2e72ce2a.mp4?token=iwXevjXQ6FnCp-x_WEgUT5cAhxNd_l_YN5PcwXoRAaJuKrjKFu_PZoh1W4amX1AKqe5QnENzM7FgXm22Nc49jf5aJh847qnMuEZ_ctLKlTBDCNme2AtG3G2CgvVGzI9YTk4pp7j6eOiUoDrGbgGoYOO25rdl5wbLQJirWR1Y2VZpaOIc8K1hDbYgZnT3rk4Tu1emFLWexreYUTgtSSehv_ThXgP_RrkM1QsWao7wXeAWP3DH5ZJnBx8vM6XB_2kyacZpKctGFwxvxRomiA4Bu5RXvdDL31d0y4RVkz2dSv68KEmfkaM6ZuaKaV_0gyGPXSfxKstYPtI6IX7NfW7fYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2e72ce2a.mp4?token=iwXevjXQ6FnCp-x_WEgUT5cAhxNd_l_YN5PcwXoRAaJuKrjKFu_PZoh1W4amX1AKqe5QnENzM7FgXm22Nc49jf5aJh847qnMuEZ_ctLKlTBDCNme2AtG3G2CgvVGzI9YTk4pp7j6eOiUoDrGbgGoYOO25rdl5wbLQJirWR1Y2VZpaOIc8K1hDbYgZnT3rk4Tu1emFLWexreYUTgtSSehv_ThXgP_RrkM1QsWao7wXeAWP3DH5ZJnBx8vM6XB_2kyacZpKctGFwxvxRomiA4Bu5RXvdDL31d0y4RVkz2dSv68KEmfkaM6ZuaKaV_0gyGPXSfxKstYPtI6IX7NfW7fYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد در مرز مهران، ۳ روز مانده به اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/453886" target="_blank">📅 19:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453885">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiYeFz51KGCkUi5XJG6qJrl382T3tqiKPZXTOBVOsQW0qQRfy0g2DO5OHjqkm92Xf5ve5tCqvTTN9wIX66crqjqyzHNvB4yjjjWY3SQBsYJrn10jqmtdumAjM3uVeEnQhlQIfluEGl8wRaslEmPUs27IN3cvA8CvTunVk846GZNKj_IJ9aRcnwUa7ihMY8Nz37Bf1kCqFgOBqcj7Wto0bZodDQ0aJBoNNIcS6chANlAs6tp_r2cl9lLvBbODBAWPzmNMSX9AaNfMYZr8K96OIweM6DKrg6f4tL1JC6H8LohHdKjtZ8pRUnvkzXoPaysZzWphYNtyDEBeJ4PdPzZ38g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لغو واگذاری ۹۵ درصد سهام هفت‌تپه از طریق بورس
🔹
در پی دستور وزیر امور اقتصادی و دارایی و مصوبه هیئت واگذاری، واگذاری ۹۵ درصد سهام شرکت کشت و صنعت هفت‌تپه از طریق بورس لغو شد.
🔹
نماینده مردم شوش و کرخه: اجازه ندادیم تا پیش از تعیین تکلیف شفاف و قانونی مالکیت هفت‌تپه حقوق کارگران نادیده گرفته شود.
🔹
بر اساس تصمیم اتخاذشده، سهام شرکت کشت و صنعت هفت‌تپه به بانک‌های ملی و صادرات واگذار شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/453885" target="_blank">📅 19:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453884">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فوت ۲ کارگر در معدن مس محلات
🔹
فرماندار محلات: دو کارگر در معدن مس محمدآباد شهرستان محلات در اثر حادثه فوت کردند.
🔸
طی هفته‌های گذشته نیز یک نفر در اثر ترکیدگی لاستیک کامیون معدن (دامپتراک) در همین معدن فوت کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453884" target="_blank">📅 19:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453883">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/588f00e937.mp4?token=QBSCstsknbtNykzFlDecpuG3daTM4QfcmrTbPgDH1LOEhOwaaGA85MeBddKh5Fq18KWyQD3nCGHr1ZJI71NESsEpT_wZXNClu4rTxIGZk6NcZQrzQA9SzyRYqHJh9S3TxaAWulZEHx2ZeE2QD3fxANmTc9tbCV2CThbnjSKu2KBeMSqOqz4Qgxrbjv2JvEMWoVHi4JXubklOrsGjtxBe0L-Ng90WhDkVfIN2dYlvkGwuw_E0Rq8nModnyu-vfU5p9aJk0m-JelXpzP0HHHQYWO_IMsGbcG9tLWWLwcOeobf5lcQm3qYOrXFBg-d3HmBGuI2XZDssdGbtVCtUNBLxQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/588f00e937.mp4?token=QBSCstsknbtNykzFlDecpuG3daTM4QfcmrTbPgDH1LOEhOwaaGA85MeBddKh5Fq18KWyQD3nCGHr1ZJI71NESsEpT_wZXNClu4rTxIGZk6NcZQrzQA9SzyRYqHJh9S3TxaAWulZEHx2ZeE2QD3fxANmTc9tbCV2CThbnjSKu2KBeMSqOqz4Qgxrbjv2JvEMWoVHi4JXubklOrsGjtxBe0L-Ng90WhDkVfIN2dYlvkGwuw_E0Rq8nModnyu-vfU5p9aJk0m-JelXpzP0HHHQYWO_IMsGbcG9tLWWLwcOeobf5lcQm3qYOrXFBg-d3HmBGuI2XZDssdGbtVCtUNBLxQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پلیس گذرنامه عراق به صاحب این عکس افتخار می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453883" target="_blank">📅 19:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453882">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoXgWRVWcZ8f-kUfONiOBeq7KvTjYjnmQ7LyxnHBNJj218twfN8r2DpOS9DRWUbz_rkf1ekdXVPKEVLYrLyceKGb_j3GlmBd7ARehYPbogDu0fNiYGyNN9S1BUZ6epmg5FLr2HepQoaZ-SBGaBFEzqiw2SyTjyRv7p0IA-xWwGNIZgiFWwC9uHpXNsVu5ZJu4rxVMKUadJJlzenpAMTDRVNWdo7AKmDSyQHnvzUoY-nnskndbVWhtqMe7bGBDBd1DV9Ock7Reyp1gMYyIEtDk2z03AtxAWyoYykumB5Bx4kqdJznRX7Ud437zVJiKLQ8noZlFVVQF-vwUJLAYqG27A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ مدال رنگارنگ کشتی‌گیران نوجوان ایران در رقابت‌های جهانی
🔹
در پایان رقابت‌های رده‌بندی و فینال ۵ وزن اول کشتی آزاد نوجوانان قهرمانی جهان در شهر باکو، امیرعلی فراستی به مدال طلا دست یافت،  امیرحسین اسمعلی نقره گرفت و آرمان الهی و سام ارشد صاحب مدال برنز شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/453882" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453881">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e6e2dece.mp4?token=ZULemshEbKh9mZCWfeZ9ehcCtKI5XafrnuRYPpD12HZ79znjig-x1adXgT8RPPKDCflDsgiD1yMesWOhJTiGSAjIbWuhyAzYqnGAc4fBwr1-MEiZRgY6pXCLob21DJe17s5IdVCsU-N1RzNT616cW0-HLORfu8DkD3wxJQPCXA4k0oSTEMZeq6GJfYqNrXBQ3HDAYLLPark3WEicYZnKb2ev4EJvRcykw9aFzrPPAGlpFNyCmsQpCWIodTBglLgEkzmWjBzNwg4mjqLO9T6Wc1VsMUAkjwXvMooOlFlBM9TxRXlJ8i7CRCkWWAxAKJ33R1_1MqYBLOjzkhX4x6AJMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e6e2dece.mp4?token=ZULemshEbKh9mZCWfeZ9ehcCtKI5XafrnuRYPpD12HZ79znjig-x1adXgT8RPPKDCflDsgiD1yMesWOhJTiGSAjIbWuhyAzYqnGAc4fBwr1-MEiZRgY6pXCLob21DJe17s5IdVCsU-N1RzNT616cW0-HLORfu8DkD3wxJQPCXA4k0oSTEMZeq6GJfYqNrXBQ3HDAYLLPark3WEicYZnKb2ev4EJvRcykw9aFzrPPAGlpFNyCmsQpCWIodTBglLgEkzmWjBzNwg4mjqLO9T6Wc1VsMUAkjwXvMooOlFlBM9TxRXlJ8i7CRCkWWAxAKJ33R1_1MqYBLOjzkhX4x6AJMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق و بلندشدن ستون دود از پایگاه‌های تجزیه‌طلبان خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453881" target="_blank">📅 18:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453880">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEKq1mwTgM4MWKd3ufu9Mh9thzrbwUSr6StGdyzgNJN9yLpwp6wyjSNypa5FiyNFIBOoS3wuQ2ssZgp4QLheZzj7kQ93ENsyqVe_knNopmKloyjCteS9_zZ9YLuEhoSQt6JW8hYzK2w9Zt13fri9mZ27NVJcricCtW6NEjgqcQBr6qzZmvzXIc7e3rN2Igl8EmCWr3HIvFVHkJ-gGVaO6J3cTi94IGxT1NUA_ZhXHL4G7xv29vbqwXK1apsJD6t23jADO3vv0BVARUuwOL_hriDYRdNfvvYvW3LpzHMoIR_3msojQYjQqcByVblKKSxcHjxRuqF_INWAG7Zs-fu0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پیام عراقی‌ها برای زائران ایرانی
🔸
آسمان‌مان برای موشکهایتان و زمین‌مان برای زائرانتان
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/453880" target="_blank">📅 18:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453879">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C52tB3GQuspeq2oAuzOsCNJzcTSiiz-SKhiqQ-NNglT5cmJIxZT4M9OqNGf5bz8e6EUkxDMUkbNPzjVLsxgXP1Ox5EtsRx_nbFSO5c_zGA4oTxeS9H6TuF4983EsnOd4u1A3QqyXm0p5-Dw9wd6efB2qLZ-SXWLH08VjB5iwPFMwOTEdaOffQuruHmAdiMqvF8XUjULSOGOl6LH_fMFkqAdVtPOMp_csQ7aYXM7G8HTSBivnYR8M9Acwrhmw7lUd1hR2xNZIgSYZYETbYnGcxRO6-HFu2lQ_9uoK0gj5XQqtonOH200qi9mxz3brObUqpIm7vIf6m-ZqmRX9AwGzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: زیرساخت‌های ایران خط قرمز است
🔹
محمد مخبر در واکنش به تهدیدهای ترامپ علیه ملت ایران: شما با معادلات نظامی محاسبه می‌کنید، اما ما با منطق تاریخ پاسخ می‌دهیم.
🔹
تعرض به زیرساخت‌های ایران، مستقیماً گسل‌هایی را بیدار می‌کند که ۲۵۰ سال معماری هژمونی شما روی آن‌ها بنا شده است.
🔹
وقتی ستون‌های این سیستم فروبریزد، دیگر نه مرکزی برای فرماندهی می‌ماند و نه بازاری برای غارت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/453879" target="_blank">📅 18:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453878">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9XvfwL22vyT2slWsu8IThx7G9J2beieTxKadzuXvCYEonDObCc2Jgq4HAg8ZoOFU11aoYD6Vgd7r6kXv8Q4lZ3X5eQs2Mwy0aL59clabxQNfl3Gds9-bputwEvBtqL1kyFFHNG47Sr_XdycHlzxNawj90A-9Lj_ihwvEZDZ6vj1cwNBLnP0M6MZW3vDXDYii3VDUCgvG9IfN2qZjHKkSlYRaqpRNDIHuIkcLTm_g427YEMVef_YpuStcvQc_lDxbvqmGFHtqGkPq6WPSFnsywn8DaYnPTMaV6aakah_2lZcfbkJAUFmGrC76k1gROTFA7l66GN7KpCgAw_icsWazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای جدید از آتش‌سوزی پالایشگاه جازان عربستان
🔹
ستون‌های دود در این پالایشگاه پس‌از گذشت ۳ روز از حملات یمن همچنان بالا می‌رود. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/453878" target="_blank">📅 18:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453877">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRn97nUncvSg1eqAvkL68sKJaeie9YOUJaUDGPHu7OJ3anNx2QxoghOmGEN2YVJTU8qOIG_V0gTUF2HnWI8qr0bBiH71InSxAVuk_TWz4RgewFcBXm4eWJysK7GLOWQ_jTVNQFtC1jTlpey-9niRbTyVPYKVGQVk9_unQxZl0nvbfB_vrVKzqG-A6IRrOgxEbHjwfyDz9-efBnx1P6u6-aXJRBZGEHeP1hx5y7VJ4I6czWa-GEpCtb6OnLL1WrgCRbla-UhWAxLAAb6dQqwbt-eJmvgAItomTc-h31PoRs_EjgfZlL9PfM2RQsyIl_71fZmn-_igF6E-nvjulKuzKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایپا قیمت پراید وانت را بالا برد
🔹
سایپا قیمت کارخانه‌ای وانت ۱۵۱ ارتقایافته را افزایش داد. قیمت پایۀ این خودرو بسته به تیپ، به حدود ۷۶۳ تا ۷۷۵ میلیون تومان رسیده است.
🔹
این قیمت‌ها نهایی نیست و هزینه‌هایی مانند مالیات و بیمه به آن اضافه می‌شود.
🔹
خریدارانی که تسویۀ کامل کرده‌اند یا تاریخ تحویل خودروی‌شان گذشته، مشمول این افزایش قیمت نخواهند شد.
🔹
سایپا اعلام کرده از محل این افزایش قیمت، حدود ۶ هزار و ۶۰۵ میلیارد تومان درآمد جدید کسب خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/453877" target="_blank">📅 18:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453876">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d52c5baf.mp4?token=hk81UDew1Tsvo_SL-oO61wwS2mSsjahPBCEC73MW5bd35fXWTJfVFrmtmsJlZSmQ-gNBjGDX94FiQ1EI5hfW-zLBH1fl7NNpfxxfSiz32rF5DsFTUzoBPirSE2cFpZKpTLSG7u75TT6txS4eFyEAZw4GTxDnAtGmpFW_ykzQJzVBwJgj6q7JfyhtfZByp8yLHfoF7gNzULWS_04m5oSYBEwQ2IotHuVYG6_UzhVW3yv-7Jw8okHiAU48z5Ev5_PvXLZMq3avSDjRRyfM40B5NTq-Ku1ph0WiNJv0eeOWG6adZzDY2LbF8Kz_3VC47fHMfj6154gmpwq5Ilj1ia9fZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d52c5baf.mp4?token=hk81UDew1Tsvo_SL-oO61wwS2mSsjahPBCEC73MW5bd35fXWTJfVFrmtmsJlZSmQ-gNBjGDX94FiQ1EI5hfW-zLBH1fl7NNpfxxfSiz32rF5DsFTUzoBPirSE2cFpZKpTLSG7u75TT6txS4eFyEAZw4GTxDnAtGmpFW_ykzQJzVBwJgj6q7JfyhtfZByp8yLHfoF7gNzULWS_04m5oSYBEwQ2IotHuVYG6_UzhVW3yv-7Jw8okHiAU48z5Ev5_PvXLZMq3avSDjRRyfM40B5NTq-Ku1ph0WiNJv0eeOWG6adZzDY2LbF8Kz_3VC47fHMfj6154gmpwq5Ilj1ia9fZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شهادت جنین ۶ ماهه در حمله به مدرسه میناب در برنامه پرچمدار
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/453876" target="_blank">📅 18:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453875">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق و بلندشدن ستون دود از پایگاه‌های تجزیه‌طلبان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/453875" target="_blank">📅 18:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">آخرین تیر ترکش فدراسیون برای احیای سهمیه چادرملو
سخنگوی فدراسیون فوتبال:
💬
مقرر شد هیئتی متشکل از فدراسیون فوتبال و باشگاه چادرملو راهی مقر کنفدراسیون فوتبال آسیا شوند تا به‌صورت میدانی مواردی را که با AFC مکاتبه شده با مقامات کنفدراسیون فوتبال آسیا در میان بگذارند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/453874" target="_blank">📅 17:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJfZLEfkpa5C9qBBmPL9U9rWVU72ttYYKCfp30Yd1YjK7J39Y856RdlqNaMHTuLndZ-12d2YhF42UZ2oydz7pEnE04BH8uBX5LlCF5TPyDcjjWrUyW9m2ZoV2WsnfpXEvpBXQ8xm-cdQijFyiJ4iET-3dPvqhtTHqHPHc-BXjxyKxIc0VN1l8SCqxkuL7OzHwQ3_FyrsmKB_pm7JcAXKDhKwhfCSmKssMA9FRjKKa70SD69FMFxp8BJH87_xseN7kWLzXkYlriZgZeVw8MPxvS5Kc9hpUDrHE_uJnVLuWpRvFEPZ20bc6sIWHOkcMMYk5T2R7ZWrd5-jzpOb9q7DYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
یادمان شهدای مدرسۀ میناب در شارع‌الرسول نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/453873" target="_blank">📅 17:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psWBDzClH7FLIodlfyo_Rk09bI3huGVMjdOkXI6edy-0BXXW84BvM923ynoTN6LbjO4FY6tMu_7p-Cvjjg4u9VF5haYuIY3gZ2o3NkQtrQfawv1cW7vB42V3NOAH73TXrS7J9OzHegEkIQS0X_inT7BWlMnaBUy-p06NZVhLho8kXizGOL-O1Vbs5QOTZaAHA25OT781cIMQLKa263CC0z91QV7fV7eReXUc1VwXZEhLOjzRZoLUuzJeQYfszSRSDG6d-5mXvxTGbhL57gcof2YIDZw7rmzc_gwlZPK-KOaZGBZYYp0SHYPqTbdTvGvBlO7oGyuGWPtgzGN-eKX9NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تداوم اقدامات حمایتی بانک صادرات ایران همزمان با پایداری سامانه‌ها/ جریمه اقساط تسهیلات در دوره اختلال حذف شد
🔹
بانک صادرات ایران با هدف جلب رضایت مشتریان تسهیلاتی و دارندگان کارت‌های اعتباری، جریمه تاخیر در پرداخت اقساط مربوط به دوره ناپایداری سامانه‌ها را حذف کرد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/453872" target="_blank">📅 17:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0x1YisiHeXjSgYcuF_-SG_vl89l8JpzMDYLr0RU7T3jbc-cqAmdaLCQugDSjJTXVnfrNpXxSbqmoD_brzV7ZrF_cZA5i7uBbgUi7JSnDcUlRajY3y3gmnDElz45mRFP7u-8orQCseVaRZvSPI3UPDhQe04zVPT9EIo3PpcK0j9Bp6y8MyzWoDGapTQmssCqhhr69Fzvrfq1lAMu36Feb-gIuDVPVUeQWX0l3-JewbjZtr9pEH6oU9TshUd3fIyexDYzfUiKrsGt2WhPdsGm_o7Aq5TZ8I0YL1Ygc5f9HytQ49CUYtGyCaJc9mnlvhxeGev_11zuqKOD5SZoh5iWzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح امداد جاده‌ای کرمان موتور ویژه اربعین ۱۴۰۵
امداد جاده‌ای کرمان موتور ویژه اربعین ۱۴۰۵ از سه‌شنبه ۶ مرداد تا چهارشنبه ۱۴ مرداد اجرا می‌شود.
در این طرح، خودروهای امدادی کرمان موتور در مسیرهای پرتردد و منتهی به مرزهای غربی کشور مستقر هستند تا خدمات امدادی را با سرعت و سهولت بیشتری به مشتریان ارائه دهند.
شماره تماس و سایت امداد کرمان موتور:
٠٢١-۴٢٧٢۴
emdad.kermanmotor.com</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/453871" target="_blank">📅 17:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/453870" target="_blank">📅 17:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMzUfRn8q7MpC1MlQcnx6s6nPMjMjRDLbn8WSC6K6f5mAZ7CdI2nuYyHCUtNR-AcY4BuheGbppgM08zDDBsZj3B6CLfJOaDGG1EdFS14LWI5GjYiQfDVtlvMQIeG-ltRvMAtch38sJW4rwuciwHblE3Wd4KnhiQDlEHylDVKCpWIwWa-dyktSjfKEkDWfF-pZZb9feG29OBAMdjCoYpk5h0tKvOM_S8sJ-VnGh1AHI5ChEe3JgVtKcEwxEQ1njCtN0hNssU3BrpSh_6Sf45qgcXRV-Q4WxEHey1ks6RP4OLt-Iw_ojJ-Li2RcKY6b8bIAP8rVRIMAG2KIiuTrv2D6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از پیکر شهید ۲ سالۀ جنایت آمریکا در قشم
🔹
سینا جعفری به‌همراه پدر و مادرش بامداد امروز در حملۀ آمریکای جنایتکار به قشم آسمانی شدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/453869" target="_blank">📅 17:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgVar7OaIXpNfzmG-8XGFSnRqVmeOUw_g2ZNUQSORJlTZ1OYx0VaOilAdX4wt4heoALvq03EJSVSPLiW71mxQgNkMgVqjd0GbIbWj6ttR_ZbY1EyxpNM0wWn4i0agGbKV-CBHu-c3vf4qTxCtXHucJL60-sPN_4375sbROWYtiqr5FWQj6NCuTD7Lg89I1bx2D3OLNhk5r0VuHi4ScmJqJYCanol0ONS1u-EZUIzRIvIFniWT3CvQx1pexVVBQJdy3k4gCaK0j5dDWFePEPQG0hdrKrnVpyyNUO_0az4L8Ejdq768AuyUpiuF3BFbnGffZ5Z9L82kAtMIp9-MkzImA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثۀ دریایی در دریای عمان
🔹
مرکز عملیات تجارت دریایی انگلیس: در پی اصابت یک پرتابه به یک نفتکش در نزدیکی سواحل عمان، موتورخانه این شناور دچار آسیب شد و کنترل خود را از دست داد.  @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/453868" target="_blank">📅 17:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_QBrYMojyc7NPizgDJ0hhjO78nXo5BpPsCktW72t0RjWrqLb2nLTEjaps4iWaP5cNUi-cn9-W4qhysgRtsHYWjNALAY9BV3A1DbylB254FmU9lWZXDU3SV6HeZT9HNNTn_iK7QW0uj9xpgmbTA2nru63LjcDIp3fmFgV2oj-au56vI9X-AKHTz6MJqgIFMIQDRlTXs_m6mdZOIx-FhDgHhtdN-cHSBxeDIlrvuSmjDCMkReZwhbBEEPMXe10ZHGrxXVgOq8XCUb8fbkwQ-X1thPgJyns4FT5-lQ_SXkMJLc5RNx64JT5Re6yxpuWD86s6kv82Yz0W1zlL9NoXGyPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: آیندهٔ ایران را مردم رقم خواهند زد.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/453867" target="_blank">📅 16:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e45f1261a.mp4?token=qy3mZwX8ljDesOMXeci-GZ1x4X-wCJ283EQ9UrcmHs9bu-RmD6k_0j66w7SqESDZR-XPplKSki64I5jwRhnJZova4FmosW1Am25fKoSCu7Jy2eWOrpq1NMiVDYMwBo5FjmwZ1KsGNJbGs2ihUncLz01Tlg-95RsJqKlx0UQ3q7tiz4eGYYhqWh0YhFatnr91VhX5q5EoFvMA_p63_fw3fCdWPBbQ9oRTuSzlKkTpSzP2RoESOcaZjzoCHjW0oDOFv4w82xVUrC-MsMO5TV_GJwFjK5-NIovqcYLXwKUR4EcOg3u4HycK6gzlZEL35b2_kwuYLBqOFAdIHll03ZLtsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e45f1261a.mp4?token=qy3mZwX8ljDesOMXeci-GZ1x4X-wCJ283EQ9UrcmHs9bu-RmD6k_0j66w7SqESDZR-XPplKSki64I5jwRhnJZova4FmosW1Am25fKoSCu7Jy2eWOrpq1NMiVDYMwBo5FjmwZ1KsGNJbGs2ihUncLz01Tlg-95RsJqKlx0UQ3q7tiz4eGYYhqWh0YhFatnr91VhX5q5EoFvMA_p63_fw3fCdWPBbQ9oRTuSzlKkTpSzP2RoESOcaZjzoCHjW0oDOFv4w82xVUrC-MsMO5TV_GJwFjK5-NIovqcYLXwKUR4EcOg3u4HycK6gzlZEL35b2_kwuYLBqOFAdIHll03ZLtsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شاهنامه‌خوانی مهدیس، شهید ۷ ساله مدرسه میناب  @Farsna - Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/453866" target="_blank">📅 16:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453856">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQ9gVVmTQBt5pHVr6QNAG-zWKLdrakYTVr3WB5ZodJA5EzhbXHaOaH0omSjHM0qjWrTHkoDoM2-EOrkY4oIhLFVn_mNLKDEebKm8RQx_QdREwC_jlecHQIvhfYTFEKpUsdXvv08d3e5Pz32lu5E-6Si-9GJMyRbYjK3SLhD4RMb4wocJ-S2BCbB_Bve-G7CnstbRScvep7IxV5_dVdU2I-6VbQh76RORtOEA6WTh7yakFf3WzJLuPDSzK-G-FgQReds13wcP9p6kGe5i-XFQnuA4ypDR0mA_KwU-EnX2UFSuqxvf4QrMvbcm1uVADoMH3dVRPrNqGHAGxB-DpKPZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZpvWrh3dQPhtXW-lPHMoNMj0EAZ5Wmyg7d9NOpjZGIOdLBW3czaxzqdg7vwD-8a2aO2q1MCIVx-GFEMewJQlxDjvQ1uMrxom9o7mPKKsDkb_wmgK10Ut9PPlQ2y3tgcoNbhp0e85GM-3Z1shjzBFOn6i7GdVm_fv7c9Nb_jLtfFbKHRIjQdrL2DlCweBxo-Cb-ep3Bz7mMnikwNtCCRFY7zDJ9X4IofNXnULpGcx2loIceR2iUHpigKifCjG_lHqY9tVYkCXMKN0kHgXHq_h9qz64oT46lFyHIV8QDQh5mbDIuoZuyOdrR7T-i6txTiX_B3xu8PvNb4L9jq8o4TNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENrXQ9AssSWxJb0XWYD1QDwBEfLw84MsulMm3Y87_HtFqvkXjByeuy1jaFX7kMMGCsFEo8VcWmfHqnlUBh8-Qh-fVERsSHtGoOTsYyuCVtCzr5PjpW58apCz2350U_xgreh52w7pM8WQ-hzYdHDoy83v-dwsCxUwkq_nT5vLws4fzwMu-OGZvShXQN2e_9EK96EeMRKgjnLCx8zdKCHVI0BUESgQzW5uSNDea-swXnGPUTDJGDNidRPH6JxUeRLB4XbGe0AYNIBixXmPwu5q6JeeyVWYhYPLMjiZwFHC_r-K_mOG3TFcU-jYbd9sfBpqiP6YyjPVgtZCTa_rKW6IbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tgKCAo_wKLbs8XMvgm8w9vqOKHBJhP03XpyeCIZ-Zuqwy4pRwiXIxVvNAGR6cGtiSalQ7hlE-BgVNOi79NdCo2ETjCx7WgeOLD_t0BxrNSLcx6e2GjFdXB0L12I1Z4oHOPsh9CmwRegvTiVB-cTEEAoK6Hqsv2vLN9KTF6pFKp59fC1NgEBBnLRm9d7mfa3djR3dDyQfOhR9U0nEJZIv3K2-mBuNNr6lnj4yyFWZ2QmjuyLqc3i6rHxh_PXSfczsYC3XmbEivvNVNWVKs-XJleJHJU9wjlj5aXHYPavtl44biu4DyLtlRseGr_lciPIHlP_krv-iVb1Yu0Oc6kgK4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTnPy0bGfONjpOh8l0m5uPB0xEvoGtz2Tnz-PPK0SSXmB3Qr_0-i-wK9ePbsRvzn00lfKpMr0I8mmPgzDAdK0_9tCvNEyhDr3b4W_pqKB4YrnNU5fqVnfIhhJfwCfaguh1kKmNmxaoQCr-b1ULBz1nVtzVyV7ZmEzO7IsluzQKfhmYzHMZEBRaykaHfAlxqvo2zd4jhbooCkN79bDtHbQrsS6XSS98PLvNT5eCfZ_icEhkjrDn3JUkAXnwjEokf9gsG1w_10QPqJErwZUSIMpwKa29NgPDjR2XQe8KscvE-PknKqorI1KTtJNjAEOdhsHBOWocoohAAQoR_VIhud1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qd5wU95xySPbZ0Y0h-NEOm0-S1eGFqPEI1aPy4qcfQPYJqU8m9uQ-2I2PV_UJA9-kFth2dbY2_tHPGZ60Vy9WbpsLzHLL4vfPJdxAKUFuq_6alAYIW2smbRCjxZADl-P9Z-DqEoaG6Dhz3ANNsHAK7MXBGwWWKwHgPFlX2bxJ9oHzXYTaTT3-nkzSNYAJdhv8ABn-Bl1WN6m7P9piOrTWQrKrO0X30Ye4g3tl2_ydIexr07u2sFzIGFSjjYbOiUOg36XbooxJ8OAbQMqmOsPd2jZCqdQ79Fbb-t30QbBFZS_mAWXN1DiS6RlT08G1dFGmrFV9RhNPdv4T4tCbhmEQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rG0Z0cf1xCAxoQnYfyeAwYCAP8sCTP9jFc9Djs86fPxJXczK4CjanQOoJY1_hXL1bGnZrqCTbd9heVjB4qW1x2hJsC5xgrtikg9qM8SnkxotU_3tl1tHthdP_5KwsgpBeTy1rfbaDWh-C0u976qCSnECCiFQEM__SSA3-CBjLGMlf8A5rb-VI90i4E7sHY2UgdKBAbpAcMoNT-LJLJZ9WoxSMYGUDWAud9JTi4i4O9Cjnf7Z1GfAmBNdDxVFOwiEXI02bur7wMMwiufAIirJMSaDZCMMoFrhV6OfhvyFyBmKzHJVE0qPkGiQslhwJGLvqFB8tzkb7OAEIvJ-09NvWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RN7xKOH2BlONSWYEBvkzVS1HmhFg0OXW0xo4ZX4eUquP6MdzYTqekSQwIYZPLa6n9nPE9fLsiXostSZzlqLnJbj4CAOE3nT3U0LRHVsfb5CCrrx9AJJe3fOwDin-tFiDprjO8GDSYAHrNt3nDyRBGU5_UwJboiFQM1fOOCR81BtFp6Lc9sgCMrrDSbUeas_597phcldTOz4Udd2121klYXvX8FNZa2lA8-76F2uDHLzli9Z72BOF2a6VSMvDKmauFE7o_Qd0TXfYDLam86U5W-nXD5j3epIVLoRMaXf6j2ADbRFxZPc8nPib2YdQ_pGVPrWHxczSq6VoM7XuW-cY_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHPWy6EbyXIP0gck0EtbkoTA9kHOaoukwRT3AEmgfEE_QndEDccjRrOaIoc3M4YZ-bvnw-DSiNB94KQhk2DkP8Oz2wR3f3E76iGv5xa4OAqCz9u3tF6jTtJJLTWJ0Wc4lC2ycfZJter1ltxpCL-tkOClWOSNuLvZzBkK74DYm2rP8qQCXMocSQXNMbTasaeeLUl40iWveAKzaW_60_lGaqlBZ_OSZolh9nKlW-LJf3Gam1NTD7SMDeyjY4gmSvyWgsfXKGO6-N8Oz4y23Z__wh6fvqU8blu0hb0ieCAc-fLXkaFdqG3HxrYUQ4I014ecrefF1gtYmB_UySVBYbCYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTCC1QFSS2BW4aXs3eY5EmBk4xS6kC_yxpKK_dBQvDfZWzxhUJo_ZP3edF7BcjHPPoAVR53dFEByyD5Tjzci6XL6AUKp4irGcULBPUHr6TtWztOoI6pSjqcwHJuO_qWkUNiWvmvqd6XFVMe-2Tbdox315ApQZ8i_0CLducXoDQW0wqUbievqtpDsN-GsLYATK_23U9AL6Yc4jMI8mELfIwQ2Z9mcje04VkjDGpHFH6s_QLqFKRbaPR9xg7VfLljdaX49b-eR60LOh50cuy9F31CBLTBOcSMYZbk6P-FjdqcXyAEdBPTT3vobJFWg6lFTJyCu4uZUhSnxKg8Ssnl3dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
راهپیمایی زائران اربعین به یاد آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453856" target="_blank">📅 16:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453855">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42e469cb3.mp4?token=XGk-76qQVZZss42U6_goZ6mKGHxDXiWIVYDLxr64DzqhyBEYaqPvLis_JoKb6A3ld-IkPnjyzurcztWYERxY-HHc8yCDNNgytXglJ7jKLGHjnNG0oRdvXYjFv1WPILj9CDSh84X_YNm8W_euXr9bpqjXYTMFbSreXX_4drMxAgMKC0V4Hk6NeCWL6aqOtHN-ORahk2WCdWL6vyjgUiNO-6uqYrnAMHJtyu8wMCL1xVTrYK0OtICIPYUUh3JfBvmWc4JpLz3eAxZ5Ur1-0cjWAcBF4PjgCg8wC-o2Ng4lddubb94vNQM8E0ieRTIzvda-sukqjxH9UuT9DdsWlypSmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42e469cb3.mp4?token=XGk-76qQVZZss42U6_goZ6mKGHxDXiWIVYDLxr64DzqhyBEYaqPvLis_JoKb6A3ld-IkPnjyzurcztWYERxY-HHc8yCDNNgytXglJ7jKLGHjnNG0oRdvXYjFv1WPILj9CDSh84X_YNm8W_euXr9bpqjXYTMFbSreXX_4drMxAgMKC0V4Hk6NeCWL6aqOtHN-ORahk2WCdWL6vyjgUiNO-6uqYrnAMHJtyu8wMCL1xVTrYK0OtICIPYUUh3JfBvmWc4JpLz3eAxZ5Ur1-0cjWAcBF4PjgCg8wC-o2Ng4lddubb94vNQM8E0ieRTIzvda-sukqjxH9UuT9DdsWlypSmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصویری از پیکر شهید ۲ سالۀ جنایت آمریکا در قشم
🔹
سینا جعفری به‌همراه پدر و مادرش بامداد امروز در حملۀ آمریکای جنایتکار به قشم آسمانی شدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/453855" target="_blank">📅 16:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453854">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_zCU1KjWjG1dl4ER7KnDbTk_ePtXEbTTlcDT0Bo4Bdboy1B8z_5DNo_y3Vg9RDREp-dv5qTHyqwJu1JwLSsgF0My69eLvrZBUR5oG_ctvZutb-tcjKEAF5LqbOeWPDcdOK7P6aHqhcC61d2Ezge9S1nzSQ03fEJ4TCGhSq57wrjArc-r-sgn0gas3TnyroZ0PmwYqphf4hNfgqxcp70Pyudzz_KIxPmnTotchilS6Np46ZxF-hcxgliObPWWQ8J_UiYHR8nJbBUnidR7DU_utXqORKgU3Y1tgApyCOUvvfI8fcvo7NyIQoXuJDukUxMjE95eAeS4Ar7IyekybEqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
تأکید مدیرعامل ایرانسل بر تبدیل مدل‌های سنتی به شراکت راهبردی با تأمین‌کنندگان
🔸
همایش «تقویت شراکت راهبردی با تأمین‌کنندگان ایرانسل برای خلق ارزش مشترک»، هشتم مرداد، با هدف تحکیم ارتباط با تأمین‌کنندگان داخلی، تأکید بر تقویت تولید داخل، گفت‌وگو و شنیدن بی‌واسطه دغدغه‌های شرکت‌های همکار، با حضور مدیرعامل، معاونان، مدیران ارشد و جمعی از مدیران شرکت‌های پیمانکار و تأمین‌کنندگان ایرانسل، در مرکز همایش‌های ساختمان مرکزی ایرانسل برگزار شد.
🔸
مدیرعامل ایرانسل در این رویداد، بر تغییر نگاه از رابطه سنتی کارفرما و پیمانکار به شراکت راهبردی تأکید کرد و گفت همکاری باید برای هر دو طرف ارزش‌آفرین، حرفه‌ای و سودآور باشد تا به توسعه پایدار و ارتقای کیفیت خدمات منجر شود.
🔸
سلیمانیان اعتمادسازی، تسریع در اجرای پروژه‌ها و شفافیت در تعامل با تأمین‌کنندگان را از اولویت‌های ایرانسل برشمرد و با اشاره به شرایط اقتصادی و افزایش هزینه‌های صنعت ارتباطات، بر اصلاح فرایندها، کاهش بروکراسی و تقویت ظرفیت سرمایه‌گذاری برای توسعه زیرساخت‌های ارتباطی تأکید کرد.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453854" target="_blank">📅 16:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453853">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c664582a4d.mp4?token=aq07bcKvRT_PScSIpwPlLDvAbbdAfzfY3UaRi2hYznok7fXuFgWppyW6TgGoFpfHNckG9dcj4iEehvMLqoxm1tzqZgNxoiWi6WDFsSaZMzoWUkYsY47X8fx7eMb9YzuLC5S6Pvp3MOpPQNXM35A2TRbUCCzuzK7IH9PISM07SvaIN049rmGyZV7SFtyhPY3G3fQd257b-5wtM-mMNr3yYZ0zWig0OkmqiuJDNd5sr30MjRdRNrN4I-fam34uUpAneI63VgQ8oGAdalQj4VSZHt7FAzP_VBRExxNuPYkYLzjmRBbEhw0CL5v8ghOeMYDrxzlieUZfVZ19fbnFGu5QaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c664582a4d.mp4?token=aq07bcKvRT_PScSIpwPlLDvAbbdAfzfY3UaRi2hYznok7fXuFgWppyW6TgGoFpfHNckG9dcj4iEehvMLqoxm1tzqZgNxoiWi6WDFsSaZMzoWUkYsY47X8fx7eMb9YzuLC5S6Pvp3MOpPQNXM35A2TRbUCCzuzK7IH9PISM07SvaIN049rmGyZV7SFtyhPY3G3fQd257b-5wtM-mMNr3yYZ0zWig0OkmqiuJDNd5sr30MjRdRNrN4I-fam34uUpAneI63VgQ8oGAdalQj4VSZHt7FAzP_VBRExxNuPYkYLzjmRBbEhw0CL5v8ghOeMYDrxzlieUZfVZ19fbnFGu5QaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
#تماشاکنید
🔄
خدمات جامع چک در همراه بانک تجارت
✅
از رصد چک‌های وصولی و چک‌های صادره تا مشاهده زنجیره واگذاری چک‌ها،
همه چیز در اختیار شماست.
📱
همراه بانک تجارت، ابزاری کارآمد برای شفافیت و اطمینان در معاملات
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/453853" target="_blank">📅 16:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453852">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/453852" target="_blank">📅 16:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453851">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b36Q3JL8FExdDU2yXw0_GrRD9XsUuash4qJbuYjDTkg-wM--jKx5yJi-RnlbCj3dyW6sXzE8w7r439wnaxlyPFeMWrbbh1usmYpY4wOs-ZHof3rUbT2JUMN2IbYZrFfmVwv5ImdfnqixWN1w0cqVeEXziDtIcqcMkx-fFufz6k_IGCu_18U06gHHK4_aQqeXYYu1a-R8gxJnoe7h37DApR2X8ax7exH5-QzMVrtTnVlfQZfyiVqYB84pIu5Xoxe3s6dLR-SRL6S8-OQuE-SHGf503RgFDplrCNnp301jI5wCjumUlK3r3cr5qy4u_M6t7ynSwqDvtee7CczixrSD6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ نگرانی سناتور آمریکایی از جنگ با ایران
🔹
در نشست بررسی بودجۀ تکمیلی وزارت جنگ آمریکا، «جف مارکلی» سناتور دموکرات، در تشریح پیامدهای احتمالی جنگ با ایران، گفت: ایران می‌تواند علی‌رغم ادعای نابودی نیروی دریایی، تنگه هرمز را ببندد. ایران توانایی حمله به سراسر خاورمیانه را دارد.
🔹
او همچنین گفته: در صورت وقوع جنگ، مواضع تندروها تقویت و اصلاح‌طلبان تضعیف خواهند شد.
🔹
یکی از ایده‌های اصلی جریان اصلاحات، حل اختلافات با آمریکا از مسیر مذاکره و تنش‌زدایی است. اما در سال‌های اخیر، هر دو جنگ آمریکا علیه ایران، درحالی رخ داده که در دولت اصلاح‌طلب مذاکرات میان دو طرف در جریان بوده و حتی ایران در موضوع هسته‌ای نیز امتیازاتی را پذیرفته بود.
🔹
بنابراین، جنگ با نشان‌دادن ناکارآمدی ایدۀ محوری اصلاح‌طلبان، آن را تضعیف می‌کند.
🖼
اما چرا مقامات آمریکایی نگران تضعیف اصلاح‌طلبان شده‌اند؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453851" target="_blank">📅 16:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453850">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQxXSDIohrrq83Z501erWogaUrjKY7o2_fkjYMgIrzKmrRkGA5JcjuWgAXl5ojCNEEb5POL2HrEJJ4ViBNkT4loP5y4yxTTh6mxAyVS5yOV7untJ_zA1CwZ5Qk1AfGe1-ZXrN2hw1HJkTr6CA6NALteVajVPsVTih3EpoS9wPP3eAtXniQCk2kz04L0_DCipwT7nIKpXeFXEtVFnGVefCPLbA9AFblctCMIhIyQQj2GCLWS6053h7qHqkSIGJ7j2AAI2Z_yGOHv23N-ynbknQZCv14dg5JeCxDsyNX_-QIoSBn0T9RWMyuwwO8TJHALvUD968GVZoLp7dBqOiRkGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عارف: افزایش نرخ ارز به سرعت در قیمت کالاها اثر می‌گذارد، اما با کاهش نرخ ارز، قیمت‌ها متناسب با آن کاهش نمی‌یابد و این روند باید اصلاح شود.  @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453850" target="_blank">📅 15:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453849">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ab26368ef.mp4?token=LgxaCoaqrmYteQYWWc45Rb4UW_C9WPNPp5vhwW4EW6CC8hXbmWMWKLojm6dFxS6d56h3fsV49m08oJ5IuX18qkq_SjAdTCcBIcckfsys_Fw99wxXF4sLfb60bbbeZvS0FCSc-G2YwGouEL_BATGzH7LUuBd_phAzFBu23mmlvO70lvZVJlOK5EfJAaEeu8bOzwuqGi63VtRmgiI0xgL6Hc146WpwpFZuBZ-rdweXqGbpvo9jl9GPvGyp1KyT6db8cY5kcfQhyvxIDkPoC5Cjs8VWQmqZoJQIX4vHO16OU859RwB7MndQjBswXeVr0V_11IFe5ED-f1e7aqsVRYtRlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ab26368ef.mp4?token=LgxaCoaqrmYteQYWWc45Rb4UW_C9WPNPp5vhwW4EW6CC8hXbmWMWKLojm6dFxS6d56h3fsV49m08oJ5IuX18qkq_SjAdTCcBIcckfsys_Fw99wxXF4sLfb60bbbeZvS0FCSc-G2YwGouEL_BATGzH7LUuBd_phAzFBu23mmlvO70lvZVJlOK5EfJAaEeu8bOzwuqGi63VtRmgiI0xgL6Hc146WpwpFZuBZ-rdweXqGbpvo9jl9GPvGyp1KyT6db8cY5kcfQhyvxIDkPoC5Cjs8VWQmqZoJQIX4vHO16OU859RwB7MndQjBswXeVr0V_11IFe5ED-f1e7aqsVRYtRlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلب تپندۀ پتروشیمی‌ها کمتر از ۳ماه به مدار بازگشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453849" target="_blank">📅 15:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453848">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-WbKjE6CV84DTS2-Mmss_7-xUkQBsnILV6Pdhhcj98Gd0tf67mMvWhojV97K7_K7KnvkI5k9xIOsBSVQWofFf2dgZaUj6Bltms-HeWH1PrIwbTKjBwc8t8m1VrC3OkEFnalCC-yojRzv62myD5Q5TNMKwog06cO2OYlzJuoWyPeBYaNGUxR_gGOA2ci8wiriHK4kzbw2U9o1O7p-GdDUofsUvBMRiDVugsgFp5MNn17lLNlzjRHjv4wmkSln2pyLHt0axKUBWc02NLjpdLg6H9JijhYsqIWMBXPty45Q95rTs3gBov6tWEhJEPntHtI3QeRzx9zc2DHhBq-4yUFqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
زیارت اربعین جلوه‌ای از «حُبُّ‌ الحسین یَجمَعُنا»
🔸
تصویری از حضور رهبر معظم انقلاب در زیارت اربعین ۱۴۰۳
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453848" target="_blank">📅 15:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453847">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca485d3e1.mp4?token=oI50lj6-pl1GMs4-LhhPGXN9-FqvbX3tDpgqfr29_5q5zddo9Xzw-YdDp4BSbn-SmGdeTqNgm1plhyJzU_gjBqiGacuCHfzjxFHNCyItoPfTNTZYRSifmc7FMppvrMRr4c9r7IndFno9ZCvcLkzVzgGbHE_ewt2YTI1cm-3fBMyeFndqQ8H6s27erLKWJrwLMVmlqLIZX0O7EJjRwxB6ckF-qnCMia_Cc2JH_LucwDMDbeFSF_x5oGFcjS7e9ZzfjYdHHDbN9BycXgByyrLUEEMqxT4ofkef2ehe_cpkeOnXZdLcen4eKBPlfs-p_lCZ2tOvO3CGVKd4JxNVAMO_kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca485d3e1.mp4?token=oI50lj6-pl1GMs4-LhhPGXN9-FqvbX3tDpgqfr29_5q5zddo9Xzw-YdDp4BSbn-SmGdeTqNgm1plhyJzU_gjBqiGacuCHfzjxFHNCyItoPfTNTZYRSifmc7FMppvrMRr4c9r7IndFno9ZCvcLkzVzgGbHE_ewt2YTI1cm-3fBMyeFndqQ8H6s27erLKWJrwLMVmlqLIZX0O7EJjRwxB6ckF-qnCMia_Cc2JH_LucwDMDbeFSF_x5oGFcjS7e9ZzfjYdHHDbN9BycXgByyrLUEEMqxT4ofkef2ehe_cpkeOnXZdLcen4eKBPlfs-p_lCZ2tOvO3CGVKd4JxNVAMO_kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام موسوی‌مطلق: تشییع رهبر شهید در عراق، بی‌نظیرترین بدرقه تاریخ عراق و بلکه تاریخ اسلام بود
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/453847" target="_blank">📅 14:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453846">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZ1XU7J1A4pGfqRYyqvWqcf2APjqSWfxenrcztXoUQt8ldUPcw47jZHS5WKI6R58HAqwHIoHuXe6mbUS1on62i1s-BeJ4FSFsZiOXfeGiG6mCoa_xCOY_8Vr73StKaPC3QA1maDCvmDdB7TuLW6E8VxzQ2bpJjR4kJWT_JAsM9QCK-mAlDkwgoVzZgshU4-JNJlrVMQnIe2CqlBbnZg7L1ZRVzApo_e6JIADLqk77K68h9of5OsFfiWx49hwo_QBFxM0h8tjfam8KmsaFIMeMstzuvwNNjpl0yCsSqJ4_zz64b4_WcEUo5H1Vk3YqwCa8XA-ngb3R5gfF57Rmhzv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلاکت پدافند هوایی اوکراین، فقط یک بالستیک شکار شد
🔹
رئیس‌جمهور اوکراین امروز با اذعان به اینکه پدافند هوایی اوکراین در جریان حمله گسترده شب گذشته روسیه تنها موفق به رهگیری یک موشک بالستیک شد، بار دیگر از متحدان کی‌یف خواست برای تقویت سامانه‌های دفاع هوایی، کمک‌های فوری در اختیار اوکراین قرار دهند.
🔹
به گفته ولودیمیر زلنسکی، نیروهای روسیه در جریان حمله شبانه، ۳۵ موشک از جمله ۲۷ موشک بالستیک و ۱۸۵ پهپاد تهاجمی از انواع مختلف را به سوی اوکراین شلیک کردند که کی‌یف هدف اصلی این حملات بود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453846" target="_blank">📅 14:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453845">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d89446ce.mp4?token=eFgNWveJl6ZF9ZwQT5vpUUlv_pUwEeXsQkPFHFcbFGcK5fFfWa8tF_ub7-XJOacFvsnqDWiXB2Nl5z_5QEGSZ5UIBPEM1WS06I9vmjQYCD9GIP-iFdGfx1klVvhB94tNA7GxjXLJ4C1piGej46PKexRr0gXjpaoOIJ6dY5dObDUSzSRfMQ67ljRF5JEdO_ABnC9U4tbL8kzdC6Jw2hIPSVWN0c1V1HO2FArsDM-smZLzSqCWPLjEO6vBdPLNsn_8Wx2bs1HKd8cOC0uvN9zJDr536eGWBeqeVzVU0Vd7Wb_NjbXfxL6dzgHiP7hm-lRAH4aGr0ejDYp4bf0Cw9J_wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d89446ce.mp4?token=eFgNWveJl6ZF9ZwQT5vpUUlv_pUwEeXsQkPFHFcbFGcK5fFfWa8tF_ub7-XJOacFvsnqDWiXB2Nl5z_5QEGSZ5UIBPEM1WS06I9vmjQYCD9GIP-iFdGfx1klVvhB94tNA7GxjXLJ4C1piGej46PKexRr0gXjpaoOIJ6dY5dObDUSzSRfMQ67ljRF5JEdO_ABnC9U4tbL8kzdC6Jw2hIPSVWN0c1V1HO2FArsDM-smZLzSqCWPLjEO6vBdPLNsn_8Wx2bs1HKd8cOC0uvN9zJDr536eGWBeqeVzVU0Vd7Wb_NjbXfxL6dzgHiP7hm-lRAH4aGr0ejDYp4bf0Cw9J_wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عارف: افزایش نرخ ارز به سرعت در قیمت کالاها اثر می‌گذارد، اما با کاهش نرخ ارز، قیمت‌ها متناسب با آن کاهش نمی‌یابد و این روند باید اصلاح شود.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/453845" target="_blank">📅 14:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453844">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب کرمانشاه
🔹
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست. @Farsna - Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/453844" target="_blank">📅 14:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453843">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde6d95b25.mp4?token=bFgt5j88scSXKxgiS065eNMzFaZC14XFC-6h-kLV7O0PM-M0t8Oj1TpHgXzPq91lnTpHG8dJklclVwJ9PUBpRne82U8SNaqDqiGAPHKHnFcPiEmvk7DR_Iz2GIhKwT17-DBIFzw6JPzH5OoWhA1cCHHsvq7muhds7VvpWrGDXadqj_t0yuP1iUkIZJ-QywYfMeFmU9eZC9ShrikzWqN4O3xkCS8ZEmN1dWR5lwDT9mPGt1_arh1_NkWREg8HMvW3bUP6C7eW5kQp6MtVYUu9ufttHgQCWiZCeGxhx29eDi8677Fe60jvhk6Y4yNr15if27dZlPtyweMInDRqiPWYLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde6d95b25.mp4?token=bFgt5j88scSXKxgiS065eNMzFaZC14XFC-6h-kLV7O0PM-M0t8Oj1TpHgXzPq91lnTpHG8dJklclVwJ9PUBpRne82U8SNaqDqiGAPHKHnFcPiEmvk7DR_Iz2GIhKwT17-DBIFzw6JPzH5OoWhA1cCHHsvq7muhds7VvpWrGDXadqj_t0yuP1iUkIZJ-QywYfMeFmU9eZC9ShrikzWqN4O3xkCS8ZEmN1dWR5lwDT9mPGt1_arh1_NkWREg8HMvW3bUP6C7eW5kQp6MtVYUu9ufttHgQCWiZCeGxhx29eDi8677Fe60jvhk6Y4yNr15if27dZlPtyweMInDRqiPWYLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردِ تنگۀ هرمز کیست؟
🔹
تصاویری از شناور متخلفی که در آتش اعتماد به آمریکایی‌ها در تنگۀ هرمز درحال سوختن است.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453843" target="_blank">📅 14:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453842">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب کرمانشاه
🔹
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/453842" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453841">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF4sd0Mdluv0VpI7E9wU55v9ROZh9b5umrPNmbyMqlTDkEnpXw2ScoG_0lizcny7S9TZ0ZMBKSa4Cl9CSroiINocv561r3KKoHhHq08LYLSzWr293omJBsVJ8K1LLnmnfqe9dDE_bmy3rBbCorAWw0zJMNwhlKxSGeya54CI_qoBePdc4brcb-M7KcZowbFicqzDgLHq51uxeWOBV85uJ7KkiLIiZcVImymKqOg0TpwKVYk-KZT8JEeQSV3oM1LlOyA9btU5kAI7nLGYYfc1yVHQ9s2bTeUBNSbu3yt78NKn876l7BnxpEfYmFeg2xRhRZkpL5J3zpwjtf2NGOFwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جزئیات بازداشت عامل انتشار لایو ضرب‌وجرح دختر جوان  @Farsna - Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/453841" target="_blank">📅 13:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453840">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDkNZ1hwjkdboz8bc7QAqFeHrbJEJcsF1F7RusN-m38kO9IUwBoT05-s-4fVi9IsUPcklB_PM_YUN_EekpEkFfJr6LMH3XiqtAQhzssn1M2ejjiEKs87Xur-5JB_2G6m9Fj7QqWD2mHMUcvboBPS3Fmap5QdUnrWGSwhaJuTNZPM5n1J5YcQ9Pc9UcPp_hLdCm2OmTjSoyEMCKPb8uupvqJ_LnghGWZ80mrDlkpTx-VRCtn0mRh5PUjcR6eQ2V-_1N9BT4iaQjAXfDmsVzYEH_lipB-Ny09FPO5ypaHSivD-pnSbRpA4e5DcMhP7b6jywkWHtf9fDRuuWG9SM60bGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قشقاوی: بررسی طرح مدیریت تنگۀ هرمز در کمیسیون امنیت ملی آغاز شد
🔹
سخنگوی کمیسیون امنیت ملی مجلس: محور اصلی بررسی‌های طرح، حفظ منافع ملی و تأمین امنیت ملی کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/453840" target="_blank">📅 13:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453839">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffa6b3220.mp4?token=AM9zWh34nJE7SAiobiQAC4m1Qher6cdA3XkgF4lZgtHcQM-eTEVXxq9_lU8iJ_UanStKGtlggGqqhF-cEh7R9mAV4Hk5ruB1VHvPcx756Zj2eFm8eQktHKWftGdJ28opuaYK4F-iI76z4Ahf4m9C9K9X7o0q1KawofGdLa_aXE6XhlAmtr4png8t1V9CghZLJoF3jz0KPIgWqgtAROAXMNRjeyZQrVD5a_Qt43ArxN-hqYCPTRJKzgrZSbThrCIueWnadVnr_iAmF0WQF-wrk9yz-nfXtY0on6AtJTKuUdNaqm2xUOPfvHL6TeKTAMKOrCHEdbyp7pM-l0nXaEUsSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffa6b3220.mp4?token=AM9zWh34nJE7SAiobiQAC4m1Qher6cdA3XkgF4lZgtHcQM-eTEVXxq9_lU8iJ_UanStKGtlggGqqhF-cEh7R9mAV4Hk5ruB1VHvPcx756Zj2eFm8eQktHKWftGdJ28opuaYK4F-iI76z4Ahf4m9C9K9X7o0q1KawofGdLa_aXE6XhlAmtr4png8t1V9CghZLJoF3jz0KPIgWqgtAROAXMNRjeyZQrVD5a_Qt43ArxN-hqYCPTRJKzgrZSbThrCIueWnadVnr_iAmF0WQF-wrk9yz-nfXtY0on6AtJTKuUdNaqm2xUOPfvHL6TeKTAMKOrCHEdbyp7pM-l0nXaEUsSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عراقی تصاویری از آتش‌سوزی گسترده و بلندشدن ستون دود در یک پالایشگاه نفت در اربیل منتشر کردند
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453839" target="_blank">📅 13:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453838">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار اصفهان</strong></div>
<div class="tg-text">🎥
باند حرفه‌ای ربایندگان طلافروش در اصفهان متلاشی شد
🔹
فرمانده انتظامی اصفهان: در پی وقوع سرقت همراه با آدم‌ربایی، ۴ نفر از عاملان اصلی سرقت و آدم‌ربایی به‌همراه یک مالخر اموال مسروقه دستگیر شدند.
🔹
در بازرسی از مخفیگاه متهمان، یک قبضه سلاح شکاری وینچستر، یک قبضه کلت کمری، ۳۴ فشنگ جنگی و بخشی از اموال مرتبط با پرونده کشف و ضبط شد.
@isffarsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453838" target="_blank">📅 13:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453831">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mv5D5nTmV1KjsxneBPt-KIsZpnBb-JxoRpy_uRZnbNCwOwIyv9bRFb2zmlor0eLdzGuEYThphiFRVhQWEfrXAcWNwj-dqMz8LfiflpjR8fPGiGarCJ157B5Zp8JzbcHg4fztqxQCBLyyMYwp66Eshmsvhe6NAg7zc0cQ3gOgCRBOWqAyJEPI55OjuTBcx1kY1xKvYWfGUgAy6xLzcJdb82c6cFBhN2qeAhnz_Z2qhBa70Cpo2Rkl8yZxdwsd_RWtfELHo1-5ZmvATAI4kwEjd_ze1hCEhIo9uTPaH2iaP7t2sREPNg5jnTouIuv55uF8dqIOkKiaREMXijBBwTnKQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lDvutuRca8eGs-PB_VWyDxp-5z2HXPrLKBk17KnwYHK3I0RXHkk8FtmzbQlBoKN1kwgWBgVJHtK9l1gTNVRNYLl3GkPxBE3J7U8IEH6fAOWU7wV8qYx2JH8jEuuMTeBn7Jb-_QJRRIV6G988OHKKkRWGz6dhgT1d8bnnrKsR6XRUos9P4sfwzRZ0uhluJGs5rmoSRMLsxD8Ce7e_doJtn1zRW86qp79ULXacg7gQGdIuTEhny25QwMD1sMndAy3zWlBH_SC5A6tWN7NYiodcEBu9Ti_w0M7DR5JU_PiqfUK0tWkLi6ojXYWKzo9pFIVFRGd6diQ0awpmlB79Iqp9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLDnuApLq8raMftDbRVZWXzMwKz57iP-V-d1--ZeNAIs0_KKhyDzPH47uQTo7mFePd8zKGBbtAEgCmEryFVWhot0mFXhP0UzmsD7dzmsYKGec8UrM-yjjO1gQKUiSAuVeeS0qB8R0mONKkACMhJA_ZkSBb8HMOojoexAMHiZVRPql0cYbdfFUUdiBBjv-d1iR5zCTVgpibYH0V6_0iNDudjPKJY9Gta-KoIj7yojygYZ4GcROm_Q4aTVI1rdaNluTD3Ncx5uGeqJDGte6F7fYnRCUUPcaJa2BvqewyHCwXT1fpkJKSMqCrCyz7F7mHAXJNd2eLmQcdwiZM3iki_Cjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xc45aO7409_Jv7J10H-EwNaCxhfeJZgm38fNjYTavBr7Roqfx4CEm8hkcibWfRFrj4vMoiUvAQLmlusmueUxaaT4_oN2YG4ERM4al3PACF_6mtQAwECkf8eIIUmXlHkwAfPwN0fvNxa4W83nguz3Dmh3EP54GXSlfhKU4o3BionXfNHN-71rtUJv08u8ADy-bDT6pqWzqwjJPJVrXlA7hjlNy5GRQ3ZD5VG9OOkdiQmlLzEG-S-hhQfZj-2dDNNC_2XjlOPyV6S1YScfcCx3-s_64AotKn7QR6q7hrEAdtA0UrialiglKZWX0n2yfcrfv5g7pXnZHTVsBQqA__iL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4-5FTO-fmDBIOv-kPMj8pyDCTyA_X02Z0lfEqUDRAbnnWg-FeuiS8O0BynqG-gwkvexVEVYA0SF_4TNtohemBiYll-R0KWZNnHDJEOZKHBkyjiZQU9Z_o5xgjBQBT9FWsB8wdpwPZrIXuHgQDxkofEaYhfKw5-JvLsaxJmkAwCpJ1owZD6jTSVg16wWmOzGDvvyFepmIjC57w3e6hHmn5zcYgOJ8IU_KmoO_HTCdLs9l0FhWb1XeVu0Kgn2AfTfj2p_bTKJmTlPU4BX--8CBaFuEzBt7Hd2CJvkwCz6oJ5dSgfxB5DTQ8WCL9RxIi9edpeFvv6AIsBVLH0Vz3VV2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jb0QDamUGvtEfeMrj3V0USjLib0szBiCj95EwkDQ14CdGt5ayGaMsXDv1RVE1akhkIhIn0PypDbS9-T6UJW72AwmUKm2dU0pXMUiv_G361s5_0Ms1ByqjJYsjuXfN3AP5mzInOucJGheQnPoRuh83zqRUuWgGVz_0gpEm514s-jYuVlW8HQaCOkRxi3qCzNtbDEfuNUQSDygDdw2-KL0dZQiOj28ElQcgfdFn_BUVnWgv_EFLKcmrYXGkaTkb_sqIfpGnYFz74jHNmzhiv2cSzG-rK8_NypQdpuL9QwEP3slZZZbU8J8-jBUpnQNiGRuVTRbPhrtLxoEhfTU_FBY-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIl4_D80T2PEGGMFm69Apj05cdLRNpnzA41Aw3x-MP35-HEjt_Ur8kA35KfDNu9hRIvfZWOB-lvGzm_xV1Utzb999WL7Vfc-ShppPB9EMkEwIolAn2ZUxgYp2fkwCzpltmS656GNctWvdsbf0REvY-GmOpWx4C748lvqLhXwaWR_jkJ8wJLNFxJ_xIea0T4CQ2riogz85QSjdXS8XcQVtA6RPOliCAXkTk0nGecgIv2ZtHqdxlwKQ6XrXgl73zXCIO_BI7RD4JupvOc_2axLOAa2kHrVaMDJKRkwSVEuMUWQKybqZ9l8rlnO6UcnLxNyLo5wDB6lSCf5UBFRLhPadg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اردوی تیم‌ ملی ترامپولین در همدان
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/453831" target="_blank">📅 12:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453830">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSVpmz83t4fHPlO6B1h1K6Z6Kgnw_Y2EtvvVYkYn-VoLaofk4kCFsUHsvZyuvIXgpJorAPz6sX62uKhPKZtDf28fwWZu_s5NG2a2yaKwqVrmevKV1FBhMDOOT7DLZ6ym2L0mx05iGXT2-v3AdViAdR533FnLUdG5dFiQ4ZQ9dXqdWI8cBDRJen9GBk3E1W-B1laN-Tk7_HkntfvwsiT3JeK5na-vGmdCSzW3G4jPUEi75OvdhlTL-BE0w5285XT3FkqO3FmwuIy6VjqqRcyeCFqzmfjs0yuIlhHUzOK_-7BrtF-pGQIBqjN8viU0hZd-NTRhHdqxdLvcT8ne1OI_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جدیدترین تصاویر ماهواره‌ای از خسارت یمنی‌ها به تأسیسات ینبع عربستان
🔹
تصاویر ماهواره‌ای نشان می‌دهد مخازن تحت فشار ینبع همچنان در آتش می‌سوزد و حدود ۲۵۰ هزار بشکه در روز دیگر از ظرفیت تولید از مدار خارج خواهد شد.
🔸
نیروهای مسلح یمن بامداد شنبه تأسیسات آرامکو…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/453830" target="_blank">📅 12:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453829">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0H1NfX4x_NBjhhJQQ7FxEU-8utmbNGl1oAJPwNFsNqUuoDQOZrOt7l7L9pDO7NNudqqBTxqk5XDikm-0-3VkCj1szZIv6YYZzA2KmhYanbqU8XII_-w8OZ9HIJ_28SEmqg0iIUrnDPJUGfawEdBHmRAh_-1-Qmi1gAHcQ3eKPMjWKh42L0aSH_Q_4SrdnkIiWVAJDy3Rya8DPhwmSKYMcxKSC_YYT-tt20PBgJOr6IR5-3c35LR7Oph_H82mYlaSed8cIoYPZ0UeumvZ7LJkJUmBqgzwlUughK8cRWc9YP4qMc1m_HZVeN7NhVXBKrg4YuhJr09wbj3J3LG4yvMRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۲۰ هزار واحدی به ۵ میلیون و ۵۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/453829" target="_blank">📅 12:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453828">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mftouGBosYJxu60Gb5ej1JkyjxmDKyQToxlijxRsPVTB0CAWE1acumqnhDeXHgHSpWv92Q1AQGhi9Kr8J8v3JH0M9YUSM8W94YL9ygAWmxbtnz5ohvJ4QJ-ETlngD5AsNtDqANk7_S1J37ZKSjYzWiKsdi45M_V3BRBslBRypoGw__QkKBkCMtAfRpzhldrZxwanS2CAYMRU0TB1jXYF_3Gv0RGP4TCD--EDOUO0Cvv5JogxZB_dejYbXgPkU638gKYSrF0rKC4TipsjGawn-p-eCIJNU7p-UTrclUmHzODqsJHIUjy_fCE80Q77Ws-RY49Zt10kUqriSQh9TVufXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت آمریکا در اردن: آمریکایی‌ها برای بسته‌شدن حریم هوایی آماده باشند!
🔹
سفارت آمریکا در اردن، در اطلاعیه‌ای دربارهٔ «احتمال تشدید تنش‌های پیش‌بینی نشده» در غرب آسیا وجود هشدار داد.
🔹
این سفارتخانه افزود: «آمریکایی‌های حاضر در خاورمیانه باید برای لغو پروازها، بسته‌شدن دوره‌ای حریم هوایی و اختلالات احتمالی سفر آماده باشند.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/453828" target="_blank">📅 12:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453827">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iU26YigLgl_8y8oS4kmGgLw8S1m6JQlZ06nXqqXxA_vLCfDNHgwgON83_5WaKbVocmowhMnt_OsWFhasMWOa--SI6vSGXyQx8ylgJUUtppZOACHxldRRAOOVG1ELmfTabp4noBmOcOVKQPmejqYfcfhPNeg9Z8fBStav6WPWZirHmfPFKA23S3l_IB9VHUwKF_QxSeZiGFb1L0UEXeYY5tWNjzw6bF_6Uj66X-cfA5NHaIXkNXCt-3ijE0e9iMeDmNB0L25OY91Auzz2yyAIb5BldXRNuuyp9Xt5s2_wpuilcVBxGJehpuupnjCENgRMQUNS0AJSTlheKRtumXwhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی ترمز سود دلاری یک بانک دولتی را کشید
🔹
بانک تجارت ۱۰ هزار میلیارد تومان از سودی را که از افزایش نرخ ارز در صورت‌های مالی خود ثبت کرده بود، با تذکر بانک‌مرکزی حذف کرد.
🔹
طبق نامۀ همتی به سازمان بورس، بانک‌مرکزی برگزاری مجمع عمومی بانک را نیز منوط به اعمال این اصلاحات کرده بود.
🔸
بانک‌مرکزی اردیبهشت‌ماه با ابلاغ دستورالعملی به بانک‌ها اعلام کرد که اگر وصول مطالبات ارزی یک بانک با ابهام روبه‌رو باشد یا بانک به دارایی ارزی خود دسترسی نداشته باشد نباید با افزایش نرخ ارز از آن سود شناسایی کند.
🔹
با این حال بررسی توضیحات حسابرس در صورت‌های مالی بانک تجارت نشان می‌دهد بخش مهمی از سودی که بانک از افزایش نرخ ارز ثبت کرده، مربوط به ارزی بوده که بانک به عنوان تسهیلات پرداخت کرده اما به بانک برنگشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/453827" target="_blank">📅 11:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453825">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e157b43618.mp4?token=d994-eEAk1f3doQetfQIzV_kPDRTBtCK-WsOdhJq4PBlF8rM4UyfDem6m1g1yNob74-Y13dzDMazSuBFWG_JkorZhk9O__EJo2tYC-jHQZ70FOFKSnZmIkY9TrsoI64ufG0pm-hsc04ErCdy_W3ep5M_ImwREs2DR3pxRlrsSq5syF4AYNg9q5TcP3KfhZ5CVMl09nofhUoPDAbgKvwlTjbbAS79VO2ViKqzGdWKqBHZaPlhVnH6I6Za8w2_41MIQH6zkU0XqMa6j5x9mB3m2jhljpgRORIxldTGC6oZio0T0TwM_rau2RHn_mFSkjElUeyPjyNdSPn-lq4VMVmrLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e157b43618.mp4?token=d994-eEAk1f3doQetfQIzV_kPDRTBtCK-WsOdhJq4PBlF8rM4UyfDem6m1g1yNob74-Y13dzDMazSuBFWG_JkorZhk9O__EJo2tYC-jHQZ70FOFKSnZmIkY9TrsoI64ufG0pm-hsc04ErCdy_W3ep5M_ImwREs2DR3pxRlrsSq5syF4AYNg9q5TcP3KfhZ5CVMl09nofhUoPDAbgKvwlTjbbAS79VO2ViKqzGdWKqBHZaPlhVnH6I6Za8w2_41MIQH6zkU0XqMa6j5x9mB3m2jhljpgRORIxldTGC6oZio0T0TwM_rau2RHn_mFSkjElUeyPjyNdSPn-lq4VMVmrLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: گرینلند تا ۲۰۲۹ مال ماست!
🔹
رئیس‌جمهور آمریکا که از بدو ورود به کاخ سفید به‌دنبال تصاحب مناطق مختلف جهان بوده، این‌بار گفته که گرینلند دانمارک را پیش‌از پایان دوران ریاست‌جمهوری‌اش تحت‌کنترل آمریکا درخواهد آورد.
🔹
ترامپ در یک مصاحبهٔ تلفنی گفت: «مردم گرینلند می‌خواهند کاری انجام شود؛ گرینلند از دیدگاه ما مهم است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453825" target="_blank">📅 11:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453824">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
سرلشکر عبداللهی: هر کشوری با آمریکا همکاری کند، در آتش جنگ خواهد سوخت
🔹
فرمانده قرارگاه مرکزی خاتم‌الانبیا: آمریکا با شتابی فزاینده، مسیر آتش‌افروزی فراگیر در جنگ منطقه‌ای را دنبال می‌کند. این رویکرد، برآیند یک راهبرد خطرناک با هدف توسعه و سلطه نامشروع در کل منطقه است.
🔹
آمریکای جنایتکار در جنگ اخیر علیه ایران اسلامی ثابت نمود که در مسیر دستیابی به مقاصد و اهداف شیطانی خود، از هیچ‌گونه شرارت و ویرانگری علیه منافع و منابع مسلمانان پرهیز نمی‌کند.
🔹
کشورهای مسلمان منطقه باید بدانند که آمریکا با بهره‌گیری از سرمایه، ثروت، زیرساخت‌های حیاتی و منابع راهبردی آنان، به عنوان سپر دفاعی ارتش فرسوده خود و همزمان تقویت ماشین جنگی و امنیت رژیم کودک‌کش و تروریست صهیونیستی بهره می‌برد.
🔹
جمهوری اسلامی ایران و فرزندان شجاع و قهرمان ملت در نیروهای مسلح و جبهه مقاومت ثابت کرده‌اند که موازنه قدرت در منطقه دیگر از مختصات پیشین پیروی نمی‌کند و ناتوانی آمریکا در تحقق راهبردهای تجاوزکارانه و نامشروع علیه ایران اسلامی، باعث گردیده است که ارتش مضمحل آمریکا و رژیم جعلی صهیونیستی از پشت خاکریزهای کشورهای مسلمان، اقدام به جنگ، خون‌ریزی و شرارت نمایند و هزینه جنگ را بر دولت‌های منطقه تحمیل کنند.
🔹
به صراحت اعلام می‌گردد؛ کشورهای مسلمان بایستی با دوراندیشی، جنایات آمریکا را زیر نظر داشته باشند و در همکاری و همراهی با آمریکا تجدیدنظر نمایند؛ که در غیر این صورت، هر کشوری که خود را سپر دفاعی آمریکای جنایتکار و متجاوز قرار دهد، در آتش جنگ خواهد سوخت.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/453824" target="_blank">📅 11:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453823">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REFFgBSx9ku297Yrwp4_km1QfmBMTFhk5WvwBC2iG9szP_lnde-GwROwWMDwlrJIouOHdZIDAtQVfA2T9P05tr2ATfGx9ga7bahcYuYdDeI268SciSJ-8-U2-y8pK8Hj6LnED28OqWeF3sNr1-JIgo5w66fwE512o3x7iRWpFss5QtSQ2TTyXyDn3kXNmJso5MjCsHLU71mnoA3r8DPeTk3ZvSdyA5Teuv2Iqlp7oE8ZkOiXv1HpD1e_lkssqPvcqROdRX3W01sFq3HrXkihhnQZF5r81zOtoawoRBQxqPIxz4pTgwd1QEWdiK011rCjqh0xLiNMg6s8rprYIGhV9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوفا، فیفا را تحریم کرد
🔹
اتحادیۀ فوتبال اروپا و ۵۵ عضو آن در واکنش به پیشنهاد فروش سهام فیفا به سرمایه‌گذاران خصوصی، بیانیه‌ای منتشر کردند و اعلام کردند که در صورت انجام این‌کار در مسابقات جام جهانی ٢٠٣٠ شرکت نخواهند کرد.  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453823" target="_blank">📅 11:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453822">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWymxOJIgG9-nTpAoWAGICS_bCAh0h3bTdK6ozUQr9S1wUoq7v3-ORm-vK0x_rs0e0V70PNCQp9_XXa2s0PD3vg9bDphHU12rIWiZmt4TH6kPCNPsxu3t3SMeEFdxxTxdm2LdVbCTNmEzo3ztmA0Mv5GUDd_HwnNlNWI7Gaz5oOlNi8M1hToYL979HuXCgzFvtzTe2438tEnXQet9iIVKUd8Ij3wJRBz-SM4yjI45CFJag5rGyLiK_76ExBnJ4dpIaNBnf0N5Ch8PZUrdKXjMdYONhErfypXOh7YB_uRRGlEOX5-0sUiklfocZZlrBgfDQpvvfXbT9SmbfKwwTJkzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ بازی خاطره‌انگیز آتاری، فیلم می‌شوند
🔹
ددلاین، از معتبرترین رسانه‌های تخصصی صنعت سرگرمی در آمریکا، گزارش داده که شرکت آتاری در همکاری با Entertainment 360، قراردادی با یونیورسال پیکچرز امضا کرده که در آن، این استودیو حق توسعهٔ سینمایی ۱۰ بازی کلاسیک آتاری را در قالب فیلم‌های سینمایی اکشن و ماجراجویانه دریافت می‌کند.
🔹
فیلمنامهٔ این پروژه را «مت رایلی» و «کارل همپه» نوشته‌اند و هر دو علاوه بر نویسندگی، در مقام تهیه‌کننده نیز حضور دارند.
🔹
وید روزن، رئیس هیئت‌مدیره و مدیرعامل آتاری، با تأیید این خبر گفت «بیش از ۵ دهه است که آتاری بازی‌ها و دنیاهایی خلق کرده که مدت‌ها پس‌از انتشار اولیه همچنان بخشی از فرهنگ عامه باقی مانده‌اند. از همکاری با یونیورسال و Entertainment 360 برای انتقال روح برند و بازی‌های نمادین آتاری به رسانه‌ای جدید هیجان‌زده هستیم.»
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/453822" target="_blank">📅 10:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453821">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/440afe73b7.mp4?token=uNVZazudwGHRKs5ToCADE-zt2dmIOIH2xAgllMTjEyKt7Cju6EmqPpsR8YvPtJibLo4tbIWeaPPu0S9PptMCzxZGBmaQbbCobN-_NiEl5JPQiP3yBU6FHFeVuiPYaqiJiZtVmgDwEpYS5C47L0UoFrb58-ftRySiYrbr7jFRuSJs442LVfeZSRhWBkN9Arm-muuRv6P9vwCgc6KaXc-PsZTbFu5eGSYC6Fa9glhidhI6r-dI_yEqidGVCtMwNcdOXukxi1cOLX3xRkjUrUmjbts4boYoMpkX6iVrISHIQ7ZEKapFV5EzT5rOD6rwIsdFi0P0TG8vbXBRlD8jS0N-ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/440afe73b7.mp4?token=uNVZazudwGHRKs5ToCADE-zt2dmIOIH2xAgllMTjEyKt7Cju6EmqPpsR8YvPtJibLo4tbIWeaPPu0S9PptMCzxZGBmaQbbCobN-_NiEl5JPQiP3yBU6FHFeVuiPYaqiJiZtVmgDwEpYS5C47L0UoFrb58-ftRySiYrbr7jFRuSJs442LVfeZSRhWBkN9Arm-muuRv6P9vwCgc6KaXc-PsZTbFu5eGSYC6Fa9glhidhI6r-dI_yEqidGVCtMwNcdOXukxi1cOLX3xRkjUrUmjbts4boYoMpkX6iVrISHIQ7ZEKapFV5EzT5rOD6rwIsdFi0P0TG8vbXBRlD8jS0N-ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت قالیباف از چگونگی شکل‌گیری میدانی به‌نام خیابان در جنگ تحمیلی سوم  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453821" target="_blank">📅 10:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453820">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656e493994.mp4?token=tm7rI-9yQoz6HcpV6DqbGwV-bVreLQWcwCvuDvBtxU08X0LvrPtiX7JDuNbXeStsMMXG-Uu6YqMTmnoTmjb1o7AfKzFsIg-nKstjnPG6tJwe1KQUB40JMSXjZthtmXQS49Re5FJp_X8XQxQEOqwnEHfAKgSdxMx2IGDKx1S4yImVowcrWCuJQZ4ote5yceXNefQJnEUNRY87VCNQPkJXUkWwwEmF5zy5JWrIYb57fV3EnylVmT-8_Icu5dr-thIPCg5ZWNQ6fnAHcn2lKtS-fpw9sl4fAZwbLKbV1ieGD65-3mQ7vpaWYNwpwLSH893usdPgnKAi7UGPmU-LZ8gQOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656e493994.mp4?token=tm7rI-9yQoz6HcpV6DqbGwV-bVreLQWcwCvuDvBtxU08X0LvrPtiX7JDuNbXeStsMMXG-Uu6YqMTmnoTmjb1o7AfKzFsIg-nKstjnPG6tJwe1KQUB40JMSXjZthtmXQS49Re5FJp_X8XQxQEOqwnEHfAKgSdxMx2IGDKx1S4yImVowcrWCuJQZ4ote5yceXNefQJnEUNRY87VCNQPkJXUkWwwEmF5zy5JWrIYb57fV3EnylVmT-8_Icu5dr-thIPCg5ZWNQ6fnAHcn2lKtS-fpw9sl4fAZwbLKbV1ieGD65-3mQ7vpaWYNwpwLSH893usdPgnKAi7UGPmU-LZ8gQOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: سرنوشت ۳ خلبان حاضر در عملیات ۱۱ اسفند ارتش هنوز مشخص نیست
🔹
پیگیری‌های ما ادامه دارد. طرف قطری اظهار بی‌اطلاعی کرده؛ از ارتش و دولت قطر می‌خواهیم که با مسئولیت‌پذیری بهتر برابر با کنوانسیون‌های بین‌المللی اقدام کنند. @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/453820" target="_blank">📅 10:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453819">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bc7642af.mp4?token=X9QGQjF42dlKbWDALadFwn5oyEXNr9c4Sf7CwHITZ-HPjT90iG_AQ3WuvfXY94JF65WxxWBCeOVo14EyalOFD_Flmbe3yfYxRskuHeAKiHPHhWs-itawpu-3-ghwBP1FxbcmxhMv_pEFznwbanGv3JqkWEbqay7pVMZhIV0mMh3f65m3suF1SuXPZxWH-BIByvKVekEgUw7IJRVZrXj9RUv2qP4yC6AbSZeBxNX8B8Oeb-nXpmoyOB4QsMWRpg9FCZE30Gj1R5D_ZaafyPRDTujScqs_iDpF7tsZK3qK_ENDE_tQc1fxZchJdRXIKJ9dxiCC0Qkru1Jjcw-7ZRhztQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bc7642af.mp4?token=X9QGQjF42dlKbWDALadFwn5oyEXNr9c4Sf7CwHITZ-HPjT90iG_AQ3WuvfXY94JF65WxxWBCeOVo14EyalOFD_Flmbe3yfYxRskuHeAKiHPHhWs-itawpu-3-ghwBP1FxbcmxhMv_pEFznwbanGv3JqkWEbqay7pVMZhIV0mMh3f65m3suF1SuXPZxWH-BIByvKVekEgUw7IJRVZrXj9RUv2qP4yC6AbSZeBxNX8B8Oeb-nXpmoyOB4QsMWRpg9FCZE30Gj1R5D_ZaafyPRDTujScqs_iDpF7tsZK3qK_ENDE_tQc1fxZchJdRXIKJ9dxiCC0Qkru1Jjcw-7ZRhztQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۴ خلبان سوخو ۲۴ ارتش چگونه پایگاه العدید آمریکا را به آتش کشیدند؟
🔹
۱۱ اسفند سال گذشته، ۲ فروند بمب‌افکن سوخو ۲۴ نیروی هوایی ارتش ایران، در پاسخ به حملات ارتش آمریکا و رژیم صهیونی، در عملیاتی از پایگاه هوایی شهید دوران شیراز برخاستند و پس از عبور از سد سامانه‌های…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/453819" target="_blank">📅 10:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453817">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-jmEXHeiY_ch88t2fPHEEsLXocfnZyYDc0b1wuV8Xe2vMhda6TRAAcf5oWhC0sOMHw_UZhSuPCKOjyr0u45WA1qYaIJofVryV-AsDMdS-eHSzo7eeMno2g9ag1fVKrMGUlui920vKpZnktLUcfyrY-Upm4RVfr8aBLgqBvpd8R64Pfvl1iPnneKOq2p4q67znWRSEgXsBrwJxDz9qvX7mYfWjP5snzAHNUGIbBSNH-v6Y9CkwgI7UhW-cIopETR7jj6nW1ENjhXvZfen-RDDnkthF1EdvrJlGptqA68DhSLSNnPLwoOklVyvD5SW0bM74ILgmeJPjc7l2kjz_kG_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار افغانستان در تسخیر کالاهای ایرانی
🔹
بانک جهانی اعلام کرد در پی اختلال در مسیر تجاری پاکستان، تجارت افغانستان به‌طور قابل توجهی به‌سمت ایران و کشورهای آسیای مرکزی تغییر مسیر داده است.
🔹
براساس گزارش بانک جهانی، ۴۸ درصد از واردات افغانستان از طریق کریدورهای آسیای مرکزی و ۴۶ درصد از مسیر ایران انجام شده، درحالی که سهم مسیر پاکستان از واردات این کشور تقریباً به صفر رسیده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/453817" target="_blank">📅 10:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453816">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
ارتش کویت از درگیری پدافند با پهپادهای «متخاصم» خبر داد
🔹
ستادکل ارتش کویت اعلام کرد که سامانه‌های پدافندی این کشور در حال مقابله با «پهپادهای متخاصم» هستند.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/453816" target="_blank">📅 10:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453814">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvjlIM3m7zhz9yNwPMg3a1Xlr4xLkz37jkZGEHrAQtZFvoPEmKMxgtTDcIjR7oCnw45GXW6VoTOdADcYPMYLZYY_eABbAXx9Fud01DMMam_Tov0gCV22NbkZDSQRxlW0BoDlmsKnWCTv0wlLjsAH-nefih2FcajZ60enKVQc_WXEske2fXlSsKH8mCErVbCbhd4gannl_TfmU2bTuWyMGekpxvZP7-vnisyPAORXaH_qSevvUuM3q9xYYahy6tyvaQIrw--6kwpZQ4MnfuckfrdssbI8mtVi1IaP2dwyohqOVmy2cZJF9nCErq4CLAkmckvcXtmIY5G-b4qa2k1bAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از شهید مصباح‌الهدی در کنار رهبر شهید انقلاب
🔹
این عکس متعلق به آرشیو شخصی خانم سیده هدی حسینی خامنه‌ای است.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/453814" target="_blank">📅 09:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453813">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oROnfMLAFzKjJJ66pJixdkQjjpu3dQjFoGXrrw63TiYtJNwR1XQLt15h6gcn2SmzlcAL54Z8H9ZQGnl9t11lzuD0EfehjztZ5PGYSmCm59p00GXj6K8iv6hEzf4gwCErib5PouDcX9XlhMkoa4olKj2wpHsXUxzbuY1ytLigB3LVWMUgRBgtSnrjvkzng6jETX_gwB01np67sixxJTLNsTV0yhr8B_dlqxzaYeFZbmzgUGx1qlgRnnJqowhwzLmPNwPiASenjPb0zucSxf66w-siGmxJil2QfBrm_CKUHufdbHAbI-ZiCVPzOXxkWPCdT2EMVt4pepV0AuZ_xmA_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تراژدی در ارتفاع ۸ هزار متری پاکستان
🔹
یک بهمن سهمگین در ارتفاعات برودپیک پاکستان، یکی از تلخ‌ترین حوادث سال‌های اخیر دنیای کوهنوردی را رقم زد؛ جایی که یک تیم بین‌المللی ۱۰ نفره در ارتفاعات این قله ۸ هزارمتری گرفتار شد و سرنوشت چندین کوهنورد همچنان در هاله‌ای از ابهام قرار دارد.
🔹
در میان افراد این تیم، نام نیرمال «نیـمس» پورجا، اسطوره نپالی کوهنوردی جهان و رکورددار صعود سریع به ۱۴ قله بالای ۸ هزار متر، بیش از همه توجه‌ها را به خود جلب کرده است.
🔹
برودپیک با ارتفاع حدود ۸۰۵۱ متر، دوازدهمین کوه بلند جهان و یکی از دشوارترین قله‌ها محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453813" target="_blank">📅 09:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453812">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK_NxCotUJ_Rk7Q8SK1XbuBipN5TohrMyydLmWIWGC_MRQPIQAfzJ4j6l5SogpvtTwSioRCfWPjoK7fjRAhToGxu-bhHCOAaRgaykESAovOJZHRStfMipo2ZOCn_f3rYULICWc6gPJOmbd6KB8mLsssaGYxDFpY5TP4mOQyRTzgZant7bmZeZ3ZRWnGR7pPjIwYDlJYm781v937ShpJsnhyG80XORVVwKc8uJd2oJfFWbxhP6vdRxvBs0-dmQCpPz4vmwrViL2_2Ysx9glGb2vFq8rQvGxoAbEdKlSg8nLWt4CRhdBbI6NX_4stNxtOsD3vJZWuIGXmVZT0GGA9Z8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متروباس ۳۰۰ نفره به تهران رسید
🔹
شهردار تهران امروز با اشاره به خرید متروباس برای خط آزادی-تهرانپارس گفت: تاکنون ۵۰ دستگاه از این اتوبوس‌ها وارد کشور شده و روند تکمیل ناوگان ادامه خواهد داشت.
🔸
متروباس که در واقع نسل جدید اتوبوس‌های تندرو (BRT) است، به‌دلیل…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453812" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453811">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ثبت‌نام کنکور ارشد علوم پزشکی به تعویق افتاد
🔹
ثبت‌نام آزمون کارشناسی ارشد رشته‌های علوم پزشکی که قرار بود از امروز آغاز شود، به‌دلیل مشکلات فنی حداکثر یک هفته به تعویق افتاد و زمان جدید آن متعاقباً از سوی وزارت بهداشت اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453811" target="_blank">📅 09:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453810">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1732ea92f.mp4?token=ScifpMjbFkVjaKkn7lPnr0SnhAlEpg4H634Qzmn_-E46C7Uwcki1sFHpx1hTcuVDJ3QtHTAmTAU0aIHq3G0RXUiwIgH5I0jX6I9rTYZB13ag3U2pScrid-61tOdufGw-4Vc5CXPjm1QZzl0xFKOGemvAJAUUmxndS8vIHLxKPvxR7ye9W7Qnc17ZDUUsQ3LLwgOTtTpujSXoDV-6JncR7uCKttF7ESh89Xzr0KM-AqhyCcq_W4rUUg_ozHLS7Fp0HYGtQ5m2mdkIM7Qu3-uaSD71N7S2sVWscpS75IujlwRUlXKAFaCihrN9Lvw72OHPIX-ywAScPDQEsnX0eqyewgtrlyuYYW6P33xHghRDQvNduRkaX6wOH9rPDaDsh9cAQa6-e_7EzVRCpO6SwplKy7qIO-u6IF9BDvJCxl4VL6Yd1yKr9FmI8_xLbIL3G7K_0j1rcYttkW804GERF03m9CA1CbV2XTN6cSHQ3693nEiDtVDGgmGy1SMRGhbczdX2lDeh34AoxkAFrkcNewLHmhz3OgVVAWVbEogz7WQshwZbQzkgdHwYe1ab_bCaoQNMAEu2xTvu7LNKlTQYwK_kYYMX_3Rm5Z-lKAAt1cNUqnxYBbu_ZB5sk7xHxhoLI4_e5v65kBVJMy93hhlZbL4OF3YsaIryi5WZfnX_eIlLTN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1732ea92f.mp4?token=ScifpMjbFkVjaKkn7lPnr0SnhAlEpg4H634Qzmn_-E46C7Uwcki1sFHpx1hTcuVDJ3QtHTAmTAU0aIHq3G0RXUiwIgH5I0jX6I9rTYZB13ag3U2pScrid-61tOdufGw-4Vc5CXPjm1QZzl0xFKOGemvAJAUUmxndS8vIHLxKPvxR7ye9W7Qnc17ZDUUsQ3LLwgOTtTpujSXoDV-6JncR7uCKttF7ESh89Xzr0KM-AqhyCcq_W4rUUg_ozHLS7Fp0HYGtQ5m2mdkIM7Qu3-uaSD71N7S2sVWscpS75IujlwRUlXKAFaCihrN9Lvw72OHPIX-ywAScPDQEsnX0eqyewgtrlyuYYW6P33xHghRDQvNduRkaX6wOH9rPDaDsh9cAQa6-e_7EzVRCpO6SwplKy7qIO-u6IF9BDvJCxl4VL6Yd1yKr9FmI8_xLbIL3G7K_0j1rcYttkW804GERF03m9CA1CbV2XTN6cSHQ3693nEiDtVDGgmGy1SMRGhbczdX2lDeh34AoxkAFrkcNewLHmhz3OgVVAWVbEogz7WQshwZbQzkgdHwYe1ab_bCaoQNMAEu2xTvu7LNKlTQYwK_kYYMX_3Rm5Z-lKAAt1cNUqnxYBbu_ZB5sk7xHxhoLI4_e5v65kBVJMy93hhlZbL4OF3YsaIryi5WZfnX_eIlLTN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: شرط ایران قوی وحدت حول محور ولایت است
🔹
در دورۀ سوم انقلاب، قوی شدن ایران موضوع اول است، بعد از شهادت سردار سلیمانی، امام شهید ما متمرکز بر ایران قوی بودند و به آن تأکید داشتند. در گام دوم انقلاب باید متمرکز بر این قوی شدن باشیم که یک شرط آن وحدت…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/453810" target="_blank">📅 09:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453809">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a503cf789.mp4?token=EZclU0wJLV8_FmVaUuXlZx4ZwN0f3tqf1kEEQOPf52LF716qgtu6Re0B-9MdSO5-aBmRayUg_DbPD3NWtIi9H0jqDo_TNmzC01ocJxyH_pAZ838GTR1W6UfWsB-ZFLQx3hQHkM9ahpXAEt3hzQ3_2-xux2wbjiWrQMi-yjABSQlOMElOn1UMBz5HF2ctk2lv9gqYX4DaKbbZluHXBuf5Ilfv8qaqblUvVrC5RWHNJQQV9huMyKQvTQ1XPH9fvM0TerJXvymL5ykK5m9WpM5e5UYldg5kkcnDVo1EnGsYNXgRiVDvtF2XbdYZ2MrtcyVMLHHdkVCb4ejwfvn4yfkuJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a503cf789.mp4?token=EZclU0wJLV8_FmVaUuXlZx4ZwN0f3tqf1kEEQOPf52LF716qgtu6Re0B-9MdSO5-aBmRayUg_DbPD3NWtIi9H0jqDo_TNmzC01ocJxyH_pAZ838GTR1W6UfWsB-ZFLQx3hQHkM9ahpXAEt3hzQ3_2-xux2wbjiWrQMi-yjABSQlOMElOn1UMBz5HF2ctk2lv9gqYX4DaKbbZluHXBuf5Ilfv8qaqblUvVrC5RWHNJQQV9huMyKQvTQ1XPH9fvM0TerJXvymL5ykK5m9WpM5e5UYldg5kkcnDVo1EnGsYNXgRiVDvtF2XbdYZ2MrtcyVMLHHdkVCb4ejwfvn4yfkuJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف:
شرط ایران قوی وحدت حول محور ولایت است
🔹
در دورۀ سوم انقلاب، قوی شدن ایران موضوع اول است، بعد از شهادت سردار سلیمانی، امام شهید ما متمرکز بر ایران قوی بودند و به آن تأکید داشتند. در گام دوم انقلاب باید متمرکز بر این قوی شدن باشیم که یک شرط آن وحدت حول محور ولایت است.
🔹
ما مسئولان در درجۀ اول باید بسط ید برای ولایت فقیه ایجاد کنیم اگر می‌خواهیم ایران قوی داشته باشیم باید از این نقطه شروع شود.
🔹
ما جنگ را پیروز شدیم ولی باید پیروزی را تثبیت و ثبت کنیم و حتما کشور هم باید امید به آینده داشته باشد و چشم‌انداز آینده آن روشن باشد.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/453809" target="_blank">📅 09:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453802">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0ppQ2TlZxwl9RZjXH1xY9zfa6dPuOzkIRKEoYxlMNGTyb8TINimePZ-rLJMDFY7DB4Dc-pKZac0TEjXEicsNBKrJKQEqZSNb_W2d5xLQpdC95M4B_FiHt5dmc2riI_eKCHX53VWmjNEdi0ajNDl77GdDjOx2qcHhRWmNapc5nBrH8CODNmrDEFx36mC7mLsNTMIqkP2cOBPAp00Pt1D2cdT-snhhr8NX9EluHt_ZnPEaUoUFV3Xey7PdAg6uA7tYa_pVgKWxqK22ipJ6mXKircqXPSQJCQLfdVsxrFV7QbrQHGoVeMGaamWvxPQN-Vu4Phque-zlijlazC1QQlfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J85qqIHnaCyxmRTmKCCYuLfeuedbE-S8lZosURnw4YdzpgGAJNr8CpfgtYlKbMj6zo9kw7gue1ZxNsdRQTQXzjL4Z_L221wc970ZoLh8iupOVHfg5bIKOGpJnpydYkLiSx5cTzE-Vjprc6O1Kr4cY7CGcXYqXO_-dazb61aWsWlqK7ph4CLLuR5QXEbJkwp1HZgWlWPC45z7XShUfNQofLebxztPMUdHUfxt5Qzc4uTcA0HDDYvb1SazVZXCKXMKjTA5mCz9Vy94csRYRs8vDHZ6JArGMMTuYmaoIP9A7TTMAxGE8qXhN7Zs6Y2Rlyqhc1kTVVsOBmp3hXPYSH5mYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3GYH3rVtzOmY1p4ASR7LmsWufa-Vsl5ODnTm-cnMGi_VYepOveIFWu9D-nPjVyIpSIDA6lOFCEtN1YF2assPWtSgco8D6SvGRMUj17Zy3QFr0EWRA18glRbvIFDNk4BgO7zjlQ--IjECAl6bc-ayBbUUKn76jkrmIeO6G_58EdAsmXYUqDTEfP3jLUYPeL7ObVzHBfAk8QK-u6quRO3iVCLWy9gpjKULg4fI8mltgfN-y8Y56M5fAN-uuOAlp13l28Kpmo3i80OHiza6VY_3AEtxkpi1FbtKQh9sN5o7QsGqNQ2jbKBLlw6wG6od8ZNMhAoJZ1twbQ-LyomMMkC6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xq4hTXl-HkW9jzA9gu9E7HdLmslIMK_sDO3L8Z2KJWkDhMcZICdQHFytzHSqwZNdR1PWloKreUseBp-nt2EldxW1P5oFex4xZNjmCRBPZImk_tImttKjyb9aBTg8SAWY_sHKtcwJiEwK5gAPY9a4G6-1IwtF-tWtLgkTnuLmGeIN2GEKwJEYpbwTIDuJwCy7QFKtycrjb6SQNdVQCg-RbL6qyWqrcxXQ9UAcpZrLw40bAtYsnzUyGPA0WOWBjO9J4Qde5BNdAUD39hV0PFg_r3J1Pihn1tVerB-a17gUc_iR5SknQiDxqvD271FbxP3g8CZqGONi6ITmUwf0cDVP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7m2dcwuMrDEcQRs0uDCjL54T1gErBo5voRjcIgFQ3mY3e-HDUWhH0gBRRF6vN9Vx6BFMr1V64_nxUb8pzciWIo39E6rPazHbbm327rlwoFBe1g2k1wUa6tDwlFVUOxi2DnPi1WSwEfpROV298CtZhDsvIUn7Rloqr9EsG2zPgKGtiXAx6C8LZTuDqOzn77eT4LGKN9r9pZZ-zoS3LXPGYv9d-A9wRGvBt5Y5NpYdDh0NkOo6eSmIfOJ-vW0_1aY6ucYWxLqvHS4fZ_2QEaQI9RHBZWl3FI5PETscWR30cXil24IAImRBDuUV53YefXP53edxnSllJ1_mACqikYFpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvBO8-TZx39tyj8ODFGTVIcWCxnobM3Q9rOPJfgau8kz3FeIFGmdQLIF4ld5l4bm3ZGN89psbmiFjGfotYANbVd8x4gqAFX156P8SXq_14332GB_j_z6ns7nz1wGaGAITY0ri8wAvH2jcV4TC8tGUXzugQPzzVWBFCE2ys9eTmALWB8F2aRGFAm0qBq8qOlSHu-LhhU_aeAPSCuBE_A3r41Y9sm0cnkMUgRHICqGGS4hPeWoB2CpPOAJyIZVfND-TJAhWNZlKVc_1ivgeXcfHEB4lqJ_5M2X1xvkVOD1g0JwE-h0c-A3qBd_kFGaLZ7G-_dSY0qx8KBtYIrc6MWRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWeXtnyQTiJ2-2InJgMaMiiR79hnjK-zlMMrTr1qfBA9Ypvt5TmLTacjh5MGpSTKWgvR-S91sZBIa4DwoiFKf7Gq81DNfowu9rZO9TXv10DcS0RnBeyv8qdLwM-ejVOwN1hPxpsLR_uOeWNXjVaGg32E5YxRbqmH-pfnFL-v2ICR90jrVgz_Sb6hZ6k2yEEepgDi_8kFBUyvY2LfqmKD-Uo32NZZfxf69cSZBVQiG-sy5Oq3x2DBuwz5rGlh7KCyHb1h4SNBM-1MxwpnWFqa1bVNvR3SQZGfVHNHaIkZ2PYBsQjjjOlXEyVIdlwQl304K_duYI9x61wxOLfZpMLtSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
طریق‌الحسین با یاد و خون‌خواهی رهبر شهید
عکس: مهدی ایمانی
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/453802" target="_blank">📅 08:59 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
