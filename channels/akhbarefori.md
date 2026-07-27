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
<p>@akhbarefori • 👥 4.23M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 20:45:13</div>
<hr>

<div class="tg-post" id="msg-675858">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک معضل جدید در موضوع کالابرگ
رسول بخشی دستجردی، عضو کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
به دلیل اینکه برخی از فروشگاه‌های کوچک توان مالی کافی ندارند و دولت بدهی خود را به آنان به‌ موقع پرداخت نمی‌کند، نمی‌توانند با کالابرگ به مردم کالا بدهند، بنابراین از گردونه خارج می‌شوند.
🔹
برای حل این مشکل دولت باید در فواصل زمانی خیلی کوتاه پول را به حساب فروشگاه‌ها واریز کند تا بتوانند به کار خود ادامه دهند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/675858" target="_blank">📅 20:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675854">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d23f804b9.mp4?token=XjudUeeisZIxcXfRSC7jGUC2tCTi-ybKPGB7EtYxMTVBWY_uCqyhqfH7u8woj4OBT3lXAB6dzgm_y3j2E9B9QTMz7T88-jtiH3281ybaXzlcnJiwr7Dl-4eH6dkGl6Xi07gt4QueJDwgeEAEmydGWKQGrJXgwCQL7JxhD13YQubaus_I73er8brm8_-WCagaKj2G_epXWXUQEm55NYVqYn3C_baggu2sxIKw30bBYADYzvhvL_kZvMQhwe7oidqYuXsRgkl2RTe2voNkRz-RyD8dtyfLQLX28smIrHjJ7cuT798yk5d6M4tc-4Z_fcZIlNeuaCzjLpQ1apzQo5cdsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d23f804b9.mp4?token=XjudUeeisZIxcXfRSC7jGUC2tCTi-ybKPGB7EtYxMTVBWY_uCqyhqfH7u8woj4OBT3lXAB6dzgm_y3j2E9B9QTMz7T88-jtiH3281ybaXzlcnJiwr7Dl-4eH6dkGl6Xi07gt4QueJDwgeEAEmydGWKQGrJXgwCQL7JxhD13YQubaus_I73er8brm8_-WCagaKj2G_epXWXUQEm55NYVqYn3C_baggu2sxIKw30bBYADYzvhvL_kZvMQhwe7oidqYuXsRgkl2RTe2voNkRz-RyD8dtyfLQLX28smIrHjJ7cuT798yk5d6M4tc-4Z_fcZIlNeuaCzjLpQ1apzQo5cdsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان شدید در وادی بنو رواحه عمان
⛈
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/675854" target="_blank">📅 20:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675853">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
سگ‌زرد: ما با خیلی از کشورهایی که بدون ما دوام نمی‌آورند، بسیار مهربان بوده‌ایم
🔹
می‌دانید بدون ما چه کسی دوام نمی‌آورد؟ اسرائیل. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/675853" target="_blank">📅 20:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675852">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ترامپ قمارباز: درباره ایران زمان زیادی در اختیار دارم
🔹
ما چندین میلیارد دلار از ونزوئلا درآمد به‌دست می‌آوریم؛ این اتفاق دربارۀ ایران هم خواهد افتاد. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/675852" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675851">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: ممکن است اتفاقات خوبی در مورد ایران رخ دهد
🔹
آنها می‌خواهند ملاقات کنند و ما در حال ملاقات هستیم ؛احتمال دارد که بتوانیم به توافق برسیم. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/675851" target="_blank">📅 20:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675850">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427876ae4e.mp4?token=vFvJLvIAUSPG90rImux3VxEZkPXJYFYPS0tRiOg4RpUleVlY-dWc2Q50owTiIgCwH0yxEAUeYRiaWS5UH2Qu176HnySnMY2rvh7HFX1V36Fxi6u5qTcj3Om9C3PLoi420IzlYSCz3530qyd-mgBvpRXbc9_sH8v9vl2A9y05-uosuHxMJNQj2zjh99qfCm1Uf2lUYJ6XVnvXostBj_GgdGFVfEA0YDxCkrIsDf3gXxLWmMS66MpoKl77YlPhb4tqJxo6OC16EdUo2BC_cHC2Eo0CYQyGNaHKUBWAv7kZQjxH7wri_6L2vqL2OhT0xhV_zId3Cwd2e8H99ZdwikGT0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427876ae4e.mp4?token=vFvJLvIAUSPG90rImux3VxEZkPXJYFYPS0tRiOg4RpUleVlY-dWc2Q50owTiIgCwH0yxEAUeYRiaWS5UH2Qu176HnySnMY2rvh7HFX1V36Fxi6u5qTcj3Om9C3PLoi420IzlYSCz3530qyd-mgBvpRXbc9_sH8v9vl2A9y05-uosuHxMJNQj2zjh99qfCm1Uf2lUYJ6XVnvXostBj_GgdGFVfEA0YDxCkrIsDf3gXxLWmMS66MpoKl77YlPhb4tqJxo6OC16EdUo2BC_cHC2Eo0CYQyGNaHKUBWAv7kZQjxH7wri_6L2vqL2OhT0xhV_zId3Cwd2e8H99ZdwikGT0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به جهنم
🔹
لیندسی گراهام، سناتور جمهوری‌خواه و جنگ طلب واشنگتن که همواره مواضع بسیار تندی علیه کشورمان اتخاذ می‌کرد و خواستار اقدام نظامی علیه ایران شد، در شامگاه شنبه، بر اثر یک بیماری مرد. گراهام سال‌های زیادی علیه ایران و در حمایت بی‌قیدوشرط از اسرائیل…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/675850" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675849">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
محاصره دریایی یمن علیه عربستان؛ صنعا معادله «محاصره در برابر محاصره» را اجرایی کرد
🔹
نیروهای مسلح یمن با صدور بیانیه‌ای رسمی در پاسخ به محاصره ۱۲ ساله این کشور، از آغاز تحریم و محاصره کامل ناوبری دریایی علیه عربستان سعودی خبر دادند.
🔹
صنعا با تأکید بر آمادگی…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/675849" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675848">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a086966c85.mp4?token=Rt5V9rlXqmq4vZwcDnRePgM0tQM4kVv0QGIzzNwq6dTMySaYy0otfMAZm6u56TmaYjSUxLQZaccaFUtqBA0jG1aJzP5W-eEyMXUaKwUL4biZHymGw4Tg6VbpATcn20nxneyKE5-qKAZhhiw5EhvhMTwvS-uE4ppn9diL8I6BMsu-VoHKKx0Juh1QOMqbD6SERTHNQ5IhqJN9FUCFCinYQyDJU1sxev9VSlKot1Cs0znYGMs_4hFr4HF9wHlxdzVWeiBsbNlSbNAPsrAVS63qWQqvPsdvsV59ATG9_faZMr24p-ucYcuDpwFSuqvvyOzOzEjnU4vyY0WZ5I9df2IdvI8O1_R6GoQpxRfFpZxhC-BYA_zq2E8VmKEnMWeBwuVedteDrKQACiIcyp_C88kDnnV_B6Nc2xei-HqAqmtnwjituWRcoxJmT9G3uBgFGU3aTK_wAKLtd4rpADg_RuYNdusYMeY8COvZOYyPfc2NJSb82H7KrZKxK_tjvl4kHdC6YPnIIoeEdSidO_O9Y0hA0uckLW7tApuAy1qyFKXDM_kbMqVpLFYectYfJPz4TYymeJgu8IE_B7kOe7aj2Q863lN2EgV0y2MTxO5swFFSgouvotWDMd3EuyP3FSfWNqPpBKZEQOssHhZL2yvF4GAxpVUBLlAJxkd7o8hp4kVwW6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a086966c85.mp4?token=Rt5V9rlXqmq4vZwcDnRePgM0tQM4kVv0QGIzzNwq6dTMySaYy0otfMAZm6u56TmaYjSUxLQZaccaFUtqBA0jG1aJzP5W-eEyMXUaKwUL4biZHymGw4Tg6VbpATcn20nxneyKE5-qKAZhhiw5EhvhMTwvS-uE4ppn9diL8I6BMsu-VoHKKx0Juh1QOMqbD6SERTHNQ5IhqJN9FUCFCinYQyDJU1sxev9VSlKot1Cs0znYGMs_4hFr4HF9wHlxdzVWeiBsbNlSbNAPsrAVS63qWQqvPsdvsV59ATG9_faZMr24p-ucYcuDpwFSuqvvyOzOzEjnU4vyY0WZ5I9df2IdvI8O1_R6GoQpxRfFpZxhC-BYA_zq2E8VmKEnMWeBwuVedteDrKQACiIcyp_C88kDnnV_B6Nc2xei-HqAqmtnwjituWRcoxJmT9G3uBgFGU3aTK_wAKLtd4rpADg_RuYNdusYMeY8COvZOYyPfc2NJSb82H7KrZKxK_tjvl4kHdC6YPnIIoeEdSidO_O9Y0hA0uckLW7tApuAy1qyFKXDM_kbMqVpLFYectYfJPz4TYymeJgu8IE_B7kOe7aj2Q863lN2EgV0y2MTxO5swFFSgouvotWDMd3EuyP3FSfWNqPpBKZEQOssHhZL2yvF4GAxpVUBLlAJxkd7o8hp4kVwW6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور بعضی از وام‌ها به صورت نامحسوس بیشتر از سود، ضرر دارن؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/675848" target="_blank">📅 20:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675847">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjtqp5rX4xNebKvzxkPainx3hjGocIP2gOYaRcSMSVHsgSH5qvUBrEfdYq--T9DVxLwxa6nQb0Xlnhoy5KkouaqMEXGmxfEVFcYAB-q-EBhTQkXYVyhEHANHISwFOaCc8pCuVaBnjp_7IVhuk84j-257GzQchkdaevBDU4m4NEnui-yZkV5CkjzwVXHiMd4MnptVePLLg8s7q59SC5ZHuSyZhE0GQ0E8Rbwdc_ARk8-56x3IddHL-2q462_21oOU8786xYzzpolPq121iRSff9QMPXFrRBkYU9WpjFJSCU9LNWK1bQpSdGC7FgElbNeBlfr9HVYNkfMZr9BtaRg_2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/675847" target="_blank">📅 20:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675846">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ezf7-o6XZe2s30ar8_lDEnuYwFaVk3r3phzK1YNvcRiA-A-IkvEcorUOmbOEIzd7EzS8DZ0RVfcPBBEO1z4hvjjudLNmGa8ZWRFClPUS-KZZNLm5lY9cz1SMypvjOImekS1y4IGZbAz--ZLtp0Lt3UbeMEsvjkH-A6G5G2BAsoBP2DbTKGv2Kub5FhB6c7kHqzKYOtc4v16HdAxobE6pBc1uFZDD6jjmS2QiUDrNCfhAqdWtIuAgVVR8VVr4WtN3ATOOs-hMuLmjdQ_OvZ4Ts4-hY1KeEMGj4hFTJE2ZuZHL9BCTB0mt2V2wtdvSEEtkdjP2QqPL_7dxsMXSNbxfEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
بزرگ‌ترین جشنواره فروش عمده بازرگانی رنجبر آغاز شد!
✨
🎉
از ۵ تا ۱۵ مرداد، انواع روتختی، شال مبل، روفرشی و پتوهای برند شادیلون را با قیمت همکاری  و اقساط ۱۰۰ روزه تهیه کنید.
🚚
ارسال به سراسر کشور | ویژه فروشگاه‌ها، عمده‌فروشان و همکاران حوزه کالای خواب.
📩
برای دریافت لیست قیمت، موجودی روز و شرایط همکاری، فقط کلمه «جشنواره» را در دایرکت ارسال کنید.
🌐
RanjbarTrading.com
📥
دایرکت تلگرام:
@ranjbartrading_com
📢
کانال تلگرام:
https://t.me/ranjbartrading_general
📞
راه‌های ارتباطی:
☎️
۰۵۱-۳۳۶۶۶۵۰۰
📱
۰۹۱۵۲۵۰۳۲۰۶
📱
۰۹۱۵۰۴۴۴۵۹۱
🌿
بازرگانی رنجبر؛ همراه همیشگی همکاران در سراسر کشور.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/675846" target="_blank">📅 20:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675845">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
نگرانی از تامین و کمبود دارو کاهش یافت
🔹
با وجود نگرانی‌ها درباره محدودیت‌های حمل‌ونقل، آمارها نشان می‌دهد حدود ۳۵ درصد واردات دارو و مواد اولیه از مسیر زمینی و ۵ درصد از مسیر هوایی انجام می‌شود. از سوی دیگر، دارو و مواد اولیه دارویی تنها ۰.۲۳ تا ۰.۴ درصد از وزن کل واردات کشور را تشکیل می‌دهند.
🔹
موضوعی که بنا به گفته مسئولان، به دلیل وزن کم، افزایش واردات هوایی و زمینی را امکان‌پذیر کرده و می‌تواند مسیر واردات دریایی را تا حد زیادی پوشش دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/675845" target="_blank">📅 20:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675844">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ادعای خوک نجس: به درخواست میانجی‌ها حملات را متوقف کردم
🔹
جمعه گذشته به درخواست کشور‌های میانجی تصمیم به توقف حملات گرفته تا فرصت دیگری برای مذاکرات فراهم شود.
🔹
طرف‌های در ارتباط با ایران از او خواسته‌اند «شلیک نکند». او همچنین ادعا کرد ایران خواهان دستیابی…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/675844" target="_blank">📅 20:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675843">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
بیش از ۱.۸ میلیون زائر اربعین وارد عراق شدند
ستاد اطلاع‌رسانی امنیتی عراق:
🔹
تاکنون بیش از یک میلیون و ۸۱۳ هزار زائر از ۱۷۲ ملیت مختلف برای شرکت در مراسم اربعین وارد این کشور شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/675843" target="_blank">📅 19:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675842">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4-zgl-06fStRjFnvmGTv7I4jtpMuUDJ-RTo-tPFGjZelOpXHt6K-sDEipXJHoP94s4VuIlLyFJ9I6-Vf7MdAoES-FNFW8EJyMBfUGlFIXFqLs5lHgIqp_9tlgQyKfNOPanR3lBY3CBLLd2gerCiTewatKiXQZLpwCe-OmSastfVbqRLZTZvT-ug1jzQwVysnULbkAcpR1FXlPa57Ef9aP2FE-UA0XbO8JkmSqqnIyfR_SI7nyXKlpo7Nm-JqkZfMPXOU2yss_IqDarWdTga-Rx3_66QeWmnabCZhTK0elIb3yDtdmEMyLBkQ6UDbp9Q7Nq4BL6WeCviXsE8vNYYjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نبرد روی میز
🔹
در شرایطی که معادلات منطقه‌ای همچنان پرتنش است، میز مذاکره به صحنه‌ای دیگر از نبرد تبدیل شده؛ جایی که هر واژه، امتیاز و موضع، بخشی از موازنه قدرت را رقم می‌زند. اکنون دیپلماسی نه در برابر جنگ، بلکه در امتداد آن تعریف می‌شود و گفت‌وگو، ابزاری برای پیشبرد اهدافی است که پیش‌تر در میدان دنبال می‌شد. اعلام آمادگی ایران برای ادامه مذاکرات در ژنو، دوحه یا اسلام‌آباد، از تغییر میدان تقابل حکایت دارد، نه پایان آن.
🔹
هشتصدوبیست‌ویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/675842" target="_blank">📅 19:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675841">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادعای مقام صهیونیست درباره نگرانی از مداخله خارجی در انتخابات
دیوید زینی:
🔹
ایران، روسیه و چین در تلاش برای اخلال در روند انتخابات اسرائیل هستند و این موضوع از نگرانی‌های اصلی نهادهای اطلاعاتی این رژیم، به‌ویژه شاباک، به شمار می‌رود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/675841" target="_blank">📅 19:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675840">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی مجلس: کشور در وضعیتی نیست که بتوان قیمت بنزین را افزایش داد اما به دولت این اجازه داده شده است
رضا سپهوند، سخنگوی کمیسیون انرژی مجلس، در
#گفتگو
با خبرفوری:
🔹
دولت می‌تواند هرسال و هرفصل قیمت حامل‌های انرژی را افزایش بدهد. در قانون بودجه ۱۴۰۵ هم ممانعتی برای افزایش قیمت حامل‌های انرژی از جمله بنزین وجود ندارد.
🔹
در مورد برق و گاز افزایش قیمت اتفاق افتاده است. پیش‌بینی می‌شود اگر قیمت نرخ سومبه ۱۰ هزار تومان برسد حدود ۴ تا ۵ میلیون لیتر مصرف بنزین کاهش پیدا کند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/675840" target="_blank">📅 19:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675839">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqotd4EOwpTm_7TAkJ1lFXxfGf6FAxDbBQKz9WJDloK9qH4fomGDiEX4QmNYqjtU1ggN2qFf7fJ6fvkrwIG3NrZ23drVnAG7DQiYKJivVxtVll1X8EE1nnQf8QPTi-rwATfGkebWx0GKEcjTurnVPeXNGox0sjJMyEILDvppMPJJLvfRVedCem3M1gMtlf-ELoffI01n78XtvQtJDLG_I42WBiJVYwayKx9qI-sgaiKcJs6Hvpl1V89Q-T3VhZEe_kR7tJXNsaBxgOlS6kP4r871BfeSoeYyjYe91akE60iOuSo7jkSCRw_Sk4HHY3c92CgtoBDdbTS-EAl8E-zc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای شفق‌نیوز: آمریکا با تسویه غیرنقدی ۱۱ میلیارد دلار بدهی عراق به ایران موافقت کرد
یکی از اعضای کمیته برق و انرژی پارلمان عراق:
🔹
واشنگتن به بغداد اجازه می‌دهد بدهی‌های معوقه ایران برای واردات گاز را از طریق تأمین کالا، از جمله غذا و دارو، به جای انتقال پول نقد، تسویه کند.
🔹
ریاض عدی به شفق نیوز گفت که ایران حدود ۱۱ میلیارد دلار طلب پرداخت نشده از عراق دارد که بخشی از این مبلغ در حال حاضر در بانک تجارت عراق (TBI) نگهداری می‌شود، اما به دلیل تحریم‌های آمریکا علیه ایران، قابل انتقال نیست./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/675839" target="_blank">📅 19:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675838">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167fec05e0.mp4?token=IXv5JDayXuihtbls3t3RhDWd586Xcqn2iv6M9GAIhFXSPHn5DF2TL5eHasfWsvp51bBVt4p24towOGZpyCN5RnKl8ne1QwE5ssKJ-UpaCEwaZvfYW88QXHzhfhoOHDzCVVDAc8NXNOyPxhvLhn8grEP4sCeV3YO0GP4H_dewbxmwyAICBro-TRSE-LNwbzC3y-riJayTMBJ1UuNIjb8lxUDA9JCanqMiMhaiozhsHVq6ewWDgdWWPiYk32F3Bj_Ln3cHTjFgby8rqch6Aes5DbBmt90LaZqA8zhBcbmBe0qv8zVI8-LkG8NLi9X42jSx96ml276ag2bu9ZlYk4qFbJTKpUlxILTXwc5h8adb1K2nJDu6omfd7qsNj9h7I2xmqiGQ32FyKD5OLsgH-uwLOiy0TKsLiYgSDuCQ1L-_gy2Pmkbh_D66LzgGrSHLAkZsYv4YmsMPL2Kcp5OCI3U-ZbqGEdc02O8tTSEiN75JJPDxXEjnMUP4sbkiTOmmVJR7gNR4oPv3X0p-s8_meZs6NEU24D6pxtyCQixlSFrJ9oo2nu_IIK1p71kk-e-HT4i96nqZNF7JZal7HG8AWohyltLXiQQvUHVSHODGtGOlwC7NfaYslsjUZJ27uez7ib0y0QLIrgqsZ6eliDbZnpTJi0PB1Qz4oD0xrfKHKzXiQPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167fec05e0.mp4?token=IXv5JDayXuihtbls3t3RhDWd586Xcqn2iv6M9GAIhFXSPHn5DF2TL5eHasfWsvp51bBVt4p24towOGZpyCN5RnKl8ne1QwE5ssKJ-UpaCEwaZvfYW88QXHzhfhoOHDzCVVDAc8NXNOyPxhvLhn8grEP4sCeV3YO0GP4H_dewbxmwyAICBro-TRSE-LNwbzC3y-riJayTMBJ1UuNIjb8lxUDA9JCanqMiMhaiozhsHVq6ewWDgdWWPiYk32F3Bj_Ln3cHTjFgby8rqch6Aes5DbBmt90LaZqA8zhBcbmBe0qv8zVI8-LkG8NLi9X42jSx96ml276ag2bu9ZlYk4qFbJTKpUlxILTXwc5h8adb1K2nJDu6omfd7qsNj9h7I2xmqiGQ32FyKD5OLsgH-uwLOiy0TKsLiYgSDuCQ1L-_gy2Pmkbh_D66LzgGrSHLAkZsYv4YmsMPL2Kcp5OCI3U-ZbqGEdc02O8tTSEiN75JJPDxXEjnMUP4sbkiTOmmVJR7gNR4oPv3X0p-s8_meZs6NEU24D6pxtyCQixlSFrJ9oo2nu_IIK1p71kk-e-HT4i96nqZNF7JZal7HG8AWohyltLXiQQvUHVSHODGtGOlwC7NfaYslsjUZJ27uez7ib0y0QLIrgqsZ6eliDbZnpTJi0PB1Qz4oD0xrfKHKzXiQPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بررسی تصاویری که ابعاد واقعی انهدام پایگاه های آمریکا را فاش می‌کند
کارشناس کانادایی:
🔹
انهدام رادارهای راهبردی و دوربرد توسط ایران، شکاف‌های عظیمی در پدافند موشکی آمریکا و اسرائیل ایجاد کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/675838" target="_blank">📅 19:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675837">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
منابع سوری: ارتش رژیم صهیونیستی درحال پیشروی به خاک سوریه از سمت حومه غربی درعا است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/675837" target="_blank">📅 19:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675833">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nobxFH51m6xNqaXPfECYrcKfS0NH5zft4pt62Tt7MJPSzb572QL1fIhHUiMqcq3Lp8tD-Czgcrvj6_F_FSrSJI4k_ZjuaBYO54-2fvdjyw7oq0gmc4NBnGXVhlZgbfQkFMFBQGhP2Z3l48X3sLZVEQj0xhdCIqMGpt67LLPAkpECRxam58NGyt53wwQ6wFk0-A4Pdvp1z2-N7GsLrTkk0NCFkaqjnHiiskCEhCvvcNHSAn_yvzUsfawarX9WF8H8dyblKsMZKlGGNsTMUOAB00Qz901eoKHSLeZYPx3oH9_xCmE_qC1KQw75wQIFyMBfuce_c5R56L_nRoVawlxptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JphjDYkCvUoekIlZGHJhlOeBdAR0euFRG_8AJHPgwLpFfVo4zrBtHDzd8l1HrzyobZV29a6hV7FZIPvyphOuKtj9_1e-BPY_X2gHHCfHB_452x8bxdx6LwuahZGvhb1Sinj-Wvpp0UwhMB9Uz9aCIICvz3IMlrtb9KA2P6lyv15LwX3jsI7MJPN3tvYToJpXF-Y79_BOStDiJVptbic4mDuMKnUt1fRd68KgEfaPhP-2a6PhKzPzX9SRgEWqJe0Iz-2G_H7DD5kJJmyT0pK66VPWIEWYE8nhnhJ9saWK6ftkRxtheVAyC29Y1LPANG9l09UibnETmx0Y0faPDlJ0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JC5kTDL4nWKBAyYPMtmXn2h9b83YXslU2Z5l44vHefK1a4nUZHOxS2gRRg5wE9-EfcT_qPuvNMu7KRIXz2cbiZbMfytlRBLLhBRogDIyz-Hfy4apKjb8pmX2QZcuRaaNcxXWJZ3jJlw7Yymi4GK3Yx51NEDUVCDQRhrvIgk-QrQ6k-ftlZv9kEUA0ydhRFMSXXWFeC0oCS0-IzABTBLc7dIOep3kBr5qAr9Sy5mCGBvgK5HX73eY8MsJ6aZo6QC25QffYVMBxK1i4Htgeq8zwJYVQtX04AOuEdSD7B90cdD7xvIyqhXrMPTPmp5u3TdG4g3ZK9ura6UVFPB1Wtu5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0QJAFEOZnPHukmEHlP-ycPA3qr5DlM_kOn2Qxr8UaLHbvnvNEPzSxaAGMsdxTxKimoLhj3wP4bwEifSLjxslhEdSc5NeISR7jOBX9xQIrEpi46I8CgkG0ZRWyFDij6q5NyLOEG_xj70SaqXafWic1Pvs9yCzipS89OIhC6t_ZhENoytZuJutNx2A5W7sPsA7RUJ6rDXUb44Si1wMmWi3ddEYZUITRbbdiAna7RNIrVTuWHZFiyngBJvZtujHUQt_TBywu6iz7_eUVNtkeoQuKkfK_xa93Casx1q455RhqC8kaMzS36xmUUIWVgOfDBmF5uDJ8ibuvngDlhuUoArTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پرفروش‌ترین فیلم‌های سینمایی ایران در سالی که گذشت؛ مرد عینکی ۲ میلیون و ۳۵۰ هزار بلیط فروخت
@Tv_Fori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/675833" target="_blank">📅 19:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675832">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 بزرگ‌ترین خطر آینده جهان از نظر شما چیست؟</h4>
<ul>
<li>✓ آلودگی و مشکلات زیست‌محیطی</li>
<li>✓ نابرابری‌های اجتماعی</li>
<li>✓ جنگ‌های فراگیر و گسترده</li>
<li>✓ بیماری‌های عفونی و همه‌گیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/675832" target="_blank">📅 19:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675831">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
آمارهای ادعایی سازمان تروریستی سنتکام از محاصره علیه ایران
ادعای ستاد فرماندهی مرکزی آمریکا (سنتکام) در بیانیه‌ای:
🔹
این سازمان تروریستی از زمان اجرای محاصره علیه ایران ۱۷ کشتی را منحرف و ۲ کشتی را بازرسی کرده و ۲ کشتی دیگر را هم از کار انداخته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/675831" target="_blank">📅 19:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675830">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700364be95.mp4?token=YPk5r2fjxP9gqWij-tOvG7PmLwDtN-ZJxmXO3l90EfXk0MnicRLOHmxlw0UaagQv3ObURkodUGGZ7K1VIEDAW-kZF4FahP-Ah_YhOjIPLAlFnI5Cswi0CoYxEtFAmJMxCzJ49oNiuQBHovpZJhHRrFTaJ7yMyL9b9pAV0jnaeJLQd9g4XDMlHlsIdgBQwlZ0_96zSbxhRkAFULU5V9nh7cUyD6aShEQWBD_hsfBwKYyptQM36I9hwsNFgBhpQ4xdmjJ_NXxgDzUb8rPqU0DhcXT5JJxEEpk1L-1WOyEadTIREQ47ZRRVGmVNE4WM1nnmkhrLsxcD2aY69FmlxtvdcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700364be95.mp4?token=YPk5r2fjxP9gqWij-tOvG7PmLwDtN-ZJxmXO3l90EfXk0MnicRLOHmxlw0UaagQv3ObURkodUGGZ7K1VIEDAW-kZF4FahP-Ah_YhOjIPLAlFnI5Cswi0CoYxEtFAmJMxCzJ49oNiuQBHovpZJhHRrFTaJ7yMyL9b9pAV0jnaeJLQd9g4XDMlHlsIdgBQwlZ0_96zSbxhRkAFULU5V9nh7cUyD6aShEQWBD_hsfBwKYyptQM36I9hwsNFgBhpQ4xdmjJ_NXxgDzUb8rPqU0DhcXT5JJxEEpk1L-1WOyEadTIREQ47ZRRVGmVNE4WM1nnmkhrLsxcD2aY69FmlxtvdcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیراندازی نزدیک کنسولگری آمریکا در تورنتوی کانادا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/675830" target="_blank">📅 19:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675829">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ضریب نفوذ بیمه در ایران فقط ۲.۲۸ درصد
🔹
با وجود رشد ضریب نفوذ بیمه در ایران به ۲.۲۸ درصد، این شاخص همچنان فاصله قابل‌توجهی با میانگین جهانی ۷.۱ درصد دارد. این رقم در کشورهای توسعه‌یافته به ۹.۵ درصد و در چین به ۳.۹ درصد می‌رسد. ضریب نفوذ بیمه از تقسیم حق بیمه تولیدی بر تولید ناخالص داخلی به دست می‌آید./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/675829" target="_blank">📅 19:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675828">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c298eb37e.mp4?token=aKOLSrglp1eIOPJK55ZOrQphvGXvNPHoqHHKuWvh64dT1k8EyBVVenVMVt1pquiNCUpeI8-bYA9ZfQ3gE_f0m3aw7EP7ec9NHuO4qdKKv4WkawQkXczwFjbgc8PlkEpV9U05pMmApKjlXEAB7FtaNAckH00Clt38vmeYRr2cyzhyWntnY6eR_RrHp4TKk2_CwTMn-P5Quk2g1H5eHDS_7XC0WEjeASEYIxEUVo7aiFXo4DS9fLJsNjN7-MKq4vSWo8xv7KwJ_xAm_ztSadO3xvqRyhk8LhihFvUID3xG9DtTd0pep9x8M1bBQmMzT9MguQMZcI3SeX6aL8AW4VhxgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c298eb37e.mp4?token=aKOLSrglp1eIOPJK55ZOrQphvGXvNPHoqHHKuWvh64dT1k8EyBVVenVMVt1pquiNCUpeI8-bYA9ZfQ3gE_f0m3aw7EP7ec9NHuO4qdKKv4WkawQkXczwFjbgc8PlkEpV9U05pMmApKjlXEAB7FtaNAckH00Clt38vmeYRr2cyzhyWntnY6eR_RrHp4TKk2_CwTMn-P5Quk2g1H5eHDS_7XC0WEjeASEYIxEUVo7aiFXo4DS9fLJsNjN7-MKq4vSWo8xv7KwJ_xAm_ztSadO3xvqRyhk8LhihFvUID3xG9DtTd0pep9x8M1bBQmMzT9MguQMZcI3SeX6aL8AW4VhxgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فضائلی: آیت الله سید مجتبی خامنه‌ای هم مانند رهبر شهید، مذاکره را حرام نمی‌داند
عضو دفتر حفظ و نشر آثار رهبر انقلاب:
🔹
در سیاست جمهوری اسلامی، اصل بر تأمین منافع و امنیت ملی است و بر همین اساس، مذاکره نیز حرام دانسته نمی‌شود و می‌تواند همزمان با پیگیری تقابل و انتقام در چارچوب منافع کشور دنبال شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/675828" target="_blank">📅 19:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675827">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
دادستانی تهران علیه نماینده اسبق مجلس و یک رسانه اعلام جرم کرد
🔹
دادستانی تهران در پی انتشار اظهارات یک نماینده اسبق مجلس که سابقه ریاست کمیسیون امنیت ملی را داشته، علیه او و رسانه منتشرکننده اعلام جرم و برای هر دو پرونده قضایی تشکیل داد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/675827" target="_blank">📅 19:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675826">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ابوالفتح: دوران پذیرش تلفات در آمریکا تمام شده است
امیرعلی ابوالفتح، کارشناس سیاسی در
#گفتگو
با خبرفوری:
🔹
اکنون که جنگ زمینی شروع نشده، آمریکا ۱۷ کشته داده است. دوران اینکه آمریکایی‌ها ۵۰۰۰ یا ۲۰۰۰۰ کشته بدهند و مردم بپذیرند گذشته است؛ الان برای ۱۰ کشته هم اعتراض می‌کنند.
🔹
اگرچه روی کاغذ احتمال حمله وجود دارد، اما به لحاظ عملیاتی، هزینه و فایده آن فعلاً باعث تردید آمریکایی‌ها شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/675826" target="_blank">📅 19:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675824">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSI4ZhDSg1iEkV-iatmdY_4R8GJTVWAo01ddUu8edjEeIDrfvfMRCbt2WNhTZa4GBJMlAPa0o5s9jgVSvhoL_GIjOtoI7NcOykSeJ0r4Zw5sK6kd3Khuwfkt13JGWRtEL61s8qDB1RtFmIlSyBC85W91it6s0pvoGDP1jocfwJZ553tqJOlQIpTo1SsQp_EbymbCqTJXeHWSi5R1lBZ9FeqrRpXvPbJSVDSYZqx27Nde8XAtW_Z19RkCfk0i3hNIgmYLwmgW3kOLg6KfQdTWmaZNcboBpo_abvVzbQrOc9jkudvKGhxwOX6mUAB1Gx2OARJfohNX_XIzrzsy2WBtBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توت‌عنخ‌آمون؛ فرعونی که پس از ۳ هزار سال با «نفرین مقبره» دوباره جهان را تسخیر کرد
🔹
توت‌عنخ‌آمون، فرعون نوجوان مصر باستان، حدود ۳۳۰۰ سال پیش در ۱۸ یا ۱۹ سالگی درگذشت و برای قرن‌ها در دل «دره پادشاهان» فراموش شد. او در زمان حیاتش چندان مشهور نبود و تنها…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/675824" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675823">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1afccbdfd.mp4?token=PdE1P8APPvpwgdiAA-B9hSIhgCWYQck47otqSZ98gL8VcjXdPhPg80wGAMgf6dE4uGsDoJRut0yzcxm3kj-qWJIwnKi6KzFrMdt_3q-ITZiZJU-ZMa9plWSe5qp7LQFAMSpf2b6MLeGEz-F8fqT60EPsh8W_i_7t2UTRDW7LEuIVna0xuYoAHRjVPNS6cw9BbKwMDZ3a8bIRKE7K0Tm3k6AwJgy0kjosYYf2n970HGU16xRL3p_jOfAYNds58-Wo4vpw6jas_XSPhc32lAqp9-2C2HRcrqaIhwQo8TuTzyuD1E3iOZIN-1FsdscpOj6cvaLpwnUqH_41ItOd8mgVdrrPMQYBZzE7WSeEG-jh_AB8ig5sZZboN0HHSGH4hk0Qk722XBYGzENjMt3gHAfiKsly7R43QOvyLDf6cBjwqxRrmPxoNC9OK_u25Z1MReTSMxB5Jo4zrl5hY9qRSIgfL1KuDN54CR9nlrpEg_dZpP4SbA_o-_IaupQPt60pBh47383UmwMRYG32tH7uQShigwppVUAmf9W-Gd636J2ucORL86m_EgARfGmL7gTedUBp1gkJa5cL5EuokDYgUKpAnV0XCk9DJMmO1ecnEo4rLYnqTCEnMyWsDf27z33IAiPoGNxgDGM4qre94GM8R3xNGD66qyjSlYosR_yXTx8fAxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1afccbdfd.mp4?token=PdE1P8APPvpwgdiAA-B9hSIhgCWYQck47otqSZ98gL8VcjXdPhPg80wGAMgf6dE4uGsDoJRut0yzcxm3kj-qWJIwnKi6KzFrMdt_3q-ITZiZJU-ZMa9plWSe5qp7LQFAMSpf2b6MLeGEz-F8fqT60EPsh8W_i_7t2UTRDW7LEuIVna0xuYoAHRjVPNS6cw9BbKwMDZ3a8bIRKE7K0Tm3k6AwJgy0kjosYYf2n970HGU16xRL3p_jOfAYNds58-Wo4vpw6jas_XSPhc32lAqp9-2C2HRcrqaIhwQo8TuTzyuD1E3iOZIN-1FsdscpOj6cvaLpwnUqH_41ItOd8mgVdrrPMQYBZzE7WSeEG-jh_AB8ig5sZZboN0HHSGH4hk0Qk722XBYGzENjMt3gHAfiKsly7R43QOvyLDf6cBjwqxRrmPxoNC9OK_u25Z1MReTSMxB5Jo4zrl5hY9qRSIgfL1KuDN54CR9nlrpEg_dZpP4SbA_o-_IaupQPt60pBh47383UmwMRYG32tH7uQShigwppVUAmf9W-Gd636J2ucORL86m_EgARfGmL7gTedUBp1gkJa5cL5EuokDYgUKpAnV0XCk9DJMmO1ecnEo4rLYnqTCEnMyWsDf27z33IAiPoGNxgDGM4qre94GM8R3xNGD66qyjSlYosR_yXTx8fAxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😣
گردنت درد می‌کنه؟ شونه‌هات افتاده؟ موقع راه رفتن احساس می‌کنی قوز کردی؟
فرقی نمی‌کنه خانه‌دار باشی، کارمند، دانشجو، راننده یا حتی ساعت‌های زیادی با موبایل کار کنی؛ نشستن و ایستادن نادرست به مرور باعث قوز، افتادگی شانه، گردن‌درد و درد قسمت بالای کمر می‌شود.
✅
قوزبند طبی با طراحی ارگونومیک به قرار گرفتن صحیح شانه‌ها کمک می‌کند
⭐️
مناسب برای:
✔️
افرادی که شانه و گردن درد دارند.
✔️
خانم‌های خانه‌دار که ساعت‌ها مشغول کار هستند.
✔️
کارمندان و دانشجویان.
✔️
راننده‌ها.
✔️
کسانی که زیاد از موبایل یا لپ‌تاپ استفاده می‌کنند.
✔️
افرادی که احساس می‌کنند هنگام راه رفتن یا نشستن قوز می‌کنند.
💰
قیمت قبل: 1,598,000 تومان
🔥
قیمت ویژه: 1,098,000 تومان
🚚
ارسال به سراسر کشور
💳
پرداخت در محل (در شهرهای دارای این امکان)
⏳
موجودی محدود؛ همین حالا سفارش بده.
👇
https://memarket24.ir/product/brief/38083/180124/</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/675823" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675822">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای سگ‌زرد: در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/675822" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675821">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
حمله جنگنده‌های صهیونیستی به منازل مسکونی جنوب لبنان
🔹
رسانه‌ها از حمله هوایی رژیم صهیونیستی به شهرک طیر ابلعروب در جنوب لبنان خبر دادند.
🔹
جنگنده‌های صهیونیستی ۶ نوبت این منطقه را بمباران کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/675821" target="_blank">📅 18:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675820">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
یورونیوز: سومین هشدار ایران به بلغارستان صادر شد
ادعای یورونیوز:
🔹
ایران پس از آنکه بلغارستان اجازه استفاده از پایگاه‌های نظامی خود را به آمریکا داد، هشدار تازه‌ای به این کشور صادر کرد. اقدامی که تنش‌های دیپلماتیک میان تهران و صوفیه را تشدید کرده است.
🔹
سومین هشدار تهران به بلغارستان پس از آن صادر شد که ترامپ، به‌طور علنی از رومن رادف، نخست‌وزیر بلغارستان، به‌دلیل فراهم کردن امکان استفاده از پایگاه‌های هوایی این کشور قدردانی کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/675820" target="_blank">📅 18:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675819">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1554001316.mp4?token=lompJUCoGNuQVuokniQHRQIZK1lRVtFaypPknX8AwFGEY6j5KN42HTDLaSP4_oXUde7q4mZ6S8NPwjjaNWBlHW_IUJ_5R4P3zpljem7ggQf371GFQanF8URzSkynZ8NQCFrtu-_7mUf3eFzeY4hJPwABuNc2pJM3lJqVxcLnmQdZ9kDOUk0903oEn1YnBkWtTWxC1V2m1xUQtLJdXuHuCrlbJUvFCrzW88AJne0MHeTT5SPj-KTlJV2iDr6mN2ULYg9dK9p2kp5pzIoA_D8clDO9LHvbsgNwvih8_qtwqYdYmk_exCLv0dDsxGIZTEKs3aaloN9Ey1RG3LAYA0rTiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1554001316.mp4?token=lompJUCoGNuQVuokniQHRQIZK1lRVtFaypPknX8AwFGEY6j5KN42HTDLaSP4_oXUde7q4mZ6S8NPwjjaNWBlHW_IUJ_5R4P3zpljem7ggQf371GFQanF8URzSkynZ8NQCFrtu-_7mUf3eFzeY4hJPwABuNc2pJM3lJqVxcLnmQdZ9kDOUk0903oEn1YnBkWtTWxC1V2m1xUQtLJdXuHuCrlbJUvFCrzW88AJne0MHeTT5SPj-KTlJV2iDr6mN2ULYg9dK9p2kp5pzIoA_D8clDO9LHvbsgNwvih8_qtwqYdYmk_exCLv0dDsxGIZTEKs3aaloN9Ey1RG3LAYA0rTiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های دردناک حامد عسگری در حاشیۀ محرم شهر دربارۀ مادر یکی از شهدای مدرسۀ میناب که هر روز ماکارونی درست می‌کند تا شاید فرزندش بازگردد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/675819" target="_blank">📅 18:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675818">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی مجلس: حدود ۴ هزار مگاوات برق به دلیل جنگ از مدار تولید خارج شد/ قطعی‌های برق جنوب به همین خاطر است
رضا سپهوند، سخنگوی کمیسیون انرژی مجلس، در
#گفتگو
با خبرفوری:
🔹
ما گزارشی از قطعی برق به صورت گزینشی و تبعیض‌آمیز نداریم. گاز را همچنان بر اساس قرارداد به ترکیه صادر می‌کنیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/675818" target="_blank">📅 18:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675817">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای سگ‌زرد: در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/675817" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675816">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
تغییر مسیر نفتکش‌های عربستانی برای دوری از حملات یمن
🔹
داده‌های کپلر نشان می‌دهد نفتکش‌های حامل نفت عربستان به‌جای باب‌المندب، مسیرهای کانال سوئز را برای خروج از دریای سرخ انتخاب کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/675816" target="_blank">📅 18:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675815">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVIfVYm_Y9RLXajSgktQUkD3NLyxNouKZvWpwj0Zy-isipv6kijtVdKGgkjtinhGwSvblw2wDPWsbFczrKCxqvG0GtJiBXjMnW7H_AlZKhhCxenT0-x2L4b8cvob0OzaFRzxuDW8TKfttV91uNkAlJ5AEBs2_cZSJ_oXLnIrC1SPz8A49oljgsPA7yI1KWqw1T1oQJjtDUBtdCnP0LUGV2BuXAMPXjsuVXR7eqPWxeYy6dF0Yhg_kg7q0CnUPuV0TMYcyY0U1fe2BwCeP0J-4rJZb6sqgYGiX2fYipq5RbEPivj0M1S1O38YX04qv7XT0ZSSNP3ldtnolTMN3YhdnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای آسوشیتدپرس: میانجی‌ها می‌گویند به پیشرفت‌هایی در مذاکره با آمریکا و ایران رسیده‌اند
ادعای آسوشیتدپرس:
🔹
مقامات منطقه‌ای اعلام کردند که میانجی‌ها در بازگرداندن آمریکا و ایران به مذاکرات، پس از توقف حملات هر دو طرف پس از یک دوره تنش‌های به سرعت رو به افزایش، به پیشرفت‌هایی دست یافته‌اند.
🔹
دو مقام منطقه‌ای که به شرط ناشناس ماندن برای بحث در مورد مذاکرات پشت درهای بسته صحبت کردند، گفتند میانجی‌ها به رهبری قطر و پاکستان در تلاشند تا شکاف بین واشنگتن و تهران را پر کنند تا به توافق آتش‌بس موقت که پس از تبادل آتش از بین رفته بود، بازگردند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/675815" target="_blank">📅 18:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675814">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqNDghtL9RKip-Q3xY0GkiZrGkXKHptUJ45cOQaFPOuOiM4V6ZyGY-xWp8kOl-Jnbybz7SZkg1m8Ik9FzyJ40F7-U6v2g5qcUhDBGG5GNH3iCQhDu0NpFZIkQsQZpDYSA_fSEnVLaQprZn6nrHo1BCeVeUAZ2mDCitdvgvy5HsyYI0QsXPyQju9UZd8_H2xW5TNxpqt5-7phuoZ1SqzQZEM8AXzWvl8JbzP-86b_m49-Vr1G0V4QeU26UdiDLboUiN5IrjKeiL1CbE75WBNE-xbSoixK3ErLFsDfZc9wqE-BpOtnpXueeLj_-DxDm6TfBlOWvQLZ9EgYoBvpTSSbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازیگر سرشناس هالیوود خطاب به نتانیاهو: تو یک دیوانه آدمکش هستی و از عدالت فرار نخواهی کرد
مارک رافالو:
🔹
شما از عدالت فرار نخواهید کرد. شما نمی‌توانید تاریخ را دستکاری کنید.
🔹
بنیامین نتانیاهو، یک دیوانه آدمکش هستید. شما همیشه به همین عنوان به یادگار خواهید ماند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/675814" target="_blank">📅 18:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675813">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
تردد از تنگه هرمز همچنان از مسیر ایران انجام می‌شود
🔹
گزارش‌های اطلاعات دریایی و شبکه سی‌ان‌ان نشان می‌دهد تقریباً همه کشتی‌های عبوری از تنگه هرمز همچنان از مسیر تعیین‌شده ایران استفاده می‌کنند و هیچ کشتی‌ای از کریدور جنوبی مورد حمایت آمریکا در نزدیکی سواحل عمان عبور نکرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/675813" target="_blank">📅 18:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675809">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OL6j58PIcCX8dP1T9aBHB_MfxP8t9rL4Tga5Ef0ROLV_HajqrRcfs2zlHF43ZkC-PcORU_vz2uGf9jDDKphkB3hPLxeqMGl0TPAO8pCzVGzc0bx4lIdqdGwprd4OyOnLXvXwqFn27JGEaiXlV1FIih2co97mk_yZBFLv4X0AlYHEil587fBeAPa9NvQ9hkh7xU7b0WA3ZIloMQYxQMsEA2VzrekpdLmxF6oGzALYFHpWTKwNFWoRqucBhbKWERndVATxywDfFD_xYfvWEQeAIiSJ4bAaIFNQGDvd3wdu4QdN1QwOfa5O73lD1R1BQ5KclPJTafVKVgr2bTaV4O2Ahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnUCkqrpUtc2BeZb_fJQetZcFDJQ2SruxBK6j-CIr-EPXrGh7sFKUmRyrRxAaGCErWYNfthzBPZMItPbEGWNKCNlVmrlIsNYq-MSXt8MTpUzyaQY43ZHhsWYE5kHgJw7U1b9m9WILkcuoLjDjVQMH6S3BdBFElVj2dt4O2gJSSd2YlzjQszquB83D0ZBpo3I96FN5XLNiu-3LgGUVRzTKb4EG5647Vwsln4QLKQgFqbZv0dyJqQQbol_AHxy8BlQwj-MLhBZVHsk7LIoyKXym8gjxISEx8TzaStVzoBs2xqCkgfjJdDiURBc-7fvLqmb3pofbY9Ei91dr2ve1SXvvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEZRPY2EyHnYPIDsruxBBuDsOKoxj7KOhUFByzY8itZZNLYRn_xMHb9Y3r4kPrzaWuoDGp4ObXa3rHkHmO-SgI3NiBIMeTH-5JTvlwChxFzpmXWAvnTyGwHCm-2dfw8wFv9Bt8ryfQcU5wZYnmpC1kxw6oMAftig5T3JRglEh5kC2FYWAXNxkvDYmNsncJgQed6A8m7S3z8Iq-tTxGen4j1bN7yhJw7xdyKZRwempNSIDjgPuyRc3CTwVcUOlcw8pWQBCV0vUUeLIx2Odprln5VKumnyB50o8g8D37nme8o_h8FUU0sd6iiQCU3j83WjjnZx_x9x26aJPM9I7M5soA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLtUyTCotoCNzQPZJu6BigAQZpIIlQP8XvWUjj1GxnBm8AFlRNdPFLiO-9ZLuUy660AdNiqXGpOXcFTWJptATYxKOuodA1HUW4LKtFFuh0-0vKTZkxoK9Q4458fLvvjiS8YBeJt3vAaceKhTn4u4lJWZOlU3zG1jaobG8qbhUP9YXIaVj8d5mu-ICDA3lc0Ran6_BzV2mNOmxob6ibc8VKDMMDJCbuRj75YATxxORBwSOpmD97e0qyYx70IoOEswC8te2rSFba_6HvMkAeGQs_f9BWgSU1ra2aDOn4NvU_G4V-mpvoZ18GQ8ijgEOB2ZqLb0S58sO_DdCwdE_UGQ5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
مدیریت هوشمندانه مصرف با تغییر عادات کوچک، سهمی بزرگ در پایداری شبکه برق کشور داشته باشیم
🔸
تنظیم دمای کولر روی ۲۵ درجه
🔸
استفاده از حالت Sleep برای وسایل
🔸
جداسازی شارژرها از پریز پس از مصرف
🔸
استفاده از ظرفیت کامل ماشین لباسشویی
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/675809" target="_blank">📅 18:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675808">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس کل بانک مرکزی: نرخ تورم ماهانه در تیر ماه نسبت به خرداد نصف شد.
🔹
ترکمنستان: حمله اوکراین به کشتی‌ ایرانی در دریای خز غیر قابل قبول است.
🔹
عضو کمیسیون امنیت ملی: عمان حق قانونی بازگشایی تنگه هرمز بدون هماهنگی با ایران را ندارد.
🔹
گاردین: دقت و قدرت تخریبی حملات ایران به‌شکل قابل‌توجهی بیشتر شده است.
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/675808" target="_blank">📅 18:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675807">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f2710a8ea.mp4?token=SOXEygH30h9oQKNLeBuNmNRTXNdv4D8ZjwMrZAd8DaGYjA40d1TK--REkARHp5s_cwR5XKu6IT-4s4h1SceLee0coRCd4fGtE9hmK39KMMLHWCcF8GPZPSFwGKjWlQPVtKQ39J1XNc68IxRXolZfl9zxSWFDhA1Cri8q2NhmVv7jUj3Gs0WPCK90ybQZ7-gqeGW4oiIh_ZU2chl-_fWXOyuLeJYj_CSdUHPsZxCz4g3EKtbukmluH3VFuDz9KgwTP8pSYGUo_yxMzwoKD4-HeOv2YE--wK365ZoRTBsUxlB3V2KFUfl5n1XnRq4rCxN60OkygQsDPpcS7edB4N-MDjSl09Gee4U-rNWjoIr9pTmY6q3jkjdaZjNdvQrF2vFA1HZDWWJXb4s9MWToE_wd5PlOz9q7I_8kbDXGWW5JCgvlf_4Tum-oiy2lUDDYiuItq65KvhnjF2lhERfsNiguc843evHvKqAIFC95dPv_gmjaBREX4VJ_KZ_v4oZEvsl2QCStG6xiN7MzRoWPCxO5RZ2OA5dpCu_x_f8FH9hKMZmE--O7AKvAyxFiwdBnze3_unfec4TvzCTpBu4MzVb4vnu3wuoDbNtXVln6pVTwQhkrociLUjSo_ZeH8s_DW5fC77soOtyY7Ml0EvgJ9MLBDPOlipqr1CKOXB9e9zw-Zyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f2710a8ea.mp4?token=SOXEygH30h9oQKNLeBuNmNRTXNdv4D8ZjwMrZAd8DaGYjA40d1TK--REkARHp5s_cwR5XKu6IT-4s4h1SceLee0coRCd4fGtE9hmK39KMMLHWCcF8GPZPSFwGKjWlQPVtKQ39J1XNc68IxRXolZfl9zxSWFDhA1Cri8q2NhmVv7jUj3Gs0WPCK90ybQZ7-gqeGW4oiIh_ZU2chl-_fWXOyuLeJYj_CSdUHPsZxCz4g3EKtbukmluH3VFuDz9KgwTP8pSYGUo_yxMzwoKD4-HeOv2YE--wK365ZoRTBsUxlB3V2KFUfl5n1XnRq4rCxN60OkygQsDPpcS7edB4N-MDjSl09Gee4U-rNWjoIr9pTmY6q3jkjdaZjNdvQrF2vFA1HZDWWJXb4s9MWToE_wd5PlOz9q7I_8kbDXGWW5JCgvlf_4Tum-oiy2lUDDYiuItq65KvhnjF2lhERfsNiguc843evHvKqAIFC95dPv_gmjaBREX4VJ_KZ_v4oZEvsl2QCStG6xiN7MzRoWPCxO5RZ2OA5dpCu_x_f8FH9hKMZmE--O7AKvAyxFiwdBnze3_unfec4TvzCTpBu4MzVb4vnu3wuoDbNtXVln6pVTwQhkrociLUjSo_ZeH8s_DW5fC77soOtyY7Ml0EvgJ9MLBDPOlipqr1CKOXB9e9zw-Zyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکی بخون، بدون کنکور
🔹
رشته پزشکی ۹ میلیارد تومان قیمت خورد!
🔹
این شهریه دانشگاه نیست، هزینه ادعایی قبولی در رشته پزشکی است! ماجرا رو ببینید، احتمالا شگفت‌زده می‌شوید...
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/675807" target="_blank">📅 18:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675806">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d677525559.mp4?token=Tqq2ldq5kOhzxlnq-cJ-ZxRDH5wtNlfOtjPN9UybdjCn5je90-R-jmQ99pFH1VqjdwpgRKH1dbvf3mY_RMEaQK866MfZ2VYAEZFBRJ_k9ZkQXqIXtbhlE27upWZSw0iORm8FI9pxJ41toEBFDr9YDvJGokSKPexMvcs1Zes2F0kgRWFU2KyPVS_8Q4UQMymK6huNKIpYe27Mtl7ARXgIMa6AW3KPSjDNrA8UEXZ063GFQ6OX4Q1zYs_dYwWx8-5YZyEhJwHZ0hyVECtpJZfD_kU2FscHVeoIO6-q9jGPi2jU0XOlv2ecxHFHguRzkCWVSwWTw6nFJgefBh-apB0HvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d677525559.mp4?token=Tqq2ldq5kOhzxlnq-cJ-ZxRDH5wtNlfOtjPN9UybdjCn5je90-R-jmQ99pFH1VqjdwpgRKH1dbvf3mY_RMEaQK866MfZ2VYAEZFBRJ_k9ZkQXqIXtbhlE27upWZSw0iORm8FI9pxJ41toEBFDr9YDvJGokSKPexMvcs1Zes2F0kgRWFU2KyPVS_8Q4UQMymK6huNKIpYe27Mtl7ARXgIMa6AW3KPSjDNrA8UEXZ063GFQ6OX4Q1zYs_dYwWx8-5YZyEhJwHZ0hyVECtpJZfD_kU2FscHVeoIO6-q9jGPi2jU0XOlv2ecxHFHguRzkCWVSwWTw6nFJgefBh-apB0HvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا وطنمونه، خاکمونه، محل زندگیمونه؛ ما با این خاک تعریف می‌شیم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/675806" target="_blank">📅 18:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675805">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
‏
افزایش تلفات نظامیان آمریکایی در جنگ علیه ایران
🔹
بر اساس تازه‌ترین آمار منتشر شده در پایگاه داده ردیابی تلفات پنتاگون، تعداد نظامیان آمریکایی که در جنگ علیه ایران زخمی شده‌اند، از ۶۰۰ نفر فراتر رفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/675805" target="_blank">📅 18:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675804">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ایده‌ای نو که از دل پسماندها بیرون می‌آید
کارخانه‌ای که ضایعات از آن جان می‌گیرند و به محصولات مبلمان شهری تبدیل می‌شود
🔹
محسن قضاتلو مدیرعامل سازمان مدیریت پسماند شهرداری تهران: نیوجرسی، دیوارهای بتنی و فلاور باکس‌هایی که در این کارخانه تولید می‌شود بسیار مقرون به‌صرفه‌ار از بازار است
▪️
عبدالمطهر محمدخانی سخنگوی شهرداری تهران:
در مسیر اصلی خیابان‌های آزادی و انقلاب و در ادامه بزرگراه‌هایی مانند شهید همت از این محصولات استفاده خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/675804" target="_blank">📅 18:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675803">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1Bk4vlUaZCuR57bE4Rgnttz0weFsuL4bRed7Ma8kA-Piocd6NeErwX1mcGvfzzz2TTVhC92be8r60EuStTSDHtF9o3_PJzw61D7Hd3YQ1A5NccPubiKQHDvSoAbtumyS9d_1-f_0PkdAVA0fWwBMAgafxatyHQztB0F22lkz91P1_knTZMyRiuHNknC-o5sl1DBf92Nlo5wiglUz-OulY9xFI9K2mGU8jLpXWbYQ0pIvnBS7dr_mZq6mPkdp89hkAnBS2ApCLJd8uj6ONH3BSvJPQCl_AIMaGkoWLu6vMkkBO8zCoDqRGa6PAnveKfEn3mW0cVH75jig1z0_KEvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داروسازی دکتر عبیدی هشتادمین سال فعالیت خود را گرامی می‌دارد
🔹
هشت دهه نقش‌آفرینی در سلامت ایران که از سال ۱۳۲۵ و با پایه‌گذاری نخستین لابراتوار داروسازی کشور توسط دکتر غلامعلی عبیدی آغاز شد و امروز با تمرکز بر کیفیت، نوآوری و ارتقای سلامت انسان‌ها ادامه دارد.
🔹
داروسازی دکتر عبیدی در آغاز دهه نهم فعالیت خود، با تکیه بر دانش، نوآوری و تجربه، همچنان برای افزایش دسترسی جامعه به راهکارهای درمانی اثربخش گام برمی‌دارد.
برای مطالعه متن کامل خبر روی لینک زیر کلیک کنید:
https://abidipharma.com/abidi-80-years?utm_source=messenger&utm_medium=post</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/675803" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675802">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCtt6zJf9moQFbyRvWuiazE2FW3f5PC7MyySN7veFkAU5zdz6NIWgZooQ3LfE-NqzTZBUG5EEJnMCl_W-ArgdG3mqVuS08OedKYuVVmC-0x_umHVmhCaWo-l_t-ADlNHRcejFPPiLFp9Uld_jv1p6o14zr6A4kcKAG3W_SizntGBU2xZjMdjVfW2ZFxwsGkSOP3WVvUcivLDLqCyhCXcDTLPsIf8kA7_54VN_ImosFSgfIqDVswysFv4imhP3K_zXzP7s4IKCeYEW2THJCbUUCUdJ3zYiLdewl3Gs3lOGR1J3Qg-I_rmSWYJzUTKgkUupCZHh1Zl_OEo1QsUaMppdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ژاپن برای مقابله با گرما، یخچال انسانی ساخته که در چند دقیقه کل بدن را خنک می‌کند
🥶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/675802" target="_blank">📅 17:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675801">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afad1b6c3.mp4?token=P5U5wQ0lS4aYcLkwzNqS8tkAugvq9IdYUrsWnV-VWuYeV8l6A6ycPZKYsbwCdF_vEL5QwOSGr7awX8pobHfl1z7_YC_pmUWBKRRD8F1ZAivlSCdqFELEvzEeSXLtn8BapNtiAfznB8Y4zXQMLBQQYeZLj2gs_vFnw6bkXRi6mpsaA9domhcANUtOCCmHVflY7W6ID9_VbaO3-TPgUQxaaXafUtYeZ63mRo9abNnZIqB_7BmezFVhr1856rCXgQzKEdtxvrzYdRRoP13mZbs3TyTrao4Rq6an-lQVisxI-BYYCAiTL8rMo08M2q8D28rYSAn6-OGFrjABXkR37IIb6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afad1b6c3.mp4?token=P5U5wQ0lS4aYcLkwzNqS8tkAugvq9IdYUrsWnV-VWuYeV8l6A6ycPZKYsbwCdF_vEL5QwOSGr7awX8pobHfl1z7_YC_pmUWBKRRD8F1ZAivlSCdqFELEvzEeSXLtn8BapNtiAfznB8Y4zXQMLBQQYeZLj2gs_vFnw6bkXRi6mpsaA9domhcANUtOCCmHVflY7W6ID9_VbaO3-TPgUQxaaXafUtYeZ63mRo9abNnZIqB_7BmezFVhr1856rCXgQzKEdtxvrzYdRRoP13mZbs3TyTrao4Rq6an-lQVisxI-BYYCAiTL8rMo08M2q8D28rYSAn6-OGFrjABXkR37IIb6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک پهپاد ناشناس در استان بابل عراق سقوط کرد
🔹
منابع عربی می‌گویند احتمالا این پهپاد لوکاس آمریکایی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/675801" target="_blank">📅 17:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675800">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی مجلس: جنگ بلندمدت و فرسایشی باعث تخریب زیرساخت‌های ایران می‌شود/ ما نمی‌توانیم در مقابل زورگویی آمریکا کوتاه بیاییم
رضا سپهوند، سخنگوی کمیسیون انرژی مجلس، در
#گفتگو
با خبرفوری:
🔹
در دوگانه جنگ و مذاکره هستیم؛ باید درست بجنگیم و درست مذاکره کنیم. ایراد وارده وجود چند صدایی در کشور هست که پیام خوبی را به دشمنان نمی‌فرستد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/675800" target="_blank">📅 17:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675799">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
بن‌گویر، وزیر امنیت داخلی رژیم صهیونیستی:
مذاکره با ایرانی‌ها هیچ فایده‌ای ندارد
🔹
ترامپ یک تاجر است، اما در مورد ایران بسیار ساده‌لوح است./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/675799" target="_blank">📅 17:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675798">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPDy570FCL0O8_IlP62KsCPb8WhOmjDL6l5SOpiPJYXeHu4WMEXqHgnbdNZwvKoVzegb4eeBMq80iefxK7nZsrMQiMfB2xE3kUj1L1y4t3-7gKTr-UQNPRDjRUyGI83KHIfNnd1xVxPIGDN-VxycE7F6MiYOwviPhc_agv6ySBVwa_lw0bphvZO_J1uP2-PvmmpLoDIZqpGjs8-VNwTy5SPnTj0cQz1d_V22j2LW_FRilj-XJCOgqtU8bWk6Kn4TVZB-BeIFfWNZSBgKM6VfuqJTuQEwr9uYFSdCShH812TFYAmWGlcTHNBkXsJOU72L3dgSRSDEMSnVIBWBcpFqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر کمتر دیده‌شده از حضور رهبر معظم انقلاب در نماز جمعه نصر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/675798" target="_blank">📅 17:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675797">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20909c0975.mp4?token=dW7dHVHoxjI7rb3ThkZZh-XdEQTJhITTRYYQKyjTj2c-vCQ3bpfkKZpmVs7bOKmZ_CQbhhjH-5S_ULTpC4OCb6cxNvWlWPUrra370EEF2NVkuLpK9OiMl-xt5rT77AFchtF7VLhANajtPT8_Im-oAG8wlSyUKFJutFWQ4GCAFefiEH_es8vf-AnV-FxEU3HlZ8JPyQaz4Iyk6r1yv1ATpFV0HRF-2SF9CMrNVGFoEBk_Sh7jQ-OBUd9D3qzoRwsJymm1qfcduSmcPasI8cDvZRfX5cF0aw5D7aqDoT9aQUQfz5j-T9UcvEIvcyw6QrFX3W5gHkSViR5pO0ztwKCP9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20909c0975.mp4?token=dW7dHVHoxjI7rb3ThkZZh-XdEQTJhITTRYYQKyjTj2c-vCQ3bpfkKZpmVs7bOKmZ_CQbhhjH-5S_ULTpC4OCb6cxNvWlWPUrra370EEF2NVkuLpK9OiMl-xt5rT77AFchtF7VLhANajtPT8_Im-oAG8wlSyUKFJutFWQ4GCAFefiEH_es8vf-AnV-FxEU3HlZ8JPyQaz4Iyk6r1yv1ATpFV0HRF-2SF9CMrNVGFoEBk_Sh7jQ-OBUd9D3qzoRwsJymm1qfcduSmcPasI8cDvZRfX5cF0aw5D7aqDoT9aQUQfz5j-T9UcvEIvcyw6QrFX3W5gHkSViR5pO0ztwKCP9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از کاروان‌های زائران اربعین حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/675797" target="_blank">📅 17:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675796">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01c3bc5ed8.mp4?token=psBnnh23-cJvNRrpzeJonO5NtETSIN8y29L_TNrdX8PR_j68QWE35JZQh7fFn96kgB_4h6m7TkWlYU_aLGeLhMvK39Xl1S6X9ULg9nR7OrcgxEPB9j3oqdU3_d4VMoL3Rt9rd4uV3ucqa8Ji8EofPbSZYt6BSH86oouqjX1QsFZRXB3e3OwulW_5yn2Z46W0fBjmjnAa0Yy4SCKeg9uzUKdJqlnmXFesonEPY7b7SQtMUdJxgCGUk96HtLqKGHWgQtNRD9NMZaTAc-hXm8wWtRl7LkvXLRhYWR75Lq4sAVQ6wRikiTlP5-Ao0AIoBcMPIfz2gveVuXmIGIALAKOxkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01c3bc5ed8.mp4?token=psBnnh23-cJvNRrpzeJonO5NtETSIN8y29L_TNrdX8PR_j68QWE35JZQh7fFn96kgB_4h6m7TkWlYU_aLGeLhMvK39Xl1S6X9ULg9nR7OrcgxEPB9j3oqdU3_d4VMoL3Rt9rd4uV3ucqa8Ji8EofPbSZYt6BSH86oouqjX1QsFZRXB3e3OwulW_5yn2Z46W0fBjmjnAa0Yy4SCKeg9uzUKdJqlnmXFesonEPY7b7SQtMUdJxgCGUk96HtLqKGHWgQtNRD9NMZaTAc-hXm8wWtRl7LkvXLRhYWR75Lq4sAVQ6wRikiTlP5-Ao0AIoBcMPIfz2gveVuXmIGIALAKOxkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای جدید از آتش‌سوزی در پالایشگاه نفت جیزان شرکت آرامکوی عربستان سعودی پس از حمله انصارالله یمن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/675796" target="_blank">📅 17:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675795">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e77e1528be.mp4?token=ZkDXzrKtgKjjRBV8psUGneGbNrzI8_7b67cbG5qxqAL7Y6NMK9IPFq_gxMCCkJKfpe5DUrfWAMHMC2wbPduMcaHaAGEogR93c_nVmCjUADIS8VKKwoojQzEdexdABqRcMzxPWYHL65xtWrYT7R1p_39plephpbyv7lWMMvU3I6Z6q6yoEAshErJJ2FVMRbnkUyrMfE_sK79L0SC2Amy8nr7bNUExyNf-AMOF95Ea7FoDowPO_druB78BFaDVMTnv48XpnBrjcEPYBFOpKGrkuc3vNzP4CD6WkRV5Ea_lQyw1Eg_UJPUPZHOv2EU3IXqez3ehaAqD_3FT1D_Qul1LZ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e77e1528be.mp4?token=ZkDXzrKtgKjjRBV8psUGneGbNrzI8_7b67cbG5qxqAL7Y6NMK9IPFq_gxMCCkJKfpe5DUrfWAMHMC2wbPduMcaHaAGEogR93c_nVmCjUADIS8VKKwoojQzEdexdABqRcMzxPWYHL65xtWrYT7R1p_39plephpbyv7lWMMvU3I6Z6q6yoEAshErJJ2FVMRbnkUyrMfE_sK79L0SC2Amy8nr7bNUExyNf-AMOF95Ea7FoDowPO_druB78BFaDVMTnv48XpnBrjcEPYBFOpKGrkuc3vNzP4CD6WkRV5Ea_lQyw1Eg_UJPUPZHOv2EU3IXqez3ehaAqD_3FT1D_Qul1LZ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی رؤیای غرب به درخواست کمک مالی ختم می‌شود، اشکان خطیبی به جمع‌آوری کمک مالی روی آورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/675795" target="_blank">📅 17:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675794">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
تیزر قسمت چهاردهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای حسین صاحبی بزاز یکی از بهترین مخترعان کشور که به دلیل بیماری سرطان خون، تحت درمان قرار گرفته و در یکی از مراحل درمان با اشتباه یک پرستار خونریزی مغزی کرده و روح از جسم جدا شده و در دشتی زیبا با ۱۴ معصوم دیدار کرده و حضرت زهرا (س) اجازه پرسیدن هر سوالی و شنیدن پاسخ آن را در مدت ۳ روز به ایشان می‌دهد و آقای صاحبی با بهوش آمدن از خانواده خود درخواست پرسیدن سوالات را داده تا واسطه شود و پاسخ آن را به آنها بدهد؛ نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حسین صاحبی بزاز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/675794" target="_blank">📅 17:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675793">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXqB5ddePxPzZ2_77bWU6PsTwRiYtDKV8znefE2Si4j68D4YPV8FDWvSjgII-WeZE2GyEnPYjQL5Dotk2WdEwUD4QoC4oW-d6oesXCtq9-4jergxfcjPDmkrIko71HSRTY8b0kU-uTr3EGBM7TLDDPqEb7nZt5PR6Rc0Bg7hUTtLyGIQ36x89WZjNGf956PUPD0u9vLhMfndfwg85elUmbAjpXb53UClvVesHqxZtmQ1wqgcGTa-lizu4TuYcu0fKWZDXUExbJvHem7deWmdaDDdokviG7IFnJN_0yLSI5cWCbDiNJluSm7Xi6PLZnYnduSAUUv90QSrmeMd0stjrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاف دمای ایران به ۴۰ درجه رسید!
🔸
هزارکانیان در استان کردستان با دمای ۸ درجه، خنک‌ترین نقطه کشور بود.
🔸
دهلران (ایلام)، آب‌پخش (بوشهر) و شوش (خوزستان) با ثبت دمای ۴۸ درجه سلسیوس، گرم‌ترین نقاط ایران اعلام شدند.
🔸
همچنین در۴۷ ایستگاه هواشناسی دمای بالاتر از ۴۵ درجه به ثبت رسید.
@amarfact</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/675793" target="_blank">📅 17:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675792">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حسینی: تلویزیون ۹۵ درصد نمایندگان مجلس را دعوت نمی‌کند
سید نجیب حسینی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
صداوسیما به عنوان رسانه ملی باید منعکس‌ کننده نظرات مدیران ارشد کشور به‌ویژه سران سه قوه باشد. سانسور صحبت‌های آنان نه به صلاح مملکت است و نه به صلاح رسانه ملی، این اقدام اعتماد مردم را کاهش می‌دهد.
🔹
در صورت عمدی بودن، سازمان باید عذرخواهی کند و اگر سهوی بوده جبران کند. با وجود ۲۹۰ نماینده مجلس تنها تعداد محدودی در رسانه ملی حضور دارند و ۹۵ درصد نمایندگان هیچگاه در این رسانه دیده نمی‌شوند که این یک ضعف آشکار است و باید رویکرد صداوسیما تغییر کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/675792" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675791">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa2999e06.mp4?token=pQpPjyRqJOTEtull92Ko_3LbdmDWmKlSvFTkWjdrjRTUjwed32mupqC8Lgg_tWsDzJVmY57XhRgSjnAGAD4xPFyTvEN289My9EnDQ7boKMQdZMdfVEFa95sJIfmcrq_sw1NtTb6xxgU6mxjBdp-CpM5ItJYmfkNjPDDhcnG3ARgwcVQH1syHRVNtlNQWvVVPaL7COSIGJvDPMg0LJD_R9uj2DBOYS1vefnvKyhIfCTYB4Z5hDfDnCL1MCSHmVo-0SxeZm4p-nArJ4eTD9yT112bRtRqB1NiL5KEiu-JtNMDzKnd_lr5RRTx4WgVTzO1nNOZynPzxlsbpCknhMdEfWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa2999e06.mp4?token=pQpPjyRqJOTEtull92Ko_3LbdmDWmKlSvFTkWjdrjRTUjwed32mupqC8Lgg_tWsDzJVmY57XhRgSjnAGAD4xPFyTvEN289My9EnDQ7boKMQdZMdfVEFa95sJIfmcrq_sw1NtTb6xxgU6mxjBdp-CpM5ItJYmfkNjPDDhcnG3ARgwcVQH1syHRVNtlNQWvVVPaL7COSIGJvDPMg0LJD_R9uj2DBOYS1vefnvKyhIfCTYB4Z5hDfDnCL1MCSHmVo-0SxeZm4p-nArJ4eTD9yT112bRtRqB1NiL5KEiu-JtNMDzKnd_lr5RRTx4WgVTzO1nNOZynPzxlsbpCknhMdEfWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه: در اسلام‌آباد طرف آمریکایی ۲ درخواست افراطی داشت و گفت اگر آن‌ها را نپذیرید مذاکرات شکست می‌خورد و ما برمی‌گردیم؛ ما درخواست‌ها را رد کردیم و گفتیم برگردید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/675791" target="_blank">📅 17:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675790">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
غافلگیری بزرگ بازار ارز در ایران؛ دلار از ارزهای دیگر عقب افتاد
🔹
با وجود اینکه دلار همچنان محبوب‌ترین ارز بازار است، اما در بازدهی سال جاری از چند رقیب عقب ماند.
🔹
دلار در تیرماه رتبه دهم بازدهی را به دست آورد در حالی که دینار عراق با ۲۱.۶ درصد، درهم امارات و لیر ترکیه با ۲۱ درصد عملکرد بهتری ثبت کردند.
🔹
در عملکرد چهار ماهه نیز روبل روسیه با ۳۲.۵ درصد، یوان چین با ۲۴.۵ درصد و درهم امارات با ۲۲.۸ درصد بازدهی بیشتری نسبت به دلار داشتند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/675790" target="_blank">📅 17:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675789">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه: در اسلام‌آباد طرف آمریکایی ۲ درخواست افراطی داشت و گفت اگر آن‌ها را نپذیرید مذاکرات شکست می‌خورد و ما برمی‌گردیم؛ ما درخواست‌ها را رد کردیم و گفتیم برگردید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/675789" target="_blank">📅 17:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675785">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گلیرم حسین</div>
  <div class="tg-doc-extra">حاج مهدی رسولی  قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/675785" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
