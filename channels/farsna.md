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
<img src="https://cdn4.telesco.pe/file/bsefD64zyA_telpyIfSw1n9i2_-5OwxYgsMAAAKWErA-umviJEOkebZILHe6RU5gOW2jx2GOOwRRD6SQg6nheD6wqsxu9E7Co-NVCgea7Suk-oFjFiPYgmb0vi1MW0oH1P_x7NfMtTTpfY-Bqzi3XoekBw-S51qFrs2ehtnTct5TtOVQ1yF5RJitI252DYc2ib8aJR3rxPdAfnnBc9PVBuPe5pnJudlsL9pIX10WXNNaHZf_JKaMBk-miAU2K33I9NhI_W-KnP2F4XlsqMNsWM0Di7t7He3VbceEk9T-LMOjnjwhLBvfuGbEjSzHC5M03Z5c_cN8MEPSryIx4RcDMQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 05:10:33</div>
<hr>

<div class="tg-post" id="msg-441957">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54ae7efe4.mp4?token=B3hoU_Wtgs_HvV6e-yVFR4LSmfJW9ouOzTD1SO8BHe_5LrIjxKNJciza8K8M2L7UteFzq6IT53d07eTiTmLbf9QhTCtnmGm10z_yb7vgsLplVoAsGcmZbbPMo2x724Gxn-3pFqlT-2CSh8LET6QgJljWCATkJUpf2w4jqbd2bElA7FPY5PsXWNDotqxT_NOqkZ3sC3cNYWF-a1bYnVnhogcv3G_gvnu85IeYRhap-RVJCw8bbx6UsgG1qoK8Sb0Hm49socoFAr_gH0a29W-Y6f8WPQNoSS_tPxhKoCLwS2jLZql2D4ZNS7lyP5zO1QE86uGWZI1cCTfRIHXowVL_og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54ae7efe4.mp4?token=B3hoU_Wtgs_HvV6e-yVFR4LSmfJW9ouOzTD1SO8BHe_5LrIjxKNJciza8K8M2L7UteFzq6IT53d07eTiTmLbf9QhTCtnmGm10z_yb7vgsLplVoAsGcmZbbPMo2x724Gxn-3pFqlT-2CSh8LET6QgJljWCATkJUpf2w4jqbd2bElA7FPY5PsXWNDotqxT_NOqkZ3sC3cNYWF-a1bYnVnhogcv3G_gvnu85IeYRhap-RVJCw8bbx6UsgG1qoK8Sb0Hm49socoFAr_gH0a29W-Y6f8WPQNoSS_tPxhKoCLwS2jLZql2D4ZNS7lyP5zO1QE86uGWZI1cCTfRIHXowVL_og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما از ظهور مشکلات خودمان فراری هستیم
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 323 · <a href="https://t.me/farsna/441957" target="_blank">📅 05:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441951">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آژیر هشدار حملۀ پهپادی در جنوب فلسطین اشغالی به صدا درآمد. @Farsna</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/farsna/441951" target="_blank">📅 04:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441945">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWTOpr7yny19wNjow4oT8d66qQ_z2-n58KNS9Wa9vxCqcGz38qJJzdobOL1-0fIJXrH7fQj7Om3FPJapd5U7Icx2HS5TlnUx4irYDvd2ChBkbwVhBEkH414dkcJtEd6ExRuDFzq_o9f5wqgl1_KNu8LThF7Lvjpe5mQqS2KpSTeAeJpI-xbJV6uMwIV4zqjS-TdGvxsY3GvWD1ewIUmZ_nblbsYhJ68dv6w1yyhTAYvlfsl7AMXSMAMd1P6rUAnvbSgj_YL9Pq-pp9rwXnt3lWSjYrlVQ8H4BkFSpdCdVdSosa6UmdKskJZBymlzLC5wJrrEm6R-XmJYTNAlePTj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژیر هشدار حملۀ پهپادی در جنوب فلسطین اشغالی به صدا درآمد.
@Farsna</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farsna/441945" target="_blank">📅 04:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441944">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLskYtia2cuqzFab3cL55lEsqWHDKd8uYg70H8dPFYpEOnHMOcMoTgeVqJWU6o7nob41OVmowDorXON5zqQzFlJCSK5SbdwgI_ruStvTj5NK0dve9YMIboFps0milOTRF7qAE4tSEJfnmIW8aMikcvDyhMh3a6t2LRMERW5ypApfo2ks452eFGHcA_nn1RleD9E69nQhEUfvBYretnW8aDaylnG5NoSwYfbnwumbXarRBosRaVjiGL1M-NhAK6V8_9cgBVOhOOVqCiF9ToVdHXA7pZjUcT3wEqC9QZoQdSyPOiR7jY2Uu6hwaKtHDQCEaWe21-sSaR_vUD1qNQRElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
زور برزیل به مراکش نرسید؛ تساوی در دو نیمۀ متفاوت
برزیل ۱ - ۱ مراکش
@Sportfars</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/441944" target="_blank">📅 03:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441943">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
رسانه‌های عربی از عملیات صهیونیست‌ها و انفجار گسترده در مناطق شرق جبالیا واقع در شمال نوار غزه، خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/441943" target="_blank">📅 03:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441942">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K37D1ivVithFzgbJLWI6EIi1Pi1F0WmVsf1idsvtVX4GCFcNrvY4IiL_MnBgFuUoag6bC6LhAudAGAlK6nw-Jn6dP1AbrA4PmKRh1Y3lzoklvN_N6-yi9vSJbWYQIqJ8Tpu4k_xD17n-d02p2MDd2FsRyQVgOKuTAwYkwQNPmdpCV2CWEf_OO7iSQEAJQ8j68WBhfXhIouGdJhJ0AHpqZcoA6JlqOa5e3ENBEesUOdysWA8-LVDnm4xVTI9m2qs_-bLPuQFd0L1rRBOBUOaX9tKKmC794pAdJ3C3F68OtQnNZHXAKAqvgnqY3ANq1te4XOqAANDrjndQlnSAn3Hs7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قفس ترامپ وسط کاخ‌سفید برپا شد
🔹
درحالی‌که آمریکا در میزبانی جام‌جهانی ۲۰۲۶ با حاشیه‌های زیادی از جمله صدور ویزاها، سرقت تجهیزات تیم ملی انگلیس و نگرانی‌های امنیتی روبه‌رو است، اما دولت ترامپ به‌جای حل این مشکلات، روی اقدامات نمایشی تمرکز کرده است.
🔹
تازه‌ترین نمونه، میزبانی مسابقات UFC در محوطۀ کاخ‌سفید است. رویدادی بی‌سابقه که با نصب قفس مبارزه، صندلی و سازه‌های عظیم در چمن جنوبی کاخ‌سفید همراه شده و قرار است همزمان با هشتادمین سالگرد تولد رئیس‌جمهور آمریکا برگزار شود.
🔹
از نگاه منتقدان، حاشیه‌های متعدد هفته‌های اخیر، پرسش‌هایی را دربارۀ آمادگی کامل میزبان ایجاد کرده، اما در مقابل کاخ‌سفید ترجیح داده انرژی و توجه رسانه‌ای را به سمت رویدادی سوق دهد که بیش از هر چیز به نام ترامپ گره‌خورده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/441942" target="_blank">📅 03:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441941">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204dfa3f37.mp4?token=CHLKS4L1tzZac_Gl6n48GVKaQYKltkE1GhTBkKPIoRhrajuZx7YL-OLp05VA8WaDEdTzDFtmqMnKCSG67VEZ5-jRq5cRNjMtlm8yLHN6Lzxt8g9BIpgYOz-FiGBJwJH2-KFbg_AjACFXyYDb0DaAs_RQMYaLA3HlJzwUD6E6wCYFrWOJZzPjsqwA6vu4B4vvwpBa5q79Il0Xh03uXfTshPQXshogf90lzOUcErct1cNR1qc0_6gnVTZPd9OAsAnQyOxrv-lv5vYEsS5FSowlEzXW_0it4UbU3jPa4eE1THad8TEaF4TtUbkseQ1hwtxYiJXrt4gpBt8fL2Mo663kdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204dfa3f37.mp4?token=CHLKS4L1tzZac_Gl6n48GVKaQYKltkE1GhTBkKPIoRhrajuZx7YL-OLp05VA8WaDEdTzDFtmqMnKCSG67VEZ5-jRq5cRNjMtlm8yLHN6Lzxt8g9BIpgYOz-FiGBJwJH2-KFbg_AjACFXyYDb0DaAs_RQMYaLA3HlJzwUD6E6wCYFrWOJZzPjsqwA6vu4B4vvwpBa5q79Il0Xh03uXfTshPQXshogf90lzOUcErct1cNR1qc0_6gnVTZPd9OAsAnQyOxrv-lv5vYEsS5FSowlEzXW_0it4UbU3jPa4eE1THad8TEaF4TtUbkseQ1hwtxYiJXrt4gpBt8fL2Mo663kdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات سنگین موشکی حزب‌الله علیه مواضع ارتش رژیم صهیونیستی در اطراف شهرک «مجدل زون» در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/441941" target="_blank">📅 02:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441940">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
در پی تیراندازی صهیونیست‌ها در خان‌یونس در جنوب نوار غزه، یک کودک به شهادت رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/441940" target="_blank">📅 02:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441932">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZgbH94W-Fb_FG7R23rxpK17NxSIFKQzQEC5r5iSHWV923dMkm56mG29Ic6vAt0AsWqfCPliEU2xwptos2lHipNDIb0tm4r9ZQdf_l-hN46KPlX4uuhHU2aA48SL9VGqXUlFSZtT1qNR0EgjlOsztPo4vQKxEOqKC3tp2WwmNhLB2mcWA2L2RYjiP6JkfObJOZj_Jrg3WVtAGikgWQqg9cngiZtdSNN5OOpOY7CQHZP5VeHKPGoGpF4Z7L4xdkQdDjTNH3G2Gol4ZzFYMutjKL9BPp3J_AI3zzA0QR54R7x8O_eOYrW2AzlhAGiCUGQ5yIWc6p6uNMea1Au7wvrX0mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJAedZR2PrRpDAUdPfvmF_cjSrdZHxBm4IBUR8F9gmQirbJbOB4KrVDRRzN36wo2UaJbp2cZe00j3-X2uDcKME8GgM-3_hkNexvyuxnizk73ZIYNFjzqLy1pn4IX-ABWmkuWUeiJbFw9BF3-0QQRpfr2UcrTDUyIYg0YhkcE2InmhyIArrnWaNOTpf1aScJUOqM-ylhzFiCs5C05E_soOHX03EILOdjPEYAt7KCiTCRKKeAUMeTN7qBzA03QuHB6lYWKkWmpyHnlLYWV8AFm0rWA62PJei5JunZktgmq_Hp7eFx0UD0Oz_oHne5GdvNiMGIxdgzR6mJQYtHYsoqJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muzq1tYhk0R4KaiQmYtbFO2M0Noll4v77S3VBgLuMOBOGx38X1jXMJhPNBMwu-Wxl4M5FrBHLxFL_TxruHXljfwZ0e2w-ESgr8TSsHnWIfPad_-f_EtrUTj6ZHLR9Y7i5N0-ZFW8K01kt8WGErN5OCU-bxHBTPEGx3Sh3ieLGS2ZDzl_1E89uvMpXs01lrPU6zwM5jUOZFs84p4YctOx0uTGImubw85UUIkzVPpu06zIx3CIBEPbNSwcwVXx6VSMCZHMcJ2tZYqOv4zTeFZJ-VPDxCiRqD3umBGRYxUY51VwZKnK-rKcSbgNdrkNUeENxKJ24_auqFhROsGK_dRfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiuM8K6PeQdzibdUiwg817oTeyr8QnLwfWhi3R_VvAwJmD9P4_DmTWY56sYyATrFQElvA8Y4VS8EPHgeOoR39Bj_J0oT9_viPpkwXhBSfgehGmHaTT_B8FCEm3ac_izVObJcfoZHnBixvQ0uv9vGZC45SCoZg88fGVDuY1X56umGghuAePbE5Lbyk0VulMU9v7sAC_LUkmjeVrCjKpQN8zPvKMNtOTP1GgCePbsZ3kRvPYx3OApZ-Z7tjMra142hSCWQBhh1wpc6ONNr0bqk7Rxtj_li9ZBIfFkw53mZlOvY5RlLhYhCp_F_ij6irEzU9e_IBb3GdQJuEhzziL65qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_5__EfyXMSA5FnEZ8F9YTAlLRYOTZdf7piQF8DmATwWvQjKmhfurXSinufpYtYEUqSErh_Ua3RB4nTLceKCPa0ZxIPUm0y066926eXGPxKk1VccdkaPT505eB1nRc0BVOYvqWl8rV3mLgt1n9djN56Rs0QoZdmOE0E3ms48wQ6V_BEqplVyW-Vx8kjOFrusP6jG6H1UOy8GIXlQcF8sOsy9_oEBIkbFkA1NqkmkNi9NWlOneyxhm3LIMU1Rvx4ZOKCIkkox3mlgwp0L_eYREM7EHA2ij-JiXYZn-h4dkp0ok1bTwjZxLklw7Km5_ay464gVWatpxksep2CPByanbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COHbylfNfcpqMFZk_oN2-qr_IXhnNWE9At_ne5WwRP20T6hFNely9DtigIeKq7Ds18Ygj8Kob4W1bUY3kGSIqrkfOXqpYFdKpNM8Alj0-tFPW4nQRgyPXDpehuNOx6Ol-zRLR2Iga7C4kgxoq9jRwcWAe-KjVJldzjyGDT2WE46y6nkhQDDkW8BgHya6GB5L1IaTPsR8tM9ZOUR1OQ58IU_huMn1INyB7leOqm68nBjodOdQFnk6Xn41O5T-dGn81S1nrRY4oM5qiQ6vIkvw65S2oGTqTIJUb5yz__TknJyPEQLqraUSZ7EZ9BRGbfBblcRCw-FqtmdRoY62s7AGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpEkGbcJvUivLGA1vrQzYBVKpA6MT9rRn5Rsc-Q8GaFuMtjFfEbFKkRN-aqZzIWfp6SVwsuBW5U5dpzT5QsySOqiQcob4TABM0uDH0lxlsRm3QGbpRrtzaQo2DG4SrX4GAK72_Ud9Y2Kr-viON7OVI263aPzOK3budhPFenr8_-uGA46Sa9VSxioFNiNSGAeRxSjGdFZvsw0qa8gEDYMvzo7uXyiFB-lUtz89gPTNuYm8jWJmQJ1Ot2rEG9swZ6612Gt6MRDYxnk6e_kCY3sgmOljt7__hjIFBOW9OIFiuEDyeZEWykwT27U-HBeuU_Ux5YuZvsKtOrb2FOSDyhsqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PA2J5yKOcV0sfmHxDj5Alqc4npRkT2ddThPq285iCp7Pv9XVTFf8fHPR9MnNYVSVhLr0YxGrcZ6eMJBYIo8tGmmx1OjvOZ1FanlRUuZ0ZJe4KgL-8dbk8aKAa3UrRX_jVjEm6Xie1ferXNDxShTDWMrWckpMhVB7vnjrrRJUA8euH1CX4TRdjU_uURr8fzShZWgdpTWBfkWChx1HN74hoku9MigwQnjTzphRmovtAQ7rgqBLB4Ajn7tF9dDp49Hasd0aEB8A_Tv40RpzfiDpryXeSijlaeHOEUlvNDKnlYRUVO8BakkLu-ThQ3J3wLcLqAQ4UyVmzBp-sgdE30ETBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پاسداشت سپهبد شهید علی شادمانی و شهدای دفاع مقدس ۱۲ روزه در شب حماسی همدان
عکس: مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/441932" target="_blank">📅 02:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441931">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hesHZUR0wxnhL4cNLnEgIQbsAaBOxCkZhnzRZp6m1TsSS1y41-nTMaRckunLVIfXQYrKzcxgfexV03PtXV_4COBfxghYF8AojJvaVHbeN1Bwipy69bEhkIHNrNf6qkWHore-VFRxpG-UoE_VaokaYSAsLRIQXhlYokX194mHiPGiz0VhYohsSxSeCYolnce4zPVDYdrcSBRAkPOY3OJj25fmUIFWhoHxnG88uDU53NonNWeus-m4ICDEs_povv1Yder_ssFqetb8gruG_3wEaD3uzBOhNYT_J-xee44kmvllf63z3JADjXapRGcw_AHWA156cTS88y5Z1vJBLaf4uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوب لبنان، گورستان تانک‌های مرکاوا
🔹
منابع خبری لبنانی اعلام کردند طی ضربات حزب‌الله و مقابله با تلاش نظامیان صهیونیست برای پیشروی در جنوب لبنان، ۵ تانک مرکاوا در شهرک مجدل‌زون در حومۀ شهر صور مورد اصابت مستقیم قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/441931" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFPPoFu74H4ebBRwzYH-Fg627347ztPSWL-mAg__4GR-NcojlKvMVB24b1N1zJL7ioc-U78MyK0yshboYkaawfz2dck80eVSpVnoimhg_3L3DD7EgjnjxAVaxF7XMMsqTWffscj7wzfKijgSlWpePJdSTrpKQRyCnGgXNjJrlqNPXoXNSZ3zRqA3HSQdu7zjbKdFEAnNU_S0VscFlhTD6JU0pDw_H0g7sB0oWfcokPLk-cqAB9ZyFC-e9cE9hn1J6Y8CEUFIEJ323m11x4_BrZru_NZaK-N0GaYMUSpIXFTJiubhW4aDX8nKG9KhLwmM35r0RYgq4z0Hi97tZ0XK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دههٔ اول ماه محرم هیئت در تهران کجا برویم؟
🔹
همزمان با فرارسیدن ایام دههٔ اول ماه محرم ۱۴۴۸ قمری، از روز دوشنبه مصادف با شب اول ماه محرم، مجالس عزاداری در هیئت‌ها و مساجد و تکیه‌های سراسر تهران برگزار می‌شود.
👈
برنامهٔ هیئات تهران را در
اینجا
ببینید.
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/441929" target="_blank">📅 01:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441923">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fP0lxAROeJAd3hMyK7DvtjXZwV5fwtorHkhlaFrRRX8wbW0yQjtk7hITSn5ox_L3uhNXORPCTIrUkyX530AiFJPBEq8O-iVJXxob6MzjOAsj_jsN3_4BzUgnsUKMBbfHmM1Et8LXELuS2RLTxkZMm-ZWOyX49dp_q9B-oPfelujEoghaz06ldyn1DXrVDKA-4hk6ErlQMmVX1jDcN0Hu6mFv-HbTgZbud6v5ABGxwML7OVfzK7gl6aXbnx52R2vsE0PrwZ2aND_P71uj68PIUP1VUODQref7Rff94BFQgy0oTVpV-7lJ5wGowzExXprI-PEPx0WHr24-nu04i2IfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afdX72UnPSRqL2aW2ZgVpx5DewKEGdalP4WlgSD4Sjis-lyrGWVpBrZoh25SICWdmxA-uiUJQNdKx0CaTNnIahE8BWkZcRqqdPeh0JQz5Jz7gsX4GLg0VQ-6C_t8MsDQtH6reCM8BF8x4BbVWGpBMxIenmUhxBfVo3eq8LIZDUPZZhSTfkChVejyLpuUdP83lvR0xIFBmh54rCskVi1xoU0sH1VOYjZZOEBqf6sCuU70PYrzB5T7iQmg_CNgxceyK1BhQYonU6ZN3woz8ebH-6xgv4LZd9sEpGJGmQGnB4LELlRh9a-WazsfYKkK01Oz2ZyxEIOeK3sUygkKjUYKfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFeLmg3e8Ethn7Z1Lu6DI_t3HBMF2nNgQwBopMHa9jVnWSGEfAN5_rGtLFYrga4JVS_O-TxX75L4gCDO0dYCCg18SfZqTKnV-JoDndAvqov_0xe9yQgQdGQdmqJquUI_6b4-EGUFmIqNj9f4k-HlMoqZxT7O3CKZqc2TbwziWwH9iINQxhmpQzWEvg8LCBYAscpsPPpj59AMigTNmeVt07tMp3IDRm8eJh3CBNY-V1Q1F2976OVxlFMkC8YOYcRW9jpYV9nnaCtW6E3CG_lvc7lCQoC8Ztjl3y4SfMal7mwL2lhWMU9Z8Gc60EiWkj_AD2NAWYbl1KRaBexyNhjwVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFG40IuYvljIcyESediW4NDb42swZrnLtQ1mMfEoo0RjSmzCUfnyTjQCMjrHJO3Tcdg5cdefi_QA0bQxJwP_uq-uXtHnd_hVfQ-vNlY13zwoLBPV0D3W4oPa6rPnaXE_3coSqtYaE5uZCrAXM-yvl1wcjAWhrV6dipCZ7cBhvR79mngySpfbB9fn2wOJBycOpxzcpGjSZlPJSwciE9-ZehYc4NTJ36pj9RDebsDvSTcABOdSUnsTtsqsGd4ckGE6PPYlfnNrTKBFtonfIXyCxG1BGP1Wg5Ip6wJSR9nVrt8bA6kgQ-fPOTjF20yTDWE15kAMZqFdxFTjKABknR7ekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SObu3lJsEPrUdkiOxua5kFpHrCpNCZgd4gwdqywXSMLuAmQPEc7WuvH7zN9T5SCimdrwXZ976vF1QzqU0KO3XhaXQvt_1c9u7_ttgggx4G-AtSnBQxWdXgex5lyDmUc_FVIMs2hj7ncnVXkk92pT3a_JyicbeFlS6iD3L_DuJEcYBf_4-fEydLippI4_TFublgoCHkVxiBhH7HC6PsubKwNiBpqSmsi5hAbQ_HPoeGrKjZbKct1Do4Vq1MiqeSfW0iP_aY0jNy178LyJngu_0lH5tehDCg2MqbFOgxXU5FfBQ-Mh5nfV242NJ0dEu6k5A2Ao3BFHg35COOgv8HtvuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hHrN0X1m-QZR3PUylAc0JZc3W1TkOVvhhUgSw72jtXxGfHOctYJnX3VGXexpzEdR-M6L7lBE51m0FkmdCTDPzfRcMe9WugdZYsKIlxu2PhVn7btxpwIQePEXdLF-fdFFRsfn3UqmfOYXtcBw2qr2L2qjzAfVirx9-TTS5uSS0AdqWIMkbHBDnqsF9Guy46q0AXc7EYLSXsZvit4pujsV01RAQQBuAwlRz7_dYAoG0zyyfMKYYTfrdp2dvspyKSk5vAtxQ8rWOV6xgskOy7MhURlnmdE84jkyQCV8ghFU_25qpX0Dfr0j45uaAAYpTUyNIhetoe8SA85yzEjqEn-FsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۲۴ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/441923" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441913">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t3-yfk3KNOeET42diCerPL_0BP6spVIJsu40LBmSXiMLNFeFPkMvvWRjRPxPaws_3VdCt0WsFTP-cwMwM8sqNTNZkg48vUxBs3yI3Z6ncP3s6H0JqzeFfOlhjHVwUrNZMFEoLrkSe393tCtUCljtwJtLmSYJiSTnYkS3n1FOwuIVSCGwEiM32EZQldX2wRZFlcpMJNLPiYtfFBU3bL3Ssbhnc-jOBf8BbdPniHRwLoIaqDfgf9xCgryFjblsYzzPHtAZ1qZHOU5SYhTzBxqZAqSbdc_gH7OglOEBtyWiaFUDHKsBJd5id2UH04Gg4SinXSHlBX9GleqpTyYqJYLDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNhX8R3pszdT5tLsqyXUSiY1TN-E8TXDd2y86fXSo6LHrf6mQQax-t08RGa-xpgfZmC26n65aEdp376jcSpltbdk92yMt4vtpuUB1TCt29_Y2SzMRaxrZ22j_5vFIyTMqs1Q9BkfL10q3BwO6zkeZc3AbthrYOezAJmEJ2HC46Og8cPvidCIFDtL-sKcaQrI7ujT8McaL5n60foLAvXWIXm1QxUJ-0tL_mx7Ro0Y1kMNHGIwGEuLObIK6N3Mk6av3OWOWobfkUSb8FMlbc6C37ciwGP8yM_M9Vz8yeYcOpeLPaQKCYfc7DZWjcX9Lhuk5i3qvO9F9KAWskYuO0BAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WL_BewdcMyEVbQje392MNLP-Z3CHxJUK3qZ_l3kCjNjSk1r2v7tjqfCf0TKTCFnSDhwz2NBWSyYIE78h-bh2hp255azI-quXIUMgImqqtdFOADb6V_VeDy2g7vjvKz3jdyy7TPVQu7pbHN5sCM8BQmgikCXQ6FYXAOmxirOR9sRUigLOwfbMiHLRy3HNIeOTskhC862yBtUoetwpaMlw-IMZ3uQ_GVp9TPcJIFw1RvpSusdqnKpYu5qwSsKtUtKTaqlUzosXEWT6dj-ylHgdK64_nOIy4f-zQS2ce0b2J6JnykX0-cI8EAwvbE9fXRNzrUYIaFjivqMRNihrTnxD-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VCIv5bf5TC2Oy1nBCCETejlMPQZZ85NdF-cWUTgacsPpaYdQF_kaYfqDQHr0_-lkWnOcJle-N4i9IMpsn0JoLKLHtcurRfoP4erLKIzmVYk-72bxW31u5S10CO-QdyNYKNvjjIMicx2owEZlrIufpjyQ3vCtnvDBcLTRnOaqmqkREb_p7iut6Pmfml_DLlCrzecZRWvipw-uJuOanO4lhEVbFQWqoXAmI4EveCIH5Y9Y3xnAUZnr1JaAqtS-vZwRFv71lZVDqYTSBEgFqPpqwKz9Hi4iKBYgqF7nLYLx6_QZGY0CYKuw2T0xYxVe6xngZepYN9iFxPdK6C45maJAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a00KH0GMOwFeg3UgsGihEETyzXBO8ZRg4KAE6mMzu0m1DO_ozqa6XWiITYr3UDuMdbClQh8-L-th5iO9BltKla6nkqP8IY1jIx4exhK5i9QmCM0cLcG8nBU5faZispt4maFOzfMqRwIUbmJB0xmt912nnA11stllNvBWt_tUh73UtuTcJsx23nyKiYtNXqj2ABKiIdytl6A7IhyTQ4TSqyS92UYGjMFuiSfp8C1macRuS4PLL1Nl9TW9faLLDTQ8EDEk42NG5y8MWAp44iQCurDBGRpnWFPm-9Z4wPKtmErZiANA-ruenVRnfXUGWpsyTu5SZzTK_hhPVnvDcaYYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU94-bqbr4FY1xc5GzJy2nsQDERAqbknI6lMYe7Ac6Ie1fpoc4Is5vbSwG12cRQUXgOp6mDvQPSERdA6dQZqO_s4Ip-P8813FN_23mh59sF1oYgKC5fwwQKKcqGMUY4b-C8JsTtruoXb-JbBLZ4L6XC26mh2dynlYp_AZZaUDeqvdYhab38AYmoqBuGeXo9sDbU2LjaJ_ERuSLk0bhg23WfRMtNrG9gYWP0IFpKdp_pGL3mQVlm1SL95r0-7r_atEu0Mgy_qAdGgQKfCR_A7jaIi3HA91OS0pMo_8jpCRU3ijCo98tzBKdV94M0oKCz9TjE_ZidlYe0VmTn1s6uNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ondJEo3SBKentoMIb-rMTh4I_2oMceydrICcj1edln8WAe_1lTdZw1Lnqes76nSEiOmS5e2pqTRM6pLD_1L_DCqUjx2XqsR7ZRx9u_6riIn3ppNYnKKRmkbubYzBYuYsEHVmok2IfyQAfU5T7JXpWoS670ZzGkEyW5plbqdkOU91OldGhYfJAjAYp6jZkDD8DAWkWG7S1eoLBPpt3Wn49O8UpCM7lEtrfZhUPwJFgtWHdwEyhVgXVnlK8AMXZTo1JYJpTexoVqA6Je7RM_S3W0NvuLdVXTo7d74Z6RcjwcKGJDg2CzWHdfAIrFGkPN9k8VL5AHO8TCp_AXx5LOeY9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2dAQOYO9pKSUof0dHS5s5T-etWFxn-fL6s7xtszz3ClbEgBWH0561aDTJvHGmiYPEnBML6zEt6SlLWtGBv4EhIGl1l9sgxpBpZuxsaImqp7akLI7uZ36S2n0oQQyyVIhxGJNebMVZ9KtO2Z2DnmnMjsRY-EZXdhPua4-z99WcP5J_kDrAlVWIxWEgkblehRhRvpsucPDmOUCt69efWE4dD9Ah2nuxmJiu3dx5-cNDqGZWOpeuxSKsns6iKVmX-Byxu6bgh8OcYm_6pqbncbj7epApecAsyI4FsPCce4GH1u--cGm-x9W5kAw5KPLE96O4nlWMV0B9mQ9__BaTAa_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdzN_aaq5dfK5BmFnrfj-QlfTC_txZVesehCAkVu9XwiAYCNA1OFU2m-WiGqvWwmW1b4hLYYRfLyrCByL4yAcxBENTjXmdZkLzFCkJFh7s5CZXkF3J3Bg9vSwiMHTbhNJs44fLJ7WZliJD1PWva8qu1Wf3cgfdudUOxYXTadLEGzQENY5NRiA9T7XtXw4lS0rtr8cssfMfc4oXjohJzhtIQ2dd6t6bnZQ6viIPSESrm-Bl7R46B2M0m1EZgwCfoXHw8hF-ttV3gE4sLZ_w40tIX3VuSZtAHLbS18efVxhcibVbaQ6dp85VTuYSxbc17snx1gBkHotQmlVBALR3GAJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eG4DX8C1KH6gbmuWkqUVRw56DKahMfRddoM8zxH2uFndlKGSHS8w2n25lmQYX_9ylm1JLCdrDEjLyiUdkb4Fj6gv3Ha9cZatgF08YS7Q3FdfhmTA6OOieQIliXFa2w-Rr23V6V_L8uFU0aRK0p8roF27sKycYYehagTyK4n3WLc_wVD0vHQWcfCY5oLsP3UHXmx9Unu1dX3XUXNw2a3_xi9pSv-j-Jbjc8V8-FKk51P6PvT8yuDxd17NzsmE60XedklpErmRd9briyes07u9RPclsT0c5bDdXm_GJgctTolbVoCOxyKSuvsnqIcBzkyYPN5MDXP-2kHv_vxlsZR3cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/441913" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441912">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">۲۲ عملیات حزب‌الله در ۲۴ ساعت گذشته
🔹
مقاومت اسلامی لبنان اعلام کرد، طی ۲۴ ساعت گذشته با ۲۲ عملیات مواضع نظامی، مراکز، تجهیزات و ادوات زرهی صهیونیست‌ها را هدف حملات موشکی، پهپادی و توپخانه‌ای قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/441912" target="_blank">📅 01:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441911">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
حزب‌الله: تجمعات خودروها و سربازان دشمن صهیونیستی در شهر مجدل‌زون در جنوب لبنان را هدف حملۀ موشکی قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441911" target="_blank">📅 00:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441910">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHm80taDjMNHxOKrzFCn8rjNGhQqg4vYvY3sqhjQU-RWIWV6nNQQnqjex7ZP1DqOU1rOdHifag5f8kWcSWhJ3z7mt2UlAMABPjggEjcepZE0vR0X0KlbWshZ0ZoEI_SLCjwjWTpkTWUtmSAe8FcuW6a_647h75p1vW99luGxIMP2DNFseZJ42Buh7yyk4jmY-YSHZ0SVgPM477CWnuVN5I_V5y2nRwzbFr-PIbBYXqEjYWXU0HrBegsyVUMV0JpjkQbKwf0-mBNwRXViZpQmpckyogPb6hIOhfm2z8gbOZl6tZ7qj3343T8UVetd9Cv8KBsjS3uNNH15stHnoH4h_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پایان مسابقۀ سوئیس و قطر با تساوی یک بر یک
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/441910" target="_blank">📅 00:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441909">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دلال‌ها برای بازگرداندن امارات به تجارت ایران فعال شدند
🔹
همزمان با حرکت ایران به سمت مسیرهای تجاری مستقیم با چین و روسیه، گزارش‌ها از فعال شدن دوبارۀ ذی‌نفعان تجارت واسطه‌ای برای بازگرداندن مسیر امارات به مدار تجارت ایران حکایت دارد.
🔹
طبق آمارهای سازمان توسعۀ تجارت تا پیش از جنگ، رقم تجارت ایران و امارات حدود ۲۵ میلیارد دلار بود اما فقط ۱۰ درصد این رقم به تجارت مستقیم این دو کشور مربوط می‌شد.
🔹
۹۰ درصد حجم تجارت مربوط به کالاهایی بود که از امارات فقط به‌عنوان واسطه تجاری برای انتقال آن‌ها استفاده می‌شد.
🔹
اگر واسطه‌ها فقط ۲ درصد برای نقل‌وانتقال پول و تسویه این حجم از تجارت دریافت کنند، در کمترین حالت ۴۵۰ میلیون دلار در سال برای آن‌ها سودآوری دارد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/441909" target="_blank">📅 00:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441908">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
برخی منابع از حملات توپخانه‌ای رژیم صهیونیستی به حومۀ شهرک‌هایی در شهرستان صور و همچنین منطقۀ «وادی الحجیر» در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/441908" target="_blank">📅 00:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441907">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
کاشمری‌ها صدوپنجمین شب اقتدار را باشکوه رقم زدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/441907" target="_blank">📅 23:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441906">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c33fb0f75.mp4?token=Dj-ZpEcv20VXVPnkPcduh3_hD-UzQNkYiLAAVnorbsPfCAKZmwqB2_zoUzVurGUDuGwnmry8ayJr_fw6ziP1heWitBYKnQuOsv_PylWUUGmppkgpljBNTdcQQpVloWlRPBsmcP6UuShbYRpKRj2nHU0STIlHdWeoVDETZ-YD5o00_LKTvQGhGZyhupkR_xBZb-CZlhicrxAZCu1xdi0xh1PYZZbKME7jEI0GZWbWc0GYbxvAGl1CY6i84wuHWYUAt1DTXcJgvI7BaePMTB8LufNlM8g-lW92vAJIk7sFZ_x3RcXufKKymT0ugAcA6fPSouxtaqsLGjUSxAxGucPGqYO86CQe2QBktDoftw2kGvFyO3s_yQNgNN4lstc0gChLK-AcAlbPSJoY00GqJOyFu9X5fsAI8qw-dWOWJMeGA3hiITfzL4CgYvPr8kOcNTat86wfXxN-uBh0G6DomLHMT2tjhEamaDPay3V66JsERv6e-UGF-rwDaKqzG0WZQV6V-CHGCOJ6GStJtk_ANPz7nATq7MIcHoepK_NDylO9NmP1D1twDYypcKT2xY0KiS3n7K7dWrXT8SUWK5zxwld--IOPfRsezj7Au6CPtYIKC7UKULezsrmehmTzhIMg_Y0dX6eqUjLiN9sz6BmIj2mIq7UGw893_n27p97nhgK18_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c33fb0f75.mp4?token=Dj-ZpEcv20VXVPnkPcduh3_hD-UzQNkYiLAAVnorbsPfCAKZmwqB2_zoUzVurGUDuGwnmry8ayJr_fw6ziP1heWitBYKnQuOsv_PylWUUGmppkgpljBNTdcQQpVloWlRPBsmcP6UuShbYRpKRj2nHU0STIlHdWeoVDETZ-YD5o00_LKTvQGhGZyhupkR_xBZb-CZlhicrxAZCu1xdi0xh1PYZZbKME7jEI0GZWbWc0GYbxvAGl1CY6i84wuHWYUAt1DTXcJgvI7BaePMTB8LufNlM8g-lW92vAJIk7sFZ_x3RcXufKKymT0ugAcA6fPSouxtaqsLGjUSxAxGucPGqYO86CQe2QBktDoftw2kGvFyO3s_yQNgNN4lstc0gChLK-AcAlbPSJoY00GqJOyFu9X5fsAI8qw-dWOWJMeGA3hiITfzL4CgYvPr8kOcNTat86wfXxN-uBh0G6DomLHMT2tjhEamaDPay3V66JsERv6e-UGF-rwDaKqzG0WZQV6V-CHGCOJ6GStJtk_ANPz7nATq7MIcHoepK_NDylO9NmP1D1twDYypcKT2xY0KiS3n7K7dWrXT8SUWK5zxwld--IOPfRsezj7Au6CPtYIKC7UKULezsrmehmTzhIMg_Y0dX6eqUjLiN9sz6BmIj2mIq7UGw893_n27p97nhgK18_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشت‌گذاری سنتی اردبیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441906" target="_blank">📅 23:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441905">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📷
افتتاح قطعه نخست آزادراه شهید شوشتری تهران   عکس: زینب حمزه‌لویی @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/441905" target="_blank">📅 23:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441904">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f265eab85.mp4?token=o0albPYe8wN82D20ccBpthWX1vTrVGyUOFbbsjclJwzhbZBEQMwgpx9Q7O-Wcp2Npk7i2f4TOASDwXMH-Vh7gMnUGcBVfw_9yoCLNL9pCwnjyJG43l2-4B6KqOLmmkof6L3UGVmcMXxlE2C0kZU0J-c8n9PZ3-6UcJuIZKNIwZ_LmBoLb355CiobLtcGgGNbalVI9Lw6GaAr7_mYpO4Ugg2uOEtMe3Iq-Tw_EI1Z-1N4x-rI1_3-18gDOtDXEXTLOeqZKBsjRVXWSyBZ7bjYYz9K7a_fqkBZ4Wv8j3ojcyKUfk-tdZhCS-ZHsWpiH743oEhefp8AmffQw6UYUElHHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f265eab85.mp4?token=o0albPYe8wN82D20ccBpthWX1vTrVGyUOFbbsjclJwzhbZBEQMwgpx9Q7O-Wcp2Npk7i2f4TOASDwXMH-Vh7gMnUGcBVfw_9yoCLNL9pCwnjyJG43l2-4B6KqOLmmkof6L3UGVmcMXxlE2C0kZU0J-c8n9PZ3-6UcJuIZKNIwZ_LmBoLb355CiobLtcGgGNbalVI9Lw6GaAr7_mYpO4Ugg2uOEtMe3Iq-Tw_EI1Z-1N4x-rI1_3-18gDOtDXEXTLOeqZKBsjRVXWSyBZ7bjYYz9K7a_fqkBZ4Wv8j3ojcyKUfk-tdZhCS-ZHsWpiH743oEhefp8AmffQw6UYUElHHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
می‌خوانیم تا پای جان، جاویدان ایران
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/441904" target="_blank">📅 23:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441902">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e8ee66e6.mp4?token=gTXpi9mwV-pLZhS1ze12dmfloloAfbVZFQN4lK8Kfr36AL0Ffe3cxjsfAU296igQNWjkRumassB8YFjz3PwjW-l11bvamiXsIEbMwCZo_jWKM4yLMr5f0AdKxU7aWyPbPcyTSgxUdH6HJMq3g0CPdSdr_6XOUSR1rc9OCQ1Poq4y1ybtxXYHRXNrxhSyT8iHnCTfSR0_6pmDaJ1FMsWTdDPyCF_EbrLqyLigMjv8wVYq8xAoYs88tECdSfi-Gk_AF7kFOkWZ0jl2_Q4C-obaXb-jLa_lk2ebBKvhLzJ9BhHANuEHbDjTZAAOOazvdjqxkkEFEpVxOsksDDgqA_DOQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e8ee66e6.mp4?token=gTXpi9mwV-pLZhS1ze12dmfloloAfbVZFQN4lK8Kfr36AL0Ffe3cxjsfAU296igQNWjkRumassB8YFjz3PwjW-l11bvamiXsIEbMwCZo_jWKM4yLMr5f0AdKxU7aWyPbPcyTSgxUdH6HJMq3g0CPdSdr_6XOUSR1rc9OCQ1Poq4y1ybtxXYHRXNrxhSyT8iHnCTfSR0_6pmDaJ1FMsWTdDPyCF_EbrLqyLigMjv8wVYq8xAoYs88tECdSfi-Gk_AF7kFOkWZ0jl2_Q4C-obaXb-jLa_lk2ebBKvhLzJ9BhHANuEHbDjTZAAOOazvdjqxkkEFEpVxOsksDDgqA_DOQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهتزاز پرچم فلسطین در بزرگ‌ترین میدان نیویورک
🔹
هواداران مراکشی جام جهانی پرچم فلسطین را در میدان تایمز نیویورک به اهتزاز درآوردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/441902" target="_blank">📅 23:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441901">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2062b21633.mp4?token=pbo7TB51PkkXePA_pPiAJQPo09K2egxXMqxjcCsT36nDqRSDuZ7kpioRcq1DbZxoFIQuxp2WDbGfN4mKpDPfUaY9J1j6LCO02O27AmTJyDFPOUz4zrb5mxSk99r7qajiWlZyL1Gc9_O3zLgCArmHZft70Hg74hlmb6mPS5jic8SfGXNtkjjughbqI3GT10LQdiWb3yUYOilBPBOS6hDhK6bY4hh01E_l0LIsxmKzhyYsTZ7iuiV55wzot2ZREaZsnSZyfp9oWSzsV5JK2UD0OcTjGjjCzvHMboWf5qJzZWgwa48TYk7YqU_wlzfFcUVGYNS-cH3TN9TXcWZu2jUyfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2062b21633.mp4?token=pbo7TB51PkkXePA_pPiAJQPo09K2egxXMqxjcCsT36nDqRSDuZ7kpioRcq1DbZxoFIQuxp2WDbGfN4mKpDPfUaY9J1j6LCO02O27AmTJyDFPOUz4zrb5mxSk99r7qajiWlZyL1Gc9_O3zLgCArmHZft70Hg74hlmb6mPS5jic8SfGXNtkjjughbqI3GT10LQdiWb3yUYOilBPBOS6hDhK6bY4hh01E_l0LIsxmKzhyYsTZ7iuiV55wzot2ZREaZsnSZyfp9oWSzsV5JK2UD0OcTjGjjCzvHMboWf5qJzZWgwa48TYk7YqU_wlzfFcUVGYNS-cH3TN9TXcWZu2jUyfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع بارانی مردم بجنورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/441901" target="_blank">📅 23:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441900">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a44fe66cf.mp4?token=fxd-rCaJWu8I50bBHVMZpYmdsQvU1fQDE3pXXx84QtfTc5fdeOoA9sZdeKMiXLGrFZkv2vdqMde0Y-im-9eqKauf-LLD7RGuUQYigha4wlkZ8CvYUg6lzwvvdqWITpOCXY5QFWF4SLxL65vmhnRHBUxkoq3uAWXdxQLZnyJFRQJsFYsChmE5dM87Sp6o1c-p9FzRdEwQ3moLXQel2fse7k-valVlRILXcrWA4OpVWvqaK-eGJZ5_Ai-06P5jMXIRmrrjf72vGmCMF2625J1azHUWG4ere7DYfaOtKJmtyKOKhdasBKyaDyOLvTKP3LjKJRywcwuAsaY-OiVFndpVZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a44fe66cf.mp4?token=fxd-rCaJWu8I50bBHVMZpYmdsQvU1fQDE3pXXx84QtfTc5fdeOoA9sZdeKMiXLGrFZkv2vdqMde0Y-im-9eqKauf-LLD7RGuUQYigha4wlkZ8CvYUg6lzwvvdqWITpOCXY5QFWF4SLxL65vmhnRHBUxkoq3uAWXdxQLZnyJFRQJsFYsChmE5dM87Sp6o1c-p9FzRdEwQ3moLXQel2fse7k-valVlRILXcrWA4OpVWvqaK-eGJZ5_Ai-06P5jMXIRmrrjf72vGmCMF2625J1azHUWG4ere7DYfaOtKJmtyKOKhdasBKyaDyOLvTKP3LjKJRywcwuAsaY-OiVFndpVZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاره‌کردن عکس ترامپ و پرچم آمریکا در هند
🔹
هندی‌ها در واکنش به کشته شدن ۳ ملوان هندی توسط آمریکا، پوسترهای روز استقلال و عکس‌های ترامپ را پاره کردند.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/441900" target="_blank">📅 23:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441899">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44ffff4956.mp4?token=OaPdgr-f8zlcMJwpTSVdOFtFYbxyfPfddQXUr92WrXDe_VUsxao2TbpgBUJRtv9pM62GFVSqP4BidoDnYrN0UJHJU2n1cS4hHPab1F6UBoDZ5HrTn9q8rzZGVkQVEcj6PLd3ZCgq2gGRYVBi-M9NbPjawLBz2XJSL95QMV4NFkUTPltPRiP51SHCLwX4_Fw1YHcTsmeS25LmQqGgmFY7LXRceEqsHZzTBJt8HFPq-sxlaiFa0HDA81CGgmc0Z0PqeOZUY837TsLSbFXzJ3fI8vwF4pwR1JiuD4r4yre1NT1pKVOhLMaJ6sUEhv2FmAZWXQ97wMtb3774328mgkYlog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44ffff4956.mp4?token=OaPdgr-f8zlcMJwpTSVdOFtFYbxyfPfddQXUr92WrXDe_VUsxao2TbpgBUJRtv9pM62GFVSqP4BidoDnYrN0UJHJU2n1cS4hHPab1F6UBoDZ5HrTn9q8rzZGVkQVEcj6PLd3ZCgq2gGRYVBi-M9NbPjawLBz2XJSL95QMV4NFkUTPltPRiP51SHCLwX4_Fw1YHcTsmeS25LmQqGgmFY7LXRceEqsHZzTBJt8HFPq-sxlaiFa0HDA81CGgmc0Z0PqeOZUY837TsLSbFXzJ3fI8vwF4pwR1JiuD4r4yre1NT1pKVOhLMaJ6sUEhv2FmAZWXQ97wMtb3774328mgkYlog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خرم‌‌آبادی‌ها در موج ۱۰۵ با قدرت به خیابان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/441899" target="_blank">📅 23:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441892">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbQIQcz_rvAbYaenK7cb7S_irk3zTI9KWUFL1BWP23_wMRMrZrbKABLJ-UH8J6g9R2XY7oYdO3HyLHfC-WauPofzdfQB-pDoXJjLRIpldCZnHRQAsPo_VNTztJNMyKAjSnSZlgsc7E-wp3MBNZiqBYRZeCwoWjB01j6ZiEhBlCjbegJmkxSE8Vs--zPrrHWZu2QVvxozDT-0MtrNN6q0RKIAYW9A8DkHH8B3x2fMd0NcYr6Qj4u2SClM3Jn51IIlcaTNBQjQWJns4CC9qi9UhFeZlxnzIzozc7C4RL6Y0AEo8UjnwO5D6mIyTZsNAusWvmAYmzwIWNCbCWmB7FNktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CS_U1AfQ4J0ygA5JQYRWQDxFt_cwQhoeVuyvH7qBTLrFFTNJOcyOj9iDZ2LwXLJBSgs7IJ5PgUtnX8W-AuZ13XU70PF0YQIr-R08ACd1jgNcmg8mLbVjRAvtf6-novqJFWo7dZ0eRjsIt-TEcRPXnTZ-rJjA0Lh_MwOsTNm5lJReVGGvypj8hVbLfq_9_Vf3D3o2byBK_hegiGltbsSf7LN7iIXBJzfBZSfwgS_XGF9PZg78-p89Iuj7DKIGS4U2YjvQcb-9cB3gXvz1oEYV_t6NO6I0l0r2KU5D5qLFeITgvVhqe0Jla8Do4GaBdknMHSKNtILLDD-ztVZ-5hG28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gpx_MJB_hkTrAGQQTwpwjZd9N2NjvR8tWxroLGR1Fu02ePiOQiZpX4CUKw6-62hNLV6jY99ct7o-ppt4VnWaVK7zp_xF0-iVHw3BDqHT4tiarPBLpCr52VyabKysUCj4E5xBvOF4NmVBAhOLwiZYW0rRwOP7WDvBwWq2N7A95piej2IqN1UwNDrIErH4v8ncsxSPkItUWee4tWgFsk9jdwxdOm2GsYfFDt3ofzRTTqf0RbNwiHJob8HqZzW9MEgU_vkN5cHQOjMwOYmhgXLb4Hvun0CgdnHWcy1uTFx5_7TBrfvPS9rPaWiO5nHGwoQqe40Wp2G74Ww5Traq_kgjMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wn93a_k1jTyR-I0F1JHoieb4FSDaFg8X9Uk-OF-wFWLuxfOU32mrQ4atD2WVrZA96VEZ3Ma4Ocp3y8TVROENIHyd3rNRcQ5f17zzvztHfQk3o_i0dyFlVzpSWg33aPxxPsb1Rz3KQugLX3vmbNh5r7kaOQamGAwZL4cdnFkrhG2ogKEAW14oJeHhInx2Ah3YskH6e8VCfZudf0zIQP0onBcTDp5uwT1HPLd4KqnAtr_Gln0Ax5DAX1SzjGoIy_rxuQoxtCDzdMqAPiec2-pAcXl7W8MLTR8o8lJrkD2pAwzSC5ikj9SWjmRUa-rFBZkTxzqA1pZ0jKdGmxmDVjnG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNtwpjhzFyqekht1DKJMzyunnbFuf9udZjNkzbJr7lSXidygN2aVFaRROo4SJvW89hLmjUA0iZ0d82-FbCypC9W9Vw_pbKyrcuD79T6BPHDV85ga4LDuPz6P7-CXOoiB8-aPNF1tTlNy8y-PMitGOTw_Bv3F3_QoP9viDhQZcl0tFdfD8T1SXKcKDSTN0KdNlb3zg73ldrNzPPfi2u1Dl8Xmm_SLKUaid5BiQ7txqj_eserELAYGdQyY8v-mfKvBEKB2J0yBxpDJsEmDwuCOD_WWRgh1ebrPOiZ1SjFG49Px1GupMu05QXxdSewck0vn6ftraZdlJTcgJfgpy80Z2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mugUiw24x4WkhBA49dztj3qTNEE5r5Ddp8cO2S2cdKgkT9tyIHFp-RGdnYZD_-kHDR71oydnAEhKfzuZ6kSEQkPbSvk4MPsEk5KoIzGZhiP9hT46uKm4iLsyHe1jn3pP6QA5NWGf74Fr34t9XehRVb2-cqhFsTtcnoFgdY2PLIaLTbZPxyXnTaNQ_r9bhPoZbaRdAaaOafgwIrnRXNNGsscvi42J3RLMobfjDp1ZP2lab1xsWSS8tv9kwEHE3mrBwyCkl6mfYWg4RJKCV4uUyW4AZsrJTd1Ywo53viNOVsvPet9w4KnEfdqmDYNJ6obvRpvpw88pqOWjzmx6YwdfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMlr7OfQSJrrXO73zXOnTy5XaCEUcRiDW8QHoH1e-m5pBVS9kPFfHxKGC8EBiF_0NeubT3gSv2B_oEaejPPAB8Wpvx_aD4Ihl6FsFkox6x18m_E0uBZhHI-uYxkwfxl1m4CrWGifO1oZDtiJxm9NX6YQUw5YB4YDwqG0z2wUY1Ize3oFsoviHq-eKRAQR1DKClZwZXq_lJsFcNGWnG3oxmSXjHjAfR9blHtK2xlD90ekD-nC9JW2IY8xdnJRz5PCO2pDRRhNidPbGLHZwNnZ4K6ltt1GJ-6DSGcJcCos7hvjAE31XIHaVxgWEbWE_GSqXs5FTGYf9EfG9_bm-7lL3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین سنتی تشت‌گذاری در اردبیل
🔸
تشت‌گذاری آیینی مذهبی در مناطق ترک‌زبان است که به یاد تشنگی شهدای کربلا چند روز پیش از آغاز ماه محرم یا در روزهای نخست محرم برگزار می‌شود.
عکس:
سیدمهدی پناهی
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/441892" target="_blank">📅 23:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441891">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f3ac65e4b.mp4?token=kvb7anPbiU-4HDj2R47PAJDjVxxob8b_ODCgkaHkqnFRpcY9zWTFaObBPdZIuX8Bz4pe2OUrZazKTkeyA3CArgRrd_MiNHPxbGsYyN5lv6uXcFzNiKmUHEJGfDCPKxH1FDdqlsGImHJf-S5yLpcdCJd-DZPyt7mEdFsijfRlN1isfW_vQKMHQ3ejCfnq42ZL4ghkzPPcjXDmYN9XEypfKNYiZmOAvtg0dniEboHQnKXXO1vmJn77bCETW4B8tW0Gky-6jJYB0Amqy8YSEuE8rstBvdH96hxb3BPP9-3Ztpvs4jySF0000gTAJNa6mhl-TtUyxYxSm6XLVA9ppuT5Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f3ac65e4b.mp4?token=kvb7anPbiU-4HDj2R47PAJDjVxxob8b_ODCgkaHkqnFRpcY9zWTFaObBPdZIuX8Bz4pe2OUrZazKTkeyA3CArgRrd_MiNHPxbGsYyN5lv6uXcFzNiKmUHEJGfDCPKxH1FDdqlsGImHJf-S5yLpcdCJd-DZPyt7mEdFsijfRlN1isfW_vQKMHQ3ejCfnq42ZL4ghkzPPcjXDmYN9XEypfKNYiZmOAvtg0dniEboHQnKXXO1vmJn77bCETW4B8tW0Gky-6jJYB0Amqy8YSEuE8rstBvdH96hxb3BPP9-3Ztpvs4jySF0000gTAJNa6mhl-TtUyxYxSm6XLVA9ppuT5Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی در یک مرکز خرید در آمریکا
🔹
رسانه‌های آمریکایی از تیراندازی در مرکز خرید هِیوود در ایالت کارولینای جنوبی خبر می‌دهند.
🔸
تاکنون دست‌کم ۲ نفر در این تیراندازی زخمی شده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/441891" target="_blank">📅 22:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441890">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7794a1c2ec.mp4?token=l5QJazhqa8iUCZCR-kgfwy3lrh254u1jB_DjxDWUY57Da_7R6qwEa9s7APZz3UIB2FzVc5h6fznVWK0CxFa8zIqnySqZroSvKnFZ96ySwKa1t3iolqkyRU1iMtML-Oiu-nIZYEI2NlOq5ETZj7Uu9_Fj3l_NNOx1usO6S51r-dXy3HpyUk34J-AJaBfsjlHpx0mMwa50QZiiLplwzwJOyU3I6NBZs9oEGMC0UMASwmphLK7TqLaGrjmge21bOmf5MrnO5WohDilYnelnQGEEIJELLBnHn49Y_XDhagDNbvB1vwbiHhqC59LQu22gDNymu4egvSnjM882a590mxxf7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7794a1c2ec.mp4?token=l5QJazhqa8iUCZCR-kgfwy3lrh254u1jB_DjxDWUY57Da_7R6qwEa9s7APZz3UIB2FzVc5h6fznVWK0CxFa8zIqnySqZroSvKnFZ96ySwKa1t3iolqkyRU1iMtML-Oiu-nIZYEI2NlOq5ETZj7Uu9_Fj3l_NNOx1usO6S51r-dXy3HpyUk34J-AJaBfsjlHpx0mMwa50QZiiLplwzwJOyU3I6NBZs9oEGMC0UMASwmphLK7TqLaGrjmge21bOmf5MrnO5WohDilYnelnQGEEIJELLBnHn49Y_XDhagDNbvB1vwbiHhqC59LQu22gDNymu4egvSnjM882a590mxxf7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاسوج یکصدا: پای شروط رهبر ایستاده‌ایم تا آخر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/441890" target="_blank">📅 22:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441889">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f61f906f05.mp4?token=Uasmpl5Fk4cuBvZlhMkBiUDBwZyUtY1iJfM4OEr6NLnrZGuaA9rRu49Ef7VRNP65tsOe6DSl8JwBp7oykeCKKnFv8ACwzsaOZuFLndaE9Xkuwh6Y0Q4UIzlXNYxYEjohVtKSvycQ8atvv7L_83yWYoZaNaA7hJY8wkQP873G_tqassdf3NBaMrp2vV9WlP7d1i-MZJd1EEPMdVqmbHQbjs5-SGaRB3BsylWyz_tyNUxkVRS6vhiSM4Rx42rRZtITSdLP1FYEl3BJUrw3JbJ1ooBH3h5d1Fhf6g_vZCkTxwIgyhFVGcGWZ49f7BzTYRyJUDVwhG-yqr7gF9THrv6NGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f61f906f05.mp4?token=Uasmpl5Fk4cuBvZlhMkBiUDBwZyUtY1iJfM4OEr6NLnrZGuaA9rRu49Ef7VRNP65tsOe6DSl8JwBp7oykeCKKnFv8ACwzsaOZuFLndaE9Xkuwh6Y0Q4UIzlXNYxYEjohVtKSvycQ8atvv7L_83yWYoZaNaA7hJY8wkQP873G_tqassdf3NBaMrp2vV9WlP7d1i-MZJd1EEPMdVqmbHQbjs5-SGaRB3BsylWyz_tyNUxkVRS6vhiSM4Rx42rRZtITSdLP1FYEl3BJUrw3JbJ1ooBH3h5d1Fhf6g_vZCkTxwIgyhFVGcGWZ49f7BzTYRyJUDVwhG-yqr7gF9THrv6NGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مقاومت جانانه مردم گرگان در شب ۱۰۵
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/441889" target="_blank">📅 22:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441888">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690182037e.mp4?token=n475RLnt1eUpo_xj7JpXHQw6hU3fCWysfLqrrpBfUvL608e7e0of8yUFLn_Zkhm_mdWYfgYl4hTwbHdXQDYUE9C75acFpcs406VYGww9m5ipBtlc6eO9Npk12Nr-L-pqeeSoH-X4J7GGI1pAQcbr2hguOLB82bi8G5XMlUb08Mb9lcj9SscItR6-LknqowKMwpzmbbmNLLc8D6mODP0apctemtI17wpxqsJ6MMKZuObav9YIfA5M_LKrVhNbCAjnOA7LrmdyLmyJQyp_PLw0REf0i49YqgeIdWCgaSmVXTcq5pOlC2QXmR-1oHTv9s_FmDq1Mhw0T4B07mV0YsKq74WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690182037e.mp4?token=n475RLnt1eUpo_xj7JpXHQw6hU3fCWysfLqrrpBfUvL608e7e0of8yUFLn_Zkhm_mdWYfgYl4hTwbHdXQDYUE9C75acFpcs406VYGww9m5ipBtlc6eO9Npk12Nr-L-pqeeSoH-X4J7GGI1pAQcbr2hguOLB82bi8G5XMlUb08Mb9lcj9SscItR6-LknqowKMwpzmbbmNLLc8D6mODP0apctemtI17wpxqsJ6MMKZuObav9YIfA5M_LKrVhNbCAjnOA7LrmdyLmyJQyp_PLw0REf0i49YqgeIdWCgaSmVXTcq5pOlC2QXmR-1oHTv9s_FmDq1Mhw0T4B07mV0YsKq74WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایران‌زمین در شب ۱۰۵ هم میدان‌داری می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441888" target="_blank">📅 22:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441887">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">احتمال توقف عملیات زمینی صهیونیست‌ها در لبنان
🔹
سازمان رادیو و تلویزیون رژیم صهیونیستی به‌نقل از منابع امنیتی گزارش داد که ارتش رژیم خود را برای دریافت دستور توقف عملیات زمینی و پیشروی در لبنان آماده کرده است؛ اقدامی که گفته می‌شود در چارچوب توافقات و رایزنی‌های جاری میان واشنگتن و تهران مطرح شده است.
🔹
براساس این گزارش، رژیم صهیونی قصد ندارد از منطقه حائل در جنوب لبنان عقب‌نشینی کند و وضعیت این منطقه یکی از محورهای مذاکرات و گفت‌وگوهای پیش‌رو خواهد بود.
🔹
این رسانهٔ صهیونیستی تصریح کرد شاید روزها و ساعات باقی‌مانده می‌تواند فرصتی تعیین‌کننده برای گسترش عملیات نظامی و تسلط بر مناطق جدید در لبنان باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/441887" target="_blank">📅 22:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441886">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyrf2QbOrgc47SImsZdccIpLvp23Mu-jqmiQTG22_8zcB3cs-uyrtrXrM-ooICYM-lSgcDPTGizhwFjLUlqGkXNjtEUj8yaeV7SXKIGjJffAfpCga9ph9XdL8umg6gkjxOowy13lpvniXQuC0hk2yZsSsF40pgS5DbMueXj1ew5F1hBqGQ6X75ROPXSEsWksHFjxITrd_HS-ZKnncs_ems4klAki-6C3VwlBdx7Y4yXCD3Z2L7uFNmmXm7I56cn0ptu14L4ifeYRW9o69vyqvUo8KvS34pYD0azBM7M3czgnSck3raifiD6O8Kea2BXJ60mbm6LsRoAv8pgpPOm5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی قطر: ایران برزیل آسیاست
🔹
لوپتگی، سرمربی سابق رئال مادرید و فعلی تیم ملی قطر: ایران برزیل این منطقه از جهان است؛ تیمی بسیار قدرتمند. اما ما آن‌ها را شکست دادیم و به پلی‌آف رسیدیم.
🔹
من آمده بودم تا قطر را به جام جهانی برسانم؛ حالا ما باید واقعیت خود را بدانیم؛ ما در جام جهانی مجبوریم در اکثر دقایق دفاع کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/441886" target="_blank">📅 22:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441885">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_vEab8Q39HiCT0BQoBMYevfcYD6uvf1kyVj7aNZabnLI0lkPY_aY2mbAQG7wT7GqQlsXbjUntEEOI6t4vDcbi1H6rjA1tKJb4aoUxnWhFGdorQUfLE72jL-RtHPBduDLuzwsxrnJelcP84rw0iJq90dDSjhnPPfHcNRnQfqTQ4qk-mCnWrH38HjUEdWLsll2MJO-GlLjn7UGrgmUzPWi0BLgT5ULu3Y0i4YdFUJf6ara5SORk0rqe4cS-ODQrkyuzoyRcofd_xxMs6_yaGiwvnnbOunPYnIHlTbd_yz8Pz6XGF6FlF2AT5QFRamVPUfgvrm4dHsATBwP4Kmc3wl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
#ویژه
| نگاه رهبر انقلاب به مذاکرات توقف جنگ چگونه است؟
* ۱. حکمت امتناع از ورود علنی به جزئیات مذاکرات
🔸
نخستین نکته آن است که ایشان درباره محتوای مذاکرات، الزامات، خطوط قرمز و شروط مدنظر خویش، در پیام‌ها و موضع‌گیری‌های علنی اظهارنظری نفرموده‌اند؛ بدین معنا که به‌طور مصداقی دستور نداده‌اند در
#مذاکرات
چه اقدامی صورت پذیرد یا از چه کاری اجتناب شود و یا تیم مذاکره‌کننده چه عملکردی داشته است.
🔹
عدم اظهارنظر ایشان در خصوص اشخاص مذاکره‌کننده، نحوه عملکرد آنان و همچنین جنبه‌های فنی و محتوایی مذاکرات، واجد
#حکمتی_عمیق
است. ما موظفیم منطق و نگاه رهبری را به‌درستی درک کنیم. دلیل امتناع ایشان از کشاندن مباحث مناقشه‌برانگیز محتوایی و فنی به سطح افکار عمومی، خیابان‌ها و فضای مجازی، ریشه در همین حکمت دارد که نیروی مؤمن و ولایت‌مدار باید بدان توجه ویژه داشته باشد.
*
۲. میدان مذاکره، امتداد میدان مبارزه
🔸
نکته دوم ناظر بر دو گزاره‌ای است که رهبر معظم انقلاب تاکنون در یک پیام پیرامون مسئله مذاکرات مطرح فرموده‌اند: گزاره نخست: ایشان خطاب به مردم فرمودند: «فریادهای شما در میادین بر
#نتیجه
مذاکرات مؤثر است.»
🔹
گزاره دوم: در انتهای همان پیام، با توسل به ساحت مقدس امام زمان (عج)، از آن حضرت استدعا کردند که برای پیروزی ما در «میدان نظامی» و «میدان مذاکرات» دعا بفرمایند. این امر به‌روشنی نشان می‌دهد که عرصه مذاکرات نیز خود میدانی از
#مبارزه
است و نه‌تنها در تضاد با مقاومت نیست، بلکه جبهه‌ای است که در آن تقابل با دشمن جریان دارد.
*
۳. تفسیر صحیح «تأثیر فریادها بر نتیجه مذاکرات»
🔸
اما تفسیر صحیح این بیان که «فریادهای شما در میادین بر نتیجه مذاکرات مؤثر است» چیست؟ متأسفانه، برخی از این سخن، مجوز فریاد کشیدن بر سر مسئولان داخلی به بهانه
#نقد
و مطالبه‌گری و به‌اصطلاح «باز کردن دست ولی جامعه» را برداشت کرده‌اند. این تفسیری کاملاً ناصواب و در حقیقت تحریف مقصود رهبر معظم انقلاب است.
رهبریِ ایشان مبتنی بر
#مبانی_قرآنی
است و فرمایشاتشان هرگز مغایر با آموزه‌های الهی نیست. قرآن کریم می‌فرماید: «أَشِدَّاءُ عَلَى الْكُفَّارِ رُحَمَاءُ بَيْنَهُمْ».
🔹
رویکرد حضرت امام (ره) و آقای شهید نیز دقیقاً بر همین مدار استوار بود؛ چنان‌که آقای شهید بزرگوار پیش از جنگ دوازده‌روزه فرمودند: «ما به
#دشمن
بدبینیم، اما به نیروهای خودی خوش‌بینیم.» این بدبینی صرفاً معطوف به خوی استکباری، عهدشکنی و ذات شیطانی دشمن است، نه متوجه تیم مذاکره‌کننده نظام.
* تفسیر ایجابی و سازنده:
🔸
تفسیر صحیح عبارت مذکور این است که حضور شما در میدان‌ها، حمایت از نظام و مسئولان آن، و پشتیبانی از تیم مذاکره‌کننده، موجب پر شدن دست نظام در برابر دشمن می‌گردد. این
#حمایت_میدانی
به تیم مذاکره‌کننده اعتمادبه‌نفس و قدرت سیاسی می‌بخشد تا در برابر زیاده‌خواهی مستکبران ایستادگی کرده و اجازه عقب‌نشینی نیابد.
*
۴. لزوم فهم منظومه‌ای از بیانات رهبری
🔹
ما نباید بیانات رهبر معظم انقلاب را به‌صورت منقطع و مجزا از سایر پیام‌هایشان تحلیل کنیم، بلکه نیازمند یک «
#فهم_منظومه‌ای
» هستیم. یکی از توصیه‌های پرتکرار ایشان، تأکید بر حفظ وحدت و انسجام است. ایشان صراحتاً می‌فرمایند: «انسجام بین ملت و دولت و دستگاه‌های جمهوری اسلامی یک نعمت است» و تأکید می‌کنند که حتی به اختلافات موجّه نیز نباید دامن زده شود.
*
۵. باور به اقتدار و تسلط رهبری نظام
🔸
تصور ما از جایگاه رهبری باید روشن باشد. آیا رهبری را شخصیتی مقتدر، مدبر، باکیاست و مسلط بر امور نظامی و دیپلماسی می‌دانیم، یا شخصیتی منفعل، تحمیل‌پذیر و تحت مدیریت دیگران؟ اگر به
#اقتدار
و اشراف ایشان باور قطعی داریم، هرگز نباید گمان کنیم که اشخاص یا جریان‌هایی می‌توانند تصمیمی مغایر با منافع ملی را بر ایشان تحمیل نمایند.
*
۶. رسالت ولی‌فقیه در صیانت از آرمان‌ها
🔹
مهم‌ترین رسالت
#ولی‌فقیه
، صیانت از اصول، جهت‌گیری‌های کلان و منافع ملی است. بدیهی است در صورت بروز هرگونه انحراف از آرمان‌ها یا سازش با شیطان بزرگ، ایشان شرعاً موظف‌اند با بهره‌گیری از مقام زعامت خود، به موضوع ورود کرده و مانع از انحراف شوند. لذا، عدم ورود ممانعت‌آمیز ایشان در یک مقطع، منطقاً بدین معناست که مسیر طی‌شده مصداق انحراف، عدول از
#ارزش‌ها
و زیر پا گذاشتن خون مطهر شهدا نیست.
🔸
مجموع این شواهد، چارچوب نگاه ما را در خصوص نسبت میان رهبری و تیم مذاکره‌کننده روشن می‌سازد. البته هیچ‌یک از این موارد، نافی ضرورت هوشیاری، دفاع از
#منافع_ملی
و توجه به هشدارهای رهبر معظم انقلاب نیست؛ اما باید دانست که مرز باریکی میان «مطالبه‌گری فعال و هوشیارانه» با «تخریب نیروهای خودی، ایجاد اختلافات داخلی و تحریف بیانات رهبری» وجود دارد که مؤمن
#ولایت‌مدار
باید با بصیرت کامل از آن مراقبت نماید.
@rahbari_plus</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/441885" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441882">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqXUQUCRLdAkirp75HqUfDhT_8IEO3lhA1PHcUmZSBWpM7ORjmw3LOhKWKtLnmXBEGhnz9BFCggQCFqnl4Pnz_zcHVL_kdKE9QJGY9e2vDA__BoEPBfsaOR3QhYvmMllH0eu6KhATFo8Id-X1VduqZHYO8q9xNfkw0ADfsqtysptA_E9LUpQ8Nqec6yFHvGNv1AnbCIGN-u7TeNte4__Z5aAr4xPpboWZgMtzRSvhwIkbzf8M8TLHr1D9LSovSN-1fWsq-JoTWH8mnwGaSLngZMMk6n27zQTrrBVbEHBndRDacvNC4eqi-p60tu_w48Sjl9kksbfFKrThP7pc24HdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVarHlPCcpCoLlar2pSMmurwz1TdUEvoEiXyTtGXTT8U7Klb46FxuE4JZFPOT4rLbuZd6jt1VHXRZAMH4ekjqf1cG2a5w517F7yN76Ge7N4_TfgNRc6T6EB0mKBIgWFDPPWar8miXjXcnlza351jw-p5t1LE7BD-9CCWyfOyE7IGrEKDoqgGrSglivOesiBcMAsyXthIGtys5nCrJ7s9vbBDhqeSwwSQ5FUwB9lAxmo_-GIltISdMsLMpOfp_6I5c8UjqtqOlkhSjKLZfsoMcBNEmu0zX6NcP4LHrj2QsRHz0NGZVCFKLh1vFXiErHteZKHUWOh7V-1yQXpfArma_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBhbvLQ4h6ux9yoYEik0QZdoQMaKKkLH3NMkzDhS2zHbyT6eaxqSK8laUTd8ben823fKZSL44nnIeVnLWG0MH9VGxc3jhKeEUAlacc_MJd1PXnj396oPWkKTZ2mreLko4fxHJ9BUloC0NmkY6WeyHZtL3h72bI7y2X0QtU-kCeBV2IeTAexXGO_RSOHCNrcrc5tDDX5zL8LD3d-_Kelys_hwqP1c-XV_dlpUsh8b85xAuVoZkBtRNJWSVEMsJehNjAXU8f2AwYFYvHwHU9DcTjx2hNOzHr6QFS5Ui0PKmr8Gqn8bMhsGBjhtH4Yn7gCZzRBSoFlDdyyHkKjKVf9w4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یوزهای «نیکی» و «نیکان» شناسنامه‌دار شدند
🔹
تابلوی نام‌گذاری و شناسنامه ۲ یوزپلنگ آسیایی به‌نام‌های نیکی و نیکان رونمایی شد.
🔹
این ۲ یوز خواهر و برادر، متولد سال ۱۴۰۲ هستند و برخی اخبار منتشرشده درباره تولد آن‌ها در سال ۱۴۰۴ نادرست است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/441882" target="_blank">📅 22:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441881">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed2e032c1.mp4?token=IOTlYmDV9OxMNOaSmHLG6w6wjDcCR3mZcVsA2VYzn-4cVzn00FN4HVY5IGuhg9tTbRL2OqG4ZAnA1wkbn5zSRcD7NwCXqojBYFL1orSB7TFMM7CiZ0YT-GrlzlJF1BvhF4IpNf5n-Y9YNY9e1U0nYtSuWiuH-oYEAHA2MrD475Ww_3IDz8ffviQcAAj_3VE2h-oPJsDOaq0jlVPIbwUWYtWAqdnrbaJesucU4OSvJ3K9GsKd3pwych93DWChVbtt3cu-5bbxN9SnVn1dd8iST5hqGXDLWNTuJwfwX157Q2r7cifGAC7tCRXCKu4oalEGovGNVOibL2Y_Cr9sO0jMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed2e032c1.mp4?token=IOTlYmDV9OxMNOaSmHLG6w6wjDcCR3mZcVsA2VYzn-4cVzn00FN4HVY5IGuhg9tTbRL2OqG4ZAnA1wkbn5zSRcD7NwCXqojBYFL1orSB7TFMM7CiZ0YT-GrlzlJF1BvhF4IpNf5n-Y9YNY9e1U0nYtSuWiuH-oYEAHA2MrD475Ww_3IDz8ffviQcAAj_3VE2h-oPJsDOaq0jlVPIbwUWYtWAqdnrbaJesucU4OSvJ3K9GsKd3pwych93DWChVbtt3cu-5bbxN9SnVn1dd8iST5hqGXDLWNTuJwfwX157Q2r7cifGAC7tCRXCKu4oalEGovGNVOibL2Y_Cr9sO0jMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله برای نخستین‌بار پهپاد «هرون ۱» صهیونیست‌ها را به زیر کشید
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/441881" target="_blank">📅 22:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441880">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124b0c8a54.mp4?token=pB9FRC0hF4wP0pKhvAzh_lEGVgm3o1Z6CpDeF_ZnaRM_rCRwHWluTiLln0jP6cUgMyCQxZkrgHvWN94ekjYvE93M_zJrRBYWLX-SekLf_CXfuV46xIEqYrLHZulGr3UB9eAUzrwwa9J5Ny5vu0rAH2N40pstZO45-ANw7OgWKdN2UMn_ZXEAaa0QulFBubqHd19F9GTkpdzfdN4zDLDjhwmKsyzN4Tq78W_sOzPwmrlFMTcttCV4LJgyaLv1jJeroo3QCEXUgy2gfEw18jJpG15g4vW49aOEG5Ytnkw7Dc8nCudCMflReK0n_68hxJ4vgYfJ0Pyg_QvBbwHq45rh4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124b0c8a54.mp4?token=pB9FRC0hF4wP0pKhvAzh_lEGVgm3o1Z6CpDeF_ZnaRM_rCRwHWluTiLln0jP6cUgMyCQxZkrgHvWN94ekjYvE93M_zJrRBYWLX-SekLf_CXfuV46xIEqYrLHZulGr3UB9eAUzrwwa9J5Ny5vu0rAH2N40pstZO45-ANw7OgWKdN2UMn_ZXEAaa0QulFBubqHd19F9GTkpdzfdN4zDLDjhwmKsyzN4Tq78W_sOzPwmrlFMTcttCV4LJgyaLv1jJeroo3QCEXUgy2gfEw18jJpG15g4vW49aOEG5Ytnkw7Dc8nCudCMflReK0n_68hxJ4vgYfJ0Pyg_QvBbwHq45rh4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع بارانی امشب مردم بجنورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/441880" target="_blank">📅 22:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441879">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f3637faf.mp4?token=nNwGWi7w20MsbQIf00vf-XMm1T4MA8q_FdQZuqe4HsdPErM8g4gKFN-3DptQDwnd22rEemIJCPLmIRBAxoB7KqakgG44K8xLzLuZIdqoSHxxZ27sPxN4OJVRkVdCCuo-OLZiIS3gU30xpZOky6LZlraeZyeRHZrmp8KYRWkOOUlEZxhE0nh1zF1wc2bx4CigRCVJ7LLFDXV8Df-XwUvB2ShJBszFpOWxs2CYj3Zvz3-Di5GjJpp5vd2tmUU4IopUlOC2_lLTUUTQ0F4rNLLz7z8RQuWGsPk2ZiLXYcs8XtI1kM__JpKJkyRjyP2yhaU0Sz38U-sGBjTIxgBNE92Y2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f3637faf.mp4?token=nNwGWi7w20MsbQIf00vf-XMm1T4MA8q_FdQZuqe4HsdPErM8g4gKFN-3DptQDwnd22rEemIJCPLmIRBAxoB7KqakgG44K8xLzLuZIdqoSHxxZ27sPxN4OJVRkVdCCuo-OLZiIS3gU30xpZOky6LZlraeZyeRHZrmp8KYRWkOOUlEZxhE0nh1zF1wc2bx4CigRCVJ7LLFDXV8Df-XwUvB2ShJBszFpOWxs2CYj3Zvz3-Di5GjJpp5vd2tmUU4IopUlOC2_lLTUUTQ0F4rNLLz7z8RQuWGsPk2ZiLXYcs8XtI1kM__JpKJkyRjyP2yhaU0Sz38U-sGBjTIxgBNE92Y2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از دزدی‌های جام جهانی چه می‌دانید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/441879" target="_blank">📅 22:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441872">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5F-fJGaOKQJFFzpSqLy4ecKZCw9OrRUaJiKGXj4nP4eUMq3owQjmyBh7fgkcpbGNrOqBE-ITefKJGQkq_AE2qmlVIR_XkycZ3F7q1yCMMvv9RTGdqtkEkreMsxMgvMtgNvdM4cPVpzBmP1KF1tD0ssvhc0P6lUgsiS1EXsayzqNSwhB_yhCBcfVnRA8SGFMGAqV79eI9niZf997abTbJpP9OqJK2gwxhwmVE6tAaArJtDOlvqYu09Y78Rfx1BWQ-AB4m7SuJMMLS0RM3xc962ufwBxfsLinqpMhtv-XxLmLo_5MtKKotTz7D3jCOk91wtlmHPkrfugKfXLsyTxpMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jG_rcJEYEHoxfaf1nZkjenE6WJm_k6aITneuEp2Pnl0Ht1Z9CPQkI3JklBe1p08d0OjU3bo9N7JgE2-I-B4k_RaCZYXjYMSBWFh-gCXueT5UhtGDfCnjsXHKM0GnfOJOEQshqqETo5arFs8387fum7y9qPjnp4Pd7x87SnzoZjAC9l_8CWH69EU6dTPQAhsmIiAl3NiGJQ6AkNMpHy0sck8ShgHzVkFp4-lahGqcNWyV7Mu0CAdSiaZoDwZto_6gHRPbTNoxcJ8HKSYgKmXnynqqW_PInzsUh0E2HHCZhNwnrNG3gEeXgpRgrpSqKIrIs_bp9W-GJET4iBENeTlrdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJ6ZInr8ll4zhVj4umkpkKqtbKS1sft6rq-cbakpxQ-WXBPJiRpa_BbG-vZWJ5vmFAmjR39w7GCOtdz4bBKKVdQ2SXBirt-vJro60TZ4zgo41Y66jXEMuQue0eBGwgECgSr6iplBJcfu3YhkFFE74Xk72zTOZnr7lgZXCrbRgyyyN9jh_JckqgDd7Fmm1TQ5rtOqYlYI5hPxMWFv2MZSeH_Qj8xS-3bV5nimcpMt15ZCpkIFlQPOFDVrnfeVLD0yWRnU_lpQm5klIGP9ZFeGDiMaDGFcZGMsxdnJTcWCFEVaNtGsKqtNrhfrH12gYV1EmCDHnN-xaHi6eYjCI5BgNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZdhz_9vaa5chQo0iIXYO02KZ-AzGie4by12H3xoGvqpamf9TyVwJOChcPZcn4hT3R4dVVN6O9D_fkeke-pn61qNem6P3pu6hi05z-xy-q6cY-6cuUZDenNOHPxDj7TIaKMxqqXtcbTWltZtmf_OdIbw6vplVme7hC3mIhi0iw_e6Z1TAeTadQJraBCQTBkfpUpkld8tp2IX_keORwDf8KtpaQWDSYb8eoH6ShVDbyjyQB-QN7QLXL6hnFAzjwYxtfoo9o8fGsrHCkXDSrkglFCjt4Tst46J2411FT3mYxEL4KKcleL4SxM6HUsrvWigAtNdIsiaTA5TaXBAbKuqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qtqi-p4CkvI6c47iU5BF_YjHJqJiBaTirsQSgnz598vEf846Lpi445-n_4rtTVllbBsQnmgsxl4odK5jTh_FNP12Ng_q1wmjz8GwoBYzWRgXdXY63BQHfrgIFEptj0jkJ32xsqIiLBkLNbuW7I7sPusb2a9z_UMoN9XBKsb00Uq_LN1sRM8NTCmaGiPTmwke6SENOzKkuG01pc5Pf3sx2b3saDOK-_ONsALpR4RVrEtmWBtvVHPbe80LpBVFoxHUhcwrWPbh7uE2GVkfmBqfBl0Jc3XdiB8fYMp4b0Rz-wQCjYjHIHcCbeu1GLBvlXTdGwQpGU3UOs80Ujdx9ewINw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIO1-XVFikgS37DnCwiQ6fVFtexLaY4Cjhm6ddjjiayW-3xChnxutcPL53Y0on3O35s05xFWiGl6qbYylSuYA-M8XNA2TYYMZyOqBi5bFiuBCUKO-D76Egx9CcQ69i-oNWnvaxLDx_TB5ZoiMZxhzUImFhF9aKkP0pwqX0yYo9f56V1ZEzw3h5JwDO69u2N5MTVFKkVDSfZSq4tcDyt1b2t_E4Fqn-kXaPnz96JUB8CXi4KEcWprvEe8K-h7uf-UNhINboUD_3jkeLOsyxsGgAPfvDTbkL-PCJ4KefSyYnQbQVwIQNvy8KEEDQ9H1swrhJr4xKR7Zy2Boe8JCYyTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UsbXjkmw1mngXpy-QTq0yhw8GCnIe1gGGTVTysTYetbUwEqGEGL2k1exrUbhUD3OfFR98N84I1VJfiePcEMWSXH7sac69ikuAh0A3RBjJsONA7MOU3l1IzeaJoBpylQ8fQzHT0MN3aWjoG5VB6hMKKP3Q_GuOr2kv1XMHeCVt8N1wSf2Ve9pch4nZA3IVqlJj2AV5PzM6SatrDwR2cJlz_v4wIE3x8iTCBGm8pvYcnDIlO5Amdvi39pjb-iAhXiaAan0NpZHcnZ9-Y8BY5jwzbm68JzaQ_XqvqSONSm3EGjUyks4n4Oh_2dTVHtygcvUpbZ0xt0iMvl6Ai96qRaDqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
افتتاح قطعه نخست آزادراه شهید شوشتری تهران
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/441872" target="_blank">📅 21:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441871">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌  حملهٔ حزب‌الله به یک مقر ارتش اسرائیل در جنوب لبنان
🔹
حزب‌الله: یک مقر فرماندهی ارتش اسرائیل در اطراف قلعهٔ الشقیف مورد اصابت پهپادهای انتحاری قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/441871" target="_blank">📅 21:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441870">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWyTsqweCXzLCdJzWFJkpJR8Gk5h9Rv_qSEIRRQluLpaUOcMmrWOets-U-wGe6OAYMZ4O1_GlImhFD0yxmDyrmyU1Wz2oH-6072QIIoaS-b7bV7B2cFK9k89U1Ek1RlDMefJEvhPrW3w6i4PotjSCnwB3aoS1vHtKK0ldSLxxmzfTbwO4IZZKOtuTrWTCCrP2GzDcNL_XEn1rHE9TapAr1Caa6EA3q-5le5ZbDw_kBLg--RuzOVKAx_V-hxCEzaD9sTvMK8EujkdH-U8292T9WNKNvccNzGkEVFghNF9w4wqbIuizS5wnmLLWzTVY93Np153bw0Ep-EG2508o2Lttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نظر شما درباره امضای تفاهم‌نامه با آمریکا در شرایط کنونی چیست؟
نظر خود را
اینجا
ثبت کنید
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/441870" target="_blank">📅 21:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441864">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎥
دبیر شورای هماهنگی بانک‌های دولتی: رفع اختلال از خدمات بانک‌های ملی، صادرات، تجارت و توسعه صادرات در دست انجام است.  @Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/441864" target="_blank">📅 21:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441863">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58b11fec2.mp4?token=MWbgXp7-hOQVCqNQFWItIpqCie5ryainODK7uxcdfR1JJXG0zB-zeZ5QaId1NG6dvx3nk4p1Ikz8psjI7ClHuseBdygRr2_6V473es-A-WOacQ3tX_6Rx9YXZrnexttCWK8NuqOm0I026raJpQRQiGbHFdEk4NS3VSPJY83M-hEDRAI3-v5sYQmsp30iRNSba_oZHI02vYKqHS9mBAqF1LnLyHM4rgc_Xg3_G_Sk4EmbYAnN62FG5d6pEhXB81z3JQBVNv-xrnxkeXq6wiJHyJhfbO4nTRAhtnWh-kKPribd9PSyGzllPl6GM7Z7FkaDFQB_1pkOBUeu_Iy-ERJVsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58b11fec2.mp4?token=MWbgXp7-hOQVCqNQFWItIpqCie5ryainODK7uxcdfR1JJXG0zB-zeZ5QaId1NG6dvx3nk4p1Ikz8psjI7ClHuseBdygRr2_6V473es-A-WOacQ3tX_6Rx9YXZrnexttCWK8NuqOm0I026raJpQRQiGbHFdEk4NS3VSPJY83M-hEDRAI3-v5sYQmsp30iRNSba_oZHI02vYKqHS9mBAqF1LnLyHM4rgc_Xg3_G_Sk4EmbYAnN62FG5d6pEhXB81z3JQBVNv-xrnxkeXq6wiJHyJhfbO4nTRAhtnWh-kKPribd9PSyGzllPl6GM7Z7FkaDFQB_1pkOBUeu_Iy-ERJVsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هواییِ تجمع مردم پاکستان در بزرگداشت رهبر شهید انقلاب در لاهور
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/441863" target="_blank">📅 21:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441862">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎥
روایت سخنگوی عملیات وعده صادق ۳ از جنگ تحمیلی ۱۲ روزه
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/441862" target="_blank">📅 21:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441861">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1615fbbd2d.mp4?token=KMZAyzCaVt-clNOOeV6pI8az8C76-SZCl1Q5pXIYpeK3Aki3dGKTAri3UyslGYEazFLy39xiN2_nt29cb90UHoeIHjMHcbyKQC6Nb4Jr5-7k0guM3Nj-Y7ujSLybdyFpssem9Ft9S8s0GnSW-kJsUnfNQVXMHf_GISuDubpF3tsrZWztZF3gXp-hNmg036lCZmMkUi9-tfRPvcnRVpgZxTcxnDf2ljnsQNDPz7SQdO8shr9UQg_IrzmSM8g2nQOBU5swbtBStcAarTaaK8-nh-FUUVa16yOtp3VYWZ5J-5dzZGLGhlQUD5BPJA6vITc1O5dK33M3mL7vp16u-Xbm4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1615fbbd2d.mp4?token=KMZAyzCaVt-clNOOeV6pI8az8C76-SZCl1Q5pXIYpeK3Aki3dGKTAri3UyslGYEazFLy39xiN2_nt29cb90UHoeIHjMHcbyKQC6Nb4Jr5-7k0guM3Nj-Y7ujSLybdyFpssem9Ft9S8s0GnSW-kJsUnfNQVXMHf_GISuDubpF3tsrZWztZF3gXp-hNmg036lCZmMkUi9-tfRPvcnRVpgZxTcxnDf2ljnsQNDPz7SQdO8shr9UQg_IrzmSM8g2nQOBU5swbtBStcAarTaaK8-nh-FUUVa16yOtp3VYWZ5J-5dzZGLGhlQUD5BPJA6vITc1O5dK33M3mL7vp16u-Xbm4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نفت: انتقال سهمیه از کارت سوخت به کارت بانکی طی ماه‌های آتی اجرایی خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/441861" target="_blank">📅 21:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441860">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29aa54312b.mp4?token=WeulA38THHbDyynjdwXokOSgj0BrG_tcp1ka8JIISo5EC2gqi8XWK920j0gUF1sf6tozjd9FO11lF8HFFnZVFclg3dpz83Z2HUkbilDec4SWczSqKy9oALsxZAZ49SUpWMwtWWMWvnnqSo5Q8JvBMUGcfxXPJ-fLbV5YrISZwf_UNdDeakV0VHGarFR8XtIWauIQ-eg6iBpxs9do04YkOG8wbIomn56AFoH5p8Fs8_bus7LwonZYZleHFzr7-9ZvgWvRvxDmzuPLK9U8xEHbaaUG7ULIGs3mJXNqgL4PMxbbmvBGGThNuycxmELgV8SD-fqKiqWBSeQUx_MDw2_bSKsZC57XP--rgsoGvG2VSjnDIt8ipLyznMdmSVguib8VkKuuuhrTgzPCVymqgCWo1RENWpDKKFsJDc3bz-y_0G8_ednqQaw2wToTAu5CC1wEQAiHc1kHivKFqB16acOvcsxYd9sYsWrwcEt97pkt4Qe9qbRJEtpAtwth9b7IpzAXrlh3XHulGvGuAnBSIQwQUXUwi8rig4IheKgXN5S6-4YYiiix9pSgR1rHiV_ZzKAOyRxve1w-8BSWfHwHzIXH64Yz2b74JCJYypFN1ok8dMKwfQfnwyzy4y5l1cEhxdyLEad1yJe3RioJvhJ4II8UOA7sXzpis9wuOBjE6RntyZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29aa54312b.mp4?token=WeulA38THHbDyynjdwXokOSgj0BrG_tcp1ka8JIISo5EC2gqi8XWK920j0gUF1sf6tozjd9FO11lF8HFFnZVFclg3dpz83Z2HUkbilDec4SWczSqKy9oALsxZAZ49SUpWMwtWWMWvnnqSo5Q8JvBMUGcfxXPJ-fLbV5YrISZwf_UNdDeakV0VHGarFR8XtIWauIQ-eg6iBpxs9do04YkOG8wbIomn56AFoH5p8Fs8_bus7LwonZYZleHFzr7-9ZvgWvRvxDmzuPLK9U8xEHbaaUG7ULIGs3mJXNqgL4PMxbbmvBGGThNuycxmELgV8SD-fqKiqWBSeQUx_MDw2_bSKsZC57XP--rgsoGvG2VSjnDIt8ipLyznMdmSVguib8VkKuuuhrTgzPCVymqgCWo1RENWpDKKFsJDc3bz-y_0G8_ednqQaw2wToTAu5CC1wEQAiHc1kHivKFqB16acOvcsxYd9sYsWrwcEt97pkt4Qe9qbRJEtpAtwth9b7IpzAXrlh3XHulGvGuAnBSIQwQUXUwi8rig4IheKgXN5S6-4YYiiix9pSgR1rHiV_ZzKAOyRxve1w-8BSWfHwHzIXH64Yz2b74JCJYypFN1ok8dMKwfQfnwyzy4y5l1cEhxdyLEad1yJe3RioJvhJ4II8UOA7sXzpis9wuOBjE6RntyZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مروری بر ۱۲ روز ایستادگی برای دفاع از کیان کشور
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/441860" target="_blank">📅 20:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441859">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcsU0jRhES4mONt4nJjmyX-JP5vCotrF92GCcr5UVeaEQFZSk9vpoO5RZfCm5bB9wt9S4OgOFGJ3NkvkAklsXVpte0njGX4JdqiHztB5ZPV4LyOgXAPpcc3XTRnMabQEn35Sf2YdTntLnP3raceHs6bVyhBJRfaoQmKVAEzM69diWav90HTvL4_62HHlPZIBKFCFsLsgJJdrmZUxKUe_RtLh3K_gPAkq3cuToSwTsIhCGxMFYVVVr5RADAPzvS3tV7TV16oJDCqGTPlvmxy-en4v19_cbyGMt_xsF-3poLpYTmEZ5cv0HvAOpqkYqcDduHv9PMnp3gwTpRnz8VqK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش غول‌پیکر ایرانی محاصره را شکست
🔹
طبق ادعای تانکرترکرز یک نفتکش غول‌پیکر منتسب به ایران با عبور از خط محاصره وارد دریای عمان شده است.
🔹
بر این اساس حدود ۲ میلیون بشکه به ظرفیت ذخیره‌سازی نفت ایران اضافه خواهد شد.
🔸
کارشناسان از ابتدای اعمال محاصره تاکید کرده‌اند که محاصره آمریکا باید با اقدام نظامی بشکند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441859" target="_blank">📅 20:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441858">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUOes2maMarWJJl0YIP32GMS_J1r1quxeNM6pOMNHcQoM4sy3dlkkiraoelFM6TZ746i4gz5tXygS-JMs5tTtXpFdumDGvTPW8adGk_o7YLADPPnbN-qdRtuBjU1fS7PBnVjNPHioPCqxE_SSKRNv1TreQm7vuiVn9wW6n-fBAd4j7Ku02VS-xhwdTjgTB8FshXu4YrAKcv_d1XjIIMn5aCMwjqRJDL2TQENqxiGnW_wMVuNfdP5beOF1klTPCkbaPDznlpvaCyUkx9oL94gV1XLPtqrqR15G_Hc_nTNSxcFFJYYcq_bHFtpadxLjXKC2hiPwKdSKtrJMMbLIn_bVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
در بازدید سرپرست بانک صادرات ایران از شرکت پارس‌خودرو رقم خورد
✅
آغاز پروژه چند وجهی نوسازی صنایع با مشارکت بانک صادرات ایران/ تاکید قربان اسکندری بر تولید خودروهای باکیفیت و منطبق بر استانداردهای روز جهانی
🔹
بانک صادرات ایران همزمان با آغاز پروژه گسترده نوسازی و بهسازی صنایع، تامین مالی هدفمند و کارآمد صنعت خودروسازی را با تمرکز بر توسعه خطوط تولید خودروهای باکیفیت، در چارچوب‌های نوین سرعت بخشید.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/441858" target="_blank">📅 20:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441857">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4b-ajHui-5xw9iRVpsOEmUy7aYyjWfrpRbksscdZEYzx-J8DDSzdybpD4lEjB1fTE4oZZzp65I_PBZgHxMic-uLVure0hXX8NDSv4-0RW0eTTxcF7vyNAsVrEZxAH9WY9WEh_-FLXqeJCrdjC1Q5r1DsOvJwpvkNpCxlznvtMVfmRVOLkxcB-_OzXIgRW_y6EyTZtfryOLxuev0ukaq9BvNt_RCPS87GtEUGjKpoR1ExA9lycdycKxtx-OHe072BTO6l3EwZs0TnWBqjp1UkFzP9BkvXimtr12wDXafLgqtSzXjA-5YBXbmAzhIIoPeWIMpHF5o3H1p-LESMO9PMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوایز میلیاردی با پیش‌بینی مسابقات جام جهانی ۲۰۲۶
✔️
«کآپ شهر» تلاشی برای پیوند بزرگ‌ترین رویداد فوتبالی جهان با خدمات بانکداری روزمره
🔴
بانک شهر از راه اندازی کمپین «کآپ شهر» با همکاری شرکت آسان پرداخت پرشین (آپ) همزمان با برگزاری مسابقات جام جهانی فوتبال ۲۰۲۶ خبر داد.
🔵
همزمان با برگزاری مسابقات جام جهانی فوتبال و با همکاری بانک شهر و شرکت آسان پرداخت پرشین (آپ) کمپین «کآپ شهر» برگزار می شود. شرکت‌کنندگان در این کمپین شانس دریافت جوایز میلیاردی، کش‌بک‌های نقدی و هزاران جایزه ارزشمند دیگر را خواهند داشت.
مشروح خبر را
اینجا
بخوانید.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441857" target="_blank">📅 20:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441856">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441856" target="_blank">📅 20:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441848">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6FBsdUlcZkOvCnUDegwrHwqAo3pBGRvwm3IloLldmRTbhimz_yfEEbOAP6FDnzp28wFBoOOdPP5zwdpa7r1HwD-iJY-C7LpbODAVseFCSUgoYZg2WCPFCks97XhPwOFIIhmc8SXMJ0Qe4mKNUqJbjk0M1Pc4yyxjWASeIL6rI0S7ZY8jHTSdhcAFRzhe_oM7eSy_CaxewsF39_CPeLzk_t8CZKPZEpRZCDUeRS45Ct70W382-uKQ2lmdCN3Op48Fz19Uu46o4Gl-CNiZqW3ZaHdXrULSHi2ke8bWBFPeoeUyZrKICXBS4ZLRDtY6965t52qdZzW6dn5EBroJAselA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUk7ngP4tve1J6_XtXw-0mjg_drcWKh1h-lp8_PT_FMJZlkuqmOsBMmKINNPQUjqnT1bDHXMxtgUU6D70Zprvzi-7lyOmRgmB_M4nLjZG0JBaX-mVoVmw3hK-KfXfNpdJCYMfaPwWnYaUqOHIuyiGbTVyL0WdNxsDlyCVn0bG5fRciv5j150X3R6gboQkinRlF7TH7LEbmvcs5F3JeULFUIVOK9PWQiGgunVai_o_96UgbF989T_81yEnxr_wENMxvFpbOXj8pTPxwXk3jpEdSN9WZP-jKrnn-zWVeLh3Ou8R9rWKFqVhuHeJHIL8yUkpSSgYUhKpLx9m1_hHq1OdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ajgI-8eMtZMDsST1-jihprhxPQJBKwNPBjU1_ist3hGzUjSmdkyeCVFSJW9bBxIlrxJ9lh7zntPjeKBs0woRsSSLKkVh2wCR9q4uRsS_xGBVQ9SlBJkA-bSDFwJG6qdN5d5sBBhFV0uoBqzliRD8mAWf6dpzKUS2CLLRGEP3LSDn9j1Gdl-UWk7vyTjXaBHlb5yK03Tp72R8P1PwMyUZMNzFjs6RoBa11_CvLozhedbPcamKmiNdWbUlAbIzry-NxmeAj6lIRcP-8KQ3LRLkAKhs5UCw9h8JCkORGSAYGQDOVAptF1rpGeQehsPr-lLMlgY-efYMYJxjgAxK6byMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHmrthKLuA7w8v9O3UunWafv3pVid4KzobuQ1nbFgr3Fqf3ee8_fOg9YSOKxuBrgy0-4fcHv2C3JEFMVA5enFmnS3bJvhjsW_PsWxK1-KiqqjTmZgMx6tv-5z19ekkWPS6VtmPBUDLH7iWUPUuvzynsuu4WKzs_yR4V5ATTCpCEmT3z78ApF3ucyb1yJF1R1zeC-SpMCN6alsa9i8XV4YB_SfE_5XRuKL7FV9xHx9kwsZhNAEOTHXA7BfdGdwFIRc6ZMnA-GLLrWreqlY6fvQR35P2r2RRJb_9ctFZECPr-6ayKELz8MHnaekX2sUAhMr9wz0EyF6CXuUWNyss8vvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnRu8rmi7xhWUxkJY7lRrFCbwnNkINYORPLrPCBfeTH2_Y-PhtItK_9rRwzN1FhpSONgZoUJkvAC0Ipq25kjAFOpHm6F4cGdp12HrOTLzCXs-mMui0RonFrMAXbTx0y6th3nEiG2f-QmGte5JGTa2KBkTyVD2CKl3ySULUAjwAzbFX78sjtY0jzqIDQU9eo-k0uQSkhNecn1UP26qWM_YVMAKXmcEyV4lEgRNY8GUOjlPW0yNTgN1-Bancu4nlkIsO41TmzoJXvH94-rVkJOvOAqJrczq624szTNJ8r4GryTk5GefcrO3jjvwJ6KfoZOpCE87SRddnkFj1bJK_w00Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سفر سخنگوی وزارت خارجه به همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/441848" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441847">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ: قرار است فردا یکشنبه توافق با ایران امضا شود
🔹
پس از امضای توافق،‌ تنگه هرمز برای همه باز خواهد شد.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/441847" target="_blank">📅 20:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441846">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ: قرار است فردا یکشنبه توافق با ایران امضا شود
🔹
پس از امضای توافق،‌ تنگه هرمز برای همه باز خواهد شد.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/441846" target="_blank">📅 20:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441845">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWpML9A3mXC27Jp3T45jvPhJx5QckY16p_cm5_C_REp8x5n3RJFY88F5-KR2c-Ft8xt3MN1sD-DN9iVXbMukQw5GUKirYKK3bGqEykOoYu-cvMSPruSWHKAH_4ReH2maO3Uafco920j0D3fU8dbDLLgCwf9Aq6T2hFqN0bEpZ97FK_7t2GcNKXSF96LIEOlXS0O5ktVV2mp5oU_FZyS0yCoqzld3ytw4lXy6BooX-iZlgD0zNOEz8SoICGebrIOvF-wWPngJGCFQcVTkTX2WQWjmEDpbGEK-qrWpRcUlJRDPtUGtECRQq-XeoHK3Nd4xo0FT3E3C2Fl01j_mfk1Fmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: قرار است فردا یکشنبه توافق با ایران امضا شود
🔹
پس از امضای توافق،‌ تنگه هرمز برای همه باز خواهد شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441845" target="_blank">📅 20:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441844">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نظامیان و خودروهای ارتش رژیم صهیونی هدف حملات حزب‌الله شدند
🔹
حزب‌الله: تجمع‌های وسایل نقلیه و سربازان ارتش دشمن اسرائیلی را در موقعیت بلاط مستحدث و شهر مجدل زون با حملات موشکی و پهپادی هدف قرار دادیم.
🔹
همچنین ۳ خودرو و بولدزر نظامی در جنوب لبنان هدف پهپادهای…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/441844" target="_blank">📅 20:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441843">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-Rp6m0vaPuuKBiIg_BLv9X1Tqp7SZnyZbAaIS01CvoXWykMcrBprG8320e4nqvxPPszmOUZ9vx3TTXO3UWY2RpRk4QVzw4Y_62iLFWBrX1GCICbovMqjqgvFhslGKwSNlPI9YSuiu1OotRZT7d4b3dlhjuG0f2f5r6tei_9hJksiJRiA0iBECex_LFOjePWrRyylmLaoEhAk4vaiNQPeDgs5Cj1LF3dUO5ZygZyVngCOmL1Uuvyq-oXxGMrhHTFpYrkVxH_Fwa3cZQ50y-il8dPEnu-h4wX0dB8x9JDn5OB4opzQ3S7ImSBkRtNtpgu9su-EksIbFN7FhR7rgTfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: جنگ تحمیلی ۱۲ روزه، بار دیگر اثبات کرد که فراتر از هر سلیقه و دیدگاهی، وقتی پای ایران عزیز در میان باشد، ما یک ملت، یک مشت گره‌کرده و یک قلب تپنده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441843" target="_blank">📅 20:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441842">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">احتمال تغییر زمان امتحانات نهایی وجود دارد؟
🔹
رئیس روابط‌عمومی وزارت آموزش‌وپرورش اعلام کرد به‌دلیل همزمانی برخی امتحانات نهایی با مراسم تشییع پیکر رهبر شهید در تهران، قم و مشهد، احتمال تغییر زمان برگزاری آزمون‌ها درحال بررسی است.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/441842" target="_blank">📅 19:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441841">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyS9pbKHTBNJlo_KzaSUH8oZFCleSlEDrmr7jfzHAuMKz18yAZXILQkZljo3646O_10BmUcQLYmoLwZTgKNmccipOl9abjAHUFGQn72g2qLz4PQdEnRQgObFludOflK5bYYoY50k51mVd8SL0YRxlGsc4-vywY1BtsrnRV6hu-JXFFaq4SciyN8WAP5lxtw56MS_GT__HzglYjMF7Js_vlWcvGNnXqlcEF0wlliNGN8ctFlfiOK01k9TaC568yeDYb3BPfpNaQCO7tH4Gn6vptO0RwAyue6OObrUgjpa79ZIq9cj8thCpgchkLNFbxf4mDkwvYRjgcgHhe1RD8ZyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهدای نامۀ سردار موسوی و انگشتر یادبود به فرزند شهید سید مصطفی میرغفاری
🔹
همزمان با نخستین سالگرد شهادت شهید سید مصطفی میرغفاری، مراسمی با حضور خانواده‌های شهدا و اقشار مختلف مردم در مسجد جامع مشکن‌دشت برگزار شد.
🔹
در این مراسم، نامه‌ای از سوی سید مجید موسوی خطاب به فرزند شهید سید مصطفی میرغفاری قرائت و به وی اهدا شد.
🔹
شهید سید مصطفی میرغفاری از شهدای جنگ تحمیلی ۱۲ روزه آمریکا علیه جمهوری اسلامی ایران بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441841" target="_blank">📅 19:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441840">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎥
صدها کشتی منتظر مجوز ایران برای عبور از تنگهٔ هرمز هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/441840" target="_blank">📅 19:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441835">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUSgQWGH_ukZf6yA9Y8uJhOr5TYn7IcXsmpSK3xnzsVrCbTJh4k1k_-pJ6D1ytMPGFANVaXwnOWZsd-REczwUkjQHNjZNxtk5XY1q0Ic8MhPde_hA4bw03kRr_Ov8K86FvNZDbSCpoliSmk8dolxubsoR2JsFzCCfMZU771QRmYsnmYGcIi_Az6gzTKb2hKHxGRcEnRqf922YRgz7FqxfAeRFSAnf022Pdtd8AYuBLe95Fc0xl3Z-9H1wBj9TOeYa9SnA2sFhjHw16Ci9028gZ2C1Ea0UxzGqgyU-TVDjq-NLZxdjgDZvS8vWEy2S9YD2xkmUL-nDURYS--9NkeYfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0Cx934UK2kuQjmj2QwCC0tbpthgxMlwuDL3LbMuin-3umD_ZNIzOU1VFZn0yfKWX1vZnUa8WSjfkHe_SjGx1W8nH9UEQ1RUS43sipiuC_Nm9Sdgcs5jK--AqSA3Q-8dt09EUjzKW84ERnN20Bc2tGEpVeHgVT-zg6gPLnknb4CacZpwwv79UkS5ZVJRdy5o8-YRjqcXT2cjgHX6JQQ9rODyLjVLyv0PD8xEk30E478OJEerRcRX64mdyr_e6JtmZ6_PG0QB6-rcAWMuBG_Wm7f6nFxtyLfrzG4PICvGTzewxHfJSvAc9TNAjW5ohN7SkRxdGkmEg7lz6m__z8vWhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0yNAffNZZMsbB2BJ1ma9j7y9pzpgbSsDHvhS8lM2zSCTggieoJZHnu214JEjUhK4DFe3pnzCRArPxIobWze1Hf49vuliPrOsyJ5IK_l_JbUQzgXeXnSTSj9y_qef4X9knrRz3lFNCwmX1uLl_hV0Hu-xmeQnxUtKnvGR_T7i_cnhhohMjj268-BtL9XsLyrPN9MgHRuT8IcIUVxsTLEi7UBP4ZnHH4RUnBX9J-OwbVK-AZlgLS0-r1c2u3ZllrxMSCdpHmJTIoRHFu42YIeGtTLRf0obZB_756LiAxZUZNNm9QCOXmB5-8dAajkZ_m5Tw4cG38MTX4wi8-6wf9Rqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d02BT6B-AkawD0Aq9Id1t7Wq_lD1tJtMOBEW0qF_NK8xqsKTLZHZewYE1tfFJIYrT5K3OayF6s6SdmuomaJhOOa49R8pivoUBwZ6-mIY3K9elbViusPwzIcIGWwqCA3RTLLk1cYHrDkLo5p-WRatI6rbwIjiNzybbIEe9dHrj6RSfhZXuqGCJeWiIi9P1qVIQF_cL7l8ezGbrFb_NlQiBQfnSxk0GW7vdRIxXb4k-NpbcBN09Zl6Q_y_T1XkGo7eOwQJzeKY_IrhSdRYCA7GOogfHA46TvnQ4xXasyWsLEc6HlrEaJB5K6K9te-bMSjl6ywL45zmdhJSYW9eGC7Aag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmZNXeok1ClFVO5ZkZKblwZApxDPdShWDQLZ9BPLX3-NNhk2LBTcgFZrTaMmYNmRKsZGaLpYJ3Gr0X_4UdfIfJZqyk0964zGdWMPluqYP_8D0NlyqdExgRR-RRVhxi8qghwxJyTHmtlTDUdPQHdvNsV1K0CLSsckYGq_KNJp50CsSQyNCMKlNUhhXWU08M8yF9LwZfv351vsyzhRk8fi2Fxz4CudGpASMSgGvM5sslZtX-NfdyAThXM0fbn_pMWXAc7EER_ArWKRa1uOs6aFUtKLY_l1upVDJGzonIBGC_FufdahqTajoA5O9WuybxT2X6WP5_ppPu0Hshi7gi3SqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصادف زنجیره‌ای ۱۲ خودرو در خیابان اشرفی اصفهانی تهران ۳ مصدوم برجا گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/441835" target="_blank">📅 19:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441834">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0Gm4IsJ7UYzG2mEoqQYlBh74G4vsAsLsO175a9Hy6Hg0xS0gZHErEQ1uNgBrQZiRsjyK1yr6tfDY5Fq4MCvUnI-OjY386jZlHgeCT2-j6UHnX47mNUhZcvEiNkNHkBEqiObEVex1BdcSNeE-EOColDi14AJ9wT-ViMqifjUFph4LPiZaJJDn6HGSaCqMtuXiRlI32JRAAyqdgZ1qYD4Bbpw7FZc-hW5mg8_M4LA7hwgNfvD0mRuoYMJ0rXXXp8YM_z5VX-eNGMzKcZqDyqj71QbfBNBKFMHykkCytBkAU5t3ftBZvCVlt8JkEJzgqjgw3dOH4hzLZfBISVTbLlIBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۲۱ کیلو مخدر شیشه در بندر چابهار
🔹
فرمانده مرزبانی سيستان‌وبلوچستان: ۱۲۱ کیلو مخدر شیشه در بندر چابهار کشف شد؛ همچمین فرد قاچاقچی دستگیر و یک خودرو توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441834" target="_blank">📅 19:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441833">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎥
کارشناسان عرب: ایرانی‌ها موفق شدند با صبر و استقامت خود معادلات منطقه را تغییر دهند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/441833" target="_blank">📅 19:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441826">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GfAER47lkYZSwE_Q2V29AwQPsfTYlxA9cYygzQqGYKcEp3qSVY5m3aYImErGxt6IuEbeqG67TiBiiUhtfF7XKCK8t52dTHggApxb1JxooaavGQELpTj5G2FWa7_QhVTYrBb5S2XB1_4UgVQNXtLD4oizqYSyXly7fM4XtFLds4nT-GL_VuQ1haxie6oJLzRt6jX-2NhQ4qBtT070wf8T4LXgUCL16sN-whhHalv3rhySGPPR5-kFbbqZKZimveax8Ln7jCSpQe7uPx45V2vhMhRiZ0Uqyzp_odNK8ZakXkSTUmMMQj4xeiiJaqMDhZMQhkvaSgevhTlH6Ynhw8c4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uv6nofMd7sMgJam_DiGPBe9igVSKLBlIXJ3DJmtmkO9c-FqiL9y7dpib2HwYZW6fKs8HfOwpk4X19plVwp99TLHGkKcUdNnrdv9Go6KA-bddzzAfrq-4BHrGBpljzRdb4sGXRvzdfJb5LdEDovEKWhPNVy32XaJsFCO5u9bkVkwbuVUQosqrhPJI7dH895hO1VmzaDuGVqVOxqLl1QRvqhoSyShPFYKuEdhUX-3R32gtnKoa79BJZu-XH7g1dGVTuT-9hE-e1ZJyXpiJwmnQRzsHsghjGkklSOks1fHyHtYyAbnGH6HnC8eIusSJFxSn3_8pwrIB4DPWy1PbtKCSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHcMv-ee6QR0Iqi2gXOlCn8v5e7xEehyP-J8HkZU2TmcP459G8eK_BqD5mYM4VnniDU6fhV95Xx-0lwX-vILL7V_eV8eu5JTaCS5eCMUuLv5wFbkgco92rlqmin-H2_8Szv8N3m39NwwLOPQX8OXgipyEH3Cjw4rvAkDHU2ckZjF9iAFfRiAw2SJOIZs6imR7LkBfJHWZyHZEyGWbi_Lc8aBk6W0WYM6hiGL4XRloZTIwwlRp6yi7iLlrp5UwU1rsnPlbV7iJ9jeM2Xvy70vtgw4XOYnsdJy-bYyW-jQLApLAHiZyfOamceNro-BryxISDVfmenX64MSiDW6mOuXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sV5cOaFh2Wd3e6jHl5oVoSBdBOLrsU-jMVBM0OKgOkD2iP28uBFgVZ8wtRO_zKXyze4cdhZt1-_tSxb2unwP5K-xUI9YmX1YqWF7oU24j-gCXM7UgpLI-l7Bx1ltbr1z70Eye1VQK9zZ4oWvcWDAsZ0LRbB2zcvSwymQYPWQXRTxP1YN1qBLEvn-rSe5vhi_MG-dL8Q-XEgvRQ0Etcf6tMXAMhxRto7nZB5ryVh499TcP7j2MlNNyv1UgsS-DEbROvmNsjhQEvP7iJJtNCpYQXhpJQ_Dumm5VFNYo-26q5cL5ckKNbJ8C2x73MiVBJKxX7pjGHyV0EB5_hz4PcBB7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bNMI70OjFftfY3xgxDb4sBq-0yq9evLT2b8DYkcnd0_sXtT8mnfyaRi3U49l0DoSLz_ntI-uBb2L_djQiJ98TPHsUtaI1oxisXB7GYPS1Gt6iOhlDeG4z6OfxqUvHpkky-kQ7fmTDxNVeBBPG2xnOhYdI8f51kcxKzLuIbo792W31dcNJJ-JhvMWwnqS6BZEiM2u5cmdRxTv_6pIBKBcr5FqN228pOuD10AJ8S10jVMZ283y9qWPM9TKvc616JMVkm31M8alXvC2ec1Afz2Yjx2y33nV09D13FKxZhw9vocLL8DtTHHSoKKLlkypv3PebAkZWAcVb2BvAN28SC7NbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ao8p06ngd0hgcUMr8npBHryunRRodBPKqShYitl6GfTDc8q4Uq8MuyDZ8JU5y_FrgdswVL40i12_cwoeQl-muKN9E0SddTxNMbxrW97CIQ6CHsBEt63eXPSf177vBMWwls-J4eOQxOsDSTCCiT3lMlqMlCEY1uoBjZEo9Ly8AG_IzRkO3ZQ7fyORv5A-Erx1VqC2fPZroERwq4-J492Cx6bezfwHzypb6PHo0u3ero7R2p3Ao2fNq7wXt13EDN_IuaBZBRm1AuVdZU6oavpc3NwN4wX-RTTbjGe3tHCkYWym_uLIkJHB3olF-O9dgpyO5wHn5l-FhZv7xIpycraU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GcvRnb6IaaQ4mD2k5Bg6aXJGyvAp3eFDjReYfZXDVBvJ5ImS9wQ-AjxuV_dWw1rsleTkMu92VVuZdFGYY3bUXusNAzQ0-FpZb5WQqRWWDcRZCuMUwFBalAhHAdunKwioK-iLw29VyObEC7TT3us-tq2ILyDBIVmjrAdyzwFVeLvW7AUlYSWBuwOBvW_6Zx5siml1XIdwT71pP1fKBF46sUuNYw_LndFerhxiV8HNh8khycKxh-Tnl0gHtEy63eIPp-JQDWt9LqpDX4X1ppGTCZ5Fv-vK4_P9mugWEVwInhv_-w7gW0-TsYbfCIXdCWhaM8Eo8zDETaq8wtBsE2dq8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین نکوداشت شهدای اقتدار فراجا
عکس:‌
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/441826" target="_blank">📅 19:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441825">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luQyU6l8gQvMN4-VrgaiXKlI2vF-v0wp85F6-b4rkSt60hIJ9AfUqvm-PQy2p_8-a9NSzsIpOd0HUvWyQXPoVrJW_n55rlgaImPyX2HD-hxzSd3vg3eBwX-8La8N4Qgh2qlFmQbz3AlZ3CjCZoWmTgb-6bARXJlzB4G9UwMGXaxKtY9Iyr0RC27wz8w9XYCSkYrriSxY81DLBkzLg8MHtIef9QUNcG13oD1iJzgtRNDMqVfKK97kQ7diNqn2MiqIZQuTCIDS2YCstAcJxMUIKiQ2xg5M0HBuV252u-N-hVplNQShdEdvTPzCZRd8IiliYnzMhz814Z-5nCxLNhN94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بسیج سازندگی: نیازمند تشکیل قرارگاه جنگ اقتصادی هستیم
🔹
پس از ناکامی دشمن در عرصه‌های نظامی، تمرکز او بر فشار اقتصادی و معیشت مردم قرار گرفته و ایران نیز باید با فرماندهی واحد در این حوزه عمل کند.
🔹
همان‌گونه که در بخش نظامی قرارگاه مرکزی برای هماهنگی عملیات وجود دارد، در حوزۀ اقتصاد نیز باید یک ساختار متمرکز و فراقوه‌ای برای تصمیم‌گیری و هدایت کلان ایجاد شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/441825" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441824">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۶۵.pdf</div>
  <div class="tg-doc-extra">8.1 MB</div>
