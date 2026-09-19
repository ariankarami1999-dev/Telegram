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
<img src="https://cdn4.telesco.pe/file/Y7D2ejLthuKI1pzf7zAF_ZigvW-aP1oJ1dzAokgC3rPJETKgUXye2xkS5LcrdKRCVbSO2sThBmQyWfh2ggbzJ5YC9AbzT5zC2ipG_UStu6sHd7XZhiDqUSLxLswyxEp38uatHwzHhwEhnXH6vbT-gD96CmQmxzFRlQOleFkJ9JHs9wGVkJBCn5fhQdgvzuXOdheAypPJv06hsqc-rXlfJo0yi-NVWzJNoDD6CeqtSAI4MKZb2VDl-FYpqRRqzDNsw_KUN_dk0vL6QrQE09lCU_tKDwx-DenuqkaBQ1ppBa05DfkduxbiEI6ne-D0PqHOu7xHcEvirJEqf68dCizUjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 00:22:18</div>
<hr>

<div class="tg-post" id="msg-463104">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7V6zK14mFjiabaoOrK29xTDNh-CXXokXatoc-AXrTmwGR2b92hQHvRQiP0N23_AD7cRzm54OOyAXoWTggbNyZ_SKFcTk2SsoBxJ4coItDGQ5xs1Ps8XPpeMjfG60di67RoEDdJ-W0KUyYspU6IjggC1rKCibdevJbEE4_qcv_wznwnGVNtYCRlWEO6Jb5J77Ig6FZXMOxKnTN2Fu5K-ld1wP80DoWo-6pojyAmp1wzm21AUsmpm0GYFVjfWBWNTxZlhcdeU61YtA-0yqmvfFyk4Pv-BF_2msPe1g_HenOlS-t982owDd5yX3zRHCrJgrlvLro0RsQ-9UmtQ5ho9zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات هوایی اسرائیل به جنوب لبنان
🔹
جنگنده‌های رژیم صهیونیستی در چندین نوبت دو شهرک کفرتبنیت و النبطه الفوقا در جنوب لبنان را بمباران کردند.
@Farsna</div>
<div class="tg-footer">👁️ 991 · <a href="https://t.me/farsna/463104" target="_blank">📅 00:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463103">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGeGmPpKmBRHvPlRfdXTvF2Jc7v-YQ1OO1rAlr2E-A1nrisO1ByDWXsKt3PuoInHv7qIllEnguC2kcSwU0UEqhfEiMJmQITZ-RadXIDKQnnG7zndPfs8oJNMaW5m5WgiEox3NpAVafNZLMLAk8TdG1ag9QQ-kx50aKcDIGYS14RfxYaZuCm9nr4h9J-GOpYmZO7iis6aL0-Xb7GAtbYhTMTiJM1KTUqzjcbiIZeZH-5PhWD5mg3r4-WZNZ4bcbTCqd_kgQc1pA8f5eOGEfjrpTQ7KxS97cO3AWbZAYgxz-wKQwxxWGNOUabhqBPm5aMyS-yCcETbPwkoDPsMISg2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتدال در عبودیت
🔹
روزی امیرالمؤمنین علی(ع) برای احوال‌پرسی و عیادت به خانه یکی از یاران خود به نام «علاء بن زیاد» رفت. وقتی علی(ع) خانه بسیار بزرگ و مجلل علاء را دید، به او فرمود: «با داشتن چنین خانه بزرگی در این دنیا چه می‌کنی، درحالی‌که در آخرت به آن نیازمندتری؟ البته اگر در این خانه بزرگ از میهمانان پذیرایی کنی، صله رحم به‌جا آوری و حقوق واجب الهی را بپردازی، همین خانه بزرگ برای تو وسیله‌ای برای رسیدن به آخرت خواهد بود.»
🔹
در این هنگام، علاء فرصت را غنیمت شمرد و از برادرش «عاصم بن زیاد» شکایت کرد و گفت: «ای امیرالمؤمنین، از برادرم عاصم به شما شکایت می‌کنم! او عبایی کهنه پوشیده، تارک دنیا شده، خانواده و زندگی را رها کرده و فقط به عبادت می‌پردازد.»
🔹
علی(ع) دستور داد عاصم را حاضر کنند. وقتی عاصم آمد، علی(ع) با لحنی تند و عتاب‌آمیز به او فرمود: «ای دشمن‌ جان خویش! شیطان تو را گمراه ساخته است. آیا به خانواده و فرزندانت رحم نمی‌کنی؟ آیا گمان می‌کنی خداوند نعمت‌های پاکیزه‌اش را بر تو حلال کرده، اما خوش ندارد که از آن‌ها استفاده کنی؟ تو در پیشگاه خدا کوچک‌تر از آن هستی که این‌گونه با تو رفتار کند!»
🔹
عاصم که غافلگیر شده بود، پرسید: «ای امیرالمؤمنین، پس چرا خودت جامه‌های خشن می‌پوشی و غذای ناگوار و ساده می‌خوری؟ من هم به تو اقتدا کرده‌ام!»
🔹
علی(ع) پاسخ داد: « من مانند تو نیستم. خداوند بر پیشوایان دادگر واجب کرده که زندگی خود را با ضعیف‌ترین و فقیرترین مردم اندازه‌گیری کنند تا فقر و تنگدستی، مستمندان را از پا درنیاورد و رنجور نسازد.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/farsna/463103" target="_blank">📅 00:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463102">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">زخمی‌شدن چوپانی که حاضر نشد به خرس شلیک کند
🔹
مدیر حفاظت محیط‌زیست کهگیلویه‌وبویراحمد:حملۀ خرس به چوپان ۵۵ ساله در محدوده تنگ سردو روستای قلعه بنی چرام، منجر به مصدومیت او از ناحیۀ پای راست شد.
🔹
چوپان طبیعت‌دوست با وجود داشتن اسلحۀ مجاز به خرسی که به او حمله کرده بود شلیک نکرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/463102" target="_blank">📅 00:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463101">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa14e10ebf.mp4?token=fOegApDcpH9PHOCruzQn88h006-0NwtF0vG6LGwqRYMxEAxdodevB6zd2G2e5BimH2J9yu3ilXMbYoRJVBBMiWZ2Tei043wteqfq1i9UkHYSjEjWliT-YssgeaBZ4n6ctPAQDL8Wp3GHR42827HCKxOEz57oVTtZRa-TId46iB0H97HsaZjLTQu5mP1Ikr2DjslzN-skqABE4kSuyugRgyKOpq1haP_FqGVC12V4DvjCpN03MR2RnbRZL_Jww7FpGYzFPKlrdLl73j4beZyf3hlXJ_4wBXmTwlihs65oDVwJ_WY58lrWcD54JDbvMg-7XLiFfnbCvZzNlI7cN1stSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa14e10ebf.mp4?token=fOegApDcpH9PHOCruzQn88h006-0NwtF0vG6LGwqRYMxEAxdodevB6zd2G2e5BimH2J9yu3ilXMbYoRJVBBMiWZ2Tei043wteqfq1i9UkHYSjEjWliT-YssgeaBZ4n6ctPAQDL8Wp3GHR42827HCKxOEz57oVTtZRa-TId46iB0H97HsaZjLTQu5mP1Ikr2DjslzN-skqABE4kSuyugRgyKOpq1haP_FqGVC12V4DvjCpN03MR2RnbRZL_Jww7FpGYzFPKlrdLl73j4beZyf3hlXJ_4wBXmTwlihs65oDVwJ_WY58lrWcD54JDbvMg-7XLiFfnbCvZzNlI7cN1stSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین گِرهی که از همسایه‌تون باز کردید چی بوده؟
@Farsna</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/463101" target="_blank">📅 23:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463100">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ba59290f.mp4?token=or2v1pGfoBuXXb4lb9oWdeEUO2fk1B_crv0dV7diLyjnkV2n9r7H6dN0NIJtmXN659RvJLtiC645wDUT8OWrqnMJtD0qw-lVwO6QA3c2ym3CE757pL24Nm-vS4Wqr0Mr_mfEaz4iiGWSwzeDAEkuIT1NibCwb2uwhWVaWspUcyXuMaZXwfGsxDf1y5K0r8cqdi9FZLIJ3Rh6KjKVMDHl46HZOzYTo6CoO0_oBp0ZcU4cIDRljgdu7RqNWdDakPKgA9w7zYFONDurEvgbr4BHbg1IbKBgFFqXARM78gdL-q4TDh1yrV8cIQPfNjTTYEWeiBele_jbC1xiQ4NxBiehMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ba59290f.mp4?token=or2v1pGfoBuXXb4lb9oWdeEUO2fk1B_crv0dV7diLyjnkV2n9r7H6dN0NIJtmXN659RvJLtiC645wDUT8OWrqnMJtD0qw-lVwO6QA3c2ym3CE757pL24Nm-vS4Wqr0Mr_mfEaz4iiGWSwzeDAEkuIT1NibCwb2uwhWVaWspUcyXuMaZXwfGsxDf1y5K0r8cqdi9FZLIJ3Rh6KjKVMDHl46HZOzYTo6CoO0_oBp0ZcU4cIDRljgdu7RqNWdDakPKgA9w7zYFONDurEvgbr4BHbg1IbKBgFFqXARM78gdL-q4TDh1yrV8cIQPfNjTTYEWeiBele_jbC1xiQ4NxBiehMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند دقیقه‌ با قهرمانان سرآشپز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/farsna/463100" target="_blank">📅 23:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463093">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LO0seEJWVVwrEz6MDNvpudRvzxcaIDdf_l_cOsYNkeRWOrFebKkkcdVD6H1K_J4bh0xuHuFSphJwxo8pCOuMG_zvJPgz5IvizkimZsQ1oHRNgtQ8ToUU-s7TvPdlKZwJdp4Vg4d3WvWduKuXFI5Akue5f71H1Tnz2vl1ncXDLraWVjwrQ1A8xYJO0kL1lA3KUBPIBVJ_YVys8mfBKx3n6xUMCkca-g_JjYJWGOg52Zw8YcmwXGargZuWZhYqw07xarA7qJwHX08JUAKTkxVEI5cyBcv4NkPhlo7fywKfxuZ_ZPf4V5IOYkr1r9DdE78NWTxHo8ivqneHWyTEZFRThA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQ8Mdcw1kI0AzhKIZcv9rRuoZ41fNAlPUmUkTbGqijTsmGE7lVRVRS0TYTtYR42Ri5NsmCf6x0VQ_NHrP7DkoKnsokHBJPp3-eiFMA7gCmBe_4O9EblNYnNmpDsaKvspYUrAJ6jyRq0Ymn806kBaYv80mIOrdYYVqS-kbYzADgiRZzqNCW22M49gvQOJJCTFLICGPQTJB85itGe9xjG_byHtjMkDwMqIQo7dM5QvTNKAKIwU-l94BZ-GnruYXRgEZ4JOCUZLkOgoczFMOAwKq-S8FjL27MrT37uXNtlOzy_JVN6Ssg5GuSL_4lFNzN9SCaPdDHpIqdu3tyT0DTLyNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fh27f7mBOy6mISZgNibN1xFjKVIbbOAoOF_fFDJq9liv42JkiQFEydHfBEbR5-d4N-d4epmI4csunwikUVxoisBUfjFxHuVAJRT8BzUouMra5R7zooAK0JmiB9wVTmLSOhYaR8NF_zKkjxjwTzBrJMwcLtOBDtuRiCx99OrzlgVNCWvJZA7_OikBw86093-BNFPmcb9Y89C58mMfBvr7hN3CjRSThI09nzviry2RnDLIOCp54RvkpoEmNSDgDR9kbedB0won-knAmrKiveh5iz22ofEw-Z4wA3mbTfC2CaPhp4etYVG0p4ALZh1Mo3eZPHhqTQeezlIzodNCVQ55qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rZCwbuKKm--T0C-4Fy2RiZ1OOwVuB1-v2PvE9FtVqhoZRFOgsGKEsMBPXf7p2Lh0WfLRu8FWw6RZg8z7_wE5uy9oOtfpo8l5M1voQhJewX2zIS7VvDHYYWw71HVv6bTvZ4i1MSMrF3Sc9IJ_tSvgIKaLFkL5KVaw0G6yF78bcAIiVDBMV5y8IcnzorPWS-MCoIfZ6eQkrDa_BzSHeQonJpGf5fyAAM8TxucaT3yD8lamU5EZRTxM7N3TArbHETGxSYW7hYWQuTbF84-B9yAGmjlbODw24HwYAqhyklyk-8Xr8Uw-MXuTqZNl3Gup26fmn0jzKlMqNebrjFJF_aUY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZormU34TPPiwvvLqyfH5Xoe4SiRDaR0p6EB9a1l_PkdPRHspeRnJsjMwbpX1W0SJihXXkwSv_8rddCKqzrGVnKfn9oMROGHR2sHr9XGSHa4VfcC3Ho53B6SRMv6nZXe293WVB8Y7zn-bAQb5CdwD_tRRp5zXeYgtzGFobMTav2YFwWFCkauZWDcIlUXNeXP4bFxa-9gFfrdHTlTudPykpwUsWVunaODUMmcvh9OZZ983hRltBQdJnBibB0HiYct7OxRdhu4QJHdRu3KkLiCFibLUqiEgQNS5xlw87-HzYS7SSHUqB7oeiy6Q75HN21PlJueMCccfOo4wqQ2_rDQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jEmLIw21pnWLyg2AKEvqdxFh4pCBaeZ0iguPVWpkJqdwoFMjWmbWCRd32lMU_wpNBADxnYSETtkitFB8O6iuUJ_V-ESYhQEv9ZD-qVy11w4XZV4q-88O0SqCLcyXzC5R23MFNzzZCDN2ljbcSJCE39tNIYUckSBC49gGxWLU4VcRn0LiOq5SzCtvagZg9ERiIpWqeu_Uft0dAUwMY4zx38sQqeI7UL0RGTpD_qQE7eBoNXlJo7t6y2DYmYMeQqvkOeRtHBUVGCeb7ClNNt4B7Nxx09_kxxFw4qkq5tuXUuhBdhBv0ARGUXm6vx4tCscEHH4dxba0rNFdJOMP9854qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jbU8sqOjJg85YAWBEBJwLH-lnWB-R_4LZfQ1i1yKzyuJq6ctUw5uH4GCUQsZj35Oydt8d0FPrWs8lVOOS2aCv98Vlu1CcgwujsUgCEithE0gCMOyZ5S3FKQm6s-vth8PcTU5a2O6qh6i_gUScdQpSjczXGB56VXMldLMWUGN-QLOCwS4OgVZ7EnHVhOv5fRQU-CMafG4IKYMXHly6ySlQ7sH-1WNvPmye-aYeuzjY_d_KC2mHXUHIeLzX_rnZLHC6rhiAbuE8TtX9qchpkhzDFs_mFXR0jKlvFzFclROoTeEHcFtTmKo1Cn2PwIG011H4MBzbi65yHVVjLEbgcrXcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رقابت‌های لیگ کشوری تکواندو نوجوانان در البرز
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/463093" target="_blank">📅 23:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463092">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/au8YxMcoICku4h8ZCqSlk1gyySXqUoL23-2N8VUJLuPJ-xJ6n2gENTfyoWPhSbCcyFg2N3X7K_HPZs0h1eJ0NBF9tbYHHRJ0HTdICpwFtttjbIyTClhOc1NVCEMlUTmamLbCQDS4BkzTFnonD02Y8HtHcaFnYeYvwvnGmXxuM5GsyXobTVsdrGFpSzd__QdNCy1emFX7q_mijxTSKkGW0s82CT1iKszDi-jZiKP4fILGKC0qH6P7ORyc9f36sYYbLqOWBEA1_UfaDwaEFO5VyKfw5YvVlHyCXs5y8G4p2Io9Y8kEd5cLTZeyGYnwtON-dUIc22op-XGqv6cdT-Kjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق مکه؛ ائتلافی برای نجنگیدن
🔹
عربستان سعودی، پاکستان و ترکیه امروز جمعه ۱۶ مرداد در مکه سندی امضا کردند که از آن با عنوان «توافقنامه دفاع مشترک مکه» یاد می‌شود. مهم‌ترین بند این سند، بر اساس بیانیه مشترک سه کشور، «اصل دفاع جمعی» است؛ به این معنا که هرگونه…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/463092" target="_blank">📅 23:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463091">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVATJA5Yn-eSLAkuzkNrCKlC1svInuMXQZOgPTVLSZYopiV7qCQxXjXQOmy3kiBD_O0VsnxTEIp4ZyshKHR_nsN9N5BA9MzdOoGWX4ZZD9AgD6wK2NaRq_j51sDt3wpGNqtHoDoxtoMKDqu9M7kRD2BWzJ9NuTBT84cSqUVbf01p7BqEzzOA0U0slOuvLmWAjL3SotNRXGyEPcp4ZyPbXSHFMQYQ-YZIUa6YKFI36JGjeRWr7KuGj1nvBKaWdQS5tKa_eRLsRAXh_GwiSIYChVopsVUPPdSuB9JPTUgU80YaZoTXZ9NAfmu0JBYIPH4Kd86n_nqh0QsHaIb4opboQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی: ۷ شرط ایران به آمریکا اعلام شده و آمریکا راهی جز پذیرش آن ندارد
@Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/463091" target="_blank">📅 22:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463090">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نقض پرواز ممنوع در محل اسکان ترامپ و اعزام اف
-
۱۶ به منطقه
🔹
هم‌زمان با اقامت دونالد ترامپ در نزدیکی کمپ دیوید، یک جنگنده اف-۱۶ امروز شنبه پس از ورود یک هواپیما به محدوده پرواز ممنوع، به این منطقه اعزام شد.
🔹
بر اساس بیانیۀ نیروی هوایی آمریکا، این هواپیما حوالی ساعت ۷:۵۰ صبح به وقت محلی رهگیری شد.
🔹
در جریان این رهگیری، اف-۱۶ مُنَوَّر (flares) شلیک کرد که احتمالاً توسط ساکنان منطقه قابل مشاهده بود.
@Farsna</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/463090" target="_blank">📅 22:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463089">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc83b27e7.mp4?token=XjWGOKzPRsTu7l_yROFLY5UVIVO9dUmRlmTGmu8wze_9fFfYaf5YV8ssSYo9zff5r2QhOwUhW3Sb73US4XvikCix8MKaN_PHwDUNILUpMhyHV7IADsRTDNWy_LujGUw8E_EFfnT1xlbRsmpcwS1kXBzI8Ek17-8hQ62cZIU6rhfAObT_gjTYPTL6FEqZ9uNUKQKYwZ-JLKDMrfpj_QvZ-MMConP_d38-3OftN_K-_ByccZeTCmx_Tf-wnKy60eCQdbXRQsWvN-VaO_gct8e_kAQH5eN454MEjZCK4DEmp32-ENSxe97EdAd0ZDfbrKwdf_ttmYvCJooceU9pd_OxHCD0gCfB8a3qtoOTzux_c_sHU95py_KeVa_Ja5VaL17KChvLKSYquSAdHuia96_U4ZhMoGqyDaaXvZw-Zy0ilMte7zvjh8FBujSYWpJkbnPiqvqBlJLQh3kEtnCYvVYJbzHiZRfGP-m8HfxTRIIMdgGne43VdnNRM6cIclp7jfgQZgI3cPrmb4CAtsMqbAUA8kC-sgZsMRPdRj8sRblS89b_0Y5mfSOir7ukvDTIOAejuptd8eaqBaIxeH-PBHAL0XQs6F8rYb41PJ4FKkaBhKUISihQR3Os2a5y1O59B__YThhV2llpmntjz7de9r0IWSk-eaDHeXejDU10kiwqzGI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc83b27e7.mp4?token=XjWGOKzPRsTu7l_yROFLY5UVIVO9dUmRlmTGmu8wze_9fFfYaf5YV8ssSYo9zff5r2QhOwUhW3Sb73US4XvikCix8MKaN_PHwDUNILUpMhyHV7IADsRTDNWy_LujGUw8E_EFfnT1xlbRsmpcwS1kXBzI8Ek17-8hQ62cZIU6rhfAObT_gjTYPTL6FEqZ9uNUKQKYwZ-JLKDMrfpj_QvZ-MMConP_d38-3OftN_K-_ByccZeTCmx_Tf-wnKy60eCQdbXRQsWvN-VaO_gct8e_kAQH5eN454MEjZCK4DEmp32-ENSxe97EdAd0ZDfbrKwdf_ttmYvCJooceU9pd_OxHCD0gCfB8a3qtoOTzux_c_sHU95py_KeVa_Ja5VaL17KChvLKSYquSAdHuia96_U4ZhMoGqyDaaXvZw-Zy0ilMte7zvjh8FBujSYWpJkbnPiqvqBlJLQh3kEtnCYvVYJbzHiZRfGP-m8HfxTRIIMdgGne43VdnNRM6cIclp7jfgQZgI3cPrmb4CAtsMqbAUA8kC-sgZsMRPdRj8sRblS89b_0Y5mfSOir7ukvDTIOAejuptd8eaqBaIxeH-PBHAL0XQs6F8rYb41PJ4FKkaBhKUISihQR3Os2a5y1O59B__YThhV2llpmntjz7de9r0IWSk-eaDHeXejDU10kiwqzGI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری بروجردی‌ها در حماسه ۱۲۳ خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/463089" target="_blank">📅 22:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463088">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/012b259527.mp4?token=kA0qZh3-t5SxDsNLkHgibFHPfw3JeOUrUrLUQQZKVsCimYhKkxFtDAb5fOwmR-sak7C-kvDtsoGibeQGhKfd_5XW9-NymV8qItuFdNke7HVSIv-7cVXiQ0A7IFn4bDhxbzlWSYEledbSQI5NHzsJj36GTDWUb-fJ17YtE9N8Mhkm5cIWrA4bISvuLWZ9IlYbGD3O2LXtWwwCMdk_LzbdNG2ujBTUmc1hVu-foCLnq_Muw6PUBY6S22ZjYIWi2vlpWtTarpSOLkWPB11DtaGnpixZ81UPcYgC4uR46mW5hMcacdgBsiARtYstpwPHhf8goK4rA5IwAYt4PE4X3aoLFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/012b259527.mp4?token=kA0qZh3-t5SxDsNLkHgibFHPfw3JeOUrUrLUQQZKVsCimYhKkxFtDAb5fOwmR-sak7C-kvDtsoGibeQGhKfd_5XW9-NymV8qItuFdNke7HVSIv-7cVXiQ0A7IFn4bDhxbzlWSYEledbSQI5NHzsJj36GTDWUb-fJ17YtE9N8Mhkm5cIWrA4bISvuLWZ9IlYbGD3O2LXtWwwCMdk_LzbdNG2ujBTUmc1hVu-foCLnq_Muw6PUBY6S22ZjYIWi2vlpWtTarpSOLkWPB11DtaGnpixZ81UPcYgC4uR46mW5hMcacdgBsiARtYstpwPHhf8goK4rA5IwAYt4PE4X3aoLFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور تهران بزرگ: تردد کامیونت‌ها و وانت‌ها از ساعت ۶ تا ۱۰ صبح روزهای یکم تا ۸ مهر ممنوع است
@Farsna</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/463088" target="_blank">📅 22:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463087">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f182971d87.mp4?token=kStC4BuJmcStzRQNHwbqfH7KngbXOaXCT_EjGm5gCQQMOYVIXixXA9XeC-iYcuyzS6djmN5jaJ1p1qiXuF6YxOU520uJYilEF26L1jTZErQYikasGWqn1BfQ0YrCiAruyo56G-4G7lbmr-uC63vnKJ80lKjyhSKSjZhTRhl1yzBEFx95rOrijaPYEPItamlSrXRla9wdjHL1Z50DRr_4jkGhjewFxehCRJU5y_fn6pzzc0kJhRZKs4Ofd10Frx1AkNyvRhYDozf1SmU5Weo6_Dr_V7L4UJGdJDkJKpihCekEHzZIoA_QC_1saG5hSslhKecjx2NxTmEalIRvhOVbEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f182971d87.mp4?token=kStC4BuJmcStzRQNHwbqfH7KngbXOaXCT_EjGm5gCQQMOYVIXixXA9XeC-iYcuyzS6djmN5jaJ1p1qiXuF6YxOU520uJYilEF26L1jTZErQYikasGWqn1BfQ0YrCiAruyo56G-4G7lbmr-uC63vnKJ80lKjyhSKSjZhTRhl1yzBEFx95rOrijaPYEPItamlSrXRla9wdjHL1Z50DRr_4jkGhjewFxehCRJU5y_fn6pzzc0kJhRZKs4Ofd10Frx1AkNyvRhYDozf1SmU5Weo6_Dr_V7L4UJGdJDkJKpihCekEHzZIoA_QC_1saG5hSslhKecjx2NxTmEalIRvhOVbEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگاه آموزش احیای قلبی در مترو صادقیه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/463087" target="_blank">📅 22:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463086">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a181082b54.mp4?token=Yc8olTJ7MZEgklvhi2tZulmiy_GG2W4hAlLt0U9bxX22hwEDYjMcJToLOHLu93JodkqmZdUfjaoy9mBhJitDyyF59_Y-gVv7EptpNCfoLNbhV55m8oheDE_J7odxnhG5AedXDdszxgz8G7e-CvHS8pBsFPHy3ggkOO6phtD4Jdq3DH1GnuOBB_v4lwebhwkJApQyXAfr7PUXhTmznm3jBQmgtCJNIxUUoO-vFAUuxGnJUa2zMHx0vbIZzpieGSOKPihRcfdZ97jnGUdN8fVTObbvjFZz-iilGk7ZYzM_2oigbD7XJ46oJerN1GBKOSys3m5LcuH6ERdWxcbdvGiPn4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a181082b54.mp4?token=Yc8olTJ7MZEgklvhi2tZulmiy_GG2W4hAlLt0U9bxX22hwEDYjMcJToLOHLu93JodkqmZdUfjaoy9mBhJitDyyF59_Y-gVv7EptpNCfoLNbhV55m8oheDE_J7odxnhG5AedXDdszxgz8G7e-CvHS8pBsFPHy3ggkOO6phtD4Jdq3DH1GnuOBB_v4lwebhwkJApQyXAfr7PUXhTmznm3jBQmgtCJNIxUUoO-vFAUuxGnJUa2zMHx0vbIZzpieGSOKPihRcfdZ97jnGUdN8fVTObbvjFZz-iilGk7ZYzM_2oigbD7XJ46oJerN1GBKOSys3m5LcuH6ERdWxcbdvGiPn4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم مشهد در ۲۰۳ شب قرار عاشقانه نیز با اقتدار حضور یافتند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/463086" target="_blank">📅 22:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463085">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qa-59MMyX_VZC6vraO0l6cq-pHFxIwCGggz_UwY_Tct1s5zYHHNB1o6HRRQj5dK-OXojj8jD0e9Xgem9YzSCHehOUvPdNycyz0d1gf3dRLTVQeYerHH4c4j87_21fJzAHltLCEz_NiZZEMdHA59VAHf0kuMoHRHXw2v2gvAGgnt_XmnqO_JYaaHXPo0k8gsEouMOzDOUO50Dj9qRBwObm27r8MX_717AE2Dyhu1eME9bmkuWygWRs-0Ho7YgxwqUXKDw8N2Obl800AMtYiKW855ruJuOkNW4Fbr4bDsOG6n4Eraug6d2HnlkI3yFFlQhjRZeI_GBmvatdIaUL0HTrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل حزب‌الله لبنان: مقاومت تنها راه مقابله با صهیونیست‌هاست
🔹
شیخ نعیم قاسم: مقاومت با تمامی اشکال آن همچنان تنها راه پایان دادن به اشغالگری و آزادسازی خاک لبنان است و همه راه‌های دیگر تنها اتلاف وقت است.
🔹
ما در لبنان گزینۀ مقاومت را آزموده‌ایم و دریافته‌ایم که صرفا این راه اراضی اشغالی و مردم لبنان را آزاد می‌کند؛ هیچ‌گونه برابری نظامی با دشمن وجود ندارد، اما می‌دانیم که صاحب حق و صاحب این خاک هستیم و باید به هر قیمتی مقاومت کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/463085" target="_blank">📅 22:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463084">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎥
ایرانِ مقتدر از نگاه دانشجوی آفریقایی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/463084" target="_blank">📅 22:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463083">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4kyjB1m-7gb_DkAz1RlSFpHtFH-GB-TzTA-DWqhYRI8XKCaqLgbv-uPfBPB7LIuosOok00SyxvGp0CJbc02zQdUIB0_797F5z0KauezPG6CFA3jWIz9QwhlBibtDn174REUarHiojf1Xu61P1xETLxVcc3aVaQbMvM5_DznW5_J4dyYvE-O925L-5eHRFbWoLAErCGacF-tJ4kQsJ-tvnS-q7-h0a9UY2cx9Xj3O-5PGklz-k5ERu8mNy5YfYtbNb7PF3TEpkiqNg2xQQZI0Ehtx5vjU2fK1EvcIaG48_4fBM13noOvdT1tlcdTcdHDymK0yHyUJ1kp3iy7jjAA5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نامۀ امیدبخش امام عسکری(ع) به شیعیان
@Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/463083" target="_blank">📅 22:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463082">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519cdf4100.mp4?token=CDXNjAI3sv8utLKdvoU7mQFW4AkjeZ1Am-_IVqtZ8Pt8P7jQqlevLAeQbGhXmw_2SMzvcXiqoi8LEazrnKq8UriCB0d0Yt_d1QnRPCgl7gopRREHXxGW6NrbRlGlDtyJ4sey7nnI59bXBSU6XruEgRnvhduugW0GOoxJAABj7WXfdAFZIXiR-atXJCJLVw6Skoyg3IZ3nQK45ERi3KsLqhqUYNyE63MlGd1xmrkLDjeZwlqxjiMhSOLXnmNixK-5EE3PfO3n-Oii_X8xe7REhjEDM2nqTK9ziQBYrxscEhGiKz9rDwdtnh9Cj8C_OauZT4vZs0OKsJaeE22Go8HgmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519cdf4100.mp4?token=CDXNjAI3sv8utLKdvoU7mQFW4AkjeZ1Am-_IVqtZ8Pt8P7jQqlevLAeQbGhXmw_2SMzvcXiqoi8LEazrnKq8UriCB0d0Yt_d1QnRPCgl7gopRREHXxGW6NrbRlGlDtyJ4sey7nnI59bXBSU6XruEgRnvhduugW0GOoxJAABj7WXfdAFZIXiR-atXJCJLVw6Skoyg3IZ3nQK45ERi3KsLqhqUYNyE63MlGd1xmrkLDjeZwlqxjiMhSOLXnmNixK-5EE3PfO3n-Oii_X8xe7REhjEDM2nqTK9ziQBYrxscEhGiKz9rDwdtnh9Cj8C_OauZT4vZs0OKsJaeE22Go8HgmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۲۰۳؛ گناباد با عشق ایستاده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/463082" target="_blank">📅 22:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463081">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ادامۀ تجاوز رژیم صهیونیستی به جنوب لبنان
🔹
رسانه‌های لبنان از حملۀ هوایی ارتش اشغالگر اسرائیل به نقاطی در اطراف شهر بنت‌جبیل خبر می‌دهند. همچنین مناطق الطیری، زبقین، میس‌جبل و حاریص توسط توپخانۀ این رژیم بمباران شدند. @Farsna</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/463081" target="_blank">📅 22:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463080">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
یکی حرف حق ما را به گوش دولت برسونه. ما هم به خدا اهل همین خاک و آب هستیم و کارت ملی هم داریم چرا به ما
جامانده‌های سهام عدالت
تعلق نمی‌گیرد؟ این موضوع با هیچ استدلالی قابل قبول نیست.
🔹
با توجه به گران‌شدن بنزین، ما عده‌ای از رانندگان تاکسی با مشکل جدی مواجه شده‌ایم.
مخزن CNG خودروهای ما تاریخ مصرفش تمام شده
و به همین دلیل دیگر
معاینه فنی
صادر نمی‌شود. برای تعویض و ثبت‌نام مخزن مراجعه می‌کنیم اما می‌گویند این خدمات به تاکسی‌های شهری تعلق نمی‌گیرد و فقط برای تاکسی‌های اینترنتی ثبت‌نام انجام می‌شود. به
تاکسیرانی
هم مراجعه کرده‌ایم، اما پاسخ مشخصی دریافت نمی‌کنیم و می‌گویند این موضوع از عهده ما خارج است و
باید مخزن را آزاد تهیه کنید
؛ در حالی که هزینه آن برای یک تاکسی پژو حدود ۲۵ میلیون تومان است. پرداخت چنین مبلغی برای رانندگان تاکسی بسیار سنگین است.
🔹
من از
روستای پشت‌تاوه ۷ کیلومتری مرکز شهرستان بهمئی
در کهگیلویه‌وبویراحمد، درخواست پیگیری دارم. از سال ۱۳۹۹ برای روستا لوله آب کشیده شده اما با وجود وعده‌های شش‌ساله برای
احداث مخزن ذخیره،
هنوز این مخزن ساخته نشده است. هر سال تابستان با
تنش آبی
مواجهیم و اکنون ۱۵ روز است آب روستا قطع شده است. در این سال‌ها هر بار لوله مسیر دچار ترکیدگی شده، از مردم خواسته‌اند خودشان با بیل و کلنگ محل را پیدا و تعمیر کنند. این روستا نزدیک به ۵ هزار رأس دام دارد و از تولیدکنندگان فعال منطقه است؛ اما با ادامه این وضعیت، دامداران نیز در معرض آسیب و از دست دادن شغل خود هستند. از طرف دیگر پل روستا در سیل سال ۱۳۹۱ تخریب شده و با وجود گذشت ۱۴ سال و تغییر چند پیمانکار هنوز به سرانجام نرسیده است.
🔹
من یک مدیر مدرسه هستم. درست است که مدارس دولتی نباید از خانواده‌ها شهریه اجباری دریافت کنند، اما یک سؤال مهم مطرح است: آیا
میزان سرانه آموزشی مدارس دولتی با هزینه‌های واقعی اداره یک مدرسه تناسب منطقی دارد
؟
🔹
د
کل همراه اول روستای گزگر
در شهرستان دلگان استان سیستان و بلوچستان به‌دلیل سوختن یکی از قطعات، حدود
دو هفته است که از کار افتاده
است. با توجه به اینکه هیچ اپراتور دیگری در این منطقه پوشش ندارد، تمامی ارتباطات تلفنی و اینترنتی روستا قطع شده و زندگی روزمره مردم با مشکلات جدی مواجه شده است.
🔹
در
زاهدان و زابل
برای سوخت‌گیری باید حداقل یک ساعت و نیم در
صف جایگاه‌های بنزین
منتظر بمانیم. این وضعیت برای مردم بسیار وقت‌گیر و آزاردهنده شده است.
🔹
وضعیت
بازنشستگان آموزش و پرورش
در آستانه بازگشایی مدارس و دانشگاه‌ها و هزینه‌های کمرشکن این روزها اصلأ خوب نیست. چرا فقط شاغلین باید کمک رفاهی دریافت کنند؟
🔹
لطفاً گزارشی درباره وضعیت
بیمه بیکاری ملوانان جنوب
تهیه کنید. بسیاری از ملوانان به‌دلیل شرایط کاری و محدودیت‌های موجود، حدود ۶ ماه است که بیکار هستند اما بیمه بیکاری شامل حال آن‌ها نمی‌شود.
🔹
بهداشت منطقه و بهداشت مرکزی
شهرستان امیدیه
طبق نمودار رشد و وضعیت تغذیه، تشخیص داده‌اند که فرزندمان دچار سوءتغذیه است. فرزندم نارس نیز به دنیا آمده و طبق گفته مسئولان باید ماهانه
کالابرگ حمایتی مربوط به سوءتغذیه
به او تعلق بگیرد. اما با وجود پیگیری‌های متعدد اعلام می‌کنند که اداره تعاون، کار و رفاه اجتماعی به‌صورت سیستمی افراد مشمول را شناسایی و برایشان سهمیه کالابرگ در نظر می‌گیرد. با این حال، سه سال است هیچ مبلغ یا سهمیه‌ای برای ما واریز نشده است. سؤال ما این است که وقتی وضعیت کودک و نمودار رشد او در سیستم ثبت شده، چرا هیچ حمایتی شامل حال ما نمی‌شود؟
🔹
مخابرات
بی‌سروصدا و به‌طور مستمر
هزینۀ ثابت تلفن‌های تجاری
را افزایش می‌دهد. ابتدا اعلام کردند هزینۀ ماهانه ۳۰ هزار تومان است، بعد به ۵۰ هزار تومان رسید و پس از مدتی ۷۰ هزار تومان شد. این ماه نیز هزینۀ ثابت به ۱۰۰ هزار تومان افزایش یافته است. سؤال ما این است که چرا این هزینه
به‌صورت مداوم افزایش پیدا می‌کند
و چرا هیچ نظارتی بر این روند وجود ندارد؟
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/463080" target="_blank">📅 22:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463079">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ادامۀ روند تعطیلی پنجشنبه‌ها در استان سمنان
🔹
استانداری سمنان: تعطیلی پنجشنبه‌ها در استان تا پایان سال جاری تمدید شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/463079" target="_blank">📅 22:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463078">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0d98859d.mp4?token=R320-XpDqSKq5dknrXiAHGMqRilJttVXlHBEzjQjT4Tn2JT7ipgGowJzyn809gNm2UvZ8pj45tn355IMnBIKQtqTilH1vervej17g-fHdCEBNK6cKHkKDKH7m0ZJV2iPB6r255GgC_p-Vc-cKys_lpcV0P6LT2BssjBP6EdkIz6atGwQ2utYSm9X1urTtnUEbFHq5UunrFswJsMM3yvYctfkgsFDkr1rhhwlT0vflpryhmlxh29xLrrC4Mp43dKba93HowNq9RLmAzpAjEfpWuRgIWnVo8xxoTqKyMLjTQnzmwA58wPWSHfWIXJdR-CmTQHqr9X1UPYHfO9EiMR5Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0d98859d.mp4?token=R320-XpDqSKq5dknrXiAHGMqRilJttVXlHBEzjQjT4Tn2JT7ipgGowJzyn809gNm2UvZ8pj45tn355IMnBIKQtqTilH1vervej17g-fHdCEBNK6cKHkKDKH7m0ZJV2iPB6r255GgC_p-Vc-cKys_lpcV0P6LT2BssjBP6EdkIz6atGwQ2utYSm9X1urTtnUEbFHq5UunrFswJsMM3yvYctfkgsFDkr1rhhwlT0vflpryhmlxh29xLrrC4Mp43dKba93HowNq9RLmAzpAjEfpWuRgIWnVo8xxoTqKyMLjTQnzmwA58wPWSHfWIXJdR-CmTQHqr9X1UPYHfO9EiMR5Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرکات رزمی باورنکردنی استاد ۸۰ ساله در برنامۀ محفل ستاره‌ها
@Farsna</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/463078" target="_blank">📅 21:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463077">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3d901172.mp4?token=apTdeU4aS-I1zin_WepQjtN1zVc4wKKBUj6osE0ZE3PzE2WpsANFJMQ7HuE6Dz84oCmhQUhLus9KHsXu1g9oCsZYiPeqFxOOPnp5QO1HEPfaELcecw1QfmWZiW2as4WIEDQL4kEjvIp8YQFr00vFDApid_F9CA3MyfChJQOpr-hno0HN4joGUA6OQwAXTsP5pCHmVmpEUKPbZ9sA1GuuUJLb0E5ryDpiCnkCAC8edT6GNvVhU_blELci9TIYn7KXIi4DmVHTIZeu2luNKwcwm7IBJk1EUB4Fsmzi4BAY5WxcZLxARNcJ3pK9DdJfqFNUW56h3NjoG92uyJjAk4oEgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3d901172.mp4?token=apTdeU4aS-I1zin_WepQjtN1zVc4wKKBUj6osE0ZE3PzE2WpsANFJMQ7HuE6Dz84oCmhQUhLus9KHsXu1g9oCsZYiPeqFxOOPnp5QO1HEPfaELcecw1QfmWZiW2as4WIEDQL4kEjvIp8YQFr00vFDApid_F9CA3MyfChJQOpr-hno0HN4joGUA6OQwAXTsP5pCHmVmpEUKPbZ9sA1GuuUJLb0E5ryDpiCnkCAC8edT6GNvVhU_blELci9TIYn7KXIi4DmVHTIZeu2luNKwcwm7IBJk1EUB4Fsmzi4BAY5WxcZLxARNcJ3pK9DdJfqFNUW56h3NjoG92uyJjAk4oEgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  یمن: تأسیسات حساس ریاض و ینبع را هدف قرار دادیم
🔹
نیروهای مسلح یمن: ۲ عملیات نظامی موفق را با موشک‌های بالستیک، کروز و پهپاد اجرا کردیم: ۱. هدف‌گیری سایت‌های حساس در ریاض ۲. هدف‌گیری تأسیسات آرامکو در ینبع
🔹
هردو عملیات با موفقیت کامل انجام شد و آتش‌سوزی‌های…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/463077" target="_blank">📅 21:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463076">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BagGUNtGvSHDazWZQl7c8ZCPGOUg7fpaqYsTVD1O1ais7dBwmtf2vJQvQCR8JCpWht9DJg0ZR3149HYXIxc6ZamakyetvaoLgqNbNLpc-1psKb1-UU9xiSY43Ht12XwKBNtviu-bE100wzPGowAnuKW1tJIalFxdzdnp-thphh4uZ4yLS7WsI8zkANcKiCoAFiUS6wrqwQCY3CUuj9rVCNEaVkKu0n2Pi7jwFVjqsoANTvXfYqFy6R6VFVepIhJqxeQWx58w3XTD0SDBlU1G-50hQHiEY1pqzL2o_xYXBYS0TLPxmIowwtndQFyTi6I9cpG18l8U2N9itv6hNe3uJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع سوخت در فرانسه اضطراری شد
🔹
نشریۀ کوبیسی‌لتر: فرانسه با کمبود شدید سوخت مواجه شده و درحال حاضر ۱۱ درصد پمپ‌بنزین‌های فرانسه بنزین و گازوئیل ندارند.
🔹
میانگین قیمت گازوئیل در فرانسه به ۲.۳۸ دلار رسیده که همراه با قیمت بنزین، در آستانۀ ثبت رکورد تاریخی است.
🔹
مکرون، رئیس‌جمهور فرانسه امروز در واکنش به کمبود سوخت و اعتراضات صورت‌گرفته توسط مردم، جلسۀ اضطراری تشکیل داده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/463076" target="_blank">📅 21:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463075">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe1ded877.mp4?token=cCecEmDonXC_rcmHYZKVOQ03AYk1VCmSF2RAU4sOtcR92QNzyqy5UtD8WJEsJVNCWxMH4ge6NKJLvXn9Kd89GpeaB1c5HSTV4eIvJwBaTchu-NLMBqL5RzOmWAQ5bZZ_K4-2yPL2DtbbOqE4GqfZStwKJrvGYYN1PhavYzUje78cQ-UbcdSWGidgovfs8fecGdC9aJFesLd6J8CUZQbEVqQpesh8xkQS4XpJSM4ooSIO5fFsJg9JXSvRXpssojCEX4X4HTsmHNy3A-yOKydtS8xiTp2RJOF1fZNhoPl9ZPuYccY7_D8EOvE8JOTA4ecsFyXD9XOP6lbLIN4x3gKnLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe1ded877.mp4?token=cCecEmDonXC_rcmHYZKVOQ03AYk1VCmSF2RAU4sOtcR92QNzyqy5UtD8WJEsJVNCWxMH4ge6NKJLvXn9Kd89GpeaB1c5HSTV4eIvJwBaTchu-NLMBqL5RzOmWAQ5bZZ_K4-2yPL2DtbbOqE4GqfZStwKJrvGYYN1PhavYzUje78cQ-UbcdSWGidgovfs8fecGdC9aJFesLd6J8CUZQbEVqQpesh8xkQS4XpJSM4ooSIO5fFsJg9JXSvRXpssojCEX4X4HTsmHNy3A-yOKydtS8xiTp2RJOF1fZNhoPl9ZPuYccY7_D8EOvE8JOTA4ecsFyXD9XOP6lbLIN4x3gKnLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نمای عرش مزین به نام عسکری است
🔹
نصب کتیبه‌های ولادت امام حسن عسکری(ع) در حرم رضوی. @Farsna</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/463075" target="_blank">📅 21:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463074">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868cac2de0.mp4?token=ZjE8vxS01Jg5AK6NsZQLPxpC7l09v-tIIywgbRlUINVZ54-COQg_Qbr52GLH9YbfrHYMn9lDNLwx2R3QEqVIgLeI4X2Ks-AJKjLoLJOlAomaJrrkfN1B8iKn-rdymDkWtbXc3BEU5s2_USIUS5QnnesVhx3_f9ephSdk89fqw0c5PZggB3sYTyLT0Saj_1O-A1DJyXd7V0LVKcyS_jVlgC8ZDWe_K_K38PJq9kUszCmKRC3Dzna0CVr8LzeRYFQEp2XrmwmPfuER9dV-M1sWPnBGQZGOuYWaDw7n1jLLxQAKCRxoahRMcrh5FyqNIYgNO5EAulVLFMkO8tk6S_DW7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868cac2de0.mp4?token=ZjE8vxS01Jg5AK6NsZQLPxpC7l09v-tIIywgbRlUINVZ54-COQg_Qbr52GLH9YbfrHYMn9lDNLwx2R3QEqVIgLeI4X2Ks-AJKjLoLJOlAomaJrrkfN1B8iKn-rdymDkWtbXc3BEU5s2_USIUS5QnnesVhx3_f9ephSdk89fqw0c5PZggB3sYTyLT0Saj_1O-A1DJyXd7V0LVKcyS_jVlgC8ZDWe_K_K38PJq9kUszCmKRC3Dzna0CVr8LzeRYFQEp2XrmwmPfuER9dV-M1sWPnBGQZGOuYWaDw7n1jLLxQAKCRxoahRMcrh5FyqNIYgNO5EAulVLFMkO8tk6S_DW7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور: اگر حذف ارز ترجیحی انجام نمی‌شد، در جنگ آسیب اقتصادی جدی می‌دیدیم.  @Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/463074" target="_blank">📅 21:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463073">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRMS62RF4QAyy5Dx35Mu-ZTvxQynXN1fVgb5SnEQK8ZDTDXiG_VqqnyDqGuGUtz2uiIvo5BfQyJ4yhz7TRwHpNckQYdRdVXqTXGyRGNDmnVYLnZwe2TGgFMzDMWB6V2nKZ511i2mYs05nhCfD5kZg0rw8poGr9feWR0oKYCRVo4doJ-WYxtD1k4NQFz_gMnx69zVd0KO_3KTD2dFS9tt-2-GhnbZG0-3K20iylebV902N00WS0OtBHeCWgpf21y-hUnEcOneaWFdrKQb-OJ_NFWWKN1ZUBNsA4DSPKpkBzODVfMwIs3B3tm3__h6s_yI7-Tw72kn-I2E793AZwKliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو در فرودگاه نظامی خارج از نیویورک فرود می‌آید
🔹
نخست‌وزیر خست‌وزیر رژیم صهیونیستی به‌جای فرودگاه غیرنظامی نیویورک، در یک فرودگاه نظامی در خارج از این شهر فرود خواهد آمد و سپس برای سخنرانی در سازمان ملل به منهتن سفر می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/463073" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463072">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b576d2e002.mp4?token=kP_Fz81Zhh3TW50rR0-eQjsEAxVwzYYrvv2MVHVr2Rhf9MeGuSpEfDozF-rEusVFBs3-j5WzFFcLHRjvkv-932DZvdy1gPpkTnZfnAclWNpaxEFqdysh398NldrcZ7-hCKj3ZDiIyDHUwgQj52mAdUlLqeVKew6Sqe2utrrG3t2JA11GOMes9jJ5Mm-fiT-NLtQGWx-fIDm-cvRKBaMtARXN_KgpZUMOqil4u01OjXVATtI7iKY5Wz5iyNtXmffzToKWCBmbFNdhz3pzfF_ckDiKrW25jSudzk9HF0bIjHwxZCWRI2JxC-uyw7TchElWEuCNJYszaCjDoExrF7_lKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b576d2e002.mp4?token=kP_Fz81Zhh3TW50rR0-eQjsEAxVwzYYrvv2MVHVr2Rhf9MeGuSpEfDozF-rEusVFBs3-j5WzFFcLHRjvkv-932DZvdy1gPpkTnZfnAclWNpaxEFqdysh398NldrcZ7-hCKj3ZDiIyDHUwgQj52mAdUlLqeVKew6Sqe2utrrG3t2JA11GOMes9jJ5Mm-fiT-NLtQGWx-fIDm-cvRKBaMtARXN_KgpZUMOqil4u01OjXVATtI7iKY5Wz5iyNtXmffzToKWCBmbFNdhz3pzfF_ckDiKrW25jSudzk9HF0bIjHwxZCWRI2JxC-uyw7TchElWEuCNJYszaCjDoExrF7_lKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور: اگر حذف ارز ترجیحی انجام نمی‌شد، در جنگ آسیب اقتصادی جدی می‌دیدیم
.
@Farsna</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/463072" target="_blank">📅 21:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463071">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6747c5628.mp4?token=C7e_Gs8ZinQmq-_HHcCrUZAxthU0eljuMqQpkYBUUn8RSvoXeWaHIrK1b2oHG5bdoC2iDQIW8v1qIpSEmKCxefMEtFdPRdbLOlppVS4lcLd7ev-G1kFmJOHTYVE0BYNNCVsuEB0LLvOTnroAzKA7_wAQ2_a1RiLVhhdybcYi8Oy29lVPYd26VgpvCsNJZYdsjLeQQ5JTqwHAfrJdmDPwgr20hY7YSKRJovfID0xFE41ue4Plzl0yo-rsX1K5VyccFzzIwT-kJncDdY7JQUFAyZYbLrvi-Jou_BLf7jQewmWsaCULiQC-unNSX4oon6NPai2YWCN0zCyupe1fglB1yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6747c5628.mp4?token=C7e_Gs8ZinQmq-_HHcCrUZAxthU0eljuMqQpkYBUUn8RSvoXeWaHIrK1b2oHG5bdoC2iDQIW8v1qIpSEmKCxefMEtFdPRdbLOlppVS4lcLd7ev-G1kFmJOHTYVE0BYNNCVsuEB0LLvOTnroAzKA7_wAQ2_a1RiLVhhdybcYi8Oy29lVPYd26VgpvCsNJZYdsjLeQQ5JTqwHAfrJdmDPwgr20hY7YSKRJovfID0xFE41ue4Plzl0yo-rsX1K5VyccFzzIwT-kJncDdY7JQUFAyZYbLrvi-Jou_BLf7jQewmWsaCULiQC-unNSX4oon6NPai2YWCN0zCyupe1fglB1yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز اجتماع ۲۰۳ مردم کرمان در میدان کوثر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/463071" target="_blank">📅 21:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463070">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f395b0844a.mp4?token=XoV5A0u_qYWNajrfCbhIokCmG4S0A5Po3ar8LXWO_xYnI9FGUywWPwnCyTqXIOLGZUfafQbXBr8xI-zMV2NWgT9PHDm_JI1krWuBiC5HERsABIV1V9_1zvWVnL3pouN8C289VXQpSq6SZDB2RROFGHXfHgKtuEz-S8ZH3JfzmI6D9y6bg7rZhmmvVwBTdFMBHs7wTiEdqSCSluIPKIT7N2b2EU5ZjF5fW47Sqz2O7S_lAyhHzFwTVamMmUZpKRiS1LmJHPYJVKCr-368w9RAgkYmgcoK6dJDQtkl3kQtJicmb6pFF-R91t-ymJ55KCGF5ybaOLknCrZt782MYFfjQQ_q9p1Qm4RnxerhMLZVS2NILy-X8vrNu8P_4JfNGmcKwCKkK3CALfWmTjXBm19pjdXQ1J5f1er0QC8iHi6kklykpcgikARXIdCQWw9dM_Dq2S8SccNoP01jblLNnVuHLMpYsDpprv_AxV96-Hg2AUdB6-zAw8UNvD1VjUouI5Lf1lNLNrmhEe7WV4YWPDlmi3-ILV_tpfoMTKdOZd8HW0HCqzd5vGUzrpiz1DxV0HI89Fa_D59sVzABvbWMxb6_KcEoVclEvORRcN6QnmKLmjVLAWYYClbzw9UvHGbE01UBiqWjLr9YY__mO3rG2SGzeSu7EYcvmvgJ6A9HWewAeO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f395b0844a.mp4?token=XoV5A0u_qYWNajrfCbhIokCmG4S0A5Po3ar8LXWO_xYnI9FGUywWPwnCyTqXIOLGZUfafQbXBr8xI-zMV2NWgT9PHDm_JI1krWuBiC5HERsABIV1V9_1zvWVnL3pouN8C289VXQpSq6SZDB2RROFGHXfHgKtuEz-S8ZH3JfzmI6D9y6bg7rZhmmvVwBTdFMBHs7wTiEdqSCSluIPKIT7N2b2EU5ZjF5fW47Sqz2O7S_lAyhHzFwTVamMmUZpKRiS1LmJHPYJVKCr-368w9RAgkYmgcoK6dJDQtkl3kQtJicmb6pFF-R91t-ymJ55KCGF5ybaOLknCrZt782MYFfjQQ_q9p1Qm4RnxerhMLZVS2NILy-X8vrNu8P_4JfNGmcKwCKkK3CALfWmTjXBm19pjdXQ1J5f1er0QC8iHi6kklykpcgikARXIdCQWw9dM_Dq2S8SccNoP01jblLNnVuHLMpYsDpprv_AxV96-Hg2AUdB6-zAw8UNvD1VjUouI5Lf1lNLNrmhEe7WV4YWPDlmi3-ILV_tpfoMTKdOZd8HW0HCqzd5vGUzrpiz1DxV0HI89Fa_D59sVzABvbWMxb6_KcEoVclEvORRcN6QnmKLmjVLAWYYClbzw9UvHGbE01UBiqWjLr9YY__mO3rG2SGzeSu7EYcvmvgJ6A9HWewAeO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جان‌فدا؛ کابوس رسانه‌های معاند
@Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/463070" target="_blank">📅 21:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463069">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fjsq3y5xvsZ9DAjHrwUQD4Iql-RaYy_ed7FYDpbPd6W7RKAWM4FyEqD48vQzkWy91sI9NRGYPrhL7l4S_qYmxTCMc9ZO1630fA6Ek0vdA3VXnsAcNmhX13RtpV46It-pSHI_DBdqxjfzjg4JUilwjEcZotFOlWkYVRJKTXV5ljpBE4kiKqJ4hev0llZ7qym1T5m0w7WqLLYFSOrhNOuBpC8fMvFRbaIwJMR54UYn7vuegZQfsiGCABo1Ok5mPiWtLNl8ya7HmJg62WSYTYdqDYyQcldA9sPec8M-fPuoOoMBUc3vR7vQ1APLSH12UC6qGX4ULLNvkpRFPDO5KnAM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مدیحه‌سرایی مهدی رسولی برای ولادت امام حسن عکسری(ع)  @Farsna – رزق ما می‌رسد هر روز از سوی سامرا</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/463069" target="_blank">📅 21:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463068">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElvFDInVHFUS_wKjtsDKEGh9RqfqVGbmpVYNZhzcYDUGpEE6U9rImmlxVR7OXVtEgufAjGQh3OIuv14qSCS4gRQ0h7eOO8vHTwyqJHrHNASSfZsyI1xcMcI_fH4yBnHk2Ne43oyE9HPHPZNvA2e_ErRBXZjUypopTaVFAWJLcV29vNNBvfFHeDMtNWpdWWx7mR35qQc-4b8xN5MCGXl-mWtyEZ3gIwLA6O0BkHPt3LSMdBDtQLvIThmpOc5GpT0rMpJHDOXL4EE0YHQNhLl8DIw744Hx28gijpWP8OoJOYESVPrTKxoCOVl3Oyu8tKMi3ZyF3nnAU1ZM5gS_8ehvuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: نیروی هوش مصنوعی [در ارتش آمریکا] تشکیل می‌دهم
🔹
رئیس‌جمهور آمریکا: درحال تشکیل نیروی هوش مصنوعی هستم؛ درست مانند «نیروی فضایی» که در دوره اول ریاست‌جمهوری‌ام تشکیل دادم.
@Farsna</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/463068" target="_blank">📅 21:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463067">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634883a692.mp4?token=gAwDYq39WjWmdDSNpv9r-Gapndot1dXNB1UbE7yCjnjie4Ud9c9f8bD0Pvm2oXmZGQdl6LWQKIYnVr8RcIpqgTlVj5do8qPo1NfH-t25jc3zlEsOwCR4oaKTPapScqMeIWUOI2YpyAikSQtkpXB-aCo6p3urRg5JFMpJ1S0aeXpFWxzxFFs1eKsNFz9LBJ0aJIjbYZsb8WRudB1S3DwKxF7O1QtpJ6tUeX0_j6-oOR61UxszMY4W1Tp5eVc3KxPnTVJDNHIRzQDSemnY1dxMtj_aXYA1nempidjKUA_qW47lprVvlXUnOsRyLRhFmCvnRDJ8jeQDcTupfe0plnLGlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634883a692.mp4?token=gAwDYq39WjWmdDSNpv9r-Gapndot1dXNB1UbE7yCjnjie4Ud9c9f8bD0Pvm2oXmZGQdl6LWQKIYnVr8RcIpqgTlVj5do8qPo1NfH-t25jc3zlEsOwCR4oaKTPapScqMeIWUOI2YpyAikSQtkpXB-aCo6p3urRg5JFMpJ1S0aeXpFWxzxFFs1eKsNFz9LBJ0aJIjbYZsb8WRudB1S3DwKxF7O1QtpJ6tUeX0_j6-oOR61UxszMY4W1Tp5eVc3KxPnTVJDNHIRzQDSemnY1dxMtj_aXYA1nempidjKUA_qW47lprVvlXUnOsRyLRhFmCvnRDJ8jeQDcTupfe0plnLGlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بنیاد حفظ آثار و نشر ارزش‌های دفاع مقدس: تجهیزات باقی‌ماندۀ آمریکا در اختیار این بنیاد قرار گرفته و در زمان مناسب در موزه‌های بنیاد دفاع مقدس به نمایش گذاشته خواهد شد
.
@Farsna</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/463067" target="_blank">📅 21:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463066">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f5ec30c0.mp4?token=WZQU2eJkZIi9fx2QK2VBI-F1i1P1Dm73fAJuKi2QwbvuSGqB1unh7-o22ZvmbWRdot9BTyHRe1rS_dBatg-FTGTtH0mkx0S5NjQvFFkKT0dR_FbbmivrAc-ED5iyESul-XlUz2oGFM_-vX9ye0yvOe8Or6aTJ71mtV36Wiqs-ISOQw2woguzZWAPsIifgWwtEJUczpG3BnjCThUQJv9HwrbkplMAEMp4mv6UCrh4cM2icYoNcf59VpI_F8TVr3sBEuWq55O8RPwYhIKbgf94XHIF01t1YWc1apyMlxd7Z9edmLegcXhPcT4blX3Sza4aRNC_x71Sf-wPmZ6bmUVgxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f5ec30c0.mp4?token=WZQU2eJkZIi9fx2QK2VBI-F1i1P1Dm73fAJuKi2QwbvuSGqB1unh7-o22ZvmbWRdot9BTyHRe1rS_dBatg-FTGTtH0mkx0S5NjQvFFkKT0dR_FbbmivrAc-ED5iyESul-XlUz2oGFM_-vX9ye0yvOe8Or6aTJ71mtV36Wiqs-ISOQw2woguzZWAPsIifgWwtEJUczpG3BnjCThUQJv9HwrbkplMAEMp4mv6UCrh4cM2icYoNcf59VpI_F8TVr3sBEuWq55O8RPwYhIKbgf94XHIF01t1YWc1apyMlxd7Z9edmLegcXhPcT4blX3Sza4aRNC_x71Sf-wPmZ6bmUVgxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردادن شعار «فلسطین آزاد» توسط رئیس‌جمهور بزرگترین کشور مسلمان
🔹
سوبیانتو: اندونزی باید قوی‌تر شود تا بتواند به برادران و خواهران خود که تحت ستم رژیم اسرائیل قرار دارند، یاری برساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/463066" target="_blank">📅 21:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463065">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a835688527.mp4?token=a67_QTWBCo0SEO_0T6BV2juvDsjMRjBDIATw4_OF6vYOp0EnaMxohvqDgf2pIMk7ror0XoFJl7JGWL91_EKXYKGfuIirqYAHjlrr4JnoOkYDKWAamuf24AxRXmqfTMy2YCRCJnEFlNq7spLBhxE76Mc5bJRN8c51ZMFG1VElUQ4Ij2moZO3AV-i4PZZk71wF0se1Oc4iaVKP0vpxkDQdyFjrj_vSRJucloGWwNt0E8WnF3iVXlgzJt_c63tpDzLDUcZV0iEos6PRbp8ziMWmfoE_ul8xuRoIZSFgbBWCoApYeSN0WB-4clzc_8kSqQDHGk2flDZqEsk3m4M9jSZ3lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a835688527.mp4?token=a67_QTWBCo0SEO_0T6BV2juvDsjMRjBDIATw4_OF6vYOp0EnaMxohvqDgf2pIMk7ror0XoFJl7JGWL91_EKXYKGfuIirqYAHjlrr4JnoOkYDKWAamuf24AxRXmqfTMy2YCRCJnEFlNq7spLBhxE76Mc5bJRN8c51ZMFG1VElUQ4Ij2moZO3AV-i4PZZk71wF0se1Oc4iaVKP0vpxkDQdyFjrj_vSRJucloGWwNt0E8WnF3iVXlgzJt_c63tpDzLDUcZV0iEos6PRbp8ziMWmfoE_ul8xuRoIZSFgbBWCoApYeSN0WB-4clzc_8kSqQDHGk2flDZqEsk3m4M9jSZ3lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای نابسامانی در بازار لاستیک چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/463065" target="_blank">📅 21:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463064">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbfe5e7a1f.mp4?token=nxLZ7T6xrZaPrtd9u8FhOhyzo5XWsJQQ9L53zQm3mucklnmjD7ULjEEuRh8aHd-uZddKpSvdtE76z06nJN0R0CHKAw2cgsIJwvJ_rvOnf-7usVZS31rM7yL-kZryhZO2EGnV0xYvQdL98XHF_SYHWXM-LmWiICZCX3rbiwZ5mSsTAbZct5IQn7Vojn8c6xX01bjfqJ-MZn-ScJgOfC1WxStmrLU2kOssduzqjv5pKBR3vnvMwXTgCFjlh7iQGZofY2hd5Yh4cN1wDmVsOcXjdiVk1LA8_B3B2fIfJXFoLIpF_yV4mek7_4fxd3_oOXQtdBjy1xB0CnZpNcbryqFLMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbfe5e7a1f.mp4?token=nxLZ7T6xrZaPrtd9u8FhOhyzo5XWsJQQ9L53zQm3mucklnmjD7ULjEEuRh8aHd-uZddKpSvdtE76z06nJN0R0CHKAw2cgsIJwvJ_rvOnf-7usVZS31rM7yL-kZryhZO2EGnV0xYvQdL98XHF_SYHWXM-LmWiICZCX3rbiwZ5mSsTAbZct5IQn7Vojn8c6xX01bjfqJ-MZn-ScJgOfC1WxStmrLU2kOssduzqjv5pKBR3vnvMwXTgCFjlh7iQGZofY2hd5Yh4cN1wDmVsOcXjdiVk1LA8_B3B2fIfJXFoLIpF_yV4mek7_4fxd3_oOXQtdBjy1xB0CnZpNcbryqFLMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر علوم: براساس آمار، آموزش مجازی در دورهٔ‌ کرونا، میزان مشروطیِ دانشجویان را ۶۰ درصد افزایش داد
@Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/463064" target="_blank">📅 21:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463063">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/603b33b381.mp4?token=p8jf-kyuUuVCELkO_MKzim8KA5d2ijN-4e_tnY72oCE9T4f5slqhhpcfDwVuNHZZt-JPSNPJ8o8rFO2AUP9Berzs4J73cBK6NIsbVarbZRwLP4Y-1Y7U79bP4_4LrzEq96B-y3lZdItySjjJKXDU2WfGTAde3th0ANNwPG8AzhUK0REeC_KrB9SBEjFZlhzbpkLB4QlAtaMA8-_ZsUC0UWye6uHnOYhNEzv_qK12neuEj8LysY9yxt80iO844IgOSAF97oElceXdM4IrC-xzBAQT6b2xr3pzchxNv8v5NZjymy9CP8EDgeQyQvMDm9CrrXewu5fhtjIyaR5u44BnCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/603b33b381.mp4?token=p8jf-kyuUuVCELkO_MKzim8KA5d2ijN-4e_tnY72oCE9T4f5slqhhpcfDwVuNHZZt-JPSNPJ8o8rFO2AUP9Berzs4J73cBK6NIsbVarbZRwLP4Y-1Y7U79bP4_4LrzEq96B-y3lZdItySjjJKXDU2WfGTAde3th0ANNwPG8AzhUK0REeC_KrB9SBEjFZlhzbpkLB4QlAtaMA8-_ZsUC0UWye6uHnOYhNEzv_qK12neuEj8LysY9yxt80iO844IgOSAF97oElceXdM4IrC-xzBAQT6b2xr3pzchxNv8v5NZjymy9CP8EDgeQyQvMDm9CrrXewu5fhtjIyaR5u44BnCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعدام خائنی که اطلاعات سایت‌های موشکی اصفهان را در اختیار موساد قرار می‌داد
🔹
حسین پدران، فرزند حمیدرضا که اطلاعات سایت‌های نظامی حساس کشور در استان اصفهان را در اختیار موساد قرار داده بود، به جرم جاسوسی و همکاری اطلاعاتی به نفع رژیم صهیونیستی بازداشت و محاکمه…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farsna/463063" target="_blank">📅 21:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463062">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_2uh6spNVKEQdIe6CAjdNpV6gTdMPxVBfuQhbYvhFa9aU6TCy1oEkaKY1MGssM-D1ytAi0yZmflkH77w5OOmSZxtgnTLiQv5Gb3oJPxOHNEUFKCYYyM0RCPIjlWtBSqo3y5VQXlafT3KwmFtCPNIGyhdGA92hlLGeXH0oNlHIiBUjLCj4zIu8F5NYkQPJbPjPQSwoNjKObcv3cyZrOIQQ-1rwug5z36-E-vf3WKMQso37JMdLZjpy5jXYIU2ceTIMnOHmNi9EXUSosmWMHnYP5hZsxhPwFzypUpOm-lugAwxviN2udVRnKANpw_lH2nU5xQHXauupT7F8tdkTJ4sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رهبر معظم انقلاب: بنده قاطعانه اعلام میکنم که ارتکاب هر آنچه به‌ضرر انسجام اجتماعی باشد، ممنوع است.
🔹
بخشی از پیام رهبر معظّم انقلاب به‌ مناسبت هفته دولت
@Farsna</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/463062" target="_blank">📅 21:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463061">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp27Awh7yqFIf00xMZ5KTrAOn5UyiVfDCJaPqTMonzVYC0RKmBcBq9nmrNn3k5m-cKfZG0nRI-550trRYtUxZJt1HZFwVIIfoBycENPKacEQehHmxowhLVMW1SEeaClhbJUBq4uYI9dxbNJZ8jMI7CjRABF6ROB82mCFqUP8YLt-5aDIWIr6uAY6jhNNXKagqpoBcine-dl-PdeemnUXU2mIG2zVXiSxvcILSzTXdkhtCKfRaKNRuXMqVW1vWfIYiesfiI4G0IjMcnfZkKuWOBvq31MZyNRfk7m_oB__1wVB64dlQJ9A8aFrBzeHREIm5pnxOhErOnNLyjRlr2NQdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار چین به آمریکا به‌خاطر تحریم ایران: تلافی می‌کنیم
🔹
نشریه انگلیسی فایننشال تایمز: چین به آمریکا هشدار داد که ممکن است به دلیل تحریم‌های ایران تلافی کند.
🔹
پکن به آمریکا هشدار داده  اگر واشنگتن سرکوب تجارت با تهران را گسترش دهد، تمام اقدامات لازم را انجام…</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/463061" target="_blank">📅 20:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463060">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎥
تصاویر ماندگار شب‌های حماسهٔ مردم شهرقدس
@Farsna</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/463060" target="_blank">📅 20:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463059">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سردار شکارچی: ابتکار عمل در تنگۀ هرمز همچنان در دست ایران است
🔹
سخنگوی ارشد نیروهای مسلح: فرافکنی و ادعای کاذب و مضحک فرمانده سنتکام دربارۀ اسکورت نفتکش‌ها و خروج یک میلیارد بشکه نفت در دو ماه گذشته، یک عملیات روانی شکست‌خورده برای روحیه‌دادن به نیروهای خسته و فرسودۀ ارتش آمریکا و توجیه هزینه‌های گزاف مالی و جانی این کشور در منطقه است.
🔹
این ادعا نمی‌تواند واقعیت خروج ارتش متجاوز آمریکا از منطقه را تغییر دهد.
@Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/463059" target="_blank">📅 20:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463058">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49ce0e763.mp4?token=niwb_SJmqWjcWwCFHSjZ2iTCo5AFt8weMXoOjON0E9jj6NIIQXDqjE1YqHAFzy_m8A5-4tsY3RwXcUWbuuWBxh72hzS9XVvZpX7n2yxu3LbfSWrCBHs-K2Sa9h5jSXcqj9l-ZDReKgdeHHN_3717ERKQj-V85rWdQndtLq8AS8b8mNHIo_2LA1ZsQzurGN3UdXauczmhEVmLkOW3TziqV4KQuLDIhc2SZANc5Y7FBwi8xVueMps0SU-FTvHcqwZ4eNu6M002tIzv73flT2kH5LUAGVW7tYEfb5epntSdKOWQ7undIJQHG-ZD65sluaOriD6PWJN2wXgv20BI_MWnqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49ce0e763.mp4?token=niwb_SJmqWjcWwCFHSjZ2iTCo5AFt8weMXoOjON0E9jj6NIIQXDqjE1YqHAFzy_m8A5-4tsY3RwXcUWbuuWBxh72hzS9XVvZpX7n2yxu3LbfSWrCBHs-K2Sa9h5jSXcqj9l-ZDReKgdeHHN_3717ERKQj-V85rWdQndtLq8AS8b8mNHIo_2LA1ZsQzurGN3UdXauczmhEVmLkOW3TziqV4KQuLDIhc2SZANc5Y7FBwi8xVueMps0SU-FTvHcqwZ4eNu6M002tIzv73flT2kH5LUAGVW7tYEfb5epntSdKOWQ7undIJQHG-ZD65sluaOriD6PWJN2wXgv20BI_MWnqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیین نقاره‌زنی در حرم بانوی کرامت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/463058" target="_blank">📅 20:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463057">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfdf8888ba.mp4?token=dUXSlFyfwhlpNuBLgR-TGjT_wzW2cxni5naBN2p_H7PXosqQZUo6qMBrOx4n08JI5IGlsw7A6K-leIOniSvvKSa692qpzAuZf-F781SqeUWETfVwuWUc0ENoZidPjaBjYod290e4PSbR8iCoJEvDgO_pGKMqPbVGQZjiW7ImUG1TYUnLxFvy_EEhyaUQkvi1F5QWeyPLt9M8FPc8uzIfzEFI8yk1xt17QMiO76Jro3oNButc7YFIB5r3ckCF5Hak-CZiSYo7yPEnzmTX4HuvIYxVroTwab484gR7KdwOyJcXvfrkEoucjp0Y-2anzZh5PRwdagJqOnhlVaGGH9dU2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfdf8888ba.mp4?token=dUXSlFyfwhlpNuBLgR-TGjT_wzW2cxni5naBN2p_H7PXosqQZUo6qMBrOx4n08JI5IGlsw7A6K-leIOniSvvKSa692qpzAuZf-F781SqeUWETfVwuWUc0ENoZidPjaBjYod290e4PSbR8iCoJEvDgO_pGKMqPbVGQZjiW7ImUG1TYUnLxFvy_EEhyaUQkvi1F5QWeyPLt9M8FPc8uzIfzEFI8yk1xt17QMiO76Jro3oNButc7YFIB5r3ckCF5Hak-CZiSYo7yPEnzmTX4HuvIYxVroTwab484gR7KdwOyJcXvfrkEoucjp0Y-2anzZh5PRwdagJqOnhlVaGGH9dU2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانشگاه‌ها دوباره پر از دانشجو شدند
@Farsna</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/463057" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463056">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌  یمن: تأسیسات حساس ریاض و ینبع را هدف قرار دادیم
🔹
نیروهای مسلح یمن: ۲ عملیات نظامی موفق را با موشک‌های بالستیک، کروز و پهپاد اجرا کردیم: ۱. هدف‌گیری سایت‌های حساس در ریاض ۲. هدف‌گیری تأسیسات آرامکو در ینبع
🔹
هردو عملیات با موفقیت کامل انجام شد و آتش‌سوزی‌های…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/463056" target="_blank">📅 20:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463055">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مهر تایید ناسا بر انفجار مخازن ذخیرۀ سوخت ریاض
🔹
داده‌های جدید سامانۀ ماهواره‌ای ناسا وجود آتش‌سوزی در نزدیکی بخش شمالی فرودگاه ملک خالد ریاض را نشان می‌دهد؛ این تصاویر وجود آتش‌سوزی در نزدیکی بخش شمالی فرودگاه را تایید می‌کند.
🔸
سخنگوی نیروهای مسلح یمن سرتیپ…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/463055" target="_blank">📅 20:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463054">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: سفر به نیویورک برای دیپلمات‌های ایران هیچ جذابیتی ندارد اما سنگری است که نباید ازدست داد
🔹
شرکت در اجلاس سازمان ملل حق ماست و ما باید در این نشست حقانیت ملت ایران را فریاد بزنیم. @Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/463054" target="_blank">📅 20:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463053">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: سفر وزیر کشور پاکستان به تهران دربارۀ روابط دوجانبۀ ایران و پاکستان خواهد بود و قرار بر تبادل پیام خاصی دربارۀ میانجی‌گری نیست. @Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/463053" target="_blank">📅 20:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463052">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: اینکه برخی فعالان رسانه‌ای ایران را دربارۀ به‌هم‌خوردن تفاهم مقصر جلوه می‌دهند بی‌انصافی در حق مردم است
🔹
ما درمورد آمریکا صحبت می‌کنیم؛ کشوری که در سال‌های گذشته همیشه و همواره پیمان‌شکنی کرده است.
🔹
خود مقصربینی یکی از نشانه‌های جنگ…</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/463052" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463051">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: اینکه برخی فعالان رسانه‌ای ایران را دربارۀ به‌هم‌خوردن تفاهم مقصر جلوه می‌دهند بی‌انصافی در حق مردم است
🔹
ما درمورد آمریکا صحبت می‌کنیم؛ کشوری که در سال‌های گذشته همیشه و همواره پیمان‌شکنی کرده است.
🔹
خود مقصربینی یکی از نشانه‌های جنگ شناختی دشمن است؛ بعضی‌چیزها به قدری عیان است که حاجتی به بیان ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/463051" target="_blank">📅 20:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463050">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هشدار امنیتی سفارت چین در عربستان
🔹
با تشدید تنش میان عربستان و یمن، سفارت چین در ریاض از اتباع و سازمان‌های چینی خواست، تدابیر ایمنی را تقویت کنند و در صورت دریافت هشدار امنیتی، بلافاصله به پناهگاه بروند.
@Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/463050" target="_blank">📅 20:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463049">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BK8FPidnT5iW1QJPuKP0ByX30S9h0s0hmFs5i4t6MQCZZhJc9BtHapuOohC8zqQ3CyFxeTeo6nXVJ3yEdBc-uNZKLLijd5VUec2LttXHzAbkOrzEBAwEkdsJ1gfGYGgAFtjeekHRzUXibCYSjxXmx1R0Dw-bKqOjODct73xULNwRGt_ZKH_I96rA0PD9Ib_SlA5ty93VV17cUJswitz_rVYzmyEZTIcuedSCnB0PX7342-93zoSFaqjkRJFyaKKGhYNJG0N5MGTi58drE1A2GhkY9P_kW7WPYmiZvaGuZZRMkbXaFOeAZ41OcTi21vtdtdd1DnZEv7o8VfQUl-l5OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رهبر شهید انقلاب: امام حسن عسکری(ع) حزب طرف‌دار خود را نزدیک خودش میداند و میفرماید که میان ما و شما خویشاوندی نزدیک است
🔹
یعنی قوم‌وخویش درجه‌ی یک هستیم، مثل پدر و فرزند، مثل برادر؛ و مؤمن برادر مؤمن است! یعنی ارتباط میان دو مؤمن، پیوند برادریِ پدر و مادری است، نه برادریِ ناتنی.
🔹
مراد از مؤمن کیست؟ آن کس که دنبال راه امام عسکری(علیه‌السلام)  است، این همان ارتباط مستحکم تشکیلاتی است میان امام و پیروانش.
@Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/463049" target="_blank">📅 20:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463048">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حملۀ روسیه به یک کشتی اوکراینی
🔹
وزارت دفاع روسیه اعلام کرد یک کشتی حامل سوخت برای نیروهای اوکراینی را در اودسا، واقع در جنوب‌غرب اوکراین، هدف قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/463048" target="_blank">📅 20:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463047">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار مهمات عمل‌نکرده در البرز
🔹
سپاه استان البرز: با توجه به خنثی‌سازی مهمات‌ عمل‌نکرده در منطقۀ بیدگنه، احتمال شنیده‌شدن صدای انفجار از ساعت ۲۰ امشب تا فردا وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/463047" target="_blank">📅 20:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463046">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6843ddc9.mp4?token=MyhZp2R6KicRqwVKIXiVz29KTSxPsJ1d8YK5PkfGvSVBY3wP18aCVVIQ1xrkmfLXdO7oy3ejR2mpVS3EM2hHIAL-tLPa07LmGlVIbFLRHs5eDv9NU3rWNCr9qbEd5nW7QmN7dRvClHm83RP8ppIzKVywnXA4NLeSgQjt26gjoFw_777ub7cy5ere_9l1rDshVsBROhI2pyUhJS1YxdUmQiuBzznUlNXdcqjB2I1BRRHfwlaUgCB0soQbo_xrZefLjWz1VXyVkxKn13NcJbX-J82R4UzRkcqv4KAiy0rdaBogOzJ8gpdkhmbe9FnTklngVtikt8i8DXr9nlvKrd1F_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6843ddc9.mp4?token=MyhZp2R6KicRqwVKIXiVz29KTSxPsJ1d8YK5PkfGvSVBY3wP18aCVVIQ1xrkmfLXdO7oy3ejR2mpVS3EM2hHIAL-tLPa07LmGlVIbFLRHs5eDv9NU3rWNCr9qbEd5nW7QmN7dRvClHm83RP8ppIzKVywnXA4NLeSgQjt26gjoFw_777ub7cy5ere_9l1rDshVsBROhI2pyUhJS1YxdUmQiuBzznUlNXdcqjB2I1BRRHfwlaUgCB0soQbo_xrZefLjWz1VXyVkxKn13NcJbX-J82R4UzRkcqv4KAiy0rdaBogOzJ8gpdkhmbe9FnTklngVtikt8i8DXr9nlvKrd1F_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسجد جمکران به استقبال میلاد امام حسن عسکری(ع) رفت
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/463046" target="_blank">📅 20:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463045">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTpC6JJKkuuYbJfMkUzhqs1SQ9Vof0T_hRZDZC0tb5E_Ub0d5fki2pxT99hXX0wNltxcQCCGWWLRl3ocgtTdYYtZT9wwQ9thJzNsikHMNpVigeMI2B403oAsHD7eMQ4IHXIU0bUFjhxek44dVMwwieMkkuv6ygAYZsQLLcZqLjHUB6xGyVbIWZlnckJShdT0-Gw9Hx5ZiypqF4f5qMYx64oW5u-y2rsroJFRG7h3YEaTOmn1dwaoHDRZUjg0KXCuoL4lQoNbULzCEadyqn-z98PBMuaOzVjruqwEHpv1irJmORfH2xGvkmlXCyqT_ZlDaQMultL52nGzLeq1_YyEiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان دستاوردهای بریکس را برای سران قوا تشریح کرد
🔹
جلسۀ سران قوا امروز به میزبانی پزشکیان برگزار شد؛ رئیس‌جمهور در این نشست، گزارشی از سفر خود به هند و دستاوردهای حضور در هجدهمین اجلاس سران بریکس را ارائه کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/463045" target="_blank">📅 19:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463044">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8yhP0Z5LwTTrJ8FCP9hfo5pjbroFb3OB4EmpssUvE1BX9oZek-gBr52GEw2AqKCtakHdZWhtWIc9Wxob6he1hE1Yv81b1fUyWGNjYI407IWF4DtFoG3rR97LSTcoB72ZezBzSJSVGguVzvGI47GTKS_A271i3BQ2aKbZxr66JJkA7rD1jQFSrlEoUVaGxqfBOl9ms5-yK3BarUNxoTuo7wOlablR829oaRYgoAPEkcps16CeKrEt_K-e1cq73uTdsYyobtl2ZAv60hv-BeE5DZoT4gZzbYITUuZeEqttzQDLaXpM4Sl-yja9jcfhVOaIL2NawqyqxvrP8bdaL6kQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزمایش «جان‌فدا»؛ کابوس جدید رسانه‌های فارسی‌زبان
🔹
شبکه‌های فارسی‌زبان خارج کشور، ناتوان از سانسور تصاویر رزمایش «جان‌فدایان ایران»، کوشیدند معنای آن را در ذهن مخاطب دستکاری کنند. این رسانه‌ها وارد مسابقه‌ای عجیب شدند تا به مخاطب القا کنند افراد حاضر در این رزمایش «مردم» محسوب نمی‌شوند.
🔹
در این رزمایش، نیروهای بسیج، زنان، کودکان، نوجوانان، ورزشکاران و گروه‌های مختلف به همراه مقام‌های رسمی حضور یافتند. اما رسانه‌های فارسی‌زبان، از جمله ایران‌اینترنشنال، بی‌بی‌سی و صدای آمریکا، در پوشش خبری این رویداد، تمام تلاش خود را به کار بستند تا این جمعیت را از «مردم» به چیزی دیگر تبدیل کنند.
🔹
کارشناس ‌اینترنشنال ابتدا سراغ عددها می‌رود: «۵۰۰ هزار نفر ثبت نام کردند، اما ۳۰۰ هزار نفر شرکت کردند.» اما چند جمله بعد، وارد توصیف اجتماعی حاضران می‌شود و آنها را «داش‌مشتی»، «کلاه‌مخملی»، «لات» و «اراذل و اوباش» می‌نامد؛ تا آنها را از حیث شخصیت اجتماعی، ارزش‌زدایی کند و به زعم خود، هواداران حکومت را افرادی فاقد صلاحیت و شخصیت بازنمایی کند.
🔹
از آن عجیب‌تر اینکه در همین روایت، شرکت‌کنندگان هم‌زمان به دو شکل متناقض معرفی می‌شوند؛ از یک طرف آن‌قدر وابسته و سازمان‌یافته‌اند که حضورشان هیچ ارزش اجتماعی ندارد؛ از طرف دیگر آن‌قدر مهم‌اند که این رسانه‌ها باید ساعت‌ها توضیح دهند این‌ها چه کسانی‌اند و چرا آمده‌اند.
🔸
این، علاوه بر تناقض، در واقع تغییر زمین بازی است. وقتی نمی‌توانند اصل تصویر را انکار کنند، دربارهٔ صاحب تصویر حرف می‌زنند و او را تحلیل می‌کنند.
@Farsnart
_
Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/463044" target="_blank">📅 19:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463042">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ce7c032b.mp4?token=n_LbWlFQFLhB-cJMS2Ux-PTeRjaO-UxKqsKSb1ee4nInv22--810HUrmg3BKBOEfwRMuIQuSuUJLFF2itHs62GVY28mbYQmhPL0oqJ1Z_Ka4f_5LX4MDVm3kvd3HEejsZ-I1rfxDGuo0jIw2H9jv4t_EMaueZdyPKbs7lXQ_n5SNrcpH_7nl94HVeLZFUqFqYtCnAwUwDdGdPqbFluJf_MESX5lArNA8JnjpollvGHGj1rOP4WMq2Y_7MVOQeh1FRaLBJgrL8qA0J5qUKybXL0AM5jHF8MWwKzuANonRWc6eVaxFZfVB5XF8P_8XcGfDuEN54UE_SOWXRNliV8qQKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ce7c032b.mp4?token=n_LbWlFQFLhB-cJMS2Ux-PTeRjaO-UxKqsKSb1ee4nInv22--810HUrmg3BKBOEfwRMuIQuSuUJLFF2itHs62GVY28mbYQmhPL0oqJ1Z_Ka4f_5LX4MDVm3kvd3HEejsZ-I1rfxDGuo0jIw2H9jv4t_EMaueZdyPKbs7lXQ_n5SNrcpH_7nl94HVeLZFUqFqYtCnAwUwDdGdPqbFluJf_MESX5lArNA8JnjpollvGHGj1rOP4WMq2Y_7MVOQeh1FRaLBJgrL8qA0J5qUKybXL0AM5jHF8MWwKzuANonRWc6eVaxFZfVB5XF8P_8XcGfDuEN54UE_SOWXRNliV8qQKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن بزرگ امام زمانی‌ها فردا در پایتخت برگزار می‌شود
🔹
این اجتماع  فردا از ساعت ۱۹:۳۰  در میدان راه‌آهن تهران با حضور محمدحسین پویانفر، عبدالرضا هلالی و محسن عراقی برگزار می‌شود.
@Farsna
-
Link
...</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/463042" target="_blank">📅 19:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463041">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YR_BteDc5yKByYUW49jkkMy_6ilEwynGHzF0nWfiRmrkv4tpJsiHhagMrHdtz4mnVqMni6KmXhLcTwoP8J2JF2k8OLJED8AohaDerrEhZVle2cGHvQ2ZlILrOhYsrAWuE4uYcuHkhE_dWQZZ7SXtpBMCRw2brjfdc0bqNYiE0Rx9YuZBDHlMtz2RTvmly8KPDK_QJqsQnXHzygyf-DgqCwB9VofFabeL9ZuyDPgHtxzBkTuDXC_kHQCkmVbjkGKwj137W-k7ZTKJqAtTXYQuQFIBJM6roiKA3e0tpjp4naZSQ94rzTyrK5LbzarJMwNfqc5O5TlK4Pz1ZBeBPjcc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت کاری جدید ادارات از اول مهر: از ۸ تا ۱۳
🔹
رئیس سازمان اداری و استخدامی کشور در بخشنامه‌ای ساعت کاری دستگاه‌های اجرایی را از ابتدای مهر تا پایان سال جاری، از ساعت ۸ تا ۱۳ تعیین کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/463041" target="_blank">📅 19:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463040">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cae342b8e6.mp4?token=nwj5xGPezRf9h_q7D8upABS08cjG-RRaZvB4A51s0Wosy4aCcbugZY7wF18Fr6G94ymK2WkZSWMfEg2FTMNSm0_klT6SMW2Pweer_JNm3Y1a-bS0_B3pUiIx_nM-2-GtIqlUPqPJeIgQQPQ_sK_NjsP-aHwH15Vw2zoeAihHxtH6Ma0eeUQ9e2Z1mHbHxfi8IT0w82GoaYt2o1M9MI1rssWNb7I8f4HNV_n6YpNMibuqlz_x_vD5kZ-zYHjEMt1kNjJ5oc375QknCrBYAFg1KivqWCAVXSTY7Pe7hXRrYWUDZnyIxMrk7jKNao5M7KxI1Gk62wodqjVOiKOiqCAMnrv9X81Q201TTLdk7hSGguZu1TNRuwE7hOurv3GbpNQGMBbZ7zP7xcdNj_ZR8cjdcredL7QDIutKdfMhrQGqIZNXJ2eZxZ03gyM03B-mp38AbvdP0a2xzKwIvbD3vjehcESvUOzcOqjlr-Oj1fXlMEHfoxnCp2DBFYpKqXilZttEikh3PFxUjHasTJf4so9UlIXc4XbUIixX3PmAVrQbYoF0IEE8AvF0w2j_L-H6xxXggZfE0hyBw2IcpXCJYoqIkOENIwFiOcSGXfoYdUunI6yUT5dAyUBa93jC6thMzd4QrwHIE92awMExLBjqhPPn1ZaZjaqJ4IUp5PFPWX17XaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cae342b8e6.mp4?token=nwj5xGPezRf9h_q7D8upABS08cjG-RRaZvB4A51s0Wosy4aCcbugZY7wF18Fr6G94ymK2WkZSWMfEg2FTMNSm0_klT6SMW2Pweer_JNm3Y1a-bS0_B3pUiIx_nM-2-GtIqlUPqPJeIgQQPQ_sK_NjsP-aHwH15Vw2zoeAihHxtH6Ma0eeUQ9e2Z1mHbHxfi8IT0w82GoaYt2o1M9MI1rssWNb7I8f4HNV_n6YpNMibuqlz_x_vD5kZ-zYHjEMt1kNjJ5oc375QknCrBYAFg1KivqWCAVXSTY7Pe7hXRrYWUDZnyIxMrk7jKNao5M7KxI1Gk62wodqjVOiKOiqCAMnrv9X81Q201TTLdk7hSGguZu1TNRuwE7hOurv3GbpNQGMBbZ7zP7xcdNj_ZR8cjdcredL7QDIutKdfMhrQGqIZNXJ2eZxZ03gyM03B-mp38AbvdP0a2xzKwIvbD3vjehcESvUOzcOqjlr-Oj1fXlMEHfoxnCp2DBFYpKqXilZttEikh3PFxUjHasTJf4so9UlIXc4XbUIixX3PmAVrQbYoF0IEE8AvF0w2j_L-H6xxXggZfE0hyBw2IcpXCJYoqIkOENIwFiOcSGXfoYdUunI6yUT5dAyUBa93jC6thMzd4QrwHIE92awMExLBjqhPPn1ZaZjaqJ4IUp5PFPWX17XaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این شب‌ها، سطرهایِ آغازینِ تاریخ آیندهٔ ایران است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/463040" target="_blank">📅 19:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463038">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0a202b5e3.mp4?token=EllFrVJf3gfFu2P7s-sASNSWIyi5Iq-ZanyFS9l0UCNe7IQMnmMr1vD9p7Pww_xRYVWeXZfuIF7NjLx8QjqbWMNSDFDl4V7Rzeh-7x2lVRn973NsQyLlPZBsqkY9JFK3GjhQC9vCWmDW5JicQzlGlhLtnBV4-gq0bCa-vUczleQh0_HHPNQn6V2IDR-LRsnAxAko5lNmvWBLqd6ECkH7ucmiGV-sdJC03mx-hIrSvgwClDcZpJkiskCyR7TRst4DzNiXdzrEMK8wMlqp8lL3GZ6wf1J2svoqBWhjCQjlg97lFKAAgDizfu-1CueyGYkO3FamUzsG2Ph2p5Hf5Zr1xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0a202b5e3.mp4?token=EllFrVJf3gfFu2P7s-sASNSWIyi5Iq-ZanyFS9l0UCNe7IQMnmMr1vD9p7Pww_xRYVWeXZfuIF7NjLx8QjqbWMNSDFDl4V7Rzeh-7x2lVRn973NsQyLlPZBsqkY9JFK3GjhQC9vCWmDW5JicQzlGlhLtnBV4-gq0bCa-vUczleQh0_HHPNQn6V2IDR-LRsnAxAko5lNmvWBLqd6ECkH7ucmiGV-sdJC03mx-hIrSvgwClDcZpJkiskCyR7TRst4DzNiXdzrEMK8wMlqp8lL3GZ6wf1J2svoqBWhjCQjlg97lFKAAgDizfu-1CueyGYkO3FamUzsG2Ph2p5Hf5Zr1xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادامۀ تجاوز رژیم صهیونیستی به جنوب لبنان
🔹
رسانه‌های لبنان از حملۀ هوایی ارتش اشغالگر اسرائیل به نقاطی در اطراف شهر بنت‌جبیل خبر می‌دهند. همچنین مناطق الطیری، زبقین، میس‌جبل و حاریص توسط توپخانۀ این رژیم بمباران شدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/463038" target="_blank">📅 19:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463037">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9aiuM1Gtb11szs1Kctj9Qe0SjIgl7gb-KZVi0JaB-2ToyZoGTZAYAABz75fnsCnoPy7o842k3bqOnQeAjxYduyYKseEqWnQEg2ex_YMbbG_5qwXOTXXV3gyRMGB4yNocsXIvkEXxNTUJWPaWb3nfjd9Hk1v_YWW8Xqlnaz-jKY4Im2f1EBuVTy1l-lFRciV3shC6kx7w84kDAoHZw1fExXNTFK981nXFljNyWTlQiByO4zX0ILijd1vXhgnfi8BNqsj8myY1hxDJh-cSEHRTbaV4PXpsMfasO1vwPsw5ILu7Zl-xsi4vqvFKTfNMhfOkZjLZ3bl9wngGElViE3xRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور کابل‌ها از تنگه هرمز منوط به مجوز ایران می‌شود
🔹
نایب‌رئیس کمیسیون امنیت ملی: مادۀ ۱۰ طرح راهبردی تأمین امنیت هرمز به زیر و بستر دریایی، ازجمله عبور کابل‌ها و تجهیزات انتقال داده‌ها اختصاص دارد.
🔹
این ماده در یک کمیتۀ ویژه باحضور مسئولانی از وزارت اطلاعات، وزارت دفاع و معاونت حقوقی رئیس‌جمهور با درنظرگرفتن منافع ملی و تمامی ابعاد به تصویب رسید.
🔹
براساس آنچه به تصویب رسیده عبور کابل‌ها و سایر تجهیزات مرتبط با انتقال داده‌ها از تنگۀ هرمز، منوط به موافقت مراجع ذی‌صلاح جمهوری اسلامی ایران خواهد بود.
🔹
در متن این قانون پیش‌بینی شده که جزئیات اجرایی این فرآیند در آیین‌نامه‌ای دقیق تعیین شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/463037" target="_blank">📅 19:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463036">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwCugZonwx3V8eW0vI64TskABOR8KAAE5yRzcP4Uh9Vx0idkAutbBU7qajcL8ftxwBDd_JYcYYZGQs8PKxvd-7U5ypTbgR-OoM3rPjvhhZa4kaYfnjLKpT2JBpXooD2N27sUXSp1bd9rGGrMOGosIsKMbViGc-Rfds60TBmBUhlu4qEgENaMRMMQpElOTox8hC0K_3y8Bqw5cYIObxVxd1Kmfk767pHZ9YAZIBwGPo8lfdpqv6o_lyiPzSl512rF5UXa_BLBg6JMhsL8IDzF1M6OgBE9GY14FCekdYVbL-P9augd1xT6jZJxoFMHmc1Tpa01IzjqIWvxrQ4vGWU-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعده‌های بنزینیِ ترامپ دوباره انتخاباتی شد
🔹
آمار انجمن خودروی آمریکا نشان می‌دهد که متوسط قیمت بنزین این کشور امروز به ۴.۴۷ دلار و قیمت گازوئیل به ۶.۴۸ دلار در هر گالن رسیده است.
🔹
این قیمت تنها ۳ سنت با اوج قیمت زمان جنگ با ایران فاصله دارد اما قیمت گازوئیل در تاریخ بی‌سابقه است.
🔸
پیش از حملهٔ آمریکا و اسرائیل به ایران، قیمت هر گالن بنزین ۲.۸۰ دلار بود و ترامپ پیش از انتخابات ۲۰۲۴ هم گفته بود یک سال پس از به قدرت رسیدن آن را به زیر ۲ دلار می‌رساند حالا هم مدام می‌گوید که «به محض پایان جنگ با ایران قیمت‌ها پایین می‌آید».
🔹
این درحالی‌ست که نظرسنجی جدید فاکس‌نیوز نشان می‌دهد که ۷۱ درصد آمریکایی‌ها معتقدند ترامپ راهبرد روشنی برای پایان دادن به جنگ با ایران ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/463036" target="_blank">📅 19:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463035">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: اقدامات آمریکا و اسرائیل این اجازه را به ما می‌دهد که از معاهدهٔ منع گسترش سلاح‌های هسته‌ای (NPT) خارج شویم
🔹
هنوز تصمیمی برای خروج از NPT نگرفته‌ایم و این موضوع به رفتار واشنگتن بستگی دارد. @Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/463035" target="_blank">📅 19:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463034">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: ما همچنان به فتوای رهبر شهید انقلاب پایبندیم و دکترین هسته‌ای خود را تغییر نداده‌ایم، اما نمی‌دانیم در آینده چه پیش خواهد آمد.  @Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/463034" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463033">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: ما همچنان به فتوای رهبر شهید انقلاب پایبندیم و دکترین هسته‌ای خود را تغییر نداده‌ایم، اما نمی‌دانیم در آینده چه پیش خواهد آمد.
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/463033" target="_blank">📅 18:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463032">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFiwHmpN0KMkwfXp7eD45gZQSKh79eVXaBak8nk6_5JSefL_23K-o4q5iDgYNvHet872cT5WPo92P5h6RpfYpDVvJ5G8cIJNWOGlJ1aTnH6g0aqe7E5uJ-DXskoRQ0CUbiBEWw35jRNbbqEUYS5c0D3JcpdBM-BK_0ZsZDEzZd3902B5HG3eRO2TBl3dGJ_XAaNFYkqPXeCpUv8xrhHxgEcnSjNRVxvoSyUZz8DQrYdxN8dhT23bpw4YDoQvJ5qBgERE9fdkJU3xxbVqMZ0xSnXsJ2b13AhCRe69aMezRm1jjIDv-BMlCY5dPQBD-ZWsvxo8Um5a8Ue5LssuC2CwGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار ارز زیر فشار واردات خودروهای لوکس
🔹
معاون اقتصادی اسبق بانک مرکزی: واردات خودرو با اقامت خارج از کشور به بازاری تبدیل شده که برخی نمایشگاه‌ها در ازای اقامت افراد، پول پرداخت کرده و ثبت سفارش و واردات خودرو را انجام می‌دهند.
🔹
ارز واردات خودرو از کف بازار تامین می‌شود نه ارز خود اشخاص مقیم خارج؛ این درحالی است ما در شرایط جنگی قرار داریم و بعضا برخی کمبودهای دارویی به وجود آمده است.
🔸
وزارت صمت اخیراً واردات یک خودرو برای ایرانیان مقیم خارج را بدون نیاز به تأمین ارز از سوی دولت مجاز کرد با این شرط که منشأ ارز مورد استفاده طبق مقررات بانک مرکزی تأیید شود.
🔸
بانک مرکزی حالا در مکاتبه‌ای با وزرات صمت مخالفت خود را با رویه فعلی واردات خودروهای لوکس اعلام کرده و گفته در صورت ادامه این روند کد ساتا که برای ترخیص خودروها لازم است را صادر نخواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/463032" target="_blank">📅 18:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463031">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkD6kA9qSR3wRvNa7oqclY1C126buJd3yjv2-34wGMhaJRj4BEG_AznPYuJlA7xDCgz6E0X6X2aloGDzylx2GMF7P1CT_3C_yZTCn13pn_93uActfdhTbmdEQ0j2D4ibQVUcK7S09qPXfV4qTI39cL7gW8SSBjqxUQ9hKnMAa3ZQdzEnxSato-75990eE4bnAqYtyL5zdFzc6O789UyOSsg9NF4vQPH22xQXha42PqBcM-nLQWfP7O88grtOg-IUV-JW-6cMIX1EInZtw2q2lKC4DWcgLd4dF2Cmst9fKVUYo-sVfsPuC7D3eYkP3mANW_2MzVJRtt5diqBYBOUF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرهاد مجیدی، گزینۀ غیرمنتظره مالک نساجی برای نیمکت
🔹
پس از جدایی مجتبی حسینی از نساجی، گمانه‌زنی‌ها درباره گزینه‌های جانشینی او آغاز شده , در این میان از سعید دقیقی و محمد ربیعی به‌عنوان گزینه‌های اصلی هدایت نساجی نام‌برده می‌شود.
🔹
شنیده‌ها اما حاکی از آن است که رضا حدادیان، مالک باشگاه نساجی به دنبال مذاکره با فرهاد مجیدی است تا زمینۀ بازگشت این مربی به فوتبال ایران را فراهم کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/463031" target="_blank">📅 18:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463030">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAC0eAveLYZJAtI93fL1wTumkrEhB_2oxzVGlT_kZRI69KsW4x6snvHBz0hUzdwCMRmOK1LASNEVJ3PSXOrz3zGbNxA6wx5glO9P5XeDMiUexIUb3EBfuH26yF8XwBBLlz5yGJQ6V5EjLsL_i6bt_vTAOv_UfI2R15rVRjdpRslDpk-EQXQhrNOdvpATtybZK4_UssTQ3r2Hs0nx8T8x9sIf3CsR0UitPbWXiIASyhq1rIpzN9tIrGCReVMMZToJnlp9zHFZiBHW09O8VWwDncRyUWVWHzwGgKHmNaV28J7j93pG0bUQHkYRzHYPX2gdX60GtZ0wMNFPCwUwhHmAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر جنوب به شمال کندوان مسدود شد
🔹
رئیس پلیس‌راه مازندران: ترافیک خروجی در جاده‌های چالوس، هراز و سوادکوه سنگین است.
🔹
از ساعت ۱۶، مسیر جنوب به شمال آزادراه تهران-شمال و جاده چالوس در محدودۀ کندوان مسدود شده است.
🔹
حدود ساعت ۲۰، محدودیت یک‌طرفه در مسیر شمال به جنوب جاده چالوس در محدودۀ کندوان اجرا می‌شود.
🔹
جادۀ هراز نیز به‌صورت مقطعی یک‌طرفه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/463030" target="_blank">📅 18:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463029">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">رزق ما می‌رسد هر روز از سوی سامرا</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/farsna/463029" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
مدیحه‌سرایی مهدی رسولی برای ولادت امام حسن عکسری(ع)
@Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/463029" target="_blank">📅 18:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463028">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMMd-fdn3FfXw4ndWNiWqcP43NAfRPJuZ3pawPXuHKCB8IdTo6NvVoY3I8jk4fUgvloyGKA4CiteGooEhVJivoJtESvxW13PA-HFPgfwVbCi3jXLfkfsdo4Bw2ntbyLAXSPzv6asrxK5c8aED140mVGYROvqpjQ4SKsvjvdCK72pEEqw3qXe4sgf8zGZ281TCRpy-u0sRMUUs9PO92qvZ5kaEjiZgGXwwTHlkYKyMAQRCXRCvFTfZDZSr1FCOBstCGBzdaPuEruDWT5NrcfS-H-wh2AqUlcAsRbC99GNZ_oxs0jbZP8sLY7g_h5XxKZT0eI4cGKdMC_adXJ5i9SFBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقایی: اتهامات دروغ و فرافکنی آمریکایی‌ها تازگی ندارد
🔹
سخنگوی وزارت خارجه: سخنگوی کاخ سفید فهرست مفصلی از اتهامات را علیه ایران مطرح کرده است. نکته قابل‌توجه اینجاست که بسیاری از این اتهامات، دقیقاً توصیف‌کننده همان اقداماتی هستند که خودِ ایالات متحده آغازگر، عامل یا حامی آن‌ها بوده است.
🔹
این گریز از واقعیت و فرافکنی، جای تعجب ندارد: «شریران می‌گریزند، بی‌آنکه کسی در پی‌شان باشد.»
امثال سلیمان ۲۸:۱
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/463028" target="_blank">📅 18:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463027">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c85b43e4d.mp4?token=IbLlcqmSHnPdI6LhJ24sjz4ICHQOYpTU5iCZ9wQSC9qPRwGRFVua4_T3EWN-ZnNnTlhos49OvWtlc80BzdXMDSL5EOeqi5M0xZ5Bu1XL-9tUb35zYo7-fZCC8MXQMuvMPDNCW4d5ZOAnJfQNz1yEqJN9V9RiKZtJ8BaOK4Ae0MhkMY_-2YOi2V_YGsvyW_73BlXbRzWQP6QdAPdj9W4E5Tk9BbwSYxTg60FPoCwFs20xc3TyTVJajoRdyYc8EKo3k_btV_8XHQ0K2VztU7pA6rRAC8FtSkGdwxD49LePlHmGTDZ39ysvMLpYArci0liMUjkUIJvqxJjtVth2A5CZ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c85b43e4d.mp4?token=IbLlcqmSHnPdI6LhJ24sjz4ICHQOYpTU5iCZ9wQSC9qPRwGRFVua4_T3EWN-ZnNnTlhos49OvWtlc80BzdXMDSL5EOeqi5M0xZ5Bu1XL-9tUb35zYo7-fZCC8MXQMuvMPDNCW4d5ZOAnJfQNz1yEqJN9V9RiKZtJ8BaOK4Ae0MhkMY_-2YOi2V_YGsvyW_73BlXbRzWQP6QdAPdj9W4E5Tk9BbwSYxTg60FPoCwFs20xc3TyTVJajoRdyYc8EKo3k_btV_8XHQ0K2VztU7pA6rRAC8FtSkGdwxD49LePlHmGTDZ39ysvMLpYArci0liMUjkUIJvqxJjtVth2A5CZ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس اینترنشنال: نتانیاهو رای نیاورد بدبخت می‌شویم!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/463027" target="_blank">📅 18:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463025">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c5bace06.mp4?token=txt_pGQ7f960MWSqP6bNG6MtFmOoIeBr_zfG0etZsW08whjILfWTH5OLvOGxBgQDjgYLaW3EbBqd25j1kcGVJnezjtB8dY7dexr5yiKCGM5STvZEKqQED9xEtBkHZUqyqYVgBqcE9cyIoZFxVFv0MJtmx9G0vaEAupx3Br_8vITh5JOTWi-_vT0qW_DL0jxWYULr3gejCJ7aF0XNqxz49KDSaDM1Pobz-2Z_5xBrBSr8L_8foVCIIRaqoy4uaD56YELgQWkBd9IjzIsHOeqMxcRt-aYThg5UE24hASPbTUf-cVan20MNHvy1MrIUtRFZmMakGA5WvN6i8i7XJtRB747OztM_fUduQCtSZox-9ZEN0r4Pwvw3MZsb3JxnmXh-46hRy2fpID2rq2j9BpL8Lx7x5-IDHZayTKrI0kzjsNaSSbYzXj5QehOSoaF4Dwwy9nIp7XN4M5Wg-5VaJKvAZiEy5ikXxWmnC-AwkjXq3QG_SSaOvEk2j8veljZWtkVglDg03p-H6HV2vtxN_1pWQFxAMwbaHoNUm2mmNhuaCK1EJsHgVdvDO6iJCwZ-qQeNZ8i5TVSXyFaJMTzOv84mbPvhmKYHf2poxhTcCdekgeHIwmoOvAcckZjndqN4FndhhNqrTmjHY2SelqidpR-vjnn0wln5H3JWb_lSQRulQD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c5bace06.mp4?token=txt_pGQ7f960MWSqP6bNG6MtFmOoIeBr_zfG0etZsW08whjILfWTH5OLvOGxBgQDjgYLaW3EbBqd25j1kcGVJnezjtB8dY7dexr5yiKCGM5STvZEKqQED9xEtBkHZUqyqYVgBqcE9cyIoZFxVFv0MJtmx9G0vaEAupx3Br_8vITh5JOTWi-_vT0qW_DL0jxWYULr3gejCJ7aF0XNqxz49KDSaDM1Pobz-2Z_5xBrBSr8L_8foVCIIRaqoy4uaD56YELgQWkBd9IjzIsHOeqMxcRt-aYThg5UE24hASPbTUf-cVan20MNHvy1MrIUtRFZmMakGA5WvN6i8i7XJtRB747OztM_fUduQCtSZox-9ZEN0r4Pwvw3MZsb3JxnmXh-46hRy2fpID2rq2j9BpL8Lx7x5-IDHZayTKrI0kzjsNaSSbYzXj5QehOSoaF4Dwwy9nIp7XN4M5Wg-5VaJKvAZiEy5ikXxWmnC-AwkjXq3QG_SSaOvEk2j8veljZWtkVglDg03p-H6HV2vtxN_1pWQFxAMwbaHoNUm2mmNhuaCK1EJsHgVdvDO6iJCwZ-qQeNZ8i5TVSXyFaJMTzOv84mbPvhmKYHf2poxhTcCdekgeHIwmoOvAcckZjndqN4FndhhNqrTmjHY2SelqidpR-vjnn0wln5H3JWb_lSQRulQD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیمت‌های سرسام‌آور سوخت در آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/463025" target="_blank">📅 18:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463024">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUF2N6oGjrP7V_2h0iVk1WJUq0nLlcy17znoxVzzRUERxbdyIOQ9xNlFJvuvmgOZohaUVEWn0JoOuZ4uxx2sg0H3-cwmLlhHchF5na-WouT8pfkwdMCbbuSiOU9_q8hYlckw5cxRPH9-jw6Jvb8W1TdI7l9rfXDN-wB4q5lW1-HyXPpLz6SRB3WJNs34HRere8FUGWNCwpn9frqzJ1sKeGnH9qq1B5ix9_4B8ihWwfQXsbErZEwgdU8qPqCepRQqg2Ee-6xF5VHiU-I2xlfuDz2E0WeFqp7tqQllaiJcL5-OhCsRf3RW6Dx7IBUsKierTA8yGyRyNT1HapxwlSwTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهر تایید ناسا بر انفجار مخازن ذخیرۀ سوخت ریاض
🔹
داده‌های جدید سامانۀ ماهواره‌ای ناسا وجود آتش‌سوزی در نزدیکی بخش شمالی فرودگاه ملک خالد ریاض را نشان می‌دهد؛ این تصاویر وجود آتش‌سوزی در نزدیکی بخش شمالی فرودگاه را تایید می‌کند.
🔸
سخنگوی نیروهای مسلح یمن سرتیپ…</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/463024" target="_blank">📅 18:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463017">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3JhFDz_x3ZneJkhgqlcio2P3lXH3AxYG3DjUR5LCl8fmoGTBVttPq86aIkNu8z8wK3KK3xgOc0VRT7VkqZ4CXb_KjbQ05IOllfRAaXBdCIuqWZJMFIKmUpJb_ldRuNJBQwub_7I485U8jjRXiMGeHuTSWLJMhokHWZhEC8-AxKBGWcW0tpTw0GtanM_BIXyof0J20B565BUwFVNBeoParrfnA1h1FtfTyI29ZGVbgZY57OGsqN_Izf1NkoFsBfhWgwfD2Zl-1M8FzXRnRxiaKKxmFAUHiDXGCqWl7PEMstPP5kdBlnwNWDEH5GC4d9wYgtU3AsiAtXdM-iUZrrnHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Akmr56GC3tOCUVHUsIgijwbpl-sPO87T3-h2qneKRtrEnHqgqeFM2LLO1Ot5X7ldPK_jKpjVa-htj-oOT62zILIRbiK9TcUnJQ3NqwkyvVKyoPiuFeM6Kl9Vbm3KrjtgqsxHlJIYEnFfLHm3uXCeWaAHLmB1Mw6wsfShGTajJN2mRfJE713R2KhME7eOqyEpKF6SNWoDFP7ZpROcQVkqtIXJbWeNM6aNrckxG6f23e9IROCwQwqiEyjRTDasb5oqSHvLtyqsFPZUlNqDftlk0z-0LKiFtw2gEd0e3gMWNPRU4yNQfxkU-BM9Dhy-SZLvvg2PksJZq-NrpHQu4k12Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukOYalKYt4wcEFvlQRb-oEKvzdvx36eSzSueapFO_SFBCXopzv0nGHBV2RwHxCqdVWLpaVMvoy_0vIAqpcqDLFEs9fBO5AHUBQQIPmEsb6_LE9CD3mr5DMLVihVqsTQtGALuemeNCrNjMnQsTUoVmGqgxr6Uh-xk7EX2Asuz3ZwHJmVq0ydJb9KDiJKO2zBAnt1j7_9M-E8iaujb0C89SSLaUWCnSMcOtlDgfiQUN19jTzDrcbwdmx99S_GOf4VB-JtyQVN42n3EMuRMV0TfuCS_9LU-BdLpBqMmPG8am6vraBQhx-m-j4rN9ThcWQSsj2TsvHX8VxW_CtqzwlYqvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hieMGGziPbZgR6DXb5MxizoVY--fLdRKq9PXKn-JCJ1q_h_m1GJSzfZqLURwy0pbFr6XfGBvQZ2fW-SxqulxRwNdRWn6uO_WpbVC6CH_IS32q0H86cIiUOtMSxGMedO9Y3ktS8ytczgySANw6jedvxgp80AzoXiV3keWAclFDG8fEkllVeKHosd8bqzefzFupD11eqNbismmza0gTP-Hme9dyCZGTOppcAdLANhEUCbycH75IkSRuwCeUhEqUTKAYNdKtcchUZPc6h1R_a_roEnLIW2xc3_GiDFpk3nPSikFUtLy18SGA7LySss9DOjPu7QR1fjvuv_ayGPgjq9yJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UijZxdgEs8nRmL-UsLL4Sef1HZbZLvMJ1qzaoS3wMBpkEClcqpCXOpGJXnD4NKp0KbwT18qnHo3fzLdwzSY4LLcGP6GlxCz9n4ChHUEAahXTEtEiIl-o9gKvukEVVCLpRMMA3VLM53N8c7JryghH4CxHEUsgIl-vm9u04ttvQ6U_oJcvw5SXUwZN8LBILvV60QGuaMEi4mOgl1VrevgtZOzapXoBYnpIIVNNg6xrLeM4CMTw_5Tp7e3qjDtHI_rmkGJFMjvrhpikwQp2zkksL754waYlEwApTFuuNbOj0nPqTweMJNYTy2t-oHa7lLkkMmF8zlMuQNvF4g2SAkQ_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-5EpAegS_6kfq6XSSC8AC6YoMBvJ1wb7oL3-18PND_l7KdoPDDemOJa5kG9kFJvpIlSpnLbu23Ki151t6XK5bNSW4O_2nMTSw0OqP2UvMc9T7qwlBhM_yeKXgrV5D9RpS-7Sxx4VtNMDwBs7mMQeNB8nFZcxwfH6RRPvXfpu-m3Li0VvKekbE2jgs62mdwTV-I4mhyXF4ix_U0zNc-cFUUtmA7tvxCTMT--KMvS4z8T-g17rSC3PuhYisjcP6f5rKq-5AP3OZhxsvLkTwYqm49lArVcNkUMX9ze_XTJqYFAtRLM5wDWvo_J1M1roIppHZWLcM4ltkVjeHFPtTYd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxhzNfqUU2f3TpJcjvieUI2sdYCVcU6OcjXi70LJyw7mwDw3BEyjAAmiCpb69Kt9fN03zb4y0UGN7Mkrs_q5WXYubrGZUUJ39o-jAhwv9lLeQPvcusyBQCN3a9tJ9JqUE1urHrN0GqBC_z2jbidHc77be52nnCq-02KnUE7HR2p7lIfywRW3ZOAcALZ9iVkbteSaniwWi5shOgtL6VT9Q4U3r8If6ExSGerqRURzu9eqUn6S-r0HPxzb2ZMY7ABY6lXfNqbiwr10Z_BeULNv7oeeX_KelNCTrMffPV-yJrlOrjLEa604tvDbU7avBR04quhRuZHrEjBqHumopXYZNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت خرما از نخلستان های کارون
عکس:
محمد آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/463017" target="_blank">📅 18:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463016">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۶.pdf</div>
  <div class="tg-doc-extra">2.7 MB</div>