بسته‌ی
#مداحی
#هیئت_قرار
ویژه
#اربعین
شماره ۱
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi
@gharar_madahi</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/675785" target="_blank">📅 17:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675784">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a679707f.mp4?token=lTB2Yk8DLYpwRtR2UZVT1IJ5AG0Xroh6Rq7L7CZ3986yBLjSC_KbhzrXv2o6qrsM5glDHZd5NMZQ2B_Rf5PQ_C0PLO4dDIiEjec7u298G_rgq1nkmrKgoQ2s6CP8jEE-b_aXelFpu2VVqGHUcZA6fibVDb1kyH7W86maEACiJe9NokKAlmz1gK_7bSYI_mMsZ8zhdKjwr8XEE-L-J4y5fSp5Fovvl4YrWDf9zcWTCKYJZXtG5hOXR2agunmN0nmZOqBFdSZPDQ9W6hn4f90tLQ0o7EG66YGe3xIO2J1Np8vqDVjE9-o7g90iem0VIKBiG9riAtlVqcMKFBFuAlTj8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a679707f.mp4?token=lTB2Yk8DLYpwRtR2UZVT1IJ5AG0Xroh6Rq7L7CZ3986yBLjSC_KbhzrXv2o6qrsM5glDHZd5NMZQ2B_Rf5PQ_C0PLO4dDIiEjec7u298G_rgq1nkmrKgoQ2s6CP8jEE-b_aXelFpu2VVqGHUcZA6fibVDb1kyH7W86maEACiJe9NokKAlmz1gK_7bSYI_mMsZ8zhdKjwr8XEE-L-J4y5fSp5Fovvl4YrWDf9zcWTCKYJZXtG5hOXR2agunmN0nmZOqBFdSZPDQ9W6hn4f90tLQ0o7EG66YGe3xIO2J1Np8vqDVjE9-o7g90iem0VIKBiG9riAtlVqcMKFBFuAlTj8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوگل رمز عبور را کنار می‌گذارد؛ ورود با یک ویدئوی سلفی
🔹
گوگل قابلیت جدید Selfie Video را معرفی کرده که به کاربران اجازه می‌دهد در صورت فراموشی رمز عبور یا از دست دادن گوشی، تنها با ثبت یک ویدیوی سلفی هویت خود را تأیید کرده و دوباره وارد حسابشان شوند.
🔹
گوگل می‌گوید این ویدیو فقط برای احراز هویت استفاده می‌شود، مگر اینکه کاربر اجازه دیگری صادر کند، همچنین برای مقابله با دیپ‌فیک و جعل هویت، چندین لایه امنیتی پیشرفته در این سیستم به کار گرفته شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/675784" target="_blank">📅 17:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675783">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c998f012.mp4?token=prto6ipaNjioLdCYzRZ1IyCkQkv449BjAf4kcpP_u_fV_EsX41F5S1Aeu2tJqwYJE4gSRlQrQYoiRviCH1ELQJhEp1rLlhtvLrJi9KH7_T8C4VGMFLtpNbCWOdNjyekY3wqDcD-EE8K1F8ryXvsV7w9FlsZJIFSYiQcwMtZDS9N-4DwQEtFSDlWe5F_so2GPGkGHBjWRX_Hq6KHhateBB1Jufk1Hx6YaFVTSbxm0XeDDI-ab4456vXM-g6dY1M2eaPgDwoMpWAWA9zIlbB7a4sbD5-bpt5zFaA7is8huu7jk4Wp0G6u-7cla-5id6pwZjb3_yQFRzsTaoOCzXu0V7iRmBa7d9mCZQR4qzSEPIruuYemndGQ0sPEKtmBXN2DO9ALaspS8xrTXcZQ0j7o38kRkjYFLpRuakjLHyOmR9dm2Wc9GNXtIXfIhbIq8888XoxsibGIIoFPgGAtrserHUzhGa9BkYNMrY6fxspzpJHeDUa1PI-tU09btdpYpIdlEPAs2Jn8GjYR4oDkeJq-hVFUna4H1jCWrFKUYMTkdBrQWXZYo2VAsBY8XTt-QdPtWjO6TKWXPhAIGXhd9hOhAKckOwzqs-XtQN5EJ1V2_PA37xjPCeroOEfigeIrE1jl-DJBEMZgeLOZtIdgjAi20255IhesxKLKJCnbCdpDe3I8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c998f012.mp4?token=prto6ipaNjioLdCYzRZ1IyCkQkv449BjAf4kcpP_u_fV_EsX41F5S1Aeu2tJqwYJE4gSRlQrQYoiRviCH1ELQJhEp1rLlhtvLrJi9KH7_T8C4VGMFLtpNbCWOdNjyekY3wqDcD-EE8K1F8ryXvsV7w9FlsZJIFSYiQcwMtZDS9N-4DwQEtFSDlWe5F_so2GPGkGHBjWRX_Hq6KHhateBB1Jufk1Hx6YaFVTSbxm0XeDDI-ab4456vXM-g6dY1M2eaPgDwoMpWAWA9zIlbB7a4sbD5-bpt5zFaA7is8huu7jk4Wp0G6u-7cla-5id6pwZjb3_yQFRzsTaoOCzXu0V7iRmBa7d9mCZQR4qzSEPIruuYemndGQ0sPEKtmBXN2DO9ALaspS8xrTXcZQ0j7o38kRkjYFLpRuakjLHyOmR9dm2Wc9GNXtIXfIhbIq8888XoxsibGIIoFPgGAtrserHUzhGa9BkYNMrY6fxspzpJHeDUa1PI-tU09btdpYpIdlEPAs2Jn8GjYR4oDkeJq-hVFUna4H1jCWrFKUYMTkdBrQWXZYo2VAsBY8XTt-QdPtWjO6TKWXPhAIGXhd9hOhAKckOwzqs-XtQN5EJ1V2_PA37xjPCeroOEfigeIrE1jl-DJBEMZgeLOZtIdgjAi20255IhesxKLKJCnbCdpDe3I8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعبیر جالب دیپلمات ارشد ژاپنی در مورد ایران و امریکا...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/675783" target="_blank">📅 17:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675782">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapp | اسنپ</strong></div>
<div class="tg-text">📊
مسیر همراهی؛
روایت گروه اسنپ در ۱۴۰۴
💚
🗓
سالی که با همراهی
بیش از ۸٬۵۰۰ همکار
، فعالیت میلیون‌ها کاربر و ثبت رکوردهای تازه در بخش‌های مختلف اسنپ سپری شد؛ از توسعه‌ی سفرهای اشتراکی تا بیشتر از ۱.۵ میلیارد سفر شهری و از رشد بی‌سابقه‌ی اشتراک اسنپ‌پرو تا تلاش شبانه‌روزی تیم پشتیبانی.
📌
توی این ویدیو، مروری داریم بر
مهم‌ترین آمارها، دستاوردها و اتفاق‌های اسنپ در ۱۴۰۴.
🤩
ویدیو رو تماشا کن و مثل همیشه در این مسیر همراه ما باش.
🔗
مطالعه کامل گزارش سال ۱۴۰۴ اسنپ
@Snappofficial
✅</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/675782" target="_blank">📅 17:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675781">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افشاگری سخنگوی کمیسیون انرژی مجلس: برخی از خودروهای دولتی درگیر قاچاق سوخت هستند/ گاهی با یک شبکه سازمان‌یافته در موضوع قاچاق سوخت مواجه هستیم
رضا سپهوند، سخنگوی کمیسیون انرژی مجلس، در
#گفتگو
با خبرفوری:
🔹
عامل اصلی قاچاق سوخت قیمت هست. مثلا در پاکستان که یکی از مقاصد قاچاق هست قیمت بنزین و گازوئیل ۳۰۰ هزار تومان است.
🔹
حجم بسیار زیاد و معناداری از سوخت کشور قاچاق می‌شود. تغییرات قیمتی نمی‌تواند مشکل را حل کند چرا که بخش اعظم ناترازی مربوط به قاچاق سوخت است.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/675781" target="_blank">📅 16:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675780">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سفیر ایران در روسیه: کشتی آنا کاملاً غیرنظامی بود و برخلاف ادعاها، هیچ محموله نظامی را حمل نمی‌کرد
🔹
فردا سه شنبه حراج جدید شمش طلا برگزار می‌شود
🔹
۴ نفر از اعضای گروهک تروریستی پژاک در نوار مرزی بانه به هلاکت رسیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/675780" target="_blank">📅 16:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675779">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
مقدم‌فر: پاسخ ایران فقط به پایگاه‌های دشمن محدود نمی‌شود
مشاور رسانه‌ای فرمانده سپاه با اشاره به راهبردهای مقابله با آمریکا:
🔹
هدف قرار دادن پایگاه‌های نظامی دشمن یکی از ابزارهای ایران است، اما این تقابل به آن محدود نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/675779" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675778">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHwp3PVEeIpDUmxZsO3hpqcJvYhSP1I5-cwXjSEKCzK4jqYezBpSN-HLSdRFULcz4NP5lOke1CzDFRWV23j-5mBlAUSc6B4uxMs-4Cj4e030Z1Yz6K8Xp9HFswQukBFc4iwOJM3JD1bM-zG7IqFaffRbjSYgGNrXx2mGnPcUNjrvAAuKYBhsMf4Tigq8Gft1GFfm19E-N-Yv028f8BaxqA4T7bjQtS3bkj3pw8k02zxUU2lqT-esIZ5kRBZPCNO5M64kNWQpJm5LNlv_0qsS4n5VyWHTNpNbNTU_JaRwqkcb8cufcl0BeAQHmfbIfszwXxReeT5c31dd8F9myjxoHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
رشد ۵برابری پرداخت تسهیلات مسکن‌روستایی توسط بانک کشاورزی
🔻
پرداخت تسهیلات بهسازی و نوسازی مسکن روستایی توسط بانک کشاورزی در چهار ماهه نخست سال ۱۴۰۵ از نظر مبلغ ۵ برابر و از نظر تعداد ۴ برابر افزایش داشته است.
🔻
این بانک از ابتدای سال جاری تا پایان تیرماه، ۱۱۹۴ فقره تسهیلات بهسازی و نوسازی مسکن روستایی به مبلغ ۵۲۴۵ میلیارد ریال پرداخت کرده است؛ اقدامی که در راستای حمایت از تأمین مسکن ایمن و استاندارد و ارتقای کیفیت زندگی روستاییان انجام شده است.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/675778" target="_blank">📅 16:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675777">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
اراجیف جان کندی علیه ایران: باید آنها را از گرسنگی بکشیم!
سناتور جان کندی در برنامه «رو در رو با ملت» به مارگارت برنان در اظهارات متوهمانه گفت:
🔹
فکر می‌کنم باید محاصره ایران را ادامه دهیم و آنها را از گرسنگی بکشیم. باید کوه پیکاکس را بمباران کنیم و سعی کنیم به آنچه در زیر آن است برسیم.
🔹
اگر می‌توانیم درد افزایش قیمت انرژی را تحمل کنیم، باید به مسیر خود ادامه دهیم. حداقل برای چند ماه دیگر.
من همچنین فکر نمی‌کنم که نیازی به اعزام نیرو داشته باشیم. این نظر من است، به هر قیمتی. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/675777" target="_blank">📅 16:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675776">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKepfszDot1oy2ner8mAaXZpYPhFMIHeWVdzLhsVTh8kmAs1QMfZ_Nhx9woeWuLadNnt1zmj2VgKeT0OxnSrhq4mTCu3XZvyVU7pOwfWa3MdtNLM57TWFrrXMB4ErARbKqVeNxb2t0b-e2Df4chGtyu1mw6CvlpILlq7q5MJnkWA4yftScZDH5eo4huSgbcz0S5iBdLFDoY96FKOG5B7pxmF_WLMbgl5paYTvAQA9i9AfC6-fgbxgNJU7Uu6yXRu0OH55D__cjShtXZMhteX3Pci2YkeSObz-yGJhjpXbj0Rawu54TEgWLgsdgrZe0eQO5Rybgja3IEy0-JCJxIa7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قبل از روشن کردن کولر، این ۴ نکته را بدانید
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/675776" target="_blank">📅 16:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675775">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWdzdxHtULay-CvaXn3MxJz1wSF_H1cl8UBTrHaj7B81lPbftlgGCvhcOULP7X_8pe9eChqoaC160wNDSBB0KrBGu4ojgtvf71-2U8j3FpfcBskECOO_7g8DJxPq_J4K8rCNHammu-1SciYbkAZvqP6arp6cnMkppjNlfE95h-QNLEq5PBx21YGKcgj4QzGiZNwCDbvAhEYLLqDHfCXwYVrqNai5QFJGch2jBzutzpLDJB8XRcN049uJdI6u5vTWmYzaDrclZeaA5dFVMJXPeT-9jkTPfa1o6VLEGJrMaVJxWLN-q6tBAuen-0tN3F1rYIKIJf7-2lqcnV-cHrsumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«رویای نیمه‌شب» از امشب روی آنتن شبکه سه می‌رود
🔹
سریال «رویای نیمه‌شب» به کارگردانی حسن آخوندپور و تهیه‌کنندگی سعید سعدی، از امشب ۵ مردادماه ساعت ۲۰:۳۰ روی آنتن شبکه سه سیما می‌رود.
🔹
این سریال اقتباسی آزاد از رمان پرفروش «رویای نیمه‌شب» نوشته مظفر سالاری است و داستان عشق فتاح، جوانی سنی‌مذهب، و تلما، دختری شیعه، را در شهر حله روایت می‌کند.
🔹
بهاره افشاری، سعید شریف، روزبه حصاری، محسن قصابیان، حسن معجونی، نادر سلیمانی، آیدا ماهیانی، سوگل طهماسبی، نسیم ادبی، مه‌لقا باقری، پیام احمدی‌نیا، کاظم هژیرآزاد، حبیب دهقان‌نسب، مرتضی ضرابی، اشکان دلاوری، حمیدرضا محمدی، سوزانا آلویز، هادی طرار، عباس شجاع و مژگان اخلاقی به ایفای نقش پرداخته‌اند.
🔹
سریال «رویای نیمه‌شب» به نویسندگی سیدحسین امیرجهانی، محصول سازمان هنری رسانه‌ای اوج است.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/675775" target="_blank">📅 16:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675774">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سناریوهای جنگ در دیدار قریب‌الوقوع ترامپ و نتانیاهو
🔹
دیدار قریب‌الوقوع نتانیاهو و ترامپ، در شرایط بی‌سابقه‌ای از تغییر معادلات منطقه‌ای رقم می‌خورد.
🔹
حضور نظامی اسرائیل در لبنان، انسداد باب‌المندب و تشدید محاصره‌های دریایی، همگی نشان از عزم واشنگتن و تل‌آویو برای تدوین طرحی نوین در تقابل با ایران دارد.
🔹
نکته هشداردهنده، سفر هفته‌گذشته رئیس جدید موساد به واشنگتن و دیدار با رئیس سیا است. این نشست که بنا به نوشته اکسیوس، با محوریت «جنگ با ایران» برگزار شده، بیانگر گذر از راهبردهای صرفاً نظامی است.
🔹
تجربه دو جنگ اخیر نشان داد که تهاجم مستقیم، با سد همبستگی ملی و پدافند مقاومت، با ناکامی مواجه شده است. ازاین‌رو، گمانه‌ها حاکی از تغییر تاکتیک به سمت «جنگ ترکیبی» است.
🔹
اظهارات صریح اسموتریچ، وزیر دارایی اسرائیل، مبنی بر هدف قرار دادن ایران تا «مرز فروپاشی» و تأکید بر کارآمدی اهرم‌های اقتصادی، زنگ خطری برای تشدید پروژه‌ای سه‌وجهی است؛ فعال‌سازی گسل‌های اجتماعی، تشدید فشارهای معیشتی و بی‌ثبات‌سازی مرزها.
🔹
با وجود این تهدیدات، معمای راهبردی دشمن همچنان پابرجاست. تجربه دفاع مقدس و جنگ‌های اخیر ثابت کرده که مهم‌ترین مانع در برابر این سناریوها، انسجام داخلی و تاب‌آوری اقتصادی است.
🔹
خنثی‌سازی طراحی‌های مشترک موساد و سیا، امروز بیش از هر زمان دیگری در گرو تقویت همبستگی ملی و حمایت از اقشار آسیب‌پذیر است؛ عاملی که بارها نقشه‌های دشمن را در رسیدن به اهداف راهبردی‌اش نقش بر آب کرده است.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/675774" target="_blank">📅 16:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675773">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb30eccc7e.mp4?token=VRaGnEvhQcLGzXdgoreg8eG1aSHXFtDKCryBd8yzqNF-pAWj-xo_bOf8NHNrgHFR86jh6_igAZyt--pmeFWWgQOc2UW6sUbG6F87lbuniF6fjH15rI7thaoBvLU94rz_rHHWCUCvUjXGNPMEnMpGv_oKinkh_ixZ-DgXtml8hT6WCHO3A59hal-UMlp8qBLzN4aPZ7-NhWVGsENOkwv04OYg9eMehdf0dHUebN0ThyrwHdxgkB7lcb_-J3e_te_Wg6nov9uA9jqMZAWAkDoSik20MUefsTleQ0U4Kq0sca95YToBvdKHbd7CQ4tXvNtt3KqtSRHDgj12kXT7j3_XOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb30eccc7e.mp4?token=VRaGnEvhQcLGzXdgoreg8eG1aSHXFtDKCryBd8yzqNF-pAWj-xo_bOf8NHNrgHFR86jh6_igAZyt--pmeFWWgQOc2UW6sUbG6F87lbuniF6fjH15rI7thaoBvLU94rz_rHHWCUCvUjXGNPMEnMpGv_oKinkh_ixZ-DgXtml8hT6WCHO3A59hal-UMlp8qBLzN4aPZ7-NhWVGsENOkwv04OYg9eMehdf0dHUebN0ThyrwHdxgkB7lcb_-J3e_te_Wg6nov9uA9jqMZAWAkDoSik20MUefsTleQ0U4Kq0sca95YToBvdKHbd7CQ4tXvNtt3KqtSRHDgj12kXT7j3_XOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های سیدمجید بنی‌فاطمه در حاشیۀ محرم‌شهر دربارۀ عشق اکبر عبدی به امام حسین(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/675773" target="_blank">📅 16:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675772">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
منابع عربی از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور خبر می‌دهند  خبرگزاری رسمی عربستان:
🔹
چند پهپاد از سمت عراق وارد آسمان کشور شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/675772" target="_blank">📅 16:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675771">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ارتش کویت فراخوان جذب نیرو داد
🔹
ایندیپندنت مدعی شد این اقدام پس از حملات ایران انجام شده و می‌تواند به دلیل کمبود نیرو یا جبران خسارت‌ها باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/675771" target="_blank">📅 16:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675770">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm25u40ROXBnEWXdBsJsNRL_0KjKnqzUbENBjg1aUyhv7KibWb7MgVFjgbcGgRXDWqfmkAn5Z4EHZ2sEQ8JrNHzpvZoAtRacyPJWox8cC3sBP4D_QIBLXE9roBuFC7TwHKYEdoi-xiyiF2FB6ZiyeE80kY5hWW_aC0jX_euBh--FPO6uXVYp2g_tCD8pkFuQ0E8PACfPhfN4tWweK4YuFyN5fCB1JrlU343dAorU-5sRC2yrAhXslakIkiGXnz5U5mZjdzO7KEoFAy3MzxYkAa3gyme9K7PR028Yx7bFhAd4Qinaq0ZETi_mMmvjEDPxPEa6svYaRvt9EjIutozWFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/675770" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675769">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
چاپلوسی وزیر دفاع انگلیس برای ترامپ: از حمله به ایران حمایت نمی‌کنیم، اما اروپا مدیون بیدارباش ترامپ است!
🔹
وزیر دفاع انگلیس با چاپلوسی نسبت به ترامپ گفت اروپا به خاطر بیدار شدن از خواب خودراضی به او مدیون خواهد شد.
🔹
لندن از حمله نظامی آمریکا به ایران حمایت نمی‌کند، اما با لحنی چاپلوسانه افزود که همیشه حرف ترامپ را دوست ندارند، ولی او اروپا را مجبور کرد مستقل‌تر عمل کند.
🔹
استریتینگ در عین حال بر همکاری با آمریکا برای مقابله با برنامه هسته‌ای ایران و تأمین امنیت تنگه هرمز تأکید کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/675769" target="_blank">📅 16:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675765">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slTRQykG60HLEsre-JhssJ4Qqc1DEv_Kabud3UjNBR9nkt3V8n7sBNywTeDl34r99uJpoWD_4U8SYDNrICCue76GlVsVR4wb0tnBwAOhVjjC6KNN3CHEk81iWZSX70rc0iNoHvEb0ZOgh1gDCj0_ude3puqEhd0YODSgMOh79hrCIaB4lEFR3gTD9_LlPtru3fA5ikOkM8hWBwk6HTad0oyPxHlCuHdp2eyCsVqNPT4f2ZvoLZd2Hy4ESKkX8Z5QhXn7TZEDn8F_FJWJD5vkNTKWe9cMHoZFanUj50JmIFsGRusawj1PdhHRE9OzQZ3gtYW3EueXQpe6dZzv-NXT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOhxnDAIJ_EMBz_wx--sCaJjnNWE3Wrs08qJREdnwSMn6z9Ql6kKrGqPs4CPOGXIKsDLqlj-Gp6e3kg75s5pm4RDpaUb6lbxkF0FlSqVA7vG_K8YG_FU3oQWJdBHJOZfIorCRcOAQ0pTLCp7CenKMptNyWFCCjC3HyF9XCGAaLxP4tT6uH0_epPgpqugAvhq0tk3g2UYKf1kFjx-fN0hRQ1_JJlPjP1dqsEitC4lO25kvW21jGGj5yCt0B65AzsqMwUXwsPpTqMRYBMkaKtDVvPnH5o5mEbGfjsWwA3ilpXntNFnZOOsWpEe1KTcUTv677UPakPYEwTbS4Ag5QzTmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IRdvWk3_pZinzYPlvcf7vWkSVl5nShW9NOjLRv6VicbT-WVVFp9rBUOonyVQSgZDRGB_YI8sQctWnqfA4nTUAAg1NxH3dSDFhPBQWqZWVV0x3vudqqhPMba65fYhGapyaUutvlV4e6r2poQOam27XKyOucolQ-_Hyl7LZ2Ur2uF4-cPHJF656EEMMjkgj3Nq_tPk84CpRK8Te_DTEvM_8sJRm_Z6ktfjg3TFOR1v5p6bF_GQf2iI0tbjG2LosON0-1ISWOmYlotJ6rEew_jQ52JlwtjlngzqKSPLZpT3x22c5m-MWcS0sIFbl0rSFae8FZ5SSEFhxDDA2RndkjIdAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dlcL7r1h-TMTemrfYJseLA-a6znWypTIxdsA7GeA1Uqu1kiU-0uKop2XmWyQvnxtL9rcR6mlxM5gvxWWikiKjomZku13Tixk-tCS59GuOaIUSsq3vyiEz_-MqwgVLdPGJga72pwWHn-roChnLOwFsh1BBsTUDfv2vTy_oEjwalA7JOxJgwZk5C1-TyZbo9Ph8KNP0jQFF8JbveGXkP-UAFXRI0mYPXwx55JiPo6Len_jq44llbC4UOWs-_R712cxnRvOTnsrCS3UhPpA3NxvjfRyDbzkSwt7ydViWxUwUuTs0vzA29kukONYA00OIdEDEeKcurqlTosYktwXWz8P0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
با چند اقدام ساده در مصرف برق، می‌توان به پایداری شبکه و تأمین روشنایی پایدار کشور کمک کرد.
🔸
استفاده از لامپ‌های LED و کم‌مصرف
🔸
خاموش کردن کامل وسایل برقی پس از استفاده
🔸
خاموش کردن چراغ اتاق‌های خالی
🔸
استفاده از نور طبیعی در طول روز
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/675765" target="_blank">📅 16:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675764">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFCgs7g1_I0-95vBOuUFRPcVUzFTlvLywrYaxxRU833-tD71hBawJOEcLbZWwUHlLvHbKeOYCeyCDySmCQrosugEEZWxpv01SUGGvkkdGtNhdnI6LptbJPxFuQYpKRgd4G_hDlM1d4geNSbhomwjBLtPkGVbgtEczHHPhO_s_L7pxl2bqO952HwcTtXAi2kt24PBNJv_3v44YERoHFcLU-g6tU3srQAWFIR4OIbtUlkuPcIvOvFuHVsH4t2BklPSq3Q1RxWjh_akX0S1CKxgFLjouBsM8BYl6EzrDLlP_X4DRxc0EMOTKBgArpfQpUuED1PW90G7LH3AnCKThL6Bhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای گام‌به‌گام نظافت خانه برای همه‌ سطوح و وسایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/675764" target="_blank">📅 16:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675763">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STh3RM0uDulNqKnRGX8L3wvxiiVwBzuJqRQMKIyb9dYSFIpqreOJx6n3qOQ23xCEaQza0x0DTvAWIv1mBKwwBgER29E4m7bCTIkTsGHXbpqWvBpLhOUtuTK9AoryzG43x49NgD2lQj4mqYFzZTrAZ4Hk3jCdvlC7KA1E038eo568kup-fw3ZVYAvkxXIgSnlEvew2hpZOouXTWvhVFwXITPYc54FHtpLMC6UIGGTe1EdEUhbv6tf0_75jv47PVet6Xtj1kw9qEkVbj23NXHgeI67hExSUPK1m3PFuC1zUymvaTLx7PJE9NlR1E0i0DRxFQqylpzYMO_jQJxHj6psxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۷۳ درصدی مصوبات اعتباری و پرداخت ۱۰۸ همت تسهیلات در کارنامه ۱۴ ماهه بانک صنعت و معدن
بررسی عملکرد ۱۴ ماهه بانک صنعت و معدن (منتهی به اردیبهشت ۱۴۰۵) از جهش چشمگیر در تمام شاخص‌های اعتباری خبر می‌دهد:
🔹
رشد ۷۳٪ تصویب طرح‌ها
🔹
رشد ۴۷٪ انعقاد قراردادها
🔹
رشد ۴۰٪ پرداخت تسهیلات
🔹
پرداخت ۱۰۸ همت تسهیلات
🔹
کوتاه‌شدن فاصله زمانی از «تصمیم تا پرداخت»، یعنی تبدیل سریع‌تر مصوبات به سرمایه در گردشِ کارخانه‌ها و رونق واقعی صنعت کشور.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/675763" target="_blank">📅 16:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675762">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZhLN6dN3LjK6sai3bTblM2jMzEEhWkILej86mGE3cpC_aMYV0GH_-vQORHS_hH40oChdgs9mxBjpq0Rls9rcSiXdvN-0YKymjrI812JEb9snjfAvmK3M-9aUpqaKLI8NxCmhVc-TJClgwRIomgo-kRPWOs0gbjcE0ZidHkD7ffUZtAePrCJWzx194gfVYP2ehksISDu9fP_pFXPv01mGgMPVY1gdSX4MncacXomJgw43j5OavI5zANxy2U3aQ0mZbBM9IhTzRCv9J6Hi5HGNKyU_z6G1IahpXDrUEe_k9iOq_NQGJE-DmatzDRY-jTEY0uTXTgKy-Js8gmY2FI9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نظرسنجی شوک‌آور: ۸۰ درصد آمریکایی‌ها جنگ با ایران را سخت‌تر از چیزی که ترامپ گفت می‌دانند
هیل، پایگاه خبری کنگره آمریکا:
🔹
از هر ۱۰ آمریکایی، ۸ نفر می‌گویند جنگ با ایران سخت‌تر از آن چیزی بوده که دولت ترامپ انتظار داشت. در مورد آینده جنگ، ۳۷ درصد از پاسخ‌دهندگان به نظرسنجی YouGov، گفتند که این جنگ ماه‌ها ادامه خواهد داشت.
🔹
۲۱ درصد از پاسخ‌دهندگان گفتند که این جنگ سال‌ها ادامه خواهد داشت، در حالی که ۹ درصد گفتند که برای روزها یا هفته‌ها ادامه خواهد داشت./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/675762" target="_blank">📅 16:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675761">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b2948d81f.mp4?token=rhjfpdgFB-57qxZomctfEMhllxR06X38X5ghK7YpqHUicdESm1lXGKaSAyYv8uPTjqd-VxJZ6h29QKhjH4g-gNXnrPViM8CK-yx2nxneg8hMmcWKyhDYgOhBncSY8YvkJFIkEygok2IYYrHzOT9Aa9T2eCJ0t-C_6E_BUkH2E5NgewTf7aPYVB0YQ61dHE3ESQgKFr8iuu2xzRkWmCmPKgnb5tLyVud6VYr44Bqt4ytcpiZCa6roLRtvtmkM7PGamGTrksgBhvtDlKCo7S3ehZcNs29AMAjPvd9ylUSuINk4GcMTYDdGhlQOdS9P7sOwoF0oGo4gmig3lTGOOKfBaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b2948d81f.mp4?token=rhjfpdgFB-57qxZomctfEMhllxR06X38X5ghK7YpqHUicdESm1lXGKaSAyYv8uPTjqd-VxJZ6h29QKhjH4g-gNXnrPViM8CK-yx2nxneg8hMmcWKyhDYgOhBncSY8YvkJFIkEygok2IYYrHzOT9Aa9T2eCJ0t-C_6E_BUkH2E5NgewTf7aPYVB0YQ61dHE3ESQgKFr8iuu2xzRkWmCmPKgnb5tLyVud6VYr44Bqt4ytcpiZCa6roLRtvtmkM7PGamGTrksgBhvtDlKCo7S3ehZcNs29AMAjPvd9ylUSuINk4GcMTYDdGhlQOdS9P7sOwoF0oGo4gmig3lTGOOKfBaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درآمد نفتی ایران ۱.۵ برابر رشد کرد
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/675761" target="_blank">📅 15:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675760">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248f0fb4e3.mp4?token=j-7PbX_rBr2Sr7WUcPHamZE4H6i4L-XFu5SNqD1_fg5Q86P8zXG6yVfECugCNiZmpm5vpDOiv_1vEqfs6gOenJHkenSIQK891g4R_qUkHdPKSv_w_c60-LYImqBATD_M1WLtDWBXqLuH_9G8DB2DXUKSgomAfnPvu1gORa6mltSBuKC7_EXmO4yMyPyG6ooDQJO35UcxdKMxy8S81DvnLlN-Lo7l9DJBp7FJTjAQgWanPfs_SFSuounRXOyrnE1jDeHhGrqeJ841qaC8FOK-E8l1ne4DYjidIb-MsG5MZc6GavIc72que2Ay92Oy7QQ1GIL0EjUIbRxuqT_I6PVfmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248f0fb4e3.mp4?token=j-7PbX_rBr2Sr7WUcPHamZE4H6i4L-XFu5SNqD1_fg5Q86P8zXG6yVfECugCNiZmpm5vpDOiv_1vEqfs6gOenJHkenSIQK891g4R_qUkHdPKSv_w_c60-LYImqBATD_M1WLtDWBXqLuH_9G8DB2DXUKSgomAfnPvu1gORa6mltSBuKC7_EXmO4yMyPyG6ooDQJO35UcxdKMxy8S81DvnLlN-Lo7l9DJBp7FJTjAQgWanPfs_SFSuounRXOyrnE1jDeHhGrqeJ841qaC8FOK-E8l1ne4DYjidIb-MsG5MZc6GavIc72que2Ay92Oy7QQ1GIL0EjUIbRxuqT_I6PVfmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیما مرادی؛ ملوان ایرانی که در حمله اوکراین به کشتی آنا به شهادت رسید / فارس پلاس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/675760" target="_blank">📅 15:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675759">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره تخصصی اتاق تهران برای توسعه تجارت در بازارهای خلیج فارس
🔺
اتاق بازرگانی تهران با ارائه مشاوره تخصصی، شرکت‌ها را برای ورود و توسعه تجارت در بازارهای کشورهای حوزه همکاری خلیج فارس همراهی کرده و مسیر صادرات را کم‌ریسک‌تر و هدفمندتر می‌کند.
👈🏻
دریافت مشاوره:
۸۸۷۲۵۲۶۹
(۰۲۱) |
۰۹۱۰۲۶۶۹۷۱۴
|
service.tccim.ir/intl</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/675759" target="_blank">📅 15:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675758">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
منابع عربی از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور خبر می‌دهند
خبرگزاری رسمی عربستان:
🔹
چند پهپاد از سمت عراق وارد آسمان کشور شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/675758" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675757">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPHtwU2ki-SVYC0kmc0cy_b3Cyzu3fxR6fRtWFUqJKoICdLLQOf86DMcRVvBey9KopAfEoo7Mvoo6i7mnETxtjf1_JEQJB0eVS-ihtslT1FpALhBIsOG8Wqr-xJNd1Au28FveGdKiWy16AMw5NSe2-RRGG3CLfVzz9wGS_HKxR0HmvsXS2MxSgfHq0eLwY3bnoG5Qw2ntNcfCGpU5ugbzRSUjutG4CQQ_y0v7tBzmi84054qmStzhBNuFBCDdipijDx3vQKn3CQeoZLloOIFUKhSxHFQkgXaRdOldrSVekoBqdrkS5Nn2MqoE9tX_l0hDHaEgK5MnyVVcl53f23xOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقف حملات آمریکا نشانه چیست؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/675757" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675756">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
حباب سکه آب رفت
🔹
حباب بازار سکه به پایین‌ترین سطوح سال‌های اخیر رسیده است. در حالی که حباب سکه تمام در گذشته تا ۳۰ درصد و برخی قطعات کوچک‌تر حتی تا ۵۰ درصد افزایش یافته بود، اکنون حباب سکه امامی ۲.۰۳ درصد و سکه بهار آزادی تنها ۰.۰۸ درصد است.
🔹
همچنین حباب نیم‌سکه ۴.۷۹ درصد، ربع‌سکه ۱۶.۰۵ درصد، سکه گرمی ۲۳.۲۱ درصد و حباب طلای آب‌شده منفی ۰.۳۲ درصد ثبت شده است. آماری که از کاهش چشمگیر حباب در بازار طلا حکایت دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/675756" target="_blank">📅 15:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675751">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGyAqHc2iSagp2fncw5WitqOBWzhg8nhXAqVppeIdfrh5OAmUFUwLnDKWj8SWagogzOEtz7AfIg9-zIBPWRVhFaa_xrwKGGT1UIUuMtaVnNWKI-DGuTXZ569xvp17ss2Ad2byvhfsoKbSHimuBo-3TjAvv4xvihmUTHgzLin5-7S6DCqXSNeoD1ROyd3PQmpZBx4HfG6SemRP3z3N2LkElyfzGQtuk-aEJJq6mXiUu8123UYtyydvs4-UudlgROgUT-pxu_iumuiO-vSLhuuCfjM8ZIKLWyPe8DzvjReIPJBpSsovwIJB07qVydrgMAl5mMY02vlot2coJvmx-J9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMltpfAazroHUyscHk8Eth34X4fjpKvPzc_LG-xt-nmbZ17oR38pFhh3xmulW7KZkzYzI8j-EO784l98WTzgai7Xf7uvn5b0VN0dWIpcmwszltvu1lFRLHRUWv-NTJfXwrq4Uv-bxJaHRNKEbSgNVrk8C1iyM-8y1ER7sNWGM-fIttkHIT90H1V_JdQt_V4G6_OdN_i_f6PsgZY92ghQwmukODvKTxfrVJP9-zS-RbH0iZ6TPi2YfgHJDUICsds3y1dH4M6PyXJykJOsScjyKiIczZeK6K5OeoRcGicylWEQ9hOFX_-c9MUKcaspZpBwU2ldJVk40i7m6UOYouUKig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/duQbWk3DHyUWNZK7nR-Tidxj8m1Az-D8UcgqPNrDwqybq7UO4LJqU-QEtihCgw64_wS-bRoZiomsmL1PxZMUEPkyxorxawXZnHIyVJ3-CFJq2tVrNXGsU2PyimLafKxBrxkvK8R3rK_FU6RV0Ct6VLCHkhNo6oS38ze9KUSbfIz-tk5pBuBk-OxS2biD25r_DmnBkSKBmcrAiz8GTsvk0uqftH0vpLwIl60F_njdTelNGvIY59HdMVKOsTjBfIwK2Hil6esSeUewSXdNJsKwGWFqybQLCgrxInoalk1wYjAcYgx7lIXEaEcrxG_mdfGVoWxskUgv229iVhwrnYKIKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ad25p8V8hFCqs1sPYXcB5jSX4OoHpoZ_JvHrriNH5mO2ym7ePTe_qeXfypADPrkEcwV6xWw-wfLkNYKqHhKrFDR6cT6B5JTD7YxFIZ8zBJEcrNW6hHtly_SBXKkmcPzRushibs4AL-3P5sHlaszk7u0Q78aVp3OO68s0CXfEVzF9kfYCP-yAKgLxFosmfDvSr7TXLyQ_CFmmggYRcJJR2OkoQbl9gyNuH-wGpHi75Q85oWpV4fcuOeocpOE6zvU5wqvsi5IEu1VCg7567Sv90kug-GAYO8BSRW_MSqkIw86grn4rrv2wHaf2fZGSECBNMNJsBS2jwEPKPjkcSEPqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIBDwuWAjfk7ya_EzWSYPs5qyFQVh4MvC0cf9MZKgViPT-L9GExJkf7wUpebs9ueGrMXyCzh6cngsg40BEQI_1A79z9NRsRjmRe_khIqhf2d-yAo8l69x0HoyBdm4o4ECDheTK21aEJTsTvzvZdM2pzu2dZSZxFNoGgb3Tu3Q5Rv9VbXwkgLQi93mE01nhkJLghsXUPeZVwaf2nzTH6On7nJOalwwQX7QhdYT9JqonzeBLfVTAq_etQ2nEtOlanLrWzUkDTND8mOKptAIKxbpg47h-qHECiGsIz6tWOYjhwxFRh-EAyToaJ46SzesmmByXZA5Lb7lFRu3TUkbQeudg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قبل از خرید عینک این ۵ مورد رو حتما چک کن
🕶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/675751" target="_blank">📅 15:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675749">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBNrJ0fpt7mg73iYwftxFpl_g1_YAkQsmGeeCP_IdYQ88YQYSxjc5fmg624k5r_mA4j5N6zPxiF5PLTUUIk_Sip2No_Jz7tbASQ3K_Y3uoR0gIDPT6eVJuycXrmXb-S_rs38DIiyzsKmY2w5wwELyZgDZ08L7LgQbybkdRsJkWZ25gAYOuHUIjXhB0FDRYKkz8t5-rnPahIbFW5Uz1eJx9YLwzV07A05ZsG5ZZuBHUpH4kjE2WE7tm4tzTpJ_lsAn6mT07VuRu3Djm36DHlVZHAcwfDzvaEN5lVpUnC0fOOt5q5qAawV_q_1tQfe9tuBdVKKswh_vsdjDSIDWKfvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: رئیس‌جمهوری که فکر می‌کرد چکش بی‌نهایت دارد، حالا به دنبال راه خروج می‌گردد
نیویورک‌تایمز:
🔹
رئیس‌جمهوری که ۵ ماه پیش با وعده «پایان سریع برنامه هسته‌ای» و «سرنگونی دولت ایران» وارد جنگ شد، حالا در دامی گرفتار شده که خودش ساخت.
🔹
ترامپ که زمانی به «مدل ونزوئلا» برای ایران فکر می‌کرد، امروز نه تنها به اهدافش نرسیده، بلکه با واقعیت‌هایی تلخ روبرو شده است.
🔹
دستیاران ترامپ می‌گویند ناامیدی عمیق، رئیس‌جمهور را غیرقابل‌پیش‌بینی‌تر کرده است.
🔹
به نظر می‌رسد ترامپ در دام جنگ ایران گرفتار شده است، حتی با اینکه بزرگترین چکش جهان را در دست دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/675749" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675748">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1e5b26943.mp4?token=oSeEgrxO5kU3TiT8BAkQRSeSuN_zg6JGcQXiXxTf-hy1TUa8oFxQb7tBJQJJdvOMug6e-i4dxP_m3Em59a7x30feMZWGZRGNKu3wtgAUa6meJw-LW0F_udFNBN4kiDbM7qVDRF4XToZ_lvIh306PBW-qbTx-5NfonkmbbWz8jJRxTpcuYyl-qswemBdgXxsk8gbc2t_nhKbKSwpDOnKbLwjuKKRTENlI4llNcVQVty44Voz-gomGEh-rNXpvuEd3V7zg31zECJ98ft0dz7-U6A0WHhhmnEeRzDhuYw270dh3EWvMkco-aaqnmI0ywrhzNZt_DsdgquxKpzdVVu5fNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1e5b26943.mp4?token=oSeEgrxO5kU3TiT8BAkQRSeSuN_zg6JGcQXiXxTf-hy1TUa8oFxQb7tBJQJJdvOMug6e-i4dxP_m3Em59a7x30feMZWGZRGNKu3wtgAUa6meJw-LW0F_udFNBN4kiDbM7qVDRF4XToZ_lvIh306PBW-qbTx-5NfonkmbbWz8jJRxTpcuYyl-qswemBdgXxsk8gbc2t_nhKbKSwpDOnKbLwjuKKRTENlI4llNcVQVty44Voz-gomGEh-rNXpvuEd3V7zg31zECJ98ft0dz7-U6A0WHhhmnEeRzDhuYw270dh3EWvMkco-aaqnmI0ywrhzNZt_DsdgquxKpzdVVu5fNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از آخرین وضعیت تنگه هرمز و دریای عمان و کشتی‌هایی که در انتظار دریافت مجوز از ایران برای عبور از تنگه هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/675748" target="_blank">📅 15:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675747">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مالکی: ایران به نوعی آمریکا را دور زد
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس، در
#گفتگو
با خبرفوری:
🔹
ایران به نوعی آمریکا را دور زد و عملیات خود را از حالت بازدارندگی خارج کرد و به حالت هجومی درآورد. این موضوع باعث شد آمریکا دست از عملیات علیه زیرساخت‌ها بردارد.
🔹
حملات سنگین جمهوری اسلامی به پایگاه‌های پشتیبانی و عملیاتی آمریکا در کویت و اردن، علت اصلی عقب‌نشینی آمریکا است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/675747" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675746">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stRbIPCaZ7Gw6QgN4JzCWO5xFFU_KEMkssV7J9kRzfTQOOes4WAqgXAV7QoBwv2W5NrHhxgZbzJyCHhWPAkc-xS4Omu4GO9LfyMn3-xgIQL26rlgyRdFlnT0X5-2_bjLOrMxwLsaUzYqi7m_anCKToP_bsRQltZsglBjwR_5yhoyG-g13oKW8LRVw6pJArD0TD8INhgZZv9Fn7wAo7biJxhiaZapLybPWijnnarPKBhGfp6rMR5HfePppzp5txnmp_kfx5B_3mnWWuIh2nesphmIsqSf1yz3aGr0D2cyZbAGu_WY-BuEbSsVTJI5_NK_DUhpovh2sEzv8mPq0gL6dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منو شناسی؛ نسبت استانداردهای قهوه را بشناس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/675746" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675745">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
رسپینا مدعی شد؛ هیچ قطعی در سال ۱۴۰۵ از سوی مشترکین گزارش نشده است!
🔹
به گفته روابط عمومی شرکت رسپینا، سرویس اینترنت این شرکت در سال ۱۴۰۵ بدون افت سرعت و قطعی در دسترس مشترکین بوده است.
اطلاعات بیشتر:
https://isp.respina.net/LTE-b
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/675745" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675741">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ji5gzVbCR_iNs9vKvD653pal4NmUNEEsmK8-_Cp_Y9s2UpimFqsRgKuxeLyVZ037Y9CDDOOL6q0i_lfvwUXKV52sBfvc-4xkbGGV9S9Yt__cw77AOEwm9XXUIx1RsyJvAOcU54n2kDD2gADQbgO2UVGHBqUuaOWHmRYLdYQRwzih8tn87f6CjRRLEfgpwZvbbm_j8xDtsd45O94KEwx35wC-Ka60-Z0Rn5N9WYLjgsRX9mIln1ggt5lGOGF8aFGe1BgnmFOb7LXSH6MprQoNtzFKKNPcXpYD1ng-TvC9ceV4Zk9D4FKJuMpoUu-lS597e6ktNdGs8JtqsZI8h0Jbvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLwcefV6044Kt6ETPwWYZdbxFL-gjv9_3lS-rnYxWSMLywZ1ayivWyQuJfNrODo7-5jYRJVKKbDYdLInII1C-jeqzxp06XX2PEoEM_LS8DP_zO2_7yQ1ge8f6iwHwEmDK3sbZcg3p9Zzvl0n9d4jpcDsD2QY5nI_-fcCNgpAjfHEtayGjGsnK1VW9SBOS2XDARhfc9pXxdtzKmcMRGNHZ1XIaC4CZL6JVzWdVn4tnEvIsVMADVqfPqeWxirjzC5CbyOcaSerC6dQLYdFKyKhRWM7CW1zSS39w3An7cch4_M2pD6_ZJ1Kg1HrbEDAn1e3NDAhGkMlKTlPQ1XE9CDzIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آتش‌سوزی در تأسیسات نفتی بقیق عربستان
🔹
منابع خبری از آتش‌سوزی گسترده در تأسیسات نفتی بقیق عربستان پس از حملات پهپادی و موشکی خبر دادند./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/675741" target="_blank">📅 14:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675740">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0abee407f.mp4?token=uGXlCCK-3tj8Gqios3_BE1-64H8Z18qtEBkTByklbdxrjga-UXwb4ccV1D3y_HIH6mxQNQ59WJb25aOl8tSAAtZolPMIXdNrtv-yntP_0SCgpD9BhLlUUxcUlBARIk-I5k7IJzF9DQvA7AZ5RhApXTG8BSY6eCi7irauHiXOffQcLd6AxuW19L8zYaMypUf6ezc4RAaznTtUnCkSV7vng5nb16KA02sPfDG7N9M3vrvWnZN2dnA859Fkbg3XYoyOc4i2XjhQpLSCCPwjR99f6kM-P7CH0OcIvOIAWbymR_9EScE3v2jrKC03dVUYO-VZdPLQQhCUpxpCCRLvkfPFGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0abee407f.mp4?token=uGXlCCK-3tj8Gqios3_BE1-64H8Z18qtEBkTByklbdxrjga-UXwb4ccV1D3y_HIH6mxQNQ59WJb25aOl8tSAAtZolPMIXdNrtv-yntP_0SCgpD9BhLlUUxcUlBARIk-I5k7IJzF9DQvA7AZ5RhApXTG8BSY6eCi7irauHiXOffQcLd6AxuW19L8zYaMypUf6ezc4RAaznTtUnCkSV7vng5nb16KA02sPfDG7N9M3vrvWnZN2dnA859Fkbg3XYoyOc4i2XjhQpLSCCPwjR99f6kM-P7CH0OcIvOIAWbymR_9EScE3v2jrKC03dVUYO-VZdPLQQhCUpxpCCRLvkfPFGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهند که آتش‌سوزی ناشی از حملات یمن به پالایشگاه جیزان در عربستان، در حال گسترش است و اکنون تقریباً کل پالایشگاه را در بر گرفته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/675740" target="_blank">📅 14:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675739">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
افکار عمومی آمریکا در جنگ ایران علیه ترامپ شد
🔹
در آخرین نظرسنجی سی‌بی‌اس نیوز، آمار بدی برای ترامپ در مورد اقتصاد و ایران وجود دارد.
🔹
یک نظرسنجی جدید سی‌بی‌اس نیوز نشان داد که ۶۵ درصد از آمریکایی‌ها از نحوه مدیریت اقتصاد و ۷۱ درصد از نحوه مدیریت تورم توسط ترامپ ناراضی هستند.
🔹
۶۳ درصد هم فکر می‌کنند که جنگ در ایران برای آمریکا بد پیش می‌رود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/675739" target="_blank">📅 14:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675738">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_IaatnU7Lz__Exvhu1-FL3ywNVwIAgKNg3vG77ywUM3o6KDY9_HT6pyA4SZJg2RXCGpPxjcW62s9TD4kpaGyZsg2nFD2pxuTemCHigI6-Um5-1X0y1oKwf2WAyy9uJHMpsaz6hTzcItIDJHjHWemGxPMmhyQqMKv61WOfyvCDz5PpQYwZMnYC6dixbm2dXGGHfY3aAfCJn249TtpyZJL68NjpuZTp7Jf9x9a4X_9xKsOYOLglFH-O0Fqftuo-_Bl7gRVy0cc0l_FIFEI2rtP4hLI8h0zEznE3WP4zCaoTFzRY-1M3XFQOtwrYUfeKK-c8vDcU3M3OZBIBu_pnePxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
ایران، خانه مشترک همه ماست؛ سرزمینی با فرهنگ‌ها، شهرها و لهجه‌های گوناگون که هرکدام بخشی از هویت آن را شکل داده‌اند. هر اقدام کوچک ما، از حفظ محیط زیست و مصرف بهینه انرژی تا همراهی و همدلی با هموطنان جنوبی‌مان، می‌تواند نشانه‌ای از مسئولیت و عشق به ایران باشد. شما برای ایران چه کاری انجام می‌دهید؟
🔹
همراهان گرامی خبرفوری؛ برای پیوستن به این پویش، یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کنید و با نام و لهجه شهر خودتان بگویید:
«من ... هستم از ... و ایران را دوست دارم، چون ... و به خاطر ایران میخواهم...»
🔸
پیام صوتی خود را با دلیلی که باعث می‌شود ایران را دوست داشته باشید، به آیدی‌های زیر ارسال کنید
👇
#همه_باهم_برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/675738" target="_blank">📅 14:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675736">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نسخه مردم و نخبگان برای نیمکت تیم ملی/ خداحافظی با قلعه نویی و رفقا یا ادامه فعالیت؟
🔹
گزارش خبرفوری در مورد نتایج تیم ملی و توقف یا ادامه همکاری با کادر فنی فعلی به رهبری امیر قلعه نویی را باهم ببینیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/675736" target="_blank">📅 14:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675735">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6cb7ebfa9.mp4?token=GAJxiDEYS2tdv7YNk2D89v1TwxGrlgjh0D5xWhCkEBTtgCG1ez-9aFNLFf2PCGl45ECfwuwli9GbAAONvZPHuPZNJiRn-_d4wjLInyIc8VCT6CxqTcCkStXtwEmcEQCjoMjdm-w_bWx5Yig7HOgYd5sDqxiGul4kdmCVBZxIcIfboaKuXtjF7F5lppofvvIMRELLbvmRewG_hWpHFpeKgW32MbEZZebflvkzXZNH7Xrey06pNOC7ish36wcfC1AMuZR_aSCNqQn-m26s2uvbCy-kXIG5JJ0JgfV-vbalHn-FlUKqvDxzIKMPQU9cn_SctQJdsxCMJoGxdYFV6PfloQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6cb7ebfa9.mp4?token=GAJxiDEYS2tdv7YNk2D89v1TwxGrlgjh0D5xWhCkEBTtgCG1ez-9aFNLFf2PCGl45ECfwuwli9GbAAONvZPHuPZNJiRn-_d4wjLInyIc8VCT6CxqTcCkStXtwEmcEQCjoMjdm-w_bWx5Yig7HOgYd5sDqxiGul4kdmCVBZxIcIfboaKuXtjF7F5lppofvvIMRELLbvmRewG_hWpHFpeKgW32MbEZZebflvkzXZNH7Xrey06pNOC7ish36wcfC1AMuZR_aSCNqQn-m26s2uvbCy-kXIG5JJ0JgfV-vbalHn-FlUKqvDxzIKMPQU9cn_SctQJdsxCMJoGxdYFV6PfloQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود سگ‌های رباتیک به آموزش‌های رزمی ارتش چین
🔹
سگ‌های رباتیک در کنار سربازان چینی در حال آموزش هستند و برای مأموریت‌های رزمی، شناسایی و پشتیبانی به کار گرفته می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/675735" target="_blank">📅 14:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675729">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYiKJDv_I-R5k7xPxDi5HTIiFGLDaHJ49aGsgD31YbnxMsWZ5qlJ_BX9qYdEn1d8u-DrvJVAaoKH3xoPgftUK4DLssOb3_Sc_6-R0oX4R5MwZ4yIIdV7BoRWQls16CktWGR9DRy5S-QpPHrPCfygx5M1_LGwZmO7IQQquqAA-KKiN-L0ap6rGecMUX9DHBOWbFiHgV-e7i1wDgzq015ts1kZQl9CHBdUqqcOVOMahQYgYoXcAY8j9JKbGy17nAofCHFvz3eQ-lP0aCtGqJfOLMqcFnlyAHuuHF1Dzje5mije1FgXrWevUo5C-OY8GmqGddxXimlZnFgJHuaMgxQq8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BLhSi1x_hc89tNd8kUjc4px_s2aAwOP5V9B93gf0ZVioDsnxZ6HiJQKqw9hAnNQKeUQo_RkY4Mtye-kB15H0NciNrtLcQlSki3VR1qZZQoxXtaMcbKUbgs29O5t-RZHb7r2IUs70yApUIPMD4oD4AA2mm3oYX5b44MuWtHR60hU6dEbBScArBNnbEjiCzVxFOC-cJ714rydPiBg9BfHDwROc8cykKK-7EpjaBbKxX5wvI5hrRY1BKPNTyUseyj2dJgybGzy-BA8xYUuLrGwHwUvSVCaJQTaCx80pPS8pHbW3ByBjlPb8G5znOJQjWTXIWL5UtFqpO9RWaOxuUwqiQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSWrXGYWVMTYL_7zj7IUipnAcBy1dSxd1AyPCNy4bh6zdQIVSYsPUAkX3cdBhmcBSMwAEPz4uZFBOeLM8OftBqpizrkTlMKlGnB0MLpyHzp5zP_3wteYBoJxuqqB2_qgURIBm-c8CEAshrSBk7LRDmRUCHxqIEgK2OpZtcbWLfEMkgqDTyk5nVbmU1S7KShdzc9xsPQECtwL8qJmWw36AwmY05ihw4F_oEuHdRt_0GNCnEKTTs_DGogJ8DMjwq3_WQtbBR76BTB0iaKe5-UQBU10406d87xLBTj10dC3r8cHm2w-kWHqB5yc1kIF1p1mkQcz4Ed7mEzVCssIQpvDeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAmlZTJmSZXxdPDop6ZeEUJvC0JbRESk1eEVvURIO12pu2KRSwEJ2ZgH1KA8araE2hVh3n2q-tYXTF8BuWkExR73HlwH3TfmcWo9oZitZBFkE_matSolsP3utLj9uHBBhtx1hDcnoDZy7GMYlC0sPud0q_GQhaIK-jrQlMtrBGAespAL3Re1wWWmaoqxKaSovGbvnxrFTIMn1iI73ocAvCTWl9MyhJMLsnyQrvDdKfzgqZt0DFVuc0v6ZtdJIEzSr0GWFoBdBMZpNd-U5y_zb7kvHY9B_MCbGDdXtfPsUeadVW9sLjjSq2NAuOqBjrj8LDkUPpjOW6PUzKrvmnj1ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۴نوشیدنی برای کاهش استرس؛ کورتیزول رو پایین بیار
🥤
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/675729" target="_blank">📅 14:21 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
