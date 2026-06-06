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
<img src="https://cdn4.telesco.pe/file/pAOfAhPescjWXlVXVusE6LBGN2pif_OUhruW9FKiLYXjNTaVKpID9h37MRICjH2KPklEiNUpKMgFc38Zf9A9X8i48RNToYqCxQECocyMNtsDUWI0s_nhu_4_YTwZWnULe0AXi3AR_aJDc8Q6ts-5LZrpFjRVLBPa7eDZd1uqMzcbBTNaBFKsgIx7A2JeajF8Nxzl5qTKp_Hw2CzoTYW4d9_OPyC1oa62umhGx5ksOtTBVW2U4BbY9IK8y9OCL1eMpnYTwOQeAvQSJdZ8z-syYn5lcw1BKWEeOUxpSXMwK0yQ_ayxYp1zIghsNv0BkuRsQtw1TUJ3hsu7SWLYz7aAcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 12:35:58</div>
<hr>

<div class="tg-post" id="msg-656566">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc25e75fea.mp4?token=r8wGr7KgB6-o36F8BDSWMxATkEeeHlVRGU0dbsSrzzuvfx_ZKkmG7xOyhqdnUYKVF5gXJGAAVEzw-Lbhe1z2lBp0o_MiNNNzUAlRMO2u2PvR_zaFsdsZPj1ADWJ5FjaqgnDRO60FgA5EJnSuEBoSEg2xK0_yf6WG3OWldQCKtRKKR9t4UFMiMO-hz4QK7FydMhWNRt9686elf412D10yPitcwoJmZAKfBtHgoTkss7kBltghUi2Dx5PzdWqAbEz4fvU8YbcUMMLpVdXeBYszJlWOpl66Xp4h1QA5H7QxahiBIFLwJaouK9G6fww146SLKzi3f2KJR9JnTJNjcv8UzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc25e75fea.mp4?token=r8wGr7KgB6-o36F8BDSWMxATkEeeHlVRGU0dbsSrzzuvfx_ZKkmG7xOyhqdnUYKVF5gXJGAAVEzw-Lbhe1z2lBp0o_MiNNNzUAlRMO2u2PvR_zaFsdsZPj1ADWJ5FjaqgnDRO60FgA5EJnSuEBoSEg2xK0_yf6WG3OWldQCKtRKKR9t4UFMiMO-hz4QK7FydMhWNRt9686elf412D10yPitcwoJmZAKfBtHgoTkss7kBltghUi2Dx5PzdWqAbEz4fvU8YbcUMMLpVdXeBYszJlWOpl66Xp4h1QA5H7QxahiBIFLwJaouK9G6fww146SLKzi3f2KJR9JnTJNjcv8UzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو جنجالی نظامی صهیونیست از کودکان بازداشت‌شده فلسطینی
🔹
انتشار ویدئویی توسط یک نظامی رژیم صهیونیستی که در آن گروهی از کودکان فلسطینی بازداشت‌شده با دست‌بند و چشم‌بند دیده می‌شوند، موجی از واکنش‌ها و انتقادها را در پی داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/656566" target="_blank">📅 12:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656565">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
منبع آگاه: وزیر کشور پاکستان امروز به تهران سفر می‌کند
/ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/akhbarefori/656565" target="_blank">📅 12:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656564">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعایی عجیب؛ آستان قدس برای تخریب آثار ملی و تاریخی مجوز گرفته!
احسان عظیمی راد، نماینده مردم مشهد در مجلس در
#گفتگو
با خبرفوری:
🔹
مدیر کل میراث فرهنگی خراسان رضوی عنوان کرد که آستان قدس از دیوان عدالت اداری مجوز گرفته و فضای انتهای خیابان نخ‌ریسی را که جزو آثار ملی و تاریخی ما بوده را از ثبت خارج کرده است و بدون مجوز شهرداری آنجا سه تا چهار مغازه تجاری ایجاد کرده اند.
🔹
این موضوع اگر بخواهد در سطح شهر مشهد یا کشور باب شود عملا آثار تاریخی،فرهنگی و ملی ما یک به یک از بین می رود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/akhbarefori/656564" target="_blank">📅 12:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656563">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXH0zOA1--zrqJPpZv_rDDicKGrEifX12A7XnpICAJvE2aMipCgbfgFZz2VUI5vq7s1nkeamG_N_nz33IKSCm0FANCV2qvtPvVVs-X88Heq6VjlAmZs1zhRoQ09fkPbrBP_klj_AFsa-vr1YsSMYfMS7eMJVh92_0ghV3aqfc8J66rIcrufmd3v65dkYWQgyX92DbR4orKj1XLBx3ug6fe-F9v5kHcLze2Kbj2sRJFK8A_RL0i4FgiXGl5NEz3nGGLT4wIb9JJfLM7YdPbiRV8DU0CdzRop8sFoiSUNAoDoRWM-H1h9HOIu9jfHC7xJ5j54P_XrmS22Zvc255HBPgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام وزیرخارجه خطاب به رئیس جمهور لبنان: لبنان را از دست دشمن واقعی خود نجات دهید   وزیر خارجه:
🔹
بر اساس اظهارات آقای عون، ظاهرا این ایران است که یک پنجم خاک لبنان را اشغال کرده، یک چهارم لبنانی ها را آواره کرده و کشور او را روزانه بمباران می کند.
🔹
اگر لبنان…</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/akhbarefori/656563" target="_blank">📅 12:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656562">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bw_uJts8jW4Wk6B2OUgcYQ8Vf0fSJVj6tCNxbwA0lcRKIhTx5fQgbbuZmxFq-ikIwDKJ1PDUArLTq_2U1KCg3pDID0WkqdFJgEETIYFtbgCsysFKE18JjJml_seUNrXmE4qBtExBIj2rnLxhdZ2CxLnUobgPd66UPRJLNEVQkbCllHpwlLsBIzHBb4vlp40RkqMe89ubf5RnqgP82EZ-oHppI6NS0Jj9oBbrjK-Mhw4XwEGBAYZE_B6qADokNWz3Eo31Tbf91OvN-h_vawLp5RX44GAaMqzWKR84hu8u9xqRZsTziq65Ki33I1Y3f1062_EnxfhTcC6suOKjW_oFUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه‌های جلوگیری از بازنشر اطلاعات غلط #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/akhbarefori/656562" target="_blank">📅 12:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656561">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb1072b44.mp4?token=TXTDV4VI3L3IhSy-vJtLxZQPf7zPTbPg489vIbfa-i299zf4Hbm-84fGcjDsfjbgEkV7-IYmYl7Xf-5EOijvaj4NsQEW_ac8TyQ_Q5Q6INdki_Y4-pHOQxui9hyTsZhQYWF2ZGdovx3gp1bSjAha476q3JQHqbGn4IsV3SmwKz54uIjXXvGlGKZa41UOubkv9WBjooN9PG7T4jo4Z689MVTB1kvJY5uuruK5irhj1KTD1pxdxtpWWcxYyLqkvdovQWQGJe-_w6oeES7OW3QX4-8riDVXeImBaHZuYPB5ZrqAW7PrkC56i4fSuPkE9B44umN6IisOOFHwfijhwGKanQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb1072b44.mp4?token=TXTDV4VI3L3IhSy-vJtLxZQPf7zPTbPg489vIbfa-i299zf4Hbm-84fGcjDsfjbgEkV7-IYmYl7Xf-5EOijvaj4NsQEW_ac8TyQ_Q5Q6INdki_Y4-pHOQxui9hyTsZhQYWF2ZGdovx3gp1bSjAha476q3JQHqbGn4IsV3SmwKz54uIjXXvGlGKZa41UOubkv9WBjooN9PG7T4jo4Z689MVTB1kvJY5uuruK5irhj1KTD1pxdxtpWWcxYyLqkvdovQWQGJe-_w6oeES7OW3QX4-8riDVXeImBaHZuYPB5ZrqAW7PrkC56i4fSuPkE9B44umN6IisOOFHwfijhwGKanQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخستین فروشگاه دیجیتال همراه اول در تهران افتتاح شد
🔹
همراه اول از نخستین فروشگاه دیجیتال خود در تهران رونمایی کرد، مرکزی که برای نخستین بار امکان دریافت بخشی از خدمات اپراتوری را به‌صورت ۲۴ ساعته و هفت روز هفته فراهم می‌کند.
🔹
این مرکز که در محدوده ونک راه‌اندازی شده، با بهره‌گیری از کیوسک‌های هوشمند خدمات مشترکان، مراجعه حضوری را سریع‌تر و ساده‌تر کرده است. توسعه این مراکز بخشی از برنامه حرکت به سمت خدمات هوشمند، منعطف و مشتری‌محور است؛ مسیری که می‌تواند شکل دریافت خدمات اپراتوری را برای مشترکان تغییر دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/akhbarefori/656561" target="_blank">📅 11:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656560">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ستاره‌های جهانی در تیزر جدید نایک؛ از رونالدو تا کیم کارداشیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/akhbarefori/656560" target="_blank">📅 11:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656559">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcoVn51G5pIsHQZtqushZZLyJcumRpj_AhsV3fkFum_vTUsTaB1acQYj23vNKUFeKoxZsTUEWOdRdtfZjQvMX9f-03wPkkmjnohvLroeenL-hNxBFhlmY3naLnsORsniOpIkXTLrO9pDYvGsXcwXZnyCXjP93gvzUbI60f6b5S0nGiK1gttcqFX-lvRSJ3sjxsdlNvNk6YO8Il52L6GIKdkZmetfyoXoDOrMMf-miK09-QEJbq25hytrqzjZCzXeWPlw5pnMFDp3ZR37kY303t6CVUrtl5KG7rmNGHZaCWy9e9lxCFVA7jQzsPTgEBF_OdD_oVLFF6d0G_S3gpZc9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صدف طاهریان به ایران بازگشت
‌
🔹
صدف طاهریان، بازیگر سابق سینما و تلویزیون که سال‌ها پیش از ایران مهاجرت کرده بود، با انتشار یک استوری در فضای مجازی از بازگشت خود به کشور خبر داد.
‌
🔹
او تمامی پست‌های صفحه اینستاگرام خود را آرشیو و از دسترس خارج کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/656559" target="_blank">📅 11:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656558">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62d3deebb1.mp4?token=QNgmk9KKv2Miov8vysbwED_rSxlrzxGV88cmNkHqZBv_Kshrj12FPvS8KbJ51sqyN8Jyth-CAWWKpf9VW1mWDcoFNZbY8OpE385mS3M4Mq6PWY0uN1d0WX_pDCxH_vDPOSFgOx3t67_rPy760OQSi7s1dRB80T2jULN-UheK9CsFA3m2xYpGtZ5okBFtUm_3vgzpX4sTKCS33DJ3URpg12W68FeNMbDhEl0K1p-Wcw5jxduOeiWmhgWSoKhiq5kMJ1N1UDoTSWhz90myx3yxZo9NaChanvAiIVhBBD9dFo3UN0SMkS7MF62lcvUvUw7BGe82hstPm2JzrsziU0xLDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62d3deebb1.mp4?token=QNgmk9KKv2Miov8vysbwED_rSxlrzxGV88cmNkHqZBv_Kshrj12FPvS8KbJ51sqyN8Jyth-CAWWKpf9VW1mWDcoFNZbY8OpE385mS3M4Mq6PWY0uN1d0WX_pDCxH_vDPOSFgOx3t67_rPy760OQSi7s1dRB80T2jULN-UheK9CsFA3m2xYpGtZ5okBFtUm_3vgzpX4sTKCS33DJ3URpg12W68FeNMbDhEl0K1p-Wcw5jxduOeiWmhgWSoKhiq5kMJ1N1UDoTSWhz90myx3yxZo9NaChanvAiIVhBBD9dFo3UN0SMkS7MF62lcvUvUw7BGe82hstPm2JzrsziU0xLDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرباز اسرائیلی: با حشیش ترس از مرگ در جنگ را فراموش می‌کنم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/656558" target="_blank">📅 11:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656557">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a3ad089cb.mp4?token=r9m6-mQlWtKgf1i73AXSaTkSuKsB0X_eQ9UP0Gc1zqwuP0QJwo4UzMvJ7vq0hIpR3UjQJuageM38Naeh3R6Ueexfd0GMUUU3FeP_UbSeTAHMiireNyzXJe82iKmVeprSY2nFo16WGA_KKtu-hg_gNP9h-W8M2aBBW_7AY4SlWTu68m8bauxwISKO8SBT1mhehN8VukiiKdgaaklv_GIjrDo9MTrHFAdyKuIEmzKMGDHMOQ2av7gZlU50BPXSF9JHfT69u5eBBP2FH1y6gf3yLrDpyNYcTkIh9u9yMoH1Mx0BjsyqXN-p_1WtnQjAMhXonK3lz9mPsK7jnZRJvmYd0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a3ad089cb.mp4?token=r9m6-mQlWtKgf1i73AXSaTkSuKsB0X_eQ9UP0Gc1zqwuP0QJwo4UzMvJ7vq0hIpR3UjQJuageM38Naeh3R6Ueexfd0GMUUU3FeP_UbSeTAHMiireNyzXJe82iKmVeprSY2nFo16WGA_KKtu-hg_gNP9h-W8M2aBBW_7AY4SlWTu68m8bauxwISKO8SBT1mhehN8VukiiKdgaaklv_GIjrDo9MTrHFAdyKuIEmzKMGDHMOQ2av7gZlU50BPXSF9JHfT69u5eBBP2FH1y6gf3yLrDpyNYcTkIh9u9yMoH1Mx0BjsyqXN-p_1WtnQjAMhXonK3lz9mPsK7jnZRJvmYd0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تست نمایش پهپادی در استادیوم آزتکا برای دیدار افتتاحیه جام جهانی ۲٠۲۶ که قرار است بین مکزیک و آفریقای جنوبی برگزار شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/656557" target="_blank">📅 11:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656556">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
الجزیره: ارتش لبنان اعلام کرده است که چندین سرباز، از جمله یک افسر ارشد، در حمله‌ای اسرائیلی به یک خودروی نظامی در نزدیکی نبطیه در جنوب لبنان امروز صبح به شهادت رسیدند / انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/656556" target="_blank">📅 11:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656555">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e22e3e9e36.mp4?token=Rkkut4CmOWFLYtw7sOyO0n5k9K6mO0LAXURXqihbh7YspRZTPAk-GUHmgEO99VOfzuDsDKZ3kC7g75nUVM3hJyUkwoNNcHDfNH0LjMYBMt8ncyQiheFsuHru6LQxtkwnE4a518v6fT0oZQE6FxjVJDW7K5F_LS_pl0ezUfS9hMIdgBXZmHhEabU1a6NebCyYbFoEA43snvkLobEQlKCsxpNCizSlxhxqrw6ff_FTHXGNOT3YPjdZBkYIekW-n9n9Pcx5sqZQdMAPcSQdFJtdUD38WL_7xt-HfZqYf53UV-7ZWDgKy7WPOFWDfjQqaJGqxYD_5EcKY5xl5JfOaq4oRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e22e3e9e36.mp4?token=Rkkut4CmOWFLYtw7sOyO0n5k9K6mO0LAXURXqihbh7YspRZTPAk-GUHmgEO99VOfzuDsDKZ3kC7g75nUVM3hJyUkwoNNcHDfNH0LjMYBMt8ncyQiheFsuHru6LQxtkwnE4a518v6fT0oZQE6FxjVJDW7K5F_LS_pl0ezUfS9hMIdgBXZmHhEabU1a6NebCyYbFoEA43snvkLobEQlKCsxpNCizSlxhxqrw6ff_FTHXGNOT3YPjdZBkYIekW-n9n9Pcx5sqZQdMAPcSQdFJtdUD38WL_7xt-HfZqYf53UV-7ZWDgKy7WPOFWDfjQqaJGqxYD_5EcKY5xl5JfOaq4oRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو پایگاه هوایی و تاسیسات مهم باقی‌مانده در ناوگان پنجم نیروی دریایی آمریکا هدف قرار گرفتند
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی از هدف قرار گرفتن دو پایگاه هوایی آمریکا در کویت به نام‌های علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/656555" target="_blank">📅 11:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656554">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
جزئیات وام مسکن برای خانواده‌های دارای فرزند یا بدون فرزند
بانک مرکزی:
🔹
مبلغ قابل پرداخت تسهیلات به متقاضیان برای خانواده‌هایی که از سال ۱۳۹۹ به بعد صاحب دو فرزند شده یا می‌شوند، به هر خانواده به میزان ۴۰۰ میلیون تومان.
🔹
خانواده‌هایی که از سال ۱۳۹۹ به بعد صاحب یک فرزند شده یا می‌شوند ۳۳۰ میلیون تومان.
🔹
خانواده‌های دو نفره (زوج و زوجه) که تاریخ عقدشان از سال ۱۳۹۹ به بعد است ۲۱۰ میلیون تومان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/656554" target="_blank">📅 10:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656553">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-O5_mPBbaSV5mYri5fmx4YpzAyux4l0-cUDiuOEPHBL2Z728PkGtAI1tdZ5k4guFdkeQBzor3lE-pOYVfuI0BasxC7zq2ILZq0OYd0p1k3xhpWvGygyq5w0V535DXMDJ1_CzsKf5_y1j4ZhZhcl4NeFXvPZl0wy1fyCX42O_wMjaA6vWBQfXfsadla59VYB19oTM2Cqss1fvpH3B9PzhoAyv8RsDBEdNIN8NKK2ppic9Nnk8Go1F3wVsyAiF9vpz7AoSJ9XcE4ZeGt-wtjZU2-5NBDUYQMRJkYEYRKipsx4L5i86r5nxWbWKdLPGf150P1g1EPEEdXtNYYmp6djLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسوایی جدید در آمریکا؛ بازداشت ۸ ساعته مهاجم تیم ملی عراق در فرودگاه شیکاگو
🔹
ایمن حسین، مهاجم تیم ملی عراق، پس از ورود به فرودگاه آمریکا حدود ۸ ساعت در بازداشت موقت قرار گرفت و پس از بررسی‌های لازم اجازه خروج پیدا کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/656553" target="_blank">📅 10:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656552">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
درگیری مرزی در زابل؛ ۶ تروریست به هلاکت رسیدند
فرمانده مرزبانی:
🔹
یک تیم تروریستی که قصد نفوذ و حمله به مقرهای مرزبانی در هنگ مرزی زابل را داشت، با مرزبانان درگیر شد.
🔹
در این درگیری سنگین، ۶ عضو گروهک کشته شدند و ۲ قبضه کلت کمری به همراه مهمات از محل کشف و ضبط شد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
@akhbar_sob</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/656552" target="_blank">📅 10:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656551">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ln43OpHMZiU73JDteOW8OKRK1JSd5F5mjNWf1TGNYVesp3xDrUQgLnlCCvCSnvnHT3d2RlKjRjGRyZW5ETs9UTDKcyGwRRBSUjVVnULrr8wd0p-EcS99aBufSRCq30fJ-Fpeg_FwtfDYrm2dYnBrytI-d6Na2hoxBFnaNtfyIPWREq1BdWqJLhc4TB6Hc-QpPpd4OPxU2NUoidgY3g5ZUHjsauYQXjzKAYu1TjwR6s-ORxJED0MmFXxA4Gd04OUIF2wXtAc8ylLgy8ny6QRqRKeagW8mSDM7SzqbdU1jVHTWJMv0ntIw4EzKvurTUYsj1ha35eImW-yU-rW_kNJF8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش ۲۱ درصدی کرایه حمل‌ونقل عمومی جاده‌ای از ۱۶ خرداد ‌
🔹
بر اساس این ابلاغیه، نرخ‌های جدید شامل تمامی مسیر‌ها و ناوگان مسافری اعم از اتوبوس، میدل‌باس، مینی‌بوس، ون و سواری کرایه خواهد شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/656551" target="_blank">📅 10:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656550">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/844fd8ea2e.mp4?token=M2-FWl-4WyPTmnspDZG5EvDQm2bD-l-Q5OVcx0lrOX0i4RGTvlx-qsKm3TLwcwQeh3VLwObXymHZH1S9BAMiCioWWG1i1pKn-kOgicE20sDdA1z9Y2SD-tjEDc3oXwcFFiNaU8nEWe_EwVsIBHJlMTPrvwa8SrJFGqhLm400ZKs3vynfZVptzSZo7uCX0K2K2bdzqUsp1fX4HcZoCPpYXhPirO9kFIdO3Nw7uMCRWnCORU3YGv1DRygtZvMoAWYEOygzb7eC9LEo5mgq6A8IAVMeVtwPWFjtnoqyha6zExxiZKTxUrok-pvuf_CQKARy0z9UL9bkrLD6r4cPbhVKxIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/844fd8ea2e.mp4?token=M2-FWl-4WyPTmnspDZG5EvDQm2bD-l-Q5OVcx0lrOX0i4RGTvlx-qsKm3TLwcwQeh3VLwObXymHZH1S9BAMiCioWWG1i1pKn-kOgicE20sDdA1z9Y2SD-tjEDc3oXwcFFiNaU8nEWe_EwVsIBHJlMTPrvwa8SrJFGqhLm400ZKs3vynfZVptzSZo7uCX0K2K2bdzqUsp1fX4HcZoCPpYXhPirO9kFIdO3Nw7uMCRWnCORU3YGv1DRygtZvMoAWYEOygzb7eC9LEo5mgq6A8IAVMeVtwPWFjtnoqyha6zExxiZKTxUrok-pvuf_CQKARy0z9UL9bkrLD6r4cPbhVKxIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای سنتکام: اهدافی را در سیریک و قشم بمباران کردیم
🔹
فرماندهی مرکزی ارتش تروریستی آمریکا در غرب آسیا مدعی شد که به اهدافی در جزایر گوروک (سیریک) و قشم حمله کرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/656550" target="_blank">📅 10:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656548">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
قاسم الاعرجی: ادعای پرداخت هزینه از سوی عراق برای عبور از تنگه هرمز صحت ندارد
قاسم الاعرجی، مشاور امنیت ملی عراق:
🔹
ایران پیش‌تر اعلام کرده است که عراق از اقدامات مربوط به عبور از تنگه هرمز مستثنا شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/656548" target="_blank">📅 10:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656547">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0Q6-YZWJLptnzvME9mDlxtWtB2ds_dP2B1CyRm1QqHeczxbJBbw6j63E6cnMb-gz8GGUxD5L3P8UUq49LpGls0JXp_HvmPhKGknyMpABuhCLct1zT8YT5ocpeGCASFnSdqIm-CwVEvnuSWsfEupkWKNm0GxlP1MFr02GuXI2qRMJjJrBqJUioYg2hLjCltVu1Ru5oT78K8zJ1__1y3T5eUzLkS_-wlaEzPKq0wL5ucVZ7royI9QMQfgiQ9B4-1Hgeof8L8zkhLIOVpCWWENKLuMaGkOXOOhLtyNQ1b_gkQSVSls8l4zk98YcfpSoZKtGc_8ChvO7jKjSEkA0oGIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رابرت پیپ: ایران ویتنام ترامپ است
استاد دانشگاه شیکاگو و از تحلیلگران شناخته‌شده مسائل جنگ و امنیت:
🔹
ایران خواستار پیش‌پرداخت ۲۴ میلیارد دلاری است و بر تنگه هرمز تسلط دارد؛ آمریکا یا باید این مطالبات را بپذیرد یا تنش را تشدید کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/656547" target="_blank">📅 10:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656546">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_tZLuVAn3OaoRI6r9e99PamN0bhOsDyV1nUJUmKwZJa-qYXy0GGNKPJGaZrU16CbpLWlbnVKWilIbEoTaTridDuMhlKP7PWUb23gcl7HyOE2kynx-WNPvdw4_G8ZojjMobO8Qa8TTV6zZT7QqWdWUz7sremc_EahkBikcMo0iZ4jbEbwqVJjvURwhqV-_hfTu1UOnVSQN_PNCNspys26I3zGH_hDXeID19e3DL6r3zIWUpakP29pOzyl4jy5vhh3ODImmkD8y0oHYskAARIh7MlorYaUqM793tRlNIHmpNIdt4ZSUXfub6Gz3yvQ_Hy3LDklLPzdSuDbLvjDsh2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفر رئیس سنتکام به بحرین، قطر، کویت و اردن
‌
🔹
در حالی که پاسخ ایران به نقض آتش‌بس توسط آمریکا ادامه دارد، «برد کوپر» رئیس سنتکام با مقامات بحرین، قطر، کویت و اردن دیدار کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/656546" target="_blank">📅 10:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656545">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59c822300.mp4?token=aSbwnH06stMS59_8DQPSA_wFgrcZpXDHwHblQ-NJbav5JNosPKv_f-A8QVNiCP9l11SgfEN1Z0KAM3sjTAsMyLgilL_BooBr4VAEyTBodQKbOa3ofCPJ_sjFKtWHAAp1Ylrdnuc7R6QQ4a7z22DHxlvGpsr53m6sHhQOJhgV1eThpBg9hKGjHHPwSpCMlft2vHO7YGii6jsvkhZawJXqkQZuL15b9MT2tImH5vL7gwIxxDovmKVk64dfNrOoIZgnbsKjZlch8G0fh4nsIWgDDo3xEobpPUgBb3KpXlbhaJ6zaUVU1KIFewMEbebFPI4FQrqY70Bw9lLfDcZ-8kNHxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59c822300.mp4?token=aSbwnH06stMS59_8DQPSA_wFgrcZpXDHwHblQ-NJbav5JNosPKv_f-A8QVNiCP9l11SgfEN1Z0KAM3sjTAsMyLgilL_BooBr4VAEyTBodQKbOa3ofCPJ_sjFKtWHAAp1Ylrdnuc7R6QQ4a7z22DHxlvGpsr53m6sHhQOJhgV1eThpBg9hKGjHHPwSpCMlft2vHO7YGii6jsvkhZawJXqkQZuL15b9MT2tImH5vL7gwIxxDovmKVk64dfNrOoIZgnbsKjZlch8G0fh4nsIWgDDo3xEobpPUgBb3KpXlbhaJ6zaUVU1KIFewMEbebFPI4FQrqY70Bw9lLfDcZ-8kNHxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دخالت والدین در دعوای بچه‌ها چطور باید باشه؟
👩🏻‍⚖️
#سلامت_روان
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/656545" target="_blank">📅 10:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656544">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHI4wiqBWwR6EiGP9-sXHvXl9eE4tbVaHP6PZzRxXsEUJ_iZ0IblnW4xxeDwwTObyfO3YfIoG4PMtc9YpkogGi96ZzCXmBvsBLaAS5pw8s6bgrsKp7AIZeoFB8V-G4zfkoAysbgVEHseTwMmOe3Z2REky6DKzFoKFeykCwCiovkTqCwmF4e56iFhwv_RPbPUkEpe3p7EN995iUh8KUbH-MqwgPXTtzFNqkJwrVXUiFfjsgrG0BbShvEgR6RRW4p_JFtEWufZ3I-Tkmml2APk3PupaV98JrydClBL-NPiufqJPEC1x43rerrRi4khfqpOGJ5O-231xGQ26b2qiJZOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir
نوشهر
📍
۱۰۰۰ متر زمین
۳۰۰ متر بنا
تعداد خواب ۴
ویلاباغ مشجر و سرسبز
فول فرنیش وسایل برند
چشم انداز ابدی جنگل
سند تکبرگ و مجوز ساخت
دسترسی عالی تا مراکز تفریحی
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/656544" target="_blank">📅 10:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656543">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
دولت عراق: سپتامبر ۲۰۲۶ زمان پایان حضور «ائتلاف بین‌المللی» در کشور ما خواهد بود
🔹
«ائتلاف بین‌المللی» نیروهای چند کشور به رهبری آمریکا برای مقابله با داعش است؛ با پایان حضور آن در سپتامبر ۲۰۲۶، مسئولیت امنیت عراق به دولت این کشور واگذار می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/656543" target="_blank">📅 09:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656542">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rr63TPJ2W5j4U-uneu42KgpvJp3P2MWbYguYo55n2Qe2zKwS5TlKjPzxHQWgL1sL39_HIzBgEpQQliy1PpWe14Y18w4KhFy6LcehXJSjAx1rC4VZvCKiniOfAliX9HBz0Tb8JzcobR16mlk53MueCmw3t0yOlmlzwWkJENfgnAApP--bRFln2IRRVe7wy93m66Lw1zIqggbHdoqNY4l09z83sy6BsJAOoeuJL5P-cd1iWZF983t8lO1q7CFzoKIr-chDIEw4Eau3o9C_uyppRSk_NtewljnC9KYOQu-U6I864oB9cibIM1wTj5vJTpBlWfICWabjGVl-XL3n-tGaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی، مشاور رهبر انقلاب در امور بین‌الملل: معماری جدید هندسه قدرت برپایه تضعیف مقاومت قهرمان شکل نخواهد گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/656542" target="_blank">📅 09:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656541">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4853bdc25.mp4?token=bXXuZM2PO260yeWqCGqT545jKqJM71dL9DBVpFi1H1fM79Xog8erU7y6VBpXzUnpL1g9rnCnDSXUk7UqMxWpoLgmT7Z-lVHBPyBOTdxRU3ya0m-TirfG5HD8tc_4aKLzqAY69sqzvwDQQ_jgA-Ui83KuRMkquTRjUSqoMtbV9yUjqvbh9K6nVuZLF2_Xr-X3S9V-J-LVefjJxMmYu5NllnQpM8O83GVdqeohKTIXHVbHURGsFkBX2yzcCAcZx2WngQjaePq31ix2-zuldcpv3D0X_tvuqaNYiLUf23EtLg_P9HxEwE22lPL0XloSev74atv29pmtmOhb6MvjA0UksQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4853bdc25.mp4?token=bXXuZM2PO260yeWqCGqT545jKqJM71dL9DBVpFi1H1fM79Xog8erU7y6VBpXzUnpL1g9rnCnDSXUk7UqMxWpoLgmT7Z-lVHBPyBOTdxRU3ya0m-TirfG5HD8tc_4aKLzqAY69sqzvwDQQ_jgA-Ui83KuRMkquTRjUSqoMtbV9yUjqvbh9K6nVuZLF2_Xr-X3S9V-J-LVefjJxMmYu5NllnQpM8O83GVdqeohKTIXHVbHURGsFkBX2yzcCAcZx2WngQjaePq31ix2-zuldcpv3D0X_tvuqaNYiLUf23EtLg_P9HxEwE22lPL0XloSev74atv29pmtmOhb6MvjA0UksQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر کمتردیده شده از لحظه آماده سازی و پرتاب موشک‌های ایرانی به سمت سرزمین‌های اشغالی در روز اول جنگ ۱۲ روزه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/656541" target="_blank">📅 09:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656540">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ویدیوی زیبای نایکی در آستانه جام جهانی با حضور فوق ستاره‌های دنیای فوتبال
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/656540" target="_blank">📅 09:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656539">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
روابط عمومی سپاه: در بوشهر، شنبه ۱۶ خرداد از ساعت ۹ تا ۱۱ صبح عملیات خنثی‌سازی بمب‌های عمل‌نکرده انجام می‌شود و احتمال شنیدن صدای انفجار وجود دارد اما جای نگرانی نیست
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/656539" target="_blank">📅 09:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656538">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
آموزش ‌و پروش: امتحانات نهایی پایه‌های ۱۱ و ۱۲ احتمالاً از ۱۳ تیر برگزار می‌شود و اجرای آن منوط به تأیید مراجع ذی‌صلاح است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/656538" target="_blank">📅 09:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656537">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
روزنامه اطلاعات: به تیم دیپلماسی اعتماد کنیم؛ آنها هیچ تصمیمی برخلاف نظر رهبری نمی‌گیرند
🔹
ملت ایران با وجود دشواری‌ها پای مقاومت ایستاده است.
🔹
در صورت توافق، ایران و ملت ایران برنده خواهند بود.
🔹
حفظ انسجام ملی و کمک به دولت ضروری است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/656537" target="_blank">📅 09:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656534">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IoyZqweEq1QaFt3yZ7wSr3XtdXxZF2QSCjypW7NXC_HVj-Jb5GaS6AmJBdHWZhbvBAmutYztk3V8BEAXyjVoS5QlK1fuRmmNbbZzzd2ee1K_HkJhlSFmxVTKSfauBupV3kZNfWvYeSjDUJYvkA0F1x_y8WW1-efMdnNdsSJVmNIzBiNs93aH9uhQU3Him5WXLLW0RHmr5QHxHpJSuml1pQnrVVLguPYBC_TFlMxqangu8Ue7ZudbF9BfYzoCP2xHayl8jcB-Gba2H7988l61odzQPXlEXt3ZrV0nO_3AheFbrqtUUB7-LXQFBxbu3IJQaDP4D1FBL7CKhyYqiGMOrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JS6HYhK4CFjZjFjVakVpM_0rKsH5LXAfStdan5bDH882TQElAgslLh3Ib8ETIkj6U42QBUK5NRpPNpgrt1EW6fw3TvchMGqxsfLCzMdvBEKjF-DaytSnFzyM7lb6eJ4a50A0IH3hFeoVsxEZVoJcDTZCQ_2M23JMZY9r2umhylgwRVApjDvQHWGC-ceLCbHg2bUhldUwu5yMp-drtdQ_QkNltRciRdb84i60TcJsuzXdyWaKwqGTMrMhcd3GaAkOLpao-fOR-T16PPukKyXkpju9eYUnOyg_7E_dEAVRU2Ll9hGo4GDtz5Qwa5dNE9gnVm3GHasZe_uEWXBRwYriEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sH5itBds6CTF6PhMe2XZL2WFm-MEnHks5RdIfdwt2bQlNIn5RzxoQLKPryYbJ4fpfELr38XlAxXl2015uTPTQfTndE2S_h6MzswJeFDPyB6ZkTGeVMpJRRKWR0jVCAnDIcWJCyTzgl22ZtveTQdAKX1EyY3VksE15l6csNYoZQBliJu9XDqePDgIjYQwSkXLP8pRpSSmdi_KTZ9uvU5sYki6gpRn5n8QLKcXnfAOnApo6odTVcWdqZkB330RyjRcfQvo-RBo4uSRmmYqiMPfQqJH3YD7B0bdhSbJFcG_-K3S9VpSX6wT7-4HRZ76tjN1fUxRwPXayyKH7LEtI6TKOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اقامت لاکچری خانواده نیمار در آمریکا برای جام جهانی!
🔹
برونا بیانکاردی، همسر نیمار، برای دوران جام جهانی یک عمارت لوکس در اورلاندو با اجاره ماهانه ۱۲۰ هزار دلار اجاره کرده است. این خانه ۱۳ اتاق خواب، ۱۵ حمام، ۲ استخر، ۳ سالن ورزشی و ۲ سالن سینما دارد و میزبان خانواده او در طول مسابقات خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/656534" target="_blank">📅 09:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656533">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6399af70b.mp4?token=pAR2-c6uegra-i0qDYZlj24e0o5O_seWDRp1GBMaIZR-Gq2Pk81NENVCArlkoVrWq_630i-f_71975n8mkQf8BvxYQ4W2sa9l-61efxL0O1zzpMIZkfrhdNiFMm9u0lgrHKFOCsJ31xshSbiVGZJyUF2yI02-2UsqylQI-aBvLVQFuqngSZ-qa2QG2tujVSfrepHRxEefwT2zP40cAVfOM7fAOBqrP7WoP8CB100ADltfMEdyqBQL0w3WlxGZtGmHNh030e6DpbEVGpvmuWvyjidL7eST-HXnfSllxlxbqH6sx8kofEQ6Q2wAzSVnFWCsAOz1s5wv53z4nbP6sgcFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6399af70b.mp4?token=pAR2-c6uegra-i0qDYZlj24e0o5O_seWDRp1GBMaIZR-Gq2Pk81NENVCArlkoVrWq_630i-f_71975n8mkQf8BvxYQ4W2sa9l-61efxL0O1zzpMIZkfrhdNiFMm9u0lgrHKFOCsJ31xshSbiVGZJyUF2yI02-2UsqylQI-aBvLVQFuqngSZ-qa2QG2tujVSfrepHRxEefwT2zP40cAVfOM7fAOBqrP7WoP8CB100ADltfMEdyqBQL0w3WlxGZtGmHNh030e6DpbEVGpvmuWvyjidL7eST-HXnfSllxlxbqH6sx8kofEQ6Q2wAzSVnFWCsAOz1s5wv53z4nbP6sgcFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقتصاد دان آمریکایی:بحران تورم مهارناپذیر ناشی از جنگ با ایران تا مدت ها از بین نمیرود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/656533" target="_blank">📅 09:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656532">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ویزای تاج و بیش از ۱۲ نفر از کادر رد شد
🔹
بیش از ۱۲ نفر از اعضای کادر پشتیبانی (از جمله مربیان، آنالیزورها، پزشکان و فیزیوتراپ‌ها) و همچنین مقامات فدراسیون فوتبال ایران که قرار بود تیم را همراهی کنند، ویزایشان رد شده‌ است./ ایسنا  #جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/656532" target="_blank">📅 09:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656531">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای سنتکام: اهدافی را در سیریک و قشم بمباران کردیم
🔹
فرماندهی مرکزی ارتش تروریستی آمریکا در غرب آسیا مدعی شد که به اهدافی در جزایر گوروک (سیریک) و قشم حمله کرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/656531" target="_blank">📅 08:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656530">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc5589b7c.mp4?token=cTy0Dt90f1MqK8Y15kZ9cDZ7_MMDLfpK-UXU4I7kOpA2iN9xSZDMcDq6kZXb5iEKvGprRjO2bEESZQSJ-KoDiHu49963MHyMsK5td4u_yOwFz3NS_QJ6gcMh5vrRfuGRTuNjOkR0CZpHP0xXION4XSHRXWGV5yW6aIy1zMdtzfPt6ukjdrZ_YJOVBsd_bp7aw0O_9HUKGERhNUTk2xqBarm7Fjns2S3pY_qZ_smYGLD19n88gHQKyn-atNXr3M8FcFQ3PKquRyOEzmJH7O6NINrTcKZtdM40loX6TPjt0hvf3iNLKs2l6JVtoYYGn9M_O5gJTbNuM_CDr_u1gGzE2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc5589b7c.mp4?token=cTy0Dt90f1MqK8Y15kZ9cDZ7_MMDLfpK-UXU4I7kOpA2iN9xSZDMcDq6kZXb5iEKvGprRjO2bEESZQSJ-KoDiHu49963MHyMsK5td4u_yOwFz3NS_QJ6gcMh5vrRfuGRTuNjOkR0CZpHP0xXION4XSHRXWGV5yW6aIy1zMdtzfPt6ukjdrZ_YJOVBsd_bp7aw0O_9HUKGERhNUTk2xqBarm7Fjns2S3pY_qZ_smYGLD19n88gHQKyn-atNXr3M8FcFQ3PKquRyOEzmJH7O6NINrTcKZtdM40loX6TPjt0hvf3iNLKs2l6JVtoYYGn9M_O5gJTbNuM_CDr_u1gGzE2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تایم لپس بی‌نظیر مقارنه سایه دماوند و ماه
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/656530" target="_blank">📅 08:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656529">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
هزینه سنگین شکست‌های پهپادی
،
میلیاردها دلار در آسمان ایران دود شد
رسانه The War Zone:
🔹
نیروی هوایی آمریکا پس از از دست دادن شمار زیادی از پهپادهای MQ-9 در ایران و یمن، برای جبران خسارت‌ها به دنبال خرید تمام موجودی باقی‌مانده این پهپادهاست.
🔹
ارزش پهپادهای سرنگون‌شده حدود یک میلیارد دلار برآورد شده و این ناکامی‌ها حتی بحث بازگشت پهپادهای قدیمی‌تر به چرخه عملیاتی را مطرح کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/656529" target="_blank">📅 08:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656519">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYczFDe9id-IfiykO69lqcwFJfPBGxccxW9O0YbdRaD8feXOTe9U6It7sZYYpvSvHmpGE3z_jIGTsGC42tdWe_VscZASsLAebKtnBdHiwdSdvH54KcwYaZk5MHues_PxSKVTT3A8pEASVAJWbRQPlhMa8DrQS5KDZZwS9tZpHWQGlvFSNINX9mJhIm1NoM40pLmxy8dYgO9BJx2LuFk5R_rWAk4r9VjMrQrJmQ3UZgGGJkUOE5IqiXnFIflGLCnxFIaDUr_9_t6bdOkTma_APMoJrqnLB6TzUTCzGXbAV4E7eUlSqozeUcQu2yRTl1_mYL92_3VPZ_Kche4F7-uB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAyMFiwMv5p6Zh7gYcx210Fv0dCV7bXK9pcjGd7WTBIL01C_JgR6eaFEco0ZVmFcOPUayCJgjT_YdoSCwMfsWQrbuECBH7yOf0NRPEeuKK73pdYxSM1x0zwMMctR6Sr0hj9-vM9srt6ze5PPVFdhFQ2EXRRWuAv_Lbq4URirOwpvOUylqRBRKhG3R3-AubGqtbSn5_wN2u_qmkf4RJfJiwDYYa2maTLqF6SZivftf_9oOSsURpm6wlynBXE-86ia3cRryQgAVS7ZTXGdUwjUJujna2E3CW76zRFoqAeo1nC3Qpsyj_h1MGoG5LI6Vz3RIrxDzq3wCQZOUhf4V57rwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XPbKnuiS2tFox3fHn_X1TitXlqj6FcU8zAPuXV4-l2fd8gkogubP1XM_lP4lWlMJEP6EdOuEgmko63GkVQn79GBXx3viUwHCOL7XvU8VchZKUgEo4YvcrWUArPl67h78NktDUays8y-qg6BT-nzzxZW6exo2_XELQGmH8O4FbDIUEuSKaJ6h94i6GI_uFGKM7hgeB9FO5YatKf6jeExwpGWNPVF35fo7buc8vJZCAOCkWNFSsW9eQSajZioX8JXeSooPo_21rQYgWRngQWuBrDjMWwdz1WWBZAqWI1RD06VttUman14-BkpUKMerv1tOWx5S6KvQBGYUa_PQylayTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VeXCMWDiX3_fLu9O1kOYOyoxaJlkgUuXXd-QrJWKgKCq4lhSKLfUiPoFS-UCNqQzc47eWWXy1LnOA2hYZUdyGSqTEJS3tj9TtpgbL6AL6NhSXvMVkPKdbbM-v-EOe2r2XcPWY4HjZB9ZYRnpl66W4IJW0G0ibYy85eH3135TR4_D4Z-CPQhlA0jsloAuSEY2nYWiC_q44xVJbabZLHBd0O867ckp1gOvFS2a3tBJrgTKNIIN4i3zh0aHCtJZ_MfssbuxUrYchke2YxzO0U0oLc8hzx5SoO7CQUQmB8BQfMXHHz2YgTmgjx1FWCw6Ih0G5LCcjnFAXdaEeNP1LpVMvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFj5taHyTwyod18uLs2zDFQf1lS39vta92xwDmK6PCilZChghkuQDZ_WAtu1BA0mJHgfKFtLUtdL4r5sfU4Ar3BvASKm92tNoGGKCIekeq_oFDZn2x48AUXbsXGdJLRqkd4T4gOnSWd5a7jYyFdHajo2_oF01aU7f6fSXkafiHo9539c7wdIsHeCb-nX3PF09X-BiU9HQnBCQ8OHs-bqbcVT3ALCmdRWD0YkJIZG1OyATzYw0mFojQ_grQ1aWfh6OTGFXcvp9tf_Ks_kumf2QcR2YmFTZ32wKyJZwAci6UbzWGWdsmxnKwnNG7sBnsFPKk5F0xHIDxi8TbJXK0FLdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rEaISgXevrYvwpKAl7U2sW82whGGoNJKkD4ZrJamVZb6munC7TNBt74tIrNDVy83p4X8jrEzWutunFHvZg1dALBBO5Sn6e2_kDWfEZUV3gaZvyReJiS4Jn7Bmv__wDgxX9HH7SjnlMl4_H40NQRh6XwExKO-h7UtmD6SRvTsAO9KhnReKWU1HrqEj72im1s4XRQStiUS7Au-CzgWYRy_6kNmE6V9GiuJHeIc0soN2M12-aCw-dE7j-kknvIt_6i2iFiuWkx-0L8QiR41Pz9178K0sNW4RHWVK8oblHgPGupzmI26ur4rGguPDlDa0K4G8XZs6nA9jEFScetMtJxysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LA2QqrKHS1Y-guD_lQChjbjouFhSNRWv0RXo8RJg2GHn2AAQ2c9ZVEwWE9TFJUmQkKwgGqV5U1hXdlYpmqvPKHWBr_7XaACHG0piK8nnzEvFjWWnMhMoivRWBFKX3dNerGtgPTsJyCGql-xU3-8bq6ri2V-XEye6QimvBzqAb9sX5TVvGxTssFlOIs-uWoloA2obS2fXDZP98F3wcV6XcMxtAWOp3uysGzR0vzYoETETm_k_xgmJSjkQf2kJkeP6A-0qlms_hisxtUISuiSAzDSHu-KdSX9qr-Vtx5nXTDLjv0LcMAndxHy1d1n0wM8yQqpZeNeTi4Zq-MMfAOZrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2YcHPtCbY6Pk8K8FWWeM-szqP7Fo4ZszouQT-kizRqqY6XI63eTRikRWVMMNV1F2EF_CXddxz7ml1JdRGK52mdI9Lh1l2Ber2BnO46MH2_Risx_Jte9YYPdCu2URSA-F50qcAcTKLXA6PXM2QMn8ztYWFs5EtWlFXgr_tb2iw0g1et8urX3Bs5L-jOiE_2RrcgJ_LU_G8tsK66uSm8wM_bBRI41G0lsc5CAulbl-axqRTnivGNTLeKBEfEdQgeNXtQ5ks7M9vE5D0oTNHhWTg7s8O23Yam5TSsP-aIGgSs7kvVAIvxil2tAb-WJmdN-UfUF0HVri2nuiBsArQhQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNSMJdV5-NUajf3yHKfYEEDcVLDvvkZYZHc0Mj7Xar627Jxv4_02vLzH_9539ZnLZw4JmlWlrIXEHbsK8eycWqQe_XcF2r8MMVE5zwA27BuOCfvOIvi0vB-sxVk--nbGb-IfI3ArNdNuPrzZsVKhG2LEaScO5BgHitnQaRbGeatlYzB7AWf5gVGdDauQTUwSMt4RM-w7MA-gCs82JvFr0PxCtEw6Qx4oP86FUi_1LZcFh534aMz5jrnSuuEFJKlUpphZbWZAw12yUNggkee3M5mwOZoUR9cn0DK4fOqafb5cbQIVKwG8lp7hjoORJmS_sV1uSY1QW1BxZynPXpmpiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itMW38D6rrfYOyEHzKnKha3Ei-dDfs2mYzZ6rpu3rSfolUWyd5UffIxewa7-G0q2kBkHB8o6SJUJ89ZhZ5BHs6bbo1_GMImqsCbft_4ekPnf80N6kn1mhO99TT6dLm0bxEjvS7wn2VBfyksNnHuWLnWxDPGz1DMQRQqgRD10j_XBPnLCkcBQO93ceks_qoF58xLQJSIDggaa2s2UexJAoLifh_R6ne2OKqazeExrJv2y2v1a9mvm_Fh2wIXPc9Y4t0ewfSoSgTjsBuEs8aLeJHIyZkdyWOBUoyDpXgh3wy-pKBS-cZ_-dGa9cV2yVgyJtOp-AtHZ4oFwIE0nAyoWBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جشنواره آدم‌ برفی
🔹
جشنواره سالانه آدم‌برفی، پنج‌شنبه ۱۵ خرداد۱۴۰۵ در ایستگاه ۷ پیست بین‌المللی اسکی توچال تهران برگزار شد.
♦️
عکاس: بهنام توفیقی
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/656519" target="_blank">📅 08:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656518">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پیش‌فروش بلیط قطارهای مسافری نیمه دوم خرداد آغاز شد.
🔹
اولیانوف، نماینده روسیه: سکوی غرب، حملات به تاسیسات هسته ای را عادی سازی کرده است.
🔹
مایکروسافت ارائه برخی خدمات به ارتش اسرائیل را متوقف کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/656518" target="_blank">📅 08:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656517">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
شکاف در روابط واشنگتن–تل‌آویو؛ پنتاگون از تهدید جاسوسی اسرائیل خبر داد
شبکه ان‌بی‌سی به نقل از منابع آمریکایی:
🔹
پنتاگون سطح تهدید جاسوسی رژیم صهیونیستی علیه آمریکا را به بالاترین درجه افزایش داده است.
🔹
نگرانی‌هایی در پنتاگون درباره تلاش‌های اسرائیل برای رصد و زیر نظر گرفتن مقامات ارشد آمریکایی وجود دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/656517" target="_blank">📅 08:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656516">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75414e6eb6.mp4?token=UtkJyNTMbUEzZBvPpIMeYoBSQ-RBVO1HuA2PRjRpXYBEs_iH9LT_myOBU0wGoJevCaLAe3E_om6fl0eYJgKEzMSSCXi3KIOK4CURpCNNqHAJi-tlwtKMtOmqtr2oTYc7kdT-Gif3autzXyWyx_7sAMjyBjV1Kso0GcaDPkZpHjfnmKpJyss8-FbMBP5vBh33zDDP78xOz4jWM5NqaIC8kEa0jgGfMWaqv3yEe6Xg2shTZwpsfIGZNR1Jah0_FhJc_-BfuxwfwbquPTIOKGpOsMMhII8wf1WB3o_tGt2MhzedjSF-zjzK4ZCT1tQp4TGPKbGsgbxZ3UPRXIolAttnBjP7Llx-KfzmQtufUbShVj00vXwH04oBOkBAWPo6BbxD2R6plDDrVrdsg7M8QLAq6sTUhF9JFeVkvBlHP5xNtBpzsTS22wW9FQb8iHme0FyTee723SCx7zWt1Me0FLEKfwOcX2xuD0OmBc1OcW4eNYfKE9kKu0kKlHF07kQV0_Jjw53VGegNkmLUBSzcvF7foBnKV5kUtqGvOlgYqKcl3N7VE1a3u9vxh-c6wRzvx6z_sUx4j3k6Pl4GhKs_ZvPgqxmDgk_2XY--ITCFvyJOVv-hYs_0E9lLbWQ8JmfDTqWqmB4e7UhPuJwC2s2yiO0kqFgdeBPhkjGEhelhrSZd_Hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75414e6eb6.mp4?token=UtkJyNTMbUEzZBvPpIMeYoBSQ-RBVO1HuA2PRjRpXYBEs_iH9LT_myOBU0wGoJevCaLAe3E_om6fl0eYJgKEzMSSCXi3KIOK4CURpCNNqHAJi-tlwtKMtOmqtr2oTYc7kdT-Gif3autzXyWyx_7sAMjyBjV1Kso0GcaDPkZpHjfnmKpJyss8-FbMBP5vBh33zDDP78xOz4jWM5NqaIC8kEa0jgGfMWaqv3yEe6Xg2shTZwpsfIGZNR1Jah0_FhJc_-BfuxwfwbquPTIOKGpOsMMhII8wf1WB3o_tGt2MhzedjSF-zjzK4ZCT1tQp4TGPKbGsgbxZ3UPRXIolAttnBjP7Llx-KfzmQtufUbShVj00vXwH04oBOkBAWPo6BbxD2R6plDDrVrdsg7M8QLAq6sTUhF9JFeVkvBlHP5xNtBpzsTS22wW9FQb8iHme0FyTee723SCx7zWt1Me0FLEKfwOcX2xuD0OmBc1OcW4eNYfKE9kKu0kKlHF07kQV0_Jjw53VGegNkmLUBSzcvF7foBnKV5kUtqGvOlgYqKcl3N7VE1a3u9vxh-c6wRzvx6z_sUx4j3k6Pl4GhKs_ZvPgqxmDgk_2XY--ITCFvyJOVv-hYs_0E9lLbWQ8JmfDTqWqmB4e7UhPuJwC2s2yiO0kqFgdeBPhkjGEhelhrSZd_Hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت اسکوات با کش ‌
🔹
تعداد ست و تکرار: ۴ ست با ۱۰ یا ۱۵ تکرار ‌#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/656516" target="_blank">📅 08:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656515">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
فوق‌العاده خاص پرستاری در انتظار اقدام وزارت بهداشت/ پیگیری کاهش ساعت کاری پرستاران
‌
رئیس‌کل سازمان نظام پرستاری:
🔹
موافقت اولیه برای لحاظ‌ شدن تا ۲۵ هزار امتیاز فوق‌العاده خاص پرستاران اعلام شده‌ است.
🔹
موضوع کاهش ساعات کاری پرستاران را پیگیری می‌کنیم؛ کارکنان اداری نظام سلامت در مقایسه با پرستاران حدود ۵۰ ساعت کمتر کار می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/656515" target="_blank">📅 08:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656514">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btUPP-62QE26B57dBPwZuQkii1__mGz0DJLVNXgrdzy527wdaWpx95TOAn5GnEJTrJfCheqAf0Z924C75tS3g2hGwxkU5L5lvt8kUL5rIRMeh50ZMlOedzkPZxLe478NbO-XmAzWqyjgLApDG5EAZSEeMIH0Ba6-tev8wfCFen2it9BxBcYVXKtTsbu5ddPHf7LEQhyYks3vEbWQtQRCB3FJCiisw0r-ROmLiBDq6J-GQITOCkLWR2e_Wtu1HTAWssr7C3d4-l2D_ht0iT_1o3MuOO-GpCWtgtBLeW31O-7EMeZihzKedyiw8Jroc12NGzyZ9nr9nfMpZfb1WdwqdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار مجدد وزرای کشور پاکستان و ایران
محسن نقوی، وزیر کشور پاکستان  در شبکه ایکس:
🔹
بار دیگر با برادر عزیزم، جناب اسکندر مؤمنی، وزیر کشور ایران، دیدار کردم. ما تحولات جاری وضعیت امنیتی منطقه را مرور کردیم و درباره مسائل مورد علاقه متقابل به بحث و تبادل نظر پرداختیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/656514" target="_blank">📅 08:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656513">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ادعای عجیب تلویزیون الجزیره: ۱۵ نفر از اعضای تیم ملی ایران ویزا نگرفتند!
🔹
هر چند هنوز مشخص نیست که این افراد شامل کدام اعضای تیم ملی هستند اما این خبر در حالی منتشر شده که شنیده می‌شود ویزای همه بازیکنان تیم ملی صادر شده است.
🔹
برخی رسانه‌ها مدعی شدند، آمریکا…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/656513" target="_blank">📅 08:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656512">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
موشک‌های ایران مغز متفکر هوایی آمریکا در منطقه را از کار انداخت
‌
مقام ارشد آمریکایی:
🔹
یک مرکز فرماندهی هوایی مهم این کشور در جریان جنگ اخیر به شدت بر اثر اصابت موشک‌های ایران آسیب دیده است.
🔹
این مرکز بیش از ۲۰ سال است به‌عنوان «مغزمتفکر» و مرکز فرماندهی تمام عملیات‌های هوایی آمریکا در خاورمیانه شناخته می‌شود./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/656512" target="_blank">📅 07:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656511">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9a05f5b0.mp4?token=BidfNeoRMs5JcEWrPeFzha2PrPIfbTUxbO-wDZDXu_wLzN1xcDE9NgfzH_JRhgU-gOL0Gt19RHYvaiHo1HQNJDW5Hmu6s3okxL3NoAVkQ6SFAfnpCidPRmwo4Trj7hPySq_EUrCH368ON1xmrjuBpd8v7bnJ_fsC8YFzH-_mdyN-pQuYN747zLBQXqmHnLuIAbAV9ew9u1iEXIG1tqUbKeRKIQYfjBMD0MTtvrsPEtff-7Op3UXZPaaw9OXgu527Fk7YDgffFo4iBri21tKEFWTx0464HaYDIfv_-ZRC_Fx2H3vCou-WEK3YXlCHEiBErgcHakwXPOFNZasWhzabWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9a05f5b0.mp4?token=BidfNeoRMs5JcEWrPeFzha2PrPIfbTUxbO-wDZDXu_wLzN1xcDE9NgfzH_JRhgU-gOL0Gt19RHYvaiHo1HQNJDW5Hmu6s3okxL3NoAVkQ6SFAfnpCidPRmwo4Trj7hPySq_EUrCH368ON1xmrjuBpd8v7bnJ_fsC8YFzH-_mdyN-pQuYN747zLBQXqmHnLuIAbAV9ew9u1iEXIG1tqUbKeRKIQYfjBMD0MTtvrsPEtff-7Op3UXZPaaw9OXgu527Fk7YDgffFo4iBri21tKEFWTx0464HaYDIfv_-ZRC_Fx2H3vCou-WEK3YXlCHEiBErgcHakwXPOFNZasWhzabWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
♦️
آمریکا هنوز به برخی از اعضای فنی و اجرایی تیم ملی ایران ویزا نداده
🔹
ویزای برخی اعضای کادر فنی و اجرایی تیم ملی هنوز صادر نشده و سفارت آمریکا تاکنون از صدور آن خودداری کرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/656511" target="_blank">📅 07:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656510">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
چه کسی برق مردم را می‌دزدد؟
🔹
حدود ۱۰٪ برق تولیدی کشور هدر می‌رود و بخشی از مصرف نیز به‌صورت غیرمجاز انجام می‌شود.
🔹
مقابله با برق‌دزدی برای حفظ حقوق عمومی ضروری است و جمع‌آوری هر ماینر می‌تواند به تأمین برق ۱۲ خانه مسکونی کمک کند./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/656510" target="_blank">📅 07:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656509">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
تکلیف هزینه‌های خوابگاه پس از تعطیلی دانشگاه‌ها مشخص شد/محاسبه «روزشمار» هزینه‌خوابگاه‌ها
معاون دانشجویی صندوق رفاه:
🔹
وجه پرداختی دانشجویانی که از خوابگاه استفاده نکرده‌اند به آنها مسترد می‌شود.
🔹
برای دانشجویان حاضر در خوابگاه نیز مدل محاسبه روزشمار در حال بررسی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/656509" target="_blank">📅 07:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656508">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amX4oGyEFC1XZ83aMOzztaHJ1lhlbwFacypExJGYXy1zLQlsaW1QkUnO878gXU0cmqGO7DFC2YyliMYBEKoHQKF2bGjDpg9nLKOw2FBxlXx63P2Ibafzn4qsEwbIJZIMJfhLAZKjjCTeFP-J6ELBm3ej41irEmLL1ZhcYsEMT3kbezvjVhCOc5Qg3r-pguaN3pQYnhzNEe-CgH9oi7PlRhJtBwgBHxftFoffDKzuAikxgHr5GVeQ2Og61pwHLXtZGNCrrgl5_lP_ChuJxnKDjJ5Obk3sK9LYHQfW2WQYm114H-Val7drHSEDI3jhdeRRPBHIRBvIGl5T2k2qydqLkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو پایگاه هوایی و تاسیسات مهم باقی‌مانده در ناوگان پنجم نیروی دریایی آمریکا هدف قرار گرفتند
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی از هدف قرار گرفتن دو پایگاه هوایی آمریکا در کویت به نام‌های علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/656508" target="_blank">📅 07:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656507">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ادعای سنتکام: اهدافی را در سیریک و قشم بمباران کردیم
🔹
فرماندهی مرکزی ارتش تروریستی آمریکا در غرب آسیا مدعی شد که به اهدافی در جزایر گوروک (سیریک) و قشم حمله کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/656507" target="_blank">📅 07:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656505">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b87e64f79.mp4?token=u1zSUYYSTMMWuaNGI6PfyPsuMi5_MZwZNQ7xjJ0j3-4-JOYSFLAstmF2tP8r8jE4XKhwyPWOXZqWlUvaV8SqWkVbEZn-vqTTFjeNC7A5D71xy2Wq6DPU1E1GFc8vBeW4n989xYLd7kehF_f7ZEwuoXTrw6p0HnEkmG6MNgqQaxlI_bODZUa5t2w4RoRXHolnStYmJ7LmWu07R0uaK6W5QEfoQ5vwPRxnHUkgQ_BIYGwJW1P6HyIKV-1WwL0Cr38yR4Xc7aCCv83RND0zXZxKrqEdUTqrFcCquAfTZxsGY7biXs9JcxTpTaZned80hPHbqnxvQ0hbsFEeEmTAxvSj2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b87e64f79.mp4?token=u1zSUYYSTMMWuaNGI6PfyPsuMi5_MZwZNQ7xjJ0j3-4-JOYSFLAstmF2tP8r8jE4XKhwyPWOXZqWlUvaV8SqWkVbEZn-vqTTFjeNC7A5D71xy2Wq6DPU1E1GFc8vBeW4n989xYLd7kehF_f7ZEwuoXTrw6p0HnEkmG6MNgqQaxlI_bODZUa5t2w4RoRXHolnStYmJ7LmWu07R0uaK6W5QEfoQ5vwPRxnHUkgQ_BIYGwJW1P6HyIKV-1WwL0Cr38yR4Xc7aCCv83RND0zXZxKrqEdUTqrFcCquAfTZxsGY7biXs9JcxTpTaZned80hPHbqnxvQ0hbsFEeEmTAxvSj2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوهای منتشر شده از فعالیت سامانه‌های دفاع هوایی بحرین و کویت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/656505" target="_blank">📅 07:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656504">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
دو پایگاه هوایی و تاسیسات مهم باقی‌مانده در ناوگان پنجم نیروی دریایی آمریکا هدف قرار گرفتند
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی از هدف قرار گرفتن دو پایگاه هوایی آمریکا در کویت به نام‌های علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/656504" target="_blank">📅 07:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656503">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای ترامپ: اوضاع با ایران خوب پیش می‌رود
🔹
«دونالد ترامپ»، رئیس جمهور تروریست آمریکا در پاسخ به سؤال یک خبرنگار از او درباره آخرین وضعیت مذاکرات با ایران، مدعی شد که اوضاع با ایران نسبتا خوب پیش می‌رود #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/656503" target="_blank">📅 07:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656502">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سگ زرد: در حال بررسی ارسال سلاح به تایوان هستیم  رئیس‌جمهور آمریکا:
🔹
در حال بررسی امکان ارسال بسته تسلیحاتی  ۱۴ میلیارد دلاری به تایوان هستیم.
🔹
هنوز درباره ارسال کردن یا نکردن این بسته تسلیحاتی به تایوان تصمیم نگرفته‌ایم. #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/656502" target="_blank">📅 07:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656501">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEROSZ9l-uiWp9nKcIugrGOx45KhGZlFuRJyJgmltsP3mYIiX8Ct3QjJMbEh7Rkef67slTalXtlyRXBgtlYIni5LVV4P7355Ut24USe2zBLJ2oFtdIjd8aapLdHJLppzdTh3lUufYciXB_92mJp-yXM9luHBw3xpOq6mjkCii1RZmCXA8FbEind0wWOK1PUbDflfh9unVVqtpZ1IYXVYn_iw-Kuh_b7YFRjSSdNLuyDOMjdx5SFPnBCBDN3lJ6d2oVkiuy8BhBc3b4l622CfpEa6XR9ZABIPNkNiojxi2HQr9Ny9vvPf3ZQqTG5CmwsE1XTMrjPWhslJczBN-0_SdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام وزیرخارجه خطاب به رئیس جمهور لبنان: لبنان را از دست دشمن واقعی خود نجات دهید
وزیر خارجه:
🔹
بر اساس اظهارات آقای عون، ظاهرا این ایران است که یک پنجم خاک لبنان را اشغال کرده، یک چهارم لبنانی ها را آواره کرده و کشور او را روزانه بمباران می کند.
🔹
اگر لبنان برای ایران ابزار چانه زنی بود، ما مدت ها پیش به توافق رسیده بودیم.
🔹
لبنان را از دست دشمن واقعی خود نجات دهید، آقای رئیس جمهور!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/656501" target="_blank">📅 07:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656500">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">حسنک وزیر</div>
  <div class="tg-doc-extra">پادکست کافئین | قسمت بیست نهم</div>
