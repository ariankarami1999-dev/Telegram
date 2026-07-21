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
<img src="https://cdn4.telesco.pe/file/Pn8m4jQS6My3h9qHmJdPGuKEtn33QUv6mPHvJw2mIKjQu1blN-Oo2a2tc3j-mvomdsHFk2aOObrOjHV0ku_qtpRXjiaMHlobajTOKLRfMZACvdqHyikBNcYelQisaRnT07YP43Ys6rMfbUoC8xMu6gNVGhyPX07o3uFUoCzrgOgIQwqvdkCudQBXOBh_Ay-rYEtCqSqJPD3Uo9KuX9TIsrZFLn2yIbK80yGIyqweaCm5Gxwsp-Dj9tQjhVkYFmAdujukDXI6M-gpi5OzmQ2aNhPC9LukYVatM9tjIm0D8kbLGZZl54suE5JlXUfAaCP-4MEVYJnT6cD1ads66cdPHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 156K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 18:01:04</div>
<hr>

<div class="tg-post" id="msg-68722">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la-1Yp4S9Ue66-D7Ym2yCu2WPztDJS2Ixh2o0yNABCJCMuilRg7rVER7U9iD0EmVNL6y04Aw3_6NVpWDRFkru83L_xcx8PRf7P-AjUtGIV3ba8-sSCYFFdjDjpELSe5DsR7XCHdYTYUDtpwBAKhic0PD__n9nacdQEKWEOkarlE8im7jZpVfjtU7CJikj238E0Fb596MXQ54PvCE6mFXkiREpY12Pt0d3DEsoyd2SoTsW68U4kaebbul7VJ2Fx8D052prYSdSLGzaVoKHYQ3_hw8NJpwPNoMmgee59I5tuas3WUihUhP-ghh0vWEStBsnIrf6hYMyL08TmCEI_kERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:  این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟ این گل‌محمد محمدی، 23 ساله هس. امروز صبح توسط حکومت جمهوری اسلامی اعدام شد. تنها. بی‌گناه.  @News_Hut</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/news_hut/68722" target="_blank">📅 17:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68720">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/OEIPAJc9r5PWJSde1W_eGMIA6L8irXsSXx467Hz9SSkGTCO5am6C-ToJaY1CMpyNTiws06JiiL6BPfeF2qOvTHGEpa72JDQ9bmTm5noYrBRCeP989DxPKKV0pJJcgYCnoTPMeyozSXWh8ck80N-1qM_KfG-yH64uYTbJi_Cz5otoWs5ZZxfIyTQbv9DYFJZwupjmzai5A6u6nfrzmlbNh34lyyug23Dd_QDluwVMAJFYl0cR5v6PucxT3ExLzQGhz4e66Bj5OjxsH6vscNR4BfV8aQp4HZHFwQd47K-0o_A-gdX21uZbxHSjd3cyBaOZjTxGbATQd4UbrLOsuecSmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/jfeTqOL7tAK2hY5uFrElhvjFORhEo7pnkds9i6Xfi88cQ-k4uUCUTCtQA6D4uj-dYTAfDoELvXE1j1uoPS756pFgXZtXR30lAoSBe6ctNkKtT6dMKy0V7WAtFExgJ2Bi6ES4g4PRLI-7Hd1JATwuDpaXiSAf4O3anoTU6vsJb2-qg9S-o6DkQ2SDfoJRwgLEUjyCSn_URgA9QdIxwTrHuwd4n7Jj3mNtanM7aOMhBI9xznCed6xJ5SIeDAZrVgnP20mW-inPRnNuO8OsxCrL87kB8VAAVNOJq32nTJMYk7qZ6nXJII19uOGfU6fHNM6GuCRrPHCWIsl-OCLxv5HspQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:
این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟
این گل‌محمد محمدی، 23 ساله هس.
امروز صبح توسط حکومت جمهوری اسلامی اعدام شد.
تنها. بی‌گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/news_hut/68720" target="_blank">📅 17:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68719">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=VirdSLGrHqOg4tNx5x358pMupAHpsTYxa31PELuR15Hy5tT89fHXMrdOQGy_5GoxbjWWtT2-lQzvk3hzQinAZX-6cK3MSHQvJ_f9aZT9345ZgFx-DC9PbFo8x9TiY8Uk6eEks_ihWAGmJH7tMslXsama4TZsuOuzmumx_fDrkUPz736ypZk4UVXLd-GMcJxM1lfdI4fErJRTIvt7clubLqgq7hxTvUoIlfoO5V8cwWRMSkz3Gc06W17wkJ-MNOK7tidruuT9xSxyQS6JFZ3yd_q_74NSmqwf5c4PSwRKJG4rjZvHHhBnSEni6xLw9Y4HbGlJ6QtrQC0qJ00uiy3nPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=VirdSLGrHqOg4tNx5x358pMupAHpsTYxa31PELuR15Hy5tT89fHXMrdOQGy_5GoxbjWWtT2-lQzvk3hzQinAZX-6cK3MSHQvJ_f9aZT9345ZgFx-DC9PbFo8x9TiY8Uk6eEks_ihWAGmJH7tMslXsama4TZsuOuzmumx_fDrkUPz736ypZk4UVXLd-GMcJxM1lfdI4fErJRTIvt7clubLqgq7hxTvUoIlfoO5V8cwWRMSkz3Gc06W17wkJ-MNOK7tidruuT9xSxyQS6JFZ3yd_q_74NSmqwf5c4PSwRKJG4rjZvHHhBnSEni6xLw9Y4HbGlJ6QtrQC0qJ00uiy3nPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمعات شبانه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/news_hut/68719" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68718">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l43FwaK9il68Ce9HkJAbVy8vE_x-Iw917uamSbHRjXz89GyLoFTJrwn8-QXBaskw9M8aYzc9Ydo6JKVrTVAWH9jywvsc1Kljb1CwMF5hdCw1h4pSPICo8cI8HvuaOeOHlf1eaqIz6hzLtMoW8w4d6JDPO1wSOB21DB99hwEflZweoveDDoMqwXAPjPx0tyxZ-jC-CI3uTYsJGV0V3VKzbPZ-483RU4MfeFB4_00qFsZofFrf_r9cM_qW2v0luzm4u1lHATpYQc7asIui4tk5_RhlDijWqZwtWjKqMzc3lLCH30KcL5jR5MpKcBV3fu-2x_YpbnzSmLI-BREj7IfY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هویت نظامی آمریکایی که در جریان انهدام کنترل‌شدۀ یک پهپاد تهاجمی ایرانی در پایگاه هوایی اربیل در تاریخ ۱۹ ژوئیه کشته شد، گروهبان «مایکل سوینتون»، ۳۰ ساله و اهل فایت‌ویل در ایالت کارولینای شمالی، اعلام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/68718" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68717">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da37587eed.mp4?token=PqFhcWd4M1XLzFSmj0nhytnaj9tPDaR3J-T00pNPqpnj-cIJ5iUM_1gdjjYY43iqyyy3cDf0kk4V8poQ3q1jx9_23dNWbZT4Kd90xa0raKhEug0lmEPktzejtCs7Wr0H2E5Flb6Jio9Ac8oKkKyukm_C_fp6dCdy-iHupVNuTvPi0LhxeTnXypBTRiOwv_ZQkkoYrgrX5auhxcBWccKeIulWT6sQowBAeFlc8CNLi76lYj-7CkA3vLY-wI3yncyyylJF-V2HUB5MaIVPBopsBTG9fId22N5CiQPJ1Eif9UbbDa-KSExpmdJ38FvyI2LMLb2_-u990ljavvnd1WePkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da37587eed.mp4?token=PqFhcWd4M1XLzFSmj0nhytnaj9tPDaR3J-T00pNPqpnj-cIJ5iUM_1gdjjYY43iqyyy3cDf0kk4V8poQ3q1jx9_23dNWbZT4Kd90xa0raKhEug0lmEPktzejtCs7Wr0H2E5Flb6Jio9Ac8oKkKyukm_C_fp6dCdy-iHupVNuTvPi0LhxeTnXypBTRiOwv_ZQkkoYrgrX5auhxcBWccKeIulWT6sQowBAeFlc8CNLi76lYj-7CkA3vLY-wI3yncyyylJF-V2HUB5MaIVPBopsBTG9fId22N5CiQPJ1Eif9UbbDa-KSExpmdJ38FvyI2LMLb2_-u990ljavvnd1WePkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شاهزاده رضا پهلوی در گفتگو با رویترز:
«دخالت خارجی در ایران لازمه. این مداخله در واقع می‌تونه باعث بشه جان آدم‌های بیشتری نجات پیدا کنه؛ آدم‌هایی که در غیر این صورت ممکنه کشته بشن.
جایگاه من به‌عنوان رهبر دوره انتقال اینه که مقصد نهایی نیستم؛ من فقط پلی هستم برای رسیدن به اون مقصد.
برای اینکه بتونم نقش یه داور بی‌طرف رو داشته باشم، خودم رو وارد هیچ جناحی نمی‌کنم. نه طرفدار پادشاهی هستم، نه جمهوری.
وظیفه من اینه که مطمئن بشم یه بحث سالم شکل می‌گیره و در نهایت، این مردم هستن که تصمیم می‌گیرن چه نوع حکومتی رو برای آینده‌شون می‌خوان.»
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/68717" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68716">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/68716" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68715">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pScCYD3_0dU19LtQFKnaskGR9rpnr93Q2389UQkSfxJ71wSgnBNGlZfHQBA1XCO9v0D6YzWcGFBccfQhf4nR9hmKnDDgrLZqzdzHMXmiwoz4i2zO6VH8g99bme16oimDy_LwBvUyNddNlfOuqU06J-FlEU60rqg98OfT1fH3ScFQN2TR2QbcLC8K300aATtBoYGAxU3blieXUp1W37qQ-6wRjQjiJA2VvPMTErCRbK93Rc1liNmz-bn3tlo1008yA6P0EmBmhEOP_KaqLdETKS9Wf90np9kK0OGHFIk05P20Xa8pTv-JHHzA-aTcOqzgWEVnDMTgNZIjreQQ8D4tEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/68715" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68714">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHL300cIlVUaYCdNQVCb9e9LYYEABLRiXnnNjMqPfb6E6PTxZQnv3nIce7xKuRZJbKWXOAsMxkJk5OLEBD4btDsSRDBQMnJa_GmlGoy_Y6OFgMD7C89YwM_SAl5NYlAAfbAqfgBvOA5jzZvqPnX8lw1WbdLcNSIH2B8bLRrQpB1ir8oktP38Fghsjlpciga9-LN6NvaN4w0RQcbTGcnfj3N6weUbwq03Wv9ZL0LIZoweJiP2Kie9EJlaiE8vG2qfsnyxYw9Q1C8eg1JGNphDxSs8spqj9kO0dq9mztLdqCpEeWDvKL5oa8TS8yMgSTML7ETjAJ3fPe768K2sBbHHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مراد ویسی، عباس عراقچی رو فالو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/68714" target="_blank">📅 15:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68713">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه  @News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/68713" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68712">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=eJmPDgHZBCMx9G7AeoUWc73frcqpU7U6brkiG-PGcrn4VAoP1s2MOImKapnqrxkYRbINLdf87bEvia0j-A5sGcebw29CCPypZKXvIgcIhLMAtvImeLPe964apW6vr1Zx3PmQbXqQmppqkJ3VXdubbQ_fZKQiN8ejBdg5zg6jxtuyZNH1tGx8aAXB4JCTzsC89OeHB_OHEr-PDVO7sz7GMraNV-RrxRI68q2XWBBfGSiEnMGH6_NIrBGuSGighwsdFvGF3lhklLmM-GNAkD-M25YViw5n-bN5kweWBaNqgpT1PzeQh-TRt6iSp3nKHV3MN8OaDzc6w6sk_XpsYFIx_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=eJmPDgHZBCMx9G7AeoUWc73frcqpU7U6brkiG-PGcrn4VAoP1s2MOImKapnqrxkYRbINLdf87bEvia0j-A5sGcebw29CCPypZKXvIgcIhLMAtvImeLPe964apW6vr1Zx3PmQbXqQmppqkJ3VXdubbQ_fZKQiN8ejBdg5zg6jxtuyZNH1tGx8aAXB4JCTzsC89OeHB_OHEr-PDVO7sz7GMraNV-RrxRI68q2XWBBfGSiEnMGH6_NIrBGuSGighwsdFvGF3lhklLmM-GNAkD-M25YViw5n-bN5kweWBaNqgpT1PzeQh-TRt6iSp3nKHV3MN8OaDzc6w6sk_XpsYFIx_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/68712" target="_blank">📅 15:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68711">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7KFb5QCEDRQVWyFlyIgcOEGePjpKJ6dZwnFmpdG_ncMoFujLKKxSiAgU7cbrUPuzsq5xhtRSTovDkrDHOJrJRp40_1nBYtOOtiHxQjrf2gYKpLuv7DUK1Duef8vIEh3TISpPnKeeu_yXSqGbgz1MrLtL5m_ADV1GD9KlUOUU07sfeWa14XXziHCEJB8O-oE8qFtwuXxudfUMkRDj_RuX1qIMAiImNaJfppJPSJHwBZb1gZyNO28WdBJ4zAu8g-MhAkMPGoApdZYZpws_qLBXzEk5oQkVBnyFo-5h51xivCi3-X0Ot6SVQJbVDUD5uDWnLaa-Ez4Z2bFUJcfzjwoTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
با اعلام مقام‌های کویتی ،  چندین نیروگاه برق و تأسیسات آب‌شیرین‌کن این کشور در جریان حملات روز دوشنبه جمهوری اسلامی هدف قرار گرفته‌اند و دچار خسارات عمده‌ایی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/68711" target="_blank">📅 15:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68710">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=dv_cfGt8voO95_vmK_Mwrp4Tnr52g2k9tt42M5LlgVcY1sxf2eRa4OIVoS2bvxJZ9qlyo_wAlLCV8gtCeXa1E70XAgPy896xLP4_OohKBN2P5kw300Q-GM4bJTz0eLg_meeJPVpIcK-QPcsfin8MYcVFlxCSLTj0-gVnnzbt-AoQtvtCPJZNPOSCJvBuYUv4IW2WqpGlkjRvuA0fdGXTDjvUE9Kd586XNVSDn9H9TU_JFQRCQIi6j_YnlCQhwTc1lLm8W_jjCPS6Bu6Y-d1xbqp45D7Gw55xkg2BGh6TOGcNrTrdXTnmuCMRRYWwKOhp-coZtH-bSuU9a3SpU8LEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=dv_cfGt8voO95_vmK_Mwrp4Tnr52g2k9tt42M5LlgVcY1sxf2eRa4OIVoS2bvxJZ9qlyo_wAlLCV8gtCeXa1E70XAgPy896xLP4_OohKBN2P5kw300Q-GM4bJTz0eLg_meeJPVpIcK-QPcsfin8MYcVFlxCSLTj0-gVnnzbt-AoQtvtCPJZNPOSCJvBuYUv4IW2WqpGlkjRvuA0fdGXTDjvUE9Kd586XNVSDn9H9TU_JFQRCQIi6j_YnlCQhwTc1lLm8W_jjCPS6Bu6Y-d1xbqp45D7Gw55xkg2BGh6TOGcNrTrdXTnmuCMRRYWwKOhp-coZtH-bSuU9a3SpU8LEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ها؟
درست شنیدم؟
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/68710" target="_blank">📅 14:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68709">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
صداوسیما:
دقایقی قبل نقطه‌ای در ارتفاعات خرم‌آباد هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68709" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68708">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🇮🇱
وای‌نت:
مقامات ارشد اسرائیلی مدعی‌اند که تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
نخست‌وزیر اسرائیل قصد دارد این سفر را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تا زمانی که از قطعی شدن دیدار با ترامپ اطمینان حاصل نکند، به این سفر نخواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68708" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68707">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=rLOjsfMMFexY0VQ8_EgtOC3zCNzsypnmsrBerHrSOWw63q-Rz6sIyRG8POu0JX_CkqrxyuB6hcGfUeaDn4c0idC5m7WHZwPYHMbQv5XUllNwuYRZRWUSDJK2LI5yYC6ubZQCkjWTNPdxoZWTwAmee4zo3YPVnAEldKLS7I4kWg1T8eROnhOoZZ2URGOKaG8zpjm4tYzkRg1euTwkZc_Y4iKSz6Us3-dNFsvKs3CHYErWzOYWhMNXjzSQZ49MyC5zEMFnggfg3OqCPnttgO9AcXarPtgWTIGTiaxwG7pHkDjoKvOnnTjBfh4mZcTBjbVKDp9w3AbGDITmvxLmPAcJnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=rLOjsfMMFexY0VQ8_EgtOC3zCNzsypnmsrBerHrSOWw63q-Rz6sIyRG8POu0JX_CkqrxyuB6hcGfUeaDn4c0idC5m7WHZwPYHMbQv5XUllNwuYRZRWUSDJK2LI5yYC6ubZQCkjWTNPdxoZWTwAmee4zo3YPVnAEldKLS7I4kWg1T8eROnhOoZZ2URGOKaG8zpjm4tYzkRg1euTwkZc_Y4iKSz6Us3-dNFsvKs3CHYErWzOYWhMNXjzSQZ49MyC5zEMFnggfg3OqCPnttgO9AcXarPtgWTIGTiaxwG7pHkDjoKvOnnTjBfh4mZcTBjbVKDp9w3AbGDITmvxLmPAcJnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پاسخ دفتر شاهزاده رضا پهلوی به صحبت‌های عباس عراقچی درمورد توافق پهلوی با اسرائیل برای تجزیه ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68707" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68706">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=S0LdsmlX8yyt7kbpw7KRLiK8GaEbiLooZVWaV9e1fokr65GmBDqLwC7IPcqvhnVS9yAYouufSew2aYP3tE-O1GEs1SKTd2XKN4sTo-0H15BaToaObIdd8TmgvDbZft907KYexmpkZS5gEX34Oe7hcHKSImvjTedeIJ89pGeXyYufoFSfv3qiQaaqTM1MaiKJ8iNDcmblae80QJu_FMAkwqZZo08z8V5-9o07kOpwjg5ozhzKEbyD9akP1i1VAADgfhhNspZ1iJMxkjRzYW7S9P8eRX_hF0f7vJhtLslXkC4XNwFHrgqS4y4pr5Fq1huePs5YZ-aJKD4HaPwpcTpzuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=S0LdsmlX8yyt7kbpw7KRLiK8GaEbiLooZVWaV9e1fokr65GmBDqLwC7IPcqvhnVS9yAYouufSew2aYP3tE-O1GEs1SKTd2XKN4sTo-0H15BaToaObIdd8TmgvDbZft907KYexmpkZS5gEX34Oe7hcHKSImvjTedeIJ89pGeXyYufoFSfv3qiQaaqTM1MaiKJ8iNDcmblae80QJu_FMAkwqZZo08z8V5-9o07kOpwjg5ozhzKEbyD9akP1i1VAADgfhhNspZ1iJMxkjRzYW7S9P8eRX_hF0f7vJhtLslXkC4XNwFHrgqS4y4pr5Fq1huePs5YZ-aJKD4HaPwpcTpzuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب سنتکام به مراکز فرماندهی نظامی، توانایی‌های دریایی، سایت‌های پرتاب موشک و پهپاد و سیستم‌های دفاع هوایی جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68706" target="_blank">📅 12:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68704">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_63Sll41xy9ZJsfZZ_lkUBQbIii0I7PkiPMMzIcPE4tnONGLkAw0XAOtven772Yp7jPDX6w8ghHzOJC6Oy3V2LgyQPOrlE7rSU36Zz4Rgv1ra5sdc_6N0jDROEFR75nv7gsBdrfrpdE9o-tv8Vjo-isP9m0kGjPG80lT2aTOr1nleVYM77glPJTn-D2F2ByLBFm8UQcNxg8h6KuHA0oUO7nyIC9TdiSHQeVoixgXqjXITXQeqRDoglzyo3qT9JgNcfU9vcA9Rzx4DLF0miTKu_tZpS30OHYR_Py_3wme30ejorbnKOfKn95n6gaBlbSEPMxE1GERVdHeb3BdF9w8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYsjs4dZOeyCoZgSi4dx2WM88Ikr7zLw9dmvsFxf0ixksppXaW19fzZM_TQiJH8tROWUbzvTqneu8ynHpb4yEhnZMUkdvyYz9pgrQXgNZ9cKvOzwqTn-M3Az5rcaN_-KUmHxbbkIXWtgkFVZWHFZrlbmjXonne85Eic9vOv9TmeiKtebr4g5qxGcDrZpcP8OCPZGFswf6RJmffmAzUbDLgWzsBxxnMjPebpu9yLShfgrvYFr4CYSgvp1Cdzs_05lCUU6TM27R8IxLYLbaGXn85IDGD37wjZQ_Ua1Oyomx6UeHGlimO66I29DXvnsWUy-GXxMddXtgTmAnaC6q9vNWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دقایقی قبل سپاه از زنجان و همدان به سمت پایگاه آمریکا در اردن موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68704" target="_blank">📅 12:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68703">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6PD3-as8ywkMOEzELZf30vgirQK4BUlhj3evbNYzhwKrNtTAj3O3hm0xdW3032843Z5SbOgtu81i_tKBiLvEA7xXWCV9CRgQEeUKv-3D6bZLUxqsXhZVFRyN0nb6SD1XfZkj5cUoVOz3bR1Zt1OJSnO9QPGcTOgKcHyu8jk67cu4Yo5GZETDE90qG7zXNVNUpsGdhdaAwF39QmAj75YrT3tiBAPF2wwbF9mOpRD5EIrXVBEJ0PJDonYr1P3wdzD9lDdc6LehCfW-xIlkm0pm4Hghmgk_YLtVM6b2kFSdqpLz_odWdw9QxiV4EcZ9w_0GuymHG6i9DiU9mVmtRbSIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
در خصوص مناقشه با ایران، مقامات ارشد آمریکایی و اسرائیلی استدلال می‌کنند که تنها دو گزینه واقع‌بینانه پیش روی ترامپ وجود دارد:
پیگیری یک آتش‌بس ۱۰ روزه جدید با هدف بازگشایی تنگه هرمز
آغاز یک عملیات نظامی گسترده و جدید به همراه اسرائیل برای وادار کردن تهران به تسلیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68703" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68702">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⁉️
مقایسه ایران و نروژ:
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68702" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68701">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=uyqJPySNBW1IbcNXy6MZ7xg5kmPQka5zrcOd-5U5eofvl_Da9ZS8mZvZSiYCssU9lfAGUF2cPt67eVhhe_rQwdcdy7_LAm3rnYbT_p43NtX-3LcaI6C-eUePlmgtVieR3drgo2YzHrkeTeSqdRDv2GUSNYtzSkTJRosp2O78OgtaiqjoSYGAqf-z-g9zHpHfUeDLL9EY8_g8RPohmu8aB9JpMh5GuibveMLsGpeuNKu9YWC6oXDqdCI4MkVzU6Kcc4PrM51RMsdOiBSI_pmsLAxH4abOZ1SdlLngAH74sm2CzOQAijRoYGCFurJPjGXlrUVsLU8imxn6BL4r8mY4Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=uyqJPySNBW1IbcNXy6MZ7xg5kmPQka5zrcOd-5U5eofvl_Da9ZS8mZvZSiYCssU9lfAGUF2cPt67eVhhe_rQwdcdy7_LAm3rnYbT_p43NtX-3LcaI6C-eUePlmgtVieR3drgo2YzHrkeTeSqdRDv2GUSNYtzSkTJRosp2O78OgtaiqjoSYGAqf-z-g9zHpHfUeDLL9EY8_g8RPohmu8aB9JpMh5GuibveMLsGpeuNKu9YWC6oXDqdCI4MkVzU6Kcc4PrM51RMsdOiBSI_pmsLAxH4abOZ1SdlLngAH74sm2CzOQAijRoYGCFurJPjGXlrUVsLU8imxn6BL4r8mY4Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
اگه پای آمریکا به بخشی از خاک کشور برسه، منطقِ جنگ اینه‌ که اون منطقه رو هم بزنیم و هدف قرار بدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68701" target="_blank">📅 10:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68700">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=FBdPiLRbpCfRLZgMhVfR2Y3u-zN5BOzlFRvfgWzfJgmguGRvE45qynkjcR691SUjmryRuwXDxRN4i7j0cz7JPSwiPANH3dBD4nUfdJ8z-zbXK9DoNRFkc6-Ja4TRfvrc1SlcBJBM26ZAbuPf_frmePaXvSn3DVwhYk2SQHzJE1aMx4y5gxI9_1dLVlZegKJSD5l0ygBsbN9eeDE0nPP5uR23T69bN5zuZn9vVyaRZvCeYeCOAm1Czo1TBffyfX_acey6OGzyLgoet3sX695asMWgiKhFTv8k7QLpd5X2hTbcn20QU7RmBlDBtk8dI6Z_8o46kowLXMyCpgeAz1U0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=FBdPiLRbpCfRLZgMhVfR2Y3u-zN5BOzlFRvfgWzfJgmguGRvE45qynkjcR691SUjmryRuwXDxRN4i7j0cz7JPSwiPANH3dBD4nUfdJ8z-zbXK9DoNRFkc6-Ja4TRfvrc1SlcBJBM26ZAbuPf_frmePaXvSn3DVwhYk2SQHzJE1aMx4y5gxI9_1dLVlZegKJSD5l0ygBsbN9eeDE0nPP5uR23T69bN5zuZn9vVyaRZvCeYeCOAm1Czo1TBffyfX_acey6OGzyLgoet3sX695asMWgiKhFTv8k7QLpd5X2hTbcn20QU7RmBlDBtk8dI6Z_8o46kowLXMyCpgeAz1U0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال ۲۰۰۵، نیروی دریایی آمریکا ناو هواپیمابر USS America را هفته‌ها زیر شدیدترین آزمایش‌های انفجاری قرار داد؛ انفجارهایی که حملات اژدر، مین دریایی و آسیب‌های واقعی میدان نبرد را شبیه‌سازی می‌کردند.
هدف یک چیز بود:
فهمیدن اینکه یک ناو هواپیمابر تا کجا مقاومت می‌کند، چگونه آسیب می‌بیند و در نهایت چگونه غرق می‌شود.
این ناو بعد از حدود 4هفته آزمایش با انفجار های کنترل‌شده و بررسی مقاومت سازه در14مه2005 عمدا در اقیانوس اطلس غرق شد.
نتایج این آزمایش بعدها در طراحی و افزایش مقاومت نسل جدید ناوهای هواپیمابر آمریکا به کار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68700" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68699">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=gQ-ynXZRynUYBJo-nTcTVBTjrQd6Ftmu4WzsZncrhLGyEydFRnswCAbgB6o5rdaboIn2-L0rN6ae7csqaNzuCNbv7I27tvxg8EVY0SFBn_0pNlPy8-j787wvh-KcZC699uQvOVQc5bSOiiUTzmmB6ARTiYPxrPT3fJPy_uXqRm94cEO-KkUcETdlkrKHTYZMCYpVwhVzlqY7NjIXbFWCfK_FXpsRW34ilt9ZbHrmsFWwZ9xOg69_BL3oEAi4rMihu8vvbugZpILo053xLE26ZL7cdY8pgukA1LFanDtYmrN0bMaR5Hs7ixpH-Tj37cBBInQ4imhYc3Hzh1yROEWKPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=gQ-ynXZRynUYBJo-nTcTVBTjrQd6Ftmu4WzsZncrhLGyEydFRnswCAbgB6o5rdaboIn2-L0rN6ae7csqaNzuCNbv7I27tvxg8EVY0SFBn_0pNlPy8-j787wvh-KcZC699uQvOVQc5bSOiiUTzmmB6ARTiYPxrPT3fJPy_uXqRm94cEO-KkUcETdlkrKHTYZMCYpVwhVzlqY7NjIXbFWCfK_FXpsRW34ilt9ZbHrmsFWwZ9xOg69_BL3oEAi4rMihu8vvbugZpILo053xLE26ZL7cdY8pgukA1LFanDtYmrN0bMaR5Hs7ixpH-Tj37cBBInQ4imhYc3Hzh1yROEWKPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
موگویی:
تونل رفتی؟یه تونل تهِ پیروزیه ، اون یکی هم بالای دربنده ، فرمانده‌ها توی این دوتا تونل زیاد میرن میان!
🇮🇷
عراقچی :
حالا
کونده‌‌خان
انقدر دقیق نگو شاید دوباره جنگ شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68699" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68698">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68698" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68697">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlQeXOvwF42RZ_hdorBVABhrPAhoVnJ2vvyyOhXkdzJZF8oXxNr9pUOZtmxvUH-JyJteq1FPmZtmYGPu5lt7w5LH8SqFUzSzn7HEuOS4te3hYV2aR-qDt6NIxlLBqH7joJIDrjyweM_jDPnQveXxkHfj6DU9Jvf0k8e717KKbypTNsRAlHnHL-eQvBAbygw6btIBPTPkH6rUN9sASv9-cE3SL8Vv9BZSVMlA1AtZvxDAXLQqFeTXTI4pp3oXEJB0YSknUigJe3O1CYRJaOqP9D82YYCS-SHsEROo6hLuwl2nsGl1ZRFo0U5zXqJjEOlCI2DoI70YNd_pAQTXBU2uFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68697" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68696">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5OwyhQOJU1ATH28YkE2x026pcF4W4wDpNlzfO3V8PDh8-gtt_hLqRuaHP8gqdnxbIaDTq0uz4_iHVYCwuam8CmjW5uGCBbhSoRi3b_hGzW1Ov4LxMJkOI-7oH8wlG8AuNaWUuMknxE5C2GBZTxwOiA0XU5Vw6YS_PVdwbY-LNyqiq0KTAtGJ6RCphbrNrMb5tpf0gbv7myLM12m_OlPMDFGAlhi-quR3sWj4VIVpLzvO2YROPIYYDTJotKeKFhdp1xcD3YimFZ8BWfAIGUNfE5I9BiEGDtHkepobgT5jhgos1y_6wG-Gqx5kWRJD672wGATYfpWSQ_cz-9Wx3Revg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68696" target="_blank">📅 02:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68694">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_0rdRA-SVbYMGzJwJN9_SYaGtOpmlfQbmyj6llUFGGymjZ_94_vHWC2x5kvzP6QR0ez0x8hvVZ3t1UE1boJPgMsqN5wYoZwWVibWGXosKSyYOlOXNW375dtmZmr9bSnd5tpZQqaC2bD-ldjavq4c72NLHbMdHmbyfXhrju-_1BD5F-qmoeDGRxF7UuVBtDsHCHS2_FZMwPFhvHdkInUvXCm99NNY9YxfCGOPvLh6H4epVasc8HTpVhTt_qsqy982LVOLBCnWqQoNi8K5VXu8ClapiZmTuJqTXJ9ga-kLh5nHXoeabNrZXmS3rcfGof3jY8qYrCQc2Xqvu8f2-q30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ:
"من گفتگوی بسیار خوبی با نخست وزیر جدید بریتانیا، اندی برنهام، داشتم.
ما در مورد موضوعات زیادی از جمله روابط برجسته‌ای که با بریتانیا داشته‌ایم، بحث کردیم.
ما در آینده‌ای نه چندان دور برای موضوعات مورد علاقه مشترک دیدار خواهیم کرد.
نخست وزیر کار بزرگی پیش رو دارد، اما او قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا برای کمک آنجا خواهد بود!
ما در مورد نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌زدایی تنگه هرمز و بسیاری از موضوعات دیگر صحبت کردیم.
تماس تلفنی جالب بود و خیلی خوب پیش رفت. من برای نخست وزیر برنهام آرزوی موفقیت و پیروزی دارم! رئیس جمهور دونالد جی. ترامپ"
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68694" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68693">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
پایگاه هوایی بندرعباس رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68693" target="_blank">📅 01:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68692">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
دو انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68692" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68691">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrACnqdNTlEzsFp0ksIWA6fwsCq2ZiJgO_24XJD_zeYTuD-Zk9aOUOpJhny8hMdD8zF4_uAszLDSq_zKkmfEhKMolwBM2ypFB5AuUiAjrKTdV6eYRhSzdvoaQgmFYvoFHkAuyXDIbm-XUGyxCenOEFBYPiOoRuWlr0kTTsg5943p7mvXfMxlwcmQDk6L6m96o8RG0FbB5i7Wh_HHCejTeVU714h0fvddoaB7df5cef903w995B1aNt_hF5TaBrKJvraZK-1x-B1_ZeHXEVdXSfSHMgKbWqlLm9tyt1oPgJQgOMa2ZUScmFx19bcPIuuvaAPyFybt8cVdgfWYmUWPlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان تجارت دریایی بریتانیا (UKMTO):
یک حادثه در ۸ مایل دریایی شمال شرق LIMAH، عمان گزارش شده است. UKMTO گزارش‌های متعددی دریافت کرده است مبنی بر اینکه یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده که مورد اصابت یک شیء ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68691" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68690">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
مجدد انفجار در بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68690" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68686">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JgeuJL4Bs-fhsbnO0uvFkuu8qCRB0raIsQ4nz_o6lsrgLggJVaG-poQZo6AFWtryWDynhszvWCrhWzz6uAADIC-tkKHFCAPwf-mBfV7csCSRvxogvC3Sbwx8tOuqB8qYBzw4neXkw3mE0LEzYqXDxkPrXlBd4a6wA0okXttZGQtdxaJCblWw4BFpxXX3_1_v1WvFJwhfjUX5-A4HpH_zhzsmjjt2I3aoHfZonJYrcingddsGHoTuugONwCJ2oXufgWPMD78KfkXukma_IXnLakNuGFP0Q1_Is6AHsMCshVfcJvYWMTLqqAJ5HqdljKovSaehdN0QDNYv2Te4Yo1Emw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PWD34dJGGfZwyJwlN1LTMpbgisgUZ3WRdkmA-sB3nRmWNMzyxRLXNusAytkecHeDdQO9ivZ0W2txFxQxwRLwKvffHrbuB-w-clxoP5sf6YHUBhf_zJoa7Z-AJY_CixlZddT5S2FuKwjo5Zx4foUyfioVq_NlSBuaCudoU6F-4UciPkqM1xmAjgy4nHkUNMzWbCLYlgwvyjnDQvnak-h0am5KUAxFPy9fCMfGf5X_NeMOKk_aPipYysJQJpQGIyhsQ28K636VI0bqvAhkMTNaJ_A8m3y8JFfCqMzJFoInzXPkU0XdkCkhi97uBAwWF7DlQ4u_hjLcMxcLx--isGI1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kAeF9KByj48iy-5OEmQY8os2NaHtilIxewUajIzYyIwu0paExwpZ-4mV6GqL7HSwGLTEQ73FB1GjBK1Ln9YABBLUIoI4WCleCxj-DwsVYoNLv7gUokr0eJNKK4G_1pycpV1D7s4EWPuqfgOzQFEPEpEn0F4Z_6nUSOYPVxzVd1KzXR6aPTEPyPehw8Kw4AWo_Pokb4sIINBzAt1M-Ae_7Dzkhf67Z2A1wjokgsCVLM5p99EzLEKHlDJ0PpCqkY8W2y76W0VElSIho2qdgjNHhsSls9E4LI2KMNI8ZmQUnPj3WMqRkYeVtNMA5Napgog6WFZJD-pgcmBjkIFYS9Qsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/juNDBaxb5jFu3c3bdmSM3QkKjSab1FBqVz3HL4feKGtCWfJq0jLbVN3ceiFZB4SLo4OieZ2eHtwctwPBCA51Ali4z7IK6mw_hHHAsh-EnBpnAZEowmmutrxL_NxzborDhOY0qtAILBdafOc6IUmAtIBIXwijN2npHet_Por1QCYGPcIw9Z7mK5I-4WVpRqWyaEs403wS2dTnyA-cEhfcVQNBJKotALY1BiHOLUqK-AQl55bI1CmLyMchfpmsbpyYBfUO-uHXiPPlA-IlcxzBz4BTbnfzAT-PDX1rOWAwOD-R1oU-xWeegXTsSjxvK_1MgP3XhFo3JHUr_FGGqBhgBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز زدن
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68686" target="_blank">📅 01:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68685">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=UI9OOrzKPr1ExbJ3eT6vwYcih1pfmsXiwrEmzT86Zg0172f7aHo9pT4Oe6ziWVohbosNJFK6-_Xdty3x783g6MAVT59ucuVCT-MC6OPgauWL9hWifKDql5TVSNqnzOG3K9Hfubn8wnfA6cUCnJOCBRckIcNlcoYlezxRZLFnpVVuMRSZ2PrGJ8OCm2-xqly--Z5j4oswRktz229QsDfa-qojjAdIa-k2pTd9gaQOpTGokyLTZc74RZv_IAGlipgm7lvC-SBO10InZOJfw7wFgXRTUNH3AbCeRy-N3WLi9dVNbeZsz6wl85QJWhQ_rMzHO20kJp1okpOSZuOesqdDgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=UI9OOrzKPr1ExbJ3eT6vwYcih1pfmsXiwrEmzT86Zg0172f7aHo9pT4Oe6ziWVohbosNJFK6-_Xdty3x783g6MAVT59ucuVCT-MC6OPgauWL9hWifKDql5TVSNqnzOG3K9Hfubn8wnfA6cUCnJOCBRckIcNlcoYlezxRZLFnpVVuMRSZ2PrGJ8OCm2-xqly--Z5j4oswRktz229QsDfa-qojjAdIa-k2pTd9gaQOpTGokyLTZc74RZv_IAGlipgm7lvC-SBO10InZOJfw7wFgXRTUNH3AbCeRy-N3WLi9dVNbeZsz6wl85QJWhQ_rMzHO20kJp1okpOSZuOesqdDgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فعالیت پدافند در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68685" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68684">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbhEaWmZW-ofzYz5KaKj-NrdGoxpIhnh2HMo0FD-iFDFnsCuW5KO0zOhuwNEcMX4PH-sXPfbQj02hbzfOBUU19GSlFWDTjNpVQLwFqf7b4I7HdKHmdpfN7Arbf5mAo22At5_lhTun7y-TIT2X2u5A8TOVbmXshBdlzDLC7G3cfv7o7C_zZVtPyemDR9t7kGtmq8EfnUcVUMvYqFiof-vVg39LLj5vR-yDqaWih_aBFzrlMNYMIcLT13vJXWbVKtNs5tZZAXgWI7wnE5JzzcnxsyJUeWtQuRcydMzh3rsSEzGR-iVjyjzxEuteUkqH1MLA0OOq5X6Leqldgf_cRPCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیر ها در کویت به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68684" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68683">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=f9MQ90HBaqVIAX5-_exdy_2GfPoPe87WV26hKU7dRSg3hGf6WMtdyp0qJQJxW4VW7cWmSeu8huKeDzcKOGmTFIHcwQqddXYODIP8TOpprPalsQCkTpXrvwVyRhWOwllrzxfgsHSIJqEDBE85-rDQs1y-ztbn3zo_L8GzzM7BVo3cs0e1njODuvd33igmJ9VuE8JUPdw7Qoims-FHCRgFkSjuIsydossgg4BbGYqs-Wzs93u0LVZYVas1_gUKg1uKdxW-o6-G_Z7YGMqtzT3DiUwhf-GLS43M2VeEHIbyXnFiJtBpDln-NZbFPeV0YD8comSGSevcd6XUPB9_GmGC_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=f9MQ90HBaqVIAX5-_exdy_2GfPoPe87WV26hKU7dRSg3hGf6WMtdyp0qJQJxW4VW7cWmSeu8huKeDzcKOGmTFIHcwQqddXYODIP8TOpprPalsQCkTpXrvwVyRhWOwllrzxfgsHSIJqEDBE85-rDQs1y-ztbn3zo_L8GzzM7BVo3cs0e1njODuvd33igmJ9VuE8JUPdw7Qoims-FHCRgFkSjuIsydossgg4BbGYqs-Wzs93u0LVZYVas1_gUKg1uKdxW-o6-G_Z7YGMqtzT3DiUwhf-GLS43M2VeEHIbyXnFiJtBpDln-NZbFPeV0YD8comSGSevcd6XUPB9_GmGC_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68683" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68682">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
مجدد بندرعباس و بندرلنگه انفجار رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68682" target="_blank">📅 00:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68681">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
انفجار در اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68681" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68680">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
انفجار شدید در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68680" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68678">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45723674d.mp4?token=hY_UeHyyr6cGW4CY5pS6qqU1vmf8XfVMA4FBvdyNL6EBvhpG4JrdEaoSACXXLwUdqUXFtasRoSJQk66foeyq450qh8snmk-LPWoK9X_JP_3GLMnldxOPKHMRJxdc-iLVcxtlrLOneJYnySKDcPhoigtRN6JiqYkgaw9ZmLnYccCkafoEKaYnX-kLmaxFKtihJJ2jcONI0TLMGgcABLVEBJc8ELMt-WnvFrlwYRlDr-DNAb5FdxBfwKgma5CgRwdRBP8aTteldXkqjdxGB94UDAiqvC6cg6pHmcbgQNAFzw0Rn6cZtwJl2hUWzcTr-WEEa3JSaLlhfTg-qNhbqZB8uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45723674d.mp4?token=hY_UeHyyr6cGW4CY5pS6qqU1vmf8XfVMA4FBvdyNL6EBvhpG4JrdEaoSACXXLwUdqUXFtasRoSJQk66foeyq450qh8snmk-LPWoK9X_JP_3GLMnldxOPKHMRJxdc-iLVcxtlrLOneJYnySKDcPhoigtRN6JiqYkgaw9ZmLnYccCkafoEKaYnX-kLmaxFKtihJJ2jcONI0TLMGgcABLVEBJc8ELMt-WnvFrlwYRlDr-DNAb5FdxBfwKgma5CgRwdRBP8aTteldXkqjdxGB94UDAiqvC6cg6pHmcbgQNAFzw0Rn6cZtwJl2hUWzcTr-WEEa3JSaLlhfTg-qNhbqZB8uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68678" target="_blank">📅 00:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68677">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
ایرنا:
در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68677" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68676">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امشب دهمین شب حملات به جنوبه، اگه این حملات یکسال طول بکشه، هیچ مسئولی حتی آخ هم نمی‌گه، چون اینا با حرومزاده هاشون راحت تو پنت‌هاوس‌شون دراز کشیدن و می‌دونن کشته نمی‌شن، پس تهش میان می‌گن چند تا #پرتابه بوده، دوای درد اینا همون مردیه که الان تو اورشلیم نشسته،…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68676" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68675">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
انفجار در بخش بمانی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68675" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68674">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
سنت‌کام:  دور جدیدی از حملات به ایران آغاز شد.  @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68674" target="_blank">📅 00:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68673">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68673" target="_blank">📅 00:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68672">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68672" target="_blank">📅 00:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68671">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE1vziJekvvz4JK2yp2jevFklpCJ3EiDREIcB5t3ptM9F4JS-e3JpGsOiFq67Q1yCaQNlfBHe9zeehGilDCOjRVKzcRlNDfnoqV8LxGzMsXOCbD4eccNNlg3PIA2dn1rRYT4lt8XHBFWZHESK8REarn0zcX5rDVBHlhjepLdUijDtYayc4od3tV9ytaqeN_uklXi5kWodv0Ad4hk8hrEj4Dh_TcyQJr3PAoCilfsxzYiUScOXfASi6ZkeefAv8ZPT3M0o2QVA585FCESp_ZaWrUFVorZqMtwZVkCoRroLbk25nSnq5H1wbzmZyZLx72guZn-zt9m8fa1DIHI96zxmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنت‌کام:
دور جدیدی از حملات به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68671" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68669">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
گزارش‌ها از آغاز حملات به چابهار، قشم و بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68669" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68668">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e80MKZKeHCORRbBTXi4y1N73dBCdYmNx9TUlCPK0i7f98slBj0Nh90Nf7kTWO_5flesd8jpAPNRxNg2zQpPvCdCW9KuI3WcVL2S3JxskSHa973P9gD0Kyz8a8bzk6WkUMxMKq_U6Ji8M85AeZmpHlvxTJlq27fplRpiqAnhrmnTmGz4ndj22faNwDn8a8QGzd2eYIlzeZFXHy1qvrsDFQo67HWA3Hnhp9DU96X-yrj6kcOS4PQ6ZVKDUUipZYvbh60BfQm4zlRchYHipzp0pzBi4hDL2ZK-7PhF8Ng007c6z1TllM5IwFRKaB6k4lxnk6RfFpdN9co8LkFzO_RqzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68668" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68667">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdBS1kD3MVYbJ8sUIGVq2vs7ZxImy6d-Ggi-iYzvIbAEXMKQt00MA-LJCNjSEs8sn7nkcZe-Vgh0q2Juo6lAzaLKb50_JPvopjesio0nhVIgbPpZDRIJpe9HkzyuibVtsTs4377uUshapyGNlm_JlVYqDiH8Ds8KemmnhsUCGCzm58h_Gyey5cmhpTOzzs_Buoh7jhcdSY5JyBd-r_nP-bD4_8Ab3rGhcCVmWtODN0rw3ur2Lw9zBFlgCR2vopBOm2kUJtx4txFm6yOYjxleqIMjvYYTSXsTAJz3lktaxQg8T29R-91-6Eb9uuuFOfT1oszNRU1mvn99Kk0dBvGf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
«در حال حاضر، تمرکز رئیس‌جمهور ترامپ بر این است که ایران را بابت نقض تفاهم‌نامه (MOU) و اقدامات تروریستی مداومش در تنگه هرمز،پاسخگو کند.
به‌علاوه رئیس‌جمهور، ایران را بابت مرگ اخیر سربازان آمریکایی پاسخگو خواهد کرد و هزینه آن را از این کشور خواهد ستاند.
این ضربات سنگین تا زمانی که رئیس‌جمهور تصمیم دیگری بگیرد ادامه خواهد یافت، اما مذاکرات میان کشورهای ما همچنان در جریان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68667" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68666">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
دو انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68666" target="_blank">📅 23:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68665">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=o6xlBT5TsM-MklW4a010PDBHxiJZV2ePTGCtfiuoV145RbAxv564nJtGd7T4hQS3pwjgjBY_od953197y46zBhKLWb9v8dslvyj7ZHlNMLyQqiBicWBoxNM6TCCp0atgGopYs4TtUjWDjJAlLRiEFzlV6Qk1vl9v5Gf7ahJUmvMmE-f_Tx_Y4VozQ7uoLdsv8AuCuPgoOxgpjmMSJExAK8h-dRPyhXtHi15m08wu3xMbG-Q23HunZgyN-Qp4q4JCKVJ0atWf69W8UbKGbosPrLjS24RnfehGf2ng7NSv04scYBwkkLW4i4y9Lp-2ak6nk4QufiO3cGUC1ThLjJhS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=o6xlBT5TsM-MklW4a010PDBHxiJZV2ePTGCtfiuoV145RbAxv564nJtGd7T4hQS3pwjgjBY_od953197y46zBhKLWb9v8dslvyj7ZHlNMLyQqiBicWBoxNM6TCCp0atgGopYs4TtUjWDjJAlLRiEFzlV6Qk1vl9v5Gf7ahJUmvMmE-f_Tx_Y4VozQ7uoLdsv8AuCuPgoOxgpjmMSJExAK8h-dRPyhXtHi15m08wu3xMbG-Q23HunZgyN-Qp4q4JCKVJ0atWf69W8UbKGbosPrLjS24RnfehGf2ng7NSv04scYBwkkLW4i4y9Lp-2ak6nk4QufiO3cGUC1ThLjJhS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یه برنامه اینترنتی، به ایمان صفا (بازیگر) یه جایزه 12-13 سانتی دادن؛
مجریه میگه اینم یه هدیه کوچیک از طرف ما که به ایمان صفا برمی‌خوره و میگه بخدا این کوچیک نیست ، اعتماد به نفس ما رو خراب نکن...
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68665" target="_blank">📅 23:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68664">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeOLk4h7z1dudYB3MhZlkenZEwVPqH1I1aJBO5E4iK8zyPm_Y__clpZkyncpVRW_-s9SXDVaIEuOFsyTraqX9b6nYSxaax3gudsmy9lkQUcZPA5ncxwi8lYHrftHUhEQqDYkNBBPeW490gckIaWELvktav_NDOR9GIfjOH8mSiq5Ywnv8SHgLSZPgYuDRyA4ZzGXdjKH0afRepbTDUrDzJ4PbVOQ1XPXfMzUoO86cJAA2oLxCuIi-umD4yy2bsA75ULYX6KsdFxZrG2o1wlWyBb4tGoj2hflrg1IV59p_srWqlQ2Wp3Qcnpt9hFkavGc65lYOxbYsZ40k1ZjdxLUNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
گزارش وقوع حادثه‌ای در فاصله ۱۷ مایل دریایی شرق دبا در امارات
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68664" target="_blank">📅 22:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68663">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
رسانهi24:
آمریکا برای مرحله بعدی کارزار علیه جمهوری اسلامی در حال آماده شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68663" target="_blank">📅 22:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68662">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675435558d.mp4?token=gBixm-Ppb268dzmIUEQI9KYWp2P091_Mxk_tgXVPmGnLPttvRBJTa527PP7Ekr1KDCs4pl19C7KYjLFZn_eo5K4jVfr-nw3V5kP0VbKmVpFCpUosQ8PGYxAb7WpAShvVJLkuZ7fiz8rr3z7mpvIh3L16ywR4ioNiNhbGslmOKtv2h2_nXkYtURb185fLvJTh1unGEVU83LADI3QhPAJO_jhjwglexY0yLRDXgfuoOwCj0V9em7i-paqb6cHdC0KJpQrruhX3WlsksVVyGSkFfnyCBSzSwemNbAWoHibB-2wGmlWIgNB75dT50aH6C10lXc5u5ZSp4GGwzwEp-64_Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675435558d.mp4?token=gBixm-Ppb268dzmIUEQI9KYWp2P091_Mxk_tgXVPmGnLPttvRBJTa527PP7Ekr1KDCs4pl19C7KYjLFZn_eo5K4jVfr-nw3V5kP0VbKmVpFCpUosQ8PGYxAb7WpAShvVJLkuZ7fiz8rr3z7mpvIh3L16ywR4ioNiNhbGslmOKtv2h2_nXkYtURb185fLvJTh1unGEVU83LADI3QhPAJO_jhjwglexY0yLRDXgfuoOwCj0V9em7i-paqb6cHdC0KJpQrruhX3WlsksVVyGSkFfnyCBSzSwemNbAWoHibB-2wGmlWIgNB75dT50aH6C10lXc5u5ZSp4GGwzwEp-64_Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68662" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68661">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIOqlXIrzyOb_k4kWAkj303lnpwEgcgPaIQSkKx8mkOC0zOgGzXdkJW20sSxmtVCP8w36dIWuw3341T6jCDkpkTu_GJzufaVHEW-hAR98M1hlycIbiSrSuFtG1wRGSfsVOH1ErmfRhI0lXU9VFvACfIhR_du9upTxLQuOIjerDqV9TeFP1WHvZ9I9pioS_dYTHJFuG2mSVl0tLr0MnyJ4kCW68e5gsJAe1RiSwwxuMnxApi1bnfjD6Khjp56V7G5V01AVehH19DnjbCrSiOpBsvC8vRjnECru3v5UGGhuWDjTeqnATezdPKerp3l5pphyJbUFZF_S3h-wApQGVxMNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68661" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68660">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در تبریز؛احتمالا موشک شلیک کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68660" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68659">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
نایا رسانه عراقی وابسته به حکومت؛یک منبع در سپاه پاسداران انقلاب اسلامی، که نامش فاش نشد، اعلام کرد:
نیروهای زمینی ارتش ایران در نزدیکی مرز با کویت مستقر شده‌اند و به نظر می‌رسد که نیروهای مسلح ایران در ساعات آینده یک عملیات امنیتی زمینی به سمت کویت انجام خواهند داد.
تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده است، و نیروهای ویژه "صابرین" نیز در آنجا حضور دارند. این عملیات ممکن است در جزیره بوبیان انجام شود، جایی که موشک‌های آمریکایی از نوع ATCAM به سمت جمهوری اسلامی شلیک شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68659" target="_blank">📅 21:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68658">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJRVhBj_Vj66_gMbTxy4DJrKkL4y515OngU1Lk4I0oLQ8bAhCZiYBJ6q5uUgBG9iufs1E2zYgXeWyua7YfOz_CHg4M6Ih26Xki5h7t5hSqzk1ReY9bc1mgvAmqmYh0rzzzOYiHl7jkCTivWG1AeFtpnI2c_i2i2R1b8qCe1z9VvjEyy859cP5E6rXhW_wgX4pCXr5589gkfcbOMc6xY3vFzGM9ysC_OBcDsFm7xI8elnCFp1AT1Ppb6uEOdugcd5P_nwMxeqQkmeWNQaORju_bfVOfQQN-E6y09uOzB2dsjFtse8ykKX755KQYYQmsTtM0gyo1RpgQL7V1sEgIjRUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، توسط شهردار نیویورک، ممدانی، بازداشت نخواهد شد و «اتهامات» مطرح‌شده از سوی دیوان کیفری بین‌المللی علیه او را در خاک ایالات متحده، «باطل و بی‌اثر» خواند.
«بنیامین نتانیاهو در دوران حضورش در ایالات متحده آمریکا، به هیچ وجه و تحت هیچ شرایطی بازداشت نخواهد شد. او در حال مبارزه با جمهوری اسلامی ایران است؛ حکومتی که اخیراً ۵۲ هزار معترض بی‌گناه را به قتل رسانده و طی ۴۷ سال گذشته، سربازان آمریکایی و دیگران را کشته است.»
«تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این چرخه بی‌سابقه مرگ و ویرانی کشانده‌اند؛ مسئله‌ای که رؤسای جمهور پیشین باید سال‌ها پیش به آن رسیدگی می‌کردند!»
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68658" target="_blank">📅 20:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68657">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ8naELrX8XIE8AH9nedM6-nogfhUq9qtQduo2i8CCZ1LvHe1MD0gZTMyZjtYpa84vj_ybQSe9X-xZSdo3D2WD3DInPtFkV_XfVS5rNa-oLFaqv14ziK4_ROBGktAdmXpT6vKNzhuKAxP3OMFcjNbsJRGsytFVybTGrU-SbNOSKLcJZomEF1-IO0-6XWRWwZ5M5_zLDoQl1iTnPZGi65QKkR_chVPUuxMljgpjMgztfAxTxxwEjY9M1dqYWKfYgxG-0qVT32wk7vq4ogmSLdCpzzYtO7hlP7XO052ZyD35Iw9oIAt9aeLPvBDV3w3GtlS-nfyOcWZMDf4T5siONi3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین و چند برابر خواهد پرداخت! این دستور به وزیر دفاع، پیت هگسث، رئیس ستاد مشترک ارتش، دنیل کین، و تمامی فرماندهان نظامی ابلاغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68657" target="_blank">📅 20:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68655">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DD5gxxlmSFLw9KAPQ_us-bbaxItCjyUi6aefdrSuEatMWMhEQSXSjjBAEcijUEi0_0ag5pue_0mdKjJ_qc7aincMHsGsrPKCr7ZV8wkodBi4AL4DfbdeC908tM0evfh2JSsxbUcAc3fGfcPR2ulJcONYGCDVvUjeFOAv1ZXqqktoGEyTSV_hI2aTDZNV9aOaVTmq7xxmbeu720e6ZtR3mDxFwdoPNfaU6Abc_DHotEkN89y3KwS-07e5Qj46-SAtGCRzKVkPJ6jJ5755IOaFnzxSWFSsNc8PA9mzpTWI929LwaMaQy0sK20eBrprGoHtY2eOT2B0Rc9Cpnz--r-z2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAIyFTZU3HYbUszYk-3-FKs5W8WhcCIMffRIY3bgHBtn9b6WFMrwOAGnhkfGGfT8E4Kg7zJ6I_rnrZSdIMQCGfY0-3TjIdt1tCrvZaOfbXA4Sti2JoKTtm7i0PLwdgmZf6mFLaVy5dXxJFi0yzDeogJNxe4n1iBumhWMKnn5GXPmdHlGoM4balCc-Kaj_va50nBkbfQvN6o8OiRt5oPcu--nfVyjhSZY2HLnLbl8auJf9IfxRoxYoVPvknNj8IQgsoplVkUsmMzmDAnSciq5wgTDAj1iOXH4U06NLtDhaSjx1oNWHlB1mQo7cifOTQBTA97SmOsXgxCXjAh_zo337Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
وزارت دفاع ایالات متحده هویت دو نظامی آمریکایی را که در حمله موشکی بالستیک ایران به پایگاه هوایی «موفق سلطی» در اردن کشته شدند، اعلام کرد.
تایلر جیمز فیهان، ۲۵ ساله، اهل هاوایی
ایزابلا گونزالس، ۱۹ ساله، اهل تگزاس
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68655" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68654">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRWV3cii6ahNvxyTplOrRoK_86T2dhAftT1pnEbeCoiVaODcBNQmp-WEHqqL56zfmHrrqL8pCx54JLo3W9rvtyGLOgiCktZC-JNYx_JovrbjZBbI6szcmErDnJxYNJ_SRE7NPLlLairDVnn8DFOf0mXVeClEYl6h69LLOKiX56WBczUypPhPWTA3qqlOWe9CaI56AGUHuGE7THKpSr8X2Rja7OdyQ0Xg6szFHUcLyrzXEND_2VjzmlmJ8umpWadPvqRCm88VT0tPL9yfHwdkvNtB2BaleQ-dCD4vL6UZrHfFDfxIu8aGvdi3eyRYbIyEwGtKIAd7M6oLKJ_d2DMxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد :))
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68654" target="_blank">📅 20:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68653">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
یک واحد صنعتی در حومه شهر خمین حوالی ساعت19 هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68653" target="_blank">📅 19:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68651">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tplchBOqnGGjhmGv9_x4Nax-TRdwnqfeKipYUjGsGLs5iB0BMn_LmnEoCUCD_O5GUYv80utXH7DRWHpYXZDQFpiSi_RfgQNivNCtCQwEn_WXq5QOTTeiqGOyfOgvLLsJXP_Zyy_Qh5NMTOAO66KSwvSuAzT_WFgmIhvDLV0MDn2_zGHOZbEXz_1Hk0U6GqL6pSdPVc1Fy-EoNyCdPkREzu5y2pm_stexcg07nl0as89anG-Wj21fNPrLd1G7X2FbOYunQVIRD6qEEfV7UgqIIH6pp3_vvwlnWBAhmL80mmwO-20PKZ366N3jVoOOokUmq6pQs9ouos1fSgJC9VQyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=k4BJMXKmmdr4PdWdCK00-PaKRvEQMUcTIwYe1OcDPDv-1Nj_MU1mhhsYPCq_fi3N79y9xrI2eixZlvO6MlGXZCByFrDqUymBTxednAf_-LY9nCv_Te_IpUE5siYAv4sp-RUXn2jKxI4SsWVed9klp1QSRI210xWQ3swu4FG2tnVt5CR19CUNf_hfyDUH1zW3rvenmw9LjH0ip1uOdeTAxThbqkKRzvWUd09QJ19QEWOCM5ivHHKTtHTt2TKpjDGnpMPWZFN44D63Z-viYCMPHZockmUe2QwqOpoiVIJq2ia_NhPKELU-Lq3xEQkMSkyzYXY3nvuh2RQvW8OhdOYXsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=k4BJMXKmmdr4PdWdCK00-PaKRvEQMUcTIwYe1OcDPDv-1Nj_MU1mhhsYPCq_fi3N79y9xrI2eixZlvO6MlGXZCByFrDqUymBTxednAf_-LY9nCv_Te_IpUE5siYAv4sp-RUXn2jKxI4SsWVed9klp1QSRI210xWQ3swu4FG2tnVt5CR19CUNf_hfyDUH1zW3rvenmw9LjH0ip1uOdeTAxThbqkKRzvWUd09QJ19QEWOCM5ivHHKTtHTt2TKpjDGnpMPWZFN44D63Z-viYCMPHZockmUe2QwqOpoiVIJq2ia_NhPKELU-Lq3xEQkMSkyzYXY3nvuh2RQvW8OhdOYXsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
دقایقی قبل شلیک موشک‌های بالستیک به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68651" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68649">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU421ZxWLIRNlztt_QZqH7rvYlonoR3T7w9gSTGyeP-dqJMjN_IfUnHAsG3K4pFpyNcrK1EoxGgC-tiYcPo0KhZE_A7kZle6VAoYv9Vv4OeL4EOK1iMl7-LJwU338FAAXHZcwwMoQy1rWUTRxskKFHXJVtbpkDIA-0NHp670-IQ5PMwZmlnJoS40ZLQ286y5GlohmlFLxahxTGvyt7i-CRFszYHtwpM8l6wUd1csNS_tIP1pu95ElzdClOG6jkrorJhbDNmlKsHtxH-TT3_7tlJ-81SjnyYJh4aO3zDNIOmKFY2OU1Jxf0uRchyZ5aPlQCqzn8u7yMcFQXBuN-yAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=u01lX4c1kpL2bfImhFPKsAiuibKkVFUM63ii4MoWqOscCEbTdkCjzVDlkLyHwhMXWNAaSX2LRlOefu5_-CtdHmEFrzHQJzw0Ou37T166R2BNQShjYNis7O-9lCrcHG6X0FGFK-UvlAukw4veRzCxOvrWIemgIW4vOE4-qZbEbaXVmhdiV0iKaqo9tG8aNAtCNKG9YVkFWm665D6sPgnddn0OpO9FVpcCllTptNmMhJiMJ2puJKaiRBnCZ533BoW0I_uhrLLum4o3Rhly-BnbvAa_d9JwPkXyzaa4tjgc7EAbrTo_UbTCv0e96lmIercZEgHYpn7gGYkEBW5AZI7U6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=u01lX4c1kpL2bfImhFPKsAiuibKkVFUM63ii4MoWqOscCEbTdkCjzVDlkLyHwhMXWNAaSX2LRlOefu5_-CtdHmEFrzHQJzw0Ou37T166R2BNQShjYNis7O-9lCrcHG6X0FGFK-UvlAukw4veRzCxOvrWIemgIW4vOE4-qZbEbaXVmhdiV0iKaqo9tG8aNAtCNKG9YVkFWm665D6sPgnddn0OpO9FVpcCllTptNmMhJiMJ2puJKaiRBnCZ533BoW0I_uhrLLum4o3Rhly-BnbvAa_d9JwPkXyzaa4tjgc7EAbrTo_UbTCv0e96lmIercZEgHYpn7gGYkEBW5AZI7U6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی در یک تانکر نفتی در تنگه هرمز، پس از هدف قرار گرفتن آن توسط نیروی دریایی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68649" target="_blank">📅 18:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68646">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMjCekOdh6UpXDro0DDOAifUNRTxpZwVUl4l6pPpxQxanLl-EjqbBARTCyqsh0_QZWlEAbw9DBZj0N8RMHwK927Q0G8Hh5Wc7VxnR_Pg4UsUv-qk6uZbmk3MH0jPRd2LBN_OzK7PdyBYQyOF7_BgxXK2W52ZOpbxEf5t_k1TZzhHTocVXMrbtNXutvwGYXX9LnKoG-wa2yA035zQtr4oeFEIwbGp_UVdFmdxV6M2JQosZmBi9efLOPkdOxH5qnMp7Vx1OdW1ZAbrJUFryZ2Iw9xYI7f8AhWcGn_jizmbBDzy1nNxnxQeNEtFgvoDDjXoHWW1s7frsuLie1J5pDG1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVdjyWefRYUmD8ce5NMswW5sGU_9qwUskY7IVFUaK6-mKWeXtlZZ48ATbRLSSvrFMoOzW_gNLcoO4Nh-4hIXbCSr-5ij5An7J3N5FAVDdbuIbyCnqNqoXIhE4CWaojtvk7ZbKHIGS82VPiBhJlo6e0iWW5DeKD5QK7dhHiR0QfZUo1y3_YaoiGtfEL0cZDmJcitbqka5gyeCk8IvC3GzPeJvWI6_59qDBT9Tm3_lS2blqrHxNChiMHEqTAs04ErjVKkRQQZjesX5wEe5yi935GnXWI-z_MV3BWEn_IqaWdm00rL1ZmK4N7wm1sDelXMXK-Kpsce8YptFebDPinNycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFO3GarYAqCTFoGYI4E_wXEY1HidpdfU5uUtwoBu6cnJ2v7ZHOneM_xBBZsr2Chje8pL2M_IECJGqsCsoztu8Y2-zEumorzRbnckt3fRgEYwlwE4_5JY-irMjJdc-MgaM23o5nXzsTePjqDeFkMhcvBQhjRKhfTDOBj7jylBtMeu2mG0W2hTkmIACCYsG-5jnrOPx1TJlA8Yc3DZ1u58OZz3zrm7ssuwMdsdn46LNlkx9jtonRum9mktEaoorPpMFrJ4DkkuwU2iMxNw2CMFlSJMJFje8OlRnBzi2W_Uivnef7qhHQcoM-671tACoDS9bt6zbbYT_rJzCcIEPx7Tdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
شلیک موشک از شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68646" target="_blank">📅 18:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68645">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68645" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68644">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLl3YP5_mPgc9-SUkVsB8PhjuXRp5g6DP716KCqW6tHcmFm2H8_h14x7DyZXtWX7-f_tXi4q6DA2oYMNFHmPsU4jvMduDaAachvXsd8jl3tcuC8P_VYky8B88xFAFvhVB-KcxvseaX8xFxc3YsOAzNqX_vWVZY81XVI2DFl-q9hUop_PiCZ35B3sx4gdsOPgSBqF3EVOcoebO0q-brJ-8nmjEmwwxBdsr3s2TzwEr7L3ZivSzepJDfQELILixjrIWFTpM-RVGRyr8F2_qLtLpMVZSETn8Yck2dKzG9bvArwYnA-__xut2rRfDn5-_-1fx7n0caJijCOBIxgwKGo3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68644" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68643">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
❌
رویترز به نقل از سازمان عملیات تجارت دریایی بریتانیا:
یک کشتی باری یونانی پس از اصابت یک پرتابه ناشناس در نزدیکی تنگه هرمز، آتش گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68643" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68642">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=VjFnfTj5f1HmlSAOzh2gcMy2oararT7BU-DWGdwHnat4Vjfs7cBYEfrz6Fg-W9B_QgAREM9Sk9MYy55ILYQo9BJCnCvWJuFVUw1MV1zPYgj295C7Qi6Jf9hC5EgxGNSvZ_D3AIzwrHDd3dXPwI8ceVVTMx5F2UbnpS6iHubNoVVi6vHuqpIZMVmhdLiUvwV-5fJt4w5HQIngfvae-i4B9XfLABSe25VzmXBTJZ_VuU6ZQbSXKNIvwzHLOpQN1duwSNPEit59msarFFKG8SNojj-bdWSJjg-ZivM2oFJ4dOvESNpyg0qLFpgGCUISV7VSDdaCv__0TNCouZt2VfzCBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=VjFnfTj5f1HmlSAOzh2gcMy2oararT7BU-DWGdwHnat4Vjfs7cBYEfrz6Fg-W9B_QgAREM9Sk9MYy55ILYQo9BJCnCvWJuFVUw1MV1zPYgj295C7Qi6Jf9hC5EgxGNSvZ_D3AIzwrHDd3dXPwI8ceVVTMx5F2UbnpS6iHubNoVVi6vHuqpIZMVmhdLiUvwV-5fJt4w5HQIngfvae-i4B9XfLABSe25VzmXBTJZ_VuU6ZQbSXKNIvwzHLOpQN1duwSNPEit59msarFFKG8SNojj-bdWSJjg-ZivM2oFJ4dOvESNpyg0qLFpgGCUISV7VSDdaCv__0TNCouZt2VfzCBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68642" target="_blank">📅 17:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68641">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
فارس:
خبرهای اولیه از مورد اصابت قرار گرفتن یک نقطه از شهر شیراز در جریان  حمله هوایی دشمن حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68641" target="_blank">📅 17:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68639">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLQDEUeFDhaRk_1gRukNrk6b4AgNEB3B5D62R8St_L1F1lfQLYmHkB9kHPP1SvdyJ6VLjNEApvdVpVi8MIcx-Dq_SsCUAt0ipf_i8GuHzEbLu3EdM26Gr915pRPHX8Gs5rO_G1q1kJkP5IWy9IwMFM8p2ve9odA8cT6-jOUJajK3oEVXwIimwq4-1nVaybLWG_rhsPE32Hg0JH6pAWWhWZCnmXWNxRJ8Rl5N5WklAYGBXk4POEwvgUHp0ehcXj7ZtwiEeBASIuWq7rPl2IO-Z8CFMGF4TPLwObWrr7yieaTcXYE2_SzZ_l34WUFfVjXAuKlEqLhMA3E9bX7C5hb5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgdOxgSDhw3jNKnaqI9smlFo5UdZz2LRRcyuNB9o2yIXpLpzbwV4pdwEafpxYqfxvEDsHN3n1tONkLa_YaPxqnzxOA7TJYcZNLvu2_FwTfeg9I9GkyRJQE0CAbXnsdMn4rFi5qokDnCV5YVEPmjBUEcKaLH-_KXBJNjRGMByc7NMcl7YGmaDyIEF8ruOieRdh6DPxptquldhkj8ac0t0dIdzorF7Dr-Sj5RZDX11sE9BVn2PoZDWW1i_B2TxNNEsL5gzOwvoAhPS-Wpv1bJA0gy70fGVEqX8Ph78bhRGYX4tyCa-0Nn9ibSiuBN9B2pPLbdqJOskwFjzZRpkU74__g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68639" target="_blank">📅 17:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68638">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⏸
حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها (1944)‎
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68638" target="_blank">📅 17:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68637">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1qBRGsgd8kcFRgDYLwWQ55T8nA3GqRoDeQaiGdsrGlnwQ5Qne7_dRYh-Bo9Ynes-6AuiPKwjcXxdwwJFUTxU_NOhcvEMWP3TtbLYntp2YSEk0640uwt6N5344mdxEShPwxso0s-b7k2ArqoMd9agYIJy-8qlHM6UsrPc4InNZIVHZ_vbkGGVCgsgiujKPLJPYf9yGlvLs6DlbWybXfoE1_qv6sqs8VqHuWu7SsZOpR2OILzUNwDt5epE-XWuwqtF7sHEiV6ma_4ffJlivWiWfup0uxsiIfz_rRJEMFtxjf7x2IQhxvqRbZEYmo9VLmEfkHUbW4hgZbiZEYHK1b3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:با تداوم درگیری‌ها در ایران، قیمت بنزین بار دیگر از ۴ دلار در هر گالن فراتر رفت.
با ازسرگیری درگیری‌ها میان ایران و ایالات متحده و اقدام واشنگتن در برقراری مجدد محاصره دریایی که می‌تواند تنش‌ها را به‌شدت تشدید کند، تردد نفت‌کش‌ها در تنگه هرمز بار دیگر مختل شده است.
رانندگان ممکن است دوباره همان شوکِ ناشی از قیمت بالای سوخت را تجربه کنند، چرا که میانگین کشوری قیمت بنزین امروز بار دیگر از مرز ۴ دلار در هر گالن گذشت و به نظر می‌رسد رئیس‌جمهور ترامپ آماده تشدید تنش‌ها با ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68637" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68636">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⏸
🏆
👍
ویدیوی کامل مراسم اختتامیه جام‌جهانی ۲۰۲۶.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68636" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68635">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
حوثی‌های یمن با صدور بیانیه‌ای، از اعمال محاصره دریایی علیه عربستان سعودی خبر دادند.
حوثی ها با صدور بیانیه‌ای رسمی، محاصره کامل دریایی علیه عربستان سعودی را بر اساس معادله «محاصره در برابر محاصره» اعلام کردند و تأکید کردند که این تصمیم از لحظه انتشار بیانیه لازمالاجرا خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68635" target="_blank">📅 15:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68634">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A65ZyJttssFt8vMGD7918DIyiq_sHYcDq2Or9otbgVl35Z13sBEV0rEJaP3B4pWV9IbUvVXsVisXbXJ3KlXv5B4Hr4Xb7eCp0r8FQo2bS4x0ykC1m1bgNqoqR48J4i7yKq7EQYV3J12VOhlgtTFTqO8MNSxosLuRta36juYQKE_MjiuQ4vfqLg3f6UKiEPUqMZ_gx6qlBpTLajslxNLgYCn0vA3XGM0oqWOFZ3XxSEDxKK0z9mwkyg3Do4blgCwYf7ExJH7ZbxCFxJyvCxMjomLb0Yfe4XsUw-ZT-Y6novYLXAqPNmNePv8I1Z5hALyglUlt-35YcrNEC4Rx091mNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز:
میانجی‌ها به ایران و آمریکا پیشنهادِ یه آتش‌بس 10 روزه واسه احیای توافقی که امضا شده بود، دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68634" target="_blank">📅 15:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68633">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0Wp8D27OpVgWJMgZnQwq8fGy4QqjmF3wGRNjLBOkO2Kxyqio9me4EDHyfdsa4-2_efuo4zivnbNIJQ01RqmrveO8LXX_-yTdklI1AUGJ3X3Vgst4yOXeeU46xVK-qvkrvw_YXacyS3nCSFhK-jwa6dNDNRKyWedLxLfeiYwNdyiYbhof8hk_euseuJOlkzcxofRbFdp20YU-TMVx9YfQLlgNLNCgcl9UblUPDMZtQvuly27-RLoKi350_cUfqI6NjYLMNozA-hzmwGPrLA20pdGImYIUeHYl7_AmuVQt4Y8eFNUzjs6nDbYNBClrHuTJSBlr18doBEeRKiawLo7YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگند. روی هوش ما اندازهٔ آی کیوی مختصر خودشان حساب کرده‌اند.
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68633" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68632">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=GTDmy-4in52WjbgLuSTzvNRCGggcvmeSG6WHXRfqPxIQ3pQSfgzH0sIDblMWr-nddgpclvnTpzT-KT_fAa1Whi5SElxhPIOstYuabaj1NT2vhHdmrixDw6fAv5hPmwlcQecGtBU7YpP_rofFkS5_XmE5B3QQ8qEAfiV0z8JUFM-41wWIaznCmn3MBjO-J9SbsQcGAa3y_ToJm7zE7-DV71QB1PEV2tPJdt4p2mxLbJbOdl1ZxVzWii3TgLrzK5IUmhtTMNfhQct_YrfIkVhzpZwopS3gEMTsT8RPcWYFrjXgZ_MJZ30bFthWTBc-sxVhQWp65uUMMdp6Py4VqQ8Ah4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=GTDmy-4in52WjbgLuSTzvNRCGggcvmeSG6WHXRfqPxIQ3pQSfgzH0sIDblMWr-nddgpclvnTpzT-KT_fAa1Whi5SElxhPIOstYuabaj1NT2vhHdmrixDw6fAv5hPmwlcQecGtBU7YpP_rofFkS5_XmE5B3QQ8qEAfiV0z8JUFM-41wWIaznCmn3MBjO-J9SbsQcGAa3y_ToJm7zE7-DV71QB1PEV2tPJdt4p2mxLbJbOdl1ZxVzWii3TgLrzK5IUmhtTMNfhQct_YrfIkVhzpZwopS3gEMTsT8RPcWYFrjXgZ_MJZ30bFthWTBc-sxVhQWp65uUMMdp6Py4VqQ8Ah4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل:قلعه نویی موقع جنگ رفته بود بیرون از کشور تو امارات و ویلای خودش تو آلانیا ترکیه بعد اومده به ما میگه شما تو غار بودید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68632" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68631">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68631" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68630">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Huw8R_dxLuiFdGXjr0_4Vjj68BaJd9sRkHlN5cxDaBg60sZ1u5lt_8RWBGprEgEN4Bssfz_wqTAq5zw6DOjTeAJEnX_dOBs7UKQF9GX-rQKN7L0WN4_ri8lMV5lXSskoO-ohw-Vot8Meo4NEqS_oAUpKWpQ3hN4F1hgfkP7DA9APIyrh9QGjLZpHBDrFCKc1cS-lwx1GE_NaosXk3hyXteGEF2zS3eu0VM6FSuE9x0aBlTFgmgh79fgKWrgdMDKs1xzUyw0d9qMtU_a8Ouv8jQcOk96ChPVAy_tR6tSLXXVDgjy6t2RTs4TZVF2hmYBzIOoDqEq2z12OoqxeeJRfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68630" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68629">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmM7SknwZDV04HwUnVJG2Vw8-A2E9KFGvOD9UkLJXaB1SFGkK4-4YUaVNvOPmeuHzh_c0zrZ5dsYbU8769CfWvT3iK8CF0rtiTa1B-VwMxan4a8AspTdBcMCSfNu_QMKIQld-3g94hrCR1vdqJdZ4PhpWmnLAyPb9BEfczNorFZZzM92z0oTcL7tHtiet66mapGj0V4wBE7OXMHQ2rWDSam0jfi_Ex5wab839ULEgpvpNcEMEJ8pqRGv5o1cdkW4aBIrs5KJu8SpzQlKqnrPeEUzAXbDyqWWso2w29sMFoBH2YQS7ZSwnb8y7sFKKYZMTPorPgA5OCTdbxCOWHLFFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عبدالله شهبازی :
شطرنج پیچیده این جنگ داره به آخرای خودش میرسه.
به نظر میاد جمهوری اسلامی توی این بازی مثل یه بازیکن مبتدی عمل کرد و ترامپ هم در حد مگنوس کارلسن ظاهر شد.
ترامپ طوری بازی کرد که انگار حسابی گیر افتاده و به توافق نیاز داره. امتیازهای بزرگی داد و با طعنه و کنایه، رسانه‌ها و فضای مجازی رو هم با خودش همراه کرد.
این نقش رو اون‌قدر حرفه‌ای بازی کرد که جمهوری اسلامی باورش کرد، فرصت‌های طلایی رو از دست داد و دنبال امتیازهای بیشتری رفت. در نهایت هم نتونست یه «استراتژی خروج» انتخاب کنه و مسیرش رو متناسب با شرایط تغییر بده.
حالا نشونه‌هایی از اجرای یه طرح غیرمنتظره دیده می‌شه؛ طرحی که اگه عملی بشه، ارتباط مناطق جنوبی از هرمزگان تا بوشهر و شاید خوزستان با مرکز کشور قطع می‌شه و عملاً حاکمیت جمهوری اسلامی بر جنوب ایران از بین میره. به نظر نمی‌رسه اجرای این طرح نیاز به ورود گسترده نیروی زمینی آمریکا داشته باشه.
⏺
اگه این سناریو موفق بشه، می‌تونه شروع فروپاشی حاکمیت جمهوری اسلامی در سراسر ایران، طی چند ماه آینده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68629" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68628">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=nrx_FQccXmDE6D7yaL9ZLj80pue8PO7UyrRU2MDo9VL1zDn29fVT2IENZGKv7uY2y82yLVbPd-vNfVmB2SI3b72V3d_KYsqEzaeG0sA7oQUkt7XHmxHauAlsCRpzzBBeM5qpEiKmwDLhtF52u8BHpjrjxxDrAhNeJYHikQcjx_SrYwG209RU_vQDHd6S6g_85KVg7Tc6nZqbVcNBE5xTH6T8I8x2F9sN-tMUlrh2rrn8rq5NisEeyFSPOdECJ9v8aCV8ZUGkC-bmcRikfs1l-G2mpePJ2ssWitqS-4Se7se6Lzk4s8mQQmGurX_TI8rzKwwwRGItdtqICNLN1yUDWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=nrx_FQccXmDE6D7yaL9ZLj80pue8PO7UyrRU2MDo9VL1zDn29fVT2IENZGKv7uY2y82yLVbPd-vNfVmB2SI3b72V3d_KYsqEzaeG0sA7oQUkt7XHmxHauAlsCRpzzBBeM5qpEiKmwDLhtF52u8BHpjrjxxDrAhNeJYHikQcjx_SrYwG209RU_vQDHd6S6g_85KVg7Tc6nZqbVcNBE5xTH6T8I8x2F9sN-tMUlrh2rrn8rq5NisEeyFSPOdECJ9v8aCV8ZUGkC-bmcRikfs1l-G2mpePJ2ssWitqS-4Se7se6Lzk4s8mQQmGurX_TI8rzKwwwRGItdtqICNLN1yUDWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
«اگه اون دسته از آدم‌هایی که واقعاً می‌خوان برای ایران یه کار مثبتی انجام بدن، قدرت رو به دست بگیرن یا مسئولیت مذاکرات رو بر عهده بگیرن، اتفاق خیلی مثبتی خواهد بود.اما امشب هنوز تو اون نقطه نیستیم.
به نظرم دنیا داره به جایی می‌رسه که مشخص شده حداقل یه عده توی ایران می‌خوان تنگه هرمز رو در اختیار بگیرن و ازش به‌عنوان اهرم فشار علیه دنیا استفاده کنن.
دنیا باید تصمیم بگیره که آیا می‌خواد اجازه بده یه آبراه بین‌المللی دست کشوری مثل ایران باشه یا نه. این کار کاملاً غیرقانونیه و اصلاً قابل قبول نیست.
آمریکا هر کاری لازم باشه برای حفاظت از کشتیرانی جهانی انجام میده، اما وقتشه کشورهای دیگه هم سهم خودشون رو ادا کنن؛ چه با تجهیزات نظامی، چه با حمایت مالی، تا این بار فقط روی دوش آمریکا نباشه.
حافظت از کل دنیا برای همیشه، وظیفه آمریکا نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68628" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68627">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=YP9ca-nOXSbfUhJjkKSD5P9oqH_pRmcoMOtl91lXgl-ELJoH90fjVtEItqVPbTv5vL6xotPnGNdkCengJvuogbrbYmpX9hIjmmjIOD-7QKAVeaxiYSB2aP_w-O3VYarVH7OgvN1Xq0zyZSnLi13MKsiK0-9zNuAfhQGPSqh9D4PZ1fNbL_KcLef4U4Q09YjfnLkK3HNFC5EPr53XvX0nDXGRg9fQ9WFB3JfL4XfZAEo6KgGzyWNeYaeftB7h9IH-d6wSgN-6ullaInbMNVBYWS7w2OWYBkZKEMAsrH7CCacOL-LUvd4tyGICJtXQR3lvEiLIe3sNIPgXc6-Y4-yuiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=YP9ca-nOXSbfUhJjkKSD5P9oqH_pRmcoMOtl91lXgl-ELJoH90fjVtEItqVPbTv5vL6xotPnGNdkCengJvuogbrbYmpX9hIjmmjIOD-7QKAVeaxiYSB2aP_w-O3VYarVH7OgvN1Xq0zyZSnLi13MKsiK0-9zNuAfhQGPSqh9D4PZ1fNbL_KcLef4U4Q09YjfnLkK3HNFC5EPr53XvX0nDXGRg9fQ9WFB3JfL4XfZAEo6KgGzyWNeYaeftB7h9IH-d6wSgN-6ullaInbMNVBYWS7w2OWYBkZKEMAsrH7CCacOL-LUvd4tyGICJtXQR3lvEiLIe3sNIPgXc6-Y4-yuiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
ایران کشوری ثروتمند است. یکی از دلایل وضعیت نابسامان ایران این است که این رژیم هر پولی که به دست می‌آورد — چه از طریق لغو تحریم‌ها و چه از راه فروش نفت — صرف سرمایه‌گذاری در حزب‌الله می‌کند؛ آن‌ها در حماس سرمایه‌گذاری می‌کنند...
آن‌ها باید میلیاردها دلار را صرف سازندگی کشورشان کنند، اما در عوض، این پول را برای حمایت از تروریسم به کار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68627" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68626">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=mASuacYZvwdT9tlgxXHPw4iFdP4xzdvSqiMPAhkFyu1MPt_XnJdkj6pO0X4-c2KY-PPvLNlwHVArdtU8lUPUlaIyu2cQESQs2WizybVBxu7-aO5elrOlQXBAhSJC4zsAX0YeQ6ogEXV2lej9VW-dpTStGODDVWUJk4KLlxH4yQ7AH2HrNtm24jM3vYbPXZhioTCMmhNPuPBKqqGG9L-jJiDj_32i-zdNm-o5ZlqI7rTFE_ZOjLP5g12pQLY_KHVyGkrhwFxYMDYa1oI6pXadgrfYzC_dXmsSGnQaIgic5GR94f6-7RhFUawtvEKWfxuwcwJz5lF6gqLiA1nKmM0dDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=mASuacYZvwdT9tlgxXHPw4iFdP4xzdvSqiMPAhkFyu1MPt_XnJdkj6pO0X4-c2KY-PPvLNlwHVArdtU8lUPUlaIyu2cQESQs2WizybVBxu7-aO5elrOlQXBAhSJC4zsAX0YeQ6ogEXV2lej9VW-dpTStGODDVWUJk4KLlxH4yQ7AH2HrNtm24jM3vYbPXZhioTCMmhNPuPBKqqGG9L-jJiDj_32i-zdNm-o5ZlqI7rTFE_ZOjLP5g12pQLY_KHVyGkrhwFxYMDYa1oI6pXadgrfYzC_dXmsSGnQaIgic5GR94f6-7RhFUawtvEKWfxuwcwJz5lF6gqLiA1nKmM0dDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا احتمال تجزیه ایران وجود داره؟
⏺
مطهرنیا:
امکانش هست ولی احتمالش کمه.
همیشه این امکان واسه کشوری مثل ایران وجود داره ولی تجزیه ایران نه به نفع امریکاست نه اسرائیل.
اونا خودشونم خوب میدونن تجزیه ایران بیشتر به نفع روسیه و چینه.
پس امکانش خیلی کمه بخوان بفکر تجزیه ایران باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68626" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68625">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LL2Cz2Y8bwoCVT8y6yrbXWc9wSFGCVWsw1t13RJi0A6aYKyOhf_xpkFo1M_1Ek_-wUKUPul3kaMhgplZDCmOS6VsTAUC0bZi2J9tvrRx8tuhrKKu797Kjp7vFRbB5FCjrp26Kfa6m9HQMgnxIdy--VcJeO5bsmevwPuGIqOxdXcgSheptlQtnhiBH3_n6N20abJLaXBOZM1RVC4G2GASnk2_NRJ-laC9alfKbHgqaQzOspKAy_6n1e1khKplsz4nwa5L9KPwvFZgfCQOIc-iwLsI4krgNGXQUKHiqmtUYYaCST3Pkxn9cWLtKXVvwrk5-xhQKK1ZDSWJQRQQTqjZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود قهرمانی تیم اسپانیا در جام جهانی رو به دولت و ملت اسپانیا تبریک گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68625" target="_blank">📅 12:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68624">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=axKXJy8j4UBCSD6hAwO-zf_OLoDBhCN0qTWJgePalUugqbu8jpILhBzuWygDfKHn1FsZNzvpyTHvTErZNrzqJTyMp4NkIXavvlshh6kMwtQAg7SPqpIA4cT-bsY4Evo-wAzTRPELiSdhYfWFvxMUsMlK12dyTCnmAkJgNSPzSXa8Ak7tIamA0yP3S8bXfxjSmh99-rF-tLiX4lI8jHCmBssW4nvVo6F1BADhOzhH6wPR2Xy8_oCqFNzRI6kZPv6VlfH-eSheHVLurZFeb4g6WWeug2MbaT7wRVQFVeSAQ_mZpzDb_bFlZx1jXmtDvrobuVm3w-3Bg1AigKEvi8RVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=axKXJy8j4UBCSD6hAwO-zf_OLoDBhCN0qTWJgePalUugqbu8jpILhBzuWygDfKHn1FsZNzvpyTHvTErZNrzqJTyMp4NkIXavvlshh6kMwtQAg7SPqpIA4cT-bsY4Evo-wAzTRPELiSdhYfWFvxMUsMlK12dyTCnmAkJgNSPzSXa8Ak7tIamA0yP3S8bXfxjSmh99-rF-tLiX4lI8jHCmBssW4nvVo6F1BADhOzhH6wPR2Xy8_oCqFNzRI6kZPv6VlfH-eSheHVLurZFeb4g6WWeug2MbaT7wRVQFVeSAQ_mZpzDb_bFlZx1jXmtDvrobuVm3w-3Bg1AigKEvi8RVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام ویدیو ای از حملات آمریکا به ایران منتشر کرد.
تصاویری از برخاستن یک جنگنده F/A-18F سوپر هورنت نیروی دریایی ایالات متحده — مجهز به بمب‌های گلایدکننده AGM-154 JSOW — از ناو هواپیمابر کلاس نیمیتز، و همچنین شلیک موشک‌های کروز BGM-109 تاماهاوک از ناوشکن‌های موشک‌انداز کلاس آرلی برک، در این مجموعه گنجانده شده است.
اهداف ثبت‌شده شامل یک سامانه پرتابگر متحرک (TEL) و یک پرتابگر پهپاد است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68624" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68623">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60340234e2.mp4?token=sO7mE07oOlnpSJWKWbeFa4j56f0l4AbbAHcyUB30XI_xaG5oXIRRKuAWQlVQvgBRbfEsZqEZ2Mvu2RPnRyb5ZTBTQjp3dz10DTreq_mWSoCLGsMuoBvdNO4mRxpwRzBpmtGgI1J8qZO7caRER-WwhR3P2fBH2a-7U22InvwActm7pdj-zb20yXaibZDTg0AakRb6RmN--a2wfUH1Qc78S0_rSnw9LSO4rxVtvZpjGEvuZmNlmE-lRxP5tZWYH5210VqeDtnpIEoSpM9tX5gGbh7P7vmby2xeEbOhMhpIkg3iktYnY0CXP_LB1XnPcjIcTcl3N8rpCse77mpR2b3Shw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60340234e2.mp4?token=sO7mE07oOlnpSJWKWbeFa4j56f0l4AbbAHcyUB30XI_xaG5oXIRRKuAWQlVQvgBRbfEsZqEZ2Mvu2RPnRyb5ZTBTQjp3dz10DTreq_mWSoCLGsMuoBvdNO4mRxpwRzBpmtGgI1J8qZO7caRER-WwhR3P2fBH2a-7U22InvwActm7pdj-zb20yXaibZDTg0AakRb6RmN--a2wfUH1Qc78S0_rSnw9LSO4rxVtvZpjGEvuZmNlmE-lRxP5tZWYH5210VqeDtnpIEoSpM9tX5gGbh7P7vmby2xeEbOhMhpIkg3iktYnY0CXP_LB1XnPcjIcTcl3N8rpCse77mpR2b3Shw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در مورد ایران:
این کار بسیار بزرگتری است که ما انجام می‌دهیم. ما کار کوچکی برای جلوگیری از داشتن یک قابلیت خاص توسط آنها انجام می‌دادیم.
حالا ما فقط به آن پایان می‌دهیم. بنابراین واقعاً همان کار نیست. کاری که ما اکنون انجام می‌دهیم این است که هرگونه شانسی را که آنها بتوانند موشک هسته‌ای داشته باشند، از بین می‌بریم.
اگر به آن نگاه کنید، پس از یک هفته و نیم یا دو هفته [از شروع جنگ]، ما آنها را از [توسعه احتمالی] آن متوقف کردیم. اما من نمی‌خواهم از کلمه احتمالاً استفاده کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68623" target="_blank">📅 11:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68622">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yi_uhAJ4Q1iw_6H060aRq2IpsV6af-RlrdIn71KZK1pOypCq2yjQGlP_2MJJwWkn1uD7ucZ-BH5kGv4hpdMNtmQBbvtkwXMVMUvhcbAjBP5f6b1d5GSIgCFHI3r1QxojwVH-C_JIT_P877SlEo7_TbET53bQVxRW7RKxSEDpqVuLwLtctbS1jTAKmDb1iTwvHUSHwXW8158IMu6P9KiFN8N8sRUfra0ix9XW2Rj9KIzfHzB15evtkIxzeymaSgxaK_bB59muDxyZmOzG7EAtVQLlO341ERyHPMtS7NPSezIr0jusiEiiDjlnGfmHaGGkD7_n4PG4Fc3Bg8VktA6tRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📢
نیویورک تایمز:با نزدیک‌تر شدن دو طرف به یک جنگ گسترده‌تر، یک نیروی نظامی دیگر آمریکایی جان باخت.
پنتاگون روز یکشنبه اعلام کرد که سومین عضو ارتش آمریکا در جریان یک آخرهفته از حملات متقابل کشته شده است؛ در حالی که جنگ با ایران شدت گرفته و ایالات متحده شروع به اعزام هواپیماهای جنگی بیشتری به منطقه کرده است.
این سرباز در شمال عراق هنگام عملیات برای از بین بردن یک پهپاد تهاجمی ایرانی که سرنگون شده بود، کشته شد. این حادثه در میان زنجیره‌ای از حملات فزاینده رخ داد که تقریباً آتش‌بس حاصل‌شده در ماه گذشته را از بین برده است.
هیچ نشانه‌ای از دیپلماسی یا مذاکره میان دو طرف دیده نمی‌شد و مقام‌های آمریکایی که به شرط ناشناس ماندن صحبت کردند، گفتند که ایالات متحده در حال اعزام هواپیماهای جنگی بیشتر به خاورمیانه است؛ اقدامی که برنامه‌ریزی آن حتی پیش از کشته‌شدن‌های اخیر آغاز شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68622" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68621">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=ig0RtzzibGPAxfjg07GL4ejLOR2n97wBYPul7fVhbqsOVY_Xi_hSzkB2-7vbOSAB5Ojf_WvFaopQbG4ClyhoM98Z6mMsxUYwRHld7J_f4Yr9EsKlWNPBcPHxCRzq3s-ELe7bWBpV7HlO2DsoRLFnvKL0Qniv9NUdz0qefy21BvQp1yt34Bmda3g-2DZ7Ux_REPpAWy5TcGFU8Pnu7yfijuEFwfi7u1einNXkH-8-Ip6NcziAhUFDppyzCzt-FeUPy15n7h-jHqm3BWL8d71_8gDCdD64tUd45ScldE6aegcLnjGYylvYuF-KuLDogR9pHUdcZt50LbjdLy-l4zbLDDTPvxcOJ1pe-DvyRSYj0P5gocxh5UMclW_I1fEDSKN8Xb798cuaXbJMxueOzYmFZZr2b6AlWHO902jXXHz0oO3MKXJeH-_GnfF3tT-uPqBb_4pdGHpo1nxRdUMQU3k8lyGlrocpx6tnw-TcQkLkvTcTYiVpQ9kuZpe1u8tfcSP-EAmgM3xnBlQxt1UBZu5dDC16wu7sJ_yP9ULm-4JojrGYfTZKpOxNO7zcEiZl_FzkdnITvc-YtT2ouC2ZDWL1KAT19dbd1mApYeG7qBS89f7uIqCK_eAd95Jz02-F6d_1NJR9OECi6uWda1FHvI__x3Nx7F02eQMzmmOs10ENNgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=ig0RtzzibGPAxfjg07GL4ejLOR2n97wBYPul7fVhbqsOVY_Xi_hSzkB2-7vbOSAB5Ojf_WvFaopQbG4ClyhoM98Z6mMsxUYwRHld7J_f4Yr9EsKlWNPBcPHxCRzq3s-ELe7bWBpV7HlO2DsoRLFnvKL0Qniv9NUdz0qefy21BvQp1yt34Bmda3g-2DZ7Ux_REPpAWy5TcGFU8Pnu7yfijuEFwfi7u1einNXkH-8-Ip6NcziAhUFDppyzCzt-FeUPy15n7h-jHqm3BWL8d71_8gDCdD64tUd45ScldE6aegcLnjGYylvYuF-KuLDogR9pHUdcZt50LbjdLy-l4zbLDDTPvxcOJ1pe-DvyRSYj0P5gocxh5UMclW_I1fEDSKN8Xb798cuaXbJMxueOzYmFZZr2b6AlWHO902jXXHz0oO3MKXJeH-_GnfF3tT-uPqBb_4pdGHpo1nxRdUMQU3k8lyGlrocpx6tnw-TcQkLkvTcTYiVpQ9kuZpe1u8tfcSP-EAmgM3xnBlQxt1UBZu5dDC16wu7sJ_yP9ULm-4JojrGYfTZKpOxNO7zcEiZl_FzkdnITvc-YtT2ouC2ZDWL1KAT19dbd1mApYeG7qBS89f7uIqCK_eAd95Jz02-F6d_1NJR9OECi6uWda1FHvI__x3Nx7F02eQMzmmOs10ENNgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«سرباز روح‌الله رضوی» مجری یکی از برنامه‌های شبکه خبر، اهل کشمیر هندوستانه
🇮🇳
و پدرش به خاطر علاقه‌ای که به روح‌الله خمینی داشته، اسمش رو گذاشته روح‌الله؛
⏺
حالا این ویدیو از این مجری حسابی وایرال شده:
🎙
روح‌الله رضوی:
با سنگ، تیرکمون، کوکتل مولوتوف و هرچی که میتونستیم، رفتیم واسه تعطیل کردن سفارت انگلیس...
🎙
دهباشی، مستند ساز:
به این حرکتتون میگن هرج و مرج طلبی، یه رفتاری انجام میدی که هزینش رو یه ملت باید بپردازه.
تو به عنوان یه مسلمون که به حق‌الناس اعتقاد داری، بنظرت میتونی کاری بکنی که هزینش رو میلیون‌ها نفر دیگه بدن؟
🎙
روح‌الله رضوی :
اسمش رو هرچی میخواید بذارید. وقتی همه‌ی مردم بخوان یه کار بد انجام بدن، شما سکوت میکنی؟ من اینجور مواقع نمی‌کشم کنار...
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68621" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68620">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⏸
ویدیو کامل مصاحبه جواد موگویی با عباس عراقچی درباره حوادث یک‌سال اخیر از مذاکرات تا اعتراضات دی‌ماه و جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68620" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68619">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ1rdJkNKbwHfIPFwbQxmns_c0BPbLDrL55gjSXCSHs5WC6OJYCHUdmYJ9tMhbR2FJHG1qq83ktFHofCutQA1NC__iLdpJDg5rhWCREgG-M3XpU3s_AtOVEAGaFSHKmFMHD2-E_WJvQSxM3DdYBCvxV0aKe8tCNR2W61QikGOm0z6kc8oKpHmuF0xKMkj9B-neTfXMD8Qh0AL0O-iIWXe2YmvQFRHCB0z8NycHpwr2cGpU8NrsF1gFksikf1beiB3HDv1GiQ-3zKoCUEWJGNckFJkxfb1sdAGt60c7l7s0vg27jRgQDUUzDIc5suqbx0-YCihGhX7R_OkPrfFOFLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68619" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68618">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YE3cioO42AXHqQC8spJH9ampOz95QFMJrTXctVj0EWtD16gY62A1jVmOUxiYN9mXUTccyR3Yin9Bg9WcuYdP0dy7IysIQWlo5h7_nVC7OhdETmuO-kJWE46FN7NBI4IkZrNBk7Pdiz8upicWM8rLLG_w0qTs7nqSenegZMyLNPTtRAhLo42xJdwvkiMXtrLtNEtSk6BtbfG1dtIGbJHMHj9PxF4kqphHlaFah-hLIOu7J2yb8NoxNDBA_P87E5bxQHRuS53CeeyuxhiU2g2xbhf0D5u57s65ioa8_gUozqKBzg-i-7Sq528hWSr038Z2__25VA5JOnRh3gP9dQi1TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در نزدیکی سواحل عمان مورد اصابت قرار گرفت و دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68618" target="_blank">📅 03:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68617">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68617" target="_blank">📅 03:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68616">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
انفجار در خورموج استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68616" target="_blank">📅 03:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68615">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=jIOJzZC0ol8GMajsVwTVSZHKHcRxhw2wptgO_OG9O8l1Q_ld2DBGXMMKQn8W1O4ZuhWJBOPRguuRkZ8DKhbT4QmiQz3Isc_Aux4dAYx_0-mHoMM4r0FBhwygGobgFqrOt4CqOwZp-Bln1WYTZ0rtLJ4Q9Uh26U2sjZLRwAVeLvwiwGNDTMDwue3AknS5uyGYbR8o44bxhiRrFBE3Ls6vkBXYYY4IPLlsU48djTmyaKPe3O-goedKF0Z9vpnifEHqnZOP1Lcr-i8sYYywBm8q2GTjgCisqphEQgiP7URSSBoQp5BUW_tzfi0H7Ff6BJZ_hmbTXRsAU-p5W1rLXI-g3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=jIOJzZC0ol8GMajsVwTVSZHKHcRxhw2wptgO_OG9O8l1Q_ld2DBGXMMKQn8W1O4ZuhWJBOPRguuRkZ8DKhbT4QmiQz3Isc_Aux4dAYx_0-mHoMM4r0FBhwygGobgFqrOt4CqOwZp-Bln1WYTZ0rtLJ4Q9Uh26U2sjZLRwAVeLvwiwGNDTMDwue3AknS5uyGYbR8o44bxhiRrFBE3Ls6vkBXYYY4IPLlsU48djTmyaKPe3O-goedKF0Z9vpnifEHqnZOP1Lcr-i8sYYywBm8q2GTjgCisqphEQgiP7URSSBoQp5BUW_tzfi0H7Ff6BJZ_hmbTXRsAU-p5W1rLXI-g3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پایگاه امام علی در چابهار مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68615" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68614">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VScpeK5r2Wltlo_PoWGioTqDE_70o8Q6JwZvxJvs0iWb9ok1ME1btFGr8FNd5ICF934b0gIel0_i2Gp9En59T0q2VvHXCnYSRjnOE8XzrYx4roW3hDkJEEfR2agHCvCbjni4XYgt_i4YoCD6OJ0K6shY7IfdjrtI1IMd3mNLi2HkDz6EYxGW4GiTG9Lh3XRmUkrJQzgbAxr7Fq1kkqlLZlGm1tS6ExRH5sxfkhZPfliZ71MlZ27HwwwjdQ-RDeT_Rdi4xhMI1T_PhJ1E0Pcu3Aox0Sif7dPqwSRm0G4rvjeGPDO5bM4p5J1ICjU4Dev2fO7PRtyYOb8GQa8ojofyog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68614" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68613">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
منابع حکومتی:
انفجارهای شدیدی در شهر رأس الخیمه، امارات متحده عربی، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68613" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68611">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521034efe8.mp4?token=bPNpNsYWg9w-0l10m7tpFeiKoiJ6-Oll4WGJaXuq_8Wq-zA3_RoJr_St6h20wv0yxl-KiC6bOGX3e7ot5XuPgew28bBAjKxkQpee78-Yt2UmEHCFdSrY5OIyU-R8f9qz985M5eEY7dhhOdhrhUTH3gSaKtrp-jjIJDtK1Mjr0seoVScG52KZcpW4VRcOwgesqsCBaqY_d-Bbejkz2ts5O9pok98jgFJUmiykh01NYYG44sBaLCpkVE-iAn8gmoX3G4QE9LUUoFEKu28qoJHc9aSeY50zVBGSzd2w14GOSm2MknivW_KAHF3-n6hnd901HeYrNthwCfP2Uj2liqISMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521034efe8.mp4?token=bPNpNsYWg9w-0l10m7tpFeiKoiJ6-Oll4WGJaXuq_8Wq-zA3_RoJr_St6h20wv0yxl-KiC6bOGX3e7ot5XuPgew28bBAjKxkQpee78-Yt2UmEHCFdSrY5OIyU-R8f9qz985M5eEY7dhhOdhrhUTH3gSaKtrp-jjIJDtK1Mjr0seoVScG52KZcpW4VRcOwgesqsCBaqY_d-Bbejkz2ts5O9pok98jgFJUmiykh01NYYG44sBaLCpkVE-iAn8gmoX3G4QE9LUUoFEKu28qoJHc9aSeY50zVBGSzd2w14GOSm2MknivW_KAHF3-n6hnd901HeYrNthwCfP2Uj2liqISMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت سربندر ، ماهشهر استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68611" target="_blank">📅 03:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68610">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f087874ede.mp4?token=XDueXsN0MnBIcOvwQbdcyykAnf9lw8V91ka2D84v0SRYlPfUIeSFMg4oip1umWOFRZbYBFKHhXoB00SeG21TRcaCN9T5vZqiAA266hiFfaM77jTmcbaadjfAcGNUVASdMunA8nc_auYSTMohuULYQDWXuCobmAGJM6ytrHKZ05LpSseeHa8EcX14j8pRbi-K_eCtjScyowZ19s0YCxwLOUqxK9O-b6yBrb7ketxvr9LUTdZLs1A831Xoz9lqAcvoKmGx_hnBjY7N2WREW8rngdpfaLy5axpCY59r91Kv8HC-_6FU-XTau8SRTubv4bUHS-2yQsUSBIK_jrOwjYDnnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f087874ede.mp4?token=XDueXsN0MnBIcOvwQbdcyykAnf9lw8V91ka2D84v0SRYlPfUIeSFMg4oip1umWOFRZbYBFKHhXoB00SeG21TRcaCN9T5vZqiAA266hiFfaM77jTmcbaadjfAcGNUVASdMunA8nc_auYSTMohuULYQDWXuCobmAGJM6ytrHKZ05LpSseeHa8EcX14j8pRbi-K_eCtjScyowZ19s0YCxwLOUqxK9O-b6yBrb7ketxvr9LUTdZLs1A831Xoz9lqAcvoKmGx_hnBjY7N2WREW8rngdpfaLy5axpCY59r91Kv8HC-_6FU-XTau8SRTubv4bUHS-2yQsUSBIK_jrOwjYDnnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68610" target="_blank">📅 03:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68609">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
تسنیم:
دقایقی قبل صدای انفجار در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر، بندر امام خمینی (ره) شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68609" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68608">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در بندرامام و ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68608" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
