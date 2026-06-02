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
<img src="https://cdn4.telesco.pe/file/CYmjr-x9uLu12tVcN89f4EPKRSCW-iJ0vcLSZoz6WpS4YEE4r-P40kipEEVDx5Zjel7R83iyHKQ6g_zhbpQPN9SdHGSYhxAiS-N45iCfY3bK_6AdPYRGVodCQPJmtx04sUTGNTyYfRxx6IlIz7UHd-VHiyULVgbQjApRS5zHM4PgTUg4HQBTlV41MOqWAU5vrOBGL9dh43s6aGTAGDgmXyevds8eEjcDi0GcIFKmLS5zWCETgwvOpNIXMEp_LBNdOl8xs0Xgz39GOYm2d-FG0YyB7wH4Ys1CcM-UJJ67rHjxyJL6rkO1ET5DMr2Wk1-qT3SNXua3lj-IP1cSU5m9iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.01M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 21:30:46</div>
<hr>

<div class="tg-post" id="msg-655545">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار کودک</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIc6Cl1nMRtwALaHEZJxhjOT8DXRnbZdvRzMevjVP2saoqxD8j-ny6Jq4up4ZgTT3AhyMDwfArjuSkyMrtDUMnivpRejHEQLCDZ0qEdka4qQi6sJ1O5t7L73_p5xLLSUSiAp_5JpzmhQpIHShOOldXxOY-HBbmGzH1owmSj0HuyTUHvJfeg0ffronfXdMZflRLsbpl9d95tHzB4GsjyCDctCzicaTkwlh8mW-R9YJwY_R1IKMEpJnSxbgaCB72QT0IeIkiss546q_9ANOM6z3C7ldfmpn4a_h6SJ1Sv9O8ww61zZCE_sw2h3euqwMUXK1Fiy2mvuhQll4-z4aW8alA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
✨
پویش قرا‌رِ غدیری
✨
🌼
بچه‌های عزیزمون قراره با دل‌های قشنگشون، خونه‌ها رو برای عید بزرگ غدیر حسابی رنگی کنن
💚
با نقاشی
🎨
، پرچم، ریسه و کلی خلاقیت خونه
🏡
یا اتاق‌تون رو غدیری کنین از تزیینات قشنگتون عکس بگیرین
و برای ما بفرستین تا همه با هم شادی‌هامون رو شریک بشیم
✨
📸
منتظر دیدن هنرهای قشنگتون هستیم
👇🏻
👇🏻
:
@ertebat_gharar
🌟
بیاین با هم یه دنیا شادی غدیری بسازیم
🌟</div>
<div class="tg-footer">👁️ 9 · <a href="https://t.me/akhbarefori/655545" target="_blank">📅 21:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655544">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
اقتصاددان مشهور: ترامپ یک هفته فرصت دارد تا با ایران توافق کند، در غیر این صورت آمریکا با «مشکل واقعی» مواجه می‌شود
مارک زندی، اقتصاددان ارشد مودیز:
🔹
مذاکرات صلح متوقف‌ شده بین آمریکا و ایران باید هرچه سریعتر به نتیجه برسد تا آمریکا از درد عمیق‌تر اقتصادی جلوگیری کند.
🔹
دونالد ترامپ حدود یک هفته فرصت دارد تا توافق صلح را نهایی کند؛ پیش از آنکه اثرات جنگ، احتمال سقوط اقتصاد به رکود را افزایش دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/akhbarefori/655544" target="_blank">📅 21:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655543">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZXDIgzLvIAJogxwtc7jReW_lFEpwNQVMBNZP0PFccnBEm3IkTANxp8XrLeop5UaixvnhpZqa2VLt_tyB0cBnYU_tZ3PtOQJg2S80yPkCHt1_UKmJCBF0cfoNPqco6MmGgI9TDJ1JaYDjy9k13BUKCMZRm-xLYJQ7MgTObD7Nsj5BUrq-WF_xQy-3ILmH-rE-zOokJDgMdzrNjqcED-e2U370-I5zBzWOyA_s_-OKZTkEs57nUk93S0hFt_4WHuSiiz0n9n3TK93P-B_s649RhB2W5JL4GmilMIcsNHjJ_DOR3ACfjxbaSd2tn9hw29Uj3XKAqXSeWHqBFG2rKfAMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهمونی کیلومتری غدیر امسال به یاد رهبر شهید انقلاب در تهران
پنجشنبه ۱۴ خرداد همزمان با سالروز ارتحال امام راحل (ره) از ساعت ۱۵ تا ۲۰ (شروع تجمعات شبانه میادین)
از میدان امام حسین علیه السلام تا میدان آزادی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/akhbarefori/655543" target="_blank">📅 21:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655542">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/905db85c9e.mp4?token=eQ1amCW2HQeKh1f0qmPrFS3_3uptpRtQ3bAvZCiQN5-qtT_y2sx6NkzJhMI51QEnGuJTAy7LndPXspBFd_n4B5dmgPgv3MGS8LLdT-0_QzgQeelmf57Us4mknCjHEgbchsMVrnoawCoCTAwO0KFevsZemih2Ur9rPg-SbYAe9heXyhyjtA8xuyylM6kFetTe6Y_Tn3QrLoJ5_IXnVv4MrTNRqSs_YU8KLsZfvsWMrnh1iXwKcxMvhw6s-vTHILCzYj9_x5FlNCcgsUT4NRsCr4HxGtpmA7-d8aAZHqhwTcPLPRZjgAATRRqik9ieE3SVtCG4Pf0ohzPbZL4jW5I1mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/905db85c9e.mp4?token=eQ1amCW2HQeKh1f0qmPrFS3_3uptpRtQ3bAvZCiQN5-qtT_y2sx6NkzJhMI51QEnGuJTAy7LndPXspBFd_n4B5dmgPgv3MGS8LLdT-0_QzgQeelmf57Us4mknCjHEgbchsMVrnoawCoCTAwO0KFevsZemih2Ur9rPg-SbYAe9heXyhyjtA8xuyylM6kFetTe6Y_Tn3QrLoJ5_IXnVv4MrTNRqSs_YU8KLsZfvsWMrnh1iXwKcxMvhw6s-vTHILCzYj9_x5FlNCcgsUT4NRsCr4HxGtpmA7-d8aAZHqhwTcPLPRZjgAATRRqik9ieE3SVtCG4Pf0ohzPbZL4jW5I1mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قاتل بی‌رحمی که سالی ۶۰ هزار ایرانی را می‌کشد!
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/akhbarefori/655542" target="_blank">📅 21:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655541">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68585caf7.mp4?token=khNC3lqvinbBRAi5ILIe2XKNiCoojFHDkEpSQRHGBB-PIcRvU4t3jNmKUCQ3sYio5NeE741G_dh9t5GACXVopsQK4oBMAD5JTPuh6mQwtqftJibSPPmUEfVYw-N0gkQbIN8hxI11Gept0Ut7pvnfQKGuatEYrFHjalD9fbmRZ7RrlmovdirznPohvZxP4KMLGfbP8pRfDjsWM9WhySGqcIsJBjozYBVcmBM8Wp3ygOoK1Q7wvD3jtY4Z2P2zP1DcG98yhb_XbY78aClCXWvZL4zHq6GVT6XxJPcPyPrpk5ttCSHBXoMWY6n-cWUdvRagtWNtQqoj8TD0d9cBUqXzEQ7qpDHhs23nc-agx9Zq-aZjmW8Oy6xiuSQdQv67-Xo9AbZe9q4UwiAkwY4alOnPA_n1NS6VURQlxh7Nvrin5JOcixH1UT4Y2rmIvF6bN6kLEBnEcQArWhk5OOboWybzft4xx8ZD_G9S8FAQ1KY5sJeYBYKj9SeZRk07qU7rBwwkNTkKNIulv5JGPaOwnOVyLP358SoItYBou8qRj26y0JYReUgoNQQS635tC2BAvUkzBqIYCcKg1QJ_E3vvq1U-GmBoEw86s8IM1Qrb86e5gpkiFuwjbaJH7cLkcQ71l5DYxs-OmaHx3SDKPuPi-N4v8zxYmkvpEcx5gomEeqYhkGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68585caf7.mp4?token=khNC3lqvinbBRAi5ILIe2XKNiCoojFHDkEpSQRHGBB-PIcRvU4t3jNmKUCQ3sYio5NeE741G_dh9t5GACXVopsQK4oBMAD5JTPuh6mQwtqftJibSPPmUEfVYw-N0gkQbIN8hxI11Gept0Ut7pvnfQKGuatEYrFHjalD9fbmRZ7RrlmovdirznPohvZxP4KMLGfbP8pRfDjsWM9WhySGqcIsJBjozYBVcmBM8Wp3ygOoK1Q7wvD3jtY4Z2P2zP1DcG98yhb_XbY78aClCXWvZL4zHq6GVT6XxJPcPyPrpk5ttCSHBXoMWY6n-cWUdvRagtWNtQqoj8TD0d9cBUqXzEQ7qpDHhs23nc-agx9Zq-aZjmW8Oy6xiuSQdQv67-Xo9AbZe9q4UwiAkwY4alOnPA_n1NS6VURQlxh7Nvrin5JOcixH1UT4Y2rmIvF6bN6kLEBnEcQArWhk5OOboWybzft4xx8ZD_G9S8FAQ1KY5sJeYBYKj9SeZRk07qU7rBwwkNTkKNIulv5JGPaOwnOVyLP358SoItYBou8qRj26y0JYReUgoNQQS635tC2BAvUkzBqIYCcKg1QJ_E3vvq1U-GmBoEw86s8IM1Qrb86e5gpkiFuwjbaJH7cLkcQ71l5DYxs-OmaHx3SDKPuPi-N4v8zxYmkvpEcx5gomEeqYhkGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازسازی نبردهای جنگ داخلی در چین
🔹
چین بازسازی‌های واقعی از نبردهای دوران جنگ داخلی خود برگزار می‌کند. در یکی از این برنامه‌ها، یک بلاگر در شبیه‌ساز نبرد گذرگاه لوشان با حضور مردم محلی، یونیفرم‌ها، پرچم‌ها و آتش‌بازی شرکت کرد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/akhbarefori/655541" target="_blank">📅 21:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655540">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f37e27a0.mp4?token=PRaPY4DTmXR7FLXZCWfae-YDJZ8WLkG4EHPnNq1joWLmVd-WtH-dXY4VXGJDmyioB1F6zbYLsknd7MO-NlBlMeVlkGdh_IvJ4mv8lxIh4rXU84vJU6bEkCtDMu82YqnFldwdM5mp9HZ0xTlnbntpovNR0ytPKQftxsZ-P7JXx-22dqmVuS9KE1apjlkqF70tew0I9zobyi8_kVy2m8XC0f167EyFS7lKKZPEgYXr_9OZyCJgAFvokWK5xEu4072mewc0ocOASd-F-ag798AgQuWyYVtTP3WUFqMewUrNVYWkVWegJU_5rjJWODUY5b2_eX7dyCp6SJI29xNjUWAKWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f37e27a0.mp4?token=PRaPY4DTmXR7FLXZCWfae-YDJZ8WLkG4EHPnNq1joWLmVd-WtH-dXY4VXGJDmyioB1F6zbYLsknd7MO-NlBlMeVlkGdh_IvJ4mv8lxIh4rXU84vJU6bEkCtDMu82YqnFldwdM5mp9HZ0xTlnbntpovNR0ytPKQftxsZ-P7JXx-22dqmVuS9KE1apjlkqF70tew0I9zobyi8_kVy2m8XC0f167EyFS7lKKZPEgYXr_9OZyCJgAFvokWK5xEu4072mewc0ocOASd-F-ag798AgQuWyYVtTP3WUFqMewUrNVYWkVWegJU_5rjJWODUY5b2_eX7dyCp6SJI29xNjUWAKWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیبرمن: ترامپ ثابت کرد نتانیاهو اسرائیل را به جمهوری موز تبدیل کرده است
وزیر جنگ پیشین و رئیس حزب «اسرائیل خانه ما»:
🔹
ترامپ ثابت کرده که نتانیاهو، اسرائیل را به یک «جمهوری موز» تبدیل کرده است.
🔹
نتانیاهو «فردی کاملاً بی‌اراده» است که توانایی گرفتن هیچ تصمیمی را ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/akhbarefori/655540" target="_blank">📅 20:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655539">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoeGZXANnPYpZ1g9lSOYw13MZqFycVXNT5BSupxfY6fs125lrTi6sQGLMFHSSrpDJfI2BFMGdbZ1aWEEz-irOiNd1oyO-XL927P68nYoOfwszN7F8MP9NdLDOQAR_k-vTdAg5prmB7Dl6ahOL9Cw8_EDMDyESiAoMQppJ6lehHf43V2zC9pZPFM4Vcwb59TMjuJkab_AW-s2XBBiYoOkQjt5AYOVG5tYSL50ZwA9avPvO4_4QrxtnP4Je2DZRNlEUwGfJTFY_S8VnbmPQbU0hKeiMioCLJKDFU0i32tM5ZfiRs3K7DKUEOe0izi58qu4BgZlqcA7OHMCfAdrP2EvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان خبرفوری برای روز عید غدیر خم؛ «به عشق علی»
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی‌ست امسال در روز عید غدیر، به عشق حضرت علی(ع)، یک کار خوب انجام دهید؛ حتی اگر به اندازه یک هدیه کوچک، یک اطعام ساده یا یک مهربانی کوتاه باشد.
عکس، فیلم یا روایت کوتاهی از اقدام خود را برای خبرفوری ارسال کنید تا با انتشار آن، دیگران را نیز به انجام کارهای خیر و ترویج فرهنگ نیکی و بخشش دعوت کنیم.
مهربانی خود را برای ما بفرستید
👇
#به_عشق_علی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/akhbarefori/655539" target="_blank">📅 20:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655538">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d20a2ef19.mp4?token=BQVL7kp8MAJ30kxHkpCky5ow9Guvwl2R1VcOJO0drTB0O8J9-ypbj8bPTIDepKSu-3BUzlZ4eT0ezrJ1Y3dUONOJdoTNnqNjDOaT5hNjGQAmemO17WfOlII5uz7XGpZYYFa0QZ5KWWiOGjAqB4uZOG6yMlFDPPGu05C1kky6nJ412jiac-tUtPhiq6H_V9s-Wt6d3qMP5HCkYul7fAz_ISSpl0b1zU3MtGXbHlPzO9qqjEoRV72i1HZ281I6i-rjq1zxjRQAmX-jTn3-m4rZsYlhhrxcZn7NkmZ0df2PWEwvB3dUi1hCvVrKwnArtdGg8z17AjWcyfUi8Alr14g9eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d20a2ef19.mp4?token=BQVL7kp8MAJ30kxHkpCky5ow9Guvwl2R1VcOJO0drTB0O8J9-ypbj8bPTIDepKSu-3BUzlZ4eT0ezrJ1Y3dUONOJdoTNnqNjDOaT5hNjGQAmemO17WfOlII5uz7XGpZYYFa0QZ5KWWiOGjAqB4uZOG6yMlFDPPGu05C1kky6nJ412jiac-tUtPhiq6H_V9s-Wt6d3qMP5HCkYul7fAz_ISSpl0b1zU3MtGXbHlPzO9qqjEoRV72i1HZ281I6i-rjq1zxjRQAmX-jTn3-m4rZsYlhhrxcZn7NkmZ0df2PWEwvB3dUi1hCvVrKwnArtdGg8z17AjWcyfUi8Alr14g9eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل‌آرایی حرم امیرالمؤمنین(ع) در آستانهٔ عید غدیر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/akhbarefori/655538" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655537">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_6Vr03syTwKNgiTZSjDfJJrvC5BAf5I2KhicsoZmlA1y-MiBYu4mD_A15rGXFMuM7OKB3r2rIODm4GmoWZGxbGAhY-g5BlbtVMsbxvFM3abDD-e6-sFH8Yw9-mH10oZzigt7teAnVZ4BmTKX3WQLHHm04clNXfgjFXZKlKAJzW-j3E1lVHt9WRBmTFWCNzZ3713qDJ6dJNB9VbHpycCknnTqnXJ5aCiF_or1_RplQMUELSu87jsiwxjXr0K3pvgC2KjPJvi5gs_Gqp0ScRUvl0dKx0KB_xv-fdeCWRTddMwxnMoNf8mPFEkpoTnGtuNgiO3EQYWudbMuRGe0AQbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌱
مهمونی بزرگ در پناه ِ غدیر،
🔹
با حضور ۱۱۰ موکب پذیرایی، بازی کودکان، غرفه‌های فرهنگی و هنری و ...
🔸
با اجرای: مژده لواسانی و امیر مهدی باقری
🔸
با کلام: حجت الاسلام برمایی
🔸
با حضور: حسین حقیقی
🔸
با نوای: کربلایی علی اکبر حائری
✨
وعده ما: پنجشنبه ۱۴ خردادماه از ساعت ۱۹  الی ۲۳
✨
مکان: مشهد، حدفاصل چهارراه نخریسی تا چهارراه چمن
@Heyate_gharar</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/akhbarefori/655537" target="_blank">📅 20:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655536">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ca748c1a8.mp4?token=omjsPBzHUOQZ7KG3RL3jhdPyl-AwMZPOM30ap-0Y4DmO1oNOIdz0jH7XZyM6uVUn6nnfFKXOn0uw40KyLkNkxkRYHNgcDh70O9hJ4gKyBV8OusUEWAXcyG1oZXOhyiJ53ctW1efzuCXt6s7gyZLxMgFjLyQ94J_c41727rEA63tO6rH0iic7CMXvXpxgts_ISdNYn7qPJwVwpYPMaqmvMk-3P8wFJ1sFQumCp_V_x1ysjiyUT0OmeRDPAlSiEB_ouowsdp4XtMeZFtnvWoHyoK3Cgn935ebW97OKg8nTEP_KJe86dDcFoRUcfgE77bh07VNW95vPKqo7g6ecHlEXuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ca748c1a8.mp4?token=omjsPBzHUOQZ7KG3RL3jhdPyl-AwMZPOM30ap-0Y4DmO1oNOIdz0jH7XZyM6uVUn6nnfFKXOn0uw40KyLkNkxkRYHNgcDh70O9hJ4gKyBV8OusUEWAXcyG1oZXOhyiJ53ctW1efzuCXt6s7gyZLxMgFjLyQ94J_c41727rEA63tO6rH0iic7CMXvXpxgts_ISdNYn7qPJwVwpYPMaqmvMk-3P8wFJ1sFQumCp_V_x1ysjiyUT0OmeRDPAlSiEB_ouowsdp4XtMeZFtnvWoHyoK3Cgn935ebW97OKg8nTEP_KJe86dDcFoRUcfgE77bh07VNW95vPKqo7g6ecHlEXuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی جالب از رها کردن جوجه اردک‌ها در رودخانه ایبر اسپانیا
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/655536" target="_blank">📅 20:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655535">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
مردم، آمبولانس آسیب دیده در حملات آمریکا و اسرائیل را گلباران کردند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/akhbarefori/655535" target="_blank">📅 20:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655534">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
رفتن به کما؛ پنجره‌ای میان مرگ و زندگی و مواجهه با خطاهای گذشته
🔹
00:07:00 دید وسیع در تاریکی مطلق
🔹
00:10:05 دو نوری که همیشه همراه من بودند
🔹
00:17:00 باز شدن پنجره‌ای رو به زیبایی
🔹
00:27:00 ماجرای نذری دادن خانواده و رخ دادن اتفاقاتی برای من در کما
🔹
00:37:10 درخواست خداوند برای بخشش دوستی که به من تهمت سنگینی زده بود
🔹
00:46:40  مشاهده عمل دزدی که در نوجوانی انجام داده بودم
🔹
قسمت پنجم، (نمی‌بخشم)، فصل چهارم
🔹
#تجربه‌گر
: محمدحسن تاج‌میری
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/655534" target="_blank">📅 20:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655533">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۵ هشدار بزرگ جهان درباره جنگ ایران
🔹
محافل نخبگانی و اتاق‌های فکر غربی، حالا با داده‌های رسمی هشدارهای بزرگی درباره ادامه درگیری با ایران می‌دهند.
🔹
در این ویدئو ناگفته‌هایی را خواهید شنید که رسانه‌ها کمتر به آن می‌پردازند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/655533" target="_blank">📅 20:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655532">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpRSLiKZZ4NL2SeQApSDPU4zF4xGsi4AFZ8jxEH2ZWvHbAGsZUa3XZaaFxzIA7wkGeydebBKZ4cJ1j4RR3324a_Oy2nWGDHsiWAl7ihoEyoTESxB8u6qWxzU6NVrVYWLsn2KNfRyXC7UUmF2BbvfTsfYiM4PYK29ZJOd7UNiQqwIaGTyDX6R9Apc0Ztn2xGercso3guDI7JhwHfd0HhQPuUnzuaR1ZIbJtgv1W_-Grp3oOTMdLktm8G31-O6UvQNjkBVmhh3ZIB8XilfB9agxhs9Z33FKYZ76rXVeYRsRYGN0zdODyOOx5h-G2E0qa78ZyEb4t6LI3IPHv4xWgHgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تغییر چهره حسین فریدون؛ پس از ۹ سال
🔹
از سال ۱۳۹۶ در هیئت دولت تا ۱۱ خرداد ۱۴۰۵ در مراسم یادبود خواهر سیدمحمد خاتمی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/655532" target="_blank">📅 20:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655531">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce27379fc.mp4?token=q7arPlWHEuwZKxIB9B4dsngZ8tyrwWm2bERQmGR0hPXDB407oUXMJvBCDovNiO5TiBXJA-b8qjKdoGu2yZQ27FQKUin3JfKDQkCKuVLIUdFJsR-xC5K9oy2eeLB4WL9Lnxtx25p54Sh0Y_rAXQSZoaj1RREU6HjJx_NZWvdZYzXe5DgOFP5yORc0fLWp9TKBBkZuPU8eZwb-4Np-AKvBfL5OzZTuT9QfzfhroW05dy-1ghIopq-Ecew2FSIdfHilJW7wdUpWgK9ngnyV7esqZEaINgypUBxVKkrLMJ3QMj4yF15KblWWftuAZtZ1n14CZxR_zcepiq_wElF4Piv9Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce27379fc.mp4?token=q7arPlWHEuwZKxIB9B4dsngZ8tyrwWm2bERQmGR0hPXDB407oUXMJvBCDovNiO5TiBXJA-b8qjKdoGu2yZQ27FQKUin3JfKDQkCKuVLIUdFJsR-xC5K9oy2eeLB4WL9Lnxtx25p54Sh0Y_rAXQSZoaj1RREU6HjJx_NZWvdZYzXe5DgOFP5yORc0fLWp9TKBBkZuPU8eZwb-4Np-AKvBfL5OzZTuT9QfzfhroW05dy-1ghIopq-Ecew2FSIdfHilJW7wdUpWgK9ngnyV7esqZEaINgypUBxVKkrLMJ3QMj4yF15KblWWftuAZtZ1n14CZxR_zcepiq_wElF4Piv9Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور دموکرات در جلسه استیضاح روبیو: تنگهٔ هرمز به‌دلیل حملهٔ ما به ایران بسته شده و این پیامد اقدام نظامی ماست  کریس مورفی خطاب به وزیر خارجۀ ترامپ:
🔹
در حال حاضر تنها سوالی است که برای مردم آمریکا اهمیت دارد این است که آیا تنگه قرار است بازگشایی شود یا…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/655531" target="_blank">📅 20:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655530">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/655530" target="_blank">📅 20:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655529">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KexmPPgxqS71aJdmvN6X6gDvOsZE7qsscP4fSMEQ3rNBG7bu_mLWe5l7nchA4_AtsOfbOriuZt_wvWVPIoJ90jhYGcLW3uw7A1czfnSHw5uRnhEr8mYMA97BxxDFMtEKX9w5PNFJ6OzZ7ANieyF_MkNMg6dgW1E-vpgEPPZ4ptDIYLeGKlq0wLJxeYdY8nv4o1WE0P6vLtaYzhbiv57liwREO51kpkziFjmGEQet6Wj6hUdBLJO6AVi5vklADJamvmg151ZPRdYMJ9-dY_3UsMj5tnpfBBgYF4opex_fz-uMGgNDx_CshFlq4SkOTsSzIJ_-smQk7-gukwS3QUHGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
چرا رقبایتان همیشه جلوترند؟
چون از قدرت خبرفوری استفاده می‌کنند.
✅
تبلیغات در پربازدیدترین کانال‌های خبری
✅
پوشش همزمان سراسر کشور و استان‌ها
جای شما خالی نباشد.
همین حالا پیام دهید
👇
👇
👇
@newsadmin</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/655529" target="_blank">📅 20:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655528">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/547b26b4ef.mp4?token=a5SiBkISXLsUnolxhnmaqiFkE6U1WOcNWC2FD4MPveJ6DYCRCv9KNhX6IMGm6jNoe-sXJYIEgFvEK-XBri1jIdICQn0hJKU1LneSCIXh2tbl0fqaR-LyOBKtjErlXODSqIZf411ToT8Umu6bMEljRcMsGVdo8cA64BqXbT1QzgvcQbfRvlKqbFwFegpbbZ5mhzHOS-31R9pY5tJGGy2rfRvOzBRndhNp-FGYN-dnU6bEOYHfbZIqoOcHIv-Ptzf8-g-nr0uiHtASe0k5uuGcIqs-cjz9y_SOj5uzireGyJu8QdeFJGDnwp3nXoRGHNR4cdvjJiO7c-ciaF1hszd0ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/547b26b4ef.mp4?token=a5SiBkISXLsUnolxhnmaqiFkE6U1WOcNWC2FD4MPveJ6DYCRCv9KNhX6IMGm6jNoe-sXJYIEgFvEK-XBri1jIdICQn0hJKU1LneSCIXh2tbl0fqaR-LyOBKtjErlXODSqIZf411ToT8Umu6bMEljRcMsGVdo8cA64BqXbT1QzgvcQbfRvlKqbFwFegpbbZ5mhzHOS-31R9pY5tJGGy2rfRvOzBRndhNp-FGYN-dnU6bEOYHfbZIqoOcHIv-Ptzf8-g-nr0uiHtASe0k5uuGcIqs-cjz9y_SOj5uzireGyJu8QdeFJGDnwp3nXoRGHNR4cdvjJiO7c-ciaF1hszd0ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: داریم به ایران برای بازگشت به توافق التماس می‌کنیم
🔹
یک سناتور آمریکایی در جلسه کنگره خطاب به مارکو روبیو گفت که ایالات متحده هم‌اکنون در حال التماس کردن به ایران برای بازگشت به توافقی است که دولت دونالد ترامپ آن را به هم زد.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/655528" target="_blank">📅 19:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655527">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf407a52ce.mp4?token=ErCSWHd6f2rrkEmKNppDjcHeSYk5od0Ba4F0aGnQIupT2CR_6MTVB39_d5N-shDjFjXBSzemnSY5-DZvoK3fEZyR6oyv4KVi-7qxpiAKCgXBsKTL6m5bUu0o0kvOqmD54HEiTfjGDiKDk1hleUwIBnAwqlQaODs9ZbVFzHZIPpq-3GlkU1HmZ8unz8JPuUqyCOGb7U5qn-mZoTbY1gkpWuRNgwldA4J98s_D2tPCbc9M4qx8cZT8ai-uLAw-2VtnlAYPCURaXjhNbj4FmyDr5WN7MnV9rIezJPfykX056P-1OstDvJsz326v2rl3tWCDeLsLZziCJXikytDdeks5Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf407a52ce.mp4?token=ErCSWHd6f2rrkEmKNppDjcHeSYk5od0Ba4F0aGnQIupT2CR_6MTVB39_d5N-shDjFjXBSzemnSY5-DZvoK3fEZyR6oyv4KVi-7qxpiAKCgXBsKTL6m5bUu0o0kvOqmD54HEiTfjGDiKDk1hleUwIBnAwqlQaODs9ZbVFzHZIPpq-3GlkU1HmZ8unz8JPuUqyCOGb7U5qn-mZoTbY1gkpWuRNgwldA4J98s_D2tPCbc9M4qx8cZT8ai-uLAw-2VtnlAYPCURaXjhNbj4FmyDr5WN7MnV9rIezJPfykX056P-1OstDvJsz326v2rl3tWCDeLsLZziCJXikytDdeks5Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خارجهٔ آمریکا: ایرانی‌ها می‌خواستند یک سپر متعارف دفاعی برای خودشان بسازد و ما به‌ همین دلیل به آن‌ها حمله کردیم
🔹
آن‌ها قصد داشتند آن‌قدر موشک، پهپاد و تسلیحات متعارف، از جمله یک نیروی دریایی، برای خود بسازند که دیگر نتوان کاری در برابرشان انجام داد.…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/655527" target="_blank">📅 19:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655526">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5998cf8f9c.mp4?token=f7w5voWYfYf_VvLYDbVXD1qLPyOLGzJiNj_B5y-7z9qqfUjIFdMQCf2TCzO056EOr1HB6F1wI-rmfUr12hH0-SoiqL3nrj8UZO82fVWPWgNv4xSQTaPYfGA2HsY9zrSyk_4R5b4BpMqktESVlKEFBEjY4gBBGmXflX7TNfmEmc3Iy82wT2DeYvYZ7EIgy5Tj7K0-YZ-rhpDjTEqcx11S0B4Lm6yj41Nc3OPruS3AHWvciQOS4cXZ9dO-a6Pn9r1MY1mD8MxTPTu78hQCJNXh4GcCzlLxw3fPKGTIFy10kAlBluD6BFjcbJllqd5qzy31SQb4Wa6VBMS4W-OxP2RR2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5998cf8f9c.mp4?token=f7w5voWYfYf_VvLYDbVXD1qLPyOLGzJiNj_B5y-7z9qqfUjIFdMQCf2TCzO056EOr1HB6F1wI-rmfUr12hH0-SoiqL3nrj8UZO82fVWPWgNv4xSQTaPYfGA2HsY9zrSyk_4R5b4BpMqktESVlKEFBEjY4gBBGmXflX7TNfmEmc3Iy82wT2DeYvYZ7EIgy5Tj7K0-YZ-rhpDjTEqcx11S0B4Lm6yj41Nc3OPruS3AHWvciQOS4cXZ9dO-a6Pn9r1MY1mD8MxTPTu78hQCJNXh4GcCzlLxw3fPKGTIFy10kAlBluD6BFjcbJllqd5qzy31SQb4Wa6VBMS4W-OxP2RR2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای روبیو: ممکن است تا ۶ روز طول بکشد تا از ایران پاسخ دریافت کنیم
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/655526" target="_blank">📅 19:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655525">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouFsXD2fSZwUAak9xKSQ5W-omZu6gW3L8bY8-mxCBKRmOh9u7r27QgHmPNfIifz0z1g1uecU1lqGugE64oDs9kUV687UsJcn8OvT5tVDk79fu5Ifpg5iLGUx2WO4MMFuNqjTA5dxeLWfRmG5Vu0jWOE7Q6IZqSZe2eDB9RHNNBMn-S9BORnum62qjkSHI3dmw97g8UZhyaSsfIi8zDkSu5cAt5eA9a5_UBVzi1mSPHUfdHQ03CCrHNvbnqiAqfm3dCVaaRUDrtB6I6Q3E4j2_i2raAqKznYdoXEOBc9wnHoYQ_aOB-MDGO0giYamhZcDxBafAXfXbi25g3_IF_3zRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناو «یو‌اس‌اس باکسر» (USS Boxer) که مدتها قبل به منظور عملیات آبی-خاکی در ایران اعزام شده بود، علی‌رغم انتظارات به دریای جنوبی چین رفت و از منطقه دورتر شد!
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/655525" target="_blank">📅 19:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655524">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f74207fb.mp4?token=d70rNzGfBD7qO_0-uCgl2U7ftVSy1eFC_sYb_FhQNQYmyuZI1ncVuXzLpKdd_0SzsNS3zNa08kGzDNDlU7b1HYQkHRChQC5TqPnpuZ6_LXPFHqb6ede_OtiuH0pAVlDnSAx6F_XbhKHkqYNcTRBamwPqhQpLfwQkke8k2EwRoAspmaYNqQoZuEwm7PUrp0_SofbKOKDaUsSHjN-N_JmMBSeP5np-U8Myh9UbflbFrYuMbRjbMt5WyoN_85nmO8IV8uGXfwqmCh4ZQH27qmqvP1IhAADQdtmb_Nr7ehn9KUb3Tgve_ONSu_7k_zhHmk272NZHHqThVUhhiai_J_z19w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f74207fb.mp4?token=d70rNzGfBD7qO_0-uCgl2U7ftVSy1eFC_sYb_FhQNQYmyuZI1ncVuXzLpKdd_0SzsNS3zNa08kGzDNDlU7b1HYQkHRChQC5TqPnpuZ6_LXPFHqb6ede_OtiuH0pAVlDnSAx6F_XbhKHkqYNcTRBamwPqhQpLfwQkke8k2EwRoAspmaYNqQoZuEwm7PUrp0_SofbKOKDaUsSHjN-N_JmMBSeP5np-U8Myh9UbflbFrYuMbRjbMt5WyoN_85nmO8IV8uGXfwqmCh4ZQH27qmqvP1IhAADQdtmb_Nr7ehn9KUb3Tgve_ONSu_7k_zhHmk272NZHHqThVUhhiai_J_z19w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاردستی جالب دانش‌آموز سیستان و بلوچستانی؛ پدافند!
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/655524" target="_blank">📅 19:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655523">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اظهار بی‌اطلاعی وزارت بهداشت از وضعیت محمود احمدی‌نژاد
حسین کرمانپور، مدیر مرکز روابط عمومی و اطلاع‌رسانی وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
از محمود احمدی‌نژاد خبر ندارم و از یک تا دو منبع دیگر پرسیدم، منابع من نیز خبری از اینکه چه اتفاقی برایشان افتاده است، ندارند. در واقع اینکه آیا آقای احمدی‌نژاد زخمی شده اند یا خیر، اطلاعی ندارم.
🔹
سایر مسئولان همان‌هایی بودند که تقریبا اسامی آنها منتشر شده است؛ چه کسانی که به درجه رفیع شهادت نایل شدند و چه کسانی که دچار حادثه شدند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/655523" target="_blank">📅 19:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655521">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYraxnepUj0YTq18UT_8kgf2w9E_J7d7V2Q_DXLc8OqggLhu-5OTc4LLkxpSrpY6_hqa6Lf620smfo0QkoRGaTYdD5NtW9lPeenMoVI0SWjN7RTKNocz3edRaOiUYaMYEVCYO5tEu82_frNfj3UTlWZGSt-54i53MPleiSOAypAKDu4CGiOZGXsOXc-sdCjtpkC46wL1bdatSO0j_tq3-agVBQgi5Et-mCgu3O76t4q3Cm1NgLgnFsCdTc3ZN3qhSsVZosf4tBBm5BRgvofRE2qVnO9bnV4q_dOqQLIXDh5MYDHsirpbHsndQdgegkFfCDqFxNKyxLMFRcnDds2pgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط بیت کوین به زیر ۶۷۰۰۰ دلار
🔹
۷۰۰ میلیون دلار از بازار ارزهای دیجیتال در ۲ ساعت گذشته نقد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/655521" target="_blank">📅 19:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655515">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgMZ9tvjff494-TfjrBrJ5-9m9y6Z9edj047_YQwFzobgWnncLvSLoCKGsgrheVCj2voWdFA4XhyB1cIJQwK5qzVIcchAQqZ-MAYpxlzY2qhZU1ePsjnbdfg8KIDFrxcc0WfZ_dM27pruJVZSztYsTjf2TGQfgOA_8XgJOMXHt6z2nSwCXokOvJX6PfBsjw5R4BjZNhwAvAjeyIOAnESxwSVHAqxJ9K1Tz2AlvfM7i0ofaOd0T5Ai4D02wLfhF8E1pGvM5V-6slZeupETtAE1xcoz00H1NxrFz7r-9CLulo6pcNhKyaNoMaCd6uvE78jUA9zWNjk8tg2RnNDXfH7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7efw9zGPMshYzqCN7l7y1uVrWVHowg-_XPJjwQA_sIeMnmLM4jmz5myeinSrtPS3p7HQ5ps1x7qsrk7RsXzmjy6jSmaeSrCoVUcUbERi6Pj4ZVw_Mx6AEHk6H2heSV0d9AhkbRGIStoBbqizWnYI6z7UpOhwZln_54aZsfhMZxv5xHqJazLMb-8cTKrhiH2FjqQqWyzmzkelLEMi22F7wmNKs1qBDdJPTEP2KFwQcxJE6JNHfvTTqUdIqzsKDC4R_d95N1L9RMfTEB2Hls4L0c--8CjmcP6wdRt5whKmKWNKLRZNw3r3gpPNRvKBvpjpBvhvd9KDO_WUxoI014p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmhY1xnCvDNcyySE9t94248AtT-1uxyc4kQTIW1NKiRRv5OPCI0wY9b5cj335h_V2yHeA11xTF8KzeqUUjQyS87nOtK7v1pQaFuMeveMB9iW--F9VzFdfxH_qzxU1YKKoqdFVzF2t2eryQFisyOTn6vMQkdm6iLnfeMbipoJ4o6ZuscTJvzuVhQYhVqvmFOCWXHHwWexYxgRA41JF57s78S4xs-Vo8WgVhVhfd4fx3fgy-PADvdcin2yf8TS6wzjPMVeSEC79wLoIKHmKr09qpp3xs5SmpIFpDcGzxfNfJUcealWpuMzylPrdCTT0jAzKeXsTt1mFNTpb912JidMsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdjFY796Nc9ZihWRfsTCOgPHTlBdMdspzMzerFYys71hlbD5TKtCMEkWrqhNZAqmJCTgawxrbLrnAXhkvuzngE6DeoP3pS0wvSMMUcazFQxrfSNpWhsghiTB6oO1X6wajteNZADyRf3N9W4oMiypKia2TOBeRBkkEcXkztth8j_dM0PNLP19T9w9gAu6Jd8F8mnBGtCptWyXO_wv4pbHw2Gdb51bukOX4b0OEXXWwiL7D6wZRaZyzPDusvltnP5puiVGsiv4CFOB0CakzYVtKWfZT8MeOwmJUPbefTthFZEqXQn6EhEkreRIeuNejyM3FNLtDBONxJEfO0EKNgluww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npfEtgzAF1fphWYEBFXinEexaJUsizYLFCZ5pZyKj5Z25UVF-WfNPiDsjZhOPZBEVE2on269w0iPp_0JyTIG90sNFGLV_QL5JHb6SC1T4dXzGNyOOlL8qGvPI7Toa-P0tMyVOhyHlpXWjrQe2lfVGBOzEeUp9X5WqiAlfTg4DGwZpkJgGk_t_ue6FgRSDOunZXGTj22snggvrE0NQk3imHqX9gDNQT7B38gNrxZ9qKkCXUtud0-odkXTXRq-IHm_NGWlpu3yGUVhQmKRrOLYX2Y4P7K9VgARnZV9b8gN5yEH_nnmc7xfAmPntpoXSIl0kwKjFztgs0FVLp_o6G0BHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vvEa-LtgB_9hQlw6ogF_TuIs77zlvtzb4v2qBQXFpWMrhdFtbkXvxGFfCyWdmKWdMGSuJVjv7B_Zq022DVt1IaprJ6TqRFjNAaGpvQLUENZhUyFUZMG9M8dKBsrpCdeoIoG5ywphoG4FcBhs_vHXqEUPrXGlS_-Qqqp5f22tWjEap9bU9O4p-WJfHa8hyJo1PXq0BDumzo_1JyQZfQ9T8vuIMTDdWDTW4wz2iW34b-6t24kRiHEXHxI4l1-nwPo-T2JGmU6n2OyqsCvOhmeGVtDGNDuruEaQZ1F67u3I_i2mrTscRtNb1kHeqrFJrjowxeKXG4RFZHu-hqIjEoXEKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آماده‌سازی حرم امیرالمومنین(ع) برای استقبال از عید ولایت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/655515" target="_blank">📅 19:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655514">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای روبیو: فرماندهان ایران با برنامه‌ریزی وارد میدان جنگ شدند   وزیر خارجه دولت تروریستی آمریکا:
🔹
کاملاً واضح است که در آغاز درگیری، آنها تصمیم‌گیری را به فرماندهان میدانی واگذار کرده بودند.
🔹
برخلاف سیستم آمریکا که رئیس‌جمهور، وزیر جنگ یا رئیس ستاد مشترک…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/655514" target="_blank">📅 19:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655513">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCTgSv_0_g02YgvP9IiqjwJhX9lWPlTfiB9R8J009OkaGkYmlnxL9_1ZrSoEEPBWCqVAfbRXK9yvPr-LtFZkr2-AetoxnJzE3G06AX8IHey_DsvGWws033ikKr4sqlkFCh2gwQgYO6LhwcP7rhxXZG9Khhx9Yg6fAaOQ5ugSu3fSbfml_MxZVgjKCvdgXhltdNal0iYaaCfYX30a1vL03L_LzYPGgyNoWtIoVuD1nzcCOq-_PKCrSj-Erd5UjiA4FkPTpislzZWH3Tp6SpfH10UzXG2zJaj5XYybxfKG1kp0hpm7aH4UFf6bFrBOsmUUzyz55NljV4NATBlu4BE52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/655513" target="_blank">📅 19:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655512">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQeroki6bPa5e5NTo-EsTXU-cevR-oS2U5rnyGkJ2iOa-CWWuhGPdf735Jv2EDGGwuu2lqocXfDVuoyGdgH9kGXt5hiWc6--zxVYDDqD8RqBU5pUnJoVtKpzWmYlWg6h1YiQBm9piChc7Tt60oSiTF6yDoO5qm7r2OaYhZtTx-TDEpEqN0eFVDBl8IGKQLC68Hbk0GMMF_1KOAkzSQhGiXoiGZsaphp1F_1wqknI4bXUwUh3NjtDyoN8eFRZseH2m46D4uYp0Vgwkbl3paX5PVUsfmNVOQiFgjkp5Jl7oXoOEV9rbKWSwzGkYu1FqUZ35ecceQbZt3TSGnZ01VRVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات جدید از خلبان اف-۱۵ سرنگون‌شده بر فراز ایران
🔹
خلبان جنگنده اف-۱۵ استرایک ایگل که در ۳ آوریل (۱۴ فروردین) بر فراز ایران سرنگون شد، همان خلبان یکی از سه فروند اف-۱۵ بود که کمتر از پنج هفته پیش در یک حادثه آتش خودی توسط یک اف/ای-۱۸ کویتی سرنگون شده بود.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/655512" target="_blank">📅 19:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655511">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
زیاده گویی وزیر خارجه آمریکا درباره تحویل اورانیوم غنی‌شده    روبیو:
🔹
اگر در مقابل چیزی به دست آوریم، می‌توانیم تحریم‌ها علیه ایران را کاهش دهیم.
🔹
ایران باید اعلام کند که با حذف اورانیوم با غنای بالا موافقت دارد.
🔹
اگر ایران می‌خواهد نفت خود را از طریق…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/655511" target="_blank">📅 18:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655510">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
شاهکار شهرسازی چین
🔹
پل معلق «هواجیانگ گرند کنیون» در استان کوهستانی گویژو چین واقع شده‌است.
🔹
طول کلی پل به ۲هزار و ۸۹۰ متر می‌رسد و بلندترین پل معلق جهان است و سالانه هزاران گردشگر بدلیل مناظر طبیعی زیبایش جذب می‌کند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/655510" target="_blank">📅 18:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655509">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خبر ناگوار؛ تابستان امسال یک تا دو درجه گرم‌تر از میانگین بلندمدت است
صادق ضیائیان، رئیس مرکز ملی پیش‌بینی و مدیریت بحران مخاطرات وضع هوا در‌
#گفتگو
با خبرفوری:
🔹
روند ملایم برای افزایش دما را طی روزهای آینده در اغلب نقاط کشور داریم. در مجموع انتظار داریم هفته آینده هفته گرمتری نسبت به این هفته باشد.
🔹
انتظار داریم در تابستان امسال بین یک تا دو درجه از میانگین بلندمدت افزایش دما را داشته باشیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/655509" target="_blank">📅 18:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655508">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادعای روبیو: شرط اول در مذاکرات با ایران، باز کردن تنگهٔ هرمز است
🔹
لازم است ایران به وضوح اعلام کند که تنگهٔ هرمز از این پس باز است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/655508" target="_blank">📅 18:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655507">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
روبیو: هیچ کشوری به جز ایران و شاید عمان، طرفدار اقدامات ایران در تنگه هرمز نیستند   ادعای وزیرخارجه آمریکا:
🔹
اگر ایران با توقف هدف قرار دادن کشتی‌ها موافقت کند، به محاصره پایان خواهیم داد
🔹
هیچ کشوری از ادامهٔ بسته بودن تنگهٔ هرمز حمایت نمی‌کند، از جمله…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/655507" target="_blank">📅 18:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655506">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbde4ebdb7.mp4?token=S2E9Qb4HQDjakJWcek1JB4wXHFhNNo3q-V_asZ1dKWP1e7HrlSxhYyasYy1sF0aatJITXchLdgOtK5TOf_sSQrIBLjCts05tv-VT-8KMvcpTQ9HR_hSef6m6U7fDTtZkF0zOo9wCUQAzar85gOWHec-kBZrLgJBISBXnSfSdO4QwGYRyCfPQBhThwlg-55qXzO1s4qRpSrfc4wORJ9s-SDI3S0z-KRO-bgHIYWMgUFKF11neqrK6If58EJUz7F7Bk5JupoNSNbMHGsmQurZWqRPMFX-cMMpoH0o2LtcFnqcpDEDxBPwbnCPXWV9ByO25Lk-S20fex_ffbhIJGhrn7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbde4ebdb7.mp4?token=S2E9Qb4HQDjakJWcek1JB4wXHFhNNo3q-V_asZ1dKWP1e7HrlSxhYyasYy1sF0aatJITXchLdgOtK5TOf_sSQrIBLjCts05tv-VT-8KMvcpTQ9HR_hSef6m6U7fDTtZkF0zOo9wCUQAzar85gOWHec-kBZrLgJBISBXnSfSdO4QwGYRyCfPQBhThwlg-55qXzO1s4qRpSrfc4wORJ9s-SDI3S0z-KRO-bgHIYWMgUFKF11neqrK6If58EJUz7F7Bk5JupoNSNbMHGsmQurZWqRPMFX-cMMpoH0o2LtcFnqcpDEDxBPwbnCPXWV9ByO25Lk-S20fex_ffbhIJGhrn7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای روبیو: ایالات متحده همچنان در حال مذاکره با ایران است  وزیرخارجه آمریکا:
🔹
توافق با ایران ممکن است امروز، می‌تواند فردا، می‌تواند هفته آینده انجام شود.
🔹
امیدواریم با ایران به توافقی برسیم که منجر به بازگشایی تنگه‌ها شود.
🔹
مذاکره با ایران شبیه مذاکره…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/655506" target="_blank">📅 18:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655505">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k29irR09dlMR_Rdd_OuKkesFH6kblYjG71Dwrltv1QgoIvdYsjemR42KiBJpo2X55tBvJX76-n77Xi0yOtCmZBV2jcLTMfUiGsR_BaSFqEqdKHx0u0AYb2WV0cKetf65PxUNL3cCfAjcikcCNSCIjFXcreZcdheSFpF2cnrSjSvtjmdxzz3nXrPHZ_dYDSkGJE-5qyi21w4wieHidgU8FHbgonpaTNWDFgA3vxl1bhutmRym9J7Qu-7gP0_jzs5fuNXp2GKg7OzJ358mtSJ7qSiu8ipNl5ZDYNni3Fd3joOZYelzVPS8o7vA7cXafZIm1jxXI0aEHZpFVOtKiwJAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امیرعلی‌شیر نوایی؛ مردی میان سیاست، شعر و هنر
🔹
امیرعلی‌شیر نوایی از آن آدم‌های کم‌نظیر تاریخ بود؛ وزیری بانفوذ در دربار تیموری که فقط اهل سیاست نبود. هم شاعر بود، هم دستی در موسیقی داشت و هم از بزرگ‌ترین حامیان هنر زمان خودش به حساب می‌آمد. از ساخت بخش‌هایی…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/655505" target="_blank">📅 18:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655504">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkDfNNDrrc60dxelOk3kKdTBn-p-eDEaSr0E-WvjY0RsJONQAEBuZX0i8lJd66UOVa46i3ptuKmYgMLG9vG69TfTq99TFnaz1vi4LNrEntcz_aoByA4dRtcX-rvm_j88ftDmpcVfWemIGubg1v36YRXJh5e-WK8t4rkRW6KULQqbqnEGgbN5yDHoWmNWBtKYBfi9vhQSYDzNSy42v4lPwFmw1K5S7nW8yB5NTP3FqWo-Zkfb837GN2hlUe1X8gdWmnjfTQeb_xaIyAnyjPgnyi4Yv6lzCoOIUvpTYG2-cF8zYojMPHauuwBMwDhl_tEtrmqj-QeSDHNPzHGjDxFzeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاکس‌نیوز: روبیو برای استیضاح آماده می‌شود
فاکس‌نیوز:
🔹
روبیو برای استیضاح کنگره آماده می‌شود، زیرا جمهوری‌خواهان به تلاش برای محدود کردن اختیارات جنگی ترامپ علیه ایران می‌پیوندند.
🔹
هر دو مجلس می‌توانند این هفته قانونی را برای توقف دخالت ایالات متحده در جنگ ایران، بدون مجوز کنگره، تصویب کنند.
🔹
با توجه به وتوی مورد انتظار ریاست جمهوری و عدم وجود اکثریت ضد وتو، یک قطعنامه موفقیت‌آمیز در مورد اختیارات جنگی احتمالاً ضربه‌ای نمادین به دولت خواهد بود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/655504" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655503">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
اعتراف وزیر خارجه آمریکا: ایران همچنان پهپادهای زیادی در اختیار دارد
🔹
مارکو روبیو، وزیر امور خارجه دولت تروریستی آمریکا، در اظهاراتی درباره توانمندی‌های نظامی جمهوری اسلامی ایران، اذعان کرد که ایران همچنان از ذخایر قابل‌توجهی از پهپادهای تهاجمی و شناسایی…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/655503" target="_blank">📅 18:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655502">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
اعتراف وزیر خارجه آمریکا: ایران همچنان پهپادهای زیادی در اختیار دارد
🔹
مارکو روبیو، وزیر امور خارجه دولت تروریستی آمریکا، در اظهاراتی درباره توانمندی‌های نظامی جمهوری اسلامی ایران، اذعان کرد که ایران همچنان از ذخایر قابل‌توجهی از پهپادهای تهاجمی و شناسایی برخوردار است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/655502" target="_blank">📅 17:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655501">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a056ec1b1.mp4?token=Y87Sw3tS3g28vr6hogGkVIxRJtn0Eo3DXek9yXH6eDOlHllQvL8sWLPlG70IgUlw7K3DveqjyrPhUIX8xKMRVUuzM8F2AXTZFTd5aU86de-mRreSqMpxU_W7NxcYl-lrwgSBnkShMnkr_aFf0ygJLurDFekKFkq54Ru-DmUxKUEApTDIJ6Zqs2VPoJLCWyY1omDhjXOtV4FeN98tYTq_dlTe6JwP6rkX7hq2_9zF0ZSFgQYj_JnySrsDtYT8fXCPPeys66appkPxUWaqhYtkeBI6yWmKJWr3cA6A02GkAB2MHe8p2aDFwJATchUBPkJxmr0ipx8pxl4VaNEm0JESlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a056ec1b1.mp4?token=Y87Sw3tS3g28vr6hogGkVIxRJtn0Eo3DXek9yXH6eDOlHllQvL8sWLPlG70IgUlw7K3DveqjyrPhUIX8xKMRVUuzM8F2AXTZFTd5aU86de-mRreSqMpxU_W7NxcYl-lrwgSBnkShMnkr_aFf0ygJLurDFekKFkq54Ru-DmUxKUEApTDIJ6Zqs2VPoJLCWyY1omDhjXOtV4FeN98tYTq_dlTe6JwP6rkX7hq2_9zF0ZSFgQYj_JnySrsDtYT8fXCPPeys66appkPxUWaqhYtkeBI6yWmKJWr3cA6A02GkAB2MHe8p2aDFwJATchUBPkJxmr0ipx8pxl4VaNEm0JESlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از یک ساعت پشت میز نشستن لازم است این حرکات را انجام دهید و کمی قدم بزنید
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/655501" target="_blank">📅 17:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655500">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مورد مشکوک بمباران فارس؛ وزارت بهداشت پیگیر شد
حسین کرمانپور، مدیر مرکز روابط عمومی و اطلاع‌رسانی وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
در ایام جنگ در استان فارس و یکی از استان‌های جنوبی بمبارانی با نوع خاصی از موشک صورت گرفت که مشکوک بود و در حال تحقیق هستیم که ببینیم واقعا علت این نوع بمباران چه بوده است که همکاران من در بخش تحقیق و توسعه پس از بررسی آن را به اطلاع مردم و جهانیان خواهند رساند.
🔹
بمبارانی که شبیه قوطی‌های کنسرو بوده  و بعد از نزدیک شدن به آن، قوطی‌ها منفجر می‌شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/655500" target="_blank">📅 17:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655499">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ho9gBCjDv6n2PbdH8sKSZyBb1V5WSNKEcB1UVecLorX88OMt11HUTRa_xCFeFQ8s8ggUVGG_go2ht9OK9X1IldkwtNP_K542bn51kJJgfHyVbkoBlkp5ZJeMNuIRrTryKxQ6bKjojRGkAT0hXheTYyFmOQrtmDYjb3YbieBrJU2-epKLI81qYK99qOK_qyupGvun5rhmPiRksASJve1VEbw9pN_mdil2aGpl5I1ps2kFIVj85Z46IZwYSPnxgdiU3w8JuULKII352Syu81WLgaOqMu_WZfS6mTE9FSrnPQgxZOKgB0jOIKLIet4_C92Jz0tvbCvZeCYIqlMJUH9y9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازه‌های آبی شوشتر؛ شاهکار مهندسی ۲۵۰۰ ساله
🇮🇷
#ایران_زیبا
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/655499" target="_blank">📅 17:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655498">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
اینستاگرام قابلیتی را آزمایش می‌کند که از نمایش پشت‌سرهم محتوای آسیب‌زا (استرس، رژیم، تناسب اندام) به نوجوانان جلوگیری می‌کند و تا پایان سال آن را به فیسبوک و مسنجر هم می‌آورد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/655498" target="_blank">📅 17:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655497">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnDm0s7_M4ObHlPkVKAA9Xxjz-P20kuYv0tB-vJjiWxlGQmF1PfB7bcYkfY0ntRxeyrj5jQLmCWZ0yVDgkOCyRB9dCWF5tZ76Z8U_4OmEk3IGzsLhmUuwsEKiVTOb8hDB1Jh7cno3zEl4I7w8lOie5_NriQD4gacS5wkqmSBR4Adkz5sNVvinXRz62eLUzu2dgwFrQVq3fpvoIbgLswHIEtkGKGNO9UifrqJgcY5O_6TAxZtCfs-HxUlKwkr-yRcpfX34whNITPNOPN63d0lIH6D7Mzx-Id4fUDoAwe4gvrmzS8PbKyEAB1a5GgSZIQ179c-Tqhzr6XvYph0oFTYqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
📣
مژده، مژده!
📣
📣
می‌خوای میلیونر شی؟
💸
🤑
⁉️
کافیه شانس خودتو امتحان کنی
🎯
✨
حتما به دوستان خودت ام پیشنهاد بده !!
با فالو، کامنت و شِیر کردن پیج اینستاگرام MOSAVILAND
📲
🔥
https://www.instagram.com/mosaviland?igsh=MXYxajhld3U5MnRkMw==
در قرعه‌کشی بزرگ این ماه شرکت کنید
🎁
🎉
به قید قرعه، به ۵ نفر جایزه نقدی پرداخت می‌شود
💰
✅</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/655497" target="_blank">📅 17:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655496">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سه روز مراسم بدرقه مردمی برای تشییع پیکر «امام شهید»  معاون شهردار تهران:
🔹
برای برگزاری سه روز مراسم بدرقه مردمی پیکر «امام شهید» برنامه ریزی شده است.
🔹
مراسم تشییع در تهران حداقل ۲۴ ساعت طول خواهد کشید.
🔹
محل خاکسپاری امام شهید طبق وصیت ایشان و توصیه‌های…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/655496" target="_blank">📅 17:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655495">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
نوحه‌خوانی خواننده آمریکایی در مدح امام علی(ع)
🔹
احمد ایبو خواننده و نوازنده آمریکایی-اندونزیایی در آستانه عید غدیرخم با اجرای خیابانی، قطعه‌ای را در ستایش جایگاه و عظمت امام علی(ع) اجرا کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/655495" target="_blank">📅 17:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655494">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDt4pC2GS1MtDDIUjTUsBsTMwH63A56xZ2oxHTF85l8lHkL8ZxtlG5WeJ_nxb1QaYc9mIYMAfdd9e2ASvdzjEsVLr2jaemboUW4HtFbuIwmtsz7-j-Te2uYz-UFEfB3VaJ4c7R2H56iaXMWOukxdsuWJotcpYWZmpr_pViTbMnNe3nY38D43pqCl9om7PLGi71KkwECDATfvvIc_-f-IBaDRj7_myXYb-ifAiBpn60J4ZYjC0_1bj7GupE199KGV23l1xctRue_BXvlqlavaKCyJzJ2TrTICs86BlE3Qgy0YjsX18YX5El3ApgWT2pnRR1n5CMeB2v1baNys7YtAOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلا گرفتار انحصار شد/ چرا بانک مرکزی خزانه طلای آنلاین را در اختیار یک بانک قرار داده است؟
روزنامه هفت صبح نوشت:
🔹
در ماه‌های اخیر موضوع نحوه نگهداری ذخایر طلای پلتفرم های خرید و فروش آنلاین طلا به یکی از دغدغه های مهم کاربران کارشناسان اقتصادی و حتی نمایندگان مجلس تبدیل شده است.
🔹
طبق رویه فعلی تمامی ذخایر فیزیکی طلای این پلتفرم ها در بانک کارگشایی نگهداری می شود؛ موضوعی که به اعتقاد بسیاری از کارشناسان میتواند تبعات اقتصادی امنیتی و حتی پدافندی به همراه داشته باشد.
🔹
معتمدی زاده کمیسیون اصل ۹۰ نیز اعلام کرده است که انحصار نگهداری طلای پلتفرم های آنلاین را از رئیس کل بانک مرکزی پیگیری می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/655494" target="_blank">📅 17:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655493">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee5d44296.mp4?token=v0ns2Xk8jf3f3XyLQOE7iUHZZg73RkMnrditIbEoiY5cj1wv55lKhR15shR3hEJvh2rQJUjtAwqIOZ1itdJ9ahePq0Wyvzz-XPrRvq0UiEjBhBqAvThE37HL7NvGnEPLKWkJtHZj-mn34JqPqfNc03MmbGB52bU73OBrgiiy7O88kot5IA_fAP-8PnNK-q6JM7mJFvuAu2okhKaa-xjCqkjhnpYPRRf8ZV0s4UGnY73tCClLOH9JbzYmpskwnvQgH9GWLj1MOqfvg-mvM6Nr5AQUK7yNc0VThAWA321uZSX9HX86sgKaHwmRaiu4fGkl6DuijH5NKV7Ec5HKons9yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee5d44296.mp4?token=v0ns2Xk8jf3f3XyLQOE7iUHZZg73RkMnrditIbEoiY5cj1wv55lKhR15shR3hEJvh2rQJUjtAwqIOZ1itdJ9ahePq0Wyvzz-XPrRvq0UiEjBhBqAvThE37HL7NvGnEPLKWkJtHZj-mn34JqPqfNc03MmbGB52bU73OBrgiiy7O88kot5IA_fAP-8PnNK-q6JM7mJFvuAu2okhKaa-xjCqkjhnpYPRRf8ZV0s4UGnY73tCClLOH9JbzYmpskwnvQgH9GWLj1MOqfvg-mvM6Nr5AQUK7yNc0VThAWA321uZSX9HX86sgKaHwmRaiu4fGkl6DuijH5NKV7Ec5HKons9yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشتی حنظله ۲ حرکت خود را برای شکستن محاصره غزه از سر گرفت
🔹
کشتی «حنظله ۲» در ادامه سلسله‌اقدامات بین‌المللی برای شکستن محاصره دریایی نوار غزه، سفر خود را از پایتخت سوئد از سر گرفت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/655493" target="_blank">📅 17:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655487">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7306ca33dd.mp4?token=kIpB6VoiorbNYh1MLTdELbJyKnLyUkvE9_tC5UMlAUMWaw7j2hdU7QmYxtYALnpvwlm32qkiYCi0C-dfGLzqznjeWsGPaI_lFeFG8qFM_IieXBSwXcSVTomw_aQdrMG41kCiYQJNKqcpG-gRDpTky65AVkkFTGRvfmFkQcuTsSMUUmgwdGOuGqCTB5Amb6PnX5d9w0axoVkyRdc8tBAVv58jChHeh2sJTUWv-p1V2anREM51a7qwG-hmYx2t0LkV1lYq70JbK2FR0FloUBt_6pA7uHm4WB5ItDoWjlPHUllcBNYVizsX4DU0ixEeqHxGEuBUVmBMDWdLNlJdfQdQjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7306ca33dd.mp4?token=kIpB6VoiorbNYh1MLTdELbJyKnLyUkvE9_tC5UMlAUMWaw7j2hdU7QmYxtYALnpvwlm32qkiYCi0C-dfGLzqznjeWsGPaI_lFeFG8qFM_IieXBSwXcSVTomw_aQdrMG41kCiYQJNKqcpG-gRDpTky65AVkkFTGRvfmFkQcuTsSMUUmgwdGOuGqCTB5Amb6PnX5d9w0axoVkyRdc8tBAVv58jChHeh2sJTUWv-p1V2anREM51a7qwG-hmYx2t0LkV1lYq70JbK2FR0FloUBt_6pA7uHm4WB5ItDoWjlPHUllcBNYVizsX4DU0ixEeqHxGEuBUVmBMDWdLNlJdfQdQjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💚
پک استوری ویژه عید غدیر
💚
#عید_غدیر
#استوری
#امام_علی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/655487" target="_blank">📅 17:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655486">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VERXBh0ZKalVS0akxHDFSs9w_NsG0AuPcOOAGxBCpjWbOsInCUkx_YRIc7emB1SDWIXPSGz1eLWWgPColuM-j7Vg1lKJExdf8-_s3zKSHSQMFeIUZwJxlj79E-naWF5q_fXZTiY6d7v38WIvXmqOvFDdyF4XRxJqgz4OR9qat2qapqY5Dkb9TFbZni8SxTAf_FIg4tVXJnZw3nybrAUVd3Q6S_D5aiMowVKXPVrJEXGMUR3V2_rG5Gxmkv42rAd8jcJIJqO7uaz_brHvh660pAY8KcFr1bCenoxftuFuG0xT7RvOu7ajoXuOziqmxkhzUS4GDXZywl7XEsOuRUI51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ویلیام پولت به عنوان مدیر موقت اطلاعات ملی خدمت خواهد کرد
🔹
تولسی گابارد در پایان ماه جاری میلادی از این سمت کناره‌گیری خواهد کرد.
#Devil
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/655486" target="_blank">📅 17:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655485">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
روایت فوربس از قابلیت جدید ایران برای مقابله با آمریکا
فوربس:
🔹
متحدان حوثی ایران در یمن می‌توانند با هدف قرار دادن احتمالی تنگه باب‌المندب، آبراه حیاتی متصل‌کننده اقیانوس هند به دریای سرخ را ببندند.
🔹
گرچه ایران با تنگه باب‌المندب هم‌مرز نیست، اما حوثی‌های یمن با آن هم‌مرز هستند و می‌توانند آن را تهدید کنند.
🔹
طبق گزارش آژانس اطلاعات انرژی آمریکا، روزانه ۴.۱ میلیون بشکه فرآورده‌های نفتی از طریق این تنگه عبور می‌کند.
🔹
باب المندب، که پس از عبور از کانال سوئز در مسیر دریایی به آسیا واقع شده است، جدا از نفت، حدود ۱۲ درصد از کل تجارت جهانی را به خود اختصاص داده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/655485" target="_blank">📅 17:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655484">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt1SSiO-8hJl4imBY9whSdvSmfh7DAOosCZVLaMfq2-tlmt1TZHOdHhz6vNWRCtryp6LU9i2M9IMmDleFZnhyI5CqBOdYhsqMwgyKP8LDB6iJGM2QM6uaf4Oe5wWJsDD2rAekP87M3W7fJqpmib-UeJtLW2r8VbXM6fSmYOqdAY4Fa_4G-WOKp0fH6dDufbXu1C6-X9xfZn5bKrbKF-P0_xkmF86iZTovVWjopE98dz9sFDXXkzy7quu5GxUAB1hKyDZqDfA_Tm5X_7AL5zsjBwxtgrBLfK88QYX7BwjlpjLozWR20IbnMblBGR_PEenv3LU2A9gZpsKloSgG5hcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کیم کارداشیان می‌تواند رئیس جمهور آمریکا شود؟
🔹
در سال‌های اخیر، نام کیم کارداشیان نه‌تنها در دنیای سرگرمی، بلکه در حوزه مطالعات فرهنگی و رسانه‌ای نیز وارد شده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219908</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/655484" target="_blank">📅 17:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655483">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به چالش‌های کم‌آبی، آیا راهکارهای کاهش مصرف آب در خانه را پیاده‌سازی می‌کنید؟</h4>
<ul>
<li>✓ بله، اقدامات متعددی انجام داده‌ام</li>
<li>✓ صرفاً در حد رعایت عمومی (مثل بستن شیر آب هنگام شستشو)</li>
<li>✓ تصمیم به تغییر الگو دارم، اما اطلاعات کافی درباره روش‌های بهینه‌سازی خانگی ندارم</li>
<li>✓ مصرف من در حد استاندارد است و تغییر خاصی در رفتارم ایجاد نکرده‌ام</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/655483" target="_blank">📅 16:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655482">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f5fb0ee7.mp4?token=OJiNHDsKpHLTcvpppA3V0yMKMmzwFyxA8xE6bWul5VXKrMPBmsoU9NqfesBhrRHdN8Htt5h2AsbW1AvawKzizw6-Hp5r_pf5GEkyO3QwHK_95lotOEIDYpkFLv55nXbVrrJPDyOpHNaEv3Z0__kmqnq7dB2MSeMa-uxASt1Q7M9p_YEIcO2k8fHw4fCEyzeCo7QdR0WOSm46hAxbLeu897t1OjwvLzgfXrlqlKcjqF3FuubkzvKDrNeWsD5twuf7P8pBMo5-SKd07GmhEyEHY-K1Mic3ZFaYmGiU2aKQSjAtAPxs14fRB4vh8ioEXnzZWhNODfWu7YDGfHm8MJdA-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f5fb0ee7.mp4?token=OJiNHDsKpHLTcvpppA3V0yMKMmzwFyxA8xE6bWul5VXKrMPBmsoU9NqfesBhrRHdN8Htt5h2AsbW1AvawKzizw6-Hp5r_pf5GEkyO3QwHK_95lotOEIDYpkFLv55nXbVrrJPDyOpHNaEv3Z0__kmqnq7dB2MSeMa-uxASt1Q7M9p_YEIcO2k8fHw4fCEyzeCo7QdR0WOSm46hAxbLeu897t1OjwvLzgfXrlqlKcjqF3FuubkzvKDrNeWsD5twuf7P8pBMo5-SKd07GmhEyEHY-K1Mic3ZFaYmGiU2aKQSjAtAPxs14fRB4vh8ioEXnzZWhNODfWu7YDGfHm8MJdA-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی منتسب به آیفون اولترا طراحی اولین گوشی تاشو اپل را نشان می‌دهد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/655482" target="_blank">📅 16:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655481">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دستور پزشکیان؛ برق صنایع به هیچ عنوان قطع نشود
آرش نجفی، رییس کمیسیون انرژی اتاق بازرگانی ایران در
#گفتگو
با خبرفوری:
🔹
مدیر عامل توانیر هفته گذشته گزارشی را به دبیرخانه شورای سه قوا ارائه کرد مبنی بر اینکه امسال در زمان‌های پیک ۱۲ هزار مگاوات کسری برق داریم.
🔹
سال گذشته ۲۲ هزار مگاوات بود که امسال ۱۲ هزار مگاوات است که نسبت به سال گذشته ۱۰ مگاوات کسری برق کمتری داریم. نزدیک به ۷ هزار مگاوات نیروگاه خورشیدی در مدار است.
🔹
رییس جمهور هفته گذشته در اتاق بازرگانی دستور دادند که به هیچ عنوان برق صنعت قطع نشود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/655481" target="_blank">📅 16:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655480">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip-OxPqtXaXawhMPPINUTA7jU1_n67ocduFYehIZOEs1iSYBCJU8B57b0jWQrblASzTxZHfFAhfjEgkmJ7om3doivPZ_5s41JmLTIJ78zeYXwbpu1rXBuORLw7oPIyyk5PPM_AKjoK6GeDeKV8t-e_H352O0YLMVO04lAGNPIL882hJTdaauejvWsji0OcizWBv6bmRRyCZC1HuL_Fnfxvzt52yLp9tKJShib7Euph2C5J8PpyocY6ILw5kP5OHnI0-o2vM2q9n4jaCUF_4XW-h80H_T6uzMdu1r6hgIpEtmgHFzIuPCOcZMQjOizI_pLIZ13kgnGF6s0Q64Sl7BFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده کنگره آمریکا: مفقود یا کشته شدن ۱۱ دانشمند ما تصادفی نبوده و بسیار نگران‌کننده است
🔹
جیمز کومر: ببینید، آنچه در ایران می‌گذرد به قابلیت‌های هسته‌ای مربوط می‌شود و این که آمریکا نمی‌خواهد ایران به سلاح هسته‌ای دست یابد. ما به‌وضوح رهبر بلامنازع…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/655480" target="_blank">📅 16:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655479">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gc6VGtu41Rb0VzA0rXsVnE3Gj_sddhFX_B6k6v4ZSGsKXV0nsVSjbgNwg5nUyXW2sjTFyO_mcI9vldoG3_G2g6ILK_1uyJSU0ejujTcukhUmlXNH2SLL4cqqntpuGJuXdjDb-BPbC-V1EBcqJxBXS2W9U4Lc_tfWRnsLJaoWjjygOb1qBmZ0DUN4ZfSBbZw0tz3AmXsVjzHdBByZh-KpBUZw3C15tK-vQT8zl4qypDlIvIEmdVcIgeKwV6tXuhwDjysTbpCXEwo0JDlV6-gW4iJkfKah8hs0ZEL8rtCjTwHyFJccervvddmnedD9oca46eXRjBcaJW67SI9i0R5qVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: ۷۰ کشتی با کمک آمریکا از تنگه هرمز عبور کردند  یک مقام رسمی به نیویورک تایمز:
🔹
فرماندهی مرکزی ایالات متحده در سه هفته گذشته به عبور حدود ۷۰ کشتی تجاری از این تنگه کمک کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/655479" target="_blank">📅 16:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655478">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea08292349.mp4?token=JcNI8hxUZSDd1rtR718zxKtC87c6DcxRDpYHETeh356qQ0GD6bDrs4UBt3S_7lci5UYztuZoHfo7CLXQRYCZJrM_DfnZvEi8dhlIrXdHAQ9b11UNhLmTnypaA7HtFo6qB5xLKZOPy_oZImjIE3WxwCgw3B896NMEW1svrB2ET7Fh1nq5GhWa2o7GIDtiVjm4geFWm1REdKvMwhQx8e6X8AebztLmTNOZOIoHu7KQjYDkAJAOhnuvTdMBNH8sK3lS6vTg7HIyGyEzgrQ4e61ReyaXfVJyWOYa-UXX3hdHTF-YFkAI7uUbbpc8VBlUMJ5nTIujG0YFZadu2y3Eu1-5Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea08292349.mp4?token=JcNI8hxUZSDd1rtR718zxKtC87c6DcxRDpYHETeh356qQ0GD6bDrs4UBt3S_7lci5UYztuZoHfo7CLXQRYCZJrM_DfnZvEi8dhlIrXdHAQ9b11UNhLmTnypaA7HtFo6qB5xLKZOPy_oZImjIE3WxwCgw3B896NMEW1svrB2ET7Fh1nq5GhWa2o7GIDtiVjm4geFWm1REdKvMwhQx8e6X8AebztLmTNOZOIoHu7KQjYDkAJAOhnuvTdMBNH8sK3lS6vTg7HIyGyEzgrQ4e61ReyaXfVJyWOYa-UXX3hdHTF-YFkAI7uUbbpc8VBlUMJ5nTIujG0YFZadu2y3Eu1-5Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور ترید کنیم تا همیشه ضرر کنیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/655478" target="_blank">📅 16:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655477">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
تبادل پیام میان ایران و آمریکا فعلاً متوقف شده است
یک منبع آگاه:
🔹
در حال حاضر تبادل پیام میان ایران و آمریکا متوقف شده و دست‌کم چند روز است که هیچ پیامی در چارچوب دستیابی به یادداشت تفاهم اولیه میان تهران و واشنگتن رد و بدل نشده است. این در حالی است که برخی رسانه‌ها و مقام‌های غربی تلاش دارند روند ارتباطات میان دو طرف را عادی و فعال نشان دهند.
🔹
برخلاف ادعای اخیر رئیس‌جمهور آمریکا مبنی بر اینکه گفت‌وگوها با ایران با سرعت بالایی ادامه دارد، آخرین پیام جمهوری اسلامی ایران به واشنگتن، پیامی صریح درباره لبنان بوده که بازتاب گسترده‌ای در سطح بین‌المللی داشته است./ فارس
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/655477" target="_blank">📅 16:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655476">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
جام جهانی ۲۰۲۶ با قوانین تازه از راه می‌رسد
فیفا چند تغییر مهم را برای مسابقات جام جهانی ۲۰۲۶ در نظر گرفته است:
🔹
پوشاندن دهان با دست، بازو یا پیراهن هنگام بحث و درگیری با سایر بازیکنان یا داور، می‌تواند با کارت قرمز همراه شود.
🔹
اوت باید ظرف ۵ ثانیه پرتاب شود؛ درغیراین‌صورت توپ به تیم حریف واگذار خواهد شد.
🔹
بازیکن تعویض‌شده فقط ۱۰ ثانیه فرصت دارد زمین را ترک کند؛ در صورت تأخیر، بازیکن جانشین با یک دقیقه تأخیر اجازۀ ورود پیدا می‌کند.
🔹
در هر نیمه یک وقفه ۳ دقیقه‌ای برای نوشیدن آب (حدود دقیقه ۲۲) در نظر گرفته شده است.
🔹
هنگام مداوای دروازه‌بان در زمین، بازیکنان اجازه ندارند کنار زمین بروند و از مربیان دستور تاکتیکی دریافت کنند.
🔹
سرمربیان می‌توانند در زمان توقف بازی از لپ‌تاپ و تجهیزات الکترونیکی برای انتقال نکات تاکتیکی استفاده کنند، اما بازیکنان باید داخل زمین بمانند.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/655476" target="_blank">📅 16:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655475">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ساخت «اخراجی‌های ۴» پس از بهبودی حال اکبر عبدی
مسعود ده‌نمکی، کارگردان سینما و تلویزیون در
#گفتگو
با خبرفوری:
🔹
با توجه به وضعیت جسمانی آقای عبدی، فعلا ساخت و تولید مجموعه جدید اخراجی‌ها به تاخیر افتاده است. بخشی از کار به وقایع اخیر برمی‌گردد اما این‌طور نیست که بگوییم کلیتش در ارتباط با جنگ است.
🔹
پس از مساعد شدن وضعیت حال آقای عبدی، در مورد کار تصمیم‌گیری می‌کنیم. آقای عبدی از بخش عمومی برای ادامه درمان در خانه هستند و حال عمومی‌شان بهتر است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/655475" target="_blank">📅 16:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655474">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oc8KeshBA7yLpYDpsi3b6lmlSVQPtfAC9-8Oze_3iXEBH2ldn3BMB68yca6BHi3JU7lz845gJURz9Oy9mZXpfdT16PL8stZyjddipDj3ECscJJsNGKvf_ROVI6jEj5KDDbu3orm5F7rsZ7tx6dk2Z2HjA0-SiWHY50e0gmAkm9lXOiWLaa_A6kCM7RCMjIx5RYeJ7rDQjBCX93TZ7qmHby5y_Zi_xoMEzH48I3kB70fy9cyRRxy04QanV9HOZNG1S85MmHSaJp4f8kg-xHXKHw_oInFX2fbCHX3uAo5gPVpvqRYqjUz4Ct6KTa-j3hM1lr9LKrWeKgestCLk4eq-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی AI حقیقت را فدای مهربانی می‌کند
🔹
طبق نتایج یک پژوهش جدید، چت‌بات‌هایی که برای پاسخ‌های دوستانه‌تر و همدلانه‌تر تنظیم شده‌اند، در برخی آزمایش‌ها تا ۶۰٪ بیشتر از مدل‌های معمولی اطلاعات نادرست ارائه کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/655474" target="_blank">📅 16:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655473">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cac4a7e999.mp4?token=cTW1J3e4rToS4krhXX8jKXUcQ-SxEsFHd8D76-DTAjta7cfqeT3Zkp0gjwWQqSc5bkfk8j3vBSDwba3oMY3c2Q_WhL1siYKknb4VTqDg4qorJsH9jMkJTS6vwrZS1mGcPC2pC3keKoCwOf4-un923wXrtkzMrq5pegcIDherTLyku5Yxt6mPZqdu2GPlv-QeSQLFjgL_N0fISgvofhCgVpLEGymu73dDJAmewXQrcfJjo6BuVQtmAxqGbWKik9oeEOhMT-oi1BlYqyFTbc2FwyAep3aiSFH23cXr95qHVk3AOYPiu3Wqps2gPDpmQ7wmN3tegy3WkBIWa1dHDJJQpjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cac4a7e999.mp4?token=cTW1J3e4rToS4krhXX8jKXUcQ-SxEsFHd8D76-DTAjta7cfqeT3Zkp0gjwWQqSc5bkfk8j3vBSDwba3oMY3c2Q_WhL1siYKknb4VTqDg4qorJsH9jMkJTS6vwrZS1mGcPC2pC3keKoCwOf4-un923wXrtkzMrq5pegcIDherTLyku5Yxt6mPZqdu2GPlv-QeSQLFjgL_N0fISgvofhCgVpLEGymu73dDJAmewXQrcfJjo6BuVQtmAxqGbWKik9oeEOhMT-oi1BlYqyFTbc2FwyAep3aiSFH23cXr95qHVk3AOYPiu3Wqps2gPDpmQ7wmN3tegy3WkBIWa1dHDJJQpjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شست‌وشوی ضریح علوی در آستانۀ عید غدیر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/655473" target="_blank">📅 16:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655472">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USH1y8DBK50am_29FpOpgE6rhfBgf0vZLi2SJcH_l1gA_LM_EdwJ9fIKffppwdo9vU6GGRmAh404MWyxNwBtSWD_6JNoIq0t_rSvK4tDWo3_xt1ogAPuesyIJDa1MGnJ32JdZaaVEemMvpwdvtSTIQxCXvH5kUyzectqTfPm199ITBB7fFSbUV-flThJZUckfXOZUtK2jYiLXqIeHAkqGPXwxFP0MapH7yDdK_baY4jKX6122fXPijmg_2ZYfcbvZfmb8VJCSAncrinaCL_XPeXlYknlN51liQII3a04sz64EQ7DMYwI6cevbh-CYF5rA2biT-6AAc-3qqCA15RWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت باشگاه سپاهان: برای اخذ مجوز حرفه‌ای، ‌مدارکمان را به کمیته بدوی AFC ارسال کردیم
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/655472" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655471">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
معاون شهرداری تهران: تشییع پیکر رهبر شهید در سه شهر تهران، قم و مشهد قطعی است؛ در حال تدارک برای جمعیتی بیش از ۱۵ تا ۲۰ میلیون نفر در پایتخت هستیم
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/655471" target="_blank">📅 16:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655470">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jG1y3e2aWr9Ur3nONKTxVa-5EWwRfUeL8qaFRmiNa6pVAjxd2M52tutQjCPwnYfsNYjFJuyhFF7yuzxvtTgYatyMzVCe3Hz1-LFbLZP4opOBloOGNSHTGJ5N-bM-b1GYcjYDFsHgdg8rqyv_vd5dooXha_U-t6hgDjEgf-Ud0iOV_Zte6wouomAX6euIaNz_81CEudxIP-5nHDMSg8ENUNo8ugHVpusf3udyLnpjis06Xnu71C75exOKmRWA4aWXWPM56UBrFAr1KThmOEDZCMAyzloVqJ3hMdCwE7f4D6wtx938nrjs4yVdmRK5w9U_g7xHPTI-uhyJnZxOQyYlVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سود هنگفت سوریه از جنگ آمریکا با ایران
رویترز:
🔹
جنگ ایران در منطقه، آسمان سوریه را دوباره به شاهراه هوایی خاورمیانه تبدیل کرد. در ماه می، ۱۱,۸۰۱ پرواز از حریم هوایی سوریه عبور کردند که بیش از دو برابر فوریه و جهشی ۳۷۵ درصدی نسبت به سال قبل است.
🔹
آسمانی که در طول جنگ داخلی ۱۴ ساله سوریه منطقه ممنوعه بود، اکنون به مقرون‌به‌صرفه‌ترین مسیر برای خطوط هوایی منطقه‌ای تبدیل شده است.
🔹
دولت جدید سوریه نیز با دریافت ۴۹۹ دلار از هر پرواز، ماه گذشته نزدیک به ۶ میلیون دلار درآمد داشته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/655470" target="_blank">📅 16:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655469">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piZhbq0b_QKxGJpfvll5d1zNWsug6MAb5RwObr5nAiTpYsiBvHW3FwQvTjWj1s7F2ym2GKYj2EBxPv4Wav4dkqYj5v8XhO-JH7rwMYJLPN6fVSczqUDRqBu7Q-Km40lQd1NG84rwqsdiOV1KeA1FGu2xK6DWOtIrpTqpiNDg16ORFfGsjfbFBD1-8Cg9DaOCbLlfM77lwUyK6ccMOWNczow-5X4PZYHEXzRLCFnyp7bBXiQYZy0ifXNjbcUQvQbVwVF3U2t_px5bfR4UTJqpzXPXTiUkOqRfJyLEseCTzWMGXuokbcIGCuFzxuwsZHqcNC_AsokMvQ5v4YFRQD551A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/
نوشهر
📍
چلک
۵۰۰ متر زمین
۷۰۰ متر بنا
تعداد خواب ۵
استخر روباز و استخرداخلی
شمالی-جنوبی
چشم انداز جنگل و دریا
سند تکبرگ و مجوز ساخت
دسترسی عالی تا دریا
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/655469" target="_blank">📅 16:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655468">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6192aa3cc.mp4?token=m_1cRd9l4nC_ej6l5ozjN5xJiLGnn3SkRUV4guFFLiDyGKEoxDldB6bfe9MhdYezypXmnkzDrgesMNOEY3HZFEc5Qk5THL5MXwKAx_0KOTUzd-oOWrZXYKTO22x_BcGGaj0ThyG85vWCAKjFPdtiStQoxTp0blLTR889aValjhZdohDIo9323nuaLoYc2zFXpZ8pymEi2_U9tQj1MKj-PB99YwufjE6rGGjOBs1AG9nETcMCwjvbbWCK7_6kIX84oxlpKVVymYUr3KF7GDjdc0MQAKvjLfZgX4MiXvj_PwcU5Xo0vUox15-V5agL3QeAzKxKbpu8-APQCRH_jxPMng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6192aa3cc.mp4?token=m_1cRd9l4nC_ej6l5ozjN5xJiLGnn3SkRUV4guFFLiDyGKEoxDldB6bfe9MhdYezypXmnkzDrgesMNOEY3HZFEc5Qk5THL5MXwKAx_0KOTUzd-oOWrZXYKTO22x_BcGGaj0ThyG85vWCAKjFPdtiStQoxTp0blLTR889aValjhZdohDIo9323nuaLoYc2zFXpZ8pymEi2_U9tQj1MKj-PB99YwufjE6rGGjOBs1AG9nETcMCwjvbbWCK7_6kIX84oxlpKVVymYUr3KF7GDjdc0MQAKvjLfZgX4MiXvj_PwcU5Xo0vUox15-V5agL3QeAzKxKbpu8-APQCRH_jxPMng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تازه‌ترین تصاویر از تنگهٔ هرمز
و کنترل ایران بر این آب‌راه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/655468" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655467">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPJhRWum5FHFhLdhk2Q2-qs3wd_GB08x7b1RJvMD7cwgTqqmdBcbLWaLsC34Z_zaGVCz46buhQ2TTb0DmLZRDBsW3-IvElTmp8zfHRVyOfvHOvfBvfC0mE8VSrZ4386Tc7mfowF3ZxXbE3m2TSqZ9lJ2pR-3e5-6rG8cfgmI3Y-_1VjbmNQ3G4kDDCAzcGTc7yZjdPJvO0XamUPV5vqTWgIZ8Tt1ePMwPOuHw-oJBP0V3Zf6wtJwlgI6u-RDYQPT1m8_8ZbO9NMzYGc7yU6wluJI6FNhAlblVxt3_vQRJs8-HF3DK4a2bejHusJD316QSVmOJhxKvTy1BZf1-61JDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پر باران‌ترین شهرهای ایران در بهار امسال
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/655467" target="_blank">📅 15:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655466">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
حماس: آماده واگذاری اداره غزه به کمیته ملی هستیم
حازم قاسم، سخنگوی جنبش مقاومت اسلامی (حماس):
🔹
این جنبش آمادگی کامل برای واگذاری اداره نوار غزه به کمیته ملی مورد توافق را دارد؛ آنچه مانع فعالیت این کمیته می‌شود، رژیم اشغالگر و نیکولای ملادینوف، مدیر اجرایی شورای صلح است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/655466" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655465">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
جزئیات ادعایی نیویورک‌تایمز از پیش‌نویس توافق تهران و واشنگتن
نیویورک‌تایمز:
🔹
در این پیش‌نویس، نوعی توافق عدم‌تجاوز با توقف ۶۰ روزه درگیری‌ها قرار دارد که در صورت پیشرفت مذاکرات، قابل تمدید خواهد بود.
🔹
واشنگتن می‌خواهد تنگه هرمز فوراً بازگشایی شود، اما تاریخی برای لغو محدودیت‌های باقی‌ مانده علیه ایران تعیین نکرده است.
🔹
احتمال ایجاد صندوق سرمایه‌گذاری ۳۰۰ میلیارد دلاری برای ایران که به‌عنوان بازسازی پس از جنگ مطرح شده و در صورت نهایی شدن توافق، آمریکا به راه‌اندازی آن کمک خواهد کرد.
🔹
با این حال، مسائل زیادی هنوز حل‌ نشده باقی مانده‌اند؛ از جمله جدول‌های زمانی، سازوکارهای اجرایی و شکل نهایی توافق./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/655465" target="_blank">📅 15:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655464">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
مرگ مرموز پیرمرد پس از درگیری با داماد سابق؛ تحقیقات جنایی آغاز شد
🔹
پس از فوت مشکوک مردی ۶۷ ساله به‌دنبال درگیری با داماد سابقش، پرونده‌ای جنایی در این خصوص باز شد. دختر متوفی مدعی است که در روز حادثه، همسر سابقش به پدر او حمله کرده و ضرباتی به وی وارد کرده است؛ ساعتی پس از این درگیری، پیرمرد هنگام تعویض قفل در ناگهان جان باخت.
🔹
با شکایت این زن، بازپرس جنایی دستور تحقیقات تکمیلی را صادر کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/655464" target="_blank">📅 15:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655463">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e270db2232.mp4?token=IfZJibbbg_u6nJd6u0VVxbkUDwIgfRioU5vWSGTkQMyRLklD-3ZxkqTrttLInS5QgxMxL8AOTGo__nxP592x4PWXQ1OnGN30IAQ_Z9hKIJ8Qnk_856hUdI44i2iAcEW109JGryROIv2SFLGHP4Djy3TBV1b7OZ5hIhh5qI8AOGbGVrEYSSz1HyaeHx-EvLqChNELIEIrGbgtAa2rHxnXIdnw1qRuVlTqFuLC-hguH970NDzgdbG0Hoz1ZDomg3JI5WP54Cxf1yYxbMFIppZAF4a9mcUkZgMnYJcl08S52mK0BQuFreugX-7ymKGTwLB9reV7pMY0QdcBo8EfJK3HZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e270db2232.mp4?token=IfZJibbbg_u6nJd6u0VVxbkUDwIgfRioU5vWSGTkQMyRLklD-3ZxkqTrttLInS5QgxMxL8AOTGo__nxP592x4PWXQ1OnGN30IAQ_Z9hKIJ8Qnk_856hUdI44i2iAcEW109JGryROIv2SFLGHP4Djy3TBV1b7OZ5hIhh5qI8AOGbGVrEYSSz1HyaeHx-EvLqChNELIEIrGbgtAa2rHxnXIdnw1qRuVlTqFuLC-hguH970NDzgdbG0Hoz1ZDomg3JI5WP54Cxf1yYxbMFIppZAF4a9mcUkZgMnYJcl08S52mK0BQuFreugX-7ymKGTwLB9reV7pMY0QdcBo8EfJK3HZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده جرقه‌های قرمز مرموز بر فراز آسمان تبت
🔹
جرقه‌های قرمز، پدیده‌ای نادر که در ارتفاعات بالای طوفان‌های تندری شکل می‌گیرد و تنها چند میلی‌ثانیه دوام دارد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/655463" target="_blank">📅 15:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655462">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سازمان هدفمندسازی یارانه‌ها: بخش اول مطالبات گندم‌کاران به حساب کشاورزان واریز شد
🔹
در این مرحله ۵۰ همت از حدود ۱۱۰ همت مطالبات گندم کاران پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/655462" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655461">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">معاون شهرداری تهران: برگزاری مراسم تشییع پیکر رهبر شهید در عراق در حال بررسی است</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/655461" target="_blank">📅 15:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655460">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون
شهرداری تهران: برگزاری مراسم تشییع پیکر رهبر شهید در عراق در حال بررسی است
🔹
روسیه:‌ انتقال اورانیوم غنی‌شده ایران به خارج از کشور ضروری نیست
🔹
زارت کشور بحرین سفر شهروندان خود به ایران و عراق را تا اطلاع ثانوی ممنوع کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/655460" target="_blank">📅 15:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655459">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b36b489d38.mp4?token=CTfkCa8YWwa40_8-WeG4JuWDzGiji07F2XyIKSf2OpXvKN0Gq2oA4mTvhzOBfq_jQ4y4WGTo67sgQp_rAlgmkyF_NqKQP0q6AH1KTxgNfh4-QJRGwzsjFTvqnMjTR_NoGPwfWrb_zgP0dGjvvqcMh88Hn56kkM8cQe5Ph5w_FycpGF-FRaaZN-vjavipy-BCL1X-oK-A_EhvmvcEuCel1VEWLJCZ1jQP2vXKsjbKjvyFm29wkR6IQjxJ6BeNEBiUKQS5A4aXGhPIzVr6725DLpxDsR6whM7oGaNY2N6d6JARSPLG7encRIK7GwTvgUpvzhPF5vtM2lZgIBBwnHDSiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b36b489d38.mp4?token=CTfkCa8YWwa40_8-WeG4JuWDzGiji07F2XyIKSf2OpXvKN0Gq2oA4mTvhzOBfq_jQ4y4WGTo67sgQp_rAlgmkyF_NqKQP0q6AH1KTxgNfh4-QJRGwzsjFTvqnMjTR_NoGPwfWrb_zgP0dGjvvqcMh88Hn56kkM8cQe5Ph5w_FycpGF-FRaaZN-vjavipy-BCL1X-oK-A_EhvmvcEuCel1VEWLJCZ1jQP2vXKsjbKjvyFm29wkR6IQjxJ6BeNEBiUKQS5A4aXGhPIzVr6725DLpxDsR6whM7oGaNY2N6d6JARSPLG7encRIK7GwTvgUpvzhPF5vtM2lZgIBBwnHDSiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوانندگی آقای مجری در پخش زنده شبکه سه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/655459" target="_blank">📅 15:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655458">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
رای دیوان عدالت اداری برای تعیین محاسبه کسر قیمت وسیله نقلیه در اثر حادثه
🔹
هیات عمومی دیوان عدالت اداری تبصره ماده ۶ دستورالعمل نحوه محاسبه قیمت وسیله نقلیه را که محاسبه کسر قیمت خودرو در هنگام حادثه را منوط به حداکثر ۱۰ سال از ساخت خودرو کرده بود ابطال نمود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/655458" target="_blank">📅 15:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655457">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تله بزرگ در پلتفرم‌های درج آگهی
🔹
در برخی پلتفرهای درج آگهی، کلاهبرداران روش جدیدی یاد گرفته‌اند که به راحتی کاربران را فریب و جیب آنها را خالی می‌کنند.
🔹
جزئیات را در این ویدئو بشنوید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/655457" target="_blank">📅 15:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655454">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ثبت بیشترین ارزش معاملات بورس در سال جاری
🔹
شاخص کل بورس امروز با جهش ۴۴ هزار واحدی به ارتفاع ۴ میلیون و ۳۴۴ هزار واحد رسید و شاخص هم وزن هم ۱۰ هزار واحد بالا آمد. ۶۱ درصد نمادها امروز سبزپوش شدند.
🔹
اما هیجان اصلی جایی است که حقیقی‌ها ۴.۳ همت پول تزریق کردند، ارزش معاملات خرد به ۲۸.۵ همت رسید و صف‌های خرید ۲۰ همتی بسته شد. با این حال، صندوق‌های درآمد ثابت با خروج ۱.۱ همتی نقدینگی مواجه هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/655454" target="_blank">📅 14:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655453">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
شبکه اجتماعی لینکدین رفع فیلتر شد
🔹
شبکه اجتماعی لینکدین پس از بازگشایی تدریجی اینترنت بین‌الملل، بدون نیاز به فیلترشکن در دسترس کاربران ایرانی قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/655453" target="_blank">📅 14:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655452">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAzRqGSg54pz6K4vJ81aYvBjqwf8DeCnSsE4mLdIQUp5JSoBywstckF5lc5xskwNfSs25srzWQDWmNevPnCxJfsNvnBDndrusBBfkUj5jXx9WhGCOdeKKtj7TiwoLww7oOaHI-Sxou0GAQ1YC1b6ikZNig8ymkJhwYrp8kdlsxrjLtp-CKbl0xW1yCqeb0R1PrQgQa2xb_hjjJ8mnoXGeScv4-pvjlcBcbJUO8Y1yDoPJ71am4szke5fdSnyXyY9d7nkAwCIjARBbPd-sdr-Dwx0hFVRSFsNVx6JNXOt6IlaNerObLAYQ3Vt55ojUIhqJTqgL_gQRrzg_XVqiFbDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰۰ بازیکن برتر حاضر در جام جهانی از دید رسانه فاکس
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/655452" target="_blank">📅 14:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655451">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTD7wiSTNO7O2eZywLB1odL1tNbiOCJe_A5pSPpUiLJltN4aD9829KB5uJ4z4AeHtQxkok3gTS19s6F_O9bjjEkU0rZ0vcRMGGpTcKZ8ebsfnf8UvKWR2ESyeixw2HZb4mt1V0iOBY3FG1d1x6BF2YrX4c1Kk5x036-mCYuJEomjiqh8t2fyPgH_rmK4NNCaGsgC05kK2nnZEflgkUXyxt1Jx1o5BOPREM7P1zDKkC6siPBMmg3koRZg3YxkGKrwJxigniIpDU68yrdDHAFGStYjGlhFtlMqTP5j7K5iWSozJbYWQsbk4lxeSBsRLr_fJXOnPl5galIfymQouyc3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازدهی بازارها از زمان آغاز جنگ تا دهه اول خرداد
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/655451" target="_blank">📅 14:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655450">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
برنامۀ آموزش‌وپرورش برای برگزاری امتحانات نهایی
وزیر آموزش‌وپرورش:
🔹
برنامۀ ما این است که اگر بتوانیم مجوز بگیریم امتحانات نهایی را از ۱۳ تیر حضوری برگزار کنیم.
🔹
پایان امتحانات را به گونه‌ای طراحی کرده‌ایم که دانش‌آموزان برای کنکور یک ماه فرصت داشته باشند.
🔹
اگر نتوانیم آزمون نهایی را حضوری برگزاری کنیم، قطعا مجازی برگزار خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/655450" target="_blank">📅 14:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655449">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
سقف کارت‌به‌کارت بین‌بانکی به ۱۵ میلیون تومان افزایش یافت
بانک مرکزی:
🔹
سقف خرید با کارت بانکی ۴۰۰ میلیون تومان تعیین شد؛ در انتقال وجه غیرحضوری نیز سقف حساب‌های غیرتجاری به ۳۰۰ میلیون تومان و حساب‌های تجاری به یک میلیارد تومان رسید.
🔹
انتقال از طریق «پایا» و «ساتنا» همچنان تا سقف ۲۰۰ میلیون تومان انجام می‌شود و سقف برداشت نقدی از خودپردازها ۵۰۰ هزار تومان است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/655449" target="_blank">📅 14:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655448">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
عبور ۲۴ فروند کشتی پس از کسب مجوز با هماهنگی سپاه از تنگه هرمز در شبانه روز گذشته  سپاه پاسداران انقلاب اسلامی:
🔹
طی شبانه روز گذشته ۲۴ فروند کشتی پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/655448" target="_blank">📅 14:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655447">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
این خانواده‌ها به‌زودی ۳ برابر یارانه می‌گیرند
🔹
طبق مادۀ ۱۳ جوانی جمعیت که در سال ۱۴۰۰ تصویب شده، سازمان هدفمندسازی یارانه‌ها باید با حذف یارانه ۳ دهک درآمدی بالای جامعه، یارانۀ خانواده‌های دهک ۱ تا ۴ که حداقل ۳ فرزند دارند را ۳ برابر کند./ فارس
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/655447" target="_blank">📅 14:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655446">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7RhQTBWupeDtjTrJLdumcYDh2o1nhj9aPk7XBwFFCBKUMCncx8mNgcoKxHwQ3j33Fb9gvwUM4jFmuGbJ5FYEVSjO-ZuOtBJHvqvTwCE9Ekg_t7VfgS9E2_Hv77QH0R8leScmS2Yo8Q8PBIsQcTRsosdmetFMpHAohUX2ryDb01XD9QQm19cVOxeymf4K9fK8oSZZP0XkeYiTG7-WMWruD4Xt5hAMkeOrgnb6XQU3IWfS6KOzE7oj1wHFZ01UYS0AZYCD9k2I0DgEdZPPVO_R0Gm3YgMUEedgIBEdar3qgQWEwA-DNQSa9CgQffgo9NaI6okO5a_iGNNSbFGX198fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی تاریخی تقاضای طلا
🔹
تقاضای جهانی طلا در سه ماهه اول سال جاری با رشد ۲ درصدی حجمی به ۱۲۳۱ تن رسید؛ افزایش بی‌سابقه قیمت طلا، ارزش آن را ۷۴ درصد جهش داد و به رقم تاریخی ۱۹۳ میلیارد دلار رساند.
🔹
به گزارش شورای جهانی طلا، تقاضای سکه و شمش با ۴۲ درصد رشد، برای دومین بار رکورد زد و سرمایه‌گذاران آسیایی پیشتاز آن بودند.
🔹
خرید طلا توسط بانک‌های مرکزی و سرمایه‌گذاران نیز تحت تأثیر ریسک‌های ژئوپلیتیک و تورم بالا ادامه دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/655446" target="_blank">📅 14:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655444">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
مقتدی الصدر دستور انحلال سرایا السلام را صادر کرد
🔹
رهبر جریان صدر عراق، امروز دستور انحلال کامل سرایا السلام(گروه نظامی این جریان) و پیوستن آن به دولت و مسئول کل تشکیلات نظامی خبر داد.
🔹
بعد از انتخاب علی الزیدی بعنوان نخست وزیر عراق زمزمه‌های انحلال گروه‌های…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/655444" target="_blank">📅 14:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655441">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
اجاره پراید برای تاکسی آنلاین تا روزی ۸۰۰ هزار تومان رسید
🔹
با افزایش قیمت خودرو، بازار اجاره روزانه و ماهانه خودرو برای فعالیت در تاکسی‌های آنلاین داغ شده است.
🔹
در برخی آگهی‌ها، پراید با نرخ روزانه ۳۵۰ تا ۸۰۰ هزار تومان اجاره داده می‌شود؛ این اجاره‌ها معمولاً با شرط حداقل سه‌ماه، ودیعه ۲۰ میلیون تومانی و ارائه چک یا سفته ۷۰۰ میلیون تومانی همراه است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/655441" target="_blank">📅 14:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655440">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
تیزر قسمت پنجم از فصل چهارم
🔹
در این قسمت روایت اولین تجربه نزدیک به مرگ آقای محمدحسن تاج میری که به دلیل بیماری کرونا به کما رفتند و زمانی را میان مرگ و زندگی که از باز شدن پنجره‌ای رو به زیبایی تا مواجهه با خطاهای گذشته و اشتباهات دوران نوجوانی و داستانِ بخشش در تقابل با تهمت‌های سنگین که باعث روبه‌رو شدن با خداوند شدند را نظاره می کنید.
🔹
قسمت کامل این برنامه در ساعت ۲۰:۳٠ منتشر خواهد شد
#تجربه_گر
: محمدحسن تاج‌میری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/655440" target="_blank">📅 14:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655438">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f33160888.mp4?token=jFO9sP-rvYgu80TJyC3XDPW9Qajb9q24GJKII4w_zI_J0SVT1pn4oqW3yDtAUIxt45oF8nW0ytrCLeH1cC_OnC50yBRBDg8zSTHA3V5luzvHVDMilUKukygeKZE2Jlml7TLh-XYgxoTs9oZjsnlJmC8PVVCVcAt5XagUG9vLfwVQDY05KLrps_WpWkJk-MUxhRaUeJSMiynsnz_n7txCenZTfvD7Uwzvk1cTEY71CdCRf2ylEKSobJcKfM3aUgWgDxD-0DTuqkSZetV3Ow1CEhFGFTOc4ADKV8DM-hBd_m93sDncaxUAkyDjda3ZVspuMMsYhDZUD7qfQA3zejjMKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f33160888.mp4?token=jFO9sP-rvYgu80TJyC3XDPW9Qajb9q24GJKII4w_zI_J0SVT1pn4oqW3yDtAUIxt45oF8nW0ytrCLeH1cC_OnC50yBRBDg8zSTHA3V5luzvHVDMilUKukygeKZE2Jlml7TLh-XYgxoTs9oZjsnlJmC8PVVCVcAt5XagUG9vLfwVQDY05KLrps_WpWkJk-MUxhRaUeJSMiynsnz_n7txCenZTfvD7Uwzvk1cTEY71CdCRf2ylEKSobJcKfM3aUgWgDxD-0DTuqkSZetV3Ow1CEhFGFTOc4ADKV8DM-hBd_m93sDncaxUAkyDjda3ZVspuMMsYhDZUD7qfQA3zejjMKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازسازی ترانه اعتراضی باب دیلن در دنیای ماینکرفت
▶️
Reimagining Bob Dylan’s Protest Song in the World of Minecraft #ایران_من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/655438" target="_blank">📅 14:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655437">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPQJ3Gf-GvmPZnacvD0nVRPK4lP7_avPUaO9qy9YyjW5zb0yurcY1QRAL_pEIuaymdPhBUz-pH047U8_gmq-Rps_e9HADh4RgdXq6mLcpYOYDejn4esPIsiQc4BCdMM5ZnAc3jCFZMQYitEjWZn8NF4FlNX4LPfDh3OeolXfgplNL91fsyD3yj4EhQ0gQOwP8lcGo2BBN5X8m_d-yM25inwi_SZI3B15QoGxqK14mFwmdP4PGeQhmoMjdnA9S5OiqgIWqGm4rGCW7gy624pflTefE2poacA3h-K_9NGuwtwBEsM3XzRhdfFI2clHtWqhfTdr4HSa6FiM8-eQY5F_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌍
از مدارک مهم تا بسته‌های تجاری؛ ارسال بین‌المللی ساده‌تر از همیشه
PSP Express
با ارائه خدمات تخصصی حمل‌ونقل و پست بین‌المللی، این امکان را فراهم می‌کند تا مرسولات شما ایمن و قابل رهگیری به سراسر دنیا ارسال شوند.
فرقی ندارد قصد ارسال مدارک شخصی را داشته باشید یا نمونه کالا و بسته‌های تجاری؛ PSP Express مسیر ارسال را برای شما شفاف، سریع و قابل اعتماد می‌کند.
برخی از مهم‌ترین خدمات این شرکت عبارتند از:
✈️
پوشش گسترده مقاصد بین‌المللی
📦
ارسال انواع مرسولات مجاز
🔎
رهگیری لحظه‌ای در تمام مراحل
🤝
مشاوره تخصصی پیش از ارسال
برای مشاوره تخصصی در زمینه صادرات، واردات و حمل‌ونقل، از طریق راه‌های ارتباطی زیر با کارشناسان ما در ارتباط باشید
📞
🌐
www.pspexpress.com
☎️
+982142281
📱
09204228195
@psp_express
#پست_بین_المللی
#واردات
#واردات_از_چین
#واردات_کالا
#ترخیص_کالا
#حمل_و_نقل_بین_المللی
#لجستیک
#تجارت
#پی_اس_پی_اکسپرس
#ترخیص_کالا
#ترخیص_کار</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/655437" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655436">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
تیم ۱۶۳ رنکینگ فیفا حریف ایران پیش از جام جهانی!
🔹
تیم ملی فوتبال ایران که قرار بود در آخرین دیدار تدارکاتی خود در آمریکا به مصاف پورتوریکو برود، اکنون حریفش تغییر کرده و باید به مصاف تیم گرنادا (رنک ۱۶۳ فیفا) برود.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/655436" target="_blank">📅 13:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655435">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c50c3bba4.mp4?token=bVByfXABglwGRmIxGNj68onu5e_NMZ5rTjyDIPBookhnWQuj2-TnrvMz-UZdliQx6gAXa7exXVCog1jjqiR6cES1pYEYcN9G-43NM2RUeEUwXIntjSaBzHfxjtYw_ZP8aovdiKeoqwQw5Wp5ywmF7Mrg37VwE06irbWX4TPURRdby5yGZU_rTvDGvDubNmsUwl2JvnfvmIfAoz_n6ib1_XXKx59xIaVooIInf93K7TQT7C0-19KnJSFzBJS-8xkQau4VEc7E98clfkpv_40eA4m74bSqbBopi0NbHTJW3ESvwpZLeP_CgMmld4R4NZvELVltsGUKbE3RLUkSbFiebmQIMXkxConRucmL_xGOMcbVrMZpW3IVkgha5Noe5A9v9FLKaUFs3QGUWEkemzeNi6JFcyVbeeExmZ8nlOekhN1AmKJiqkVRAJQwg5IMgdgFvvT4ZW8VLw-8yXq1YmNSzRGWIe-8_7Ty-oom5ePMe8diLzVF5p8u_9dH9cVVOfofTXiqtslq5eXmYM5QFF6oV_PmttQbCmjAIKVRAZO4OqlQK4OR6FPrVq05kzka8dwzhAIU5PAGinEj1p9sWLH532b7rqbVVNHok3kLEeoRqg3Jrf_uv0uKg2asNFdQmTfrXnCiPiqrx7s-emdEgaEC26BTLfbsuaIoucHTgdyN_qc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c50c3bba4.mp4?token=bVByfXABglwGRmIxGNj68onu5e_NMZ5rTjyDIPBookhnWQuj2-TnrvMz-UZdliQx6gAXa7exXVCog1jjqiR6cES1pYEYcN9G-43NM2RUeEUwXIntjSaBzHfxjtYw_ZP8aovdiKeoqwQw5Wp5ywmF7Mrg37VwE06irbWX4TPURRdby5yGZU_rTvDGvDubNmsUwl2JvnfvmIfAoz_n6ib1_XXKx59xIaVooIInf93K7TQT7C0-19KnJSFzBJS-8xkQau4VEc7E98clfkpv_40eA4m74bSqbBopi0NbHTJW3ESvwpZLeP_CgMmld4R4NZvELVltsGUKbE3RLUkSbFiebmQIMXkxConRucmL_xGOMcbVrMZpW3IVkgha5Noe5A9v9FLKaUFs3QGUWEkemzeNi6JFcyVbeeExmZ8nlOekhN1AmKJiqkVRAJQwg5IMgdgFvvT4ZW8VLw-8yXq1YmNSzRGWIe-8_7Ty-oom5ePMe8diLzVF5p8u_9dH9cVVOfofTXiqtslq5eXmYM5QFF6oV_PmttQbCmjAIKVRAZO4OqlQK4OR6FPrVq05kzka8dwzhAIU5PAGinEj1p9sWLH532b7rqbVVNHok3kLEeoRqg3Jrf_uv0uKg2asNFdQmTfrXnCiPiqrx7s-emdEgaEC26BTLfbsuaIoucHTgdyN_qc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف عجیب در اورست؛ چادرها و کمپ‌های ناشناس و رهاشده، منظره‌ای شبیه «شهر ارواح» ساخته‌اند
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/655435" target="_blank">📅 13:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655434">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eflRo3pCP48PdR_8hngqmvr2Glq77zikP1Pd13V_aLhNEw5bclP6qhX-RDm8F1qkzPS8UbnUv9vr-f5SMDvy8Pb-iUYHTi39TVnzeIAVEJm3nqKfc3tA72V9Uoc93pFRfNbntu6Vq_EJYO2tTWhJ2yyrNqCf5n9XRoL4tZBA7RUd9u4GjkHcDrPutcrNqMHja9aj-BVZeJrqCzkTN9M8lX86xSeupKu9PEzb939nnzFQ-z2JLxF4M0yMQZN5t4Jw9qAdjOc5lia_fmrCDZM4DRCwWUDwoDeNpePMYq_wwcfSskQQchUsXy-z7l8W3BBjRPFtXSf3U7GyZeUmB0Tj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس همچنان در مسیر صعود
🔹
در جریان معاملات امروز شاخص کل بورس با افزایش ۴۴ هزار و ۴۱۶ واحد در سطح ۴ میلیون و ۳۴۴ هزار واحدی ایستاد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/655434" target="_blank">📅 13:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655432">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT70_5RWgiUYwy5EUcC7_WtR0m8bz4JQ3rUa2T7n2p7JZMnZKqowwyf-Qm0dR8PXwQenrwCoPGM6J5wD0ENyS5mJ7VkyII9z_BVxqv5pQMD1FzoQqHUSMciesKwa4jeA1dYJwwNFjI-R4A21DerP6Q3TjCBM0MPMqcjV76Gy7jElIocMB_gW-DBblv-80hWNd8Mh7BleXtyATB3WBSvb8vc2BhNuzCar9Vana3uDwJ-SRLgbvlEFGQT8FxNaZTukp8UWUym8PBs70f4ZvYw6JOQaM3aWgSP6k5RORsqCJBZzF6pikiC6Dv50EC77F2v57weTNtcJFE07rAfyJEmBjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر اقلیت سنا از کنگره خواست جلوی ترامپ را بگیرد
🔹
چاک شومر، رهبر اقلیت سنای آمریکا، خواستار رأی‌گیری کنگره برای مهار اقدام نظامی احتمالی علیه ایران شد.
🔹
او در سخنرانی خود در سنا، مدیریت دولت ترامپ در قبال ایران را به شدت نقد کرد. دموکرات‌ها برای بازگرداندن اقتدار کنگره در تصمیم‌گیری درباره جنگ و صلح، فشارها را ادامه خواهند داد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/655432" target="_blank">📅 13:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655431">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای واشنگتن پست به نقل از منابع: مقامات نظامی ایالات متحده در چندین قاره، سطح حفاظت را در انتظار بازگشت به جنگ افزایش داده‌اند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/655431" target="_blank">📅 13:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655430">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
اسپانیا: در هیچ اقدامی که تنش با ایران را افزایش دهد شرکت نمی‌کنیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/655430" target="_blank">📅 13:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655429">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioMzcNqmVv_nsWMZS8W8JqxtfRzi6CiYz0uQ93DZ-H7hUwax7_yjQsaEPYv3yNta2t7KSdoEEHFLp48uw-wbxsOa7ehyiXTEyXIbczies2Bf9DQSf5idirjRyHGc5Nlq0PR5QdmNRLgNCnA8SleXvvJgBXDHXyfeEQM4HWo767gHjwjBcBXpuEs4w2LKO9UuuDcXG5JkVFJSsphlx_UuabbY-fu4hpJXMMQxgS9Yuv3pc8tKc1JytIpOL59Jezx5EgHwxPPE5KPR91mPUazXHWcr3LG5pm4Et01XNMCItbgnRhRHukEMkL0ICmbfZakFtsfd2DIZFaiTSfwAckW76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانگین سنی تیم ملی ایران در جام‌های جهانی
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/655429" target="_blank">📅 13:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655428">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef7a3d1bc9.mp4?token=Z92M5U1uAg_4EAJSm68X6GEsArGJ4ho_HwkJGC82xZ5zzC8C51OvOqq0LI3J4J3WFbH7TqH32kSej6vHQsVl8XkEU9tp8rm4ghIQvX8wGawz_gU-ZCt7TjDsFrzr1sgeWYiYRjPc4_aOH6389On-XiJ9kTK83aHV56lmkdjHLIvBkXLINr40Rk-ggi6xo9P_k6-NeY-6SYKsoHIn2LqcDxGJdfeqlLkT4zFfayxv4uI-5yeFeFRgCwkYFtTXtaOUH0e9wZtORNV7FAfJWwlUls_B3dwd5S2U1O9LWLzcbz4W0qiky2GwyUm99sjJlhcFOI_IUlLjX4SMLtl9i6cZ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef7a3d1bc9.mp4?token=Z92M5U1uAg_4EAJSm68X6GEsArGJ4ho_HwkJGC82xZ5zzC8C51OvOqq0LI3J4J3WFbH7TqH32kSej6vHQsVl8XkEU9tp8rm4ghIQvX8wGawz_gU-ZCt7TjDsFrzr1sgeWYiYRjPc4_aOH6389On-XiJ9kTK83aHV56lmkdjHLIvBkXLINr40Rk-ggi6xo9P_k6-NeY-6SYKsoHIn2LqcDxGJdfeqlLkT4zFfayxv4uI-5yeFeFRgCwkYFtTXtaOUH0e9wZtORNV7FAfJWwlUls_B3dwd5S2U1O9LWLzcbz4W0qiky2GwyUm99sjJlhcFOI_IUlLjX4SMLtl9i6cZ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری مشهور آمریکایی: ۱۶ میلیارد دلار به اسرائیل می‌دهیم در حالی که مردم پول خواروبار و بنزین ندارند
مگان کلی، مجری مشهور آمریکایی:
🔹
آن‌ها (آمریکایی‌ها) توانایی خرید خواروبار را ندارند، توانایی پرداخت قیمت بنزین را ندارند، توانایی خرید خانه را ندارند، توانایی پرداخت هزینه درمان را ندارند، و ما ۱۶.۲ میلیارد دلار فقط برای یکی از همین ردیف‌های بودجه به اسرائیل می‌دهیم.
🔹
آن‌هم در کنار هزینه‌ای که برای جنگ اسرائیل علیه ایران کرده‌ایم، جنگی که هیچ کس نمی‌خواهد. هیچ کس.
🔹
در عوض به مردم خودمان کمک نمی‌کنیم. آن مصرف‌کنندگان یارانه‌بگیر بیمه «اوباماکر» متضرر خواهند شد، چون ما اولویت‌های دیگری داریم؛ این واقعاً خشم‌آور است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/655428" target="_blank">📅 13:11 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