</div>
<a href="https://t.me/farsna/463016" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۵.pdf</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/463016" target="_blank">📅 18:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463015">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erqUq4r5uz85gs--ptNOIlVyqOZEqXDdROwomQcb7LuuiYVpmkUw3qA8ChPLL0PhtBN0xiYbVKV2mVau8PeEdXZWL2E4Y2WyMSuTaP6xaFZEn8dV43FNTffO9dN1WspOE1F-au3G5HH5eoFEinYQPdwuCoNvLd8qj5VLOK97NYFD9fg267F09jPiHD_iVy5CZsknCdDO3rS_BXDZ4Kd_EnmhMxLEhtglZyqBI6hfBsquUl6Kq3DvWqcuMxYR8Oi60baw_ZUbKAw4IecGNWrfIK7nTdFpyK729Bx5ecF9iLK-1wMXPMyTfYmO6yYthsatbfOQg64khNSo5ngxKuM44A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالق چت‌جی‌پی‌تی برای پاسخگویی به شورای امنیت می‌رود
🔹
رویترز: سم آلتمن، مدیرعامل اپن‌ای‌آی، قرار است ۲۳ سپتامبر در نشست علنی شورای امنیت سازمان ملل دربارهٔ پیامدهای هوش مصنوعی برای امنیت بین‌المللی حاضر شود و دربارهٔ رویکرد این شرکت در قبال توسعهٔ ایمن این فناوری توضیح دهد.
🔹
آلتمن در این نشست که به ابتکار فرانسه برگزار می‌شود، دربارهٔ موضوعاتی از جمله ضرورت همکاری بین‌المللی در حوزهٔ هوش مصنوعی، تدوین استانداردهای مشترک ایمنی و اقداماتی که اپن‌ای‌آی برای کاهش ریسک‌های این فناوری انجام می‌دهد، پاسخ خواهد کرد.
🔹
قرار است آلتمن در این جلسه توضیح دهد که اپن‌ای‌آی چگونه تلاش می‌کند میان توسعه قابلیت‌های هوش مصنوعی و مدیریت خطرات احتمالی آن تعادل برقرار کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/463015" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463014">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neu94cGbZpqniZuqSvgwNkEtHkGf5C_ViX-eMjRf8MTxGjqepjemGsQRtJet-q0824WaD8G7qvXBYEN5Daf7euDmXbC3BxuF87NrsuPn02UqAATilXY0ufDGdo49-ttR9iqoJL3UPIikYUjboYkn1EzlPwfRRO6nxEMH6oDVCuObbCEqZjlE93A9ExBi7qoKC-YEQUzr6EHaxoWaR3UND7Bh4Dppbo3E7WalYcWoD7mRHEs2jdZ4VDeBwoRHY4rDOfWMhkUMh0D5TqI7pkoyd7vuXbJBuKeUC6U3X337UHuEfUPIp26JTUOcQVI4ZsD0Y3rNL5X3XDZeD5tvrG98Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای غرب: پوتین برای تشدید جنگ آماده می‌شود
🔹
به گزارش روزنامه تلگراف، مقام‌های اطلاعاتی غربی معتقدند که رئیس‌جمهور روسیه در حال فراهم کردن مقدمات یک «بسیج مخفیانه» پس از انتخابات این هفته است که در چارچوب آن، ممکن است هزاران روس به خدمت سربازی فراخوانده شوند.
🔹
طبق این گزارش، همزمان، سران اروپایی هشدار داده‌اند که جنگ ترکیبی کرملین علیه غرب احتمالاً تشدید خواهد شد.
🔹
در این گزارش به نقل از منابع اطلاعاتی ادعا شده که پوتین در جنگ اوکراین به بن‌بست رسیده، با این حال، تصمیم گرفته به‌جای ورود به مذاکرات معنادار صلح با میانجیگری ترامپ، دامنۀ جنگ را تشدید کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/463014" target="_blank">📅 17:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463013">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ec7927ad.mp4?token=ZYqzsaGg5unoj_eDNzYuOfm-u9d9wqTVmb20tJJ1nIVooVMarSJsjNjVBMXlKGm4Jen4Uifmkv47UjJ4v2PTVMKuanLZBxzrZn1CAJBzeEcRTNyquInOi-LBFPHPyJggvyPqK8oacHQe4gQQOfY7642obf85G3TSHMGFjvBpDZT28jMtNLk_pwxzR8aIrcy789V1rZ65cPyXqp2H7oDE-jwwNv3s33Lstfa-yhYa54Pfz2DQIDH3B-mGYOWuLgDB6Otn7-MPd4zYnmDe7rNf_pJnX0nWvLwabMmvR4Y34kjL6Yol-TFRumQivLKUo8Z61O0ehvmr9HXhs6f-tQSunUYWP2XVWy5gmvS7Inqwh2b2NMtvDSvdP1J0ismBv9JN3dDN5-d1gWs688vxcevH3olmPFBMfqq7sW1ewbSnDLEtTRkUISlwNUddCblAoyVUTC1tKA1gAbKY8T08Y8rKmzEV7PBZQRGBB0fFbijzNLDyJa0Y5LIXX33Jw6I48w2QjF39ckCiZTBOu8Yoqh0NGPgRy_Ems9n0TzK48r5Jfa_S50M2MgNMqNPYh9_FRhmKKdp5Pt21LuOJYLysbsSjR1oPcBgRVJlSftDnWCM1RY276LXgrvOvyIfE1-ceCGBigqxXI72Gz4dBDwUFGr7u5HZ0aObyH0Ft2Agb-jtaaXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ec7927ad.mp4?token=ZYqzsaGg5unoj_eDNzYuOfm-u9d9wqTVmb20tJJ1nIVooVMarSJsjNjVBMXlKGm4Jen4Uifmkv47UjJ4v2PTVMKuanLZBxzrZn1CAJBzeEcRTNyquInOi-LBFPHPyJggvyPqK8oacHQe4gQQOfY7642obf85G3TSHMGFjvBpDZT28jMtNLk_pwxzR8aIrcy789V1rZ65cPyXqp2H7oDE-jwwNv3s33Lstfa-yhYa54Pfz2DQIDH3B-mGYOWuLgDB6Otn7-MPd4zYnmDe7rNf_pJnX0nWvLwabMmvR4Y34kjL6Yol-TFRumQivLKUo8Z61O0ehvmr9HXhs6f-tQSunUYWP2XVWy5gmvS7Inqwh2b2NMtvDSvdP1J0ismBv9JN3dDN5-d1gWs688vxcevH3olmPFBMfqq7sW1ewbSnDLEtTRkUISlwNUddCblAoyVUTC1tKA1gAbKY8T08Y8rKmzEV7PBZQRGBB0fFbijzNLDyJa0Y5LIXX33Jw6I48w2QjF39ckCiZTBOu8Yoqh0NGPgRy_Ems9n0TzK48r5Jfa_S50M2MgNMqNPYh9_FRhmKKdp5Pt21LuOJYLysbsSjR1oPcBgRVJlSftDnWCM1RY276LXgrvOvyIfE1-ceCGBigqxXI72Gz4dBDwUFGr7u5HZ0aObyH0Ft2Agb-jtaaXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی انگورها مردم را دورهم جمع می‌کنند
🔹
تصاویری ببینید از حال‌وهوای جشنوارۀ ملی انگور در لاهرودِ اردبیل.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/463013" target="_blank">📅 17:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463012">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌ صدور حکم اخراج ۶ دانشجوی دانشگاه شریف به‌دلیل ایجاد آشوب
🔹
معاون دانشجویی دانشگاه شریف: در پروندۀ مربوط به ناآرامی‌های اسفندماه، مواردی مانند درگیری فیزیکی، ایجاد آشوب، حمل سلاح سرد، توهین به پرچم و برخی تخلفات فضای مجازی مورد بررسی قرار گرفته است.
🔹
در…</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/463012" target="_blank">📅 17:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463011">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLYvgBVga_HISsmPOavizpzy1SpnQVa5VZh2kzXt4ytTyssneZTtR9wNLwD-lETlL-CjOg6v63jk_H1rIEVYVi-rUodfUNgd5vRTL8hu0xIZ8-CFX9V3vKthMrVWhN7Kb5JssrwlmGfJT76DOXHWZCy1BfUgT_Ox0yzzAtN5YyVHOFzP4EulTU3FHIPg_qxHFSj8DvfUywGWh2cfqfi6Izi8t-Fy6Z6ubHOv4KKb5wpkzkKIjleZ15_YCWaxry7PAeXwTowWX6XM5F9tmviqIiwulW-cTYlDbQmKJT-a777tqFRDcB3mnzR_qwls35AbwAM9YVPaF4-060HzTAl1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم خطاب به سایپا: اول خودروهای معوق را تحویل دهید بعد ثبت نام کنید
🔹
در حالی که سایپا طرح فروش بدون قرعه‌کشی کوئیک و سهند را برای مالکان خودروهای فرسوده اعلام کرده، تأخیر در تحویل برخی خودروهای ثبت‌نامی قبلی سایپا همچنان محل گلایه متقاضیان است.
🔹
برخی مشتریان از
تأخیر چندین ماهه
در تحویل خودروهایی مانند ساینا، اطلس، سهند، کوییک، شاهین و وانت پراید خبر داده‌اند؛ در مواردی نیز با وجود پرداخت وجه و تعیین موعد تحویل، هنوز دعوتنامه، فاکتور یا خودرو صادر و تحویل نشده است.
🔹
یکی از متقاضیان می‌گوید با پرداخت ۵۰ درصد قیمت خودرو در فروردین ۱۴۰۴، موعد تحویل خودروی او دی‌ماه ۱۴۰۴ بوده، اما تاکنون خودرو تحویل نشده و افزایش قیمت خودرو نیز هزینه سنگینی به او تحمیل کرده است.
🔗
سه پویش فارس‌من در اعتراض به تأخیرهای سایپا:
🔸
سایپا به تعهد تحویل ۹۰ روزه خودرو عمل کند
🔸
مطالبه اجرای قانون و تحویل خودروهای معوق سایپا
🔸
گلایه از تأخیر سایپا در تحویل خودرو
@Farsnews_My</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/463011" target="_blank">📅 17:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463009">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8bFguapWv3YT5h7eUzPkS1vYJktoCo_3zAYkUdVCsxiVSP2RLuFxdZJNgrk6DuurZzPTVp7ShiBtFDjC6nbLtw6ClhQJtt6XYbm4pGejJQJfwSi3Wa2BsTcZ_K1goBx-BN7dK5cIPkASQeeiwvSGcTryZ0Ss8mel6B-78qNnqceDI9RJHuGcON68FXo1UZSrcs6cEic0fJPetE6KtCWzGqW_E-pJQzFGrPeKSo-dVDXL5Yaow2fTrMz1V6loCRH89J9T07w-S_hFaJtkF4XdcDGuGZW-nvpWu9o36z1MCXPz7SlLo2Oh1c2FuUtUrjCIvF1EVN3mzatRA1SVcNDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش بدون قرعه‌کشی کوئیک و سهند
🔹
سایپا از ساعت ۱۰ صبح ۳۰ شهریور، خودروهای کوئیک «جی ایکس ال» با قیمت یک میلیارد و ۶۳ میلیون، و سهند با قیمت یک میلیارد و ۳۱ میلیون را بدون قرعه‌کشی عرضه می‌کند.
🔹
این طرح بر اساس قوانین نوسازی خودروهای فرسوده اجرا می‌شود و فقط خودروهای ۲۰ ساله و بیشتر، یعنی مدل ۱۳۸۵ و قبل از آن می‌توانند در آن شرکت کنند.
🔗
ثبت‌نام:
saipa.iranecar.com
🗓
تحویل: مهر تا آذر ۱۴۰۵
⚠️
هنگام ثبت‌نام این موضوع را درنظر داشته باشید که بسیاری از خریداران پیشین محصولات سایپا با تاخیر تحویل چند ماهه تا چند ساله مواجه بوده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/463009" target="_blank">📅 17:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463008">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICcRqjVFfNirmnrzrvN8POB-HsxBN_gmG8q2VkhlUetp3chZF_OZzhVQ7afhV_Ke9KYe8BnN87oZVmQYZFg8rJuDW3QrWMCKhxNb3gYBDcI-8fcD2NJ0PL0_AF09avtORd1SS87s1vDEvVoOKHF6DOd0CDp6Qy3moFMdaRjJJE_3elN6P6qy5POwPDnrt9Ho0qlNH4lZ6J3ojkgYH67Jv6zDYuQAMBvCdATEHKSE_EWI6Xkg030IoH3FhM5DiSGtjDMQt3-HIJ8c7zraTulapjCoEFrXlpYP5-5XeqW6So5sJcK1x8vw30hMrz0BkUMLndiNyaM8KEXOXjn52l_DOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم انفجارهای مرموز در انبارهای مهمات «الجولانی» در سوریه
🔹
مرکز موسوم به دیدبان حقوق بشر سوریه خبر داد در جریان دو انفجار اخیر در مراکز تسلیحاتی دولت الجولانی، ۵۴ نفر از نیروهای امنیتی وابسته به وی کشته و زخمی شده‌اند.
🔹
در تازه‌ترین حادثه، شمار قربانیان انفجار انبار مهمات در یک پادگان نظامی متعلق به «اداره تسلیحات» وزارت دفاع شورشیان در نزدیکی شهرک عیاش به ۱۱ کشته و ۱۰ زخمی از نیروهای وزارت دفاع رسیده است. گزارش‌هایی نیز وجود دارد که از مفقود شدن شماری از نیروهای الجولانی در جریان این انفجار حکایت دارد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/463008" target="_blank">📅 16:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463000">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlUFaYa9q5y1lMtOFuQHPBUvmoTJI0k5MJgMVCqumtSSKg5RLCYfyHRgcdV-sXMlHf5-grTqIcq6rgalw5gmbA4Rc3tUBiU1HPfodAGhSveKLaTcNYO338Ja9X7lh1SP_ZTmteunpJt8UKjidt5q1h4yavd8wO0izrCqW3YhH4JPjjaI6_eQsucVm8bWeba9BZM06Kaqh-FZ8xaFarubdi-Ett9UxaQ75sGqvWH173vF8AP2qxJv-XPW59cLBaEpLzLrMR-Rj3zvQZ23VZI-iSjdcaO6J-AC4D7hxBSbuIuA39uui23GqptSrSUQuYl32op9z0Sa9W_l1NRLjz6Qfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس دانشگاه آزاد: «جان‌فدای ایران» صورت‌بندی جدیدی از هسته سخت ۹۰ میلیونی است
🔹
رنجبر: در بیش از ۲۰۰ روز گذشته، مردم یکی از مهم‌ترین عناصر ایستادگی و عبور کشور از یک دوره دشوار بوده‌اند و نشان دادند که برخلاف برخی دیدگاه‌ها، نباید قدرت را فقط در تجهیزات نظامی، توان اقتصادی یا ظرفیت‌های فناورانه خلاصه کرد.
🔹
ایران می‌تواند نقطه پیوند مردم و عبور از نگاه‌های طیفی و فردی باشد و حضور میدانی مردم در حساس‌ترین مقاطع، یکی از عناصر ایستادگی و انسجام کشور بوده است.
🔹
در این نگاه جان‌فدا، پیش از هر چیز، یک مفهوم ملی است برای معرفی هم‌میهنانی که ایران را مسئله خود می‌دانند و علاوه‌برآن، در هر عرصه‌ای که کشور به آنان نیاز دارد، مسئولیت می‌پذیرند.
🔹
این نگاه می‌تواند مفهوم «هسته سخت» را تا مقیاس جمعیت ۹۰ میلیونی ایران امتداد دهد؛ از میدان دفاع و امنیت تا دانشگاه، صنعت، اقتصاد، فرهنگ و خدمت عمومی.
@Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/463000" target="_blank">📅 16:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462999">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQ9AI2uWqvXXUFI1mOb5r4ukl7NBmab5oiSiDTG6PnyPAeMfBuLymbsA_LyZzBjiSLplCkDVMY0pbjPdyYt6zV2qjvRPbDcCJA31FgaKs-dIMLLdmqzINgxmKY6E5Q4UkHJYQ1IhrTfjy038WM8tAq95quZ-EY8uK675XUuISHcZUJ8Qb9dMMMfjjRoRP_w9qbuXoUT1dNyzqsO6CgTmbZ030Mnnekc5I897mOmOC6MtYuAxNPKh-sjCTQN-gDaPZpcCcovZIvodh2gmWA8eixlcIZTDO-aRFFZfmjStohZ4mhfzgVUr04zBnVKm8lib5Nlem3BIzuxv1GqOrsA54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ صدای فاکس‌نیوزی ها را هم درآورد
🔹
چند چهره و تحلیلگر شناخته‌شده شبکه فاکس‌نیوز از تصمیم دونالد ترامپ، رئیس‌جمهور آمریکا، برای ممنوعیت حضور ام اس نَو، سی ان ان و پولیتیکو در کاخ سفید انتقاد کردند.
🔹
آری فلیشر، از تحلیلگران فاکس‌نیوز، ضمن ادعای اینکه برخی رسانه‌های حاضر در کاخ سفید از نگاه او «جانبدارانه و ناعادلانه» عمل می‌کنند، با ممنوعیت آنها مخالفت کرد.
🔹
بریت هیوم تحلیلگر ارشد سیاسی فاکس‌نیوز نیز با تأیید اظهارات «جاناتان تورلی» استاد حقوق دانشگاه جورج واشنگتن، اقدام ترامپ را سابقه‌ای نامناسب دانست. تورلی گفته بود این تصمیم می‌تواند پرسش‌های جدی قانون اساسی ایجاد کرده و جایگاه دیرینه آمریکا در دفاع از آزادی مطبوعات را تضعیف کند.
🔹
هیوم همچنین درباره این تصور که ممنوعیت رسانه‌های منتقد باعث پوشش مطلوب‌تر برای ترامپ خواهد شد، گفت که رئیس‌جمهور در این صورت «در خواب و خیال است».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/462999" target="_blank">📅 16:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462998">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSv54-JTXFGRNRSVVOOyrukCaYBCYVK-ANMAmPxSm_P8ZbRYkl0TaqczGrYa6X85P5-webg1wXso1Jv0_Hrq-xDIplMqsUU2RhoTM9U5iU8oD7qoPqLBAyNyLPDeCOxKPh7JQ-JC1f2w4BWFo868LIGc_wp3RVgnsHycE2X5f3IB4xMsaXT3-6SZdtTuCP5w4yP6BsKVF7Z6Bjyw-wKrRnLG5d2RdTy2GsAxUvrfdoDLOxi3V3saWBsy830ep7hUJWA9f_JXabG1g9PF-MpSZQNs5jcKLDXzeIgy1tjqThnQ15Yck31zbldzjIr3NwnlMvbCL3IqHNtfbaj0JBytjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت به وطن؛ از سراب غرب تا واقعیت ایران
🔹
بازگشت یا اعلام تمایل برخی چهره‌های شناخته‌شده ایرانی برای بازگشت به کشور، بار دیگر یک پرسش قدیمی را به متن افکار عمومی آورده است.
🔹
تصویری که طی سال‌ها از زندگی در غرب و زندگی در ایران ساخته شد، چقدر با واقعیت تفاوت داشت؟
🔹
گفتمانی که غرب را «مدینه فاضله» و ایران را «جهنم» روایت می‌کرد. این گزارش تلاش می‌کند چرخه این روایت‌سازی، پیامدهایش و اکنون موج بازگشت را تحلیل کند.
معماری یک روایت: «غرب بهشت است، ایران جهنم»
🔹
دهه‌ها بود که ماشین تبلیغاتی گسترده‌ای، تصویری دوگانه و تحریف‌شده از دو سوی دنیا می‌ساخت:
🔹
غرب:
آزادی بیان مطلق، رفاه بی‌پایان، عدالت، رفاه و معنای زندگی.
🔹
ایران:
سیاهی مطلق، سرکوب، فقر و بی‌آینده‌گی.
🔹
این روایت تنها به رسانه‌های ضد انقلاب محدود نبود. جشنواره‌ها و جوایز بین‌المللی نیز به ابزاری برای پاداش دادن به روایت‌های سیاه از ایران تبدیل شدند.
🔹
فیلم‌سازان، سلبریتی‌ها و چهره‌های فرهنگی، آگاهانه یا ناآگاهانه، به پیاده‌نظام این کمپین بدل شدند. نتیجه؟ موجی از مهاجرت که نه بر پایه واقعیت، بلکه بر پایه توهمی ساخته‌شده شکل گرفت.
برخورد با واقعیت غرب: سرابی که فرو ریخت
🔹
اقتصادی:
زندگی در غرب برای اکثریت، به‌مراتب سخت‌تر و پرهزینه‌تر از ایران است. کار مداوم، بی‌ثباتی شغلی و فشار معیشتی، بخشی از واقعیت پنهان لیبرال‌دموکراسی‌هاست
🔹
فلسفی:
انسان در نظم آهنین سیستم‌های لیبرالی، به ماشینی بی‌معنا تبدیل می‌شود که در چرخه تولید و مصرف گرفتار است. آزادی واقعی، قربانی نظم بوروکراتیک و اقتصادی می‌شود.
🔹
سیاسی:
آنچه در ایران «بی‌هزینه» است اعتراض، نقد، حرف خلاف جریان در غرب به‌سادگی ممکن نیست. دیکتاتوری نرم، در تار و پود نهادها نهادینه شده است. این مواجهه، برای بسیاری شوک بود. اما اعتراف به آن، آسان نبود.
کمپین «جمهوری اسلامی رفتنی است»: فرار از شرمندگی
🔹
وقتی فشارها بر مهاجران افزایش یافت و نارضایتی‌ها علنی شد، کمپین جدیدی شکل گرفت: «جمهوری اسلامی رفتنی است. امسال دیگر می‌رود.»
این روایت، ۲ کارکرد داشت:
🔹
توجیه ماندن در غرب:
اگر نظام در آستانه سقوط است، پس صبر کنیم تا سقوط کند و سپس «پیروزمندانه» برگردیم.
🔹
پوشاندن شرمندگی رفتن:
اعتراف به اینکه «غرب آن بهشتی که فکر می‌کردیم نبود» برای غرور بسیاری گران بود. بنابراین، ترجیح دادند به جای اعتراف، به کمپین براندازی بپیوندند.اما آن کمپین هم فرو ریخت. جمهوری اسلامی نه تنها «نرفت»، بلکه ریشه‌دارتر از همیشه ایستاد. اینجا بود که موج بازگشت آغاز شد.
اعتراض‌های خارج از کشور: نارضایتی از غرب، نه از ایران
🔹
بخش قابل توجهی از اعتراض‌های ایرانیان خارج از کشور، در ظاهر علیه ایران بود؛ اما در عمق، فریادی از سر نارضایتی از زندگی فلاکت‌بار در غرب بود.
🔹
ویدیوها و روایت‌هایی که بعدها در شبکه‌های اجتماعی منتشر شد، پرده از زندگی دشوار بسیاری از همین معترضان برداشت.
بازگشت: حق قانونی، اما نیازمند شهامت
🔹
بازگشت هر شهروند ایرانی به کشورش، حق طبیعی و قانونی اوست. هیچ‌کس نباید به صرف مهاجرت، از این حق محروم شود. اگر تخلف یا جرمی صورت گرفته، باید مانند هر شهروند دیگری از مسیر قانونی رسیدگی شود.
🔹
اما نکته مهم‌تر این است: چه خوب می‌شود اگر این بازگشت، با شهامت اعتراف همراه باشد.
کسانی که سال‌ها واقعیت‌ها را وارونه جلوه دادند، مردم را گمراه کردند و به کمپین‌های ضدایرانی دامن زدند، امروز این فرصت را دارند که: جبران کنند، واقعیت‌ها را با مردم در میان بگذارند،
و خطاهای گذشته را به مسیر اصلاح تبدیل کنند.
🔹
چنین بازگشتی، نه «فرار از شرمندگی»، بلکه آغاز مسئولیت‌پذیری است. و جامعه‌ای که این شهامت را ببیند، بهتر می‌تواند زخم‌ها را التیام بخشد.
🔹
بازگشت مسعود بهنود و امثال او، نشانه‌ای از پایان یک توهم و آغاز یک واقع‌بینی است. غرب، آن مدینه فاضله‌ای که روایت می‌شد، نبود. ایران، با همه مشکلاتش، خانه است. و خانه، جای بازگشت است به شرط آنکه بازگشت، با صداقت و مسئولیت‌پذیری همراه باشد.
🔹
امید است این روند ادامه یابد و همه ایرانیان، با شهامت جبران، به آغوش کشورشان بازگردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/462998" target="_blank">📅 16:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462997">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6pWnFZCuR47cGFdxP95jE1sWCnnWphY8hgRbWMMAAFF0qpFIVxA9SIvOW1YUdgQKDOwA_Sp9Y6iMnwyDIwSUJCd6sybrYRb6VyNKmU4--wWKY4Mt1UhN-CnMcObFdRzOVE5Sr9z9FKG6NUIgO6jxAMrO-qo9j0E1JXiVAX7WBSQIO9HT1JJeVh9SY19rsSMhByO5y5RUd7WCWDOgcDg03KFUkJEGcFJHIje32QlMzkwVmNDlqomwwovvJ-P-1TDl8Msr0aGUL3I8kHDshKnkIwtEKpydoh1_WA_xAN1DCR04w2mA_vcmI21Z3N8DELwrvetguYNlWrPOnEDob6egA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویری از بلندشدن دود از فرودگاه ریاض
🔹
برخی منابع گزارش کرده‌اند که ۲ مخزن سوخت آرامکو در شمال فرودگاه و ساختمان بخش بار فرودگاه هدف قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/462997" target="_blank">📅 16:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462995">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxuYh-7KfTgeibWYsKDqimvvS1Y7sTuDzfLltKZWTExLoOX5ybmITpLaSQRZXqDWM5Vce3b87RCwxCDuAsQVGfWYqACW4AK7vUWwGQRMC_UGjtT5B2JQWW9zZhDX3X08KSjGBWYOWEY48Tw5iW-hdeQ4t33lRHpOvyC9re_q_ajAVKIUFFTctQfdswmzBkjFcB6sVOIT3_ss-Q_f0NKdTS1QkRUArRURywijEBl8aAPUnjM68tzGYgUsym_3ZXWX-meIar5f6Cj_F2o0q_wYSKUKT6kUO1vMHWqsPopcCFtWSYL49786fD6E_1WYOzLJi-GjFLYGyGe1W5uXk-8mSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف پروازها در فرودگاه ریاض پس از برخورد پهپاد انتحاری
🔹
منابع خبری اعلام کردند که در پی نفوذ یک پهپاد انتحاری از سمت یمن به حریم هوایی عربستان، پروازها در فرودگاه بین‌المللی ریاض متوقف شده است.
🔹
هنوز جزئیات دقیقی از میزان خسارات احتمالی این حادثه منتشر…</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/462995" target="_blank">📅 16:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462994">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f1be6cbc.mp4?token=HLYxtuIkm6SHnSk48NRs3emHzVhFrxiBPYZoqFBGLdXa2Dn6_HWlvXCTRq3adee6HuFNY1jaNtkZsv2IOjF5a0rEutVzSeJNKl_wX8Qj7BA5u5KD0lcexv37yW-G0eN0pIkyIHnXMBK-Iq4koEj8kdPRoZnyJdeGVuUL1Tdp9AepiRWkyYlJBdh6mx8YppPp24pED3XAXx83-nkDZo7UFVsYB01TqCGcZxk327ghN1DBaXhWBlujOBBVwwSR2NGH2jiq-2P2tn36E2NjAdthd6fMhjFQS5bS1OUBq7fYoM8EGaU5N9p1-ChxawdF8bHmOqbFgUhiXjJByklvJn3ZYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f1be6cbc.mp4?token=HLYxtuIkm6SHnSk48NRs3emHzVhFrxiBPYZoqFBGLdXa2Dn6_HWlvXCTRq3adee6HuFNY1jaNtkZsv2IOjF5a0rEutVzSeJNKl_wX8Qj7BA5u5KD0lcexv37yW-G0eN0pIkyIHnXMBK-Iq4koEj8kdPRoZnyJdeGVuUL1Tdp9AepiRWkyYlJBdh6mx8YppPp24pED3XAXx83-nkDZo7UFVsYB01TqCGcZxk327ghN1DBaXhWBlujOBBVwwSR2NGH2jiq-2P2tn36E2NjAdthd6fMhjFQS5bS1OUBq7fYoM8EGaU5N9p1-ChxawdF8bHmOqbFgUhiXjJByklvJn3ZYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیاه‌پوش‌شدن حرم امیرالمؤمنین(ع) در آستانۀ فاطمیه به روایت ۴۰ روز
◾️
اختلاف در نقل زمان شهادت حضرت زهرا(س) باعث شده شیعیان روایت‌های ۴۵، ۷۵ و ۹۵ روز پس از رحلت پیامبر اکرم(ص) را به عنوان روز شهادت صدیقه کبری عزاداری کنند.
◾️
در ایران روایت ۷۵ و ۹۵ روز به عنوان فاطمیه اول و دوم شناخته می‌شود اما در عراق مردم و علما، ایام روایت ۴۰ روز را نیز به عزاداری می‌پردازند.
@Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/462994" target="_blank">📅 16:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462993">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMscYdwsZ4ewFIzUXb4V0ITr1YO1iQN7jywY8K3vMlZSrsYiqrjCkglWSCUJNIwGlieiuFg2Wtg1-dbUWQq7vexiuk1QvAPZW63C77fENaC0ainJw2OLMNpF7EIsoB5Z50axYMRPnZTIsrv5efvlWTIDaUVg4vXGS_tpgmzfSOpVCSaGfYHXZ0jK2Saa601ZRWKeu9Ak5uPgXZaXbT0jRH1j7JxrH-1hgWLabpyJ-6KtbimmUC-reHAolezEaDnZ0CHrMGvR2MQSRIVjglb1g3dowoVm5Npg0F0DO0oS8Dd61X6YTfcCmycml5pSMfKyz0gwHZLIrozFUMI5ZYDIig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویری از بلندشدن دود از فرودگاه ریاض
🔹
برخی منابع گزارش کرده‌اند که ۲ مخزن سوخت آرامکو در شمال فرودگاه و ساختمان بخش بار فرودگاه هدف قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/462993" target="_blank">📅 16:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462992">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAyC55yU7YJkPqNCeQE6XpRXj-I530t9wH_4r3mkUMGnEVMcLU24kCnleEsiGiAsWlKqAWwjl4JVg3lnyH1fwHu7-ploHsyff7arL5X_nC-a4hZWDbony-2uherdq_Ov9hvVqB5Dj-1TBMvqk9oB5oanG6Q-sG3pgZETV0PhAnFN6IdZgyHTrJxCKhjvA4UAHvWstcubP0lNcNeT_tJE1XnKo_1sFV-CREVkYeGu_TI1lFsvcEG6dwdhSaSU7555TmGA9sf8b2QP12EqLOaosWZ5jHTjnjE_32tNi8WlBryvDz0QlFIW8o-G3YJC1LsjLDFeJnuP3sezjZUui1TQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیمه یا ارز ترجیحی؛ کدام‌یک دارو را ارزان می‌کند؟
🔹
«هرسری به داروخانه مراجعه می‌کنم قیمت داروهایم افزایش پیدا کرده است. من هفته پیش زیپمت ۵۰ هزار را ۱۵۰ تومان تهیه می‌کردم الآن خریدم 270 هزار تومان!» این را یک آقای 54 ساله که به بیماری دیابت مبتلاست به خبرنگار فارس می‌گوید.
🔹
گشتی در داروخانه‌های مرکز پایتخت، این نگرانی را تأیید می‌کند. متصدیان داروخانه‌ها نیز با اشاره به فاکتورهای دریافتی از شرکت‌های پخش، می‌گویند که هر محموله جدید، با قیمتی بالاتر از محموله قبلی به دستشان می‌رسد.
🔹
همچنین کارشناسان نظام سلامت با استناد به آمارهای موجود، از رشد ۱۰۳ درصدی قیمت دارو در ۶ ماه نخست سال خبر می‌دهند. این گرانی به یک معضل سلامت عمومی تبدیل شده است؛ به‌طوری‌که بسیاری از بیماران توان مالی برای تهیه داروهای خود را نداشته و گاه مجبور می‌شوند قید درمان را بزنند.
🔹
در سوی دیگر ماجرا، تولیدکنندگان دارو ایستاده‌اند که از «عدم تطابق دخل و خرج» گلایه دارند. آن‌ها تأکید می‌کنند که با جهش قیمت دلار و حذف ارز ترجیحی برای بسیاری از اقلام، تولید دارو نه تنها سودی ندارد، بلکه در مواردی با زیان همراه است.
🔹
رئیس سازمان غذا و دارو، در خصوص احتمال افزایش قیمت دارو گفت: اگر نرخ تورم کشور و تمام عوامل مؤثر بر بهای تمام‌شده دارو مانند سایر صنایع ثابت بمانند، انتظار می‌رود قیمت دارو نیز ثابت بماند، اما بررسی تغییرات قیمت نیازمند تحلیل دقیق مجموعه عوامل است.
🔗
بیمه‌ها چه نقشی در حل پازل پیچیدۀ بهای تمام‌شده دارو وجود دارند؟ از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/462992" target="_blank">📅 16:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462991">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجارهای کنترل‌شده در جاسک
ِ
هرمزگان
🔹
فرماندار شهرستان جاسک: صداهای انفجار شنیده‌شده در منطقه مربوط به عملیات کنترل‌شده انهدام مهمات است و شهروندان در این خصوص نگرانی نداشته باشند.
🔹
این عملیات تا ساعت ۱۸ ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/462991" target="_blank">📅 16:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462990">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25bf1edfe2.mp4?token=OBTXe8-AyBjecE61IE8HOl1NKMzeKh541WnAylTOyIbHA0OJDt4m3b9ijB5iOvP2k-rVx_rmbiJ0fBpaAMEjoSqPDXZXRxtgU8VE3ignjy5lom9B-58dTzI-CQjCwS6rIYUaWPzP_bqtszv9d-3ZtWlI3bJUq4RKWizHrXLmvoW6muD3fCxDVc3ESWpVPZaHBeH1ZSC2_q8HzP77DzGIFjEG7aTNa68H40_MmZflEXmBwGHBq35_kS0um3Ro7RYTaRRH60OJSGjETo-oIr_-kWdqxyv9Su1Gb11-e0JYryI0uXPr8kCYMKQag5FAKdfpFCMf5qnpCzNiwllOXSPNyXB6wPpInPQbDSibt1_X3aoBLBpRPKHKI8B1ZDrSfSXgGE-6VJu01IPwy_lDZBGhgf6XiT9kMzW_fXOcRya9sHvGBFx_vgqWM6Le6uxY0Jj6hA2tApexGA0722VH5ikrZ3hgtP48O5sf9McmvJaM6EFGL63-h4czfSMnTRcS0PQszVzqCLaZ5NByvA7dDqK3Q2EPv_WZ_-UgdjIz-6BGBKdsOAYRwQfnT0BVXQMbfYz1VXGIjDO-FhqYI8-01CueWtgy48cHr9P1vo17Peqr2MYzGgjayj6O2dzIlprlN4wRhGxAoEN9BLhUtF_HE_8jr568_z8_swpYlObi67T3sgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25bf1edfe2.mp4?token=OBTXe8-AyBjecE61IE8HOl1NKMzeKh541WnAylTOyIbHA0OJDt4m3b9ijB5iOvP2k-rVx_rmbiJ0fBpaAMEjoSqPDXZXRxtgU8VE3ignjy5lom9B-58dTzI-CQjCwS6rIYUaWPzP_bqtszv9d-3ZtWlI3bJUq4RKWizHrXLmvoW6muD3fCxDVc3ESWpVPZaHBeH1ZSC2_q8HzP77DzGIFjEG7aTNa68H40_MmZflEXmBwGHBq35_kS0um3Ro7RYTaRRH60OJSGjETo-oIr_-kWdqxyv9Su1Gb11-e0JYryI0uXPr8kCYMKQag5FAKdfpFCMf5qnpCzNiwllOXSPNyXB6wPpInPQbDSibt1_X3aoBLBpRPKHKI8B1ZDrSfSXgGE-6VJu01IPwy_lDZBGhgf6XiT9kMzW_fXOcRya9sHvGBFx_vgqWM6Le6uxY0Jj6hA2tApexGA0722VH5ikrZ3hgtP48O5sf9McmvJaM6EFGL63-h4czfSMnTRcS0PQszVzqCLaZ5NByvA7dDqK3Q2EPv_WZ_-UgdjIz-6BGBKdsOAYRwQfnT0BVXQMbfYz1VXGIjDO-FhqYI8-01CueWtgy48cHr9P1vo17Peqr2MYzGgjayj6O2dzIlprlN4wRhGxAoEN9BLhUtF_HE_8jr568_z8_swpYlObi67T3sgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پویش ملی «برای پدر به عشق پسر»
🔹
به‌مناسبت میلاد امام حسن عسکری(ع)، مسجد مقدس جمکران، پویشی در جهت ترویج «همسایه‌داری اسلامی» و با هدف تقویت و نمایش وحدت و همدلی ملی برگزار می‌کند.
🔹
با ارسال عدد ۱۴ به سامانه پیامکی ۳۰۰۰۳۳۱۳ می‌توانید از جزئیات این پویش…</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/462990" target="_blank">📅 15:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462989">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اشتباه هوش مصنوعی، آمریکا را تا آستانه جنگ با چین پیش بُرد
🔹
بهار امسال، تحلیلی از هوش مصنوعی زنگ خطر را برای آمریکایی‌ها به صدا درآورد. آن‌ها با دریافت اطلاعات اشتباه، گمان کردند که یک کشتی چینی در حال انتقال اجزای برنامه تسلیحات هسته‌ای است.
🔹
به گزارش سی‌ان‌ان و به نقل از منابع آگاه، ارتش آمریکا برای توقیف این کشتی آماده شد؛ اعضای مسلح ارتش آمریکا در حال آماده شدن برای سوار شدن به کشتی بودند و علاوه بر این، هواپیماهای نظامی نیز در آسمان آماده بودند.
🔹
با این حال، تنها اندکی پیش از آغاز این عملیات برنامه‌ریزی‌شده، مشخص شد که هوش مصنوعی محموله کشتی را به اشتباه شناسایی کرده است. جزئیات بیشتری از محتویات این کشتی ذکر نشده، اما منابع به سی‌ان‌ان گفته‌اند که گزارش هوش مصنوعی «کاملاً نادرست» بوده است.
🔹
به‌گفتهٔ یکی از این منابع، آمریکا «تقریباً درحال آغاز کردن یک جنگ» بود، زیرا هرگونه عملیات آمریکا علیه یک کشتی چینی می‌توانست خطر تبدیل‌شدن به یک درگیری مسلحانه میان ۲ کشور را به همراه داشته باشد.
🔸
این اشتباهات درحالی پنتاگون را تا مرز وقوع یک فاجعه پیش برده که در سراسر ارتش آمریکا و جامعه اطلاعاتی، مقامات در تلاش‌اند هوش مصنوعی را در تقریباً همه جنبه‌های کار خود بگنجانند؛ از تحلیل حجم عظیم اطلاعات خام که آمریکا جمع‌آوری می‌کند و انتخاب اهداف برای حملات، تا کاربردهای پیش‌پاافتاده‌تری مانند مدیریت بودجه، لجستیک و زنجیره‌های تأمین، همگی توسط هوش مصنوعی انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/462989" target="_blank">📅 15:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462988">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3670fcb55.mp4?token=RrjMYT6sgUy-TnHWcHuSBmsq9IHrbhm8jqSLEHphVFdG3y5C2f61VrYk6AyumwYB6XBYqb12wF2Xof125eI88FS8l-p8JDq5JJ8H9QQjr4KZhAcIDnp6zfB7dHWFsVFB4Hium1K1DoMaa_RIgAOfL_IzksQ9rHHRv_oxs-uTJMNojctzLJtxRp1aK7j3sbkj2h1H1Ue_eNOf7xD2q-n8J8C9zDexHu7Cu8mhekq_0z4_aZdINHZSvo7ks-b98te8SyBn3PboRcblCcLsG5lXozppCHqvP2TLjp80mFEYQ09agXoAg3EgX_3cpJnqUsjYZP1Z5dSBcs_xBllShPwQdCywkESU6npUf2RWzyYl-gjtdcQHWAta5azqOUAe16xKc70i00TLHig1dVaT3fCXlaaDA5mkIpbaJML3umNZ8nbsorUwgcItDzfMMEpWNq-RJyDcl4hAoojTiXSfB65yGdIu166QFdJVSANn99yXk9W4bj-K-dOliiS7CAUwStKFRsm3mNx3ntkwX3ZZnLrH03Ndo3kZKUdKTmW7OOl1mmAXSYQRVkz22YzxCFHvH2NfoxVVdMBpFfpcnpdvBsLhN6TmWBoRx5sWYE95vZ8_Jmm3QsDfUBcoSqY4h0QkQE7pswR5VnMFDeRVt-rdo63-3w-LaKgdTdzcM6hFgbFHDXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3670fcb55.mp4?token=RrjMYT6sgUy-TnHWcHuSBmsq9IHrbhm8jqSLEHphVFdG3y5C2f61VrYk6AyumwYB6XBYqb12wF2Xof125eI88FS8l-p8JDq5JJ8H9QQjr4KZhAcIDnp6zfB7dHWFsVFB4Hium1K1DoMaa_RIgAOfL_IzksQ9rHHRv_oxs-uTJMNojctzLJtxRp1aK7j3sbkj2h1H1Ue_eNOf7xD2q-n8J8C9zDexHu7Cu8mhekq_0z4_aZdINHZSvo7ks-b98te8SyBn3PboRcblCcLsG5lXozppCHqvP2TLjp80mFEYQ09agXoAg3EgX_3cpJnqUsjYZP1Z5dSBcs_xBllShPwQdCywkESU6npUf2RWzyYl-gjtdcQHWAta5azqOUAe16xKc70i00TLHig1dVaT3fCXlaaDA5mkIpbaJML3umNZ8nbsorUwgcItDzfMMEpWNq-RJyDcl4hAoojTiXSfB65yGdIu166QFdJVSANn99yXk9W4bj-K-dOliiS7CAUwStKFRsm3mNx3ntkwX3ZZnLrH03Ndo3kZKUdKTmW7OOl1mmAXSYQRVkz22YzxCFHvH2NfoxVVdMBpFfpcnpdvBsLhN6TmWBoRx5sWYE95vZ8_Jmm3QsDfUBcoSqY4h0QkQE7pswR5VnMFDeRVt-rdo63-3w-LaKgdTdzcM6hFgbFHDXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحبت‌های رئیس‌جمهور بلاروس دربارهٔ ایران
🔹
رئیس‌جمهور بلاروس: آمریکایی‌ها می‌دانند که ایرانی‌ها هرگز در برابر هیچ کسی زانو نزده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/462988" target="_blank">📅 15:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462987">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7touxZ7lXmHBLXCPoA527piSSmlnVK30cFFFcFx0nuRVxYZP4RyAchbPd4n2sq55seCT-1BUWaNILCUEiR-Qaed9xuqnMYP11Fz5XI7e4DEjKiWFH2phiCU6EmThi6db3XpY5fLuSNuocNanfJlpElKrShTpMd_-hDYltNEjsWKcWush001IodtRN0dQtNJk4i_GYcyeD2WOsparM_PtY1kcKolfcQDVqCk7zKeCkcv2Q__QeiL6Crm4Wc8kvclSmBxYl16S8NPC72FPPbYtq0Y9LGxnDofMb1NQ7P2jqDeFy5j252D4mYFlKn0oouKI8Ym4xJgQbCi5yExsFgXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساحل مازندران به کجا می‌رود؟
🔹
خوشروان، پژوهشگر علوم دریایی: اگر روند کاهشی تراز آب که در حال حاضر حدود منفی ۲۹ متر است ادامه یابد، جغرافیای سواحل مازندران دست‌خوش تغییرات جبران‌ناپذیری خواهد شد.
🔹
مطالعات جدید نشان می‌دهند که افزایش دما و در نتیجه افزایش نرخ تبخیر، این تعادل را به شدت به نفع کاهش تراز آب تغییر می‌دهد.
🔹
براساس مدل‌های اقلیمی، در سناریوی انتشار متوسط کاهش حدود ۸ متری و در سناریوی انتشار بالا کاهش حدود ۱۴ متری تراز آب تا پایان قرن پیش‌بینی شده است؛ هرچند دامنه عدم‌قطعیت در این مدل‌ها قابل توجه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/462987" target="_blank">📅 15:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462986">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">امتحانات نهایی در رصد پلیس فتا
🔹
رئیس پلیس فتا: همزمان با برگزاری امتحانات نهایی دانش‌آموزان موضوع تبلیغات فروش سوالات امتحان نهایی در کارگروه‌های ویژۀ عملیاتی پلیس سایبری کشور درحال رصد است و بیش از ۱۰ مورد برخورد انتظامی و قضایی با مرتکبان این جرایم صورت…</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/462986" target="_blank">📅 15:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462985">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f2c369a7.mp4?token=FXD2FiXe0_F22sJRA8amqoLDbzhQW9BsChg-mN3Sdspb9oRojvftzuwF_Df03EG2KmnRB2lsFcf-CyRGrC13z-RbiOIzQNOTnNuGNc6unb4zx6TgqA0A18C-X0XiKYyi41X6dhUHxc1osaYJgLKpauiYq_KbnFpK00RiKalZvwG3e9Uhzz7s88qsmX0N3Mw-hSIHFxcBoiB8SFANYn91rL1GHonHjnBuFf7OCq358xsNsWGVD1AbXwo-HySNwkoADwX2pq_6rV4BjF7uscUhW9DLygfwg_Aa1nk-K8GDUHX-_2aTlUZyG0NHY4B-iz5sbNaYS-XGVFgMp21ifhq3iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f2c369a7.mp4?token=FXD2FiXe0_F22sJRA8amqoLDbzhQW9BsChg-mN3Sdspb9oRojvftzuwF_Df03EG2KmnRB2lsFcf-CyRGrC13z-RbiOIzQNOTnNuGNc6unb4zx6TgqA0A18C-X0XiKYyi41X6dhUHxc1osaYJgLKpauiYq_KbnFpK00RiKalZvwG3e9Uhzz7s88qsmX0N3Mw-hSIHFxcBoiB8SFANYn91rL1GHonHjnBuFf7OCq358xsNsWGVD1AbXwo-HySNwkoADwX2pq_6rV4BjF7uscUhW9DLygfwg_Aa1nk-K8GDUHX-_2aTlUZyG0NHY4B-iz5sbNaYS-XGVFgMp21ifhq3iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سازمان بسیج: رزمایش جان‌فدایان محدود به تهران نیست
🔹
موج‌های بعدی این رزمایش عظیم و مردمی به‌زودی در سایر استان‌ها و شهرها برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/462985" target="_blank">📅 15:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462984">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">📷
رزمایش ۳۱۳ هزار نفری جان‌فدا با حضور رئیس‌جمهور  عکس: دانیال همتی @Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/462984" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462983">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311e3e5dac.mp4?token=BM0cf00qqEOaHVfASqgkqpsvfmaaIcN66lOkPIhuYWs8LvEW5xHRsdDUeaK446KFP8JbJcFn_KNJW3mhktDoF4cRjW5ReEp5UL3_tctYYMOzPNEAhqIp4AY5IQdECU84vhBqsuyUcQWPt9cm5ZJXu3o7otiQBCVUjH9m30czGSj2J1uhUH4yqUGV9T2BX2Rh57p0B4cs96eNpG7sUSiz8QcwT7vb32rY3UnjgM-pyijOwr408yTlbeh0jytAFs9F4FXr-okNAMhR7yWoeAVKyVsMCwFeWAYu3wkttmcaSyreEeuVNgdm79A7V2tM7edy5uDosZIl6lMYz29JgYzMYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311e3e5dac.mp4?token=BM0cf00qqEOaHVfASqgkqpsvfmaaIcN66lOkPIhuYWs8LvEW5xHRsdDUeaK446KFP8JbJcFn_KNJW3mhktDoF4cRjW5ReEp5UL3_tctYYMOzPNEAhqIp4AY5IQdECU84vhBqsuyUcQWPt9cm5ZJXu3o7otiQBCVUjH9m30czGSj2J1uhUH4yqUGV9T2BX2Rh57p0B4cs96eNpG7sUSiz8QcwT7vb32rY3UnjgM-pyijOwr408yTlbeh0jytAFs9F4FXr-okNAMhR7yWoeAVKyVsMCwFeWAYu3wkttmcaSyreEeuVNgdm79A7V2tM7edy5uDosZIl6lMYz29JgYzMYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رسانه‌های عربی: پروازهای فرودگاه ملک خالد ریاض پس‌از اصابت پهپاد یمنی متوقف شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/462983" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462982">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvmwfQhaZsSpWGdZa6_FvtzPmDTChU58iFyzTxZrQkMPO2Lp7s9lPPtBe1dULqJ4m_7LZeSg800hETja_IPjlbJQmDtnxauzVE502zEBIij1foJxAnNoQ84tZfqMEFYyFmiXXHdG_d52UwMyuSSXaByLpnBd8Y3gT47O-d_5joZiT7jTnfK9biPIPLc6Rb3okujRjj1kq26V6wESJS10--fF-BV7t9RKVh__JNFp07I61MC8tNtTZFIBYMZhdcf28HjYs6z1UGv94rgUlCgRKx-awg66d9etWoGg6zj9NjT1ouWlBzi_ypMaZDnAUlrs6BNxBqkkUmVwtDxj1lJqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودروی خارجی وارد شود یا نه؟
🔹
امسال بیش از ۱.۵ میلیارد دلار ارز به واردات خودرو اختصاص یافته؛ رقمی معادل نیمی از ارز مصرف‌شده برای واردات دارو.
🔹
موافقان واردات می‌گویند با جلوگیری از واردات خودروهای خارجی ممکن است سرمایه قشر پردرآمد را به کشورهایی مانند…</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/462982" target="_blank">📅 14:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462981">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e0cd9dfe8.mp4?token=vSvhpL6fw9-GcMv8PMIBQGUo_kgHi_jdUjlurVVbkQzNM9RJleLNGUHBOLlTO3TrtbEamESPs3sIkp8KM_vm8HauSbFgsyqM3LBUq26u5o0u7hF3UvW36KYKtUgCBIKzqV3Y1pzDKZjeQcW4aVqNFvhfbYE4h9KnOAExeBCXUMW0eKgz_YFPlgw4VG54oCwNlndae1HN6MkWoLuAxc9iFt0qW17kaVotg0F-Cx4v1adj8s9260iucH29J9uKChcPpyMf_HBseFyKLSzvDIJ_xs87lNbHOSeJTa-h3ZKQPohB19skKsUR58zPl2WGDLzm6ql_lORKnuckvKo4b3WJAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e0cd9dfe8.mp4?token=vSvhpL6fw9-GcMv8PMIBQGUo_kgHi_jdUjlurVVbkQzNM9RJleLNGUHBOLlTO3TrtbEamESPs3sIkp8KM_vm8HauSbFgsyqM3LBUq26u5o0u7hF3UvW36KYKtUgCBIKzqV3Y1pzDKZjeQcW4aVqNFvhfbYE4h9KnOAExeBCXUMW0eKgz_YFPlgw4VG54oCwNlndae1HN6MkWoLuAxc9iFt0qW17kaVotg0F-Cx4v1adj8s9260iucH29J9uKChcPpyMf_HBseFyKLSzvDIJ_xs87lNbHOSeJTa-h3ZKQPohB19skKsUR58zPl2WGDLzm6ql_lORKnuckvKo4b3WJAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سال تحصیلی جدید دانشجویان آغاز شد  @Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/462981" target="_blank">📅 14:48 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
