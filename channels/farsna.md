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
<img src="https://cdn4.telesco.pe/file/jXZIhH7qH3uKnsPcTr8K5xbUxv2O9ytnNY2ojt7O4qlfN4nqvJTr5-XO1pltpNiufIvzTkD48Cv_EohRfFz_86p_u8vDjM_53ZH_4C-2PhGDdWNHKRlDtxI5Lr5Psc49l5hA9HGPwkFV-KC-Zlw2lyjSaXlWZqE3GEgI200YkKi4rQjHzdK_mrvrdsiSB5dcmhe3yE0Izn-IdXwbXUaWsKXA-jBts3iMHLM_QnAQnqHYnWY2sE96yuFrDe9HUZiCvvwj-KZrvSWVseatDt94yFLdt8irYJ9TjcVUf8UPbHPdSBxMiB9_N-cASpqBtC-xejb41BVqEJcWQ3Rj5_YiRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 11:50:17</div>
<hr>

<div class="tg-post" id="msg-435682">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjWYBg15ysnBKG5V4SHRKLD3XazF1_z50WPR48AVbhKbcJnyOMAZIfR3ZgUzfM8crnLL05ZdRWifvGqy6d7KEjPHdP29n4jJ4vc_j3kRranb9W_ccPVGeFuebexQMVtZowPbx1P-L7XtxxtU0iypwKxqfkEd8g1kEFch3LOyciKDNM4qKglXQKCS5NsZiLcoFEBOQE6x9RP6UCBgtrUroz5yeiKqz4x7FKuYz80REDj9-peoBsSps3ncMTCQJINQLKeN2y5Cyi96Vot3fzeAFdCegB_FHEntf7eX0u1jihLz-zjNyubLxzmJlF7ptfk99tJUPTpcXMFYaKxr3iDnyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل هم به امارات سفر کرده است
🔹
سازمان رادیو و تلویزیون اسرائیل اعلام کرد که «ایال زمیر»، رئیس ستاد ارتش رژیم طی ایام جنگ علیه ایران به صورت محرمانه به امارات سفر کرده است.
🔹
رادیو و تلویزیون اسرائیل افزود که زمیر در این سفر با مسئولان بلندپایه اماراتی از جمله «محمد بن زاید»، رئیس این کشور دیدار و گفت‌وگو کرده است.
🔹
این رسانه عبری افزود که مسئولان بلندپایه ارتش رژیم صهیونیستی زمیر را در این سفر به امارات همراهی کرده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 432 · <a href="https://t.me/farsna/435682" target="_blank">📅 11:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435681">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRoKo98U21iJbmPUGhC1t7jSSxPEA9T0a_vwWK2tl2TxD0Azpyzg2iDics8uHbr1dByJimY7fcRCMQon1M4NliqacMmecRWeIxtkQ3cSJZRfcw7U7Qa3HSqnSqWalHI0o3idHpXkHA6RhFGenEd4LuG6cqGsRceQqTVR7HChiQrxdtmsDujNCZNHJRXgxoak_IfeNKaIl0ZNFZJM9UDHVj4C9zQXSBWxByHLcTycbmi_Y69lKXApOsRii1uBl6OOVMWaBJNYG8329803snJrTdtTXtIv3X6fkWi20i3VlZ3MYteLKLMTBbwH7rGYsnr5Zww0LaH-gAoyAcyEK-MhwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر حاتمی: مردم مطمئن باشند تا آخرین قطرهٔ خون پای کار هستیم
🔹
فرمانده‌کل ارتش: آنچه موجب اطمینان ما به پیروزی و توانمندی می‌شود، ایمان و اعتقاد است؛ این ریشهٔ عمیق در ایران اسلامی دارد و هر سال در دههٔ محرم، شاهد یک مانور عظیم ایمانی هستیم. قدرت اصلی ما نیز همین قدرت ایمانی است.
🔹
این قدرت ایمانی است که می‌تواند یک جنگندهٔ اف-۵ را به فراز مواضع نیروهای آمریکایی در کویت برساند، درحالی‌که آن‌ها از پیشرفته‌ترین سامانه‌های پدافندی زمین‌پایه و هوایی برخوردارند، مأموریت خود را انجام دهد و با آرامش کامل بازگردد.
🔹
این قدرت ایمان است که می‌تواند دشمن را چنان دچار آشفتگی کند که حتی به اشتباه، هواپیماهای خودی را هدف قرار دهد.
🔹
در غیر این صورت، اساساً قابل مقایسه نیست که یک اف-۵ را با جنگنده‌هایی مانند اف-۳۵ و اف-۱۵ مقایسه کنیم.
🔹
مسئلهٔ مرگ برای رزمندگان ما حل شده است؛ ما برای پیروزی می‌جنگیم، اما شهادت را نیز فیضی عظیم می‌دانیم؛ همان‌گونه که حضرت امام خمینی(ره) فرمودند، چه شهادت و چه پیروزی، در هر صورت ما پیروز هستیم.
🔹
در پرتو تربیت دینی در ارتش جمهوری اسلامی ایران و مجموعهٔ نیروهای مسلح، این مأموریت بزرگ به‌خوبی درک شده و اهمیت آن برای ما روشن است.
🔹
ما به مردم عزیز ایران اطمینان می‌دهیم که با تمام وجود، تا آخرین قطرهٔ خون و ان‌شاءالله تا تحقق پیروزی کامل، به این مأموریت مقدس ادامه خواهیم داد.
🔹
نیروهای مسلح با تمام قوا از تمامیت ارضی، استقلال کشور و نظام جمهوری اسلامی ایران پاسداری خواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/farsna/435681" target="_blank">📅 11:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435680">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
ترامپ: رئیس‌جمهور چین به من گفت پکن به ایران تجهیزات نظامی نخواهد داد اما در عین حال گفت چین به خرید نفت از ایران ادامه می‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/farsna/435680" target="_blank">📅 11:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435679">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaXA6gdtOHGUm6ah-LsUC1vrvIXMVrt-Sv_QMsEwF5jha9qWfM4b6Xspv0sFHNt-mcxSUoCnIjzstKZMqMnLW2MIRzX9ZICzVc1jOWIzrluJEGHgTOKqeF1Tq3199I40VU2ZiisHRJmhVkjGCReCmsljGNKtEDK8fMeU4xAgtGm1UmU9c3AWo0ZxPcbNLyWwYJ7FIJmS4DRbguvpNa1cOCE0Vjf6ot7jqt4Jmwfns7NBqv8cmoFd4fQUF_M3vmBVnbV5wDCGqLYNhN8Ges0w8AJ0GyjQwT198b99UfRh2lDSaqkr1ikApgUkU_GPWd9uhxdSqH_Yv5Mf0TP6LYV8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر ساعت آغاز سرویس‌دهی خط ۵ مترو تهران
🔹
شرکت بهره‌برداری متروی تهران: با توجه به تغییر ساعات کاری دستگاه‌های اجرایی از ساعت ۷ تا ۱۳، حرکت قطارها شنبه تا چهارشنبه از ساعت ۵ صبح آغاز می‌شود.
🔹
همچنین این خط در روزهای پنجشنبه از ساعت ۵:۳۰ صبح و در روزهای جمعه از ساعت ۶ صبح آغاز خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/435679" target="_blank">📅 11:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435678">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYSrQxNtZ_1DFNnaHZItzUU4ZEFFvTU7v8p1O_rN0h7I-Ag-233D8PTV4LHg0jgjMEnWkf5qusMI9eMJfMITQTvR_gRiCRm0Prf8xlk22LPSEdFCWgyugNyswRTCRVHRNaL61wNG4oPfu19HpH9GMIumjtFmx020PSm5fG7KV5ScDQZAFx93qrd_MlKfDHyR2tRw7Ur_Vjzk1io2Qv5rv4c8k2c0gr5HvMaIoF-I6ZRo6i5MdQnP49KQGN_hLmzY3QdFgRL_Gg8q5LpFm4SEirPeAFMi5p8xrh7zUVWH5SYOfL6iGi8A-Z4CsR0WX-A-rJF5y8vw1hfkwZQPI49cNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجهٔ روسیه: جنگ علیه ایران باید فوراً تمام شود
🔹
وظیفهٔ اصلی درحال‌حاضر در رابطه با ایران، پایان‌دادن فوری به جنگ و دستیابی به یک توافق پایدار است.
🔹
وضعیت خاورمیانه و شمال آفریقا به‌دلیل مداخلهٔ نظامی و سیاسی غرب به‌طور فزاینده‌ای پیچیده شده است. ضروری است که هیچ مشکل یا مانعی در تنگهٔ هرمز وجود نداشته باشد.
🔹
برای رسیدگی به بحران مربوط به ایران، باید علت اصلی بحران را که تجاوز ناموجه آمریکا و اسرائیل است، درک کنیم.
🔹
ایران بحران تنگهٔ هرمز را ایجاد نکرده است؛ منافع آمریکا کاملاً بر نفت و بازگشایی تنگهٔ هرمز در شرایط پیرامون ایران متمرکز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/farsna/435678" target="_blank">📅 11:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435677">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">۸ پلیس پاکستان در مرز افغانستان کشته شدند
🔹
در پی حملهٔ انتحاری در منطقهٔ باجور پاکستان، دست‌کم ۸ نفر از نیروهای ارتش پاکستان کشته شدند.
🔹
مقامات پاکستان اعلام کردند که این حمله در خاک افغانستان طراحی شده، اما طالبان گفته است که این موضوع صحت ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/farsna/435677" target="_blank">📅 11:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435676">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfETNN2f4gYr75brpmmU9flu_X93if_iT6kkTwjEkePsDOX8JLfoMbdqu6D9KiGZi1frdqkaPg2ecmvKQJ1jsF21tl2VvmICGki6_RCwsrcz_PXHTOKvuTyz8GnQxAE8AykP9bdMKfzkGGh_83L-WDts6QmpGo9pgorifdTiJyavcwCIAc_yfmjp20XvbkIJtK_UOJxjAJxP8rtiEmUYkGxPyE7RkaFb4CdpE-kgYHCZO40JojXVGYylME0likXYBfICpEVucXerYm12hkGelnWwwE3Tr5SLoRK_EWXIXgRna-hGFuZvnBeYXQ2n4npVgzYKnSqUuoPPXA0iaRnyeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرفروش‌ترین و کم‌فروش‌ترین خودروهای بازار ایران را بشناسید
🔹
طبق گزارش مرکز پژوهش‌ مجلس، خانوادٔه پژو و سورن پرفروش‌ترین خودروهای ایران در نیمٔه اول سال ۱۴۰۴ بود.
🔹
همچنین خودروهای وارداتی نظیر X33 در فهرست‌کم‌فروش‌ترین خودروهای ایران هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/farsna/435676" target="_blank">📅 11:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435675">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCA8xCJenCNkqDwQ7V1hNF67qT3A__rs4xHwkB90SEqh1xyEw4hyRFtuchbN0xzGZqz2nfVSp1YBNOPkvDG67T4rY8G6BiNLKHIbj_NeDHVbg60jNXL13yRsa87QzqCYeEMUJ-ISqQhetoMzqixbzV_w-HPe2uEHclD91R-XXdcJ3XzR0WBdM4asuAWQRvkA9DkYaA9-avSfjzx__QV_6djMfeRSTzA_-hvX_eZ7qnTmXUjqLd2bX4sGwcVnlZThjAuHCbMWFLB9fKOiKk6715Vaq5dWD6JNl9zpvfCS94KHeN7YsJ5JqcxHtEG7Aq0HJ0bod5b1ZGAKceuZGsRQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتین هم چند روز دیگر به چین می‌رود
🔹
منابع خبری به روزنامهٔ «ساوت چاینا مورنینگ پست» گفتند که انتظار می‌رود رئیس‌جمهور روسیه اواخر هفتهٔ آینده، در ۲۰ می (۳۰ اردیبهشت) سفری یک‌روزه به پکن خواهد داشت.
📌
این اولین‌بار خواهد بود که چین میزبان رهبران ۲ قدرت بزرگ در یک ماه، خارج از یک نشست چندجانبه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farsna/435675" target="_blank">📅 11:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435674">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4D9zYb106VFMzj7R-qZUreVWSjzCF-3_3arVFSt2QquNX60gDChAXl-_CC3VU66mpU_IMEnPXLS0T6lMJencUyzzGvzq5X1y0eQAwppBevs_sw68dTU-Fu7nnz4rnZVlI5VPgFybfyQ2iMxG-YMZeJvWzUv4CIdZ8XIszIWe6A6GTOdke0lMsp1W5gt1AbRXXsFFk3KQrjL5SYF0pvYHMJJjPajYimrTwFntcnpn20jPi5BYabnd9n4Dn6Y__B6GWOyOh1cBogOujAy6JwY9BBJmiCnGYytu3J_15FjnJo-GFW4ylijQM3ntF2aFAZCryGLwYxHFfOwk8r61nrZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح تامین سرمایهٔ در گردش واحدهای تولیدی از خردادماه
🔹
رحیمی، مشاور معاون اقتصادی وزیر اقتصاد: اولویت ما برای آینده، تامین سرمایه در گردش و حفظ اشتغال و نیرو است.
🔹
با تامین تسهیلات حفظ اشتغال بنگاه‌های تولید، در گام بعدی، وام برای تامین سرمایه در گردش واحدهای تولیدی است؛ این وام برای سرمایه در گردش بنگاهها منهای حقوق کارگران پرداخت می‌شود که از اول خرداد اجرایی خواهد شد.
🔹
در این طرح معادل ۱۰ درصد از میزان فروش سال ۱۴۰۳ که در سال ۱۴۰۴ حسابرسی شده را به‌عنوان سرمایه در گردش به بنگاه می‌دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/farsna/435674" target="_blank">📅 10:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435673">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شکار یک مرکاوا و ۲ بلدوزر نظامی اسرائیلی توسط حزب‌الله
🔹
حزب‌الله از بامداد امروز در ۵ عملیات خود، علاوه‌بر هدف گرفتن نظامیان صهیونیست، از انهدام یک دستگاه تانک مرکاوا و ۲ بلدوزر ارتش اشغالگر در جنوب لبنان خبر داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/farsna/435673" target="_blank">📅 10:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435672">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsPzGMl8RGvg6wppHQqpXJud9tXBxnT2cXq_s2uAj0n-JX4SY6oSd4WGeRMiGrYpbTRuKVNTEzGU2wyAT_0a6SfSmY4F4qejJNUO8VA2pX7ynALcD6RjMq3uz7aclT-Ao8ZvlCa0aoQn9monIoSE_1jAgf4LkU9aT3RB2J4RtuuIWj8w-me1_HwA3xKMSfVLntRrsGPIQ0xbFIf2tpGi1tO2zyMj2P3WVpN5oCXPjGrI3WNPb3idLnn8_s00-vQRf6HVgQ6CGIOBX8Pam_Zhby0HlpjG6mZegfb8RFt_kx28HyLL-6MuF-s4dcz8H8LvnnEhWngHPvA6s9buW66I9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوجوانان ایران با نام «ماکان نصیری» راهی المپیک می‌شوند
🔹
کمیتهٔ ملی المپیک تصمیم گرفت کاروان اعزامی ایران به المپیک نوجوانان ۲۰۲۶ داکار را به نام «ماکان نصیری» مزین کند.
🔸
ماکان نصیری دانش‌آموز کلاس اولی مدرسهٔ میناب است که در حملهٔ آمریکا جاویدالاثر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/435672" target="_blank">📅 10:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435671">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بورس آمادهٔ بازگشایی شد
🔹
سازمان بورس: آمادگی برای بازگشایی بازار سهام از اواسط هفتهٔ آینده وجود دارد. زمان دقیق بازگشایی بازار به‌زودی اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/farsna/435671" target="_blank">📅 10:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435670">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d4a7ed75.mp4?token=GCBpxYk_6QfAN9NzmZ3UGIs_7tO9E5xc5RpsYps5STDM24Hz8QmY8G6JOfLld_sGqbhpj2tANFoiRwcN2QGSaeHgrtuSmEpXgnpgIutTny8ZbKgLi3kwouwlnfZTWew-VpPc2ZVF9ZFyvhKKPaivA7J2rJvHf7AgOWtHCEOJDYVT4Rk2piy6i9Z9-3JD1z9tAw_iqQfTelKubwu5bXs9-r1s3lrlQFbAR56R4XJ9Eoy2gM3JciP6IDbOD5LyXzW6OzegHTj38kOZbzVAyURrlnSijDU9APZXvKL8LJmL3pXOwVitO_MDQDuNrtQa4RU3T0OlDiFyjrIDGTuLgA8ngw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d4a7ed75.mp4?token=GCBpxYk_6QfAN9NzmZ3UGIs_7tO9E5xc5RpsYps5STDM24Hz8QmY8G6JOfLld_sGqbhpj2tANFoiRwcN2QGSaeHgrtuSmEpXgnpgIutTny8ZbKgLi3kwouwlnfZTWew-VpPc2ZVF9ZFyvhKKPaivA7J2rJvHf7AgOWtHCEOJDYVT4Rk2piy6i9Z9-3JD1z9tAw_iqQfTelKubwu5bXs9-r1s3lrlQFbAR56R4XJ9Eoy2gM3JciP6IDbOD5LyXzW6OzegHTj38kOZbzVAyURrlnSijDU9APZXvKL8LJmL3pXOwVitO_MDQDuNrtQa4RU3T0OlDiFyjrIDGTuLgA8ngw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ پس از پایان سفر به چین، راهی آمریکا شد
@Farsna</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/farsna/435670" target="_blank">📅 10:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435669">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dX8yTp-jJlvKqsybwjcVXDptHtvyUAs-62JKQzI_jfsYlzWeE9DWgutrqwqIi6KDn75RG2LVQh-VZA8eVTFZiyc79nY0pzskhFaQWJLq_zWKgfp7mLRq_cP-0PL6UdaKfN9_91A6pILN6iB-pCmToEJJfL6HNDkMHMI1IEHOQFsV4CXiYIdsHMZRHBapGInIYAGJp5T8A4BElGDrQrtAGT1wDY6RNHWcuKjmWQfy3DaObPVdFwrpoKTThJvBMvxNM2rlqos56pFWNOALak62uxfZYsG6hIEsjkjGN3Icrs1B17KD2uTkJUttz8z_mz_qF_SNl_iWXjnJeGfbG9hIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عصبانیت امارات از افشاگری دفتر نتانیاهو
🔹
شبکه i24NEWS رژیم صهیونیستی گزارش داد پس از آنکه دفتر نتانیاهو سفر وی به ابوظبی در ماه مارس را رسانه‌ای کرد، امارات پیام اعتراضی شدیدی به اسرائیل ارسال کرد.
🔹
این شبکه افزود که اماراتی‌ها بسیار خشمگین هستند و این اولین بار نیست که چنین افشاگری‌هایی از دفتر نتانیاهو منتشر می‌شود.
🔹
این رسانه به نقل از منبعی مطلع تصریح کرد افشاگری‌های دفتر نتانیاهو دقیقاً دلیل عدم دعوت از وی برای سفر به امارات طی سال‌های اخیر است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/435669" target="_blank">📅 10:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435668">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnLaOw_VkDBhRZSC5yz2t-8BM9NW9L3AMlAZii1ulahZWXS18hoVToDQ49ieRKs0fshimAyESuFVWD_joqmQfl8CKMUiKnuR0OHI70I63R96ODdWg2B8AhIOfNX-9GT_oR5yt1pSuQtvMTjUW5XbmzmBeAFrPGbOoLVbZK0AarWI2XK8ViSykcS7MIsmbX3fAh3KxqjEW2A23EBSgskgdx-49qtKtVicAZYQoTaWNnlIF8fwL3ZWw8aiN6bRI4KjvDMhEF66LWH_Bxv9oHKdiTw1SnpGfHdxvhEQA36lfp3ukg8RzIseX83WqGkeV2Iy2wPLDJfd7bBVXM_r4l1eHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: ۷۰ درصد آمریکایی‌ها عملکرد اقتصادی ترامپ را فاجعه می‌دانند
🔹
سی‌ان‌ان نوشت: در عصر سیاسی حاضر نادر است که ۷۰ درصد آمریکایی‌ها بر سر هر چیزی توافق داشته باشند؛ اما درحال‌حاضر، طبق نظرسنجی جدید ما، ۷۰ درصد آمریکایی‌ها موافق‌اند که ترامپ عملکرد بدی در حوزهٔ اقتصاد داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/farsna/435668" target="_blank">📅 10:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435665">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ws42vGbgKxyigTnNsCOdOJs7WSL764B6BO9H6PabLRjGM4J0YARJAPhYrlBxMbkevyP7i8wXZpS7jpwt8E5ebTccsrZKkEgRNyBmG-g0kEnEC0xqWm7aXbSxrbpooC3LQeaKKbOsXmcetGwD6BMNI02WXhyiNJxGFR8MrKZlDB3OyWKqFHXGNEnRLTh1FLnJJu8KZiXsrkYVAHiC7eTb9MwOZGLOzJlx5w3G9jSdARw3o4-QsSvpjNzl9mErJHFxrGTPbKje6vHR5xyiVnsVav1jXi2kgeOAOUM3QFhWVed1-TyuzVsAbbYBKYfqnfuAA6NOTjBBCC0pf6vJvrXxVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: اصلاح شورای امنیت یک انتخاب نیست، ضرورت است
🔹
ما دنبال شورایی هستیم که نمایندگی واقعی از تمام قاره‌ها و مناطق جهان داشته باشد. بیایید از ظرفیت‌های بریکس برای بازسازی حکمرانی جهانی و بازگرداندن اعتبار به چندجانبه‌گرایی استفاده کنیم.
🔹
جهان امروز شاهد…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/farsna/435665" target="_blank">📅 09:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435664">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XL1ric5Zss32E04vVlAQUdFg9FVGDx2bONzZQ9S10G7t9abJezw0LPXoW2X6eTGn7BLsvBQX_aAVyD3CSHbwdbhpynUuNQbQLRXON-OdcanZCRD5tEhlJU08ekcwo_MoqfM1KJBAipZSPQDf64-yYzEz1CcQJsZeE3equb8ELQpsl7ROVo4cq2sgDDwsCf27CP4ClKyHr09wo85-mEpmwrOy9xMj5b6Ce7E0W-D2zXiQ_H9K8ZvSdJ-ZqNNISvWlywpt7FpWsUaRI5slN5ZbhY9M_JuOqbkEb7LIIZes88zNCWpEyd0UeHQiOcgNd-uKK-nnw2GutgkR1-YaE_a_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین: ادعاهای آمریکا دربارهٔ مواضع چین علیه ایران کذب است
🔹
شبکهٔ المیادین به‌نقل از منابع دیپلماتیک: ادعاهای مقامات آمریکایی دربارهٔ تغییر مواضع چین درخصوص برنامهٔ هسته‌ای ایران یا تنگهٔ هرمز که پس از سفر ترامپ به پکن مطرح می‌شود بی‌پایه و اساس و کذب است.
🔹
موضع چین دربارهٔ ایران واضح و ثابت است و تغییر نیافته و چین روز گذشته از بحث درخصوص این موضوع کاملا خودداری کرد و هرگونه ادعایی خلاف این، نادرست است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/farsna/435664" target="_blank">📅 09:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435663">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNtxyXW1vcXCBCMbfC0nrg3l9oYuJzg-b9WxV8YnVSW-_hDSh2Cii6HlR51qA6mw-EaW1yhgV-XQQQljYpURx9kQAFsEiuuIP5f3HEhvxGuksMxGOnnzRscTIA4gzHXMqZnGHc5BaVgFefCGLIEmLfMQgZ89I3OFN3PN6L-iujpVB5vBtZ8FiAM-jK4MD9jSIFmrZxizOix_xge1sLdKIF0bASgx8KARsSH-OkLsGF0vuylZHqq9gvbcMISoXiTusP6rS3G8i-LM5nJXKorr-0wHXzRw49HY9Ibu3yQsA3PwfnQ7h-74PmEt_8W8cOuM9fqPfVIsqqkz_35oKHME8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاچاقچی‌ها بخشی از گازوئیل صنعت را تامین می‌کنند
🔹
اطلاعات رسیده از وزارت صمت نشان می‌دهد، سال گذشته صنایع مجبور شدند ۶۰۰ میلیون لیتر گازوئیل مورد نیاز خود را از شبکهٔ قاچاق تامین کنند.
🔹
سال قبل نرخ گازوئیل قاچاق در مناطقی تا ۱۵ هزار تومان نیز بالا رفته بود.به عبارت دیگر کمبود تامین گازوئیل صنعت سبب شده تا ۹ هزار میلیارد تومان از بخش تولید به جیب قاچاقچی‌ها برود.
🔹
در سال ۱۴۰۴، ۳.۹ میلیارد لیتر از تقاضای بخش صنعت توسط زیرمجموعهٔ وزارت نفت تاییدیه گرفته اما تنها ۳.۳ میلیارد لیتر این میزان تامین شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/435663" target="_blank">📅 09:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435661">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tiu75NY8FX_h0nyrW-OcOIFDoaAHmEf_vNoN5xl3AdBzlLtTN8Jua8uezLKhD3OV-z0H5-FaHLcTeS1L-sVQdVMFGnN-iH2FFHDACbBTZHVG1f0Yiv8a_UcZb3Vi1ZN3g8AjwtLjDZkfmYFZldO9P2hKji8KynlkZnNZa7wM5B-Sh_DazZKg8djskB4ddsknlIUT69CAer1oMB2kObC_AbAOGKq9d7N0S05XKjui5SlnX7KJXA43ss846IRu2OlhOLExd8zcmYAy3KbsFFNRl7KZI-x8EWEwNoHYquKh4zOv-j3tdCYgxS84tLnfkgQREDZwCjQHhZcGnc9qU5iXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGirWsCO-2IMOlrVgB5PbOKwDtDj6Y5R8uJpeMfOLpEUv-lo4BnsFYdlsPeuzDS3y2Kck8W3JsxbtrGWiuuEnXF9XiU8Yf_bxKQonJiRbMZhJBDkpoCnvO1ALObaVCVxaoOj9syQzKxGCHTIK9qXwNt2CGOOuperYvkr1QrhKyN2OvFTqqRDulRH1C-BDZ5FXcLoNoTgFKoaHVwugbKAzV9yFyyhKyFfqjODNFqvpyywiI7TJ1uJaSf4cCbdtE4rgRrisUH3BiUNMwzYTJ8sl6P5uEGuXnlt1ilWLcw__4HBUblS_qe8p26UXVEy4DnBmVn93F_J8AZDuxrx246QCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار و گفت‌وگوی عراقچی و وزیر امور خارجهٔ آفریقای جنوبی در دهلی‌نو
@Farsna</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/farsna/435661" target="_blank">📅 09:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435660">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhkUZBWUPO89JvqdCwjvy5LOjEGIigUGaprtT21FoIN1iaDUUf3lZpZF280S0D7V5yTqqoHzhMa1yGIKGN3uBwdi5IZ2kG58nwSN_C1WsENxsLoPqiyXkEmBxkKIp-voWxkWdahujbe72QITVidhVBJRRrX_F5D95ACR19mRktaJQ5RbrJPyHz3xZYWD8ThkDCLrIOmGRSQv7dnD22u6iyLDEo09yHD7hDWkf2P8nw8s3AJizS_FUVeHORAih0mTwNecPsxoyYZndFzXNcZIL8msIWTCuLtp441h3yj116GeP2s-HxThR6ND50IepPYLzenDeGAbH_IsQivyEqZVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: اصلاح شورای امنیت یک انتخاب نیست، ضرورت است
🔹
ما دنبال شورایی هستیم که نمایندگی واقعی از تمام قاره‌ها و مناطق جهان داشته باشد. بیایید از ظرفیت‌های بریکس برای بازسازی حکمرانی جهانی و بازگرداندن اعتبار به چندجانبه‌گرایی استفاده کنیم.
🔹
جهان امروز شاهد بازگشت به دوران جنگ‌های بی‌پایان، خشونت عریان و یکجانبه‌گرایی افراطی است.
🔹
کاربرد حقوق بین‌الملل، حقوق بشر دوستانه و منشور ملل متحد از سوی متجاوزان قدرتمند، به لفظی و دروغی برای توجیه جنگ و اشغالگری تقلیل یافته است.
🔹
از این رو، ایران بر ضرورت اصلاحات بنیادین در سازمان‌های بین‌المللی، به‌ویژه شورای امنیت، تأکید دارد. اصلاحات مورد نظر ما، اصلاحاتی برای «توزیع عادلانه قدرت» است، نه صرفاً تغییر در نام یا ترکیب اعضا.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/farsna/435660" target="_blank">📅 09:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435659">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXHeRv9fnMK0zsEofRSAh8PIA5g_BnV-GUGoD7B7vD_X7-jJJ4hzNSstpjtmXkoGs_Wt71tc0pTfTeah3UIB5FqiB6mmJEiOUbx5I_rtLl5mSOSP6VPFlFnlwE9jM5Zno3Rzjz51McYh9zsLW-A0DCClI-7Mns26ea8rXf67DDof9ZpapbZ6zA54AHZ0ypfZhfxPZkHaDuCRzLbjDoGsU35Je1qavpjs-_lZfl140y6BBYLoUEVMuqusbNLyFi3rkjdb17ZjnBrEgrn4fbkoU1G_QsSINH40t2DoQOToaSCJcVoaWQN-siZVDgT6W0K-WAZFuBV8Xrr_rrJPZ0teqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط جدید دولت برای متقاضیان یورو با کارت ملی
🔹
مرکز اطلاعات مالی وزارت اقتصاد، ثبت مشخصات دریافت‌کننده، هدف دریافت ارز و محل و نحوهٔ هزینه‌کرد وجوه نقدی درخواستی برای متقاضیان دریافت ارز با کارت ملی را اجباری کرد.
🔹
بر این اساس، بانک‌ها و صرافی‌های مجاز موظف‌اند اطلاعات دریافت‌شده را در سامانه‌های مربوط ثبت کرده و سوابق معاملات ارزی را مطابق الزامات نظارتی نگهداری کنند.
🔹
بانک مرکزی به‌تازگی اعلام کرده به همه متقاضیان بالای ۱۸ سال در هر سال، معادل ۱۰۰۰ یورو با کارت ملی خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/435659" target="_blank">📅 09:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435658">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/999bea2fda.mp4?token=W7_1f5BoP9ye9193GnRmCtOWCsDfE0ZACelOO56T5YZIySpi4zhIwfjoPE9CQ6jF02yo7Cr84SriqMnMttFdV28Xa5N35RXiCHWHnzdIEzf2o3ZDj7_u5Ae2udefiI-JChhqFtoYyWugFzyduwGUvwC6V5A-USufwSTLwmtgjan_BMNj5vVHhpRDCHa-ZpV--H8XD5WRZCgbfG7LudQeVHRCOXr8y2fmOyTJmlR_ec-3ggkdWu-_Z4pXLAAzpFqSPTjhFZIkym8nzyxXDDLa_X8b4EvjzV8cKy_weMS5FsEeIqWMlt2c_W5lAT_bCoUDljXjED1KspDvTe8qGk9K3whtGPlaBBN5Kp7_hchHAw-06fkOJbcDYPPkRoFNthXQZ_gUMZXWMF2rMABUGyItJ9VaTbYxQBfCp1kifPgFZ8LkgvadqaduMF6dJ6s3BvbzXlrDnqPjfA_qCXdeQGAjzVHw0JuaPgc8DKd9yb1wERdlnl1UayBbq-ZTz-de3ncSuBiyNvBE7Kila1Ez4qGyXwnHxHIbhdBG75ogbt367-Htw-mJU3SukRisnDWQubfFHUhIXFxudJuk-7TQqBh1dEyzvhWNNa2cxnqXcWMd5ByF8zDTAxCFnexp6HJ2AFX_M08Oj0LGixEkmJkfX7_IwNYtRBr6P-8fgqIs02OcvKs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/999bea2fda.mp4?token=W7_1f5BoP9ye9193GnRmCtOWCsDfE0ZACelOO56T5YZIySpi4zhIwfjoPE9CQ6jF02yo7Cr84SriqMnMttFdV28Xa5N35RXiCHWHnzdIEzf2o3ZDj7_u5Ae2udefiI-JChhqFtoYyWugFzyduwGUvwC6V5A-USufwSTLwmtgjan_BMNj5vVHhpRDCHa-ZpV--H8XD5WRZCgbfG7LudQeVHRCOXr8y2fmOyTJmlR_ec-3ggkdWu-_Z4pXLAAzpFqSPTjhFZIkym8nzyxXDDLa_X8b4EvjzV8cKy_weMS5FsEeIqWMlt2c_W5lAT_bCoUDljXjED1KspDvTe8qGk9K3whtGPlaBBN5Kp7_hchHAw-06fkOJbcDYPPkRoFNthXQZ_gUMZXWMF2rMABUGyItJ9VaTbYxQBfCp1kifPgFZ8LkgvadqaduMF6dJ6s3BvbzXlrDnqPjfA_qCXdeQGAjzVHw0JuaPgc8DKd9yb1wERdlnl1UayBbq-ZTz-de3ncSuBiyNvBE7Kila1Ez4qGyXwnHxHIbhdBG75ogbt367-Htw-mJU3SukRisnDWQubfFHUhIXFxudJuk-7TQqBh1dEyzvhWNNa2cxnqXcWMd5ByF8zDTAxCFnexp6HJ2AFX_M08Oj0LGixEkmJkfX7_IwNYtRBr6P-8fgqIs02OcvKs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: کشورهای بریکس پس از ناکامی آمریکا در مقابل ایران، به ما با چشم دیگری می‌نگرند.
@Farsna</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/farsna/435658" target="_blank">📅 09:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435657">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
سخنگوی ارتش رژیم صهیونیستی از هلاکت یک سرباز صهیونیست در درگیری با حزب‌الله خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/435657" target="_blank">📅 08:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435655">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ecf055bf9.mp4?token=hywEkDSc_IE8AOYR6zZm2N8ONjrC4aZVfhG8h2ssol_R-iYPs26J7gsgINHQrvwyzEKV1-mwCUQFVs3EJ6hFTLM6xSIvC9JHaaee9nFfzITYBhf4t9dY4A-0gPnfrn5IcdNHCwQp5v2Hm65EwOPBgmEOAq_t6pUBlzJ_VrOOM9Av1MZxNWBQiALGkOUVFwFYFPpveKdOh0QNretC9C7SFv4GckSRvMSz-nLv2ZDgbVooqFEkYGXEUzKuFi4McVuvYq56Ur4v4Az6bypAlpNOQklsNonhudRqlX1ykn77hNCfIhzt8sS8353ChniPOliNt8yjPXMN5iewqa16XuhqqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ecf055bf9.mp4?token=hywEkDSc_IE8AOYR6zZm2N8ONjrC4aZVfhG8h2ssol_R-iYPs26J7gsgINHQrvwyzEKV1-mwCUQFVs3EJ6hFTLM6xSIvC9JHaaee9nFfzITYBhf4t9dY4A-0gPnfrn5IcdNHCwQp5v2Hm65EwOPBgmEOAq_t6pUBlzJ_VrOOM9Av1MZxNWBQiALGkOUVFwFYFPpveKdOh0QNretC9C7SFv4GckSRvMSz-nLv2ZDgbVooqFEkYGXEUzKuFi4McVuvYq56Ur4v4Az6bypAlpNOQklsNonhudRqlX1ykn77hNCfIhzt8sS8353ChniPOliNt8yjPXMN5iewqa16XuhqqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجۀ آمریکا: در مورد ایران، درخواستی از چین نداشتیم
🔹
ترامپ هیچ درخواستی از رئیس‌جمهور چین نکرد. منظورم این است که ما در مورد ایران به‌دنبال کمک چین نیستیم؛ ما نیازی به کمک آن‌ها نداریم.
🔹
ما مسئله را بازگو می‌کنیم تا موضع خود را به‌روشنی تبیین و آن…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/435655" target="_blank">📅 08:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435654">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be64a7f7c3.mp4?token=HPwz0qR-FhiflpyIbiyCcFYfepGCm7sypy_Land1kdgku4TvcQW0CGMWW3m2ZlNqvF1JKJRrRY5XQsiNisw8uM86-OkWQp79DP7cB44GlOG0oiHlEADN7TjpArg7oziCej5ZLgOFDMyiV75-Zk8cp8CQD1fBUs2nGFgwg8k6n2porRFIPW_87UaseglPlFDhrII78ITdfg2lil06kPuJgAbXuhvD4bc7znkYhDo-Eiis7EmLK_mlimXAuWuZb7PhnieZq-e0MiIeesagcs7WnZVy84Y6A2-kWDfvJcD8oj1pLPUS4DC30It3xil3aoMoH8hquYki1uxtwi0iVQ7PXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be64a7f7c3.mp4?token=HPwz0qR-FhiflpyIbiyCcFYfepGCm7sypy_Land1kdgku4TvcQW0CGMWW3m2ZlNqvF1JKJRrRY5XQsiNisw8uM86-OkWQp79DP7cB44GlOG0oiHlEADN7TjpArg7oziCej5ZLgOFDMyiV75-Zk8cp8CQD1fBUs2nGFgwg8k6n2porRFIPW_87UaseglPlFDhrII78ITdfg2lil06kPuJgAbXuhvD4bc7znkYhDo-Eiis7EmLK_mlimXAuWuZb7PhnieZq-e0MiIeesagcs7WnZVy84Y6A2-kWDfvJcD8oj1pLPUS4DC30It3xil3aoMoH8hquYki1uxtwi0iVQ7PXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: رئیس‌جمهور چین به من گفت پکن به ایران تجهیزات نظامی نخواهد داد اما در عین حال گفت چین به خرید نفت از ایران ادامه می‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/farsna/435654" target="_blank">📅 08:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435653">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f5790d0b.mp4?token=Kox4G_oiRt9tpLyi3O8TMLN18_Fe6FvluBL5ngoFi30xnCrsbWzHaXz2dg8AjFKr6HZNTF_mQbHrarlkCY4sGOACHqb11PrM0xXyelkXY--EMnswYIV3zD2HaS65enlGj9unPCaaNm9P2oZYOyMMbX1eSuNmm2I2kM6hJEV9YePWR48tsmBTHiCZVIC-qPTEoZRiequrnU1jxxm2ZQuHWviIueZ2stS6LNwO1jAlFuEcbugmM8YrcuQqfRuoGLuPPLML47wkQ953tE21EvGm8ssOz8qKc-mgDdQvMHF_AWgtU0_eLH1Z0q9xxzxdhgBiYZhbwrQoi1bAmz3mCOrd-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f5790d0b.mp4?token=Kox4G_oiRt9tpLyi3O8TMLN18_Fe6FvluBL5ngoFi30xnCrsbWzHaXz2dg8AjFKr6HZNTF_mQbHrarlkCY4sGOACHqb11PrM0xXyelkXY--EMnswYIV3zD2HaS65enlGj9unPCaaNm9P2oZYOyMMbX1eSuNmm2I2kM6hJEV9YePWR48tsmBTHiCZVIC-qPTEoZRiequrnU1jxxm2ZQuHWviIueZ2stS6LNwO1jAlFuEcbugmM8YrcuQqfRuoGLuPPLML47wkQ953tE21EvGm8ssOz8qKc-mgDdQvMHF_AWgtU0_eLH1Z0q9xxzxdhgBiYZhbwrQoi1bAmz3mCOrd-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌هایی از تولد و زندگی در پارک ملی گلستان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/435653" target="_blank">📅 08:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435652">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a1079486.mp4?token=BdBCgHo_MUl087JlogGjx1z63uuaKiR2K5kOL1-HY-QJhrruxNNF0HbSuVXR8-lQnF72fuBhJ9XZAfwEjAOfECaxPBbYS1K4MBXEO9jONVUy_tHIuvShXq0bJ3LQslR5KxiiVVbvd0Ygs6o48HFUwUJ5qg6hh18DKxn8OL4ZMvtJYDQyHtRB8dAxH7v7WRLfVrYbV9Lss8JfIvU5_8hUCzVyNoJyUE3mGGO1fI354qawPyqmKW-O4-F0_UWWjkk6o9B3jjfZ-10hePxAx8K3NrASTDCOcL-z_jEf-CmEYewXcqZu9TIjpYsvZOZzLvSS3QbNz2rIlnx90CLS8wotJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a1079486.mp4?token=BdBCgHo_MUl087JlogGjx1z63uuaKiR2K5kOL1-HY-QJhrruxNNF0HbSuVXR8-lQnF72fuBhJ9XZAfwEjAOfECaxPBbYS1K4MBXEO9jONVUy_tHIuvShXq0bJ3LQslR5KxiiVVbvd0Ygs6o48HFUwUJ5qg6hh18DKxn8OL4ZMvtJYDQyHtRB8dAxH7v7WRLfVrYbV9Lss8JfIvU5_8hUCzVyNoJyUE3mGGO1fI354qawPyqmKW-O4-F0_UWWjkk6o9B3jjfZ-10hePxAx8K3NrASTDCOcL-z_jEf-CmEYewXcqZu9TIjpYsvZOZzLvSS3QbNz2rIlnx90CLS8wotJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مورفی، سناتور آمریکایی: ایران امروز بسیار قدرتمندتر از زمان شروع جنگ است
🔹
جنگ با ایران یک بن‌بست نیست؛ یک فاجعه برای آمریکاست. علی‌رغم آسیب‌هایی که ما به ایران وارد کرده‌ایم، گزارش‌های اطلاعاتی نشان می‌دهند که آن‌ها هنوز اکثریت موشک‌ها و پهپادهای خود را در اختیار دارند.
🔹
آن‌ها همچنان برنامهٔ هسته‌ای خود را حفظ کرده‌اند و هر زمان که بخواهند، می‌توانند عملیات نظامی را در تنگهٔ هرمز از سر بگیرند.
🔹
بهترین راه پیش‌رو این است که ترامپ همین حالا محاصره را تمام و پایان جنگ را اعلام کند و امیدوار باشد که کشورهای دیگر بتوانند با استفاده از دیپلماسی مؤثر، راه را برای بازگشایی تنگهٔ هرمز هموار کنند.
@Farsna</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/435652" target="_blank">📅 08:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435651">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🎥
برداشت گل محمدی در شهرستان گرمه استان خراسان شمالی
@Farsna</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/435651" target="_blank">📅 07:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435650">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce2aWO-KfF0WgXQmT91_2CqL9cO9QMICdvba4UnyTQJEd3CPMHJSUrHBC27cB_PEgAD3eCIvQUs87cW3W4gkf1cT4GaxPCfUW1V54XpuaEf5TI2j9O3ynOU0lpmtj52Rg478pVrdvRQ9Fy38kNneqOr7vX3S4BLhu-iy9NFMQ0QOQxeOQ05InZxVWI3JCsUyxER0s1DCV2h-R_K1k46OrCOi3ri3jOYiTLigkzR-4TdXZXUSpfnmO7ewR98PM8Ld-6ygD6ml-1yv2cWCnp0BnDkUfDAvDVkUR_IZkGLIlaUASV2nGfUEovuT86xW_iOe4vrK5npWD-wK1Yxmrzp7rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط آزاد تولید اوپک پس از بسته شدن تنگۀ هرمز
🔹
سازمان کشورهای صادرکننده نفت (اوپک) تازه‌ترین گزارش ماهانۀ خود را منتشر کرد. این گزارش تصویری بی‌سابقه از کاهش تولید و اختلال در بازار نفت را ترسیم می‌کند.
🔹
تولید نفت اوپک به کمترین میزان در ۳۵ سال اخیر رسید و عربستان سعودی نیز با کاهش ۴۲ درصدی، تولید خود را به پایین‌ترین سطح از جنگ خلیج فارس در سال ۱۹۹۰ رساند. آمارها نشان می‌دهد کویت نیز بیش از ۷۵ درصد تولید خود را از دست داده است.
🔹
در این میان، خروج امارات از اوپک نیز زخم دیگری بر پیکر این سازمان وارد کرده است.
🔸
حالا با توجه به اختلال در تنگۀ هرمز و کاهش بی‌سابقه عرضه، کارشناسان انتظار دارند نوسانات شدید قیمتی در بازارهای جهانی هم‌چنان ادامه یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/435650" target="_blank">📅 07:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435647">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QbrzRO5KEp8AeirFJHVVqD_cls5G4hbdhxGFsXWkU8hQBo3sGmslK8m5M7GyAMhyiPR8QWzVIzVTxXAEzYx0ZErhM8hqqgcIWLBPIsNjYyz4oLd5zPCd06iC8dHf1rNz66jgiU1pmFeeBWACrJm0y07u8KHBuVvzz_Zk0TF7_5LXbdMsWIcSkZ2Y5i433wn4cD4uGA3oNGh_WkXZz_U39CgNo6WOboZkjiBQhpSBBBhQO4A8ql9GgzryCA48lkl_UJeJ7HtDg_LHpkBvtOc0gAAdeUoLMNl1849liiqv3rcyIQO3Z3adGualOtSNedLiiJMl9QuShlWnUqkjeqeLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AIo6RjuDrnXgXP0SpkodFs_Sws3Eu1NQcwpdPt87bvqTJEBlcyYIjWuhyGEMbUnACcE0KpxLjxohHdgIfLYV0A4p7kqYEWv_h0smYU0mfitrVa5RDqE16cdQC0rC9uX8zHUMTLDCjVdiIqbeT2UWMv-kIMyfT7vlVfuCtszl5jHhHIgTGcExXtgsDmpzBrXEovVEG5NnJJgQ600QpuwviBUvL7h_ivErZhEtYEZzkrUT1zT_ho0Yh6G5PIpWdyt7mfy4ZYTLoPZAIOINh9dH7nyVahHPbpFxeOFpPIoY0Kver_7HFOmValLr2CV5Mw3HcYQ5bZwzbfIJ1zfZ6Wns4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCbvK1ShaZlb46BjryCW-GTJIGFK9TmuoOoRf7A19jh-0wYIF3_6gaZkjhkncyXxAdpXQJDh7XwjLO88JaQupI8Xj0wvOtKpGAv1XDUOXfLMsSQZ1M61_rQ7UZ_r7gRxm8Rc6YfTxcpwmR_kNdF9i6Py3Q8hdw-K4BYUmSTB3pMKh__SWK8PInugLVkD5i9HG7TuArK51CXpOcgxcW-9XF5MX3hLGXSYZ5q_aoSku_j8icNdE1Ess4Y11MKOA7ucHpYsNayhNCQUacq5v8NXaR9Dd0TjTWDNG68Z1vtgs1BUyeLt0nWQjK3LLzKg037EA27FIx2aNOoSaT6gUClI6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار و گفت‌وگوی عراقچی با وزیر خارجۀ هند، در حاشیۀ نشست وزرای امور خارجۀ بریکس در دهلی‌نو
@Farsna</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farsna/435647" target="_blank">📅 07:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435646">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔹
کالابرگ سرپرستان خانوار با ارقام پایانی کد ملی ۷، ۸ و ۹ شارژ، و امکان خرید از فروشگاه‌های طرف قرارداد فراهم شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/435646" target="_blank">📅 07:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435645">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXDtIULT7kc2PR6Ak7Me_PKsbOK7YS3vvx3u8SesC9_0tdABrdgcAjNJAf5i-KRflKdEbYjaXIi_3VLL0fZt8UheyaQrWDYAe18k-WV9tNUJ5L8byInhzjc-P44prHGjSPKxjAcMhfZXF3DBteSUHBWNt_B9sTRoFdX8yK5XTRPGaab94kRMxlW6t33sEjJrBq_hOQ13HfmKJEf0uPLQ4en7YAcc7vwvUfwaUsmSKyYac82o5oygroX_mAv5uhd3KhUtbphcFSJb0fvOJOVZ-sICgWQWlDCUmkx5op92BUBaIMRM-QaklLXEe-T6DKAgAFy-dXQ6Gu1mVD14-ai2_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
خیانت به همسایه، پنهان نمی‌ماند
🔹
بقائی، سخنگوی وزارت خارجه: مَن خانَ في السرِّ، سيُفضَحُ في العلن. کسی که پنهانی خیانت کند، آشکارا رسوا می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farsna/435645" target="_blank">📅 07:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435643">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">همکاری یک اسرائیلی با ایران، بدون دستمزد و به‌دلیل نفرت از اسرائیل
🔹
پروندۀ یک فرد ساکن فلسطین اشغالی که بدون دریافت دستمزد و بر اساس نفرت از اسرائیل با مأموران ایرانی همکاری کرده مورد توجه رسانه‌ها قرار گرفته است.
🔹
«احمد دعاس»، رانندۀ کامیون ۲۷ ساله  متهم است که با انگیزه‌های ایدئولوژیک و ناشی از «نفرت عمیق» از اسرائیل، اقدام به جاسوسی برای دستگاه‌های اطلاعاتی ایران کرده است.
🔹
بر اساس ادعای دادستانی، او که به واسطۀ شغل رانندگی به نقاط مختلف اسرائیل سفر می‌کرده، تصاویر و ویدئوهای متعددی از مراکز حساس تهیه و برای یک مأمور اطلاعاتی ایران ارسال کرده است.
🔹
دادستان‌ها می‌گویند دعاس پیشنهاد مبالغ مالی را رد کرده و اعلام نموده که این کار را صرفاً به دلیل تعهد ایدئولوژیک به ایران در جریان جنگ کنونی و «نفرت از دولت اسرائیل» انجام می‌دهد.
🔗
متن کامل خبر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/435643" target="_blank">📅 06:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435642">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a9714e59.mp4?token=rvac1z8ITrl-nP1DG2xm0NYReBw4o4c9XCcHu04b4VB_NETcRyQ-AwE6Dpem31dutbZKIpHi0-B0ShJSEBeivxB1IXEK8l_aWMi5V6gH2ENvewjpQGKoGtoXhZ_ecVrwwdP-7ESEdzlS8fn1GK1Kf4-_Y2ehX7rp5Aat1_YtzjpiIFfUrXRTxDsPPVrUpEd6pOQ3y8Vs-lS-_OCzoLluJteYdnhwu_Dh6kcUCgdczy1d0APum4owyXQGZnVWK6UtHfGHa2GvMxGPE3FzSGRti9hzOQlAD90AsSbVf24w61-4xp31RGZVRwLnFC_ykyTldoCxFwfLS-G4vk8jO-te2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a9714e59.mp4?token=rvac1z8ITrl-nP1DG2xm0NYReBw4o4c9XCcHu04b4VB_NETcRyQ-AwE6Dpem31dutbZKIpHi0-B0ShJSEBeivxB1IXEK8l_aWMi5V6gH2ENvewjpQGKoGtoXhZ_ecVrwwdP-7ESEdzlS8fn1GK1Kf4-_Y2ehX7rp5Aat1_YtzjpiIFfUrXRTxDsPPVrUpEd6pOQ3y8Vs-lS-_OCzoLluJteYdnhwu_Dh6kcUCgdczy1d0APum4owyXQGZnVWK6UtHfGHa2GvMxGPE3FzSGRti9hzOQlAD90AsSbVf24w61-4xp31RGZVRwLnFC_ykyTldoCxFwfLS-G4vk8jO-te2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاکبانی که تلاش می‌کرد پرچم ایران را بالای بالا نگه دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/435642" target="_blank">📅 06:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435641">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epMiaYTZdSYjHnehRcGax4TrdGgwAZkKYh9opI7vBAK-sLV_IpJdxeUvMy8xisSCLpi7OwSMQnBL6O1c_EGvk19uaM_m8af_1BUmZu-Za4dbg1hnQmYltsDntuUO65UPwCOkXn0KcTuE-PNAJWcCdRX1HucK8IEmNWfy2fpkGIG10qPuXr5zuv6YnSjF1gwOVQOVtjvP58FZc-DwU7BKUpzXVG3WK_ZCf9OojlzTO661ohCTXKA-LCWLtcBc5NeC6nERnZpgJnIy95T91BG6GsGQcHwx52Jamvxpcwg1JOjZE-dJJC2RqFDHEL9WuI8jeEEZwVukmRQnGHqSYd7RLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران غول‌های فناوری در چین
🔹
وقتی هواپیمای حامل دونالد ترامپ راهی پکن شد، فقط یک هیأت سیاسی در حال سفر نبود؛ مدیرعامل شرکت‌هایی هم در این مسیر حضور داشتند که بخش بزرگی از آینده کسب‌وکارشان به تصمیم‌های چین گره خورده است.
🔹
از کارخانه‌های تولید آیفون و خودروهای تسلا گرفته تا بازار عظیم هوش مصنوعی و سفارش‌های چند ده میلیارد دلاری هواپیما، بخش مهمی از منافع این شرکت‌ها به پکن گره خورده است.
🔹
ایلان ماسک به‌دنبال خرید تجهیزات تولید پنل‌های خورشیدی از تأمین‌کنندگان چینی است. اپل هم همچنان وابستگی بالایی به تولید در چین دارد. انویدیا نیز به‌دنبال ازسرگیری فروش تراشه‌های پیشرفته هوش مصنوعی H200 در بازار چین است.
🔹
هرکدام از رهبران فناوری برای این سفر یک نیتی در سر دارند که جزئیات آن را
اینجا
می‌خوانید.
@FarsnaTech</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/435641" target="_blank">📅 05:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435639">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e37c5896c.mp4?token=frnGMQv6tAXJzty6nkHzQBuf4BAqZkL6lhqbs7Z6aaQyy_relNg-lg1hiunzwUpVHZeNF1hdiQsGshVaZZ-HowO5t8MTKfEOA9vVVpWOyr8GOdLuhpbL22aV0ZuoZvWWGCerUkJoBFS06oHVfjVcwzAwLPlRaBHFh6aVkO5XKN-xvzKxQlUPdDhV2bkdoczq599YVERAzs-_88mb0CtyQnnh6ZLIpiemEuXZY-igs6Cz50ZKUbpf1j-3a559nM7bZqd2CJ1k-F7dNPHEF9J7F63zGnaJbBYhp9SZR9AWzLmV_3UvhkyLi3Ig-Rba8MUG2egzY1MiM2D0dElNguyqRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e37c5896c.mp4?token=frnGMQv6tAXJzty6nkHzQBuf4BAqZkL6lhqbs7Z6aaQyy_relNg-lg1hiunzwUpVHZeNF1hdiQsGshVaZZ-HowO5t8MTKfEOA9vVVpWOyr8GOdLuhpbL22aV0ZuoZvWWGCerUkJoBFS06oHVfjVcwzAwLPlRaBHFh6aVkO5XKN-xvzKxQlUPdDhV2bkdoczq599YVERAzs-_88mb0CtyQnnh6ZLIpiemEuXZY-igs6Cz50ZKUbpf1j-3a559nM7bZqd2CJ1k-F7dNPHEF9J7F63zGnaJbBYhp9SZR9AWzLmV_3UvhkyLi3Ig-Rba8MUG2egzY1MiM2D0dElNguyqRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده سنتکام: ۶ کشور عربی در جنگ با ایران کنار ما هستند
🔹
۵ کشور خاص هستند که به معنای واقعی کلمه در کنار آمریکا درحال دفاع هستند: امارات، بحرین، کویت، قطر و عربستان.
🔹
هر آنچه انجام دادیم بدون اردن و همکاری نزدیک با اسرائیل غیرممکن بود. آن‌ها فقط مأموریت…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/435639" target="_blank">📅 05:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435638">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎥
به‌نظر شما، این‌روزها شجاع‌ترین و باشرف‌ترین آدم کیه؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/435638" target="_blank">📅 05:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435637">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تعطیلی موقت دریای مازندران، از شنبه
🔹
ادارۀ هواشناسی دریایی مازندران: باتوجه به مواج‌شدن دریا، فعالیت‌های قایقرانی، صیادی و گردشگری دریایی از اوایل روز شنبه ۲۶ اردیبهشت‌ماه تا اواخر وقت یک‌شنبه ۲۷ اردیبهشت‌ماه در دریای مازندران ممنوع شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/435637" target="_blank">📅 04:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435636">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNUG80s--DRgaI7mhdPnh-A1DA-y_stZDwn9t6Bl10CZMqWS2vYWhJRUHT4jVtdybP75wZo0uoT1WfixulJ4wCj2HRm9Ftc5PtVFC-w8hv8ThOoLJtbrMVcEzbzsqqpDr9K9rwFOfIFnpcHANKFNeyFbGJSwpcJUXJWvvV0t4HdHv2JpVmZFuHef8lTuN_53YEvO83_NGcrojWHh646kz2m0p2mP1L7ORlctqC7BOMp3bn3Ph8VCeVtvKulpmBATcAEm9YLsCEvBowhlmAP156RdlWhyv6F2G0dDvcHhGibwtW9ben8yL_zhw9gwMrDOvIK_Mx6skmJA-oUyv_n7wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرر هفتگی ۶۰ میلیون دلاری هاپاگ‌لوید از بحران هرمز
🔹
شرکت آلمانی «هاپاگ‌لوید»، که یکی از بزرگ‌ترین شرکت‌های کشتیرانی کانتینری جهان به حساب می‌آید اعلام کرد، تداوم بحران و ناامنی در تنگۀ هرمز، هفته‌ای بین ۵۰ تا ۶۰ میلیون دلار هزینۀ اضافی به این شرکت تحمیل کرده است.
🔹
به گفتۀ مدیرعامل این شرکت، محدودیت‌های ایجادشده در تردد دریایی، زنجیرۀ تأمین و حمل‌ونقل جهانی را با اختلال جدی مواجه کرده که بخشی از این هزینه‌ها ناچارا به مشتریان منتقل خواهد شد.
🔹
این شرکت پیش‌تر نیز اعلام کرده بود افزایش هزینۀ سوخت، تغییر مسیر کشتی‌ها، رشد هزینۀ بیمه و طولانی شدن زمان حمل‌ونقل از مهم‌ترین تبعات بحران بسته بودن تنگۀ هرمز برای صنعت کشتیرانی جهانی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/435636" target="_blank">📅 04:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435635">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4445eb560.mp4?token=CqUDzas-64kWsJsLsjxHkVUJ-LqtTe2kiC5vuaO5lPWaDOJqe_bKVmPAykbnMrX5TAPsoa8WfBBCDW-9_vt1U-yghDcqUXmLFv_0xMn286EFi4GpOj7zCIyEZKwb42rRJu3twlC49vBnG2uRbcGhiAOU6cmYdPdYgiZfcbc9JZb6wv_OykDYLbhlVqoWXuy5HQO8-bTgkz29lfPpfJfaPQBMId7eb-0m6abH8dDrMrORGb2bFIlPRnleAXK3QZi-RZkCEK7rBb1bmW7jriFleYi60BjVgqn_H3hdp93MPBfU0guYrMMeGQ7S2pF1WdyUZ4CPrePOKMMuryonfNsm1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4445eb560.mp4?token=CqUDzas-64kWsJsLsjxHkVUJ-LqtTe2kiC5vuaO5lPWaDOJqe_bKVmPAykbnMrX5TAPsoa8WfBBCDW-9_vt1U-yghDcqUXmLFv_0xMn286EFi4GpOj7zCIyEZKwb42rRJu3twlC49vBnG2uRbcGhiAOU6cmYdPdYgiZfcbc9JZb6wv_OykDYLbhlVqoWXuy5HQO8-bTgkz29lfPpfJfaPQBMId7eb-0m6abH8dDrMrORGb2bFIlPRnleAXK3QZi-RZkCEK7rBb1bmW7jriFleYi60BjVgqn_H3hdp93MPBfU0guYrMMeGQ7S2pF1WdyUZ4CPrePOKMMuryonfNsm1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غیرت و حماسۀ میبدی‌ها در میدان دفاع از ایران
@Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/435635" target="_blank">📅 04:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435633">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">درگیری فیزیکی مأموران مخفی آمریکا با مأموران امنیتی چین
🔹
شبکۀ فاکس‌نیوز گزارش داده در دومین روز از سفر رسمی دونالد ترامپ به چین یک «تقابل شدید» و فیزیکی میان مأموران سرویس مخفی آمریکا و نیروهای امنیتی چین اتفاق افتاده است.
🔹
شاهدان عینی گفته‌اند این درگیری روز پنجشنبه زمانی آغاز شد که ماموران امنیتی چین از ورود یکی از افسران مسلح سرویس مخفی به محوطۀ «معبد آسمان» جلوگیری کردند.
🔹
این اتفاق باعث بروز تنشی شد که ورود هیئت‌های همراه به محل مراسم را بیش از ۳۰ دقیقه به تأخیر انداخت.
🔹
خبرنگار نشریۀ تلگراف که در محل حضور داشت، این رویارویی را «بسیار شدید» توصیف کرد.
🔹
طبق گزارش‌ها، ماموران چینی اصرار داشتند که افسر آمریکایی نباید با سلاح گرم وارد محوطه شود، در حالی که آمریکایی‌ها معتقدند حمل سلاح توسط تیم حفاظت رئیس‌جمهور آمریکا پروتکل استاندارد و غیرقابل تغییر سرویس مخفی است.
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/435633" target="_blank">📅 03:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435632">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf2ce3d4e.mp4?token=nEMTAT3RtZBATH6R0wb7P2K4UmoeBc9w19ew-H5Xc3tzmy360MHqpWfqrnZle1GS8cw-7_y3Ucu-ri0f47BkmCRc2gBrg0lWOCALMepuGEr5nB2le76O7bBZSn5urxCRH6XSzxy09v-wKzERu57KdnZGYugn8-soA5GDF4pYY7B77mIyqY2BuPUMzQu-rpR7M6-HsoF4CjJ6sKAaOXjzT31iS4uKpI2ry8D2xlmxsZe00mt3ft2Dhj_zu-z1Vm0dMspQfZWdEovQG0GCyL_YOdMNy9dPBFPnyt2tZj-1ytuMMVD9fgwYz-Ev7UaaU3kj4D2T64-F31HARD2a5AbiIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf2ce3d4e.mp4?token=nEMTAT3RtZBATH6R0wb7P2K4UmoeBc9w19ew-H5Xc3tzmy360MHqpWfqrnZle1GS8cw-7_y3Ucu-ri0f47BkmCRc2gBrg0lWOCALMepuGEr5nB2le76O7bBZSn5urxCRH6XSzxy09v-wKzERu57KdnZGYugn8-soA5GDF4pYY7B77mIyqY2BuPUMzQu-rpR7M6-HsoF4CjJ6sKAaOXjzT31iS4uKpI2ry8D2xlmxsZe00mt3ft2Dhj_zu-z1Vm0dMspQfZWdEovQG0GCyL_YOdMNy9dPBFPnyt2tZj-1ytuMMVD9fgwYz-Ev7UaaU3kj4D2T64-F31HARD2a5AbiIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: هدف ترامپ از جنگ با ایران، تسلیم بی‌قید‌وشرط و تغییر حکومت بود که هیچ‌کدام اتفاق نیفتاد
🔹
داک‌ورث: ترامپ، تنها در عرض ۲ ماه اهداف نهایی متعددی را ارائه داده است؛ او از «تسلیم بی‌قید و شرط» و «تغییر حکومت» در ایران سخن گفته که هیچ‌کدام اتفاق نیفتاده است.
🎥
ترامپ گفته است که جنگ زمانی به پایان می‌رسد که سایت‌های هسته‌ای ایران نابود شوند؛ اهدافی که پیشتر در جنگ ۱۲ روزه ادعا شد محقق شده‌اند.
🔹
او گفته که هدفش نابودی کامل نیروهای نظامی و زیرساخت‌های ایران است، درحالی‌که جامعه اطلاعاتی ارزیابی می‌کند که این اتفاق رخ نداده است.
🔹
حالا او گفته است که هدف، بازگشایی تنگه هرمز است؛ در حالی که جهت یادآوری باید بگویم این تنگه پیش از شروع جنگ باز بود.
🔹
بنابراین وقتی نمی‌دانیم برای چه می‌جنگیم، قطعاً نمی‌دانیم تا چه زمانی خواهیم جنگید.
🔹
مقامات اطلاعاتی آمریکا معتقدند ایران به اکثر ظرفیت موشکی خود دسترسی عملیاتی دارد‌. ایران نسبت به قبل از شروع جنگ، کنترل بیشتری بر تنگه و اقتصاد جهانی دارد.
@Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/435632" target="_blank">📅 03:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435631">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f21a5aed.mp4?token=NY6J4dOwXznwbiS7N5n95JUw-yqAzzOn3_PD91vMUVB8xn7ZTIr09pxWs08FBN5lnaoOHAE1js38iXFMIOnmg9LMHgW7TLvWUhxTZSy84Pr0wf_lJNIhOtdMBzvd_ix4f_CONAoGhEWu0qrBqFKzP0JbgqXyJmtApzWibH_0_ZcaI5FEnYn1eyiD2E9uhndjV-wE8llhWYmN7VsjIWDyWGzeVo1WFt31NYnwypITNpJjHCs4ayPt2eKUQMA8V_GTc3zl7kEoq5gHQxrv7KIW52TH5-RcLBxbV01I1ur32FVFtBi9LJSNkP_FJJmKzCvMZIvl1GlEd7J5IJV8QJ_1Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f21a5aed.mp4?token=NY6J4dOwXznwbiS7N5n95JUw-yqAzzOn3_PD91vMUVB8xn7ZTIr09pxWs08FBN5lnaoOHAE1js38iXFMIOnmg9LMHgW7TLvWUhxTZSy84Pr0wf_lJNIhOtdMBzvd_ix4f_CONAoGhEWu0qrBqFKzP0JbgqXyJmtApzWibH_0_ZcaI5FEnYn1eyiD2E9uhndjV-wE8llhWYmN7VsjIWDyWGzeVo1WFt31NYnwypITNpJjHCs4ayPt2eKUQMA8V_GTc3zl7kEoq5gHQxrv7KIW52TH5-RcLBxbV01I1ur32FVFtBi9LJSNkP_FJJmKzCvMZIvl1GlEd7J5IJV8QJ_1Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غوغای قمی‌ها در شب ۷۵
@Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/435631" target="_blank">📅 02:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435630">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZzAHKlMSFytim4oPwEnG3eRTjRvHrtbLj-k0ZrDuIIV5r7FsuTurdp97nwddSfF2waR3VmoEf9_4WcLnTTJCfCic2thbHHAN00axaJ8pkKHWCjCRA3hCqG734hQTQl2Ttk16mu1VkIAjlXs3pQ95-SRQt8lIwu_TvoiiuN466gb1L6HhacG8FEYI-AZUG5dCb9RjEqC08ETpCWhNvrHF4Wrr0IreHQBpdZpvOFrBwRWn3MS8Iakkld8oSbZFrZpbVVw2BVbfTUiNt1z-ebYEIYT9MisPPZt-u57lvgYq8IDo0c-WROjmDqhOo_u3vbN7k8aHFS-MWG95LmbmuzIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسری بودجه، دلیل لغو مأموریت سربازان آمریکایی در لهستان
🔹
ارتش آمریکا روز گذشته در اقدامی ناگهانی اعزام بیش از چهار هزار سرباز و تجهیزات به لهستان را لغو کرد.
🔹
حالا پایگاه دینفس‌نیوز گزارش داده کسری بودجۀ ارتش آمریکا، یکی از دلایل اصلی تصمیم پنتاگون برای لغو اعزام ۴۰۰۰ سرباز به لهستان است.
🔹
درحالی که سناتور جک رید، عضو ارشد کمیتۀ نیروهای مسلح سنا کسری بودجۀ ارتش را حداقل دو میلیارد دلار عنوان کرده، شبکۀ ای‌بی‌سی نیوز گزارش داده مقامات ارتش رقم واقعی کسری بودجه را بین چهار تا شش میلیارد دلار اعلام کرده‌اند.
🔹
پنتاگون پیش از این هم اعلام کرده بود که قصد دارد حدود پنج هزار سرباز را از آلمان خارج کند.
🔹
به گفتۀ مقامات، این اقدام سطح نیروهای آمریکایی در اروپا را به سطح قبل از تهاجم روسیه به اوکراین در سال ۲۰۲۲ بازمی‌گرداند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/435630" target="_blank">📅 02:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435629">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1967133bbe.mp4?token=VT0i0lTpfPPtQz7AWxnx3dqGKlqt3btK5-0r5DpXgOKTpQAU26Vee1fBlRkZ19KT4ydQkpSrAxqlz4NVxSg2AuAHwhijtLFmWqaKe7q3IzJA34nIXI0Lo_vpVcQ6N6ne8-GswLP8IVVEftAmvZA3jRwIzAA0bihsEJp9SNgq_sMMbbmi1XWlV-J-61k5FiqWFiCE2VtmdqKycazo5CUJFWsUGeJZ0cACHkrP4oMvpyXGOYY2eOD2eLxHpasWMqTWwDHaWCwba3uqZI7t6yndEPr11fUmvqqTu8B-NnZZiFdutEbavbpXsrfxKSPu8tkrM2eeQi1N75GS04TYjXsqPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1967133bbe.mp4?token=VT0i0lTpfPPtQz7AWxnx3dqGKlqt3btK5-0r5DpXgOKTpQAU26Vee1fBlRkZ19KT4ydQkpSrAxqlz4NVxSg2AuAHwhijtLFmWqaKe7q3IzJA34nIXI0Lo_vpVcQ6N6ne8-GswLP8IVVEftAmvZA3jRwIzAA0bihsEJp9SNgq_sMMbbmi1XWlV-J-61k5FiqWFiCE2VtmdqKycazo5CUJFWsUGeJZ0cACHkrP4oMvpyXGOYY2eOD2eLxHpasWMqTWwDHaWCwba3uqZI7t6yndEPr11fUmvqqTu8B-NnZZiFdutEbavbpXsrfxKSPu8tkrM2eeQi1N75GS04TYjXsqPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
هفتمین رأی‌گیری سنای آمریکا برای پایان جنگ با ایران شکست خورد
🔹
مجلس سنا برای هفتمین‌بار قطعنامهٔ پیشنهادی برای توقف جنگ با ایران را رد کرد.
🔹
جمهوری‌خواهان تقریباً متحد عمل کردند تا اولین تلاش از زمان عبور ترامپ از ضرب‌الاجل ۶۰ روزه برای دریافت مجوز…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/435629" target="_blank">📅 02:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435628">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b9997533.mp4?token=sf1tAU-g7vzuN4j8TTzd3s3XfyMy_8EJ9Oc1y4tgy3Sgt4GW43Oe1Bv8UHguAW9NrqddOwtYCK4HWcOZmnxpkY3_x3IXsga-99bk2ton8RFWtuNSuXohK2Xe8dEVPMZjhV4yxpBNQMMXXhDRl1dq0zxsK1Y3oyQttxkq7N91o-5dCP6Hdy-sDXB8IlB54Plk6MgSnI5pZGp7laLgzxi7V2bxuBChMEQXhpkHQlsZGO5gKUtcc7JoTlDspXuqMLDhzfwxT_aRCCiysVi9aW-s1bdLgBniKckNTJG7AFCZFXFx_Yrciid3cnaT0yKhc6MvgwdqggQsTCUJdjSBIofTMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b9997533.mp4?token=sf1tAU-g7vzuN4j8TTzd3s3XfyMy_8EJ9Oc1y4tgy3Sgt4GW43Oe1Bv8UHguAW9NrqddOwtYCK4HWcOZmnxpkY3_x3IXsga-99bk2ton8RFWtuNSuXohK2Xe8dEVPMZjhV4yxpBNQMMXXhDRl1dq0zxsK1Y3oyQttxkq7N91o-5dCP6Hdy-sDXB8IlB54Plk6MgSnI5pZGp7laLgzxi7V2bxuBChMEQXhpkHQlsZGO5gKUtcc7JoTlDspXuqMLDhzfwxT_aRCCiysVi9aW-s1bdLgBniKckNTJG7AFCZFXFx_Yrciid3cnaT0yKhc6MvgwdqggQsTCUJdjSBIofTMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بامداد شب هفتادوپنجم، و میدان‌داری تهرانی‌ها در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/435628" target="_blank">📅 01:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435627">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUdtDkKdrsmKMV1zOSj-qmRK_LctZ71Cr7yhDqnxt01evptChNikQI8-2flDbHEztUmOY8A8nAXxqGAW3rmzuyf1sNhN9xdLm6qz7lKQerqE4AjslVgHEADshFWcOtYzB6fJ_diFGBKLHXxLO1kw0v2Ydh-60nEKmHZMmA7irFGoXlHoU1fACOqIPqkACWXxRCjvOCAL9Qoq5YcXKnWU6bBujzdd1mV5hsmN26w4TeKktXwsMQW5KkuexKSvxyXZ6anDGIRJI0mY8LAFOAn2wYSkpHg2HaJzzle8L-CtY8FFEGuvp97w7RkAboM97q0XSpMeDK9MrDUBIlNvscSEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام موافقت ترامپ با نظر چین در خصوص افول آمریکا
🔹
دونالد ترامپ در پیامی در شبکه اجتماعی تروث‌سوشال گفته که با سخنان رئیس‌جمهور چین که آمریکا را «کشوری در حال سقوط» خوانده بود موافق است.
🔹
ترامپ با وجود این حساب خودش را از سخنان شی جین پینگ جدا کرده و مدعی شده که منظور او آسیب‌های دوران ریاست‌جمهوری «جو بایدن» به آمریکا بوده است.
🔹
ترامپ نوشت: «وقتی رئیس‌جمهور شی با ظرافت تمام به ایالات متحده به عنوان کشوری اشاره کرد که شاید در مسیر انحطاط باشد، منظورش آسیب‌های عظیمی بود که ما طی چهار سال ریاست‌جمهوری "جو بایدنِ خواب‌آلود" و دولت او متحمل شدیم؛ و در این مورد، حق کاملاً با او بود.»
🔹
ترامپ دوران حضور ۱۶ ماهه‌اش در کاخ سفید را «درخشان» خوانده و گفته منظور شی جین پینگ آمریکا در این دوران نبوده است.
🔹
ترامپ در پایان نوشته است: «دو سال پیش، ما واقعاً کشوری در حال سقوط بودیم؛ در این مورد، من کاملاً با رئیس‌جمهور شی موافقم! اما اکنون، ایالات متحده جذاب‌ترین کشور در تمام جهان است.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/435627" target="_blank">📅 01:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435626">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34b785d46e.mp4?token=qZqj8l_OUZ7D1hlpO0qbe8CcakMUNyQvOm_ZjXHIRy01J-viv-dxP03T4HCEeVePCBohTYDJR1c8Kiq0KYmVJzbncZfWX9A8AdxkXFnFUv-aLEJiAxkUy_337j6uFJC3q441W17mo8iA9IbrHhJHcmpzJ9If4uB_dJoVXgSx5S9cXZT14qamU_WaIzp9nQ-hA3i-KhpUxFQk331vW7O_CSdOiXVdMcHQQF7AbzkP9fb4Wht8UPs9bgovo2m4jjBGNg_zCpUyMfKVX3CSzb7Ow5wjrDdjHE84srYRtANmKRSDi1kq39zOTpbixaAHr_6TnBtOQ3H15hLh8--lTGbpEa4ibjWcZzV46X0g6LmIYkVXWpbVmT4vucAxKU6xc6ejoWAkAVx38TBJLLdwt7LWFRDhaJzYXTHSLuvKFzCCkuf2e5kgHSYyGr3WDghL0t1UdMPy_lkqu7EBnVA8trQH1xxtgnSWBahTNAaB7ED6wvxMV7lxpbNi8KrZbU9g6f39gCYaf0YEfmtSQ12h6qMwRX9esjs_ngJdOBPFEQVENIlg9SPdepktTFGN0NSi8TM6spi2LVsdMOCyKOlQkRzSvC6caL4WdWGEuh_LmR82UHPIT0C2D5dF2pmVz5VWCY_InT1_0jwulCbIDlzpiGCRipBt50e_3tbA2oDfgYhCI4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34b785d46e.mp4?token=qZqj8l_OUZ7D1hlpO0qbe8CcakMUNyQvOm_ZjXHIRy01J-viv-dxP03T4HCEeVePCBohTYDJR1c8Kiq0KYmVJzbncZfWX9A8AdxkXFnFUv-aLEJiAxkUy_337j6uFJC3q441W17mo8iA9IbrHhJHcmpzJ9If4uB_dJoVXgSx5S9cXZT14qamU_WaIzp9nQ-hA3i-KhpUxFQk331vW7O_CSdOiXVdMcHQQF7AbzkP9fb4Wht8UPs9bgovo2m4jjBGNg_zCpUyMfKVX3CSzb7Ow5wjrDdjHE84srYRtANmKRSDi1kq39zOTpbixaAHr_6TnBtOQ3H15hLh8--lTGbpEa4ibjWcZzV46X0g6LmIYkVXWpbVmT4vucAxKU6xc6ejoWAkAVx38TBJLLdwt7LWFRDhaJzYXTHSLuvKFzCCkuf2e5kgHSYyGr3WDghL0t1UdMPy_lkqu7EBnVA8trQH1xxtgnSWBahTNAaB7ED6wvxMV7lxpbNi8KrZbU9g6f39gCYaf0YEfmtSQ12h6qMwRX9esjs_ngJdOBPFEQVENIlg9SPdepktTFGN0NSi8TM6spi2LVsdMOCyKOlQkRzSvC6caL4WdWGEuh_LmR82UHPIT0C2D5dF2pmVz5VWCY_InT1_0jwulCbIDlzpiGCRipBt50e_3tbA2oDfgYhCI4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه حضور مردم کوار فارس و علم‌گردانی در خیابان‌های شهر
@Farsna</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/435626" target="_blank">📅 01:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435625">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzkPrjXNoylrpW7eMWKPxG-cSZZ7aiLz3MXtcphJ8M0Rb9rF3D419rTp-j13e5x1i2CSm5Z_7WpBsMdPVC08euMX2ujwL9KuOloCuxLoezJv4S6ZvJJn_qmccKynzw09czMtj9MSnpAWC9BSmlTC8NEqgq66-iaK_kwJMMOc_A4y7gM8CtTM_TFVdcwJ4tI732rJ7MTudFzLFevOycFkRV4gis3CwGV4SPw-I1KgkflIOr6HE1EX4-K5ETxNSM_26wr_1XB9HvHIVHLiPZnQ2TveyniQ6M6ZIEXTrd9nWjBns3kX1jQoKcf2jlHx2xXxpUvZvi4FHdneHeICZ_etjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شناسایی ۶ هزار موتورسیکلت احتکار شده در آمل
🔹
دادستان آمل: یک کارخانۀ تولیدکنندۀ موتور سیکلت در آمل، با سندسازی و صدور بارنامۀ جعلی اقدام به دپو و احتکار ۶ هزار دستگاه موتورسیکلت کرده بود.
🔹
این انبار با موتورهای احتکار شده پلمب، و پرونده در دست بررسی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/435625" target="_blank">📅 01:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435624">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307d27fbb1.mp4?token=sKUMENr83-3T_8_NDXZ5yal7k5Hk7gaMp6-xCEkkIJKy3io0ECj_g0jNfE7h2Qaxhq-CBFhd7xCF5JcI4Z0gl4T4HyLx4LSoVMKXgY8uivQji7CAbYSsNR_ke0N9b4FkPBCN3ho8US54tiGcnuV53nJfa6DNV3802IWHTB6EsJZCSP6jLDjuio4FjkMaLQQW8d7-2TQG5AzSvTxhxJPgPCfh8KK3oE_VoRk4MZmQhwBbjz6kTK3HbtkO_xVAaFxAn27r-E6E2nZQ9tozEwM8fq6VPCqfNrLC_tf2t7c_jbAdp4Nr9DNHt_UMZkPJkuMCmC46QKjBLraP_tX6o8JuNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307d27fbb1.mp4?token=sKUMENr83-3T_8_NDXZ5yal7k5Hk7gaMp6-xCEkkIJKy3io0ECj_g0jNfE7h2Qaxhq-CBFhd7xCF5JcI4Z0gl4T4HyLx4LSoVMKXgY8uivQji7CAbYSsNR_ke0N9b4FkPBCN3ho8US54tiGcnuV53nJfa6DNV3802IWHTB6EsJZCSP6jLDjuio4FjkMaLQQW8d7-2TQG5AzSvTxhxJPgPCfh8KK3oE_VoRk4MZmQhwBbjz6kTK3HbtkO_xVAaFxAn27r-E6E2nZQ9tozEwM8fq6VPCqfNrLC_tf2t7c_jbAdp4Nr9DNHt_UMZkPJkuMCmC46QKjBLraP_tX6o8JuNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید حاج قاسم سلیمانی: فضا را برای همه نوع آدم‌ها باز کنید
🔹
خواهشم از خواهران و برادران متدین این هست که فضا را برای همه نوع آدم‌ها باز کنید؛ بگذارید همه نوع‌ها بیایند؛ بعضی از افرادی که ظاهرشان شاید ظاهر مناسبی نیست اما باطن خوبی دارند.
@Farsna</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/435624" target="_blank">📅 01:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435623">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎥
موج هفتادوپنجم حماسۀ مازندرانی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/435623" target="_blank">📅 01:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435622">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/255f024260.mp4?token=tR_UOp_vVQaknk0VsFCyUKYPZSA6Olo4QujTdmGObn0P4YoNd-WJVVkX7UKtHXT2l1fMW2_ETci8s7ifx1qYkwxHacNiFs6A634OJxxPuSgXjpiI4PMO3dE70CDYZtxI-oXzTmf94VhRVAcNz8YdrpkyC4-FufQzpIjDEpbaW3wzC2X6a83G5In4t6t9dun2lxRVIMs0GFCCKTcL4gM25rny5C-5Y89A_8NJZsuUSL0Ovh52n3AOhhPIrlfcxmySGmxnLbcE9lZVJF7G8PJ5bkatHfNbo3e-TUpLyDNKBvnOHG_5XEh45kIAq5K5nkSyz4DKoR3oM27ThHcnCsEPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/255f024260.mp4?token=tR_UOp_vVQaknk0VsFCyUKYPZSA6Olo4QujTdmGObn0P4YoNd-WJVVkX7UKtHXT2l1fMW2_ETci8s7ifx1qYkwxHacNiFs6A634OJxxPuSgXjpiI4PMO3dE70CDYZtxI-oXzTmf94VhRVAcNz8YdrpkyC4-FufQzpIjDEpbaW3wzC2X6a83G5In4t6t9dun2lxRVIMs0GFCCKTcL4gM25rny5C-5Y89A_8NJZsuUSL0Ovh52n3AOhhPIrlfcxmySGmxnLbcE9lZVJF7G8PJ5bkatHfNbo3e-TUpLyDNKBvnOHG_5XEh45kIAq5K5nkSyz4DKoR3oM27ThHcnCsEPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جو کنت، مقام مستعفی دولت ترامپ: وزیر خارجهٔ آمریکا گفته‌ که ما مجبور بودیم به ایران حمله کنیم چون اسرائیلی‌ها قصد انجام این کار را داشتند
🔹
در واقع اسرائیلی‌ها به ترامپ گفتند اگر او رهبر ایران را ترور کند، مردم ایران قیام می‌کنند و حکومت را سرنگون می‌کنند و این اتفاق بسیار سریع و آسان رخ خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/435622" target="_blank">📅 01:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435621">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d283bf7bc4.mp4?token=MNNbZymfWkgEthxaYOjr-DmfQB0qgX61QxjTmj_BGmXgbVlDA4iK5hJu0TLGc0IavM_xUxvhIiQqHwxlvYklj2RABxluVjPw4KYEMWSwX8zoAhp9x4pAmS0_ZzagmX9dm-hySw2XaH-WkemlCXxa153EK0ToMpQipswhNinV3fwHWcg8WGd8aUUhVRmMf-rOnvyG1axbWaYf5wOAR9YFDWxyjE_OtXN2kmiR0CPGpP4pB3OH9eHubzEwvZXqExu-z1oTabY-qaWbHwQ_8yrT9gcdfAEfXFV-U9MRq831UcgnPD51v8NyaWbZhF64T9hfkF4bNaPSu6PzLijlhbjiRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d283bf7bc4.mp4?token=MNNbZymfWkgEthxaYOjr-DmfQB0qgX61QxjTmj_BGmXgbVlDA4iK5hJu0TLGc0IavM_xUxvhIiQqHwxlvYklj2RABxluVjPw4KYEMWSwX8zoAhp9x4pAmS0_ZzagmX9dm-hySw2XaH-WkemlCXxa153EK0ToMpQipswhNinV3fwHWcg8WGd8aUUhVRmMf-rOnvyG1axbWaYf5wOAR9YFDWxyjE_OtXN2kmiR0CPGpP4pB3OH9eHubzEwvZXqExu-z1oTabY-qaWbHwQ_8yrT9gcdfAEfXFV-U9MRq831UcgnPD51v8NyaWbZhF64T9hfkF4bNaPSu6PzLijlhbjiRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیعت مشهدی‌ها با مشت گِره‌کرده
@Farsna</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/435621" target="_blank">📅 00:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435620">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎥
مردم شهرکرد، ۷۵ شب در سنگر خیابان
@Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/435620" target="_blank">📅 00:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435619">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cv9pVA5Snkb_Rb69QETrYBnlzeIFkqm_Twn6Ja7XASGeGnMc4E0qDLFGWH8--dyAp4lZ9W4fZbdHFyS3QTlyS7yUMi6Lq2-9y9uyRiDwtarkhIPAxBRI4IscKDmue37i2e9w2V7sSWgHdTlBAiyVjETw9zOWoH9xuexvgqC4oxioYqJ-syAZkxmMxd9xEyCCo6hij2y1KP0NRDwC_Y21nxBL_s-6hwktFnPQp9PvyiDK0LCn8XwyLZWDYeeODxY61TWbdmSV8DWBOz8FKd30BZO19l3LK4ttBaUHsSUGZVc7YIpdjIWlzV01Pgdv9pkrybkke-Ubpkee04VNkxCFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از شهادت پدرم فهمیدم «شهیدان زنده‌اند» یعنی چه
🔹
فرزند سرلشکر شهید اکبر ابراهیم‌زاده در گفت‌وگو با فارس: پدرم همیشه می‌گفت «اگر احساس کنم جایی به من نیاز است، وظیفه دارم که به آنجا بروم.»
🔹
او برای این منظور، حتی علایق شخصی‌اش را هم کنار گذاشت. بعدها که بزرگ‌تر شدیم، از او ‌پرسیدیم «روحیۀ شما به نظامی‌گری نمی‌خورد، چه شد که این مسیر را انتخاب کردید؟» او پاسخ داد «گفتند به نیرویی مثل من نیاز است و اطاعت کردم.» فکر می‌کنم روحیه ولایت‌مداری و تکلیف‌گرایی او باعث شد چنین مسیری را انتخاب کند.
🔹
مهم‌ترین ویژگی اخلاقی پدرم «مهر» و «رواداری» بود. او هیچ‌گاه به ما اجازه نمی‌داد درباره کسی بدگویی کنیم یا قضاوت ناروایی داشته باشیم. حتی اگر با فردی اختلاف نظر سیاسی داشت، باز هم نمی‌گذاشت درباره او با بی‌احترامی صحبت شود.
🔹
پدرم نسبت به استفاده از امکانات اداری یا دور زدن قانون، فوق‌العاده حساس بود، هرگز اجازه نمی‌داد از موقعیتش کمترین بهره‌ای ببریم و حتی از ماشین اداره استفاده شخصی کنیم.
🔗
ادامه گفتگو را
اینجا
بخوانید.
@Farsnart</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/435619" target="_blank">📅 00:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435616">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zs6C9F8rk7Uq7nXEVoRSQJk2L9c6StdRmpMo5nxgHAdBy_sNgfK63bKak2jZ3lG9G1FOmwF_xChFFUHLtM9dS1CU34IBB5s_8CMMwYInOF6EegykQSG69od0_Q5YIbICtKw6GvwyuC8sac6mQusjrgytRJ9494y62dm22gIogg1KuuwshF3rYA1KG3DAUkDUP8ijV-I5Wp6GeJ3h4g2yiBhoRsCJGjP2KjUdFA-YBfEkfukIxu2Cuyd8LAzP2RuQ2aANyGdCg2cO1lCsZwxreJ-HeKPzmIjI2rz0Nad6Ubp3skbuwZlBgnvZzVK4MzA3Fmdz0pXOvhJUfqh_-v1UJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBw4W_dgeTwWX57Stiz4lN7qnw5bNJSoChLTph-E8uTgUzQSAQoF4BV56XLc2uxddvx3KiafWPFD7LEKW5l5rLgTcMZwuLQx1hWxrVXCxlXS6PiiidtZpaFN1H6KYG37bz0cMNO1ye5AreYoOGFD1hc_fQFZEDokyWhjs14fbTlmn-GhbgqBLMlG3I004OuUWvA_KbipZKn7LPrqxShoEvEUTClPYk2fSxxaZ-PTHy_vUEPecVbmQSlvfuDIqbdnea7vU23GhI8gJR263rGD48W7TP5PlZlZIOJWwLzeIE6curEV8s6CMO-zrp_riIPLpF10h6A769a7e8Sb4aTzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/izYwCmZTsZOyWKiWg_3GTxIFDZ7-nHvMHiKR60FHkeXYyFtf9YkPj2GaYLm0DhqWjVnFbaxz9rUZY_ixzPU1GluOrNYUzwo0ic6WeQfIVJF65H72gsEBAv2Uu70rp5gzqjiOWZCV4L5TxCR_2HYs0WNo6zAfFxPY01Gy5A61oUozzb-WpIdJq2jVC_j7W_EpyPkSHFl2A63JxWbpgfY6nEG079-3cO1j_k91wSIwAr_1wihhbxh0sQTxl2W4JRXyfrftu2B8UJc7VoXNzAvFqggjNM3Z6D_3hCipF8DQyrWhfNINHmoC11KnaV50mqHQnJDbEahpuWWxVjBD0qE8nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حنظله: مغز متفکر سفر نتانیاهو به امارات و معمار اصلی توافقات ابراهیم هک شد
🔹
گروه هکری حنظله اعلام کرد که با هک «ساموئل شای» طراح سفر نتانیاهو به امارات و معمار پیمان‌های ابراهیم، شبکۀ مخفی او را افشا کرده است.
🔹
به گفتۀ این گروه هکری، شای نه‌تنها هماهنگ‌کنندۀ اصلی تمام توافقات پشت‌پرده میان رژیم صهیونیستی و کشورهای حاشیه خلیج فارس است، بلکه تسهیل‌گر کلیدی روابط پنهان اقتصادی، سیاسی و امنیتی میان تل‌آویو و ابوظبی محسوب می‌شود.
🔹
براساس اسناد منتشر شده، شای، اپستاین را به «سلطان احمد بن سلیم» معرفی کرده و از این طریق بسیاری از حاکمان فاسد امارات در شبکۀ اپستاین گرفتار شده‌اند. موساد نیز از همین مسیر برای وادار کردن آن‌ها به پذیرش خواسته‌های خود استفاده کرده است.
🔹
گروه حنظله اعلام کرد امروز ۲۶۵ صفحه از تماس‌ها، شرکای مالی و ارتباطات محرمانۀ شای را به طور کامل در وب‌سایت خود منتشر کرده و تمام اطلاعات مرتبط با شبکۀ مالی او در کشورهای مقاومت را در اختیار سرویس‌های اطلاعاتی کشورهای دوست قرار داده است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/435616" target="_blank">📅 00:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435614">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f20e0ec79.mp4?token=NHCT0_JP_mZvk0Iol2HO422q3lhTPJcU_cPI9peR5x82i5pPc5jGx9CLcm-n0iovWj26I-atYEQ5lmtGqyYupmc7091kBe7gpGqTtRVOmhruw9zDw9YbAdds3KYUUmoAXjS0r-taa2XH_3cDpX1vQ_iMxKgw9x9x93YQOJZpsz9l2A7r76r9o-BLnhVXbJg4Oz4ziet1CvynWEZYiIVpSprFM7kLkuSToJDwaWqYdHxaBowNDWaqi8rDwkRttDVfDt_0oDrl4rRo7sHUVOeqtcYeU1MYoDvUvAiHWzXNbFuR008NEvFcUVN8BiuBDnTrIEMBXbzSAZD_RbXU3FIOkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f20e0ec79.mp4?token=NHCT0_JP_mZvk0Iol2HO422q3lhTPJcU_cPI9peR5x82i5pPc5jGx9CLcm-n0iovWj26I-atYEQ5lmtGqyYupmc7091kBe7gpGqTtRVOmhruw9zDw9YbAdds3KYUUmoAXjS0r-taa2XH_3cDpX1vQ_iMxKgw9x9x93YQOJZpsz9l2A7r76r9o-BLnhVXbJg4Oz4ziet1CvynWEZYiIVpSprFM7kLkuSToJDwaWqYdHxaBowNDWaqi8rDwkRttDVfDt_0oDrl4rRo7sHUVOeqtcYeU1MYoDvUvAiHWzXNbFuR008NEvFcUVN8BiuBDnTrIEMBXbzSAZD_RbXU3FIOkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طفرهٔ فرمانده سنتکام از پاسخ‌گویی دربارهٔ پیش‌بینی بسته‌شدن تنگهٔ هرمز
🔸
هیرونو، سناتور آمریکایی: پیش از اینکه به ایران حمله کنیم، آیا این فکر به ذهن شما خطور کرد که ممکن است ایران تنگهٔ هرمز را ببندد؟
🔹
فرمانده سنتکام: یکی از مسئولیت‌های من ارائه طیف گسترده‌ای از گزینه‌ها همراه با خطرات و فرصت‌های مرتبط با آن‌ها به وزیر و رئیس‌جمهور است. فکر می‌کنم صحبت دربارهٔ اینکه آن گزینه‌ها دقیقاً چه بودند، نامناسب باشد.
🔸
هیرونو: بسته‌شدن تنگهٔ هرمز توسط ایران به ذهن شما خطور کرد؟ بله یا خیر؟
🔹
فرمانده سنتکام: تقریباً ۱۰۰ بار از تنگه عبور کرده‌ام. من تقریباً هر روز به تنگهٔ هرمز فکر می‌کنم.
@Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/435614" target="_blank">📅 00:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435613">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679e1ebcfa.mp4?token=tC6fBWTvQjdLrgJH75Pp2QNpfHU3JReCDG2ElIsGR-j3iaX3yed2j-A3LVUzSoNxkis404AHuJY9aZPJXLGGqP2m4nLG8woJEZsetlv51dQRJxp7aUGYyzx7jk08gP033zUP8GNSPNTinyuptvOq2h4ZIsgDO4UhAGe2_dz8I-r_g__Vvg4ooUlHMhv-E3j-w4RcJr7si14woHCiQRE9LNSWdfLArU1MP1rjweOaA3TKseKHFBFCeey-yS_8pBIXloVFHNB-jSVx8URKdxVrxOkBsF7VXcaS-a2vjOaS5mqzkrlG0wGaq3GvLdzgYDVAXF_St0qSQYx8GKWRSZZcgatAV0Mv2pCI8uJ7DC9NHXYNLyfL9QXMi-jdjtbHw6h7JGSFq-gSewItqbDcuWDc0hzXqwLnQ4WawHTSML_gFx5zqq_2z0bt0jjwxxC8b70eRVxoqMEV6vnlXmLm0tnXqC8u4BU_vPvIxE0XzlGOlWL7H5b3t_Eov5MkMzyL-tX5cvG-7cCjZdZwg4CvQSCYeMKTTU-nmdk1SpgdIGiz5_TsrgRGRe1RcfMPfKmZqj1OuXapjc-5qgkciaEw-DXGVPWxoB4K096NBZKpJjZwNKMp2SlX11ZUZ-IuJZERdlT8K7h1hZAW5WihiLeDKKMCsiGmzDzE4ksiVL9ejouL9SY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679e1ebcfa.mp4?token=tC6fBWTvQjdLrgJH75Pp2QNpfHU3JReCDG2ElIsGR-j3iaX3yed2j-A3LVUzSoNxkis404AHuJY9aZPJXLGGqP2m4nLG8woJEZsetlv51dQRJxp7aUGYyzx7jk08gP033zUP8GNSPNTinyuptvOq2h4ZIsgDO4UhAGe2_dz8I-r_g__Vvg4ooUlHMhv-E3j-w4RcJr7si14woHCiQRE9LNSWdfLArU1MP1rjweOaA3TKseKHFBFCeey-yS_8pBIXloVFHNB-jSVx8URKdxVrxOkBsF7VXcaS-a2vjOaS5mqzkrlG0wGaq3GvLdzgYDVAXF_St0qSQYx8GKWRSZZcgatAV0Mv2pCI8uJ7DC9NHXYNLyfL9QXMi-jdjtbHw6h7JGSFq-gSewItqbDcuWDc0hzXqwLnQ4WawHTSML_gFx5zqq_2z0bt0jjwxxC8b70eRVxoqMEV6vnlXmLm0tnXqC8u4BU_vPvIxE0XzlGOlWL7H5b3t_Eov5MkMzyL-tX5cvG-7cCjZdZwg4CvQSCYeMKTTU-nmdk1SpgdIGiz5_TsrgRGRe1RcfMPfKmZqj1OuXapjc-5qgkciaEw-DXGVPWxoB4K096NBZKpJjZwNKMp2SlX11ZUZ-IuJZERdlT8K7h1hZAW5WihiLeDKKMCsiGmzDzE4ksiVL9ejouL9SY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین «حیدر حیدر» در اجتماع هفتادوپنجم مردم رفسنجان
@Farsna</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/435613" target="_blank">📅 23:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435612">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDF8lJFHRfpd5uW4QTdoGyBC_rd21yaSigxZ9aE331P9szWJS52DqQGEGx7cPmg1s1fKV7hKvEXxl8mnrgx9zc-BSOCLAA7JlQF2c_IiIp-fa0AGoY2Jw_QeOkahAVXPCtvxHToHpXV_gXvCXtxR4EkZqJgxXeehOfii60pJ2zRM-0i8ZyayYpcJAOo1SUjTMPr2gxlkQA858IbCbHWjEP8JOj651G0PwKrv42UyfBFMe91MOvnY4Lahy-UafJJ16nwuZbsQztorSkzwFm2Msxe5nTi8CfhtUo5dKajrsg39_yedlxJVlK2QNr0zpFcGj3U3XCcLmhbGQJREzfmNcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: حداقل ۱۰ دانشمند آمریکایی کشته یا ناپدید شده‌اند  سلسله این حوادث از سال ۲۰۲۳ آغاز شد:
🔸
مایکل دیوید هیکس: دانشمند ۵۹ ساله آزمایشگاه پیش‌رانش جت ناسا (JPL) که در جولای ۲۰۲۳ درگذشت.
🔸
رانک مایوالد و مونیکا رضا: دو متخصص دیگر از JPL؛ مایوالد در سال…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/435612" target="_blank">📅 23:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435611">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c010d4779e.mp4?token=YaM1-jKB8nq5POZs-y-7GkK4LNfIA0IAOhyfxjlTVKRgcTeFCZN4w97qPBG7NRSqo7rWqd5ouVggVEDBC4tvQrJoxHpEUWcyPnj-gS0636ZvpwWJ35HCfGxmS0wGFcfFwpA0W19R7B4FSAKH5jQ-UYMqoO4l37F9qQIrlKjYCPj9tRqE5_nsTKK9rHUwXiAV5dh5VOLOELBwH8GvaMUUhLCdqmSGA_Ogg19EplW__gIGEs7rfhKkvHUlUoFxAK3JSXOMJ-HGLI3ZSu3KSHUsikr0oCzIqBNCwkMfLMR-xZVIjDx-B2GemGOL6Q3XG6C8nNUrd0pNTJybVvgk4-Md9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c010d4779e.mp4?token=YaM1-jKB8nq5POZs-y-7GkK4LNfIA0IAOhyfxjlTVKRgcTeFCZN4w97qPBG7NRSqo7rWqd5ouVggVEDBC4tvQrJoxHpEUWcyPnj-gS0636ZvpwWJ35HCfGxmS0wGFcfFwpA0W19R7B4FSAKH5jQ-UYMqoO4l37F9qQIrlKjYCPj9tRqE5_nsTKK9rHUwXiAV5dh5VOLOELBwH8GvaMUUhLCdqmSGA_Ogg19EplW__gIGEs7rfhKkvHUlUoFxAK3JSXOMJ-HGLI3ZSu3KSHUsikr0oCzIqBNCwkMfLMR-xZVIjDx-B2GemGOL6Q3XG6C8nNUrd0pNTJybVvgk4-Md9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم دامغان امشب هم شعار اتحاد و همدلی سر دادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/435611" target="_blank">📅 23:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435610">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZasWDh_D8azSt_0HIdlN2wCJwJmy-jKEFGJiChxANm6sZ4z4u6Wdv0dEnxyvWQ9TNy7R2Z6KPTm9AFQX9dP8dgxmmsppI2Z4ChB835fY0AlNbTZQ1USbR6YR7xV7nsNejU7WxOGwT_aD312W747vYebp3tv3-Y_sDAcVEtrjlL9Aup4OhOOe8GNDA9B2UoSGGL0B56w7pLg-La4MFLlHcLJDabIZdpfcmG2M-1KPYN3witsBFddoMM_ADO5DjROHMCROU_nHmwDDssJL9ysvMAYlXKPaXOtrSRxyU_1voZa_IutsxuAMLgSXqTjCT9SYEYz4MOTSx4hiPUlnV_ax3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش‌ قالیباف به رکوردشکنی نرخ بهرهٔ اوراق قرضهٔ امریکا
🔹
قالیباف با اشاره به خبر افزایش بی‌سابقهٔ نرخ بهره اوراق قرضهٔ آمریکا نوشت: پس شما درحال تأمین مالی هگست، مجری تلویزیونی شکست‌خورده، با نرخ‌هایی هستید که از سال ۲۰۰۷ بی‌سابقه بوده، تا او بتواند در حیاط خلوت ما در تنگه هرمز، نقش «وزیر جنگ» را بازی کند؟
🔹
می‌دانید چه چیزی دیوانه‌کننده‌تر از بدهی ۳۹ تریلیون دلاری است؟ این که برای تأمین مالی این جنگ‌بازی، نرخ بهره‌ای به اندازه دوران پیش از بحران مالی جهانی در سال ۲۰۰۸ بپردازید و در نهایت فقط یک بحران مالی جهانی جدید نصیب‌تان شود.
🔸
گفتنی است در روزهای اخیر بازده اوراق قرضه سی ساله آمریکا به بیش از ۵ درصد رسیده که این نرخ از سال ۲۰۰۷ یعنی سال پیش از بحران مالی جهانی بی‌سابقه است.
🔸
افزایش نرخ بهرهٔ اوراق قرضه به معنی افزایش انتظارات تورمی، افزایش نرخ بهره و بالا رفتن هزینهٔ وام‌ها و در نهایت وارد آمدن فشار تامین مالی جنگ با ایران به آمریکایی‌هاست. جنگی که با هدف تسلیم ایران آغاز شده بود حالا دارد اقتصاد آمریکا را تحت فشار قرار می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/435610" target="_blank">📅 23:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435606">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/run7qsbuxvUXfJH-GrukODoGLV_sozXPEJsq-08sCAVHdyg8wwMqHHorelMIrREwA17CN_Kiu5BnRp55bzzwmjHhApi6nLOHW5FZPyputcQ3WNnefeyRBLKVyWix7ayMabOrk3mzyk3ryHCpLlEP6iQichkXJxsJx82NVEZHHDETklkd9BV7z_tiVgAFwdf87MijGb2bHowplqZd9MM9BOTN2bVhIP04gny6KNUhaoiabnkKw04XrNtniFbDDzBeYkYhS9FvW0vxLW9H56JcPncEWH4YFJfMZmJDUtgQkwN3T2F04Pau2YhLE50S3RZLDBexiDjA_YnZiMXUbgRX7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jF78waXIQvFp5I5rYekk8EuSc7bH13WDGp6LmWDUbnMCapE3LSsTol-6HkqNgzuZ0lPXfAaucEglMU3ks5b1WqhAhGeum47WSH2HqI0zU5a-xko_r92EjEiOT0E9lZMGDqAxtyt5SX3zXCt5QR9r72rGTf4ea-fpIzj0_plgulxyRALfNqBb4uoswA2rSGb0jrSFqPYfmcPPLF0-BETiLwTo--P7Yj6Jkxa8l6zdgrE7-IlGr77rqGt_Pg-CrofHIn9DHax-qsoPYAuTyo20oy6n0TMwPYQckJp_CQmKSFLBPb1AfqgSgQC9LxhhDjGUS145up22JDH0ihgb1OAhnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqRgP1zJKlD6SZ-kDHeBx5W183MrXesP5tiF4LY6ApgVcnvJo-Yo0Oa4bWHiTXKCDtcxOltSPV2Bzc3srpoo_SMp8CIo_7J8Cytnwq3PplRSfOBhiaX7hFLxaDAz0gPu0YtHCH0y4GUWqzHeVsfJajoo_anfQqnSg_g0x2snz117044MEaSNJmtOlvmcXC7yNZ0htmlWsFhaw9zFIb1bLhk79Vl-fUNsFfAjCXq-ifaRM855WHvB8vg3rGd2D0M06cwydmfTO7ErYBOM5mOJz97uN607LCBXTDkSlh-xw8zmyHvltU5j_DIoxdf9X0-ySa7vcM5iTfJ_ehsoopTFLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/amtFRAcJp9Kn7JuaFetMjpWtcGSOsAvlb6CGRbMRc8Ya8rKpTniN30oODmrg5o--XtFUwI5IYXJRXCktM4lzhwSMLfUaZxBhr3dQ7CSHFTJv2vggkACaBXutFp6ILoOAKtPBN2jerQiJpyhPz_T_8KoGcULaRFdOmed6S2MQPDY6blXzLYLFCZOR1jrUzQlSAoNyvt8qTK76EuNgzD7twHtEdB1nzTzqiNez1YD4CthuP__mJ4KjpzzZrZ6V-gT4WEnBsdHnDhQpB-K6DpXeqmCzniZBos9NCjNJxpaeri44EWtihI9J36Q12J_ZOowfSYb-7dt8M-SAS12HnbsvSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اربعین شهید سرلشکر سیدعبدالرحیم موسوی در قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/435606" target="_blank">📅 23:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435605">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b9085ba5.mp4?token=LlL4QQ71XkeT1dLuyWJgYBpkHYY6q_AHFglZQh4PvedxFgNUBu56N7dfMRUvG3_c7TbjEVgAQ9HSSm5I_jBWH1eOD-ki0lXCWlF78HK3gYXvS1_M0DIuwbChluYJRBW62DfRuuSo0HmCL1077j9xhG1spAWpufqI7CkW9C09Lp8WnuWgHA8NC_eDSJLXfAAg14J2UaM23lkg1Qo56lkHvZ6wBVxCOD8Jm7qbPgQ4kmmDu5_oVgYnbdQlNlz31QKB6VUrcQLu3olgE5Y8UgYzfXz_lC2EIUHijJa8UsaEhlpkQ00sT0iF3HFx5a8FednEAz4IietYV7ePKFvro1G6RaZ2tpc-vxje0ZEhWTGBZPirCEGIusib8tt4u-mfGUYHy9lsGaNchcHhmxUeD5rSFg5VMeU7auxQ_wWdxTpb3g-CihPFn7Zh_8zA7kDD63k_-2stO59cIS5ccQ41pUYOVPXYGkfGyq_A78WB8qNXBPIDI5VD_FohRRtOvR4sgFYI9rtSg6Hkhp_assrlEgJHr3iOAJD2ulyVgfQGbuQ1LFk8libG8BsU0VzSvo3Yh-tL4jKEyaZFZQ-clqOlliPJ13SyLa3a52B73CZK32GYeAY8sNrwY850pKtf8bHhECHqP6AogF0zoUHEbu07AWS1iesNxfiJ7WkqzrdSIP0Mbqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b9085ba5.mp4?token=LlL4QQ71XkeT1dLuyWJgYBpkHYY6q_AHFglZQh4PvedxFgNUBu56N7dfMRUvG3_c7TbjEVgAQ9HSSm5I_jBWH1eOD-ki0lXCWlF78HK3gYXvS1_M0DIuwbChluYJRBW62DfRuuSo0HmCL1077j9xhG1spAWpufqI7CkW9C09Lp8WnuWgHA8NC_eDSJLXfAAg14J2UaM23lkg1Qo56lkHvZ6wBVxCOD8Jm7qbPgQ4kmmDu5_oVgYnbdQlNlz31QKB6VUrcQLu3olgE5Y8UgYzfXz_lC2EIUHijJa8UsaEhlpkQ00sT0iF3HFx5a8FednEAz4IietYV7ePKFvro1G6RaZ2tpc-vxje0ZEhWTGBZPirCEGIusib8tt4u-mfGUYHy9lsGaNchcHhmxUeD5rSFg5VMeU7auxQ_wWdxTpb3g-CihPFn7Zh_8zA7kDD63k_-2stO59cIS5ccQ41pUYOVPXYGkfGyq_A78WB8qNXBPIDI5VD_FohRRtOvR4sgFYI9rtSg6Hkhp_assrlEgJHr3iOAJD2ulyVgfQGbuQ1LFk8libG8BsU0VzSvo3Yh-tL4jKEyaZFZQ-clqOlliPJ13SyLa3a52B73CZK32GYeAY8sNrwY850pKtf8bHhECHqP6AogF0zoUHEbu07AWS1iesNxfiJ7WkqzrdSIP0Mbqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهرکردی‌ها در شب ۷۵ حضور خود برای جهاد صرفه‌جویی شعار دادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/435605" target="_blank">📅 23:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435604">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e145c4f6d.mp4?token=BXFn7wYnZdpFDHwPF4i-b9bmMTPjBu9QpC3BeH7ZXb5MiiV3tG6nm50McSU-ZwPIytZtnvYQ_AjfgPXVJFgiuDS-Pf9ylqtWfR79ktsOrwWm5gqjxFwvIeDSPnYNDfpVEjDsMFReKEFJtML-wdHOgudz6k8noYlLx5mexwukD85V7JMxVNj5tM2Gu0YKGyu6j8GfPxnaBZk7ZwygB4vyh9qMowGPmNeMCVT8SBQ7oKRX-megyrXFvUslOedDFfwR-3WbxFSgJGESBzsIyE3THssHTBZJMFyZaoOD69psXUvQYGItm2QlSTFVt8IemCXsOsGqVoNW2nDKTtdSchpiog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e145c4f6d.mp4?token=BXFn7wYnZdpFDHwPF4i-b9bmMTPjBu9QpC3BeH7ZXb5MiiV3tG6nm50McSU-ZwPIytZtnvYQ_AjfgPXVJFgiuDS-Pf9ylqtWfR79ktsOrwWm5gqjxFwvIeDSPnYNDfpVEjDsMFReKEFJtML-wdHOgudz6k8noYlLx5mexwukD85V7JMxVNj5tM2Gu0YKGyu6j8GfPxnaBZk7ZwygB4vyh9qMowGPmNeMCVT8SBQ7oKRX-megyrXFvUslOedDFfwR-3WbxFSgJGESBzsIyE3THssHTBZJMFyZaoOD69psXUvQYGItm2QlSTFVt8IemCXsOsGqVoNW2nDKTtdSchpiog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم میهن‌دوست محلهٔ زمزم و زهتابی در شب هفتادوپنجم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/435604" target="_blank">📅 23:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435603">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94c1849696.mp4?token=Z2KTwRshjq_UilANoa1ia7bXo5vqUGSaZ_wDn303wPJLcD4O48luuPZJ_GJQerKYpwk3g78u9DpWq0JANrrav-ZaFTqQUpX9thOyew6PpBhexgY_TR_ed91vTecC5HIujcMx4Ggp8GyTvkpkq-AM6Ea95puGiYlu2NmNOPxMnlEgAG6qpl5065UkNizdr1vT2OeWcf3OzDj3tRgFGG0TNY2IskPWE28Tpd0Z7fJ3QdL2XZBVEEkjAzf6K0GgxaOS3wj6eCyjUW9uRWCWO0vMcVFasrl6nlX9T-dNGgQux4QQO4acvPp8Lv7gwtqHDtq-jP_Sfdx6-sSRZ-RMsL_i-xevqi3nG4qD4y_NgrYl59oR7Z0k_jo1sTUPunwvMTZ76TJdNr7Cc5r2T4zVqeVW1xnaiBo3WR8S6jmMF_aXYuFTsRxZoEzSHbCpnkuI0xQCOncTARk6qrKeo_jYPZ76ffWZYhjl9QWGEqVsvO8t8VKMn6BMsSCSRVI4vf3emHMxsb1j3I2okXM9KU_D7bSc0LnluEbkl4lb_qYtUbp0HdY9Lbqh3uhhlEZzdxu3HCxZxsNzAbDivT9do21Gj6dhWMtFxIpE1SABl_tL-c_WevBgnul2bq_VKaNuPJsmeB_4H9g3G5MvtMsk5VjMWZYmn79z4TT7nfFoIdGP8OJZ6HE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94c1849696.mp4?token=Z2KTwRshjq_UilANoa1ia7bXo5vqUGSaZ_wDn303wPJLcD4O48luuPZJ_GJQerKYpwk3g78u9DpWq0JANrrav-ZaFTqQUpX9thOyew6PpBhexgY_TR_ed91vTecC5HIujcMx4Ggp8GyTvkpkq-AM6Ea95puGiYlu2NmNOPxMnlEgAG6qpl5065UkNizdr1vT2OeWcf3OzDj3tRgFGG0TNY2IskPWE28Tpd0Z7fJ3QdL2XZBVEEkjAzf6K0GgxaOS3wj6eCyjUW9uRWCWO0vMcVFasrl6nlX9T-dNGgQux4QQO4acvPp8Lv7gwtqHDtq-jP_Sfdx6-sSRZ-RMsL_i-xevqi3nG4qD4y_NgrYl59oR7Z0k_jo1sTUPunwvMTZ76TJdNr7Cc5r2T4zVqeVW1xnaiBo3WR8S6jmMF_aXYuFTsRxZoEzSHbCpnkuI0xQCOncTARk6qrKeo_jYPZ76ffWZYhjl9QWGEqVsvO8t8VKMn6BMsSCSRVI4vf3emHMxsb1j3I2okXM9KU_D7bSc0LnluEbkl4lb_qYtUbp0HdY9Lbqh3uhhlEZzdxu3HCxZxsNzAbDivT9do21Gj6dhWMtFxIpE1SABl_tL-c_WevBgnul2bq_VKaNuPJsmeB_4H9g3G5MvtMsk5VjMWZYmn79z4TT7nfFoIdGP8OJZ6HE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: کویت فراموش نکند که تنها در ۹۰ دقیقه توسط صدام تسخیر شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/435603" target="_blank">📅 22:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435602">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کشف ۲۱۰۰ تن برنج وارداتی احتکارشده در هرمزگان
🔹
سازمان جهاد کشاورزی هرمزگان: در نزدیکی بندر شهید رجایی بیش از ۲ هزار تن برنج وارداتی از کشورهای هند و پاکستان که به‌قصد احتکار و ایجاد بحران در بازار دپو شده بود، کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/435602" target="_blank">📅 22:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435601">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">مردم دیگر پس‌از وقوع حوادث به پمپ بنزین نمی‌روند
🔹
«یه پمپ بنزینمون نشه» جمله پرتکرار این‌روزها بین مردم در مواجه با حوادثی مثل جنگ یا زلزله است اما بررسی فارس نشان می‌دهد، پس از وقوع زمین لرزه در آخرین ساعات روز سه شنبه در تهران، تغییر در مصرف بنزین پایتخت اتفاق نیفتاده است.
🔹
از حدود ۲ سال پیش شلوغی پمپ‌بنزین رویدادی پرتکرار بوده که در روزهای ابتدایی جنگ ۱۲ روزه به اوج خود رسید.
🔹
صاحب یک جایگاه در مرکز تهران به فارس می‌گوید، میزان شلوغی و مصرف بنزین در هنگام حوداث طبیعی و غیر طبیعی بسیار کم شده و در زمین‌لرزه اخیر در بسیاری از جایگاه‌های تهران شاهد صف هم نبودیم.البته ممکن است در ساعاتی شاهد صف باشیم اما در جایکاه معدود برای زمان اندک است.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/435601" target="_blank">📅 22:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435600">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d401f8ad0.mp4?token=G2qhqOdpJ2ScZa5vxe0CdcSTF_czeStyyECimEMadT85_DxQK9xcxM6MmsDrKo_DJrioejfyfNzCbQ5qfr0E49dYDllLQEuF-k-zoP4sSsBquXW6mHGkQNgrhpRaNGj0lzYD-2BJ58awVfud3hwEe-YCGavkoQthCGcYm0fLicZlTySKr1CJr0MA-nbb7dTCKrLzHDHQq10TrQn-3BVeyC5ACi8P2XAuLTfLPYzNfOkIqbQOuwxa-iu_Snvvf246jkTFf8ThfHb1PEfOawFRq4MqBDCemJEvfESE91796N9INSU-dqOH-3j66_WhKmIkcsWMxvXwKZe-MaCBSsU16jRJzfVPo-CgXGFN1Fk27OTDEnIByc3jVvRXWoauKeTuPfc8vWAtHQ7mObOB0nm-upanqc8MpVxdGecgoJonkmBPcdDALlLkcFwQmQuO53UNKa_27RVbiRCIji0WtWsfaCUhS4feq2qSLp5MhEWaLrAIrvxNVlWpNwk2u-99TtamIvI4Eq3O6Htaji_IxTwqshcMzhAoOIwia19KwPgW_GxA-fjKObZ2j4npNd2806iElCCvthnqRCoq2_6hMMhsRwL0dOp5mBL4L3y0ONlYBNBNvW1-vvZg2pCq4kerCtW2epcH8ejCAgIC0wm-qi0O_FgXOCcPAUjL6MQoyjt7IJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d401f8ad0.mp4?token=G2qhqOdpJ2ScZa5vxe0CdcSTF_czeStyyECimEMadT85_DxQK9xcxM6MmsDrKo_DJrioejfyfNzCbQ5qfr0E49dYDllLQEuF-k-zoP4sSsBquXW6mHGkQNgrhpRaNGj0lzYD-2BJ58awVfud3hwEe-YCGavkoQthCGcYm0fLicZlTySKr1CJr0MA-nbb7dTCKrLzHDHQq10TrQn-3BVeyC5ACi8P2XAuLTfLPYzNfOkIqbQOuwxa-iu_Snvvf246jkTFf8ThfHb1PEfOawFRq4MqBDCemJEvfESE91796N9INSU-dqOH-3j66_WhKmIkcsWMxvXwKZe-MaCBSsU16jRJzfVPo-CgXGFN1Fk27OTDEnIByc3jVvRXWoauKeTuPfc8vWAtHQ7mObOB0nm-upanqc8MpVxdGecgoJonkmBPcdDALlLkcFwQmQuO53UNKa_27RVbiRCIji0WtWsfaCUhS4feq2qSLp5MhEWaLrAIrvxNVlWpNwk2u-99TtamIvI4Eq3O6Htaji_IxTwqshcMzhAoOIwia19KwPgW_GxA-fjKObZ2j4npNd2806iElCCvthnqRCoq2_6hMMhsRwL0dOp5mBL4L3y0ONlYBNBNvW1-vvZg2pCq4kerCtW2epcH8ejCAgIC0wm-qi0O_FgXOCcPAUjL6MQoyjt7IJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع شبانه مردم بجنورد با حضور کاروان زندگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/435600" target="_blank">📅 22:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435599">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b399cb7af.mp4?token=de0BEBMRAtyliWpdDyKRzNxhpCihtyM0_2K2-ZOkCTfQYw6DpSRKRTYrkPkuFEomDYJKJqftxa75AvtrKpgSJZxQz-TYmpqxEomhCMgatkD1PPZMLLeBsRejFTStg1tEc_R39tn9KLCsYa7hjljWZ90aKsPNmCw3RJIxYtiJTalEf79jb2o6oCMEEKSJwyJfJ3tkz4Xnq_pNNzBUQbfVXSLzlsqHEL9yLZAyUdtXo-IzBkXt9njBC11WA5wugY67xnssw-2Hl5oZix5lQuYKpm-9Ukd_yUKkdDbndXbT5o06FvUaycE9lsfu2gkx0T2ut62viLZf5zB1nOHsymL1Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b399cb7af.mp4?token=de0BEBMRAtyliWpdDyKRzNxhpCihtyM0_2K2-ZOkCTfQYw6DpSRKRTYrkPkuFEomDYJKJqftxa75AvtrKpgSJZxQz-TYmpqxEomhCMgatkD1PPZMLLeBsRejFTStg1tEc_R39tn9KLCsYa7hjljWZ90aKsPNmCw3RJIxYtiJTalEf79jb2o6oCMEEKSJwyJfJ3tkz4Xnq_pNNzBUQbfVXSLzlsqHEL9yLZAyUdtXo-IzBkXt9njBC11WA5wugY67xnssw-2Hl5oZix5lQuYKpm-9Ukd_yUKkdDbndXbT5o06FvUaycE9lsfu2gkx0T2ut62viLZf5zB1nOHsymL1Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت کارکنان بیمارستان میناب از مواجهه با انبوه دانش‌آموزان مجروح
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/435599" target="_blank">📅 21:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435598">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VramdMSD6wM4IWfCBUHz9ahRqZZOqeZUk195L2tvjDvdJ_pAxHjsR9yluGlqL2hhkVpcqars_lb6TvgVxMHj3bd_vNZUHnNIwcg1H6941B9lSabRBXkE9vtWaIAhljV1-CCCmjhFshqis5kIuN3NuY0sGQ5rSonsLKY35gplvAGN9gGnFRSYXpEQG1SXLMm1ptLok9JFFBHPsPXMyredfEZMYy3kIMhEkZ3WQTF2SQD9jAqrM61KkG4LbA5zCRo3jUgS5w_mpgvuGyWSSFyAtPDQd2kD26jm7PE5hTOuftHqGcN-mcqRCKtnlqc_Q5RCciUBpXvQg3WviP68oVRy3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
علی الزیدی پس از سوگند یاد کردن، رسما به‌عنوان نخست‌وزیر عراق انتخاب شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/435598" target="_blank">📅 21:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435597">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d376cd237.mp4?token=koZB1qGFXeFe1yZh3NOYlW1RU9VyaFf2YHF349CHGpXKPq5UAE-vNASDN29efdITTQwuRpZLwss5Le6yxAJnsaJABt1ecza0WNeJhgOv9-MU7zRkvQqkmJ79_orenpN59GVpF_fNQvH-Zm5qGUs8nohMtWdbLXlRE9sX1dU6Oz4mwzFZqAKl_buCRiOOoZDfD9o3MkBTMceW9emcxnwxVYiiG_eduipUxtKdT6NhG6lcu95UBXE8QRvClcuMWaeA3PauZpSBR1ZmpdG882BeCOeQTxcoZgpCTb53ix7EiWoH_7qZCplbw6G2375p5aQ5EV1vscPoZYSYRQBFCSxULw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d376cd237.mp4?token=koZB1qGFXeFe1yZh3NOYlW1RU9VyaFf2YHF349CHGpXKPq5UAE-vNASDN29efdITTQwuRpZLwss5Le6yxAJnsaJABt1ecza0WNeJhgOv9-MU7zRkvQqkmJ79_orenpN59GVpF_fNQvH-Zm5qGUs8nohMtWdbLXlRE9sX1dU6Oz4mwzFZqAKl_buCRiOOoZDfD9o3MkBTMceW9emcxnwxVYiiG_eduipUxtKdT6NhG6lcu95UBXE8QRvClcuMWaeA3PauZpSBR1ZmpdG882BeCOeQTxcoZgpCTb53ix7EiWoH_7qZCplbw6G2375p5aQ5EV1vscPoZYSYRQBFCSxULw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برنامهٔ ترامپ برای ایران معکوس شد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/435597" target="_blank">📅 21:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435596">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186bafc9e9.mp4?token=HOnF-M6zmmztFppVzIDGSMGPnmzQj8hGuASI8e1SGllizInMIiL5k04gQpz7K7Z4Fx1tqkzI-P5xMu6XOYZHDo1eXFCTfebvb3Wau2KxPWysAzLyJR9jNn0h3iUFpDYAUX8f_VsgJYP0TrhPZxFUkpN0EPCyVxrTdgTrxYxUb_B8zZTarHejglhmSGw9Bj6b0QSGkWPiEX5yGdJXSj7JQRK-Kr8rjMBMwloV1dx-Dy5la8EtLoff3sOAHhXx420AUesZj7BlEuTkwVq6lf9VBkeLB32xX4JpNhJz2ZtjmwqU6vPK5ji9M8yUJ6OPJOTEf82gkA-FIpo4A8ohtcElWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186bafc9e9.mp4?token=HOnF-M6zmmztFppVzIDGSMGPnmzQj8hGuASI8e1SGllizInMIiL5k04gQpz7K7Z4Fx1tqkzI-P5xMu6XOYZHDo1eXFCTfebvb3Wau2KxPWysAzLyJR9jNn0h3iUFpDYAUX8f_VsgJYP0TrhPZxFUkpN0EPCyVxrTdgTrxYxUb_B8zZTarHejglhmSGw9Bj6b0QSGkWPiEX5yGdJXSj7JQRK-Kr8rjMBMwloV1dx-Dy5la8EtLoff3sOAHhXx420AUesZj7BlEuTkwVq6lf9VBkeLB32xX4JpNhJz2ZtjmwqU6vPK5ji9M8yUJ6OPJOTEf82gkA-FIpo4A8ohtcElWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی خطاب به امارات: ائتلاف با اسرائیل هم از شما محافظت نکرد
🔹
وزیر امور خارجه امروز در نشست وزرای خارجه بریکس در دهلی‌نو در پاسخ به ادعاهای بی‌اساس نماینده امارات گفت: ائتلاف شما با اسرائیلی‌ها نیز از شما محافظت نکرد و در سیاست خود در قبال ایران بازنگری…</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/435596" target="_blank">📅 20:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435595">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بزرگترین توافق تبادل اسرای جنگ یمن انجام شد
🔹
دولت یمن از انجام توافق تبادل اسرا با دولت وابسته به عربستان خبر داد و آن را بزرگترین توافق تبادل معرفی کرد. رئیس کمیته ملی امور اسرای یمن با اشاره به اینکه «لیست اسامی ۱۱۰۰ اسیر و بازداشتی از طرف ما به امضا رسید» خبر داد که «در این تبادل، ۵۸۰ نفر از اسرای طرف مقابل از جمله ۷ اسیر سعودی و ۲۰ اسیر سودانی آزاد خواهند شد».
🔹
المشاط، رئیس شورای‌عالی سیاسی یمن ضمن تبریک این توافق گفت که «صنعا تمام تسهیلات برای تکمیل این پروندهٔ انسان‌دوستانه و آزادی اسرا را طبق اصل همه در برابر همه، ارائه کرده است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/435595" target="_blank">📅 20:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435594">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bae404a54.mp4?token=MTXKuLkShaIvNpNBBenGeqocjnA8SIwN6hPFR1LYEL6ky7Poxpvk2o7MH_eJ4fu82hrKK2k2hiZSg6swVPudxCjOh-xR0H6NGooI0tsPUocnqDoRj7CXYKwzNBpgPDS9tOEPvKaGOPCsWrshUOghtxzXk2BCyTvh40yH_py2PPWaNekQZWTPaKUx1bYHKtsEBhxnNe0en_MkO2rGVXgyg8-O-v53NG1rETKzzvwLIFD-24gXg8yMfo7fpmq4LjbHzCJ6UuLSHePyXeP8EbkzKxM8-0ta3hpE7kKqEYS3mzq35qyJXbAWLZ7ieONi3p9pXBCL5Emzb5uXBNr4G61miYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bae404a54.mp4?token=MTXKuLkShaIvNpNBBenGeqocjnA8SIwN6hPFR1LYEL6ky7Poxpvk2o7MH_eJ4fu82hrKK2k2hiZSg6swVPudxCjOh-xR0H6NGooI0tsPUocnqDoRj7CXYKwzNBpgPDS9tOEPvKaGOPCsWrshUOghtxzXk2BCyTvh40yH_py2PPWaNekQZWTPaKUx1bYHKtsEBhxnNe0en_MkO2rGVXgyg8-O-v53NG1rETKzzvwLIFD-24gXg8yMfo7fpmq4LjbHzCJ6UuLSHePyXeP8EbkzKxM8-0ta3hpE7kKqEYS3mzq35qyJXbAWLZ7ieONi3p9pXBCL5Emzb5uXBNr4G61miYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: هنوز هم روزانه یک میلیارد دلار صرف جنگ با ایران می‌شود
🔸
سناتور گیلیبراند: قرار است چند روز، هفته، ماه یا سال دیگر با ایران در جنگ باشیم؟
🔹
فرمانده سنتکام: ما در وضعیت آتش‌بس هستیم و مسیر پیش‌رو توسط سیاست‌گذاران تعیین خواهد شد.
🔸
سناتور…</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/435594" target="_blank">📅 20:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435593">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727ca1076d.mp4?token=aQOtjbBcWRDUVnjWtYkR_KnmBPF-0ErN3uqNn4xiPKgyM0yCtjE-ynFX0dsIHrjznfFx_8P8G6vaN3BD1OPjjF5B72YG6kY1wtONPHxP-xB2-766ZyDpeFcpuyF6DqBLCwrRyIAi6woWcKwsAm9s4RYLSSBVk_gDUmG6ALGjIOzI2wlg4ZivcAzH9uZCsjHwsEd9OLlagnQUjlkfBtfiFkulBdc5UW3OvBS3S9nSjjSalcJqY-4gzrrO-mPssVF1_n6L6fIZnMV4bc5koJZVKxYG8k2QmC-41ksUrsu-ZyswokIQALuAseogzTpIBwOGMFx6qUBtXb1a19mdDqn7ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727ca1076d.mp4?token=aQOtjbBcWRDUVnjWtYkR_KnmBPF-0ErN3uqNn4xiPKgyM0yCtjE-ynFX0dsIHrjznfFx_8P8G6vaN3BD1OPjjF5B72YG6kY1wtONPHxP-xB2-766ZyDpeFcpuyF6DqBLCwrRyIAi6woWcKwsAm9s4RYLSSBVk_gDUmG6ALGjIOzI2wlg4ZivcAzH9uZCsjHwsEd9OLlagnQUjlkfBtfiFkulBdc5UW3OvBS3S9nSjjSalcJqY-4gzrrO-mPssVF1_n6L6fIZnMV4bc5koJZVKxYG8k2QmC-41ksUrsu-ZyswokIQALuAseogzTpIBwOGMFx6qUBtXb1a19mdDqn7ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: هنوز هم روزانه یک میلیارد دلار صرف جنگ با ایران می‌شود
🔸
سناتور گیلیبراند: قرار است چند روز، هفته، ماه یا سال دیگر با ایران در جنگ باشیم؟
🔹
فرمانده سنتکام: ما در وضعیت آتش‌بس هستیم و مسیر پیش‌رو توسط سیاست‌گذاران تعیین خواهد شد.
🔸
سناتور گیلیبراند: در حال حاضر، ما همچنان روزانه یک میلیارد دلار هزینه صرف جنگ با ایران می‌کنیم. مردم از این موضوع خشمگین هستند.
🔸
این رقم می‌تواند صرف کاهش هزینه‌های مسکن، کاهش هزینه‌های غذا، کاهش هزینه‌های درمانی و پایین آوردن مخارج روزمره‌ای شود که به‌دلیل جنگ در ایران مدام درحال افزایش است.
🔸
معنی قیمت بالای بنزین و گازوئیل این است که هر چیزی که آمریکایی‌ها باید برای خانواده‌هایشان بخرند گران‌تر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farsna/435593" target="_blank">📅 20:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435592">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbcfaecd0d.mp4?token=G_Kpb-9nuE7xKF23lm0RCjxnuKdT6QqFqPQwPqkevuHf5QFubxqBpdDbiXhGfDZbCkzP5OY_plK_EEHzOSa9CPZ1jZFu1AKr6XDTSmCt-WfzmZPs1ZEH-2n1Kxz4Shg2A17dHfuaxBliXoDyVngFw_C5aNeCyBgsVplCNo39We5YyeUmVad4YhGdCj9E1Ivy-OZ8MvG1JRqA8oYzOmf2B__zlMxN-IUENzn7KqFOl30SAXYKEMUUwLZcbp-gJQ-bW2LJ1xmEU1SYBykXf8E7NzNUe0V2Ynk8P3C-I_2KIkirLOGpn9wV1Guk9kvQjc_jr5y7GPWLG_57ztxsHEv-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbcfaecd0d.mp4?token=G_Kpb-9nuE7xKF23lm0RCjxnuKdT6QqFqPQwPqkevuHf5QFubxqBpdDbiXhGfDZbCkzP5OY_plK_EEHzOSa9CPZ1jZFu1AKr6XDTSmCt-WfzmZPs1ZEH-2n1Kxz4Shg2A17dHfuaxBliXoDyVngFw_C5aNeCyBgsVplCNo39We5YyeUmVad4YhGdCj9E1Ivy-OZ8MvG1JRqA8oYzOmf2B__zlMxN-IUENzn7KqFOl30SAXYKEMUUwLZcbp-gJQ-bW2LJ1xmEU1SYBykXf8E7NzNUe0V2Ynk8P3C-I_2KIkirLOGpn9wV1Guk9kvQjc_jr5y7GPWLG_57ztxsHEv-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: حمایت آمریکا از دیکتاتوری پهلوی باعث وضع کنونی ایران شد
🔹
تیم کین: من بارها و بارها صحبت‌های ترامپ و وزیر جنگ را درباره اقدامات بد ایران از سال ۱۹۷۹ شنیده‌ام اما بخش زیادی از داستان هست که مردم درباره‌اش حرف نمی‌زنند؛ تاریخ از سال ۱۹۷۹ شروع نشده است.
🔹
آمریکا در سال ۱۹۵۳ (سال وقوع کودتای ۲۸ مرداد)، کودتایی را برای سرنگونی دولت دموکراتیک ایران رهبری کرد. آمریکا یک دیکتاتوری یعنی «شاه ایران» را سرکار نگه‌داشت و پلیس مخفی او یعنی «ساواک» را آموزش داد؛ سازمانی که هزاران ایرانی را شکنجه کرد، تبعید کرد، به زندان انداخت و کشت.
🔹
۲۶ سال بعد از آن، انقلاب سال ۱۹۷۹ رخ داد و بله، آن زمان بود که شعار «مرگ بر آمریکا» سر داده شد. حمایت آمریکا از یک دیکتاتوری و سرنگونی یک دولت منتخب دموکراتیک، منجر به ایجاد ایرانی شد که [با ما] بسیار خصمانه رفتار کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/435592" target="_blank">📅 20:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435591">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🎥
اوباما درباره برجام: بدون شلیک یک گلوله برنامه هسته‌ای ایران را متوقف کردیم
🔹
رئیس‌جمهور اسبق آمریکا: ما بدون شلیک یک گلوله آن را متوقف کردیم. ۹۷ درصد اورانیوم آنها را خارج کردیم.
🔹
هیچ بحثی وجود ندارد که آن توافق را کار کرد و لازم نبود ما عده زیادی آدم بکشیم یا تنگه هرمز را ببندیم.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/435591" target="_blank">📅 20:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435590">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsKGh16NS6iGQEq36m2TrOM3HjkgFIdbKBIaiirfRTb01vFiyfi_F7QmIl0YV0mPYPBq1WztsQScxNhQ0Av0oT4daeI6NU9WULRH6zOa9stwlsmlYzs2lLZqSZP2nuMGGnkv9IV8sDUDyIFAO_DHzT-zLsyDC8dvq0jkgwCNBchP7IlJnsQ0pvoYVtwFFKlbLnxGVZhrtNjOfKbY2ytYDOHQfL9qAE9i1xtfYkBpa-vENLlbj0ET_0tCq9hLNzwXyWd-l83AYMGIAKotHxTvHMhdse8o3aGcUJ1l0CRShItWVP3Jy5KrRJtZKO4v8eNXvL7cLiJPaKipDFo3Sm0AWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهاد صاحب‌خانه‌ها در میدان مسکن
🔹
در روزهایی که فشارهای اقتصادی بیش از گذشته بر دوش خانواده‌ها سنگینی می‌کند، پویشی مردمی شکل گرفته تا مالکان را به همدلی با مستأجران و پرهیز از افزایش اجاره دعوت می‌کند؛ حرکتی که می‌تواند در کنار مقاومت مردم در عرصه‌های دیگر، به کاهش فشارهای معیشتی هم کمک کند.
🔹
مردم این سرزمین هرگاه ندای عدالت و مساوات شنیده‌اند، از یاری یکدیگر دریغ نکرده‌اند. این پویش هم تلاشی مردمی است؛ دعوتی به همدلی با مستأجرانی که این روزها زیر فشار شرایط اقتصادی قرار دارند و چشم‌انتظار همراهی و گذشت مالکان‌اند.
🔹
اینجاست که نقش مالکان می‌تواند تعیین‌کننده باشد؛ کسانی که می‌توانند در این میدان هم همچون سرداران یک نبرد، با گذشت و همراهی، به مردم و جبههٔ اقتصادی کشور یاری برسانند؛ همان‌گونه که در سیرهٔ بزرگان دین و فرهنگ هم بارها دیده‌ایم که گذشت از منفعت شخصی، راهی برای سربلندی جمعی بوده است.
🔹
اکنون پرسش این است که شما در کجای این جبهه ایستاده‌اید؟ آیا مالکی را می‌شناسید که در این نبرد، با گذشت و همراهی، نام خود را در کنار مردم ثبت کند؟ نام او را همراه با روایت این گذشت خیرخواهانه برای ما ارسال کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/435590" target="_blank">📅 19:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435589">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a59b3bde01.mp4?token=OeIe5rsdRk9bd67a3c6EUAgAv9-gC40x3CPFlJFXY7BCYzLBDPpkZ4oOfsC4Rf6XnFU2bLvFWuutD01gRXScw0uYZWUZ4FZnpAmWJKj5g-1zWfJuBEk6TmqG2O4wN6qWp9gTzh0qgg9U72_Bpm8-Ol1QbN0VPEWemkvNX_WuM5__vdL5RoEtOMusD4DZx_Uh8KrgOv-PdRo4ggtAOQDFNvWapsHyEPeTJnxGjHQwxcyCQAxnvteBg-b7_XtLqqCr1D5Bgv4h9jTAJU_KAxCXLDWevqzMTDHmnspJFq2ZBURYk40WHi3ypRcKtIBy851OYYuUkudgfyMPoa7Z-L3Zog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a59b3bde01.mp4?token=OeIe5rsdRk9bd67a3c6EUAgAv9-gC40x3CPFlJFXY7BCYzLBDPpkZ4oOfsC4Rf6XnFU2bLvFWuutD01gRXScw0uYZWUZ4FZnpAmWJKj5g-1zWfJuBEk6TmqG2O4wN6qWp9gTzh0qgg9U72_Bpm8-Ol1QbN0VPEWemkvNX_WuM5__vdL5RoEtOMusD4DZx_Uh8KrgOv-PdRo4ggtAOQDFNvWapsHyEPeTJnxGjHQwxcyCQAxnvteBg-b7_XtLqqCr1D5Bgv4h9jTAJU_KAxCXLDWevqzMTDHmnspJFq2ZBURYk40WHi3ypRcKtIBy851OYYuUkudgfyMPoa7Z-L3Zog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جونی ارنست، سناتور آمریکایی: عملیات‌هایی که علیه ایران انجام دادیم بدون وجود شرکای فوق‌العاده در منطقه امکان‌پذیر نبود
🔹
ما شاهد بودیم که بار بزرگی بر دوش اسرائیل و اردن بود. ما کمک‌هایی از بحرین و امارات دریافت کردیم که حجم قابل توجهی از آتش حملات را متحمل…</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/435589" target="_blank">📅 19:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435588">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b441fded1.mp4?token=TOXnq0IIiPpxr6TD1JfTUwsT0RbVX6xcrK2zp1OMnoYd7ugnOFPBpXbSQFs38tDrdYumdxzr4JOnjj2WyP4REFSWzIESQX1CDjbCQgvA7OiW0vTX5mj2lHPAdFD2qUEBo7uWquj_HvLWrIvCLTOMcHjxW1CZmTafOgVBQwGmimdVq4PGr_bF66V_fiiy7eChlTQNW3PVkUoeB0oPD9ZSl5AKbnuGvasf7PZSyT2_4-Msh9GP0boxqaHs2RBzkm0p9joyhVCmZ-dFPvdKO0pcx18uTrXMc1Z6ixxeA2hWYLFHysjI4PxyzqxUgNrxSfHvbGT14J8PddT3V7zgUMSpeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b441fded1.mp4?token=TOXnq0IIiPpxr6TD1JfTUwsT0RbVX6xcrK2zp1OMnoYd7ugnOFPBpXbSQFs38tDrdYumdxzr4JOnjj2WyP4REFSWzIESQX1CDjbCQgvA7OiW0vTX5mj2lHPAdFD2qUEBo7uWquj_HvLWrIvCLTOMcHjxW1CZmTafOgVBQwGmimdVq4PGr_bF66V_fiiy7eChlTQNW3PVkUoeB0oPD9ZSl5AKbnuGvasf7PZSyT2_4-Msh9GP0boxqaHs2RBzkm0p9joyhVCmZ-dFPvdKO0pcx18uTrXMc1Z6ixxeA2hWYLFHysjI4PxyzqxUgNrxSfHvbGT14J8PddT3V7zgUMSpeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جونی ارنست، سناتور آمریکایی: عملیات‌هایی که علیه ایران انجام دادیم بدون وجود شرکای فوق‌العاده در منطقه امکان‌پذیر نبود
🔹
ما شاهد بودیم که بار بزرگی بر دوش اسرائیل و اردن بود. ما کمک‌هایی از بحرین و امارات دریافت کردیم که حجم قابل توجهی از آتش حملات را متحمل شدند.
🔹
عربستان و قطر نیز تماشاگر نبودند و فعالانه مشارکت داشتند. دسترسی به پایگاه‌ها، لجستیک و همکاری‌های اطلاعاتی آن‌ها از نظر عملیاتی برای ما بسیار حیاتی بود.
@Farsna</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/435588" target="_blank">📅 19:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435587">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e98740f13.mp4?token=bCSblqwfdPwbh7--0ra3Y0uu5rymZoObsH6w0oaQ2N7_P3L0okg4Cc69ObDZdvNFWYw5Bd4tRi2mxYbBcSzOpEI7U4rAVbWJfzNYB9UIt6tbIPCaejELxYrI9Sa3BAcAaML_ngbP4aDksay4Y21M1_S867oBHQO-nxRJx7fW7ebduVgJ1_YSYOXyC7noly4DtFFt85F6SQYeHf-_GE1TXdQqr2Ht-xp3uGOS9kYozH9LNraXcmzSzTyl6xZuxNay1HKaDXnoL6KCjho_VHwZxu7nsQjRgwykGlLLm-L9_1YfDJkknqNAwtiVv0IHfihGlLBuHAlKphjqZiGuMDCADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e98740f13.mp4?token=bCSblqwfdPwbh7--0ra3Y0uu5rymZoObsH6w0oaQ2N7_P3L0okg4Cc69ObDZdvNFWYw5Bd4tRi2mxYbBcSzOpEI7U4rAVbWJfzNYB9UIt6tbIPCaejELxYrI9Sa3BAcAaML_ngbP4aDksay4Y21M1_S867oBHQO-nxRJx7fW7ebduVgJ1_YSYOXyC7noly4DtFFt85F6SQYeHf-_GE1TXdQqr2Ht-xp3uGOS9kYozH9LNraXcmzSzTyl6xZuxNay1HKaDXnoL6KCjho_VHwZxu7nsQjRgwykGlLLm-L9_1YfDJkknqNAwtiVv0IHfihGlLBuHAlKphjqZiGuMDCADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الزیدی به عنوان نامزد نخست‌وزیری عراق معرفی شد
🔹
منابع عراقی خبر دادند که چارچوب هماهنگی شیعیان به‌عنوان فراکسیون اصلی پارلمان عراق، علی الزیدی، فعال اقتصادی عراقی را به‌عنوان گزینۀ نهایی خود انتخاب کرده است. @Farsna</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/435587" target="_blank">📅 19:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435586">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc997db7c.mp4?token=NPFL8_Msik92doO5jQ1PT5MhrcwSclfI81UCysxGyOA8MySDBuSrUWcn43vxePWPVJwyBYWiZHK50iZXUJnjX7IWTkmmVhA2oz6XhXr9cslV8PnAFJXnBpfp1_h_1RlhkstpbtsYWxZKiiswj66fp-vMP5UOcfsT8pQQ3Je7gc66EIIWaQx-pfSeHUk_ydQPW2XHCFB7RdD7j0vptE5mRvcGuGYGQoDWEZ0lJJVyb2eoSrHnmYJe00b8cTrOVZnTqAqR1vOczniT-STgXSEmR_bDmkUkiI7A18O2FJUxaJMsODYJtC2LMZSLnz0Ca2X8QeJ3xg9suiT38pXNqWaSNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc997db7c.mp4?token=NPFL8_Msik92doO5jQ1PT5MhrcwSclfI81UCysxGyOA8MySDBuSrUWcn43vxePWPVJwyBYWiZHK50iZXUJnjX7IWTkmmVhA2oz6XhXr9cslV8PnAFJXnBpfp1_h_1RlhkstpbtsYWxZKiiswj66fp-vMP5UOcfsT8pQQ3Je7gc66EIIWaQx-pfSeHUk_ydQPW2XHCFB7RdD7j0vptE5mRvcGuGYGQoDWEZ0lJJVyb2eoSrHnmYJe00b8cTrOVZnTqAqR1vOczniT-STgXSEmR_bDmkUkiI7A18O2FJUxaJMsODYJtC2LMZSLnz0Ca2X8QeJ3xg9suiT38pXNqWaSNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی فرمانده سنتکام را به چالش کشید
🔸
بلومنتال: آیا موافقید که در اختیار گرفتن اورانیوم‌های غنی‌شدهٔ ایران مستلزم حضور نیروی زمینی و تلفات قابل توجه برای آمریکاست؟
🔹
فرمانده سنتکام: با توجه به ماهیت محرمانهٔ برنامه‌ها، صحبت دربارهٔ برنامه هسته‌ای بسیار نامناسب است.
🔸
بلومنتال: دشمنان ما بسیاری از چیزهایی که ما می‌دانیم را می‌دانند. کسانی که از حقایق بی‌خبرند، مردم آمریکا هستند.
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/435586" target="_blank">📅 19:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435585">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dmygsr7yViADn1F4Xl29UoXsfpUysx4wiyCOgqvUb-Nwik1js3yR8S5SB70VmpVM70uF_eTumFsCcMmC-LBW3jD0cnUErEw1A6UA9YiPlqGoFn9FYG1IQ0rS6Yy86QJYc82_A03qEVYGfRy_qypZfbqt_-whcgOtEYAEY1P98DBbLFaLOu_upM4vtHzjbtWTlbrXqhlADfhJBGjydUpdKGoUGwBY2jqtfsBAY6NFKgHyoD-Hh6f0PqG2cUwCTJQPuk0af4n3WcPlFMDrwkhN9oiNQvRfFyhJlH2BvlNUFzv7xgu1bbF7jSmKVWSEsAhC2DOIxJPSi_zfeiB_2ys4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عراقچی در حاشیهٔ نشست وزرای خارجهٔ بریکس با مشاور امنیت ملی هند دیدار و گفت‌وگو کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/435585" target="_blank">📅 19:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435584">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69aba23e2a.mp4?token=qHvq06ZQva5W0AlFg1mIDNVUCsGvRB5xtCwYrPlGLDod8xx5IW3nXhY6BqaQP4wIchhSBDlDkqxaPT7pwoeFgs5EvyxMKESv_cSCdv1N6FJOxuxLlpLNuxyl-vs3J7Op7fJQCVOYMr8HSXv08K_FhKyu1KktKKCTp5GXizGGAIGYnwq8Uaug9VfIOxYjoE-ZoBEhWQsvdJAFcy7BOCLXSCDbwuB9dWOxi-uuQdyCKfW5ZC47SXgddJ_LPUG-OG5tNhagp9DZ81hvXzyfOfBOsyMx9pAZPvhpdpKT7JFbu6Sp97cqfP9iG9Nelg6tqU3UVld9Xe2pb1GTdgSt37ILqwA_FtlghNMrKBFZwvri6kPU0JfIEf8VGDYiC2Xv92Dtv4kdHeiDGANf4aOc5knPUkIiqHZl2oCU5KVLH6DgsX_mLVMQmX-mXaHxrOB-kqnujSWhi4hSACQ6tsYAg68L4dZVLvDkXbaUOG4f6hTcsy3ymiYhXlEnNjn_MSa-iSt0PNDxgbJnoLOzWG6RJuVSO47o83jZl9C_mg-ozOc1tlTu_dQz8AXHyV-riBPUbA44_uUhSqCz90O2nTmYu9OdOfKQaQJ8lZbYEA1J4TXmleVsPqJE0xQi_rWoYsPu1g2LCcctG1q_IG3HcW4nNJ-evX_SafR2JzQguHxpILH-PQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69aba23e2a.mp4?token=qHvq06ZQva5W0AlFg1mIDNVUCsGvRB5xtCwYrPlGLDod8xx5IW3nXhY6BqaQP4wIchhSBDlDkqxaPT7pwoeFgs5EvyxMKESv_cSCdv1N6FJOxuxLlpLNuxyl-vs3J7Op7fJQCVOYMr8HSXv08K_FhKyu1KktKKCTp5GXizGGAIGYnwq8Uaug9VfIOxYjoE-ZoBEhWQsvdJAFcy7BOCLXSCDbwuB9dWOxi-uuQdyCKfW5ZC47SXgddJ_LPUG-OG5tNhagp9DZ81hvXzyfOfBOsyMx9pAZPvhpdpKT7JFbu6Sp97cqfP9iG9Nelg6tqU3UVld9Xe2pb1GTdgSt37ILqwA_FtlghNMrKBFZwvri6kPU0JfIEf8VGDYiC2Xv92Dtv4kdHeiDGANf4aOc5knPUkIiqHZl2oCU5KVLH6DgsX_mLVMQmX-mXaHxrOB-kqnujSWhi4hSACQ6tsYAg68L4dZVLvDkXbaUOG4f6hTcsy3ymiYhXlEnNjn_MSa-iSt0PNDxgbJnoLOzWG6RJuVSO47o83jZl9C_mg-ozOc1tlTu_dQz8AXHyV-riBPUbA44_uUhSqCz90O2nTmYu9OdOfKQaQJ8lZbYEA1J4TXmleVsPqJE0xQi_rWoYsPu1g2LCcctG1q_IG3HcW4nNJ-evX_SafR2JzQguHxpILH-PQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراف تلخ کارشناس اینترنشنال: رسانه‌ها برای مردم یک دروغ فانتزی از جنگ ساختند  مهدیه گلرو، کارشناس اینترنشنال:
✅
در این جنگ بچه‌‌های مردم کشته شده و خانه‌‌های مسکونی مورد هدف قرار گرفتند. رسانه‌ها برای مردم یک دروغ فانتزی از جنگ ساختند.
✅
جنگ بخاطر مردم…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/435584" target="_blank">📅 19:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435583">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e0ea89f96.mp4?token=DHZaCopXGKqpmAr_nEFhNLPnSYfbIkU6qI7JgqUnYRVpqiTFqHdCb2iKsijbUJgcHrHLVo6zH8aTsRRgXgEdQTciQ-jovpem736Ik0ddjJv_YwtUthrBt3juX9bOIFkPPYsBzAl064JMTQrXycReEsRS0VFbPGBcNzpOHZWCbOoPm6wt9zXsyOysnb2lXQij-dApj0MkMXq4vyzlwAvMFRuqtSvjaKyqfF7j722wqkq7CX1-FfjZxszxMGoi7Y-wvnUe4LFSMU3JeELMmRdjStF47pXdYijIw2jL8tj2YOE42xBypZXntR4vYGDGSNW9E9d8pVEiqkHgXewri7hTNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e0ea89f96.mp4?token=DHZaCopXGKqpmAr_nEFhNLPnSYfbIkU6qI7JgqUnYRVpqiTFqHdCb2iKsijbUJgcHrHLVo6zH8aTsRRgXgEdQTciQ-jovpem736Ik0ddjJv_YwtUthrBt3juX9bOIFkPPYsBzAl064JMTQrXycReEsRS0VFbPGBcNzpOHZWCbOoPm6wt9zXsyOysnb2lXQij-dApj0MkMXq4vyzlwAvMFRuqtSvjaKyqfF7j722wqkq7CX1-FfjZxszxMGoi7Y-wvnUe4LFSMU3JeELMmRdjStF47pXdYijIw2jL8tj2YOE42xBypZXntR4vYGDGSNW9E9d8pVEiqkHgXewri7hTNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: رئیس‌جمهور چین به من گفت پکن به ایران تجهیزات نظامی نخواهد داد اما در عین حال گفت چین به خرید نفت از ایران ادامه می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/435583" target="_blank">📅 18:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435582">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrBZ-Gy9HQ6XZV7z7WJYHWbDl3LznnobBELXk67wW8EThnl-sfC2sQwzIFeWqZexuR8mHj2-E8MzXtlmb6H3KWoABuXh_KZWfITnJkH8Z-gi9c-zBBMTPpiIyK0K4wlrL1LQ0Y3trpPjdpjIaIepPzcb4jGv6VUYPs6GBv32PLn225CswNrxECoXfE9Jy3cE9s-TSqo6Y-4WthCvCiAO1_oGWFCgBljkCXWb9fxmDDH9LGw9jMoyzQo7Z18otUXyUuBqjQmMxMYNqcJPH8PICdWMJ8eHh0v3KMFFWg4qOX-1YvXr-XLyEXEa6zCJRg-nUFRSiPcLdwysWWY3hzqxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه اسرائیلی: علت تکذیب سفر نتانیاهو به امارات، ترس از ایران است
🔹
شبکه ۱۲ اسرائیل گزارش داد که تکذیب سفر نتانیاهو از سوی مسئولان اماراتی‌ ناشی از ترس است؛ زیرا ابوظبی می‌ترسد به عنوان یک طرف در محور ضد ایران، ظاهر شود.
🔹
این شبکه با اشاره به ترس امارات از  تشدید تنش‌های منطقه‌ای، گزارش داد، ابوظبی نگران است که به خاطر روابط با اسرائیل، به هدف مستقیم حملات ایران تبدیل شود.
🔹
بنا بر این گزارش، امارات در تلاش است است که سطح حضور خود را در مورد روابط با اسرائیل نسبتاً پایین نگه دارد.
🔹
این شبکه می‌گوید اماراتی‌ها با این تکذیب به رسانه‌های اسرائیلی این پیام را دادند که روایت رسانه‌ای مربوط به روابط با اسرائیل باید کنترل شود.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/435582" target="_blank">📅 18:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435581">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-35.pdf</div>
  <div class="tg-doc-extra">3 MB</div>
