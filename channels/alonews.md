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
<img src="https://cdn4.telesco.pe/file/uuaO_30NAUJFOZne5QEs6BFqWzcpVW1cDLkuBzsJ7iKzdEsDSeTpvyVvolx1fevRsMWz-rDvUz5Fbnj7anr_OTt7_CUx3lADW6w34HDrdEmjiPFo58uKp9UyAYFbcIP23whoSQlYezdEwxW35pjI5t1naZKG7ltae7-w2h_8ShvYkhmhRe35V7QhD8yn6AfwO0hQ8xEt3ZMaa341qh2L4D5L6Vjq7WQo-I30LoQxCjL0kKqKp3sDDdw7cJhDAwSSX_s_hgXTGmZR0YgjDta6xbCSwRBTfBZbrTMo2v2mdSisN1B8n9Q-p0qQjLOTvNrYgV0Dbd64PxWE1aFiWs7wgg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 22:44:37</div>
<hr>

<div class="tg-post" id="msg-151335">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
هیمتی: بسنت اعلام کرد تا دو هفته دیگر ایران فروپاشی اقتصادی می شود؛ ده روز از این دو هفته گذشت و اتفاقی نیافتاد
🔴
من گفتم میلیارد ها دلار خریدیم و دپو کردیم حالا فکر کرده اند ما رفتیم از فردوسی دلار خریدیم؛ منظور من چیز دیگری بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/151335" target="_blank">📅 22:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151334">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فاکس نیوز»: ناو هواپیمابر «بوش» خاورمیانه را ترک می‌کند و تنها ناو هواپیمابر «جورج واشینگتن» در منطقه خواهد ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/151334" target="_blank">📅 22:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151333">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
تحلیلگر صداوسیما: آمریکا چون دزدی می‌کنه دلارش بی‌برکته و به همین خاطر مردمش گرسنه هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/151333" target="_blank">📅 22:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151332">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه اینجا رو بخون تا از بازار جا نمونی
👇
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/151332" target="_blank">📅 22:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151331">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
فارس: جنگنده‌های آمریکایی در چند روز گذشته چند بار تا نزدیک مرزهای ایران آمدند مانور انجام دادند و برگشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/151331" target="_blank">📅 22:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151330">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=q8wc51_Q2_Cj6P9f_wO8xwQplgjxgzeYihGEwJs6VITjQjzW0NkOM64xdCKb94jh9UCSk3lV88Jrm36jPrCgqLZr5wW4bzdixmHpro8ajwALWay628rWCpEkgy7c3mcVsH8Th7KNHpaU5dRpWehbZ1D8ZmzsEhOvBnA9_YKrWCslnw1PJsKb74CoTetmkkX60i596feEhKtgcZ2ATxcDCZokdqmedujPy1FXpb4ic9EnO4iihiVaNJ-CJ1512BDQ5l_ljbt5fwqaFfBlEKUyd2Lv9QDVO7i8-KP1Jx8zWURfzaM724_eKO_-XOOu6APYgLIn38c5Qt5vJ3bjFkwy0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=q8wc51_Q2_Cj6P9f_wO8xwQplgjxgzeYihGEwJs6VITjQjzW0NkOM64xdCKb94jh9UCSk3lV88Jrm36jPrCgqLZr5wW4bzdixmHpro8ajwALWay628rWCpEkgy7c3mcVsH8Th7KNHpaU5dRpWehbZ1D8ZmzsEhOvBnA9_YKrWCslnw1PJsKb74CoTetmkkX60i596feEhKtgcZ2ATxcDCZokdqmedujPy1FXpb4ic9EnO4iihiVaNJ-CJ1512BDQ5l_ljbt5fwqaFfBlEKUyd2Lv9QDVO7i8-KP1Jx8zWURfzaM724_eKO_-XOOu6APYgLIn38c5Qt5vJ3bjFkwy0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل هوادارای لیونل مسی برای خداحافظی در آستانه آخرین بازی این بازیکن برای آرژانتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/151330" target="_blank">📅 21:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151329">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
فکت : آخرین باری که روسا گفتن وضعیت تحت کنترله، ۴۸ ساعت بعدش کل اروپا درگیر تشعشات هسته‌ای شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/151329" target="_blank">📅 21:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151328">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
عمان: یک کشتی در مسندم هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/151328" target="_blank">📅 21:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151327">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
الجزیره: در پی گسترش اعتراضات دانش‌آموزان، دولت فرانسه مدارس را تا آخر هفته تعطیل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/151327" target="_blank">📅 21:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151326">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ثابتی: رسایی جز افراد بزرگ تاریخ ایرانه حقیقت رو گفت و روی حرفاش ایستاد و رفت زندون به خاطرش
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/151326" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151325">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
شرکت ایران خودرو مجددا درخواست افزایش قیمت 40 درصدی تمام زباله های خودش رو به دولت ارائه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151325" target="_blank">📅 21:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151324">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
گزارش دو انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/151324" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151322">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLOdP8NKkEnGaVAByKoMuZRn04Yydrwv0IbesUpauOnVujVbDxeIP0FHlE2ok8Q_-bEbkXVTtky130clZmjqMpsB4yX6e0z6r6SjI-c5FZUBgJ42ANXdBIWOXzW6hwH359RBOKTNsX_-s4s2VQTa4db_sT3xKSPJlIKV8EM50AjybKpzqlaVfrgkNGcjKXxjvs-N0t-OpQfbZu8DhRBmLCpgo37vkQvimRwO1035fMaZmQgw6jNv2J3ZVvAR1fikWGXtuX31C7zwY8CtEjQofujptlnVU8DxcBNBc8RGK-PHdy1W9fUaqlA-S3Lv1RiJoVjK8htSCtwGWT565d--yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bN5GTw3i5POCrt09OpxkFz0gRo50BWjfUgu7yT8vTxyntlpPZSGjFWrzC0ohKsllyHE7JaLnAHX3h35b4I2yZk3WCJYhsUIfhXjodxRJL1aagfr1cWbO1L7te2uzWnrOqSIcdqDvgkAk5L6vssITQmuHLHcsCUUs-ux1qUeiZrTps2E5jdXvrFXsU-TcZBz8GQV8FBYM5fU6OTWDYJzFTfqTDD6lA8cTza5jGp6JNdEu4Ztzr3nT6QMWmxqApwazHJz_4ypGfPnmBlSBTi8CC8r002jzqmRadeB7D5KETtH6zQBFIASN9DAyBjzhquujkK0k2vIorF2ZlM01013zTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدیدی از ستون‌های دود برخاسته از تأسیسات آرامکو در روز گذشته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/151322" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151321">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری / روزنامه عبری «معاریو»: برآوردهای قطعی نظامی حاکی از آن است که اسرائیل در آستانه انجام یک عملیات نظامی در یکی از جبهه‌های منطقه قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151321" target="_blank">📅 20:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151320">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فاینشنال تایمز: مذاکرات ایران و آمریکا پشت پرده ادامه دارد
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151320" target="_blank">📅 20:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151319">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
مرگ مشکوک در آزمایشگاه ایرکوتسک روسیه؛ آمریکا از احتمال بروز طاعون ریوی ابراز نگرانی کرد
🔴
وزارت خارجه ایالات متحده: گزارش‌ها را با دقت زیر نظر داریم
🔴
مسکو اطلاعات دقیق را «سریع و شفاف» منتشر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151319" target="_blank">📅 20:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151318">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
الجزیره: رهبران دموکرات، شوخی ترامپ درباره اجازه دادن به ایران برای بمباران لس‌آنجلس و سن‌دیگو را محکوم کردند
🔴
آن‌ها رئیس‌جمهور آمریکا را «آشفته و خطرناک» توصیف کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151318" target="_blank">📅 20:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151317">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTaawvfS0gbeDa_wYkr87v_Kd8OlM0R_KuIlOViyRwnkobU9eM3crkJD5HJOerXkHpl5j2MFgZ0Mx_lM1sMIMEqSgN4v4hqD6KREApmpH8M1gfsNbjFoYpSZhdqC0DC75E6hmGmIe7AR9qr-oNrlCxs_5ile1_qCanq7W-cLKBNcgZIbS5SK2lIHw5twC3moh8NSrLH2D8BSur0VBgWc8vVrLa-2UZGi70iWGevW3hDcV0mWkiQaBaz889F2WZ-S2G-OKe4IUhRoaF3k5vNoTg3djWPsOOraTAjNpUgo8dR-97xdL3TeKm_JYy3B9GIl3VZwQy9md_UihzRgOAnboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تردد پروازها در فرودگاه القریات عربستان سعودی، در نزدیکی مرز اردن، متوقف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151317" target="_blank">📅 20:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151316">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ریانووستی: یوری اوشاکوف، دستیار رئیس‌ جمهور روسیه اعلام کرد که ولادیمیر پوتین، رئیس‌جمهور این کشور در جریان سفر خود به ترکمنستان برای شرکت در نشست سران کشورهای مستقل مشترک‌المنافع، روز جمعه نهم اکتبر با مسعود پزشکیان همتای ایرانی خود به‌صورت دوجانبه دیدار خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151316" target="_blank">📅 20:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151315">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
شلیک موشک به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151315" target="_blank">📅 20:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151314">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
یک مقام قطری: مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد و پیام‌ هایی بین واشنگتن و تهران رد و بدل می‌شود و قطر نقش میانجی را ایفا می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151314" target="_blank">📅 19:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151313">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رایتل رسما اعلام ورشکستگی کرد و سهام خودشو به مبلغ 130 همت در مزایده قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151313" target="_blank">📅 19:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151312">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزیر کشور برای انتقال پیام امیر قطر به پزشکیان عازم تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151312" target="_blank">📅 19:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151310">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=fTSj2FdB4qn3ftXzDPAIjzlKT4GONe0aFs-ZI-lVUEOMZcfizMOSu888HqYXstai7mf_igTyYzq1d2gB9_JxC0hxEbbv0UOzzHuufNw7rCf_M5Dlx868WJrWmFL1V2lBMIG_MnOog5lExRIZKt7tBjBf9RkLA_qSbiDce6-LRy6bsrgto6pvz1XY9BFgg1cQ6RVg-1dFf2Nnqf0q35vSg0SdAWykTyXjoKXnGQuMmQhfUPnSovpN0Q0_o5FOIAwYzdQ1SaQnbZgssN8Ylkov4TI69b5Up68VkVAk1lLjyvQ8sRKwayCNHE5seUfYKyhdoirR0coX_7AwI7TOwd5mSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=fTSj2FdB4qn3ftXzDPAIjzlKT4GONe0aFs-ZI-lVUEOMZcfizMOSu888HqYXstai7mf_igTyYzq1d2gB9_JxC0hxEbbv0UOzzHuufNw7rCf_M5Dlx868WJrWmFL1V2lBMIG_MnOog5lExRIZKt7tBjBf9RkLA_qSbiDce6-LRy6bsrgto6pvz1XY9BFgg1cQ6RVg-1dFf2Nnqf0q35vSg0SdAWykTyXjoKXnGQuMmQhfUPnSovpN0Q0_o5FOIAwYzdQ1SaQnbZgssN8Ylkov4TI69b5Up68VkVAk1lLjyvQ8sRKwayCNHE5seUfYKyhdoirR0coX_7AwI7TOwd5mSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدون شک این عجیب‌ترین پرونده فساد توی تاریخ ورزش کشوره!
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/151310" target="_blank">📅 19:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151308">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad6fe8b02.mp4?token=CS5a0K4v01_wFX6Yz5Yzd37SjgKXSNu96fVMOeGBr0wcYYCSZ3CA0wAfqrHLjFgQGtF0G2A1M7bfxmCl0pHGz4-dT-nn5zLTjvbasFc4KYUiGTgPpEHXTS4uojEOnOebioh4yY9ZbOekkKhOuVredi0EdeoOGsr95HCFdm0A-SAO7TX2cH20TEiYinIQuX7ST3-yXcPFOMGdCdguHWI-vVhFbslXOVuO7NFnyeOeA_M8X85FRXA_zy7hIHS8QLEqtz0Xg0uXhvQfbFQfcwdaS5CVtzUfa0cUY2aKv37Q7ADGkduA-ivanTOLigMkXFeVnQTH3o8fAqQTWI4hFlHcGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad6fe8b02.mp4?token=CS5a0K4v01_wFX6Yz5Yzd37SjgKXSNu96fVMOeGBr0wcYYCSZ3CA0wAfqrHLjFgQGtF0G2A1M7bfxmCl0pHGz4-dT-nn5zLTjvbasFc4KYUiGTgPpEHXTS4uojEOnOebioh4yY9ZbOekkKhOuVredi0EdeoOGsr95HCFdm0A-SAO7TX2cH20TEiYinIQuX7ST3-yXcPFOMGdCdguHWI-vVhFbslXOVuO7NFnyeOeA_M8X85FRXA_zy7hIHS8QLEqtz0Xg0uXhvQfbFQfcwdaS5CVtzUfa0cUY2aKv37Q7ADGkduA-ivanTOLigMkXFeVnQTH3o8fAqQTWI4hFlHcGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گروه حامی حمید رسایی، سران نظام رو تهدید کرده و این‌بار گفته‌ «کاری نکنید مهرآباد را برایتان ناامن کنیم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151308" target="_blank">📅 19:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151306">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏
👈
پاکستان: خبر استقرار ۳۰ تا ۴۰ هزار نیروی نظامی ما در عربستان، ساختگی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151306" target="_blank">📅 19:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151303">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZi4IVFZgJDAHSzddQ6v2EKo1dKpsmkSBbraRPR8bB3ey2E_aqHXTKdMRmTStsN2LLZeD3KyeuHFXSWlLzhTD_eb0i1LwPROG9ieS6v0UNyUfOeTNR544aMTpYNH6613Ci9rpcnjmAQN56iytH95gX7DrbQkFttK25H6qlCv05TeMuS0xxuFwOL6l2xXP8XYWiTbUzNoNKZTeVWVVW9exywTGRZtxpDztaf6t5u21iX7jVZXgXwe5lMnI79eVdjEymW14uA_OXbRQpbi9CWP3tW0k8zpA2wqIoQozTIArjSp9SFxzHD6Hsu8q8e1KbVOb7a4kVFt_57hJNUKTOgUsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZI93l5R3L0lt4ASH-xc3-Q6p3ReL7suT-Xgbmlpbe7XavSDbp2CXmD72MlAkCso9eFOwseLcHslO9vAlZh1cI-kie9ZZiLHcMgl3X2ILTxvabfoqhxH_nl_iSBEYMxXs8Y8fio3vw2yoMZojVqRsY4bcokAkTWMAO_5EHsIZ2vCFQz90Vtzyiog56WCfRgOSBK9jU96LXa7mwjQLMHGiKU4m7LNPC-DxNEnBFkIUACERum14xQIDPoyfHoi7J0GNXoKfJoVXHhm3J4zwUC7bPMqM1U7xaYVYohYQj3A-c2NhqSFQPr-hdNO42CgNhuyqCJMKbhm4lsNVr_vO5KZ_qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5c69c2aaa.mp4?token=TR1whVBWsHQSSNZk2VeLOcG2Ez9wcyL94w0HHDsY-uSDpwhkg9uGPNrlkMCxt5nzH7q4pe-phS_dCYHlhfMI1eq85FGC9Szus74CqVNJG_W_9loNl3VNh1e8X7v89AUU31D6hGoSwB3Fk95vuj3DqEpLwwPGq4UUkesegXw0Lx3Dc3HnYQH9XpY3ay8pKRVF78qybwf0os4p_a8B5nmpwqvtf77xl0shxgr63KFQCR-76nPuxvTKE0QugQtbx4UGtL-mQbrRLYQ5rnosMzFwnqpZyL28eEqy3K0Oj35Qj_P3XiWuf8G8FUkPpmiomUjt4CYt7vJfMqp2W_smoITZRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5c69c2aaa.mp4?token=TR1whVBWsHQSSNZk2VeLOcG2Ez9wcyL94w0HHDsY-uSDpwhkg9uGPNrlkMCxt5nzH7q4pe-phS_dCYHlhfMI1eq85FGC9Szus74CqVNJG_W_9loNl3VNh1e8X7v89AUU31D6hGoSwB3Fk95vuj3DqEpLwwPGq4UUkesegXw0Lx3Dc3HnYQH9XpY3ay8pKRVF78qybwf0os4p_a8B5nmpwqvtf77xl0shxgr63KFQCR-76nPuxvTKE0QugQtbx4UGtL-mQbrRLYQ5rnosMzFwnqpZyL28eEqy3K0Oj35Qj_P3XiWuf8G8FUkPpmiomUjt4CYt7vJfMqp2W_smoITZRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم و تصاویری از بمباران توپخانه اسرائیل که بیت یاحون را در جنوب لبنان هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151303" target="_blank">📅 19:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151298">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8Tj8koKC0Gycq4BZaRtnqBVAwwWQxFZJWeFWmbdz8uUixgabVxZRatHj2tBRisBDo5igpinpU7AEGm3L4aqnKYAqFhL5uZdDk4kxfoQ83ywTi2dI0qf_Ck-UXkY9LbmwMXofLm2A6USLWN-WRZSbU42MxpCqiRRhDJWIBjQTirPOjgnHja0r1f_SKlM78nrJa-1-31kI18E_yQS9djTrpBVDmqTNPeUdNbuAspuhJb2nZkL5Y_cao6knzFx_BonHocSeyz702kgP4Mr09rOAd6cdFcsMSWd5XHHEX5KAYSfFexTQeeAAHvSRmI3yOPToj77p9NxrWRss0cY-_jMzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درمورد اتفاقات فرانسه:
آنچه در فرانسه در حال رخ دادن است چیزی کمتر از مهاجرت انبوه و خارج از کنترل نیست. این موضوع درباره مدارس نیست؛ این درباره اسلام است که می‌خواهد کشوری را که زمانی بزرگ بود تسخیر کند! رئیس‌جمهور دی‌جی‌تی
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/151298" target="_blank">📅 19:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151297">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
شورای امنیت ملی اسرائیل به اسرائیلی‌ها هشدار داده است که ممکن است فردا، در سالگرد ۷ اکتبر، مورد حملاتی در خارج قرار گیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151297" target="_blank">📅 18:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151296">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZciWHD_dQN9zPccC62vwYBLUgC9sfmCB-_Il6qNuFr89FCo-1Zc5mS_0VlPmRQK1T7YWWaD_VS-edveXwRUoYWn6H4BX2Nml7yf-dy3llBXdvVRZcsk1OuyX-jbfo6teUraeA3QCttjMT8HNOC-whGYMJ73e0PsLqp2d3wxl4SXIxfKo_XfG0fxjS-LyZo4jfani4823QUn7OWBmaYnCfo5pV_075A8mz6F8jyFjzrFc--pARWSkm6G4VruPROuUSldk5m-IkkEqJrbYZ2g-Z5CK3kw2jphBhWAYvVE32L4IxUm8Ro2yhVGhx3uIa3F-aizpZWspS4YFkGuxq690Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طاعون روسی دومین کشته خودشو ثبت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/151296" target="_blank">📅 18:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151295">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14d58e2d38.mp4?token=WW_nLL2Xp2_a3_4Ebxh28QqLWPY8kY4RivVbpSWAm11NycfGQzNVcgwSgp77V5syEXfBypG5jGaGpdgBI78AHPbuGJD81nd90FgiKVghGI_gu9jqb_cunCCo4dpyUAb6zTVHOWURSyooz0FjMeUm_4G5ovawCID_dXuE8rcqpxpIUMDbRuNEaZJqUvDnezszeDaiTerMuFdUKyaabZcE5Nazsylln602ajsXgVAEjLy8KPslFKbDt1pUOn4EjWfvcJnAsIR834WOtVHget1NMkRJGdwTbHK80wPrIO90Z9w5_oKCp_f7frqdhUYPIX59RRtEzrSLMRQI5QUoUuTAZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14d58e2d38.mp4?token=WW_nLL2Xp2_a3_4Ebxh28QqLWPY8kY4RivVbpSWAm11NycfGQzNVcgwSgp77V5syEXfBypG5jGaGpdgBI78AHPbuGJD81nd90FgiKVghGI_gu9jqb_cunCCo4dpyUAb6zTVHOWURSyooz0FjMeUm_4G5ovawCID_dXuE8rcqpxpIUMDbRuNEaZJqUvDnezszeDaiTerMuFdUKyaabZcE5Nazsylln602ajsXgVAEjLy8KPslFKbDt1pUOn4EjWfvcJnAsIR834WOtVHget1NMkRJGdwTbHK80wPrIO90Z9w5_oKCp_f7frqdhUYPIX59RRtEzrSLMRQI5QUoUuTAZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت عجیب آرامکو
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151295" target="_blank">📅 18:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151294">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رویترز: پالایشگاه‌های مستقل چین با کاهش شدید عرضه نفت ایران، خرید نفت از عراق و قطر را افزایش داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151294" target="_blank">📅 18:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151293">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
مدیرعامل آرامکو: تا تنگۀ هرمز باز نشود، فشار بر بازار نفت ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/151293" target="_blank">📅 18:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151292">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLb70JhNIRf8gwu8C28t2HJCob_DdNpBl0ZdgGZDGZbZyLTeRMvdIb_78Cil0HcurP0UfrK5lQVy7ojAinSo0yupe3Gy7wPr4N77GxKnaHmq9lO2eyPAvGNQUs1qWQhq_5E_keBwNORI_uh-4JY1BNu1uaLS21qYkn2AxVB-YUzlR01VfUB0Q6iAY3aB8jfpw7CXPxysAhHxmBxnxX8fb57xFfbGZPpU8QBJfDcvY6yL1JWaHrIqJ6X83i22vF8Bwvn335FQ9-RYdAS-44kgOxXTrLPL5Od8aa8lnRghq1ioBvr0P9BHVscPYsLiXDQZ1jUAOQbyl5Kbv-NRaFZmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق تروث سوشال:
گردهمایی‌های من بار دیگر حزب جمهوری‌خواه را نجات می‌دهند!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/151292" target="_blank">📅 17:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151291">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏
👈
ایران سفیر فرانسه رو بخاطر سرکوب اعتراضات در فرانسه احضار کرد
😂
😂
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/151291" target="_blank">📅 17:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151290">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d4fc5eba.mp4?token=haehAV77ciDz-2vbzlJtXJKZbvNRJE0LRrE9SBBFuNhTM8HyX2U4QJ66oNymDe0u6wyuszit3BePbEJl1JVho7FOOIUOrRGNOFjzXIRIlCxhilGTsL88Cc0wE61zHKhe5syGUkPJLSAPRl5mPeyCSq1iMxXjiyBxwkrxEwPAtVaVU0jzfraA6d2J-KJBb-FAk1MrgYE0gUI2L_DNtkVVaSKQLg7cx4cUfOTi4WFzbb_JHyBEjEt9nyX-t-OswJXSs48y6Rf40GFPFwyPmUkcNXLk7AQN303FRqYQgjUrv0t4Bb4XjKBgnrmUGrZvMUqhBtGqtNJ_StZstzIBXn_aJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d4fc5eba.mp4?token=haehAV77ciDz-2vbzlJtXJKZbvNRJE0LRrE9SBBFuNhTM8HyX2U4QJ66oNymDe0u6wyuszit3BePbEJl1JVho7FOOIUOrRGNOFjzXIRIlCxhilGTsL88Cc0wE61zHKhe5syGUkPJLSAPRl5mPeyCSq1iMxXjiyBxwkrxEwPAtVaVU0jzfraA6d2J-KJBb-FAk1MrgYE0gUI2L_DNtkVVaSKQLg7cx4cUfOTi4WFzbb_JHyBEjEt9nyX-t-OswJXSs48y6Rf40GFPFwyPmUkcNXLk7AQN303FRqYQgjUrv0t4Bb4XjKBgnrmUGrZvMUqhBtGqtNJ_StZstzIBXn_aJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه آخوند تو تجمعات شبانه :
یکی داشت رد میشد گفت حاجی پرچمت خیلی بزرگ نیست؟ گفتم از این به بعد تاکید رو چوبِ پرچمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/151290" target="_blank">📅 17:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151288">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
یک پزشک تو فضای مجازی : اگه طاعون تو ایران شیوع پیدا کنه، تعداد کشته ها تو ایران خیلی زیاد خواهد بود چون مردم ما علاقه زیادی به مصرف آنتی بیوتیک دارن و از گذشته به خاطر سرماخوردگی آنتی بیوتیک مصرف کردن و الان بدنشون نسبت به آنتی بیوتیک مقاوم شده و اگه خدایی نکرده به طاعون مبتلا بشن دارو دیگه روشون جواب نمیده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/151288" target="_blank">📅 17:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151287">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏
👈
دستگیری سارق تلفن همراه سیاوش طهمورث
‏
🔴
سارق سابقه‌دار: معتادم، کسی به من کار نمی‌دهد!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/151287" target="_blank">📅 17:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151286">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
گوترش دبیرکل سازمان ملل متحد: خیلی نگران جنگم از آمریکا و ایران میخوام خیلی سریع دیپلماسی بازگردند و به جنگ پایان دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151286" target="_blank">📅 17:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151285">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64f2b181f4.mp4?token=ZAM_8b3tS9LutO_onoBmp2BjQ1XI4DlQ5mzpRjZ7oaSW-fwIn6_Ja8iwJlJzox9fljVbZ0TkTwbLyTNdFi7sViNyDEqETYjfLFQJ8vtzHC6Ro9Zp1DLfS33pYd1LW23GHNnCnaoW2vHzHzJptr0LCpb9nRJjDX7xNxg6fUzWpTwHrhtLDkvoC7Io6CuyaOWf6pMWtuA4RyINYwiw1PrRWhAnvYNrp2ZxCwiE2Yp1sOMZAVzB3ijOTeigZLjV-NR-tjnoCQzvFFtRnoKyIGZR3aBVioROaZCTr92EcIMeKONVOAMaaLFVgQBY38djkrFMKpDbuSWT5twa0DCjN0Vcjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64f2b181f4.mp4?token=ZAM_8b3tS9LutO_onoBmp2BjQ1XI4DlQ5mzpRjZ7oaSW-fwIn6_Ja8iwJlJzox9fljVbZ0TkTwbLyTNdFi7sViNyDEqETYjfLFQJ8vtzHC6Ro9Zp1DLfS33pYd1LW23GHNnCnaoW2vHzHzJptr0LCpb9nRJjDX7xNxg6fUzWpTwHrhtLDkvoC7Io6CuyaOWf6pMWtuA4RyINYwiw1PrRWhAnvYNrp2ZxCwiE2Yp1sOMZAVzB3ijOTeigZLjV-NR-tjnoCQzvFFtRnoKyIGZR3aBVioROaZCTr92EcIMeKONVOAMaaLFVgQBY38djkrFMKpDbuSWT5twa0DCjN0Vcjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی به ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/151285" target="_blank">📅 16:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151284">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی به آمریکا:
شما در جنگ نظامی شکست خوردید و در جنگ اقتصادی نیز شکست خواهید خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/151284" target="_blank">📅 16:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151283">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDWUUxjP2cHXmRhocMWFrXWl4Ulg_eBDpdwB0njqdJDgTrql3-up9VyrfwX_f7rM37c8fHLQBoc9681s2ag1luqmcGnXyYxBQ90uECxLw53G6kB3jogBRnucKJdggrnQgEKMoCCUYP_UQOozUhokrjiEx6zBzTFkIiZ6ak-ANBss7ierY6h9FJX04lbRDji3-tRlQDrGEJKkJlK46A3XGXFUdT0LplYwx8zOw8vddSEFlu_1K3zhSUUuMIqzCt-zRK67FpiRH2psOm0yvgvpl3RlhhIWwywVbcNuSjg7BnfhEk9-tWCKHrxzx88nN2Kc-F0MCann7llITyD50DEJdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: گزارش ها مبنی بر سقوط یکی از هلیکوپترهای ما دیشب در دریای سرخ نادرست است. نیروهای ما در خاورمیانه در امنیت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/151283" target="_blank">📅 16:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151282">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJXtr_LqaonnANHb-yF-NL1AWo65YqcX5T71FC7FQZrtkqclQ0-hEIfl9fggdsmOb35m4NQ3USQT8YG45mlRYzyPZnzEQOTlMVfIhU04xhVS3EOQ98M42Kyw4GnqdW8GYFcRmCxL9HcqOlCPOqr_OFzv8dLX3RQ6QyJ3DKRI5n4qSqC3u5qbOfOVj5Cm6znAktoAnPtWomp18sfdDLo9a3zZms2D5S4eVYwNgZxe-znxmRTXDEusufobBrPWwYaarZeieBnrAYfV1jL-YXN9IPUtyHM1q1hPAvuHRHlqODt8RGPWxFof7ZwwUr62Km38iNzt5sxOIGDJm0rPZAsFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت هم‌اکنون ۹۷ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151282" target="_blank">📅 16:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151281">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24468a4f6c.mp4?token=hcXk320HXxHf1VDCAcCbJerGEIh-Ao7CU5RG8iBful4h6O9UIvDe4VbY_KnOadmorsybFF8ITynv-UVIOBaKutAwihLXIE3piTcbseDiyouK1A5m4PAisU1EXgDyoITB1LbHxtakQQzhbWGf9jTDDDx8jy2mPBbPylDkXivtMF3T1YB38bXy_p5IDH9m2A5TFM8qZlE5tOarO8wMgqFXx3AIMlhjG0maDLaGDXDlAU6QUIyqXpFd7yYYOyViKvxk_ti4Jmhbw9BjgnrKIAp_NQnC1_zPCDcOPwstBzi8J-gHJ8cRcVWzNDKHPxgEnmfRqNFlqNWUgVeO32Y1Zpt4ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24468a4f6c.mp4?token=hcXk320HXxHf1VDCAcCbJerGEIh-Ao7CU5RG8iBful4h6O9UIvDe4VbY_KnOadmorsybFF8ITynv-UVIOBaKutAwihLXIE3piTcbseDiyouK1A5m4PAisU1EXgDyoITB1LbHxtakQQzhbWGf9jTDDDx8jy2mPBbPylDkXivtMF3T1YB38bXy_p5IDH9m2A5TFM8qZlE5tOarO8wMgqFXx3AIMlhjG0maDLaGDXDlAU6QUIyqXpFd7yYYOyViKvxk_ti4Jmhbw9BjgnrKIAp_NQnC1_zPCDcOPwstBzi8J-gHJ8cRcVWzNDKHPxgEnmfRqNFlqNWUgVeO32Y1Zpt4ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان با صدور حکمی پاک‌نژاد وزیر سابق نفت را به عنوان مشاور خود منصوب کرد  #سیرک
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151281" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151280">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
پزشکیان با صدور حکمی پاک‌نژاد وزیر سابق نفت را به عنوان مشاور خود منصوب کرد
#سیرک
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151280" target="_blank">📅 16:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151279">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
پلیس انگلیس: یک شهروند به اتهام تلاش برای انجام اقدامات تروریستی در نزدیکی پایگاه نیروی هوایی فیرفورد دستگیر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151279" target="_blank">📅 16:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151278">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93e00a668e.mp4?token=vRNaaeWRlZbsSAYANDRPMPy08yw0Nxfq9v3i88eT-11iyoOm-lu263TjxSmngcJkImGGJxumNurokuq7kqQiayOZaEdKf6ouLCBzgLJd_SaZ5N-J7gGj0EirWGG6WGtCnadjVTvs1r8Ktu0XKY53cBGZeO9QKgOnXKhOHWebPwre9dMbKVP_HLRi2EbsdNk_yU1hmPKdGAycC6wvk4axSrwhfCkzD9R5H8RBAe9916haMSd2NQ2tLsaON65f8KaiMZMMFKG7jRuYjtYZ2fxIiZ7gfVvT8tW0RbW93GzNBla_rZjgsnEj_Gmzg4GivjesxG56FQhQaAEi7DAI80mMsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93e00a668e.mp4?token=vRNaaeWRlZbsSAYANDRPMPy08yw0Nxfq9v3i88eT-11iyoOm-lu263TjxSmngcJkImGGJxumNurokuq7kqQiayOZaEdKf6ouLCBzgLJd_SaZ5N-J7gGj0EirWGG6WGtCnadjVTvs1r8Ktu0XKY53cBGZeO9QKgOnXKhOHWebPwre9dMbKVP_HLRi2EbsdNk_yU1hmPKdGAycC6wvk4axSrwhfCkzD9R5H8RBAe9916haMSd2NQ2tLsaON65f8KaiMZMMFKG7jRuYjtYZ2fxIiZ7gfVvT8tW0RbW93GzNBla_rZjgsnEj_Gmzg4GivjesxG56FQhQaAEi7DAI80mMsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداد عادل : هربار میومدم خونه و میدیدم یه جفت کفش له و درب و داغون جلو دره، میفهمیدم مجتبی اومده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151278" target="_blank">📅 16:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151277">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
مارکو روبیو: جهان در طول ۲۰ سال گذشته تغییر کرده است. تمرکز ما تغییر کرده است.
🔴
من فکر می‌کنم ایسلند و موقعیت آن نقش حیاتی در دفاع از اروپا و میهن ایالات متحده ایفا می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151277" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151276">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0a8054a9b.mp4?token=nxKu2qEnIzaw2YU1EXnE4LHOz0BZDnLRuO9ZPrtBNC4u-IOKtAlxXu57H7il2nrXw4MUCF3j437-mAPrpxk84t6zY2B513b5BFRfNKvGD-3i8KG6NGcQjYqNoMoBjIRFiSKQjRZdQoBUinDnc-Byc8WICiPlTZ_M7aDDr-nNI3xBhHHEn-Tl_QQwHAJrPOqj-6hYCeHk4yjbljIOHvGR9GaTzPjbLC_8ViK_llfswMpo4CF6X1ssX2MrYBAOz6DH-xGW8dLL6gEmSnSGvsdKB8JM-B0PEx-0OLOOp2NlNqAzaOasJoBTXJo61P01z8Lp42PPw8gqQobTbhWioFkHao3YLZgL-uTIGex4Ojq9KBgcPPZD_M8Xb_skZr1iGk-Jzts6U3z-B-WCk_FyOXBwQ0HDZdBW31ivp8i-zZZ1PwZhN1F8KSmxQ08wwxoOyaC67l4sozlM3eV1DHWwPSjir7a0jHz3GKnNB_-eAB_VJyLVtnBhs6vH2-Rjwz-TUpsnpVOwZuUMlJhvX7IaqI_wt4lRs7bWq4heQeTUJxMbcuwG5OrOijO_BIkZJ7bAZa_YJ0Zal0XJDHNusDblWYJTHmphzDlqmxTAuxtC7yoYxQfpI9ueM7351n8QLwSomV-w98sily5zzyB5W2SFx2Za6OyA0KO2P1jzg6cZuBiA7AM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0a8054a9b.mp4?token=nxKu2qEnIzaw2YU1EXnE4LHOz0BZDnLRuO9ZPrtBNC4u-IOKtAlxXu57H7il2nrXw4MUCF3j437-mAPrpxk84t6zY2B513b5BFRfNKvGD-3i8KG6NGcQjYqNoMoBjIRFiSKQjRZdQoBUinDnc-Byc8WICiPlTZ_M7aDDr-nNI3xBhHHEn-Tl_QQwHAJrPOqj-6hYCeHk4yjbljIOHvGR9GaTzPjbLC_8ViK_llfswMpo4CF6X1ssX2MrYBAOz6DH-xGW8dLL6gEmSnSGvsdKB8JM-B0PEx-0OLOOp2NlNqAzaOasJoBTXJo61P01z8Lp42PPw8gqQobTbhWioFkHao3YLZgL-uTIGex4Ojq9KBgcPPZD_M8Xb_skZr1iGk-Jzts6U3z-B-WCk_FyOXBwQ0HDZdBW31ivp8i-zZZ1PwZhN1F8KSmxQ08wwxoOyaC67l4sozlM3eV1DHWwPSjir7a0jHz3GKnNB_-eAB_VJyLVtnBhs6vH2-Rjwz-TUpsnpVOwZuUMlJhvX7IaqI_wt4lRs7bWq4heQeTUJxMbcuwG5OrOijO_BIkZJ7bAZa_YJ0Zal0XJDHNusDblWYJTHmphzDlqmxTAuxtC7yoYxQfpI9ueM7351n8QLwSomV-w98sily5zzyB5W2SFx2Za6OyA0KO2P1jzg6cZuBiA7AM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره اوکراین: عضویت در ناتو در حال حاضر روی میز نیست
🔴
در حال حاضر، ما صرفاً بر پایان این تعارض تمرکز داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151276" target="_blank">📅 16:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151275">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
مارکو روبیو درباره مورد مشکوک طاعون در روسیه: به نظر می‌رسد روسیه موظف است که به وضوح اطلاعات بیشتری را با جهان به اشتراک بگذارد
🔴
این کاری است که باید انجام دهند. امیدواریم که این کار را انجام دهند
🔴
ما این موضوع را به دقت زیر نظر داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151275" target="_blank">📅 16:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151274">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151274" target="_blank">📅 16:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151273">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151273" target="_blank">📅 16:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151272">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP48Egffxc1UAh4dEfh30EGCVRYa3ofkZdohrRAXNfb9dZmzPsjVcwz8utXXQuWZUYDKxu6ZTBmykr0d91rDzG5PRu_2QCi78u3r0sz6GKNqI3EP3E4aZwsDfq9L9iLm5Fp_9VAzS3U0JB3XzNZIQcTXYHsbfNBe2Yb1bE4x-3i9d7HmdJQ0ACemAVBrfH8sUcMl5w3dYA_bY3lAeHTlkOqCFWtlxczkZR_v7SIUXqDDin6ATOml3VNpoSSnpv6qzB4ATT6fIKLVMY4Vn5nr7lSIcbW3-et9FN29XYIk3sH_Dv2mZwatvRbDlvGhwq0NnbV6mWFbgHKe6pJVa6kXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: باید جلوی دستیابی ایران به سلاح های هسته ای را بگیریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151272" target="_blank">📅 16:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151270">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNLqIceCoAhnUc1YLW7EEvaF6F1eeW8GFdLJT2ycVQ8o_0-cPzQpJB7B83EVrGiNoQZBov05nBBGE4X7gFPBBvanu5MeEgo0TkM0e1O4uqEG4jm7pqukOO6MXD8RLpAUEL6wdIeBwNjnBFhdDS48PnabacwZCtO-6YLJkWlpfqT_wPN4hyisjGdM3wjJIu_ppfwHr84MuKuC1UQMJB4ZiAdQUj8TbE18XieehpA3QdCAQN2sJQQ0EYI9-vJXntzHtyr9V7mQyO5hH2yzfRFngovSHF7AoDOpab-_RK6esCKelef3DcfE0RCfnZR34PEkg1tBlOvwrLmQj2kw0TL7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
یک نفتکش که در حال عبور خروجی از تنگه هرمز بود، در تاریخ ۶ اکتبر هدف اصابت یک پرتابه ناشناس قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151270" target="_blank">📅 15:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151269">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
گزارشات از اختلال شدید در اینترنت
👎
👍
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151269" target="_blank">📅 15:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151268">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزیر کشور در دوحه: از نقش منصفانه و میانجی‌گرایانه قطر و پاکستان تشکر کردیم
🔴
بحث‌های مطرح شد که ان‌شاءالله سطح تنش‌ها کاهش پیدا کند و سایه جنگ از منطقه دور شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/151268" target="_blank">📅 15:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151267">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رویترز: پالایشگاه‌های نفتی چین، خرید خود از نفت خام عراق را افزایش داده‌اند تا کمبود عرضه نفت ایران از طریق تنگه هرمز را جبران کنند
🔴
بر اساس این گزارش، حداقل ۱۲ میلیون بشکه نفت خام از عراق و قطر خریداری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151267" target="_blank">📅 15:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151266">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
عارف: ما به هیچ‌وجه نگران تحریم‌ها نیستیم، چونکه کشور ما در برابر تحریم‌ها آب‌دیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151266" target="_blank">📅 15:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151265">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
تسنیم: پلیس فرانسه حقوق معترضین رو رعایت نمیکنه و تا حالا ۶۰۰۰ نفر از معترضین رو بازداشت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151265" target="_blank">📅 15:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151264">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
خبرگزاری دولتی سوریه: احمد الشرع برای دیدار با محمد بن سلمان وارد ریاض شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151264" target="_blank">📅 15:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151263">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
قاتل فراری پس از ۱۹ سال دستگیر شد
🔴
مردی که سال ۱۳۸۶ در جریان درگیری در یک زمین کشاورزی در فشافویه، فردی را با شلیک گلوله به قتل رسانده و متواری شده بود، پس از ۱۹ سال شناسایی و دستگیر شد
🔴
براساس تحقیقات، ماجرا پس از ورود گوسفندان به زمین مقتول و اعتراض او آغاز شد. در جریان درگیری و تیراندازی، چوپان با سلاح شکاری به سمت صاحب زمین شلیک کرد که به مرگ او منجر شد.
🔴
کارآگاهان اداره دهم پلیس آگاهی تهران بزرگ پس از سال‌ها پیگیری، سرنخی از محل اختفای متهم در یکی از روستاهای اطراف مشهد به دست آوردند و او را در عملیاتی دستگیر کردند.
🔴
متهم برای ادامه تحقیقات در اختیار پلیس آگاهی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151263" target="_blank">📅 15:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151262">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
وزیرخارجه روسیه: مذاکرات ایران و آمریکا به بن‌بست خورده و بعیده توافقی انجام بشه.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151262" target="_blank">📅 15:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151261">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41d64143a.mp4?token=WHQE7uNGMUh_1JlxUK_GEf7TOL7bJmy3kYQVLPNyPtY433yZ6l8QH1H2U7_gRetBzh3rT6oZgM3VIIzenmme33Lr784jvs3mFwI_CblFEkIlQhxLRkFN8cEQ2rgQscFasQkHQ5TC43DaKkrXHo6ldSP7BlYRffZTUMOn-y6dMosX9WFUQ0GXBoXwug8Tbw8RYdytGcEz2GMVj7ZrGONF4g_VpdoflOiew2tYM8rJYKhUy4rcL4UPiXCbT--YNUT9hXJp8ol3_Op2gpyZIkLT_VIdmXkq7AMDGDmRnd-3WjjWIRCY8S1ia_qq3C6M0V_o7geF2g7Ao8KFxRkaEEjuY7YPcPREG-Q0ZK6Q4JWaCJCs7DlLNTGSOysLeUUU0kGVj9UCfM2dSRwOsI-ev8JjDO_qIoqaeJXWGcLbHZY1KVbg8Lu-LpGtElObzA6ZlSJ6yb3ZGSPRcLlRzyG-d0NTl70UptzU61KaSybvTTNi8Z8VIzDlwJYaUgXbzF-Yo07MciXTLy7OBiZhRYeEpEF27MogxjbMxkFEp3lxpCZoaeoF-Qm2EyZEM09adLQAYDXIQ6Sa5smhjp0CVgtJJ9Im2-p54ACw7QrssgEWIVXsvkEqnk3UlOaGwLbRjkUJAg-Y_uWZenHtn3nNAg45zueO_pYzLFXBt3-SkWw20qEcIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41d64143a.mp4?token=WHQE7uNGMUh_1JlxUK_GEf7TOL7bJmy3kYQVLPNyPtY433yZ6l8QH1H2U7_gRetBzh3rT6oZgM3VIIzenmme33Lr784jvs3mFwI_CblFEkIlQhxLRkFN8cEQ2rgQscFasQkHQ5TC43DaKkrXHo6ldSP7BlYRffZTUMOn-y6dMosX9WFUQ0GXBoXwug8Tbw8RYdytGcEz2GMVj7ZrGONF4g_VpdoflOiew2tYM8rJYKhUy4rcL4UPiXCbT--YNUT9hXJp8ol3_Op2gpyZIkLT_VIdmXkq7AMDGDmRnd-3WjjWIRCY8S1ia_qq3C6M0V_o7geF2g7Ao8KFxRkaEEjuY7YPcPREG-Q0ZK6Q4JWaCJCs7DlLNTGSOysLeUUU0kGVj9UCfM2dSRwOsI-ev8JjDO_qIoqaeJXWGcLbHZY1KVbg8Lu-LpGtElObzA6ZlSJ6yb3ZGSPRcLlRzyG-d0NTl70UptzU61KaSybvTTNi8Z8VIzDlwJYaUgXbzF-Yo07MciXTLy7OBiZhRYeEpEF27MogxjbMxkFEp3lxpCZoaeoF-Qm2EyZEM09adLQAYDXIQ6Sa5smhjp0CVgtJJ9Im2-p54ACw7QrssgEWIVXsvkEqnk3UlOaGwLbRjkUJAg-Y_uWZenHtn3nNAg45zueO_pYzLFXBt3-SkWw20qEcIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امانوئل مکرون، رئیس‌جمهور فرانسه، شاهد اولین آزمایش پرتاب موشک بالستیک جدید M51.3 از زیردریایی هسته‌ای "لو ویژیلانت" بود.
🔴
مکرون گفت این آزمایش، قابلیت اطمینان بازدارنده هسته‌ای فرانسه را نشان می‌دهد و افزود: "برای اینکه آزاد باشید، باید ترسناک باشید. و برای اینکه ترسناک باشید، باید قدرتمند باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151261" target="_blank">📅 15:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151260">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
یدیعوت آحارونوت: از زمان حادثه فلای دبی، 7415 اسرائیلی از امارات به کشورشان بازگردانده شده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151260" target="_blank">📅 15:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151259">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3251d4a5c7.mp4?token=usZEVxwjTBWflPL_3ZGWDCNR5oSgmb5AJ6HpEGGz5GsHlqMkMmX2mHoRbRJBOlD-T443oWUcbj3V1gCPFYkPOcxjifPzotMI6DRgHaBwFlXPI5OGgc25nvgkcPcV3tGaPZh27xMDVnj0rp0qza5_u1rWenBbjOmRzVrJjx9t5OnunDUZLgxFpMCfKI2aRFMk-vrg0qetCexQ-ZzVmVc5vuRQnsiT1ra5c2QUW3Dhq-qHojmbdCABQNQ2IFM6Xj3LySeQnB9TFvJoC8_EQktEFFD7ww18J4y49JarscPKXR_Of4u0itsxR149IzTHW-uTyu2DZ9LcLryld1yTs6mCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3251d4a5c7.mp4?token=usZEVxwjTBWflPL_3ZGWDCNR5oSgmb5AJ6HpEGGz5GsHlqMkMmX2mHoRbRJBOlD-T443oWUcbj3V1gCPFYkPOcxjifPzotMI6DRgHaBwFlXPI5OGgc25nvgkcPcV3tGaPZh27xMDVnj0rp0qza5_u1rWenBbjOmRzVrJjx9t5OnunDUZLgxFpMCfKI2aRFMk-vrg0qetCexQ-ZzVmVc5vuRQnsiT1ra5c2QUW3Dhq-qHojmbdCABQNQ2IFM6Xj3LySeQnB9TFvJoC8_EQktEFFD7ww18J4y49JarscPKXR_Of4u0itsxR149IzTHW-uTyu2DZ9LcLryld1yTs6mCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی: اسرائیل اسم خیابان‌های ایران رو عوض می‌کنه
🔴
مراد ویسی میگه اسرائیل داره اسم خیابون‌های ایران رو تغییر میده. شورای شهر هم فقط تابلو رو عوض می‌کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151259" target="_blank">📅 15:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151257">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
اکونومیست: آزمون اصلی بازار گاز هنوز در راه است؛ زمستان به دو «اگر» بزرگ بستگی دارد
🔴
اکونومیست می‌نویسد با وجود آرامش نسبی بازار، بحران LNG هنوز تمام نشده است. قطر از زمان اختلال در هرمز صدها محموله کمتر از سال قبل صادر کرده و قیمت LNG در آسیا همچنان حدود ۱۴۰ درصد بالاتر از پیش از جنگ است
🔴
به نوشته اکونومیست، عبور اروپا از زمستان پیش‌رو به دو شرط مهم بستگی دارد: هوا نسبتاً گرم بماند و صادرات LNG قطر تا دسامبر به وضعیت عادی برگردد. اگر هرکدام محقق نشود، رقابت اروپا و آسیا برای محموله‌های محدود می‌تواند قیمت گاز را دوباره به‌شدت بالا ببرد؛ در یک سناریوی سرمای زودرس، قیمت‌ها حتی ممکن است به ۳۰ تا ۴۰ دلار به ازای هر میلیون BTU برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151257" target="_blank">📅 14:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151256">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1oq3L_xDc77r9_dWR_yeQywiTclDE1Yt7sD70jumjg0Tmu6-UlKzB2D8I1Wn3LGjnohVG0Cmqls92jrT5RDTI7JW6fYUFzR4mzrio3QFbJ8yFcZ2rkEUmPA7EQgeRAvLEa0dkbyMD0agNNcHLh80_PeRenMj5Ly9xbZsujqzmfCP-TZIewbY3MJfdTVdGcagQB2_9PYz1XH5FqGhec7IzsRM3JZb7niu2gAkCms0N5WTgceE8IvLL94ekzIaGfYOHIqy4lXZV46j1S8UOxkaE6ttJxuVEt-Z0BKm1s3Agctp7xWcZhh9ME7DdZcNCcUkOWNw0IaitFeGTJN-3dH3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز 6 October ، روز جهانی فلج‌های مغزیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151256" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151255">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdtovXS3IoDZTDKzY6Vldf3mBhsst4DCbcgrzKIc9qCIJ3BgFWaeKOB5rWTOledTOW_QyVj1igb-TfWx_QqucJ716mlQN504j6sVHH7oe_w9WbwT9iF2nxF-y95BFATslt-wZBpqptG6ewgzJrOzFoVMvCEWNNcqmiGrMPbHaz9ppM3JBHz39EpL1cmDoJXaJ5FFzZVmNJgzux-JtFxrw8DevwPrcCZ84HKLr1N4wcwUpc3pJJU3p6SRh92BWkLYly5Yv1p8iULRYWmwj16UPxDcymZiHXiaf3fC_r5OfvKYsosbGkQAl_kgIW82d7O5hYHx2oPKx2P0Hcxg_J8prw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اختلال هوایی در پرواز های ابها عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151255" target="_blank">📅 14:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151254">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سخنگوی دولت: برای مذاکره آمادگی داریم و از آن ترسی نداریم/ منطق ایجاب می‌کند که مذاکره را انتخاب کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151254" target="_blank">📅 14:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151253">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وال‌استریت‌‌ژورنال: سرویس مخفی آمریکا CIA یک لیست از ۵ الی ۱٠ نفر مسئولان ایرانی را به اسرائیل داده که این افراد را نباید ترور کرد چون قصد دارند در آینده، حکومت را به دست بگیرند تا ایران کشوری نرمال شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151253" target="_blank">📅 14:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151252">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وال‌استریت‌‌ژورنال: سرویس مخفی آمریکا CIA یک لیست از ۵ الی ۱٠ نفر مسئولان ایرانی را به اسرائیل داده که این افراد را نباید ترور کرد چون قصد دارند در آینده، حکومت را به دست بگیرند تا ایران کشوری نرمال شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/151252" target="_blank">📅 14:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151251">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزارت امور خارجه هند: ۱۲ خدمه یک کشتی تجاری با پرچم پاناما در حمله‌ای در سواحل عمان زخمی شدند که ۱۱ نفر از آنها هندی بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151251" target="_blank">📅 14:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151249">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رئیس سازمان ضد جاسوسی آلمان به اتهام جاسوسی دستگیر شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151249" target="_blank">📅 14:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151248">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فرانسه: تحت نظارت مستقیم امانوئل مکرون، یک فروند موشک راهبردی جدید با قابلیت حمل کلاهک هسته‌ای با موفقیت از یک زیردریایی آزمایش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151248" target="_blank">📅 14:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151247">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزارت خارجه قطر: تماس‌ها و رایزنی‌هایی که از سوی میانجی‌گران میان واشنگتن و تهران در حال انجام است، همچنان ادامه دارد
🔴
اعلام برنامه سفر وزیر کشور ایران به دوحه بر عهده وزارت کشور قطر است و این وزارتخانه درباره دستور کار این سفر اطلاع‌رسانی خواهد کرد
🔴
مذاکرات درباره ایران در جریان است و نگرانی‌های طرف‌های مختلف را در نظر می‌گیرد
🔴
برای سفر طرف ایرانی به‌منظور اطلاع از اقدامات انجام‌شده درباره پرونده خلبانان، آمادگی داریم
🔴
آخرین تحولات پرونده خلبانان ایرانی را به طرف ایرانی اطلاع داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151247" target="_blank">📅 13:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151246">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c01e4ed6.mp4?token=HDakp5GGkWt2mcH98kAtLqFh6XTMfpau5ONHo9ELhZhOZzG_dHAf4sCtfrEuMFsYzxCYTdFI8n_qPOq5SVuUGrKRgpAJmJsvHeSGU31TsTaKmEzTsOzNG0Wp0jn-nE6Q9bwVS9yfYbHQEiuJ2yEV3TnsNC-2rcbmJN07BHqYcwjxBJt5rlWcFrmn_SLT2c6BoS1LpweMcfElZIGs4iCJ4fl5cM6I5XKG2rBomTQB3wqBG7gKKaEKBnbcDN7S9Kn-E79wYdgBSGZelIlNASRMbMVnKeeg6KqjY_UgbTwQkdqwCwb-URnIBL1D9_cMVftnwFp3ah7WofPZXJhxvFdfZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c01e4ed6.mp4?token=HDakp5GGkWt2mcH98kAtLqFh6XTMfpau5ONHo9ELhZhOZzG_dHAf4sCtfrEuMFsYzxCYTdFI8n_qPOq5SVuUGrKRgpAJmJsvHeSGU31TsTaKmEzTsOzNG0Wp0jn-nE6Q9bwVS9yfYbHQEiuJ2yEV3TnsNC-2rcbmJN07BHqYcwjxBJt5rlWcFrmn_SLT2c6BoS1LpweMcfElZIGs4iCJ4fl5cM6I5XKG2rBomTQB3wqBG7gKKaEKBnbcDN7S9Kn-E79wYdgBSGZelIlNASRMbMVnKeeg6KqjY_UgbTwQkdqwCwb-URnIBL1D9_cMVftnwFp3ah7WofPZXJhxvFdfZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو
:
معجزه‌ای که جهان امروز می‌بیند — حتی برخی از کسانی که ما را محکوم می‌کنند، پنهانی می‌گویند: «وای، ادامه بده، ادامه بده»، زیرا آن‌ها این قدرت را ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/151246" target="_blank">📅 13:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151245">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
فروش تسلیحاتی ۲.۲۷ میلیارد دلاری آمریکا به سه کشور عربی
🔴
وزارت خارجه آمریکا با سه فروش احتمالی تسلیحاتی به امارات، مصر و کویت به ارزش مجموع حدود ۲.۲۷ میلیارد دلار موافقت کرده و این بسته‌ها برای بررسی به کنگره اطلاع داده شده‌اند.
🔴
بزرگ‌ترین بسته مربوط به امارات با ارزش ۱.۰۴ میلیارد دلار و شامل تا ۱۰ هزار سامانه هدایت APKWS-II است؛ مصر نیز قرار است سامانه‌های موشکی جاولین به ارزش ۸۳۲ میلیون دلار و کویت خدمات تعمیر و پشتیبانی سامانه پاتریوت به ارزش ۴۰۰ میلیون دلار دریافت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151245" target="_blank">📅 13:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151243">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OuFdV9aJrkcHKofCckKmi9CLG8vZoFjsR1c-tDku2uiPW1gAfqSW8kqshQPfFGCe4CC7_Up5ymY_Mn_HckaMG4Ce8amv2d83rzvp-OKEltUnLuZyXaoeG4tAzbS3_qN17X1h5ezZzacuXxdd8YEgQAKC5izjCAtLvozfWKJblAgVO-kPGTnP1RfaXdBSPQfEpkJGsY6bXcKVoFKLPNkNo37tpISLwmw3L239HO7SGfis7g5iuT1DGN90cOlXnWuEgRP9JYghtTicp3sbPE8_9gQSAkLkiZPgCbq5r955fQ6lU-EXvd0pP_LXwZYc6RFMNX_ppGY3Ka4g5BjDvWSLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4IiYJ153OESv_RZQ1jjr3B_O6ZmUIsNWaeSbezbNSPp_6saX2WBObN-3fvy4PkEITdFCqQC01-pklRGq-rJBIHzItEJXc2rz5V9ekOJotJitvJy7WV428CIRXxuENV7GHG4WtzM62OZZTWdYoyX5DcRqGgAJLFrLbluEA1S9mQdwkyHQL4Yr3xrm0YUbKuGJuZdvUuiY3clt6nAxc28t4OgNb7GAK12r06PWC6pJlmlOb10PBI8_8yWuoe6FsqbbL05TK9r1PvTnP9CH8JifgvnsIjYKVHw6rqdseq_V0UVpRITGjWp1z484ecvRrcET8L8syoIEEhh1IYQfzKW_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بدون شرح از جانفداها
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151243" target="_blank">📅 13:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151242">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ifdo2arlJUnX-7NcR20s084efFKCLCkJeWNQGHvaAGluVkdWgNCWgXxlP-Aj4kzhI-T1D4HERhTcnfxcn8nV3cK0KVtbsPezZAYiC2fea-cyYh8wlt2XHPsdmP7YQHTquK5vKC3YULJdx8Uv-obqSyjDFfdM6a1fbLSInaFfzrrmmyNGjVJOtaWW2p9WPGl2AKknOHHA7RieCvh7A28X1VsrpXefbEttxULoq8cpCDhzv1SmN1UNmHjaERq0QfK_A9aW3dhCMxdywY6ving75qEw0Sn-iVYdyVLQPgRrev15HocM2D-DEqI0K5hNsyRpb4gIC8gvOVVaKCpG6cgzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخی منابع اعلام کردند زین واکر بازیگر دو رگه ایرانی آمریکایی و برنده جایزه نخل طلایی وارد ایران شد
🔴
وی پیشتر گفته بود قصد دارد برای دفاع از ایران بازگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151242" target="_blank">📅 13:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151241">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
خاویر بلاس، ستون‌نویس حوزه انرژی و کالا در بلومبرگ، به نقل از «راسل هاردی» مدیرعامل ویتول نوشته است که طی ۷ تا ۱۰ روز اخیر، به‌طور متوسط روزانه حدود ۱۴ میلیون بشکه نفت و فرآورده نفتی از تنگه هرمز عبور کرده؛ شامل حدود ۱۲ میلیون بشکه نفت خام و ۲ میلیون بشکه فرآورده‌های پالایشی.
🔴
بلاس تأکید کرده این رقم فقط مربوط به عبور مستقیم از هرمز است و صادرات از خطوط لوله جایگزین جداگانه محاسبه می‌شود. رویترز نیز حجم اخیر عبور نفت از هرمز را حدود ۱۴.۲ میلیون بشکه در روز، معادل نزدیک به ۸۰ درصد سطح پیش از جنگ، برآورد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151241" target="_blank">📅 13:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151240">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muUu6ReeNcKIKJ5xY1UaivEEB_uglOBaTVH30fWTVYIkyJYVFKifgKCNq1LFxutGtyI6A7gfZg3wnonP2IcdU2YdA7OkMNdl1SDlZu09UKzG4ON5baxNjFTDZlkeOI2J0WhvHJpjJJWjjQiJAAOFL7Wd7DV9qeuqrm0X0qHRCya5g79clYf85X7ZdLoWcczgAHR3AlihMN2ElBaxqnv63OpIqsv4V-JpmJzlQvQ9mfxypPYRvenAnJ3mHAT3ul_0TnxALW1f-z80s8ifS3LOdm1_G4j99E15ay_1SFT9nNaM9g68kyiOXkIOx2JBSmtkSFgZdTipNUe9fM35EVf9mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار کلاهبرداری
‼️
🔴
کانال فوق ارز دیجیتال فیک معرفی میکنه و میگه بخرید تا سود کنید
🔴
به هیچ عنوان به اشخاصی که ارزهای ناشناس و بی پشتوانه معرفی میکنن اعتماد نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151240" target="_blank">📅 13:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151238">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MhqBnEIOJQ-lAa5D2rpmK9smsMRZgm80VE-UjKPi6nL4zIRQw08EZ5ZvMNm3JcN1DBRFNYhl2yzUvWvwXaGiOH7M-B-r9sUkQRHK0HIQJWMzSGGqP9R3nvdtgiRqQENP-J3XKKRq0P_5xuYLRLwWK7nXqABwPi_MGTt1iAp4WsDvHfrQjScL1TvI5lYcyyDfT3wbXVxiEmGWYu7E1jmEAt76ySagUP75EumURHzK_RJ-Q0votUaecIKMbLBPkhKeUGr_Vf31qP1gmBsRq8n6kekH8Jgczd_A0zLJcSaWp0wzNPZ18FLWSYXo5JnpUhe3o6Jtn8MMG6LOwiG0uisBzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sk-WburxYRT-quF7ZbASqXEizxKZIFDhmepzjTAGQpgfQ4duNxZF360Cg2SuiBG1IczGCNgv0QYB75sNR8KZTzTEmSjEx9Ha07zTkbMVDq57i7U1zw8YVMNa9IsNYVgoV4GcgzDsYwBLPjHtlGET1Y3F8jfBbBpapMAIG8293RyMdiAiRGITDGwYL_NcA6D5tMV_yrPdkYe3l7pRp9i07R2PHjEB8dys3m10W700UObL9tIBYy2FT4yVmvbrzaq0AOGtLc2XZ1Whz3J0q1lUVqNzrM0qocVJdDS7nfU7gr7l_mce-aWeZG5_1f0UXaDT5bZH-8hjL37BGe4ua0_Tow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اعتراض دانشجویان دانشگاه جندی شاپور دزفول به کیفیت غذای سلف این دانشگاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151238" target="_blank">📅 13:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151237">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
مینو محرز: طاعون روسی جدی نیست، کافیه از ماسک و دستکش استفاده کنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151237" target="_blank">📅 13:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151234">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
یحیی سریع سخنگوی ارتش جنبش انصارالله حوثی ها گفت که این گروه فرودگاه بین المللی ابها را با یک موشک بالستیک هدف قرار داد که باعث اختلال در رفت و آمد هوایی در آنجا شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151234" target="_blank">📅 13:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151233">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
سود امروز حساب های متصل به کپی ترید  پشتیبانی
👇
@shahab_amir_support  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151233" target="_blank">📅 13:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151232">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8873094f08.mp4?token=u0qG2GbWRw_dgY0GQOyMDNKvsdZ1CsQ8VmjMwRYz_4dhAY-izdawDL1yndvqlBju9eBuYOA3bYwbE8smJ_HfCL3qVTJMzSVxhy_WP-EgpQR_u-zfM6Q_03pokoOPh20CYovaL_26YR91cv4r5X8cpNWExe08Jy1X3GoA595KedqQquanfcBzlrS1Li_tpEmG7_39YL3VfSwLrMqCxuwJJYaMSTrtZEyinHYmiEUaaDQ-uLBEZk41RXIoBMC0F40FIEm4AmU_L1NduHqBlvioje0BKKmPHhqJkm-TLCS0f5wQBFrKj_A2GcIn6l5mDq50JQJ1Dl85X_AXbR-vOEzfiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8873094f08.mp4?token=u0qG2GbWRw_dgY0GQOyMDNKvsdZ1CsQ8VmjMwRYz_4dhAY-izdawDL1yndvqlBju9eBuYOA3bYwbE8smJ_HfCL3qVTJMzSVxhy_WP-EgpQR_u-zfM6Q_03pokoOPh20CYovaL_26YR91cv4r5X8cpNWExe08Jy1X3GoA595KedqQquanfcBzlrS1Li_tpEmG7_39YL3VfSwLrMqCxuwJJYaMSTrtZEyinHYmiEUaaDQ-uLBEZk41RXIoBMC0F40FIEm4AmU_L1NduHqBlvioje0BKKmPHhqJkm-TLCS0f5wQBFrKj_A2GcIn6l5mDq50JQJ1Dl85X_AXbR-vOEzfiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: در دنیای غرب امروز، در دموکراسی‌ها، آن‌ها نیز انتخابی ندارند — و نمی‌جنگند. ما انتخابی نداریم، و می‌جنگیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/151232" target="_blank">📅 13:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151231">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
صدای انفجار در شمال ریاض، پایتخت عربستان سعودی شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151231" target="_blank">📅 12:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151230">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869ee22d10.mp4?token=W_OA4TpKWsoPMBrrVLAKYynDz2_5VEof4_vs-0fwJ0OOkQgzubNE3YlWcadvvFzbRc9tAjCmizyzrYKkb1Cqyw7_w-WMNMuVWyijZfyQ-UkGZOnbbzo2WzoQWO9nuMs3WY1Ccy1fsHndMzK3weLGBLXka1yqRYLzKeV7d7wAhC4oEO2kaF5p07Wb2bHNpbMVHLL6sCTIHlgeLtiCsx5KlZh2scXS2tv2vGUx2Pq7Hd4pqBUXAxe68yWKHDbkfnnT0g5PEile8e6a_jqhvtzRZSyVHwiUp-lmPKwe7pXz1D0frl3Cc-oodTYuyhcWzJHmHZC-5WFrMK8Nhiz_06Qcwx_2PeJOXSkzJshEmf9s0Tm_818VJhzmC0jjVyQPo_2cpRhBrqDyf54uwJJyasKULF-m2ZAn-VoWTbhDf1vHs2L8LtljhS911I3P0RUC0RZmzjAwjXoMG-4E1whYSfnNUyYvVCx4dlJ1q4jYYi2Z8YmQ6JkgIobVx7WvgflwY__NYMnHjVBu7Yua2ERayurotkMbo3XlnSk5fKwCtX1IteOtiBDB2hYTym1QuhrrfDjaL8FqPvh6y_NPkTwXikrWe8S8t8NLCvhDO4sfVRAau3yJeOcBKZZVhSi0wiV59sa2VE8EkU4ZwlPHmRAQuCJdnf3J3V6LlcjzrUQMVdqm5a4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869ee22d10.mp4?token=W_OA4TpKWsoPMBrrVLAKYynDz2_5VEof4_vs-0fwJ0OOkQgzubNE3YlWcadvvFzbRc9tAjCmizyzrYKkb1Cqyw7_w-WMNMuVWyijZfyQ-UkGZOnbbzo2WzoQWO9nuMs3WY1Ccy1fsHndMzK3weLGBLXka1yqRYLzKeV7d7wAhC4oEO2kaF5p07Wb2bHNpbMVHLL6sCTIHlgeLtiCsx5KlZh2scXS2tv2vGUx2Pq7Hd4pqBUXAxe68yWKHDbkfnnT0g5PEile8e6a_jqhvtzRZSyVHwiUp-lmPKwe7pXz1D0frl3Cc-oodTYuyhcWzJHmHZC-5WFrMK8Nhiz_06Qcwx_2PeJOXSkzJshEmf9s0Tm_818VJhzmC0jjVyQPo_2cpRhBrqDyf54uwJJyasKULF-m2ZAn-VoWTbhDf1vHs2L8LtljhS911I3P0RUC0RZmzjAwjXoMG-4E1whYSfnNUyYvVCx4dlJ1q4jYYi2Z8YmQ6JkgIobVx7WvgflwY__NYMnHjVBu7Yua2ERayurotkMbo3XlnSk5fKwCtX1IteOtiBDB2hYTym1QuhrrfDjaL8FqPvh6y_NPkTwXikrWe8S8t8NLCvhDO4sfVRAau3yJeOcBKZZVhSi0wiV59sa2VE8EkU4ZwlPHmRAQuCJdnf3J3V6LlcjzrUQMVdqm5a4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: بیشتر اقوام باستانی دیگر وجود ندارند. آن‌ها این پیوستگی، این رشته‌ی وجود، این چشم‌انداز بازگشت و آمادگی برای فداکاری، برای آمدن، برای سکونت‌گزیدن و یک‌بار دیگر به دست گرفتن شمشیر داوود را نداشتند
🔴
بیشتر اقوام ناپدید شدند. قوم اسرائیل در اینجا توانایی‌های فوق‌العاده‌ای را به نمایش می‌گذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151230" target="_blank">📅 12:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151229">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/JEkGr0UClIKgIDuQBse_LrSd60wkW0QuZb-ZQDUikyUQldDPVQWdHQ3WmnOi-iWdmwFf4qbVrW0BQqExomsFPN7uAuI0BxTj-Q5pZrnaQbKKvYWNEX3kKjWTzLKGS48dzKKYN7EnAPl99GjIdITD4kCqQPzV1u7CtdoF2CezxRvqMGpsRffLHV8CWI1u-t8aQBHRMPWU6TjpCh-90rZqnpqVzh44jCYVuEnDse9jiadY8hVFFOflUHmD_e02oNRgS2YPi1P_bBUwTG8EBxRBLzDqhDB5ZeqQL5vvZ-5HyXPA5gCPQXV2fsZo0FUX_JPG1I9dZCXu3xDxNqemP1xfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های پروازی نشان می‌دهد که در پی حملات یمن، فعالیت فرودگاه بین‌المللی ریاض به حالت تعلیق درآمده و چندین پرواز نیز موفق به فرود در این فرودگاه نشده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151229" target="_blank">📅 12:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151228">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93c4fbc3d.mp4?token=rijLdE_IO5r8gdu-1CZkfYknU4fp3f-9HuiIR5cPsQ_TTSLSaGdGy4bY5QZw14490yBRqIpgbnZ-NfzLx3eHUtA5TSXuxRITPpdWJ2Vt6N6fj-CL7eT8mzlCPyfOWiUvlERNbzqrOr-VNE-v2HQU6l17UBxJYITUQ9KIoB-Nfbc4ygOkmLMs0phR3XGa0l2ZG3nHa86BT-wpyvAr5FQZFAxuROi2adyNmZ_q8FkrCezLAhx5np5bHHdFJaMBUFtxmmScu3L91GLt2D3izKKSyPdmOOkyfkPFDfh-sf1v0pQZQTwoddyh-bmPrXtyIcPPh-23weITsTfzj3fxMa5C1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93c4fbc3d.mp4?token=rijLdE_IO5r8gdu-1CZkfYknU4fp3f-9HuiIR5cPsQ_TTSLSaGdGy4bY5QZw14490yBRqIpgbnZ-NfzLx3eHUtA5TSXuxRITPpdWJ2Vt6N6fj-CL7eT8mzlCPyfOWiUvlERNbzqrOr-VNE-v2HQU6l17UBxJYITUQ9KIoB-Nfbc4ygOkmLMs0phR3XGa0l2ZG3nHa86BT-wpyvAr5FQZFAxuROi2adyNmZ_q8FkrCezLAhx5np5bHHdFJaMBUFtxmmScu3L91GLt2D3izKKSyPdmOOkyfkPFDfh-sf1v0pQZQTwoddyh-bmPrXtyIcPPh-23weITsTfzj3fxMa5C1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: باید به شما بگویم، من فقط به مدت دو سال سناتور بودم. این شغل آن‌قدرها هم سخت نیست. شما حاضر می‌شوید. برای مردم خودتان می‌جنگید.
🔴
حداقل، فقط حاضر شوید و رأی خود را ثبت کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151228" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151227">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07fe7b3ea.mp4?token=Ij8Btq5q6-Pyc7i6JEhr5AlACfRLx38wuM1o2koH1ENkYdzvBviUfw_PbwMkLlYOClg8huq55EFhlal9BG2G8bORxmsAl8iSPuBjo9QEcE6aYsURikfUn99QaVvRqnZdE8U517yu0zeIQXsvDazdxBcMq4ASBMkpa1me8_yokwlSTZkj6QqRhxTsMSedrDtLRElKisibdJbCn01FXfxqpDq5PRGcGLvVektOq0Ylg4Z_IK-JDQUK39OgOSbX816vVm_q1xO-liLPSdj_b9eP4pNSZXaO9SQfJ19icC356wJlYnVPiDaw1C49QW52WHr5ZmxXyPjPcgNMXmeAy3UOSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07fe7b3ea.mp4?token=Ij8Btq5q6-Pyc7i6JEhr5AlACfRLx38wuM1o2koH1ENkYdzvBviUfw_PbwMkLlYOClg8huq55EFhlal9BG2G8bORxmsAl8iSPuBjo9QEcE6aYsURikfUn99QaVvRqnZdE8U517yu0zeIQXsvDazdxBcMq4ASBMkpa1me8_yokwlSTZkj6QqRhxTsMSedrDtLRElKisibdJbCn01FXfxqpDq5PRGcGLvVektOq0Ylg4Z_IK-JDQUK39OgOSbX816vVm_q1xO-liLPSdj_b9eP4pNSZXaO9SQfJ19icC356wJlYnVPiDaw1C49QW52WHr5ZmxXyPjPcgNMXmeAy3UOSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: برای مدت بسیار طولانی، دشمنان آمریکا به آلاسکا نگاه می‌کردند — با منابع طبیعی باورنکردنی، فرصت‌های باورنکردنی و فرصت‌های راهبردی این ایالت — و دشمن قلمرویی را می‌دید که بدون دفاع بود
🔴
ما این را تغییر دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/151227" target="_blank">📅 12:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151226">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1Its-gJCYk33SwKfnOnK8dHsjTMm3uUolYS87TxQmbFxXapvDhZES_5MeQQAY3tSEduc4Fmwbuw1zNiQsL8sL21YLsWw1ly4JSb0Gg70rcrjudWRLzuIC2ZJ471eKaw3VIQlUOmyEstRNl5TMo09_tW_a7xwHnpS5oBnHdP_Yv6wdTla4znJLCpba0eFeHfmzj_6yaDba7NmLWE70BcOj96MjBSVKj1pqoCD6dtAVOYtKBHZ5UkfUEEW2jxR27NI2LBz2e-wXL1fD2RDxrTaVgc-x-QOQgohHZ_nEi2R3mm_aLLK4UpfZXbvd9mVdKc7Q-VBUYmQ-4JRboVmhW1Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت همچنان به ۹۹ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151226" target="_blank">📅 12:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151225">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203e8b13d6.mp4?token=R6MFvXR9PvQcIwV7dGMR_LORul4xEwoB91MBRNjxye6_hdaOUf4auSSWkLrZhnHxl_DsiPZdyV-vLAaZcQYEbOfpJMeUlVg7RjI-ccc8PSxX949kAFZVMBOjhcKm5rCOZ5RZeQ4GRrOHaENAw2IWDgalolK9nSzxQeL6LIT0hMCma1QCiZMpeaxZ3S0mGI-KIVxATQzeJ5Z33rnbvSWnSwBFuOq4SBq6vKmPsnMPBypmPUidYZOV3ndG56d_5_W77MFkZ3Ho43m_cNYEs4vHCre277OQsKS0p-TU-NSr3SRb_SqPlWg4kn1sPOsy90LlbzepkoQOIvCiHgDgvvZEODP5Xt70koUo7lg0xMeHWEN3WDxcQDND20aJ7fpCjz1y_Tpj1Slx9roWVUXFPeRW6Cb3KK78wRCMVVQJWQSPIqGpMUkKSukUgxC8L7SgZCGDvTUx5MvCuYYs4a4lRY9isidUyYtpG3B58GyEIpgWZG8o2UTL2sQhjVQbrPkNNPuJRxsEiTEpHhA1anEfBrSQM6XP4Dral1jfYoX1BSx6yIN3NRis9aUASBBqyQZYDUjIhvbGJAH69vWiZKxETELJdOpkHC57qhprgOGBiGqdjvcALzkjw3aiU3rlYay0Lcq3XUugu0tJ1U7mI_HQjdGIhldqClahntwVDTU3EhfQwUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203e8b13d6.mp4?token=R6MFvXR9PvQcIwV7dGMR_LORul4xEwoB91MBRNjxye6_hdaOUf4auSSWkLrZhnHxl_DsiPZdyV-vLAaZcQYEbOfpJMeUlVg7RjI-ccc8PSxX949kAFZVMBOjhcKm5rCOZ5RZeQ4GRrOHaENAw2IWDgalolK9nSzxQeL6LIT0hMCma1QCiZMpeaxZ3S0mGI-KIVxATQzeJ5Z33rnbvSWnSwBFuOq4SBq6vKmPsnMPBypmPUidYZOV3ndG56d_5_W77MFkZ3Ho43m_cNYEs4vHCre277OQsKS0p-TU-NSr3SRb_SqPlWg4kn1sPOsy90LlbzepkoQOIvCiHgDgvvZEODP5Xt70koUo7lg0xMeHWEN3WDxcQDND20aJ7fpCjz1y_Tpj1Slx9roWVUXFPeRW6Cb3KK78wRCMVVQJWQSPIqGpMUkKSukUgxC8L7SgZCGDvTUx5MvCuYYs4a4lRY9isidUyYtpG3B58GyEIpgWZG8o2UTL2sQhjVQbrPkNNPuJRxsEiTEpHhA1anEfBrSQM6XP4Dral1jfYoX1BSx6yIN3NRis9aUASBBqyQZYDUjIhvbGJAH69vWiZKxETELJdOpkHC57qhprgOGBiGqdjvcALzkjw3aiU3rlYay0Lcq3XUugu0tJ1U7mI_HQjdGIhldqClahntwVDTU3EhfQwUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه آلمان، واده‌فول: ما همچنین باید بتوانیم دولت اسرائیل را نقد کنیم.
👈
اما باید این موضوع را از محاسبه‌کردن هر یهودی به‌خاطر اعمال دولت جدا کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151225" target="_blank">📅 12:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151224">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
دولت فرانسه اجازه ازدواج مرد با مرد رو صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/151224" target="_blank">📅 12:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151223">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
تسنیم: استیضاح عراقچی در سامانه مجلس ثبت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151223" target="_blank">📅 12:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151222">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزارت خارجه فرانسه از تخصیص سه میلیون یوروی دیگر برای عملیات نظامی در یمن خبر داد.
🔴
بدین ترتیب، مجموع کمک‌های مالی اختصاص‌یافته از سوی فرانسه، به 7 میلیون یورو رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151222" target="_blank">📅 12:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151221">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سخنگوی قوه قضائیه با اشاره به رأی پرونده‌ کلثوم اکبری: ۱۰ خانواده‌ درخواست‌ قصاص کردند؛ به ۱۰ بار قصاص محکوم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151221" target="_blank">📅 11:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151220">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رویترز به نقل از سازمان هواپیمایی کشوری عربستان سعودی: فرودگاه‌های نجران و جازان شامگاه دوشنبه هدف حمله قرار گرفتند.
🔴
در این حمله ۳ نفر زخمی شدند و خسارات مادی نیز گزارش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151220" target="_blank">📅 11:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151219">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7970a23c01.mp4?token=sNapFCBnLpUqPIaNWE-mBkPAn1Q9zqqc0F38i_vuoj2X55qywJ25BmTr9NihPvpnCICF9Hs6uPH8nvXe8vTzfMwm-k7Z3jzQQ9oUJtBfZ9C8fjAofOl0P_dppP_kqDDKleA_93h8E2S_JRGR51I7hhY61CWW0YZJvcNpE1_xcYc5k6AJn2yojnJP105CZDmeb_Iw3F0rIZaH0oo3KUQNgFhzHAZHhwr49ipuivR45Q0wlJrXCIkeQoyRJYuoh02Ql-tzQnvPCPNAGWa9LS5vwZN-x-GRvhbtCGYJy-GOtcXBKrEtF4hnTIPMFIAOZEgbkL8_77voGzYksZJWryaZ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7970a23c01.mp4?token=sNapFCBnLpUqPIaNWE-mBkPAn1Q9zqqc0F38i_vuoj2X55qywJ25BmTr9NihPvpnCICF9Hs6uPH8nvXe8vTzfMwm-k7Z3jzQQ9oUJtBfZ9C8fjAofOl0P_dppP_kqDDKleA_93h8E2S_JRGR51I7hhY61CWW0YZJvcNpE1_xcYc5k6AJn2yojnJP105CZDmeb_Iw3F0rIZaH0oo3KUQNgFhzHAZHhwr49ipuivR45Q0wlJrXCIkeQoyRJYuoh02Ql-tzQnvPCPNAGWa9LS5vwZN-x-GRvhbtCGYJy-GOtcXBKrEtF4hnTIPMFIAOZEgbkL8_77voGzYksZJWryaZ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استاد مطهرنیا: آمریکا هدفش تغییر رژیم هست اما یواش یواش چون نمیخواد مثل عراق بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151219" target="_blank">📅 11:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151218">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBI4Hox78ou1fNjvsPhTgUw6-7C9hxSQ5XgdUMThP6NyFfNFnjeArnSczzu9oYUcwESjWellDN_QmzmalDViD_cNERHGnFvue4J_hj1JJOKYzlx7z09H7k1mMhMFXsPawdufiaTDe-Jj9j16g_TIFG_-xH5SlOLjBME4azbT-MXYSGKTsj0nLBwvYKeicqV_CpAKVKNBlgeaIDL3evF8t379yhRU4sZTi0pL6s3Y5n9iH0BE0F0L0ET3UlBr4VgMHVaN6IF9_iFeoY4SrJpH4eGnZN1SNyvjB0JN5F8RTUWJwwM-_8PucNYpvsWjgS6zZF6GAUDyMn9EKLB_4-rjGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمدباقر خرازی پس از یک ماه بازداشت با صدور قرار وثیقه و پذیرش آن آزاد شد/تحقیقات مقدماتی پرونده ادامه دارد و هنوز کیفرخواستی صادر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/151218" target="_blank">📅 11:36 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
