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
<img src="https://cdn4.telesco.pe/file/YSt5bCrQaN3c4xKmJwoWVmE6mymrCp_mEVXXt_BwjOlebRcMvRq5PIDPr9s1Rs8NODVopSEPklXmX9T9KZZ5vmBk7nrAdAhDgtcT-lcCO55twE9jJKi8DQoGwJR-fxYcjEeLUazcAYyamj1twUFB0970DwA9lf6pKGJMXwxduToHApuopTTnJ5Lk2gL4q0FZoF7nrYk5Jnv_oJ0qaSLZEk88fZbxWG50_t7zrWUXETrtebXER6quHD0p0L4E_kjWTAerMpkLVbZD_OHnw4qML0GjMs2yFtvdQQf9O_BUi6LaNHfKnbk7i_FXGMGPhDD4IKl1OCnaO_hiHZU2rFeyZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 12:21:40</div>
<hr>

<div class="tg-post" id="msg-675703">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d875a96f83.mp4?token=ufCbjgRoCLSO9d4MxXaiOntrG6VQ7fgl_VZzUvEpbBl6SufiN6nun9xvn7A8ppbi5JsfE0UtZxaYlkAKiW2Cgj7rvQhc8gNFgA7_TJuIvn44uByMwB-mbldVaJpyDVZbw_lLI5nMDnRWYTjLBxfdvSEhBl5ee7su5MSSCblaIXxPXYoq_qpbyTUxVC3ZFC7loBdkN2w0D9wyZL1SiyNYL6h_92IVJh8JtEkTgPhBg7HkXhfrWrw742bs4gtLYkeAQruE_yBmcHpbo38EKrJMeRza75OfXu39UdJ_Cm-fupNz0Q9HB0yFcB_Fcz_DntfszVSQeNSRkwZZqcz-SrbmXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d875a96f83.mp4?token=ufCbjgRoCLSO9d4MxXaiOntrG6VQ7fgl_VZzUvEpbBl6SufiN6nun9xvn7A8ppbi5JsfE0UtZxaYlkAKiW2Cgj7rvQhc8gNFgA7_TJuIvn44uByMwB-mbldVaJpyDVZbw_lLI5nMDnRWYTjLBxfdvSEhBl5ee7su5MSSCblaIXxPXYoq_qpbyTUxVC3ZFC7loBdkN2w0D9wyZL1SiyNYL6h_92IVJh8JtEkTgPhBg7HkXhfrWrw742bs4gtLYkeAQruE_yBmcHpbo38EKrJMeRza75OfXu39UdJ_Cm-fupNz0Q9HB0yFcB_Fcz_DntfszVSQeNSRkwZZqcz-SrbmXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منبع آبی که سند جنایت جنگی ترامپ است
🔹
تخریب منبع آب روستای کوهستک سیریک، زندگی هزاران نفر را سخت کرده است/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/675703" target="_blank">📅 12:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675702">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قبض برق مشترکان خانگی مشمول تخفیف ۳۰ درصدی می‌شود.
🔹
وزارت دفاع روسیه: روسیه به ۲ کشتی حامل محموله نظامی حمله کرد.
🔹
فرمانده نیروی زمینی ارتش: انتقام خون شهدا را می‌گیریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/675702" target="_blank">📅 12:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675701">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
عدم حضور سهام عدالت؛ مجمع هلدینگ خلیج‌فارس را از حد نصاب انداخت
🔹
مجمع عمومی عادی به طور فوق‌العاده شرکت صنایع پتروشیمی خلیج فارس، به دلیل عدم حضور برخی سهامداران عمده از جمله سهام عدالت، به حد نصاب قانونی نرسید و امکان برگزاری آن فراهم نشد.
🔹
بر اساس دیدگاه‌های مطرح‌ شده از سوی برخی ناظران، عدم حضور این سهامدار در شرایطی رخ داد که طی روزهای اخیر، علاوه بر حواشی و فشارهای سیاسی پیرامون مدیریت هلدینگ خلیج فارس، ابهاماتی نیز درباره وضعیت مدیریت و نحوه اعمال حقوق مالکانه شرکت‌های سرمایه‌گذاری استانی سهام عدالت و اختلاف‌نظر میان مراجع و دستگاه‌های مسئول در این خصوص مطرح بوده است. از نگاه این ناظران، این شرایط می‌توانست بر فرآیند تصمیم‌گیری مجمع سایه افکند.
🔹
بر همین اساس، برخی تحلیلگران معتقدند سهام عدالت با پرهیز از حضور در مجمع، ترجیح داد تا زمان رفع ابهامات موجود، شفاف شدن وضعیت مدیریتی و فراهم شدن شرایطی عاری از هرگونه شائبه، از اتخاذ تصمیم درباره ترکیب هیأت‌مدیره خودداری کند؛ تصمیمی که به اعتقاد آنان در راستای صیانت از حقوق تمامی سهامداران، به‌ویژه میلیون‌ها دارنده سهام عدالت و سایر سهامداران خرد، قابل ارزیابی است.
🔹
در این چارچوب، به حد نصاب نرسیدن مجمع را می‌توان نه صرفاً یک اتفاق اجرایی، بلکه نشانه‌ای از تأکید سهامداران عمده بر ضرورت حاکمیت شفافیت، ثبات مدیریتی، رعایت الزامات قانونی و حفظ منافع بلندمدت شرکت و تمامی ذی‌نفعان دانست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/675701" target="_blank">📅 12:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675700">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ec3b00a7.mp4?token=ng-IqIPjnW-ouUCgRifHngADddVnppXJw0NQ4eUhP0GnBwIKdBzSWcIWxI_rC6ozjivsGhUY1BzNvAdYDFPAi9_KaXMsW_X5eCNYwVxbtSs7Qz4BSA6OL2UlkHxdC5uZ60cpY9WadT0QofC5G-RHsbEmSHNPgnGmvtY4lPBwAfyWJOki3zsCmGsSGkxLIQyb19xop72tPuR0JllLNhpK3EmzOM6Gi_JdqIZ-Rn5Bv0Knwsqlml1LOI7guGY3ILHYSJouTpFNJKyeMMRpVYrDIPm27WzsA2-Pe3MbnVUKwg_C5PDXsB9ajPhYth_2tittmCjrlB7ib-j-Z0cBpWbQWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ec3b00a7.mp4?token=ng-IqIPjnW-ouUCgRifHngADddVnppXJw0NQ4eUhP0GnBwIKdBzSWcIWxI_rC6ozjivsGhUY1BzNvAdYDFPAi9_KaXMsW_X5eCNYwVxbtSs7Qz4BSA6OL2UlkHxdC5uZ60cpY9WadT0QofC5G-RHsbEmSHNPgnGmvtY4lPBwAfyWJOki3zsCmGsSGkxLIQyb19xop72tPuR0JllLNhpK3EmzOM6Gi_JdqIZ-Rn5Bv0Knwsqlml1LOI7guGY3ILHYSJouTpFNJKyeMMRpVYrDIPm27WzsA2-Pe3MbnVUKwg_C5PDXsB9ajPhYth_2tittmCjrlB7ib-j-Z0cBpWbQWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اطرافیان ما بیشتر از چیزی که فکر می‌کنید بر سلامت‌روان‌مون تاثیر دارن #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/675700" target="_blank">📅 12:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675699">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e834c6b9.mp4?token=pGiQRU_DgP8mCdziaG7Xol6A2jBoU-BVNEAxZfxcnVG-bF70A0Ur2lboVoxpok7caAAN2N-ovuHhPVGwVZp47wWgZfzE7xfb3ivUbgWvEDBDAvfGZWKw1Dx4klfS8RbuGPFBqQwPmBCLxFh7er3gf4aQj_OuMq97Q967X-W6wOTrCyqOcP9Lfah7x18GpCh0UIAgq17da7MD68KNxIVuhn_FL2NqRsRPUVm72hX0Ir5hljv1YHhW8KQu0CeRgMmfLfsi43I7aF9sQgavwZJApJxnBHUbP3UPEOIjNT6bTdOkJffl5POD8mn4CzEsUcFgGYPYk6Mz6CKH1ekoJfrN5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e834c6b9.mp4?token=pGiQRU_DgP8mCdziaG7Xol6A2jBoU-BVNEAxZfxcnVG-bF70A0Ur2lboVoxpok7caAAN2N-ovuHhPVGwVZp47wWgZfzE7xfb3ivUbgWvEDBDAvfGZWKw1Dx4klfS8RbuGPFBqQwPmBCLxFh7er3gf4aQj_OuMq97Q967X-W6wOTrCyqOcP9Lfah7x18GpCh0UIAgq17da7MD68KNxIVuhn_FL2NqRsRPUVm72hX0Ir5hljv1YHhW8KQu0CeRgMmfLfsi43I7aF9sQgavwZJApJxnBHUbP3UPEOIjNT6bTdOkJffl5POD8mn4CzEsUcFgGYPYk6Mz6CKH1ekoJfrN5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
#تماشا_کنید
💎
تسهیلات
طرح کارنو بانک تجارت
ابزاری ویژه برای حمایت از کارکنان شرکت‌ها
🎯
سبدی از خدمات متنوع اعتباری برای نیازهای گوناگون
🔗
تا سقف ۲ میلیارد و ۴۵۰ میلیون تومان تأمین مالی
📌
📞
برای اطلاعات بیشتر به شعب بانک تجارت مراجعه کرده و یا با مرکز ارتباط مشتریان این بانک به شماره ۱۵۵۴ تماس بگیرید.
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
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/675699" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675698">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS851S0oo50hpnfdWqvlWbW-loPztp7VY9YmVLttRDgHLWWp9WpH5DjvbGVCWBhhtsH5Jw-v-gz866ej_ZnrWlhVx1Mb9L2ivXweyYwhqBfV80R_Up93r9im2FNX_so8JwqozeDeO5AljO1mGP_m8ENYQgoLJ4zn3nUbnHy90oMUalE3rxQw8-7Nen2OSzNuZcHWCOLVzzsBwSJN3y2bUS97I6OUoSSmOGTtcGSRnLq8PY6pWSafgpuGcNbEJV9_19GOWOVSeBis4J_guo8iuy1R7tOYJGyfAYfuva_1veYHLu8UqxPzXpGajHAtaylSbCAjK4Mcv3nr-Ml3Sl-hkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پژوهش جدید: دمای هسته زمین ممکن است تا هزار درجه سانتی‌گراد کمتر از برآوردهای پیشین باشد؛ یافته‌ای که می‌تواند راز پایداری میدان مغناطیسی زمین در میلیاردها سال گذشته را توضیح دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/675698" target="_blank">📅 11:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
بقایی: هرگونه اقدام آمریکا با پاسخ قاطع ایران روبه‌رو خواهد شد و گفت در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست و تنها گفت‌وگوها با عمان درباره تنگه هرمز انجام می‌شود
🔹
آمریکا باید یاد بگیرد مثل یک دولت مسئول عمل کند. رفتار آمریکا در این یکی دو سال شبیه یک باند مافیایی است که به هیچ قاعده و قانونی پایبند نبوده است و هم در گفتار و هم رفتار همه هنجارهای حقوق بین‌الملل را زیر سؤال برده و نقض کرده و قطعا تا زمانی که چنین رفتاری از آمریکا ادامه داشته باشد نمی‌توانیم امیدوار باشیم به شکل‌گیری یک روند معقول.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/675697" target="_blank">📅 11:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3801908a2e.mp4?token=gI452buSwAuHmkCy2z2Nwz2hCcO973LDhLq1YPYKbVOGuXUmGog7i-D0WMeM7EVoS_x-YiQFtb7MrmDcW9322vcECYy7n_EQnMfYv2fcw2qtwHL_lHLDiAjly2gPIftxD2URcMV940zl7zBjySZnklzpKhl2MyrCkYJvhVPlA6y8-Kpg009y1LRkHFbJXUlTfb8FVhKKU4MXH9egR-23ggRu3x2KPmk_jFXi-3mPneASaU8AaN_MiXFzOaxwVBRWFrj_9ZtW7hJ-A0-mytxV0iExChDm_PguFe26sAW-8iG6Ei7hIm_Zf42JJ68croWrYB0m8YPxYILvHvsKF-49cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3801908a2e.mp4?token=gI452buSwAuHmkCy2z2Nwz2hCcO973LDhLq1YPYKbVOGuXUmGog7i-D0WMeM7EVoS_x-YiQFtb7MrmDcW9322vcECYy7n_EQnMfYv2fcw2qtwHL_lHLDiAjly2gPIftxD2URcMV940zl7zBjySZnklzpKhl2MyrCkYJvhVPlA6y8-Kpg009y1LRkHFbJXUlTfb8FVhKKU4MXH9egR-23ggRu3x2KPmk_jFXi-3mPneASaU8AaN_MiXFzOaxwVBRWFrj_9ZtW7hJ-A0-mytxV0iExChDm_PguFe26sAW-8iG6Ei7hIm_Zf42JJ68croWrYB0m8YPxYILvHvsKF-49cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: اقدام نظامی آمریکا علیه زائران مشهد الرضا و زائران اربعین حسینی معنادار است‌ / آمریکا از روی استیصال در ۱۰ روز اخیر علیه زیرساختهای غیرنظامی انجام داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/675696" target="_blank">📅 11:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f4ecd59a.mp4?token=BZ5uKB3WGpw6STvqM0mV8HNtRqozAt-8oUHDOAdTSK_r_ukSvZp7gVV-9osv9OPy7M3AxCO2ErqSCgFV0sOm2rBifSuNRrhBfxAFPI9Nkv6gPQAear_afgw08xnqDq_G1-e5fQg6Huu14XSN49_3TERB_ofXQAjo8HVY0p_-IoLmaEg1nsaCZdOJgiRP-09GjLK6pfv5TICjOTlT1wqNL36CQ9XZVPQeGnAT-G9m-mI9X-yHc72J4TL6V1ShIjgiUZC-vg0J99TOG0pmQTCpSbWtQfx-Dy9OLQe3zrOPHBrBQyyzvuP3s2bXb3orMkXHmt2iXXaayPCB9PZxe1nbBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f4ecd59a.mp4?token=BZ5uKB3WGpw6STvqM0mV8HNtRqozAt-8oUHDOAdTSK_r_ukSvZp7gVV-9osv9OPy7M3AxCO2ErqSCgFV0sOm2rBifSuNRrhBfxAFPI9Nkv6gPQAear_afgw08xnqDq_G1-e5fQg6Huu14XSN49_3TERB_ofXQAjo8HVY0p_-IoLmaEg1nsaCZdOJgiRP-09GjLK6pfv5TICjOTlT1wqNL36CQ9XZVPQeGnAT-G9m-mI9X-yHc72J4TL6V1ShIjgiUZC-vg0J99TOG0pmQTCpSbWtQfx-Dy9OLQe3zrOPHBrBQyyzvuP3s2bXb3orMkXHmt2iXXaayPCB9PZxe1nbBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدرالحسینی، کارشناس روابط بین‌الملل: تکرار درگیری با ایران می‌تواند شرایط را برای رژیم صهیونیستی بحرانی‌تر کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/675695" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه درباره مذاکرات ایران و عمان: چند دور مذاکرات درباره نحوه مدیریت تردد کشتیرانی در تنگه هرمز در روزهای جمعه و شنبه برگزار شد
🔹
تأکید می‌کنم وضعیت تنگه هرمز هیچ تغییری نکرده و به دلیل اقدامات تحمیلی آمریکا کماکان تنگه هرمز بسته است و این…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/675694" target="_blank">📅 11:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675693">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
بقایی: در حال حاضر هیچ مذاکره‌ای با طرف آمریکایی نداریم
سخنگوی دستگاه دیپلماسی:
🔹
درخواست مذاکره از سوی ایران خبرسازی است. ما همیشه گفته‌ایم هیچگاه از استفاده از ابزار دیپلماسی برای صیانت از منافع ملی فرار نکردیم دیپلماسی را ابزار برای حفاظت از منافع ملی ایران می‌دانیم همزمان به هیچ عنوان هیچ اقدامی را انجام نخواهیم داد که طرف مقابل برداشت ناصحیحی از آن کند.
🔹
میانجی‌ها ممکن است پیام‌هایی را منتقل کنند در خصوص تحولات جاری، ولی در حال حاضر هیچ مذاکره‌ای با طرف آمریکایی نداریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/675693" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675692">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d195aae53.mp4?token=Qz1vQu8Ryuu4Z0uKt63G7gyNS44kxFcL-myyCYcg3O2b6qjpUxCDkbWGcINdDbd0JJvSMTYCqeVmqG8qeCF3_dBCRqgsNKs1ZkxhygR4mjME41m3BAAohAHeuNQ9xSFEgavWUJpPAP-SJH8-Q94X2ZxqRE1pVSip4BQr1opHiXdOMndCE_KckpyAON7H0J8JRtbckLweSxf1yPE369aPiRtdUVeYkBU99T5nL_QcKNokqyfxCMJHSgwar_8Hn8ZEE3H4VucF7MLY0zsmmBp6h6f09rNFkm9L8NvxZa6B_d-2ny293i76YJe59yxVAh_uEjGSVfn0vKcWOoVuzCOeaHRq_t_hAALJXbDKRmvwTKbn7BZNopd2PqibaThzHjYsjrCJiwmla69jUiWewoD-kEY5fOKHN1oTcSNdYbs3fhFCrkoELhNcwIqEpgLna5w79y5X7HwQ8_L5k4LpRm7Mw3qVUEW43R691-RwbLzW5faIoiIJM393YFMQhN5THFb7A6drzzVryjB3KyjN8XFh2djnkSrWR8O-fcCxb5--Ic6MkNob79gHr-BauIpR9b1gIs6Ous9c_vQn2tDJOg1q1BMdm381tuKR96o47BuI9qf_e-Coi6dD6LeCIIg5cfeNoZ5Bh73ZsgM1XPIFJRLReL03rj2aak6HKt71U8hyFpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d195aae53.mp4?token=Qz1vQu8Ryuu4Z0uKt63G7gyNS44kxFcL-myyCYcg3O2b6qjpUxCDkbWGcINdDbd0JJvSMTYCqeVmqG8qeCF3_dBCRqgsNKs1ZkxhygR4mjME41m3BAAohAHeuNQ9xSFEgavWUJpPAP-SJH8-Q94X2ZxqRE1pVSip4BQr1opHiXdOMndCE_KckpyAON7H0J8JRtbckLweSxf1yPE369aPiRtdUVeYkBU99T5nL_QcKNokqyfxCMJHSgwar_8Hn8ZEE3H4VucF7MLY0zsmmBp6h6f09rNFkm9L8NvxZa6B_d-2ny293i76YJe59yxVAh_uEjGSVfn0vKcWOoVuzCOeaHRq_t_hAALJXbDKRmvwTKbn7BZNopd2PqibaThzHjYsjrCJiwmla69jUiWewoD-kEY5fOKHN1oTcSNdYbs3fhFCrkoELhNcwIqEpgLna5w79y5X7HwQ8_L5k4LpRm7Mw3qVUEW43R691-RwbLzW5faIoiIJM393YFMQhN5THFb7A6drzzVryjB3KyjN8XFh2djnkSrWR8O-fcCxb5--Ic6MkNob79gHr-BauIpR9b1gIs6Ous9c_vQn2tDJOg1q1BMdm381tuKR96o47BuI9qf_e-Coi6dD6LeCIIg5cfeNoZ5Bh73ZsgM1XPIFJRLReL03rj2aak6HKt71U8hyFpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از حمله آمریکا به شناورهای صیادی کوهستک سیریک
🔹
منبع درآمد بیش از ۱۰۰ خانواده، در آتش حماقت‌های ترامپ سوخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/675692" target="_blank">📅 11:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675691">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ارتش اسرائیل مدعی انهدام ۲ پهپاد در مرز اردن شد
🔹
گزارشی درباره منشأ این پهپادها منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/675691" target="_blank">📅 11:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675690">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f77b10de2.mp4?token=E8QnuaXfkT7T_bmKMDNBtayhwkgbQWvGMCdEso9jLMYacz2PleBVnepfHPdDFMRc5u3IJC1bixx2BQ3TdBRdiotdKDPFU1I6IdZ8hihjJubqbJC87PLu3CfvzG62toxAsMIN2ncFRPrvp84ZSb3wzYtT8TRl62xotS1b9EWx7jfQLc-vCg-w2lZ1a5tFwvhfUZMkEljzffD_jQqPwCqFnhtqUSDFsEpMoV4nuRr1BisrcKnrzV0-C13UgFuUg7ncloXsiD2gCuYoDk4o8H6jQDRCM9qe-xFz_Nzv6mc3ABiJ9Jq2vudJCjNMedkiHQSx90hppu6gR7CVENt24iVabA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f77b10de2.mp4?token=E8QnuaXfkT7T_bmKMDNBtayhwkgbQWvGMCdEso9jLMYacz2PleBVnepfHPdDFMRc5u3IJC1bixx2BQ3TdBRdiotdKDPFU1I6IdZ8hihjJubqbJC87PLu3CfvzG62toxAsMIN2ncFRPrvp84ZSb3wzYtT8TRl62xotS1b9EWx7jfQLc-vCg-w2lZ1a5tFwvhfUZMkEljzffD_jQqPwCqFnhtqUSDFsEpMoV4nuRr1BisrcKnrzV0-C13UgFuUg7ncloXsiD2gCuYoDk4o8H6jQDRCM9qe-xFz_Nzv6mc3ABiJ9Jq2vudJCjNMedkiHQSx90hppu6gR7CVENt24iVabA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرز تهیه یک فرزند مضطرب/ چه رفتارهایی از جانب والدین منجر به ایجاد اضطراب در کودکان می‌شود؟
/ تلویزیون اینترنتی مدار
این برنامه را در آپارات ببینید
👇
▫️
https://aparat.com/v/nalwl41
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/675690" target="_blank">📅 11:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675689">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: فرانسه با پوشش سفارتخانه و به‌بهانهٔ ارتباط با جامعهٔ مدنی در امور داخلی ما دخالت کرده و باید عذرخواهی کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/675689" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675688">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2b72f70b.mp4?token=a07wCi3LzMykTdvrO8odQyRSVKv1NDcbHL_h3pYQQlwLIkBdanBeqDqsYROLKueFSHDDMUg5M-BwqCv-sp9363dSvBSm_FDiaq2nDUjNiD-Qd0gEQb1MwUnulkYrhmv3gkVHbh3jIn_kUYGfuGpJskfR3BIQNT7UAkbqDpzvTs2IndjwF1EVBLRf3DIqJatXApOYSgKWoIJZeGaIs_bCQw9K5UjUzbKh75cAPRXvYatCPOnlFykuiL5nd2nNkCf1dDhGe3HJaVWFWU2hcZwM_Nsofnd8---Dsm-Gunmya13uL1pKxQ2_2ffX8Iwbw-ojKt-Tn99EaSDNRpOI3rt0iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2b72f70b.mp4?token=a07wCi3LzMykTdvrO8odQyRSVKv1NDcbHL_h3pYQQlwLIkBdanBeqDqsYROLKueFSHDDMUg5M-BwqCv-sp9363dSvBSm_FDiaq2nDUjNiD-Qd0gEQb1MwUnulkYrhmv3gkVHbh3jIn_kUYGfuGpJskfR3BIQNT7UAkbqDpzvTs2IndjwF1EVBLRf3DIqJatXApOYSgKWoIJZeGaIs_bCQw9K5UjUzbKh75cAPRXvYatCPOnlFykuiL5nd2nNkCf1dDhGe3HJaVWFWU2hcZwM_Nsofnd8---Dsm-Gunmya13uL1pKxQ2_2ffX8Iwbw-ojKt-Tn99EaSDNRpOI3rt0iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدرالحسینی، کارشناس روابط بین‌الملل: اگر اروپا در اقدامات آمریکا علیه ایران همراهی کند، جمهوری اسلامی آمادگی پاسخ متقابل را دارد/ تهدیدهای ایران در مورد برخی کشورهای اروپایی معتبر است و توانایی داریم که پاسخ دشمنی آن‌ها را بدهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/675688" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675687">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c98f25ef.mp4?token=OxvXRssvJhJ2jOOSsASGw9cRic-1NYCDb8Mi-tr50gpqoaWSwWIJa_B5ofWl45Su4DWEkJd83zes7nJHxPfYuUa46wjEEzNhvvbg_8-r2XqtO6_DnxFANyN1bT6jpSJJ8lZYZlbDa20MMZzDKT0wGaMR7k3CNrc5U9h6Ev-iny7DL5ObSs3d4uIHzDH_XsKR-qMkZDS2i_7Uzh4EktpVKS5fVHAgX0Csrzj_qbywiuu60UJ-3g0Ls7LTxWN6IWbGZqQ0-viZOcoorCqHKgSCelYS5Ao64ltr6UzIwL5ZLH35ThgPFtfuQsSWvmnF490NF4bqyPU2jFadehMtyTIJYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c98f25ef.mp4?token=OxvXRssvJhJ2jOOSsASGw9cRic-1NYCDb8Mi-tr50gpqoaWSwWIJa_B5ofWl45Su4DWEkJd83zes7nJHxPfYuUa46wjEEzNhvvbg_8-r2XqtO6_DnxFANyN1bT6jpSJJ8lZYZlbDa20MMZzDKT0wGaMR7k3CNrc5U9h6Ev-iny7DL5ObSs3d4uIHzDH_XsKR-qMkZDS2i_7Uzh4EktpVKS5fVHAgX0Csrzj_qbywiuu60UJ-3g0Ls7LTxWN6IWbGZqQ0-viZOcoorCqHKgSCelYS5Ao64ltr6UzIwL5ZLH35ThgPFtfuQsSWvmnF490NF4bqyPU2jFadehMtyTIJYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه خطاب به اتحادیهٔ اروپا: شما که هرازچندگاهی به بهانهٔ حقوق بشر بیانیه‌ای علیه ایران صادر می‌کنید! آیا کودکان میناب ایرانی نبودند؟!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/675687" target="_blank">📅 11:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675686">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599dbc5f5b.mp4?token=V7eTuzUDwRC89aw0MCojsIc4RBoXrsIiSCmJ8GO9XrIjkB5CzFdHpwwFA5QgUTdTTXPTDWE2O5iIbP8QHsEbmLW5gilR4enaC3_ckDuRrP385IKfuoW2Dvqausj43vcxoDXITdsSRXstMhBoPogJrwIV6oOCS6_M8bJ56MgloJs1h9GN8PNDpaQdIwja63WbpQ7OkLg1KV8TKDC2jgE48oksXkmcTU3stDneNgeajGxRI1k3hLaugDjCFWxai8RiAyuq3RoMeZSHOklreIdKsQ2Dp_lf9aJHJJOTGrjtYuA0T3l3hXLsjUrQK0zA2mYTTIDZtv8BoX58YI6CCr9FaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599dbc5f5b.mp4?token=V7eTuzUDwRC89aw0MCojsIc4RBoXrsIiSCmJ8GO9XrIjkB5CzFdHpwwFA5QgUTdTTXPTDWE2O5iIbP8QHsEbmLW5gilR4enaC3_ckDuRrP385IKfuoW2Dvqausj43vcxoDXITdsSRXstMhBoPogJrwIV6oOCS6_M8bJ56MgloJs1h9GN8PNDpaQdIwja63WbpQ7OkLg1KV8TKDC2jgE48oksXkmcTU3stDneNgeajGxRI1k3hLaugDjCFWxai8RiAyuq3RoMeZSHOklreIdKsQ2Dp_lf9aJHJJOTGrjtYuA0T3l3hXLsjUrQK0zA2mYTTIDZtv8BoX58YI6CCr9FaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجمع عمومی عادی بطور فوق العاده فارس به حد نصاب نرسید
🔹
مجمع عمومی عادی بطور فوق العاده شرکت صنایع پتروشیمی خلیج‌فارس که بنا بود بعد از مجمع عمومی فوق العاده این شرکت برگزار شود به دلیل به حد نصاب نرسیدن به تعویق افتاد.
🔹
به دلیل آنکه کمتر از پنجاه درصد سهامداران در این مجمع شرکت کردند(۴۳.۹ درصد) بر اساس قوانین و ضوابط موجود، این مجمع تشکیل نشد.
🔹
گفتنی است مجمع عمومی فوق العاده فارس از ساعت ۹ تا ۱۰ صبح امروز پنجم مرداد با حضور ۷۸.۸ درصد سهامداران برگزار شده بود.
🔹
زمان جدید این مجمع متعاقبا اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/675686" target="_blank">📅 11:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675685">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
واکنش سخنگوی وزارت امورخارجه به حمله اوکراین به یک کشتی تجاری ایران   بقایی:
🔹
کسانی که پیشتیبان دولت اوکراین هستند باید پاسخگو باشند. تبعات اینگونه اقدامات غیرقابل پیش بینی خواهد بود .
🔹
پیامدهای این اقدام می تواند شامل بخش های مختلف دنیا شود و کشورهای حاشیه…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/675685" target="_blank">📅 11:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675684">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه خطاب به اتحادیهٔ اروپا: شما که هرازچندگاهی به بهانهٔ حقوق بشر بیانیه‌ای علیه ایران صادر می‌کنید! آیا کودکان میناب ایرانی نبودند؟!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/675684" target="_blank">📅 11:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675683">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91ffff6f6.mp4?token=Kb3pDvpMHK7jLSUscAsNShEq8iNyCcXzs5PVGrWHsMIkpYHMmGsBCU42Fva1l-5Q3yJl7mftzvVOKYe0dp5SbHFTjM4xMsg3wQVwNp_QBAFUMMeTysM1inESezPF1WJr9124WIM5BRvsac3zqc3C-yNWl_AlisloQa62l5ynW1fyhAlB9V0c6uVbGKyZI9w2ehSgdm0VvXEu5E9BOqSu07v51H1mAwzknpZ2BXibM8AmFdKkp_Xm9uoHLRsxp6gRrWnMb23z7kBGccIn0bUYNa_BWOOFYs6oWTGjZZaJwZd85TQqHRkmkuh2LsRkOHJNkfLCWsfGuU0IXwuzZG7nnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91ffff6f6.mp4?token=Kb3pDvpMHK7jLSUscAsNShEq8iNyCcXzs5PVGrWHsMIkpYHMmGsBCU42Fva1l-5Q3yJl7mftzvVOKYe0dp5SbHFTjM4xMsg3wQVwNp_QBAFUMMeTysM1inESezPF1WJr9124WIM5BRvsac3zqc3C-yNWl_AlisloQa62l5ynW1fyhAlB9V0c6uVbGKyZI9w2ehSgdm0VvXEu5E9BOqSu07v51H1mAwzknpZ2BXibM8AmFdKkp_Xm9uoHLRsxp6gRrWnMb23z7kBGccIn0bUYNa_BWOOFYs6oWTGjZZaJwZd85TQqHRkmkuh2LsRkOHJNkfLCWsfGuU0IXwuzZG7nnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: آمریکا تعیین کننده زمان جنگ و صلح نیست  بقایی:
🔹
جنگی که قرار بود ظرف ۳ روز باعث فروپاشی ایران شود، حالا بعد از ۵ ماه دشمن همچنان نتوانسته اهدافش را محقق کنند؛ این نامش مدیریت جنگ نیست.
🔹
تا وقتی منافح ایجاب کند دفاع خواهیم کرد و هر…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/675683" target="_blank">📅 11:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675682">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbb8512399.mp4?token=ClGxzAKEnOvijMYWw2Ztjz9ALgy5twMCb9kaD4ELVuM-Onv29IN32uaSWxV23XakOFZqny6zcmm7VV4vAct5k3eBCoZaDKHJ-3IG9k15T7ZZoMbtIbvgYizDP0LsMbFTo-mzgcYaIBCC5CHU_KeEL82jDavXw-xNHci2zd3gt6whwDevlZSuYlxWYErGuD0cFIT2KYf8dPP20RG4-oNhCNp47iNmp-a4ZhAkYOQr-Ot3RjGhZ4GgKHhs_Z9QQSUNqbJpEhvs95dqSDjgjtejrvAgSH2SNYMHEd3enZ_RFXpj7tcaEf_rQOBH9SADhs5htspiNckUM2EYS-njMR2ytw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbb8512399.mp4?token=ClGxzAKEnOvijMYWw2Ztjz9ALgy5twMCb9kaD4ELVuM-Onv29IN32uaSWxV23XakOFZqny6zcmm7VV4vAct5k3eBCoZaDKHJ-3IG9k15T7ZZoMbtIbvgYizDP0LsMbFTo-mzgcYaIBCC5CHU_KeEL82jDavXw-xNHci2zd3gt6whwDevlZSuYlxWYErGuD0cFIT2KYf8dPP20RG4-oNhCNp47iNmp-a4ZhAkYOQr-Ot3RjGhZ4GgKHhs_Z9QQSUNqbJpEhvs95dqSDjgjtejrvAgSH2SNYMHEd3enZ_RFXpj7tcaEf_rQOBH9SADhs5htspiNckUM2EYS-njMR2ytw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجمع عمومی فوق‌العاده شرکت صنایع پتروشیمی خلیج فارس آغاز شد
🔹
مجمع عمومی فوق‌العاده شرکت صنایع پتروشیمی خلیج فارس امروز دوشنبه ۵ مرداد ۱۴۰۵، با حضور ۷۷.۷ درصد از سهامداران و نمایندگان قانونی آن‌ها در سالن همایش‌های بین‌المللی ارم تهران آغاز شد.
🔹
این مجمع با هدف  قرائت گزارش بازرس قانونی در مورد پیشنهاد افزایش سرمایه هیئت مدیره، اصلاح ماده ۷ اساسنامه مرتبط با میزان سرمایه و تعداد سهام و بازنگری در فعالیت‌های فرعی شرکت برگزار می‌شود.
🔹
لازم به ذکر است که در راستای تسهیل مشارکت سهامداران و طبق ابلاغیه سازمان بورس و اوراق بهادار، امکان شرکت مجازی و طرح سوالات از طریق سامانه «
mymajma.com
» فراهم شده است تا سهامداران بتوانند به صورت برخط در روند تصمیم‌گیری‌های شرکت سهیم باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/675682" target="_blank">📅 10:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675681">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: آمریکا تعیین کننده زمان جنگ و صلح نیست
بقایی:
🔹
جنگی که قرار بود ظرف ۳ روز باعث فروپاشی ایران شود، حالا بعد از ۵ ماه دشمن همچنان نتوانسته اهدافش را محقق کنند؛ این نامش مدیریت جنگ نیست.
🔹
تا وقتی منافح ایجاب کند دفاع خواهیم کرد و هر زمان که لازم باشد از ابزار دیپلماسی استفاده خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/675681" target="_blank">📅 10:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675680">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcddfc84d.mp4?token=IIsN9FzXGbxdDZ06urXu-lPOXfkHu8sBfIr9NefZXg5uxSxpPYk5_oDfpEthUzvmz5Rdhb-9Fq1LMP1sRUr3NlzaNjFh-maS-yRoEfnKZVcMQLkE9FWC9uiyH_hFC5knP3MrLVW2GefwuQrgtOQWLVUpXMSsbT_ZfAvGayOpvlUOXc_lo7wxy3v6gv328EtjYRJ5G1jgEomi1Jjqck7RG-KDwoFLd_D3ALfqaNsiKLD1-YiUebpRaIAd-jPhJbf22ppdlDMue79ob09xtpsNTvprb4xwzIBOQlwKRQotZB93QzcXMZMbrT_Af5hGz9XriZf7VnxAzRbApIA-ii8U7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcddfc84d.mp4?token=IIsN9FzXGbxdDZ06urXu-lPOXfkHu8sBfIr9NefZXg5uxSxpPYk5_oDfpEthUzvmz5Rdhb-9Fq1LMP1sRUr3NlzaNjFh-maS-yRoEfnKZVcMQLkE9FWC9uiyH_hFC5knP3MrLVW2GefwuQrgtOQWLVUpXMSsbT_ZfAvGayOpvlUOXc_lo7wxy3v6gv328EtjYRJ5G1jgEomi1Jjqck7RG-KDwoFLd_D3ALfqaNsiKLD1-YiUebpRaIAd-jPhJbf22ppdlDMue79ob09xtpsNTvprb4xwzIBOQlwKRQotZB93QzcXMZMbrT_Af5hGz9XriZf7VnxAzRbApIA-ii8U7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله زنبورها فینال فوتبال را متوقف کرد
🔹
یک اتفاق عجیب و کم‌سابقه، فینال رقابت‌های قهرمانی ایالت باهیا در رده زیر ۲۰ سال برزیل را برای دقایقی متوقف کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/675680" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675679">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4de6a51b.mp4?token=hsYuEGUxZJbFtiodAxJWanDK9fnL1xNxDxBu1knj-nnd_VObGyjGR-Y749WpVCwdhS1Gynus4EJO6HLR55r-v_myPsofSqzbQAC34cHr2jjldluFivyPk9fsmnhh9j92Mn2isFrI_IjcSKg2HLf72dRU_vnhjU_WX1ylJObrHqAuT7Qx8yd4ti2-EkrifX2uYCuv62y5IvaWoaAwecLUOBcfVe2oHUevI8IrJqHXjbRGJhteraUfz80l2Oqb8pLpR-gvTibqt9sFh9N2ZqFV0mnSvz5kWZDM8XDfHZuL0YicJZawZ-Z6Zlx1KmTtVoFZ7oa-R5MONhmhxIcuwWsHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4de6a51b.mp4?token=hsYuEGUxZJbFtiodAxJWanDK9fnL1xNxDxBu1knj-nnd_VObGyjGR-Y749WpVCwdhS1Gynus4EJO6HLR55r-v_myPsofSqzbQAC34cHr2jjldluFivyPk9fsmnhh9j92Mn2isFrI_IjcSKg2HLf72dRU_vnhjU_WX1ylJObrHqAuT7Qx8yd4ti2-EkrifX2uYCuv62y5IvaWoaAwecLUOBcfVe2oHUevI8IrJqHXjbRGJhteraUfz80l2Oqb8pLpR-gvTibqt9sFh9N2ZqFV0mnSvz5kWZDM8XDfHZuL0YicJZawZ-Z6Zlx1KmTtVoFZ7oa-R5MONhmhxIcuwWsHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک: رژیم صهیونسیتی از صبح امروز حملات توپخانه‌ای را علیه جنوب لبنان آغاز کرده است/ در این حملات ۵۵ شهرک در جنوب رودخانه لیتانی کاملا از بین‌ رفته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/675679" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675673">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mr6LIolZ_avJmfhdz2BFOPneqDk_lYPx-hKto9q0CXgtVqokOen1PvlpiJgpTeyQxmA7C6YTGmj7DE4CPO5FuC35wWIqLwnJyiXL2RZLiJML1Os2UciLgyr23WqNWvJ0z6Katx2XGnvUXsu_0jwRxsLgD6L9i6unFIcwvot-67MuPhe1qVMb4xExTomvKjP_4SGxGwg1USOKnchy4uL-YoEuCS4naPu-1UFV33hh1kLr24KLXQIoCKg2XtAmx9YOIQQwvvPj0t3AUZO8hT7X0vDgQM8np-hje8sGAynBknRaJ2rDWWvnvYWb64wg9_a0vLMMnASIBISUG-CGOd0E1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bs7N2z9MdFAIfZ3h-j313Nze4OHTmucY36yN6so9ZUK9PMU6cR0vIKsZL6XdNK5RtkV3FnCYP-1tX_a8LSrTvFHlUmLr0J-uKjfo9cd8UwupXJii14qdqmFl9yQw4o3kLSl0d7aywUATBNVlxDG6p8SiWmpQ5ThTnb-p3DG5KUvvHiPUdS1nwq8_D8-Cnj6KSVK0Imc5h7PfPrZDOM6dh7-2MGxChMw7ujktwHPoudNM9wFPbldgS9P1xqQUIC6VIxlhl3ghjJ5WnYWxS3-cbIW50DsXTjCqSQPHP4LD0pmCW_YEOHygGn4FOCtxlNCtMGyLSS67UEBs-uXzHnXl5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tv_3xdsSFZQ79rnvYu7EDuqlqVIwu3rXWXQmmJa3NGbNxR975i8RhWhEQwU7CBarvbhLT-VztaoGSJxHC9PLyXbx6Tc-R_a0y3C7wUz_WJRpfX8EYGbubio0RgFUENKvOGXsqPyCC7igaq5O52djJEhMaYWkD2KEnvFfh_MLMk3GtSBB2wuJ4CSV5yhHGih3q0-6KsaJCAOnBUfQ5OXW-Sen2HRu9Y8Kqy1dMCTjsk1i6j-311mRJ0ZOF0mb0bHjri8A8FjAoItST7iBPeId-APLnHd_2KmsKIplG4HCwSVUudStghBAz9ZSKnKU_E0rZVP-OY31ZByXlirYpFMp9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V12opmBlkYy2xN77g3vJhwDcq3_e-SdYIh5IJi4OdybKcNkI0wG9BAC_0zIbqctqhAAYm4LyLF5h7f3eFy-d_N91xqHe6E1IB2Gibm5sHA2g1PNRdo6AIuer-C8emwUIm9PTHXERO0D7U5R-f76ZevCSVGrTEFmiGxQUAU6vONOhZPGB8PYWvSj_TbD8CzaCju7J_j9MOe_GBRGag_XBGiKYEyMvdQ_BcAwDnCu7tiA6c5JNrVMoHryJ8tXgv2w4fNyhqSdiGsk1W4Icr8Vwgb7bERG-IjeO_C6CH-uue9ISU7G3_rr4-1Qqu8ViLl_ztPqUnhgNkZf3KbgyQY_mhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbiz-4wGXZTYZKwQLjmwe4DjieHjJtqhcN3PMzs-5XpfPtkPn2H4ARF5YJ4AKe9Q2PTLHTlAoKkPTuXBcH6OnpUhZ0cs12ThRgPj9VONSGu_8kJuQZYLMxGC4TzdQ0vvdjugjlGCvX7OSe1qnMhypC4Yn6-LlmBZDhZMgnFIIpDKNwQknMIrhxVIc7VC0yYi_FOdfzM4CrfxVhzkJiirZBnjE4nsgi-pfCAFCDwt2xn5eRaSpUkRf1T77rgTLBAH3khKgI-M07EUYItDXqR6G_MsiOv547pgqU3CrUbZzVrjynSTI6BQlRnxWlO6VEYaojMhD68AH7W092EDuG-mGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KG3QeU6B8N-tdrPZnAQ6j8cgYjJLYHqL5hZH6Fz7V7vzU5Fiw53AgmKh5Ecz4e0biu4j2dNWpCn4wXpAEFA646-BBGIE8n7OJ7dQLeLCXNhYlCIcHQEPAJWv_7iSIEpddxdvGnJWQaONPhKX5T1SWEmpFy-1TB626mJ9rjircTNskR9l41307Iujo-r9kmDHouzMOkNGFZpF7YNrE3kHCIBQZtMBtT9ee7Ytk_iSpG4XUSxu82XlkSv9ClmxiVCr-OOqhbH72Urfo_6oUzHdmHJKnqpmwQZVO_VTRwWd9AfpImVM_oLbcra_CygtXLDe3zuTUAO_EgROF7nuDGR8cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کودکتون روزی چند ساعت باید بخوابه؟ جدول خواب مناسب هر سن رو ببینید
😴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/675673" target="_blank">📅 10:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675672">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a62bcbbf.mp4?token=fxZu0RkjrDSUXI_tsxKH-W6cYwWQO5ptodI3GHNtwITJ7MHZtqIIwUm6xLmWqKp1Qzd0YBZFNVAL3WISZ9FiymtSglHg9B0cmZ3YlPD_XB5p3auZ_GKW8xADESqxO5t_8lRyADeRqleo86eBsm_lzVQCwN0LzC_RSwbs7Vk72-moElrJsy_UzqqoDAPOR54c-YPf8XpBRj0wp-MvngOQCcDK_wUGl8i1QPZJ3sFwiNaLg-hiJVzNJMIOIMeTSzLnuyzj_K8JsgNEkxe-YPBMFGTlYeBffBhIwlXrtK1AUNUcIV7WFnaxDadLinYd80ooSiKfC87AejCuSYLQL7H6sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a62bcbbf.mp4?token=fxZu0RkjrDSUXI_tsxKH-W6cYwWQO5ptodI3GHNtwITJ7MHZtqIIwUm6xLmWqKp1Qzd0YBZFNVAL3WISZ9FiymtSglHg9B0cmZ3YlPD_XB5p3auZ_GKW8xADESqxO5t_8lRyADeRqleo86eBsm_lzVQCwN0LzC_RSwbs7Vk72-moElrJsy_UzqqoDAPOR54c-YPf8XpBRj0wp-MvngOQCcDK_wUGl8i1QPZJ3sFwiNaLg-hiJVzNJMIOIMeTSzLnuyzj_K8JsgNEkxe-YPBMFGTlYeBffBhIwlXrtK1AUNUcIV7WFnaxDadLinYd80ooSiKfC87AejCuSYLQL7H6sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز پذیرش سهامداران برای مجمع عمومی فوق العاده فارس
🔹
از دقایقی پیش پذیرش سهامداران حقوقی و حقیقی برای مجمع عمومی عادی فوق العاده فارس در هتل ارم آغاز شد.
🔹
امروز  در حالی دو مجمع عمومی فوق العاده و عمومی بطور فوق العاده شرکت صنایع پتروشیمی خلیج‌فارس برگزار می‌شود که بیش از ۱۹ میلیون نفر سهامدار این شرکت از سهامداران مستقیم عدالت و سهامداران حقیقی با مراجعه به سامانه «مای مجمع» می‌توانند به صورت آنلاین این دو مجمع را در
این سامانه
مشاهده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/675672" target="_blank">📅 10:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675671">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miDoy6Xz3nFeWMhr17RK3RmXnLvd8OY928iF5jTOdGhCUx12RXR5pWsfeN7r9q_m66CuGGiFufJHM4T3HmyKWm70yjb-SEZwH5eD85Ep183D4eYVhfQR-o5KMWclN6AyK25TA_rqXgOBsf-l2iMYamSjxIIjfLhtz50N_ZJd85CIRhstPcek8xUb8mTGoQyQDQm9fPF0bQqiIIGG8BDrZzh4WY6Avsn8TbrpaMGtQeg6I-hVzQ08jL8vANI1EZVgo8jJedQIjXzMDx4KgjOCENARinPkt_4_zMAvRJCrO-FkKcGcsNXUtmpmQRQNd0aL0dy6na8-GUiSL7StuRfiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: اقدام «فرصت‌طلب مستقر در کی‌یف» نمی‌تواند بی‌پاسخ بماند   وزیر امور خارجه:
🔹
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و یک ملوان را شهید کرده است. این اقدامی است که به‌وضوح منشور سازمان ملل را نقض می‌کند و به تحریک اسرائیل انجام شده تا اروپا را به…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/675671" target="_blank">📅 10:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675670">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rcn5AUAZonjOOt0QvjCgHMB0V-Ran9say3DIHC-bzReMvrottOdWLgatgBIhU4qbGdFoC9-Qfc15Wo9Q7Y6FPFSnlCRcjwNE76NIoiwlYcbb7euXSjZIXgL9_Kd4M_6aDlhVEllJ4bhTst3GxgNyUl3CTlawS5CtuhUrxqCUMhd64nzIQUucC_jUROz2QPRg8RZ7YqeCWyvTui52l8bLqvv8aEWqGq-srgTgJ-eH8QxBvNt_qHrB-b2eO1bGbHyn60JP4jxWDnSgju63QVuLIwziP5FldHWBeAnfJV3_xaPfVOMp8BAbUJFeNiz171HXFM58VOJ28jNXPjFju69mzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مادر ایران‌زمین؛ کوه دماوند
نمای دلربای دماوند از دریاچه حوض سلطان قم
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/675670" target="_blank">📅 10:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675669">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
‌
ارتش: به تجاوزات احتمالی دشمنان، شدیدتر پاسخ می‌دهیم
بیانیه ارتش به‌مناسبت عملیات مرصاد:
🔹
پنجم مرداد یکی از اوراق زرین تقویم‌ ایستادگی فرزندان رشید ملت در دفاع از ایران عزیز است.
🔹
ارتش با پیروی از رهنمود‌های فرماندهی معظم کل قوا، همراه سایر نیرو‌های مسلح، آماده و هوشیارتر از همیشه، در برابر هرگونه تهدید و توطئه دشمنان ‌ایستاده و ذره‌ای در مسیر هراست و پاسداری از استقلال و تمامیت ارضی میهن اسلامی، کوتاهی نخواهد کرد و تجاوزات دشمنان را شدیدتر پاسخ خواهد داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/675669" target="_blank">📅 10:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675668">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab9f096c1f.mp4?token=vpGG6n62_GHPbD3oil46kd4Jb5K0ZBsB5lo1EseQdkhSAo2xtmnuz_bTIUMiTo3Ap2g_KVMJdQXp6quNi3xrjbtF4sFt2i-7bhxW7a1LqJwH8YAcXHX4E0Rlob6r9i5wsyouiX-xkI3HRgd-nsfgf9wJsppvehfXY_ZVXRXXS_LfZuUWL25nE1Hgt3Tq3GN8dhxBlItJALb_ulR4gzx1sDRO9d2RWMpA3ZIGFSgjSdMRkvGaRODrex2NOYDsIbx3c_iue28qoUqfUHZ8Xh3I5vveLNI9Ep0xGl9Gqau206W47ULMNMCjL8E89GfASROl9XMp_-bT9LV4nCyD6bH7Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab9f096c1f.mp4?token=vpGG6n62_GHPbD3oil46kd4Jb5K0ZBsB5lo1EseQdkhSAo2xtmnuz_bTIUMiTo3Ap2g_KVMJdQXp6quNi3xrjbtF4sFt2i-7bhxW7a1LqJwH8YAcXHX4E0Rlob6r9i5wsyouiX-xkI3HRgd-nsfgf9wJsppvehfXY_ZVXRXXS_LfZuUWL25nE1Hgt3Tq3GN8dhxBlItJALb_ulR4gzx1sDRO9d2RWMpA3ZIGFSgjSdMRkvGaRODrex2NOYDsIbx3c_iue28qoUqfUHZ8Xh3I5vveLNI9Ep0xGl9Gqau206W47ULMNMCjL8E89GfASROl9XMp_-bT9LV4nCyD6bH7Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این تارت خوشمزه شکلاتی پایه ثابت همه‌‌ی مهمونی‌هاتون میشه  مواد لازم:
🔹
مواد خمیری
🔹
آرد ۱۸۰ گرم
🔹
پودر قند ۵۰ گرم
🔹
پودر بادام ۲۰ گرم
🔹
کره ۷۰ گرم
🔹
زرد تخم مرغ ۱ عدد
🔹
وانیل ۱ قاشق چایخوری
🔹
مواد فیلینگ
🔹
خامه ۲۰۰ گرم
🔹
شکر ۲ قاشق غذاخوری
🔹
شکلات تلخ ۲۰۰ گرم…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/675668" target="_blank">📅 10:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675667">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
هشدار پلیس فتا؛ پیام مالیات معوقه تله جدید کلاهبرداران
معاون اجتماعی پلس فتا:
🔹
در روزهای اخیر پیام‌هایی در پیام‌رسان‌هایی مانند ایتا، روبیکا و بله به نام سازمان امور مالیاتی کشور برای برخی کاربران ارسال می‌شود که از مخاطب می‌خواهد ظرف مدت کوتاهی روی یک لینک کلیک کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/675667" target="_blank">📅 09:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675666">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
روابط عمومی سپاه استان تهران: انهدام مهمات عمل نکرده تجاوز آمریکایی صهیونی در شهرستان پاکدشت روز دوشنبه ۵ مردادماه مرحله اول از ساعت ۹ الی ۱۱صبح و مرحله دوم  از ساعت ۱۴ الی ۱۷ صورت می‌گیرد
#اخبار_تهران
در فضای مجازی
👇
@AkhbarTehran</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/675666" target="_blank">📅 09:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675663">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7eyQBjEzgy46WW7HJF7g3yEL6UBFBrOgfhpzQbfboj1iiA11Z2OTAsn5fdo4iemB9uo0MCBH6xIj6Ui7-6zUTX5_zH3goUp-hCKyESUTf6smJjHTuHDz-2DUBv8NUHooq9xAJe-yX6DPcvjsOUAFOLQE_MVjHkoy905myx1yqAsch72YGneWIqKcb6FL0vR_aaS321IpEvvYBBr5vXFjp_OeKWnWlur3o4APSY-Ok7N33lK8BduZksxkvY6Hc2TQYZO7eyJbntSUZXL1KSpSFlDL2ndyJD8qY3mJ-T299k4yvXFpqOTqGmAdHnAik-UCxh5KIkT5KOyOvcfOdHVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پنتاگون بی‌سروصدا تلفات جنگ ایران را فاش کرد؛ ۶۴۲ کشته و زخمی
گاردین:
🔹
دولت ترامپ در تلاش است آمار تلفات را کم‌جلوه دهد، اما پنتاگون با به‌روزرسانی خاموش پایگاه داده‌اش، پرده از واقعیت تلخ برداشت. از آغاز جنگ علیه ایران در ۲۸ فوریه، ۱۸ سرباز آمریکایی کشته و ۶۲۴ نفر زخمی شده‌اند.
🔹
دولت می‌خواهد این عملیات را جدا از نام رسمی «خشم حماسی» نشان دهد تا تلفات کم‌تر دیده شود، اما قانونگذاران هر دو حزب این «تفسیر سلیقه‌ای» از قانون اختیارات جنگی را به چالش کشیده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/675663" target="_blank">📅 09:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675662">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVfN5uS5wpos9GXZebulrcscveGaqNxg0BqxreBGcxGSXBS7MkA_N3B6LIVlP-DqzqEblkgFrAAmERpgdpP9l7sWVAcQS8ehcUCAS9jxH9hxrluwRcelNxtpseoesJcstfpi8r5Dffi41k10e-FxkmGiYyJbEE_Txu4JBcBXVxGeQtD7nNDKucScFJO3QKHxyD2b8JrIszEJGWlmTHw80lVC0kF8VZk5O0sLVAFI-Bom3Im5BuxOM5X76snGL125cegAWvKJWp0QYpDQK7xifvqMhsU9NQa8UIXrnUKUAy-zKT99B0WZHqeRYy5f6_DbI_xK7n4J8RhsdrIDe-dHMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار سفارت ایران در لهستان: پاسخ به متجاوزان اوکراینی حق ایران طبق منشور سازمان ملل است
🔹
زلنسکی با الگو قرار دادن رهبران رژیم صهیونیستی که ایالات متحده را به جنگ با ایران کشاندند، رئیس جمهور اوکراین به دنبال کشاندن اروپا و ناتو به جنگ با ایران است.
🔹
او پیش از این از وظایف خود فراتر رفته و نه تنها در امور داخلی ایران دخالت کرده، بلکه در تسلیح برخی از طرف‌های حمله کننده به ایران در طول و پس از جنگ ۴۰ روزه نیز نقش داشته است. واضح است که خویشتن‌داری ایران بی‌پایان نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/675662" target="_blank">📅 09:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675661">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
المیادین: یمن از عبور ۱۶ نفتکش سعودی از باب‌المندب ممانعت می‌کند.
🔹
چهار مسیر ویژه زیارت مرقد رهبر شهید در حرم رضوی ایجاد شده است.
🔹
قطر و عمان درباره تلاش‌ها برای کاهش تنش‌ در منطقه با یکدیگر گفت‌وگو کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/675661" target="_blank">📅 09:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675660">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umdTkgQ8QHHFGM9KeeOYWsGwxIJNSa7WdFK0Ao4w2AAd1r3UnLZfRf8Bq_y4aTaAwOPOEdKWLbbIb8sfpKOinVHY3ujujd0kWf1Fbxwd3jhzGmzMAOslprO_HSai3nrWnVJ8D_GLw8Fnlr6WOGIPHNDmLT9P8AWQz2c7FN-zKCJurcMB2DXsz-fz6boUGszgzN0YjGOffQq11gYM9Mn1xWk8WEslLzW0_e4WGC2YEJJ454k1aoLpnB5nsThk8KY2Wzj7uxv0ZA9auBRpP8llOcSGyDeQhBwv-BBSg1KBB1KDLfX7Xgk6hZHWBo41n_eVnPlTrcbNpBL7-P5NF_UBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تداوم هفته سبزپوشی بورس
🔹
شاخص کل بورس تهران امروز  با رشد۶۰ هزار واحد به سطح ۵ میلیون و ۶۲ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/675660" target="_blank">📅 09:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675659">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✨
تخفیف  ۵۵٪ ویژه هتل مشهد
در گروه هتل‌های لوکس درویشی
🎁
هر ۴ شب اقامت = ۱ شب رایگان
🏊‍♂️
مجموعه آبی و گیم‌کلاب رایگان
💆‍♂️
ماساژ رایگان اتاق VIP
🚕
ترانسفر 24H فرودگاه و حرم رایگان
⏳
فقط تا ۱۵ مرداد این شرایط باقیست ، همین حالا تماس بگیرید
📞
05138080
‏
🌐
darvishihotel.com</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/675659" target="_blank">📅 09:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675658">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f92c7e73.mp4?token=HL4OIF-4fuxbiAqQ52c_HsyOCN4Ig_OiM9BVV3eQjF2pjauCFJ8-a11Bhp6C_CpTXlKfrGN56S4EKSNflegiNcL5cO_tzgagE5dKrT2Ld85lQ_Dy0-5N7kRqeKjXRwsYbL6o36DUrOE1jjMOw5yMGa5pUglEFQOBbI_I3rcOPujSV7tQ9UOeDaxQyqjeXgBGy_VhuQyYscp3KfxC-_xveSMicJrYlr0mUejBqFapFrYYEWoAHrO2RZr7Wxgac-HBK-yC3wrQeRNYuxoD0OpXj6wmicy27HbsIKwdwRy5qufJpeAnKn1Xq1-b1Bg6erJQG0zfvfo96i3EvR2Uz6pMBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f92c7e73.mp4?token=HL4OIF-4fuxbiAqQ52c_HsyOCN4Ig_OiM9BVV3eQjF2pjauCFJ8-a11Bhp6C_CpTXlKfrGN56S4EKSNflegiNcL5cO_tzgagE5dKrT2Ld85lQ_Dy0-5N7kRqeKjXRwsYbL6o36DUrOE1jjMOw5yMGa5pUglEFQOBbI_I3rcOPujSV7tQ9UOeDaxQyqjeXgBGy_VhuQyYscp3KfxC-_xveSMicJrYlr0mUejBqFapFrYYEWoAHrO2RZr7Wxgac-HBK-yC3wrQeRNYuxoD0OpXj6wmicy27HbsIKwdwRy5qufJpeAnKn1Xq1-b1Bg6erJQG0zfvfo96i3EvR2Uz6pMBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تابلویی مربوط به نقشه ۱۰۰سال پیش کرج
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/675658" target="_blank">📅 09:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675657">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d1f32b62c.mp4?token=YP_YjBoWo5dYq7KMMC8ZJogUDttLRoFTBVc0dzYxM5cUXWiaunhFgkgJDVBhmzAQVFjYHgnB6l-eaa-y6OozmCLW_tl-ekTWuJ2u_2ZEkSecqDExGmsTn7m_6y6pRXm3k8yWD8LboLIHoO9k9x6PNRC99z0_HoRkmvXjHvoYJtoX0B-f4w3WECSg9Lv0VjOOix0sHkknR-lqMdXZ2Zc_3hKNtrQkn4TBWzlTMYnrQYHh829BEKpci2vTZAWSa912X2aDSnHio4kahEcxP1wXiScwNTvtPjQO08mXwALNNc7l2Kqb8BWrYFjttzwwlh3-EewzRpasKxX4VOB-0krioQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d1f32b62c.mp4?token=YP_YjBoWo5dYq7KMMC8ZJogUDttLRoFTBVc0dzYxM5cUXWiaunhFgkgJDVBhmzAQVFjYHgnB6l-eaa-y6OozmCLW_tl-ekTWuJ2u_2ZEkSecqDExGmsTn7m_6y6pRXm3k8yWD8LboLIHoO9k9x6PNRC99z0_HoRkmvXjHvoYJtoX0B-f4w3WECSg9Lv0VjOOix0sHkknR-lqMdXZ2Zc_3hKNtrQkn4TBWzlTMYnrQYHh829BEKpci2vTZAWSa912X2aDSnHio4kahEcxP1wXiScwNTvtPjQO08mXwALNNc7l2Kqb8BWrYFjttzwwlh3-EewzRpasKxX4VOB-0krioQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب آشیانه جنگنده‌ها در پایگاه هوایی شاه فیصل اردن‌/ انبار مهمات نیروهای ویژه آمریکا هدف قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/675657" target="_blank">📅 09:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675656">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b5adfbfa.mp4?token=ZgAD5BVtAwXUxvSadeecG8diQXqgw-qHFlrnizffm0rBBI5CecEDdxwdXhC3CkaaXO32ZwJDMPW_M9H7668EEJ9LxR9RJX4QZH9e7Uw2Gt5N3H1hJB3JduTwsuiZxU4O7XfFseUCmRUorFU2yuOKPVuw-xx9rqWU9X-L6rk1KG31FMB0bK_JWrZ-HCTQHMEipr_V1gb1XwQKienXNZIbZAffJaidsxg6M5PE6MGwuPhPIgLbDsatFSbPGt3J_xOQJ059Nrbgb2NvUY8-_xiFrVofKRns463cNFsDZ-s8qCf9hI1xNBB4ZGu9lqN-ziXTTNB1vj_kTQSrxlNBOJj9Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b5adfbfa.mp4?token=ZgAD5BVtAwXUxvSadeecG8diQXqgw-qHFlrnizffm0rBBI5CecEDdxwdXhC3CkaaXO32ZwJDMPW_M9H7668EEJ9LxR9RJX4QZH9e7Uw2Gt5N3H1hJB3JduTwsuiZxU4O7XfFseUCmRUorFU2yuOKPVuw-xx9rqWU9X-L6rk1KG31FMB0bK_JWrZ-HCTQHMEipr_V1gb1XwQKienXNZIbZAffJaidsxg6M5PE6MGwuPhPIgLbDsatFSbPGt3J_xOQJ059Nrbgb2NvUY8-_xiFrVofKRns463cNFsDZ-s8qCf9hI1xNBB4ZGu9lqN-ziXTTNB1vj_kTQSrxlNBOJj9Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار تصاویری جدید از اصابت موشک‌ به مخازن سوخت پایگاه هوایی موفق السلطی در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/675656" target="_blank">📅 09:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675655">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5137ab1f7.mp4?token=O1NPrRofe7-XP_QrrYK22TTV6jhovBweVgQJkQc-CvjRvilLoYa2_s-yKLKakU9gZzIXwjaZIBSU4eeSm4h7dlBPYqGc3eAbwW7adbO3y1ZDmYbixefpW1YBJnxCptAxZc6YNWsyHoqklskqsU13kDvhI-nhW99T3apEvUkv8QrvJ9mvT9tacJPC6ETHC8vdO6j3nYXtpYWg77JzhKzMeTOenbkge-5A00INGpBb-nYvI89Ny41iM5zkyjw_R3hmuD7QiOvp_mEytZ-Q_92325k90tGt575I8TAQ8JaT1aYg__fd0TBa14NiYNVTkqfwBEIxf_kB9vR7CjYuQWEkqBk3A4jqqXrVIZOJP4_TPsPe1mNl7U3qkjZEsu_ord24la_8k8Y0Ud7uKAxa1THm_-1U1uy__9SlOTLqXHdvS_UT_tu0TlNHVu5C4TJZZmvXLZO2GytmiLX6y4SgyFfCsnD0KFC539UxyqfNwRk0qu1mXSbhhzvER19nyaw7_0hyr_q5XHcE6XpTL1m7HFKv3aby5pQwuzN4vMpUf7xxCzCP8RVqqj0PeLc7y0Gn2b8AWc2FoXCqIhR6EMX_vDlmoXGtQ3rEX-ICdMt-sSMY1aHMWWwaxi2JpWsg00SoiFlikD5v4DbRrzBKlU_VSzUrE9BlDCqRshqb-XJcdXgPJyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5137ab1f7.mp4?token=O1NPrRofe7-XP_QrrYK22TTV6jhovBweVgQJkQc-CvjRvilLoYa2_s-yKLKakU9gZzIXwjaZIBSU4eeSm4h7dlBPYqGc3eAbwW7adbO3y1ZDmYbixefpW1YBJnxCptAxZc6YNWsyHoqklskqsU13kDvhI-nhW99T3apEvUkv8QrvJ9mvT9tacJPC6ETHC8vdO6j3nYXtpYWg77JzhKzMeTOenbkge-5A00INGpBb-nYvI89Ny41iM5zkyjw_R3hmuD7QiOvp_mEytZ-Q_92325k90tGt575I8TAQ8JaT1aYg__fd0TBa14NiYNVTkqfwBEIxf_kB9vR7CjYuQWEkqBk3A4jqqXrVIZOJP4_TPsPe1mNl7U3qkjZEsu_ord24la_8k8Y0Ud7uKAxa1THm_-1U1uy__9SlOTLqXHdvS_UT_tu0TlNHVu5C4TJZZmvXLZO2GytmiLX6y4SgyFfCsnD0KFC539UxyqfNwRk0qu1mXSbhhzvER19nyaw7_0hyr_q5XHcE6XpTL1m7HFKv3aby5pQwuzN4vMpUf7xxCzCP8RVqqj0PeLc7y0Gn2b8AWc2FoXCqIhR6EMX_vDlmoXGtQ3rEX-ICdMt-sSMY1aHMWWwaxi2JpWsg00SoiFlikD5v4DbRrzBKlU_VSzUrE9BlDCqRshqb-XJcdXgPJyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گریه‌های بی امان غلامرضا نیکخواه در کنار پیکر اکبر عبدی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/675655" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675653">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d04916277.mp4?token=vxWvtVqREwo9MhGu7fXIB8J-bcr5C1WFqplBpbzNbvU9qqnMXMFAMfECNtzsNGxl4v6McXacA9MnYNqn9DhIlPyMcv1erZQg0Thaf5th8GyXr_KbQ1bwO5TNhLphnMt9wiYvP4etgL84S3COD91BsW7FeihxbJr0T3P5cPH6ANMmlOmbGF5i8k2KlXGQh9Cf-jgRRsHcTAkCbjgbZrXljCAEBgCvHa4-HtnL2fYcQUPTMYwlrydEkcIktBvJ9cETy00Xqp6HGg-D1nWEbcwnfxNmt_mHRxsKgI1CCayTXZjDqQ8CKy22Ja3sF6gvRn4dxg4t7Bx2x3jF_hQ17NbiIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d04916277.mp4?token=vxWvtVqREwo9MhGu7fXIB8J-bcr5C1WFqplBpbzNbvU9qqnMXMFAMfECNtzsNGxl4v6McXacA9MnYNqn9DhIlPyMcv1erZQg0Thaf5th8GyXr_KbQ1bwO5TNhLphnMt9wiYvP4etgL84S3COD91BsW7FeihxbJr0T3P5cPH6ANMmlOmbGF5i8k2KlXGQh9Cf-jgRRsHcTAkCbjgbZrXljCAEBgCvHa4-HtnL2fYcQUPTMYwlrydEkcIktBvJ9cETy00Xqp6HGg-D1nWEbcwnfxNmt_mHRxsKgI1CCayTXZjDqQ8CKy22Ja3sF6gvRn4dxg4t7Bx2x3jF_hQ17NbiIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آلومینیوم چه کارهایی می‌تونه بکنه؟ چند کاربرد جالب رو از زبون خودش ببین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/675653" target="_blank">📅 08:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675651">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8b3b13be.mp4?token=AUQlDk3KHZE18p6wZkKqdu6hLXDmqwYWY8Y1_e-Pui329Km1VPqBdpRAFpLcGI_J9X1lK29cXHXPQHLWuZev_b4h_RB7KMFM4JZ_I0A7tQ5xqWB2eI5UynSvkkTaulOHG-8L-rzD-yVcYIVWoGWFEuuz_8tyOcqCg0lrYbhlywQ4YJXZLz1N_Ig3n7fc3mBgkbF4ld7Qgcg3WZPyF0PDS5oLU5YL4FSAsnDVWmlW3HT8tgov_GjrppFCA9-QixmK1xS41GnzY8Q6J8osnwcj2NclzZem4uSAQFCqaW9p0HUbjvirKhXKp1eWg60S-ZCGhkezAAWMfRP2x3b7_YxLYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8b3b13be.mp4?token=AUQlDk3KHZE18p6wZkKqdu6hLXDmqwYWY8Y1_e-Pui329Km1VPqBdpRAFpLcGI_J9X1lK29cXHXPQHLWuZev_b4h_RB7KMFM4JZ_I0A7tQ5xqWB2eI5UynSvkkTaulOHG-8L-rzD-yVcYIVWoGWFEuuz_8tyOcqCg0lrYbhlywQ4YJXZLz1N_Ig3n7fc3mBgkbF4ld7Qgcg3WZPyF0PDS5oLU5YL4FSAsnDVWmlW3HT8tgov_GjrppFCA9-QixmK1xS41GnzY8Q6J8osnwcj2NclzZem4uSAQFCqaW9p0HUbjvirKhXKp1eWg60S-ZCGhkezAAWMfRP2x3b7_YxLYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوز، گردی شانه و خمیدگی بدن قرار نیست تا آخر عمر همراهت باشن
🔹
توی این ویدئو چند حرکت ساده اما مؤثر رو نشون دادم که اگر منظم انجامشون بدی، می‌تونی به بهبود پاسچر و فرم بدنت کمک کنی. #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/675651" target="_blank">📅 08:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675648">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvLDnGpZB-vh1ZIkGSQj1UcvIERMdjbRRGnbLnC782UBxnnKisxYsaAdAPe7c10vh0caUOqbCXhLEgetdJjUc1v9vTTJNRcQEfESoUKED38rcKSCGatI4gjteg5R-rUi4hgJ5SZ-AgCcarIcKaV4Xe26MkxUK0xDxMFfrUG4ixfoN1Ur7idNN1iR-RRwM77iD5rC-_ocAAiZIuJz9sk7Utbl0DkNCSzJp5nPOM0gTAt3Ag8KbYvPqNYsfQlqUG3SjOPfUBNOp3ETp1kJ_EUXK9zBO7uaDmoPUoL-zro_NFDtXE-zW8DtxSbdf2wmKIlh7WWTP1fkiJyYqcAl1Z4DjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۵ مرداد ماه
۱۲ صفر ‌‌۱۴۴۸
۲۷ جولای ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/675648" target="_blank">📅 07:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675647">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
پنتاگون: از آغاز جنگ با ایران، ۲۲ نظامی آمریکایی کشته و ۷۶۴ نفر نیز زخمی شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/675647" target="_blank">📅 06:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675641">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXOuw2YLUJWOI7l9V0-ZW9fUDJ9i50kJ0-n9BhpWyvnnhsvhLSBDhsMy8Qm5-xrF38pYPEH6hYtshCZ0fdmk8Y1wIe2iytBVSOZHqAO1gcYWRNSiCtzNArLrcnbbDNNaccmlNOJeRD46LNklkwI69OHaNBUlT3d7qbNF6yHwWa0V8Bk3w2XSGNyZS9Raw1JFL6WqYYN0uPv_NV50bFNLjrBAjwzrQNyTKdZAsLiu3QXHK96OSFNL4dvMo4NmBQfT5inhaT_WUkQnMnrUAFFX86AxMuMqJhgC9b_oO29ZcHAjDNZS_Wh0wGkl3g9GuWS4es7nGZoxHgKgnfwmqgZbuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKyT6e3Ot79SGV-rmYPG7-woCaJpA9G1T5kwiP9uEuA3ZNBPPesSnaZ1tJkGMQW4-xDVsXs84Qb2KTBDuTgY2kjJSLlfcM6Ztko4u0E7JrjXTtvGrDOEpM76nlP6sbpM-KzSINfcJqZJbrRJRxMlvuiH5IX1IYTGU1lE2CWUiqn_gPivA2qxawFJ_776yR26KtFl5l_DOIscGiKAhXKK83fHCWMsZ4sCDrELU7iByvGYTRE0WDniwBLBknh1Mpg0DbTjocUXeysZ5nkzbMm5wjl3qpsaiXHs_OOMk6sf85zehUWzUwOftd6hPuYFpgGdPZvfG29M5lFcD4G-ICgjrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aBNXUf_5Rw6QNoSant7XKTep69Ank3-urR-BUaXS8A8FjjHPdRZeEyRqYNeuKn0sy9R72U4mibVq7Zm635TDeFN9ZvVXhHwPMHQA8h25ZPNflqipZ-9UEX6ogNL83umig3oO6kvhrRa3VZAGoUof6iwIfDFHOBRmM92yrSrRDt5twMG3X_z-1j3WsPpX7QuCBqOb4ri6L0hyVlLNE9K0T88rmODXGf-wO0MqoA3uXc8ylgzK8AleAuJpE8im1cMA6WZP2qsm6oVm7Gzu-trk3ca5cs5JICN1L5gEo0M55BWdMFlQ5FIcyVjwniS4uwrPoCVCM3Mh1m5rKaVme5ujqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WpDoyUAQVkX-FKvMv9w59AYB9WugCfCOMOfEiUqdAlECpE-jRyW3RsxTAb2426Inu82N_M_ifIqiGEhcuA6-6o6lr0lCxZYhMLQkHu-MR4G2FOnvYu8d2AqjWautUt90LgHi-4YVmPw6EYUgjymzdaN_Uf8jjDeoBtDKxk8V4rk0b6K71SmSWBvwhUTLjSJOfqP2QR-LU3EaH1nEaDHKxmNtTcVj_-JmjEzVmFrUjCjc8SqVr4jVj4kiWaX2hx4oZBWTQ07oQlCSN53eKXzPiNONGjpgrgAxZp3f3bmP4Mv4Q_vMTkGlH4XZtmHCLcw21U7atuwyw78nAHih-VugOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شیطان زرد با کمک هوش مصنوعی به خط مقدم نبرد آمد
🔹
رئیس جمهور آمریکا طی ساعات گذشته پستهای مختلفی با کمک هوش مصنوعی در حساب خود در تروث سوشال منتشر کرده است. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/675641" target="_blank">📅 03:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675637">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adTuJt0pcmN6-__AourGWOxtcVawo92NfyVtSzbJiQe_0TjXuunpP_hTLBeRTX1ofgzUpZKvIsOgzSpZ9mEurYwA9MsZfIhw2qwJbHKgJJJQdhRT9t1sJXYFi96ZZ82_legky2fJlseFp6it6ZjZ0BHU1kPecYrfJ-kCW8RrN8qotHFAdM2YD391vbdCm7yNfu1E8aXWOh5pSkNXEDQ-jyxvWTLFv-NNcJukVMLny7gN6i84cYr9Ou74-uzT8owtdyCSUNZblxVfFTYOqIVx9BDEh6OkwF6ydl-Cy-FStMv00lv59XfbNsG_l-YAIgyjIZXr5LcEa1CjOncwAluqaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای زائران اربعین
🔹
کدام مرز زمینی برای سفر اربعین شما مناسب‌تر است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/675637" target="_blank">📅 02:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675636">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b6ca7302.mp4?token=kMVjN6RO98J1Jkbdbqjqwb_dled1imh_2bXTc1SgIgo288QzwrrpORyrIQ4Ih5N7EjrNQbvhERvBpN74i6bxz7-izGv9K39BATu0SqXjHsDP0N-5SlIdcESLHUk8WMlTghNdaceo1dtfODM84C-JbNFFegm260TAYbYhIfVyRjGVFN8RoGUDKiyjR8FRJTD4ly_dIwn-WmGcAltVN0CcO07Ga-NZYqPSonySzhRhIqMxR6R7SCLDVeOvPTYn_zG1DTIYqlBgMH_RvETBArQ1uM4-lBM7vRhWzacstko-Thh-jOjo-AojQ52EwwiB_416ztbw1ORlS_TT5kejixQ7zr_vgYW9SybUB4iFe2-CDkjpH0zIGA-0XxIYtbyX1rAcRg2ao2Tun4fPOq3oyUH7Wkxj6AgyfLjuf6UPFE6htAvHQMOW1zUn43KJBMG6DQTaMxqu0beDOe_OTtouneazcbRkOZAF2FbekQEe6SXP_qnpcmmogmEOrSgg5TVooCWFyBrWyLKXbMp5YfCqt3S-66O0oLLq5wbxzcDfKF-8hAhaBSmmpdKNHxG8_rB2wNthq0nKSBMPs4AYcPOFuNh-c14Md70AFCbSCvO6wZgvRAXIvWGYDp65pU2cZVocfBpD5A_ZXGG0DlmcJoxy9XR12rtRcwYSONF09Lvud2ON53I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b6ca7302.mp4?token=kMVjN6RO98J1Jkbdbqjqwb_dled1imh_2bXTc1SgIgo288QzwrrpORyrIQ4Ih5N7EjrNQbvhERvBpN74i6bxz7-izGv9K39BATu0SqXjHsDP0N-5SlIdcESLHUk8WMlTghNdaceo1dtfODM84C-JbNFFegm260TAYbYhIfVyRjGVFN8RoGUDKiyjR8FRJTD4ly_dIwn-WmGcAltVN0CcO07Ga-NZYqPSonySzhRhIqMxR6R7SCLDVeOvPTYn_zG1DTIYqlBgMH_RvETBArQ1uM4-lBM7vRhWzacstko-Thh-jOjo-AojQ52EwwiB_416ztbw1ORlS_TT5kejixQ7zr_vgYW9SybUB4iFe2-CDkjpH0zIGA-0XxIYtbyX1rAcRg2ao2Tun4fPOq3oyUH7Wkxj6AgyfLjuf6UPFE6htAvHQMOW1zUn43KJBMG6DQTaMxqu0beDOe_OTtouneazcbRkOZAF2FbekQEe6SXP_qnpcmmogmEOrSgg5TVooCWFyBrWyLKXbMp5YfCqt3S-66O0oLLq5wbxzcDfKF-8hAhaBSmmpdKNHxG8_rB2wNthq0nKSBMPs4AYcPOFuNh-c14Md70AFCbSCvO6wZgvRAXIvWGYDp65pU2cZVocfBpD5A_ZXGG0DlmcJoxy9XR12rtRcwYSONF09Lvud2ON53I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیلگر لبنانی خطاب به فعال سعودی: آمریکا جز حفاظت از اسرائیل و غارت ثروت شما هدفی ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/675636" target="_blank">📅 02:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675632">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdac069110.mp4?token=VJ02ir3OVpE9wX0PNbUIOln6y-V6G0P8WcCs99ZEQNPCyacOdtyhmMpbe_IPxNLyqhVsjxb5OuMzZqG93qp4aJNUcEAiH08OQORojLBJPSfZO5jRHqzBwz6Sp_wDcYITGK4eM9LyKkz_ikF2X3V9CrS__Cf9ZaZsXLIBDVApdnx1xh6X4hiGAFwuPp3G-CEAO15ALxQfwiqomQcy9zpHFla3ztrwMG_WTEDlbvL6feV8UBZ5K4WakE5T9n7fU8c25MzDRLzX38IL-OKPYbLhHiD0uPBD00tIZT2SWLERnjxYYvcd4S7Tn236KxJK9vO9Mzeq27UQhhg6XRegZnDYaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdac069110.mp4?token=VJ02ir3OVpE9wX0PNbUIOln6y-V6G0P8WcCs99ZEQNPCyacOdtyhmMpbe_IPxNLyqhVsjxb5OuMzZqG93qp4aJNUcEAiH08OQORojLBJPSfZO5jRHqzBwz6Sp_wDcYITGK4eM9LyKkz_ikF2X3V9CrS__Cf9ZaZsXLIBDVApdnx1xh6X4hiGAFwuPp3G-CEAO15ALxQfwiqomQcy9zpHFla3ztrwMG_WTEDlbvL6feV8UBZ5K4WakE5T9n7fU8c25MzDRLzX38IL-OKPYbLhHiD0uPBD00tIZT2SWLERnjxYYvcd4S7Tn236KxJK9vO9Mzeq27UQhhg6XRegZnDYaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قضیه بی پایان چاله سرویس روغن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/675632" target="_blank">📅 01:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675631">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujKk9VmQS2Y8IhIafYGnvGLjU1bpre9sK4-Y1c3wmKensp-Q_JygxsH-8aupTkX6iFKGZybFIyK5x4df3xchsaseDCwf9au1OQI9ULnemoSjnyNIRu9zxAcOgt8UQzi8J4YOpM2wiK0M8CgATdSfS6fwnKIfJ1f_nkfWWjenHRTFYF3Sv2NZM6ngcQsWjU7eQzeEEdrLZyEszN3goYOqpvB-Ql1zDb8niSk3z4S3n2VIHPCMmTWDW9sNuGWgPq1goGmwk1rn98kOGqru2wjpl-lqfvtEeh-OkkZq3nSJ9IkjnX_ew7k839dSCV8XaAVCF3Uyb5x8RPjb9mq57mCJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم عزیزی: اوکراین به زودی می‌فهمد ایران اقدامی را بی‌پاسخ نمی‌گذارد
رئیس کمیسیون امنیت ملی مجلس:
🔹
هر حمله‌ای به ایران همیشه هزینه‌ای دارد و این موضوع امروز هم صادق است؛ ایالات متحده و اسرائیل به خوبی از این موضوع آگاه هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/675631" target="_blank">📅 01:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675626">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp1LAFD0wueyjh_RXQpoX4izmLGy3WIrwnpHhrstImgwmdjjQlUuQVfz26MAzkEPdUU-IRSrHQKRFM7PhdzGa7zwUtruVhgdAEwUtQrZxZIXVB4bIPhl6K3YpFugEQlvHcdWtIarai02XcqDXx-OPS1EZLhtv1si-q0OCL4xjKR8Q4GgGvdXI7LaI57Od_51zXLkz69KivvyKuy-z5Fgif4mjbTqoTTDNKrDAu8D0ZQjGHvQtXYPnh6q1kViyOcdBcgYt60WZBSHlvuUhK_M9Phq36KdExxyIeB09wGuEBK4Yk0tuYFdwLrYzOm_KWXV06wzOk4If19vVmIM2Ry4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهند که آتش‌سوزی ناشی از حملات یمن به پالایشگاه جیزان در عربستان، در حال گسترش است و اکنون تقریباً کل پالایشگاه را در بر گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/675626" target="_blank">📅 00:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675625">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/850e2e6b24.mp4?token=N6GL_lpgKvn3VdDkFRTmrs5Il1q8x4p4d6sh8tgniDozkFC6kjPHjMRMACAivCuoQf1CLMnqrT4bKvlX_qGUkFovj59mKk60EUhd4JpOPOS9a6X_Gh0i99zSe8_GcKVo6fivRIliLXAoN6CTuA8eBcoHU0ZKr_La2rqC2WTj2pOjjUcCd3aT4KQe2VLQ1tOXfc6W9hgdYSESEJTxhV_a9IV2rFfiC39K4veaWcStRoGeNnqGsXsj2YmUSIP6ftjNJjrV8_1_qpf4I1_S1bELkcHaikBOC_Mvo2xx3fhjlCKR_Ou3py-HAJSagM3oYgdHHF34f_QKRMitqcp8-0Kl8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/850e2e6b24.mp4?token=N6GL_lpgKvn3VdDkFRTmrs5Il1q8x4p4d6sh8tgniDozkFC6kjPHjMRMACAivCuoQf1CLMnqrT4bKvlX_qGUkFovj59mKk60EUhd4JpOPOS9a6X_Gh0i99zSe8_GcKVo6fivRIliLXAoN6CTuA8eBcoHU0ZKr_La2rqC2WTj2pOjjUcCd3aT4KQe2VLQ1tOXfc6W9hgdYSESEJTxhV_a9IV2rFfiC39K4veaWcStRoGeNnqGsXsj2YmUSIP6ftjNJjrV8_1_qpf4I1_S1bELkcHaikBOC_Mvo2xx3fhjlCKR_Ou3py-HAJSagM3oYgdHHF34f_QKRMitqcp8-0Kl8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عملکرد تصفیه‌ شدن فاضلاب با استفاده از لخته‌سازها و فیلترپرس‌ها، لجن را در کمتر از یک دقیقه از آب جدا می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/675625" target="_blank">📅 00:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675622">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si_vqycMFv7tMyfuGbEs0pxgjn8W4BFpOx5z0ANhZa7KCeyxRmvvk7gwy1-loinstpNd0QraaY_JwpMjVGpGYQyXCY0K9J65j34HVzUnj0QJs20L8pNqi4k89d_z2v95AgzASODCq6JehOx0hTisr9OloHvEgfcfBHuARLmEWFWJbSbaEEM8BkALWq-0PU7ykfXm7kVn8t9IKoLLOCXXNStm3bpuJlxgBEgu8d6pCxwzVBZg3UPDJi0hKm2EeDPZeZ2jYp9ZYPgtX8ihGWFLYFtyOZKWhWzXPhNuEl8rjJytrSYcJp3tp31yIND7kKIfZW7Cvc9_em7Ua4IO114j2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخواست دختر اکبر عبدی از مردم برای اقامه نماز شب اول قبر
🔹
المیرا عبدی، فرزند اکبر عبدی، با انتشار پیامی در صفحه اینستاگرام پدرش از مردم قدردانی کرد و خواست برای آرامش روح پدرش، نماز شب اول قبر اقامه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/675622" target="_blank">📅 00:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675621">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b348c813e.mp4?token=JmSH7pKTkS0pi8wFn88TfXWqL9Fu36YaLir9_q3Q8I-hrMpkGfdqJATjgHggne-CEWXcRktEF1GP-KbjfTpV1xU2gbTvFBv6YLwk0gxZvYy_e6wYbPKsJHgpOOS4mq-GYFNRvwarDd_JLAGn6SKszW-bkTzyzzM4xISLm1M1AK9o7_w1GBGl_0Y1KZLOa9b7jJ0v_XQE2zvzffr_Ujqv91a03Q8Z1AQh5rsY814FnV4UydN0KFfZ6VgsJSEKvb-GEVbkVRJuVkiAKU90OHxgG70KktFZJLNMqeMVj3YEI0pxvAoW6UEmpDjZwxSdrud3rI0GwIeQmfmmpVKfvEl2eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b348c813e.mp4?token=JmSH7pKTkS0pi8wFn88TfXWqL9Fu36YaLir9_q3Q8I-hrMpkGfdqJATjgHggne-CEWXcRktEF1GP-KbjfTpV1xU2gbTvFBv6YLwk0gxZvYy_e6wYbPKsJHgpOOS4mq-GYFNRvwarDd_JLAGn6SKszW-bkTzyzzM4xISLm1M1AK9o7_w1GBGl_0Y1KZLOa9b7jJ0v_XQE2zvzffr_Ujqv91a03Q8Z1AQh5rsY814FnV4UydN0KFfZ6VgsJSEKvb-GEVbkVRJuVkiAKU90OHxgG70KktFZJLNMqeMVj3YEI0pxvAoW6UEmpDjZwxSdrud3rI0GwIeQmfmmpVKfvEl2eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از یک تصادف در چین که دو طرف حادثه تا رسیدن مأموران، همان‌جا منتظر موندن و در این فاصله سرگرم گوشی‌هاشون شده‌اند، در فضای مجازی پر بازدید شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/675621" target="_blank">📅 00:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675620">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZgP8mnt6r-1PV_o8e-pP2nw7RD4-B6FT28yPSgVY7lspYyygNYbgxA54keapS7JQ3ewRHV9eQzRiok2TPTmqqoG4vz4Wy1nfYmwZp4GuLTE4f7_KyOMIqekeppZN-IFv_TqAF5lxGiDvycaU24_6LW3D1fsjwHQCE9LOIxIWSg0QYM7iorQ0mdVZff286ErfB-s0HRshtmDLVxyCzTyQdHbtPedl_B2xbvdDqYspqdlBkxL02hhF1jhMOWN8LIfArIOrtG-TK82zfofh4O_NnPotozsXY28_Ef_SCJKjxS9z79abIA7uVrmG5pn0w4MLmWs4zPey8nFal0gzYWzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیطان زرد با کمک هوش مصنوعی به خط مقدم نبرد آمد
🔹
رئیس جمهور آمریکا طی ساعات گذشته پستهای مختلفی با کمک هوش مصنوعی در حساب خود در تروث سوشال منتشر کرده است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/675620" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675619">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3212f3f8f5.mp4?token=cm6Ew1544AWO9SeisSIR2oAYgco2tzEjd7uYz8v7GqKYDpO5SgW-wzwoFqag3lNA4DlbSF40EltPqU7ThkIIgsuK3exFXISKJ4pvY9LDSSa8dgsB-daL0yK9CR5MX2Hs2lfUGPAeKtk8dmKm6qDZBxxq9yRsIyErTTxtL0Tb2dtJa5gupgW-m3YD6Ri0rbJteVIrgFDe3Q1YmzB3VjL-UWzO0JXc_N1BgOt7YapC0-qZiPTuM-SeQZ7fVUjyZyq49TiukYHVCXFTbVmo_X9OFQPXINUkn9iwmZj04_DcOfAHmoo6tbaPNzGzou_N7EoRBaSoOOlgM28NgvwOkwPBWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3212f3f8f5.mp4?token=cm6Ew1544AWO9SeisSIR2oAYgco2tzEjd7uYz8v7GqKYDpO5SgW-wzwoFqag3lNA4DlbSF40EltPqU7ThkIIgsuK3exFXISKJ4pvY9LDSSa8dgsB-daL0yK9CR5MX2Hs2lfUGPAeKtk8dmKm6qDZBxxq9yRsIyErTTxtL0Tb2dtJa5gupgW-m3YD6Ri0rbJteVIrgFDe3Q1YmzB3VjL-UWzO0JXc_N1BgOt7YapC0-qZiPTuM-SeQZ7fVUjyZyq49TiukYHVCXFTbVmo_X9OFQPXINUkn9iwmZj04_DcOfAHmoo6tbaPNzGzou_N7EoRBaSoOOlgM28NgvwOkwPBWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خادمان عراقی اربعین امسال با سینی‌های موشکی از زائران ایرانی پذیرایی می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/akhbarefori/675619" target="_blank">📅 00:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675618">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e830fb3882.mp4?token=MWFDK9f21sDMevHMhJch3tGk3uCTLYrKaAsLC0rwCIvOAzhYqFKu4hGd04h34R4U-rSFzU_KkyzKXoCb3ucSIIDZbZNX3R4q_z7NBTsUcFIGt14VBBrAuoakJaxgfucHfer_9LvNYrStCk1gnZeXv0GykYCWTQrbfnjasaBjyGKvvm0S3q1FTk6Nrx77z8VJ2usy4qzvKqerR9_iHRnPmoRe3A7wNgxk518GDmXJkTeLqXqdja1l7Y9U7DUN7rE5shUbYoTl7PS5sPB20pHvwp_rATGAu1UeKSKHAmgv-6MyLQZkJ3vY6gD_oErqTqEVrIfqmJe3p6CQ7Tsq5cBEFDHebgUVvtbA39TSH_m71kIi94JrobvJXqh1mnsIB9HWYZWp3krrhsMqSAFXkacX5YvTkqMeQRuu_fxBTO34y1kLIg8Q87Zg3XfnPleUrDHZWPMvMN0JlWQqolRItPahsbH5J54FKOIIYgShnyW394U3D0mnwXx5DeCTZNYGfklm_RzJDmVcgi2hFoKNh446JbDRCjTFGhrCFu0BuobGRk296M1ZesieA7LTzI66SYTTpZ3T56APEkujjB5fDOnOpkUwr6EtEJ4dfech4jrFUAcQism39UX2MtDJTRUpnS-OArp72vZcL6wiWmPEHSfqwxK08pW6LkwuhBPfi-BBOxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e830fb3882.mp4?token=MWFDK9f21sDMevHMhJch3tGk3uCTLYrKaAsLC0rwCIvOAzhYqFKu4hGd04h34R4U-rSFzU_KkyzKXoCb3ucSIIDZbZNX3R4q_z7NBTsUcFIGt14VBBrAuoakJaxgfucHfer_9LvNYrStCk1gnZeXv0GykYCWTQrbfnjasaBjyGKvvm0S3q1FTk6Nrx77z8VJ2usy4qzvKqerR9_iHRnPmoRe3A7wNgxk518GDmXJkTeLqXqdja1l7Y9U7DUN7rE5shUbYoTl7PS5sPB20pHvwp_rATGAu1UeKSKHAmgv-6MyLQZkJ3vY6gD_oErqTqEVrIfqmJe3p6CQ7Tsq5cBEFDHebgUVvtbA39TSH_m71kIi94JrobvJXqh1mnsIB9HWYZWp3krrhsMqSAFXkacX5YvTkqMeQRuu_fxBTO34y1kLIg8Q87Zg3XfnPleUrDHZWPMvMN0JlWQqolRItPahsbH5J54FKOIIYgShnyW394U3D0mnwXx5DeCTZNYGfklm_RzJDmVcgi2hFoKNh446JbDRCjTFGhrCFu0BuobGRk296M1ZesieA7LTzI66SYTTpZ3T56APEkujjB5fDOnOpkUwr6EtEJ4dfech4jrFUAcQism39UX2MtDJTRUpnS-OArp72vZcL6wiWmPEHSfqwxK08pW6LkwuhBPfi-BBOxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیاده‌گویی
جولانی: ما هرگز نباید مجبور باشیم بین جاه‌طلبی‌های اسرائیل و ایران در منطقه یکی را انتخاب کنیم
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/675618" target="_blank">📅 00:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675617">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toTtHKhU-3EUElbukAZzZ0CgWszrU0WvIpFByaMz6CrV396JjnjXh_V_xZK5n7Op48S7fKPgLbh7clZh83OIOR7GAKpkkNmjJfNq4xr0VfUNFD3de-c5PB0-P6BUg6A6n00beNoRPT42U2wZ4JpZhkfXJNsW2j5YMb4b78txlNfVxuIVdvHOhDGvREngshnNL_J-01-Z3ZvCIofgdI1UfaxKGuMnLNfm2enoulQmY3oZSe1aFgL-II3SZUJ_UOsQ2W0FuBPesIBh-znH7QlFWCRc8Ey3qZrS9nmvNSKzmsPShxnqwFu7K1ejeX84C1xzuvh9TZn_nh9eeF4DDDizJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/675617" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675616">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84cd7cb3c4.mp4?token=KIm62_BGHVNLrizDhHxKK5cDpRQLzG7yT8li7qD1Cj3Lr-2mRr60eImInnEuZEI_avEKp-acKmJ9LA3JcgllY-sRHDesBrXj28rnP_L-8FzrWGFoVQJ17mriIU10SLjKbaqr7xg6pfuGnLpWOoaHy7viotYECzM-dXTD5Upm67VRY_wJSycRg2M-H3Y5rdi23ghdutb6loDC2cvrViJCX-iEWikDGcZUQtrC5NGnngPCdk_5xif0uVVDyQbnKlhnE4J1VA4iyJwahOYEfbWASpLaFWyrN3_PSteS4GC3IIVorWctNY9cPgxugG41wHop_CcwK64sPJH6Bb7-9sYS6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84cd7cb3c4.mp4?token=KIm62_BGHVNLrizDhHxKK5cDpRQLzG7yT8li7qD1Cj3Lr-2mRr60eImInnEuZEI_avEKp-acKmJ9LA3JcgllY-sRHDesBrXj28rnP_L-8FzrWGFoVQJ17mriIU10SLjKbaqr7xg6pfuGnLpWOoaHy7viotYECzM-dXTD5Upm67VRY_wJSycRg2M-H3Y5rdi23ghdutb6loDC2cvrViJCX-iEWikDGcZUQtrC5NGnngPCdk_5xif0uVVDyQbnKlhnE4J1VA4iyJwahOYEfbWASpLaFWyrN3_PSteS4GC3IIVorWctNY9cPgxugG41wHop_CcwK64sPJH6Bb7-9sYS6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در اوایل ماه مارس، لیندسی گراهام پیش‌بینی کرده بود که حکومت ایران ظرف «سه تا چهار هفته» کنترل شهرها را از دست خواهد داد و مشارکت گسترده‌تر کشورهای عربی، «شتابی تقریباً غیرقابل بازگشت» ایجاد خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/675616" target="_blank">📅 23:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675615">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32d175a29b.mp4?token=OQrq8XEVWeV3RxPWYnYQHfLXoaZRl7eAaC83MkRT8AzyNjZjImZf5YYNfxTqk7YnatxRJly8NlFIcSAX0XJiHiMjVtc1-_geVW9nCCRep4xMWALMJiaITBuKm3QEgNKoBTIthE_6lMMNQZyiQkwa8kFyfZ1YueJSx0xekxsVWaKAjRm0cUJ3GJiAmojiXvqxIn7bOBHrPA_CLRtCqvOjlX9G__947Xxa8k2dL9s0Wt00f_r-kFT5fNFG1UzuXItLEVAgFlbM6cORtPmGKl19tEkVqM9BSd1JcRfQg95Jk0gVk7pQMYY5rbEjRcapwfHFe9ubUwvWqqf91ERhhf6hQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32d175a29b.mp4?token=OQrq8XEVWeV3RxPWYnYQHfLXoaZRl7eAaC83MkRT8AzyNjZjImZf5YYNfxTqk7YnatxRJly8NlFIcSAX0XJiHiMjVtc1-_geVW9nCCRep4xMWALMJiaITBuKm3QEgNKoBTIthE_6lMMNQZyiQkwa8kFyfZ1YueJSx0xekxsVWaKAjRm0cUJ3GJiAmojiXvqxIn7bOBHrPA_CLRtCqvOjlX9G__947Xxa8k2dL9s0Wt00f_r-kFT5fNFG1UzuXItLEVAgFlbM6cORtPmGKl19tEkVqM9BSd1JcRfQg95Jk0gVk7pQMYY5rbEjRcapwfHFe9ubUwvWqqf91ERhhf6hQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست جدید شیطان زرد: دشمن را دچار کابوس کنید - ترامپ ٢٠٢٨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/akhbarefori/675615" target="_blank">📅 23:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675613">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93448d9c96.mp4?token=mpiYBlBFz1oAI3a7ujz-7wrdYBzjpaG9ZvgJDgb5QDM7C0hsTZ6TtvG80JszVZOusZtDYJ9OkM8tV-YSfB-8VKCT5bY_Jz-PLGjh2MStBvr1eJQ8yN8jIwq_bZRdagM1-5hUyBqJdJJPl5mQQbWi3kkVemBXSosilvwB8EEzzTNxDYrraAEYyCDDIWkZaQSBUH-Q30UuwVrznnIW07FLnnGhmWO3uM_tloM8LIPvOrSvHMWQ_Pat9QXz3R0MWgsZCnXRjtKRGWU52iwDozaC5gZzQkuPeZC-3moSpFlRO88jL-PezYQKyQuO6URcXUZPRam6LGRsg5S5VYleMdof6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93448d9c96.mp4?token=mpiYBlBFz1oAI3a7ujz-7wrdYBzjpaG9ZvgJDgb5QDM7C0hsTZ6TtvG80JszVZOusZtDYJ9OkM8tV-YSfB-8VKCT5bY_Jz-PLGjh2MStBvr1eJQ8yN8jIwq_bZRdagM1-5hUyBqJdJJPl5mQQbWi3kkVemBXSosilvwB8EEzzTNxDYrraAEYyCDDIWkZaQSBUH-Q30UuwVrznnIW07FLnnGhmWO3uM_tloM8LIPvOrSvHMWQ_Pat9QXz3R0MWgsZCnXRjtKRGWU52iwDozaC5gZzQkuPeZC-3moSpFlRO88jL-PezYQKyQuO6URcXUZPRam6LGRsg5S5VYleMdof6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
الموت ثبت جهانی شد
🔹
سی‌امین اثر ایران با عنوان «دژ الموت و استحکامات دفاعی وابسته به آن» در فهرست میراث جهانی یونسکو ثبت شد.
#اخبار_قزوین
در فضای مجازی
👇
@akhbarghazvin</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/675613" target="_blank">📅 23:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675611">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rb8V3CIiFryptBN3JbUNKTFBL0_uR1kBxPA5z__dYNCJmYndgLWTyVjixRHfjRJ9M-8b1tMCy4i55dVpfbnWRtVEWpUx_LM7ijmg9FkNGHNXHwF6q5-adroiJI09-AxDoTuDztx6h1rJry8655KDk_JDm-dmIX9FAUov881Qe1FDzIMV7BNmChwkSaL6L81qaxiz7hP-fUklVD17-fngiiqpMeot-jS7BWYENO88gGIUQSVDiM_CWD6z_59T0lgQGCVtLzZCh1y3Zs9AzgIrI8jo3PpSUgzzhl2BJHcikUuELgALfCsZyWq40qwXOxVPsiMuW7jFGOHWE1BA4GR1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5hmxNkYoZ4HDF8KPJnKSvHL3-ATp2utTyauaXiRGaVZKSq-sdmNrybCFZ7KxXjwgk31P2u_97xVVqHHLLf-CKHBrx-0u5-xZKOJgiSqL_7H1Qr6WO9v5ueBlYjnho2zNPDfCYDbdyLtdMOJC4vW3RWTsEgxewO_0yheXwWskyLCY9WEsX69-yMCnGlvI0qj1RH1drVopPEbe9eIkXQnPun8T_lClZr4d92rPIJgjkKTULRSyvIBpbcmA6C87UER94ATcsV0HePbumbEdIet63CTOpoD9xMAPxqMX96AbXJtn4F7RL-m9eYsbcnD6iTYf31kjJHHdE0DruunOvSnXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر برای تربیت دینی نوجوان خود چالش دارید، این کتاب را به فرزندانتان هدیه دهید
🔹
«نامه‌های بلوغ» میراث فکری و تربیتی اندیشمند بزرگ، علی صفایی حائری برای همه جوانانی است که در آستانه انتخاب‌های سرنوشت‌ساز زندگی ایستاده‌اند. او با زبانی صمیمی و عمیق، از بحران‌های بلوغ، آزادی، انتخاب، اخلاق، عمل، رضایت الهی و ساختن شخصیت سخن می‌گوید و همچون پدری دلسوز راه درست زندگی کردن را نشان می‌دهد.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/675611" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675610">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c89c9b87c.mp4?token=toeOs7V_SP1Qgs06ndFEMdLezdgSK-lI1LQyNpg2mC9L33C9Zi9RWC3x51ED2SeYxo1XD-t6go53oGYylVYr-NIl__Ipu7gIvjOp1Gk5RC_F01xPx4f-YtGMIAmVUdAsPPusDceau3VpB-2XUK_fh7pmirWxXkrbI5ypn9_gt1kKmt5Zy6pP_DlAG1biFs1Xfa1w9Qt7C3JZawTY2EAuED0BO7RtFApF3KxTmjZ_XyvleQArYRlobQkjtl9zxQ5wX65HNE397BZZ96qBNTNIHLMO5XToXNILAJE87a_EXKy0b0GhOjDD4zMfVFDOyNGiJjOlmxmyPNZqQWyNn8mn7FmbqA3f0RaQDgmKQokrCdmwBzYrRj6zhqQrK5KUVNfaX_6ThiVbcq6DZrGrqUxLMqCvn3ipZz1oe6BKqh_LIsfsOQFKRtiKbxJ7Eqj_M9Jox4wK0lzZpOJZrWivlEJtJVtPOOR-dPxwApztEMbL8WVc3QcuaFuuF8X4hD21NUUDyP3Bh7UNC2HN8I87SqeEB774oFUfT3zaJuqZml_RU1iYQ4czIOJcKTMXFZEJLMv1_GnM-9LzETuFOGX3KAFaRBmYVOqzM6d3U7hJpWUn9tkYnMVBbvcX-bCkrWSb2GifGdGn6jvTQ8yR4jPu-Q152jMFfDCsqW4gAKaQruvVoHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c89c9b87c.mp4?token=toeOs7V_SP1Qgs06ndFEMdLezdgSK-lI1LQyNpg2mC9L33C9Zi9RWC3x51ED2SeYxo1XD-t6go53oGYylVYr-NIl__Ipu7gIvjOp1Gk5RC_F01xPx4f-YtGMIAmVUdAsPPusDceau3VpB-2XUK_fh7pmirWxXkrbI5ypn9_gt1kKmt5Zy6pP_DlAG1biFs1Xfa1w9Qt7C3JZawTY2EAuED0BO7RtFApF3KxTmjZ_XyvleQArYRlobQkjtl9zxQ5wX65HNE397BZZ96qBNTNIHLMO5XToXNILAJE87a_EXKy0b0GhOjDD4zMfVFDOyNGiJjOlmxmyPNZqQWyNn8mn7FmbqA3f0RaQDgmKQokrCdmwBzYrRj6zhqQrK5KUVNfaX_6ThiVbcq6DZrGrqUxLMqCvn3ipZz1oe6BKqh_LIsfsOQFKRtiKbxJ7Eqj_M9Jox4wK0lzZpOJZrWivlEJtJVtPOOR-dPxwApztEMbL8WVc3QcuaFuuF8X4hD21NUUDyP3Bh7UNC2HN8I87SqeEB774oFUfT3zaJuqZml_RU1iYQ4czIOJcKTMXFZEJLMv1_GnM-9LzETuFOGX3KAFaRBmYVOqzM6d3U7hJpWUn9tkYnMVBbvcX-bCkrWSb2GifGdGn6jvTQ8yR4jPu-Q152jMFfDCsqW4gAKaQruvVoHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از آتش‌سوزی‌های گسترده در پالایشگاه آرامکو در عربستان سعودی پس از پاسخ کوبنده یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/675610" target="_blank">📅 23:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675602">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MPJiC3kIElHZWQyAgMQYqIx52BrHfJVovoeYAp-oVnuK-i2Kh4q016tHpSoSvwKjPORuLuWqXOvLTac9jH5CjnRvUhgQ9Yf9nEKLgoI-MXYretbiw_LnAVd_WH3oi8N2MzBU-pz0bx_S9LfpQYffrF3E42uUxqcqoEu8X_xiFZDPcYGDMKP9yeMWp7y1xKgblhlfx4fZBsF3Sltwqto-rG-UHxlT0jG4ooOTQJUDgcAN8SJ9jClju46s9tXm8kNtxH8mYoY1Tnz7SexBrjtlBLCZP8snZDePTySe2jf-KC1b4U908ZFY6vKisS80yyOI24YwdA2xPl2J85Cx5N4jMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQ2e1W0TmWUTB_QOQ9pNebWuyaW0tlvxNxdYH7hf3SufMXS3X8ipVf_8WHXcxoiD7YnYjBoKK05s0HXR39GA-709sknQxp9-vXNx0NtKZI5sbX1PeYlqXpRkBXyusT_Svs99cQNMUch-_8HlW6pWvmpHkQ1IRZ8Fms7qfQpAtcNnXNjNVIeED1H9yCdtkC1GETZPDGFXNZyp_oIIhfNQfmK58nUfDp-SMGjFB0Yqhc_K0Chn_KwksEdYa8Yw9G3weaGuGnqBI0UN5uRLHryzU7UHLj8tTiLHciSA3-UjUdN97CiG-E9Vu7sODQcqVLuaxkNLdwdhYoXEunXNhKmENg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZxLVfEmfmnlOmWeVIZstBgoStZwbY4bSgVt4E06FtzksEVmYHe0oeAw5hlnlS4L_7Rps86NZWdW3koI5MGmI_ied7gO4KNwaw3DF1dMQU5Kkh8Dm7Zv-q5w_3-XBWG4PeWvZOkeUzDoQhcJXibKSbHFI8lTN4Txcsgma8v27eo18_kOcLvc_L3HQE0X36duAo88u-Iq6jgqzm3-v4_9bdcqJlkX-9HiC1FAhMEoUsCTdRKHTiT6szb4DDdPyBbu4qd-dmBJzhIxrqtVtExh1Ad6cdxefn2JnSOvBy_kbO_nuihnQRxD7AFeeaeAG4tKMx0nWeePbdnDXLnl8R0g6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwWtMdLToGeQ9qV_FSuOf6qEuwJIEwZTwDoGNxeavR0w7PUDCKn-VYiLcIPj9CKy8kqlfu3Rd9XhsfYeiAljFLE-1vmhtB48wNCHDMpAdpkfSjtgR3gMpUggFiIpyk_UOnCrreRuSvnoYc0vk8s-QyWXsmTeliyhDJCvWulFjnlgW2ziuQhrzWn3QlVg8ielYrHqFNU44TG5qCBw4snBW9h1FmWlxA0_4XUN4nOwVubTRcwK2pASYUCFDPt-TBJkqkOrZKtd7kKWoU-A1pRGBj4paLde2kGi8G6p3DPDAZ3EIbXk-AO2ArSgV0gNLQNwXQr0O7cospNXSGiCCnh8wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L21MtjZISGzbG0m5hmGMRs2hPxp9Kzs7csowpbioDX49uav_j34eBDw3t9Zw9fVg8rKKbudU9EVAs93pmo7opguZRArtFLAmP50J88HSJslSgmDDNV9lFlL2oasz9o1_zEzn8vwmRMhT85Fs4SfrgfSjSgCr0OBN74KOmFUEyUKEgP-HCPLp4L38Y7aDKKlupXpxIdnGRDKTxyFCdgLOQpr3Ld0W2BQv_bPBMvLZZ0j_rBY0vdn51Cjx-Bquq_pfmaphZIw6nHxQBMFe94igqB1YkGqt4nIYKfr0dAPWumA30ca4Q0OcsE0k0xhRLVTupRyt1k5eIPYA0P-VFT1lBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f703df7c8.mp4?token=QlhrsrY10Q7nbs9x6kUFWDYgqpDyWazCA9WIRD0ECmjWgj9bJrt4oEulljn1IsBDjcQE1_PDmHVCRwaEmE2R-4wNURE8Eof8uEPKSJYjgN28Jhhf_pkjCNAn3TrohOl9d3q03Q7b_uJ5YKUWXaO3Ll-MUGQUijB9Vg8GGVX49PqjA0v0teEETy5RaS_2QheKE-qTI3ZwzTh65Bjx_uvoNvemSazxVqsqose7rLfgdx4pHDb584MnmatQaix4cUcYdY7xwn6QUj6UDrbqbx3r5Vl6RVarnzbJ6UMFJKS4L4wLJeRDXSRNfN80bmuEySj4MrfSWz5yBFGz8f97dpdVXL6wVqza_LTDYNolniPKKmphjYTYvkyH3wf2ny6Bmrj-6YRSbL5tB3j8z0Rfjp6QWfe0Y5SwU7nwqo1BjXDwyqgeCelbDZt9IqRqWxl3XFZpE7cn9ju3eDn8jdIGRikhk2mUstHHWzkflHpN19xXWB2JBFabesrhKaRVYwhEmWjBjoH-8gVGV4rS1dnkTq4md2cB9MVFXb69JYVDuQqeY-BRsNeNalvevIQ1oKLsRP3h8E-sn105RPuoEdhmb7bfYezkbPiKAr1yZ4JdnNh2gm_5k9FvHHbPh06EsrqmHbFlgwp7gwffMyQQtMvas8Y0pg9ihaLGWO9IL-GXUn_t9Dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f703df7c8.mp4?token=QlhrsrY10Q7nbs9x6kUFWDYgqpDyWazCA9WIRD0ECmjWgj9bJrt4oEulljn1IsBDjcQE1_PDmHVCRwaEmE2R-4wNURE8Eof8uEPKSJYjgN28Jhhf_pkjCNAn3TrohOl9d3q03Q7b_uJ5YKUWXaO3Ll-MUGQUijB9Vg8GGVX49PqjA0v0teEETy5RaS_2QheKE-qTI3ZwzTh65Bjx_uvoNvemSazxVqsqose7rLfgdx4pHDb584MnmatQaix4cUcYdY7xwn6QUj6UDrbqbx3r5Vl6RVarnzbJ6UMFJKS4L4wLJeRDXSRNfN80bmuEySj4MrfSWz5yBFGz8f97dpdVXL6wVqza_LTDYNolniPKKmphjYTYvkyH3wf2ny6Bmrj-6YRSbL5tB3j8z0Rfjp6QWfe0Y5SwU7nwqo1BjXDwyqgeCelbDZt9IqRqWxl3XFZpE7cn9ju3eDn8jdIGRikhk2mUstHHWzkflHpN19xXWB2JBFabesrhKaRVYwhEmWjBjoH-8gVGV4rS1dnkTq4md2cB9MVFXb69JYVDuQqeY-BRsNeNalvevIQ1oKLsRP3h8E-sn105RPuoEdhmb7bfYezkbPiKAr1yZ4JdnNh2gm_5k9FvHHbPh06EsrqmHbFlgwp7gwffMyQQtMvas8Y0pg9ihaLGWO9IL-GXUn_t9Dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش تصویری روز دوم حضور شاعران و نویسندگان ایرانی در اربعین به نیابت از رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/675602" target="_blank">📅 23:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675601">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_dK3AGezak8XH2Ter5t1bDUwHWDogF27xD38zAsK4uK2N2qKcvQbHbdbpC4UAPo3qWODjRcJBkOUZQkazw5afsNBfgk7ooHbbteCBUKq1tAZXRV-sJajvONgtmjc3VWtaIobiVoHUHBUghNzy2hitZp36heKWwkD1_SRKTBdAE5L0lAECTlmUgQC0w9mn9AnE7sqroDYB4jiWWr0W9Ps3qvDYP0pdZvQ794NSi0bb3KJ4sGwbjiAOsCvD1dLMwAVAycYxLUz7YpNNAWhltu2KKcsYbkppYzjoEL9SmXFk2QVb-P8-oy_ZpfQMI4QuBtvZQeX1bBprF-3qPCueTbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سکوت مشکوک و مرموز نتانیاهو در بحبوحه جنگ با آمریکا/ اسرائیل ترسیده یا آماده «جنگ بزرگ» با ایران می شود؟
🔹
اگر اسرائیل وارد جنگ مستقیم با ایران شود، ایران نسبت به فعالیت های این رژیم بیش از پیش حساس می شود و اقدامات اطلاعاتی و جاسوسی موساد سخت‌ می گردد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3233259</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/675601" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675599">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
حدادعادل: انشالله آقا مجتبی سلامت هستند/ روایتی از شغل و درآمد ایشان پیش از رهبری
👇
khabarfoori.com/fa/tiny/news-3233395
🔹
تصاویر حضور چهره‌ها در مراسم تشییع پیکر اکبر عبدی
👇
khabarfoori.com/fa/tiny/news-3233343
🔹
سکوت مشکوک و مرموز نتانیاهو در بحبوحه جنگ با آمریکا/ اسرائیل ترسیده یا آماده «جنگ بزرگ» با ایران می شود؟
👇
khabarfoori.com/fa/tiny/news-3233259
🔹
عجیب اما واقعی/ فوتبال بازی کردن زن مشهور با شکم برآمده
👇
khabarfoori.com/fa/tiny/news-3233331
🔹
تراستی‌ کیست و چه‌ کسی مسئول فرار آنها با میلیاردها دلار پول بیت‌المال است؟
👇
khabarfoori.com/fa/tiny/news-3233211
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/675599" target="_blank">📅 23:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675598">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhCQyj1-SkmSDfbR8BFm1xD04cKjJISueZTStOZDz_IXdI1wboHHfqWw9-_QoLE1h6CPM4NGDsYl0e1wegBfNGrR9D6X4Wrn5hVaI1kBspWNCLExZmzoXAQEA9Gyf7LIMcS-drpPs8tSRK2_vIx2R4k62fU7fKhwBnHR1IAe01_Akrq_uyXZ_sfaapptAkgJkl3F8KGds9BvImrN7_RB_kHjO7bRoEheNPUYZ3u0JXHHSQT66c9ULlKiBfMNW4kxYGRGHn5xGCulZKsIpH6sjinPlZIJy_zLBzpG_Nc2caSq_lCbKU-NXwpbHccNANFtejkq6KJLQcW5aXkXjNpqJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر گستاخانه و عجیبی که شیطان زرد منتشر کرد: حمله به خارک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/675598" target="_blank">📅 23:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675596">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4bX1XDFgQpnfv9WT0CAM9AmLRvtNiMi_H0pmmrovVzqTXKxh29RNvxeO-CSk0l4SP0WlS8aQnHWkF53h37MIT4KoiYC6MGGYSt2iR25KnAJjFgKTYsNP62AhL4dJ_UiUuWdOyOIuIYzXiPHUcy1Lfw2D5_gVg6Z00KXeN4QYh6yX8qmufw3uhXZEAEiQJYYAJErNwz0UN4aeK02Ylc8Mk1NQpCtwpbsvNaWCE-5GarJLj5a4BgUVSvVtEwZYGwctDe1lJetHkGQXnQ48hZ27HefvKF1KKyL-i4UExNXdQmo7-yi0Jqp5l2WnC9lTNM-401SUklofkyg11uCU6V3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریشه‌های شک از نگاه امیرالمؤمنین(ع)
🔹
امام علی(ع) شک را محصول چهار عامل می‌داند: مراء (بحث‌های بی‌حاصل و لجوجانه)، هول (هراس از مواجهه با حقیقت)، تردد (وسواس و دودلی در تصمیم‌گیری) و استسلام (تسلیم منفعلانه در برابر شبهات). این عوامل مانع از رسیدن به یقین…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/675596" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675594">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">🥀
السلام ای محور هنگامه اش
ای همه حرف وصیت نامه اش…
▫️
باز خوانی شعری که در وصف فراق حاج قاسم در محضر امام شهید امت خوانده شده بود اما اینبار متفاوت تر…
💔
@Heyate_gharar</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/675594" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675592">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8eca1d072.mp4?token=CopXoWr7Ikz0DEyyIFWQ3mu7cG9LKSTGkIQrUfFFUwqFITgrDoukOxKgpr-GXcRAr3d8bMlhcOiHC3ZUEFsPiwUYiAM-K-6UtqOwtf2PU39KhLd3ExBwHmFlUVmCJtSR5nHNBfDd2BgU8-t1VlzgdEt6OFgfVscaoNSVwLm2T9xOxLxqb6f4FTUsvncf9JaUijNQ1IcZp8c5zHCVNgWzZV0miBQ9K82kE5fVCDLUA2lVF-6RI9NpiCf5C5nSDtffGHWj8g1TWu0Vr56vvm9ODeGPRQUFmEDxLZi6q_Ft1f4hKBKJ4GtE1AiBH_kMNV48Bx9NxXw_N-1cvEHD1f1JKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8eca1d072.mp4?token=CopXoWr7Ikz0DEyyIFWQ3mu7cG9LKSTGkIQrUfFFUwqFITgrDoukOxKgpr-GXcRAr3d8bMlhcOiHC3ZUEFsPiwUYiAM-K-6UtqOwtf2PU39KhLd3ExBwHmFlUVmCJtSR5nHNBfDd2BgU8-t1VlzgdEt6OFgfVscaoNSVwLm2T9xOxLxqb6f4FTUsvncf9JaUijNQ1IcZp8c5zHCVNgWzZV0miBQ9K82kE5fVCDLUA2lVF-6RI9NpiCf5C5nSDtffGHWj8g1TWu0Vr56vvm9ODeGPRQUFmEDxLZi6q_Ft1f4hKBKJ4GtE1AiBH_kMNV48Bx9NxXw_N-1cvEHD1f1JKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری: آیا با توافق هسته‌ای عربستان سعودی راحت هستید؟
🔹
ما برای مقابله با سلاح هسته‌ای ایران را بمباران می‌کنیم، اما با عربستان هم‌پیمان می‌شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/675592" target="_blank">📅 23:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675590">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf60d3589.mp4?token=ZafnDG-6fGta6-kfam0532wKm11yqOPrK5AvRCx51MvK96QVvrodLMVEKLI1Coy3_HiRiWGGL1F1fPiHQsPgMJ6dJhvBJKsQ1Ff4pkVlmCbDzeXx7nyDYmoAM4oDZofQ9KWUBymKbxJbG6pyUYeWqPvZtdQPF80fx8-3K4SNbnCKBUxP0gAQ1lmQeQALwS0v-yp2eAM5UOFMhHfwvstbxpDDy8lLYCPk_amOBX1W6vKhBPnvKZsJzsRuUIScw9ZaPp3Bk4FOSyGFjGdQGFaReYjnXehdWZEv94N46OMhXwS2DGX3OdKKwG6XnewtcFQm1favQ6B7pybRU7TYIsEBvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf60d3589.mp4?token=ZafnDG-6fGta6-kfam0532wKm11yqOPrK5AvRCx51MvK96QVvrodLMVEKLI1Coy3_HiRiWGGL1F1fPiHQsPgMJ6dJhvBJKsQ1Ff4pkVlmCbDzeXx7nyDYmoAM4oDZofQ9KWUBymKbxJbG6pyUYeWqPvZtdQPF80fx8-3K4SNbnCKBUxP0gAQ1lmQeQALwS0v-yp2eAM5UOFMhHfwvstbxpDDy8lLYCPk_amOBX1W6vKhBPnvKZsJzsRuUIScw9ZaPp3Bk4FOSyGFjGdQGFaReYjnXehdWZEv94N46OMhXwS2DGX3OdKKwG6XnewtcFQm1favQ6B7pybRU7TYIsEBvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بازرسی: برخی تراستی‌ها خیانت کردند
🔹
یک تراستی ۲۰۰ میلیون دلار از سرمایه کشور را برنگرداند و از کشور هم خارج شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/675590" target="_blank">📅 22:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675589">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/996d5978c6.mp4?token=Y31RhMOliYY3npm5LDkmSdu_9_YoZvQml9Pn5Z61ud5FoaeA9D_kCW-QxGLXZSxYA3eMZ3fQJ7w9w6Zb9JT00mPYSLkXviOhUdkiq6034o5EeliIXG399vvEU2leLBPXMoSRd9xaQwdBtBO8O7NWig93Ysnl_TiB92vz2ceFaeFFjwIXRQx1g5hPFr_9vo-XHOjmZW2t3GprBmMFn_DYDuPpwoTEq6Vfb8-S_B_w6YZ9yWXdJLH42k1_0xshzU0e2ixB3LAu4rfHMNJCL0Quly6l83jA_atQmx_hqjh52ces-h4R_TYXAJ4cRrfriMI3oWD0VoKbrkmkEW-65r8nUj-FOTeYIp0jHvJ0n154hQDgLInwu1tJ3XyRyFJdsEmKOLE68yLRS5d_n02V0XqSExCwU34jeUkXtBcglQmziKkr2NLZHgc5UoHEQ1aTT5C_h4iT4nPEIHVRXpX792n2nO65W4yAvGW-vAep6JZHT6mT3J6JtlAlGpV3wN3kzcawMywvTpcSu9dBK58b9fIunLYBxHmgn6pPwQcdBNpn2htMUKRprr3Qfb8QZA7DfSul6A3tPJUeB_32Hts2yuYZ1Lcr8SBijt-tCaA9e1NcsmRdWIiX6XztyxOkS4tLGU6UwxgYPei-LsxBp73uTSCguQat14SkDnea6bc3yyq0ZCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/996d5978c6.mp4?token=Y31RhMOliYY3npm5LDkmSdu_9_YoZvQml9Pn5Z61ud5FoaeA9D_kCW-QxGLXZSxYA3eMZ3fQJ7w9w6Zb9JT00mPYSLkXviOhUdkiq6034o5EeliIXG399vvEU2leLBPXMoSRd9xaQwdBtBO8O7NWig93Ysnl_TiB92vz2ceFaeFFjwIXRQx1g5hPFr_9vo-XHOjmZW2t3GprBmMFn_DYDuPpwoTEq6Vfb8-S_B_w6YZ9yWXdJLH42k1_0xshzU0e2ixB3LAu4rfHMNJCL0Quly6l83jA_atQmx_hqjh52ces-h4R_TYXAJ4cRrfriMI3oWD0VoKbrkmkEW-65r8nUj-FOTeYIp0jHvJ0n154hQDgLInwu1tJ3XyRyFJdsEmKOLE68yLRS5d_n02V0XqSExCwU34jeUkXtBcglQmziKkr2NLZHgc5UoHEQ1aTT5C_h4iT4nPEIHVRXpX792n2nO65W4yAvGW-vAep6JZHT6mT3J6JtlAlGpV3wN3kzcawMywvTpcSu9dBK58b9fIunLYBxHmgn6pPwQcdBNpn2htMUKRprr3Qfb8QZA7DfSul6A3tPJUeB_32Hts2yuYZ1Lcr8SBijt-tCaA9e1NcsmRdWIiX6XztyxOkS4tLGU6UwxgYPei-LsxBp73uTSCguQat14SkDnea6bc3yyq0ZCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کری‌خوانی جنجالی بین دو چهره قهرمان مردان آهنین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/675589" target="_blank">📅 22:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675578">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWNC17oDQiMLu-8DwS1124PmndjuaMRjBOTRrz-2_Cn5J3r-c8qmc8ynJBeVaognyx-O55tMgfg_O8huc8MZJkZu7BTskva4WBfIOqqOjFNE4TY_cYIMBcIskcfypKTB_1ixQP3-QcAUOjnL5ZvTkAWpeT8DH2WlbIz45JBTyGJYQXqawyd4ihobMeXKqwPvt8YJUa5jJgdaV-vuOdHBcP2rvKUvoWPDCxgZQMiSWtmBwzvzMpnxKTvJDokLKwMWCUI3grC5di0oLMHhxt2Si8foGUrLQJYQ5QbNoWxWtMwZma6HpKPeXGU8QN4rNeaO0P9-avhc6WeZBrWS7_HhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cfh3-J2jtMowk2dISDjvstvQfpnULNp9KR2g23FNV14AJ-cD_q5JK6GC9HKSOuEmUQOMKprLvJNcZDs38dsm2ws9PQ54M_usIFQPPLQ5-ekvaxx225EWBHJz82Gq9fy1mb5uq5_k800N25hkXbg5XNBhOamJm16DVqoYYethQvfY0WCJe8c4nlqPuK-OJwZXlJ6eWlhtyeUxchOL66VosAL1aujCk47ratml4NgQf8qxQUiFkUkLjpbN3J28FxH_1SM89KcotfgTfkVZ0GDAT51beYbyFNiYfWGurLc9h4pds4gLjz9SXSW37YRvlX-F2iRgQQX0N0dr1kmezs7tMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNaRPfyTv0X6S1b3UxTKJRINwRCjNN9_RrVamN_vGskCg3ETAQ-yDLkeTz83luLDqef3j5Ztsks43Uf0joQp8nTdqMo-oS6wZg1EzHon5LvzWtyzqruq654kNahnKR9_VxCesjX8xQq5rRcNit0bZtCKJi55k9M3liu00cQ6f_I9M0bx19rMii3Xgyq1vUzJzYDb1KYsQSIS4J9Foi3qr-_B1jTBk5htQuCLjLQFYf-8gFturZ8NttNYuLye9e32CxZiJJjm3jDBxIRTapHdDyiQ_15mJms-oATnvRBGF0O2UL50wonP52bYHxv6BenwGuBqUz3YyIx4CHP2Bhia8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IwFPuan3dgEnRindrH9XRMinUZtK1J6cxBNtk5NlIrvW0eJTV7wwWKYMa4NHOaXsAd6Dbq-En3qkCXMkKIY9Z-OTA67RNIdm6Pdj24ixRjvM-YXboEqffkdQjV_3q7tKjvruRFxcyC5TTBGonRY3HlCbzfMSJnwHg0FP-LZUzebgAEuwAhiFL17OpydFYU9AgvxaxlFOOwvtIABwSRBBOVjSwxum0IKCSWNx3jto4zwwFxaxZy4BK6qvrGp3_06EuwGx0B1Zz9vwkkzVghhlx3zBhWahvBh_BFqDEEDXjlJCIjP-bdcgm2qLc8mAjiCFGi5BwWuYCM00B0BCUxSbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMH7J03AEXPPtS_maOnRLC306eFjAWO4N8SFh3cmyhaMSYkTESYdBkSUgd_4qXOLI8RajF4ShVXYZikUIp-vPSqdOxxQqBLe6DKDfhJia7KY3uNVC_CP-MtmmQjPPXrTtlZAp6o274iZEXw58SzQvUYHAVtHWyuSNIfJBGRaBaNgh9S1KJ5dhfysJ118VgtYFAQOiFk5fGfC_s3D5ruFOtbgC32n816OfGAMDGFTZ3xnlz83XM6fCYar9TrKA5wU3AOzC7Qv_VKLkSNyTdNKwcT70u-_k5JOgkO5KzfUbxlHYar5R6-Hx0NZJdkrBCwvBj9pkb45pjpKqzGaJCR3VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cs3rpZkGWheD8BPhkVb3hMEhVUBv-msQoTLNnqxHzYFDo8hOfgSthWtkPztbTuo6Jw1MZ0yY9dBizRRjnOGYUiRTqbUaQcCTAiCtfTrbx_vfFIbTix6GAzrE94yE5QngLw-z32nTZCDXIKb8rXjlTKKrJn3H-L4psVUNuvnVGHRp6w4YxC9wPRFDJNByfOL2zawrPl8HTCWaOAS0RhZofZdpvmcAvC_WwbPGjOBi3brf-bxJacyjOOrIXr0GfrT3FLNbfp8rovnmOWVfntXjSVn-iGKz_5FZygei3I8GOp9_9uZQpNXwDperKB7Da6HL8nHGt3lcCZ6Rc6j25YwSHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVbu9nDxS8BsfADOGgjffhpKGXhS09Ng-Bd6EsoXO8DWsDpcQG1WqB_-H8pTMtr_CiokPwY2O2FNNetTCWhFs1AYntU9fZCUAPEQCrI12OW--hJBXPFFjcnTot4kV0ik9txMqU7_CekAGbJrmlUP3Gf1CbrI6R6Wnj2ezr1nHCL0EM547pahVtktStZyc3f-3nTuO5GwMbuzCKF3yh8IevbywVFEq93XI-GB7RJW_yVPULloMwv0_5xfWD98nY--RHQZ3cu5xF_1qjSQNp_ysEbIXLzN0O5JcJX9ruWHvkSClZuacBYRFBBnxA2wdxh1VOzXj1ClS1TJ3ZQIR77tag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYky0k_3CYKEu989XW-VOd_EtggpJwfsCz3OUx4Mt_eF4HP1f6Zw2pWiR1UFAPT-k2scWrDalkqxfdZYu0t0qSq1DY9ce2cBOPNR9TXSEPjlVPvYHqOcdwiDku0FGsoPfA8j46IUjb-kaHvDy5ZBqNLaZeFMi0Nwj6kZi1Vgl6du4wz1ZJufS_W8ITHcd3LNAHES2jww4OXOmRacdhmQqLhI66UdCwipmRDYOnQukR057RLSpOUH0OUbbh1BVNSBynz21StgPJS84amOkeK6N5A59eFNGRwZuq1uqSBOi6FusKoArOqQ_DQ2mDjCpGfFENZmn0B8oBH_um5HlMaQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nBEOEG9roZN5Fdfxj1xo4-kB6n75kB1fxLg1yjdDaVKuXXD0kcz7nlQmlPG6qI3B1fmEPpRWxVAZZH8M4V1GESholnFBs0jiKeCv24q2trwDmhjLcB0vuhfEQbNnF688lDvUGrXW_czZWBWCW8TKcCktKRKcuUfEkgUybjWGp31tYSp6ZzOPhm3B2QTHuL1gQHqX51JRxYwbVgiGb7ZaGqfRoosBE8GVtm3Ed493ddOKCePO_Bgu_2FxQ5T5ciSI_C3cYRv1OTRSae_FOxzu1YKcuqHwI1EWg59zbbqujFG36a8Iaoac-GM3a8NDwNUrzc2ZVexnkh9z70WKEDKTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfnAamTJg3mMBSY878mrLp_E_9qxmu4xwwOGhK5oY3PMFDRF5unPXhUKb-XQSyIXIB4tr3F1_ux17uTdUU8RD9ORrsy58as2S4u6LPROIDAKrffJOuaAmuY3XM1a_jqGiV-EuxT1tYU_RyH6kroYP1HOsiqARQ3htclDOptLsj-oyt6B9UnZ1y3auXs328E6jSjIbwUo26abLnCR8JwphLfRPKSuqK5VmDsz_CmdVtaiNwSLGs77Aivf9Ih045LBp1nl-_Uay4RiMHt49VStU_Be-qmi6m52Ud5blKuwS1OvuEQyWDFhbROlkacIh_6XFOKcBUCeycOUWsWQLZHJlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت راهِ حسین(ع)
💫
✨
راه امام حسین علیه‌السلام، راهِ مهر، ایثار و دستگیری از مردم است.
🌱
این روزها
#هیات_قرار
با همراهی شما مردم عزیز، با توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های حائز صلاحیت گام برمی‌دارد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/675578" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675577">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5vcS3yYoglAd6FuYvbhev5pdu1_LLO1Lp7LJ8MK9IaOAdzp4Y-455oBctWSrfJPfaxHGVC1FYoww6Qq6MNcogJC40h2Wmu29shcDL7iZ6W4aUnuAgGhWdEpgoglDCdFzgp7onFtETTMfBI7EKQK6kHA_6TbYFT8KEdeigFwZ2taPrVHrbINbMiDT_4mmbymOEO_adQX-UdM73ZpKJngxk9_eDUJIT08BnaAnLYpUDEFVeSbRIX0WYUGItzP_tBnalDPt5s3iiTt95ZllaAgX4T6Oi6YrRzrv3PvEe7cMBaabgQ1nTdk9hcGG4cxMAJJ6UNTuIuZ4YjRJQMAEXk9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو: ایرانی ها سلاح شیمیایی دارند تهدیدی برای جهان هست
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/675577" target="_blank">📅 22:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675575">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7dfcd159a.mp4?token=EX8CAnJPgOPp8-CMl0iF75OlQlibuVVRB5ddDuMCYAydQjH7zXXhraWwSIWLbWpqsz6M6kQjzYesYb_fFOxN_3gu3ysbwSv2LqsQnWpkWcHonzMOhPjOQRDmGN1YQm_Nv2a1S0i2tIGvJd-puGTrgOa3uowwfKsCfiuode6csFwQoGNchyzNBb62mi8UWLE858XvEQmeLW6ojwi0eP6ZoHpbE6dLcIiTGh3wPZhBP7jII1pTkum790kFWcejfB29qPhB5S2sTLxz8q6Pq6kyYpapQHK7svS3AMt_dLupIqB1z8ycOB_aNTxF3iApg4Jn3K1X36hd_cfnluKS-QcUWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7dfcd159a.mp4?token=EX8CAnJPgOPp8-CMl0iF75OlQlibuVVRB5ddDuMCYAydQjH7zXXhraWwSIWLbWpqsz6M6kQjzYesYb_fFOxN_3gu3ysbwSv2LqsQnWpkWcHonzMOhPjOQRDmGN1YQm_Nv2a1S0i2tIGvJd-puGTrgOa3uowwfKsCfiuode6csFwQoGNchyzNBb62mi8UWLE858XvEQmeLW6ojwi0eP6ZoHpbE6dLcIiTGh3wPZhBP7jII1pTkum790kFWcejfB29qPhB5S2sTLxz8q6Pq6kyYpapQHK7svS3AMt_dLupIqB1z8ycOB_aNTxF3iApg4Jn3K1X36hd_cfnluKS-QcUWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدرت ایران از خانه‌های ما آغاز می‌شود
🔹
هر قطره آبی که حفظ می‌شود، هر لقمه‌ای که هدر نمی‌رود و هر کیلووات برقی که بی‌دلیل مصرف نمی‌شود، سرمایه‌ای است که برای فردای این سرزمین باقی می‌ماند.
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/675575" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675574">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aad3726c0.mp4?token=Uk9WfhQlHN7aUaiCzaOfIogrDYM7-Q4hKdgZWAt-B3y0zcl6ylsWbJMjGcFRJnczMDy81JgDIUrBVLEvQSIa54MrbNefNN1rT-89qMCkQwUYK_9gkNgsjAw53kAO7wQzCzmhkKNE1bgzVwbmb4N-JycOz1Ic0y9ISqJ3cEOwxz92_W_LBPzGIX0FUi9HIUUvLarOdtydmRBiwj5fCIy7eLxIKr7VN-DuPrP6AxN1GhZqaefRI6SXMFlSsqA6dSk4d6zBwnVldM3lei9djnomc3Nc6bAqSWvfjDLgdCkhWdhptFp5SeqgWUb11-V2EVThbVYY5IeXMG-yT6YWUdjQwUSYkJpsprSG6hNhxOgsZRNjAx9BR7tkxSoqbL5g2kuR8tvpomLOgoS4aa7eRQWjOiDRvXde8af-Hge6_bSGv_HluuKqOuHNXkThW07p_6yPj72E58Faf1q2q4Wkq_9spTK-L1NjvDkI10lUO9T9kb6N1rAE66jkMgasfa2zK-H1RdBkei319QzRrWQ_4z5yiz3M1Kc3ranh_FYxzEgTnfGWZlcitBpEJo2YS2xFfJiObalUiv7Bx_eW0QsW8Kgu1NYIU9mGrsLiBAt2qmKcFpn-_VIuOAGq9tBEXIzH67Et03N2_rDF3i-xcc3ksNyhaFwJ3PfUMB-RBLoB7OV4WTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aad3726c0.mp4?token=Uk9WfhQlHN7aUaiCzaOfIogrDYM7-Q4hKdgZWAt-B3y0zcl6ylsWbJMjGcFRJnczMDy81JgDIUrBVLEvQSIa54MrbNefNN1rT-89qMCkQwUYK_9gkNgsjAw53kAO7wQzCzmhkKNE1bgzVwbmb4N-JycOz1Ic0y9ISqJ3cEOwxz92_W_LBPzGIX0FUi9HIUUvLarOdtydmRBiwj5fCIy7eLxIKr7VN-DuPrP6AxN1GhZqaefRI6SXMFlSsqA6dSk4d6zBwnVldM3lei9djnomc3Nc6bAqSWvfjDLgdCkhWdhptFp5SeqgWUb11-V2EVThbVYY5IeXMG-yT6YWUdjQwUSYkJpsprSG6hNhxOgsZRNjAx9BR7tkxSoqbL5g2kuR8tvpomLOgoS4aa7eRQWjOiDRvXde8af-Hge6_bSGv_HluuKqOuHNXkThW07p_6yPj72E58Faf1q2q4Wkq_9spTK-L1NjvDkI10lUO9T9kb6N1rAE66jkMgasfa2zK-H1RdBkei319QzRrWQ_4z5yiz3M1Kc3ranh_FYxzEgTnfGWZlcitBpEJo2YS2xFfJiObalUiv7Bx_eW0QsW8Kgu1NYIU9mGrsLiBAt2qmKcFpn-_VIuOAGq9tBEXIzH67Et03N2_rDF3i-xcc3ksNyhaFwJ3PfUMB-RBLoB7OV4WTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی جدید از حمله ارتش یمن به منطقه جیزان عربستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/675574" target="_blank">📅 22:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675573">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad6e203b4.mp4?token=fm3Xf5nk2EEFmmSTijJ9tWFDEA70v_AL0QrxIANJkXaWpHU4WXWlGX0veNVOz_JdkAURlWmE0G5ucE8EjH2M_Q6oEzIrYqLyXs1PDy9HxUun3FFRjEaO_NfLRLRgpnNDklV6laEWme8kgxgzY8d_rH8ms8konSfnQ8DjSECaoZMyYmC6t_rSL4zhg7iLtxi4qQf6eIu1F_WY-WLCvU9yVvLGqnaRlb8PSb7TzJoH3rwaMb4ObF14fkzg9zSNOaBfBPRrFngqL1JfDmBdFM7Q2-Qych71q4-wYEtAQIOpU5WJXXNyFM14v4IoIK6JsbC0E_8gL3KEh8U-d4wyrhmE6hxKzws5FbytmTSuUpIZmi7NG8fGxwCxLwerZ1EEG5NRhiOrUjxH8qwyFR7L2i3eL5JcT2l-HlTzNVE52zQiMXF1WvvDlgySGfRcmz7vd3LAWaRXXmZ1swthjfIb-qYe3jbvWR1G9mJ1HenTOID9xgNTXYkcRvo0oKplxsqcPXMtrlVeZFxXVv_7LWhvaoetR70tcFC3kdBfvhs6ZRpYlMSYz8tLp8Ew3fY5R4QZYb3zQ7Crxin_Jodv48dK2AX2LgTQpvaBGW-cx7DRVSRHxV28IHcM2FDjLUgO8xl_0U_bBS4H-91fWlqMfjihdyv8bQ1n3sIhk_7DFyKZFunQG9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad6e203b4.mp4?token=fm3Xf5nk2EEFmmSTijJ9tWFDEA70v_AL0QrxIANJkXaWpHU4WXWlGX0veNVOz_JdkAURlWmE0G5ucE8EjH2M_Q6oEzIrYqLyXs1PDy9HxUun3FFRjEaO_NfLRLRgpnNDklV6laEWme8kgxgzY8d_rH8ms8konSfnQ8DjSECaoZMyYmC6t_rSL4zhg7iLtxi4qQf6eIu1F_WY-WLCvU9yVvLGqnaRlb8PSb7TzJoH3rwaMb4ObF14fkzg9zSNOaBfBPRrFngqL1JfDmBdFM7Q2-Qych71q4-wYEtAQIOpU5WJXXNyFM14v4IoIK6JsbC0E_8gL3KEh8U-d4wyrhmE6hxKzws5FbytmTSuUpIZmi7NG8fGxwCxLwerZ1EEG5NRhiOrUjxH8qwyFR7L2i3eL5JcT2l-HlTzNVE52zQiMXF1WvvDlgySGfRcmz7vd3LAWaRXXmZ1swthjfIb-qYe3jbvWR1G9mJ1HenTOID9xgNTXYkcRvo0oKplxsqcPXMtrlVeZFxXVv_7LWhvaoetR70tcFC3kdBfvhs6ZRpYlMSYz8tLp8Ew3fY5R4QZYb3zQ7Crxin_Jodv48dK2AX2LgTQpvaBGW-cx7DRVSRHxV28IHcM2FDjLUgO8xl_0U_bBS4H-91fWlqMfjihdyv8bQ1n3sIhk_7DFyKZFunQG9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رازهای پخت یک کباب تابه‌ای خوشمزه رو از زبان خودش بشنوید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/675573" target="_blank">📅 22:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675571">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942771bc59.mp4?token=QH-Wde4MKbWQcJ1HRsrOzrCZX5kE2r4XSdUM3uejYGcr2-jNjQGVqX6ch4ymWfmMEHDCpASxS1vS_pxPPqLiyv9kmCW2P8z9xpToDZ37X37k3Y0S_V2ZLANA4Gai14XEqA0RiM1GhXSH8tCOgpAOSF-bcVKFxt00AG0aLYCkew_YHFvxPDT5hHWEQiqTSNXVt9_xXPZIXC9tn6MN3nH2IP96ZZSkaBwf4IVP8WYiaBv9WmpCXPfVQELluMRiWLDoKVb4KSpR8VIKadKVMGaIiLnqun4voVqYIdwq7f6bTXCNY0zzc-hjsfG1cnU2r73VcOM5o6869JptzJaRBlNb8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942771bc59.mp4?token=QH-Wde4MKbWQcJ1HRsrOzrCZX5kE2r4XSdUM3uejYGcr2-jNjQGVqX6ch4ymWfmMEHDCpASxS1vS_pxPPqLiyv9kmCW2P8z9xpToDZ37X37k3Y0S_V2ZLANA4Gai14XEqA0RiM1GhXSH8tCOgpAOSF-bcVKFxt00AG0aLYCkew_YHFvxPDT5hHWEQiqTSNXVt9_xXPZIXC9tn6MN3nH2IP96ZZSkaBwf4IVP8WYiaBv9WmpCXPfVQELluMRiWLDoKVb4KSpR8VIKadKVMGaIiLnqun4voVqYIdwq7f6bTXCNY0zzc-hjsfG1cnU2r73VcOM5o6869JptzJaRBlNb8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: جنگل پرتقال
🔹
ژانر: درام، عاشقانه
🔹
خلاصه: جنگل پرتقال، درامی آرام، شاعرانه و تأثیرگذار است. این فیلم داستان معلمی را روایت می‌کند که برای دریافت مدرک دانشگاهی‌اش به شهر محل تحصیلش بازمی‌گردد؛ سفری که او را با عشق‌های ناتمام، خاطرات فراموش‌شده…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/675571" target="_blank">📅 22:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675566">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
یمن ۳ نفتکش سعودی را هدف قرار داد
🔹
شبکه المیادین به نقل از یک منبع ویژه خبر داد که نیروهای مسلح یمن طی ۴۸ ساعت گذشته ۳ نفتکش سعودی را هدف قرار داده‌اند.
🔹
تعداد کشتی‌های عربستانی که از دوشنبه گذشته تا امروز یکشنبه برگشت داده شده‌اند و اجازه عبور پیدا نکرده‌اند، به ۱۶ کشتی رسیده است.
🔹
این منبع همچنین خبر داد، از زمان آغاز محاصره یمن، تاکنون هیچ نفتکش سعودی از باب‌المندب عبور نکرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/675566" target="_blank">📅 21:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675564">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
الجزیره انگلیسی: ایران می‌تواند با پهپاد یا موشک «کی‌یف» را هدف قرار دهد
🔹
تحلیلگران بر این باورند که واکنش ایران به حمله اخیر اوکراین به دریای خزر بر اساس ملاحظات سیاسی گرفته خواهد شد.
🔹
از لحاظ فنی نیز این امکان وجود دارد، چراکه فاصله کی‌یف تا تهران کمتر از ۲۰۰۰ کیلومتر (۱۲۴۰ مایل) است و این فاصله در برد موشک‌ها و پهپادهای ایران قرار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/675564" target="_blank">📅 21:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675563">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldFHXiHYa3I36KPl5B6RdysDcDWrPz22Cmx0mVvZAlxwyNCynv1aXEwim7IiyVr6I4X9yWur-yVKiO76DyRUTmJkk7_EzrmxV_wehk0edtZUPyVFV2SGiODyruMez3UNkWcwZO6GoDReUpPDI7KrkBv-u_zrY6XOCwaeI-3hxr5iYKtnncuHUisqHiDwbwqNoQzJnIymFiMBfvWwbny-FrPXma3LfWvIEAdlupHAE_yq0RiBAggva1G9PwI5owe4LLtrfl3ahqHL9OJOAVtcE2XHobVt7-dwv6adVMdcIdpXah7Ys-MKKPIb1fzaMpFGVFM7-OUGlGScuLz6hnL_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شرط اول
رهبر معظم انقلاب در پاسخ به نامه دبیرکل و رزمندگان حزب الله لبنان فرمودند:
🔹
جمهوری اسلامی ایران نیز در راستای خط مشی رهبر معظم و شهید انقلاب امام سید علی خامنه‌ای رضوان الله تعالی علیه دفاع از این مجاهدان مظلوم و مقتدر را سیاست راهبردی خود تعیین کرده و حفظ تمامیت ارضی لبنان و رفع کامل و بدون قید و شرط تجاوز رژیم صهیونیستی را به عنوان شرط اول تفاهم نامه ی پایان جنگ تحمیلی با امریکای متجاوز قرار داده است.
🔹
هشتصدوبیستمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/675563" target="_blank">📅 21:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675562">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIjvCf4fkp6pEMFOS4IrKvv2HllkYfHQ1jq77SoeTC0_nuKsbSLols7_bfEuYokViPRUPZFcGNYRXXVZDnHx630ztiARp6GdA8Kt2sy6Y7jMMD3LmLy6xqcEq-KNv6iRNS1UgtqnWZDFq-B9BP0sK4W93FWoO78pUWGf2CgmS9zhDPaASIGIoT2Biv4LsAcKcyp-EQvoXHHsRy9dqXEYghfa_aueo9kqK_UE_SZ3tDX-O52iV8yIKz-INCJGq9srfaWy6FexZmYDQQoxczNIN1-ShbIPnsWE8ohihL-dtzlSJ3x4baJkcERXlohoGs1CPi8UosA3S0AuM_08x22H4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگر دلت هوای زیارت اربعین کرده، این فرصت را از دست نده...
‼️
🔸
با پویش «زیارت به نیابت امام شهید» می‌توانی هم به نیابت از رهبر شهید انقلاب در پیاده‌روی اربعین سهیم باشی و هم شانس حضور در سفر کربلا را پیدا کنی.
🔸
به همت هیئت قرار، ۱۰۰۱ نفر به قید قرعه راهی کربلای معلی خواهند شد.
📲
برای پیوستن به پویش و شرکت در قرعه‌کشی، عدد ۲ را به سامانه ۳۰۰۰۱۱۵۲ پیامک کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/675562" target="_blank">📅 21:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675560">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قیمت برنج و حبوبات تا ۲۵ درصد کم شد
رضا کنگری، رئیس اتحادیه بنکداران مواد غذایی تهران در
#گفتگو
با خبرفوری:
🔹
با آغاز فصل برداشت، قیمت برنج ایرانی و حبوبات بین ۲۰ تا ۲۵ درصد کاهش یافته و امسال برخلاف سال‌های گذشته، کمبود یا افزایش قیمت در مورد این اقلام نداریم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/675560" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675559">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان درباره مدیریت آینده تنگه هرمز
سی‌ان‌ان به نقل از منابع آگاه:
🔹
عمان پیشنهاد ایجاد یک ائتلاف منطقه‌ای برای ارائه خدمات در تنگه هرمز، مشابه آنچه در تنگه مالاکا انجام می‌شود، را مطرح کرده است.
🔹
پیشنهاد عمان شامل سازوکاری برای پرداخت داوطلبانه در ازای خدماتی است که در تنگه هرمز ارائه می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/675559" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675557">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
انفجار بمب جاده‌ای و انفجاری در مسیر ترانزیتی زاهدان ـ خاش
🔹
گروهک ضدانقلاب به تخریب زیرساخت‌ها روی آورد
🔹
عصر امروز در محور زاهدان ـ خاش یکی از گروهک‌های ضدانقلاب با کار گذاشتن بمب جاده‌ای و انفجار آن به تاسی از آمریکا و رژیم صهیونیستی در زدن زیر ساخت‌های شهری، باعث گردید تا بخش اعظمی از آسفالت جاده تخریب، و این محور مواصلاتی مسدود شود.
🔹
در حال حاضر با حضور عوامل اداره راهداری، پلیس راه با یک طرفه کردن مسیر، تردد با کندی در حال انجام است.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/675557" target="_blank">📅 21:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675556">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkX0-LS5qnRpqPAbahiyL8fnInYZ-dj3WwZsNZTUxyugwpDuqJ5FoCHXbwgE9RAf_Uo09pUkzViNDfPZtedVYRHkVmZ9lQpd_2KrSUj35wap91lpp30pEOjvS1e-c9PRDnlMq7ZlxBci_IjNSCn6q8ttK6wSSg6r420q9nMVkd75UTr8-Vn5fNfZE9Y34NxCvYXuVj3fAR_bD2mUmGNC7lcA3fhOg7i_cnx_q4emM7oP5WPDaUM78894wlkxNZVCV89lmir8QHL34XxshYzYTWyVMpiDBwTzxVTa8L95f2C6bIhS-3E6tZTI2wfHPrsjTUQAMFUS_0cJ81p7Dt3wEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رواق دارالذکر به روی زائران امام رضا(ع) آغوش گشود
🔹
رواق مبارکه دارالذکر، مدفن مطهر رهبر شهید انقلاب اسلامی به روی عاشقان و زائران حضرت امام رضا علیه‌السلام آغوش گشود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/675556" target="_blank">📅 21:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675548">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4oGxAxcYggueMBR5zcH4E5EPm31B0cuC-Fdw36Xytlv0WG_O4VhXaVrvOYbdQXIyK3mQqqi2jGKdfzML_uo9t-zg2d961eMVEPiJ843Ur5Y6wZxJh0acOZojIoPbKYXsSKh1Lv7PqEUK1wrOtYUGxpbMDwdmehzlwXSD6p5lqanGp-uAUb7cjtzioKwx0c_nfCcSOfdCgIBTq93GQQjYbZMH5Z_0pL8HZ3OpNbeUxdJMuFKctFyBhywqtnq_AZFCXjcaJulWDFuukTaaaHoiQ4Ciy3yuN8M2MupX4B0SMKSStHWS4BeMMlPMWfk4cC0NYT7f2oeV1L3gSJ9P3aUDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnkvYYqM-65WPhzpZyPv5tZy641aoLfE6tlHRoKKkQDNBHOOVbecCZ5ydaKXTDOZcLjXA0gAdcnXLUOvPpVxDqTmRCvDxnKsA5gZ4ngU7ZR3YJyLaesqZFeOvE5qwFx6vLbuc2D-3o_WNccfoTSKlMXKW-agaz_jiS0ffBL1XBZqHobAJsV4VrJAScKPQtf1voRZQW3pDiPNU2EfFsi1aqsCQJ0_ABSJhM0zFDdGVshg6KjKWaD2kbyXcNDO-BVsGOiPrM_Pp9O7cnyFr25CR5mRpNZK-iA0hUFCSrvMbYOYNVnhFdsNt9Qb3GiQFbAxg6quSOEbhj2b_Y2VtkSLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQfqsDKkNoDtErHvJh3wAUyaM4HVnv0J2aaL6fAYdoVC6oYnMAk2Vv4yt-sGWVnaoVjJC2bZZM783W5immpVs4rzTeumZDa6neus8DHNdTRDqbkTX4aNlmQcV72pIPJ7jHxvWS9rwsuGGBx0YrWxVIxVbcZ0u_68xUNLv2ZIjm-ZDBPC8M3Rh6eH-IKaaSWj_7Z-sfaW-YUHsEjwpkcMAr6uRcYy92CwT__0fNtaMKKaHtGu0FDDnb8FA2gQHzwnjOoQ2E9B2qEYWvPeY7EW2sKUQWfvx4rMEEb3bltZpO69FJE5UEFrmur40m70uzqy2e62UmMYWeIpZ6B8oOD1tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۸۳ درصد جوانان آمریکایی خواهان اتمام فوری جنگ با ایران
🔹
سی‌بی‌اس‌نیوز در یک نظرسنجی نظرات عموم مردم آمریکا دربارۀ جنگ با ایران را بررسی کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/675548" target="_blank">📅 21:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675546">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48a0e4ce7.mp4?token=CgkLwgR7HJMzzbCAopNuGkkRgi8WPEJU54v0N27Q7tC8253-tydIZvIMANrwh4OuNzMwbpDyaS9s0qw7CHyJMerb8iDfGotznzQCRakWGQcBy_Z0dp6-UCPK9c7X2Vhgo4WSSGg8aa6cccUbWWVbcfsxGBUa6n7L7ifNSLX64_CqwoVlWvR2lciSFkNEu07MlnH0mNdkG86Uu5N9bDmgp5Ci-WBnr-LLVrbWYdMkbYUrSAWteAXmTZ_PBe1x3643vgYjXG9dS09JMri9IW8_mh9u5bVKCh4p3KVmTmjA8utSrm7xs2bOpKhLDbyHiM_hLGy4lNWS3CHBYtYcM_Xd4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48a0e4ce7.mp4?token=CgkLwgR7HJMzzbCAopNuGkkRgi8WPEJU54v0N27Q7tC8253-tydIZvIMANrwh4OuNzMwbpDyaS9s0qw7CHyJMerb8iDfGotznzQCRakWGQcBy_Z0dp6-UCPK9c7X2Vhgo4WSSGg8aa6cccUbWWVbcfsxGBUa6n7L7ifNSLX64_CqwoVlWvR2lciSFkNEu07MlnH0mNdkG86Uu5N9bDmgp5Ci-WBnr-LLVrbWYdMkbYUrSAWteAXmTZ_PBe1x3643vgYjXG9dS09JMri9IW8_mh9u5bVKCh4p3KVmTmjA8utSrm7xs2bOpKhLDbyHiM_hLGy4lNWS3CHBYtYcM_Xd4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رواق دارالذکر به روی زائران امام رضا(ع) آغوش گشود
🔹
رواق مبارکه دارالذکر، مدفن مطهر رهبر شهید انقلاب اسلامی به روی عاشقان و زائران حضرت امام رضا علیه‌السلام آغوش گشود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/675546" target="_blank">📅 20:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675541">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
فرمانده سنتکام مدعی شد جزئیات حمله بعدی آمریکا را بیان میکند
آکسیوس مدعی شد:
🔹
فرمانده سنتکام گفت گام بعدی احتمالی ارتش آمریکا، از سرگیری عملیات نظامی گسترده برای نابودی ۲۰ درصد از اهدافی است که نیروهای آمریکایی در جریان عملیات «خشم حماسی» تعیین کرده بودند اما مورد حمله قرار نداده بودند.
🔹
کوپر گفته در صورت عدم تصمیم به بازگشت به عملیات نظامی گسترده، ادامهٔ کارزار بمباران دو هفتهٔ اخیر بی‌فایده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/675541" target="_blank">📅 20:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675540">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpMWyy2u5i8o032Ms2NuLRbcb9zbyovBNjEa9gki5cA6oAXac_Cj-5Nr7dQxMFMs4BQksPc0VNk9QHzBs3lWZUbAPwKU0IXrU4YBBv4gNzpoO0oJi4DeS-UlD_D7HC8HJlvkZdiJhT-TDcLS8DHEh-Wk2iTFmLVBPPt4BfGjSRGBGDRigLOKwpCV9EF5Wi42yijVZvbBZl-uhXNMLv_w98K0L06gHk5YJ_eFE8SP3pWzyUEfo4nS8HTHEywDRypDMyYuPrPEbALw_t1Uh_94wEqfSrTUeZSvAScMGOhpo494UPxG86JtZzE79o1-7RPzxVzm5L7LDszRWNGIp0rjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهاد و مقاومت رزمندگان حزب‌الله، عزّت و سربلندی لبنان را در جهان اسلام رقم زد
🔹
سلام خدا بر روح ملکوتی سیّدالشّهدای حزب‌الله سیّدحسن نصرالله و همه‌ی فرماندهان سَلَف مقاومت و یاران شهیدش رضوان‌الله تعالی‌علیهم‌اجمعین که نهال مقاومت اسلامی را به درختی تنومند مبدّل کردند که اصلُها ثابت و فرعُها فی‌السّماء، رزمندگانی که با جهاد و مقاومت خود، عزّت و سربلندی لبنان را در جهان اسلام به ارمغان آورده‌اند.
🔹
بخشی از پاسخ رهبر انقلاب اسلامی به نامه بیعت دبیرکل و رزمندگان حزب‌الله لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/675540" target="_blank">📅 20:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675539">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
جهاد شهدا، مقاومت اسلامی را به درختی تنومند تبدیل کرده و عزت لبنان را رقم زده‌ است
🔹
صلوات و رحمت خدای متعال بر شهدا و مجروحین و خانواده‌های صبور آنان، مهاجران فی‌سبیل‌الله که تحمّل مصائب را بر خود هموار کردند. سلام خدا بر روح ملکوتی سیّدالشّهدای حزب‌الله سیّدحسن نصرالله و همه‌ی فرماندهان سَلَف مقاومت و یاران شهیدش رضوان‌الله تعالی‌علیهم‌اجمعین که نهال مقاومت اسلامی را به درختی تنومند مبدّل کردند که اصلُها ثابت و فرعُها فی‌السّماء، رزمندگانی که با جهاد و مقاومت خود، عزّت و سربلندی لبنان را در جهان اسلام به ارمغان آورده‌اند.
🔹
امیدوارم به برکت دعای خیر سرورمان عجّل‌الله‌تعالی‌فرجه‌الشّریف انواع عنایات و الطاف الهیّه شامل حال همه‌ی مجاهدان و شهدا و جانبازان مقاومت و مهاجران و خانواده‌های صبور آنان باشد.
«وَنُرِيدُ أَنْ نَمُنَّ عَلَى الَّذِينَ اسْتُضْعِفُوا فِي الْأَرْضِ وَنَجْعَلَهُمْ أَئِمَّةً وَنَجْعَلَهُمُ الْوَارِثِينَ»
🔹
بخشی از پاسخ رهبر انقلاب اسلامی به نامه بیعت دبیرکل و رزمندگان حزب‌الله لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/675539" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675538">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
جمهوری اسلامی دفاع از مجاهدان لبنان را به عنوان سیاست راهبردی خود تعیین کرده است
🔹
اکنون که حزب‌الله لبنان به‌عنوان پیش‌گام گروه‌های جهادی در برابر هجوم سَبُعانه‌ی رژیم صهیونیستی و حامیانش، چون صخره‌ای ستبر ایستاده است، این پایداری پیامی الهام‌بخش برای ملّت‌های آزاده‌ی جهان در جهت رهایی از ظلم و ستم استکبار جهانی و دست‌‌نشاندگانش شده است. بی‌تردید بخش قابل توجهی از این دستاورد بزرگ مرهون صبوری، نجابت، فداکاری و همراهی مردم لبنان خصوصاً منطقه‌ی جنوب بوده ‌است.
🔹
جمهوری اسلامی ایران نیز در راستای خطّ‌مشی رهبر معظّم و شهید انقلاب امام سیّدعلی خامنه‌ای رضوان‌الله‌تعالی‌‌علیه دفاع از این مجاهدان مظلوم و مقتدر را سیاست راهبردی خود تعیین کرده، و حفظ تمامیّت ارضی لبنان و رفع کامل و بدون قید و شرط تجاوز رژیم صهیونیستی را به‌عنوان شرط اوّل تفاهم‌نامه‌ی پایان جنگ تحمیلی با امریکای متجاوز قرار داده است.
🔹
بخشی از پاسخ رهبر انقلاب اسلامی به نامه بیعت دبیرکل و رزمندگان حزب‌الله لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/675538" target="_blank">📅 20:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675536">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
پاسخ رهبر معظم انقلاب به نامه دبیرکل و رزمندگان حزب‌الله: پایداری در راه مقاومت، نصرت الهی را در پی دارد
🔹
نامه‌ی شما برادران و فرزندانم، رزمندگان مؤمن و شجاع حزب‌الله سرافراز که حامل پیام پایداری و استقامت برای اعتلای کلمة‌‌الله و باورمندی به وعده‌های قرآن عظیم و آرمان‌های عزّت‌آفرین امام خمینی و قائد شهید آیت‌الله‌العظمی خامنه‌ای رضوان‌الله‌تعالی‌علیهما بود، موجب تقدیر و تکریم است.
🔹
امروز که ملّت‌های جهان از ظلم و بیداد دولت امریکا و صهیونیست‌های جنایتکار و نابودکننده‌ی حرث و نسل به ستوه آمده‌اند، راهی جز جهاد و مقاومت، پیشِ ‌رو نمانده است و پایداری در این راه، نصرت موعود الهی را نصیب مجاهدانِ راه حق خواهد کرد «...وَكَانَ حَقًّا عَلَيْنَا نَصْرُ الْمُؤْمِنِينَ»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/675536" target="_blank">📅 20:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675534">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
سعید آجورلو عضو تیم رسانه ای مذاکره کننده ایران: انتقام فقط یک تصمیم سیاسی نیست؛ برآمده از خواست مردم و روح جمعی یک ملت است/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/675534" target="_blank">📅 20:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675533">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
محمد حسین پویانفر: ما مداحان نباید در مصادیق ورود کنیم. چون به هرحال همه ما سلیقه‌ خودمان را داریم و اگر بخواهیم از تریبون مداحی سلایق خودمان را بگوییم اتفاقات خوبی نمی‌افتد. ما باید از نظام و انقلاب اسلامی دفاع کنیم و جانمان را هم در این راه بدهیم
/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/675533" target="_blank">📅 20:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675532">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b424b8bc.mp4?token=BDwvEiHScWHtf_DAISaah7zhGPShiCNsWvnAF4ni-Egyva8vkIRWNzlPtfHLW0NLVLEqBRB2q9vQLgyYdyeI4ynbs57yKryddOPespd4hoIMAN5nOBScSymW-r5IMsLfTrJRh6HsEyFV0FAf8vNPP6lXglPdGzhP-RpLra47ApOn4bQ4q6y6IeFaKhk2nPo6uvJOfUZ9JCbzTDEp4IPCWvFcjAptzEvfHGQG6sQuXODvytbjo64dFCjo6DIhK-uN3wSFCGKhJw5TOrCiFu-8REm6xcxdTJah8DqqRgBLcn2NZHAqAi89sLD-UVAIV1Gn1JI5pPoSbPqc4R6pBHCniaj1lcrG_g_HS7JXXVeqD2V4slJo0gLuHEslf1jdRmlIwVwL2v1Dl7E5Bm2LED18XsDMlCDnVAMg-b2EKSLJkPaXZvZ9m5TIwYrhBDffpzqwhFlCH84_irtOMQMC5W74-hcAH25iO7gVMI2PIWM_rLl2j2Dlaa5McVTMIS640m8DpOH7_p_vl2z1JFV2HFZGyEkMSgXkSDkAa_4rSNst9a2F2YX_9HG0UiKdJUon2O-g-3bc2vD_SiH4_6GWTWwywNMoJmvHt8nLz2eN3A0CcYuXxS0ASsZe8McAADwAfDs9eKRq_39d9bP-D-GlywNDZH2GXjpja1DLcPmWiLl2fUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b424b8bc.mp4?token=BDwvEiHScWHtf_DAISaah7zhGPShiCNsWvnAF4ni-Egyva8vkIRWNzlPtfHLW0NLVLEqBRB2q9vQLgyYdyeI4ynbs57yKryddOPespd4hoIMAN5nOBScSymW-r5IMsLfTrJRh6HsEyFV0FAf8vNPP6lXglPdGzhP-RpLra47ApOn4bQ4q6y6IeFaKhk2nPo6uvJOfUZ9JCbzTDEp4IPCWvFcjAptzEvfHGQG6sQuXODvytbjo64dFCjo6DIhK-uN3wSFCGKhJw5TOrCiFu-8REm6xcxdTJah8DqqRgBLcn2NZHAqAi89sLD-UVAIV1Gn1JI5pPoSbPqc4R6pBHCniaj1lcrG_g_HS7JXXVeqD2V4slJo0gLuHEslf1jdRmlIwVwL2v1Dl7E5Bm2LED18XsDMlCDnVAMg-b2EKSLJkPaXZvZ9m5TIwYrhBDffpzqwhFlCH84_irtOMQMC5W74-hcAH25iO7gVMI2PIWM_rLl2j2Dlaa5McVTMIS640m8DpOH7_p_vl2z1JFV2HFZGyEkMSgXkSDkAa_4rSNst9a2F2YX_9HG0UiKdJUon2O-g-3bc2vD_SiH4_6GWTWwywNMoJmvHt8nLz2eN3A0CcYuXxS0ASsZe8McAADwAfDs9eKRq_39d9bP-D-GlywNDZH2GXjpja1DLcPmWiLl2fUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیت الله جوادی آملی: هیچ فکر می‌کردیم روزی برسد که دو ابر قدرت دنیا رو مچاله کنیم آیا این معجزه نیست اگر معجزه نیست پس چیست؟
🔹
یک روز آیت الله بروجردی حتی نمی‌توانست یک مجلس دعا علیه اسرائیل و به نفع مردم مصر برگزار کند؛
🔹
از کجا به کجا رسیدیم!
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/675532" target="_blank">📅 20:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675530">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
اشتباه را پذیرفتیم؛ مسئولیت را هم
🔹
در روزهای گذشته، خبر محدود شدن فعالیت «خبرفوری» در برخی پلتفرم‌های داخلی، بازتاب گسترده‌ای در فضای رسانه‌ای کشور داشت.
🔹
فارغ از هر قضاوتی، یک واقعیت را نمی‌توان نادیده گرفت؛ امروز، میدان رسانه، خط مقدم نبرد روایت‌هاست. میدانی که هر لحظه میلیون‌ها خبر، تحلیل و روایت در آن منتشر می‌شود و تصمیم‌گیری در آن، گاه در کسری از ثانیه رقم می‌خورد.
🔹
در چنین عرصه‌ای، همانند هر میدان نبرد دیگری، احتمال بروز خطای انسانی هرگز صفر نیست.
🔹
همان‌گونه که هیچ فرمانده‌ای در سخت‌ترین میدان‌های نبرد از احتمال خطا مصون نیست، در میدان پرتلاطم رسانه نیز وقوع خطای انسانی، هرچند تلخ و ناخواسته، امری اجتناب‌ناپذیر است.
🔹
چندی پیش نیز به دلیل یک اشتباه انسانی، مطلبی کذب برخلاف سیاست‌های رسانه‌ای و مصالح کشور به اشتباه در کانال‌های «خبرفوری» منتشر شد؛ موضوعی که نه با رویکرد همیشگی این رسانه همخوانی داشت و نه با سابقه آن در حمایت از خطوط قرمز امنیت ملی کشور.
🔹
خبرفوری ضمن تاکید بر استقلال دستگاه قضا و ضرورت اجتناب از هرگونه حاشیه‌سازی، اعلام می‌کند که خوشبختانه نهادهای نظارتی با اشراف کامل نسبت به فضای رسانه و بدون هرگونه تاثیرپذیری از انواع واکنش‌های بیرونی، همراهی ستودنی با مجموعه خبرفوری نشان دادند که خود الگویی برای مواجهه با اشتباهات ناخواسته رسانه‌ای است.
🔹
خبرفوری طی سال‌های گذشته، با میلیون‌ها مخاطب، یکی از مؤثرترین رسانه‌های فارسی‌زبان در مقابله با جنگ روایت‌ها و جریان‌های ضدایرانی بوده است. رسانه‌ای که همواره تلاش کرده در کنار منافع ملی بایستد و سهم خود را در دفاع از امنیت روانی جامعه ایفا کند.
🔹
این مجموعه رسانه‌ای، ضمن پذیرش مسئولیت این خطای انسانی، خود را متعهد می‌داند با همراهی با نهادهای دلسوز کشور، همچنان در قامت یک رسانه مسئول و سربازی وفادار برای ایران، به مسیر خدمت و اطلاع‌رسانی صادقانه ادامه دهد و خطای رخ داده را در همین مسیر جبران کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/675530" target="_blank">📅 20:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675528">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLkymNliNn1nGh89fG8lT1aneEMJFE2CHemX9ZRuUsGfdT9fJHPMMZbvVQGsvgOZnyW80tmpELMYyCNiol38xJDoQ2tTZbL_CDi1XF-qOyPgNkpNZtJ1bEmftk5CRfXu4Kmf_BOLH2VYAxIY8Ga8Q-zdzVSNmY2zLAY34RakjTghPeyTV_rI7I1I-M0XbOHl457pVpXPA3DVzYRfbA13zZTjb2SR9HR2kRrVLcWrnMGvuuzFvAJ53ibb3bN1d_Ca08C4MKpyL2N5IsAuj8Ng5RpNjcdi7T-6LQHIQa3auPQ1ExafP08yc9ciyJrGnQWMZ9ZlDvXyE6E1iKqSb-JJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان بلاتکلیفی صرافی‌های رمزارزی؛ نسخه جدید برای رگولاتوری رمزارزها در راه است
🔹
عباس آشتیانی، رئیس کمیسیون بلاک‌چین و رمزارز نصر کشور، از تدوین متنی در کارگروه ویژه اقتصاد دیجیتال خبر داده که با هدف تنظیم‌گری میان‌بخشی و تقسیم وظایف میان دستگاه‌ها بر اساس ماهیت انواع دارایی‌های دیجیتال تهیه شده است.
🔹
رضا باقری‌اصل، رئیس کارگروه ویژه اقتصاد دیجیتال نیز می‌گوید: قانون، دارایی‌های دیجیتال را به رسمیت شناخته و کاربردهایی مانند توثیق، ضمانت و پذیره‌نویسی را برای آنها پیش‌بینی کرده است. به گفته او آیین‌نامه در حال تدوین، با استناد به همین حکم قانونی و سایر قوانین موجود، مسئولیت هر دستگاه را در حوزه‌های مختلف مشخص می‌کند.
🔹
با این مصوبه می‌توان انتظار داشت اختلاف‌های میان بانک مرکزی، وزارت اقتصاد و سایر دستگاه‌ها بر سر تنظیم‌گری دارایی‌های دیجیتال برطرف شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/675528" target="_blank">📅 20:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675525">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg1GiILbp8MXoRJPkAi_hKm8j8qCqkhfu5sXhctPiuSGqc2K40kDV-JdPbehWCmOfV0cQO5YkplvNj-4tf8TBtuB68N9_MG5dU-Wm18BJ91U9jEcJ5CgKxlEgLarAxObsKmb-i41iB-_DL8ygqYt2KcboD_TbcDJ1-CrUMpXbCs1_dcdm8IBGzHoUGwuXW7IfcdtLUH2Z1tsnTv-Ea4x8Z-WFFgfbII1hnpeXSs4eaVhf--j8xVlWY7biT2Xv_dzsPUV-fAFm2aYmdKWkjKtOcT8P6kotrF4aNK6KOOdDqEC-pmqDQ037gUVXIrgIiyWs3hVDtE4lWAJCcOV9BGrng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/675525" target="_blank">📅 20:08 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
