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
<img src="https://cdn4.telesco.pe/file/mztGlRduPcyRrBtusGH3aFM4QE7rNKfGZjDoFiqsmdhof-GTreXVrleH02dbLeAXBcTbYvEsjpiMxAjY65qdRVzC-wy2tsPngoLZdkKBnpXg7XdOS0mRRJ-NHk0xXK_xETHnUYlFZ-isTGKtc2Wh9eDWZpkLSXcG22-QpOuVxWk--L5VaHLTLPS1x6yycXU-yLkpPIW-EG9sMSsCNa5cQYM4BQFn7rxxa8mfmHLbZGZH3hRUsCqrhnkHZrx6VCHnvyTAFFYrXSnUz3WfmY68Q2u1PgCNg7xC4nNW4Tj5Y6Il1Q4pCfuqpLZWlm9PeykVnWKxbaWe8TKM4CNFNzmTXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 936K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 14:39:06</div>
<hr>

<div class="tg-post" id="msg-130500">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وبسایت انگلیسی شبکه Aaj پاکستان امروز گزارش داد که شهباز شریف، نخست‌وزیر این کشور، سوم ژوئیه (جمعه ۱۲ تیر) به ایران سفر می‌کند تا در مراسم تشییع پیکر رهبر سابق ایران شرکت کند و پیام تسلیت دولت و مردم پاکستان را به مقام‌های ایرانی ابلاغ کند.
🔴
بر اساس این گزارش، شهباز شریف در جریان این سفر با مقام‌های ارشد ایران دیدار خواهد کرد و قرار است یک هیأت عالی‌رتبه او را همراهی کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/130500" target="_blank">📅 14:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130499">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
رئیس‌کل دادگستری تهران: حکم ضبط اموال ۲۰۰ همتی برای مؤسسهٔ مولی‌الموحدین صادر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/130499" target="_blank">📅 14:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130498">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
یک هواپیمای سوخت رسان آمریکایی از پایگاهی در انگلستان به بن گوریون آمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/130498" target="_blank">📅 14:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130497">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
الحدث: وزیر خارجهٔ ایران فردا به بغداد سفر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/130497" target="_blank">📅 14:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130496">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سخنگوی سازمان هواپیمایی کشوری: پروازهای تهران - دبی از ۱۰ تیرماه با مجوزهای سازمان هواپیمایی کشوری و همچنین سازمان هواپیمایی امارات برقرار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/130496" target="_blank">📅 14:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130495">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
شهباز شریف: آزادی دریانوردی یک کالای لوکس نیست بلکه ضرورتی مطلق برای کل جهان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/130495" target="_blank">📅 14:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130494">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb4f7a6ed.mp4?token=T5xPEoQhKgr8fS9uK-82PiJZW_wqyFLt88MdJD1ilZ9eK5YqM_rcfHMKYbXxshmwr0rpkwHPDeHIeBh1IgvHtvq7LocHVZMDArA9AEZS8exoDAyvVOK7IJ5si4hmpFp5_nfUEYU6GTeMYDc9IYZf-f32xP21RBBgmwXB8MBjKYfyHyQfph6WFzfSVvCA1QXG8URd75Vi6fASdcrUgoEtD7HTvRhKyeYFveRmrgXfvVGh1vTIF5OV3vEN732Y5Snn6MiXjtkkcfyu9lAL7sySLad54RU8zDTYJhJtoKtY79PWF9m6NqDY8sPpnz_3kdvyzteybc61pOrqdkxXC3i0sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb4f7a6ed.mp4?token=T5xPEoQhKgr8fS9uK-82PiJZW_wqyFLt88MdJD1ilZ9eK5YqM_rcfHMKYbXxshmwr0rpkwHPDeHIeBh1IgvHtvq7LocHVZMDArA9AEZS8exoDAyvVOK7IJ5si4hmpFp5_nfUEYU6GTeMYDc9IYZf-f32xP21RBBgmwXB8MBjKYfyHyQfph6WFzfSVvCA1QXG8URd75Vi6fASdcrUgoEtD7HTvRhKyeYFveRmrgXfvVGh1vTIF5OV3vEN732Y5Snn6MiXjtkkcfyu9lAL7sySLad54RU8zDTYJhJtoKtY79PWF9m6NqDY8sPpnz_3kdvyzteybc61pOrqdkxXC3i0sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سلیمی، نماینده مجلس: اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/130494" target="_blank">📅 14:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130493">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thh1rA7hU96kgavXh4AE78UuqyH5Za5mVPAV1HezuFyT-fGCi0mOU05JquzthRbu3EhOMDivu6G5Hg-80YTFwAXQdctfjohuxFnBS2XV-MdJjjirD_GGQJiOMlesq_yXuki2LMzwan4Lm23xm9_LTStd-osopsaovxupZg0eS1YIjz9N5PNgs3lQmChMqA0ch4UgXDomXVD3EkW90TrAqudYLiqu22P7QkslSeYcKEuClrMazZg9Bsc3oH6LsCJ24GJ2Ci7k3ZLPpvzLF5F85e-UMmUY2E_vttlyYweMKAHqmQux8i8EKTa-jsl4PeWIcI4XSvuxbFSnkm0gRaMoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حداقل 5 سوخت رسان آمریکایی در منطقه خلیج فارس فعالیت می کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/130493" target="_blank">📅 13:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
باهنر: اینکه عده‌ای جلوی وزارت خارجه تجمع کنند و بگویند چرا مذاکره می‌کنیم، قابل قبول نیست
🔴
کار‌ها تحت نظارت و رهنمود‌های رهبری پیش می‌روند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/130492" target="_blank">📅 13:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ3pgp5jgYpqiIiOGtsK2HFBr4ZVbW0zgqk7-JU3IMJXlHKtVw8a8sE3_v0cXMCiZS2Z3V-XvH-VbHuhNKzdrKzCalkEQGKd2lwSc_a3teuiFcUQ7JaO5p4xp5rhFdd5Aaz44J7_dwFj9tpcUhoAEcxx8ZLRVwY91cF4qm9fAAleq9go1jti3c4TQj0Qow1vo339jDUrBUZF37wOesRvq5GyeMfkufK4jT8Hjmz0Cx9162uI3DExPQl0ZdU3u-sKZ2n_jf1Gs5Fowe2sMrfZb3P73fUFHBZzuBP3C0n4PE9-ji9vphjOXIk8MaA92Du8MF8vBioNMr6-dELTKizj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی: پاسخ سریع و کوبنده‌ای در انتظار ناقضان تفاهم‌نامه است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/130491" target="_blank">📅 13:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130486">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/677cb04ce4.mp4?token=VUewZZ736eqRyHW7tI4LbrofQBhfdOrGiLRGpNaTrE38s3qtTuILkl-GrrGWchcpscfZDZyTb6iMTDTbgWyL-naOeUSP3jDl4irlP3XfqTxAJ9l3osTjzFMntKYWoWXKzxIuI22QKa-SABdapTfWt2KMFMk_yfkQTLZzbe9N542sFhmejq8ob7WlUB-7zoIj4pVLgsn8qR3WyUjwriwM3ZB8aAqrstjaZAf_wmUNW7SojXn3ibZPgHAkh73u6GorGE-obX-OFzoTbmPFAT9INgOjJDPkfry0kw5hpZcnUAKWapV08-Ea6BeS1hx6WA2pfrupnmd0KH-ALb8iRNCE4I_L-MYKJJxrPsdpHgw1eC6MLNN-HwAfPn1lxOHvO6tkWlRlghG2Qtw7WbrYV1PAd9yHEzY7i1ZUvqE5i7H2uxY-C2shNxOUCNRDd1ZnqL4vAG_2v48iwGj8jVEkVzixr63e9ZIK-1G-V7jTIFmGrWvfrqG95CsxL-h4oO1RZ-L8wG0zEIlAGLbu7_5cQ7CNLvlFHucYlHMjVk7478Yy4jeTFse6GjvMeOyuWzY2Y3ouWWWRcvJLGqhdN1rNC0dxI3OXPgCFkeUEnSQ4PAnq-sypv3cahWEzevLuKX94Q7JY9x7YN6EbbsXGcJvqfz5QRe80BXiiuyhH51AJItzZr3I" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/677cb04ce4.mp4?token=VUewZZ736eqRyHW7tI4LbrofQBhfdOrGiLRGpNaTrE38s3qtTuILkl-GrrGWchcpscfZDZyTb6iMTDTbgWyL-naOeUSP3jDl4irlP3XfqTxAJ9l3osTjzFMntKYWoWXKzxIuI22QKa-SABdapTfWt2KMFMk_yfkQTLZzbe9N542sFhmejq8ob7WlUB-7zoIj4pVLgsn8qR3WyUjwriwM3ZB8aAqrstjaZAf_wmUNW7SojXn3ibZPgHAkh73u6GorGE-obX-OFzoTbmPFAT9INgOjJDPkfry0kw5hpZcnUAKWapV08-Ea6BeS1hx6WA2pfrupnmd0KH-ALb8iRNCE4I_L-MYKJJxrPsdpHgw1eC6MLNN-HwAfPn1lxOHvO6tkWlRlghG2Qtw7WbrYV1PAd9yHEzY7i1ZUvqE5i7H2uxY-C2shNxOUCNRDd1ZnqL4vAG_2v48iwGj8jVEkVzixr63e9ZIK-1G-V7jTIFmGrWvfrqG95CsxL-h4oO1RZ-L8wG0zEIlAGLbu7_5cQ7CNLvlFHucYlHMjVk7478Yy4jeTFse6GjvMeOyuWzY2Y3ouWWWRcvJLGqhdN1rNC0dxI3OXPgCFkeUEnSQ4PAnq-sypv3cahWEzevLuKX94Q7JY9x7YN6EbbsXGcJvqfz5QRe80BXiiuyhH51AJItzZr3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز شنبه 6تیر 1405
تجمع بچه های دوازدهمی و یازدهمی جلوی سازمان سنجش تجمع کردن از ساعت 12به بعد و قراره تا ساعت 4ظهر جلوی سازمان سنجش تحصن کنن برای موافقت سازمان سنجش با تعویق امتحانات نهایی به بعد از اربعین چونکه سازمان سنجش مخالف تغییر تایم امتحانات نهایی و کنکور هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/130486" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130485">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnhdTIF4fFrV336Mo1kq3yHP807XXhZzQ-8i8e5OAzKxOLMQDSmuuV9NgIVlIweOe19qPp-Rt-NxmiDuUDmCpiy_k9Y_22O0yvGZcT6t4qBnC6NumEELzvF547blmcTJ9r7ntW5lusJ6yEBK3n8dxnSPzgg0ceaj9YN74FauyRY3uUcM-PFD0iC32sAbGwE6-k6aWuGptT47kaqxVF1aFlOychv26yrnR1X29hsdaBqopGlgWJSzQziiOYJY7tdH8ZAUGajbiUJt18Yf2Tw0GYJ-unZH8euZjZPvTZrj65emLPyo_8-zR58946FoBK5CDR96KfrB6GfEYznBo0OBUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مولوی عبدالحمید:ایران نباید سرنوشت خود را به لبنان گره بزند، گره زدن سرنوشت کشور و منافع آن به مسائل کشورهای دیگر با منافع ملی ایران سازگار نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/130485" target="_blank">📅 13:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130484">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
برقراری رسمی تجارت ایران و امارات پس از توقف چند ماهه به علت جنگ
🔴
معاون خدمات تجاری سازمان توسعه تجارت ایران از فعال‌سازی مجدد مراودات تجاری میان ایران و امارات از مسیر بندر جبل‌علی به عنوان یکی از مهمترین بنادر جنوب خلیج فارس خبر داد.
🔴
این بندر یکی از مهمترین بنادر ترانزیتی جنوبی کشور امارات با ایران است که عمده تجارت با ایران از این طریق انجام می شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/130484" target="_blank">📅 13:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130483">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
مقامات دریایی بریتانیا: یک نفتکش در تنگه هرمز مورد حمله یک پرتابه ناشناس قرار گرفته است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/130483" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130482">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
صدای انفجار در تنگه هرمز
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/130482" target="_blank">📅 13:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130481">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2if0Wou-VQLO2a3pumx-rexaL8M87-Gt4QTl39RExR10GLxs7UEGEDk0xm3P2Y6wmSShxZ2MYs-SVtPi5msCzjQh-6bmwtfLxOLdBANIzYH29M0hwqTSrFBmeGHP9gdm4cqyBxnpvxdNhBJgh6C0q5K2DhOCCRb1Z9DFuW0DoqINxp2yBM0kf6aiI8_RcBxLL4db1nk7N9aLjVg2JXI7jyG5zSDFz5MLH_VX3Hacf9sW4pVmtwm6e7zEWWpWiUJ4Yr7MDV6J8YzNhYtlp2Og70bme-tvn5xMiC_9fU6WbXNzguJqCkMjoQt_9nkRgk9HgmGiMhVy-lIUls2ZzEBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اردوغان: برای بقاء ترکیه با اسرائیل مقابله می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130481" target="_blank">📅 13:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130480">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
صدای انفجار در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/130480" target="_blank">📅 13:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130479">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سازمان مدیریت بحران: استان‌های آذربایجان‌غربی، آذربایجان‌شرقی، اردبیل، گیلان، مازندران، گلستان، سیستان‌وبلوچستان، کرمان و هرمزگان در معرض بارش‌های شدید و خطر سیلاب قرار دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130479" target="_blank">📅 13:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130478">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
منامه: ایران صبح امروز به بحرین حمله پهپادی داشت
🔴
وزارت خارجه بحرین این حملات را محکوم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130478" target="_blank">📅 12:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130477">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
حمیدرضا رستگار، رئیس اتاق اصناف تهران از تعیین نرخ های جدید نان در واحدهای یارانه‌ ای و آزادپز خبر داد و گفت: این نرخ ها از روز شنبه - ۶ تیر - اجرایی می شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130477" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130476">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ستاد مبارزه با مواد مخدر: رصد ماهواره‌ای کشت غیرقانونی مخدر از سال آینده راه میندازیم تا دیگه خشخاش نکارید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/130476" target="_blank">📅 12:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130475">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
المانیتور گزارش داد؛ عصبانیت در اسرائیل بر سر رویکرد ونس در مذاکرات با ایران
🔴
منبع نزدیک به نتانیاهو: ونس به آرامی دارد ما را به کیسه بوکس خود تبدیل می‌کند؛ آنچه اینجا اتفاق می‌افتد، پیروزی ونس بر چهره‌های طرفدار اسرائیل مانند مارکو روبیو است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130475" target="_blank">📅 12:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130474">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
منان رئیسی؛ نماینده مجلس: شماها از پشت‌پرده خبر ندارید ولی من خبر دارم.
🔴
یه شخصیت خیلی مهم تو جلسات به فرمانده‌های نظامی گفته بود اگه با آمریکا توافق نکنید؛ من استعفا میدم و میرم.
🔴
فرمانده‌ها هم سر یه دوراهی سخت گیر کرده بودن و اگه با نظر اون شخص مخالفت میکردن ممکن بود اون کنار بکشه و کشور وارد یه خلأ سیاسی بشه. آخرش هم بین بد و بدتر تصمیم گرفتن همون گزینه بد (توافق و آتش بس) رو انتخاب کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130474" target="_blank">📅 12:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130473">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رویترز: یک پهپاد اردوگاه یکی از گروه‌های مخالف کُرد ایرانی را در استان اربیل در شمال عراق هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130473" target="_blank">📅 12:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130472">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
دبیرکل شورای همکاری خلیج فارس گفت که موضوع اختصاص ۳۰۰ میلیارد دلار برای بازسازی ایران در جلسات بین وزیر امور خارجه آمریکا و وزرای کشورهای خلیج فارس در منامه مطرح نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130472" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130471">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ولودیمیر زلنسکی، رئیس‌جمهور اوکراین: با موشک‌های «فلامینگو» یک کارخانه تولید سلاح در منطقه ولگوگراد در عمق خاک روسیه را هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130471" target="_blank">📅 12:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130470">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=F9G_omQwlqhIvz0ecz6D62MbLEpG0WTAbx1viZKPr5d2ONKC6Wq7bpHWdOGz9C6db_OutwrBUWrjQVCc3tJ1h2Sp5YYKnAzzUSiR7OOqqxjEdOcspKvHELt8cAxu2F1QhjdoF0C6HG_dv2Cniq9iGDl3vbvjbSjC7R3a8cItBrVxw76x972BhkI61nAv0nB9wrjTyVxRAxhehzCoWJylAMUT5x0X3Ag2wOUfby2cLuMqjSyV5b0N27VaX5LWSXgpCajiUxxc9OUbQzYZWVt2vQ_nzgfQhDZUG9RmNhu0-L0mU0G0Pxh79IlCNo_ZmpbiF-2rnAm9YDmSfLNdm2jYkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=F9G_omQwlqhIvz0ecz6D62MbLEpG0WTAbx1viZKPr5d2ONKC6Wq7bpHWdOGz9C6db_OutwrBUWrjQVCc3tJ1h2Sp5YYKnAzzUSiR7OOqqxjEdOcspKvHELt8cAxu2F1QhjdoF0C6HG_dv2Cniq9iGDl3vbvjbSjC7R3a8cItBrVxw76x972BhkI61nAv0nB9wrjTyVxRAxhehzCoWJylAMUT5x0X3Ag2wOUfby2cLuMqjSyV5b0N27VaX5LWSXgpCajiUxxc9OUbQzYZWVt2vQ_nzgfQhDZUG9RmNhu0-L0mU0G0Pxh79IlCNo_ZmpbiF-2rnAm9YDmSfLNdm2jYkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130470" target="_blank">📅 11:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130469">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
صحن علنی مجلس هفته پس از تشییع پیکر آیت الله خامنه ای برگزار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130469" target="_blank">📅 11:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130468">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkBp2CicbLbzlWiOIUnOBa08Ujs4HLUgFXtJhGngFmg680apaIa11ikZbXt9B67wG7Jqn8H5XdXOYHS9pOCoRom0Ninrb0QvS11YNtCTXepLU-yAxDM6sby8G431rZYKpKyeuJQz8GZ5L-37P_9-8v5KlWaflUzx3hP_au9D0WtcPnsspCEdA4e1MarOW5RRo7sSCr79xHaB8-fz_IhX5hKDz5bq1xXYfIbuYkl5eErXngB1N41Is0qH9xMdkpzUPfN_B4D8UfCCeVNNEIm1B8qCA-87GG7kx9K8pVFtIiidiz7v0PqwKbEKZJNKrB3y2Q0aj9uFbWgTPPUxCpTEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم استان های بالای 100 درصد:
▪
آذربایجان غربی: 106 درصد
▪
ایلام: 114 درصد
▪
چهارمحال و بختیاری: 103 درصد
▪
خراسان شمالی: 103 درصد
▪
کردستان: 111 درصد
▪
کرمانشاه: 105 درصد
▪
کهگیلویه و بویراحمد: 100 درصد
▪
گلستان: 103 درصد
▪
لرستان: 109 درصد
▪
مرکزی: 101 درصد
▪
هرمزگان: 101 درصد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/130468" target="_blank">📅 11:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130467">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh8LfW09T9o-azPlUdys9xtrD9kpgIYuPvzkAxCqTAnoxQwowAqcYYEUZHEST15zA9p9hWF4M0tbE2GqxSz63eH-WjxIo7Z374m7DHX3vGSvhXTp3a-vCRn-Mt_vX7tlYn2J2-F5euL6ZUmnxOknlSVKP0Sj3ukh5Nx86VNFFFbM0XwdBmEu5S1bWElFdm9389cVcMnTTmO-DJLS4u8jqedIf7sx0TSMyRC3q-Th9mGVa5OaOkTHILIhTP1CqvxPR5Nyla8O_E2KvxmJZEuQ_FMybUvEyxsbTXZxfaW5Okczr1__uejIkCOYUQJ0dyg9Gy5VDb13JOKiM_A8rgTLkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره جان بولتون: جان بولتون، نماینده سابق بسیار احمق، نامتعادل و بی‌مهارت ایالات متحده آمریکا، به تازگی به گناه خود اعتراف کرده!
🔴
او فردی وحشتناک، دیوانه‌ای است که فقط می‌خواست دردسر و جنگ راه بیندازد و هر جا که می‌رفت، بی‌جهت مرگ و ویرانی را به ارمغان می‌آورد
🔴
امیدواریم با او به شدت برخورد شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130467" target="_blank">📅 11:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130466">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
با وجود اعلام برخی بانک‌ها مبنی بر رفع مشکلات، گزارش‌های مردمی‌همچنان از ادامه اختلال در خدماتی مانند کارت‌به‌کارت و دسترسی به حساب‌های بانکی حکایت دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130466" target="_blank">📅 11:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130465">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbf31c890a.mp4?token=q2pNqKuKzz8SNoA_cqR0LXTmxzOrNrunBFFet3zh_wsY7rTZaMshRAY6UYMR977sSgU1eOn_95eeJl0NbsHtzv0RZvnO_y-Cw2lx1kuI16Dmrbkg4IspCNzhr5upKWKN2UNGnTdT7wpuTNWDhMIF3kD-dX0UAp62A9RtvOMa_NEBx9N31sb_RsjatA0vUDKgCuxjJXudo_fHiDFwbAt21wVEERrnV-ixIcJrA6UQYT854rRnTZAm6XC3KPdYMtWcA_RLSXfnCibxJ1YToQbGsYeT75nm63H3CLOm0FAJ1oEo712KlZL6J1zx-eEwcmm9ngcQCwZuSHNbqIa3du8Zeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbf31c890a.mp4?token=q2pNqKuKzz8SNoA_cqR0LXTmxzOrNrunBFFet3zh_wsY7rTZaMshRAY6UYMR977sSgU1eOn_95eeJl0NbsHtzv0RZvnO_y-Cw2lx1kuI16Dmrbkg4IspCNzhr5upKWKN2UNGnTdT7wpuTNWDhMIF3kD-dX0UAp62A9RtvOMa_NEBx9N31sb_RsjatA0vUDKgCuxjJXudo_fHiDFwbAt21wVEERrnV-ixIcJrA6UQYT854rRnTZAm6XC3KPdYMtWcA_RLSXfnCibxJ1YToQbGsYeT75nm63H3CLOm0FAJ1oEo712KlZL6J1zx-eEwcmm9ngcQCwZuSHNbqIa3du8Zeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفته!
🔴
کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130465" target="_blank">📅 11:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130464">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سازمان حمایت: قیمت جدید خودروساز اصلاح نمی‌شود !
🔴
در شرایطی قائم‌مقام وزیر صمت با اعلام مخالفت این وزارتخانه با افزایش قیمت اخیر خودروساز، خواستار حذف نرخ‌های جدید از سایت‌ فروش شده که سازمان حمایت به‌عنوان مرجع قیمت‌گذار در توضیح اظهارات این مقام وزارت صمت اعلام کرد که «منظور قائم‌مقام وزیر صمت از اظهارات اخیر، اصلاح شیوه قیمت‌گذاری خودرو بوده و این سخنان به معنای اصلاح قیمت‌های اخیر ایران‌خودرو نیست.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130464" target="_blank">📅 11:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130463">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: ارتش اسرائیل بخشی از نیروهای رزمی مستقر در جنوب لبنان را خارج خواهد کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130463" target="_blank">📅 11:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130462">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2rHbfB8rgVFh0LkooK3E7_tA8WiO2JIOmODAvMzaNbp8l_7cu38UnptpWdSajwVAwAv5ArGIG3k5aXVSyrfhPvJuYciSdFuLH88_wulawaBlCFalCaA2xG12E4GMZ_TjLhiDveOZTcndMeczUYt8favFbHC-RCLiMVxzfeoeRAo6HEF6vYBj4WfuEh8qWc4JPMtz7Y812VttTVLm1uUrTygywcktKnLtz9yd2-EgXcMe6hzeLusacMAwn2-zfzImkuuwroUfnB_HseMhuRupMsXQGpMseUil19sA_cYIjSd8QvEPtPJKIa0pSUDui5MO7ca0ByD8l4xn_Z4APNRgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: بعد از حمله دیشب، هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود
🔴
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130462" target="_blank">📅 11:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130460">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULFCw38VcYOSH1bicGLgCA4k1mxbk1j_gPBJVMLGlWI2-U7NkJMtWTmfaJMEOb3-SylGLQGGuN71cfDANPcQ6mfsUdbVMU7rnY8DrwBE-13LMrGQM2yuUdHhWdhuHj97zJXQeoDb9NQZOf4DqRlVPwZoBm6VHk4sSfXATjD-Bsma_VKqHi_9zqO-p2P_qQWiPFMRoUzl_O7s_7oF3TjIv3DjLO41dei3h_DNGdquCy61yAsY395sfxK8z8u-2PqSPt4b8fzwaWEcnubVz3kq-h67iBlJQtVv7JoFlptIRu3bT7sOkvOmLnCG83xGl7qTWUv3-00EdLU1Ypf_EKhuqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq65GUsDnpC2S-WgshvHqnJavG6fAMYJ4XugpRXKP4blfqH81t_zC4tAhP_1uuK_5BlEhP-CkTCNxeh8TUdDGYxRprCy9H40nhhGVa_zjOVMHCwTRwCkR53QRyQI9xXL3KY83jH9g0I1N494sPn3iT1Wgw-TY_KEX2qJehOMW6E6zlvE0IzuxmwV23O6fHsrvGai3ERyO9zawESvNSAJOhp2Xj20SCkbc1I01ypkjOKVe4Yv0NBL2O03N309PRJuHRxZfGLBDqKN_JAutQ9CHZvCNLxLty9PcrrLvMw-O87nXkeKuVYuDDPF_0EpuWknqRTwm5qrhzrj6z3duekPig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شباهت عجیب سرمربی مصر به یکی از کائنان معبد آمون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130460" target="_blank">📅 11:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130459">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/806fc925bb.mp4?token=IMdz2TsQZ96wrKqbzPOOZbfDGjE95LzU5s40tO8PTwiSoTH4nKOX6J_PvPgz3TAo58mej9xkhyFtQi4zFTQvIWU7mDV3YJiepNkuKaxsTQFVozhtgpW9aJy06t0G7w9z23j9UxVjMOT7t0HreFYOf9ghOvmKDj14s5E3hjtMoDvfK-TBktzbdSgZALqEZNFtZ1UjGw0FxWC7igozwRp28n-l6ivrF7_cgY7w6l5HlQyOrWp4hquMXnYKKc9kryT1tFhbnm-yCb9h2xHxjhureiBNSho0VUKzHCxrurkbCs0MZhFmpElpOptfI0tXIff27Wm_D3Wbwx6_eH0b1pIXTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/806fc925bb.mp4?token=IMdz2TsQZ96wrKqbzPOOZbfDGjE95LzU5s40tO8PTwiSoTH4nKOX6J_PvPgz3TAo58mej9xkhyFtQi4zFTQvIWU7mDV3YJiepNkuKaxsTQFVozhtgpW9aJy06t0G7w9z23j9UxVjMOT7t0HreFYOf9ghOvmKDj14s5E3hjtMoDvfK-TBktzbdSgZALqEZNFtZ1UjGw0FxWC7igozwRp28n-l6ivrF7_cgY7w6l5HlQyOrWp4hquMXnYKKc9kryT1tFhbnm-yCb9h2xHxjhureiBNSho0VUKzHCxrurkbCs0MZhFmpElpOptfI0tXIff27Wm_D3Wbwx6_eH0b1pIXTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام ویدئویی از حملات دیشب به ایران را منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130459" target="_blank">📅 11:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130458">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزارت خارجه ایران مدعی شد آمریکا با هدف قرار دادن چند نقطه در سواحل جنوبی این کشور، مفاد یادداشت تفاهم را نقض کرده است.
🔴
این وزارتخانه همچنین اعلام کرد حملات ایران ماهیتی «دفاعی» داشته و مواضع مرتبط با نیروهای آمریکایی را هدف گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130458" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130456">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8NuMdWoGvXk_McXhSK-G_ZCqWUAoNeDoVVo3Dy3RSttgyHCKC8z03FBRAQRMXFPJUbvPXhCyU5DCMbLV0PF33Pcx466tI0abIEBIxeI2eEX6kzxtY7FzDOTrjzzROWbOfU_mZsDoiniip398G_kgj7GkLpC_uz2ViVLOs-zRp4tiAxYEO5ZhVqC7psCertovGsyzLj9O0-Y6omNwN0M6klnZB70sw5Ubfa4qY9QoPgFoHHClSDEcHfD8jaqsqYusPRjQ_GlwIvj4KOfIqFe7TafrOtxUYZ14y5L486_S1308POMi8dXdqi2oNv7sYoMLrGV0UcrQib_RRImdGCNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHndB_jbEdMWQQz3LEVSMsnePxxmbEZ0hKKPsmvx6Kxa3v1-EUqbVSVS6o9zvm0NNdQBJhpC6VfebVJSAj3advhziMkCS7cVKmTXOjaH0A4AAPd2aqpawE4CUep2y-EDhv1-7PYnUzGfOb74zTwGrrRhJDsJkjpZoYVrNYdTwH10Tq95jkWDK1pSoYvLB4Hfplkbm6m263nqZIQRj7WlIZdXHM1GF0Q46EL9xt5c9ypQlD-ddVzGB1rMmz70hwWCUbHnruPiCtB89RhAJtpMllbdKclcL6SSYdtys4kQ688rffwsAUPaRPGD3ykUpRfIgOfTvizxe0uLqfYClAuoWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شانس ۹۲ درصدی ایران برای صعود از نگاه سایت اتلتیک و ۸۵ درصدی از نگاه سایت اپتا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130456" target="_blank">📅 10:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130455">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
خبرگزاری ملی لبنان (NNA) گزارش داده است که نیروهای اسرائیلی بامداد امروز اطراف شهر مرقبا را که در فاصله حدود ۱٫۵ کیلومتری (یک مایلی) از مرز لبنان و اسرائیل قرار دارد، بمباران کرده‌اند.
🔴
این گزارش پس از آن منتشر شد که اسرائیل و لبنان در واشنگتن یک «توافق چارچوبی» را امضا کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130455" target="_blank">📅 10:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130454">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q30sMcoL0pBtE7iupjoRAZ_WJ2uuNPmEZ4i7b1S1UhTBaujc8YQB4lhFqjwGhATI8WkK3fHpyJkajkr_Hchfr1KmqxgqkAm9Of8XG0nPMo2sxQH6m_BCeMsttXasqADWJGIo9ORUuqvWC04mS6Px48GHMHbQJ0Eftm7OMuW-mpYLKYWv0j5OglLlDMCbM1BYpImNWufYCjmClqT87N_LbEsPkHgYBFc2wSwgKL5xdvNLYR_Tl1no10IO75zfoSbkuBsfkLmBkID0PWS0iuy9cLT7S5f5moKBjPXR_PBJnxdveMDuUt1x3dm34xMiLCCw8mURgYbuWPhupWjTpTiGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده دیشب به انبار پهپادی در جنوب کشور حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/130454" target="_blank">📅 10:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130453">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
به گفته مدیر بنادر شرق هرمزگان، پس از حمله آمریکا در اواخر روز جمعه، هیچ خسارتی در بندر سیریک در جنوب ایران گزارش نشده است.
🔴
این مقام مسئول با بیان اینکه این بندر به طور کامل عملیاتی است و هیچ آسیبی به تأسیسات یا تجهیزات آن وارد نشده است، افزود: وضعیت در بندر سیریک عادی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130453" target="_blank">📅 10:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130452">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: ارتش اسرائیل بخشی از نیروهای رزمی مستقر در جنوب لبنان را خارج خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130452" target="_blank">📅 10:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130451">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozJZTxz4CH7-LZzKqVfs7cDY08DxoxuKVlV7L5LOUD25ZnGRkgO1AY640F-wW1cyz_rgLViD8BhhtTXm9BVvV7v2LOFf8F08eKlmKrS7Ow7NMa1ORRxqNkHZTCVPBxL4XxTqe68ucHpSG_VSdgu177PltV3ytIvXrGxFaVqhZcpFXJOhD7JPQD9HtqLEwwLqY9aURQb3hfGa-OQDuO8i_xsD_5S2VKPuR_PTB8eHaU9A6duLvrZk1vWxPcj6M6DMKzLp-y6EcB7pvSGrKO6VOvOLoBtQ9TrszarKkYDsx9vAkwjbHeYGvs4_DiF0rb7Xpk9atbpzOewD6DHNNJVD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز آمار:‌ تورم نقطه به نقطه خرداد ماه به ۸۸.۶ درصد رسید
🔴
تورم مناطق روستایی در خرداد ماه نیز به ۱۰۸ درصد رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130451" target="_blank">📅 10:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130450">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DG4RdHq3cPmTxz7BW_pZjugOn-Fd9LM0IgrGKsltrCaXMV5Zb3JHBRm3JYOdI3Ml6gPT8cjSmTJcL4iWVEcsawVLLyJC2jyT6QyyGf9XT62Ez3-Oo0phBPEmObywqiLGsp5QfC_VG2nXtQou7zfEtemFuO2O4mMncdjuMUgyY5B0a6gn3U0AoG544Cawi5OsBR_7hpWbbA9gaJqWlOg4yTx8RVO60TakNqMgfN-aWLGpqDgEgBjY6AXG7Bq2pSoexsrBX3r4Pr9gjIHP9oF44NdNBD3EZS9n--mKbNxnYI0DmUByN0LVH9riBHFyf1bXnZjCBriU-gv7BkokiRzOag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش آمریکا با قراردادی به ارزش 36 میلیارد دلار خط تولید موشک های رهگیر THAAD را 4 برابر کرد
🔴
این قرارداد در ژانویه سال جاری امضا شده است و بزودی لاکهید مارتین آن را اجرا خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130450" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130449">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3293127d1f.mp4?token=aHwKoW0kZItrlpnXJOHby21O1-MU6lx2YpT4vAn2nybQlG8_0A0KmVbKMeBaF0a8GBn9VLwGG6Pm5dZyQfjN2G57HBfkjDSSYP1N1kyAd1_JxjaruaZ5EgCS1re3E4Qxa3m5eFYtNw4c4TyaoDP3b90rIra6ErbtRilUf2XJSRp01S38rmFuOFhm9kXtZfwEb2PU6Qef7T7ulbu3LjAsixSLrN-D84FI4IG-vAq1anyYTAknLWeAbVdIDBFh7iCK2wzJvzMmIaFEk0IcAC7EwuAOHq8iwTTXjNwUCooMg-ws8V9NRiIOP7TCZMh2qXOSCzr2_h_fs9R2aOBNejSqEol6UfYCM6NiCHFXHwoq-G1jVmm1gcDZN0hMPjkuyevMqQ-pC1CWpE2Ix8oRcQexO0cvCeMuaiGkSfWz2jAT44fV7aXE_c_ogZIeeQHf7nyrjPQL-27CaEcwCYI41MkoXJIOr32DNNktxy1JR78gGG5fgSRyuLqyap8yP7XyXY0sgMvJLfPVe35y-XBFfK0zeDEw54FxQA1uUjiGDvdR1Tskg7epwqLYsrKrqPktQ6ENkV-WGUYp6DYP0tfeBYArvwROd0M_B1-hQz1FXf7YVmfOge0Q3Y0E3Gfn0RTzAp88OR2wAo2jbyKuD19PpRAxzrGwzYSxOBOwxgYcYCXZdjs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3293127d1f.mp4?token=aHwKoW0kZItrlpnXJOHby21O1-MU6lx2YpT4vAn2nybQlG8_0A0KmVbKMeBaF0a8GBn9VLwGG6Pm5dZyQfjN2G57HBfkjDSSYP1N1kyAd1_JxjaruaZ5EgCS1re3E4Qxa3m5eFYtNw4c4TyaoDP3b90rIra6ErbtRilUf2XJSRp01S38rmFuOFhm9kXtZfwEb2PU6Qef7T7ulbu3LjAsixSLrN-D84FI4IG-vAq1anyYTAknLWeAbVdIDBFh7iCK2wzJvzMmIaFEk0IcAC7EwuAOHq8iwTTXjNwUCooMg-ws8V9NRiIOP7TCZMh2qXOSCzr2_h_fs9R2aOBNejSqEol6UfYCM6NiCHFXHwoq-G1jVmm1gcDZN0hMPjkuyevMqQ-pC1CWpE2Ix8oRcQexO0cvCeMuaiGkSfWz2jAT44fV7aXE_c_ogZIeeQHf7nyrjPQL-27CaEcwCYI41MkoXJIOr32DNNktxy1JR78gGG5fgSRyuLqyap8yP7XyXY0sgMvJLfPVe35y-XBFfK0zeDEw54FxQA1uUjiGDvdR1Tskg7epwqLYsrKrqPktQ6ENkV-WGUYp6DYP0tfeBYArvwROd0M_B1-hQz1FXf7YVmfOge0Q3Y0E3Gfn0RTzAp88OR2wAo2jbyKuD19PpRAxzrGwzYSxOBOwxgYcYCXZdjs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیل ماهر: برنامه هسته‌ای ایران نابود نشده است.
🔴
جی دی ونس: کدام بخش نابود نشده است؟
🔴
ماهر: ما به آنجا نرفتیم. کل ماجرا این بود که باید به آنجا می‌رفتیم و بررسی می‌کردیم؛ در غیر این صورت، این کار را نمی‌کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130449" target="_blank">📅 10:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130448">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
پی‌بی‌اس (PBS News) به نقل از یک مقام آمریکایی: ۶ فروند هواپیمای نظامی ایالات متحده، چهار هدف ایرانی از جمله تأسیسات راداری و انبارهای موشک و پهپاد را در منطقهٔ سیریک در ایران مورد حمله قرار داده‌اند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130448" target="_blank">📅 10:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130447">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
مرکز لرزه‌نگاری اروپایی مدیترانه: زمین‌لرزه‌ای به بزرگی 5.4 پاکستان را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130447" target="_blank">📅 09:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130446">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
صدای انفجار در دزفول ناشی از امحای مهمات است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130446" target="_blank">📅 09:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130445">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
شاخص بورس تهران با رشد ۵۰ هزار واحدی به تراز ۵ میلیون و ۲۱۱ هزار واحد  صعود کرد.
🔴
۶۲ درصد نمادهای بازار سبزپوش است.
🔴
در حالی که ۸.۳ میلیارد تومان به سهام، حق تقدم‌ها و صندوق‌های سهامی وارد شده، ۱۵۴۴ میلیارد تومان از صندوق‌های درآمد ثابت خارج شده است .
🔴
دو روز کاری پایانی هفته گذشته بیش از ۱۱ همت وارد صندوق‌های درآمد ثابت شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130445" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130444">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
شمار قربانیان زمین‌لرزه ونزوئلا به ۹۲۰ نفر افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130444" target="_blank">📅 09:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130443">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f4d96d2d.mp4?token=jRsbv92lKRlrqBz1HbMJyk3z1n-LpGcORFaYAy7TyFaA3ePssvwpSlcdXiG53A8trUAsF2bi_n5GX8oA5XHBRAwkkA-e6KOf8-zpKDTzZm79Asl-P2iL4YlBKKLWLW0zOdUfP3AimiBVocp4Qp96ehDoqONGD-VMIzKe-txyWsk6iuTEPZvAU8y9UDz4HZWPR903sRH3RJaZydy_bZsi_TxDnFZGIV5On1s1wPbxxEcYCmElHFdrB3IYt9c7Bxu1R7BPo2MyczPMscG6ZbyG7iExA9Shj4f1fx3nWaSZPDra4lwiNmddkXdxFaRoHvf4tOSrSRRU0mWfHsnb9tml_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f4d96d2d.mp4?token=jRsbv92lKRlrqBz1HbMJyk3z1n-LpGcORFaYAy7TyFaA3ePssvwpSlcdXiG53A8trUAsF2bi_n5GX8oA5XHBRAwkkA-e6KOf8-zpKDTzZm79Asl-P2iL4YlBKKLWLW0zOdUfP3AimiBVocp4Qp96ehDoqONGD-VMIzKe-txyWsk6iuTEPZvAU8y9UDz4HZWPR903sRH3RJaZydy_bZsi_TxDnFZGIV5On1s1wPbxxEcYCmElHFdrB3IYt9c7Bxu1R7BPo2MyczPMscG6ZbyG7iExA9Shj4f1fx3nWaSZPDra4lwiNmddkXdxFaRoHvf4tOSrSRRU0mWfHsnb9tml_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قلعه نویی: اینم یه ازمایشه؛خدا داره منو میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/130443" target="_blank">📅 09:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130442">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qjs94HmXk9gw1pAzNEKA0KNa14HvSMcgaS88dLRPttwqrKAFFVtnFkEvSIBIkXnO-kCy5Idx_zq_DccTNSNDF_8ectbdjcgmUtJzXPUXyd6_Q9sjCL6vHosj4Ft9iAHxlmT389RLh3xbbzH6zo42uN-4h9ljph1-8Im_C1sKyvJPlSO00iqBg6lULb__VM9nyenryzcMm_4NhshbKfzfYfQWuBpUR-je3jnZ87Nz20LjD29pZDrrss0pYhXjiIKfCeWkn-Mta7itNkAg_UPOYpSujWhZKefZwmP2SFidti33VWvN_BxR30lYSgWqK2BioMaxYDtRVRxkfEb_VNxxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری سردار آزمون پس از تساوی ایران و مصر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/130442" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130441">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفتگو با نیویورک تایمز: حملات علیه ایران به معنای از سرگیری عملیات نظامی گسترده و جنگ نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/130441" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130440">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
قوه قضائیه: موتورسواری زنان منع شرعی ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/130440" target="_blank">📅 08:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130438">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2gsCYVtKDBcbkROQDV7p2nkTXDTjoYB85J2nIKpwQ96QBYXjhZCqT41u7D9oVcqW2r8C7WVLvToOtg7-qfjj5UkwT0BfJGih5VWRfpSkGH37gyqTdtqnPLDTBweBuhb7Zdc_2cchKFxmUA20XJrWoobJ6hU-_c8A3FieZUrGnrt4d7IfHPhQ0MzTOjVI0gdcCb7dAo9s4ScqCZJ0hICRMAaIQpZTYN9-HZkdsRpHlcS-DJ6futht9NV4AJYLmtPdEeTUGa3pW4a_ln6nnqnIJiXs4FvjFPVT8QY12_DKMPmqzNg-vU5NsFcCeYJ5vaggsGcIIjw-oN6LnACUX0KPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ونس:
ایران توافق آتش‌بس را امضا کرده است. ما به آن احترام گذاشته‌ایم. اگر آنها در مورد نحوه اجرای تفاهم‌نامه اختلاف نظر دارند، می‌توانند تلفن را بردارند.
🔴
اما خشونت با خشونت پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/130438" target="_blank">📅 02:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130437">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی: حملات آمریکا حدود ۹۰ دقیقه ادامه داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/130437" target="_blank">📅 02:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130436">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXWDduVrkewAnqEyMNHIys__kH7t9dSFsA6UEeYbbigP7Io_J5ieN755hUC_Vj8woYakICbGjP79aYBYeCFouru-TC6drbn7lFCc5YMy_6ZSImrtbRmZT4NohzWYG0WFmnq8iTqtkv5F7VJyuwlIWZ7nnlbJEC_EXqxrdwvaNOYhRJzOU2qEHAfxBJG19KIwwChD48hgJ-S5T3ojgb8qWPINszIz-Y0svo7VbW-z3fXWkN1AE4dZWoCbIfbRCG-CWsdyro41_mqXaNh-CD4tayyhh6f4nuv-LB26rB2i5c23-TMx2eVCIEqgu09oaJDIBwesZSryBHPQj057HIv4eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی از ترس خوارج مجبوری خودتو قایم کنی.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/130436" target="_blank">📅 02:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130435">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ ۚ
🔴
به دنبال نقض آتش‌بس رژیم صهیونیستی در جنوب لبنان، ساعاتی پیش رژیم پیمان‌شکن آمریکا نیز مانند همیشه دست به نقض تعهدات خود زد و به بهانه‌های مختلف از تردد یک کشتی متخلف از مسیر غیرمجاز در تنگه هرمز به حمله هوایی به سواحل جمهوری اسلامی ایران اقدام کرد.
🔴
نیروی دریایی سپاه پاسداران انقلاب اسلامی در پاسخ به این تجاوز نقاط استقرار ارتش ترورستی آمریکا در منطقه را مورد اصابت قرار داد.
🔴
بر اساس بند ۵ تفاهم نامه اسلام آباد ترتیبات کنترل عبور و مرور در تنگه هرمز با جمهوری اسلامی ایران است؛ لکن آمریکا با تحریک جهات مختلف در صدد تخلف از این تعهد بود که پاسخ لازم داده شد و من بعد چنین خواهد بود. در صورت تکرار تجاوز، پاسخ ما گسترده‌تر از این خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/130435" target="_blank">📅 02:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130434">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ونس: خشونت با خشونت پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/130434" target="_blank">📅 01:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130433">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فارس: سپاه فعلا نگفته به آمریکا پاسخ میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/130433" target="_blank">📅 01:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130430">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U70QlL27dYWCpw6jbzc-pamJ0AarFrNMlxd7SJfVpnmokM0NqHxp2I4XFvSh_f1aak7WU0NdqUiIIJcjcNXrFZkKZ0qXIkeZk2aJUIL8iE3POObphhFE4lCMgvFO-gt4C4CaKhxwwl2p3N_NCkoX3XrCGAqginTGugDw7L8op_ovsKKo576ig0UG32r2AeBrZ1P1eIdnAavdUfdG2QKmqEBXx8TzL8E5Eyx4izm9lgJyylCPi91LRXQH70eVwp1tVWbguui9y_Q9kepPzIaVDUueaZsrBCfHtFpOwkgCqFkSXdBAjO8dExGstLQgT91YdH1NshCUQmPxf0gae16q4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1bf794007.mp4?token=OKpzUATexcUpx8jDZ8n4ijOKOc8kpNZmNPHvJXwb7OTAgKpxULKB4J4M3hOI45gp72cURnOppeGJJpFfWKnqHH01L-U4hLlHxBBNoNA6VNC1bLiASd4H569EHXn-m6UvV81VFLMlZzesD0JA9gzi1pnspHjrO4SIQfBXxljQV3NiIyhy_TF0z5OFhJRQDr5QRVF64xW9uAriUqfqiE4FDwyn1LVWpNEoqdCB5b6I8LoL8UK-E5dnO7ToWgELm8FmEIp-mWK2ZppB7cGehQoQVTz8oEDjOxqjHiNr-DlO4f_1i0aWS3N5CymOptQ-UIo1jtOUWZuc0O9sRUfmaJmjig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1bf794007.mp4?token=OKpzUATexcUpx8jDZ8n4ijOKOc8kpNZmNPHvJXwb7OTAgKpxULKB4J4M3hOI45gp72cURnOppeGJJpFfWKnqHH01L-U4hLlHxBBNoNA6VNC1bLiASd4H569EHXn-m6UvV81VFLMlZzesD0JA9gzi1pnspHjrO4SIQfBXxljQV3NiIyhy_TF0z5OFhJRQDr5QRVF64xW9uAriUqfqiE4FDwyn1LVWpNEoqdCB5b6I8LoL8UK-E5dnO7ToWgELm8FmEIp-mWK2ZppB7cGehQoQVTz8oEDjOxqjHiNr-DlO4f_1i0aWS3N5CymOptQ-UIo1jtOUWZuc0O9sRUfmaJmjig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرکوب اغتشاشات در لبنان شروع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/130430" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130429">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
برخی منابع عربی در خبری فوری از آماده‌باش در پایگاه‌های آمریکا در بحرین، کویت، قطر و عربستان خبر داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/130429" target="_blank">📅 01:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130428">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رئیس جمهور لبنان:
اغتشاشگر را باید سرجایش نشاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/130428" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130427">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0-rPIps_OY1Oy4iaP2EIAHtuhvF-psQMMT7Ft1wtENAa7UxfFMJUvvqNBt7gVfNgsvolh8ksn6KKQzzwu8jUpNgu4owCttUt4Th8ScNllZZZ20AkQbgHA-oO05CKdpNyfoQXploMWlEJ8--5luq08E3E9n-iFWJkQQ6kpDLi0lkiNSvR-IXrOIClfZvQ_q_PyOAQpHWslIEd8eJIAjRIwmxxD8iBz-IQsw8Uf3j1-xjL4tUhtFpbkNEay5p6tQ1e_PKG-WsvURf9DTMJQGpER-mD74QLhvit_SE6BKpUWRK2kA2k4AWOKY8jHpj9o_ehAGTvCnRv63lmKash7vu5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای ارتش لبنان برای سرکوب اغتشاشات وارد عمل شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/130427" target="_blank">📅 00:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130425">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c12144a38.mp4?token=fm8siUt83P-Yx_2Ck78Cf96kTxLPkasPC-7i52FYAwFSncXfdDfllhjKvbeO7ZVlN26EYvpvX2gcQcc8LevKwFHSkw9eki6fO0rYWWSwLypBkfinn5cFFQorUfQpFmMSycely6QaMHqJROjn8PgQcH5JLt53iTR7j_KVRVXop9YYd08rI0HY_rUFaoLdXQAQ0WR8W-L8F63x-Ti-TO04IL7gv0p-hdoghaW8GlCm92E8hguJrtIh240JYv4Zld3DyKKXtJ_ZYYpds5fC0kEWsEbFi3zbPACqn9x9B3dEQsYFeqpYwf9ZaGDzSiVA5lPtzXyAdPvS6m843E1OlSDI4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c12144a38.mp4?token=fm8siUt83P-Yx_2Ck78Cf96kTxLPkasPC-7i52FYAwFSncXfdDfllhjKvbeO7ZVlN26EYvpvX2gcQcc8LevKwFHSkw9eki6fO0rYWWSwLypBkfinn5cFFQorUfQpFmMSycely6QaMHqJROjn8PgQcH5JLt53iTR7j_KVRVXop9YYd08rI0HY_rUFaoLdXQAQ0WR8W-L8F63x-Ti-TO04IL7gv0p-hdoghaW8GlCm92E8hguJrtIh240JYv4Zld3DyKKXtJ_ZYYpds5fC0kEWsEbFi3zbPACqn9x9B3dEQsYFeqpYwf9ZaGDzSiVA5lPtzXyAdPvS6m843E1OlSDI4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از اغتشاشات در لبنان
🔴
اغتشاشگران اموال عمومی را آتش زدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/alonews/130425" target="_blank">📅 00:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130424">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ارتش لبنان به سمت اغتشاشگران در جاده فرودگاه بیروت گاز اشک‌آور پرتاب می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/130424" target="_blank">📅 00:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130423">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
خبرنگار فاکس‌نیوز به‌نقل از مقامات ارشد دفاعی بیان می‌کند حملات هوایی آمریکا همچنان در جریان است که باتوجه به حجم تحرکات هوایی در جنوب کشور ادامه‌دار بودن آن قابل انتظار است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/130423" target="_blank">📅 00:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130422">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سپاه پاسداران: ما مقابله با حمله‌ای که توسط نیروهای آمریکایی به جزیره سیریک انجام شد را اعلام می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/130422" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130420">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e331902452.mp4?token=P0DMyySECIJVzwltEWLQAjfgS5uGN4Ll7H6jZuBhqXDyGpnjJXeeClpVkJ3pKILvlWrCdio3xpyWP85g1BRKlmQchF1LeBK8aTXh2hz7CpgjX9D75YNM7Y4ILBKZL9zwx43jIHQkwkJAyVg_Y9zuJ63dN5a1w75Ah-Tl4TAPzsLhjfaGKYq2fKJbY9Gs6jLWyHseK2ffGTybkpa6_c_cNPH6vNqsELe6t0xMj15eP3njIfy062yc11H5NQS5n4CBaZlwCKBdFYBEDcHgOJZ8omPn6XoJbRUB4bjV1pFgtoTeIhgFdVvDucIHHUex_bRh5fM5oQivHxs47MoQnS9SkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e331902452.mp4?token=P0DMyySECIJVzwltEWLQAjfgS5uGN4Ll7H6jZuBhqXDyGpnjJXeeClpVkJ3pKILvlWrCdio3xpyWP85g1BRKlmQchF1LeBK8aTXh2hz7CpgjX9D75YNM7Y4ILBKZL9zwx43jIHQkwkJAyVg_Y9zuJ63dN5a1w75Ah-Tl4TAPzsLhjfaGKYq2fKJbY9Gs6jLWyHseK2ffGTybkpa6_c_cNPH6vNqsELe6t0xMj15eP3njIfy062yc11H5NQS5n4CBaZlwCKBdFYBEDcHgOJZ8omPn6XoJbRUB4bjV1pFgtoTeIhgFdVvDucIHHUex_bRh5fM5oQivHxs47MoQnS9SkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اغتشاش و کودتا هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/130420" target="_blank">📅 00:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130419">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
گزارشات از جابجایی لانچرها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/130419" target="_blank">📅 00:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130418">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
تسنیم:
نقض آتش‌بس و تفاهمنامه توسط آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/130418" target="_blank">📅 00:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130417">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
خبرفوری/ حمله به تهران
⁉️
برخی منابع خبر دادند در صورت گسترش حملات، به تهران نیز حملاتی میشود
⭕️
@Akhbr_Fourii</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/130417" target="_blank">📅 00:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130415">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فاکس نیوز به نقل از منابع آگاه: حملات آمریکا به اهداف ایرانی ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/130415" target="_blank">📅 00:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130413">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYKdKLiZB0peRcJCWuX9yiEmXQI-qh5w-iJS2PXN3JyXAj88O4AOQqKQzXKJDxoWCLi5mf_67QdJsAq9tRpBHZS8XEZEszGvBxxmMLBwRs41PX8qppHI5qUzvALYRxGZbLmAklrUG1YJPQI_vbwKdYXp_nESGFgz44HnwvDMr_BHWhm1RJV7-sBhoRJjOHx_t7kphMRhKkhaXHBVBvVelOaw8B07KQp2DliQoh5oNRhZmgtFgnPm0rH74TedrlH5SEfgaktUSfEDcTaiKMcbXVHWs1Ci8WKhadO46GvzfjB9U-afO4TAW5FE-A2wRlUSAtlYWbkiktNrShaKECvTZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا: ایالات متحده در پاسخ به حمله‌ای که یک کشتی تجاری را هدف قرار داده بود، ضرباتی علیه ایران انجام داد.
🔴
هواپیماهای ما حملاتی را انجام دادند که سایت‌های ذخیره‌سازی موشک و پهپادهای ایرانی و مواضع راداری ساحلی را هدف قرار داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/alonews/130413" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130412">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
گویا یک دکل مخابراتی در سیریک مورد حمله قرار گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/130412" target="_blank">📅 00:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130411">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فووووووووری/بریزید اینجا
⬇️
https://t.me/+1RDlZFB3XPtlNzg0
https://t.me/+1RDlZFB3XPtlNzg0</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/130411" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130410">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی: ارتش آمریکا در منطقه تنگه هرمز حملاتی انجام داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/130410" target="_blank">📅 00:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130409">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ep50HTCjGPU1uaqg70VTp4oIL0cfLrawcyyaD5nCb3l7mz0_5FIbnQOrlTbf-3q44KBXHnsSOf3F5-YJ1xmP1bEr_SwYrRRRhaxTb-6RNUTHZzrIyiVoBR-3fTmxA_cmx6LjXViSoO6p1YnLdViivDI71MWjLFG71KBmy1H5bm8NiTOA0bNAkBbINOWnfwIw4lRxIGbIHqRMDVjFWMApobyfx8dnmoZz18uzAjEiWivlPx6IJ1tqIKBiO9lwI-wxcBs8EdriXj0sQ2gWtxxoGP6QsL2NdL0MpILy6Hvsl0aGE1uOSc3xiUOQ37zfRYOZflXd8MMYlug2YMZPy1zdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندین هواپیمای نیروی هوایی ایالات متحده بر فراز امارات متحده عربی و ورودی تنگه هرمز در حال پرواز هستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/130409" target="_blank">📅 23:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130408">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
برخی منابع ادعا کردند صدای انفجارها، صرفا نوتیف دریافت سویا و ذرت بوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/130408" target="_blank">📅 23:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130407">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری/ترامپ: خواهیم فهمید چه میشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/130407" target="_blank">📅 23:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130406">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوووری/طبق برخی گزارشات، سپاه قصد دارد اهدافی در منطقه را در پاسخ به حمله آمریکا مورد هدف قرار دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/alonews/130406" target="_blank">📅 23:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130404">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری/سنتکام: اهدافی را در ایران زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/alonews/130404" target="_blank">📅 23:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130402">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوووووووری/ارتش آمریکا در پاسخ به نقض آتش بس از سوی ایران، اهدافی را در جنوب ایران هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/alonews/130402" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130401">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سه صدای انفجار در سیریک، هرمزگان شنیده شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/alonews/130401" target="_blank">📅 23:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130400">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tx3Q5ocuzgepeHIoJ3gYeAtS-H7yHYtejLMPrhFnh_jzH8jRfjaEQog8lMkNk27I9sk6H2ii5CN9g1ppvcppXDuBnUK9GvVxU10SFXf3NcuRhdLwOMpr3eYTY65WcDXt7DS3RM2gd31shKZpfi07vzlFuLOSKhXCmvBaQz1MIz3hE6TYSCj7-apoJSmfiM4Y06-KViygLQNsOQYUKl-mS_11AiYQcy3gCwK545JV-Isl7s58rMhbIobdjRmsHtJLp5OFalwDMNp0S6ilzCEVCatM-5Z3Cb7d_zkcLUwRIP789oesMWWm8Ak8XfEdN4xi030WlshZJAyIpabiO648BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده…</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/alonews/130400" target="_blank">📅 23:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130399">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2nVkN7xid50G6Ec6m9uxIWFDW6wnu_rIr4P0XEDe746vSDeT_Vnb3vLt8Rut-RqYbCsiRnQX0ksSWRzduFb7ZnzjQRQNNjGv7WXICUvbnbti87_fLzhT_2JLEbeog9WW7gqbtc6kDbRc1NgWa-mSo5jr98nXN_n-hiCvqYQ22ZCFHvblBmwX2nTeKxRGyZ_MPA9Opk573ECjtUQZMcJrb5GAs12U4YyvCIHaxsfUfir24Dj27N8IDaaxt_BvT31TGhRTmXRZBeM1qEEJ6UEuXkY_gwP9wJBCvmjNidhDavuZ-OVdFdc2rYMwKHol1Kc6d0mOp__4oZSymcbLfIqYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موکب تنگه هرمز تو ضاحیه بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/130399" target="_blank">📅 23:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130398">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: ما مجبور بودیم به ایران حمله کنیم، چون اونا دو هفته با داشتن سلاح هسته‌ای فاصله داشتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/130398" target="_blank">📅 23:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130397">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی: اگر دشمن خطایی مرتکب شود، جنگ بعدی دیگر مانند جنگ 40 روزه نخواهد بود، مطمئن باشید ما توانایی‌ های جدیدی را به میدان خواهیم آورد و آقای ترامپ بداند که اینبار تلفات انسانی گسترده‌ ای در پی خواهد داشت
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/130397" target="_blank">📅 23:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130396">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی: اگر دشمن خطایی مرتکب شود، جنگ بعدی دیگر مانند جنگ 40 روزه نخواهد بود، مطمئن باشید ما توانایی‌ های جدیدی را به میدان خواهیم آورد و آقای ترامپ بداند که اینبار تلفات انسانی گسترده‌ ای در پی خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/130396" target="_blank">📅 22:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130395">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
الحدث به نقل از منابع سیاسی لبنانی:
سخنان نتانیاهو با آنچه در پیش‌نویس چارچوب توافق پیشنهادی آمده، در تعارض است
🔴
«چارچوب توافق» با اسرائیل به‌صراحت از «استقرار مجدد مرحله‌ای» (عقب‌نشینی یا بازآرایی تدریجی نیروها) سخن می‌گوید
🔴
بر اساس این توافق، ایجاد مناطق آزمایشی با تصمیم یک‌جانبه اسرائیل امکان‌پذیر نیست
🔴
این توافق هیچ‌گونه به رسمیت شناختنی برای «منطقه امنیتی دائمی اسرائیل» در خاک لبنان در بر ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/130395" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130394">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: ما مجبور بودیم به ایران حمله کنیم، چون آنها دو هفته با داشتن سلاح هسته‌ای فاصله داشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/130394" target="_blank">📅 22:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130393">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
حزب‌الله: چارچوب توافقی که در واشنگتن به امضا رسیده، از دیدگاه مقاومت مردود است و هیچگونه الزام یا تعهدی برای مقاومت ایجاد نمیکند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/130393" target="_blank">📅 22:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130392">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124d0585ad.mp4?token=Nteytn4Sj7tcpR1YOxtfJsnJVKk8Yreo0Njbiy21PS0dPygFfWY1UZaJkMuU_Ka_nqGoEnEvKS8zYgUVoHH-4-PyNy1Rw5CF34Sk5QY-TY6zmI4lQh8MtOBWZqfoVS-1z4fDyQeaL4PvecC--Zgr1wsw9R5o_-mtobfpH2TZcLQg5p7pr-_4C2YsnXBc56HkPvt8Lbv5_x6uA_S6yJr-x8g-CxQ4lJphiswkIcEecuC33uC9BQsBSq149qYVdHmCmLWjUuWl4UA9gTWDlUWxpZGIhvWwhoxurMX5R5O9_ajjC3-RH28UvuQgR0yYhWObduMiV9AVWxwz-SENn6HZyIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124d0585ad.mp4?token=Nteytn4Sj7tcpR1YOxtfJsnJVKk8Yreo0Njbiy21PS0dPygFfWY1UZaJkMuU_Ka_nqGoEnEvKS8zYgUVoHH-4-PyNy1Rw5CF34Sk5QY-TY6zmI4lQh8MtOBWZqfoVS-1z4fDyQeaL4PvecC--Zgr1wsw9R5o_-mtobfpH2TZcLQg5p7pr-_4C2YsnXBc56HkPvt8Lbv5_x6uA_S6yJr-x8g-CxQ4lJphiswkIcEecuC33uC9BQsBSq149qYVdHmCmLWjUuWl4UA9gTWDlUWxpZGIhvWwhoxurMX5R5O9_ajjC3-RH28UvuQgR0yYhWObduMiV9AVWxwz-SENn6HZyIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ توافق اوباما با تهران را «JCPOC» می خواند.
🔴
پ.ن:
Joint Comprehensive Plan of Action
است که در فارسی به آن «برنامه جامع اقدام مشترک» یا همان توافق هسته‌ای ایران (برجام) می‌گویند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/130392" target="_blank">📅 22:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130391">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ: کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که تابه‌حال در خاورمیانه رخ داده است.
🔴
من فکر می‌کنم خمینی (منظورش خامنه‌ای‌ست) و دیگران در ایران از اینکه من سلیمانی را کشته بودم خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
🔴
او یک ژنرال درخشان بود. او مردی بسیار بیمار از نظر روانی بود.
🔴
کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که در خاورمیانه رخ داد. مردم گفته‌اند که بزرگترین اتفاقی است که در ۱۰۰ سال گذشته رخ داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/130391" target="_blank">📅 22:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130390">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9bda5bb20.mp4?token=c3TPtRcy9eEj5Ra8IbyKKEvUxOoyDLZUC6Ixi7-cQC9OC68wMLJWTMHtAOkpJuM8KQekBaHoHiDVDj5HfVredhvjO8939bt627gqCY1b1dBfZxopJKeAiyfDzoKmukYlFfW5GWKZHiCsYY5fp4zrTgpyWDsBHxNeUDxnLKCSZ4s55mU7f4pla1BOxAVV2CDik3XuvaPAaHjeVDdIQ5BhwUGMDma4lmV35jj6WJqaLsrnmsAi-eYAvlktdDPfDarLs-dckgEzUK2HZSNPxifwjYU6PREiok1kaTl8OkGWq1uoy8VwWkMflWPd1Db8_gPtcKReAPkhxW2eSgmyIC-CH6Krk8hhrdPp5t_HIQZZX400YYJp2XR_J6qiKr4UM8GADYkamaBMoPJ2KZJ-rJXsFBwmtPT1Iq7vwwv_8L0v24byM37eoHjmgbF30KjtKF5nNWJei-v0XXLxeGGtApoTdLErxzv-e4onDy_n3ZSdvVt5U8t3eZLuvY9hG7OMP63KOae26AUC0mkW8VLZhx_TyoDKMd0HcfMPEft6oD2Yuljn20J_6eAg4COS062TIJ29eXxlbBqbfnuZb8yNTNODxd_LPvVZ3Pnn65Xav9HWg0dESSkTNiRRvAW2bg6ZQDkJZuJwM7-oTcJwQmMGbODxqe9yNdqH8rxKGaTLKz0PenI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9bda5bb20.mp4?token=c3TPtRcy9eEj5Ra8IbyKKEvUxOoyDLZUC6Ixi7-cQC9OC68wMLJWTMHtAOkpJuM8KQekBaHoHiDVDj5HfVredhvjO8939bt627gqCY1b1dBfZxopJKeAiyfDzoKmukYlFfW5GWKZHiCsYY5fp4zrTgpyWDsBHxNeUDxnLKCSZ4s55mU7f4pla1BOxAVV2CDik3XuvaPAaHjeVDdIQ5BhwUGMDma4lmV35jj6WJqaLsrnmsAi-eYAvlktdDPfDarLs-dckgEzUK2HZSNPxifwjYU6PREiok1kaTl8OkGWq1uoy8VwWkMflWPd1Db8_gPtcKReAPkhxW2eSgmyIC-CH6Krk8hhrdPp5t_HIQZZX400YYJp2XR_J6qiKr4UM8GADYkamaBMoPJ2KZJ-rJXsFBwmtPT1Iq7vwwv_8L0v24byM37eoHjmgbF30KjtKF5nNWJei-v0XXLxeGGtApoTdLErxzv-e4onDy_n3ZSdvVt5U8t3eZLuvY9hG7OMP63KOae26AUC0mkW8VLZhx_TyoDKMd0HcfMPEft6oD2Yuljn20J_6eAg4COS062TIJ29eXxlbBqbfnuZb8yNTNODxd_LPvVZ3Pnn65Xav9HWg0dESSkTNiRRvAW2bg6ZQDkJZuJwM7-oTcJwQmMGbODxqe9yNdqH8rxKGaTLKz0PenI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
اخبار فیک/جعلی گفتند که ایران امروز بسیار قوی‌تر از ۴ ماه پیش است.
🔴
آن‌ها تشنه‌ی انجام یک توافق هستند.
آن‌ها به ما بسیار زیادی می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130390" target="_blank">📅 22:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130389">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e369539a42.mp4?token=qEx4Ow4Ww4h3ghKa-DLzAyIgXi-U4CiaahZaB-WJbDTwOEDiqYUS4MmEb-MBNh6LnQgvBfzqgy_lDdLS7bSRL2jMIU7ei_SMDde9SHT30xwtGYuuj2tHj1gl-h-qFBz22UZMI0uzzb4fgUe3K_VWpgeURc3pjlZBArFuPo_rKiP-7jV2uTL_C12IyGRMzqfgdCh4h5Xh8WQIrIHn4_AXwgGrmOygWseQWtRGVuIZRiWDl5LTrUgtuAUIwUp3pM6U6VzKgp3-pIbj68PFtOwY7I3RFdcKtFTIL6D_wDrPkxktc6lmTt_5M3w2h5GvXdusCKdMwTrPdXmVodIuU27DkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e369539a42.mp4?token=qEx4Ow4Ww4h3ghKa-DLzAyIgXi-U4CiaahZaB-WJbDTwOEDiqYUS4MmEb-MBNh6LnQgvBfzqgy_lDdLS7bSRL2jMIU7ei_SMDde9SHT30xwtGYuuj2tHj1gl-h-qFBz22UZMI0uzzb4fgUe3K_VWpgeURc3pjlZBArFuPo_rKiP-7jV2uTL_C12IyGRMzqfgdCh4h5Xh8WQIrIHn4_AXwgGrmOygWseQWtRGVuIZRiWDl5LTrUgtuAUIwUp3pM6U6VzKgp3-pIbj68PFtOwY7I3RFdcKtFTIL6D_wDrPkxktc6lmTt_5M3w2h5GvXdusCKdMwTrPdXmVodIuU27DkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره رهبری در جمهوری اسلامی ایران:
دیگر کسی نمی‌خواهد رهبر ایران باشد. گفتند: «چه کسی دوست دارد رئیس‌ باشد؟» و همه گفتند: «نه، ممنون.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/130389" target="_blank">📅 22:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130388">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ درباره شهردار نیویورک:
شهردار ممدانی که به نظر آدم خوبی می‌آید، گفت که قصد دارد مطمئن شود مردم افزایش اجاره‌بها را تجربه نمی‌کنند، حتی اگر هزینه انرژی افزایش یافته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/130388" target="_blank">📅 21:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130387">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a205f15b6.mp4?token=GWMoD0_MS7PAtLcuzJpAVgR0dmAxqJ5t631c7ij0wo1albFs0qhnUh8o5HLpH5IsArNz25BkBrufsi_EIhT4VRSjJA_rMMV_sJc3aZ7WXmUAVOjOkwU7GRNWsUPl5-ChKH8xT2wxwVtL1Dj-fT7p4WOmfPsU0zKDojysJtCvmtAtiIpnYynvXU31ett6DZas-K_uLy48T_i0T4P7hmL4jbSuGWVuQ7sAU4eQnz51VGJyBJuAwiYSaR3ZIvghfQQYB5Wwz3idUSXIlEiodSGB69FABIQpaniCiPTLudgwyjUC0gAhzRsU99Vge7A2h_pQN2dpj-pr7ALdCshlfYbv4ANJFzR-icOYWexIVpbqrwRu6KhxaXc6SnbbXXz-gNxgO-O-MiMXteDJTe17vQs-R2pSQy0WTiZoqcVbkSMr8E-RNbve7OmmLBEwMqdnVe-NLQTtbPnuhkwaNRVqv0GL3y4sk7BRD4GhrLS02KQD5mlZjVUNzIPvWz3vCK-GZGAhSx_KReCrxxqoEyevOlVeIi_ODafcevUQXOni0B2DGH_0gNA8VfKVN7WSaSwtX0rQPOsML0xxPc83bNIFVyrqDDw7MaGHb7MPaXsSPgjaKhZoTTT5n_10RUX2sVBa3eVyXXm0c_L-kLcBkRtdnCqAN7B_uKXFZAWkgNhqi_sXBu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a205f15b6.mp4?token=GWMoD0_MS7PAtLcuzJpAVgR0dmAxqJ5t631c7ij0wo1albFs0qhnUh8o5HLpH5IsArNz25BkBrufsi_EIhT4VRSjJA_rMMV_sJc3aZ7WXmUAVOjOkwU7GRNWsUPl5-ChKH8xT2wxwVtL1Dj-fT7p4WOmfPsU0zKDojysJtCvmtAtiIpnYynvXU31ett6DZas-K_uLy48T_i0T4P7hmL4jbSuGWVuQ7sAU4eQnz51VGJyBJuAwiYSaR3ZIvghfQQYB5Wwz3idUSXIlEiodSGB69FABIQpaniCiPTLudgwyjUC0gAhzRsU99Vge7A2h_pQN2dpj-pr7ALdCshlfYbv4ANJFzR-icOYWexIVpbqrwRu6KhxaXc6SnbbXXz-gNxgO-O-MiMXteDJTe17vQs-R2pSQy0WTiZoqcVbkSMr8E-RNbve7OmmLBEwMqdnVe-NLQTtbPnuhkwaNRVqv0GL3y4sk7BRD4GhrLS02KQD5mlZjVUNzIPvWz3vCK-GZGAhSx_KReCrxxqoEyevOlVeIi_ODafcevUQXOni0B2DGH_0gNA8VfKVN7WSaSwtX0rQPOsML0xxPc83bNIFVyrqDDw7MaGHb7MPaXsSPgjaKhZoTTT5n_10RUX2sVBa3eVyXXm0c_L-kLcBkRtdnCqAN7B_uKXFZAWkgNhqi_sXBu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ با اشاره به پیام کمی پیش خود در تروث‌سوشال در طعنه به کمونیست ها:
راستش را بگویم — فکر می‌کنم من بزرگترین کمونیست در تاریخ می‌شدم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/130387" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130386">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ: تمام کمونیست‌ها بی‌خدا هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/130386" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
