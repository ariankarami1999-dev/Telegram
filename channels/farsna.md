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
<img src="https://cdn4.telesco.pe/file/WdwJDQpNa2na9MkaJY_OqkXkM_ayQOd24J0OjA5xB55kpr-MhT0aKK3VqlHcOCY-UIf2ow5-OD_5a7iCeQZrEsdUvl6veTTf1IC9lRwAfG_ln1UlU_SipQmT745QV0aJSxpj6gDNBtnNXiSPG8Lx4qTiJR8HujMyT_A1bQ4fNvcM_WITAkttvS1fP30jAWu9ZxE2xjTU5r46kh0Orub7xeaj-kO2DjRrZCZc5MHgPpMS5queKJrq1x3W6Y2h87wwlZtnCq_YR9PpoEOYXGLmWeMD25EK6iDc-2RzHa79QPR60jm_75fUzRKCSDq9KlruMLiU8EZgOsZzZc_swY-_3A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 05:15:07</div>
<hr>

<div class="tg-post" id="msg-443931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIhjP9-wCh8f4_iJRGqxHuXASiltr8B935w6nX6o8NmjM6leKZCb1yICDUIj3p4YkiaT6P_c5Z4PWX725Tob17w9Fp6-FslDtfS0fSs1X4BX76FI5BFKScTu98hjAVEBPSfNF5vtayg03JR6Pd7qCS8v2fPVZIHek7AKFVuq8mkqtq6RuVEGpDrELQeeLiBQOnix8dn2bXHXwg4tcmOE9mYt7UvNavwQ5bcLZcgfdT6BvtsIBqPLa-iwlSjJurLgZL8F9rJX80_IFN0LKZ0UAB9fGp6azRNcY1upZj1FEdXzvCIHuKaHQp9Q7scpMHBdvoGueJJBIDkobp5nOpvmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تشریح نتایج مذاکرات روز گذشته توسط وزیر امور خارجه
🔹
میانجی‌گری خستگی ناپذیر پاکستان و قطر باعث پیشرفت های بزرگی برای پایان دادن به جنگ در لبنان شد.
🔹
همچنین تحریم صادرات نفت و پتروشیمی تعلیق شد، محاصرۀ دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد…</div>
<div class="tg-footer">👁️ 785 · <a href="https://t.me/farsna/443931" target="_blank">📅 05:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOn1UY8_Bn1wZzOYtu0qFpSdv9z8UK-0lv1Fc3yN3a99dHm033Fjyf3Qgh6JT3xCzbXLN4uwO0kOYHQj-vaYUZKQXkd3M_R6jGv2IC7pmeZ7yHwDVj0ss-aZHvmKNvz1C5fTpZ3QhHjP8s_nIrKAm4aJzJ7rPTsuUEIqXulEsvjXeD-1m9XAC235Zl-huR1H9jDBH9wWgn7hIuTuIQckBUC0sW0bBiZpqD4OOVaqwcVbA0eIxhJa7icNZQvSPn4lj1U_zw7nvEML8lKX-QHuADxXOnqO34k5_v_ilewWv3jMP9SDPRbFZdWV99tha3wCqcHvKGTVg_pnGLCXKtoGKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تشریح نتایج مذاکرات روز گذشته توسط وزیر امور خارجه
🔹
میانجی‌گری خستگی ناپذیر پاکستان و قطر باعث پیشرفت های بزرگی برای پایان دادن به جنگ در لبنان شد.
🔹
همچنین تحریم صادرات نفت و پتروشیمی تعلیق شد، محاصرۀ دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعۀ اقتصادی ایران اجرایی شد.
🔸
اولین آزمون واقعی: واحد رفع درگیری‌ها در لبنان
@Farsna</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/farsna/443930" target="_blank">📅 05:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc09b214d.mp4?token=YldFsYRBpQrURfCoUjKGnAR3fnwCxVkPH6OZAF4KHJzNSrqt1aJhqOkIfSsR7TiJTnKuOhNnPesmyCsHjgBgWs-Q6Jh4zPHR6b8a-NdcUHj8D1EWMlXA3lc3HGL2fKeLC9bJGyQkhachRUnyoz0tlDKcoK2nUBC95kRuPEH9LVsbSxID1A5vVTvLY263KT9Ep2LmLD_cn9fXFuQkdOrpZUsAs5XuSoVuZbyr77PWMfHyuu84bdXOSJNJXzb45M1YcyeSzivE1ZGjxJE4amY-vFpdIl0DubHUUZQTiccv0br-25d8Ki-tnm7y_i6LjKhqKhxJzxvD_SoYCjTIrL9Zfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc09b214d.mp4?token=YldFsYRBpQrURfCoUjKGnAR3fnwCxVkPH6OZAF4KHJzNSrqt1aJhqOkIfSsR7TiJTnKuOhNnPesmyCsHjgBgWs-Q6Jh4zPHR6b8a-NdcUHj8D1EWMlXA3lc3HGL2fKeLC9bJGyQkhachRUnyoz0tlDKcoK2nUBC95kRuPEH9LVsbSxID1A5vVTvLY263KT9Ep2LmLD_cn9fXFuQkdOrpZUsAs5XuSoVuZbyr77PWMfHyuu84bdXOSJNJXzb45M1YcyeSzivE1ZGjxJE4amY-vFpdIl0DubHUUZQTiccv0br-25d8Ki-tnm7y_i6LjKhqKhxJzxvD_SoYCjTIrL9Zfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقائی، سخنگوی وزارت خارجه: با حضور میانجی‌ها، سازوکاری برای اطمینان و نظارت بر ادامۀ توقف جنگ در لبنان و تمام جبهه‌ها پیش‌بینی شد.
@Farsna</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/farsna/443929" target="_blank">📅 04:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
بیانیه مشترک قطر و پاکستان در مورد پایان اجلاس بورگن اشتوک
🔹
اولین جلسه مذاکرات سطح بالا تحت چارچوب تفاهم‌نامه اسلام آباد در بورگن اشتوک سوئیس با حضور نمایندگانی از جمهوری اسلامی ایران، ایالات متحده آمریکا و دو طرف میانجی، دولت قطر و جمهوری اسلامی پاکستان، به پایان رسید.
🔹
اجلاس دریاچه لوسرن در فضایی مثبت و سازنده برگزار شد. پیشرفت‌های دلگرم‌کننده‌ای از جمله ایجاد سازوکاری برای مذاکرات فنی بیشتر حاصل شده است.
🔹
بر اساس این تفاهم‌نامه، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
🔹
مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
🔹
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.
🔹
علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.
@Farsna</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/farsna/443928" target="_blank">📅 04:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
بقائی: یک متنی را دو میانجی یعنی قطر و پاکستان صادر خواهند کرد. این به‌عنوان سند توافقاتی که در جریان ۱۸ ساعت صورت گرفت معرفی می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/farsna/443927" target="_blank">📅 04:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: زمینه برای آغاز مذاکرات برای توافق نهایی بحث شد. قرار شد گروه‌های فنی به کار خودشان درباره موضوعاتی که لازمه اجرای موثر این یادداشت تفاهم است ادامه دهند.
🔹
در این مرحله کار هیئت مذاکراتی تمام شده است اما تیم‌های فنی کار خودشان را فردا ادامه می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/farsna/443926" target="_blank">📅 04:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: نگاه هیئت ایران این است که باید گریبان طرف مقابل را برای اجرای تعهدات بگیریم.
@Farsna</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/farsna/443925" target="_blank">📅 04:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443924">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
بقائی: اظهارنظر تهدیدامیز امریکا باعث شد ایران حاضر به ادامه نشست چهارجانبه نباشد
🔹
در زمان نشست چهارجانبه اظهارنظر تهدیدامیز امریکا منتشر شد که باعث شد ایران اعلام بکند در چنین شرایطی حاضر به ادامه نشست چهارجانبه نیست.
🔹
قطر و پاکستان تلاش کردند گفتگوها ادامه پیدا کند و ما گفتیم به صورت چهارجانبه نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/farsna/443924" target="_blank">📅 04:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443923">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: جنگ در همه جبهه‌ها از جمله لبنان باید خاتمه پیدا کند
🔹
در خصوص باقی بندها که لازمه برای اغاز مذاکرات نهایی است گفتگوهایی انجام شد.
🔹
درباره صدور مجوزهای لازم برای فروش نفت و ازاد سازی دارایی‌های ایران بحث شد و پیشرفت های خوبی صورت گرفت.
🔹
در خصوص عبور ایمن کشتی‌ها از تنگه هرمز قرار شد سازوکاری ترتیب داده شود که مهم است.
@Farsna</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/farsna/443923" target="_blank">📅 04:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443922">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxptsQnpRIx_pLN9glObTe_ZpGuwq4nhbmIpA8hB9pfhhef5gWMHSohwwerHexY8Bv3fmsPZQT15NidAzca4kPauwXNHnzwKItMC63P_EOVVZOl0P3r9y4T9uqaT-pULGOO-9kiKPSRTFsUvz72MfPcsX-vVySDlfCOXzBtSDjZ79__5jPyvifCMsYyfXQIQwQrvHXnPAZcBLeY0cnD7p_0xs4jW9BugXEkPiV_tjGKqxHIDanTCs5-XI7LrHM3Lh-imlVmE5bW55cPzpFjFMPOZo9-kE4fP_mCbg19xx0bvhg_Q4XJ3R29tcmOz5dVdiuRhIXUIzeeOMDORmaabaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش فوق‌العاده ظرفیت قطارها برای تشییع رهبر شهید
🔹
مدیرعامل راه‌آهن: صنعت ریلی کشور در آماده‌باش کامل قرار دارد و تمامی ظرفیت‌های ناوگان مسافری، ایستگاه‌ها و نیروهای عملیاتی برای خدمت‌رسانی گسترده به عزاداران بسیج شده‌اند.
🔹
افزایش ظرفیت قطارهای مسافری، راه‌اندازی قطارهای فوق‌العاده، بهره‌گیری از قطارهای بین‌شهری، ریل‌باس‌ها، قطارهای ترن‌ست و تقویت ناوگان حومه‌ای از جمله برنامه‌های راه‌آهن برای پاسخگویی به حجم بالای تقاضای سفر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/farsna/443922" target="_blank">📅 04:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443921">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC_4NYHVeqEpfI4lXzWKv61YIkLdLn4p-cyCA0jYpVSk3G008nl8ftTU4i2_lUNfJtzFez_6c830iyAgEC7SLGkj9I5-Xx6ZhSVcoUu9rRZqJ2aDgT_tIsSHHDCg-7VRFbiyPFc5XujSWrkDJ6sEbOv6xtdCE8b-Ktd0iUtdegIaHfnDD9VV9pFzEWzuvSwgVk7GqawOC94njJMgFvX0PrXvDf08eY8VDOl2XlBemCbbJGFa2WK-q89irXQNUat_kH20NecbR6Mcw3hyAWyOj8-8uuEk8bZdhekV-CRp9G50Ve-66yYvaTH36ir9q_ifO2XvlKlu-tEOy4nqdthBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تساوی دور از انتظار اروگوئه مقابل کیپ‌ورد
⚽️
کیپ‌ورد ۲ - ۲ اروگوئه
@Farsna</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/443921" target="_blank">📅 03:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0UfCqmLToEd3GfVA_HweS_WQxjAXsTVRYRKzErMkWp50mIXrvdu3y6ikbUXKdd2ska3tgm0r2kd3lzgtut6o3vm9lQmyJEFULQzx-Byhu5bJULBOybWjqrxiN8SNHIewf1-x4fo5m4jjCffIkcacmWXESWwAOSNkJyWyp8j3EhinGL_DYQaJzJl6DXmJtpxqa3eQG4c_y1oYol9jxia6lYaTLQAKEGQ2yyaqTauauL_kzITT_GYS72vPALYThzhxU95WTQfjMqeod9bCKOExkhHV7oMllC5Sy3817zaZfRX_CnoNDdSMJW26n_lLdqDZ_UK7uZ4gLZa9vDqj75DKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5Yjf8Ilh_p8vEtimpr7y_YPFBuO5Ogba0EXiaRJ-8AC59lyLhe16S8g4IBWinYcZiBBJ1fg1M5MIpuoPRz_xbnQnI8Tt_cniXofrt3_qfzFH2yAAfaHzsmY2gvx8N25_6dQ-Xwy73oJda9oAydj1oW3i-AG2hWM9M5tlaLvVyCp6sVdVyrhT6_bJPWva9VnQ2dsDW5G6H6C2qK-ENTazjzVdd3rerSpj8wfWytKCeLGFUVQuze2s9sSe4KIre1I5-zsgzWGEx_VSapCAx00u4cLbzbtl9F0WR7NdNQY9JQ8cstka-VD8_yC3VPEEo60l94x9eM-izrXLLhDU4KPiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4-2OCcAd6ZRGMqPFID7RJBkALo8eTkw2efwiJaQHvw1nE1toSl2WPEDM33NVHCt4VSWSgePTzHcFfC7AWL_e7O9_k4WRaBInWNd2QM8AT4EQ8IfVGpSLIn1m8-0rwS5N3fXob_7WmxdWGjARWRa0dwrvwAsc0jNew9LXpYfPj9XFylTdJqM9sINNNWoj7LIV1vtx-ka4zmXFT9TQmrA_a2xUqN8P9ejA9mLh5nLrnnVGMjyC4Z3c6_-IvpyRlGLLhRCXWwWrjDf_aSVTtBaSmu-Xll95FKhWC9iTEpyPyPOLbWO9gpnPvFCw5P4WG0WQS90trvWU94Wf-v0iGznMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wl_RxUj2IJPsPrHM_BjmPl_GIQG9jy9VGmM4tozFoc4nbelrgInV8Jyh4ZEuXG-K4N-zA5VkPhmuZZ4jOxhOptOeaIpGN6B7Eqqw-7L6bnp4q99vpWI0JqSuvdfHTsH1K_-1QSoGwryuWay_a0aNcpR4AhqNIEQmIPJ7Rgtag5p9toKWLFK3ZOo9kYjkAQcWfJGPZy7wZQxTeaMVPuRdT6FkaEyfbf0_zBWW9rzEH28WfPq-LRUeymYRYtoBdXErMS-yP-nLY1ngucuEASteHkVpEjB8H5AwHI4oSo8AYHNZwEoxeutI6SMEzQERIrSRwHRJMP3WzYHBIBZNfbNJHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنیا به افتخار ایران کلاه از سر برداشت
🔹
واکنش تماشایی بیرانوند برابر بلژیک و نمایش دلاورانۀ تیم ملی در جام‌جهانی واکنش‌های زیادی به‌همراه داشته است.
🔹
خبرنگاران و کاربران شبکه‌های اجتماعی به نمایش شجاعانۀ بازیکنان تیم ملی ایران مقابل بلژیک در ورزشگاه سوفای لس‌آنجلس واکنش نشان دادند و تیم ملی را تحسین کردند.
🔗
شرح کامل گزارش، و واکنش‌های جالب کاربران شبکه‌های اجتماعی را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/443917" target="_blank">📅 03:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9ut20Let3-VSkPfzKN35q4UtCC86TqZiNFA-DpRqC2z63FDf1NPC5pWn3lNh-SQRsorojzBURxWOXY9V1Y0vgoM-dcCGdv4y5uv4YLW8kLpFfq9sTZ-vV0tHZn_wGWgzm3-Y4FrXRkv9MU7ViaBrQAAhBN3NwNM3tTEMSu2zFfyMrjnAKSs_d-pJk0g9z0CKF_CKcEbSKTFi7Z80mwy-D65IXsemq83BCUYoGed0bXO4NKZRHRylyU0CvhwO6YItxjxSVWz2tenzg1mGbf1YLPAjEGtVC26PrizXUaDrOWpR8KUTQ2DzpOetBsYx8rKwh9g51oY0M-khtPShFYZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هراس ارتش رژیم صهیونیستی از شکار فرماندهانش به‌دست حزب‌الله
🔹
رسانۀ عبری واللا به نقل از فرماندهان ارتش رژیم صهیونیستی نوشت: حزب‌الله بار دیگر سامانۀ رصد و جمع‌آوری اطلاعات امنیتی در مقابل «خط زرد» در جنوب لبنان ایجاد کرده و تمرکز خود را بر هدف قرار دادن فرماندهان ارشد میدانی اسرائیل گذاشته است.
🔹
نمی‌توان این واقعیت را نادیده گرفت که فرماندۀ پیشین تیپ ۴۰۱ بر اثر حملۀ هوایی با پهپاد به‌شدت زخمی شد، معاون فرماندۀ لشکر ۳۶ با یک بمب کنار جاده‌ای هدف قرار گرفت و زخمی شد، و فرماندۀ گردان ۵۲ در حملۀ هوایی با پهپاد کشته شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/443916" target="_blank">📅 03:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443915">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">می‌توانستیم پیروز شویم
قلعه‌نویی: برای برد ۳۰ سانت کم آوردیم
🔹
قلعه‌نویی در نشست‌خبری بعد از بازی با بلژیک: ما ۶ ماه در شرایط جنگ بودیم، لیگ نداشتیم، یک‌بار و در یک فیفا دی حدود ۴۰ ساعت در مسیر بودیم تا وارد کشور دیگری شویم. ما شرایطی را پشت‌سر گذاشتیم که همه دنیا از آن خبر دارند؛ بحث ویزاها، تعطیلی لیگ داخلی به خاطر جنگ، لغو شدن بسیاری از بازی‌های دوستانه و مشکلاتی که در مسیر آماده‌سازی داشتیم. بعضی از بازیکنان ما لژیونر بودند و برخی هم لیگ تعطیل شده بود و بازیکنان بازی نکرده بودند. فکر می‌کنم در بدترین شرایط ممکن وارد جام جهانی شدیم و دوست دارم همه دنیا این را بدانند.
🔹
در بازی بلژیک هم ما می‌توانستیم ببریم و هم آن‌ها. ما هم گل زدیم و هم دو موقعیت صددرصد داشتیم که کورتوا، دروازه‌بان بلژیک به شکل استثنایی مهار کرد. با اینکه شانس برد داشتیم، این نتیجه هم دستاورد خوبی است که دو بازی جام جهانی را شکست نخورده‌ایم، مخصوصاً با شرایطی که توضیح دادم.
🔹
علیرضا بیرانوند یکی از پرافتخارترین دروازه‌بان‌های تاریخ فوتبال ایران است. امروز یکی از روزهای خوب او بود. از همه بازیکنان و به‌ویژه علیرضا تشکر می‌کنم. او تمرکز لازم را داشت و توانست یک امتیاز بسیار خوبی برای ما بیاورد، هرچند ما می‌توانستیم ۳ امتیاز را هم بگیریم.
🔹
فکر می‌کنم تمام کسانی که بازی را دیدند، لذت بردند. از همه ایرانی‌هایی که با نگرش‌ها و باورهای مختلف در ورزشگاه بودند، ایران را تشویق کردند و به تیم انرژی دادند، تشکر می‌کنم.
🔹
ما فقط تا فردا می‌توانیم از این نتیجه خوشحال باشیم و بعد باید به فکر بازی مصر باشیم. مصر تیم بسیار بزرگی است و فوتبال خوب و با برنامه‌ای بازی می‌کند. هدف اول ما صعود است و ان‌شاءالله بعد از آن برای مراحل بعد برنامه‌ریزی می‌کنیم.
🔹
فکر می‌کنم طارمی کمتر از ۳۰ سانتی‌متر در آفساید بود. ما برای خودمان برنامه خوبی داشتیم، بلژیک تیم بسیار بزرگی است و در رنکینگ جهانی جایگاه بالایی دارد. با این شرایط، فکر می‌کنم کار بزرگی انجام دادیم. هم آنها شانس برد داشتند و شاید حتی بلژیک شانس بیشتری برای پیروزی داشت.
@Sportfars</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/443915" target="_blank">📅 02:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443914">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiGMvBSSZAT4U7qs11EpmDwGoJXn0k1_v6m5VTn6nzjLTUyzBYHVOL9j00VF3fEyEH9x4mLzX_Txftvw9BP8usDwQaWfr4B2N3rIOW5JqBa8jWl4aQBd168m3CLrDif8BH-6BYy2H13UsktcGEPq5PposlQMrM-nCB1ASX796iCYdIFHRCa8SQkBS8PAYGKvn2rT73Ai1y-5q2pXa9iKBXs42rGh3HH-tTzzgWlpxBXaupJgFWhVqBG_TbZ2jwQTxduJ2icncWWV_6AHzvIwbmhwormldWGpYHz4PInVglfxahOqWIT2zAIOjKlVab4Cp4IXVtWmSIVg_UgNzz3EIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر رضایی: آمریکا باید پاسخگوی تجاوزات رژیم صهیونیستی در لبنان باشد
🔹
ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد.
🔹
در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/443914" target="_blank">📅 02:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443909">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_GbTr3p9TZw3aKj-sg9DIp0VJbbpP7g853w2h4l3sryuMbZyz7cmUGRqT01WiYgRCEsVLsXyOw0AJVO-Vv2jAgNd1CcnNR1u5tVbdC07s-5Yl8gXByXksTGrr-LxF3WW5SItDf0kgM_WY10rTP4MC0nqgBddwZfFerqa7LVnie6cuZ_kxFu9aeJdYbER10ATGtH3SllndekI02zi7ZJhWq9wzuZlFtwRmbvxfmm5viHLC0QKZGXw-rfdleknUFBl5MPAfpZgabKBBv4F_L_cKg0ZGFcVnxwEbNiNMjF2NmCSSDagKGL5lA8d8EOBGFQfSboQy4WW9BJ_fXblgHvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptAHQ1dw3RQK8b1MSy5lzBNiWhZ1cOm8zY3BSRJPXasWr6uAgBmkTU_ry5vu4F_djaxDcwvNCMKB9nXt2gVVwS3mxSLk7CKTzQX57U2izUrtPCcAlZpA2eCF5YO3PKlpMTeUSG6eVsy7IMKL6HI3888V3QaubEWDDV2tcKIg-FQ47QLC-9N--6p4JYbazKM6XI8GJ6DBmmZdx9KxwOZNh8XE2j0OmbcHIvY5lE97hMrBDq0-Yc9BWD-gEyA0UcGUnsniPyg8uQZyZ8jXzvdanzJBwgARuLmuu5-hrRjThuPsetYO9lbJxuVWShbOfeeINl_rCLJ4xnrPX2Bbrur6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFNlwLVe1sq0RKm76lcLB60zlITSTP9-L0um1oiD15u9LauoQjw4AJVrWb95jyqGelMu7ucO1BhW1wuNqdVxWVUJb0wfhyRGsS6qbnrm6AGx-79B5spAeAhd1YUxzLWxgfAXTtGzaOU2YGKz5E3qTOszRR5PKENDnpd46wquy3ZUZDOwzpfmT2u59vLLSzTXwwJr0wxSw0xgYucCynIFGX1Lk32nS8PTG9nTeykeKc3LtXpp7XpeN-Am-TGifLcXkittZh7VTmb0x02-Q62AYj_HoJI6A93GOMTbX4bJ3xNzAQ8hElHhPHr6ZvOXw9SIFrOvXN5L04ZO-WHdkcwfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Crb6uy1-yLlEAxo-OvzdR2UGf7j3xxCpfV9owvwVfihjP-MM7L2tBR5AzNkH2YciOKyO5NTqtHy1vPNGiwfq-zy95K9h0U0yDvgmOqERc7Ocm3o6wFDLOqYUmc33yid13DzE-Yn38oKyG0sZzcNmKA9OXJzCr0UseI-Af_w3gctIT9lZJ-iBWrSMyM02KA83urYUoR6vnifsmpPdztr43Zwnd0_qil8_WS99X6EMj-cB0Zc1UBqfJgAva-0lU6fpZrI9cTvWiIf66bzPoit-SD9c2RrKJqOA8mz8rkIFbSL4s7BZPDwjyjmj9I3zwktrnLxLE6fAcmSembe1Mm4Omw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F6xa8Rz1HEWnNbVxnTySI5TvlHXOlmnWA2AR2KtIVUHoFPZ9AiHRKThI4gUhi_L9n0nowlMrJOuKpB10sUP6YyP2MksWx24mIWq1uaf0ABZCeQSas9jxpU-UXKdK1LvS8L4ntSeQJ5FkVepKWbNtVUaZyrqr1OUMU8hi0ywu1KdonpP4T9avEPVDNyqL-nAu8GSSB306fDWwpjxxHe-DvMNCidotee0XfqfBCBIIEDBE-WQCj_GEBhwYuNpBXKEpKl1L7JGX5YBFpSk6TpeFj2vN0DFYLp6rtzkpa3cHXMrRUynPAaj6qi1wfKBq9dSgKa53bZA7Co_So70aIZ35Xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/443909" target="_blank">📅 02:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443899">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gWV8rAWJsnNeKXcQHiUIvbACcea2vnP-PZuySA4cyUVaMNpyfo3r1gn2JkhTsvcAuLOgkJ73mLfGWMyuJSmalI3xoYTX50T-gVs5Ct82w5AXtzW0Y2VWpNg6Dkk6YYpvsGY9Ql0YwzsxBN-FAURp5j98B22Wle48xtDkvIpgAO6Jiu8ZSVebyR0AcbBcKq-7e2yp1Qgq_Hlr6hs0ess1501YW_HXSfq4j4hu0LB06_nKM14uJn_jDSzM5NJCGh354zIFyg7dQDiEE5Waf0CGJxxK78Or-aadD7Uo_0hWHdF3I0jz-MiYNvzwFWNBP8WWuOEsSuv_2BV9u4vWGCM3JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdsHVLXlTaG5CjQn_gJHFF5d70fohMEDbF5AxaDEwPdlmhnYvWhkAKItthUoeAZMQwo_h_O2hyQ43Btm3geB0FzhlhizgcB83b3jCCK_g5ihLTmSRLFBojRIVmts4KPEVvjy7FG2e2CriKrkBr-GQWr31xii5-9sP8Jq1CiFdfFCukNvz1S-r83McHIXCNR-rexfObysx2CfUMOTWMZdiQ0r-_ylnOYGG1zWhrjjBRGzG_CQFIBHV5_1kAYBkPwgg51yaS-9TqaQGeAmkGhSEgnvgH0dfb8cUSDDbYOrPoiAqUIGzLtXrXxqe-gfuQx9WQWD0pQsbhdRYtbRNxYlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BeB2I1OpXCyk2WMuxJxJII4e47klnWDiFzTGbvVB_9_VBZpogpX-sR86Ru8_kkvoW3vu1iGz7DWO5dUcfFWS-LoClQQn9Io6q7ofVZ_Wld19AZdZgwTiGnGB_dkP2Y1WgRcmXUHnimH0mcg3JQkcrZoI5jCuQ_ZWgv0Vw1T6rT8tk3NX7QxznzvxS13-B2qqvDT8IR1lJDbVZdXddXDLIpCWnh9MVt1DqdllIbEphyAWXwFdYAzyZpuEUkUjc6AYxvbYMCPbvvxnxB4fmx3vj8QNEv8b2eCOKT9qHgU50symKiuX22MK8vfU9a7ILXf0SP-QOAT92yQBY5HDoW-AJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWWNDK0yERJNQ9vJl4NeDNzncogjFQfXf8hwYi4Qumc1KaKgdvtAFEEGomhq_xmznvwaGUxGZ6IheNXbWcpG2dxaQFmnRDQqP14tMYaicCdC0UZ3H7j2T791CAjt_E06_dAIffIZEnic-LbQCq0nCvtoo8b-YTeDPwlif7O-MPzNWAZdHe4e-D95xYcZ-hXnjytC0cV6AP-3N4K5Dto4SPbA6VRHZZa9RogkpLQ1_NB-GPG_R83rWURFkA9ccI-gHAkbEbft1AJrU6qfvZm_Jz5KJfHkMnOrdPGdX7gK8IbBEB4jcQUHtMFLA1LiYKBjvjP7gcd9NCN7eNiRTljkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbcFDeTAEfKubmXi4Xbohgj_qT2RyIQRRt20qCZzIaMhDvr2NTyG4cHPWnQTxCdAGNZ0B2i6hxcdOAcTedtJ0-2M-S2FL2p_7MumOxpyMF9cfJsJAjgjQ7C6l8WP832rM-3f7CJNQnN22W4rn00YZunlZpTIHDLLQ-JLPgfN_mdRct1OyUZJdsG6BV5RMhBOCLYG9Z1lFejj1yTy1JOPJE8-1JT5KXjTuoVbun8c_OUGVKpDOyOBGISxHVY7cVQDynwmjZArE7IOAblkOddq75Ojh_N83S15WahArdAjkUapudPSwjEhi1VhooG0I-IdAQDsIAePJ0LTCU4XESSLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MoGbQtsUCy7hASMHJgSuZ32tp_MWwlsAT2qvd9cp7LIVCgpDteVRsaLRJNfWnN7ORC8z2O0JkU_rRVav3CK44wTEh1gP0vpSXrbWEM2mF4DNGwtqquhglH1jZA-2aBEpoK4dweHxdCRg0zCn-U6XtNnrvKBcQZ6LaeE_yQQb56SiHuq1y80ZSlPBZbThD7azy-Z4O9MAuTKX15nodCN_NxAsVycLsxCHMduDSBDleqRSypLNZTgXleCfKofSG950KmoN958q-fd_hZE5p3ItqwlPZZO191hnoC8x6NVR-PoH3xWp22wddGnRhppLEs893x0I-o3nYorf2VYnwHl1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PP99d0YM73KNWOXAzxA7YX5t9OFNv7otHKTS0NVt0ZpLkBAxjM3lnuG54m1QC6XNKCtusWbjqfMM3WiU5yhW0f0pFDG6xt-8G6eAc8wdRkGFJH0BX52WDvIGNwtttqu17NT28UDGZx6QoJL9USY1wxDv_Unyq_AzaMFMWYtHat2YxC2D0_Sb1c7UL6ZLMK_hnSqILuNVP_bye56hcLn6FujAqbAXILyBLawoXIV8IlK_kUJmAw-Tg3w-9xKv4ycChodCG7eCG8Dj3uTgpNLrsXLUuChqmZ0Kzj8PZWSo5uTHGv9EEWpPokjYkw5rBUqcEH4XXINU1kN8OOyoxvjEGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBdGdyZnPohSpPR0i4ji1FrCS780AWgGIf9Xa6uMhl-7MimqA9xjGGzD_adtlg1hgotgdcAVb2NIY7n-5SC5RKyMAjNmKELwJYbbJB6ZVhe_07oAVERWjkCzsYsKh6O3rHXzeGvxSOXA5e1cFv88WBJsPBh50r9wSlaAqJiHxyBGcDtwDOs5kozwgMtn-n3Qe6iNu1DZTfxcmcFaJe1pe-yqzscii07IbXE972uaPO0oKfk2aoV31L72UQl_xoB7uZ5OKDf4xpkDRx5cX4VFunFv-U_kyiHHnPOZgCXiLupMJicHo3dQimNkiwiLXKWZJPVJEX8hY5UKByNCko0oQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AsjoYibrQKm6vDx4AQQ4ws9afFK39aznEAq4qeiRD54YAPCyQ0seGh9JxmDFy-oPhXrCv7v0CezEiWzAB0yuMTbmd9KuKCR25jEiWbkEmZqlpQfYDPiht-rLlYH3ntQ9QtccXG4J9JwZTDH-tJ8up5ezItKnTyYPpu3h_NlQ3a4UA_XvifmexbrBITNt9t6W1CDDTep0vZdylPAlzdyl3k58wJQcfWR05YdcO-sCc1oKJwQUtT6Qbl6xqN9x7RLOgdEX_kJ1njWo1_bbB1bgDMg1OuOgxo1OXNqF31MTFP0uBBS_pxHDL0qgOGLJvYMc9zGwnq2CFro-2eyii1SuAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TsxPG2wgbLIEU94UD4VBcfAVGjnWl1LrqlTK8kV1WJiq-auhCHMTqfM5J5rQN8QgG_QHb_ZE29M6Ua3XZb27acZSuLZ30VdMboUTsoCC23niN1hzyXFIYksA1deIIP2R4nUmYJaT7RRhHCZhlIlhaWhM0LjMbIzoelPC36UYLY-ri1_548M8GPc3O4sHrzNoa5nCPOx9jOGoXwz7BzEFK8iaLnw3Vl7VcplQSCeW2yhFL5F8xm_4_W4DnTEKKkg9cTgKkiO8sUtCuPYxwg5o6krtRTRNRSiKMhq4U_IlNMmj5PFu21P3ozMiY9JM-HcoikpajCoMr5TjZcVAZFZfLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/443899" target="_blank">📅 02:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443898">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTW9xOzy9kXPceQ5rJ2DVJRn91BIIUvrnT1kTPYu1cZy4bOB0KFIuWdW4tVDNYPaL6aEeX67rVZqgG6AmXELpIFTAPr-WTexvYalEgxgUScxMN9EB0ICt5fDDQsfqkKZjoR9fyiarjcFOibuUxTljFImY8j6SUxy93OVvYnppz_vfE2qiP8yTMk3qezBJxLwiI9Lu2JM9e5cz0osKOE7fIFxdVy9lixTtugCKqOhz0ZIh8AZihSiDh-jvvEpeR24_lYURCh5g2egANfhfThEvkAZgzSR5RXqduz2uR6jZV65LDuGP7oMTlw3tzSNqmG3uhxNZlC5a0b7epLFZS2vUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجولانی از ترس حزب‌الله به ترامپ پاسخ منفی داد
🔹
الجولانی در توجیه ترس خود از رویارویی با حزب‌الله تلاش کرد سخنان ترامپ را به گونه دیگری تفسیر کند؛ وی مدعی شد که ترامپ از آنچه در لبنان در حال رخ دادن است ابراز نارضایتی کرد و درباره نقش سوریه در یافتن یک راه‌حل امن و بدون تنش صحبت کرد، اما این اظهارات به‌اشتباه این‌گونه برداشت شد که گویا سوریه قرار است فردا صبح وارد لبنان شود.
🔹
وی تصریح کرد: من نمی‌خواهم سوریه مداخله منفی در لبنان داشته باشد و ما به دنبال راه‌حل‌های اقتصادی هستیم، نه نظامی.
🔹
سرکرده شورشیان سوری عنوان کرد که سوریه به لبنان نخواهد رفت و به ترامپ گفته راهکارهای دیگری غیر از جنگ و مقابله با حزب‌الله وجود دارد.
🔹
الجولانی گفت که می‌توان بر سوریه برای یک راه‌حل مثبت تکیه کرد؛ از طریق تقویت حمایت از دولت لبنان، تقویت نهادهای رسمی، و ایجاد پیوند و ارتباط میان نیروهای لبنانی از جمله حزب‌الله، زیرا راه‌حل‌های جزئی و ناقص مشکلات بزرگی ایجاد می‌کنند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/443898" target="_blank">📅 02:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443897">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۷</div>
</div>
<a href="https://t.me/farsna/443897" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۶ – کتاب آه</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/443897" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443896">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7gq8PYonEwa-dDMrq7S8vBPQMytLG_lNapAUO1rRODGndDr0wDfVEhKFVKo23AWDd2AhOEqkiSd5pvqA7Uhzu-F2Ogo3cGEq9qGzqOfEs9hslLxFFP1aV0_X3ssLjO9hJEKNMDCcj3wMtv8xMfWzR3cEy8JOZRvoZUT2lA0zE5Es330_hRANrdZ6kvsG3AhmH9_onXiUDldsm5vmSlZWvuyywfHGoVVrmdi0ZPo6oqlXa4bsFVW_1mPmBXad2jfHafFI3lltXvLujK_RrxSvn8PK1GOyF205wYvXeZAFPniU5R9Ab-zz2CU0JAhes2efpXEjz2uEHViKPE8XUxlRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر علیرضا بیرانوند: خدا را شاکرم پسرم سرباز ایران است
🔹
مادر علیرضا بیرانوند، دروازه‌بان تیم ملی در گفت‌وگو با فارس: علیرضا در مقابل بلژیک جانانه از دروازه تیم ملی محافظت کرد و اجازه نداد دروازه ایران باز شود.
🔹
این موفقیت تنها متعلق به او نیست؛ همه بازیکنان تیم ملی باغیرت، همدلی و تلاش مثال‌زدنی بازی کردند و بار دیگر نام ایران را در سطح جهان مطرح کردند.
🔹
مطمئن باشید دعای مادران ایرانی بدرقه راه سربازان عرصه ورزش هست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443896" target="_blank">📅 01:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443895">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8PEbCxRxkjFmu9Z08pIk4S8EeoLHL2zwjiP1q2MhRyn0gHMx39WNBY69ZiorG8EgsIPPi5NtoIvdljKVwOY7Haw0roFhz--HOigwLw_Ap1clSMd51o4YN4VwBl8dEPsHqBc-WZVx6OomLhyMAeLkxthn4fffu3KI3KZ6yHxhm7T10PjCf7pG2DrlhqhoQoL5hZlqp1fstsHGCBbF_9nCiOrt63AX-C0zPwE8vFq5IcKYUAgRPdvy0SdfKgSfWMo6_mOtOKxHvjp-TluzzZsaBFQOEH-mbfwMFjCpT9bS56Do574LBNZ6xv6W1HRBZF1IGG8ZGBwUGBO3NiRnXPojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
این تنگه هم بسته است  پست صفحۀ ترول فوتبال @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443895" target="_blank">📅 01:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443894">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8312480c63.mp4?token=diXpdFJOBD2056dYICyId_Ig7ok6FqANT_hDsbj5h8IlriKkor4ulal1FEPrxyZDZSOnSC7Xu63TlEEwsFOskilAtlwaQKB0KPs2aNCLj_TZRSd-P6s63cO6mX2Mc09UOaNXemz8zcO8FdmcI_-vP9ihkpWu8YzeS2ZT_cqcjS5xOUptTgTfOBet0V0l-ixQ0PSrIXz21nn5awWjxjqNZ6sJxuAJXMJ44O-8xmrmSbi14BSfU3sqbEEn8IeeNlC5OwmrAnJBqntgEreq3PJrNkXzGqxpfvxJ3T8713cADny_fSb-lUmrAkShIko_sLfEnSsj3mzYbmHgL8yhIrs17g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8312480c63.mp4?token=diXpdFJOBD2056dYICyId_Ig7ok6FqANT_hDsbj5h8IlriKkor4ulal1FEPrxyZDZSOnSC7Xu63TlEEwsFOskilAtlwaQKB0KPs2aNCLj_TZRSd-P6s63cO6mX2Mc09UOaNXemz8zcO8FdmcI_-vP9ihkpWu8YzeS2ZT_cqcjS5xOUptTgTfOBet0V0l-ixQ0PSrIXz21nn5awWjxjqNZ6sJxuAJXMJ44O-8xmrmSbi14BSfU3sqbEEn8IeeNlC5OwmrAnJBqntgEreq3PJrNkXzGqxpfvxJ3T8713cADny_fSb-lUmrAkShIko_sLfEnSsj3mzYbmHgL8yhIrs17g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کوچک‌ترین شهید کربلا نماد تاریخی بزرگ‌ترین مظلومیت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/443894" target="_blank">📅 01:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443893">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87c76a71b.mp4?token=Jl-5UwQ82WfAoABW30A__hIShWJyzS1XvZMG0l4tT31dfe4UpAk636f_Q07OdawY9XG5GI78N9frR2_sWEDkrPaEUMX-V4Dlf8q-0n0h79hlR-FmsjyzCOQwC9CBJBquYRFMMdkxyyw6Wg5nJXFm0IRRpDfKza1fhntw7GLky70akqE8RDzcX0zg4jG1xa8j5HG_16iD4SvEpkRdYQDaHbgWPj8pSXaR3_aphLJ3j47yY83mgITslM4Qwj-iIIaK0yTmZy0C2UUsSXLRl9f405uU_180cMZukFNL4Az4US0_54p8SFsOUHnhYwTzzkt4BdXE35g-SvIzUz8qcBiWCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87c76a71b.mp4?token=Jl-5UwQ82WfAoABW30A__hIShWJyzS1XvZMG0l4tT31dfe4UpAk636f_Q07OdawY9XG5GI78N9frR2_sWEDkrPaEUMX-V4Dlf8q-0n0h79hlR-FmsjyzCOQwC9CBJBquYRFMMdkxyyw6Wg5nJXFm0IRRpDfKza1fhntw7GLky70akqE8RDzcX0zg4jG1xa8j5HG_16iD4SvEpkRdYQDaHbgWPj8pSXaR3_aphLJ3j47yY83mgITslM4Qwj-iIIaK0yTmZy0C2UUsSXLRl9f405uU_180cMZukFNL4Az4US0_54p8SFsOUHnhYwTzzkt4BdXE35g-SvIzUz8qcBiWCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشویق تیم ملی در لس‌آنجلس با پیراهن‌های هواداری «میناب ۱۶۸»
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/443893" target="_blank">📅 01:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443892">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fn28dhzbI6eFHiC8oauWgSMQuXkud_oPNbKEiuabh3IBLJhoKw9ubb6qGnWXP49gZusV0lRtKNGTCnYqxXrJ6VmmRKj8Pl6zRHtkLXER-h2yr8nPA9pMowC6sCdF3-tYNmKgQTS-GVqAu5MUoG-sq_Vat3ogOSzManot4X-z2Iu6pS33D_YA95--ob8nhgjzAvHdjRBg9tFJtSbeYi0fW2VdppHd3ix8hKss3JmSdsFNo3GdowvkuYl7g2PhZqpaPmyWgucNGvpNx3bKk8EZ4VsRnLv-ODsLGrDUGaFdT2lPlR04KkV9nvdzEWPj28x_ToJ3J-bUlFS0aa8m8inM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط اولِ کار
🔹
روزی سلیمان بن جعفر، به همراه امام رضا(ع) به خانه ایشان رفتند. امام دیدند که غلامان و کارگران مشغول کار در باغ هستند و مرد غریبه‌ای نیز میان آن‌ها کار می‌کند.
🔹
امام پرسیدند: «این مرد کیست؟» غلامان گفتند: «او را آوردیم تا به ما کمک کند و در پایان کار چیزی به او بدهیم.»
🔹
امام پرسیدند: «آیا مزد او را از قبل تعیین کرده‌اید؟» پاسخ دادند: «نه، هرچه بدهیم راضی است.»
🔹
امام رضا(ع) از این رفتارِ غلامان بسیار آزرده‌خاطر شدند. سلیمان بن جعفر جلو آمد و گفت: «ای فرزند رسول خدا، چرا خود را ناراحت می‌کنید؟»
🔹
امام فرمودند: «من بارها به این‌ها گفته‌ام که هیچ‌کس را برای کاری نیاورید مگر اینکه اول مزدش را مشخص کنید. کسی که مزدش تعیین نشده، اگر در پایان کار ۳ برابر حقوقش را هم به او بدهی، باز هم گمان می‌کند کم داده‌ای و منت بر سرش گذاشته‌ای؛ اما اگر از قبل مزدش را تعیین کنی، وقتی حقش را بدهی از تو ممنون خواهد بود و اگر ذره‌ای بیشتر به او ببخشی، آن را لطف و پاداش تو می‌داند.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/443892" target="_blank">📅 01:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443891">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SY4c7R7d4rG6-E58gdPVc43D8i87lxLcfionW5FZaCh8Zz-5i1j9ESb-82g7trhD2nrKs-9_FnW2MJClNDbBpjuA9HvKIvdi9iCTp-mY689T8WM3ncIouC5m9GmjnI2lUO9PiD8_da41t0dYklAWsM8li3gqHSKP3NNSlITPAOjZ-8GMW0o-5sPNrN9pyKRAugTfX6j34uQG51psjPofHPEgzO0hUJAdfUX8RC5lO1hz8EDgT-zv5FqG1looykmGv8ZWjlPyOKjcL_z08s0HMsYCa6C5MPNnHbM4tXreevltepjAqVxa8AaHwMVfMlXtS5gFBqPmkcT3_kI7eNl0SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آمار بازی ایران و بلژیک پس از پایان بازی
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/443891" target="_blank">📅 00:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443890">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1ZDwDdWVyOqfxFdMjv_I3ppkMKmujD_dw0ttBETldOqW3EncSXHgONjUqVi1m1dsQHYAO3esenR7my-Pb9Fd5um9VFxodUMBVqeRbAlZA3bqnljpKOKrXJPBXJYimjNvmsrdO2ilrvrxXpsmS6rbmnFLFPZ_wQKr2AdrpQl1tbLz2z_cbCUyoxA8OlogDJ8_HcDhcs7zvF5jdzG13ROD5roKz-c4RKYDmHe9wYmqYikmgguFKGv_n113cdR-bOEd-xpY91Cc7I_GElKjfIjU2S8SskbE6EvYFvu7huz0avVIXBiUdeWo9ImDizrYwsU3GBLroIlIwpGxcqv5YGacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
علیرضا بیرانوند بهترین بازیکن دیدار ایران و بلژیک شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/443890" target="_blank">📅 00:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443888">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68d893be4.mp4?token=bxEbfaMlJeq-8RnKyiqWGffpmBLHaNthdRcqAMrwI-2_Ajy8Ekv92Gglm5Oh53Wt8LIK9QPFZZDvlud-CdCkuxA5TBaq_YRkFbOaGsuIi-aLYxndFnriewC6OFUdljCXK_R04WxKkurmtvlvzYrx1sXjSwfvpo_BhSrXnDopOefGLovKC9TlSs4F-5uOG8vvWVByXiY2F9T9brhZ-1JM0ayPB9viEWxikyNRIF-51uY9uptk7BOgbQhqa5PBPytNyNgcfM9JOJlmFQWVas-i-T58bNJnzq-3gRMpT02HgEZoCU3WGNX9uw-_YgNCQObA8PN04_FjjHjBRIPjE14-mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68d893be4.mp4?token=bxEbfaMlJeq-8RnKyiqWGffpmBLHaNthdRcqAMrwI-2_Ajy8Ekv92Gglm5Oh53Wt8LIK9QPFZZDvlud-CdCkuxA5TBaq_YRkFbOaGsuIi-aLYxndFnriewC6OFUdljCXK_R04WxKkurmtvlvzYrx1sXjSwfvpo_BhSrXnDopOefGLovKC9TlSs4F-5uOG8vvWVByXiY2F9T9brhZ-1JM0ayPB9viEWxikyNRIF-51uY9uptk7BOgbQhqa5PBPytNyNgcfM9JOJlmFQWVas-i-T58bNJnzq-3gRMpT02HgEZoCU3WGNX9uw-_YgNCQObA8PN04_FjjHjBRIPjE14-mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند: اگر دقت می‌کردیم می‌توانستیم بازی را ببریم
🔹
به کادر فنی و بازیکنان خسته نباشید می‌گویم. به مردم ایران تبریک می‌گویم و دست تک تک آن‌هایی که ما را حمایت کردند می‌بوسم
🔹
بلژیک یکی از قدرت های دنیا است و قبل از ۱۰ نفره شدن فشار عجیبی می‌آوردند. آنها بعد از اخراج دنبال اشتباهات ما بودند و خدا را شکر که مساوی کردیم.
🔹
اگر دقت می‌کردیم می‌توانستیم بازی را ببریم. بچه‌های تیم ملی امروز برای تمام ایرانیان با قلبشان بازی کردند. امیدوارم مردم از ما راضی باشند.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/443888" target="_blank">📅 00:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443887">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">قلعه‌نویی: از تعویض های خودم راضی نبودم، حتی شانس آوردیم بعد از ۱۰ نفره شدن بازی را نباختیم.
فوتبال همین است، مثل بازی قبل تعویض‌ها جواب می‌دهد ولی آنهایی که در این بازی وارد زمین شدند توقع ما را برآورده نکردند
@Sportfars</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/443887" target="_blank">📅 00:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443886">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/707c34c86a.mp4?token=kTv-Ca5_cvzTSIYHZeoG10ihCLwGY50XX5x5r-beZgS3qDF6Apt4S7tm9CETZrX7bo94ldvMaXujIJofLtaxHlyPh8pFO3NOZWLLg8bOPiAR_leysiFaaha-x8Akwn6At1ZYOXgY6_Zy6TgJm7DB7ODaGiBMzG3AnLgDPPsJypuJWWRfu3qFuFEd9U_6A51okPMISzJnfV7d80MrpMLu1FwNDr1tgjNCXagA2zGqvbIaLwTztunrOU-JMDl0G9pmMYCf6hflRVHMeFsFDVOzspi4kgPwJbDqn3mtzbYrnsnFUiXroSa8plN2h3QvvgZSKrhb7EHdWpcWRR3n_TALIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/707c34c86a.mp4?token=kTv-Ca5_cvzTSIYHZeoG10ihCLwGY50XX5x5r-beZgS3qDF6Apt4S7tm9CETZrX7bo94ldvMaXujIJofLtaxHlyPh8pFO3NOZWLLg8bOPiAR_leysiFaaha-x8Akwn6At1ZYOXgY6_Zy6TgJm7DB7ODaGiBMzG3AnLgDPPsJypuJWWRfu3qFuFEd9U_6A51okPMISzJnfV7d80MrpMLu1FwNDr1tgjNCXagA2zGqvbIaLwTztunrOU-JMDl0G9pmMYCf6hflRVHMeFsFDVOzspi4kgPwJbDqn3mtzbYrnsnFUiXroSa8plN2h3QvvgZSKrhb7EHdWpcWRR3n_TALIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بعد از پایان بازی با بلژیک مهدی طارمی تمامی اعضای تیم ملی را دورهم جمع کرد و با آن‌ها صحبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/443886" target="_blank">📅 00:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443885">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oM9DkzHB7irygqG2Tcg1cmHE7m6GwvEt4mzOEoXpX9PrteXvPXgRqsQ2MqItl0gC2MvetjKi1hPzD9fNfk4z4_rN4KDRMXE4YNKAScw-n1M_-YgWbvzEz085OUFpUXVzKq3tWtJfbmPeN9GRo3-whZsvtOZBrPKQ6cRNfIpa81q7f47cxAwS2m6_7BUaxeYv_QERWx0PvxHto3npTqIjZnmLJOaDsTpiyqgW7zEakCFS2MM1hUOBzJXEvY2ajxBFMTIuWLd7sLPKumIGNuIsrXrkSgNZDh3mu0T0o3P3Y1Te21Ovj-aEuvYfuvTtTd-0vNGxAUB9pdlAB35kpSrqvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جدول گروه G جام جهانی پس از تساوی ایران و بلژیک
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/443885" target="_blank">📅 00:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443883">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUvr4fi6JdYwX4EoaVhIg_4F9rXyD9YYFPmfE4KBWabUoLGQtO2_rR6rJcOzQ-GEJQ-iHh141LzIx5L-1WzvSFsF8Q09Zxo4pe9NP4qAeF1J5wTq98BnQrxuJ62dTL0eHbyQ4BdjJ5afIBlno23whimJWphcOyCGNrRk5aMv_UZi8K7mOs9mZubDN7j3agPvMwhCAM-4JLeEmzqm3TvePMtQF6lYGX7I0b2xdoe8DaqiUk1b2TWlaGn-vYzZrQRB5XkverFSev9CS_Xx9yeXIRKA2anHW9r4uND_R5q0_mim20sCvOnuxhaxqV0dcY-SSlpT3Jk9LnCVH2bOk0yxVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
علیرضا بیرانوند بهترین بازیکن دیدار ایران و بلژیک شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/443883" target="_blank">📅 00:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443882">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1HqJhu9N0ca4jx3yIFZPu-s6bxSpTzfM0bbuXrBfb0w2gFTuEqclwlcpOrkgU88IW5_0yvR4wtoAHF7DQdsflzg5_V6GkbSO5mwE2jtb1W4UQ7RusQI7f6BWqQCbhYS8jJ6BGTVhT8I4z_49OjCyRG55evl8b56wvN1I8YiiSDZEIIwC24OKkwttsCyzKko9tJN3H1fv50A8kBw7p7lUzB7IRkqiJWpZE-aUc3d1cRmLJo2e4BQcxY1lzD9E4ThXba1I1EQxGXG3ecBvOXT9sdkpp-hdHs_TqToeDENYElMMoSDd4d08WPClvggTbd7KfvJCIfno5qm_6FfdjJ5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران با متوقف‌کردن بلژیک یک امتیاز دیگر گرفت
⚽️
ایران ۰ - ۰ بلژیک
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/443882" target="_blank">📅 00:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443881">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deec9c986b.mp4?token=rEyyFRo0c11II1xbg79sJv3kg7lgdGEru_XI0IxqNv911INfgJWojFs8gKVfi6LV6tX2sNnsyR16N2rTe1HCcHYnwPkZ9tYZRvqwYxbx2O6_OOam-Vd2yiKPVNMisNnln3fMud6mSNExsPlAEoRhumsp2MGz9rssc0NEyp9N8hBitOv0PgMgAaUgaUH1oUVfaPTvChvhxf3se6jzpaMq1kGpSH7Crxfs2puoD3k6blE5AC3q9dj5jwhv-nc6UnCDtGSRm5W3nSCSA-SmGWUdYlK_fjTzxy0OewV4Hm3-MfykRxREu20qtGrRPLqzz8ipeJ-1kQzBtjiZW3q59Suy3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deec9c986b.mp4?token=rEyyFRo0c11II1xbg79sJv3kg7lgdGEru_XI0IxqNv911INfgJWojFs8gKVfi6LV6tX2sNnsyR16N2rTe1HCcHYnwPkZ9tYZRvqwYxbx2O6_OOam-Vd2yiKPVNMisNnln3fMud6mSNExsPlAEoRhumsp2MGz9rssc0NEyp9N8hBitOv0PgMgAaUgaUH1oUVfaPTvChvhxf3se6jzpaMq1kGpSH7Crxfs2puoD3k6blE5AC3q9dj5jwhv-nc6UnCDtGSRm5W3nSCSA-SmGWUdYlK_fjTzxy0OewV4Hm3-MfykRxREu20qtGrRPLqzz8ipeJ-1kQzBtjiZW3q59Suy3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خروج خوب بیرانوند بار دیگر دروازه ایران را نجات داد
@Sportfars</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/443881" target="_blank">📅 00:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443880">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e86c6c233.mp4?token=Uc0y40C7hPDQdk1B7Gz3K5NU2N6vDQgovR9bUQtODFAY8KPDPwOjEeB8fcplQapTqvSBO2Vq4H2ch-cI3oK9PGxix5ss_Nx5ZgVskNpNhNYUuhITs_2RbIghDNix6uyPNuFY_IJzPD9mip_ig2jKcg19zZbDOWFEpKcn-O9VDMKMMVvCRwYkf5zG24nvVEcNUsx-vrhQtneHxizcbG45c_IrI6kAFWsrcep0iTDOm3Bfs6SPRRrFj6gohZvzL55WbyeJZ1HHwuY3Dh34aQkRE5lorJSOZuG3f8bDPq1dXE9znBT6Cv6Egjst2bXDFldUXWTdbvbJqLsvzUeJbdKKeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e86c6c233.mp4?token=Uc0y40C7hPDQdk1B7Gz3K5NU2N6vDQgovR9bUQtODFAY8KPDPwOjEeB8fcplQapTqvSBO2Vq4H2ch-cI3oK9PGxix5ss_Nx5ZgVskNpNhNYUuhITs_2RbIghDNix6uyPNuFY_IJzPD9mip_ig2jKcg19zZbDOWFEpKcn-O9VDMKMMVvCRwYkf5zG24nvVEcNUsx-vrhQtneHxizcbG45c_IrI6kAFWsrcep0iTDOm3Bfs6SPRRrFj6gohZvzL55WbyeJZ1HHwuY3Dh34aQkRE5lorJSOZuG3f8bDPq1dXE9znBT6Cv6Egjst2bXDFldUXWTdbvbJqLsvzUeJbdKKeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخشش بیرانوند بازهم مانع گل بلژیک شد
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/443880" target="_blank">📅 00:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443879">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a83ebcb5.mp4?token=QycljBqBMO2NahCbk_fy_EUZX1UHA7fevpqGey3KPncz1TD8w1Xy0qX3whHSGws1g_NWVgoylauCnzzpEoBtEWeXrcpsHANGGfsamWtqpvjIHDBSSTjWaInYdHxe5gg7YCmEgLiX34wWlZrM_AwYJnRhOsnLW2KySEAKFOP7Bffssyw1pjFC7VGraweJKBv2nCLTxEvzWNHVk_qAPSr1k8gQPhoqyHunUECVhcW97xUs4SP05DWsiiXUhMKfFUEJbncYn32Ppu_DcSYEES0i4Y7ADjioJJ8azWSUeVE2BEaZ4x7xTu4UXsfmBFN1k8VCil6LyBuxvkbB6ioBVLyWgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a83ebcb5.mp4?token=QycljBqBMO2NahCbk_fy_EUZX1UHA7fevpqGey3KPncz1TD8w1Xy0qX3whHSGws1g_NWVgoylauCnzzpEoBtEWeXrcpsHANGGfsamWtqpvjIHDBSSTjWaInYdHxe5gg7YCmEgLiX34wWlZrM_AwYJnRhOsnLW2KySEAKFOP7Bffssyw1pjFC7VGraweJKBv2nCLTxEvzWNHVk_qAPSr1k8gQPhoqyHunUECVhcW97xUs4SP05DWsiiXUhMKfFUEJbncYn32Ppu_DcSYEES0i4Y7ADjioJJ8azWSUeVE2BEaZ4x7xTu4UXsfmBFN1k8VCil6LyBuxvkbB6ioBVLyWgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کورتوا ضربۀ محکم عزت‌اللهی را در دو مرحله مهار کرد
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/443879" target="_blank">📅 00:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443878">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7oCu23035UMnPCkea-VQMPL4Iu8pgGeXUsNKASKGdbwORxPc7juHMIcUNlyKvYNyBHJp9Vx6RD6VvUJ_r5zAGNm8H7qWzcWwD4CGWrKZvH1BSZDfkZjFbFwxacd4BTFU66-IJo5QrZE5PxG1AwTMb5UryKnFjZseSapv6dt9gEKxJ-c6cIBs_nUU0l_9V4swc6CzX_BHp6kY7q9OXBR3rlDpbJZ4bMm2oMpLdZBjN-OYLFMWLfeMi4wWwRGXxVmLTYZ2DyPSmCeq000wjSC9evpnMUeR3plTA1TPtBRKEZXywNwbfETTHaCwfq9HU-TNVWw9-pvfaVZHum6o3qGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بیرانوند با واکنشی تماشایی بلژیک را در حسرت گل گذاشت  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/443878" target="_blank">📅 00:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443872">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oeiXQsANeMCDehDTWzgM66ba_aFMKGwYesNQ5-1BxjrpmawU8Id3ZEZnxiGPo_l8WdLO4dspvNJjwLMhCbxWPZ8q0udXQTDK2Fz-wiTHZ3iO8vdVTJuSZcTE7rU95kjLgE7Avni32jZQy_-IPkBzkt5u6GtUINZg0zXqdTFTj9F1lqM0NXxqF_DJgMMG9Zir2TvxVKrKWKHaV0346QH7cnzO_NC6Eqt0u76DS3U1v7f2TKzMJd4e1zTJQDOS0BgMU1XnLUjsJ_Oz24iUYQTwu2o_nq3yy_fTJFhohJiIztj9TdsfDX1e73eVQHYfhxXaLCE0J9ZwWdkB6i7e-AFC9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QBmU3cWT8rCuLL7JLEnrb22BFzzPi9ePGDpFF6upO6MSW1s7QEAcBKkaejVEh7jNOr5Omte4nyEwqWMvHh-4HLMbOxe1DxRFUiQ4ConOY2yo4pmsEQ8o_c3F2qX6ckW_ieL7-RWWJtjGznZSwClMWfD-fcpld3E3i7wJYlxE5CAjmRyNIWuoQI44lZNjjHoqMamBXCK3jv3pYyViWTkK_aHPE3IzzhsbSySvKrl5SFqIWte4HN3jL278Y7ig97XbCsyRD-tQIDA6t7zSZddSLp0rxQf5DuSH_FMqFnIxVX62SKSPIySWRqjGY-kNRpluLjg1tHeOAh5aJ-7cmf5BPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_GnS7t0kjkboQ-CXCeCneIqRAYHhqiQwDJJs596Uaa5FnppsjAKuU3aMzWX-uu8XIEoOxLpw5Qg4Ki_CFvxgPUSfezMmzi5IAGmNPGfhLXMixzHjFHikduy6P0_5IbubW1pvjXhg9DOUVOLUr9jwuE-jB_RVATScVTIHD8jsm5SJ_sEyWW8MTBw_YPViP3Y53u2q8sFD_SF16fBEph_jHsw6MRE547NDv2dfr-HtNMsHPffdrMTbnuhnvSlEqCbWNgvZGKYJL_2SeEeDJQZkhBYrtDijtrnk7VHkBfNRmmMI3KvOP5awk4ntlgPvv5B9zO3yew7POl44DCUAKQsWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c72f3ba2.mp4?token=dgQ96_Pj_XjdBKNdbHtpdGqWlFOJLQi0iQlITM75Nfs6ON7r92rJShL1jmrmomKZRwfKxB3swZryLokNSq49giXmVT3BLx16r65gM2f-zHTLtP3GB0d2HVL_ZtlZ8issoIoHI_u0lHVCPB6PnFm1AB5kMzhFD2lSUjmXGwjJbK2Ew_9KAgzuKKLwCDttIoQ9jSEWQ7sFHrzQHlJ7J-4dTnGlniM93u60wRwwnuiQs5h6Ixzd8LldUIUjfP5jDkYtsuu_D1bnmAe-ZGM5sipofE-Pf8eeJ7buGtzv9pRSzs7khJngSxwaXDbH7jXjLWLw4g63cUjh_z4oSScgaeARLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c72f3ba2.mp4?token=dgQ96_Pj_XjdBKNdbHtpdGqWlFOJLQi0iQlITM75Nfs6ON7r92rJShL1jmrmomKZRwfKxB3swZryLokNSq49giXmVT3BLx16r65gM2f-zHTLtP3GB0d2HVL_ZtlZ8issoIoHI_u0lHVCPB6PnFm1AB5kMzhFD2lSUjmXGwjJbK2Ew_9KAgzuKKLwCDttIoQ9jSEWQ7sFHrzQHlJ7J-4dTnGlniM93u60wRwwnuiQs5h6Ixzd8LldUIUjfP5jDkYtsuu_D1bnmAe-ZGM5sipofE-Pf8eeJ7buGtzv9pRSzs7khJngSxwaXDbH7jXjLWLw4g63cUjh_z4oSScgaeARLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد شهدای مدرسه میناب در ورزشگاه سوفای لس‌آنجلس
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/443872" target="_blank">📅 00:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443871">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">حیدر سلیمانی، کارشناس داوری فارس:
✅
داور آرژانتینی برخوردهای جزئی و کوچک را خطا اعلام نمی‌کند و سطح خطا را بالا برده.
✅
البته طارمی در دقیقه ۵۸ به شکل غیر طبیعی خودش را سرنگون می‌کند و داور هم این موضوع را از قبل مطلع است.
🔴
اخراج مدافع بلژیک به‌خاطر جلوگیری از موقعیت آشکار گلزنی صحیح است.
@Sportfars</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443871" target="_blank">📅 00:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443870">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2bc3e0ee9.mp4?token=SzhfF4PzWJNVLI1GspF-ELkRyMRShjDdZSp5WlqNk4_i5zzUG9_aUNZ7Pp98uFV3LAYKzBblB12Q9E7t6n6JyYPTM77qR6ufkOn26euycNWQAQggWmDUa_JIh0XDgTYaddVkYZ6YEFemtPYXoiUjGvoUJ4YEHL90GBdefgOqPKz-7KBMpTE-jBr6yY1tlsypgJXvafThqBYKdbgH-8cQ9MkvIBwFNPmG-ppYKYSoLct85f06iWjLEc_jD5Op4gRfeejPiwxoWJZjLhV-cFUg6DYGat0WbLGOijpBqWfw00fsOJrsB3w_OtLxqVNt0jqh9B1PsUP604YR4yjYn1wiHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2bc3e0ee9.mp4?token=SzhfF4PzWJNVLI1GspF-ELkRyMRShjDdZSp5WlqNk4_i5zzUG9_aUNZ7Pp98uFV3LAYKzBblB12Q9E7t6n6JyYPTM77qR6ufkOn26euycNWQAQggWmDUa_JIh0XDgTYaddVkYZ6YEFemtPYXoiUjGvoUJ4YEHL90GBdefgOqPKz-7KBMpTE-jBr6yY1tlsypgJXvafThqBYKdbgH-8cQ9MkvIBwFNPmG-ppYKYSoLct85f06iWjLEc_jD5Op4gRfeejPiwxoWJZjLhV-cFUg6DYGat0WbLGOijpBqWfw00fsOJrsB3w_OtLxqVNt0jqh9B1PsUP604YR4yjYn1wiHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
بلژیک مقابل ایران ۱۰ نفره شد  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443870" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443869">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚽️
بلژیک مقابل ایران ۱۰ نفره شد
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443869" target="_blank">📅 00:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-443868">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fada0446b.mp4?token=jvgvNH4F6_E4qMxPeH2CkmQCKE8ELNONzhhn5oqmRHDV8S4QBBNeyviST0se6yIcPNgmS1i9Di-fkgbEPnA-DqlDEgMNLIHWNibWVNCmZfTrbMQLBPfT5eaACH-mHcwFMCugaiYrACNumfmCoxW1IRAQQ1r97LNd-Rg6SZ75z47h5qETZXQCc6_M5HYVJTC6SMrFmxuXbSI4y6lBcS_P1r8B2sRPIpZQWXbpkFAHNNyiEln3KetrxmbUQ5gEJ6Qs722I2bIVbCdj--pTHtKfVV886FxARSoyeqChdTWmankEYILPYuOmXRf84Gl5mdEF5JNuLjeoNlR4p9cf7C9P_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fada0446b.mp4?token=jvgvNH4F6_E4qMxPeH2CkmQCKE8ELNONzhhn5oqmRHDV8S4QBBNeyviST0se6yIcPNgmS1i9Di-fkgbEPnA-DqlDEgMNLIHWNibWVNCmZfTrbMQLBPfT5eaACH-mHcwFMCugaiYrACNumfmCoxW1IRAQQ1r97LNd-Rg6SZ75z47h5qETZXQCc6_M5HYVJTC6SMrFmxuXbSI4y6lBcS_P1r8B2sRPIpZQWXbpkFAHNNyiEln3KetrxmbUQ5gEJ6Qs722I2bIVbCdj--pTHtKfVV886FxARSoyeqChdTWmankEYILPYuOmXRf84Gl5mdEF5JNuLjeoNlR4p9cf7C9P_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧤
باز هم دفع خوب بیرانوند
@Sportfars</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443868" target="_blank">📅 23:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443867">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7835d332c7.mp4?token=qGZqWqPcGzNzvi-9hIDSZx4-d9fuLI62arMsavd-KzwEzhzPkUdo6RrrPzDRq5vjEFY4Q7uPjAdW8Lc7NKhZbe73Hza99pfIBSEzlmcQh0CA_gKfyEgVuNMyeVG4YOVQlv6yP8_50jkYwoV1JRggBlK4yeIj8xhRl5HaevcIRAjMP-95sbP144LqOskzEiMFhuxGyAvMp0Ap1JcQwlM8D23Fam8OMp-5RDh0GibTbO3zDKcygr73_-4f80nWBU-UKGRBNt-Vfrg7uwQCg1IiXUtkZkWlERJ-iYme64XEcC1QPN1LtpUySLoUodiO8QqGZ3XomXb-uqBMj658Nb6kGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7835d332c7.mp4?token=qGZqWqPcGzNzvi-9hIDSZx4-d9fuLI62arMsavd-KzwEzhzPkUdo6RrrPzDRq5vjEFY4Q7uPjAdW8Lc7NKhZbe73Hza99pfIBSEzlmcQh0CA_gKfyEgVuNMyeVG4YOVQlv6yP8_50jkYwoV1JRggBlK4yeIj8xhRl5HaevcIRAjMP-95sbP144LqOskzEiMFhuxGyAvMp0Ap1JcQwlM8D23Fam8OMp-5RDh0GibTbO3zDKcygr73_-4f80nWBU-UKGRBNt-Vfrg7uwQCg1IiXUtkZkWlERJ-iYme64XEcC1QPN1LtpUySLoUodiO8QqGZ3XomXb-uqBMj658Nb6kGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند با واکنشی تماشایی بلژیک را در حسرت گل گذاشت
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443867" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443866">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d60bcbedb8.mp4?token=gDxsOFm0SZrxeZ7nAmuTlDHok2QFFlKJwqWDVcYQAbp0csDMLocG_oE1JAU3YkMwd9PSYUE4-vxwASVcgaBAu54ihErz4maoMPJ7JACx9gWyQwkYTjghwkN2gBGGYYydNjy1WRqW9-hcd-8ej_WPf9Si6tqaaN_mj7-OlsNjPfxj3h7N22mfTLrVr6V7iurBgEoP4bAWabeaXMogIuS6JPCLF2FjOM2EWL2acIYyXEGbkfUsWj5AR3SgJt3SPpyrxQTITfoNsbYH2VYAgXtIjc3ZHzL9UeqCNje_g155NZXMnfMJfslSiEDRq8oAa0oee4omB1hnNMMzjHhF4odEmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d60bcbedb8.mp4?token=gDxsOFm0SZrxeZ7nAmuTlDHok2QFFlKJwqWDVcYQAbp0csDMLocG_oE1JAU3YkMwd9PSYUE4-vxwASVcgaBAu54ihErz4maoMPJ7JACx9gWyQwkYTjghwkN2gBGGYYydNjy1WRqW9-hcd-8ej_WPf9Si6tqaaN_mj7-OlsNjPfxj3h7N22mfTLrVr6V7iurBgEoP4bAWabeaXMogIuS6JPCLF2FjOM2EWL2acIYyXEGbkfUsWj5AR3SgJt3SPpyrxQTITfoNsbYH2VYAgXtIjc3ZHzL9UeqCNje_g155NZXMnfMJfslSiEDRq8oAa0oee4omB1hnNMMzjHhF4odEmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کورتوآ دوباره مانع گلزنی ایران شد
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443866" target="_blank">📅 23:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443865">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb8be175c.mp4?token=ZaqOsoj9XEY8RhtRVmZxHiaVZlc075SL2U6J5NIBSOSgogP54OoTR9CAUBKNki5fqbjF7EZ9wRkCyL5GeP9I_P85IW9fxMrPIB8UoZ63Hd7Cvvp2aiqNs-ACm1cYSz16KVFvcaJmsgZeT5ShEvpb4_HlLp3jAo7pY3sJETR6B4M1lbTmTKwoGTO8vnA1TJz4oek95FvdADQI-kjKVIq_LoKOLoQvpFKZqzVXu0erL0tn5LBCPKuYV8WUqf-EBU1nMQIEmvMY5qeXm6q_XYQ-qJo0VKndmEcNqqhzlLge5fvGRm9-7PQnt2bMU01_wCq6aSgey1GJHufTaP9TWXcCPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb8be175c.mp4?token=ZaqOsoj9XEY8RhtRVmZxHiaVZlc075SL2U6J5NIBSOSgogP54OoTR9CAUBKNki5fqbjF7EZ9wRkCyL5GeP9I_P85IW9fxMrPIB8UoZ63Hd7Cvvp2aiqNs-ACm1cYSz16KVFvcaJmsgZeT5ShEvpb4_HlLp3jAo7pY3sJETR6B4M1lbTmTKwoGTO8vnA1TJz4oek95FvdADQI-kjKVIq_LoKOLoQvpFKZqzVXu0erL0tn5LBCPKuYV8WUqf-EBU1nMQIEmvMY5qeXm6q_XYQ-qJo0VKndmEcNqqhzlLge5fvGRm9-7PQnt2bMU01_wCq6aSgey1GJHufTaP9TWXcCPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443865" target="_blank">📅 23:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443862">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c68b3facd.mp4?token=mCvc_3DI6cB4maw1Upp8rrqiG_uSMN50x-XhRWFQdAPCzocLOPKRI8WGOnMoi0MUSPvJuzZzTBMYqF72_ZidBUKou0JIKs3HnB4VnyiAIXMbtuxRX8dFakpx588dvbFlZCFFYl2QuGSdaITu79WsK4zD6P52Xe-rg2aFbGavzhPwaLBQOvnKEtlPLYiiPOfv6Lmc8_4ejhlwGWBUUL38omCn41wdmk8seN6XzThEt_2bFXAb3yIOuGgVTESQeDIeaMVXz_1BqKhYTKc9DjpLb4bnTg9EaZ3rJr41_eDdqte-4zcBE0DjrvChqwIm5oafXPknbK_paJ8ZBt7JxYEDiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c68b3facd.mp4?token=mCvc_3DI6cB4maw1Upp8rrqiG_uSMN50x-XhRWFQdAPCzocLOPKRI8WGOnMoi0MUSPvJuzZzTBMYqF72_ZidBUKou0JIKs3HnB4VnyiAIXMbtuxRX8dFakpx588dvbFlZCFFYl2QuGSdaITu79WsK4zD6P52Xe-rg2aFbGavzhPwaLBQOvnKEtlPLYiiPOfv6Lmc8_4ejhlwGWBUUL38omCn41wdmk8seN6XzThEt_2bFXAb3yIOuGgVTESQeDIeaMVXz_1BqKhYTKc9DjpLb4bnTg9EaZ3rJr41_eDdqte-4zcBE0DjrvChqwIm5oafXPknbK_paJ8ZBt7JxYEDiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسداشت یاد شهدای جنایات آمریکا در میناب و لامرد توسط هواداران ایرانی در ورزشگاه لس‌آنجس
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443862" target="_blank">📅 23:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443861">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2hkYACQV26Lj2xQMvwAdgTOUv6tXC7_qS3nD0Cc0AKZbOD7ObCb-qs6_UhEQl1PJ0b7xEvnevTTY6h2ZokyJABEbRQ3qAMdERWkO2leBFIz0_6o9dCIfil9L6qfWsobwdjkeYVheSzFWwZn3kTh97OByj16QWhR5RdvQVg32ioRxWYT-_4bIlrtODB1h5oz4cgnHuAWEFdI0fYAeWRfYhCfKeo-b-BfxIVQb5cuVKKstAcl4IKE7vJbNF0KjQE9NH4NuR37r9axHBLjGWHCuiex6zw1q-bCAsR0bqzpHpImeiAS9dAhYN7_E4t84eH4nUx3aHSvkq67eEmoCgaqtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پرچم یا حسین در ورزشگاه سوفای لس‌آنجلس
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/443861" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443860">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">جام جهانی با تحریریۀ فارس
نیمۀ اول بازی ایران چطور بود؟
🔹
ایران در نیمه نخست دیدار مقابل بلژیک، نسبت به ۹۰ دقیقه بازی برابر نیوزیلند، عملکردی به‌مراتب منسجم‌تر و پخته‌تر در نظم تیمی و سازمان دفاعی داشت.
🔹
قابل پیش‌بینی بود که بلژیک با اتکا به کیفیت بالای بازیکنانش سهم بیشتری از مالکیت توپ را در اختیار بگیرد و ایران را به سمت فوتبالی واکنش‌گرا و مبتنی بر دفاع و انتقال‌های سریع سوق دهد.
🔹
در چنین مسابقاتی برای ما، موفقیت بیش از هر چیز به کیفیت بازی بدون توپ، فشردگی خطوط و توانایی بستن فضاها وابسته است. استفاده از سه مدافع مرکزی در کنار حردانی و حاج‌صفی این امکان را برای تیم امیر قلعه‌نویی فراهم کرده بود که با تراکم بیشتر در یک‌سوم دفاعی، فضاها را بر هافبک‌ها و مهاجمان بلژیک ببندد.
🔹
مرکز ثقل حملات حریف هم مطابق انتظار حرکات کوین دی‌بروینه و لئاندرو تروسار بود؛ بازیکنانی که با کارهای ترکیبی، پاس‌های عمقی و همچنین انتقال بازی به کناره‌ها و آوردن توپ به عرض زمین، چندین بار دفاع ایران را تحت فشار قرار دادند و خطرساز شدند.
✍️
مهدیار مظهری
@Sportfars</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/443860" target="_blank">📅 23:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443859">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
موج ۱۱۳ شب‌های اقتدار در بسطام سمنان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/443859" target="_blank">📅 23:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443858">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b03afac6.mp4?token=W0T41gsvvkAePy3knaOiAI68lv1l3K3xxELbq60p-Q15SNWam2Qs3tbPa4xz24RDOOyF1ir6g_6zXkN_V8Z-B0veWQElEEmodFAPx9xLfMM71NmAWzpIOfeKoRzmABcOkH40XITpo7K382GBHXsVCsAlJjNxTEB9u8tfPvFMBr7_c6hC8Q12rwDC-NUgh2jPtOesrosWXNLh72-7I6dv-mJXtp6jWKyy3iX3-I8DUSIRK_6rZCtUAt9kxiq5GTgWG8WeGCffbnNc6mnl-FPfU8lySRFGqI_DLyhEXzM8LTQ4dhgUUOnyCtnKJEA0capG3cRNIfxdnTrcDTElQKwMj2M-ZhIlHWtvG1fZKX5_UcPJnIst5Ad5Hb2xgLbPyvszUblWr5gQQVDor7TS0ozuX6xFNYHfaCn9Q71jET0f2nJ_7dg1U80lC87Y5wsgHN9Zb0h9orenL85xPAen06vZzuszb9spiEqwpPplVx4-nQG6C747eQTBJ3FGWi7vK1WnTcEYcZZ_MTeRqjNw5hkWFJTK6fAH4BMVaiJ1hF-Em0N-A6qIf0ED5koQ484zpUKoqxvCjGtdIUYKMWehiQPg-__sYsbbxCuhY0C8ZrAprZ-PnCgP9LpTC-1HjXGimeXRg12W4EtRH02NbgAtS4NFgBdUg7dq8UA54AG4uPGTi5U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b03afac6.mp4?token=W0T41gsvvkAePy3knaOiAI68lv1l3K3xxELbq60p-Q15SNWam2Qs3tbPa4xz24RDOOyF1ir6g_6zXkN_V8Z-B0veWQElEEmodFAPx9xLfMM71NmAWzpIOfeKoRzmABcOkH40XITpo7K382GBHXsVCsAlJjNxTEB9u8tfPvFMBr7_c6hC8Q12rwDC-NUgh2jPtOesrosWXNLh72-7I6dv-mJXtp6jWKyy3iX3-I8DUSIRK_6rZCtUAt9kxiq5GTgWG8WeGCffbnNc6mnl-FPfU8lySRFGqI_DLyhEXzM8LTQ4dhgUUOnyCtnKJEA0capG3cRNIfxdnTrcDTElQKwMj2M-ZhIlHWtvG1fZKX5_UcPJnIst5Ad5Hb2xgLbPyvszUblWr5gQQVDor7TS0ozuX6xFNYHfaCn9Q71jET0f2nJ_7dg1U80lC87Y5wsgHN9Zb0h9orenL85xPAen06vZzuszb9spiEqwpPplVx4-nQG6C747eQTBJ3FGWi7vK1WnTcEYcZZ_MTeRqjNw5hkWFJTK6fAH4BMVaiJ1hF-Em0N-A6qIf0ED5koQ484zpUKoqxvCjGtdIUYKMWehiQPg-__sYsbbxCuhY0C8ZrAprZ-PnCgP9LpTC-1HjXGimeXRg12W4EtRH02NbgAtS4NFgBdUg7dq8UA54AG4uPGTi5U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران‌دوستی مردم آبیک به ایستگاه ۱۱۳ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/443858" target="_blank">📅 23:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443857">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7d2c52f9.mp4?token=iLvEGQBu89NI2ngsZzY_xq0YFdr-UtdJ7lZvUOYuyY0mgKv0q5tRRvMmTT9EWxRkDnzSb-YTvBKbDbIv48HqdYhysrhhZGL8-QzGpM0VPh_nDnJM-2qhyePYskTM9z4zpwFhH0DSa60WKUhHsv4wpY7RUuSIW0ecb6_IqY36_I2Qp8HG2uQj0_OOCUT67wZcJBMDo4nAzQyjQabvnAog7tt63MRjDfk-TZv_N70bI2LmB2wYdBm6shF2YhNYr-xcVrU77-eVzPXHS-FukCWlFJwXUpGIW8qUMJ21GEpryoOFs_SnzO1ueevWaQtOM-yz87uRN_gFcZxN5lqU9-ngpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7d2c52f9.mp4?token=iLvEGQBu89NI2ngsZzY_xq0YFdr-UtdJ7lZvUOYuyY0mgKv0q5tRRvMmTT9EWxRkDnzSb-YTvBKbDbIv48HqdYhysrhhZGL8-QzGpM0VPh_nDnJM-2qhyePYskTM9z4zpwFhH0DSa60WKUhHsv4wpY7RUuSIW0ecb6_IqY36_I2Qp8HG2uQj0_OOCUT67wZcJBMDo4nAzQyjQabvnAog7tt63MRjDfk-TZv_N70bI2LmB2wYdBm6shF2YhNYr-xcVrU77-eVzPXHS-FukCWlFJwXUpGIW8qUMJ21GEpryoOFs_SnzO1ueevWaQtOM-yz87uRN_gFcZxN5lqU9-ngpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۱۳ شب حماسه و همدلی در گرگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/443857" target="_blank">📅 23:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443856">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📷
نمای دیگری از آتش‌سوزی در تاسیسات راس‌لفان قطر  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443856" target="_blank">📅 23:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443855">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQXPpyj9uM2mwfhJQES7zljb8FkWDdifBTv3MUaiI0oUKPOuROLkYFi-u9TwsDS-e-qVXVVbCmi4ZKJgFvtbSMIJZmoxQEaLUuhqLho9eckRucTA6bF8j21ljssPp-O6b1x-e3pFqMQT6fCLn3oH7b-Soos-A_vqfq7PC8gxDNNo4JX_DlbT0V5NXDKY6wSCYBgNSpAtWam3bUDNnV6rfnHI8GukwUaDxtAfpNIFx_NY5Y51hQJAhXVA_ZqrWlM5FFNklv1gJrk45RBQzlUjdWYjBC6byCkTkCQcj80IaYC7SewS4yX19AG5y4D260bj1J-_lMLvSx_Yhx_GtaecjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
برخی منابع از انفجار در یک ایستگاه سوخت در تاسیسات گازی راس لفان قطر خبر می‌دهند  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443855" target="_blank">📅 23:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443854">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPMSHgD_9blJH1ZdMBHQBgvDOBSCRaqDweGCfQxPaC0uIVPjd8SdOFAvNxHzw5WJQwUJ-jzx9m0OW8l0UPMrzb3EnuvbRp86OVtAMA9Zer0KidqBJJ8B6IMWyTU9-0SoeOMfAwnFg6sxIrPRnR8yzsPCNvTtXaHzu3eY5TaJuDd0fyGm8Nmr3X-Zm4DPhT62svqLNee4VmL3bcumakCe9s24MzVtVUKwoqJ6wYY5tC4CT9NspEPn4xAi0hJ45SaOYjeelZmmubA60YEbjlCk3jKFKF5M7FsmfzXDpFPt3QPTU3s7XRJOA4T4V3pngR2Cq0Xz3-st998VH3_DKCxssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
شبکهٔ کان مدعی شد: ارتش اسرائیل در روزهای آینده پس از اتمام بیشتر مأموریت‌های تهاجمی خود، کاهش نیروهایش در جنوب لبنان را آغاز خواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443854" target="_blank">📅 23:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443853">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gzk__Oih7bpr3Pus1w_v6H4rxGdeCTXwppc2Z0N9R3gpKKYRm2sJTRajZnjafDOHNCd4_FdLT2x1Shkno6EebiwfqfUuMVlnC3DigCGW2l3xY5h-vb5ZHykPSMoNYqvx8ZQcCZME33X-P3Z4u3IGeuaoVBtjuWc__BA4SmN3WfbDjR8Ons_ZDZQcQjcEYtDewKzQ0_Q_osA91zJq28Gk9IN7NWVnXkqIc7qSi-nMuLCBMmoaP3iz7lJs0u4WL6ayrxOVzAq9pKFLx3oHNCuJR3aGAKBzlKSW7Hbh8ETtytmKIAUL28XU5a_4PAEQsZTsVVHWddw7cN2_3KZhemSKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
برخی منابع از انفجار در یک ایستگاه سوخت در تاسیسات گازی راس لفان قطر خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/443853" target="_blank">📅 23:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443852">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVtb4yFd5GnkmTB04kSftqcsBBfK1n9BuwTytgHBeVBYfGojx7vjPTuS8d36x-fb99T1Ql6WnD3tKq2qjQU4q5uHJWlMStN-MUdzBcGfvcsUZlg4cQ53cYDiwlAR-w-XRIBUGRFU8gWztdmQNs5iW7Dl7KY-cRYfEzEdVElt5mjVONrlJ7YcqV8yfkgoHlrKcBDmB0LHGObIe-YETSb6fcVdRIf7Q1-xjxKpWKsZnNoGHynLnBS1Ndv7UssMijuiF-5HlTrxAKUW_pE907LG1incBIytNh68HZxjBPsh3tvrheVmVQQ-15FgRwPz5PVW7pKRKqxvFkJ0WbSnRvQmoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمهٔ اول بدون گل تمام شد
⚽️
بلژیک ۰ - ۰ ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443852" target="_blank">📅 23:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443851">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔸
شبکهٔ کان مدعی شد: ارتش اسرائیل در روزهای آینده پس از اتمام بیشتر مأموریت‌های تهاجمی خود، کاهش نیروهایش در جنوب لبنان را آغاز خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443851" target="_blank">📅 23:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443850">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f153f4d657.mp4?token=fnb0xzJ5CW91IWkpF0x0UbHWhqZup-4-mh-AUeBCqEXrozaeGmrVELxqNUJwGS_Xq8kN_ZI8dVsRv9aoZrq1X0tNKWNpZeKruA07rotpJDLnbIUUBW8GtA2dQJ97jP3Mdn7-VqohoKtG80LQzLPPhXafnrKDohuBJ-g6UwI40p7YSdLvgh4dmVg8cAYEQOZv3h0z-Us1q0qP4mlOvaT-yInIsRXbs0ceQcx5ny7pxNCoNzyGTI3rge20naFIvkENLS-ffVEKXem73Es2ECoC5oyn-JJWq6EMWFzkQtsh9VR4pD2m7asAEpNF_727Eh6Wr2viH4Fg9rRYkhYLMoxtog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f153f4d657.mp4?token=fnb0xzJ5CW91IWkpF0x0UbHWhqZup-4-mh-AUeBCqEXrozaeGmrVELxqNUJwGS_Xq8kN_ZI8dVsRv9aoZrq1X0tNKWNpZeKruA07rotpJDLnbIUUBW8GtA2dQJ97jP3Mdn7-VqohoKtG80LQzLPPhXafnrKDohuBJ-g6UwI40p7YSdLvgh4dmVg8cAYEQOZv3h0z-Us1q0qP4mlOvaT-yInIsRXbs0ceQcx5ny7pxNCoNzyGTI3rge20naFIvkENLS-ffVEKXem73Es2ECoC5oyn-JJWq6EMWFzkQtsh9VR4pD2m7asAEpNF_727Eh6Wr2viH4Fg9rRYkhYLMoxtog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند بازهم با مهاری دیدنی مانع گلزنی بلژیک شد
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443850" target="_blank">📅 23:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443849">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c65abc230f.mp4?token=jXEs3PUKMs2M6XS-5r1asw-S6mT6h6_X8kFgO5ayDn50Zua-BdiS8wSuWdSPsjGPntcLybTnOSwtaJbL7FgNU-5Fih3ivMHWbdatxYCO5f7hWk1-ptYjUwJXGFwilWdB24Gge06dgJtWpMJES8MNLQMpeAXrdM9KT0aOh_lBe0myN11TTbgNZl646TRZMnG-WcgzFVo0DnSTnT90PorqK84s44i68e12d9RDwjOZDX786KT6q7UM9Cz-nhnOSqJN__EgtUZFM7BSn2sF77gpmcPCgMeUrnMF7Q5bgKpfoPBfIYTKH42TiqLJApQEdK6erF9u6RJrRTz361O7VthujA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c65abc230f.mp4?token=jXEs3PUKMs2M6XS-5r1asw-S6mT6h6_X8kFgO5ayDn50Zua-BdiS8wSuWdSPsjGPntcLybTnOSwtaJbL7FgNU-5Fih3ivMHWbdatxYCO5f7hWk1-ptYjUwJXGFwilWdB24Gge06dgJtWpMJES8MNLQMpeAXrdM9KT0aOh_lBe0myN11TTbgNZl646TRZMnG-WcgzFVo0DnSTnT90PorqK84s44i68e12d9RDwjOZDX786KT6q7UM9Cz-nhnOSqJN__EgtUZFM7BSn2sF77gpmcPCgMeUrnMF7Q5bgKpfoPBfIYTKH42TiqLJApQEdK6erF9u6RJrRTz361O7VthujA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داور به‌خاطر تعلل بلژیکی‌ها پرتاب را از آن‌ها گرفت و به ایران داد
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/443849" target="_blank">📅 23:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443848">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5V8XZQJfmmxZGFX5L_CayvR_zhzvDFZjIoxc8NaDKFIRh-SIYiSJdq-yEwJD07J-HfvkPHp0RyG2myaV5uHWhspVLl9a6c38zBCe3hFLdffL4iLdUcgUNW01HzDNAmytyZj0as8gOdu9ZOsJxBFYO6KcdOYAt84e2SUOQ6BzP1lUZp3KjeWPNxyo-247WSbUe2wKvK3tkQKHluGi4yTTlUIyO00t1ZnFQdUZsevLeF4ZpsP6vhA0slmvKL_EMwmEgTRXGRZKAWI_K3JtGNVbme4NqmRX84yGgiQn3YozgL8zU6CjKzJZycHRT2Wv6Gckjs9tWE9VlaZgql-KMkjNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏁
حیدر سلیمانی، کارشناس داوری فارس: طارمی میلی‌متری در وضعیت آفساید قرار داشت و اتاق VAR آن را تشخیص داد.
@Sportfars</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/443848" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443847">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3ac4f39ff.mp4?token=AAP-u9Suy3nN6emyfj9KkgjDF1x6oP5zIfG-7Aeiyp-cxHUA5WSi8RM6kxHrQDXvg3z4Mu39EjSSY_n1Kr2FuiQ4MFnAaXfBiu2dn_OlmOl2FFigQHqiintJLLGMN-tefdd2rhBjoJ5T2FRoRKRlki_yqoGTZ3bOyy64s30_m0f454ghN6SSi6eXt-47DsWRVRPY9NHgb_AlwMLo885kGcpw1-E6mhMcQ6EBKEOnPiCnnoojPtGEICGvZjAFE9YWlnDnfBvAfT2nMjBfleQU5KAgqR7RzLpuwI2zstUM5Dz_wbZkM-b-s0Bi-n8BRVJMNTXvKLAPJ7i6MnFuPccUKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3ac4f39ff.mp4?token=AAP-u9Suy3nN6emyfj9KkgjDF1x6oP5zIfG-7Aeiyp-cxHUA5WSi8RM6kxHrQDXvg3z4Mu39EjSSY_n1Kr2FuiQ4MFnAaXfBiu2dn_OlmOl2FFigQHqiintJLLGMN-tefdd2rhBjoJ5T2FRoRKRlki_yqoGTZ3bOyy64s30_m0f454ghN6SSi6eXt-47DsWRVRPY9NHgb_AlwMLo885kGcpw1-E6mhMcQ6EBKEOnPiCnnoojPtGEICGvZjAFE9YWlnDnfBvAfT2nMjBfleQU5KAgqR7RzLpuwI2zstUM5Dz_wbZkM-b-s0Bi-n8BRVJMNTXvKLAPJ7i6MnFuPccUKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل ایران به بلژیک به‌خاطر آفساید مردود اعلام شد
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/443847" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443846">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0bca6b693.mp4?token=MoHoIofdPIrniE9HtyYF0unR9rF8AwN2hkaInHrH4kaq7jz2Seqnk2LOXbWvHtZXqVOFZ38Avi8ZE9uxF7roxqlnuLWAQDmuAPPoBBtuFmpWSvnbFqaBEcC1fBJpSBvyEjjESQhzrrpUX3WMv2uJQ6jfjQj44wjDXuj9TWn8jV-5sZg7Ht0E9K6PcNUtJuLI2_10BcUdrIWXh4DTLaMw5zI3ZIAn5vfH7Az4tg4j4OOW_VmURZ_0g1lpSzQJzHvd4c4WkcnZxmIvhD11EH3lb1Y5cGoELHLst9-F2yfyIKznmycYhIAU7OHq1PC8ucLgHUHreBwentZfMLr8YcrKuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0bca6b693.mp4?token=MoHoIofdPIrniE9HtyYF0unR9rF8AwN2hkaInHrH4kaq7jz2Seqnk2LOXbWvHtZXqVOFZ38Avi8ZE9uxF7roxqlnuLWAQDmuAPPoBBtuFmpWSvnbFqaBEcC1fBJpSBvyEjjESQhzrrpUX3WMv2uJQ6jfjQj44wjDXuj9TWn8jV-5sZg7Ht0E9K6PcNUtJuLI2_10BcUdrIWXh4DTLaMw5zI3ZIAn5vfH7Az4tg4j4OOW_VmURZ_0g1lpSzQJzHvd4c4WkcnZxmIvhD11EH3lb1Y5cGoELHLst9-F2yfyIKznmycYhIAU7OHq1PC8ucLgHUHreBwentZfMLr8YcrKuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند با مهاری دیگر بلژیکی‌ها را ناکام گذاشت
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443846" target="_blank">📅 22:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443845">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/443af77c7a.mp4?token=Hgh-n6Hp7S7n9jjei6lwuHbzW2qkxShYo_WgeEwYmwjF7EJQ8zh9Rcv_WwEpHTfAQy5RdfGqmSc9FBb8U4LAYBpAW087ErBMvy8cGmDv3Rj6zRvHHjqjQYdfgRws_EOqpery0oIKMXJLoQtrMxOPW7pb_5SdpsDhV1SFCd3STmNcqCYArTKsSLmPn-r_xDPzJglStqBqtQN-ISOIR4alkDOzLFwCTvmr6AdDWZCS_v0GNa1N0wABCkQwbjvyT4IJc0RzYj9iyHBjIHUgC5CFZdTVJN9jQOrOrRd_kFfcK7UBMZataZFXBWIGfT5jxKMuvMMP9XRSr5rFUbDP0A4Tdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/443af77c7a.mp4?token=Hgh-n6Hp7S7n9jjei6lwuHbzW2qkxShYo_WgeEwYmwjF7EJQ8zh9Rcv_WwEpHTfAQy5RdfGqmSc9FBb8U4LAYBpAW087ErBMvy8cGmDv3Rj6zRvHHjqjQYdfgRws_EOqpery0oIKMXJLoQtrMxOPW7pb_5SdpsDhV1SFCd3STmNcqCYArTKsSLmPn-r_xDPzJglStqBqtQN-ISOIR4alkDOzLFwCTvmr6AdDWZCS_v0GNa1N0wABCkQwbjvyT4IJc0RzYj9iyHBjIHUgC5CFZdTVJN9jQOrOrRd_kFfcK7UBMZataZFXBWIGfT5jxKMuvMMP9XRSr5rFUbDP0A4Tdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربه سر عزت‌اللهی از کنار دروازه بلژیک به بیرون رفت
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443845" target="_blank">📅 22:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443844">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408201b9e2.mp4?token=CAWHapG7G9D_QVGccs_iBrdun5OPsmivKSEMcClORNJiCZxNTwSYD7brcf68Y6Jdd-YO1A3qV-1eMdIYIf_w7c4LyThVOf9aCEnoSvCIYKz4W2M8qXNq-bDW6xUHcYJDiYKSdKoOGJzJm9RNGiyrMCGWoTPknoniqxsfo78HzzT0tPvtX2nIJIiXNjcredLCxIIj2swkAKUla0hkcHgV4vG7atEHKqzgg09hKLBIw_lO7-U_pxG8TgabOV8sgfvvV9sdEqBam9w9Sel1ABUIMEMwooM5Hdyn2Abl2RhWEETV7o80tgSFxNBOsm_C06BDKObyFY6EKpNveP1jfAJEFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408201b9e2.mp4?token=CAWHapG7G9D_QVGccs_iBrdun5OPsmivKSEMcClORNJiCZxNTwSYD7brcf68Y6Jdd-YO1A3qV-1eMdIYIf_w7c4LyThVOf9aCEnoSvCIYKz4W2M8qXNq-bDW6xUHcYJDiYKSdKoOGJzJm9RNGiyrMCGWoTPknoniqxsfo78HzzT0tPvtX2nIJIiXNjcredLCxIIj2swkAKUla0hkcHgV4vG7atEHKqzgg09hKLBIw_lO7-U_pxG8TgabOV8sgfvvV9sdEqBam9w9Sel1ABUIMEMwooM5Hdyn2Abl2RhWEETV7o80tgSFxNBOsm_C06BDKObyFY6EKpNveP1jfAJEFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کورتوآ مانع گلزنی ایران شد
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/443844" target="_blank">📅 22:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443843">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🟡
حیدر سلیمانی، کارشناس داوری فارس: اخطار به لوکاکو صحیح بود چون لحظه آخر پای خودش را خم کرد و به حالت جمع شده ضربه به بیرانوند زد.
@Sportfars</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/443843" target="_blank">📅 22:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443842">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b488eaafe.mp4?token=cf8CqMzOMeHmOhQRT9FJsXobID1rOpktSY45e2SF5xmehTEGMtt-8n_xTJWTrcSL13Gc2Z3kSIWnuSPmPjQU7t3kLNZUJkBHqmcoGZSAo5Q-XHZPxMFG6zRGzpi2yOBGfcz6yXPkTC59_T5ieRpSBfKrbq2Lix9MaSVEGXY0f52QS11tVNAkVjVmubjo42SJBsJv5X9UykFHMLrvuVI_mD_MKsFd9MwNub_e_41ebraZhiRvvBwgJH-GWAkJG552uh3XPHrYqrquEAb7N9MYyZTKKCoDp5TB7u2Tl-hMi-AuL_rtmxCZ3LU_e6Hv2Txa113Kdu6YEfBdRFDQz34oyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b488eaafe.mp4?token=cf8CqMzOMeHmOhQRT9FJsXobID1rOpktSY45e2SF5xmehTEGMtt-8n_xTJWTrcSL13Gc2Z3kSIWnuSPmPjQU7t3kLNZUJkBHqmcoGZSAo5Q-XHZPxMFG6zRGzpi2yOBGfcz6yXPkTC59_T5ieRpSBfKrbq2Lix9MaSVEGXY0f52QS11tVNAkVjVmubjo42SJBsJv5X9UykFHMLrvuVI_mD_MKsFd9MwNub_e_41ebraZhiRvvBwgJH-GWAkJG552uh3XPHrYqrquEAb7N9MYyZTKKCoDp5TB7u2Tl-hMi-AuL_rtmxCZ3LU_e6Hv2Txa113Kdu6YEfBdRFDQz34oyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند با واکنش خوب مانع گلزنی بلژیک شد
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/443842" target="_blank">📅 22:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443841">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d7d87aee.mp4?token=egbxZ_ebx-fJVxqY2ZLFwJWVCdnOFOELa6zX4gRFh41XC-qwc0achyMs_D3LIHoCOz1rMgKSTUENFG6eJUUZ-R_nraQghQQLoJ9Rzx7Pr-DwFuBVjjHHC4Qz-X5BTWJD7Gcq1iRPcqudeSpEbIBIV06xBr9mqUj_qknA0EJhUIIWZMc7wz1hiYNrWluhtkculSqWpXfdsxqWN47hacRisqRKaprPnVpbXmO7xy2vPLnJAGAag3Lwe4jZmc6eHQZQqLw0Q0oVecqpe-_hSMKDJ9MI7cAA-oktCHsC3vkQKEUAJX_AS8tgxn6S5q1qQ_FKpPMjjHP9Lia7ZrJ0bESEiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d7d87aee.mp4?token=egbxZ_ebx-fJVxqY2ZLFwJWVCdnOFOELa6zX4gRFh41XC-qwc0achyMs_D3LIHoCOz1rMgKSTUENFG6eJUUZ-R_nraQghQQLoJ9Rzx7Pr-DwFuBVjjHHC4Qz-X5BTWJD7Gcq1iRPcqudeSpEbIBIV06xBr9mqUj_qknA0EJhUIIWZMc7wz1hiYNrWluhtkculSqWpXfdsxqWN47hacRisqRKaprPnVpbXmO7xy2vPLnJAGAag3Lwe4jZmc6eHQZQqLw0Q0oVecqpe-_hSMKDJ9MI7cAA-oktCHsC3vkQKEUAJX_AS8tgxn6S5q1qQ_FKpPMjjHP9Lia7ZrJ0bESEiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لوکاکو به‌خاطر خطا روی بیرانوند کارت زرد گرفت
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/443841" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443840">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afb774a2cb.mp4?token=ddvf2DCtDidg1IYREkATLs7AieNJKyS0Z7uZKUsImzUxgl5QOOrmYF206jdTAO7r_Xv_g1ii8hkd0MPhg66BbbYCQvgDoUifeS83I7JyEdJWR09qQkdZyTnwmpxbKEE0nJQdQvm_gjfsCt9PpPichh9CWIxy9u2oIEbAipv-eyOzu5YAi7Cn0rVZ8slE1ElLWMCT6IjOE9LZw4CgS9sDII_hIOpk-gaF9D9TtQzwVfcWJyB62F640F_qXCwFIukCp3H2naUtH4HDmEc_h-ioYvdzLWalXx1nrh7UC4j3QIDLvLRsPZtHjCZz5_KrqpM8HVp2UDtxfQDgQyL7Xdm1fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afb774a2cb.mp4?token=ddvf2DCtDidg1IYREkATLs7AieNJKyS0Z7uZKUsImzUxgl5QOOrmYF206jdTAO7r_Xv_g1ii8hkd0MPhg66BbbYCQvgDoUifeS83I7JyEdJWR09qQkdZyTnwmpxbKEE0nJQdQvm_gjfsCt9PpPichh9CWIxy9u2oIEbAipv-eyOzu5YAi7Cn0rVZ8slE1ElLWMCT6IjOE9LZw4CgS9sDII_hIOpk-gaF9D9TtQzwVfcWJyB62F640F_qXCwFIukCp3H2naUtH4HDmEc_h-ioYvdzLWalXx1nrh7UC4j3QIDLvLRsPZtHjCZz5_KrqpM8HVp2UDtxfQDgQyL7Xdm1fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرود ملی ایران در لس‌آنجلس طنین‌انداز شد
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/443840" target="_blank">📅 22:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443839">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/611365639a.mp4?token=iCY8uA2A8hGonXTBMnEq6gfqk-DY2mFIYHHTjmhRAx5V__tFMrNE_ym8hdagOkh5WN4I4AeCOLGKmNgKhEj7kmjh1FkHWa4IZo6Os60njpyQNyxMBDWBau2i1_D06ry1tyVY6jNGnyV9PTuKjwsCFZ80pRaXS8UjqnqV1tOOyv5-rIz7JbQgBlORTMX7-Utn0qVLe4jwitBJiq2EdkhmeYcO6Fnf679DOTTHsOtVQZbo8-3ex4U9lROGfUp5Sf2_qp8R1Rc5WxC8bJ483cfGwhZVvv6YDFgIHqQBZstEByl_j7o7DDFs4G2N_wFUSKcLdwria5JZnKwVh7uO7SOHJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/611365639a.mp4?token=iCY8uA2A8hGonXTBMnEq6gfqk-DY2mFIYHHTjmhRAx5V__tFMrNE_ym8hdagOkh5WN4I4AeCOLGKmNgKhEj7kmjh1FkHWa4IZo6Os60njpyQNyxMBDWBau2i1_D06ry1tyVY6jNGnyV9PTuKjwsCFZ80pRaXS8UjqnqV1tOOyv5-rIz7JbQgBlORTMX7-Utn0qVLe4jwitBJiq2EdkhmeYcO6Fnf679DOTTHsOtVQZbo8-3ex4U9lROGfUp5Sf2_qp8R1Rc5WxC8bJ483cfGwhZVvv6YDFgIHqQBZstEByl_j7o7DDFs4G2N_wFUSKcLdwria5JZnKwVh7uO7SOHJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پرچم غول‌پیکر ایران در سوفای لس‌آنجلس دوباره باز شد
@Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/443839" target="_blank">📅 22:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443838">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7387e000.mp4?token=OukTopefiWupfaRlLw5o9EUauPCs9g3Zynowjq9t5K_EzIqvWedfwV0RD4tgmh0v3SYRtKrsYdZeTzjg0mfe7PfkBh7MUYcUBJDCvlebYsWW9n8V6BDpNCzJjmLPQq2BAJMqBBxMOUGJSFBbslnE6AN_mF-_KG11ldTLDhWSi38vZLiCPJcV0jjCbqhZG6dD310JJAC64slZNljYltfKIOihaGyIbhlaOAazXiM6NgzC5AV4lAuYXb76t33LKMzh5DIFA1PGpmuLoAdqTaT7Fsv166Kh3RapJAFH3dB0smjVN2E7A9POZecPQMPhu_tY8USgJC_BAwErIax2ouLIOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7387e000.mp4?token=OukTopefiWupfaRlLw5o9EUauPCs9g3Zynowjq9t5K_EzIqvWedfwV0RD4tgmh0v3SYRtKrsYdZeTzjg0mfe7PfkBh7MUYcUBJDCvlebYsWW9n8V6BDpNCzJjmLPQq2BAJMqBBxMOUGJSFBbslnE6AN_mF-_KG11ldTLDhWSi38vZLiCPJcV0jjCbqhZG6dD310JJAC64slZNljYltfKIOihaGyIbhlaOAazXiM6NgzC5AV4lAuYXb76t33LKMzh5DIFA1PGpmuLoAdqTaT7Fsv166Kh3RapJAFH3dB0smjVN2E7A9POZecPQMPhu_tY8USgJC_BAwErIax2ouLIOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش شعار فیفا به زبان فارسی در استادیوم سوفای لس‌آنجلس
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/443838" target="_blank">📅 22:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443828">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvJNUB3_qXP8WzTv-T9jugZ3YZ2Cr4xwYKGturbl0dqMAne4GMJ650qlKdw0cwv6kAd0bgdm3kHmg7lJcQ84q0AMIgcg1oYI5tPAILD0wHN3egz6_AkzjUUjjNaZa0ypg4U2rkL_TrFiVJcoLISCnUr67yLqwdJvQ8FRGBbhQ2WJYEJrNSZXx-KSDh7WmQFQ_crZL43JJvDHVuosHdV5dSeRZf90UIjlezRz_6tEPbpzUgRrQtJ5tAuZ2B9U6-EkYx9Dpy2P9KA_JxDfq_uXtK8UWcSVUPzwrR0VIBqtJSZjK7V95aTH5biy8MnG4zam8TpjnLwJNrhfneLasQ_oAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NzQh1lAR8M9sFKRZFSxoNDqbKKLQnqXqk6rKdc0xT0RB9x5Qh2INsCzIMLDNSKupXvkptwzAxAS6Xfx-cBmpiUBKiGKfbkTLrUyFGIgo-9njGiRs6RFgxZnlwul4ijXcxHH9eT-BPyjuvW3dD4aITPPzO13qJNjduwvv_pQoHoyVuzl1c9r5U2EmzeodvSaMEayJ3G2hkjjVivTdu0zGJVsj-eF1DamqTmuyxFz5FJt9Frn18mwNaXE5AFrUY0s2ICERczrppiZtkxj8oWhwjWjjD_om9QUtSTWTQ1sL5jFQT0bggXNCzuW3djpQTKQs02lybb6QK560uhwOiLFZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHj6pJAoI_q6do7YxOlyx7KdiX-3ZAwW75GOhLLU_0MGvyNsLEkaf9RUvgZKYO2rT8GjAOdxQeQXeRXG4wN8Tn7hS9UgQ5j254sdOVzx6d5PQ__HvHa8Yf5oqws87TiyVdV-U3zSRJT8TdqpYNkrgt-ZScWbKIbXdrzvpCTHK1dbqLG5bPEjAdB15Rkm7O2LL-3ZGiGUs7BxgIxF8RHDCMOj9KUaPKoeHj9Gdavkc4sW-R4TPCJAcyBJBuiZHF4L6yCmjx0io0EdaYhXtCPu_1NE6YcLVwUlPas3OHBvc037tZHWqix8bFbOCq82VkCvdix0RPhb1KoOzXwHfM3uVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXKpL1FxL5XRBp0KkV7RVSmuDEjZXipPKrXgF_T81IHOT2UatTaVsPvk2kPS6OkU9JI-dZNm1ICDY5kHwYXY7SVv-1tbpbbAuR9LunUlxfiV9iFP5oWrE78S9i0rktq2QRAbwZFILblRU3uPAWyEWeQDHM5R8lqtKLohMmESqli-fMRmUqjes9aRn4ySvcoDnDHqM11XVqhO7V5TgLjWZPval8yDz-3BC1kQPPuI77nEXwA3X9EjYmkWP6qrosTjVVsO3EeO7pKM_YuQ-wiCpPFbXO-8lVpISw57c1Yv9e4XwUQ2HPH_EOFFtKcDKj25gVKt6kF77Rq_UPhjeuFmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXeRqsjf_cAA0QWCDzKt9TKWlFE2WKCbC1srPsZgaQCNsZI4lSETq0h1hx708JogBQ49DvqnVeDXCwnPgvf4a1QnvmivcQ6M7VkVQI1Wz0cYcabzaah7hrkFXo2skKi0cVUMxxqSYEx5SgzS84n_VxoUEmGCnNAT7zxLg0vXTHenvjaKhITOqqp-TlcpgF0BleZmqikE4zIthTHu_J65C0dOu1pDx4brkA8eI9XxhvjBxHNbj4rqgNgusEQbg33kk53UmofCJTHJMf6iqgjbHCkFGhuy6j5y8zoMdufYNRBw_hzsm-yN04cHjamcO7UcIgCCxv7ienQT9mkACUu1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fc7QxYS3k464Q3ZqpVCJONZUxQBK758jCDtyyAQ_kvKS8joEe36hhGO5PbC828XTb4t_mwFAD_NmW0ih1NLWE4XP2FPEVdroQZ-Ks3Y02GdYmiw7f_kr7CypSu51tDRPAaRIrdK8y9NxNONaT1MA_vh-HAl3ZcVivTTOaB-VhD9nEp2suLTHKUI-jGEbkM8JWAPSB5aXsmCQYvz_Q1r_3iNIBynJMt_yzADOY6m5RzMZAI8FOFRN5GzbOzDH8hDBxyr4aX2OI47dvuecDePRgK2r7y92tnKpavjQn6pg83rTcY7FPZNZWqajiUlfIQ9hcMnajJdokbnmKktWozWgdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQQYVkz00qkt9k01wuubUXghm9KASgJ-32P2re4Gbz2s3d0krzTt6DGgHAofw0SKRcheLGHuARFtVql2j9LCaxeMZFtuOk-OBuj0Q72kQ6Y2eNkplDdb-Gm1LYrDuXoa54Wa3KIDNa9ohl1wjslPN3pdA8HcJ8f0i2QrVKpEaO9HSlTOO0VBi76wmWAkW9eOpQlYNITJcniBbVr8CSGaDUaPUiETIHBniqdipCKAidnsBof-UU0-wFHbI0aP37GycvhDrC3C2no3GokXv1uZC13ApKZczoHD1KER8LHY8-oyLgCcikVPKb0jSY1-TrmlB9rISE_EW1tcyDaaayUthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLlmecSXXhXahNparNJpQS_CmMcNV9-v-WQl38pSJFifTTGrA0vkTs0Si6ZPynm3HgiyDkxsKmbdzJvBjq_wQO_0P59vVFY0bse-HmZjEl0xbiRcgVcxaG5CPSDz2ZDeudqDFt8ggvC1eid_6B_S9NdAfA8FYL_a2O65l8ma3XKct6XnVuDTrhxyQ9us0LJX5jyL_7NukHlEFo15E4TQ0YdhTTumchA3paRBXqrG_2Vr5PA8xbHCHtWWKfHlEj_B4sgCISK9o56BY_B-aeKQv6emDaqlJE2MfZnBf73eb6UAWVEIjuS0pUgaA3UVPSmHQzKAcQGkDcEU1HIYZNy09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/syTOmOZFVifyZzXuVChVxyWUUmMh3W2pOY9n3Tc9JumlhK_EnUGjDAPjLxpx439z_8IxBpg0_4AJFEy5urlwJvJ4V9yFlEwoiUx4JKfuYQa4mY8SMkr_Hryh5Hu3iUfz_8R9xOBYYv0sjsQWPmwOBYsUCVhj5hEoEgy5bGfJR8OOOV3tzoH4Byu-jAlKqsfN-yDr4xQHGZeyLZ-Q64L2jjXVccS1VnQztuyrdhuG0e3wEYWZm4nBMNn6utu9rXCTl40XJMVy-hzL5XilSPOcwgFH4ULXpITGKvCvTnXKAKL2iYLWbXqyyIH6EZX1cB7EmLhb7nrU8QlZHc7nDZLgnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuSvAcigIWtoJZzQhJP_PXwFdRl87yVXL4YQfSyKP68HtefZqjCuZxNCzjIokd5gAf3vekgOXloxiJD6lHQ5hcFfKr09-3Fbhg1d4Ies1HtraTsiNWLpEJh2GPU_8SMADpkYQK7GSi8i9CBseP-0sCCF1yikwyY6J9BEyf2bM3TR_jCWtAopI8R5mbS5f7bH1OBd7ZMThdi1DNTX6NoWSBy3lCXWDclEyJSmn8dBV0bpQvxpht1WLOjLZ6J8fxLejQHeM1P6VF8gMP2KCLGadn7xqI1qtOk3sNkdGs2mGeHwV0CqrfIJE9zHtm1Hj5lM4ss8kPMo_Z1mVkvHbU39uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اولین شب مراسم عزاداری ماه محرم در جوار محل عروج ملکوتی قائد شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/443828" target="_blank">📅 22:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443827">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3f0c88a9.mov?token=f4CH58oJyWCakmb8rRIFZkmP-Vc_3v-F_OF930hOrF33EpLNTeVr7K33YNTB2u3O-Cf7hh3DspahhPfwvEZmVIw0hLvqd1MlHendy885KAhGs0V2koNf_y6X6kGqwns6rJ52JUtm1plZoVGB4T0fya7p-I2M0h5rOdg541JEMvPA7zjYM2A_IFPJmRgzZQrxH2Oe3_NXlr6Px8R4-v-3pvMvk5XKvjlOgXUlyAymv82heNlfJ6yYsVeByTQvOMtGWKfP-XCb3GAJjECP63jsyfK1aSxjD2KU0dTf9M78AYo0oGPa4jfVorL6lgw0C5Prs5Cvr4691lRlFNVMi8jZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3f0c88a9.mov?token=f4CH58oJyWCakmb8rRIFZkmP-Vc_3v-F_OF930hOrF33EpLNTeVr7K33YNTB2u3O-Cf7hh3DspahhPfwvEZmVIw0hLvqd1MlHendy885KAhGs0V2koNf_y6X6kGqwns6rJ52JUtm1plZoVGB4T0fya7p-I2M0h5rOdg541JEMvPA7zjYM2A_IFPJmRgzZQrxH2Oe3_NXlr6Px8R4-v-3pvMvk5XKvjlOgXUlyAymv82heNlfJ6yYsVeByTQvOMtGWKfP-XCb3GAJjECP63jsyfK1aSxjD2KU0dTf9M78AYo0oGPa4jfVorL6lgw0C5Prs5Cvr4691lRlFNVMi8jZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرم‌کردن بازیکنان تیم ملی از زاویه دید هواداران
@Sportfars</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/443827" target="_blank">📅 22:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443822">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNxlLpmk8yHhhMwcOem93wpfSWlv7yFxIQdRgxTAPWtCXWzfqnNISK64YTC6waaU0mbpM3uelN_LIjuASLrAYnNQnipilmx35JppWacpq04i9ue5-dRgWtBSpy2CnA-4u7PfWT25zZd3MJtMR-PC41sqDjnDsCj4T6YmKek_MxDpzAXBqoMA6EqZjFAC2NlQTT0XOVuxZkO69nVR0JkJLHkNWiJ1AOlOiiYy9_FpcYVKCUhhIlOQkGO5dh628r-UHcY3b_-MbwrsN8GAc4c877FMy3OBKe0Vn1NwxYiXeyn19Vn4Uy4FlGHOJ0XYgR5HbBbde0GlZbs7ZxBrmnSgwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4Yq9RpY_K2PNz0ZiaC_67gteObraGbjRPslTiJbZY_SF1dVW05ihFO6r3tRvSIBkB-6vEgkPj7EBeYyVo0vd3SIPfOAwOPbGVb3HaqmS2TkPqfaGy-hXtKaDJIfo3SYYJp9kQewZmXBae_ZvXt-9qjj0Cc4423IECxrS4Q83yzP0hwhAdfq8GCIu_hYYfV_stw7oa13VfazsaChI0XPvBboEPeNiRCYY3X55lTBrFvDNCTK-q3EJ_PW3EbxnxSlbqA5dJr1f5kJQiMc5XLRMGITGHegekCfrCxA46KJ0kA0zEvSoD-mfENiLz729Blvg-MV0ShkvGaWuCb32p41hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDQLwnBkjFwZdHLFa0irikxyr3Jo6-_npe_XU94x_L5mFbpyFldlrvnVDNsO98vRixFWvQc1RFfNfJv-uSQ4MH89pmd_YV_j2CTC-7spei8LLpm-r8zsB-bEmxA_USLdCVd0twbUAP_EvrXJpgjFFkl-mZJTvi3wZoGlTUcCBlAJSZY73U0DOK6Ohmy69SkyxwmStLo1uXBPyHNHqRFJ9Mzr5qh9v6o8F2LYBYc-EJn5Hs68NMEJtnny-K65tXMMw2RHQoCKKJdvOrOp35najdC8GWPjCUHUnsQAAQjDTjjnnhR8ZVKqGX-Dj15PTMmZX25p9skjVpbI6Mospr6nMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWuHbQcF0dfRsLzSASh9CW1Z5FxPJhzAl3YtvMMvJz8wmIVRVe_STPsDzXfXlIizJLt5r2xrgqRTYsR2bhV7PTvIHL1RLLL4cOKrIeklzYCo3qIrjpeGOyhWqxweHVRyY9tO06u99AUvNmDJsenCU_46Vm8KPRokpSbEvzx83MFYaKBUrPkL966FDVvgRUUZJGgCgb4Y86JleOBKYc7Dxw_8thQKkToUnhFPqbt3TG47ZFmM6zsHs6b1kqImRTE5tKvQVOHgTeKZkHmGpK5p7AyZT_vZhCUvmDyYqSBEXUPNNom-uLg3Rxp6dzega9JAaCqsp58fKNWx3WfQ9nOU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IIuCtHd6kZ1IgGN-HBaFJPtaGTUPwrPNtqI0x_FfWFW2Arg0oukihhsEzlh5C5oz4VwV32OAGUkiFbC7BS6-1IItakzPa7K6lFs7ckXGMP_5HHd6FM8uB9seLUock2Th6KnNoty9uj6XPZ_sLZso7v6esneMWbDPq3epqVt-RD6c6KpTXzXOXEQvruPPHVELY9h-6BZ0jWqkTrWQKu1uH42fFeSUvq9TI_pe5LU1fFe00OwM10rL1hEocY1Ek4ectu1dvFG2mdz0m1-Jzje0IgQFtpYoQEHf36k0gE6pNos7IuDwZVoh-T7sAgl7LOr5zIij7tQ4hFZOinkis4nq9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از بازیکنان ایران و بلژیک در ورزشگاه سوفای
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/443822" target="_blank">📅 22:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443815">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bK7xW5mE39sujuQuJAGSTjdkzwmTO-REt7FtkP7Wvt0lbtgolN7O3VEMw_nRuxWdWjxZMiFQAniEkhsqkmy_p_18FhrRKFeyDRAAS21up52o3FNu-Ojqxy11mMI7Tg4UrUZWn4xRMyO36vmq0tU0WTymNXt8RH7TVbfNkv5CytavJAMCpgRj_x58XF96rZ1LKG-BHnErgzHIlaADk797cmwlad2dQnK1Op_8ErzaBswGNaj9g1TOHQU2PDQl73UqSolhzcAb2GRYCpjMWyoNZJhJnVCC79u_KFYCoJeDmwx-2r7Wq48poDlIHYfHibDASJmbBP5FD4ZSOm7R4pdzfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OnNJMg0jR7MLY72xCYLP-5HKFjPhoxJfSEkGAgsTAuJ-in9e2IWJINbIk4UTffQl97kLlPFMM5IkwCxiMBRU7GSrU4iNCrCmWa9fcRsS85r5LafZM6a-douENHU0RaeWxh0U8-RrZtNDTa9OaymVEnMMb_lZ7OJFI1E6WV05wUjyvy6DbaMmgr16V9BZAFmjPNcSr7ruSJYAkZhABItXwPEto1-UXl2ao3xe_0Bnqb13JP2uCRFXvHF7HsXf49nf-3CrnrLuYEU5ADHddx6sQUpXRs4_gPao3eEB3hsUagTawb9nW86-yfoW2XkmRlfbWik0___ARj8UrSAn1Cguvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAZ6nFsYF5wzF4zDR51o71X0vt1j1W1PtIU8YCItcx3e3MiinT0ZB8fNrmf1JG-emzpdgPCg38Cc1OthVddipTv26iTeWy-kqGan2yHQUfETV1nv7QvaC6QgSMcdZ43vQzB1gDb_dmNufbMbPgNup4HTqbDpOGXXKr8Xi0H-NhBR3aAMMAnryD8nKgTsTrEOYhnKQBFMmAjybZ9CCk4x3VcqdRgzOKi2FUwDdC8cYqhJskffDx4TQQLpH71umf8Q2vSItC4vKs60d21Nhfqoo2UTtauvraEjzqIeymzivTs5MQeaTI5E4lPVmeIkLcoLiy1eFzASbqEYWDc-0rds4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQ25TNnV3qVFRHMS7jKARBNNhGYsQJw15Ic2nRFcxDBl5RohrzTUzIv0fpVER9hLJxK_i3VOqikXgZDz1g0SQeSfIcfEFhMY8ooKx-f1TviAsjCckQCEqfQyqb1Rr2gUsm7fQ4ZXu-CO2vGbcVsT3bW4LLQKtBjJRYACvPr0BaeCVxSSQPJdO4TjqZRRHTI5_1H00gGxoD3N5cLbWtRqZGLbbbgN1FeAZIL4QH2oW8JYXPbT3uwomYAL0VTgV_1wzw9vvbCt5bAy6ffPJn8hQfsZoysTyckdoJIidr_iiHBQQuq8l3m2VyCntwRe42UincaE8WSlfj-8oEtVNVb0bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dOvB3in2tmd5vYpnndj8PPyilywrtmNPsseVr6l7LOIJi00w-sDXfTGrMrf1B7wxw5FOrdKc-mVk29xPBhHzmHdz8KuuSUqjwJULCkFHhgCRR1Sel134cuO4dP3ppyfNswhaJuCpe-GQsj01w0wkJ2bNX7au6eWY1ulDY_5n771DWXHqkvpMkR8U9j6loLVcnvBKibdaHIflOHorkYZ3WdeJv-jeHxodOaISPKp7UJer06-Ek2cHP8nkccsTQED8N42jb3ni9oPp0SjD6ewY7NccWaKrbDJEWAx0q7NcRW49lhf3epObRqETTGi_ADKEr0fd-dvi0TEHbnlhfnS3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-PqWH9xGO75l-FBPbPfju1LelCapodh4rDaEn6H5zKHUf4tvAjYNayS9OzOqZwWD58p2CaMwA42QcLZgqewUa-Yg_u5UynkMZd7twHVO34AtyrJas2KcZUt3zAOnFbjgzInisQs_0Dc6W9D1FVAK0P-0CXb_Np-RSfLcXi9RDXLBAQb1qVS3dNhiv595FdDkoPPLZwnGyjyVRthY8ZuzB8Xq-_A93ileopMNDYZ4JVLBS1UL9OWZlSgtRZM8UvvTufikQhYf-Jojbp2N0TVQxiTQvKPwuJinKOcyHZtfPs-uFxSQvuIKRzpSuykWE650sP5ZlF_dfM5pbtyjP2nJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nf1K40KvZug8sj-4bs3oAb9xNGSrGrWD1QpdwVCPH6YZdFS7xrA44rYjWs3rC56WVSIETH33ch-H8M0QZ-w78sxVePXOzKA-CizF0XLRMGwkhvATgX_zUVhRRtGsa7dZpsG_c22hqVgzq1A92AkP37K6JX6UcneukC5EiFU0zGrkv9oXn1O8hT5MKGJyuHkgPN8QwaPs3ntXpoqXCcu7CgkBF3mGEeuXpP0U8xuA5SwSq3iTt70lx0yaYrUxW6iL6Ct1V9LL3jt0XIVXngNYGoMsAjE3RK-aT3VfAHOGVaHkZznkezELE6Z4LjQq65d63WUjqOQN5Do0h16n1YJGtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هیأت بهشت، محفل تخصصی کودک و نوجوان در تهران
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/443815" target="_blank">📅 22:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443814">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2ddf754c.mp4?token=UGJr7iirctM4t4JrWydIhM9lm22dl72CYf2Umh42YbfeXXMF_v1nVO9HF1pUjw2blT9JW7s1T8hE0lfcawh2Rvcx96qKSMhau_280FnBmMTx78MMNK7MVKuZIuGucWXMUUTKi6Ade5fsr8zHgvYODkv9_Swwv2qf2j4igNUgK6logIm4cn0WKhzgkYagosk4F-Yyy7_BKcWOUBmvJk-QzunuRHV8ko5dSWj9lL0BMWHToMP6KY4w-GzkyajJDSpap3cO7Mwbcjlc_5E8vcHtCR4Wl2vlbjL1bhJMhIsblcZyG2XBpbivUpbRU05OXvLR6OQjusnTcnvGz7e00VpZbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2ddf754c.mp4?token=UGJr7iirctM4t4JrWydIhM9lm22dl72CYf2Umh42YbfeXXMF_v1nVO9HF1pUjw2blT9JW7s1T8hE0lfcawh2Rvcx96qKSMhau_280FnBmMTx78MMNK7MVKuZIuGucWXMUUTKi6Ade5fsr8zHgvYODkv9_Swwv2qf2j4igNUgK6logIm4cn0WKhzgkYagosk4F-Yyy7_BKcWOUBmvJk-QzunuRHV8ko5dSWj9lL0BMWHToMP6KY4w-GzkyajJDSpap3cO7Mwbcjlc_5E8vcHtCR4Wl2vlbjL1bhJMhIsblcZyG2XBpbivUpbRU05OXvLR6OQjusnTcnvGz7e00VpZbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرم‌کردن بازیکنان ایران و بلژیک پیش از شروع بازی
@Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/443814" target="_blank">📅 22:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443813">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff90ff1350.mp4?token=vkER2LTi1TzUE3WREttf7Wd20FaNHmtYo8bsCBTuFqcmDb2EgrwrPGVMvkvJreu18EK-SKTc9zRuOrmxzHrZSpZxewPHI4UPNGzQIc3iZGPUj_VuxfpFFedSThhGGuehS-yE0BYhpcVn4G3PB-tAK9i7nvqVoD9xBhLpJywHA9Mjwesxj1xEanr0Av6M_O1XNkqlN-x4CAKa0P7AF4-pA8ni6-i1F7Bu5OSNyrsm93xk5ks1gNT9VG_6ZPZulWw7hDIOs1qnhUL9CaOBL1DSkVhUrBAWKSm9I6C4_KxVN7PBiiNv-S5qJN2n1itEyep_KdraTBqjEl-dWrS_MV0e7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff90ff1350.mp4?token=vkER2LTi1TzUE3WREttf7Wd20FaNHmtYo8bsCBTuFqcmDb2EgrwrPGVMvkvJreu18EK-SKTc9zRuOrmxzHrZSpZxewPHI4UPNGzQIc3iZGPUj_VuxfpFFedSThhGGuehS-yE0BYhpcVn4G3PB-tAK9i7nvqVoD9xBhLpJywHA9Mjwesxj1xEanr0Av6M_O1XNkqlN-x4CAKa0P7AF4-pA8ni6-i1F7Bu5OSNyrsm93xk5ks1gNT9VG_6ZPZulWw7hDIOs1qnhUL9CaOBL1DSkVhUrBAWKSm9I6C4_KxVN7PBiiNv-S5qJN2n1itEyep_KdraTBqjEl-dWrS_MV0e7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر اقتصاد: قرار است رقم کالابرگ افزایش پیدا کند اما فقط برای ۶ دهک پایین جامعه.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/443813" target="_blank">📅 22:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443812">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzytNNOetGeBrXP7WzeU91dQpQmOT6BdFUQOs-Rp603Deciqc3HStJi97mcWwTqB7J6CcLHYlPVJHEm3FYtCnue6-MYa7kgTQZS8tiyKWad6XoLYZvvN1O_s4dh9X_pPrBOQ1ZMM_Km_qsFyasM8vO8xfOAaTiAgC_Xp0m0q7XQ7m5wNXeEcqPBGBpZVWKICjNWlEeCV00A_k7RQXa6JsGs4hOeYA629H1LLB_XvswmmF2Q-5UWjrjr9nNgQxfVNB3AOkz-obTJ0H5D7Xp8wNMnubx11BrIMWhPt5dMlOqRLQiMob99Yx4TnQy9QPEOwoJHGOGmMO0poTtcb7mVz2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام آمادگی ارتش اسرائیل برای «عقب‌نشینی جزئی» از جنوب لبنان
🔹
شبکه ۱۲ اسرائیل شامگاه امروز یکشنبه مدعی شد رژیم صهیونیستی به آمریکا اطلاع داده که امکان عقب‌نشینی‌های محدود از لبنان به عنوان «نشانه‌ای از حسن نیت» وجود دارد.
🔹
به گفته این شبکه، اسرائیل به آمریکا گفته که بر حفظ «خط زرد» در جنوب لبنان تأکید دارد؛ این خط، مناطقی است که صهیونیست‌ها در جنگ اخیر اشغال کرده‌اند.
🔹
این شبکه در عین حال گفته آمریکا تا کنون از اسرائیل نخواسته از جنوب لبنان عقب‌نشینی کند.
🔹
به گفته این شبکه، اسرائیل در حال بررسی امکان عقب‌نشینی از «قلعه الشقیف» در جنوب لبنان است.
🔹
خلیل نصرالله، تحلیلگر لبنانی در واکنش به این ادعا گفت که عقب‌نشینی از ارتفاعات الشقیف، در اصرار ایران بر پایان دادن به جنگ و زمان‌بندی خروج کامل ارتش اسرائیل تغییر ایجاد نخواهد کرد.
🔹
به گفته نصرالله، مسئله مهمی وجود دارد؛ ارتش اسرائیل در آنجا مستقر نیست و ماندن آن به معنای خسارات بیشتر برای صهیونیست‌هاست.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/443812" target="_blank">📅 22:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443811">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mimmy1qsxtziQsmXSSFpTuMm0B46iIYBywiOAXZS3jVknqtEl149EchrWkJlFzLqiZTgvdtLgWEoEVX2u7FoTy_okd-VMt3bxLKbSs0mqP_9ch0gw14My8DumBrjPiLyqPvqC5QTSDSpZPELhWwEh_7x-P_h3EI66WNtwQ3KMDsKXjE8tyH3_OVWyh_UJuKrOeIxY3R9bBN4wsDudF_fA5HF2Zts08O5h8PH3KLQEn8UCJ_RoeiZJGWFJN_8j7jRTHiQ6OhqpKMJGwBnKILl5lRdpo-lvGSNSVad5uYumjNRyNeaMumL3UApHoMWmAXELIF_oW_hD9IWqaZIjI8tvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تختهٔ فنی جلسه تیم ملی ساعتی پیش از آغاز دیدار ایران برابر بلژیک  از توسل به حضرت علی‌اصغر(ع) تا یاد ایران و شهدای مظلومش در میناب @Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/443811" target="_blank">📅 21:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443810">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb634b19f0.mp4?token=eXQh_1u5EwWCL_kJDgqfuZ7BdqFpUvp6Gb75BNyrTukmsDOIKA8Mgp5JLBgMSbJgd1Agf_oqwKOOSX1Ot3X6Zxhdh0axjiCtpFhzkDPhSBiEIECaiduE3vEmlgjx0Rg7du8Oc0ZVG2p0lY-_bLvSBi80yVbREAtSthJ0CZquM4SfGykUy80Pci3GBvB_xaC8596s-QofMffXbbVGX32bZRRphQ1IwSyILE0p88_67O1MLnb7JJa4iNsk3EXZBpxibnpALxXdZVU7oScCXMfNb_Ilu7PFXEqDAest93vHsoju4MLDacY5jECBjr6aFklHflPRumfkxlkyjdYaClOygA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb634b19f0.mp4?token=eXQh_1u5EwWCL_kJDgqfuZ7BdqFpUvp6Gb75BNyrTukmsDOIKA8Mgp5JLBgMSbJgd1Agf_oqwKOOSX1Ot3X6Zxhdh0axjiCtpFhzkDPhSBiEIECaiduE3vEmlgjx0Rg7du8Oc0ZVG2p0lY-_bLvSBi80yVbREAtSthJ0CZquM4SfGykUy80Pci3GBvB_xaC8596s-QofMffXbbVGX32bZRRphQ1IwSyILE0p88_67O1MLnb7JJa4iNsk3EXZBpxibnpALxXdZVU7oScCXMfNb_Ilu7PFXEqDAest93vHsoju4MLDacY5jECBjr6aFklHflPRumfkxlkyjdYaClOygA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی دانش‌آموزان شهید مینابی را با بازیکنان تیم ملی همراه کرد
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/443810" target="_blank">📅 21:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443809">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران روشن</strong></div>
<div class="tg-text">🔴
امشب یه اتفاق عجیب توی بازی ایران و بلژیک قراره رخ بده!
این کلیپ رو جدی بگیرید و مراقب قفلی زدن روش باشید
😁
#ایران_روشن
💡</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/443809" target="_blank">📅 21:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443808">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/443808" target="_blank">📅 21:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443799">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ImrQU0Z5lAcuZQ-5MOBkNoqHZkuwt_fTp2QuYGGIaL0JCfj6QYCU8-oM9aiVROYZ1x4E1bkix7r15ayeL6hI_v6mo51Len3yY9cEaqt_a2FWRZIEoI8NXy4UKr5ASXq1dJmjZl_ATkntZ24YbVUyA6vXWq90Iib-SFf0bP5K41iKKn9uXbTrU8cNgAE6hhsOGHRTJ9H9hQZf6phrrLNh9t9J2K_iNxucoRNZ0FRyWXa9B6CQ2OwWfppKVGzGJvAIg5dU6Krdg612DvcqyTjUmvY6kGWxW0wmfyzo_0h8wWr81sx-QaGObbCQvXEpj-EbOi3VKIw1SW75fkS9WSv65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCEBrJqCkP_9cZQ_KB-82f_ON9j9tPdr5TCrBFhwUyUnf8rKtPxm_1rNhE1KFJhSDpyVGBozLsAz8hVx00P94fSIwUjYAaVO-DNCnMk9Uz-SpHR4LLlC6L8L1vhBMSJ46PJEA5-4MxhcMoKwQ0jfdz4a3mkIkaS52jrCVeLthoz_Jtd-liZH4XU0KIglMp-dljKzSBZDEG_tKr-LoZ6ExY6YZEt2chZzOyQ0ckw8W0w9zBx0W71OYTAcuzhjkwmd4BGj6HdHzKgcHb3BF3SwY6iTqW5rPk5WeUoMmcZ7cl8sQH4KyZu-fYICCJXRdLETz3kU1bSIK2KR9T4jEzVk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBZRqg_0-vKkEvL0ae3QYEnWw1QPpMuT-a1lQpw9v9FNG_pBq6gwlWwXh6Yq28eG-gN3OO29Z-DK8pL15lM6hh0mUk3xICwLofhQbjpgeHqlaUCJ0Gc9bBVxycz3H8JAjTwjb7OiPrIuGkV4dWHsWQpKJsPF-jMm1Gst2LgzHvAZHt2z9_TC8D72VfovhIfHmzEcWL0SUvISJb5waEuA2c4EEbnQDvseeMERXZviPJjsOKPBR0qOjW8_2_D3kWCDDJ2Yw5fZZujQAdtpOAWXwDkzrPqoT6Sym65wirRjHIUYs8ZWiO1JFjJd5A29tUR4c5yfaF4qz_Sq9YcULyro6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCWOjbv6US7tb46IOwMYbgLIYDP7Ykqd-eTXoyi7wybxYgF9ZigS1Yb-BCAJ6lTTM1fKG3jjpUaJKVLjmuOlvnRRFthnKmsYZA6Kh_DzLHaHjYAGNOl0Y0l9yw9NcELehUzswcUow-eSLpktTqG0BF5jJ0nrUBqjnnT0cMc_VAf_4XpNggKV65iiTIUkSB3BjTeTXTV2Lf6UHp865eGOGVpaCMopu7ansWQgQRcxN9DvUmrWdBgZSNrQYba7CkxMnbxnUj9k5N1q8-1KRH15tP4Zml2ASLJO_0BA8GRC6SEDAwbQS2fogJl5tPLytN6tXUIIIK3waAvNRTYclQQyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDaGgYDvhiDtx-bnAlyz513rPSIBoEodE-YVI8U3nPR5NuQac-yNqbz1oFvD6r1BxI6umv9EjSP03LCJR6MOqmNItms_1vMNSl28BEvBqMxNBZAsQVBUBm02DvlxY29q11foQYiXfJu_cmXUXnbnXuynvTJAG52kAcBxqJtypCh1vNywiFGpA_r7222p-B69DUc2N-rSTBxDXfBpXVoL235fCzdfOIUwm-Qr-N8fi1YPnJtiDOO8AU_tTGfPBbkjihW5Oaq7VTR1YN05iWQegq7OMk8-IPYa3ezdTQvDzjn4EsoivDQ27zUsGiF7-02aRpJNVJlkxwWZOCtYz1Zutw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFr5eb0YjKK-Uuk5fZnDbI5fR_EI7GbyipSzh7cAzXyDaJRMDrhij5DyF55efIzQWMNqhyo6yBh8uM7qUU6qKkrHPmhcRGujdBsXzse09ceXp7vGUVDtUwWdoMwutLGeJwuxtvEYnLsug3oL7zLRhlfAn6-qoi4vRafsfPY6Nt9Dd_CSPvx41_bj8umvp_c0vfn9Ux9x_UYB9gxTL-s7M72F_mlFM75XxY3PP5IRXGBXWpFGfbsxFWom2nVjx5IHv4oa5J06A4VeGddrNxRqk7MBX39m9om3vK2LUaFZ-BdYUKvPUhEYOWfjTPcezT_nibmS3n0s2tUWneVy_Bp9dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMv_oX84_dy-kz1xSCWHN9WANtlcvCphwLJ5unge43zfTuHiDBCDCv47Z4-b-QxE_wWuHPNLIJnkjd_cBmHjLGpXNf2vpcbS-9WMXyTiPn1qjt9jJFGpHxp8opuvykgEN7EOaiWqALvEPj4PiBjVtt1AhCKeuZr8sqKwij7UOJP0WHOTcb7jrQpC49zv7APIdTqK-Dt0b8ijM-J7LhQBYsEtT_waVQF8xZF9D1Y6X03heELGFBzIAMi4X5JD2p_psoMq1M1mEBVAYNn0ZU4J7uZMNtMoGlWM-mr5Z1XzjgQ9jHpb1WLAD6u0MVkMU5MaQCPv3HHWNGTrJN7oqDCbCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxT3Xq_wBIbuU5SPL-Ywg4k2ZuKziEdf50IGXtDi-_QjNi5IDF00pbS0oo50tN_fePJ8T7HKmgNh0Zj4DR61OR_7c9kqaPg9LeMBMtSLOJAm4LTovpgX8fsgiykYQfN_ZPUBGA62n-SedSVVnEfp4aF6dC3KuvUtTqGYqNBhwwVjE_LSOAWJ_DV6ZNqFahDVO4hcAq7MMubqCLU8xSNZhUXz1hrsOLYDxSXNrUu5-oLOsAIyiRMB6oe-svOijepd758jQx9uOuXKv7Oq1JqJg8UFmOUGz0bYxIeVOxO6QdCcSAf8oaYVgFyiiUtYpdrlbh6bRnWlTPJf1bipZUczEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62468a1ab8.mp4?token=P2x65BWKlonUaHqe_n2EJkYitBRnlF-bgGJlQ6hPGMCJRdXRWgzqIenkIUS3lbKl1pqVL-P9RJE-UlQPNqcxFmSXljnsND2mVPdnh7Y4mkjR77EGyKT3NpOOHGc4C1HIFIwRK1b8QKto4Rx7pXaHEvU7_rKQ1AJSLYcYGYi-zPb7IHO9RgjxG77-ImYlCLOjJsnntVIo_vRq2_9htJcj6u6OJUznS2j0iU-DdY7Z6TFcpzrMnGqGBCEHBGbFLyLcN86zHIVJWI1n_BAhtj42ugyHt4jyVH-Rgar1XwzPoIbidMOJhiscsPu6x4RyWZRHKJFlzk3Kv-RhFjZP4zrf7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62468a1ab8.mp4?token=P2x65BWKlonUaHqe_n2EJkYitBRnlF-bgGJlQ6hPGMCJRdXRWgzqIenkIUS3lbKl1pqVL-P9RJE-UlQPNqcxFmSXljnsND2mVPdnh7Y4mkjR77EGyKT3NpOOHGc4C1HIFIwRK1b8QKto4Rx7pXaHEvU7_rKQ1AJSLYcYGYi-zPb7IHO9RgjxG77-ImYlCLOjJsnntVIo_vRq2_9htJcj6u6OJUznS2j0iU-DdY7Z6TFcpzrMnGqGBCEHBGbFLyLcN86zHIVJWI1n_BAhtj42ugyHt4jyVH-Rgar1XwzPoIbidMOJhiscsPu6x4RyWZRHKJFlzk3Kv-RhFjZP4zrf7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تجمع‌های حمایت از تیم ملی ایران و گرامی‌داشت یاد کودکان میناب در اسپانیا، سوئد و آلمان برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/443799" target="_blank">📅 21:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443797">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f37986bc4.mp4?token=KGwkJb23lerpgidCvnv06vZGf1W00GNiUmnv-a3kVkgCxnmpEnlE17NaHqdAe8GWBl4onSIdUOHf9ZSwQeMnVzcinob5B8lw5rTtKe4WP4-RImU6pXOnIl06-7nu6P6KPcn43EFPHJrR4_nipV6arSVJWCoTcA5568m3-Uq31rL4Eiqj2RT-2ESnnmZcH-OGUuVWi-PgrDAK3hRAuQWRq-N-9DwAAMLdFCfYfz1OOkInjDYZGbhFYMO_DMqPOhfVeaGyvRjM57gF_Qh4OMKd6mp86DErEH3C_0evEu0AtjWUvZ98EdKHqWDgqtWQbE9J3vMcfyotKB9Glt4--2HO_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f37986bc4.mp4?token=KGwkJb23lerpgidCvnv06vZGf1W00GNiUmnv-a3kVkgCxnmpEnlE17NaHqdAe8GWBl4onSIdUOHf9ZSwQeMnVzcinob5B8lw5rTtKe4WP4-RImU6pXOnIl06-7nu6P6KPcn43EFPHJrR4_nipV6arSVJWCoTcA5568m3-Uq31rL4Eiqj2RT-2ESnnmZcH-OGUuVWi-PgrDAK3hRAuQWRq-N-9DwAAMLdFCfYfz1OOkInjDYZGbhFYMO_DMqPOhfVeaGyvRjM57gF_Qh4OMKd6mp86DErEH3C_0evEu0AtjWUvZ98EdKHqWDgqtWQbE9J3vMcfyotKB9Glt4--2HO_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لامرد غرق در ماتم سیدالشهدا (ع) شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/443797" target="_blank">📅 21:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443796">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a333d8ce.mp4?token=Ccerbcx6u-CRPlBbX05yFusmpjvLkmY-G7gkUckXxcCm8Do-2NdCrqVv3u7BSMgjEt8Zp_ANy6VQjtNkt1jdjoShDDAAUQbjjrJm4gVqgz8Vpm31fHkwOJMCtnmeBz9adO1s9Ul4oBp7OKeLwj1Asuagf15G8KHAxZz3nGfchpUxFu40ED6Rgtbn3WAwL0jZZqiMeHCveJfIfeqLgjf54qUuWfykL1ACiVZ1USlusXPW2PZZzl46TmcZgP0wuUGxN1W-ibUfCsgGf1vyasBTTt6_m9JWUO0nx6UuiAtDDAoX-mBjg1CJrSUe5vzAE3yKb7Z5IJtOZvRF1c2uzrvzhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a333d8ce.mp4?token=Ccerbcx6u-CRPlBbX05yFusmpjvLkmY-G7gkUckXxcCm8Do-2NdCrqVv3u7BSMgjEt8Zp_ANy6VQjtNkt1jdjoShDDAAUQbjjrJm4gVqgz8Vpm31fHkwOJMCtnmeBz9adO1s9Ul4oBp7OKeLwj1Asuagf15G8KHAxZz3nGfchpUxFu40ED6Rgtbn3WAwL0jZZqiMeHCveJfIfeqLgjf54qUuWfykL1ACiVZ1USlusXPW2PZZzl46TmcZgP0wuUGxN1W-ibUfCsgGf1vyasBTTt6_m9JWUO0nx6UuiAtDDAoX-mBjg1CJrSUe5vzAE3yKb7Z5IJtOZvRF1c2uzrvzhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع عاشورائیان سپیدان در قرار ۱۱۳
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/443796" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443795">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950ef5c419.mp4?token=kJdT9Lntiz7evFvluJT6xVsZ_teEuK674gqkvCseIDtCZ0dtnaY9YBTUh87VUoTAYLObpeBfl1fVlk-LXzGMqaBLCTfCaXfpQvemqD8gTS3ExHrMf_qzeOg5gfJWZw-RV5lQjtRfGNva6T9EYqBzkCZSSZxpx0xndrnhlTQfvniwI1xor80d-t5lLO072n3pC9Sch6DNYkaeAPp97MudEC-ZRSeBPfby-ZdExniFVeGNfCS3EDXdeRwMa4oyNBuB3erAn1wjEJJNJEyFh0SiFNvDtgwd_yfT5ep_6jGNUHdaEkkQKRdskEIEJ2ER9hYj6Hqk-WYjGVaNStrVq9OPyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950ef5c419.mp4?token=kJdT9Lntiz7evFvluJT6xVsZ_teEuK674gqkvCseIDtCZ0dtnaY9YBTUh87VUoTAYLObpeBfl1fVlk-LXzGMqaBLCTfCaXfpQvemqD8gTS3ExHrMf_qzeOg5gfJWZw-RV5lQjtRfGNva6T9EYqBzkCZSSZxpx0xndrnhlTQfvniwI1xor80d-t5lLO072n3pC9Sch6DNYkaeAPp97MudEC-ZRSeBPfby-ZdExniFVeGNfCS3EDXdeRwMa4oyNBuB3erAn1wjEJJNJEyFh0SiFNvDtgwd_yfT5ep_6jGNUHdaEkkQKRdskEIEJ2ER9hYj6Hqk-WYjGVaNStrVq9OPyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورزشگاه سوفای لس‌آنجلس ساعتی پیش از دیدار ایران برابر بلژیک
@Sportfars</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/443795" target="_blank">📅 21:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443793">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApCpo5SqgTjiFTHRrLqP_OYHhQlbt4Uw918BUXiNbOdmf2nEd8YF7Fv_N7HlUpdwZSOU-lHc-ol5lD6TNN461mBHYrJeRyaRJts-S-zqrdxs0Kg6SNe6Ya4KchQYs-RlfVYTWf3FjAqyjTR0o-q-3sYNFlfejQ39C5-arKg1zCuYm943o-mDET6cHqJXgFqs9Ssk4zfNSLNKB4VrwTTMT7ZAwTVbRZ5myQWQH1clfPrGOcoEDv2Tb97A6-nMoMwyz1O7C2XQEiCNykJBAXHAOQRacqo2woT7TRIAOIXw1nuf9sPu0EnbY_g7Y6YjWQFCxthODviyPDlHaqOKXb8X1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر اقتصاد: تصمیم‌گیری در خصوص نرخ سود بانکی برعهدهٔ بانک مرکزی است
🔹
نرخ‌های بلندمدت نباید طوری تعیین شوند که سیگنال تداوم تورم بالا در سال‌های آینده را به اقتصاد مخابره کنند.
🔹
در شرایط کنونی استفاده از نرخ‌های کوتاه‌مدت برای کنترل نقدینگی و مهار تورم، منطقی‌تر از افزایش نرخ‌های سود بلندمدت است.
🔹
ثابت‌ماندن نرخ بهرهٔ بین‌بانکی در سال‌های گذشته، آن‌هم در شرایط تورم‌های بالا یک «خطای راهبردی» بوده است.
عکس: مرضیه سلیمانی
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443793" target="_blank">📅 21:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443792">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎥
زبان حال امام حسین(ع) در نماز صبر بر داغ علی اصغر
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/443792" target="_blank">📅 21:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443791">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs5l13CkVas8J9gyp2H2rmukTM7cTAxEGsXLn2cy5cImoTucOQdJAOmlgzc2ib2PpPQLSW2gEs2MWDlFsJFyd6AtuWqKa34W0nt1c5XXpVon-BdFOKrgBiJXykU2RUssrdISt06W-lIfl_D6XYFtiHe63dLc7fdXMmJhtXTlp6j_rf71P3ZZ9C7K1qbO-KjZj07NAsm9Z55lGqHyOl6xkq7g3zlyvymimo8D0GxFgY0uOFy70QvLSdbctBA6wpmmon3VFaTdkSi9A3aDs6-xnppmIonIlciUz7H0XaxbqcZd-5E3G306ZmyQZk9x_Mza3MYg51k2wAhlxby2uK7buA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب ایران مقابل بلژیک اعلام شد
⚽️
بازی ساعت ۲۲:۳۰ آغاز می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443791" target="_blank">📅 21:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443790">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3I0cj6IinJCUICIysQzQ_BcILFwPeQD_d1UTQqzTbrE-J4Kl8CHwz5-mmCmSYW0nZfs_AI-fyfRongHS7W0azV7QAsEoVdlRekjQWMH00nK7E7yOQ0tod2BDuoQ7X-lvC4urlZDmdoXuJQs0mCxwsY8yZz2niVBl3wnUhQMlxqF_hz4U9lVdKgmlOcx-SScj9Y15vixIIdj5e-Qv05r4nWIsjQnukb0SnaOLr-YxirD9TgKrgicr3cSb_KgNEGmahyNjmoEeBk_n0F_7b3TbMGh0y-Mh6hcLpj4Tcz4e7szM6NO5iWUMo4nbgoCbCCF_k5WW3zBPn11gzO3GXRYaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای رئیس‌جمهور؛ دشمن هم صدای شما را می‌شنود!
🔹
خبرنگار حوزه دولت خبرگزاری فارس: این روزها، تقریباً هر جلسه و دیداری که دکتر پزشکیان در آن حاضر می‌شود، با فهرستی بلند از مشکلات کشور آغاز می‌شود. از گرانی و تورم گرفته تا ناکارآمدی‌ها و گره‌های کور مدیریتی؛ ایشان با نیتی صادقانه و رویکردی شفاف، سعی دارند تصویر واقعی از وضعیت موجود ترسیم کنند.
🔹
اما نکته‌ای که در این میان مغفول می‌ماند، فقدان «راهکار» در ادامهٔ این فهرست است.
🔹
مردم ایران به‌خوبی از وضعیت معیشتی و دشواری‌های روزمره آگاه هستند؛ آنقدر که نیازی به تکرار آن از زبان رئیس‌جمهور ندارند. کافی است یک‌بار برای خرید به سوپرمارکت محل‌مان برویم! درد آشکار است؛ آنچه مردم از رئیس‌جمهور خود انتظار دارند، «نسخه» است، نه تکرارِ درد.
🔹
از سوی دیگر، در شرایط حساس کنونی که کشور درگیر جنگ ترکیبی و رسانه‌ای دشمن است، هر سخنرانی عمومی تنها برای مردم پخش نمی‌شود؛ دشمن نیز تک‌تک عبارات را رصد و از آن بهره‌برداری می‌کند. تأکید مکرر بر مشکلات بدون ارائهٔ افق روشن و برنامهٔ عملیاتی، در بهترین حالت بی‌اثر است و در بدترین حالت، به «پالس ضعف» برای معاندان تبدیل می‌شود.
🔹
نکتهٔ قابل تأمل دیگر آنکه نظام در موارد متعددی برای تسهیل امور و همراهی با رویکردهای دولت، از جمله در بحث مجوزدادن به مذاکره با آمریکا که موردنظر رئیس‌جمهور بود، گام برداشته و میدان را برای ایشان باز کرده است؛ این درحالی است که سابقه و تجربهٔ تاریخی نشان می‌دهد علی‌الاصول این مسیر، بیراهه و بی‌نتیجه است. این همراهی نظام، انتظار برای ارائه‌ی دستاورد و برنامه‌ی عملیاتی را دوچندان می‌کند.
🔸
آنچه از رئیس‌جمهور انتظار می‌رود، عبور از مرحلهٔ «مشکل‌شناسی» به‌سمت «راه‌حل‌دهی» است. اگر مردم باید کاری کنند، دعوت به اقدام؛ اگر مسئولان کوتاهی دارند، خط‌دهی روشن؛ اگر رسانه‌ها باید کمک کنند، تکلیف مشخص. این همان نقشی است که مردم از رئیس‌جمهور خود توقع دارند؛ نقشی که فراتر از توصیف وضعیت موجود، به ترسیم مسیر برون‌رفت از بحران می‌پردازد.
🔸
غُرزدن را هر کسی در کوچه و خیابان بلد است؛ اما سخن رئیس‌جمهور باید افق‌گشا و راه‌گشا باشد و همراهی نظام را با دستاوردهای عینی پاسخ دهد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/443790" target="_blank">📅 21:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443788">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnM3lS_-SvBiLA9AVyDY7a8RPvbaBrYvEUCx3cjCv0yrtDOkb-7ed1kXattEsimgZ4kzFwjRNFCu7SjweNFHGzmkp-dxB2ruaskduTf8VoO5uhrPGamcxcz53SZZxOg3RIPirNEtk2ndOBBOlRfU4T9EEgMzz90kXF9bYvoPooanrI_skm2fugDiIt7d9Vt-yly-2X_ZjdIAoPg6y71q4hD58CkvZSkPceyXS48bw5Ss6d8QrI-G0bFRL1fHUFCDxv6v-KawU8gU1eeOV2c3YqnxvfRniph_8xkjOSWV0q3iSPZFdV8YR6ZxDlwUE9Z-3JdQGmsBAspS6YJZfAl0WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز ۶۰ قطعه از پیکر دانش‌آموزان شهید میناب خاکسپاری نشده است
🔹
رئیس دادگستری هرمزگان: هنوز ۶۰ قطعه از پیکر شهدای دانش‌آموز میناب که در تفحص‌ها از محیط مدرسه و فضای پیرامون یافت شده، خاکسپاری نشده و باید شناسایی از طریق آزمایش دی‌ان‌ای روی آن‌ها انجام شود.…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443788" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443786">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixxsveqXbp6vAlqKeaO1VRJ0MDTVzyG8J91TVc2IRNm0cbl0jQN-4yKDbxjlAxDu5HbmH6sIgDVzrK6TNPUywcnHOjMg5_gAn95bnXMk8EUpzq-Vn7CqxqVS6SOoi7KuHT3LzgNbPDFU_DyVez6y5NoPzVArw5vd-G9US4yrQvs4WSpt4d1mRE6wS8bulh1d5vHKJeQikk4hd4vnTGQT_IMZzRUBjgHgrXGyPyN3wys0IY3ROLMvKtQ8GeJK0zMtc0169le8GOBQ2KkvOQEbCIIZ4su558rlgX5TVNcP4zXdlS6DiG_K_3PnTvWGCyJJESExAiNYn46drf_yJV9tYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443786" target="_blank">📅 20:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443785">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba735417d.mp4?token=GvYBaTPageBrLMc3xZxf4qAmtQwmhPNPqaxIfDZ7WdTwi7lQLG7bnNiF-zzBpYoW74w_a5Vag8XRc-yIercoZvDVd-tz0nS_aWS6pwW7WIpXc7NMVnLywThAF1_oMlcJvTWX2JENczizTzT909fjazpx8sEEE7tYDQCAtHXUv15pkfk23kPScjw7QcHjl9-4PpQh8NJh_YgiXFBSykUsmXeUvAgYnBj_-1RQxj9LYy71LGrJSRvL25hLpjo7lrjZeheSQC2bPgHbkysXxPiHW4vN2TpCdNSX-oYEI4fAPiLyMJnDI2N59Au5A9OxBZRxlvR2UJUxKPj6Kg5jfek-ZJgbE-_UVPRzj7yN3YV5IBQ6NqeMu-e4L7yv0BOPRsczSJS96yHhCUvtCDNlqadmHCXM_fc1qutA1MkiNd20y6rj121XnDaRJpfGV-vPVMDyqxyAmHc6ZeR-i7UyRieFojbBF9xR2ybEs9M4VZhCmeLyQcf68O7hRN6Z8wZnuxivyShtg7u4RY5vk2wNaUS_nUBZ1NdlIwhAB642bVfgIJCTNSAjFNKv-tgbKmW1OQ1HcRH3LAb8jLoPyWsw_SQDmBdihPMMyeUcXbBDkrzA279LsyoQ3usAtkieQhAnqgfnxZjUSry41_pR3pb_CVpZu5Et_nTNA-_QLqflwU9sOoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba735417d.mp4?token=GvYBaTPageBrLMc3xZxf4qAmtQwmhPNPqaxIfDZ7WdTwi7lQLG7bnNiF-zzBpYoW74w_a5Vag8XRc-yIercoZvDVd-tz0nS_aWS6pwW7WIpXc7NMVnLywThAF1_oMlcJvTWX2JENczizTzT909fjazpx8sEEE7tYDQCAtHXUv15pkfk23kPScjw7QcHjl9-4PpQh8NJh_YgiXFBSykUsmXeUvAgYnBj_-1RQxj9LYy71LGrJSRvL25hLpjo7lrjZeheSQC2bPgHbkysXxPiHW4vN2TpCdNSX-oYEI4fAPiLyMJnDI2N59Au5A9OxBZRxlvR2UJUxKPj6Kg5jfek-ZJgbE-_UVPRzj7yN3YV5IBQ6NqeMu-e4L7yv0BOPRsczSJS96yHhCUvtCDNlqadmHCXM_fc1qutA1MkiNd20y6rj121XnDaRJpfGV-vPVMDyqxyAmHc6ZeR-i7UyRieFojbBF9xR2ybEs9M4VZhCmeLyQcf68O7hRN6Z8wZnuxivyShtg7u4RY5vk2wNaUS_nUBZ1NdlIwhAB642bVfgIJCTNSAjFNKv-tgbKmW1OQ1HcRH3LAb8jLoPyWsw_SQDmBdihPMMyeUcXbBDkrzA279LsyoQ3usAtkieQhAnqgfnxZjUSry41_pR3pb_CVpZu5Et_nTNA-_QLqflwU9sOoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت درگیری بالگردهای آمریکایی با مرزبانان ایرانی
🔸
این روایت با کمک هوش مصنوعی ساخته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443785" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443784">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66174a612d.mp4?token=SEHvT1sgcuic83_VDMRVhgmzk6xhjJH05mLZsdvqWhe67AMkszmSpHanzfjcvl0FMEiPpCxZjkzudSHQptcLZCPcvGv7i8Py1xYlKz23107WZYlcR3DMqbq6Vn6gT9yBn3fuDLe_SLJb0OD5H5OxxWV7vrOr-m94ibYSBp3weHyezoRqOGl1uxKwsmcwyeoh679pC0v80UH3UzC4HQ6VX6OphGc3nNseN7KgjBNUyEkKBnRPTer6rwtnj0GGC597trWSNbAIEq3-jhPf9FKXAjWj2rtV2TuJQSdC0Wa8S_q1EqXz9FU5FKxtudnt2PRKmWaE14BscU2j7j2KnnL63Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66174a612d.mp4?token=SEHvT1sgcuic83_VDMRVhgmzk6xhjJH05mLZsdvqWhe67AMkszmSpHanzfjcvl0FMEiPpCxZjkzudSHQptcLZCPcvGv7i8Py1xYlKz23107WZYlcR3DMqbq6Vn6gT9yBn3fuDLe_SLJb0OD5H5OxxWV7vrOr-m94ibYSBp3weHyezoRqOGl1uxKwsmcwyeoh679pC0v80UH3UzC4HQ6VX6OphGc3nNseN7KgjBNUyEkKBnRPTer6rwtnj0GGC597trWSNbAIEq3-jhPf9FKXAjWj2rtV2TuJQSdC0Wa8S_q1EqXz9FU5FKxtudnt2PRKmWaE14BscU2j7j2KnnL63Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل سوم اسپانیا به عربستان در دقیقۀ ۲۴
⚽️
اسپانیا ۳ - ۰ عربستان @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443784" target="_blank">📅 20:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443777">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4OTaRIlROHJG4871Lr4f-7cYrI56-B2HmtPf9mXOcQVAe__FvvsmnM0s5jaMwA91YGm_0FGx_pC3hJSJR5P3_L_EF7PY9_lQeGf8YOO2YnXQmUrR-i-o7eFB9jKzJIBnI5d-1WarsrOpuilLIJu4nMyxWjQaZl31mIqxu8np9LXoxnEHKPZUCoV4VoY-umAnGT1JEqHe8d0EtZ-ystkgLLsWcHnxaCdsj7gFYgTxcbKjMXCCke0rtZ2bh1KTb1ClUpMzGpFTOuJ8T6i5jrP6YowXyrsFTi5ZmwIWwHqf5n3unrIJUtYpLXV_Ad-YHEqy6TsaFlBdfAVk8QLPeK_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VpMnpLA_Mnq7ijKgfjczymOnLoMnROypExOhq79XGP2ze6yRWXSfRqd8VwuoW73IUR0n6diXLT5hPCWw-t3MvNjDK7-VW0kTWACV_U05HzDmLqwEjrlFB-nrFTFWcwEHzxWlOE8kBiAQtHEo2CmEvnPZl1l7UwuEQY5HjylxT3bujXJf-cv28ta-KnJaPhcSwwuzUMbr_RBX_cg3iTpNaJIq5YKLYA26hNkcvQ6URU9cJcwR1ZTnZRrLJKJUfFATeumv13dYkubhS5VlYLvCI6raFaXy0AY42K0O-xcSZPzVxSpzdtYRN0FzHygbRLJaFKsU84IbqmVkg2S-4yVSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1awdbIQub1Y936TPMNHYIRQNwvHXt6z63DqhL3LN_trI0iQD4MHPfuFFvIMan8mI99FuIxz9WG6D15NJ0-mPRkXpDoBlfdS8QFdzHrJXEm9jxsfoJ1lkqxWyXAsJHP9FoEzPA8OIRAiEvzISUbsz-sseL8KHPLTgAipn8yvTyvE3WDg4mNKwL5lIIf972HxqbpRX1GFoSBlKvT7DQkozbRNvF6VZ2ZEykkCDw3faSZzgc2upTz0cKgcTUyz_Nb1awHbJelYQnC6eYz1eRThwQj3MuaV4_YPcf36zwNNTgPPskcI32t3WIQJ__9djb2uFZQc9zVMEXpoJ1iS37X8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZTngXPnkuSUmng8xNh8FWBoE7zf3bciLWepiJE4ST62wqVsfkdPy6DnG86yVZVDpkmrE1uN6IFyz0TtnnDTsSEcT3lmcKLqQM3FbPCIoNRksme0TPOqrMKjoLe6bGaglNmBk1f_JRWyFUAbh2qm1IVHPpshoiWheMn-M6pVOZVS04tekXbTPbDrdogP5VvU3T_KlHICSN_XWMLcgk_sa8MZy6HGb4y63r4OsXH_pkDqGaXrc3Y8uuUkCEhE66MDA-xKd_hL7xDUl5XvnGDG6PGQqRXouoF0fjBv-YM1K0wvaLCMRRFn0yX0iyax07k43obFaVNaitcMn64yYMfCWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R89OnV4wHGWdL7ftA-o642x3ZPywsA38P5s3nwkb7Xpw5mGk3kxfHRr4nWs7tksAjcbPa2BTpxqve4-IllWpYt2IR_xqkfWeNrmrO-8Eeb5r3YWqBWtl09b9EMwlrBDYCg82Bch4qGWtmnJ4tr33a904rFRAeMfF5jSTMA6S2fAv4VlpBi5zqX9Eh-HqoRSDMzHmrQmJJ-MOvYqNFmk6jIOwVo79188PvSbY5G3TIwH8txklTt4zf471bVXAXxfz1W7lOxGCFos_r0JF_pimNT7ahiyEoy6IZq7jj7z96g-_bYBjsV4ofnVZc7kOgxR5GfU122ZlZbZV3L9NMCuNUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LajPuZFgbWAM2EorCdbqfMvya00p6BprqfmHrIvJ56aTe2fkW5ANjqYxSBuEClnuKB6958o3aclnsz6_0qxSu0hvf9EAGm4kVBCpFQK7zRG6SVqtiLl8PGtjBqLPhTIjJhULcrFIqENBbIZ_PDAm1u_Y3QpTlCos9zZMeTaNdjQA2hj9Ai5XDHYJCrrayV62aPDxxSgUrm02MG8xsGIEldzj7tiuLbzCFS_uIb2Yhj7rr6sxf7YNHRk1xitqFlE7D3v1XjpHXRrA4GfSvUy_JKCAubfR_m4xM53M0xmFO2XYUSWiquJ-KPXAA9HAMv_8_Fuelvh3QLicaha5oMdzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4IQJRxFvLcw1zjCr63m4D7MdLWFNcZ1iKvXPM51BAhYOcdlN08tQLoov_8JdNzK3CLCssY67abkihRR950Zw_MZ6igH0khFuykSRkUzQT2ScszpsV2knQy04QqUgkzClLbqImj-fR4aXCAULPa5NF5Diu7ND7gAqd19sSF08A-RDNxss4jdWgELhon7k0tLhajwCWyRqTRpR-c5qxbWmjT5vX6T2GwIIf9U-M_8gO4GUdrZiKJ701O1tihaqkNelDtUyAZmw0rN7SExqILGdFpsCJMNxDiqs7G8i-sUbs4FgcXZF-xx0-oYy3Putu8oYz-_xGBH8WDSycj12GzBCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری سنتی در بازار تاریخی اردبیل
عکس:
رضا خانبابائی
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443777" target="_blank">📅 20:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443776">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌
🔴
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/443776" target="_blank">📅 20:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443775">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044678e878.mp4?token=tsSU4Rual3CTPMyEZxJYaR7vVSJVcXwON9ZxQBFJUUd39e5gF1AKUcszRO0eO4vbOM4QbZfqAZe4lFquQ8O-VlQ-8nXM6jSE73SKKv-pq-8z9GqBXRkoqjgX9ZHac8hQvyxDROJ1hmVt0SoT71stLbA6RQfMyU6YcjGCQdMZrVt0NKCAV2pVpvmJu44HY_Pwf70ho7wNPXF1P4T0uMhtXmtdUFJzfEhbW6W5y5a5b3etk4sdzbl4ARSWMB7TjVwwgnfEbmjpe4_D3Dpva246VEcR_JQcoPLjhS8dLk5HUIA_BouY3VyyBSdaFpO6Gu_Epxx0AoOjj1GriW954bdSsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044678e878.mp4?token=tsSU4Rual3CTPMyEZxJYaR7vVSJVcXwON9ZxQBFJUUd39e5gF1AKUcszRO0eO4vbOM4QbZfqAZe4lFquQ8O-VlQ-8nXM6jSE73SKKv-pq-8z9GqBXRkoqjgX9ZHac8hQvyxDROJ1hmVt0SoT71stLbA6RQfMyU6YcjGCQdMZrVt0NKCAV2pVpvmJu44HY_Pwf70ho7wNPXF1P4T0uMhtXmtdUFJzfEhbW6W5y5a5b3etk4sdzbl4ARSWMB7TjVwwgnfEbmjpe4_D3Dpva246VEcR_JQcoPLjhS8dLk5HUIA_BouY3VyyBSdaFpO6Gu_Epxx0AoOjj1GriW954bdSsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حجت‌الاسلام میرهاشم حسینی در برنامۀ سمت خدا از تعبیر شگفت‌انگیز اندیشمند آمریکایی در خصوص چرایی مقاومت مردم ایران در برهه‌های حساس تاریخ
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/443775" target="_blank">📅 20:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443774">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دادستان تهران: ۶ میلیارد یورو تعهد ارزی بازگردانده شد
🔹
علی‌ صالحی: با پیگیری‌های کمیتهٔ مبارزه با مفاسد اقتصادی و دادسرای تهران، حدود ۶ میلیارد یورو از تعهدات ارزی منقضی‌شده بازگردانده شده است.
🔹
بر اساس گزارش مسئولان بانک مرکزی در یک ماه اخیر بیش از یک میلیارد یورو به‌صورت نقدی بازگردانده شده و حدود ۲ میلیارد یورو هم تعیین تکلیف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443774" target="_blank">📅 20:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443773">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qs4QHvzzD9fqw9qmgmXuB6M_2Wni2MtaxUuyn7m6xlJd_3OOVDEDI85jExAYcskbSM6xDHdlpkb857AvukcYbyQNaQ0JFdtEqICRh7AT2t922rPzCuYicklpssTPPNUo3JkpbmaITtHQ-2nJTNmOqxWaYXJbev5OC9akQVDdSSxHi-UiK_4LJcg3XNVtkzEOpKzfuF6TpbYcU1X_mODGVPQOozAEtmBHKeplirt5nr3pSfI4a5jMthnNhZ_UExKFCiYAGFXjlP_dMdKzDLHwKtUF6XzDqqfPOD7563u1Yw4YU_6o2CZlPbJwqwBYt-YqJNRPgBluIVAhVttmlU0wbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌ثبت‌نام حج ۱۴۰۶ از دههٔ سوم تیر آغاز می‌شود
🔹
سازمان حج: پیش‌ثبت‌نام حج تمتع ۱۴۰۶ دههٔ سوم تیر آغاز شده و همزمان این سازمان پیگیر تثبیت نرخ ارز زائرانی است که برای حج ۱۴۰۵ ثبت‌نام کرده بودند اما فرصت تشرف را از دست دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/443773" target="_blank">📅 20:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443772">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🖼
قالیباف: تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم؛ آمادۀ پاسخ هستیم
🔹
با خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
🔹
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/443772" target="_blank">📅 20:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443771">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5071210334.mp4?token=E_HpA6OSvps2t6aOxdyu6os2tlYo5P120Ppo6uFvgOzO0Y8_Bv0DDyWe3VAagYdCC20_9MV8Gq2tD_XOzU4vhNoJUgf_3A4UM1pV0nN-Wzw-ckVwLr8uPxZHpsrxXpX_U2g8Nal2_CNoGppp-vlScw48J9j-tk0IsNnR_iQ6PC2l1hYFZ1s5jSCAG257BF9UVVK3B2sFDBTwURALqR0VdHhGcrO76fDnJ1TsjlCaXD43yjnr-dnAG-fMXztR4rr7Y0KObLjD7f1GG9WdfyA_HbYdaF__04pcjpGw14wQg3J-_tyeKUprh60X8v5Yya6hkSZ4WXKwx6J6lFKVkvItS4RlucEhoLQxom1Kg_-Gt7BdW4DZvvjSrEkG6tM7dBFa8ihn0F4sCJCGevG_poWPOPC7DHxr8UACiVZFLoVBrTyA1reEd4HYPiwMeBr1YAmd8-uMMwNJen7HlXuf0dhIv0_M1Rf4uj6SLUGh4tPgQ5yqjvuDmvKOwhRn1vuJD9-FfbPd8hrH6Dw-k2oOx_N9wxt2V3GjAszoGwU9aS9UFXyqT-L1hp0yaXTTHhvNXE0gsPWF0RDaVZ-s9BV0HnA__Nbg-lAkLU4RP7JSOhIbxdV5dmNrd91_UU7tzgBsN7vUxh7rC2OsB4HuGsTReGy4rPq1CZIQhGJP303wwMKCmw0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5071210334.mp4?token=E_HpA6OSvps2t6aOxdyu6os2tlYo5P120Ppo6uFvgOzO0Y8_Bv0DDyWe3VAagYdCC20_9MV8Gq2tD_XOzU4vhNoJUgf_3A4UM1pV0nN-Wzw-ckVwLr8uPxZHpsrxXpX_U2g8Nal2_CNoGppp-vlScw48J9j-tk0IsNnR_iQ6PC2l1hYFZ1s5jSCAG257BF9UVVK3B2sFDBTwURALqR0VdHhGcrO76fDnJ1TsjlCaXD43yjnr-dnAG-fMXztR4rr7Y0KObLjD7f1GG9WdfyA_HbYdaF__04pcjpGw14wQg3J-_tyeKUprh60X8v5Yya6hkSZ4WXKwx6J6lFKVkvItS4RlucEhoLQxom1Kg_-Gt7BdW4DZvvjSrEkG6tM7dBFa8ihn0F4sCJCGevG_poWPOPC7DHxr8UACiVZFLoVBrTyA1reEd4HYPiwMeBr1YAmd8-uMMwNJen7HlXuf0dhIv0_M1Rf4uj6SLUGh4tPgQ5yqjvuDmvKOwhRn1vuJD9-FfbPd8hrH6Dw-k2oOx_N9wxt2V3GjAszoGwU9aS9UFXyqT-L1hp0yaXTTHhvNXE0gsPWF0RDaVZ-s9BV0HnA__Nbg-lAkLU4RP7JSOhIbxdV5dmNrd91_UU7tzgBsN7vUxh7rC2OsB4HuGsTReGy4rPq1CZIQhGJP303wwMKCmw0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این شماره‌ها متعلق به کدام ملی‌پوشان است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/443771" target="_blank">📅 20:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443770">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f8e34612.mp4?token=Ke61eg-8V7RnxLo2sbx0oheR3To30930rDWejR0gJl2EbXMtIi_Yt0OgdnFuQJEGC9-S8HmzSSoFKWTOuDsjWyI8raGw8DO85y6K_w2A3fIU5hwnkKhzdQqYHIt_-TNIf0Fl_WrMakSHWQxDVr0VUNGgkztLGtPmaM8LLp3O_8uWXEbRZpMTR7LcK2riV1MexZxEbkAMbIMvN8htzlZ-rvQtW-kO0lgcfId5kSMVFAseU8V30xs6HpuoTR6tS0uBzXmP0yYMVGJkSKsK0BwIUOKBBIXWje8hbti4UVGpnpOlOX2NPdD0If5ym15_E98_ki8nQ-awAuD7NBLuBOTeHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f8e34612.mp4?token=Ke61eg-8V7RnxLo2sbx0oheR3To30930rDWejR0gJl2EbXMtIi_Yt0OgdnFuQJEGC9-S8HmzSSoFKWTOuDsjWyI8raGw8DO85y6K_w2A3fIU5hwnkKhzdQqYHIt_-TNIf0Fl_WrMakSHWQxDVr0VUNGgkztLGtPmaM8LLp3O_8uWXEbRZpMTR7LcK2riV1MexZxEbkAMbIMvN8htzlZ-rvQtW-kO0lgcfId5kSMVFAseU8V30xs6HpuoTR6tS0uBzXmP0yYMVGJkSKsK0BwIUOKBBIXWje8hbti4UVGpnpOlOX2NPdD0If5ym15_E98_ki8nQ-awAuD7NBLuBOTeHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم اسپانیا به عربستان در دقیقۀ ۲۱
⚽️
اسپانیا ۲ - ۰ عربستان @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443770" target="_blank">📅 19:57 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
