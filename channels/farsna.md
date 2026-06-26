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
<img src="https://cdn4.telesco.pe/file/Qw8e_ZfkHvuaHQ1gHi0CWP0Pb0srIIKUEt51aOXDHZhCODLZKFtDKyfbq9_QjiNDkVNGFeX8vCuWT55o-zIHGi7q7y8iNaTwX1mMlwRvLjw26yu-XLo2m3VTBaL9QOJvGTzFL4zspsofWcyQtlY0wWOC2WFeH4e42o5KVzUpwfPqNHzAN1qM5dLnKA9rWwTx_GMHyiaJu1ctaimIdSUTCdrmk9mL-OtD8Vq281Z8IFhP-tIqN5-ZodlwMLxhTeqcGvmlkFc-NLhIJaaPlxEPj6miySu2VHcmEYIb0gllacCc4I2goVuUEyQ21Tf0Z_LRbiIh6vemPA6JMrGtkbd8tA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 00:32:49</div>
<hr>

<div class="tg-post" id="msg-444976">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj9PzB9bRW-pg6kmdQWaY4_vRvGkcRDwQPo6SmpfZM8g2U8eX0gnXavNCy_ymj0mzVRj7QwOlKsxChcRTqxwTPmgwWRXkdCaqq8kjKZvjRBNQdB0y5L9qRqwj5n7SnixX4r9IF8cNGcXk-ikdFfIEON6AlRG6dDSr5mrfgx_ysURyRoPZSJ0UapEWs2FbR637MixS9NZ6vKwmsLtm6gBpUSfCguj95KBUxVu8kdwG89f5XRLrPJko7pKhGU22jM3yB_keh5OoJf9L3KPfwdAdsxchhelQwrbfaDdm2eGVi_esJWrREMd7MPzWEK0V0jDfhkb1Mq_IiOmgV-khifHyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ گل‌باران شد
⚽️
فرانسه ۴ - ۱ نروژ
@Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/444976" target="_blank">📅 00:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444974">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d312347ed.mp4?token=qg69YilmAdLYEiyqdQMqVm_N9cMrMxFqY2XrZBgwraqhZvPn3s_qkCrPIiLrgPn55nLsbNeOocIh42pCfob5Zy_B2uz5pS4VNd5iqrhU_Srtq5BmCf74CslxYD-g9LxiLSNtqpxRAPSUIYGK0PegFHnAF2Zm9524W2pwKIcKHmJYLSCqItLqVvXVyOwUzY9-YCX30rwOadyPgd6BcJ64TmXfCkwj0ToQiZJdT9qqtuflTQJ80FGJ4P7AeQhkE3MEoCPr6i4UuUVpU4vBRNU3hPton6_qoQ71pn9swN0tjB8l2ZoFyni9oHRKQw9vJ3n9PbLxhDsc8W9GoaagnbZVqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d312347ed.mp4?token=qg69YilmAdLYEiyqdQMqVm_N9cMrMxFqY2XrZBgwraqhZvPn3s_qkCrPIiLrgPn55nLsbNeOocIh42pCfob5Zy_B2uz5pS4VNd5iqrhU_Srtq5BmCf74CslxYD-g9LxiLSNtqpxRAPSUIYGK0PegFHnAF2Zm9524W2pwKIcKHmJYLSCqItLqVvXVyOwUzY9-YCX30rwOadyPgd6BcJ64TmXfCkwj0ToQiZJdT9qqtuflTQJ80FGJ4P7AeQhkE3MEoCPr6i4UuUVpU4vBRNU3hPton6_qoQ71pn9swN0tjB8l2ZoFyni9oHRKQw9vJ3n9PbLxhDsc8W9GoaagnbZVqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمجید رئیس‌جمهور لبنان از توافق با اسرائیل
🔹
جوزف عون ریاست‌جمهوری لبنان: توافق اولیه نخستین گام در مسیر بازگشت کامل شهروندان لبنانی به سرزمین‌های آزادشده و خانه‌های بازسازی‌شده آنان است.
🔸
این ادعا در حالی است که مقامات اسرائیلی از جمله نتانیاهو اعلام کرده‌اند…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/444974" target="_blank">📅 00:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444973">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">سنت‌کام به صورت رسمی حمله به اهدافی در ایران را تایید کرد
🔹
سازمان تروریستی سنتکام اعلام کرد که امروز مواضع ذخیره‌سازی موشک و پهپاد و همچنین تاسیسات راداری ساحلی ایران را هدف حملات خود قرار داده است.
🔹
طبق ادعای این سازمان، این اقدام در تلافی حمله پهپادی روز ۲۵ ژوئن ایران به کشتی باری «اور لاولی» (M/V Ever Lovely) با پرچم سنگاپور انجام شد؛ کشتی‌ای که در حال خروج از تنگه هرمز در امتداد سواحل عمان بود.
🔹
سنتکام مدعی شده این حمله نقض آشکار توافق آتش‌بس و تهدیدی علیه آزادی کشتیرانی بین‌المللی بوده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/444973" target="_blank">📅 00:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444972">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎥
ترامپ: از اینکه ایران پهپاد شلیک کرده اصلا راضی نیستم!
🔸
خبرنگار: شما گفتید که ایران آتش‌بس را نقض کرده. آیا این کار عواقبی برای آن‌ها خواهد داشت؟
🔹
ترامپ: خب، به‌زودی متوجه خواهید شد.
🔸
خبرنگار: آیا آتش‌بس همچنان برقرار خواهد ماند؟
🔹
ترامپ: از اینکه دیروز…</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/444972" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444971">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBEMPi-Wn-kq3IwwlA2LAffFjjPGqJQdERuUsBAJbkHjwkyvdHutLLJWHm9J7ldrrg3VcRm5-zo3OHkB3KNSMcM0BnyIzPNrvRMzXVA-4zwA91pT9K7J-UJivN8OS7xzAucQZWi_QTK-2LeigZu5gML7iz7y41lOy-WCq9x-WsGJ1Q3e1MVP4HSopPNysNLUWxskwtg7Tgv9DwLzKTDPntNQlwLp1ilYBrhjISI6wD5dg3kUh9pc8uuwPmVeAkyNQIY2RIkLeVz6NxiIRYJx1IHVjjkWN0fzX8w_Mj2jyfPXkKoiidTyvRgTM2kx24MDwOz-xBuxYJOwd3YgJLvTdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی کوچک‌ها بزرگ می‌شوند
🔹
کاروان خسته از راه، در پهنه فرشی از خاک و شن توقف کرد. بیابانی برهوت و تا چشم کار می‌کرد، خشکی بود و آفتاب. پیامبر(ص) رو به یارانش کرد و گفت: «برای برافروختن آتش و پختن غذا، هیزم جمع کنید.»
🔹
اصحاب گفتند: «ای رسول خدا! خودت می‌بینی که اینجا چه صحرای خشکی است؛ در این برهوت حتی یک تکه چوب هم پیدا نمی‌شود!»
🔹
پیامبر گفتند: «هرکس به هر اندازه که توانایی دارد، بگردد و بیاورد؛ حتی اگر بسیار اندک باشد.»
🔹
یاران میان ماسه‌ها، زیر بوته‌های خشکیده و لابلای سنگ‌ها شروع به جست‌وجو کردند. هرکدام تکه چوب کوچکی، خار خشکی یا ریشه رهاشده‌ای پیدا می‌کردند و با خود می‌آوردند.
🔹
وقتی همه جمع شدند، در کمال شگفتی همگان، تپه‌ای بزرگ و قابل توجه از هیزم در برابرشان ظاهر شد.
🔹
در این هنگام پیامبر (ص) فرمودند: «گناهان کوچک نیز این‌گونه جمع می‌شوند. ابتدا به چشم نمی‌آیند و هر کدام را ناچیز می‌شمارید، اما وقتی روی هم انباشته شوند، تپه‌ای بزرگ از تاریکی می‌سازند.»
@Farsna
-
#حکایت</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/444971" target="_blank">📅 00:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444970">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
بروجردی‌ها: ما و حزب‌الله تا ابد هم سنگریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/444970" target="_blank">📅 23:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444969">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpx6vlgv5Ko1miRdM4Wv38fSrJJLFjmA9db07umUMAFFf0PyuaOyW4C6kNRKUdfMadOndjRLFAO-Bn2b4kb1nVoCt-pDWUkeGKx2y9vg47soFJS4NfckO72bOYEZJYwMxBuWF8YsnbSe1Q-PhpOrMP7dAFn2cFUcZDa4vo1b1Qke8V6vqjnzj6vyyKufqkSDBZfYT76dq5KijVdoaBzXzmQUeyGCOpaLk7t_axnhQjG0exS9Dm56d1R61qDFUOS4um_q6i-QxE9vjVJfpJUrpDnHNxQuoN6v9LwT9J7JP-ZF_hbwqUfdE23PFCJy9zHjEo0gUV_FjkxuZf-kQQ7e9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها قدم نخواهیم زد، میلیون‌ها ایرانی کنار ما هستند
🖼
تخته آخرین جلسه فنی تیم ملی فوتبال ایران پیش از دیدار برابر مصر
@Sportfars</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/444969" target="_blank">📅 23:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444968">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=dBERqvpPdSneUfcIbBbFguwGaFO17EQ9T1mveSHm6gwKqt3IctAmu0Ak11xmC9dDF6Bjlpt3LCpEX9akIXqwLXQ2UBE79jd3Id0THnsaLKLfrrislqycNZQgAr4KtZnSWl9Y9zD-HBjIcG45_mokkH9uysEVcrAgUbHFGBhedcK3Zcjj6sHKzCAI8KmQWRbfOt15ou6FZcXjLK-7Kh_K3xLB2k6OLCdpPD5LIrkwx3zVTx3A79OCtUbEJJv5e6Plph9jPZIl0aFUcMbrq8M3H-20o12utan0gMCUwp68cFNs2mVlBOe2_kjaQrBfa4nl7P2GTOGWO0WxgcvrqRV1lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=dBERqvpPdSneUfcIbBbFguwGaFO17EQ9T1mveSHm6gwKqt3IctAmu0Ak11xmC9dDF6Bjlpt3LCpEX9akIXqwLXQ2UBE79jd3Id0THnsaLKLfrrislqycNZQgAr4KtZnSWl9Y9zD-HBjIcG45_mokkH9uysEVcrAgUbHFGBhedcK3Zcjj6sHKzCAI8KmQWRbfOt15ou6FZcXjLK-7Kh_K3xLB2k6OLCdpPD5LIrkwx3zVTx3A79OCtUbEJJv5e6Plph9jPZIl0aFUcMbrq8M3H-20o12utan0gMCUwp68cFNs2mVlBOe2_kjaQrBfa4nl7P2GTOGWO0WxgcvrqRV1lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای ترامپ درباره نقض آتش‌بس از سوی ایران
🔹
رئیس‌جمهور آمریکا: جمهوری اسلامی ایران دست‌کم ۴ پهپاد به سمت کشتی‌های درحال عبور از تنگه هرمز شلیک کرد. یکی از پهپادها برخورد محکمی با عرشه بالایی یک کشتی باری بسیار گران‌قیمت داشت.
🔹
خسارت وارد شد اما کشتی توانست…</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/444968" target="_blank">📅 23:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444967">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بازی ایران ـ مصر فعالیت ادارات در برخی استان‌ها را به تأخیر انداخت
🔹
با اعلام استانداری‌ها تاکنون، ادارات استان‌های کردستان، قزوین، فارس، سمنان، گلستان، یزد، مرکزی، خوزستان، کرمان، مازنداران، زنجان و آذربایجان‌شرقی فردا با حداقل ۲ ساعت تاخیر شروع به‌کار خواهند…</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/444967" target="_blank">📅 23:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444966">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75775a8a4.mp4?token=aag10xAkWr4YBr4IdAJEHfaNb7_drFZy_y7pLOyLAk9Ir1CN8umD9Zm4Xd7t7Ee6F-IkYl5qNuA3RTYkNNYhvuOGO0QMsTmMrcS12LhmxmDm50-MxpT7XrtVYx1NWLj3nXB64KTLv_KL-IsHZe0ZpENELe__BHApN311AWMmIb69Ur6MBbdt_eU9cC01B_dyG56s8cjhDtslnlzYcg3OtB_s0ti3y27yYizTnrHEBv-39EGuNJZ8W8lwAznJc-TCGq-K4Zd1Hp7clEkVwht7ShMxgM6KbXe9T657iMpLPkY-CtmzN_KHgfQtLAkIiSPhMSrdR_dx0tcDxoDRKooUSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75775a8a4.mp4?token=aag10xAkWr4YBr4IdAJEHfaNb7_drFZy_y7pLOyLAk9Ir1CN8umD9Zm4Xd7t7Ee6F-IkYl5qNuA3RTYkNNYhvuOGO0QMsTmMrcS12LhmxmDm50-MxpT7XrtVYx1NWLj3nXB64KTLv_KL-IsHZe0ZpENELe__BHApN311AWMmIb69Ur6MBbdt_eU9cC01B_dyG56s8cjhDtslnlzYcg3OtB_s0ti3y27yYizTnrHEBv-39EGuNJZ8W8lwAznJc-TCGq-K4Zd1Hp7clEkVwht7ShMxgM6KbXe9T657iMpLPkY-CtmzN_KHgfQtLAkIiSPhMSrdR_dx0tcDxoDRKooUSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری مردم مراغه در پشتیبانی از ولایت زیر پرچم امام حسین(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/444966" target="_blank">📅 23:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444965">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎥
گل برتری چادرملو به پرسپولیس در دقیقه پایانی توسط محمودآبادی
⚽️
چادرملو ۲ - ۱ پرسپولیس  @Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/444965" target="_blank">📅 23:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444964">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4602da6611.mp4?token=d9KEo2grTEwBtnQjqbIeVa_P5b9X0azFtnNaThkiox55IQwr_zQG1_2vVnLA_D2Z70md_D1ZxfEMwhC8IFApNLkbTE3XbdInz1pxk53eJWPTbdIR7IHEAh7XPiUs9UiJzLusudIWm9Mmdz5K5ICRTFROydrr4eLHpdcpG8vvgzdx7l2sBnYxHG24IPuSZn5RVA5F9UGES0-LjgLUV2xbp-QWUi2rj4itlXwsQWiE20mrNdPpOfI4LP_lK37jIfNIvRAkX0e11aFz-nyLub9a2D7edTpqraUbP3_ePBqSQdO434R4gfGSTMpErMmQknZqZp7tFiGWhWXOWJEiT44zPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4602da6611.mp4?token=d9KEo2grTEwBtnQjqbIeVa_P5b9X0azFtnNaThkiox55IQwr_zQG1_2vVnLA_D2Z70md_D1ZxfEMwhC8IFApNLkbTE3XbdInz1pxk53eJWPTbdIR7IHEAh7XPiUs9UiJzLusudIWm9Mmdz5K5ICRTFROydrr4eLHpdcpG8vvgzdx7l2sBnYxHG24IPuSZn5RVA5F9UGES0-LjgLUV2xbp-QWUi2rj4itlXwsQWiE20mrNdPpOfI4LP_lK37jIfNIvRAkX0e11aFz-nyLub9a2D7edTpqraUbP3_ePBqSQdO434R4gfGSTMpErMmQknZqZp7tFiGWhWXOWJEiT44zPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل تساوی چادرملو به پرسپولیس در دقیقه ۵۷ با ضربۀ سر صادقیان
⚽️
پرسپولیس ۱ - ۱ چادرملو @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/444964" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444963">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3LeVwtg1ynw8WG-NHHePpckHLwu2up_-uPgvTX--T-bVUgg42OffoT2UMelDATupDwULGn_hpxgCjs8A1ktusAtY2ZfgfvaXacs3MICuKBvl1flw8UdOBHSegZmoQdwEeH0BjCRaBX2Gi2GyX93KjWDVjPCJQTcgr7YExPyyxTFpKpstqGGhZvMsNcy0QhCFxY5qukuXaceO9FS87HathgikPMGNM97d2VcVlUnVbQe7_nf5JHbdzszwqKUIsbjjARzpa9bUObEIsRZqDPxIv6cMzAsq6N9HNgC6qGXQX_IAtu7qY4kvF3uOgytMtpHFzTjTG7afxfZ2WWCiV7CIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعاهای نتانیاهو درباره مفاد توافق اولیه با لبنان
🔹
نخست‌وزیر رژیم صهیونیستی امشب بعد از اعلام توافق اولیه با لبنان آن را «دستاوردی بزرگ برای اسرائیل» توصیف کرد.
🔹
او مدعی شد که اسرائیل بر اساس این توافق تا زمان خلع سلاح حزب‌الله در کمربند امنیتی باقی خواهد…</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/444963" target="_blank">📅 23:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444962">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc4eab69f.mp4?token=FxacERbrFY3rDN-qfGykZwHXcifmZmig5jF9RqGIUD_b77Os9YU0St9iHuIsG1yv9vgAy7wGAqxRhiUx3hXWYe5OINdS6Vpwt9P6fIUir040tffjoQN5m26e6nL0-PVvEr6xh_-OmofwVBu2So0T2CN0kTZZWNxlYJkJWT7fY7XJxQTmH3XeBe_4WreClRP9T_VZsbo7PNf7_w32dmK1MFx-VhFF2OjbphE4ERbz19Ou7d35PoPBz96HR7NaagpydXbp_4BkUSOTgCniiLQ3zpcpvxolVRQoV1PqZhiK8VBeuOkYhKmXTrs_9sS9wTiATHc49zmvGk2bVCoBvajUIkbIW8Z-w4em-4s5ZYcFf1kG_pu4AJZ3LqMdcQL9fJKX-uuJ3PprqNfXyHahlfJn0qGJMNXBEf2q3k3q0yMQeTX6VOj5v5vzi832rpDJBYyZBQppBInB9tfel5Vj9FgYdiyAdEe3RLkxdDm5JwIT_2rmMtVI9yHTzHgq8Qg4mrDkoyzWp8OhALYybhf9VBueBA6B_7xw_C7Ay6q58oSVLHDlgfVL-xcnxTOGApZ-qKLzyGwK9MkmGqj5M77Rb2bIGPe_N06y0233thFIfBh169GDKUAvjTvCF811RSQtDCTv3O2LDf6eTLqNRas_kavv5AsVooPtFqGzoUneHLA2dEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc4eab69f.mp4?token=FxacERbrFY3rDN-qfGykZwHXcifmZmig5jF9RqGIUD_b77Os9YU0St9iHuIsG1yv9vgAy7wGAqxRhiUx3hXWYe5OINdS6Vpwt9P6fIUir040tffjoQN5m26e6nL0-PVvEr6xh_-OmofwVBu2So0T2CN0kTZZWNxlYJkJWT7fY7XJxQTmH3XeBe_4WreClRP9T_VZsbo7PNf7_w32dmK1MFx-VhFF2OjbphE4ERbz19Ou7d35PoPBz96HR7NaagpydXbp_4BkUSOTgCniiLQ3zpcpvxolVRQoV1PqZhiK8VBeuOkYhKmXTrs_9sS9wTiATHc49zmvGk2bVCoBvajUIkbIW8Z-w4em-4s5ZYcFf1kG_pu4AJZ3LqMdcQL9fJKX-uuJ3PprqNfXyHahlfJn0qGJMNXBEf2q3k3q0yMQeTX6VOj5v5vzi832rpDJBYyZBQppBInB9tfel5Vj9FgYdiyAdEe3RLkxdDm5JwIT_2rmMtVI9yHTzHgq8Qg4mrDkoyzWp8OhALYybhf9VBueBA6B_7xw_C7Ay6q58oSVLHDlgfVL-xcnxTOGApZ-qKLzyGwK9MkmGqj5M77Rb2bIGPe_N06y0233thFIfBh169GDKUAvjTvCF811RSQtDCTv3O2LDf6eTLqNRas_kavv5AsVooPtFqGzoUneHLA2dEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی منصور ارضی در شب شهادت امام سجاد(ع) در جوار محل شهادت قائد شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/444962" target="_blank">📅 23:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444961">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4uv1Wp-4dZRwAkRLXlw1wTJA_NTS2mkck5xXQcaGaf7vpamN_tCgvwz_MIP41Xp6Jx0tzD4ew0DzpQG4dPg5hK6XrUffrvYSWU1FYmKtlvwFVD66axfaWq7ljdTVxO0-M9Xlw1m0Q2kkhMb_r7-C1OyEGbNIYPCUukXt3H3vqLud4wHBNEsVfpMtaTbE07Udd2uWP87Q-VZD15W_43GqU0WX20ZSdiJ38OtDpz12Kwa0f1UB16-ytngy3qW6mfltlT0GvvXcoynxxtu_DUCKLsh_Rd_SnmvOBxFAxrjBGc5to7DPxkmWvbL3m6DK8OtonUBmacZ0ZwCxMYICiC9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندونزی میلیون‌‌ها حساب کودک در تیک‌تاک و یوتیوب را بست
🔹
وزیر ارتباطات و امور دیجیتال اندونزی: تیک‌تاک ۴.۱ میلیون و یوتیوب حدود ۶۰۰ هزار حساب را مسدود کرده‌اند و دولت انتظار دارد سایر پلتفرم‌ها نیز همین مسیر را دنبال کنند.
🔸
اندونزی از اسفند ۱۴۰۴ مقرراتی را اجرا کرده که بر اساس آن، شبکه‌های اجتماعی پرریسک موظف‌اند حساب کاربران زیر ۱۶ سال را غیرفعال کنند؛ این قانون تاکنون پلتفرم‌هایی مانند ایکس، اینستاگرام و روبلاکس را نیز دربر گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/444961" target="_blank">📅 22:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444960">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5RC-xy-_tZ7u5w3hbFsxBAlUp0q4F2kSAmT6vdbRqYBAEilfLC6TY3Es3urxfusz02nbkJfdinmvI2psE2NZSS_ykRoTJM-6LPUVsyypYZJJ9XpKX1D7Nf1sNs8Rg4ifq5p30KPff_a_ut8_ofXGnQZqcPFN0YgTerySwW6rEnzdjRLGTjX1VYH9qiCMTYstqPIquhGhb4fo0a3zTYbkZFdKBkRCUZLZRd98pVeV2tHMjMs66z3pDtGmO_XeNKId8FXtasD6YBeRp62g6KhsP49LUXF-_BAAN4ByOj_vuIICozXV2BPCe63ZtZLiX8aoC7sKkNGUyGuKT8kuL6BNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای توافق اولیه لبنان و اسرائیل با حضور وزیر خارجه آمریکا
🔹
لبنان و اسرائیل با میانجی‌گری آمریکا و با حضور مارکو روبیو، وزیر امور خارجه آمریکا، یک توافق چارچوبی امضا کردند؛ توافقی که قرار است زمینه را برای آغاز مذاکرات رسمی و مستقیم میان دو طرف در سطح رسمی…</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/444960" target="_blank">📅 22:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444953">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mm3296tMg40P68srYzuRBHPvBu90iEHtqby2G36t3ibi6fTyBsYbimD3cGmZVI32jbHQqIX9jwCwRaLgA7QdlneJh6exQyRn0OE-2goYpfAwah3l26yuiNehWbnuYENNMseucftDoHnl45SmfwEBG6ASOeHdLqVJy8U9MGdK55GXQ8ojPrPwgatAMW3Z4yXfteSslTD5jhByvZjed0Cxf6D6mHCeyLBSmdrxK1VeDbET3OHF2NMbEbo6SqOG8Qmj8sZONnb7aUfnepcxncv7SG3HCjEhUe9mw1BHvZJFmdUggxo6SGvnFJ3R5RGyjJSuJIAm2Z6ecs2Y408GJChscA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZ3-FjZJOVzUQiZHw160DLcEcMDvtd8jSEOEMAVT7ETfG4YW7ia4n7q-x92DfTTxNK-DCuGw05wAG3SSRNNqFC7LRpGHrGKngfR5nLd-Uze_2iWMvxtToDjEnQPSnaShrvway2mF4ZqBmu2DvXu8JGC8-zTxioLHdx3AlqMbm9fFlsZ_wp2zccKpmfVftURErlwr8Xhvq1cr-4xuCzvXQ_I9c0i19XwojCLuvrpuYgh3K-bkZdfWZUxje79NDQzfrkw7WrH8k5untqXAKgpG1EsShKXx5dk2oZzbQhJSIJ2P7CuZtby5GJQMABNX25oVB2TPm9Ysf2vTRSu1EI1ddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWWqenhJ9-R7LCNN44WmC6yGPqd6OTL07070UDenqOKEyD05pH0ZCFtlr8rj_HYA8f_46eiX6WFSclH5Z-bVlKcd5wRLpElmbVztSbxcoj9JP9RIepceKbiJg5cl6kUocA3q3DLj29x_hPGbH4JGZqptEUDhW1TcwImmK_g-2q6qiAd_yUCegPTcjstRatQ2dalZhj1-7xwb58QJOcIoy6wd59PXZeiPYTzBtiW50uoSQF3JzbJI19LukPF10EW7F1HvkGZ4tWqy5QwndRk643OHMWJhNbCS8aP8i2bs_9oHcndwBt3wC7NkkHSukqD9mCZrfJMtxqoZMMQZ-BPFkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8lr9j9FRCmpKqWr7e8Ey9xJNCj14UG7hZ39YhhQsj7cujddIroJXCnwrG18i_7uSA09pACDsHanzrTD99rJQ1HZ5gHXE7vLyzq7shfEzHU2_06Cdzi6UQnF0JPksdvJN8a9SSC56BkFcfDQjEFtJBWdVGvDFPUK-gbumQICa1XO3un158Ue2o2QocVi1XqVEWhvvaRuE1xQPW_FMJs5W7dBrbZW3nkR6Ycj6RQq72dXbKKwPOOZ0nPlmUBKNKgJs7BmpewM5deWtaupMvTJXRaqwEnALIUJhHgtDEpYXLMN1M3a8_vjvHJCJtqmGcyQLZs9QGpo9pT3nZtvJa2C9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AI0BOIkmx1yqtKOkpKo74rYE1Nk4OTzH4jMr8XuI7GMEtNn81LON26SB3fwxaPqC15HoQeL-PiBZiVrKf0dmq1z9cD7FTn-3E6h3cTovXzMPpnqK2mwxS9EGNqxLKfn6Vzut1oqMrSF0Rxu6sOF-DnSZWi9ZNiz6zoZsZwmoheGRngaLW7eO5105rx6ZlirBPAl_2vIKnIo9eqgjybpBmWNTGzN2gOcCp4ko0nEXxkVzx783X-sjUKnjkKzPDDaFLvNPOaOpr0c9Qa4n309NgesIRpEZ88_WKj2lwaTsbCpgxdcHobV9W7Xfjp4sxB0xdyRPcIiwK7plY56bb4s4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4YTvHH3J5o4NuGOeYgTOkAIFUr6kXaUWpkQlOpm9XpLOjr1IGGHzfP-1-dGKsJzLmRl_HOyHfBt73JQV8L4ADp3i0LwnVH66cFKTJ6ULjVqz2mhXt0BYvdXR9EJ25uc7C3MyZMaPZamfiHQb3RRrwRAA62a9GUC5hqk3Sh_qW-YGNtygu6Q8FzDKsMdWSpsIKVp6j7pRNFGDLf5aUsFmhwQCCIKWHmm1NicbN8rQ2aGhDghsnJw50Oil78CjmbuaVQEBKpMveauGQ5pZeW20mkFlMDg5vgZPzslCPFsUs4TcrZlKOxpUNyUyX0O0kvjHiRbPP5e1vbeic84P5IFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuTgdveBygcWQq6al4ortui4UWRFH4MohHLRItPBJGYMx9tHkS7itQ6s3Ra_YMVcC0SaT7grIVfoK1YBcneSyvgF7Ymcj3Hx0ojSdc_mM60fx2R5LGQ--tA8xsZCEEdWazxrFfGaxMikuRw5svre5v-K4aNMlUHbbqyr1aEX346WkRqWUullMCWYR1uiC5OdExqv6Is0Kfv9B4B3TEDtsuENz_T4I1GdvdiFXyd-o_dCLB1RNTh8Ge5I5l00oFZJuomkIGgUO4P92tTb0tidVtEiPxE50cTX_w-jFgus8NOZ6eBHaib6Rm8AKV-N6uSL_2egWyE9kEQVZthhXDQMVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دسته‌روی عزاداران زینبیۀ اعظم زنجان
عکس:
عرفان تقی بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/444953" target="_blank">📅 22:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444952">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvCp8k9uboNrVwDyU7vnXHR-rUBuiWjWr2t9Fx83VlkWo59PohOg2ky6lm_9JK3C8AKn7HxStAAoigan6fhVjGwOc5O8HJySQe7INbQWrXKBW3NmqC_3Ozbb9L1HW_nOLG52Po4sto8aOG0YpiUvvsFFI-3KQltyXmvy06sYfD-O1dF0kt4NiYJmQe09UahWYQh9abgRjCrN5L79gnrUCztGaZmAY0Yf4C_P7xCv_sR4vg9_Lm69EI5fBX9ic-wnqfnKIEoNcQ5AD0UHxFmCDu6qzTUzuq0GYsEtNJbG7-Le9oUAwyPFBgW63I2IRhbY0CdCTN6WftStwnWzydpt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر رضایی: اگر آمریکا و اسرائیل جنگ جدیدی آغاز کنند، تلفات وسیع خواهند داد
🔹
محسن رضایی در مصاحبه با شبکه نیوزنیشن آمریکا: اگر دشمن خطایی کند، جنگ بعدی دیگر مانند جنگ ۴۰ روزه نخواهد بود و مطمئن باشید ما توانایی‌های جدیدی را به صحنه می‌آوریم و آقای ترامپ بداند که این بار تلفات انسانی وسیعی خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/444952" target="_blank">📅 22:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444951">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bec861830.mp4?token=ukTmnXIUbrzTbo8tfrPLNbz3M6o4Y8GCq6qNzOY88NvebyFSAG9RbGolJsf2h5wIKGxIweNatYq-Brq5UMP_yq-M7CJp5zrvLCNDiu-lGv-syff8cBm5D9kCtfihXskNEymC-dVEjhfzLandOw7rIgtVtZ3xL8X6tP0Sga9UfkfDIUkZMZH1a7KsXHTojBvfzG6g36OitZ0ZjaqOlJ-jVn88zLXkFzagTTyrDNYAISGZHqg_17CffQ6Dsv3Un40AtECfuQPhyxeGp91LoEsPEH0WxtEMHduWeP5VRfDhyvy42uHo8WQJzKRr_1iVLkIBtzMV2Rg-p5hmV1kS4I6xGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bec861830.mp4?token=ukTmnXIUbrzTbo8tfrPLNbz3M6o4Y8GCq6qNzOY88NvebyFSAG9RbGolJsf2h5wIKGxIweNatYq-Brq5UMP_yq-M7CJp5zrvLCNDiu-lGv-syff8cBm5D9kCtfihXskNEymC-dVEjhfzLandOw7rIgtVtZ3xL8X6tP0Sga9UfkfDIUkZMZH1a7KsXHTojBvfzG6g36OitZ0ZjaqOlJ-jVn88zLXkFzagTTyrDNYAISGZHqg_17CffQ6Dsv3Un40AtECfuQPhyxeGp91LoEsPEH0WxtEMHduWeP5VRfDhyvy42uHo8WQJzKRr_1iVLkIBtzMV2Rg-p5hmV1kS4I6xGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های گناباد در شب ۱۱۸ مملو از پرچم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/444951" target="_blank">📅 22:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444950">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee42512ab.mp4?token=GV5KIjgJ1DnVJNsh0LsGKMPjNfRVjzwZa0Z0K8X1jO7Po91s7hDI6c5FjqRRq_BlJSADhixLv219ZyRqLXpT6meZWF9FympmZ3kWp-pYunv8nPiutby2m3vJRnVGgKKOrxIXTP7Q8tMXK-X9mD-aaEY7I5YiAJKbQUbmsYuC7IvIKjcMD6sknv14mDJ8hXw19HnPgJcSt4lOL9UxkelUV2yrs2xNJjDCkt7AYeE9HS5Q8mihL0VFY8Cmqc2vtH_0J-ufnICEp3qTeB4nn3i0X2HMl0nrMNO-MXMi_xwrxRsc_56DFd20MHvsj-uv6MB1KvJeeo9jNaSbo0MM9GBj1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee42512ab.mp4?token=GV5KIjgJ1DnVJNsh0LsGKMPjNfRVjzwZa0Z0K8X1jO7Po91s7hDI6c5FjqRRq_BlJSADhixLv219ZyRqLXpT6meZWF9FympmZ3kWp-pYunv8nPiutby2m3vJRnVGgKKOrxIXTP7Q8tMXK-X9mD-aaEY7I5YiAJKbQUbmsYuC7IvIKjcMD6sknv14mDJ8hXw19HnPgJcSt4lOL9UxkelUV2yrs2xNJjDCkt7AYeE9HS5Q8mihL0VFY8Cmqc2vtH_0J-ufnICEp3qTeB4nn3i0X2HMl0nrMNO-MXMi_xwrxRsc_56DFd20MHvsj-uv6MB1KvJeeo9jNaSbo0MM9GBj1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج یکصد و هجدهم حماسه‌سازی آبیکی‌ها در دفاع از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/444950" target="_blank">📅 22:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444949">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f778503301.mp4?token=AJ0lWYyIWfRh6iLmlDeb8OMHk6455yD0S9Pzev1is0ApUxIsazVEP5-SFw_5lD6D4IV0SxEsnfgoaK7cWhVj_00expKndBIKmOAaG6RW5sZmCoz5bRvKrSyIndMHaNRu43pWiALh60TrcMGphgdjn9ofhOPdhxHW1I1Usb5601BEApCj9hV4Bie0JU_tDb1ZL7bzRoo5lfhZ7fetXFUlY-xGVpLdSJqPlk1ygi9ogXCdkZQpcae0mpwun_61dsAz_sGeUbWtE3BYHtkc-AR8h8n3SIfDuReLDBtqX1OBiOMY-iWIuef8uuLkefNb4lZ7E0UWsEXUWhp1BVJpVcpnVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f778503301.mp4?token=AJ0lWYyIWfRh6iLmlDeb8OMHk6455yD0S9Pzev1is0ApUxIsazVEP5-SFw_5lD6D4IV0SxEsnfgoaK7cWhVj_00expKndBIKmOAaG6RW5sZmCoz5bRvKrSyIndMHaNRu43pWiALh60TrcMGphgdjn9ofhOPdhxHW1I1Usb5601BEApCj9hV4Bie0JU_tDb1ZL7bzRoo5lfhZ7fetXFUlY-xGVpLdSJqPlk1ygi9ogXCdkZQpcae0mpwun_61dsAz_sGeUbWtE3BYHtkc-AR8h8n3SIfDuReLDBtqX1OBiOMY-iWIuef8uuLkefNb4lZ7E0UWsEXUWhp1BVJpVcpnVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران یک تنگه هرمز جدید ساخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/444949" target="_blank">📅 22:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444948">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b7e35bc0.mp4?token=Sfjf66UvBIjDAWMXyUSOuDfO-FtiEXU31gZQpH6fMOiqF-iyaKa3tmC3-bD3tLfNum5hVLJY1BjRokLSSNsifcSAuBnpXgEFNHh3wK1zoH6jEH0ZW9WNq7YNfwye-rc65xcNbfVSAfUp85VQ1GJn7wzMTr1dEj0vwXyQ69Wr4hxIsPXd6a8T6bTo_GSTE_eKPqWeMtLmk6hkxrpcNrsdst2rfYQqjRfg9kW1g3la1a4wvCTJU58SK8Xzc9LMbad_2HidgT1Agw9J8qy_RhbpOxes-mNoTQCrzirC1GXCqtNs74x544_pSfvwngg0zAZ7uJCwdibP1X9NI0fakeJSYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b7e35bc0.mp4?token=Sfjf66UvBIjDAWMXyUSOuDfO-FtiEXU31gZQpH6fMOiqF-iyaKa3tmC3-bD3tLfNum5hVLJY1BjRokLSSNsifcSAuBnpXgEFNHh3wK1zoH6jEH0ZW9WNq7YNfwye-rc65xcNbfVSAfUp85VQ1GJn7wzMTr1dEj0vwXyQ69Wr4hxIsPXd6a8T6bTo_GSTE_eKPqWeMtLmk6hkxrpcNrsdst2rfYQqjRfg9kW1g3la1a4wvCTJU58SK8Xzc9LMbad_2HidgT1Agw9J8qy_RhbpOxes-mNoTQCrzirC1GXCqtNs74x544_pSfvwngg0zAZ7uJCwdibP1X9NI0fakeJSYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ دوباره ترامپ به رسانه‌های منتقد جنگ با ایران
🔹
رئیس‌جمهور آمریکا دونالد ترامپ باز هم به رسانه‌های منتقد جنگ با ایران حمله کرد و تحلیل آنها مبنی بر اینکه ایران بعد از جنگ قوی‌تر شده است را «اخبار جعلی» توصیف کرد.
🔹
او گفت رسانه‌های فیک گفتند که ایران امروز خیلی قوی‌تر از ۴ ماه پیش است. آن‌ها (ایرانی‌ها) مشتاقند که توافق امضا کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/444948" target="_blank">📅 22:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444947">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a29cf8fc.mp4?token=baXpv74ejIqQNuKGjbaxKClX4Vkn3mXSSoZ_A6VtgV2Oemug1SiWwkQek5ZaxqA-NQ2yujeaAKj7AeOG7hVJnm3yAp0cY3j7HYoViIELbQgC1FJG7gJQJvf_SmOfcI57jbFc2D2pXotumTGQoZjt5WxIi23UBiE9OMididmP7L8zRhux56xXnLP8lj8eCphFAD2PVamZDrC-HjDjkUdmHrk2nl4wv1XoQy-pwefGXmgv5H_Fq5EkYPbhgIQD-iHEqFMyo3R3LnxaD2rXO2mjdtF9S023Y95vrWC7DSi94JkWNuMS5EjOAxsWKm65W0JsEq082ySHCmZRAGpYdqh8Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a29cf8fc.mp4?token=baXpv74ejIqQNuKGjbaxKClX4Vkn3mXSSoZ_A6VtgV2Oemug1SiWwkQek5ZaxqA-NQ2yujeaAKj7AeOG7hVJnm3yAp0cY3j7HYoViIELbQgC1FJG7gJQJvf_SmOfcI57jbFc2D2pXotumTGQoZjt5WxIi23UBiE9OMididmP7L8zRhux56xXnLP8lj8eCphFAD2PVamZDrC-HjDjkUdmHrk2nl4wv1XoQy-pwefGXmgv5H_Fq5EkYPbhgIQD-iHEqFMyo3R3LnxaD2rXO2mjdtF9S023Y95vrWC7DSi94JkWNuMS5EjOAxsWKm65W0JsEq082ySHCmZRAGpYdqh8Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامه نماز استغاثه در اجتماع مردمی گرگانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/444947" target="_blank">📅 21:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444946">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84b642f256.mp4?token=reDVW7LMREO_lKM5uD8vCbslyW4fXSgSF1j5H_HnurpHOKjpY5Xe1UK0mkvjSIQzjEjTNEt0CA_1KBAkg-6cSlmz08OXRJdo5oIo2-zRfD1LUPfYFwxjXRPQHxSJhYwq1xU2dzWvNKifLUBfmdFdnSYn_7q-vO_f83RpO-nZFshBzJCXpFDDQKyNMdQXG89Olnv_q6OFhhb2t-bN0ehrT-OnOyfybfzlumvXf_tzRE0OyFuIBg0ETXgbwkPcqCBRRIsouSKXDQpvily3LeJgoefFD8tDSSvb91xcpwlz8E3UJBaE-SlFyMMr5Fl7cWWor6Q-amMu_pktyq7PBZz-8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84b642f256.mp4?token=reDVW7LMREO_lKM5uD8vCbslyW4fXSgSF1j5H_HnurpHOKjpY5Xe1UK0mkvjSIQzjEjTNEt0CA_1KBAkg-6cSlmz08OXRJdo5oIo2-zRfD1LUPfYFwxjXRPQHxSJhYwq1xU2dzWvNKifLUBfmdFdnSYn_7q-vO_f83RpO-nZFshBzJCXpFDDQKyNMdQXG89Olnv_q6OFhhb2t-bN0ehrT-OnOyfybfzlumvXf_tzRE0OyFuIBg0ETXgbwkPcqCBRRIsouSKXDQpvily3LeJgoefFD8tDSSvb91xcpwlz8E3UJBaE-SlFyMMr5Fl7cWWor6Q-amMu_pktyq7PBZz-8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم پرسپولیس که پس از بازبینی VAR مردود اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/444946" target="_blank">📅 21:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444945">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4f2cce4d.mp4?token=X5WD3RzgReLOeXUatbtdq7p2hiVRxJLxeCwIq_JPswwL_Ig9YiqYHwewwnFst3xe4FHlsNSoGwwyoMnMaQ3jGkW9XjXI8N6Ee5UMSbyE-L4Fi0LUcvXJ7BKq8hGHwUH-tQc83kqcamUBsIq9-pATwgc7c8RMx-vPwQedBUX4_Q_RyI184_1UqdwhqEnO68NptuvII5xllKlEyxuG8IZNdQ1aClB-uqpMiZwMhW1av8D9qxikQrvwEXb2hgAFx3vWQDy9WTeWznBqBDsUAhKl7q6DJ5k7wJZHGeTsG7oH0yqbBsvGgsiWdkUoityXHrtvBMt1UXdZcBOcPiB54cCDHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4f2cce4d.mp4?token=X5WD3RzgReLOeXUatbtdq7p2hiVRxJLxeCwIq_JPswwL_Ig9YiqYHwewwnFst3xe4FHlsNSoGwwyoMnMaQ3jGkW9XjXI8N6Ee5UMSbyE-L4Fi0LUcvXJ7BKq8hGHwUH-tQc83kqcamUBsIq9-pATwgc7c8RMx-vPwQedBUX4_Q_RyI184_1UqdwhqEnO68NptuvII5xllKlEyxuG8IZNdQ1aClB-uqpMiZwMhW1av8D9qxikQrvwEXb2hgAFx3vWQDy9WTeWznBqBDsUAhKl7q6DJ5k7wJZHGeTsG7oH0yqbBsvGgsiWdkUoityXHrtvBMt1UXdZcBOcPiB54cCDHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به چادرملو در دقیقهٔ ۲۸ توسط محمدامین کاظمیان
⚽️
پرسپولیس ۱ - ۰ چادرملو @Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/444945" target="_blank">📅 21:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444944">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc67743625.mp4?token=b5ngy8qHLxssPxc4bf-isQgOz8qU_3EFQ2fThvutFgONuVJ9ba4qwEwaXPikzmSbxoYMR9KIKriuNfW5AEEAULEulpUa1DH72IrSw5mXUXOJ3QltDQiDhEYMfVmNdd1IPbu4Y8ehH-4FhrCyIliiLF4t_3Y0GwLkhVRQ7qsWjWC4Q_tKjkyZ81bSYZPkXRkohiFgX0jHZ81xHIsFGmdhbsKnjHxxzlhnxwA8WMcVOvAU861XS5oIO7QUKStzpZXqsrXNM4e1Rsi0LKkEeGqcTsYp1FamTYQQJnSEnfPcJUMFAL3DH6jwRYWQZKEIeKoGp1G-olXplIJ-Jvws7Wgh6pYbsd80qU9cyt6Xvil2TYfJ6TX-uo_IvR-rYizrPfv56qOZWRbbjtzsqIRpsQIBykmIJ4WR4POExIlBTAJNaLjR3YYJIxPouVGXnUHyE9vnRXBxh52BB9EEywhv8N1LbDEpuFVHdHMFfFaLUEbReWChhub1P12PZPaTAfYd75brsGxeAjDRSDDeqDzmWIR-EmV1NkDRMCBKPZ4jvu4V_YFEUhmSEPs-ydKtESc7M1mfhZlNU_u65Kpp_aJcVr5avSKnVhezin3zyzdRK3kuGJVWKE7a9BXcpxrW-pHzxPatW_RSS6wukI9Qe0dZ1LcD7MGrIBqy3nbF-MxBcJ2gK74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc67743625.mp4?token=b5ngy8qHLxssPxc4bf-isQgOz8qU_3EFQ2fThvutFgONuVJ9ba4qwEwaXPikzmSbxoYMR9KIKriuNfW5AEEAULEulpUa1DH72IrSw5mXUXOJ3QltDQiDhEYMfVmNdd1IPbu4Y8ehH-4FhrCyIliiLF4t_3Y0GwLkhVRQ7qsWjWC4Q_tKjkyZ81bSYZPkXRkohiFgX0jHZ81xHIsFGmdhbsKnjHxxzlhnxwA8WMcVOvAU861XS5oIO7QUKStzpZXqsrXNM4e1Rsi0LKkEeGqcTsYp1FamTYQQJnSEnfPcJUMFAL3DH6jwRYWQZKEIeKoGp1G-olXplIJ-Jvws7Wgh6pYbsd80qU9cyt6Xvil2TYfJ6TX-uo_IvR-rYizrPfv56qOZWRbbjtzsqIRpsQIBykmIJ4WR4POExIlBTAJNaLjR3YYJIxPouVGXnUHyE9vnRXBxh52BB9EEywhv8N1LbDEpuFVHdHMFfFaLUEbReWChhub1P12PZPaTAfYd75brsGxeAjDRSDDeqDzmWIR-EmV1NkDRMCBKPZ4jvu4V_YFEUhmSEPs-ydKtESc7M1mfhZlNU_u65Kpp_aJcVr5avSKnVhezin3zyzdRK3kuGJVWKE7a9BXcpxrW-pHzxPatW_RSS6wukI9Qe0dZ1LcD7MGrIBqy3nbF-MxBcJ2gK74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت‌پردۀ سفر روبیو به کشورهای حاشیۀ خلیج فارس
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/444944" target="_blank">📅 21:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444943">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUazBL4W8_cz4rGEqpz0IovNgxVWbGIXdjVgauJowwAh5xyO-8MEID4rEL8krFg34pYn_yi66mScpRquH_o5iyasx5LxN2hS3FMaVK-0Y7OPatBL1_4hzV2ye10csoZYq_wgtp_5cdtpwFHczTq-zyOxiyoR1FtUmWSSyIbgx-I9lMQZlhrvLuhok74w5SYTrVK6buNEWbo3XjxvwzEUN2qG-meHse9twvCmbMUa1YmMZUN9qwTpYc6jSKk9936-l7EqLsXGgXuH7jCaABY-jaDywcIQcllka0pzahJbrje04WlK0DcgS83rQMkD9Ov0EKzFJ_pIytYFkGAxktthdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای روبیو درباره توافق اولیه اسرائیل و لبنان  مارکو روبیو، وزیر خارجه آمریکا مدعی شد اسرائیل و لبنان پس از مذاکرات در واشنگتن به توافق اولیه رسیدند.   @FarsNewsInt</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/444943" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444936">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feWpcY1kND-RbMLVMoOIc2MTKQZ4P1k5rlon6J_peov-UhPidUVrhCZOjoeCkJiUqwpYrjWfa9iYc8NGam6M9oSHnExLjUuQCGb5Ys1L-cjuWU8VAI7hDvUayxnzq3Rw2puzeXioJQLItVnmTelPpBky_0YWBzrNUvvnYfcVnB7AlA3RQ9QjREG_XIAL5kvRM3pEng1d_Z938jh02gzcjOM7N1qbKStUpWF-Gkf96rm7nzLs1Zhx0g6nXf_8-wRz2UguTw-Vsb6Rj0pgxLl6hZd0HFXZJZs2-gyVHe-pvxyKKQiyF9WGVnGIj6f9F9nzTXb292WgGSLmeQ9Q_EHT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3BkkhSkRt0L4-bLFXsOjqpBo_caKKLbzUcU9OHPLGaPjqUEXDiY56LwcW60hFXR8UygDYAlvMaOrpx6Kr0LmFrT6Nr1tMUwox5cvVcrVsvH1SC1z4Fyw4O31W5DLKVsVGF1aJC3Dn7Tub9Es8pA57-dXVVTXWIl_FhFh5yIPZ7MfL9VZtL2IGk9y0C8YLKEPHV8sxam2HuPXGi2S9erD_0GEqbR39MpY8TovZ6fti1W6dHo1b2nqX5_Bzc_LXR16Ae91GY_w9qqki5KbDGUBcVqwCxSWRTNq7infeOXamrCSDqNo9p5oRTAQGjs9pxiIyKtvZP0nwL_YcgyASy5wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-v-5iBHno88ia0F8CsY4SUdom8ReoV7r9fV7r0fVMdWI6tAaCH85f0OKBDRT5-QWfDLLVOdO6y9Z2-TS0rwPG7QQ7eAlF45Lx9vkNyBNyDswxwO-pfs7MK-rjXpfdkG4XyhgIRfqkFolQ0TdMrATu62PW___RXMVv5CCbyLkoY8M0TPI039gKUtX6Jmpf2_U5EYgyUq1NBuNq2VfTfkC2k7H0aKH4HH5oOBvItRu5oFKqFzzhpWcB5MwE_JlH_3E_hCssb5UY0SiX47g4iSoh_KRtl09ma3REEtmDWTrnx5iK56BFbt18a-E-cU5yUj3PvpZesvQeczMqeBX2ueBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HnYsi9kcE3swNTmM_uSVj4fEL-9PHpV1KIxVVV0lSyOLYX22rCQN0QOoo84y5J0GXMO3uWTy01KOy3e0Vs9w1tnwQqlD9-VTaqfPQ_YmaE542y2C5AGsixRMZpp6UZRLn0yqiCCxjENSUtlmdOjRxaaWjQfAqkYB8tfpBYAdtY96xGIsP1wiy2iP6AuX6sS5UD1g6UJBPAuBC8S6I-JRBX3P-31_kgmw8gw0spVaq7ZNCD_a-Nk3s2aXh4PMBynyQ_jlXGSIeifvbsYT9iPorD1ygo29pejQj98sDtgquh7p4vKBXBZ4QZcoQZwINyfeE5CY7gfZqLrrJGSt3NUOxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ijb0BRsRh_4woC1lR6DGyopZA7K_jxYbL-Zf4ps4I21CgmeMZzcGE6bTFviH-1zyofGD97nMewCj5LzvrFtk_n2z8WO5c6XkEmdTNIJDVkkKlcJocx95trpu2B9omjwtoXb8mXEpcUC4h0BkKOsY2hb-O34-FOluiN95bMbI1qAoTkoCe5OaTohd99wO3fsWXZlMPVR8i6QLtq0aW9Lm5nZGYj9Wm-gGLqDBSHdFAnmPYC4A8iqHVeRu5-CE-nFw9ysTSHACh-JSbV0hR75p2J5Rn1I7yFhjV6GdhbehVTVP5-0ZgkTxrQXv2KlTQDelVXqO2JXx1s3ECRIaYWHB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cISMNbLhTCK4hIP2M9lNez5ky2vwYlLESLVlSIiTeP4nqUDur55JtvvcKYKB7kHkBxzhNpvy3hfbO2gWX7tjvhkbhYTbowmUJ6dUrXE3yc8OJ1hnq4Ok638KdCqA9nTG6kUTg9ZY7RrWGnFIsTekvqy2gRcEgyDzJVR603fCThe_UChgLRcE9mL67rOcM0tqWqRQPIdtJwe-Z-yA2j5r2JrTgdkgb43rGcwzigYZDSgeSFscmivIAwaVfD6i59R-7Y5mhl29pMORDLxi_Y9ong8x9a32LhAi-clJg8XgYyzPIEvULOLPJcfM_u2kkD4CF1EXAn3mN1lM5awbo-su_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ocr8PhLj70Bx8McyFLfSUd-NgIukCP5i1EbauzfUTKbKM752uEA4vIcKdDCbGrPH000pWz4KBaTAU20euz_XlXJ2p4-4XUmKDjynWz9dOWA8JP5HQwcAK-JFAjm-aWoENrEkVrufj9r_UoSc8y2sHisB4Q8_lwWrZfVOCLAstBmaHqp_pN5XWzGTxmUBOaXUj-UyAiBUbdIcOFt80kepNMd78PWM3qCUpdXEjV4T6rEun00LaAwbs0vYMTci4JfG1em_bVcbu_1cpTHPzBOQ7-vX23UBHKOcpX5o5rTpPd1i1Tzlt8DWfmWuY56ihP1c0t2BEUyW6CUtFT3gjDhn9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین شب عزاداری در جوار محل شهادت قائد شهید انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/444936" target="_blank">📅 21:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444935">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎥
این روزها مردم بیشتر به چه چیزی فکر می‌کنند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/444935" target="_blank">📅 21:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444934">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pU3elWL3MZmiwK5sUgpPBcIrTMUmTXf06SaXqJ4xIKR6zbXWxfGf-53jjgLeOotbaI_eQxf6JgVVUt5DqXT4geID0u_GTkVh-UtWbFDQdY9p4IkHo5W6y7B5MT9pyngsXDRj3BfH1ZbpUpSmNE5rnupagNd2elKLYC_ut4ajU1cN4e_UU3Got-5AXGxIvU2dqw8lTDl7Xvr1ADrtCf8IR-cKl9PAIP7zTXr3436YamX_WBmqltkQMPIHlHCCQF7YSkllmJ0mduFd74pvqYMZMyNx2L7WRhMnJqgq_YSpjAWtfr-Yx6_0jHhlOs-DNvQv_fNAfpEvC9UQ5lgd3_uZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه در لیگ ملت‌های والیبال به سختی از سد ایران گذشت
🏐
فرانسه ۳ - ۲ ایران  @Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/444934" target="_blank">📅 21:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444933">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1q2QHgIR55cydfJMD2uP50ukVSvD0qUsuqszxbTJX6PTbjxWEVIHLKUYnyltW9oZ5_V_o_buofqd3bGkbRWHEfaoCJVzF3Fvkfm9GbwnYUQJUYB4SzgfWM3s5Ky9x5XdPHv0BWLUopw68PEpgDE_6J4UITzUp-MNs-b7BKsnZi_mEGxTd0fO9YoJpK9kNkwAXNxgn5TVIs5oEYICIXjqcNGpvtZBu2DyVhhgy6F4SWtEnyDBOtx2ELaj95s7lZn16dfcdVvDYRq1gbtx8JvGmaird244oybQ7f8BNC6nOQBRaifd0fS8JCl0_XKhzWQr4mHekS4BSSYyQ9qWI76bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای روبیو درباره توافق اولیه اسرائیل و لبنان
مارکو روبیو، وزیر خارجه آمریکا مدعی شد اسرائیل و لبنان پس از مذاکرات در واشنگتن به توافق اولیه رسیدند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/444933" target="_blank">📅 21:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444932">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d5088049.mp4?token=F3kuFbvEEdObiwRfJWGPq4t6gkgopGHM5vwFvZhNG1d08mjd4SOddRn95bkihySNPIm1SkfRVggfH2m7Xkm_Ye-a5OLE7FlUrDtmd7kWjw04Io-NgVHGDdutzedgfagM0pl3yRfqybJyaXZTPL9duZLAmb6JG9I8sA66DAIqY6wM9a8iMouYllGBXE3JMWGUI4SeZH4IDEUvgC_r0xaCMvfsr1_trkAlETa-_xyjPwXw_TCzIl_Faozkv8YtrK4faha8tJ8g3ucBIdRK6JKGOEttgxouwYV3tuMH0gK5P32Hrq5UAKhGN0_34_6G_ALNuRPdUdtiiNFUzDytYEpDjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d5088049.mp4?token=F3kuFbvEEdObiwRfJWGPq4t6gkgopGHM5vwFvZhNG1d08mjd4SOddRn95bkihySNPIm1SkfRVggfH2m7Xkm_Ye-a5OLE7FlUrDtmd7kWjw04Io-NgVHGDdutzedgfagM0pl3yRfqybJyaXZTPL9duZLAmb6JG9I8sA66DAIqY6wM9a8iMouYllGBXE3JMWGUI4SeZH4IDEUvgC_r0xaCMvfsr1_trkAlETa-_xyjPwXw_TCzIl_Faozkv8YtrK4faha8tJ8g3ucBIdRK6JKGOEttgxouwYV3tuMH0gK5P32Hrq5UAKhGN0_34_6G_ALNuRPdUdtiiNFUzDytYEpDjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به چادرملو در دقیقهٔ ۲۸ توسط محمدامین کاظمیان
⚽️
پرسپولیس ۱ - ۰ چادرملو
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/444932" target="_blank">📅 21:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444931">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ec14eaaa7.mp4?token=c9OMnxfHLoy3MrEIidY8iL_s4gg6ECI56RccVoULUF-rIADida61upx3hqU75Isny9JTeVIQ0-F0IvSyXWg7mnZbJMWJzU1iJOQOaGEjck0S1mXeqUEObFO9pZPNzhuP7fc4YGYHbOTq8Y69Ei5nF3CA89ZjOj4q-Zywr2QydRRODs2C-4N_DTIj9CbCkMuXMpqhMzGgKGQJT_cXJeo35XLhHoHCouxnPbdvt-8tFhKqXuQUzMgFpapuQZoLYsCo6i8ZLC3pYDIGYogQAvIzVr6DxGSl78Ja0DHy6fsgbmsn1kq7KmPgbwpW1Qu8OoBZKHxzhDQXTSouz4r82mqmCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ec14eaaa7.mp4?token=c9OMnxfHLoy3MrEIidY8iL_s4gg6ECI56RccVoULUF-rIADida61upx3hqU75Isny9JTeVIQ0-F0IvSyXWg7mnZbJMWJzU1iJOQOaGEjck0S1mXeqUEObFO9pZPNzhuP7fc4YGYHbOTq8Y69Ei5nF3CA89ZjOj4q-Zywr2QydRRODs2C-4N_DTIj9CbCkMuXMpqhMzGgKGQJT_cXJeo35XLhHoHCouxnPbdvt-8tFhKqXuQUzMgFpapuQZoLYsCo6i8ZLC3pYDIGYogQAvIzVr6DxGSl78Ja0DHy6fsgbmsn1kq7KmPgbwpW1Qu8OoBZKHxzhDQXTSouz4r82mqmCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیلاب تابستانی در مرند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/444931" target="_blank">📅 20:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444930">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
رئیس دپارتمان داوران: قوانین جام جهانی از اول شهریور در لیگ برتر ایران اجرا می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/444930" target="_blank">📅 20:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444929">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2CnQzf_lewMstiewa50lERHUeKh9WqmzSk9iwZZn_-NNArLJrsFfm4p3kbN0ag1FCS3Vc1BRp5jhreuRYF2iKeer1jHESVMYXWwVru1i0oqPcG-unpP9IlPse4-3LKCuXLkYbe5y781DRzBcjcHkqyr3KXFN8zTM98Yg-b5nrbAUeY0J8RKaplH1dgiQpvAB3SxFaUZ5ViLA9drlXVZPwPH1KidAWAko6Xn5XZwyK3rHlEE6XPwjBF0LSXGg3aGh4JuHvVODsaGH--lRUVvKQ0ezlcDgzLwFYSOxzdBc_dMFlmargtGE3FbMK6Sxt7vy-pwGjeo9GnbeF-qsj_ZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمدید مذاکرات غیرمستقیم لبنان و اسرائیل در سایه اختلافات
🔹
وزارت امور خارجه آمریکا اعلام کرد مذاکرات غیرمستقیم میان لبنان و اسرائیل که قرار بود روز گذشته در دور پنجم خود پایان یابد، برای چهارمین روز طی روز جمعه تمدید شده است.
🔹
این تمدید پس از آن صورت گرفت…</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/444929" target="_blank">📅 20:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444928">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/996699e984.mp4?token=kpZGTL6Q_gKwqGho3jyAiTLgMzQlG7hqmHcYo6T5fB24A46OIZ4NtwSvYp2WQCWHSFPGCAL6f7b8N4C-DQ6RsSH3bXGm45pUQOWKQ4ougBg8C4WREAPrglHmP6YjqHHsjhV3xHVIgOiSYgadvY36IaWrzBVjLeXcgeMh6tMK8Tiz6si2yErVmItFiP60lxVaB4OpXFeVUAzZLG3mvKgPfPrkAq3NsuBAJiy6ahQHcIISEv9R9VpDUsP8ZhA__m85hel0qZjiVGcrTzCMPFu7s2yTVtU5Ms8QnLrOmFRHbXtfCFUsHTCeAEs4CEmNf6dEg3NR1bCzfABk8vyiE1cy8qh-1s1i6-huqlhbpbjdDRmFnhq50hsgHqZfavI2VsTe9FpjmyD1aPjFjGXWruE-CUiFAab4U1ER-Ut4rX3phIlLgToa6xqK-m33wdL-mhmG7mHOLuLRHTfKXlwKnU7QtfJqC4_znJqzSbyVDD4rB29hk8lvzNiuz_QrnP-rMj5b94oD4pDHh5F00YQK8rePxPC2HyAyQI2UCwbDabYZyVv6I4k3N0G79ehKvJW7Ch8ueypWWynys0c3moetk-E7i1DrhbdUoDctJr21VbJ2nd_-hA_pmjGl_FlaZgvFGkVxi0lp9s8e5v7z_g9xwGHe8ThCpjBmmUYd0TRalTmmV_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/996699e984.mp4?token=kpZGTL6Q_gKwqGho3jyAiTLgMzQlG7hqmHcYo6T5fB24A46OIZ4NtwSvYp2WQCWHSFPGCAL6f7b8N4C-DQ6RsSH3bXGm45pUQOWKQ4ougBg8C4WREAPrglHmP6YjqHHsjhV3xHVIgOiSYgadvY36IaWrzBVjLeXcgeMh6tMK8Tiz6si2yErVmItFiP60lxVaB4OpXFeVUAzZLG3mvKgPfPrkAq3NsuBAJiy6ahQHcIISEv9R9VpDUsP8ZhA__m85hel0qZjiVGcrTzCMPFu7s2yTVtU5Ms8QnLrOmFRHbXtfCFUsHTCeAEs4CEmNf6dEg3NR1bCzfABk8vyiE1cy8qh-1s1i6-huqlhbpbjdDRmFnhq50hsgHqZfavI2VsTe9FpjmyD1aPjFjGXWruE-CUiFAab4U1ER-Ut4rX3phIlLgToa6xqK-m33wdL-mhmG7mHOLuLRHTfKXlwKnU7QtfJqC4_znJqzSbyVDD4rB29hk8lvzNiuz_QrnP-rMj5b94oD4pDHh5F00YQK8rePxPC2HyAyQI2UCwbDabYZyVv6I4k3N0G79ehKvJW7Ch8ueypWWynys0c3moetk-E7i1DrhbdUoDctJr21VbJ2nd_-hA_pmjGl_FlaZgvFGkVxi0lp9s8e5v7z_g9xwGHe8ThCpjBmmUYd0TRalTmmV_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعزیۀ «عطش تا آتش» در روستای صحرارود فسا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/444928" target="_blank">📅 20:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444927">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRArSbW9z9e70gZH8K9P01zKcw6qulh_ziT6stOeQLPvVPmp6jbzPLRMeAjy65U-sWEpj9hezlyX8aJywLnjE6VLzLj-bDqZsnljfF-bQGwt8SLW8Amp10rMfD3GZCLXPYOTqIc2eAqazOwhx7sTc8VsNyjQTsCzNUMnj9c8EJK2-dJ49BM1f_rqEHgUcsHqoQ0m06offtHgIeCRJTpMj6KJ0Ee6_sOGRMkheUKPnWS3ISdIr--A7j31hQUMIaTbqUzU04oxhzgo2qKBO1ZO_WzV8tpipFpVXJU8HlFQZ0oSq3TSJAW4uH7Fs9VMCrJHOvbsl2L2wEr5DBg9UypZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: تنگۀ هرمز سرزمین ایران است و هیچ ارتباطی با آمریکا ندارد
🔹
سردار محبی: به دنبال ادعاهای مقامات آمریکایی مبنی بر برقرار شدن خط مستقیم بین ایران و آمریکا در خصوص تنگه هرمز، اعلام می‌گردد این موضوع دروغ محض است و به شدت تکذیب می‌گردد، این اتفاق نیفتاده و نخواهد افتاد.
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/444927" target="_blank">📅 20:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444926">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NddmSRVjGa0R_SCqQvnLBXVnR1kZNE8cr2D_qxAXQMiaz6Pui3wHRqaq06S5TSbZKYUuCwGiWhfkGW7pXDdFGGxyMguA1DSzhyF73CxXbkOOZS1xtg4e7sRW91xgV1WHm7iHBb0nxVrzPaS_k_CriOgxry7Z8NUvxUOgHk3gBlwOq0oebVjnOL5TYpfKGUCn-b3wtKttAdU061VMQjidOESCVyid2GMo6aebjsNW0uecBVjmGkL5I6wmZdIXMQiyFyov1LHSU7zCdrsudaOPoi1iP4GfWtfdRmSn1eexRkXvop5cWRq4c5VqtGvozbBoOyqVYYMdLSNtFUjHsR2E_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تصویر رهبر معظم انقلاب و قائد شهید امت در دست عزاداران طویریج در کربلای معلی
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/444926" target="_blank">📅 20:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444919">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRzBaZHHqfQXC7vd5Eyjo-GtFrpSmCXwKRYwoOQx0nxaOURdhET_TMDZ9AzFe05LI9oxc5cANCYVcjbi6jyuqlL-7B0rF_c30m0jnjU7ZyOsdAX57yEXv_jUSgCvbxkwPhdXw41AVa2CKm4amoT5mNNDCvYAb4woBmYvPh5GqZWVvac8JnEMkH4CkUxAirlvHG0WL_Z-PX-6_ijpfjlo7sKWtbq5WGuhU3alf_sDPod8CPsl1QbAJgIH_ZgwinQ0XgOPLHRvXUEuJ4pVxWB51zwbeZM5PliFSOYMMcL498JTle7gJM5mk8FdgRlOCbLiaLjXJ4yz2f8VD7f5lQMVyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugA7syaVcrnkhExftZkXMXDgTheYjBW62vrUtPs9JgkDeqFID-jp7igi4nJSKz6f8TvR7GQKmeynIOd68Cf-l1NcnZM-s3G81t0_IInfoNG2FqA1miWvfRGqQRZeoaXPbW6-Bv6DPqkrC30tSBFFx-7FmgP-chDV2ZLWtcLRk5QeN-_Jcbk-Sjrg_jlXXFlb4wb06a9eNVEFl5Qv4V02X8sxv5ISApPBj6spoPZ_66I-pcLdYy3BihLDPVXXsmqLkEJP64yMP9n1Ai1JywN0vQSUBTmxE520i63eJU-DuowdQvt6bSLtvuFYKbNvAmHa2lfaPqAtDe-Csjr5CmrCNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qvo8CejEzkeNUFrtlu1urw9NlSBMimzOm9CA8d8K0IIvIbZLxOSdsx4MZjvOJ0cLf4ZWcT8rRq_hqYPwdhdauh3eON0ULzB6AqPJvKHSkFGiOeWM24rAvpogmgDfvA93RfTsmlhNXegH02br_IA5dhjlKvV-1wn5ENi5U8G6aH-hMmOkIruXrEqmOhJzoXPgkUl1odXpD2Vy4YaZGASyBGJ7YIVQs6UvGy2RZPUlPHmAtv1P9ycNx9kYfwv7ordw9GY5cIfMq2_JMT5h709LHHEV01U8HRVmpU5RYdJwQfhQt5oJd1xtiNBILiRqmf-sxJMcCHdxpSew21yNPL8rcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhdnD-wKNuJ_PFgvju_spbUGNtHrdwX8OgCFuWlmdiNiblx9_LYeLMkrX7OB_jaelAabqhY_d3bOwwYRb6bcUdKktmnTZlF2KmKhkBRFoGwN5PAY2grsT8LwwxtUUck3-HId9uIFrtr29sWKACJzSSqYhCKwioVBQ7Nbe2_O6zEADJ7uUszdZaSW9OrXvtiObrIglhJBH_N26_qzfQ3fhK0Z8L1Jb2QpyNkmtyEYLptQ_hJ7tgv4yS9BJQtg2ghGCE3gLfD4T75qXPRpBHYEfW90vGkkVQsQ3BmzfxervPXlbX3vCLj3nT95VMqkc8CC81RNqzCJ_qlT_NwpIbwlAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/laIaE23Y32mDQp5ON_y-Srtj9YwjR9YvAqvsPGtVuahr3-5xOuUJPWeQtQZ4XekLFMe1YxO5sYxfWBqe5BxV4Xq5f93XclhHZfU3p5oUoAQq0KF81xng11pR-nxD5PaHwNmaLL-mGR0G_ueZEFIyVSuIQP7O8k3_2AiHmBpdL5U6eFHWnbA5NtfiagQCAN5imxcs0l8x1ycxJ3DD_F-rb0j-af3gVr2VWPB-nFQSIzNafPhEl5SVRsAaOD-zUBxxd-8bl1-BXGYQc7fY5SG1kd9TyWg11IAeIZ0UfWNtQbudqsfmzS0pq8JzxyOfFKyzCzHa8fr7pWF4V6NZPnaPBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCKAEcbKzMeRU-aFmipnAjCwJzFp6bqF5HzTX3fj-2VsolYenWvDLWBfTQC5OXqq5sDYktGSLZn9nObADab1O0as37g8xZFoibOUTt-rTI4T-vX4Tfu_G7QSkjUM_qwguhWWDIiqYiPUMwt7EenEaM_TEPbBdyCLkVbmODMr5xB3plGr9WlK9zZk42BsvFBn38XLpkzz5lnYWLMpdFhIedGOXS56D02ZlJ_D1i9x0u8IMJTp2lSn6DE7gbVsGS34aEQ4WIk6KBqu7wNT10wnx39F-tk-E7BWgltrJ91O3AQ_oLhTvKBinBmxWQSjZuEED365jCDB5JaxKqhew54mcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEhat27mFpGZnl_qXyFk-U4SwrTWnrkL6Ae9KmNmNOXJ7Dn8yv0I7RHI3VNkiiw52Js7A97isHxfHPxoxBXik-mJHCN-rnT2bf2haVyzjKEPlQAdgy3Pc79rV19Yz7UygOxAkSc_1JEnSroUd2qoakKL7QF_WvQB-PFQVZ5QFjwX3sku1b9M0y-GOzP942Qm9QZ2wghsVkx7CA-6I6gr9utUUIe2HxtN2ScvwXXRs9jplxYSS6c3ZyGEAeYE82V8bQ0i9yQ8nWQ6C1opxCerhrmzvgkN5IBbGx0EYzTuQlDVOD8CWHR0smv3RKENQQD1f6VdteRt_Mi1slEc-6EAKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تعزیه سنتی در روستای کلوت میناب
عکس:
معصومه کمالی
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/444919" target="_blank">📅 19:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444918">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7Mvak48HgcmcwwPhdHabkEDDZvyCeMtBch7erJE1dgEj-ayty-ssLJDtoiKlV_8iN3JR48pjqmf04RvfxUiM8tastt6vmsNY4w37nYi_YWiptVXE7muDgFZyERRETK4cgvN7rYGDGiICD6nLNrnazpX5Vwizsxc19tm8TAAlz5iBUwWUwy9YvUslEyVPyQMhDCqWpNI4DJtRbYYNGGWcdsRr-YCMzbT7D12o78nXzrs-tsN1_egzBGFJDk4XNpDPS_e7qfnGysO2gmU2OB8C5Q7MPyTbs_GIUsZujKguUYydUTGnkyQLOisxASAXS_KKvAvwNrGIPmS5nT7OiODFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
اطلاعیه
📣
مشتریان گرامی بانک ملی ایران
ضمن سپاس از همراهی و شکیبایی شما، به اطلاع می‌رساند در راستای به‌روزرسانی، ارتقای زیرساخت‌ها و افزایش پایداری برخی سامانه‌های بانکی، خدمات مبتنی بر کارت بانک ملی ایران امروز جمعه ۵ تیرماه ۱۴۰۵ به‌صورت موقت از ساعت
۲۲:۳۰ تا ۲۴:۰۰
در دسترس نخواهد بود.
پیشاپیش از بابت این وقفه موقت پوزش می‌طلبیم. آخرین اخبار و اطلاعیه‌های مرتبط از طریق کانال رسمی بانک ملی ایران اطلاع‌رسانی خواهد شد.
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/444918" target="_blank">📅 19:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444917">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGeZgom0iwxQL4gzYa8jKfYAgvyFJZwjVnHr7GwwnLqodxbgWpAxZbIMII_B96hkUy8Sdlgj3-84O0o5iF7yUH6brJrGfligJoDHhKo6LJ7C3FGd5-luSgeEc95p0sVglpKJT0VBJlsbNvW9lUrUdhpKlWai6wOYhTAB_gUPTeqnkgM0r_MxLx5LvA1SrbofWO19RwoY-KTsxFEhdZLliOnxlErd6Gh7ArfNazKEfmBGopcjSxgxWGsqDDFCEP1jLqfjgNqsbNBnRlHw5mxaOdA66MDOr-tt_7lsBQoH2xXxx26YrEWEwvoP7j4b_BUAPllm2EL7QtvoQWbB9-ZXMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/444917" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444916">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/444916" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444915">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌  رژیم صهیونیستی مدعی اشغال بلندی علی الطاهر در جنوب لبنان شد
🔹
ارتش اسرائیل مدعی شده که نظامیان این رژیم اشغالگر، کنترل تپۀ علی الطاهر در جنوب لبنان را به دست گرفته‌اند.
🔸
این ادعا هنوز از سوی حزب‌الله لبنان تأیید نشده است.   @Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/444915" target="_blank">📅 19:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444914">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFiX0Nzbx4HVg_Hk6vl3rgdBrIOSylPZ9ADNeTPMqDKsAecGr131ohJ2MZ6BnCzYL3HN2crrmqA6YJwYLQM386hL6wbh3uQnT9gh8r6oaUdQdPct-wapLOFlBmeaarD1uQMXCKb6CJr7-W2aNbIJqPSB_RzRIrg8XwpuDrhzxbrkzeu0qmSj4kJWLxu0C8nZ0EkjdqOP3Fbt-8en8FTMEFj62SszLYwkA5De5N9vz5oeQnfLMnTlr5gVpgwj-GAKhiIKlfZnk820BmZEWm7PdgwQzOEk9hkRDLkkIL4449hyce0QPyWYo23v-MuEMvX06VwjV4G5T1xz8Pw7VWBH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ درباره نقض آتش‌بس از سوی ایران
🔹
رئیس‌جمهور آمریکا: جمهوری اسلامی ایران دست‌کم ۴ پهپاد به سمت کشتی‌های درحال عبور از تنگه هرمز شلیک کرد. یکی از پهپادها برخورد محکمی با عرشه بالایی یک کشتی باری بسیار گران‌قیمت داشت.
🔹
خسارت وارد شد اما کشتی توانست به مسیرش ادامه دهد. ما ۳ پهپاد دیگری را ساقط کردیم. واضح است که این نقض توافق آتش‌بس است.
@Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/444914" target="_blank">📅 19:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444913">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
مخابرات درحالی‌که همین چند ماه پیش افزایش قیمت داده بود، سرویس ftth را دوباره حدود ١٠٠درصد گران کرده. چرا نظارتی وجود نداره برای چنین افزایش قیمتی.
🔹
خواهشا یه پیگیری کنید خودروسازی سایپا چرا اینقدر ماشین‌های ثبت‌نامی رو دیر تحویل میده‌. الان ۵ ماهه از تحویل کوییک می‌گذره تازه خبری نیس که هیچ باید چند ماه دیگه صبر کنیم. از این‌ور ماشین مردم که پولشم کامل گرفتن تحویل نمیدن از اون‌ور مدام پیش‌فروش میزارن. نهادهای نظارتی بررسی کنن که مردم چیکار کنن.
🔸
ممنون می‌شم صدای ما رو هم به گوش مسئولین برسونین. شوهرم کارگر یکی از کارخونه‌های خصوصی هست، سه ماه از سال گذشته و وارد ماه چهارم شدیم ولی هنوز حقوق فروردین رو هم نگرفتیم.
🔹
آخه کشاورز چه گناهی کرده از برج یک گندم تحویل سیلو دادن ولی تا الان فقط ۴۰ درصد پول رو دادن. ممنون کشاورز از خوزستان.
🔸
ساکن شهر قدس هستم امروز دقیقا ۴ روز هست که آب نداریم، فقط یکی دو ساعت اونم با فشار خیلی خیلی کم. به اداره آب مراجعه کردیم هیچ شخصی پاسخگو نیست.
🔹
از اسفندماه کابل تلفن محله‌ ما دزدیده شده و طبیعتا چند ماهی هست قادر به استفاده از تلفن خانگی و اینترنت آن نیستیم ولی هر ماه قبض و هزینه آبونمان برای ما می‌آید. وقتی مخابرات خدماتی ارائه نمی‌دهد و مسبب ادامه قطع تلفن ماست چرا باید آبونمان پرداخت بشه؟
🔸
لطفا پیگیر بیمه صنف رستوران کترینگ باشید.
🔹
شرکت پرشیا خودرو از سال ۴۰۳ ماشین فروخته الان تحویل نمی‌ده لطفا یه پیگیری بکنید.
🔸
لطفا درباره حقوق معلمین هم پیگیری کنید. سال‌هاست فقط ادعا می‌کنن اما در عمل هیچ تغییر خاصی نمی‌بینیم. رفاهی ۲.۵ میلیونی چه دردی رو دوا می‌کنه؟
🔹
اینجانب در طرح فروش محصولات ایران‌خودرو بعد از ۵ سال بالاخره برنده شده‌ام اما اینقدر قیمت‌ها را بردند که توان پرداخت را ندارم. با وجود داشتن ۳ تا بچه امیدم به این بود که ماشین‌دار بشم.
🔸
الان یه ماهه می‌خوام برای مجوز احداث گلخانه از منابع طبیعی مجوز بگیرم ولی هربار می‌زنم درگاه مجوزها خطا میده. هربارم که باهاشون تماس می‌گیرم می‌گن مشکل به‌زودی حل می‌شه.
🔹
تمامی استان‌ها به‌جز هرمزگان مجوز تردد خودروهای پلاک منطقه آزاد خود را در استان گرفتند. چرا استان هرمزگان این کار را انجام نمی‌دهد. لطفاً پیگیری کنید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/444913" target="_blank">📅 19:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444912">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkVG36NQi7umb95uxdC1kqoqc3_H2yqnh-NvJ7qAiCh0CXR0RiebIkOxovhDTK2ScuKAzSqhkf5zkHxRYBD1cvxb_tEsLCeSBc0RIalXr5gPEgpgPpqASqvod_v19Qkipa86pun5tyIxQA1-Hp5pu74ZPT8KhR8JexdKD0hnkabar1LGdUGuow-gcWlnUnAcSxDTYsEbgG2ng51z0nMV6j_HqdLzXyR8hrQsRdubBZZyiSkR3-BoJfqL72XZQodNuH5h_WvfZNEYPOhqAOkUoZdt1lZd4EkQXsnlOjAknnu7wVtdhr53bXdf1vsUAOg4FmYHhc0OazM101kxqQRtfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخبر: قطب‌نمای برخی همسایگان هنوز دوست و دشمن را وارونه نشان می‌دهد
🔹
مشاور و دستیار مقام معظم رهبری: بیانیۀ شورای همکاری خلیج فارس، اشتباهی دوباره و همسویی با کسی است که امنیت منطقه را قربانی تجاوزگری‌های خود کرده.
🔹
توافق چه با آمریکا و چه اقمار جنوب خلیج فارس یک زنجیره است؛ یک حلقه‌اش که بشکند، کلِ زنجیره‌اش در آتش ذوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/444912" target="_blank">📅 19:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444911">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آتش‌بس در جنوب لبنان کماکان نقض می‌شود
🔹
ارتش رژیم صهیونیستی مدعی شد که ۵ نیروی حزب‌الله را در شهرک زوطر شرقی پس از نزدیک شدن آن‌ها به نظامیان اشغالگر هدف گرفته است.
🔹
ارتش اسرائیل همچنین عنوان کرد که نیروی هوایی این رژیم یک نیروی حزب‌الله در ارتفاعات علی…</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/444911" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444910">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtgOjBjnUmV6SmDWjI_fib13t9uWvuusZKQ0iO6fai5EcWkiM1tC8MV-dxWXkehtWC_ZtXSbeucGTMMcMCUKZpBzmzzZB2zegfYQ95UcJMX1wtexkiE8TBnGwzULGhe1XDVYiZYE9oSZtLbDZfUKHIrEoZhSCInIhPTmQIl4pWEoxmHTrR_RdiGLSoGTUpffG3dIbUWC5hWK__dVPUcot6Ng8Ifz1EqRPMyxVCEVaD2DhCPioM7EHIahNtQ2jU5HPg8zTPxFjlu-_27OleVmsdEmJPp-mggs9oRbEzwduCEoIL-g8k9964E00efZyEeUwhLysNfD7Xd0NnnOlZ3lxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزینه غیرمنتظره برای نیمکت استقلال
🔹
یکی از گزینه‌های ایرانی استقلال برای اضافه شدن به جمع دستیاران سهراب بختیاری‌زاده، وریا غفوری است ‌که طی فصل گذشته در کنار ریکاردو ساپینتو مشغول فعالیت بود و در بازی مقابل مس رفسنجان هم هدایت آبی‌ها را به عهده داشت.
⏺
باشگاه استقلال بعد از اخراج ساپینتو از غفوری خواسته بود تا در کنار سهراب به کارش روی نیمکت دهد اما این پیشنهاد را نپذیرفت و کمی بعید به نظر می‌رسد که این بار نظر خود را تغییر دهد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/444910" target="_blank">📅 19:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444909">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25959a2ba1.mp4?token=DywZ3yhi2abh5E2Cd4IUaUqd7sfn2w9cT_7Hq7pUSkQajQj3CNUwPyTWI-7yj5wpa4yYXt_FOSHRQXAqeB9qxBc2WCL8NPmnZ8P1KFVvww0p1h-yTOC7GyljLzKv4tRr4aeeNj975iynYJuRnDt5fdDbNCazEcbKa3On1Uwr1S2lPy5TpU35v1tbGV_KRVS1qkZKFrWYPbdIi_gMwslnyUx0VU37qojwQiRYhwq-EnO4Nv_To-TyRfWZN_FuR5Iv9OuuHDCMSx9iUg9B5dfbUt7PVfLvjH-6xy3cuV3JUOqReA9Qa8M_m6On_RgmfchEPRdqsYl3BcTSd0nYFGt-8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25959a2ba1.mp4?token=DywZ3yhi2abh5E2Cd4IUaUqd7sfn2w9cT_7Hq7pUSkQajQj3CNUwPyTWI-7yj5wpa4yYXt_FOSHRQXAqeB9qxBc2WCL8NPmnZ8P1KFVvww0p1h-yTOC7GyljLzKv4tRr4aeeNj975iynYJuRnDt5fdDbNCazEcbKa3On1Uwr1S2lPy5TpU35v1tbGV_KRVS1qkZKFrWYPbdIi_gMwslnyUx0VU37qojwQiRYhwq-EnO4Nv_To-TyRfWZN_FuR5Iv9OuuHDCMSx9iUg9B5dfbUt7PVfLvjH-6xy3cuV3JUOqReA9Qa8M_m6On_RgmfchEPRdqsYl3BcTSd0nYFGt-8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحبت‌های صریح حاج حسین یکتا
🔸
علی‌الاصول یعنی ما نباید اجازه بدهیم دیگر جام زهری به خمینی داده شود.
🔸
علی‌الاصول یعنی باید جواب توهین‌های رئیس‌جمهور آمریکا را مسئولان ما بدهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/444909" target="_blank">📅 19:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444902">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lfuBRnJS0eitU9nUqB565CYD-LfNkIAPyQKSAsdbe0oYVjAdzrAjcdiKGmtQb3V4QnoE5QbLdOqq0qzbEICSuHn86KjwYAaRlZa66uaOPlFTxW6cE3vAbMEf2YFQwp_HEw6D3F43a1ZUKElcIdOhJntHTFbUl2IJPUdqFYe6WitjvF-PfPb97FtQ6Zt4bCdXCMkC0M-eXf76TWElFiNK1bxTNs_qESOAlUQ30pw2wiytj2v710KSGAEgtOFZb8do-EiF4rmTU3glJP7zIOiJccjWC6qGbt3X2q_ZPMARhZ6_Nm7ot9fbwvSmPzbo8Db_K-903ugsY_9wvdl5szwI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cfEpgr_FU1o2x0tixBrL_eWK5J7ePbjRbdF3NfT4_JNbSz9IXKLteqaCbNSL7AzrosCbLLmx7sksXWgz5AGBS9mRBAPur1VvdLGmLNIbeaHZrlCHFnjvzGbbr_4qIm2NmQBJizzcnmLvy593A7ymdMB-7_yKQtq4bU7DyaePxFhOvg0zXgynwYED0GBnaLlmUP9bJ0Be4OE4vOq3SghMcuSj9wwNTCCNTwD9YZ7oNgIwQEdEPNv-v6N0OcpOAzp81h5G0qYyjudC2JrXjvDx1y571BItpVH-xmPVfFHww4XALhWpscgg0VJJw6GJ7Rl9aQ1MEyxphDm3bJ941-ckWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FraQcNySJ2KaRx-RjN4GdcNHAsM7PhNC5bgdvplDeMsqyvJ7SIsPTQmirP7N9z23LKRf0pJu88O8I1f_CK3gs9sPP_SG1Gkx7QUptJXIFm7U0hdKI-Fx4kzOvUO7W8pEfFJW2VAW3IVx8KDSiiXCI0C4GCWARDvS2eRw7O5nrSepnjhXhNpjrlDg2ffc7a3aSHd0YwapcRwfGp7ArNOY1xJAUObidwNNVVOih0krjLu5sN5APcpLjcVBl0F7C-Bc7i4NpwfTUGr8JLzuzkUiD7ASM7HiU6tiljp4pECFZiVtgPi16m7iNTwoH5QD1luKpiF2Rw7Ycf4LTLX-WnzBmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N44vMRXhngG2o5_pVsNP10fk3Nl64GwADJ5GuR4wQE3wa8TchKCnWdlrWoZas03LnA_PfllsSiLk7T4vUKlxtnnBHeNvEs4Kb_RJsP00vFmDP8_geDWDjUFZZkM5yyKwX8TykjwERvkdoLw_5rN0z0MzZWkgOsF4MkEzT3_a92muEEIYsxzV0L_8wWaPQZnFxGsmMO80Llsgz45J8WTLmAEdEHk83fkt62ICmdIQLmqGyK9FwxeQm8_QSvqnbGA9L_l3JGUvuPu2F7u5k0-xgZI8hcM6sdb3jRXVHcDSlCFDSodzQwX45qfvmvFHHztrR39krV2HZZTuDn-K6WUkFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_eWqyefFY9uCm7s6OQaHUbOppiyzsURv3sTL9CJGIww8k1DxPzOLpmHbcdOAAcw1ty6h7G15BogxLB91In_aYg7eZeQmEwdJglV21AruEhKP1MwJ6rUkVbp3591jlY7FWLc3XFNwajJUvTyfF_oJHdZmvvidphRKh0YAqRcLv5rXEip5ZwMrwj4jtNn0Sz_WEnlBy7wvSYdXfNoFUE8RcTJFIlQJVkwHqe4M495QHNr3fIgwqA8v5AiNGJJCxMZkN5kaLvTpB5Atep3pWig8w3uWF48uraxojpw8YKnoPDR0xmYcu6T879_PUUeNv84NXMhmr3MtmY93djNChTitQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ewo0XnXC_73M4vS9G3uO3pH5R7g4BVmgSW_xLHj7s9sf_DFofJqKRs9Mw9Ql2yNnUa8IK_en4tOgAeaaXuQSM8isQ9_Trv7Bdx4hm4HXvP6Vg4NgJAE-2UE9XkpFEHpGq_v5XujoBQt65XyokcgJqHO5dho2rSwXOX8JMKFKuGJMaMiut5rePP-KcwAfI6m2KafT7ME9D0aLVkI2VBFWXvZigHBYBvb310MgYSCvYSAmhC5gf1gn4siM83Sd_Y2vyZH1Jzs7rpRxdNNWOp4ZGYg5wykhbY4J910GYKnw4QhA4uJSofYe35yxLsv97SKeIJCcAsb4wGjh9VU6tiappA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SU4POt5H0a8pMXbsUpLuVVKDMinGb9aH0rL0fAFJREjHNySW13mY2POIltFBJKsjklBYaokb4nJTTMoRJq8CxljHINyi44fUTbaNj4dvb_TWwFXAnkpgon2uJJcAKGCIqG0kQtDK0qwGIvFio5Zl2deiuHn4DXVG7_CIdX0uZqd_RlpDLlrYAWaY4wMcZ5DNfgvW-FLxZHF6wgHERuY73OV36JHLrxU42ZoHisPb9DP_GjcvMIoqnCdEhx4wvVjmeDzMpfwrXKg35Juta_6luzaT3ltPN2QU-RXAorB8yzyBUcFDFKJ3YhMcGgQpJPVqnX6c-etgBhd48_wO3OWraQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نخل برداری حسینیۀ شاه ابوالقاسم یزد
عکس:
محمد صادق حبوباتی
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/444902" target="_blank">📅 19:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444901">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجارهای کنترل‌شده در جهرم
🔹
سپاه استان فارس: انهدام مهمات عمل‌نکرده جنگ رمضان از صبح شنبه در حوالی شهر جهرم آغاز و تا پایان هفته در ساعت‌های ۷ تا ۱۲ ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/444901" target="_blank">📅 18:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444900">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">عمان خطاب به اروپا: عبور از تنگۀ هرمز مستلزم پرداخت هزینۀ خدمات است
🔹
شبکه بلومبرگ مدعی شده که عمان به متحدان اروپایی گفته کشتی‌هایی که از تنگه هرمز عبور می‌کنند بایستی برای ارائه خدماتی مانند کمک دریانوردی و کنترل آلودگی هزینه پرداخت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/444900" target="_blank">📅 18:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444898">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444898" target="_blank">📅 18:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444897">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6f03fe18.mp4?token=t0USu9qv4zSXh9C1-I8TJ0kmfSRJqSpodFbRql5MwwwdMS4_rWAMPcvwpybXgtCvav9PISbpkUDf4TW-Kq__pPXdBWlwVGQlWPzlKTRbZ1mZuAVREm4miRxsJXpERYiE8ugyyt6fdu_9lK9-otRpPv5WMz_N-DOSNVZFoiWoY5RVYt975Y_BxzMLsDGXB2_NKWjtzntnhP81voiYFjFKcTgPGcktZsHgCcOH4jFnPysG_MU3P6E1pJlaH6EfEm2zn9M6CdtLETTYeLq7fty4PMzI3VQRSs7iLJlzqvT3QtQ4p5ptodV6GgDZnA8QYR0LywIzYpRQYrr_kvZM-gerkG3EU5cwPGz3OijS1Vw8ZgTCzrTNhnL0PNbxHkigmr8d3uwld9y3O4WVBEml6UgiH4AKcQwE1WBBz7GHfQ8B4hQIf0b8Xwi8cC00AJYHF2Oc9XstbuT6lu9zi63MuiAATKUvcB2HxGMzzwjG9P0RmL-0z_nJROdvRkaYAV5_-PK7Ss_AdyjDAd_R4cG7fETqll13VdaZrogNgxp5ZA_aZPdeQmHGn_f6mwWEL0dFL6kqVhFZHcEaQcxL3kH-WuS-s7ILwImxEOgc5Yr_pZsOG-rghJbVeDVhnTeJMd95Tgt4RwKq_YRF-3Gwgt37shtnywNQqCnkqCqQQi00LB-PLMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6f03fe18.mp4?token=t0USu9qv4zSXh9C1-I8TJ0kmfSRJqSpodFbRql5MwwwdMS4_rWAMPcvwpybXgtCvav9PISbpkUDf4TW-Kq__pPXdBWlwVGQlWPzlKTRbZ1mZuAVREm4miRxsJXpERYiE8ugyyt6fdu_9lK9-otRpPv5WMz_N-DOSNVZFoiWoY5RVYt975Y_BxzMLsDGXB2_NKWjtzntnhP81voiYFjFKcTgPGcktZsHgCcOH4jFnPysG_MU3P6E1pJlaH6EfEm2zn9M6CdtLETTYeLq7fty4PMzI3VQRSs7iLJlzqvT3QtQ4p5ptodV6GgDZnA8QYR0LywIzYpRQYrr_kvZM-gerkG3EU5cwPGz3OijS1Vw8ZgTCzrTNhnL0PNbxHkigmr8d3uwld9y3O4WVBEml6UgiH4AKcQwE1WBBz7GHfQ8B4hQIf0b8Xwi8cC00AJYHF2Oc9XstbuT6lu9zi63MuiAATKUvcB2HxGMzzwjG9P0RmL-0z_nJROdvRkaYAV5_-PK7Ss_AdyjDAd_R4cG7fETqll13VdaZrogNgxp5ZA_aZPdeQmHGn_f6mwWEL0dFL6kqVhFZHcEaQcxL3kH-WuS-s7ILwImxEOgc5Yr_pZsOG-rghJbVeDVhnTeJMd95Tgt4RwKq_YRF-3Gwgt37shtnywNQqCnkqCqQQi00LB-PLMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان دلدادگان زینب(س) در زنجان به حرکت درآمد  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/444897" target="_blank">📅 18:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444895">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5615887ffc.mp4?token=HK4GY5ZtAsoCcEiTfs6Adipma7L9CdDnB94KauSSeTIYegkTDzaeTtJ8WEOOXwC20E77dzEgHxEanFdCIbSyzE5_oGlJX2oghRQE8Tht93rp5AZ6mFGDC5Rb-bJilRAxiDKJs769KLr_2mzwEGMhjp7a0-PA3RkFqNS-9zmFXDxXptY7lr_FPmDOoRm492fhuzcKy-1o-fYmTSWX9l78QaLVoKixU244gS_NW7AlgLhSgV--2gbXs0BSndPXTm0Bi5sIzHX9lb92tAQ6h71wRu0YDb3lMPwG72vRTQ9uCT58n0GmCeAhCz-mxHRMhBwfoEQKF51LxMwPe8A-d6EGTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5615887ffc.mp4?token=HK4GY5ZtAsoCcEiTfs6Adipma7L9CdDnB94KauSSeTIYegkTDzaeTtJ8WEOOXwC20E77dzEgHxEanFdCIbSyzE5_oGlJX2oghRQE8Tht93rp5AZ6mFGDC5Rb-bJilRAxiDKJs769KLr_2mzwEGMhjp7a0-PA3RkFqNS-9zmFXDxXptY7lr_FPmDOoRm492fhuzcKy-1o-fYmTSWX9l78QaLVoKixU244gS_NW7AlgLhSgV--2gbXs0BSndPXTm0Bi5sIzHX9lb92tAQ6h71wRu0YDb3lMPwG72vRTQ9uCT58n0GmCeAhCz-mxHRMhBwfoEQKF51LxMwPe8A-d6EGTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع جنازه‌ای که توطئه علیه حماس را خنثی کرد
🔹
تشییع پیکر برادرزادۀ شهید اسماعیل هنیه با حضور گسترده مردم غزه در حالی برگزار شد که جریانی مشکوک از هفته‌ها پیش فراخوان تجمع علیه حماس را صادر کرده بود.
🔹
هزاران تن از اهالی غزه امروز در شهر غزه، پیکر «ولید مجدی هنیه» را تشییع کردند؛ وی بر اثر جراحاتی که در حمله اسرائیل به اطراف مجتمع مسکونی ایتالیایی در محله النصر در غرب شهر غزه برداشته بود، به شهادت رسید.
🔹
اما نکته قابل توجه همزمانی تشییع پیکر این شهید با روز موعود مخالفان حماس در غزه بود، جریان مشکوکی به نام جنبش ۲۶ ژوئن از هفته‌ها پیش از اهالی غزه خواسته بود تا امروز به خیابان‌ها آمده و علیه حماس شعار داده و تجمع کنند.
🔹
با این حال امروز هیچ خبری از حرکت علیه حماس در غزه نبود و برعکس فضای این منطقه با تشییع پیکر این شهید کاملا همسو با حماس پیش رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444895" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444894">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3aa5894fc.mp4?token=sAeNbKmOj40V4h29cz8_rc1jMpIejSs1KKSIF_zHN6DphFQa6uDJiVZgHBMpWs5B8XyY-k3l5LBXchlv58nclLWm2Jsedc_NLF91T-1mVGCaWLjBxAqBriNeQxT3lKhZavbvWFDCNeKMG8ydeQWtHCgPY-0zzLvNiZI1-lPdNRufGfp3j8fmLeo50cBG0v3HHE-SJNH_D9QvPvNKgLfwnm7m-ojMOSO364fr8mE8dDzm0WYSHgUpl4xb25KHPa9PqoASshWGXu8ByCuGXar-KBgymuOla9RnmeXTIKzLROgg7-p4LB5-5Y90rlEpuyBqlz1VOKkoFpzMwdlCib-6Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3aa5894fc.mp4?token=sAeNbKmOj40V4h29cz8_rc1jMpIejSs1KKSIF_zHN6DphFQa6uDJiVZgHBMpWs5B8XyY-k3l5LBXchlv58nclLWm2Jsedc_NLF91T-1mVGCaWLjBxAqBriNeQxT3lKhZavbvWFDCNeKMG8ydeQWtHCgPY-0zzLvNiZI1-lPdNRufGfp3j8fmLeo50cBG0v3HHE-SJNH_D9QvPvNKgLfwnm7m-ojMOSO364fr8mE8dDzm0WYSHgUpl4xb25KHPa9PqoASshWGXu8ByCuGXar-KBgymuOla9RnmeXTIKzLROgg7-p4LB5-5Y90rlEpuyBqlz1VOKkoFpzMwdlCib-6Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخل‌گردانی ۱۱ محرم در شاهرود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/444894" target="_blank">📅 18:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444893">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترافیک پرحجم در آزادراه‌های استان قزوین
🔹
پلیس‌راه قزوین: با پایان تعطیلات ۳ روزه، ترافیک در محورهای آزادراهی قزوین-رشت، قزوین-کرج و قزوین-زنجان پرحجم و در برخی مقاطع نیمه سنگین بوده و پیش‌بینی می‌شود ترافیک در عصر تشدید شود و تا پاسی از شب ادامه ادامه داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/444893" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444892">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
۲۲ ملوان ایرانی پس از رهایی از دست ارتش آمریکا وارد پاکستان شدند
🔹
وزیر خارجه پاکستان خبر که ۲۲ تن از خدمه کشتی‌های ایرانی ربوده شده توسط آمریکا وارد کراچی شده‌اند تا پس از آن به میهن خود بازگردند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444892" target="_blank">📅 18:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444891">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meD7wvACSxVaOrfBYAMvrMFcmBgT9jIp52coBbcVJReDF10KxGxUoOvDHRpesjfFNJBXOtqG3pnGtoW-XzvdoYcX-cDUfKqdGYTDE3kYbVv9UgZiqrXnrEADAfIdpOzDelO0wTg07jZiLclc-EAJKpBlIKlI6p_oRXIy9PCKeN_PGpVuKnh-Dz_fwx_GcQIKA7cdB-jilANrdIaGJiVzgXuhN6OSsYVuUx6xmyD-L3y0gCIo-1xiTp4YX6Z_WZUhLDpwjZH9owAxoeik0yu77dqV55Dd2bYdyuUNmH96N9DoMtrU_fb6kA999MT8Zc1ZbO1NznnL6fi-G_PFfI1hEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ایران ـ مصر فعالیت ادارات در برخی استان‌ها را به تأخیر انداخت
🔹
با اعلام استانداری‌ها تاکنون، ادارات استان‌های
کردستان
،
قزوین
،
فارس
،
سمنان
،
گلستان
،
یزد
،
مرکزی
،
خوزستان
،
کرمان
،
مازنداران
،
زنجان
و
آذربایجان‌شرقی
فردا با حداقل ۲ ساعت تاخیر شروع به‌کار خواهند کرد.
🔸
تیم ملی کشورمان ۶:۳۰ صبح شنبه در مرحلۀ گروهی جام‌جهانی فوتبال به مصاف مصر خواهد رفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/444891" target="_blank">📅 17:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444890">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01c0ca6b8c.mp4?token=CkX9mompbGBpf5LNem3G0sTQGqTplRpaTBnI8RO3CppxmI0eDNfIdqmDiHT8qLEBu2nTyVM_0ewFjBcCIlL_T6dMY___AkYPP3NCj-L7q57BQAL41HLqLh6o2RH23D8aX9Ga43KGxA0PFpVegxp7TgPgIvbUHwhEC9zMZdAYXgs9mYzj16Z3CRefqpviHtr01rUGrq5vCDUqfESlp8F4BI768MIOTsRtaP0AWi0gqXa0h-k40QvO7GVci7XifwEA_Dpe1zn_6h7Sed33B3Mj_A40VKVrtKE6QiZHEXM8FsDem9frZ9mEbT4VcgeInwxboICD0Fs6JsDeF7SSchexb3WS-E0CoSQ9HdgCr-vKLcoETixXH7xMoRvGi-80sqU3G2ijfT3Q4OH8yJQLZioMJ3eJIVCUB4lzVB9LILtxB2C-UqvPgfpfZfJSK41pdkWS1O4JxHMp4kEh6kg4LW6thIXGNZMr2_Yix7OMas7udgPWAFZIweV47OfXchNgVbaYWZSzkEuvIS9WUjAI19vzarMtl4J8cpQfTUDvY-WFq3mO5-hrTWB0zDQrsnrU1gLPLjK2WV82cEgHstX3LG0EFMiBz7Zm7F-WgfOBtjZvVVbLbe12WYJ9EbsRXtHeegIlDidRdL9qqGCQm32qdQt6ZLTJeR0wjGMB6Eo92v0YwLM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01c0ca6b8c.mp4?token=CkX9mompbGBpf5LNem3G0sTQGqTplRpaTBnI8RO3CppxmI0eDNfIdqmDiHT8qLEBu2nTyVM_0ewFjBcCIlL_T6dMY___AkYPP3NCj-L7q57BQAL41HLqLh6o2RH23D8aX9Ga43KGxA0PFpVegxp7TgPgIvbUHwhEC9zMZdAYXgs9mYzj16Z3CRefqpviHtr01rUGrq5vCDUqfESlp8F4BI768MIOTsRtaP0AWi0gqXa0h-k40QvO7GVci7XifwEA_Dpe1zn_6h7Sed33B3Mj_A40VKVrtKE6QiZHEXM8FsDem9frZ9mEbT4VcgeInwxboICD0Fs6JsDeF7SSchexb3WS-E0CoSQ9HdgCr-vKLcoETixXH7xMoRvGi-80sqU3G2ijfT3Q4OH8yJQLZioMJ3eJIVCUB4lzVB9LILtxB2C-UqvPgfpfZfJSK41pdkWS1O4JxHMp4kEh6kg4LW6thIXGNZMr2_Yix7OMas7udgPWAFZIweV47OfXchNgVbaYWZSzkEuvIS9WUjAI19vzarMtl4J8cpQfTUDvY-WFq3mO5-hrTWB0zDQrsnrU1gLPLjK2WV82cEgHstX3LG0EFMiBz7Zm7F-WgfOBtjZvVVbLbe12WYJ9EbsRXtHeegIlDidRdL9qqGCQm32qdQt6ZLTJeR0wjGMB6Eo92v0YwLM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان دلدادگان زینب(س) در زنجان به حرکت درآمد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444890" target="_blank">📅 17:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444889">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcdOz31jWIOGBSRN_Luwdez1IPFQr6OGgLvTDLSyvHZdxHRFmB6FnqsL8ElNqrKjEHCiTSXn2h_QkdTSg2QCos6r0j0gmHte-wcgn9wgoNcsS29Rig4L85TODACmKAdcVJUJankC7Egrjzlr1ZoRJ3j4B9w6hbg3eDXAo7PePud3S75upMPWPKj820DABofUKgtKafi9gzrLaO0iwUUp5TBqfYtH26_5q0OXc-AgDfxg6v1xGI9Qtg_Rqnpp8E8bBo0jdzQD5YQW24vaw35vcmXzwl92P0MFPdRVDO4VIWk5-tgKNKje7FMqOOcmGKyossF1cMlwuNilwaD5tAuVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸ مدال جهانی و جام بهترین تیم برای موی تای ایران
🔹
تیم ملی موی‌تای ایران در پایان رقابت‌های قهرمانی جهان ۲۰۲۶ مالزی، با کسب ۲ مدال نقره و ۶ مدال برنز به کار خود پایان داد.
🔹
همچنین تیم ملی بانوان ایران به دلیل عملکرد موفق خود، عنوان بهترین تیم مسابقات را به دست آورد و کاپ این بخش را از آن خود کرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/444889" target="_blank">📅 17:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444888">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkD-1RwD-bI3Jl8A1pjzReVJh5J3nK9mAZ3-u7KEMPsna0kG50Yy9AcsN6eq_hlCNwgbnS3XRDkprcqzpc6947J8V4DNtMJ2xzQAg4QMnMEN-7u6rbsFhB35D-idB1mnqyND-BtFlZPkOm_IUQKDAWvYkoQLznsTwTjQjnX5JyskXIM3yNNK4HbIWPx0ZdosnPEKLqj5hoP9juU8lV_ThJO9fe0fMGzpSnD6cMzUDc1Vo7PQRRg6ndglZoyRyN840IdLcDiN2g0jUeOs82WlQppH5OE11878uvauAwZkzp9TTLmilvTP4ey4ApDLfKW9_XpoipERDUTgB9gafL_Ezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار وزش باد شدید در تهران از عصر شنبه
🔹
هواشناسی استان تهران: از عصر فردا تا یکشنبه، وزش باد شدید در استان تهران به ویژه در نیمۀ جنوبی و غربی پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/444888" target="_blank">📅 17:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444887">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1VP2BYV1W88mM-4sGyK2_y0ZGhpmLegB6qzin5Ww1JAE3OrFVIPJ7HYCljdKCQ1TISfzs1M3CXrRVP2Z0-kLac_ZhvKfCAgmPqprvwcJkaLvgB0nZBqm0vVNDuvvX-QIIrFTbvAOUfgmqYDwUA7B_2FDPDuF_RxZ2q_T4VABuINfbPVfZU9MmFXpNaG9sh2KaCElYIugwZ632ywkaHN8hlDY1UjFydUzLQ0ZaQgIgA1mIVm2HBRyHAvRoqrkL9ipmAnOPj9ekeOpOqcJc-XvrmkJ6N0CVeSpVXz4nNj0-Sx4jdFW7RuvWG6-Ep02taCAXQE-InlMKKX78QiDNEfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آینده هوش مصنوعی بیش از کد، به مس نیاز دارد
🔹
وقتی قیمت فولاد افزایش پیدا می‌کند، اثر آن به سرعت در صنایع ساختمان، زیرساخت و مسکن دیده می‌شود. فلزاتی مانند مس، نقره، لیتیوم، نیکل، کبالت و عناصر خاکی کمیاب، نقشی مشابه فولاد را در فناوری‌های پیشرفته مانند هوش مصنوعی یا خودروهای الکتریکی دارند.
🔹
نوسان قیمت یا اختلال در عرضه این فلزات، به‌ویژه مس، می‌تواند بازار فناوری را تحت تأثیر قرار دهد. تحولات ماه‌ها و هفته‌های اخیر بازار مس نشان می‌دهد نگرانی از رکود اقتصادی و نرخ بهره بالا قیمت‌ها را تحت فشار قرار می‌دهد. از سوی دیگر، موجودی انبارهای بازار مس کاهش یافته و بسیاری از پیش‌بینی‌ها از کمبود عرضه مس خبر می‌دهند.
🔹
بر این اساس، ممکن است توسعه روزافزون بخش زیرساخت در شبکه‌های برق یا فناوری‌های مراکز داده و هوش مصنوعی در بلندمدت، کمبود عرضه را جدی می‌کند و در نهایت به کند شدن یا گران شدن توسعه فناوری‌هایی مانند مراکز داده، خودروهای برقی و زیرساخت‌های انرژی نو بیانجامد.
جزئیات بیشتر را از
اینجا
بخوانید.
@FarsnaTech</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/444887" target="_blank">📅 17:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444886">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWqWfEj68MA54DYXmw04DIYdreSedqMk1FhdQNLz_tYemGnUUB_NPJsy1JNISodKsUrmXUF_L0doJjg2PwQnVHKFbLT5vYgs22p5GJiyvdO0bRZNTDZ45KqBnCNa6ccsb5AqXr4REP8Q9fpr0xGhif6nEu2c-XhIaP_xdai4NXSgIhw_Yc2YTDFb6m2pVBcDub-GO9wSZH_OI7_m1Sz3wdl2GWmGVQDEV_-L7L56yFDgEpPc51HlL0JjgmUVkRmmduvTQ37Lhs7kGTjVnDJckqqb26yo7FKW0NIBWIUWKOrlJz9xuvenBrzwmwSpHGFaVSC_O0vLn-IoIsz-6NV0hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار حمله موشکی در دبی صادر شد
🔹
وزارت کشور امارات با صدور هشدار حمله موشکی از طریق تلفن همراه، از شهروندان این کشور خواست تا در مکان‌های امن قرار گرفته و از پنجره‌ها فاصله بگیرند  @FarsNewsInt</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/444886" target="_blank">📅 17:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444885">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN9EUEyQKs2CSFc9Kz9r-8LVfBeppF4wR4QQbCSgGuRKmoT17nnssMg8Tok8I_KZEvRnAbNOZ9-Y24gF8T7YSNe8SJ2u5LMPghOWMr6HgZiYPMJDwMZdF5XcH9san_yqLbjOD0wPJrNyrb6OsljjFyBpChoyb86M_Z5YNK9mIC9brk7BuI-BnQ1-C0V8xlVqAkN_3WRqMyOb4aYFlhO7JuXXYJ1sXI5CTEfsPMBl57j3j4u5uhEbe2VUN9jVcnIqIZ07xl88P6EkpQk7XwPQVPzeNeHc_Q4a19ASIHjDr80KjoQLPfhSjpvmmLvIWBdmLBhClmQa99pqiZEb4PNn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار حمله موشکی در دبی صادر شد
🔹
وزارت کشور امارات با صدور هشدار حمله موشکی از طریق تلفن همراه، از شهروندان این کشور خواست تا در مکان‌های امن قرار گرفته و از پنجره‌ها فاصله بگیرند
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/444885" target="_blank">📅 16:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444884">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4siNqJddk4i_EL_eSzPPDYhGu1vQAdm8Ta0C_DbRs7UHdzmXfS4mYQ17_HAgznge1fITmLN6VlwpO8Lra3NDav1jf3l2771SnOoTEoa1kY9pFS3A1O79CHnWfBpLyo6Ki-7t8odyhl5wKTZ1PyiVtB5d6sAW0Tr_w4t7SsOQ2pclHqUthOff-JRvL6qFRQcJlODj0WOZn1CiQoqDjy_PnWgn0z0Me7mMJr417J5dwqMjGPkNngWWoQ6t_viMq5MobAEb9_hXT-eGyW2DyUCM24LhIuGL2vZPA820vx79_LfKjCJDNKbTQJbDsU1s2KyvOah7aFLX0lUSm9lLE7_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهای عربی و آمریکا بیانیه مشترکی دربارۀ توافق با ایران صادر کردند
🔹
در این بیانیه آمده: ما از امضای یادداشت تفاهم بین واشنگتن و تهران استقبال می‌کنیم و اهمیت تلاش‌های میانجیگرانه انجام شده توسط پاکستان و قطر را مورد تاکید قرار می‌دهیم.
🔹
ما بر اهمیت حفظ…</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/444884" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444883">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc864a17d1.mp4?token=QUDm9eYUE4xgL4DLpt6c6WOWKuSXAjwkQyC8ygw3GIHCKvipAs-ooJ5tFnolPwIeavda0KAU2H81PgCbZNZaEVj7FrVcSYwd7AGo51jgSCqQ9Q9j09J_gsAW3a3s1KCiWzuwQZX-q_rCb2Qk9MdXrED_9qYEtKUs6_ZGFkZidFycfzjdn8hI9aAHJuW1alJEVpaghr76rsgoHfCF39uPdu-037jGZWZp4eXHn4VfpYuArQotyGjKtRzK_M-4Z11TnC8ONCxIK1JlwE2oCIlhHmhGB-Q45r8ZoQpaqLOEINNgB5V0uBoHiEq4L4lvaGohNL3Yhn9gJN2NB6jwhIf79A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc864a17d1.mp4?token=QUDm9eYUE4xgL4DLpt6c6WOWKuSXAjwkQyC8ygw3GIHCKvipAs-ooJ5tFnolPwIeavda0KAU2H81PgCbZNZaEVj7FrVcSYwd7AGo51jgSCqQ9Q9j09J_gsAW3a3s1KCiWzuwQZX-q_rCb2Qk9MdXrED_9qYEtKUs6_ZGFkZidFycfzjdn8hI9aAHJuW1alJEVpaghr76rsgoHfCF39uPdu-037jGZWZp4eXHn4VfpYuArQotyGjKtRzK_M-4Z11TnC8ONCxIK1JlwE2oCIlhHmhGB-Q45r8ZoQpaqLOEINNgB5V0uBoHiEq4L4lvaGohNL3Yhn9gJN2NB6jwhIf79A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شما
پشتوانه‌ی عظیمی به نام "خدا" دارید
@Fars_plus</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/444883" target="_blank">📅 16:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444882">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViPL_BRrGZKm0xdZIQIFF8EVnUyTERn7HqnTQbkcs-0UPjpZ4TbQ-1ox8SRmPhiZEbp1w320q3J1QJ8HskdO_2KmKyKOl4MElPBArW1qIIZvTLkhaX7RTV3M1Aw9UuBbhHPK8RzTVSs6UTMuX98pvmDCDILbvytPahEd7Rj-ufO0poOSJ6BrguvrMEoXZ7zLXE00MmhRYjqLpXW3vQCjlMSG7Wb3VKfH2fpupIc9oJuIF-AbVuDpCw0rd6q9CIibTX0dhqNvLCqV3e6WkbgM6086LfLTEHQBzK1ilUVUR0iE0dD3y7UN4rEtxicMlml1Hn5X5EHC14Zc7u60ROsidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیام عبری سردار قاآنی به صهیونیست‌ها: اگر با پای خودتان از لبنان عقب‌نشینی نکنید حماسهٔ سال ۲۰۰۰ تکرار خواهد شد
🔹
سربازان جنایتکار و تروریست صهیونیست، در کمتر از ۴ روز ۱۰۰ کشته و زخمی دادید! اگر با پای خودتان از جنوب لبنان عقب‌نشینی نکنید، حماسه سال ۲۰۰۰…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444882" target="_blank">📅 16:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444881">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
رئیس‌جمهور موقت ونزوئلا از افزایش شمار کشته‌های زلزله و سونامی در این کشور به ۱۶۴ نفر خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/444881" target="_blank">📅 16:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444880">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsXy3t8cw8lyW3uBTpwuvi9dQgYDwqqBEpLsiX573BuT4_-Pz-j1j-dy9GP91e3-1Z5EKC4CkkniVORaaqs3pUJqjrrD9LbukKNc03HYXYXlzZLczV9Fuh63iqdD_XCey7KEDS-_9qxPD6t4J3C_dnY6C1A7WkvRw0Z463CQWoHoZm0FZVHism9ZY2f5q_BlM1QEjEGWazlA7A2gtk-sYVGdAytWkvykC-ZUdViA1xg0Re66hxPPIYo6YCVSnFvC4a1aG22dkSMw7j7mGm4T0WWKPn13NOl7zGC0s0NTdeZaYAPfC7ikc2ugcVaqCYU27iFoMaGVbvCOFt7g51QElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهای عربی و آمریکا بیانیه مشترکی دربارۀ توافق با ایران صادر کردند
🔹
در این بیانیه آمده: ما از امضای یادداشت تفاهم بین واشنگتن و تهران استقبال می‌کنیم و اهمیت تلاش‌های میانجیگرانه انجام شده توسط پاکستان و قطر را مورد تاکید قرار می‌دهیم.
🔹
ما بر اهمیت حفظ…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444880" target="_blank">📅 16:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444879">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🎥
تاج: با وجود برخی ناسازگاری‌ها ایرانی‌های آمریکا متحد بودند
🔹
با توجه به ایام سوگواری حضرت عبدالله الحسین، بازیکنان با نمادهای مذهبی مناسب در این مراسم شرکت می‌کنند.
🔹
اتحاد بسیار خوبی میان ایرانی‌های حاضر در اینجا برای حمایت از تیم ملی شکل گرفته است. همان‌طور که در دو بازی قبلی هم دیدید، با وجود تعداد بسیار محدودی از افراد ناسازگار، انبوهی از مردم برای حمایت از تیم ملی به ورزشگاه آمده بودند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/444879" target="_blank">📅 15:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444878">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca429e17b6.mp4?token=CDqHeT1EurMtGNBuKlAUGj-94NpgPwB0lYDxYvCK9LbA7aBnTzrKjOxa2fOTABWlNBg0x8WrmoOGMJGtVnILgPWa-Ej9YzFG4MXnePojFT12ZoOfbzYVay9uG4uoyLkyFCkpnKyZBmqcfylxWVl1Sr6jX6TjQEpCjuLHbzBncAvJl8DE14vv_80I7JjorH5VE43AiToIywJzvqRqbVH_45G2BbLGwQmKxBB50yVz0MzeMFWHfiIqpF5pX2PIUULthSw1G944Fqy6nNHfgkOaFN98UGtOkaaZlKWP0BZfdyM6KqKPC4lL59f4AvpYxdQiO4Z-u2PhyJ5pZYVahO1wLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca429e17b6.mp4?token=CDqHeT1EurMtGNBuKlAUGj-94NpgPwB0lYDxYvCK9LbA7aBnTzrKjOxa2fOTABWlNBg0x8WrmoOGMJGtVnILgPWa-Ej9YzFG4MXnePojFT12ZoOfbzYVay9uG4uoyLkyFCkpnKyZBmqcfylxWVl1Sr6jX6TjQEpCjuLHbzBncAvJl8DE14vv_80I7JjorH5VE43AiToIywJzvqRqbVH_45G2BbLGwQmKxBB50yVz0MzeMFWHfiIqpF5pX2PIUULthSw1G944Fqy6nNHfgkOaFN98UGtOkaaZlKWP0BZfdyM6KqKPC4lL59f4AvpYxdQiO4Z-u2PhyJ5pZYVahO1wLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماز جماعت شهید طهرانی‌مقدم در محل تست موتور «قائم»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/444878" target="_blank">📅 15:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444877">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEaY0qSX610f1k-XDZJaFb3CtnyawpPx222Ztz7ujvDJcWfLSqFNwi57EBJwmizpALEbKzqsighN2xQLXF3ryqcCNHpsPPydgGCvT5xQQABrBOCPFvYwj1mK217LfLg5-Zc164H_JtSuVYA22Yhyqi6iYt8YzEz2YjO8Fy_ez6Zxk6r5S0hsmr1CJKRaSSXYk66Tm8-2Zg2TC2Rkm6AUdy-q4U0uteEwQR8xGv3uyWMUNoWrUsKoAgi4lz7YhM9poadGmRV8KyMihCQ4Jv3gQkqlZix5K0cxgbJHOg-CQ9ebAcbiQQkEo2wlMoYDDabY9W9MI4d7uq9Pi3h8yvrRdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ارتش اسرائیل برای شهر منصوری لبنان هشدار تخلیه صادر کرد
🔹
در ادامه نقض‌های مکرر آتش‌بس از سوی اسرائیل، ارتش این رژیم با پخش اعلامیه بر فراز شهر منصوری، از ساکنان آن خواست این منطقه را ترک کنند. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/444877" target="_blank">📅 15:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444876">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/557d43e873.mp4?token=JFgqq-yD6PqaP247bmWeK35DufliCcCWbo6l0KgMkHurY0VVqp9HumyHi9DKU9_n0o67GLUEIZeOqm2LiNRzaQ08cCEUFMGjH7xccPNHkMg6DCiOAaU_aUS88AxyvA8ad6f0GNHBjqp8QOcRJT7opX_s_tc0yD5mPsVpl3d0wC-ZIFOW4vOV1gWt3nTCnmVkHOVfskA-ambLDL9IzkRUOKmcHGjI59QqyfNBUUbqoaBUJoxdITVhnKNKkkgk2lm_dQjxpNFlPz2WB2t_z_5b1K4fBkgS5glnqgs0Ih6dyjaP8g43PrnI8bfi6yePlvrREH04eBkqzv_leMMRA6cm1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/557d43e873.mp4?token=JFgqq-yD6PqaP247bmWeK35DufliCcCWbo6l0KgMkHurY0VVqp9HumyHi9DKU9_n0o67GLUEIZeOqm2LiNRzaQ08cCEUFMGjH7xccPNHkMg6DCiOAaU_aUS88AxyvA8ad6f0GNHBjqp8QOcRJT7opX_s_tc0yD5mPsVpl3d0wC-ZIFOW4vOV1gWt3nTCnmVkHOVfskA-ambLDL9IzkRUOKmcHGjI59QqyfNBUUbqoaBUJoxdITVhnKNKkkgk2lm_dQjxpNFlPz2WB2t_z_5b1K4fBkgS5glnqgs0Ih6dyjaP8g43PrnI8bfi6yePlvrREH04eBkqzv_leMMRA6cm1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای نجات ۳ نوزاد در بیمارستان خاتم‌الانبیا(ص) از زبان پرستار شجاع این بیمارستان  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/444876" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444875">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqhthnD8jlVfRdW4oHCyWIdik_4m-TlyqVPxW3TgSGKmii9dkvCLRbO9qNOJuE35NmSXiJG3fPID-jMgNfoiLhiR2vu0ygHEQbKz8fQLDNwiSG4DXXtZzbfV9fJGdxWg1MWeBchwJVq8qnDHwTaTCOtbKROD32Euc5nrqfZ2j46axz2C1-lY9iveqfV3LegLF-NiQDmPT2RPnf_ix4C6_FBeJQfPGiCQfmwp-HWWRMGdD450u6EmYyVyqtBAzQJYZwynSHDIt0XGS4hXkL5eTGEubDkvyv0vRMm5swz9I8GEMNWcTm6ErAy9WNud0FZAC4i6gGR5J0aGAu2NncI_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امام جمعه بندرعباس: دریافت هزینه از تنگه هرمز، حق مردم ایران است
🔹
حجت‌الاسلام عبادی‌زاده: اعضای شورای‌عالی امنیت ملی و رئیس‌جمهور متعهد شده‌اند از ۶ مطالبه اساسی جمهوری اسلامی در مذاکرات پاسداری کنند.
🔹
تنگه هرمز در محدوده آب‌های سرزمینی ایران قرار دارد اما ایران در گذشته از دریافت این مبلغ صرف‌نظر کرده بود؛ اکنون که دشمن امنیت این منطقه را به خطر انداخته باید مدیریت ایران همراه با دریافت هزینه به رسمیت شناخته شود.
🔹
در موضوع مشکلات صنعت خودرو، : بازار خودرو رقابتی نیست و همین موضوع مانع ارتقای کیفیت شده؛ باید زمینه ورود بخش خصوصی به صنعت خودروسازی فراهم شود تا رقابت افزایش یافته و کیفیت خودروها ارتقا یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/444875" target="_blank">📅 15:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444874">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
ارتش اسرائیل برای شهر منصوری لبنان هشدار تخلیه صادر کرد
🔹
در ادامه نقض‌های مکرر آتش‌بس از سوی اسرائیل، ارتش این رژیم با پخش اعلامیه بر فراز شهر منصوری، از ساکنان آن خواست این منطقه را ترک کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/444874" target="_blank">📅 15:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444873">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583654c04e.mp4?token=dFDhJiruuK4FGAn0CsZeke4xjynloSaqzYtsBhLTzTmGtUuDCDBX0fzRVoq7AWg2wly0JRrTOLliT_APnUrda4ZSLLN4jaelPBAG6QG0rBr4wNSY3OGnkCDM9a4ec1Iez83Q2iJ45gvA5cZpoQAlw2h_e0ZO7ul6mihXHMBcRmrZ1o3BPqr4658JAvwQwgEc7z9sMb3Tfe5O1N-FOYsjeTZiWIJEYVPdAtE6MAv-U1gr2ZjFYN-7D6OFHmcweee4-uVid0pHT2l36ykaNgKLhIpLXCq6QH8_qbCkyNen5J7SfKgs0lJZLNFFcwJ5B7qrcn29RrzFsTuJvIDtfvERAx_WIsEUc3eQUvU15w6m7mk8PU2uHfVezvIvxAPqLnnY_asiiEpsQjTMhnW2U37NZBa_fslsfndZIsUgweMMu9TGiC5Ji0eMZcRuV3RnFsEHcKs05VROu91qHpm341MG5n2XHBG4mrYfl_P8K84-XRjgKD2qYZPkTar25lm1nk5xnKQ--20ICtwHtWAar4b1SLsEI3UEEnqCmsmf4cvJh7gWyKBrktES_E6z1LSNLbCJY5Va4iQ2sak70b3leFXS-XcMFwMKXIKQN3X6I6ODO_wK52XtTZkBgnLey7BlpPAEwiUTBHLTSBaOTA5FnZnKZj0LZ7CKrHaq7ty8xXUPZBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583654c04e.mp4?token=dFDhJiruuK4FGAn0CsZeke4xjynloSaqzYtsBhLTzTmGtUuDCDBX0fzRVoq7AWg2wly0JRrTOLliT_APnUrda4ZSLLN4jaelPBAG6QG0rBr4wNSY3OGnkCDM9a4ec1Iez83Q2iJ45gvA5cZpoQAlw2h_e0ZO7ul6mihXHMBcRmrZ1o3BPqr4658JAvwQwgEc7z9sMb3Tfe5O1N-FOYsjeTZiWIJEYVPdAtE6MAv-U1gr2ZjFYN-7D6OFHmcweee4-uVid0pHT2l36ykaNgKLhIpLXCq6QH8_qbCkyNen5J7SfKgs0lJZLNFFcwJ5B7qrcn29RrzFsTuJvIDtfvERAx_WIsEUc3eQUvU15w6m7mk8PU2uHfVezvIvxAPqLnnY_asiiEpsQjTMhnW2U37NZBa_fslsfndZIsUgweMMu9TGiC5Ji0eMZcRuV3RnFsEHcKs05VROu91qHpm341MG5n2XHBG4mrYfl_P8K84-XRjgKD2qYZPkTar25lm1nk5xnKQ--20ICtwHtWAar4b1SLsEI3UEEnqCmsmf4cvJh7gWyKBrktES_E6z1LSNLbCJY5Va4iQ2sak70b3leFXS-XcMFwMKXIKQN3X6I6ODO_wK52XtTZkBgnLey7BlpPAEwiUTBHLTSBaOTA5FnZnKZj0LZ7CKrHaq7ty8xXUPZBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور از تنگهٔ هرمز فقط با اجازهٔ ایران
🔹
پس از هشدار سپاه پاسداران، ۳ نفتکش متخلف خارجی که قصد عبور غیرمجاز از تنگهٔ هرمز را داشتند متوقف شده و به خلیج فارس بازگردانده شدند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/444873" target="_blank">📅 14:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444872">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/963f27ca18.mp4?token=SmAo3ZlTU8NpB61uug4F6Tbptu2E2gCe6-dXUKvjz6VLi5-pkSp0UqlHcjpskpy7h-qJd-nCpdeQmxcra7VdEvZOQNof-8V447WUQfEBOvt4GqnUut0HJ5YS9scQEfxpu25r71BhFjnklD3d1DAFtAxaGQ-9hKoFXdVo5JmhIwClaUD3xVEFeRbBB19XkoXcDT6Gu_vptAq05FpQZK4Vdk_K1ZfxVqU65NrBIZwgNrp9cBOMLT4Suhdfhv4qtS2dKYvQUAu0uAB5VWmwA-JEUdAD-bCxEkPvgnjocJdrFuqzy7zqSi6-R9GTyXyY6ZX4NdkjpnMMmjDjxTXGxv77wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/963f27ca18.mp4?token=SmAo3ZlTU8NpB61uug4F6Tbptu2E2gCe6-dXUKvjz6VLi5-pkSp0UqlHcjpskpy7h-qJd-nCpdeQmxcra7VdEvZOQNof-8V447WUQfEBOvt4GqnUut0HJ5YS9scQEfxpu25r71BhFjnklD3d1DAFtAxaGQ-9hKoFXdVo5JmhIwClaUD3xVEFeRbBB19XkoXcDT6Gu_vptAq05FpQZK4Vdk_K1ZfxVqU65NrBIZwgNrp9cBOMLT4Suhdfhv4qtS2dKYvQUAu0uAB5VWmwA-JEUdAD-bCxEkPvgnjocJdrFuqzy7zqSi6-R9GTyXyY6ZX4NdkjpnMMmjDjxTXGxv77wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نصب یکی از بزرگ‌ترین سکوهای نفتی خلیج فارس در شرایط جنگی
🔹
سکوی رشادت به وزن ۶۲۰۰ تن توسط مهندسان ایرانی طراحی ساخت اجرا و حمل‌ونقل و در میدان نفتی رشادت در خلیج فارس در روز اول تیر نصب شد.
🔹
این سکو به گفته مسئولان اجرای آن، قرار است ظرف ۶ ماه آینده با…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/444872" target="_blank">📅 14:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444870">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7c04248e.mp4?token=EVtHh5I7qH0xRkYJQO6huaJlXYfvQ5Pi6RJ2E7qudewbYgK4HAasFTch3D27_z6QzHg3-AsJX5UEhP_drqKeZdIo2d2pLSTwTd8uSjRsXahC8jYI8BAXRIiQVm4xFJkYnfRCEgbBA1Ec32k03AIlVEdP0V7bBO_SZClCMboF6ChMk2pnzUwvGvnyXAhhjGki4xgSVDdtMRd3GKTYua3KmtUW36J2W4yoCh_bHC3SRzWlIxdxE5WBxUm8gYA4pLfr6AdnWUykQH9X7ZCzXKvAmSv8tnr02OzXPU8iK0jstizPnIYtHdGro-4IrV83N5IR_WmIdjpcPo2OM1l7PZgcBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7c04248e.mp4?token=EVtHh5I7qH0xRkYJQO6huaJlXYfvQ5Pi6RJ2E7qudewbYgK4HAasFTch3D27_z6QzHg3-AsJX5UEhP_drqKeZdIo2d2pLSTwTd8uSjRsXahC8jYI8BAXRIiQVm4xFJkYnfRCEgbBA1Ec32k03AIlVEdP0V7bBO_SZClCMboF6ChMk2pnzUwvGvnyXAhhjGki4xgSVDdtMRd3GKTYua3KmtUW36J2W4yoCh_bHC3SRzWlIxdxE5WBxUm8gYA4pLfr6AdnWUykQH9X7ZCzXKvAmSv8tnr02OzXPU8iK0jstizPnIYtHdGro-4IrV83N5IR_WmIdjpcPo2OM1l7PZgcBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود دستهٔ پرشکوه طویریج به حرم امام حسین(ع)
🔸
هزاران زائر از سراسر جهان برای شرکت در این عزاداری، در منطقهٔ قنطرة‌السلام در روستای طویریج تجمع می‌کنند و سپس در مسیر ۲ کیلومتری هروله‌کنان به‌سمت حرم مطهر امام حسین(ع) به راه می‌افتند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/444870" target="_blank">📅 14:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444869">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دَرِ فردو و نطنز چه زمانی برای بازرسان آژانس باز می‌شود؟
🔹
به گزارش خبرنگار فارس، براساس شنیده‌ها از متن تفاهمنامهٔ مذاکرات هسته‌ای، نقش آژانس بین‌المللی انرژی اتمی صرفاً در مرحلهٔ پس از توافق نهایی تعریف شده است.
🔹
براساس مادهٔ ۸ این تفاهمنامه، در اجرای توافق جامع، یکی از گزینه‌های پیش‌رو برای مدیریت مواد هسته‌ای، رقیق‌سازی آنها در داخل ایران و زیر نظر آژانس خواهد بود؛ اما این مرحله، منوط به حل ۴ موضوع کلیدی است:
🔹
لغو کامل تحریم‌ها
🔹
ترسیم جزئیات بازسازی اقتصادی ایران
🔹
تعیین حدود و چارچوب خروج نیروهای آمریکایی از منطقه
🔹
نهایی‌شدن پروندهٔ هسته‌ای
🔹
منابع مطلع می‌گویند تا پیش از حصول توافق نهایی، مادهٔ ۹ تفاهمنامه صراحت دارد که ایران هیچ تغییری در برنامه هسته‌ای خود اعمال نخواهد کرد؛ تفسیر ضمنی این بند آن است که سطح نظارت‌های فعلی آژانس نیز بدون دگرگونی ادامه می‌یابد؛ به این معنا که ایران همچون گذشته، دسترسی موردی به سایت‌های بوشهر و تهران را برای بازرسان فراهم می‌کند، اما اجازهٔ ورود به سایر تأسیسات از جمله فردو، نطنز و اصفهان را نخواهد داد.
🔹
در همین حال، دیپلمات‌های آگاه از روند مذاکرات تأکید دارند که رافائل گروسی، مدیرکل آژانس که نامزدی دبیرکلی سازمان ملل را نیز در دستور کار دارد، در اظهارات اخیر خود تلاش دارد نقش بیشتری برای آژانس در این مرحله تعریف کند؛ اما موضع قاطع تهران، ادامهٔ روند فعلی و رد هرگونه زیاده‌خواهی پیش از توافق نهایی است.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/444869" target="_blank">📅 13:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444867">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c892433e.mp4?token=k5qoCZ3-jxAWick3gbQx-aMWqt7toJ6Wz9j6d1OZcicMvKd6zpcrTPSVZhL8DnnHO6YJP_ohzxxamz0_4QiFvAwkPysJB32thZLLMo6-2eZFAy_ikkz0tNQcvIU-ScyGplQbv4N50iH3j-J34nUTHfNutviSjoVnGtOYmdfS9fU7Z3yZQ4Mhx4FqtVx8_6m7OjOYFqQ_IaMehkv3Ptsop-aFb9uJuCuMYznsQEH2jeHfrE6zIfmSHMxr9Mh9l9e3vOcDagChTu1nX3kJLRxyfJO_VNbxpjcd753KSnsYpVgl5HBNiP3r6ifJBmqYwRDSx-aolgPd52ZPVDpXsp0h3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c892433e.mp4?token=k5qoCZ3-jxAWick3gbQx-aMWqt7toJ6Wz9j6d1OZcicMvKd6zpcrTPSVZhL8DnnHO6YJP_ohzxxamz0_4QiFvAwkPysJB32thZLLMo6-2eZFAy_ikkz0tNQcvIU-ScyGplQbv4N50iH3j-J34nUTHfNutviSjoVnGtOYmdfS9fU7Z3yZQ4Mhx4FqtVx8_6m7OjOYFqQ_IaMehkv3Ptsop-aFb9uJuCuMYznsQEH2jeHfrE6zIfmSHMxr9Mh9l9e3vOcDagChTu1nX3kJLRxyfJO_VNbxpjcd753KSnsYpVgl5HBNiP3r6ifJBmqYwRDSx-aolgPd52ZPVDpXsp0h3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متن حماسی که در اتاق همه بازیکنان تیم ملی نصب شده است
🔹
در تاریخ فقط یک چیز می‌ماند، آیا ایران صعود کرد یا نه.
🔹
چند روز دیگر هیچ‌کس از تعریف‌ها و تیترها حرف نمی‌زند، همه فقط می‌پرسند آیا ایران صعود کرد یا نه.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444867" target="_blank">📅 13:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444860">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IcbBd7-hHwbTf8IpA3CoIYCXbx58l9sr0BzIyTimHMJloUp_kKNtU0iYEBdVy5Y3bAQuEFRk76Gk1ieHT80Bgwi5RO_Ankzgnvs_b8UWYWwrwycXE8zOJIEhFDvyfk_2zVUHBnCutEJcg6Rghk29E1T-2T6ujRUinfQWnRsMIoSfcBxHL9lNjQHV5pqrYVqzPxaXE3sHsaDCZ_UIZKJX5j54siHVV8kShMIbvLBnNUAgpvfOvaRVY3WE8903F8NEujoaKqWenJAm6lL1QtQ64KeQe87vqiJqGuklig0Kzo6tv5QFIxB_gaC6PaGvPpJ2v6b2uO2-OjWExas3_7QG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MsknEhpktiXMx69Lh-8w0v67bZFbPr17Nmj-YWd3Ygx6p8BPjpqg05uIVgOTAV1GbpbOr7UoXp0YzG_q3VoE_40s2tNAh0WnxlitgIj7RjGrjcHdKcZotfPl9nIjAp0_o_Cc928pnrPwUF7BF2dvnRgEf3ZjJYwJYEkDOzMsiyo7Kv5Ubf2eGrpXbTb8bbX201bS7bO6ASYLCSd5VDumX_Iy_WuqB9XZN234ACQfMt3aFLsBqHPNVzesJkWyUb7hyVekYeR9nCikFT5nL08I0jRssFj-h1On7AoX8vGAbzAG0LDfHAbOq6rUYTNwI-yWzeAduLNeF0EzchEqRcgNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLxubW61nc4fvc92ztCP3GRejS0U0bFjIVa4kCSo0rdVPOiMF8Z0yH7jeEwlmPahBgxyP79CccW-p1ILdqltteFiPe6gH5cKK1axaVKMvX4237-Qp4k3CgBgQPK6MYGePQtXEOCb64KAiFmMCacmN-YYL7uqeLap0exZvndcOwbLlomiX6MIoUUarc427UylSLH2BANPlhNHazl3M6x22GzXY-oUzBNrJf8ZEXv8ZGFkyvHDETkiAIJN1OXj0wDQYuuluPO7oVovJY2nNoXOmePKOD9NyZSArA-DiHWcUR7V3tTmOh_SWKnnpmHknGSG_-zN1mP95znEPn5Pedli-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iE57qYRSEXFBU0l7R1QOZLtuZQCIHN0TayYuoThZYyDfTPJzugJWHQpZlFhvf0tlC0Vl1SpPau7gfXpGUMsVFX6j9DxF1DwHj7dVRMCRcUdGuj6D8rqa9_QTB8y3vhX9oE0Uv3lLBbf6NG_VTXHWPY8MIlk7U0n1USpWqf8pi-wqdK5yPW65wPoMp37dfHZjx8Y1TeHChh1xFjoqXAzEPeutqlI6bgSTYGqWosoh44cPJFFRrrv14oHB5MWoFb-Hs056LFAmFBWUrpXXZeluBDeorEom_oBGROfnQSxnbtMhTlI1eF7J4JOVs99jDmDsZEjeHebO_bdvrvRioS10VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5OTGUMIK9wJifiBmMP0vKpdDC4IeDTnj6gbmlUZb6Vsord0Ndpdignmf6sP7cHNs-SKJYHUE5IePyM5uMA5_cXAjNUbA2Q1afeNgbebKbc-iXy0u7UnAdxmxekCNp9_UhWtV7rnzX8pFJbZUksBnW2KI3YYaBWGu7taawP2euU46eBudoDG93snYfMlBmnw-RWjNz4FLU4I14qFBUv56y7ipKpGRTv-1DgQ7llfqFphCP9kqtFsfcY4b-F-4qXcL8be00pU9AGdsWiji1OXblzuDRZwLv0F6SNl8Es2Vycbe74zF0igmUcC3tARZdAqcVxok2xdCUAhitAt_AWwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SU2Llkr3zSOZWSOXFQoulCnb0I7RA-67INfIM0W6UWswfj2fx6btjtoctqTRBAMbsCeMWUNdxOPTyYKZIcJfTeC0UN-i134ZwM_W4pmiM65fmuZAW9M-GMIRjqUUxqbwy5hNTTAlIIEZpX1c0X11-vQGAaKtw6klTgEP93s55tsDv7ut8Wj2lwezsoDIxdCGBsnYnnmeqhhwakBN9mTZNloLoWt6kjMnfo41DUBRiIbvPtQrY45RK79V1-9r68SSF4UrFPShC7rrJi-Zsalmp3y_JWsOt443r_Df_hUWI1jRsJfOc9eyqFyCIqORWRMVAkvvGi9bsqOk66HBRWSISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jYL53jXWqi_gN6zAjZERtabWkM7dl6IuVKTtRuKhE-jS_DFVDbAe9thTroNTwa_f4NIqnnQ2hOsXOiIXUiNzRsVkx_FW3dyN9raD09wE147nX7pNpyMhPuYsFH4P7CD0oRfH_ntRXgOhMgzz58K3V1-pra4DUc_QjcEpfmBrSdaPDLioHuTVXCWPPJBN-gCQCO0DaWqjTNosQb5y768C2JxPUlKU47Wjtsq6DW2peBdHO6fMQCDOL8ciKJTO9Eb2U8cHETtJMyg_Q7Q0tABcHgcALECUD3iB2RJM_6C3pBBN5_SwDObhIMH4grLO0FvTfOcLz8BDn9pzpSegn6XOMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اشک و اسارت غریبانه
🔹
نمایش آیینی «یک بیابان بی کسی» با محوریت وقایع پس از شهادت حضرت اباعبدالله الحسین(ع) و اسارت اهل‌بیت ایشان در دولت‌آباد کرج اجرا شد.
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/444860" target="_blank">📅 13:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444859">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4cwv2yBABKdHHj5ccygXKqC-rB2teGWp93cIKWhwD18Be96Oi-3KDrkC3yilwJaG95T8AImEOwJK1ENgDdaSVIi3FkLibNXFT-9IIco92WNcrKfT2JCdAPiq8_8xP77nnvbujtGnz2_fd8iWbJWwnzGyNUPKChTWXCGWVkTctjlOccvTgr-UJvlszjuu1NpxaaJ-VRWF--IPkqaFyqV1fTZ_PDAR2nfmhWW4ARdk-yOv-EZmGjzIxaBXYqngW_BW6pKgLkl--Q0rD8ASUPrQEVQdIM0KlBQ99dzQ5ovN3iKVsd0a0d07IoliVFkviNU9brZmT8w6PsRvKHpTMSTPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب نماز جمعهٔ تهران: اخلالگران اقتصاد کشور باید مجازات شوند
🔹
علی‌اکبری: اگر در جامعه‌ای ظلم به افراد ضعیف رواج پیدا کند، برکت از آن جامعه گرفته می‌شود و خداوند متعال ظالمان را به‌شدت مورد مؤاخذه قرار خواهد داد.
🔹
احتکار و گران‌سازی عمدی، به‌ویژه در شرایط جنگی، از مصادیق فساد و تضییع حقوق مردم است و کسانی که معیشت و سفره مردم را گروگان می‌گیرند، باید متناسب با جرم خود مجازات شوند.
🔹
شواهد نشان می‌دهد جریاناتی به‌صورت سازمان‌یافته و با سوءاستفاده از شرایط موجود، درصدد جابه‌جایی مرزهای عفت و حیا در جامعه هستند؛ مقابله با این روند نیازمند طراحی‌های جدید و بهره‌گیری از همهٔ ظرفیت‌های کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444859" target="_blank">📅 13:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444858">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkSUagR9YUJPhtPJ1hVCsHBKC_nxYgUsHa2ILn4u8bXfRkumnXJ4EC1XVzF91hUxi7VxzQ5G6YuQdVTLhl6QYfYWTXshskO2XWn3Ft0KPsf6wXXlX7qBJxi0ge4PrzvGsHgQWPnse9K0ODVZCTW6dSxcVT8KDdM2bWx8R-fRs9UPMMINIjzjqbrpK-u3Xd_GDuiZg1FecwiJOtdkM32ZzdGkRMDmWa9-dNJ84vB4cLD8zhd2CNyVwGNNYxZlAcXBBSfdSIPbD91DW57-vhy0-mF1bQEi7U2Qstik2oib3hK20viTrkm-iGk5YPDtBGxMvMQB1Fk6Ae2UdY_bYBSnvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطبه‌های نماز جمعه را در صفحات ائمه جمعه در فارس تعاملی دنبال کنید
🔸
امام جمعه مشهد
🔸
امام جمعه اردبیل
🔸
امام جمعه اهواز
🔸
امام جمعه یاسوج
🔸
امام جمعه قزوین
🔸
امام جمعه پاوه
🔸
امام جمعه کرمانشاه
🔸
امام جمعه زنجان
🔸
امام جمعه همدان
🔹
امام جمعه ساری
🔹
امام جمعه بوشهر
🔹
امام جمعه اراک
🔹
امام جمعه شهرکرد
🔹
امام جمعه کرمان
🔹
امام جمعه زاهدان
🔹
امام جمعه سمنان
@Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/444858" target="_blank">📅 13:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444857">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ei1H8PWB4Zkeudhzep-WLsMCOqg433AnBQXZ5AC72xJWVKlJsEO7fFH4sBcMdrdhSzmKG4DrmlrOCzGGj6zo4CqcbLNLxNI0AFvldOOlST2LLlXwBKWquNgh6hPxt2uXzCpvTrg-t1cCzmq0TGrwDrLCOudiYP8j0Y6lERykUbYD6paDB6UW0EGSFtfFvwE-Qjwma924oOyHr35ha7L3rmnFj2wCSw6teNQ6C9_eJUTNMqUfpCAU5ZuoWBhKONOFebIa0GJkYs0rpdR3YqhZAni1Op1NZYUZsbhQ7w8nsoVxrWA8BPkC9VjfQacC_NJpKj4gIHJ1WZg5D3iCHhjpqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت بازی پرسپولیس و چادرملو تغییر کرد
🔹
با اعلام سازمان لیگ، به‌دلیل درخواست شبکهٔ سه سیما برای پخش مسابقهٔ تیم ملی والیبال مقابل ژاپن، ساعت بازی ۲ تیم چادرملو اردکان و‌ پرسپولیس، امروز به‌جای ساعت ۱۸:۴۵ در ساعت ۲۰:۳۰ آغاز می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/444857" target="_blank">📅 12:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444856">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_Ybyy6gyiaeifdGPrYksgP3wA1hYjW3NdjY2EJXH5RCKUejbQMzcFTnVoGhjOoJa5oiFhD0BBCnQJZhGZosUfqr-HqfidSpBwPjEOqdKRhlTgexAGKtVH8yWMf1y57H98id7HPZQ1Es1S6phIxk7iVa_vdy8LOe4ADaLVPAvkSwqQEhmT7Qr4aADyTYZiky7LdeoI7BImMyn83YhxeHKCqGwE7Q-byHRlm_Zh4DZgV5Jy-n8BIqrlGez0xzADTZuIOB3-6hr7IlIsbG-ELyR61M8StBdRvnhXZnujoKIcqo4-Q69hmg9uk0sQkjrahyqKlTdUexil1gWukRLK9tAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی سپاه: عبور ایمن از تنگۀ هرمز تنها از مسیرهای اعلامی جمهوری اسلامی ایران ممکن است  بسم الله الرحمن الرحیم
🔹
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444856" target="_blank">📅 12:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444855">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQeUzVWD9RmFxuPAp4bUig9ctCjeI8vu_oD4GD5l4sNeQrAINmvodYGjNbu3bMrbXleCiXAHlmbTuzqqT4hjTGt1EyyHQcbRWv6OMliy9o_5SF0w_Zt0mwnSZmuTsgvIg1R0rEuI8I3xYEO8z7fckmVRHb2AudwLmiiD5SGPb-Dk84wnSYQ5ftCJ084CaU2D3tIRtmkosgRYRcReyF0Vv5wR7Wn43UTs4gquqfORlU1o1q7SAZgirRHTN5_8-MDCcB5Y_lHTnkKif0P4RbzCcIZrJZHogN_NUiadjWQcFR4DMThINzlZrMZeiL-WcCCmMBd0B9WQ4lBqmI6g9iMnGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبس گرم‌ترین نقطهٔ جهان شد
🔹
براساس داده‌های منتشرشده از سامانه Relay Weather، ایستگاه هواشناسی طبس با ثبت دمای ۴۶.۸ درجه سانتی‌گراد در ۲۴ ساعت اخیر، در صدر فهرست گرم‌ترین نقاط جهان قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444855" target="_blank">📅 12:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444854">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgLWGohFtn3DGWXReGRmH6dBnVbLIW2K9O-KuyJB_YfvftaMJ7itZK0EHYwyla8EiYQc7THWo7ROI2Q7tjG3VJncU4SlYnXniOqwj_63B02Jqmmpty1AweXLgsg_MdpaFm3MopTQe4zA0f5DUz-1C3h-VXWNdIvArh7g2GJapHnuedA6DZvUj_NaRZLVNlg-BEEBpYGx--x2oqy-4_2V56Sx40jCrf8HI9EEHzp2uY5b35G7yR1JSwSEtFwBBd1lYsm7FkS2d5nidVLokBaAGIiji9S12pRi8smduXzpLB5mvd10ol7Idnofs0zTSuBCViiEWCrcmNaKcvTyGH2l3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازداشت یک ایرانی در مونته‌نگرو با درخواست اف‌بی‌آی
🔹
پلیس مونته‌نگرو به درخواست اف‌بی‌آی، یک تبعه ایرانی را به اتهام حملات هکری گسترده علیه دانشگاه‌های آمریکا و آنچه «خدمت به سپاه» خوانده شده، بازداشت کرد.
🔹
اداره پلیس مونته‌نگرو  امروز در بیانیه‌ای مدعی شد این فرد از سال ۲۰۱۳ تاکنون حملات هکری گسترده‌ای را علیه بیش از ۱۵۰ دانشگاه در ایالات متحده انجام داده و خسارتی بالغ بر ۳.۴ میلیارد دلار به بار آورده است.
🔹
در این بیانیه همچنین ادعا شده که داده‌های به‌دست‌آمده و دسترسی به حساب‌های دانشگاهی نفوذشده، در خدمت سپاه پاسداران انقلاب اسلامی و سایر نهادهای ایرانی قرار گرفته است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444854" target="_blank">📅 11:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444853">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej_q4LfWRkIj_oCd5jPHPDw5lA9dYUEL4E67EQykyXwUdIIQI8ChdHi3MUBewfsUY1MPKgfYwmJ9lkkYtWyraQMyb3ag4mkY0igMLn2EmCL0EqbnAsLG7AZRJUfPLjkRDJVZLC0IJSlqTioy1jsj2unRC-M4xCPwHqknfJldR5sC1k8ivmeOmcsy-5v-5PlBcLdj9_tQ0yhcfiwfcNRaZz4mg7-BvMVZHGv8mGaZNjDCsUJl9VGPl_TzZmm16755oDtVbutHePSlRR4mzkUkrZNPh0gi4aLGF_ARto9WZJsZ17PDQ1xlm1InaWWqsBaU3hJxAVG2hQwkEyT4cbICqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگترین و دقیق‌ترین تصویر از کهکشان راه شیری منتشر شد
🔹
تلسکوپ فضایی «اقلیدس» دقیق‌ترین تصویر ثبت‌شده تاکنون از مرکز کهکشان راه شیری را منتشر کرده است.
🔹
این تصویر که از ترکیب ۹ عکس مجزا ساخته شده، وضوحی برابر با ۳۲۴ مگاپیکسل دارد و بیش از ۶۰ میلیون ستاره را در بخش متراکم مرکزی کهکشان، موسوم به «برآمدگی کهکشانی»، به نمایش می‌گذارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444853" target="_blank">📅 11:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444852">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/semFvZXDXVM0cP_uGceVCFo-svlAtVSHc6sWtAKyAYr9jSUkDG59V8ZpkQWP3JD4PaNoJOVbT93hqm17sWfVkNVfjW0krIYkdBBiBoZItKJ8eUblcFOVw_3_4teAI9d7_iF1ENHwKwAUD8BY0GTXEVr0Iz23-9heCm1EKv18lQDcp2W3aHxLMcd2565zvgOkzCUCOuQCK7Jkq96rAyTw9xTLYqApZnLf1qDSK9b5lNx_WwKAWXXGCKCXsyiDo-QSayDzNr8ROhHyC2qhyK6emMU9Ao_3Kew0g9aBbckVe17hdN-SZ372t3623FGVPr9AGmgitBiI5lgsL1zpo0la_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل حزب‌الله: در کنار ایران خواهیم ایستاد
🔹
علی‌رغم تجاوز، ایران استقامت کرد و محکم ایستاد.
🔹
ایران به تفاهم‌نامه‌ای دست یافت که اعلام رسمی شکست آمریکا و اسرائیل بود. امروز، ایران در حال شکل دادن به آینده است، نه تنها برای خود، بلکه برای کل منطقه.
🔹
از…</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/444852" target="_blank">📅 11:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444851">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bH16TcxsXhb30Vcj2XaQZcmfla_cTn1m1F5oD97deO-bPOvBh88h_qFiQTgKGc6xwINh7RUnppKX30SRLZ2bYU837ccebApq26WopXA0R7qH3IwUhOuZeMGueMNwRhVjNAdb2i1VR3wNkblr4LjeCHrE0qdCI9A_Xavm-oN5NUArln4zXKv_5KM4y0BbXnrfIthtyrIa7OwU4-nkZZftpkYwoRQb6ap7bcnuhJXNFYSsUXAQfIM9d2Gs4KWlpmNbhOqOW31yfDE2Tjw8j2BXpMaSLFd3mzof-64KcY2a8Dia4MdnmtQSlw-4OwdtCJYYjMBZo9pciQdxaJBEXyix0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل حزب‌الله: اسرائیل چاره‌ای جز عقب‌نشینی کامل از لبنان و توقف تجاوزات زمینی، دریایی و هوایی ندارد
🔹
دشمنان جنگ همه‌جانبه و بزرگی را در زمین، هوا و دریا علیه غیرنظامیان، زیرساخت‌ها و مظاهر زندگی آغاز کردند.
🔹
آن‌ها با استخدام مزدوران، طراحی فتنه‌های فرقه‌ای…</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/444851" target="_blank">📅 11:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444849">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAUj4cvNffnIrAG_ml4wRO9o8YH69FC22NqOkrMlRWZfozr8dFghq6SsmX6iV60NiyV56ggpfkqc0hlo039bhK9uxkPLRzGry4URhmp6w9Z97UgY_n1UZoEKhp7D7zFRjJEQNiKHQPajZ_wFC3LE6_p3MQLrarXcMxqG4uVdMZk_ZEnbbQU2y1VtC8WndfZgpDK-o3pzNthJGq0yR0I-iNX5nS_CFCz3ctEE40nV5iyCcYzOB58C6iqOYPA6aDQdlGUVASbQPLU3tdMkCwVidzT4eRjHTqZXC9qgfP1gTe6TIfY3PGU4NLaC7GrI8PzKsq9eojrpTZy2Zoda4dG1BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KA-4lGR6fOiPCLsbvgkSX0U-z4EyaZd001SwSnz2YtjcCyfuWN86GUSnpA030U7c3swxnYmSixgMrSJHb7wNCpOdhVDqyRbTBsSD6of-9zFaPMiFuWV-ikZfIMjdrz1xpOsyWoi1zf2179KTUGpbT_S3QfZdbUMgMYl3tTMAktHUGgBqjt2Z6pd60ipe-it8Mot11dNb_91QYKyk4XB6OIypmYpx3R24qXrERDAgk0g3mp3B9FoSpwSuuHCcH2IgPbgTqVGT5BOXebwhJ_bZeB-zB2z4Yi7-M7T6iRWTR5Cv7u1lhz2gbAa_zEGJP1xJcl5RRrmo3C5GIiDkFBGy1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیهٔ وزارت خارجه دربارهٔ بیانیهٔ مداخله‌جویانهٔ وزرای خارجهٔ آمریکا و شورای همکاری خلیج فارس
🔹
وزارت امور خارجه جمهوری اسلامی ایران، مواضع مندرج در بیانیه مشترک وزیر امور خارجه آمریکا و وزرای خارجه شورای همکاری خلیج فارس -مورخ ۲۵ ژوئن ۲۰۲۶- را مداخله‌جویانه، غیرمسئولانه و تحریک‌آمیز دانسته و نسبت به ادامه رفتارهای ستیزه‌جویانه و مداخله‌جویانه در منطقه هشدار می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/444849" target="_blank">📅 11:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444848">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_5CNiXO4jqafK6DuRebdIOuTWIhJYznzYApr3qLP_pvtWW0aNGf2pXQTQxfpKksdcsWSAUD5K9psSEheWagIG-Luml8Z0nH0RQvj6UYYZARIs-vFEBBag7YFyGA8sQAO6JtzkgN3XmM7SVWz0ObnMW1DmBF0aIfPqYeckYLYveNjJaxzf39-KWwm1zwLfMJPA2f26jmNn2UPrQvR9GQB9lmLf-WAHMNjdKjww_VXOEwRegk99_FUv3xHH7r8JCZWJYrnUm3bD_GA69bHbafDzOvqmCbdliYnqBDEz5-LoaiH24EvdV59b-z6n0zO2QtPiVHWQ7o1kLXHnXanbSXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل حزب‌الله: اسرائیل چاره‌ای جز عقب‌نشینی کامل از لبنان و توقف تجاوزات زمینی، دریایی و هوایی ندارد
🔹
دشمنان جنگ همه‌جانبه و بزرگی را در زمین، هوا و دریا علیه غیرنظامیان، زیرساخت‌ها و مظاهر زندگی آغاز کردند.
🔹
آن‌ها با استخدام مزدوران، طراحی فتنه‌های فرقه‌ای و اعمال محاصره مالی، سیاسی و فرهنگی، به دنبال نابودی کامل وجود ما بودند.
🔹
ما با صدای بلند اعلام می‌کنیم که طرح آمریکایی-اسرائیلی را در هم شکسته‌ایم و اکنون همگان باید خود را با این معادله و مرحله جدید وفق دهند.
🔹
این تهاجم که هم‌زمان با تجاوز به جمهوری اسلامی ایران به منظور براندازی نظام و سلطه بر توانمندی‌های آن صورت گرفت، در دستیابی به اهداف شوم خود کاملاً ناکام ماند.
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/444848" target="_blank">📅 11:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444847">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترافیک سنگین در جاده‌های مازندران و‌ مسدود‌شدن کندوان
🔹
پلیس‌راه مازندران: از ساعت ۱۱ مسیر جنوب به شمال محور کندوان در آزادراه تهران-شمال مسدود شد.
🔹
همچنین پیش‌بینی می‌شود از حدود ساعت ۱۴ تا ۱۵، مسیر کندوان در جهت شمال به جنوب یک‌طرفه شود.
🔹
در جادهٔ هراز نیز محدودیت یک‌طرفهٔ مقطعی در دستور کار قرار دارد و زمان اجرای آن بر اساس حجم تردد تعیین خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/444847" target="_blank">📅 11:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444846">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pso9hmmV-jnxuFqiQAd4GVrQryuuun6rk93aVcBZw_adPbOX5V9nVfeRzTaSnkkpMIVmdtmmhBWuHbKJaPZcKFQ7FFPDWUex9io5zZGPQuivYlPWIm-6uxm21zXEIcVTuCE6pZdlUMCnGY-At1SIfIbtanY4PArbSXx3q-aeIPHE3GOFTkeEf4VnbeOQBYSO9dHdSrsaw82jlfeDUkC5MHgCqpuXUJy8BHb3x3Jlt7NSdPO8fOHXyr30qngnW8-hbnSZnMQ87UHMthtjdt7wvrDRwzcWFxX-npAx6ApljDD04eHMEp3fT_nimrDkPtIaky1L4FOvhUDax1ao8e8_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمدید مذاکرات غیرمستقیم لبنان و اسرائیل در سایه اختلافات
🔹
وزارت امور خارجه آمریکا اعلام کرد مذاکرات غیرمستقیم میان لبنان و اسرائیل که قرار بود روز گذشته در دور پنجم خود پایان یابد، برای چهارمین روز طی روز جمعه تمدید شده است.
🔹
این تمدید پس از آن صورت گرفت که تلاش‌ها برای دستیابی به یک فرمول نهایی جهت «اعلامیه مشترک» به دلیل اختلافات عمیق طرفین به بن‌بست رسید.
🔹
منابع آگاه گزارش دادند که «مارکو روبیو»، وزیر خارجه آمریکا، شخصاً در جریان این دور از مذاکرات مداخله کرده است.
🔹
محور اصلی این تنش‌ها، اختلاف بر سر ماهیت خروجی گفتگوهاست؛ اسرائیل بر امضای یک توافق دوجانبه رسمی و الزام‌آور پافشاری می‌کند، در حالی که هیئت لبنانی تنها حاضر به پذیرش فرمول «اعلامیه نیات سیاسی» تحت نظارت آمریکا است و از ورود به معاهده مستقیم امتناع می‌ورزد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/444846" target="_blank">📅 10:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444845">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
قرارگاه مرکزی خاتم‌الانبیا(ص): تحرکات و حضور هواپیماهای نظامی ارتش تروریستی رژیم صهیونیستی در آسمان برخی کشورهای همسایه به سمت ایران را اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
🔹
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل رژیم صهیونیستی نباشد، جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/444845" target="_blank">📅 10:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444844">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJjbORyiDXHKjSncxbcDCj-YM5Oo5JrQaqoEervpSeDFKhI4Eo4u3jfVoEX4dc43FjAJUymXlWNM5rMdyNJ1v8VGnZOKkcI3CqBo9W8xSxSv2um7eL8PGaTxKpuGiDWFxSuTz55Qoa-dXyFBhoL0oFFrJ0c7KLfxbS2nRRfviQFnJGqPI9fRneotnNnc1VEcrrEKdduM5-WMSwNvyfgpPLLhGv-Bu6mcyQvwZwxHHuhlM4UMR2X6F1mkKAbIaPOr9IFPBF_bA46yR0Pg6aiPsD40jGAQJy0hKFAIYpXVoo47W9tMwGXSrx0rvoKVvqu4yDoEoEdIZDTnonbhMEAW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پوستر فدراسیون فوتبال ایران برای بازی مقابل مصر
🔸
این بازی فردا ساعت ۶:۳۰ در ورزشگاه لومن فیلد سیاتل برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444844" target="_blank">📅 10:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444843">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqCaVYg4oHKJxB7QLT3zNuDNpLGQNZV4IXTKfdlAKBv0rFrQ_f9oglP-U-OEmjK5lFe5UTDzCpKbLA8iG5SJ8exYcfqbFvyDxt2gzjiyiyN03uowmK1xDW38wU2TyaoXzPZd7qmoyU8ZEZhJ0CByIRQ1aY6KwKXjxghb9Z0KU3MIEEA3drkbUa67Wt1I1rsGO2yZbFthFv_Lz84zh5uLluI7sqXMI9N80p82ELyl6z2g71ZYvX9Ms1wh8y-pAQnCBZrj_aVSeRD-RLSfZkT75Hb3qVWPNs0c5yJax84q5SDsBEFYuMcmOrYoGXGskb1j0NVTZcs8pcEzc1xNMv7a5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای آخر هفتهٔ تهران در وضعیت قابل‌قبول
🔹
براساس اعلام شرکت کنترل کیفیت هوای تهران، میانگین شاخص کیفیت هوا در پایتخت به عدد ۷۷ رسیده و در وضعیت «قابل‌قبول» قرار دارد.
🔹
همچنین میانگین شاخص هوای تهران در ۲۴ ساعت گذشته نیز در محدودهٔ قابل‌قبول قرار داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/444843" target="_blank">📅 10:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444836">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f22l787pzFV6XxDOdGzq18MGxwRvuzBCMEJiutxeEPTTxjwhwBTauPdsr4QnNoTOcWih-xpBYhfJ0gPOJfEq9moxlap-of-3impjssDeQWrDoz_qlJMulcADYH8jUXkAtYul1If0_FUP5QDXxydOMq3xvvTg0TvblqkGK1M6L16Lj3lLWSds79D0A80N5fgKvidbyVz8hOqJgaX047Mqzpx0Pt8qhY3nRYa3L9L8ebsRvhtGvM8djMP-WRLNBFB_r2Jx0TxwAWbgazPheiTznr232nC1sygZoOcKck3fU8EdFg0qyppj9EFSe5cmhOQumrJFw746BIIi2jEcTc4OxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCfQRK6_RDNPwHXHMmyIpN_-1ZuEHom9PLb_0-rCyVMac-Wa3kMTNDfvjTEIaLpmVqd-EqfBCLdmrxAhvwwaG4Ed0LUFpvzgjag6SVlh2kKQ53VC_69VdJCO52-XjnQH-UTMjNoCXUBSbJRD_vKjoKZb6etRYoSLCwbAoLj_wYf9FDywo0ynPATurYz_lVb17pTXWWvHVOQZniI0j49eKHG1am4VopVFvlLjYqjUF2uOFOfzolb3rqStunpR1bB88ppNK5UZui2jSz667lcdkyJS1WTT4pdQszmmAlWeCJhUEGwVCGSWZjj5xmKAHKkU7E9kfjibb2JD7olVd7qKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSwGjUilqUvpHM_9cbqEXF_gFq_8v-k900o7d7UB72YRzcf-5Bi40-gW32FrG6e-fHuOp0Ehpzd_UWxmyjcDCFDtIy8Ntwek-X-vKVOyJgEOVmGQ5aBVwpGJY7TwP3eDyjQlemjKH9N-djawlEEAk8pm1FrFpV47E9HLkClNHdg88ppSaNWMTCilgo_unMGTP9ZtmxJHtcc4sBNHoqDhmerYhITD4Z_Qng7er-OFwPyCe9QfUmkv2e5cNK4q2OTo6dv5g4r9xFSiNPfhqE1H1B9aqQNz2h3zG2yTJAuaW4sYT9BxVv2YTpRUk8W4Y4vxZ7xPy30BbWKg_pfLcYi4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIG3ju4wDTVqGFtCEJ58riEradIBCgxDz2iir9HfJoTN2Q-L46Jih9hS_HapzVjXbnNuDA84uqbSuyTBbi8GJCBVA1wbxZZ_INwDmnhE_aP-gZe8AoKHW2A4qAHt4QNRwyNMCFVRceOF4oQ1mkORDade6CiADGBsqJ00IJKHkl8tMbIZDiWvIfTQKnJ55Xs2SLfuaQfyf3dCgdltgBpzltI9F9YLXCd6RSljMCY9GmrouxXnMzfUlrC8C5_4cBAnDFsWlxFmNPYSwzH6xABgUxeBg-GycwPBdoZypLS6u9EA08RtJg6pqSwCryT5eLUbxii-MQiEUTExTL-sNe2l9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MDFFu2ki7LLoMUAf263PHfJNbiybwATQMBvzmVDqLCnDngw_8q0M1SRv2abeiZ13LptYKodjYFrOWoHrE8L_IsG7HGGQu1lDSTlY9z2cO8SDustCtZ_2rjQZ2eprn1eGuV8I6FnNZA3X-RJeV8YRG1uLbIQaf33n3ugYW8_JU5kpP2ggjty9Y4bP6DkW89zfJAJ_gHsoSVYfrOVPgCBp93mw2XiOanS_FN5GKYECzHx7L6KDAOEYQU9fHgHP21S_GblIALcGSSPTS2HQYrAeptk5Jxr_DxbAn2Ih0ZsiN1BzPD3GrwFbMHahlzhc2Zq6vthxk7ZQ70cqyifu6qEy1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FuwkmUsSAGhZSmPOd0Q5ya9EWRpYu8b9h-KiLifBp3s4FmxSF_8hEtCL4D32dUiRYLmkK6338bCOhwRg4y7_YN5SxRDw9g6JiDGaAWhKNTezJvf5sdV74P6chDsAjlpl2x75HRCj2WQvGB-UXavmuFJbm0Tp823Xv_3RivYWn-EyybMSEzoQGZov9mJj9CCvdNX9dSQhwX_VHDRElUOKvMEfUmk6dX_IeN44veGWFKv7OL0GzTJtVQtvS2cf5nSEfuuCL4nMJ7wBFnsO_mPqV6bH8DYBCPyKBcLiQyqn4OFAU7VZzNkUqkPuxy_HoyLPTf6In5Xfyv1Nw1SoatFNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZylA-u0R8vjNBoqaUvC6T0BsjvBRsYI-cwpfcDJctdF7eVTPGVY3JP8_28TcCUCSIVgDpCHzUbmCAtHYrpMZZ6lrHoYM11VSTnkn7Z1WVpiP6ObO0Qox8WNQzMc4ElNbujj4YoBjIiZGbqsZOY8pbsAmtEmn7Z9QTJaWkRuO4agRA5mkK4vHKYRyJtqfT8puM0IZOIy87DmzwYMCRA-HG_3qH9bGFJxXW97H0ESJ1d0EUdIouMgBXy3eaApbgin7uxJ6hmO6yHWYTPrBB2nTxCtntw6-GE4OyeqrWQXjNpSyVCTE4lNmxZTyylXBqBpp6sFtgPMI-5dEeBT4S1HTug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم
شام غریبان در قتلگاه شجرهٔ طیبهٔ میناب
عکس:
معصومه کمالی
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/444836" target="_blank">📅 10:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444835">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dio3wB8BD6_3RK24ZICZJ6XUxqUc8D-iXpDvsXbrG-tZCH0dZu9zr_dg3Vdht7sAi_Ag1sVppGSxHxnnscTH2692JCSsSgKxFrC78FNHGLv7sokJYwznl0gB6QgJ7wmus98Gx8G1exsyqyqM3G4ifseSeOBEGubbgaltmGWR0t3adMm0sL8WNqiJy3LwTKLFwncILlrTcBaCoK2npNLsj7sFAlJCWWhQNTi48o1koe1t3mflZJU08GNETH5Iv2UBERBKnrhpHSx6zGwypWGZlg6snzQptGqhLIC0K73dZfOiXbtRsOMeMJBEb9RHthqBA8yQc4bS0OIzXe2DczIdrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ پهپادی رژیم صهیونی به جنوب لبنان
🔹
خبرنگار المیادین در جنوب لبنان از حملهٔ پهپادی رژیم صهیونیستی به شهرک المنصوری در شهرستان صور خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/444835" target="_blank">📅 09:44 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