</div>
<a href="https://t.me/akhbarefori/656500" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
حسنکِ وزیر
🔹
بشنوید از داستانِ مردی که طوری پای چوبه‌ی دار رفت که گویی بر تختِ پادشاهی نشسته است؛ درسی تاریخی برای «باوقار باختن».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/656500" target="_blank">📅 07:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656499">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3118ae458.mp4?token=QGssc3uLEybFvU9rXUFI0MvV2z8DeZ9EoACQTTaMwzJFbtpfhZZ7B1gAvDGxW5wz8IJtDnWoBpe_grCe20dLtZlvOeXCjX2duPkqELpkN87SyidoWwasogUn715HAZ_uewwlMSZIraTLm_NfGIsSCkeaVvtWEsXAv1YPKYJ1ZTCYVdJQvO6zZVDnJOjDQL8579RoXPUpwmq7UKoUTU5ANH-7EhYBEU--9KT2EwGZzS82kXkIgtTC__qxEuJYOI8XKNmGvUWlUQ8n__MzZtR8POz5sNx2C6TD1qAYfAcTZppVuYxpRqou0Ug6nf_eeKCB-T_H0QPRsyBLJqaTbwGUpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3118ae458.mp4?token=QGssc3uLEybFvU9rXUFI0MvV2z8DeZ9EoACQTTaMwzJFbtpfhZZ7B1gAvDGxW5wz8IJtDnWoBpe_grCe20dLtZlvOeXCjX2duPkqELpkN87SyidoWwasogUn715HAZ_uewwlMSZIraTLm_NfGIsSCkeaVvtWEsXAv1YPKYJ1ZTCYVdJQvO6zZVDnJOjDQL8579RoXPUpwmq7UKoUTU5ANH-7EhYBEU--9KT2EwGZzS82kXkIgtTC__qxEuJYOI8XKNmGvUWlUQ8n__MzZtR8POz5sNx2C6TD1qAYfAcTZppVuYxpRqou0Ug6nf_eeKCB-T_H0QPRsyBLJqaTbwGUpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسنکِ وزیر؛ و تراژدیِ «حفظ وقار در مسلخ سیاست»
#پادکست_کافئین
| قسمت بیست‌و‌هشتم
☕️
🔹
هیچ‌کس به ما نمی‌گوید وقتی شکست قطعی است، «چگونه باید باخت؟»
🔹
در این اپیزود به سراغ مقتدرترین وزیر امپراتوری غزنوی رفتیم. مردی که وقتی فهمید راه نجاتی از چوبه‌ دار نیست، به جای التماس کردن به آدم‌های کوتوله، با فاخرترین لباسش به استقبال مرگ رفت تا به تاریخ ثابت کند: در زمانِ سقوط، «اصالت و پرستیژِ خروج» تنها داراییِ یک انسان است.
برای بیداری، یک شات غلیظ از تاریخ ایران کافیه!
از اینجا ببینید و بشنوید
👇
https://youtu.be/wGPuPBpm5AY?si=Ln3xUuAdgTaF5EDZ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/656499" target="_blank">📅 07:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656498">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDIqCdRV3TmOXqQCDXfvhEv6xoUMP3APK2uHxDZtOX6l_N5WvcVZ02RZUJOasg6eLV1ia2ju7qnhHG2SGZJXrDJULmDedZhpZO8JVmZVIzp8IwdmkPBK1tMuNWUc9-qDi7xp0kzbJjg8xQE223Jw5w5qDCclfnNTyZRDhmsWCW16Dq7kWwvxViWC9UXZLuOQ5dyQvNtcsIATJzEfFyxeCoTkP2mjaJ3fhmBqNHBaEA4BrOm1RGLnoYxLfwjkQ7xCupcN8EsAkNpXfO96aUCCCAQqLJ5hHpFQwn8diO-yI8tKNf_XR7zoagmKmyL-LlxxRUCAwUry-JJvhmagh2nSkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۱۶ خرداد ماه
۱۹ ذی‌الحجه ‌۱۴۴۷
۶ ژوئن ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/656498" target="_blank">📅 07:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656497">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سنتکام: ایران ۷ موشک به سمت کویت و بحرین شلیک کرد
🔹
فرماندهی تروریستی آمریکا «سنتکام» حمله موشکی ایران به پایگاه‌های آمریکا در کویت و بحرین را تائید کرد.
🔹
سنتکام تائید کرد که ایران ۷ موشک به سمت اهدافی در کویت و بحرین شلیک کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/656497" target="_blank">📅 05:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656496">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
دو پایگاه هوایی و تاسیسات مهم باقی‌مانده در ناوگان پنجم نیروی دریایی آمریکا هدف قرار گرفتند
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی از هدف قرار گرفتن دو پایگاه هوایی آمریکا در کویت به نام‌های علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی آمریکا در بحرین در پاسخ به تجاوز ارتش کودک‌کش آمریکا خبر داد.
متن بیانیه سپاه به این شرح است:
بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
🔹
ساعت ۱:۳۰ بامداد امروز چهار فروند نفتکش متخلف با تحریک و هدایت ارتش متجاوز آمریکا بدون هماهنگی و بدون توجه به اخطارهای مکرر نیروی دریایی سپاه، قصد خروج غیر قانونی از تنگه هرمز را داشتند که پس از اخطار، یکی از نفتکش ها مورد هدف واقع شده و متوقف شد و دیگر شناورها متخلف به عقب برگشتند.
🔹
به دنبال این واقعه ساعت ۲:۳۰ بامداد، پهپادهای آمریکایی یک دکل مخابراتی در قشم و یک دکل را در سیریک مورد اصابت دو پرتابه قرار دادند. در پاسخ به تجاوز ارتش کودک کش آمریکا بلافاصله دو پایگاه هوایی آمریکا در کویت به نامهای علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف آتش موشک های بالستیک نیروی هوافضای سپاه واقع شدند.
🔹
به دشمن متجاوز و کودک‌کش اخطار می‌کنیم در صورت تکرار این شرارت‌ها به پاسخ محدود اکتفا نخواهد شد. مسئول عواقب بسته شدن کامل تنگه هرمز به روی خروج نفت و گاز شما خواهید بود.
و ما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/656496" target="_blank">📅 05:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656491">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQrt6vSCeImYiJRSJuUQTMn1TsIqdrL4jYpG8bYIsQXkT7fmY7b1XA9_Mr7tcnzlRykeoX1T1-2aeQVLXKffsAarFUyA8ghaedy9hd2RAh14k8n9Hx2MgEU6PH8Z_dqNZJeBweEUTS5wkIKvAkvJZVy_t9E7uDp3uMPnvw9WtWRP47-hLqrXuWs57bC_UxDXen4gSQEpmze0s8wsPMAbIrtOMfj87JmO6sdi-7kqczS82hc3-_kaSMMp_lwdms5DBICD-lnFU_up64A85eRtEFUCOu9mUMB0_xVLO5E9zOs7xvkXZFHWNimSSxpbVFc3gNJZ-zW6CigP0oAc-arURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/656491" target="_blank">📅 00:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656489">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh6eGA-DShhbwgIz9uJkb93GEWAHKqX-uQEDJLxBYrTuMraD8t1ZFVOzp0deraL735ZnZGhNfOsrxLN3MLRnO0kXhkka78pQbTp3eUy0auKyDHHdvQPFvU983xH5XdCN60TLVdlLD7-kdZBSUeg7trcrIx_dk44KPjiT3Z9K0CHEdCojxCMMZY4mEJcTuFUnYMYyVIF-jisB4j2v3rzXrVtnjlxOxx6Tpmj97WVDsWgReGz0KRll-iIo9AkM6_-Y-foAZRGp6n1js9H2-8arKPQgwN2Xl0_3aKOAhfiKgU6M6xV-JVilMW0Bb0vZlDOcgiO53v3sftkBWpicla06NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سنتکام به شلیک اخطار ارتش به سمت ناوشکن‌های متجاوز آمریکا  ادعای ستاد فرماندهی مرکزی ارتش تروریستی آمریکا:
🔹
شلیک‌های اخطار از سوی ایران برای هشدار به کشتی‌های آمریکایی در دریای عمان و عقب راندن آنها نادرست است.
🔹
لازم به ذکر است پس از شلیک های اخطارِ…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/656489" target="_blank">📅 23:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656488">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0LUvut5j_E6LfyM0Xj-Amkphn24VthyGtHvvHrnWmHSKI-Ljyl4noPPZp9InMgHiDywAKSKVMyT_cf6ZyYIoIoAaQxCviCtkgQ_g2qYCB2Yks6skKuNqfxJWl-aeRQCuMMMg-kvqfXmoJN_nOjxsL4YbegFWMWnPGSF4s-AWV3rn_OAlgo58uSd57HppY5mrc4Zxarfp3hn9ZazTYL1sWDEnsK50d4vWZb1M7HH_5GN82ScAVRAfdLkCnMUqt-6isAPI97W5ROUi4kTDqckgoTyJjSxlewWcWEaBrb_CGuP5JnZk4mTr9o_1-QsfEjPqXwBIgkkgbneAQEIbEg0sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگ زرد: در حال بررسی ارسال سلاح به تایوان هستیم
رئیس‌جمهور آمریکا:
🔹
در حال بررسی امکان ارسال بسته تسلیحاتی  ۱۴ میلیارد دلاری به تایوان هستیم.
🔹
هنوز درباره ارسال کردن یا نکردن این بسته تسلیحاتی به تایوان تصمیم نگرفته‌ایم.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/656488" target="_blank">📅 23:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656487">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hd3_iDBNONAkZDbx4pVU5YKPqK88P3IDevmeUbQNMHi6KNuKmMDCGaNjgLTaCK7NK4kflnEOL9ealk81rUzHqmSuJNpm6nnsmw0C6aJqAZxxl-3cwXcw5-IA6foxQig-t_LG5e0mMsCMZwa8x0PopZ5YRUYoy5WPNCSdoDqZ2oX4IF4-A5x3uX8_UjZS-xgz9YhkkB8MT46cHfY3EGnt0_fuLYJ3QG-wEVnTP5vw5j2KdT3bFmCkzxrj5Km8zW1xes4WRIjih-so6T9v3a-qOkcojzaDf_0P0zAwIhJFWKPTbH45lFUgDe0gW4hxK1YtS_EDna-i2nWDTweWCtNdhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری تماشایی از قله دالانپر ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/656487" target="_blank">📅 23:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656486">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a55273f8b.mp4?token=atPgiaEHnWhP0WA825jAQEWZRWSLxyXqwDNBTElIHxv9fTtZJDgE3Mna3MLdkcyU4XEkNU69sa5t_QdRGaIwg0qzDR9sDabUg-U6zPvI3f-x6HFeO-KiDPVDNXZ2ftgERvtKQUiLnTAojVx1o75LLA1IeqHIUmEQhoqLEz1cI0iK2M0Idf3zUIe0XJo6xkWDp0gq0lN3Dr02G_kPCH7gDwst5GsILWjRvnxFv5Ass5alqSkhWmrV3GRbFXMs37ZuaML6z4lNFLkBjo8VOtPtBDAFN3GePpjCp4iotclNsrvalWL2updIqFZXU39SutfKXzILT1R6VU_6RRsknT59toWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a55273f8b.mp4?token=atPgiaEHnWhP0WA825jAQEWZRWSLxyXqwDNBTElIHxv9fTtZJDgE3Mna3MLdkcyU4XEkNU69sa5t_QdRGaIwg0qzDR9sDabUg-U6zPvI3f-x6HFeO-KiDPVDNXZ2ftgERvtKQUiLnTAojVx1o75LLA1IeqHIUmEQhoqLEz1cI0iK2M0Idf3zUIe0XJo6xkWDp0gq0lN3Dr02G_kPCH7gDwst5GsILWjRvnxFv5Ass5alqSkhWmrV3GRbFXMs37ZuaML6z4lNFLkBjo8VOtPtBDAFN3GePpjCp4iotclNsrvalWL2updIqFZXU39SutfKXzILT1R6VU_6RRsknT59toWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهدید یک نماینده مجلس به ترور مقامات اسرائیلی
متفکر آزاد، عضو هیئت رئیسه مجلس در شبکه افق:
🔹
اسرائیل بداند که مسیر ترور یک طرفه نیست/ همین امروز در خیابان‌های اسرائیل اتفاقی افتاده است که معادلات را عوض کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/656486" target="_blank">📅 23:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656485">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔹
خبرهای داغ امروز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
گزارش لحظه به لحظه از اخبار جنگ و مذاکره ایران و آمریکا | از شلیک موشک هشدار ایرانی تا توقیف نفتکش از سوی آمریکا
👇
khabarfoori.com/fa/tiny/news-3220568
🔹
ترامپ: به‌زودی جنگ نهم راه خواهد افتاد!
👇
khabarfoori.com/fa/tiny/news-3220567
🔹
رئیس جدید موساد کیست؟ | همه‌چیز درباره مردی که می‌خواهد نظام سیاسی ایران را تغییر دهد
👇
khabarfoori.com/fa/tiny/news-3220645
🔹
ماجرای آرم «ساواک» روی سینه طرفداران سلطنت؛ چماق به دستان وارد می شوند | رضا پهلوی «موسولینی» می‌شود
👇
khabarfoori.com/fa/tiny/news-3220679
🔹
پیش‌بینی یک نماینده مجلس: آمریکا بعد از جام جهانی سنگین‌تر حمله کرده و ایران را تبدیل به غزه دوم خواهند کرد!
👇
khabarfoori.com/fa/tiny/news-3220707
🔹
ویدئوهای جذاب ما را در آپارات خبرفوری تماشا کنید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/656485" target="_blank">📅 23:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656484">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
صدای انفجار در کردستان عراق
🔹
خبرنگار المیادین گزارش داد صدای انفجار در حومه سلیمانیه در کردستان عراق شنیده شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/656484" target="_blank">📅 23:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656483">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c285d770.mp4?token=DOIm7tOSWfMipblBwz6uLqx3KkluGNlo0DVVYL3vNMT3RHZxTl14VT3oCG59Ss6FneAxz5huoSJ_ZJRvl4pWD02ddO9OxPFGzegb3VaA0Hv0sHIiUBz89IkuKYZQhkZY6toIOLNLqq8iZpeZ-s3TOZLT9hZ97ssX_68CjtLOtpv1rKhcFI7UXfeorDE87HsTx1STvBHitdfKsUgO6glNHfHl1FxE4PduQjbWk7mWgIqC2e9NwFEd_Rx1cDadXostg6NCpgTrYwOjnDIp2AG2m0FCR_je4_SqwXIda1zaEYyDsBV0EWehzulAxjSO0hDMcFGw4Ta_mRMsM_9ahJkL-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c285d770.mp4?token=DOIm7tOSWfMipblBwz6uLqx3KkluGNlo0DVVYL3vNMT3RHZxTl14VT3oCG59Ss6FneAxz5huoSJ_ZJRvl4pWD02ddO9OxPFGzegb3VaA0Hv0sHIiUBz89IkuKYZQhkZY6toIOLNLqq8iZpeZ-s3TOZLT9hZ97ssX_68CjtLOtpv1rKhcFI7UXfeorDE87HsTx1STvBHitdfKsUgO6glNHfHl1FxE4PduQjbWk7mWgIqC2e9NwFEd_Rx1cDadXostg6NCpgTrYwOjnDIp2AG2m0FCR_je4_SqwXIda1zaEYyDsBV0EWehzulAxjSO0hDMcFGw4Ta_mRMsM_9ahJkL-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو پربازدید در شبکه‌های اجتماعی از
تینیجرهای تهرانی در یک دورهمی که جهت حمایت از ملی‌پوشان فوتبال
دور هم جمع شدند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/656483" target="_blank">📅 23:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656482">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">شب شب ولادته تو دلها قیامته</div>
  <div class="tg-doc-extra">مهدی رسولی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/656482" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
