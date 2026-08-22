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
<img src="https://cdn4.telesco.pe/file/iaWB7MDc1dHliDQK12R5YMtpS238bEoVQnNmumkkh5omoqvLj2TpbFhntFyrY1BwfcoB6ArxdbAZXEDqeB9LWNS6t54FGSftMwMuLJi5_sOemfddCl_4bHYn_zchxcs5LyzsRZnPUMUbxy5sNyNdZzfG54q6JgQ7-ftSrGH971jdbih_FWRw1YBJm-ZJ4PjlyJv_MgyQUqrTasQLPaZJ1unYqYCE-v2Se5XK3xpOs6-pjAUj9XMydxpgpHmramLfzXouAvVa2tBwiAX_l12-vaL2Xeb6OQl6gnWhRSyBQsWsGx3fB8H3LRmDel7pSr1QrYwSACwg8c3MhWx2cC2aug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 986K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 13:18:42</div>
<hr>

<div class="tg-post" id="msg-143159">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTChTxf0yfr3cZrA7NKh2nLDMkUXm29IDAwUacKDPf3hAVPmhVjX_XZjEo5QDpshLS9i7osOfOQ6rZWkWoKhhvAe4Aaj65hmerS1rmEbLhgRcLvG7znLc-DAko551HhUUXmP-QsH6rJDQYqPLPZN7NZhM8MqB0pBvX-CCZ3lJiwHfccduuaHeD5GJJYNpOZ30JBZInw5B-MAKNbL8OtaERtLutj2pCNNZlJEdnaQfrk1qAaX7bkjDr71v-3gEoFo-KytymDtqzdbZP6IVUjmZY5iNBMB633mjEBofWpxKT4WLRQkEzcH6Ce6Hf0CoQoUCRjda3DYPUGW8E15isxKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYU4TvQoWNR9B2OO-4fVBmxqve9OFhznOqlHCgzMZulqJ2sMsroisDs6BWbHWE2h0hr1_ZTTTxAuG5Dg8byhLRBSv_GhB8M7VLslqiSaELhLqTa_UDlRFQuVL3YuhDmcAL9k_eJDqOHo1xp83LHENYUKizuNeHtho6w8fw1dGFvw1GMleE4_QthUPZOaUe4U7xsBXomDP7btx7-2m0XQQrxXpBtCciRN3HeJCMyT2Lzw917rCds1ykcTdnzvQA3u0ioxrQBLPcLY5Y1rFArn1V3W1aE5b2HWqgHSftJrDu1FlKJZrdE0RBXkdXgALWdt1GuiJEUZx3gveml-wBmbeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک کشتی باری ترکیه‌ای به سمت بندر آشدود در جنوب اسرائیل حرکت می‌کند، و یک کشتی باری دیگر به سمت بندر حیفا. در همین حال، یک کشتی سوم به سمت بندر ایلات در حرکت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/143159" target="_blank">📅 13:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143158">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
آمریکا و کانادا نتوانستند به یک توافق تجاری دست پیدا کنند و آمریکا تعرفه های ۵۰ درصدی به برخی از کالاهای وارداتی از طرف کانادا را اعمال خواهد کرد که این موضوع باعث تشدید تنش بین دو کشور شده و کانادا با ترک مذاکرات اعلام کرد وضعیت آن به حالت تعلیق درآمده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/143158" target="_blank">📅 13:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143157">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc77a9086f.mp4?token=J33jllIN2Y1ZaflAEiZoq0DfjF0nQXmHM0G6ONAProyyLMo_eQmPswmXaFgA2zTm1k2lMsdwUG9SKAD-uI4FX4uRDN_9nFDb8HhKoRJwjpLL3fraev9x9O8Jf8ob_uyhTmX5IS_U6ZK8cbJGBWl8pg5IeznQsztnARnpzSxgoSiuBEartHHqM673IJrFeCv3AFEi4udS-2MVei4VsXDAIMOacz-VgmKrM8l1XMEzU_yQARCZKkvtDqR67iroO_vHLkrEiWzzJGIx6mL3BRUhde4OcvPK4kLx2G0aS5h_6gcPpbkhnTR5sj_X9hyXernX35oQ66f1jWW_MYRxYSH9jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc77a9086f.mp4?token=J33jllIN2Y1ZaflAEiZoq0DfjF0nQXmHM0G6ONAProyyLMo_eQmPswmXaFgA2zTm1k2lMsdwUG9SKAD-uI4FX4uRDN_9nFDb8HhKoRJwjpLL3fraev9x9O8Jf8ob_uyhTmX5IS_U6ZK8cbJGBWl8pg5IeznQsztnARnpzSxgoSiuBEartHHqM673IJrFeCv3AFEi4udS-2MVei4VsXDAIMOacz-VgmKrM8l1XMEzU_yQARCZKkvtDqR67iroO_vHLkrEiWzzJGIx6mL3BRUhde4OcvPK4kLx2G0aS5h_6gcPpbkhnTR5sj_X9hyXernX35oQ66f1jWW_MYRxYSH9jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو مشغول کمپین انتخاباتی و در بین انبوهی از مردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/143157" target="_blank">📅 12:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143156">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClbfhgMXNB4SekX7NZsCDJM7LaZnJ9ftpa8CLAFLhKAcJTC5lzMVLjASO0i2QpgDWKbCVl8txX7iRt2eysEPDAAF6u6x2yvqY-UD87ch6v60uAgcnwz1JbIhOB9Pz8uvRfGMquvmHEqgtoKe7kS6scObpP4j63WV8UR30lUaRrwYVdUcdkZKRCmeQ09Z0pDxY6zgr44SMV5n0G8ddysmPrq0g4bNzriksyZmIBO0qJq-a9XHVl1c_dynLYx072eCKJeFN06IaK1YGK2p4r0fA1dbc_D3z6_z1tPCYlNhkMGNiRZUOyhCh3eDPzAYNWNo3ccXu0Vqk-ykrhUu47UtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هدف ۱۰۰ میلیون گردشگر در عربستان سعودی پیش از سال ۲۰۳۰ به وقوع پیوست.
🔴
عربستان با هزینه زیاد و ساخت زیرساخت های گردشگری توانست تعداد گردشگران این کشور را که با هدف رسیدن به ۱۰۰ میلیون نفر در سال تا قبل ۲۰۳۰ بود را محقق کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/143156" target="_blank">📅 12:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143155">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
چین بیش از ۸۰٪ نفت صادراتی ایران را می‌خرد و به همین دلیل هدف مهم تحریم‌های ثانویه آمریکا خواهد بود.
🔴
تردد در تنگه هرمز تقریباً متوقف شده؛ پنجشنبه فقط ۴ کشتی کالایی عبور کردند و هیچ نفتکش بزرگ یا کشتی LNG در میان آنها نبود.
🔴
ایران برای برخی نفتکش‌های عراقی مجوز ویژه عبور صادر کرده است.
🔴
آمریکا می‌گوید توانسته حدود ۸ میلیون بشکه نفت در روز را از هرمز عبور دهد؛ در حالی که پیش از جنگ این رقم بیش از ۲۰ میلیون بشکه در روز بود.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/143155" target="_blank">📅 12:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143154">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcHGEUAK3d06cEqW59yIxfJfcZBvJ99_tZAV8wW0xQ9InWX2nxsOJhuOYKfWLlBO4lMv4aM_dMfeUPffPMh1bxRu_48Whq9fgghaFKHHu5XhBlcyiIWlOR_mFVGmLJaunIogy-K0ijQmJimqFZ6Hlq-udI21jcfI6tGHZGhJQtwAikK8Ofgd6rxh4u9vzYtyXvofV3Yq7vYvxqRW1DJUlNAur426-bn9TCjcvgmba0E7YLhtOlCfCk0NUJDKjacMrudRZUaYsH5hWiHYVeZ7kPlYAxG5zLdqccn2oTdmsAHAobw9rXmSDyY4kUBQJj0YiAGCZOaxzSEbUX-Rw0w6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار اسرائیلی بین شهرهای آرنون و کفر تبنیت، جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/143154" target="_blank">📅 12:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143153">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
رویترز: آمریکا روز دوشنبه تحریم‌های اقتصادی جدیدی علیه ایران اعلام می‌کند که احتمالاً خریداران بزرگ نفت ایران، از جمله شرکت‌های چینی، را نیز هدف قرار خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/143153" target="_blank">📅 12:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143152">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
حملات نیروهای اوکراینی به منطقه بلگورود روسیه، ۲ کشته و ۱۳ زخمی برجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/143152" target="_blank">📅 12:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143151">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
قیمت دلار آزاد به ۱۹۰ هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/143151" target="_blank">📅 12:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143150">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سایت فوتبال ۳۶۰ رفع فیلتر شد و دوباره در دسترس قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/143150" target="_blank">📅 12:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143149">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: با ادامه محاصره دریایی، ممکن است از پیمان منع سلاح های هسته‌ای (NPT) خارج شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/143149" target="_blank">📅 11:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143148">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKIftJ498pQf-C8qTa8ZdTCmVnbLNQ96hwUNJ0a50YDlyaz2Hdj3wR1NZOcBpcJeFPWlXlo-7jK77_38DnYxxf9ikbgiB6eDhhKBlkrDiVv92dIKnmmxjMCwPYbUOqGUcwfcCkCHIOKQrWLqggy9thHEuxXRxbi4E26_QMPHxMHCZAG8Y0S9lC0P8Ox1QrA4HzkiEG0QFdVSGxs1fX52AA5dj1Sge2hBUArLM4P3aVby5K2gFkj2ZQHeBUeumf7PcByYyk1C05HSXImhDcdmqw3hak9zGtNAFanyXcO9IuLJuZGzvKxeDmhJMPUwLXpYgq7RTwpzf4fSBWg6SIKvbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک تانکر نفتی متعلق به شرکت "ادنوک" امارات، شب گذشته با موفقیت از تنگه هرمز عبور کرد، و این مسیر توسط نیروهای هوایی آمریکا به طور گسترده محافظت می‌شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/143148" target="_blank">📅 11:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143145">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMi07pF-ugbfZVG4z6_YfopjOXJtyNAH6ak_PSOlX3f0aHvvpqzec82Q74jpV0p6AEPhNR0oOz6FCQzAO33uPjYWj-dW13MOhOwiCFl25jpjTAcLHy8e_l5R--kfntQL2WhN9Wnu6V4-gPeTkfS-VpwYq34b7MljuCP4bEZDjLi5HD9dbrb7Dg91YmEWksVZjdiZFDhjLvYsrPKk-6Bsb7aRYp_b11Fvlc4AHIXh6hDnQHc5OQryCPokGKPj578hLJPm88yUi4rJtBRt9bJ534abtEZhqeSNfKmuyE62oQ85fsY202oKOTY009mVJB-2vIWt91K7ZQ-cFKjz2ipLZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QCHrZ3XSwoP_tvi5cgPS0babZMMaJ9MNKcXIdGsPodM0hDU39z4Bh1dfzDZ9_2mdbZMcT_tx3ALbFaupxMO_awhN8rnG9tgoSHO1fzZrAikdEsvDQ8lUCdkrtsg2J2EJv9zKGYO8T5xwPvFcKLUG9S8myydus12FPcf1M-fdSYTpFVIkvUwOaoN2GpZkHyWo0xdW8pA8jclx6XbmJT5RCCfkk3hyUVQH6prFH8ud26jqfmMQ8YTpmHo6_JNwRVgdok17rS2jDWyXK4H9yIZgMI6pyt2uACmUNrCBifAG_Zhl9DwCK8roNvePYdxl2leTgAhGKI2bCc4dGD48TNtx8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اوکراین برای اولین بار با استفاده از پهپادهای خود، به مرکز لجستیکی شرکت Ozon در شهر چاپایفسک، استان سامارا حمله کرد.
🔴
این شهر ۸۰۰ کیلومترتا اوکراین فاصله دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/143145" target="_blank">📅 11:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143144">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام آمریکایی: در کاخ سفید درباره جنگ با ایران و راه‌حل پایان دادن به بحران آن، اجماع وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/143144" target="_blank">📅 11:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143142">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e429be9d1a.mp4?token=ucfpcmwEQCpB6gQVGP_6FRrcKAaJfoQ4jxEK6hEDVQGwiDRaRKq8aWeTZ9m2yAQRSAfY6FveLx1aCLbUdHMQpmdMrS7TodHBqU2T6l0aorgOsoj_fa5O5O1SF3s6M6JbYaiLAvC83L0lc4ZfHljneEQuUYSE_ZOKVE3ZuhgrJ80d-L0KF6kkhtV3pONyXVemo80jOWBHA_gEPssOyJIxGjtgFsQXI8GkPZwQ-0YPj0yE_rgYYCY5_hk7iYu7UvUUDvvb4e80ayeUhd1RmvHRivNWZyEWFVGyzB1o4Z_LOhnkVZs0x-PKbfBeAqnXSpqTh6eiVyFQXDU4BAWl_hf_eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e429be9d1a.mp4?token=ucfpcmwEQCpB6gQVGP_6FRrcKAaJfoQ4jxEK6hEDVQGwiDRaRKq8aWeTZ9m2yAQRSAfY6FveLx1aCLbUdHMQpmdMrS7TodHBqU2T6l0aorgOsoj_fa5O5O1SF3s6M6JbYaiLAvC83L0lc4ZfHljneEQuUYSE_ZOKVE3ZuhgrJ80d-L0KF6kkhtV3pONyXVemo80jOWBHA_gEPssOyJIxGjtgFsQXI8GkPZwQ-0YPj0yE_rgYYCY5_hk7iYu7UvUUDvvb4e80ayeUhd1RmvHRivNWZyEWFVGyzB1o4Z_LOhnkVZs0x-PKbfBeAqnXSpqTh6eiVyFQXDU4BAWl_hf_eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرنگونی ۴۵۷ پهپاد اوکراینی بر فراز روسیه؛ انبار «اوزون» هدف قرار گرفت
🔴
وزارت دفاع روسیه از سرنگونی ۴۵۷ پهپاد اوکراینی در مناطق مختلف این کشور طی شب گذشته خبر داد. رژیم کی‌یف در اقدامی کم‌سابقه، انبار شرکت «اوزون» در منطقه سامارا را هدف قرار داد که منجر به تخلیه ۵۰۰ کارمند و توقف فعالیت این مرکز شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143142" target="_blank">📅 11:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143141">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
فرمانداری سیریک:‌ احتمال شنیدن صدای انفجارهای کنترل‌شده ناشی‌از خنثی‌سازی مهمات در شهرستان وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/143141" target="_blank">📅 10:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143140">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
محاصره باب‌المندب، تردد در بندر ینبع عربستان را بیش از یک سوم کاهش داد
🔴
یک شرکت اطلاعات کشتیرانی انگلیسی:
ریاض برای مقابله با این محاصره، مسیرهای صادرات نفت خام خود را تغییر داده که زمان سفر محموله‌های عازم آسیا را چند هفته افزایش می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/143140" target="_blank">📅 10:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143139">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزیر علوم: آموزش دانشگاه‌ها در سال تحصیلی آینده حضوری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/143139" target="_blank">📅 10:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143138">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
اهواز با بیشینه دمای ۴۷ و اردبیل با بیشینه دمای ۲۴ به ترتیب امروز گرم ترین و خنک ترین مراکز استانهای کشور هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/143138" target="_blank">📅 10:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143137">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
نظامی کشته و ۷۵۶ زخمی آمار تلفات ارتش آمریکا در جنگ علیه ایران
🔴
بر اساس تازه‌ترین آمار پنتاگون، شمار نظامیان آمریکایی کشته و زخمی‌شده در جنگ با ایران به ۷۷۴ نفر رسیده است؛ ۱۸ نفر کشته و ۷۵۶ نفر زخمی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/143137" target="_blank">📅 10:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143136">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
رویترز: ایران به درخواست بغداد، اجازه عبور شماری از نفتکش‌های عراقی را از تنگه هرمز داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/143136" target="_blank">📅 10:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143135">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EW6epnYupi3P5TWeA4w7ewvEV7DY3sNB-S3CCABt9AlqcWA_4MeAHpQeLEt9fiIk_spAYNUAeJbduol64oe_hDVeLflry1CRPDrtAyo3tDXyFU_EW0P2e5OcOR7Jycdohp-LYbOm3jDUYpgEEGVNL20MWq6q5UljdD2mVDNctaRLMjcV2LqEO4VSl94ENiMdIRKyHvAgmg3VGJW6pjSSnTWEs_fVfvD-8v-nguOTn_rJePKHX72fFMDkn6tMxyi4-EGFUb0CvaljMcO9R4aY9XNGjCI7l_2GsfuCfwX9p0WEvpUuF58-KAgNbAvKze3xnuPvBmWzqwleGZvQ60s4NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس از ۶ میلیون واحد عبور کرد!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/143135" target="_blank">📅 10:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143134">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
روزنامه اطلاعات: حرف‌های پزشکیان و قالیباف درباره اوضاع اقتصادی را جدی بگیریم / معیشت فقط غذا خوردن نیست که بگوییم با یک لقمه نان و پابرهنه می‌جنگیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/143134" target="_blank">📅 10:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143133">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIeqq2_1gvU2WbC2hkTHFqNX9VKod503fSoHf2pzFAUEa_Zns0uxE6ol41QHNgBxmGQEMdJSgDsireRuVu0uSCP_DMTSVGo_CO4pFuA2ZKTL3fgK_TfpBFw2-pTT2Zd3ceAB9GO4ZuIdyH6d1u3U8a3qrLj-RP1QSuvEbQU8mhOxb5tvPg9kd3UlFD5nWFWWzICkoMQHAapLzmDMCpvKr4zyTY7tXBfEBMY0IfmpxjjwUaOYzubfVYt_dxXLK2pWKprW1DprhWzVniV48JRw8IXwqFXR3TK3yH3hiZjxo3VcPXIhiplKWtJ1UqMP99zp6NBNS8UCBQBfPNSYFoyWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الیاس کردی، تحلیلگر: گویا راه حل چهارمی برای بنزین پیدا کردن!
🔴
کیفیتو انقدر پایین آوردن که مردم از ترس خراب شدن ماشینشون دیگه بنزین نزنن… دولت با همین ترفند ساده، مصرف رو کنترل کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143133" target="_blank">📅 09:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143132">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d266281cd.mp4?token=G2Mfx3SbSaxM4T2IbTgeqe3XJ1m2o_T3jN1IVagthkFX3dhz5oTzDBAtIAOLIuZSC5qR_nW7iofnsEMHfgjgcOpz-nXBr6hYNXRpwgh5Co-Z_Y5R-6jcQ3LV95IZIrocnPK2ClEl35QBBMelqFH_lYSXdn4ql9t1vB1fAagi3j6EYE0y4vmPsm3RzTvk-fLIAxDcecVVWehiPZfJ21hOsEJUPNXZZLnJgH20rcfxyOrBWVpE0k8EQ4B3brMPusBOJ9UoJeIPTJfgoTzqR5y3oD2woBdBGE6s3_33lnitqLnB-LOuLKvCP5cT9fFGM5gsAe8dSkBXt5zLCqn23xScQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d266281cd.mp4?token=G2Mfx3SbSaxM4T2IbTgeqe3XJ1m2o_T3jN1IVagthkFX3dhz5oTzDBAtIAOLIuZSC5qR_nW7iofnsEMHfgjgcOpz-nXBr6hYNXRpwgh5Co-Z_Y5R-6jcQ3LV95IZIrocnPK2ClEl35QBBMelqFH_lYSXdn4ql9t1vB1fAagi3j6EYE0y4vmPsm3RzTvk-fLIAxDcecVVWehiPZfJ21hOsEJUPNXZZLnJgH20rcfxyOrBWVpE0k8EQ4B3brMPusBOJ9UoJeIPTJfgoTzqR5y3oD2woBdBGE6s3_33lnitqLnB-LOuLKvCP5cT9fFGM5gsAe8dSkBXt5zLCqn23xScQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، در حال لذت بردن از خود در پوزیشن‌های مختلف در یک جلسه عکاسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/143132" target="_blank">📅 09:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143131">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5vV_MVyNEEH9bNNM5PM2-aglwmnNvdJt9wLYuE8fyChFBvjA9i5dE83WCRcNjViD1lp3AOP6Pt2w_jLhwdR9mAQpcG15vIVWHhK3E_EWh_40Nf8BCNwi0dOk4fF9_64HKuCwMpd2gw2N3G2qR3puMmNFtRRPoX_Me9mks-YmHbiiE59b-8aTMvpAp6-nZWOtY1M5VZ38eNeUgIda7k__NURhRgNmhjFbV3i5q_whjWgWOgR3ro62G_fcozrqgMI5TYe2sj6V32CceCvIccAyrvZlPbdPwZ6jCJQe2u87EYuPBGbg_rTlRnp-7g2_MKjUpZfie1SbUWRB31xdYo70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق تروث سوشال: تاکر کارلسون اخیراً با تاماس ماسی، نماینده «سابق» سبک‌وزن، و مارجوری «خیانتکار» گرین، همه‌شان بازنده‌اند! «نظرات» تاکر به زمین خورده و فقط بدتر خواهد شد.
🔴
دیگر کسی به او اهمیت نمی‌دهد، زیرا کاملاً بی‌اهمیت شده و اتفاقاً، به‌طور شگفت‌انگیز، فردی با هوش بسیار پایین است. او به‌زودی نمی‌توانست از دانشگاه خارج شود و شاید اصلاً نتوانسته باشد، اما فقط افراد واقعاً احمق نمی‌توانند از آن چهار سال شگفت‌انگیز زندگی عبور کنند! تاکر می‌خواهد برای یک پست سیاسی رقابت کند، اما باید مجبور شود یک آزمون شناختی بدهد.
🔴
او شانس ندارد، اما احتمالاً می‌تواند چند امتیاز را از هر تیکت جمهوری‌خواه که باشد، بگیرد! تاکر یک بازنده است و همیشه بوده! مارجوری تیلور براون (گرین تحت فشار به براون تبدیل می‌شود!)، یک زن جوان بسیار عصبی، در عرض چند هفته از یک محافظه‌کار افراطی به یک «اهمق» لیبرال تبدیل شد، زیرا من از پاسخ دادن به تماس‌های تلفنی او خودداری کردم — نه به این دلیل که او را دوست نداشتم، بلکه فقط به این دلیل که وقت نداشتم. او در نظرسنجی‌های جورجیا بسیار پایین بود (چون تأییدیه‌ام را پس گرفتم) و شانس پیروزی نداشت، بنابراین او، درست مثل همه‌ی دیگران، «استعفا داد!» تاماس ماسی به عنوان یک سیاستمدار شکست‌خورده و یک فرد واقعاً بی‌ادب ظاهر شده است. او فکر می‌کرد بسیار عالی است که به همه‌چیز، صرف‌نظر از اینکه قانون‌گذاری چقدر خوب، قوی یا مناسب باشد، «نه» رای دهد.
🔴
چه تیمی این خواهد بود، سه بازنده و یک جیب پر از سکه! تنها شانس آن‌ها این است که به دموکرات‌های احمق چپ‌گرایان رادیکال بپیوندند و سعی کنند وارد سیستم انتخابات مقدماتی شوند. به همه‌ی آن‌ها می‌گویم، ستایشی برای خدا!
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/143131" target="_blank">📅 09:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143130">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
افزایش ۲۷ درصدی تردد کشتی‌ها در تنگه هرمز!
🔴
سی‌ان‌ان با استناد به داده‌های UKMTO گزارش داد تردد کشتی‌ها در تنگه هرمز طی هفته گذشته ۲۷ درصد افزایش یافته و ۱۰۳ کشتی وارد و ۸۹ کشتی از آن خارج شده‌اند.
🔴
با این حال، این میزان همچنان تنها ۲۰ درصد میانگین تردد پیش از جنگ است و نشان می‌دهد هرمز همچنان با شرایط عادی فاصله زیادی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/143130" target="_blank">📅 09:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143129">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏
👈
ادعای اکونومیست: هکرهای مرتبط با ایران به تأسیسات آب آمریکا حمله کردند
‏
🔴
هکرها طی تابستان به تأسیسات آب و فاضلاب دست‌کم هفت ایالت آمریکا نفوذ کرده‌اند.
‏
🔴
ارزیابی‌های اولیه مقام‌های آمریکایی نشان می‌دهد گروه‌های وابسته به ایران ممکن است پشت این حملات باشند.
‏
🔴
این نشریه همچنین تأسیسات آب را از زیرساخت‌های آسیب‌پذیر آمریکا در برابر حملات سایبری توصیف کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/143129" target="_blank">📅 09:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143128">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سازمان دریانوردی ملل متحد: ۱۹ دریانورد در بحران هرمز کشته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/143128" target="_blank">📅 09:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143127">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJtA3Zt9Jr0eHxGAP3U47anYlsg5nVyjejgM7rmPIj3jtzssoaR-7eMSQH2RSIUhAYLGnLIIbwrHfaG5d8CccqEwXoaBHqc11o-02rtgd79jJP9EiY0YniwaVG2KryaFyYqBeq_S-KYBFQuHrkej7e79coZ-2FaIYB5dVFrxXKHmrPKYET-_Xn8hOimU9JZx-FSoQio9x4l-xEZ2k2Crhlglv9PgRkmd9GFkvd9Bl7AnSMUzjgYr8_cIxM1QX2a5xtr6d-hEjj3k5h_xIBYrNFFNb7yrmpEYU0m7araIIP5UFH7ICHBYvftfmXgvFJUWKMYXDhk8LGKln6pRa0Hahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تحرکات جدید در العدید؛ ۴ سوخت‌رسان آمریکایی و ۵ فروند C-17 قطر در پایگاه
🔴
تصاویر ماهواره‌ای Sentinel-2 که امروز ثبت شده، حضور چهار هواپیمای سوخت‌رسان نیروی هوایی آمریکا در پایگاه هوایی العدید قطر را نشان می‌دهد.
🔴
همچنین پنج فروند هواپیمای ترابری راهبردی C-17 گلوبمستر III نیروی هوایی قطر به العدید بازگشته‌اند؛ این نخستین بار از ۱۲ ژوئیه است که حضور این هواپیماها در پایگاه مشاهده می‌شود.
🔴
بازگشت همزمان هواپیماهای ترابری قطری و تداوم حضور سوخت‌رسان‌های آمریکایی، از ادامه فعالیت‌های هوایی در العدید حکایت دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143127" target="_blank">📅 09:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143126">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee2e6eb68.mp4?token=WneyYmFArWOlF0Eo_Wgx_OjJ3LAhUnffY6dOgNpyrooZpeAoHzf4VDmoJuCkEEsnsLQVVEspbQpCj1spgB93pPovWtM2cQchbvN_yTGYS8GcGAOxW4nSLlEtrU7QRjP5s-Kh2wwiF_ceA-B5j48laPODBYYWYuVdOI3J-afZVkh7oSk0T5Web-w3KFojMEy38JeiFRoyRX9CxhXDjjPbEDYnrmuwr9WslD9zlk7ylODtsUbnIMOEGw0ct4Ge1m6SipgQwujo31AuC5CuEUpCtNIjkc9it7MsuHvrGgWru3OahN8nG2YDZtfSWjTbMDm8mPm1YG1isYp0MQdClnTjgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee2e6eb68.mp4?token=WneyYmFArWOlF0Eo_Wgx_OjJ3LAhUnffY6dOgNpyrooZpeAoHzf4VDmoJuCkEEsnsLQVVEspbQpCj1spgB93pPovWtM2cQchbvN_yTGYS8GcGAOxW4nSLlEtrU7QRjP5s-Kh2wwiF_ceA-B5j48laPODBYYWYuVdOI3J-afZVkh7oSk0T5Web-w3KFojMEy38JeiFRoyRX9CxhXDjjPbEDYnrmuwr9WslD9zlk7ylODtsUbnIMOEGw0ct4Ge1m6SipgQwujo31AuC5CuEUpCtNIjkc9it7MsuHvrGgWru3OahN8nG2YDZtfSWjTbMDm8mPm1YG1isYp0MQdClnTjgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عبدالملکی، وزیر اسبق کار: درآمد نفتی کشور در طول جنگ 40 روزه حدود ۳ برابر شده
🔴
دروغ می‌گویند پول ندارند و نتوانستند نفت بفروشند
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/143126" target="_blank">📅 09:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143125">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e3bb4da8a.mp4?token=DnrX-bYfYJMoNbURBU4KvoZ2r8fsWFJSZ3lS2AGCqGy7YMqkwzOcyT1FCWubg3rdIUmUTYfiiKTDM19w-OLnJdErprhzC3MvpQY2WIqAjd4WYLu6yHfJ85oMdz2lypwQd9thj6bysmGzdENXJkjOqtFw_6pIgsPKBrKtKQJRzMmZyFwP7F0Nc16w_hEyKXn3GKxudYrG-X5SRx2QTOOiYBepA1kx1XDuXLdLIPArKOpptLoqRWjYhqDZSUDF0Mp8_E71b1TnAPzVKYV3u-pC9Amd65qShDmJ7HR6ZoMx-uqplg6glSxvRe9ucmYg8LyRDAfFPX0UKysBXAHq6ara_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e3bb4da8a.mp4?token=DnrX-bYfYJMoNbURBU4KvoZ2r8fsWFJSZ3lS2AGCqGy7YMqkwzOcyT1FCWubg3rdIUmUTYfiiKTDM19w-OLnJdErprhzC3MvpQY2WIqAjd4WYLu6yHfJ85oMdz2lypwQd9thj6bysmGzdENXJkjOqtFw_6pIgsPKBrKtKQJRzMmZyFwP7F0Nc16w_hEyKXn3GKxudYrG-X5SRx2QTOOiYBepA1kx1XDuXLdLIPArKOpptLoqRWjYhqDZSUDF0Mp8_E71b1TnAPzVKYV3u-pC9Amd65qShDmJ7HR6ZoMx-uqplg6glSxvRe9ucmYg8LyRDAfFPX0UKysBXAHq6ara_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرونشست متروی پرند بازهم به مرحلۀ هشدار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143125" target="_blank">📅 09:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143124">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: اعلام تحریم‌های اقتصادی جدید آمریکا علیه ایران، اعلان جنگ به همه دولت‌ها است
🔴
تحریم‌های جدید، بسیار فراتر از یک «جنگ اقتصادی» است و تلاشی برای تحمیل حاکمیت فراسرزمینی واشنگتن محسوب می‌شود
🔴
«ارعاب اقتصادی» برای وادار کردن یک دولت مستقل به تغییر سیاست‌ها، یک عمل متخلفانه بین‌المللی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/143124" target="_blank">📅 08:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143123">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n12M_I-R2GLD8GXmQeItMoeiQn1WonEMoixP9fWftVEqzXk6frirMs63Vol2Y7CE9jbmnuwyyitIRg9CW1ntWXKdm_Pv-Hbn8wgJxV3psx9PBN5jn7PBNMmf9c7f3-FrG5J-TaREAsaEFIOOQlRM9dyZ-Wx_DdqqENd2nijSlGx0w27FvTkK-z0iyMmYDOyF_rwts1rDmqPbYTiLefDZvPViQgta5FtBlB1mxpm9E9_5EK-tf8jFWWcQqjhjeCkKLH_t8_gVg-GSkShh5TUMm8uSOlYKQ6bBNVYbPgs8sHxWWHceDqNEMCcuYINjBFOc9TIvdvzi6s-5zwVKD5Bjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاکستان برای میانجیگری بین ایران و امریکا ‌۱۰ میلیارد دلار میخواهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/143123" target="_blank">📅 08:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143122">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3053547436.mp4?token=c6hT8Z5C2stbma86uf-R1q8bPDhzrjq9b3VLs3gLf0olcrFVWobrrv1r2lj5Qn5q8FACayDP2WqFBMuDyhfD6K9vCtSWShH3we3cTv8YxjU_O4DFWb04ZAhHrTGqCRGR4-VSyX2FZFpyYG6Qwj7Dmng8IFHnb4tppAhmQXWVrErhC_l_q1fzxqpFm8onBZNDB1Hhorz_hE73j4l7u3ngWqkP8b4K2G4Ohw99wv49ObK7KEqw-chePuCe0yI6R6zDVqSg3pzqqksiOI-LyJ8-9KobmPrZrhip5dtcy6MRNotk8SkbG3zP_U2eUwSzuVvcHJik8LExF2Kz-qeGHSUY0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3053547436.mp4?token=c6hT8Z5C2stbma86uf-R1q8bPDhzrjq9b3VLs3gLf0olcrFVWobrrv1r2lj5Qn5q8FACayDP2WqFBMuDyhfD6K9vCtSWShH3we3cTv8YxjU_O4DFWb04ZAhHrTGqCRGR4-VSyX2FZFpyYG6Qwj7Dmng8IFHnb4tppAhmQXWVrErhC_l_q1fzxqpFm8onBZNDB1Hhorz_hE73j4l7u3ngWqkP8b4K2G4Ohw99wv49ObK7KEqw-chePuCe0yI6R6zDVqSg3pzqqksiOI-LyJ8-9KobmPrZrhip5dtcy6MRNotk8SkbG3zP_U2eUwSzuVvcHJik8LExF2Kz-qeGHSUY0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
ببین، شب جمعه است. ما زمان زیادی داریم
🔴
لعنتی باید چیکار کنم؟ برگردید، ایران را کمی بیشتر بمباران کنید؟‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/143122" target="_blank">📅 03:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143121">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7543d7abdb.mp4?token=MHTDwbmjpog1IQqoRzTdY8PrtN4xRLvZPbWW3MlShJDw2NyoLVHqfoxaTFVg7zsr5andM1lon01KdWtSeX6hTo7hptIZAW0YxEwA6CIoVwxR2DSJwq1wyKhh6zDoZ2joITQG-AMjbCw8snD7B87kCNW-QbCf8Df3wykNkF2e3HloHGT_Thuy16mgKOzarH5r-7qZ0kJDU9g5oU9pBhUn7uKWGRJRMpDs5gJqo1TTgffeJug3xzy3XXgciLKpM3MfYUinm7lgUZQhpdhJH8zqT-KFY939LpRM7O4XUXG97ElbWXyWXxU3h_s_YXWtTxg57H4xpFjw_Ywwg4BiG3RZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7543d7abdb.mp4?token=MHTDwbmjpog1IQqoRzTdY8PrtN4xRLvZPbWW3MlShJDw2NyoLVHqfoxaTFVg7zsr5andM1lon01KdWtSeX6hTo7hptIZAW0YxEwA6CIoVwxR2DSJwq1wyKhh6zDoZ2joITQG-AMjbCw8snD7B87kCNW-QbCf8Df3wykNkF2e3HloHGT_Thuy16mgKOzarH5r-7qZ0kJDU9g5oU9pBhUn7uKWGRJRMpDs5gJqo1TTgffeJug3xzy3XXgciLKpM3MfYUinm7lgUZQhpdhJH8zqT-KFY939LpRM7O4XUXG97ElbWXyWXxU3h_s_YXWtTxg57H4xpFjw_Ywwg4BiG3RZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
اگر ایران به سلاح هسته ای دست پیدا می کرد، از آن استفاده می کرد. آنها اسرائیل و خاورمیانه را از بین خواهند برد. ما نمی گذاریم این اتفاق بیفتد.
🔴
آن بمب افکن های B-2 یک سال پیش به امید سلاح هسته ای ایران پایان دادند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/143121" target="_blank">📅 03:27 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143120">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef46552dbe.mp4?token=nLYouTNshfDbhsd31WPUqOlMtjJEJSo4UEUjxKwbk9EKuFUr7HOJYyWUFG09dtOehjDTV6q3DJQsedNM-OMME56egHwB6FZ6rNmbVcS9XDZGz1inaV7_TXAMt4rx3pLkyM8D4-83dBMlaoCx1XAI8K1VthOlVoKCu3O6inG0an3ilAGslR8JrMPob_1GIihgK1WSrd3uvVkaXGGAYCPQCOyPJI1wuI2ruq3Npq4bSEFgVgeMnWb8KwE7wO3P-f84D66Cz-y1aBzAM0snnIZtA43ZOaQvTqCqyyQWvioFhXdtYdnVZNdF1gp2fKSivK2sYX0_4WpfJGyI0S0rfGuY0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef46552dbe.mp4?token=nLYouTNshfDbhsd31WPUqOlMtjJEJSo4UEUjxKwbk9EKuFUr7HOJYyWUFG09dtOehjDTV6q3DJQsedNM-OMME56egHwB6FZ6rNmbVcS9XDZGz1inaV7_TXAMt4rx3pLkyM8D4-83dBMlaoCx1XAI8K1VthOlVoKCu3O6inG0an3ilAGslR8JrMPob_1GIihgK1WSrd3uvVkaXGGAYCPQCOyPJI1wuI2ruq3Npq4bSEFgVgeMnWb8KwE7wO3P-f84D66Cz-y1aBzAM0snnIZtA43ZOaQvTqCqyyQWvioFhXdtYdnVZNdF1gp2fKSivK2sYX0_4WpfJGyI0S0rfGuY0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
اگر در میان دوره ای شکست بخوریم، استیضاح می شوم.
🔴
قرار است من را استیضاح کنند. آنها هیچ ایده ای ندارند که چرا.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/143120" target="_blank">📅 03:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143119">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ:
هدف ما نابودی برنامه اتمی ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/143119" target="_blank">📅 03:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143118">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ: تنگه هرمز قلمرو آمریکا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/143118" target="_blank">📅 02:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143117">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ درباره ایران: این در واقع یکی از بزرگترین مشکلات من است: نمی دانم با چه کسی در ایران برخورد کنم.
🔴
این تنها کشوری در جهان است که هیچ کس نمی خواهد رئیس جمهور شود.
🔴
آنها می گویند: "چه کسی می خواهد رئیس جمهور شود؟" نه، نه، من نمی خواهم رئیس جمهور شوم.»‌‌…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/143117" target="_blank">📅 02:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143116">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29acd65e5a.mp4?token=GGca26-PnRy8ph_GC6Ka7Z7tyMw6apT3M14v98EQIwnfs_hBNCLfXKApiDuFbUDEpBnwNulPCQzoccQpYxH8mlHh47NuLdUmOWi7pGgL2bYIs8eqgwe1SB0X7VTXQyhoZZckIs9PbrgKfQO4_cZJ0bPr6ZfZZVkBPHmB2YPwC7mAXyqFvcaczhcoEQpZhHJUxEmwAhRhVEgMiEmvWnV-zYE8PYsjjY7xW3ilmYAgjdfxG18Avo-LzGcfPKMaVs-xpvveHbwmNlwhaP_sOPrmOzbOchhDjUePW9JAXeyhgOb1Q7PTE_w4rSOtWl2SxzQ7R_KF703nTkvm1D-W_Fd7562_rW4keRVr8QCG94WPkPUqoX0bJCGyvSiPP6fQa8F7ywKwMznqGRre9gcvytrVABcJyB6UMa96eBenreEDull6g5Rgqd0UFosW_rpppaI5AW8_QIbTZMYyam0xTxYDCid9l4WuYlHOsJB2PMi39ucPaIQFAj21vCHLhtwAqwqbNd2MwR6wAsHpBPLbzSJ3ve3K0ABWEhpNmXYLtxBHAiOfB-mIi1uvgEfVZmtp14mSMG-TbjDIrZ7lQxmfRHlC8GEWUTl-n4jB_exzb-YbuIqk9qG2YQC9-ju5OAF4D4E-Be_qOah5aJIGWlBwBZ6Mn_KgDvldrd5dtTOq5jvs3-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29acd65e5a.mp4?token=GGca26-PnRy8ph_GC6Ka7Z7tyMw6apT3M14v98EQIwnfs_hBNCLfXKApiDuFbUDEpBnwNulPCQzoccQpYxH8mlHh47NuLdUmOWi7pGgL2bYIs8eqgwe1SB0X7VTXQyhoZZckIs9PbrgKfQO4_cZJ0bPr6ZfZZVkBPHmB2YPwC7mAXyqFvcaczhcoEQpZhHJUxEmwAhRhVEgMiEmvWnV-zYE8PYsjjY7xW3ilmYAgjdfxG18Avo-LzGcfPKMaVs-xpvveHbwmNlwhaP_sOPrmOzbOchhDjUePW9JAXeyhgOb1Q7PTE_w4rSOtWl2SxzQ7R_KF703nTkvm1D-W_Fd7562_rW4keRVr8QCG94WPkPUqoX0bJCGyvSiPP6fQa8F7ywKwMznqGRre9gcvytrVABcJyB6UMa96eBenreEDull6g5Rgqd0UFosW_rpppaI5AW8_QIbTZMYyam0xTxYDCid9l4WuYlHOsJB2PMi39ucPaIQFAj21vCHLhtwAqwqbNd2MwR6wAsHpBPLbzSJ3ve3K0ABWEhpNmXYLtxBHAiOfB-mIi1uvgEfVZmtp14mSMG-TbjDIrZ7lQxmfRHlC8GEWUTl-n4jB_exzb-YbuIqk9qG2YQC9-ju5OAF4D4E-Be_qOah5aJIGWlBwBZ6Mn_KgDvldrd5dtTOq5jvs3-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
این در واقع یکی از بزرگترین مشکلات من است: نمی دانم با چه کسی در ایران برخورد کنم.
🔴
این تنها کشوری در جهان است که هیچ کس نمی خواهد رئیس جمهور شود.
🔴
آنها می گویند: "چه کسی می خواهد رئیس جمهور شود؟" نه، نه، من نمی خواهم رئیس جمهور شوم.»‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/143116" target="_blank">📅 02:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143115">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یک باشگاه مختلط در تهران به خاطر مختلط بودن پلمپ شد و ۷ نفر هم دستگیر شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/143115" target="_blank">📅 02:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143114">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEhtpHYPXA2Hg8xOmiQD9d90lAtED5OlLiOzTFf2rDKHudM0_FhU4fmc_bapWl1ZfENk-LhVdy10OM_rjcpM3sn9Ydn_pQl4_61eSYTL1OtoDverVlqzLYXr5BUxdeMJlrZw-PbxOi5DGbo9PzXtZu5lFUaJ9Sa7HH31N1KboAVz2Z6HqoFngxJHo4Bl1plCL-mXJYwfE1hg5iMwlx2SICE9jESgRzokPf0ZFLWngxsuKTpQpoKIMQQDUlzBDPfXn7Y1LRgxL00lI8mG8aAKlE8ooAEkqGw_nAPVAl5PBi_r_l_6ht81OEtOEpTO9ArStQS_alY8bBNwc6BA5oHtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی مسیر ۶۸ فروند کشتی تجاری را تغییر داده‌اند، ۳ فروند را غیرفعال کرده‌اند و سوار شدن به ۲ فروند دیگر را انجام داده‌اند تا از رعایت مقررات مربوط به بن‌بست اعمال‌شده بر بنادر ایران اطمینان حاصل کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/143114" target="_blank">📅 02:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143113">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt3e3IX20Ou32cRTZzc37hB-slctkSOaGxvgZQ0O1txybciNxP2EmfnUoNMWWNNSaPoK4Mx-LagwPWvKuI2HoDkn16VPYnI4VfPygSIXtdfevK_jLmwh7dXcMpQ1n4USCni43ynTm8B9yfqAn_xXfiVF4jVpnFUY91vhA9a7JsXBCmv2VJEPwkZLRadZzJzUgI0CFxKqS-pGhLvcYZ3qLEIGDAQNH9LxzJiHRV4kyDhsuRaA3OTSWRGHDgKWflo_5FX1-rEzIcUwa44ruwKYdemJBLEHXU9fmSAtmGs3eaNEw8mvI8ROAs6AvQac1gWFBp3hKdQqt_Pl7cOSN-I1zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند جنگنده F-35 بر فراز امارات متحده عربی پیام اضطراری ارسال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/143113" target="_blank">📅 02:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143112">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdaZBqAUeeaxzzi8mSqOiATM6iZ1Br6J39dTZORoP2oMzAR0B494jM5fFxTBa9Aan9-DH_M3bmUfUIXtq8ZSBOTBL0H1Efv9m6BZRad9ismJX5v49ODFAETjtwwp0KN9uOtIVySSiPkhqGlJmbkLGPusJYnwgtLPHt1wQ9vLQa7gtH93Fh3QcoxLEicC-A0QPA4quHX1DM4b2ig2Qwu22CI_cFTuMdLEXl_xFib25L3noaGQRDS8zk6WmdKSKhgh2EKS3lr7jbwIhqjJlk5S4LgeLLf6sy2vDJ3ycX6ykO2Zfkd4ceAkcSfTkQk4YTUUS6D-wxCXN0bHemQgDBtxIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایران : هیچ راه فراری نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/143112" target="_blank">📅 02:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143111">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سه فروند موشک بالستیک "اسکندر-ام" و دو فروند موشک "اس-400" به سمت کیف، پایتخت اوکراین، شلیک شدند.
🔴
موشک‌های کروز "باندِرول" نیز پس از حملات موشکی بالستیک، در حال پرواز به سمت کیف هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/143111" target="_blank">📅 02:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143110">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTwkV3m2w--m4p52dBK-xUFYHucX-toeGSN-_jQm8fUNvBBGUadsK7XepsPN6udnq25ORvyeUTevdBWryFUeVuw8ssC7xWUuL2BKgx-1j4A7lMVE9p53NFRyHGUkvXQWidsvF1g6nL-OtB1cNgz5d0okF8nzREs6j1sRStsse1rwe8Aqps9Qd8BbNgTE2I9o-mO-LGzgpPyfx96enqhlia54XfxLnEnD3Bl5GHUhX6Q1I75fbhFAlIMbWsYdEJg2_wY8hilHXf4g4YQ7Gw9jSw_07rJGLWySr-YP-T9ARlDl0s1KkZDXsQeBSNnEKuLB1-X5UNbIJ2Is1clxQiTUWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنج فروند هواپیمای تانکر سوخت‌رسان و یک فروند هواپیمای هشدار اولیه مدل E-3B ساخت آمریکا در نزدیکی تنگه هرمز در حال پرواز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/143110" target="_blank">📅 02:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143109">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpvtbES1fNEDpP-tOXHBw9YVZnvUYcldifxlx_VcUgip4q7SICEckbCwUU3336PmWP_5oU8_m13AGZ6joVP3AH0l-h9CP_AQ1f9DdEYvXSuipUrjB84011IdKRTvjUlxRsOJB1CNUAz3edn1q4pNKUvWVoqnkPTACiJh2jo6Gm1fjWw2uCCqn1KMjT718g5UST8locZ331GwAttRSwtYcIL6PnpEq_Us1shhAmSp1UWR-FcWTJyLjrUk9HUv_1tHzm17SyNYiAN0_AhkpMg7aSI9u2othdr6AIoVKYNBcdxJRyIYQAqbM8jtJPltdd9zffecyZyYlN-SNK0trkWzwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان اینترنت یکی از استان‌های یمن رو قطع کرد،حالا تسنیم هم این حرکت عربستان رو غیر انسانی دونسته و گفته حکومت مزدوران هست
🔴
حالا تو ایران چندماه چندماه قطع میکنن و انگار ن انگار
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/143109" target="_blank">📅 01:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143108">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4d99d90e.mp4?token=dBV3P2jvRbTjIy2QCX4hWMY6GUopRd8hXRGLkA0epABu-Ot8DGbaHtxRvdpxG1OUdf-PrsWRzjI-zVmq0lOBcpQfj7FzPLPtywSaEbTJ8588p7DVBmcjGBdLnhDkE3VsarGIOcDFeWbrnGYa1O2n7jc_p_3-UkPzjIkGVrNIr8Ukk9NcUmDf8HP6sk58ftSscgSUM3oEfJ8E9uIEpBQ5CWetVHtUM2IecZcAuW56AQ5RlkTB3bzcKW9vPgs8AU9jMnGOzhog00MCriTTkz6yuCwoevdThMjnBAGVKBFeI58yJOR3G1b3nQ223pXEp8K2SV-sHPMgQMtQyFL8y7dLpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4d99d90e.mp4?token=dBV3P2jvRbTjIy2QCX4hWMY6GUopRd8hXRGLkA0epABu-Ot8DGbaHtxRvdpxG1OUdf-PrsWRzjI-zVmq0lOBcpQfj7FzPLPtywSaEbTJ8588p7DVBmcjGBdLnhDkE3VsarGIOcDFeWbrnGYa1O2n7jc_p_3-UkPzjIkGVrNIr8Ukk9NcUmDf8HP6sk58ftSscgSUM3oEfJ8E9uIEpBQ5CWetVHtUM2IecZcAuW56AQ5RlkTB3bzcKW9vPgs8AU9jMnGOzhog00MCriTTkz6yuCwoevdThMjnBAGVKBFeI58yJOR3G1b3nQ223pXEp8K2SV-sHPMgQMtQyFL8y7dLpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تبلیغ عجیب بستنی میهن در امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/143108" target="_blank">📅 01:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143107">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
تام باراک، سفیر آمریکا در ترکیه، در گفتگو با ماریو نوافل درباره حمله اسرائیل به پایگاه هوایی ابوالدُهور در سوریه:
اجازه دهید نظریه‌هایی را که مطرح می‌شوند، بیان کنم.
اولین نظریه این است که اسرائیلی‌ها در حال تحریک ترک‌ها بودند. اگر به یاد داشته باشید، ترک‌ها در شرایط مشابه، یک هواپیمای روسی را سرنگون کردند. این یک بازی بسیار خطرناک است، به کارگیری هواپیماها در مرز بدون اطلاع‌رسانی و بدون توافق.
این بخش جدی و نگران‌کننده ماجرا بود، زیرا من می‌دانم که ترک‌ها – سازمان اطلاعاتی، سلسله مراتب، وزیر خارجه، رئیس‌جمهور، رئیس سازمان اطلاعات – همه بر خویشتن‌داری تمرکز دارند. این واقعیت دارد. آنها تهاجمی نیستند.
آنها علاقه‌ای به حمله یا حتی درگیری در هر نوع رابطه خصمانه با اسرائیل ندارند. این برای منطقه خوب نیست و برای خودشان هم خوب نیست.
همه به دنبال راهی برای خروج از این وضعیت هستند. از نظر ترکیه، این راه خروج، بیشتر از ایران، یک راه حل برای مسئله فلسطین است. این واقعاً مشکل اصلی در میان مردم ترکیه و جوامع اسلامی است.
بنابراین، یک نظریه این است که آنها فقط در حال تحریک ترکیه بودند – که این یک ایده بسیار تهاجمی است، اما شاید به خوبی پذیرفته شود، به عنوان یک طرح قبل از انتخابات. این یکی از نظریه‌ها است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/143107" target="_blank">📅 01:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143106">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1803367449.mp4?token=D6E0ydtvwcwBRVcLt4CLk9Br5gXtOAqsf28BvbpJKqzAHC81yq9ZDNVD0APDkwsVmuW64QNIUpnQUL4SyquLbyjgky_e7hqUUYGs8umpn8bNr2Dc0QG42AuFXktSTWgMknl0LisyMBJnPNYR2a4gw03_f81gMlsNqCjGSL63v4gaZPxKm2zq3no-PrBN-AxfX54ngTuF71AGOR0wDPOT0CzTQv3HhHuogl_A9NclvNR2_IbH4wpOvH_sKmTaQEkqfBSgt5u9qYbxENg1adfRiLDzXzAL2eltPEBjkyCbDe9aX1vywAIEpXaYctp8G35p7o81bRJsc5aX84qktoOYVAr2JnSu5e8hCUt1WdaUkRdrWoo803jrYNjgNYxWAPkm1xz2yOpL6AG24us_rrkp2XB5K2mLkIQjFl8Rd0d4Z30Qn7SPcrlXMupNX42Cv0eic4xopnSI-0al2oQpJO0WEtDI32NIvAl6i5Cu6YpR2geGuLa5KMbVSqwpvQwwNP4ZCmTdeYzyRULNwwPAGwWFGhmxq9WAASoeC0RBwBli3JqCNxFFACrA9dBQpKKgUAZ7qPyzEiBEb5CzE6S20Op0mdQ5kwtx1pHg1TCvuie9BaWwNKzkFD_DJrtwsvyIav428uZDV_JpBsStsT7CRfgguA4yAitJ1p6pQFQP57_Ns7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1803367449.mp4?token=D6E0ydtvwcwBRVcLt4CLk9Br5gXtOAqsf28BvbpJKqzAHC81yq9ZDNVD0APDkwsVmuW64QNIUpnQUL4SyquLbyjgky_e7hqUUYGs8umpn8bNr2Dc0QG42AuFXktSTWgMknl0LisyMBJnPNYR2a4gw03_f81gMlsNqCjGSL63v4gaZPxKm2zq3no-PrBN-AxfX54ngTuF71AGOR0wDPOT0CzTQv3HhHuogl_A9NclvNR2_IbH4wpOvH_sKmTaQEkqfBSgt5u9qYbxENg1adfRiLDzXzAL2eltPEBjkyCbDe9aX1vywAIEpXaYctp8G35p7o81bRJsc5aX84qktoOYVAr2JnSu5e8hCUt1WdaUkRdrWoo803jrYNjgNYxWAPkm1xz2yOpL6AG24us_rrkp2XB5K2mLkIQjFl8Rd0d4Z30Qn7SPcrlXMupNX42Cv0eic4xopnSI-0al2oQpJO0WEtDI32NIvAl6i5Cu6YpR2geGuLa5KMbVSqwpvQwwNP4ZCmTdeYzyRULNwwPAGwWFGhmxq9WAASoeC0RBwBli3JqCNxFFACrA9dBQpKKgUAZ7qPyzEiBEb5CzE6S20Op0mdQ5kwtx1pHg1TCvuie9BaWwNKzkFD_DJrtwsvyIav428uZDV_JpBsStsT7CRfgguA4yAitJ1p6pQFQP57_Ns7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤴
چی بودیم و چی شدیم!
🔴
لعنت به ۵۷ای‌ها و رژیم جمهوری اسلامی که نه اینکه عظمت ایران رو از بین بردن بلکه خاکش و فروختن به عربا، آبش رو خشک کردن، به طبیعتش رحم نکردن و هواش رو سمی کردن.
🤔
بماند چه بر سر ملت آوردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/143106" target="_blank">📅 01:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143105">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa5f32711.mp4?token=ZFulbY-Mr4WpaeqsYkddRlOsRzcOcSPi5zUhncm20515kuNAleb4oqhyYOMRYN-w4QgyiL-Chttnq4aOk1J2MYzYX3n9Eu6qglWLbxUDvkl-8FlBfzuCWQItYEuABZ9gXpLxDpQRFgfwg61MbAHOP3q25p6nAFe039boI7wt0Pm0dX4l14kgjtCbQIzdbKB1-I895akLWK4vv-WlWKLoqAA8XRr5ccgHw2isHI1NgBoa-dyyCgwmyABdIJiWqqOJs6IxDiihGLUzdl_cCy3hAG9yE3dwKjaM709LMtXPUeG-quE1MeUzqInu4jI9ayEC0LwGC37nqnqM8sHi4Qzoaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa5f32711.mp4?token=ZFulbY-Mr4WpaeqsYkddRlOsRzcOcSPi5zUhncm20515kuNAleb4oqhyYOMRYN-w4QgyiL-Chttnq4aOk1J2MYzYX3n9Eu6qglWLbxUDvkl-8FlBfzuCWQItYEuABZ9gXpLxDpQRFgfwg61MbAHOP3q25p6nAFe039boI7wt0Pm0dX4l14kgjtCbQIzdbKB1-I895akLWK4vv-WlWKLoqAA8XRr5ccgHw2isHI1NgBoa-dyyCgwmyABdIJiWqqOJs6IxDiihGLUzdl_cCy3hAG9yE3dwKjaM709LMtXPUeG-quE1MeUzqInu4jI9ayEC0LwGC37nqnqM8sHi4Qzoaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مینا نامرداری،خاله معروف در ترکیه: حسین ستوده(مداح) اسطوره هست و عاشقشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/143105" target="_blank">📅 01:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143104">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0431f22324.mp4?token=uR8PYLWl65aihhc_rlc38yvbvj1Xad3dljHhId6teV5be7yHIlsiUVjBNwOBXQXji8op8hD08wwzSfEc2YaOPqvysjos-gYl_QCN9zbsF_0ikXivgiV-2mNooJmyzLxQWUZIGlsmh1OUnWqtPDmLBpynSKiZYMPNs7-u_t-tw5NJIFA5XkrmqIP9lPtYsLhLMWgXkm6ALZ9gXhYRDgBPIthq6ACnxrESP8RiQaLI2yWUO7UDucvmMJhDKpRD3ZT3arISLQ8AoMkLaXw8zhwsxzxaky4PKYhEGlZmqAe0GrP6aBZy0cO0bdTopXp2buH6geIZqiig9QZFdp9bnkXBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0431f22324.mp4?token=uR8PYLWl65aihhc_rlc38yvbvj1Xad3dljHhId6teV5be7yHIlsiUVjBNwOBXQXji8op8hD08wwzSfEc2YaOPqvysjos-gYl_QCN9zbsF_0ikXivgiV-2mNooJmyzLxQWUZIGlsmh1OUnWqtPDmLBpynSKiZYMPNs7-u_t-tw5NJIFA5XkrmqIP9lPtYsLhLMWgXkm6ALZ9gXhYRDgBPIthq6ACnxrESP8RiQaLI2yWUO7UDucvmMJhDKpRD3ZT3arISLQ8AoMkLaXw8zhwsxzxaky4PKYhEGlZmqAe0GrP6aBZy0cO0bdTopXp2buH6geIZqiig9QZFdp9bnkXBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید مدنی فعال سیاسی و جامعه شناس: چرا حکم بابک زنجانی اجرا نشد ولی آن بچه گرسنه اسلامشهری یا نازی‌آبادی که در دی‌ماه اعتراض کرد را سریع اعدام کردند؟
🔴
چرا نظام در برابر انصاری بانک اینده و بابک زنجانی انعطاف نشان می دهد اما در برابر جوانی که برای سیر کردن شکمش به خیابان میاد هیچ انعطافی نشان نمی دهد و اعدامش می کند
🔴
پ.ن: چون فاسد با فاسد کاری نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/143104" target="_blank">📅 00:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143103">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ:
کنترل کامل تنگه هرمز دست آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/143103" target="_blank">📅 00:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143102">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316345b8f0.mp4?token=LKXK-uLJcI2c3btRSYIlYlaHX7oUwt2egRrHHNGH5iYiWsq5FiIbYZcHYzwoF4UBbafmFckttM9N3Tx4ZMywyjDXMOYGp0rNwdDZKZUsqA6NHw-g6NSWJzbJIA-n8vGmusG29JC5adBpger8yCOH_JFGdkEud3Im7wt_WCSi9-rn-ik6ajSftuueBjaFP7g3r872g6JhheXKZQfS7d1g8x1yAhB0OazaAjK6XXDAjGRUOx5zJ9uNtxqi9en8GHPBBJZjfw7T6oEYHWK1AydVFcU1lMe_b2Wz64HXVh4ot0JoUEB4KWAZf7SSdYr7AAtQnVW2ReClmNxn6JmBErcz9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316345b8f0.mp4?token=LKXK-uLJcI2c3btRSYIlYlaHX7oUwt2egRrHHNGH5iYiWsq5FiIbYZcHYzwoF4UBbafmFckttM9N3Tx4ZMywyjDXMOYGp0rNwdDZKZUsqA6NHw-g6NSWJzbJIA-n8vGmusG29JC5adBpger8yCOH_JFGdkEud3Im7wt_WCSi9-rn-ik6ajSftuueBjaFP7g3r872g6JhheXKZQfS7d1g8x1yAhB0OazaAjK6XXDAjGRUOx5zJ9uNtxqi9en8GHPBBJZjfw7T6oEYHWK1AydVFcU1lMe_b2Wz64HXVh4ot0JoUEB4KWAZf7SSdYr7AAtQnVW2ReClmNxn6JmBErcz9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
من فقط معاملات خوب انجام می دهم.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/143102" target="_blank">📅 00:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143101">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها دیگر پول ندارند و به پلیس و ارتش حقوق نمی‌دهند‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/143101" target="_blank">📅 00:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143100">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
خبرنگار: آیا بازگشت ایران به جنگ اقتصادی به این معناست که گزینه‌های نظامی آمریکا محدود است؟
🔴
ترامپ:
نه، اصلاً اینطور نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/143100" target="_blank">📅 00:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143099">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: تورم در ایران بسیار بالاست و به 300 درصد رسیده است.
🔴
آن‌ها مشتاق به انعقاد یک توافق هستند، اما هنوز برای امضای یک توافق مناسب آماده نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/143099" target="_blank">📅 00:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143097">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa01c7683c.mp4?token=YeUqSGp0aT-bcK2dbwFUYAFBtdx9QVKcPtQ_NPxkyHfRPVwm9RY78GV19HAJjkuzL0hWEuCnszt1dwwFlYGC_OAQ4egEsXBopDxwYGD1paAhsQWZWX3ST6Wbj6l2hKQPgrNE1-EfEmcIJ-B7UF3GvpPJvDLuQs-G3o65qwpUVCd_V0ZjINKsiLT-il3Im-zhfvIK4cYDmqm0-X7ltf_19Mz8qPfcNOdc2ED-OtizTG37w-bL-hb8HfdMJ2_ZGG2jVAUrZq-huhTz7zjXE4jpJq1cSbJVcPgZZdaeRv4WWqvuLqr134MZKVSjw_lmk_k3vpyp7bymLt3yU8udUae4cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa01c7683c.mp4?token=YeUqSGp0aT-bcK2dbwFUYAFBtdx9QVKcPtQ_NPxkyHfRPVwm9RY78GV19HAJjkuzL0hWEuCnszt1dwwFlYGC_OAQ4egEsXBopDxwYGD1paAhsQWZWX3ST6Wbj6l2hKQPgrNE1-EfEmcIJ-B7UF3GvpPJvDLuQs-G3o65qwpUVCd_V0ZjINKsiLT-il3Im-zhfvIK4cYDmqm0-X7ltf_19Mz8qPfcNOdc2ED-OtizTG37w-bL-hb8HfdMJ2_ZGG2jVAUrZq-huhTz7zjXE4jpJq1cSbJVcPgZZdaeRv4WWqvuLqr134MZKVSjw_lmk_k3vpyp7bymLt3yU8udUae4cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری زیبا از تهران پس از جنگ.
🔴
پ.ن: جماعت دائم التحریک باز نکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/143097" target="_blank">📅 00:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143096">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اگه توام دنبال پارتنر هستی بیا
👇
@sesoteBot
@sesoteBot
@sesoteBot
@sesoteBot</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/143096" target="_blank">📅 00:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143095">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏
👈
گزارش ها از شلیک گسترده تانک ها و خودرو های زرهی ارتش اسرائیل در نزدیکی شهر نبطیه، پایتخت حزب‌الله در جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/143095" target="_blank">📅 00:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143094">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/efcbd0652a.mp4?token=T5osPYA6exR6l0X0fDtFCYScRoRqM1MChFTViqksvLjOko3ihdHkVBSpTYcogmnyd3lv44xToW3L1g61EIwDvYF0dXQgH8WQepSgR72XNdoOfZbhx3wqAVTxtmLWG22-ech03SvfTDa5Wm1L47sjbKNRIWURY9CZZPjrO3rqHywLCS54SLbwkmbxQFNEBdxUawjyQSbUN37Cl6XsqHRVj7Mi5Uww7LwonsccZkK05rMd_6m8LYmPdJ4QqTiI0fwlKyUMsTIt6tG9F6oBJM3aDZOsEs16rhX_q4p29gDqzaEJKQz_78IYwIZmAdI1Z-D4DXK030ruJ_Rkh3o40BfoKGDF0RARFIVna92xZ3ld39egW3Etm1E4EGQ6MPCBh-R1ro7yPxy95wMOlkCJKaoG1hIm1QZ4cx53bzToL1zxdgxuom6nOLcjIBeHwX8OJ--SwmzA_roS_gNtRY5kP710zTI1ui2anaezOEHy-p7XI3N58sFsXmx_gE8yK6-nDYFJvDcTQl6R8iifMWKOcNyJGMk8wbt2QZo6SrT6odWSYRLtkrQIb1Ni4LJsF4MzRgkQiL7twCq8uPBK9tH64o0MG4Dn61G0Tg90b1wYgwkniiXoNeSPgzg8XXrNFzS_uqsUw9kMaLQ5QP99w1RE4MlzX7duavDvyobEi4JGfK8Py7M" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/efcbd0652a.mp4?token=T5osPYA6exR6l0X0fDtFCYScRoRqM1MChFTViqksvLjOko3ihdHkVBSpTYcogmnyd3lv44xToW3L1g61EIwDvYF0dXQgH8WQepSgR72XNdoOfZbhx3wqAVTxtmLWG22-ech03SvfTDa5Wm1L47sjbKNRIWURY9CZZPjrO3rqHywLCS54SLbwkmbxQFNEBdxUawjyQSbUN37Cl6XsqHRVj7Mi5Uww7LwonsccZkK05rMd_6m8LYmPdJ4QqTiI0fwlKyUMsTIt6tG9F6oBJM3aDZOsEs16rhX_q4p29gDqzaEJKQz_78IYwIZmAdI1Z-D4DXK030ruJ_Rkh3o40BfoKGDF0RARFIVna92xZ3ld39egW3Etm1E4EGQ6MPCBh-R1ro7yPxy95wMOlkCJKaoG1hIm1QZ4cx53bzToL1zxdgxuom6nOLcjIBeHwX8OJ--SwmzA_roS_gNtRY5kP710zTI1ui2anaezOEHy-p7XI3N58sFsXmx_gE8yK6-nDYFJvDcTQl6R8iifMWKOcNyJGMk8wbt2QZo6SrT6odWSYRLtkrQIb1Ni4LJsF4MzRgkQiL7twCq8uPBK9tH64o0MG4Dn61G0Tg90b1wYgwkniiXoNeSPgzg8XXrNFzS_uqsUw9kMaLQ5QP99w1RE4MlzX7duavDvyobEi4JGfK8Py7M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده، تصاویری را منتشر کرده است که نشان می‌دهد جنگنده‌های F/A-18E و F/A-18F Super Hornet نیروی دریایی ایالات متحده، که بر روی ناو هواپیمابر کلاس نیمیتز به نام USS George Washington در دریای عرب مستقر هستند، در حال آماده‌سازی برای انجام عملیات‌های شبانه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/143094" target="_blank">📅 00:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143093">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
خبرگزاری فارس در یادداشتی با انتقاد از صحبت پزشکیان درمورد لزوم پایان جنگ نوشت: ایران جنگ را آغاز نکرده که پایان دادنش با ایران باشد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/143093" target="_blank">📅 23:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143092">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrzorxgtI8Tvk3UGY0n06tR0pn2q63bWblFqu9PGLtoOlqWsuWTcQ3CkHXQu2X4mY8dtaLVMY2BA5uze1hu_TSxpzDTbNWMfq1vgwlOTXcvptK9GmwqApRWVP_Nyz5pYQpZEQYipxEWIw8gOjkG2Q75loyKe3mgqojAQ16_cO4mjzja7IJEdHqZMkomfbCDqo7zpDXfwbMmLXElqWGctglkVvBG07WlhziRtuO20E1rHzncGcd2XW7V3YjYBXrGKZ_EgldIwniwInQZWyjGr_GgxP0PH0joxtEJGb77SuYxjytTqkDvqvpRys7CAyw9xGuLPPVfkHwwAlG88DYvtrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینستاگرام، صفحهٔ «رواق دارالذکر» را مسدود کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/143092" target="_blank">📅 23:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143091">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKDv8WbpemiXCR-YhIlpBzmDhG1_Rt0Y_u4__IlWKB9Jw67eD3769OFo9yZodvjSVBoCBLC2eEsr9-bzSYQN4vGlUjXpjcAYNsM7FFOtrA55JUJbTzrJBPVL82dRuclMZgyVIP-CoBBgiKBlS76U-t7pfLsefhX6vcocPQ9llM0nHzy7F0mRsC-grXOy2BYQTil2vmA4wwWxC6ITpuKKtJA2uiTwxyyUq5JAFayBAo3B76rXFoGve59jQlAfAYdjIy0sbugCpkyDTOcX_kOmxuJJG9otT2umUkh61ODUubAACjqeAOYTBlI_-mgqglJxPNHBtcimVBBi0DXu9MW9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی جنگنده‌های اسرائیلی، تپه علی الطاهر در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/143091" target="_blank">📅 23:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143090">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
حسن‌نتاج، نماینده بابل: ما نمایندگان نسبت به بنزین ۱۰ هزار تومانی نیز معترض هستیم، اما دولت به دلیل شرایط موجود بر اجرای این طرح اصرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/143090" target="_blank">📅 23:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143089">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
گاردین: ترامپ برای هرگونه اقدام اقتصادی جدید علیه ایران، ناگزیر خواهد شد شرکای تجاری ایران، به‌ویژه چین، را هدف قرار دهد؛ همین مسئله رویکرد آمریکا را دشوار می‌کند
🔴
سفر رئیس‌جمهور چین به آمریکا در ماه آینده نیز ممکن است تلاش‌ها برای اعمال فشار بر پکن درباره واردات نفت ایران را پیچیده‌تر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/143089" target="_blank">📅 23:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143088">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
به گزارش فایننشال تایمز، اوکراین به دنبال کسب مجوز از ایلان ماسک برای استفاده از پهپادهای مجهز به استارلینک برای حمله به سکوهای پرتاب موشک بالستیک روسیه تا عمق ۲۰۰ کیلومتری در داخل خاک روسیه است، چرا که کیف با کمبود شدید رهگیرهای پاتریوت مواجه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/143088" target="_blank">📅 23:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143087">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
تصاویری از پهپاد های فیبر نوری روسیه در حال درگیری با نیروهای مسلح اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/143087" target="_blank">📅 23:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143086">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
سه تا از گیم پلی های لو رفته جدید gta 6 که هکر cyberleek ساعاتی پیش گذاشت و چنلش تو تلگرام بسته شد  برای دیدن کلیک کنید
🔴
اگه دوست ندارید اسپویل بشه نبینید  @TitrDaily</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/143086" target="_blank">📅 22:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143085">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1ApP8FsNlX1YPQtMOighCUTHfMpXbaeCxBKUWUjVdZta572K1-HJI0EAXGpEpSNl8FAf0tsE8pRgs2IAJaTMWNgbrVpT0Hei8ZfY0O7AeWMdKJG0MD6YpK1ekkusozJDQAIzDyF8ffWswQcgpJbtqh-xlbkqa-Kz-1xdH9ub_aH4nVP3L3YobfhQLsJmKK-Ol4IqCexzXryoikAyqGh9eNvXlkrtDTJEQ09f4sFvXYaMP-z8dNLqUpS5EWZt8IlQLQON2jZg5YB5ynGQsK-G7tOA761ULhmAeN6VD5qfC6_C3UCBV4-qarCSctFNhqPxPpwpRgYcMVBy3bTynctBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر یک روزنامه سازندگی:
صادرات نفت؛ صفر
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/143085" target="_blank">📅 22:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143084">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1b5z16pvZaYcFK5iLX6FfXiZzjNOQku6fYUfsPiXTgg4iZdWeFhvuNnLv2qhNbShoZbqyq1ixTBn3UyMBqsUJU-1C65YxmGjBldAkoKoB69YEciOR25JEaVEnWCbKPk4NgKBjksuKu1_RHYBotqs5iYXy6DGYUihXgkrFdA6WlL27UIxCS5zS2beMjLqc1ENPBljoFKvhbBfzkiGdnug6TuG6f6LPBPzOG1d84wBHak4OAVr0tivELFVrnKALK8_tL9CuWs-Iu7VZUEkbe0I6xEaFxfVJMUAdRV_GdsL2YLqPTHa-1adxZUEeTpSh5Mt1tz5cB8QFwlQ3HqQJXLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت‌های نظامی گسترده آمریکا در نزدیکی تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/143084" target="_blank">📅 22:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143083">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نخست وزیر عراق: قصد داریم تولید نفت را طی شش سال به ۱۰ میلیون بشکه در روز برسانیم
🔴
بستن تنگه هرمز چالش بزرگی را ایجاد می‌کند
🔴
ما در حال کار بر توسعه صادرات نفت از طریق بندر جیهان ترکیه هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/143083" target="_blank">📅 22:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143080">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aH8J8ZAI2ek_kTG3Zcrk78ZAsHO7csUZcpWqobTp8R13CMxscC_UE4ILm9iZ_mJG-G-j3M9AIcF_D4xr8mL0p-5fe38YA0wq4kn2Mr_EATnNShU8OWJN8n0ejI0yO-IkSwGTS4uN8cDVWy43jQ_kw3_I3x8OjYr-xMqI73imK1clVK4QWAXV8Ou0GH33kF8E3E6fEjME8iuZvQMOmv8wd6eH9UeMZCJ18OAqdSoW4NaaG4WQq0NWKwRiWbmKQhBuQW4e-3VqwdTCMDd-EKl4LikQRmGpyixs3Fa-VA5AW8xJzb8Wt147zSTX5BIa8BgpGsfMLeLhElOa2zfxmmqOVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iixdTFUrj5aVpkeiPBlLn6IS-RQFQOiVCpDcdrJyZmaoY3c7GBDuGQqjmnrSxGGc-_IdxXhcA3toZP2SeJaAJsS8JXIrMxaJBkTiOZU9avl4d6wMgm9OHojKVK2p6PTLF15sx23tsCMPt8n0pNTzWweCiakZq_VhPr9gq-FD7iGzO8C8D6xC5XEaOcacgLmh-rRWq_i0eX7fMtxh9w65jDLKwxtAeYbXLFDXH_0kLrRUFTtOUICy35T8XDpN7wPIMTbRb9fk2OUwy6Ae6TDGpMNjEt-ZLb6m-feFS4zpqjl59sr-eHV7RwLazrgwFvjpnK4By3bCI6lJ8cIlKnbTow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpqDHSsN-NXkNBJBaEA6Tuw84_84g42IDIWmn03ijD48PZdpV7yUb4jfsYsSyVqPgGRYXmVE0Hu45S0v0zR2ScMXn7TQxFZm1mZa6aHnzY8ooaV26LCD958aFaTq9GPshI2T0FCvCCzuxlQ0i8P6B96PcYPbTSx4crisoZ0umdh4H9_r1P48gJejfCRWy__sKM78FA-VsI2XzkPhw92xWE5VXZXevl7Ym8WDWJ98jHUBkN_FIqFFRC2oKDJSOWsWwbHbIpPGQPReVTdBw-UKK1l6kFLGYEKkv7NK386i9UsE0zr-wjQNwPMGQzbsuvJB6wnQcZ9vDktCgK2lHwSY2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک پهپاد عمقی مدل FP-1 متعلق به اوکراین امروز در سواحل دریای سیاه، در منطقه کارابورون، واقع در بخش آرناوتکوی استانبول، پیدا شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/143080" target="_blank">📅 22:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
الجزیره: هیچ نشانه‌ای وجود ندارد که پکن قصد داشته باشد تحت فشار آمریکا خرید نفت ایران را متوقف کند
🔴
پکن وابستگی بسیار شدیدی به نفت ایران ندارد و اگر واشنگتن فشار کافی وارد کند، می‌تواند خرید نفت ایران را متوقف کند، اما چنین اقدامی برای رئیس‌جمهور چین، هزینه سیاسی قابل توجهی خواهد داشت
🔴
تسلیم در برابر فشار آمریکا می‌تواند در داخل و خارج از چین یک سابقه خطرناک ایجاد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/143079" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143078">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e316f6b04.mp4?token=Kc4qz6SX9T4NwR4yHrSETAOen98d3LRFL2_VBQDLKzs3bw-q-NXH_Tc2IcBnD495SOqbzWpm06l_Hcfqj8y-4ZiWTkbIgCyHP1Rftb4seaZdv2TGhjyOdxZ83F-AX4z_d0PFUMRr3Jb3zs4MMNDu61gWkXatLTwlcWmeIRtgihaWJNDNx4aq2ZPuyZopo0yCzhW403SC5KC2eipa7XZQM5OfVgUbTYaRImrC5OZswCfn6U_KgyrkLlblyfJsvpxdRTUNLFr2yEwEMXYSKCZzRnL1IHwp5rlCFUNPo46o6kEXiLQC1B3dkztAAOJ7TYOMGyndNKwB2nxyojcPTS3PVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e316f6b04.mp4?token=Kc4qz6SX9T4NwR4yHrSETAOen98d3LRFL2_VBQDLKzs3bw-q-NXH_Tc2IcBnD495SOqbzWpm06l_Hcfqj8y-4ZiWTkbIgCyHP1Rftb4seaZdv2TGhjyOdxZ83F-AX4z_d0PFUMRr3Jb3zs4MMNDu61gWkXatLTwlcWmeIRtgihaWJNDNx4aq2ZPuyZopo0yCzhW403SC5KC2eipa7XZQM5OfVgUbTYaRImrC5OZswCfn6U_KgyrkLlblyfJsvpxdRTUNLFr2yEwEMXYSKCZzRnL1IHwp5rlCFUNPo46o6kEXiLQC1B3dkztAAOJ7TYOMGyndNKwB2nxyojcPTS3PVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: ما هرگز در امور داخلی عراق دخالت نمی‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/143078" target="_blank">📅 21:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143077">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_TBIDc_EL5Dm_fdxrM8zU-ShmqPt7XTNPEHzScQIvgG-90Nik-kasiL6Wr7_cgWkHp5IhGevOYnLkAiIMWP6TeUl6yITa2j1Szjj6Uhd40QUC7dPtQ9BbObO96ZYt1UgeBKuHCMcdtUVCoNY5P4sjSRVtN-lFgJRqpY8ndIaBxX7EiA058_E3wz1Iu86e6lmEAT9mWAK4MoIpfZgiKzJ8zA2aSq1_Xoov_iK5I3X1e4YhjXj1JDBhV6Ro-AKIdBV5SjspfkR1Zbil3V5y8HA9zTpQck0d0zl2Ndcle3UJ4RXHLfo6pi5f2blZqRyF1q6z42ZOCPxYV8mrTDiTrwTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس وایرال شده از پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/143077" target="_blank">📅 21:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143076">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXlcFiH76aBZ2tu-Z5or2JorkLUYzA2KQmMEbiw9IMBYKOFtqiSM9LplPvPM0iHdexG3J87uJoTJ5KKpzA8d2J8DO6U8ZnU5UL_AG8_40d-J3cyfp6SzdUbPDyjWxJJl4VI8vq6P9z-XoO7J4Pjm0aIJAZ1cj77S0nZwomRibNUWDBY5NqdYZ-lYYOituqLtwdM7tkl0E_Y4xB5vzeGhxd5Pyu8e7xixAOhUus9YXTMcAhVuFQi-YvBAu7_Zw7_bUpm-vSPTKrd70Q6vpvsD2X-eM6YMnQKW_pI0XLWN4Hddclzu-1HODpvsBpIBGS2Ns50oNDga3cT8idAtnFU1Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف و هیأت پارلمانی همراه وارد تهران شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/143076" target="_blank">📅 21:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143075">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNyBWOb-Ktl12Py9gMANZAaXbPj6RdjwjoOpt04DuqQyawy8JDDJHDoeJvlhbAxrPUGJF4bDVBqc7zfprzthAvIy8yy68tSLdE1wqJozfM45UKICjUJOymo6vFS-07AnBUhxXZNdVBxIGoI1ivAlFdGu33S100RM1d_WhLMgIQFz1aNkKNN31-puOk4WiVR0AyuGN_J0EYVb2nXXRE7haIIZMlPCMEWsZv0G24VH97IbE225WKGYrMp7A_-_jiy1UXwqXyjR8nR-hwUEsM0jEu1jovOy0Kw3IUYGbvOREuoRrL8Ku4ZzVQapK8eXb-Du_7DZBWHzcQsUAaEDS1Fkmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بازنشر کرد: رئیس‌جمهور ما به ایران هر فرصت ممکنی را داد تا سرانجام رفتار خود را اصلاح کند، از نقش خود به‌عنوان بزرگ‌ترین حامی تروریسم در جهان دست بکشد و به کشورهای تولیدکننده بپیوندد. او درباره پیامدهای ادامه مسیر غیرقانونی و وحشیانه‌شان به آنها هشدار داد. اما «رهبران» آنها چیزی جز رفتار تروریستی و قانون‌شکنانه نمی‌دانند و اکنون رئیس‌جمهور ما به وعده‌های هشدارآمیز خود عمل می‌کند. این‌گونه است که رهبری واقعی عمل می‌کند!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/143075" target="_blank">📅 21:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143074">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da64c04333.mp4?token=aDJCHkk0mtfS_TT4lkR8k2GHZKXrfGHx4-9pC5zwr8Ko351htRE4ykusW4dh4hktWC4Et-fhciUPLrdDMld8ezZbaHHg2_UeUbpTI2qGSYlDoGgba4h7Y__cFyiYHBZU4ZHWD_P-pyWvQ3xZa1X5YcGftrvz6XrdloALT242zHRqDIPil9WrfFa00s3qHJ1O5LFtCAghx4UuFW6-tDWlFSLshPgEz5kCvN92iG_0rLPjg08sfHJQEDKvzihdaBP4f1EdYyagKZr-pnXghnwLqY3YRJMVo4-P_rVD6tjGj_Li2dCZ0ugquvNrc1xOnKjqgrmEhJ1BIoRxibe5ypTDBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da64c04333.mp4?token=aDJCHkk0mtfS_TT4lkR8k2GHZKXrfGHx4-9pC5zwr8Ko351htRE4ykusW4dh4hktWC4Et-fhciUPLrdDMld8ezZbaHHg2_UeUbpTI2qGSYlDoGgba4h7Y__cFyiYHBZU4ZHWD_P-pyWvQ3xZa1X5YcGftrvz6XrdloALT242zHRqDIPil9WrfFa00s3qHJ1O5LFtCAghx4UuFW6-tDWlFSLshPgEz5kCvN92iG_0rLPjg08sfHJQEDKvzihdaBP4f1EdYyagKZr-pnXghnwLqY3YRJMVo4-P_rVD6tjGj_Li2dCZ0ugquvNrc1xOnKjqgrmEhJ1BIoRxibe5ypTDBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: سیاستمدارانی که با چند هزار دلار به واشنگتن آمدند، پس از دهه‌ها خدمت عمومی با میلیون‌ها دلار در سبد سهام‌هایشان از آنجا رفتند.
🔴
شما چه چیزی به دست آوردید؟ ما چه چیزی به دست آوردیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/143074" target="_blank">📅 21:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143073">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مدیرعامل شرکت نفت ستاره خلیج فارس: استفاده از متانول در سوخت در کشورهایی مانند چین، آمریکا و اروپا تجربه شده و این ترکیب هیچ آسیبی به خودرو وارد نمی‌کند و قرار است این ترکیب در ایران نیز انجام شود
🔴
پ.ن : ماشینای اروپا و آمریکا کجا ماشینای ما کجا
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/143073" target="_blank">📅 21:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143072">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKkQqnDlo8AUP6Ys-LDcmE_6NBkK1YFo8UAZ0Q1lLd92remfIb_G6aV0rZdB2mRYiozABevieVchdws1OheI6IVxHLLbpEfVGn6-pE4JhoDsxnp_Y_TqtMeB4VttacOAkSMfKZnos1fkkW9Kl_IMsMR9sgqRpFOS2F8xujIGR7YGW3Gb3GQjpgE7ZVHwA-9LuTDdkWiEXINZWSFVqOxFxTwax5dWNCRR8mvI8MX5lhEZDpx6JPTj2dsDaYKzp87Rf_JQNKED-nC1nnsMd8A7K-5dppEZjwpCaKG3_HZRvVcjd5l8exystsf4snnBEE8cBTInK2fik44KUlU_FM54Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
تصویر یک کاربر شبکه های اجتماعی از مقایسه وضعیت سد کرج
🔴
بهمن ۱۴۰۴
🔴
مرداد ۱۴۰۵
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/143072" target="_blank">📅 21:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143071">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pkypN1Lmz57P2_JJYKR4hJD4Y7eMnZYJoinwEFXa_wPoMhusQsLf5bbZ0UxLValToIWytrk2s2ulxr5XPhvlhdunIwGCECnj6Aj023U3CW1_-2-KsDBb0yA0vLnPt8byvq84ESVZ_oQOLZydj_tyjV0z3Bkgq9I0m8goKBWrfze6VC84SjJFzW95BSXl-v6lT5tYZ_BRCpoS-fbxoCyJ66gyJTBFH7WpLWOYs9Seigy0mvHIhpSRh6c4fSw8HEKg2DarX-1nSJ9C91LJyezud8fGDtk8n4qwaM-7xAXaUbVPwezT7JGCHtd07AQcalz_6zuFzHJTxLIBFJE3gjRFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا اعلام کرد پرتره ترامپ روی سکه جدید یک دلاری چاپ خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/143071" target="_blank">📅 20:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143070">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
فرماندهٔ نیروی دریایی ارتش: به‌زودی در پهنهٔ دریا درس تاریخی به دشمن می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/143070" target="_blank">📅 20:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143068">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkIBuRkD6qXT4HrHPE_iIOSmVUhbI4F_xnkyyX1u4FhdkfwV3OOiIZCEcMQwVMoTBl0hmZ1tOtiHmSFpQKQuYtRIkNprmqHs36cK3DlVxgZSZ_VrjWLvxWCJPyQRLU3t0XiyCUimaPoeIEcuQxI1NLerZ0slwcuvNnEfmTBhMkFLrbAlynr-tzOwEKT3yI4w7S3tCIVGzUBrAtLiXcwa8j524dJ-TNv_WciW1MsmAzirbvCZbEdAarA_OIPaIiOlI6by-Zz5Gl2kep20vIj1BnVm0c5x_Qrc7eZaU6IfdKFdrxFDs3LM_IJAZVowuPvr4gWvEWSVf3WHzs2XkvMn3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی انس طلا بیش از  ۲۰۰ دلار دیگر گران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/143068" target="_blank">📅 20:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143067">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
قالیباف: تفاهم‌نامه مفصلی در حوزه امنیتی میان ایران و عراق امضا شد؛ ایران هرگز در امور داخلی عراق دخالت نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/143067" target="_blank">📅 20:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143066">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
خبرگزاری رسمی عمان: وزیر خارجه عمان و عراقچی در تماس تلفنی، درباره آخرین تحولات و شرایط ازسرگیری گفت‌وگو و مذاکرات رایزنی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/143066" target="_blank">📅 19:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143065">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fptbjflhdbbxcfzb7PiNpLdq9HuCZAM9yPm3lhOnv_LqyfdEUkLqoiirTinWcfj-9EGAyEtpIWkorBIaGor7QWIvkzYZge8aJu7wCMOSczXisVJaR-s9af3HnaHbZZgN_oBJcCLEhIhmSxIqWdczLci8jNyS89RQgQcgdtWKwTxlKv47S3jqc0pvfyKetjASEPl2b2ixybQKRPFhQIp2WwyPDQJr5QlNRfjpxi77wWjPY2ewseanhA_zp0tMB1CV7i_qwMfhIg5r9pMBtutW75PVA-r4zVz8DlTzFT6lau_0SR3_eX-eHoHosFcE0V_QvsSRrI9jsgx9uqyH9OQj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش توپخانه اسرائیلی به شهر بره‌شیت در لبنان، در محدوده منطقه امنیتی جنوب لبنان، هدف قرار می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/143065" target="_blank">📅 19:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143064">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HS5HDXdVVxx7Yg0DR7y6wMiFzkeoLHB7AKFiIfjNke8D3Kxqzu_yBodcVVVyLexyzKiJ-GY7vtymYV-QfrV_V08aXf1Q90K1Ij_t3_clAPGIO2zeIzl9grzx4BExrWOc-jmHQys1ajxWtU50k1k93wDBgZEa3Nf77MRQDmplLfw9w475wtDL5c_Lp1OLuV1GgM34T4G62AR8HycjVN6El7iBHi2OUi0nBhzS8u2jTQjsDLKYZPHzc7Cmxo5z3Mu1Oe_m2l6JQym_M_KfuQASZH2jECAAMibsNZTnM25UXFu3S7yx2WQciKGgCNq5yUGEHTsBm8uQyaJNRQcAlmmP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس، ابراهیم عزیزی: آمریکایی‌ها ثابت کرده‌اند که زبان دیپلماسی را نمی‌فهمند، بنابراین نه تحریمی را برداشته، نه منابعی را آزاد کرده و نه دزدی دریایی را به پایان خواهند رساند.
🔴
اما تاریخ نشان خواهد داد که با زبان قدرت، نه تنها مجبور به انجام این اقدامات خواهند شد، بلکه با عذرخواهی از سرزمین بزرگ ایران، منطقه را ترک خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/143064" target="_blank">📅 19:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143061">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRfyu7VUpiC_Y1Bsb0s-vYYWIyYB67wKONsqXccZQ0D4TiCAGtC2H7nbPtU6aRxtWj-EMm6c52j5-DS4ae4wYMCUgG4HrwcDiHGAirjnYY_lj7IuQhohoGm5V0zunkBmOeN47VyWBMG3TUWPkmAADxTsy111qC_kDVDCrEYDjfLXjhx4lJkMh8_w182dkUiazQLAr-1zGpzxdou7hWg6jLN2zNz3D86LWJFuWItPmXYKnLVT54fT9KLeQ3MjN_-IgbFR4P6-XzohKCQ9i6AhK-FHD2Ghm53ls-4UqnI23z7TZO80b1Xx8uIrJVwLrh0A9tEPBvN1SdZMwNt23ao46g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQzFdW1lk7aP0143MGdwhiOdEhDhzF9LwB3TlpDV4pwBzN16vbNCAohbCQiR27MHr10ujMHPLl14koqtRlLU_zQ80q0C6uw76ddh05zDEyGOZiEZzGq4TfQlawoclO18YddTIwsevzXpGN0T1o_GkHZx_TBpDwNYFAGiToft3LRGxFbIl9ObOjausnqmmX_raWyA06Xzwq8SDBHZQn5pXXmdcYCbsyanFY1r0M-l5SiZFzeLjYocVNeZrKl3MdtcfIWllOyVZzjV0MQNfzJzxKA3Ij2LT72VN6Lf4xW4t27gEsOA_KSvHqOkwl9UJC6zosx0DFuumhOzveo3TN80PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ro0aIbuOihPBCH6LqlZQp9_cqWFe_e2JstWBlMZEwqMl5eH7aPCuYWEvixVEe_3qu37ZC3ON6muR6_TAujmfh-E7e5XenCa0GWJ6ZC8SvAyrGhLCffEDaapQfLOuVgkK3VeqDrwhJXfxdQQlENAqi_gBzJC-ONdcuyvFUKsWaQHQp-z5fXJAuwoz_02D3jAsL849g3TZjoRHS9iCSLkWKsc1CZvYKDGFHwdML3JxJ7Kq2oZaflL2PzgGr9Gy9STe_Cgwbdb5SyeW4zMuVKnmhPngroBdYtTpSm40KISQCA6j4wIB2F7AmZbNNL5imX-O-aeU6e7btZ6oceWtFrl7tQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">علی  دایی برای تولد دخترش یه هدیه حسابی لاکچری گرفته؛ یه BMW M2 مدل ۲۰۲۶ که گفته می‌شه حدود ۲۵ میلیارد تومن قیمت داره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/143061" target="_blank">📅 19:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143060">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
آکسیوس: بازار نفت دیگر مثل گذشته به اظهارات ترامپ درباره ایران واکنش نشان نمی‌دهد و معامله‌گران اکنون بیشتر از مواضع سیاسی، به واقعیت‌های میدانی در تنگه هرمز توجه دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/143060" target="_blank">📅 19:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143059">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
العربیه: محمد بن سلمان، ولی‌عهد عربستان سعودی، برای انجام یک سفر رسمی عازم فرانسه شده است.
🔴
دفتر امانوئل ماکرون، رئیس‌جمهور فرانسه اعلام کرد که انتظار می‌رود  این دو در مورد تنش‌های  غرب آسیا گفت‌وگو کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/143059" target="_blank">📅 19:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143058">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سید عباس عراقچی: ۱۴ سال پیش: «سخت‌گیرانه‌ترین تحریم‌های تاریخ.» شکست خورد.
🔴
۸ سال پیش: «فشار حداکثری.» شکست خورد.
🔴
۵ ماه پیش: «استسلام بی‌قید و شرط.» شکست خورد.
🔴
امروز: «سنگین‌ترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
🔴
ما قبلاً این فیلم را دیده‌ایم.…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/143058" target="_blank">📅 19:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143057">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
گزارش از شلیک توپخانه و حمله هوایی اسرائیل در المنصوریه، جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/143057" target="_blank">📅 19:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143056">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSNM8-7bsL0PE1t3XJ3eAs1ik8xNF4ll8YNbf9zQ_PZJ5YEk6K4qYTkgsQH8DVt99gmbV0VRJMoASGRWbpkpEciREDYSHy-6hpC__vVp1J4Md71ydBCBTgF5XwonwJKrqam-JziXQHGOEwSgehS6xbBxaMHypKGp8MxFz6Jz2S_xNEG-w1GRrI7vrwUYobWqID5Rz62R-zYsZoahUZPV-SsvWKlT9-hbTzTH2cJXw-2pjwyEiUrqonUqFOUyYp5ACM2_aKVaiH82xbxoBhY59F19LjBE34tLsRsvl5cNSXdFU-ZyhAjdcjUnFxvHaWKFZcbw6mEwgysNiOD_rLmLyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید عباس عراقچی: ۱۴ سال پیش: «سخت‌گیرانه‌ترین تحریم‌های تاریخ.» شکست خورد.
🔴
۸ سال پیش: «فشار حداکثری.» شکست خورد.
🔴
۵ ماه پیش: «استسلام بی‌قید و شرط.» شکست خورد.
🔴
امروز: «سنگین‌ترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
🔴
ما قبلاً این فیلم را دیده‌ایم. همان بله‌بله‌ها. قلدرهای متفاوت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/143056" target="_blank">📅 19:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143055">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزیر کشور بلغارستان: بلغارستان تمام اقدامات ممکن را برای محافظت از پایگاه هوایی بزمِر[متعلق به آمریکا] در برابر تهدیداتی که از سوی ایران مطرح می‌شود، اتخاذ کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/143055" target="_blank">📅 18:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143054">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b2c4df98d.mp4?token=P1VG7wpndNMIxPC9yJhSPF3NXNqb6vXYXMg9UC0AuW3BOgFUVs3AU_YAcZH71Y1zT338BmMzP4huUYmRl1W19fkrZbupmv5jsm3x8i-5U0Qz4ss27R4ygAUklPMLT2UOWwRj_zmIUeh0kE3jv-h9tBlXd9LLE7cgsLxzPqTfl6uYQAcAqpYdEw86zMvc6NxbstvmvQgib3iDQ-cUd7x6ATKZB7nSJc8nnlQVffw7a3mYsQi1MtvbVROfS7Gz1WbAOQNl7HFjlqHnEWUrZF_BoASkyvCLoJ2n0lvB_gkX1sC8vU67aETXn6II2leNE1SvWiw5SdyPv_3JIdDUf2NZ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b2c4df98d.mp4?token=P1VG7wpndNMIxPC9yJhSPF3NXNqb6vXYXMg9UC0AuW3BOgFUVs3AU_YAcZH71Y1zT338BmMzP4huUYmRl1W19fkrZbupmv5jsm3x8i-5U0Qz4ss27R4ygAUklPMLT2UOWwRj_zmIUeh0kE3jv-h9tBlXd9LLE7cgsLxzPqTfl6uYQAcAqpYdEw86zMvc6NxbstvmvQgib3iDQ-cUd7x6ATKZB7nSJc8nnlQVffw7a3mYsQi1MtvbVROfS7Gz1WbAOQNl7HFjlqHnEWUrZF_BoASkyvCLoJ2n0lvB_gkX1sC8vU67aETXn6II2leNE1SvWiw5SdyPv_3JIdDUf2NZ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هوایی اوکراین به پالایشگاه نفت روسیه
🔴
پهپادهای اوکراینی به یکی از بزرگترین پالایشگاه‌های نفت روسیه در پرم حمله کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/143054" target="_blank">📅 18:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143053">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل: اردوغان یک دیکتاتور یهودی‌هراس است که کردها را قتل‌عام کرده، از تروریست‌های حماس حمایت می‌کند، نیمی از قبرس را اشغال کرده و تعداد بی‌سابقه‌ای از روزنامه‌نگاران و سیاستمدارانی را که با او مخالف هستند، به زندان می‌اندازد.
🔴
او اکنون به دنبال…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/143053" target="_blank">📅 18:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143052">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
روزنامه تایمز آو اسرائیل: فرودگاه بن‌گوریون با شدیدترین اختلالات پروازی در جهان مواجه شد و میانگین تأخیر در پروازهای خروجی به ۷۰ تا ۹۰ دقیقه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/143052" target="_blank">📅 18:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143051">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU8cRIV4IQJXzLXMHnC_MEv2ugMaMsN3-ulEGht5g00PK75CvFEjstr5csvJq4gf7gH-_vr_Qc8yAs901zNjaptkspSST0KmoSpY7ZZZmlC_RBC7P5X7ZAtMBm-7_vBD7HLIcbmpD_6Aj7xRVGeFBv8DdOXw6RGA1Rfpr9fZpB1e6MP1bxW3kl9rJnUxEn27WdNYWgZ2JQFAJHT8uCz6eyvCvKD9Fz1tz_sAWDlxyuvFWREjDV9_2KMIpo6zdUrPFhc-Z71x39zV8ByZkmeQxv8wxnR8SXj2UBMsID8wjqFgvxwtmBk4bDG80uR54DiHSSsOzssp3lneNbJtE-hZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل: اردوغان یک دیکتاتور یهودی‌هراس است که کردها را قتل‌عام کرده، از تروریست‌های حماس حمایت می‌کند، نیمی از قبرس را اشغال کرده و تعداد بی‌سابقه‌ای از روزنامه‌نگاران و سیاستمدارانی را که با او مخالف هستند، به زندان می‌اندازد.
🔴
او اکنون به دنبال گسترش تجاوزات خود علیه اسرائیل به سوریه است. اسرائیل این موضوع را تحمل نخواهد کرد.
🔴
تلاش‌های مضحک اردوغان برای ایجاد ترس در رهبران و سربازان اسرائیل، تنها دموکراسی واقعی در خاورمیانه، به جایی نخواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/143051" target="_blank">📅 18:16 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