</div>
<a href="https://t.me/farsna/441824" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۶۴.pdf</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/441824" target="_blank">📅 18:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441823">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBKsSEm7XSciVkLf2uhZUn2T5SJY7M-flnz2e8Ru0D85i6gDjO78_m3EQxlqGyJVHe7O3g2bIFQ-efLsNjKZVjBvBygLDSMzRqKUSYikqc3klt14BICd_RoIW9vSKgKO2cvPe7bjuPdAhJwhz3zqeIuGwPsa9Abo7bkVRZRvzB8G3nitmnTBtWZgz6yxu3snsjWxiXEk3XE7gz12qVjEjLTx6fKdRl3b_iTPJVJO9Non56n6JIZc4zSUkkTmNnIR1xuTTKzAJ53KGmM1kHY2X-xX27mIytUxsGmvCSUWkosE7oq4DLlhA5n4sthUuBmPwUOy0LDZWfSinxDzX2k6JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به استان نفتی «حضرموت» یمن، نیروی نظامی اعزام کرد
🔹
پایگاه خبری «وكالة الصحافة اليمنية»  به نقل از منابع خود در حضرموت گزارش داد نظامیان آمریکایی با بالگردهای «شینوک (Chinook)» وارد پادگان «نحب» در بخش «غیل بن یمین» شدند.
🔹
این منابع احتمال می‌دهند که این نیروها از فرودگاه «الریان» در شهر مکلا — که نیروهای آمریکایی از سال ۲۰۱۶ آن را به عنوان پایگاه نظامی عملیات خود استفاده می‌کنند — یا یکی از ناوگان‌های مستقر در دریای عرب حرکت کرده باشند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/441823" target="_blank">📅 18:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441822">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0G-FuMoDeujeK9-lG3mkjbV9HHrK4k_W4ii5InAn3Flp76h11hcNRux9VigQ0H7uJ_9Aw7SGtszz5WBcEjlR0AW589XooyyQ2HU5fhswAjZlkfY3Rqdga0MLyHNuqVy8mZeaKMn-qU_zEG8gJ4g_Z7-8Z-lez2MYzxo49-ZY6cS9iSa1AAztENRCzKyntGhQesejWWa9lr9mk_PG0te0iKXlT9ZyvpsvCOrpY-IitxJazmwb-ukykD5GBAw02xf-k8RxhFWVO7-vsftobXoohT4KIMLAs0NawLJxFKS0PSwpz1qGTkj6nWe_uiZ46L-F674aUdYGjVAJFUX_BnVug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاح آزادراه شهید شوشتری تا ساعاتی دیگر
🔹
آزادراه شهید شوشتری، یکی از مهم‌ترین پروژه‌های عمرانی شرق پایتخت، تا ساعاتی دیگر به‌طور رسمی افتتاح و وارد مدار بهره‌برداری می‌شود.
🔹
مدیرعامل سازمان املاک و مستغلات شهرداری تهران: پروژۀ آزادراه شهید شوشتری که از…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/441822" target="_blank">📅 18:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441821">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHyhzEr-64roHv1i2V2RvFw_dMkH8fhoF4_lrY-LUVnIbThklM4rMgRzNNdLDnCENDzFLOJUOJRl6HzGKbzAs1YUtmG4alRQFEvo5mZfwYEMjS3eE6cpOdBi5Ul_Xx3nla-vUaZnteFBVMgn32wv17-snCg2_hdooCADo3Zq44zS7g_KtFSbu465LVbnfbBND3WOec9RDJCBD2kZQUTzj55oaiL-ETqoz2Q1d7lRqvRWkn66UckGXIleBRDCZSPqZs4UZsvSEHrNIkkuWMTgHb9uM7YQAnB8mpdXPcfH0x4SgBZgXkyNI1zq6wM3EUoHnLnmmIaT4I6QFgsoYrIQrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: باید هزینۀ خدماتی که در تنگۀ هرمز ارائه می‌شود را دریافت کنیم
🔹
آزادسازی پول‌های بلوکه‌شدۀ ایران بخش لاینفک توافق خواهد بود.
🔹
قرار شد که در این مرحله موضوع هسته‌ای و مسائل مربوط به آن مطرح نشود و متمرکز شویم بر خاتمه جنگ و مسائل لبنان.
🔹
وجود پایگاه و حضور نظامی بیگانگان در منطقه باید پایان یابد.
🔹
اقدامات ایران برای مدیریت تردد ایمن در تنگه هرمز هم در راستای صیانت از امنیت ملی است و هم در راستای خیر عمومی جامعه بین‌الملل.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/441821" target="_blank">📅 18:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441820">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPOtbEfrMQdNpnb0Hnjdy0HoT4AB662BfSLRrVGqXshCSChPQunIjhgyimwbcA9vAzi5UlCD4gShflb65MjxS37zlJ8hHK7xlgWFkzBgBVmjAXoxvsG8fpCht5ZqiMJ7BkG-eZSI2R0lb5gQRsWWk7goRA6vFWuAmVScgjvOmDdPkE8WOOC00MBDzmCunHYAVCwnfPAb2M61FD-fN4-oA8QDF579ALT54lUQEGbqrhc7M-ejA3r6jG-JXrHgelLN9s2G9Z-h1VbfUtGVMxnHXRglnvpE8LIcVTFcZA7u-UwtEw1n--rzY_Eu1vCcpDLJQ8tNYZpIzaFejAcAAFRLCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا دسترسی خارجی‌ها به ۲ مدل هوش مصنوعی را محدود می‌کند
🔹
رویترز: دولت آمریکا قصد دارد دسترسی کاربران غیرآمریکایی به دو مدل جدید «فیبل ۵» و «میتوس ۵» شرکت آنتروپیک را به دلایل امنیتی مسدود کند.
🔹
این مدل‌ها برای کارهای پیشرفتۀ تولید و تحلیل متن، برنامه‌نویسی و حل مسائل پیچیده طراحی شده‌اند.
🔹
آمریکا نگران است از این فناوری برای شناسایی آسیب‌پذیری‌های نرم‌افزاری سوءاستفاده شود.
🔸
در صورت اجرای این سیاست، تابعیت افراد می‌تواند به یکی از شروط دسترسی به پیشرفته‌ترین مدل‌های هوش مصنوعی تبدیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441820" target="_blank">📅 18:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441819">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d98451060.mp4?token=EBlTNZic3oPwmNKJRF7g1lFQfTqzuVh9C-MmpT6QsMyuC7JZI7SR-gcznGarus7vc1BSU-AodHmkaqDe4D8v9rTQ7O8Hx6nliBDsSjOVVzFTu_2liw2NWaVJITpIwLwDaytjCI-vkehDOYWYijEMMIBAemiiCFInKcQL9fcP_S3G3HoeBo98QwWoROpZuQTBQ-efYzh2dzZh74NtEVwd9k7KOc7Re7h6zw0pgW2xfWK00psTUpSydTthgLcI4Rddfr7wyKTcec9yLUr7yL9TuQXfWaf2Su1wYBZTlFqhY-F7Br_Q8CxKgwmPR5TY7Cj2cZcl3WnliA3hRUhEPUrKyZs7WWSJqiSkkU1RqA7PniiSueBEW6eoumvaqJr2RXB2neGyJfvzSfPdnIvB-TOvbzoQ5tjC0DkJmnfY_D2HUjVMaoh2yL9_F7VOjqNeyz9oMPwiseyRkJ_resS86Gcdki9eeVrHowweHUrhGBWFuATyMLs4BXeICvpcOJpO2pKzQZz4urP_XV0GiPr-ykQnt_4zIgYSO41N_gBsakcjNLw-dLI_4UeSNGw-yJL2XeU8k0Gc5rlcWrEDkTfs39KyVBZjH-6yFvBZ28YUtCTKH-qJg-99lZwvJ8VD1lwPy0Rw4hT-qLTVDYDZlO4KHz0XV_-ILstPiJsqp8PWqWETYJI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d98451060.mp4?token=EBlTNZic3oPwmNKJRF7g1lFQfTqzuVh9C-MmpT6QsMyuC7JZI7SR-gcznGarus7vc1BSU-AodHmkaqDe4D8v9rTQ7O8Hx6nliBDsSjOVVzFTu_2liw2NWaVJITpIwLwDaytjCI-vkehDOYWYijEMMIBAemiiCFInKcQL9fcP_S3G3HoeBo98QwWoROpZuQTBQ-efYzh2dzZh74NtEVwd9k7KOc7Re7h6zw0pgW2xfWK00psTUpSydTthgLcI4Rddfr7wyKTcec9yLUr7yL9TuQXfWaf2Su1wYBZTlFqhY-F7Br_Q8CxKgwmPR5TY7Cj2cZcl3WnliA3hRUhEPUrKyZs7WWSJqiSkkU1RqA7PniiSueBEW6eoumvaqJr2RXB2neGyJfvzSfPdnIvB-TOvbzoQ5tjC0DkJmnfY_D2HUjVMaoh2yL9_F7VOjqNeyz9oMPwiseyRkJ_resS86Gcdki9eeVrHowweHUrhGBWFuATyMLs4BXeICvpcOJpO2pKzQZz4urP_XV0GiPr-ykQnt_4zIgYSO41N_gBsakcjNLw-dLI_4UeSNGw-yJL2XeU8k0Gc5rlcWrEDkTfs39KyVBZjH-6yFvBZ28YUtCTKH-qJg-99lZwvJ8VD1lwPy0Rw4hT-qLTVDYDZlO4KHz0XV_-ILstPiJsqp8PWqWETYJI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله یک خودروی رژیم‌صهیونیستی را در جنوب لبنان هدف قرار داد
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/441819" target="_blank">📅 18:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441818">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpl_o4pxJvof9oyBZwS3kXaA-zyHOkzW7au_xK7R9SsQa1RU1RBAMejUKWVjGSgrKXJyjpp_frICf8f-l7ByW8i2aEYYGaqD_jb4KB4FOLRGeNv8hfM9vR6g49wKraJx-BwBTZ5N-rjbVTgmzlvw3MUa3wOCwRJFoLUo8BwXlq3jRn-HFck-7CZJLZbIY7CcvKOuiCpXhjNpIB1P_3Mob-8yzOCRtI2eofLK1lk5aDKqSGqg1e_knjchNb4rBl-SdOJJ5xdtWswRtny2AEgbhZmpeQMZ_E4cBjSGg5CARQOrrDTgTl-bO-8uw95yx9rp9W-2hVUyDwW1AsJPjJYWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادستان‌های آمریکا تحقیقات از مالک چت‌جی‌پی‌تی را کلید زدند
🔹
ائتلافی از دادستان‌های ایالت‌های آمریکا، تحقیقات رسمی دربارۀ فعالیت‌های اپن‌ای‌آی را آغاز و این شرکت را برای ارائه اسناد و اطلاعات احضار کرده‌اند.
🔹
این تحقیقات بر موضوعاتی مانند نحوۀ تبلیغات، تعامل کاربران با چت‌جی‌پی‌تی، سیاست‌های نگهداری و استفاده از داده‌های شخصی و همچنین پردازش اطلاعات مربوط به کودکان و سالمندان متمرکز است.
🔹
دادستان‌ها همچنین خواستار توضیح درباره شیوه آموزش مدل‌های هوش مصنوعی، سازوکارهای کنترل رفتار آن‌ها و میزان خطاپذیری پاسخ‌های تولیدشده شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441818" target="_blank">📅 18:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441817">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/964e670110.mp4?token=qByPiyeKG0Pabzou72AvRtxdYJzrLayAou9npMR12vaO18RyKCL-I1xZm42lkZSNqCt6Ag1QzgQwSUvPtZV2yVbcr5pr77-YBCaSQReqTlY0RNfjpyxw_BK450Vwi9LOhjWz9gW-nCll_STYXfRRIQaew1Y3Ty1Kqq-QDIvJl_RZsE4aQ2LuH7HWws_VAavnoCKxHQurghj9B6hPMwlicsiGuxxcyKv_1RN1R8dbUHKnJxYoV0s_PNs4KXN9EBxPVnG0yFWVMPgM8dsIhabRSaRmmJb-NfyeQlC_w0GlOrAkHh_MBtQ1hFmHM67tlBGXiODO5jCgfjeyIeWMQcsEVzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/964e670110.mp4?token=qByPiyeKG0Pabzou72AvRtxdYJzrLayAou9npMR12vaO18RyKCL-I1xZm42lkZSNqCt6Ag1QzgQwSUvPtZV2yVbcr5pr77-YBCaSQReqTlY0RNfjpyxw_BK450Vwi9LOhjWz9gW-nCll_STYXfRRIQaew1Y3Ty1Kqq-QDIvJl_RZsE4aQ2LuH7HWws_VAavnoCKxHQurghj9B6hPMwlicsiGuxxcyKv_1RN1R8dbUHKnJxYoV0s_PNs4KXN9EBxPVnG0yFWVMPgM8dsIhabRSaRmmJb-NfyeQlC_w0GlOrAkHh_MBtQ1hFmHM67tlBGXiODO5jCgfjeyIeWMQcsEVzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲ ماه از این ۱۲ روز گذشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441817" target="_blank">📅 18:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441816">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پیام فرمانده قرارگاه خاتم‌ به مناسبت نخستین سالگرد شهادت سپهبد پاسدار علی شادمانی و شهدای اقتدار ایران اسلامی
بسم الله الرحمن الرحیم.
🔹
۲۳ خرداد، یادآور آغاز دفاع مقدس ملت ایران در برابر جنگ، تجاوز و جنایت تروریستی ۱۲روزه صهیونی آمریکایی و نماد ایستادگی ملتی است که بار دیگر نشان داد امنیت، استقلال و عزت خود را با هیچ قدرتی معامله نخواهد کرد.
🔹
در نخستین سالگرد این حماسه ماندگار، یاد و خاطره شهدای والامقام اقتدار ایران اسلامی، به‌ویژه «سپهبد پاسدار شهید علی شادمانی، فرمانده شهید قرارگاه مرکزی حضرت خاتم‌الانبیاء(ص)»، را گرامی می‌داریم؛ فرماندهی مؤمن، بصیر، مجاهد و راهبرداندیش که عمر خویش را در مسیر دفاع از اسلام، انقلاب و میهن اسلامی سپری کرد.
🔹
شهید شادمانی از فرماندهان برجسته مکتب دفاع مقدس بود که از مسئولیت‌های میدانی در فرماندهی لشکرهای ۳۲ انصارالحسین(ع)، ۳ نیروی مخصوص حمزه سیدالشهدا(ع) و ۴ بعثت تا فرماندهی قرارگاه نجف اشرف، دانشکده علوم و فنون پیاده و در نهایت نقش آفرینی راهبردی در قرارگاه مرکزی حضرت خاتم‌الانبیاء(ص)، همواره منشأ اثر، ابتکار و اقتدار بود.
🔹
ویژگی ممتاز شهید شادمانی، پیوند کم‌نظیر میان ایمان، اخلاق، تجربه میدانی و تفکر راهبردی بود. اخلاص، صداقت، شجاعت، ولایت مداری، انقلابی‌گری، مردم‌داری و روحیه تعامل و هدایتگری، او را به الگویی ماندگار برای نسل‌های آینده نیروهای مسلح و بلکه جوانان غیور و مدافعان دلاور وطن تبدیل کرد.
🔹
امروز، در فضای ناشی از جنگ تحمیلی سوم امریکایی صهیونی موسوم به «جنگ رمضان» که ملت مبعوث و برانگیخته‌شدۀ ایران اسلامی، خلق یک رستاخیز معجزه‌گون در حمایت از نیروهای مسلح بیعت با ولایت و خونخواهی قائد شهید امت آیت‌الله العظمی امام شهید سیدعلی خامنه‌ای (اعلی الله مقامه الشریف ) را رقم زده است پیام خون شهیدان اقتدار برای ملت ایران و دشمنان این مرز و بوم روشن و آشکار است؛ جمهوری اسلامی ایران با اتکاء به ایمان الهی، سرمایه انسانی مؤمن، توان دفاعی بومی و وحدت ملی، تحت زعامت قام معظم رهبری و فرماندهی کل قوا حضرت آیت الله سید مجتبی حسینی خامنه‌ای (مد ظله العالی ) مسیر عزت، امنیت، اقتدار و پیشرفت خود را مصمم و باشکوه‌تر از گذشته ادامه خواهد داد.
🔹
اینجانب ضمن گرامیداشت یاد و نام «سپهبد پاسدار شهید علی شادمانی» و دیگر اقتدار ایران اسلامی به ویژه فرماندهان عالی نیروهای مسلح، بر تداوم راه پرافتخار آنان در صیانت از امنیت ملی، تقویت بازدارندگی و پاسداری از آرمان‌های انقلاب اسلامی تأکید نموده و از خداوند متعال علو درجات آن شهیدان والامقام را مسئلت دارم.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441816" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441815">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e089dd3f60.mp4?token=pTxdkusclLt-xH7QKH8kW8godkOcBzUdNzxOvSTdC_kihidifMqa7cCqTuoP5w4c3jdCZL0nqPs8lhmQ1DZSSMFdRpA3jjM2EwZsAAVfIDl7bZ6_4PLp5Ft-hWPod8ALC1iuCmaQf3_dpXJGOx-Mzj3Z8dh2a1Ix0s-vexUwxr1QhwNyCJFf7tSRuFmEPCXYAmC658s05BOcGk_1MR0aLmBYfS1byaiGmOEUIRtXptBLrGmkyBeyFZoL0DFLQpTvCqySNHOg3JymUHXzXqWKMLZSq9OO05CKRjLSbvzC2DXeJP0m7rEIGEtZhUjniuJstW_nEKiLPqqJQ10dMls3Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e089dd3f60.mp4?token=pTxdkusclLt-xH7QKH8kW8godkOcBzUdNzxOvSTdC_kihidifMqa7cCqTuoP5w4c3jdCZL0nqPs8lhmQ1DZSSMFdRpA3jjM2EwZsAAVfIDl7bZ6_4PLp5Ft-hWPod8ALC1iuCmaQf3_dpXJGOx-Mzj3Z8dh2a1Ix0s-vexUwxr1QhwNyCJFf7tSRuFmEPCXYAmC658s05BOcGk_1MR0aLmBYfS1byaiGmOEUIRtXptBLrGmkyBeyFZoL0DFLQpTvCqySNHOg3JymUHXzXqWKMLZSq9OO05CKRjLSbvzC2DXeJP0m7rEIGEtZhUjniuJstW_nEKiLPqqJQ10dMls3Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند دقیقه با جانبازان کوچک جنگ رمضان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441815" target="_blank">📅 17:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441814">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqAtxfv95dpr4JrA9_8_8tWEtP_uoZIS1sYLgCqiUC7V12yxq4xrj14JU5xQmdABRcFMGKsKkJxRbZEvgJHOwG3f9PDUxJTBD8R6h9pwJh-N9XrrU8BOff0tsgPAoL-b4JjAdnRncjtROAzFszkRpELdKWx-QZyM-bzrPscw7F5_ZfWaToVCkswJvua2q0jMy_DwJCdmuRpsuCmQdTcgB1DkJM_Uy3tXUx9VW1nKZgQCzZi1jTjy-3q66RTc_x1GpoJ2BNZE6BywofNj7avRvB6TYjc40E-n7AkDNTMAp1Y8t3qA47l_RoKnSg5oLWvDchy-jnqgyI1nXCsAI4Ep0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار وزارت بهداشت: مکمل‌ها و ویتامین‌ها را خودسرانه مصرف نکنید
🔹
دفتر بهبود تغذیۀ وزارت بهداشت: مصرف روزانه و خودسرانۀ مکمل‌ها و ویتامین‌ها نه‌تنها ضروری نیست، بلکه در برخی موارد می‌تواند به سلامت آسیب بزند.
🔹
مکمل‌ها جایگزین غذا نیستند و فقط در شرایط خاص مانند بارداری، شیردهی، سالمندی، دوران رشد یا برخی بیماری‌ها و با نظر متخصص باید مصرف شوند.
🔹
مکمل‌هایی مانند ویتامین D، کلسیم، امگا ۳، آهن، روی و حتی مکمل‌های ورزشی نظیر کراتین و گلوتامین، تنها در صورت نیاز واقعی و با تجویز متخصص توصیه می‌شوند.
🔹
بهترین راه تأمین نیازهای بدن، داشتن رژیم غذایی متنوع و متعادل است و مصرف بی‌رویۀ مکمل‌ها می‌تواند عوارض جدی و گاه جبران‌ناپذیر به همراه داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441814" target="_blank">📅 17:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441811">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985b9f9324.mov?token=J2VcKZ6wmL1c7JoEiGGw0wbdUGYKu5CEyWkgJLlH0axVqUxKQjGfQ8XiTJcdHE2Bc37_0j7QX66JccGyejV4NHd1wWQdjF14fLnSdsSTyYAu3bkZNULrCQshB7rjcdwHwCDS7HnNcNdD_ax7YUjSqNPf24u_WpJZKWFeHZ1uerQTcD-94l4_8Z3dLEcnylV1-s0tTblPx8ww2a1ktsuoJpKrtvnHsuWqURJ9eJs633JWy_37ZTlj2GxXLGk9vwWr3NIX0hLet3JVJMH4Q50t75PZIcqLsjrhJPiGmHHfQZ-xRzRGbOWeu5JfS2a0T4uRZZwy8gski3GXt5aA9oK1DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985b9f9324.mov?token=J2VcKZ6wmL1c7JoEiGGw0wbdUGYKu5CEyWkgJLlH0axVqUxKQjGfQ8XiTJcdHE2Bc37_0j7QX66JccGyejV4NHd1wWQdjF14fLnSdsSTyYAu3bkZNULrCQshB7rjcdwHwCDS7HnNcNdD_ax7YUjSqNPf24u_WpJZKWFeHZ1uerQTcD-94l4_8Z3dLEcnylV1-s0tTblPx8ww2a1ktsuoJpKrtvnHsuWqURJ9eJs633JWy_37ZTlj2GxXLGk9vwWr3NIX0hLet3JVJMH4Q50t75PZIcqLsjrhJPiGmHHfQZ-xRzRGbOWeu5JfS2a0T4uRZZwy8gski3GXt5aA9oK1DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهروند برزیلی که اینتترنشنال را سر کار گذاشت!
❌
«دود ناشی از انفجار در شاهین‌شهر» عنوان فیلمی بود که اینترنشنال از درگیری‌های چند روز پیش منتشر کرد.
✅
اما مدتی بعد کاربری که این فیلم را برای اینترنشنال فرستاده بود، نسخه اصلی آن را  به خبرگزاری فارس ارسال کرد.
✅
این فرد ساکن برزیل، بعد از دیدن اتفاقی رد دودی در آسمان که به محل یک آتش‌سوزی ختم شده، تصمیم می‌گیرد فیلمی ضبط کند و آن را اصابت موشک و انفجار در شاهین‌شهر اصفهان معرفی کند.
⚠️
چند ماهی است که شبکه اسرائیلی اینترنشنال با کمبود سوژه مواجه شده است و برای اثرگذاری بر جامعه مخاطبانش هر خبر و مطلب غیرمستندی را به خورد آنها می‌دهد.
🔎
این نخستین باری نیست که اینترنشنال بی‌پروا بر سر اعتبار رسانه‌ایش قمار می‌کند. پیش از این نیز وقتی از سوی مردم ایران بایکوت شد برای بازیابی اعتبار از دست رفته‌اش اقدام به استفاده از هوش مصنوعی صوتی برای بازخوانی پیام‌های مخاطبانش موسوم به «روایت شما» کرده است.
@Fals_News
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/441811" target="_blank">📅 17:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441810">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
سیاه‌پوشی حرم حضرت معصومه(س) در آستانهٔ ماه محرم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/441810" target="_blank">📅 17:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441809">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLVVt-eabM3gfxO8KDiQC8yvemIb3KysrBJtRujo6g5bRO0jM4bsQIDVLJuTBt-wYnCbNpbReo7Jkgc031UdcpQXjoh-EDyOSW5pIWDzeH5QDOj5_hNTb2oSRV50k5Z_gR6JIJbvUUVe8-liQME9lpJw-yHdm9nUizzpC36lCTCfYU1kfS0b_PYyZEPXdLsH7JAXgYqU1_HPoFUKMegrfdZT7yJu1gVFoyCrljZmzb4qJgje5b-NVbHzWycUf87B-CcMf0t3IUcpAJAgykS25JKzGiqohTFkho1RJarVFM7rJGJBBs0IAOIm9MZX9jvdPW7zvr-L69qUn581fU5iZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب بوشهر ‌سه‌شنبه قطع می‌شود
🔹
آبفای بوشهر: به‌دلیل بهسازی خطوط اصلی انتقال آب و همچنین انجام تعمیرات اضطراری در بخش برق تأسیسات آب‌شیرین‌کن، قطع یا افت فشار آب در روز ۲۶ خرداد و به‌مدت حداقل ۱۲ ساعت رخ خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441809" target="_blank">📅 17:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441808">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaaTf7DjEt6bvLUXHYXtr7pezw_a1oDWUEaOp7jRJV0ifPvRiXtJPUSVKDFvpyUwD6xl-6agFyRR_B47FrlMXvn__OdUU0llEx3ITXKF1K6SWrl6hNyFgimFWTc5ULq-xc9iuA2ttaYBjhzqZTgfwKXZGLYOrlms7XnsUGh72itkQ3vYaebykNdwGWq0hr8olljUgio8v36SipefLcWekakDvyLDq1rooPskLeEfHbRcRMxIAH7_ocHRc0izceRJYodpJEF2-DDWJqlmXMyGIRnnu0p9Wy5hCYRxItFLX3ANDi3SzTJTLe1TTvfpEZYpJZKu0-72op9aHIrFs9Od2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار همیشگی تلویزیون از دوشنبه برمی‌گردد
🔹
سریال مختارنامه قرار است دوشنبه از ساعت ۲۳ در قالب ۴۰ قسمت ۶۰ دقیقه‌ای از شبکهٔ آی‌فیلم پخش شود.
🔹
این سریال با وجود بیش از یک دهه بازپخش مداوم و تبدیل شدن به سوژه‌ای ثابت در فضای مجازی، همچنان یکی از مهم‌ترین آثار مناسبتی رسانهٔ ملی محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/441808" target="_blank">📅 17:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441807">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOo0Huax9E1-PxYE4fKWFSv8AW6ISn5Wz0YtTnPE7qWy3m9r26W-pVSmCkST1QnysNPf3zO0Seo1uitCYyo7Bgdvo4RQ2-FG8ACFqEmFphUfhYbX67NEV4fbFH5YNYH55PTeDXi5OFPrdWZvjFvHM4YEl-HXUEzkHYGKw0apDsoseJ0g_56Dii0-W3uUJJYnSa6l_yhFsTAGO_iSLUgj4Ru_o_8YQp6owBRRvY6BHpbFFJUDsoWduyJoUS1KflD3WiuGt_SLHk7MDvEaUtaJzkHbWXS9yb4dixM6UbyfIiM1Gx0xiO69ZZcvBOgUexVSVoj6b7tet72CPlFDgg1TNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰۰۰ مگاوات برق با نوسازی کولرهای تهران آزاد می‌شود
🔹
استاندار تهران:  در شهر تهران حدود ۳ میلیون کولر آبی وجود دارد که بخش قابل توجهی از آن‌ها از موتورهای قدیمی و پرمصرف استفاده می‌کنند.
🔹
در صورت جایگزینی این موتورها با نمونه‌های کم‌مصرف، امکان مدیریت مصرف نزدیک به ۱۰۰۰ مگاوات برق فراهم می‌شود که معادل ظرفیت تولید برق نیروگاه بوشهر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441807" target="_blank">📅 16:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441806">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">درهای دانشگاه قضایی دوباره به روی زنان باز شد
🔹
رئیس دانشگاه علوم قضایی اعلام کرد روند جذب بانوان در مقاطع مختلف تحصیلی این دانشگاه، پس از سال‌ها وقفه، دوباره آغاز شده است.
🔹
این اقدام در راستای اجرای سند تحول و تعالی قضائی و استفاده بیشتر از ظرفیت‌های علمی و تخصصی بانوان انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441806" target="_blank">📅 16:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441800">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1OJmMUmFPrikCukPVwDgXZ4SohbO9YQzY0iZfkBy4ozK70Tgzj4glEtzY26ykjzohbbEffkr5tveaa1ZuEdG9TwTi_a-aXGgnT6eb_JFvhgk6hGpOTxTlpl8oFzUoWEUTFibIDl6Qg78Zrpu_EuxKE-PxdG_YQ42tDYjuq9yrCowDDRby6CxdEOmnTbtr5kyXejp0DDxoukojCZu-oWNoAGanJ3svTcEXu0AmkDg-ov_Lv0EhWCQENlE9wUilbh_0kYn54HMgjdS6IaQrTfcbMJ2zA7SLaPkkExEErjwJz9TDPi3KB2YBWHD5PC_JWJTI-qvKHisH8tmrbpGvr2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjUx3Ah0Yb3llLbl6wTlpoV4DR_T9HG5oalRUhQEBe_ofzSSGk7OtfHr99gPO_suSNiVS6IaHFXf4SzpmLd-uVbrKvNbQBF2KT__eZ7lzyfX708AJNourMtJpSxaj-73kpuD2v25br4wipAD3QwDRMHpOT0LHhhnHjJoabcUOWlJv6NFuF7SKIaHFZWYGZooIKjJ3t6LK9rU1Gv3-6s071PrFQpF6i78N3tU2IUTSBko-0-KPq_GvturAzGDDOBm5u4py0NRvLQR_qQgWHp7CaT5J7Hi7eZfEcCV9aQaPx08zlwAWPZoQtv4YJ73mJAPmSleL-mRCeyPxzPEa99xYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2DEUzdLCmGYYoGQ-rzw2tNgMxw-P2oMw4bScQ_u5ohQ5ZpDnfUuZPtgJ5p1ecYSJNF1_r-a418f3QlDRBl01cyhOkUeP2wZ06zavj4Cow-gRlAJ91GRiFk-vp0i1_VdW2YP376KE5qnAQ5KL5fZXg7F3W5JkwA8VUIDJ3orb2J-RlI6nLPtJYOcXp_cOiO-WIGF-6FFXMoyDbDOvvZlNQai660D_0CE-OD5LL0PfC614UdAtFuugL7YQ20K1Qm0so1UjqcDJZf1CGIp0HOMKXWJl_SyuW-DlEM4Ch4qmqR_PzhE5Y_wmkhoVXUWLk7YSduYCT-rt2kNGlIARVs90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpgJ5HsS4aiWBSD78qUoatXqSCJiYUHF1kBS7O8H8aVEqUoyEy708Mh7m11yW8Tlw2CCjXAEGiuhcxtkhMo-IXrEeekptBOLYKb-tH4tm21028CIfA6SdVuKkxBObmURgCvNoYIEIvfnMUzKdHceQ_nJ3tZdvzssic5LoCAp8tDM-oql9YTA-yIco_uupVTUn4zMkMDnCM8ttYuqHTF7PkE62o-buyo5YJZzcm4XfA27I5Knghdhns3yv7NZYC0GwfLubfKeJqrhuILdheDX7i8QS_ttOAPTuYCvXW0sDl_615rHG_NcaeRG2DyYdtAMCQ2ffZaO61V2eBa_nq-grA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlBPYZeGLTiAMiy_cMfD1zUYbpNK-2Q0EXMfVxnFZ-GVOmC6HayDfgQcOsgG9RidepPMHTrmkjO2Sr4ziod104If5QbHy6gWw6JRSmsUcPCl-BU6FgWgUp0_ihDeRzr5N40mOZTZsjzoFmy9KErcoKJymkS8gvFraFHwxF7xDYxVNvETdPLFeFWREWNjXSwiWF6OgaSQL2GMDBHk3NUnEVG0hGTySStuy3hCG4qCYwSSovDTmIUez2QMs5m7O_wOHnqfLYUiPf-RJwWuDwWYu-bKKc91SjByTycplr41o-R0SR1ypOfqAGreUYb9cH2o-zFcobRoAiSiPtNBRyyO8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22310abe25.mp4?token=tiNxziMULcwNzhiz9geNtXVqUPRICj3_Y9zJFouYwVG2xh9QYsVT4Gb6H5fSD1Na3HAC76O-R3WoLbARm4kRNjQ4-zgAJdPmU_GCs3qA7SbToonpsY8h-cVyGU7hEjQGAB3PdVtbO_MYfTt9gQCkjEypBS-CMMWI1BIDjyxsd0PX1oKGXwzlFxT8lAKOa5LbXv3-xmnD22oIRxJAnmHhS8go4eHdax6q3iVqg32Cj2s-v5Vlyx3czMR59JA83kcZj2iHyDndcIBZVcpRUa5hP_KQ3HMevm0Asy8HGl0Ak9Ayf4fR3w1oNQ0AtYQhiwAxJdEE44izJ9zsYnT0UhhqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22310abe25.mp4?token=tiNxziMULcwNzhiz9geNtXVqUPRICj3_Y9zJFouYwVG2xh9QYsVT4Gb6H5fSD1Na3HAC76O-R3WoLbARm4kRNjQ4-zgAJdPmU_GCs3qA7SbToonpsY8h-cVyGU7hEjQGAB3PdVtbO_MYfTt9gQCkjEypBS-CMMWI1BIDjyxsd0PX1oKGXwzlFxT8lAKOa5LbXv3-xmnD22oIRxJAnmHhS8go4eHdax6q3iVqg32Cj2s-v5Vlyx3czMR59JA83kcZj2iHyDndcIBZVcpRUa5hP_KQ3HMevm0Asy8HGl0Ak9Ayf4fR3w1oNQ0AtYQhiwAxJdEE44izJ9zsYnT0UhhqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگداشت رهبر شهید انقلاب در لاهور پاکستان
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441800" target="_blank">📅 16:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441799">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9cfdf36f2.mp4?token=ejR40-MEKzOddyoWJoA-ScYGo7Uhkd9F_uArfGN7kH7Op4fG9H01PtGd_cV-wtLvTp1d75Sw8GUAodHy0ACg58FoKHsKaDgt2I4GF4aj3LhRpYSdC6muNlruk1_LAbpBJGZ2FG6UvFsoaoYZjIrH_HT-OoqTdK_RXW7MezQLpgTAUVoQ1mzp8QMg0iJSbNPNynCgA2CH0aKtvIZkxi3FO5GV3P5Ib7JjNCSq78za0lH_yO4FF7kRINiwyvOFHTqAijlyOXTKmZh6rb5UB2lY3cDf77G2rObQ0-tXYMhsAugn5I2OMTBAbL5EkDmmXUfxKxTpEMty6kcBIb_ytAmr2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9cfdf36f2.mp4?token=ejR40-MEKzOddyoWJoA-ScYGo7Uhkd9F_uArfGN7kH7Op4fG9H01PtGd_cV-wtLvTp1d75Sw8GUAodHy0ACg58FoKHsKaDgt2I4GF4aj3LhRpYSdC6muNlruk1_LAbpBJGZ2FG6UvFsoaoYZjIrH_HT-OoqTdK_RXW7MezQLpgTAUVoQ1mzp8QMg0iJSbNPNynCgA2CH0aKtvIZkxi3FO5GV3P5Ib7JjNCSq78za0lH_yO4FF7kRINiwyvOFHTqAijlyOXTKmZh6rb5UB2lY3cDf77G2rObQ0-tXYMhsAugn5I2OMTBAbL5EkDmmXUfxKxTpEMty6kcBIb_ytAmr2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس هلال‌احمر از نخستین دقایق پس از حملۀ دشمن به بیت رهبری  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/441799" target="_blank">📅 16:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441798">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDrsC8542NDxvwHHGC79HTR5Kik4wK1Pq5fZEMKn6u_OMvSoMeuWde4l_lbv1oIbZAQuAi7hrrfPzp4aF7jjdOxonkej9OstVmf8npi7i7BiQVk2UO7n08wMQGJ58OzWrfAzYyTEVtY_gss36RnK-u5MVY2tHv2WQ4L2r09cUAs-plr5_2XUOdYGJ_A8VFIS3A0mGsjJqFllMRtDkWgINwtx822f6aLHr802kPsiPSGHnvOAiTOhANmbGYFW5TQmQXXfK2xR9g3D2KXK9EcFVowloSJOAAzeo3GHnUYASGEufeiThEL6_0NkXJM7Sm1vQjmE4TZVPL_GeJtyVpMUTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت تخم‌مرغ شانه‌ای ۱۰۰ هزار تومان کاهش یافت
🔹
گزارش‌های میدانی نشان می‌دهد قیمت هر شانه تخم‌مرغ (۲ کیلوگرمی) در روزهای اخیر با افت ۱۰۰ هزار تومانی، از حدود ۴۹۰ هزار تومان به ۳۹۰ هزار تومان رسیده است.
🔹
به‌گفتۀ مدیرعامل اتحادیۀ سراسری دامداران، ازسرگیری توزیع نهاده با نرخ دولتی و راه‌اندازی سامانه اعتباری برای خرید نهاده، به آرام‌تر شدن بازار کمک کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/441798" target="_blank">📅 16:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441796">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pA53bbP0Jovayc2Ih2gyRBfASAcVwI9K_4VVbNFPuYSBTEw2objAcig2nUHgTar33bJDL0i-2zSW_AAE1NR73576uRsqblmcYdJI1_RU7WmDZpPinh6db6I3u-IOYHgHjH9FEzbtU3CL9M0oyQN6vex32XMQInPT5-WdnvzYN7CyE-oexqj2K2Wdj5KoVhW5EO0klrjcglzqEbLKw1oIEB3gUQzq3yBPF7Q-UyWIxmFm1p7Z-LVdx4pqQxiSG4MFmYFaC7OksCeGBNuK49Dh1h2uDqIuhvEluclNJRFblJH4A-CUDmPLo3YWR47OilkGM8v08kKgRiWW-Qphw2G5ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ پهپادی اوکراین به ترمینال گازی روسیه
🔹
درپی حملۀ شبانۀ پهپادی اوکراین، یک ترمینال دریایی گاز در سواحل دریای سیاه دچار آتش‌سوزی شد.
🔹
این مجموعه از بزرگ‌ترین پایانه‌های مدیریت و صادرات گاز مایع روسیه در دریای سیاه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/441796" target="_blank">📅 16:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441795">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9761f96324.mp4?token=RmdtfxuoDUxrXtvBZpt7aVckEk-p9JBjWUOCUJtaz3f6GfFQBdoHmErLJKHu4qUBk6JN3SltnM-kyoPCrUPG4RcDbSSgploHSGYqJ7ZNEViTv__WzXZ72o8TQSasxMI21jjRdmf3_J7Cl4ie6-8M5bB-toLTRNtRi6k-rijBO4cVh0tDJ7uLeSwHa_nMFzy65DFsuVw_kZ6PcyQdqe8UDhbfTERMVM1FkhuUuG1-f6qUleIVTyhgPHRcVq_rrmqoJfEqzMQYwYOnQWtgyASYG_WStBt9A6ZQMeaBPboKfKeF1MfyRiCA__MW0SOPZlEgy8ndYV8MSSDZNNERZd8Y-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9761f96324.mp4?token=RmdtfxuoDUxrXtvBZpt7aVckEk-p9JBjWUOCUJtaz3f6GfFQBdoHmErLJKHu4qUBk6JN3SltnM-kyoPCrUPG4RcDbSSgploHSGYqJ7ZNEViTv__WzXZ72o8TQSasxMI21jjRdmf3_J7Cl4ie6-8M5bB-toLTRNtRi6k-rijBO4cVh0tDJ7uLeSwHa_nMFzy65DFsuVw_kZ6PcyQdqe8UDhbfTERMVM1FkhuUuG1-f6qUleIVTyhgPHRcVq_rrmqoJfEqzMQYwYOnQWtgyASYG_WStBt9A6ZQMeaBPboKfKeF1MfyRiCA__MW0SOPZlEgy8ndYV8MSSDZNNERZd8Y-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس هلال‌احمر از نخستین دقایق پس از حملۀ دشمن به بیت رهبری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/441795" target="_blank">📅 16:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441794">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa8322c0cb.mp4?token=XC_NydNpH3GSOC8rMKVE5b2uZAMwulQgAF4ifcYcpDhQ16-Id0HJ9mrgndH3IGiV62Qo9-Lj2jQ7gVgoA8p0NMB0NJd7jaGhFQYg4QVmVP3-uh30CKU1Z9Pv6ZPlCQSKJwrE7jCw6naCLj9wgWd_MevWk0iccKyg7xLXquWf90u94uy2-R3a_YZpuUtH5N3ET2tOVjg8dGBqavhwqqLBqP0eseuGkT-bF7NrqNed407Fml9aFFCM_2uwvoBVqjPGK3j52oG6aB98d1Q8zworrZX_SReSsQ5KEqHdYvv9XYasnM72OQ2f_nXzesW7h_9eSTulemBOwwK4VmzJkZ_AiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa8322c0cb.mp4?token=XC_NydNpH3GSOC8rMKVE5b2uZAMwulQgAF4ifcYcpDhQ16-Id0HJ9mrgndH3IGiV62Qo9-Lj2jQ7gVgoA8p0NMB0NJd7jaGhFQYg4QVmVP3-uh30CKU1Z9Pv6ZPlCQSKJwrE7jCw6naCLj9wgWd_MevWk0iccKyg7xLXquWf90u94uy2-R3a_YZpuUtH5N3ET2tOVjg8dGBqavhwqqLBqP0eseuGkT-bF7NrqNed407Fml9aFFCM_2uwvoBVqjPGK3j52oG6aB98d1Q8zworrZX_SReSsQ5KEqHdYvv9XYasnM72OQ2f_nXzesW7h_9eSTulemBOwwK4VmzJkZ_AiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم از حال خوب دریاچهٔ ارومیه می‌گویند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/441794" target="_blank">📅 15:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441793">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sglvb_29G0SgBoSTR60VGv3lsbrXmZwl9GjWD6UA8fz-fKc12n3oCeaIGTx-hso3mKjbj0cDHcX0GAtMntZMG6oWH-BAtukuOXovQi-90FWn7aWMPPox7ZFoXxIyUQOlft-ixzELyeVVtMqIpai7VWlFkwfnxUZsZOfWltu1eoWoVmwSJbwfHsFscwZuFE4Z4fY8GK9C5svFVUt5VBtugLYzve_h4Ws5ZF4Z9OMKXuwP2JOMPMOiU_fvMQcO4UIlQM_aFu77H_w4jDHq-PvVs7WOmkaGeseIgbrSccXUjQbDT2mDk6BZMOj6A3CQl08i8MHODJeCIgedMQj3Ezv5Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزینه پرسپولیس لژیونر شد
✔️
یحیی گل‌محمدی، سرمربی اسبق تیم‌های پرسپولیس و فولاد خوزستان، پس از توافق با مسئولان باشگاه دهوک عراق، قرارداد خود را با این باشگاه امضا خواهد کرد تا در فصل جدید رقابت‌های لیگ برتر عراق هدایت این تیم را بر عهده بگیرد.
⏺
باشگاه دهوک که فصل گذشته عملکرد قابل قبولی در فوتبال عراق داشت، امیدوار است با حضور این مربی ایرانی بتواند در فصل جدید برای کسب عنوان قهرمانی و حضور موفق در رقابت‌های آسیایی رقابت کند.
⏺
گل‌محمدی طی روزهای آینده برنامه‌های خود برای نقل‌وانتقالات و آماده‌سازی تیم دهوک را به مدیران این باشگاه ارائه خواهد کرد تا تمرینات پیش‌فصل زیر نظر او آغاز شود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/441793" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441792">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a1c90fee8.mp4?token=iPpjuQcuEtiWJ4eojllz1eX5-pRqSb8XBtCBNdqevWy1HspepRIrr6vBwSo66snXA7sh6Fwq1jjwMGrvvwK696F6Lx7kipDa1Cf2hsJ0Z-ianEb4GA0o4xDYgiUWPHvPPGyYBCEiKG87T-VdjbQIqU-UdNnV9JlGviAWc0V4iZAkTn56zmmdSYg7Wy2bshshHH9n3AvRqLZ2JUxGDXrjKjyNzETU5WrLfooXBDZ8MUmYkp5PENZZ-iSKX0dmlmxNhzINvM0mn7KsBYSRjU2i49trYQBSw3JhlabMEEyFFwvk64H5sWv925vGpunVb4h2ynjYFIli1ptQlz9H0m9z1JGBY0S5mES4WObFviFJDcHxQYUFr7AnPGlIXqpK9vHRtXBGA_ms7eTmjyAT1jvoZdWKqiVbL-PedV4BSNRfeLrHPOkHxEIOiQ1Gb4cY4DwGpip5yFPx3BBoJC4CFBiDWrO-UPONuv2tAvLjcmLWy35Jr_i61zwk9UyCMTqsWsqFQXLgzogW1sd0r_LqFo9GfhB8trjJ-YsTunmzNoGSTtw8nZ0OJPzkt14vUGsKzLe3ScwrQqaufHpa02ge7lAI4bVfIF1Zi1PVRyOm3AS12rP6eGOXcxep4pFM7NA1uevHpHe7gPgsLmyluqn3C0ksBftHUD-KESWFbqV_zypbZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a1c90fee8.mp4?token=iPpjuQcuEtiWJ4eojllz1eX5-pRqSb8XBtCBNdqevWy1HspepRIrr6vBwSo66snXA7sh6Fwq1jjwMGrvvwK696F6Lx7kipDa1Cf2hsJ0Z-ianEb4GA0o4xDYgiUWPHvPPGyYBCEiKG87T-VdjbQIqU-UdNnV9JlGviAWc0V4iZAkTn56zmmdSYg7Wy2bshshHH9n3AvRqLZ2JUxGDXrjKjyNzETU5WrLfooXBDZ8MUmYkp5PENZZ-iSKX0dmlmxNhzINvM0mn7KsBYSRjU2i49trYQBSw3JhlabMEEyFFwvk64H5sWv925vGpunVb4h2ynjYFIli1ptQlz9H0m9z1JGBY0S5mES4WObFviFJDcHxQYUFr7AnPGlIXqpK9vHRtXBGA_ms7eTmjyAT1jvoZdWKqiVbL-PedV4BSNRfeLrHPOkHxEIOiQ1Gb4cY4DwGpip5yFPx3BBoJC4CFBiDWrO-UPONuv2tAvLjcmLWy35Jr_i61zwk9UyCMTqsWsqFQXLgzogW1sd0r_LqFo9GfhB8trjJ-YsTunmzNoGSTtw8nZ0OJPzkt14vUGsKzLe3ScwrQqaufHpa02ge7lAI4bVfIF1Zi1PVRyOm3AS12rP6eGOXcxep4pFM7NA1uevHpHe7gPgsLmyluqn3C0ksBftHUD-KESWFbqV_zypbZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گروهی که عکس شهدا را به خیابان‌ها آوردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/441792" target="_blank">📅 15:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441791">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نظامیان و خودروهای ارتش رژیم صهیونی هدف حملات حزب‌الله شدند
🔹
حزب‌الله: تجمع‌های وسایل نقلیه و سربازان ارتش دشمن اسرائیلی را در موقعیت بلاط مستحدث و شهر مجدل زون با حملات موشکی و پهپادی هدف قرار دادیم.
🔹
همچنین ۳ خودرو و بولدزر نظامی در جنوب لبنان هدف پهپادهای حزب‌الله قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/441791" target="_blank">📅 15:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441790">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJbBNpKT-aqXqHeM1uVxXK3abAdamVTQexDyxSv3rbjLIgMxZxXHPzCdMMO5RYbgbh2cPCq8uHh1Y4fQgpi3c9U3hZYnVNnGGnmdr-YGq2ga-cw0gG90YLL3uYsurT1NX6mnv1323HWle_7TPVFJMCIVme1jw7oNYs0e3bZFBBaF4lAHDC9wipWZNUHWoiHQCSXWav9_2ablWvORuY1UfYiwzxaMiZNKTOzLl29pg9y3VbESwEK62Yz1RuXqQGVEHtJ6OwFmUWPTpFEjJrulycYFIt3yg2xi4t-1xBHQZG_DZ1NtKAj3MNXmTNP7iySX0sEKeuQhdVKgppqDuvTs9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به آهوهای ایرانی هم رحم نکرد
🔹
درپی حملات آمریکا به جزیرهٔ خارگ، تاکنون تلف‌شدن ۲۵ آهو تأیید شده است.
🔹
معاون دفتر حفاظت حیات‌وحش سازمان حفاظت محیط‌زیست می‌گوید که آمار تلفات حیات وحش مربوط به مناطق خارج از محدوده‌های نظامی است و تلفات واقعی بیشتر از این میزان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/441790" target="_blank">📅 15:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441789">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baeb39f02c.mp4?token=NLbj67GPgEvcCGHW6v9TZY7m8nkhiqhxFXzNmGmdEGedgEjI7_QSvJXXiv92XLVhxLiFXL1lQH8I5Ib635ho5uC1XZ6QPW6GqbPjLKjn35brpdhMN8bDJNHBye1ZxCrwm5nkVLN1HyQdPL3_tj_M9FjRdhvZ28Q94FVNuhZdclzCP1UfZEUUALTZDZu2AkVHQvN9jeg3SOmgPFh7T7B-4pd_jnCWHF7Iuf4AAVeQPAQkzSLryNv7F968L85_Vj5qwCpjpPUfTCI5e9uSzwJDEjGvgz8dPxVq1BKwi6W1Rp-0xi8MASkDwZiJeA2u6LwzwWsm32PyND1nV7O2Uyd1Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baeb39f02c.mp4?token=NLbj67GPgEvcCGHW6v9TZY7m8nkhiqhxFXzNmGmdEGedgEjI7_QSvJXXiv92XLVhxLiFXL1lQH8I5Ib635ho5uC1XZ6QPW6GqbPjLKjn35brpdhMN8bDJNHBye1ZxCrwm5nkVLN1HyQdPL3_tj_M9FjRdhvZ28Q94FVNuhZdclzCP1UfZEUUALTZDZu2AkVHQvN9jeg3SOmgPFh7T7B-4pd_jnCWHF7Iuf4AAVeQPAQkzSLryNv7F968L85_Vj5qwCpjpPUfTCI5e9uSzwJDEjGvgz8dPxVq1BKwi6W1Rp-0xi8MASkDwZiJeA2u6LwzwWsm32PyND1nV7O2Uyd1Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتتاح آزادراه شهید شوشتری تا ساعاتی دیگر
🔹
آزادراه شهید شوشتری، یکی از مهم‌ترین پروژه‌های عمرانی شرق پایتخت، تا ساعاتی دیگر به‌طور رسمی افتتاح و وارد مدار بهره‌برداری می‌شود.
🔹
مدیرعامل سازمان املاک و مستغلات شهرداری تهران: پروژۀ آزادراه شهید شوشتری که از اواخر دهۀ ۸۰ آغاز شده، نقش مؤثری در کاهش ترافیک سه‌راه افسریه و بزرگراه بسیج خواهد داشت.
🔹
قطعۀ نخست این پروژه به طول ۹.۳ کیلومتر، از بزرگراه امام رضا(ع) تا بلوار هجرت، تا ساعاتی دیگر به بهره‌برداری می‌رسد.
🔹
سپهبد شهید موسوی فرماندۀ وقت ارتش، در آزادسازی بستر اجرای پروژه و پیشبرد کمربند شرقی تهران همکاری مؤثری با شهرداری داشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/441789" target="_blank">📅 15:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441788">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9ZCmNNd8LHVlP4Yohrdasn6A8KqxzfrJjfUSkTTfJpMpTMoA6pe8nfbM96YOXgv-MgebdJhYM9MluDA_r1lqMjeQsR0wbYkuqOxzAp5eHL1oGV1DWLzZF5IyUXfHzYIPmVSRaWQ2VvC7rD3IEoxz7_zlvlnM3DuGb7j1l1_Ad31-PsP3T7-emo2iKoaqt04ufzJ5LJFrm8ai8V-nDoOebrRhc2lxlen_zUHLFANKUNpEoys0tiLXJZBYTXy09VBaEJeM-T2-8ADJJ4SS0t916Bg88DB68oRjt8XeeXmLZ9uJgHeQJCGi6Cecy9_xyUjiOnqqertKbY1Y843iqelag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حمله به یک کشتی در تنگهٔ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس: یک نفتکش در ۶ مایلی شرق عمان هدف اصابت یک پرتابهٔ ناشناخته قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/441788" target="_blank">📅 14:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441787">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc596f18b1.mp4?token=bVCtlB513hE1ZywxRMjwPg3reSr7ZR3M8U48eDEkwHAniZxvpLETC_1JgsvbgGwiVllgjMFrwfgWX4ZPL8v3RpQnsp2TTYmanhxctg0VTfSTWpo7XKJjDJ85OWQjj2NOXNzdNNRgEf4iqIm5tfqr1MgCgyNWMLLHUg25a3NF27UqMNU__ajYVLQP5IwIVaMBrbQQEV-SzH9Zge3BjPDD2GoDlmUvQVelo0yTf29knsoleiupTt0JQJuZJ6ord1jGRJ9_5mpLD8cyaXq-Cf72TgjVjxrXOtEFP9ICbiCWd2jXSbnGYlNX1Iy-0hxbzQ0m6OyiBU0Sen4Q8MUgZM-pMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc596f18b1.mp4?token=bVCtlB513hE1ZywxRMjwPg3reSr7ZR3M8U48eDEkwHAniZxvpLETC_1JgsvbgGwiVllgjMFrwfgWX4ZPL8v3RpQnsp2TTYmanhxctg0VTfSTWpo7XKJjDJ85OWQjj2NOXNzdNNRgEf4iqIm5tfqr1MgCgyNWMLLHUg25a3NF27UqMNU__ajYVLQP5IwIVaMBrbQQEV-SzH9Zge3BjPDD2GoDlmUvQVelo0yTf29knsoleiupTt0JQJuZJ6ord1jGRJ9_5mpLD8cyaXq-Cf72TgjVjxrXOtEFP9ICbiCWd2jXSbnGYlNX1Iy-0hxbzQ0m6OyiBU0Sen4Q8MUgZM-pMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اختلال در خدمات ۴ بانک کشور/ تلاش برای فعال‌سازی سامانه‌های پشتیبان
🔹
از صبح امروز خدمات الکترونیکی برخی بانک‌های کشور از جمله ملی، تجارت، صادرات و توسعه صادرات با اختلال مواجه شده.
🔹
این اختلال در بخش‌های مختلفی از جمله موبایل‌بانک، اینترنت‌بانک، خودپردازها،…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441787" target="_blank">📅 14:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441786">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c58291e3d.mp4?token=tNH6DrrfYbgRFarlXyLHjGcZKOCL2McBiKN-Tj0xAsvCzlVQgZ_6n9IHtqSzDcl9C0lDWLJ3yObmOy3XcsP5-Lqp73QpNa-p13Azp-Nij6RY3I6HehSxq8E2a9KAxd-DQNO_qH-2GWo78nrag6JhMZxc_2KoePcZar8Xqnr8J9lIxgBKHf0oQbCc3Win07AYp8upNTG_uagyWO1miNFeCb1UG1-rAOUTaaNZ1O2T-fqsLIT2tiH5F1EjeoEM6tEVbsO-iKmyzH4XFCKwWY4paFvwa75pVZVP1jZA8chRD1BJpB-almsjk0A4qYJz2a1UGs7LSN6AZr0-YUWcLgd4wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c58291e3d.mp4?token=tNH6DrrfYbgRFarlXyLHjGcZKOCL2McBiKN-Tj0xAsvCzlVQgZ_6n9IHtqSzDcl9C0lDWLJ3yObmOy3XcsP5-Lqp73QpNa-p13Azp-Nij6RY3I6HehSxq8E2a9KAxd-DQNO_qH-2GWo78nrag6JhMZxc_2KoePcZar8Xqnr8J9lIxgBKHf0oQbCc3Win07AYp8upNTG_uagyWO1miNFeCb1UG1-rAOUTaaNZ1O2T-fqsLIT2tiH5F1EjeoEM6tEVbsO-iKmyzH4XFCKwWY4paFvwa75pVZVP1jZA8chRD1BJpB-almsjk0A4qYJz2a1UGs7LSN6AZr0-YUWcLgd4wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ نام خود را روی همه چیز گذاشته است
🔹
ترامپ که پیش از ورود به سیاست، به عنوان تاجر نیویورکی نام خود را بر ساختمان‌های تجاری، زمین‌های گلف، استیک، آب معدنی و حتی دانشگاه خود زده بود، اکنون این رویکرد را به سطح نهادهای ملی و دولتی رسانده است.
🔹
ساختمان‌های…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441786" target="_blank">📅 14:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441785">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06a04b797.mp4?token=NOEufgLtWUJbxvS-a46_dPqo2IwwoEvkevEYMWYRAMOoP5VDFtx468XWa1cKoKCcZ-pQwzfAkNyxECp8Pg2lZvu7gJkTWO9MGkKJdexUaqqMuqJoEi7tZm8kHWDDNz9-2Dds_NR9R1_T03NU2NtNd1ukbA7ddjcslIA8nciSaxX7q2tQfz1eM-7cFlqiLAMiJ6LxXDYLK3yyS_aGmSQHkF-EJOkpSuTSaY5N2zsMlSd1LcWOGeSSPUbglk4525Rsbj0bG7iRA0tdQ5xW8xr8tvRv6PNHtIPLSq77xDtvXYke6ail5QVO3x6oiEVYD8FR_nBKwmZpoNKIxlCKb27aqTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06a04b797.mp4?token=NOEufgLtWUJbxvS-a46_dPqo2IwwoEvkevEYMWYRAMOoP5VDFtx468XWa1cKoKCcZ-pQwzfAkNyxECp8Pg2lZvu7gJkTWO9MGkKJdexUaqqMuqJoEi7tZm8kHWDDNz9-2Dds_NR9R1_T03NU2NtNd1ukbA7ddjcslIA8nciSaxX7q2tQfz1eM-7cFlqiLAMiJ6LxXDYLK3yyS_aGmSQHkF-EJOkpSuTSaY5N2zsMlSd1LcWOGeSSPUbglk4525Rsbj0bG7iRA0tdQ5xW8xr8tvRv6PNHtIPLSq77xDtvXYke6ail5QVO3x6oiEVYD8FR_nBKwmZpoNKIxlCKb27aqTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آبروریزی گستردۀ سلطنت‌طلبان در خارج از کشور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441785" target="_blank">📅 14:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441784">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d5fc3535.mp4?token=VKrZ62DRXQpUHyoPjLB1gvoIwiSg0WcsxvY-UvZEc5kEWcHrTDGcigeae4ivHLrR6noxkIyumRFXCtjmjkDLfWi2b7OA_LBx7SopKQWLfZE7HTgiMJpCvI5YyQ_emyyIsFqXGoW-kpzb0sS7LCUs_l4qY3UNZWm2q7IiZQY5UMU73ePC79xHHCj-HuZH9szTSoDEH-bHqVtF5qKlkCjxdcmD93tonhRA5NCGE3J1SxDC_vhmWfpbrDyip3xia2P0x0gzcnLgxlKI9109QxNl9So_WXGeZnFKM9kS9qUokZT0D8-XRwoN-qcS-Eps94nWKpDN0zXxdAPfsWrkLWnTGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d5fc3535.mp4?token=VKrZ62DRXQpUHyoPjLB1gvoIwiSg0WcsxvY-UvZEc5kEWcHrTDGcigeae4ivHLrR6noxkIyumRFXCtjmjkDLfWi2b7OA_LBx7SopKQWLfZE7HTgiMJpCvI5YyQ_emyyIsFqXGoW-kpzb0sS7LCUs_l4qY3UNZWm2q7IiZQY5UMU73ePC79xHHCj-HuZH9szTSoDEH-bHqVtF5qKlkCjxdcmD93tonhRA5NCGE3J1SxDC_vhmWfpbrDyip3xia2P0x0gzcnLgxlKI9109QxNl9So_WXGeZnFKM9kS9qUokZT0D8-XRwoN-qcS-Eps94nWKpDN0zXxdAPfsWrkLWnTGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیش از ۱۰۰۰ نفتکش منتظر اجازۀ ایران برای عبور از تنگۀ هرمز
🔹
صیادی در تنگۀ هرمز ممنوع است و مذاکرات بین ایران و عمان براساس قوانین بین‌المللی برای عبور کشتی‌ها در جریان است.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/441784" target="_blank">📅 14:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441783">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxrNMZP-o1da_HR-GM7ugUJJJMY5Olc56JWCxK50-Tt7Ubl32RlSS0Mdlso33seiEjHc-uhNlXLnZ0pCwMI9TEF6E8ntaNnhHQ3GmEP1jTBoWOxoyVN9l8RKvLsmsiGmrkShTZsnMPuQ_Ch9nJQpDJ9tTbDiXnFK7VG9lFj9abFf89iaFQP2dgDLku8GNiDb3lpavH4oRLIqZxhXQiuRjQY15zxp4Wi5gM64CoWn5LgjZq5NXASk38sByGNghauDOdDwxwVxqPW1yqIet2dMewKP64qu5HEZzwcPdbZ7bobQZlQB6U9oXB7oyUtQSjpM7qdC0ghBxxT7o8N57gjvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ جزئیات مراسم وداع، تشییع و تدفین رهبر شهید انقلاب اطلاعیه شماره ۳ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه  بسم الله الرّحمن الرّحیم «مِنَ الْمُؤْمِنِینَ رِجَالٌ صَدَقُوا مَا عَاهَدُوا اللَّهَ عَلَیْهِ…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/441783" target="_blank">📅 14:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441781">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🖼
تا دقایقی دیگر، جزئیات مراسم وداع، تشییع و تدفین امام مجاهد شهید حضرت آیت‌الله العظمی خامنه‌ای قدس‌الله نفسه‌الزکیه با صدور اطلاعیه دفتر حفظ و نشر آثار رهبر شهید انقلاب اسلامی اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farsna/441781" target="_blank">📅 13:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441780">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLvRBL3vZyJ6vGwoLBUH5Ck8tV-eFtZDLsps4j7CuNCEO0bJPASci2CfE2LqEQU-yBFm_ZRypjtHwHh34jkBb9tFZhA06itoFM5LGC692YC-PzvPKhd_rSohP-MCRnS5rn3tLsikzQSarM8DkTMerVRsewvoafRfjPmJCDP1JqtV45gohTQ3xyb7NLLaZA8nrh09hN-92SJJl3qWD3GyhvxkiM-weALINH-5VrLRV85L2Etl_W3SzqqxK0hgjmb-X257nl3qFlsF86k0KbUQpwUbN9bw1RnOt5Nf-Ah6bRNqUBtgUZ30Z76rSQ84ztPSEdQcgcUPdIWgq9HO0y80VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: ‏به تأسی از شهدای جنگ ۱۲ روزه، تا پای جان برای  پیروزی نهایی ایران عزیز ایستاده‌ایم
🔹
یک سال از آغاز اولین دور از حملات جنایتکارانهٔ رژیم اسراییل و آمریکا به خانهٔ ابدی ما ایران می‌گذرد؛ کودکان بی‌گناه را به قتل رساندند و از هیچ جنایت و قساوتی پرهیز نکردند.
🔹
‏به تأسی از شهدای قهرمان و مظلوم جنگ ۱۲ روزه، تا پای جان برای سربلندی و پیروزی نهایی ایران عزیز ایستاده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/441780" target="_blank">📅 13:53 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
