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
<img src="https://cdn4.telesco.pe/file/gF2A3lKwkaisNQhpP8hTq1fpplwJXLaZw-Fcv2GG6qOMrov4rvWb9o_Cbk4OGVomY_RL3OrgIx6DsqGlOOvT_vsyzVfRk0Jg_QDNG7RfKZZzTeTnH48X6QHN44a4Wt3SE238iKinUvP6HbeV4IuOUQqaBPcnc3vL0CEhY-4hfjSVwRpopcwmjkgo5qeuP237ikeas8PH-wnA-c9KyGmZkY5HG7qUtwtCv2ePWudgX2Cnw7-QCgoeKs7SesHJnp8I2QBr6JW25APCZvvMdeQg7UYdFwDBPY9TiVkAATqCIagdh9vQcQXiIf2HAOpj5kbmBlR2_ZdnynX_76yFPuv-rg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 16:53:27</div>
<hr>

<div class="tg-post" id="msg-442579">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d885ce4dfc.mp4?token=BbrCYi8sgK8mBb-DHiI-ndFJ8ehgLzstg8eZw3J94-ChsgOVw5vUe8bkqz6UiRMPEWP43npOSOqQHM8LgAqYBR32I-Z6quG0uO8RqVzuX03Qe3LI1ld3-1TGvUxCIK2ZQvKkdJouZYtMkhGUTbrgUOKKSxwQUKKVgXTuFL0lqsds61rpIanO2oOANdP_8LysDyNdWDwgHFP9NUAXX23lpluzhZT-S1uG1ezjj9IrHudtTIjLNnUNneH3bi3AQjTq7LCL2u38PXqdwd-gA92CHhUgaH4W3Xpz1tRXcFuumTuMpThe_yR4ZxRmuyJPttWWIw3bDDJfldsoXFi6CcdMTgGKM30Z88EGPJ3dSw3qojLk30_MjgYpDi9h8QEMY_4kTJV97QNI_eIw31ZQrduSy3Koxb_fszS6ykBLLh_AwUrm7FgVReguXmTAc2pGpTA3dEc3VCf9cWmiVYjSuS7XvAJlon5EycI1HZ5TkYFMdzZfhendiaymJk9djG70-8BB3FK-qUjp0u9n-MW3fFxveIW4klf8Ad2Zzs-R4zMqBqAknqR4uUBU9tiTUQ6rN1CuLbeHZrs69SnWO1Dhv69ZYLAKM19OHIeaW696wEQqTC5yip7ltWfP-spE4-_0oPdDPsKxX8C3h4WINMkkINW7zoSrDS19Xx7sIGbya--MtV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d885ce4dfc.mp4?token=BbrCYi8sgK8mBb-DHiI-ndFJ8ehgLzstg8eZw3J94-ChsgOVw5vUe8bkqz6UiRMPEWP43npOSOqQHM8LgAqYBR32I-Z6quG0uO8RqVzuX03Qe3LI1ld3-1TGvUxCIK2ZQvKkdJouZYtMkhGUTbrgUOKKSxwQUKKVgXTuFL0lqsds61rpIanO2oOANdP_8LysDyNdWDwgHFP9NUAXX23lpluzhZT-S1uG1ezjj9IrHudtTIjLNnUNneH3bi3AQjTq7LCL2u38PXqdwd-gA92CHhUgaH4W3Xpz1tRXcFuumTuMpThe_yR4ZxRmuyJPttWWIw3bDDJfldsoXFi6CcdMTgGKM30Z88EGPJ3dSw3qojLk30_MjgYpDi9h8QEMY_4kTJV97QNI_eIw31ZQrduSy3Koxb_fszS6ykBLLh_AwUrm7FgVReguXmTAc2pGpTA3dEc3VCf9cWmiVYjSuS7XvAJlon5EycI1HZ5TkYFMdzZfhendiaymJk9djG70-8BB3FK-qUjp0u9n-MW3fFxveIW4klf8Ad2Zzs-R4zMqBqAknqR4uUBU9tiTUQ6rN1CuLbeHZrs69SnWO1Dhv69ZYLAKM19OHIeaW696wEQqTC5yip7ltWfP-spE4-_0oPdDPsKxX8C3h4WINMkkINW7zoSrDS19Xx7sIGbya--MtV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ببینید چقدر خوبیم ما...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 366 · <a href="https://t.me/farsna/442579" target="_blank">📅 16:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442578">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0c4fe8180.mp4?token=dtZeSTJO-UbingZUpby1JUBT0N64w7JQ21wdrqdUeE4gdrEL8PfQD8Xtppt0jRTfFqJG5FFGQcKVlYnHYA7O7riG1juytDnGltQkxuCGC8-M0aOmCIkD1Yp7eOePYrUUsPD4swYiylgemmP1cYB3MNcZFg-_27aiAjMLMoJuHCqHuGhfOhOFigRWn_CjccrYWSGaPLPs_VUBmT6D1MgMK4Xdls8RGbN8u7r8cDxeSRmn_WCFsKY9V6_agCdDy_OhBTVMM3CDjPrJXpCBhu4dX4pzXsAhCQlIhnZ14n_UVjJ0JZ_uZ9lZ-aZ75lImypXmTUqz9EsjAuMsDu3tyWBXBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0c4fe8180.mp4?token=dtZeSTJO-UbingZUpby1JUBT0N64w7JQ21wdrqdUeE4gdrEL8PfQD8Xtppt0jRTfFqJG5FFGQcKVlYnHYA7O7riG1juytDnGltQkxuCGC8-M0aOmCIkD1Yp7eOePYrUUsPD4swYiylgemmP1cYB3MNcZFg-_27aiAjMLMoJuHCqHuGhfOhOFigRWn_CjccrYWSGaPLPs_VUBmT6D1MgMK4Xdls8RGbN8u7r8cDxeSRmn_WCFsKY9V6_agCdDy_OhBTVMM3CDjPrJXpCBhu4dX4pzXsAhCQlIhnZ14n_UVjJ0JZ_uZ9lZ-aZ75lImypXmTUqz9EsjAuMsDu3tyWBXBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی محمود کریمی برای فرماندهان شهید و ماکان نصیری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/farsna/442578" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442577">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b67a9666a7.mp4?token=rkfjuTHtdo2tOUoemz_WyS7U5tVkMXJypfHXe3EDhM7aFN3T26wGR14qLP1Cu-ersY_ZNVTxF0T48lSxJhQBdHKO5yfx3k_OxXF7fW_cJTUiL_a8xJ4MrR9Cf7AKQPeBKqnBiLujKylxrbi8U9hd_7eF0XbJ_5x6ZtcjHsPjjeBXu2Dmys1gWwOitr6F3EAPd8Lr4gzYTffDt9ChMU1CIe6ZcFMEjtBQ_uuv9kCEgkNXo7lsbrZRDgdqdAFUWPLpcrp8B2plsKd1tkjO2jFz4S6TlFPixUGBy9TK5TI27HNRqY4z5EWg-ESFaZiuLmSPUAHvi3y2Fd65YKf5LfPetA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b67a9666a7.mp4?token=rkfjuTHtdo2tOUoemz_WyS7U5tVkMXJypfHXe3EDhM7aFN3T26wGR14qLP1Cu-ersY_ZNVTxF0T48lSxJhQBdHKO5yfx3k_OxXF7fW_cJTUiL_a8xJ4MrR9Cf7AKQPeBKqnBiLujKylxrbi8U9hd_7eF0XbJ_5x6ZtcjHsPjjeBXu2Dmys1gWwOitr6F3EAPd8Lr4gzYTffDt9ChMU1CIe6ZcFMEjtBQ_uuv9kCEgkNXo7lsbrZRDgdqdAFUWPLpcrp8B2plsKd1tkjO2jFz4S6TlFPixUGBy9TK5TI27HNRqY4z5EWg-ESFaZiuLmSPUAHvi3y2Fd65YKf5LfPetA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحنه‌ای از ۴ دفاع پیاپی ملی‌پوشان والیبال مقابل بلژیک
🔹
با وجود ضعف‌های زیادی که تیم ملی والیبال در هفتهٔ اول لیگ ملت‌ها داشت، اما ملی‌پوشان ایران مقابل بلژیک در صحنه‌ای دفاع جانانه‌ای را به‌نمایش گذاشتند و نشان دادند می‌توانند با تمرکز بالا، نقطه ضعف را به قوت تبدیل کنند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/farsna/442577" target="_blank">📅 16:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442575">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌
🔴
شیخ نعیم قاسم: از طرف حزب‌الله و مقاومت اسلامی، و به نمایندگی از مردم وفادار لبنان که مشتاق ابلاغ مراتب قدردانی خود به شما هستند، و همچنین ازطرف شهدا، در رأس آن‌ها سید شهیدان امت، سید حسن نصرالله و جانبازان و آزادگان، از شما در مقام ارشدِ مذاکره‌کنندگان…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/442575" target="_blank">📅 16:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442574">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما همیشه گفته‌ایم که ایران به حزب‌الله و مقاومت و مردم لبنان همه‌چیز داده و چیزی از آنها نگرفته است
🔹
ایران به ما امکانات، قدرت برای آزادسازی سرزمین‌مان، برای التیام زخم‌های جامعه‌مان و کمک به آن داده است و اکنون ایران خون می‌دهد، با حمله…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/442574" target="_blank">📅 16:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442573">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
نامهٔ شیخ نعیم قاسم به قالیباف: کلمات از بیان سپاس عمیق ما نسبت به مواضع قوی و حمایتگرانه از لبنان و مقاومت و الزام رژیم اسرائیل به توقف عملیات نظامی در تمام جبهه‌ها از جمله لبنان به‌عنوان بند اول و اساس توافق بین ایران و آمریکا ناتوان است.
🔹
شما تنها و…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/442573" target="_blank">📅 16:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442572">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
نامهٔ شیخ نعیم قاسم به قالیباف: کلمات از بیان سپاس عمیق ما نسبت به مواضع قوی و حمایتگرانه از لبنان و مقاومت و الزام رژیم اسرائیل به توقف عملیات نظامی در تمام جبهه‌ها از جمله لبنان به‌عنوان بند اول و اساس توافق بین ایران و آمریکا ناتوان است.
🔹
شما تنها و مؤثرترین شعله امید را در بازداشتن تجاوز اسرائیلی-آمریکایی از لبنان به حقیقتی تبدیل کردید که به جهان ثابت کرد ایران حامی حق، مقاومت و مستضعفان است، و اگر دیگران راه آن را دنبال می‌کردند، آمریکا و اسرائیل این‌گونه گستاخ نمی‌شدند و اشغال صهیونیستی بر زمین فلسطین و قدس باقی نمی‌ماند.
@Farsna</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/442572" target="_blank">📅 16:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442571">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0426334c5.mp4?token=lvd68_MC6ISsMXBo-q4-h3GGVR9z5tXGQhr0OTq0EJxpr2KWvdALgkQo-iA4MKrTa5kAMQ0mn4z3IBaRae3wQNAxtB30-M1KfbEuoCkmpwwp9hC4W3BToGz-p8lkBRLnm3EytGFAAxcbwGbzARGe3aUjq9mnyoV6GZXx2hF_pRreHczv8Z81if1ddrL7iqHNfH7SJjPSN2lrncAGHqoEUcqZvTW9fkc2PP7z5TUeopgaA5K-QkMnhydEtHaADYI5fjldDpwZax_0H-m1Nb0079XtkNBA99U8M-Oah5Mu2BT-GFdh0CQVTaFRKiJm0yJGPpjg9eqZhZcEh9J8ztVdPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0426334c5.mp4?token=lvd68_MC6ISsMXBo-q4-h3GGVR9z5tXGQhr0OTq0EJxpr2KWvdALgkQo-iA4MKrTa5kAMQ0mn4z3IBaRae3wQNAxtB30-M1KfbEuoCkmpwwp9hC4W3BToGz-p8lkBRLnm3EytGFAAxcbwGbzARGe3aUjq9mnyoV6GZXx2hF_pRreHczv8Z81if1ddrL7iqHNfH7SJjPSN2lrncAGHqoEUcqZvTW9fkc2PP7z5TUeopgaA5K-QkMnhydEtHaADYI5fjldDpwZax_0H-m1Nb0079XtkNBA99U8M-Oah5Mu2BT-GFdh0CQVTaFRKiJm0yJGPpjg9eqZhZcEh9J8ztVdPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قطعۀ دوم آزادراه شهید شوشتری بدون قطع درخت ساخته می‌شود
🔹
رئیس شورای شهر تهران: قطعۀ دوم آزادراه شهید شوشتری طی ۳ تا ۴ سال ساخته می‌شود. بخشی از پروژه به‌صورت تونل زیر جنگل و کوه اجرا می‌شود و به جنگل آسیبی نخواهد رسید.
🔹
یک کارشناس شهری هم دراین‌باره گفت:…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/farsna/442571" target="_blank">📅 16:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442570">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610aa9973e.mp4?token=Sk6kzK8iMQinL6t0Aonn36SQ4YFmgYBRhsB5egIkXqUrmTbKPn-1ngd6Whmvo9bbTnCtz6xscrW1JdKLX0MqYZeqo0ulgssbQWeVOUINykeLWVEZjDZvWCEubbAYXTEtImadHE5hnE6HGvG3_2AGwdASolGdfwV5EiLLCZatbM4ECa2FuPTqBooZwSOM9hCRfpJsiJROqenFO-iIZVyASf46P9EGs24ToM0sCAgXrXItwlqqo48ct_pCDHSE31ANK2lH1mA2zwJkqbSZbWxBc-fccqOGSA2evAuU7lhLO2A86sA_zzxYgFDJjTFI__QTk-D5zN_6UD32B3wM59RcSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610aa9973e.mp4?token=Sk6kzK8iMQinL6t0Aonn36SQ4YFmgYBRhsB5egIkXqUrmTbKPn-1ngd6Whmvo9bbTnCtz6xscrW1JdKLX0MqYZeqo0ulgssbQWeVOUINykeLWVEZjDZvWCEubbAYXTEtImadHE5hnE6HGvG3_2AGwdASolGdfwV5EiLLCZatbM4ECa2FuPTqBooZwSOM9hCRfpJsiJROqenFO-iIZVyASf46P9EGs24ToM0sCAgXrXItwlqqo48ct_pCDHSE31ANK2lH1mA2zwJkqbSZbWxBc-fccqOGSA2evAuU7lhLO2A86sA_zzxYgFDJjTFI__QTk-D5zN_6UD32B3wM59RcSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزئیات جدید از ثبت معاملات ملکی در سامانۀ کاتب
🔹
سازمان ثبت اسناد و املاک کشور: مالکان املاکی که دارای سند مالکیت حدنگار سبزرنگ هستند، می‌توانند به‌صورت خودکاربری یا از طریق مشاوران املاک، نسبت به ثبت معاملۀ خود در سامانۀ کاتب اقدام کنند.
🔹
این قراردادها دارای…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/442570" target="_blank">📅 16:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442569">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9767cf1552.mp4?token=kEbrHY0-P7F8M088dSuFJd4wh6KVzOsMbbTVj01-VyqmfIjYugd-wr2iSBuIFmT_dCpn0ghHO0UL_BGjXE3WgeK2tbj9mukkW-HMmmE4rD9E_R-8f3OydOGbdkOtJyQh911QJ9G0TdA2C3mSVDF4z1NKZBHiSkZRGJSN6SWWeaEOpKl7xKZtRGTe5oMklIrMjb3pY8r457DuLc4G9HMZCttZ7l36J6VI8sHQWHqgAMEDh7OW6bu3iTSzIsk6i4IzYYagyFaJFf3dgtZfnW7EZa2OetJyACWEE-qMWep9Or8IlgKQOgmnTEjBZp-dopMeP5TtQLfcrTjJ6FvjxqiQRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9767cf1552.mp4?token=kEbrHY0-P7F8M088dSuFJd4wh6KVzOsMbbTVj01-VyqmfIjYugd-wr2iSBuIFmT_dCpn0ghHO0UL_BGjXE3WgeK2tbj9mukkW-HMmmE4rD9E_R-8f3OydOGbdkOtJyQh911QJ9G0TdA2C3mSVDF4z1NKZBHiSkZRGJSN6SWWeaEOpKl7xKZtRGTe5oMklIrMjb3pY8r457DuLc4G9HMZCttZ7l36J6VI8sHQWHqgAMEDh7OW6bu3iTSzIsk6i4IzYYagyFaJFf3dgtZfnW7EZa2OetJyACWEE-qMWep9Or8IlgKQOgmnTEjBZp-dopMeP5TtQLfcrTjJ6FvjxqiQRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور شهید لاریجانی در منزل شهید محمود باقری، فرمانده مقتدر موشکی ایران
@Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/442569" target="_blank">📅 15:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442567">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-KoUGN-bc3JsVmkDCIm3apR7xa-pYhn37KzVIQmICx1xo8Qjb7Z_vB8zdBN0qWTcQiEjloRbt1J0dc2eXSABMMjBdd3q8BauszBmsKJJBnrTY8GEr3SFaFUcEnM17k8GV8cqPXUhpZzYTqMgxWhKeg7b7_tE4herNwmmML7za9LUtozZ-7mJ1V2zU0C1H_3NpWSORXNTG5WmlM5gdgyhG8bDUyw8mEejmZWGxEBJ_OYeQhnh7C8GSVqyMUk_fi6avVC9tnKCqv8X_kJAgzhBVgnjCLQaRgv53VreW680MWLITO0Yh07hu_e0lnOgarG9cTtZ3PhnqLuF2vLg3woMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd87c0908.mp4?token=unM8t6-VhCrg9-CLjDivZX1LUkUja5SYht3P2915KC-41lmrx6wNR-UhxWFG1If2yvWyBMYZ1nBackr8TDSxJMp-81P4zEBL3NHgyd1LjE7vRULno-OmjZW8ygT2SDJYy8etMNRMOTkQlh6F7cretj7T8K-KfY0rb2ZWA3t8rtYCkRF8CvlRntxTdgdXYBSquTQRsPkMGgNqxs7RDjlS1op68LSMOcjdkpj_oyOtko9kUDvQDdqlVsISHmyUKMdSHO7bIDm7Ob_w380_9itIvvR9qF5gb7fAKkfLULBgSWQil3-wkeCxzAcbiYTwcSjAh3mLAKa8J1OFpmPWdF9pcpDRa8aDDXbbovd0N4YHwRj_UqTITiHS1mCl_h2T-iGXlGsPxrWs1sg3mVZ9tgfg5ZYSrdCkRBH8YeTOwmgrzo0tMzlkheCil0rIhyQJqYs7SMQtirNQSvV-0iinn1KeCcZU6twNixPxMK4WKVVc9vLHFhsfQfx8RkzpL36F0AkNZsbQty0X3odU1xb3UsHp4fviTjXpzklSjgqFuQWHBE-Vgzpxoqd-O8svWopQOiOshEMzOu8OY15Q4946WopMWQIn7KaasBjGZy1WSrFNzD_Sansj1Kfcv1CsIGz3JXPJrLC_zEozDfXvpq7J6w7THA-F00aqMth30lSr0zizmaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd87c0908.mp4?token=unM8t6-VhCrg9-CLjDivZX1LUkUja5SYht3P2915KC-41lmrx6wNR-UhxWFG1If2yvWyBMYZ1nBackr8TDSxJMp-81P4zEBL3NHgyd1LjE7vRULno-OmjZW8ygT2SDJYy8etMNRMOTkQlh6F7cretj7T8K-KfY0rb2ZWA3t8rtYCkRF8CvlRntxTdgdXYBSquTQRsPkMGgNqxs7RDjlS1op68LSMOcjdkpj_oyOtko9kUDvQDdqlVsISHmyUKMdSHO7bIDm7Ob_w380_9itIvvR9qF5gb7fAKkfLULBgSWQil3-wkeCxzAcbiYTwcSjAh3mLAKa8J1OFpmPWdF9pcpDRa8aDDXbbovd0N4YHwRj_UqTITiHS1mCl_h2T-iGXlGsPxrWs1sg3mVZ9tgfg5ZYSrdCkRBH8YeTOwmgrzo0tMzlkheCil0rIhyQJqYs7SMQtirNQSvV-0iinn1KeCcZU6twNixPxMK4WKVVc9vLHFhsfQfx8RkzpL36F0AkNZsbQty0X3odU1xb3UsHp4fviTjXpzklSjgqFuQWHBE-Vgzpxoqd-O8svWopQOiOshEMzOu8OY15Q4946WopMWQIn7KaasBjGZy1WSrFNzD_Sansj1Kfcv1CsIGz3JXPJrLC_zEozDfXvpq7J6w7THA-F00aqMth30lSr0zizmaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
میناب ۱۶۸ روی سکوهای ورزشگاه  @Farsna</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/442567" target="_blank">📅 15:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442566">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjKataFc-1PwceMDnQS6qB4bQMNV4Twy7fUv0dcaIkVhQoZrY5qFlPyglOboLhBAXXZEQbZLsesNCri04QAhTr1G7ssPMDQ0YUXuUqcLyuR0aa8NAgzxnX2EhuGzRHzjXkKKalQOXL08NUerWaqnG8EPf8WwJ-X4Pya9K1c8hkIx86eNwHhM2HPbUwZJuni2cNVv_va3RRQ63s0Hv913HfHQpd4G312O6YxzGeOucd1tjjLw8oGVCeqfBL16iXgZrZjtHB1yILS3EmtDTCXV1W8OQQuGIgiTJ-IY0LRmKvPOYwnCJWby2N8xSsBgYPMazjS7j2kfoAU0KmvZ6LCfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال وقوع سیلاب‌ در ۸ استان کشور
🔹
سازمان مدیریت بحران کشور: از امروز به‌دلیل فعالیت سامانهٔ بارشی شدید، احتمال وقوع سیلاب ناگهانی، طغیان رودخانه‌ها، آب‌گرفتگی و رعدوبرق در استان‌های آذربایجان‌غربی، آذربایجان‌شرقی، خراسان‌رضوی، اردبیل، گیلان، مازندران، خراسان‌شمالی و گلستان وجود دارد.
🔹
همچنین در مناطق جنوبی کشور، به‌ویژه سواحل هرمزگان و بوشهر، خلیج فارس و تنگهٔ هرمز، وزش باد شدید و تلاطم دریا تا ظهر فردا پیش‌بینی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/442566" target="_blank">📅 15:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442565">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lR4ZrygWsHcTCrG9IlJx5_Qm-W7w3TWfy06CokkkvOWYGgN1S16Jx_h6upp2TCaKU6RywrnIM6FeqPScKCiG8drB6om6gQCyar3WnCJfGkifv7arLt0dT3Fr-jojjqG9rjg8wFQf5xjRRh-U-I1vZN_Q9OKLqr8BaGJ0jy5DPNOw-rCS8RhVklKGu3lweiQJj6BdyYa9XN9uc8c9FBaPlh-Vi7k1a1USCIyWiVVuuOHBFgOeGXAF3Toyiq55In5dI_YqJNxvMIxvC58Cf5d7OqFpk52U-Ig5t09AmL_feF4mSJgtKMHWu2RYzSJXB-60HGeOoyQxG7ayohhI0k5frQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزش باد شدید در تهران ادامه دارد
🔹
براساس داده‌های هواشناسی تهران، در ۵ روز آینده آسمان پایتخت صاف تا کمی ابری در بعضی ساعت‌ها همراه با افزایش ابر و افزایش وزش باد پیش‌بینی می‌شود.
🔹
همچنین از امروز تا پنجشنبه در دامنه‌ها و ارتفاعات در ساعات بعدازظهر رشد ابر گاهی بارش پراکنده با احتمال رگبار و رعدوبرق مورد انتظار است.
عکس: حمید عابدی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/442565" target="_blank">📅 15:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442564">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSnCKaeW2TqM_1lCsfaJrFAtLZUFM2J-0x6EzqHYFQWsryIeqK62_N1bOUUUjm9XNHS5QS5E9etEgerSePuMN-nFw7linf2su2oj-OlnTpk3A4-9SYDIUZNaDHZXSmd3SqgyY0nb7m_4fBqplsjw5MIkgUyKCwWc8ZVyOPO9HDidS8H-mDkbIbLnxwQLpb20Uhp5OMMovybyTN4c3XbgIY0vqaFe5B3xtTFlt0CJvhMWujYIaInloVkhpII_3u14pQ3UqSmRBL5cFZUBh5pOGcgpzdipSscoBLtCUT1ph1HgiVBw_VZSUajwgcNtdUcpP4fW-W3R0fWvvpwKosaq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ایران در رتبۀ چهارم
🏟
پرتماشاگرترین بازی‌های جام جهانی تا اینجا
@Sportfars</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/442564" target="_blank">📅 15:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442563">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎥
یادش بخیر آن رهبر جاویدان در بزم ماتم
🔹
مداحی محمود کریمی در شب اول محرم به یاد رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/442563" target="_blank">📅 14:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442562">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM7r1Z5Zp5VCODbGPZXcehGVK-6OVx9Wn-CKH4u1i8m4EL0Ds5sdM2y12yygaGs5jeI8t3rVTgrdQhseLEMb8IUpE4ustSaQNRoM7SaJ04m8siTuX1T4a0Yg9VM-K6R8zCB59zuzZPF_LYQ_tDVt3W9-LpRgWvSiW39PAKRFZEfIFwBcXrVKVhI3HG3GJyh_ZQ60AZ2VOsm1xCl3KxQZKsS31Gf73roiU4C_Ue_ksWQL6O9dokojI8lkoXuvQEIbQH-GjDsPl02biXnbIKuBdc7KjiiIqn2GjCs3QmH3z-6Aba8s6L0jIAOTyG1A8KwxTEtBVPZGaKI_4UUdlCMXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سرباز طبیعت به‌جای ۱۲ نیرو کار می‌کند
🔹
فرماندهٔ یگان حفاظت محیط زیست: یگان حفاظت محیط زیست به حدود ۷ هزار محیط‌بان نیاز دارد، اما در حال حاضر کمتر از ۶۰ درصد این ظرفیت تأمین شده است.
🔹
بیش از ۲۰ میلیون هکتار مناطق تحت حفاظت در کشور داریم و بر اساس استاندارد جهانی، برای هر هزار هکتار باید یک محیط‌بان حضور داشته باشد اما اکنون برای هر ۱۲ هزار هکتار یک محیط‌بان داریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/442562" target="_blank">📅 14:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442561">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14d10416a.mp4?token=AmSiNNB8jmc8HDNJM-HdLuKie_bErLWcQ9P3M0FBHltPaoiJnUyEzYtiPCwOuQDteDZTvOb94M2QvlVMSwyLMJO-Frqp7S6_w9NTL-X3A7PRsySjxY1vtzzK2YncK7oNANQ50dGbXAm2dZ6hcFGiwSMvLD-el7egOt0Ca4fblSvkRnCC0wj9JbKTuBKQmlWVtejaaNZTxRkAk3Z-HoUaZHbzgI5OgXwgoozD9zSjR795pCqtYknPWs32H1oNAeGi5FlEQx59KJv7_axXEsz4qB2IgKwZhr5s9CYIRKD4Gz7V7jzhA3ruFWa-zJ5g85Bx12Earqjn-TOquTPsU2tPmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14d10416a.mp4?token=AmSiNNB8jmc8HDNJM-HdLuKie_bErLWcQ9P3M0FBHltPaoiJnUyEzYtiPCwOuQDteDZTvOb94M2QvlVMSwyLMJO-Frqp7S6_w9NTL-X3A7PRsySjxY1vtzzK2YncK7oNANQ50dGbXAm2dZ6hcFGiwSMvLD-el7egOt0Ca4fblSvkRnCC0wj9JbKTuBKQmlWVtejaaNZTxRkAk3Z-HoUaZHbzgI5OgXwgoozD9zSjR795pCqtYknPWs32H1oNAeGi5FlEQx59KJv7_axXEsz4qB2IgKwZhr5s9CYIRKD4Gz7V7jzhA3ruFWa-zJ5g85Bx12Earqjn-TOquTPsU2tPmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان محاصرۀ دریایی آمریکا، با عبور کشتی‌های ایرانی
🔹
دقایقی پیش چند کشتی ایرانی نسبت به تردد بدون مشکل از خط محاصره اقدام کردند.
🔹
طبق اطلاعات ناوبری کشتی، یک نفتکش ایرانی VLCC از آب‌های آزاد به‌سمت بنادر ایران در حرکت است و از منطقۀ محاصره گذشته، همچنین…</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/442561" target="_blank">📅 14:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442560">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39152c14ac.mp4?token=idZGmkFDytUOFvLRkh8_9IEAGOipAGovreR2SLq_2gNzZgwlNQ4H31sIt1LM_CZh9Mw5l6mU0ZO58nTkw7iZBKi3qwfMrm7fBg2ylG5jhvI66FT5a5SYE87UzdrOo61A53S9AosydfzU3Gf-cwdWv1woZS1qMSw_xrOhdRg77s4u0PQDqzJ-UONqWaWD-vgxNmll1wtEjtAGaDKtu9hnfGCTiWU3eyJ3BXEUCg-On055BDqUYgoGryj95yDW0qhhFpNNI_UkZ7lg4jHYd9CIa4BwJ1t18SfNegxqEsd7L0LjU7JK-Vi28jGWNA03yAnAtGrib244qsIDnDGOj4AjBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39152c14ac.mp4?token=idZGmkFDytUOFvLRkh8_9IEAGOipAGovreR2SLq_2gNzZgwlNQ4H31sIt1LM_CZh9Mw5l6mU0ZO58nTkw7iZBKi3qwfMrm7fBg2ylG5jhvI66FT5a5SYE87UzdrOo61A53S9AosydfzU3Gf-cwdWv1woZS1qMSw_xrOhdRg77s4u0PQDqzJ-UONqWaWD-vgxNmll1wtEjtAGaDKtu9hnfGCTiWU3eyJ3BXEUCg-On055BDqUYgoGryj95yDW0qhhFpNNI_UkZ7lg4jHYd9CIa4BwJ1t18SfNegxqEsd7L0LjU7JK-Vi28jGWNA03yAnAtGrib244qsIDnDGOj4AjBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اژه‌ای: ما برای گرفتن حق‌مان مذاکره می‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/442560" target="_blank">📅 14:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442558">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HETSNvde76GD0iE0GufyPIezTogA2_Fvw1wIEYvjN7jRuF4QsSHFZ6gJWS4mIU0YzfqAZCm6kVCtbPGohln-pdw_-V5IWLM6KJBJx9uoi4XZEbqUBmKQ3IeqvkPuE2Cbnp6wjGeX5gMinqW-KkJh5fmhYvcUW1uQK7NOPXKpj0tOrgq-0AKMm7ls_ndcWtRaGNm_P72JAjKaK1T3NGXSlLJxCsCucNsgTyIW54xuD1qvVi9i5g_FK6dLPZ4korKkdwO7KrVNUcWRuiucFn-BRKPZd54Qu0DKxaR0ULzYR3T44qvRjITf1-8EcL08mDL-0lPRFzjaaQJL9IZ9yvxZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YhHPKW46XhwSfxPzpULV-vLk_80c8crMMSdu3RQoN4cjsErTA5maXDakgLGIubqcgHznXuORmeVEewH7dG9skFhavJmN69-bkEbn2AnV6keKB-rqpVregLlUUzVCK_6UJGz_cp0ZW7eZEJf2rUZU_zBxx81ffqEAA5DnHsaCNDAbs2_yZisYRiR2IFmdPaGeYhRpJnSVXGg417z3yzZ_pNB2SA8VrxDIVimbHupzGztrWqDUPe-LrITVAesFJckZQWjMyz2ny9xlD9MGXK2NI5WKVKv2taGQloZN-Wg18rAHgKagrrLEoKWD5jXtJgnpBcZh1PGemWuoK-1Be8sKlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تفنگ محبی مجوز دارد
🔹
شادی گل محمد محبی در بازی با نیوزیلند باعث شده تا رسانه‌های ضدانقلاب و برخی از کاربران ایکس با حاشیه‌سازی این شادی گل را خشونت‌آمیز تعبیر کنند و موضوع محرومیت این ستاره تیم ملی ایران پیش بکشند.
🔹
نکته جالب این بود که محبی به چندین شکل شادی گل کرد و تنها در بخش کوچکی به شکل شلیک تفنگ آن هم به صورت ضمنی شادی کرد.
🔹
اما با نگاه به شادی گل‌های ستاره‌های بزرگ دنیای فوتبال این نوع شادی در مستطیل سبز عادی بوده چون بهترین فوتبالیست‌های جهان به این شکل شادی کردند و محرومیتی برایشان درنظر گرفته نشده است.
🔗
شادی گل‌های مشابه بازیکنان بزرگ را در
فارس
ببینید
@Sportfars</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/442558" target="_blank">📅 14:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442557">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b69d86769.mp4?token=HjjxZC6a6BhJOX7XCVzB4gUG0FEuI4wGCzuRnf1SvCbgByr71bgoK2pztTNlSvVpnLBwQWKR_Pp0-kZ7ti--dcsojeZSRWdrGLy0deSh_sIElj0RC5hjxO-pV7-UBxp3aVuIZfB3mTqwL11wDLggRA04of6UpvSnZLEE0uMTXx8SstOFBuCxo2dDcGqFQilDeoyq7cP8iDQ9_gxMcIq6IxvrLmESqAyWrfGoSG3JgLSSTJ7sjAYs3I_Y9pgSrN5lFbKJJ1YwHT5EAUsMH3gsZhQi5UiXnGbMZxJ78ng1h3xGj8klTM6hgKxieHq3o4IYCE4EIaV4odzA8xlQTnrT3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b69d86769.mp4?token=HjjxZC6a6BhJOX7XCVzB4gUG0FEuI4wGCzuRnf1SvCbgByr71bgoK2pztTNlSvVpnLBwQWKR_Pp0-kZ7ti--dcsojeZSRWdrGLy0deSh_sIElj0RC5hjxO-pV7-UBxp3aVuIZfB3mTqwL11wDLggRA04of6UpvSnZLEE0uMTXx8SstOFBuCxo2dDcGqFQilDeoyq7cP8iDQ9_gxMcIq6IxvrLmESqAyWrfGoSG3JgLSSTJ7sjAYs3I_Y9pgSrN5lFbKJJ1YwHT5EAUsMH3gsZhQi5UiXnGbMZxJ78ng1h3xGj8klTM6hgKxieHq3o4IYCE4EIaV4odzA8xlQTnrT3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در مقابل بدعهدی دشمن می‌ایستیم.  @Farsna</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/442557" target="_blank">📅 14:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442556">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkYQwSL2CrZDFEJpFSZNhztjQBa-9GysOxp7Vl79Un1BvFNZcGNxYf6ZhgqcFcMGaXsptJUN3MoE_ugd9OpFjsWYVw5qdNWpCVhr0yXPonABU3S3AF3xlNIffBPbqiUZmQhZy2u-a9IwwNmpD7NPXJ68sJhlGmkJBxkKt6nX_pKH7GJ1ukD1HNfPHBsGgua_9EI_R0CsZpKGgLo2J5WsXKzv2v-Opd4dCAHISeMIH347aF0euHF1nt3gYbxqHGYg_Jy3KMYp-msEddgQ1Z-6mdnbu--H3tIu2FkBfEJ33gXiHY9XWZHHmrhVWguMGHJx_nBx99tKeSZ1FWBI0T83oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عراقچی: جمعه پس‌از امضای تفاهم، مذاکرات آغاز خواهد شد
🔹
در مرحلهٔ اول مذاکرات دربارهٔ خاتمهٔ جنگ، محاصرهٔ دریایی، تنگهٔ هرمز و آزادسازی وجوه مسدودشدهٔ ایران تفاهم شد و در توافق نهایی دربارهٔ موضوع هسته‌ای و لغو تحریم‌ها تصمیم‌گیری خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/442556" target="_blank">📅 14:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442555">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb7cce6c6e.mp4?token=Z10wGLrxp13LyOfF2I5CPbNu5s3Be4w0RWpomuvanaYEPgp8EVaawcA8UVwU5wtDbVtKZ8-nxp9Ugx3-4hmKbYeTT8J0qVMmtibeokyqi7cSWdU_1XGCEdU8gfNbN8O3hrvVv7AQ7qV1QPqK9MvYg7tOqB39xsfrtDlirw1Ww9uGgkWB72N_zV9Qwv_EkHGKiUPgG92_IEY87liMAnurJs82PdotyYnnMsnNZW2J6CCetuIJU6nWmfY447T3p74G0OOpPdB_qAi5i-boj_k2FXYpHU3D_Uj1xFsPQ2V6mGaQP5k-9mOjjOUo0pKX9RKBKgdy8HJJXpUsB5rzJ9Wezg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb7cce6c6e.mp4?token=Z10wGLrxp13LyOfF2I5CPbNu5s3Be4w0RWpomuvanaYEPgp8EVaawcA8UVwU5wtDbVtKZ8-nxp9Ugx3-4hmKbYeTT8J0qVMmtibeokyqi7cSWdU_1XGCEdU8gfNbN8O3hrvVv7AQ7qV1QPqK9MvYg7tOqB39xsfrtDlirw1Ww9uGgkWB72N_zV9Qwv_EkHGKiUPgG92_IEY87liMAnurJs82PdotyYnnMsnNZW2J6CCetuIJU6nWmfY447T3p74G0OOpPdB_qAi5i-boj_k2FXYpHU3D_Uj1xFsPQ2V6mGaQP5k-9mOjjOUo0pKX9RKBKgdy8HJJXpUsB5rzJ9Wezg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اگر من نبودم الان اصلاً اسرائیل وجود نداشت
🔹
الان اسرائیل ۱۰۰ درصد از روی زمین محو شده بود و هر آدم باهوشی در اسرائیل این را خوب می‌داند. @Farsna</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/442555" target="_blank">📅 14:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442554">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9149ef45.mp4?token=DunOnneTphUS5UoA7Id5_U3iozxkfzbDJ-ZC-RQx0XRpBYi0tb-qyGEm_jgmUHWadLQ3cY3pMEcbyRorSzPO9GI4j2nuhu0A4UQxXMbV8iw9Ni5rCAc_xRPijyrzGYfAiyiea1bqxHtbmvsXuM7dV5NKg4mX89iNDR5Zw_1c65BEIzhPFsiKNQ6i0wCalDRjuzmri9rUigsCZ2rfEDkyr1OOZj0MiEoeRT--IpFzgjtfMuVqgBl1REv0Tw4ooBbz7ssT4WGg_HjG8U7yJ_71R-IYmJhHSIBFA2mLG5_51PhGq-ST2DHSbZAOqhc_X3dTx1WF4S3_2Ce6OiVdF_m7hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9149ef45.mp4?token=DunOnneTphUS5UoA7Id5_U3iozxkfzbDJ-ZC-RQx0XRpBYi0tb-qyGEm_jgmUHWadLQ3cY3pMEcbyRorSzPO9GI4j2nuhu0A4UQxXMbV8iw9Ni5rCAc_xRPijyrzGYfAiyiea1bqxHtbmvsXuM7dV5NKg4mX89iNDR5Zw_1c65BEIzhPFsiKNQ6i0wCalDRjuzmri9rUigsCZ2rfEDkyr1OOZj0MiEoeRT--IpFzgjtfMuVqgBl1REv0Tw4ooBbz7ssT4WGg_HjG8U7yJ_71R-IYmJhHSIBFA2mLG5_51PhGq-ST2DHSbZAOqhc_X3dTx1WF4S3_2Ce6OiVdF_m7hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در مقابل بدعهدی دشمن می‌ایستیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/442554" target="_blank">📅 14:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442553">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6800f9e7b.mp4?token=CltjZ5dlB8-CSl1QJ9iZFvGoWtPn6tQkvIqjWYilKNS5tqkIZjlrXwOJM-8yKtvUxpng6Ql3i_t-vX60YwKFpP-isWmGsU1Z7iSN8EDJKQA9dEZ4e5FT1yimMxCH084daS2rqSqyJ7eFVQwUvSU0RdVxPrEf4oYTIa78Swxw6giwIwizTG5PcI40W2ybixFOCLC9opDWljM1oqUCtrKFkk0_PBoeDvV6CEQaryfRqBVAY9SMs1J-d03Bi7aR1RfCFtpqXTeN8mBu5hsk3U-w4BNEfEAZVv9-YRDwSgHHSX-dC1YHG1clRXAJaqpwkoP3o-Cjgt7xBUJflc9f0vTjXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6800f9e7b.mp4?token=CltjZ5dlB8-CSl1QJ9iZFvGoWtPn6tQkvIqjWYilKNS5tqkIZjlrXwOJM-8yKtvUxpng6Ql3i_t-vX60YwKFpP-isWmGsU1Z7iSN8EDJKQA9dEZ4e5FT1yimMxCH084daS2rqSqyJ7eFVQwUvSU0RdVxPrEf4oYTIa78Swxw6giwIwizTG5PcI40W2ybixFOCLC9opDWljM1oqUCtrKFkk0_PBoeDvV6CEQaryfRqBVAY9SMs1J-d03Bi7aR1RfCFtpqXTeN8mBu5hsk3U-w4BNEfEAZVv9-YRDwSgHHSX-dC1YHG1clRXAJaqpwkoP3o-Cjgt7xBUJflc9f0vTjXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: جنگ اوکراین هیچ تأثیری روی ما ندارد، جز اینکه ما سلاح می‌فروشیم؛ ما هزاران مایل آن‌طرف‌تر هستیم
🔹
اتحادیهٔ اروپا هزینه تسلیحات را تمام و کمال به ما پرداخت می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/442553" target="_blank">📅 14:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442551">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afed014df.mp4?token=VHI4xvai5-mn3ehOtoR1BIX8HLDGIexCmtbcTqofxVrzMmjQxwFq-rgFmept7g8AzM_ZUTSMaFVBN5VSJXgRzDXnDobZcq6iSEcWzihqO8atFD1WDrzsoRWobcY0Q9oizRQ5jq3T2PQiw6_tHknWHQahec3Ee_HY1qz-WzcjwPk0Y2lLwqO_stIfxhFCC_Dq_yLmIjhpo-58aALodVrds2hS99uCphyQkv5sykwGytLpesoxHvgc9yXGot8r09mwWnCEk9mfIFf-dgO0r-IDcRET0uvC4PcUaPe29Va8xPui_T4hr0jOe9VeGCNLqIEmW5WnaGGEUhLttiUBeT21Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afed014df.mp4?token=VHI4xvai5-mn3ehOtoR1BIX8HLDGIexCmtbcTqofxVrzMmjQxwFq-rgFmept7g8AzM_ZUTSMaFVBN5VSJXgRzDXnDobZcq6iSEcWzihqO8atFD1WDrzsoRWobcY0Q9oizRQ5jq3T2PQiw6_tHknWHQahec3Ee_HY1qz-WzcjwPk0Y2lLwqO_stIfxhFCC_Dq_yLmIjhpo-58aALodVrds2hS99uCphyQkv5sykwGytLpesoxHvgc9yXGot8r09mwWnCEk9mfIFf-dgO0r-IDcRET0uvC4PcUaPe29Va8xPui_T4hr0jOe9VeGCNLqIEmW5WnaGGEUhLttiUBeT21Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: به اسرائیل گفتم «بگذارید سوریه حزب‌الله را کنترل کند».
🔹
من فکر می‌کنم آن‌ها بهتر این کار را انجام می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/442551" target="_blank">📅 14:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442550">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54dbe2cab4.mp4?token=lzIGmUKxItPq8TouqsAlnj6X-6UMXYyDKcuz3-nUHb3Od27lZz7G6OUP0NBw-6eKD1FZ2_5BAMRpZHaGr32clyeuhhij9ByOveG0aGAyEYtwTiH_uJDQaK0scoMFJcZeKqaT48hUC3udq2qp-AilynfALoYy6qH8Ch5FSndsizSp5YxdnViIVnGzWLd08AbwTQhGWsYVJZFJmILN5w5ZDQzHh0CK-f4xXS4nsTtgXO9n1iZr_Rri0vyrX2DD5_M-9RUAol3Eyy-v9L83sNx0sOTVrwW-kY8vodsN698lrym0lupnc0dxKQvqbaQ1-nshnbM2FmCWNdEh5DHgtAI3Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54dbe2cab4.mp4?token=lzIGmUKxItPq8TouqsAlnj6X-6UMXYyDKcuz3-nUHb3Od27lZz7G6OUP0NBw-6eKD1FZ2_5BAMRpZHaGr32clyeuhhij9ByOveG0aGAyEYtwTiH_uJDQaK0scoMFJcZeKqaT48hUC3udq2qp-AilynfALoYy6qH8Ch5FSndsizSp5YxdnViIVnGzWLd08AbwTQhGWsYVJZFJmILN5w5ZDQzHh0CK-f4xXS4nsTtgXO9n1iZr_Rri0vyrX2DD5_M-9RUAol3Eyy-v9L83sNx0sOTVrwW-kY8vodsN698lrym0lupnc0dxKQvqbaQ1-nshnbM2FmCWNdEh5DHgtAI3Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خانوادهٔ شهدای میناب مهمان حرم امیرالمومنین(ع) شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/442550" target="_blank">📅 13:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442549">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b48cc3d0.mp4?token=anS-AkSw9V8OOxLyHGpdBZUccMSHsq2VWASw0g-1oIPFWw9GyUKQqdNTOH4uIRdbr4Xaft6jJ2jkrvFF9NcaU5HyMV0hHkTeWtJElA30vZRP_-GTzsRH8VV_VZOxVEsDnJ29nmphfsz8Szu3-PiH6dnK0tzcsUvyNOCETXJPsh0Qi29unhrnH81_ajwxWlNGn5awuqUO_8apTsJxn7MXhNldFCKTEBMQAJPC2kpltDAkRBBGzod5rFCO_qTrdoTQ4uqJRRCriiaccbGkYUXYjhEtzBdV9hq7ts-Bwe6nidtEX1OYLm03G18gKhJs8oS0l2pODCcBn3cv2qrdeE_oNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b48cc3d0.mp4?token=anS-AkSw9V8OOxLyHGpdBZUccMSHsq2VWASw0g-1oIPFWw9GyUKQqdNTOH4uIRdbr4Xaft6jJ2jkrvFF9NcaU5HyMV0hHkTeWtJElA30vZRP_-GTzsRH8VV_VZOxVEsDnJ29nmphfsz8Szu3-PiH6dnK0tzcsUvyNOCETXJPsh0Qi29unhrnH81_ajwxWlNGn5awuqUO_8apTsJxn7MXhNldFCKTEBMQAJPC2kpltDAkRBBGzod5rFCO_qTrdoTQ4uqJRRCriiaccbGkYUXYjhEtzBdV9hq7ts-Bwe6nidtEX1OYLm03G18gKhJs8oS0l2pODCcBn3cv2qrdeE_oNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاخبار: الجولانی ‌دنبال آتش‌افروزی علیه حزب‌الله است
🔹
روزنامۀ لبنانی الاخبار در گزارشی هشدار داد دولت الجولانی با سوءاستفاده از تحولات منطقه‌ای، به‌دنبال فراهم‌کردن زمینه یک درگیری جدید علیه لبنان و انتقام‌گیری از حزب‌الله است.
🔹
طبق اطلاعات مقامات لبنانی،…</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/442549" target="_blank">📅 13:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442542">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_jQdtQZ7HrkrzfvFg-e7fqefpQ41165uv0AA4CtOVYyifWWaNXYaoY-FNA90gPnrWeY3EXp9xO4nFdp55TE3M72nTyNNMvzNVcUHOKyuGzvmVrCvADHmXLFdSRRf-uGcnHuT9_en7LMbGPGs7ssA3DFm-gYn7go6IdYfQjaCtrri6WMto1Mq0D2ZRXBwY2_fba41Sax7SnZ6Js33V_97TyTOW17t4asi-EmnvBIw8t1bjPtS2OMQkNVoE6FYUTEnkmsqONZqTwkrhS9OgIenEcZQOmTs4QHROfQuxescXLKnqWGQJTah0xO_pZ4yidHuHSKDu4m6KhymZqr1zLaqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXVtJz6RzK5TuzbtxARoRVCYG9sGizYizcQ2h-caLAOCh0lm48liz2Az3_nplbBdqhs_IJHE5uQQoNfpAl8qSHsb2KOXvG9cPFidz5wd-Ap6_Md7kd0Yxm46oZie4tmJUGV5dm28F-NPxBS0tg_zl-QF1l5ZbGIAvjR_t8-KpJPpYG50v0Q8HHmAg30uLZJTUHqjzbR-LlqIctWzEvFjvPua3Ht7pR36di9EdXrP-JXD9Nl-uSk6GiByyfr5Nn0NuOIxQefWasPsc2QQOq45CFUwLsq0nH11LDLPRXKjYvfmS1DBmik89VZSQio14mS7aZPwTUVZjtEq6K-cyfcyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wx5y05jLEdXd97z1-AJTLNIMXxfTk6RCfO4xKq6EuXdThxa1xb-s0S-rGio_RS2utSCfCpdsFKlXigvEWH36rWjxucS27EZ_u16eY-gnrYJPYbZKml3gvsunzHra1gjHBtSfmL-7OrE1nB8jN4yPWukipQR8_Iy3Q8CQUpQGt-bOX0IRaMiUwnN-6wO6cl92CwNPKNjayqQxpu74m-VnQdHELZJKFI7VId8q8AJ3WMOFZOvwRbLIUNhOh9HCt3b-feaIvsxo-Gwq6kkwizxsFbldkBgWUPP4K6Or4w_4UnxjyNB4ERu9B59AZ973s-8cLb74heXqI2Hmr5mXCVOAGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ovu3djmAV06YOmcU4dGKu7N5A3c-iPAz_QT42GFutDxNNGOrNFy2eSZoySWUMOIDmlngVBYdanw1Rblv8v-g7aM5BNANN6cOOe5o-WMom1Wa4Hh6wRneu9Fye7SDBvX381czsC2TiJSDTkzLPDh3Bhuu2Jy7Vy9ZhcfzmeFz8I5d5cResay3fUshDKNIl8bZbYgtCgxSO3K8uYKBoscl4K7S2M1mlzBiYpXoOJdmfMz4psnLZxZI_w-8Vdb73-PN23YyQ3juVYbxaONvHN1UZLoxtWP8DcsN94m3cOKzQjpztBT2SB8RBP1oJgixPYdpc-uxZgXaodU4RiwtAHRDMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfLNiTNzVfdxFfCpLuYx_bWd_D2E4b_GMaexsGuZJBQssoFWl6BZJkfaJ-KwOdEvTMcuUbn9-8AwL3wBJFS1XAjT-Z98sWQhRmBD5nwkX83OiYr8sVBDkch_KwQpGiDPKXzARLx48aKk6f-94q73nHPHLrGrwpL6VYAJzdd8yzdOdy9DSEu5pTG_wu8zs_OhpZVZx0Vvn5GDMtkm2VkN5YmBnLFJcaTl6A0Ppakc6K9VC-BwD5kEK2FYrogOdiljRdKbmRLqAlk7P3KavLFmw7a-ChiMs9ovufSGbXRy9dK-TchDLyldltsZkeBGUnthlkebsoDVV8jxLRT_OR0INA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OrM3GkfOb43C3DQkGkj_3L5qQV0yo_OAvAXf7SKqDtk5edxZ-OC57tMIOLlzeEm8CQvinX7qyw4tnU5oggio-B6fgHMtIY4tg-_-dt12FD6Da3B5_s85GIcigC1Txr2EHYMbcc7nIFqf7Y5e5CooAH7r9BqQAk9AK6g_yHT07xVu9L_3EjvosrjxTgcq5D_BbFZ8m6fBdkQR3Gi2qEGvvYAerepP0-qbndUiMHHTAtfMLp7PLcl_eJwRV2TwEoTQX1v0syUQ_IiIs0j-3_mPJbK5n2A0qPzNyizunHryJAc_t1toZRVEgibNFrevO51baEI5yn0MEspc3OlTknTf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bvHBb70qNVUkYMbm6iMJj98FAONiGrxiiHNWHCSeze6AibU_J4WHl8o0jf5iCdVzSt5SKSJVb9gyqwDxcaxsKztamA-HalFdmy1xsw2j_tp4Q_x45g-HA4wcZ7a7uXYuHy6pM6ExqZ_u0C0shBHC3nJTlBXSRktv4pa5JsdA93eITm8MKChvs0-lA010yaA-Rjz4741__CTaiex6Benyr2RmdGrgErpctPQ14cqwUep-JXzjIdRT2o5V0GsEQENalh48Atwpn6aRtfRoIbzOr2ZJ7m77SBfpgQiDNvzxGDkat-mDOzqSshmQ9S9WashV5tXufOdZggehMbanq_tBGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
عراقچی: از صبح دیروز جنگ رسماً در تمام جبهه‌ها تمام شده و هر حملهٔ اسرائیل به لبنان نقض تفاهم است
🔹
یک طرف این تفاهم‌نامه ایران و حزب‌الله هستند و طرف دیگر آن آمریکا و رژیم صهیونیستی؛ خاتمهٔ جنگ مشمول خاتمهٔ اشغال است و بدون عقب‌نشینی نیروهای اسرائیلی از…</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/442542" target="_blank">📅 13:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442541">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b96935ff.mp4?token=IAliFKAwcjA2-her-UGjyPt9iKN8ZU69aQxvInfkJePArkHisgm3kl2T2me0u_Jmxml8ifL7tLg78lZqR2s3GJ-Sf559la-S4GMHifZZLnfCi8SXUoEKNLi8-w_AjgkdU1YUa3jbLGLli7zsPft9gAgyUxVeKE43EPQ7Y-getdKxM78aHAq-63lIkzxLhZlQMlAE0hqORgsybYHxYz-RxdPoS8iN3qGaVLqT6k-u5JvF1EBXgU-p-wjlvmwMGJcflewzKxBIttV-53XxJ5f16w9OGME56rkmaUjCSHFHiYNLObLVN4WGRRmjAEcz4t7EOp81LM_38eTQ4SMm89ad5B8nLM2WDhMdoSko9ffDUwGjbVYPPmjw2yMcSb4gxOCDHtQPl8d1qWmGi0jfNE8UOowyVh1w17_hhSd68EmIppYdeEUOZuq2IXC2xchv0tPPLdzRVsJRu_DBlJTl0fvxQamGJjjW3qh-yT0X41XFuP554DQMFxb8jX5wS1f0dPMzUnrAVcnDe-lAvLWUj-TOIvcw7aNocHzxmWxSqxJIcruyy_V71K8tHtkMPQ_tb_F0LAZG0INsa-Si6URZo2d9ZQeKzrAniV1efQClT9nly5ntYr6vtCNj2FZcyTdaDCYooihgE7up_mY6B2bUlSf5val3ye_dpEHjycNJ7rUx9fI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b96935ff.mp4?token=IAliFKAwcjA2-her-UGjyPt9iKN8ZU69aQxvInfkJePArkHisgm3kl2T2me0u_Jmxml8ifL7tLg78lZqR2s3GJ-Sf559la-S4GMHifZZLnfCi8SXUoEKNLi8-w_AjgkdU1YUa3jbLGLli7zsPft9gAgyUxVeKE43EPQ7Y-getdKxM78aHAq-63lIkzxLhZlQMlAE0hqORgsybYHxYz-RxdPoS8iN3qGaVLqT6k-u5JvF1EBXgU-p-wjlvmwMGJcflewzKxBIttV-53XxJ5f16w9OGME56rkmaUjCSHFHiYNLObLVN4WGRRmjAEcz4t7EOp81LM_38eTQ4SMm89ad5B8nLM2WDhMdoSko9ffDUwGjbVYPPmjw2yMcSb4gxOCDHtQPl8d1qWmGi0jfNE8UOowyVh1w17_hhSd68EmIppYdeEUOZuq2IXC2xchv0tPPLdzRVsJRu_DBlJTl0fvxQamGJjjW3qh-yT0X41XFuP554DQMFxb8jX5wS1f0dPMzUnrAVcnDe-lAvLWUj-TOIvcw7aNocHzxmWxSqxJIcruyy_V71K8tHtkMPQ_tb_F0LAZG0INsa-Si6URZo2d9ZQeKzrAniV1efQClT9nly5ntYr6vtCNj2FZcyTdaDCYooihgE7up_mY6B2bUlSf5val3ye_dpEHjycNJ7rUx9fI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دردسر دوباره برای طارمی و الهویی در فرودگاه لس‌آنجلس
🔹
کاروان تیم ملی فوتبال ایران پس از دیدار مقابل نیوزیلند درحال بازگشت به تیخوانا است، اما روند خروج مهدی طارمی و سعید الهویی از فرودگاه لس‌آنجلس مانند پرواز رفت با تأخیر غیرموجه همراه شده است.
🔹
درحال‌حاضر…</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/442541" target="_blank">📅 13:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442539">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1BBEJVjkZFAyKsnPhbo7agmZYIjn8EGjnUjCtDX59UJnZZ75tILhyKLUCfc0h2Du8U-bNGlKc8zqZaZWSE-wRj_R-qoNHem09eJ9JhGiMGXnEDqlsWqVQiOhJ4RoNw6TieWCxv1Xy6mqYBeIR8qHsaQS21HoWF4K1nEHPsAc6qf4XXMUtB7DBMXYfWCogGPfCxvXljwBUEVL2202zaTfoRe6V9jhMEHavP-PRkK5Q6T0gNbtuKriaZkXZlbNvWiCHIg42XaFwXgHg4yK81gSI4YHlgHnTsxRljg0wIX07h75WTvSruAOpjS5rjUhIxLJRAKL__PWOdFa_qv2DUHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjDDgMS7c-sndohh5NwcgczLVo6BVLhZ6r0d2uTrJWXYhuTM1f0qlvreedG9uVs1FfXoOqQOPIQGBY1hXvGgRj2ztUDtpABYcNPTjAZlc9qEHE3M6yyrZUdLRS9c6PG8gZDYGwtMfwBGO3SVmCSG1f25gpIvaBIQr_xyUsy-p30zPAKBtWpwC3nN6sva78-EhQ5NsMVNE6r2SNKhMt2ghTSKm_Ltb1bvKwGfveCX5CU3QON6_QYx55BeKUYztuBJahHBnpaPui4Yzb9Wz3ElhHgBsYICUO9paS7INL_j4SVRp3xOSX9lnWOz785f_laEgxCX-nVKVhjW9rcRMCFa_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ تعویق یک‌هفته‌ای زمان برگزاری امتحانات نهایی دانش‌آموزان
🔹
آموزش‌وپرورش: درپی برگزاری آیین وداع، تشییع و تدفین قائد شهید امت اسلامی، زمان برگزاری امتحانات نهایی پایه‌های یازدهم و دوازدهم یک هفته به تعویق افتاده است.
🔹
بر این اساس امتحانات نهایی پایهٔ یازدهم…</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/442539" target="_blank">📅 13:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442537">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63468508a.mp4?token=XheaelvkdwHRZk8IDsHe18BZKMYlGu6yxu0DfU2MKmTbopVSheuP-HXW69BqVGeroRI5WQg1r5n578mmpuVJ6pBEVgQD8wV9XfEnQOhCLMcziiqC0aNS2Xl9DsqAiFblQoy2lKyABmQkFbimIqghYw4y441mvDpYFhFjaAEnQA_T4VC8RivD4qdGXKZ3QddQVDQVozftASz0wdm5vwhhqYYshypGcM0AnZJmki-uJmKp8g3d5ztbx2n1L79b1Wwnz2fodwNUiY9bjnomLT_JBLBEJ4F28B99APaVnAUPDgCRysjybzCbkV-ZqecD7yrAvYds4HS_OME-5Ia01lJXqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63468508a.mp4?token=XheaelvkdwHRZk8IDsHe18BZKMYlGu6yxu0DfU2MKmTbopVSheuP-HXW69BqVGeroRI5WQg1r5n578mmpuVJ6pBEVgQD8wV9XfEnQOhCLMcziiqC0aNS2Xl9DsqAiFblQoy2lKyABmQkFbimIqghYw4y441mvDpYFhFjaAEnQA_T4VC8RivD4qdGXKZ3QddQVDQVozftASz0wdm5vwhhqYYshypGcM0AnZJmki-uJmKp8g3d5ztbx2n1L79b1Wwnz2fodwNUiY9bjnomLT_JBLBEJ4F28B99APaVnAUPDgCRysjybzCbkV-ZqecD7yrAvYds4HS_OME-5Ia01lJXqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسانهٔ آمریکایی: حال ترامپ خوب نیست
🔹
همزمان با سفر ترامپ به فرانسه برای نشست گروه ۷، هفته‌نامهٔ «نیو ریپابلیک» گزارش کرد: «واضح است که ترامپ حال خوبی ندارد». این رسانهٔ آمریکایی با اشاره به این سفر نوشت: ترامپ ۸۰ ساله در دیدار با ماکرون بدتر از همیشه به‌نظر می‌رسید. به‌سختی چشمانش را باز نگه می‌داشت درحالی‌که ماکرون داشت از تحولات صلح با ایران تمجید و اغلب برای قدردانی از تلاش‌هایش به ترامپ نگاه می‌کرد.
🔹
در ادامهٔ گزارش آمده: بعدتر، ترامپ که در کنار ماکرون و همسرش در فضای باز ظاهر شد، خسته به‌نظر می‌رسید و دست راستش متورم شده و تغییر رنگ داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/442537" target="_blank">📅 13:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442530">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0TnriyETisoM7JpOdKw8pibY4QRUV8HMr9lkLR1fsoDpp7AXMH8lBK7pnL4acEag4GZvk57E4FutYSak_LQZmrvmYv4r89emfLctJ8x4lJSwY69wg_NxGUPdTKgoqRI8zEi-y2OI86poqoipqQ26H9l5lrqqDhdUSY-MGFViFwEMVrtPpWLXXznxXFDBIz7yAvO5IIHAtufpLQhOU6bVXLkcJAzCL2FN6ZQNXbpoNkbVi686y9hMheBZwGEfpoGNQsjT6lljkgt8USYXu7nKWHE0UsOdEJQz8HsFV-v1zLdT0q-ZgyqG9Sek7RIOiqSl1iOxLJ5FkbZJApdSq9f9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BsZbRCAaV9kcxPiDJln98M7HKdmCtsScCvldZ3XwqcNdCa9SCpJdG8tmRiZcMH3iCrRPOGsZFoLRt7YWzDVL-QGYH45OJlMdg7v-waYdwUN9cJlEL7U6EyGz4l4HYpuP5jsZz1HiYMDXKjDt4crPgIR37JQRiTosMYeV19Gq0460v59o1GQglSaC5Tylo-U_MGe85YpKwuexnr1mamaJwoQaMe59v5fV4CGYtzbjdBLfPcndJq9SX36ZgOemjyV6XXDQutXUzVbUTkZYhKzXti5cZpIDbc_srMy79cxOjasHp935GSn6T0_6OGQmWHAa-ljx-VOoLHJZYsyEH8eqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyRhN9TkKuBSM9xTtWpZIdMe9hP2W50tdN1wSEl5FgKwrBmUN-yhkowuuDnJqT97iyVMyhJUmzK7fC_UpH5L2nhSUFM-x9DN2cTFC3UGvrwQ78r0vcCiz1hY1lIwtdg1DQOSkS2yj2d8zJWcYcNRxAmXrqCkJHTKX5OR3Lb6Sjkiq8JyT3nmv74MWeoU_6jmZjBNB1wmY3Y0qaRTiobZJNF_1uv3TENcWG9m821TpvNUvrrr9R1Co_PkzotOIhD4SxLj0Gdud0bdlUwDT19s_u_WKvtqsXaR6758BORSEOQFmXX5baX-sI5c2PlXCG9NmXRI5zLwI_uJlimLOAnVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FyimdzSIXIHH8rqTGaT148TWbKxnHH-sxorvF-vtAEVjb2rEoO6b7zjK13N4Vmb2Ge2XSxhxSopbbzU6phg4RTHZZuEsGVYtIT8gF3EoGIYilKW2dWljuSV2VZScBdzU4ALVChqZ27EF9ZqFCvHdcjy-gUisV-3Rgfkreh9W5TVmgEwAh_zGRYOwXEFkP7LHZrdQG-kSvTgpfrk5tuxoCTRnrL2uTWJg5GP6CG7Ds1uCqy10V8OiU_AvFENpzM6_yrZ9rLsmK7tKLQMfY9vikP2srvkppeHE9TyGlxHAVd2BC3agbcz8sBaaq6EOtdcvp96k39NRRGGSS5z_ASupaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJ-d97SE9naPdQJtMSB9IF1oJYwXJqU2V2KNgyaPuxM_SBUSg-fjI7paRjhuE_iYbh1ErwJ8nmrlWlXcDCW4_7u8CbnM4v82WR-xzpj34bMY_6b2dhWiVmgMBByxyBG4n-GVYscYnotLVT4SqGO9_Jt_naFhw3rRtSEMUHexZzmCOQac1KmzXH4yTjsiyaBEt5M9bFh-KDThykIq-mnbJA2GPzYJR2tumcKsQ930qvBqg4HG901eDS0JW_fu-TwIz02FdledZmwOrPZbbOpUIS4-WGgMGH7FmDyCeqD_5kMXFGJmpRDH9Ys4-E4-fUOsuu4XvOHJg3TZ4ktRq7HnfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OeyViJDjupsxt1psD010L87JFbcHohETXWezbLL6PI0vz3JCsXAaKt-Hvx9iS61vexAKybfngtY4SsiOwVwnOJWwB1P-HXuejW3fVYHjPWuaQjg-mAQSV8YqFer0TkTplFroISvVnMJnr2GUPdZGiCkkRdU_40o-uxxeuSQMtleWtkZeaWde1sD4hQBoGYcF6TtXNbWqX1Pm-px3sYVdvNU69udEFQBC09vEG7lIJ16hh_9GbY1__jKMJY4sGkNuCQ3nwE43FCHFzGhTD3i7zXGzseOuE4DkaqF5h2KnQhgfzWj6UKKQRLyDUnBbFEtFGGF3Ahwl2grHOQr5ahehRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bjp6pmwrWPvMEet8t0sgD2x7FrParcvVUX23FDDyvuoT7bi5DE7a3sorwMd_XK2uiR8qOObHvLCuoJJgqjZSd5CloJexzLZpoYuUNwR-5Mp_Vo8SYI3IpxnG2iMGpUHztFCmovdBgFwSK238knarrjORD6rhEp4O1SKqT5WLindlbD0v_52bjx4zRuE1LHd1Wa8guYGEzAoKs2mwq2euuUB5aMhAnWooVp7_E-YfaoMYeUlh3QbHtEQjM9HkJJfX3MCdYnY0n40l2sehHdwKolebNgBiPQqLXPQqxadvpUFa3USZB63MVYqXs8ORu2OHO_MOL3SWYQYI76HmX-WZlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اعطای نشان فداکاری به خانوادهٔ ۷ شهید ارتش
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/442530" target="_blank">📅 13:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442529">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جواد زمانی و ابوالفضل ساعدی از لیدر‌های مسلح کودتای دی ۱۴۰۴ اعدام شدند
🔹
رئیس‌کل دادگستری استان سمنان از اجرای حکم اعدام جواد زمانی و ابوالفضل ساعدی به‌اتهام محاربه و افساد فی‌الارض از طریق کشیدن سلاح گرم و سرد، تخریب عمدی اموال عمومی و خصوصی به‌قصد مقابله با نظام جمهوری اسلامی ایران و اخلال در نظم و امنیت جامعه، اجتماع و تبانی برای ارتکاب جرم علیه امنیت داخلی کشور خبر داد و اعلام کرد «حکم اعدام نامبردگان بامداد امروز اجرا شد».
🔹
در ناآرامی‌ها و اغتشاشات دی ۱۴۰۴ شاهرود، این افراد با سوءاستفاده از مطالبات و اعتراضات برخی اقشار جامعه و در راستای اهداف دشمنان آمریکایی صهیونی علیه جمهوری اسلامی ایران، جرایم متعدد از جمله تخریب و آتش‌زدن اموال عمومی و خصوصی، اخلال در نظم و امنیت عمومی، اجتماع و تبانی علیه امنیت کشور و سایر اقدامات مجرمانه را مرتکب شدند.
🔹
براساس مستندات موجود در پرونده‌ها، محکومان اقدام به شکستن تجهیزات و در چند شعبه بانک، ایجاد آشوب و شورش در مقابل فرمانداری، واژگون‌کردن خودروی پلیس و مشارکت در آتش‌زدن آن، حمله به منزال و تخریب خودرو و انجام سایر اقدامات مجرمانهٔ مؤثر در برهم‌زدن نظم عمومی و امنیت جامعه کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442529" target="_blank">📅 12:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442528">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqyyjJzaS63X8o3rVjQiGO5QgzK2oafMcWW_9Y3AJkv0Ad2k58hgPSuFunm4l8aluVHNMjRPSc44eMMa4rCMFskxpKa6WKDjQnXeVghtg5W1eRzCXbotnnItacNKFeDCFvXsLk9_o_KjRt3BHetjyOUtUGoCuHn2eTVTAOjpwVbKKYaK6blhLZX7IrhB3c9gSTEGDw4PR_zgvp7FpJdB_lDGJNZyKn5TmYTJT0LiZaCXyhaD1VWGGz9oP7a0dTgZk0f0NGpjXX-BQIoxarJgTwktvOJCUtjgVOpUmDWZ4Ukma7SVaodJUxSfXzvmERXKOBZo3oat56SVgKw_tqY5PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۵ میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با عبور از مرز ۵ میلیون واحد رکورد تاریخی جدیدی را ثبت کرد. @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/442528" target="_blank">📅 12:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442527">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎥
اذن عزای سیدالشهدا(ع) از امام رئوف در حرم مطهر رضوی
🔹
مراسم اذن عزای سید و سالار شهیدان در حرم امام رضا(ع) برگزار شد و با تعویض پوش و پرچم گنبد رضوی، حرم ایشان به‌مدت ۶۳ روز به‌رنگ عزای امام حسین(ع) در آمد.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/442527" target="_blank">📅 12:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442526">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYNUuy4NExvGKLJNdpFUnUBDLjvL6-pwbln-ro7zQMqHnYkRkAG6ZX-FaZx2c09V70fi3cSFCSSQWs12O-lUoHNGaKuGATfrgSxW3_G4dFFts92zi2O0v_Z9Hjar8IAV79GyqsEVk7LXs28TGbUj5cLeiS8wpxAulrlFShxcOnd-uH1KOGFMsU3RAwPC9Eely8wtfozG_qug90aotwJdGy2Y1MiE3UTrN2V29mK-yv_O5IpZKM0Mb74r3DmibUlx6PzvBBr1tvdoLDekqpsg22Jm4VoTeZPDGEDhYc05YSSVlAzoa_TAm3aOusFWNM6HKMDa1465TNSWR1f3cDxlOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم آمد و افق خونین نزدیک شد
🔹
سال ۶۱ هجری قمری چند هفته از خروج امام حسین بن علی از مکه می‌گذشت. کاروانی که از مدینه راه افتاده بود، اکنون در سرزمین عراق پیش می‌رفت؛ سرزمینی که هزاران نامه از آن رسیده و نویسندگانش از امام خواسته بودند به کوفه بیاید و رهبری آنان را برعهده بگیرد.
🔹
اما در همان روزها خبرهای نگران‌کننده‌ای نیز به کاروان می‌رسید. فرستادگان کوفه یکی پس از دیگری از تغییر اوضاع خبر می‌دادند. عبیدالله بن زیاد با شدت عمل وارد شهر شده بود و بسیاری از همان کسانی که نامه نوشته بودند، یا سکوت کرده بودند یا به اجبار با یزید همراه شده بودند.
🔹
چند روز پیش از آغاز محرم، خبر شهادت مسلم بن عقیل به امام رسیده بود. کاروان در مسیر عراق حرکت می‌کرد و از سوی نیروهای یزید زیر نظر بود. فرمانده‌ای به‌نام «حر بن یزید ریاحی» مأمور شده بود راه را بر امام ببندد و اجازه ندهد کاروان به کوفه وارد شود یا به منطقه‌ای امن بازگردد.
🔹
فضای کاروان با روزهای قبل تفاوت کرده بود. نشانه‌ها حکایت از آن داشت که رویارویی بزرگی در پیش است. امام بارها در طول مسیر به همراهان یادآوری می‌کرد که اوضاع تغییر کرده و هرکس مایل است می‌تواند بازگردد.
🔹
کاروان در این روزها تحت مراقبت کامل نیروهای حر حرکت می‌کرد و عملاً اختیار انتخاب مسیر از آنان گرفته شده بود.
🔹
محرم آغاز شده بود؛ ماهی که حرام و زمان پرهیز از جنگ به شمار می‌رفت. اما این‌بار حوادث به سمتی می‌رفت که قرار بود در همین ماه، یکی از مهم‌ترین و تلخ‌ترین رخدادهای تاریخ اسلام رقم بخورد.
🔹
کاروان هنوز به کربلا نرسیده بود؛ اما سایهٔ کربلا بر سر همه افتاده بود.
@Farsna
-
#روایت_کربلا</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442526" target="_blank">📅 12:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442525">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هرگونه حملهٔ نظامی رژیم صهیونیستی به لبنان یا ادامهٔ اشغال سرزمین‌های لبنان نقض یادداشت تفاهم است.</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/442525" target="_blank">📅 11:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442524">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-OWZNWRFmY0i8uN83rc9VInfXUQqPKRAOzTUclV0qLJCp6x68Hms7U0hS16EMJ8YuDot8kmpeIe-A2uMmKJLQCrygOxxijhrU2TFSDooKNOCHM0mKKLhn8mlTfeNKh2eY87evOmOgxXvQdRBmobE-U5sBKXniWkf-gTUYTd0tUyerIrBndMxYsFifB3EiAaPK20k4sOce9MlYQfHjSgHAPlMxiXq05N79k1PILE0ubkozlBCTWTQCSI5r9YjomeeB6zBtoGYFxwQ1DJ8w3YfIuGsS4nAywlYoGqECYM4dhvm3qMoDxQL_1HPW47v6M1mhhQFExbpMDx_IkytNU6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
حماقت ترامپ
🔹
کاریکاتور جدید کمال شرف، کاریکاتوریست یمنی
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/442524" target="_blank">📅 11:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442522">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec0210a91.mp4?token=Dcm5dCLMV3cjvzCyNOkzw89ej8KeT3bM_AZOgqltUgi74G72fu5qrwhu_tfdF0sa8TtxiXb84DnwvgoFgLadOvQmV0-PWtxtFJDqY-4QOV--bWDig1MkVdDDbL127iSB8GemJaPIPYHPurgnEIkqCsPmPCCw33npfvLlQFAWjPkpYXutc9REbQFrLNCTGtH4gdUV_rUu1bG1TNSgL4-AwpwlibNqq6hWKzCe7Y8hTBqMcKVeLc9GbZ2CRK4_s9rvLnGCtad2r-Nus2AFqG80s8ESVbCw3qEA0RUX9A6c2kTYKYSrIYUwgI7vWURHZZvcLSo03NG8qL2SSVii4NBwv6HCYU0Z_NwatNwGy3w4tKPJYZSVtlwZrs6FI6KeBkQbnuT3P_3OcsKyikVl4rJT-_-GhoEDmYruF8yh4RgZC9-Z4UnmeLe6DK3LOGYK1fWHOguRn-8DMGeF0uGeLDtVe6LjYGTMozw3v7F6SZZQOk_-mjlMtKdFybo-vyrPjdRQ-Ja_z6h-YL604oi0zBAkaRKXibM-8wQ6xKcwJmjXh4cHzJoeT830v7yXNCPI8jhjsAbJqHKmo948zYdpO5Cug5Bv8KFCF91tPCoNifWmR1f5lMTJPgms500m6oG9PKSYZ3xMQK_qO3yGKZ7VWPgur19UUWxBFbmBCsJhz5NQL8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec0210a91.mp4?token=Dcm5dCLMV3cjvzCyNOkzw89ej8KeT3bM_AZOgqltUgi74G72fu5qrwhu_tfdF0sa8TtxiXb84DnwvgoFgLadOvQmV0-PWtxtFJDqY-4QOV--bWDig1MkVdDDbL127iSB8GemJaPIPYHPurgnEIkqCsPmPCCw33npfvLlQFAWjPkpYXutc9REbQFrLNCTGtH4gdUV_rUu1bG1TNSgL4-AwpwlibNqq6hWKzCe7Y8hTBqMcKVeLc9GbZ2CRK4_s9rvLnGCtad2r-Nus2AFqG80s8ESVbCw3qEA0RUX9A6c2kTYKYSrIYUwgI7vWURHZZvcLSo03NG8qL2SSVii4NBwv6HCYU0Z_NwatNwGy3w4tKPJYZSVtlwZrs6FI6KeBkQbnuT3P_3OcsKyikVl4rJT-_-GhoEDmYruF8yh4RgZC9-Z4UnmeLe6DK3LOGYK1fWHOguRn-8DMGeF0uGeLDtVe6LjYGTMozw3v7F6SZZQOk_-mjlMtKdFybo-vyrPjdRQ-Ja_z6h-YL604oi0zBAkaRKXibM-8wQ6xKcwJmjXh4cHzJoeT830v7yXNCPI8jhjsAbJqHKmo948zYdpO5Cug5Bv8KFCF91tPCoNifWmR1f5lMTJPgms500m6oG9PKSYZ3xMQK_qO3yGKZ7VWPgur19UUWxBFbmBCsJhz5NQL8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر زیبایی از یادبود شهدای میناب در رختکن تیم ملی
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442522" target="_blank">📅 11:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442521">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda22ccf1d.mp4?token=ByzGOlo1BubCAbfyISVIA8YyJoorJHvXSmvfcJds5f8DZ5AOK48vQbVPRFQwor08-q3UcIvXH7PdaLCfPIKLQyyXuAm5599hDYA3AlIPXn4uE4A9ZwYQfY5ajXm9r0GIwwwnSKhL4l3dsj9Bz5qGTDTetKVRZUrFSjl-Xar3IRYus5WM_wqulCaB8G2R9jckdIyZbtDxjxi1n2xTiy0E4Bp5ELabb74J06I2gbWr04G_Zdox2K_spJD7aOo4efgFvdEKlDtCqPeP130gDIg1Vp5AQcNquBx-2jvfaXV6EsH7CcsEPkqDbOQyIqi1XVwRa_XQOl7QvxHGy75PGngF7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda22ccf1d.mp4?token=ByzGOlo1BubCAbfyISVIA8YyJoorJHvXSmvfcJds5f8DZ5AOK48vQbVPRFQwor08-q3UcIvXH7PdaLCfPIKLQyyXuAm5599hDYA3AlIPXn4uE4A9ZwYQfY5ajXm9r0GIwwwnSKhL4l3dsj9Bz5qGTDTetKVRZUrFSjl-Xar3IRYus5WM_wqulCaB8G2R9jckdIyZbtDxjxi1n2xTiy0E4Bp5ELabb74J06I2gbWr04G_Zdox2K_spJD7aOo4efgFvdEKlDtCqPeP130gDIg1Vp5AQcNquBx-2jvfaXV6EsH7CcsEPkqDbOQyIqi1XVwRa_XQOl7QvxHGy75PGngF7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: جمعه پس‌از امضای تفاهم، مذاکرات آغاز خواهد شد
🔹
در مرحلهٔ اول مذاکرات دربارهٔ خاتمهٔ جنگ، محاصرهٔ دریایی، تنگهٔ هرمز و آزادسازی وجوه مسدودشدهٔ ایران تفاهم شد و در توافق نهایی دربارهٔ موضوع هسته‌ای و لغو تحریم‌ها تصمیم‌گیری خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/442521" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442520">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce85b3d54d.mp4?token=Adyzi4qPDymqdFf8_VoMJeGqYazYX--hU_ElaYyL10xi5d6Dk1e3Iobl3hAR0uMbR2rFcACJ0zQf6pA-M4DCtoostm4FON9fQF4OgjOC-zORaWCr58N4R2LqcsGZhkvt6i9BIucqdjlQG-8oKhSk1oXez6DH_WKFzBgVob_iV-_sQih0FZQvc4fEwnUtCbXFXBI_5pohqJ0tqv8Dfjz--zz45-d1jUaxjCwNj42ntPpHkca4z1PiwLmqegeXEGlGbbSWSoJLmX90w4foY7LhUO9NIJQF7QU62G2aB6whnuk5pJ8g1V4bVogcLar7u8_51t8WdkBs9P_mk1UpM9du3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce85b3d54d.mp4?token=Adyzi4qPDymqdFf8_VoMJeGqYazYX--hU_ElaYyL10xi5d6Dk1e3Iobl3hAR0uMbR2rFcACJ0zQf6pA-M4DCtoostm4FON9fQF4OgjOC-zORaWCr58N4R2LqcsGZhkvt6i9BIucqdjlQG-8oKhSk1oXez6DH_WKFzBgVob_iV-_sQih0FZQvc4fEwnUtCbXFXBI_5pohqJ0tqv8Dfjz--zz45-d1jUaxjCwNj42ntPpHkca4z1PiwLmqegeXEGlGbbSWSoJLmX90w4foY7LhUO9NIJQF7QU62G2aB6whnuk5pJ8g1V4bVogcLar7u8_51t8WdkBs9P_mk1UpM9du3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: متن تفاهم با ایران بعد از جمعه منتشر می‌شود
🔹
این سند بسیار محکم و تأثیرگذاری است. مثل سند زمان اوباما نیست که یک سند افتضاح بود. این یک متن بسیار قوی است و من می‌خواهم که انتشار پیدا کند. بنابراین احتمالاً خیلی زود این اتفاق می‌افتد. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/442520" target="_blank">📅 10:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442513">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICKNZyYD8kkQBrH4zl3Az_fnuBg7qD6fYIncaVdgKyzrNj26nycS7UdAE7QSbUbX-jbGrPtuEuVEIB_ih--p44SnPbDecMgUiLBKYlEftqbJ5HTLOFI-5y57NuN4DN-98K6wlJR1x9mJ_-PX4NuzvO-tyKRG0x1NEXG025LQ6Xt9DOT_loyrcPbnbwVjmc0gdVpgcM6KgdJmxZV_okCWgBcs2xxUtU_WcE2Y-P8MS_Rsn0MTgEawo8d-CrpSaxmCHP4NcDSccopv0Mxxf2sJSjiB4ZLQceRpUs_HNeNthmJ8ogufKZt0jRnnZWhSOf6QFeFWpxKbY6-Dpx9Sgz5fCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXn-6p4ffdGdtjR1FZh4pAEi5_E5B0B4Jd4DMF20P1QLSiZSh-Pdb3b3JWCS64jlDjAuUxiso-ayjMlRajd0r010LJIjEiZuc4Kli8DCbQSC79VlrjvlYacpmOFgmCG7YPJt1uveg4wlPxIdeqW51QIxTfX2AreolICkzo52_LoQWiY4o60HPJDo4QX-nAUfGV-E-suaeMSgCkqerW_fmaP4Gbyv7pqvIrtk2XJ3x4QvpE3F5i7A4KW7y97-WIuyvXMPAvR3bf_mhq_fzTLyuoMW5T9XUqZsTc-0VVsiTlt_yJBU1W5htyony9Et7Gc6oPh7HIlGfZku6Owssq1o8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBYRg3tRxtv7-96_els1lgKPUHz-b0DuA8oiPbft54mYzp_Yo7SNCMuKDCWvemRVLM5lYCW7MFgvT4ORERHz8paDX_Tzc3lsg6nCmMKYISG2rvuJ-ZbxeFOKn46ZUn5Xmn_Y-TGDL3FSxnJDHI3OK-exE6-cZYziqdBrcVy43q_Har9eFXsCBEab2S7uxs3vpCrg9ESYdpi5NMtyWXs4b84OB98I2zxU3KDw2xhhT3mnE-Q6520SH1PNPjCb5b0o8paPQ-zeRrWNJb8TMH3_GzIP5-G_OWZ3eTzmpXdzbIHLZ-Rm8y5Lfx9IWAGbwRp0voN8RvZGSweSSM9VEV2rNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J6IrpiLd7TqvlfqMvUqLfJBzXUnHo-pTkBV7Oi2q5GQF0U8McJ-GhOrZ7LYovcd9Ae71I12cDRX_Ds3ELRxHfbpQNXvj0GNe2epmT-JJt-dQI2CszQw0MGq3-ponqlZFUJfoeN2gkFi0OglSAeb4UoO-3oUdFj93O6CBrml37hIqMS_SZHhfolTCoINKaOubLJrqEq_7BMKR1XJGbvuyQHkzxF68tOOrc2u9oTagIBlUFVB4JSTwjjU03iuf4eFmBkKgpT9REfJi_V73qAcUdwguq6-xWqTpW5BnskSYF-uQxR7qtObZ4yWfwGheN73By9wP-Y1S3DuwbQx1He45kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOfbYYGt9Vl2_eJYH4nEPXMIfXl1CxUAKl_ofi8V3rYaui5K174vyj5HscLlr_Dsx4c4lFc6QqnsAaKwjVKOnFoUjLuht-0ACFx_nJu0v4DIgxpExlxGUVZJuVqP_NRfOr5zheNv2lcLK-EI4CD4uWvqXIWEYeBF9T5Ng54tT8MsnOHQeoL2ku2f9zuhycfBxklr62oyXFVetD59fZPJ2ORlNUdLc4_4wbkU1RieUp_CV7F5DvZUGVOLSxBIp6An7IHAr8hztbjqhFF4V7hUe6A5VM7Jf2KwoNBUxEX_QxdTZavbhozynmOxKJxACxekKNc2uBG1j8pITwIOG-Yt7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VS6VtIYsZT3IHBdU_FomRQebwrva5vKnG1F-UFswH16WLeXJtU2ZpIgX-KuIBs3ablpFUF0BeUE1Kls8Q608X82Y7tbkcpPo6uUFMpRCEAUsJ6sHfP-ej_KkACdngUaQkpzczB4nop35rBRgABiVrmYLAOfH4bREIae32Ze4GpngVJD4DdPg3IykHLziGk6zlLiMm-111_5bwhQcjwPa5U5WsmpsZw2Rqpu_c83wglvVIxwIOjkOU22-aSAthJ59Y-tonqWkyn7qsMW87n1Se-VhQRVc7QNKL5LtAAzRlW0r7Wsva7n-ntOcfGJr6zbEbxz8MhR7gQGxqr6flMGSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOAsH5_9anK2xUdfNo7KUcSdL7o7ybbU47BYflsnEpnS0mTvqWDC849IVsamcGSjsMhYRhwQ_7PtNYQ04_dIYR6EXYmCUOpmS8NaXMFbg0hDVoar8mL-s79J_0-nx08tsetevaPo47oOrfj10Ot6QJZo-3sZXYHEejHssszOeX3OCLPeDQ-F6Ja91hJf88SckmUGD2Ww1YqkZLB3DNafEHhn-fhkmipuUGKaYPYAR6S8wq3hw_zLFdw3OkNPmY5p-x-1yPPsNz-xWyO9lfJq2XLKzbHNba9graeXIHdCx0aQrLceBlK0bRr2crVM8YfX9ZiF1sUaU4xIEWWT1xTxlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
خلاصۀ بازی ایران و نیوزیلند  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/442513" target="_blank">📅 10:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442512">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4pzZoMOxGbN17s-KrY1zcz5lOuILwhrO8882VlU4frhvFI65m36LoMrQpcO4S_IAo1wjnAMgxw4tRutzdcdvtG9EWIwK5SglrC-ztsnWwhcboIMhp1wnFYHtbou77uLWNZTunxJmhDH4sHJKEj1-XP-DizE2rrLBBgwm6TD_hOT_wTf__lW85vUt0Xz0Sr65LEsLP3ucuoVmx3Jxnbgg7skdzwYLO3Nd3AZ9svmrVnO2-35RANYmz5Ux0Cyb_4xauzTKIz2zGkLrkIgmedccuO0d1rLx6wYtIcS5crCxIK1m9v-DeQGex5ah2tFGYDujyZfTOPTfd3w-PzLuXIE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل ارتش: هرگونه خطای دشمن با خشم انباشته مواجه می‌شود
🔹
دشمن در جنگ رمضان و جنگ ۱۲ روزه به‌دنبال تسلیم ایران، نابودی جمهوری اسلامی و حتی تغییر نقشۀ کشور بود، اما هیچ‌یک از این اهداف محقق نشد و در نهایت خود به‌دنبال آتش‌بس رفت.
🔹
برآورد دشمن از مردم ایران اشتباه بود؛ ملت ایران با حضور در صحنه نشان دادند در دفاع از کشور، اعتقادات و نظام اسلامی ایستاده‌اند و بخش مهمی از این نبرد را مدیریت کردند.
🔹
اگر دشمن اشتباهی بکند با یک خشم انباشته مواجه خواهد شد که کار دشمن را بسیار بسیار سخت خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/442512" target="_blank">📅 10:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442511">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSjcTDspoWViuUgj6TWX-sBh4SMHubSTecHK3ugMYeissoKu3QgbZabg1_Nr8BzkMJ3sq8ZDPwaWrQtJtpJsj05dSwXypANlbQaHaApMMSuu1k5EyJ9qoT22EQcr_uH3maTVjv0WF4XoqddJ-rYGYNQboF2EF6Mqrq86QwtEhHTfF9-ZDq8lhEeXEx5XjfZQZZlzWJqG9RTVvK94nO_0I1mEbG5Bp_a7yVXLhuvf58Af4kY-lYWvZFv-Ut9ajsRLAjf3KsA71_Fg8lfr0g0AhjDbtQyHyfrVUfgswEL-Giq3A1HipLfg6QBSXqc8y3Bg4nPGFVPBxgKqKjRGFoO9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمران: ایجاد منطقه آزاد در تهران به تسهیل ترخیص کالا کمک می‌کند
🔹
رئیس شورای شهر تهران در واکنش به مطرح شدن ایدهٔ ایجاد منطقهٔ آزاد در تهران گفت: چنین اقدامی می‌تواند در تسهیل ترخیص کالا مؤثر باشد. برای نمونه، در صورت ایجاد این منطقه اتوبوس‌هایی که در گمرک بندرعباس متوقف مانده در تهران ترخیص می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442511" target="_blank">📅 10:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442510">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دردسر دوباره برای طارمی و الهویی در فرودگاه لس‌آنجلس
🔹
کاروان تیم ملی فوتبال ایران پس از دیدار مقابل نیوزیلند درحال بازگشت به تیخوانا است، اما روند خروج مهدی طارمی و سعید الهویی از فرودگاه لس‌آنجلس مانند پرواز رفت با تأخیر غیرموجه همراه شده است.
🔹
درحال‌حاضر…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/442510" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442509">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQTXJMvA0Sxkfr0nMu__lSr5xMSInmJFj40P3y0AarINq4U7JJeT424jvI1HOnNhGAZgGLsOAjvLnQ5ZrQDy90eX0yYxlAArnQMUqa7Gt-Fo1kTfco6meez8l7-oXdBbqApP-kgMY3Xpf2d1nwZT8KVE6Khhqh1GpWxkIvYoyP98OwA_JdaI3pSFHYJcKysc1D_XpIOK8MHFWJiBQ6vI0fUpBfKdEw1lpVtFLe_klOOAbgDV90LvoXX1a6zC2uZIZLqsNN17GaUUiaWNKJ6wojLS-XZZPuWJb4nPwDBqSBYx2LJzHztG2DhBJfdvsWXrLZ06r5EN5LwAHCaa_uF6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دردسر دوباره برای طارمی و الهویی در فرودگاه لس‌آنجلس
🔹
کاروان تیم ملی فوتبال ایران پس از دیدار مقابل نیوزیلند درحال بازگشت به تیخوانا است، اما روند خروج مهدی طارمی و سعید الهویی از فرودگاه لس‌آنجلس مانند پرواز رفت با تأخیر غیرموجه همراه شده است.
🔹
درحال‌حاضر تمامی اعضای تیم ملی در هواپیما حضور دارند، اما این ۲ عضو تیم ملی همچنان در مراحل نهایی خروج از فرودگاه قرار دارند و تلاش‌ها برای رفع این مشکل ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/442509" target="_blank">📅 10:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442508">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INAJsOKgaoZBxmqPt9KdDnVWnI5XxoSB0Ot7iFx2dnKAmEi2IKspmaO5HbNerhQWOzU6RtqJxXeMxVzVxGqS2Vai9JJsZu8ZMoDrq9bYGUZzHZ_s1RAhivopIoKa2qA8svm3ZQMXzWdm52EOgjv1LO3GVM4OQEFmBxKW2sx8-8kgL6yino42TXdGQ6Q1hmYItAYolIz8LXTYyNX4p7XhV9l57aFY0S__vQcr0qEmHeiKMoehUpSvuqSpDFmD5cE8Ab_IvUwPt_nsnkiXMvnoeX4iHbsFBu6axFDhV3NJ8MSeFYETqQZTZEojWBwH_Dk3WryCMmHUayB4CkwCarw56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب گزینهٔ اول استقلال
🗣
براساس پیگیری خبرنگار فارس، درحال حاضر سهراب بختیاری‌زاده گزینه اصلی سرمربیگری استقلال در لیگ ۲۶ است.
🗣
قرار است شنبه هفته آینده کمیته فنی جلسه‌ای را با حضور تاجرنیا برگزار کند.  @Sportfars - Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/442508" target="_blank">📅 09:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442507">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده تا ساعت ۱۴ امروز، احتمال شنیدن صدای انفجار در صفه، بهارستان و اطراف آن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/442507" target="_blank">📅 09:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442506">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZ8QkNh8MqONc-OoxmkkaRbcJm3a2H9FSRTeqoSme710QFI68qt_OXZV3rBtxJMEEQLRbRPgypHI3OQyRIL3GjIhXN0s-CTZUXQ82U9mQMs2sXBFvSEiwItLLK1wECTF_F2RwzOxCDjRKCpnsgF-AluGeavw_Zi5QnnyckW4EqO3-5svsgvgqtAp7kAUDfTm7bO43nHXFOloQSs0E6InwfpwdWsEzot0FYXlf3QJEIkRUs_9w9WUgIFianCZabPqd6x_7i43u_EMJJfdz1NaQBrBgwENttLpkYJp1Na3yjnPoHnVqJa-eXJOXkAY8Zd2ElsVUc-F9xH-X7nHoobGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک افسر پلیس حین مقابله با قاچاق
🔹
ستوان‌دوم عرفان شکوری از کارکنان انتظامی تالش در جریان دستگیری متهم به قاچاق کالا که دارای چندین فقره سابقهٔ شرارت نیز بود، به شهادت رسید؛ طبق اعلام پلیس مازندران، متهم دستگیر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/442506" target="_blank">📅 09:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442505">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxtCGAFWNW_U6DCzKXVv1q4JQXI32EaZSmiQDsIREGcMVX2R38QbcYiScgNka710plYWHFO19jUyd0kgJYxXsQ4bYZP7hMzppIa6Fn-bWru80WspRua2ICsnNRnzxwmxIeubBc6fjojC0aLdq-IgZL4s2tuwGDV7BtEdAzKSbfCApKMVpcXZajTvfyUHGaHFNqbj1Hgjwopw8wrupPjXamallClojFhRq8X3L6Ki-M_6lNEiFMl3a_z3TM0P4vAlFER9PHjz9SV6xh_z-UGJpyb9orpQJ4yhN-NZT5tz16dCdGzD_0Fdf_O0gP_ArR9aIKqFduR9-su2w_w62JO4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سند منطقهٔ آزاد مهران صادر شد
🔹
سازمان ثبت اسناد کشور: سند مالکیت منطقهٔ آزاد تجاری-صنعتی مهران، به‌وسعت ۷ هزار هکتار و در قالب ۷ پلاک اصلی صادر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/442505" target="_blank">📅 09:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442504">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejZYAAks7Q7r26zBCzAIfwAxWlKRsfPOJ7jmvUEwb0BCNqIpShQXx3hsXYgA2PaxKC7DnCCtPpZMRbfk9jdtBDfPOT-E95MetmANpWCVFunY8u7Za3jhu-x4Iu_1D5eQjLy8ofPLtx10o64yhlzCUDAyAbxAzxncLlrC9NfETnRlek6lOVDsGe6XyvX4HJ4g-WQiq6EwAelItfUAn_WgVSOYreiGx5NPwKZKCr40S5ghTwe4d7DuA07vYEd1znZaSeOtrR04Z3U2Yz6QN7AiaqUmRmkEWh_4CMaB_hoNI4P15heYMFGrAqCGvPMDjZOkD5Qv-7JgK2ARnYYECSLVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۵ میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با عبور از مرز ۵ میلیون واحد رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/442504" target="_blank">📅 09:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442503">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎥
زاکانی: ۱۴ بند تفاهم با نظریهٔ تفسیری مذاکره‌کنندگان و امضای آنان به‌عنوان یک سند در نظام اسلامی است و اعضای شورای‌عالی امنیت ملی به آن رای داده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/442503" target="_blank">📅 09:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442502">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1areXz022BwyywlA5zzTXQmWCugD_rzPlB6kGu7t5DutKMlQKlrMPwEBzo8JWYEq3EYHqDmuIJ6fP5Bekz-VLkn7SibRZ7niKGlQHBIfBZ9d95zRjX_HfWImN1NwsEuXITp8kwuIedbcq-GFLvuQOep-J8EXENYu-SnRqogOVvAVzMGzt7vbbY4V9AvsFXmYMWWflYYd9sfzGiqvpbCWkj8fHUiN40xRwDwYqFnFi07aWzYhViAyVesH8ixUVhGdzlq91S7zBCHB8n8qX7YFgMhFp_d3V5xa074OR_1uh_gh_uYbk39unpRT2ZESS5qkyqEZ3CvBzrJ_WQl1HvTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌙
ستاد استهلال دفتر رهبر انقلاب: امروز اول ماه محرم‌ است.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/442502" target="_blank">📅 08:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442501">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0379533dc4.mp4?token=Zk_w1Y_M_pwGTBGG-rZd2lONvpeCtfqOOvOt25IPKcB66rE9DRRXqRLzX40tz2Ah3sjVc6af3XtHcVNm0mrjk-abD3dmY2A-_j5lwVXSkym7mrxjZrPdaqdRX0kwtyctMMydBtMEWFpUtEaBXVGfq7utUHgHxzgqfhGORWdLtAYzjWBkoapqg_H1q9tPVVcNE8BtmE7WQ00pvlIkX34mFjoOshS5HJyHlPu4eu-ZI-4i2cQKuJRnhwxDN5tQtgF69OqnnmepVKWl94PWDcILtU75AzJCS2hrANN1exzB1iUKu3HDoCdJBId7Y6Me8vuORNtxQ2RrR3z99cKEVOVjQmpA3_lyCL3BpaWsDJhRTZyqPm7U_tLG0p-Uk1kIxW-xSwmXQmw4K9nD94uKLo_DN21j2sjb796aDZmww_vBq41mE_5o0ajqVWV34V8mlPExBLRoSxkRp5BUzBW-yQdFYq_U_ALK7j7lUttSW1r-rHIox-0Gg4KmxFnu3XTrqd78qXMjuZ5ANKFpCBbBcIY02UvHqJcBk_bvn6wSa4ckgRLLFim1JF2wo2JFJ4niYRc-Q2UZFx94d7wDnkg986TwllEiaVipHACatSaUEe3xMhFjPfysQD4hEN4VpH91zbXejEAE23GMfhcKP9OJLg6FyxqM70kV0jZ-FERIZBGJfjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0379533dc4.mp4?token=Zk_w1Y_M_pwGTBGG-rZd2lONvpeCtfqOOvOt25IPKcB66rE9DRRXqRLzX40tz2Ah3sjVc6af3XtHcVNm0mrjk-abD3dmY2A-_j5lwVXSkym7mrxjZrPdaqdRX0kwtyctMMydBtMEWFpUtEaBXVGfq7utUHgHxzgqfhGORWdLtAYzjWBkoapqg_H1q9tPVVcNE8BtmE7WQ00pvlIkX34mFjoOshS5HJyHlPu4eu-ZI-4i2cQKuJRnhwxDN5tQtgF69OqnnmepVKWl94PWDcILtU75AzJCS2hrANN1exzB1iUKu3HDoCdJBId7Y6Me8vuORNtxQ2RrR3z99cKEVOVjQmpA3_lyCL3BpaWsDJhRTZyqPm7U_tLG0p-Uk1kIxW-xSwmXQmw4K9nD94uKLo_DN21j2sjb796aDZmww_vBq41mE_5o0ajqVWV34V8mlPExBLRoSxkRp5BUzBW-yQdFYq_U_ALK7j7lUttSW1r-rHIox-0Gg4KmxFnu3XTrqd78qXMjuZ5ANKFpCBbBcIY02UvHqJcBk_bvn6wSa4ckgRLLFim1JF2wo2JFJ4niYRc-Q2UZFx94d7wDnkg986TwllEiaVipHACatSaUEe3xMhFjPfysQD4hEN4VpH91zbXejEAE23GMfhcKP9OJLg6FyxqM70kV0jZ-FERIZBGJfjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: بازی خوبی کردیم اما از نتیجه راضی نیستم؛ شانس برد داشتیم.
🔹
باید زودتر می‌آمدیم که اجازه ندادند. سازگاری ما هنوز کامل نشده است.  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442501" target="_blank">📅 08:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442500">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">همتی به مسکو رفت
🔹
رئیس بانک مرکزی در رأس هیئتی با هدف توسعۀ روابط پولی و بانکی میان ایران و روسیه، صبح امروز عازم مسکو شد.
🔹
این سفر در راستای گسترش همکاری‌های مالی و تقویت تعاملات بانکی میان دو کشور انجام می‌شود و قرار است طی آن، طرفین دربارۀ راهکارهای تسهیل مبادلات پولی، تقویت همکاری میان بانک‌های مرکزی و ایجاد سازوکارهای جدید برای افزایش حجم مبادلات اقتصادی گفت‌وگو کنند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442500" target="_blank">📅 08:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442499">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/508119118f.mp4?token=EDwtN7snBHwGXCLXl60hbDWhh1gFyGJzDcqGxGtD9CdqXp59TSEoEb3Bhl2_ImHwgImKm7z3RMXIiu7Y8YcP1PiHP-Fx83cXxNzCpBQF4gC8zbif-tjHSZjG_y7pnBIL-J-2LIVoF1DRQsd90c9tcF15iSCMOzbSGe7jW6_pgrWHQj9Uq12_PtO-rymQz5xgbmdY09d4wrDg31yxEKJvpxYgXjXJt-5PowyBEu6uYHU9xM6Upsv44OPQ2mk2Qqb6Kp8HPpyId5dV0EjRNdIPaU_hPLEJZ2RblW6efsXkU7H7g3Hx019rb_8Un3K_W4Bl4MGV6tVAzH6t8pOQJNit2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/508119118f.mp4?token=EDwtN7snBHwGXCLXl60hbDWhh1gFyGJzDcqGxGtD9CdqXp59TSEoEb3Bhl2_ImHwgImKm7z3RMXIiu7Y8YcP1PiHP-Fx83cXxNzCpBQF4gC8zbif-tjHSZjG_y7pnBIL-J-2LIVoF1DRQsd90c9tcF15iSCMOzbSGe7jW6_pgrWHQj9Uq12_PtO-rymQz5xgbmdY09d4wrDg31yxEKJvpxYgXjXJt-5PowyBEu6uYHU9xM6Upsv44OPQ2mk2Qqb6Kp8HPpyId5dV0EjRNdIPaU_hPLEJZ2RblW6efsXkU7H7g3Hx019rb_8Un3K_W4Bl4MGV6tVAzH6t8pOQJNit2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت زنانی که پای آرمان‌هایشان ایستاده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/442499" target="_blank">📅 07:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442498">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kg4AxkHEiPouEDSP5wQ4S2RZFbW27iv0JTv9wwipmyK1_9mLSiVbCbMYW6v0YFIsUKasZel8tvTiWf8rKIftZYii_gabtI4gCfkrcp2moybd1lcIHsc2QehKKYejBOl6xY-e_4Cszx2kOKsrsTziiXuseMijDXlauwyniILXZULwQxyuCgrqobK2S7ggFAixFvChwTlsQ1o44_lvWa4X0_XSI55n8yKOpwZcb4Zw39xfMsh7lA7JdJVVD9jLJs8miH8nC_hxCZk4Lu8OtzWDBHiib_MLBGHF7ki9diUxRkGBBtBBEdXFzflyUAKapntKBN9rEhrc0C5ixhnmnW2ogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغوش باز «شیرین‌سو» برای ۲۰۰ پرندۀ مسافر
🔹
تالاب شیرین‌سو در شهرستان کبودرآهنگ به‌دنبال بارش‌های زمستان و بهار دوباره آبگیری شد و جان تازه‌ای گرفت.
🔹
به لطف باران، بیش از ۲۰۰ پرندۀ مهاجر آبزی و کنارآبزی به این تالاب ۴۳ هکتاری بازگشته‌اند. حضور این پرندگان نشان‌دهنده بهبود شرایط زیست‌محیطی و افزایش ظرفیت زیستی این زیستگاه طبیعی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/442498" target="_blank">📅 07:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442497">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f9ddb167.mp4?token=bHv-UDRBSzED6o3_s-iNYH-VDbrtEqIAqKRI_z0uNyCED6wco4kxN7VHfXlB7cM8f-9Bn29C6phNRTMWt9KDFCwFy3TP_SBBImYie_Jm33GionXNNEk7UmMhO7mA2Son07UU4bq6GdMAN24qBRguI5JZDSMgG1VoiJ9wsrRqdZkfSBY07a_MIbzSOWyE5hdrYPTgXLWRD_hXAPAOLjigTxCmqkNQvGQmlFC-5hNahJihYcsu74VEIxemBc8H8SIcXzIN1Rbkh9jHC0TCFJMNxDImdPPIdkYStFbNWHgaNn_O3dCh0Es8Pu7Q0x7oWbcU6dQLXJgjrC-935DL7GpzFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f9ddb167.mp4?token=bHv-UDRBSzED6o3_s-iNYH-VDbrtEqIAqKRI_z0uNyCED6wco4kxN7VHfXlB7cM8f-9Bn29C6phNRTMWt9KDFCwFy3TP_SBBImYie_Jm33GionXNNEk7UmMhO7mA2Son07UU4bq6GdMAN24qBRguI5JZDSMgG1VoiJ9wsrRqdZkfSBY07a_MIbzSOWyE5hdrYPTgXLWRD_hXAPAOLjigTxCmqkNQvGQmlFC-5hNahJihYcsu74VEIxemBc8H8SIcXzIN1Rbkh9jHC0TCFJMNxDImdPPIdkYStFbNWHgaNn_O3dCh0Es8Pu7Q0x7oWbcU6dQLXJgjrC-935DL7GpzFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
میناب ۱۶۸ روی سکوهای ورزشگاه  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/442497" target="_blank">📅 07:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442496">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abq_CVJZaP8WB-lmCNZuzZM1tmJDd1vOT35GcVTrw8_pDaPru5GaXN3pohy4f2hV79499SZ83PrCvX-uf0t9158IeUEV0ybb7iI9WPf1lzG5ac1IR_ll33jnkUgAe5J6gkUif5dofNIZHmcC8yDPJOE0n9Z__puT4SaLrkFcondS91ypC_QoWHfPU91szltjbnoHC4yAXllcLHY94mqOy6gXwxP2iKz1oWD6RYyLb_inMgyocA69zXTifnkNAqDTSwvmWurCIk3_mimUORzyC2-UGlyYO53I_wvKb-Fs-jjCkiuAmqXIuMMWwSukPIB0UWH7PmKT2zcB-OVYhleYtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس داوری فارس: داور در اعلام خطای مهاجم ایران اشتباه کرد
🔹
حیدر سلمانی: در دقیقۀ ۶۷، داور به اشتباه خطای مهاجم ایران را روی دروازه‌بان نیوزلند اعلام کرد؛ دروازه‌بان با مدافع خودشان برخورد داشت.
🔗
شرح کامل تحلیل قضاوت داور بازی ایران و نیوزیلند را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/442496" target="_blank">📅 07:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442495">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تساوی یوزهای ایرانی در برابر نیوزیلند
⚽️
ایران ۲ - ۲ نیوزیلند  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/442495" target="_blank">📅 07:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442494">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627745dd75.mp4?token=np4l7tA7odNnuQ1YJj4UrQtbwwwkqdp62UsJLRvlymxinMlpqQfKxXVJvle1OCh0lzvcOR_zdxWYQkonHgahGRRWU_N2g_9iW7B_zu4kRHtv7od1hr0sQ6-rqeopo6AgB0M7Sr_Jn6dqOVOflLLURUjiHRHGBBnZBq6liwVsoBtZqSRbRKjFVcpzEz01UMa1YuoXvND8WLIb3wkEKCKDzJ_fhDibOJPXI0f3SIEaQEDEWKeU9fdYWjYn3KrUuODwiJacCy8zs1Cw4PuK-Rka8L3azEnmZFoPTkA2Zq81Rg131oPq5OPri9oIkOXbxCkcQgkDSI0qEDb8fNDEVz--UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627745dd75.mp4?token=np4l7tA7odNnuQ1YJj4UrQtbwwwkqdp62UsJLRvlymxinMlpqQfKxXVJvle1OCh0lzvcOR_zdxWYQkonHgahGRRWU_N2g_9iW7B_zu4kRHtv7od1hr0sQ6-rqeopo6AgB0M7Sr_Jn6dqOVOflLLURUjiHRHGBBnZBq6liwVsoBtZqSRbRKjFVcpzEz01UMa1YuoXvND8WLIb3wkEKCKDzJ_fhDibOJPXI0f3SIEaQEDEWKeU9fdYWjYn3KrUuODwiJacCy8zs1Cw4PuK-Rka8L3azEnmZFoPTkA2Zq81Rg131oPq5OPri9oIkOXbxCkcQgkDSI0qEDb8fNDEVz--UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: بازی خوبی کردیم اما از نتیجه راضی نیستم؛ شانس برد داشتیم.
🔹
باید زودتر می‌آمدیم که اجازه ندادند. سازگاری ما هنوز کامل نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/442494" target="_blank">📅 07:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442493">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4244f3cf92.mp4?token=ZfvNR4Bg2TRJYi4_yoAFCYUGR19E94LkwPKf8pEyDMtD6jfr3KCvgS4b2zrCJcXjkEa032X7ry6mcrBBZbGpRUzLy7VhdD8gG8Q-LPzgipKVbAf2H_xEGGc4ly61BhwFDtINvxkks-zfnwFC_2IESEx31WiVmhjHK2calSgcQngyhBhMp8-88wHQ41kZ89oEBURkQmE0Sjb04wLKTds9y-AjUGlXsvUiZdPjn0bnh-N_JrVEj-RwgSJxSvg7hlL58Bnr6hHTRP4l-Qd-R8SdrUl63DT_E8bWk5Trqg5PEqlG1U5kpgQjPLnOJcJA83FzdE2Egx5DMOa9-ZoQWm06GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4244f3cf92.mp4?token=ZfvNR4Bg2TRJYi4_yoAFCYUGR19E94LkwPKf8pEyDMtD6jfr3KCvgS4b2zrCJcXjkEa032X7ry6mcrBBZbGpRUzLy7VhdD8gG8Q-LPzgipKVbAf2H_xEGGc4ly61BhwFDtINvxkks-zfnwFC_2IESEx31WiVmhjHK2calSgcQngyhBhMp8-88wHQ41kZ89oEBURkQmE0Sjb04wLKTds9y-AjUGlXsvUiZdPjn0bnh-N_JrVEj-RwgSJxSvg7hlL58Bnr6hHTRP4l-Qd-R8SdrUl63DT_E8bWk5Trqg5PEqlG1U5kpgQjPLnOJcJA83FzdE2Egx5DMOa9-ZoQWm06GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
رامین رضاییان: بازی را خوب شروع کردیم اما گل غافلگیرکننده‌ای خوردیم.
🔹
بلژیک هم مساوی کرده، مطمئنم تا روز آخر می‌جنگیم و می‌توانیم نتیجۀ خوب بگیریم.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/442493" target="_blank">📅 06:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442492">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPgksAJvSnMn5acZu2-3ALmfueW1juPbCrrs3fqNveWlsbEtMqbkmeV4naIcMa5aOAOI878FrFPTAY5B4dcaRCJX_KHAK72KLAedqih_EJn1yl_Vqe2rUfHx3njqcovGmZFsIOC3XvABesy6RCrL3PsMHsY-flobD-ybzrxx9NCbYvrNE4JxIV0hjKZtHyBrwlRD91yt3mBDuCUrNEo4jDYi6m-LGo4edUredfcNTR1kqLb1i2Ajf0eqhfARuXxCL7GNDdkAD-z9iCSfzJQ1a59FtzlMSkTVZylHfqWoDAP5QoqoSDSooCpa1rE3pp9Xyx-4YJ4BMUiuHa9ltjDO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جدول گروه ایران در جام‌جهانی ۲۰۲۶؛ همه برابر
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/442492" target="_blank">📅 06:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442491">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKh3jByCPnLrhfcRy5wpqWRW_mwK0ddIfV0s4vucyZOp2n7m9WVXx9H4re38pIkmkq98UbDd7_0gabGjFEL7hsSbF71mGsM8R0Nx04wXKUYigtUJj-tm0XTEFC-ucE2kc6fMfMQe6njD5Zfnb6DK6o9pXvvKGtAjsGCVUqqfltNXrczcyl8HUbka8TWPiOlsaHiGaJKPq_2guPbL1CsIorRrPJPElBe6d_ueVvxK27zxghK1mY-0xfhyW5MxN5XOZia4zSXrHwHL69nvZC4oAhn4Rsn8_KIiQHNAZva53sl7Q8SpsW4ILF9K8x6JE079j5tdUgZhq5qyVNjkbbot8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تساوی یوزهای ایرانی در برابر نیوزیلند
⚽️
ایران ۲ - ۲ نیوزیلند  @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/442491" target="_blank">📅 06:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442490">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn5t6_p_Lz5HiyArQXVJ_F9g3whQxiHfzIQCUhpsT6ipLmSkX7Kah879zm0DhF-BWhYT1W9s60QAVm--PbpVe6LwiCvlgY8lYnrHjRV-juYsmGGACnp0Zm4TYYMBuKff8vJUyFePz0XIsamgjdeUy9j2wn4tPVF46MvlpkUrsij_2HkbbLB5Hf0e-HLSW1viCw7bsSMTE1plq8fJZv7no0zCf0psOfPSa7Ft5wXfrYJyECGiU6ISnYyIEBjrKDcdqnZudwv_RQ5xdfk4mA5Mc2JIHX0NBjdMF27MyVkbJQ6biVXCAn1ME6gQIKwq91KDjNo7tLozQlxdujeV6SCbYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تساوی یوزهای ایرانی در برابر نیوزیلند
⚽️
ایران ۲ - ۲ نیوزیلند
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/442490" target="_blank">📅 06:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442489">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb3f718a25.mp4?token=cXifyl9nIT9CIlnGtglfRukCnkO4Z2OVvFYH14QE8uv5XTvIuLvFkfUdNzTlREWzNGIkDnf_ST3bwcKoGVXA85gQ8a0MbEX3Y6Hrmj2K1kTqib95HC-Vc7mUtj7CdJXlHpcpGoidiGAGZ7P4gvAPDQx0UGFCxYqItGqxGBWBmcNqyp0vdvNM9B2XsO8jL4PIGuDE6sP3n5YaiM3t8h_HmrLuRKYsnf8P9Xm7X2_yKocN1vugoNpcGh3JECTkonoloyuGtxImkVKt68hatbNqb_myi3L6-TvPTz8ZujqbUbq5dlnpxkgu1rNpKAm4EryU-U5BfzslhAwdIlairXaUiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb3f718a25.mp4?token=cXifyl9nIT9CIlnGtglfRukCnkO4Z2OVvFYH14QE8uv5XTvIuLvFkfUdNzTlREWzNGIkDnf_ST3bwcKoGVXA85gQ8a0MbEX3Y6Hrmj2K1kTqib95HC-Vc7mUtj7CdJXlHpcpGoidiGAGZ7P4gvAPDQx0UGFCxYqItGqxGBWBmcNqyp0vdvNM9B2XsO8jL4PIGuDE6sP3n5YaiM3t8h_HmrLuRKYsnf8P9Xm7X2_yKocN1vugoNpcGh3JECTkonoloyuGtxImkVKt68hatbNqb_myi3L6-TvPTz8ZujqbUbq5dlnpxkgu1rNpKAm4EryU-U5BfzslhAwdIlairXaUiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت عجیب نعمتی در موقعیت گلزنی
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/442489" target="_blank">📅 06:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442485">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EoWlvk2IoRmucjhwBKO_BJiFUBdIA8eXUK1MmmDyGJOkeenc05FyeKOjiJFX5cXBTnP3WYBPjIgnL81QQhSXw-0W5qrCU3b3Cmr7zDgWHkvDcbCqPXAe8JOBWH2NEhTbTkS1LUcE5r0hKDkwH1f9_9y-nAewzKIapBDXPgfLd7i0C5o7ilhj-2xluAhlDVGUuhoSKWqcy00i6cipH2SsybsMpPNQHBeLlSdJNpcEegAM8SE_pdsj-xcvCL4trBn0Tbf4bjPSZGv-H267O_WukXomrPJGzMk2mIBRINVMLse9r8HxIm4WaiMgkkGRA10TQcIdB8z_7QrgdUdy1J2R_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3hm9bqnUP47nwtVrxeIQp1pCJrRdQ57COBnanyP--JPDLFwgmUopy2Sr-s-PXUacCziQ16al66QwcUdciI9fNSQdTSQx0OL1nCxvolazalxraGCvfTVRd3lnF2s-nCVPctVkWOAaIqrLQGwBue1ziufuFR0VjoYnD57uExO80WzlbxONv7qKmyku19tOFKJjvEzsMLi06KBCpyjxrLezIArDndu9F4P-Aev95U8fAEnqDz6aR0g0aIcD05Dim3AauCzmiTGyDMah2vmJZFCG0NnGV_VyD8kTuFWB5h92mW_YXh281qJCLdsJX87xsxslrMHS0BJXNJ1_LuVvtF_qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k4NPRWyn27vgWBfE6n5XOoT38yd608J3EmsKBOOtJhV0Ucfpkl0syCxGgs9NTK9OeBtBUQdqJ6duvIxAQmvlXnegmktKoTgZYufrxHsLwhtNM4fvdCdcQJ_pJ3nDWi6CMBKwIxrJ7BQ97Uf2GM_NNzi3R7zKjy1I6v5CAoUW_EKpoSxbZQjT5msWT59r_qbiTEpOmvM4GQTb__ed2i_lPu_cb0r-BZm4rElYmNOKC3wDklJLWeP0IRWGuaiPLgzhKdnsEccZjfkFwdAuaui_GbRATph7XgHCQbm3pXdVOFhRO6_qB6mcUpjjbx13VHdN9P-nO3HYOv5Sdb89RgwHOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dUpELcDtckjhmTX2S4M8anltbYk8v2uPWXB5go_DLP0fNTs5H1kKUF834YMYJ0rmt5gwRk1-FTrk60pUisEYUoqc3Cko2I1BB4rFOFPHn6ZdAF74J638mePOG15j_1ETWvv1muVSRy3i5xQ9rXmHU_7SaDfs5bVb0HK3H-4nEgetcXqMvn2Jp7PVBknxhNSg--9hP9DRnmc8inxiA6UJANmFqaZURZlE1a_pa53lbdXS611c5Ad5kQWdOtBdtdpKX54Gi4Jyi3HSvj8L69ScV_6lX_e8faExFgaqprJc_VrLIiTqzC45-8k6f4fWgtFIlfX8Fx7KzeRfi4ECHanHgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
گل دوم ایران در دقیقۀ ۶۳ توسط محمد محبی
⚽️
ایران ۲ - نیوزیلند ۲ @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/442485" target="_blank">📅 06:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442484">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚽️
امیرحسین حسین‌زاده به‌جای مهدی طارمی وارد زمین شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/442484" target="_blank">📅 06:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442482">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚽️
احسان حاج‌صفی به‌جای سامان قدوس وارد زمین شد
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/442482" target="_blank">📅 06:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442481">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76ef17530.mp4?token=riFytAakrY5g0pVzeN7PoHLt46U1a2p61pBzyqMF45HwVJnZgEVt2avtT7UNBLb09Nh58copwvi6NxHZtbQgWktCKWCI0gT5QSdxB2ZV9RG_UKa-MACKb3xctJgKot7QOS3k8vhdDo1WAM-caeRTNBSzWY_oz7GG1qaq1zY30rIFA2OGynwU9AlTWxkO99a2MpmEhoVLA7SZYajnn5Q0Xnw_L6u63gnsgyD94_OblqMDNl-sOMIrQW7FVikxwPL1oFt8ECCc9UZMRXXSlQbEjeZ7oMvzFDQkgQNj8mzjuaOQKj73TtIQsWw_oi9B2xwaDvjxcRZuDJoFBZFMZvZqvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76ef17530.mp4?token=riFytAakrY5g0pVzeN7PoHLt46U1a2p61pBzyqMF45HwVJnZgEVt2avtT7UNBLb09Nh58copwvi6NxHZtbQgWktCKWCI0gT5QSdxB2ZV9RG_UKa-MACKb3xctJgKot7QOS3k8vhdDo1WAM-caeRTNBSzWY_oz7GG1qaq1zY30rIFA2OGynwU9AlTWxkO99a2MpmEhoVLA7SZYajnn5Q0Xnw_L6u63gnsgyD94_OblqMDNl-sOMIrQW7FVikxwPL1oFt8ECCc9UZMRXXSlQbEjeZ7oMvzFDQkgQNj8mzjuaOQKj73TtIQsWw_oi9B2xwaDvjxcRZuDJoFBZFMZvZqvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم ایران در دقیقۀ ۶۳ توسط محمد محبی
⚽️
ایران ۲ - نیوزیلند ۲
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/442481" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442480">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3VAuSBL5_KrBMl1HL6YHIHW9qbCqRjLIQoWVedq6XN5BjK7UJmqQjt_xFQo_DoXTY0yBnO_nRNbLLOTZn9IfG2JAvI37njeQ-hrlaGot3UoP0eF97bfBgH2guct4ywt1JuFzIBEGu-_poGE7KaA8rN7u1LkEWBCwyKg6stKA8A0GkukQee8paoawjTaXCR8qCcgsn4txSscnVXc4qWRn2C49vBJg5a3sp6a0sqWwh4qH4fDOnQfzQUxzQARnrsePEKnZp3QnUS6BhSHrdfuZdhocOfRvYikkXurUMyrd6zLp7Pobk2qgjCgLw6E-ubnO32pkxezojqsR6qhq8Kizg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
میناب ۱۶۸ روی سکوهای ورزشگاه
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/442480" target="_blank">📅 05:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442479">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ff7336c5.mp4?token=YGuAR3EeRUvWOK8Ze_tgAfeLSFESQTt3BQxPGa7JifjD0QBJ2Bozn4CMHaz9_9QPzboJzDuV70zFQ99d6FngrLstmwP4Ef4YPuFNX9AP7f4PPZx0T8HFiIAScVDULYXfL_M8yCuoZWmrEdvx7dZMoVC8Yt0YWL-0z73aqwfZhj3ju9tcQODclWR4oay4lmdnX3-niS_OVOhlHFIUm1Y4OzX7fm3FjK3G-vxKilO4tnGKTUFxnpbrmLlM3npcGFLOeoYqzDFkzUuFiAfPuPTag3VctByUyrREE_wGlcq5JUFSgNiQB1rwZcBDf8Rc2mbJbFg4oY1AH6XjmroVKEX8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ff7336c5.mp4?token=YGuAR3EeRUvWOK8Ze_tgAfeLSFESQTt3BQxPGa7JifjD0QBJ2Bozn4CMHaz9_9QPzboJzDuV70zFQ99d6FngrLstmwP4Ef4YPuFNX9AP7f4PPZx0T8HFiIAScVDULYXfL_M8yCuoZWmrEdvx7dZMoVC8Yt0YWL-0z73aqwfZhj3ju9tcQODclWR4oay4lmdnX3-niS_OVOhlHFIUm1Y4OzX7fm3FjK3G-vxKilO4tnGKTUFxnpbrmLlM3npcGFLOeoYqzDFkzUuFiAfPuPTag3VctByUyrREE_wGlcq5JUFSgNiQB1rwZcBDf8Rc2mbJbFg4oY1AH6XjmroVKEX8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم برای نیوزیلند در دقیقۀ ۵۴
⚽️
ایران ۱ - نیوزیلند ۲
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442479" target="_blank">📅 05:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442478">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7c11d9c7.mp4?token=irX3OLXiBWleH4riAt29SosG95S7kbhqlpjCmjPytqhWtp7hziyU1Yt4zwg5sXDO4wX-jlSFYky581vy4jJlZumRM-qEooVNqs-pEK31J1PLNha8rCmuKrZasFcoEZKdOAsoft8o1R3PGIrzW3jDPEFvQ_DOdsFikNRnxCKXJazhTKu4fh7BzApjBa36YXpZGVb_2Is1rSI09QiokQrRV-HlxdOSWOI7A-whzPQFRrhmMy46AScTbQsldd8ce4XUh24u9nT4a3ECgFGtMHjYkMxpNBtVgW__KE4J5GNd2mU8SP9sZd18JkXvVJeG75aPuJryfYswpdjWDEH4SfkAgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7c11d9c7.mp4?token=irX3OLXiBWleH4riAt29SosG95S7kbhqlpjCmjPytqhWtp7hziyU1Yt4zwg5sXDO4wX-jlSFYky581vy4jJlZumRM-qEooVNqs-pEK31J1PLNha8rCmuKrZasFcoEZKdOAsoft8o1R3PGIrzW3jDPEFvQ_DOdsFikNRnxCKXJazhTKu4fh7BzApjBa36YXpZGVb_2Is1rSI09QiokQrRV-HlxdOSWOI7A-whzPQFRrhmMy46AScTbQsldd8ce4XUh24u9nT4a3ECgFGtMHjYkMxpNBtVgW__KE4J5GNd2mU8SP9sZd18JkXvVJeG75aPuJryfYswpdjWDEH4SfkAgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربۀ مغانلو از بالای دروازه به بیرون رفت  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/442478" target="_blank">📅 05:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442477">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad3fbf9d9.mp4?token=jExerjtZmHMPDdqsKqJyWF8P5aYKKiy8QrlRG2pzILAgL88O6UVc3PBQNTKSZ6nfdojWC0FnJssKJHKMUZDoxg_RRe3UuX-6zxsvbbGAZVYWBPqL90aHo-XrMeikBC9X-8qowWNxOfyA2vruy8ZcnXyTZRwI6Z0q4bIgP7Ds_hfwmqMcaMqTesiLM-j6TeRFoLcN6TBPQraUpAyjdPxn4VtebqF9GynYyd5Z0VHlD9xlS7Pz29DWYxVL8Oi8iLtjGi602hrmgfNO2RYMFwjb0PQK8_Djm8Az79JRhcz0CkdHcKHKir3WTMpUj2eJCs-D6fA87X82LY5vqqgTf6gg-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad3fbf9d9.mp4?token=jExerjtZmHMPDdqsKqJyWF8P5aYKKiy8QrlRG2pzILAgL88O6UVc3PBQNTKSZ6nfdojWC0FnJssKJHKMUZDoxg_RRe3UuX-6zxsvbbGAZVYWBPqL90aHo-XrMeikBC9X-8qowWNxOfyA2vruy8ZcnXyTZRwI6Z0q4bIgP7Ds_hfwmqMcaMqTesiLM-j6TeRFoLcN6TBPQraUpAyjdPxn4VtebqF9GynYyd5Z0VHlD9xlS7Pz29DWYxVL8Oi8iLtjGi602hrmgfNO2RYMFwjb0PQK8_Djm8Az79JRhcz0CkdHcKHKir3WTMpUj2eJCs-D6fA87X82LY5vqqgTf6gg-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربۀ مغانلو از بالای دروازه به بیرون رفت
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/442477" target="_blank">📅 05:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442476">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9a562a209.mp4?token=rh6_t6P9NzKlziumCo8zQbyoHgGBssN9uGt3ZSckvmeU7uBClmJ-zNMK30Df2vsy3ILnSFnKnvrHmaQPce8OEG78mf2WRUkW9tlIX4dc0WiBe9pv51EfDxcO0H01ONxWPGtZjTFbAmdTwuH6gyrnbgmwnU7cNwvUV82GdV3luKulZCkn-I_erqXriRLDItpOnPkp5g7oavcbBecsSb0UFWKcbu8ImoifBaSUvtHpCHDc2-y7uEUlaYTl0ftCd0ZYJdUYBvVF1U6GXriWjUcEBSeoAzqD53dQmFPTZ_kAIIYCH67Du_ja7uDTghYg-o7-Wxr6OMFFKJYm_DqxIJxg8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9a562a209.mp4?token=rh6_t6P9NzKlziumCo8zQbyoHgGBssN9uGt3ZSckvmeU7uBClmJ-zNMK30Df2vsy3ILnSFnKnvrHmaQPce8OEG78mf2WRUkW9tlIX4dc0WiBe9pv51EfDxcO0H01ONxWPGtZjTFbAmdTwuH6gyrnbgmwnU7cNwvUV82GdV3luKulZCkn-I_erqXriRLDItpOnPkp5g7oavcbBecsSb0UFWKcbu8ImoifBaSUvtHpCHDc2-y7uEUlaYTl0ftCd0ZYJdUYBvVF1U6GXriWjUcEBSeoAzqD53dQmFPTZ_kAIIYCH67Du_ja7uDTghYg-o7-Wxr6OMFFKJYm_DqxIJxg8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در شروع نیمۀدوم، مهدی قایدی جای آریا یوسفی را گرفت
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/442476" target="_blank">📅 05:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442475">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/719b90c3d6.mp4?token=HoYkh8t8IT1WQND7XG8f1lbI66CMG7F_KL2undE9QfPon4PDWhKxF9K3pb0UGdcubHAmz0xZQUVl3GLCoGs9cizwXSHaydYgoGBx6ZjViKL3sgbGxABjtp0yg_kXRHTAmKAeGqExq3UhZ2hKcv2541VTSW-rsNp154qUEIrYA71ca8qmf5bEl2kSg_00qvlHOzRdjQSBFw0a8-0P2Qx637YL8WLvub4VyMxYqBifodahnpWvJD6xAlJiIbJXwb-zG68maNx5gq8_89MD_ujNjQb8m_0uo3JgVtOvsT7pocsjszTZCPP6cDpPNltE38Apb9E_Z53gQTWwoQbbEEovFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/719b90c3d6.mp4?token=HoYkh8t8IT1WQND7XG8f1lbI66CMG7F_KL2undE9QfPon4PDWhKxF9K3pb0UGdcubHAmz0xZQUVl3GLCoGs9cizwXSHaydYgoGBx6ZjViKL3sgbGxABjtp0yg_kXRHTAmKAeGqExq3UhZ2hKcv2541VTSW-rsNp154qUEIrYA71ca8qmf5bEl2kSg_00qvlHOzRdjQSBFw0a8-0P2Qx637YL8WLvub4VyMxYqBifodahnpWvJD6xAlJiIbJXwb-zG68maNx5gq8_89MD_ujNjQb8m_0uo3JgVtOvsT7pocsjszTZCPP6cDpPNltE38Apb9E_Z53gQTWwoQbbEEovFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد ایران ایران هواداران در ورزشگاه سوفای لس‌آنجلس
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/442475" target="_blank">📅 05:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442474">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bf7284b1.mp4?token=a6h6oDDkcG7pLj6RvOQBF_s2mYH96Lvvfwi3am7KK3L0x5enp6rC6-_5znYMgS2LbOUkKwYr2ZjysmqNI9n8mDR6Y1ivWKU6bXMosohVWAqpfdFnpPHSbWXsvWUdYt1PiD_EpEpGJCLfHzeseufN8DKsxzd_cXXLRS7RpYlcHDOKWRFvYkPEdbKdNzniyQUNq9_vCDAXtQ4xki3d03dTWkFPnScmVFahItMVJbe_5zDTYFNG8B0MZddgj_fysOVM-ZG1tWfrZ0GcD5hB5M35Gy8dVkbnLC_OB6NZFkY_qSj1EJoz5ldRkJdV6KIP2iT_LqhGfY9eDQBD2G4UWLp4NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bf7284b1.mp4?token=a6h6oDDkcG7pLj6RvOQBF_s2mYH96Lvvfwi3am7KK3L0x5enp6rC6-_5znYMgS2LbOUkKwYr2ZjysmqNI9n8mDR6Y1ivWKU6bXMosohVWAqpfdFnpPHSbWXsvWUdYt1PiD_EpEpGJCLfHzeseufN8DKsxzd_cXXLRS7RpYlcHDOKWRFvYkPEdbKdNzniyQUNq9_vCDAXtQ4xki3d03dTWkFPnScmVFahItMVJbe_5zDTYFNG8B0MZddgj_fysOVM-ZG1tWfrZ0GcD5hB5M35Gy8dVkbnLC_OB6NZFkY_qSj1EJoz5ldRkJdV6KIP2iT_LqhGfY9eDQBD2G4UWLp4NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر شهید مدرسۀ میناب در دستان تماشاگر ایرانی
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/442474" target="_blank">📅 05:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442473">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c43df35bb.mp4?token=Ui3xir67tH9ElokdLQ_z3gF9UXzJ-4EE0VmJsuk1TgA5O7ZYomzD2hECvQHSoRi_MjyxXfcxXqwANEptjhPlWz1JaCTMEg8Zb6IvRpINryUgIj84FzHluopo9-bYAIWN9fUfR9sG3SC-Xk_VACp6vKzzmGZB9EyLhxEyl3oQ6u-N1ouX2d9LWGJznvy4MqcJFDH5dSrw5W8CqjxzPw1SeXdZCcrnZ_aJTS-So1hWNRzQEJtNVo7mBLcyJMnZZDU8Z_bevJ1OaNgIsxZt05WsjcrPUyq245Vnwtn97FqqR8MFXZbv-YLk7pHEn_SgQU8EWYILB1P5izLTB9BS2tm8Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c43df35bb.mp4?token=Ui3xir67tH9ElokdLQ_z3gF9UXzJ-4EE0VmJsuk1TgA5O7ZYomzD2hECvQHSoRi_MjyxXfcxXqwANEptjhPlWz1JaCTMEg8Zb6IvRpINryUgIj84FzHluopo9-bYAIWN9fUfR9sG3SC-Xk_VACp6vKzzmGZB9EyLhxEyl3oQ6u-N1ouX2d9LWGJznvy4MqcJFDH5dSrw5W8CqjxzPw1SeXdZCcrnZ_aJTS-So1hWNRzQEJtNVo7mBLcyJMnZZDU8Z_bevJ1OaNgIsxZt05WsjcrPUyq245Vnwtn97FqqR8MFXZbv-YLk7pHEn_SgQU8EWYILB1P5izLTB9BS2tm8Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل دوم ایران در دقیقۀ ۵+۴۵ که آفساید اعلام شد
.
⚽️
پایان نیمۀ اول؛ ایران ۱ - ۱ نیوزیلند
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/442473" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442467">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-WbOIwGQIWaZYYCnu85YBoGIxey75J-poSmi2l7goEfFLRUfpF8nhNl64A2RU0AmdLFfd3z-HK5a1lSVTZBjkQqRiXlv0D_xF1lbkNxIVV6T73fUv2HZr53gTkCcpc-ZFDF_2hDNm8CekMTG7QxY9tUfF67kMJ5uk1nsgtPw5I23GC5h7S3lz8nefFFjvTXTcWYCATOWvuhKVS_PyEie23cnADteqeeeKwxvoy2A5GkLsBVg5GhXb5kw0Ug5wBe-1gbImGOwN27vWEt2GEYFxhVl0tQtEp6h6o0cxOl-CKVUazIJByfuzL9w9NI4_6Sg8qgznio5kwEWv6fHG9bww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V04P-N6MzLbz4wP3wG2F9j83KCTJk3CIKVZcjDqK_7BKhNldwg3B8x_pWIVQmT-n8-bGHST-FijE8yGTvF4MV_37swB8g-8KeZp9yXtdPysjXtuZRp_bItnSGZ-8xWWjhc_mwqvibZc1eVhZQbomPKMGD2hVJslRVrjcD0GHyPZK5QBkQV6x7MT97mf2cfbc4usM7_R9M8RR0kC7MORyCgPEYCZIMYaP5b_dYrP5DrAavF9BXCXQKKXNf_YMb-d-Q41tKNYkbH1eC4yvd9VWo1xptTOU7jzTUAlXSz8kF_Z_jdSvDmQaVujYs2xu3we0jjDPkaGz0JaUbSOJTIi4EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KymhPAoW1jlHPakU_LCtIih9_ogUCm0-pxkwmZe4drZx_kOOQZFnHOQrCQHXCP078X6C-56h701FNEXbrA25mz1CZ6zM-YV-lgpne1pS5Bwvo6C8uKjwOOqWHQRlsPdjA8duoMrIE3TurO1rnsxMjXi_Idu995PgBvx7C-Mk3PI1XwxVkUQAHmznrS5bZatdfZz7vtujmqM1rF-3iEG9j_tcOhalSl7KkK-eIehHnxpz3_W87TD0JXWo1G2tvNKz6nG_Bbo1Fl1hODzwwFdItgKoN22W5Ne7rlUK5rHf3yel_K7feJXyc5MSMuV1OuxxoBw4-lFM16N0PBoK-6tf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iECFVrTV69lgZiuizYI9HoqFGDiRvMi-LE0lucqWHuDk0Ao_lrgwFkkgd7Wk8a3hA3Sr2CCawOt-ZIY-_WIDGRHKe4ZdMCI2eDCn1R3XYmmiE4N6fI6SH3EAIfJkYoZY7BXdIatlrhAyn6TFqvF6I-V84hXpjKRaVgAggvcdUgIOoz3yrJ0aOstZzTnJmw9thyU1xjmaivMJt1QLVDAn55QyWUB_NQznFTDa1XCNpAnjFycW_NRyadPivTuay262dabbw923EPEKUs7r16wMgdW_t_rjFjtWu9aUp08SWLgbuSyrO8UKwTvzS44Sw4jUxXer6DBhTqxPAdi4igJi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PwNwMfbv8IUmtDFmevxYLaO623Etrx6wc6KGre6IhsSqzcps2-Wh7WQEAJ2KCjWZobGDLSL6FgcB3cG1SBLRldC-LXPH3WGu_671MzkdZTMoRjFKC1o6EMZytiDQujJzVa4_VtRU_VTUfVwIKUkS_zBBXyKST1e0SbS8ib7wSsOc4hB5UH7NHHBUPb78gHlf9UPP1iyr0_Dok1g9QTefR4HLIYat2bfZasSsO4wRqwymXIRZeJnIgYuGdl1NmD0zxXaklGw22_2AbZAgwK-Iu8MIZkhBMVytExx95es4sBb95xWwrvl8CRy7LYvYHQ_ofWGUGBAAQKFpjsFCO7PAOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuiKcH3cleppzlMfiMIyqEr5ckHq1F-dhzogwj5uZtlSoCZFDUH3-yvW2rqZdcn2LA4UPxmdzV2yu4i8JXOAW1jrDYQP8w-TBnnAJ5nopz55HwGZrcn1BflQEQFD2Y1anG-lahs35dW5XH-Xrug8gd7CytHwtgzHB2oy7-nO3ymgijwCEHnOANeDTwqUBFsrIHG6q0HdnzivlRzkLNDNn1mEHruhi5dKw03RiGkKiLNXGuPMWuWAcDAMIRasoQIY2zqgg5_IOee4oVsKLZitQvBUfGLp08feyX2bAySZwC-yQltKcehfEB3__R4EpIbmf4rjpiMeKCd95rjHUZiSUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شادی بازیکنان تیم ملی پس از گل اول ایران
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/442467" target="_blank">📅 05:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442466">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ccac3f33.mp4?token=tcj-6MSn7qtPyq7AxQbXQQvrto50iGEmWmNHy7yphm77LmGfhnMd1TxOQThpyLxb5nwSfYO-loqc03qMIjHLzWwnJXUb0jAnAA123indM38V2fj7qm4bKnu5R31NYr4DcQUXYyz01CSDxRpnoLS5A7JI-xpMDrVtpplOwYhX8iNcrE24t8JPM3kfp9koAMxPjUqp5vKpQDLU_3BkBD1N8k0D8sYet2NoHQeZStxbw-3gBKxOwScr7xAfxBDIEqwvuedDKSWQIhtzmxID0DOzg-SYOwcJzsHSfKhf3NbNkDiucsyxPr04A3bKIfUcAFFyFYCyzyPBYVLBXQ7iA9qaRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ccac3f33.mp4?token=tcj-6MSn7qtPyq7AxQbXQQvrto50iGEmWmNHy7yphm77LmGfhnMd1TxOQThpyLxb5nwSfYO-loqc03qMIjHLzWwnJXUb0jAnAA123indM38V2fj7qm4bKnu5R31NYr4DcQUXYyz01CSDxRpnoLS5A7JI-xpMDrVtpplOwYhX8iNcrE24t8JPM3kfp9koAMxPjUqp5vKpQDLU_3BkBD1N8k0D8sYet2NoHQeZStxbw-3gBKxOwScr7xAfxBDIEqwvuedDKSWQIhtzmxID0DOzg-SYOwcJzsHSfKhf3NbNkDiucsyxPr04A3bKIfUcAFFyFYCyzyPBYVLBXQ7iA9qaRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول ایران توسط رامین رضاییان در دقیقۀ ۳۲
⚽️
ایران ۱ - ۱ نیوزیلند   @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/442466" target="_blank">📅 05:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442464">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f08a530a.mp4?token=N97s_iv0HMM7GeUS0Had91wpASzJtqHufHRi34Xre_uhKVbvAFoohhEaV-KxYiohmqAjamQL8Od9b0AbhkhfrLKZSGOkfGgqCpeDXRUFbfOIwmod6UsO86koZfdAfHBJ6Su37CtIxRRHoUEVjHo7A2MMQVr43WC4b6lgFl4WEhumPLI2xvtE2JI5Mg8CXJRGL77OvOS_UTtvhPFcic32QN3JbVhHQQhoy5XQhcCGoDvOnyxto5agZumA_UT6KMm34CuunKEok459Sf8KYOSjX4ecmJjQMxNfdYzA-FuUQvqSMK4lKksFUawBAJnh4X592THKvsUbB_7shbZGi7kjlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f08a530a.mp4?token=N97s_iv0HMM7GeUS0Had91wpASzJtqHufHRi34Xre_uhKVbvAFoohhEaV-KxYiohmqAjamQL8Od9b0AbhkhfrLKZSGOkfGgqCpeDXRUFbfOIwmod6UsO86koZfdAfHBJ6Su37CtIxRRHoUEVjHo7A2MMQVr43WC4b6lgFl4WEhumPLI2xvtE2JI5Mg8CXJRGL77OvOS_UTtvhPFcic32QN3JbVhHQQhoy5XQhcCGoDvOnyxto5agZumA_UT6KMm34CuunKEok459Sf8KYOSjX4ecmJjQMxNfdYzA-FuUQvqSMK4lKksFUawBAJnh4X592THKvsUbB_7shbZGi7kjlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول ایران توسط رامین رضاییان در دقیقۀ ۳۲
⚽️
ایران ۱ - ۱ نیوزیلند
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/442464" target="_blank">📅 05:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442463">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8c3438698.mp4?token=ZSZ1DpKxkDw1raJV7ww911KjESzA2ldACwE6YOwWwmCW6x-nNjHpPAJM4RmNSFQDXehujmkbmCnXv7rWwCq8j1i_YjtvvYaF4j_U7_djIo_w3r6zgRLfv_qgNwEroyb_2aykRePI-GtSE4RugMByA32T9bIz2n21ptdQgH7PdkkJnLr1Jt2yI4TCtFHoFHCtgpBXh9PQSw69ZOYApq4JKaenYGgk1Trx8Ioxy6HBGOGQoov3nWRL8fa7aspM5tx58UhP36YyQxgHow1HhK0H6pMFkpMqrBlH0rHH7qL8MiW7vTMUog93Xo1NxYfBOCRqEdB9LafWskpH2So_rL9SxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8c3438698.mp4?token=ZSZ1DpKxkDw1raJV7ww911KjESzA2ldACwE6YOwWwmCW6x-nNjHpPAJM4RmNSFQDXehujmkbmCnXv7rWwCq8j1i_YjtvvYaF4j_U7_djIo_w3r6zgRLfv_qgNwEroyb_2aykRePI-GtSE4RugMByA32T9bIz2n21ptdQgH7PdkkJnLr1Jt2yI4TCtFHoFHCtgpBXh9PQSw69ZOYApq4JKaenYGgk1Trx8Ioxy6HBGOGQoov3nWRL8fa7aspM5tx58UhP36YyQxgHow1HhK0H6pMFkpMqrBlH0rHH7qL8MiW7vTMUog93Xo1NxYfBOCRqEdB9LafWskpH2So_rL9SxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحنۀ برخورد مدافع نیوزیلندی با مغانلو، که داور دستور به ادامه بازی داد
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/442463" target="_blank">📅 05:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442461">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259f717fd2.mp4?token=YNHTYyVNpikkUZHdhPeONsxgHSsOaZ2x4cOmzWqE6JZ1tKWTNfFeNxcN_iLXcsMpa-OhMsyMAZLB4Bh9xQRc316OtGmjiPRitUooyW3hLKqbzAGyhk701XF6-nQaYq-nAyiuevUsO3DpgJoG1Yyur33k4yTO2Gr_uOOn2GDwXq1my3nCzWlOFld2Gl8UWr0F8Kk_gGS01OWTogyZ84rbygX0Pmy3pQ3IKBzTii9_0BY6q8ZQOQGWqOQkqaT3434M6Zmu0150qYxXfCFAzCqHs9n96P2Sxg2FvpRFyX10O7cSIgkp8-E93OgjUL1wRdy3ezXeiIB0lbbsX_41JKTxwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259f717fd2.mp4?token=YNHTYyVNpikkUZHdhPeONsxgHSsOaZ2x4cOmzWqE6JZ1tKWTNfFeNxcN_iLXcsMpa-OhMsyMAZLB4Bh9xQRc316OtGmjiPRitUooyW3hLKqbzAGyhk701XF6-nQaYq-nAyiuevUsO3DpgJoG1Yyur33k4yTO2Gr_uOOn2GDwXq1my3nCzWlOFld2Gl8UWr0F8Kk_gGS01OWTogyZ84rbygX0Pmy3pQ3IKBzTii9_0BY6q8ZQOQGWqOQkqaT3434M6Zmu0150qYxXfCFAzCqHs9n96P2Sxg2FvpRFyX10O7cSIgkp8-E93OgjUL1wRdy3ezXeiIB0lbbsX_41JKTxwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت طارمی به تیر دروازهٔ نیوزیلند خورد و گل نشد
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/442461" target="_blank">📅 04:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442459">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc9656da9.mp4?token=cA8rh1UZTqyu6eJVyJBR4DerDXPgbymDfXtj9FqSanry9JesEaDOtTZhSUEplu8C9yA6f87_4jULmhhSnhpBWL6ADWcZ6MRL3hduI8F8ahzRLgRFHq31w3pGJ1l6AeB5DqcXQFy-x9X5BTraz66X6SnUXPdsnaiZOtoba6HXK4pEUdO8zgwr0JDXNEvDIPKk1uFpLCNlGu10M4q1naWCnMYcsb-xHiBsFUhjsysDjGGL7gsEsLE1MVghtFxX9KPDGT_M5c6smJuvQPMgA6yhWlr0oE91Ef638zSfOmTgSPar3aLsns7nZOEe98Oyw-Zv7Y9p7b3UGzTCKL2f3LHzCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc9656da9.mp4?token=cA8rh1UZTqyu6eJVyJBR4DerDXPgbymDfXtj9FqSanry9JesEaDOtTZhSUEplu8C9yA6f87_4jULmhhSnhpBWL6ADWcZ6MRL3hduI8F8ahzRLgRFHq31w3pGJ1l6AeB5DqcXQFy-x9X5BTraz66X6SnUXPdsnaiZOtoba6HXK4pEUdO8zgwr0JDXNEvDIPKk1uFpLCNlGu10M4q1naWCnMYcsb-xHiBsFUhjsysDjGGL7gsEsLE1MVghtFxX9KPDGT_M5c6smJuvQPMgA6yhWlr0oE91Ef638zSfOmTgSPar3aLsns7nZOEe98Oyw-Zv7Y9p7b3UGzTCKL2f3LHzCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند ضربۀ بازیکن نیوزیلند را در دو ضرب مهار کرد
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/442459" target="_blank">📅 04:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442458">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba11b250.mp4?token=V31Q6wDp7_nUoO-5WOkdEhlMIi5mCBTkXbHYjShRGsuxJp4MSZCcPKJ_D5pNrSaXzgof6XEKzqEzW0IJwEHKMGYzZ5QbkgKpkfwnaTF5QJaBCD8i2Qsj1hd-YvQ5RHGVxXL2rC0_Xq4ZV-xEAwjpIfga4rv4_CLKmBAgufMjuh_jI22YPUorjGWe4ami4TbJtTfzY9_u2kdcVpfWMb-I4SgH_zlqoS3svn7VCZ3JLNr9EkZ8zVA7e9AuuoHGtN62YGBtco1_l4H8ALmWdlUpWjliHSsUrMnZ9tLREe0wT1Z6579fMptMpkGVZgJn6S_7QEtLPIk49vSaEiZadi6ySA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba11b250.mp4?token=V31Q6wDp7_nUoO-5WOkdEhlMIi5mCBTkXbHYjShRGsuxJp4MSZCcPKJ_D5pNrSaXzgof6XEKzqEzW0IJwEHKMGYzZ5QbkgKpkfwnaTF5QJaBCD8i2Qsj1hd-YvQ5RHGVxXL2rC0_Xq4ZV-xEAwjpIfga4rv4_CLKmBAgufMjuh_jI22YPUorjGWe4ami4TbJtTfzY9_u2kdcVpfWMb-I4SgH_zlqoS3svn7VCZ3JLNr9EkZ8zVA7e9AuuoHGtN62YGBtco1_l4H8ALmWdlUpWjliHSsUrMnZ9tLREe0wT1Z6579fMptMpkGVZgJn6S_7QEtLPIk49vSaEiZadi6ySA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکل عالی مغانلو مانع گلزنی وود شد
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442458" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442457">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/666ec3016b.mp4?token=fimf8DTCKZdzmm_zXC_SHiAMXmq6in1VEhDnz9ZFYm7UhlE3I7_MdG1SRIkpE_tvRvWU3gThUJ_hlehyJ33BdtHDjNtRdvPs1RHl9lF7N4NmrJwIh65tidbupRxsQIaBHu0gIRdKLie1wpVR7n5A3ycPmuT6tra0wuHbhOlccvMkMRZOo2SDF-BuHB-78hzXCUtfgoHOCL34gC0uzrUG_7fC57XO36TJJoUVUIkkiVpN7M8DubX6wswUdG-1Rs9VepQCUX0z3uGleIGJZBIkdJz1i_d_ZwrSJVoB01q3vPCy8082NNREk7Tac1GiyaHlSYtgOWcgwhgjrQAOa0hdmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/666ec3016b.mp4?token=fimf8DTCKZdzmm_zXC_SHiAMXmq6in1VEhDnz9ZFYm7UhlE3I7_MdG1SRIkpE_tvRvWU3gThUJ_hlehyJ33BdtHDjNtRdvPs1RHl9lF7N4NmrJwIh65tidbupRxsQIaBHu0gIRdKLie1wpVR7n5A3ycPmuT6tra0wuHbhOlccvMkMRZOo2SDF-BuHB-78hzXCUtfgoHOCL34gC0uzrUG_7fC57XO36TJJoUVUIkkiVpN7M8DubX6wswUdG-1Rs9VepQCUX0z3uGleIGJZBIkdJz1i_d_ZwrSJVoB01q3vPCy8082NNREk7Tac1GiyaHlSYtgOWcgwhgjrQAOa0hdmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول نیوزیلند به ایران در دقیقهٔ ۷
⚽️
ایران ۰ - ۱ نیوزیلند
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442457" target="_blank">📅 04:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442456">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d8601fda.mp4?token=gw93yHaU7h_tfmRegjZLjO7XnIWR04Skx1LJ1aB7n99oOXwEj657d-VYY9CiG1QYprzjRowTkk3a-NcjTLfwEFqLmn9jH7RfFmrkmSuBckf4GxWkU9ypsg_bLZLKWz9HEmA6AV9SmGmAKHoAD7XDWrdeJ64ptTzSbwz_WN5BeqBEsbBvA85cDECkSQR7lJ4cZbyPqngRTY-S5fytgrMrrnzC84WZ-aVPNb5XNJvalKno59R9YqvAryOUR0-ZQOyC2kkIFBak3GoZ7uo6FrEtF2lAao2pL-ffltlo0uqdB3q1X_LyMPbelE9uqNnMXcO4GJdxAhQLjiHXAPNUxxF70BnwLTDV8pUQtv9NF_NpARilDYvKJXG19M3p7wiZIGasrmvb8JlC_NRvSkxnhLb7D7mtN_nY5jijv2U_zfM6AEVPgBnk87SAt5Z6iUE8Lbkmq1CBU7sSrhl4PB-e8MIFkxBIG45iEXfraoY72nALgkMd2wm6VL1nyfRgVYi7L1jk-QeJjInNC8TtLKf2CxwoHaIZD344bE-pVBhea8UDHyomqGOwePB-DNXShRhiWuohNLV3g7NQzVhgWeIv4AcsNAAam6k5RCzV3VdD72KjRMnzwuXDrfkemJi_SBSg75A_3F_kyG9C6GlDdZwSkWRawY5-xaa2ndfD3hjO6MOA8aM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d8601fda.mp4?token=gw93yHaU7h_tfmRegjZLjO7XnIWR04Skx1LJ1aB7n99oOXwEj657d-VYY9CiG1QYprzjRowTkk3a-NcjTLfwEFqLmn9jH7RfFmrkmSuBckf4GxWkU9ypsg_bLZLKWz9HEmA6AV9SmGmAKHoAD7XDWrdeJ64ptTzSbwz_WN5BeqBEsbBvA85cDECkSQR7lJ4cZbyPqngRTY-S5fytgrMrrnzC84WZ-aVPNb5XNJvalKno59R9YqvAryOUR0-ZQOyC2kkIFBak3GoZ7uo6FrEtF2lAao2pL-ffltlo0uqdB3q1X_LyMPbelE9uqNnMXcO4GJdxAhQLjiHXAPNUxxF70BnwLTDV8pUQtv9NF_NpARilDYvKJXG19M3p7wiZIGasrmvb8JlC_NRvSkxnhLb7D7mtN_nY5jijv2U_zfM6AEVPgBnk87SAt5Z6iUE8Lbkmq1CBU7sSrhl4PB-e8MIFkxBIG45iEXfraoY72nALgkMd2wm6VL1nyfRgVYi7L1jk-QeJjInNC8TtLKf2CxwoHaIZD344bE-pVBhea8UDHyomqGOwePB-DNXShRhiWuohNLV3g7NQzVhgWeIv4AcsNAAam6k5RCzV3VdD72KjRMnzwuXDrfkemJi_SBSg75A_3F_kyG9C6GlDdZwSkWRawY5-xaa2ndfD3hjO6MOA8aM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمایت خانوادۀ شهدای میناب از تیم ملی فوتبال
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/442456" target="_blank">📅 04:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442455">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlLqyxvET5P6MinwPbUkTX2x78WqWXp9aVFH1jC7P-vTo760CrmlLx-Moeep7qlCLIm6mhB18hxaC3MAoi3iHL-L4iZJkDPVadHznQ4tvX9lTJ429h3bdvlnO2-onUS1_hRn0lykh-2qOQ2M7Gz6j1TC67LdVAVz1zIuiZZFnn8Ro3Xx96JOfkCdmTKM24vft-RLlTjNqZ27IhLeLv7_eNo5pql01CsQzjGQ_kTU72mtHRxIKT2C9aG-qnkR2RYPPFyLE0SS3_SlnCaeQVehE4CQWEqJ9vsmkGk0Le-iuGvZfaHY3qJTv_CXEBMSRrUvP--cYN_HzXqcXI5C5IhzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس تیمی ایران پیش از شروع مسابقه
@Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/442455" target="_blank">📅 04:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442454">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d6d9fa8a.mp4?token=CBJUpkxv3A-WyJ8pT34tKeDiJOlvrykhnetkO0wuAw6Wl3LHIpLx2fWjpC7P_ljIg9EKg7TWrKmmYxWj14AdlvwiEpo67mYfbMdEZkK9rYgE8IW2zoBERUDlyFnKfkfV3NY50CbhsGcoY4CjxZcwcVm3Lh3WGp0egbqa5vw2fODpck9UW9RRVfObQxaxL5iR0PBICWzvXUZ63yU6ftKtis17g_zdDsY7-IVw_cfKGXE85t0Rci8sPYQ85wKVwbJ3ZuqfKaUFTgDiFuSFZQ5w-CHi1WMwvAguHr2SyqjY56VriroaIBcfDi5jes7o6WhGFrNCZ34N8c3MB3BbQrEmdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d6d9fa8a.mp4?token=CBJUpkxv3A-WyJ8pT34tKeDiJOlvrykhnetkO0wuAw6Wl3LHIpLx2fWjpC7P_ljIg9EKg7TWrKmmYxWj14AdlvwiEpo67mYfbMdEZkK9rYgE8IW2zoBERUDlyFnKfkfV3NY50CbhsGcoY4CjxZcwcVm3Lh3WGp0egbqa5vw2fODpck9UW9RRVfObQxaxL5iR0PBICWzvXUZ63yU6ftKtis17g_zdDsY7-IVw_cfKGXE85t0Rci8sPYQ85wKVwbJ3ZuqfKaUFTgDiFuSFZQ5w-CHi1WMwvAguHr2SyqjY56VriroaIBcfDi5jes7o6WhGFrNCZ34N8c3MB3BbQrEmdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همخوانی سربازان ایران
🇮🇷
پخش سرود ایران در ورزشگاه سوفای لس‌آنجلس
@Sportfars</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/442454" target="_blank">📅 04:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442453">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
ورود بازیکنان تیم‌ملی ایران به زمین
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/442453" target="_blank">📅 04:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442452">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a3133c8fd.mp4?token=UdAJQQNE3iq3m7YZlGuzi4gpDncTQLLGobOtQpFKq7lMieK8bVA4CN1wRBnAxnIxQHXFZHsOoeK_uGvowVWUZ-q_w5tNynRqhahuLTqSq6FbmgmGgne32eadHi41lKVUIWsbnmZa4I-Q5AQ1gfkExxlg_UWDN3_6Yzxz2LFqImo_o7_1L_I-0RoyDAOofGGnBk8cdXJfkFr5yC67I6qz2erR8b0zWqlV3qjh0hOGMUqmvRkrMOOMMiT0FTb5zTgRQRN7LqjsrXdliTo6xHfWevpeYC9HyM6gYym0s72jRRkY-YK4cQ7k7CEfPV7fYp6jwXQc3divZMHXXXzhWmjLsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a3133c8fd.mp4?token=UdAJQQNE3iq3m7YZlGuzi4gpDncTQLLGobOtQpFKq7lMieK8bVA4CN1wRBnAxnIxQHXFZHsOoeK_uGvowVWUZ-q_w5tNynRqhahuLTqSq6FbmgmGgne32eadHi41lKVUIWsbnmZa4I-Q5AQ1gfkExxlg_UWDN3_6Yzxz2LFqImo_o7_1L_I-0RoyDAOofGGnBk8cdXJfkFr5yC67I6qz2erR8b0zWqlV3qjh0hOGMUqmvRkrMOOMMiT0FTb5zTgRQRN7LqjsrXdliTo6xHfWevpeYC9HyM6gYym0s72jRRkY-YK4cQ7k7CEfPV7fYp6jwXQc3divZMHXXXzhWmjLsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پرچم بزرگ ایران در ورزشگاه لس‌آنجلس باز شد
@Sportfars</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/442452" target="_blank">📅 04:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442451">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bb88373f.mp4?token=jKyAcwwzACdCd6L9CXFVPfwnAli_LU25eURAfbYj1bjl6Z1iP1n1E5vPmvzO6SZC_L2O8e62baNmm83YWQmT1rpjWAEN7KG7Q-XRzAIN5SbYSGl2fkhl6QiEAx9uT52AYcWDKgFtErV46TnHYNcCvPEdttIKrfwtvGnl5CivkSw8nq0ugpuGUkO8sRlqzQ3kNFpRlMrup48Phkj-lMxkQceqrAtAz3_rVn3X69UJcl7UNbxvkxYVp9g8wUXOFthb09Q0LAdW5dd5Dy3dxf-6dm_nx5HaYNoAY2tWqH19TPglREwflWB57IZrwcso2Z8Uth_6DYPBtD6NE9bJf2Or73BmOMWf76M4xI7mNlt5P1S2SwNzveVsPmCc5IYGeRhSq2ftKo_qCVvBLExjChQsjhMzd0tGKUJaooXZ4PYg73-pvyJq2b1HnJ7wxd1gJeHannZurUwB-1A8k4Z6vsWT9GYKUTRtMDIBWZknQueoE_Hg5C3ctDcz2NpmIyshgiPMpJ9_Y4fx-JMVuenKdtqHFVyGjEOjuHgaBHaflOT03TltWxgMH4y1bcCuYGSugNI9DLtJBldSPZjXp3SEq69HDQuatnMZrDEoz3Upzw-Nt2_YrrdnTMjvCTgl3idVkRqZUuBnPf4DpILd85jGDnQ4lTnVyAfh-KMp7yKrnRzIP_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bb88373f.mp4?token=jKyAcwwzACdCd6L9CXFVPfwnAli_LU25eURAfbYj1bjl6Z1iP1n1E5vPmvzO6SZC_L2O8e62baNmm83YWQmT1rpjWAEN7KG7Q-XRzAIN5SbYSGl2fkhl6QiEAx9uT52AYcWDKgFtErV46TnHYNcCvPEdttIKrfwtvGnl5CivkSw8nq0ugpuGUkO8sRlqzQ3kNFpRlMrup48Phkj-lMxkQceqrAtAz3_rVn3X69UJcl7UNbxvkxYVp9g8wUXOFthb09Q0LAdW5dd5Dy3dxf-6dm_nx5HaYNoAY2tWqH19TPglREwflWB57IZrwcso2Z8Uth_6DYPBtD6NE9bJf2Or73BmOMWf76M4xI7mNlt5P1S2SwNzveVsPmCc5IYGeRhSq2ftKo_qCVvBLExjChQsjhMzd0tGKUJaooXZ4PYg73-pvyJq2b1HnJ7wxd1gJeHannZurUwB-1A8k4Z6vsWT9GYKUTRtMDIBWZknQueoE_Hg5C3ctDcz2NpmIyshgiPMpJ9_Y4fx-JMVuenKdtqHFVyGjEOjuHgaBHaflOT03TltWxgMH4y1bcCuYGSugNI9DLtJBldSPZjXp3SEq69HDQuatnMZrDEoz3Upzw-Nt2_YrrdnTMjvCTgl3idVkRqZUuBnPf4DpILd85jGDnQ4lTnVyAfh-KMp7yKrnRzIP_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معرفی ١١ بازیکن تیم‌ملی فوتبال در ورزشگاه سوفای
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/442451" target="_blank">📅 04:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442450">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adfc9fa056.mp4?token=ux20k2RtSJkXcUYL2TKInyeQXClCLPrqwMD0856a1IFtzlXPFDdf50Ua-ddzxcINhgSs61slPby3_nIS0d19wK1yq7ETy-hiQJEC7x_y01yQtGt2Kt8yfodrUMe0jsfeElhYkju0ZV1RJPODk9DRPD1_GVqjyxpuhfVstaXOAsIBmtOswRfEqwsWk6vCvwgFY2GO_KjgLf2pY8ibh8VcOZmBuIx-qI8OCOkoebX2Gg7X-Vr8a1_I-M0datyXr81yPHIIJ4pPpNAOnI1uZY7eAvgMVflnLXrNtGjcS5AoLB9d1JgdD5X8xeTBED1XyScF8SY4iyuwGjLl-DqdFqI76w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adfc9fa056.mp4?token=ux20k2RtSJkXcUYL2TKInyeQXClCLPrqwMD0856a1IFtzlXPFDdf50Ua-ddzxcINhgSs61slPby3_nIS0d19wK1yq7ETy-hiQJEC7x_y01yQtGt2Kt8yfodrUMe0jsfeElhYkju0ZV1RJPODk9DRPD1_GVqjyxpuhfVstaXOAsIBmtOswRfEqwsWk6vCvwgFY2GO_KjgLf2pY8ibh8VcOZmBuIx-qI8OCOkoebX2Gg7X-Vr8a1_I-M0datyXr81yPHIIJ4pPpNAOnI1uZY7eAvgMVflnLXrNtGjcS5AoLB9d1JgdD5X8xeTBED1XyScF8SY4iyuwGjLl-DqdFqI76w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدای پرواز همای در سوفای پیچید؛ پخش آهنگ تیم‌ملی در ورزشگاه
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442450" target="_blank">📅 04:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442449">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYKQoF2fKNj3F4TdrUi3xtd8mws_u66NR6HE-qZFNBhYpcBSgyV97-QkC5mlrphx5tmK7lYt-4Q1Tfv5xIpNLTEuKwpLCdhW2EJv0dbwOmIF28WHBmiQkO5f9TUIp85e9wHZLlYf6Kice8Raez0AZJkqtYGPMU1X0Lsh-Adxo_n4qXSW7FinNI8wjlZqOUDfN6VhS_4idZajCZQt5PGfGVWSUc9AEOyn2cS3XIRn5SquKi_jfHR8606eyc_1F-0ci88dSU4f4ofyvHNsZH71JwqmLwHiGk6-FWnWZLbpjbiurAjE3DkscbxyPV7shuhBu0uXRDIwlHVm083qSmWabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه‌نویی: شرایط تیمی بسیار خوبی داریم؛ با تمام انرژی برای مردم بازی می‌کنیم
🔹
سرمربی تیم‌ملی در گفت‌وگو با فیفا: بازیکنان باتجربه‌ای داریم که برخی از آن‌ها دو تا چهار دوره تجربۀ حضور در جام‌جهانی دارند. مطمئنم با تمام انرژی برای مردم بازی می‌کنند.
🔹
نتیجه دست خداست اما با وجود تمام مشکلات مانند ویزا و کمبود وقت برای سازگاری، شرایط تیمی خیلی خوبی داریم و بچه‌ها مصمم هستند یک بازی خوب و پرانرژی با اجرای فرامین تاکتیکی انجام دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/442449" target="_blank">📅 04:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442448">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BItQt2laliadojVDl7rOawmx69A6Ia-ulNOxBGFHPv7ufUTS_01zJjeoybbsoyWaKEvuC39MftHCybsJstS3lhbG24wTjk9FvldVYErbznHENQX3Q7EgvfQhxtZVSTJxcJc4K3fcMTq0k7OdRdTLYSqZv16bX8BGUl1Q6oAa5pPDcrDt2G6Zp9R19JOqgqyMhYyU_weaenFS-T-Hghx6TW0mecmANbad2OeDzq_uQfTFMfmKowhwGQq8QrgqHUPkoZ0vreSniAGiEKWLZV2XfU_nqpVqzVAD74xcXmpqkBqZZFyZMcWLD0aa5fjHvyq2AF2TI2tQ2w2_4KKqjaIPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌فروش بلیت قطار‌های مسافری تیرماه از چهارشنبه ۲۷ خرداد آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/442448" target="_blank">📅 03:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442447">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030daf485.mp4?token=LAugZIMlPmfIwTohJCI1aOXiHbxD6X-Jqi2EpcNeu23Momr7g-HK2dqpeN7G2kQio0IJXSvxCn_qjXUsG8wqkLoclx7aJ6nEM5vfR0appJAFdxyTsZd7o7Nxxh_sTSHCVyueImeWVy5rU73wvfmNkZHLrge_ZFDFonqom5-2JJC4s3p__4kSFX4V5yL2RXVepyK1t03xPbmjoxPb7A8346vKUrDUrAhq4M3qSdS8EEQIlucKB7x8Z8F2NswGEdvmgUuhwVrgZTktqHJnJgpT2NVmCqFZ3rlTISduy6lEzlXC8jkcdVMjuD9MqNK0TAog7DccYlNRCtIqy1BHi_J0JnwCuz1LqYS8wQZZyrSvL1g4833lZhZkY_PaeJObj-9RcUmCST2GEkycbJfpG7ARoPkCH2UPwf3QkCt2I0WNPklAsZkx8Qr2efsi0_2v7JrwqGQzQlhKi864jcQck2YM3ZF_pZpeZmZyuwJdmyHHGH-qavjtNZ5zpdcGFIvnFawcsgnTB655sYuGMbpJTQRXBuzxHVz5TbauEdZCt5HOtiuTVALBJ6-ntCJA9AzBRp-rkqKi9U_MBdqgqqvBcUvRyb6t8Jy-bDwuGALHFIAWfgLGZsPbEuxinA_PRpEPrEHWIf5mA1ZCfeBdXb2lmy6k9l7hjiZVD6iYEJytPeLu1zM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030daf485.mp4?token=LAugZIMlPmfIwTohJCI1aOXiHbxD6X-Jqi2EpcNeu23Momr7g-HK2dqpeN7G2kQio0IJXSvxCn_qjXUsG8wqkLoclx7aJ6nEM5vfR0appJAFdxyTsZd7o7Nxxh_sTSHCVyueImeWVy5rU73wvfmNkZHLrge_ZFDFonqom5-2JJC4s3p__4kSFX4V5yL2RXVepyK1t03xPbmjoxPb7A8346vKUrDUrAhq4M3qSdS8EEQIlucKB7x8Z8F2NswGEdvmgUuhwVrgZTktqHJnJgpT2NVmCqFZ3rlTISduy6lEzlXC8jkcdVMjuD9MqNK0TAog7DccYlNRCtIqy1BHi_J0JnwCuz1LqYS8wQZZyrSvL1g4833lZhZkY_PaeJObj-9RcUmCST2GEkycbJfpG7ARoPkCH2UPwf3QkCt2I0WNPklAsZkx8Qr2efsi0_2v7JrwqGQzQlhKi864jcQck2YM3ZF_pZpeZmZyuwJdmyHHGH-qavjtNZ5zpdcGFIvnFawcsgnTB655sYuGMbpJTQRXBuzxHVz5TbauEdZCt5HOtiuTVALBJ6-ntCJA9AzBRp-rkqKi9U_MBdqgqqvBcUvRyb6t8Jy-bDwuGALHFIAWfgLGZsPbEuxinA_PRpEPrEHWIf5mA1ZCfeBdXb2lmy6k9l7hjiZVD6iYEJytPeLu1zM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بازیکنان ایران در حال گرم‌کردن هستند
@Sportfars</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/442447" target="_blank">📅 03:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442446">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639510f858.mp4?token=BGAEi3c1sEnCV2rZQzetBH9siB1WrmW6xzbfWXro1VE99EgFq3zbMOdt9z1t2w0C6jI9cnROnb1FwRWjbzc-FBgW7OXKLfCOkaIl3gQf8HIb3zKliiinwwQTg0L8IAUlV10Lsk5bWSc0BGQsS4Dbld-2mUrswS8TWz6KN516RqO02J45HjFl-pU3BIZgaJoHR8zZhWtVAmRLoIoZUFsriaNwEWewodWlM8mOR08CpydNsSsbFBRg8DHxHNPTRf4hsR2d9gsbMw24KxkwIAwRAP7kK2wWUEsv1nIOX2ja1NBk5hzPjMC-MlkoifYusNdNAkzff6627pqYMxQtNkhRlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639510f858.mp4?token=BGAEi3c1sEnCV2rZQzetBH9siB1WrmW6xzbfWXro1VE99EgFq3zbMOdt9z1t2w0C6jI9cnROnb1FwRWjbzc-FBgW7OXKLfCOkaIl3gQf8HIb3zKliiinwwQTg0L8IAUlV10Lsk5bWSc0BGQsS4Dbld-2mUrswS8TWz6KN516RqO02J45HjFl-pU3BIZgaJoHR8zZhWtVAmRLoIoZUFsriaNwEWewodWlM8mOR08CpydNsSsbFBRg8DHxHNPTRf4hsR2d9gsbMw24KxkwIAwRAP7kK2wWUEsv1nIOX2ja1NBk5hzPjMC-MlkoifYusNdNAkzff6627pqYMxQtNkhRlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی از ورزشگاه سوفای لس‌آنجلس، یک‌ساعت مانده به آغاز بازی تیم‌ملی
@Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/442446" target="_blank">📅 03:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442445">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbE5wqVV5LZqnOC_oayuYP9KQA1ez4FanzbTNEOEy06a0v6x12R8-YNZ8lxwAOIlXkki9Qm652OjhYl5nhCBQyY8X4mKIxkRKBZWAfI7SxDcDBT5Qy8Huoy4UObOgUuvo5j3NzUsX5YYAck0imnGnCci4Fy539myItQ5LEu4y-Fshs7n_JMMxLGic4SE-zw98kYofcyQJQ1N0PRNZ6njv2DdznQ7EatH2uRWQ_PZR_1xFb9EKu5Ps9sAZw-ncbH9NFvl_N01GKlPHHuYQKEq1TOIG1VPX3F64Tn3zwIb1SJWWvqRRKwbI1uF4YwNpEd9URpmpL06DqOHjJxDyGUmyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان در آخرین دقایق برد را از دست داد
⚽️
اروگوئه ۱ - ۱ عربستان
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/442445" target="_blank">📅 03:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442444">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07a6002605.mp4?token=GmoNxtOylis6pPmnHqP_s0XAwEqNBg78Wi6RZmz7_-3cm2-7_GDeuoESvRd49gFLjj3-fYfVQ_lgOInAJnB-bdbpWLOgqCPqyAzLKU6dfWSbTGQJtMZEXnkyhVTKMMkVdlkFsFLQMpQi2OvEbwNQWACscrBOn_iiMr8SBQP0jFR-LxHMHOt9uj6G8w8jqiDAtROIY7tazA7S0BrfS00Xgf-Sv_QnMlc-7SdXN9MWKnkgednO4SMrllmNUmPwOYkRVsMmgrKvtdSkGLirIXmghW7rsS5W9qvcBKxilI0GJdcQ3IzKKm9P_hR4o3BMvs1AlzEnQQ9IjfKruiP9zeXQUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07a6002605.mp4?token=GmoNxtOylis6pPmnHqP_s0XAwEqNBg78Wi6RZmz7_-3cm2-7_GDeuoESvRd49gFLjj3-fYfVQ_lgOInAJnB-bdbpWLOgqCPqyAzLKU6dfWSbTGQJtMZEXnkyhVTKMMkVdlkFsFLQMpQi2OvEbwNQWACscrBOn_iiMr8SBQP0jFR-LxHMHOt9uj6G8w8jqiDAtROIY7tazA7S0BrfS00Xgf-Sv_QnMlc-7SdXN9MWKnkgednO4SMrllmNUmPwOYkRVsMmgrKvtdSkGLirIXmghW7rsS5W9qvcBKxilI0GJdcQ3IzKKm9P_hR4o3BMvs1AlzEnQQ9IjfKruiP9zeXQUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد «ایران، ایران» در ورودی ورزشگاه سوفای لس‌آنجلس
@Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/442444" target="_blank">📅 03:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442443">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTgSPZdRHxa0sO9XRNuNaqQA5CG5WUkUGcApwsp1p1F2_QKkZ_0_2Tgu2TKfrAh1ZDTW5l-navuR8J-kxvUwC7RxqnYfpRL6AaLWll2_rzhwVWM_iUAeoTcvLa4vqvWba7KHWSl3XrQYv9nPR01Q4h6UzFlVJeuV9PwSof2CdyY8KVbvUJg591ElIQ45UQUFf46I_etnw2F0JX7YdP8TDwacTgSwB8YcCy57SNyOvzfxwfBXNm2UtyZz8xpCCyt5Ni1Baw67i5WMW-2jm3gy7PC5kjiYqLDZBEvqG5Fl0teVEyrlyBCGCbZ7V3FbaFv0fjr0Q4BfJLJpXPjByrmBWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب تیم‌ملی ایران مقابل نیوزیلند
⚽️
ساعت ۰۴:۳۰ @Sportfars</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/442443" target="_blank">📅 03:18 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