شب شب ولادته
تو دلها قیامته
برای عاشقا راه سعادته
🎙
#مهدی_رسولی
#ولادت_امام_موسی_کاظم
(ع)
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/656482" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656481">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/008d1f0eff.mp4?token=QaFBXdSMM-NwhAKvLnZeMMSr87FIgR5jwPY2_7EiNUeU4y3y7BWP8c2MzHRlCTJV2DzUW_DBdBXYCdFC5wcMTyR3mfZWJxiimBRktpysR6SYRpPs7lvflmn_HsWhrLZCc_AXECyDN31U2rrf48fe4oLmqYtawUm-_TmHloRhthycOONPgx4pQ6hT-so3zTtIc13rvklqXx_GSvz3HvK4LvRhE2fHsfFwCug_inNETonatPqFY5fYbd69nSnonkCSsivIMqJDmVbXu3_kj9_DAr1Y5Ok_MkU7sm9PsOyVq8b6C3MMottyN8CuFuf-jucgADU93OcqJ5yaWX8nqOBnoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/008d1f0eff.mp4?token=QaFBXdSMM-NwhAKvLnZeMMSr87FIgR5jwPY2_7EiNUeU4y3y7BWP8c2MzHRlCTJV2DzUW_DBdBXYCdFC5wcMTyR3mfZWJxiimBRktpysR6SYRpPs7lvflmn_HsWhrLZCc_AXECyDN31U2rrf48fe4oLmqYtawUm-_TmHloRhthycOONPgx4pQ6hT-so3zTtIc13rvklqXx_GSvz3HvK4LvRhE2fHsfFwCug_inNETonatPqFY5fYbd69nSnonkCSsivIMqJDmVbXu3_kj9_DAr1Y5Ok_MkU7sm9PsOyVq8b6C3MMottyN8CuFuf-jucgADU93OcqJ5yaWX8nqOBnoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجلیل از شیخ نعیم قاسم، دبیرکل مجاهد حزب‌الله با ابتکار مردمی در جشن ده کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/656481" target="_blank">📅 23:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656479">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dd4Z75JcMoYyvWRHnJ3vhP3IV_H__jcJr9DlBkr7qPzW4z_BruFHY-7ggOCgwKaF51Nkn2gG9cN24ymBF12BZOKDnoAf0cai4PYu8B_DZCMkBksVOQIThzF-l3LD5hiM5v12E0MUAhDUnB0xqLmD3HF912XovknoEPq3gEEJ5p3pKM6r1LMEW0_mJH6b-afBxGkdFK2E3FCoeYRzbTtZsme6BROW6LsROsznWHFjCQo8J1bRhG7DhXtZyDY4HI2-qMxVnIcjy9aFs_mjqSi-JDvp-RLCcAqb2MYTMWT8jrRrzoDsyoqKccvDec9Ff0k5feLciA4HmOho17O2QkbmWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvRFSZyljwkHqOfADT1FhMp5IjAd3PxnZLpRFlgGHnvio9cLCbo8U8Lio2qtUaCqLxCSW6Pdm7HFWwe4tStbu1TyaWbZ_hdCDhzqEzzaf3T17mTxUWMpR6vWNun_nFOVuwjt3qoHIDayhbZdTon1s7LLVTSm1IH8MiKvY8S1Tt5V3siQjXhUQ3DBcpFtH8GJCosogB9PQMswyojT97tLPiNqOuH3q78QKRjUDyhfDtkgltr_PU20qW_80jQU2O6Phenj4gCRVe6_Ba2MVLFno6K0R1m_fD4KKu9zSKE8gZtQWLrM9Dzph9DVYT2bmfIJIhH0SNWLzqZLuRbztYX3WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وضعیت خونین بازار ارزهای دیجیتال
🔹
بیت‌کوین برای اولین بار در دو سال گذشته به زیر ۶۰,۰۰۰ دلار سقوط کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/656479" target="_blank">📅 23:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656478">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guX1BPCHAYObJR0eT9iADxcg2kV-D90oMyJq3guuekRLoI3ltTsajWT3nwR5zl5RnSkeykSxC8TFnG6dObCWes8jxwQFiFNdL3hcIxahnoLXHgCEIwoRL4O554EgQYxrYa-KUpEege8jLxfDCfSWZljauK5yB_OCURUR62jSBSdrXHSnWck6IoDQDABEDK8HaLuSg24TQgEDJ9moWOxyANt832bZZnx5cGd5JCUutNk3g9DbR0WAUeBOGoi4oXQ-kiYSe4wnJUKebRwBtLpxCnrlovhFhPSH_1Vg-CJinoGEq7qSpjy5zPRdefY1FMhNUORMrO1SryEQwv6wq8Sxvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای آرم «ساواک» روی سینه طرفداران سلطنت/ چماق به دستان وارد می شوند/ رضا پهلوی «موسولینی» می شود
🔹
آنچه مورد توجه رسانه های اروپایی قرار گرفته میل طرفداران سلطنت و پهلوی به «اقتدارگرایی» است؛ میلی فزاینده که روز به روز بیشتر می شود و مخالفان استفاده از خشونت و خشم را می بلعد. اما استفاده از عبارت «اقتدارگرایی» فقط بخشی از هویت برساخته توسط پهلوی چی ها و طرفداران سلطنت را نشان می دهد. به نظر می رسد طرفداران سلطنت و پهلوی تبدیل به نوعی جنبش «فاشیستی» شده اند.
بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3220679</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/656478" target="_blank">📅 23:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656477">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4756779ec.mp4?token=Nk7rQR4r799K89qDT9hwYsLmQ2mnjEj2sXThfpPSG9DS4SDGUeoydFEXnNs9Ce8KDwEYaMsPrBo4iIMlyJpvbm9y_TtYIcqTk9K-B7ojKsumEXBv236b69ijMKTBTgkuAbEG78AiBFFnPe_UMDOPPT8PX39YOq9cT-zPeCh0yIjiZ8ZRN5-hTiTE8BwG7NvSSgSavRV0t1bd1VcV9gi42_z30Eh0xcqQCmr1WvqVMb_Gi3wdlP19IRVUckdsRccly9SKICYo4AgKp4GE0qgTSe0FyPsVBk9mcTMCjHSTkxZOcwoTXn3u2hHLeNjUGyrSyajqT7mnA1B0Xf_Bl-UjxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4756779ec.mp4?token=Nk7rQR4r799K89qDT9hwYsLmQ2mnjEj2sXThfpPSG9DS4SDGUeoydFEXnNs9Ce8KDwEYaMsPrBo4iIMlyJpvbm9y_TtYIcqTk9K-B7ojKsumEXBv236b69ijMKTBTgkuAbEG78AiBFFnPe_UMDOPPT8PX39YOq9cT-zPeCh0yIjiZ8ZRN5-hTiTE8BwG7NvSSgSavRV0t1bd1VcV9gi42_z30Eh0xcqQCmr1WvqVMb_Gi3wdlP19IRVUckdsRccly9SKICYo4AgKp4GE0qgTSe0FyPsVBk9mcTMCjHSTkxZOcwoTXn3u2hHLeNjUGyrSyajqT7mnA1B0Xf_Bl-UjxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخست‌وزیر پاکستان: همواره در کنار آمریکا بوده‌ایم؛ برای همیشه از «ترامپ» به عنوان «مرد صلح» یاد خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/656477" target="_blank">📅 23:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656476">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
مردم در یک هفته ۱۸ همت نقدینگی وارد بورس کردند!
🔹
در هفته‌ گذشته بورس ایران با موجی سنگین از ورود پول حقیقی روبه‌رو شد. سهامداران خرد حدود ۱۸ همت نقدینگی جدید به بازار تزریق کردند و موتور رشد سهام را روشن کردند.
🔹
در همین فضا، شاخص کل با رشد ۷ درصدی تا سطح ۴ میلیون و ۳۵۹ هزار واحد پیش رفت. اما ستاره اصلی بازار، شاخص هم‌وزن بود؛ این نماگر با رشد خیره‌کننده ۸.۲۷ درصدی از سقف تاریخی عبور کرد و در ارتفاع ۱ میلیون و ۱۶۲ هزار واحد ایستاد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/656476" target="_blank">📅 23:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656475">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
تریتا پارسی: به بازیکنان جام جهانی ایران ویزای ورود به ایالات متحده اعطا شده است، اما آنها شب را در ایالات متحده نخواهند ماند
🔹
آنها در مکزیک مستقر خواهند شد و سپس برای هر بازی به آنجا پرواز خواهند کرد.
🔹
این بدان معناست که آنها باید در همان روز بازی از طریق…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/656475" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656472">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f1d4b315b.mp4?token=s0zboiiywwv8DEvErTjV62yzBQPfVPgWgZGzQGxbdmhEg3B22d1MSMCozG_lnv8ZyQS6tOsGk_q3ApgMllXhTYLY_4i6BESFHLt8-5PpWkEpBvofbzOFNCUU3NOXfwndvsGs1As0Hj53ERAybQOGqJjs-6g57dB74B832o6we0ASs3R-GLiGtFXf1-r8LjZlwwFEAOjOja7wy1zHjti7nD8IEsPPspRUvZynOfWDo-9WV167GhZLDpothH_y900Na37_-D7Vw_uAcuRPmQnXGravX3AmzJ7XAy4DH1xg8zTBwmnmsox4UYS3hfIWZlWB8fDtoLHfHB6i5zQIIsL7sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f1d4b315b.mp4?token=s0zboiiywwv8DEvErTjV62yzBQPfVPgWgZGzQGxbdmhEg3B22d1MSMCozG_lnv8ZyQS6tOsGk_q3ApgMllXhTYLY_4i6BESFHLt8-5PpWkEpBvofbzOFNCUU3NOXfwndvsGs1As0Hj53ERAybQOGqJjs-6g57dB74B832o6we0ASs3R-GLiGtFXf1-r8LjZlwwFEAOjOja7wy1zHjti7nD8IEsPPspRUvZynOfWDo-9WV167GhZLDpothH_y900Na37_-D7Vw_uAcuRPmQnXGravX3AmzJ7XAy4DH1xg8zTBwmnmsox4UYS3hfIWZlWB8fDtoLHfHB6i5zQIIsL7sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام رضا علیه‌السلام:
کسی که قبر پدرم را در بغداد زیارت کند مانند کسی است که قبر رسول خدا (ص) و امیرالمؤمنین (ع) را زیارت کرده است.
💐
ولادت باب الحوائج
#امام_کاظم
(ع) مبارک باد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/656472" target="_blank">📅 23:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656471">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
حمله به کشتی ترکیه‌ای در دریای سیاه
🔹
المیادین گزارش داد که یک کشتی ماهیگیری ترکیه‌ای هنگام تردد در دریای سیاه هدف قرار گرفت.
🔹
در این حمله یک نفر کشته و ۴ نفر دیگر زخمی شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/656471" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656463">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgxs55ClOTNU_aB0TC1tsKiWqqGD3Hvuo9zI2_3xXvH8t9wpZysIprcJbFAKE6RMsd-VB0VRCdO4UpIKpQk7ybOZ0UqHV5kSBOv9RRZParNCdSmzo1bDDbA2RZNUpqw4soZh6EYLwSJa2vsn2CQcNeP3MjZz8J3YOcdMER4U3DZbQHXpx7sOlqTCLTppSDtWCh6zYBeymD2U2bZv52RWcuton6FL7IvLbaBTYZ0lIJXgMCBatH6OTs3N8Xq9sq4yojleN0GBVY0RnhEnxK0bhVJXQ3LledAvlyxJIUNOEk_0Ojw3wyqjxMwN_UmDUbKhPdZOCZne7jKB4QKQJnvKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMyrsXx51om2QQ2ZeVF0YVr_xcKGmI9XMz-aRXKO_7GiKP5UmdXdRJpHW6epkTkIgNv6EiXIhQdlwXWgMNc-q3bd4Eua_g_qPe9eLKfCj_Yg4b-_jExNbsOKEe_pPwkQqSASOgnx1BHwQM6PNcpNtV8LIKkpl98vL5PXvTBqZ60nIx-Sx2eItYXMrsggOyBY4jFR1ajtFnXPVfbBUkTKxMMO92gQDVJK9pdqrDiGO7Q42S0t_Hwa2eFgHnBETKNXfKLpIcbondJqRUnFQB_gdZPMI4NWqwtqsyPdwgZYf2iDCSARrD9K9mc5SapvgSG-cFTC301p1HwVm1hIfUsKQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tlQTqOoucxEWPdSLoW7XZ2pY_WSBaQeQiLmn_QOXxpJhBjMdcTsY-jwlJmJDiPtkkwwsL6AIO1sfqC2jXp0VTbc2MryjZtWk-ODzoGdQXDF-jcxlO5yKCqtREbbOkMyxWfdpRzBSQfb9Ri56EGAilCQNPUTrBWWODx41mS9B6L7xgbXHMBjb4C_aCueVXDwWcUuNszGtONzcCgPa355nPMNs-tbUg8wk7kKjjaGMRI7oSIVZQaMUMLqaZD26j2_CYuWc_bINI0OaX6hPMZh6gVsBE1QmPYlwzsHX6QNM2eJ9FezFxCFowvLbC9hhBZ-IozijBpz9-3v0Szh1xp41cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyZ-aCAl7GcxUl0doO5uXMu16fM_fUy8ae9Qi1vhpyF94zpKFlsLg7tLlYsjJhos6MYjTmOOvlLYN13spQUBgzYguT0T24H7NyvlJaeCXPvAsxqNAa3ykANl3XeOO2tYrwRK-OAFLRJ5K4Cks8Drk4NdgAPBSnTLuQNf9Eceh3f9h3VuS_36tcPrsib9agbtF6RiYsjwEMv88w2DS-6qSoRN97v0_O_xLbsvJgVVV71KcrFBNIfiGsYf9pE3QxSKkKLjCZf0GK_UIB7g3Swsg4R8ZS2eHwfa4PaSb2maBUbSf2SoPY2bShS0RgG0pgnMOjP3SXrhoRn4I93yNy1_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XNlkLj-hEpM-6D7GIN6C0-uUjP54lagjpzjdpEugwE_Fl4mTF31fAwZqE5AnWepJ2WDKfaMJgU9AjWvUee-q3OHdP8GDjDG0X-o_KbKVRyr0r3MCZUNLg42O4MO-Sfobnm5eQI0LYaiffNCRbGyD3xe58D6Crs5I0MMsMw3oleXnzpdsNz1XVmME__9d0kgt8vkiwPgxJILzqy8-QA8NcZAw7DW-ob3xTzpJVnAZqr9pHSQ14DywPO6YY8eLcmSJaW1j2O7miH5Lu2jpxgvXNGY-0VRGhDXQfjiWsTFkV9N2wQ392NMA4ns2t5Lre3nuPO5sSxm42WPF71iskYUatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoSiSNLxZoEBBPEDW4q7lt6_dyA4DEnemBq5XRSjyymR6qlCz7V2CRd_8X36J1_XrhPD54cn0rODWspTrD-kVMIgaxxxvX5zqqOGGVzi9nmWE7FTIgL4QtGg_MgfZPKJtcDUPL8_wn2h2Q9Ms7dURL2J-REVeR6whEQSVjCFSc4FgOqeAoONJopGN5gHIUzCbt5grDv5YdDYQHBIiDCzRVkZLKAuhl5n_TIbRI5d6Dn-lFhOGDJCgn7YJNtylEwyzil0CsuGzmO2_lEKA2PgiBR7n8aTlU8vSwDdOgjehrhJWPpbq-syMK_q-XJEcNC4hcnLhidNuDRJtr2_-WrhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PcKlppptluE05JFpEt_F7QEMNaApIgnJabsol6PbeVqwa9xvg1kSmfYQfG5mR2SbxdbFs6jhyP8lcR5Z4lADcHFgxBffDw8ZtiYC7SMbshSoE2dMmNo1L9KvlqjueKSHiuicEfzUCVfm-5pmoo_Iw0Jd8R0XcAS1SaXHAVtdHdrEE2YN9YryAbnVeX3FEgIWIh4ahInOtg_dnK7FCLtnGBEUC4l52WEXP_wCiIHsOyfW8avEO5Yb-AGVuw0ER8Ddm4A8ULjAt6x4JmHNkwccDOIwstmthS-Yzww4k9FTv_rce0IDPw1XdgLgxptFrsvjziZ_MFDmiKoMU_IWV4MGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CibMFIZEXJJ9FKklipHfqoe7P8otCZQi3adlpajPuk9h7PPLwFUnU_ZrrKX9fL2lQ2ICHfbViYMHjJ1yt_mEa1kZaCE9wFdb3LZ-wp72vPjf_i3wOJ8eT_l_DQUqSv-OE-e3CjuS5LCea9jvbZBu2Tpy7n8yxTqahevwldDQFVvYZRLTYGGSIdm5-ITVvvun8T6iNdAfaf1xjqZTMwUPs-G9XyDf-6CBHIMQDMGgbYmgSRBkemgyhEZvPoSw-Wv29fqQEWmvz1yeEZ2fdLmXdF5PQuN3S3A_9JjXywRogj3StCfvdgiq-BZ_bajz16adstaZbLa7LwV2dT7jVaArhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۸ عادت کوچک روزانه که به شما وقار و ابهت می‌بخشند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/656463" target="_blank">📅 22:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656460">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f1d4b315b.mp4?token=vbZz8fNoaFenJKjr8Hlby7ceQLoWrhAigSu5oolioz9j47QnK6teF7Xl6x0t-KILw9bctZbg0psvRc6azDaNCT6k2WPVDQdCGL7E9KZOGgBx7piI1Uj9Oh4gzl-2vVuUH-WK5khhuRjeBvG3GibZnHvSHBRMqTcf_z1PrBTUQFVxF7Y2d7Dp2QwhYuKg_qzwHULY9DvBVao6PPF6dzhRmKFLLy056HiCF5yoTwBDFVDxeBEqWdRMhqni3jwjnYzqXJEJrPZRyOoSxywacHJU2tEpJCIpuequShV5NeWT75EVaFc14QZbYccGRztxwZXCtDxmXSQ97j1CCra53LsE0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f1d4b315b.mp4?token=vbZz8fNoaFenJKjr8Hlby7ceQLoWrhAigSu5oolioz9j47QnK6teF7Xl6x0t-KILw9bctZbg0psvRc6azDaNCT6k2WPVDQdCGL7E9KZOGgBx7piI1Uj9Oh4gzl-2vVuUH-WK5khhuRjeBvG3GibZnHvSHBRMqTcf_z1PrBTUQFVxF7Y2d7Dp2QwhYuKg_qzwHULY9DvBVao6PPF6dzhRmKFLLy056HiCF5yoTwBDFVDxeBEqWdRMhqni3jwjnYzqXJEJrPZRyOoSxywacHJU2tEpJCIpuequShV5NeWT75EVaFc14QZbYccGRztxwZXCtDxmXSQ97j1CCra53LsE0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام رضا علیه‌السلام:
کسی که قبر پدرم را در بغداد زیارت کند مانند کسی است که قبر رسول خدا (ص) و امیرالمؤمنین (ع) را زیارت کرده است.
💐
ولادت باب الحوائج
#امام_کاظم
(ع) مبارک باد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/656460" target="_blank">📅 22:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656459">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfwnrVAdGW-8NbERmRcaRq1spy90NQYLdZSjw-QLMFvD5MEvLKKfLv97NZySiD_v_s8LNNoghVHPeb_-MaGQwFQKEZujxbS4tlmqbLknq7gz4zvcSUjhu7QiO0R6TQt71ZJGBAtDC9NtF5N8QZUMPd4xyTRGyYmLA5ypGipPEL0_ZMe96f1WQIoPQIG8KIoAPbiHulIA5yWPSR8Ery0teb-9GfNleJZcRGUxPZK_qpDI2i3QRJVwCA61Hsx9cdAagyjXDAfILRabrbMa_yAIni4SiEaZyLBAwf3wdWHRTPIytnt8SvKJq2iEEiaGqGY1i44vVQT6pqiaJ19rkggDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: روادید ورود به آمریکا برای بازیکنان تیم ملی فوتبال ایران صادر شد #ورزشی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/656459" target="_blank">📅 22:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656458">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
بخشش جریمه بیمه نامه شخص ثالث از فردا به مدت ۱۵ روز
بیمه مرکزی:
🔹
همه دارندگان وسایل نقلیه موتوری زمینی و ریلی بدون بیمه‌نامه شخص ثالث، می‌توانند از فردا شنبه ۱۶ خرداد تا پایان ۳۰ خرداد نسبت به خرید بیمه‌نامه شخص ثالث اقدام کنند و از بخشودگی ۱۰۰ درصدی جریمه حق بیمه بهره‌مند شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/656458" target="_blank">📅 22:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656457">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ترامپ درباره پوتین و زلنسکی: بگذارید خودشان حل کنند؛ من کسی هستم که آن‌ها را به این موقعیت رساندم #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/656457" target="_blank">📅 22:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656456">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1MeyV0FAgBKlDBAuWRy19ulFQkgci8amBVPRRJjAEiEZnfeSW4blGeQMDv0kujSii6GLBnBvCbjzDyPP4oFkmoibtyEeuuNi75LXL9mymF1exZcChxgAJFpjHLxvAMyup0S2Y1joxctDuKxda0lV5rQydcy4gW4ox33wZp2kATCr5-AT6BCDcr6M3bER8uQ1NDBHJGdHdL70mauMZs4-8qpnOfuoFS94DTik1-ZTtnXhq-WCnuVVX14Ibg8Um2F96yo8Iy4s88OIu9wnUtVRDb-Z8hKKZTOHmkvYqEzuiiZPQVU7W_G26PDbyTnfPc-mku6qpuJg2nl8e3o6vAe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس آمریکا امروز یک تریلیون دلار از ارزش خود را از دست داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/656456" target="_blank">📅 22:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656455">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای اکسیوس: تیم کارشناسان آمریکایی مأمور طراحی جزئیات فنی توافق هسته‌ای احتمالی با ایران هستند  اکسیوس:
🔹
در صورت ورود مذاکرات با ایران به مرحله دوم، تیمی از کارشناسان هسته‌ای آمریکا باید طرح‌هایی برای دفع مواد هسته‌ای ایران، محدودتر کردن برنامه غنی‌سازی…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/656455" target="_blank">📅 22:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656454">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03b8820397.mp4?token=Bpv8_YoO7gHgjqcS6QjexojF2ziVCNXLZSkAlsxSEhEFxt_TX8hxrOZeICmwvorHsyTSwMCPGSpZiu8t708ST-gpkAXpWRu_K-0uoBfWfDLUleSj0AwMSP9d4FsB9peInV-Ek5gVji7xMyB60Qh7rHS2SVCOvqXQu2475csx3BqlqqpbKQuG-xgdqOceFBlLE-Ms0pPW6NEgEHsY0-LKypyQYmFMuj7MTMVOx7lrMWjjjpOmiRMvL9kQARl3Uz7uwglDaDyrfM_LL_cLVU_HAbi_CS6YgOnX9BMj02rT9YxwcsuSKTbyu5u3o5VakvjE0PfT0YAwgGJsmVxxhRX6gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03b8820397.mp4?token=Bpv8_YoO7gHgjqcS6QjexojF2ziVCNXLZSkAlsxSEhEFxt_TX8hxrOZeICmwvorHsyTSwMCPGSpZiu8t708ST-gpkAXpWRu_K-0uoBfWfDLUleSj0AwMSP9d4FsB9peInV-Ek5gVji7xMyB60Qh7rHS2SVCOvqXQu2475csx3BqlqqpbKQuG-xgdqOceFBlLE-Ms0pPW6NEgEHsY0-LKypyQYmFMuj7MTMVOx7lrMWjjjpOmiRMvL9kQARl3Uz7uwglDaDyrfM_LL_cLVU_HAbi_CS6YgOnX9BMj02rT9YxwcsuSKTbyu5u3o5VakvjE0PfT0YAwgGJsmVxxhRX6gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع مردم تهران به یاد حزب الله قهرمان لبنان در مهمانی کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/656454" target="_blank">📅 22:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656445">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spzGTZq-6xzr_Gbs_5CHbPAcVzuoK3VGxK3tIDWg8VAAxMcDaDKBG8CbTlsUh3o2ST0LsxjU3fCCOPapYoFwb5yV9O5fbgOr26-UawzKKpanKdy5lNNMDgI-Z1AHRb_Sne8w5i1RJi611BUQ6raT79dHjTFMHitJ7jaqyP3Lch5_6muN-OrN7KYVnfg1wn7etXLqGsXIdioZac96ex6B9HHHViRjAsFaqNsonP_yx8gt5pOOkdo7ASghxZ7wGARGe1gwubGdPRoozorbmkGmVVW936hb61hGyoijb8VN1ymKISdcdsHS7g2uq5R9foAf9uQu3H3CDw_JA0Jb2gfJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFnos-w8s54sQ4dnmh68LZz_O8QkftCiET9t8KnuxFxMwXOKT041tvL_MGoPbVT4_2ApPDPnLXoyU8yYrP649tCCZHMIQsaAUGDq4edIaj2eWXVb9ltoYZlTj0GAJ9kTVuEiXPWYqulZiM5Dx87y7j06yKHyUfh_kNX8MmoBtkPqZOtsCvNwWeko6gqdkp1aGgpmR3uY3qBgwIds4f0mpRD_B6AqO26LUEA6aOCoQudaEEzx28bxNZsnrkH4j_2YrrjL2CsJ-_hiBlUbC7XOs9Lc9loHUvp-m5K9e3cARQFIqAC29MXwFX0V9alPrImR-t8_c2sxCdpk_q4fZPi3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mc3GVJsiS9GPyweBpSNHsUMmTK_yq7upOzKGKWtOc9xyQw0eR9Mel4np-e7J79HPlo1woUklmK1nU3BXua5H2PCrDCxHVIxP5ZhJ0JIQ_LzS8hjBwPVbyulUCZ0wRGhsV6xsjcgOp6uMqCqchXBzb8YG8S3aSmPUD0gkMNi9FjhfLsEi3ttoAL-cBAmmX3zMlHAy7G1vHHLD-63p-oQvvyZNwVNeWGbNllL9J9rb_kVyVjbA6fXSiiX4LuQZzKoP_xmKit4xfQzpV18pvOKM7Vsz8-b0G2F1uRQdL55RWpfML20TM6e8jnYChVb57RrEHMSavnLrA3ZgLQBK80BQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BaA9iLZZecVRPnmxxNeggvob2JRB4an1ojkpJVKYC_DB_o-VidBPvd8mxejRVEpYMrW8O2uTyoQxXDfZlrCmWeY8gkx-tD1hQM9j4tDqskh_tiHTMItOebFh7l2KXQ0iN0C1RDIYbWG8PBy4ywhSIWfmPWjx96wZ3D_PyOnHf9SRDnFCzLP00TFDn92tFbND9Np8hGjKwyDTkl43e6KiuN40APOKhZFHcXbezPp_SKpw99wgltHXHzo6dsb98L6lcTyqA-TxGydmAuxFgDgg6B-7vnt0b7aKufhQb0xtLkchNn_d-FToQjpv6UKBM38pHOt_4AOjcWs_WfFnWujxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDLwiY6VBawBhvqNCIGHf7fSr7DN69S0yhCMmR2d3M6bNIyHPqZm4t1gG7ZAuZBsmF_dBJ-lfTOMl2YiI4AyRc1_u7hEBreOMyfJtJv3h0D4Iau7p8zbTy_sT0yZlOgdhiB8u6l-aaH4ta-XBGWHGgT17j2iHgVNvbGF5qYbTlRf_bVsMe61Ya5s84qgbfWGwjPPha20aQN60YyYMDxdjJQPU8zrGPKZE5kprgJiumuMJ1_49HjdmwGGhFTflhRbzq1I5TSC56YrHii9P5RdBkweW1jQ2u72rD_QGsJkQlvWm1LIbfudpQPj9yn9YziJYJ0nQIbWe9Wlu8lNdz7wPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tgKSipq5xMAqtAQzeXkrNevWZj6BlFhg5JkYKH1CzylGOzkYYdjnHSCGKgVHmyYECHG7q1rFR0YkLMFkeQ0ZRHrSXwWJHcwfTF-bldwg5x3QLJ0XXN_mVB8kl2LQI56fnKJ8sh8LTjvLmDuIvTZSisolel33U6Oe8t3JgBFTEHQXg8VQNu4cUMLIKffYK2UCQWXJ3MttxOeUxtJiEJ-X6CmaZB3_4XwydpKUl_G2Rl1xXYXRXb-adlx9H3pMdXD22ngj7TQ7JCTs1EbzLdwgF1FWjefLONYtkxivq-GgCJaCJuMFL1sf235pSwmGKU9dlJFqEFdWk2EURHGfSTtv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2WX-yNo30u_idzJEembuqF_KOaBvNMwpLLJWi-hqjx8JZeRMXvDpGOn1YqIayxPoEhpQutR7Al_M-F6ap6-ET1CnYfSA1YDxX0JgxJQCbMR8rZkjj8OyFUfVNifr_T0AbZr_q1ZMF6mccxQMHBgEdTvlg5kgZyyj9bJHwHDC14grc_h3R1iaWyBCnVgFBNRMEonBORaDMb9EruA6NBwIW6ckb_R0KhXh7v7iFkgldXtmZMN2gZQpDiOt0JTvuf8qfNCcapiFYLbiY_51LFLdu4TNm1MU3_WjHI6JZ8jaUkGD9YIb3DsE9oZL3ov84SJZGZRUcKdQG9v3ojIe3pGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-B9DLtrjoxNOylO0uC2L-g86YsW-dmz8_NwG7j-TMFXIMMHEyFO7J50xgHTqN65QzdC7tx-AxrWgpCHIsVxqlFGSNMU8bCP4NXbJbRHlOItUigCwVOwbV7d6rZA6TwZ4TFvrgCeNv98SACTDIHlA7FFlWqNOH11BWTCED5dLL7CJNivVQ2LSf4pRD-uPvPUUltypjNU6cxxSjf4Ppgk9A8loCQc-eXXNeuPH0XbRhEC031XtZAO1t5j6aGEfsh2eZlyYZ1kUdLrQpBWlw4zFjtAuK5iiqW7cIgp9cpwfK2R50NjTrxYijaNLJZf_9Xy9QBL8utNGkOOSLI7nxDL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXLbFGXQAnGTfFYO-UwLcaX03UzZQFNnn_Q71RV5cKtLZFXsZsZMSpPNEX7Yln0nAdTsCweqnOb3Scv5IZdHUDF2D60J3l0nHNwzNrKap9FtUPDNgyMXqVqaHdN56O2-RgML3-vI2dhDcM7ouZK9NMs9O_ZKpiUKikXtQ68TszqOSM-1Fxcsv6sTFze5SOB9qmoMfjz4uZ_udBPHnT82zBakxgOCXakXFA8ClQnsdajMyAx190DLvZgvE-2gCFxFZvSCOeKgyV-cGJWk34F_Gwux80HCizEwopJXygD2O-StrX9NVZLtdtmnSV-quo9DBl-MqQRtZX0PyKJXFMKYvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت قدم‌های خیر
💫
در مسیر
#همدلی
و حمایت از خانواده‌های ایرانی،
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، تلاش می‌کند سهمی هرچند کوچک در این مسیر خیر داشته باشد.
این خدمت، با حضور و اعتماد شما مردم ادامه پیدا کرده است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/656445" target="_blank">📅 22:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656444">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgyGmyDjmBTvLKgecdmTnJhwpoq2RsUfLjj_I911UMOejCleu2a8KcVQhAM-aRBF7K1wdcluXmQQA6S7zgnMeVR0EspwfV_UPnS8eGq8ltGxjLwLu9STqjp_3HVNAWc1vADXe4oIH8eGhePumz8Nqx-i67CxAlODVp7NYQhciy8Ro0go59LuUtcThotEW75E1Ms21z40fB_QUwwiCH2d5kw9euR2G8GngklA4Rhy_ec13fPpJxXKwZPnqubkjPguMAjZugIoXIYimfwA5qN7Vc5BDtJq_RtAQTONSpRen471aLLXMVxLN5juN7GHQCqfM4-JKATmahuhWlvwpQpK3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صاحب ایده تغییر نظام در ایران! | صعود یک نظامی به رأس موساد در بحبوحه بحران اعتماد اطلاعاتی | مرد ناشناخته‌ای که رئیس موساد شد؛ رومان گوفمن کیست؟
🔹
صعود سریع رومان گوفمن از دستیار نتانیاهو به رئیس موساد، یک گسست از سنت در جامعه اطلاعاتی اسرائیل محسوب می‌شود؛ آن هم در شرایطی که این سازمان پیش‌تر با انتقادات شدیدی دربارهٔ شکست‌های امنیتی گذشته روبرو بوده و خود این انتصاب نیز با مخالفت‌های داخلی همراه شده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3220645</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/656444" target="_blank">📅 22:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656443">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای اکسیوس: اختلافات جزئی بر سر یادداشت تفاهم میان ایران و آمریکا  اکسیوس به نقل از مقامات آمریکایی و منابع منطقه‌ای درگیر در میانجی‌گری:
🔹
واشینگتن و تهران همچنان بر سر چندین جزئیات مربوط به یادداشت تفاهم (MOU) اختلاف دارند.
🔹
با این حال، این منابع می‌گویند…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/656443" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656442">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای اکسیوس: سفر ویتکاف و کوشنر به اوک‌ریج برای بررسی گزینه‌های فنی مذاکرات هسته‌ای با ایران    اکسیوس:
🔹
استیو ویتکاف و جرد کوشنر برای رایزنی با گروهی از کارشناسان فنیِ احتمالیِ مذاکرات هسته‌ای با ایران به آزمایشگاه ملی اوک‌ریج در تنسی سفر کرده‌اند.  …</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/656442" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656441">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFIKnRPEpyjZ9xQWZqAiMyOkJhNHD9YZNJxdJs8tiqQKtt24yhpsmTmAoENshQzAiEMNGyJaXgMZA_FcbDmvAaG_ipyVV9XwIo5ckHCT_xEc7EOqeC2XBXPyRtqBak2rDcEcoDU-u47wlfGjpwkZNpNaEls2r9NcFL-VA8s9SfDn2g6iEbVsXrQW-2b5u7fEAXNgaRWqz8OoJ9P4Gm_H8v-Tfg2CmlxYS5N92OIQWpHVGF6JYzToITm224_RSke2qn-y5ThiD92fwo84adq-8G8Z5VD0nbdIF8bJe360k1eIEJvkiLeiuoXwR7W8XBl60HqpUVrTQTbMQAENRmoJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتورسیکلت موربیدلی N249R
✨
249 سی‌سی
💪
تندرو و قدرتمند
✅
37 ماه گارانتی از نیکران‌موتور
جهت مشاهده قیمت نقد و اقساط و مشخصات فنی روی لینک زیر کلیک نمائید
👇
https://l.nikrun.com/0re
🏍️</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/656441" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656440">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای اکسیوس: سفر ویتکاف و کوشنر به اوک‌ریج برای بررسی گزینه‌های فنی مذاکرات هسته‌ای با ایران
اکسیوس:
🔹
استیو ویتکاف و جرد کوشنر برای رایزنی با گروهی از کارشناسان فنیِ احتمالیِ مذاکرات هسته‌ای با ایران به آزمایشگاه ملی اوک‌ریج در تنسی سفر کرده‌اند.
🔹
کاخ سفید در پی دستیابی به یک یادداشت تفاهم (MOU) با ایران برای پایان جنگ و آغاز مذاکرات هسته‌ای تفصیلی است و قصد دارد از پیش تیمی از متخصصان را برای این روند آماده کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/656440" target="_blank">📅 22:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656439">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgx5Q-1t4rwEfik7XeXGnVQy-Dvw34sogXohhPNEHcwS3DO068BF8nP-ZOwppZgdR7pvtXiVQaZiFFlkPUdoRCbKoH9BR3CXGMa8Rs9gjo9cVzTpCyln0K2xPsF7hRA3dZihYhthQ2M2jwxImoRZtNJY0pYzj06ElM-FwMMOqnJ6yM9WXhRS-1tMUeNHRk0AMqaYPMP-tvPnRTNM2_NAce5bUd_Tx9FvsYbOnicvfLJ9E6lQwMUth2GRlaR_XqfhTaVXqhT-esF7gHZP7kBnsZs5VYbs5ygf1qLg0nWSWnh8ZSxIpV70CbIoih_ngTkR-tk4-YyDJmEo_aFjw-4rdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر منتخب خبرگزاری فرانسه از غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/656439" target="_blank">📅 21:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656438">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای
سخنگوی دولت عراق: سپتامبر ۲۰۲۶ پایان ائتلاف بین‌المللی در عراق خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/656438" target="_blank">📅 21:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656437">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33bc160535.mp4?token=GJovYEXsgRxeU9agcB2NiczijBW7miYFPDmOcaO7wx0z9Ywqx-h5l2M3z2hl2YwscG1QFWYjqt1BlZITHzobhVCX8ESDiWAtP-_JU_We0t3aM0Iss5oBMghYvOBXBAPvLhyVZOUDjscqRU55DXropPRxAeO2vLbjWw0L_K-LthstYDBbaZ-slw5tjZkMb3Sgm5d5lE118iTd-i8MkTl6GqmTeSSd3TAnsJtDmWoCpOP3n2IEL05f1cMKyLxwg1i65d2A3Geh3DeASpYbiw2itdKMcx5WMdp1GnzbzSUPHYugsG4cQfXYPRpCnEdl62rIo9IRJruZZWkKKC-uAvhIEx4DmvjMvk-nOS-w4J2XAhPLhqAPndAObtDWBXuI4Ws0znpTKHzS0SpcZQno375PX2on0yq8mdiqc8p2QwVMGZdENWy6uYPlSEkJrkpr2zPZ8QYXc4fEBIzkOm2W17frtnI3bs9bbWUV3gDSnH19JVyBdOOnQqOF4orRlxA18QjqOxcOiHq4oSQsuhzH3C1BkcBBSwimCD-EqkPcHOF0bGoTKbekajOiLkgG6nQeoRQ0whJ1gRKd8XifIlvn9X09LixAhH7JOb4p3ecn-eK_GnyGJD6Ov3OsOV9CjWNia-wWQsFD92nJ33wZAfEJ1Nv056eGFkNi2oXTjoZTh1rKX-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33bc160535.mp4?token=GJovYEXsgRxeU9agcB2NiczijBW7miYFPDmOcaO7wx0z9Ywqx-h5l2M3z2hl2YwscG1QFWYjqt1BlZITHzobhVCX8ESDiWAtP-_JU_We0t3aM0Iss5oBMghYvOBXBAPvLhyVZOUDjscqRU55DXropPRxAeO2vLbjWw0L_K-LthstYDBbaZ-slw5tjZkMb3Sgm5d5lE118iTd-i8MkTl6GqmTeSSd3TAnsJtDmWoCpOP3n2IEL05f1cMKyLxwg1i65d2A3Geh3DeASpYbiw2itdKMcx5WMdp1GnzbzSUPHYugsG4cQfXYPRpCnEdl62rIo9IRJruZZWkKKC-uAvhIEx4DmvjMvk-nOS-w4J2XAhPLhqAPndAObtDWBXuI4Ws0znpTKHzS0SpcZQno375PX2on0yq8mdiqc8p2QwVMGZdENWy6uYPlSEkJrkpr2zPZ8QYXc4fEBIzkOm2W17frtnI3bs9bbWUV3gDSnH19JVyBdOOnQqOF4orRlxA18QjqOxcOiHq4oSQsuhzH3C1BkcBBSwimCD-EqkPcHOF0bGoTKbekajOiLkgG6nQeoRQ0whJ1gRKd8XifIlvn9X09LixAhH7JOb4p3ecn-eK_GnyGJD6Ov3OsOV9CjWNia-wWQsFD92nJ33wZAfEJ1Nv056eGFkNi2oXTjoZTh1rKX-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احیا و حقیقت | قسمت دوم: ترکش
🔹
هواپیماها رفته بودند، اما میلیاردها ترکش هنوز در آسمان و بر زمین می‌چرخیدند...
🔹
درست در همان لحظه‌ای که کارکنان در حال تعویض شیفت بودند و محوطه از همیشه شلوغ‌تر بود.
🔹
همه‌چیز می‌گفت باید ده‌ها نفر آسیب می‌دیدند.
مسیر ترکش‌ها، تعداد افراد حاضر و منطق حادثه، همگی همین را فریاد می‌زدند.
🔹
اما آن روز، اتفاق دیگری رقم خورد؛
هیچ ترکشی به هیچ‌کس اصابت نکرد.
🔹
این فقط روایت یک حمله نیست؛
روایت لحظه‌ای است که در دل آتش و اضطراب، رخدادی شکل گرفت که بسیاری آن را فراتر از یک اتفاق معمولی می‌دانند.
🔹
روایت محمد جامعی از حمله ناجوانمردانه دشمنان آمریکایی‌صهیونیستی به زیرساخت‌های غیرنظامی ایران اسلامی در شرکت فولاد خوزستان
#از_نو_تو_را_آباد_خواهم_کرد
!
@khouzestan_steel_co</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/656437" target="_blank">📅 21:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656436">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
مجله نیروی هوایی آمریکا: حمله موشکی ایران پایگاه العدید را از کار انداخت
مجله نیروی هوایی و فضایی آمریکا:
🔹
در هفته‌های آغازین جنگ ۲۰۲۶ میان آمریکا و ایران، موشک‌های ایرانی خسارت شدیدی به مرکز عملیات هوایی ترکیبی (CAOC) در پایگاه هوایی العدید قطر وارد کرده و این تأسیسات را از کار انداخته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/656436" target="_blank">📅 21:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656435">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrbUPodwI1QADRoLn9dwtAKEeWE0wAQlOOsEaG47UXptjKpDrto9NVXt7uE1GCYzU_xL2A2-kYtxuF6Wptzo4zvLcRwjD4tGZhulirFvU0weQsdZIPolRRT2z5yfonuS6kzRUyVxYStFrWnYjOI1Zxs3Sa6R71YSZxu333GyYwsuyPXmzTQAPxkgF_5i1WYTQh9spIa2bGBgiqoE4S3XlRi_LbiKI0cigvemKbLbe1KsTC4mJG3yB2VF0GIS6sKKTuImBeO7ow98LcnaSRD9eALdn8Y2_4fxXSFsNgj7jXSz49z-07Pb94hpXBjm09tuhbWnXLd8LUpFKEMCMSrHdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زلزله در ترافیک اینترنت؛ بات‌ها از انسان‌ها جلو زدند!
🔹
بر اساس داده‌های جدید شرکت کلادفلر، برای اولین‌بار در تاریخ وب، ترافیک تولید شده توسط بات‌ها و ایجنت‌های هوش مصنوعی از کاربران انسانی پیشی گرفته است.  سهم بات‌ها به عدد شگفت‌انگیز ۵۷.۴ درصد رسیده است.
🔹
مدیرعامل کلادفلر این اتفاق را «غافلگیرکننده و بسیار زودتر از پیش‌بینی‌ها» توصیف کرده و گفته بود انتظار داشت این نقطه عطف حوالی سال ۲۰۲۷ رخ دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/656435" target="_blank">📅 21:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656434">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: ما در رابطه با ایران موفقیت‌های بزرگی کسب کرده‌ایم؛ آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/656434" target="_blank">📅 21:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656433">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7056189cc.mp4?token=Oxb-6nQHGdgrtoIPeLriJiRBI0hnpC2qIoLvKs5RuwJHk-WADxjKwslUV-mE3tT1vs9u3p44vbyhnoIgM1vZM0xN0QYBzIRKvcSKcn--gv8cT42znRuqEC7ro9QMEopxpBdd5A2Iw1a3fODOGai53v-qgy7foiZCK8q_0Lv3aAb_JUbhRfsbp7neEajnNIc_avjv0QhL8ygS8pOnydBg4UiUDn61JzNo-qMZUR5_KFDOsx115Bsd6z4LDLv05GKM-55VCLOR53dFzXKiuL_lXGWuHhRExTOKmezszPm0hwJz81CCSjeEVxSSMKQcosd5MkuOUr8DNPXdHl5o0vxYLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7056189cc.mp4?token=Oxb-6nQHGdgrtoIPeLriJiRBI0hnpC2qIoLvKs5RuwJHk-WADxjKwslUV-mE3tT1vs9u3p44vbyhnoIgM1vZM0xN0QYBzIRKvcSKcn--gv8cT42znRuqEC7ro9QMEopxpBdd5A2Iw1a3fODOGai53v-qgy7foiZCK8q_0Lv3aAb_JUbhRfsbp7neEajnNIc_avjv0QhL8ygS8pOnydBg4UiUDn61JzNo-qMZUR5_KFDOsx115Bsd6z4LDLv05GKM-55VCLOR53dFzXKiuL_lXGWuHhRExTOKmezszPm0hwJz81CCSjeEVxSSMKQcosd5MkuOUr8DNPXdHl5o0vxYLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: ما در رابطه با ایران موفقیت‌های بزرگی کسب کرده‌ایم؛ آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/656433" target="_blank">📅 21:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656432">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c2eddcb6.mp4?token=KtMNHvRXG59Km-SxulwNFvkTrU0DTLhxdhG-2y7f9T-fp2MQt2gZFY6gLGhn-A8uXUm9SMcg2lw0mKxF83bictelVz14ucW2cnqlKPrGzFYEe0zjcBh_lakdJW7D60TSiGrmFPPKQv0t9yh5n3uJSzXFw4fG3UgUDQlfoZwemRxm-e6jIxgGeMItqbFICcT1WOEot12wTKm_v0kX-W4x_e3x_C7Qj97fw4SB36z6IoisejCQjB8XrGCWHY0oxFFc-vZeDO0MURlsbKI3SSciaFSy5e7DNnxRtc4gAQAiYbCC1yhmvTptUHYV4St2dIEt_zrn-6sx2RqUPMAh10IaLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c2eddcb6.mp4?token=KtMNHvRXG59Km-SxulwNFvkTrU0DTLhxdhG-2y7f9T-fp2MQt2gZFY6gLGhn-A8uXUm9SMcg2lw0mKxF83bictelVz14ucW2cnqlKPrGzFYEe0zjcBh_lakdJW7D60TSiGrmFPPKQv0t9yh5n3uJSzXFw4fG3UgUDQlfoZwemRxm-e6jIxgGeMItqbFICcT1WOEot12wTKm_v0kX-W4x_e3x_C7Qj97fw4SB36z6IoisejCQjB8XrGCWHY0oxFFc-vZeDO0MURlsbKI3SSciaFSy5e7DNnxRtc4gAQAiYbCC1yhmvTptUHYV4St2dIEt_zrn-6sx2RqUPMAh10IaLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حقوق خنثی‌‌کننده بمب چقدره؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/656432" target="_blank">📅 21:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656431">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای نتانیاهو: توافق آتش‌بس با لبنان هنوز تکمیل نشده است
🔹
بنیامین نتانیاهو، نخست وزیر اسرائیل در نشست کابینه امنیتی این رژیم مدعی شد توافق آتش بس با لبنان هنوز نهایی نشده است.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/656431" target="_blank">📅 21:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656430">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAi7pQLZ6RMcvWctCPCRb__VfI5gVjVAYpn5Nr1stF8osy9aKqvQWTPWvjDy-rSxfUE-iCzz0--zDlb0r82ZWdepH5ECTNWl3u8iA7YZ9aq4sCIt6tGCGOe0VGmGHwI9J47CwrEbq2pAuaqy1YsXXdBCDRuFNch4sEVAhk11UnCd3URWa6zUGm85yAuJ3-JPdMRjdow7tfwzf8FWLX2j2u2MBuQ2Z3oTiSgBmp5Y-yIPiSpDDk74_cy_UYTCjvtdFUHoD1m1ddDqZ6mRa5Mfm2hPrTPrBibgGikuicpxNjzhM7TPDJKrCOSxNzBY7O21LzWPzb2SqnU199kl0uI1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح جدید فیفا برای مراسم پیش از بازی‌های جام جهانی
🔹
فیفا قصد دارد آیین پیش از شروع بازی‌های جام جهانی را با حضور تمام بازیکنان ترکیب اصلی و نیمکت دو تیم در اطراف دایره میانی زمین و همراه با پرچم‌های بزرگ دو کشور هنگام پخش سرود ملی برگزار کند.
🔹
به گفته رسانه فیفا، هدف از این تغییر، مشارکت همه بازیکنان فهرست تیم در این لحظه نمادین است.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/656430" target="_blank">📅 21:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656429">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8e4d50f1.mp4?token=kvOgVE0eUibEAsWGl6-Y7V7CZPtHGtQoeCu7eQGqPm2DUCqJQem_KDPvVAtK7IjrBolgJSYV-QQlOBLU4_mamOoWTwg5GF2OcQwk870whR9hhmbfKQaNS3XkOwel7B-6gtT-ts0QLmTvVs_Vc0Nso6zry2x1_4kiat7poPMOv37n_P_QiQt7ZJQI-m6bJkCeTY1WaOlTMZiW9dgIhSyc7qPcM3h9tATl_blmzgezMT1GS5b7CKIPnAKHDSSo9MHBAhXfL4kL2g9qdCRLErknSUt-AQeGGU0xu7IrgFYL-gzvTIExFOHWd4ITM-OLt0SdwwUBWXBbjYNqH6oLZkQJ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8e4d50f1.mp4?token=kvOgVE0eUibEAsWGl6-Y7V7CZPtHGtQoeCu7eQGqPm2DUCqJQem_KDPvVAtK7IjrBolgJSYV-QQlOBLU4_mamOoWTwg5GF2OcQwk870whR9hhmbfKQaNS3XkOwel7B-6gtT-ts0QLmTvVs_Vc0Nso6zry2x1_4kiat7poPMOv37n_P_QiQt7ZJQI-m6bJkCeTY1WaOlTMZiW9dgIhSyc7qPcM3h9tATl_blmzgezMT1GS5b7CKIPnAKHDSSo9MHBAhXfL4kL2g9qdCRLErknSUt-AQeGGU0xu7IrgFYL-gzvTIExFOHWd4ITM-OLt0SdwwUBWXBbjYNqH6oLZkQJ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای عمل نکردن بمب سنگرشکن در دفتر فرمانده فراجا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/656429" target="_blank">📅 21:05 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
