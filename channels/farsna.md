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
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 19:05:31</div>
<hr>

<div class="tg-post" id="msg-463035">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: اقدامات آمریکا و اسرائیل این اجازه را به ما می‌دهد که از معاهدهٔ منع گسترش سلاح‌های هسته‌ای (NPT) خارج شویم
🔹
هنوز تصمیمی برای خروج از NPT نگرفته‌ایم و این موضوع به رفتار واشنگتن بستگی دارد. @Farsna</div>
<div class="tg-footer">👁️ 688 · <a href="https://t.me/farsna/463035" target="_blank">📅 19:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463034">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: ما همچنان به فتوای رهبر شهید انقلاب پایبندیم و دکترین هسته‌ای خود را تغییر نداده‌ایم، اما نمی‌دانیم در آینده چه پیش خواهد آمد.  @Farsna</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/463034" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463033">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: ما همچنان به فتوای رهبر شهید انقلاب پایبندیم و دکترین هسته‌ای خود را تغییر نداده‌ایم، اما نمی‌دانیم در آینده چه پیش خواهد آمد.
@Farsna</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/463033" target="_blank">📅 18:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463032">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/farsna/463032" target="_blank">📅 18:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463031">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkD6kA9qSR3wRvNa7oqclY1C126buJd3yjv2-34wGMhaJRj4BEG_AznPYuJlA7xDCgz6E0X6X2aloGDzylx2GMF7P1CT_3C_yZTCn13pn_93uActfdhTbmdEQ0j2D4ibQVUcK7S09qPXfV4qTI39cL7gW8SSBjqxUQ9hKnMAa3ZQdzEnxSato-75990eE4bnAqYtyL5zdFzc6O789UyOSsg9NF4vQPH22xQXha42PqBcM-nLQWfP7O88grtOg-IUV-JW-6cMIX1EInZtw2q2lKC4DWcgLd4dF2Cmst9fKVUYo-sVfsPuC7D3eYkP3mANW_2MzVJRtt5diqBYBOUF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرهاد مجیدی، گزینۀ غیرمنتظره مالک نساجی برای نیمکت
🔹
پس از جدایی مجتبی حسینی از نساجی، گمانه‌زنی‌ها درباره گزینه‌های جانشینی او آغاز شده , در این میان از سعید دقیقی و محمد ربیعی به‌عنوان گزینه‌های اصلی هدایت نساجی نام‌برده می‌شود.
🔹
شنیده‌ها اما حاکی از آن است که رضا حدادیان، مالک باشگاه نساجی به دنبال مذاکره با فرهاد مجیدی است تا زمینۀ بازگشت این مربی به فوتبال ایران را فراهم کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/farsna/463031" target="_blank">📅 18:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463030">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/farsna/463030" target="_blank">📅 18:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463029">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/farsna/463029" target="_blank">📅 18:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463028">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMMd-fdn3FfXw4ndWNiWqcP43NAfRPJuZ3pawPXuHKCB8IdTo6NvVoY3I8jk4fUgvloyGKA4CiteGooEhVJivoJtESvxW13PA-HFPgfwVbCi3jXLfkfsdo4Bw2ntbyLAXSPzv6asrxK5c8aED140mVGYROvqpjQ4SKsvjvdCK72pEEqw3qXe4sgf8zGZ281TCRpy-u0sRMUUs9PO92qvZ5kaEjiZgGXwwTHlkYKyMAQRCXRCvFTfZDZSr1FCOBstCGBzdaPuEruDWT5NrcfS-H-wh2AqUlcAsRbC99GNZ_oxs0jbZP8sLY7g_h5XxKZT0eI4cGKdMC_adXJ5i9SFBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقایی: اتهامات دروغ و فرافکنی آمریکایی‌ها تازگی ندارد
🔹
سخنگوی وزارت خارجه: سخنگوی کاخ سفید فهرست مفصلی از اتهامات را علیه ایران مطرح کرده است. نکته قابل‌توجه اینجاست که بسیاری از این اتهامات، دقیقاً توصیف‌کننده همان اقداماتی هستند که خودِ ایالات متحده آغازگر، عامل یا حامی آن‌ها بوده است.
🔹
این گریز از واقعیت و فرافکنی، جای تعجب ندارد: «شریران می‌گریزند، بی‌آنکه کسی در پی‌شان باشد.»
امثال سلیمان ۲۸:۱
@Farsna</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/farsna/463028" target="_blank">📅 18:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463027">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/463027" target="_blank">📅 18:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463025">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/463025" target="_blank">📅 18:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463024">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUF2N6oGjrP7V_2h0iVk1WJUq0nLlcy17znoxVzzRUERxbdyIOQ9xNlFJvuvmgOZohaUVEWn0JoOuZ4uxx2sg0H3-cwmLlhHchF5na-WouT8pfkwdMCbbuSiOU9_q8hYlckw5cxRPH9-jw6Jvb8W1TdI7l9rfXDN-wB4q5lW1-HyXPpLz6SRB3WJNs34HRere8FUGWNCwpn9frqzJ1sKeGnH9qq1B5ix9_4B8ihWwfQXsbErZEwgdU8qPqCepRQqg2Ee-6xF5VHiU-I2xlfuDz2E0WeFqp7tqQllaiJcL5-OhCsRf3RW6Dx7IBUsKierTA8yGyRyNT1HapxwlSwTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهر تایید ناسا بر انفجار مخازن ذخیرۀ سوخت ریاض
🔹
داده‌های جدید سامانۀ ماهواره‌ای ناسا وجود آتش‌سوزی در نزدیکی بخش شمالی فرودگاه ملک خالد ریاض را نشان می‌دهد؛ این تصاویر وجود آتش‌سوزی در نزدیکی بخش شمالی فرودگاه را تایید می‌کند.
🔸
سخنگوی نیروهای مسلح یمن سرتیپ…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/463024" target="_blank">📅 18:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463017">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/463017" target="_blank">📅 18:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463016">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۶.pdf</div>
  <div class="tg-doc-extra">2.7 MB</div>
