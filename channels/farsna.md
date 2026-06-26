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
<img src="https://cdn4.telesco.pe/file/Qw8e_ZfkHvuaHQ1gHi0CWP0Pb0srIIKUEt51aOXDHZhCODLZKFtDKyfbq9_QjiNDkVNGFeX8vCuWT55o-zIHGi7q7y8iNaTwX1mMlwRvLjw26yu-XLo2m3VTBaL9QOJvGTzFL4zspsofWcyQtlY0wWOC2WFeH4e42o5KVzUpwfPqNHzAN1qM5dLnKA9rWwTx_GMHyiaJu1ctaimIdSUTCdrmk9mL-OtD8Vq281Z8IFhP-tIqN5-ZodlwMLxhTeqcGvmlkFc-NLhIJaaPlxEPj6miySu2VHcmEYIb0gllacCc4I2goVuUEyQ21Tf0Z_LRbiIh6vemPA6JMrGtkbd8tA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 18:41:18</div>
<hr>

<div class="tg-post" id="msg-444898">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/farsna/444898" target="_blank">📅 18:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444897">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6f03fe18.mp4?token=t0USu9qv4zSXh9C1-I8TJ0kmfSRJqSpodFbRql5MwwwdMS4_rWAMPcvwpybXgtCvav9PISbpkUDf4TW-Kq__pPXdBWlwVGQlWPzlKTRbZ1mZuAVREm4miRxsJXpERYiE8ugyyt6fdu_9lK9-otRpPv5WMz_N-DOSNVZFoiWoY5RVYt975Y_BxzMLsDGXB2_NKWjtzntnhP81voiYFjFKcTgPGcktZsHgCcOH4jFnPysG_MU3P6E1pJlaH6EfEm2zn9M6CdtLETTYeLq7fty4PMzI3VQRSs7iLJlzqvT3QtQ4p5ptodV6GgDZnA8QYR0LywIzYpRQYrr_kvZM-gerkG3EU5cwPGz3OijS1Vw8ZgTCzrTNhnL0PNbxHkigmr8d3uwld9y3O4WVBEml6UgiH4AKcQwE1WBBz7GHfQ8B4hQIf0b8Xwi8cC00AJYHF2Oc9XstbuT6lu9zi63MuiAATKUvcB2HxGMzzwjG9P0RmL-0z_nJROdvRkaYAV5_-PK7Ss_AdyjDAd_R4cG7fETqll13VdaZrogNgxp5ZA_aZPdeQmHGn_f6mwWEL0dFL6kqVhFZHcEaQcxL3kH-WuS-s7ILwImxEOgc5Yr_pZsOG-rghJbVeDVhnTeJMd95Tgt4RwKq_YRF-3Gwgt37shtnywNQqCnkqCqQQi00LB-PLMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6f03fe18.mp4?token=t0USu9qv4zSXh9C1-I8TJ0kmfSRJqSpodFbRql5MwwwdMS4_rWAMPcvwpybXgtCvav9PISbpkUDf4TW-Kq__pPXdBWlwVGQlWPzlKTRbZ1mZuAVREm4miRxsJXpERYiE8ugyyt6fdu_9lK9-otRpPv5WMz_N-DOSNVZFoiWoY5RVYt975Y_BxzMLsDGXB2_NKWjtzntnhP81voiYFjFKcTgPGcktZsHgCcOH4jFnPysG_MU3P6E1pJlaH6EfEm2zn9M6CdtLETTYeLq7fty4PMzI3VQRSs7iLJlzqvT3QtQ4p5ptodV6GgDZnA8QYR0LywIzYpRQYrr_kvZM-gerkG3EU5cwPGz3OijS1Vw8ZgTCzrTNhnL0PNbxHkigmr8d3uwld9y3O4WVBEml6UgiH4AKcQwE1WBBz7GHfQ8B4hQIf0b8Xwi8cC00AJYHF2Oc9XstbuT6lu9zi63MuiAATKUvcB2HxGMzzwjG9P0RmL-0z_nJROdvRkaYAV5_-PK7Ss_AdyjDAd_R4cG7fETqll13VdaZrogNgxp5ZA_aZPdeQmHGn_f6mwWEL0dFL6kqVhFZHcEaQcxL3kH-WuS-s7ILwImxEOgc5Yr_pZsOG-rghJbVeDVhnTeJMd95Tgt4RwKq_YRF-3Gwgt37shtnywNQqCnkqCqQQi00LB-PLMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان دلدادگان زینب(س) در زنجان به حرکت درآمد  @Farsna - Link</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/farsna/444897" target="_blank">📅 18:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444895">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5615887ffc.mp4?token=HK4GY5ZtAsoCcEiTfs6Adipma7L9CdDnB94KauSSeTIYegkTDzaeTtJ8WEOOXwC20E77dzEgHxEanFdCIbSyzE5_oGlJX2oghRQE8Tht93rp5AZ6mFGDC5Rb-bJilRAxiDKJs769KLr_2mzwEGMhjp7a0-PA3RkFqNS-9zmFXDxXptY7lr_FPmDOoRm492fhuzcKy-1o-fYmTSWX9l78QaLVoKixU244gS_NW7AlgLhSgV--2gbXs0BSndPXTm0Bi5sIzHX9lb92tAQ6h71wRu0YDb3lMPwG72vRTQ9uCT58n0GmCeAhCz-mxHRMhBwfoEQKF51LxMwPe8A-d6EGTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5615887ffc.mp4?token=HK4GY5ZtAsoCcEiTfs6Adipma7L9CdDnB94KauSSeTIYegkTDzaeTtJ8WEOOXwC20E77dzEgHxEanFdCIbSyzE5_oGlJX2oghRQE8Tht93rp5AZ6mFGDC5Rb-bJilRAxiDKJs769KLr_2mzwEGMhjp7a0-PA3RkFqNS-9zmFXDxXptY7lr_FPmDOoRm492fhuzcKy-1o-fYmTSWX9l78QaLVoKixU244gS_NW7AlgLhSgV--2gbXs0BSndPXTm0Bi5sIzHX9lb92tAQ6h71wRu0YDb3lMPwG72vRTQ9uCT58n0GmCeAhCz-mxHRMhBwfoEQKF51LxMwPe8A-d6EGTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع جنازه‌ای که توطئه علیه حماس را خنثی کرد
🔹
تشییع پیکر برادرزادۀ شهید اسماعیل هنیه با حضور گسترده مردم غزه در حالی برگزار شد که جریانی مشکوک از هفته‌ها پیش فراخوان تجمع علیه حماس را صادر کرده بود.
🔹
هزاران تن از اهالی غزه امروز در شهر غزه، پیکر «ولید مجدی هنیه» را تشییع کردند؛ وی بر اثر جراحاتی که در حمله اسرائیل به اطراف مجتمع مسکونی ایتالیایی در محله النصر در غرب شهر غزه برداشته بود، به شهادت رسید.
🔹
اما نکته قابل توجه همزمانی تشییع پیکر این شهید با روز موعود مخالفان حماس در غزه بود، جریان مشکوکی به نام جنبش ۲۶ ژوئن از هفته‌ها پیش از اهالی غزه خواسته بود تا امروز به خیابان‌ها آمده و علیه حماس شعار داده و تجمع کنند.
🔹
با این حال امروز هیچ خبری از حرکت علیه حماس در غزه نبود و برعکس فضای این منطقه با تشییع پیکر این شهید کاملا همسو با حماس پیش رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/farsna/444895" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444894">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3aa5894fc.mp4?token=sAeNbKmOj40V4h29cz8_rc1jMpIejSs1KKSIF_zHN6DphFQa6uDJiVZgHBMpWs5B8XyY-k3l5LBXchlv58nclLWm2Jsedc_NLF91T-1mVGCaWLjBxAqBriNeQxT3lKhZavbvWFDCNeKMG8ydeQWtHCgPY-0zzLvNiZI1-lPdNRufGfp3j8fmLeo50cBG0v3HHE-SJNH_D9QvPvNKgLfwnm7m-ojMOSO364fr8mE8dDzm0WYSHgUpl4xb25KHPa9PqoASshWGXu8ByCuGXar-KBgymuOla9RnmeXTIKzLROgg7-p4LB5-5Y90rlEpuyBqlz1VOKkoFpzMwdlCib-6Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3aa5894fc.mp4?token=sAeNbKmOj40V4h29cz8_rc1jMpIejSs1KKSIF_zHN6DphFQa6uDJiVZgHBMpWs5B8XyY-k3l5LBXchlv58nclLWm2Jsedc_NLF91T-1mVGCaWLjBxAqBriNeQxT3lKhZavbvWFDCNeKMG8ydeQWtHCgPY-0zzLvNiZI1-lPdNRufGfp3j8fmLeo50cBG0v3HHE-SJNH_D9QvPvNKgLfwnm7m-ojMOSO364fr8mE8dDzm0WYSHgUpl4xb25KHPa9PqoASshWGXu8ByCuGXar-KBgymuOla9RnmeXTIKzLROgg7-p4LB5-5Y90rlEpuyBqlz1VOKkoFpzMwdlCib-6Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخل‌گردانی ۱۱ محرم در شاهرود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farsna/444894" target="_blank">📅 18:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444893">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترافیک پرحجم در آزادراه‌های استان قزوین
🔹
پلیس‌راه قزوین: با پایان تعطیلات ۳ روزه، ترافیک در محورهای آزادراهی قزوین-رشت، قزوین-کرج و قزوین-زنجان پرحجم و در برخی مقاطع نیمه سنگین بوده و پیش‌بینی می‌شود ترافیک در عصر تشدید شود و تا پاسی از شب ادامه ادامه داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/444893" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444892">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
۲۲ ملوان ایرانی پس از رهایی از دست ارتش آمریکا وارد پاکستان شدند
🔹
وزیر خارجه پاکستان خبر که ۲۲ تن از خدمه کشتی‌های ایرانی ربوده شده توسط آمریکا وارد کراچی شده‌اند تا پس از آن به میهن خود بازگردند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/444892" target="_blank">📅 18:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444891">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meD7wvACSxVaOrfBYAMvrMFcmBgT9jIp52coBbcVJReDF10KxGxUoOvDHRpesjfFNJBXOtqG3pnGtoW-XzvdoYcX-cDUfKqdGYTDE3kYbVv9UgZiqrXnrEADAfIdpOzDelO0wTg07jZiLclc-EAJKpBlIKlI6p_oRXIy9PCKeN_PGpVuKnh-Dz_fwx_GcQIKA7cdB-jilANrdIaGJiVzgXuhN6OSsYVuUx6xmyD-L3y0gCIo-1xiTp4YX6Z_WZUhLDpwjZH9owAxoeik0yu77dqV55Dd2bYdyuUNmH96N9DoMtrU_fb6kA999MT8Zc1ZbO1NznnL6fi-G_PFfI1hEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ایران ـ مصر فعالیت ادارات در برخی استان‌ها را به تأخیر انداخت
🔹
با اعلام استانداری‌ها تاکنون، ادارات استان‌های
کردستان
،
قزوین
،
فارس
،
سمنان
،
گلستان
،
یزد
،
مرکزی
،
خوزستان
،
کرمان
،
مازنداران
،
زنجان
و
آذربایجان‌شرقی
فردا با حداقل ۲ ساعت تاخیر شروع به‌کار خواهند کرد.
🔸
تیم ملی کشورمان ۶:۳۰ صبح شنبه در مرحلۀ گروهی جام‌جهانی فوتبال به مصاف مصر خواهد رفت.
@Farsna</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/444891" target="_blank">📅 17:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444890">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01c0ca6b8c.mp4?token=CkX9mompbGBpf5LNem3G0sTQGqTplRpaTBnI8RO3CppxmI0eDNfIdqmDiHT8qLEBu2nTyVM_0ewFjBcCIlL_T6dMY___AkYPP3NCj-L7q57BQAL41HLqLh6o2RH23D8aX9Ga43KGxA0PFpVegxp7TgPgIvbUHwhEC9zMZdAYXgs9mYzj16Z3CRefqpviHtr01rUGrq5vCDUqfESlp8F4BI768MIOTsRtaP0AWi0gqXa0h-k40QvO7GVci7XifwEA_Dpe1zn_6h7Sed33B3Mj_A40VKVrtKE6QiZHEXM8FsDem9frZ9mEbT4VcgeInwxboICD0Fs6JsDeF7SSchexb3WS-E0CoSQ9HdgCr-vKLcoETixXH7xMoRvGi-80sqU3G2ijfT3Q4OH8yJQLZioMJ3eJIVCUB4lzVB9LILtxB2C-UqvPgfpfZfJSK41pdkWS1O4JxHMp4kEh6kg4LW6thIXGNZMr2_Yix7OMas7udgPWAFZIweV47OfXchNgVbaYWZSzkEuvIS9WUjAI19vzarMtl4J8cpQfTUDvY-WFq3mO5-hrTWB0zDQrsnrU1gLPLjK2WV82cEgHstX3LG0EFMiBz7Zm7F-WgfOBtjZvVVbLbe12WYJ9EbsRXtHeegIlDidRdL9qqGCQm32qdQt6ZLTJeR0wjGMB6Eo92v0YwLM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01c0ca6b8c.mp4?token=CkX9mompbGBpf5LNem3G0sTQGqTplRpaTBnI8RO3CppxmI0eDNfIdqmDiHT8qLEBu2nTyVM_0ewFjBcCIlL_T6dMY___AkYPP3NCj-L7q57BQAL41HLqLh6o2RH23D8aX9Ga43KGxA0PFpVegxp7TgPgIvbUHwhEC9zMZdAYXgs9mYzj16Z3CRefqpviHtr01rUGrq5vCDUqfESlp8F4BI768MIOTsRtaP0AWi0gqXa0h-k40QvO7GVci7XifwEA_Dpe1zn_6h7Sed33B3Mj_A40VKVrtKE6QiZHEXM8FsDem9frZ9mEbT4VcgeInwxboICD0Fs6JsDeF7SSchexb3WS-E0CoSQ9HdgCr-vKLcoETixXH7xMoRvGi-80sqU3G2ijfT3Q4OH8yJQLZioMJ3eJIVCUB4lzVB9LILtxB2C-UqvPgfpfZfJSK41pdkWS1O4JxHMp4kEh6kg4LW6thIXGNZMr2_Yix7OMas7udgPWAFZIweV47OfXchNgVbaYWZSzkEuvIS9WUjAI19vzarMtl4J8cpQfTUDvY-WFq3mO5-hrTWB0zDQrsnrU1gLPLjK2WV82cEgHstX3LG0EFMiBz7Zm7F-WgfOBtjZvVVbLbe12WYJ9EbsRXtHeegIlDidRdL9qqGCQm32qdQt6ZLTJeR0wjGMB6Eo92v0YwLM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان دلدادگان زینب(س) در زنجان به حرکت درآمد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/444890" target="_blank">📅 17:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444889">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcdOz31jWIOGBSRN_Luwdez1IPFQr6OGgLvTDLSyvHZdxHRFmB6FnqsL8ElNqrKjEHCiTSXn2h_QkdTSg2QCos6r0j0gmHte-wcgn9wgoNcsS29Rig4L85TODACmKAdcVJUJankC7Egrjzlr1ZoRJ3j4B9w6hbg3eDXAo7PePud3S75upMPWPKj820DABofUKgtKafi9gzrLaO0iwUUp5TBqfYtH26_5q0OXc-AgDfxg6v1xGI9Qtg_Rqnpp8E8bBo0jdzQD5YQW24vaw35vcmXzwl92P0MFPdRVDO4VIWk5-tgKNKje7FMqOOcmGKyossF1cMlwuNilwaD5tAuVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸ مدال جهانی و جام بهترین تیم برای موی تای ایران
🔹
تیم ملی موی‌تای ایران در پایان رقابت‌های قهرمانی جهان ۲۰۲۶ مالزی، با کسب ۲ مدال نقره و ۶ مدال برنز به کار خود پایان داد.
🔹
همچنین تیم ملی بانوان ایران به دلیل عملکرد موفق خود، عنوان بهترین تیم مسابقات را به دست آورد و کاپ این بخش را از آن خود کرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/444889" target="_blank">📅 17:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444888">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkD-1RwD-bI3Jl8A1pjzReVJh5J3nK9mAZ3-u7KEMPsna0kG50Yy9AcsN6eq_hlCNwgbnS3XRDkprcqzpc6947J8V4DNtMJ2xzQAg4QMnMEN-7u6rbsFhB35D-idB1mnqyND-BtFlZPkOm_IUQKDAWvYkoQLznsTwTjQjnX5JyskXIM3yNNK4HbIWPx0ZdosnPEKLqj5hoP9juU8lV_ThJO9fe0fMGzpSnD6cMzUDc1Vo7PQRRg6ndglZoyRyN840IdLcDiN2g0jUeOs82WlQppH5OE11878uvauAwZkzp9TTLmilvTP4ey4ApDLfKW9_XpoipERDUTgB9gafL_Ezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار وزش باد شدید در تهران از عصر شنبه
🔹
هواشناسی استان تهران: از عصر فردا تا یکشنبه، وزش باد شدید در استان تهران به ویژه در نیمۀ جنوبی و غربی پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/444888" target="_blank">📅 17:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444887">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1VP2BYV1W88mM-4sGyK2_y0ZGhpmLegB6qzin5Ww1JAE3OrFVIPJ7HYCljdKCQ1TISfzs1M3CXrRVP2Z0-kLac_ZhvKfCAgmPqprvwcJkaLvgB0nZBqm0vVNDuvvX-QIIrFTbvAOUfgmqYDwUA7B_2FDPDuF_RxZ2q_T4VABuINfbPVfZU9MmFXpNaG9sh2KaCElYIugwZ632ywkaHN8hlDY1UjFydUzLQ0ZaQgIgA1mIVm2HBRyHAvRoqrkL9ipmAnOPj9ekeOpOqcJc-XvrmkJ6N0CVeSpVXz4nNj0-Sx4jdFW7RuvWG6-Ep02taCAXQE-InlMKKX78QiDNEfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آینده هوش مصنوعی بیش از کد، به مس نیاز دارد
🔹
وقتی قیمت فولاد افزایش پیدا می‌کند، اثر آن به سرعت در صنایع ساختمان، زیرساخت و مسکن دیده می‌شود. فلزاتی مانند مس، نقره، لیتیوم، نیکل، کبالت و عناصر خاکی کمیاب، نقشی مشابه فولاد را در فناوری‌های پیشرفته مانند هوش مصنوعی یا خودروهای الکتریکی دارند.
🔹
نوسان قیمت یا اختلال در عرضه این فلزات، به‌ویژه مس، می‌تواند بازار فناوری را تحت تأثیر قرار دهد. تحولات ماه‌ها و هفته‌های اخیر بازار مس نشان می‌دهد نگرانی از رکود اقتصادی و نرخ بهره بالا قیمت‌ها را تحت فشار قرار می‌دهد. از سوی دیگر، موجودی انبارهای بازار مس کاهش یافته و بسیاری از پیش‌بینی‌ها از کمبود عرضه مس خبر می‌دهند.
🔹
بر این اساس، ممکن است توسعه روزافزون بخش زیرساخت در شبکه‌های برق یا فناوری‌های مراکز داده و هوش مصنوعی در بلندمدت، کمبود عرضه را جدی می‌کند و در نهایت به کند شدن یا گران شدن توسعه فناوری‌هایی مانند مراکز داده، خودروهای برقی و زیرساخت‌های انرژی نو بیانجامد.
جزئیات بیشتر را از
اینجا
بخوانید.
@FarsnaTech</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/444887" target="_blank">📅 17:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444886">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWqWfEj68MA54DYXmw04DIYdreSedqMk1FhdQNLz_tYemGnUUB_NPJsy1JNISodKsUrmXUF_L0doJjg2PwQnVHKFbLT5vYgs22p5GJiyvdO0bRZNTDZ45KqBnCNa6ccsb5AqXr4REP8Q9fpr0xGhif6nEu2c-XhIaP_xdai4NXSgIhw_Yc2YTDFb6m2pVBcDub-GO9wSZH_OI7_m1Sz3wdl2GWmGVQDEV_-L7L56yFDgEpPc51HlL0JjgmUVkRmmduvTQ37Lhs7kGTjVnDJckqqb26yo7FKW0NIBWIUWKOrlJz9xuvenBrzwmwSpHGFaVSC_O0vLn-IoIsz-6NV0hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار حمله موشکی در دبی صادر شد
🔹
وزارت کشور امارات با صدور هشدار حمله موشکی از طریق تلفن همراه، از شهروندان این کشور خواست تا در مکان‌های امن قرار گرفته و از پنجره‌ها فاصله بگیرند  @FarsNewsInt</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/444886" target="_blank">📅 17:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444885">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN9EUEyQKs2CSFc9Kz9r-8LVfBeppF4wR4QQbCSgGuRKmoT17nnssMg8Tok8I_KZEvRnAbNOZ9-Y24gF8T7YSNe8SJ2u5LMPghOWMr6HgZiYPMJDwMZdF5XcH9san_yqLbjOD0wPJrNyrb6OsljjFyBpChoyb86M_Z5YNK9mIC9brk7BuI-BnQ1-C0V8xlVqAkN_3WRqMyOb4aYFlhO7JuXXYJ1sXI5CTEfsPMBl57j3j4u5uhEbe2VUN9jVcnIqIZ07xl88P6EkpQk7XwPQVPzeNeHc_Q4a19ASIHjDr80KjoQLPfhSjpvmmLvIWBdmLBhClmQa99pqiZEb4PNn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار حمله موشکی در دبی صادر شد
🔹
وزارت کشور امارات با صدور هشدار حمله موشکی از طریق تلفن همراه، از شهروندان این کشور خواست تا در مکان‌های امن قرار گرفته و از پنجره‌ها فاصله بگیرند
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/444885" target="_blank">📅 16:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444884">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4siNqJddk4i_EL_eSzPPDYhGu1vQAdm8Ta0C_DbRs7UHdzmXfS4mYQ17_HAgznge1fITmLN6VlwpO8Lra3NDav1jf3l2771SnOoTEoa1kY9pFS3A1O79CHnWfBpLyo6Ki-7t8odyhl5wKTZ1PyiVtB5d6sAW0Tr_w4t7SsOQ2pclHqUthOff-JRvL6qFRQcJlODj0WOZn1CiQoqDjy_PnWgn0z0Me7mMJr417J5dwqMjGPkNngWWoQ6t_viMq5MobAEb9_hXT-eGyW2DyUCM24LhIuGL2vZPA820vx79_LfKjCJDNKbTQJbDsU1s2KyvOah7aFLX0lUSm9lLE7_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهای عربی و آمریکا بیانیه مشترکی دربارۀ توافق با ایران صادر کردند
🔹
در این بیانیه آمده: ما از امضای یادداشت تفاهم بین واشنگتن و تهران استقبال می‌کنیم و اهمیت تلاش‌های میانجیگرانه انجام شده توسط پاکستان و قطر را مورد تاکید قرار می‌دهیم.
🔹
ما بر اهمیت حفظ…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/444884" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444883">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc864a17d1.mp4?token=QUDm9eYUE4xgL4DLpt6c6WOWKuSXAjwkQyC8ygw3GIHCKvipAs-ooJ5tFnolPwIeavda0KAU2H81PgCbZNZaEVj7FrVcSYwd7AGo51jgSCqQ9Q9j09J_gsAW3a3s1KCiWzuwQZX-q_rCb2Qk9MdXrED_9qYEtKUs6_ZGFkZidFycfzjdn8hI9aAHJuW1alJEVpaghr76rsgoHfCF39uPdu-037jGZWZp4eXHn4VfpYuArQotyGjKtRzK_M-4Z11TnC8ONCxIK1JlwE2oCIlhHmhGB-Q45r8ZoQpaqLOEINNgB5V0uBoHiEq4L4lvaGohNL3Yhn9gJN2NB6jwhIf79A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc864a17d1.mp4?token=QUDm9eYUE4xgL4DLpt6c6WOWKuSXAjwkQyC8ygw3GIHCKvipAs-ooJ5tFnolPwIeavda0KAU2H81PgCbZNZaEVj7FrVcSYwd7AGo51jgSCqQ9Q9j09J_gsAW3a3s1KCiWzuwQZX-q_rCb2Qk9MdXrED_9qYEtKUs6_ZGFkZidFycfzjdn8hI9aAHJuW1alJEVpaghr76rsgoHfCF39uPdu-037jGZWZp4eXHn4VfpYuArQotyGjKtRzK_M-4Z11TnC8ONCxIK1JlwE2oCIlhHmhGB-Q45r8ZoQpaqLOEINNgB5V0uBoHiEq4L4lvaGohNL3Yhn9gJN2NB6jwhIf79A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شما
پشتوانه‌ی عظیمی به نام "خدا" دارید
@Fars_plus</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/444883" target="_blank">📅 16:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444882">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViPL_BRrGZKm0xdZIQIFF8EVnUyTERn7HqnTQbkcs-0UPjpZ4TbQ-1ox8SRmPhiZEbp1w320q3J1QJ8HskdO_2KmKyKOl4MElPBArW1qIIZvTLkhaX7RTV3M1Aw9UuBbhHPK8RzTVSs6UTMuX98pvmDCDILbvytPahEd7Rj-ufO0poOSJ6BrguvrMEoXZ7zLXE00MmhRYjqLpXW3vQCjlMSG7Wb3VKfH2fpupIc9oJuIF-AbVuDpCw0rd6q9CIibTX0dhqNvLCqV3e6WkbgM6086LfLTEHQBzK1ilUVUR0iE0dD3y7UN4rEtxicMlml1Hn5X5EHC14Zc7u60ROsidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیام عبری سردار قاآنی به صهیونیست‌ها: اگر با پای خودتان از لبنان عقب‌نشینی نکنید حماسهٔ سال ۲۰۰۰ تکرار خواهد شد
🔹
سربازان جنایتکار و تروریست صهیونیست، در کمتر از ۴ روز ۱۰۰ کشته و زخمی دادید! اگر با پای خودتان از جنوب لبنان عقب‌نشینی نکنید، حماسه سال ۲۰۰۰…</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/444882" target="_blank">📅 16:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444881">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
رئیس‌جمهور موقت ونزوئلا از افزایش شمار کشته‌های زلزله و سونامی در این کشور به ۱۶۴ نفر خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/444881" target="_blank">📅 16:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444880">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsXy3t8cw8lyW3uBTpwuvi9dQgYDwqqBEpLsiX573BuT4_-Pz-j1j-dy9GP91e3-1Z5EKC4CkkniVORaaqs3pUJqjrrD9LbukKNc03HYXYXlzZLczV9Fuh63iqdD_XCey7KEDS-_9qxPD6t4J3C_dnY6C1A7WkvRw0Z463CQWoHoZm0FZVHism9ZY2f5q_BlM1QEjEGWazlA7A2gtk-sYVGdAytWkvykC-ZUdViA1xg0Re66hxPPIYo6YCVSnFvC4a1aG22dkSMw7j7mGm4T0WWKPn13NOl7zGC0s0NTdeZaYAPfC7ikc2ugcVaqCYU27iFoMaGVbvCOFt7g51QElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهای عربی و آمریکا بیانیه مشترکی دربارۀ توافق با ایران صادر کردند
🔹
در این بیانیه آمده: ما از امضای یادداشت تفاهم بین واشنگتن و تهران استقبال می‌کنیم و اهمیت تلاش‌های میانجیگرانه انجام شده توسط پاکستان و قطر را مورد تاکید قرار می‌دهیم.
🔹
ما بر اهمیت حفظ…</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/444880" target="_blank">📅 16:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444879">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🎥
تاج: با وجود برخی ناسازگاری‌ها ایرانی‌های آمریکا متحد بودند
🔹
با توجه به ایام سوگواری حضرت عبدالله الحسین، بازیکنان با نمادهای مذهبی مناسب در این مراسم شرکت می‌کنند.
🔹
اتحاد بسیار خوبی میان ایرانی‌های حاضر در اینجا برای حمایت از تیم ملی شکل گرفته است. همان‌طور که در دو بازی قبلی هم دیدید، با وجود تعداد بسیار محدودی از افراد ناسازگار، انبوهی از مردم برای حمایت از تیم ملی به ورزشگاه آمده بودند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/444879" target="_blank">📅 15:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444878">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca429e17b6.mp4?token=CDqHeT1EurMtGNBuKlAUGj-94NpgPwB0lYDxYvCK9LbA7aBnTzrKjOxa2fOTABWlNBg0x8WrmoOGMJGtVnILgPWa-Ej9YzFG4MXnePojFT12ZoOfbzYVay9uG4uoyLkyFCkpnKyZBmqcfylxWVl1Sr6jX6TjQEpCjuLHbzBncAvJl8DE14vv_80I7JjorH5VE43AiToIywJzvqRqbVH_45G2BbLGwQmKxBB50yVz0MzeMFWHfiIqpF5pX2PIUULthSw1G944Fqy6nNHfgkOaFN98UGtOkaaZlKWP0BZfdyM6KqKPC4lL59f4AvpYxdQiO4Z-u2PhyJ5pZYVahO1wLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca429e17b6.mp4?token=CDqHeT1EurMtGNBuKlAUGj-94NpgPwB0lYDxYvCK9LbA7aBnTzrKjOxa2fOTABWlNBg0x8WrmoOGMJGtVnILgPWa-Ej9YzFG4MXnePojFT12ZoOfbzYVay9uG4uoyLkyFCkpnKyZBmqcfylxWVl1Sr6jX6TjQEpCjuLHbzBncAvJl8DE14vv_80I7JjorH5VE43AiToIywJzvqRqbVH_45G2BbLGwQmKxBB50yVz0MzeMFWHfiIqpF5pX2PIUULthSw1G944Fqy6nNHfgkOaFN98UGtOkaaZlKWP0BZfdyM6KqKPC4lL59f4AvpYxdQiO4Z-u2PhyJ5pZYVahO1wLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماز جماعت شهید طهرانی‌مقدم در محل تست موتور «قائم»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/444878" target="_blank">📅 15:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444877">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEaY0qSX610f1k-XDZJaFb3CtnyawpPx222Ztz7ujvDJcWfLSqFNwi57EBJwmizpALEbKzqsighN2xQLXF3ryqcCNHpsPPydgGCvT5xQQABrBOCPFvYwj1mK217LfLg5-Zc164H_JtSuVYA22Yhyqi6iYt8YzEz2YjO8Fy_ez6Zxk6r5S0hsmr1CJKRaSSXYk66Tm8-2Zg2TC2Rkm6AUdy-q4U0uteEwQR8xGv3uyWMUNoWrUsKoAgi4lz7YhM9poadGmRV8KyMihCQ4Jv3gQkqlZix5K0cxgbJHOg-CQ9ebAcbiQQkEo2wlMoYDDabY9W9MI4d7uq9Pi3h8yvrRdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ارتش اسرائیل برای شهر منصوری لبنان هشدار تخلیه صادر کرد
🔹
در ادامه نقض‌های مکرر آتش‌بس از سوی اسرائیل، ارتش این رژیم با پخش اعلامیه بر فراز شهر منصوری، از ساکنان آن خواست این منطقه را ترک کنند. @Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/444877" target="_blank">📅 15:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444876">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/557d43e873.mp4?token=JFgqq-yD6PqaP247bmWeK35DufliCcCWbo6l0KgMkHurY0VVqp9HumyHi9DKU9_n0o67GLUEIZeOqm2LiNRzaQ08cCEUFMGjH7xccPNHkMg6DCiOAaU_aUS88AxyvA8ad6f0GNHBjqp8QOcRJT7opX_s_tc0yD5mPsVpl3d0wC-ZIFOW4vOV1gWt3nTCnmVkHOVfskA-ambLDL9IzkRUOKmcHGjI59QqyfNBUUbqoaBUJoxdITVhnKNKkkgk2lm_dQjxpNFlPz2WB2t_z_5b1K4fBkgS5glnqgs0Ih6dyjaP8g43PrnI8bfi6yePlvrREH04eBkqzv_leMMRA6cm1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/557d43e873.mp4?token=JFgqq-yD6PqaP247bmWeK35DufliCcCWbo6l0KgMkHurY0VVqp9HumyHi9DKU9_n0o67GLUEIZeOqm2LiNRzaQ08cCEUFMGjH7xccPNHkMg6DCiOAaU_aUS88AxyvA8ad6f0GNHBjqp8QOcRJT7opX_s_tc0yD5mPsVpl3d0wC-ZIFOW4vOV1gWt3nTCnmVkHOVfskA-ambLDL9IzkRUOKmcHGjI59QqyfNBUUbqoaBUJoxdITVhnKNKkkgk2lm_dQjxpNFlPz2WB2t_z_5b1K4fBkgS5glnqgs0Ih6dyjaP8g43PrnI8bfi6yePlvrREH04eBkqzv_leMMRA6cm1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای نجات ۳ نوزاد در بیمارستان خاتم‌الانبیا(ص) از زبان پرستار شجاع این بیمارستان  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/444876" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444875">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqhthnD8jlVfRdW4oHCyWIdik_4m-TlyqVPxW3TgSGKmii9dkvCLRbO9qNOJuE35NmSXiJG3fPID-jMgNfoiLhiR2vu0ygHEQbKz8fQLDNwiSG4DXXtZzbfV9fJGdxWg1MWeBchwJVq8qnDHwTaTCOtbKROD32Euc5nrqfZ2j46axz2C1-lY9iveqfV3LegLF-NiQDmPT2RPnf_ix4C6_FBeJQfPGiCQfmwp-HWWRMGdD450u6EmYyVyqtBAzQJYZwynSHDIt0XGS4hXkL5eTGEubDkvyv0vRMm5swz9I8GEMNWcTm6ErAy9WNud0FZAC4i6gGR5J0aGAu2NncI_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امام جمعه بندرعباس: دریافت هزینه از تنگه هرمز، حق مردم ایران است
🔹
حجت‌الاسلام عبادی‌زاده: اعضای شورای‌عالی امنیت ملی و رئیس‌جمهور متعهد شده‌اند از ۶ مطالبه اساسی جمهوری اسلامی در مذاکرات پاسداری کنند.
🔹
تنگه هرمز در محدوده آب‌های سرزمینی ایران قرار دارد اما ایران در گذشته از دریافت این مبلغ صرف‌نظر کرده بود؛ اکنون که دشمن امنیت این منطقه را به خطر انداخته باید مدیریت ایران همراه با دریافت هزینه به رسمیت شناخته شود.
🔹
در موضوع مشکلات صنعت خودرو، : بازار خودرو رقابتی نیست و همین موضوع مانع ارتقای کیفیت شده؛ باید زمینه ورود بخش خصوصی به صنعت خودروسازی فراهم شود تا رقابت افزایش یافته و کیفیت خودروها ارتقا یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/444875" target="_blank">📅 15:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444874">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
ارتش اسرائیل برای شهر منصوری لبنان هشدار تخلیه صادر کرد
🔹
در ادامه نقض‌های مکرر آتش‌بس از سوی اسرائیل، ارتش این رژیم با پخش اعلامیه بر فراز شهر منصوری، از ساکنان آن خواست این منطقه را ترک کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/444874" target="_blank">📅 15:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444873">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583654c04e.mp4?token=dFDhJiruuK4FGAn0CsZeke4xjynloSaqzYtsBhLTzTmGtUuDCDBX0fzRVoq7AWg2wly0JRrTOLliT_APnUrda4ZSLLN4jaelPBAG6QG0rBr4wNSY3OGnkCDM9a4ec1Iez83Q2iJ45gvA5cZpoQAlw2h_e0ZO7ul6mihXHMBcRmrZ1o3BPqr4658JAvwQwgEc7z9sMb3Tfe5O1N-FOYsjeTZiWIJEYVPdAtE6MAv-U1gr2ZjFYN-7D6OFHmcweee4-uVid0pHT2l36ykaNgKLhIpLXCq6QH8_qbCkyNen5J7SfKgs0lJZLNFFcwJ5B7qrcn29RrzFsTuJvIDtfvERAx_WIsEUc3eQUvU15w6m7mk8PU2uHfVezvIvxAPqLnnY_asiiEpsQjTMhnW2U37NZBa_fslsfndZIsUgweMMu9TGiC5Ji0eMZcRuV3RnFsEHcKs05VROu91qHpm341MG5n2XHBG4mrYfl_P8K84-XRjgKD2qYZPkTar25lm1nk5xnKQ--20ICtwHtWAar4b1SLsEI3UEEnqCmsmf4cvJh7gWyKBrktES_E6z1LSNLbCJY5Va4iQ2sak70b3leFXS-XcMFwMKXIKQN3X6I6ODO_wK52XtTZkBgnLey7BlpPAEwiUTBHLTSBaOTA5FnZnKZj0LZ7CKrHaq7ty8xXUPZBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583654c04e.mp4?token=dFDhJiruuK4FGAn0CsZeke4xjynloSaqzYtsBhLTzTmGtUuDCDBX0fzRVoq7AWg2wly0JRrTOLliT_APnUrda4ZSLLN4jaelPBAG6QG0rBr4wNSY3OGnkCDM9a4ec1Iez83Q2iJ45gvA5cZpoQAlw2h_e0ZO7ul6mihXHMBcRmrZ1o3BPqr4658JAvwQwgEc7z9sMb3Tfe5O1N-FOYsjeTZiWIJEYVPdAtE6MAv-U1gr2ZjFYN-7D6OFHmcweee4-uVid0pHT2l36ykaNgKLhIpLXCq6QH8_qbCkyNen5J7SfKgs0lJZLNFFcwJ5B7qrcn29RrzFsTuJvIDtfvERAx_WIsEUc3eQUvU15w6m7mk8PU2uHfVezvIvxAPqLnnY_asiiEpsQjTMhnW2U37NZBa_fslsfndZIsUgweMMu9TGiC5Ji0eMZcRuV3RnFsEHcKs05VROu91qHpm341MG5n2XHBG4mrYfl_P8K84-XRjgKD2qYZPkTar25lm1nk5xnKQ--20ICtwHtWAar4b1SLsEI3UEEnqCmsmf4cvJh7gWyKBrktES_E6z1LSNLbCJY5Va4iQ2sak70b3leFXS-XcMFwMKXIKQN3X6I6ODO_wK52XtTZkBgnLey7BlpPAEwiUTBHLTSBaOTA5FnZnKZj0LZ7CKrHaq7ty8xXUPZBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور از تنگهٔ هرمز فقط با اجازهٔ ایران
🔹
پس از هشدار سپاه پاسداران، ۳ نفتکش متخلف خارجی که قصد عبور غیرمجاز از تنگهٔ هرمز را داشتند متوقف شده و به خلیج فارس بازگردانده شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/444873" target="_blank">📅 14:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444872">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/963f27ca18.mp4?token=SmAo3ZlTU8NpB61uug4F6Tbptu2E2gCe6-dXUKvjz6VLi5-pkSp0UqlHcjpskpy7h-qJd-nCpdeQmxcra7VdEvZOQNof-8V447WUQfEBOvt4GqnUut0HJ5YS9scQEfxpu25r71BhFjnklD3d1DAFtAxaGQ-9hKoFXdVo5JmhIwClaUD3xVEFeRbBB19XkoXcDT6Gu_vptAq05FpQZK4Vdk_K1ZfxVqU65NrBIZwgNrp9cBOMLT4Suhdfhv4qtS2dKYvQUAu0uAB5VWmwA-JEUdAD-bCxEkPvgnjocJdrFuqzy7zqSi6-R9GTyXyY6ZX4NdkjpnMMmjDjxTXGxv77wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/963f27ca18.mp4?token=SmAo3ZlTU8NpB61uug4F6Tbptu2E2gCe6-dXUKvjz6VLi5-pkSp0UqlHcjpskpy7h-qJd-nCpdeQmxcra7VdEvZOQNof-8V447WUQfEBOvt4GqnUut0HJ5YS9scQEfxpu25r71BhFjnklD3d1DAFtAxaGQ-9hKoFXdVo5JmhIwClaUD3xVEFeRbBB19XkoXcDT6Gu_vptAq05FpQZK4Vdk_K1ZfxVqU65NrBIZwgNrp9cBOMLT4Suhdfhv4qtS2dKYvQUAu0uAB5VWmwA-JEUdAD-bCxEkPvgnjocJdrFuqzy7zqSi6-R9GTyXyY6ZX4NdkjpnMMmjDjxTXGxv77wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نصب یکی از بزرگ‌ترین سکوهای نفتی خلیج فارس در شرایط جنگی
🔹
سکوی رشادت به وزن ۶۲۰۰ تن توسط مهندسان ایرانی طراحی ساخت اجرا و حمل‌ونقل و در میدان نفتی رشادت در خلیج فارس در روز اول تیر نصب شد.
🔹
این سکو به گفته مسئولان اجرای آن، قرار است ظرف ۶ ماه آینده با…</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/444872" target="_blank">📅 14:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444870">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7c04248e.mp4?token=EVtHh5I7qH0xRkYJQO6huaJlXYfvQ5Pi6RJ2E7qudewbYgK4HAasFTch3D27_z6QzHg3-AsJX5UEhP_drqKeZdIo2d2pLSTwTd8uSjRsXahC8jYI8BAXRIiQVm4xFJkYnfRCEgbBA1Ec32k03AIlVEdP0V7bBO_SZClCMboF6ChMk2pnzUwvGvnyXAhhjGki4xgSVDdtMRd3GKTYua3KmtUW36J2W4yoCh_bHC3SRzWlIxdxE5WBxUm8gYA4pLfr6AdnWUykQH9X7ZCzXKvAmSv8tnr02OzXPU8iK0jstizPnIYtHdGro-4IrV83N5IR_WmIdjpcPo2OM1l7PZgcBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7c04248e.mp4?token=EVtHh5I7qH0xRkYJQO6huaJlXYfvQ5Pi6RJ2E7qudewbYgK4HAasFTch3D27_z6QzHg3-AsJX5UEhP_drqKeZdIo2d2pLSTwTd8uSjRsXahC8jYI8BAXRIiQVm4xFJkYnfRCEgbBA1Ec32k03AIlVEdP0V7bBO_SZClCMboF6ChMk2pnzUwvGvnyXAhhjGki4xgSVDdtMRd3GKTYua3KmtUW36J2W4yoCh_bHC3SRzWlIxdxE5WBxUm8gYA4pLfr6AdnWUykQH9X7ZCzXKvAmSv8tnr02OzXPU8iK0jstizPnIYtHdGro-4IrV83N5IR_WmIdjpcPo2OM1l7PZgcBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود دستهٔ پرشکوه طویریج به حرم امام حسین(ع)
🔸
هزاران زائر از سراسر جهان برای شرکت در این عزاداری، در منطقهٔ قنطرة‌السلام در روستای طویریج تجمع می‌کنند و سپس در مسیر ۲ کیلومتری هروله‌کنان به‌سمت حرم مطهر امام حسین(ع) به راه می‌افتند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444870" target="_blank">📅 14:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444869">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دَرِ فردو و نطنز چه زمانی برای بازرسان آژانس باز می‌شود؟
🔹
به گزارش خبرنگار فارس، براساس شنیده‌ها از متن تفاهمنامهٔ مذاکرات هسته‌ای، نقش آژانس بین‌المللی انرژی اتمی صرفاً در مرحلهٔ پس از توافق نهایی تعریف شده است.
🔹
براساس مادهٔ ۸ این تفاهمنامه، در اجرای توافق جامع، یکی از گزینه‌های پیش‌رو برای مدیریت مواد هسته‌ای، رقیق‌سازی آنها در داخل ایران و زیر نظر آژانس خواهد بود؛ اما این مرحله، منوط به حل ۴ موضوع کلیدی است:
🔹
لغو کامل تحریم‌ها
🔹
ترسیم جزئیات بازسازی اقتصادی ایران
🔹
تعیین حدود و چارچوب خروج نیروهای آمریکایی از منطقه
🔹
نهایی‌شدن پروندهٔ هسته‌ای
🔹
منابع مطلع می‌گویند تا پیش از حصول توافق نهایی، مادهٔ ۹ تفاهمنامه صراحت دارد که ایران هیچ تغییری در برنامه هسته‌ای خود اعمال نخواهد کرد؛ تفسیر ضمنی این بند آن است که سطح نظارت‌های فعلی آژانس نیز بدون دگرگونی ادامه می‌یابد؛ به این معنا که ایران همچون گذشته، دسترسی موردی به سایت‌های بوشهر و تهران را برای بازرسان فراهم می‌کند، اما اجازهٔ ورود به سایر تأسیسات از جمله فردو، نطنز و اصفهان را نخواهد داد.
🔹
در همین حال، دیپلمات‌های آگاه از روند مذاکرات تأکید دارند که رافائل گروسی، مدیرکل آژانس که نامزدی دبیرکلی سازمان ملل را نیز در دستور کار دارد، در اظهارات اخیر خود تلاش دارد نقش بیشتری برای آژانس در این مرحله تعریف کند؛ اما موضع قاطع تهران، ادامهٔ روند فعلی و رد هرگونه زیاده‌خواهی پیش از توافق نهایی است.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444869" target="_blank">📅 13:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444867">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c892433e.mp4?token=k5qoCZ3-jxAWick3gbQx-aMWqt7toJ6Wz9j6d1OZcicMvKd6zpcrTPSVZhL8DnnHO6YJP_ohzxxamz0_4QiFvAwkPysJB32thZLLMo6-2eZFAy_ikkz0tNQcvIU-ScyGplQbv4N50iH3j-J34nUTHfNutviSjoVnGtOYmdfS9fU7Z3yZQ4Mhx4FqtVx8_6m7OjOYFqQ_IaMehkv3Ptsop-aFb9uJuCuMYznsQEH2jeHfrE6zIfmSHMxr9Mh9l9e3vOcDagChTu1nX3kJLRxyfJO_VNbxpjcd753KSnsYpVgl5HBNiP3r6ifJBmqYwRDSx-aolgPd52ZPVDpXsp0h3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c892433e.mp4?token=k5qoCZ3-jxAWick3gbQx-aMWqt7toJ6Wz9j6d1OZcicMvKd6zpcrTPSVZhL8DnnHO6YJP_ohzxxamz0_4QiFvAwkPysJB32thZLLMo6-2eZFAy_ikkz0tNQcvIU-ScyGplQbv4N50iH3j-J34nUTHfNutviSjoVnGtOYmdfS9fU7Z3yZQ4Mhx4FqtVx8_6m7OjOYFqQ_IaMehkv3Ptsop-aFb9uJuCuMYznsQEH2jeHfrE6zIfmSHMxr9Mh9l9e3vOcDagChTu1nX3kJLRxyfJO_VNbxpjcd753KSnsYpVgl5HBNiP3r6ifJBmqYwRDSx-aolgPd52ZPVDpXsp0h3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متن حماسی که در اتاق همه بازیکنان تیم ملی نصب شده است
🔹
در تاریخ فقط یک چیز می‌ماند، آیا ایران صعود کرد یا نه.
🔹
چند روز دیگر هیچ‌کس از تعریف‌ها و تیترها حرف نمی‌زند، همه فقط می‌پرسند آیا ایران صعود کرد یا نه.
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/444867" target="_blank">📅 13:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444860">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IcbBd7-hHwbTf8IpA3CoIYCXbx58l9sr0BzIyTimHMJloUp_kKNtU0iYEBdVy5Y3bAQuEFRk76Gk1ieHT80Bgwi5RO_Ankzgnvs_b8UWYWwrwycXE8zOJIEhFDvyfk_2zVUHBnCutEJcg6Rghk29E1T-2T6ujRUinfQWnRsMIoSfcBxHL9lNjQHV5pqrYVqzPxaXE3sHsaDCZ_UIZKJX5j54siHVV8kShMIbvLBnNUAgpvfOvaRVY3WE8903F8NEujoaKqWenJAm6lL1QtQ64KeQe87vqiJqGuklig0Kzo6tv5QFIxB_gaC6PaGvPpJ2v6b2uO2-OjWExas3_7QG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MsknEhpktiXMx69Lh-8w0v67bZFbPr17Nmj-YWd3Ygx6p8BPjpqg05uIVgOTAV1GbpbOr7UoXp0YzG_q3VoE_40s2tNAh0WnxlitgIj7RjGrjcHdKcZotfPl9nIjAp0_o_Cc928pnrPwUF7BF2dvnRgEf3ZjJYwJYEkDOzMsiyo7Kv5Ubf2eGrpXbTb8bbX201bS7bO6ASYLCSd5VDumX_Iy_WuqB9XZN234ACQfMt3aFLsBqHPNVzesJkWyUb7hyVekYeR9nCikFT5nL08I0jRssFj-h1On7AoX8vGAbzAG0LDfHAbOq6rUYTNwI-yWzeAduLNeF0EzchEqRcgNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLxubW61nc4fvc92ztCP3GRejS0U0bFjIVa4kCSo0rdVPOiMF8Z0yH7jeEwlmPahBgxyP79CccW-p1ILdqltteFiPe6gH5cKK1axaVKMvX4237-Qp4k3CgBgQPK6MYGePQtXEOCb64KAiFmMCacmN-YYL7uqeLap0exZvndcOwbLlomiX6MIoUUarc427UylSLH2BANPlhNHazl3M6x22GzXY-oUzBNrJf8ZEXv8ZGFkyvHDETkiAIJN1OXj0wDQYuuluPO7oVovJY2nNoXOmePKOD9NyZSArA-DiHWcUR7V3tTmOh_SWKnnpmHknGSG_-zN1mP95znEPn5Pedli-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iE57qYRSEXFBU0l7R1QOZLtuZQCIHN0TayYuoThZYyDfTPJzugJWHQpZlFhvf0tlC0Vl1SpPau7gfXpGUMsVFX6j9DxF1DwHj7dVRMCRcUdGuj6D8rqa9_QTB8y3vhX9oE0Uv3lLBbf6NG_VTXHWPY8MIlk7U0n1USpWqf8pi-wqdK5yPW65wPoMp37dfHZjx8Y1TeHChh1xFjoqXAzEPeutqlI6bgSTYGqWosoh44cPJFFRrrv14oHB5MWoFb-Hs056LFAmFBWUrpXXZeluBDeorEom_oBGROfnQSxnbtMhTlI1eF7J4JOVs99jDmDsZEjeHebO_bdvrvRioS10VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5OTGUMIK9wJifiBmMP0vKpdDC4IeDTnj6gbmlUZb6Vsord0Ndpdignmf6sP7cHNs-SKJYHUE5IePyM5uMA5_cXAjNUbA2Q1afeNgbebKbc-iXy0u7UnAdxmxekCNp9_UhWtV7rnzX8pFJbZUksBnW2KI3YYaBWGu7taawP2euU46eBudoDG93snYfMlBmnw-RWjNz4FLU4I14qFBUv56y7ipKpGRTv-1DgQ7llfqFphCP9kqtFsfcY4b-F-4qXcL8be00pU9AGdsWiji1OXblzuDRZwLv0F6SNl8Es2Vycbe74zF0igmUcC3tARZdAqcVxok2xdCUAhitAt_AWwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SU2Llkr3zSOZWSOXFQoulCnb0I7RA-67INfIM0W6UWswfj2fx6btjtoctqTRBAMbsCeMWUNdxOPTyYKZIcJfTeC0UN-i134ZwM_W4pmiM65fmuZAW9M-GMIRjqUUxqbwy5hNTTAlIIEZpX1c0X11-vQGAaKtw6klTgEP93s55tsDv7ut8Wj2lwezsoDIxdCGBsnYnnmeqhhwakBN9mTZNloLoWt6kjMnfo41DUBRiIbvPtQrY45RK79V1-9r68SSF4UrFPShC7rrJi-Zsalmp3y_JWsOt443r_Df_hUWI1jRsJfOc9eyqFyCIqORWRMVAkvvGi9bsqOk66HBRWSISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jYL53jXWqi_gN6zAjZERtabWkM7dl6IuVKTtRuKhE-jS_DFVDbAe9thTroNTwa_f4NIqnnQ2hOsXOiIXUiNzRsVkx_FW3dyN9raD09wE147nX7pNpyMhPuYsFH4P7CD0oRfH_ntRXgOhMgzz58K3V1-pra4DUc_QjcEpfmBrSdaPDLioHuTVXCWPPJBN-gCQCO0DaWqjTNosQb5y768C2JxPUlKU47Wjtsq6DW2peBdHO6fMQCDOL8ciKJTO9Eb2U8cHETtJMyg_Q7Q0tABcHgcALECUD3iB2RJM_6C3pBBN5_SwDObhIMH4grLO0FvTfOcLz8BDn9pzpSegn6XOMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اشک و اسارت غریبانه
🔹
نمایش آیینی «یک بیابان بی کسی» با محوریت وقایع پس از شهادت حضرت اباعبدالله الحسین(ع) و اسارت اهل‌بیت ایشان در دولت‌آباد کرج اجرا شد.
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444860" target="_blank">📅 13:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444859">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4cwv2yBABKdHHj5ccygXKqC-rB2teGWp93cIKWhwD18Be96Oi-3KDrkC3yilwJaG95T8AImEOwJK1ENgDdaSVIi3FkLibNXFT-9IIco92WNcrKfT2JCdAPiq8_8xP77nnvbujtGnz2_fd8iWbJWwnzGyNUPKChTWXCGWVkTctjlOccvTgr-UJvlszjuu1NpxaaJ-VRWF--IPkqaFyqV1fTZ_PDAR2nfmhWW4ARdk-yOv-EZmGjzIxaBXYqngW_BW6pKgLkl--Q0rD8ASUPrQEVQdIM0KlBQ99dzQ5ovN3iKVsd0a0d07IoliVFkviNU9brZmT8w6PsRvKHpTMSTPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب نماز جمعهٔ تهران: اخلالگران اقتصاد کشور باید مجازات شوند
🔹
علی‌اکبری: اگر در جامعه‌ای ظلم به افراد ضعیف رواج پیدا کند، برکت از آن جامعه گرفته می‌شود و خداوند متعال ظالمان را به‌شدت مورد مؤاخذه قرار خواهد داد.
🔹
احتکار و گران‌سازی عمدی، به‌ویژه در شرایط جنگی، از مصادیق فساد و تضییع حقوق مردم است و کسانی که معیشت و سفره مردم را گروگان می‌گیرند، باید متناسب با جرم خود مجازات شوند.
🔹
شواهد نشان می‌دهد جریاناتی به‌صورت سازمان‌یافته و با سوءاستفاده از شرایط موجود، درصدد جابه‌جایی مرزهای عفت و حیا در جامعه هستند؛ مقابله با این روند نیازمند طراحی‌های جدید و بهره‌گیری از همهٔ ظرفیت‌های کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/444859" target="_blank">📅 13:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444858">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkSUagR9YUJPhtPJ1hVCsHBKC_nxYgUsHa2ILn4u8bXfRkumnXJ4EC1XVzF91hUxi7VxzQ5G6YuQdVTLhl6QYfYWTXshskO2XWn3Ft0KPsf6wXXlX7qBJxi0ge4PrzvGsHgQWPnse9K0ODVZCTW6dSxcVT8KDdM2bWx8R-fRs9UPMMINIjzjqbrpK-u3Xd_GDuiZg1FecwiJOtdkM32ZzdGkRMDmWa9-dNJ84vB4cLD8zhd2CNyVwGNNYxZlAcXBBSfdSIPbD91DW57-vhy0-mF1bQEi7U2Qstik2oib3hK20viTrkm-iGk5YPDtBGxMvMQB1Fk6Ae2UdY_bYBSnvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطبه‌های نماز جمعه را در صفحات ائمه جمعه در فارس تعاملی دنبال کنید
🔸
امام جمعه مشهد
🔸
امام جمعه اردبیل
🔸
امام جمعه اهواز
🔸
امام جمعه یاسوج
🔸
امام جمعه قزوین
🔸
امام جمعه پاوه
🔸
امام جمعه کرمانشاه
🔸
امام جمعه زنجان
🔸
امام جمعه همدان
🔹
امام جمعه ساری
🔹
امام جمعه بوشهر
🔹
امام جمعه اراک
🔹
امام جمعه شهرکرد
🔹
امام جمعه کرمان
🔹
امام جمعه زاهدان
🔹
امام جمعه سمنان
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/444858" target="_blank">📅 13:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444857">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ei1H8PWB4Zkeudhzep-WLsMCOqg433AnBQXZ5AC72xJWVKlJsEO7fFH4sBcMdrdhSzmKG4DrmlrOCzGGj6zo4CqcbLNLxNI0AFvldOOlST2LLlXwBKWquNgh6hPxt2uXzCpvTrg-t1cCzmq0TGrwDrLCOudiYP8j0Y6lERykUbYD6paDB6UW0EGSFtfFvwE-Qjwma924oOyHr35ha7L3rmnFj2wCSw6teNQ6C9_eJUTNMqUfpCAU5ZuoWBhKONOFebIa0GJkYs0rpdR3YqhZAni1Op1NZYUZsbhQ7w8nsoVxrWA8BPkC9VjfQacC_NJpKj4gIHJ1WZg5D3iCHhjpqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت بازی پرسپولیس و چادرملو تغییر کرد
🔹
با اعلام سازمان لیگ، به‌دلیل درخواست شبکهٔ سه سیما برای پخش مسابقهٔ تیم ملی والیبال مقابل ژاپن، ساعت بازی ۲ تیم چادرملو اردکان و‌ پرسپولیس، امروز به‌جای ساعت ۱۸:۴۵ در ساعت ۲۰:۳۰ آغاز می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/444857" target="_blank">📅 12:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444856">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_Ybyy6gyiaeifdGPrYksgP3wA1hYjW3NdjY2EJXH5RCKUejbQMzcFTnVoGhjOoJa5oiFhD0BBCnQJZhGZosUfqr-HqfidSpBwPjEOqdKRhlTgexAGKtVH8yWMf1y57H98id7HPZQ1Es1S6phIxk7iVa_vdy8LOe4ADaLVPAvkSwqQEhmT7Qr4aADyTYZiky7LdeoI7BImMyn83YhxeHKCqGwE7Q-byHRlm_Zh4DZgV5Jy-n8BIqrlGez0xzADTZuIOB3-6hr7IlIsbG-ELyR61M8StBdRvnhXZnujoKIcqo4-Q69hmg9uk0sQkjrahyqKlTdUexil1gWukRLK9tAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی سپاه: عبور ایمن از تنگۀ هرمز تنها از مسیرهای اعلامی جمهوری اسلامی ایران ممکن است  بسم الله الرحمن الرحیم
🔹
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر…</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/444856" target="_blank">📅 12:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444855">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQeUzVWD9RmFxuPAp4bUig9ctCjeI8vu_oD4GD5l4sNeQrAINmvodYGjNbu3bMrbXleCiXAHlmbTuzqqT4hjTGt1EyyHQcbRWv6OMliy9o_5SF0w_Zt0mwnSZmuTsgvIg1R0rEuI8I3xYEO8z7fckmVRHb2AudwLmiiD5SGPb-Dk84wnSYQ5ftCJ084CaU2D3tIRtmkosgRYRcReyF0Vv5wR7Wn43UTs4gquqfORlU1o1q7SAZgirRHTN5_8-MDCcB5Y_lHTnkKif0P4RbzCcIZrJZHogN_NUiadjWQcFR4DMThINzlZrMZeiL-WcCCmMBd0B9WQ4lBqmI6g9iMnGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبس گرم‌ترین نقطهٔ جهان شد
🔹
براساس داده‌های منتشرشده از سامانه Relay Weather، ایستگاه هواشناسی طبس با ثبت دمای ۴۶.۸ درجه سانتی‌گراد در ۲۴ ساعت اخیر، در صدر فهرست گرم‌ترین نقاط جهان قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444855" target="_blank">📅 12:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444854">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgLWGohFtn3DGWXReGRmH6dBnVbLIW2K9O-KuyJB_YfvftaMJ7itZK0EHYwyla8EiYQc7THWo7ROI2Q7tjG3VJncU4SlYnXniOqwj_63B02Jqmmpty1AweXLgsg_MdpaFm3MopTQe4zA0f5DUz-1C3h-VXWNdIvArh7g2GJapHnuedA6DZvUj_NaRZLVNlg-BEEBpYGx--x2oqy-4_2V56Sx40jCrf8HI9EEHzp2uY5b35G7yR1JSwSEtFwBBd1lYsm7FkS2d5nidVLokBaAGIiji9S12pRi8smduXzpLB5mvd10ol7Idnofs0zTSuBCViiEWCrcmNaKcvTyGH2l3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازداشت یک ایرانی در مونته‌نگرو با درخواست اف‌بی‌آی
🔹
پلیس مونته‌نگرو به درخواست اف‌بی‌آی، یک تبعه ایرانی را به اتهام حملات هکری گسترده علیه دانشگاه‌های آمریکا و آنچه «خدمت به سپاه» خوانده شده، بازداشت کرد.
🔹
اداره پلیس مونته‌نگرو  امروز در بیانیه‌ای مدعی شد این فرد از سال ۲۰۱۳ تاکنون حملات هکری گسترده‌ای را علیه بیش از ۱۵۰ دانشگاه در ایالات متحده انجام داده و خسارتی بالغ بر ۳.۴ میلیارد دلار به بار آورده است.
🔹
در این بیانیه همچنین ادعا شده که داده‌های به‌دست‌آمده و دسترسی به حساب‌های دانشگاهی نفوذشده، در خدمت سپاه پاسداران انقلاب اسلامی و سایر نهادهای ایرانی قرار گرفته است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/444854" target="_blank">📅 11:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444853">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej_q4LfWRkIj_oCd5jPHPDw5lA9dYUEL4E67EQykyXwUdIIQI8ChdHi3MUBewfsUY1MPKgfYwmJ9lkkYtWyraQMyb3ag4mkY0igMLn2EmCL0EqbnAsLG7AZRJUfPLjkRDJVZLC0IJSlqTioy1jsj2unRC-M4xCPwHqknfJldR5sC1k8ivmeOmcsy-5v-5PlBcLdj9_tQ0yhcfiwfcNRaZz4mg7-BvMVZHGv8mGaZNjDCsUJl9VGPl_TzZmm16755oDtVbutHePSlRR4mzkUkrZNPh0gi4aLGF_ARto9WZJsZ17PDQ1xlm1InaWWqsBaU3hJxAVG2hQwkEyT4cbICqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگترین و دقیق‌ترین تصویر از کهکشان راه شیری منتشر شد
🔹
تلسکوپ فضایی «اقلیدس» دقیق‌ترین تصویر ثبت‌شده تاکنون از مرکز کهکشان راه شیری را منتشر کرده است.
🔹
این تصویر که از ترکیب ۹ عکس مجزا ساخته شده، وضوحی برابر با ۳۲۴ مگاپیکسل دارد و بیش از ۶۰ میلیون ستاره را در بخش متراکم مرکزی کهکشان، موسوم به «برآمدگی کهکشانی»، به نمایش می‌گذارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/444853" target="_blank">📅 11:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444852">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/semFvZXDXVM0cP_uGceVCFo-svlAtVSHc6sWtAKyAYr9jSUkDG59V8ZpkQWP3JD4PaNoJOVbT93hqm17sWfVkNVfjW0krIYkdBBiBoZItKJ8eUblcFOVw_3_4teAI9d7_iF1ENHwKwAUD8BY0GTXEVr0Iz23-9heCm1EKv18lQDcp2W3aHxLMcd2565zvgOkzCUCOuQCK7Jkq96rAyTw9xTLYqApZnLf1qDSK9b5lNx_WwKAWXXGCKCXsyiDo-QSayDzNr8ROhHyC2qhyK6emMU9Ao_3Kew0g9aBbckVe17hdN-SZ372t3623FGVPr9AGmgitBiI5lgsL1zpo0la_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل حزب‌الله: در کنار ایران خواهیم ایستاد
🔹
علی‌رغم تجاوز، ایران استقامت کرد و محکم ایستاد.
🔹
ایران به تفاهم‌نامه‌ای دست یافت که اعلام رسمی شکست آمریکا و اسرائیل بود. امروز، ایران در حال شکل دادن به آینده است، نه تنها برای خود، بلکه برای کل منطقه.
🔹
از…</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/444852" target="_blank">📅 11:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444851">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bH16TcxsXhb30Vcj2XaQZcmfla_cTn1m1F5oD97deO-bPOvBh88h_qFiQTgKGc6xwINh7RUnppKX30SRLZ2bYU837ccebApq26WopXA0R7qH3IwUhOuZeMGueMNwRhVjNAdb2i1VR3wNkblr4LjeCHrE0qdCI9A_Xavm-oN5NUArln4zXKv_5KM4y0BbXnrfIthtyrIa7OwU4-nkZZftpkYwoRQb6ap7bcnuhJXNFYSsUXAQfIM9d2Gs4KWlpmNbhOqOW31yfDE2Tjw8j2BXpMaSLFd3mzof-64KcY2a8Dia4MdnmtQSlw-4OwdtCJYYjMBZo9pciQdxaJBEXyix0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل حزب‌الله: اسرائیل چاره‌ای جز عقب‌نشینی کامل از لبنان و توقف تجاوزات زمینی، دریایی و هوایی ندارد
🔹
دشمنان جنگ همه‌جانبه و بزرگی را در زمین، هوا و دریا علیه غیرنظامیان، زیرساخت‌ها و مظاهر زندگی آغاز کردند.
🔹
آن‌ها با استخدام مزدوران، طراحی فتنه‌های فرقه‌ای…</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/444851" target="_blank">📅 11:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444849">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAUj4cvNffnIrAG_ml4wRO9o8YH69FC22NqOkrMlRWZfozr8dFghq6SsmX6iV60NiyV56ggpfkqc0hlo039bhK9uxkPLRzGry4URhmp6w9Z97UgY_n1UZoEKhp7D7zFRjJEQNiKHQPajZ_wFC3LE6_p3MQLrarXcMxqG4uVdMZk_ZEnbbQU2y1VtC8WndfZgpDK-o3pzNthJGq0yR0I-iNX5nS_CFCz3ctEE40nV5iyCcYzOB58C6iqOYPA6aDQdlGUVASbQPLU3tdMkCwVidzT4eRjHTqZXC9qgfP1gTe6TIfY3PGU4NLaC7GrI8PzKsq9eojrpTZy2Zoda4dG1BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KA-4lGR6fOiPCLsbvgkSX0U-z4EyaZd001SwSnz2YtjcCyfuWN86GUSnpA030U7c3swxnYmSixgMrSJHb7wNCpOdhVDqyRbTBsSD6of-9zFaPMiFuWV-ikZfIMjdrz1xpOsyWoi1zf2179KTUGpbT_S3QfZdbUMgMYl3tTMAktHUGgBqjt2Z6pd60ipe-it8Mot11dNb_91QYKyk4XB6OIypmYpx3R24qXrERDAgk0g3mp3B9FoSpwSuuHCcH2IgPbgTqVGT5BOXebwhJ_bZeB-zB2z4Yi7-M7T6iRWTR5Cv7u1lhz2gbAa_zEGJP1xJcl5RRrmo3C5GIiDkFBGy1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیهٔ وزارت خارجه دربارهٔ بیانیهٔ مداخله‌جویانهٔ وزرای خارجهٔ آمریکا و شورای همکاری خلیج فارس
🔹
وزارت امور خارجه جمهوری اسلامی ایران، مواضع مندرج در بیانیه مشترک وزیر امور خارجه آمریکا و وزرای خارجه شورای همکاری خلیج فارس -مورخ ۲۵ ژوئن ۲۰۲۶- را مداخله‌جویانه، غیرمسئولانه و تحریک‌آمیز دانسته و نسبت به ادامه رفتارهای ستیزه‌جویانه و مداخله‌جویانه در منطقه هشدار می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/444849" target="_blank">📅 11:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444848">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_5CNiXO4jqafK6DuRebdIOuTWIhJYznzYApr3qLP_pvtWW0aNGf2pXQTQxfpKksdcsWSAUD5K9psSEheWagIG-Luml8Z0nH0RQvj6UYYZARIs-vFEBBag7YFyGA8sQAO6JtzkgN3XmM7SVWz0ObnMW1DmBF0aIfPqYeckYLYveNjJaxzf39-KWwm1zwLfMJPA2f26jmNn2UPrQvR9GQB9lmLf-WAHMNjdKjww_VXOEwRegk99_FUv3xHH7r8JCZWJYrnUm3bD_GA69bHbafDzOvqmCbdliYnqBDEz5-LoaiH24EvdV59b-z6n0zO2QtPiVHWQ7o1kLXHnXanbSXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل حزب‌الله: اسرائیل چاره‌ای جز عقب‌نشینی کامل از لبنان و توقف تجاوزات زمینی، دریایی و هوایی ندارد
🔹
دشمنان جنگ همه‌جانبه و بزرگی را در زمین، هوا و دریا علیه غیرنظامیان، زیرساخت‌ها و مظاهر زندگی آغاز کردند.
🔹
آن‌ها با استخدام مزدوران، طراحی فتنه‌های فرقه‌ای و اعمال محاصره مالی، سیاسی و فرهنگی، به دنبال نابودی کامل وجود ما بودند.
🔹
ما با صدای بلند اعلام می‌کنیم که طرح آمریکایی-اسرائیلی را در هم شکسته‌ایم و اکنون همگان باید خود را با این معادله و مرحله جدید وفق دهند.
🔹
این تهاجم که هم‌زمان با تجاوز به جمهوری اسلامی ایران به منظور براندازی نظام و سلطه بر توانمندی‌های آن صورت گرفت، در دستیابی به اهداف شوم خود کاملاً ناکام ماند.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/444848" target="_blank">📅 11:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444847">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترافیک سنگین در جاده‌های مازندران و‌ مسدود‌شدن کندوان
🔹
پلیس‌راه مازندران: از ساعت ۱۱ مسیر جنوب به شمال محور کندوان در آزادراه تهران-شمال مسدود شد.
🔹
همچنین پیش‌بینی می‌شود از حدود ساعت ۱۴ تا ۱۵، مسیر کندوان در جهت شمال به جنوب یک‌طرفه شود.
🔹
در جادهٔ هراز نیز محدودیت یک‌طرفهٔ مقطعی در دستور کار قرار دارد و زمان اجرای آن بر اساس حجم تردد تعیین خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/444847" target="_blank">📅 11:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444846">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pso9hmmV-jnxuFqiQAd4GVrQryuuun6rk93aVcBZw_adPbOX5V9nVfeRzTaSnkkpMIVmdtmmhBWuHbKJaPZcKFQ7FFPDWUex9io5zZGPQuivYlPWIm-6uxm21zXEIcVTuCE6pZdlUMCnGY-At1SIfIbtanY4PArbSXx3q-aeIPHE3GOFTkeEf4VnbeOQBYSO9dHdSrsaw82jlfeDUkC5MHgCqpuXUJy8BHb3x3Jlt7NSdPO8fOHXyr30qngnW8-hbnSZnMQ87UHMthtjdt7wvrDRwzcWFxX-npAx6ApljDD04eHMEp3fT_nimrDkPtIaky1L4FOvhUDax1ao8e8_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمدید مذاکرات غیرمستقیم لبنان و اسرائیل در سایه اختلافات
🔹
وزارت امور خارجه آمریکا اعلام کرد مذاکرات غیرمستقیم میان لبنان و اسرائیل که قرار بود روز گذشته در دور پنجم خود پایان یابد، برای چهارمین روز طی روز جمعه تمدید شده است.
🔹
این تمدید پس از آن صورت گرفت که تلاش‌ها برای دستیابی به یک فرمول نهایی جهت «اعلامیه مشترک» به دلیل اختلافات عمیق طرفین به بن‌بست رسید.
🔹
منابع آگاه گزارش دادند که «مارکو روبیو»، وزیر خارجه آمریکا، شخصاً در جریان این دور از مذاکرات مداخله کرده است.
🔹
محور اصلی این تنش‌ها، اختلاف بر سر ماهیت خروجی گفتگوهاست؛ اسرائیل بر امضای یک توافق دوجانبه رسمی و الزام‌آور پافشاری می‌کند، در حالی که هیئت لبنانی تنها حاضر به پذیرش فرمول «اعلامیه نیات سیاسی» تحت نظارت آمریکا است و از ورود به معاهده مستقیم امتناع می‌ورزد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/444846" target="_blank">📅 10:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444845">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
قرارگاه مرکزی خاتم‌الانبیا(ص): تحرکات و حضور هواپیماهای نظامی ارتش تروریستی رژیم صهیونیستی در آسمان برخی کشورهای همسایه به سمت ایران را اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
🔹
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل رژیم صهیونیستی نباشد، جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444845" target="_blank">📅 10:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444844">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJjbORyiDXHKjSncxbcDCj-YM5Oo5JrQaqoEervpSeDFKhI4Eo4u3jfVoEX4dc43FjAJUymXlWNM5rMdyNJ1v8VGnZOKkcI3CqBo9W8xSxSv2um7eL8PGaTxKpuGiDWFxSuTz55Qoa-dXyFBhoL0oFFrJ0c7KLfxbS2nRRfviQFnJGqPI9fRneotnNnc1VEcrrEKdduM5-WMSwNvyfgpPLLhGv-Bu6mcyQvwZwxHHuhlM4UMR2X6F1mkKAbIaPOr9IFPBF_bA46yR0Pg6aiPsD40jGAQJy0hKFAIYpXVoo47W9tMwGXSrx0rvoKVvqu4yDoEoEdIZDTnonbhMEAW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پوستر فدراسیون فوتبال ایران برای بازی مقابل مصر
🔸
این بازی فردا ساعت ۶:۳۰ در ورزشگاه لومن فیلد سیاتل برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444844" target="_blank">📅 10:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444843">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqCaVYg4oHKJxB7QLT3zNuDNpLGQNZV4IXTKfdlAKBv0rFrQ_f9oglP-U-OEmjK5lFe5UTDzCpKbLA8iG5SJ8exYcfqbFvyDxt2gzjiyiyN03uowmK1xDW38wU2TyaoXzPZd7qmoyU8ZEZhJ0CByIRQ1aY6KwKXjxghb9Z0KU3MIEEA3drkbUa67Wt1I1rsGO2yZbFthFv_Lz84zh5uLluI7sqXMI9N80p82ELyl6z2g71ZYvX9Ms1wh8y-pAQnCBZrj_aVSeRD-RLSfZkT75Hb3qVWPNs0c5yJax84q5SDsBEFYuMcmOrYoGXGskb1j0NVTZcs8pcEzc1xNMv7a5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای آخر هفتهٔ تهران در وضعیت قابل‌قبول
🔹
براساس اعلام شرکت کنترل کیفیت هوای تهران، میانگین شاخص کیفیت هوا در پایتخت به عدد ۷۷ رسیده و در وضعیت «قابل‌قبول» قرار دارد.
🔹
همچنین میانگین شاخص هوای تهران در ۲۴ ساعت گذشته نیز در محدودهٔ قابل‌قبول قرار داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/444843" target="_blank">📅 10:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444836">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f22l787pzFV6XxDOdGzq18MGxwRvuzBCMEJiutxeEPTTxjwhwBTauPdsr4QnNoTOcWih-xpBYhfJ0gPOJfEq9moxlap-of-3impjssDeQWrDoz_qlJMulcADYH8jUXkAtYul1If0_FUP5QDXxydOMq3xvvTg0TvblqkGK1M6L16Lj3lLWSds79D0A80N5fgKvidbyVz8hOqJgaX047Mqzpx0Pt8qhY3nRYa3L9L8ebsRvhtGvM8djMP-WRLNBFB_r2Jx0TxwAWbgazPheiTznr232nC1sygZoOcKck3fU8EdFg0qyppj9EFSe5cmhOQumrJFw746BIIi2jEcTc4OxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCfQRK6_RDNPwHXHMmyIpN_-1ZuEHom9PLb_0-rCyVMac-Wa3kMTNDfvjTEIaLpmVqd-EqfBCLdmrxAhvwwaG4Ed0LUFpvzgjag6SVlh2kKQ53VC_69VdJCO52-XjnQH-UTMjNoCXUBSbJRD_vKjoKZb6etRYoSLCwbAoLj_wYf9FDywo0ynPATurYz_lVb17pTXWWvHVOQZniI0j49eKHG1am4VopVFvlLjYqjUF2uOFOfzolb3rqStunpR1bB88ppNK5UZui2jSz667lcdkyJS1WTT4pdQszmmAlWeCJhUEGwVCGSWZjj5xmKAHKkU7E9kfjibb2JD7olVd7qKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSwGjUilqUvpHM_9cbqEXF_gFq_8v-k900o7d7UB72YRzcf-5Bi40-gW32FrG6e-fHuOp0Ehpzd_UWxmyjcDCFDtIy8Ntwek-X-vKVOyJgEOVmGQ5aBVwpGJY7TwP3eDyjQlemjKH9N-djawlEEAk8pm1FrFpV47E9HLkClNHdg88ppSaNWMTCilgo_unMGTP9ZtmxJHtcc4sBNHoqDhmerYhITD4Z_Qng7er-OFwPyCe9QfUmkv2e5cNK4q2OTo6dv5g4r9xFSiNPfhqE1H1B9aqQNz2h3zG2yTJAuaW4sYT9BxVv2YTpRUk8W4Y4vxZ7xPy30BbWKg_pfLcYi4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIG3ju4wDTVqGFtCEJ58riEradIBCgxDz2iir9HfJoTN2Q-L46Jih9hS_HapzVjXbnNuDA84uqbSuyTBbi8GJCBVA1wbxZZ_INwDmnhE_aP-gZe8AoKHW2A4qAHt4QNRwyNMCFVRceOF4oQ1mkORDade6CiADGBsqJ00IJKHkl8tMbIZDiWvIfTQKnJ55Xs2SLfuaQfyf3dCgdltgBpzltI9F9YLXCd6RSljMCY9GmrouxXnMzfUlrC8C5_4cBAnDFsWlxFmNPYSwzH6xABgUxeBg-GycwPBdoZypLS6u9EA08RtJg6pqSwCryT5eLUbxii-MQiEUTExTL-sNe2l9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MDFFu2ki7LLoMUAf263PHfJNbiybwATQMBvzmVDqLCnDngw_8q0M1SRv2abeiZ13LptYKodjYFrOWoHrE8L_IsG7HGGQu1lDSTlY9z2cO8SDustCtZ_2rjQZ2eprn1eGuV8I6FnNZA3X-RJeV8YRG1uLbIQaf33n3ugYW8_JU5kpP2ggjty9Y4bP6DkW89zfJAJ_gHsoSVYfrOVPgCBp93mw2XiOanS_FN5GKYECzHx7L6KDAOEYQU9fHgHP21S_GblIALcGSSPTS2HQYrAeptk5Jxr_DxbAn2Ih0ZsiN1BzPD3GrwFbMHahlzhc2Zq6vthxk7ZQ70cqyifu6qEy1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FuwkmUsSAGhZSmPOd0Q5ya9EWRpYu8b9h-KiLifBp3s4FmxSF_8hEtCL4D32dUiRYLmkK6338bCOhwRg4y7_YN5SxRDw9g6JiDGaAWhKNTezJvf5sdV74P6chDsAjlpl2x75HRCj2WQvGB-UXavmuFJbm0Tp823Xv_3RivYWn-EyybMSEzoQGZov9mJj9CCvdNX9dSQhwX_VHDRElUOKvMEfUmk6dX_IeN44veGWFKv7OL0GzTJtVQtvS2cf5nSEfuuCL4nMJ7wBFnsO_mPqV6bH8DYBCPyKBcLiQyqn4OFAU7VZzNkUqkPuxy_HoyLPTf6In5Xfyv1Nw1SoatFNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZylA-u0R8vjNBoqaUvC6T0BsjvBRsYI-cwpfcDJctdF7eVTPGVY3JP8_28TcCUCSIVgDpCHzUbmCAtHYrpMZZ6lrHoYM11VSTnkn7Z1WVpiP6ObO0Qox8WNQzMc4ElNbujj4YoBjIiZGbqsZOY8pbsAmtEmn7Z9QTJaWkRuO4agRA5mkK4vHKYRyJtqfT8puM0IZOIy87DmzwYMCRA-HG_3qH9bGFJxXW97H0ESJ1d0EUdIouMgBXy3eaApbgin7uxJ6hmO6yHWYTPrBB2nTxCtntw6-GE4OyeqrWQXjNpSyVCTE4lNmxZTyylXBqBpp6sFtgPMI-5dEeBT4S1HTug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم
شام غریبان در قتلگاه شجرهٔ طیبهٔ میناب
عکس:
معصومه کمالی
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444836" target="_blank">📅 10:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444835">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dio3wB8BD6_3RK24ZICZJ6XUxqUc8D-iXpDvsXbrG-tZCH0dZu9zr_dg3Vdht7sAi_Ag1sVppGSxHxnnscTH2692JCSsSgKxFrC78FNHGLv7sokJYwznl0gB6QgJ7wmus98Gx8G1exsyqyqM3G4ifseSeOBEGubbgaltmGWR0t3adMm0sL8WNqiJy3LwTKLFwncILlrTcBaCoK2npNLsj7sFAlJCWWhQNTi48o1koe1t3mflZJU08GNETH5Iv2UBERBKnrhpHSx6zGwypWGZlg6snzQptGqhLIC0K73dZfOiXbtRsOMeMJBEb9RHthqBA8yQc4bS0OIzXe2DczIdrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ پهپادی رژیم صهیونی به جنوب لبنان
🔹
خبرنگار المیادین در جنوب لبنان از حملهٔ پهپادی رژیم صهیونیستی به شهرک المنصوری در شهرستان صور خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/444835" target="_blank">📅 09:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444831">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfPgnwZZ7vbphVD8xzEngLCNxgMDTf16GpQ72fxAP8DGsHbcR75eF_nW60-5QYZVIppM7uvQU1FwcpIguDPerLVuzEGQPyFUZRcM99QICx8jbomYwvkHVE-0PuZpvRMT-56u7lM-Z3kk5lsgzCt_Dprzboa1_xyy57_h2gDsBuJzmKH8LIpOYx_6DRreJOHWe8lQkdiJ2tp9vawHy7l_29LDnhpSOdc4tk1dVlkeql3hs4E8syqmo21FB_obbevTroguC4xMU8H0ZfdcOY4f_LRs-RRs4q8KwG9H94Q0MJIIWwEWj9Uj-rlTLGzPLBmoxDC6Feng8y52o-FCSKKmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/imnKZ5C23W4eHakRy3ygMVI3e_7oEU2xw_A0lGPeSrJMp-fkGYtRykJZ61spJ6XkNuBH8MuoJtaRg2TCxiHnrMkW2GTBYVkZ1yQMl7Go4lryNNWInRNrxTkJ7cUafidIIRVLVMHXjFAJUQPjoT9OQyrcs05ABamtaY2FnS3_JB9Jgs5GQ6fdcjxyPAxQK6PA8RNIi4JOZB5NIo4eVDCKFd6EPpgB4F91c3nYUzJvaXt6E0bVQHIQO_R4orqnLvlSNUt3amIChfKWHBgSyI12D9cZ6Bmtwj7E8kT4IYajf96MTpdeOo6FInLVf_QVb2jRDmmmdsmv2ADzcvAiT1lpyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBKuSeAA3_m3G7HEWhXktrUaL_sn7n6hKIGjFMiqqiVQNrGwtpH61t2ycDBySo19-uKXQcYOdWzkObHlGG9KLmGYaWvEAt7ls7qYppmAcVp57-rLEuFmaImUSt5-dMiEgBNDFEgigz_1S1m1WOtIzqpbWjLUVTo42RZji4fezjcpOikUo3AvGfgh8yGQAo2cL2HQcEcaW69UfGiazl_KsDlGAnHJcZEa-KTb33duw1bpp7A8bdyAI7XaiND5lnhkPUqaZ5LM26UOhqqU22XK0XGZJThXHlxYJdsBKE5k8um8JaD9wXg2a6PzgF5mRt9eVCcq3E-BQIpNkZpr32XDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kj_yTzmFVB-tsS-l1-axgaqA7JeaYa1JnPqOE0Oi9nAXR4rRs5ukxJeliHsSDidCxbYQ5WAPHpizsbUJMAzAbUWax2LPq_0V3Nj9xUPkqJq6njSNEuTxUAmKQbRaEti1aPtcxh7EgxqyhsK-zHPczMtMBav68qFMzStSkMNsKl0e4CRE5MgWPRcA2kVkA9jvBQBW1gOYqhqGpOOkwaQjAsTBvnVcU5UZ1YED8MoInhznpFnX1SVdAUEnSZQCinX2N2Xn6hGZ24h29xMzYq34jKll-VoF59cKjl1smwWHtef7_3ainW6Wgh_J5LNf3rnExkdTPIUuMxeyVZ9ULNe32w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید ملی‌پوشان از ورزشگاه لومن فیلد(محل بازی با مصر) در میان استقبال هواداران ایرانی
@Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/444831" target="_blank">📅 09:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444830">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حملهٔ پهپادی رژیم صهیونی به جنوب لبنان
🔹
خبرنگار المیادین در جنوب لبنان از حملهٔ پهپادی رژیم صهیونیستی به شهرک المنصوری در شهرستان صور خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/444830" target="_blank">📅 09:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444823">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7aqrA6SNUjDmOB2BlfCT6UYIE5moNA_XpemiZc6A3sYvLQ9rENZxw8bZZ5_lMM6EDeaxDjtQ9CWvjhdUnPZKGrch9pYHbcDsvay-mhth0Z6v-E6LGJt06ZOPIJpdl1wokQOMQFFmvldHYbRIeiUPEWDmUT_xKo3rw4i2oLwGjaSEJ0II94QVTvRwQSSOQYJmZr23eXWC3Y_65kV0FuFT1FKcbDhqE_hpLfusLrdu60k4bDvhkGP8u70FJqs_wATFqaE9cO3rCC3vA8GHqAlqApJij6ZWYYreoQU2TE0DsPAsV6YwKiaQ5kQG8BCAp5zDMAdWP8rO8tlzIzoisFT2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlDQpcpr3tSXfy9SWVH31o7MGZcaFkknKgdNWb5T4m9AvwUUSHH8PZtZpA3MMieTEcQ3KRu_gNI_Cg1kYhnWwrioo3U5cI_iSDAef5foOoMILhqMJEg7XPRJSzmq6URWMRGC0EBxoYDbSvWyFo6WoD7YUt0vyY7ePw-_qc142j_KaKacIMsQpvi0vAd_a5ujqERVvPslueCER6SB7M9NZpahVSb74b14czFYAj3v1Gf97Zt_PaM3W76D1YDLZRPcKO9gcUDYSTXdcdm5oljly-IcYX80J9bOhRVtwxC8CfHvXQ5xiI359YqK3Y9j_zzBh_nkTbfVRRcojweIHx5FDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9atwd4y5MCaOgps_Q0R2dhyFzpm2gjZFHLTZBpoTpTE9wg0RG3hA3DmEGXTm2FqMQoQxGGiUi24SqIn3ahgb8n4L7D6Yo9Cr6qbzD4BcHeZmhBa64_lBzBawgcA2_xziHtxX6Va8Ao5BnBoPskQiaNuETJ1hyByYbqjXCtdm67MD4-kY15gbwXOBSUfQb2WZY72DZPbRAaI81KcrmF7RvHdhmeR4-BBgy08N1Sj7xzv4OGwyEcuvQkvZUN7p7MTafBx00xP2pcea5rLmGAucnM_3S0NEjyqdbpbnfxYtCIFFg92ISGFi0SZMUV5sGAO_jH9eVoc7vvzTa1SVPiBBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DYM2RLUPO8JLutqliXrTjaPNkAjhJPjMUnFSgfkqRVTrwSIBQ58JmYtfNcKVQja7cHsz_K8kJdzAd3N3tiJ9dKpIXAJXYLSpzYEjiw5jFXU8FMnxToOW7DmAla6YFIAgd4WTfnTOYigz8jcN5LRxSU26cRP5F7FzsAUdWAajryWxdiPqnhBr-At_S3DzYAbj7Yhp9zUNQstoUgAh478CulxH-_jnOe9RRD_9mFCtMGBk5ZIIZrWJ9g93umIzT2JjgCWFFe6ipKh1F-L5dArJmq3yd-WW-DS3gqPf-KejdF2LCuF-4OUaBKfYYxNqcucjgqgZzadw2DZ_ypJtdHF8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBzVPNfB9iz4bWXQZPQyLdvi4pPi6dpVpS4wJlBpjUxlHfYBEEW3Lnod0KycxmxNuq8AnHtjykHVvtOqY3abHJHvMRFd5jfJKuJpQmql888f-gpgziL5M0CJ7lHN2oMK7yPzrwDpGPdQxmLJs0bAqqJhJ-8JzKWdPOdhzOTd_GnWqM4yjmAykFiqqJoXvIBZXT4iOHXj9sns4DEujlqpeaWzP_pGa3BOB4nhTGlOUbI8Q0EWzyMy8jRTfw4HzPzEpjHxc0fbOKtgYzVMRbjc9lGSzrvjLu7bEVKZy4WqntNIIOJ4QD8a6TiFfP7QKxO1UcBVcrCyZl7hZbpTkMgi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Po-9spR8NrztUDsqjeIklnVaFa9UggjaF4rY13QevjWwlVe2Oj82M3aTkkiZd63SzrJz-XNwUxIpoCMlG1VOBRPHu8zcslEBAdgDNZETBpJzaTRTNlC4unAbw_0T4IZnVe_4cswi4UHXbsQVLhj8Fq6nI62NQPy4PrfoDtZm1VF2kqgIuMlAPRgHRnzxjPQkfSTs-91Hw2XcNs8mQvUhQwYZDO9DELisdlIrNrtr8AHzKR9y6FW0cSvqB815yvd7ioKiv6C6ecbIRKxp9Epevlxt0dTceZKBIACCTkseCqG5UC7OP4wVU0t_Qznic_hTZIYcDUn8sxPrxrBTKOdO7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-HtTTCzJsZwuOtFllEgHBN5nlkCFeGYD5eu_jQ0LQJKPRu5jNVxjUDV-QKx7OhN1o56SrX8cLluDnRMmCaRG7cpLTSleLv5VtU8bgRCwfgZ72dtDTONVYLgMku7KCvfl01op5lYh1pADz9wJKYcCQY98Pcuq9SXniTZ-KeX2O5lYQL2YyrCv3RnfCOsTv1JCk9rAgJNIYlvknR6NXc2XYHgZApGnkoYLqGlhylzefVw8vapMFjed7tPWI0aJ8BBaSWpep6GLfEIyS9z67ZvK8yTkcPjtN_Rof7Ork053vHJDVwybYERKZtMEPK8c8BtXnHCKubIqkzYw6fUMHCVCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین ۴۵۰ سالهٔ نخل‌برداری روز عاشورا در یزد
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444823" target="_blank">📅 09:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444822">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7z9U4C4fu_9MYef0y6B3c8WbW9NaHURXWiUtYVAbx1tQ3f7ZwfD0yQyb73JJZeCaqcSUG5R8iP-3ytuyqVwJiHVkv1q4G0NIc6_ODnQP8VFx6grThCPZoVZDDj_uQseK0Pk1qWKNr-hWZKJ8oFGkhI_PLpm2co-kj0dHpSoeCfI1S08zlZ7UMWwo1pJQYpFG6KrrDpWjJwxKZvDIxDeg66pVTsfUfe4W5CsDkx8H8TWnPq3JqTmihsAAgwe5_gbpDjK4KaH4AeotJMa4bqMi_mxzIC_Bp_wP0b_f2nk3ed_cJK4Qrr7ydISVGYyMZ1UyTyGJsqBJGLox-nWMzN3rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیهٔ تیم ملی دربارهٔ احتمال تبلیغات همجنس‌‌گرایی در بازی مقابل مصر
🔹
فیفا به هر دو تیم شرکت‌کننده اطمینان داده است که هیچ‌گونه مراسم یا فعالیت تبلیغاتی مرتبط با این موضوع در داخل ورزشگاه یا به‌عنوان بخشی از برنامه رسمی مسابقه برگزار نخواهد شد.
🔹
موضع ایران این است که هیچ‌گونه مراسم یا فعالیت تبلیغاتی مرتبط با این پروژه نباید در داخل ورزشگاه یا به عنوان بخشی از فضای مسابقه برگزار شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444822" target="_blank">📅 08:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444821">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c3d38816.mp4?token=rQyMrdCGhacJBZwDwXlpudfsyp2XLqciQoJw5FhqvamRb_C0ICrdY-6zbG9uEzkHLvnS8Sdq2DRU6J94IEvQewbLYZAj7Y6icnJKVCdzMa74_j6OtZGdYIrcyX6DBw7wTmT2QpYtGOOQvpF76whiD0UI9HmGfbUT_-eZE4aqwaetL073rzvPOw0JP4TaGvvPqdw9776FbYtX0YGJaUbd3VatW3NgvdP1C15vn7jUnpOJEwmr8VT3gaNibo0MDHjS1xMUC2Pn7NXlebwq7LnqARgrFZNzFnXzJprUPDXahzqeUNd3VdgfGIU7pUDo9Q5PAZbPaJe9yvIiuHGqdERiQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c3d38816.mp4?token=rQyMrdCGhacJBZwDwXlpudfsyp2XLqciQoJw5FhqvamRb_C0ICrdY-6zbG9uEzkHLvnS8Sdq2DRU6J94IEvQewbLYZAj7Y6icnJKVCdzMa74_j6OtZGdYIrcyX6DBw7wTmT2QpYtGOOQvpF76whiD0UI9HmGfbUT_-eZE4aqwaetL073rzvPOw0JP4TaGvvPqdw9776FbYtX0YGJaUbd3VatW3NgvdP1C15vn7jUnpOJEwmr8VT3gaNibo0MDHjS1xMUC2Pn7NXlebwq7LnqARgrFZNzFnXzJprUPDXahzqeUNd3VdgfGIU7pUDo9Q5PAZbPaJe9yvIiuHGqdERiQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این سگ رباتیک در سرمای کشنده هم متوقف نمی‌شود
شرکت چینی «دیپ رباتیکس» از نسل جدید سگ رباتیک خود را با قابلیت‌های زیر رونمایی کرد:
🔹
عبور از رودخانه یخ‌زده با عمق ۸۰ سانتی‌متر
🔹
حرکت در دمای منفی ۳۰ درجه سانتی‌گراد
🔹
صعود از شیب‌های ۴۵ درجه و عبور از مسیرهای سنگلاخی
🔹
فعالیت در ارتفاع بیش از ۵ هزار متر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/444821" target="_blank">📅 08:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444820">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMHK9Iw6jQg3M7sV5Sq4aGouWjS1uAqNkB8Js8gcz05txG2kgmhRIxoNdVBwiUNtbpMeH4LdkUFF6te4L_dJqn5bHnotZeLx0OVIs2Nx3mwNUZw9zFCxl6dfWg6B4_l9avYm3-XD7pz8lCbIPYncUu6kvNX_9DRo6NNBTGZRlCzoSpRBkqBtVUX8m7Fxhtb4plUzLiPS2WDM5nLl2zIevCvOaOCdSGMNAm342RI5_sRzWWXdyDmkn3qyiMVrTM_4GnRyzhXkMESA1M5FZPcarv_XfaKFqp76lXar0J_OwwXy4618Duv-64B53Otvvy9tgnlw5D3amBeGTaZIeGUjNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا خواستار بازگشایی سفارت کشورش در ایران شد
🔹
مارک کارنی: کانادا باید دفاتر نمایندگی دیپلماتیک خود را در ایران و ونزوئلا بازگشایی کند. داشتن سفارت و خدمات کنسولی در یک کشور به معنای تأیید سیاست‌های آن کشور نیست.
🔹
دولت کانادا سال ۲۰۱۲ تحت فشارهای آمریکا و رژیم صهیونیستی به روابط دیپلماتیک با ایران خاتمه داد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/444820" target="_blank">📅 07:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444819">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/784bb86381.mp4?token=eYY-zBasdgwixABq8oi147j5fKjyBDRYzPhnLpPSNwn8XKgkSgd6RuzLvLIypHPaQSZtvmitXZ7l4yTaEUylftp2hv2SPgXDP_NW15zZltizAtb3tp6UvY3Ar3g9OAMizE_JUoQTDsI5hlJ0iNNh0Zqh4nrY5eGBvLPM4JkZR_o-Ih0vZPm_AAamh0bIy2GkxBdeUStp3qlK_lXDekrgexebgfw4BPaHdgxCo9zZW5D3zmQiZLOagMZ1VkSBBHoL3lIvKqKVCHzW6JZNKW4xKctlkZbcwz4-ojxiVgce30G2Ty37mxtwNa53c11-tVI7ZyzVH1GuR9mA83oDtorsYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/784bb86381.mp4?token=eYY-zBasdgwixABq8oi147j5fKjyBDRYzPhnLpPSNwn8XKgkSgd6RuzLvLIypHPaQSZtvmitXZ7l4yTaEUylftp2hv2SPgXDP_NW15zZltizAtb3tp6UvY3Ar3g9OAMizE_JUoQTDsI5hlJ0iNNh0Zqh4nrY5eGBvLPM4JkZR_o-Ih0vZPm_AAamh0bIy2GkxBdeUStp3qlK_lXDekrgexebgfw4BPaHdgxCo9zZW5D3zmQiZLOagMZ1VkSBBHoL3lIvKqKVCHzW6JZNKW4xKctlkZbcwz4-ojxiVgce30G2Ty37mxtwNa53c11-tVI7ZyzVH1GuR9mA83oDtorsYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش جالب افسر نظامی عراقی به عکس رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444819" target="_blank">📅 06:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444818">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bcd71e97e.mp4?token=YClai60EKpYTaqvEFqEhiy_pMZ494dH9WpP_S7VFdPEuCzhJMtqsgsf5GySemkAEE-St-4QPxxw3g0kofkFUGq4FpcUf0NJyWygf_CayWrgnKmhRVw6nxHK9oWkAG0CywWN5YjZVBl9Sv58cbu_z7eFt1AWgNfWnc5OFZD8k9nQyeH3ixqe5UWJ69fjjBYbfDR2PZpK8IkDqbpEj1ISNeTj5DSWPNWGg-tVfivrJX0hfyVSyS2xjKBsVUvs04uhAe3qIQx2R8TxAe6GgFHI9Zk-LLQ5MNq4nrFf79y_9iysBfrmUEXErj5BZsSEXt9cxQ1xLhtCZJWgUsSRsDuESaXynfH0CgPUyNsIypeF2Il7_OyKtk6d17BIEqbwZ57-ieFzZogLcvZ3gnupB0S0PRpNFV2VJenpfJGIqF4EUk1de5zPHlr8jJQHX9b7wo_rQiooY9VrguTvjvVUK32VZarK3_NS5oV9dx3NZjjVKC81kc3XFvrW7IP-csXwt0Af1SAlMImmUDfkPKHO0JvSXycf4yhe1EKGf4YO-uqfI3XCdLfkubupNYZH6QOfqTCIk4ap4SaBHfzAWqybV2jQ7gdJPjkQ8cfXYWQVgQoReHJHxfCKMJoByGDXjP9iSRuvrQtkO-q9Q-8ostXxV1_bGAo-QQuFfxMNGlw4qNGvll5U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bcd71e97e.mp4?token=YClai60EKpYTaqvEFqEhiy_pMZ494dH9WpP_S7VFdPEuCzhJMtqsgsf5GySemkAEE-St-4QPxxw3g0kofkFUGq4FpcUf0NJyWygf_CayWrgnKmhRVw6nxHK9oWkAG0CywWN5YjZVBl9Sv58cbu_z7eFt1AWgNfWnc5OFZD8k9nQyeH3ixqe5UWJ69fjjBYbfDR2PZpK8IkDqbpEj1ISNeTj5DSWPNWGg-tVfivrJX0hfyVSyS2xjKBsVUvs04uhAe3qIQx2R8TxAe6GgFHI9Zk-LLQ5MNq4nrFf79y_9iysBfrmUEXErj5BZsSEXt9cxQ1xLhtCZJWgUsSRsDuESaXynfH0CgPUyNsIypeF2Il7_OyKtk6d17BIEqbwZ57-ieFzZogLcvZ3gnupB0S0PRpNFV2VJenpfJGIqF4EUk1de5zPHlr8jJQHX9b7wo_rQiooY9VrguTvjvVUK32VZarK3_NS5oV9dx3NZjjVKC81kc3XFvrW7IP-csXwt0Af1SAlMImmUDfkPKHO0JvSXycf4yhe1EKGf4YO-uqfI3XCdLfkubupNYZH6QOfqTCIk4ap4SaBHfzAWqybV2jQ7gdJPjkQ8cfXYWQVgQoReHJHxfCKMJoByGDXjP9iSRuvrQtkO-q9Q-8ostXxV1_bGAo-QQuFfxMNGlw4qNGvll5U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلوه‌ای از عزاداری مردم گناوه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444818" target="_blank">📅 05:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444817">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a8626732.mp4?token=nhWF9GKb-VDco5FoIyMELZ-uK9oB86UePO9Pm-7uUmNbEDGMOcjJ_e7VbEoBAck9x5DjU51LsP9e1C6u6yGy_3zx_C36aeMVvLPYvgFQjrSNmtwidIODoKG61S2s8o09FtLw71hNXmmCSsNcBw-UY4cWxbhscOC_aXMNM-0VhRvn121rv-nhyC14v5rrfl14xG_1qrD-tntONFoWgALSujBEhr9rWpVuZnTjbDrg1xUEALwjKQFyDpYFgpHocDlbsQ0ePjwD2SyoJuvbtGpWOaMrXFZmc0k90imPD5L6Xn-be7SAt7XF7wE68UbTypMaHrDv1WmYbs6PufoiN_T-2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a8626732.mp4?token=nhWF9GKb-VDco5FoIyMELZ-uK9oB86UePO9Pm-7uUmNbEDGMOcjJ_e7VbEoBAck9x5DjU51LsP9e1C6u6yGy_3zx_C36aeMVvLPYvgFQjrSNmtwidIODoKG61S2s8o09FtLw71hNXmmCSsNcBw-UY4cWxbhscOC_aXMNM-0VhRvn121rv-nhyC14v5rrfl14xG_1qrD-tntONFoWgALSujBEhr9rWpVuZnTjbDrg1xUEALwjKQFyDpYFgpHocDlbsQ0ePjwD2SyoJuvbtGpWOaMrXFZmc0k90imPD5L6Xn-be7SAt7XF7wE68UbTypMaHrDv1WmYbs6PufoiN_T-2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام وفاداری از پاراچنار پاکستان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/444817" target="_blank">📅 05:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444816">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61bb005091.mp4?token=awo2FKmzlH3Kaml3v12uXklGhhwS6lNtnAz6hpPrmtc0XQw7jPy2lYTgBBiW495dCp2NdlUTsEKD9XCqAD0QiuHL10BFR5Oos9NHH0b6zJA7_6NNyUwvg5uy7B6s1eN3rVmsCb2IoPlqHspxQgopum72uActFkihiAQR0RUwA1E66IziPQ0-aaGPPveejtfi2heoyPtz0vs5x2ILN_pqB5C6zXDO32-CZ57zKu-ptyo29bnoHEW1MwFhpBjp2mnigH3AtwXEQVVjsDmyFNdeznuCioAjTSXBqqcBqK7grQxBqyuecZYPHhYtKtfv11v-pekUmuLNIgX5ys2jwZvoh1-zjc4sfmr_8dxLxg071l29MFk5pX62vsjjU55fL3S5ButCxypZHcUC6jKudrIXztMAWR9VOutYMgcrJpMLbi3HjKusbSrHagU7wjMGAGyJM2GZKrIwvlW1zkCLACznCsfCjGgJlxHfKmde69VDa0c8TATWncvV2UNWJUQ6Mfg9sn84arjePseUhLGXu_tZtQdT8tSpfHAQURApZTU5PSiQDU_iXYlQEW69sZ9beaSMVxXS0eWRxTmUpntT8USEZ6RlkDx_jbKMXyCvisFmRFaIcerzRfbOLbzAkVw8SI07Q-IYn6SrjcG6Nz9q8hTNV6G3TEd6eDd9xsTvE4lqLc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61bb005091.mp4?token=awo2FKmzlH3Kaml3v12uXklGhhwS6lNtnAz6hpPrmtc0XQw7jPy2lYTgBBiW495dCp2NdlUTsEKD9XCqAD0QiuHL10BFR5Oos9NHH0b6zJA7_6NNyUwvg5uy7B6s1eN3rVmsCb2IoPlqHspxQgopum72uActFkihiAQR0RUwA1E66IziPQ0-aaGPPveejtfi2heoyPtz0vs5x2ILN_pqB5C6zXDO32-CZ57zKu-ptyo29bnoHEW1MwFhpBjp2mnigH3AtwXEQVVjsDmyFNdeznuCioAjTSXBqqcBqK7grQxBqyuecZYPHhYtKtfv11v-pekUmuLNIgX5ys2jwZvoh1-zjc4sfmr_8dxLxg071l29MFk5pX62vsjjU55fL3S5ButCxypZHcUC6jKudrIXztMAWR9VOutYMgcrJpMLbi3HjKusbSrHagU7wjMGAGyJM2GZKrIwvlW1zkCLACznCsfCjGgJlxHfKmde69VDa0c8TATWncvV2UNWJUQ6Mfg9sn84arjePseUhLGXu_tZtQdT8tSpfHAQURApZTU5PSiQDU_iXYlQEW69sZ9beaSMVxXS0eWRxTmUpntT8USEZ6RlkDx_jbKMXyCvisFmRFaIcerzRfbOLbzAkVw8SI07Q-IYn6SrjcG6Nz9q8hTNV6G3TEd6eDd9xsTvE4lqLc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بغض پاتاوه در سوگ سیدالشهدا(ع) و فراق رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/444816" target="_blank">📅 05:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444815">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28f1f8624.mp4?token=bV7sAqX5Spyj6uk6cv_zbw2t-idrBcBgsMpHD6qlHSFfz5o0tyCLYwx2eRkaIUDc-3B-eoujnFvalMCpM7a-9XdKcXvG5bfBXaJFE1pbziTXc5QTHAea6mDQq9SbxIiiUaO7aZf8IWdMp-g3xxwOhEU2hOdZDcA-H-zXbKrnyCH7gCV4W4DqHGxUzRE7AH96ZQ0vAbOmV3QWVh5bpwhGV8sncfucrydtry4mkjri5qs7DDfTE6CD_653r3p_ds92osS9OtpaK0jgYo8TyoRipMlIdV_xMVafuglb_MGRmMicQHEAtlmwaplAvlQSY4XxlL1SFgSuHBZ05_HTnY5b7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28f1f8624.mp4?token=bV7sAqX5Spyj6uk6cv_zbw2t-idrBcBgsMpHD6qlHSFfz5o0tyCLYwx2eRkaIUDc-3B-eoujnFvalMCpM7a-9XdKcXvG5bfBXaJFE1pbziTXc5QTHAea6mDQq9SbxIiiUaO7aZf8IWdMp-g3xxwOhEU2hOdZDcA-H-zXbKrnyCH7gCV4W4DqHGxUzRE7AH96ZQ0vAbOmV3QWVh5bpwhGV8sncfucrydtry4mkjri5qs7DDfTE6CD_653r3p_ds92osS9OtpaK0jgYo8TyoRipMlIdV_xMVafuglb_MGRmMicQHEAtlmwaplAvlQSY4XxlL1SFgSuHBZ05_HTnY5b7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش سوگواران یاسوجی در شام غریبان سیدالشهدا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/444815" target="_blank">📅 04:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444814">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8058afc21d.mp4?token=cqBwtZBLQrkfglTyX2aiQxrjVUYb6K69HuBLRkZdWwFvX2GFCa1gYI_d6hi3FPXLWqRb-d_wWKb-wKGXmheD6OP20kwlPsJmOzwX0fhz1czyi7gloJ6ZL3UDOX93NeBSCktYcrQrjR0PwcChGaFqqT0mEquAphAovoFfbyKQhS9ZH5s6AWUB3jKI06ZUhyJ65QdW-LB7H5x3VaZKhzDkzdMNZaxj98scxjUPMGEP_YxvAJ3AuIOdcCQsYg7YdcSCby8YiKCqFDq8OmCAw7LAxRLVHNxjh_8wGYUCENXlyO2hNkAOKq6MWRkCJpLl8ZlpUm1dyk_xVCcOj5OH-8fG7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8058afc21d.mp4?token=cqBwtZBLQrkfglTyX2aiQxrjVUYb6K69HuBLRkZdWwFvX2GFCa1gYI_d6hi3FPXLWqRb-d_wWKb-wKGXmheD6OP20kwlPsJmOzwX0fhz1czyi7gloJ6ZL3UDOX93NeBSCktYcrQrjR0PwcChGaFqqT0mEquAphAovoFfbyKQhS9ZH5s6AWUB3jKI06ZUhyJ65QdW-LB7H5x3VaZKhzDkzdMNZaxj98scxjUPMGEP_YxvAJ3AuIOdcCQsYg7YdcSCby8YiKCqFDq8OmCAw7LAxRLVHNxjh_8wGYUCENXlyO2hNkAOKq6MWRkCJpLl8ZlpUm1dyk_xVCcOj5OH-8fG7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شام غریبان حسینی در اجتماع مردمی گرگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/444814" target="_blank">📅 04:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444813">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5df31ea72.mp4?token=ZogIeZVHj6t6M4NVjjAFH4E1JtVrFQ6byDwA_kj_GJsrWgLCPvo0RMt7YhrtacP2rF55ovHajYq0ZVs4E8S_6acLdWpX4QnjQ0auKbpQ1xsP3nCC3ckObJDZsk2D__7NxU7GkYf57394RihCpn8D8lSD11yo3CJKfNMSMUxBLg7cMMt7VJiWN7ppb8O7eHD3yw5Hhwwq9NPtuD7Mb715jLRQyyk__8Cp694S1DmiBv2GDCcptxaN5F8Ba644HFxSeQsPy3eRis9MRCpEazS2dqWz-q4yfYmgitu_8v4JvJ_qCxIVaPr-du23pB62sCMXvVn_gYpim6STZKk_0x3nLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5df31ea72.mp4?token=ZogIeZVHj6t6M4NVjjAFH4E1JtVrFQ6byDwA_kj_GJsrWgLCPvo0RMt7YhrtacP2rF55ovHajYq0ZVs4E8S_6acLdWpX4QnjQ0auKbpQ1xsP3nCC3ckObJDZsk2D__7NxU7GkYf57394RihCpn8D8lSD11yo3CJKfNMSMUxBLg7cMMt7VJiWN7ppb8O7eHD3yw5Hhwwq9NPtuD7Mb715jLRQyyk__8Cp694S1DmiBv2GDCcptxaN5F8Ba644HFxSeQsPy3eRis9MRCpEazS2dqWz-q4yfYmgitu_8v4JvJ_qCxIVaPr-du23pB62sCMXvVn_gYpim6STZKk_0x3nLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستاده می‌میرم به‌خاطر این پرچم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/444813" target="_blank">📅 04:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444812">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4deb9721d7.mp4?token=PaJUUmUszoz9-0gjYlxKdNy612RxfEAsPRRouH-Je4BwpwquO9_7PX468fF2VraVIz9GeTlR8IQuK_yWN11THqb_hzIivb_39FP5XhvmQOykpAopB6-YHq3Q23_8eDAiwCNlfm53WSWPurHp5jCmZrSc89Es7cN9n2gjnCGJuLwXtym4hiVqvFkygFGdBzfrxORjdW-j_F7cZnrSxNwk1i89o79fr9kvIeitxLZQNrEjJ5kdKQLoMCYcvAOSkpHTioYNeHGmGXUh70nQVoPQ_6Bdqgu5F6vsxCAJXU21IqoJjgsWY3LoVXCJnLpHhpCMXGFqkBr2ee3Q8gpMY2Yq6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4deb9721d7.mp4?token=PaJUUmUszoz9-0gjYlxKdNy612RxfEAsPRRouH-Je4BwpwquO9_7PX468fF2VraVIz9GeTlR8IQuK_yWN11THqb_hzIivb_39FP5XhvmQOykpAopB6-YHq3Q23_8eDAiwCNlfm53WSWPurHp5jCmZrSc89Es7cN9n2gjnCGJuLwXtym4hiVqvFkygFGdBzfrxORjdW-j_F7cZnrSxNwk1i89o79fr9kvIeitxLZQNrEjJ5kdKQLoMCYcvAOSkpHTioYNeHGmGXUh70nQVoPQ_6Bdqgu5F6vsxCAJXU21IqoJjgsWY3LoVXCJnLpHhpCMXGFqkBr2ee3Q8gpMY2Yq6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سینه‌زنی مردم روستای ابرسج شاهرود در شام غریبان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/444812" target="_blank">📅 04:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444805">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IEqUPZthRDAKrBbIZJ871SV7b0oDxfcidvfauatKxG0fnCGOW5XL1Y0pigeDH8IXvpC7HAGYoFlh7sTaCI26osGBUk15sRaqhaHytOwqIMaSh9FRlfd15biMpBQCZZB5vcluYdXpgSzf82OXL6S3AoRyO38k74F9PPfYr3FsA0Zrcz10jRjpMR_TlW5s9MIBQ0lha2sT67bt3pD2hd-EBK46skGElNfnn2PWFO2ALHeA5bDcB1so-TWmUjLVasBvuZjaiv4NEOWVJsOV6ikSgS0zc11KT8qJd-TpuOQo7DoEfatfA6cbA2vUkO-v8kCp5w0VGVm-CFN9pt5WnByaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3oDqS40ByoXKefuLk0niMfZP16QHoGeCkXzO0Z7U0Q-wYOEFB9PVG0GM0GvY0RzbI_QDjoOyOm9RjIkoywRlcHHlUEEaXs7SgNrCzAc0gXdYsKzH1y3GgdNEfp0CMOaviavi3eZaTnJAR-31WC_b1T3EQU3-fLPLP713Fk13mW0eKDVx2ohwPgIP4e5kDeIpL6kU-A2JaXJZCrLIIzAi_czOEnkbLG_ehdf_YcDHvmR3__t_jinqE1nfEpJGXcDexw8IpOOvIZ0yuX1tWAxxF5BbPcHDDT7GQQlHBCjb2QeZE7K3V4Oq8v-S_QTRVV-CRyqS2HRt9hgC7lNC9RsLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3gHmywQWOTl37-8c9U29Pf2qPs00B3YpY7XWnqz1dkWCBdpF6ZkXPKJBM2giUatqYMPEAZv9zostu9adgMW3d_Zc5qZ6QyarAA90QQA3W_v0tHMbxzriCYy3opqd9LMiEwJGOVsMSP7b6DG29WuiB14ei00bagkcvKOylxXCCLP01Uszci1HwRCb-2eI2MvwBNmVnMO5zuruHJo1yreLefn8sbaWVdSxrvLejzoQxQjYlO-Y1UgOpSX232NoIadbZ8XNgh8wlEobL3kFOTkRs3i-TJsyv_j4NLa2bRghKCvwYO0aPSFkENPNFpfu1Vsgfqo0Q5cGRPQwTLM0V5Q3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdqupQNiJXPWflEth0aS7i_nX07o280C_aUZZCyw0R3xjDI6jWBlO0HVvtRvigzCZco7cZInFtVc756hPUwOpN9T5Mx1VurpyNGUoDq1u_t5Mue4viWz6pM2BVlPbQrQGUY4frPTHkRYUhG4BLLUrsFuj90cOlzy4KkXKjbmHYF1pTWmdtKYEpPjtbN_bPRcO1eaO5GaA564-6bZOy__B3vZDPp27Z7RWnbZe962eyrdYyFYm0ud_-ScRl6lbQbCGu0DBzQXkbJqDZKPvUFH3IfjUKV7gP9lU1guP8f3TCfbAKugLPvQ3CdZfksoekG0SdvN1ItGYAS2hYmtZMcMHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCzuPfNc3C4XixAj2pneOF8QibTXw16xVmsfFAF-fC4i-bbgsG5AjTae486ARMs3_aaPjafso1aw9JYPrb2wnH831X8Hdu6_KnWe2nL1_r2YsjgTCqgG0c6XnMMtZdzS-JtHuyUPU3VhXQqYUz23GJBNIrPXiR4rOfDL7FewtilC0yX78m2QSJuAbwnDbIMcJ6KpvwJyQhkwE5XPDDDKSP-5TFY81dRH4Yi0Cjj9EmQ9EwJo9y6ulMeqUluLPZdFhhViuHbPyFbsG7_3iwKNhW0muk_SQqtm2rFG3ifzP_2tmlnERgo-r5nJTc2ljNUKvHMQlNSJRR_xJqEIypaqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pU5aiIh_cYntJUm1oKzDvdnIPW8bhHctRH4Ww4FveSt9qFlF9ObnCo5V6kL0ozGVbgAhqASfpr-bb744RJG0dOnuK3wk4gTFoVvhzTAMygqwrJb00NzO6LW1c3Ga5CDLuDdxsss1hrr3_G2VvS6mTpAL5aHgfJpZJGudha1PQvM-wBZy_uhIbgSF2t6wgYJ1RuiMxhcM8bBpuL2LrmdBdFhp7dD-TziILsUkbDP-8t9J-tt53z8IDvTN2XMEXY4yTI-mKeRk8evDR1IFACECyazTfaT12psntvaB09NyXI4IDTz6KaqXbZJQRlw7q_76OQj7j7ZcC4esy0_9fg179A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MB2eQeIeuJ1wnMxZ9mRY9682QIWu1yUiZwdEJsjV0M768QyLKv-0TKUmwbrTEWFxyZxHMFDpsD9n8x8cDPDtOuSxB9cPsJVNsXJCzGl96RdnsIA0qlE2t-UO2GPZl1xTGxyfnyw7aGjRRi8bb6pQPtTPwvosRSx3L3y2JAFwbXxOLuy7LYmOCt2eEMWhUEzZVXCwA_rEygfB_ftk-nhKCQqT072E9mL77ooXDtLlw_tBvT2i5ewxolxpX5Q19kb6VqbhcfAio64ZJd5eXVE7MdYi2NKsATqWyDwnE8EvIQo6n2mapxy7b4eLa4LAnDqYNChXY7ADfBdQuPIr2HeQ4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شام غریبان حسینی در حرم مطهر رضوی
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/444805" target="_blank">📅 03:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444804">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d1b948b1.mp4?token=Uyz3HNr820M9Z-92juCl-580E3rmBD9Qpn1hEW7UNkyp9ehUf4FnvXpXv6IXB2U4koIOHOb4Er7ChFpPJLKaHEaCChJu-m_7-ob8s8abGjsJdhZ1xvU_gGPhh-xDj_prwoj3TUcPZu5ilvMeHWsH3V0dadmTuCZOkumbUh2aRgFaTR2PpZSK9PCSD2iUuV6V3vrBRgVqxGrynsIRnXRrJuaUbUKi3E3Hrs4_MXfDDgS-b49xXOW3LC4dLYRR9MLbmGPe8vMDpRp01lDAwD81oY7vY4ADcehPRdJcNtfxJ8JJflTpO3wpv_dvazpqTkkooCHC1XD1-1EwEnm3fpFFaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d1b948b1.mp4?token=Uyz3HNr820M9Z-92juCl-580E3rmBD9Qpn1hEW7UNkyp9ehUf4FnvXpXv6IXB2U4koIOHOb4Er7ChFpPJLKaHEaCChJu-m_7-ob8s8abGjsJdhZ1xvU_gGPhh-xDj_prwoj3TUcPZu5ilvMeHWsH3V0dadmTuCZOkumbUh2aRgFaTR2PpZSK9PCSD2iUuV6V3vrBRgVqxGrynsIRnXRrJuaUbUKi3E3Hrs4_MXfDDgS-b49xXOW3LC4dLYRR9MLbmGPe8vMDpRp01lDAwD81oY7vY4ADcehPRdJcNtfxJ8JJflTpO3wpv_dvazpqTkkooCHC1XD1-1EwEnm3fpFFaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دسته‌روی شام غریبان در فاروج خراسان‌شمالی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/444804" target="_blank">📅 03:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444803">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86078b1ca1.mp4?token=e1eaWp_r6h_f5swg1y7aYkHhX7BEV8cmeEU7hU0CZ66GsVCEN84H2GueY2JBwFBNtJwV6iC8MKVOQ5TDbI1aHliaeMd74Rn9GZ-rtD0l69ITqVwwu4HdgPJWYZ4bSO8s9MEc6UMy3uihHJRxCqNQ7CZ6K25wsHUdmy_2fKlLI8C0XpRg_-xc-DpYSSPpOI3ghKIQExI7gTazE57cnwh95UVpRq0smePSMcI3UirzhZx16JGMpjiCMLC-JGKXeNLiN9RsY9mznwkT21EbCCbgI1YuZUbV6tD846U3vsclM6TtqIDP89YLzkKtnwA8M-MMGj8nljMZ6H2n0rR6DFxacg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86078b1ca1.mp4?token=e1eaWp_r6h_f5swg1y7aYkHhX7BEV8cmeEU7hU0CZ66GsVCEN84H2GueY2JBwFBNtJwV6iC8MKVOQ5TDbI1aHliaeMd74Rn9GZ-rtD0l69ITqVwwu4HdgPJWYZ4bSO8s9MEc6UMy3uihHJRxCqNQ7CZ6K25wsHUdmy_2fKlLI8C0XpRg_-xc-DpYSSPpOI3ghKIQExI7gTazE57cnwh95UVpRq0smePSMcI3UirzhZx16JGMpjiCMLC-JGKXeNLiN9RsY9mznwkT21EbCCbgI1YuZUbV6tD846U3vsclM6TtqIDP89YLzkKtnwA8M-MMGj8nljMZ6H2n0rR6DFxacg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت دلدادگی مردم مشگین‌شهر اردبیل در شام غریبان حسینی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/444803" target="_blank">📅 03:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444802">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9971189333.mp4?token=p1CejIE2bkUicWx3YfDUP3iLGqhhXI8p8l-210ymLRzlRxqJ2tjCJj1_UUfZWvWIzpMZlFHNDz24JvxiNW0yuX1nR-PlWe_3fHKTiEIZADDe2HnJDxghywA9wM6KeCW7JI2ZtEOYxjLR2xXgirm-bHZ13NBTd_9IsOnG8a2zbsX7yh5UEN_L7USt5N4eLfGppFySECi8WgUKeW_RMFOUd-ie2CaDsqt-ae6OScM9RrwEOmNzjOicrXHRkUcV_sCDnyuQ_H9qZPbaSLf9C3d_9Nvgb5fSYhnVO1rc-W7-gKzmKZoWz33ezJuuvrsu5wEhtF2Lo0ZWUy7MJqkf4xZYhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9971189333.mp4?token=p1CejIE2bkUicWx3YfDUP3iLGqhhXI8p8l-210ymLRzlRxqJ2tjCJj1_UUfZWvWIzpMZlFHNDz24JvxiNW0yuX1nR-PlWe_3fHKTiEIZADDe2HnJDxghywA9wM6KeCW7JI2ZtEOYxjLR2xXgirm-bHZ13NBTd_9IsOnG8a2zbsX7yh5UEN_L7USt5N4eLfGppFySECi8WgUKeW_RMFOUd-ie2CaDsqt-ae6OScM9RrwEOmNzjOicrXHRkUcV_sCDnyuQ_H9qZPbaSLf9C3d_9Nvgb5fSYhnVO1rc-W7-gKzmKZoWz33ezJuuvrsu5wEhtF2Lo0ZWUy7MJqkf4xZYhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم حضرت فاطمه معصومه(س) در شب شام غریبان
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/444802" target="_blank">📅 02:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444795">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTKlcoz_EBY6bVITBqm4OHSIOo32zaImm9fcggyI7TEN-YmSmDc5DMvIn3ugUDhX1IwXANcQOUOmt83f-DJP0-8VrCw20ipCBJMQnY0mJKs9IFP9D2OMUmELjpWGW-HX7NKHl-81TxO0cXmdo-xwA060gjm77G5U13Xmtp6pKOlCeUOyb16njb3GL85ffqA9yvvXAwMm1S-pdtiCobVWosspqq7P3o4zOojc0qcC4Xy6KyP0GvZ_JgnEGOgVKsxeFdIf-LLB-IzIfk9nHYgPzfwEPNt6-orXVg6tyPoYfGKExHAEmhiOj4SL6ITWjXMuuvyErybfjoozfK67XMNjAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKleHNJfG9kjwtZCOcHaYdljDPe863UEuuJYspg7aYuCjqRFvNgGF777YZ8O0oyraf6upLj8bC4YWVRULD3UcXUn6Tp2w8JmOSzxr32_4PJY4Py23YCGrlxlC0-YWjku-UNRd3jfWqZnIHb6wBALvasc6xVTDdhqicdBQKwwTz_FKiGkc6Sc_e6ntdqNlYMG-vy2TIeaV8YiY8MThQbXXa_WjKYBYVGqLW5cwXVYkw9R55Urxk6IeEhC6aHvxe7nRmSDiBNjRvHI3N-sigGIyZp8XLGcisBK1y3Jea5YG5YYhoJAf9z-hvthz59_Qia1b5YmF1qY3wMzjHcueDsYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uk37Q2O303IqMnQDpP4_cbaqOnhfQ6DhDnNMkqrrdt8cLXMQkdbqtN9GWQhhm8ipckxVDbomz020_fD9CrZir0IEAsomHUOsaK2JW97Ak3cplhIasKzOw34KQr0g1phtzSMd3uYcyLXFqONW0wzW-hh1HR39n1BbU2XWQiNvfvbRmSsFvZZSlBP8Anl2_7H1BFdcaV_7MFnbJzw8BemtuZZ9BjyCrjeiff8VcDJ9hrlz9QGHuE0mMzjgzFE9AGiJEsMZsF4V5FmPgtF1O5jDt3rawhhJPFCuWLisbM5VNgs8IOBGbAaUt4BOz0ASoELiAOoTq66Ccq1YnBo3DM0kfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KaZHbWSmpmXPf1idZahfbtfRodTGsx7nLPuDD7yJcy8B5NsTd8gyM67hpI68kKvdzWaDBk1crORYS9krVpmWUPt0ltqZMowVtPULA27BQrCONqRpskUiG-VDbMSqYzT3mI_dySGdBLC1eb9A_9-cxMHH7wUDdRM0_2rLRYwBjk1VngKzJ8mvzb01pvevyDB6UkU_crpbUQzIJjxDgVJVncaS12crC5KvRmJxvyAyQNf9lKJRKz5pZY7N7JYFGrKsyiLpjOylhBjkJ2qib7tlYRjY0DvmRdqVPoxNkN5eQwV-YELDFfdgjYfsxG7q62Xf4oQNFFD9_v6HD8g9VWUS7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEpJa7B7v3vXlzKRx05vekgrwvIGnLgf0s3Nhb_F4ZCzaZcEwsj4XM1jVBhrHXZz21ByE9gzS_a8Pq9URbJcMzQf9-t2Xpgfs58KdTzsh28x3o5Otdx0qJsk7Us1bSa_4zHCJpjnafLyhTzYWAOBQaVwSWW00z3vEdEGlDERbMTFEOScr4bRdVniarREuGr6bZeymfysex9_U1PISZ2zdpcpr7QAjZ5l3TjV1IU3ADIAkM7Z2Bm0qQWsB2HsY1n3FiemswB9NgIDqJKvtXIG2Gp-bP8ErOViebSFIupTUuPhACoLsr8P3Q8NR6gDH3UcLHjhUaGJQfo10w_Ki6dlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dB_xjEjzcpXrhh7XS1goWl9WUx8bNjAb8eoKcznJxx1hPaQh4dMxEC4UDGfegiGgMrhGvt8-fHPWj3krnPKUNYsusT1Q8d98-JzKp2jtb8q90tzsGSPVULYiVBHPidp8WehgwZJ3iNg3smNDgWzrh5qe-oqhEnztqTLBAK7e4ySVPrNnOnmfRBXT8LnrFpF0ph1zjG3rN64jDvqdi7jdNbKaUAfoe6eNBVimom-1_i6lYXi8r6uzjl23ZYe2J_cOJAnzIQrVVsny522ywv88WqkFsIFr0qD8Y7epk7rEuxiRW5OVf0W_IbDnsgL9RwCqVgqcDHHvPk43KZN8o1OCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4r1clTMz3s-aXn4QCqngrWIV9Cu6fiKP8Z79ZHNrKlMWo41e1-FiD5HbnR206l_qIPB3G0QTdYXJOzwHV3jFgKfWvz853Feq-uWC6OGfzF9asdwVKz2oc8ft-yRFLnVtxTIvLP9djLbxm6ehSC29ee2eqs2EMOQMne2hd5pjSiSBY3u_OQCKoHp2OXKITLub0p1veHykXjoKZ-bJtu4bO3hk_FVzD79XaRkOl0zBVIQlgoBbUdel_bcM6rQZwfvazLKnHILUMigwNTVo8sv0qulsmMW48xIVX6NjyUwLMWuy5AcKStK4ldCwyJ7UgQT22vQNQLGlGrn0PM334o-MQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
غروب عاشورا در دل صحرا
عکس:
هادی هیربدوش
@Farsimages</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/444795" target="_blank">📅 02:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444794">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aafd7947d.mp4?token=B68Wtq4aMl94ThbmMJy753Q1Ke9OBCxtKJIyTLR1SUm_xjHe7PhgzhoT6vBUnAnP7sxiVgfyjaI9G7hK4Yx1Xf0IQc-7UroYVh-bcSBVJNVEDyLLW5lLBAWWroQFMNlkfTYZBDbQtXiAo8NdrG28aEwcCIDyHt_MYCZHWLB3WCw56TcL9CSo-tEF6SOb9ev1BW-nGYjEnB-ziXDf5YwCiKieVRaaQUV9ngFoQP231Q-We5ARZnbJWs3hckNiepQlEY8pofRv7UFOtvlr5PgrmGuCF-C5eDWHC1XtTBaLmXkM1VU1nywHaUUwVY0yVdZL1XjT1w3PyTD3gWR-Vn9EMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aafd7947d.mp4?token=B68Wtq4aMl94ThbmMJy753Q1Ke9OBCxtKJIyTLR1SUm_xjHe7PhgzhoT6vBUnAnP7sxiVgfyjaI9G7hK4Yx1Xf0IQc-7UroYVh-bcSBVJNVEDyLLW5lLBAWWroQFMNlkfTYZBDbQtXiAo8NdrG28aEwcCIDyHt_MYCZHWLB3WCw56TcL9CSo-tEF6SOb9ev1BW-nGYjEnB-ziXDf5YwCiKieVRaaQUV9ngFoQP231Q-We5ARZnbJWs3hckNiepQlEY8pofRv7UFOtvlr5PgrmGuCF-C5eDWHC1XtTBaLmXkM1VU1nywHaUUwVY0yVdZL1XjT1w3PyTD3gWR-Vn9EMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب وداع در کربلا
🔹
هم‌زمان با شب عاشورا به وقت عراق، زائران به یاد آخرین لحظات کاروان امام حسین(ع) در کربلا شمع روشن کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/444794" target="_blank">📅 02:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444793">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902db0de46.mp4?token=h1VLjH_zQrqdPFn7bjwdfDOqx2TJEwoBrLJmdN9nZtIhM7wdOUbpLjj-Pav8G_dTQ4Vewa5ABiGlTfrwpBCyQ5_WajKjDvkGxd6E_PTKAjbjuW15aD_DZoWqeUXsLnFSa0EB8LfVkir6ugjLVjgbgrHFZoNfRNa5lqzg1Q65zwQOkVQUiEj5BAVBHiPwzpvUME2JYszdy1dL9_vI_-NwnNlHn9cPribGpbFUAypqYS7EzpQjtrSsC7Xs-QeHfmmWJ5kM6cGF4vyJ9cHPNu-WiiZsuD0pgZFks5Ow9SM-jciBVJOXY2gce6U7I053M5tt_ugEPlETw-oLxK6LjS-4NhlkUmgsNkuHR_lPQc1g8O1HDrw-VLo_f1ZVWxB4j8trQEM8qWsA2rukZiYVYbFynrBeX3xOoVyvGDk_zD2zM0LIpGG8n8aqzYlWE-ExccnlP1cVswLQ80auMAULmriqfpbCKS9Qm6qUIUlrw0jpD3xuCBF5dzxjGd9Fp3SfAQR-yhFYRhLA1kOC_HEl_Qgq1Iyw-TRF8zKbIH-dnII-6JkcEAw3mriNnC_JvhdQ-cCco5SyXcBHCMr1RnQV01Kqe73Y3ghNNmaFbIO8SKjnpbBHTOUOn_Ear_o7GQarv4qIExfPlvkdWLbDjxkVwuWgmpaXGrP3qJXdNG2mGH8S5_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902db0de46.mp4?token=h1VLjH_zQrqdPFn7bjwdfDOqx2TJEwoBrLJmdN9nZtIhM7wdOUbpLjj-Pav8G_dTQ4Vewa5ABiGlTfrwpBCyQ5_WajKjDvkGxd6E_PTKAjbjuW15aD_DZoWqeUXsLnFSa0EB8LfVkir6ugjLVjgbgrHFZoNfRNa5lqzg1Q65zwQOkVQUiEj5BAVBHiPwzpvUME2JYszdy1dL9_vI_-NwnNlHn9cPribGpbFUAypqYS7EzpQjtrSsC7Xs-QeHfmmWJ5kM6cGF4vyJ9cHPNu-WiiZsuD0pgZFks5Ow9SM-jciBVJOXY2gce6U7I053M5tt_ugEPlETw-oLxK6LjS-4NhlkUmgsNkuHR_lPQc1g8O1HDrw-VLo_f1ZVWxB4j8trQEM8qWsA2rukZiYVYbFynrBeX3xOoVyvGDk_zD2zM0LIpGG8n8aqzYlWE-ExccnlP1cVswLQ80auMAULmriqfpbCKS9Qm6qUIUlrw0jpD3xuCBF5dzxjGd9Fp3SfAQR-yhFYRhLA1kOC_HEl_Qgq1Iyw-TRF8zKbIH-dnII-6JkcEAw3mriNnC_JvhdQ-cCco5SyXcBHCMr1RnQV01Kqe73Y3ghNNmaFbIO8SKjnpbBHTOUOn_Ear_o7GQarv4qIExfPlvkdWLbDjxkVwuWgmpaXGrP3qJXdNG2mGH8S5_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرثیه نور در شام غریبان قوچان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/444793" target="_blank">📅 02:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444792">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3944ecfd4.mp4?token=QnciLyF6bBEAQwvcawnyrXPlKGEmzJJNUuHvfov6Fw4XgwYqy4-QkHBKEZVoO270yQAXhoWhPnxm3wjLwxGkrB-rL9KpzJeqf84T7RwXhu5l-pHOrcGhP_j6B-PANFLHG2WEh9vDx3fxXSYD6SWMIyPWqiPalTIv_trjOJ_cZpM_ZsQMXaVD4scBtiUGRr3FdE_SM4V9Ceq5po4DGSJM8q_tgfozFbKWlJx2iv_PE-jDjCMRmPawFgbimLcYCYXiJNN_znfawyZ5dBLvXsqzymn_ivxxIs5hzu0WSa6AmCyf3qxPeuTBf4AnwPv-GNHp6cSai0kLI6ZgMw6S6jmIkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3944ecfd4.mp4?token=QnciLyF6bBEAQwvcawnyrXPlKGEmzJJNUuHvfov6Fw4XgwYqy4-QkHBKEZVoO270yQAXhoWhPnxm3wjLwxGkrB-rL9KpzJeqf84T7RwXhu5l-pHOrcGhP_j6B-PANFLHG2WEh9vDx3fxXSYD6SWMIyPWqiPalTIv_trjOJ_cZpM_ZsQMXaVD4scBtiUGRr3FdE_SM4V9Ceq5po4DGSJM8q_tgfozFbKWlJx2iv_PE-jDjCMRmPawFgbimLcYCYXiJNN_znfawyZ5dBLvXsqzymn_ivxxIs5hzu0WSa6AmCyf3qxPeuTBf4AnwPv-GNHp6cSai0kLI6ZgMw6S6jmIkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد «لبیک یا حسین» شیعیان ترکیه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/444792" target="_blank">📅 02:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444791">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78fba2c1b3.mp4?token=SZRAZcXa0oMoQioYUW1zJJnzsywyYdLJTmIumQr8n8fIRgcvKMD3wbJOHDOfKvbnAXZrmxlHGi4T72C8JKKn23MPTI1uwZzj4hD7UDhEUbcnYNjALjEoUUwBW6PiRgOSchA1-KoP990SF3SE7jLO6h99oE3HfCg4yl_9SvUL_vRwF7RpSeunbUYZ8Qi0R2a2_0HH7CiLI3N2a9B8rQ8ChTvcDx106RYupY10dzz1DCPR3jsxg0ALi1t0uut7FtvgKJubdQdwJdbdmmIBQ1QNy5i42WAJ_yf6l8gdEHnrgt0CB12rwixvOs_Hr8kt6BeVQRASu5C6aH1h9pWCL6gpg0cwJxTvwSDhUNgaIOfgJq9z0D7c2bUdsjYtsKGNDoDryTvlzpj-gDZngqcWnh6jsvXZSV5c1_HIOqVGv9hxeq8rvVP0Sqp2Y3uzLp_w_vSI9A0lDPlrlGp1UUnKwHGia8XUR4xKw5iKYUgiKlzvO2wLnNO58zNuv-wgbnsCnfqP87XrZwoZ25aHxXCGBWLkNVY-YENedL4jtVafePzEVQf4MwVJfX03UVvy7H7d9wvmFUJx5p0luQF1Wf64FzO-J_XAVWqwdwiJFKzXrEolsiUJRhTx6gZxQuvoz0jnbBLEPUHsbUP66l7-umEYs_Q-GbUT9oCI_Pzxt5u-zWMBDiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78fba2c1b3.mp4?token=SZRAZcXa0oMoQioYUW1zJJnzsywyYdLJTmIumQr8n8fIRgcvKMD3wbJOHDOfKvbnAXZrmxlHGi4T72C8JKKn23MPTI1uwZzj4hD7UDhEUbcnYNjALjEoUUwBW6PiRgOSchA1-KoP990SF3SE7jLO6h99oE3HfCg4yl_9SvUL_vRwF7RpSeunbUYZ8Qi0R2a2_0HH7CiLI3N2a9B8rQ8ChTvcDx106RYupY10dzz1DCPR3jsxg0ALi1t0uut7FtvgKJubdQdwJdbdmmIBQ1QNy5i42WAJ_yf6l8gdEHnrgt0CB12rwixvOs_Hr8kt6BeVQRASu5C6aH1h9pWCL6gpg0cwJxTvwSDhUNgaIOfgJq9z0D7c2bUdsjYtsKGNDoDryTvlzpj-gDZngqcWnh6jsvXZSV5c1_HIOqVGv9hxeq8rvVP0Sqp2Y3uzLp_w_vSI9A0lDPlrlGp1UUnKwHGia8XUR4xKw5iKYUgiKlzvO2wLnNO58zNuv-wgbnsCnfqP87XrZwoZ25aHxXCGBWLkNVY-YENedL4jtVafePzEVQf4MwVJfX03UVvy7H7d9wvmFUJx5p0luQF1Wf64FzO-J_XAVWqwdwiJFKzXrEolsiUJRhTx6gZxQuvoz0jnbBLEPUHsbUP66l7-umEYs_Q-GbUT9oCI_Pzxt5u-zWMBDiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شام غریبان پردیسی‌‌ها در جوار شهدا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444791" target="_blank">📅 02:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444790">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0e474c49.mp4?token=v-G_Es-mD_oToIhNd7gn6FvuwKU5pnGz-hNfhP5eaL36cUL50W8rj8UDhHHrh_7p896sZ6ws_keGiQbITrTWFY33RNRMMicBODfc3UMGEHuy47BGeO8zTiV7ZWjzrPkPjHOB-dkAeCKl62guAGS29dEMCTtT6cCvsviKOBebqordUlCYSBwPTZ3z2dEs-b74ua5rMWY8UpzPjrtVYx1pa8u4cRvmvQAR7732YbjEHO10eb0yu5OVCqy4H2qWHYVCMTFiWuVUTNKf2b-pKrheoW5XLPmR8N3vKa-jKKQBuK-mLUpqUJoIgV8Ye1-bNwJS9JIDrBPbfnWScLPrE-C_ZDALwxpJktPw-PGTWvGwJFMU__F1IpIFchJ3sIxM6tSjuZXC5cuBE0gP3LLYkVF3aaVYcPd3i0TFIhxoVvWFWM1B5vIEKWei7eW22BUnp4yITEN1OdqOZGzJg7kOSecVDbMW2pZVYGSQY8Uv5jxl9RG8lQrrK21I9TQJwdnzNU4-a4m8QJt1gLU9pxF9RMNEPl1ufh1TUVfFvHQcyEtQraVZaIUEqupJILvt-NEAXUFkZQ-DBvOynoCWrtrnYfD_w3K675CAmdStiJupQe0QFNB0JS-g6HUEVqxDqvFVIhHyriUciIs6QgHVSumZPW3CcVFOsLlva6Vvq_S49NpDQvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0e474c49.mp4?token=v-G_Es-mD_oToIhNd7gn6FvuwKU5pnGz-hNfhP5eaL36cUL50W8rj8UDhHHrh_7p896sZ6ws_keGiQbITrTWFY33RNRMMicBODfc3UMGEHuy47BGeO8zTiV7ZWjzrPkPjHOB-dkAeCKl62guAGS29dEMCTtT6cCvsviKOBebqordUlCYSBwPTZ3z2dEs-b74ua5rMWY8UpzPjrtVYx1pa8u4cRvmvQAR7732YbjEHO10eb0yu5OVCqy4H2qWHYVCMTFiWuVUTNKf2b-pKrheoW5XLPmR8N3vKa-jKKQBuK-mLUpqUJoIgV8Ye1-bNwJS9JIDrBPbfnWScLPrE-C_ZDALwxpJktPw-PGTWvGwJFMU__F1IpIFchJ3sIxM6tSjuZXC5cuBE0gP3LLYkVF3aaVYcPd3i0TFIhxoVvWFWM1B5vIEKWei7eW22BUnp4yITEN1OdqOZGzJg7kOSecVDbMW2pZVYGSQY8Uv5jxl9RG8lQrrK21I9TQJwdnzNU4-a4m8QJt1gLU9pxF9RMNEPl1ufh1TUVfFvHQcyEtQraVZaIUEqupJILvt-NEAXUFkZQ-DBvOynoCWrtrnYfD_w3K675CAmdStiJupQe0QFNB0JS-g6HUEVqxDqvFVIhHyriUciIs6QgHVSumZPW3CcVFOsLlva6Vvq_S49NpDQvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای شام غریبان در قتلگاه میناب  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444790" target="_blank">📅 01:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444789">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03fd973e38.mp4?token=n76tLXzsvu_R2jH3v8FTuEsTZcKdN3spklwIYKOljmg2BU_Sc6juFjqnvh-olIioXqCI-Wg7FLl6YKLvs2908ogJf0b76cv6vDMsUcZq9AEfk6VPBHhxfoG54FrVVHWDB5r0DNF7KZXyrrhhwL3yCJyPxEmkvdx8EbwE37ggL9vZapQswrQuRXCSjEGxVQh2Q6kOkmx1Sj2gPaz1-yIEa9t5BXMy_N5gS6furQxpxNMUoHh6rFjECs4a17X8URurQtBdN3qb6WUulZNK4aw0NT0KLOWjCht9xKHkyeKx-MsA9gGTzD4QsP7GbiOPR4HlNEPMLejDJ5znZ1WDWnD8R1cwhF5K-pnmItkmyTEFBN-iI2ENIwQ0oi5xq0-260JDt_JSA3Ogfh2wHRvczRolov4bKOLrBGWRmIKPQdpHxyN9BIKUPwIgLdRQJrflTROXU2LEKnK1FCEplxnaAdndFjYlXTZVV5fJIAtvLGyuOikk3dRBQftmTsOpZF5KBOfav--GXUAMfI3Q5qd6hJ1iOWs4B5ODTSmIh-TASJ9_EtjPoNTcbsDIzSeJutdsYnzDeax5BvmxezuSSSzUvlzYKh4Blwaixa0bHlR1B5E7AtnRAX6MKv0P5NX3miwtK_3Hn54zc97u2vY1GtlGM-AHXX-28_8s39_KOeob9n2w6Ns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03fd973e38.mp4?token=n76tLXzsvu_R2jH3v8FTuEsTZcKdN3spklwIYKOljmg2BU_Sc6juFjqnvh-olIioXqCI-Wg7FLl6YKLvs2908ogJf0b76cv6vDMsUcZq9AEfk6VPBHhxfoG54FrVVHWDB5r0DNF7KZXyrrhhwL3yCJyPxEmkvdx8EbwE37ggL9vZapQswrQuRXCSjEGxVQh2Q6kOkmx1Sj2gPaz1-yIEa9t5BXMy_N5gS6furQxpxNMUoHh6rFjECs4a17X8URurQtBdN3qb6WUulZNK4aw0NT0KLOWjCht9xKHkyeKx-MsA9gGTzD4QsP7GbiOPR4HlNEPMLejDJ5znZ1WDWnD8R1cwhF5K-pnmItkmyTEFBN-iI2ENIwQ0oi5xq0-260JDt_JSA3Ogfh2wHRvczRolov4bKOLrBGWRmIKPQdpHxyN9BIKUPwIgLdRQJrflTROXU2LEKnK1FCEplxnaAdndFjYlXTZVV5fJIAtvLGyuOikk3dRBQftmTsOpZF5KBOfav--GXUAMfI3Q5qd6hJ1iOWs4B5ODTSmIh-TASJ9_EtjPoNTcbsDIzSeJutdsYnzDeax5BvmxezuSSSzUvlzYKh4Blwaixa0bHlR1B5E7AtnRAX6MKv0P5NX3miwtK_3Hn54zc97u2vY1GtlGM-AHXX-28_8s39_KOeob9n2w6Ns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گچساران یک‌صدا با زینب(س) در شام غریبان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444789" target="_blank">📅 01:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444788">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGPP1zmADkH4QStLipxH5hMmcYqL3SgGAT_VdickcfPFid5528jqQI8okmBpv161XcUkOMfuxidfg0BJTJW34oBhJJALAmcFBZQ8tBAhxrvWet1xtd-0TyrPgWoJuhwdL3Ltf637vvLLpL4_adyf4V7-HCTZNoM3Oa5jxN-uNIQililoQ8w07jxbUQugGxsfZRJXhfPxswX_xLX5DDwKNQOv57zFIqwnzNixnCG4Scy8m5n6-QC_67HcblbQCRtm8w5_KTpVpqSrkcJiHvHLKwbHwYJ3nRMryr5qyVYLcKTs1hOQYxpV2uKPgZB1kHSBRG2FmA2tRRNXNm1jEGrLyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکوادور غول‌کشی کرد و به‌عنوان تیم سوم صعود کرد
شکست ناباورانه شاگردان ناگلزمن مقابل اکوادور
آلمان ۱ - ۲ اکوادور
@Sportfars</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444788" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444787">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDONam7NfI_2Z8g7EgFioFs4Z4G10qgM2ESIQti6DjFip-tAsQLNlnD8ZV6c8XddbC2Z6VOYVaDLyouMR-aaJe1jG0T4T16AYmD8TTkrgTrXtRC0DTh7pCZqxiTOtfGzxkxYZJT6fYOBzYhNRi0rt1pIC04qTynDUA4EWqH9Ml3ZlGYW_PjsrU1nqhvDEg0g4WT8jjwGHEbSuRFoO6LckY0jxB_9EdNkMsDyM66G7SKEZfUT21znzYTnu5VSJxbA1NvU1Ppweb70Izo5JB9NGjFcYTCtfDy4Z3UK2Z-JS1u_BS5xiDTMeBKB2ZsL3ZPw9crz5tR48V2l8Z64yW2vcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساحل‌عاج مقابل تیم ضعیف گروه پیروز شد
⚽️
ساحل‌عاج ۲ - ۰ کوراسائو
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/444787" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444786">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b942a47af.mp4?token=TVwwm2i8ZfhwA0-7jCjjzvrGuXMFgc66i9qU7YjF4FnykDxt9eYJ_p09L-xWxrWfmInyq6jTIhRMU068mGQoNz6ofUPNX_UG40kYeaWjoCHZh0zPjTYbJ-jkz6n4hbRSE0Y6Y0Wr0Zt6XIGDSceDrpWI98xJcPbklGPgW4I9pr-7Vf1NpAoa_G_JLDQqtpJZ_AfwXlARwPKs-gXvxtPOKNWhuZM3wULoAuTBQ_nFeCNXNnB9mf_G9DhCS12Hkom3PXNpB_iv5SrKRLdyP_LgNt7jzXjUxT4f0meL5egP1JnJJI07wgwUJ_8SNa-7Gx4e_M6dPFK7YVvYnNHPUk7H_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b942a47af.mp4?token=TVwwm2i8ZfhwA0-7jCjjzvrGuXMFgc66i9qU7YjF4FnykDxt9eYJ_p09L-xWxrWfmInyq6jTIhRMU068mGQoNz6ofUPNX_UG40kYeaWjoCHZh0zPjTYbJ-jkz6n4hbRSE0Y6Y0Wr0Zt6XIGDSceDrpWI98xJcPbklGPgW4I9pr-7Vf1NpAoa_G_JLDQqtpJZ_AfwXlARwPKs-gXvxtPOKNWhuZM3wULoAuTBQ_nFeCNXNnB9mf_G9DhCS12Hkom3PXNpB_iv5SrKRLdyP_LgNt7jzXjUxT4f0meL5egP1JnJJI07wgwUJ_8SNa-7Gx4e_M6dPFK7YVvYnNHPUk7H_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شام غریبان حسینی در صحن و سرای حرم حضرت عبدالعظیم(ع)
@Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/444786" target="_blank">📅 01:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444785">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fde42a79.mp4?token=gbNexGx27vFppHWKglebIlR7uvuZ8p6qfB1BXJM4GAjsA0IkE_1V2noww8WS-IX3dk6Ghx2Hgqr4t-i4rk9fvUCys8DJIR_ssiyeS7AM0o-eHcA1e0Sf6zW28hVOYskNzjQvxk5MXnx-Mo8O2W-vmtYkDV2nionv8mFabGoN16f875plR6UtfZREERDtxnC8b_jRqtlyajLIIGc_IVHGlZ_wQAVaIHIOQ8FKa0Ok6uuFKAMgPndRo0qE55fN5JUZ7rWwc4QOFhgxrXMcKu5dRb27wOoY0wsY3fq1GMl8iR-Y4qVxfkF26f6b5B_SmkXZjyLo-IKLeNVjIFfRSpgiAFTFsUKDZLQOrO13MnmUtQtdO90-bLHsDRMSn4puq7w3jWn1Fd_iuFaX26CBMPL382M_iJavkEP_BxQXATNMyJqZgtQrkaphxzsNX-8kWJ2hWr7BLiZcOHe3nfKHk-xoxjMSjkuz3iiDuFUCxtMCcgYgyeHoEm03WHuoy--aZePeWMV7US8ps63BNOz2pRuWuLMXTiGt8XCGpdB3mJaPbt8cVUzaxb1qzAfTyJ6tj7TSSs64TnDdCZY7QNn4GGjcNpGNoZWbRswxCeRZ9OhKDeRiSMlOFxD9wLbADwf8e2xTIgro5Y-X-lTOGmNdResmbQRaajNaz6Iu4Uuw8CYb1gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fde42a79.mp4?token=gbNexGx27vFppHWKglebIlR7uvuZ8p6qfB1BXJM4GAjsA0IkE_1V2noww8WS-IX3dk6Ghx2Hgqr4t-i4rk9fvUCys8DJIR_ssiyeS7AM0o-eHcA1e0Sf6zW28hVOYskNzjQvxk5MXnx-Mo8O2W-vmtYkDV2nionv8mFabGoN16f875plR6UtfZREERDtxnC8b_jRqtlyajLIIGc_IVHGlZ_wQAVaIHIOQ8FKa0Ok6uuFKAMgPndRo0qE55fN5JUZ7rWwc4QOFhgxrXMcKu5dRb27wOoY0wsY3fq1GMl8iR-Y4qVxfkF26f6b5B_SmkXZjyLo-IKLeNVjIFfRSpgiAFTFsUKDZLQOrO13MnmUtQtdO90-bLHsDRMSn4puq7w3jWn1Fd_iuFaX26CBMPL382M_iJavkEP_BxQXATNMyJqZgtQrkaphxzsNX-8kWJ2hWr7BLiZcOHe3nfKHk-xoxjMSjkuz3iiDuFUCxtMCcgYgyeHoEm03WHuoy--aZePeWMV7US8ps63BNOz2pRuWuLMXTiGt8XCGpdB3mJaPbt8cVUzaxb1qzAfTyJ6tj7TSSs64TnDdCZY7QNn4GGjcNpGNoZWbRswxCeRZ9OhKDeRiSMlOFxD9wLbADwf8e2xTIgro5Y-X-lTOGmNdResmbQRaajNaz6Iu4Uuw8CYb1gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع بزرگ عاشورائیان بندر امام خمینی(ره)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/444785" target="_blank">📅 01:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444784">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c42d828f9.mp4?token=PG95Z0z-xuUGzjgwte5xfUUg1URF6V_ukb35BrByZHEoU4YctDI8QTTjG-JiHNRQ8aLVIOAJsOUXwvwhnkDgR4TFR0aKSm7eLE_xa2QhGYscXpacjPiS1qOQzQVGFtI3oTU6FTarY3AgR5shiIGFSqSL_PUtPMRXZ-k-g1g9PzcL4jsoB62BP_65aUmQyjqXNOaOKygfiWoaBWTmi95C8I-lrS6JPMDDYef5yVwOeKsXyCaVEHNgQ1uXHRx0aLpXzMTLzzBbC5oIVwiAi-AHmvEL1Da1sYAExjgldjruY5aPlQnpc_u2Bskp26w-4eh7R3RFzGQat_6a2lxMaOMScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c42d828f9.mp4?token=PG95Z0z-xuUGzjgwte5xfUUg1URF6V_ukb35BrByZHEoU4YctDI8QTTjG-JiHNRQ8aLVIOAJsOUXwvwhnkDgR4TFR0aKSm7eLE_xa2QhGYscXpacjPiS1qOQzQVGFtI3oTU6FTarY3AgR5shiIGFSqSL_PUtPMRXZ-k-g1g9PzcL4jsoB62BP_65aUmQyjqXNOaOKygfiWoaBWTmi95C8I-lrS6JPMDDYef5yVwOeKsXyCaVEHNgQ1uXHRx0aLpXzMTLzzBbC5oIVwiAi-AHmvEL1Da1sYAExjgldjruY5aPlQnpc_u2Bskp26w-4eh7R3RFzGQat_6a2lxMaOMScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش هوایی مشترک ترکیه، مصر و جمهوری آذربایجان
🔹
وزارت دفاع ترکیه از آغاز برگزاری رزمایش‌های هوایی مشترکی با مصر و جمهوری آذربایجان خبر داد، این نخستین بار است که چنین رزمایشی در آسمان ترکیه انجام می‌شود.
🔹
این رزمایش حلقه‌ای جدید از همکاری میان ترکیه و مصر به شمار می‌رود؛ دو کشوری که طی هفته جاری رزمایش‌های هوایی مشترکی را در مصر به پایان رساندند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/444784" target="_blank">📅 01:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444783">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb90483b0.mp4?token=APWoI0mPdtfzfWh-idL1PJ6X2ksIdHmMSsTBTxWVXYn3Kr6Iujqdb7LlbAOZaEvxWGhilM3Px_pOyzenpR30oai-VnuL-ZHFFmLBau02eomxGupWn4Z68PP8BJ_hb5wDXySV_Z4fnlMitFBil_8SivppuF3OVzsT7jjvip7Cf8Og3U1G1Tv9HWI8ekV1GBrzU2joALDCwc2q1maPSO4qW1KaWEaMPrinuxO82aHhfwQjBJm8Rx0V2Rf-imFxnx1PCbAW1Q0tvuRwkGBSZOcXz1TuhXHE9pM4IVKCmOZ-b_e3QnMH3s5nJMZWeHKsxjEkwKK6GChTjY25aS5FOgtJ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb90483b0.mp4?token=APWoI0mPdtfzfWh-idL1PJ6X2ksIdHmMSsTBTxWVXYn3Kr6Iujqdb7LlbAOZaEvxWGhilM3Px_pOyzenpR30oai-VnuL-ZHFFmLBau02eomxGupWn4Z68PP8BJ_hb5wDXySV_Z4fnlMitFBil_8SivppuF3OVzsT7jjvip7Cf8Og3U1G1Tv9HWI8ekV1GBrzU2joALDCwc2q1maPSO4qW1KaWEaMPrinuxO82aHhfwQjBJm8Rx0V2Rf-imFxnx1PCbAW1Q0tvuRwkGBSZOcXz1TuhXHE9pM4IVKCmOZ-b_e3QnMH3s5nJMZWeHKsxjEkwKK6GChTjY25aS5FOgtJ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میان‌داری مهران غفوریان در مراسم عزاداری امام حسین(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444783" target="_blank">📅 00:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444782">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎥
نخل‌برداری مردم تفت در قاب دوربین
🔹
هزاران عزادار در تفت یزد با به دوش‌کشیدن نخل، بار دیگر سنتی چندصدساله را زنده نگه داشتند؛ آیینی که یادآور تشییع پیکر مطهر سیدالشهدا(ع) است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444782" target="_blank">📅 00:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444781">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e7c8a296d.mp4?token=mjLISo-vY1GPSBObRL3o3jEsnS4VQBvQ7FVKfZbkaZkqOpKlGx2-f-fMkVlVnx_ZIorJwRlwRe37QGDxjNQRoM6bUdnStfmFwfyCSzG4P_FZGs0L09jh0qITm2KTCI3-ghNkuphsY4a04CY3pJq147qEyAdNs69uFPIb_6YG4c0MrNTxFopKlGETOPhb2Frxd8erLR8JYdZFCohDoOLoFQjfC_mEL_wQt-OGOb_a0owED27L-JmM513cz6pB0l4zqYJ_ta3VJHVShBJRH6J99zhuu_n2fnEDGkGBAR-Yo1rgxdAsIXAttg8czE25j59N1-elcxxCuOs8ldpL2zWQrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e7c8a296d.mp4?token=mjLISo-vY1GPSBObRL3o3jEsnS4VQBvQ7FVKfZbkaZkqOpKlGx2-f-fMkVlVnx_ZIorJwRlwRe37QGDxjNQRoM6bUdnStfmFwfyCSzG4P_FZGs0L09jh0qITm2KTCI3-ghNkuphsY4a04CY3pJq147qEyAdNs69uFPIb_6YG4c0MrNTxFopKlGETOPhb2Frxd8erLR8JYdZFCohDoOLoFQjfC_mEL_wQt-OGOb_a0owED27L-JmM513cz6pB0l4zqYJ_ta3VJHVShBJRH6J99zhuu_n2fnEDGkGBAR-Yo1rgxdAsIXAttg8czE25j59N1-elcxxCuOs8ldpL2zWQrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس‌جمهور در مراسم شام غریبان امام حسین(ع) در ارومیه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444781" target="_blank">📅 00:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444780">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1167de7231.mp4?token=kaKlUqaMq6D71jFQlaXUsJItlmcq9afqbU4W-45QJK6kaLB6NvCk270aXPV26bUStOgUcOeAuwD6pa6N-l2NXBxD32HWGCFobfVEsY8-RUcjWPSGVNJeu6S5AfgzdcXZJvdpxCuGRipDAsHkBMdg8BKtQ49bYwN1aiqEeCwQowx9qmgUo1yOL2ohL3RWsZ-IIqKv-hIWaYEBDuLtltA4LEdJ1EY6rxqbJEh-6W0r41RuKTUoVm4ofyMySPlEMM0HJyyennWIliFVvhiAqFDT3UnxaCaTw4jcBdPfk-FYTIrWM1lV0Es5_7m6BFOvQKgaSAcroQyd5UVKn_zC2EMfYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1167de7231.mp4?token=kaKlUqaMq6D71jFQlaXUsJItlmcq9afqbU4W-45QJK6kaLB6NvCk270aXPV26bUStOgUcOeAuwD6pa6N-l2NXBxD32HWGCFobfVEsY8-RUcjWPSGVNJeu6S5AfgzdcXZJvdpxCuGRipDAsHkBMdg8BKtQ49bYwN1aiqEeCwQowx9qmgUo1yOL2ohL3RWsZ-IIqKv-hIWaYEBDuLtltA4LEdJ1EY6rxqbJEh-6W0r41RuKTUoVm4ofyMySPlEMM0HJyyennWIliFVvhiAqFDT3UnxaCaTw4jcBdPfk-FYTIrWM1lV0Es5_7m6BFOvQKgaSAcroQyd5UVKn_zC2EMfYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای شام غریبان در قتلگاه میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444780" target="_blank">📅 00:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444779">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱۱</div>
</div>
<a href="https://t.me/farsna/444779" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱۰ – کتاب آه</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/444779" target="_blank">📅 00:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444778">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حزب‌الله: ارتش اسرائیل ۲ غیرنظامی لبنانی را در جنوب لبنان به شهادت رساند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/444778" target="_blank">📅 00:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444777">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f86a659f.mp4?token=HivBmWex_UdfYRyLS9e214TBJFEq-hwNe8cFFkzLaMZNAwauBRso2Y296wvT9vyxOHlbKM08VI8iXIPhpe3l3fyFhcqlskmtx1hB3MxhjiKb1a55NEaI69kSiOwguRtW7isIDXHduTiwvd_8OZTJEAFN-CSV-00OwAO1FhZBsLHHMYXMWJPUfZLb0TG_ymUQwG2kjUNpKYqVKgTqfrOUYTWinl5ybjhBr5S-65mgQcMT4FOlJ47FJKGMK_WxmCgm7IEL1tr0p4mdFbErNskX6EBKYYoe2QavT2yUIBfKrEqK5ctGI9YGgIX90OGDBwaJaHGDQnyKYs41c4jPTkYQGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f86a659f.mp4?token=HivBmWex_UdfYRyLS9e214TBJFEq-hwNe8cFFkzLaMZNAwauBRso2Y296wvT9vyxOHlbKM08VI8iXIPhpe3l3fyFhcqlskmtx1hB3MxhjiKb1a55NEaI69kSiOwguRtW7isIDXHduTiwvd_8OZTJEAFN-CSV-00OwAO1FhZBsLHHMYXMWJPUfZLb0TG_ymUQwG2kjUNpKYqVKgTqfrOUYTWinl5ybjhBr5S-65mgQcMT4FOlJ47FJKGMK_WxmCgm7IEL1tr0p4mdFbErNskX6EBKYYoe2QavT2yUIBfKrEqK5ctGI9YGgIX90OGDBwaJaHGDQnyKYs41c4jPTkYQGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهیدان حاضرند
حضور و غیاب شهدای ناو دنا و جماران در شب عاشورای حسینیه معلی شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444777" target="_blank">📅 00:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444776">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGcFL0d-GtSa6QVDvB4yaltWMuOEkqr-UTraGNLr1jjrsvO5Ga4vaFXuy930cdANZ4jc3_hd3Scdp36x8eIEJ5B-K3YMt1e-d1MCIe8LeNra704pgSAq7bkx6a6Iw14vvUx9FS9FIPA-aDqzDo4Ympo6vaQg4URyVkI3ZSzN5I_J6hYuvJow92deGXcArFwfsdnZdYUeoorE0psTyu7gy1DZ39kHf5Npc_ItB2mmsrQolMVht3PmWQ9qsUJ81qQU9u50ktd-vuMZMjN6fWy3ANMUB0Vroo91REkeZrEiN6n5kVJaNhRB_LBk0AnH8Dgl-QpS3PUbA1oREbYdg2zr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمان و همسایه‌آزاری
🔹
مردی از مسلمانان انصار به حضور رسول خدا(ص) آمد و از دست همسایه‌اش شکایت کرد و گفت: «ای رسول خدا، از آزار و اذیت‌های پی‌درپی همسایه‌ام به تنگ آمده‌ام و در خانه خودم آرامش ندارم.»
🔹
پیامبر(ص)، علی(ع)، سلمان، ابوذر و مقداد را فراخواندند و مأمور کردند که پیامی را به گوش همگان برسانند و با صدای رسا در مسجد بگویند: «هرکس همسایه‌اش از شرّ، آزار و بدی او در امان نباشد، ایمان ندارد.»
🔹
سپس رسول خدا(ص) فرمودند: «از هر طرف تا ۴۰ خانه، همسایه محسوب می‌شود.»
@Farsna
-
#حکایت</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444776" target="_blank">📅 00:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444775">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نجات ۱۱ کوهنورد در اشترانکوه لرستان
🔹
مدیرعامل هلال احمر لرستان: ۱۱ کوهنورد گرفتارشده در ارتفاعات اشترانکوه ازنا با تلاش امدادگران نجات پیدا کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444775" target="_blank">📅 23:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444774">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">حمله توپخانه‌ای اسرائیل به جنوب لبنان
🔹
شبکه المنار گزارش داد که توپخانه ارتش رژیم صهیونیستی مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/444774" target="_blank">📅 23:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444773">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRoFLlJx2gGtQaUo7QoMiST7rgyVxbLV1l9TBqgZiwG4W6rEdhzKQJaLLrvlUxutBXpvC3XpSjpxYGzKB_uMuC7nnyal0YgClDwTgHBRWgpaBcHXHXjJcTpCC9kE5Xm1lbMQ-9DWVBWjCaBtq_emDY3jIqx_lLxMZuuzu5GBIONG2a98z00gsHtAwsMsR7d-a7v668CRd2blPw9AWSw_H7at4KkDBgVpU_6mfXvgydoqes4Yk3pqH2WYi32oTklTevmmJNorFRdQCKjRg6cGXHNGUqUsw2PYUWh73T8j_Cj00TNWvcfuszRK9fqttuVJbbx0jn7HVQvJGYDxtM_Ipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر انرژی آمریکا: تحریم‌های نفتی علیه ایران بی‌تاثیر شده بودند
🔹
کریس رایت، وزیر انرژی آمریکا امروز در پاسخ به سوال خبرنگار آمریکایی مبنی‌بر دلیل برداشتن تحریم‌های نفتی علیه ایران، گفت تحریم‌های نفتی علیه ایران عملاً بی‌اثر شده بودند.
🔹
او بر همین اساس اشاره کرده که صدور مجوزهای عمومی برای صادرات نفت ایران امتیاز چندان بزرگی محسوب نمی‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/444773" target="_blank">📅 23:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444772">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_Qb85TfmEUQiLTVAhMoPG-zqT8zelE9MzVaYtc8vwT5Pvkv0jtZtuEdmpekDG5MXoWyjGyD3cCg4BeJCWNnW3XcwKz5GiomkZlaH6D_Iq1Z8YNXIkM2GJWhtCz48O5xRyV9ocwW-pxobxsb4bBQHgHjy-FZRqM0pV8oY0rDNr7YruC5sR_j2XinWdgyPzU4MqYN7Dnmih_cUvS2qLkn3MZAobDkpr9URNMHMivUx3X1F6tufP6czNwbMb3_xVr1x8S0mneb24Wp0WXIvlNFT19_JG2ABGaPx8yUMCXzT-x9KmurxxxLT6fPGZMAt2W53ylMG0sKENndn3G7_JM98A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مهدی طارمی: وقتی مردم زیر موشک بودند فوتبال دیگر هیچ اهمیتی برایم نداشت. ترجیح می‌دادم در زمان جنگ در ایران می‌بودم.  @Sportfars</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/444772" target="_blank">📅 23:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444771">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDdTuDnNxmdshGr4aP7pJGhFhgpbaZ6Z70fhU3vWLiKH7x7PXTezlY0zfmQr-qMyYu3xu99DXpLT1dl0sKrCSblzb6ftIigFBkLMMtg5CgvOhE36oTJOUR3ItUt2OgB4Eavc8gJ334qb6tGS0w6h7JKN1z5n0aJjK-MF1NP6IM4hrGyHicT8A4lAUbF4yt1yyjVuEUT54ytltl0s1oeEV6yTB-TsWaTLfVE9181PIsZVHd1OvQbFhednZcDEj71cN8JGZYiIsdlMZe4h3wBSv0Ag8BRhISiVX6tQQnXDtuqJZPfOcImzISMxSKh8bXptJBk-BjfDpZ4LaOVDbsNi3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«پادماده» رویای سفر میان‌ستاره‌ای را محقق می‌کند؟
🔹
استفاده از «پادماده» برای پیشرانش فضاپیماها بار دیگر مورد توجه قرار گرفته؛ موضوعی که از حمایت ایلان ماسک و جرد آیزاکمن، مدیر ناسا، نیز برخوردار شده است.
🔹
پادماده نسخه معکوس ماده معمولی است یعنی به‌جای پروتون، نوترون و الکترون، از پادپروتون، پادنوترون و پوزیترون تشکیل می‌شود.
🔹
هنگامی که ماده و پادماده با یکدیگر برخورد می‌کنند، هر ۲ نابود شده و مقدار عظیمی انرژی آزاد می‌کنند؛ انرژی‌ای که از نظر تئوری می‌تواند برای به حرکت درآوردن فضاپیماها مورد استفاده قرار گیرد.
🔹
بااین‌حال مانع اصلی در این مسیر عملیاتی‌کردن این فناوری است؛ کنترل انرژی عظیم تولید شده از واکنش ماده و پادماده همچنان یک چالش بزرگ علمی و مهندسی محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/444771" target="_blank">📅 23:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444770">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9j2BuJPupJrvitDU2irTk0jw8TNi2IgszR3N51XkBabo9nML48qtXf_il1epVEaKwDtW5bl6CoVesJjr0e0_FTg6MfZkQuR5q_sklJv3AOppp7CruuHakh6hjcvEirbu0J6L_At6K5w39hR0TEt4JHH-DUAy2beEjV2hzXf02bofUUDCK80Bx6Sb6fjy5_igrv477RaoPoEiugL7Q-53XqmPLS6cdI6yw0H2rfC3AsJZgRdK5qPBtPPYMithW-1lYX64oniTygsR9P4fomULo0k8pxLqJZ1JPYisogh-q39OXmmfe3uE7Zi7Xr9OXZajc-QvmRNgLYkDHMGtb-hCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
روضه‌خوانی مهدی سماواتی در مراسم شام غریبان حسینی(ع) در جوار محل شهادت رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/444770" target="_blank">📅 23:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444769">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5_GI2wAtJy69Fnyaz6ENL4PLS0hIEG7_w6YM6SdwqXt-tfBMQAAd6lNagzEteo4shBWrXBtBxHKzIgXMNw6Nk42aC_VPQin5xXPG7r5hVM2UF3JyAZgYzw0EH-8XIq8WRmUZSy0TvyEHwxKihfaruhL2NvnlM_f9LtSp_bA72fM23esICueKQxPq1c9Q-lRZ3fhblzDqDT1BQXvleJ4PrqnUDypSW-AqxLrB-HS0Ocf28ZiyvSVfSJUhjJ2Dwg44GMMrj89ThpF-kod2_IfdFmOroiGBpjGs6VZMnHmOLKbV95Z6npg0gJV74Q4R3T7RLC9DSwMHfC4ftqTuKHPLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بس در جنوب لبنان کماکان نقض می‌شود
🔹
ارتش رژیم صهیونیستی مدعی شد که ۵ نیروی حزب‌الله را در شهرک زوطر شرقی پس از نزدیک شدن آن‌ها به نظامیان اشغالگر هدف گرفته است.
🔹
ارتش اسرائیل همچنین عنوان کرد که نیروی هوایی این رژیم یک نیروی حزب‌الله در ارتفاعات علی الطاهر را مورد هدف قرار داده است.
🔹
شبکه المنار هم گزارش داده که نظامیان صهیونیست با سلاح‌های خودکار به سمت شهرک بیوت السیاد در جنوب لبنان تیراندازی کرده‌اند.
🔸
این درحالی است که طبق بند نخست تفاهمنامه آتش‌بس میان آمریکا و ایران، جنگ باید فورا در همه جبهه‌ها از جمله لبنان متوقف شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444769" target="_blank">📅 23:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444768">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ddbb7c13.mp4?token=o9L_JXeolcFf44vMi_gmjEDQyc6T0cAs5g0U2eE_RTQgBwA_dWo-CR5nh9uBvooA8QyVtZxTn5bEOfYfDdSlGn8A1ITbugCM9K4h7W1Afv0W_7etnAPgjvSGQdsXmXwE-yPL9WN4pvrJdWzsHExrsTiW2UlLbQ4ITrqvJEoaqSKFVXajdZ8NuxOAlAVIvbIbQs4J-dT9gC_5uyvqRV-8GMxf4bo7AuLq-1On432Cg79WJLIrVci7ql2w13gW2W0Qt0FzFq3QhIdPmDYrcB6cMBbToWrc3Dr1LZmWFtlevnvXzVCvBJyoZJuLrWGcZk4gvfmZW0LJhusTqiGZ3nvHDcAkG88JFShOYaGSDdKFKflzF4OT1Zd6TD0DUj5PIwzFpP-qexPISnegewl6AmQy8MCQs5tDrtXXlOt00nhZwory5ga-FBsham8AFg72itYkMHlZQu5iq62zIJjOCRrgqndWP6rKLKCS_dnRc70VvyB8NeO-EJHIWF7Ygcx8lpQoe7D-NQp9oJhTpc2lM6QCA8p1lm8etjZBmFh_GA4W5Md9xdQ5QdH5ko8naSBV1qNiZEZo0KWHwJTZ-N_CLWMxrvJlu3eXjSddWvksN3kHiVQYbwmkGfbojH8OgL1P_8-GXvMUW_SU8e0rUVaE2pfOffJOfsGrF7mwGxsQOWAC2Y0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ddbb7c13.mp4?token=o9L_JXeolcFf44vMi_gmjEDQyc6T0cAs5g0U2eE_RTQgBwA_dWo-CR5nh9uBvooA8QyVtZxTn5bEOfYfDdSlGn8A1ITbugCM9K4h7W1Afv0W_7etnAPgjvSGQdsXmXwE-yPL9WN4pvrJdWzsHExrsTiW2UlLbQ4ITrqvJEoaqSKFVXajdZ8NuxOAlAVIvbIbQs4J-dT9gC_5uyvqRV-8GMxf4bo7AuLq-1On432Cg79WJLIrVci7ql2w13gW2W0Qt0FzFq3QhIdPmDYrcB6cMBbToWrc3Dr1LZmWFtlevnvXzVCvBJyoZJuLrWGcZk4gvfmZW0LJhusTqiGZ3nvHDcAkG88JFShOYaGSDdKFKflzF4OT1Zd6TD0DUj5PIwzFpP-qexPISnegewl6AmQy8MCQs5tDrtXXlOt00nhZwory5ga-FBsham8AFg72itYkMHlZQu5iq62zIJjOCRrgqndWP6rKLKCS_dnRc70VvyB8NeO-EJHIWF7Ygcx8lpQoe7D-NQp9oJhTpc2lM6QCA8p1lm8etjZBmFh_GA4W5Md9xdQ5QdH5ko8naSBV1qNiZEZo0KWHwJTZ-N_CLWMxrvJlu3eXjSddWvksN3kHiVQYbwmkGfbojH8OgL1P_8-GXvMUW_SU8e0rUVaE2pfOffJOfsGrF7mwGxsQOWAC2Y0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شام غریبان حسینی در میدان فاطمیه کرج
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444768" target="_blank">📅 22:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444767">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4a0c646f.mp4?token=jQUIhhUP1VxTrdWGGBbkZtoLU8V0smQPYZ6X9BSsotKxo0yL7yxKpnPb2zhPpSOOKpq8_mBXLa6S4nnAuZwIAt2IxD5AZIEiutwdJ275TImeaNLlId7vALTbhPBjGjM86Pnb2c8F9f8aKJ_E0_D7Psgf9-pVNJjBl7DOafHaReNiQTgo5DNF5gHSY8pEJ95hYwjF0eyEN617ZpoKO3s0f8ThSqj2XgwWOT2ktjf7J17Zs8zYDpMGmrMl92m25nDe8ai-0U0jazDnAPNhCXtEa8xQ57BY1ZZhm8OHtoXGHdxHlGutRNc3Bfu-v_v_5s2u_23NV-0TrL6TmJP-RiGAwZLzZuAMVmq_oIn2RSko4aYkHCjut0lVOyL_TUYOixUou9tw7OVy0cRoTHJoNqDw3BtUG3Qe9Imtahq_OplJydAyaRJFQ-JF_REFnvkF6JgT-cE4kDJ5VFYrJSvNpxwUCIf0FvWoTt8jQ_--4FdXcWK5JG-pyWpGrBliwm_6ocblR1o3MT3x-7qFxR6eKpERQIWx6ZewmGcOss9Be4hnhQ4F4NBb3Nbza2hHa2qu8opKLWdNzZ8vsqXuBukzvfz11nthe1jkbg7OoYFMWZgwvC1NqB1s2fbxeAmNZCA_3_keFQiGHt8i1IyzBq8yB6UjFmksdPe7oLpmdx1CsCkUKp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4a0c646f.mp4?token=jQUIhhUP1VxTrdWGGBbkZtoLU8V0smQPYZ6X9BSsotKxo0yL7yxKpnPb2zhPpSOOKpq8_mBXLa6S4nnAuZwIAt2IxD5AZIEiutwdJ275TImeaNLlId7vALTbhPBjGjM86Pnb2c8F9f8aKJ_E0_D7Psgf9-pVNJjBl7DOafHaReNiQTgo5DNF5gHSY8pEJ95hYwjF0eyEN617ZpoKO3s0f8ThSqj2XgwWOT2ktjf7J17Zs8zYDpMGmrMl92m25nDe8ai-0U0jazDnAPNhCXtEa8xQ57BY1ZZhm8OHtoXGHdxHlGutRNc3Bfu-v_v_5s2u_23NV-0TrL6TmJP-RiGAwZLzZuAMVmq_oIn2RSko4aYkHCjut0lVOyL_TUYOixUou9tw7OVy0cRoTHJoNqDw3BtUG3Qe9Imtahq_OplJydAyaRJFQ-JF_REFnvkF6JgT-cE4kDJ5VFYrJSvNpxwUCIf0FvWoTt8jQ_--4FdXcWK5JG-pyWpGrBliwm_6ocblR1o3MT3x-7qFxR6eKpERQIWx6ZewmGcOss9Be4hnhQ4F4NBb3Nbza2hHa2qu8opKLWdNzZ8vsqXuBukzvfz11nthe1jkbg7OoYFMWZgwvC1NqB1s2fbxeAmNZCA_3_keFQiGHt8i1IyzBq8yB6UjFmksdPe7oLpmdx1CsCkUKp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاکر کارلسون: مردم دقیقاً برای جلوگیری از جنگ با ایران به ترامپ رأی دادند
🔹
تاکر کارلسون، مجری سابق فاکس‌نیوز و از چهره‌های تأثیرگذار جریان راست آمریکا، در مصاحبه با شبکه اسکای‌نیوز با انتقاد شدید از سیاست‌های دونالد ترامپ در قبال ایران گفت که مردم آمریکا دقیقاً به این دلیل به ترامپ رأی دادند که از جنگ با ایران جلوگیری کند، اما در نهایت دقیقاً همان جنگی را گرفتند که وعده داده بود هرگز رخ نخواهد داد.
🔹
کارلسون که چندی پیش از حزب جمهوری‌خواه به دلیل حمایت بی‌چون و چرای این حزب از اسرائیل خارج شده بود، در این مصاحبه تأکید کرد که وعده‌های انتخاباتی ترامپ درباره پایان دادن به جنگ‌های بی‌پایان خاورمیانه، نقض شده است.
🔹
او که پیشتر از طرفداران سرسخت ترامپ بود یادآوری کرد که ترامپ در زمان تبلیغات انتخاباتی گفته بود که رأی به بایدن یا کامالا هریس به معنای رأی به جنگ در خاورمیانه و جنگ‌های بی‌پایان است.
🔹
کارلسون در ادامه با اشاره به جنگ ۳.۵ ماهه آمریکا با ایران و هزینه‌های گزاف آن، آن را یک «
شکست تمام‌عیار
» برای سیاست خارجی ترامپ توصیف کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/444767" target="_blank">📅 22:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444760">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l36Np8Q_dJb-zTEH5NLt5vm-CdQQflla1rmH7FoGEWul9fnE3JA80z_bgbpCqJRAJFlphmQXCKBnOT46ezKGVH-Z-iBSToX26k_VJw9iNPvnCuHuMhzayzmYL57zFtcHOOhjaoqYuIrEVvAtvk6dEX7NK2L52YWQaGfu2NNDYf7XuVXhtm5o-Bf7QgDkzkz7IW41I1x0oM1P2C3faHTMXVkEpXXs4nyhprNi9b3gS-cIAgL1VsolG8CqmJl1A4cdXnxPjQFsWSGzPyZV1cIkHLDAoDkaYSmLs5hIgTG08C5ShK8XIxnjzoMnmc0H-aqx3YSwVUBH2GrC8oI_UxFSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9yfw2fCjz4WU6f8wdy9oUEL83lYADeleHxtYDBXRu2dCoj4SsO_c0eCHTGYbx7Dudb7DRElSSuKnnKf1PBiDGjedTAViGqH3XNRwHrhbiU69pkF5ruGOGtOvjs3GVUI9yWI1wFS2j-dO6-z2XIWfACfZfTgYaUAlX9SIx35h8nMRmDi-nJerxPQraUt-x67fCPWnLu_xZA0NbJRILbCeWNYvBHTMS8Ru5Qhg9sMm9hQm3VfilrP2hYGielCcsWptNG45Bx7YyzOeN-MB_AORv40RvWOqDrkLYCMCaKzOmxfe4ehBjR0x2EZJNYCe7Bwb0uHdATx3pvYHOHQ119DVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVhaKwY9X0po0aBAewyUjeeW1uu3xauGrjMeTVEjBIwclea7XrcuHhQGihUo2zfIuk2b28N1rPKXU8WnQPVEquTGahfY5xg2f8VobS4FQ7MdJ38tEVvTGx8M6mqqMuMyuFCvCUQNRz5RLR7HfbY9z5n5YuPWCH5qfHuqKN3ugUGPXWBqXy2qXHS5q0LxpcczAtxiO1ymzDLlieFQWJojLVsjAdiRr_8xBkgzNY1fzX7M5JplYYCZOVSYiWj9u4LvNNovbBQf4ivackLjS2AW2-rIOXrN0bTvyoRbbIUidFg-Gh5Uu0KY2JeAbNag2pnsjOkYeUGQG3ICT0MQb44FZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HefgriA81jVf8DdE_iD57ZJxt0jZuE27Pmm1aJ0o0qvbd1h3cYZqGIZnAz3TM5Jw6vzyyuWfTmzAq0PvuXft4ddTB1jsh-ufQ7Za-MQLVd14nwVzV1pd35Vsc1dacT98GGayT2q9vAzPU3fNQ6HdG32QIZtQ14XRsesSzKVLPfaMfrdSdWU5qsaqB9B13DhULhVPeySKAcatEVwVOO-67lbyqoFtXY11sVn41JBs5xX1BpQaul4rXSR_aO-vdcBi2ObDg5p_Owyif9tljl2XEeJhgXrxLnnE3zgRPbP_BkOgsQZpODj1qyJVifM35nOAn5MgNEmb7hJSsZwJyQJZAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYhKazF-H6BvbUw9MuGtcybENF3okxnGo4NxKc0Po2biQvtmcDvK_pma_caL4wgCpOIH6kiaEjEiGprnJb2kXY-gMh40bmUfFUmbzxdUiXBign1mL_SiuZa5pQ8UdukgJ-Hv6yMYIjNxPmnRlvLLH_Gdf18RIEk8AhxcgzDPJGGTEMd6XANtLw6B-vg5VzDenrGuYg-Rrjp__z74ugQQg51eX1Z1bBPBNUNFrTHQMvdX2ysRCN8CpHA164XmPidsOH3DtDaa1DSIz1957rCRP2Zetr00p1VqaBwpriRk4OznMwBYKTXK1DY2aTsGYfZ4neCR-CeYTBC8tkjFbcK_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idRoyhdRIzdRLTA5TteY8wXU0_FBmhI8hkBukOvXYUQXpP3vhL8UskNON1T58KSmHD-UDkmVYknvy2ai2hYW8MIn-bVtCuC_NiBiC0vYg8_O6KmnkOwxinhzqNb3d8laJnfAMW8YpLip8PO-UfBwJkYiMljol8abauNdaC1LxKM_EXh6xpj3LHOVq5h8tzaGCqpV1FioZiAruQiq4LO2qG-ffMG2n0eUz6LdmX8VWt2u0hMB8KLmJ_4y7FinQnxAJW8vChDyx7bPH8u2b7DGWGuT4svrNjqxt_cNXeOg5BRkorod-YMHfYyRIx8TDZch_2HKzVi6AK5645kFJ3ZsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUb0OPktQyXiYWSdAq5l62tC2EFCiNgdMMEn1-pTJ89-tqztN3Lg05KZ1aN-mxUOPrc6cZgP-WTnx0s9cSA7dNBWozraWHlc4nwnDfQxIYEE7o2cmmlGWe2i4ZT-hdCfZWL1_CJ75bMvoQ_WQt_Z_RxF6_MnP5q2xfePEDPT-Jjg9kV9qP_3WXTXfFwWBRtTx5H1O6P4KvFEEtBmC6pZYVptBRB8vGyvPeyNJ1azGhF5rMHrrjh3KIiStuJCM6Gxg79ghoeY85PyksrrRcT2cY33fDf_TeRtUYUF6gKFkzDQO8sP04e02WoPE2Fp36CFKBg0GRBr8XoecjVfitpYqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خروش عاشورایی اصفهانی‌ها
عکس:
حمیدرضا نیکومرام
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444760" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444759">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1ZBIQLMsuqWwBa185CAxMCBMhSuWwudg2QRcresBYfH9UjZFsIR6nN-bSldAGxKB2a4omXLKeJqk7l-Ru2WOtzYRlaz4eInZk9Ql1bIsIlwkUL6flATl-tpyLzrrMK-aIYAUcc2sMsLtca8g89Yn1VzUMjb025jqS50lz5p8JQ72zjfLRmQjBgR2MaL1uxvc5IQl2kC7T7kfEHgSvfWhTZsiMTCSir3_N836uZoNtmY2z3E7nBP4zmQecDzyZL5gGNJgQBO4aqWCFg9Fah5U6EGe3-UaRSw3dnc1veg23QOkvANlBXlH8kIQvDvMmMk05Ffakv-k-U7lUiriUCAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نهاد مدیریت تنگه هرمز: تبعات عبور از مسیرهای غیرمجاز با خودتان است
🔹
نهاد مدیریت آب‌راه خلیج فارس(PGSA) در پاسخ به استعلام‌های مکرر اعلام کرد: هرگونه تردد از مسیرهای خارج از چارچوب تعیین‌شده PGSA، مشمول تضمین عبور ایمن نبوده و از پوشش بیمه و مسئولیت‌های مرتبط برخوردار نخواهد بود.
🔹
تبعات ناشی از تردد از مسیرهای غیرمجاز، برعهده مالک، بهره‌بردار و فرمانده شناور خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444759" target="_blank">📅 22:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444758">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6b44073e.mp4?token=hLAdO_O6-ycKRWM0OCeitn0Lfxz8M_6Y1V0d_kSZtaSXefJRfEbCOPAWywdfWBXhyxa2GU-U3Hr_djbKdz6kV7bWeRHV6EOcLItymz63fndDzmVFsabmm2AYthWaLTE1c_Wo-R7OfD_Vgyh2vRW_w_qqBoOQLcIRj9z1AL6qzdcsf-nHYompcnNDob_McpJO6T4YIE8oFSevlhJzU-2BE9y-AIMX0aQr3PEne_OJeOKijgAg7dvbQgiuZOEVXYpfXqs19QmbnjO0NCf_uUSZ6vLtxPHsJAOD4Qu6UpKYv2SH-tUavvj5s3_dU5KBPSpejgpZyDIaK7GSn8nTkf6n6b9QyLSY9B7HjJPhsDrryQs-k1wRbNGN6fbl8A5LYMBRJauUPcISFSV09TOJ4wBhe75HS7qYT9gf9Ft6zcGaHgdSfdJi9Id8Q50dYNI58XD-H2u_-8Dbk0dvREBRCPAie7xA5goOScevg1on7eHdOZpcJo3NtGi8QUUbVdGYwvvov1r2DfGgzqmn-pfCD_3ft9uj7PhGQcvA7d2GE3VDcDzdBbmwJe9I2j3OYD6uEpIRi3gcyniP337eBqthVbz3W6T_T20_OXJ3zyZw64mE-Vx0lJOLc79dwltLVyL6N5I6SnJ7Ub34nbqScZug-vaz_IfEN3U05_RBQApc_gTGYNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6b44073e.mp4?token=hLAdO_O6-ycKRWM0OCeitn0Lfxz8M_6Y1V0d_kSZtaSXefJRfEbCOPAWywdfWBXhyxa2GU-U3Hr_djbKdz6kV7bWeRHV6EOcLItymz63fndDzmVFsabmm2AYthWaLTE1c_Wo-R7OfD_Vgyh2vRW_w_qqBoOQLcIRj9z1AL6qzdcsf-nHYompcnNDob_McpJO6T4YIE8oFSevlhJzU-2BE9y-AIMX0aQr3PEne_OJeOKijgAg7dvbQgiuZOEVXYpfXqs19QmbnjO0NCf_uUSZ6vLtxPHsJAOD4Qu6UpKYv2SH-tUavvj5s3_dU5KBPSpejgpZyDIaK7GSn8nTkf6n6b9QyLSY9B7HjJPhsDrryQs-k1wRbNGN6fbl8A5LYMBRJauUPcISFSV09TOJ4wBhe75HS7qYT9gf9Ft6zcGaHgdSfdJi9Id8Q50dYNI58XD-H2u_-8Dbk0dvREBRCPAie7xA5goOScevg1on7eHdOZpcJo3NtGi8QUUbVdGYwvvov1r2DfGgzqmn-pfCD_3ft9uj7PhGQcvA7d2GE3VDcDzdBbmwJe9I2j3OYD6uEpIRi3gcyniP337eBqthVbz3W6T_T20_OXJ3zyZw64mE-Vx0lJOLc79dwltLVyL6N5I6SnJ7Ub34nbqScZug-vaz_IfEN3U05_RBQApc_gTGYNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با تبسم گفت ای ایران بخوان...  @Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/444758" target="_blank">📅 22:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444757">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
من راننده تریلی هستم ماشین‌های وارداتی که دولت دست مردم داده گازوئیل یورو می‌خواد. قبل عید به خاطر کیفیت پایین گازوئیل‌ها ۲۰۰ میلیون خرج سوزنای پمپ گازوئیل کردم الان مخصوصا استان سمنان اصلا گازوئیل یورو پیدا نمی‌شه لطفا پیگیری کنید.
🔹
الان ۲ روزه خط‌های موبایل و اینترنت روستای دهشیخ استان کهگیلویه و بویراحمد بخش پاتاوه شهرستان‌ دنا کامل قطع شده و داخل این هفته ۳ بار این اتفاق افتاده و به هر مسئولی زنگ می‌زنیم امروز و فردا می‌کنه من به شخصه از شما تقاضا دارم این موضوع را پیگیری کنید.
🔸
وزیر می‌گوید قیمت مرغ طوری شده که مرغداران ضرر می‌کنند. گناه مردم چیست؟ چرا برای جلوگیری از ضرر مرغداران، به مردم باید فشار بیاید؟ اگر می‌خواهید مرغدار ضرر نکند و مردم هم بخرند، واسطه‌ها و دلال‌ها را حذف کنید.
🔹
۲ ساله می‌خوام ماشین بخرم، ماشینی که می‌خواستم بخرم از ۱۵۰ میلیون شده الان ۸۰۰ میلیون تکلیف ما جوانان چیه؟
🔸
مسکن ملی برای جوانان بندرعباس مانند یک رویا شده، من از سال ٩٨ ثبت‌نام کرده‌ام نه‌تنها هنوز خانه خود را تحویل نگرفتم بلکه با پیشرفت ٨۰ درصدی هنوز هم پیامک واریزی برایم می‌آید.
🔹
اگر ممکنه یه گزارش کار کنید در مورد نقش مافیای پمپ آب در کاهش فشار بیش از حد معقول آب که عملا مردم رو مجبور به خرید پمپ کردن.
🔸
اختلال بانک ملی هنوز درست نشده کسی که مثل من بچه مریض داره برای خرید دارو باید چیکار کنم پول تو حسابمه ولی نمی‌تونم انتقال بدم.
🔹
خواهشمندم موضوع برگزاری حضوری امتحانات تحصیلات تکمیلی دانشگاه آزاد را پیگیری و منعکس کنید.
🔸
برای دریافت اعتبار از پلتفرم ازکی‌وام استفاده کردیم گفت اول باید ۱۰ میلیون تومن به کیف پول واریز کنین بعد مراحل طی شه. درنهایت با درخواست موافقت نکردن. حالا حدود یک ماهه از کیف پول برداشت زدیم میگن به علت شرایط زیرساخت‌ها به مشکل خورده!
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/444757" target="_blank">📅 22:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444750">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5SuJMN3UPuWH_dzNq8kUSJ2vvDijdzJHrbxsxCQBFYm2SlhzEixySTz07sxsuUeEQwW6CiumkmE6JjSbxq0K7TfigfSoYGJ-Da6VcTPr3K0fSikfBCcSIkFmzM7gHx3IWPZBuUfrjVtw85q2OkCkUlaIuhLpzKhJiqnIHhPpkAJnpsDfD3TvIGHFrsTOtj8hdB2HW3k2i0iKhL910jbR09Yuco4r9fLfaYiT5CZMHA-3HC5JvRNocKSiUSdvB_-3_tcEPv5JwvDVE8UX7hAzUschqZkwMJ9AEAdyVQGCV-OeD0grReYrn_rgfq8P3jUdCjjVJZwLShZiYqQ2-ciqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFkmEuyBcx2tpro49j7K0g6BtJOHLqkb3GsVT02fuSbbeKja2QspTLK_tl_20ZK45kpn1ICbagEeYrDz2f3CoAFkqtQUS6TxYwpGKcQnb6uyOKwlH0hkxgu2di4_U4lSMkWfj3KozpVgLu3MO7q-5uRDa2xLKakr3MSSDyGFapimVNVA1iH4v180M0qDjVVzmOB4XZ-ZagQRqiLTZkB9d5nLYi_LrC24ojQfjLt9TAxuCw7V6hX_QiIOcG4K1XHPd_q1T-7ASS00zjGjaf0co6FZEZzzt1kEMhBCPDH0wRB98mx5oX1eOqbB3tiW1rD2p4M-991dyj6ntQPQI_8ZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkWrzHpxHPYgfvZU01i6Bry351KgII-sVa9BJRIo9kyvSTJmuehaPq33c7sibkNFB8OaRd2VTP2ikhd9osHDAQYfti_oJ0frNtLgsrk-gkwGmlXS_jPQRgqkri_H5MVDQIk3oTn8opCqDk-vW5tzC3LeQ8ocfWXnwtgaj7EpSQ-u8oIX2qgpZZVCW_giQtefeGJDeEBII-k7zELZ2PYAereEARE9toCtiu22R1MBT1P344Vm5a_tllcnrRauTUh9FOGFNs-kV5qwmA3_TW2QaLZtNevVWs59VV4vpG3xJgrRqqx9Zi1h58bYvizrFgZ2TO801189ZEodOxu0LGNUzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GC-J98MpvQLtj-lJiJ1KoYW6usxCAouulQ_KZS6m8VsBavWAuMAyRI1SCO-Ve3p_KhHMS9M3RV9vhUfR5ELjP4hiN1dSq3ZUT91BJ_rpeoesrRZPc9u5mDDFNNIWaNWMXdNK3T1GdCge7tfXn0vNqNhPpUkkLN84pTQqMCbYjGD2829X6ZS_8ktius_ruquZagaB64X3VGV_eQa4JBqqi4BWhWWYR4DbFwRh4f7ioMWbEtHQXtUFrDtQobwN1jGCbsTWdU5m2udpxRJC7-QgXT9TC2ErPql8NhlwC4_bLBAJclJFUt_qHghsn6dsPSG6Hfgnhbfxrna5QdwswVG_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5PfeKozuz7HLyW2hDuHYsWnMcEAxTR3hF7MPGRKUREFCfZrqDFknwe1xzYfSFaxR6GuR1zFF0JpP_8zkousl2o60OY0CJP6CaZsXpTtV7Orleu4wYBHFkF-LiHMH67HzRatQJkjDYsEZRRsN5I0Fh5jJi7p0eIoEgzNi-15-EneRlTuLPIRNx0sYErsAgDvRH4DQgVGbCNrE59YXy8AIVyhofwgigGg2bHoku_94lGgC7VlyrVeac_NjkmuD9QFklDQEIesbr7PsKtUNIXltCJNybo9zGxnMQVS4OPrmdYD0ycre_tKHa8W6gnVeOWhyQLAyyk-n6bks2cLsP0DMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nADQbUvGm5y3OH3BbseC4vv5DerRsCXBMbsrYF4ZJuxKMbMiiGDFKMxCmbktdYB4PKCEOPFHxE6xZmbvkMpBK_6xqQYgv4EeCabeGH6B02VknqtqDgrnIWtw4mHUj06BcWZjQV00ju6zQcc1cqCiuJ3moAqhY1qxc4MU8ej9jwl567p7TruT_qfj5o5K8fhWlJ_2Ot0V6CO--sSZuUh_sGkLsQJE4Wh02qXif5qc_Hxo5QZsSvDU_EPslVUESZTBj-zkaQAlyayTomFmXkwJYcJP6Zi3-Jtg6Q6Mkqmyx4PMD1C_B6BPNQkHc_QeUfLLlUvRAXX_YRnK2QcI_mCnEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUa2N4gLpkOW8tcVdCQS29XtFwUjRg1rVAiA99iIcrxoNzcA5WeGVVeydIyacZqmj-gH-VeOy4J3nrywI58UGeR-41IY-7wosg_kx_-NKuNAMfte41bYIIdIcuMb1zy9iHokzfnvftbDPUNzuFHlmK6-litWnqMBG5yGR1T9ctSRvlXBHMFApkfFmjclHWh8DYkgo5E_xDQ8MkJ2W7c45zZxiuCtnopsQYaLnn7fn5udmjtmHsqSojBTM2B0eS9HudURScHy5VzoaKbKuxw9SJkBfLMQEMJavh4CiVNhwoPoXUnpP7gGd_nU19rGmmwlDnrxwoRjLADbFl9VHhDxDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری پرشور زنجانی‌ها در روز عاشورا
عکس:
عرفان تقی‌بیگ‌لو
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/444750" target="_blank">📅 21:46 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
