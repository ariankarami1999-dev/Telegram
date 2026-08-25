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
<img src="https://cdn4.telesco.pe/file/uPx7a63hGcV4DJRwzKBBZIN5UOgz8_uj3jW3mRsuv7xvLTaPN9YJvuosNCoHP8dD2Betgdv-yexJoolpU07eeNrecnhXpzyYot708JNFrq2GiKrhJZxJBDTsL87quwuA1t12dsX-s1LSAr4_tYQcBzJLISiEUHLZomwssJ9nocyKZZEkiNWawH81aeu3bSvZBKRTDGRGnHtxPV4EvluY8WSmUTLkFqntX1VFh3H02Jwrm_c8uRelXQXCsXvJVGa78v7GPNXcer2QluMIJHKbzwfufmy1sINYbEPswKFElsQxBgeKlzqMJW8m0vHEQpAqtaLeZThU1z834bKysHXupw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 23:23:06</div>
<hr>

<div class="tg-post" id="msg-458250">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">غریب‌آبادی: همچنان در وضعیت جنگی قرار داریم
🔹
معاون حقوقی وزارت خارجه: تا پیش از جنگ‌های اخیر هیچ مشکلی در تنگه هرمز وجود نداشت و ایران نیز تمرکز ویژه‌ای بر مباحث مربوط به این آبراه اعمال نمی‌کرد.
🔹
پس از جنگ ۴۰ روزه، توجه و تمرکز راهبردی ایران به این موضوع…</div>
<div class="tg-footer">👁️ 348 · <a href="https://t.me/farsna/458250" target="_blank">📅 23:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458249">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">غریب‌آبادی: همچنان در وضعیت جنگی قرار داریم
🔹
معاون حقوقی وزارت خارجه: تا پیش از جنگ‌های اخیر هیچ مشکلی در تنگه هرمز وجود نداشت و ایران نیز تمرکز ویژه‌ای بر مباحث مربوط به این آبراه اعمال نمی‌کرد.
🔹
پس از جنگ ۴۰ روزه، توجه و تمرکز راهبردی ایران به این موضوع جلب شد و ما همچنان در وضعیت جنگی به سر می‌بریم.
@Farsna</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/farsna/458249" target="_blank">📅 23:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458248">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27ed05b57.mp4?token=qpccxg7VhP5AGH33f5BPl4JYzi-Whn2uzmwh4-zKS1rwwpiOIdRY7yul2AuaZc_qn-9LATV_0yfLr3tnxpleWoLbLwZbK3SZr3mWdJjF-2z6eewelk1xmWYwzdwv6RGYvzb1MWTad_3BAaLk0PvcMr6LFxFigKjLcht_mzGfGqc-a_cWeT8sY0uQC14AbLAEif1KwEjJyFhJUujK__3jyHknYZyg0MnG7w3XUpGfjNvhN5sDXlxvr4ugC3XSqHxJOfy6dRKd9NuI2R4KMznIkDJrKMh1Hby44S0pZpV0MoMZYTWR_akjxidKMFEmk-TcE45v82obEtlktvzligS5cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27ed05b57.mp4?token=qpccxg7VhP5AGH33f5BPl4JYzi-Whn2uzmwh4-zKS1rwwpiOIdRY7yul2AuaZc_qn-9LATV_0yfLr3tnxpleWoLbLwZbK3SZr3mWdJjF-2z6eewelk1xmWYwzdwv6RGYvzb1MWTad_3BAaLk0PvcMr6LFxFigKjLcht_mzGfGqc-a_cWeT8sY0uQC14AbLAEif1KwEjJyFhJUujK__3jyHknYZyg0MnG7w3XUpGfjNvhN5sDXlxvr4ugC3XSqHxJOfy6dRKd9NuI2R4KMznIkDJrKMh1Hby44S0pZpV0MoMZYTWR_akjxidKMFEmk-TcE45v82obEtlktvzligS5cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: قیمت برق فقط برای پرمصرف‌ها گران می‌شود
🔹
بدمصرف‌ها اگر این شرایط را ادامه دهند ممکن است در ماه‌های آینده قبض‌های سنگینی داشته باشند.
🔹
اگر کسی نیاز به مصرف بالا دارد باید به ما مراجعه کند تا از بورس انرژی برای او تامین کنیم. @Farsna</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/458248" target="_blank">📅 23:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458247">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdcc2e628e.mp4?token=RUDLZ4QHxu7ApRI4gSDu8Pi6XUR1uN_l5G5PSIp1o4IY0RjOtWVNWN3RA-OvAuR3hArUkPa18bbRdb7wnhswjaM3ltB7HtKPTaKZGURV3k_anZxbfRHog74v-Z7thpysa42Y9cmNIT40Q1CpCfUHmfAhbzoPuVJrrrHGKGg8CkuEgiAt68wqVZ-4Z-aTgEJgYH5AtlExn8LPYALaogJ2AlHcPWWMsm2S9Tc7vZmiGPAeUAlsdLeZaBbe_9iN8Z0ZP-Suqg8suDfq0JR3bYi5tsZD-3fk29uovh1CJ0mStk8RcDUtoKtsSjxH6WDoj1C3ZbgCz1kKuloRl1Nw-obMJIkWIP-aP80zi86xO7wfB6et5e4r274iExT6jGFJdDQpTwFzhWugZ_cJQgLFS2C7s49Pyw0_1OFSeupxlIz3QX_dJ9fjYrO0OULdTNXWx86x7V-220B4zj8jWbe0JJ12cZQ2MES3P39agf3cdyaCXtXHJ6pz4JUlIMCzP6_vD1EyBMAktR5z2D7US6M1D7i2TPuKjj9xnd2wpZ2rgyyXmZm4tFZdy9Tx8s7J29jWQ2DYHZO_nb7fdlGfK8UKgorR9RGWc9ShfI6G7jr2fgww5X_y7akJ4LSDCd4uEFZ4rCb2uqbXxSSVg0WHw3oWx-8Dk68Mm9baZo19crCLOvFx-s8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdcc2e628e.mp4?token=RUDLZ4QHxu7ApRI4gSDu8Pi6XUR1uN_l5G5PSIp1o4IY0RjOtWVNWN3RA-OvAuR3hArUkPa18bbRdb7wnhswjaM3ltB7HtKPTaKZGURV3k_anZxbfRHog74v-Z7thpysa42Y9cmNIT40Q1CpCfUHmfAhbzoPuVJrrrHGKGg8CkuEgiAt68wqVZ-4Z-aTgEJgYH5AtlExn8LPYALaogJ2AlHcPWWMsm2S9Tc7vZmiGPAeUAlsdLeZaBbe_9iN8Z0ZP-Suqg8suDfq0JR3bYi5tsZD-3fk29uovh1CJ0mStk8RcDUtoKtsSjxH6WDoj1C3ZbgCz1kKuloRl1Nw-obMJIkWIP-aP80zi86xO7wfB6et5e4r274iExT6jGFJdDQpTwFzhWugZ_cJQgLFS2C7s49Pyw0_1OFSeupxlIz3QX_dJ9fjYrO0OULdTNXWx86x7V-220B4zj8jWbe0JJ12cZQ2MES3P39agf3cdyaCXtXHJ6pz4JUlIMCzP6_vD1EyBMAktR5z2D7US6M1D7i2TPuKjj9xnd2wpZ2rgyyXmZm4tFZdy9Tx8s7J29jWQ2DYHZO_nb7fdlGfK8UKgorR9RGWc9ShfI6G7jr2fgww5X_y7akJ4LSDCd4uEFZ4rCb2uqbXxSSVg0WHw3oWx-8Dk68Mm9baZo19crCLOvFx-s8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو:  اگر اتفاق غیرمنتظره‌ای رخ ندهد تا ۹ ماه آینده مشکل برق نخواهیم داشت
🔹
تابستان سال آینده هم شرایط بهتری از امسال خواهیم داشت. @Farsna</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farsna/458247" target="_blank">📅 23:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458246">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84b7cdbcf7.mp4?token=LVjQEf4z-5lmmXyJ_agt1VgoviOceOGko8D5xWj4wEb6JpJxIlEKaODxByKktYznmyn5BBJbD2Mq8Zl5h7dgSyOM8EWk93WzzEMqHNdNSgS6yLJa1Egrooc3bO1FUG84mP6mioQLy3mG7abpBQBCedRIw4NlOcTwBAGMRZ6oiEcsyvAe-v-WaRWHKuTKKDPZYtfLdEoZScj9jEwaFzbY1-A7YCuqgYLpo67CUhBBYbx34Nsr3alx9bg5R2gDxbdYNY5zC_NHjo8jAbSOFOLqRJokabLLbpBByIEJxnf70A9Omz2HwxrummnPjQ1kC27WjndPP5GXlnMoVdyo2tLr9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84b7cdbcf7.mp4?token=LVjQEf4z-5lmmXyJ_agt1VgoviOceOGko8D5xWj4wEb6JpJxIlEKaODxByKktYznmyn5BBJbD2Mq8Zl5h7dgSyOM8EWk93WzzEMqHNdNSgS6yLJa1Egrooc3bO1FUG84mP6mioQLy3mG7abpBQBCedRIw4NlOcTwBAGMRZ6oiEcsyvAe-v-WaRWHKuTKKDPZYtfLdEoZScj9jEwaFzbY1-A7YCuqgYLpo67CUhBBYbx34Nsr3alx9bg5R2gDxbdYNY5zC_NHjo8jAbSOFOLqRJokabLLbpBByIEJxnf70A9Omz2HwxrummnPjQ1kC27WjndPP5GXlnMoVdyo2tLr9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضدانقلاب این‌بار یک «پل چوبی» را دستاویز دروغ‌هایش کرد
🔹
برخی رسانه‌های ضدانقلاب با انتشار ویدیویی از وضعیت نامطلوب یک پل چوبی در روستای ساتره بخش مرزن‌آباد چالوس ادعا کردند که این پل تنها مسیر ارتباطی اهالی روستا با مناطق اطراف است و وضعیت نامناسب آن دسترسی ساکنان را مختل کرده است.
🔸
مسئولان محلی ادعاهای مطرح‌شده پس از انتشار ویدیویی از پل چوبی را رد کردند و تأکید کردند که این پل تنها مسیر ارتباطی ساکنان روستا نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/farsna/458246" target="_blank">📅 23:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458245">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049564136a.mp4?token=PqlR4w6ab-JujANuIk707sZB9WLXWtL8ba5hdt1jh5sE00JniTsvBnFMpcX_NHxfZzr5oi2mUgY5myRk9rRAc-3agrt5ZLmYq2TARopU7AHlERzR4NOzDwQYow4RcuHalvrob_jXwrxO8cvTqhctHpbwsqTyXVzMLuMZ2Bvr_g4b95q23roF83gWpSLTeajkYHDsdvQw7xFDC2YDptQsbjmyf0FvLbja9u-8-WFe4JrbNrhBYaEM0-dSdDFwjf_-Wip-9qtHLehz8Dohk8NZGWEYgP-N3cCuPtCtbeYICAZfjcZPbjBpSo609Bs3woPL8l7VzOA9qnjRrKLiUN1ebw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049564136a.mp4?token=PqlR4w6ab-JujANuIk707sZB9WLXWtL8ba5hdt1jh5sE00JniTsvBnFMpcX_NHxfZzr5oi2mUgY5myRk9rRAc-3agrt5ZLmYq2TARopU7AHlERzR4NOzDwQYow4RcuHalvrob_jXwrxO8cvTqhctHpbwsqTyXVzMLuMZ2Bvr_g4b95q23roF83gWpSLTeajkYHDsdvQw7xFDC2YDptQsbjmyf0FvLbja9u-8-WFe4JrbNrhBYaEM0-dSdDFwjf_-Wip-9qtHLehz8Dohk8NZGWEYgP-N3cCuPtCtbeYICAZfjcZPbjBpSo609Bs3woPL8l7VzOA9qnjRrKLiUN1ebw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌آبادی: مبلغ قبض برق ۷۵ درصد مردم اندازۀ قیمت یک پیتزا هم نیست
🔹
ما از ۸۷۶۰ ساعت سال فقط حدود ۱۰۰ ساعت کسری داریم.
🔹
هر کسی بخواهد برق او قطع نشود می‌تواند از بورس انرژی برق خریداری کند. @Farsna</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/458245" target="_blank">📅 23:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458244">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235d2387c4.mp4?token=SXUMON1RXG0cbDLeWL9ADBV1oiZajHg6digmiCcLmbjYMQevupJ2s1-N6ksNyVPQA_7zzAzMywTvqG373xxl1p7WmWn91l8e9pKno8Q4q440kZLjTHaxgxqq_qicqCksUuZv_TtbADUV9JXu6BspYBWDX08yteCY8YTznlU0-nY7y_6XOR6AkhR244S_gLYw5ApzADu_L9JjN0cD-a8wo0dm8xt9G2PV3IalWdqpoXcuapaeih4rzAlfI6e80G-viifFXoFDI9bkhZfEnorSqL-OWl1aIU8avqj9EpNyz5eppCu6mC4_R5BBpoHaZ0kxT5oejDEKbeQ_DKdUILcIdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235d2387c4.mp4?token=SXUMON1RXG0cbDLeWL9ADBV1oiZajHg6digmiCcLmbjYMQevupJ2s1-N6ksNyVPQA_7zzAzMywTvqG373xxl1p7WmWn91l8e9pKno8Q4q440kZLjTHaxgxqq_qicqCksUuZv_TtbADUV9JXu6BspYBWDX08yteCY8YTznlU0-nY7y_6XOR6AkhR244S_gLYw5ApzADu_L9JjN0cD-a8wo0dm8xt9G2PV3IalWdqpoXcuapaeih4rzAlfI6e80G-viifFXoFDI9bkhZfEnorSqL-OWl1aIU8avqj9EpNyz5eppCu6mC4_R5BBpoHaZ0kxT5oejDEKbeQ_DKdUILcIdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: روی آنتن زنده از مردم خواستم به‌خاطر استان‌های جنوبی صرفه‌جویی کنند؛ ناگهان ۲ هزار مگاوات از بار شبکه کم شد
🔹
من همان‌جا گفتم پای این مردم را باید بوسید؛البته از مردم ایران همین هم توقع می‌رود. @Farsna</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/458244" target="_blank">📅 22:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458243">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E02-99X5_aYMCojqssAMYZpbF6ckkIJN9puMaWEUUe3Wx8fNr5PNLeujFG0UNV_9o9G-xare-PcCHgiIrEanSVV61k6xD_newpUgAZyctUGhbVLF27XiLGOMoL0HO-zs9A7tue9dck_7O9VP83Lh2twnqAWFLe3_f-DiXB51vWSW7wnNBfhj21DpD4i2KPXmH2r8chD8dLJ4aTom8afTUb0yv3DITqvUSp0TIM_nyRrhKr2BAOXY4YoFc8ExY-r1zNnmQsapbZaQPGryD0PzmWhjKIL_n9xX5uIXdK2bT1fpn8jnzW_ryIU3iqW0LHg1K4pYCH0CaJo5kNJiv7PVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: با دیپلماسی با همسایگانمان تعهد به صلح را دنبال می‌کنیم
🔹
وزیر خارجه پس‌از دیدار با مقامات پاکستان و عمان: تعهد ایران به صلح و ثبات، همراه با دیپلماسی استوار و مستمر با همسایگانمان دنبال می‌شود.
🔹
در گفت‌وگو‌ با میهمانان پاکستانی و عمانی، بر راه‌حل‌های منطقه‌ای تأکید شد.
🔹
چهارچوب پیشنهادی برای ایجاد یک کریدور جدید، مین‌روبی مشترک و مدیریت آتی تنگه هرمز، نمونه‌ای روشن از این رویکرد است.
@Farsna</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/458243" target="_blank">📅 22:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458242">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkFq4FYcRU7GGda3mKhdlffL9xwEoDVu5ZX_u0wqBb0eOlAZcKU_Ug2F8gWsNxwduCWuC9xc0f1mSXzOs0Rzlu99Hf_2FlOuN4z83UlLPG8XLMu-Qs16nGpBdhlXbXgDxOGtVsidl9NAOZnqNM51xExuRv1OUA1LFuMYhBGlb2FqzCDuBDiyqj1bwv-Hafpd4e31_RotrnYyGLmVG-m280egzHRm--iLSMpASW_1RtUeCDJPvYKsgzWUNKnp-05fovj45IvKvEFZTrPRI0U4DjXl-AanwwkX5m_A4zjnFNwlvSY_oODzAKsxDN9gqEsCOhPIKKBRGFOO4D2kC6uAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف به بسنت: نمایش مضحکت «روز پیروزی» نبود، «روز دلقک» بود!
🔹
وزیر خزانه‌داری آمریکا که ادعا کرده بود تحریم‌های جدید علیه ایران مانند «عملیات نورماندی (D-Day)» کوبنده و سرنوشت‌ساز خواهد بود، در نشست خبری دیروز به سؤال خبرنگار درباره توخالی‌بودن این ادعا پاسخ داد: مگر من می‌خواهم اقتصاد جهان را منفجر کنم؟!
🔹
قالیباف در واکنش به این سخنان نوشت: این برنامه اصلاً شبیه عملیات نورماندی نبود؛ یک استندآپ مضحک در کلاب شبانه بود که در آن حتی دیالوگ‌های طنز خودت را هم فراموش کردی!
@Farsna</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/458242" target="_blank">📅 22:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458241">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ac54f50d.mp4?token=smBLnfiZAfxRtM9htzKV7G00WaiOGaS197upP-DIku2shi628BwIXw9zkmxEQOtH8nw8uyTlFSwkNdN5lfYVAT4X9FbSODLxYP8UOBZPG643SzhDmB2cD6tBM-BN5roC3SdMcn2NqD_165fHY3P11msbgJI9NR9cmMAksCuQw-bWvdNamQcEPI5UDCvpRoGMGowTaW-n0xWl8d8bqkkxtB_t0XHPCK-3aihirc7vo955K6tWJWZ6dfZkIx17hH7wwZjWo4ImNcGEPRBwR21-KwOP7DbMTq1klm2kfE9STfJAJndYi2i0hhbgu7Nmy7nO8NziU70FCIsYTjK67OOwtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ac54f50d.mp4?token=smBLnfiZAfxRtM9htzKV7G00WaiOGaS197upP-DIku2shi628BwIXw9zkmxEQOtH8nw8uyTlFSwkNdN5lfYVAT4X9FbSODLxYP8UOBZPG643SzhDmB2cD6tBM-BN5roC3SdMcn2NqD_165fHY3P11msbgJI9NR9cmMAksCuQw-bWvdNamQcEPI5UDCvpRoGMGowTaW-n0xWl8d8bqkkxtB_t0XHPCK-3aihirc7vo955K6tWJWZ6dfZkIx17hH7wwZjWo4ImNcGEPRBwR21-KwOP7DbMTq1klm2kfE9STfJAJndYi2i0hhbgu7Nmy7nO8NziU70FCIsYTjK67OOwtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: ما آن‌قدر نیروگاه داریم که حتی اگر دشمن تمام توان خود را به کار بگیرد، نمی‌تواند همهٔ نیروگاه‌های ما را هدف قرار دهد.  @Frasna</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/farsna/458241" target="_blank">📅 22:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458240">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-KO7IVUYXeJik-nusu-TeUuf9z-EBwyAcYpLLwECUOqf2k7x9ByJZf5GGPuMiMM0Jzx8qEwvdOdHdbJgX1XVbw9ew5qG6pBzPpb-T1pNgK9tOYrHaVPWb7aXpMx-9-Wets4WcHnNpMf7Q-CgmPczfza0ALax4mSDVo4ssyhkxJFgleWEp0G3oiSBESntVaIXj0JzWiq5axGbWXu0kb4dxpJYRbXpv2mWbh5JYm65olqD7dTFZt_dhjam9akS7C0Irs5nSMkL8dkmW_xflrz1cCfTO0km8LuBQcvMXb7BznfIVGB4aD9OOW-CcLKwdsiEHMf9wm-bCWIstsh4-03vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلایی که دابسمش‌های سمی سر کودکان می‌آورد
🔹
درحال گشت‌وگذار در شبکه‌های اجتماعی هستیم که ویدئوی پربازدیدی توجه ما را جلب می‌کند
🔹
دختربچه‌ای خردسال، با ژست‌هایی کاملاً زنانه درحال اجرای یک دابسمش با آهنگی است که محتوای آن سراسر خیانت، روابط پنهانی و مفاهیم سخیف جنسی است.
🔹
شاید در نگاه اول، این فقط یک بازی کودکانه برای جذب دنبال‌کننده به نظر برسد؛ اما واقعیت تلخ این است که تکرار این کلمات و حرکات، بذر بی‌حیایی و بی‌عفتی را در ناخودآگاه کودک می‌کارد.
🔹
وقتی یک مفهوم سخیف برای دختربچه ما عادی شد، او در دوران نوجوانی به‌راحتی طعمه آسیب‌های اجتماعی و سوءاستفاده‌های عاطفی می‌شود.
🔸
برای اینکه فرزندتان را از این باتلاق مجازی بیرون بکشید و اصالت و وقار را به او هدیه دهید، این تکنیک سه‌مرحله‌ای را با هوشمندی به کار ببندید:
🔹
هرگز گوشی موبایل و اینترنت آزاد را به‌عنوان پرستار کودک رها نکنید. شما باید خلبان اصلی پرواز فرزندتان در فضای مجازی باشید.
🔹
اگر روزی متوجه شدید فرزندتان در حال زمزمه‌کردن یک آهنگ سخیف یا اجرای یک رفتار ناهنجار است، هرگز فریاد نکشید و او را با کلماتی مثل «بی‌حیا» برچسب نزنید.
🔹
در این شرایط، یک انسان مقتدر غرور بی‌جا را کنار می‌گذارد و پیش از آنکه کودک به سن نوجوانی و بحران‌های حاد برسد، از یک روان‌شناس کودک و مشاور امین کمک می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/458240" target="_blank">📅 22:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458239">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3cc1597a2.mp4?token=M2YWoBny11MfBGPrUWmwTSUFXj0VBjlRdlcQzZGgaOi65MJfJ1VgshglNwFwAz-cDXPpMDSM99IdZypzMe4fOP1w99snIxgS2sKZjXJehWIe7EiCSW0rlHHDOEDF0YS1QCryFX2MLFIeHMU9s34Uz_-sTlNB9svaOUS5fcS9q6ZQYAMmbXh9zhorSJ04nXXg39KL9v7cRZjqKV7lAKrcPAlsLDqMDbCm3Kr1Rdh37kv7SSyOjDmH-GioBMbVXbmJio82AWUPeEQjPP7oVGNSv_Sw11om3Ey_QwjPZ_t6F7x_O4O-qeSSPExf1cDG-mELz5hvx4qhHRqNrLXKgVy3cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3cc1597a2.mp4?token=M2YWoBny11MfBGPrUWmwTSUFXj0VBjlRdlcQzZGgaOi65MJfJ1VgshglNwFwAz-cDXPpMDSM99IdZypzMe4fOP1w99snIxgS2sKZjXJehWIe7EiCSW0rlHHDOEDF0YS1QCryFX2MLFIeHMU9s34Uz_-sTlNB9svaOUS5fcS9q6ZQYAMmbXh9zhorSJ04nXXg39KL9v7cRZjqKV7lAKrcPAlsLDqMDbCm3Kr1Rdh37kv7SSyOjDmH-GioBMbVXbmJio82AWUPeEQjPP7oVGNSv_Sw11om3Ey_QwjPZ_t6F7x_O4O-qeSSPExf1cDG-mELz5hvx4qhHRqNrLXKgVy3cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: یکی از هنرمندان در زمان جنگ به ما گفت می‌خواهم به نیروگاه بروم و آنجا ساز بزنم
🔹
زمانی که جنگنده‌ها وارد آسمان کشور شدند، با زحمت توانستند او را از نیروگاه خارج کنند. @Farsna</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/458239" target="_blank">📅 22:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458238">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d787a763.mp4?token=GTIK4nAhrsR2JnP-Rwwi5M9Q5VjPtBGwq3SnRsgkwpa4z2znceEq1YX9iwz00rutaUg9Hymqj2zdLy-3i5YYWZMdRkStVLMYk5xdjvkl6jEJgp3C1yZy07NsVO5Vb12q9wISjrfwXpYLvdinLEhWZZxGROx9VmufuPaw8j84gr9rrccTPGk3-DAK53tBMnww0IUl91uBPUpXDlkXTye3W7HvSD8VPMqHd5EslKvCXHwyzr24T_fZt1uQwExpgwjD6mwIRxkce--WCbaE-a2uR5aFLiluRFYVP38sq7zVXBJRZzQxt8dYRHTgvM8qo4Acw09ykMKCmPmxqBQIRacXEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d787a763.mp4?token=GTIK4nAhrsR2JnP-Rwwi5M9Q5VjPtBGwq3SnRsgkwpa4z2znceEq1YX9iwz00rutaUg9Hymqj2zdLy-3i5YYWZMdRkStVLMYk5xdjvkl6jEJgp3C1yZy07NsVO5Vb12q9wISjrfwXpYLvdinLEhWZZxGROx9VmufuPaw8j84gr9rrccTPGk3-DAK53tBMnww0IUl91uBPUpXDlkXTye3W7HvSD8VPMqHd5EslKvCXHwyzr24T_fZt1uQwExpgwjD6mwIRxkce--WCbaE-a2uR5aFLiluRFYVP38sq7zVXBJRZzQxt8dYRHTgvM8qo4Acw09ykMKCmPmxqBQIRacXEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: یکی از هنرمندان در زمان جنگ به ما گفت می‌خواهم به نیروگاه بروم و آنجا ساز بزنم
🔹
زمانی که جنگنده‌ها وارد آسمان کشور شدند، با زحمت توانستند او را از نیروگاه خارج کنند.
@Farsna</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/458238" target="_blank">📅 22:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458237">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febdb381d4.mp4?token=XfnZsXZapcAqYcWu7rVWQRbzDJwTHRo4RCY7TStp2mz-TLbgsm8ZkLJSYgbg0-uAFkhtoSAySJVl08ExHgxdLrXP56qf80sVqW9NVmoomCJIzYCpeKiZ5gof3lAgdyv5sWP8ryOZMV1LCqXhfidXZqW4nqVYhvZ6-AeizZVf9AIevOHteyq0pg2fIRqZGtOT1JhWmSCL6ZJ8JF-Lmdhq2l0Sbk5i9RpgqI4Tb5qAsDSC-om2pSEOrfVEzCXgXI7bNBQ75DQ5jG5ypX3YFxvYWDZUElgiMRAlyNe7OIGBIeFgjuabkF9sP6XO5wwjzK5NysE3g_qcQjmNsjoewxLjfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febdb381d4.mp4?token=XfnZsXZapcAqYcWu7rVWQRbzDJwTHRo4RCY7TStp2mz-TLbgsm8ZkLJSYgbg0-uAFkhtoSAySJVl08ExHgxdLrXP56qf80sVqW9NVmoomCJIzYCpeKiZ5gof3lAgdyv5sWP8ryOZMV1LCqXhfidXZqW4nqVYhvZ6-AeizZVf9AIevOHteyq0pg2fIRqZGtOT1JhWmSCL6ZJ8JF-Lmdhq2l0Sbk5i9RpgqI4Tb5qAsDSC-om2pSEOrfVEzCXgXI7bNBQ75DQ5jG5ypX3YFxvYWDZUElgiMRAlyNe7OIGBIeFgjuabkF9sP6XO5wwjzK5NysE3g_qcQjmNsjoewxLjfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۷۸ شب حضور؛ مردم همچنان پای عهد خود ایستاده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/458237" target="_blank">📅 22:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458236">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a53bd01c80.mp4?token=mIamlku-vSUo4T7EfFThPt3z9aFY6uwUWMuuLkx343e9yoPj_FkOcfhdmS1FYgaB-x6P36kfoMQMtRdMTfxevs0laVA8mqmsqqST0S8aMf2DaB-QWeQGS5pWz7_As46dFAxh23SuIKqbDsSg9SDhYSryKCs8iyJjipz3r-FSiHofOre3L0G2n2VnouGHecrOkaDwllnhd9ALhP_sHP_QoS_zgQk2Lldaz6kyE07U_anYtS90AobqTdQ8-t4WzId1igSxtONYV16csl1dL6-rK4-UQry6KNL1xbKdvP6rNUcmbtOm8u5gRRYRgdIYbk5-hZflfkV7lDCKiUyEzLCAdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a53bd01c80.mp4?token=mIamlku-vSUo4T7EfFThPt3z9aFY6uwUWMuuLkx343e9yoPj_FkOcfhdmS1FYgaB-x6P36kfoMQMtRdMTfxevs0laVA8mqmsqqST0S8aMf2DaB-QWeQGS5pWz7_As46dFAxh23SuIKqbDsSg9SDhYSryKCs8iyJjipz3r-FSiHofOre3L0G2n2VnouGHecrOkaDwllnhd9ALhP_sHP_QoS_zgQk2Lldaz6kyE07U_anYtS90AobqTdQ8-t4WzId1igSxtONYV16csl1dL6-rK4-UQry6KNL1xbKdvP6rNUcmbtOm8u5gRRYRgdIYbk5-hZflfkV7lDCKiUyEzLCAdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم مراغه ایستاده در سنگر خیابان در ۱۷۸ شب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/458236" target="_blank">📅 22:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458235">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5327c0708f.mp4?token=ewg_a1ST8zPPvUup6BZwy50P9WzdvFAqhnStjrdPUd56Zt_6GserARiwHAiPpriZG0b2hRmM8zukLQ9-2vvqcS6owqF5FvLBbKaoo80lexxNu08d7D7cXT7dxTuU4nghhae-RFq7Y1SBe-83B-BHBBAwqp3y7dsrFKQwVfSb6jFu1sz1Q0DOLPRULNbV3LWrj5p3RMt90st-a0d1cBaYDg3L6DwFK5STSFhg5qKUjeeYjX9UayKDjAmNmELczUEh_e7N1L-HWkKbLScsDiWxb4BB8v1x2_V-YBz3sjhNSzaOhTMSl77WMf-jrwEGXmLwsDzaf7_h5u38-9rd3BR28g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5327c0708f.mp4?token=ewg_a1ST8zPPvUup6BZwy50P9WzdvFAqhnStjrdPUd56Zt_6GserARiwHAiPpriZG0b2hRmM8zukLQ9-2vvqcS6owqF5FvLBbKaoo80lexxNu08d7D7cXT7dxTuU4nghhae-RFq7Y1SBe-83B-BHBBAwqp3y7dsrFKQwVfSb6jFu1sz1Q0DOLPRULNbV3LWrj5p3RMt90st-a0d1cBaYDg3L6DwFK5STSFhg5qKUjeeYjX9UayKDjAmNmELczUEh_e7N1L-HWkKbLScsDiWxb4BB8v1x2_V-YBz3sjhNSzaOhTMSl77WMf-jrwEGXmLwsDzaf7_h5u38-9rd3BR28g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی حرف خیابان‌ها در شب ۱۷۸، یک کلام شد؛ «انتقام»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/458235" target="_blank">📅 22:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458234">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
ما جمعی از متقاضیان پروژه ۲۵۶ واحدی نهضت ملی مسکن در صومعه‌سرا (گیلان) هستیم که از سال ۱۳۹۹ ثبت‌نام کرده و هر نفر ۳۶۰ میلیون تومان در بانک مسکن واریز کرده‌ایم. مسئول پروژه اداره کل راه و شهرسازی گیلان و پیمانکار شرکت پایاسازه پاسارگاد است. با وجود پیگیری‌های فراوان و گزارش به نهادهای نظارتی و شورای تأمین شهرستان، هیچ اقدام مؤثری انجام نشده و زمان تحویل همچنان نامشخص است. متقاضیان عمدتاً مستأجر و از قشر ضعیف هستند. تا چه زمانی باید منتظر بمانیم؟ از شما تقاضای ورود و پیگیری جهت احقاق حقوق عامه را داریم.
🔸
برای ثبت‌نام فرزندم در پایه هفتم به آموزش و پرورش منطقه ۴ مراجعه کردم، اما امکان ثبت‌نام فرزند من و بسیاری از والدین در این پایه میسر نبود. مسئول مربوطه اعلام کرد که این پایه بیش از ۱۰۰۰ نفر اضافه شده و به دلیل اینکه پیش‌بینی این تعداد دانش‌آموز را نداشته‌اند، به مشکل خورده‌اند و ثبت‌نام فرزند من بلاتکلیف مانده است. لطفاً به وزیر انتقال دهید. ما باید چه کنیم؟
🔹
از بندرعباس پیام می‌دهم. بنزین آزاد در جایگاه‌ها نمی‌دهند. این ۱۲۰ لیتری که گذاشته‌اند همان چند روز اول تمام شد. سرویس حمل‌ونقل عمومی هم به اندازه کافی در سطح شهر و همه خیابان‌ها وجود ندارد. خیلی از مسیرها تاکسی ندارد و مسیرهای طولانی را باید طی کنیم. مجبوریم از خودرو شخصی استفاده کنیم. لطفاً این پیام را هر طور می‌توانید پخش کنید.
🔸
ما کارگران مستأجر باید دردمان را به کی بگوییم؟ کی مسئول این اوضاع آشفته مسکن است؟ من با دو تا بچه چه کار  کنم؟ شما را به خدا اگر از دستتان برمی‌آید، صدای ما قشر مظلوم جامعه را به گوش بالادستی‌ها برسانید، شاید فکری به حال این وضعیت بکنند.
🔹
چرا وزارت صمت این شرکت‌های خودرویی را به حال خود رها کرده تا هر کلاهبرداری که دوست دارند انجام دهند؟ مهرماه ۱۴۰۳ از فردا موتور یک خودروی SX5 پیش‌خرید کردم و مبلغ ۵۰۰ میلیون تومان پرداخت کردم. طبق قرارداد می‌بایست سه‌ماهه خودرو را تحویل می‌دادند. الان دو سال از آن تاریخ گذشته و هر بار یک دروغ جدید می‌گویند. آخرین حرفشان این است که جنگ شده و اصلاً این خودرو را دیگر نداریم؛ بعداً جایگزین و شرایط خریدش را اعلام می‌کنیم.
🔸
در خصوص کسب‌وکار اتباع در کشور پیگیری شود. چرا آن‌ها بدون مدرک می‌توانند کسب‌وکار راه بیندازند اما یک ایرانی باید اسیر کلی قانون دست‌وپاگیر باشد؟
🔹
لطف می‌کنید از شرکت فردا موتورز که بالای ۱۰ هزار ثبت‌نامی خودرو و معوقات بالای دو سال دارد، خبر انتقادی بگذارید تا به گوش مسئولین کشوری برسد و به داد مشتریان بیچاره برسند.
🔸
از خواف مشهد پیام می‌دهیم. حدود ۵۰۰۰ نفر برای زمین‌های امتیازی و ساخت مسکن ثبت‌نام کرده‌اند، اما هنوز در بلاتکلیفی به سر می‌برند؛ الان سال چهارم بلاتکلیفی است.
🔹
من از فروشگاه زنجیره‌ای خرید کالابرگ انجام دادم. همان‌طور که می‌دانید باید ۵ هزار تومان (به‌صورت یکجا) کسر شود، اما یکی از شعبات یک‌بار ۲ هزار تومان و یک‌بار ۳ هزار تومان از من کسر کرد. این موضوع باعث کاهش شفافیت می‌شود و کار اشتباهی است.
🔸
بنده ۶ ماه است که برای نقل‌وانتقال مسکن مهر فاز ۸ اقدام کرده‌ام. همه مراحل از طریق عمران شهر پردیس انجام شده و به مرحله فرم ج رسیده‌ام. ۶ ماه است که در سامانه املاک و مستغلات قطعه می‌خوریم و نمی‌توانیم استعلام بگیریم. می‌گویند شما نباید مبلغی پرداخت کنید چون ملکی به نامتان نیست، اما بعد می‌گویند ۴۰ میلیون تومان پرداخت کنید تا کارتان انجام شود.
صدایمان باشید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/458234" target="_blank">📅 22:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458233">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d5b024e0.mp4?token=TNbOudXzp1v5VtBrQhTuKEhXcRuhKxt2vCXmxW11FV3-QZ-oBnuaVyoIvc43jCtSpOanexOecf4EdthuxWRLICO11A060NzoI0udAs8-fzdEeQH637RHVfSvluub-tslp8JoCbGaK93HJXyHt1d1TIECLwe_psBqpfUpR7ySuO9iqVqcoZUBcfG4ndThKyuZO-Oa-e7a-HtRsb5Km5I5Vo_wqBp7pE069hCHnlhkoREwc-qrKtZOgjVc7i5LanZd9_w-lum9MXl9-9d-CCF7jr6FTazTK-75ig2JSvc7Uud6FwPYwijBSIVSL7yKnvS5xtMBKttl8lUFQOaEr9AIpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d5b024e0.mp4?token=TNbOudXzp1v5VtBrQhTuKEhXcRuhKxt2vCXmxW11FV3-QZ-oBnuaVyoIvc43jCtSpOanexOecf4EdthuxWRLICO11A060NzoI0udAs8-fzdEeQH637RHVfSvluub-tslp8JoCbGaK93HJXyHt1d1TIECLwe_psBqpfUpR7ySuO9iqVqcoZUBcfG4ndThKyuZO-Oa-e7a-HtRsb5Km5I5Vo_wqBp7pE069hCHnlhkoREwc-qrKtZOgjVc7i5LanZd9_w-lum9MXl9-9d-CCF7jr6FTazTK-75ig2JSvc7Uud6FwPYwijBSIVSL7yKnvS5xtMBKttl8lUFQOaEr9AIpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزه مقاومت: حملات رژیم صهیونیستی به جنوب لبنان و منطقه علی‌الطاهر با شدت ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/458233" target="_blank">📅 22:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458232">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f2bf22e1b.mp4?token=uDnDTWITDsNMEhiB8TMZJZfqdJlPVgOs0ZdhBFLdtuUDnRLWsBeG_faW4aunCUoh_BWrsIhTLu6FPbGdWu_6p24sRLrjqCkyBT-7PILkXmnNQ4BOsyzydsDAe3xggC5E3TwZdqRAIpsT5TJmt9NKTy8kf72Dsd00w4I3_NKxf5R6q_BpJwxkgZcedupYUY0PMLbuBpDIoGeh2RbQHoJrpnolh-Nfo95LHvqD9oEM7HFdxdkA7lZKXifYv_n3qNik7I15xDA5uq5j2OkFnHPyMrHNABhR6Z2vIsnHc1-j6HebALxHYUIuYwPsY47xQPoczEn5QMlhlgtrUcKeq_IsDHqHBBHXxtAWtn7twSOWOyzq_UnrHy7XnP6jBli0bwv46VMTE9gT_eHqpYzQtMBzqz011QbnCGctbmYBpft6enkzxbI45P_kzMBHNEmd-r6rSiP8IDgj_CE7nJrTzRP05g-hj8uySI4WG94pITAl38cwCfhKFen1Dmp7oD-Z4A3azYPglrtr0OW8_OwzmnZ7xrILgRtYtZ9ORmeP0gIwNwKfVlU-gdoXP_6xXlNSQF4Q25adLsYDv-F300lii7Zi5q2Ul48ppM0CZnaUw2I7HgrOUSTDWPrXrhMXt1OECWhedmTEV74ddemrnaMK77uJiZhzuFs_OjyWE8cNPRaMn2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f2bf22e1b.mp4?token=uDnDTWITDsNMEhiB8TMZJZfqdJlPVgOs0ZdhBFLdtuUDnRLWsBeG_faW4aunCUoh_BWrsIhTLu6FPbGdWu_6p24sRLrjqCkyBT-7PILkXmnNQ4BOsyzydsDAe3xggC5E3TwZdqRAIpsT5TJmt9NKTy8kf72Dsd00w4I3_NKxf5R6q_BpJwxkgZcedupYUY0PMLbuBpDIoGeh2RbQHoJrpnolh-Nfo95LHvqD9oEM7HFdxdkA7lZKXifYv_n3qNik7I15xDA5uq5j2OkFnHPyMrHNABhR6Z2vIsnHc1-j6HebALxHYUIuYwPsY47xQPoczEn5QMlhlgtrUcKeq_IsDHqHBBHXxtAWtn7twSOWOyzq_UnrHy7XnP6jBli0bwv46VMTE9gT_eHqpYzQtMBzqz011QbnCGctbmYBpft6enkzxbI45P_kzMBHNEmd-r6rSiP8IDgj_CE7nJrTzRP05g-hj8uySI4WG94pITAl38cwCfhKFen1Dmp7oD-Z4A3azYPglrtr0OW8_OwzmnZ7xrILgRtYtZ9ORmeP0gIwNwKfVlU-gdoXP_6xXlNSQF4Q25adLsYDv-F300lii7Zi5q2Ul48ppM0CZnaUw2I7HgrOUSTDWPrXrhMXt1OECWhedmTEV74ddemrnaMK77uJiZhzuFs_OjyWE8cNPRaMn2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح‌هایی که در دومین روز هفتۀ دولت افتتاح شد
@Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/458232" target="_blank">📅 21:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458231">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIfTY8zEsC-g9xSPXRy78oH1ntZkzdOLDkUnhimnXc5pbldZhhifi2JxFa_yflb-4OopEzo7v3dvihUEgI7pRKXfSG2eWy3QVtzjgEdPfdxW9SCRUjfOsHU9DlxpFiQ7gjOtdcRpgU0oz0nWT5IxPeeaRUVgVdUtqerZ_d4KHXpPlcWJiUF8oGfncxH1AYP2DC4gQGj6PbPMwzkFZ5NwWIdJlOIK3w8Ce-oTeo_vIaB5jJ97onTYfdW-Eke_hd1wnAWDgENS2D2dpRpaFfupnt8UcNoy32Mg2pJCCl_nueZ8eEGAFNO7Ho8QCEA2mR6YHw9k8QkggZltc5RV5kYCqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف به جعل خبر ۱۶ ساله علیه ایران!
🔹
خبرنگار سابق گاردین در پیامی با افشاگری دربارهٔ انتشار اخبار جعلی در این روزنامه اعلام کرد مطلبی که ۱۶ سال پیش دربارهٔ حکم سنگسار یک زن ایرانی منتشر کرده بود کاملا جعلی و ساختگی بوده است.
🔹
روزنامهٔ گاردين در سال ۲۰۱۰ مدعی مصاحبهٔ اختصاصی با سکينه محمدی آشتیانی شد و اعلام کرد این زن به سنگسار محکوم شده است. مصاحبه ای بحث برانگیز که در رسانه‌های خارجی بازنشر شد.
🔹
حالا ۱۶ سال پس از انتشار، سعید کمالی دهقان نویسندهٔ این مقاله بابت انتشار مصاحبهٔ دروغین با یک زن ایرانی از مخاطبان عذرخواهی کرد و نوشت : آن مصاحبه هرگز انجام نشد؛ من تمام آن مطلب را از خودم درآوردم. داستانی ساختگی و کاملاً کذب بود و من مسئولیت آن را می‌پذیرم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/458231" target="_blank">📅 21:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458230">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1mSh5CCnFSIhYSpPTnvuIWixNf1FTOG5C2l0ve9vESUbmhJEv64ldWc7bi3W1GT8cNQ2gxY-V-IPNyyfAtcSjJWMQl3bzswyGT7IQ4mmwXjO-UF2UUaTPrFC5RwdYJR9T_UkVYVKvsLNoXaAVOEve9bR0R2w9tZXpQe7Pf8PY_dXIxwpw-XT_xlNDci41ihM15l3tfQLY7y67j65UZBr2jUdc3yOF5f08somFyCVKGuGCbESWl5c8cwuIIC_svDPk_tV9NZbPBqaUbq-Nc11t4HHj3vkuGc76cdqymu0YmpX1oFKuptPv3ehcVoupzRVsMbXPLePKdvM2iYpnttTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«قسد» رسماً منحل و فرمانده آن مشاور الجولانی می‌شود
🔹
روزنامه القدس العربی گزارش داد که طبق توافق انحلال شبه نظامیان کُرد سوریه(قسد) رسما اعلام و مظلوم عبدی فرمانده این گروه به عنوان مشاور الجولانی تعیین خواهد شد.
🔸
فرمانده قسد دو روز پیش
گفته بود که این گروه تاسیسات نفتی تحت کنترل خود از جمله رمیلان، السویدیه و سایر مناطق را رسماً به دولت شورشیان سوری تحویل داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/458230" target="_blank">📅 21:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458229">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9LFSKb04Tla1arvLCfyeodKQ6no9bbeFKbQ0oblLFL_ha5bNffXc6swq1MfQhwJVWodlnzjcuzZwUycp6hhQ9gS_y3NNkcQ_Fk-jSffJCy4DVAxEYecThRwbC-STwgWZ01LjuMencusW83qD4DXcIeUsUJQxI-1IleApakRN6fmbbpdm5me1WUp9gg02rYzWoBVgAp71N5clYtR4XYDSCtC7s9mLcgPIoCK_BVBEATb8irR8QpDLucq1zfzmOxSueQQPo-xhsNFRyvAWgRTicb8vfr7I_GHfUZNKYCAPNqtgjyqrlW3_oRpWJdouL0qPHgw0phPP_Hsm6HoDontMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوک به پرسپولیس در آستانۀ دربی
⚽️
اورونوف در دیدار تدارکاتی امروز پرسپولیس مقابل امیدهای این باشگاه بار دیگر دچار مصدومیت شد.
⚽️
هنوز میزان مصدومیت و مدت زمان دوری این بازیکن از میادین مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/458229" target="_blank">📅 21:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458228">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ae424a74.mp4?token=C-JWvLW2RiM5yiaRJm8adbfjQb-n9m8otAEw4McmFnWBcIYdULTtZxfpJyV_GGr_Z7LkOXdEnxacp3zW_jeWY5uc8WFQUjgYK23Epwyub934d4c6HmWd9uF2TBYHx2ymWEkdTktSylqdGKIK-dIvony2nBJOXaTDYp0UhNze491WuIyg9oUbYXVucCT2t1xuUfbiDvkDr82HqG8XEkaDqg8EHCiC8dqeXA1ZVpQoW8I9kgmcwaPtF33UaVDYswUE8w0YAfG1cH8niFBC1gd-SONfvUcGkU--vGEZWecVRYxha7SwBSXPGuY0Be2Yf6EXgS0NxQ3ecoN8lCOuzqjPZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ae424a74.mp4?token=C-JWvLW2RiM5yiaRJm8adbfjQb-n9m8otAEw4McmFnWBcIYdULTtZxfpJyV_GGr_Z7LkOXdEnxacp3zW_jeWY5uc8WFQUjgYK23Epwyub934d4c6HmWd9uF2TBYHx2ymWEkdTktSylqdGKIK-dIvony2nBJOXaTDYp0UhNze491WuIyg9oUbYXVucCT2t1xuUfbiDvkDr82HqG8XEkaDqg8EHCiC8dqeXA1ZVpQoW8I9kgmcwaPtF33UaVDYswUE8w0YAfG1cH8niFBC1gd-SONfvUcGkU--vGEZWecVRYxha7SwBSXPGuY0Be2Yf6EXgS0NxQ3ecoN8lCOuzqjPZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت ملی گاز: افراد سودجو با استفاده از انشعابات غیرمجاز، گاز را سرقت و از مولدهای اضطراری گازسوز برای تأمین برق دستگاه‌های استخراج رمزارز استفاده می‌کنند.
🔸
مردم در صورت مشاهده این موارد با شمارهٔ ۱۹۴ تماس بگیرند.
@Farsna</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/458228" target="_blank">📅 21:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458227">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwVexBQshduaXa9ORuQgTl6C2XLCpplHstW9_YLMMXHUU3q2aJAH8TFAXczCjaWkx8_fQk9xgmcc1qEDoz6lh-HaR3iuXAMgqmGU11AnJZuFEKYAG_WB4MTAsj8uGB992631ZO4l1N0CfAlmOul1Nbip9qdPxHgSYzsubgQ5YW30sbCEyif8X3omL0-0Q0kEIOZZyHUWai_RKG8y9PvWAHXEgu2CVAxFDcVM8tdtMZBYV2b6-hgXMmmwHUWEwPNJX-7GAhDYf2viUlx5QXCUyXPBjg1uemye4EbL7fY4npUBFPnb7PtIbrrpTq1p__6lRZFLDvMOU3eZWeB4uLeKeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان از آمریکا درخواست وام کرد
🔹
پاکستان رسماً از وزارت خزانه‌داری آمریکا درخواست تسهیلات تثبیت ارزی به ارزش ۱۰ میلیارد دلار کرده که بزرگترین درخواست در تاریخ این کشور به شمار می‌آید.
🔹
این درخواست پس از نقش پاکستان در میانجیگری در مناقشه آمریکا و ایران، که روابط با دولت ترامپ را تقویت کرده است، مطرح می‌شود.
🔹
پاکستان در حال حاضر تقریباً ۱۲.۳ میلیارد دلار بدهی دوجانبه کوتاه‌مدت دارد که نیاز به بازپرداخت مداوم به عربستان، چین و کویت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/458227" target="_blank">📅 21:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458226">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djT681t2rwc9P1__i3q-3wnck39nFivGTCUAU-ymphANSr4YBQP8rLt45xVVcZtHBAngbTejjkc7LQ-PTOqrQ_VP6obG-HM3Jk4BwdBZJcAhm5FPy67opqpmY2KtUzLB4JBncb43Ejv0VIAJSHfNl307eO4AdhDOPJtVrWldwTeQIPIKhohshShcBb8OqA5LM9wP4sF6BWnmwzANCGMAJNnKakC0z5UlD2nZVPWbPlMT_4SzG63PVIPIybopbBkQMtbTfO4_3P31lfdvfaxxiw4beqwuJCUlgEE3PDAxWJl4HXj-yNkZLKnL4PfVrBxqwqwXjkvB1YxPieIyz8RuIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه‌نویی در تیم ملی ماندگار شد
⚽️
دبیرکل فدراسیون فوتبال: به جمع‌بندی رسیده‌ایم که آقای قلعه‌نویی تا پایان جام ملت‌ها سرمربی تیم ملی باشد.
⚽️
انتظار داریم او تیم ملی را در جام ملت‌ها قهرمان یا فینالیست کند.
@Faresna</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/458226" target="_blank">📅 21:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458225">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqtCHBSef1lKB1rDbSfl7CldOHFBRJ8dvHs0MtOw7XDD8rDzbzCY4LBn4aGCpoS3lOn4i96UCTUV1cdNWU2rxdvXYWGrLjbgW4_i5Gpjs2eHxKc1HsycBG1ilDWwjQmEinM-TgJ41inHK7qiUQJj_SNon-vtcGXCAjnl4ivyUhxk5c1AEcT9m9jtgKjXZFYvwNt7ngK8GfI-ETl1Ttu8v4zjmpDTQoCOFwCD5ISv0MRqvkZzFSaJ2-64Y1FOJJfPYHwtz7ujK0TqisvMq6h0rK8-uxrxCiIatTtP1ViSujJ0vDDW7DicDVj17AzalSCIjc0_HcZa0sES759Y2rck_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ماجرای استفاده از «شومیز» در یکی از مدارس تهران چه بود؟
🔹
انتشار خبر استفاده از «شومیز» به‌عنوان لباس فرم دانش‌آموزان یک مدرسه دخترانه در سعادت‌آباد از صبح امروز واکنش‌های گسترده در فضای مجازی به همراه داشته است.
🔹
پیگیری‌های خبرنگار آموزش‌وپرورش فارس نشان می‌دهد این ماجرا مربوط به مدرسهٔ ابتدایی دخترانه دولتی در منطقهٔ ۲ تهران است.
🔹
پارسا، مدیرکل آموزش‌وپرورش شهر تهران، تصاویر منتشرشده در فضای مجازی را غیرواقعی دانست و گفت این تصاویر ارتباطی با لباس فرم طراحی‌شده برای مدرسه ندارد.
🔹
تصاویر دریافتی فارس از آموزش‌وپرورش تهران نیز نشان می‌دهد لباس فرم طراحی‌شده برای دانش‌آموزان ۶ ساله کلاس اول در سال تحصیلی جدید از نظر اندازه تفاوتی با لباس فرم سال گذشته نداشته است. آموزش‌وپرورش تاکید دارد اندازه‌های ابلاغی در این لباس‌ها رعایت شده است.
🔹
یکی از اولیای دانش‌آموزان معتقد است اشتباه مدیر مدرسه برای استفاده لفظ «شومیز» به‌جای مانتو یا لباس فرم باعث ایجاد این جنجال شده است.
🔹
آموزش‌وپرورش تاکید کرده اول مهرماه بر لباس فرم این مدرسه نظارت دقیق خواهد کرد و مدیر مدرسه هم به‌دلیل سهل‌انگاری به هیئت رسیدگی به تخلفات اداری آموزش‌وپرورش معرفی شده است.
🔹
مدبرنژاد، مدیرکل انجمن اولیا و مربیان، نیز گفت یکی از سیاست‌های اصلی وزارت آموزش‌وپرورش برای سال تحصیلی ۱۴۰۶-۱۴۰۵ این است که لباس فرم مدارس تا ۳ سال تغییر نکند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/458225" target="_blank">📅 21:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458224">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df681d69b0.mp4?token=gQLNeaiq9EILL-bIs2vhBgCG2VxsccyIylwUrjqqiaY1jdwkRTFyN49dQ1JPKbrHhdF0JG9Bt-J2wgqxhk1fxM16QegBfRZtE6LZkOteYLHTxuSW21TUtqHNXkl4dHAz46B9HxRHDZHpcZtsYE62WRnH_7DP5sr6nLy9vBPAEBy04gliokH89YrBg5LIpTHNduLrQTNq3DVOnq8unwnAn0RXlY_MiDrimElgveq1LPJ0KYWGgRpkwf-pA_tHDJN7K5Pvl6CNx-AEGldLApp485HglY8AGC7o3lIg3-Wi-GFamjwwFt-Zb3ySDWzkquvN5aLs24i9EF5j-yPLZvf-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df681d69b0.mp4?token=gQLNeaiq9EILL-bIs2vhBgCG2VxsccyIylwUrjqqiaY1jdwkRTFyN49dQ1JPKbrHhdF0JG9Bt-J2wgqxhk1fxM16QegBfRZtE6LZkOteYLHTxuSW21TUtqHNXkl4dHAz46B9HxRHDZHpcZtsYE62WRnH_7DP5sr6nLy9vBPAEBy04gliokH89YrBg5LIpTHNduLrQTNq3DVOnq8unwnAn0RXlY_MiDrimElgveq1LPJ0KYWGgRpkwf-pA_tHDJN7K5Pvl6CNx-AEGldLApp485HglY8AGC7o3lIg3-Wi-GFamjwwFt-Zb3ySDWzkquvN5aLs24i9EF5j-yPLZvf-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افزایش عرضهٔ بانک مرکزی، نرخ ارز را کاهشی کرد
@Farsna</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/458224" target="_blank">📅 21:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458223">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f161b189f6.mp4?token=IMJSwujgAe3YvgpenBn_cBv-PiiGLhHHf9QQYiRzQM1UwLoVxfeuEHYm62_fq4ahMz-7JRAcQeK-YOrpJAI7-chi776UjCo--YyTBAg2buX4qbY9YLbopBoXMSTtzjk4EBTsgFBimv41o0e5OR5bG7NHSdNC8JjTC1Z10L1bxt4LDYK2hiMEkXd_MeiaItmgrQC8t1B9EmiH4YiPzgVeEQDQs-JsXWTqg71dYSm3TpMHy8EBRbspSDgT56K1Fd5EtM2r-C_B_TaRscm8kJzSAq11FQpqllaNRDjl8jNvwV8EisZR5Oc2Wzxzi-1SyN5S3HBMjpN_v6xbOcf6GuyCsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f161b189f6.mp4?token=IMJSwujgAe3YvgpenBn_cBv-PiiGLhHHf9QQYiRzQM1UwLoVxfeuEHYm62_fq4ahMz-7JRAcQeK-YOrpJAI7-chi776UjCo--YyTBAg2buX4qbY9YLbopBoXMSTtzjk4EBTsgFBimv41o0e5OR5bG7NHSdNC8JjTC1Z10L1bxt4LDYK2hiMEkXd_MeiaItmgrQC8t1B9EmiH4YiPzgVeEQDQs-JsXWTqg71dYSm3TpMHy8EBRbspSDgT56K1Fd5EtM2r-C_B_TaRscm8kJzSAq11FQpqllaNRDjl8jNvwV8EisZR5Oc2Wzxzi-1SyN5S3HBMjpN_v6xbOcf6GuyCsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: با راه‌اندازی ۲ پالایشگاه جدید تا پایان سال، تولید روزانه بنزین کشور ۱۲ میلیون لیتر افزایش می‌یابد.
@Farsna</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/458223" target="_blank">📅 21:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458222">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59db84866e.mp4?token=SNBn2VTblHhI43TUiLX4Iyeumhr7WDbD_bbiJtsMMd2jqdJjd0OYe5e5Y_sczjCo3f1Wb_vJj_2xdQ2USo5zMR9XwFEcuvk2H1qNfzxKPSKVbcGNX09PAM3J4BMn4ZtM0cisFeJaAlEak5KKKkPqa_E9ciPb4pyfkPPb64qcJ1HfAaQjwa39Ddr9NVuRkcNlVmEQn5PSsVy8TDjDq8Eq0Eu5RXHR05iblZfkKGIgpgU94qyjvHe8wQmONQMjEIvp0s6pNMHNQSyiUwkCKqob4IwfcXw59kDBqVYDafWPAKxbsghB-9ce8a53ehMBEHgwZ5jpzEvUfZZPa8K2DhCwTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59db84866e.mp4?token=SNBn2VTblHhI43TUiLX4Iyeumhr7WDbD_bbiJtsMMd2jqdJjd0OYe5e5Y_sczjCo3f1Wb_vJj_2xdQ2USo5zMR9XwFEcuvk2H1qNfzxKPSKVbcGNX09PAM3J4BMn4ZtM0cisFeJaAlEak5KKKkPqa_E9ciPb4pyfkPPb64qcJ1HfAaQjwa39Ddr9NVuRkcNlVmEQn5PSsVy8TDjDq8Eq0Eu5RXHR05iblZfkKGIgpgU94qyjvHe8wQmONQMjEIvp0s6pNMHNQSyiUwkCKqob4IwfcXw59kDBqVYDafWPAKxbsghB-9ce8a53ehMBEHgwZ5jpzEvUfZZPa8K2DhCwTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوک برقی وزیر نیرو به صنعت فولاد
🔹
رئیس انجمن تولیدکنندگان فولاد: قرار بود سهمیهٔ برق کارخانه‌های فولاد در این ماه به ۴۰ درصد برسد، اما ناگهانی به ما گفتند که سهمیه مانند ۲ ماه قبل فقط به اندازهٔ ۱۵ درصد تامین می‌شود.
🔹
تولیدکنندگان فولاد با اتکا به برنامهٔ…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/458222" target="_blank">📅 21:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458221">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78fe676b69.mp4?token=iuUT1nvnWsP2bz9fcYM2LZcy6WXJhinMkv5e5NjGHqNTqEOSNa66voZXWXZY5XuHsfRxe5vgTxTaOF4GFoV6HrVagnxX1AGXrJdBh0QLNG2QBk7iwFPjt_rCYG9CMe4BdmHk7uPVMP8oV0KcXK_gvyCoKyUHVXo4Oe1H73_wW3vIS6k4zWfxEoyjjT3_TG1_lJinQufNDco7CXBX9oIKG1NVjrV87ZXIY5jelg57g7Kwrmb0SySSAs0gZu2qvmqjncle_CZ4hVAutwI7qlehN-W8wAzccBZxwuse5ne7fmhiMqe9PwmnG_SecdV9GTgSBOpvjI4c7D_u5z1a7yRaNUMF6pbxwsiqnCfpWF3Numa_FOBJgUn68jx0GaufL1CoOcw58hzAR6hnLT47vYedDaU0NYiT_B2CpZPus2auzBBCSw5FX91xNGyZjguKBmmKWxOMsKIwPbHTNgsrexqvy2YF_2bIAKi0NoySLOo599MoCzmjfmMfI_-raARk3isupAaE9HpUzRZg-MhKQKlhfApWsyYSJ9CQAHIVfVNMUTrOx6ZKMPyFtm00gxuplpn5lyElvmRwU60dVTNPwR1WHT61_h_oisJoDezhnKjaTn1MvC2BdR14VHaM3NYZScQctElKInSOY-h6YRrn5wojSZTlOuLpHDeOipmiF46iFMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78fe676b69.mp4?token=iuUT1nvnWsP2bz9fcYM2LZcy6WXJhinMkv5e5NjGHqNTqEOSNa66voZXWXZY5XuHsfRxe5vgTxTaOF4GFoV6HrVagnxX1AGXrJdBh0QLNG2QBk7iwFPjt_rCYG9CMe4BdmHk7uPVMP8oV0KcXK_gvyCoKyUHVXo4Oe1H73_wW3vIS6k4zWfxEoyjjT3_TG1_lJinQufNDco7CXBX9oIKG1NVjrV87ZXIY5jelg57g7Kwrmb0SySSAs0gZu2qvmqjncle_CZ4hVAutwI7qlehN-W8wAzccBZxwuse5ne7fmhiMqe9PwmnG_SecdV9GTgSBOpvjI4c7D_u5z1a7yRaNUMF6pbxwsiqnCfpWF3Numa_FOBJgUn68jx0GaufL1CoOcw58hzAR6hnLT47vYedDaU0NYiT_B2CpZPus2auzBBCSw5FX91xNGyZjguKBmmKWxOMsKIwPbHTNgsrexqvy2YF_2bIAKi0NoySLOo599MoCzmjfmMfI_-raARk3isupAaE9HpUzRZg-MhKQKlhfApWsyYSJ9CQAHIVfVNMUTrOx6ZKMPyFtm00gxuplpn5lyElvmRwU60dVTNPwR1WHT61_h_oisJoDezhnKjaTn1MvC2BdR14VHaM3NYZScQctElKInSOY-h6YRrn5wojSZTlOuLpHDeOipmiF46iFMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افتخار ایران، مهمان ویژهٔ تجمعات شبانهٔ مردم شد
@Farsna</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/458221" target="_blank">📅 21:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458220">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b746a75b.mp4?token=o_xTMtEZ4iuNiTp4FNc4l6HLj2cLkpROLrhRe5CAIBnmVAEFfOfvpTEGr3IDCdbPcTYe-SbXz3dbZ_SJXkD59WN0P3-hXCwTEVh9bMvrLxwDMdqJTy8XsT2sCCnPNKM8LQ0hqa-fbT-d_y2tnsLBpz6AtmTxQivWlIXqOeb5s_k7Vok5ZxXqzinU1rkupywI-mxrDGEi3nTKMg6WdeyRcjedIB9tbuZe2uwAt1NaEEZZK4iIz_5LS2Od35-Ab-JwyEmemrYU6VUJCgeGCNoXtKiNLzmBNYhqWxQgPciyCTUYPEvFmxRLrv8hqWDkGiK84ISY04UAfv9eyPOjczd_nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b746a75b.mp4?token=o_xTMtEZ4iuNiTp4FNc4l6HLj2cLkpROLrhRe5CAIBnmVAEFfOfvpTEGr3IDCdbPcTYe-SbXz3dbZ_SJXkD59WN0P3-hXCwTEVh9bMvrLxwDMdqJTy8XsT2sCCnPNKM8LQ0hqa-fbT-d_y2tnsLBpz6AtmTxQivWlIXqOeb5s_k7Vok5ZxXqzinU1rkupywI-mxrDGEi3nTKMg6WdeyRcjedIB9tbuZe2uwAt1NaEEZZK4iIz_5LS2Od35-Ab-JwyEmemrYU6VUJCgeGCNoXtKiNLzmBNYhqWxQgPciyCTUYPEvFmxRLrv8hqWDkGiK84ISY04UAfv9eyPOjczd_nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن‌چه در دیدار نخبگان جوان با پزشکیان گذشت
@Farsna</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/458220" target="_blank">📅 21:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458219">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6-on3ilY-fpFxdg8jBfUe_efbgJq-Q6jfMQghEhhtnUsNZL5kHED4JQM2EMowq-_xWeCo3Y2aVj3Iqh2NjOtCl7leKdWDB6sjHH7Sz-frMyy3vqjq0PLMUGk2GarZfpE6iOzeMFvzC2soFjZBoUqWTcmnR3w9EnvhbnbR85GQlKWEBaAD-JodTKZ41hIFBvL0_YaNkyPg_r3HUazBCASsw3AsQeFR93vN1umL-mIsGZEE278i2SREzkXyvqP3o3ezBYRF_K_ZQEwyc6OQi1YaXqksqlg1Nk4lIeu32-gi4SihQ6uM3TiNUqXlA7MSfYj9lBn48FCYSfZA_OUOHkKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج یک هواپیما از باند فرودگاه مشهد
🔹
روابط عمومی فرودگاه مشهد: پرواز تهران به مشهد هواپیمایی سپهران هنگام فرود از باند خارج شد اما مسافران و خدمه در سلامت کامل هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/458219" target="_blank">📅 20:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458218">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70c5de9c08.mp4?token=eS8oZAc_bGGxceyqDovdiv5EVQE8KFkFgf6sG6VDdF3_OndjnJ6dUcGB2gkHZmfLiCM4DkCME0RbEIQ7BzYqmQg9JLCPidywIH9wYOa6zxro7F7TZ3vGPICMQbsYtdSHL_3E7wqHT_bpkprnY7aIWWjyZ3UuQ1s0oBwctfVrqeIbOb9zX_y-ywxIs35C0-QmySv1rnCAM3TlLMFxgDqDsTp7zG3uIH-TUQpSMcX_r6RHfhDSFrL5ESLJ6Qmbh-QtaM3RI6ww-7bYfzhgFFH6fojgWQWk96qhQ033hnoDz6mpYgn1_92tBGOMrXcb8vLOWg1UMQsddLhiL7Tb319tFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70c5de9c08.mp4?token=eS8oZAc_bGGxceyqDovdiv5EVQE8KFkFgf6sG6VDdF3_OndjnJ6dUcGB2gkHZmfLiCM4DkCME0RbEIQ7BzYqmQg9JLCPidywIH9wYOa6zxro7F7TZ3vGPICMQbsYtdSHL_3E7wqHT_bpkprnY7aIWWjyZ3UuQ1s0oBwctfVrqeIbOb9zX_y-ywxIs35C0-QmySv1rnCAM3TlLMFxgDqDsTp7zG3uIH-TUQpSMcX_r6RHfhDSFrL5ESLJ6Qmbh-QtaM3RI6ww-7bYfzhgFFH6fojgWQWk96qhQ033hnoDz6mpYgn1_92tBGOMrXcb8vLOWg1UMQsddLhiL7Tb319tFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جایگاه‌های سوخت درگیر موج شایعات
@Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/458218" target="_blank">📅 20:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458217">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71720c1c8.mp4?token=gNujAiOMGx44ocozRbBR4eccVOnkG8HFzW8XFas77xff04RwIejqjpHr9Iy0Ic_v9skXJ-ordajbmFlftM1f2jVPcPqlgM5NKZmubwCuoeA33y8LUldJoi6B7IJnsr_2JIcsVcD_eFtmV8QIAJhAwPR7jIVOaLQuserJxsNaaq_XLLnMiW5MNJAMUJBH5ccQ5hDR4zItY1kCT5ln7olEPqfJwVFf1OSCpRV2eSNEDrz0khQwaHZ90-q5CtmHpFdZuYhc-xtGMHjp9SW79XeHaW3h3sOVdxcck05-SVGs29EQGUOTFpPSHUDPSdMCKJPYg8No7_cniX31Nm6qYmk8Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71720c1c8.mp4?token=gNujAiOMGx44ocozRbBR4eccVOnkG8HFzW8XFas77xff04RwIejqjpHr9Iy0Ic_v9skXJ-ordajbmFlftM1f2jVPcPqlgM5NKZmubwCuoeA33y8LUldJoi6B7IJnsr_2JIcsVcD_eFtmV8QIAJhAwPR7jIVOaLQuserJxsNaaq_XLLnMiW5MNJAMUJBH5ccQ5hDR4zItY1kCT5ln7olEPqfJwVFf1OSCpRV2eSNEDrz0khQwaHZ90-q5CtmHpFdZuYhc-xtGMHjp9SW79XeHaW3h3sOVdxcck05-SVGs29EQGUOTFpPSHUDPSdMCKJPYg8No7_cniX31Nm6qYmk8Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهاد کشاورزی: صداقت پزشکیان و اعتماد مردم به او باعث شد این ۲ سال سخت را پشت سر بگذاریم  @Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/458217" target="_blank">📅 20:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458216">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl7c9r6qWHDqxhur3pcPxHUeR6l493qRCjZbKjyjoqtQkSV47st7L1kOyEDfuJrJiWGGHYbnJQ8nhAloYfwunM9ByNkk60tt1XEZ7dDt1GDBJgwj1Tu76eakxgL9SfFRLAVIp-QHgAoOyl3kMQdwm-afj1iSsnBukSmwTtVzlltoTA_GWaj7-Yyn-gWxoa7NDJobLkBoVrg-SEYGb8vCuBxd2Lnzrxc4eMLjeKP27GtQQ0MiH3hhw13Y9XZMpOjHZ4rDvoefPc84DzP3-TyTLd8nPqXvEas2OUke4ZFqehM6PVe-jfp5CxMU2N2IkBj2jzJEZPOFUeqHKddhOgDR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوک برقی وزیر نیرو به صنعت فولاد
🔹
رئیس انجمن تولیدکنندگان فولاد: قرار بود سهمیهٔ برق کارخانه‌های فولاد در این ماه به ۴۰ درصد برسد، اما ناگهانی به ما گفتند که سهمیه مانند ۲ ماه قبل فقط به اندازهٔ ۱۵ درصد تامین می‌شود.
🔹
تولیدکنندگان فولاد با اتکا به برنامهٔ اعلامی وزارت نیرو، برنامه‌های تولید، فروش و صادرات خود را تنظیم کرده‌اند اما اعلام ناگهانی تداوم سهمیهٔ قبلی برنامه تولید را بهم می‌ریزد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/458216" target="_blank">📅 20:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458215">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSaB1OajpYfgWuRE0qgv72ROlLZxF08HwqElYsYbzOg0kkaqILrgQLRNn3x6rVb0A0OIraRqoA7FZww8N44Ij9KBYDiN1cIJiCcpVmH9Y3zSt3Qj7w52rSZbPg0bRtfzFENZh0igf4ov07u1GDc8BARvEsESncwoA0K33yDsaYVMm9dI7mofWvi0fyOPS1bxXQX1VF57Y44fKhVZ1bknIEdJXCsniq7flFw0fkTNLWbvoOnelsW7xWAy5ghMB3aj1wYOQW2sJVEo3wojTKnnSVQ55Ou9tnDGAh03tmFpBZSGEvGTsiER-hnZlLvnQ_U5RxjKLll79ii5CXQnjyQjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی دولت: سهمیۀ بنزین با نرخ‌های ۱۵۰۰ و ۳۰۰۰ تومان بدون تغییر حفظ خواهد شد
🔹
تاکنون هیچ تصمیمی برای افزایش قیمت بنزین گرفته نشده است؛ هرگونه اصلاح ساختاری نیز با رویکردی تدریجی، شیب ملایم و بدون واردکردن تکانه به زندگی و معیشت مردم انجام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/458215" target="_blank">📅 20:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458214">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۲۶.pdf</div>
  <div class="tg-doc-extra">3 MB</div>
