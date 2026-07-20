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
<img src="https://cdn4.telesco.pe/file/MDIU6T8CK08QS04VHiR5X31iLq652x4LxbOPRMTq2RpjQ8rYVUxvH0nxcZm0QfxnUVU6QXEoSjuYm9z458MmBPkq8kfIHuKq3Qx4O7qO-IaLA4mPovXLlff4O6fPLfWsQ7zpuF98vuTSE0Vekbhh-J4-iY2YY4A-UCXvKXLxa_pP6YUpeA5XhzyvBhTM36cfIsGOE4EVDc_GptHDjS3vTQE1xDWD-S04YwqeYMsqgqXkTVFrOhBMn0B3IHuJmdg2C5_ZNFTwuWsx-p8xbc7Taj7Rr4urrtHUzQVlY7uTJBEv9xmA_iDzVtRJYJKWXbvH4cucHoLRK-qGbpxR-AuVQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 14:49:00</div>
<hr>

<div class="tg-post" id="msg-451393">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a54248017.mp4?token=fu8Tob3Zhg47uPUIgOXohgaob0bQkZYS5yJyix8-j_GdYkHPg01jUdD9HEZSEmkdS2OP6QLzW8xJ5v8S2HCW0hHJdwJCLubvUPmOfqoqx8Rle9oOjt6OPG0nqnIoTOdgoi9KzHeTgm5gGs9_cJUQQM7bZsVS8g2RRCW3d6PlHSiLBQ913OfRriIFLGwcVXSg7m6Gz1_4msawVEPUe8I-GGzhRNDjEtIqDgDhPiRd_w8aiwvaVj5B-32vUQIljQuYpunD5G0rexgxx294anyLW04m36e6mv6Y200ZF_OzV6gtJGqQu2ALmpHhPeFPA3vtWpDZdSKXu70DLnX5s5QlTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a54248017.mp4?token=fu8Tob3Zhg47uPUIgOXohgaob0bQkZYS5yJyix8-j_GdYkHPg01jUdD9HEZSEmkdS2OP6QLzW8xJ5v8S2HCW0hHJdwJCLubvUPmOfqoqx8Rle9oOjt6OPG0nqnIoTOdgoi9KzHeTgm5gGs9_cJUQQM7bZsVS8g2RRCW3d6PlHSiLBQ913OfRriIFLGwcVXSg7m6Gz1_4msawVEPUe8I-GGzhRNDjEtIqDgDhPiRd_w8aiwvaVj5B-32vUQIljQuYpunD5G0rexgxx294anyLW04m36e6mv6Y200ZF_OzV6gtJGqQu2ALmpHhPeFPA3vtWpDZdSKXu70DLnX5s5QlTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربات کوبندۀ موشک‌های ایرانی به پایگاه‌ها و منافع آمریکا در منطقه
@Farsna</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/farsna/451393" target="_blank">📅 14:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451392">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSS9Awd314S-fq8WQwW5JlIHQ9FLI9dbCqi5waPynDMRnhoagSxs6iVo9c6slfByp1lp50ZBIYnns1M4RXu70p1ubePbSH_c7JJShKFwI7XnrXzTCen1ZDJ7NAXcXtt2lQPfY7QXCw0q9mbIgM3jm9_XEQxEC3w1aIY7sXTbZJ5-zpEToJFNYXUrza-M0hUZtGlvr1LKCiZP5FmOAkb6D1qgGnn4FJZGf-r_g3_dsk4rnqG2M0MZtgrAf74oVW9b0i7gfqcONLQsioZR7Ul9iIU1VteXfHFlwFdsK4Sn-QTPzRo6tQ3DPqi8G6wio479OrnsvKzFnxxapOls2nI7wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خليل الحيه رئیس‌دفتر سیاسی حماس شد
🔹
جنبش مقاومت اسلامی حماس از انتخاب خلیل الحیه به‌عنوان رئیس‌دفتر سیاسی این جنبش (عالی‌ترین مقام) و جانشین شهید یحیی السنوار خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farsna/451392" target="_blank">📅 14:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451391">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
قالیباف: آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگ‌اند
🔹
آمریکایی‌ها روی هوش ما اندازهٔ آی‌کیوی مختصر خودشان حساب کرده‌اند.
🔹
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@Farsna</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/farsna/451391" target="_blank">📅 14:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451384">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4imlSh_OKpuvOF2bMnCJGSKCLhSkwRzPaGuSaAIyywHyJgDUW0s1aOE3uZjpcBa3sR2ekyaAO-cyS8C31f6IoApnrVPzWnraH1NtLeJqS8OE_ZiG4OTAENlY_ZI2DeFisIq2HKpGXCAoWYFjjAteqgeYYddA7RlBeXAvrK79fgMm6Z5ySzXAgA4B3avmBZtZBB1K6WbPzjjt_ZZsO0AdhJBK66e6cMoFD0GpYU7aEcjIp4uTz7UmwhdkHwRnAXPfUxYZzTD2c_nbQnoaFcvDLGH-rYHE-Rsd7TOAtJpYUjI93m9Ho8Ws8U4GdSsNbKlieX9xec37G4yClbKRtADJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPgyeav9pyH_FnPf36zPUC7-GDOcK5SC6vOd35YDo-5TXLbloGyv6N_JFsibaAPaXPLg3nS6RHRaV9Ey5M9txT9TP52TJ-HfKIvuyukDKSN5wZ1znZEK9bNLou1JODwyFxFmaFXnazfGBaPEqlinGdyYDzJaS1IUbjVeAXZK4CaoQnahDhAO162ggMg_R4R4XHwodkmiz7uqon1IZFgsh5xIfIhSsa8xHr1A65M3LfcjbsjKXWkfnReOtKUOFGfev0XrhGpWy9P12h1Vb3R47R6zrk0sJKlPQAZKuI0yJ87RSzMjF5Utq9Kt7gUCq5QzBdb0TCF2sLiSQgoTu4sHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9AvmKaFRSKyiCIFLRLooYcjT0CmOzfPhb0jkWidjrwhWlbDLLUtrgZ9zWfFzCEkofEkn32i7cINFZdRh7SFRtSTfudNxQebhs6JukCEkLAHSIfSzAdptIWlODongaKve5BU63Oh75HaznaTYH4eKjtfAdNtoCYY3FSfJ-EaNdGY1ihpX7dHYblqBlywcxZbK8ll7S2PKe9W94zN1J3GtI3rNnOSq4EIWnGi1Cb9RbOWG6naYuxCiIO_-vBd2MBJUJWZMsoZIJhbrnHw8R-h5DvX3OW21yp-gG6tjQSh-uD4IB-CyaA6am13i1of9n7nvoZZ4E3kOL7FIzEd0rTmlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrzyybA3Xhh0ARbZmDKYIrEfy5JoqFZTIhRBXEY_cIuSp11kWJfhIpz6buts9x37kLz-U7sBLgLjihLNtoRNkm8HtNqPwz7WzhFAEspkPndQDofvbB4x8fmNO55M13pnZVBnElhlaPM57Tu4deIiItKG76sChW5H-ak-gQRwSyOnW2ZSM0_R60zoqdeu6SNjD_GJH7zWYSQaY9W68WlMSxsMk2L0cHPu5sJWDJXi8DZ6tPrpoUwEzE5NnDJxOfwKXgz4VjLAd8fVlNxJzKVf__iLcHm7-6XpN2GoJiR8hUrTejOJElle9vMWz6aH_bEg7GctpYqoK5fY8HyE3SRQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lR_4NHtYBSeKMnw3SJJ-8faQhftpcGTkifZLyARq15OkrDl72TJYMCgyNeSgPA5LpC6z_FIvK5FewWgOGzulJTowc0B_8BCqcJ4G6Cam5pC-4HRfDvRs2Cbx-vO5QQZXXOVW5ceFnI5OEjxhfPByi94KScQYc1Wcp7L5R_-z3k7LXoYS5X8HrndHjdVPnGiiTNNNsF1TYglV35EZw1BdZw_zJyz_jsMT7R0JvxKTl8tqwnRZH9pYrMKN0kZpFBTUL9cdHl-TUAyCkaZQsRnI7DBj-JPJDHTnRBe6me1VZOApxo4gxVB_cqPoiGTXk8XaFGHQb8w-IG1qLEFWOqhfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBxQe_aHkQDwBgikJSgv9tnUnRz2r5GrGblDm0ugI3_LI7vok0VpVZUK8R8gQlI302LNvetyEnjWRxoNEfwUvWLXhNeqOQWycurV402CtBUXkaLZTQMX58b4-1MEypIdIoUVYNlkiVffrLaak8gQ8Mwo3fpHT7e7y-CeC8PVWAu1pfzZaA3xM0VIRgUOZ_TBOhSqobsFL-sJ2JxQ4Ub9K8Y_ogB2wI06nERzZLyKfI0YT1lNvdEwWc90v0iW0NYOmDypwyt1eTC5cZUrkNscQrKyNPpewzqj5nl68DYm-VhWfyxjMrvQfM5XyGPNTP-X7FfkL97hqTsGwXr6IYSanQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qG9X48JdAWFU_bqwnATZcmVSkZBgD5c_AFHxp51gUwVMJmxDsZoj_SJAaDNsIJTPkhPO73LiiRfZMN8BfbY3pyfFIyjLZQmcH9KMiuGZozQ6XVN8uOAkZBtew67GI2K8HRTHu0nCWUr8xd4TgBXlHoF_EDX_UsTVc3eKxWW86zAazHFDSlnyijq-pVBLs8p8zILdoiIbHFuj-oW6r82EnVZAWiLsgjZojCxzIe3H-cnIDokzBeNCThULhdDR1FXZ1NHxe7Qt0UV0StSNDaurEUSlmg_gEWjYdDt2Pa3M0hEQM4KJJtE2CyW91ih7hH3Mg_QehnZh_7P-rD51_JkHIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
درمان موفق تومور مغزی بدخیم
عکس:
زینب حمزه‌لویی
@farsimages</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/farsna/451384" target="_blank">📅 14:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451383">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tm4PWGNS5cWv_o5aQgskia0fBhiX06BEuZ-jy26isG527_e83UbkXaZuy65CcBaQPzKHNCNFQoomf3VFWNHgyM6Wtyxn6j-pr5zypSu5T57mgv0xiz4A4KJJD1oVp8gnXLzCf-xErOWV2IhMxMLRp2C7RUqgjewysQIvfWwtCCaQ6hAyB2zvMEw5cKWUy_VLFiTRh6AjMlu2GOf_y_Xt7MpPmb6Rbi7vr2ig1e0oAo51wD8dggQit1hFnxC-xKKj3vSDVbraggFDmBdkx_r4FU-KxQFsRurEAAMhliqhL93aSSoNtMYoK-h9maEXblu7WnqIryUUwIbeT3TPOFC0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پزشکیان: همۀ ارکان حاکمیت باید از سیاست‌های کلان کشور پشتیبانی کنند
🔹
تصمیمات و سیاست‌هایی که اتخاذ می‌شود باید به گونه‌ای باشد که حمایت و همراهی همه ارکان حاکمیت را به همراه داشته باشد، زیرا در صورت فقدان این هماهنگی، نه‌تنها دولت بلکه کل نظام با دشواری…</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/451383" target="_blank">📅 14:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451382">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پزشکیان: مهم‌ترین میدان نبرد امروز، عرصه اقتصاد و معیشت مردم است
🔹
واقعیت این است که امروز ایران درگیر یک جنگ تمام‌عیار است. جنگ امروز صرفاً جنگ موشک‌ها نیست؛ دشمن به این نتیجه رسیده که با حملات نظامی نمی‌تواند ملت ایران را به تسلیم وادارد.
🔹
در میدان نظامی،…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/451382" target="_blank">📅 14:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451376">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNKB3vNEX26BNbPfOEDn1CW3M4LpqoubnLjX-q2OEf0qffCSh_nrdAKz1fq0Qkm5j1EPg1MAz74LtZHfneVgmS0SDrQgLIj3w0gELkekPJBP3Ke8Ry-ZynHcZlksg-RW91dPi1I_mlSSUnwkm1R1m_x2ohOKeA3dv4jG9n9ykTgE0qcImGbr5i5hFWynRwWjxZtc_0WCDopUfbXQuCWDSUApxTmFZtAPFllh-FX1sSENpg9IFGjcY6O94aDG2V1BBrnxtzExH4y3XNSR1pR2FC_O3i2bfBo8gHO5LQGvuKfzWq8UUbBizjA0gUYLYEyMq3uyPdQLSKbVzISgLGG7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGhE_BDFnlZYLqtEI_gfqG4X8wH5GU9RKfbQCE8lOXV451AlegJzzlpx7P_MkbSxHCm4Eq_RFhWDApD4XLFZOBo-92L1PzhxafEYFY4fTGJJJT_PIOmANaBcr6j2clxlorB1wp5gtb65IYr1yJjMNaP4Suf-WqtPsES7JTFUn643nismnG9SXf60Ra9UWRtgahuu884kg95k4C9_I_jS8szUpuE7pf5RyBHe_WOoi4vY0SlNCCEXpi7Rwl6iKGJpn5egk5RzKIPXvVp-Zhtw9rFoHuKsyq8TpfkRuJT79EDe4flyjPQGxln8pP_E-pqR4gmlch2QeDNu7JBHVDaayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJ3NDdk7mG9DJ5R-tgzZ8cb10oQX8-5o702F7prSfmmQSx3oV1-HPKY5dVB-bETpZsgA5bDcNUv9CFhjgS34SWTnGxtqTR9fPLiIyO7o_ltFgRNeX3lJ2GkGNGjEZLWctVLTOjyEZPR3Y5LPoWh1RBpJUWAEZ9mALRCVVT0dN52sy8N3q2di9bdt3802cMjkQ1EQhby892dx5idykQtUThikJCh54nvg1wayJDhRmqVrb9SvmV3pB-2lzoJM29xzrGkT0d-zoM3o2H0wion6NVAkbCF8v39Yu-9y-u8M0hapl76Is0xhIp-4-PjlDMIgx33N_ByMVeJGvD9BdMneuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuWMBecf_po9IVLbPZNHS6cx_1xvbpInWlWxYfCgPSiwf4bKrm3rh1J2aA5xafNUmXj0BYju0P4adRf6n_607L6Xv1GKFIV9wWoZXOeE5930HrcNeF6qckcIWQEfbCXqfl5vdpDSnA6aqzBpuZKVBANfA1jtiXbLQQz7s4nOL0A0-5D1CX4XaGxHXI9z6A53r2VVeN9rsSu9z0WkiXHe_0GcvXStWH443V7g7s1qbHTNMaH-zAcezamsSEUn81GIk0_Ul9GzxlJETm9Yrx7fzFKjopfeZEN_hyyWq_eN8zeFaqFuqu11SJhbm8k5AFX1Y-SMSi8g-O-DF_6HobqOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_gytnKD_yoGpoG4r6fCi-ZzHGfPMa81Lg03t79A6DCwJBvsKWJs56UvNT8gu6-c6g6m1q7aOBuvDwkRuMNdoqcgJOMm8yaxlQIoQWdF6wuiPjzJt_R8ZdcAvJTYUCZyLjpLOcke7f5QW7-rzI-bx669dfHQR5FfEX_bE2ta15JG2fKKZx1ydrTRpuvcsHpJEa8Cc2E_i1Dw1WxEqckzLgCHx_ntKgCRaMqtco6ZJS3pj-RJdyxH5XEeNS0knvPUT4q23bCbm8Y-NrcFfjB5-Y4-R39KNEtr3p6YP0RqulYiG-yaM-tIRwwzwJKxP6S9j7juKSav-MGdSEw-eV29eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZTNu_gnNG4ED7PLhLGs1gEr8nDXDuMvzV3-ZqdVMXjhEjyeT1IqWQ1teUsIfXJ726zMWTnjKIWDSCACt50ZMq9iaSlmyZPAaDgEjXGaFP57vxmVVZbordIyhNFI90W-sYPKPpDCGYWpbyof5vmSL2EKb0uGx-we7CzYgr_voJRAcEvWNPBxeQ5j-Xpg-NI4dmaeYlqn-R6yTON__dhT0uGEgL832DamBekiTId_3-wUoNJdMXcu9SxK5KO19Kn8Aue6XRIdqfGjVCTBejpvdIL9HVvVlz1PpnGm-Z6C5BRgye0KQIH-plUY8e8wyMrQhEO2joSaJIYuH8aO5cSV3sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر جدید از خسارات ایران به دارایی‌های آمریکا در منطقه
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/farsna/451376" target="_blank">📅 14:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451375">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پزشکیان: مهم‌ترین میدان نبرد امروز، عرصه اقتصاد و معیشت مردم است
🔹
واقعیت این است که امروز ایران درگیر یک جنگ تمام‌عیار است. جنگ امروز صرفاً جنگ موشک‌ها نیست؛ دشمن به این نتیجه رسیده که با حملات نظامی نمی‌تواند ملت ایران را به تسلیم وادارد.
🔹
در میدان نظامی، نیروهای مسلح با اقتدار از کشور دفاع می‌کنند، اما اگر فشارهای اقتصادی موجب شکل‌گیری نارضایتی‌های اجتماعی شود و این نارضایتی‌ها گسترش یابد، سرمایه عظیم اجتماعی که مردم در حمایت از نظام ایجاد کرده‌اند، ممکن است آسیب ببیند.
@Farsna</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/451375" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451374">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52f4bb1e8.mp4?token=XwK2domPm6xmqIk428pJcDPWxLjT3BLS_KEz10hsmYyvuXKDIMTkv2Oh5qBTCtSVREdcBt_IA3LSaETz-nj_0YrqM5pevKRHmU_hS3q1e6eYf1Jrdj2yb2sbnNP6Q68ueqg8aEQGmoZM2Nai9PJzWQZrEMZ2XdJURgsx3PGe1YeO4I4IqXmtRdK46nOHMPRETMiQFR_59Rv4DSx-II9bDzp_nBi-ZZUBL2VanKJQxYnAJnIrZN3ZTCcGLRmPJsKQLfwR1pV3gZF4o2pTPunZ8OMkOlGuqwsPAjlm8PNv515VMV2sO1vDVTF3NJlun40ebpbxHuRX8jlFJTkabhsbcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52f4bb1e8.mp4?token=XwK2domPm6xmqIk428pJcDPWxLjT3BLS_KEz10hsmYyvuXKDIMTkv2Oh5qBTCtSVREdcBt_IA3LSaETz-nj_0YrqM5pevKRHmU_hS3q1e6eYf1Jrdj2yb2sbnNP6Q68ueqg8aEQGmoZM2Nai9PJzWQZrEMZ2XdJURgsx3PGe1YeO4I4IqXmtRdK46nOHMPRETMiQFR_59Rv4DSx-II9bDzp_nBi-ZZUBL2VanKJQxYnAJnIrZN3ZTCcGLRmPJsKQLfwR1pV3gZF4o2pTPunZ8OMkOlGuqwsPAjlm8PNv515VMV2sO1vDVTF3NJlun40ebpbxHuRX8jlFJTkabhsbcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بانک مرکزی: بخشی از افزایش نقدینگی در ماه‌های اخیر ناشی از افزایش ذخایر ارزی کشور است و این به معنای «نقدینگی باکیفیت» است
🔹
سیاست‌گذار برای افزایش تاب‌آوری اقتصادی کشور برنامه‌های متنوعی در دستورکار دارد و کالاهای اساسی و نیازهای مردم تأمین می‌شود.…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/451374" target="_blank">📅 13:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451373">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70933c45cc.mp4?token=a5HNlSfigkxebeHQc2okBcuu5SYIvR6z2wafoyEPdWjcApQDjFnkBcy0_dD1KbBhIfcqBen14Bg48bwQC77Su2ToULOiSUEBK9mszA21kF15XCCj2l2cpViPT3K7bJ-LqkQ9-QS-0nLzNLmOGuiPN51_RNPA-w9LEKTEUACfbigmUBtfmxUxH7bMm-Hjb2PqgLbbxICOfZ97R2iOsdv4GD1FJW5_qcfrQ3cdka2bLGl3VD6AH48uf5vOgS76GfWUdKIdvxZF6KKnt2Ti06YiwmhHX2xIrukAgX934Zl3tBvE4BrSRcKCiu39nnV1UbKVunqKGfzLuwTjp1-HajJFQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70933c45cc.mp4?token=a5HNlSfigkxebeHQc2okBcuu5SYIvR6z2wafoyEPdWjcApQDjFnkBcy0_dD1KbBhIfcqBen14Bg48bwQC77Su2ToULOiSUEBK9mszA21kF15XCCj2l2cpViPT3K7bJ-LqkQ9-QS-0nLzNLmOGuiPN51_RNPA-w9LEKTEUACfbigmUBtfmxUxH7bMm-Hjb2PqgLbbxICOfZ97R2iOsdv4GD1FJW5_qcfrQ3cdka2bLGl3VD6AH48uf5vOgS76GfWUdKIdvxZF6KKnt2Ti06YiwmhHX2xIrukAgX934Zl3tBvE4BrSRcKCiu39nnV1UbKVunqKGfzLuwTjp1-HajJFQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بانک مرکزی: ادامۀ فعالیت بانک‌های ناسالم و ناتراز را تحمل نمی‌کنیم
🔹
مهم‌ترین ماموریتی که برای همکارانم در بانک مرکزی تعریف کردم، کنترل ناترازی بانک‌هاست. @Farsna</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/451373" target="_blank">📅 13:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451372">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c95d9957.mp4?token=DqnVTzGzck8dJYoY9JrvSfPnOD93UTZAwFFtj891EWgimQvA0gU8cXqc71t9tlaOr_Ykrsqi14YYIMRqcJ8j3Vr9gQDwGOjz0zAkKjdzqfeqVOpdWjA_d_Skv9ZZpZjfj2Ic6qXRlQmx213mcWfTSuwktkyQ-Zgb0f50YfZDhQ4qyzA6ui7Um3L9A1516cNrup6wveQO_Szbah_DHmp3vUB4lh4pxjbo17wJy1iR7C2MnOCQlnVgxnCdz3VHMaCzQ2pLwL0_pi_nrebdMn8H7XLwiEdX9XAa_2Rv4NxXtisvN9AmCkKRJYVWpjnAK2d65tNw3gG0L7OqMrCo2w4Eag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c95d9957.mp4?token=DqnVTzGzck8dJYoY9JrvSfPnOD93UTZAwFFtj891EWgimQvA0gU8cXqc71t9tlaOr_Ykrsqi14YYIMRqcJ8j3Vr9gQDwGOjz0zAkKjdzqfeqVOpdWjA_d_Skv9ZZpZjfj2Ic6qXRlQmx213mcWfTSuwktkyQ-Zgb0f50YfZDhQ4qyzA6ui7Um3L9A1516cNrup6wveQO_Szbah_DHmp3vUB4lh4pxjbo17wJy1iR7C2MnOCQlnVgxnCdz3VHMaCzQ2pLwL0_pi_nrebdMn8H7XLwiEdX9XAa_2Rv4NxXtisvN9AmCkKRJYVWpjnAK2d65tNw3gG0L7OqMrCo2w4Eag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: بانک مرکزی منشأ تحریم، جنگ یا کاهش درآمدهای خارجی نیست اما این بانک مسئولیت دارد از تبدیل این شوک‌ها به بی‌ثباتی پایدار جلوگیری کند.  @Farsna</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/451372" target="_blank">📅 13:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451371">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c90d5c5af.mp4?token=oM6wNMAtu1ey2EVAnJsQ1IJSBYzbjm8mTPuSGp1AxAHuexcdZSfLNMCBlDQ6R2cgGm1BeUVkpZcHPgw-utswb_dZR8B9v3WB7GelaaWdKmR9hj3FwhfSmk73nxvLxClEvI7HFh9puHsBKTH-a707kUEiiUNabb-a_mRatz5V0Z-0XEhXSqBvIlLASRKKhoC0G57JRUrbhFCgeW24hJVzOC2LoNnMdmhwAEi8VcOjaX1gPnNAQz_dJh46jRQ6ah4ARCyeWW0CPkNxoU94KYnMnXFpBnDvJ2WLHLK-ZBtaLgERN7ziweY0v_zNfXELYeoWQYV8hj2b3Cmw885vP77TCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c90d5c5af.mp4?token=oM6wNMAtu1ey2EVAnJsQ1IJSBYzbjm8mTPuSGp1AxAHuexcdZSfLNMCBlDQ6R2cgGm1BeUVkpZcHPgw-utswb_dZR8B9v3WB7GelaaWdKmR9hj3FwhfSmk73nxvLxClEvI7HFh9puHsBKTH-a707kUEiiUNabb-a_mRatz5V0Z-0XEhXSqBvIlLASRKKhoC0G57JRUrbhFCgeW24hJVzOC2LoNnMdmhwAEi8VcOjaX1gPnNAQz_dJh46jRQ6ah4ARCyeWW0CPkNxoU94KYnMnXFpBnDvJ2WLHLK-ZBtaLgERN7ziweY0v_zNfXELYeoWQYV8hj2b3Cmw885vP77TCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: بانک مرکزی منشأ تحریم، جنگ یا کاهش درآمدهای خارجی نیست اما این بانک مسئولیت دارد از تبدیل این شوک‌ها به بی‌ثباتی پایدار جلوگیری کند.
@Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/451371" target="_blank">📅 13:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451369">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjTLUH1_cGsdG1jz_SzzKI91pHAohS-f5fxjAstgIk_EI_TMfUfdldRpldWWQOReZhFyGDvjs8G7bXY09AP4IJsc3LEtbZwye7Q1faHv1ZyhqFBILhI7RKlZY8VEMRIXgGULNT0veU5R64wG0HFjFyyuOdODapdeV8RGk8bsuWAANIeBhvw9edAxb2bQReKa7NfiFaMgH_idEIBn0qB1_uHPC6sCi4lTph9ZKcb0Fc0ljweorwergSXE2fA74gGvbwEH5gZPeFi3icsWG86hDc7KZdnbGVy5SwxX6XkXlqGTaM6YtATq-xsIPtEmisgUG5wnzak8Hbbp82zJWOv1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LayDOjZ_irQCgMsbDsH-4_sT_wQhgFT0pCRTD0SlcRqLHkLUbMb5vi1HhYoE_vhV__lpcDW1KKFY0ThDZSsqUuqasFge8oHZXNyajB00kV5XvypetTbgNMbdJGEtwvI4gmkmn3i0VGTwVTm46LYLB4nlcStmEWc2mUh7f8Dcnnom8RXsEOM4_YzgpYwxfgX6PtpcwqREp-PPabWqEh-CUxJjjQfYC5Ya1MtShEMDPT2X2D_0VJu44dPakdxuxLgLujyYY68kS7OX3LHb3jCHydgZSu2wXxluQPFbNnbzQEPn7_aICNNf16diFulRGT-r4mkUI3lm1vqhyhEZ6h8m9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر فتوشاپی از عکس معروف مسی و یامال، پس از قهرمانی اسپانیا در جام جهانی ۲۰۲۶  @Sportfars</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/451369" target="_blank">📅 13:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451368">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65616cf8d8.mp4?token=IGs09kotExFmKwUBFIo0fHLsBhzs0FkPwGNpDuFsMMvNVwwNiLOSnAy_ahHx5pPDHtbwWhaFyyCvao7DPqLHaqs38_CtgIEGazub6IOrHmh-fTgKWTIIpEOCdiYk4pya1iWTlGiCXYR32F6eHoFS7ibL-9yqkNKHkz_NlfM1Y13mfmHakSyzrcoYndanSx0YcMOFOch4A6CYbOPYbwVp0kk_FL2TGAmLGz7XuhC9qUtOhaZ43-PhIrergh13BcHPvaMeOCoL6Im9-MawKtjO-CaHKELHwCJhEtDRv-4q1BNEGnFJEQYWgT5c7G3ZSu8K3XliCV6XqDvDfKKBxZHiAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65616cf8d8.mp4?token=IGs09kotExFmKwUBFIo0fHLsBhzs0FkPwGNpDuFsMMvNVwwNiLOSnAy_ahHx5pPDHtbwWhaFyyCvao7DPqLHaqs38_CtgIEGazub6IOrHmh-fTgKWTIIpEOCdiYk4pya1iWTlGiCXYR32F6eHoFS7ibL-9yqkNKHkz_NlfM1Y13mfmHakSyzrcoYndanSx0YcMOFOch4A6CYbOPYbwVp0kk_FL2TGAmLGz7XuhC9qUtOhaZ43-PhIrergh13BcHPvaMeOCoL6Im9-MawKtjO-CaHKELHwCJhEtDRv-4q1BNEGnFJEQYWgT5c7G3ZSu8K3XliCV6XqDvDfKKBxZHiAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ اصابت موشک‌های ایرانی به اهداف آمریکایی در منطقۀ عقبۀ اردن  @Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/451368" target="_blank">📅 13:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451366">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt9L0yA_Yb-TdKxW38lsAGsZR5VUvaFSovwppRaER8XD89DNY9rja6KAKSv5wITEZ9qh5iXdX7f5UNiRcjn72mkCNrtozBGuK_FX3KhypAEsKtSEGJNv3ey1xt3ozmpdaMj0a2vzWlBDpHTt3CB4S6p8j2sLHOmO7qtWOkdbl1rMET1nArDymFNcWY-G0ERmpkkH6l6cTEVF6G940hOi5gCw15A57IciaKCGPU5RXKLvkXzzR2buW9P6-Kr1fmqTfNtOPSuJImXY8Ja2Sh_EO2wfgpBZ-d8-PFXqw-CMQUdEVCN_nDZk5ot7LAkRXaNuitSa0sw1HLms5ekyOOlTKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سابق دانشگاه شریف: ایجاد دوقطبی «جنگ و صلح» کمک به دشمن است
🔹
در شرایطی که ایران مورد تهاجم دشمن متجاوز قرار گرفته، انتشار بیانیه‌ای از سوی افراد و جریان‌هایی خاص که بدون هیچ اشاره‌ای به متجاوزین، جنایات بی‌پایان آمریکا و اسرائیل و محکومیت آن‌ها، صرفاً بر «صلح» تأکید کرده، واکنش‌های گسترده‌ای را برانگیخته است.
🔹
رسول جلیلی، رئیس سابق دانشگاه شریف در این مورد می‌گوید: در شرایط جنگی که ایران مورد تهاجم سوم قرار گرفته، انتشار چنین متن‌هایی نشان‌دهنده بلندکردن پرچم ذلت‌جویی است. کلماتی که در این بیانیه به‌کار رفته فقط کلمات ذلت‌بار است‌.
🔹
تعجب می‌کنم چرا این آقایان و خانم‌ها در این شرایط حساس که امروز شهرهای ما مورد هجوم قرار گرفته چنین متنی را منتشر کرده‌اند.
🔹
این متن به خواننده منتقل می‌کند که نکند ایران به آمریکا تهاجم کرده که توصیه می‌کنند دست از تهاجم بردارد؟
🔹
آیا انسان با شرافتی می‌پذیرد که وقتی مورد تهاجم قرار می‌گیرد، از خودش دفاع نکند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/451366" target="_blank">📅 13:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451365">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">۲ مرز جدید به مسیر تردد زائران اربعین اضافه شد
🔹
رئیس ستاد مرکزی اربعین: امسال مرز سومار در کرمانشاه و چیلات در ایلام، در برخی ساعات و به‌صورت محدود برای تردد زائران استان‌های هم‌جوار فعال می‌شوند.
🔹
سال‌ها ۴ مرز مهران، شلمچه، چذابه و خسروی، مسیر اصلی بودند که در سال‌های گذشته تمرچین و باشماق نیز به این جمع اضافه شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/451365" target="_blank">📅 13:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451364">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0D7uZCUFK8f28ojXiOykBmqGt3IDRDQ2H9G8957q0Y3idVsRQPsuSEpnUDg1A-JT3G5njj53-okdfHMb6Ff7Lnm3DwHUGMJH3Vp9I-z86dkHaOwkXnPu45iXJxRASFiXEPu5sImOTJXYZGHo1XSp95cPoPGcwlP8N9KKHGCfZFR-M2SeD2UgXBQwqG_jCjf5PtgX1MwAoMBzwchN7OEJEGGNI-51Wp7oxhs9TphfTl7IhevWSpjxU-Rd3UYJSJn_tZrHjPOM6xlIvQ0PwUBLZUJyz2KjctVN0SG69tWSp867epdR2LSFCbBlgPX_eXpQSq5AqS7SyjphTOcrT7FOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر الهامی: به‌روزرسانی توانمندی و آموزش پدافند هوایی ضروری است
🔹
فرمانده قرارگاه مشترک پدافند هوایی کشور: نیروی پدافند هوایی ارتش همگام با تحول مستمر تهدیدات هوایی و پیشرفت فناوری‌های نظامی، برنامه‌ریزی‌های لازم برای ارتقای توانمندی‌ها و تجهیزات و به‌روزرسانی آموزش‌ها را در دستور کار دارد تا افسران آینده بتوانند متناسب با شکل و شیوۀ تهدیدات آتی، از آسمان ایران حراست کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/451364" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451363">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF1WCbFjsPEtZIRwYOXYkJJGlWXq7RS3GenbJ0JOVYGZS1xswbcafy-WDQyLwdNJMaYWjncwSoqyEk8wHITPDwk7aSYM4AeH8hWDLWZWpdBGtTNxsW20uJeSgCLWL5LlxkvaB3O6jniwS6Vn59N46IAqP6tOyygxlbHbvw8q1EdWjGHjJUofXlpK-Rules-s-WDhFS5Qr7rdLQ1YyxCVHEfg6TtjRqQLPvMdWU7hrNbspnrWnYuKQ0CkYWJSoge-0DLS3zuxuRRhKIMoLKq5zg4GcOk3SBJS-uxD5dIG6dO9_iMJC7LSW2Oe6mifoek-f4kmHz5is7SU-cqFQF4q2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به کانال ۴ میلیون و ۸۰۰ هزار برگشت
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۵۸ هزار واحدی به ۴ میلیون و ۸۱۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/451363" target="_blank">📅 12:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451362">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7187234822.mp4?token=oiwVmhXrAI5Un41ZQcy0dva_qEZuRxejb8at_fZkwNpvFRaKsIsJoJIRkX1Mm4nbLQNvS6pikDTlgfAbZyH6yEDwqRQLlEMcnvI88yfrGCWI7UoknTEVjAFFXOgQfAhWJ5e1aM5z_L3P6GQXURxeBt_GmRGriWwJ_d9jFE8PJ8Kr40_oY6DtrltsXzS9p7EJhWR8wZeRQoJhSy_6cLI57A1aXTo5OMcAV4gQKBJ6O_6a804O8Zlg4e0R9iJyos1z_nBObFeBlYGMUCxCFLVpMhX5SxyegOGj_2n2aMF_TL5t5dbvu1mvyLKCHfy8MgcTHdhV-U9hTtLR0BvV4oFncA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7187234822.mp4?token=oiwVmhXrAI5Un41ZQcy0dva_qEZuRxejb8at_fZkwNpvFRaKsIsJoJIRkX1Mm4nbLQNvS6pikDTlgfAbZyH6yEDwqRQLlEMcnvI88yfrGCWI7UoknTEVjAFFXOgQfAhWJ5e1aM5z_L3P6GQXURxeBt_GmRGriWwJ_d9jFE8PJ8Kr40_oY6DtrltsXzS9p7EJhWR8wZeRQoJhSy_6cLI57A1aXTo5OMcAV4gQKBJ6O_6a804O8Zlg4e0R9iJyos1z_nBObFeBlYGMUCxCFLVpMhX5SxyegOGj_2n2aMF_TL5t5dbvu1mvyLKCHfy8MgcTHdhV-U9hTtLR0BvV4oFncA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: منافقان و نفوذی‌ها می‌خواهند مردم درگیر مسائل دست‌چندم بشوند
🔹
یک فرد نفوذی و منافق با تابلوی دشمن به‌میدان نمی‌آید؛ او با پوشش خودی در داخل صفوف ملت قرار می‌گیرد و تلاش می‌کند با نشر شایعات و طرح مسائل سست و بی‌پایه، مردم را به‌جان هم بیندازد و…</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/451362" target="_blank">📅 12:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451361">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4528a984.mp4?token=lpsiYXI-xxq3ivmDEBunerp10itt8qMf1xvOcpYI5r6GXueotdFNRHLk0zvOh1ln4vutGxY3KgNsKMp-FrAG1OITt8VKtRr0sdORhC54jx4eMBNvEYwFxZuUI6XEIgtj40vVBLlZjdNZ_mZWS0ShVQ4U-WgCPkUnDZ11EoJezL22E5HPXVnaLh4d80Bc-mPA3rAAQcIZir5bN4kSaSUV7HgohzgkjXfAM8xhiM7XBYy6WFJfe-MNdA6-5ugyQNQ9DqWd-hk_OX3hLbPyGmakdYlCjeWp7zuYk_gF3xDUONrjueCMYzi46gIix5LjZzYEIYlaQKMKYzXYbM-YfgKglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4528a984.mp4?token=lpsiYXI-xxq3ivmDEBunerp10itt8qMf1xvOcpYI5r6GXueotdFNRHLk0zvOh1ln4vutGxY3KgNsKMp-FrAG1OITt8VKtRr0sdORhC54jx4eMBNvEYwFxZuUI6XEIgtj40vVBLlZjdNZ_mZWS0ShVQ4U-WgCPkUnDZ11EoJezL22E5HPXVnaLh4d80Bc-mPA3rAAQcIZir5bN4kSaSUV7HgohzgkjXfAM8xhiM7XBYy6WFJfe-MNdA6-5ugyQNQ9DqWd-hk_OX3hLbPyGmakdYlCjeWp7zuYk_gF3xDUONrjueCMYzi46gIix5LjZzYEIYlaQKMKYzXYbM-YfgKglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: تصمیم‌گیری در زمان جنگ نباید با تأخیر انجام شود
🔹
بدیهی است که در زمان جنگ و شرایط اضطراری، تصمیم‌گیری در زمان مشخص مهم می‌شود و ممکن است اگر همان روز تصمیمی را نگیریم، دیگر فرصت نباشد.
🔹
باید همراه با نظارت، به مجریان قانون اختیاراتی داده شود تا…</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/451361" target="_blank">📅 12:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451360">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb3f84a931.mp4?token=APp5tg-hxT-UaIwLv9pmft7o2ZXkLm4FHnD7YBnwEzqAe43k_PRvRmGMfIW7qX-PRZBoVY2-5UtzGkTykpwdTvCKbKJT40kwQ-nBf7uXZPauM5JN3jESWxf8iktzkq3LaW8PzgraQI5Q6ZCJIvJc-MUe1a-dMctQ_1NdTSXHj_LPeBe6UEggLhrTai34oKxrNujDGOeGvCDCWaYp8dBLdIcDxBMyEAEgc93LNAjZmRTbNLKeihjquIKOkGOyLMwriEygak_QUZnfocG8Bgcyj-joe3QA6cIw3jU1K_sZD8J2RkHEEj0gCOY93mBigL8PpSWFXZSrhA2J9C-gjJcMkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb3f84a931.mp4?token=APp5tg-hxT-UaIwLv9pmft7o2ZXkLm4FHnD7YBnwEzqAe43k_PRvRmGMfIW7qX-PRZBoVY2-5UtzGkTykpwdTvCKbKJT40kwQ-nBf7uXZPauM5JN3jESWxf8iktzkq3LaW8PzgraQI5Q6ZCJIvJc-MUe1a-dMctQ_1NdTSXHj_LPeBe6UEggLhrTai34oKxrNujDGOeGvCDCWaYp8dBLdIcDxBMyEAEgc93LNAjZmRTbNLKeihjquIKOkGOyLMwriEygak_QUZnfocG8Bgcyj-joe3QA6cIw3jU1K_sZD8J2RkHEEj0gCOY93mBigL8PpSWFXZSrhA2J9C-gjJcMkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نشست شورای‌عالی قوه‌قضائیه امروز با حضور پزشکیان به‌عنوان مهمان مدعو برگزار شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/451360" target="_blank">📅 12:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451359">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUrRW9HaHK0241nJ3c0j8sRR--YI_aD_AmtyW6vrisDLq3NuM3x0CqKQc7Ivwt0CPQacQTDNTTVyVqJpKaC-6h4qpSvGSU7uF5CJTJXLi4nqu1z0SnBOD70sgWArBN7bJPSpN6syaELxiq0VD1DIvJlpz5HRbprk9foax0kvS7VnYhCwvU8FrkqNfN-MwHP5wZ8Ppzubv2Si0B12I56iR367Gc5fyf4DJZKFiJUZVQkHK-HfqcgkctxdK6m1uO5S8Ncj_cce-MK3EdqvVlmce9pD9f_AbqrPRk6FhKrWkewzqQnmuB-Er9RowG_Yqo6eCXzToYdjpVWlHEdLBSvz8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تبریک قالیباف به روسای مجالس اسپانیا به‌مناسبت قهرمانی در جام جهانی فوتبال
🔹
پیام رئیس‌مجلس به روسای مجلس سنا و نمایندگان اسپانیا: قهرمانی تیم ملی اسپانیا در رقابت‌های جام جهانی فوتبال ۲۰۲۶ را به شما، مردم و دولت اسپانیا تبریک می گویم.
🔹
دفاع شما و بازیکنان…</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/451359" target="_blank">📅 12:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451358">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4M0IcXZv2FqC8Tdf53wxudanDtvD5HKq-U_dbrFD9hoIS138vAMRbznh2sWxLrE1iI7Sr_EgQddigS3dRYs8vG4hENKWdL5z4WknA1oX05sdBlH9K0HIz8CEugRMRZ1MQOQfTO6bTGcppQ1ZX8gFw-thjRSbMJ67nKQDaPG7ERJ3rXxNcsVnt_17991URbgCECKGBoLMIm06kBznT1D4LbF_4fppIX6XaZM7is7FAgZ1dnC-FCSc6sJDZOQzCaaUmgoyYrpUh-JJ7sisol5SR7_kDgxNVaEYU63qO_bp8o1BzZCJCbQNUDxudsAimnjLWN4siksBk6N23ZHxB075Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی در بیمارستان نیایش خرم‌آباد
🔹
دانشگاه علوم پزشکی لرستان: لحظاتی پیش طبقهٔ همکف یکی از بلوک‌های بیمارستان درحال ساخت نیایش خرم‌آباد دچار آتش‌سوزی شد که با حضور به‌موقع نیروهای امدادی مهار شد.
🔸
دود مشاهده‌شده در خرم‌آباد مربوط به این آتش‌سوزی بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/451358" target="_blank">📅 12:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451356">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6739b20d2b.mp4?token=B6pR-BYRznWv_qAoaGIQ_vFqdLDpD_oG2XCZBs17hqvyFgnkMOsWjLDzJQXUqhixw8qZR6hx-M40N3NFMNi6NYrOoeoEz3SOt1GKxs-WtBhAel4Id3VdTinkSu1c5o99NQnDgOR4KvFLzNOfyswaR2SbpObWg6EbQRh3d6gNS6g5IFrMdpNf3QbwmlV1TNhIfERqRumy7sZ7mySM3ZV3yLDIBBEqijhgIb_xY4eqYQSVMcxSxQXg0pb9JnMAy8ndzpGJ0XKE0sB_ZgwtPutTBfsYrzu-kRzw5mlPYJ1QW8DKKMDOFUP_MlLUYvvOND5EoKECwF4-_v1doF3p-CGsJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6739b20d2b.mp4?token=B6pR-BYRznWv_qAoaGIQ_vFqdLDpD_oG2XCZBs17hqvyFgnkMOsWjLDzJQXUqhixw8qZR6hx-M40N3NFMNi6NYrOoeoEz3SOt1GKxs-WtBhAel4Id3VdTinkSu1c5o99NQnDgOR4KvFLzNOfyswaR2SbpObWg6EbQRh3d6gNS6g5IFrMdpNf3QbwmlV1TNhIfERqRumy7sZ7mySM3ZV3yLDIBBEqijhgIb_xY4eqYQSVMcxSxQXg0pb9JnMAy8ndzpGJ0XKE0sB_ZgwtPutTBfsYrzu-kRzw5mlPYJ1QW8DKKMDOFUP_MlLUYvvOND5EoKECwF4-_v1doF3p-CGsJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجربهٔ ایرانی‌ها این‌بار هم جواب می‌دهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/451356" target="_blank">📅 12:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451355">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تکذیب دستور تخلیهٔ چابهار
🔹
فرماندار چابهار: تاکنون هیچ‌گونه دستور تخلیه یا هشدار رسمی برای شهروندان چابهار صادر نشده و شرایط در این شهرستان عادی است.
🔹
برخی رسانه‌ها و جریان‌های معاند با انتشار اخبار نادرست و فضاسازی‌های هدفمند در تلاش هستند با ایجاد رعب و وحشت، آرامش روانی شهروندان را برهم بزنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/451355" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451354">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkYZzvVEvd6nIWmQkUm-ivfiIGMgr9oXhBiXMBzkMatuD2C5Vr1aeZt6DyXNI21k6jRtWVwz8Ql3a7XEOqV4tAiYy_fbI9DvNctEsYZcNoDcV8k7_NeAQbM4cVkYEbjnRO63e2pqVfFgpg3lQ5J6x5Bj_bB3kSMbAVLM260KT1mi640A9hXu6IoeTov9Ws1PhHh8b7zVk6NL_U6XI6BZfKnEdoMgA_s2VMoia39rcGfh5LXxjyQpQ3-DPM7i9u80nnNjrtQi5vrN6-WiXWA9sZJqRWULS2bcZ63ys5jajr1RMznPSmI-2SjwyzaMYstGOg3a4PGTA8ScQ6QLXYXXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نشست شورای‌عالی قوه‌قضائیه امروز با حضور پزشکیان به‌عنوان مهمان مدعو برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451354" target="_blank">📅 11:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451353">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎥
جشن قهرمانی اسپانیا و شکست آرژانتین در ضاحیۀ بیروت  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451353" target="_blank">📅 11:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451352">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4868e6348d.mp4?token=T_N23QWPyCH7FZV0cD7tNYvw6US0HlYwT6ESBIE1mK9pBUhDpKwrvOPZ6gsO-3VZfCgFdLd1uV0gmZydSSE8HS3cWmwi-9kg591-oQrFjSFEQcmMWn2rZZkCQ9vywnuuFaqwYYOFngwwdnKrF7xx49Mf3cv2se32NeAWSPAva96WKoA5QtnDWEtEMIfILS5tGctvtAOEA95j62-rHIA1Evh4H6iB-XrjTEvw5zST8nmdcxpHiHnUnQav1-CDMiHKnEQkrLvB_zT141EazIyIvydlK2upXmNkLJBwQafIHqwVI_oYHjcjHrliqBm3fdLoqN4NCvPfFRcdYdKRdxSNbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4868e6348d.mp4?token=T_N23QWPyCH7FZV0cD7tNYvw6US0HlYwT6ESBIE1mK9pBUhDpKwrvOPZ6gsO-3VZfCgFdLd1uV0gmZydSSE8HS3cWmwi-9kg591-oQrFjSFEQcmMWn2rZZkCQ9vywnuuFaqwYYOFngwwdnKrF7xx49Mf3cv2se32NeAWSPAva96WKoA5QtnDWEtEMIfILS5tGctvtAOEA95j62-rHIA1Evh4H6iB-XrjTEvw5zST8nmdcxpHiHnUnQav1-CDMiHKnEQkrLvB_zT141EazIyIvydlK2upXmNkLJBwQafIHqwVI_oYHjcjHrliqBm3fdLoqN4NCvPfFRcdYdKRdxSNbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای دروغ جدید ترامپ دربارۀ آزادی یک تبعهٔ زن ایرانی-آمریکایی
🔹
از ساعتی قبل، تصویری از یک تبعۀ ایرانی-آمریکایی به‌نام دنا کراری، هنگام ورود به یکی از فرودگاه‌های آمریکا، خبرساز شد. پیش‌ازاین، وکیل این زن نیز با توییتی در شبکۀ اجتماعی ایکس، ادعاهایی درباره…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451352" target="_blank">📅 11:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451351">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f878972977.mp4?token=bAxAO9oddRNjAYlVsC1Vxnf8_kgrhQC0I6y8Bd3n8GhzfhCtt0QfXwqnC470GRpSlS_AVryUlfl2iPAIr3LrTBCnJ0oQGQlBPXcfFjN58HrUs5SDTy9jJsCbKPL-TlZhcwvURi09dgq9sP6-zhFBmooyEigWWyA9iYFn6BV6Q3jcSzQ-AjCMvQnMIs23aCBimIbIY-8lhtCu9Ga_G0XAUQ-Cbk7tOYOlITtLT5LAu6diILVnuLXBBZQTZqyC1cwSBxywS6wuljpmFVhKEmR-_vfi9tILBKDvVm3pxExPdScKmENzqXSgPhOCNZTGVrKKuOwW-9Z4cXhwrdTFa3OWjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f878972977.mp4?token=bAxAO9oddRNjAYlVsC1Vxnf8_kgrhQC0I6y8Bd3n8GhzfhCtt0QfXwqnC470GRpSlS_AVryUlfl2iPAIr3LrTBCnJ0oQGQlBPXcfFjN58HrUs5SDTy9jJsCbKPL-TlZhcwvURi09dgq9sP6-zhFBmooyEigWWyA9iYFn6BV6Q3jcSzQ-AjCMvQnMIs23aCBimIbIY-8lhtCu9Ga_G0XAUQ-Cbk7tOYOlITtLT5LAu6diILVnuLXBBZQTZqyC1cwSBxywS6wuljpmFVhKEmR-_vfi9tILBKDvVm3pxExPdScKmENzqXSgPhOCNZTGVrKKuOwW-9Z4cXhwrdTFa3OWjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: فارغ از تفاهم‌نامه، نباید اجازه بدهیم که از تنگهٔ هرمز برای تهدید امنیت ایران سوءاستفاده شود.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451351" target="_blank">📅 11:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451350">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2ee38c75.mp4?token=doGgD38a3zCWCgzqF3M9oiQP1MWXfI-bWnBYFe9iV-eX3HBlM4MPgp6bdVP6NBQZ2agGtUwU2ydcTCz6gFm0SXpiiF0F34seLvTHxXqXjFZvhWrTK-FKs1LzYZFMlBZQFjEIHMBJE-9bbgFGUBc9zABikjFuP5Cgn7X-jkYLa6lUbhSADvEpGSZtaCUqZwySNnrvuah7unymvHbMuJGXc_XTh37Y2qpp3_yQ0hVodAwIFXvNz2Pmg7mKdrwfhztzT_bK49mfHHvVflHHqyWsD98f80lvnR9v0Vvj8ZP7vNjcNe52Al9t4JduBa653aITgHuncAaqg-J0wq0rr7hp3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2ee38c75.mp4?token=doGgD38a3zCWCgzqF3M9oiQP1MWXfI-bWnBYFe9iV-eX3HBlM4MPgp6bdVP6NBQZ2agGtUwU2ydcTCz6gFm0SXpiiF0F34seLvTHxXqXjFZvhWrTK-FKs1LzYZFMlBZQFjEIHMBJE-9bbgFGUBc9zABikjFuP5Cgn7X-jkYLa6lUbhSADvEpGSZtaCUqZwySNnrvuah7unymvHbMuJGXc_XTh37Y2qpp3_yQ0hVodAwIFXvNz2Pmg7mKdrwfhztzT_bK49mfHHvVflHHqyWsD98f80lvnR9v0Vvj8ZP7vNjcNe52Al9t4JduBa653aITgHuncAaqg-J0wq0rr7hp3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: از نظر ما چیزی به‌عنوان «تحریم هوایی» در یمن وجود ندارد و اصل تحریم‌کردن یک ملت را ظالمانه می‌دانیم
🔹
هواپیمای ایرانی حامل هیئت یمنی حاضر در مراسم ادای احترام به رهبر شهید و جمعی از مجروحان یمنی بود که در ایران درمان شده بودند. @Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/451350" target="_blank">📅 11:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451349">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2438504620.mp4?token=kZRrZJcKb17F3yU-fJSwWCEcxBTC2YdRmtBNgxWCLJWKkqZBzZxP_4KrKj5PmDKwSanYXs_a6WMSPHH93B5GqkzJEkiHkEW_SBbQIam_W-aZ-e1faZwDIczrvg2HbjB_UjbJcenjgqjo704nzTbKtbIfK1A4UUVvbPT5TzotDpeYsv64lKG8GYub9ntHESA3RlNtpanrkkI9WbybXwrSiWSJ_vbUusXZzT1rnab1kPszVpGxQJbSRxDmPXED7wKNDWziKLH7l7F5RxMi9R1nijeZnLmbbN0j0kBPKlv1U6M0gMmtuCQD5suMKO7NYFCk1jfX0XqfJGDz6keFmWAWCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2438504620.mp4?token=kZRrZJcKb17F3yU-fJSwWCEcxBTC2YdRmtBNgxWCLJWKkqZBzZxP_4KrKj5PmDKwSanYXs_a6WMSPHH93B5GqkzJEkiHkEW_SBbQIam_W-aZ-e1faZwDIczrvg2HbjB_UjbJcenjgqjo704nzTbKtbIfK1A4UUVvbPT5TzotDpeYsv64lKG8GYub9ntHESA3RlNtpanrkkI9WbybXwrSiWSJ_vbUusXZzT1rnab1kPszVpGxQJbSRxDmPXED7wKNDWziKLH7l7F5RxMi9R1nijeZnLmbbN0j0kBPKlv1U6M0gMmtuCQD5suMKO7NYFCk1jfX0XqfJGDz6keFmWAWCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: تا جایی که طرف مقابل تعهداتش را اجرا می‌کرد، ما هم اجرا می‌کردیم
🔹
ما هیچ‌وقت پیشگام در نقض‌عهد نبودیم؛ اما زمانی که آن‌ها تعهداتشان را نقض کردند، ما هم اعلام کردیم که تعهداتمان را اجرا نمی‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/451349" target="_blank">📅 11:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451348">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جاسک
🔹
سپاه هرمزگان: عملیات انهدام کنترل‌شده مهمات عمل‌نکرده امروز از ساعت ۱۲ تا ۱۶ در محدودهٔ بندر جاسک انجام می‌شود و به‌همین‌دلیل احتمال شنیدن صدای انفجار در این محدوده وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/451348" target="_blank">📅 11:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451347">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbf440b549.mp4?token=BE4m3-rAVGNYjmj0ygzMJFPUHD7UYmV4lAezQ3B9X5yFM_d8ZoZ4cZHS-zyLaNZqSnSK5r070xRVQWRiL1zdQ5eNYykPznHgD2hwcDD1SZK4NEId2tJDoDrIaIeLvSKUl2bvdCtWmcLBDC2vDOzJrsNFsdzBBym4q9mtVSlnAOm4rXEmNfTrdQcKPi6QNiEeIXZXAgQqavUGVazT5_lXyOytGa5MqN_HAHw_aCdeKu7b7FautON35hGeUvw1W3CvkSJg6fLwvfzu_CaXCqFDDASsMlKkkWm02R4h5mqqkm6IgM95sZYr2MT6bEazkwuyLZmU26HAWXepVbXtKMa8Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbf440b549.mp4?token=BE4m3-rAVGNYjmj0ygzMJFPUHD7UYmV4lAezQ3B9X5yFM_d8ZoZ4cZHS-zyLaNZqSnSK5r070xRVQWRiL1zdQ5eNYykPznHgD2hwcDD1SZK4NEId2tJDoDrIaIeLvSKUl2bvdCtWmcLBDC2vDOzJrsNFsdzBBym4q9mtVSlnAOm4rXEmNfTrdQcKPi6QNiEeIXZXAgQqavUGVazT5_lXyOytGa5MqN_HAHw_aCdeKu7b7FautON35hGeUvw1W3CvkSJg6fLwvfzu_CaXCqFDDASsMlKkkWm02R4h5mqqkm6IgM95sZYr2MT6bEazkwuyLZmU26HAWXepVbXtKMa8Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: منظور آمریکا از دیپلماسی، تحمیل، ارعاب، تهدید و تحریم است و تا وقتی که در این فضا باشند، پاسخ ما دفاع از کرامت و حاکمیت ملی ایران است.  @Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/451347" target="_blank">📅 11:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451346">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d272ea39a.mp4?token=T1DY_VZs3iJalzP6wRxPky9IC_bJvoXJxtLZ_AXcHOdOY4oPAL7d1Pd8OpVyK_81Ac7Me7bOyUfr5ecZHyT1v39zJH4mBySLMNBAGgHx6bhlTIqvEOu_N2RYQs4d6LPn9D3LNMhGDCBvEXKIuzotsdjNYPr05do5GISErPQGq9lUZRi970OnuW-_LTaDXTIPWSQbOURVsTmIjKrYlqf0jmDZhY0qFWieF0FpFjiDZZWJ1kxyQRVbEePyPguIG1lXQkrD58JXfzXOj13Dn7Nw5FSpysuAznZWa0gdh4cgltgkms4C0p3lI3CUQjJjB4wGxl5AmbqGSG4FSfZTFio4Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d272ea39a.mp4?token=T1DY_VZs3iJalzP6wRxPky9IC_bJvoXJxtLZ_AXcHOdOY4oPAL7d1Pd8OpVyK_81Ac7Me7bOyUfr5ecZHyT1v39zJH4mBySLMNBAGgHx6bhlTIqvEOu_N2RYQs4d6LPn9D3LNMhGDCBvEXKIuzotsdjNYPr05do5GISErPQGq9lUZRi970OnuW-_LTaDXTIPWSQbOURVsTmIjKrYlqf0jmDZhY0qFWieF0FpFjiDZZWJ1kxyQRVbEePyPguIG1lXQkrD58JXfzXOj13Dn7Nw5FSpysuAznZWa0gdh4cgltgkms4C0p3lI3CUQjJjB4wGxl5AmbqGSG4FSfZTFio4Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: صلح را در طاقچهٔ روابط بین‌الملل تقدیم نمی‌کنند؛ برای صلح، باید جنگید!
🔹
ما بزرگترین انسان‌هایمان را برای برقراری صلح پایدار برای تک‌تک مردم ایران تقدیم کرده‌ایم؛ باید از تصورات فانتزی دست برداریم.
🔹
آمریکایی‌ها خرداد پارسال گفتند «برای…</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/451346" target="_blank">📅 11:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451345">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331f15255a.mp4?token=WqKjAfLH3IBC9EPnumaU6rLBt9CEd0WyrdvU2Pu1skXy0DAr2T6SIU5bEqOuIvkk4qgREkLMBJ-ONvG6bcf1_Oxkdo9tqV7F7pKhPDSxsgMHAuySSsQ57malJl69He1irn4aALP1YV2TijhXWhqjP3ydQAwjsjONgwF901O7M5764XrDBxS5suHU8nSdzuezXUoFfpNPTlwUefqz2AE5JpjBuwElLKBgbseyE_9wY5Sun5Rpzy7kfZvd2Oy2Mty8WDYdsCjcdPTu2nOruCdSxA4VH_zM-vBjxqQy4rCfO6batonA2ci_T0WKQ_Y_9u1WByGg3jDtGiUXOPR02KGjXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331f15255a.mp4?token=WqKjAfLH3IBC9EPnumaU6rLBt9CEd0WyrdvU2Pu1skXy0DAr2T6SIU5bEqOuIvkk4qgREkLMBJ-ONvG6bcf1_Oxkdo9tqV7F7pKhPDSxsgMHAuySSsQ57malJl69He1irn4aALP1YV2TijhXWhqjP3ydQAwjsjONgwF901O7M5764XrDBxS5suHU8nSdzuezXUoFfpNPTlwUefqz2AE5JpjBuwElLKBgbseyE_9wY5Sun5Rpzy7kfZvd2Oy2Mty8WDYdsCjcdPTu2nOruCdSxA4VH_zM-vBjxqQy4rCfO6batonA2ci_T0WKQ_Y_9u1WByGg3jDtGiUXOPR02KGjXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: همزمان با درهم‌کوبیدن منشأ تجاوزات آمریکا توسط نیروهای مسلح ایران، از هیچ تلاشی در دیپلماسی برای توقف جنایات آمریکا فروگذار نمی‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/451345" target="_blank">📅 11:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451344">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e384a7c28a.mp4?token=HwLrUlT074tuXpyRTzOey-p366q4cjNfRSNHj0gERX8QQPH3OvSMHl1RmL_SDdZ73a8-R4W3fzyyfoKj15EMncCXoYutfu2hmDqOLu0mrYAwBapoRZ0TMfm-93EmsvIaueVGlDU9XRM6NxJ7WcuBp1FeAvcDMcR0UdSoP_n5BSpsU-xpjfmFQtctXKr2b5qNUxRAtFEjt86sF2gOC0ps3Jwr3VU6qFY2-54Qq8--Y_n_blYtmSLW1GBAFP7V4yytPn95q_f7XunfQnbhlwCRXGPtL0i17ZYbohOsJM0wqs50Dc_VjTcdbOpW8dx4wgBNQzHsZHd3gnOwi7kAP7oHyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e384a7c28a.mp4?token=HwLrUlT074tuXpyRTzOey-p366q4cjNfRSNHj0gERX8QQPH3OvSMHl1RmL_SDdZ73a8-R4W3fzyyfoKj15EMncCXoYutfu2hmDqOLu0mrYAwBapoRZ0TMfm-93EmsvIaueVGlDU9XRM6NxJ7WcuBp1FeAvcDMcR0UdSoP_n5BSpsU-xpjfmFQtctXKr2b5qNUxRAtFEjt86sF2gOC0ps3Jwr3VU6qFY2-54Qq8--Y_n_blYtmSLW1GBAFP7V4yytPn95q_f7XunfQnbhlwCRXGPtL0i17ZYbohOsJM0wqs50Dc_VjTcdbOpW8dx4wgBNQzHsZHd3gnOwi7kAP7oHyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مقامات آمریکایی این‌قدر در معرض گزارش‌های ساختگی هستند که هر خبری دوست ندارند را هوش مصنوعی می‌دانند
🔹
آمریکایی‌ها خودشان هم می‌دانند که جنایت میناب کاملاً عامدانه انجام شده است. مقامات آمریکایی با برجسته‌کردن موضوع میناب می‌خواهند نشان…</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/451344" target="_blank">📅 11:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451343">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9uH5IoH-nM8Mn-p8H7n5IZU1PwBDtsmRGyTYxxdL66S3EUQfVsBdQEctZGcG-4pfosISY_Xec9Iu4DwQAl1lmwt9XGj2hQEzba4NX6RAaPZaKThk01vVLbe6KMRB_1kkDrJcnLu2xXzQeRSbEhtmAJc6l-UQFYdSqwwSJOHqZEyU3w4F0atpELgfwF1cyr6YYbMHQUntdWDXF-YB37Wi0l4FP52EKMm90kEDduaHttdO7iM5E2eQfdLc7YgUZShxAm1brVNy3BssBNAT-V7pfRrh0iMdQWDMRRBKopRHsdHf5COhZgBV8ac90U_VApwrWJT1sQL1mpvuc7Zje_AGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندازۀ تخم‌مرغ‌ها هم آب رفت
🔹
قیمت تخم‌مرغ در بازار تهران به شانه‌ای ۴۸۰ هزار رسیده که نسبت به دو هفتۀ گذشته حدود ۸۰ هزار در هر شانه افزایش داشته.
🔹
در یک فروشگاه بزرگ منطقه ۱۹، یک خانم میانسال در حال خرید تخم‌مرغ می‌گوید: هفتۀ پیش شانه‌ای ۴۲۰ هزار تومان خریده بودم. شانه‌ها با وزن ۲ کیلو قیمت‌گذاری می‌شوند، درحالی که این‌ها آن‌قدر ریزند که معلوم است وزن کمتری دارند.
🔹
پیش از این، تولیدکنندگان کمبود و گرانی خوراک را عامل افزایش هزینه و گرانی تخم‌مرغ می‌گفتند. این درحالی است که مدتی است وزارت کشاورزی از افزایش واردات و ترخیص خبر می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/451343" target="_blank">📅 11:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451342">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597a7bb75c.mp4?token=Qs2BI7gkiezjz_EqfxhHcJBDeV6aoVJcb_m3c0-KC214WHMe57p0RjtLu5yML_uNZPCFEcrHyfKjCK0Pi-rdWiGu8UrzB2nv-Kig2GopNpQ0LiowfZpDiqxkJ8YblsjqOuGZ_OTLMA_D6ALP4LILMYrgnjHrkzsSiGnIuZWUgE4NKmj6ELVJKG-zcb4TQbz4TNRpF_uxEvUVr6p6iEVRgK8nWWvl_4vRr3x2dmK9lLiSQna8r8Vmhx_3_BlzeHskUuMEwk0kFC4Gom7nNm9qaG6FdBA_Qz3MNDrgtTUh8CCWpl5ZhpgQQhpI4WWLdpEIj9CioXBiMTlfHsUyKxzLkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597a7bb75c.mp4?token=Qs2BI7gkiezjz_EqfxhHcJBDeV6aoVJcb_m3c0-KC214WHMe57p0RjtLu5yML_uNZPCFEcrHyfKjCK0Pi-rdWiGu8UrzB2nv-Kig2GopNpQ0LiowfZpDiqxkJ8YblsjqOuGZ_OTLMA_D6ALP4LILMYrgnjHrkzsSiGnIuZWUgE4NKmj6ELVJKG-zcb4TQbz4TNRpF_uxEvUVr6p6iEVRgK8nWWvl_4vRr3x2dmK9lLiSQna8r8Vmhx_3_BlzeHskUuMEwk0kFC4Gom7nNm9qaG6FdBA_Qz3MNDrgtTUh8CCWpl5ZhpgQQhpI4WWLdpEIj9CioXBiMTlfHsUyKxzLkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: متن تفاهم‌نامه روشن است و تفسیرپذیر نیست؛ آمریکا جایی نگفته که «به‌دلیل اختلاف در تفسیر» به ایران حمله کرده  @Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/451342" target="_blank">📅 11:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451341">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYuHkz10sDYKfWS9lmEQpwNKR3-8PVRAmyu00j66Kq8L95fBA7lpV4h3005W1uXpvzBQuBZMPlIwbxb1auos3WvBHVqmmBmKW7RruqXsdwz1GrqufiNto1p452iAqcFNBkzgt3ZIwipnEYj-SIC6pqt3fX2nemcpHKbsT9xj4xlRlyvAhkD2dxdLgt6ZcXX4kYY6m4KkdHFUiKMgIksryR5VItcaEyHRudsMMRiL-2al6Q8zZaQo4AMnQzFXcVR3fcWilpCjWRs-vuAnDAi0VrdZaqcr8R-buruXEYp6JtwEVh7QF7CPAttV7vaTZXITt8j8HcMIcp4gao8RhD-bFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مراسم بزرگداشت شهید زهرا حدادعادل از طرف خانوادهٔ ایشان
◾️
پنجشنبه ۱ مرداد، ساعت ۱۷ الی ۱۹
◾️
میدان فلسطین، مسجد امام صادق علیه‌السلام
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/451341" target="_blank">📅 10:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451340">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ea164fb5.mp4?token=AmVQ-EPKAoRzA3FAHc1IcFWxpEHEMvpIRPvO2of4ZhGQU9LkVQas02qWQjHkZAvo58TFEzQoZs8tIH4EiADdjoCMwTCesw31M4lVHN7k_4iOc76PkHvf4cNP3f2mxBJmKBMUdS2O2ouAi0pTp_6h_Im88uCF4r-6h4tNFmRGrHJk3_2oVd6nqLSt_TiaYWO6Uzqeij4OcJLw2FcTlNT02bnnph0w8MkyVXux5VPa-Ncgn_cswUpra5RB41rfYxfuDfG2G8jdICiaw1gZUzAJzGFJBDhvRvlDqqmrLwOOoEMPh0g6jD_GhNlF7AxT2wO7DyXU5K6vNgmIjDEZ3fAEuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ea164fb5.mp4?token=AmVQ-EPKAoRzA3FAHc1IcFWxpEHEMvpIRPvO2of4ZhGQU9LkVQas02qWQjHkZAvo58TFEzQoZs8tIH4EiADdjoCMwTCesw31M4lVHN7k_4iOc76PkHvf4cNP3f2mxBJmKBMUdS2O2ouAi0pTp_6h_Im88uCF4r-6h4tNFmRGrHJk3_2oVd6nqLSt_TiaYWO6Uzqeij4OcJLw2FcTlNT02bnnph0w8MkyVXux5VPa-Ncgn_cswUpra5RB41rfYxfuDfG2G8jdICiaw1gZUzAJzGFJBDhvRvlDqqmrLwOOoEMPh0g6jD_GhNlF7AxT2wO7DyXU5K6vNgmIjDEZ3fAEuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: متن تفاهم‌نامه روشن است و تفسیرپذیر نیست؛ آمریکا جایی نگفته که «به‌دلیل اختلاف در تفسیر» به ایران حمله کرده
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/451340" target="_blank">📅 10:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451339">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Snw1na8As3LAb0PRLICbiCDQK1EK-5mVGRcXQL3HFMnCoxn9K0lJjwHsEsSaDFSsBOqskZEkvOa8hilI1cHQGLTY8DxEm6XYVCCX02-Gt5qi139Rm_-QXxki52Jdzby-fIyxc9DbLS-nMVyEpq6UP6i3hQLRjunnFA0i0XZ1uiY26SAJ0EOKYptorf_BGizfZ9pDRVROY4sGBYjIFP_FhCh5gGeXluG3yXBJ3RiWvXMlz5hp5wEdo8oRyo3Sh9YumJF1-DzoHgHqhUruc1dlap5je007NWUUHBok9g9Y9blvanm_q0GKW7MOTIutd6IV9NdqI6MLSKoFDZrYwpcRuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسب ۴ مدال توسط دانش‌آموزان ایرانی در المپیاد جهانی اقتصاد
🔹
تیم ملی اقتصاد ایران در نهمین دورهٔ المپیاد جهانی اقتصاد موفق به کسب یک مدال نقره و ۳ مدال برنز و کسب عنوان بهترین نمرهٔ مالی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451339" target="_blank">📅 10:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451338">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785f2fdeb8.mp4?token=UP9fNWXGxxoQjSbc8FAnpDGtYjPovlKopu0VODV6ytMzsX1dg0yNjAfaOhPtkv1x-fz2I0dznVBgwDlQo-5vyTtNSZYEIAaIjAh7NlmMus6YVjL9P4PJaLGUSRG2YzLzYa-uwyIzdvj1ziIF4ts42ZwXkyuErX0eOiDnxrJy1pI118GDG8D-YxDWytpp-TPnDaAdKqkdNcRaAQ2xfDOqSoeLz6E6xdYJkyLUcGmjlYjmNM9rYtEdujVMCLY36rI82Z4DhGBLdLhwsFWy63OrkFswv3PU-lG2IAHwdw61MJ3ThMNk364e0bYIlRZs9-BtLZbRQxyrLw3x9tBxI0AhEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785f2fdeb8.mp4?token=UP9fNWXGxxoQjSbc8FAnpDGtYjPovlKopu0VODV6ytMzsX1dg0yNjAfaOhPtkv1x-fz2I0dznVBgwDlQo-5vyTtNSZYEIAaIjAh7NlmMus6YVjL9P4PJaLGUSRG2YzLzYa-uwyIzdvj1ziIF4ts42ZwXkyuErX0eOiDnxrJy1pI118GDG8D-YxDWytpp-TPnDaAdKqkdNcRaAQ2xfDOqSoeLz6E6xdYJkyLUcGmjlYjmNM9rYtEdujVMCLY36rI82Z4DhGBLdLhwsFWy63OrkFswv3PU-lG2IAHwdw61MJ3ThMNk364e0bYIlRZs9-BtLZbRQxyrLw3x9tBxI0AhEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوشحالی اسپانیایی‌ها بعد از سوت پایان بازی  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451338" target="_blank">📅 10:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451337">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">احتمال شنیدن صدای انفجار کنترل‌شده در اصفهان
🔹
استانداری اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در جنوب و غرب اصفهان، بهارستان و صفه و ابریشم تا بعدازظهر امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451337" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451336">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a52bc34670.mp4?token=VL5LOhRwIRvH6Qwy4F4u85Fge83ajMcJTw8NYnrup7JgzQtPoGzL9hgekeos6xKF-Ku8ydIXGkdyog49u4oAly8deBaVj_g5W091wS7kOO1SpVNJzUh83jqj-3308IIJXI2VxtTrJ9lP22biUk4Xrbqy4YvL9xfaq69hYAH9vk0FeaCIgrqrn_cW_ErNhKkibeMvgW1IHoeeTHGoKOOjuvP_XZlL8fTN1TAvSK9GPfLVkW0X0hP5zAp9PM8cr8m5zkVj6kqJVoS2WRNBHhK6lhm_GXAdz7VG2vqn0V3t_oNy2td5B-2pAGq6Q5voInMVagKM8mVVEGQ8HtNhpNpxkHCrTl86niYznLRwEbnYf-BtKdlzeIZfMws1LCXjWXhPLEvOO3Ac4oxI04LY3OSQT-MEkWz1tCua9vjs1JsHZ4E0kJwP_7FcOiYdEUuLz3lfY_J-Zbcr0w8vW4YnszrqHrJq7OjUnpis5N9emzzhIqt9JUWnrMZ5TFPeJCBebRAuIF-OYE8D7I7FyUs8MrE4uTX7XU3ib0kGAwiHWZckgHXUtZgNjNvJSK7_wKCIeqfVUyJXH-XujC2r__XVehJdhz6D72hu7Q9bN0oCSOuAPFr1Zh3qpOmELDM1A39DJ65PAMjifhZz7xyA23SPsZicSbrFk9AX9-xP8KhUPwlClFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a52bc34670.mp4?token=VL5LOhRwIRvH6Qwy4F4u85Fge83ajMcJTw8NYnrup7JgzQtPoGzL9hgekeos6xKF-Ku8ydIXGkdyog49u4oAly8deBaVj_g5W091wS7kOO1SpVNJzUh83jqj-3308IIJXI2VxtTrJ9lP22biUk4Xrbqy4YvL9xfaq69hYAH9vk0FeaCIgrqrn_cW_ErNhKkibeMvgW1IHoeeTHGoKOOjuvP_XZlL8fTN1TAvSK9GPfLVkW0X0hP5zAp9PM8cr8m5zkVj6kqJVoS2WRNBHhK6lhm_GXAdz7VG2vqn0V3t_oNy2td5B-2pAGq6Q5voInMVagKM8mVVEGQ8HtNhpNpxkHCrTl86niYznLRwEbnYf-BtKdlzeIZfMws1LCXjWXhPLEvOO3Ac4oxI04LY3OSQT-MEkWz1tCua9vjs1JsHZ4E0kJwP_7FcOiYdEUuLz3lfY_J-Zbcr0w8vW4YnszrqHrJq7OjUnpis5N9emzzhIqt9JUWnrMZ5TFPeJCBebRAuIF-OYE8D7I7FyUs8MrE4uTX7XU3ib0kGAwiHWZckgHXUtZgNjNvJSK7_wKCIeqfVUyJXH-XujC2r__XVehJdhz6D72hu7Q9bN0oCSOuAPFr1Zh3qpOmELDM1A39DJ65PAMjifhZz7xyA23SPsZicSbrFk9AX9-xP8KhUPwlClFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موشن‌گرافی| سودای تجزیه
🔹
روایتی مستند از طرح آمریکایی‌صهیونی برای تجزیۀ ایران و نقش خیانتکارانۀ گروهک‌های تروریستی تجزیه‌طلب.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451336" target="_blank">📅 10:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451335">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzNJUmAnTAXmjeQ7MDGv_seIQpApOiJzD46cEIWnv4bMrWLUbxg9ls20VBVghbkx003tL9oWHa4t0w-LbUeMlgy72QfffdshsqOLbk16T1EfX9Cx03M9ZDDIYgKQdQKPzlIJObwefL0ec4qKfJZJrP2JtzZ3AdqQtnWl3sfGoxzmMQ2bxdl--ipghwU5WNE0gKW_lDENFVmZkfdzluJTaryXVzxrrANSa94BKKhD97ffNzKM9JHp8noAnincX97O-mLDkFOkckFY2h2cuDVdkrLVnvKDEHhVmUnfstC2qbVlFJQ_YY_DgclFk6u0sHI0r_t-DvbDp4bq3y9BE1_WDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلا فوئنته: به شاگردانم افتخار می‌کنم
⚽️
سرمربی اسپانیا: به این نسل از فوتبالیست‌ها که با تکیه بر این فلسفه همواره در حال پیشرفت بوده‌اند و الگویی از یک گروه، یک تیم و یک خانواده را به نمایش گذاشته‌اند، بسیار افتخار می‌کنم.
⚽️
این تیم شایسته قهرمانی بود. از ابتدا تا انتهای مسابقات شخصیت، کیفیت و جاه‌طلبی خود را نشان داد.
⚽️
فران تورس همیشه آماده بود. وقتی وارد زمین شد، همان تأثیری را گذاشت که از او انتظار داشتیم و گل قهرمانی را به ثمر رساند.
⚽️
آرژانتین تیم بزرگی است و مسی یکی از بهترین بازیکنان تاریخ فوتبال است. قهرمانی مقابل چنین حریفی ارزش این موفقیت را بیشتر می‌کند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/451335" target="_blank">📅 10:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451334">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
سپاه: دو نفتکش که قصد تردد در مسیر ناایمن تنگه هرمز را داشتند منفجر شدند
🔹
اواخر شب گذشته دو فروند نفتکش متخلف که به تحریک و اجبار ارتش کودک‌کش آمریکا قصد ورود و خروج از مسیر ناایمن و حادثه‌ساز جنوب تنگۀ هرمز را داشتند منفجر شده و از حرکت باز ماندند. …</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/451334" target="_blank">📅 10:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451333">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فرماندار بوشهر: دقایقی پیش بوشهر ۲ بار هدف تهاجم دشمن آمریکایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/451333" target="_blank">📅 09:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451332">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15ea928e59.mp4?token=S5r8RChGdcqZPIxmo0No-4IKHRpNiukZ_33ZTPAugTPL1X6jniUowsi4ew8GkeRwJN5YZuqLcnq_tS_RK_4-NWqlQjfC9mKMiPFaRlGMU56AzAsMZJzVJNwHhpjs5_OhUdLVxdKglWGuxa7m0pdgyG72n3QAPQP_GT-qrSJnefkP9gyN_v-wTjB5EpwPkCPr77TxnXL-xASIzO_2a6d6I_IDNpfNNTslI_Vt5-oSdxDmTwCAPyJ413NJ3O-TmM0QiRyOjJqOLLRlv_7oC6nuyoF-EvxAob7odWkrFTTqwF7I2hq5RLWAyZ9T6h3jJGbeeA32V7kJUrImLNSukZKPXIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15ea928e59.mp4?token=S5r8RChGdcqZPIxmo0No-4IKHRpNiukZ_33ZTPAugTPL1X6jniUowsi4ew8GkeRwJN5YZuqLcnq_tS_RK_4-NWqlQjfC9mKMiPFaRlGMU56AzAsMZJzVJNwHhpjs5_OhUdLVxdKglWGuxa7m0pdgyG72n3QAPQP_GT-qrSJnefkP9gyN_v-wTjB5EpwPkCPr77TxnXL-xASIzO_2a6d6I_IDNpfNNTslI_Vt5-oSdxDmTwCAPyJ413NJ3O-TmM0QiRyOjJqOLLRlv_7oC6nuyoF-EvxAob7odWkrFTTqwF7I2hq5RLWAyZ9T6h3jJGbeeA32V7kJUrImLNSukZKPXIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ لرزش‌ زمین‌لرزۀ کرمانشاه در ۵ استان احساس شد
🔹
لرزش ناشی از دو زمین‌لرزۀ بالای ۵ ریشتر کرمانشاه، در استان‌های ایلام، مرکزی، همدان، کردستان و لرستان نیز احساس شده است.
🔹
سازمان مدیریت بحران تأکید کرد که این زمین‌لرزه‌ها صرفاً پدیده‌ای طبیعی ناشی از فعالیت‌های…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/451332" target="_blank">📅 09:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451331">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
رسانه‌ها از اصابت مستقیم موشک به منامهٔ بحرین و بلندشدن ستون‌های دود خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451331" target="_blank">📅 09:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451330">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glpZCzalW-yrx4XrARvrdrOhpGjRfqd3cSABgiZ3zwSc_N9QdGMGUFM567ibI3zviIN6U3XaIVaMd75XHKEwxGZrWHrnlJQm5q-Ink5ancJ4ZNjB66IF0R6VX_Fkw0eoHmkKEhPYNaNixTVTSrGP0VNGNIiRlmWp-GflljVCLiP8nzzl3E3xrn7t3GO2xsg7S-87dyJ9x_l88lusZdLUOWLp0-s9PFPZ5JSISCYrkdnPAfCUA-OvEAeZrrBYaq0EkO-zeYAJzV4IbuUvbOvSCR-du8FZuuRLCzCBcsE0T1QaZFBFydvdniGNqqdkuKbEqYitWuiM4M6jJZUg274Vlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌فروش بلیت قطار اربعین از فردا
🔹
رجا: فروش بلیت قطارهای مسافری برای ‍۱ تا ۱۶ مرداد، فردا از ۸:۳۰ تا ۱۱ صبح به‌صورت اینترنتی و از ۱۱ تا ۱۳:۳۰ از طریق آژانس‌ها انجام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451330" target="_blank">📅 09:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451329">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌ جزئیات حملهٔ ساعاتی پیش دشمن آمریکایی به اطراف تبریز
🔹
بامداد امروز یک منطقهٔ نظامی در جنوب‌غرب تبریز هدف حملهٔ ارتش تروریستی آمریکا قرار گرفت. صدای انفجارهای این حمله در بخش‌هایی از تبریز هم شنیده شد.
🔹
مدیرکل مدیریت بحران استانداری آذربایجان‌شرقی: این…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451329" target="_blank">📅 09:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451328">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
وزارت کشور بحرین از فعال‌شدن مجدد هشدارهای حملهٔ هوایی خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451328" target="_blank">📅 09:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451327">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">امام‌جمعهٔ اهل‌سنت میرجاوهٔ سیستان‌وبلوچستان به شهادت رسید
🔹
سحرگاه امروز «محمد انور ریگی» امام‌جمعهٔ مسجد علی‌بن ابی‌طالب(ع) شهر میرجاوه در استان سیستان‌وبلوچستان توسط افراد ناشناس هدف سوءقصد قرار گرفت و به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/451327" target="_blank">📅 09:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451326">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
همزمان با کویت، منابع عربی از وقوع چندین انفجار در شهر منامه پایتخت بحرین خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/451326" target="_blank">📅 09:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451325">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5a63e91.mp4?token=BKvOgcMBKl2CF14E7vCgYbWJTuaXpOsRjJFkSSAl5bHD7DrGa-uvgX0xKMVXxWln1fRjddRN568dSnlRJCt5KUmpUGT5LWGoIXg4N-iiPXRqnIjUkbR8AChi_3SHfo98mqQer7Xx4pKN_nruv-W-t5eY91TTv-U-X9Kd8O6EwM8egdxqtVq6QlT5kqoN3BblXMlxV5Zt0gCMurBJhYZKXMNm2ftHx50NAg24byC09mI7jzZqTm-ZDclloTtrVks_ci2_pKwtyVssXNPLr_yNlhrF-_n-7yIneRcd8vRarboRsepiFBTkEuEec6NEznSRBqXtOV_ONGSnOVRJ6idgvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5a63e91.mp4?token=BKvOgcMBKl2CF14E7vCgYbWJTuaXpOsRjJFkSSAl5bHD7DrGa-uvgX0xKMVXxWln1fRjddRN568dSnlRJCt5KUmpUGT5LWGoIXg4N-iiPXRqnIjUkbR8AChi_3SHfo98mqQer7Xx4pKN_nruv-W-t5eY91TTv-U-X9Kd8O6EwM8egdxqtVq6QlT5kqoN3BblXMlxV5Zt0gCMurBJhYZKXMNm2ftHx50NAg24byC09mI7jzZqTm-ZDclloTtrVks_ci2_pKwtyVssXNPLr_yNlhrF-_n-7yIneRcd8vRarboRsepiFBTkEuEec6NEznSRBqXtOV_ONGSnOVRJ6idgvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریای خزر تا فردا مواج و تعطیل است
🔹
هواشناسی استان مازندران با پیش‌بینی وزش‌باد و مواج شدن دریای‌خزر، تمامی فعالیت‌های تفریحی، صیادی و کشتیرانی را از صبح امروز دوشنبه، تا بعدازظهر فردا سه‌شنبه ۳۰ تیرماه ممنوع اعلام کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/451325" target="_blank">📅 08:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451324">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4665c76a3.mp4?token=SPClbd9CpYFr9azQM4PhTmauEEga35cpYa4ShSzpZ9AHdq-Z6sJxtJEF_K--bAVcbNb2QsVD_AV1KtrYJqX56jQ4TyFxbPE7-qBvD7gMOoJSWNo2zDbiTSjCGKUL-ssoxK-pi2Ey4TXl5uxYF0vj6_qAU8qcAVHcKEE_-AuFK9PAPbMNd8MA7r7yPIUSLOhx5vOOX_Z2oHK4LfaK_C2zD50Mpr1WrBe0FnuCMGp3hdtmWiZtWPqPAtXEtI8oFkG_wuHzxriocu3PgN9R0N9uAQk6hudUfJxmp5V4c1dG0qFgYOnWupPmmMmKWKagOrGKBA4R5rFOw0UdiObtbhA9WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4665c76a3.mp4?token=SPClbd9CpYFr9azQM4PhTmauEEga35cpYa4ShSzpZ9AHdq-Z6sJxtJEF_K--bAVcbNb2QsVD_AV1KtrYJqX56jQ4TyFxbPE7-qBvD7gMOoJSWNo2zDbiTSjCGKUL-ssoxK-pi2Ey4TXl5uxYF0vj6_qAU8qcAVHcKEE_-AuFK9PAPbMNd8MA7r7yPIUSLOhx5vOOX_Z2oHK4LfaK_C2zD50Mpr1WrBe0FnuCMGp3hdtmWiZtWPqPAtXEtI8oFkG_wuHzxriocu3PgN9R0N9uAQk6hudUfJxmp5V4c1dG0qFgYOnWupPmmMmKWKagOrGKBA4R5rFOw0UdiObtbhA9WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ لرزش‌ زمین‌لرزۀ کرمانشاه در ۵ استان احساس شد
🔹
لرزش ناشی از دو زمین‌لرزۀ بالای ۵ ریشتر کرمانشاه، در استان‌های ایلام، مرکزی، همدان، کردستان و لرستان نیز احساس شده است.
🔹
سازمان مدیریت بحران تأکید کرد که این زمین‌لرزه‌ها صرفاً پدیده‌ای طبیعی ناشی از فعالیت‌های…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/451324" target="_blank">📅 08:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451323">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎥
گزارش زندۀ صداوسیما از تبریز: صدای ۳ انفجار از غرب تبریز شنیده شد.
🔹
این اولین حمله به تبریز در دور جدید حملات دشمن آمریکایی به کشورمان است.  @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451323" target="_blank">📅 08:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451322">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">معاون امنیتی استانداری خوزستان: بامداد امروز آمریکا به یک نقطه در اطراف شهر بندر امام‌خمینی (ره) حمله کرد.
🔹
این حمله تا این لحظه خسارت جانی در پی نداشته و اخبار تکمیلی اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/451322" target="_blank">📅 08:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451321">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
همزمان با کویت، منابع عربی از وقوع چندین انفجار در شهر منامه پایتخت بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/451321" target="_blank">📅 08:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451320">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
انفجارهای دوباره در کویت
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در کویت خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/451320" target="_blank">📅 08:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451319">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌ کوزران کرمانشاه دوباره لرزید
🔹
به فاصلۀ ۵ دقیقه از زمین‌لرزۀ اول، پس‌لرزۀ دیگری به بزرگی ۵.۷ ریشتر حوالی کوزران در استان کرمانشاه را لرزاند. @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/451319" target="_blank">📅 08:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451318">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در سیریک و خورموج
🔹
در ادامۀ حملات دشمن آمریکایی، دقایقی پیش مردم استان هرمزگان از حوالی سیریک صدای چند انفجار شنیدند.
🔹
در استان بوشهر نیز صدای ۲ انفجار از حوالی خورموج شنیده شده است.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/451318" target="_blank">📅 07:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451317">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">زلزلۀ ۵.۲ ریشتری در کوزران کرمانشاه
🔹
ساعت ۷:۱۳ دقیقۀ صبح امروز، زمین‌لرزه‌ای به بزرگی ۵.۲ ریشتر حوالی کوزران در استان کرمانشاه را لرزاند. @Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/451317" target="_blank">📅 07:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451316">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">زلزلۀ ۵.۲ ریشتری در کوزران کرمانشاه
🔹
ساعت ۷:۱۳ دقیقۀ صبح امروز، زمین‌لرزه‌ای به بزرگی ۵.۲ ریشتر حوالی کوزران در استان کرمانشاه را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/451316" target="_blank">📅 07:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451315">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
آژیرهای خطر در بحرین به‌صدا درآمد
🔹
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/451315" target="_blank">📅 07:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451314">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
آژیرهای خطر در بحرین به‌صدا درآمد
🔹
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/451314" target="_blank">📅 07:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451307">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌
🔴
قدردانی سپاه از اطلاعات مردم اردن؛ هواپیماهای بزرگ ترابری C17 و هواپیماهای فرماندهی کنترل P8 ارتش متجاوز آمریکا هدف موشک بالستیک قرار گرفت
🔹
سپاه: مردم شریف و ارتشیان مجاهد اردن، با تشکر از همکاری صمیمانه و اطلاعات دقیق شما که موجب هدفگیری دقیق رزمندگان…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/451307" target="_blank">📅 06:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451306">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دریای خزر تا فردا مواج و تعطیل است
🔹
هواشناسی استان مازندران با پیش‌بینی وزش‌باد و مواج شدن دریای‌خزر، تمامی فعالیت‌های تفریحی، صیادی و کشتیرانی را از صبح امروز دوشنبه، تا بعدازظهر فردا سه‌شنبه ۳۰ تیرماه ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/451306" target="_blank">📅 06:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451305">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0J-v2CQNFPJNkrhC-xaNhg5wQLD64Rd_TNiGErggRtJqt51y3YK5wqmN4gpB0BK19-c7T-qqHMQXmRmJieNeMeV3r06wdcmj2g_pskEVkYCLMIMiGdUmUqOdQBed3c1-P8Y_4OoflT0YTMZejxydbvQnOtxsEJSuK7aN6L41ChJ6dnZUb1qLVa0vt_7w2tuoO7Osq4rPiwMjbwwzfhJz7cjDqClEl7LcvuwQKe8phTE8B_C5-80ohsZSQW_34NoHdqOxmC9Ze51aupJFF3-nOBCN850omGj5AQgDgTMjFozHFXTQt98EJ885qEedlJNytSM_Z8GIaTZQmR-xc0OvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من، معلم زبان انگلیسی رهبر شهید بودم
🔹
من که روزگاری سرهنگ بازنشستۀ ارتش شاهنشاهی بودم، در سال ۱۳۵۰ معلم زبان انگلیسی آقای خامنه‌ای شده بودم؛ کسی که او را به‌عنوان یک روحانی «روشنفکر» می‌شناختند.
🔹
اما فقط این آقای خامنه‌ای نبودند که درحال یادگیری بودند؛ من هم از هر فرصتی برای بهره بردن از محضر ایشان استفاده می‌کردم...
🔗
روایت‌های این سرهنگ بازشسته از جوانی رهبر شهید را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/451305" target="_blank">📅 05:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451304">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
خبرگزاری فرانسه: بهای نفت‌خام برنت از ۹۰ دلار در هر بشکه عبور کرد و به بالاترین سطح خود از ژوئن (خرداد) تاکنون رسید.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/451304" target="_blank">📅 05:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451303">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌
🔴
سپاه: دو نفتکش که قصد تردد در مسیر ناایمن تنگه هرمز را داشتند منفجر شدند
🔹
اواخر شب گذشته دو فروند نفتکش متخلف که به تحریک و اجبار ارتش کودک‌کش آمریکا قصد ورود و خروج از مسیر ناایمن و حادثه‌ساز جنوب تنگۀ هرمز را داشتند منفجر شده و از حرکت باز ماندند. …</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/451303" target="_blank">📅 05:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451302">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
انهدام یک فروند پهپاد MQ9 در آسمان اسلام آباد غرب
🔹
یک فروند پهپاد MQ9 با آتش سامانۀ نوین پدافند پیشرفته نیروی هوافضای سپاه در آسمان اسلام آباد غرب رهگیری و ساقط شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/451302" target="_blank">📅 05:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451301">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">معاون اجرایی رئیس‌جمهور و وزیر نیرو وارد استان بوشهر شدند
محمدجعفر قائم‌پناه، معاون اجرایی رئیس‌جمهور و عباس علی‌آبادی، وزیر نیرو، پس از بازدید از مناطق آسیب‌دیده استان هرمزگان در پی حملات اخیر آمریکا، وارد بوشهر شدند.
‌
🔹
این سفر با هدف بررسی میدانی آخرین وضعیت استان‌های جنوبی کشور، ارزیابی خسارت‌های ناشی از حملات اخیر آمریکا و پیگیری روند خدمات‌رسانی و بازسازی زیرساخت‌های آسیب‌دیده انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/451301" target="_blank">📅 04:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451300">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه دریایی در نزدیکی سواحل عمان خبر داد و اعلام کرد یک شناور در شمال‌غربی منطقه «کمزار» دچار آتش‌سوزی شده است.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451300" target="_blank">📅 04:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451299">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd94dc223c.mp4?token=fVe7HkfGToYL5H6Ui7TUScU6h4RU50PQlWCR_1XheIv18JREY3xzU6KqBVWyPQLh61TBg6WTC-fC_vbUA7MoikDsbh-ObU7jGajChNadymvQv64_oUA_N7lb8Yo8gJqLvQZHv35QilANVOCQgdFd7SoeHXtQv2lK1ZUiD6SfsGIwg2VvoT6hWO5MqjPbm3dac0vhwwO5R9_fi--R1KBjuh4ZeolGR9d3w5CMLlF-vl6RC0wFiITKGERa7K1YRM2CrqR1ucKVNB1QdaRS1gsvCphe8P7NY7MlpZdSUwpzMP5uaQXH1RAsQEN56BrKel5jpYsDPOp8k3hAK_dPglA4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd94dc223c.mp4?token=fVe7HkfGToYL5H6Ui7TUScU6h4RU50PQlWCR_1XheIv18JREY3xzU6KqBVWyPQLh61TBg6WTC-fC_vbUA7MoikDsbh-ObU7jGajChNadymvQv64_oUA_N7lb8Yo8gJqLvQZHv35QilANVOCQgdFd7SoeHXtQv2lK1ZUiD6SfsGIwg2VvoT6hWO5MqjPbm3dac0vhwwO5R9_fi--R1KBjuh4ZeolGR9d3w5CMLlF-vl6RC0wFiITKGERa7K1YRM2CrqR1ucKVNB1QdaRS1gsvCphe8P7NY7MlpZdSUwpzMP5uaQXH1RAsQEN56BrKel5jpYsDPOp8k3hAK_dPglA4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سازمان تروریستی سنتکام: بامداد امروز بقایای جسد ناشناسی را در محل حملهٔ موشکی ایران به اردن پیدا کردیم
🔹
در این حمله ۲ نیروهای نظامی آمریکا کشته‌ شدند و یک نفر مفقود شده است. @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/451299" target="_blank">📅 04:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451298">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3415729dc6.mp4?token=CWjjGqGgwiCKUtl4j2RJG_EixSbsaOJb1zPUpGGFhCVnL_QuHA7DACujUTxqSfyIey5tgdAv00Rsg2S8VAqaXlU37Z34Tzc-OOXc-31dkScGoYLdSXXuR4_41swvhBfqC7kkUXf6du0tvKEdg5BGi-s6veDYuVjX2fR2Zybr_1B4tNKmGXsUhzgc88gkt-m25uz9HqtP1MfzPhOcydEcKqSPfjfDC0rhMNx9MZwvR06TC4UVzUZO2O9ys1tW8sVSZakB8qfyXqIY8vQWEZkRY8HhnJU3D5MQ30m4xv_lPtd-ern-QeXaFYYpUsS5-eL5d3BPYzqyuxclHuY5TS7ucw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3415729dc6.mp4?token=CWjjGqGgwiCKUtl4j2RJG_EixSbsaOJb1zPUpGGFhCVnL_QuHA7DACujUTxqSfyIey5tgdAv00Rsg2S8VAqaXlU37Z34Tzc-OOXc-31dkScGoYLdSXXuR4_41swvhBfqC7kkUXf6du0tvKEdg5BGi-s6veDYuVjX2fR2Zybr_1B4tNKmGXsUhzgc88gkt-m25uz9HqtP1MfzPhOcydEcKqSPfjfDC0rhMNx9MZwvR06TC4UVzUZO2O9ys1tW8sVSZakB8qfyXqIY8vQWEZkRY8HhnJU3D5MQ30m4xv_lPtd-ern-QeXaFYYpUsS5-eL5d3BPYzqyuxclHuY5TS7ucw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در سیریک و خورموج
🔹
در ادامۀ حملات دشمن آمریکایی، دقایقی پیش مردم استان هرمزگان از حوالی سیریک صدای چند انفجار شنیدند.
🔹
در استان بوشهر نیز صدای ۲ انفجار از حوالی خورموج شنیده شده است.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/451298" target="_blank">📅 04:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451297">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQHjbQQUBU48qYpMfeVe0gPSh4IbMYh1jzrixBRmw--WE3a4-hNubfz6-U61IWBY1Nd7ZrbpySnDsKjvfOPLvefdlxrBecpI2UXg4lHiVriBxhbLX5qUIZtIs4FcogNRQadFXnAsx4bgU-hVRcx598yCvXaq5TNj0Ne6hZ8EV6lEx7Ap_kjxb2x9KaQvPkN3ZqncgUHMeUjZ_PjtR0FYXjpqSSlOpV3lolRFEbHUf0iPZQ0RGRnjSP_-zNboTTz6_CzPjC1BwUZmTkC4IErItM42feKIikBmVb3N7nlcTVxri9WJqd90GFgf39I0bZg4e4W_JTBK_lOvk8inJKDzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: امشب ضربات سختی به ایران وارد کردیم
🔹
این کار را برای ادای احترام به سه میهن‌پرست بزرگی انجام دادیم که احتمالا جان خود را از دست داده‌اند.
🔹
ایران متحمل خسارات بسیار سنگینی شده است و نمی‌تواند به سلاح هسته‌ای دست یابد.
🔹
دیگر تنها به جلوگیری از دستیابی ایران به برخی توانمندی‌ها اکتفا نمی‌کنیم، بلکه اکنون در حال پایان دادن کامل به این موضوع هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/451297" target="_blank">📅 04:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451296">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca23ce1378.mp4?token=eMU53WFnzoVzx0kjrJU0lTsxsp-v5Lruons8lbIS9z6_Pf82IF1TI3drNBEmJfw947T62l_xsLTh0F5RG_i21KOd7WTlLiHipnhjrbJPflLYrbD8fZ7FiNYDWQnbN7Rhmsk4lHuVNoxJcvIdd5mivfrBjYGmMnfXSnU3PAcydikXtHGvm1fSgXvoQHGPK8RMSqUQgtQ16wROgswYpx4OBIA_Xp1I0H2pVCpH7dJcvU2QQUZTKrLd3Binz8fGN0k1XTkEF709sCzxdQDAf2XrRTyyn_qf2wAva26mHP4qbCdARsuRkIh4m-FY30LbxmwTc7OMK7b7NBjLyDk8SpjiEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca23ce1378.mp4?token=eMU53WFnzoVzx0kjrJU0lTsxsp-v5Lruons8lbIS9z6_Pf82IF1TI3drNBEmJfw947T62l_xsLTh0F5RG_i21KOd7WTlLiHipnhjrbJPflLYrbD8fZ7FiNYDWQnbN7Rhmsk4lHuVNoxJcvIdd5mivfrBjYGmMnfXSnU3PAcydikXtHGvm1fSgXvoQHGPK8RMSqUQgtQ16wROgswYpx4OBIA_Xp1I0H2pVCpH7dJcvU2QQUZTKrLd3Binz8fGN0k1XTkEF709sCzxdQDAf2XrRTyyn_qf2wAva26mHP4qbCdARsuRkIh4m-FY30LbxmwTc7OMK7b7NBjLyDk8SpjiEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ صداوسیما از تبریز: صدای ۳ انفجار از غرب تبریز شنیده شد
.
🔹
این اولین حمله به تبریز در دور جدید حملات دشمن آمریکایی به کشورمان است.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/451296" target="_blank">📅 03:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451294">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های آمریکایی کویت خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451294" target="_blank">📅 03:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451293">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه دریایی در نزدیکی سواحل عمان خبر داد و اعلام کرد یک شناور در شمال‌غربی منطقه «کمزار» دچار آتش‌سوزی شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451293" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451292">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در سیریک و خورموج
🔹
در ادامۀ حملات دشمن آمریکایی، دقایقی پیش مردم استان هرمزگان از حوالی سیریک صدای چند انفجار شنیدند.
🔹
در استان بوشهر نیز صدای ۲ انفجار از حوالی خورموج شنیده شده است.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/451292" target="_blank">📅 03:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451291">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
رسانه‌های عربی: انفجارهای شدیدی در امارات رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/451291" target="_blank">📅 03:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451290">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در ماهشهر و بندر امام خمینی
🔹
دقایقی پیش مردم در ماهشهر و بندر امام خمینی صدای چند انفجار شنيدند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/451290" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451289">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در کنارک و چابهار
🔹
دقایقی قبل مردم در کنارک و چابهار صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/451289" target="_blank">📅 03:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451288">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سازمان تروریستی سنتکام: برای نهمین شب متوالی حمله به خاک ایران را آغاز کرده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/451288" target="_blank">📅 02:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451286">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd98ab8a9d.mp4?token=ef3MFq6AltGHVF7_yt0HNj0hz3dslrBUjmGPDRlGA3AifeEDw9TT5texkzGk2etbksAp2_q8IHp3E7D79OK8QG7fT6Bg0pfG65cOPfUGCxWW3rKCbgq-7wInel8XkfSBq933UgGQ5cfJS1L2mx-3hUIY_fXxvEJsmcPm_wQYguOeRveQGzJAkwbbm0LrlL_KF14D-qkN0oYZmGGxVx162yS2QFFnhP1nJAgbEuqskmZHiEDzvPruqsx2-5CFchEwrbBhud1Nvf_6jDNwA7GSNZaFYbrwDJAUNtCsuyTm7JJLnT67XBpZghyIdQnoo1VThLbJXP6_qnmN2AjUAkJ1ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd98ab8a9d.mp4?token=ef3MFq6AltGHVF7_yt0HNj0hz3dslrBUjmGPDRlGA3AifeEDw9TT5texkzGk2etbksAp2_q8IHp3E7D79OK8QG7fT6Bg0pfG65cOPfUGCxWW3rKCbgq-7wInel8XkfSBq933UgGQ5cfJS1L2mx-3hUIY_fXxvEJsmcPm_wQYguOeRveQGzJAkwbbm0LrlL_KF14D-qkN0oYZmGGxVx162yS2QFFnhP1nJAgbEuqskmZHiEDzvPruqsx2-5CFchEwrbBhud1Nvf_6jDNwA7GSNZaFYbrwDJAUNtCsuyTm7JJLnT67XBpZghyIdQnoo1VThLbJXP6_qnmN2AjUAkJ1ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن قهرمانی اسپانیا و شکست آرژانتین در ضاحیۀ بیروت
@Farsna</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/451286" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451280">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehq-Xy7jlXGKWLj_DtoLFl-w6u9pMiljHXeFs70vABg8-h3Ob-UFfHqP8QJ_2V9yBRgwTND4N2Tqa4TXr1BCxWzkPXLKb4oHIL7vL4aQ_GAtkusD6QzyEi11T_iyUVxQHIw-Y0f8bOfXca1su07SbhMrpCE9yJDNc1JqahQFVjCxiajqzVZvohUfLXYXZAhHrERr3lJmiEpD6Lq2J5-gR41Wop3h6l5-m0i5jErvFbHjB2JbypDYMOp4rWlY23p1X4qIdie2o0qzMXJaMfNQDV_XhuGpbMX9A2eXD8SI5NNCp932Jl3jO6q2QGm3v3rQoTnxQgdBZUFln6AcGKlMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJFc6JU3q1u4F6HWVd4guS1OEcqR1QNg0YF6v_CPUllM0dI0qLZePoCUECHfiOfSiqmLl6IV78CYCw2_vXVdKhHXFACHTmpvTaK0Gt-z0KJ5PvDm0OoMBdYsobc7Pb0_JSk_KDPDZU3jj2Yn7-2NbLztc5Mo5nxi9DbsuwXCNz71dofMymi1mWrIXE4KqQ6q45zYCTCYpSaV7p2_NinP8-JX7KGf6J-6f1brMiB36pKPZWrTMNEpn2Qw_89Iu6QBrwOHZA2OwmoAl-O_RwB-wXQK5wIO7qWZlECWYl8-KtLtZxkS6aaz-2nD6JeF36n-gn66Ow75sENEftJ7GFyknw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVwxoZovyMm7hhc-kN1240tRpa-kELgub6VADmsnjHYcBGjLQxMhflu8Ps8y6PSXZoCAtxQvsJUR9QdtdoK6Hg4zG9TcQFoEQFGZPubAAl1ilGyfzIgmQVQCqJdFC8n0lo-kgxZXnYSAr7aTU2fs6f9ev9nhNSBN8UhUryTF9xGVcUa9C6IC3XgtYMTqZj5EGrJ6aD_f3QcVaIjoGBI47KvNw_GtNL5LwG_HzKV6TQDCv7TLNKDeTgpZjEhOmFs5vGE2rOgDQBWSgZJph_40Nou5KVPC5eEDEFzubBZnHvO2QX6sWEWXmRwSHNExiPIBaIYv1K2yY1F7s9l9uayPNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKDp7zSbBSMp5j04C9v2vxoMIFP9rZ_A_i6YyPZFmmQr7Cilg6HYvbWCRqSfcPgaSHUuEC-zGf-mOPqQmakdh-ejmcv5grICDJaFCMQTT3jlBv8nco9VYdkOMgYpePqtsP1LJMZ-WkLpTR9vkt4WTJvwljhmOez4NJSEPG5xEmgKZH-kRFwEI85GF-pBlfAfbSpnHxUcA-rhW85hAD2oLHEKEUBqu0GJBfryogBrnOufJ_adAq9ZloKOPThIjEThDT3nDDg3rTBAFiFH_xPp1RgGM-LEci2942zMVlvvFyzquXAOsSxSy1wkrAoi7-kF3PObQtm1RQB5hW-oVRGYpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPnESLkWsghmtTNZ5Dm1cNOfSerQeWXbF8YPCy2WMEDUI9YFhdCVPwLDElvLhbygBnaPk6ZbVAmINdvLLWORfdzYFMyevxHSj_3U0lyHLWpPASfTGEEepYEFIOGBM_766A5Yym856rZej_5aA7shnWqlu2FoXOn9LPsCPQBv0Pm2JsBa8DNZmUPpnaTjJipIw7J7zuLfOawBCSYTYQs1_fhNK2DcKHeZjHWm86b-gCEfjmxO9hNY5Cvcn9hZ-yPptGYKWpq25CxlUovce62oZ-BaFxsMqmGOtNtW79Phexcg3SbG4Llcf6cOCBwQeHEhIYH39_oBLOgTRG6H5YWcGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBatjrOdPwfS2LLY-wKamv3FtzlNGI-WmU5p4AqyhonDD80HK5xmpXYwL2u57uAdc9kPi7JNH2xx1g1SMduOSWOad4orMRwAcl0UkO13D50s7smCnPMf39wS61Ia-ks4SpCahWYwS82GfWe-H9209GO0AdEwlcXYCkkJgAZ189TcSKgyHaNINLoLZBfYRdoIh7S8-ivYoMktshsXN5te9XSaMbxV1S84Oumcn8nolMa5law8qjYZBaPKOhN9AXhabWHdlbVaneZqTDYSlWhhXUH6XLQ1CaK7Ze66cKrPbCb4rLJ1ytoEBhpM0gqaTmUaGpKqVzLJtJEnBRXgucC0BA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سرخیِ پرچم‌ها در صدوچهل‌ویکمین ایستگاهِ خون‌خواهی رهبر شهید در شهرکرد
عکس:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/451280" target="_blank">📅 02:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451277">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CsST8N_GSG91oAcQ7TMOZXp-WQkBNXx6aI0epGPTa7LFzMeSDXyMm7U0Mj5y1OEyXOjZ8_6HEbUiV5TIDJkRkoLSlJBkmaHHwmgpm-2-YAPpu3uVWGhYbx2paRvI5WQSlWvGH-TfjO8HpoSFY4YLe46E7qAwaSPlUAuubI6J12dtafIk3Yf1SaVpRvuvDHQ2wDW4ezN6N8ktdTaX3rH6VEZIlFRP_vEifS3nJjJwms2KKnI0eyO8_mQFMzMaotVVx_JP3Is3du-5YJZa_GoxPhAFSGcFYw9NYPcVyFTBjMQgZyQQKX86Glf6tqVmQtPbBR5zHL_gEQwQLXjbHJV73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FBvQw6hlQMsjxV1SaImkvonxxpE-Qp2sN3y4EN5y_8Oo_wGisADC1edGdYb-hVa1xcJm8p2t3Yu82slxxqcljLEzcvpliKccpswcFpJq9uEmXKnufM7xaSOtQX9zJtPL5_AnHDgkSodet9RReVbgQQYpAB2CkvsJ0ArJ1M3ZtZXQRAkUPEymc_dG2jplbETzYUbfuFv-h8Ops2wV_IjGbAB8AIdJ5RNAABaiUoJ0PgbPutsua8Y3U_C2h1vC8NtHiPGrahIQH6MPHdcc8Z_xAWUMZtXDrxnjf7JPyhttoxmqsFd2i7Tb2xMkLpRWai9raBW69tvtbNe5zaHs4X_BIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQkE8qdU6atXUE4baVVBnIPSVfbfIXyiRZDPM0fJK8QEEmnwvXpRxOKIMV8UoBlUbGugAWtkCFurwsmiADRdFnEoBRHFBzTy0tkW0Ch5Mezt01S-lTfV95_0HvUbmafbG7wx7KDRwaUE68uWyCeJMQNr9R0q22pExRLyjH6sRmWZPa4CoMr33B-kXbC690qA6kofD8-EP-o4LjYSCXg0J3G7XxRNa5HkA5lbI1pBMZjjvz6RuztSsJSIjgTSkRWyVCq4iz5p2uOmK_q_TRKofNARQeTnfEd98F4WR8xFKRB9atSMejCp1-s-kGhvgqeHzQbcY_5QYvMX2ewGuppmgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از بالا بردن جام قهرمانی توسط رودری
@Sportfars</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/451277" target="_blank">📅 02:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451276">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‌
🔴
منابع عربی: پایگاه‌های آمریکایی در بحرین دوباره مورد حمله قرار گرفتند.  @Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/451276" target="_blank">📅 02:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451275">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
منابع خبری از به‌صدا درآمدن آژیر هشدار، و وقوع انفجار در پایگاه‌های آمریکا در بحرین گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/451275" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451274">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f565906dd1.mp4?token=YR-Np5S2ogJWL9WESXvZmWKS3j8NFuVS3P1Nj2vQyUJuLAeA8jL_4hmNi2aPust01c-xZG4x9C0z7YqVZxnIN0QkPvJEbi0QOwCpKi-QZC8srNG4lbz5Oz7qZ3wbzWrJOsmzCmp4jpDl_mLBJvg9dq9y2a3-f_FHvzO4PIRDfw2-4W2ByFAA0UvvYw5gCEx3I2JLqQJYVXKVv6JGuT0I-T_6fEgY3s6MmcT4BBrWAvXQZUFcNDfo9z9CUxzS5V5YfmdgV1Hh74cPBFxWoLc1FhtNmULSN4LDfYzn0utN4ELigf3MDSdYb5c1xvcdnodqyTFeMJ6Fbxj8jfrFYpsfrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f565906dd1.mp4?token=YR-Np5S2ogJWL9WESXvZmWKS3j8NFuVS3P1Nj2vQyUJuLAeA8jL_4hmNi2aPust01c-xZG4x9C0z7YqVZxnIN0QkPvJEbi0QOwCpKi-QZC8srNG4lbz5Oz7qZ3wbzWrJOsmzCmp4jpDl_mLBJvg9dq9y2a3-f_FHvzO4PIRDfw2-4W2ByFAA0UvvYw5gCEx3I2JLqQJYVXKVv6JGuT0I-T_6fEgY3s6MmcT4BBrWAvXQZUFcNDfo9z9CUxzS5V5YfmdgV1Hh74cPBFxWoLc1FhtNmULSN4LDfYzn0utN4ELigf3MDSdYb5c1xvcdnodqyTFeMJ6Fbxj8jfrFYpsfrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهالی تنگۀ هرمز در شب ۱۴۱ حضور در میدان خیابان: وای اگر خامنه‌ای حکم جهادم دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/451274" target="_blank">📅 02:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451269">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2j0gxlxmOAHndleXr9hKw8Cr-au8oC7XkSPAqFRevlAHzh6e0WmkP4c1qTFtfAXoCnyE2K5IS38i5zAZ8-nhEf9sy6zNyXBzJNz_ELV-T6DoEwc-TetpXr_gBkWwWqwNYzmtHVWGcZneytCpkIzlQb00zci1MJNJ20CQvQb2gJOU3ZWN_a472JJeUqmgXUwymGYLCfJyLCRWyuniAyNROpn5mJFOrhhF_uGrIS1PvQEigPeH_MPuRJm5TQTIoPFYJRvbUC_KbHWIMpbH_wvX49Bs1T_eaFNbskRGyVPpLJ8l2-bvay6igUGuHEh3yIDd3QRJi8Rv9uEPsIoGiVysw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_FBNM8WOOmVHBPpD20UvH_OIPQ1mGFUTXAZjyOecGtoYghoPoVebi-VmhLwrKodOImcltjHvHmQTWEYUVILlMYMBTWEGL98MmB4doaPS7EHbI7b_kUq1kvi2ae1_iGTTU4nRWwQ6QrOGE_xpma0CU-d-DU4ZavNBURT7rINGmqiMEUWZz63fWi5dMcu-P0ok0i9ZoYd3lIw95VyxjVsBwah1d1i2UrHMG7bXNbI4S8tfUyIyKCZOaPkbw9qSmKTWPT1vHUS9LPgpKozEpC8r9ajVHoEo397u2zgw5fnPSaMLVAg8JOCpqMpdUFG4M_GI7c4wc3QR2d9rxlrMeF4tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPQVdOyX-9sNWKYZS-TbayS0vU1geuWIx8tTfa_RHzlFM9tDd8sOYRU2uneeZMfBGDYAFxPi9PFkyYsEI4lfIpkXRzB9t83WTKVfQEa0TSWqj6s2p5OlWF2yLsyLm57PegHw3jkqZyh46a60DJ34h6wuPikvrXMOM6dWg6_SSv3qCJovIHBp-z23X45O0B-OGyVcwpm_Ko3_ltlNcJ0HzNYZ-EOonCgJ8lA6bZGHBKDF7qdc5JzuD-tsD1HyLVZ0SuqVYOXYEBrr4aT9W-5Qq9s16VX2zlW6skKRoE3z9OHcyseP8roBxACQhxqydVePwlL_JfOdoB2V5zt4EQLtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quUGS5PlFYMnnPBtJJ_g2SWdcimBxcHshdr9unGRIlESiNOkkT--y1UvUAIMGn7J1qsP_iVDMdF1ECwKnwIgdLbmOcQn15ebbWKWYSR6cf2TN8nCEjrdTgaMIwVLp-Zo36e7Q7sUCLR88xiLGhYQrRsK41Yw3RxJ4GE6gXCMppu8rkHDVpS0mAo8LpOBnbXcRswEujepkRfivTa6pEh_kWCOAGsQXzlmrS32KyNtsZol1glDJ1krtRA2H2mAt7SfLS-7AGJPap6HS2i_KSsKNjoKah5XAxjt5u0R3LO8wGy89ZV7kfakiFGQp8q6qA-CcF7s9iLpytv8rZPq80QDtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8sChhu90uFPQAVQY10PCbUh4pp7D8SzlFKAnoSgl9AkTDp4K-aR9Ahni_0vWnmHtEaQG-oc8W9JYso_PhvUCCCW6SX-JkxD-9U2ueWWM4nyuG6njSo9P6k371Zgdo-124lmmyjY7r1Ui0ZMhAsZhKtNKEk-7UwIljDNuxxZ96m4Q9PnaBm3WTR9JIX4AuJ3JmaPAjCXHHAb-NrM_1Ir-cdPWZMbVquQbak2-xPznyV9Wjsr18YrTfHwBrdxzSQjOOcts0EhcsQtizPh9zSJCerME91MYqDR37W6ZqQ1vrajHXgwKTt5p8q4YXD7BOduKGgKvrSCwSNEO640smecEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر فتوشاپی از عکس معروف مسی و یامال، پس از قهرمانی اسپانیا در جام جهانی ۲۰۲۶
@Sportfars</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/451269" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451268">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌‌
🔴
منابع محلی: پایگاه‌های نظامی آمریکا در کویت مورد حملات پهپادهای انتحاری قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/451268" target="_blank">📅 02:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451267">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
رسانه‌های عربی از شنیده‌شدن صدای دست‌کم ۲ انفجار در کویت خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/451267" target="_blank">📅 02:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451266">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
رسانه‌های عربی از شنیده‌شدن صدای دست‌کم ۲ انفجار در کویت خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/451266" target="_blank">📅 01:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451261">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ILCAMEqmBphed0OP6Nt8Kuei6tSty9BEPwho9q5_61FDJeJeVC4U3YE3le_cHIKEsUDJHp8uuoDME91WOgSxVsoqdruAYg3yStfshASiZMt-y58vAOftP2_cnrnehTF1Mmgz4WL5wF60Ouk7w9xwV0qSzaahMtV487ieaAzS0BvnxQ8DeK50KnfLqMhYFLTvr0I2Mn1YWz4zoKei5Yie8e6UeXOgf2CXD5EDK5mB5LfXfcjUmKs3gYU6iOEsyz9Yg4oQDL0BMQ3wu7S4bZ3bOJcU1egaSmiY7fdYiQ1U8LntvSuoYGGI-39AfhcE7Ms5XNUI-N26lUQ0TCIqHDwHwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cb67WtIqFi8Y9vrT3bjj04EuFfaQ_H6O0zyy2FmhehrKGZqmFAJhtnl5YlhyJGbX6lCqI0RjQxyj3kCSPN7s7sXdegH9TxcS6IfPbEBUV_0FoY_0nQh1jT5_Q80lKsX7qbjXgUT5fZOI986ABPqFYbZirw7QNoQBrNemzCCk8rgGoP6HE27wZQvvDkR4uE43uiYuuueTzjjqS2yEZM7Qdu6j9QQdJJg4Xol8UEnL5ow6h4uEEnzcSnMWHMQlGNDThwXWpbegWNxqX9-bQOgauvdb9ZDJa6NZyhWEvA3BKvNO7NN_K-D-VVKeQjbBHmZTPxMqN-AznjrryVBIiYSM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pm9QBkpyucLNKS4pphciGMYrYktlm-AtOwRg9A05rYOuCvswI7l_0Ga47Sci0aSNglaCMzUHHp30_m9J47O7joBZvQWxR7kEJw8cUNMk3CXOOALsHJykzOc9eZlmRH0UbVg2q4AJO1vKHu-2DYIrJFhEw_Ds4onlCZnrEjvVPU4JLHF3heY-X1LMHhDTI3FS0eSyeuq0cpSgq5IkdSuVNqzo8JOc5WOaYYl-SGQm9Jqy69e1jJVMG7JU8dDvq44OwQhPIyyocrw6OjS_OqoKKiT2XB9SpSEr-z5C94TaldadrJlVOTZvN7UQa-wIAgFY4w8nG7Bok93sQQ8ZdA5YHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BiZZ-BfWkKtZzvyryRm_5wlTtd6t0je2jEne0uIB3QNx7-sTEGMSd98fnE1ySGQy7s2OByZSTd3G_cca2lDGnQpEFmeqTF3GRh654-6hRq9z3uU2L915Dl0EpeuynsdKuzTEJcsG1n_0Z89zPCPl6CZfsRH3bwZoU1jadKJmbQq40Z4ygqIniCG9rOduTejcN8n-DRQRIL1HEdFOy374dn4laT9mFDQBD7_VPphBQ2-CdwS8TqG2nSnkcvKV7DENq7yMcucvRfp-KAhAhSVnXQKvrr8vbgsF2WKnyWV1sYl8MRN-8jElRgXKgavBcq3Pr2rYvVu9wi-f5KA1mDXfOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMg2gTu1x_NL9Fwb6jYNhG9DSH7VciDGJWCiknH9VSBpnQ_dR-wglG3nnzd_uN9R4kgBZvzB8W_DmJ5Mrfov-JQxI5ybEGjVZurO2AqCNGapoh8RKzIeBi1ezgQ4IwSnCQNZ0jO8LcueDfGAwZ6dwNkYNPTeqUA8f3UmitrzEYbeRyPgfSbBxQssKPQ5P18XWotHq6xeQ0FwjbQaReS6a-ybmaW7K5o4xEgn4TFWHQK8LFeXflJRQT5rN9mTsK3dDh9TTNAQg7rldIJ9weQZHNNksHVPv4NDHH0TQekNt2eLqo0qby9aSYY-JXV9v1sy-boGIQrwKlXesNXZ5zCm5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۲۹ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/451261" target="_blank">📅 01:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451251">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uS67bNa3QGhbo4U5aiwI2c5nENqvoRoKd5ZfNvmqQtH00qLAYtankgbDlNsrmHPIeJUIiL3ReOilcF-qe0jC4fDSu6SX5Y9zdHDRBhv5mUzFND-y3K2f4Lup8EQFYKoPJO2yh1HL_pr2AkNf9x4hpWkICLjIkP_fXJdEQZM8x_NFrEhxvR_4pLruPca1y15AVh4JKNGuB70X7rplS8VG7ynY56yHbJ_fHBEbBJUN0AEixIn-SOuCXQXSOgycpVaacLyqbFIBwYuAftz5A-g8lyA_NiP0FvX4uJm9JXcHknaYRAfM0TFr69FRiEax1Q_M8y7v0467Ml5i7bZygA90dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-qeIzJWpUweU_AVuyZCrn3-tgx1m7kIz16xK1AzGGoWV1VrR3dXDiEAjgV71btTTQ9wHjif7BVmJFk0C1OdLxPjlYTbhPOX8EkKRmF1O-6ZJPDqWH0SPZff5lWhu9AnkED1ivrCSDYpvYEx2EGXY3HavaxwT6fWWThAv9kMdyliKQmKHyKUL0wo6nImqv0AalDd-1IdVkS-JBpS9C343tOq6xZceCuwnRUI2VbyrK6TVZKmgkUWcGMsCb_xKwFuJCNPjlKXDe4Ow6rnrHGa1RgaJFEE6Q9KtClGyQyBDS4yqBw75IMQTN7p6qteZRo93RuOQJx1CB0BqAGAKu-cuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dihOciHSBXw0bHe8Mxtd4Bw0bXsHc-3jUkHyLytfZStV7rFqr2-mHZzHLFjYFT__nX5usL0Xra4Gc5GmlOSfs_CMTQ5jSH3Zm56ZxWJ0LQyQzgfOd5Z1TudUkxxVP0vpFBgVJNSCQUVq_T2qTGTQBJf8LGrD4RSU9i3xgvNhCavLvnFe3mKsqX0Q1VUMCi5bkFwCi3cIuRyR4QrRMQUU6oBD-CwmZ3IZRCtOfGVPtHKSMjpoMVxtS3D5RETbj4CyLqkq7g7ouzKPvD0JiFXy8LYsOS9r74E8Ngfku2BuVb5VX2UI2rYXhl0YH2VCcqclhN-Pu38gsHNUBCKJmHxTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWRz6Zco5hQP54V1ZbZJMsSi_HeyauszHeuKPzkoPwzymx1PhG4xyxTS-eMgHOx7pgt9P8hEY04r9SDSaF8TucKdqdMmU8LPjO58n175WFMkJeFERAlPz2da1B6aH8f1LuN-nFskZK-edkUEGdTKfyuewd8fgntQ7RyAHbmHI4-okbbWD9BiPJ-ZLezPJzBsazEzZxzZ2b6WyusK9wQ9CF6Bofi3eXY1vxcorLSVXygeVn9u9W6iqKEto5IsXn6_8CL_pOMKdMIerk76K_9tUlOOIZ7dWeEZmE75adPCVZcZF9inSbYNLaPDNrJSUSG2B17uz41eWhuHQfu7WazSIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHnAfEpiqmETsTIDn6Qj2U-lRB5AbpICBngj3dNSL2sV6NupSVbxFtduqLmDSHQmwpIAmdyH_U3PZe348I3G9GQI6rgN5N_C027nikddxRnv2NTMSzIDeyq_V2fS1O8CNfVCD8MKocSGsxrlbf8ZLbpy-00UwBnz7NHHO6nNQYrSCB-f4_5fQRj4iD_UhbpDoQ6GBMogzZuOlgiOS34UCMyVBA7f082EatxPHyNr9eOaIEHEFvGoqeUITnsgQ28NwxjH7EKDe3nTPj5C4iPSRguWBYIcR46X7p4_fK_eWHOdLdbwcFgdPnzz4tLQ5vYTc1yLe9CrzgE8CmnrFtAdZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHWIcyVSnN2_zPGD1xHVKnHErd2huu_g5CYg8QgJsPYNJ3wI-M9bgEqURYYCfN93OYqlCwNgzQgXgV5xt8ETt1EiIk2OQeJW5dOpaKoJsaa0aSy2l1y_vtInXS2dc9ewsZNEeGWG3j8KwalB_ZltF_BI6gEk8Jc-qiX77zeHSDfkSXCK786uwosWAYEPuQswNZPOOhPMQgfGJYsDs4MflAQ_ZkExEYpTwmcfvHsa42Ttn8ne-89wLoD8Y36xE7pW4reyi1S8qQshW9tKp0FTgUAFm9FLtYcX2qdLc_IPie_8n2RhrFIl-os0YQL9PIDN3q76eOLhmPlaWoEfH8QgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elYHkwSkdiVchzD-geMaUKYcfnY-Sk73st48GOkm9NJrY2EGuvJAMGEcKlUkXnb38X7Y47jWSoidgc5734a0EbWigQLGdnmJRcLIKtytD4NBehbM8HPn9bkbzFK_lz-vzL-yiqt4XXU3QWZmiZMZXJYIE6aTtjZBh_11WxatzJ_rrEzSArubuuGgJxfzl0SKFncbzx8PeImpqbisQCFP8L2yQ19XK6wZ9OWc4-TpiLyPut4z9cqENpmVPU7JVgFvTpTNlOPqO0ymf6IDOyh1K8-BDeAPYYQl_DvTQPG8TcNffFrqC8C9bmG3nIvKlCCKoIIFIpfq8bd6Re9O-JBJlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rO2kUSf3gl9th6efJcUZmo4aR05jRKIxH7m8X0AIuBPtB4iHwdujBCK3uWC0eyrGoHPnAL7Z8jeXWxxFV8fwEM2nUYxmUs5Li2ZvPr8bTahW309f48tviN50XQIE6pYEFEg-IgR1O9jawizHOcl4vCkAwAXsqMmJdPETbhyOs9MQUFc61Bg9dY1D4zmG9uFcp6MG3LePE7cQtg5hdT8wn0t1XtRNLwfNzELGyYvZvsTGz_X-yCqHDjZTZzz-4TRhBuzxuHVnYfblh7rHNJN9p4epRdDj3Ntwb9zE6Q70UPcFaqKrdyUsbcRjkNItSxHZ8AJXVGndMutv65RTvxDIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVX5pYqpKndyCNvQbkCrZ6lMbLO7-DNaHuMVPQvKR1-QP2GFo0fdTqP_9HpMcs6KXXMc2DMh3kJjHu0SFrM35TxdVj-kxwPwdK94JQYp0GxdEMoqH2lcL5oq93He0W-cPIh1m_7RL9eRD3naY0Uj6O5fUXRuxrBX61YmTsvaZfM0lkpgxnPTkhAB2TmnwKfdoZ0WKbin5ojfHhZZiYjO7tudhdER0fYjF3hFGkFkv9W2F7zxP5QBScV9ci04OXBj5Yjkgbaybw_8atiNoRr9H1lNM7Daxye5kUFUKx4hSXHa-oUPjDE8wAefBur6CMSyJUsfdrUK3zPtwiOMngOYqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njGGWpC_RmniCkEZaVTTLjtHfcK6kZDUbU0zIZDVv_BG9OKL_FIpfRGYIGOXXEWrDRArzrBoVNdA3JfeLfY2oGVCSms0jlPH1_mrzTEBDX0dQKHFgE-cDjoh7jGrXSn30OpB20g8e_DHMTBFeEK48cp2BEuDsirF1aQZUguycKgbo1Chy2D-gJu5ZQK60yltr6eFQn4Fecq2xbLbvwoYObV29sD071BcOk0J2NAnCTCMEbIUHoJRP6N6Z39iUjM6MpiqDvXzXCRnOiGeZYxJIN9QtL0jEK01Hnk3VPzkevVdgFe1KAU6MgaLm7NyAMqUVXUuVHCx4yBsIkb9eDo5mA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451251" target="_blank">📅 01:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451250">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCaO1OryniJKRSFWg0grFT_KmyDIdWJO0nX4c_bny-OGvGFzP6GS7-8B6ZdAkxgZuGMrnRmokehk7ZvwLu3J8rsJL8rinFZE7Rm-emJiNydCeN_jOYlK4xjqxx_X6RvLOvnev3aFMwxkDhnyizKzCME-bptWAZ5OS6Ue3qVr5wzeGo6yN362MGHIuD0eaTYw_3SRCR98kMUxc7ulpFJfEvWXVkX3UbBifMMkJSEYSrFUYdE8jR986Bq_6W8drnSRqirkHfchpCK_jvhekIqRoaIxiWQDpjCKCNbUWj2tjBzrME_pT_wY3mh-5xf2xY0M1IeVIRd4BAs-nHQmmdIljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پوستر فیفا برای قهرمانی اسپانیا در جام جهانی ۲۰۲۶  @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/451250" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451249">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxT0BsxPxMEp4ZpB8qdDs67CEU1I3ufPmtN30Z3RIzWK-1F5ABD-nd2OxaiELJAUuRTJA-90Uz5h5jDl_fDVigF6TLN_jAdfTj3EPw38msD1cLQZNc3wVXw8_bjBvTYnIgQO9rl9CHgwde_3yqH-SDcPNPv2Sc2M3MWOuIsoCV51huajh77fWLrvuTTqXbaY6KtNbGMQMgIHR25x404ChLZAX5okVSN7ThBBHLsUpy_x0EFGIt2TsNTF6Xwb4cT2CUC5TNuKGL7ebdkfa0tJ9Yc3xZUMJoiXFAvyivA9MMywfP-gBLkR1yjjX3_CrtZq1hWQ-pOIoTa1W_6--hOmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
یامال پس از بازی مسی را در آغوش گرفت
@Sportfars</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/451249" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451248">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1NOI8LZDVhChIWIy5iw3Dc0UFI8ZgycmVgLZwWSNRnMgb0zHeLHOzZvF8fvChBWKmw4v5uLmxwxVMKZSUoZGqNUDdwy4ElI-fPeuNu79cgG3FarIQ9GMXVnIaRl2eQzGejFEwG8jDDJv0gPR3dNKcpJDEIzO97vK2mt-wRuxeQg7waVpT8seQHvKT9_v8XQWPsJLwLTAMYGsPDtGlTp1P4DZY0VDKwnGZHh9ysPlxz8ftiCYQGagt3ttrfJIThmQP9KIELoxVG4v0djtQDiTHvN04uTd8odHQ4BndVUNOPdftoBO5l4k4KmMF5KwQ-s4PHJnZk0DxlOEm2Fmg__GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حسرت مسی پس از نرسیدن به جام  @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/451248" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
