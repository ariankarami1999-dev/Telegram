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
<img src="https://cdn4.telesco.pe/file/hifPu5GDa8jtfV0viVJp9frf4UCPGdMol0Qdg98lNebRu7rTO-o5EIqIiEk8r5jsr6hJCX0A55l7Z7yi41xrbjoB80k6cSkpmBdjXqg90xGwHy57ZFRemzfZwRCM19OzfmsYKXtfUNuVHynWqjevyu0ILe4CTBCg3AoqxjCWWDZ9jzXUQqN3PPhSy8tUFvxmVv25XCShb_-rrrHQOmDDQ5z3S2L6A71_He3z-kTM6iUwforljftFbDTaE9hdsHQ2ah4n0pVH_psXs_kP5qYJQBgCOhB4uzY8oTOx9zBNYbubpCl0Tj5QuZzKy-CT7p7BUDDmHOWlVZaFdx3jPjjZvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 04:35:40</div>
<hr>

<div class="tg-post" id="msg-452586">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7feTSgJxa6mYaK-spm-lMKLkMfbR4JaeZ5zwKCApWfMUN_vEsj_9fQO5bb4o1CbapBxI1Blc2arKYKKzQ_ixgamNjhpepuOWYHRQnri_A74I9GM3Ss4TCjBRkRDeCv_fyxDcYIOt_kDiMjXnw9UW7C0MEkFQtm5UrKUUhEYfhDI9EtCuXVGA4JKg4_dBH8sR6aP88Oeq2hnO1SaG9WUbdMeB8YoqXE38ixQqm8DTC1w32G-Q9dwbdcwwAzNzKwPF2zvXXCDHRlD5dtAWNGx422Vx-VcRSCPIlwClV-s5qeGgs7j_XHu5lulZ_5bauy__8tKX_rIHy4U1mHDCKLpRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/reONUq4Ay4kkt2-WmmutWDtr5LwR_98s7EyHVfTZ2TanHbgzUIW55JSsX0vxAcnjZ6ktd7OpjmFqyEDi2scht-JpnDT3WyRuubrrW0NFZq15mNsJIz-iGS0P1hkZQ-bm15BGAVHQF3jLZfJoWRl2PYJocTghVoCiiO_6qnz8nLnjercOrd_S8PAY0V4lHvGlN4vMpYnti_Rxe90NrLymgmXaWgB_wEn7YcoBa75IDEzzoQaBjB-pekaK9g_a-nkkW0M5TF7qeeg2dH9FmsvQ6GvE8arBCtUWVPVxGHt-YtJqNfB9AR5y-vkYgUh9mFRgCnkmT-isnWPFysDH4w0nXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ln6kgz91MAGs2r9y5PPFejMX0yff-t_4HxmUQVTC45BoQ-zs67UZ6tFuLeJXTNaXhQPCW8fg0jTXBlvMbj-4YGU977tCnxvDDe9Q_s4D7iLaRQiyQBFxsqvQdPLjHieJY1BzBGBcoO8Z7iSHqSccmm-OMRkKxp68qaKjUniyybPB5oK3USzTjWLLCxQott7y8GJG9kXNGk6__21xy7HyxQOLher9Js4kwCUs8OhVgwjLIWIkI6cskiif0Qk9zG4K9C8dRRll-tFKOd5atu5EnxIOM6coeXzPAH0r3_0vt5P2-4K8Shcs2Hjs8HQVFZNUVSobUx-IqloRauvaEKJfng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از انبار مهمات تا انبار داده؛ چرا مراکز داده به هدف راهبردی ایران تبدیل شد؟
🔹
حملات اخیر به بحرین نشان می‌دهد که الگوی هدف‌گذاری ایران وارد مرحله‌ای جدید شده است. در این مرحله، هدف صرفا انهدام تجهیزات یا زیرساخت‌های نظامی متعارف نیست؛ بلکه گره‌های پردازش اطلاعات و محاسبات، که ستون فقرات ماشین جنگی آمریکا را تشکیل می‌دهند، به فهرست اهداف راهبردی اضافه شده‌اند.
🔹
بررسی مختصات و تصاویر ماهواره‌ای نشان می‌دهد که طی دو مقطع زمانی، هر سه گرۀ اصلی مراکز داده AWS در بحرین هدف قرار گرفته‌اند؛ موضوعی که از وجود یک منطق عملیاتی مشخص در انتخاب اهداف حکایت دارد، نه مجموعه‌ای از حملات پراکنده.
🔹
این توالی نشان می‌دهد که هدف، صرفا وارد کردن خسارت فیزیکی به چند ساختمان نبوده است؛ بلکه فشار بر زیرساختی بوده که پردازش، ذخیره‌سازی و تبادل داده‌های عملیاتی آمریکا در منطقه بر آن استوار است.
🔗
جزئیات و شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/farsna/452586" target="_blank">📅 04:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452585">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نیویورک تایمز دلایل اصلی توقف حملات آمریکا را فاش کرد
🔹
روزنامۀ نیویورک‌تایمز به نقل از مقام‌های دولت آمریکا گزارش داد که دونالد ترامپ، دست‌کم در مقطع کنونی برنامه‌های خود برای گسترش عملیات نظامی علیه ایران را کنار گذاشته است.
🔹
زیرا تشدید جنگ می‌تواند ذخایر موشک‌های رهگیر پاتریوت و دیگر مهمات پدافند هوایی آمریکا را در غرب آسیا به سطحی نگران‌کننده کاهش دهد.
🔹
به نوشتۀ این روزنامه، موضوع کاهش ذخایر تسلیحات دفاع هوایی تنها یکی از عواملی است که بازگشت آمریکا به عملیات گسترده نظامی علیه ایران را به اقدامی بسیار پرریسک تبدیل کرده است. نگرانی از گسترش جنگ در منطقه، آسیب‌پذیری متحدان عرب واشنگتن در برابر حملات ایران، پیامدهای اقتصادی جهانی و تشدید بحران انرژی و پناهجویان نیز از دیگر ملاحظات کاخ سفید عنوان شده است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/452585" target="_blank">📅 03:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452584">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea8682337.mp4?token=UYJFzJLQjK2ZFJHQ4MhPE2fXiSGp0sG9uYVQoZwVn73oJhMhaMeAamCJNq72s4Jn9aqgNoj3m7F1uiIYjYx2YcWwO1ullnAfbxSng7hTghcigZk4jmgcCbx7ZS3h1VCFUwqkfSzFBk-51H_xCRdvvZIeVUzTRMoCmP2j5WPvkzTGn-j3psdunCRfpcfUvho5B3uxr3BAD-mSghq289OM-GAN1dou_ShkhiPsOqdSN-q_ckbHR526wUcAAkeVRx2yOEYIjEP3WmtmBA9h_JdXFwjLn2ygK386n3ANFrnAOzqlkhtJdnRXPMF7_14vbyleqUVGNDG4QpJfg4SuszxvUy4qnQe8UVJdXqgz4gtlol3Qzqt3HPEDNKkh55OvT8CHH3T-MgNaFuURXqt1QUoTNf2ExuJH0Cr0IJdTOFWRdUu9Jjobh6g8EM_A6P4S6eyrCq4UWtuhLi3WqF-LT6ru0i_czoPVZq86IIYFuS3R0D-2t0WFd8YnVk81xr4HX4FGOoy3h7XHYjYELHscPij7eZ4LJT2Jok_EXOe29GXUl1JPBn4HQ5Pr3l9PotSJikpz8q_qKXpcYdDDU7c-Igpr6zRnaO8LjNd7d_tEJDDdrnVe4fel_tB-Gq4bmHEd2xwZnlek2TYXVp5yisbzT74plfK7suXORhQdieAfU9JTFLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea8682337.mp4?token=UYJFzJLQjK2ZFJHQ4MhPE2fXiSGp0sG9uYVQoZwVn73oJhMhaMeAamCJNq72s4Jn9aqgNoj3m7F1uiIYjYx2YcWwO1ullnAfbxSng7hTghcigZk4jmgcCbx7ZS3h1VCFUwqkfSzFBk-51H_xCRdvvZIeVUzTRMoCmP2j5WPvkzTGn-j3psdunCRfpcfUvho5B3uxr3BAD-mSghq289OM-GAN1dou_ShkhiPsOqdSN-q_ckbHR526wUcAAkeVRx2yOEYIjEP3WmtmBA9h_JdXFwjLn2ygK386n3ANFrnAOzqlkhtJdnRXPMF7_14vbyleqUVGNDG4QpJfg4SuszxvUy4qnQe8UVJdXqgz4gtlol3Qzqt3HPEDNKkh55OvT8CHH3T-MgNaFuURXqt1QUoTNf2ExuJH0Cr0IJdTOFWRdUu9Jjobh6g8EM_A6P4S6eyrCq4UWtuhLi3WqF-LT6ru0i_czoPVZq86IIYFuS3R0D-2t0WFd8YnVk81xr4HX4FGOoy3h7XHYjYELHscPij7eZ4LJT2Jok_EXOe29GXUl1JPBn4HQ5Pr3l9PotSJikpz8q_qKXpcYdDDU7c-Igpr6zRnaO8LjNd7d_tEJDDdrnVe4fel_tB-Gq4bmHEd2xwZnlek2TYXVp5yisbzT74plfK7suXORhQdieAfU9JTFLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد روان زائران امام‌حسین(ع) از مرز مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/452584" target="_blank">📅 02:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452583">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ارتش تروریستی آمریکا: تاکنون مانع حرکت ۱۲ کشتی به سمت ایران شده‌ایم
🔹
سازمان تروریستی سنتکام در بیانیه‌ای مدعی شد تا امروز مانع حرکت ۱۲ فروند کشتی تجاری به سمت سواحل ایران شده است.
🔹
همچنین این سازمان تروریستی گفت که به دو کشتی حمله کرده و آن را از کار انداخته و دو کشتی دیگر را مورد بازرسی قرار داده است.
🔹
در ادامۀ این بیانیه آمده است که نیروهای آمریکایی روز گذشته عملیات بازرسی نفت‌کش «شارمینار» با پرچم کامور را در دریای عرب به پایان رساندند و این شناور اکنون به مسیر خود ادامه می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/452583" target="_blank">📅 01:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452582">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVvmL6F4KvoR-zTWxxUCSwbNPYN95-HOBIZW1bCkw9DYJ6d-FNd2RZR8UDxMH2D-TzuvfTmmAus6pmBJq-bEjZcpG9mzS1P-Tnuq9Bv5rJD8iO21vZVKce99YiRBdPIeuX7tdwkUewDNzCrHvDKOF7hL4YYt8DyU7esplMeQBVfqbiAJoXgU0B0pGSRVBGiToSkDIclMv_xzZ6T6aUBy2frn2ibr6vUCBrehQuQyTefranKEhihJk50q_6xP8snWK16lODZLQsZqa4zg5ZrRKHOXuX_5fmgoN4ZTUzt_4ffjA5IGSjC0ZIwT63SjVasFEt7VhlZrmwwe0LdvINnZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میش وحشی قربانی شکارچیان سابقه‌دار شد
🔹
۳ شکارچی غیرمجاز که با سلاح بادی پیشرفته وارد منطقه حفاظت‌شده ورجین شده بودند، پس از شکار یک رأس میش وحشی، توسط محیط‌بانان دستگیر شدند.
🔹
میش و قوچ وحشی از مهم‌ترین علف‌خواران مناطق کوهستانی ایران هستند و کاهش جمعیت این گونه‌ها به معنای کاهش منابع غذایی برای گوشت‌خوارانی مانند پلنگ و افزایش اختلال در اکوسیستم خواهد بود.
🔹
به گفته کارشناسان، مقابله با شکار غیرمجاز تنها با حضور محیط‌بانان ممکن نیست و باید از گزارش‌های مردمی برای مهار شکار غیرمجاز کمک گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/452582" target="_blank">📅 01:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452581">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDaWaFlFH4TUTtbjefIc9PcWEOAZApZxLJ6gOA1PBDOhQmisPUFC9TY3aAQeIkfu-rqx7n1me-dyxSkJ1m5_l-pT9pRtLb018gdFXqjnEVijfUkak0ZMVQE9HK_57VuvKtcvQNgNq2uEzk-WO7pfq3123o1PwePcZMe5SQnHywCNw5v80nEr6sl6Z2dmoo4pX3Mg9PX8rRFbO9ekxe1269tLDilwYcE0rs24FEfz7KZpHJGj6BDHFpxDhwvyxB_cEe0jqKJPhEFLSlCn3L9wkRGzkbKWaclj1RqksSrHBa5ySKiMz3RDYtxgZ8dEc7mC-BAo8vbbhPMj96r7BwXq5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد ۵۰۰ هزار زائر از مرز مهران
🔹
استاندار ایلام: مجموع تردد زائران از مرز بین‌المللی مهران از ابتدای ماه صفر تاکنون از ۵۰۰ هزار نفر گذشته و خدمات‌رسانی در این مرز به‌صورت شبانه‌روزی ادامه دارد.
🔹
ظرفیت پارکینگ‌های این شهر برای پذیرش حدود ۱۵۰ هزار دستگاه خودرو فراهم شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/452581" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452576">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuw3HkNKfUo9YSNQ7AsZUEq6hWGOwQQNNFQ8D_XLd3zz0A1Hf4TAysoLGD8e29hJbUilSOSFBgoAby98sq834G3sqMC1LH7mMzcWrliyJDS5yn5fY9W1bjfOc0rArRf7UR-SQafP1YAZxn0X-Fk80AwgekLi6PxpcrgL6PVdZLvfpWALg52DZPiPY8pnf75z-YwZ8cjt4mgjORTOzcaJv69hCH2aFfasD-jujSLdjulZLIbbRSaZwEJlQkeooxrGeeRC9eaCgtAkCtYlUYGIzOmpUXJG5BSPHrsZIMo-T1pf_6bR8Gt30i-GDVN8sQoOk7OrQpgvbdD45RkK3UuQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z9M28tBpLsyn8pfTHoVSQEc3NPSx72ZXiSbsNPeMKQQz47GgCV4Ix8t6rjjCcqE6_4-9jWQHJI3vzYf2YNXSr_fp3Kmmr8xYbJojP5GVZew26J027CcY-7g0fFkobb4lkkUw8MfhuapbjStEzbS5jkyHW2eNDAs81H4YLbAwOVRGjYco0PQDW0Y2qbeDagw0nYoUi5YKOzf5FgM5kF17XnBJkQrkKfqVslDVShoDC5vrm9O-rzTMPAuqY2s5OdLOOGaA9Nxd0pBCbwfhxV7dh6s1zSvLZg_yPNC0jiJHdEPcZrXTVnVBLt9POavbEk-yKj3LtYFivgr0SvlT02Drcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOywaB6ySyF52mQYeztURb_9mtHfApqiwjUswMtGPC-sG4IGO7ceEekp2EIY99lH3y1fhPdhiFywuuJOgrtLWnoYZRHhDWlUGGNqEHDVNesacwsxicUKb3RE7r_H8IyNL10bXGy40TpHo4PR4z_fskZPMm9KAEUMrvVJijoXpB4ElCRCROJCSFjlJH3ycIaqjoAhCHW6UDnRne1sRD03jZQmWnMYODUmGBByZca5PJ9HEVNZJNXcbhxlymYa-OkrCkx3z5wBkH3WV-jI2YMs4X_UuU8eXi3CQ1LwC54tXZaxKdjA7j-EWOioUoDF74qmi9ak5YGcf3URlxdTH9D9XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFnJdYniZM7qW-AjAZwM5qdsPugSUUMXGeFgkaexNlL0Qpuq_u_tImM0CfhX4gcP55YZ6wDXgcNm4RowpYBGoDUz6egQeQAlY_ONTYudIDYGROWgOh38KCTqebYU7xsvQIDEo3g1rsBBkKtr_flPbNAOUWii11ztrziC34yUvfsY7-NE7jFGme-WtniPr5n6uwcY5b-8wJC-9qYGrYwYy-PJngc59sVDxFVtIRbpVSFMhaRliLBbBEkHmkul17ilQe822SFuxPQ2JAxDA4BaeF-hJmRb38MA4Fg-ZrRQY_YIvC0ZBcVo5BLB5CtQX0NfajemllIX3aSwsTqL3llang.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dsXld0g9hKM9lHLJf-oZPlC80BmBQ968FTuuHxpLoq9O3JM3-xNkBf7L6H_85pNzeR4VpE4OuTQV_xsCRIU9bQtxqqp9Yrur0mx6uevsDv24C9c5oUXs_tRQmlpQEXnGzW2Oxgcp7bhSE3uJttj9MyVZtTxZvm60rYvmvQbIVhv630dQPaQ_P0UBWHGdoxCHSmYtEWVWvVYn3qD-uRIYsKuXbW35mfuWkEor18XihwE4g9PBbD1uTSlqLvEc0vNwkQckp9bsv2NydiQayy0MFrVBe8dK-fvl5-FXZ5ulSkxPlHMnxgVSrYVu7nkCGI_fcKGahP5OyK8HIAZdqV8v4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یکشنبه ۴ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/452576" target="_blank">📅 00:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452566">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/shVBYWoGjSirTUJu96LmhMq7NryEmtSmn3acnZHNn27KU0J_0vWPQQdIs8JnKSd_j9zyzSMf8pmF-U-tj64YnqF6ukYvamQDEhRfkXB6sgbN6vGFmt563DYkA3W_Wcx56-nT6-XREvnLu70gLibBLycWSxFkIXx2j2UzQ3HFcuX5Z7rB8nLoB1GMH3yjCaeon22AGQngKTYUwPiBizTSkqOZXQi71iIeV2haHwGXMVYTPSZ_REhaIZjJeRPwG0kNpYdjcuL5O27lm8228kjgnlvr9pcqCfu0IPwzTeAAHppk8O4UwZptp8cO9SSjKvIb_u-v-w4MAUARw3f0iY49vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdgKK32cDKkIRitn-ueThN2ka0IArXImRcCn2ZTOYzEHSa3XuXH7wuRuJk5QSiqeVKP69cCr9QLRp0SEzw3MRogFamMf1rH-J3ViUvyac_LMrPCSJx4II7SyO__vQk0hxEnTSRNdUIQt_gSpTjgCR6KDN7uC-EdTcvifFa2ypUEvrSB7bjnHI75l6HB4ua-TM0_UpFlc-vCZtCrQ_Pc0lzvcrqw2hDVyzjIKJqKYXXybUZRFtK-oZBIoNYb4utQq6ru3u8SYkwP92fekR5epFdDyNmG9VGh46YfT-DW-cOSTw93T-B-quHLBGrXWSCTpMWxgHfleNEm3P2-XqJ7HVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mr-Zp47LfFdx0Bw_uuFK0dAqbBGYYTj7avl4yVrTZVhTZFk_ADWh0qvomn7ezTwtB5WZ8ILxcH9f-mof19JI2n68WmYQZRoGUUIwQ-LEsQom5FxeUoIgDGCZHmlb0uDNVfuLLCilYVuOHW1piwoiwF5-E0Vg7Sy6GwiPCL9poDhoBf2QGC0ZYcR9jvehprC5HWYbM7UFKPDq-L6WUalkA5RibB4w9ljsHXtVT94obO6Lh4YgtWJ5tZN5RHLWV257GQqIZlq5zXAjQrwod44mKmtKxW1x-0sq6rJqIHxp7iuOg_gUueIeQA0uufiQp6NSCR20wCuI6kgkgLHJo33iMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPNWdpW3-hFHtIxcmyat91Q4pz4YKpyeMcBPFKl2KhZplCWHL_tAXthcd94_ua06Arc-iaUZizoq9oBmNQa77-8dDwzhwuR5285QnLToh8oI522ibNVLHYEIraFcE3B0hX3v0IqUQPotWwlqhjH3XAameZxrHGXi0DyJFtTNyBNRVJCPGAGon7el7neK4KUZfWXoZcN9VTKCvrdjL3wqzCABmHFyyAx0IZgG3fsyFp3eKJtKizgmEIBh9K4Y7M67V4wlvyuyH87dAEpT2yqcLJdyNqPo0_usoRFzLwGE54sbjcCYNRS4p9nrX_ldb-SWHmsN1m5JOwQpeeMQOj8rEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoNEtnMppdnCbm6b_CtVd9QgEKGTmRcZI1B4hmKM0XSQYB_8FBf9EAbjt_IyN_FTZHkEERkm0NRXMiROSC3lLaEYcB3jyBSNPW6_c6GpOU6nXBkP59RTfi0N4S0Who1Sozid8Z9Uh8TyLEgjg3GGRA-Y7oYV3LPjm3I68u0GmLwxWVtjTw2gBfHfSaSrYKMZYCV2oWr0aFmHxwkB_cc5YqF7su1aiFlzW7uR1ZNtDB5EgRGHnJF5V9WWhn5UT38QuLoUyafErl4hqSwPagLCMUnXPAtxenFefRoYdAB9lItbDliRHzbLhxverluS6YKuyzTACruI8dGME5hcuW_1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yn64mAoeh9zrKryIqfeajFLvFfHb0wcOUiP6zq8wP5xHA2u06n98PmxGHGwZ3Y3-Y0vbb7VCyrBu_1rCAq-Ot1XX1HKBsSnyvJ5_NiFcGfmyO74tRH21DZGey5S_zFALa8aVGYCD_YU5bskOkcC_tk6IJKb7-FpD-Xi1mZrRXsEEvPaXZHfZjG-jBYUSjF1_OWkQVVD2FFoUFJbEVkxz29ZqmqazJisUiIHO0Q9AU5O0GQHwWrdB-ahPXh9VPVYFS1kvb0fFFTc-22E2xzy2NFL3xeV2D00UukHB3qHIrzmnFZleb-GKb98DlxrYzToZAejVIQmrBMxlvstv9lZnMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V8l7ojzzIBqPLnt87KO364v00mjqe_LZ7WJbm_ck7W7fa3OSeTIfQvnB1LwWv8IW5M-MoucG7Q1SsLiyUGeWmQc4G8tEMersZaZyXxGjojE-KieRCkZdDg90DrmWwix4XcqA3yGBxpUXk5IiaFFwuRsyqiV8NY2TLBv6V4O3_7tAfYLQ8iHko6Iv67BS9bhw2dR4z50Pvn2jAb_JJOh5IEvBQ6GrwtzB-HTD-GEnsKeXWHrgQ1rBgXEIhBqa_JJMmR3h1DI5ICHcq7CStfGEPI4w3IkBvP6Bwo6RfCMqfRLoT_dt2QJEmcDLSwYdV31gCItj5IBHGr6dvRC3QHfs3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBnGjkteIR4-jvgK33nqEIqSTQsVPEzU4W9Pd17rjKZGfjMDKvsyvF426wRBZHTGgGyf3smgfRoQ1z0nMwJnGZfMNeI5gFhOWJr9mqmoZR0a9oz9aVuSPb9pXrndKwpFmmnCaFP7yFbfN-Z3aZOLEvp0RbAeerUPUbbI_yCNttoo02TWfgvG1OSleSAnfLIXZIjqUibygyQwzRLLzuKj52Sw9g3IxsxDLtkCalbbiqepH8U3vEJxvB19-fpYOlLEu7Eb7NLuMnNdMMYiPCO1YaacqPi650E9aK3pL1AwIKgrAueoKiYdzYJom1CRcJSrrQvNkISWDMEe0HTrZFWsSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bnyyqH4pyqe-RmcLQPaiUMOcwHucVy_9UTj1yddnq6F0i333Vmam0M719MyUSeq5PSy2ni3p67rf3_HO3UrZpwh1pVLCCgltRuOp1LK5UbA22vA7z7JaBJy-Zz4WP5qDSkgUO6Y-XGxOoPCtE9n0Rt5zJqBH-TyrW3wN8N2R-sI61_i-HZCI5LGdQaQ--68-YR3XiIk8WlD3-SbWtB4eQBCONGcRRnPi78BGa7BqzJfNOGN3e09Spgzh43i6aDnkasGrPrqaplWp-3_RUKxCIPnuPD3tALvYd86z7H26GMYcRj437s4Gyne0cI_oxl4NspGvyauw0bbtwn-keTBl3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tHfjb7dvsH37r7EMAL4zhsC-zrtn9BM9ofs-F72ikOJI-XtPXIX8gbG7ky6WZDQ4y__hqSQLzaP9rHLJkK9QpqshFBUL-FEpVeP6C_WMxYZa3TY5DfWuaUSGkd7CFbv3T8HpfNQiNe0Ff8ljAfSj39ex_jZvkG2JDDZFxxwcNzbDSjMLBIAxk9eXNoFNmLiKetvab0w3nk7M1afkWfsZqJi2ynOLO3qYyFApc3o_T8bB6KiowI97kqryEcFlkw6NzsMxKdNkMUl1GDQhEkqyCU1RIu1g9H9SzhkCckv8iW9X9vds4ZL7AhCQ3j6fuONlR08sGlGf06IxK2LqLkaFkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/452566" target="_blank">📅 00:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452565">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9902904ef9.mp4?token=byXgEdbA2Ft9DBN7gSAyO06HjBhYxQn50QBhsSB_zXrbmB3f_oZtKuv4-K5R6z3UH46fAvkRSFkS09jf8Y4BppHP3VmCYjKLcycIR22CNivXpv8sC6enVau8hAtHCgPWFPVFmU_mIzMd_0d3xW6kCK9ZXW7EwPFUdszPzf2rVS6V7ySFi6iIIzomjFnATKS2rx18jskZ2_Fdz7jCGuSQhpdXqbKQNtXeS-O99EIlJbvh5ZfW3mFYkK7Atj3Bw5GAcDI5h6EdVWImcRHqUWj85j5gmVJjJVycytSRn3AeZ9Vk3N7XNXUZuT_Dlp4U8eKt5npcr-kk1G8Po7jDesPsCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9902904ef9.mp4?token=byXgEdbA2Ft9DBN7gSAyO06HjBhYxQn50QBhsSB_zXrbmB3f_oZtKuv4-K5R6z3UH46fAvkRSFkS09jf8Y4BppHP3VmCYjKLcycIR22CNivXpv8sC6enVau8hAtHCgPWFPVFmU_mIzMd_0d3xW6kCK9ZXW7EwPFUdszPzf2rVS6V7ySFi6iIIzomjFnATKS2rx18jskZ2_Fdz7jCGuSQhpdXqbKQNtXeS-O99EIlJbvh5ZfW3mFYkK7Atj3Bw5GAcDI5h6EdVWImcRHqUWj85j5gmVJjJVycytSRn3AeZ9Vk3N7XNXUZuT_Dlp4U8eKt5npcr-kk1G8Po7jDesPsCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله با خودرو به جمعیت در پایتخت آلمان
🔹
منابع آلمانی از حمله فردی با خودرو به میان جمعیت در جریان رویدادهای «روز خیابان کریستوفر» در برلین خبر دادند.
🔹
روزنامه آلمانی بیلد گزارش داد که در پی ورود یک خودرو به میان جمعیت در جریان رویدادهای «روز خیابان کریستوفر» در برلین، تعدادی مصدوم شده‌اند.
🔹
این روزنامه افزود که عملیات امنیتی گسترده‌ای در محل حادثه در جریان است، اما تاکنون جزئیات بیشتری درباره تعداد مصدومان یا شرایط این رویداد در منابع موجود منتشر نشده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/452565" target="_blank">📅 00:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452564">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رسانه‌های عراقی از وقوع انفجار در یک شرکت سرمایه‌گذاری اماراتی در استان سلیمانیۀ عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/452564" target="_blank">📅 00:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452563">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea1b1cd5c.mp4?token=uyKLIIEhnn_U9dIPGaGw1pIOOIDmTixUli6p1iL6jsI8AW6lNKXMaVZ8Af_FFIeDgIYaFsrSIwu2DtDH_aaYpF_z7w4Kp3oYSJ_ambg2PBdOHIbUUCe0Mn9CjqJ29m9p2xRKSecU8Tb5JoJmBI3RrQoCTXPXHdzv-PqjcO8vKvHoLvFtw-A1F3qtycUsdYskjr1XeqIbpgotYqVrnviqzi2q6WzuAXVBSPqW1Cm-FUU-ArLeHTYsEjTlJ0YM4hd91VnIehwBKsScLAYxn1WseiSgXcCY11pzFYMTU28jVkxFa_SGottPIZEnP24Au1EHsZ4hKmyrNIOvp4ZEEu2Gxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea1b1cd5c.mp4?token=uyKLIIEhnn_U9dIPGaGw1pIOOIDmTixUli6p1iL6jsI8AW6lNKXMaVZ8Af_FFIeDgIYaFsrSIwu2DtDH_aaYpF_z7w4Kp3oYSJ_ambg2PBdOHIbUUCe0Mn9CjqJ29m9p2xRKSecU8Tb5JoJmBI3RrQoCTXPXHdzv-PqjcO8vKvHoLvFtw-A1F3qtycUsdYskjr1XeqIbpgotYqVrnviqzi2q6WzuAXVBSPqW1Cm-FUU-ArLeHTYsEjTlJ0YM4hd91VnIehwBKsScLAYxn1WseiSgXcCY11pzFYMTU28jVkxFa_SGottPIZEnP24Au1EHsZ4hKmyrNIOvp4ZEEu2Gxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عراقی:
وقوع چندین انفجار و آتش‌سوزی گسترده در استان کرکوک عراق
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/452563" target="_blank">📅 00:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452562">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ادعای کویت: هیچ حمله‌ای به خاک ایران انجام نداده‌ایم
🔹
با وجود حملات مکرر تروریست‌های آمریکایی از خاک کویت به اراضی کشورمان، سفیر کویت در آمریکا مدعی شد که این کشور اجازۀ استفاده از خاک یا حریم هوایی خود را برای عملیات تهاجمی علیه هیچ کشور همسایه‌ای نداده است.
🔹
او با ژست صلح‌طلبی ادامه داد: موضع کویت در دعوت به آرامش، ثبات منطقه‌ای و دور نگه‌داشتن خود از هرگونه درگیری نظامی، ثابت است.
🔸
این درحالی است که حتی روزنامۀ وال‌استریت ژورنال به تازگی مدعی شده بحرین و کویت در یک اقدام نظامی مستقیم و نادر، اهدافی نظامی را در داخل خاک ایران هدف حملات هوایی قرار داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/452562" target="_blank">📅 00:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452561">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">منابع عراقی:
در پی حملات اخیر ایران و برای چندمین بار پیاپی، سفارت آمریکا در اربیل هشدار شدید امنیتی صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/452561" target="_blank">📅 00:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452560">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">واکنش وزارت خارجه به حملهٔ اوکراین به کشتی تجاری ایرانی: ایران طبق اصل دفاع مشروع، در دفاع از منافع و امنیت ملی خود تردید نخواهد کرد
🔹
مسئولیت پیامدهای ناشی از ماجراجویی رئیس رژیم اوکراین، برعهده آن رژیم و حامیان و محرکان آن خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452560" target="_blank">📅 00:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452559">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b3ee1c54.mp4?token=mCTbDSmkBnQa_r4D5fDjvtkHb6Wio7HXRJIO8kUQLLk45uNhbdW3z9uXH_TfIV6bpJ0P56ZpazKvdmMfM-kplcjF5haotMs0HLkXd2wujPqaV06w-nJBZFdg_NkFEYMe6bSbQuAMSbKYn1Mth8hQTxKfLoGWt7bvLB5XO_HU_ePmmxpIMTxK8LwbMa6emYJzY9koBGQ5CKgeJiDEeb9u2izdZ0R7ujS6LuRzy5FmaQbLkaBgju_Vhk6uYhhL91DqJQKB-Z6DZw2z0wc_9Djcrvx8yddIxAGqqKueJdj9czEdul1K6xfhOTB5NKgFlAkkEz3s-gihI1c6GA-1YmDmtW660a2JuYz6LbN1bE7yZ57Dpp-62OnPmHKX5REXgbNyhI_-aziV8NqDJ1K-g6Sw6SVRj0SslWth5QKN2ykhqTAfd0WHnJA2N3j26hlaiFXMcz7O1qN5DZMDG1laxqWZoe3gkFD-x0hYIOyehIMtz0oqxwBQouFEBCM76rK4x4RKMgIotDyGyDS-dAoMcuQuu1_qOIgrPGlSJBRB5ChU2Dpgnd_hhyiIorBJbOdw58ehEL5v4FysmUlF3w0lYrPBF_rpSWggU3ssikTrNR-mL7cCnJuFMK_F-R6qKgr8LKnx4HQFp5oPUnPUD8TNIl2CRmJRRhmfEImSXP8pcUyifVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b3ee1c54.mp4?token=mCTbDSmkBnQa_r4D5fDjvtkHb6Wio7HXRJIO8kUQLLk45uNhbdW3z9uXH_TfIV6bpJ0P56ZpazKvdmMfM-kplcjF5haotMs0HLkXd2wujPqaV06w-nJBZFdg_NkFEYMe6bSbQuAMSbKYn1Mth8hQTxKfLoGWt7bvLB5XO_HU_ePmmxpIMTxK8LwbMa6emYJzY9koBGQ5CKgeJiDEeb9u2izdZ0R7ujS6LuRzy5FmaQbLkaBgju_Vhk6uYhhL91DqJQKB-Z6DZw2z0wc_9Djcrvx8yddIxAGqqKueJdj9czEdul1K6xfhOTB5NKgFlAkkEz3s-gihI1c6GA-1YmDmtW660a2JuYz6LbN1bE7yZ57Dpp-62OnPmHKX5REXgbNyhI_-aziV8NqDJ1K-g6Sw6SVRj0SslWth5QKN2ykhqTAfd0WHnJA2N3j26hlaiFXMcz7O1qN5DZMDG1laxqWZoe3gkFD-x0hYIOyehIMtz0oqxwBQouFEBCM76rK4x4RKMgIotDyGyDS-dAoMcuQuu1_qOIgrPGlSJBRB5ChU2Dpgnd_hhyiIorBJbOdw58ehEL5v4FysmUlF3w0lYrPBF_rpSWggU3ssikTrNR-mL7cCnJuFMK_F-R6qKgr8LKnx4HQFp5oPUnPUD8TNIl2CRmJRRhmfEImSXP8pcUyifVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شجاعی عضو هیئت‌رئیسۀ فدراسیون فوتبال: در مورد ماندن قلعه‌نویی در تیم ملی هنوز تصمیم ‌قطعی گرفته نشده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/452559" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452558">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a48e534a.mp4?token=r2XneW808vxCqBShvP72FkamF0MmAkPBkS1_X6nwsLQj7wfKNsff4uH9IfJwqhebPGezor24XT4KUGYVu6zaa61cw9uwLSYhgtxC5PaM-IY6e-sgcKs3disqle_8Qxl5Z3VHa4YOkbLlrE-3ImWb-ohOQ11Ly15n7vGhS7Gj-ICpDhf90G7LKI35rbvJ_5qVLItuznCO-zG5s138apJOUpAOynCuhYjkxhulZtq2Loc4fqen25CjpG_2nhbzwT6kLcjyzPYpo_-hXRDB_QqYVJhzFDhwhFJzLahy6dNc0qkzHVkT8ex7bdOTRFxZy1GiTvx28U9UacRMaOjuj_oDbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a48e534a.mp4?token=r2XneW808vxCqBShvP72FkamF0MmAkPBkS1_X6nwsLQj7wfKNsff4uH9IfJwqhebPGezor24XT4KUGYVu6zaa61cw9uwLSYhgtxC5PaM-IY6e-sgcKs3disqle_8Qxl5Z3VHa4YOkbLlrE-3ImWb-ohOQ11Ly15n7vGhS7Gj-ICpDhf90G7LKI35rbvJ_5qVLItuznCO-zG5s138apJOUpAOynCuhYjkxhulZtq2Loc4fqen25CjpG_2nhbzwT6kLcjyzPYpo_-hXRDB_QqYVJhzFDhwhFJzLahy6dNc0qkzHVkT8ex7bdOTRFxZy1GiTvx28U9UacRMaOjuj_oDbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
افتتاح زیرگذر میدان سپاه تهران  عکس: ‌محمدمهدی دهقانی @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/452558" target="_blank">📅 23:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452557">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7B_SGRDcTQWCr6F1RKPm3vca6S9c_NvQil1cLboEuPWPI6_8KCjDdEU8cmockrLD107nfLYpGc5mu0_bRvR71Wy8Es3RfOMkPCQiWc4pZ9zkF5JaovjIuPEaWXyfuFghQ6epJ8VdUtlqcLPJPrhiAXOH16gJp6IJZr1Nk6GpM33ySW5gTFQeM5mGApJOvJy9SdMWe0atasGR41PgdLdU2wX6zma-cfkDMRVh7o7m6NroxzbjN_wib2LgY3nOpaluslBz2YKPeSF1ubZP-VKVwkVxjA7Uvr0QQu-nL4q7lr6Xz1w1DCXvCbbAZ58yTyELS__qONpoepXTREZRnExEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: انگلیس درصورت همراهی با آمریکا هدف مشروع ما خواهد بود  @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/452557" target="_blank">📅 23:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452556">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5TYDLaPB3oas45xq9fI9oQ5YJJo6ofspew-TNAMIfgWxHl8cobsoh2wyEBxggaVBbpPcy967wYSXKqmFGoz8O0XPyfkkCHlfzye9tYKE7s2szPusRKi38KEp8_cjpAxwWvtHr8fhRxueOp8TrZU8EcqF7fi72INIlfNcom63sKcbasqtH8RgdCqewePEQ7Q9dO5TNuj1e1gwGge2HfBkeF1jxDvsi-OwmcAOZ6loTn8Q2-Om8VSDfkrLvbwZBjE0CoAbD_KoEJ9YQDQ4zONLwL6AwlAECaOlkZMVmcAnSuYBF96hlq97Jh3GDfYM9IMvJ9dWOoSa02W4oByM-qjTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: به کشتی‌های انتقال تسلیحات از ایران به روسیه حمله کردیم
🔹
رئیس‌جمهور اوکراین در گزارش عملیات‌های جدید علیه روسیه مدعی شد: در حملات دوربرد به دریای کاسپین، کشتی‌هایی که در حمل‌ونقل محموله‌های نظامی از ایران استفاده می‌شدند و یک کشتی جنگی، هدف قرار گرفت.…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/452556" target="_blank">📅 23:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452555">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6eYqd4ok4iT0zkPd5LOWEUIVWiTO8i7l3muEDlHnkXxb2iSREOpKv7diZqwf20EDTYZlUOMeVkxBgTI1eD-pwDo_CLLWOcey0i4Snh6PjC7iUO6_TuNRtC8-2zYuT5PGKIpxZpQljsm1LWpXl0k2CPb0MiMBP65SI9cqsWYdGwCirEtyqiLsrgFgKspcv9IVvpoSdu0wQlc-OD5Mb7AU5_ol4r1cugZM9kSLC5rSDL61bdczm8-aqg0epAPxc6aXSsGpoq8gyPOfzfIZKug5Svsvxwq2jFdOSxKm3ZpWu9etfiQfAkRYdvC8xWUivuRSfnsE9BYn3VyFAISzkaXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ۱۱ جنگنده و بالگرد آمریکایی را روی زمین منهدم کردیم
🔹
سردار محبی: از ۱۷ تا ۳۱ تیر نیروهای مسلح ایران ۱۱ جنگنده و بالگرد آمریکایی را روی زمین و درحالی‌که در پایگاه‌های آمریکایی در منطقه مستقر بودند منهدم کردند.
🔹
همچنین ۱۷ پهپاد شناسایی و عملیاتی،…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/452555" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452554">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A--UZuXl9mJKWb7xyPFOwsKSm7EBaactFj3Rs-YIbSKzprPR2f3soad7gsKx2M1Hz4kuZrgiVAxuh1qrqHkr5XAhZKTXa6ziypX9CMnesvgmaLa3oKQaU0QvMFjVsYoUiQweqPm6TaCDXxMFs_RrpZg0roNPf3qgIrGSwp85-4wYF3fObb51eyEEyR1NQhufhd8eu0DGnymO30x5tgC8YD27bmEaLQx_x4JObI9MUFzi4PYeGNqN_Royb3Jv3VC7katMJKme9XByae1DKaKRhYDKJOBcGdP1qJkZHLdbK-ztpyWtNY6YvolkY3_YRjWYHR8CGrxl8i5eCvWA-hxBxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منزل «بن گویر» هدف حمله پهپادی قرار گرفت
🔹
رسانه‌های اسرائیلی گزارش دادند که یک پهپاد در نزدیکی خانه ایتمار بن گویر، وزیر امنیت داخلی رژیم صهیونیستی، اصابت کرده است.
🔹
این حادثه، طبق گزارش رسانه‌های اسرائیلی، نیروهای امنیتی را به حالت آماده‌باش درآورده است.
🔹
شبکه ۱۴ اسرائیل خبر داد، پلیس و سازمان‌های امنیتی ذی‌ربط روند بررسی و تحقیق را آغاز کرده‌اند.
🔹
صهیونیست‌ها تا این لحظه، جزئیاتی درباره ماهیت پهپاد و طرفی که آن را شلیک کرده، منتشر نکرده‌اند.
🔸
این در حالی است که درباره تلفات انسانی یا خسارات مادی در اثر اصابت پهپاد، جزئیات بیشتری منتشره نشده است.
🔸
تحقیقات امنیتی و فنی هم برای بررسی جزئیات این حمله ادامه دارد و مقامات رسمی در مورد نتایج اولیه تحقیقات سکوت کرده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/452554" target="_blank">📅 23:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452553">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سخنگوی ارتش: تقریباً تمام زیرساخت‌های آمریکا در اربیل نابود شده‌‌ است
🔹
امیر اکرمی‌نیا: ما آسیب‌های جدی به پایگاه‌های آمریکا در کشورهای منطقه وارد کرده‌ایم و بخش معظم این پایگاه‌ها از نظر عملیاتی، توان اجرای عملیات به‌طور جدی را ندارند.
🔹
مخصوصاً در اربیل…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452553" target="_blank">📅 23:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452552">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIer1zxKeLCSvnKYFMfz4_h2WBkdTYa1uidXClDRZpkKkj28W1OUeRVOpmd6aCKI6f1lYHg7uhnUZUfE632QUVZ7I7uNjwglYQNSyVD7pq36_upRZ0tmdnsRzaYc-ctb2JcBw7pWJ3361NUKK5pdxUm6tpxL3n_26Xa2cHmwG4Qofi9ab3KSmo-D22uNB4OJXt6ZmII5d3ek_yiyk9qU3Bm7YV1-1XW1oBSfYNitfHrmVOgwayRmHUeA2ZPsUkM-5SupZluYebRn4Yx8xIER62H9WVVEUm39uWOZyUAPjYN8oKjgU5RcYl8p6TsLTX--cISei8RuaO1KjKvkZzONgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: تقریباً تمام زیرساخت‌های آمریکا در اربیل نابود شده‌‌ است
🔹
امیر اکرمی‌نیا: ما آسیب‌های جدی به پایگاه‌های آمریکا در کشورهای منطقه وارد کرده‌ایم و بخش معظم این پایگاه‌ها از نظر عملیاتی، توان اجرای عملیات به‌طور جدی را ندارند.
🔹
مخصوصاً در اربیل عراق تقریباً تمام زیرساخت‌های آمریکا نابود شده و نیروهای ضدانقلاب توان عملیات را ندارند.
🔹
آمریکا از توان، تجهیزات و پایگاه‌های زیادی در سطح منطقه و حتی در جنوب اروپا و مدیترانه برخوردار است و تلاش می‌کنند خسارت‌ها را جایگزین کنند.
🔹
در هر صورت ما این آمادگی را داریم که اگر این جنگ ادامه پیدا کند مثل گذشته عملیات‌های خود را تا زمانی که آمریکایی‌ها متوجه بشوند با تجاوز نمی‌تواند اراده خودشان را به ملت ایران تحمیل کنند ادامه بدهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452552" target="_blank">📅 23:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452551">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4830f3ef.mp4?token=iCyRrqDoj_Hirc_GneyP1SnJ7qO2DYWI6Sd0wk9Pb6RpKp2evyIpSeDuXxyftbQvyrOTWp4SOYl_5isBsdM-MTYPFq1DbxWAFnfT3z6DGVhVR4x2ch4D4h4Mfy8oxTQta9cREv4yhWDaFas_WalvTgDQ3ecaU66xmdQJufo0STTfT2chIz5HJyqKheipTXhC5AqJZkpnNyNTHvhI0lGlcR-fVHnk-zDrKtHy11LnIHiuUAGylR99ClSt5iUKzHSAVTKQCC_GfUi2c-EVapXYTB9-2kMeE-xSHh6wnsgDsGqyrU5Ke0mPDgZvugt70uA4qDKZG28eRBnwNL97EmMJnYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4830f3ef.mp4?token=iCyRrqDoj_Hirc_GneyP1SnJ7qO2DYWI6Sd0wk9Pb6RpKp2evyIpSeDuXxyftbQvyrOTWp4SOYl_5isBsdM-MTYPFq1DbxWAFnfT3z6DGVhVR4x2ch4D4h4Mfy8oxTQta9cREv4yhWDaFas_WalvTgDQ3ecaU66xmdQJufo0STTfT2chIz5HJyqKheipTXhC5AqJZkpnNyNTHvhI0lGlcR-fVHnk-zDrKtHy11LnIHiuUAGylR99ClSt5iUKzHSAVTKQCC_GfUi2c-EVapXYTB9-2kMeE-xSHh6wnsgDsGqyrU5Ke0mPDgZvugt70uA4qDKZG28eRBnwNL97EmMJnYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقتدار و اتحاد، پیام مردم مراغه در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452551" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452550">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2SyQ_ND4H7WLe79unQNYkaqc_UU_Tuhw0Fq4ERTeRtIciU5gnZnaNSHuB-AEu2hkSJKqXxdEGoiQnlOLmUO2jc4qsm1p2zv2_BewlhAc4cYqdkEXHUAhz5S5lq9FSrT3RkSni0mjhRPu5T68eF0F0qjOzON3UTS2L5Jt8eFNclKs-ROfhB9mP24qOyVCylRvnU4TYzez_6Aqcs1fQZL3s3X62wR1ZPbpXEf7ME_laX06ylqwfaYSuOJ4_kevt6ZKZGQw-WX36-6GG-ceRXWVp_Y2JCebbIrEVbZJuUdLCAVJygmeO40-SuXO5z_5zSIVFl5deRfi_IQPt2f40f5zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام ۷ باند و کشف بیش از یک تن موادمخدر در لرستان
🔹
فرمانده انتظامی لرستان: ۷ باند تهیه و توزیع مواد مخدر منهدم و بیش از یک تن و ۱۹۳ کیلوگرم انواع مواد مخدر از آنان کشف شد.
🔹
همچنین ۲۱ نفر از اعضای اصلی به همراه ۵۷ قاچاقچی و ۷۳ خرده‌فروش مواد مخدر دستگیر و ۴۰ دستگاه خودرو سبک، سنگین و موتورسیکلت از سوداگران توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/452550" target="_blank">📅 22:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452549">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
بروجردی‌ها: سلام بر مدافعان ایران، از طرف مردم در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/452549" target="_blank">📅 22:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452548">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56c4b40db1.mp4?token=MT9P1rCmYgSrqJBBqb9Lklm2o7qGhOGJOAuIz2londZiMGe2CPLlkRFyubROcsl-t6z19Or_jrsRX1jEbVPwQ58bV1-WjYWJSqLqJ58yQzxnFJLtQvJ-KIQz4GvP2h6h19llbUrEuLa907DBtNM8rDw-nPWuFZE1K59XvUcGc5CIXFLGQggz9X8TIkbddhvD8fXL_EhVLCC8zbvmXfIGFi2J91Vg7R3qOsH5539pQ8XqbVlxZLwHsc3x4xf5f6O8nOZ2i0fRrDNKZCacohp-lSZclMw8BKqncMMEpE5GZ-Ea7lNV8gUIQDwsVZSAUJTwXYjCqYdua2dY79XafSIvpYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56c4b40db1.mp4?token=MT9P1rCmYgSrqJBBqb9Lklm2o7qGhOGJOAuIz2londZiMGe2CPLlkRFyubROcsl-t6z19Or_jrsRX1jEbVPwQ58bV1-WjYWJSqLqJ58yQzxnFJLtQvJ-KIQz4GvP2h6h19llbUrEuLa907DBtNM8rDw-nPWuFZE1K59XvUcGc5CIXFLGQggz9X8TIkbddhvD8fXL_EhVLCC8zbvmXfIGFi2J91Vg7R3qOsH5539pQ8XqbVlxZLwHsc3x4xf5f6O8nOZ2i0fRrDNKZCacohp-lSZclMw8BKqncMMEpE5GZ-Ea7lNV8gUIQDwsVZSAUJTwXYjCqYdua2dY79XafSIvpYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علی نادری: تا کمترین فشاری به آمریکا وارد می‌شود، جریان داخلی آن‌ها در کشور فعال می‌شوند و مردم را می‌ترسانند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/452548" target="_blank">📅 22:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452547">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/239777d5c8.mp4?token=Hxrp1_EfhQ7NrVNnApWUcG5yRqmtEoTGtVdxIl2E34wG2zQ3SVoirenZnWUDz_iMAuE0iPiYgGANJuZ4MEpxdd1FTVRDcuZPXeqn6DCXv3QuBdCuYSJrfLDtYRzoq2hR782dloIkLVsyREpXkIkv6wetwd3Dxt_7TEr6skHV7Tu9LtUlha0fXsBgrZXaVOqZoPiehGSFYwxY559_XefNqmSRTloEx877i71rDIj-OcLNry_TLYRU0XPqfREwLst8bd1Qvw_tTJOSiJfdJ-KuIzB1KGlGE5qn_QcR1BHjL2gJ9-K2XUmk85iOb5edpqPvgghYdfaLXoymCfBp1-NDfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/239777d5c8.mp4?token=Hxrp1_EfhQ7NrVNnApWUcG5yRqmtEoTGtVdxIl2E34wG2zQ3SVoirenZnWUDz_iMAuE0iPiYgGANJuZ4MEpxdd1FTVRDcuZPXeqn6DCXv3QuBdCuYSJrfLDtYRzoq2hR782dloIkLVsyREpXkIkv6wetwd3Dxt_7TEr6skHV7Tu9LtUlha0fXsBgrZXaVOqZoPiehGSFYwxY559_XefNqmSRTloEx877i71rDIj-OcLNry_TLYRU0XPqfREwLst8bd1Qvw_tTJOSiJfdJ-KuIzB1KGlGE5qn_QcR1BHjL2gJ9-K2XUmk85iOb5edpqPvgghYdfaLXoymCfBp1-NDfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت دختر دهه‌نودی از با حجاب‌شدنش در برنامۀ محفل ستاره‌ها
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452547" target="_blank">📅 22:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452546">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11c8107cff.mp4?token=KDe0SPMU_EdiMYtiGODCe2stUPHEqbGQxoKC4VCtwPsFHqXYTlZq-d2mz4q2pjHs2FaaMD3OoEMIoDvy8hX8RR0gz_n4o9_26RvhL65xliK1Gap_KAXH8uf5QRs5QEPFi_xMJbik4EjfEAJdXarJ0_EU8-bJcsmFv9hn2UY0buTaEF0aRJDofSgl0wKQ_BUVkQrjE4abchpOhH68imo7H-sV4WylVY24RfuB9WNnIafFjwvjTi8q1GKlovXaWArOzIs2Twwjl9Nw0xeqOhQhYRBNNj81-b30ySt-C2l9Z1sKR4rcgjA2yEEdyxOx3ILOgAmD1kQLWLOYDy1-utmXHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11c8107cff.mp4?token=KDe0SPMU_EdiMYtiGODCe2stUPHEqbGQxoKC4VCtwPsFHqXYTlZq-d2mz4q2pjHs2FaaMD3OoEMIoDvy8hX8RR0gz_n4o9_26RvhL65xliK1Gap_KAXH8uf5QRs5QEPFi_xMJbik4EjfEAJdXarJ0_EU8-bJcsmFv9hn2UY0buTaEF0aRJDofSgl0wKQ_BUVkQrjE4abchpOhH68imo7H-sV4WylVY24RfuB9WNnIafFjwvjTi8q1GKlovXaWArOzIs2Twwjl9Nw0xeqOhQhYRBNNj81-b30ySt-C2l9Z1sKR4rcgjA2yEEdyxOx3ILOgAmD1kQLWLOYDy1-utmXHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس: بحث اصلی میان ایران و آمریکا، تنگۀ هرمز است
🔹
هرگز تنگۀ هرمز به شرایط پیش از جنگ باز نخواهد گشت.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/452546" target="_blank">📅 22:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452545">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزیر آموزش‌وپرورش: امسال استخدام گسترده‌ای نخواهیم داشت
🔹
در استان‌هایی مانند تهران، شهرستان‌های تهران، اصفهان، مشهد و شیراز کمبود نیرو وجود دارد اما امسال برخلاف سال گذشته، جذب گستردۀ نیرو انجام نخواهد شد.
🔹
براساس اعلام آموزش‌وپرورش سال گذشته، مقرر شده بود که  ۷۴ هزار نفر در این وزارتخانه جذب شوند که حالا این عدد بسیار کاهش پیدا کرده.
🔹
این در شرایطی است که آموزش‌وپرورش به حدود ۱۲۰ هزار معلم نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452545" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452544">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmE9BVJ5xfUGgS54n7XRyORf_ehpvcmBzr5xlY8WZGbFoE9Vs81QXMM4r81yekl3tBvfYblF7VUQXQYRv8nZLOthnaCoXlFiv2rnCbLSShaJID_cWDpRY3OJ3jeLRqpn1Xok51umCOMBm7BnIDsy0gU8STXeTZwluDMCMDnwmNBVYiYAAR8c2x96pBqTQZJhnz_uznWFIdGcHfU293zMqqXmiRnm9-Ov0eKqd3v6WxtVhfU9XMUaLuZ_6SSMjWNa4effX1GDisansXxejQtA4NE1H417GmPZnInBSHG9gSX9lohqcFDG-lwj47b9SvmCYht8cnpcXrJgY4yS9n8Tpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده نیروی قدس سپاه: رفع محاصرۀ ۱۱ ساله یمن، مطالبه‌ای به حق و انسانی برای مردم مظلوم این کشور است
🔹
سردار قاآنی: رفع محاصره ۱۱ ساله یمن، مطالبه‌ای به حق و انسانی برای مردم مظلوم این کشور است.
🔹
انتظار می‌رود دولت عربستان از تجربه رفتارهای غیرعاقلانه و پرهزینه آمریکا عبرت بگیرد و به محاصره کشوری مسلمان با جمعیتی بیش از ۳۸ میلیون نفر پایان دهد.
🔹
توقع مسلمانان جهان از عربستان، که خود را خادم حرمین شریفین می‌داند، آن است که به جای ادامه جنگ و فشار علیه یک ملت مسلمان و مظلوم، توان و امکانات خود را در مسیر حمایت از مردم فلسطین و مقابله با جنایات رژیم صهیونیستی به کار گیرد.
🔹
تلاش برای نجات غزه مظلوم، مایه افتخار است، نه ادامه محاصره ملت مظلوم یمن.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/452544" target="_blank">📅 22:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452537">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTELAMQZuzXcIhlOfNVr2UyaRAOTsw71Lo1fqbTWA6rkB-MDWB-fhoA22PZtSUYlEFCJeo0kx0LNLbe4bfhJB616OlGBbqVpGJxLVr7UcbLeYRhtr1wfKJUATu6DDymRvJTyz1vppEua_6uDoPWLL9b_HIBFZ5NJCBNNBfIEVjqnpoi2NhUYD-xeNObq0X6Vq0nhdCKoc2mNe9x6fZBIM1vxpWanH6Bi4p33WMkk2e9obWs5TYClGXZZpbJLz-PZzHSdh-NnI1Tr1WXmtsMt4CjTxycnIuQvHwSWnLSoWv2rQLl2d9dHI4k_yGu1tTDA5ZApdKt2aEVHnb4y-BfMNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NC87KZlU0MlR9GZxMUMlbqrPErGrAUXF5LUQNV9fyJFSTYSI5Ezb7CxZdKl1kjPHWZX5vKU8qoc_cvX9fUekuSaZ5TsbUCSY8i_2V6Zn1jDJl20dqpUWKmnF2mpdN3LuHyLF0BXnvGZDra-90bPZvAO_eiInHPGjx6HFWsmoaH9UUrAxtuJqUcemh8C7LHpOC-FnvT36mpop_JRxSmyf7e_P4ZUyI7BLGn9nfScue1wOeuvABy0noOoAmE8snks-eRFtNwiz1idszbQb-tOFj7tY_izSKYXS7YKh6be6tVC1acxf71fSuMbS0noYWpXj6THHDziqyNJKemrmj7evzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJrHrnHxviMl2QV7Wq1Jjr8WdooXeF52dVNjwy0LKno7_uyaLcd8jxFPMJQiOVvkLvqgCNIFcGozFokmJZMMAcH463JmYGhZRvzaJeEMy2tMecDajmsNG1zIsv57pYcZdzVFupZmi2SkzkHRqMo1LYaM9xdSkGbSpwoE97xDKNgLxg-bcqjTE7lScmqJFggvQUw6_CGhwh3anCjFM0nY9ds0YMoNpGUm6-Teu2ETRfayl5x--Y1-6nMr2Z3qwbBBY_xEjEFhw6NXYThaDehbD2j_RSnStmb_WGXW0PUSKNn6fhASBexiEjPIM9LRD9ne7AyUZJB6eJp0NzXG1-jMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRurN8aGdErdqeJ467ViTok2ZFfB906tIjp-D0Ht-MKrcMztjoPmKRbufok0QOxqgfnFQ_loyXt6BfdvvW10yZzbH5snm0YZNG1MZxrEiZx1UmTpyv5-7KfqjbrTtZZnrUTpF4Cs6rzpeTRmPXQp2Qhxm7hW_TAyerZJNm81lcCTJ0geyFiso09QsXpLdYcnNtMKRikP5Y3ioW-iMGd9c1uwm_TEQuKqD8SaR8OrYo1GKIhFSiw158fjTAsLPb9YLDqtMDk5-2x3FmZ0JrwfcpUIoH3j-4oVyigxfvlTHkbIMQHG8gjgGsl4P7c4rQ2XC511WIFTEwnJoRtCyDwFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oz6CE0192BeFIgNZO7R04sBpW-j6GTuNEupbxYmzntADGz59RZNcyInYHjgrkKhrpnCGic2LxIcQu98M8ob0n5QXjU9ElOIVxQDQ6siaPiAkiRd6C7pYT4wcnryZFL6KGHyGW6QVdqeD5v4aiM3NBd8GeqnbSS09ifcWeBtYYwTCZFG5ExWvXgIEDf1M7fXNdn_Iy2BVyfK4Uy2OIYSb1ZfDUCfH1dEKlmUXXqGor0rTEyO52zONYaCs3XqHHWIxjEmyjN74Mp9rIRIFp4y1t5JDYIBPgxMsnoh62qW6M4lcvBhLfSHy9ZN3hmfjakDuZCAlxkTPv_URpxJEpTvXDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7jV2y6FTkk0RM3Z1Zdzn3nz4NpWrywMFRZPBd-2gGBGI2kY8a4ul5_9jcJm5IuHJC5tLVDWoIXSwd1guN_gCmgz5M9qiJt9hZ5pDdfj45E_xQmIVkzIq47JhnreVvnbWkSO_tYieZmwJKHuIgp66FLQ8k_XNrGzCjHShz-XKz5gYLJ8PZBNjUKXZ54laigGowG-Q1m5X1zQ3UTMDlB3KG_AgT26Eydf2DF6CJc8efmcbVn6iZ6pBxZ9LB47lD5W7AJ1iZEM1_py3XOq6rn4qXvNuvDLa1FNIv01mqBVoXYU1EdCPynpQePsWbYG6DE1oN8nHIB_2I6Ucw_ifyDR3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwmh7KLnYnoX8zh1GHxXoCU0_lxFoHd9nDRs4F1XX3SKSqH4hR8tcUNEA-4DZuI2iBnjAGirVsYD_I-_ITcIjIXuA0Ds1JFYaMupZtj8uPOlTfBaWmVDPsjn9EoXOrVhbHGE18we4kr0IKqP8R_jf8UShN4WzqIzBfnH-3JDPQaxsHcxg0SgdiU0OPhyMxp3BbuFHPBpfPvap3H1J_ecjsjhlnfRV22FcUc0jfzw9bYnXC209KVPMWedafTnNVvu5fXvCnbytt3c4kpjKtkodFySjstDZWmGAGnntZI7zcdnEebnEpnvgBG21iSbsuMz7cPrKml2KcUb2GE-WP-yfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آئین گرامیداشت شیخ‌صفی‌الدین اردبیلی
عکس:
سیدمهدی پناهی
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452537" target="_blank">📅 22:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452536">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX6rXLkueG_bc-ftSQuCGvDwNIRIUoo4Um55SYsjrlaU7WgIKVIemTEdwXuRsJx4ynACRudqoOlP7_h6p9BohaVuos45QfC_nxxnsL6flS06icm2F7yfO_wOr-5hZvkP_6aqH89Hi-k8Kbf3GCkPwA2Z7_Y5DFG00UtSMdOqrVJGhmrgD7JsOYqSQkBvrm0BQSgXoPsiRVSPXo-Sduzb_M76qM1UQPxjw8qHa5TF7taTOHNrTv8-lJ5WvtY5F6ltyCPH6x2AZO4WbCuVFEK1J5qvdPUBGVBwrm6SdP_mVkI9Eo7YKUbIfY6LWXlLC2_G-j2YHZtxRDep3SA3qlsLGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر به ۱۰۰٪ خواسته‌هایمان نرسیم، به جنگ بازمی‌گردیم
🔹
درحالی‌که آمریکا نتوانسته در طول تجاوز نظامی علیه ایران به اهدافش برسد، ترامپ گفت که «اگر ۱۰۰٪ از چیزی که می‌خواهیم را به‌ دست نیاوریم» درگیری همه‌جانبه را از سر می‌گیریم.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452536" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452535">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e865cae1a1.mp4?token=CXoeZqoZcS-vbV7jB_b07uNBw76_BPDGZy4I01uy5pkZpU2_uN8OqQauUTBWcKU4zfsBFZJz673yc43zGmfWAWwNHvIUD9Qhp5oU_SJ82UlVUI8yYFatoPMk_TUjgpGgcl-8PahFaSyI6f8QHfkbsu5vVmtFzX9N6wLQena0turEgr0UapyD5n2gzW1YrnaHFKeu_wUrRxjh8SQzxm-1xmFTgmWdpQdIInepTsJOmFUImascNULKgebtFK9F5q2bOuNTSRhVLmR-cYzhaeY_r7lnBmXBIX2fSFQihpfrYxknLNxp3IgZykHnGmPc9-TjTkjcaB1zu6nT9wqElF0VBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e865cae1a1.mp4?token=CXoeZqoZcS-vbV7jB_b07uNBw76_BPDGZy4I01uy5pkZpU2_uN8OqQauUTBWcKU4zfsBFZJz673yc43zGmfWAWwNHvIUD9Qhp5oU_SJ82UlVUI8yYFatoPMk_TUjgpGgcl-8PahFaSyI6f8QHfkbsu5vVmtFzX9N6wLQena0turEgr0UapyD5n2gzW1YrnaHFKeu_wUrRxjh8SQzxm-1xmFTgmWdpQdIInepTsJOmFUImascNULKgebtFK9F5q2bOuNTSRhVLmR-cYzhaeY_r7lnBmXBIX2fSFQihpfrYxknLNxp3IgZykHnGmPc9-TjTkjcaB1zu6nT9wqElF0VBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۴۷ شب غیرت، وحدت و ایستادگی
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/452535" target="_blank">📅 21:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452532">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۰۲.pdf</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/farsna/452532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۰۱.pdf</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/452532" target="_blank">📅 21:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452531">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34a3524522.mp4?token=cmNF20Hc4DN5jBUc0Op6fMIYENh3SC5TMZU56bIT_lzxVpXykLj5m5qbKsXbovYNEDpWv1HRtc48e2bY3i9soGyJ3e3cNDoY8q5prvOehwtaEQIbw869sFPoSqvITVGeLV2Vv4USAqd9ndX5uUcOfBtn5_NtRVFSqROgkF-gdVSqqRwuvykQYmNdUt-hqj0N3IzeVZsNqrvxYT2Nn8eJOINWq1fVy0FqSEju9JZSWHeiptiKmh0ghX00kjlXYxAtxUIDMVBB7GUGrPO5JjNhOUj7NF97swxBBaJYoFET5JMA9GICWH5Z-gox14SKl9G5hB04TPA_SQF3TG0_eVmrcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34a3524522.mp4?token=cmNF20Hc4DN5jBUc0Op6fMIYENh3SC5TMZU56bIT_lzxVpXykLj5m5qbKsXbovYNEDpWv1HRtc48e2bY3i9soGyJ3e3cNDoY8q5prvOehwtaEQIbw869sFPoSqvITVGeLV2Vv4USAqd9ndX5uUcOfBtn5_NtRVFSqROgkF-gdVSqqRwuvykQYmNdUt-hqj0N3IzeVZsNqrvxYT2Nn8eJOINWq1fVy0FqSEju9JZSWHeiptiKmh0ghX00kjlXYxAtxUIDMVBB7GUGrPO5JjNhOUj7NF97swxBBaJYoFET5JMA9GICWH5Z-gox14SKl9G5hB04TPA_SQF3TG0_eVmrcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرز مهران در تب‌وتاب اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452531" target="_blank">📅 21:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452530">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0a4262117.mp4?token=uf8bweyhOSqaEVLLtU0FCaPjOzhu4XD5SN8CGfqvlCcdLA-BLt0q7LC_BjxIO0zmdCIxiHjCKjYhD4C-FWnNFB6mXtR1AgDZVeq8F33WcecNxFrC3fbuOnS5F8gAb-xtZb022jWMNWrCcFylUZtMANgexKrTT56R0eZCF5JnZmpaMJ8bmrbV2ub2kCAPEC7GPP5hhFZSLL03-zM1awpi6cS2aRasjOvOn8SRscN0fZ3GSa4IwCuxNIQ3NlATx9TQ5sF6gaHNx-GjXJWzXM0m74Rbc6B4XwauJyArlE22D7UO0l4cCCreeUr4OJfgf92HV5U8-Yp4WMT93oS5ad1NNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0a4262117.mp4?token=uf8bweyhOSqaEVLLtU0FCaPjOzhu4XD5SN8CGfqvlCcdLA-BLt0q7LC_BjxIO0zmdCIxiHjCKjYhD4C-FWnNFB6mXtR1AgDZVeq8F33WcecNxFrC3fbuOnS5F8gAb-xtZb022jWMNWrCcFylUZtMANgexKrTT56R0eZCF5JnZmpaMJ8bmrbV2ub2kCAPEC7GPP5hhFZSLL03-zM1awpi6cS2aRasjOvOn8SRscN0fZ3GSa4IwCuxNIQ3NlATx9TQ5sF6gaHNx-GjXJWzXM0m74Rbc6B4XwauJyArlE22D7UO0l4cCCreeUr4OJfgf92HV5U8-Yp4WMT93oS5ad1NNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس کمیتهٔ حمایت از جمعیت: کاهش سهم بیمه‌ها در حمایت از زوج‌های نابارور، غیرقانونی است
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452530" target="_blank">📅 21:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452525">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fe5KgG_4sWtwreRYY4IurkN4_TDDcavhg5j-P0WlUzRj37BKvyOSJwWTqcd0PToiTa6ObZr9HuSlCRCWAgRRNzjYkBQwlElXdis0d388_G_DkZs0qmKIZQMQa3APsEdOy_AYu9jcOuaK0qFOrzOzlPMkK6WJ9Jo87-fN9q-Gw_uT34s9GxiY5eIkN0JOGlLvtuoTAJ1UfAM-oDvw5vGgKFTRO2Tka3Ylp3BSeXDgSXAvZ0QsC9AbgkRUKWUR6ibq-sy51FpjkYJviaayUOXWcZrZVlDwRCvAUVVRzVFS0FYfodoLY09M8eY4Fxa2MFnb9mA2DpRwNlD_tpnyrnZa7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ulk9J2EmUYRQ6nWq1tIl5SWAh57TvscNIakUyEqeoroQd24Ef_0L5C1iJY0Zk-jdpxHyQT8zfuIzEZytz7BEpcGAMLJ22S_R52_pArmcbJ1sYd2JRQJLE5RD9KJvw6cmiYXtEaKG00FLgM3ceP-SMGJxnupThnKuwCGvorne2m2KkEL-nlFP-P34LUyGxg18O1Iyzm-CMPNsodrSczY-pJnpXRXSNoMQujBH6KSF9Na2B7Dpl9HpHV2P-3otnr1DRUClHVpuB0zPfRMP3dlYsAb21-LxraaHSI1fscnL_evm84eUdyd0oLivkKmSfR0z71dBvUYtE2NDzvJppAGAaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmLUAQVXNhYQWVAXe1Oeh2xGislqkbzBM4Xwzw96BOmONJ24SX4kS8r4vyQNovkJHiTZE33b3tHPKKhpgWG4d1P6peJPYrLFDLqAqKuLEEtqB64ocPFdcexpPKDqXCxAZSRvioBch2G_OrTkIJq-Xre0i-mUbvS6fI3-7GvRx5VdjUjbA7GrVrbELKjEJOoNPUzpJ7g2qj8CITZUZ4rPTDBL2Rr9Ul8IjyFE3Vy5S2c5DQ0QrrJBfq48a8Bjt-uzmh0a8Gz883d0vt2jZhG7DYi6feUNQS0pIPeBCZaM7A7keUqC_Uo2HePgrBk19Ugn1ydlOpnjnQRSMNI-aZuoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3WHpda7Pju9tFIbl35KTaO6EKw6VOXMIQdLE_Xnff9vx8J4Pa9f57VpwLe2pVFyx3JaC0AwXXZR-mxcZ4sN3-3baPy1BGB8NtsVqxVkr11qndPBBpYaRM2lZsPBM_3zjqbnnR-f2rB1dwmfwpiHIXvyeiaYdYEcR3tjvmYfReiUUa2lQhfWPnlmlz-e6c1IuWZvSOkizAx1pr6YC-roPSfrC_DnQA3ohVnRxf2XbWFeb1DqfvRyq89ksQ8e_wR7rbbPfNxoONs3HmSoY-9pD3pcaoGuG-jCUIPzMmad-CCgJiHhzB2L-McqE0fksIDne4r2gjj1uf25JbOAGAN86g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9QCQMSirY2kEZhG_c0Y9of_SUuHlyTfCq7MeDZzxh-b81WtQYHoJcojpqhETc-KUkT-fWtFP_KAA7l4lBJrimy1ibmPJ2QQZQE8TGC7clNkkc0P4YiLB6VY6ZrP3ktrRY790ksbbB6almCPdyb_TWVK8UuHe7I9iKT9YTZ-vr7o4-243yWrJtQhBoKadiNQ1IIERhLVcJ9BKF8g5F8C1VUIEZ9Zr3t6-p0IJPUNualBOgOASvAPog-1UcJVSHZQRmDDKOxPTk_mOmNebH13wJqKuiACBMOsV2ujnIWBiDnPSCufkMGOArbi_yXBNwGmVIX7tgfAAqrayZP7tq0qEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
زیرگذر میدان سپاه تهران افتتاح شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452525" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452524">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee16b1c0cf.mp4?token=F7Dm73pqMvScdjMzFw_JpL7l1XNa6F3xL1xlejnbEgq2DKzAEZvO3aET03IkvdCL7FC5_dVRZtSWti6cSlvadq30DvTNIffckqrE4ptJnhd86vf_a9RAN4Tmzs8LzolTqkiYHb6WMDYeJSmnbKQKi4avsImFOnjUzgufdMd1i45uWP9gjlISzPhCJGXbbaTGfU92m0ZoARVy8pJR0Ypl-xyVxincjTh6Gv4GYxHtIoONekoSkLMD6sTIirD0fAvjX_DwDoG7RotxY5SC5EQL7vhr7hM6Y47S0adHSIIBOlG4qirJAJcg37Wk9npfnVzqYbdh4R8CTqMDSc4ICLfDvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee16b1c0cf.mp4?token=F7Dm73pqMvScdjMzFw_JpL7l1XNa6F3xL1xlejnbEgq2DKzAEZvO3aET03IkvdCL7FC5_dVRZtSWti6cSlvadq30DvTNIffckqrE4ptJnhd86vf_a9RAN4Tmzs8LzolTqkiYHb6WMDYeJSmnbKQKi4avsImFOnjUzgufdMd1i45uWP9gjlISzPhCJGXbbaTGfU92m0ZoARVy8pJR0Ypl-xyVxincjTh6Gv4GYxHtIoONekoSkLMD6sTIirD0fAvjX_DwDoG7RotxY5SC5EQL7vhr7hM6Y47S0adHSIIBOlG4qirJAJcg37Wk9npfnVzqYbdh4R8CTqMDSc4ICLfDvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هرمز؛ جایی که ایران کوتاه نمی‌آید
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452524" target="_blank">📅 21:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452523">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6875bdfe96.mp4?token=eC_1SKUhEEdo33Hi_2gTctRz3zriZgQXK_B5VrL1767ZhF4zLDKLXhIl945-K6jkON4ime2h6GxTi1YJ8rS9JKLWrUlxLlRiNuPqhVGc3LUK6OR1Cm61fWOr0_9m1H05Y10wEgOiHnpNvh1ptembuPdP-11GmlVgQjsKR5-dSfiFiZjOVaIOld1oRYfXGnRVOJHu37g-06eFKJwokOGpL6-a1HV2Gw7EEqGvvQgThFK6FxJTkJ06cKuZ5Lf_dziO75aEfCfmxPDfjs9FT3A-fGP4ybFiZPsh7cA93rZkdCDoPERECOyIGsC0edg2LUH1wwUaCFZHEpXTe5nfBbr9Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6875bdfe96.mp4?token=eC_1SKUhEEdo33Hi_2gTctRz3zriZgQXK_B5VrL1767ZhF4zLDKLXhIl945-K6jkON4ime2h6GxTi1YJ8rS9JKLWrUlxLlRiNuPqhVGc3LUK6OR1Cm61fWOr0_9m1H05Y10wEgOiHnpNvh1ptembuPdP-11GmlVgQjsKR5-dSfiFiZjOVaIOld1oRYfXGnRVOJHu37g-06eFKJwokOGpL6-a1HV2Gw7EEqGvvQgThFK6FxJTkJ06cKuZ5Lf_dziO75aEfCfmxPDfjs9FT3A-fGP4ybFiZPsh7cA93rZkdCDoPERECOyIGsC0edg2LUH1wwUaCFZHEpXTe5nfBbr9Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قفسه‌های خالی دارو دوباره پر شد
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/452523" target="_blank">📅 21:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452522">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b55d37f81e.mp4?token=oxmMUFoAzh6b0vNU2WhMckD3-dBdbE1R_bM16BAgUlh8CGxSzypEKAgltmzvAXvRRf06PfPviTlsx8qp27WdmfGRCECeGw7A_yiNBZ4P_5i2Myxk2T2CuBWs0UFHL0Ppopz593MV5R2DU2DIrtXMUn-VnHAkzuAt0DpI78NDMp9IRAVIgRjkng5bVlo_wb3c9q8uoLz4mkJM3MZYN5Mtd2dHifMJGdLPcThrxDsM_sOuiL0Qj9QBSAjpmYja34VuoZdKWypCoOidyM-2RIHhLyMVBBo72lcQGdL8lAsKaGua17F6nG4CrlbLzxlWsOtqrG6pErIdAqtY7j9nr34y4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b55d37f81e.mp4?token=oxmMUFoAzh6b0vNU2WhMckD3-dBdbE1R_bM16BAgUlh8CGxSzypEKAgltmzvAXvRRf06PfPviTlsx8qp27WdmfGRCECeGw7A_yiNBZ4P_5i2Myxk2T2CuBWs0UFHL0Ppopz593MV5R2DU2DIrtXMUn-VnHAkzuAt0DpI78NDMp9IRAVIgRjkng5bVlo_wb3c9q8uoLz4mkJM3MZYN5Mtd2dHifMJGdLPcThrxDsM_sOuiL0Qj9QBSAjpmYja34VuoZdKWypCoOidyM-2RIHhLyMVBBo72lcQGdL8lAsKaGua17F6nG4CrlbLzxlWsOtqrG6pErIdAqtY7j9nr34y4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شجاعی عضو هیئت‌رئیسۀ فدراسیون فوتبال: در مورد ماندن قلعه‌نویی در تیم ملی هنوز تصمیم ‌قطعی گرفته نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/452522" target="_blank">📅 21:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452521">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af05d11ca.mp4?token=vjLilhEE0QE-7TB57xquSnOUlo5-nfPNFYoLimsnf83gTvr5GBmbbFq_O3_oWVTYqj4Z4n6k9IntNAA3h4wNKGEA1cx43xT0CGLJ3NJRJZEy8lxLXzXYH-7faRbiTsBmqQAc-nsun2BTQnIeGo_pUk5vpdrH7R7GtbeiRsFCu0MkjhcDszuymf-3evirvjbtalDiN-KVLrsL1Mb_5zWonSALPSx4AgnYkMpyzBk6le9lW7JXKmhhmfYAhyntmqcEqt_pQHkEKDrIIkHx3Zq2WuXWDWlVz6T33uYvAOEraP44WemrXNL3by1U7jP1AN8cCsXEU2fy54yEPwe48a6KwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af05d11ca.mp4?token=vjLilhEE0QE-7TB57xquSnOUlo5-nfPNFYoLimsnf83gTvr5GBmbbFq_O3_oWVTYqj4Z4n6k9IntNAA3h4wNKGEA1cx43xT0CGLJ3NJRJZEy8lxLXzXYH-7faRbiTsBmqQAc-nsun2BTQnIeGo_pUk5vpdrH7R7GtbeiRsFCu0MkjhcDszuymf-3evirvjbtalDiN-KVLrsL1Mb_5zWonSALPSx4AgnYkMpyzBk6le9lW7JXKmhhmfYAhyntmqcEqt_pQHkEKDrIIkHx3Zq2WuXWDWlVz6T33uYvAOEraP44WemrXNL3by1U7jP1AN8cCsXEU2fy54yEPwe48a6KwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری عوامل رسانه‌های معاند در جریان جنگ تحمیلی سوم
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452521" target="_blank">📅 21:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452520">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4048be1e.mp4?token=ZGhvz4wizsq-RWzlGMJeEC5qeJ7bT3SjEDgV07bWTS2jTpV11pSCtPEWSo1cqkFqUp31hTbUCPxrIBlKW8-MkZwTMrgpwT9a0-aZaextmnRZMKmbYp0Fb4_-Aii77RZVJQPw7C6LLUoj13Jjhh49bAsCNEiaqkw4uaMhR5kXs4RR76_YIUpdBRLy9PNu2AMNuYXrQHu5OmaNYfWqf-FRkPfGGyHgW1-UvcFlaoghEFm2bQYrcuwNpqFUmfjw0rLhuPpTPF0iohR3HaMOhL56TYhNo-_NXKmEHlVE4NnAdRDqdQF9qjIQkTGhMK0aeeQNMbki7YR_CGqFYdgOncHbkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4048be1e.mp4?token=ZGhvz4wizsq-RWzlGMJeEC5qeJ7bT3SjEDgV07bWTS2jTpV11pSCtPEWSo1cqkFqUp31hTbUCPxrIBlKW8-MkZwTMrgpwT9a0-aZaextmnRZMKmbYp0Fb4_-Aii77RZVJQPw7C6LLUoj13Jjhh49bAsCNEiaqkw4uaMhR5kXs4RR76_YIUpdBRLy9PNu2AMNuYXrQHu5OmaNYfWqf-FRkPfGGyHgW1-UvcFlaoghEFm2bQYrcuwNpqFUmfjw0rLhuPpTPF0iohR3HaMOhL56TYhNo-_NXKmEHlVE4NnAdRDqdQF9qjIQkTGhMK0aeeQNMbki7YR_CGqFYdgOncHbkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهبرد یمن در برابر عربستان: محاصره در برابر محاصره
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/452520" target="_blank">📅 21:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452519">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس نوجوان‌</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da11d63e0a.mp4?token=SkhyxOe2QKPEClF7abU-CUf5qmTRaOqh9uy_GhGxfiY7dZ4SPCT2lFlmKE8IsyFU6opJE2vMO7c9q6mAAYwv9f6vY7u9h9BwL2l0xAOFHCXV1S841c6AHEdB8QXFms8mYKTCXX-Sn-91Wh9hpaY9WdRuhA-cKf2a-BqT5-Iz_64-KBxcWDlw8fZlltVadQaxvJfaSOZNJTho2p4sp98TY79Tocm3hoe8Q5xap35RVE0wqN65i2AlVSRow5Ce3fNLyV04OlGUheZPVEEgD3yIh-nC6V3BJAu8bKUE9m1NrRm-Qb2h9iZ5FSqs8tAhnpkt6MaBcL69BO_LGfZiUR2ThQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da11d63e0a.mp4?token=SkhyxOe2QKPEClF7abU-CUf5qmTRaOqh9uy_GhGxfiY7dZ4SPCT2lFlmKE8IsyFU6opJE2vMO7c9q6mAAYwv9f6vY7u9h9BwL2l0xAOFHCXV1S841c6AHEdB8QXFms8mYKTCXX-Sn-91Wh9hpaY9WdRuhA-cKf2a-BqT5-Iz_64-KBxcWDlw8fZlltVadQaxvJfaSOZNJTho2p4sp98TY79Tocm3hoe8Q5xap35RVE0wqN65i2AlVSRow5Ce3fNLyV04OlGUheZPVEEgD3yIh-nC6V3BJAu8bKUE9m1NrRm-Qb2h9iZ5FSqs8tAhnpkt6MaBcL69BO_LGfZiUR2ThQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«سفر اربعین» یا «حضور در تجمعات شبانه»؟
🔹
اگر این روزها از خودتان می‌پرسید «به پیاده‌روی اربعین بروم یا در تجمعات و میدان‌ها بمانم؟» این ویدیو را ببینید.
@Fars_Nojavan
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452519" target="_blank">📅 21:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452518">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سخنگوی سپاه: ۱۱ جنگنده و بالگرد آمریکایی را روی زمین منهدم کردیم
🔹
سردار محبی: از ۱۷ تا ۳۱ تیر نیروهای مسلح ایران ۱۱ جنگنده و بالگرد آمریکایی را روی زمین و درحالی‌که در پایگاه‌های آمریکایی در منطقه مستقر بودند منهدم کردند.
🔹
همچنین ۱۷ پهپاد شناسایی و عملیاتی،…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452518" target="_blank">📅 21:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452517">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a41eec522.mp4?token=khMk2V9Kl3sfHcig4IjBgI3ALQxLYZoOj5zgkJ6wgdGBVo_sWTTg0t6VvUsMjeeSm54ivRCmnl7RdW0ObtM0GiUBtVzccw1CUKlODJNZYvdniTnsdgIKUXfJbjqmTciAF3E1QY4aYJUoGr6myj-V7Vi6xGPVjCAlapZI88zcJEF7X62SoGKFuaib2ukz2nk7TW46hJFXNh0YtoPwQm_M0yymOlAt-Lmv6GVHB38fRazEuYGbjHxrEu23L_C8SdBYZbMze77Ahlz9qhzN_8A9A_stIir53FQTmwp0W9RO5Fs7xk9pfAUjodQ2NSuXQBKpQ7ukndfmRwKMzeVl6OJRsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a41eec522.mp4?token=khMk2V9Kl3sfHcig4IjBgI3ALQxLYZoOj5zgkJ6wgdGBVo_sWTTg0t6VvUsMjeeSm54ivRCmnl7RdW0ObtM0GiUBtVzccw1CUKlODJNZYvdniTnsdgIKUXfJbjqmTciAF3E1QY4aYJUoGr6myj-V7Vi6xGPVjCAlapZI88zcJEF7X62SoGKFuaib2ukz2nk7TW46hJFXNh0YtoPwQm_M0yymOlAt-Lmv6GVHB38fRazEuYGbjHxrEu23L_C8SdBYZbMze77Ahlz9qhzN_8A9A_stIir53FQTmwp0W9RO5Fs7xk9pfAUjodQ2NSuXQBKpQ7ukndfmRwKMzeVl6OJRsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگهٔ هرمز؛ ارث پدری همهٔ ایرانی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/452517" target="_blank">📅 20:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452516">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f21a08d6.mp4?token=e-u7kSSPWU-OhFp2D5tsyKmwAChCU32O_kr7AIyz5IWMIiQF35u9jqwSL5fxl4YCsj5XRSEx5D3LsIJet2U-2CIisqoQOtwyCZm0T2rZsPdJZvuUkDbfm8zkg4Q-6Yvxe-RF-ba_3C9fv4Wvhc7zGUtDlgBt7_gytc9jRGRy3Pf8wp1dCMzXauxo5b2QWWlGXQA_tV_9Ue3RwalPBn8V97MUe2XIn7j5uOCAihphSJb4mjNHkvxRzm0q3bOxHd_kG-TN2nEVOEgJnuADUgc13S6SrkH1q-DSa2jkFYQTjI7y_PGwTnj2PDKZb9Sa05tVX7YVCXOcOCDP60covTUSDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f21a08d6.mp4?token=e-u7kSSPWU-OhFp2D5tsyKmwAChCU32O_kr7AIyz5IWMIiQF35u9jqwSL5fxl4YCsj5XRSEx5D3LsIJet2U-2CIisqoQOtwyCZm0T2rZsPdJZvuUkDbfm8zkg4Q-6Yvxe-RF-ba_3C9fv4Wvhc7zGUtDlgBt7_gytc9jRGRy3Pf8wp1dCMzXauxo5b2QWWlGXQA_tV_9Ue3RwalPBn8V97MUe2XIn7j5uOCAihphSJb4mjNHkvxRzm0q3bOxHd_kG-TN2nEVOEgJnuADUgc13S6SrkH1q-DSa2jkFYQTjI7y_PGwTnj2PDKZb9Sa05tVX7YVCXOcOCDP60covTUSDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشت آهنین ایران بر سر نظامیان آمریکایی فرود آمد
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452516" target="_blank">📅 20:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452515">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54cb2bbb46.mp4?token=rGQs4MWSdBC1-5miRnkv2-1C8T0I9WR27r8uR8oMYyMw9jf4E7ZdYJxn651IbBrjvIcTbRsE1pj0CgWXZtzQctFaql4tT1Oagte-Dsq9u28Ho0SkuP0AqHdfZIh8nzqB5vCzvw19PTjMBKYuutdhMPGHP0muw5Mn8dRKaKPXdS8tRw-hhAbYzuyc3F6tOqXBHy2Yn2iJl4i5-lcfCi0cYGoxFMp8w4WI6frWRM9orWZU6lbb_R86EPtDCs4I3sIERNvEek7QjGoHRe4IROSztVTi4fwLf9bPM8v98uyrkMbSa5gGEa0-bqs1En6Xidf4T6xXeDh4uInAJ9aAlDoN2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54cb2bbb46.mp4?token=rGQs4MWSdBC1-5miRnkv2-1C8T0I9WR27r8uR8oMYyMw9jf4E7ZdYJxn651IbBrjvIcTbRsE1pj0CgWXZtzQctFaql4tT1Oagte-Dsq9u28Ho0SkuP0AqHdfZIh8nzqB5vCzvw19PTjMBKYuutdhMPGHP0muw5Mn8dRKaKPXdS8tRw-hhAbYzuyc3F6tOqXBHy2Yn2iJl4i5-lcfCi0cYGoxFMp8w4WI6frWRM9orWZU6lbb_R86EPtDCs4I3sIERNvEek7QjGoHRe4IROSztVTi4fwLf9bPM8v98uyrkMbSa5gGEa0-bqs1En6Xidf4T6xXeDh4uInAJ9aAlDoN2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن‌سوی مرز مهران؛ زرباطیه آمادهٔ میزبانی زائران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/452515" target="_blank">📅 20:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452514">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtHanMgtMNlAsZpDmXsvMvYyujnIbuWeK6YpM3wOAEIoJ9bLAFZ8DAYaN4sd6YZR-Q5C7L-iTfoDPwf6sS_0Jw0KAmvANugkKGZt7uXXhcUQl2BSVF9oaOx8hufr3FQyqV3ntjlN1SG4Eqd5zKtY435wmtC8Rv3Nbfzz1t9nio33TXpKGPDm-7EID-02_Oj7yesalqd2f6J3V6e9mGGDBLZzTaJyWCehJQG3cJM0bXupA7Nx6-iPM1zBfWcNqwZ10vCqNqp_DImrmIkF-fvs0KON_1QBKg7gwmvzQhTYAmDOOvU05Ita6hvAmKyABl-reLSm6WTyrfKEVHAS5rjiQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زارع به پرسپولیس پیوست
🔹
محمدمهدی زارع، مدافع میانی ۲۳ سالهٔ احمدگروژنی روسیه، با عقد قراردادی ۴ ساله به پرسپولیس پیوست. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452514" target="_blank">📅 20:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452513">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUouXMD723Bu81du5Z_6fpWZlEZQkIZD6xctRZrMNMwRgA5cmn8OxkQAM_r42jakkBwtjEnBlgifRXCN0EUorMn2Dm6J7VT8EJ0Qf6zD9dZA3vT3iM7_Cv-yvFDO3pQOlL7BQZBhRzDa2sOPOq6eAHXs6WagbOP7IwxAmCYncJyLLGhCEu8PkF7LV_IucOsX4LPQqp3Mv5Q8qMoqNEx_4G85a3rns8jCMVgTwTANWyJVleV0FpIF5Oilsl8s0CyqLwuC6727aU1iaypjdG-3lwBgcM4JkXaxGwGNeRFk2rlJfzKb0-Ubi4vrA55Cv4N4Zwt0SQe86NACgaR5X8Bdlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ۱۱ جنگنده و بالگرد آمریکایی را روی زمین منهدم کردیم
🔹
سردار محبی: از ۱۷ تا ۳۱ تیر نیروهای مسلح ایران ۱۱ جنگنده و بالگرد آمریکایی را روی زمین و درحالی‌که در پایگاه‌های آمریکایی در منطقه مستقر بودند منهدم کردند.
🔹
همچنین ۱۷ پهپاد شناسایی و عملیاتی، یک جنگنده اف۱۵ در آشیانه، یک هواپیمای پی۸، یک هواپیمای ترابری سی۱۷ و ۸ هواپیمای سوخت‌رسان منهدم شدند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/452513" target="_blank">📅 20:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452512">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0BfOtx0KZ1ZpUqBJ9RFOatnsceb1i_6zhp4TT2ueSGBbn1LGOeeODI8uonFGGyuUmIbwyNz562Vyne9blnaVrdQbdsBmOCnUJHNhR6_XdOIOmiW0UkJmHWlZMGhg5_nGQxD4X0cT0W_v1O8EGilEYe7fQtq5v6jDHIYHUlC1QcLDC3YvAPPxohSggeGtoqPyLje9jLFGZTPSHuYWH9h8ltylqiSQSBwB86PAS-7EO0Z9GquztHfXKAW51MFVs0xAcDfPOGBMuTnvDfbBCFOF_41he0__or9s0sSPAwdOJNN7rpKvll_dr7pmF8lJrW091aLq20rYGwHx6rKMFGgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر ارشاد: ایران مدیون صفویه است
🔹
شاه اسماعیل اول در ۱۶ سال توانست ایران را یکپارچه و منسجم و عناصر هویت ایرانی را احیا کند.
🔹
یکی از برجسته‌ترین نمونه‌های آن، توجه ویژه به شاهنامه به‌عنوان شناسنامه فرهنگی ایران است.
🔹
انتخاب نام ۴ فرزند شاه اسماعیل از شخصیت‌های شاهنامه، نشان‌دهنده توجه او به فرهنگ و تاریخ ایران است.
🔹
دورۀ صفویه را باید دورۀ نوزایی ایران دانست؛ دوره‌ای که هویت ایرانی و در کنار آن توجه به اهل‌بیت(ع) جایگاهی ویژه یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452512" target="_blank">📅 20:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452511">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlJfrjF84aYQhvyC2mcSBouomNG2qaN4h05fMD4jinXNjly_08L3QxvxBau1MvMuFKAWB5W3oJxoivesvSf5rJiVBNjbL8zx1XCaHgltgvGZ40Y1l70nlceOF25Mgia0HnRjRePTH5vb-WNXOAeywR4Q5wWvGoZAJ43pD8EKTHNIAgVb1vg4r5ZHPUzvo_Qb7MPF7SPKXZF-CXzpSEWrHN_gwE2Breb3DQ2LasHX_iXhIkQileCsxdJO_BzK0Syl3vu9UlYetjhdIcH4MP7ch8ZoJ3TnY3WLS4K4ogvugUgyhjjHQzJqFeVPVqWR40v9D2yt6_CWlX4Xr-Voco-5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت آلمان در تهران شایعات مربوط به تخلیه کارکنان خود را تکذیب کرد
@fals_news</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/452511" target="_blank">📅 20:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452510">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkgVuKraAyWYE1rmDgIdCZuD4-HBdpFh2t9Oe4a20Rr914hOraIWknwc1rhdlGeZEJ5K9I9vHBPi2h7U9QZ3wua6xkxX9SejpPU-4gykJ0rQG51tEXVVHzq6irsXb34aOkjwovNLUT4uv2uQGcHaFQuy3k4NbgbRydQV2ofF-m-qMg1Hd4Y2MU-qwKPuGuRYBoWRYuVohvm-Fh53sCElia5QoOErtZewOVMP4n7OI0XeLS_LgPirb-egwS0jh_dIZ9i1RXvnSgUvIuo5eGY8FijBiWgm-GCQJqL5tG16FO3jmSg7m46Z0gc3KGgZLFj0us-PC7THVRn4Kal9K8RyVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
اجزای لاینفک مرام و مسلک آمریکایی
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/452510" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452509">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOuJYMPtm0xJM6nTEpjmMqdxloFHbfPwBfdJh7ksswBdX1dw0E4VU-jjKnwtMmtIoNKT-n5VyfXmcGBiL_xZpO80PKJe4XvVe1Q7HwVBBppQTiQpE6uXru4vCDr7d3_Y2r-jg5AK0xjrflTg_PhR9h90AqCcX73HYi1mvjfSfbs6ju_l-vo9D97sw1Qs43lMfF82wI7iZvQA6lLaAmjiL5t50O7vnHFI7_0YEfhlnZQ0fsZ34-k3ek5dH3KOnr30eb9V1YyGLSjaWMoIwXgMH0Bx88mfawRLNSZBhLkKaE4Kl9PUD2Tu6IYWcYZn-bwqbMxWupbdv5q02oNOhEEBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اوج‌گیری تردد زائران امام حسین(ع) در مرز شلمچه  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/452509" target="_blank">📅 20:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452508">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c9fa9c75b.mp4?token=cVl26FZP7FVtk2f5PYlvvORo3fXwJumNuCsA4Z_laV0lE4_akiBpq49kor0MFboKx__tkpcfORjs3sQCwA4lXBvscMQaNwG0o0pwyhbdOlngsx6NlROFppAaN6j5eSI_UhfuTRACMkiWFyg6HbC8hEjtudT7OJFq924_5pCJD8kp-5WkENUKi9m7dD966T7OeY7jAH-nTimqSYCOjn6UfyQ7jaHxAQbNzUnHmVK70eVNhZyjT5C9ThIqkXiptkhsVgV5IAGqe2NOq0aWF7e7rknw8cf4HoTTBydidCMuqgFBGANcFNh-XasqvBnE0wyYnEuIDgrWGWjf1hhbv2gg5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c9fa9c75b.mp4?token=cVl26FZP7FVtk2f5PYlvvORo3fXwJumNuCsA4Z_laV0lE4_akiBpq49kor0MFboKx__tkpcfORjs3sQCwA4lXBvscMQaNwG0o0pwyhbdOlngsx6NlROFppAaN6j5eSI_UhfuTRACMkiWFyg6HbC8hEjtudT7OJFq924_5pCJD8kp-5WkENUKi9m7dD966T7OeY7jAH-nTimqSYCOjn6UfyQ7jaHxAQbNzUnHmVK70eVNhZyjT5C9ThIqkXiptkhsVgV5IAGqe2NOq0aWF7e7rknw8cf4HoTTBydidCMuqgFBGANcFNh-XasqvBnE0wyYnEuIDgrWGWjf1hhbv2gg5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صلح‌طلبی این‌شکلی نیست!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452508" target="_blank">📅 19:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452506">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766bf261f3.mp4?token=kl8XsR9LnXBoTIARE_bQw9iJp3g8nj4rbjmOyyi7GlDiU7zlG0lBCwx40_vnCF1dcmoI7kcD-fDSFuiKWSV1wvYiFUDthQJUnFfOZAfaC_bNNNxvI7dnDKzN6HDpsjKPjY_MzJUzBWO-hei-bB6dCKCh4S45CljThBJg8mXcEp9_z7wnuMFqf8pGqu8-c8li9S_TCFCZainBpatykDSjpnSf8BzE11bjz-v8_RJebCpHDh6iagBJxk0CS05Ml6GMYy4dmLe2OUKm61VYdqWun6XS_lVwJBRHzqm-mbLh-Vzzf-cdI8RsMPUj2rEW6vxLTAV_mTs6lFxYyQg1hH11NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766bf261f3.mp4?token=kl8XsR9LnXBoTIARE_bQw9iJp3g8nj4rbjmOyyi7GlDiU7zlG0lBCwx40_vnCF1dcmoI7kcD-fDSFuiKWSV1wvYiFUDthQJUnFfOZAfaC_bNNNxvI7dnDKzN6HDpsjKPjY_MzJUzBWO-hei-bB6dCKCh4S45CljThBJg8mXcEp9_z7wnuMFqf8pGqu8-c8li9S_TCFCZainBpatykDSjpnSf8BzE11bjz-v8_RJebCpHDh6iagBJxk0CS05Ml6GMYy4dmLe2OUKm61VYdqWun6XS_lVwJBRHzqm-mbLh-Vzzf-cdI8RsMPUj2rEW6vxLTAV_mTs6lFxYyQg1hH11NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شهادت ۲ برادر هرمزگانی در بمباران پل کهورستان
🔸
مازیار چترزرین ۱۱ ساله و همایون چترزرین ۳۲ ساله، ۲ برادری بودند که در حملهٔ متجاوزانه آمریکا به پل روستای کهورستان در شهرستان خمیر به شهادت رسیدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/452506" target="_blank">📅 19:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452505">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1wxiiV2rI1hNgxSfiGo6_H-sg6D0YaByNZa4rklSbDPeAsK6uD6ILFPlR0ku5TSMnQeaMwehjugHuzhpsjpkSkCRswJGNiWoeodcvvLzJ6A30boKmwXd3GAcKL7QSu_VT3foAEjGw8E69FkaNXy2-a71Tb0F6Qne50mPspl41ZZg8y-2B44-3VTWQgsl4SIcl60wAPCj_U2gkLFShupyInh69rdeoD6Ev_apXZkNN-bAKElq4lH5UeN4Rpdhx-aVIKKee9iwt--J2-JwcEzm9qgCE4-PxyXfUBvKQnTcoqgL3qzmkTN0DhD9RperuwhghC9MCNkK05R7jsKw3M2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: تأکید می‌کنیم که تحریم دریایی علیه دشمن سعودی همچنان ادامه دارد
🔹
گسترش اقداماتمان را در چهارچوب معادلهٔ «تحریم در برابر تحریم» و «تشدید در برابر تشدید» انجام خواهیم داد. @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/452505" target="_blank">📅 19:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452498">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rP0S3V7YWsfycZExVVfOqEVr7b5IUafPaxFPApYTQW1u9-9NNGlSZQZtBy0E5alBtY-JsNnQ1c_ql1HmETcBvY2owIrntrlvsre8itTyKnEWa619JuwYvMULWOXPtAJEqJX-jxqHaq3War74PGIjsM1TpWdR7bCxyZ59peB8GU0jwQGatLBZfB-0LV3yKfEMBEfUcC5LzZapiWN5L-cSmnv2CAEylvBNtJZHQrukFAxwifBYuqFRtI7YQZbv88-va3May4R6oobizr33RsGOr6gYbXYuMh8oujeGst8I5Cea-LVA7Pa6onHyOIt1UR-9E_a3Z05s5ZwhKtgAQCcxqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDaRyWi1uPyBg67FhTI4enedPFfYNotbHLeHLG7OOIuX2S1IAKDYAZWRtTsOhfRqgQ27X1l-JSG9xc3jiaQKjqijQ41xZe_QJQsQ6eGYgAn7MHGEbsRa8-tQ4lircOjMBUi74AmrMUT3W_2OKzD6s-ft7Qf6jlCfTyQXebYmc0q9icMmQsBA-0IJAZyLENzUyp4e31MlAqTVTDoNV6YjKYt7GBnhadDPVvabOa3Mqi5mXAAsy5LvetaxwHdsfW0mcgn7zjUp161EkmTjWFnb5dsdUfNVjvFjCGn2n65hGHLKNMutdGeoSRra79d2xdVxSCXKnyIGWBaPhofq_sp3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hb0pyNb9o1ayJYuPaio5a9djNN4LfEEau5ZHVp2Lm3Czm_SbSH2K_q6whzpsBrw4NpwEMCe2grGC5febNJFRGIC2b4QVAPkhXvhQ46WsEo4aXDk99g1SX3Ug43avo2MkvTOb0Q9QAvL0UG1QA0j4c8m8cDDufPV18d-lt-o9TAfZb6mzxT0MefHyI811N43ksIp9rKQNwne1n__rbkDaedpRMcda1hLn5Hfzm5Aq3531hI5lbfziCex3blatM9Wpx3NyhRFqij20twggsd5Xjh_9ZclDMKx6neQaHJEk1Nj-Zmm8cOLQGbKr4-sSKabsVl2vmw6FOPFWSMNrnqtANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uf5gK0n7AB_iZkKMC7rtHwH4X-_aAiyDY5U_oyJnQf3zJ13vX2jlr6FHKFZK9-AFinC190DS07A79XJ7dhmrFoQRvQY5qPfh1leZQtmUzip8OxxhpG7BDwotXtbQSqD2K1su5pi3vmwysyi5GqyOeCB_HupbrCu-5BkhQyc3EU1o6icLr0OkLyMLcAwNjUCVFBLtCqJVlMOBg5Arqgc8735CqGSvGfB0J8vh6sBdKjIHzJ9e6GYciLeTCkfKzKKuPpGhLS2fcl_H1MBetKqERVz2EQvxBRbGoTxSgQetQRqDqvekxpQv0Li0uyDAV79ZlLFRMa3LditAS4IAeoB5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkuSvPk9g16QpX7L_tVc9eefF5VVbGcqniORSpQR33wq9Beap9vd6TffCK7REDUvcDHgEQihLrepHw_gaOfxmM2i-_Is336oCAWSEwn1hIavcNUJuv5r5DVhTOBmoM952KyD6WYtA0LEVaNykGAT5_VGiw3-NTghASGZ0v5c52GUIkGenaULiVap5Eyzk4qRRJCjKFHh7H4_D5tchWSJE_n7Ua7p0Z_aB8bRCYJNN5p8os0tfKjl7ifJeZcSSLMbrUTGP6PMRlhya60GGyEl1GdbVeSrjRVEdLHQq8k7OXhWerVBSoGULYHY4LEfffACSJEW85JaoMyw8oYdvGr0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P4yaMLlyAbHBir8IwpPBV63YxZEdK200S1uIwJDxvPkaESh7ZzWuD-UAoAOZi6DEm2Re0J50Pq2TDepA3hVkttDPERe8X9bfjY_ahN6NiJFIkNo9fNDfHPo__yRlhcN9S9KhQEGZvlOfeo9Stdh3xoD-DHLIzj32Vi210yW4czZX4_clFlqS58I6BR_b8VvQ3TFUu6IjakqfNOiS2guR5kz9D9DmAKJAM6cBocD0Jr7vrfdnwgUsVANAsd4fQspxrLORyaQdgqwS5OaJmZ4yHDX4ARD5aUwnZ11MTxEYD-_sWmsCjnQw4CWl2Sf7pXETn6V7Is4WNcckUcrNvoo1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yqwzkdw0cHydod9As5r1aDt6PV0JcxJa-vwikdsOgdj8zXt4rhdHghSjgg5dbaFe7W15tH8sMHb4M-gUrqn5X7jMo3wnslnwMiSyZIMk0CLM-YIIMSlGagQovh1wn_jSIbO4mwzmC_cfEj44SdiTZAJxdrq3q8Rq25aDKrDc2_8BG-jEf3d9bUtdWMfvjsJ8Wn6j4o2JW3DYZLzPcF0bwI-QUVJdPB0BXXZvU5kZnUztpXdD-J-f-m3h2ssLGeFr7Y8zphavd2-HKkGE1qSFFMgCcPCzJ2DolwnGBNnPKtCdwNroNA72cWOtID5hDGCT9hQJ3e0VeLCM9IKPPYt3JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شلمچه از قاب کودک و نوجوان
عکس:
فریدحمودی
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452498" target="_blank">📅 19:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452497">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxuUHsXt0KnfMUmNXmzUko37gDaVIFMGC2K04764WLgTctKRvVK5pGUG6fEfdxB2ddIvIPu5RoF9IlvwscYQBniCOnv9qDBWx50erj7F7EtGr9sYgUQY6-FqTVEb3825kNWHPydv2xAkezXKjBVvFerdZT8a2bvi5P7trURzl47aTRd8mtRhpqVOvpiWkaYrDOXHjYo4rfzp_UM6hscAhHaS1x85iPM-3yUA5297DBZX8OcKytHfSjtYXxJZJF5ofIZn4v5zTK0vEFZp5ONPhV8Cg3fZNtWkEOOOah7vF5kg2skdR_HVQr6oIZH4gQtodf_Zp4CyO9SaG5iP4BE6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی از حمله به پایگاه آمریکا در نزدیکی فرودگاه اربیل خبر می‌‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452497" target="_blank">📅 19:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452496">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎥
سقوط هواپیما بر پشت‌بام یک خانه در آلمان
🔹
آسوشیتدپرس: یک هواپیمای کوچک امروز تنها ۶ دقیقه پس از برخاستن، در پشت‌بام یک خانه در شمال آلمان سقوط کرد.
🔹
پلیس شهر اولدنبورگ اعلام کرد در این حادثه دست‌کم یک نفر جان خود را از دست داده و یک فرد مفقود شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452496" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452495">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f080bfe89.mp4?token=D9LbjTel-JkCTVJ3TrjsidwjNF4dvuW1b2AZt63ZB5adqpiellqrrBTd8psrNpETLqaGVpHgonhGP6MYtcv7p0KVgVmAMTaqe0NshQTAZMCic2Wm8gCl3glWWt2ZzVqUzTlpvQDomZbJlUi91QCEOOeYLfZBVuInzY4ko6MxUg8aJv0n6P0TzYHOJfSsJ_1Fp0lx0UNGL_gQ5Y8e5YpbDV2N-c97JHZSx9x_8CjCGD400c5Cc8y-2ujaUcBfhwNxD0IP23RYRqKU8cd5dlvNPzzVTEJMSNkb0qxxNVezVJGxEhFF_taftX8PnuHVhEfkMj8VPipXMxxdPwAn7W_yoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f080bfe89.mp4?token=D9LbjTel-JkCTVJ3TrjsidwjNF4dvuW1b2AZt63ZB5adqpiellqrrBTd8psrNpETLqaGVpHgonhGP6MYtcv7p0KVgVmAMTaqe0NshQTAZMCic2Wm8gCl3glWWt2ZzVqUzTlpvQDomZbJlUi91QCEOOeYLfZBVuInzY4ko6MxUg8aJv0n6P0TzYHOJfSsJ_1Fp0lx0UNGL_gQ5Y8e5YpbDV2N-c97JHZSx9x_8CjCGD400c5Cc8y-2ujaUcBfhwNxD0IP23RYRqKU8cd5dlvNPzzVTEJMSNkb0qxxNVezVJGxEhFF_taftX8PnuHVhEfkMj8VPipXMxxdPwAn7W_yoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه مسیر پیاده‌روی اربعین از نمای هوایی
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/452495" target="_blank">📅 18:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452489">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jmo5xR61Y3itxKo-YCyfb1E4PCI0BhreTWqSi70r-obN731ZGANi4_tEMxDBb-9HPHlwqAOWPcLNCd494c4dbiEircTv-gWfraBK7_SC1H1VUdCLjLw4GXNaIYAuB5qFCt3eP-MApBq9SRYdl_WZsAIY8LYUiOLapG8Hygt1mtWtcE4mvdgUbMWMCq2gmlXvSS4LJNE3raBtqUBdNzc57cz1EzpNBJtxgkDtOnfJhtCEU2JJdCOPzNVnuZQ44GkjjEna3akSePmTZ8Usz6OOAwK28Kt5-1SBM_kCE8VSam7iiB6OQVL18CIeuhO8Qfkjr2E6A6_o8P_6LuzbS2i-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mi3xKI2TuPGTn509RW7JDdZlvqIcx1s5T37e4bRkmatnw-Wpscpj2QnjSDj62A9Hv2ZNEpWq6DFRhnSfG2Qeb3WXPy5m4UkVsnMsiiqne19s22QMOHvWAYfN2Y_S41FdYhtg8xTurZW77LBHhhgBbHDRdspb_agEQ6z16DqPNI0Xm_hpMCy6MRiVWv-PI65YwIx4hH7LfAz7TexzS9TuZXVdNvTNEPfGvPAfUPhut0EtICpYjQnIWZ_dA9pafX3Eoskq86mx2PxA7-SxqF6i6i2jLzRZTU5M9V5R--aiF8T4F4xHhnCAM7E_9obW7isbIUEG0c59oimP3Ik8pu37Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwdVMI6JvtHE0v7sVwiYLctUwjSW9KkSwUB0ub72Vovl8YRLh-Mb-Uvqn_fTt8UtFnkQaryJ0xFE-rp1lHg0Dl0kLKNoi5eXDbzY1SRtUbOFFh9i_7p_PitxssIIWrSE3QsbtPMS5__cgPgwfv5Y47XmZjMSTSqh7ZmDLNyLaeYhIiXnqGCVxfX36W7lsB9MVV_4wy2OvLpbaLhK6PPBYaXUKDWQ0TpLG7bcQLu_xd5SeA2QeWwQVF6UyJ0iwU4Prg-4rUOiw5ZFYdG_qkq2qAxIWUQ_NyC5NtrKDV6nbsIspRiUgxNlB55mqJjxxOJfGlRggzjQPwdHlasFG1etIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haVyKWgtPxFlPJs7uKGFPuz0i4VpvfAECnpPDpdPDuIl9eJK0VEymnJ-oN_FhicIhKBWfB6EbfATHPSPSIlSHIfH9J_JmVOKrzMcZ5KQxiRFC2OpKYKgKgvd0nyBQt5cjiAnw-FfeXdqWjVoLQtXQeHC5YIiDPJnc_MyyIEG_JX29IHSTkgGG-YgN4r8Mmy_HcETa1UABOFjV6F1s-a1zz15AYNSg-cp89ExdDOz-WR5U3IH-Jlicih2nl1yA2LEK3-Y1uKb5pe0X1Z29kDeAYX-5UrmuQDMhEq8DiJ5WZdzGIAAvZAZ1c71z7_EI06QaJp9FhdIKYvUg23LOwnMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe7x11YvGVUs7KV5wBkOPHyk3NI14Gb_TXH1Qt80d9mrkRcf1wTBypCzu2QlA5INyLZBPZ8spdAi__qQXpsgb-1uVGpNjbcXJQORyx4RgyI1F-p-NZXQF7EeqEq6wrmGRwLAOVwDrpekXlFRWw2dkT2paQgq8ZJKNARp73Z7cqvt3qHTeFzND4m2oqKO4lgqhJJ534n-REzcYQRwfhtKPopRI1aiMhTzYnWLRXb55hY63KR_Z5g0uYZbvzA3k7CAlDeXR9TbOZfS_RJZ-sXw4u9yvw7rCddtmDHHga21BAIC4QjVbKdrMdyGu7IpsM7qPgrcEhaDkLStl9CLN1rX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sfs44bdvbD-PTvu9pyG-NQ4n8olNmfyNavp0sMQFbbLBvW6xDT4JHUVLOBnGprdGVGwb80vdwPA4OG8WaOgVVDFToyDZMjcRdOLtiIUPhGR8wrnx_plfjBK0H4tmjtCyPi1UkNV2B_oDG8laYg5kAxHvc9lyarausgNBVidhlL7dYNqu6Ehwl345qSxyN9u5BR6PdmSe0vSKkatr59oWMJzyERqe48Q1o_6pJ5N7dSt20R3IqkCpg3I7SZq5hztB-afWgF5qjjrfqOU4iy6JP20udqxyoTW1nglpzQyVysBvgnGlYq-UtKxkiaTeMoFw3_7X491ZeYgDaW3J38hm5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هیئت نوجوانان آرمانی
🔹
تجمع «هیئت نوجوانان آرمانی» با محوریت برنامه بدرقه زائران اربعین به نیابت از رهبر شهید، امروز در حرم حضرت عبدالعظیم(ع) برگزار شد.
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/452489" target="_blank">📅 18:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452488">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac1ea01dd.mp4?token=NuDCRjNlo8W2rBnTv5DD3yU1Tf4b_pfpZ_Q1JkikXthDowZ03UYxOS4xOvTRkGbJEn4i6lLDMgXYhFnp47XShrd8gq55U80h-Tq_Z6Q0I3JLnfSE33RqoCRy52H3Mpl1ENHi9YKa-iir7C_1ZfqXc_ywm-vq_6_CT7Q_8Ja00jalgIsJpKyvOdqE1d_4jlierwlKLyjpowY0V1ADq0Cn74qlLDEtb6ikZJd3YoQTOmBtA8strleETvh_0Zg9xf_gw1NblwdaCetPqIxH-rhkztdo3EFu2vh1rnUH4SScNQrkEiAFgr9eAJr0xmiKmtVT285U4tUA81SzovrFXBW_CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac1ea01dd.mp4?token=NuDCRjNlo8W2rBnTv5DD3yU1Tf4b_pfpZ_Q1JkikXthDowZ03UYxOS4xOvTRkGbJEn4i6lLDMgXYhFnp47XShrd8gq55U80h-Tq_Z6Q0I3JLnfSE33RqoCRy52H3Mpl1ENHi9YKa-iir7C_1ZfqXc_ywm-vq_6_CT7Q_8Ja00jalgIsJpKyvOdqE1d_4jlierwlKLyjpowY0V1ADq0Cn74qlLDEtb6ikZJd3YoQTOmBtA8strleETvh_0Zg9xf_gw1NblwdaCetPqIxH-rhkztdo3EFu2vh1rnUH4SScNQrkEiAFgr9eAJr0xmiKmtVT285U4tUA81SzovrFXBW_CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرد عراقی: شهادت امام خامنه‌ای مثل شهادت امام حسین(ع) رمز موفقیت اسلام است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452488" target="_blank">📅 18:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452487">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur_IB5xeyTpysGbpT0eQiuMT48IJZJ7uuympdU-RgV5JlLJ__X871wCZ6KCBdh_dAQDaxZ943vGUAc-CdnDmp_SKX3abC-S1sVAGqOqU7PleRjzl1F7A3UCNsrwq0LQxOoeJIDFp-X_S2zs3I7iUXz0Hyl-jQXnM5_ehqbVGjbeQNbaAXwfHZMPZoPmdh7J6Nl4lsF_V9rBUh5Zb7OnJzqNwkKFBFKWMeVGIvd_gi6PJq7wSReVnAwHQE2OrrLjJ1ZKu9cfwCiX_ryH1QCgAFzXofTtY-OxJzcmvI5hN1GcYXqnGaSqpeItCe3clszTJMGSoy5mYAXul6FwkjKb6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفوذ هکرهای حنظله به زیرساخت ارتباطی ویسکانسین آمریکا
🔹
گروه هکری «حنظله» اعلام کرد در واکنش به اقدامات اخیر آمریکا در منطقه، زیرساخت اصلی شرکت اینترنتی
SupraNet Communications
در شهر مدیسن ایالت ویسکانسین را هدف حملهٔ سایبری قرار داده است.
🔹
بر اساس ادعای این گروه، این حمله موجب اختلال گسترده در خدمات اینترنتی شده و هزاران کسب‌وکار، شرکت، شبکه‌های دولتی و مراکز شهری با قطعی یا اختلال ارتباطی مواجه شده‌اند.
🔹
حنظله این عملیات را «پاسخی به اقدامات تحریک‌آمیز آمریکا» توصیف کرده و مدعی شده است که این حمله، آسیب‌پذیری زیرساخت‌های سایبری ایالات متحده را آشکار کرده است.
🔹
این گروه همچنین با تهدید به ادامهٔ عملیات‌های سایبری اعلام کرده است که حملهٔ اخیر «آغاز راه» بوده و در صورت تداوم سیاست‌های آمریکا، حملات گسترده‌تری علیه زیرساخت‌های این کشور انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/452487" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452485">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f612840789.mp4?token=L0EGcE21DlQ1L99kBuBQ3rq3hSQ_TY6bre62Mlk48qdpN1ossm6EDWKYVg0JpXL3i1INjlqmCe9rpUON8BCGnom4uPJiuNd8750s0JdUpP_xIp0VZyIwKVLZZ-EPur30ASD_-oWFE3SvZLAUamR25k21I18ziovc_otTy7KVKhld8yEaRYKnnbXJLYXTT65Mol0CrlbYwlRq_dQH8qA_LRXnE3UyNhM-VaVtdOgc0zjTef9WQDlZhvNz5Fe9pHZ0qKfktMV-qCIHSWa-VsT9QDvCFcZqbG0IkDznE_w8GSQ_Mr8ffu3qARbalRipS8s5iCV0JzN8qlKFd0cPGk5iJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f612840789.mp4?token=L0EGcE21DlQ1L99kBuBQ3rq3hSQ_TY6bre62Mlk48qdpN1ossm6EDWKYVg0JpXL3i1INjlqmCe9rpUON8BCGnom4uPJiuNd8750s0JdUpP_xIp0VZyIwKVLZZ-EPur30ASD_-oWFE3SvZLAUamR25k21I18ziovc_otTy7KVKhld8yEaRYKnnbXJLYXTT65Mol0CrlbYwlRq_dQH8qA_LRXnE3UyNhM-VaVtdOgc0zjTef9WQDlZhvNz5Fe9pHZ0qKfktMV-qCIHSWa-VsT9QDvCFcZqbG0IkDznE_w8GSQ_Mr8ffu3qARbalRipS8s5iCV0JzN8qlKFd0cPGk5iJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راز نام‌گذاری سیریک چیست؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452485" target="_blank">📅 18:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452484">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19d35bbfb4.mp4?token=eVAQ1YouglfGbM4bdklcLp5x3pg2Y8HIBYIqNxwosFzjwVZohfoyHsEqcVAwuzCt0vNstHC8HN-4QgBfVhPMHnpX-QK67g89lBtkfiRdy4vr5iOirF9kpWD1RJYpJPn0HlqkVSIzc8W05XRw5Si0CsiqhW4agsRUombPwtgb3Yv4AvBp6csjFgDAdamyTHLaaLdjKTUb61vGso6DQ568kRQST0GmQmEkrVoBRi25_rGAXN0ykWZqIOn47A4invwBnviHRZNQEvGY_YDk1v6vq5VqejR0gFZEFLuoue2gm_O_jiHtiBf9N-X9_q_60X9EeoveQLafUFVVYXhIdAtRPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19d35bbfb4.mp4?token=eVAQ1YouglfGbM4bdklcLp5x3pg2Y8HIBYIqNxwosFzjwVZohfoyHsEqcVAwuzCt0vNstHC8HN-4QgBfVhPMHnpX-QK67g89lBtkfiRdy4vr5iOirF9kpWD1RJYpJPn0HlqkVSIzc8W05XRw5Si0CsiqhW4agsRUombPwtgb3Yv4AvBp6csjFgDAdamyTHLaaLdjKTUb61vGso6DQ568kRQST0GmQmEkrVoBRi25_rGAXN0ykWZqIOn47A4invwBnviHRZNQEvGY_YDk1v6vq5VqejR0gFZEFLuoue2gm_O_jiHtiBf9N-X9_q_60X9EeoveQLafUFVVYXhIdAtRPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیرگذر میدان سپاه تهران افتتاح شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/452484" target="_blank">📅 17:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452483">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در زنجان
🔹
سپاه زنجان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در غرب زنجان، روز یکشنبه ۴ مرداد، از ساعت ۹ تا ۱۲ وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452483" target="_blank">📅 17:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452482">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f5e69327.mp4?token=EwEPkyN1yIDNjiVfxfVVQT6zN86y1ZZTvu0timw3gkI6ZZ3IiUbIl0cWVuyZEdLTViLDYET8bzMleHp7LjWkoYSclfUMTAhEYvVew_Xzp1dJ050nqal276ndAczJIX-Jj7nt9a83JQu5TdPqV8Q7CGENj4hOqexAffRX_STdFQS2iCtLt5ba_7q-7RxI6QMbJtjzmkwbC2xA7VbevCUc7Od9mHOUuet2NOitNOoyrcDGokD-6CERBk7ZCVYgNVA8mf79tIP6N1qtseiSie4gt8iIgJkjbG87j-ifa28mihUM47wTvf8S7jkYqpV-VYRXgXQP2KWXdL6M84NM9rXkHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f5e69327.mp4?token=EwEPkyN1yIDNjiVfxfVVQT6zN86y1ZZTvu0timw3gkI6ZZ3IiUbIl0cWVuyZEdLTViLDYET8bzMleHp7LjWkoYSclfUMTAhEYvVew_Xzp1dJ050nqal276ndAczJIX-Jj7nt9a83JQu5TdPqV8Q7CGENj4hOqexAffRX_STdFQS2iCtLt5ba_7q-7RxI6QMbJtjzmkwbC2xA7VbevCUc7Od9mHOUuet2NOitNOoyrcDGokD-6CERBk7ZCVYgNVA8mf79tIP6N1qtseiSie4gt8iIgJkjbG87j-ifa28mihUM47wTvf8S7jkYqpV-VYRXgXQP2KWXdL6M84NM9rXkHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اوج‌گیری تردد زائران امام حسین(ع) در مرز شلمچه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/452482" target="_blank">📅 17:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452481">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568ec4ada3.mp4?token=h99jND6A-3T-u3LDCj-_WNn0rE9GbMfE94GXkeglXbSvhlbgRbZNos-lCXppyviZDV0nLcSXPMq390wFS9nCGD9gKebjsNygbTtZ-zwS1cz22grlIw8SHxVzjnirdYSCGSGBAH5UqfmxdnaMF-rLWKkdFjVuTnMnNF59SJ4np9ps0ruUzW4PQAoocxflppSAcrYZC8i1zfYQ9XseBU475kJHsMJM0UHO6DnX2J9rng5ViF78QI_7U4hIC-NE1RAqyHLammQyRZHwYamEs4s4HsMj4wJql-oSoimm_PcHQRtfrZr-8AT72dT-eWpE_iPu-YLfofz6rFVurmwIKIuY5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568ec4ada3.mp4?token=h99jND6A-3T-u3LDCj-_WNn0rE9GbMfE94GXkeglXbSvhlbgRbZNos-lCXppyviZDV0nLcSXPMq390wFS9nCGD9gKebjsNygbTtZ-zwS1cz22grlIw8SHxVzjnirdYSCGSGBAH5UqfmxdnaMF-rLWKkdFjVuTnMnNF59SJ4np9ps0ruUzW4PQAoocxflppSAcrYZC8i1zfYQ9XseBU475kJHsMJM0UHO6DnX2J9rng5ViF78QI_7U4hIC-NE1RAqyHLammQyRZHwYamEs4s4HsMj4wJql-oSoimm_PcHQRtfrZr-8AT72dT-eWpE_iPu-YLfofz6rFVurmwIKIuY5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: عملیات دوم، اهداف حساس متعلق به شرکت آرامکو در شهر ینبع را با چند موشک بالستیک و کروز و چند پهپاد هدف قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452481" target="_blank">📅 17:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452480">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌  شعبه‌های ساعدی‌نیا همچنان پلمب هستند
🔹
دادگستری استان قم: هیچگونه مجوز بازگشایی و یا فعالیت مجدد برای شعب ساعدی‌نیا صادر نشده و شعبات این برند تجاری همچنان پلمب هستند؛ موضوع مصادرۀ اموال ساعدی‌نیا در دادگاه در حال رسیدگی جهت صدور حکم نهایی است.
🔸
از ساعتی…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452480" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452479">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kP0-vYV8Kk00Hn7qRMYPFqJWZ5jl0umI9P0Kkcg0hZRUW2lwXrnvjsP0uooEpKTvwFrpsAEabeUiUYTkgdD7YFBnQ0chbNFEgw12GAey0taeLnlPi3VhztZhyCo13DTkGJYzSImqiXnEjdcTftgWnQLJYi12KOt81H-vSRIq7fKIA_OpTA9jhQFfTCj6oM3JlNidu20SqhiAPVbDFtoC_pHf6OvQimRqMILg3hS5gtfiLUfuKLvOdfRxe4e9zYAItsLsEZMugtifeyVI06Q9g9PdwOLF3OZTAewKsRWv81pjVjji-leyWEq6cBj7zKACiQS_ambmPR21dOwRy58mPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس خوزستان: مراقب کلاهبرداران اربعین باشید
🔹
فرماندهی انتظامی خوزستان: افراد سودجو با ارسال پیامک، لینک و صفحات جعلی و با وعده‌هایی مانند دریافت ارز اربعین بدون نوبت، ثبت‌نام فوری ارز زیارتی، در تلاش برای سرقت اطلاعات بانکی و هویتی زائران هستند؛ از کلیک روی لینک‌های ناشناس و مشکوک خودداری کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452479" target="_blank">📅 17:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452474">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJ0dw4yoB9Wh-gPNgequsSNrKSi5xBGSLYVWrKtlIe_SBTD6mJ7gr0rFrZBHbeVZjf0iCfUQ_GW2K_0puw_k-iqxYztVMfcOfFdSHwjKx334idpy7efrKN5TIqcMheqtugrp6y0U65uU3fjthgwHF6vVh2YHvB4E8jMeye2OcJoX6sZbGB5hfxWlIYfC6-28BJuqIDnuygw4TQcYBgrNDsVIdZkeGALsMHqIoLnntaiFnoDWpQbPaJKCdYLCgwUYsZqMA3LiIkAEUtxvWRpZyB52UsnA8el7ExTxQ1Np_XicbCJ_ksGMWwpYsx-GkvpkpvkTbulapRcNrPqUzSOEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vLr6mGsL50P3XCeXcHxyuJHS1jCIlHApIwAA-ui0TaL5uqZNhAjPUHSXEXyzrxmE9WbNYrJPv2ZrsI5wldNbcV0by9iQ9_z63gOZ9d6S4oevt9LJo0BTwD4Uve6l-nci8o_MaMosxL9ajToVsrOf05krD_gnsSzWM0oWJEcWIGT5jj8UbIhmKtQ2GJneBwjxcSsap10rOXtKudlY0itkXnH51oqlp7WN6IL_7MZkiZyYbXcOgv2iXo-qxeQ4NS_AITlAsffKKlI3jYp9fH2toxj-m9xYtQT4hWAHN764O77W1_dTXMMyvoIdqnuxwG-3QZko4h7bOqaXzk57Se9TTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLc5D63AqAxIw6WeKFR82xGbRcvni18x78f9PBcyC0DJFwc8YHnS1DQI50OxphBcJF-aIZJg-9WJs-QEnyZrHIE3LQM1XZ8Mgvf2AgZA9zTe0q4Cd0u9QbbHv1zZvgmzXR38qwEELaj4zU86hOvhGXBB6tSsDvgnNNHQgIoKjOLlE_lOGoxhG6KK2EBNWZRX64SsCQgoGdiUwUrxAIH89rQ9EtB5GiD2rWgshK1QpBK7aFD6n33tayzIJlNuhqJJ90v4Cq7SNFVEgwBzFKl2KXxbmwoI94D7Z7hjYLoziWau7hFXOplAhWWfvP_VHZCc36Fy9baIdVtkFk8J3Y-aAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOMw7SyGwyg5LSnnlXUwMsJ4-_86vnjuY_d55SwPczvJ_qbyLXGpI7utUeV5XmYAX5pCl-gBNpE0m09DmBC0MCs1GNQX4kdI7-qB-iBUR8lxTRTo2vSC0lQkRiAcaDRaBzmsYVufVujmSRCXZdOX__P6JlZKmd8UJvMMLHc5CsNylZY-zrzkWQBRg5dYDJYfweehtohGAsUcwuRnkl9_He9BWn5xN2WfnQy9Y6BH-sJe34oOBI1jcTDWrxtTd8ufY5N7I2f5vukXAYuWz92AdvBBQ4sAa0-awBCFayZDER1ZVGZ3K9HireGxdYOc-s9S9wXRlLcbTpf4O93BTPQ3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkZ-B4RoPL24K53KymVCVEBG0Mzchy_YzkoPval4FQsXFCDCpp78AR8dxqwWIZa6P3JU5C-rYe_VKILlUZCxyyM0XZtDtcNHyzIBroAO9Oml23Q0L7QVcnUr4n7ILNA1okPFWBcNoWDdSYV8Jszy3IjOVy4ndTLNjlgYgte8ZL01DLzHFAOiJhGa0YOV5IBv35pmV6gGfDNDGythRvZwFhesNkGwfxnAQ3ZrFftToSfyFM4uCNXJgWoZauyMzEIG83XqACMF6v4Rk0enoyRzaJX3F2hwOABubG_OiCfhLhBoDYvXwzw7kF2mi5vnHYZGFaA1D3Fca767P4uOgjJ76A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت گندم از دل مزارع لرستان
عکس:
نگار ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/452474" target="_blank">📅 17:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452473">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f50f57b7.mp4?token=XzoTlSMHltWD0D2X7EGkAhT4L_y4U35fR-Pcq4dH_oBcn8Ex6PHMg3vZ7I-JQR-rIP5H79GMnMhZZT0THS9MabhYKTpLYRHu3daQ7HKf7Ik483iASrx9H1cUMWvIL_nwbPrhJ_u_NoO25r63ZiPZmMT_BwOi_hcm6C_hys1ue0mg9ClgtP8ZRlpa8nHrIABA_BA7UMk7zrAs67py8HtSrBh39Rh0Z6gNyvtpHSqI9uKhdYu1RMbopzMX5F2-6iUuYHAMvbeMBANTqbrhzyDqgk5Ueufe3qgtk4liHCBcnPUDWI0GDTsVRB9KN5x1np9gSRw2ASNxnB-8JrUac2Kh8URcMGnnNCNTfREbynwBjTl46cR9du__DsE68w0ct_IQbQvBRl7jlllalXmTyADDyav5Nqe-amwFeJDb2uJ9Kzl43F6iBYqFjcSI2aC5lxz6gC8OXoJXPN5fvTNHpvrYGvEto5pbz0ZWYeUpeOAi-8r1Welc8_EimoekAzUm8_YpP3gWc-XpqYUTF1QPHLlS0jNmcu0Zc64IlcE4HfzN4xeRkoSep5DnR7nLaXDKssGAstlcvrfvWZUPgCRQ5WsOon8klaqXiNQFN6FdDmnXCLTdR1JfZeP5ZUBjaL-FTlfe2bPNtRmZg-k2R-drPafPZzw0WSsZCRt1zsfIISzArDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f50f57b7.mp4?token=XzoTlSMHltWD0D2X7EGkAhT4L_y4U35fR-Pcq4dH_oBcn8Ex6PHMg3vZ7I-JQR-rIP5H79GMnMhZZT0THS9MabhYKTpLYRHu3daQ7HKf7Ik483iASrx9H1cUMWvIL_nwbPrhJ_u_NoO25r63ZiPZmMT_BwOi_hcm6C_hys1ue0mg9ClgtP8ZRlpa8nHrIABA_BA7UMk7zrAs67py8HtSrBh39Rh0Z6gNyvtpHSqI9uKhdYu1RMbopzMX5F2-6iUuYHAMvbeMBANTqbrhzyDqgk5Ueufe3qgtk4liHCBcnPUDWI0GDTsVRB9KN5x1np9gSRw2ASNxnB-8JrUac2Kh8URcMGnnNCNTfREbynwBjTl46cR9du__DsE68w0ct_IQbQvBRl7jlllalXmTyADDyav5Nqe-amwFeJDb2uJ9Kzl43F6iBYqFjcSI2aC5lxz6gC8OXoJXPN5fvTNHpvrYGvEto5pbz0ZWYeUpeOAi-8r1Welc8_EimoekAzUm8_YpP3gWc-XpqYUTF1QPHLlS0jNmcu0Zc64IlcE4HfzN4xeRkoSep5DnR7nLaXDKssGAstlcvrfvWZUPgCRQ5WsOon8klaqXiNQFN6FdDmnXCLTdR1JfZeP5ZUBjaL-FTlfe2bPNtRmZg-k2R-drPafPZzw0WSsZCRt1zsfIISzArDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وضعیت پارکینگ‌های مرز خسروی
🔸
مسیر ورودی شهر قصر شیرین تا محل استقرار پارکینگ‌ها در مرز خسروی در کمال آرامش و بدون ازدحام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/452473" target="_blank">📅 16:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452472">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0xZ8zfdUjUJYqdLvU9-L3g9WttWrZ3FXMDDAfgusy_eP0VUfVwkM0dBVn4xfeujB9Q6xHYqFNlql0KHwAoIX-giiAGYpijsKweJCz6CkJmuz-o3nr5L79yHaM-OzJ2-WtKHLk9jKb7wMeqnWsJGGhAWsvGDIvQjwf2TWo3awuAX08VkdEUQXwcUiLw-1sTSIp_y9IFznBxhwCoDpkrkFd6yiAJnHJUvZles-feLlajkbU3cPxpLsMIbJ4q-W2omrIVLSGVPugb07K03-ZphjPq1vUweRRudSTcUP67vpMRQz555bfMj4gj8gZ5fpbn0nn-mTCov3wMV8HXKoNMy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیمه‌‌ها عربستان را گردن نمی‌گیرند
🔹
هم‌زمان با تشدید تنش‌ها در دریای سرخ، شرکت‌های بزرگ بیمه‌ٔ دریایی مستقر در بازار لویدز لندن، از پذیرش درخواست‌های بیمهٔ‌ خطرات جنگی برای شناورهای مرتبط با عربستان سعودی خودداری کرده‌اند.
🔹
این تصمیم که به‌نقل از فایننشال‌تایمز اعلام شده، شامل کشتی‌هایی با هر پرچمی می‌شود که پیش‌تر در بنادر سعودی پهلو گرفته‌اند.
🔹
بر اساس ارزیابی بیمه‌گران، کشتی‌های سعودی در کنار ناوگان آمریکا، انگلیس و رژیم صهیونیستی در گروه پرریسک قرار گرفته‌اند و برخی شرکت‌های بیمه نیز در حال لغو قراردادهای بیمه‌ای موجود هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/452472" target="_blank">📅 16:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452471">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
منابع عربی از حمله به پایگاه آمریکا در نزدیکی فرودگاه اربیل خبر می‌‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/452471" target="_blank">📅 16:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452470">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/019e07e598.mp4?token=UL5Enu1zxlghtAlcJjQZkV9eo0lTzXpzqfJWrGsl7rvHQooyH-tvDzCAF6FuZMdAFx7YgGS4R7im-PQQRtWnFlXcmLqWdBY2kWnwjCuFsAiryozXf0Wht1JTcVQGRXuhwW5XZZVrJ5aUjUXJZjtNerjUshEIsembFRsL2ZET_-jqKT9EbymiRLsW18ubq2a9AnU6b1Cfw9PY4BboNxRRudBDDL6mu5l6gPOBWXpWd7eBKtLYr9HeFniOMZItKxFrnlLIe0fCpjaqFbbmAtwLGjFG4KsY67vYMWdYhNoEtiuxErHqMgvP8DsMsqJ2MAREdzvgaELQ0w1tOlcdOIr-w1X7SmZZ1vCae0CsTktz3hKkS76AEu73mLTzv6aaR_Ir_nj_SRlz4KYAyGX53umgi5JK8SVtkUI9mkY-JeGJyG10FDHschzEoJk8iUhA-GrqRXiU81uxqON_Z-fJ2c8cfgM6EDl17dZldsFlDY9KE1Ccbm_YU_eICkdJ550l5mlCVWSUIwAexPAsmQ2D9nCphnIHAVze0V6HwRjPEOEagwIDyZM-a_tsTJGlZYGWPVEFQWmyGa0NfLb-JAaf5XcpoLiFkFH_XzqaNZJGpIog02RqHN7tambNbLl_-kPsRQ9y_8MmrPFIpUVnbxbpUsSm49maJ8uzZF4GhU7_-ucJTQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/019e07e598.mp4?token=UL5Enu1zxlghtAlcJjQZkV9eo0lTzXpzqfJWrGsl7rvHQooyH-tvDzCAF6FuZMdAFx7YgGS4R7im-PQQRtWnFlXcmLqWdBY2kWnwjCuFsAiryozXf0Wht1JTcVQGRXuhwW5XZZVrJ5aUjUXJZjtNerjUshEIsembFRsL2ZET_-jqKT9EbymiRLsW18ubq2a9AnU6b1Cfw9PY4BboNxRRudBDDL6mu5l6gPOBWXpWd7eBKtLYr9HeFniOMZItKxFrnlLIe0fCpjaqFbbmAtwLGjFG4KsY67vYMWdYhNoEtiuxErHqMgvP8DsMsqJ2MAREdzvgaELQ0w1tOlcdOIr-w1X7SmZZ1vCae0CsTktz3hKkS76AEu73mLTzv6aaR_Ir_nj_SRlz4KYAyGX53umgi5JK8SVtkUI9mkY-JeGJyG10FDHschzEoJk8iUhA-GrqRXiU81uxqON_Z-fJ2c8cfgM6EDl17dZldsFlDY9KE1Ccbm_YU_eICkdJ550l5mlCVWSUIwAexPAsmQ2D9nCphnIHAVze0V6HwRjPEOEagwIDyZM-a_tsTJGlZYGWPVEFQWmyGa0NfLb-JAaf5XcpoLiFkFH_XzqaNZJGpIog02RqHN7tambNbLl_-kPsRQ9y_8MmrPFIpUVnbxbpUsSm49maJ8uzZF4GhU7_-ucJTQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مرز خسروی کاملا اربعینی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/452470" target="_blank">📅 16:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452469">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t82HvPAsbzxXlJaaLTwicgx8hBT0gB-o0-fhhsQ-fvWDb_3q8idkO9ysq4pr-Pzx2-WSYhTP47D5N5quUh3aY4iLaWVluQWGu_MiFJzkbdi6D1zaj--aWy1SpbkX9bdF5EY0FSCFFR365DMmMuZ3WxoP-PS_QyuH8jpBoee6hpQfDXrqTcQZuVBwCip6kGopGhYh-Qn9cFAsg8lVX3KlUBB7-v_DCAS1fsRN1njbHDyB0E7PIly8idDdRp76uZefy_q4tCvg2icx57nrW8IGPACdIcbnvM3FwzpVEgs1CFed7vNmdqrBaV14jsN814Lok9PJIFtIjd2yN_YFvwDcxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا با چینی‌ها هم به چین نرسید
🔹
در المپیاد جهانی ریاضی که به میزبانی شانگهای برگزار شد، چین عنوان قهرمانی را کسب کرد و آمریکا در جایگاه دوم ایستاد.
🔹
نکتۀ قابل‌توجه این رقابت، حضور ۴ دانش‌آموز چینی‌تبار در ترکیب ۶ نفرۀ تیم آمریکا بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/452469" target="_blank">📅 15:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452468">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqmr0KpVXFuxsnnh4LhWDPoSrV7upnRv4VZ2ywoO3AnOT4MUie2M-DVR6CXCVblfJjKY2I5ou-WPounMOsn2fFb3zZSa1i9AcIwZdSi0_ZwaL2O8EcdqA6N-z4WqxRdqKj1HHrsiJtaIhq8-AMzPCHg2hRfTtg9SOr_QdT4iKw9frQPR3u-SkUxtrRy4498GiEftSocifWh1EwITGWVHPYGWKh3tNX2D6QDC3SL2U1g-08_yrebngYh_HphLpmOqr1b0pu5gqeIJW03J7Q9bjn6LKTax2qo2_-RrqLCvSaAEHRfmUy0LSjJ72LJLvPX7g8S-rBrDuF2BQ6Qo_y14Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان همکاری پرسپولیس با اوسمار
🔹
طبق اعلام باشگاه پرسپولیس، با پایان رقابت‌های این فصل فوتبال، همکاری با اوسمار ویرا سرمربی برزیلی به پایان رسید. @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/452468" target="_blank">📅 15:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452467">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: تشدید در تجاوزات، نشان‌دهندهٔ اصرار دشمن سعودی بر ادامهٔ محاصره مردم ما و نقض حاکمیت کشورمان است که این امر قابل‌قبول نیست و مردم آزاد، مؤمن و مجاهد ما با قاطعیت و تمام قدرت با آن مقابله خواهند کرد.  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/452467" target="_blank">📅 15:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452466">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: به لطف پروردگار، این ۲ عملیات با موفقیت اهداف خود را محقق کرد و اصابت‌ها دقیق و مستقیم بود.  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/452466" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452465">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: عملیات دوم، اهداف حساس متعلق به شرکت آرامکو در شهر ینبع را با چند موشک بالستیک و کروز و چند پهپاد هدف قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/452465" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452464">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: عملیات اول، اهداف حساسی از تأسیسات متعلق به شرکت آرامکو در جیزان را با ده‌ها موشک بالستیک و پهپاد هدف قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/452464" target="_blank">📅 15:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452463">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: دیشب ۲ عملیات نظامی مهم علیه تأسیسات آرامکو در جیزان و ینبع انجام دادیم
🔹
این اقدام در پاسخ به تجاوزات سعودی علیه شهر و بندر حدیده و جزیره کمران و همچنین ادامهٔ محاصره مردم یمن و نقض حاکمیت یمن صورت گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/452463" target="_blank">📅 15:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452462">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: پدافند هوایی با یک گروه از هواپیماهای دشمن که وارد حریم هوایی شده بودند، درگیر شد و از انجام جنایات بیشتر علیه این ملت بزرگ جلوگیری کرد.  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/452462" target="_blank">📅 15:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452461">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‌
🔴
نیروهای مسلح یمن: عصر امروز در بیانیه‌ای جزئیات عملیات نظامی گسترده و مهم را اعلام خواهم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452461" target="_blank">📅 15:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uix64kNHalk_aYCehBjOjHZhxVDsQrj8TYd-oAP6D9Sn_Eq-3kBFyo18cTxIDMDm-yV1MzkbRebLcrOTNOfpB0OIbakdVk0fKsOGIWGbtQRS860VpGtktb9vLOLaBsfedghImu00IdE2TW90D9ZTYqrvGSAVx40nQUj384QflP67tIoRySBP5i2iO6BXPw9D20dCuN0clycxKFJKDV1uTrVHx_2R-RouMwimDL83Z8SlchBkAQLE3octn8lZLgJM3Cs3ROZo2duDq5zJe76xLSkfqWbzhdGjbkq-njSVeZBRBb11AaSu1BN37tcCC8GU0VEkR4n7k2DKBRvX8ESarQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنترل جاده‌های اربعینی کرمانشاه با پهپاد
🔹
پلیس‌راه کرمانشاه: امسال ۲ پهپاد به‌صورت مستمر گردنه‌ها، نقاط پرتردد و محل‌های احتمالی ایجاد گره‌های ترافیکی را رصد می‌کنند و اطلاعات لحظه‌ای را برای تصمیم‌گیری سریع به مرکز فرماندهی ارسال خواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/452460" target="_blank">📅 15:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452458">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d560d16c5.mp4?token=FWOGHa_ZKh0rKxsJCYZn7grfIQbtRqIFe_V7SgkJvOBp-c5878Brhcuyv6h6Sq2E0Mgmpl3NALNyBFsfJpwOnTN2ngyTa8bJmiIFCJJA7t2VmYE01D3enjF_LUqbLLJ3cNdBrBCH4_Q8I9sZTvcxcBtGt_TBpTPtVJuE08EqUULOGDFU8_9aMi9JKL0VbixA9LyjmKYGmDW3yw7f6tIDIPHMwq8Aum52IPPs5TBgxIRbz7PmYM3R7RLTQfAvqmyagMRdzAsUHPE2rCbeu4NQ9xHeTVmyra91SRvDzZ9MI24x6jjuDoCXTAvJyhl3Yr0h8m4u_f9i5PJf009h_x_M9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d560d16c5.mp4?token=FWOGHa_ZKh0rKxsJCYZn7grfIQbtRqIFe_V7SgkJvOBp-c5878Brhcuyv6h6Sq2E0Mgmpl3NALNyBFsfJpwOnTN2ngyTa8bJmiIFCJJA7t2VmYE01D3enjF_LUqbLLJ3cNdBrBCH4_Q8I9sZTvcxcBtGt_TBpTPtVJuE08EqUULOGDFU8_9aMi9JKL0VbixA9LyjmKYGmDW3yw7f6tIDIPHMwq8Aum52IPPs5TBgxIRbz7PmYM3R7RLTQfAvqmyagMRdzAsUHPE2rCbeu4NQ9xHeTVmyra91SRvDzZ9MI24x6jjuDoCXTAvJyhl3Yr0h8m4u_f9i5PJf009h_x_M9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳۵ کشته در تصادف دو اتوبوس در سوریه
🔹
بر اثر برخورد دو اتوبوس مسافربری در یک بزرگراه در مرکز سوریه، دست‌کم ۳۵ نفر کشته و بسیاری دیگر زخمی شدند.
🔹
به گزارش خبرگزاری دولتی سوریه (سانا)، چند بالگرد به محل حادثه اعزام شده‌اند تا مصدومان را برای مداوا به بیمارستان نظامی حمص منتقل کنند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/452458" target="_blank">📅 15:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452457">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8a8ccc7e.mp4?token=G2kQiYH8KwkwXiBRo9ghyxDFL1Gi78OOklKk6taDL5ZPq7FP0LziH0KKw0xGMtT-ddMQg5oSQPhYi6cvguuBSxl4pTPAZloXgZBXtGN8VFMywRTs4tO4bM3ugcs2EKoHdVVdV64cWjF0O3fpsuwiWg2zZ-gmlhCOs1RYd2KgfSPTARRYQBbwRrOjXCYgSRgyVi05rLF8pmgaXxLySHsaQ8_iK99SZJhzK_lrYC--QhllVOAy2HZDAfsAg2AXGULoe4zQA8KjPu4bYqazZ6Jyw0ex9pvLih4HtUmG3rzD0k5vE429l4HhYpJlMkkN0IFDaGlhw49_WH9TRrcZ2MnfdC2DngLjua12X_-s06ox0iBDDgzTzHsQWHiVqo9z5w48cYpMuKbbb2A6XBzL9CK4d-7SWoYADJzSiuFitavGjrgRRWUtIcDyypRF1EZITvY-mNJMVqo9F4XBBS_D5QfK9hlzMOTMZs3QuJhujxkYfQq2AcoJG8EEQEwBWY7L_TLEBVYYUmoHVYdsE9MZeyDKeYxkGGwu6CpVt5vx57U2EKCnoj4qnVf2pG5s2AnbhMAf-24zA0O13sIsNWN2SpKo_hITrt9ErxeYNGuXNxpBJE-LKg-hjU-h0iCQoMQnGPXJEoG2KdCaUR2SRVqqi1WiFPPEFffio28cxg7RZvU9Z_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8a8ccc7e.mp4?token=G2kQiYH8KwkwXiBRo9ghyxDFL1Gi78OOklKk6taDL5ZPq7FP0LziH0KKw0xGMtT-ddMQg5oSQPhYi6cvguuBSxl4pTPAZloXgZBXtGN8VFMywRTs4tO4bM3ugcs2EKoHdVVdV64cWjF0O3fpsuwiWg2zZ-gmlhCOs1RYd2KgfSPTARRYQBbwRrOjXCYgSRgyVi05rLF8pmgaXxLySHsaQ8_iK99SZJhzK_lrYC--QhllVOAy2HZDAfsAg2AXGULoe4zQA8KjPu4bYqazZ6Jyw0ex9pvLih4HtUmG3rzD0k5vE429l4HhYpJlMkkN0IFDaGlhw49_WH9TRrcZ2MnfdC2DngLjua12X_-s06ox0iBDDgzTzHsQWHiVqo9z5w48cYpMuKbbb2A6XBzL9CK4d-7SWoYADJzSiuFitavGjrgRRWUtIcDyypRF1EZITvY-mNJMVqo9F4XBBS_D5QfK9hlzMOTMZs3QuJhujxkYfQq2AcoJG8EEQEwBWY7L_TLEBVYYUmoHVYdsE9MZeyDKeYxkGGwu6CpVt5vx57U2EKCnoj4qnVf2pG5s2AnbhMAf-24zA0O13sIsNWN2SpKo_hITrt9ErxeYNGuXNxpBJE-LKg-hjU-h0iCQoMQnGPXJEoG2KdCaUR2SRVqqi1WiFPPEFffio28cxg7RZvU9Z_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد رهبر شهید در مسیر اربعین
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452457" target="_blank">📅 15:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452456">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c09242037.mp4?token=hqwtYrNvijjHdevhr-9o7poM5_79EtVIo4G8GDJZqjnEIlooTU_dthQbzfK0gdNLIdnm51d0TejgdIMNKoIhKwLNc0cXULzdEfgZIAVj3oMfh7TnfHunpxTf0vu__675OMBrdOvX2nYgDxL7aJhYBNZOEhbXrnuNt_Ha7DZK4lTwf8879ctNN5tuHlAxfrXqqlGdzn58zAMNN4sFHKPA8oP__BysbEiic_A_6pOL0BQkq9pl6trVCOoP2kV69p9GiEPLiauKNu_leteVd70hOd79HhWujOEA1cN7VJYABPcPdZewqVdl7VuPKCwYULYcsLvlRdwUMz9sLM39cbRQnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c09242037.mp4?token=hqwtYrNvijjHdevhr-9o7poM5_79EtVIo4G8GDJZqjnEIlooTU_dthQbzfK0gdNLIdnm51d0TejgdIMNKoIhKwLNc0cXULzdEfgZIAVj3oMfh7TnfHunpxTf0vu__675OMBrdOvX2nYgDxL7aJhYBNZOEhbXrnuNt_Ha7DZK4lTwf8879ctNN5tuHlAxfrXqqlGdzn58zAMNN4sFHKPA8oP__BysbEiic_A_6pOL0BQkq9pl6trVCOoP2kV69p9GiEPLiauKNu_leteVd70hOd79HhWujOEA1cN7VJYABPcPdZewqVdl7VuPKCwYULYcsLvlRdwUMz9sLM39cbRQnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستایی زائران در مرز مهران به ۵ ثانیه رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/452456" target="_blank">📅 14:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452449">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xxl4aSFNTcg9fXi-mV5g2GYpO7F3YM5QmUpyCRj1tFf0VvFiR2UN45nSFZQ_21qzeNxCtknrRW9wkszcWoBJEpqt5_tQ-RIiryktuourK_j0_8CMRC_OOD5l2MwKX8JmEQ_G-bLdyOv01Sir2c0jHwSHxrKTd3PbyzRRj8LcXHCDhxe6QOktOJWc4XT8ksuVyVZxFo4bSyuF-xwO2XZBqE7pZ3rnbNtIG63YwtcMJQrxfs92DpJgK-BCXcFu56LWG46yEGXQMJM48vamNSy2mlbH5p2zA9dSonQDeMe_q9JWbTsyNshVV79mV2Fn4Q_iYeOeKOb8CHAhynBXNd-mpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SqG22Lr-bvyMMOM8KpHy-9clqr7w0BggBLeUl1jxAobtQ03EnjTlcjAT0K4NnYkvQENsbW9o4gxWIHq68C93jNEV0rWphwtB_BLdMkVAoDKizhiFSjLApqCxiKIfcqvRe90DGChjdgesZgcx3Jsm14oH5WMVF1-idDbyqcKipUXotVyPHMSTAR_XZ2i4qbGVY9WsQIa7U-_kfGERU-VjxZTNJaJRd86mDdyPxP4Nx84bytuq--OO62GRe9olGrezRb5dFjAJiSHXeUFAHnLMuHEgOtc9cxeZXG5I5hS3LRUAjTPvRAhCZX_09L7IR9zzXzCxwMTUYksWafG2jH7E6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nws68adCyourqgYvKgW8E-waSIHp2PYR9Aclf7BrKKnXO5iaqgq26FehdOOaxCQLEtd7xWWhpNrP4PuYPf5okHnQOhrcAVrt6ipLSdZ-gGgoEBJhgWC-_1kYnqO9_9cYkcyHTnY8j7GL9FgoLsFe5k5ympccuPU6goSdgyH2k6lZ5_UfUHXZUi8rXOutIqu6TybUJu_sisCvpv4W0qNVTmVDYj2jfkKfCajhGzqPHCNuVOM-I1eF3OnLtVdDf2aUxcrcFubE85PxbxWlItQwz94SfLhAh3Y7ZlVis2jpWpASXNgTWj9YWO_6dQrws5GFXJ7LWldov90-tSRekqXYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcO9XLEfkjR8OKyB_44IMU0TYqeAZoQJX0PjLQuHFGxcbN7oCmR8Fu_1JB8N41bzS4CN70mD8Wt0cx45fMCQA9vR7DT4CeMzMQenTIzB0gPzcDVMGRwmYA96uFUuCepAJBL8llSE3j-00EQ6eEGTOD3QG3sFxS-E21vNFXC4gs0adf24xcDT-_1pjObvo9XqZ4EhTJ8jz4QRYDIPcfdiDYZhByJweinScas_Wjj-LVyBMuAzV0Gq-dtR4_YVgSJGp8Ih9UfAfJnLP7wWSXPGqc5W6PEK6Vu7C7jOoKW5wBV_YTifn2KgUY6OYDw5jhSMiS6h2og44qRcMAU09GaqpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0lQ3CTgyI18VNOIsVtEHbfHeblUvRkPeNT5RWtBJsh_fTyXCsvAEfid2YousQIU8GFgR9A87JATqd69xRQBx3LMrVlCr5FfnxKm-mwkNYIkQ6hiF7TSzKRdI-E5BrI4sM0cgNVxZ4OAK86sLfRekxDDA1qUREdXj2IlF-el5CsA2PozC7FXE-wTXqT2nXXwOnw1FOz2VBqBMB4vHuJQsKsghLAkykPILZthHb41pKE18dwEGgqRjhtmqB5Yx4Vs58LIoE-UXl793pIXDSYaZa8G5aJfKpOGI9yw-BDX80lmOUvNRWBjFf1Tqws54ZmRxD4ny7g5XBIG4tS_SnqELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrvrJPrKfOQhMjE8sCweHep-AtXYcpnCt92g2yVfcvnUM40LFaVwIeNrEPium6W_e2IG2k1epL_KhuvUj-BIcsj4y_AeOzAHMiZeVGUMBc-Cj_90dLJSB0rNiR7h-KNt8z_ckIXtmTptDWEFIFIlpsmWSb-cyrywrJokCCA8KwvBiwMKi33R57H_WiIWhEbN-3AjkDnMVU6Zq8FyNrcNBl0QAFwBKSEz4paxmvU4i8XJ2u5QVm71jmCOXpGai0bJnX-kCG9UTzf--A3FlftZJLugKzInKzQ25A7tYi73iwjK2A3Oi8DicMphI-EKqYF_XD0olpAUrvfQ38Bax2iDSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qpvb1TNntc4Jmpq_TP_BoJlouAcwwYIRIwgSn7OaFGARw94x87RnIEe8KGySI1Hthffz4NJJi1j3-HO4TtYuDKlRu9kO1QcyMKrvS9anh0fi2BdbqPsjT49B52duuOm0ltrX2OpnYxumSRA1tD8K3t4nHLSGvqKPK4qGTO_zelqJ3ji_SKKW90sKcbTZWlKIGmy3GoDuahk80JnPUCmoi62LI1y-TFEwhY8BDyvhWCSsNgwCT0MfwnoKJxF3M1pCIg1pLgfstXwPmUJFMhvRn6kbY5j7MXahzN1yJ6av6fY4drZMJEAUGM7Vomk-H7uYKXIjnkam-mYXY2he6_bIOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تردد زائران حسینی از مرز خسروی
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/452449" target="_blank">📅 14:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452448">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502d70608d.mp4?token=WtFLuUcWSso01RZVXkuu_Fq8ssNMeoJ1QCR4qSQV-tJ36nS-dWec5t7ZhQAJ_b9SvjFPrZk7zUMnQTxsPel6-toeqDmRT2Sv63_MQSREuQjei5gb7OZDX2TeoUTdPhVx2YpCKY0dLZjfYe6Xcu9cSbNFWskDmsar90RjPt-EtCyia8j9rm-iWYyNr5pXAAvTZ0MNjSlITtUuWes0dh6h7NZBLcfe3CmifpZZHNcjVDNuX1Ev9gczBQDj3uF-ptGJr0Tw2bPyVInyjidWzTj5i1nKHRWbGElCUO_ajoyM4XMXhbNkeMdMwcUYENr6dCZvElqo45GuLCHwegq0ifM-zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502d70608d.mp4?token=WtFLuUcWSso01RZVXkuu_Fq8ssNMeoJ1QCR4qSQV-tJ36nS-dWec5t7ZhQAJ_b9SvjFPrZk7zUMnQTxsPel6-toeqDmRT2Sv63_MQSREuQjei5gb7OZDX2TeoUTdPhVx2YpCKY0dLZjfYe6Xcu9cSbNFWskDmsar90RjPt-EtCyia8j9rm-iWYyNr5pXAAvTZ0MNjSlITtUuWes0dh6h7NZBLcfe3CmifpZZHNcjVDNuX1Ev9gczBQDj3uF-ptGJr0Tw2bPyVInyjidWzTj5i1nKHRWbGElCUO_ajoyM4XMXhbNkeMdMwcUYENr6dCZvElqo45GuLCHwegq0ifM-zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرعلی جداوی، دومین جاویدالاثر مدرسهٔ میناب
🔸
علت اینکه تا به الان اسمی از این شهید منتشر نشده بود، درخواست پدر او برای باخبرنشدن مادر باردارش بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/452448" target="_blank">📅 14:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452447">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=btvC-Z5-uUco74mZhoXzCim9LL-DVtMZh4CkWnHLwNw_1r-_HZGDbvS79bV0QI3gIYuVdRWGmkGvSdkje82ArVi0QN91jujTjpOyQzitx3p1xTeRuM5hwoO4EZPzS4ddfQxwdAqAQm6merZTj7ED3tgtzO3zDtMeBTehFpJI3n0LxgxNnjUCT2XD37vxTh-_zg-HDSzR0P1yKGBSU211ppo3a2dP8lL2Avm6IcW2PQUCzaSDwlKUqGcogUNFWGTDnkdOyL3QtHQI4ZbkwZkjL1O9ufy1_Pk-lUt9zVw-wiWYSF05Wqs8X7VfplPTYkH0Eea4j_rjpLsYJ164Z0Dy4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=btvC-Z5-uUco74mZhoXzCim9LL-DVtMZh4CkWnHLwNw_1r-_HZGDbvS79bV0QI3gIYuVdRWGmkGvSdkje82ArVi0QN91jujTjpOyQzitx3p1xTeRuM5hwoO4EZPzS4ddfQxwdAqAQm6merZTj7ED3tgtzO3zDtMeBTehFpJI3n0LxgxNnjUCT2XD37vxTh-_zg-HDSzR0P1yKGBSU211ppo3a2dP8lL2Avm6IcW2PQUCzaSDwlKUqGcogUNFWGTDnkdOyL3QtHQI4ZbkwZkjL1O9ufy1_Pk-lUt9zVw-wiWYSF05Wqs8X7VfplPTYkH0Eea4j_rjpLsYJ164Z0Dy4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بندر جاسک اسلحه‌به‌دست منتظر آمدن نیروهای آمریکایی هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/452447" target="_blank">📅 14:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452446">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmJmldPnBcwx2aqohJMoPC9Xs_CC-_jqoEGwtWoVrmKKkDPp59jP9YcNjHFCcWm0cDuLY-uCTanNRy40V9lQAbYyZzqM_jBpL-3qplqXzsz3gW3TEN-STjuWfQ79aBiL8r17v_g_0c6bI6-MQqWHcIseeh-PJERo8PWaEl_xzgnK1jg91ZDBBraUYss-wXKi7hdGgmmQ2GrP-05LSCoT_ObxtCGfuscx5h2YTN6Mlg5jg7hjbLUMUinBUzDLQ_zro9Q12SX07ZuJ7Lk2-Itj_zyyWwH7sm1X7L9uqgbMP-3CgtrG0sr8PVEd5Ep472g1_o2cLpIDKZxzup6I-QMOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: به کشتی‌های انتقال تسلیحات از ایران به روسیه حمله کردیم
🔹
رئیس‌جمهور اوکراین در گزارش عملیات‌های جدید علیه روسیه مدعی شد: در حملات دوربرد به دریای کاسپین، کشتی‌هایی که در حمل‌ونقل محموله‌های نظامی از ایران استفاده می‌شدند و یک کشتی جنگی، هدف قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/452446" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452445">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhUweGw4_aJU3JBMTScO2RUbs_7pdDVi90q-sdId6jPmkQy1XRuYzpyDCsU51MslHQrdZgdZe0mhgOit6j2cFjcLMwcSYgZos4z9cld_MMuUKtkRGWGU7ISSnL1YRKYDMNhSEO0MclIp_LYwiFz7aqCmFKKhlIKrbP5-pOt9k1QGHwgkFt8fBIr_JvcaBFPhYwCJl3yVmgBnLm8GhkkG6nDaJI9Przx8AE563JyjgzrIYPBl9kzP7FbkM9uaQZP-qTD8kST8xeslb-5_SEwWLAZGzTFvhupMLYcczQ7L1LLIv5LIma5Gcvv9MlinqYmlXILgTWXhzckvs8zvGLYPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بذرپاش: جغرافیای مقاومت زبان حسابداری خودش را دارد
‏کاری که حماقت ترامپ با تجارت جهانی کرد:
🔹
افزایش مسیر ینبع–تایوان: از ۱۹ به ۴۸ روز
🔹
افزایش سوخت هر کشتی: ۱.۶۱ میلیون دلار
🔹
عوارض سوئز: یک میلیون دلار
🔹
جمع مازاد هزینهٔ هر سفر: دست‌کم ۲.۶۱ میلیون دلار (بدون حساب افزایش بیمه و کرایهٔ نفتکش و...)
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/452445" target="_blank">📅 14:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452444">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حملۀ هوایی عربستان سعودی به یمن
🔹
شبکۀ العربیه از حملۀ هوایی عربستان به استان‌های مأرب و الجوف یمن خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/452444" target="_blank">📅 14:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452443">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtHdASrU1aR3mitYTaHTdeLmLeJyDZpROpIw7v6Rv9-B_ayAUb_p5eXUHVG_dewu9lYZB5fuSheT21rW7hZEXIWmQi5TthLMH3hWpbSbjnQ7ofAEkPMOcSjMo1d-GnAeii0w_pmNvLhmV48wDv6J4JQjJplAGT2yjE2GIMmySeNZiuzcmJaDzJKtDdZJ0lP5QJLTHYoOs3YH3G8a2ukaWwycGJw5m-FuVTr9xPLGE7fsXG1VPopEnARN77qgOv4Oa4WQ0Wl83v3rzZ5ai9ifwEWa2Kz8DR24gaLsqxNuMnpayq4pNT96Uvn1-nknAj5Vulinktjxo0q3uV2coSdzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در فکر دور زدن قانون اساسی آمریکا
🔹
درحالی‌که در آمریکا هر فرد فقط ۲ مرتبه می‌تواند رئیس‌جمهور شود اما دوستان ترامپ در واشنگتن نقشۀ جدیدی برای ریاست جمهوری ۳ بارۀ او در سال ۲۰۲۸ در سر دارند، طرحی که در واقع گول زدن مردم و دور زدن قانون آمریکاست.
🔹
«ان‌بی‌سی»…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/452443" target="_blank">📅 14:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452442">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c4603615.mp4?token=A9igX2CxeXEGG1nMPjLzprBHiXOy2nYyF_mwZMYyenIpU46AclyaYYESnrvRHVqJScyIqQn2tU6UXiwSVc0DMOg1_BPyF1O_nwxHDOLuZdiRlsLgyWECuQsuLDJQPK6Hn4nF2Rvjj_yzraXiL6gpH5ySIq6ETfJF2I6tNPYOBW0MWlJy44XfBx8krQcmsFHea6gOEavW22eppeeZWxBLkHDzvBeCenryW9ui1XP1bLFEEUgXHHRZ_QD_hWP66WDJOxP8X3F_eRa7wLD7kresY8_zlWCSO0m-ezSS8qWpg9boCgNt_FPk6RGvqmsoOMiAx_TfzMtynyrw6XwEi8KZg1C8OQpI0JEq0T3KnfQeq_RljrLXZzAE65ol_DYl62ZNH3--Qy43mZqrF8yKlbMgqgN77RK0cU5vAgMS4H2YEKMenk-DgBGNeBGjSYb8Kerlz7_Q-uk5xf6n2eba3DU1Obkd79ZqVU2-D3j_ClzRHiTLnI6gFkiVKvgdPRW0_acJDT7zK-HsSWW6Dc5NmmIHvQJWjFW3pqSxTIMwoIPWnFvZuP1T4aQpqdl9qzG-NhnSjyv4cwsLTPfUs_fgqGdPL1eser59q86coF7z5WZeYvlChw3AndsXlbAZ8hQ1EZUzrts4DjQrLQNOkAzrm_fVrFz9mQgkj7VeUT_Sj5OBdhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c4603615.mp4?token=A9igX2CxeXEGG1nMPjLzprBHiXOy2nYyF_mwZMYyenIpU46AclyaYYESnrvRHVqJScyIqQn2tU6UXiwSVc0DMOg1_BPyF1O_nwxHDOLuZdiRlsLgyWECuQsuLDJQPK6Hn4nF2Rvjj_yzraXiL6gpH5ySIq6ETfJF2I6tNPYOBW0MWlJy44XfBx8krQcmsFHea6gOEavW22eppeeZWxBLkHDzvBeCenryW9ui1XP1bLFEEUgXHHRZ_QD_hWP66WDJOxP8X3F_eRa7wLD7kresY8_zlWCSO0m-ezSS8qWpg9boCgNt_FPk6RGvqmsoOMiAx_TfzMtynyrw6XwEi8KZg1C8OQpI0JEq0T3KnfQeq_RljrLXZzAE65ol_DYl62ZNH3--Qy43mZqrF8yKlbMgqgN77RK0cU5vAgMS4H2YEKMenk-DgBGNeBGjSYb8Kerlz7_Q-uk5xf6n2eba3DU1Obkd79ZqVU2-D3j_ClzRHiTLnI6gFkiVKvgdPRW0_acJDT7zK-HsSWW6Dc5NmmIHvQJWjFW3pqSxTIMwoIPWnFvZuP1T4aQpqdl9qzG-NhnSjyv4cwsLTPfUs_fgqGdPL1eser59q86coF7z5WZeYvlChw3AndsXlbAZ8hQ1EZUzrts4DjQrLQNOkAzrm_fVrFz9mQgkj7VeUT_Sj5OBdhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد روان زائران اربعین در مرز شلمچه  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/452442" target="_blank">📅 13:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452441">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af7pgKMVsCsmekK5vALuR65RHNnSDWcEGTQuTTgPl05_lBPlc9oTkEvl-eqzPKMVDmG-ClkHn3evpUymXPR5l0__0XWIBqJOrr4JACDcByX7SiCVAktiI1A6cIekDdt9hV2f-MbPNLF0zdbD4qfBBNl-YkgeNTQ60JueUyr94BBtoxjmkIyrz1Cvv7fK9gIwx9EOb3bl-q42vjqcHtVC_HFYIh46Ff8HZnfN6YOrfGEpinTvXOrnIxlIWYjPTnGX6w17TIwq8YJSRwa3wC9nf6ebRhh2FIr69W23YOgoQOJ3n5vNLo7ZedwLCPM_T5RzvrR9bKQ3zOKVcupyGqB1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی: شلیک‌های مداوم رزمندگان ما، تا تسلیم کامل دشمن و گرفتن انتقام خون کودکان مظلوم میناب و لامرد ادامه خواهد داشت
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/452441" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452440">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjVFdGUTeP_Ogp7-zwT-De48t374XMxutzfzAlvBOFZ3HmpZT7tjvmeMB1lWqT-Wt5z4gnTUCeXfaTQ5-ZXlRDCDFGtwwWPCqfCrEuitKD7OTXICCKKFlFewrqkPo5kh_oVmdqjuw3NYWo7D6jcrRgzNj22m1paouCTQSStLK5f9X5qClsmL0tH4F_v-Jm8gepn39KrsPx-UQObNXKXkoJ5vDjyt9D0VDTs4Tsc_SLmkmz2yLdvMNQB-Gd3Wi2pedjM_Q44tf61gZWMqq4hkX97MTho44vTQnRus7XhXbYc12vdBP8UuEYw4z8bPDcjgAyqS-QhnTfXFJD_QHB7vpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انیمیشن «سفینه نجات» در راه سینماها
محصول جدید سینمای انیمیشن ایران
«سفینه نجات» تازه‌ترین انیمیشن سینمای ایران به کارگردانی هادی محمدیان و تهیه‌کنندگی محمدامین همدانی پس از ۲ونیم سال تولید در سکوت خبری به زودی توسط پخش بهمن سبز در ایران اکران عمومی می‌شود.
محمدیان پیش از این کارگردانی انیمیشن‌های «فیلشاه»، «شاهزاده روم» و «بچه زرنگ» را برعهده داشته و همچنین محمدامین همدانی با انيميشن‌ «پسر دلفینی ١و٢» شناخته شده که فروش ۵ میلیون دلاری و جذب ۳ میلیون مخاطب را در جهان رقم زده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/452440" target="_blank">📅 13:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452439">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-text">🔸
مجمع مس ایران به روایت رسانه‌ها | ۷
🔰
مس ایران، در مدار آینده
🔻
مجمع عمومی فوق‌العاده و عادی سالیانه شرکت ملی صنایع مس ایران چهارشنبه ۳۱ تیرماه در مرکز همایش‌های بین‌المللی صداوسیما برگزار شد.
گزارش گردهمایی سالیانه سهامداران «فملی» را از نگاه تلویزیون اینترنتی «معدن‌شو» ببینید.
#در_مدار_آینده
#مس_ایران
#فملی
@mespress_ir</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/452439" target="_blank">📅 13:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452438">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/452438" target="_blank">📅 13:26 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