</div>
<a href="https://t.me/farsna/458214" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۵.pdf</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/458214" target="_blank">📅 20:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458213">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6kN_FCJjfQu7dbGDCD6QNZ6YJ7kmgfLwdHikk11okNOzi9sL4zLcktZ6AaFi6g4EAisRAGhDL0v7ukl_6J17w9gZ6v69VcVh7x_5dK3Q-lkpKcYbzNiaE3TTVX3P8OBtS5cD--ZagtFESYt5x3WGCGGUXsbrcAUR8e5atKOXnv9Q7c_g31PWktN2DXvKlh9gY0-7I4mhcUgpNF3qZbRgq6l0JE0ZQNEIfwJ-UHMY4Y9KCGrKcDeODTAECpn5e4PJWTJ8rUf0rzjv5xZqGjnig29ixgJs8_7xxKdSDkmgY1U_wtgXmfsZ26FixVGmVXkekHFzPPMT73swHcYmHje5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: آمریکا در جنگ نظامی و سیاسی شکست خورد و در اقدامات اقتصادی نیز شکست خواهد خورد
🔹
نقش ایران و عراق در ایجاد نظم منطقه‌ای تعیین کننده و شرایط برای ایران و عراق حساس و تاریخی است.
🔹
این که قرار است نیروهای ائتلاف آمریکایی از عراق خارج شوند، یک افتخار تاریخی برای دولت و ملت عراق است، امیدواریم این خروج به طور کامل از زمین و هوای عراق محقق شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/458213" target="_blank">📅 20:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458212">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgXG0deZfcRFYd4wDK_0yevaNH31nIK8KlyAlBdp-VGpsp-lBCGwuInCoCDYD6IoQrjV96eBcCkQ21Q_jdnbYXx7q248enVhl9MuG-iU4nx8m4TPngevJk6z6TOCyOsBLm8Uf78X8CWh3cqfcOiSnIv1Dj_eitdsoJdbJ693aGZET9WNPiSiOrtKX4U6Gouvp-kIj3u4QDd2G80BisknWL0rM6vHRBio9pdLZzy2nhxreJVzjgtDFJaM_1dwLI-QpJ6ZFEITgkB4bCVgw-mCIceyUxxFbHIKbwV8uQ-I4J0fpWJ366TzGdmUZ5wBDstzexSsyFtknF1XIJdDBONuDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت سرباز صهیونیست از قتل خبرنگاران در بیمارستان غزه
🔹
رژیم صهیونیستی سال ۲۰۲۵ در یک حملهٔ دو مرحله‌ای به بیمارستان ناصر در غزه ۵ روزنامه‌نگار از جمله حسام المصری، فیلمبردار رویترز را به قتل رساند.
🔹
مقام‌های اسرائیلی پس از حمله اعلام کردند هدف، یک دوربین متعلق به المصری در پشت‌بام بیمارستان بوده که حماس از آن برای زیر نظر گرفتن نیروهای اسرائیلی استفاده می‌کرد!
🔹
یک سرباز اسرائیلی که به دلیل ترس حاضر به افشای نامش نشده به آسوشیتدپرس گفته: ارتش اسرائیل هیچ مدرکی پیدا نکرده که نشان دهد دوربین المصری با حماس ارتباط داشته است.
🔗
ماجرای حمله اسرائیل به خبرنگاران حاضر در این بیمارستان را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/458212" target="_blank">📅 19:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458211">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نتایج اولیه‌ آزمون كارشناسی‌ارشد منتشر شد
🔹
متقاضیان می‌توانند برای مشاهدۀ نتایج اولیۀ آزمون به سایت
سازمان سنجش
مراجعه کنند.
🔹
مهلت انتخاب رشته از ۵ تا ۱۰ شهریورماه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/458211" target="_blank">📅 19:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458210">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed5e4ed0de.mp4?token=lDoHc-AGIf_5FleVEt5b0hJJemNJ_IuqeAw-D0dZiu9lufTNDMn8etOEH70ZQN6ZDkSUJhUNdroIveJI_1RGzvEDdN6dQ263thNv8O--Duz9BqQe1EzwDEyMgwGD4fHQkMk3-TG1fIuzZ9C8rYuv-AvAcqey8RVT8pT0vEhi95BUnO-LGjFWAwNEjNWkFEZKpOTWZ0Bm6N__MaFSGrYwZseqHrU0BTt8a4tjgnqKtjsUCAt72wc-1hlQJhnacNAk7_OI_6sg-ei36OBLwmko0AfeZw_tPKhaVbDbpcmZ-g80rjfUrMGEuuOdE_vD3C10kzqfPgIjXajVugQQaYYP5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed5e4ed0de.mp4?token=lDoHc-AGIf_5FleVEt5b0hJJemNJ_IuqeAw-D0dZiu9lufTNDMn8etOEH70ZQN6ZDkSUJhUNdroIveJI_1RGzvEDdN6dQ263thNv8O--Duz9BqQe1EzwDEyMgwGD4fHQkMk3-TG1fIuzZ9C8rYuv-AvAcqey8RVT8pT0vEhi95BUnO-LGjFWAwNEjNWkFEZKpOTWZ0Bm6N__MaFSGrYwZseqHrU0BTt8a4tjgnqKtjsUCAt72wc-1hlQJhnacNAk7_OI_6sg-ei36OBLwmko0AfeZw_tPKhaVbDbpcmZ-g80rjfUrMGEuuOdE_vD3C10kzqfPgIjXajVugQQaYYP5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهاد کشاورزی: از ماه اول دولت، افزایش ذخایر کالاهای اساسی را دنبال کردیم که باعث تاب‌آوری در جنگ شد  @Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/458210" target="_blank">📅 19:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458209">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6edef8b8.mp4?token=rCKVB7Ko_INjmp75kxbsKeO4I6yaZNagySTSpHlz1ymwhhsj04Kv1lJlzGUM2KTnV1XQWwxE84f34JOpvkqW_NOGny1e5oQVjcoa90j0t8F4GF8u08DlWiw5XW7P6FSlhHy2qLEG3tvqR07UDUHBGQwZtVzsBKqYh8fJ8RI4ozAvX8x4_A3dKna1SY1LfHGasnBwpSevZNH4s7dRfP50OopH-HDwPp4QFLQ9E61c7JqlGL1XEKnppQlWtG44CtE6I30MTFzPfjOUsqeobHO9ouMHVV84FK5MpN1LxGahA8FnofBenX07Pg1KaINmEjOXgHA1QPDUwvNlbQOyl7J6Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6edef8b8.mp4?token=rCKVB7Ko_INjmp75kxbsKeO4I6yaZNagySTSpHlz1ymwhhsj04Kv1lJlzGUM2KTnV1XQWwxE84f34JOpvkqW_NOGny1e5oQVjcoa90j0t8F4GF8u08DlWiw5XW7P6FSlhHy2qLEG3tvqR07UDUHBGQwZtVzsBKqYh8fJ8RI4ozAvX8x4_A3dKna1SY1LfHGasnBwpSevZNH4s7dRfP50OopH-HDwPp4QFLQ9E61c7JqlGL1XEKnppQlWtG44CtE6I30MTFzPfjOUsqeobHO9ouMHVV84FK5MpN1LxGahA8FnofBenX07Pg1KaINmEjOXgHA1QPDUwvNlbQOyl7J6Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهاد کشاورزی: از ماه اول دولت، افزایش ذخایر کالاهای اساسی را دنبال کردیم که باعث تاب‌آوری در جنگ شد
@Farsna</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/458209" target="_blank">📅 19:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458208">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOkQfucgakv_tIAsMS_Qoel96wAPy5WDFox3CtEt9aCIdPQLu7tcFlyLRujOnZhIFSxPjbzBSBzexm8pERbZ2ygz_P3GmzQSM0eVtlY1EralIo6s3IdXKkgBk6y6BCnHCfMQl0ZKkpQnoWwiOMvmL6MZp0YlsVwqzTCZ4r32z0p_V6GHOLVXZYR4z8W0fpyqigqWhCk7tV4O9HZpP5voyZbp5kte1LKNF-UW2t2EXNIblKf8EO4CTMuuO8jxq2zTYKx5fTab1DRQD4cyMhbQTlbOSPBuO3AfJT4jQZ4Rns_HhbxbJzEZ9vYTc0VYfCXxqMP5rrBo5Y7xSVIUhnzKBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: جنگ اقتصادی آمریکا علیه ایران، حمله به حاکمیت ملی همۀ کشورهاست
🔹
وقتی قلدری اعلام می‌کند که همه بانک‌ها، بنگاه‌های اقتصادی، بندرها، فرودگاه‌ها و دولت‌ها باید بین اطاعت از هوس‌های واشنگتن یا مواجهه با انتقام آمریکا یکی را برگزینند، موضوع دیگر صرفا به ایران محدود نمی‌شود.
🔹
هیچ دولت شرافتمندی که برای حاکمیت و منافع ملی خود ارزش قائل باشد، عادی‌سازی چنین قانون‌شکنی کلان و قلدری نظام‌مندی را نخواهد پذیرفت.
🔹
البته کانادا از جمله کشورهایی است که کم‌کم دارد طعم واقعیت (قلدری آمریکا تحت لوای مذاکره) را می‌چشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/458208" target="_blank">📅 19:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458207">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8aveJ1Bx5_4HQNukmesQZh81NuEw7zBlo9-Y8Au2mImd8cwP63sbS1nW2KI-WpCPXKLev-vZb556Zm1ipvKHd9DfUi-O8mQq-6du7mLPczF3Q17hnANhZ-TyDH5qbHIwg4C-rejTNkqgs5Eru81447JvkIc2paHtIdIggUrrsKUFGShgjniQkcy7HQnM_GvrjD-6tGNwKkKCZlW3BecKLds6rkadGLehIvVNG3y8wyUr8buE3B4CwcFxCFd6ugvtP3pGy84eY3mv002I6bmf7kWcsyJ8bAVTYhIDTHRXiKeGNznk7laG0GqYTiMM8VxK1w5o7mNFW3lnUhhqsbwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکۀ آمریکایی: مجروحان ارتش آمریکا در جنگ با ایران به ۶۵۳ نفر رسید؛ ۱۷۰ نظامی هم ضربۀ مغزی شدند
🔹
ای‌بی‌سی نیوز دربارۀ تلفات نظامیان آمریکایی در جنگ ایران گزارش داد  شمار مجروحان ارتش آمریکا به ۶۵۳ نفر رسیده که از این میان، حداقل ۶۴ نفر از افسران ارشد بوده‌اند.…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/458207" target="_blank">📅 19:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458204">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7KxwVO_AExUSXCMikcWCB4ziWZL7SRsuscMDfG6VvixgJn0DgELcOH5C5eE-4PwH2on552bd_Xvl9Q0ARm3Fjyy1ueowwifC-O_C_EuKsKx1AZm51rSCU3nmZjP71UKH1TKVvy2AREEJMpDJZU1VsovUcD7X-rT7QDT6Tcv8Pzi8mZsU4Zo8t2Lo0e7mb210Z_lwBqwrvcDvZ0hb1Cgw3FGVpGKLl4tca09gk_gm4ebDMNJglrrDrucvk4GEyN_jYwyC5yt0Kfqb7K_LpxV6m2PdYiKG8ZrB4duHqV6QwrK_q7wdy0LmfQgVveqmngFEvFZ3AdkJOtkLY2bSi3zfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyX1I_KoYD_5Vp9o1YgvCZfeRiF9nrQ5_nIM4PXeiewewuzFzlT15w-pKTgK39To8Tgakxw7prO0L3MlnYGMUkfwjRfL-Qny8H36_Ls3QwxdP3M4OribvZohxT_vV_dWwZ8SB4Y5HeAazMrmeDQfM4VJi_Lgu1rmE2wl2egZ_A5qHnluNqhv6mR0q-dC2UfsQV4iuxvb0tcIJR8n6e-sJcYRHJnyo3IGAvBUlpmIzoFRPgIEexjZxdvGJ1Ihwmk3OZglThaDiJg5R-dDd81QUbecEXJLs2tHegn-eL_mC8yqaIphwzxhAV-0_LqJmjBbmXIAeEkxYvGbMHKD78P-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S79IZ0C5lmvfGjNllEJF4CLtLLm_o4EiZ35XeO0MildcXy3mI85RjhZCjjOZzVF5YWRRcBARshSRT66-SsHqCBiqu6W2GVH-UTl_0UTgV6yR2S_od5NQfIKDnRjkZsb3u0rRmy0-tSeR2CykH8l9uIQnrRfJKvm2EWTDhf0fydvsBU0HDRCvhAiJKk4nrA40qSrqjFjpYK43RHXMsaqovqwjxZqHluZDTf0ori4lwsdx7CznYDrvI5V3tmFoOh1mUP35EDyMAo46zaLFgad9auwyujybKpjIPWw8TZTX0CB-se__lPcuILEDQqXlTxRNY-jmOUMaJv65zEGIv-zkDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: آمریکا در آیندۀ منطقه جایگاهی نخواهد داشت
🔹
دبیر شورای‌عالی امنیت ملی در دیدار رئیس شورای‌عالی قضایی عراق: ایران خواهان عراقی مستقل و قوی است.
🔹
کشورهای منطقه خود دربارۀ آیندۀ خودشان تصمیم‌گیری خواهند کرد و آمریکا در آینده منطقه جایگاهی نخواهد…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/458204" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458203">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda1ad0212.mp4?token=PljW-WiQ8X9I2RkVL46FABkrllxo0YTztsYD1ygIYiU0aWfjMv7nZy6SbYr9eF46oxY9K3gqSrC3l-xMx3modHcLvZ2sh_sRdHXyOYJ33Jv9FvHNFxKTaDDsj8q2v5VIoJDbNhrQL_muHze41MOv6rN0W5ytOgA964xhs3nvAIJKSb3LKjnJcaM8R4KML1TOtd9HSjv1LP2iyYPa83e3jaJqL6FZlet8yE1id0jV6athu4INwn7eEB8aO1QaaDsii5eQk0EPtyz6XWuIK-zJ3jpWLqSwSxNBbIYrRsG8sDV_qhl1PwecvZTtZMeA30Wf8KGe71lZAuxxwvVYwalD6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda1ad0212.mp4?token=PljW-WiQ8X9I2RkVL46FABkrllxo0YTztsYD1ygIYiU0aWfjMv7nZy6SbYr9eF46oxY9K3gqSrC3l-xMx3modHcLvZ2sh_sRdHXyOYJ33Jv9FvHNFxKTaDDsj8q2v5VIoJDbNhrQL_muHze41MOv6rN0W5ytOgA964xhs3nvAIJKSb3LKjnJcaM8R4KML1TOtd9HSjv1LP2iyYPa83e3jaJqL6FZlet8yE1id0jV6athu4INwn7eEB8aO1QaaDsii5eQk0EPtyz6XWuIK-zJ3jpWLqSwSxNBbIYrRsG8sDV_qhl1PwecvZTtZMeA30Wf8KGe71lZAuxxwvVYwalD6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای تولید ۱۰۰۰ سامانهٔ دفاعی ایرانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/458203" target="_blank">📅 19:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458202">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXprYoLOyKbIy6BExuy_z6MEl3U_ZAtlCOPCwy8w1VB__13UQdKCAA_zVebPXSs0MQ8dA-H3G-2tGQEATr-cJkbj08MWUN2vUA1cAgA0Aw4ngMgnLSI6_6qTcvt7IVpeupEBx7TfmuTSopC1hIgPXXFYKwTIRYNBBEtbXPC9U6Mo8P5-tY1n-39nI9rkGlCtiB8KdJk5HMznKdRbmN8T09h6aUuFsYJgAEG6mFFV4PMyJFOvnrrYmXaSe9pmaP36CIcurq3-5vBj8eyJJhInaet5BFdhHtoP605jZRCSplDxoR7G63kFuyXlRy6EnFvY8f7L6AgYYdHC5Y5mhsjrOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهام پیمانکار پنتاگون در سبد ترامپ
🔹
ترامپ درست ۲ هفته پس از ورود تاریخی و جنجالی اسپیس‌ایکس به بازار بورس، بخشی از سهام این شرکت را خریده است.
🔹
در نگاه اول، این کار شبیه یک سرمایه‌گذاری معمولی در بازار سهام به نظر می‌رسد؛ اما حقیقت بسیار پیچیده‌تر است.
🔹
اسپیس‌ایکس یک فروشگاه اینترنتی یا شرکت تولید موبایل نیست که سودش فقط به رضایت مشتریان وابسته باشد.
🔹
این شرکت یکی از شریان‌های اصلی جنگی و بازویی کمکی برای کشتار توسط آمریکا در گوشه و کنار دنیا است.
🔹
از پرتاب ماهواره‌های جاسوسی برای پنتاگون گرفته تا ارائهٔ اینترنت ماهواره‌ای در مناطقی که وزارت جنگ می‌خواهد، همگی به اسپیس‌ایکس سپرده شده‌اند.
🔹
مسئله این است که رئیس‌جمهور آمریکا از یک سو در این شرکت منفعت مالی دارد و از سوی دیگر، دولت او درباره قراردادها، مجوزها و مقرراتی تصمیم می‌گیرد که می‌تواند بر آینده همان شرکت اثر بگذارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/458202" target="_blank">📅 19:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458201">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLhcuPb2buaap7AwwnpOYDoFfFLZyKPW4f7SDzyc6xZ7VF8TB7PlzKxaUbLTX5VedkcyqrU93sAGAf0flllcg61Q_CZ6HUkUW9VwIcTTN5qi3EEkNszTQEIBLkAr3aIYB3JOUcINqFhdK5E74FqE67cVGzKsx51edLGtOqoVL3av83yakTnuAMRASbCCIS72pdABX1szZEn14W3cmHqXyNIMDHnvei8TdkIRMmneJNr2c3gswF7wKkcMBpG3piPXesxDywPNzXskXxR0wLzj7Shw1w2jKd8G_FyGGmH-v3TnVY6E9uLUta1edb90tLtIyvIUgXnwJ9wTBp-jUfhAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلارهای گردشگران سلامت ایران در جیب دلال‌ها
🔹
ایران سالانه حدود یک میلیون گردشگر درمانی جذب می‌کند؛ بازاری که با وجود پزشکان متخصص، مراکز درمانی مجهز و هزینه پایین‌تر خدمات، هنوز با ظرفیت واقعی خود فاصله دارد.
🔹
رئیس انجمن دفاتر خدمات مسافرت هوایی و جهانگردی ایران معتقد است دخالت برخی واسطه‌ها و شکل‌گیری بازار دلالی، یکی از مشکلات جدی گردشگری سلامت است؛ به‌طوری‌که بیماران خارجی به‌جای ورود از یک مسیر شفاف، گاهی با واسطه‌های متعدد مواجه می‌شوند.
🔹
کارشناسان معتقدند گردشگر باید بداند از لحظۀ ورود تا پایان فرآیند درمان با چه مجموعه‌ای طرف است. قیمت‌ها باید روشن باشد. نقش شرکت‌های تسهیل‌گر باید مشخص باشد و مسیر فعالیت آن‌ها نیز قابل نظارت باشد.
🔹
گردشگری سلامت می‌تواند برای ایران تنها به معنای ورود بیمار نباشد. هر گردشگر درمانی برای اقامت، حمل‌ونقل، غذا و گاهی سفر به شهرهای دیگر نیز هزینه می‌کند. به همین دلیل، رونق این بخش می‌تواند درآمدی فراتر از هزینه مستقیم درمان ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/458201" target="_blank">📅 19:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458200">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTSt0tH1HYzilQ_NJIN2jG4Kjl0bYuH5o6m1xYndc11N6eYOfjhIIiDqEvSdhkIQNw3_OLm_xEg4apDHVhYf4pOHE_-5j1q6qZlmctxtrAs37lMyzsC4q77VEZYKAz6cphaJduV1O6Jpjw2xTMkmycIS5i8kOp9xiaYhmYs_qeL9BK5g33rBDUFcMOlyQs2rZxo8Tu72xp-6_aaCjnNTSyzTjQFlGCa-2TW276oA70Qpi7DmQ3Mr4mDXzG2Gg8xbZNKHJyr8aNex_ANmf-JKK6TMtVeGGh1TbfNdzUf2YgWinXlDsyIcrX3EdC1fJuQt0FZIQjKuPO_pwiXbZUPlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ایران و عمان: دربارۀ چهارچوب ادارۀ تنگه هرمز گفت‌وگو کردیم
🔹
رایزنی وزرای امورخارجۀ ۲ کشور بر ازسرگیری دریانوردی ایمن در تنگۀ هرمز با حفظ حاکمیت خود متمرکز بود.
🔹
چهارچوب پیشنهادی شامل این موارد بود:
🔹
ایجاد یک کریدور مشترک از طریق تنگۀ هرمز
🔹
اجرای پروژۀ مشترک برای مین‌زدایی از تنگه
@Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/458200" target="_blank">📅 19:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458199">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLgAxD9sYeyjaLFuIEWLUL1M_dlq2EE_KM5bc5GxxSXUe0Ids-4rB1w2dYFwr_pMmA5mfV8h8F1hDsyMKdWi2I_TvYld-b38ZnHRayB8KO4SXS2PCgQXy6Tltl2TsNlXZahlZbWzeA1-gtihJ1RKwKUo2AQgRwilDka-jRBNodOspacWhXMTdg28qlabxMocEkjIkA0WgooRQhn_x75KbE5nLBQfGgQzhvuLi3iC-0_GBXqs8whNgQ5GE628tsJPugX-r7IdY79z4TueoQvfWkx99uivrwAV7z6Doj7GZU42xyoMWsBrnhEVlKbi-CtR1oPbyGmOqGTrYW2QdkRJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: ما از طریق نیروی فضایی، تنگهٔ هرمز، کوه‌کلنگ و ۳ سایت هسته‌ای ایران را زیر نظر داریم.
@Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/458199" target="_blank">📅 18:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458198">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🎥
مسئول مسابقات لیگ برتر ایران: ورزشگاه نقش جهان بعد از ورزشگاه آزادی بهترین گزینه برای میزبانی از دربی است
🔹
نامه باشگاه سپاهان برای مخالفت با برگزاری دربی در اصفهان؟ من هیچ نامه ای ندیده‌ام. مشکل حضور بازیکنان لیگ برتری در تیم امید با تعامل حل خواهد شد.
🔹
محرومیت هواداران تراکتور و پرسپولیس چون رای نهایی‌اش صادر شده بود باید اجرا می‌شد. امیدوارم دیگر شاهد این نباشیم که بازی در لیگ برتر بدون هوادار برگزار شود.
@Sportfars</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/458198" target="_blank">📅 18:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458197">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7uOixXY3hJs7M8lZ1MoJM6i2hLjE6KILRkdaVJJmbiufGfxBJl4vljP0xwBbu5It_c0YOXTx-rAuz_P4tLftkjveYun3FK03pPVDTuFuZ0nvPVqGkGXbYPUADfFZnKRBrNAXTfwl3jodm9C6JXWb1QAHMbzphln38eINFxOR5cu_NjhzVqKj6k-suMqCeJ2s860hM8qacrLa8hNL1DT2cxFp3rAgB6-J4b_egWKxzXWABeCNLypmZxpUC-Pf4UIjhzKaty60xhAOuocCXe_3kIhfyh84FYemr_oSG9Jmp6-FdQDqtJEwKfrj3q5ikm46WGssyYnKXKKy57UgrhjrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم‌ترین موضوعات مطرح شده در جلسه  ۷ ساعته رئیس‌جمهور با رهبر معظم انقلاب
🔹
تأمین نیازهای معیشتی مردم
🔹
شرایط موجود جنگ تحمیلی سوم و آینده پیش‌رو
🔹
بررسی تحولات حوزه نظامی
🔹
تأمین منابع و مدیریت مصارف «ریالی، ارزی و انرژی»
🔹
تعامل اقتصادی با طرف‌های خارجی
🔹
وضعیت مسکن و اشتغال
🔹
بررسی نحوه ایستادگی کشور در برابر دشمن
🔹
مهم‌ترین توصیه رهبر معظم انقلاب حضرت آیت‌الله سیدمجتبی خامنه‌ای به رئیس‌جمهور
«حفظ وحدت و انسجام داخلی و پرهیز از اختلاف‌افکنی»
بود.
@Farsna</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/458197" target="_blank">📅 18:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458195">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXBqrdPEtgbEML7wHLDx5QAznpimO0jTdoYSc2NL3DRwfmpMlF085rMVy1jZD8ZQ9ZZv0pE-Mph1yAG09altSevsC8mHJlzNC9NJ3owNDYYxnfkDygWozJfThcnuhzH6Dj5oc32OqdATVwrpD-dQSrMy29zQjPujAaBW46uZF87JdBNpFMJEt0EJmrBTOm1Ml4Uy0KChlHuH8NnPeI5alwTG7Uq2YONvK9p8KzELRzzB04vlvm3bioaVTrngKGzdsEHKSzdFnBFheevZdqhMdT9KaKBp8Gjl0BeGh6JDRbmCDuMDMPuDr92KjE6IROOCQOabFS1wkBzbqNTPAoP92A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsykC9lRVkeSamvbKer2vWmmZH9pZOgfJkm3WPTWaCt2Yy3BB1B2DPp1b7bfHGE0CzNmKQZiCUa_FdJYvZf7bDa9UVQVjRzfzGW4lFaGKUJzdbAEvJzZ2-c3Uny7tfYniPjv0vmu4SOYsjnjhkvhaCtwXw_FpW51IpejtY3EyvgCq1u6T2T5zkMYaSQBfSS3rKqTeF-6DNdqLSB2V81X4q7n4-p2DXAeVm1AtIoIH6a6yXm1uwnOzmOUdzuNnrzdf5m0h22U5zOupb15rsvoXmcXKQn_ceXwJ77lwNtsr1BsaPYUvAFzr4_ZtoWjuS0IGFZ8DHWQGkKLlndJuqAYhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ، حریف بازار ارز تجاری نشد
🔹
طبق گفتهٔ رئیس کل بانک مرکزی در حال حاضر روزانه ۱۰۰ تا ۱۵۰ میلیون دلار ارز در مرکز مبادله تامین می‌شود.
🔹
بررسی آمارهای مردادماه سال گذشته نشان می‌دهد که این اعداد نه تنها در رنج ارقام سال گذشته، حتی بیشتر از آن است.
🔹
این در حالی است که امسال کشور هم درگیر جنگ و هم محاصره و محدودیت در تجارت از طریق بنادر جنوبی کشور بود.
🔹
رئیس بانک مرکزی می‌گوید تاکنون ۱۶ میلیارد دلار ارز تامین کرده‌ایم که ۹ میلیارد دلار آن مربوط به صنعت بوده است. این رقم مشابه میزان سال گذشته است.
🔹
ارز تامین شده در بازار ارز تجاری صرف واردات مواد اولیه تولید می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/458195" target="_blank">📅 18:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458194">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌  عارف: جایگاه نخست ایران در فناوری‌های پیشرفته در منطقه را مدیون رهبر شهید هستیم
🔹
کشوری با شرایط ایران در حوزه‌هایی مانند فناوری نانو، بسیار سریع‌تر از پیش‌بینی‌ها حرکت کرد؛ به‌گونه‌ای که از ابتدا قرار بود در جمع ۱۵ کشور برتر این حوزه قرار بگیریم اما ایران…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/458194" target="_blank">📅 18:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458193">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مسیر شمال به جنوب کندوان مسدود شد
🔹
رئیس پلیس راه مازندران با اشاره به انسداد مسیر شمال به جنوب مرزن‌آباد، گفت: حدود ساعت ۲۰ محدودیت یک‌طرفه کامل از مسیر جنوب به سمت شمال اجرا خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/458193" target="_blank">📅 18:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458192">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">عارف: پیش از جنگ برای اقتصاد کشور برنامه‌ریزی کرده بودیم
🔹
معاون اول رئیس‌جمهور با اشاره به آمادگی دولت برای شرایط جنگی گفت: برنامه اقتصاد جنگ در آذرماه ۱۴۰۳ به تصویب رسیده بود و دولت بلافاصله پس از آغاز جنگ از این برنامه استفاده کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/458192" target="_blank">📅 18:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458191">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elRSz4tZs2MGn7ddiS1T1wI0iKcKrFH0mQPOk9b0iwqM4CS7o4JikevwOqBlbmvezmf9Rku4sE54ZAGW-CKTlmao1B8UDt3IRMvFfRGNChXRVdp_9L5a_QED0JzSXD_JGzqlNvsLM55SFJ2dOgbRs9kWnRKTq8pUFNJzs2ZTzpv8QM0wngc60BT8SpWk9W_QWzcs_ieD5XsTd8BRgAy8hvDnKzpMQz24SCF34S-zDMX9z9a4sDD4Dnm7pkQdyH56D1CUi4XC2dyQUDSKoFnq5cKcwzxCrNlww_SvmJooLUjYbMfmXjFlIphR5k6T5JK1TPi9sIfvRBYn3mPbETLUCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: پیش از جنگ برای اقتصاد کشور برنامه‌ریزی کرده بودیم
🔹
معاون اول رئیس‌جمهور با اشاره به آمادگی دولت برای شرایط جنگی گفت: برنامه اقتصاد جنگ در آذرماه ۱۴۰۳ به تصویب رسیده بود و دولت بلافاصله پس از آغاز جنگ از این برنامه استفاده کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/458191" target="_blank">📅 18:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458190">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87fe6b2685.mp4?token=A3snor0GNKoIMpcXW25IpRqRlR_43g8AQcntRTGmptfEs_Fv0gDYeWKcG9pFHnWHpi8rhoGSu2gCky_fNxjERd4qWnP47uYfz1Y6zSyRpDYcb_58hfegcSJ90wq9r-OXxfTU_icU2qG2qBM8omZuutcsJfanJR8Wmt7VuSp6p6cwG4OZkLmgiJhhvF3nL77t7geuyJsAoINWJkIZYOBr86ho3S4RH2PN2_aDvqfqWBm542CPEeT0RE7dclcKZ-os7Ey_2zT8JkP60vhLdmyPMwKB9oT2y6ZiyRHUOTH9yHMT1red9TfRJilC6dW0ks5itHd2ZsYDWbBmmgqbVrmQTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87fe6b2685.mp4?token=A3snor0GNKoIMpcXW25IpRqRlR_43g8AQcntRTGmptfEs_Fv0gDYeWKcG9pFHnWHpi8rhoGSu2gCky_fNxjERd4qWnP47uYfz1Y6zSyRpDYcb_58hfegcSJ90wq9r-OXxfTU_icU2qG2qBM8omZuutcsJfanJR8Wmt7VuSp6p6cwG4OZkLmgiJhhvF3nL77t7geuyJsAoINWJkIZYOBr86ho3S4RH2PN2_aDvqfqWBm542CPEeT0RE7dclcKZ-os7Ey_2zT8JkP60vhLdmyPMwKB9oT2y6ZiyRHUOTH9yHMT1red9TfRJilC6dW0ks5itHd2ZsYDWbBmmgqbVrmQTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رد شدن موشک از بالای سر نیروهای برق‌رسان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/458190" target="_blank">📅 17:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458189">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پزشکیان: دشمنان روی نارضایتی‌های اقتصادی هدف‌گذاری کردند تا ایران را به آشوب بکشانند
🔹
دشمنان متوجه شده‌اند که از راه نظامی نمی‌توانند ملت ایران را تسیلم کنند یا شکست دهند، از همین رو بر روی ایجاد مسائل اجتماعی و نارضایتی‌های اقتصادی هدف‌گذاری کردند، تا از…</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/458189" target="_blank">📅 17:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lva9H8FMBJlDpvu9qC15k8zskqthZYBMd5T7YG4-UDhf3Tm0Pd-Ma_5OR65wM1-edLIoMo1mpdF6ToU1W1Zh64BHdAfamz8q7fo_LrWbg3Fo5biZ_sUPUPTZhrf9tVO4_8NIadpp9_sHkqlsXgtQy6k8I3f3acPnL0yWvFg8c7ymAMVTs1h1HxqeB7F9Kbakg8L5QET3nz7RwBZ3HMq7Fzx9eXsEqfVZK-3t39hvZuSAc49TJZyVcYbxyh0ZT85LdDP3d9hO2DcOy_ffGGDJeMRfnUrhcsstM9WH3ir-NBC6I-puvZODlZK-Mz6NEdOfpwBaWy1B7pqDex4da-xVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fEYWr9v2FU7GbSqPLPVjGZbVaDIQtO-J5FKZ3tTwER8fb3P4aoBzvRbfxp7uPApcVh-8OF9Luee3BFNrniT1-gNife-9dwVlBL5fjqZDUqSJQrg-FrAWeQ_sW5wG8NnaYmb_-bEig5mPBkdflr0dtkqgzNKD-oQ9N4pP_v6Z-EqeQrycZ05KjtX_wZMVJ9_Rlak8uuglXmF6QK7-Eda-70I-K0JFHK8NTQghpuUFJuYzRE3G53xvlnYIMuHkJpoAD49NGN8E3UP0qbJCIIhqWKjF2CaZoMkHOtOD4OkhOiDvC0qbCyvktYOJQbo71Gd8UERNq0_DCplzT1Vmh63OQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Grc0qDFXD75Csg91-dMdYwAOJTLMcadt-QiYINMKLSYSTG86-ntAZPiDVcmqC_6rr9bf7Zz_tCYRfWPPsVxs1z2AbXSOhzi_YWNkRtnl3eQbgrwsnYQDfHBOJEMhemhGcPkIR8nW5H9-0HGiPgUhtIxwaeZxF0Da5y2fbplaAgAarGlwlMIdNdKqyRstATUUS1ck63bqbl0LrQtcoTiaHkB5__-mUbFVqCATwD_ztfBuVxST3SR_jPw9p3kgOT34NLZXdOVv_UiZoPW8JRDxklMmCoiIlkyQc9pB5F_p0Qhfvusynt3FMo4rE8PEgQBSBn7xtMq7Km2Tehn1twS4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgQqNLkRevXiFnaKtEqtl2X2521w-FM1NnFmYzc4fDEu5L92Ys-D4fTiTLW8gUXTzl7ZF7_CDMI5LIHqdp5iyxZ-LAZjz7nzNiK4QfvvLv3uyehj01kuHxjTi8_h9s_1mB23RSFxK8BjYJW7C_qVu0OyNmQHet0JPQLwn0P6DMwFkOJ6UbWV-S-Qv5v6oHHrWPJ24owUyqpEaq8vA7-aDfr32VmnzKBIEXlEOyhO-Vi-6WfnZZiKTkba2Z96IIYVY4mn84-ziKsSnd4iDxl1AnP4xfqhLLCdH--2CmxDmi1BNl_M7DvQpwvM5J9KOMh7QH4_EQzR6W-TnTpOWLPBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3bGtz_bsPibc30AZrHO7B6UgGplbkKdIssS2hwrlbivDB1m9jwrumqJEuczN2PWEGHS-rdARGw-Df_aMOkmmmEWU5XvWdOOzht0e-fdtnd3ffFkgiQUZ3S3SuBNS_uf5pIF2q_nZmPKC7gLxBYwgcFxNPHt_W9QKo9zDvP0pdLlvPoFZe2ngZnjSbLw7Haq96MgVA2coM-4_HCH0S1wF6_F3fXfdd8W76O15XFYGpCVTW8HGswbJOaQ9Oam9GvmXYrAKwmxtB7JbGWPp3ZwBj6WCnhqLOSyXU_UCK6BbjBqN0hBMysZmfqhq47N7kGfdRL5-J0CFRnmoarQ9_s-aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور رئیس سازمان بسیج در دورۀ معرفتی تشکیلاتی «آرمان»
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/458184" target="_blank">📅 17:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrnaG0Dg4FcoV2WEjMQVcSTl2x-wIbef2GB9BtFXm9gOlOY9C_rcnuXUHDltuVQ4LQKZ_RzztBXsVAI3nv9ZRTt76u4xXCp44DQnk1l37IHML48qUsO9-CkwIVFEG0JCHOEw8A0iqT98VihFGWjbUPgVCPeobVkePz-XD-2FTOn5BrvT_8psWBdGLNdVVrNpUZTz1hWakCPB4emtWbPNZJAHMKFJfTR-uS1Ozji-YrjhjoE_VTNoTPZeQle3XZO7G5SGvm0qXNxGbEHfdHgPtZWFdEtBunTakE4nJcG7zGBi2H11qhiGROQY9SkGbKEG7TDHD1IkNZgb6zk1SPXQDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: دشمنان روی نارضایتی‌های اقتصادی هدف‌گذاری کردند تا ایران را به آشوب بکشانند
🔹
دشمنان متوجه شده‌اند که از راه نظامی نمی‌توانند ملت ایران را تسیلم کنند یا شکست دهند، از همین رو بر روی ایجاد مسائل اجتماعی و نارضایتی‌های اقتصادی هدف‌گذاری کردند، تا از این طریق ایران را به آشوب بکشانند.
🔹
ایجاد فشار اقتصادی یکی از راهبردهای آمریکا و دشمنان برای این است که تسلیم شویم، اما آیا باید در برابر مشکلات کوتاه بیاییم و تسلیم شویم؟ قطعاً خیر.
🔹
تمام تلاش من و مسئولان نظام این است که وحدت و انسجام را حفظ کنیم. هر یک از ما راه را پیدا خواهیم کرد و با مشارکت تمام آحاد جامعه، منطقه و کشورمان را آباد خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/458183" target="_blank">📅 17:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458182">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3077fb76f3.mp4?token=H1UYjsA2tz3CGI3HuV3PgrlgVT4zfT3Ua00WDnKiuv_BBrGEcAOiEEUGsgWhha6_3jQD3AlEhtSzV84X1B4sye-RhbRve2eOxWTGExq9RVxls9e9W-64jVBNp2TojSPAGyBgqs422TVlZdFstCAWaA3s7BbfBgLPIG9OUXV3sdH8RIaVhpo_TZORjObTZjwJAZKfsqryTEJ_4oLGMRg2Q49lHqC5ptmjXVbmJtQC4HuMJkT73QYeKx5DiGICy8fMnyqQmS0fCYxWzVbqsO3v0V1iYpS-0nH7dYV-70qLE0WJz8CO2xjd2Dk6osIqMs1wIvunEx9fAETzkiDsQ3o5MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3077fb76f3.mp4?token=H1UYjsA2tz3CGI3HuV3PgrlgVT4zfT3Ua00WDnKiuv_BBrGEcAOiEEUGsgWhha6_3jQD3AlEhtSzV84X1B4sye-RhbRve2eOxWTGExq9RVxls9e9W-64jVBNp2TojSPAGyBgqs422TVlZdFstCAWaA3s7BbfBgLPIG9OUXV3sdH8RIaVhpo_TZORjObTZjwJAZKfsqryTEJ_4oLGMRg2Q49lHqC5ptmjXVbmJtQC4HuMJkT73QYeKx5DiGICy8fMnyqQmS0fCYxWzVbqsO3v0V1iYpS-0nH7dYV-70qLE0WJz8CO2xjd2Dk6osIqMs1wIvunEx9fAETzkiDsQ3o5MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادامۀ حملات رژیم صهیونیستی به جنوب لبنان
🔹
توپخانۀ اشغالگران، ارتفاعات علی‌الطاهر را برای چندمین بار در روزهای اخیر گلوله‌باران کرد.
🔹
همچنین شهرک المنصوری، حومۀ شهرک‌های میفدون و صربین، و منطقۀ دوحه كفررمان نیز هدف حملات توپخانه‌ای اسرائیل قرار گرفت.  @Farsna…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/458182" target="_blank">📅 17:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458181">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ddeff49d8.mp4?token=uLat67h6oveR0c1bd54AHcuQipguGX1IvlR_3E_skUoRKOlvUV_EUWsiqZDxeqtTKv3NSVlRSeMyRVlC9ZPLt_MiL_efuuU4mSUub6VE-XydsFyAKhTrRv06anR7ImPzOEGiXSPJWbeouqC3CDSM-z4LVqztCzYt8V8o9K-GsfsUAxp_AYSOXYjB8lZD2BNmm-fsl6EdUsghYbOY4zlpxaMoN7Uz8YJi2iO7muvcPGRFTXH0MLEVSLAUxs6qkNxxKUqKhWLRtWWnEjNkjQUDdTCSNPLXeY--MYlkDtMHnCRu-lEWS5LOjqXGMOSWkmlm1cOD68RV1wmUsqzRf7LQmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ddeff49d8.mp4?token=uLat67h6oveR0c1bd54AHcuQipguGX1IvlR_3E_skUoRKOlvUV_EUWsiqZDxeqtTKv3NSVlRSeMyRVlC9ZPLt_MiL_efuuU4mSUub6VE-XydsFyAKhTrRv06anR7ImPzOEGiXSPJWbeouqC3CDSM-z4LVqztCzYt8V8o9K-GsfsUAxp_AYSOXYjB8lZD2BNmm-fsl6EdUsghYbOY4zlpxaMoN7Uz8YJi2iO7muvcPGRFTXH0MLEVSLAUxs6qkNxxKUqKhWLRtWWnEjNkjQUDdTCSNPLXeY--MYlkDtMHnCRu-lEWS5LOjqXGMOSWkmlm1cOD68RV1wmUsqzRf7LQmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«دی دِی» ترامپ «دی‌فیک» شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/458181" target="_blank">📅 17:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458180">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fnz8ZNb2-gEbiIREMrZrIQM7WW3DnSdDsViamgcmiaWjD76SX4aDHGC9DfjWbZqTWCw9jlG0Eq1Rm3SwUY0AfV5OBraG427iUulPGEO7KxRZqnPrhFL_IArizBRPRRZqr46WKwXmdu-3lXH1YBSspicWAi9eTaOsZFIiUVFfdeQNq-_yIwWH1WXFUA8Q9ZY-Io0FfM1IT0s8IHguBODHJtQzmyWSPgWJZ5yv9vb7tylyq9s9ogssKfsRgFoWmn9Ptmy2wtTmHbxeFIk_3Orn0a63PCyRJQAtDc5Yc9X4Ia-vqVfC8x_FMUnJi4MGulIJi1sDgSYpCOFBRxFO-FKBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار چین به آمریکا به‌خاطر تحریم ایران: تلافی می‌کنیم
🔹
نشریه انگلیسی فایننشال تایمز: چین به آمریکا هشدار داد که ممکن است به دلیل تحریم‌های ایران تلافی کند.
🔹
پکن به آمریکا هشدار داده  اگر واشنگتن سرکوب تجارت با تهران را گسترش دهد، تمام اقدامات لازم را انجام خواهد داد؛ همچنین اگر شرکت‌های چینی در هرگونه گسترش قابل‌توجه تحریم‌های ثانویه جدید ترامپ در رابطه با ایران گنجانده شوند، تلافی خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/458180" target="_blank">📅 17:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458179">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
رهبر انصارالله یمن: عربستان فرودگاه‌های ما را بر روی مردم‌مان بسته اما فضای مکه و مدینه را برروی صهیونیست‌ها باز کرده است. @Farsns</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/458179" target="_blank">📅 17:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458178">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌ رهبر انصارالله: از هیچ تلاشی برای پشتیبانی از مردم فلسطین و مبارزانش دریغ نمی‌کنیم تا وعدهٔ حتمی الهی برای نابودی رژیم صهیونیستی محقق شود
🔹
تأکید می‌کنیم که در کنار مردم مسلمان ایران هستیم و به تقویت اصل «همگرایی جبهه‌ها» و همکاری میان محور مقاومت ادامه…</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/458178" target="_blank">📅 17:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458177">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رهبر انصارالله یمن: تمام امت اسلامی در خطر است؛ چراکه صهیونیسم زیاده‌خواهی می‌کند و دنبال «تغییر خاورمیانه» و تشکیل «اسرائیل بزرگ» است
🔹
پیروزی بزرگ ایران نتیجه استقامت در برابر تجاوزات آمریکایی اسرائیلی است. @Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/458177" target="_blank">📅 16:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458176">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRUZzUjcnGCX6Vmxmdz_2nNev9mxLiS_rwViM7zuoOIZavGv2-Dbouj6RFYJSU-Mkc5efONVnlln3K1UIfPt4QsBS14HVxroPHIo3Hho2mv6S1pgcuWwcj01ETY-m2klEUB0DHnWOOxbOWXLOSEkd4O5eXp_OopDAKfY7S9BNOjZDZNX0hlWTPUsS4CFiby9-pLI4K0dJLzx4sd4oQuXQRjjpjFyRs9mPt66Klf99DAPGoU7smYXu-hONMcq40AncPznEjQKX0Ig5TqF2PtGS66IyXGNHaFpQrfIPyW3okC2RurpJ2a2hGEHdmCQna1qpAYEkL4AcbqqAQg5M87h2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انصارالله یمن: تمام امت اسلامی در خطر است؛ چراکه صهیونیسم زیاده‌خواهی می‌کند و دنبال «تغییر خاورمیانه» و تشکیل «اسرائیل بزرگ» است
🔹
پیروزی بزرگ ایران نتیجه استقامت در برابر تجاوزات آمریکایی اسرائیلی است.
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/458176" target="_blank">📅 16:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458175">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48cf1095b3.mp4?token=Q1NpNURJldKOjVS6TJ203c-xk7foRFuNfIpHCXm6UbyacuJlB6kltOjMwkxog485T92LGbNV8zPZ1jfz99R4CVOoMcvmsXJwl414z1Of0b8_Z8wGotzd1FU3p2PkcOVdGZ18uaD8A6EdfYlFf80nIYl2yWwJHHmmXqxfg3ZLX96l66gdQOsCfVT5WoSjyBZ5FoRc3KDAhVf81De4wolv3gYzEScNDuWM_jd68y9nTDJkexEDw3Pbn1osLhqPIpaP_KeO96eYZlZiC569ZqS23a9-VksAI2cl9260NlKqH-lza38vnPgRdOE9nY_860UGQJBs7fDLAfTDs1eJxcFCooi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48cf1095b3.mp4?token=Q1NpNURJldKOjVS6TJ203c-xk7foRFuNfIpHCXm6UbyacuJlB6kltOjMwkxog485T92LGbNV8zPZ1jfz99R4CVOoMcvmsXJwl414z1Of0b8_Z8wGotzd1FU3p2PkcOVdGZ18uaD8A6EdfYlFf80nIYl2yWwJHHmmXqxfg3ZLX96l66gdQOsCfVT5WoSjyBZ5FoRc3KDAhVf81De4wolv3gYzEScNDuWM_jd68y9nTDJkexEDw3Pbn1osLhqPIpaP_KeO96eYZlZiC569ZqS23a9-VksAI2cl9260NlKqH-lza38vnPgRdOE9nY_860UGQJBs7fDLAfTDs1eJxcFCooi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش عجیب رضاخان بعد از شنیدن خبر اشغال ایران توسط متفقین
🔹
روایت مهم و دست‌اول وزیر دارایی و  نمایندگان مجلس در دوره رضاخان راجع به یکی از حساس‌ترین دوره‌های تاریخ معاصر ایران
@Fars_plus</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/458175" target="_blank">📅 16:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458174">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/icu46_V5JG9h76HM3XYbpbetTmYDunTN6thPd8skz5KH--yeyzWcV-VWb2zndVjs2oKKIy6gL91zFZQ8XNC4pKwagfu5DLEStRF0Q7HZsq8viKlOLZDD_LYc-aGd1R51m47qGCpNVPA-P2kClZuZbtR81jNRODRpD1UPFMw4Y5bXANH6Egn2WnIlW0_180oFNa9ACWWrkSIE_sgYhB0vaG0kcIHgwdXk1RvvtFTnKPZDJQo3H36zdnp68K9w1j0UqeTbp5N6pd121KZHEF8iTG5vyAkVaS5AOg7mltxc5aNQLq5IPJHL2zwVauP8uuJXdQPdYbCDq9Mn5MDtrQ9Vsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چادرملو کرسی‌نشین ارشد بورس کالا
🔹
شرکت معدنی و صنعتی چادرملو در صدر جدول عرضه کنندگان شمش فولاد بورس کالا قرار گرفت.
🔹
به گزارش روابط‌عمومی چادرملو،  نتایج معاملات بورس کالا نشان می‌دهد کچاد باعرضه ۲۰ هزار تن شمش، بیشترین حجم عرضه شمش در معاملات ۲ شهریور را به خود اختصاص داده است.
🔹
در معاملات ۲ شهریور بورس کالا، میانگین موزون قیمت شمش به ۶۴ هزار و ۶۱۴ تومان به‌ازای هر کیلو رسید که نسبت به میانگین قیمت معاملاتی هفته گذشته، معادل ۳.۳ درصد افزایش داشته است.
🔹
میانگین قیمت معاملاتی شمش در هفته گذشته ۶۲ هزار و ۵۷۵ تومان به ثبت رسیده بود.
🔹
یادآور می‌شود؛ در معاملات روز گذشته در مجموع ۶۱ هزار و ۲۲۵ تن شمش در بورس کالا عرضه شد که با احتساب معاملات مچینگ، ۱۰۰ درصد عرضه مورد معامله قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/458174" target="_blank">📅 16:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458173">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyGkoAbmFrjhyPERMlzXNbRp-2asmR57y7O6FhuP6IcuX5L-ZFN-FGRnlfq88BGYfUkns-E1sbWrmvVJAlXURays9qAKEiHvjY-fORYUynbrnBhoDm_HElPmU8bm1mRi4UmFwOsOEoksMX8kehxtbwqooe5h99LcatrmlyLxtqs2zA967TrpsCDycoc0MIVAWI6GjE7DNELakbYMdu8jUAfkAR_IT4bcM6aEF-k_fdWc2br91wYBgwGpZFkGy-O8Hrtf_UeyYfWWjz8jjbxaypwL6dQ3w6RgxgXUAA4Vu5L1kL-bYSlSFchOdHDgkM3TZV71fJqsP8q1vd3-hv-wCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
یکشنبه‌ها در پارک آبی اُپارک، بازی‌های گروهی منتظر شماست!
در سانس بانوان، در کنار آب‌بازی و تفریحات اُپارک، در بازی‌های گروهی شرکت کنید، با دوستانتان رقابت کنید و شانس برنده شدن هدیه‌های ویژه را داشته باشید.
🎁
🏆
🎟
برای خرید بلیت به سایت اُپارک مراجعه کنید</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/458173" target="_blank">📅 16:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458172">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/458172" target="_blank">📅 16:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458171">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTv9eDuBbEWPfYO86b3Y95mbmaSrNn6yzyTQs3frMmmFsG0Bczc-BDU-0Nq2BrH8fND_7NPLKF8NRAvYcysBDSA-xyPp92HnAFEnjlhCeTUo-XKWTOtSVAZ-uhtMctJeFHHpm8HuAq0DtdPfp8Y0hyrkOeV0lkPZAIlmUAa8vI_MIPTjNcz9zU10fy2SK4vBo0jDXvwiorTtYuzYiTk5L1yz_JT4XS1XuDiukkBQJxeTModbkT9V4e6be9bAhtP3WthLr9kJ4brZpMt0eWD6KQgBBs6s0UkvdocNG03kOm5rG52Zdq-V55IS8qZPPMz7AoCcKhPl40q19xRuC1cS7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس مبارزه با مواد مخدر داراب به‌شهادت رسید
🔹
پلیس مبارزه با مواد مخدر داراب فارس: سرتیپ دوم حسین حکیمی در درگیری با قاچاقچیان مواد مخدر به‌شهادت رسید.
🔹
در این عملیات ۲ نفر از قاچاقچیان مجروح و یک نفر دستگیر شد؛ همچنین ۱۳۳ کیلوگرم تریاک و ۲ سلاح کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/458171" target="_blank">📅 16:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458170">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567b7b39b6.mp4?token=rmhNe-kfjebYrsVx5Qh4Vk7vJPX6a24G1GTSCxp89eiF4Zg47LwIhi5aZ16P4JADkrMzTyQ7oQqkssDNqPjA0Dc4o3Lbx3fSn4oVNlcYTy_b-ebv3KO3nX1J6-Xwd6JyfMzBqRIHcArsrAx_0wvyl4_DQvmovPGjizBXFtruHlkfj_Mjgop4X9z54Ln0Q4zqBtfisE3TRd9LHKEsS2yYq0s0M8ts_GovWbmvpothBCKfJvANGVhLdGpW6HkzqLDQ7NBgGdgUNE_J2TQQodQ5fJRnOvUSoJt_Tqu_DbzMBfgc5JIMmAJe5_V7rETb4M-MkK545EZPdcIeLdjVw2gj1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567b7b39b6.mp4?token=rmhNe-kfjebYrsVx5Qh4Vk7vJPX6a24G1GTSCxp89eiF4Zg47LwIhi5aZ16P4JADkrMzTyQ7oQqkssDNqPjA0Dc4o3Lbx3fSn4oVNlcYTy_b-ebv3KO3nX1J6-Xwd6JyfMzBqRIHcArsrAx_0wvyl4_DQvmovPGjizBXFtruHlkfj_Mjgop4X9z54Ln0Q4zqBtfisE3TRd9LHKEsS2yYq0s0M8ts_GovWbmvpothBCKfJvANGVhLdGpW6HkzqLDQ7NBgGdgUNE_J2TQQodQ5fJRnOvUSoJt_Tqu_DbzMBfgc5JIMmAJe5_V7rETb4M-MkK545EZPdcIeLdjVw2gj1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیلاری کلینتون: نتانیاهو فردی مخرب است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/458170" target="_blank">📅 16:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458169">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N97E8W4l0SQpMO_0r5G6GGcRmnagqs4OSZmWvGJfDpd1TQp_xfotHsk3oahYfjP5c7Ict5rFRJNNrYgoXyjLsnAHn80ztoyFxSBS9UZcbBq2yMHJMuB6AnimXB_Z_xoURQqUL7Fx_iXyIkgluGBRbV3paljt7gZctEiRbjZBrbUhCnqahhPpuLgOvUvjQcwVzJnO8-uoL9OziIMxSOe8AE6UAf3ZRAaEXTnsH7gbCs1_MzT_kTlqamBgwtwVKbwL_kJ_3XrWnqIkqR6bBIFtGB-4ClIYC07BWGvOmSkYWf8T0bJ4E8vMKXRW3yomGRE9vngfPt84K6tMyqMk0FlFKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سرلشکر رضایی: همۀ جهان فهمیده‌اند ترامپ خالی‌بند است  @Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/458169" target="_blank">📅 16:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458168">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c291b758c0.mp4?token=EuImh8aOhAn5OBZTulzPc291r69vQT6b3t8JwFuFv1chS5XFQbxEDceSp7gFHXfiFy0HSxn9thgXGxSuUYgqXQljWC_lursxEeRqul43Su526E5SogkXyR-QMDdmtUnf6UUA3kIXFx1M7n6LdqUEI_0cf0PpDv1P5J5G4KvXtDYN7HS0_13kCd7OLrdkW52iBMsDee2Y2flzfDY10YKBnktfvf_gtkngTRmYcfVhgHPkKjFtuMo7wElyMLiSow8TAgGxm1jb_fLmxJ-WMed2XorakehFa09ZA152CEIfQz8--j_O83Ot0yuFmlY_t6qwbNqhTTzXfh5_1Q081PjPnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c291b758c0.mp4?token=EuImh8aOhAn5OBZTulzPc291r69vQT6b3t8JwFuFv1chS5XFQbxEDceSp7gFHXfiFy0HSxn9thgXGxSuUYgqXQljWC_lursxEeRqul43Su526E5SogkXyR-QMDdmtUnf6UUA3kIXFx1M7n6LdqUEI_0cf0PpDv1P5J5G4KvXtDYN7HS0_13kCd7OLrdkW52iBMsDee2Y2flzfDY10YKBnktfvf_gtkngTRmYcfVhgHPkKjFtuMo7wElyMLiSow8TAgGxm1jb_fLmxJ-WMed2XorakehFa09ZA152CEIfQz8--j_O83Ot0yuFmlY_t6qwbNqhTTzXfh5_1Q081PjPnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کربی: آمریکا در کارزار اقتصادی علیه ایران ائتلاف تک‌نفره است
🔹
مقام پیشین کاخ سفید و پنتاگون با تردید درباره اثربخشی کارزار اقتصادی آمریکا علیه ایران، گفت تحریم‌ها در میانه جنگ معمولاً کارایی ندارند و اجرای چنین راهبردی بدون همراهی متحدان دشوار است.
🔹
«جان کربی» در گفت‌وگویی تلویزیونی با شبکه ام‌اس‌نَو درباره وضعیت تصمیم‌گیری در کاخ سفید ترامپ نیز هشدار داد که قرار گرفتن رئیس‌جمهور در یک «حباب اطلاعاتی» و محروم شدن از دیدگاه‌های متنوع، به توانایی او برای اتخاذ تصمیم‌های بهتر آسیب می‌زند.
🔗
شرح کامل این گفت‌وگو را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/458168" target="_blank">📅 16:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458167">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4OCkcbWOq7AKwvd3S2MjdgfsdeXRPlvNHCJSuxWxMmtnPtWILHGnSjaP1aPokXsILFg9Noh4z7Lovb89Dd54zKrZTeuEUo5xVowBDLwd55oZFLQO_ZW3EAgOrKwJ5xfxTlYIOaDvjiWAOCQ6dZqLonvrefi4X-t85_b-gcxnouwTI-1DT5PtrsSi3h2e6oNMBTFdcFfPshh9jWq_rSdBxGqMhTPpIO098ZkYQpZwya-QmfubTRNejJh0lXRE1-Jfs7rR-edfnVwSLOmuc5RlWZF0C7A8B-W-Ygt8Ao2sFcz308ZvE08yQ7MU2Fn_-3Bfp5FV1V1ZqED5X94_3vy1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس‌جمهور در حکمی خداداد غریب‌پور را به‌مدت ۵ سال به‌سِمت عضو و رئیس هیئت عامل صندوق توسعۀ ملی منصوب کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/458167" target="_blank">📅 15:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458166">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfJPiZslAw5mGuaGKxHJwbEGCNa91ZL0rcpYgcWK0lccJXZWIQ22K3oxIv1g5R5DRbTDoouEAgHActM6fsdepEq9Ma9ppBp5C3jo3GRkv0yJvlD6Sp0vh88mfBibd16LAyPYtEN5IioZlQiMCqXYdwufbOGKYvukrzF35GmmDABuYW5Y1KrA84UMeA4Sx2XXnUCn5yCOhe3k56vNK-ciskN6WaQB-NQch7-fS3GEKIJWrQQsak1zJ8OwM9F4k-KdTTvZVHMscgCIjuQYA-_XIh6AqC6zF7pQQnP1DFkUhsEtlAPx1xtk5i-2ZnjZukwyCBAchqK5WJtRAcz1rsL3gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری ۸۴ متهم پرونده‌های کلاهبرداری کنکور
🔹
پلیس فتا: ۸۴ نفر از متخلفان و کلاهبرداران مرتبط با کنکور دستگیر شدند؛ در جریان برگزاری کنکور نیز ۲ نفر که پس از تصویربرداری قصد انتشار سوالات در فضای مجازی را داشتند بازداشت شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/458166" target="_blank">📅 15:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458165">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌ تاریخ و محل شهرآورد مشخص شد
⚽️
دیدار رفت استقلال و پرسپولیس چهارشنبه ۱۱ شهریور از ساعت ۱۹:۳۰ در ورزشگاه نقش جهان برگزار خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/458165" target="_blank">📅 15:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458164">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عرضهٔ ۵۰۰ میلیون دلار اسکناس به شبکهٔ بانکی
🔹
بانک مرکزی در نخستین مرحلهٔ عرضهٔ اسکناس، ۵۰۰ میلیون دلار اسکناس در اختیار بانک‌های متقاضی قرار داد.
🔹
بانک مرکزی اعلام کرده که در صورت افزایش سفارش‌های ثبت‌شده از سوی شبکهٔ بانکی، آمادگی دارد حجم عرضهٔ اسکناس…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458164" target="_blank">📅 15:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458157">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLTN7tcx4zWdvppnrrI8KwF3CVnXwfHwe8SG--VfoSLMDOPklNcRmIDgxeyEH9tJ8dSHdTQoqz1a7voVT1lSdryLidSwRy-eLMq1HgsHNyOKuVHzQY0-xWBxDHGzGoIcTeDTsx_06qVxnYXoPOlD1AZYTl5n2MSRPOMQ50aCszpih_vFP4yo3nKhFd8kvFPqKNS-spV0FyXczrXrMf23lnAP6tjfAWXRcDk0xAyf7ANLb-us_yHhQ7tWDAerSzsRnb06Cb4xF7bE-WQrBKR2HjTFrzRZSTrXqPfaVohQ9DgK4VpIEUtQoQBJM7vwF9TzYGck-2q01lsWHNuXEXsZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5_KNYjuoRaSZMqblKvp40j7pTyurzQGzKbFPmNmrtkqRgO9ES4rUiREbKGbePnJSizroeGljJ22-dr7JIH6R47aSXYTILHuOHF0YfciYrsIL8aDbZyACbKSnFNVf7GjYhOXsP1F6zjhRVdrpLhN5ZTO68ib9xtWfN3DYh2Sql2d86MNX_9TPy8Kmq-laTF1okT1PHjOWS74zYOcThXB8pvfsVaSASkby5mrVgzcjH4uWfxuIiYZaQA7NUbIOTZel0ClILOXP5YUZVK2pC4hew-m7RVLyQup8SQK9j-_qc8NyhH12LwtMmoht0MX22smEsh0kDppTBjp249LCuA0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWspFoFZ1PobpVjPKmqYToCS8xlwqsyidulIuEfOsAFRQv-U1dA-AGMfdN1Fso-QB0BipKHcb-fz9cpyvgAeHGltj_o4ge2cAO48qyQFm-EdOnAeHQqTjVwO24xzY6zuQiMNtijrBxIyOM-hz3jp69fTSSRpM-9CPCKAzito3qcbedbJ3gbMf4IKkThSW38_eRTe3JB-VR1-bX3vx_63WAhCW9yqMHfH-QKvDk-NwQFCRkCOKj_MMiuHoIocX6y-Skx8twEF98VX-jJX2ffdY57nkXxj3-fYDPozc4Ewpkp6mAI3ZyWMI6STYHYf7irPB0mW6g5HYeT5JQQZEnnORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FemaJRdCZXxeXZH9r3TNtOv58ETh4Y-wNBDZZE5-PrWDghBau-rAVwzRC5y_yH5WHK1oWBw2VkHhZ4dU7LOfNtrWvNZX36iPEmQW25LoNRmIgXuSm7ubOJ2xuVcCCRfUOYrZbn6-QCmMtCrAQUwz77CbPSQqDxolQPIFWEb9O3AH847XbRxENrfnYEGz2303RH0GdEvjfSefirVF28zHp9arkPiy9fRWalC_dx5Hyrorc7lHeuGAIOrMbwYt9GlXGkCiixOvLykKQ7sERvV-eLusMxqp2PTH_OHKmK2oxdMdxDpH8K0Jd7W5x7PIeK8iZR6Ep46-VRgKdnLTi7SDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hu967w8ftwAAYohuhnyvtS1sYnlABsBXkbUup_4TK18stYY-dQt14Ux3s2cImbIq765p_gj7fOjX4WsipNXO44_127B47VH_2sS07UVrws14TuQakOThsLC8mV9YSWd3nL5j4X0WoTdzhfGiUdt_xudotZut-tduCkmW-zU7t6E6lPGr7-LEMyhVF2RBu7TXoTJgsKS1ymanN2uDX8tTIZ0bEPAH4WGRasCuSbI0M7ZSVbTk-6D5LZupSN06V98UIcqwmaleflN4HPDWDdZEtGiIH5yp7wpWAB6PLon_YUwpFFPN6XT_h6VAsBwLowbVm4Le0ykJBTTncYZlSCnG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-WJsiUVII0AcidvJpyyK6IAfiYJbQwgoxBZCERb-aR9uNghjuJy7wd8qyxtBl9HrSHrmRAPLqsv4AgvNmpsz-mBV9_myvFZ0AOjtAx7JYmzNfiP9QEsQLLClm7xQhSngBfT0hwy5eEbMWf0iAt86Qkc1u_jOD5fW0RTGYom5wOC5cggW6uBMSmRupimrpAjYyQPphQERPEYTvJtcyk8Lv4Ez1x0sVF2k-7zJTm2C3UjCmSNCecvG_LnZyoJstbmfZep_xopv-qfg865cE9cEUWutqmN3jWZaOap-sX_wY6Uw5GKwkxI0oXA0Gk5dnpPL3UuO_J7wVCm9XS64aQSHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0iTTa4eAyyQrRDvzjR4_BcBSIliYBzVS3cyIbGib8YTuKvAg3LN8KE64mUeOcd1DIOPXjqknygzZrkoK4yYsTqBuuSFHxfqKm7275nXz7rKD8CXEbuLFf2rlvXv9EPxQ5-uTC0gDuPtZii7ZxlXnwRp2EPe01OFYqQXeQ95hnTT5QhnXY6Yg2ktOwJTSf2SDvZFyjmGIuMTBFozzpRZsEb7L7jLm5Xr2MTVYsVfl9HWYkxOgGDrCQttkcmDa2Nd_Kb8V8bynxeH68E-5YNyfK4JmI8qrdoPj715yOi2qZiCKlL-oOFlAEEsPyAJ41q8YkgZC-4QMeFNU1y9sDvGew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سارقان و خریداران اموال مسروقه در تهران دستگیر شدند
عکس:
‌محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/458157" target="_blank">📅 15:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458155">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0PJcPsmmmEQj8rTeKqVktcyzq7PyURJhAFtqJjygd1xfuqz5yVVeAlsjikuzMwwHsU_6my_1Ym3J4-2hvXngXDlmz8fY7Bp9lWFfC4K7Oh-lRD1BBaIAlX3ySQEZWxqLK6yU0TZ3lygn1cqOnVUVDLHqBuQym3dw2JZOPzjgZP5LjK_ht12gN6ATJ0bltdP-ILSHNqiS3655zagym4_PhMNiNP-VIw7Nguwr7TsrtFhBYPkgFkCtrpbjOnPRKojG425fUY1QHFHPkQI-SAVBBlJYoiSXWORuoH5_8dgyspQduVmurL7vkfYxaSPyuoZJHOXYN8Iwc35kSFjjockHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FLyOY8Y2434xtHLSBxNHua_Zr_euvSpT20MSgiYo7dBCACNXQU9JB5qux75vkXsPPIL8rh1G0J9UlILUFJgsh-APIB2L9CgftUnVAAJkMMgmkwPsiUAdQrBi1SMmcVRThztQWQBxml95DGyxJBBM8QF1A4kBGvzrzuxnRbCmL13fTw6xdFZTcFLkW3tsfrZOMrBwqIby2FvFVzgaatirSk-UZt5iWc5_M-NKtDNc937nZHsjv4Ar_frOC8HqwyhS5LnQAqtf4KM9e21Zoe_1NPdeKoLPMWzlMsnijyPc0t4uTOqe3_Ef5KF5Ngxb_QzDNlAN-LWd8YnfJp3NdcPh2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزیر خارجۀ عمان فردا به تهران سفر می‌کند
🔹
سخنگوی وزارت خارجه: این سفر در راستای تقویت همکاری‌های دوجانبه ایران و عمان و ادامۀ مشورت‌های مستمر سیاسی بین دو طرف، به‌عنوان دو کشور ساحلی تنگۀ هرمز، برای کمک به تقویت صلح و امنیت در منطقه انجام می‌شود. @Farsna…</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/458155" target="_blank">📅 15:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458154">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGFZMHoiB1w3UWL8koP36rGrdxpR2uFBu6_4Vs8HOeK8oNs96rhEhkCTBi3EX65POKnWoa4uX0FIFQ9SD7_VHXy3Ph4JPjF5eJB-buG9u-SPoxgnkL5n9VE-RmCXdGSipHsHafy2Ms8BBOk75Sxk-R6IUj5s7ND6_nvsKPD9lAlja0l67_9p3TGSory18Nfj1wsoTdnzaAIaKYz_U5U2X9vpr0nFzO0TjRDjWvNpqWMFZWMnasDvYK2QeyT4LKC8zpWoQojKNkfPnwlqJCPLMGeuY8-8XVc05l_UyKQaNXntqudQkLA9jPUL2e1UH4O_C9bNk7cGWKUo99HM_a1_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ از توهم هرمز به دریاچه کانادایی رسید
🔹
در حالی که توهم روزهای اخیر دونالد ترامپ درباره «آمریکایی» کردن تنگه هرمز خبرساز شده، حالا او در پیامی به سراغ تغییر نام یک دریاچه کانادایی رفته است.
🔹
پیام جدید ترامپ در شرایطی منتشر شده که پس از ناکامی مذاکرات چندین ماهه آمریکا و کانادا، جنگ تعرفه‌ای این دو کشور همسایه عضو ناتو بالا گرفته است.
🔹
او در پیام خود نوشت: «ایالات متحده در حال بررسی جدی تغییر دادن نام دریاچه انتاریو به دریاچه آمریکا است.»
🔹
رئیس‌جمهور آمریکا افزود: «ما انتظار نداریم که دیگر هیچ مراوده تجاری با انتاریو نداشته باشیم. از توجه شما به این موضوع سپاسگزارم.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/458154" target="_blank">📅 14:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458153">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pubhvdDuefs3DxIA9GWlZVrJHtlwAy1agzUaChBmbxh3EpMWlSKovY5LUOnd9OxZjE7zB8YQSuJxLi6FfaD5abUlVKkaiRZWokvnRu9WUi_XV7FdPnCeBYSKvxACx0YyF9XXadl4OaUbUlVHi6kR70-g9ta87z5QKCuIZQg9riUHwUA5zM-JLlLx7hwCwh8xPuoTIZxJlCY1rvmrMJGGIv2tsvP6gPMT_j6bfqNXfr7dQBkV3I8L9g5z87EnJoD7HpFYx2byjj_bwv8NFDrUg0nv4H1Y30FIaW5hcgCa7L5DVPjiEMCo3ucc-6vOSmz7u_pwb6luAePGHmC4a5Ts0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: هر فشاری که معیشت و امنيت مردم را هدف بگیرد، بخشی از جنگ است
🔹
کسانی که میدان فشار را گسترش می‌دهند بدانند، ما هم برای دفاع از مردم میدان را در چارچوب منافع ملی گسترش خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/458153" target="_blank">📅 14:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458152">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZbBZqSPQETpoXQ7lgCHbq5h04PEhHJ_Xf9jOSC3AFdPCmpzip81jyXJ8u-6cRcJ19S0P-l92GTrfUvxOB32fyre-fr16eo_gOWP6sXiKFbv_3MWrxrmzPstw5GawdEu3w-Hl9pke8BfifVZ2OqWSjTrJWQkXYVp_YRu79bTRAv5qhujp0nkxuu83AbzG4IM5AeqPByw9KLK8mJ_x0hBay63vKODvXwYcD5PrC2ncs5RP9QB61x7BKr5-xYekligbaZ7bOhkhfoff3Q7BwvVtCI1V7F5RzT5Vu1Oovg8Mt8GpAwnefFEuxWk1pIlcv2dmSZjmspUGtEpfhtRpAxT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۲۶ سلاح غیرمجاز در مرز سیستان‌وبلوچستان
🔹
مرزبانی فراجا: در یک عملیات از قاچاقچیانی که قصد انتقال سلا‌ح‌های غیرمجاز از مرز سیستان‌وبلوچستان به کشور داشتند، ۲۲ کلت کمری، ۴ سلاح شکاری، ۲ نارنجک دستی و ۱۳ خشاب کشف شد.
🔹
قاچاقیان با استفاده از شرایط سخت جغرافیایی فرار کردند، اما تلاش‌ها برای دستگیری آن‌ها ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/458152" target="_blank">📅 14:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458151">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a487029da7.mp4?token=OfVSej94AlqzjyHb7KwXrrMlziunZhvOyT8sm4nETqg9yAG8ZlW2t8BoDOUorwcNtk33WHD_iueGmdi1yD7zXx_szwAz27XqvFEl2nyq-l7y9j4l1cm7M9MceS2kHsU2_WZOXe_wrzRf-gWQvIpw4VsKLKXYUHINHu7iPOwU2TT4dR2Pl9_1Nrbn3o4nRfTyMFpWsvLSzDKOw38yCEMfSTbPXxWhD948R3SXcef9Lmiin4tjZViojRJ0e4EOPJ3SADRpm1Z48459XuVbQDFYqegkYgOIIyMLnZQ6Ugj6cWxW0YuxzV1N2guDb4OGSjzEqC9li9WQq56DaVxycSLpRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a487029da7.mp4?token=OfVSej94AlqzjyHb7KwXrrMlziunZhvOyT8sm4nETqg9yAG8ZlW2t8BoDOUorwcNtk33WHD_iueGmdi1yD7zXx_szwAz27XqvFEl2nyq-l7y9j4l1cm7M9MceS2kHsU2_WZOXe_wrzRf-gWQvIpw4VsKLKXYUHINHu7iPOwU2TT4dR2Pl9_1Nrbn3o4nRfTyMFpWsvLSzDKOw38yCEMfSTbPXxWhD948R3SXcef9Lmiin4tjZViojRJ0e4EOPJ3SADRpm1Z48459XuVbQDFYqegkYgOIIyMLnZQ6Ugj6cWxW0YuxzV1N2guDb4OGSjzEqC9li9WQq56DaVxycSLpRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژه‌ای در دیدار با رئیس شورای‌عالی قضایی عراق: همکاری‌های ایران و عراق در همهٔ ابعاد عمیق شده
🔹
رئیس قوه‌قضائیه در دیدار با فائق زیدان گفت: روابط ایران و عراق در بُعد قضایی و حقوقی روابط با تفاهم‌نامه‌ها و موافقتنامه‌هایی که منعقد شده، توسعه پیدا کرده است.…</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/458151" target="_blank">📅 13:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458150">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6RGNUn5ziVwduB6H7UueOdIk2-VtKAm3CKSrzcw9oncEmxfKzgkyHqTHO42QwIU4k88T1UXCMYAta4MWvkJwkYpC_AshKpO1E0G_5KTfbcuSWxg_5Vqnj5PKrlDSZ7JrYuqasRapS-tJIvVuEojttwVsoZHDHTlDBMt-Yrow1HfcmFqUExVxDnMlMi2WMtN1k0gyiM8_-GcpfRu8BTl2PBOcN1aEC76vWf-EKotrpMXYS8j_kl4oz6DOlIrGjAs2gdq4YQNDBMkkqHzs8bhPsBuo4BMArbRag0Zal4BPSu-Qo3uH5hCq2UaNqe7s3AgT1iiyanEOQh9BcVXrFYVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قربانیان جنگ ترامپ با ایران در مزارع آمریکا
🔹
طبق گزارش فایننشال‌تایمز، کشاورزان آمریکا می‌گویند تبعات جنگ با ایران باعث جهش شدید هزینه‌های تولید شده و بحران مالی بی‌سابقه‌ای را برای آنها رقم زده است.
🔹
براساس برآورد فدراسیون مزارع آمریکا، تولیدکنندگان ۹ محصول عمده از جمله ذرت در صورت نبود حمایت‌های دولتی ممکن است امسال حدود ۳۱ میلیارد دلار و سال آینده ۳۲ میلیارد دلار زیان کنند.
🔹
این بحران در آستانهٔ انتخابات کنگره برای دولت ترامپ اهمیت سیاسی ویژه‌ای دارد؛ چراکه کشاورزان از پایگاه‌های مهم رأی‌دهندگان جمهوری‌خواه محسوب می‌شوند و نظرسنجی‌ها نیز از افزایش نارضایتی اقتصادی بخشی از جامعهٔ آمریکا حکایت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/458150" target="_blank">📅 13:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458149">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d8c64f97.mp4?token=ut4_5BlVDuCz7bvXq5JvIBaLxIwRqaVB1jDvYuGJdqD-pEeLQKENh05jdSo9mijytPg-LbyNrkiYWYdQ3J3DlCLnYUvOawqOInENqOcSPhXxyRP7heqF8akqd-E-91fIHjDSdFBd-ElquuferIy3xer-SfnR2aglaFSv9fn9wAXQXW2Dd4f5QU142yU7YrUmyzfAcSerWmuBmdIhOOeayOxGtA3CbQzsgzR48Q4OElgr1LItkDzWqoKdPWcUoSH9WRe_az-UKUsGV_ym0VeppC7SKmqgYHZsejqrS5odkcZUtiPC2bZeAFvyZPWXqMWY4kQZHo0Tptm62RShZ7Tu51q3YjeKx7XcFB7QfK2yX7CNk3CZnE8tmTXmAbSlRmf5lNkP438zD4nTDNTdqtf6ZR3j4kpbPKnPNrf22WdEQV0iVsmwZ5lbNlaUsYWSU_Bl8YIAUSYBQ9hFzIX1-JhDS5DpP4xHdlaWskBbHirXYh1Vkp59MBkua4mBOFd20Y50hjmVcaBa-tKFc389Rap4f1wyMvdYh207Dk89aeS0hftA-7eEiKU-PmWCt9xg2jrKBvt2-DEEw4q9FMPtbAN9Ey6S_aa1L2W5ga69fGTpYN3X_PFirrVnXHNqxZVgGm4ilIub3NgMteuJ-7ylB0j6ZU1dsp3sDkPvWrf-uxbIYa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d8c64f97.mp4?token=ut4_5BlVDuCz7bvXq5JvIBaLxIwRqaVB1jDvYuGJdqD-pEeLQKENh05jdSo9mijytPg-LbyNrkiYWYdQ3J3DlCLnYUvOawqOInENqOcSPhXxyRP7heqF8akqd-E-91fIHjDSdFBd-ElquuferIy3xer-SfnR2aglaFSv9fn9wAXQXW2Dd4f5QU142yU7YrUmyzfAcSerWmuBmdIhOOeayOxGtA3CbQzsgzR48Q4OElgr1LItkDzWqoKdPWcUoSH9WRe_az-UKUsGV_ym0VeppC7SKmqgYHZsejqrS5odkcZUtiPC2bZeAFvyZPWXqMWY4kQZHo0Tptm62RShZ7Tu51q3YjeKx7XcFB7QfK2yX7CNk3CZnE8tmTXmAbSlRmf5lNkP438zD4nTDNTdqtf6ZR3j4kpbPKnPNrf22WdEQV0iVsmwZ5lbNlaUsYWSU_Bl8YIAUSYBQ9hFzIX1-JhDS5DpP4xHdlaWskBbHirXYh1Vkp59MBkua4mBOFd20Y50hjmVcaBa-tKFc389Rap4f1wyMvdYh207Dk89aeS0hftA-7eEiKU-PmWCt9xg2jrKBvt2-DEEw4q9FMPtbAN9Ey6S_aa1L2W5ga69fGTpYN3X_PFirrVnXHNqxZVgGm4ilIub3NgMteuJ-7ylB0j6ZU1dsp3sDkPvWrf-uxbIYa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
ببینید
👇
✅
معیارهای پنج‌گانه انتخاب مدیران در شستا
🔹
محمدرضا سعیدی مدیرعامل شستا ضمن تاکید بر اینکه توسعه اقتصاد در گرو توسعه بنگاه‌های بزرگ است؛ معیارهای پنج‌گانه انتخاب مدیران در شستا را تشریح کرد.
@tappico1381</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/458149" target="_blank">📅 13:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458148">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0UoWdqBGkpvCSStCectjt9lYg04DcpqZzhqWhywWEDEZrHaB3DhaycLfekhTUvTJmA8aYCKP7dOEqndSiVZufnNKZW_yKYnHLD2-sT8MAm6sPwMmdvDcJ7PnbETHbrLqc1k5JDB2MGBOdeAcCaywohP9XwJXnntcZ5rkB9v0IhJAXd620F91z4kDVeiAs4Elwe4VtwjrvUhNNfHiAZC3tyEzIbbeaLLplWc6unurj_xjBdZt96ykst4V7ZZePTPKR2_Jct3B3VhqHIZrHm8asoIQCjuY9jiTnZL_VgHY58nCv_xjvcZGDQkrSR3O8OfPk7MuylSmcKtrHS-l0Ctew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
واگذاری سهام «سیمان تجارت مهریز» در فرابورس
⬅️
نشست خبری معرفی سهام شرکت «گروه صنعتی و معدنی سیمان تجارت مهریز» با نماد «سمهریز»، با حضور مدیران شرکت و خبرنگاران بازار سرمایه در فرابورس ایران برگزار شد. این شرکت در راستای سیاست‌های دولت در زمینه واگذاری بنگاه‌ها، توسعه نقش بازار سرمایه و مولدسازی دارایی‌ها، در فرابورس ایران عرضه خواهد شد.
⬅️
مدیرعامل شرکت با اشاره به ترکیب سهامداران، برنقش کلیدی بانک تجارت به‌عنوان سهامدار عمده تاکید کرد.
🔗
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/458148" target="_blank">📅 13:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458147">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/458147" target="_blank">📅 13:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458146">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boziJQG1YlMPVDT66C7Oaq4Zb-j-t6r9OdFv4a-EVl34W9IlcWZfnA_TgxseGkrBKeeaOsrKBWaXwoW3gEYbFxl9auxaOVOvdN9JbLXQwqNMgzlBkqIkFbsi8q-lEidBx7bKUZlQZWB9Vjn9ynSy1smAMUw4g-6woMRs5wW7eRWsMrJ-cLa1McehzFkls7MMhqvKALhR74VFVIh_uu531jdzWH6cVp8l59BbdYRU2Qszha0Ddch8RZ6czCMbL-mR0Yi5-v5FmfshlSCe5PtGoC6KK4YaSMz54C5m_PQZC8kkXmlLNIRWW3uOFNOoFMjsrO4xp2x9w_JKsGs0fp5pTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای در دیدار با رئیس شورای‌عالی قضایی عراق: همکاری‌های ایران و عراق در همهٔ ابعاد عمیق شده
🔹
رئیس قوه‌قضائیه در دیدار با فائق زیدان گفت: روابط ایران و عراق در بُعد قضایی و حقوقی روابط با تفاهم‌نامه‌ها و موافقتنامه‌هایی که منعقد شده، توسعه پیدا کرده است. ما بر تعمیق هر چه بیشتر این بُعد از روابط تأکید داریم و در این راستا آمادهٔ هرگونه همکاری با دستگاه قضایی عراق هستیم.
🔹
اژه‌ای با اشاره به تفاهم‌نامهٔ تبادل زندانیان بین ایران و عراق گفت: یادداشت‌های تفاهم و توافق قضایی و انتقال و تبادل زندانیان میان ایران و عراق منعقد شده و بر همین اساس، ما بر تقویت موضوع استرداد محکومان ایرانی و عراقی و ایجاد تسهیلات برای خانواده‌های آن‌ها تأکید داریم. پارسال بالغ بر ۱۳۱ محکوم ایرانی از زندان‌های عراق مسترد شدند.
🔹
رئیس شورای‌عالی قضایی عراق هم در‌ این دیدار گفت: حاکمیت و ملت عراق در موضوع تجاوز جنایتکارانهٔ آمریکا و اسرائیل به ایران، با دولت و ملت ایران همبستگی دارد. ما هیچ‌وقت حمایت‌های ایران از عراق چه در سال ۲۰۰۳ و چه در ایام بحران تروریسم را فراموش نمی‌کنیم.
🔹
خون شهدای ایرانی و عراقی در مبارزه با تروریسم در هم آمیخته است و ما اوج این قضیه را در زمان شهادت شهیدان حاج قاسم سلیمانی و ابومهدی المهندس شاهد بودیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/458146" target="_blank">📅 13:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458145">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YppLEocn6hwW1I23SDmhu8UGrVbxzTMPvUWTfPESrQmZL4a6-DFZknPuid5zXY51f-rPCCQdeph7dFw20y9Q6ZpLDTDJFz0Bjmy7AfC9Wpg2bO5VD6Rdsah_s22qAiEpukz7ssj5l6oetIrsl2FvVay72KFci_ZJ82D5opB5-CpdAz65t4RQ6Rw4uRXWDUkv8ZD7yFsrjdfp3lqGP5T_wHHNyRu9dFnhPS05f3-0UV87jYlluTdOiCHRV-iKOKZtD85bLs2QGXSV-MHkxbNNdp1TvBPbRWuOTB5Hw6icBbJeq7KwnqYM-ur_CKgw3Ga81C5MTaIMPEH6bvZDSE_sWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گران‌ترین بازیکن لیگ ایران مشخص شد
🔹
سایت ترانسفرمارکت در به‌روزرسانی جدیدش ارزش بازیکنان فصل جدید لیگ برتر ایران را اعلام کرد تا امیرحسین حسین‌زاده، مهاجم ملی‌پوش تراکتور با ۲.۲ میلیون یورو گران‌ترین بازیکن لیگ لقب بگیرد.
📊
پنج بازیکن گران قیمت لیگ برتر ایران:
⬅️
امیرحسین حسین‌زاده(تراکتور): ۲.۲ میلیون یورو
⬅️
اوستون اورونوف(پرسپولیس): ۲ میلیون یورو
⬅️
یاسر آسانی(استقلال): ۱.۸ میلیون یورو
⬅️
علی علیپور(پرسپولیس): ۱.۷ میلیون یورو
⬅️
حسین کنعانی‌زادگان(پرسپولیس): ۱.۶ میلیون یورو
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/458145" target="_blank">📅 13:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458144">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8OerPeIM3vECjmPmYeK0gA1lDk7nG2-G3gm8cC-ffxEuTHT5ZCkxeUybAq22xawnRIbPB8TSDG5rCvwuk18EYdJrvwoix7ewR_hO3NeFxv5fn96C5ejvLB2hZw0v-kBN6wq5yXbAaqt8uPa0YYtnxeTnXT9t5Nq7P33yTJ0AECqHaM-2_tzkB9c0RQW1zdk8u7EB7O7YT6gJjuel79-IW-r8jjjareeFQ8BgMsu0naFfcW1aLqxqyBuYs4OkLdPzm9qGcdV1zSY-T5WUodx8aR5be0zuU1MNc_VbkEan7jrJtvtyDViynbvah9N55CsDAmybMWyLBpuIo8i7CjG1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین: با تحریم‌های غیرقانونی آمریکا مخالفیم
🔹
چین ضمن مخالفت با تحریم‌های یکجانبه واشنگتن علیه ایران که افراد و نهادهای این کشور را هم هدف قرار می‌دهد، تأکید کرد که از حقوق و منافع شرکت‌های چینی حمایت خواهد کرد.
🔹
به گفته سخنگوی سفارت چین در واشنگتن لیو چانگ،…</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/458144" target="_blank">📅 13:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458143">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">طرح مقابله با نفوذ بیگانگان، در دستور کار صحن علنی امروز مجلس
🔹
سخنگوی هیئت رئیسۀ مجلس: ادامۀ رسیدگی به گزارش کمیسیون امنیت ملی مبنی بر مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در دستور کار جلسۀ سه‌شنبه صحن علنی مجلس قرار دارد.  @Farsna…</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/458143" target="_blank">📅 12:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458142">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXavLdFfbk5b52wUr9qQmBldLEJ2LxAZIv2Yrv6fHHlyEozDnrS7Xu0IU5KmaKVAM0MF4obAQbl7t7juSE6OsUwY43nttUS22X6BCZGT0RbvBcgvm0Pj7H5fweZLfWYl97-8SE2LOZA8jn55aWfU4VHn5tLr0F-trUoymaooAphx-Zj4MNewr-DPfpwXVjgyHrZd6tDv51SUTgG1uLnU-WR8whe9sytiH7c8Bp0hQgDUAp-rD5NeXyqo1aMPjuZnYvHCxLMwAmDRkYDMJpL7t9FjFuXlxepK79gqxIdChy1cM9eYqmpf5Jy_6X6FP2tNpzeVLskDc8Rn-2KfXRK81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد تاریخی جدید بورس با جهش ۲ درصدی
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۴ هزار واحدی به ۶ میلیون و ۲۲۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/458142" target="_blank">📅 12:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458141">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ab6957ba.mp4?token=EKGqPoaCulfwkqD12UzK5nncVgel1bkqbwU0HelLWA342THhz1TIjBi6369YJXZMTUA-q2-SnVuLEna9amDtGS_1vWw_5BMy6ZEcca_dmvA7km2JFnw6zO8aNeodIgCpdMRYQ1K0l0474QaZF_3ydOJdHc5N-eJ0EOv1JjatrYAjLmX410CVKeUfkS8cgY5_eNhcYftuGofH0VUH_pwltdBB81HfdBNhxaoW_TSoNLMdVB07H8ohPFOxnELHxVT19wohOxS5m4dewZMFneiOhkUGPUnRhH7I3LaaARHwg4M1RgBB11IFZzrqTGUK4pMyO-LGrq_YnHB1aylbIV8AUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ab6957ba.mp4?token=EKGqPoaCulfwkqD12UzK5nncVgel1bkqbwU0HelLWA342THhz1TIjBi6369YJXZMTUA-q2-SnVuLEna9amDtGS_1vWw_5BMy6ZEcca_dmvA7km2JFnw6zO8aNeodIgCpdMRYQ1K0l0474QaZF_3ydOJdHc5N-eJ0EOv1JjatrYAjLmX410CVKeUfkS8cgY5_eNhcYftuGofH0VUH_pwltdBB81HfdBNhxaoW_TSoNLMdVB07H8ohPFOxnELHxVT19wohOxS5m4dewZMFneiOhkUGPUnRhH7I3LaaARHwg4M1RgBB11IFZzrqTGUK4pMyO-LGrq_YnHB1aylbIV8AUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: تا ماه آینده از طرح جامع تقویت اقتصاد خانوار در تهران رونمایی می‌کنیم
🔹
این طرح در ۴ سرفصل مراکز آموزشی و پشتیبانی دارد تا کمک کند که اصطلاحاً به‌جای ماهی‌دادن به شهروندان، به آن‌ها ماهی‌گرفتن یاد بدهیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/458141" target="_blank">📅 12:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458140">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad6cf14bb.mp4?token=Tpw-qOqF8j1fEKcdYjsnFSZwjDJke5YOIi8e0G8Spp7_VLmaVOU5NKN9hlNvatxW8kpXGRoYzCp34EKn02mM8kc0dyq0Iv9BrbiAsXhnFkvD5Pr-0-kQNJ7aK7xEOBKvDb2Tr_R-lFvJ1BiDigEoi5uh9r1lMUsrbtx4wasby7Mq_mkrOD3Ldm39hYsnK2RrIpD1KwpYo230B15CXZO5y_4t57cG_nSq2XKs39z3BjBERZ8U4LzY6heXoRm88d0ZLvQr6HShXh8_Est2Nl7AjfvWIh5RNuYlLJcVJoYuYWndNWXjDdQHdVjqAM-z6CKai7PIJMMOGC5ckMl_N-ysRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad6cf14bb.mp4?token=Tpw-qOqF8j1fEKcdYjsnFSZwjDJke5YOIi8e0G8Spp7_VLmaVOU5NKN9hlNvatxW8kpXGRoYzCp34EKn02mM8kc0dyq0Iv9BrbiAsXhnFkvD5Pr-0-kQNJ7aK7xEOBKvDb2Tr_R-lFvJ1BiDigEoi5uh9r1lMUsrbtx4wasby7Mq_mkrOD3Ldm39hYsnK2RrIpD1KwpYo230B15CXZO5y_4t57cG_nSq2XKs39z3BjBERZ8U4LzY6heXoRm88d0ZLvQr6HShXh8_Est2Nl7AjfvWIh5RNuYlLJcVJoYuYWndNWXjDdQHdVjqAM-z6CKai7PIJMMOGC5ckMl_N-ysRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: شهرداری کنترل بازار اجارهٔ مسکن تهران را از چنگال سوداگران خارج می‌کند
🔹
۵۱ درصد تهرانی‌ها اجاره‌نشین هستند که بیش از ۶۰ تا ۷۰ درصد درآمدشان را خرج مسکن می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/458140" target="_blank">📅 12:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458139">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a323b1e08.mp4?token=Fs9-VaoSlUXKZBfa4qg7jxU0XhbsL-59U0KcC1_iE5xwaFOFwHHMlUrqJopt_JIEIOy8FspmwNMLK0cizwAAdwTY9Z0VwCz8c_jqo4StWh67mOJr8Ex0gan6lZ0SzloRMxY75ZRhjrEudyS3_jXHY6dsbKchfXeZHX4EXhoYmIL-M4VKLB_A4momtA1_UoUad6qvl-ItSs1kKNY64lZ_soz9U2-K1j8d7Nrb8WNFiwSv9VMmFaUPQCTimj4o8adZCurBs62Ho6Wo5RoDqMYoLDenDvFL1ub9cPSjW4V7TpOMsV5Bh7SttEJjpfI6mIQeaCXdE-EOo2nvgILcRIyMlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a323b1e08.mp4?token=Fs9-VaoSlUXKZBfa4qg7jxU0XhbsL-59U0KcC1_iE5xwaFOFwHHMlUrqJopt_JIEIOy8FspmwNMLK0cizwAAdwTY9Z0VwCz8c_jqo4StWh67mOJr8Ex0gan6lZ0SzloRMxY75ZRhjrEudyS3_jXHY6dsbKchfXeZHX4EXhoYmIL-M4VKLB_A4momtA1_UoUad6qvl-ItSs1kKNY64lZ_soz9U2-K1j8d7Nrb8WNFiwSv9VMmFaUPQCTimj4o8adZCurBs62Ho6Wo5RoDqMYoLDenDvFL1ub9cPSjW4V7TpOMsV5Bh7SttEJjpfI6mIQeaCXdE-EOo2nvgILcRIyMlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ عرضهٔ مسکن متری تهران از فردا آغاز می‌شود
🔹
درحالی‌که بیش از ۷۰ درصد درآمد خانوارها صرف هزینهٔ مسکن می‌شود. شهرداری برای خانه‌دارکردن مردم، از فردا طرح «خانه‌ریز» را به‌صورت رسمی آغاز می‌کند.
🔹
قیمت خانه‌ریز معادل میانگین قیمت کل آن ملک است و افراد می‌توانند…</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/458139" target="_blank">📅 12:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458138">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2af26a6d5.mp4?token=qgvVTAVLdoHDtC_99nSNQ2aC3Tx7VEDutpjqBLUGfm8EV3SaILSWgnr0BPV7mgMFKD61Q7YYO7FiBa5w9OqwN7pst8S4PPDqH585xyjAl0xfhJ5-i7OqTxtwrM-sWxHo1nf8-2YGxPPTRYkqhipYXWH1wOU9CBFibB31rLKx7D2fB0gwcwXwbhsoiHKhmXStGwx2zmwOsfImF4aJN09gpiVw2kfMZSmMa_XqJhALrT04q6Fr4s2TsePOf2QmabVVrAC4RB59l05V5M0NWzrGs_ltGsRffB__zbOBLxavUM1UZ4Tc9BynwAu2Yh5Y-TkavR8MBX9LHEAhdUKqsTjEGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2af26a6d5.mp4?token=qgvVTAVLdoHDtC_99nSNQ2aC3Tx7VEDutpjqBLUGfm8EV3SaILSWgnr0BPV7mgMFKD61Q7YYO7FiBa5w9OqwN7pst8S4PPDqH585xyjAl0xfhJ5-i7OqTxtwrM-sWxHo1nf8-2YGxPPTRYkqhipYXWH1wOU9CBFibB31rLKx7D2fB0gwcwXwbhsoiHKhmXStGwx2zmwOsfImF4aJN09gpiVw2kfMZSmMa_XqJhALrT04q6Fr4s2TsePOf2QmabVVrAC4RB59l05V5M0NWzrGs_ltGsRffB__zbOBLxavUM1UZ4Tc9BynwAu2Yh5Y-TkavR8MBX9LHEAhdUKqsTjEGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی: کالاهای اساسی را برای دهک‌های پایین جامعه با تخفیف ۵۰ درصدی عرضه می‌کنیم
🔹
شهردار تهران: یکی از اقدامات مهمی که شهرداری تهران به‌دنبال عملیاتی‌کردن آن است، ارائهٔ تخفیف ۳۰ تا ۵۰ درصدی در کالاهای اساسی به دهک‌های پایین جامعه است.
🔹
در نخستین گام به‌دنبال…</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/458138" target="_blank">📅 12:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c6340a4f.mp4?token=JMeYRhJixkQvas8vlSpVEP45mCFAaMcTUeerDTLpy5RdD16IVn08bY2vGL4uZuTqOxjQcpj2Euj-voWCf1qsO_gzUvAyocFatg9Bir28PJe4UUvqIwQRPKtsxtbvaStRGMjCayeMNMjnyNlAFsCIptf84Uz-6_sHSO1fP-keSyWzbOAArOUtCvmgRe2ERBTSJjtnVaBzTMl65v9TaUkwsF_95rQsa12CRyCXi7TJp2EUIi2TwsGqBixTUC1yv0Zb_VCnrSb6CWI4m4Nmy6hGiIMzWbMTof_xirqGTWNpZnSkijLwdrDpLF_Pi5SHXItGA31M4PBJtzfdLdK9LWRYVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c6340a4f.mp4?token=JMeYRhJixkQvas8vlSpVEP45mCFAaMcTUeerDTLpy5RdD16IVn08bY2vGL4uZuTqOxjQcpj2Euj-voWCf1qsO_gzUvAyocFatg9Bir28PJe4UUvqIwQRPKtsxtbvaStRGMjCayeMNMjnyNlAFsCIptf84Uz-6_sHSO1fP-keSyWzbOAArOUtCvmgRe2ERBTSJjtnVaBzTMl65v9TaUkwsF_95rQsa12CRyCXi7TJp2EUIi2TwsGqBixTUC1yv0Zb_VCnrSb6CWI4m4Nmy6hGiIMzWbMTof_xirqGTWNpZnSkijLwdrDpLF_Pi5SHXItGA31M4PBJtzfdLdK9LWRYVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون پزشکیان: رئیس‌جمهور به من گفت «آقای زاکانی یک اتاق فرماندهی برای پایش وضعیت مصرف سوخت تهران درست کند و من حاضرم روزی یک ساعت در این اتاق وضعیت را بررسی کنم». آقای زاکانی صددرصد پای‌کار است.  @Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/458137" target="_blank">📅 12:22 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