</div>
<a href="https://t.me/farsna/435581" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-34.pdf</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/435581" target="_blank">📅 18:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435580">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K100jYzRL7DeZ7IkxootdsZX5BtNKuPEOTZYNQrCJAVss92IHa_uUw7R0pWHvbJJbuCRks9IYTwsBHHp4pkPVa3Pnmny2uKSTIBs8-aLU5ZI6ZiI76bU_EuNLmoQ9vhsyUK8R7I2Vr0vrW3zYyJHnHsWsXMffuFWwa2dUgRjLNin5M7JdTmmj3NFeUWxEYQe5NdGX75ax4dtV4Wy2tlRMdzy-gaGwJtfwTwvlSc7qaQkNGCZfwzl3Dm9THVDYOFBk_qgiUmp7WXbYGwXavCn-6oJXP0GpvgI7lmc74bt3zdSxjVoNPvYrky_Fk5JiGgVi4t-yPZ4MyStV5ULtIpFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: مردم ایران نشان دادند راه گذر از مشکلات، همبستگی ملی است
🔹
همانطور که مردم در جنگ ۴۰ روزه کنار هم ایستادند، دوران بازآفرینی را هم با همدلی و وفاق پشت سر خواهند گذاشت.
🔹
من از همه مردم برای این میزان موقعیت‌شناسی، فداکاری، ایثار و تلاش سپاسگزارم، ایران را با هم می‌سازیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/435580" target="_blank">📅 17:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435579">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Za2c7RsyZYcsICAnSFI2Lwqxuk4kxGjWua_bhhZuj88h7dbn1E5vzmdcdFgCIGXUictrGJHzWOhMqtGhgCrvY-RRYEBRBxxLB8a2oGbhS9avDwXGMxo9ES5wgQz4CDLziI6t7kDI9mPq4fwVUtQswv3meYpFlIgUerieibVWIjco1XEsmgWnXAf5Obb8v9aF3XnH59xATycSf8hCSiXLfuO_Bk04h-RsPzVmO7xK2QTefdKeTCs1RXX0WjtvG3XpGmW_uakPSLxZyLY3TWbstNO7fLKtYUz0tbIG5FMIqLT2SXVUK0lpsxD0FPazXR2pgU1svWHfEzKU-S9VBy-OLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی در دهلی‌نو با لاوروف دیدار و گفت‌وگو کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/435579" target="_blank">📅 17:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435578">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb2fdc28f.mp4?token=qg4pseYm5XGqrdLzY9vls7a3R_9uhs2ftE-GUJONAS_7-ZBVfZJiHX-XJcNG2EFRzlP4zxBjOYoeYgzf4Xf024M3G3Ecp7mt5yq3xDFMVXSzzgYtmkJsA55uH64qR0Eqnte57XqaWgVLHfBcLY1NE8Vvvf0zXRCzlGxMv6nFEBusoVaQc4lWgQsiYPEj3lp5ldEyNVsnafmR0AJNTIQL-5qHyLvtc-MhBO0-UrpVw6XtkrSp5Jp-9Tor_WNgE7OanxJVlX3LRAJMXK0yspR-6tAtO9Ac5M4GBlEI1JcpWBRZUY6VHtJ3BDqwB8qJ_jwBxIQbbYxBnx6IgshgSpBCbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb2fdc28f.mp4?token=qg4pseYm5XGqrdLzY9vls7a3R_9uhs2ftE-GUJONAS_7-ZBVfZJiHX-XJcNG2EFRzlP4zxBjOYoeYgzf4Xf024M3G3Ecp7mt5yq3xDFMVXSzzgYtmkJsA55uH64qR0Eqnte57XqaWgVLHfBcLY1NE8Vvvf0zXRCzlGxMv6nFEBusoVaQc4lWgQsiYPEj3lp5ldEyNVsnafmR0AJNTIQL-5qHyLvtc-MhBO0-UrpVw6XtkrSp5Jp-9Tor_WNgE7OanxJVlX3LRAJMXK0yspR-6tAtO9Ac5M4GBlEI1JcpWBRZUY6VHtJ3BDqwB8qJ_jwBxIQbbYxBnx6IgshgSpBCbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله تصاویر اصابت مستقیم پهپاد انتحاری به خودروی نظامیان صهیونیست را منتشر کرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/435578" target="_blank">📅 17:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435577">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca48112cfe.mp4?token=qAevsJTDsww3IywZFaJxblJq0b8-wfrM35lLe5cWDMXfj2WNSy6kjNVF5gRGy1mV_P9xdx-z3k4zKDgTRC3giyq95a4aK9kCFvmkT-N8yxjMt3B1qmK8M1VUXIPywnbH63K4UkJuwcvUjW22-ajmeqXDwVlHFe7q0OxVWa8bWwZDTF2rUOXGy4oUm33cVWMsUS6gAamPb43g29zHeAjdJ-tzRm-vEsDqE9Ib0-dEHp4vrTwuNav7fIhRwXO4M_Ec7-UPFybkBA11WGUhWjt1qOb7Ft7BeinNzWxmrzNyPBXkfbRD-cE5mfBvm-kh6Xz2R5dHCqv--Djt6mKedw2f3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca48112cfe.mp4?token=qAevsJTDsww3IywZFaJxblJq0b8-wfrM35lLe5cWDMXfj2WNSy6kjNVF5gRGy1mV_P9xdx-z3k4zKDgTRC3giyq95a4aK9kCFvmkT-N8yxjMt3B1qmK8M1VUXIPywnbH63K4UkJuwcvUjW22-ajmeqXDwVlHFe7q0OxVWa8bWwZDTF2rUOXGy4oUm33cVWMsUS6gAamPb43g29zHeAjdJ-tzRm-vEsDqE9Ib0-dEHp4vrTwuNav7fIhRwXO4M_Ec7-UPFybkBA11WGUhWjt1qOb7Ft7BeinNzWxmrzNyPBXkfbRD-cE5mfBvm-kh6Xz2R5dHCqv--Djt6mKedw2f3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله تصاویر اصابت مستقیم پهپاد انتحاری به خودروی نظامیان صهیونیست را منتشر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/435577" target="_blank">📅 17:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435576">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl1_u8cUtDvBDLHI7ew7hvwkx2VV3rBnTKbhO2ZOAu_7Tl2_Fkd_lzRGuSjqtuxEecd-e8Q4oXVXslSaLXhFhbNy6jQoABBwlpeCoGCiiM-rJWnaPNowzuJVkzTy6oPNZutr3JlH5b9xBo8v0uAeflK5mQ1ryuMBnY_CLWQdhYpMZ15C1kMzIQLhaEg4mE8hKAsKJ-x3DSG6I4IPB8WGTiKxTAPqxnCgn245GVBw-Co1RyNETMph_3ixqQq8TmM9Cj2G_MUIgfhrKG5zFg6UI9gOTcPqD2e9ZCMPXRKYn-8beeuzsS2u4HAquTZ_XYFHyZMYyiqf5fmNGo1zYUafnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عراقچی: ما هیچ مانعی در تنگۀ هرمز ایجاد نکرده‌ایم
🔹
تنگه هرمز اکنون بیش از هر چیز از تجاوز آمریکا و محاصره‌ای که بر آن تحمیل کرده، آسیب می‌بیند.
🔹
از نظر ما، تنگه هرمز برای تمامی کشتی‌های تجاری باز است، اما آن‌ها باید با نیروهای دریایی ما همکاری کنند.
🔹
ما…</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/435576" target="_blank">📅 16:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435575">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حزب‌الله: تجمعی از سربازان دشمن صهیونیستی را در شهر رشاف با گلوله‌های توپخانه هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/435575" target="_blank">📅 16:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435574">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVi-eiZ4hv3hNIH4TlrP0sutFTaT-z3uqlwL-_FhSLLX7_RmbKACnHIMs9ldOOvB3IxwQ13I_qdmBo5-FCSSsFWZD6a4JkIWn3CRcUD1J4aSJmdNhxakseEkt1hazNOTLQh9kK--81D-mLRqDwCFKTOhSbA8WScgwsAt05STzB2BWG1XvppA03DC_qCJyzduZVhP669sqlcm9W15jU97xUselILYunPJdLzsrkmR8SKvXr3YhFYOIwQx5EGVLsVUyOngK1TFcxeJv4zefma1Ote7Sd3qZDot8K2APYI0bLmLKQBsns4LP8IhuD8NEogzXSW2YTMZlvqSdokN1RZEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین پرونده کپی‌رایت ایران علیه آپارات
🔹
آپارات پس از ۱۳ سال فعالیت و انتشار بدون مجوز بخشی از محتوای صداوسیما، با پرونده‌ای مواجه شده که رقم خسارت آن به بیش از ۳.۶ همت رسیده؛ پرونده‌ای که از آن به‌عنوان یکی از بزرگ‌ترین دعاوی حقوق مالکیت محتوا در فضای دیجیتال ایران یاد می‌شود.
🔹
برای درک ابعاد ماجرا، اگر یک شبکه تلویزیونی دو سال شبانه‌روز برنامه پخش کند، حدود ۱۷ هزار ساعت محتوا تولید می‌شود؛ رقمی نزدیک به برآورد برخی رسانه‌ها از حجم آثار منتشرشده در آپارات.
🔹
یک منبع حقوقی به فارس گفته اختلاف صداوسیما و آپارات سابقه‌ای چندساله دارد و حتی پیش از ثبت شکایت رسمی در سال ۱۳۹۸ نیز تذکراتی درباره انتشار تولیدات تلویزیونی داده شده بود، اما روند انتشار ادامه یافت.
🔹
طبق رأی دادگاه، پخش بدون مجوز ۷۵۵ قسمت از آثار تلویزیونی در آپارات محرز شده، هرچند برخی گزارش‌ها تعداد کل برنامه‌های منتشرشده را حدود ۱۶ هزار قسمت برآورد کرده‌اند.
🔹
کارشناسان قضایی بخشی از خسارت را بر اساس حجم استفاده از محتوا، اثر آن بر درآمد تبلیغاتی و کاهش ارزش انحصاری برنامه‌ها محاسبه کرده‌اند؛ آن هم در شرایطی که مجموع درآمد سکوهای فعال کشور سال گذشته از محل ترافیک، تبلیغات و اشتراک به حدود ۱۳.۶ همت رسیده است.
🔹
آپارات در بیانیه‌ای اعلام کرده حدود ۶ سال پیش سامانه‌ای مشابه یوتیوب برای مدیریت حقوق محتوا راه‌اندازی کرده و از صداوسیما خواسته بود از این سازوکار استفاده کند، اما این پیشنهاد پذیرفته نشد.
🔹
در مقابل، کارشناسان حقوق رسانه معتقدند همان‌طور که آثار پلتفرم‌هایی مثل فیلیمو یا نتفلیکس بدون مجوز در سکوهای دیگر منتشر نمی‌شود، انتشار آثار صداوسیما نیز مشمول حقوق مالکیت است.
🔹
مطالعات جهانی نیز نشان می‌دهد عدم حمایت از مالکیت معنوی آثار کیفیت آن را کاهش می‌دهد و بهترین راهکار، ترکیب سامانه‌های هوشمند تشخیص محتوا، قرارداد رسمی میان پلتفرم‌ها و صاحبان اثر و تقسیم درآمد تبلیغاتی است؛ مدلی که هم از تولید محتوا حمایت می‌کند هم اختلافات حقوقی را کاهش می‌دهد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/435574" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435573">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4eaa8ed4.mp4?token=oqvtl74UEq3sR0CLVHzBU6gcC3b4SHMsj9gf4sJTK4zK_YNPTYzHYNrPCk78El5wP5Ay5NZ5HCcOb8hZXUDWBFypkycNjb5Kay6DdabFCH-B2-5PJhGMS3tNgtEHhIFpxlbe36rv-O_oZKON4IqbaLhUQT26pFdm6orCwR2M62OfYKxaKyDG_QQEhdCwsJhCacduuOkZhJBLHm8BzhvoWPMXDNL9HyUBm4Nfw9W-lwRv3soyZEbgX5zWCV9yfzZ8XiellWdwSymbK3C0YAwZLzVl4f9op7225aaiQBL254FJEeVbqLwehDFAroXpHaVwmlK9UKHRl-0FzoDjYjxrlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4eaa8ed4.mp4?token=oqvtl74UEq3sR0CLVHzBU6gcC3b4SHMsj9gf4sJTK4zK_YNPTYzHYNrPCk78El5wP5Ay5NZ5HCcOb8hZXUDWBFypkycNjb5Kay6DdabFCH-B2-5PJhGMS3tNgtEHhIFpxlbe36rv-O_oZKON4IqbaLhUQT26pFdm6orCwR2M62OfYKxaKyDG_QQEhdCwsJhCacduuOkZhJBLHm8BzhvoWPMXDNL9HyUBm4Nfw9W-lwRv3soyZEbgX5zWCV9yfzZ8XiellWdwSymbK3C0YAwZLzVl4f9op7225aaiQBL254FJEeVbqLwehDFAroXpHaVwmlK9UKHRl-0FzoDjYjxrlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستاده برای ایران…
@Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/435573" target="_blank">📅 14:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435572">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2a56d1d6.mp4?token=l697QViGp5cQh1YMs0DhcFpKmtNxaREVMEzAbof60HG1F2pDi6eBvboT9A6O0qnQovDfeRzEOFBkTdtEBZpzmO3g7SlRFIO2gWXGgRQJE_fe63ITEnGlUp8PpwZOdk4Fn-Xrup_6SH3Ai4UOsjeUvYD6JmV61cnBfr45bm9Zfgg6sE8TsaCBoSOs6V1HuCZqv2E36PZmor-8qZH0YwZlIgmP_zJFAxKlck5gDMk1XMhFejzr5NARuYdijSmy-EZDBDbzCNJXmoN3FEeKJXzJdFtB4XiL85cdFdJPUAJOXXI3ij5yVSNiY4cO-inexhmIaL1nYcDsWMJm9aBNSBePdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2a56d1d6.mp4?token=l697QViGp5cQh1YMs0DhcFpKmtNxaREVMEzAbof60HG1F2pDi6eBvboT9A6O0qnQovDfeRzEOFBkTdtEBZpzmO3g7SlRFIO2gWXGgRQJE_fe63ITEnGlUp8PpwZOdk4Fn-Xrup_6SH3Ai4UOsjeUvYD6JmV61cnBfr45bm9Zfgg6sE8TsaCBoSOs6V1HuCZqv2E36PZmor-8qZH0YwZlIgmP_zJFAxKlck5gDMk1XMhFejzr5NARuYdijSmy-EZDBDbzCNJXmoN3FEeKJXzJdFtB4XiL85cdFdJPUAJOXXI3ij5yVSNiY4cO-inexhmIaL1nYcDsWMJm9aBNSBePdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عارف: به هیچ قیمتی تنگۀ هرمز را از دست نخواهیم داد
🔹
اصلا تنگۀ هرمز مال ماست؛ ملک ما بوده حالا مدتی از ملکمان خوب استفاده نمی‌کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/435572" target="_blank">📅 14:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435571">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6fb1016c.mp4?token=vjX3yUnMrYIxuOw8tzXIWUZTFa2kSsoY7BanLpU_NlxfqbPI0Uw9YNXsysTyJoT0ux1W0Ok-cwDvUrS_IeF4BtgbU4bt2tv8M6dBa_orEgzJOXPvOfHp0ZjC0mwzss3t3mCqBZkQFTCZu0DdBDmJWQU2uIXBaUB_revQJWZG-9gi3RPlCaWo_SEG1Y2k3RqrzJII2T_lnH_rcKaRlLEP5YnlQI2RVH_pNJGVIk_4jg8FdXASnx1mECfSMnPRsqjpOJOf24IzBOoey02ncTu-UysQDx86Y5hew6AOvrPyf5ocmtdPSkr3GOibQMw3J2TbOAOWgob4zfOv238DD48lWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6fb1016c.mp4?token=vjX3yUnMrYIxuOw8tzXIWUZTFa2kSsoY7BanLpU_NlxfqbPI0Uw9YNXsysTyJoT0ux1W0Ok-cwDvUrS_IeF4BtgbU4bt2tv8M6dBa_orEgzJOXPvOfHp0ZjC0mwzss3t3mCqBZkQFTCZu0DdBDmJWQU2uIXBaUB_revQJWZG-9gi3RPlCaWo_SEG1Y2k3RqrzJII2T_lnH_rcKaRlLEP5YnlQI2RVH_pNJGVIk_4jg8FdXASnx1mECfSMnPRsqjpOJOf24IzBOoey02ncTu-UysQDx86Y5hew6AOvrPyf5ocmtdPSkr3GOibQMw3J2TbOAOWgob4zfOv238DD48lWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران، ترامپ را کت بسته به چین فرستاد
🔹
تصور کنید کاخ سفید، در میانه جنگی اقتصادی که به چین باخته، تنها برگ برنده‌اش را مشت آهنین ارتش می‌داند. آن‌ها می‌خواستند با حمله به ایران پیش از سفر ترامپ به پکن، یک پرونده بزرگ را با اتکا به ارتشی که ترامپ آن را افسانه‌ای…</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/435571" target="_blank">📅 14:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435570">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edbd824a7a.mp4?token=MrVe-b21ZUaXu9iL5UPBTvFbP7-xQtse25NClT1uyhecHePgBpFmiZro44xt702GrT8mTjp_ysoIh5OWMicmAikOBacG-kiHubDWPxvYP8uuJeGUWkHCfSlsXbxWaZuCffoOR9OvOUydPaBF2aZ4Tk5oFC9NlmD1YfFdhsT31IN3lOlD0RPx5e9Jm9D7k7-SQpdeXmzFVwFQ3YR2nsMJ9gzIPQjB5oZnm1gnwMEac35bkMHmaZgCJy1hCULwfRWsEKQcm_GOLmkrwLgvAe5v72hmFCO9aHszb9LhFEq4h8pXBM9BHFgIMxmvtkTv6eg6dUIkyVMTO8gUVzTpG6TJozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edbd824a7a.mp4?token=MrVe-b21ZUaXu9iL5UPBTvFbP7-xQtse25NClT1uyhecHePgBpFmiZro44xt702GrT8mTjp_ysoIh5OWMicmAikOBacG-kiHubDWPxvYP8uuJeGUWkHCfSlsXbxWaZuCffoOR9OvOUydPaBF2aZ4Tk5oFC9NlmD1YfFdhsT31IN3lOlD0RPx5e9Jm9D7k7-SQpdeXmzFVwFQ3YR2nsMJ9gzIPQjB5oZnm1gnwMEac35bkMHmaZgCJy1hCULwfRWsEKQcm_GOLmkrwLgvAe5v72hmFCO9aHszb9LhFEq4h8pXBM9BHFgIMxmvtkTv6eg6dUIkyVMTO8gUVzTpG6TJozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی خطاب به امارات: ائتلاف با اسرائیل هم از شما محافظت نکرد
🔹
وزیر امور خارجه امروز در نشست وزرای خارجه بریکس در دهلی‌نو در پاسخ به ادعاهای بی‌اساس نماینده امارات گفت: ائتلاف شما با اسرائیلی‌ها نیز از شما محافظت نکرد و در سیاست خود در قبال ایران بازنگری…</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/435570" target="_blank">📅 14:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435569">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d695d1f5.mp4?token=QLtDMeUcEU00HpHie397WWhvEJMla3-nHa_NxZYqR5yw751s7p9M0hrCroyCF6FuaUzUGYnQdO14XWnyoIarhPUQlLMJC-PE7LqQzWu2KKFemdA8BOhOA5BnzPQ8P2GBuRpF8H2_xTsOJ_oPs2-gSkM5hlNpODFoAMqzdv6xlrTKUD9GUaj496PIko7N8jQMYyPwG1Ib_g9rh3JKDAuxCDMnb67amsOcZAUvb-SAOSwNdtsW-X0SGnARqIDNDJjvTKp6fcBouiNfcsRzPNawzpy9DEUIycXBwa9-ygSvG5kyf6JvNMQ4Flnr_vrt5MQGjDZanVBwVq3wKR_Han8Bbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d695d1f5.mp4?token=QLtDMeUcEU00HpHie397WWhvEJMla3-nHa_NxZYqR5yw751s7p9M0hrCroyCF6FuaUzUGYnQdO14XWnyoIarhPUQlLMJC-PE7LqQzWu2KKFemdA8BOhOA5BnzPQ8P2GBuRpF8H2_xTsOJ_oPs2-gSkM5hlNpODFoAMqzdv6xlrTKUD9GUaj496PIko7N8jQMYyPwG1Ib_g9rh3JKDAuxCDMnb67amsOcZAUvb-SAOSwNdtsW-X0SGnARqIDNDJjvTKp6fcBouiNfcsRzPNawzpy9DEUIycXBwa9-ygSvG5kyf6JvNMQ4Flnr_vrt5MQGjDZanVBwVq3wKR_Han8Bbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آغاز عبور کشتی‌های چینی از تنگۀ هرمز از شب گذشته
🔹
به گزارش یک منبع آگاه، با تصمیم جمهوری اسلامی، امکان عبور تعدادی از کشتی‌های چینی از تنگه هرمز با رعایت پروتکل مدیریت ایرانی تنگه میسر شد.
🔹
بر پایه گفته‌های این منبع آگاه، پس از پیگیری‌های وزیر خارجۀ چین…</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/435569" target="_blank">📅 14:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435568">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabdb4251f.mp4?token=lVw1_DXbOmzQeSCu2rkIOgkROYIZFHGQ6w3vv2nkEzbFhbRhTj-6sGeYTdo4JTl7NFexkeNT3zQHQ7Jdz08d80FK75kEKFkrZ1qu05tgdD3iWhNbwY2wUq-8cL2sdGOtARObZXhe82hZVF9aiNDb75SyOF7AvpSYASGXkaBV04s-TfhUJhlPBNkLWzTlfLhMGqisuAqGD-cFOGwxFUsg9I0ZrTmfBKS3IyrKtAJ2PqPGDrP7AYPR1QcIniFrXPF-3bGh-2XCgoXA6I8dwYs3uNjwYCoEKnfZT9x2F0fVyPgVBpKKCz-fkP7iWySXl24vbQhpyNoJX_Dz4ok8JBb-7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabdb4251f.mp4?token=lVw1_DXbOmzQeSCu2rkIOgkROYIZFHGQ6w3vv2nkEzbFhbRhTj-6sGeYTdo4JTl7NFexkeNT3zQHQ7Jdz08d80FK75kEKFkrZ1qu05tgdD3iWhNbwY2wUq-8cL2sdGOtARObZXhe82hZVF9aiNDb75SyOF7AvpSYASGXkaBV04s-TfhUJhlPBNkLWzTlfLhMGqisuAqGD-cFOGwxFUsg9I0ZrTmfBKS3IyrKtAJ2PqPGDrP7AYPR1QcIniFrXPF-3bGh-2XCgoXA6I8dwYs3uNjwYCoEKnfZT9x2F0fVyPgVBpKKCz-fkP7iWySXl24vbQhpyNoJX_Dz4ok8JBb-7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خسوف اقتصادی برای دنیا با بسته شدن تنگۀ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/435568" target="_blank">📅 14:19 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
