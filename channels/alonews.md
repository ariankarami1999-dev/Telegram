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
<img src="https://cdn4.telesco.pe/file/VnP8xr8Ny-QGA0GhN77_Sw9J7tY65fzCyMcbaReYguqvlv6v2eS0cpF8UU-zcm-Uvv1D4OjsTZy5ZQ0ZqwQgK1VhcRHhoayr045z7oEMSPdjZFieyZCoKUswco_2W7C4CT958u5h-ZqRkiCvAirHEVNNcLDmQMGJIgVgZmCaRcvuMTdruilEarUF6IYGL4aftOlBIgrlBg3kn8CHOjLLl1fDSmGUejK0i1o1bMGRkm3-itWurDYEBDS1ebRf2d_7Nhaz77w21kpQFDERAwwws50qWKM-wLI8yJjIVG6Or5fpKPVOu9dS4Wog0_PJ8P6mjGEKW2txnuYAfP8TSpkIvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 933K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 14:07:51</div>
<hr>

<div class="tg-post" id="msg-130660">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgG9Aj3wBBiew120pyLNMzjTT0vKM-THEPK6I0q4vkgamkQgtnLgFjFYJRH6X_7njyiQtG4he_rO6Qm1ekShZ3NuT0jG4iD6_fTTyru95eTuupC_hKQVNi5aOKsl76oVh2mf_mucN7wQpqIBUjyrxNfwOvf4QNLEECORP0mbobuZM-lQGIkKNuVqVyF_FKuWYZgz2ZZLlXEUo2M0JdoSpKaiKShZEHXeWn0yQMX1nDnzM8ZiECjpnp0xy6_Fzy3rmb8crrUfbDqNWzhumAfyJob_BDsQg6CMMZwx2TDJkkLfiTDRcQQS8dE8X7S4UmW-Kddm4da6qzPiN4s0IVNrxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر اسرائیلی، الی کوهن، می‌گوید دولت جدید راست‌گرای اسلوونی به رسمیت شناختن فلسطین را لغو کرده و سفارت خود را به اورشلیم منتقل خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/alonews/130660" target="_blank">📅 14:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130659">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337aefd3c4.mp4?token=vyx4_KN-wXDgQx2EBTpdSUROBNtY5VQBpqfIk9D6wfvy09Blwkk_M-LNLBoBdV3zPol09MnotMQ-P5GX1eZSk4xHB0MH-67CPiE0WR4xdDKG1OF0pNfjoyZH-w-AC8aSGUnoBibr4KDMVkS1nHEh_-1HDyHBLlLD2KnrUrBh5VlWOXQ6ypsngVRvEf1WZTXsq7YO9_qfaquUe9Calrr1TI9sTmROt286X9W_qK3Snw5OSNM-OsR2ntNhNZOB5fEAwIjVISqSoUBY9cM5PKoo7gWatXcPfj9_O7eMc6BjsXeZk13x1CGrXSIZW_LGaD4xxN8sSzhJt-yUt8D0urrk_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337aefd3c4.mp4?token=vyx4_KN-wXDgQx2EBTpdSUROBNtY5VQBpqfIk9D6wfvy09Blwkk_M-LNLBoBdV3zPol09MnotMQ-P5GX1eZSk4xHB0MH-67CPiE0WR4xdDKG1OF0pNfjoyZH-w-AC8aSGUnoBibr4KDMVkS1nHEh_-1HDyHBLlLD2KnrUrBh5VlWOXQ6ypsngVRvEf1WZTXsq7YO9_qfaquUe9Calrr1TI9sTmROt286X9W_qK3Snw5OSNM-OsR2ntNhNZOB5fEAwIjVISqSoUBY9cM5PKoo7gWatXcPfj9_O7eMc6BjsXeZk13x1CGrXSIZW_LGaD4xxN8sSzhJt-yUt8D0urrk_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلزله ونزوئلا؛ تصاویری دردناک از لا گوایرا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/alonews/130659" target="_blank">📅 14:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130658">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
اسماعیل کوثری، عضو کمیسیون مجلس : شعار مرگ بر آمریکا عبادته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/130658" target="_blank">📅 13:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130657">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8jTrIHGMjfjOmYeip9G_joF_ZE7xPTyYnael3_flAzyM9To93rHL6_DUPH8hwucIyfQPfT1YfQ5uSuA59fmi-KMdEeJykPbsk_4gFus7LC2i0Bxk1IymPeT7jMw2J_wCmjsY6HDONWdfc4zSxKycRiMPbBPF-cAv5GK2mO50ks3Y2LZFKwkaZBGFv3K7UuCDwHM6BOKEPm0Quq-YTEAqQhCxw4UkDC3uxrNN0syESdykQZN7jbw0a6zhBh39WX-LcNWGAiG6OI_CsWWD7Asq58DKaknvvm2B1XhvWXo8WKI211OkPXVVA01-urcO9YXpIrQHcRaVBYHjemHJ4LIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری پربازدید از  اقامه نماز در رختکن تیم ملی فرانسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/130657" target="_blank">📅 13:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130656">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
شهردار منطقه ۱۰: ساخت اولین پارکینگ پناهگاه تهران در یکی از مناطق پرجمعیت و پرتراکم تهران به اتمام رسید و بزودی بهره‌برداری از آن آغاز می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/130656" target="_blank">📅 13:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130655">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6b806d95.mp4?token=jMZS9Rkk9MKcoBumvle5CElQ95ig6aYv44SBC_2gPLevRWG_LytqHl2izGy69RuX_DpBNgSDXQBV9IebhNE5ueJVMqxSubLk3PFpl0KckzoX-4ySV5LBeCbl1KI-__dIwidjH1552lE9oWzrPJiDAJJR-GNJJ5vkyFBgfmx58xIOpk_93GxhEtyI5HPb6AbZENo0jrVbSJgDXQkT39TsOo0mBiGjpIpGRJ6v18mVLTkGbaMSJN8hb2vH2J4_BirwB1K2lFK7XaTQPyoIRyaAPQlIP89bbab5YRqXsmZ-25ShMdb7PwOE2jKIzSlHifzuKUx-_Un3Zhm4V8FHEhuQiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6b806d95.mp4?token=jMZS9Rkk9MKcoBumvle5CElQ95ig6aYv44SBC_2gPLevRWG_LytqHl2izGy69RuX_DpBNgSDXQBV9IebhNE5ueJVMqxSubLk3PFpl0KckzoX-4ySV5LBeCbl1KI-__dIwidjH1552lE9oWzrPJiDAJJR-GNJJ5vkyFBgfmx58xIOpk_93GxhEtyI5HPb6AbZENo0jrVbSJgDXQkT39TsOo0mBiGjpIpGRJ6v18mVLTkGbaMSJN8hb2vH2J4_BirwB1K2lFK7XaTQPyoIRyaAPQlIP89bbab5YRqXsmZ-25ShMdb7PwOE2jKIzSlHifzuKUx-_Un3Zhm4V8FHEhuQiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع انفجار در تل آویو
🔴
منابع خبری گزارش دادند یک خودرو در منطقه «حولون» در تل آویو منفجر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/130655" target="_blank">📅 13:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130654">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
الشرق نیوز سعودی به نقل از منبع عراقی: نیرو‌های امنیتی عراق اقدام به بازداشت سیاستمداران مرتبط با پرونده‌های فساد در منطقه سبز کردند
🔴
الحدث به نقل از منابع آگاه: ۱۷ مقام دستگیر شدند؛ از جمله معاون پیشین وزارت نفت عراق و رئیس یک فراکسیون پارلمانی که متشکل از ۱۹ نماینده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/130654" target="_blank">📅 13:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130653">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43c16a967.mp4?token=d-1n91v9IYBEf2kzmWVn-QgrDpM5_s-Q-0kiYsLm6ya4Q9DED4Ti5e_7Mv9SBjE4yE7x0oamVWzV6rrJHczPLHP3Cdpu2uuPaWEygUb8vsMq2Mr6sF8jsX3emLOp1ETQcbgIpj0saXnWa2EEuNYj5iAV1yVPM3axkC1V9fkV_geEOdlS4nuKTa0lVgIh2Ihlg_4Il7buQxbC-d8Y9pcIR4jyYdD84tS3d7rMlDUqiARMMLtqPqdpHLpjuzDkbs1VTuoUj07Ds-klYh32w1-YYmKOS8W_hcq4OfT31N0Ybgbzo1W4b6b_vFPzz-GlWUt_adbm-xtsQDvkMnkB42xGOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43c16a967.mp4?token=d-1n91v9IYBEf2kzmWVn-QgrDpM5_s-Q-0kiYsLm6ya4Q9DED4Ti5e_7Mv9SBjE4yE7x0oamVWzV6rrJHczPLHP3Cdpu2uuPaWEygUb8vsMq2Mr6sF8jsX3emLOp1ETQcbgIpj0saXnWa2EEuNYj5iAV1yVPM3axkC1V9fkV_geEOdlS4nuKTa0lVgIh2Ihlg_4Il7buQxbC-d8Y9pcIR4jyYdD84tS3d7rMlDUqiARMMLtqPqdpHLpjuzDkbs1VTuoUj07Ds-klYh32w1-YYmKOS8W_hcq4OfT31N0Ybgbzo1W4b6b_vFPzz-GlWUt_adbm-xtsQDvkMnkB42xGOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عباس عراقچی: هرگونه دخالت و هرگونه تلاش برای اتخاذ ترتیبات جدید یا جداگانه از آنچه ایران در خصوص تنگه هرمز در نظر گرفته است، تنها وضعیت را پیچیده‌تر کرده و بازگشایی تنگه را به تأخیر می‌اندازد و تنش‌ها را افزایش می‌دهد، همان‌طور که در دو شب گذشته شاهد حوادثی در تنگه هرمز بودیم که منجر به افزایش تنش‌ها و درگیری‌ها شد.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز و ترتیباتی که جمهوری اسلامی ایران برای بازگشایی تنگه اتخاذ کرده است، دخالت نکنند، به یادداشت تفاهم امضا شده پایبند باشند و اجازه ندهند این یادداشت از مسیر خود منحرف شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/130653" target="_blank">📅 13:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130652">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
طبق گزارش روزنامه هاآرتص، سامانه‌های دفاعی اسرائیلی به قطر و عربستان سعودی فروخته شده‌اند؛ با وجود اینکه هیچ‌یک از این دو کشور روابط دیپلماتیک رسمی با اسرائیل ندارند
🔴
اسناد و تصاویر نشان می‌دهند که هواپیماهای سلطنتی قطر به سامانه دفاع موشکی C-MUSIC ساخت شرکت Elbit Systems اسرائیل مجهز شده‌اند؛ سامانه‌ای که برای محافظت از هواپیماها در برابر موشک‌های گرمایاب طراحی شده است.
🔴
همچنین شرکت‌های اسرائیلی در برنامه جنگنده‌های F-15QA قطر نیز مشارکت داشته‌اند و قطعاتی از جمله کلاهخودهای رزمی JHMCS و عینک‌های دید در شب AN/AVS-9 را تأمین کرده‌اند.
🔴
عربستان سعودی نیز از طریق برنامه F-15SA شرکت Boeing تجهیزات مرتبط با اسرائیل دریافت کرده است؛ از جمله صدها کلاهخود JHMCS و عینک‌های دید در شب.
🔴
ارزش فروش کلاهخودها به عربستان سعودی به‌تنهایی حدود ۱۰۰ میلیون دلار برآورد شده است، در حالی که قطر جداگانه ۱۶۰ کلاهخود را در قراردادی به ارزش ۳۵ میلیون دلار خریداری کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130652" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130651">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f694ed771b.mp4?token=jYt23inqLuPMpt-iqNB0TrdDA3M86xvHN1wcmUOD48sbIBQP76o-Bx1Tv4GccL0rUqNxUdQN4LqVW1YnYj5twKx9QNABNVyBALEq42yVrRnFMYH7eVGHBbNHj28e-gVlDqAxsMf-pZppkLEWKdAXYMwVtTsi9-QbeOmTGY2EvVNucMRdmha1ewYyW_1DuWDOal3Ma_vi50G5v_tDM0zV3XtgmBo9fEkbLG7wkeOpgmdKdnlPXtA_SdPuXs9gEfw7VE00JragQWidCt_3_ik5vd53QbbMApayiERIMDARTl1SsdyKAYKRBJ-cBssiZjOwjbz3E0-BoSGm15wz838FhjXXGujrWr7XNx9uLtdbZKriyKOU64uUJASEVW30188g_Ls5T0yqIDyVveLBW9T7gp78VLXz371aZqVVjCbGbJgyjFwOkN7uiYeuPrE_dJsERRh0RWELfuMnJ3MThJqGNFiCNspjL4AZmWpKcV-5MjosuF616MN79tAzm-gmH7psCunFWM_lMtH_Mkzv0mIr4bYlHIB-oAeBb34HY8u49HwJH0YRZR3Q3UYiXalKvJwPYf-FQiAwDl-l7j_xLEii-tFGmnPSgLcoRZ7vGTNJGFFqbbUiQBuA4lcQQU4w60fjHDZYmWsA09IHWv6zZGLrY97_DZqHhfEv-7twXykCUlo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f694ed771b.mp4?token=jYt23inqLuPMpt-iqNB0TrdDA3M86xvHN1wcmUOD48sbIBQP76o-Bx1Tv4GccL0rUqNxUdQN4LqVW1YnYj5twKx9QNABNVyBALEq42yVrRnFMYH7eVGHBbNHj28e-gVlDqAxsMf-pZppkLEWKdAXYMwVtTsi9-QbeOmTGY2EvVNucMRdmha1ewYyW_1DuWDOal3Ma_vi50G5v_tDM0zV3XtgmBo9fEkbLG7wkeOpgmdKdnlPXtA_SdPuXs9gEfw7VE00JragQWidCt_3_ik5vd53QbbMApayiERIMDARTl1SsdyKAYKRBJ-cBssiZjOwjbz3E0-BoSGm15wz838FhjXXGujrWr7XNx9uLtdbZKriyKOU64uUJASEVW30188g_Ls5T0yqIDyVveLBW9T7gp78VLXz371aZqVVjCbGbJgyjFwOkN7uiYeuPrE_dJsERRh0RWELfuMnJ3MThJqGNFiCNspjL4AZmWpKcV-5MjosuF616MN79tAzm-gmH7psCunFWM_lMtH_Mkzv0mIr4bYlHIB-oAeBb34HY8u49HwJH0YRZR3Q3UYiXalKvJwPYf-FQiAwDl-l7j_xLEii-tFGmnPSgLcoRZ7vGTNJGFFqbbUiQBuA4lcQQU4w60fjHDZYmWsA09IHWv6zZGLrY97_DZqHhfEv-7twXykCUlo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، خطاب به ایران : به شما ربطی نداره هیچ جایگاهی اینجا ندارید
🔴
نه شما، نه حزب‌الله ،هیچ نقشی یا حقی در این موضوع ندارید
🔴
اسرائیل و لبنان هم بر سر دو منطقه نزدیک به خط آبی (مرز) که من پیشنهاد داده بودم، به توافق رسیدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/130651" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130650">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نتانیاهو : توافق ما با لبنان ضربه بزرگ به ایرانه
🔴
ما این موضع رو حفظ می‌کنیم تا وقتی که حزب‌الله و بقیه گروه‌ها خلع سلاح بشن و دیگه از سمت لبنان هیچ تهدیدی متوجه اسرائیل نباشه
🔴
ایران سعی داشت ما رو مجبور کنه از جنوب لبنان عقب‌نشینی کنیم
🔴
این خواسته‌ها رو بارها شنیدید و ناراحتی و انتقادشون از توافق، هم از طرف ایران و هم حزب‌الله، رو هم دیدید
🔴
من روی منافع حیاتی اسرائیل ایستادم و با این ایده که بخوان ما رو با زور وادار به عقب‌نشینی کنن، مخالفت کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/130650" target="_blank">📅 12:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130649">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpgpILB9FbMmEHSF0caX_57QE5Pc7zKDSj0XXmSqbnCPXaCIwYKIHvU_CXbAPOU_bJi_qGqzVdeX2ua89mefT6UDE3NAGd10m4o9S8IdHpa-ZaXWSsNVgBMhBhMrjOdUGtUMm8fmaa-rlSQ8k7_3TvOI716IfvGGbmmLrKMw9lFTL9FIIVjZ8tevtjJkx9wY3NIyK6rMJBZaOSYEuQKzcf7BDh5g0fIUNs7uG7HGeztsvibJkt677pabpfQVUeClPZ_1CvvtbI_jdj876OPFWuPaNpbGQZMI32mmZp_vZeSojFSgfFFdlpvNSFe214rlgoi-sjdfRIVeEZIYD0ZxKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریزش ۱۰۰ هزار واحدی شاخص بورس
🔴
شاخص کل بورس با ریزش ۵۳ هزار واحدی در پایان معاملات امروز به ۵ میلیون و ۰۷۵ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/130649" target="_blank">📅 12:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130648">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
عراقچی: مسئولیت ترتیبات تنگه هرمز با ایران است و هیچ نهاد یا کشور دیگری در این خصوص مسئولیتی ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130648" target="_blank">📅 12:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130647">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=iwPXcaw65Ax166R_o_hi5Hcu8P7t5rNcwHL3q4QJziNi7HqewswH2KG7PCviZosOQYtBNWoiVU3YEO4vbiY1X8k1KveX8lqsZdIMGHCkCurvVMkeWE73ju87temEXbTtRLWD8yVDBcLQnXN3JO5OwYIc5i06-wzjfdP03AmnN8vhIL_j1laPYy5brfxxlUvaxpxzhYWmAgvpV1kqMgHRkQ3qr2c7oipQektNfsdIdoqGz6VjJ38VAfJamIU1tuY9sFccW764QIz77aHbePnIDKGYdosS30zfzTlD-VP-iBpjEggt0WHnZ8AdjF_u-9SgH3y1ULTqbulxn2i18vDM6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=iwPXcaw65Ax166R_o_hi5Hcu8P7t5rNcwHL3q4QJziNi7HqewswH2KG7PCviZosOQYtBNWoiVU3YEO4vbiY1X8k1KveX8lqsZdIMGHCkCurvVMkeWE73ju87temEXbTtRLWD8yVDBcLQnXN3JO5OwYIc5i06-wzjfdP03AmnN8vhIL_j1laPYy5brfxxlUvaxpxzhYWmAgvpV1kqMgHRkQ3qr2c7oipQektNfsdIdoqGz6VjJ38VAfJamIU1tuY9sFccW764QIz77aHbePnIDKGYdosS30zfzTlD-VP-iBpjEggt0WHnZ8AdjF_u-9SgH3y1ULTqbulxn2i18vDM6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
‎
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130647" target="_blank">📅 12:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130646">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
عراقچی: آمریکا موظف به توقف حملات اسرائیل و اجرای آتش‌بس است
🔴
بر اساس بند نخست یادداشت تفاهم، جنگ در تمامی جبهه‌ها از جمله در لبنان باید به طور کامل خاتمه یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/130646" target="_blank">📅 12:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130645">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/487cb1c4d0.mp4?token=npHx8vGpcXgIb1aFZR821vXobNeOcM3E2sbUAb5UpL3qlkVLe_wSyoKk3JU8kvkXpHlyCRZ7A6kpfQe_K0f8aBH9ViqewZRqmEJNDGLKt5XZnWfHTW2OfYU1pVNCOR0RmRxI6r0N9oEZgqjECcKg0at5gCq5RFPb4o9Xy1PBBP0txF-NsM9r5EhblldfcElEO8a3RMlODDDG_qvv8p5GymqbEolpdydQHNwfLf6c51iPW2PSujBX3jVAqchmKy11iEjHf_Aq5ZJtPSYzwIuvix4k5gs26435k8THN-RrlhXXVboHSlAzslwoA2mXNIEmhhNbXZNAZPmNBu9whClg0YvG_ltjMLNEEpKBhVStAez68ZFf7zLH-zrhvFCc0PYhA4VJPO-KG7VTjvhE_nAJI-E0aILpYYGsRuJz-_6cZ3mVHGmfW7A1VgIjlEevpP3E5kfVtquzDPEtlyl6vanSoMirUzt1ftRTI7H4upEsvh0glX7KBKlDLx8mwvdDV53lDHEacP3aDPRrhelUa-JbQQbPhR4dVuqtiDCtBR-cEfKEJ0PeHItWyNtXyJhRvshcLD2pMGUfdHbS1v_D0e9ENLj9_k_B1fjcjkZSD0ctYs3Sy1uhbjkjeZ20G6wsG9XleTA9IAduuBLjtXAa56Uadubhv_SZ5SvtJkdhc-3zUe0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/487cb1c4d0.mp4?token=npHx8vGpcXgIb1aFZR821vXobNeOcM3E2sbUAb5UpL3qlkVLe_wSyoKk3JU8kvkXpHlyCRZ7A6kpfQe_K0f8aBH9ViqewZRqmEJNDGLKt5XZnWfHTW2OfYU1pVNCOR0RmRxI6r0N9oEZgqjECcKg0at5gCq5RFPb4o9Xy1PBBP0txF-NsM9r5EhblldfcElEO8a3RMlODDDG_qvv8p5GymqbEolpdydQHNwfLf6c51iPW2PSujBX3jVAqchmKy11iEjHf_Aq5ZJtPSYzwIuvix4k5gs26435k8THN-RrlhXXVboHSlAzslwoA2mXNIEmhhNbXZNAZPmNBu9whClg0YvG_ltjMLNEEpKBhVStAez68ZFf7zLH-zrhvFCc0PYhA4VJPO-KG7VTjvhE_nAJI-E0aILpYYGsRuJz-_6cZ3mVHGmfW7A1VgIjlEevpP3E5kfVtquzDPEtlyl6vanSoMirUzt1ftRTI7H4upEsvh0glX7KBKlDLx8mwvdDV53lDHEacP3aDPRrhelUa-JbQQbPhR4dVuqtiDCtBR-cEfKEJ0PeHItWyNtXyJhRvshcLD2pMGUfdHbS1v_D0e9ENLj9_k_B1fjcjkZSD0ctYs3Sy1uhbjkjeZ20G6wsG9XleTA9IAduuBLjtXAa56Uadubhv_SZ5SvtJkdhc-3zUe0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گرمای شدید در فرانسه باعث بیهوشی راننده اتوبوس و تصادف شد
🔴
در فرانسه، یک راننده اتوبوس به دلیل گرمای شدید هوا هنگام رانندگی دچار بیهوشی شد و در نتیجه این اتفاق، راننده کنترل وسیله نقلیه را از دست داد و حادثه رخ داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130645" target="_blank">📅 12:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130644">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7Bjc5bOP5TcrxXCHKG6i1Zu8tTM-7b2ZtuP4-5R16LMKWT1wL0aYuoOhwVbfYJlehTcaLJLP0Y77yi09-xSFJkObjdxOU6vspt2FrcL0kiZkWoIoW-BqUsbBeuKgIbrwtiWLCftjIVaAW3oFoE-uN4PO615m120lFtvyYA17FKbr_TQrN_eHXRXBrKU0b0LpKKU4x3XEEpY9Dvw7MF5l6HqJOeZ-EoYKDvfXqKEiNeyusXDrcG2LVK_NpnBd5Ygj1zYF5Lvc85wY3s70scmiS_T6UefXxIcPmCzRPxTZnUU0IA2dHhW15xr5EDQcUx5rIYZHIcpnE0dEvBCS51Vyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130644" target="_blank">📅 12:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130643">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
قیمت دلار ۱۷۰ هزار و ۵۰۰ تومان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/130643" target="_blank">📅 12:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130642">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
عراقچی در بغداد :  روابط راهبردی ما بین ایران و عراق به طور ارزشمند ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130642" target="_blank">📅 12:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130641">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26a14380ab.mp4?token=UTviY7jE5Gvv5nBRpU0pju0huBbutQZoR3dIIQsquAnNGq5HFdcJaTaqRNtWC2LuwCdqmdRgpF8qnqaYJ7o4fAvcAXarfXCp-zl_aBdAzSn8zh5LnRPMWLr2cCQlodkxLHJasjLIGRnd9XPq8sflygi2jA311tvvPJvGiBArZ8Vo7vAmZ3dd9f03-1DyDnxkbHIanGxMmYjfsjUjzVHAsURA-KSsijbyg0MMCyWOcVflOo-rQGER1nO_dHSXYe6Tc2knfxWYTtuFOKcJG-0Y4gMYfgsphEsOcFyDJ248-3G6iFOZD3Nl67j_8rk4tZs7aN_18VHfGRZ0jVG9UVC4XLww9h1JYMcn_VFSSLRuY5MVk32Vu0uelsCMCNKUBgt6XQ7ODfwobzMJp9w7p2uje6JOeyoIVk2cBmduCEY8rYE5UT_gQ7UnQewrcg7bFuIFDvzGx4dMYZMfoXeQQpBi-TxGoa6x57rtuqLCy-4PdXUaMzaAwD5GmkBKG_hGSw8g5Tik5b6725f5XN99OBHL6-qldSy2GPNtPx4I0i9If6ZLiGLfDkWD2JQoOtRcs1AjMrjKxawYV6xApVOkqVzR1lfosOKYbY5mF3X9MCCX5iQCAqL58bHNSAgw8pURwR4tdCf6CuT2hJTQv9GhUI8R5ZSe8xQ5TEFJLd5_tn_T1OE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26a14380ab.mp4?token=UTviY7jE5Gvv5nBRpU0pju0huBbutQZoR3dIIQsquAnNGq5HFdcJaTaqRNtWC2LuwCdqmdRgpF8qnqaYJ7o4fAvcAXarfXCp-zl_aBdAzSn8zh5LnRPMWLr2cCQlodkxLHJasjLIGRnd9XPq8sflygi2jA311tvvPJvGiBArZ8Vo7vAmZ3dd9f03-1DyDnxkbHIanGxMmYjfsjUjzVHAsURA-KSsijbyg0MMCyWOcVflOo-rQGER1nO_dHSXYe6Tc2knfxWYTtuFOKcJG-0Y4gMYfgsphEsOcFyDJ248-3G6iFOZD3Nl67j_8rk4tZs7aN_18VHfGRZ0jVG9UVC4XLww9h1JYMcn_VFSSLRuY5MVk32Vu0uelsCMCNKUBgt6XQ7ODfwobzMJp9w7p2uje6JOeyoIVk2cBmduCEY8rYE5UT_gQ7UnQewrcg7bFuIFDvzGx4dMYZMfoXeQQpBi-TxGoa6x57rtuqLCy-4PdXUaMzaAwD5GmkBKG_hGSw8g5Tik5b6725f5XN99OBHL6-qldSy2GPNtPx4I0i9If6ZLiGLfDkWD2JQoOtRcs1AjMrjKxawYV6xApVOkqVzR1lfosOKYbY5mF3X9MCCX5iQCAqL58bHNSAgw8pURwR4tdCf6CuT2hJTQv9GhUI8R5ZSe8xQ5TEFJLd5_tn_T1OE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلیپی از شادی بازیکنای تیم ملی‌ تو هتل که امروز فکر کردن صعودشون قطعی شده اما ۱ دقیقه بعد از این خوشحالی، بخاطر گل دقیقه ۹۶ اتریش به الجزیره صعود کنسل شد...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130641" target="_blank">📅 12:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130640">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
در پلی مارکت هم‌چنان بر روی صعود تیم ملی ایران شرطبندی می‌کنند
🔴
تیم های اتریش و الجزایر الان تو آمریکا هستن و برای بازی باید به کانادا بروند
طبق آمار احتمال سقوط یک هواپیما ۰.۰۰۰۴ درصده که اگه این اتفاق رخ بده ایران هنوز شانس داره جایگزین یکی از این تیم ها بشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130640" target="_blank">📅 12:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130639">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
یک منبع مطلع در گفتگو با ای ۲۴ نیوز مدعی شد:  اهدافی که فرماندهی مرکزی آمریکا دیشب در ایران مورد حمله قرار داد، هم اهداف جدیدی بودند که ایرانی‌ها اخیراً ایجاد کرده‌اند و هم اهدافی که قبلاً مورد حمله قرار نگرفته بودند.
🔴
از جمله زیرساخت‌های ردیابی، سیستم‌های ارتباطی، سایت‌های دفاع هوایی، تأسیسات ذخیره‌سازی پهپادها و توانایی‌های کاشت مین مورد حمله قرار گرفتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130639" target="_blank">📅 11:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130638">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ریاست جمهوری لبنان: ما حملات ایران به بحرین و کویت را محکوم می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130638" target="_blank">📅 11:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130637">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
دلار هم اکنون 170,000 تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130637" target="_blank">📅 11:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130636">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سخنگوی ارتش: در خرید تجهیزات پیشرفته نظامی از کشور‌های دوست و ساخت داخلی آن‌ها، برنامه‌ریزی جدی داریم
🔴
قطعاً در روز‌های آینده از تجهیزات پیشرفته‌تری برخوردار خواهیم شد
🔴
پهپاد‌هایی که در روز‌های پایانی جنگ از آن‌ها رونمایی کردیم، بسیار پیشرفته‌تر از نسل‌های قبلی مانند «آرش-۲» هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130636" target="_blank">📅 11:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130635">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeVIele0Txr3J4JDBSHBM1jGhR-GHK4qn7OQPZEN2dXz0t32fdCNmQggQb-i4vZtEPsoqHA0gWuoSQwfuoe02DEKTE-xJMyerwoKKyqqa5kbMPMr_1saDn0n_khJCEncYsUje9CZjFMKF5bO_CWVg3ePaxDorpgg1xdjHeCutgmuvrH2wpqhls7amsGjItJ06BrPuf50H7hdLrpH3ywFtybredGDS0_A8_eqHP349pN674-Jpb6JCtDVToGXBbOYJOPW8JwF7-Bai3tW2v-HXwSQyr1B_BbFHa1FQXflIfBtDEHIdAwZ1CL8FD1epd--CyL2BXhr5TdPK5osEzRbvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رایزنی وزرای خارجه پاکستان و بحرین درباره جدیدترین تحولات منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130635" target="_blank">📅 11:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130634">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
قیمت مسکن در تهران از پیش از جنگ تاکنون ۸۰ درصد افزایش یافته است
🔴
تورج سرباز، عضو اتحادیه مشاوران املاک: با وجود افزایش ۸۰ درصدی قیمت مسکن از پیش از جنگ تاکنون، تعیین سقف ۲۵ درصدی افزایش اجاره‌بها اقدامی منطقی برای حمایت از مستأجران و کاهش فشار بر این قشر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130634" target="_blank">📅 11:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130633">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
جو بایدن درباره ترامپ: ببینید، این فقط تحریف و تخریب عمدی او در ناتو و انتخاب پوتین به جای متحدان آمریکا نیست، یا این واقعیت که جایگاه ما را در چشم جهان بیش از هر رئیس‌جمهور دیگری در تاریخ تضعیف کرده است. این فقط پروژه‌های خودمحورانه‌اش نیست—تخریب بال شرقی کاخ سفید برای ساخت سالن رقص، نصب نام خودش بر مرکز کندی، ساخت یک طاق به افتخار خودش، یا حتی استخدام شخصی برای رسیدگی به استخر بازتاب. واقعاً چه بازنده‌ای.
🔴
ترامپ از زمان بازگشت به کاخ سفید میلیاردها دلار درآمد کسب کرده است. این برای من کاملاً تکان‌دهنده است. او هیچ شرمی ندارد و صادقانه بگویم این برای کشور شرم‌آور است. اما ترامپ اهمیتی نمی‌دهد. کسب درآمد از ریاست‌جمهوری یکی از دلایلی است که او می‌خواهد رئیس‌جمهور باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130633" target="_blank">📅 11:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130632">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAT2YjAOEqWXaSntweAUnYjIY3Hvm3lgpG29ygkbzmxyDXwr6QKdydT2dqlgKCExAdt89V5gc0_1fCT6qMU4SnIyLfro0sXfQ8OFsM2zMwSZkzwOBNg9wSihS-BwAlk-xlgIhJs4ROrtsbFxerxOW1opf-hONm_aYDBeIsP0BaqSS3igVLst35xjeOeDTkZr7Oi9WE5STbOwvPmWnrOsHa3NBnb1m7m3npagOa4reinKumhQDFN7Uakd_Aax42hrX3tlCSV8ji8x3LyFjxM3NQxp9lB9uLpo3bWxFni8O0TATwMh9FAaZiHtpZCur9Nc2vp7ZnPhWI_-CUpRK_GL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استقبال وزیر خارجه عراق از عراقچی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130632" target="_blank">📅 11:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130631">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAP7rNw1ODsNF5Z2EuSErKhXt_Zrp-m53peg4gMzNv-hvQSbhU7dRUz6kJ9eI1LMKrKj0a-NgdUkq5cv1bKaeG1ZZYi3FfGAvY3gGwinukQ5LkAWpZsubBOrSXnrN8icpY-a5ci3bhOeJ6RK0HOaDkaQWqoMJnZwj5BUICvO0fk1aRZsCLBqrTAK1OSenteVCnvnPcPv77cK0kS4l4SlANwSgmAnVg5eO0Ps_oghNjKunUFHYVQPz760i5PUwd3YHf5tP39BnjdDAXj_dtxFIBi-J9QSfpcPymjfb3HZ7fncj-3qWxuR7dZuPJVnRrju9ldt0DshO16rlmb_9UJNzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی ارتش اسرائیل به الخیام در  جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130631" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130630">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2d370498.mp4?token=Aw9UH1eeEtEBT6nXUNutNHIrVMUNonua-m-tB-AXY7vWyNxpp6I-nWfs9_Hr21_q5zWdpMqAXen3ALpj49Tvh9qOgu30zQackLFHIxPkuW4VgE5it7QUys3rj0W4YaZDJQ439uLuZlphW3Nahu6BXC9SwDTI36G9DoONP60HAQUpONKTbrnTK9mn1RBtNDrFd010g-CLKxfcJTnMvSPUL1VgtcX-CAUQLX1WCOZ-fx4GtLCla7kouEjQLMmpnSafMuwk5xzEgN6JNOzq9XJS6mX16FlW9WfGG1963S_gkMdra-PNgf2OligL0nTWg7MyKZ_p3a4m0HOIcIYSqqXspChCgeES4ZgTCWfAe5Fm82QHG4n8isex354pmMdVHyakb30WCMb1WYRJXfdS3qPDhLoaz7F1pPkA4yP_FiOe06QAkLsJ4k78qqK5mUbdPepAxMd8_AUWMh81n3voK8beHNVp1rdr1dsk5OItj_BvOzqVMjV_oXii5cDL1edS9K30QojD9VKhPPl3AqCmGiLC0jZzkno9izWEdoJ3C4B-wQ7KWZvTGZg_dKrSSLY8ooiK55ANyRIXENqkVxo6HXG9XLaSqctxPMb1Lcd2pAwcxDdDB68Bdskr3laOdw_OeqiDnWmitGNSV4Vuuc6ddGi2O8jZHNcuv8tgMBcaYHUuKmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2d370498.mp4?token=Aw9UH1eeEtEBT6nXUNutNHIrVMUNonua-m-tB-AXY7vWyNxpp6I-nWfs9_Hr21_q5zWdpMqAXen3ALpj49Tvh9qOgu30zQackLFHIxPkuW4VgE5it7QUys3rj0W4YaZDJQ439uLuZlphW3Nahu6BXC9SwDTI36G9DoONP60HAQUpONKTbrnTK9mn1RBtNDrFd010g-CLKxfcJTnMvSPUL1VgtcX-CAUQLX1WCOZ-fx4GtLCla7kouEjQLMmpnSafMuwk5xzEgN6JNOzq9XJS6mX16FlW9WfGG1963S_gkMdra-PNgf2OligL0nTWg7MyKZ_p3a4m0HOIcIYSqqXspChCgeES4ZgTCWfAe5Fm82QHG4n8isex354pmMdVHyakb30WCMb1WYRJXfdS3qPDhLoaz7F1pPkA4yP_FiOe06QAkLsJ4k78qqK5mUbdPepAxMd8_AUWMh81n3voK8beHNVp1rdr1dsk5OItj_BvOzqVMjV_oXii5cDL1edS9K30QojD9VKhPPl3AqCmGiLC0jZzkno9izWEdoJ3C4B-wQ7KWZvTGZg_dKrSSLY8ooiK55ANyRIXENqkVxo6HXG9XLaSqctxPMb1Lcd2pAwcxDdDB68Bdskr3laOdw_OeqiDnWmitGNSV4Vuuc6ddGi2O8jZHNcuv8tgMBcaYHUuKmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر صداوسیما بعد از گل سوم الجزایر: یک کشور مسلمان، کاری کرد تا کشور مسلمان دیگری صعود کند!
🔴
پ.ن : ۱ دقیقه بعد الجزایر گل مساوی رو خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130630" target="_blank">📅 10:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130629">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
عضو کمیسیون صنایع مجلس: افزایش قیمت خودرو در شرایط جنگی به مصلحت نیست
🔴
اکنون که نرخ ارز کاهش یافته، هیچ اتفاقی در جهت کاهش قیمت‌ها رخ نمی‌دهد، اما در زمان افزایش آن، بازار و خودروسازان سریعاً واکنش نشان می‌دهند
🔴
باید رعایت حال جامعه در اولویت بنگاه‌های اقتصادی باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130629" target="_blank">📅 10:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130628">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سخنگوی ارتش: در طول جنگ ۴۰ روزه تجهیزات پیشرفته‌تری ساختیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130628" target="_blank">📅 10:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130627">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55b7858092.mp4?token=UOUqQ7fEGExakwKMEbUXsi1FORGxeZwXp0wAupFvCstO8DLAt3YVX-CBmWmqXzCI9RQFn82zgLz1ftc2zI73qBtUzBR0p1WK4jUNlvSVxNcJ_qj0-D2SAQpLVmQuLomBEq13a0QV3giLvJkShhnkhT77pXyDH2goYZN-mnZ1hL0bcyKgTsZcJakEI-yzAYMjwE-EWhb9XoNVaGpaY0_pPr17MCvaiYjGOX-bwnh3RiERLOHF5Pp4aGuuXMCP_HvcpjaPPkfVQykgMnxaG22fD-QPeSEP_TuoaXoJ5k0idOc3bBE4lKaTUZ_Ef5HHB5g50hrZth3_ZFD6M5mJDbCqig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55b7858092.mp4?token=UOUqQ7fEGExakwKMEbUXsi1FORGxeZwXp0wAupFvCstO8DLAt3YVX-CBmWmqXzCI9RQFn82zgLz1ftc2zI73qBtUzBR0p1WK4jUNlvSVxNcJ_qj0-D2SAQpLVmQuLomBEq13a0QV3giLvJkShhnkhT77pXyDH2goYZN-mnZ1hL0bcyKgTsZcJakEI-yzAYMjwE-EWhb9XoNVaGpaY0_pPr17MCvaiYjGOX-bwnh3RiERLOHF5Pp4aGuuXMCP_HvcpjaPPkfVQykgMnxaG22fD-QPeSEP_TuoaXoJ5k0idOc3bBE4lKaTUZ_Ef5HHB5g50hrZth3_ZFD6M5mJDbCqig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حملات ایران علیه پایگاه آمریکایی در کویت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130627" target="_blank">📅 10:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130625">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivI_pugxuC97P7BA9eGwdgnPpuzL19v94yH45UjiAyK0fM-IJrkkZZS_FkrIVv8kmF20Ke6nwLa0R6wfBsZ3-LuPX6mzsQBzCEQz9Ju_XXrmG73tS6nIZkK9-TkptHqZlZhNj6GzCtKT-yZveHbpNM8SbOcuw9XQeDW1V4b4ZiZVUeijOCz5-xsb0jgqhXHot4MLipGsSNqCOHHoLaIdEiCo-l8fianSq20g8CFzAkDj6m-yEcidOTQDsj6w6Cl4KfNGbsg3aUBgYOvT5c6R2A1GfcEZdKo8467Fa2ynOotydUy1LUqMzIW_injzeig0Ci0nFF7NHLIT_yI3Ka80yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J853rP-UP7_ggocRwDFUHcdCXGsDcsXBSEs23FMwurgdrVOz1dOceoU6avxiil4EKr0o2FLIah7f3XcaCCfkm_8GMzdLFIIWnBrdEnoPZeA2gWEnn8pNlGv--3r1jG5JD5WGK-FniHaF7wkQh2r9IHCI_S3BR6UUGqtnKQzsHjZP_mdiBtGZroqKBMRIwaavQHLSFEhL4xgBwtMc1XvUTBNFmcXnpFZtpKH3gfy41aFVXYxPYPHVb7x5Ca56ABuez56IQdu1Va6peA05dAziWLx5Z_UOMpYJBDhSidCPjASdQqHp2WeCER8k2P0JWzB6aNLveafmxheOnoTKB-XMrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آثار حمله هوای صبح امروز سپاه پاسداران به بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130625" target="_blank">📅 10:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130624">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a809c61b67.mp4?token=iyhOVYRd6167-tjnKmuC3EBLh9VJeH7d8CKWdUKm-WIA3maLjB8OY_J6b56UYphOzo1yEPPYGfyQ04q7F8QonYxKuRP7ISThIEXBx-ejvgkqr56f4cvronZrf6eGexlWjWHnfyXbWIgz33le14cix0rbbTXoLmkfvXb1_AwmEfb_VRo-C5QFLY2SU31wRzGWHCVd64zlGKsrdpQ4QX33PnFg5oYBelTBqCfhR0NlSLTS18xd7jXDtkkpJbuBMsD9xniD2KG466wk6St5bzSAneQKNc_y2Qb-w7Uc-YOvaR9Wv3N7LBlLWrUiEhmGt6fMfEVUaZrvgqESlIxRUBFdLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a809c61b67.mp4?token=iyhOVYRd6167-tjnKmuC3EBLh9VJeH7d8CKWdUKm-WIA3maLjB8OY_J6b56UYphOzo1yEPPYGfyQ04q7F8QonYxKuRP7ISThIEXBx-ejvgkqr56f4cvronZrf6eGexlWjWHnfyXbWIgz33le14cix0rbbTXoLmkfvXb1_AwmEfb_VRo-C5QFLY2SU31wRzGWHCVd64zlGKsrdpQ4QX33PnFg5oYBelTBqCfhR0NlSLTS18xd7jXDtkkpJbuBMsD9xniD2KG466wk6St5bzSAneQKNc_y2Qb-w7Uc-YOvaR9Wv3N7LBlLWrUiEhmGt6fMfEVUaZrvgqESlIxRUBFdLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رهگیری و انهدام موشک‌های های بالستیک شلیک شده به سمت بحرین با سیستم پدافند بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130624" target="_blank">📅 10:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130623">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/840a6ae0e5.mp4?token=Zs8ru53d51KG4sCBdLbVNmQGoP78b6WmJVLLNGHXnyuiB314PHopa7t_GhvujnbbTH9bSiM82gZzoRrOJujrOWpsF6lvq3dgeMS6hdBbDoDyvQq-fbx0yGdCjqcTHmWx2Famcj2kgzU0DS2UDwon-oJDpfhjG4GmtTCapiJp9lUsgaM_QgFaUffiOnswUMNmoQ9LbVZ4v1fsJPNqZ1id8qo8smwHyrRkMIZ511Gql1_bEjJHnRlbz9EmZzR1EtBMgCLuLrhoNjiswnpb9u-XG4jQwlVD50SoPIR3q9dW2whOA4uZEZOSJgtqbRZI2JCxYe4napOUMdvN2QHFUZ8EIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/840a6ae0e5.mp4?token=Zs8ru53d51KG4sCBdLbVNmQGoP78b6WmJVLLNGHXnyuiB314PHopa7t_GhvujnbbTH9bSiM82gZzoRrOJujrOWpsF6lvq3dgeMS6hdBbDoDyvQq-fbx0yGdCjqcTHmWx2Famcj2kgzU0DS2UDwon-oJDpfhjG4GmtTCapiJp9lUsgaM_QgFaUffiOnswUMNmoQ9LbVZ4v1fsJPNqZ1id8qo8smwHyrRkMIZ511Gql1_bEjJHnRlbz9EmZzR1EtBMgCLuLrhoNjiswnpb9u-XG4jQwlVD50SoPIR3q9dW2whOA4uZEZOSJgtqbRZI2JCxYe4napOUMdvN2QHFUZ8EIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی سپاه: از اینکه دولت به سپاه نفت داده باشد اطلاعی ندارم و بعید می‌دانم چنین موضوعی صحت داشته باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130623" target="_blank">📅 10:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130622">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ارتش اسرائیل: عبدالرحمن ماهر زیاده، فرمانده هسته النخبه در حماس، را کشتیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130622" target="_blank">📅 10:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130621">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
نیروی دریایی سپاه: شلیک‌های کور آمریکا به سیریک، معمای اشراف ما بر تنگه را حل نمی‌کند، اما شلیک‌های ما به متخلفین، راه روشن عبور را به باقی شناور‌ها یادآوری می‌کند
🔴
حساب پایگاه‌های آمریکایی منطقه جدا است؛ جهنم را در این روز‌ها تجربه خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/130621" target="_blank">📅 09:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130620">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFsVnpMyw1S4c3IrWwUzzh5QcujUAF5Rcn7o4IXsiVaPRhh9NwZ3D6hVFH3BtKg_FY0GQUoks17qN6k_xm1hkXG114oz7li1y5b47CSxR2udK-gP7s6B134BkxZvn1LKu-PiQzT2_Qfakn6QW4r--8oVT3_g4B8LLzKySNN-B3L0CUbNH6yt5m4PgORaCzy4SyPVCkYXc2RM2veCQoCSj9MXyyAefI3grtmmoMNKM0gcij65H2PnI25ernhxrENrfUYiuq3OLJfOVKoFkUrnSUxljQvIR8aEbAwMhku5PPTyFHbdR5_P9lUikXZCoHCDDUQmZFm_eGaXZYCtzfqCYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این برج مخابراتی در سیریک هدف حمله در دو مستند اخیر بوده است که توسط فرماندهی مرکزی ارتش آمریکا منتشر شده‌اند.
🔴
این بمباران در پاسخ به حملات ندسا علیه کشتی‌های تجاری در تنگه هرمز انجام شده است.
🔴
آنچه از ویدئو ها واضح است تسلط پهپادی ایالات متحده بر منطقه است، چیزی که بسیار ترسناک است؛ در ساعات اولیه جنگ ۱۲ روزه و ۴۰ روزه پهپاد ها براحتی در موقعیت های تعیین شده حضور پیدا می کردند بر سر مواضع گشت می‌زدند و لحظاتی بعد کروز ها، بالستیک های هوا پرتاب و بمب ها بر سر اهداف فرود می آمدند....
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130620" target="_blank">📅 09:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130619">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
عراقچی وارد بغداد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130619" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130618">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
بحرین: تکرار حملات ایران به خاک کشورمان را شدیدا محکوم می‌کنیم و خواستار اقدام فوری جامعه جهانی برای متوقف کردن تجاوزهای مکرر ایران هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130618" target="_blank">📅 09:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130617">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69b93ad135.mp4?token=aI9pWNPuJ6RidF-TYDYFDlGJ2kUHFRGs9Mh1Tj3SeLLRRtxe1cZB24kxyC9dwXXcQXCyaw-NeL9_n9kMrA4br1zXZx96GrYdymP_jOmltTDzU2tYpwjbvSyyps68MMQk8P6eYMJV7K30XTbBEjuoLGRIBUGYfamq1raTnlQT9epcUH15wBUN8dAxsJuAJ-nQNcMROIO53rlTSvUJz-ij6TZWUVErGoqxgV_i1uOAFlzPFsVuupZTamtkf9UbAd1bM3ayLm4LiAuKAE2fxXI4YlhWsn3C7RjQaRpW7wH6gOWyzV9VwLP8tuyIYfVOihQt0QxgRzGE-sANwarI7A7cQ7RJOsVCZUsPFzZHCgb3fUiGB6nsdJjvhp4guxeM-EZRxozKhtkhdeicTDdHMK1O3axQGw9uPh5i2n5WFRwMLTItkqCu_i99e7q3AQ8ISkELjJh1ndah7p71mMLt2QhZ8vbeBvLRw23edUSWD_lV7kywrZrscucDGLAbB2CytavMq6MjJn1POS55IIHjBKVAw-Vf52IJ5voficSFj3r6zPmxTl8v3itOcJk0VN0Wx6hslSSpYYP4svGYpEJqM-_xqrjdUcjgX51ccs6GAoohk297jjk7olq23uCec0pj5slajKATKI9EZkWdCz7qeKatRiP4OXMrvs94TbOWhCEkLYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69b93ad135.mp4?token=aI9pWNPuJ6RidF-TYDYFDlGJ2kUHFRGs9Mh1Tj3SeLLRRtxe1cZB24kxyC9dwXXcQXCyaw-NeL9_n9kMrA4br1zXZx96GrYdymP_jOmltTDzU2tYpwjbvSyyps68MMQk8P6eYMJV7K30XTbBEjuoLGRIBUGYfamq1raTnlQT9epcUH15wBUN8dAxsJuAJ-nQNcMROIO53rlTSvUJz-ij6TZWUVErGoqxgV_i1uOAFlzPFsVuupZTamtkf9UbAd1bM3ayLm4LiAuKAE2fxXI4YlhWsn3C7RjQaRpW7wH6gOWyzV9VwLP8tuyIYfVOihQt0QxgRzGE-sANwarI7A7cQ7RJOsVCZUsPFzZHCgb3fUiGB6nsdJjvhp4guxeM-EZRxozKhtkhdeicTDdHMK1O3axQGw9uPh5i2n5WFRwMLTItkqCu_i99e7q3AQ8ISkELjJh1ndah7p71mMLt2QhZ8vbeBvLRw23edUSWD_lV7kywrZrscucDGLAbB2CytavMq6MjJn1POS55IIHjBKVAw-Vf52IJ5voficSFj3r6zPmxTl8v3itOcJk0VN0Wx6hslSSpYYP4svGYpEJqM-_xqrjdUcjgX51ccs6GAoohk297jjk7olq23uCec0pj5slajKATKI9EZkWdCz7qeKatRiP4OXMrvs94TbOWhCEkLYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام تصاویر حملات دیشب جنگنده‌های نیروهای آمریکایی به ۱۰ نقطه در جنوب
ایران را منتشر کر
د
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130617" target="_blank">📅 09:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130616">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8RUzp83l562B_70v784vyW9wKU_xWmUbCFKT9wH8kbRiZ3Fy0AmENZqijrbS_osFf0lBIOYpj9VmRy91B6XQ2W-Y85VL6GpKL9xCasfj5qrI6YdxDsN1SBDTWrDRFNAJhobozjKVWfANSdqYVeNIgN9xJEDYcNtYMkjyrbmBVrIGXS2lgSM2R6_3MPUyd8AHfqlD7uh-k1ybqZTlIppGxB85qdnNuyfv2sM8Yk2eReOyUzJFqTtLZ_zZIrlav6M6iLeEp6P7oWWDmkORDF9S6m768pMe4P-x2Gnn8mQ-75Z1Oaj51NrGIIyWfdTNS8E1rVJgNaUuVH2TfCSSpusMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از سربازان ورماخت ، که منتظر هستند تا پارتیزان های لهستانی قبر خود را بکنند تا به انها شلیک کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130616" target="_blank">📅 09:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130615">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
یک مقام آمریکایی: در حملات ایران هیچ تلفات آمریکایی گزارش نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/130615" target="_blank">📅 08:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130614">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
بامداد امروز، آژیرهای هشدار به‌طور ناگهانی در کویت به صدا درآمد؛ این نخستین بار پس از آخرین هشدار در ۱۱ ژوئن است. این هشدارها همزمان با شنیده شدن صدای انفجارهایی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/130614" target="_blank">📅 08:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130613">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
المیادین: هدف حملات پهپادی امشب، اهداف آمریکایی در پایگاه هوایی شیخ عیسی در بحرین بوده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/130613" target="_blank">📅 08:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130612">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcvQY4Yj0mvSPrNpUP_4YzQ7IWbU9-UIuhagFU-JctAzhAAzSj56RLTYY1nyIcZqgBxk3Kd4w1AKNGtd18cGItbqP8qDivQY6y9gqVP6yBo0z8csAMzK_7RU986cCUY_EUpdxR_O6Q6RypHXnBGBZK_WeRUA4TAgQFrL6n2s4abyEEYaa_1v28Brdl_CyDlq8ZAuCwkiP1uoGuYq27ZwGxTC3pySeSJhohxiXj8tDjGO4CxU-yzaEl80TqX3GNMRdLDczOUtXFQAC7Bk8FV25Emeh6XBJ_e2rV5WVlge1ZLkdrldkCDx095GeQHZrkKJKV7-9H8x9qpON12nWT79aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه وزارت خارجه: آمریکا عهدشکن‌است و تفاهم نامه را نقض کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/130612" target="_blank">📅 08:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130611">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
اطلاعیه سپاه پاسداران: بامداد امروز با پرتاب موشک‌های بالستیک و پهپاد به سوی هشت زیرساخت مهم ارتش آمریکا در پایگاه علی‌السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحر.ین، آن‌ها را منهدم کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/130611" target="_blank">📅 08:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130610">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj3GljVGEw5Zs6fLDIXZ_AN3TuQD_h0OKTyC63Jp-03q0LAw1aRru4Pln_3Mw_YZqKmaBhYgbB_xC2INQVhQJvWllcMhGdU1YjnAAJ5lSRXNbccjmSYPwekiz8f_qIfppsQYFp5ed86SRwERRJiIqQNu3QfmgvR-7w-MCp-HzeDaOWx1o3_NqTaErNJgQTi0VCo4Cs9Csxb6VfpATCxZJfNOjoQVuVu-pmnybaqFCRHfdrDpmm9q_ZhNPf4JleF9xY3EG41zNuUpA8nhz2pUAeA1nNaO0Yv6b13yxgYhX-rmmMvdA4GlRrcse5g2RIkaisTLuzR3EF1mTmPN_Eq3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال:
هواپیماهای ایالات متحده همین حالا مکان‌های ذخیره موشک و پهپاد و سایت‌های راداری ساحلی ایران را هدف قرار دادند، زیرا توافق آتش‌بس را نقض کرده‌اند، باز هم! بسیار محتمل است که هرگز درس نگیرند!
ممکن است زمانی فرا برسد که دیگر نتوانیم معقول باشیم و مجبور شویم کاری را که با موفقیت آغاز کردیم، به صورت نظامی به پایان برسانیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت! پرزیدنت دی.جی.تی
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/130610" target="_blank">📅 02:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130609">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
زلزله‌ای به بزرگی 6.1 ریشتر سواحل جزیره «هونشو» ژاپن را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/130609" target="_blank">📅 02:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130608">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7GlmIiupKKIR6G0KM2gejZbm-sow6I0_C9HaWUiaW8X9zLIShUnNGYNOgcPoGUIaO-NX7Ae43_pyNRz2_LCPojhB1qtRAc3gWy7A5zGLT3sPvbwdzfrG-8-Uib89dcUvZ6pnazPRDJ4SKLo380VqbBVo2BAraz6MBGz0TJKma9h2H-pmEatk2V5PYYmEIxhiz-2SYnjMe6MVOzW28qKlT0a4DNXvtSXo0bHN6VvePoABFg_yKg365_p8vtvq81rV3P36ZDxLyEguafhNyY1aJjsWHX5szU3q0NZQMhf3nkNPXMhpJMoL-zrVq5Y3OECiV6VSScuY_1tWAr6nWVZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ونس: توافق آتش‌بس با ایران همیشه کمی آشفته خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/130608" target="_blank">📅 01:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130607">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فاکس نیوز به نقل از یک مقام آمریکایی: حملات امشب آمریکا به اهداف ایرانی تکمیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/130607" target="_blank">📅 01:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130606">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fp0sflWui4JAtsWV1HeTNoexiMsNtrOEuas_TF1JUc1l-hM7C7GkvTo-BT4UXNwK7jceL0C_DhH8AbF2ZpY6gXD70QtjBczjBUmq51vikSEkEtgF_rBpYkdLmX0HAdDAzzmmUVzYiWcB1j_GGarmoLeR63_E6oS2MdxXcDAceGuXWhDRMHIYiF5q6xLGJFdf1pYve_wkaV2pTRFVIjzu87Kve76GicotaA4jpocU6mmOFbu5cUCq_3yCX378K-Qen8POVbae88c01DIkXWzKdDT3Hc7wXbq1RL91dC8UCvRUpuzceVugiMSX1UAlsOm-KWjeNvy1YfSbTvcUTGtAYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز سوخترسان آمریکایی در نزدیکی خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/130606" target="_blank">📅 01:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130605">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
چندین انفجار در بندرکنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/130605" target="_blank">📅 01:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130604">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/130604" target="_blank">📅 01:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130603">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوووووووووری/بریزید اینجا زود
⬇️
https://t.me/+1RDlZFB3XPtlNzg0
https://t.me/+1RDlZFB3XPtlNzg0</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/130603" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130601">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irGZpwkLNrLUwMVh1WGBkGaFF9gf17Z0q9jFgb10U9-WtoRMNFsL1gZGoZunHs1lCvyNh7sX6raECMlfLGuEcoxyoKwk-JQf-e6q1R39-LnKJH8JH3tTqTWQskTtaSeq04ackTJwkFPHHxewFu3WPT1YOUjKjnxRapkuDza_CtoMagMK39v019vIP5OfhOcsjAwEtqwDi99JAQTPvzdTd-e3m1sV5uAO3zJwTPwx6uJ_A719f02ZQ7-YBP3XbRsvp3tTI6P0XkQTttAlABIHfla-r2LuiiTEUg4MEf5sSZ6J3tfRvuD5DydmJrgBBgQJgWTWAjQ0duJlLVD0z3c4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ایالات متحده پس از آنکه ایران با هدف قرار دادن نفتکش M/T Kiku در نزدیکی تنگه هرمز امروز صبح آتش‌بس را شکست، به اهداف نظامی ایرانی (نظارت، ارتباطات، دفاع هوایی، انبار پهپاد، مین‌گذارها) حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/130601" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130600">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIhorul49-y6GDyQOHK2VTFoWHO_XrQwekt9Rs0NZcHBzee0NY3OG7_efY1VpI-iyNmAt4L7RBk7hjqKFrx7R_8BHPV6RpU9_ANEOZTx_oV5Goop9cqV8mSYWRw1kI758yFtA6R4jbN8dg1nzlG1CGYo77If0A2qQQ_n3_CjHXN1aKEfc0_GOgxCMXzkbQ-urKNYJCf7Xeg6eeXjmPUdVWWBRjFoAVwWlLLZ5on6AUAoR2ZJzNx96qx_IVAh-j1sS9LDwvjx0eXnXEdPXdLL3VFMDzG5tA7PsabR2-OMsno9lZPhNezvwuUv1HHrIEYWEmpP7ReRcfU-VV_nVPLrUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام آمریکایی به خبرنگار آکسیوس گفت که آمریکا در واکنش به حمله ایران به یک نفتکش تجاری امروز صبح، اهداف ایرانی نزدیک تنگه هرمز را هدف قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/130600" target="_blank">📅 01:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130599">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری/هم اکنون حملات آمریکا به جنوب
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/130599" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130598">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری/صداوسیما: صدای انفجار در سیریک شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/130598" target="_blank">📅 00:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130597">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ امضای توافق با اسرائیل را به رئیس‌جمهور لبنان تبریک گفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/130597" target="_blank">📅 00:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130596">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOOT09Z4mNcQqdkLXwaogf3RuhDP7YO0M1Yhqw-R23DDiXrvMHh9p5TwYNUGFC2Dv9yFSxJi9lGcVfmonv8eK0Hn4thPcfYdqEKCyK-FBtNwr0KAwOSnHXhqAHdTp6BdDyAAgQXFY6pF-uZleUN0TnM7TOY6GBsEy7FoWBgnA-bnETbrB5nPQFaGWmO4e5ul13qjXWMV-Vy4WX1ZctUHmxgNUQcDhNX2jNH-AIQNGWFfQkz5A36G1uUU8A6STV2NNVfqNTG-rsaLawyaBQ4UCXX9VZiwmRmEDK74P3SSy_QJttvsuthCL5bp5Oo0tZoDLlpiAPs-f72rFKHS5-lwLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محارب‌های حزب الله در خیابان‌ها لاستیک و سطل آشغال سوزاندند
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/130596" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130595">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baff5cae92.mp4?token=tBG50sk9mdQjBUo4v3E5d0K5E93IXEkq-csKN1C7-rCqVHrdYTOjdJ7ihnkglxJFahemK0RtOjgrcfyb4EkosHADee9QdAounabiP3PD3MNgUVKTsVgiRoZJ81WfZ81FrTr9qkHnWka_HPgsKbh1Qfa8kH_MwbwdbE2ikzFrpCFhNpBXIaXN-rfIb7Q3esOpZTn4ISL7Sulpe97MSoHq5JYV0P5GzTbNhugQ8sZFr2G9yiD4Tv0JD1qo_FZ7FvmjWebKe_MYVs43HeQwy9yml6iHZF07kgUAjWVkNunrkajsRgE8I9al8Njr7dryu3nOZipsD18_Gvqou5zA3wHdzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baff5cae92.mp4?token=tBG50sk9mdQjBUo4v3E5d0K5E93IXEkq-csKN1C7-rCqVHrdYTOjdJ7ihnkglxJFahemK0RtOjgrcfyb4EkosHADee9QdAounabiP3PD3MNgUVKTsVgiRoZJ81WfZ81FrTr9qkHnWka_HPgsKbh1Qfa8kH_MwbwdbE2ikzFrpCFhNpBXIaXN-rfIb7Q3esOpZTn4ISL7Sulpe97MSoHq5JYV0P5GzTbNhugQ8sZFr2G9yiD4Tv0JD1qo_FZ7FvmjWebKe_MYVs43HeQwy9yml6iHZF07kgUAjWVkNunrkajsRgE8I9al8Njr7dryu3nOZipsD18_Gvqou5zA3wHdzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از اغتشاش امشب طرفداران حزب الله در بیروت
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/130595" target="_blank">📅 00:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130594">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">تو دنیایی زندگی میکنیم که برای یه وام ساده ضامن بالای ۷۰سال رو قبول نمیکنن اما سرنوشت ۹۰میلیون ایرانی رو پیرمردهای ۹۰ساله‌ای تعیین میکنن که تو رفع نیازهای روزانشون موندن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/130594" target="_blank">📅 00:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130593">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzAgNSY5Jir0Y6B5lydUGsJWVD-urkEC2eMu5m_i_-LEUOQvXuOmsNSmHkHkeenui6SGc6yCR_fshmcYalbb1_JqXRZSaMfLVTCOQBH-Sl62XBukjjxQnQ83mPupWPUcAPeTZa436_V5IlSnRdPJE44MgCzg9Sxxu7c0i3wQz4z3FM48F-PBColviulQ9qP5kK2IwkAaUerByZCtjATGp7MLONsDRSEu1pn7phX5SIKAR1RedrHzoZIw8NEaUQaQ8WsrkNXiaBa9ihiosEo2LYri67V3ki7mgb3o7sMGL3CfMdNq11taD49Eb7ry7zdv2OQS2Ii9uM_jCGR3shXZhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگان رهبری: مذاکره کنندگان نباید وارد مسائل اتمی شوند و نباید تنگه هرمز رو از دست بدهند، مذاکره کنندگان باید خطوط قرمز رهبری را رعایت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/130593" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130592">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
رئیس‌جمهور صربستان که پس از ماه‌ها اعتراضات ضد دولتی تحت فشار قرار گرفته بود، شامگاه شنبه اعلام کرد که طی چند هفته آینده استعفا خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/130592" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130591">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYPEa7UvNywHVaxfbYfY-Tun5wgXN3EnmQpeN_Gew6yeXhhuie6rQOaNIVq0uQYNGNydCu34NFJtDGPx03NM_PlKFm1TSHSvHdeDkaOltWDTNbs-1I2eV6R27HRHjx1wroECXgym3xZdBoobWB61cQruonwin8fnHXNU7twyRbo7XiKtulAuWmeKB2u1WErF6l_RR1UFVdwiJqlZfBUeVCpskZb2kh9RrbqkAOcaJVIkOtSI3Agd8ZyQH6iNeCDdAdknQvrXpcnE-AT2oQBik_io-cNQsvDO9XPEStm1-HnP7vocIhIHNxlYl49CjI1wUA8k1cjNaV_kUWMSiAVExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: درباره هسته‌ای نباید مذاکره بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/130591" target="_blank">📅 23:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130590">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b6cc76c6.mp4?token=HX9giw3ku7VvaZX7mth5b1SXNU1kUAbv9NPwaaE8D27o3Soz8Qa9_qhbICgLDmypDcN9SZUaq1l4oGYJ8RiSB58aMTY9-l_ZWPHbyRAMZgZUTK6ayZnSilcQ9wsCnc-wRq9Jgwv8y_pEh2e_QwXChnbWb2te7wtu5PK-zkOn7ukas7pE8XF1ylNXFLAM1MgUV2z8H2QPUM6hPGYXqMXHpQeMiPLV_XqkRwTfIzVCzk1PsFw-ruKZb32FNvbQPpjvuddXm_R32zjGh52_Pcj7OsFmZA6v8WPWLlI-wqf8MMP1Pv1-O2TpkscaxRwngZQOWMelAQTSTA0qtqJz0sRYOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b6cc76c6.mp4?token=HX9giw3ku7VvaZX7mth5b1SXNU1kUAbv9NPwaaE8D27o3Soz8Qa9_qhbICgLDmypDcN9SZUaq1l4oGYJ8RiSB58aMTY9-l_ZWPHbyRAMZgZUTK6ayZnSilcQ9wsCnc-wRq9Jgwv8y_pEh2e_QwXChnbWb2te7wtu5PK-zkOn7ukas7pE8XF1ylNXFLAM1MgUV2z8H2QPUM6hPGYXqMXHpQeMiPLV_XqkRwTfIzVCzk1PsFw-ruKZb32FNvbQPpjvuddXm_R32zjGh52_Pcj7OsFmZA6v8WPWLlI-wqf8MMP1Pv1-O2TpkscaxRwngZQOWMelAQTSTA0qtqJz0sRYOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نبویان: فقط یک نفر از بین ۱۳ عضو شورای عالی امنیت، نظر رهبری را بدرستی تشخیص داد و آن فرد، جلیلی بود
🔴
افرادی که ادعا میکنند ولایی هستند فرمون رو برگردونن نسبت به این تفاهم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/130590" target="_blank">📅 23:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130588">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQGWd45A9PYJy3eFYBCh229PiZvNz6LIi4-lfPgCXTgcBxHk4f0b01xNKUO4N-K-U-3NJ5B8U3NMls1X5XbOVT21CLdPVm0kbRtLoSbA5QZOLr6jI9rJW1aZnfu5F_P8h5toGQ357JY4PDuOxQTNKh03gTEOr9HWzjN0uC4cHVeP1_D7_b2NBk6mdjWUXJ9j1Z-MRGFMFk48-HB_9u0e7Fm9fMthQdSckX-joBfSpGwzk8fZ0HrF1yO8vJ3HAscAP69UhC3rWExw1cr9daEPd0gFSgMm3jmePC-OW4lm0qI-mpmY2FCoo2zheGYbCwjNr7Rk2t5G8XZRdRwxaWMaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جان سینا : ظرف روزهای آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/130588" target="_blank">📅 23:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130587">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ونزوئلا دوباره زلزله ۵.۶ ریشتری اومد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/130587" target="_blank">📅 23:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130586">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56cc34c4ff.mp4?token=j81uMSvOT36T5WmcBCjOENDaW9577YUbc1Fk_DWwqgTNzR_iE9AT4k3MFD-GNgxSnl6tZue8j1x99Zme67d6OJv2cXkOSovuNrfuiWm2hPIv88bniog4JPi2d38c1Es_Bn8_8G_ExNwAaU9AjrlUGDhlxrdqMUeXnIsT8-0j3M1pla0D2-nxup4KafPWf3oG4KjAWrXErSA93oBd_sopTXRAbFukGU5V754aBAody3rupFZD_Sd4dm2pEkXUM2dVsGSyRjER86wrDnAqhASS-TqobkzxZovJRgViEBodnrn_ezOianYO6qf8MpnlKx-onON7emH6FdNKnXpQo7oz_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56cc34c4ff.mp4?token=j81uMSvOT36T5WmcBCjOENDaW9577YUbc1Fk_DWwqgTNzR_iE9AT4k3MFD-GNgxSnl6tZue8j1x99Zme67d6OJv2cXkOSovuNrfuiWm2hPIv88bniog4JPi2d38c1Es_Bn8_8G_ExNwAaU9AjrlUGDhlxrdqMUeXnIsT8-0j3M1pla0D2-nxup4KafPWf3oG4KjAWrXErSA93oBd_sopTXRAbFukGU5V754aBAody3rupFZD_Sd4dm2pEkXUM2dVsGSyRjER86wrDnAqhASS-TqobkzxZovJRgViEBodnrn_ezOianYO6qf8MpnlKx-onON7emH6FdNKnXpQo7oz_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم منتشر شده از لحظه حمله به چندین نیروی نظامی در بانه-شب گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/130586" target="_blank">📅 23:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130585">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf65d7d28.mp4?token=MYucbZjvZf0XsHBqwDliS_8Nh4otMGopjiip87POCvODZ40XLTlWIJ16CBhcb7TscdVPFHqY5RPh9OcpR-xnQxet_J9i5oJV7sCgzfidbu527eYi8M5H6VLbiMUngmIO8CrPVV3FdkFpCk0RgvZZ6ej00i7emX1yosM4hok6xlR_glwi935fqVJxUIYfFG6Z_KBfKvr92WfIafj3ZzzN0YMNzhyK6hrYy3lszWlWv0oJWWJW1U1-BEbdtZc5nCJMedvPtpSluolb_PQJEkUzj2V9Y9kby5mh6yOpM2laI7T11RfTJb6v-U8jsPINGrvc0Nm_Ryo2updzivlihisTXQikF1jItGCSERpmrDevUy1q3PlObdIjNAq7bpPauIITLNQRYtjnSbiKf3D67i_jsbFbE1sBbUapE9SPgtW4yhZ97TbFHOPA7nOmQnS36H60DMnyYEVjqTj7amUBMoqaFbj-jSfoBvCu2uAMQkW-RvHpx6b05CF8VMuwmwBo2_FIqQDJInN70Z5HbvqlDJ_zsqconDLlnsN9zuVNpoPkefYSm6NSMG_bg9Z8-us2QCD5lOO6Ydc5amcMkc2Od-SK4ZgMBBUq77FQiGEhE8JRId3knISeEovx9RLew37hE7RgemlpXOfWVgjWkdGTSiXxJNyu9FckHjoQ9iWKPIQ8pMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf65d7d28.mp4?token=MYucbZjvZf0XsHBqwDliS_8Nh4otMGopjiip87POCvODZ40XLTlWIJ16CBhcb7TscdVPFHqY5RPh9OcpR-xnQxet_J9i5oJV7sCgzfidbu527eYi8M5H6VLbiMUngmIO8CrPVV3FdkFpCk0RgvZZ6ej00i7emX1yosM4hok6xlR_glwi935fqVJxUIYfFG6Z_KBfKvr92WfIafj3ZzzN0YMNzhyK6hrYy3lszWlWv0oJWWJW1U1-BEbdtZc5nCJMedvPtpSluolb_PQJEkUzj2V9Y9kby5mh6yOpM2laI7T11RfTJb6v-U8jsPINGrvc0Nm_Ryo2updzivlihisTXQikF1jItGCSERpmrDevUy1q3PlObdIjNAq7bpPauIITLNQRYtjnSbiKf3D67i_jsbFbE1sBbUapE9SPgtW4yhZ97TbFHOPA7nOmQnS36H60DMnyYEVjqTj7amUBMoqaFbj-jSfoBvCu2uAMQkW-RvHpx6b05CF8VMuwmwBo2_FIqQDJInN70Z5HbvqlDJ_zsqconDLlnsN9zuVNpoPkefYSm6NSMG_bg9Z8-us2QCD5lOO6Ydc5amcMkc2Od-SK4ZgMBBUq77FQiGEhE8JRId3knISeEovx9RLew37hE7RgemlpXOfWVgjWkdGTSiXxJNyu9FckHjoQ9iWKPIQ8pMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله مجدد تندروها به جمهوری اسلامی
🔴
چرا روز تشییع آقا با روز استقلال آمریکا تو یک روز هست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/130585" target="_blank">📅 23:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130584">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فرمانده سپاه تهران: برای مراسم تشییع رهبر سابق در تهران حضور حداقل بین ۱۲ تا ۱۵ میلیون نفر برآورده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/130584" target="_blank">📅 23:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130583">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ArWcVRk8EtEBQ3Yfyoe5_nbwVE_WVVzpZlE1aDX-isJkvJDjdf-T4H0xqPLJpqzsWHCF2REzCZbV0WssVIJG87EpjLNnGXWq3kLQ0etNZP_IyJx7ryovl3o33W0wwqdEmeyvaReG0CWNLToigz8P1ogqQ7Pp5Sxy86hgXCL91hCoe1MHNXkhDNXyuK3zFDYbqWj4xjdzX-_7WFYiRhpMiZDfzUYSa_p83bJTmV5d4XLhrInAS-oYAyE-Tnj1M6X7ro3G8hhEx3UrJ0qlCPzue3qnUh_k7dokqvxu6qW0gUGmGIivj7oiE5omQ7tt3AUmiPsi457mG2aB3G4gnq4p8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو هر کشور باید چند روز کار کنی تا بتونی GTA6 بخری:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/130583" target="_blank">📅 23:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130582">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fcba67c0.mp4?token=AVGZthdV3CE8JObE-kswQt4_KSnos3FjK572bOkzVuo3JD2cxSp5GUACKPhgkOPdm_xlxOP3Ve4Ey2R82_fY7nm5LiyKP_zYOcU-ZuTm374Z_LWRh47pANnTCDDocFZjFCQodFq3iUazwgNcYhfpSP4XLYT8PThlGrxjdSRYHvti5JspWqNd1yDA7Oikz1U1JnfunW5F_-bmCev6p3ffKyuXvwpNnUQY4Yo50izTpjcNjAxoNZYxxYCcgCTYKPdbf-AVb3L7qfDJoHmcanL0A1W2UAaiPZGzVIuwm9OwjCRIRXoVBMQrITFIRS6O9GQJ9ez54oUiyBYk4iSlLnYlwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fcba67c0.mp4?token=AVGZthdV3CE8JObE-kswQt4_KSnos3FjK572bOkzVuo3JD2cxSp5GUACKPhgkOPdm_xlxOP3Ve4Ey2R82_fY7nm5LiyKP_zYOcU-ZuTm374Z_LWRh47pANnTCDDocFZjFCQodFq3iUazwgNcYhfpSP4XLYT8PThlGrxjdSRYHvti5JspWqNd1yDA7Oikz1U1JnfunW5F_-bmCev6p3ffKyuXvwpNnUQY4Yo50izTpjcNjAxoNZYxxYCcgCTYKPdbf-AVb3L7qfDJoHmcanL0A1W2UAaiPZGzVIuwm9OwjCRIRXoVBMQrITFIRS6O9GQJ9ez54oUiyBYk4iSlLnYlwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف به سیم آخر زد!
🔴
یه عده که اسمشونو گذاشتن انقلابی و سوپرانقلابی هیچ غلطی برای این انقلاب نکردن ولی طلبکار از همه هم هستن..
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/130582" target="_blank">📅 23:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130581">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
بنیامین نتانیاهو: ما وعده دادیم که غزه دیگر تهدیدی برای اسرائیل نخواهد بود.
🔴
حماس هنوز برخی از توانایی‌های غیرنظامی را در اختیار دارد.
🔴
ما هنوز کارهایی برای انجام داریم، اما این یک دستاورد بزرگ است. مقایسه وضعیت ما در ۷ اکتبر با وضعیت امروز غیرممکن است.
🔴
چه کسی اهمیت می‌دهد؟ چه یک گورستان سیاسی باشد یا نباشد، هر کاری که برای اطمینان از امنیت و پیروزی دولت اسرائیل لازم باشد، انجام خواهم داد.
🔴
اگر نیاز باشد وارد لبنان شویم، وارد لبنان می‌شویم. اگر نیاز باشد با نیرویی غوغا در آنجا عملیات انجام دهیم، این کار را انجام خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/130581" target="_blank">📅 22:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130580">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a356ac50.mp4?token=GzpcbleNxOsaI7wPgOswGmavMIvah3WGR7cwjOhGa4HM45QS1Xi7xMRlyYLsCzyVu5U0ePy01qiBRu0SdWc47WxoU_cVJkfo2Q11OfDwri1emnzBExEAUHIdGnkYD1w6-HUeacnThZIHqQyLIhsPLoxZotrOcfrIwaDRTJ4au8ykrrvExe4jPdRd3G4zejXkxVQX-JbZvBGsWunuKhvzXbuisOBnTUSOK9FYy9ofTZBAFeLSNb8_7KMR0RNPpAw9BKPF7epccxeLZelOEmK8c0SyCmLXqDrpWQOTuRvcEhhYwtuI4XM3bil92X3SGGlgrNxNUZWfmDblR3rcSMHurw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a356ac50.mp4?token=GzpcbleNxOsaI7wPgOswGmavMIvah3WGR7cwjOhGa4HM45QS1Xi7xMRlyYLsCzyVu5U0ePy01qiBRu0SdWc47WxoU_cVJkfo2Q11OfDwri1emnzBExEAUHIdGnkYD1w6-HUeacnThZIHqQyLIhsPLoxZotrOcfrIwaDRTJ4au8ykrrvExe4jPdRd3G4zejXkxVQX-JbZvBGsWunuKhvzXbuisOBnTUSOK9FYy9ofTZBAFeLSNb8_7KMR0RNPpAw9BKPF7epccxeLZelOEmK8c0SyCmLXqDrpWQOTuRvcEhhYwtuI4XM3bil92X3SGGlgrNxNUZWfmDblR3rcSMHurw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید لیلاز: آمریکا در بهمن ماه مجدداً به ایران حمله می‌کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/130580" target="_blank">📅 22:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130579">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
لغو مذاکرات فنی در پی حمله آمریکا به سیریک؟
🔴
تیم مذاکره کننده ایران در پی حمله بامداد آمریکا به سیریک درباره بررسی لغو مذاکرات فنی در حال مشورت هستند. یک منبع مطلع در این باره به جماران گفت: مذاکره کنندگان معتقدند نقض صریح ماده یک آتش بس باید واکنشی در سطح توقف مذاکره داشته باشد.
🔴
به گفته این منبع، تیم مذاکره کننده ایران همچنان در حال مشورت در این مورد هستند و رایزنی های خود را ادامه می دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/130579" target="_blank">📅 22:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130578">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ونس: قیمت نفت الان به ۷۳ دلار در هر بشکه بازگشته، در حالی که تا ۱۲۶ دلار رسیده بود؛ این نشانه‌ای است که یک اتفاق واقعی دارد می‌افتد
🔴
آتش‌بس وقتی با ایرانی‌ها طرفی، همیشه کمی آشفته خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/130578" target="_blank">📅 22:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130577">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
گزارش اعتراضات و بستن یک جاده با لاستیک‌ های آتش‌ زده در مسیر بین شهرک ریاق و شهر بعلبک در منطقه بقاع لبنان توسط طرفداران حزب‌الله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/130577" target="_blank">📅 22:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130575">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63d4338d6.mp4?token=MfIZceKZ1Z1NVTS_K1dQEtT5t-8zJQNlTA3oB8SF6xSmNZCddwu3Lc3_tILyhq31mDSxjyuZri4KGb1jLeZQqkXUcWet5f_5FtgbW0h7n0T67CNmYUyWvXyEZ-3V3dsCFrWxYzKq-qaytzOvA5KbOg6XaAPdgRvGBcHEnYkeTnZ8wsPqnPXjV4JslKYFTTlWBHy7KtGSzqQF4KxMy8nd7VOZnLP4bQ7M_7H71iIHPGoqPS-cxjAan7MoR55Q6P2OZEna-lnz7csxHE0Z_FnOb85gHRVZ787UHd0fxttJMyg_WESAFfPRy1kzV1oEGYVWKjoDQO1okaIUvZcbU0g9BTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63d4338d6.mp4?token=MfIZceKZ1Z1NVTS_K1dQEtT5t-8zJQNlTA3oB8SF6xSmNZCddwu3Lc3_tILyhq31mDSxjyuZri4KGb1jLeZQqkXUcWet5f_5FtgbW0h7n0T67CNmYUyWvXyEZ-3V3dsCFrWxYzKq-qaytzOvA5KbOg6XaAPdgRvGBcHEnYkeTnZ8wsPqnPXjV4JslKYFTTlWBHy7KtGSzqQF4KxMy8nd7VOZnLP4bQ7M_7H71iIHPGoqPS-cxjAan7MoR55Q6P2OZEna-lnz7csxHE0Z_FnOb85gHRVZ787UHd0fxttJMyg_WESAFfPRy1kzV1oEGYVWKjoDQO1okaIUvZcbU0g9BTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ایرانی‌ها استادان تبلیغات هستند
🔴
تیم مذاکره‌کننده از دولت است و آن‌ها برای مخاطبان سخت‌گیر در تهران بازی می‌کنند.
🔴
دقیقاً همانطور که در سیستم ما سخت‌ گیرانی وجود دارند، در آن‌ها نیز سخت‌گیرانی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/130575" target="_blank">📅 22:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130574">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
بنیامین نتانیاهو: از همان ابتدا گفتیم که ما طرف توافق بین ایالات متحده و ایران نیستیم.
🔴
اما این به معنای نداشتن منافع نیست. ما منافع خود را داریم و آن‌ها را اعلام خواهیم کرد.
🔴
این در مورد مسئله مرکزی—مسئله هسته‌ای—نیز صادق است. قصد دارم هیأتی به واشنگتن بفرستم تا منافع اسرائیل را توضیح دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/130574" target="_blank">📅 22:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130573">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
بنیامین نتانیاهو می‌گوید اسرائیل نیروهای حزب‌الله را حتی قبل از اینکه به آنها شلیک شود، می‌کشد:
🔴
دیروز تهدیدی بسیار دورتر از سربازان ما وجود داشت - نه در برد فوری.
🔴
آن‌ها هفت نفر را دیدند که وارد خانه‌ای می‌شوند. آن‌ها هنوز شلیک نکرده بودند و هنوز خود را سازماندهی نکرده بودند.
🔴
اما آن خانه نابود شد و آن هفت نفر حذف شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/130573" target="_blank">📅 22:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130572">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
عراقچی، فردا در راس یک هیات دیپلماتیک به عراق سفر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/130572" target="_blank">📅 22:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130571">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
بنیامین نتانیاهو: من نه تنها به دنبال استقلال انرژی هستم که آن را به دست آورده‌ایم، و نه تنها استقلال اقتصادی.
🔴
من همچنین می‌خواهم در صنایع دفاعی و صنایع تسلیحاتی خود، استقلال امنیتی داشته باشیم. صرفاً برای کاهش وابستگی خود به دیگران.
🔴
نتانیاهو در مورد مذاکرات ائتلاف: همه می‌توانند بپیوندند، به شرطی که موافق باشند که اسرائیل دولت-ملت مردم یهود است.
🔴
نتانیاهو: دشمنان بیرونی داریم و قطعاً منتظرند که ما یک جنگ داخلی را آغاز کنیم.
🔴
و می‌گویم، همان‌طور که مناحم بگین گفت، «دیگر جنگ داخلی نیست. اینجا جنگ داخلی نخواهد بود.»
🔴
برای رسیدن به این هدف، قصد دارم یک دولت ملی گسترده تشکیل دهم — نه یک دولت محدود، نه یک دولت چپ‌گرا وابسته به احزاب عربی، بلکه یک دولت ملی گسترده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/130571" target="_blank">📅 22:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130570">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ونس: مذاکرات با ایران موفقیت‌آمیز بوده است
🔴
اگر با ایران به توافق نهایی برسیم، عالی می‌شود.
🔴
افزایش جریان نفت از طریق تنگه هرمز نشانه‌ای از وقوع یک اتفاق واقعی است، اما توافق آتش‌بس با ایران همیشه کمی آشفته خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/130570" target="_blank">📅 22:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130569">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
بنیامین نتانیاهو:جایی برای دو کشور وجود ندارد.
🔴
از دریا تا اردن، جایی برای دو کشور وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/130569" target="_blank">📅 22:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130568">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نتانیاهو:ما طرف توافق ایران و آمریکا نبودیم و منافعی داریم که با واشنگتن در مورد آنها گفتگو خواهیم کرد
🔴
ما به عملیات خود در لبنان علیه هرگونه تهدید فوری ادامه می‌دهیم و دیروز ۷ عضو حزب‌الله را که در خانه‌ای دور از نیروهای ما بودند، هدف قرار دادیم.
🔴
ما خروج از مناطق آزمایشی در روستاهای زوتر غربی و فرون در جنوب لبنان را آغاز خواهیم کرد.
🔴
ما به کنترل ۷۰ درصد نوار غزه نزدیک شده‌ایم و حماس را محاصره کرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/130568" target="_blank">📅 21:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130567">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نتانیاهو: هیئتی را به واشینگتن اعزام خواهم کرد تا منافع امنیتی اسرائیل را در رابطه با پرونده هسته‌ای ایران تبیین کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130567" target="_blank">📅 21:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130566">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFU9N9uyoxvFMPaFlF_NGSA_uSsGpLUhFVCSW7YFKot-r8hx2ix6PrPFXSxUu_RSURYyZnctqlUdBSlX9dTLTasxDa5MOFtWWCsq6uRtFn1jUVzyWIkEJsnT-2zFf7ymaXT3TuTc_93vCjATZrTqOwxdTzyTNW0Rq_WNr0-qk6wwQbZn8OVXI8dpv4QNOzc6RWDxorn6ptVSuyr9ddPR3cKTZXZT2n_C93xyj9-H1qn_vVY11wAktibqDssIG19u1yTAVkwj_NICzLu7sAShu3l1DKiCEpte5SDPUTQz1svKDMgTSteA62aL95hmoAfm40GHt6s_eSCqg1u7BiuZhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل بن گویر:
توافق با لبنان اشتباه بزرگی است — من امشب به نخست‌وزیر مراجعه کردم و درخواست کردم که در کابینه رأی‌گیری شود، و هفته‌هاست که علیه این توافق مبارزه می‌کنم.
🔴
در واقع، فعلاً در بیشتر قلمرو باقی می‌مانیم، اما دولت لبنان حزب‌الله را از سلاح‌هایش خلع سلاح نخواهد کرد، وزیران دولت لبنان اعضای حزب‌الله هستند و نمی‌توانیم به لبنان برای گرفتن سلاح‌ها از حزب‌الله اعتماد کنیم — من درخواست رأی‌گیری در کابینه خواهم داد.
🔴
فقط سربازان ارتش اسرائیل حزب‌الله را نابود خواهند کرد — هیچ نهاد دیگری این کار را برای ما انجام نخواهد داد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/130566" target="_blank">📅 21:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130565">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: من قویاً با هرگونه تلاشی برای مجبور کردن ایران به عقب‌نشینی مخالفت کردم، و اکنون ایالات متحده و لبنان به ایران می‌گویند که این موضوع به آنها ربطی ندارد.
🔴
ما در حال از بین بردن محور ایران و همچنین محور سیاسی آن هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/130565" target="_blank">📅 21:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130564">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نتانیاهو درباره لبنان: به یک توافق چارچوبی رسیده‌ایم که به ما امکان می‌دهد به درگیری با لبنان پایان دهیم.
🔴
اسرائیل و لبنان بر سر دو منطقه امنیتی برای آزمایش روند خلع سلاح حزب‌الله توافق کرده‌اند.
🔴
ما به لطف ضربات دردناکی که به حزب‌الله وارد کردیم، توافق با لبنان را نهایی کردیم.
🔴
در حال تلاش برای نابودی زیرساخت‌های حزب‌الله در جنوب لبنان هستیم و هنوز کارهای زیادی برای انجام دادن داریم.
🔴
۹۰ درصد از زرادخانه موشکی حزب‌الله را نابود کردیم
🔴
ایالات متحده و لبنان بر سر ادامه حضور ما در منطقه امنیتی جنوب لبنان توافق کرده‌اند
🔴
به نیروهایمان بر آزادی تحرک برای دفع هرگونه تهدید در لبنان تأکید کردم
🔴
توافق با لبنان می‌تواند به توافق صلح تبدیل شود
🔴
این توافق، اسرائیل و لبنان را تقویت و ایران و حزب‌الله را تضعیف می‌کند.
🔴
از دولت لبنان به خاطر شجاعتی که نشان داده است، تشکر می‌کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/130564" target="_blank">📅 21:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130562">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=Q6zq8Z1vYdl5q2UUC5s_b_ahGN2y9AM9p3fN_5MUl8wj-J8suuF1ryq2G_i2GFCa5k6-NEZEmS0SGTZp743RXZyBt6W62BhiI5fEXWZAGMdbxTyq9bw2Cifu0sq-8zSgf8DVLxMpF4xwfLJEqqmZYlP7dxu6b0MpHSaAnKGqC3lsXgPS3Fs8Ee-G7NmHlbYDdte2m-E_Uyth_ytYyT0YA2lfs5H9azJhAYp59wZEnlm_7Dbui74GGX4V6UeMLcO96T4U-wpONu8dGySX139mP0MDFMKW9wsRekmDyJpTE-Rpfykl9wOQz7grPkQbXIvofdjMScDsgSVnLW2ob57q1m3U4l14Sniu_kYwBljn81Jl-V1VUDNqQN6H47HrVvOzXfx40NZoVIlImsM7lODV9KwJDkPR8SO5BvljOHOCdZi_dsGKHyFbI3K8BxrpcuEiiSlL0aWrhjkveXS4wUXmzDZKmR6ObIzJ-T52emRh_C8GZTX3j0J6uBKNfpbO6o-qWeZCcL6QsrnKAo-LZEzHZ3UYm8jfUByDR5NszcTI5u7MC1oNpZ36QpxFJXwO7GFWWRH6VLHN-fmu5ubGLv5-yPlX8B79d3y0W_PIXWBithWwVqDp9FVpHXsyqR-xiIjEHGe8j8IHBwhPxvxiMSSSOIGGDFwDiuz-L4yX3vQH6-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=Q6zq8Z1vYdl5q2UUC5s_b_ahGN2y9AM9p3fN_5MUl8wj-J8suuF1ryq2G_i2GFCa5k6-NEZEmS0SGTZp743RXZyBt6W62BhiI5fEXWZAGMdbxTyq9bw2Cifu0sq-8zSgf8DVLxMpF4xwfLJEqqmZYlP7dxu6b0MpHSaAnKGqC3lsXgPS3Fs8Ee-G7NmHlbYDdte2m-E_Uyth_ytYyT0YA2lfs5H9azJhAYp59wZEnlm_7Dbui74GGX4V6UeMLcO96T4U-wpONu8dGySX139mP0MDFMKW9wsRekmDyJpTE-Rpfykl9wOQz7grPkQbXIvofdjMScDsgSVnLW2ob57q1m3U4l14Sniu_kYwBljn81Jl-V1VUDNqQN6H47HrVvOzXfx40NZoVIlImsM7lODV9KwJDkPR8SO5BvljOHOCdZi_dsGKHyFbI3K8BxrpcuEiiSlL0aWrhjkveXS4wUXmzDZKmR6ObIzJ-T52emRh_C8GZTX3j0J6uBKNfpbO6o-qWeZCcL6QsrnKAo-LZEzHZ3UYm8jfUByDR5NszcTI5u7MC1oNpZ36QpxFJXwO7GFWWRH6VLHN-fmu5ubGLv5-yPlX8B79d3y0W_PIXWBithWwVqDp9FVpHXsyqR-xiIjEHGe8j8IHBwhPxvxiMSSSOIGGDFwDiuz-L4yX3vQH6-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره لبنان
:
اسرائیل در منطقه امنیتی زرد باقی می‌ماند که ما را ایمن نگه می‌دارد. و این یک دستاورد بزرگ است. بزرگ!
🔴
چون آنها چه کردند؟ آنها تلاش کردند ما را از آنجا با انواع روش‌ها و فشارها بیرون بکشند. البته این اتفاق نیفتاد.
🔴
از رئیس‌جمهور ترامپ و وزیر امور خارجه روبیو برای مشارکت و کمک‌هایشان تشکر می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/130562" target="_blank">📅 21:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130561">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
شبکه عبری کان: فرمانده سنتکام فردا به اسرائیل می‌رود تا بر عقب‌نشینی اسرائیل از دو منطقه در استان نبطیه نظارت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/130561" target="_blank">📅 21:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130560">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
العربیه به نقل از یک منبع پاکستانی: وزیر خارجه پاکستان در تماس فوری با یک مقام آمریکایی خواسته تنش‌ها کاهش پیدا کنه و ابراز امیدواری کرده آمریکا به اتفاقات اخیر پاسخی نده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/130560" target="_blank">📅 21:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130559">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
جی‌دی ونس: اگر به توافق نهایی نرسیم، آنها هنوز به عنوان یک کشور بسیار ضعیف‌تر هستند و برنامه هسته‌ای شان نابود شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/130559" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130558">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
مدتی است که برق شرق تهران قطع شده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/130558" target="_blank">📅 21:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130557">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZOFlRdk2x5JCcuz_7L4ob5wXnOxAx4NHEtPsyVzIAN0CE6qsirQLXWylbM8qh2RQ-2LMoVUw8n2lggne25FUuEbCNCIXmNMJQSvRHdesis7mRg6a7WUT9G09gh75oIRNUGBygXvBtTb0yXEHFnoGw9HXB5mF7vg5ITcZuqZtL7KWO59m-QndjqxdurXlSxcuUWTLW-NPb2T3DTdU1BEfDcUWh1b0I4cmXPiSjFAyES86LDGpx9YG8wcE1vgKoRgs4argl-FfHSH6hcjw_PmZyijoACU5Lw20edk5ZyTnoSHkSuwfNAi0WCLgCe-ox5SQTkm1M2FO9tZgqsn00V2VYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدتی است که برق شرق تهران قطع شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/130557" target="_blank">📅 20:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130556">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70efb8d7c.mp4?token=it0WVqcY5ocU0SYVIBhrSiNJ96A1igR5a5iOvlefC-wdqbTu7qmM_cLkRFQaLMVF76Ed2mXYpMTITraamajzhz2an3wht6y8j2JDDNpun2Ju8s-RnAjev9SBQvSQC9KJjdzF1wmHHZK2wvp5ePnM7iE__LZSjCjhlBJqa4vQu6FuWN_3Z6kW_MnK1Z_vixj3pOB4yx_Jr-r4RwfZo8-_qpvzI8rV2QLERtDXDe4_N9kKcDXx1deKDShoumE9gGPeLBltPlAY4cI32cRoJGi5PB7AhIMiB9QpWIYWkdqAKI-FVaQA4N3tZrrUuuiM2iDEaVedFwuvJDU3SFLjRt4cbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70efb8d7c.mp4?token=it0WVqcY5ocU0SYVIBhrSiNJ96A1igR5a5iOvlefC-wdqbTu7qmM_cLkRFQaLMVF76Ed2mXYpMTITraamajzhz2an3wht6y8j2JDDNpun2Ju8s-RnAjev9SBQvSQC9KJjdzF1wmHHZK2wvp5ePnM7iE__LZSjCjhlBJqa4vQu6FuWN_3Z6kW_MnK1Z_vixj3pOB4yx_Jr-r4RwfZo8-_qpvzI8rV2QLERtDXDe4_N9kKcDXx1deKDShoumE9gGPeLBltPlAY4cI32cRoJGi5PB7AhIMiB9QpWIYWkdqAKI-FVaQA4N3tZrrUuuiM2iDEaVedFwuvJDU3SFLjRt4cbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیدپوشی سبلان در نخستین روزهای تابستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/130556" target="_blank">📅 20:45 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