</div>
<a href="https://t.me/farsna/463016" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۵.pdf</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/463016" target="_blank">📅 18:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463015">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/463015" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463014">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/463014" target="_blank">📅 17:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463013">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/463013" target="_blank">📅 17:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463012">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌ صدور حکم اخراج ۶ دانشجوی دانشگاه شریف به‌دلیل ایجاد آشوب
🔹
معاون دانشجویی دانشگاه شریف: در پروندۀ مربوط به ناآرامی‌های اسفندماه، مواردی مانند درگیری فیزیکی، ایجاد آشوب، حمل سلاح سرد، توهین به پرچم و برخی تخلفات فضای مجازی مورد بررسی قرار گرفته است.
🔹
در…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/463012" target="_blank">📅 17:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463011">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/463011" target="_blank">📅 17:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463009">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/463009" target="_blank">📅 17:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463008">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/463008" target="_blank">📅 16:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463000">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/463000" target="_blank">📅 16:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462999">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/462999" target="_blank">📅 16:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462998">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/462998" target="_blank">📅 16:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462997">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6pWnFZCuR47cGFdxP95jE1sWCnnWphY8hgRbWMMAAFF0qpFIVxA9SIvOW1YUdgQKDOwA_Sp9Y6iMnwyDIwSUJCd6sybrYRb6VyNKmU4--wWKY4Mt1UhN-CnMcObFdRzOVE5Sr9z9FKG6NUIgO6jxAMrO-qo9j0E1JXiVAX7WBSQIO9HT1JJeVh9SY19rsSMhByO5y5RUd7WCWDOgcDg03KFUkJEGcFJHIje32QlMzkwVmNDlqomwwovvJ-P-1TDl8Msr0aGUL3I8kHDshKnkIwtEKpydoh1_WA_xAN1DCR04w2mA_vcmI21Z3N8DELwrvetguYNlWrPOnEDob6egA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویری از بلندشدن دود از فرودگاه ریاض
🔹
برخی منابع گزارش کرده‌اند که ۲ مخزن سوخت آرامکو در شمال فرودگاه و ساختمان بخش بار فرودگاه هدف قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/462997" target="_blank">📅 16:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462995">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxuYh-7KfTgeibWYsKDqimvvS1Y7sTuDzfLltKZWTExLoOX5ybmITpLaSQRZXqDWM5Vce3b87RCwxCDuAsQVGfWYqACW4AK7vUWwGQRMC_UGjtT5B2JQWW9zZhDX3X08KSjGBWYOWEY48Tw5iW-hdeQ4t33lRHpOvyC9re_q_ajAVKIUFFTctQfdswmzBkjFcB6sVOIT3_ss-Q_f0NKdTS1QkRUArRURywijEBl8aAPUnjM68tzGYgUsym_3ZXWX-meIar5f6Cj_F2o0q_wYSKUKT6kUO1vMHWqsPopcCFtWSYL49786fD6E_1WYOzLJi-GjFLYGyGe1W5uXk-8mSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف پروازها در فرودگاه ریاض پس از برخورد پهپاد انتحاری
🔹
منابع خبری اعلام کردند که در پی نفوذ یک پهپاد انتحاری از سمت یمن به حریم هوایی عربستان، پروازها در فرودگاه بین‌المللی ریاض متوقف شده است.
🔹
هنوز جزئیات دقیقی از میزان خسارات احتمالی این حادثه منتشر…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/462995" target="_blank">📅 16:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462994">
<div class="tg-post-header">📌 پیام #75</div>
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
@Farsna
- Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/462994" target="_blank">📅 16:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462993">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMscYdwsZ4ewFIzUXb4V0ITr1YO1iQN7jywY8K3vMlZSrsYiqrjCkglWSCUJNIwGlieiuFg2Wtg1-dbUWQq7vexiuk1QvAPZW63C77fENaC0ainJw2OLMNpF7EIsoB5Z50axYMRPnZTIsrv5efvlWTIDaUVg4vXGS_tpgmzfSOpVCSaGfYHXZ0jK2Saa601ZRWKeu9Ak5uPgXZaXbT0jRH1j7JxrH-1hgWLabpyJ-6KtbimmUC-reHAolezEaDnZ0CHrMGvR2MQSRIVjglb1g3dowoVm5Npg0F0DO0oS8Dd61X6YTfcCmycml5pSMfKyz0gwHZLIrozFUMI5ZYDIig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویری از بلندشدن دود از فرودگاه ریاض
🔹
برخی منابع گزارش کرده‌اند که ۲ مخزن سوخت آرامکو در شمال فرودگاه و ساختمان بخش بار فرودگاه هدف قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/462993" target="_blank">📅 16:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462992">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/462992" target="_blank">📅 16:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462991">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/462991" target="_blank">📅 16:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462990">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/462990" target="_blank">📅 15:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462989">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/462989" target="_blank">📅 15:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462988">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/462988" target="_blank">📅 15:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462987">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/462987" target="_blank">📅 15:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462986">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">امتحانات نهایی در رصد پلیس فتا
🔹
رئیس پلیس فتا: همزمان با برگزاری امتحانات نهایی دانش‌آموزان موضوع تبلیغات فروش سوالات امتحان نهایی در کارگروه‌های ویژۀ عملیاتی پلیس سایبری کشور درحال رصد است و بیش از ۱۰ مورد برخورد انتظامی و قضایی با مرتکبان این جرایم صورت…</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/462986" target="_blank">📅 15:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462985">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/462985" target="_blank">📅 15:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462984">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📷
رزمایش ۳۱۳ هزار نفری جان‌فدا با حضور رئیس‌جمهور  عکس: دانیال همتی @Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/462984" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462983">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311e3e5dac.mp4?token=BM0cf00qqEOaHVfASqgkqpsvfmaaIcN66lOkPIhuYWs8LvEW5xHRsdDUeaK446KFP8JbJcFn_KNJW3mhktDoF4cRjW5ReEp5UL3_tctYYMOzPNEAhqIp4AY5IQdECU84vhBqsuyUcQWPt9cm5ZJXu3o7otiQBCVUjH9m30czGSj2J1uhUH4yqUGV9T2BX2Rh57p0B4cs96eNpG7sUSiz8QcwT7vb32rY3UnjgM-pyijOwr408yTlbeh0jytAFs9F4FXr-okNAMhR7yWoeAVKyVsMCwFeWAYu3wkttmcaSyreEeuVNgdm79A7V2tM7edy5uDosZIl6lMYz29JgYzMYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311e3e5dac.mp4?token=BM0cf00qqEOaHVfASqgkqpsvfmaaIcN66lOkPIhuYWs8LvEW5xHRsdDUeaK446KFP8JbJcFn_KNJW3mhktDoF4cRjW5ReEp5UL3_tctYYMOzPNEAhqIp4AY5IQdECU84vhBqsuyUcQWPt9cm5ZJXu3o7otiQBCVUjH9m30czGSj2J1uhUH4yqUGV9T2BX2Rh57p0B4cs96eNpG7sUSiz8QcwT7vb32rY3UnjgM-pyijOwr408yTlbeh0jytAFs9F4FXr-okNAMhR7yWoeAVKyVsMCwFeWAYu3wkttmcaSyreEeuVNgdm79A7V2tM7edy5uDosZIl6lMYz29JgYzMYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رسانه‌های عربی: پروازهای فرودگاه ملک خالد ریاض پس‌از اصابت پهپاد یمنی متوقف شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/462983" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462982">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvmwfQhaZsSpWGdZa6_FvtzPmDTChU58iFyzTxZrQkMPO2Lp7s9lPPtBe1dULqJ4m_7LZeSg800hETja_IPjlbJQmDtnxauzVE502zEBIij1foJxAnNoQ84tZfqMEFYyFmiXXHdG_d52UwMyuSSXaByLpnBd8Y3gT47O-d_5joZiT7jTnfK9biPIPLc6Rb3okujRjj1kq26V6wESJS10--fF-BV7t9RKVh__JNFp07I61MC8tNtTZFIBYMZhdcf28HjYs6z1UGv94rgUlCgRKx-awg66d9etWoGg6zj9NjT1ouWlBzi_ypMaZDnAUlrs6BNxBqkkUmVwtDxj1lJqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودروی خارجی وارد شود یا نه؟
🔹
امسال بیش از ۱.۵ میلیارد دلار ارز به واردات خودرو اختصاص یافته؛ رقمی معادل نیمی از ارز مصرف‌شده برای واردات دارو.
🔹
موافقان واردات می‌گویند با جلوگیری از واردات خودروهای خارجی ممکن است سرمایه قشر پردرآمد را به کشورهایی مانند…</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/462982" target="_blank">📅 14:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462981">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e0cd9dfe8.mp4?token=vSvhpL6fw9-GcMv8PMIBQGUo_kgHi_jdUjlurVVbkQzNM9RJleLNGUHBOLlTO3TrtbEamESPs3sIkp8KM_vm8HauSbFgsyqM3LBUq26u5o0u7hF3UvW36KYKtUgCBIKzqV3Y1pzDKZjeQcW4aVqNFvhfbYE4h9KnOAExeBCXUMW0eKgz_YFPlgw4VG54oCwNlndae1HN6MkWoLuAxc9iFt0qW17kaVotg0F-Cx4v1adj8s9260iucH29J9uKChcPpyMf_HBseFyKLSzvDIJ_xs87lNbHOSeJTa-h3ZKQPohB19skKsUR58zPl2WGDLzm6ql_lORKnuckvKo4b3WJAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e0cd9dfe8.mp4?token=vSvhpL6fw9-GcMv8PMIBQGUo_kgHi_jdUjlurVVbkQzNM9RJleLNGUHBOLlTO3TrtbEamESPs3sIkp8KM_vm8HauSbFgsyqM3LBUq26u5o0u7hF3UvW36KYKtUgCBIKzqV3Y1pzDKZjeQcW4aVqNFvhfbYE4h9KnOAExeBCXUMW0eKgz_YFPlgw4VG54oCwNlndae1HN6MkWoLuAxc9iFt0qW17kaVotg0F-Cx4v1adj8s9260iucH29J9uKChcPpyMf_HBseFyKLSzvDIJ_xs87lNbHOSeJTa-h3ZKQPohB19skKsUR58zPl2WGDLzm6ql_lORKnuckvKo4b3WJAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سال تحصیلی جدید دانشجویان آغاز شد  @Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/462981" target="_blank">📅 14:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462980">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II-Mc7hqv7BVtlLRiMXFgWqTpttLCa2OyQeZZaoUSU13OcMCs7w_hbHx4p1H_AA3UpttNyW360-OJoGp6UN6RysHx0TCl8nLfv3BwE5mRdx4k0hGzrGj9v8vcEYJIie2jz4tcCxaH1GJT5sE0g88r1wNULK8vkxOKGUjxg2munXAlAiOQzsePPxFLMMyZjM5BwP5HkiZF_v-ZTB4Bsixgqrz6IcMdZzpsuRodl-jLY4XlItdU-GfCpTp778j30roBAVFPwRLpF44zv5OkNYGXqwsaKydR_pjD-fl0bnbZvysyr7MR5Reac0oEbwK9dEKSoTiAZtJQlE4y_VZNqURMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب شهریور ایران از دلار نفتی سرریز شد
🔹
درآمد نفتی شهریورماه ایران از ۲.۵ میلیارد دلار گذر کرد. پیش از این در ۵ ماه ابتدایی سال بیش از ۱۳ میلیارد دلار از فروش نفت وارد کشور شده بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/462980" target="_blank">📅 14:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462979">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjj7GRADhvtAnC1-PAcQntqek8Qkmu-EaDtGmf-0H_8ggMXayIxhDSH9-FiJ5b4Z0jkzNfJXwVzmFyplsg3s5Iw3Sx3i2q86kc-VAIdrublkxgOAPP3sNLjbwLtbB7K4yNlTt5P45nDDSzF4XGD-9CrQLv08C9UFcXimhLB637sNdLDjrdyxjjPDdIa50KD7onZjjXF4pBLfJkiftcO2VYX-dy22zTwIDi8jlcsuVkUz1h2mx-YLWBRQR14eXx0sP6iwgwxjwcL_zefS35CXp8c3pdsV03jYPnMf39bSI3lfkfH2jsxv1JEt58n6vQlx2hy8Ewv-Ki7IOA80psPFtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی با انتشار تصویری از مشاهده آتش و برخاستن ستون بزرگی از دود در نزدیکی فرودگاه ملک خالد ریاض خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/462979" target="_blank">📅 14:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462974">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJkpTI33dxhst_FNp2dPrBqwD1O_39vPbXjBwuC3FzIgT1D5qrgtOTovYMv1RejYcxeVDFgTUkV6STFwSZUMAIBgrszd_93T40vfunxVMOaheWQqMak73--Eg8D4X5amQiLp-MZTrgbI-kKs7-8RR8l34v3Q2jthnHZqb4meOzH3W8SFfbRhTc1i_3E-G2WlzaS4ZAKtLoP5Av0WOIICL0qfRpM7eAJWfHJ3Xb2efuZ9tRczSHBlt_e4HnYDRCViwEkHeY6E2b53LWGCNYCMyxUTFi_A-BIl5UBbpGqduk5u_GZd5C1z60Ld7dSVGtYZX5tt-rekcNOGUOLaW_5LJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oyB0KEm2ztdAXbNyXCEmbgzs-K9LeQqdDz7jEIx1f4kyUC0ZVdQNmzyO1ebMGzI9h_FbHQtil1G913ZIbtxrPLy759-dKzdojm4XC7VjoJUKXc_n6WusY0Kt8BCGVuXschAypMYynymyy-PKDDuxWLr1AR1DyEIV9W1IP4ToTsURO8xOk9ZbgYUn_L3Bj39cJM_7y6QkYz7wCaWCcl58A_x3oTHYaAzg0wkN-rmf9n75LSayZYljcB-75BjF1xQh12aD8YDm1tOXhluhVU5Dd7QXln4M2MWUS-GtjM6_lZnlfdWUVMB13WssBbDKuRRDoNB16eRlMoDhfJY3zOqXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TheLsrTVJ_Xp9LHRxhtxBANdmuJ8Yqa3EYsOzK5DoUGWhCi622hEPLBhLkjbXMGli3NPAoebyYCJ6RddoNzmtk99Ga0mFegaM_8IVU6V-JVkJtFi5y7Sv2-2b7hZnTo6E6xzIFynV_8ZTOB2wDlo_wXR208ozv9R7z_oF_3Rs6-JUttPkV7wowvYcmja3tGHcGTDvqB0SD2WKTG9trhYIw-orSYJ8dWO3KXwV-qsTatWZ2eu3bAXxNvRTtMmug07z70Ygh91l4fRbZYH8Z11lQAzvWuzzyu4oVF1jwskfviOc6RbiXZBgDbkU5MKWrYBA55IGZLYc1ylUxczHAJkXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PPUfOMNfAnXVYlSa8RptY15IGkD8lRCqA6wyO67dO3L6ZjrdaWUwFxpQfydEVhTG2U8ldT8wZzZUfKmv0mblLL98QWO32K1NQf1xtds_GdtqgQylUdIxEeymiVni8Bm3ZjU6rzhM91_6dylcA_al97tFeENIJc-hi1k_RUQG-wKSpgVCk0wqnfjif5xH3ypDuElxoB5bFClKnYe8QvulI9iW8UEWCMnnKK-LgJlR1oLJsz50LDQFA7nwpLSiXgWPBpdLAw1Lhy2CyM_Y8D9Z40N8NvHg-te_CYnKk8x-Myde0RW9gD4ZYHd4vGGI1cU5AE9QJgQMtORS-dO7eKjvjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfHQ_77Fk0Q0pok4OkS4eOPgH0v2CziyAaGE6xbWI7V0DD-2C1dXCqDl80HYxXmmJ5AN8hdTdXSshhxSyxe6Iirg9luyuSVq1xbbbZSrHa5niM65w8UKnKyxksakeGkfDRTyJz21UjCW2BzCqzqoUDUZYnMoiOLtp4LRD4MRZ6slOIJbywR3oP2rS405yoUyvnr71Z27Hel2vgZXbWGhzMpofTvB4roNgA28ofniknzCLRBN8UdSjOHiL_jwtQYSj3p9nh6pyh3X9ka399jq0T9km6ee_b8MFh2T21ct-HctXCUfxm7pDx4gRbSheVM79RPDWCUeM4jSXECh4KOwtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نمایش اسبان اصیل ایران در رفسنجان
عکس:
مهدی امین‌زاده
@Farsna
....</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/462974" target="_blank">📅 14:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462973">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmakd1ARNF3St6vTihhQnJCHE8xXkS50kMTc-qNXW00OSPUlLDUy9g1D6OELoNuNqPDAiThqVLpGTL3z_ZK_nRwfFsfTvNEJOeKcChcQVqPtvgNdR6nlh0Krfanzhl-z2uVO6zwH3Nb4xzEwFz2TMZfVnhfnUUfjOx31TCiMlkrhWucz1sIUBsnlaDp5CnfcowN03Vjk0TOz9T9Nhsy1hUPQrCD-tGkXAbJeJO-_JzTLEdFQI4zXUsZ2dWY5qZqZ1AtCgLDYoiJ45s1IZU54czn3ppxM_T7A2xcfEZoUEqv0Ew9gkyalkhR1zNcRhv49RJS2JrOGDdECZYo7fcxhug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی با انتشار تصویری از مشاهده آتش و برخاستن ستون بزرگی از دود در نزدیکی فرودگاه ملک خالد ریاض خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/462973" target="_blank">📅 14:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462972">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52c0bd9395.mp4?token=roCBjlWvQRJseko6HiWHJooTTcA8EsfVLzjDDEUy-4zMv7OTN_kjhYPM17xElneB69bEQXurjMfy_cV7UvwBKuFrPhNNbkquJ1ubatnbDzC_v0kGRoGWSVfv-9GbKEJHzj3Ki28qzEvWLeSiUsycBF2Mtqht5eEe42inkjGTVjpTaQ0O1Ln8L0D5z3gTuoGiYBVeE8nriTeMp-tcfb3BGaJSOfn96mE8BlDtJ_qRlcvfD2p3tCVVxvAo1k3tZDFj3hqJ6L1iMBk5eNpxe4py6j6hHulMdU50SbyOuDWitIuMLivlhzVMUM62fmXpjDIZTDYR7AUa5vkZL4bMFQ0UQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52c0bd9395.mp4?token=roCBjlWvQRJseko6HiWHJooTTcA8EsfVLzjDDEUy-4zMv7OTN_kjhYPM17xElneB69bEQXurjMfy_cV7UvwBKuFrPhNNbkquJ1ubatnbDzC_v0kGRoGWSVfv-9GbKEJHzj3Ki28qzEvWLeSiUsycBF2Mtqht5eEe42inkjGTVjpTaQ0O1Ln8L0D5z3gTuoGiYBVeE8nriTeMp-tcfb3BGaJSOfn96mE8BlDtJ_qRlcvfD2p3tCVVxvAo1k3tZDFj3hqJ6L1iMBk5eNpxe4py6j6hHulMdU50SbyOuDWitIuMLivlhzVMUM62fmXpjDIZTDYR7AUa5vkZL4bMFQ0UQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعدام خائنی که اطلاعات سایت‌های موشکی اصفهان را در اختیار موساد قرار می‌داد
🔹
حسین پدران، فرزند حمیدرضا که اطلاعات سایت‌های نظامی حساس کشور در استان اصفهان را در اختیار موساد قرار داده بود، به جرم جاسوسی و همکاری اطلاعاتی به نفع رژیم صهیونیستی بازداشت و محاکمه…</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/462972" target="_blank">📅 14:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462971">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6bfc600a.mp4?token=o9aT-JXojQkLlPUmGfh94VTz2ZI00odVSVIydgPULIGnFm79vgjh2cr3IaSlRglJNOQrExoW2KysLts2SauzN4pMg2TJSpkIQtOp_Kh5SHVcVjk5ZNE3WEQFH914HTZGvif7awIYumlUY0h8IXoMLMEFftjgPrOhkQalbppwIUIkkyKsZ_yrGHstFFm8gzo0v3K4ZMIkw2JmDYQkbqH1Q2vou2xcLBioxJMWnXpMpBINWYOH6W80Vx7XJu4h1WbE-ftTmMMlWjhCK0KFQcPql00oh_EzjxQJ6HC4Uku4slpWs5OWMiYdyNz-xOhCoXAlOuZ-xkeKjvC_UJ5YQ9UJvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6bfc600a.mp4?token=o9aT-JXojQkLlPUmGfh94VTz2ZI00odVSVIydgPULIGnFm79vgjh2cr3IaSlRglJNOQrExoW2KysLts2SauzN4pMg2TJSpkIQtOp_Kh5SHVcVjk5ZNE3WEQFH914HTZGvif7awIYumlUY0h8IXoMLMEFftjgPrOhkQalbppwIUIkkyKsZ_yrGHstFFm8gzo0v3K4ZMIkw2JmDYQkbqH1Q2vou2xcLBioxJMWnXpMpBINWYOH6W80Vx7XJu4h1WbE-ftTmMMlWjhCK0KFQcPql00oh_EzjxQJ6HC4Uku4slpWs5OWMiYdyNz-xOhCoXAlOuZ-xkeKjvC_UJ5YQ9UJvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سال تحصیلی جدید دانشجویان آغاز شد
@Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/462971" target="_blank">📅 14:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462965">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBUizdV3XFNDc-AMzKA2jKOiLyXfCFebc25ceADaqryjSQSFqfkpv342draSKRgAIeQGHP14nwUPafVYiVMvir8UfsupqqH-NYnANed9RBc1Iboy7ohvL27WmHWncpTaepUoZ_VlQHLJc9fwsp6NG35HxZtm9TDJqa42ZsetJtXMvKLOVwE7vnfoADbwQh9353YwvY-OWPd7yIRUs8ZTvigTY8yqV6MKuPLPw18OGe7ceUSHQ14zNMui8iJuvwV1WWIuqLwiqaOUtvvTySfEjPgYAnwrqguw6pXG-83VEuZXu4UcyEBSlFAQIq4tsHLB1D570nUQXSowHrFOkzcmWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWwe8gzQVvYYCmyxpl_L5Z9hYtAAVs-V5hLXC-M4yiGT84FXFyLVSsBFOmvip9zIM_Ddz2Scw0-XIJtYZ-TqtABzIjA-u7BYrO7Lk1cUqvpDxgnNdIs269uFNIawNtzqEhX4MAglT8Dwa-FbSihTNm4uo3Kc4a9N1KUflWUJZBU_wPRFggUH3CV1o5ZdRQvD_nQZb6FgMz_xckO70_Pwgu7SNY2AQICTg0SMG5Wixup25VnDFkZlYAQxCq9Af62DC8CRqsBD_SLKcK7R0yuUB0nHDQvaigSE_KrP7GU4doc57nseXyVN3kJ5VUdWNugeUbphYRU9-vI5rDjDZqRCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWL78tYpNJuJiFfTVxe2GkDogmXqt2KlRWq7HilTTNilM4OpdvMGtFYVJHP1LE6tUeYVM6AujKxkrNsbhAntICNPIZsY7CAsfDlcY8xRZmFh8di6tNfZoZ0sjnxSENZPy_xQQu3DebOVrveg1-RBQxtiVh81gDKr1YNVstE1EXb15HcxJa4OXeMaMgGTnF0y3KpiNO_AlGDbP7ZAu3XnM08l0FfhGiutnSh30u3wNosqZU-nU1d2iKZm_b-T0UFC6TCqe4wLQdAM4hrS6aM1E15BbHaVYjn12dD3T9NR6uaGqq2Py3EoZrno6jztPTCH8EqdWF7IGCkp5LPVFYuOkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBi02-UllATIjl13w-CJfyiu2RHfiQh23H7vl8l1kvvKk-wSVjYDvCZf9yImD62LH-I8IbFt5k1yVmt671NarnTJkRJxE7Bb2h6RbGasj51IHYRYhfS-IiGzj5XExNced2j0LjyMLHYSbdTVHZsvDBITAo0eJyQHQpr-xGbX6OzwGy91Fsc8bMLvirC26xd7fX0nOi0n7pkO2srIgljIjffiGIe1r6-I7e4oPhtU-7TdmPgppPLcKHE4iFWBt8NhrqY94ZR4xUOl8YNhZehgL3WpH5WTkans1xh29_7ucQ9PXZDhPSblTFCalxG9wb4RkFSOo1hpSbK4FlP4R3FRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNLWYz0cCkHyBXD9hfFeA1Y3-Pfo26aJRwMlJJcsFmm2vLQkKqYjEDUDYRnRon_UCjowgj09RCMJM9eSCLLCEemYM1JwbLyIhCjMEpJ0smiOQAqir2ir6A54T0fsd647FFBDkzHzrCrVDn1hyWt5jFSGvQoVn_QymVAbdaRqMEZd4S5gp_TGbb4OV_sqc1PdKm3SXAKgUQAU-FDuQ3fZetJtpQyP3hsDalGec4gNoDrKb7cz48fgJcq6T6rnYlIdAUYH60E5Sb7Zry_rQILAZqkGVPfFEEYFGu_JWlZMO3RcvjgsrgqOGEKmtEVYmBbjECr2bvFHILKhK9h7zXz2qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxEgr6GX9XNYB7sbuHyEP-H6TVS3v7mdeCJUgkuFmlf5_FnStLWr9sbdZzWe0ceCrwrsX-2KcfViXECaxsuXbroo5B7GXjXKFZjAtKkiZFs3uFKzMymx9f7WVUZMQY1vUQ7u2zFeXYFTF-5eJKgwg3qZ29wV1qL4rZgcYrr_41AFYCCc6aLjgIvQEgQhVEBu92E6y6ctofDfklbtcW5SW9uW1g-HMI5I_cu--135WXzdu2098TFfL1BohsvMR57ED3ZCwIddBrFDkG24g9Y4DDeqXDgQnz0SqHaY65fVnLCDpR89XSJwFY4hpCAW-iQrICasoQTk2Jz4WaHx2nohvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
صحبت‌های جالب در مورد معرفی کاروان ایران توسط سخنگوی ورزشگاه
🔹
دائم گوش می‌دهم ببینم دیگر کشورها را مانند ایران معرفی می‌کند یا نه! گویندۀ ژاپنی کلا سکوت کرده.
🔹
بالاخره احتیاج به نفت دارند؛ اقتصاد را هیچ‌وقت دست‌کم نگیر.  @Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/462965" target="_blank">📅 13:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462964">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2a09ef29.mp4?token=U8_1b5f9-dwROFYayiFiJCgAAdHUSpkpttEupIkPC4Tox1uOeRv9SxNbvnq0epmiAcBmL_WukD1RGlnLVrwFS-JUf8_CX-Eb2QdOVNH1fq-1nn1nlPuGXLso-sVyS2PeJLb9cT8TlTPteKF0hkaExnGo7UcHzEs_aUG-6O295Bq5HhgLzc_3vgLH1L68OOzYYGhHjJnYvGht35nrtPBZroqymmi42UeUIILN6RcFV8LD6M7AvL70aM9VU7yttG45eMjB45207BBDdAlkW6c-Ne7mtDX3hvUesILvlWFImfYPA5wmcaoVSDEgCKL2FUnpwKsPL3w9Ph7j_lXSSknkFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2a09ef29.mp4?token=U8_1b5f9-dwROFYayiFiJCgAAdHUSpkpttEupIkPC4Tox1uOeRv9SxNbvnq0epmiAcBmL_WukD1RGlnLVrwFS-JUf8_CX-Eb2QdOVNH1fq-1nn1nlPuGXLso-sVyS2PeJLb9cT8TlTPteKF0hkaExnGo7UcHzEs_aUG-6O295Bq5HhgLzc_3vgLH1L68OOzYYGhHjJnYvGht35nrtPBZroqymmi42UeUIILN6RcFV8LD6M7AvL70aM9VU7yttG45eMjB45207BBDdAlkW6c-Ne7mtDX3hvUesILvlWFImfYPA5wmcaoVSDEgCKL2FUnpwKsPL3w9Ph7j_lXSSknkFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار کارگر: تجهیزات باقی‌مانده از حملۀ ناموفق آمریکا در دشت مهیار اصفهان در موزه‌های بنیاد دفاع مقدس به نمایش گذاشته می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/462964" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462963">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGRscFzC61SUUpqKVOslJ5ddtfUqt6jglPlHSYdhYC6m_aIbcXCTs9LcjkbhZAL_5COEOhu5KAEtl25NAj5kfwG2t_UrSLpVd-yadxcneZR30F1EAoKcEuAoGIyxRlireplGoVEM2PTWxMDCkpFZl5fCM4Fjg7Csxrvf0UzgaLIyTiVtDx_wtj_d59yCJCNSYxW0V4lHusAtHXIrPRc57HUOVu_sgKZgQ8TFeh8-lRo_tU-Lt3Mdk-uhH8K63A8SrjETeObBXJa7gvoRB7FxWqu6BUGTZVMouQd5lEMW1suPItZu3Mesf_GD-ICka3_QiA1kJM_QB1RwgfmjiSsTrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست یاری پلتفرم‌ها به سمت رئیس جمهور برای فرار از نظارت
🔹
پلتفرم‌ها در نامه‌ای به رئیس‌جمهور، با انتقاد از نظارت ساترا و آنچه «نظارت بی‌ضابطه» می‌خوانند، خواستار انتقال مسئولیت تنظیم‌گری شبکه نمایش خانگی از ساترا به وزارت ارشاد شده‌اند؛ وزارتخانه‌ای که خود به‌نوعی ذی‌نفع این حوزه است و رئیس ساترا نیز پیش‌تر از «ترک فعل» این وزارتخانه سخن گفته است.
🔹
روابط مثلثی، کپی‌برداری از آثار ترکیه‌ای، رقص، مشروب‌خواری، روابط آزاد، کمرنگ‌شدن قاعده ازدواج و چیدن مسیر دوستی، نمایش خانواده‌هایی با بنیان خیانت، خیانت مرد به زن و اخیراً زن به مرد و... همه اینها بخشی از محصولاتی است که شبکه نمایش خانگی در سال‌های اخیر به مخاطب عرضه کرده است.
🔹
حالا نامه‌ای با امضای نماوا، فیلیمو، فیلم‌نت و... خطاب به رئیس‌جمهور منتشر شده که در آن، این پلتفرم‌ها خواستار بازگشت تنظیم‌گری شبکه نمایش خانگی به وزارت ارشاد شده‌اند؛ همان وزارتخانه‌ای که بنا بر اظهارات جواد رمضان‌نژاد، رئیس سازمان ساترا، در این حوزه «ترک فعل» داشته است.
@Farsnart
_
link</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/462963" target="_blank">📅 13:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462962">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f11843d50.mp4?token=JQaiLnPZUXo8pyNTEb6tIwYLpDlJDjaLCyeZ3BingrhJef0JfgAUCfkOclKNJodTd7S6uqaHFH-AWpO10YGio6Op8uOupFibKGUfA5upNZVDiHfv1YOif4ptuOl2Eq5I5o0KPIT3V6yMGx9chZZAMDB2hHgKMowRWjBL_mkc-V3ggGc045_Cjz_40HfUcw1uYeacrmAXAzl02MLV4uMvt1FfGsTVIO8dAygp2smdG59wJWg5zdwwSVkpcpXxqWxguy3E8ihf2viU0-AcMQA0JmJ-l2D_Pn_HDyKb9E-fvtfeaRl35nAJVJVPdNSHFDU87qL1aDGptq1j_plBWjX5rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f11843d50.mp4?token=JQaiLnPZUXo8pyNTEb6tIwYLpDlJDjaLCyeZ3BingrhJef0JfgAUCfkOclKNJodTd7S6uqaHFH-AWpO10YGio6Op8uOupFibKGUfA5upNZVDiHfv1YOif4ptuOl2Eq5I5o0KPIT3V6yMGx9chZZAMDB2hHgKMowRWjBL_mkc-V3ggGc045_Cjz_40HfUcw1uYeacrmAXAzl02MLV4uMvt1FfGsTVIO8dAygp2smdG59wJWg5zdwwSVkpcpXxqWxguy3E8ihf2viU0-AcMQA0JmJ-l2D_Pn_HDyKb9E-fvtfeaRl35nAJVJVPdNSHFDU87qL1aDGptq1j_plBWjX5rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژۀ کاروان میناب ۱۶۸ ایران در افتتاحیۀ بازی‌های آسیایی ناگویا
🔹
شور و هیجان گویندۀ ورزشگاه هنگام ورود کاروان ایران به محل برگزاری رژه  @Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/462962" target="_blank">📅 13:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462961">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4XXXXSCES6zAPt5uD94EXTtob7jHFx1DANKJQP1KCggDO5-PSAlH7p6fc9xun00CI0Xp0nyGM5Cr744ReGPibpQ2mp75PAkiq9tGOdOWiGk-48IJUsKnw0Jf3l_5KzEw3Ce7v11LlERms0Qe7JdNnv2p98BtgrSzQmxT1aylRGd6bfQjhWbMl2nKIDp7jENxJq1bCvOZ-vuWhParJ_WYneg-zIpY0WHS-4APijVzme3TJkS6rtzMZVENj7iQtSC5WQT5Y4vC2RdCEMrWXspiHq_hRULPAXLXTigyws6ZTmb2ckCoe7ywGzKYK6SogfEF14Xvm-djrwEIITLmTRo8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کره‌شمالی در واکنش به آژانس انرژی اتمی: ما یک قدرت اتمی برگشت‌ناپذیر هستیم!
🔹
وزارت خارجهٔ کره‌شمالی در واکنش به قطعنامهٔ آژانس بین‌المللی انرژی اتمی که از برنامهٔ تسلیحات اتمی پیونگ‌یانگ انتقاد کرده، اعلام کرد: جایگاه کره‌شمالی به‌‌عنوان یک قدرت اتمی «برگشت‌ناپذیر» است و این جایگاه به‌پشتوانهٔ بازدارندگی هسته‌ای حفظ خواهد شد.
🔹
همچنین خواهر رهبر کره‌شمالی در بیانیه‌ای آژانس بین‌المللی انرژی اتمی را به داشتن «استانداردهای دوگانه» متهم و اعلام کرد: دیدگاه جانبدارانه و استانداردهای دوگانهٔ آژانس بین‌المللی انرژی اتمی، عامل اساسی فروپاشی نظام بین‌المللی منع اشاعهٔ هسته‌ای است.
🔹
در بیانیهٔ کیم یو جونگ آمده: آژانس بین‌المللی انرژی اتمی در برابر فعالیت‌های آشکار اشاعهٔ هسته‌ای آمریکا و طرح کره‌جنوبی برای واردکردن زیردریایی هسته‌ای چشم‌پوشی کرده، اما در مقابل، قطعنامه‌ای را علیه فعالیت‌های هسته‌ای دفاعی و مشروع کره‌شمالی به‌طور اجباری به تصویب رسانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/462961" target="_blank">📅 13:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462960">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8aa05441.mp4?token=Eprs0xv-mr7m3_KEsJVYW_AEUm_-v9F5Y7tSSNR2JhIfA-ZmmstHePXSC2xE88fAtD4yeg2ToFvM3VBSk4rtmx4A8IYQGNlxmlDxP237326hSYmZnj_vdndsQA1IHHOoGiam4vBXUBA_v2C_fCZNWtnjM2NC5oYJcXer7Ocd_L34UnrNm06kPwYc-TmXX9ukEGRqH5BuEi575fobZI_lQrOsT5mxSvhELh7Ta2lMpk9g8WR0J3IXtc4PSomcsdg37qgsYnNWq4PmCiDA7g86V2gi-Sm6ckkYdvTcPkqV9rvjlSZponbNhCqMPvqpiQti7wjgCPyPBp7WvGLYVOK5sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8aa05441.mp4?token=Eprs0xv-mr7m3_KEsJVYW_AEUm_-v9F5Y7tSSNR2JhIfA-ZmmstHePXSC2xE88fAtD4yeg2ToFvM3VBSk4rtmx4A8IYQGNlxmlDxP237326hSYmZnj_vdndsQA1IHHOoGiam4vBXUBA_v2C_fCZNWtnjM2NC5oYJcXer7Ocd_L34UnrNm06kPwYc-TmXX9ukEGRqH5BuEi575fobZI_lQrOsT5mxSvhELh7Ta2lMpk9g8WR0J3IXtc4PSomcsdg37qgsYnNWq4PmCiDA7g86V2gi-Sm6ckkYdvTcPkqV9rvjlSZponbNhCqMPvqpiQti7wjgCPyPBp7WvGLYVOK5sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیگنال تازه در نقشه‌های بارانی ایران
🔹
نقشه‌های هواشناسی امروز نشان می‌دهد شمال، شمال‌شرق و ارتفاعات کشور همچنان مستعد ناپایداری و رگبارهای محلی هستند، درحالی‌که مرکز، جنوب و جنوب‌غرب بیشتر تحت تأثیر هوای گرم و پایدار قرار دارند.
🔹
در شمال‌غرب، سواحل خزر و…</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/462960" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462959">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3445e3d598.mp4?token=OFOtdrfJcJRJz_rlxHW0mjhzTv0lgjVFw2pokIKcrum0fbNEGcTuMXsQ8cwuSSBrWJkrM-L9YJk6weSZYjqSrQqoGcqgbS4HYzh9StilBtVI2Q8g8HonHI8IoV5cGlPkmCYC0_Urtam-qi7-jh4yACZYT-2O4pb4oHqLakNBzW6tt8Ps9x7TDMWv6_bZ41jXDdKuY9cucdu6BVcKNvERDVXmnrVhIiziKuQfjqvN4Jfrw3QfBiHyBc746s5-uam72hm8RXr2UpO0KSzhaF2fW1EIwcBwAoB3g-3G-oUgXHo5qcX3rgyu_SAjEqZ5BSogi8x7tMPe-cuD-QRvqwMKcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3445e3d598.mp4?token=OFOtdrfJcJRJz_rlxHW0mjhzTv0lgjVFw2pokIKcrum0fbNEGcTuMXsQ8cwuSSBrWJkrM-L9YJk6weSZYjqSrQqoGcqgbS4HYzh9StilBtVI2Q8g8HonHI8IoV5cGlPkmCYC0_Urtam-qi7-jh4yACZYT-2O4pb4oHqLakNBzW6tt8Ps9x7TDMWv6_bZ41jXDdKuY9cucdu6BVcKNvERDVXmnrVhIiziKuQfjqvN4Jfrw3QfBiHyBc746s5-uam72hm8RXr2UpO0KSzhaF2fW1EIwcBwAoB3g-3G-oUgXHo5qcX3rgyu_SAjEqZ5BSogi8x7tMPe-cuD-QRvqwMKcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم افتتاحیۀ بازی‌های آسیایی ۲۰۲۶ در ورزشگاه میزوهو شهر ناگوی ژاپن  @Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/462959" target="_blank">📅 13:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462958">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromصبا فولاد خلیج فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kavy3C4JcXGqRyt5V-O2KzE3cweHofBhjKhFeOj5uWtU2om5OHRY2-kPl6gxpy4O-XNK-qYMkdg5f7vP050opcqKtfd_8QQneWeaPmyZwgSmZ4wOSpC938fVxcUSC6J49we5UI1xSUF36e1obaS04_0JbuyXocB4m4uiRADDtbgi0ID7CBmynAbUL7FjWSRweamvqIrg8neIMQVtvEd21wjIih_rItEDP_P8_cyUcc1tf16xM0VVzjAoILbY82-jtUN3SiLV4cv5lJG4tLKgEYC-r-KaCM0mY7DsxoAehp-X2sBa6RahYhvvxtZvLR0iZM1nukUDAg4Pl6bLgbSWnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خون تازه در رگ‌های سهامداران صبافولاد خلیج‌فارس
صبا فولاد خلیج فارس در پنج‌ماهه ۱۴۰۵ با جهش فروش داخلی و بین‌المللی، افزایش درآمد و رشد شاخص‌های بورسی، تصویری متفاوت از عملکرد خود ارائه کرده؛ روندی که برای سهامداران، نشانه‌هایی از بازگشت رونق است.</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/462958" target="_blank">📅 13:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462957">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPkQ1vVdlecu4zGLwsnVqlCKvBsoTq7StBdWmMp6kMjcIubqizDBoalBG7ZHVB6mr9X31GAfVtRbPJ7afxNqy6UF8GGAYk6F0lrAozGheXAnenYNpCBmqbq-cNxt7FY-rnuyxJ30EkVdLwiCjdFUohCcRddrapBtss9qCKSddAno9K18ZweXy0qxnIEuBi1DgpBLCiSMJnWuIwJCtx-qDbSV_GZ28ghg-_iKOaqWGApvM2z8tbzJAHo_SRcdozwZdHZwaN7kgfIrM6U-2VF-COKQDf1ae9DShBCdxYJNF31Gagj6Xb7ypwavn3OC22gtjogsQmtvZ2DleCBlP8cY9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
یکشنبه‌ها در پارک آبی اُپارک، بازی‌های گروهی منتظر شماست!
در سانس بانوان، در کنار آب‌بازی و تفریحات اُپارک، در بازی‌های گروهی شرکت کنید، با دوستانتان رقابت کنید و شانس برنده شدن هدیه‌های ویژه را داشته باشید.
🎁
🏆
🎟
برای خرید بلیت به سایت اُپارک مراجعه کنید</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/462957" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462956">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/462956" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462954">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786c37f584.mp4?token=eMcCe7TUN4u1vMbhpVHEJuQRXB6UeMAmNs8uJxaAGuOJ584LDdoOoBlL2QXNMNcF7eMwBTXfvpOhERI7CdNqh0AiOgs0_s36z3gnb_WQgqSsEdQBdR_Pb6rl1Pci8xgeqWSAnvjesBDdMO6zYhCJuJxFDUobdwZvDlhIiW1-WcGw1LGRy28zVC0-dj5o2eIaFVgEOO5SMIByxLXajDcsInA5XRyHcmaQSg6JPJL3lt5kOUvf9pUHHgCRF2z6eVMQJ_VapFztgTf_sNLaFkQe47JIRmzVGgQ-mMvvz4hY19_V4z4SfRW7Id1Oba7fi6wKhtfLN0rURuBJlIpXflsEzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786c37f584.mp4?token=eMcCe7TUN4u1vMbhpVHEJuQRXB6UeMAmNs8uJxaAGuOJ584LDdoOoBlL2QXNMNcF7eMwBTXfvpOhERI7CdNqh0AiOgs0_s36z3gnb_WQgqSsEdQBdR_Pb6rl1Pci8xgeqWSAnvjesBDdMO6zYhCJuJxFDUobdwZvDlhIiW1-WcGw1LGRy28zVC0-dj5o2eIaFVgEOO5SMIByxLXajDcsInA5XRyHcmaQSg6JPJL3lt5kOUvf9pUHHgCRF2z6eVMQJ_VapFztgTf_sNLaFkQe47JIRmzVGgQ-mMvvz4hY19_V4z4SfRW7Id1Oba7fi6wKhtfLN0rURuBJlIpXflsEzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم افتتاحیۀ بازی‌های آسیایی ۲۰۲۶ در ورزشگاه میزوهو شهر ناگوی ژاپن
@Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/462954" target="_blank">📅 12:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462951">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjSCHkuTgKHXH2LUIkCVeTw6s6pBBx_EeXbjRPuKkYhnnA2o5mB5hr7mRpU2jcU5OMwJU_efaD_WdV6jSoBIkZuWU3G27b37O49Fj77dh_vkGhAJypnYr9bcfVUauQgA5vZfNNKzfGkfUZtVOY1ydAGTk-S5hkJ6Zqzxr7f6oYF7n0wuLbmAIt-irjVPQxUS1ojlrIuLtZlpOLTxzrlAs4qGw6AtwDut8Ot65yUYHmC2oplNCu6Bw7RHfUGI34ClQBQ_mLdIOF_KWBVA34aWYaujGF6hisXq1ihhCLapXOXoLlii0lmQo8lf1lCAXDYR_GOSsJ0xKaSw6nqauQPAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریزش بورس به زیر ۷.۵ میلیون
🔹
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۰۹ هزار واحدی به ۷ میلیون و ۴۴۹ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/462951" target="_blank">📅 12:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462950">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آیت‌الله سیدموسی شبیری زنجانی به‌دلیل عارضۀ خونریزی معده در بخش مراقبت‌های ویژۀ بیمارستان بستری شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/462950" target="_blank">📅 12:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462949">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNFsaCXz3yimVGDpfQvUbLHXQpetPE5CbTBNYZdk6T9I0PVoOvBiswRQaulAIqS6RJtgfeCWQ2nTLgAnilHcqNfWTRh3pJMgZZ0wUoxednvHAIpH60iqlvD5q-jxRW7PxzbixbKIew60X8uwN8IcMk9n6EQTKZQiiE8JWxK89Q9Pr5FUVGdMMC6LsL9QDCKqJ_QY2WOnlvb4Jbwie3FaLZyLNzd1JMYnE5Fojwv1w_LrVT4ojzULOO7gCd4_5hK1CDU0vzVAjb9o1hVCUg3iOIq0DtkEivx7aAuIs72L-HG-Grf5xyjbJZ-7eDDAbMKfWsvNMW464ZwcM_ARg_J4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز دور جدید ثبت‌نام عتبات
🔹
ثبت‌نام دور جدید عتبات از امروز برای اعزام تا نیمۀ مهر باز شد و زائران می‌توانند بسته‌های کمتر از یک هفته، یک‌هفته‌ای و بیشتر را انتخاب کنند و زمینی یا هوایی راهی کربلا شوند.
🔹
با وجود احتمال افزایش هزینۀ سفر عتبات در پی نوسان نرخ ارز، زائران تا نیمۀ مهر می‌توانند با همان نرخ قبلی راهی کربلا شوند.
🔹
دور قبلی متوسط هزینۀ سفر زمینی ۳۰ میلیون و هوایی نیز حدود ۶۰ میلیون تومان بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/462949" target="_blank">📅 12:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462948">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نفت فیزیکی ۱۳۰ دلار شد
🔹
اطلاعات رسیده به فارس از یکی صادرکنندگان فرآورده‌های نفتی حاکی از آن است که با ادامۀ اختلال در تردد نفتکش‌ها در منطقه و کاهش شدید جریان نفت از تنگۀ هرمز، قیمت نفت فیزیکی اکنون به بالای ۱۳۰ دلار در هر بشکه رسیده است.
🔹
انتظار تورمی در بازار محصولات پتروشیمی که پیش‌تر با کاهش واردات نفت چین مطرح شده بود، تا ماه گذشته با کاهش ۲ تا ۳ میلیون بشکه‌ای واردات نفت این کشور تقویت شده است؛ به‌طوری‌که واردات نفت چین از ۱۱.۴ میلیون بشکه به حدود ۸ تا ۸.۵ میلیون بشکه در روز رسید.
🔹
همچنین براساس این اطلاعات، جریان نفت عبوری از تنگه هرمز از میانگین ۲۱.۶ میلیون بشکه در روز در پایان سال ۲۰۲۵ به حدود ۴.۹ میلیون بشکه در روز در سه‌ماهه دوم ۲۰۲۶ رسیده که به معنای کاهش حدود ۷۷ درصدی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/462948" target="_blank">📅 12:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462947">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjBNeVnez6lYeVKmF9ikW69Sth1oDixkMHnX9V5QgyHwSswZijpJOl2Medx4v9ai7sVcZc7LOzFZWcqkfa2hm6wHWhrNyzfvIau3dsIi9RZ-mbANlO9bcmpeRh76Bu6Jc3bREc-cSselfwY2l8GvvejUPYQb1ONgJ2IK6nYG3loXWcKQ6OUBzlm_FkaBa2G_ozt6K2iY2p83JXGG7F54wec81Xn1Bi9-yHVwQ3_l7shTmaVHHUoNl7vLUGzzm_uG6x-6J0_-GIpIixs_ebUz3p4_PXuBCFGrRJm9IcLAYW5FpIyIgcBn63hJ3ZDVDbFMkIIyrcHLZQBnRxHADvzmKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیگنال تازه در نقشه‌های بارانی ایران
🔹
نقشه‌های هواشناسی امروز نشان می‌دهد شمال، شمال‌شرق و ارتفاعات کشور همچنان مستعد ناپایداری و رگبارهای محلی هستند، درحالی‌که مرکز، جنوب و جنوب‌غرب بیشتر تحت تأثیر هوای گرم و پایدار قرار دارند.
🔹
در شمال‌غرب، سواحل خزر و دامنه‌های البرز، رطوبت و شرایط همرفتی می‌تواند باعث افزایش ابر، رگبار و رعدوبرق محلی شود. این بارش‌ها بیشتر نقطه‌ای هستند و لزوماً تمام استان را درگیر نمی‌کنند.
🔹
در شمال‌شرق نیز ارتفاعات خراسان‌شمالی و رضوی و در جنوب‌شرق، بخش‌هایی از جنوب کرمان، شرق هرمزگان و سیستان‌وبلوچستان مستعد رگبار و رعدوبرق محلی در ساعات بعدازظهر و اوایل شب هستند.
🔹
در مقابل اصفهان، یزد، قم، سمنان، فارس، بوشهر و خوزستان همچنان هوای گرم و خشک خواهند داشت و در مناطق بیابانی احتمال گردوخاک وجود دارد. تهران نیز عمدتاً پایدار است، هرچند ارتفاعات البرز می‌تواند با افزایش ابر و ناپایداری محلی همراه باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/462947" target="_blank">📅 12:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462944">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/462944" target="_blank">📅 12:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462943">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c05b437b.mp4?token=p8S9VKoxfL-h3dG9ohBBoMAc9J2h95aUfC6jWQx3MincNqDxx0UmklU1EE80VDEtDlPoBuQOnYfNsLSEq_52iBY4cXmDtm5lDWV-7VvTyQOGFnk2Rm1uwS11ZSeS9K8TGuNJeg6pEEG3-A-HyQTcWqaGp_cZOCpq-g7WRSPn_gVKfSqdpwPPxUGyKZYypwoNd7jHJdIGmYg7i2oaiAfz89HNkT1CKXu_kIzV2YpNUsMBhifkN77OGhSP9Q3PLxSzSYisEJ1y393oxrSrTElqgHIxCWz31P_cAJ9NOZnND3Kt_ipaXbyhDl6a5wNImsGEI7AsaK_HplW9BNOA7XvHmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c05b437b.mp4?token=p8S9VKoxfL-h3dG9ohBBoMAc9J2h95aUfC6jWQx3MincNqDxx0UmklU1EE80VDEtDlPoBuQOnYfNsLSEq_52iBY4cXmDtm5lDWV-7VvTyQOGFnk2Rm1uwS11ZSeS9K8TGuNJeg6pEEG3-A-HyQTcWqaGp_cZOCpq-g7WRSPn_gVKfSqdpwPPxUGyKZYypwoNd7jHJdIGmYg7i2oaiAfz89HNkT1CKXu_kIzV2YpNUsMBhifkN77OGhSP9Q3PLxSzSYisEJ1y393oxrSrTElqgHIxCWz31P_cAJ9NOZnND3Kt_ipaXbyhDl6a5wNImsGEI7AsaK_HplW9BNOA7XvHmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ صدور کیفرخواست در پروندهٔ شهادت رهبر انقلاب و اعضای خانوادهٔ ایشان و اقدام تروریستی منتهی به شهادت دانش‌آموزان مدرسهٔ میناب
🔹
دادستان تهران: کیفرخواست پروندهٔ اقدام تروریستی منتهی به شهادت رهبر انقلاب و ۴ نفر از اعضای خانوادهٔ ایشان با تکمیل تحقیقات مقدماتی…</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/462943" target="_blank">📅 12:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462942">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پشت صف‌های بلیت قطار چه خبر است؟
🔹
پیش‌فروش بلیت قطارهای یکم تا سی‌ام مهرماه از امروز آغاز شد و بلیت مسیرهای مختلف از طریق اینترنت و مراکز مجاز فروش عرضه می‌شود.
🔹
مدیرعامل راه‌آهن گفته برای پاسخ‌گویی به تقاضای موجود، سالانه به ورود ۳۰۰ واگن مسافری نیاز است و تا پایان برنامۀ هفتم باید حدود ۱۲۰۰ واگن به ناوگان اضافه شود.
🔹
در مسیر تهران–مشهد نیز با وجود فعالیت ۸۲ رام قطار، ظرفیت این محور به سقف خود نزدیک شده است. راه‌آهن برای تأمین فوری ۳۰۰ واگن مسافری از محل تهاتر نفت مجوز گرفته است.
🔹
از سوی دیگر ضریب آماده‌به‌کاری لکوموتیوها حدود ۵۰ درصد است و افزایش هزینه‌ها نیز فشار بیشتری به شرکت‌های ریلی وارد کرده؛ نرخ بلیت قطارهای مسافری از ۱۷ خرداد ۲۱ درصد افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/462942" target="_blank">📅 12:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462941">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZWKGmHiepXlHLp6wBEzMuMaACf8Owyop-Ks-UqdkUu18KOU1SMHShxw4UYXuSRSVbCjLmkfbrRPOTsoII6NHVEKFtXcmZBxxG9Xzi7E85hBjhlNOQkfiPz7kJrZCLCPIiDjYuWNLdHIMPO6aRz-fVjTdHVlPfyyjdDXutA3zySU9vQrutVg6_hUNFKaEMgMuZy_328unIR2QNEjE_QZFwERyVuLNbyqMo8xLp6Vs6zCHzorF0Wg27RhNhgdIFo__VW9jSjlKGrS_DwvDoGiXvfei3_zjJaE9seJIs5KKwO9fPoQ1CjExNoy7Omlq9Y93V0_uF6BLPvxOoOKIbK1Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام جرم
دادستانی علیه عوامل برگزاری دوی ماراتن تهران
🔹
درپی برگزاری مسابقۀ دو ماراتن در بوستان ولایت که در آن موازین قانونی و شرعی رعایت نشده بود، دادستانی تهران علیه عوامل و دست‌اندرکاران برگزاری این رقابت اعلام جرم کرد و برای آن‌ها پروندۀ قضایی تشکیل داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/462941" target="_blank">📅 11:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462940">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a2334d95.mp4?token=eRKL0KAexQsxXcYt5ncdxPrmy8Ptr1my__HejvbKBWLEwERY_iBYJKuRuYQcNnvCQRdlogVuCfkLmT9oxtHdmK2RJFCbLFFlWImQaCJg6hEg7_sPCdca9bvDrFW6wTymjldttgCjk9nZrm1Q48P-InyantdqmKJBWvuLSjCbIoFRPvuwLBn4xa_839ZRqgEf54IK6aHoK0Io31pI-9fJc92VT11mvaCttxxER6WUAVpFrmbXSGVXmpQzcDctn3MSY8Z8yESYDM-89nMNdBkAckiaY36nhvRc9eNx6lGHNZL9MaRKC6Cyh2VB5FvAsULjdWAcf6kwtY-D_Oj-5ToOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a2334d95.mp4?token=eRKL0KAexQsxXcYt5ncdxPrmy8Ptr1my__HejvbKBWLEwERY_iBYJKuRuYQcNnvCQRdlogVuCfkLmT9oxtHdmK2RJFCbLFFlWImQaCJg6hEg7_sPCdca9bvDrFW6wTymjldttgCjk9nZrm1Q48P-InyantdqmKJBWvuLSjCbIoFRPvuwLBn4xa_839ZRqgEf54IK6aHoK0Io31pI-9fJc92VT11mvaCttxxER6WUAVpFrmbXSGVXmpQzcDctn3MSY8Z8yESYDM-89nMNdBkAckiaY36nhvRc9eNx6lGHNZL9MaRKC6Cyh2VB5FvAsULjdWAcf6kwtY-D_Oj-5ToOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی شورای نگهبان: انتخابات شوراها به‌صورت تمام الکترونیک برگزار می‌شود
🔹
زمان برگزاری انتخابات شوراها در اختیار شورای‌عالی امنیت ملی است.  @Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/462940" target="_blank">📅 11:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462939">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ee14176c.mp4?token=iAURAhaQ6TXx6sfiUB92B-U6N3evcoeT9ra1fBzOIeObfeC2fSqucvdOrn6iDaL7jt6U26CqOVzx91kenWZN86-B3_pi34ighM3DbqZ-sN9QA_xpKl3v6b4MxmcUtYIl2feEx6725UQj99RzTRXlhcyYUQ1yaQUobVHTn86zXDJp7sjZ3kwCsWDpmAz-Uya_bA1enhudqhxb5oTPEcwchHVZBEVzjsGg8d3nGamWn0hDmk-ALq9lnAyqdRHCRiS51ofC-bED069meVqS837umoYTNPx4EWy1fNzbhQjCbi_xGbPEYliEp39HHN3_4t3NhwvkRgnkcklZjhI4-21mjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ee14176c.mp4?token=iAURAhaQ6TXx6sfiUB92B-U6N3evcoeT9ra1fBzOIeObfeC2fSqucvdOrn6iDaL7jt6U26CqOVzx91kenWZN86-B3_pi34ighM3DbqZ-sN9QA_xpKl3v6b4MxmcUtYIl2feEx6725UQj99RzTRXlhcyYUQ1yaQUobVHTn86zXDJp7sjZ3kwCsWDpmAz-Uya_bA1enhudqhxb5oTPEcwchHVZBEVzjsGg8d3nGamWn0hDmk-ALq9lnAyqdRHCRiS51ofC-bED069meVqS837umoYTNPx4EWy1fNzbhQjCbi_xGbPEYliEp39HHN3_4t3NhwvkRgnkcklZjhI4-21mjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: احتمال دارد انتخابات ریاست‌جمهوری و مجلس به‌صورت همزمان اردیبهشت ۱۴۰۷ برگزار شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/462939" target="_blank">📅 11:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462938">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d442ae694.mp4?token=a0RuWXtmZkaN045mC0Up2NP3lyk2aGJS2ib6FFObGpvG1oXyIIACzMNr_EGLXFiLydzDYFdA8dk5p1Nzi7yLWI_bJbo8MkBVvVl_DIriVCcKDKd1rHM030sd9elZgTPFl06W45hwPalDeamIc20aS8twF17-6bOOId19Y1qD6AJl4-n7EjpjVmuVWrlaFLqn3lxFEOQM1Z2X-DD_EW9Q3NOEqKHeI3GfwSIFhhrC22SBd83knizyAwpHNpNKJncS3_3Ee0afdOtZb48_MJ5jj-mk9jbIRGiSZOukRGIpayzt_qv0r3UjTBHllLq2JheyKSWtNFurmw77jz0ns4lWmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d442ae694.mp4?token=a0RuWXtmZkaN045mC0Up2NP3lyk2aGJS2ib6FFObGpvG1oXyIIACzMNr_EGLXFiLydzDYFdA8dk5p1Nzi7yLWI_bJbo8MkBVvVl_DIriVCcKDKd1rHM030sd9elZgTPFl06W45hwPalDeamIc20aS8twF17-6bOOId19Y1qD6AJl4-n7EjpjVmuVWrlaFLqn3lxFEOQM1Z2X-DD_EW9Q3NOEqKHeI3GfwSIFhhrC22SBd83knizyAwpHNpNKJncS3_3Ee0afdOtZb48_MJ5jj-mk9jbIRGiSZOukRGIpayzt_qv0r3UjTBHllLq2JheyKSWtNFurmw77jz0ns4lWmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: ۴میلیون و ۵۶۳ هزار و ۱۱۸ نفر اتباع خارجی شناسایی شده‌اند
🔹
۳۵۲.۶۳۶ نفر از اتباع امسال به کشورشان بازگردانده شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/462938" target="_blank">📅 11:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462937">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">لغو مجوز فعالیت یکی از شعب بانک ملت در ترکیه
🔹
روزنامه رسمی ترکیه اعلام کرد مجوز فعالیت یک شعبه بانک ملت در استانبول لغو شده است. نهاد ناظر بانکی ترکیه دلیل این تصمیم را اعلام نکرده است.
🔹
بانک ملت چندین دهه در ترکیه فعالیت دارد و دارای ۳ شعبه در استانبول، آنکارا و ازمیر است.
اما آیا این موضوع سابقه دارد؟
🔸
بانک ملت پیش‌تر نیز با محدودیت‌های مشابهی در انگلیس و اتحادیه اروپا مواجه شده بود که موفق به رفع آن‌ها شد.
🔸
خزانه‌داری انگلیس در سال ۲۰۰۹ محدودیت‌هایی علیه مراودات مالی با این بانک وضع کرد که در سال ۲۰۱۳ با حکم دیوان عالی بریتانیا لغو شد.
🔸
اتحادیه اروپا نیز در سال ۲۰۱۰ دارایی‌های بانک ملت را مسدود کرده بود، اما دادگاه عمومی اتحادیه اروپا در سال ۲۰۱۳ نام این بانک را از فهرست تحریم‌ها خارج کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/462937" target="_blank">📅 11:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462936">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9b1fb122.mp4?token=nYeUtJ3XmHbnsKFe-5hMViExMQTIuckk4Am0_3glCyvhFDxfxf1vGHJaCuTihhmupLmkEDo9uncbKW6nzODJeuzetj46p_zcKjN3y8SMhJmvNk3AtnwLpPK7MXN7xDx1rFgnia-3iTYVS9ceKGktn9-yeC_Op-ZFD62rOW7LweIq6_7-eC19Wmd1iW8SaPysLcmg5xeBoHApiRRUG0b70bJCdvCAbspS-6maYWaYMAVydjQZ_GmZWeXq1Yrv3urPSc-xJnvXEpPs_4kPgcB9iv2okgQ6wCUnm2vMh9zbDBB8y0uMliwLCSKkqxNsFvLZVGXMaLgjEDkL76kAWD3XsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9b1fb122.mp4?token=nYeUtJ3XmHbnsKFe-5hMViExMQTIuckk4Am0_3glCyvhFDxfxf1vGHJaCuTihhmupLmkEDo9uncbKW6nzODJeuzetj46p_zcKjN3y8SMhJmvNk3AtnwLpPK7MXN7xDx1rFgnia-3iTYVS9ceKGktn9-yeC_Op-ZFD62rOW7LweIq6_7-eC19Wmd1iW8SaPysLcmg5xeBoHApiRRUG0b70bJCdvCAbspS-6maYWaYMAVydjQZ_GmZWeXq1Yrv3urPSc-xJnvXEpPs_4kPgcB9iv2okgQ6wCUnm2vMh9zbDBB8y0uMliwLCSKkqxNsFvLZVGXMaLgjEDkL76kAWD3XsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور تهران: تا ۸ مهر عملیات عمرانی حتی در معابر فرعی متوقف می‌شود
🔹
ممنوعیت تردد ناوگان باری به‌جز دارو از ساعت ۶ تا ۱۰ صبح مثل هر سال اعمال می‌شود. مجوز دورکاری اختیاری یک روز در هفته از اول تا ۸ مهر برای کارمندان به‌صورت اختیاری تصویب شده است.…</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/462936" target="_blank">📅 11:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462935">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr772VgMp-BAJmSYRjmkGUBdOwmGTz-d9KmDjcZ63zKL7G6_bLnw17x2f5dxrWal9sPRlZaexCy23rULHtILkrnpcFaICKEmwRCLstq9QRynq-k09gIEgO4dy0I9yTegYQtBOxiF2rVik0_VbHEVSorRpzkIdHf2Jp_EJFD3Xfk_n076DAYpmvjEtadA_l8Z7ec3nj3fWbhYau9CcFlnvxEwlnFHf2Frl7KillLJb0VMe5a4if9ZIYhtRKA4dMXSE5vHy671oxsMYQSTYIqgWDXe0WNLFzcxas3kw05nXOUQo3Tzcg10JeCNXbS52sJwdM80tATUxIStbPK6bzXAnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«پرسپولیس ب» کنسل شد
⚽️
باشگاه پرسپولیس که قصد داشت با خرید سهم یکس از باشگاه‌های فرد البرز و بعثت کرمانشاه تیم دوم خود را در لیگ یک حاضر کند درنهایت موفق به خرید سهم باشگاهی در لیگ دسته اول نشد.
⚽️
به این ترتیب پروژه راه‌اندازی پرسپولیس ب در لیگ یک، دست‌کم…</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/462935" target="_blank">📅 11:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462934">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcaQjlqXnbS2TREm9jFH0GX4QieOLVMS4834gMpL8VDOtGHhAPvWEhOkMrAsVO41TSMLAu156wEf5ovzoIzTLtU--EEPHWBElNPfwcRObBnMjwujd6-VRRnj5JqRbMRdQD12ieRXWfqSyFexL4QinXpIEB6sC0OVQ4HK6ePj2ywYOMLUUHiSTNJv1Eposc2W1apm20ZCmtBlB7T0W8I3s7Z99-2VrCQVtqcGzNUCT4HtHsNdRqRNqi40NlrpVCdtapJDMZ41opaID80RC1cFany7mS3tpNHIPXf_CXUHcAel-ju2WHK27o2VXsNUAeoGE-uiOmttH-nqkS1wR7gAgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله سیدموسی شبیری زنجانی به‌دلیل عارضۀ خونریزی معده در بخش مراقبت‌های ویژۀ بیمارستان بستری شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/462934" target="_blank">📅 11:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462933">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecf6MQ-eGGze4_XfdA7K_2lOI3vhyOA6ObYB1ZzubTxn_19lcuXks5eYdKmY48nIeFq6LArzkjnqysbuMrOv6DGfFIU55O9Te8BpZEwJGwClrzVsyVZhzIgQAb-HZRm9Mj-EMWsYmtjewUUAKWIy6iEFG4sHcHS4QaKU4rDpxKvlPt67IDvu_2I3_o6fTRHwW-01eZ6rG2FmF1EkkoyutFrap2CsYmT-ymD6TJcAlhpuUeVP56rEPMzkQoxZ2670aAE_tcvSzXVDdJ2eA19VS1Mqi8EfCFcDKobRtXxwwfws7_h-buXt2xayv0p_QVuLq0YLoyg7qVYav1rTUbKwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ لحظه‌شماری نخبگان ایرانی برای کالبدشکافی زیردریایی به دام‌افتادۀ آمریکایی
🔹
کارشناسان حوزۀ نظامی معتقدند غنیمت واقعی ایران از شکار زیردریایی هوشمند آمریکایی در دانشی است که از دل این سامانه استخراج خواهد شد، و آمریکایی‌ها باید نگران روزی باشند که فناوری…</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/462933" target="_blank">📅 11:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462932">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf99e50f39.mp4?token=e1ovyFYHpyPZzYyk-VdIauHjr7H0U-k0hZF_6DVkGt4mPCTzqvnZFLd01S9rfWfxbMAraC3nKYW_gIB6eXHMWm68gCmENFaQLwmd52GQIjSmnO2H6euafdVPQHd1Nvf9cIoKZriojfJjAB4bYr3qQkOn7gf_6FE1JdSptdC3Qv6F482zCIZWN9sGLEn6wC07f0tVWLnwWxQLL90-1L7lUnijKJkbsKZJSl1Ky6DM5GhxZg09m1PHxircElIv-bbumsDzJ8Z4z1rijH7Mj8qvHCic1SXqd1pq0gyB32ovXJ2QOTvfcTHvNWIdt8HjW2bddMEbTK8HRAojW7CnSeu2oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf99e50f39.mp4?token=e1ovyFYHpyPZzYyk-VdIauHjr7H0U-k0hZF_6DVkGt4mPCTzqvnZFLd01S9rfWfxbMAraC3nKYW_gIB6eXHMWm68gCmENFaQLwmd52GQIjSmnO2H6euafdVPQHd1Nvf9cIoKZriojfJjAB4bYr3qQkOn7gf_6FE1JdSptdC3Qv6F482zCIZWN9sGLEn6wC07f0tVWLnwWxQLL90-1L7lUnijKJkbsKZJSl1Ky6DM5GhxZg09m1PHxircElIv-bbumsDzJ8Z4z1rijH7Mj8qvHCic1SXqd1pq0gyB32ovXJ2QOTvfcTHvNWIdt8HjW2bddMEbTK8HRAojW7CnSeu2oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور تهران: امسال یک میلیون و ۴۰۰ هزار دانش‌آموز در تهران داریم.  @Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/462932" target="_blank">📅 11:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462931">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ef82db5.mp4?token=SbFbN3v-fckJKM-7Oqdh05WBAmOABk9fd6CltST6f4AYbXsBpSbQ0gi1JAPxNE7wBrdZPnBWTvyiLh3v6Jj2LsVCyDzbp4cl0kZJ60eRFNLIlSdPU1gu8xp6_75X0io8xbpPAa9BpehGkm_Ajz7_2llCxPQodO_chVfYSDB7BlehZ-u7N6TMI7-HpaOF2PinNYXFFVvgf5Jk532IR8GWD1uvIW8JsKqo9PTDOrMWYYUumbqi6h98o30EuuBG4417W0isDD5-571iR7cPAx8vmrLAzZH4E8mGkKf3v90VepCcTMPXNSfOZIStyan_fbwG58_Seacd8QKyHpOo-lsYRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ef82db5.mp4?token=SbFbN3v-fckJKM-7Oqdh05WBAmOABk9fd6CltST6f4AYbXsBpSbQ0gi1JAPxNE7wBrdZPnBWTvyiLh3v6Jj2LsVCyDzbp4cl0kZJ60eRFNLIlSdPU1gu8xp6_75X0io8xbpPAa9BpehGkm_Ajz7_2llCxPQodO_chVfYSDB7BlehZ-u7N6TMI7-HpaOF2PinNYXFFVvgf5Jk532IR8GWD1uvIW8JsKqo9PTDOrMWYYUumbqi6h98o30EuuBG4417W0isDD5-571iR7cPAx8vmrLAzZH4E8mGkKf3v90VepCcTMPXNSfOZIStyan_fbwG58_Seacd8QKyHpOo-lsYRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: نگذارید جوشش خون شهیدان فروبنشیند!
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/462931" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462930">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d4b05f527.mp4?token=oNka_moy43DhW3knDMFKCmkmflvik_X9mNZqO_rnens4JHZiVZCMlYDp6Lgair71A3CKn20Nw3WulFDiuTMmB5_kjqHxIkhlaiPJ7wgyTNNx03IziJx-6f9qNIXSZqTkaG3CU1q8_aBb9H__TULu6t4bBd0yKqauLdY8CinHp2rLaVGNigiadvVLGvrHkIKWrSau61HbrQK42kT7zB-DBR1Ktq9WkmRcIC8JEEljkU06uknUhhrwKlNJwJjY94fz9OF1iBacv-iVFGIzgzBfNxOQ2IlrIfZeFeoci3rRFB9hywbizzNgQgqdFp2IxrDpCY9cP6pBwWUnLftPtr-1-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d4b05f527.mp4?token=oNka_moy43DhW3knDMFKCmkmflvik_X9mNZqO_rnens4JHZiVZCMlYDp6Lgair71A3CKn20Nw3WulFDiuTMmB5_kjqHxIkhlaiPJ7wgyTNNx03IziJx-6f9qNIXSZqTkaG3CU1q8_aBb9H__TULu6t4bBd0yKqauLdY8CinHp2rLaVGNigiadvVLGvrHkIKWrSau61HbrQK42kT7zB-DBR1Ktq9WkmRcIC8JEEljkU06uknUhhrwKlNJwJjY94fz9OF1iBacv-iVFGIzgzBfNxOQ2IlrIfZeFeoci3rRFB9hywbizzNgQgqdFp2IxrDpCY9cP6pBwWUnLftPtr-1-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور تهران: امسال یک میلیون و ۴۰۰ هزار دانش‌آموز در تهران داریم.
@Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/462930" target="_blank">📅 10:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462929">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plp5VZxndNjg5b-DxVlJgXc1BP77ssg-QlC1hmqF7clLgMRQnLOKb9iqeRh_6agAwMnpLrLJ9J556fts-SgXxTvsK406YLZNbA4E11DvPV6BHpxzSy2hMoAW5f0ogmAK_FAPlWULMeJPBcmEIBmVdLImz_pbz7R20qEVJ9NHrHQnfwWX9CRpEyHx3VYsTdNy0BSjQTYqZpQ3OwK2EEiZmKy2IK6WT2fLh1n9An82iAfXvdvgbkiq0w7P2WunfCIskwVnZ17kFX9iyGvZ8ukW9CZ7GBkUdBO1bCeIiy9Y55D3GOBgdJxBOGR-rXkhoFx66Uig-wXvg6PMNxvCsVp4xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنظله تصاویر سلفی ۷۰۰ نیروی امنیتی اسرائیل را منتشر کرد
🔹
گروه سایبری حنظله در پیامی با اشاره به «نفوذ گسترده سایبری به تلفن‌های همراه صدها نفر از افراد وابسته به ساختارهای امنیتی اسرائیل»، اعلام کرد تصاویر مربوط به حدود ۷۰۰ نفر را در وب‌سایت خود منتشر کرده و مدعی شد این افراد از طریق ابزار «ناعِم» هدف قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/462929" target="_blank">📅 10:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462927">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bcb37fe03.mp4?token=e4_HAABUkPZC00x4bgQ34xUrTvxLHPNuZymvnSJVGn2lFINVf6gQrf08SXvLnlLNHds6sSKxppfGlDsh0nMhxHc1DyZq6bG45hTbzyuA1AI6gO88FXBN3J6n3U12iiggsS7DSt96Y5mW9U384058yKcOJK5o4-PW8_mWdnkvT3qv9ULfY0Cjur5aXHkgbN0XDE_znz94C77b40Gz-eYvUjv2125JiSUmAUy7G4FkVj7UNYcsU-1aEcDjxCUjQHJZqK8cx-_VNKjl7KOdV3MBMi9fgfRLDWSgocm0Mw1RjbGU4sFfU8UpKK6iHeSnDAttdCFbAHKB6CTpqXXZlTcaXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bcb37fe03.mp4?token=e4_HAABUkPZC00x4bgQ34xUrTvxLHPNuZymvnSJVGn2lFINVf6gQrf08SXvLnlLNHds6sSKxppfGlDsh0nMhxHc1DyZq6bG45hTbzyuA1AI6gO88FXBN3J6n3U12iiggsS7DSt96Y5mW9U384058yKcOJK5o4-PW8_mWdnkvT3qv9ULfY0Cjur5aXHkgbN0XDE_znz94C77b40Gz-eYvUjv2125JiSUmAUy7G4FkVj7UNYcsU-1aEcDjxCUjQHJZqK8cx-_VNKjl7KOdV3MBMi9fgfRLDWSgocm0Mw1RjbGU4sFfU8UpKK6iHeSnDAttdCFbAHKB6CTpqXXZlTcaXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت‌پرده انتخاب اهداف نظامی دشمن توسط تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/462927" target="_blank">📅 10:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462926">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dj1Ix30iAPEaoZ5JPEfnNWlFWpjgizWkK_CyoMPOEQxJG3oi3kSmeQOs1Ogy5gaviNunby5mleB3ktgzEYLXIg4IGubG25QAiY4r_ykjPpCrPqFKLweFA62airCr_X2CoA2Fyq7iYnFu8K_ijC7ZQg5DmK_3mfN0oYP5Vq4ksrcXq_TF2-Gs75FLZDh2HqCajBtlShT6P0ILYGKniztROjcIN27H9EpsjLhRRF1UUlOliCgk5oYBkcXl-ccsZz95UCdMwH21B8hDMLMvldnjITNFxp1dMkSwPi8G6LLVLqHsES6sINd2DhW3-pcF-1Hf57l6BWQkPI0dCyqqpHd4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462926" target="_blank">📅 09:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462925">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg1s-nD5EzzNb_DaaE6WU5GPdxSck4gh09SKmWLD5jDNgguK7xwUkofo62GV5WXJv49zbeXjpZgxIbnVlR9ew1I7KM4CTkv46EKPvwxlnFj4OP5_w57gDuDMk66WNd-sZL1HCDOhSXFlpB0q0ptKKYgZ1YZEvLyk91Q_ZkHNMPJ47sP89VUu-jcHMR9KzjLyeSpGHNGDi0_oXuJpWNcPVeu5Zrr7LPa87XluzwI8hex-3RI7v-b8XzT_wczi4HQC54BORbAVVqsjx6a74PT6IyhIYbzioXb9GKmgDWQvw5EWR5sD8RSuXVocH-9nN86cuoo8JYUShnA-Yj-hBdHmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پاسخ عراقچی به وزیر خارجۀ فرانسه: اشک تمساح بس است آقای بارو!
🔹
یک‌ونیم میلیون الجزایری در جریان جنگ استقلال آن کشور توسط فرانسه قتل‌عام شدند.
🔹
پاریس کم‌تر از یک‌دهم آن‌ها را رسماً ثبت کرده؛ ولی همچنان از هرگونه عذرخواهی بابت جنایت‌های استعماری خود خودداری می‌کند.
🔹
اشک تمساح بس است آقای بارو؛ سکوت شما در زمانی که آمریکا کودکان دانش‌آموز ما را قتل‌عام کرد، گویای همه چیز است.
🔸
وزیر خارجۀ فرانسه در اظهاراتی مداخله‌جویانه دربارۀ ایران گفته بود: «ایرانیان باید بتوانند آزادانه دربارۀ آیندۀ خود تصمیم بگیرند و حقوق بنیادین آن‌ها باید رعایت شود».
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462925" target="_blank">📅 09:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462924">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa65aa3a39.mp4?token=gROaW7M82BlceZ1CKd4ImiwlJroWCWZK9X63iqDsgpy15ggFRGD5yF6pJAf57TfNa5GImyLV25AOb0p99mMSE7JilYvPo-WdJTifksfy_3_rpEObJ64_L9GCMFtsHB1aZlIzF3Jtph1SZ3meSHhSb40hEsXwEPff7FxF3681bk3pMbZAUFSQWiptJC0-36tODaZpAlHgrw72A-aXSZUedWbqK6Th1Emb0t8kDouc3SxvgeUxtjIe1i8oUiOMBeq1vV3zumI-V1ByHne3WLlM5DmqMie_KvSqHUbmw8i0IILYeRGN4At9PJ_LBRWWEkueOWHLmBvIlJfbT3WITvtzHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa65aa3a39.mp4?token=gROaW7M82BlceZ1CKd4ImiwlJroWCWZK9X63iqDsgpy15ggFRGD5yF6pJAf57TfNa5GImyLV25AOb0p99mMSE7JilYvPo-WdJTifksfy_3_rpEObJ64_L9GCMFtsHB1aZlIzF3Jtph1SZ3meSHhSb40hEsXwEPff7FxF3681bk3pMbZAUFSQWiptJC0-36tODaZpAlHgrw72A-aXSZUedWbqK6Th1Emb0t8kDouc3SxvgeUxtjIe1i8oUiOMBeq1vV3zumI-V1ByHne3WLlM5DmqMie_KvSqHUbmw8i0IILYeRGN4At9PJ_LBRWWEkueOWHLmBvIlJfbT3WITvtzHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان نیمۀ‌اول بازی هندبال ایران و کویت با برتری ایران  ایران ۱۵ - ۱۳ کویت  @Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/462924" target="_blank">📅 09:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462923">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq5eLjTFAADX9CC7sh4RgHdnDQ7hae6RX3cGNqhpAq9HMR1S67L5f3hfIeGGBoSfHWH_kVwy4swSOfLSAN05rK29H1XPDgD7ukNqC-9KTvE3z1rTUtp_jLKZqgWqcwp8o6uQfqGE2VfsX7hh-Nxik43iKHeZs7JHOtvhRaZgcDq0w6s5opcCuxlGzuk2LoiEbR9I6lovE3U0v36r1j8mg3VapUd5r5g7A_3GFVZxYlz5Btbx1eOvHOSv3yjRCRKwuJoGkHcGxqIJiglqG7d5kBdoIwNQm_tX0_9FLdHNkiqgL-WIzeGHZ78PYRT28PX-uJhR6xS8nPZqMm3goegOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام خائنی که اطلاعات سایت‌های موشکی اصفهان را در اختیار موساد قرار می‌داد
🔹
حسین پدران، فرزند حمیدرضا که اطلاعات سایت‌های نظامی حساس کشور در استان اصفهان را در اختیار موساد قرار داده بود، به جرم جاسوسی و همکاری اطلاعاتی به نفع رژیم صهیونیستی بازداشت و محاکمه شد و پس از طی فرآیند قانونی و تأیید و ابرام حکم در دیوان عالی کشور، به سزای اعمالش رسید و به دار مجازات آویخته شد.
🔸
در جریان جنگ‌های تحمیلی ۱۲ روزه و رمضان، دشمن صهیونی-آمریکایی برخی از سایت‌های نظامی حساس کشور را هدف قرار داد که مشخص شد برخی از این اهداف با همکاری عدۀ معدودی از مزدوران و خائنان به کشور مورد اصابت قرار گرفته‌اند.
🔹
حسین پدران از جمله خائنان به کشور بود که تلاش کرده بود با ارسال اطلاعات حساس و طبقه‌بندی‌شده به سرویس‌های جاسوسی آمریکا و اسرائیل، در راستای اهداف دشمن عمل کرده و در این مسیر بنا به اعتراف خودش به منفعت مالی دست پیدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462923" target="_blank">📅 09:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462922">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/145990c427.mp4?token=BL24nSLstvKM-1aDnqPDUy5gcZSFor5lnuxnck3YawsFXeqDm22sQkal5pS-b4eV6w4GGltLqaJBJNIKLyAW1fkyb5MjOQf2MYnFy2NZJu-ijnlpeR09SYxSFhKCX2J4Vl8SASS6WlWygJ80EQ_yYp34fJy9EBprsVEx5rMQZuvohWEvSvVAVgPdfhgRr0Ji7F9dUHv8Awi_ZVtikjGzBHYQVmYwN9r_mAjOPurMrCLSZDKuqOry1sILc20Su5n8lySt82ahYLT6SVeit7sz5of5fC0i5t2H4C38HsNukVcX5v9DwhJshDksfwretQwLuQSD6t4k_-Pg5yClxr5tjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/145990c427.mp4?token=BL24nSLstvKM-1aDnqPDUy5gcZSFor5lnuxnck3YawsFXeqDm22sQkal5pS-b4eV6w4GGltLqaJBJNIKLyAW1fkyb5MjOQf2MYnFy2NZJu-ijnlpeR09SYxSFhKCX2J4Vl8SASS6WlWygJ80EQ_yYp34fJy9EBprsVEx5rMQZuvohWEvSvVAVgPdfhgRr0Ji7F9dUHv8Awi_ZVtikjGzBHYQVmYwN9r_mAjOPurMrCLSZDKuqOry1sILc20Su5n8lySt82ahYLT6SVeit7sz5of5fC0i5t2H4C38HsNukVcX5v9DwhJshDksfwretQwLuQSD6t4k_-Pg5yClxr5tjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: در ۵ روز آینده در بیشتر مناطق کشور جو آرام خواهد بود
🔹
در ساعت‌های آینده در گیلان، مازندران و گلستان باران می‌بارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462922" target="_blank">📅 08:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462921">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آغاز پیش‌فروش بلیت‌ قطارهای مهر
🔸
پیش‌فروش بلیت قطارهای مسافری برای سفرهای بازهٔ زمانی ۱ تا ۳۰ مهر ۱۴۰۵ در سامانهٔ
raja.ir
و سکوهای آنلاین فروش بلیت آغاز شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/462921" target="_blank">📅 08:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462920">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b167cf75d.mp4?token=UfI21jX8k5YD5XWY0qbRbGxmlWBWlBPEkj7M5uvx2li0HkPn7dBmiMUrpLHYaoCL3Lrk_Bk3nC2tqBzNhUblhXX6uzxs0IoKttkmGEZZaEm5893a_ktP4V0bCRzJu-Skxnk7igZ_C51ox572GokwBTPRhqejcbFTrZIi0ptPJcw0P7Cg-dAADJvavrlpZqyX3LWMQw1UaFrOA7dPYCAYhquPvT-V4zUh2X_BAhrPEhU6B3ZfMJzVMZd-lYUVWR5Bk6ovTh5dc5oiNvovFPnK84wyHqRgol0tq6xVPz9lwQCQ4GzvdOr0YhRZt7zuJL0Qi9uieUhku8IcCTB-G3kC1FV3LHsNxE6FGGGi4JV5kHu1wdsJ1fCMqNE5o8NIfm4_DEA7Yqch1zeEKFHzCnkqZ5rqFJWwdFtoXyFWUW5gac3GowOqwkA0fCqTAlMq1iFT-5fi_lS29qJKVdK1A6x-3HXK-oMQmOtcPH23bZWJ1eSp_uJuwewxn9c1jFrG0zrkPlIVjmbMETYn6JvyzTJmF0actImUQWY1knraUImMC8pf5Q1aKOuGXnKH-2HF-I6x9q1f-G2PcMWtrhRyls-MBuTiT6kaUZXxXPeHj5GvWJYxis4koQTlONELRk-akmtwoS29ftgpzdpOZK2a9FiKxLln8hbc1GvhxvFr6mxaZ3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b167cf75d.mp4?token=UfI21jX8k5YD5XWY0qbRbGxmlWBWlBPEkj7M5uvx2li0HkPn7dBmiMUrpLHYaoCL3Lrk_Bk3nC2tqBzNhUblhXX6uzxs0IoKttkmGEZZaEm5893a_ktP4V0bCRzJu-Skxnk7igZ_C51ox572GokwBTPRhqejcbFTrZIi0ptPJcw0P7Cg-dAADJvavrlpZqyX3LWMQw1UaFrOA7dPYCAYhquPvT-V4zUh2X_BAhrPEhU6B3ZfMJzVMZd-lYUVWR5Bk6ovTh5dc5oiNvovFPnK84wyHqRgol0tq6xVPz9lwQCQ4GzvdOr0YhRZt7zuJL0Qi9uieUhku8IcCTB-G3kC1FV3LHsNxE6FGGGi4JV5kHu1wdsJ1fCMqNE5o8NIfm4_DEA7Yqch1zeEKFHzCnkqZ5rqFJWwdFtoXyFWUW5gac3GowOqwkA0fCqTAlMq1iFT-5fi_lS29qJKVdK1A6x-3HXK-oMQmOtcPH23bZWJ1eSp_uJuwewxn9c1jFrG0zrkPlIVjmbMETYn6JvyzTJmF0actImUQWY1knraUImMC8pf5Q1aKOuGXnKH-2HF-I6x9q1f-G2PcMWtrhRyls-MBuTiT6kaUZXxXPeHj5GvWJYxis4koQTlONELRk-akmtwoS29ftgpzdpOZK2a9FiKxLln8hbc1GvhxvFr6mxaZ3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۲ شب مقاومت ملت ایران و اعتراف دیرهنگام شیطان بزرگ
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462920" target="_blank">📅 08:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462919">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febaebfe43.mp4?token=hrjTxX6oogYcImcyOvZYCwOaixpDV_o3X5tCPpPUHjiOvOILHWQKdo6IetEMtg4t_6bUNVk6AGj1xHS85IPzZc8S97Klbi8vYGidrncofxhOHH-6M_r83nUEzxPCwN1tl2UOdiImoIQQ88fAu6yK7SjHS-LJZXeBcHWDuM6PCHr_q9J3BcP6BkLKSKaTh1DIoyI8RtqTF-kvy32480Hs4FswxWJfSnrbGD0mmUeHAhehXhT-d0IM1MfcGR4fMxsv0P_r73hlKkNpEeAKooPlq_CkzF1V70jH1u8c3C6IDr4N3Q9j9FFq3sBm2i_T11no6wjc_U3EoBKNGsTBPAQAlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febaebfe43.mp4?token=hrjTxX6oogYcImcyOvZYCwOaixpDV_o3X5tCPpPUHjiOvOILHWQKdo6IetEMtg4t_6bUNVk6AGj1xHS85IPzZc8S97Klbi8vYGidrncofxhOHH-6M_r83nUEzxPCwN1tl2UOdiImoIQQ88fAu6yK7SjHS-LJZXeBcHWDuM6PCHr_q9J3BcP6BkLKSKaTh1DIoyI8RtqTF-kvy32480Hs4FswxWJfSnrbGD0mmUeHAhehXhT-d0IM1MfcGR4fMxsv0P_r73hlKkNpEeAKooPlq_CkzF1V70jH1u8c3C6IDr4N3Q9j9FFq3sBm2i_T11no6wjc_U3EoBKNGsTBPAQAlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان نیمۀ‌اول بازی هندبال ایران و کویت با برتری ایران
ایران ۱۵ - ۱۳ کویت
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/462919" target="_blank">📅 07:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462917">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اعتراف پنتاگون به هزینۀ ۴۳.۶ میلیارد دلاری جنگ با ایران
🔹
پنتاگون در تازه‌ترین برآورد خود اعتراف کرد جنگ با ایران تاکنون ۴۳.۶ میلیارد دلار برای آمریکا هزینه داشته است؛ رقمی که هنوز خسارت‌های احتمالی واردشده به تأسیسات نظامی آمریکا در ۸ کشور غرب آسیا را شامل نمی‌شود.
بر اساس سند ارائه‌شده از سوی پنتاگون به کنگره، این رقم از دو بخش تشکیل شده است:
🔸
۱۱.۲ میلیارد دلار هزینه‌هایی مانند سوخت، حقوق و مزایای نیروهای حاضر در عملیات، خدمات پزشکی، قطعات و نگهداری تجهیزات و دیگر مخارج عملیاتی
🔸
۳۲.۴ میلیارد دلار مربوط به هزینه‌های جبرانی شامل هزینۀ جایگزینی مهمات مصرف‌شده، هواپیماهای آسیب‌دیده و سایر تجهیزات و دارایی‌های نظامی
🔹
به این ترتیب، بخش قابل‌توجهی از هزینۀ برآوردشده جنگ نه صرفاً به هزینه‌های روزمرۀ عملیات، بلکه به جبران مهمات و تجهیزات نظامی از دست‌رفته یا آسیب‌دیده مربوط می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/462917" target="_blank">📅 07:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462916">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrQox7nbTagy_-so4YL3fSZwSOIx67QQvZzY3Xh47eRuwUWG9nIEKQHjbUvDUG9o07zxqQNH7xnjQfoEeSYfYdWf8jcZge0HPL6IwApDTqPTITdSwcbnCF_nua-BynJuEHV9GAAd8-7cR0YWS3ZmnaRP3P6EYr_lZ30YxFT-hU3XmZHE8qa9zMiamrGV8FhDxLivV_Rh8eBsjZ5TN9olDFtURN6qZ5MPaUTeP9lamkzqlV6qiqcRVexyoXDybItEIBHIb0JlM_EpJw1DV3v-_tW97njZuLuJA7OsVwxd0TYyi850O3oYfll8vk0tYBtG3ibT27j3EawyhD8HlBNyKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار به مسافران شمال کشور؛ خزر مواج می‌شود
🔹
مدیریت بحران کشور با صدور هشدار دریایی سطح زرد، از افزایش سرعت وزش باد و ارتفاع امواج در دریای خزر خبر داد.
🔹
این شرایط از امروز تا ۳۰ شهریور، مناطق ساحلی و دور از ساحل استان‌های گیلان، مازندران و گلستان را تحت تأثیر قرار می‌دهد.
🔸
از جمله پیامدهای احتمالی این شرایط می‌توان به خطر غرق‌شدن شناگران، آسیب به قایق‌های کوچک تفریحی و مسافربری، اختلال در تردد شناورها، و اختلال در فعالیت‌های ساحلی و فراساحلی اشاره کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/462916" target="_blank">📅 07:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462915">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRtYvYFH4QxUj-6LcCvyguGTRoCVh4bHeWJTNdXbXwqFmu56nHHSYaBtlmGxIQW0zJOOyi1_04gtIFlIrkQvCq87ylKTfb2EDXySm6EOzFrhKSzVnij87LkH8FPfJNFGec6EMCWX4Xph7fmXIVfD3P-37g5OVEgYYp-IKV74BBWAx0X7i1217GV6Ipcqp49MXArtyELUtvT3YYLjHTidfwVJwfGxNgne3weTbuAIyFDFv006D4f2CDuMFw-WUFq6flhktNykCpTWjnyuDp3INWJRxoyjMxu1qstaVQw22xq_H44IJPyUFyDxZ0fgGEhKGzi6OqfGkjWLyrmEKLUmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز حضوری مدرسه‌ها با ۱ میلیون و ۱۵۴ هزار کلاس‌اولی
🔹
آموزش‌وپرورش: امسال یک میلیون و ۱۵۴ هزار دانش‌آموز کلاس اولی وارد مدرسه می‌شوند و جشن شکوفه‌ها، مطابق رسم هر سال، پیش از آغاز رسمی فعالیت سایر پایه‌های تحصیلی در سراسر کشور برگزار خواهد شد.
🔹
تمهیدات لازم برای بازگشایی مدارس اندیشیده شده و آموزش در همۀ دوره‌ها و مقاطع تحصیلی به‌صورت حضوری آغاز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462915" target="_blank">📅 06:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462914">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ub7Frn_yh6cAblLcT0f5hhjJpA8Qj1NujyS3cwxG-5lsUHXf4sKasxMcU2j_FYqpXeWoI6OEt6kc8HhyCeRo3x1JmSdJTNsCH-KOSgNV1psXQY8PiKl18vGVQFxzJfN0Z-wJv1v-IGfvelG-1U1QejPxgfnm6VRPNyqrZeF0Cmak-qJPT-mCDznog3YuChKtfPVzz0ZMBRHURd16BTOdwb04pJQZRo_H4j5UJLS5KERZCIB8iP0p2aOzcuBTIdz_TLW5KAj4ytqaoVWYgcZLq07KR5YLkWTs8NGii_PSjZJfsxa2CzEpTAFNleyoFlRtRYIdpv8qXXCvP42aGTC94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مغز ربات‌ها در آستانۀ جهشی بزرگ
یک شرکت چینی فعال در حوزۀ هوش مصنوعی تجسم‌یافته می‌گوید ربات‌های انسان‌نما ممکن است تا اواسط ۲۰۲۷ به نقطه‌ای برسند که بتوانند دستورهای طبیعی انسان را بفهمند و برای اجرای آن‌ها مجموعه‌ای از اقدامات فیزیکی را انجام دهند.
🔹
«اسپیریت اِی‌آی» اکنون ربات‌هایی دارد که در خطوط تولید شرکت‌هایی مانند «سی‌ای‌تی‌ال» و «جی‌دی‌دات‌کام» فعالیت می‌کنند و نرخ موفقیت آن‌ها در برخی وظایف ساده و ساختاریافته به ۹۰ درصد رسیده است.
🔹
اما ورود ربات‌ها به خانه همچنان فاصله زیادی دارد؛ چراکه محیط خانگی بسیار متنوع‌تر و غیرقابل‌پیش‌بینی‌تر از کارخانه است و به داده‌های بسیار بیشتری برای آموزش ربات‌ها نیاز دارد.
🔹
این شرکت برای جمع‌آوری داده، حدود هزار نیروی قراردادی را به تجهیزات ثبت حرکت مجهز کرده تا کارهایی مانند بازکردن یخچال، بازکردن قفل و آماده‌سازی مواد غذایی را در محیط واقعی تکرار کنند.
🔹
به گفتۀ مدیر شرکت، سخت‌افزار ربات‌ها با سرعت زیادی پیشرفت کرده، اما «مغز ربات» همچنان ضعیف‌ترین حلقۀ زنجیرۀ رباتیک است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462914" target="_blank">📅 06:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462913">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آمریکا با فروش ۲.۷ میلیارد دلاری تجهیزات پدافندی به اوکراین موافقت کرد
🔹
وزارت خارجۀ آمریکا با فروش تجهیزات و خدمات نظامی به ارزش ۲.۷ میلیارد دلار به اوکراین با هدف توسعه و ارتقای توانمندی‌های دفاع هوایی این کشور موافقت کرد.
🔹
به گزارش رویترز، این قرارداد بخشی از همکاری‌های نظامی واشنگتن و کی‌یف است و بر توسعه و به‌روزرسانی سامانه‌های دفاع هوایی اوکراین تمرکز دارد.
🔹
با این حال از زمان تأیید وزارت خارجۀ آمریکا تا تحویل تجهیزات به اوکراین، ممکن است ماه‌ها و شاید سال‌ها طول بکشد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462913" target="_blank">📅 05:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462911">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMZa_dOkfXTXcsow0yk0dVn4mexj5UanD_qqi7pWlCYe0oH-jvJPJPGmqulE2jtX9u_cDU57eNhwFSidOm8-RbxC-ttAKXEVa2h11LD2gJ1BR6asWtu9r_PGMx_ratYrelAssaVqsj6dmbsGZywolYeWDAhFCMi7Pg9AZpDy0jrQZX4fhD9GojYVAhc7EtnuCjRhU65rxlPzN4IRTfODhOZo68P3dYE6mWRTdf01MF2WDMdg8bEGMyoioDUk2mr6K85YvLUC7W-rSOi0aEASZVoR964ZHhgdehDBO4XVdSoyD2w62QyPBbLTF_J8ExAzuC6x6t11uO65m6A9uYitbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAfsDcqazWUU4lf8uZ1k6JLHylvaq-3p3Yb3kXhZtM2cbmWKHAaTrsXCC1uqg-BbENgGILypHikQt9hKVFxRG7JUznBB1pgcVkVifkJLFemUMVpbWdG-gcc2lX-FtT2cbphH2eq8tP3_3INAAZkuAfLXglBhYOpf5soRJkkA3bnFnOdIxA3maLC3_uyrIkRxjJdeD96GquBMHrCYRMFHc0VSQzB2WKsAQxmv0NI4hgQc0JBU9wTYE3KmyMOuFChQUL-emC4mNBKTZVEfiBcwQRmwEvfqolbGPb7szcaZC8PGuknRpIdML37XD4kx7Qx9qcSG28x71CVla5vkDKLtig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همدستی انگلیس در جنایات آمریکا علیه ایران
🔹
فعالان ضدجنگ در انگلیس با تجمع مقابل پایگاه هوایی فیرفورد، تاکید کردند که لندن با فراهم‌کردن زیرساخت نظامی برای حملات آمریکا علیه ایران، در معرض اتهام همدستی در جنایات جنگی قرار گرفته است.
🔹
صدها نفر از فعالان ضدجنگ می‌گویند بمب‌افکن‌های آمریکایی از پایگاه فیرفورد برای انجام عملیات علیه ایران استفاده کرده‌اند و بنابراین نقش لندن در این جنگ فراتر از حمایت سیاسی است.
🔹
به گفتۀ آن‌ها، زمانی که هواپیماهای نظامی از خاک انگلیس برخاسته و به ایران حمله می‌کنند، لندن عملاً در این جنگ مشارکت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462911" target="_blank">📅 04:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462910">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/513f35c074.mp4?token=tHMhV_819MvyLjub-HmVPg-6Co-E1EKe_e50dTn-5x-zpVCUXEDrL4vqGH8tx52hahkgBlRS8p45jN9JLr4xE9Qn_nAxWcg1OkLaYpvD4ealEQ-zFPHCQScECFQQCImSm2Y8-gunRkPigS-2Fr4LRZjzQQhbEyjNY65fJLP8mmPlWQk0LFiDnVWla5Iw0gLD1c4Ez_HM9bXzMVAQqRBVBZA44_My6O1uDRd5duLf6yeVMa8_MCYaNSczCxpGRg6DfgqA-412qDPv4Sq9LrTaIX1sXjnJ9aK4cZb1TxN-3LTeZ32JKI4UI-omFYoREnMOVartsxOHxDeOeVnKWSG1DYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/513f35c074.mp4?token=tHMhV_819MvyLjub-HmVPg-6Co-E1EKe_e50dTn-5x-zpVCUXEDrL4vqGH8tx52hahkgBlRS8p45jN9JLr4xE9Qn_nAxWcg1OkLaYpvD4ealEQ-zFPHCQScECFQQCImSm2Y8-gunRkPigS-2Fr4LRZjzQQhbEyjNY65fJLP8mmPlWQk0LFiDnVWla5Iw0gLD1c4Ez_HM9bXzMVAQqRBVBZA44_My6O1uDRd5duLf6yeVMa8_MCYaNSczCxpGRg6DfgqA-412qDPv4Sq9LrTaIX1sXjnJ9aK4cZb1TxN-3LTeZ32JKI4UI-omFYoREnMOVartsxOHxDeOeVnKWSG1DYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایمانت ایراد دارد اگر یادش در دلت نباشد
🎙
حجت‌الاسلام کاشانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462910" target="_blank">📅 04:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462909">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9375f31c39.mp4?token=qKZPaOgMk6j0yD0dYHQjFIM2NYG229XYQ69PCE-fMYwzzNoeQvRy-2sogzWnyoaA2H7oCxXK40RXBGmqgIuo7l3IALKQJ--yTst32kMZFHqAXdiJU-F2PE2QWOsVfXGcMghlcH1MgwGnpfgseDibrDi5jpsEbxmNVdHhURlgv7932ckQ44GUiAt82ptaMtsYkA3wsTVLVRr9bLv5uNItqTWNffYIys_U_uzQsz9Iz3iE62xhYk8s2xKGdMVZvyVKPOLxG5bEp_25rtY3ywu1-78dMAv0FP_IAlGEW6ovK0-GOhlYgBwKyWjvn3TrYCEMcm_4GX3409SRDGniecsA_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9375f31c39.mp4?token=qKZPaOgMk6j0yD0dYHQjFIM2NYG229XYQ69PCE-fMYwzzNoeQvRy-2sogzWnyoaA2H7oCxXK40RXBGmqgIuo7l3IALKQJ--yTst32kMZFHqAXdiJU-F2PE2QWOsVfXGcMghlcH1MgwGnpfgseDibrDi5jpsEbxmNVdHhURlgv7932ckQ44GUiAt82ptaMtsYkA3wsTVLVRr9bLv5uNItqTWNffYIys_U_uzQsz9Iz3iE62xhYk8s2xKGdMVZvyVKPOLxG5bEp_25rtY3ywu1-78dMAv0FP_IAlGEW6ovK0-GOhlYgBwKyWjvn3TrYCEMcm_4GX3409SRDGniecsA_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدئوی منتسب به موشک یمنی در آسمان شهر ریاض  @FarsNewsInt</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462909" target="_blank">📅 04:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462908">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d160a38e6.mp4?token=YzR71sgjM7Dr2cGE_U49R2IbIPJ8AvMN2o3oUh0yEQ1mB4bpdZf4n6x9N-uMm9Y4jrtFP9OxIwTIeqxhfeK_XWGoJV4d2weXymSVajoY4XccELwH1PwKsTj-J1EfflD8Q1NvN2vQZX2DuahcFQyfKBNLHecmo4K70VPfCJv2tuhiwTOoNscwE_cDJftlfaCbiRp0LqiVqyZCUezjv5ucp9eukcdYmq-75d1JVwFbQEQ6HRyniODL4gKljK4p3sbCVF7XFBkC-BrQUwxmbTAjV8yWZxFdybaVmRThS96PPWQhot2chnzvDMx907A1DNtPHVUIIIKG9HACpQhInpAXOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d160a38e6.mp4?token=YzR71sgjM7Dr2cGE_U49R2IbIPJ8AvMN2o3oUh0yEQ1mB4bpdZf4n6x9N-uMm9Y4jrtFP9OxIwTIeqxhfeK_XWGoJV4d2weXymSVajoY4XccELwH1PwKsTj-J1EfflD8Q1NvN2vQZX2DuahcFQyfKBNLHecmo4K70VPfCJv2tuhiwTOoNscwE_cDJftlfaCbiRp0LqiVqyZCUezjv5ucp9eukcdYmq-75d1JVwFbQEQ6HRyniODL4gKljK4p3sbCVF7XFBkC-BrQUwxmbTAjV8yWZxFdybaVmRThS96PPWQhot2chnzvDMx907A1DNtPHVUIIIKG9HACpQhInpAXOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدئوی منتسب به موشک یمنی در آسمان شهر ریاض
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/462908" target="_blank">📅 03:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462907">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حملۀ موشکی یمن به ریاض، پایتخت عربستان
🔹
سازمان دفاع مدنی عربستان، در دو شهر ریاض و الخرج هشدار امنیتی صادر کرد.
🔹
منابع عربی از شلیک موشک از یمن به سمت این شهرها خبر داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462907" target="_blank">📅 03:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462906">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOUb3zb4dN89Z9LdA6b4_VcGS2ubLSVShIc09uyZgCSQgHwBPpvFBd2oqm8YndIsodP5qkNdQb2WbrZicBvgMexiZ-3C6t42YWZ7WK8tHXFvsqRe4KHoOVMktmrJVQCFSDEmB6evF3lDWyawvyP-EuVuSB48N72QqDrTLSNm_4Q1r-tRvahuLT6PjlSQZOv8M0guz4pLJLysBD5wTmPCn_EUHWOU8In1yMqHb9w60Zp512fUWHJxK98qcvZRYQFo0Ua_19pEtlOBwolLczioO8K5G7Prvwti1_CRqBw1qas28phGKU0uhnAEPBGerb6LskyWgn7ERfLsJItzi6mzWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۴ خبر خوب از اقتصاد، فرهنگ، زیرساخت و فناوری  زیر ساخت و خدمات عمومی
🔸
داراب و زرین‌دشت با افتتاح ۱۴ طرح کلان برق، پایداری شبکه و ظرفیت تولید انرژی پاک را تقویت کردند
🔸
سازمان غذا و دارو سامانه هوشمند پشتیبانی داروخانه‌ها را راه‌اندازی کرد و ثبت و پیگیری…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462906" target="_blank">📅 03:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462905">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdVEpEkcGry-_8ECyTWBY04XtKTSnjNLUW94sDc9wdaFP5hUAYKHUoFYcVRAGkDQsdlIjxIGO3hxjYdAGPsJTvNjEaDDwhG2HSwSYIGqN1Oly1AN-PxHrH933OMLxuK2BeqbEFacb7m12faDckxCLYZPA05dv6IUYADky4tucE7zyrU6A85vs-V_QnsAhCAwqIL4z7CorSK5LiI6o8-jgCJxVgq9QiL_KVBSbVHMuUAXp7DEXpVf0Yj4J98uFBaWrMZV6kgQKLo6q55SfBvmQ2m5w3Va4MJUaLo6ejY6krG9damqZvEDK8rjEeIFNO1ZKVwVVV8wnH14ySJsTYjrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار گردشگران ورودی و خروجی ایران در بهار امسال
🔹
آمار وزارت میراث فرهنگی و گردشگری نشان می‌دهد در بهار امسال، ۹۲۸ هزار و ۷۴۶ گردشگر وارد ایران شده‌ و در مقابل، ۲ میلیون و ۸۵۵ هزار و ۱۴۶ گردشگر نیز از کشور خارج شده‌اند.
🔹
طبق آمار منتشر شده، عراق مبدأ و مقصد اصلی گردشگران بوده است.
عکس: امیرحسین ترکمن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/462905" target="_blank">📅 02:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462904">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLMfgaZK3psKFfO9zQh8BDnz329x6EC-iKC1FsDWDWtfV4zLf9hNvhqxVR1uucNW7pFIlysoAb5jb5D5cOgRbkvuGSWK3HrXoW8ZvslFLJJCl9i09mU86MuAR-2oTzYJQxgOFipHMUJPfJv3eCC7siMszjLH954mLV3iXJ7RePP5CjJdmyRvnxoRNPaLEia8jlF8oCzhpQiFK2BPSjxX7APoSBL-X9JvGxnFBneXv1Voel1KTd0CP7zpveehHqNu6X--NhUeMH0RIASQn_guNlpwbCh8O2xLxyH4IyNHSqRrDoxdjYATBxiPfT14AO7TZOeQ-tU34V8utaDU_jixbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات رژیم صهیونیستی به جنوب لبنان
🔹
ارتش اشغالگر اسرائیل، اطراف شهرک القنطره و كفرتبنيت در جنوب لبنان را مورد حملات هوایی و توپخانه‌ای قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462904" target="_blank">📅 02:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462903">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I86Pr8uq4aopeug42Tx47uzSKvTQKXUaVnxG7hLvQRxTH8hs2khtdzgKsnWT_TnLCdZQErhEVBMCKedAs1-2I0R8jpYxHwJ4eKwI_q3cbpd8aSaB3USq6nI1I3BklPBa3Wzfm-VVGtmC1s38IabRyVaFqiKGErwpVgl5UTcLiJ4eX1EB_96zrtAi6ClIuerApyT-KSy6GwNmZYtFhwow9KLsuFJqADpo0h45OCugXZEtvlQ7cRd6N9H8coDjVSJBJQRmzgoQJBsJsqyQ4kzhevTT-NAZz42w_fisIIrq_tsm2PnxSdd9lRYLN5XHme_yeQoUZYS01dV4mI4m2Za0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: گرینلند تا ۲۰۲۹ مال ماست!
🔹
رئیس‌جمهور آمریکا که از بدو ورود به کاخ سفید به‌دنبال تصاحب مناطق مختلف جهان بوده، این‌بار گفته که گرینلند دانمارک را پیش‌از پایان دوران ریاست‌جمهوری‌اش تحت‌کنترل آمریکا درخواهد آورد.
🔹
ترامپ در یک مصاحبهٔ تلفنی گفت: «مردم…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/462903" target="_blank">📅 01:38 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
