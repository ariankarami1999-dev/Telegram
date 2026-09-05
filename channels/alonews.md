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
<img src="https://cdn4.telesco.pe/file/SN3MWV-wzQYAq2seln4eToVb3D4kGTvU45xzt3k63VMIPqIGkhsfxSl-eUchaxrsFVeP0PlVM7nPERlEft6S6EKmTAMCUgUPCyCc6oiFvuTcFc7hIczuXMRNfhQ9Jc5_IWX6sMHXTKtHzH6e2zBG-LmurMz41VkTcEACsv-jU9LO8oZhMswM2BC-RXuPj48rRddZYydMjLWzVOn2792ABev6rbk--5PojWwx_9xYDFW2D5Ahk3t1Ddw_NP2NqjBQV9boGe02UK9cpETGBFNoqI4qbUdITPiRyQxILaKDZch6XnAkyn6f6XlVMCmjUb6L4yBBhJCCGF89FZcOBuOt4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 939K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 14:49:11</div>
<hr>

<div class="tg-post" id="msg-145717">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1fae30cd0.mp4?token=PQjITn6NvOGSEdAfVyl52cL4rQDNZ3oQAXHEgOGBQF7dEY0QludEkDEwDbLo5tJqxZog7mVuBUAphG-vGKpLdeRZSdhnLP1vwZGq_hE0KLg4yOmOQnyUFJLfkbXVK5LZWKNVBGtTovsgDQMWM_XznvbK5p65XYhcSR2TNbp--zGcqEWOP69lZdt9AVgaCCk235Ha68Ff110VnBLHY0pLp-wOxJDmMuNv43PiF-6-eUxKJos6VXxZbbQrS7TZQp4AFUoP7QecWp9EvdimF_SDyONv0ieFCVMCoqT8sSEcH_C1GSeL2GcJG2zqifH7bc753XPJzfGgzTnrwpmTbRQUbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1fae30cd0.mp4?token=PQjITn6NvOGSEdAfVyl52cL4rQDNZ3oQAXHEgOGBQF7dEY0QludEkDEwDbLo5tJqxZog7mVuBUAphG-vGKpLdeRZSdhnLP1vwZGq_hE0KLg4yOmOQnyUFJLfkbXVK5LZWKNVBGtTovsgDQMWM_XznvbK5p65XYhcSR2TNbp--zGcqEWOP69lZdt9AVgaCCk235Ha68Ff110VnBLHY0pLp-wOxJDmMuNv43PiF-6-eUxKJos6VXxZbbQrS7TZQp4AFUoP7QecWp9EvdimF_SDyONv0ieFCVMCoqT8sSEcH_C1GSeL2GcJG2zqifH7bc753XPJzfGgzTnrwpmTbRQUbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نِتانیاهو درباره ایران: چه کسی در تاریخ ۷ اکتبر فکر می‌کرد که ما چهره‌ی خاورمیانه را تغییر خواهیم داد؟ من فکر می‌کردم.
🔴
نیت من این بود که در نهایت با ایران درگیر شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/145717" target="_blank">📅 14:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145716">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
دریادار سیاری: ملت ایران به خود ببالد که مقابل دشمن مسلح به همه فناوری‌ها؛ ایستادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/alonews/145716" target="_blank">📅 14:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145715">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نتانیاهو درباره غزه: بازسازی غزه فقط در صورتی امکان‌پذیره که ابتدا خلع سلاح انجام بشه. هنوز نمی‌تونم بگم چه نوع بازسازی‌ای انجام خواهد شد، چون در حال گفت‌وگو با دوستان آمریکایی‌مون درباره این موضوع هستیم.
🔴
گاهی اوقات دیدگاه ما با آمریکا یکیه، اما گاهی هم اختلاف نظر داریم. وقتی اختلافی وجود داشته باشه، آمریکا منافع خودش رو مطرح می‌کنه و من هم از منافع اسرائیل دفاع می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/145715" target="_blank">📅 14:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145714">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50080ba6b7.mp4?token=ZL54G5aQ2xf2eZ5b8iekfY6b7o9vgPJAXWRyRNuyuYaPOiQSzP-AVO_U6igenWgca4QUFgCgj73Q43_S7CSNRMJl5RdEnEOoQbijVVhXTFeAd3USqyZIqSLGwoo8jgUpX6JXIa5uS9vVmySDFaExYbc8NN6jGjeMpsUJMdtz55FQ5wLKqjTv6eObngoUnUnoDRFrUio5m48h-L6ClrEosZlBsSxD9oLg2-g9FqkgUa1JZQyUquamHujdbwYhYSdIAXXosY6inEEErNHgzN2m_Qb29YN171cGKOzXJWUR669A_6d6dqUy1Q8bzDnJJ0jf66wQBeBxvOCjxzbhw2eCiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50080ba6b7.mp4?token=ZL54G5aQ2xf2eZ5b8iekfY6b7o9vgPJAXWRyRNuyuYaPOiQSzP-AVO_U6igenWgca4QUFgCgj73Q43_S7CSNRMJl5RdEnEOoQbijVVhXTFeAd3USqyZIqSLGwoo8jgUpX6JXIa5uS9vVmySDFaExYbc8NN6jGjeMpsUJMdtz55FQ5wLKqjTv6eObngoUnUnoDRFrUio5m48h-L6ClrEosZlBsSxD9oLg2-g9FqkgUa1JZQyUquamHujdbwYhYSdIAXXosY6inEEErNHgzN2m_Qb29YN171cGKOzXJWUR669A_6d6dqUy1Q8bzDnJJ0jf66wQBeBxvOCjxzbhw2eCiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسن روحانی: به مردم بگوییم قرار ما این است با قدرت‌های بزرگ بیست سال دیگر بجنگیم، اگر مردم قبول کردند برویم ادامه بدهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/145714" target="_blank">📅 14:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145713">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fa90f779.mp4?token=PMKavym1ARQYCRZDwl06LoLUiMFQsC-X7tVOdnbTKeuWKZsftrohVCgiwGCqP5638AfQxqwRkqpmpd-mUTgZI92zmElEqPz1ZuIUczqio42xOV06QjO64LTL4WKl10oJHM6029qzt53UoabJIycmtoGsg4v18XwpPCacfj89iW8KMK3dr8tFHaeNzvhKkfWCmxCwYZgsaEXlb0IftJOHjgtTDz9AL2FxAMz16MlPMLpNNk2ZxK6zgbIu0fER0jlxr9pKRSEogWOzMqrQZ_NrlqnhQLaNk3HYyjJp2dE4r0HgWtDQXJWyu6sZx42blf2ZpBv9GJhHxzR24GGdS9Qyhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fa90f779.mp4?token=PMKavym1ARQYCRZDwl06LoLUiMFQsC-X7tVOdnbTKeuWKZsftrohVCgiwGCqP5638AfQxqwRkqpmpd-mUTgZI92zmElEqPz1ZuIUczqio42xOV06QjO64LTL4WKl10oJHM6029qzt53UoabJIycmtoGsg4v18XwpPCacfj89iW8KMK3dr8tFHaeNzvhKkfWCmxCwYZgsaEXlb0IftJOHjgtTDz9AL2FxAMz16MlPMLpNNk2ZxK6zgbIu0fER0jlxr9pKRSEogWOzMqrQZ_NrlqnhQLaNk3HYyjJp2dE4r0HgWtDQXJWyu6sZx42blf2ZpBv9GJhHxzR24GGdS9Qyhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرود یک فروند هواپیمای نظامی آمریکایی در فرودگاه بین‌المللی اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/145713" target="_blank">📅 14:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145712">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec68e65f4.mp4?token=NpzhexPKLRN-CNfZei_HFYFY2TXIDOccpFGESqfxbYHaFg5TzE2g_-cKp3U9wjd9T4PUUKhHCjSPDSIqM7hTzjQkIYmDPTlgM7fgrolrnW81Zcr1rMNvDelFTCCiE3K__eESBbuvTiiFsCt7XbV9okHasKfVgcvO-f3xRPY986v_HQaidvDATMVMfSsSPv8TnGXMVDz8CAo5_n8dKLuyFa45GzFyoBp70_YPQNJGxmZfSTXa31jzwL5Rnnbo_SgRC5H8ajYh-zZHyrjmgGrzObbIsuZj0isi0x7dU9hKESqrYkXrQ4Pl5SSLFDSD7mr48jqVumF4qNWgaAyrsS7igw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec68e65f4.mp4?token=NpzhexPKLRN-CNfZei_HFYFY2TXIDOccpFGESqfxbYHaFg5TzE2g_-cKp3U9wjd9T4PUUKhHCjSPDSIqM7hTzjQkIYmDPTlgM7fgrolrnW81Zcr1rMNvDelFTCCiE3K__eESBbuvTiiFsCt7XbV9okHasKfVgcvO-f3xRPY986v_HQaidvDATMVMfSsSPv8TnGXMVDz8CAo5_n8dKLuyFa45GzFyoBp70_YPQNJGxmZfSTXa31jzwL5Rnnbo_SgRC5H8ajYh-zZHyrjmgGrzObbIsuZj0isi0x7dU9hKESqrYkXrQ4Pl5SSLFDSD7mr48jqVumF4qNWgaAyrsS7igw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: اونا می‌تونن به ما حمله کنن و ما هم پاسخ می‌دیم.
🔴
متوجه شدید ایران داره به همه شلیک می‌کنه؟ به کی شلیک نمی‌کنه؟ فقط اسرائیل.
🔴
چرا؟ چون دقیقاً متوجه حرف من هستن؛ تا وقتی من نخست‌وزیرم، چنان ضربه‌ای بهشون وارد می‌شه که حتی نمی‌خوام جزئیاتش رو بگم. این ضربه از قبل آماد
شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/145712" target="_blank">📅 14:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145711">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
زاکانی: به دنبال تولید برق با انرژی اتمی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/145711" target="_blank">📅 14:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145710">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
پارلمان پاکستان برای نخستین بار به عاصم منیر اختیار قانونی فرماندهی هر سه نیروی ارتش، نیروی دریایی و نیروی هوایی را اعطا کرد
🔴
دوره فرماندهی او دست‌کم تا سال ۲۰۳۰ ادامه خواهد داشت
🔴
وی در مقام «فیلد مارشال»، مصونیت قانونی خود را تا پایان عمر حفظ می‌کند و برکناری او تنها با رأی دو سوم پارلمان امکان‌پذیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/145710" target="_blank">📅 13:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145709">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وال استریت ژورنال: تحریم‌های اعمال‌شده توسط آمریکا از تیرماه گذشته، ایران را از صادرات نفت بازداشته است.
🔴
مسدود کردن تنگه هرمز توسط ایران، ترامپ را مجبور به پذیرش شرایط آن نکرد.
🔴
رهبران ایران انتظار دارند که این وضعیت (احتمالاً تحریم‌ها یا بحران اقتصادی) تقریباً به مدت پنج ماه ادامه داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/145709" target="_blank">📅 13:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145708">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
پزشکیان: وقتی جوان ما در خیابان مشکل دارد مقصر ما هستیم/ درنگاهی که داریم باید تجدید نظر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/145708" target="_blank">📅 13:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145707">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ccdbf8531.mp4?token=s94PBPEFk2W1Lxt8Sd5rzDgjCk-8XxPqCow_ol3kQBIsa413J1eM2KPC5UKtwVbvjdn6XCtRDDsIVukvsh_lyiFUDtV923HO-uy5J0WyMkY7feV3w3IIbRuoa_Ci36V4hLBOwEiDnEi5Kp8A3ETSjycp9foH6MN1S24VD8vMzAATP34F1gv54XE5m6ozw7a9g1pxpc32yDBFU3cpGB2x6uUYO_LAoo14NV3ckaKDh53ekE6HyqdrmfYR4npoh76QCaDqpBRk6NW26oVRIAowhRJPXxZsoelAucFqGBCBTBLIR3zt7uMYGedwIhe-exEsPvOR1o4r3gDQBngnOd6ADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ccdbf8531.mp4?token=s94PBPEFk2W1Lxt8Sd5rzDgjCk-8XxPqCow_ol3kQBIsa413J1eM2KPC5UKtwVbvjdn6XCtRDDsIVukvsh_lyiFUDtV923HO-uy5J0WyMkY7feV3w3IIbRuoa_Ci36V4hLBOwEiDnEi5Kp8A3ETSjycp9foH6MN1S24VD8vMzAATP34F1gv54XE5m6ozw7a9g1pxpc32yDBFU3cpGB2x6uUYO_LAoo14NV3ckaKDh53ekE6HyqdrmfYR4npoh76QCaDqpBRk6NW26oVRIAowhRJPXxZsoelAucFqGBCBTBLIR3zt7uMYGedwIhe-exEsPvOR1o4r3gDQBngnOd6ADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: همیشه می‌شود بهتر شد، بهتر دید، بهتر فکر کرد، بهتر مدیریت کرد، بهتر کار کرد و با هزینه کمتر، باکیفیت‌تر عمل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/145707" target="_blank">📅 13:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145706">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
مدیرعامل شرکت ملی گاز: ایران در میان تنها ۶ کشور جهان با روند افزایشی شدت مصرف انرژی قرار دارد و باید حساسیت نسبت به مصرف حامل‌های انرژی در بخش خانگی افزایش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/145706" target="_blank">📅 13:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145705">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5747cd754f.mp4?token=D6JPVDTwUGfu5obNAxKnuCCdrVV5p2c39A-rEG858AXnSiIz69h2A853GiClK4srRtNESpNAESC3hLzdTZv1nGwxIJD5D2Mg9J9s3m80ITHizYDLH93uJSlbEp9V3ZzFXCcj1AJfpp6Eb_NejdoMzn_McTSfbTfZca9sfmNmvG9akE3VNFYCEN1LpEcEBHh7DxpDrzQMDMMqGsQhf4zp-kcxdT8fiNE_ubG2qSnJhqrxoNfbUkUHnR_cmgK787W2j-joVsbs32HQ32eja6muTqw4H9m4V3PS5dT6Yvs_BhaXrPPOamZRvneXZfkDtbXq7L0nSEiAZOkV-l4x6nsZFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5747cd754f.mp4?token=D6JPVDTwUGfu5obNAxKnuCCdrVV5p2c39A-rEG858AXnSiIz69h2A853GiClK4srRtNESpNAESC3hLzdTZv1nGwxIJD5D2Mg9J9s3m80ITHizYDLH93uJSlbEp9V3ZzFXCcj1AJfpp6Eb_NejdoMzn_McTSfbTfZca9sfmNmvG9akE3VNFYCEN1LpEcEBHh7DxpDrzQMDMMqGsQhf4zp-kcxdT8fiNE_ubG2qSnJhqrxoNfbUkUHnR_cmgK787W2j-joVsbs32HQ32eja6muTqw4H9m4V3PS5dT6Yvs_BhaXrPPOamZRvneXZfkDtbXq7L0nSEiAZOkV-l4x6nsZFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای یمنی (حوثی ها ) در حال حاضر به سمت مواضع و تجمع‌های نیروهای وفادار به عربستان سعودی در حرکت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/145705" target="_blank">📅 13:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145704">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBrhLWvWURK4QRmWxnGTq8XyNE3htmVbPFQ2fuZFkX7Jbzr76UEgIU_0VoeUJ9ZcghZluIHR-WZAiU0oixrWdrsUMjutyrE2NFhpcQvrwXr-pAQ3AgHZUT4FQWMgu2L6QLpANb0h7TPKlUpmb3g8U2erYLpqfgpgbaDdjt9eMtj0pbP9YtJtuCdWDrRa_5G5Gb0bHkIHmnwKJ_ntPKyxqkBcno0dbgONHxayZmCy4nav6NlW5L-kQRjckt7YXp3bRAdfsvrZC-4HvEtE3D9BAVGr5eUSn7KrS6Vmo4DJrtBhzmgPfwxHv6z5yeZ5QLuLkXiRKB6xtbcLSYRH4LOIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر جدید از چین، یک پهپاد بزرگ و پنهانکار با نام غیررسمی WZ-X را نشان می‌دهد که دهانه بال آن حدود ۵۲ متر، هم‌اندازه بمب‌افکن B-2 آمریکا، برآورد شده است
🔴
این پهپاد احتمالاً برای ماموریت‌های شناسایی و مراقبت در ارتفاع بالا و پروازهای طولانی‌مدت طراحی شده است. گفته می‌شود این پرنده توانایی پرواز در ارتفاع بیش از ۱۸ کیلومتر را دارد و برد آن به حدود ۱۹ هزار کیلومتر می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/145704" target="_blank">📅 13:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145703">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
عارف، معاون اول پزشکیان: مشکلات اقتصادی قابل حله؛ مفتخریم که در تمامی زمینه‌ها به خودکفایی رسیدیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/alonews/145703" target="_blank">📅 13:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145702">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8814fb781.mp4?token=BvsZaJZRtRwn7AaWplzuWny1oLcxLls8W1FwJS3hEuenTDOfbum49QkCEcPVL83sGDPTBtlj9Xkes7HEG6xwK-6YwbCnduXe2-rZpx9UD6xceEeXo98ZBQT7inEQn6N0pcLglWGZvEtMVkFEH-xYpKRXCLnM0c9k-f_rxodTIftUp6TKSVOTMU0Lg2b1Q9HRaY3fZCqw4zOss2aFEpFODZcI_I9af93JBpJDqUR2PqmxAcmIyv4GAyr8gA9gG6-WJ6Cdgml21xeSHfnHHCyd6tshCgp3GC54P-ZGPTofW9N1dbE1JywuCbe7ei1MmMUZGaRcSRQA4KYjtkkAMtGHu7O6I6qT3sOIIE8vlO9DPJ0upNNkuS5V37GuJKi8coPNGX1sWhOoTYe-LOVuFxsdVTNkhQCxm3ai37JAbAD4ZNXkXsWW8d6hOHLyqu_KEOYveD1yWs8tUXBneBwzHr59K6KFrxc6kZKIywOKdxms1Ye17DqGItGcWAfs7hDkyyX6p-aYEy4C9Hq3TZLe2byGhuivCY48iQhFaZaw5l1vp8jOETkn689g7_3ihLdD0T3cuuNyk4mII1GDKcXjVBiAvODMQpewXH8U_q8XMVaPj5GoJ-SkFchLkRnbpClxPGjJ0ajUylrV9i6kQLkvrEkQxcface-nfZKzfpQ2uwjx9Wo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8814fb781.mp4?token=BvsZaJZRtRwn7AaWplzuWny1oLcxLls8W1FwJS3hEuenTDOfbum49QkCEcPVL83sGDPTBtlj9Xkes7HEG6xwK-6YwbCnduXe2-rZpx9UD6xceEeXo98ZBQT7inEQn6N0pcLglWGZvEtMVkFEH-xYpKRXCLnM0c9k-f_rxodTIftUp6TKSVOTMU0Lg2b1Q9HRaY3fZCqw4zOss2aFEpFODZcI_I9af93JBpJDqUR2PqmxAcmIyv4GAyr8gA9gG6-WJ6Cdgml21xeSHfnHHCyd6tshCgp3GC54P-ZGPTofW9N1dbE1JywuCbe7ei1MmMUZGaRcSRQA4KYjtkkAMtGHu7O6I6qT3sOIIE8vlO9DPJ0upNNkuS5V37GuJKi8coPNGX1sWhOoTYe-LOVuFxsdVTNkhQCxm3ai37JAbAD4ZNXkXsWW8d6hOHLyqu_KEOYveD1yWs8tUXBneBwzHr59K6KFrxc6kZKIywOKdxms1Ye17DqGItGcWAfs7hDkyyX6p-aYEy4C9Hq3TZLe2byGhuivCY48iQhFaZaw5l1vp8jOETkn689g7_3ihLdD0T3cuuNyk4mII1GDKcXjVBiAvODMQpewXH8U_q8XMVaPj5GoJ-SkFchLkRnbpClxPGjJ0ajUylrV9i6kQLkvrEkQxcface-nfZKzfpQ2uwjx9Wo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقبال و بوسیدن دست اژه ای توسط هندیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/145702" target="_blank">📅 13:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145701">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پزشکیان:باید کاری کنیم دشمنان طمعی در این مملکت و آب‌وخاک نداشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/145701" target="_blank">📅 13:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145700">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
زنسکی:روسیه امروز به فرودگاه‌های کیف و بوریسپیل در اوکراین حمله کرد، این در حالی است که قرار بود نمایندگان ترامپ از این کشور بازدید کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145700" target="_blank">📅 13:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145699">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1acc0d88.mp4?token=VayU75M1N_4CkqtBcp3L8xT9fbboo0TrAUgvY2psFx53bn6pU_eY7bZswQmqkZHeTJO49cjGtFE1-F_53MnB2FqRpheSHeDVWpt7TWPk1y8jBOVTIenB5DYr_mkvTxR9qoCWnbydOBRejijVs07iyCJxn8yhHGJ179kdD3roQ_YPXDc-KMtk5E7vF5rYPcyfj58zEYpADm-4VM-L3HWUN5vy5n51twGaUq_pEIQXNHIyIeerBr35FPix4pPFHMxZKhFXwFPGkH17dwuzC76FqkhaHosGtGdMgjJ4imuSE6l31ijw7bHTZg1aUUdj6Zy-OZzBXPapkw9p8BBN-tbQ5JQslc_WRDW07OnwYONjcJrN41h3gG5V-TTRDOhPkgyRBczwTdbG-v5-V2wg3zhJWzKwn3jOH8Tp7pgn2wInX_6zXlgIpahKi0gN-evZ-sxvcqqso6_Z1Li0NFeOtdKxLycbeIlmRTnv8MKl7kGH0t8cRMXrXU2RizuYbDRaB_IQCv4PaJIAttj7AsJqlXZB5pb7Qh9pP5XN5qSaxJC2ftvdlCqr112_lf2pi4munzafCK63L0Jt_zipq92RB0Sz7mY0yHoj4CKTXimrrv2n5yUHvemxeFNs1GF9Be_ZSsGZOLJbtx_AlARRaYlK_La61i_O_e9zOpSOZ6rOjbVagw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1acc0d88.mp4?token=VayU75M1N_4CkqtBcp3L8xT9fbboo0TrAUgvY2psFx53bn6pU_eY7bZswQmqkZHeTJO49cjGtFE1-F_53MnB2FqRpheSHeDVWpt7TWPk1y8jBOVTIenB5DYr_mkvTxR9qoCWnbydOBRejijVs07iyCJxn8yhHGJ179kdD3roQ_YPXDc-KMtk5E7vF5rYPcyfj58zEYpADm-4VM-L3HWUN5vy5n51twGaUq_pEIQXNHIyIeerBr35FPix4pPFHMxZKhFXwFPGkH17dwuzC76FqkhaHosGtGdMgjJ4imuSE6l31ijw7bHTZg1aUUdj6Zy-OZzBXPapkw9p8BBN-tbQ5JQslc_WRDW07OnwYONjcJrN41h3gG5V-TTRDOhPkgyRBczwTdbG-v5-V2wg3zhJWzKwn3jOH8Tp7pgn2wInX_6zXlgIpahKi0gN-evZ-sxvcqqso6_Z1Li0NFeOtdKxLycbeIlmRTnv8MKl7kGH0t8cRMXrXU2RizuYbDRaB_IQCv4PaJIAttj7AsJqlXZB5pb7Qh9pP5XN5qSaxJC2ftvdlCqr112_lf2pi4munzafCK63L0Jt_zipq92RB0Sz7mY0yHoj4CKTXimrrv2n5yUHvemxeFNs1GF9Be_ZSsGZOLJbtx_AlARRaYlK_La61i_O_e9zOpSOZ6rOjbVagw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): حملات هوایی علیه آنچه «مراکز نگهداری تسلیحات متعلق به حزب‌الله» در جنوب لبنان خوانده شده، انجام داده است
🔴
ارتش اسرائیل مدعی شد این حملات یک «تهدید فوری» را از بین برده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/145699" target="_blank">📅 12:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145698">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7425ddc2e6.mp4?token=arcr82_2d8z-45zIWNMModgd1apfVLPugnmEw2VPDRDRg3PB1vaOyL1_vMwFPCtHUdRpK9hAPdRPUBxFkDKbOTxYYDLa4taNlV0tJyqF6yO_H2APml2R9jwz3W8bS4xTwUPW5VSH3p4eCNJWml4bMQl9sgNUUqBP7AIeSEgIIg2z8X3_wdmS035xZPEz36cDpdMk4du-U99Apj2Utxg_luXhx4G5TzT8Iei73jw9hC_dl5BLP_8N7ps5bNvgT6wiPaHZRSw414Ii5tNY7QTY6L3sh7wHBfqIK-kLeEfWBwLRqILwhI6PQo52BUHSS7MmHij0h-q-feStUNqkSPQuVAhjSsxoX_YPF3JwWvsT8NgPsWEp8-IWQATyEfqe8oLMog3NH9dvByj5aysaCXZDcscRMLlmAOvZaK3GsG3ct1WGASPnHkZrcp1SozsdxmrBcyeCpDrCQ6GUcUCIk_t8eMZPpyYB6UfWJ6Dhgx9ZI9831VWV6G3Y-GOdvZ6SZQ_qnYEdnhJV12OmnIgFaUJS4O84WLobYpfx0_MWaBr0kNiEqItC5JV9ksZgdDK11rxtUeaJG-hNhiT45lvzv5J2IxAmgZ4ryTnd13gt2FtnluLwtcXH5wsjjBHQyeP52go_9E2lDkCir-X3OcnP7sOpcA399JnAcfLWVV5DWermwu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7425ddc2e6.mp4?token=arcr82_2d8z-45zIWNMModgd1apfVLPugnmEw2VPDRDRg3PB1vaOyL1_vMwFPCtHUdRpK9hAPdRPUBxFkDKbOTxYYDLa4taNlV0tJyqF6yO_H2APml2R9jwz3W8bS4xTwUPW5VSH3p4eCNJWml4bMQl9sgNUUqBP7AIeSEgIIg2z8X3_wdmS035xZPEz36cDpdMk4du-U99Apj2Utxg_luXhx4G5TzT8Iei73jw9hC_dl5BLP_8N7ps5bNvgT6wiPaHZRSw414Ii5tNY7QTY6L3sh7wHBfqIK-kLeEfWBwLRqILwhI6PQo52BUHSS7MmHij0h-q-feStUNqkSPQuVAhjSsxoX_YPF3JwWvsT8NgPsWEp8-IWQATyEfqe8oLMog3NH9dvByj5aysaCXZDcscRMLlmAOvZaK3GsG3ct1WGASPnHkZrcp1SozsdxmrBcyeCpDrCQ6GUcUCIk_t8eMZPpyYB6UfWJ6Dhgx9ZI9831VWV6G3Y-GOdvZ6SZQ_qnYEdnhJV12OmnIgFaUJS4O84WLobYpfx0_MWaBr0kNiEqItC5JV9ksZgdDK11rxtUeaJG-hNhiT45lvzv5J2IxAmgZ4ryTnd13gt2FtnluLwtcXH5wsjjBHQyeP52go_9E2lDkCir-X3OcnP7sOpcA399JnAcfLWVV5DWermwu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از آتش‌سوزی روز گذشته کوچه برلن
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/145698" target="_blank">📅 12:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145697">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY1eB6cPNPM2LEXRN7m-NUlmYNufX5yS5TA0oFfW9rkHcCWEckYvyhabm_mB0tpBJvF6xZfEdsAmgfXbiCnnsnEz1S0XYxeFaavBSbTCfWsr04FMeL03GITqXg3fzrl_MWLwhJQxap5Bspogv6iS9PsI0Fe7rH8WvV2qmcoCuU97K0N7ZivQJZLXBgaAZvSEosxPsqOAZD8nIpiWy4aMl9SwwhPOIaFWr4pdGWWNMeWPUZdlH5p6XJxUzMYGWW85FQUYpr7XUbDoaK79OpfWNVUCtETXswFTn4vTTAX7BdsBt58TXddOh5zrHxYF4d_8AQQP9IzUCktkBsDLbT8FEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی ایالات متحده به سرعت در حال بررسی گزینه‌های جایگزین برای هواپیماهای بدون سرنشین MQ9 است، زیرا گزارش‌ها نشان می‌دهند که این نیرو حدود 50 فروند از این هواپیماها را، معادل 25 درصد از کل، در جریان جنگ با ایران از دست داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145697" target="_blank">📅 12:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145696">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWudpCOJAKY0c1TYNuvZTYgJ3mpNBHmtJb7D9QWni7ekp1o2QI3fe4hXTOFXxuZRLjWHbP3pgeHcCbHbBWjViYELEJ6NkdDCpr7tyN6WRist61Mo_9Rl4Lggz2ynmC-5Fhv5xHA-lvj2W3gNC75YWhUotj0dM1_vGLknD2U3QuFpU_boNo9kZiHSKuXI5mSa8GO5WL4K5_gp8Lbyc-Elsdg6N0Wli4UOCLwg_P2YXDhHikROAOKQQLmnh8y3Kh3K8psZ6lWVH4x-MxP3U318tgAKpzBQl_Vzchn48TR-zCSQIj_sivp1lC_K1zOHwnpeUX8lN0hX1D1ui5aucIB3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رصدهای تانکر ترکرز نشان میدهد که دیروز روز بسیار شلوغی در  انتقال نفت خلیج‌فارس از تنگه هرمز بوده است ، ۲۴ میلیون بشکه نفت ، LNG و LPG با روش کشتی به کشتی در دریای عمان تحویل داده شدند. تانکرهای حامل نفت دیگری هم در دریای عمان رصد شده‌اند که در انتظار یک کشتی برای تخلیه بودند. همچنین حداقل ۷/۲۵ میلیون بشکه نفت به اضافه دو تانکر LNG در خلیج‌فارس در انتظار چراغ سبز سنتکام بودند تا با اسکورت آن‌ها از تنگه هرمز عبور کنند. در مجموع چیزی حدود ۴۰ میلیون بشکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/145696" target="_blank">📅 12:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145695">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ویتکاف و کوشنر، دو فرستاده رئیس‌جمهور آمریکا وارد مسکو شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/145695" target="_blank">📅 12:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145693">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=kulchPVVnd4dFbRyrVpCRkcG6JtPd9Q8vZucW73JOW6GQiJxSnoCPHW18nr8mnE10bTK56cWWakzi4TVInYhuPCSZ9TfuGdpr6zYu4gTJbOL-sX2nCd6jCED3vsiFwcCQlO20fvQkXpV1XeBE4SfcFLMF-IIypLi1SXmU46NvVDfk1rTamKe5c3RQDgyMGVo-hVClRd3jlTanB-4lv5HFAMZ1-hqp3zMAo6CW3X3GIWOo1CxzSXiNiBHu94gy5g2nGXdxkisMIk1892Xm3WdwHvjokQVN9jwYpfcUDpmiFNPRhmyA9lFuJNuJwqNPeQtsYANM1_N1VJCA1L-qHQ2dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=kulchPVVnd4dFbRyrVpCRkcG6JtPd9Q8vZucW73JOW6GQiJxSnoCPHW18nr8mnE10bTK56cWWakzi4TVInYhuPCSZ9TfuGdpr6zYu4gTJbOL-sX2nCd6jCED3vsiFwcCQlO20fvQkXpV1XeBE4SfcFLMF-IIypLi1SXmU46NvVDfk1rTamKe5c3RQDgyMGVo-hVClRd3jlTanB-4lv5HFAMZ1-hqp3zMAo6CW3X3GIWOo1CxzSXiNiBHu94gy5g2nGXdxkisMIk1892Xm3WdwHvjokQVN9jwYpfcUDpmiFNPRhmyA9lFuJNuJwqNPeQtsYANM1_N1VJCA1L-qHQ2dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از نفتکش هدف قرار گرفته توسط آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145693" target="_blank">📅 12:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145692">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سپاه: صدای انفجار در دماوند استان تهران مربوط به برنامه‌های رزمایشی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145692" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145691">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de9af4ecb.mp4?token=Z13bVTpBGDvLbrws6HPQrWVkedAkIw3tuULJ9G1szisVRqAEspndLz54cDF-y_osiqvjsCQdMj_UTN84I6ydGYhIOrZdoMxgXBkjWhHrTZBXHYPAwfbDqZYlM2D_SESW1C5SdjC3-ox7AcMm1x8_AuMq0yTIeKkzQKy89BTyi2_SaF0t25v9om_HCJxJAzPkQAoZ_L9Pa8sv-x4hOSqPpKf47x5NKztpG6YdfKkN9sPtUyXLj2mX1PdR0-KfA-5-0Aa_tMRroE-BJwl0gcnmh_Fg4eMIXFb7QsBUuK-f2f7hcywNFNcggdzhbqd8eVGARvRWeih30_Oh2pPzUj0g3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de9af4ecb.mp4?token=Z13bVTpBGDvLbrws6HPQrWVkedAkIw3tuULJ9G1szisVRqAEspndLz54cDF-y_osiqvjsCQdMj_UTN84I6ydGYhIOrZdoMxgXBkjWhHrTZBXHYPAwfbDqZYlM2D_SESW1C5SdjC3-ox7AcMm1x8_AuMq0yTIeKkzQKy89BTyi2_SaF0t25v9om_HCJxJAzPkQAoZ_L9Pa8sv-x4hOSqPpKf47x5NKztpG6YdfKkN9sPtUyXLj2mX1PdR0-KfA-5-0Aa_tMRroE-BJwl0gcnmh_Fg4eMIXFb7QsBUuK-f2f7hcywNFNcggdzhbqd8eVGARvRWeih30_Oh2pPzUj0g3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری‌هایی بین نیروهای مسلح یمن و نیروهای وفادار به عربستان سعودی در جنوب شهر حدیده در جریان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145691" target="_blank">📅 11:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145690">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری / فارس: دقایقی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارک شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145690" target="_blank">📅 11:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145689">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سخنگوی شورای نگهبان: طرح جدید مهریه در نوبت بررسی شورای نگهبان قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145689" target="_blank">📅 11:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145688">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145688" target="_blank">📅 11:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145687">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
راه آهن کشور اعلام کرد ترکمنستان و قزاقستان با تبعیت از تحریمهای جدید آمریکا مانع انتقال ریلی کالا از چین و روسیه به ایران شده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/145687" target="_blank">📅 11:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145686">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
خبرگزاری المعلومه: منابع امنیتی اعلام کردند روند خروج نیروهای آمریکایی از پایگاه هوایی الحریر در اقلیم کردستان ادامه دارد و انتظار می‌رود این پایگاه تا پیش از هشتم مهر ماه آینده به طور کامل تخلیه شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145686" target="_blank">📅 11:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145684">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
روحانی: الان مردم در تعیین سیاست‌ها و آینده هیچ نقشی ندارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145684" target="_blank">📅 11:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145683">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=OQNOJpszzSP39hVAm-5rFiob9GMgNmnWp1xjZ2KI2k4EfsDtaHigPCQlFESdVFJKjN5GtCa8HJq1-HNt5uJJpPHboGJ6CtImHvIxFcSdmghTIp_xUTDSThBRudP8EdaKl7rkXiA9uIL2noadp1A1KDY3j4toMz-qrK_DSawn99K65ESNCt4tVzsk2ioyi065fvvo8C0al-A_d0cEosDBmZJoXqQTvctQuMe8UczRhGzevFMhgFfMQ-Gc3Ggzya2QXAAHyFSTYOpPjUVGk6YTuwroSe26U_a4-_sTYCsD4F_m8JJ5nLbpVJV2sZFhjm0I-mJCJJKq-EoJnU_fnps15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=OQNOJpszzSP39hVAm-5rFiob9GMgNmnWp1xjZ2KI2k4EfsDtaHigPCQlFESdVFJKjN5GtCa8HJq1-HNt5uJJpPHboGJ6CtImHvIxFcSdmghTIp_xUTDSThBRudP8EdaKl7rkXiA9uIL2noadp1A1KDY3j4toMz-qrK_DSawn99K65ESNCt4tVzsk2ioyi065fvvo8C0al-A_d0cEosDBmZJoXqQTvctQuMe8UczRhGzevFMhgFfMQ-Gc3Ggzya2QXAAHyFSTYOpPjUVGk6YTuwroSe26U_a4-_sTYCsD4F_m8JJ5nLbpVJV2sZFhjm0I-mJCJJKq-EoJnU_fnps15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار 223000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/145683" target="_blank">📅 10:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145682">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وال‌استریت ژورنال: در بحبوحه افزایش تنش‌های تجاری میان آمریکا و کانادا، به بخش ضدانحصار وزارت دادگستری آمریکا برای مدت کوتاهی دستور داده شد همکاری با مقام‌های کانادایی را متوقف کند.
🔴
در یک ایمیل داخلی از کارکنان خواسته شده بود همکاری در پرونده‌های مشترک و تعاملات سیاست‌گذاری با کانادا را متوقف کنند؛ اما وزارت دادگستری بعداً اعلام کرد این دستور ناشی از یک سوءتفاهم بوده و دستور اولیه تنها مربوط به تعویق یک جلسه برنامه‌ریزی‌شده بوده است.
🔴
مقام صادرکننده این دستور بعداً آن را اصلاح کرد و به کارکنان اعلام شد که همکاری با کانادا می‌تواند ادامه پیدا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145682" target="_blank">📅 10:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145681">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سازمان غذا و دارو: واکسن آنفلوانزا از اواخر شهریور و اوایل مهر در دسترس قرار می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145681" target="_blank">📅 10:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145680">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رویترز: کاخ سفید گزینه‌هایی را برای جایگزینی استیو فاینبرگ، معاون وزیر دفاع آمریکا بررسی کرده است
🔴
با این حال، هنوز تصمیمی گرفته نشده و کاخ سفید و پنتاگون می‌گویند فاینبرگ در حال برکناری یا کنار گذاشته شدن نیست.
🔴
کناره‌گیری احتمالی او می‌تواند به موج اخیر تغییرات در رهبری پنتاگون اضافه شود؛ آن هم در شرایطی که نگرانی‌ها درباره کمبود تسلیحات و ظرفیت تولید مهمات افزایش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145680" target="_blank">📅 10:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145679">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
یورونیوز: نظرسنجی‌ها نشان می‌دهد سیاستمدار راست‌افراطی مارین لو پن در مسیر تبدیل شدن به رئیس‌جمهور بعدی فرانسه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145679" target="_blank">📅 10:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145678">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
بانک ترکیه: علیه تحریم‌های آمریکا اقدام قانونی خواهیم کرد
🔴
الجزیره اعلام کرد: پس از آنکه وزارت خزانه‌داری آمریکا بانک ترکیه‌ای «گلدن گلوبال» و دو نهاد زیرمجموعه آن را به بهانه ارتباط با ایران تحریم کرد، این بانک اعلام کرد که علیه این تحریم ها اقدام قانونی انجام خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145678" target="_blank">📅 10:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145677">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
طبق گزارش منابع محلی : نفتکش هدف قرار گرفته‌شده در جزیره خارک، یک نفتکش کوچک بوده است.
🔴
بر اساس این گزارش، این حادثه تلفات جانی نداشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145677" target="_blank">📅 10:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145676">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری / فارس: دقایقی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارک شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145676" target="_blank">📅 10:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145675">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری / فارس: دقایقی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارک شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145675" target="_blank">📅 10:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145674">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
تتلو: مردم منو فراموش کردن، چطور دلتون اومد؟ حتی اونایی که تو پلی لیستشون هستم هم فراموشم کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145674" target="_blank">📅 10:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145673">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4411422981.mp4?token=IZxvHTvceHmbdiV4W6yQUy4hf9NdK590WkYnfpKS46APjm1HLyQX4sLBLCdOq4WefC2juDytWwCyonFAaWEn0_9yPN0mwaxPV9b-oEb_seV5mfxy-KSDPE3CuR5umepV7E9JHWxp7W4PGCLjnzsNE7nW6c-I5c0vzVGhi4x97bY8c2EcY1A-SnRasvVtzqeKED63fErLnHGQL5KbKwWt5iumgW9ENKy90TnSl_yXBv-090vGMMFsi9iEvgfKc8c0ETN4-QSwWgDhYbRVD1UIPAMivovTI9zfL4_wvML9D6uvk5y1wdYKFu8JjHK5TGrsOlyuxSqG4uZc8ch_Wkey7jq-crsifaI_5a46mtlPxsnHEnTP3z6lS-s1ENlGA9X9i5I2DsdkiRNStTZy-vMoXxgRE4nYkEIBUnsyoach9v4fB2gWETbdfnLSYVO-RiR7fv90nBWvWlaTfAmmzJbm6FOCExpfhHJyqpjgBgJvRpHBT51750_i3AiUtSyXY2FE9F2fHwmSGb70nrA8GcX6s9HDESJCWmkphIlmWPaTlCypQS0aA2WBhmGpVDeIODTw12W7BPFXc_PhceTeN1p4MshDn0-srZjl7kqCvyvMPSBjn7Tg8Ga363_0r9Zpq2xNEghmL1RoqSELA7WMsZqkZlVS9fCayoJf-hCh6agLDiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4411422981.mp4?token=IZxvHTvceHmbdiV4W6yQUy4hf9NdK590WkYnfpKS46APjm1HLyQX4sLBLCdOq4WefC2juDytWwCyonFAaWEn0_9yPN0mwaxPV9b-oEb_seV5mfxy-KSDPE3CuR5umepV7E9JHWxp7W4PGCLjnzsNE7nW6c-I5c0vzVGhi4x97bY8c2EcY1A-SnRasvVtzqeKED63fErLnHGQL5KbKwWt5iumgW9ENKy90TnSl_yXBv-090vGMMFsi9iEvgfKc8c0ETN4-QSwWgDhYbRVD1UIPAMivovTI9zfL4_wvML9D6uvk5y1wdYKFu8JjHK5TGrsOlyuxSqG4uZc8ch_Wkey7jq-crsifaI_5a46mtlPxsnHEnTP3z6lS-s1ENlGA9X9i5I2DsdkiRNStTZy-vMoXxgRE4nYkEIBUnsyoach9v4fB2gWETbdfnLSYVO-RiR7fv90nBWvWlaTfAmmzJbm6FOCExpfhHJyqpjgBgJvRpHBT51750_i3AiUtSyXY2FE9F2fHwmSGb70nrA8GcX6s9HDESJCWmkphIlmWPaTlCypQS0aA2WBhmGpVDeIODTw12W7BPFXc_PhceTeN1p4MshDn0-srZjl7kqCvyvMPSBjn7Tg8Ga363_0r9Zpq2xNEghmL1RoqSELA7WMsZqkZlVS9fCayoJf-hCh6agLDiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سریع‌القلم: آمریکایی‌ها بعد از انتخابات کنگره به سراغ عملیات گسترده نظامی علیه ایران می‌آیند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145673" target="_blank">📅 09:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145672">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c9a950b3d.mp4?token=MMUbEqthlmssHXiQan_tnXvSmH2-SYF5ytSuXFyaCkEsGa0TSs3nyVui_rakiTE3NDOSM7ObKyyPphRiQEakh9qQaZvfutN4_L16KNnskhs-D29X7LbgFDtcZUKtNlPsQJ_cojxm9IW0DDi2uMtexuKnZAvbZejaeAqkseCMXKIs7fltHqmadE99CQmsez44jC1-1uOChbx2tV5KXgAbiF9LvQcsIP0eFWGzt05NTN_MwV0ncvBCzF5c18809UpCc0paVDS_ZBo2nMuxoqv4vgSzKCwI0CYwNmQO-8wvqxhXFqrRpb9HlULb9xDRW5zkZDNU7KdfDJSu-QnhuKa1nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c9a950b3d.mp4?token=MMUbEqthlmssHXiQan_tnXvSmH2-SYF5ytSuXFyaCkEsGa0TSs3nyVui_rakiTE3NDOSM7ObKyyPphRiQEakh9qQaZvfutN4_L16KNnskhs-D29X7LbgFDtcZUKtNlPsQJ_cojxm9IW0DDi2uMtexuKnZAvbZejaeAqkseCMXKIs7fltHqmadE99CQmsez44jC1-1uOChbx2tV5KXgAbiF9LvQcsIP0eFWGzt05NTN_MwV0ncvBCzF5c18809UpCc0paVDS_ZBo2nMuxoqv4vgSzKCwI0CYwNmQO-8wvqxhXFqrRpb9HlULb9xDRW5zkZDNU7KdfDJSu-QnhuKa1nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در پی سیل‌های ناشی از طوفان به جنوب چین، خانه‌ها زیر باران‌های سیل‌آسا تخریب می شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145672" target="_blank">📅 09:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145671">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
یک نماینده کنگره آمریکا: اگر درگیری با ایران پیش از انتخابات میان دوره‌ای پایان نیابد، آمریکا در معرض گرفتار شدن در «یک جنگ بی‌پایان دیگر» قرار می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/145671" target="_blank">📅 09:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145670">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
مکرون خواهان آتش بس در جنوب لبنان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145670" target="_blank">📅 09:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145669">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
رئیس‌جمهور چین، قصد دارد در سفر آتی خود به واشنگتن، هیأتی بزرگ از مدیران و فعالان اقتصادی این کشور را همراه خود ببرد؛ اقدامی کم‌سابقه که در بحبوحه تنش‌های اقتصادی میان پکن و واشنگتن انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145669" target="_blank">📅 09:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145668">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bd7d8bb1c6.mp4?token=E2VNHs_PjkvjQdoAFWvZFP3apseXvzlBI5A6AmgRkJZyarxEDBqqsRfKJsmUjQeZRMvRlIRpZACxhcg7Yr_YdnPv0GKgF7HhJg-7xg3qWJXNpnuMIb25iAXqOQO5W-3LPI-PQ_gxRYCJXLQxL5Ke2CGS3klWCv2zW-fMSJx8SJgSWdTsgXxgYN9mo4ModJQWodkq9YQ6F_yA7kS-Z18CjjGaBo8xFvYceWcV_FRB_pR7Aub_1oEJzR48I2E3dMrnNDcqxCfiDTkjDhQ6vMARh7mFvefZnBQkgKF4di13aQ6zVrhH2h4ILQI1M0gsX2NQCJIDxG9lykgsPHELW6zppA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bd7d8bb1c6.mp4?token=E2VNHs_PjkvjQdoAFWvZFP3apseXvzlBI5A6AmgRkJZyarxEDBqqsRfKJsmUjQeZRMvRlIRpZACxhcg7Yr_YdnPv0GKgF7HhJg-7xg3qWJXNpnuMIb25iAXqOQO5W-3LPI-PQ_gxRYCJXLQxL5Ke2CGS3klWCv2zW-fMSJx8SJgSWdTsgXxgYN9mo4ModJQWodkq9YQ6F_yA7kS-Z18CjjGaBo8xFvYceWcV_FRB_pR7Aub_1oEJzR48I2E3dMrnNDcqxCfiDTkjDhQ6vMARh7mFvefZnBQkgKF4di13aQ6zVrhH2h4ILQI1M0gsX2NQCJIDxG9lykgsPHELW6zppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رانش زمین، رودخانه‌ای در نپال را مسدود کرد
🔴
رانش زمین گسترده در منطقه «آپی هیمال» در شهرستان دارچولا در غرب نپال، بخشی از رودخانه چاولانی را مسدود کرده و نگرانی‌ها درباره وقوع سیلاب ناگهانی در مناطق پایین‌دست را افزایش داده است.
🔴
مقام‌های محلی از ساکنان حاشیه رودخانه خواسته‌اند در حالت آماده‌باش باشند، زیرا ادامه رانش زمین می‌تواند مسیر رودخانه را به‌طور کامل مسدود و در صورت شکسته شدن این انسداد، موج ناگهانی آب ایجاد کند.
🔴
گزارش‌ها حاکی است جریان آب در حال عبور دوباره از میان توده رانش‌کرده است و این حادثه ارتباطی با فاجعه بزرگ سیلابی اخیر در دیگر مناطق نپال ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145668" target="_blank">📅 09:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145667">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نیویورک پست: تا دو ماه دیگر ذخایر سوخت ایران جوابگوی نیاز درون ایران است
🔴
۳ حالت پیش رو است:
🔴
۱-سهمیه بندی شدید
🔴
۲- گران کردن بنزین
🔴
۳-بازار چند نرخی
🔴
(با محاصره اقتصادی٫ برای کسری بنزین از ترکیه و امارات و ونزوئلا سوخت وارد نمی‌شود،  روسیه نیز خود کمبود بنزین دارد)
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/145667" target="_blank">📅 09:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145666">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1a3ab30eb.mp4?token=pTMs1mxwvm37hK1bMb2sRRtpyGUYaPBSCQQXmRTyZOydteuQtPzAeNzJRySbGokOxvrd0Crm-4kBdTnmeb8mvS5MeIbDRXGo1qUyIgfenTAYBGSVK4yCeTzJcxlheXaseJG7y7Ezr9RCIgHlxL3KauUpd8x-h2SMsgxS3TzPYwWorxkT5A75jsBXNYC3YrYqYlTVeJ6g6tCfLaXYYAE-1YPEbK15Yr9tdh7qUM6WAXlfrIOAogJFxi860wJ92ZFHuGW2j0XnEvlo6Jt7_jrHQvhDo2fIxdTyUhQM_3F-7oCUEOXgLN6oXv_aoaQzYojDuUY0H_PzWgoftjFtUo1Jwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1a3ab30eb.mp4?token=pTMs1mxwvm37hK1bMb2sRRtpyGUYaPBSCQQXmRTyZOydteuQtPzAeNzJRySbGokOxvrd0Crm-4kBdTnmeb8mvS5MeIbDRXGo1qUyIgfenTAYBGSVK4yCeTzJcxlheXaseJG7y7Ezr9RCIgHlxL3KauUpd8x-h2SMsgxS3TzPYwWorxkT5A75jsBXNYC3YrYqYlTVeJ6g6tCfLaXYYAE-1YPEbK15Yr9tdh7qUM6WAXlfrIOAogJFxi860wJ92ZFHuGW2j0XnEvlo6Jt7_jrHQvhDo2fIxdTyUhQM_3F-7oCUEOXgLN6oXv_aoaQzYojDuUY0H_PzWgoftjFtUo1Jwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امارات به لنج‌های ایرانی اجازه بارگیری نمیدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/145666" target="_blank">📅 08:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145665">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
تانکرترکرز: ۷ میلیون بشکه نفت آماده عبور از هرمز با حفاظت آمریکا است
🔴
داده‌های کشتیرانی TankerTrackers مدعی است تانکرهای حامل حدود ۷ میلیون بشکه نفت و گاز در آستانه عبور از تنگه هرمز تحت حفاظت ایالات متحده قرار دارند.
🔴
این مجموعه همچنین اعلام کرده روز گذشته ۱۷ مورد انتقال کشتی‌به‌کشتی نفت و گاز در خلیج عمان شناسایی کرده که حجم محموله‌های آنها در مجموع به حدود ۲۴ میلیون بشکه می‌رسد.
🔴
این ارقام نشان می‌دهد با وجود ریسک‌های امنیتی، تلاش برای حفظ جریان صادرات انرژی از مسیر هرمز همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/145665" target="_blank">📅 08:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145664">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از منابع مطلع:
بازجویی از حدود 50 عضو ستاد مشترک ارتش در رابطه با افشای اطلاعات به رسانه‌ها درباره جنگ ايران.
🔴
این تحقیقات با نظامیان بر نشت اطلاعات مربوط به کاهش ذخایر مهمات حیاتی ارتش متمرکز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/145664" target="_blank">📅 08:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145663">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=kh33Wvnh1wC3oHMgdhAneeO3f8GaI7rgrO4CpA-EVfSXK75QFHpOF8Ffoh0wIKIftBbO7PQOf927R1JzHdsJOH-YBSJqRFeJEH5tnr_hI2PscQb8CPkF9dHF03cc1OaGPcnaH4xTnisfgF-LNzwVmHFptNojlQHUdmnv6lCgaz04EGLuaIMS47Lz8KkHeop3B2Wy83qb5UTu7hdISp0G51drnnPBrYDqF6aqBu0_qVCPx7MbUio-JGmPyBPZ3CNUc4NhMB25m7qVGUSN-wbocLyFg0GquvufYbC-wIZpc3dXmcPFznmzrpES8Q4voOEzIFNkxyH5LdzbWv4RJhz4Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=kh33Wvnh1wC3oHMgdhAneeO3f8GaI7rgrO4CpA-EVfSXK75QFHpOF8Ffoh0wIKIftBbO7PQOf927R1JzHdsJOH-YBSJqRFeJEH5tnr_hI2PscQb8CPkF9dHF03cc1OaGPcnaH4xTnisfgF-LNzwVmHFptNojlQHUdmnv6lCgaz04EGLuaIMS47Lz8KkHeop3B2Wy83qb5UTu7hdISp0G51drnnPBrYDqF6aqBu0_qVCPx7MbUio-JGmPyBPZ3CNUc4NhMB25m7qVGUSN-wbocLyFg0GquvufYbC-wIZpc3dXmcPFznmzrpES8Q4voOEzIFNkxyH5LdzbWv4RJhz4Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون وزارت ارتباطات :
حتی اگه جنگ بشه هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/145663" target="_blank">📅 08:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145662">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
کپلر: کشتی الغشامیه که حامل گاز طبیعی مایع بود و در کریدور جنوبی تنگه هرمز، تحت اسکورت آمریکا حرکت می‌کرد، از ادامه عبور انصراف داد
🔴
بر اساس داده‌های رهگیری کشتی‌ها از شرکت تحلیل کپلر که در اواخر مرداد ماه منتشر شد، کشتی الغشامیه به همراه چهار نفتکش دیگر حامل محموله‌های LNG از تأسیسات صادراتی رأس لفان قطر، به سمت شرق و تنگه هرمز در حرکت بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/145662" target="_blank">📅 08:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145661">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c61211abd.mp4?token=UY2q1D-ebvIDJ0paPzkdO0MuN06NvEhnqw8a_brK3M_Xm9MSVXUa9uQMX1NBNFQCWu8WpAZI-6XgMS9uNY2tS8tCTBW2Ko1ZHQOtN1AFUHx6cBB13tNq2JmJKshdwUfPiMhusSW1DaJ5sm1SlCsvXJ6wwRK3KUtfwJr-HW4v8dYHUZ9hj23qNUmXmEkG92LqWwpxagjrKfb5I5rgpL6QdQDOS7s8unIxUE77PaIVaNafOf65NQTzRECUa156GrXIhVEvHCaXgq5u6QA0zKspB-vF7HIZPCwE9b2PtDCNCbiw3craySyZcWZtwjTc1KeTmObVNOMXJhLAaY9Hh2KmDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c61211abd.mp4?token=UY2q1D-ebvIDJ0paPzkdO0MuN06NvEhnqw8a_brK3M_Xm9MSVXUa9uQMX1NBNFQCWu8WpAZI-6XgMS9uNY2tS8tCTBW2Ko1ZHQOtN1AFUHx6cBB13tNq2JmJKshdwUfPiMhusSW1DaJ5sm1SlCsvXJ6wwRK3KUtfwJr-HW4v8dYHUZ9hj23qNUmXmEkG92LqWwpxagjrKfb5I5rgpL6QdQDOS7s8unIxUE77PaIVaNafOf65NQTzRECUa156GrXIhVEvHCaXgq5u6QA0zKspB-vF7HIZPCwE9b2PtDCNCbiw3craySyZcWZtwjTc1KeTmObVNOMXJhLAaY9Hh2KmDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از منطقه میفادون، جنوب لبنان، پس از حملات سنگین اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/145661" target="_blank">📅 08:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145660">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a9c103ed7.mp4?token=cqKstRQjFN5h3vnztEJtudiOip1uTcW9FNam-xzwBAVBm6IZKwQjc2_V4DOtuiKDqoJOJ1p0JeJUJ00d9QSLf-g4gCLuUdwcvUCSf_ptKbl4SqfNp4XskAay1pjB-Wba26UOAkktcw6HKEi0wKM2UggellxGRKpul2TzFhvCFiP9Zvq1FLB7heWhcVoJO-A9FfiERSrF8Joc4V3A55XqA4e-4zoj_yHRh81EiG1vfNetOMq0H72GUQLdVIHC8LMcxqRmh0kkX25fI-TI1UjJCZEcLSMfZZpy3q-Dvq_cq2s_9OEmC3gx_O_De_ESoEC_HrJR8dWFwOXHzSg7AqOwag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a9c103ed7.mp4?token=cqKstRQjFN5h3vnztEJtudiOip1uTcW9FNam-xzwBAVBm6IZKwQjc2_V4DOtuiKDqoJOJ1p0JeJUJ00d9QSLf-g4gCLuUdwcvUCSf_ptKbl4SqfNp4XskAay1pjB-Wba26UOAkktcw6HKEi0wKM2UggellxGRKpul2TzFhvCFiP9Zvq1FLB7heWhcVoJO-A9FfiERSrF8Joc4V3A55XqA4e-4zoj_yHRh81EiG1vfNetOMq0H72GUQLdVIHC8LMcxqRmh0kkX25fI-TI1UjJCZEcLSMfZZpy3q-Dvq_cq2s_9OEmC3gx_O_De_ESoEC_HrJR8dWFwOXHzSg7AqOwag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روحانی: اگر قرار است با قدرت‌های جهانی ۲۰ سال دیگر بجنگیم، باید قبلش از مردم بپرسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145660" target="_blank">📅 08:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145659">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f34f2cc3.mp4?token=LuFi2iXEPuplMtYx4NGqpqnbBqmjPuIhQeFot9TuejkppxuMDL_NoaYtC63EVd0I1LT8W_DXwIEA-_9arOL-1ziSMl-Vad4Jqg7ZDy7r8ZqwbtGSMmpXbYxLsqb1rkF6ZJ_CZhs3isB0djwv0LBbEgj2N-9pI7F-ZZMQO5Fcyu7mUKRM0Nx9KAUCIARymXJtePlrHjglSlZJSyW89JVWs8tTtjMk8KOZsC-CumbjkH3VI-H7hF1ZABSJbQCf5chzDWyReiB4WxlSxWeMch2mC4SNz8ngYx2HUESleqwU4i7Ber-VmDON9WAeHzlwh5ZB7WZ9vFEH8rC8_8uJzKiuEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f34f2cc3.mp4?token=LuFi2iXEPuplMtYx4NGqpqnbBqmjPuIhQeFot9TuejkppxuMDL_NoaYtC63EVd0I1LT8W_DXwIEA-_9arOL-1ziSMl-Vad4Jqg7ZDy7r8ZqwbtGSMmpXbYxLsqb1rkF6ZJ_CZhs3isB0djwv0LBbEgj2N-9pI7F-ZZMQO5Fcyu7mUKRM0Nx9KAUCIARymXJtePlrHjglSlZJSyW89JVWs8tTtjMk8KOZsC-CumbjkH3VI-H7hF1ZABSJbQCf5chzDWyReiB4WxlSxWeMch2mC4SNz8ngYx2HUESleqwU4i7Ber-VmDON9WAeHzlwh5ZB7WZ9vFEH8rC8_8uJzKiuEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موتور نیسان پاترول 2026 تو حالت عادی ۵۰ سال بدون مشکل کار میکنه و باز نمیشه
🔴
بنزین بی کیفیت باعث شد ۷۰ میلیارد تومن ماشین، سوپاپش ذوب بشه و موتورش بیاد پایین!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/145659" target="_blank">📅 07:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145658">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/145658" target="_blank">📅 01:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145657">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpdzuqHqNrLadSqEoHVTMoxuC8PTz023InJL9pO7YYBkFJeX7sOeCu_CmLrDFI-YrrqrrPWJTxQ5C_Ard56RL4BOJlAMQ9brJ1vpSuIRZ09ngKCygMOO4YctknPsEHJk0rgDRVOfTVnnsFpKVFXMYrqYU3YKKlMhrc4EH674p4fas_Iv5Q6_H2fFEXxJbK7uJdvJkv9ec-VUdv1Qo2-EPfRkKTwvEJy1AzKCO3m3zsgnLsoM-1ZO5xD07EGQfwP-eMwHdczKn7iLWRn95XotAEahOeBlKzxXrOFXzCCmIrn4Noi5fm6Osw55uYtrEPrfIiy1BjtxEU8q2JZWW8CMrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
اگه اجازه بدن من فردا عازم لبنان میشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/145657" target="_blank">📅 01:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145655">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=Dk2afqOEOzZ9FmI9-Pk7JP_pfI9FBpIsM-S9Z9yPYZsHAzZ71q1pRNA7KJSWgFiCa3vEz0vMR76Zb3lhDu1LIBWyFnnMpm1q7_vjx8pEEhiG5tePnzcjRginCf0WcBBrSgNksihE5Zln_Kzn8VkPV5BnD-9jLkGEqoGNh4mKtSuvu3UAqvUQgIcbw_Qc_agsxNzown2Un1OJmpLjrGaakd7DwgGg_zxWZQ_xSbc6ZrOtoXeYWZ1G8YuFdsIOiqnYcRB7KZUZflKtNxiBFHngnIbUVvYtLz-0zlxWEB7gtiW3TNSttMq7BTpoxq4Ip_JLhSW3MU9T4V_P_7TCLN04Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=Dk2afqOEOzZ9FmI9-Pk7JP_pfI9FBpIsM-S9Z9yPYZsHAzZ71q1pRNA7KJSWgFiCa3vEz0vMR76Zb3lhDu1LIBWyFnnMpm1q7_vjx8pEEhiG5tePnzcjRginCf0WcBBrSgNksihE5Zln_Kzn8VkPV5BnD-9jLkGEqoGNh4mKtSuvu3UAqvUQgIcbw_Qc_agsxNzown2Un1OJmpLjrGaakd7DwgGg_zxWZQ_xSbc6ZrOtoXeYWZ1G8YuFdsIOiqnYcRB7KZUZflKtNxiBFHngnIbUVvYtLz-0zlxWEB7gtiW3TNSttMq7BTpoxq4Ip_JLhSW3MU9T4V_P_7TCLN04Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
معاون وزارت ارتباطات :
حتی اگه جنگ بشه هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/145655" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145654">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
نتانیاهو: جمهوری اسلامی سقوط میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/145654" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145653">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">خواستیم روزیمان حلال باشد
جوانیمان حرام شد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/alonews/145653" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145652">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فعالیت پدافند هوایی اسلامشهر تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/145652" target="_blank">📅 00:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxIebNQYTgd1XvqjoMlyseNzLKaQNyC6KX8BsOhfns0QfAebAzBOzdlwtiOUSU3AQ3YQUm1y5nX-qvgpPcVbeHdjnBchB04QOIuy2q2K07_Dyw3A8c9nOHRHDhiPef2cxiduJuC91LK5et4bCGMKEHH6rduJ2_5h_X1L-u8gAlO9xsKx_RAEhn0YiEJTV-H6Mhv-FgATKqUurXknFY-JfZHe98LqOW61mFFkU22LFt_hDHd9UTHZO57DOkVVCRRcOH5OQUpPrvskh8tzcXjVFVxZj1F3faspfjaUqRbMs0CsLVyifpSWsyDDZ5H3NlZU24gi3dBcWkeJjwblSCBsng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
این وسط گروه هکری عدل علی تصاویر برهنه و منشوری مسیح علینژاد رو منتشر کرد
😐
😐
😐
😐
😐
🚨
مشاهده فوری عکس‌ها</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/alonews/145651" target="_blank">📅 00:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145650">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=HVnBknBIgrQUKzfeyfW6mBa1tFRdvwEygc9PzBwqbI_jLxIvhjXfin8mjIn533_nfmAykURakmd23iCrkT-6teexb3qhWR0MI_D-n116VWA5ufygHQoy8Am8JdQsyrmj-lFwG6VwTC0MrThoEoE5w9YVYnKntnU4VnoqjtFXcwVVVp57bZIcnjgKfawVghpqI4_rxy8FHMRUgJKAaGR__lJTt974O1B9sZ8qTJg3d9-PB5edocU2otZNSHpsNvMhLVvuICf4ntkO0JAn-egQ31Ugg1665h00201QBBVow2-tcAr3url2-pujfrkh6ty-f76eVHmCopoc-ToABg535Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=HVnBknBIgrQUKzfeyfW6mBa1tFRdvwEygc9PzBwqbI_jLxIvhjXfin8mjIn533_nfmAykURakmd23iCrkT-6teexb3qhWR0MI_D-n116VWA5ufygHQoy8Am8JdQsyrmj-lFwG6VwTC0MrThoEoE5w9YVYnKntnU4VnoqjtFXcwVVVp57bZIcnjgKfawVghpqI4_rxy8FHMRUgJKAaGR__lJTt974O1B9sZ8qTJg3d9-PB5edocU2otZNSHpsNvMhLVvuICf4ntkO0JAn-egQ31Ugg1665h00201QBBVow2-tcAr3url2-pujfrkh6ty-f76eVHmCopoc-ToABg535Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری شبکه خبر:
گازوئیل ۳سنت تو آمریکا گرون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/alonews/145650" target="_blank">📅 00:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ارتش اسرائیل: نبطیه(از شهرهای حزب الله) را هم بزودی تصرف میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/alonews/145649" target="_blank">📅 00:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بچه‌ها این گردونه صراف رو چک کنید، من الان شانسی زدم ۵ دلار بهم داد
😐
😂
انگار اصلاً پوچ نداره و به همه یه چیزی میده.
برید بچرخونید ببینید شانس شما چیه
👇
https://r.saraf.app/s/agrd277</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/alonews/145648" target="_blank">📅 00:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145647">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ارتش اسرائیل: پهپادی را که حزب‌الله به سمت نیروهایمان در منطقه امنیتی پرتاب کرد رهگیری کردیم و هم‌اکنون با حملاتی پاسخ می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/alonews/145647" target="_blank">📅 00:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا روز جمعه اعلام کرد که فروش احتمالی مهمات تهاجمی با برد افزایش یافته به عربستان سعودی به ارزش تقریبی ۵ میلیارد دلار را تأیید کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/alonews/145646" target="_blank">📅 00:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/945968d3e7.mp4?token=oZGa_KcIG6Ns-Fu60LuTQdKAN-ETNTXF3d2oIUJKS6gfZMQQ5QiaxS3EOOYVjmrAgqP18Tn4nOjS_FKfJ1eHyRtPegQdrPOtijT3Ts0hUra-ydL_k2z-z2Fs-luL33jkqkD0IDP8aimKpNpvIF7Ph9bJX9UgFk4CpWB6soUG5Y8wsswFJIclG-Ymfm16moftnCYe0Poth9N4BqhcG2J6vwZ5GjRM8ksX8afU87v5lF41W0RTcLDwqWi3I069rmITl6beMBPuCcQ-ACPXTA_BLTUffHOAzQ-EDNSnCZQBykKBVuCqaGny7hEQpTGwF7q1nQKRid0Pwmig-NjLGS0jTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/945968d3e7.mp4?token=oZGa_KcIG6Ns-Fu60LuTQdKAN-ETNTXF3d2oIUJKS6gfZMQQ5QiaxS3EOOYVjmrAgqP18Tn4nOjS_FKfJ1eHyRtPegQdrPOtijT3Ts0hUra-ydL_k2z-z2Fs-luL33jkqkD0IDP8aimKpNpvIF7Ph9bJX9UgFk4CpWB6soUG5Y8wsswFJIclG-Ymfm16moftnCYe0Poth9N4BqhcG2J6vwZ5GjRM8ksX8afU87v5lF41W0RTcLDwqWi3I069rmITl6beMBPuCcQ-ACPXTA_BLTUffHOAzQ-EDNSnCZQBykKBVuCqaGny7hEQpTGwF7q1nQKRid0Pwmig-NjLGS0jTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: مردم آمریکا چه زمانی باید منتظر حل‌وفصل مسئله ایران باشند؟
🔴
ترامپ: چی؟ انقلاب؟
🔴
خبرنگار: منظورم حل‌وفصل بود.
🔴
ترامپ: فکر کردم میگی «انقلاب» جالب‌تر بود. حل‌وفصل؟ نمی‌دونم
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/145645" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
فرزند سردار تنگسیری: تاکید می‌کنم امکان ندارد بتوانند تنگه هرمز را به صورت نظامی باز کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/145644" target="_blank">📅 23:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
المیادین به نقل از مقام ارشد ایرانی: به کره جنوبی هشدار می‌دهیم که هرگونه مشارکت این کشور علیه ایران در تنگه هرمز را به منزله مشارکت نظامی در تجاوز تلقی خواهیم کرد
🔴
سئول منافع و اعتبار خود را فدای سیاست‌های بی‌ثبات‌کننده آمریکا نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/145643" target="_blank">📅 23:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145642">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
اعرافی، امام جمعه قم: آمریکا با روش‌های جدید جنگ نامتقارن و چریکی جمهوری اسلامی آشنا نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/145642" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145641">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c61211abd.mp4?token=rN6Vs00zhEXirDf5Z2Z2VpeDoK27HwUlpOQ1Ibl2j1KLRBXivKfO9-wXITE6p2Zf336U2BibaUJ5t49-abTmmH54EpyQTcokPyNEUCd4Ownl5EPh0oQ4DqafR0gC8KZsbAyVAJOBFiiElvUWlGfiZhB2ZpWUyf4HQ9iBOLA4prBLhhH_MO7riUynEYOgltNOBaXAwxYxXPw52YSPF5Ywkry53oW7sdmnnFL39V-1vR__v2R8dlLpC8U3SbRCNxP4LMh8LOk4cbrMMfvg3kNlZ7DO20XfhrJF20UXaPWE9cMP8v4BlEqcxNg8-kg7DEuhbFzUpCd7hXDYIqwTfHvJKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c61211abd.mp4?token=rN6Vs00zhEXirDf5Z2Z2VpeDoK27HwUlpOQ1Ibl2j1KLRBXivKfO9-wXITE6p2Zf336U2BibaUJ5t49-abTmmH54EpyQTcokPyNEUCd4Ownl5EPh0oQ4DqafR0gC8KZsbAyVAJOBFiiElvUWlGfiZhB2ZpWUyf4HQ9iBOLA4prBLhhH_MO7riUynEYOgltNOBaXAwxYxXPw52YSPF5Ywkry53oW7sdmnnFL39V-1vR__v2R8dlLpC8U3SbRCNxP4LMh8LOk4cbrMMfvg3kNlZ7DO20XfhrJF20UXaPWE9cMP8v4BlEqcxNg8-kg7DEuhbFzUpCd7hXDYIqwTfHvJKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از منطقه میفادون، جنوب لبنان، پس از حمله اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/145641" target="_blank">📅 23:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145640">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4plMtd9lJ8t5-w8QzvusW4-NhLhQj2tbhTZn22BmV50M6am5PRAPQlmHpyEitzEux8x1HeT6y4os_VLGDKVyAriKb-MiVi3dgDQJvr4_5Hgo31oCGDfV6zaa2E4xGciBvYBf_H2jCmPUPrsp8GwwBcjvmvFek67P3W51oy59f76zEkoRmJOjhS-QoLaNtEr02ltG190PJQLzGYoZ1DyZLbAvquH2TbtVhXvZhZR3KgaYTbuWyJ-EOQ3uHoPbG8TBVLKFjjrqm5OfJl2NtEbrv1y4NueZ8lqIvIoWQhNUz7jTX598h_2yuVi61YR4xMLOay-D5moLbUMmgysSbxHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایید حمله پیشدستانه ایران توسط رئیس کمیسیون امنیت ملی
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/145640" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145638">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
پولتیکو: ترامپ قصد دارد به‌طور گسترده برای جمهوری‌خواهان کارزار انتخاباتی به راه بیندازد، اما نامزد‌ها نگران‌اند که حضور او شانس انتخاباتی آنها را کاهش دهد
🔴
برخی از این نامزد‌ها در گفت‌و‌گو‌های خصوصی به تیم ترامپ گفته‌اند که به حوزه‌های انتخابیه آنها نیاید
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/145638" target="_blank">📅 23:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145637">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ درباره کانادا: اگه ما نمی‌خواستیم با کانادا تجارت کنیم... فکر نمی‌کنم کانادا اصلاً وجود داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/alonews/145637" target="_blank">📅 22:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145636">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ: اگه می‌خواید به‌عنوان یک ایالت ثروتمند بشید، باید برید سراغ مرکزهای داده.
🔴
اگه می‌خواید با فقر و جرم‌وجنایت دست‌وپنجه نرم کنید، به نظرم مرکزهای داده رو تأیید نکنید.
🔴
خب، انتخاب با خودتونه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/145636" target="_blank">📅 22:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145635">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
دونالد ترامپ درباره جنگ اوکراین گفت: «در مسئله روسیه و اوکراین یک مشکل شخصیتی وجود دارد. زلنسکی و پوتین واقعاً از یکدیگر متنفرند؛ نفرت شدیدی میان آن‌ها وجود دارد.»
🔴
او افزود: «این نفرت در مسیر حل‌وفصل مسائل میان آن‌ها مانع ایجاد کرده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/145635" target="_blank">📅 22:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145634">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ در مورد تنگه هرمز: در حال حاضر، خطوط لوله در حال ساخت هستند. جاده‌ای از طریق سوریه در حال ساخته شدن است؛ در واقع، این جاده باز است. مردم با کامیون‌های بزرگ حامل نفت از طریق سوریه تردد می‌کنند.
🔴
تلاش‌های زیادی برای ایجاد جایگزین‌هایی برای تنگه هرمز در حال انجام است.
🔴
تنگه هرمز دیگر آن‌طور که قبلاً بود، نیست.
🔴
ایران، اگر نتواند عاقلانه عمل کند، که من نمی‌دانم آیا آن‌ها قادر به این کار هستند یا خیر، در نهایت به تنگه‌ای به نام هرمز دست پیدا خواهد کرد که دیگر آن اهمیت قبلی را نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/145634" target="_blank">📅 22:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145633">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران گفت: «به شی جین‌پینگ گفتم لطفاً در موضوع ایران دخالت نکنید.»
🔴
او افزود: «چین واقعاً درگیر این موضوع نیست و دخالت بسیار کمی دارد؛ در حالی که می‌توانست نقش و دخالت بسیار بیشتری داشته باشد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/145633" target="_blank">📅 22:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145632">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها رادار نصب کردند، زیرا ما قبلاً آن را از کار انداخته بودیم. حالا ما آن را برای بار دوم از کار انداخته‌ایم. اکنون ما هیچ فعالیتی را مشاهده نمی‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/145632" target="_blank">📅 22:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145630">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ درباره روسیه: ویتکاف و کوشنر پیشنهادی را برای پایان دادن به جنگ به مسکو ارائه می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/145630" target="_blank">📅 22:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145629">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ: هشت جنگ را پایان دادم، اما جایزه نوبل را به من ندادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/145629" target="_blank">📅 22:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145628">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ: هر یک از بخش‌های مهم این کشور که ما برای آنها هزینه می‌کنیم، حدود ۶۵۰ میلیارد دلار هزینه دارد.
🔴
ما باید به سطح ۱ درصد برسیم؛ نباید به سطح ۴ درصد برسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/145628" target="_blank">📅 22:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145627">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خبرنگار: ۱۸ نفر در جنگ با ایران جان خود را از دست داده‌اند. ما شاهد حضور نیروهای نظامی برای مدت زمان بی‌سابقه‌ای بوده‌ایم.
🔴
ترامپ: بی سابقه؟ مگه نمیدونی ما چه مدت در ویتنام حضور داشتیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/145627" target="_blank">📅 22:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145626">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68db4c2c5.mp4?token=L3gdl4Vbkvqyv2FWfcBvVymZqE2wLxRfGuZmRbB-Q5ethmGxG20BZ5V2-QW5taQtm8XIRpnUnseWL8S4lyYGHC6VLzmzdQPl4RTn7qo0wh0xwFogEPxiVhtgqjlxFs4bCVZzFkgT_d4vL22QjNasFyYwJgd25D2hj0_XOi8R-F6gee2EiDwUOiJFnW6_e7DlsmQZCjS_-QCyjnFf5vJbPQuJLWLDjibO3KkBhrmNknuEJXDOOmgdbTdUMdvu43LUY3T0niNde426CI9zWGk6df088wzoP-cG7slYr89uMkr9GxA13SnazeKDalM-YL8oEbVxEKRKEVYiRzyDckCa5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68db4c2c5.mp4?token=L3gdl4Vbkvqyv2FWfcBvVymZqE2wLxRfGuZmRbB-Q5ethmGxG20BZ5V2-QW5taQtm8XIRpnUnseWL8S4lyYGHC6VLzmzdQPl4RTn7qo0wh0xwFogEPxiVhtgqjlxFs4bCVZzFkgT_d4vL22QjNasFyYwJgd25D2hj0_XOi8R-F6gee2EiDwUOiJFnW6_e7DlsmQZCjS_-QCyjnFf5vJbPQuJLWLDjibO3KkBhrmNknuEJXDOOmgdbTdUMdvu43LUY3T0niNde426CI9zWGk6df088wzoP-cG7slYr89uMkr9GxA13SnazeKDalM-YL8oEbVxEKRKEVYiRzyDckCa5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره پوتین: من با پوتین صحبت می‌کنم؛ من او را خیلی خوب می‌شناسم. پوتین قصد حمله به خاک کشورهای عضو ناتو را ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/145626" target="_blank">📅 22:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145625">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18d6d722f3.mp4?token=SqbaW6HczeYgmukkYtXLhvupFQ-98KTAHYJZbaFjo6_WQliZvYGSirtk5jbSriCB5psOqJuJIbXHzN9rDwea08jOBp1Tzq90ggSSkiOcGOI-BrXFTOsOBYGhwIe55aoUyFfsT8qcIZ2xmFnZu7ajNA-GuA2KTWwisDjYo9eM_2j511Spo1psZYcHJkUAMYGxJGy1ibRqK18ToncmO3y52ar3078QxelvF4oaiXZkYzWitt5pPf5ZeJkppSYo3fJJcqyo_ya1Lmokghs0Jv9nppLUulbZd1cs_3HLjsdgmjpVQsp8GwrYx1ulOZ9D1DoQ2a5EqhJssO0VyIRQQSBQWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18d6d722f3.mp4?token=SqbaW6HczeYgmukkYtXLhvupFQ-98KTAHYJZbaFjo6_WQliZvYGSirtk5jbSriCB5psOqJuJIbXHzN9rDwea08jOBp1Tzq90ggSSkiOcGOI-BrXFTOsOBYGhwIe55aoUyFfsT8qcIZ2xmFnZu7ajNA-GuA2KTWwisDjYo9eM_2j511Spo1psZYcHJkUAMYGxJGy1ibRqK18ToncmO3y52ar3078QxelvF4oaiXZkYzWitt5pPf5ZeJkppSYo3fJJcqyo_ya1Lmokghs0Jv9nppLUulbZd1cs_3HLjsdgmjpVQsp8GwrYx1ulOZ9D1DoQ2a5EqhJssO0VyIRQQSBQWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما ونزوئلا را تحت کنترل خود درآوردیم و در واقع، ایران را نیز به نوعی تحت کنترل خود قرار داده‌ایم.
🔴
در این چند روز، هیچ درگیری مسلحانه‌ای رخ نداده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/145625" target="_blank">📅 22:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145624">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532c884d67.mp4?token=hR71bes4PE5kSXL1Fb2rBAK2NtbrXb13WmEOQujGuZu8VGrAkPwDz1ThS3m6QxzXMQjClQgjFsngmgDpuqjZ3XjocqFjk0tisTb62vAoBi7c9q5DIyutG-Zh05g2TniPyCRZiYFGaOwZbRpeohw_78mGMjiDgs0MZSgNGjomOvgRFwE2hQojm-pe455S0CltHabzRENFktvqN0Ji4-5C-fMFrqSApXbopVcarpTcWtc32vPS1EdcCXF6KanczhYqdEYd6DDQ-P50uK9iWGlcRTOd1Air0HqId6CR0m_HTXPVTGSuv2soMMmzFo31xZ4S-XyeFB-q5ijN-27yiWUTq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532c884d67.mp4?token=hR71bes4PE5kSXL1Fb2rBAK2NtbrXb13WmEOQujGuZu8VGrAkPwDz1ThS3m6QxzXMQjClQgjFsngmgDpuqjZ3XjocqFjk0tisTb62vAoBi7c9q5DIyutG-Zh05g2TniPyCRZiYFGaOwZbRpeohw_78mGMjiDgs0MZSgNGjomOvgRFwE2hQojm-pe455S0CltHabzRENFktvqN0Ji4-5C-fMFrqSApXbopVcarpTcWtc32vPS1EdcCXF6KanczhYqdEYd6DDQ-P50uK9iWGlcRTOd1Air0HqId6CR0m_HTXPVTGSuv2soMMmzFo31xZ4S-XyeFB-q5ijN-27yiWUTq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: اگر این درگیری با ایران جنگ نیست، پس دقیقاً چه چیزی است؟
🔴
ترامپ: من آن را یک درگیری نظامی می‌نامم، زیرا برای ما مسئله‌ای جزئی است؛ یک موضوع بزرگ نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/145624" target="_blank">📅 22:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145623">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ: رشد اقتصادی باعث تورم نمی‌شود؛ نادانی باعث تورم می‌شود
🔴
ما باید این امکان را داشته باشیم که به جای اینکه همیشه شاهد رشد اقتصادی در سطوح ۲، ۳، ۴ باشیم، شاهد رشد اقتصادی در سطوح ۱۲، ۱۳، ۱۴، ۱۵ باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/145623" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145622">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ: اگر یک کشور با ما رفتاری نامناسب داشته باشد، ما هیچ تعهدی برای انجام هیچ‌گونه معامله تجاری با آن کشور نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/145622" target="_blank">📅 22:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145621">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5G99L4NcA7BFQigV3EZEdrzh0TAdGNtd77OeGelPjyRdvKyfkJIGl0Ev9qshEXI0ACCo8W83jHHRiRueIA5RJDw_c7m_aiIqjj3DqNEgKP3Rb76NnTAbO7wiBhztXDzE0qgO6scE-Kr5nUCgLLl7LD35V0nfcRmjYIDaQNN65wWFvq9-BiJNV8_E9coofaihAntfZ0cyJCyqQuYuUb9TW09NxwLtZD7VR6VGZabt8oGESy6rV1EEP0iDcUBlO4jggWCWn9flvGkOznJmeZb5SNAbbrLDhsz7JBYFeLOOTvev4lzoiiUFfj3_9QMC16KjLv9-yFAVgepFYgZD7N-sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هزینه آبدارخانه شرکت بورس انرژی: ناقابل ۱۱.۵ میلیارد تومان!
🔴
صورتحساب کدال منتشر شده از شرکت بورس انرژی نشان می‌دهد در سال ۱۴۰۴ این سازمان بالغ بر ۱۱.۵ میلیارد تومان صرفا هزینه آبدارخانه داشته است.
🔴
همچنین با استخراج صورت‌های مالی بورس انرژی مشخص شد میانگین حقوق دریافتی کارمندان این سازمان دولتی در سال گذشته بطور میانگین ماهیانه ۹۰ میلیون تومان برآورد می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/145621" target="_blank">📅 21:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145620">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95b5c30eb.mp4?token=nJAqduqHAb2qTh8g-n4xj-IqvuUzAzJGp4bBoS4eC1n2o3qDinNpkuRx3WgwHdns4Osx04_DYShVEZP4ewxcyypJhmhMSu-HRxFho9luPjoC_xfGD_koY68mLOC1ntme_Imk1yf8cgtxBrT0D6d6DJF1FnhVnQR8keSg5gyFvDSVaN9hdCmSgpeo39I5ouN27VjcuF9_Qvn0V0oR9j-C_zQurHs26M_wTgTwlhECuCdglzDVxqQAGaomKDzL8wJU46fjFbyISgWvfabRwo9S7X_O52suhYY024wtjxMqtw1_9u2I2k81ShOOQO6bWNfZgxjN99crKZkjejv2NqYHug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95b5c30eb.mp4?token=nJAqduqHAb2qTh8g-n4xj-IqvuUzAzJGp4bBoS4eC1n2o3qDinNpkuRx3WgwHdns4Osx04_DYShVEZP4ewxcyypJhmhMSu-HRxFho9luPjoC_xfGD_koY68mLOC1ntme_Imk1yf8cgtxBrT0D6d6DJF1FnhVnQR8keSg5gyFvDSVaN9hdCmSgpeo39I5ouN27VjcuF9_Qvn0V0oR9j-C_zQurHs26M_wTgTwlhECuCdglzDVxqQAGaomKDzL8wJU46fjFbyISgWvfabRwo9S7X_O52suhYY024wtjxMqtw1_9u2I2k81ShOOQO6bWNfZgxjN99crKZkjejv2NqYHug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر یک کشور با ما رفتاری نامناسب داشته باشد، ما هیچ تعهدی برای انجام هیچ‌گونه معامله تجاری با آن کشور نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/145620" target="_blank">📅 21:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145619">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: با فروش احتمالی بالگردهای بل ۴۱۲ به عراق به ارزش تقریبی ۱۵۰ میلیون دلار موافقت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/145619" target="_blank">📅 21:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145618">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9abd049084.mp4?token=CSXQOY24biT-5CBOnXLICV-Q06Rw-IiRp8MdWmrU3IcYmuRthZ-_3ZY0CSiZqXHR_HAUfeWqVxoaeDoe2VnxULWQ3Wr6iH9EjLesLXubj1CSL2hCa41xA2g6waZOPKw1SyWp74FWpW0G7jW_AlD7urjUNk58zH_ZGNGrLX7ufPYnMBxjZtjd33qvi0PupcMyO2TdZJfzrkMWQZ0Sj1F7XED-_jgyxb3-a5s-9byZE1hZJTgPLzHF_zCn0qlvbN7XKBrZPYPPq04Q7QhhgW-8s4IXc4p9No52xu3PPvhETDUwjVL2rkUL-d22kk80hYVwP-KVtJvkWBzOCoRTPU9Siw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9abd049084.mp4?token=CSXQOY24biT-5CBOnXLICV-Q06Rw-IiRp8MdWmrU3IcYmuRthZ-_3ZY0CSiZqXHR_HAUfeWqVxoaeDoe2VnxULWQ3Wr6iH9EjLesLXubj1CSL2hCa41xA2g6waZOPKw1SyWp74FWpW0G7jW_AlD7urjUNk58zH_ZGNGrLX7ufPYnMBxjZtjd33qvi0PupcMyO2TdZJfzrkMWQZ0Sj1F7XED-_jgyxb3-a5s-9byZE1hZJTgPLzHF_zCn0qlvbN7XKBrZPYPPq04Q7QhhgW-8s4IXc4p9No52xu3PPvhETDUwjVL2rkUL-d22kk80hYVwP-KVtJvkWBzOCoRTPU9Siw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین پاک خبرنگار مقاومت در جنوب لبنان: منطقه علی الطاهر سقوط کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/145618" target="_blank">📅 21:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145617">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWujYjioO20AjXtGgyPKXN9oH4FdEv7qk9q5V1uwPvSBTtFqUZb3qeI5dKOEjiOF-YadMQCQzWTvT0PnlRexE5yFUMFXm469MyZkZ34fZi7t34W6HpXO_cNYoxssfMKkvJWs-Tfr3NYq7Gb3mBScBWckzl4tUt3FeV2RAe3OAK_lgv3sRrUFEXcwKnxhCSEjU5uL-YMbS2WWH-B9f1vAsaOWBlkH0Ee8H8XT9k2pUAeBgggYGEstWQLsoujtXbyl2OJjGAhVM-xXHzUE9gG-3ZbjO0T61JmlbBM__oZS-m30g20zxNtRrZ3lZaRBGOB7u9cpE9dZ1bfbazNa7LH82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه NBC: سربازان آمریکایی پس از درگیری با ایران، دوره استراحت خود را در یک تفرجگاه گردشگری در تایلند سپری می‌کنند؛ در حالی که فضای متشنج ناشی از جنگ با ایران همچنان حاکم است. این صحنه، تضاد میان فضای تفریحی تفرجگاه‌ها و وضعیت آماده‌باشی را که ارتش آمریکا به دلیل جنگ در آن قرار دارد، به تصویر می‌کشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/145617" target="_blank">📅 21:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145616">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T22MUkWbqcDuIqeRCPTbzRo1B349jZCGYs6pkUxP_E6KRyPqDSvaPnA_JtyqBZXZQASekJ2jSMjq3i56phyIdw3qksptyo8ymLvH-dxutb5abFNVxmokgj42GJP4DCE7s7J8LfWSl6wZAI5sd9Gf13kMmk_r4fdtOYSHtED3utVNpujemdQngzVFUQxyTxrWWN4wWWONPbE04kN1HCzbJ3k3Pd4L9RW1X1EF5MrM0iSA46LJstO2mgSmphFTeJeGgbUb3JKUhtHkJ-XpHwS6rf9il8NMoRZSXFx6rVvux0YH1ay0ivi-L0vsWc4WhUEd3fZDfwG6ug1lDpB0H_aKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وب‌سایت رسمی کاخ سفید بازی‌های ویدیویی راه‌اندازی کرده که در آن‌ها کاربران مهاجران را دستگیر کرده و دیوار مرزی می‌سازند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/145616" target="_blank">📅 21:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145615">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
به گزارش سی‌ان‌بی‌سی، آمریکا یک بانک ترکیه‌ای را به اتهام تسهیل فعالیت‌های مالی مرتبط با ایران تحت تحریم قرار داده است.
🔴
هم‌زمان، اسکات بسنت، وزیر خزانه‌داری آمریکا، تلویحاً اعلام کرده که در مقطع کنونی برنامه‌ای برای اعمال تحریم‌های بانکی بیشتر وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/145615" target="_blank">📅 21:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145614">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKOOVm7TUTAJH5VaXUpZVlz-ooZw2i6dXSTX_TPyW1au4ncpb0OVY__GQzytFJslwMyCenrO-vdQcnOx9vbmEAnfXNLX9IQW-uCp3v9qWZuE8KucqwhEePabVUJXcIWYGHeO3nrNZLkuS7kuFcrRHt2mm-qwF9JH6foF9ATRXgB6szLw2hOKX4A3sotLi0wXWIkgvozt7fUMu6LVLRVdUO6IkBwy7wQaas1XgEbCFjgl74s2y5OkWVs3kBYTolJqgVMSY40lPfQw2uCiAh44oGkA_aq69DKt9xooKTJYRwXE7WECJJl7Iafc9tXQCLTQTnU4RQ_DvMHmMKbhgNJ1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرنده همای سعادت تو طالقان دیده شده:
تو روایات دیده شدن این پرنده باعث اتفاقات خوب برای مملکت میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/145614" target="_blank">📅 21:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145613">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F810VOGXaXuK_MjNJ0qNXJD6DS_ITq6pWN68cBIbScotxxVXcozqooFKNPUFfnxmVa_4rBOV7dlmvh020qNYRrtgF9WzklDT20D2zbUPohcwhRhK9QW4OVR5fVOEruPjedPIfTF4e-omEBnpKXh1tD1PgKrDLdOBFvJe0xiZmSTXsYxGedHESyb5YBLiynRXTvanQ3UlROpRA3375_Xp3BJZEoVnd1SSFmM7VEmgO6rEUkxiUYplw_2p1j67dgnXUq8EBhu4Gzp0crCQEEL902mcj1zU6-FJw1Mae47zZm7Gz3ibgEaIBOObdCLAqETUiXdmxrVPv9ks23Tp_SA0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این متن رو داری میبینی
یه نشونه‌ست برای آغاز مسیری جدید از زندگیت تا یاد بگیری که چطوری،خیلی سریع به موفقیت برسی!
💸
✅
اگه میخوای درآمدت چندبرابر بشه
💰
اگه میخوای لایف استایل زندگیت متحول شه
💡
وارد کانال شو بهت یاد میده چطور دلاری پول در بیاری
اینجا میتونی روزانه درامد داشته باشی و سرمایتو چن برابر کنی.
لینک عضویت کانال وی ای پی
✅
👇
👇
https://t.me/+nTm6gDB4A8gyYmFk
https://t.me/+nTm6gDB4A8gyYmFk</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/145613" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
