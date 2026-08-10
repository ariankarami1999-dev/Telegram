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
<img src="https://cdn4.telesco.pe/file/LS3aAaFhtq0KVGUsAKWBXtM5RKCtqYzs077z4e2EHIw3oA-UhYQKODuLcm8ENz0V8pkOFf6AfjFe_Bv4Yr-Ru50z8IodLnnToCXrYCHDvlQyuzwWj71arb89cGAAUvj2vtztZ-ii3ZDv4Ak4M8iAsBLtrt42DQvmAEktxn0haRfhgZ1XB7kf_yQktJNoOEH2wyPVxy-5yUzh0vPOqd2T3Z6NRGChWZ8zqREtKxQ0PVZkK8DjvgeaAB5JFO2ubG9sPIzdLjPcbOoY2t8TeQ5TKj_NqU8aqL9-TszyCSA5WArgXoKCAJwzrunJjBLkO1rJRhtP6_GsoZFrLKMsin1gmw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 18:58:47</div>
<hr>

<div class="tg-post" id="msg-455356">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۴.۷ ریشتر در مرز استان‌های خوزستان، ایلام و لرستان و حوالی حسینیه به وقوع پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 685 · <a href="https://t.me/farsna/455356" target="_blank">📅 18:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455355">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0893f142a.mp4?token=MtoQ0-oSpJpHfLZT7aBBlXeBplDbpbjUvqXqg_IfOo6E-BavbmlSztF4gBo6efUC4bArNRfxF3sJRfrfYHqT6dYh2uyaKrErccsnVPProUM5AQfTfWhRvgW1wp9IICoRlub7E-9DxriaJRMTMes8ZGe7o6B744LTU2TluGwArb9jrGOw27xosfZ-cHIdEabFaOkkP47-hS4uo-4IXa4QTAgYhqVMIcIfWg5YV28WA1mHOkP8zmU6Wx4RFUUgjWagKOV-fIFECLesn7hW2Dj1meaT9VOZSElydwyBtKK3Lnf1wDe3rysTsDUrcIxbl1NRHDZ3WPyEnwwOW9yvWStt8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0893f142a.mp4?token=MtoQ0-oSpJpHfLZT7aBBlXeBplDbpbjUvqXqg_IfOo6E-BavbmlSztF4gBo6efUC4bArNRfxF3sJRfrfYHqT6dYh2uyaKrErccsnVPProUM5AQfTfWhRvgW1wp9IICoRlub7E-9DxriaJRMTMes8ZGe7o6B744LTU2TluGwArb9jrGOw27xosfZ-cHIdEabFaOkkP47-hS4uo-4IXa4QTAgYhqVMIcIfWg5YV28WA1mHOkP8zmU6Wx4RFUUgjWagKOV-fIFECLesn7hW2Dj1meaT9VOZSElydwyBtKK3Lnf1wDe3rysTsDUrcIxbl1NRHDZ3WPyEnwwOW9yvWStt8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آموزش نحوهٔ برخورد با سلبریتی‌ها در یک سریال
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/farsna/455355" target="_blank">📅 18:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455354">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPjrNp3WBHPM8isaOU7-CHTsKQ-tyCLSn5AfUwnTLOFyT9dZQBMYvUqpTt0CE7dgvSmmlm9w0tsc2uM19uypAugTWxoArffRNcaIRTtXcwiJghw13iVBGsU36G7bEeVKKKDjBO4SE13UBTOw7sHXBTFRCm7NyU0YxUox1XD_ZBpP7t9M_e-hfak0Q165eVzVa9sUOwe73YnOZ8FyVBkRezGCKetpeUcfCNH9lvpbCtmpVyOL6LesnuHaeIRBASMoO7q8IaEyPYMXeYugQArol5maeEg7uGUj3937OUoZkhPR4fFHE5I5rgKN0SOtScTCY1VIX-vPxgxByZf3_fUYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: با توفیق خداوند پالایشگاه آرامکو در جیزان را با استفاده از پهپاد به‌صورت دقیق هدف قرار دادیم.
🔹
این اقدام در پاسخ به نفوذ پهپادهای دشمن سعودی به حریم هوایی استان‌های صعده و حجه صورت گرفت. @Farsna</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farsna/455354" target="_blank">📅 18:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455352">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FobmflJpS7MCUcGjmdUxAragLY5LLODCgjKuvOMiupBM9BAeHUVm76RXpCiEgDanTPxEgMMgPMJMSWGKFUMMZUFlzyzhWMQmTHnrWQwz_2IRpXprB2AfPJIH5sAoTLe2J7Ad0spxiNZXRRSnwt71XcMkp0rqI9va901Ej8WnAvQ8vhQTzDTrst2GOq__5gdA4FBw2_pY-W0KjKSKPLFkYzc3DCLatBpu1b3rVC-sfK4BUAwybu5b1UP-biNsDBmMaazQoMU0H-Uo0UiCxBd2LShpdmUawp9uVOTxCbmRO9XhpAwuWdJotMWEgmvlR9EXcKtwnL7EKbOPmMznloJwGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تا ساعتی دیگر احکام انتصاب تنی چند از فرماندهان بلندپایه نظامی جمهوری اسلامی ایران توسط فرمانده معظم کل قوا منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/455352" target="_blank">📅 18:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455351">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8b99ad50.mp4?token=nlRzqPxObW5hekZcoobManlsftad5jzf6v1aW9b5XDXyREh_WX8rNNykfzYrFuarAksMdBA3_36DBc2mEfqUnoKkgqyTx4QolRb1I7sHQ_Z78majXMT4BR3ZEoeq2a3N2G_tSv644sLoL4gnDpvE-8_w454nDbi3-jsRr9rNnWJc2otNsP1DJWU9aZqunojisT_F-jMHCt0zrs3WJVfDcaq9HyKinrCsAtNZ4Bf2p66AZ0I0t0uj1Djxoz3RrTDXd755_IO-1VeZ3u2HVy-llVvaseaX5xbWqFzmh6oHsY_vbJiz7UPoEVS8bUT1Pc91m6qYyzlDXCaxcT6jTkxx2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8b99ad50.mp4?token=nlRzqPxObW5hekZcoobManlsftad5jzf6v1aW9b5XDXyREh_WX8rNNykfzYrFuarAksMdBA3_36DBc2mEfqUnoKkgqyTx4QolRb1I7sHQ_Z78majXMT4BR3ZEoeq2a3N2G_tSv644sLoL4gnDpvE-8_w454nDbi3-jsRr9rNnWJc2otNsP1DJWU9aZqunojisT_F-jMHCt0zrs3WJVfDcaq9HyKinrCsAtNZ4Bf2p66AZ0I0t0uj1Djxoz3RrTDXd755_IO-1VeZ3u2HVy-llVvaseaX5xbWqFzmh6oHsY_vbJiz7UPoEVS8bUT1Pc91m6qYyzlDXCaxcT6jTkxx2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاکسی پرنده سریال پایتخت در واقعیت وجود دارد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/455351" target="_blank">📅 18:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455350">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1921d9c71.mp4?token=ZyZQv9YwMv-Q2D1PSSwDWf3wI0gbewYR55wBAjhRFNlXNtAtT6nNukq_8Xl1bmGnQakawlyiavy-6BjhrkkgGtb9FIfwQvPSJ0PMau4zJ4koHr6OZC3sRAfs98mBKN4XXebhcEg9uIV1iX0Gc7l30AtM2HA-R5HPGaffAdtFsN-hMJH88TQkyHyLHm3IH3z4Ywm5Z9zGzrKEgSfIi5vbhcLwtaLZOKkrjeDW68tjX7_1IbOXCWAFLIKJe877dvI4wl0F2b8ZuwwKH22nKt_szvQVa2-cO_3aCFFt5G-K4DncsSAwmOUus1V8HFmDjNcElaeVy99_ltfGq7JXCU9F5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1921d9c71.mp4?token=ZyZQv9YwMv-Q2D1PSSwDWf3wI0gbewYR55wBAjhRFNlXNtAtT6nNukq_8Xl1bmGnQakawlyiavy-6BjhrkkgGtb9FIfwQvPSJ0PMau4zJ4koHr6OZC3sRAfs98mBKN4XXebhcEg9uIV1iX0Gc7l30AtM2HA-R5HPGaffAdtFsN-hMJH88TQkyHyLHm3IH3z4Ywm5Z9zGzrKEgSfIi5vbhcLwtaLZOKkrjeDW68tjX7_1IbOXCWAFLIKJe877dvI4wl0F2b8ZuwwKH22nKt_szvQVa2-cO_3aCFFt5G-K4DncsSAwmOUus1V8HFmDjNcElaeVy99_ltfGq7JXCU9F5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه سردردهایی خطرناک هستند؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/farsna/455350" target="_blank">📅 18:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455349">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3205d65f27.mp4?token=IynMFTrwKVBd0vZ-flk2qF3w0hbD5KqIDv2hpOxg-yXdPyljdDLsRjAaUU5B1al2BE9wFA-tPRXC1EK27fekqLwX4X82-mHYF4PRu92QAQ5vNqz3O_XXqrbmJ7DimG4d9wBU5P_uCmJF3Se-mgpyTQ0cWjNQ7Y_3aC1G7CGgt23T5oAnBi8L2B0EZUOd81VM9DILaCyojleCQpeNMA7TdjMdP-8114oU-_M1LuFELDOp1o5tQOedifcQrISCME_pFXrnPZR-kKgSKxVu1QU5rSAMlglNkd36LkbYtpgi_ePBlL-l-vZ4YJgNzA4bd8OBq3KNGVB-Z1GoEHZIKKM_bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3205d65f27.mp4?token=IynMFTrwKVBd0vZ-flk2qF3w0hbD5KqIDv2hpOxg-yXdPyljdDLsRjAaUU5B1al2BE9wFA-tPRXC1EK27fekqLwX4X82-mHYF4PRu92QAQ5vNqz3O_XXqrbmJ7DimG4d9wBU5P_uCmJF3Se-mgpyTQ0cWjNQ7Y_3aC1G7CGgt23T5oAnBi8L2B0EZUOd81VM9DILaCyojleCQpeNMA7TdjMdP-8114oU-_M1LuFELDOp1o5tQOedifcQrISCME_pFXrnPZR-kKgSKxVu1QU5rSAMlglNkd36LkbYtpgi_ePBlL-l-vZ4YJgNzA4bd8OBq3KNGVB-Z1GoEHZIKKM_bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین تصاویر ماهواره‌ای از تنگه‌ هرمز
🔹
ترامپ می‌گوید، «تنگه هرمز باز است و ما آن را کنترل می‌کنیم» اما پایش‌های دریایی می‌گوید معدود کشتی‌های عبوری از مسیر ایران تردد می‌کنند.
🔹
داده‌های شرکت رهیابی تردد دریایی مارین نشان می‌دهد عبور از تنگه هرمز به میزان محسوسی کم شده و جریان عبور از مسیر ایران برقرار است؛ پایش‌ ماهواره‌ای این شرکت می‌گوید تردد در تنگه هرمز روز یک‌شنبه نسبت به جمعه ۹ کشتی کم شده است.
🔸
شب گذشته تصاویری از شعله‌های آتش در نزدیکی تنگه هرمز منتشر شد که گفته می‌شد شناوری در منطقه «کمزار» آب‌های عمان در حال سوختن بوده؛ ساعاتی بعد تصاویر نشان داد که یک کشتی که می‌خواسته با اسکورت آمریکا وارد تنگه هرمز شود، هدف قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/455349" target="_blank">📅 18:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455348">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54ef328501.mp4?token=u7vXbL6FnIJEK7Nb-VrTXY76hlj4ngFuPz-LI_o-0n-wWG6VzJxN_6VQ89lKXvKh8Tw5gnb5iAXfYs5qkPP2YcZax2XQzBg7oPu2ydla1WuVnHtZ2l4zHGI0wWXrteDZfaZj7woGkD9SpNGBMMfEO6Nl2GFykFkMdZhszYfy9068rRYjjruRu895V4ZxwEQGVmX1QspGpLtEq4a7gA64xbyjSc_E771vACAOCrijcGqyv6bp9yYquMAMvcmri8gB5Yj3p5pI42QP6cKFGRQ47XMT3xCLsTjEfWA5rkDwa4Fsma9-LoAefRD3wKoweYoihx_B0cih-2aAUlq-Yk26rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54ef328501.mp4?token=u7vXbL6FnIJEK7Nb-VrTXY76hlj4ngFuPz-LI_o-0n-wWG6VzJxN_6VQ89lKXvKh8Tw5gnb5iAXfYs5qkPP2YcZax2XQzBg7oPu2ydla1WuVnHtZ2l4zHGI0wWXrteDZfaZj7woGkD9SpNGBMMfEO6Nl2GFykFkMdZhszYfy9068rRYjjruRu895V4ZxwEQGVmX1QspGpLtEq4a7gA64xbyjSc_E771vACAOCrijcGqyv6bp9yYquMAMvcmri8gB5Yj3p5pI42QP6cKFGRQ47XMT3xCLsTjEfWA5rkDwa4Fsma9-LoAefRD3wKoweYoihx_B0cih-2aAUlq-Yk26rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغوش خالی مادر پشت کیک تولد دخترش
🔸
هنا دهقانی قرار بود ۱۰ ساله شود، اما موشک آمریکایی مدرسه و قلب پدر را ویران کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/farsna/455348" target="_blank">📅 18:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455347">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84326ff6a4.mp4?token=JqiHeRQcEv9GNeqnyFwsUvkUmJmZEyfBHen9ftDoajVnLkwaS_IGo2Nd9eHmYTNC8KbJWpjmxX3GfZfqi_slc1HD2A1bpE9UOzUBxcfAbswKwy0aEGbHG4Tn3w3bcEZptoroy0gKYbx74ccSF8Xo5TV5cMTBKugxoWyNYlrCYD63NuQjWP-eCy3YJZOaoDUOdHMnSm1NJ5WjBWaV1aElG9dDjCPCpSL91B8WGT_LZpyMASBEwcLnLpYh-lw-yYYdzMipmEGEbg4TM7Tj8JzpRSyJRzcR6jetHTyg32NQhasHUcUBHn3jt4ss7TjxtXGASeVjm8VANqngp56Fbso-oRDgOYXLRSsLBennTzo-iGdJF9Ic0aRnxVMBL2rmKF4eyS-5eXufH018AZGl_YKh069EreEzWhwSGFzhUrjf8SPsO-npEodiTaZS2ZSoDLyhA8xWtmUmtJPMxb1XZjk6kmN9Xtz2PtNQIRMXgCnSPba-fhSl_oXEY64fsVU1XnDEdtLMIEm2kCktltBuvvsFVbZxlhnXmFQiVDmRFKdS0K-fvDp5BSz2BrHhu9TAlPPjb1qRzYt0r8hzedbQm_Is4o7YRvJVXT_hdZQBXdEdB5B4HGmhUJFSgcUNqeMyA4LKiwtoBFYYcr8xqrbbkfSWn_rH-CDnphMlk9DBVXULG8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84326ff6a4.mp4?token=JqiHeRQcEv9GNeqnyFwsUvkUmJmZEyfBHen9ftDoajVnLkwaS_IGo2Nd9eHmYTNC8KbJWpjmxX3GfZfqi_slc1HD2A1bpE9UOzUBxcfAbswKwy0aEGbHG4Tn3w3bcEZptoroy0gKYbx74ccSF8Xo5TV5cMTBKugxoWyNYlrCYD63NuQjWP-eCy3YJZOaoDUOdHMnSm1NJ5WjBWaV1aElG9dDjCPCpSL91B8WGT_LZpyMASBEwcLnLpYh-lw-yYYdzMipmEGEbg4TM7Tj8JzpRSyJRzcR6jetHTyg32NQhasHUcUBHn3jt4ss7TjxtXGASeVjm8VANqngp56Fbso-oRDgOYXLRSsLBennTzo-iGdJF9Ic0aRnxVMBL2rmKF4eyS-5eXufH018AZGl_YKh069EreEzWhwSGFzhUrjf8SPsO-npEodiTaZS2ZSoDLyhA8xWtmUmtJPMxb1XZjk6kmN9Xtz2PtNQIRMXgCnSPba-fhSl_oXEY64fsVU1XnDEdtLMIEm2kCktltBuvvsFVbZxlhnXmFQiVDmRFKdS0K-fvDp5BSz2BrHhu9TAlPPjb1qRzYt0r8hzedbQm_Is4o7YRvJVXT_hdZQBXdEdB5B4HGmhUJFSgcUNqeMyA4LKiwtoBFYYcr8xqrbbkfSWn_rH-CDnphMlk9DBVXULG8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهی که شنوا و ناشنوا نمی‌شناسد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/455347" target="_blank">📅 17:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455346">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حملات پهپادی یمن به مزدوران ریاض در «المخا»
🔹
شبکه سعودی العربیه مدعی شد سامانه‌های پدافندی مزدوران این کشور در المخا در حال مقابله با پهپادهاست، هنوز درباره تلفات احتمالی ناشی از این حملات، خبری منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/455346" target="_blank">📅 17:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455345">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccc08889a.mp4?token=WrOJtln0d1eZoUuDL_UZi4dzR3cc5HWJYvU97MATACVgVRglKEZZ5W86LWAcyH6B5UNwkwjkL26WckFwMx43U-MV3UrhyrU7E8WzNDOV4lVH6fKwTd1gmu4H3Fshja6bN8PgMeg0DBZtErJ7Gva4vkXIq846qzwSEkoPXFzEmCXfukuZDOrK-viYtpwZzM-tlrxkJUYmM9bb1B4wJFk-f3tpQuhyEvnNKs8PDvPdF3XMnjpUM-reVML-2MTKzrR_8STRh_llSBVwPOed9dFYQ90mvOcaAJIMhd7DmWf_yIDfAaZXx_-fUYf_SPM6XdAAbqzfiEYAO-sz-D1Ndn4UAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccc08889a.mp4?token=WrOJtln0d1eZoUuDL_UZi4dzR3cc5HWJYvU97MATACVgVRglKEZZ5W86LWAcyH6B5UNwkwjkL26WckFwMx43U-MV3UrhyrU7E8WzNDOV4lVH6fKwTd1gmu4H3Fshja6bN8PgMeg0DBZtErJ7Gva4vkXIq846qzwSEkoPXFzEmCXfukuZDOrK-viYtpwZzM-tlrxkJUYmM9bb1B4wJFk-f3tpQuhyEvnNKs8PDvPdF3XMnjpUM-reVML-2MTKzrR_8STRh_llSBVwPOed9dFYQ90mvOcaAJIMhd7DmWf_yIDfAaZXx_-fUYf_SPM6XdAAbqzfiEYAO-sz-D1Ndn4UAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سودی که از کنوانسیون خزر به جیب اروپا می‌رود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/455345" target="_blank">📅 17:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455344">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1361d468b1.mp4?token=AQ9LknnaYhVzIIZSsiaqwfJwiX_FUbpXMr7wWi3cTCp9V1ujYaa7CWsBTNejIxa7K4NClJ2p1mUt299AaQ7Wq3yAMTShqnL3e1PALnfH25ZxAa-S6mRlF1kc1EcyoKH43qJHlJUMdIeEbygCNODrjBCcuAwnHpLLzoJKQZWgtaPB2kUgAbpDQMZGhBVyopKBOoa932ORJU3ac4cteQC-bYilTwZkj9a7_IsPvafsGFrQEZgAiph_IZU6dN03rZvAetd-cI4T7zcRYyDYZc0NFqEWTrtxDC7FwUJo1l_KLkxAgxImTHsR9hmJDdAQ8Zd7TaNd_aay1quOFrpjjpk3Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1361d468b1.mp4?token=AQ9LknnaYhVzIIZSsiaqwfJwiX_FUbpXMr7wWi3cTCp9V1ujYaa7CWsBTNejIxa7K4NClJ2p1mUt299AaQ7Wq3yAMTShqnL3e1PALnfH25ZxAa-S6mRlF1kc1EcyoKH43qJHlJUMdIeEbygCNODrjBCcuAwnHpLLzoJKQZWgtaPB2kUgAbpDQMZGhBVyopKBOoa932ORJU3ac4cteQC-bYilTwZkj9a7_IsPvafsGFrQEZgAiph_IZU6dN03rZvAetd-cI4T7zcRYyDYZc0NFqEWTrtxDC7FwUJo1l_KLkxAgxImTHsR9hmJDdAQ8Zd7TaNd_aay1quOFrpjjpk3Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: مردمی که به خیابان آمدند معرکه برپا کردند و کارشان خیلی باارزش است
🔹
کسانی هم که به خیابان نیامدند، اما با وجود گلایه‌ها، کمبودها و گرانی‌ها با دشمن همراهی نکردند، کار بزرگی کردند؛ دستشان درد نکند. @Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/455344" target="_blank">📅 17:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455343">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad0c712aa.mp4?token=ezHo2LZKlwzOh_6OMMPb8Ke48ZywxUBT8wW9nLzhoRMUxkfmfdvyq1HEACmzDvt2ywJFw4N-7WZZ_sBwDRhZcOzycx_IVFWrF4TWB1TUERk5Tgyybh_Gv5Lu7Xb1uJYo-JI5cNesrtSgOc_6OY5L8fugbakVT4PLZO3LDPUpYLZHSAQQsIihRSMwDkgAezIykGRA3JAq23dn83xPZD_DByglhI2Mmykh-QZJtkviJ9sSj7_BYcwxLsfxLxQzYctyddvESy-6E2ZKQQ8-yqmFghLtODC5arkIjwthd-N2Zm6MDJXBy_XIvPyvvijcTMSL7gouAeoU21s_Gy3r6O6T1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad0c712aa.mp4?token=ezHo2LZKlwzOh_6OMMPb8Ke48ZywxUBT8wW9nLzhoRMUxkfmfdvyq1HEACmzDvt2ywJFw4N-7WZZ_sBwDRhZcOzycx_IVFWrF4TWB1TUERk5Tgyybh_Gv5Lu7Xb1uJYo-JI5cNesrtSgOc_6OY5L8fugbakVT4PLZO3LDPUpYLZHSAQQsIihRSMwDkgAezIykGRA3JAq23dn83xPZD_DByglhI2Mmykh-QZJtkviJ9sSj7_BYcwxLsfxLxQzYctyddvESy-6E2ZKQQ8-yqmFghLtODC5arkIjwthd-N2Zm6MDJXBy_XIvPyvvijcTMSL7gouAeoU21s_Gy3r6O6T1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چین در محاصرهٔ طوفان دلفین قرار گرفت!
🔹
تلویزیون مرکزی چین از وقوع طوفان سهمگین دلفین در چجیانگ خبر داد؛ حادثه‌ای که با وزش بادهای شدید همراه بوده و وضعیت اضطراری ایجاد کرده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/455343" target="_blank">📅 17:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455342">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39091f25b.mp4?token=F8McyYssLmH-lZ8FXYBbC1khpnxC6fKj5_LwRs-nEBH187piCfVaQnqlTEN3TvbhK7Y1SyP1rN_APxjWOccPKV9F-6RhICeFd9wLbKaFE7SZfKJi4JazOw6YrFfqFlTN5X1tbWjzvxDh5-sTZA_tcZ98C6veydOLUmh-MtzLzjoMRTniiSTMchAvwI0SiqZNoMAN1e3Nx5FpDRv9Vf0qz_lNOzWygvcykjvDzUgx0yrtJ-bY0CsYv7SalXSaWcg4M4E4Qd8GzJAv1y5nk7pA8EAkEQG1eTKOCo5R7a45_WCZPXDRV1PELXpxQELkgqzgEorQihsBGkSZsuA4w-NXTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39091f25b.mp4?token=F8McyYssLmH-lZ8FXYBbC1khpnxC6fKj5_LwRs-nEBH187piCfVaQnqlTEN3TvbhK7Y1SyP1rN_APxjWOccPKV9F-6RhICeFd9wLbKaFE7SZfKJi4JazOw6YrFfqFlTN5X1tbWjzvxDh5-sTZA_tcZ98C6veydOLUmh-MtzLzjoMRTniiSTMchAvwI0SiqZNoMAN1e3Nx5FpDRv9Vf0qz_lNOzWygvcykjvDzUgx0yrtJ-bY0CsYv7SalXSaWcg4M4E4Qd8GzJAv1y5nk7pA8EAkEQG1eTKOCo5R7a45_WCZPXDRV1PELXpxQELkgqzgEorQihsBGkSZsuA4w-NXTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: خدمت رهبر انقلاب رسیدیم و از هر دری گفتیم
🔹
ایشان از لحاظ جسمی  در صحت و سلامت کامل بودند و رهنمودهای خود را ارائه فرمودند. @Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/455342" target="_blank">📅 17:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455341">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89e6f90d9e.mp4?token=u4Nho8aFzs9rDo4l6PaoqqSQe3DfwLlkLqlR9XW_sXmjbr3u311hBF_JpokxmmjldZFSOnTK18dvIWH7tU-c1Ba-s-xMUO0wXpCT6SzTLUDc2RV5Q3piHyn0HjinF8vt_RSf4CmT5In0_OsWsoNLTAXquEo-pXi1Re8pm6FJD8Rjo9vD2GdwqOd_6b9bJd2HKT8FRwXTdUTWWaxP2Oo_TZlWkWg9aJp7L9oZuzBPT_bTkcXkcFxUMzsy1B8VqoH9ousapeE_KryWc-K-ACu6lAUyHPbTdzemjFYARyPNKSjFD3YPUCz8ooZCHOqn4LAN0LJjgpoGnPkUKClDgxVuBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89e6f90d9e.mp4?token=u4Nho8aFzs9rDo4l6PaoqqSQe3DfwLlkLqlR9XW_sXmjbr3u311hBF_JpokxmmjldZFSOnTK18dvIWH7tU-c1Ba-s-xMUO0wXpCT6SzTLUDc2RV5Q3piHyn0HjinF8vt_RSf4CmT5In0_OsWsoNLTAXquEo-pXi1Re8pm6FJD8Rjo9vD2GdwqOd_6b9bJd2HKT8FRwXTdUTWWaxP2Oo_TZlWkWg9aJp7L9oZuzBPT_bTkcXkcFxUMzsy1B8VqoH9ousapeE_KryWc-K-ACu6lAUyHPbTdzemjFYARyPNKSjFD3YPUCz8ooZCHOqn4LAN0LJjgpoGnPkUKClDgxVuBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس‌جمهور از دیدار ۷ ساعته با رهبر معظم انقلاب
🔹
پزشکیان: رهبر انقلاب بر حفظ وحدت و انسجام ملی و توجه به معیشت مردم تاکید داشتند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/455341" target="_blank">📅 17:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455336">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmDRO17JV0WJaEvSUWdpQLC0U82_gq4PktMNn8QkTZ1zHr19wPE7pPaCQd73N_xnaBluHb39HZ-XcRwegCur8bQB6_kD86zpaM0GsEDubx6_q0nD2KuaVbyhKe1kFC7bzJA7h8yDXKbYGLcZhDLofDGLwbYWTlQxEghLo3npvicXI8zwVhFpSHpuP5T5JWTIsQcIKyjG4EilFsQ2ofW6Dc6B73Xcluq10qar0BJEPLIdfHrS_gOOHIy8z076Fve0YG1Fz_0_n_EAV9538BA32XNWoqUdChI0TpAxz78wW-b9l2mrCihi42ZM3iaxExMiila7Uko0tG7Mcg0D0tftEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqOf6tX78IAak5xrUKVTf8mOkzl36JGxPyyqJzEr-5yGz0iwMxt_Xzbe2U-CCqxw1rmpivb9qNIb67igT_dLeGToZ53mOjmzqhvO_ggURlLU5gFc022sEs8VOC3YKNq-u7Xne7eEziukY8S_TdccelBMXdeoGSSHaH4Bb1m4xWcdKJTdM3U1ooik49K2S7JWR_3A2H1MKzD0DxQkwAaP37YZoexwYDS0W_0UQdqVL_Rygeg8047peL8HU5BC0aoCsbmnEGK9VI2sl_AOdMxpviNEJWdsSRHaY6GH3Mi5HbKn2UgcswsYK-Yl1we43Flo0bygMfhASCwX2kCmx8Uc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EvKsicmJq0-FNba5Eu7m6TcLO1InH6uUeNMu2ApqVBFMNNkTCJCY1bb9Fa9L2MngceEprGf8Y25NMvf5TW50_CxM-BmCPoVRm8CZQKfU_M_9Gid459HuMnrfs9YYFKNvJoRnZtFq6W35zjd_mzFDNzAzj1wzY7WgCzKJ6wu8vsFauM6hEATvmcrTG-n-oHcxuTo1i9ntmN5xoSvVrYUEUsVfzmUiDSOdafBcXLUjT9YYIYEzjUpdF1aSXoLPkd5FGM_GO3YF3p2cndLC251i9IjEl3q5mz31F586uQKy5brr0TdK4anxxI1uT3-mfqgr0ta8TIIA2DzBQ6bA2bcKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEbFMTR8EL-shnwHrvx6omVfLQPCnr1cSAkhgLijIPghsQo5MvaBrzYylwm6s7bnw_jZ_P_AmFbIWxIexrHA8vLYrydYhMRilN8c2ZHd40LBS82bh-9FwUE0ytb3wlSMRzbyh7fRJ7A9569sjHvRM_i1jHNtj80DToBwYK1ZLNJ7AhK8DQgECGJCtPrE56wIJnxAeRRcg74_OLZ2S-9b0HGzng9m12qZuU6v8SddJb8Ce1r05GLozR_qOdqezQ7YsspTLjDvjKiJ21XCqvYLljGWZ7C-6Ubv0P_-EqB9FAK6D-Aqr9_l_SdxNdY09W6xr9Yk-v8STewcaTG--lLI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ieqNmG4MeXVMvk7PK4cTnr3FC65HC-tUK5nt22rHX56IRzbMzeqypZ-43bQmLExMMAKGiSVUvTQQxW9jeF6WbN4_LjmC_9Vq81QpphhGv5wQNce4AhJxZab_67VJTDduMWfWjTaTAlL0tUEtyBhbX1fFJTVceRapOt6W3dEpB3VtD-RREDzz7J4fmLVyCeVoH7f3QU1n121VXPSaQHKQ24zCDn5QIZwq04yO7xL0CZqWsgfNrIxkucYow2pZrWLtvqs5Osrj69AX9FsAa5at_y1Ab0l1WyjLbR5jDJ4rJcVoRY-7yHBmshh6FI81GiVt0OMpVW1LNWjSqroqfakSmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسیر بهشت، آمادهٔ میزبانی
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/455336" target="_blank">📅 17:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455335">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab61161747.mp4?token=H94hNXnLscQ5aqlqyGebMkUyYWMyRQmdngRugclJ3Ym7Z0wlqrXvU7xbR1krJGyn6012L-EnRBjosEfG2Zjr_zm3PPF6P6fMy9W09J_MmFUZ3zUYG1ASGrPUR3VaESRvmL_saZBkaveM8K8fB6PVe8YS354BCqH-6At4gdFTCrQf5zr8l8dAG3yYV2AWOoaRRTz04qBNy_GI-auDMCa8jVh8rx1CxezvwEyrBkQA2EsCH2VHzP0uu8_lzNvpSIHDFCnsmRP682i1ck0n7qP0FWHSTgdles2u1RmLf2FmDtQ7bKHTxLZ0c65TZ_Wc0cCWoYN2oV4J3526nmPDZMA0Vi8zJ42PZId78bXHil4f_n_jk3OTvsoEOEPJczyf_e6_1uwPNlneLLCUMtsBLZ4jLiI4AVK_1tHzhZTfkr_VZ8FSvoLtg350fNE869qHQD6WCaJrLEh75Ce_4PnOAvGTHntMPm7RErQWtC3RlSQ6ZboYVpavwdLGTNFNHet1NIoZisDVB6_Hxq6x-0xx85k82XvPqa0T2SjnVt8aIA9Mp0gY8sJ1Va5vJQMCMzGHRJ5fPRxJkhrJk6_mRXRYdlYVewC3sXOtT1Wi0GX1-lDSAZMAAxg0vcBOC8dHWMFnbTcCc-Ap1POmy3wOqkW7ROm-E9P8UT528yX8PAixRh2TQK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab61161747.mp4?token=H94hNXnLscQ5aqlqyGebMkUyYWMyRQmdngRugclJ3Ym7Z0wlqrXvU7xbR1krJGyn6012L-EnRBjosEfG2Zjr_zm3PPF6P6fMy9W09J_MmFUZ3zUYG1ASGrPUR3VaESRvmL_saZBkaveM8K8fB6PVe8YS354BCqH-6At4gdFTCrQf5zr8l8dAG3yYV2AWOoaRRTz04qBNy_GI-auDMCa8jVh8rx1CxezvwEyrBkQA2EsCH2VHzP0uu8_lzNvpSIHDFCnsmRP682i1ck0n7qP0FWHSTgdles2u1RmLf2FmDtQ7bKHTxLZ0c65TZ_Wc0cCWoYN2oV4J3526nmPDZMA0Vi8zJ42PZId78bXHil4f_n_jk3OTvsoEOEPJczyf_e6_1uwPNlneLLCUMtsBLZ4jLiI4AVK_1tHzhZTfkr_VZ8FSvoLtg350fNE869qHQD6WCaJrLEh75Ce_4PnOAvGTHntMPm7RErQWtC3RlSQ6ZboYVpavwdLGTNFNHet1NIoZisDVB6_Hxq6x-0xx85k82XvPqa0T2SjnVt8aIA9Mp0gY8sJ1Va5vJQMCMzGHRJ5fPRxJkhrJk6_mRXRYdlYVewC3sXOtT1Wi0GX1-lDSAZMAAxg0vcBOC8dHWMFnbTcCc-Ap1POmy3wOqkW7ROm-E9P8UT528yX8PAixRh2TQK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پژوهشگاه رویان: اروپایی‌ها ایران را برای درمان ناباروری انتخاب می‌کنند
🔹
شاهوردی، رئیس پژوهشگاه رویان: پیش از چالش‌های یک سال تا یک سال و نیم اخیر، سالانه بیش از ۵۰۰ زوج نابارور خارجی در پژوهشگاه رویان پذیرش می‌شدند.
🔹
بیماران مسلمان از کشورهای اروپایی، از جمله انگلیس، برای درمان ناباروری به ایران مراجعه کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/455335" target="_blank">📅 17:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455332">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fedab4855c.mp4?token=Q4nKnliThZhGyN55aQ5vgFzIfCKtIQe86BEZUNF7jysGYG_ZyDIY6Qn2Lnyw56nYRWb2RLFFWM5jFHVPrVlc6D80fXj6BoTR1bcMF3QT7BC9_l8ffyyuvl8FgKXEgSy4XHm24lxQkkqCEuF-1dAkTvq3PSe0-bFQw1fvMyfaI2LLgPaQfvGQ6XZ4ZdmgmUz9CNe_hyO41eWt9_PkcD53vPrRxnNEQecDBkQu9MaSiPrDRYQ3PnKUG5d9fMuOCGmGLciPq58YwcwwaYdROA4wXLm-cROaVoeLXsPD1UuMxh0sfLsOryJVeUCQsNsc9xinoZajzUvqlD7ATKzwJC0YvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fedab4855c.mp4?token=Q4nKnliThZhGyN55aQ5vgFzIfCKtIQe86BEZUNF7jysGYG_ZyDIY6Qn2Lnyw56nYRWb2RLFFWM5jFHVPrVlc6D80fXj6BoTR1bcMF3QT7BC9_l8ffyyuvl8FgKXEgSy4XHm24lxQkkqCEuF-1dAkTvq3PSe0-bFQw1fvMyfaI2LLgPaQfvGQ6XZ4ZdmgmUz9CNe_hyO41eWt9_PkcD53vPrRxnNEQecDBkQu9MaSiPrDRYQ3PnKUG5d9fMuOCGmGLciPq58YwcwwaYdROA4wXLm-cROaVoeLXsPD1UuMxh0sfLsOryJVeUCQsNsc9xinoZajzUvqlD7ATKzwJC0YvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سی‌ان‌ان: زلزلۀ ۷.۴ ریشتری غرب کلمبیا را لرزاند
@Farsna</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/455332" target="_blank">📅 16:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455325">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMA6NBWkiY8qaX5x8_wCxp31MrX3XYaClteceYUwDvumTHNclZ3BNRmrIlopi6P5CKB1zBK_BK8tEi8fAt3xjotGRuOwZilaWujwPQUXSXjopw3O-Ykg8Y_mLqoIt9GHr82mntfA-yFmiWfl6F8ijvf2sWxpDViPMK0IC5jDhnDkn0b3MysLJgm1OASJO4XZfEN5FvmlbToeDfd3ifryCuY3MYpBS_OCVISqjSAPWaWPg0fkFsrvN6NqZtpbKlUEYL6E548woP6H5TAnTZ-9U9bvxIKDSuawCb-sHe76kYV22R1dYIm0m9DcR8qKDM9WmHYNgFkLcix9bI7vh4QWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CkealDVSyT3EdGOyFtiQYVaTP4np9kxDwzSr7CcxQ-zZipVypbhQlyShY2IiC8hJw4YtK-aWAdcGOpONqgBM1ks0ExjdyTRc6nh40Jw_GhwKkDW_71KrTIqvM_uPFTKLUTd4p5A2T07qb1FMO90nTEMknZBn01vDGXnZcoRxfCh2JwmDYQFJXgqW9oajYkUpwZMhhWjLLl7-ztmTRaNRK7pWLUk80OcTLon7zRjDqMpvbPyepXcJR5KpDV9RzCnbiVkFz7OMwnqTvqLJH7FcaZwx5rtHOamQmP2lLfjQzIRa9DPli-MK9ekapp_7uXz27fJtoeXukIJqRmulq6mohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQtP993Yh5zOC1GxLxXHjT9I1pITeTfX8FcNPj7BLMx6FVLkfIQ01ljDFWTT9YWudR4tbhAOcvwJB-Q9Kk8Rm1MngAs-DDUS-u8sZlrvNch0jKXLYcPpoGfALxw9aYcdF0ydCJhFb82GwU8yia7pGymuqmW1cee514l2K3lKamZFaeufnGRHhxfnv14YyR4MQd5r_vKAt7ztKj4BDiNjiEkI0qmw3YlsHWNhgAkRWWrfdudKgOSlpap9bbxHAGXcOSr2kM_JnbSary4n5hJ1zL1Frz4l0xLwJAccVQ9ZucOTP-MpwY6BW_YFbIi6rDGTTr9QGVHnvwGtVMlizK9mag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBG0Q5cYpqaD5QoWMhFMV4MV8zJm7KYX07WWJfegjVMItjxcTpfedayETP8Pqd-Nnl-nI5rQe6-ZhNOMDIdci3ZTwmq7S0NBZ4j52Fil4_2923WPpphVY0JaTU_KmjrmK1YmYzu_1F9eZFPVBKtOhw0hrjIeFT5qmCTooATHFhit5VPSbKLxRajS1bHrxxiiwMEHd-OFk3K-vcG6oWZUHZa8rrt8EyainzND5FU6c7xgdG-RDkVFRrIQrgcAUoTgHDV62k7KvC7zu6xMCVNIad379dfMHupwSZLopk3SGkW7zaedRDfV_HrWj1giLpov-DeEk0r75zxq6WQ708yCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYFxxPlQM_9RTg5VrHmDiIz7vcNtKSTg9eoVcKe_oLFL8szZovdDWjzyf8dXFjzgctl4Nboh1MYVJK3AK6hTwNf8hvpMxTWlmhcaQUnCoxD2i3wguXwlT_dNb6WqhBnYEA7X6rgx_9pGqs6pQSAHky8DXrpJ7KE7fnDH2QwXEEOTSBNJnCwEOjMrI8Lafb9P5n3M_wcWP-eYnYRvhGSqwKU44Yuyn7GnOsOT81_TWSvXptNb_cpJ7xy03EslpTWJ4NmiXPKLvpDOcIKPwd76Wk7fuAp57rcBLe_Si3ZDzYzl1s8saJ9KNQDf2tmPx00iQmOl_lRIVGvbJEAz2IrFXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnjq3uDkoQhDWH2lcOUASI02LsGcH72Fbi0tQK_LcvQjJLl8KZtJTiuVOZoi2epNjJWXN0Q4fXYfradMUYLHYykeYHMlHbYS6KGPzSb-L5wDn-OEd-JimeQDKDaNYYwnYCgbWCuLf_fXAq4jE8_AH4O99i6T8bMMDXwROaEoiXxKoUcqqhGYIRHbqwLiO6vKk9n5uWgS9BibvXKqXwMTGSxaG4R7BjlrWFAkYimow6RCVFhITubmF_O1hDUqEvrR0lZe4kMmNC7XQd3lu7SofsgB5_lWPU8BJHaenbE1XoH_D8gjh2t5kX8fnqAWKUigZwXkCrfnO4KYZNhLYiVBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1dsH45kaxvIb5Yi4cBEQUEpg-nZLnEvLqsqzyDATBr-wJhumMhPKj4UMGPJCOR1cJ12hQMIKX6TZ-CNpmzjMQ5-y5OsccMAaJPP4_XNLk2rjBcQQrsYccXwzbCfpRwS6z1c-olEkJSSh4QLXFLR2aJ0hhKAy0xpJ26JT8v43exdPWSD5K_MHd113jmIfUBbaDXKKiN513qo4_K1g1opOGuMbpQYpgkZ6wVXAtzttYCsqrVIqMlUleJ5nwxjgr9TC2xx1sqKYKbBhdiGwsssm8gLBIg8fG9rm_0Y7akhk3YhU-xs1yQNnmGii7qEqZRtvt2cweZxM-ZN2kuQg6hIuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم تجلیل از خبرنگاران قزوین با حضور سخنگوی سپاه
عکس:
امیرمهدی زارعی
@Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/455325" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYAgdxWAAo60MKlLFeLG8Jk903RY3BfMUlnzYY8k5S0HYlL2wPMxWdLX_Lcqhm1woWFF_GCgkWCHkV10BYLuzs2tAZbQVPRO3szNSXOAAh3uhJc5EDBAKvzy2Y6UjCowdTFqL42sAent-QPVQ2_UiXqhwE_AG73aMmILa9Tx-WQqhq4lsU2MM3UWCfzvQBKVCmGdxZp0ALban36rseeqGXo3LaUFtDOqsrLhvVbDUKc6sO_adaoA64lg91qQUpedRAmMPJKixjo_z1qEIG4K9PIoWAJ9UVxqZ0bxsKeURGxbA-GaMtOmANhcoC1ImaHuA6_VXKkWbPERugbYnsnr_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باغ‌وحش غیرقانونی انزلی به آخر خط رسید
🔹
باغ‌وحش انزلی که بدون مجوز سازمان حفاظت محیط‌زیست ایجاد و شروع به کار کرده بود، طبق شنیده‌های خبرنگار فارس، امروز دوشنبه به دستور دادستانی پلمب شد.
🔹
زمان ساخت این باغ‌وحش مشخص نیست و مسئولان محیط‌زیست می‌گویند «تا چند ماه پیش هیچ گزارشی درباره این مجموعه وجود نداشت».
🔹
مسئول باغ‌وحش انزلی علی شرفی پیش‌تر در مدیریت باغ‌وحش صفادشت فعالیت داشت؛ مجموعه‌ای که به دلیل تخلفات متعدد، در سال ۱۴۰۳ تعطیل شد.
🔸
پس از تکمیل باغ‌وحش مسئولان مجموعه برای دریافت مجوز از سازمان محیط‌زیست اقدام کردند اما محیط‌زیست اعلام کرد برای این مجموعه مجوزی صادر نمی‌شود و نگهداری حیوانات در آن تخلف است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/455324" target="_blank">📅 16:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlYgwnZ7twaSYJ4iTkTkI_cjVLm-HmWVZk18OEfk6tTUsCa7A9-L1-iKYaA0PeunzkaXxiQLF83VxGyhZbTrdfWl1-FYeMPZau2271_7dpVq6rF6AB6xZH3OdIz2NWvmM4MEBktQg4sE_absGTHXm68qssxzUEpG8cJbYcvT5tVGaUb8ePaI59WTduQdkmowGwCdMwkvEO-JEiq5SqXfqAh1ZuxVMDzRQCHP7gFzWQr0H9aQ9xTuaXFwBe9ipB9skJ7Vx76h1DdLk82zCuz842fHA307SGXIxqpDm-Srgi8hKiFkzkWZwfujzxbfwXiHdu9B3tT1mJo7UC8hqLVa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور نظامی اسرائیل با پرچم باکو؛ حفره امنیتی کنوانسیون خزر
🔹
باتوجه به سابقه همکاری اطلاعاتی، نظامی و امنیتی برخی کشورهای همسایه شمالی ایران با اسرائیل و حملات این رژیم به کشورمان در پوشش مخفی این بازیگران، به نظر می‌رسد که تصویب کنوانسیون حقوقی دریای خزر، دست تل‌آویو را برای حضور نظامی باز گذاشته و کار ایران برای تقابل را دشوار می‌سازد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/455323" target="_blank">📅 16:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455322">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CV--mf_yF7dVQ3pp96emsXeR-5m9QvZGM6lxgtltUm23eiHUpJcPkftwiW4KF9NLwM2RJaFqrVE6S9wmTWC98X0miRYE34Q38ljC66fTokEosEruZX_eWoyGbbFhp8LwLheepE3JH48D3h6f3fQ9xBWw7n2eCMgqSly0v516tHMH8sVksnpJ4wRVt0wRSkMFhSderchdmquR6Fdx5gMFEWULYgiA9yzp1grERbsgr_2qQbN0b2WnGV5mARhQgW_rNMx_UUui2BUNxx-XAQTJBpTe0TU6ufj0EEwMeObB3daH4RxMcDG01utDBDst9XXTGPbGfiLB7isztCQ1HtZjNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیار و گوجه هم شناسنامه می‌گیرند
🔹
رئیس اتاق اصناف کشاورزی: «برای گلخانه‌ها و محصول‌شان شناسنامه صادر می‌شود.»
🔹
صاحبان گلخانه با مراجعه به سامانهٔ یکتا و تکمیل اطلاعات ابتدا برای گلخانه و سپس برای محصولشان شناسنامه می‌گیرند.
🔹
شناسنامه، فرایند تولید و سلامت آنها را از ابتدا تا رسیدن دست مصرف‌کننده را نشان می‌دهد؛ اگر مغایرتی با استانداردهای سلامت وجود داشته باشد مشخص می‌شود.
🔸
چند سال پیش روسیه و هند فلفل‌ها و کیوی‌های صادراتی را به ایران بازگرداند؛ مردم هم معترض بودند که اگر آن کشورها به سلامت میوه‌ها ایراد گرفته‌اند چرا در بازار داخلی فروخته می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/455322" target="_blank">📅 16:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455321">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657a35c5c0.mp4?token=qIO9hPQhoHmtNVjbvyYnQ0OmGeTHgM2WwjqY_5-ApdvQaSf8R_jlRqQI4eKfgQXdPpnS2MVDiYM5z0p72CCjwz-EBcM5QZ1Chvf-LuCZu_gnvYFLfhebexwKN1mw5x6fKDASeco2RUt3B2N74xSRf84ZZNxZha0PSx5Al4glV4hZQ9DAIqPbM8dHAvPM8vVQhQ6pzv7KcwH6Gx3wqIKOYpKav_aQL6qlEwFVhDfr4WbbErdJo-_ofm-xtRGyv6nZr2yPhxmYcSOrxbI6TgQI2QLLm2iezQeTw6BED4vOUVN5-uadefmXsZ9BUmJfu0NhvTlGdc52ToJqicx2NPJC9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657a35c5c0.mp4?token=qIO9hPQhoHmtNVjbvyYnQ0OmGeTHgM2WwjqY_5-ApdvQaSf8R_jlRqQI4eKfgQXdPpnS2MVDiYM5z0p72CCjwz-EBcM5QZ1Chvf-LuCZu_gnvYFLfhebexwKN1mw5x6fKDASeco2RUt3B2N74xSRf84ZZNxZha0PSx5Al4glV4hZQ9DAIqPbM8dHAvPM8vVQhQ6pzv7KcwH6Gx3wqIKOYpKav_aQL6qlEwFVhDfr4WbbErdJo-_ofm-xtRGyv6nZr2yPhxmYcSOrxbI6TgQI2QLLm2iezQeTw6BED4vOUVN5-uadefmXsZ9BUmJfu0NhvTlGdc52ToJqicx2NPJC9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقد هنرمندان به تبلیغ عجیب یک تاکسی اینترنتی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/455321" target="_blank">📅 16:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455320">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2571d3c962.mp4?token=mVlovMaYhHvQepvEFrr0LN6kIDq5BGs9D4KLnEUS0u4ji9VTtjjSp8SwbmX0iKyC75YHiimKb709JA9Y1Li0e-X7Z-xklAknOdj0oqYHLGv7Q36zDk9L8o3HaPZ49QcTt0CZyZer6PhAc-Yd5kPXpSOb5MCVY3OiS49mHwMFnYWtrxAwquPTAwVt_UgqW3zz46JrRN0XWPCwc-sJ0g_XnlE98Yza0de0qP43X1x3-Ckd9OWoqaBXwzKxzh1-qTX61Ivw40ztHNTBycs6jSb40VeL-yKEJ6UWAUwpAFtlOqE6eL7WqlYL5g3KzSaZb3XDEdbOq4rF2AvSPa_fGLKXlmD1_ZyiqEJLr6WxGCeVK2mzAL4H2t2GTm4GB2hJ0Edj9_kZ1DTJgJwm87DEjlbP1UM8wWR7QWfPwzmReGsPkRB1eePvJ4oERcq8Kx5iuOQKVnwzXny1KcoQ6eT0Nmy4_KjZVHF1uCZ48I-RFf_s3To9MWKKX5S55mwBOE45Ly-lk5GxZjuXNtfQKdoCAKkskU6SeYhpV2_zjjEzGKJjKvU8XRbIwhI5csh00zRWRglLnKW7pHa5oP_KJQ50CHi2MP73oGRlVc76U7G2nqE6hnMilv6UzFavG2g7_jieW_tjptJVomuE8EKENOE5kGkogATCOxjwUr7hV2zh6Mevr7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2571d3c962.mp4?token=mVlovMaYhHvQepvEFrr0LN6kIDq5BGs9D4KLnEUS0u4ji9VTtjjSp8SwbmX0iKyC75YHiimKb709JA9Y1Li0e-X7Z-xklAknOdj0oqYHLGv7Q36zDk9L8o3HaPZ49QcTt0CZyZer6PhAc-Yd5kPXpSOb5MCVY3OiS49mHwMFnYWtrxAwquPTAwVt_UgqW3zz46JrRN0XWPCwc-sJ0g_XnlE98Yza0de0qP43X1x3-Ckd9OWoqaBXwzKxzh1-qTX61Ivw40ztHNTBycs6jSb40VeL-yKEJ6UWAUwpAFtlOqE6eL7WqlYL5g3KzSaZb3XDEdbOq4rF2AvSPa_fGLKXlmD1_ZyiqEJLr6WxGCeVK2mzAL4H2t2GTm4GB2hJ0Edj9_kZ1DTJgJwm87DEjlbP1UM8wWR7QWfPwzmReGsPkRB1eePvJ4oERcq8Kx5iuOQKVnwzXny1KcoQ6eT0Nmy4_KjZVHF1uCZ48I-RFf_s3To9MWKKX5S55mwBOE45Ly-lk5GxZjuXNtfQKdoCAKkskU6SeYhpV2_zjjEzGKJjKvU8XRbIwhI5csh00zRWRglLnKW7pHa5oP_KJQ50CHi2MP73oGRlVc76U7G2nqE6hnMilv6UzFavG2g7_jieW_tjptJVomuE8EKENOE5kGkogATCOxjwUr7hV2zh6Mevr7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران تابستانی خیابان‌های یاسوج را زیر آب برد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/455320" target="_blank">📅 15:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455313">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDGc10XFQlSk8hs0J8wYpIesxBD-OMwZDY-EAz2Y4S5iUnNHTBpU27d71SDMnsM-uez5OF6_FXuemB6wEpkynUVgrdLBY7G5IJ9SQHSNiuELWMxlyRoZXGu9uTkVa8K5WzcVkrCxIFJK7-zrrTMcTrWlx4CjWYtO-a1koIjCVPiBtzPartxpt3FKEb_MAdRDPpuOE-Y-gaY63yMj5beTONrrLnlDmbjXpaZLsPXC7E_WrCibNuf5i32EKdnBqiaWaUdKCE4NBoV3gS7GqoknPA-88mvrHelkvEYNdIzFCKn6y7i7Bkgq-2OGk90_cdzTWr_v2Yf0ToZ29ZFVicudbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guXAQs0SwdkwLXNhFZntnx68bRMOPdDeij470i1jq4toa99CXpikBaxuFsWw4LwJgZ6Rlo5JHlJqVJmHBY_z9ZCNf8mftIGo0lvHFvBDVKvpue4NQcqPWHgI1EVKAEAMnrJlXY-D8uKVwTxc-l3NKRtfvjdGAMHqByfR8fybBA2vwBLDqxyEZo2F8CnsOAuC59CCbQVOlLP5ynjIF-7C2Kznr0StuxwbU30Mr2PaGqF6l2iJSF9XtcEkOawiyfRjbBbwvKUDGaSSjynr9ISNpQIMOX24MSQoAvsg5X65JJFNIN74HVDdABsTlopk07X1Nf8QLh9CtegD-VekH1zT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhAN54HdYD-HNKcNfWlHNw9qzJsP4tw8ffTbN9WNblrwqgRa1CowoaIJtEvHzlXxut4-vvk-p3wAyYJ2XtJ2d_jG24zeCc1jkAe1fgIeDZEFmXY-IzDvJiFRc2No0_VoDR1BkWHoIahWBKNf16J9D7Q8O75MpVBCV_BJovcIjghsMbsAPKkXzLJa6p7tjw2jlFpKlvYCdCS-muX_UpVcKLQFCgjR32BZDA1ukHzsEAo6ondn9CSdi7zGftQHTMUQy5COMPcVVdJ7LbBR5acglHMY0JNba7MUnRRw4NN7S9QMlLVcTky6DttFIjC1qHs-tt7MnXv_ZDSXZ_rS3qbt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tscpHlZpixeYhqXqvRESDe4ivwCBIy4vJNp3xk8hCpsVZsQQBbv6bjrSUkXNpOFSG90QeKyhWSzoxlROvrKiUtDzenWrUgWuCzzlO84ymttViwX1ARnc-2FR0u_lcSw0q4yP6GIHdSKO3-Bjx69EyDcgqaqDd5rhqs7ynv44f6BLPMVbB7zePUxAGJmgTnbZXfmexLlhJsxeIAHUUYI-ISZpqssY5AOian7D_WbTZUVnH6eBUDlsLECnnjWmJUMZwysQJbjnm7RJdfQVLXcH1UyXNXBq6dtRAPaOI0g7o1SP9H9heFinkTzi-hDQurKwv9FTS9ztmUoHSYFFuPHIKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THf1SftUhzXvrHzuucHiizIlXKqX6yv6PwuxJklLTO1N9e5kmyGMWHtyu_GY-ivtHTOum9MuGPF1PZ9JSRRgfCf53V1OTAVGbRUB0oP29S2HCVWSscXZfXlO1nV9Rv9CpeH76fASHYFOhqgRINmyHL9twps44fvYRlGu2A8PJ9JbwfShxiIz4fUixBrL9d3hPbDRWQT_DCARAw8GLVCSj5SUlJZpU817mGPRydlVDv5U-V00CxGYemGFZ9jipqCa_Jwu9kYnVaQeHl5d1eiwB3EkISrQl-vsquDatFzNA11zj6jOxSUMf_8XhfW6Xt252jCsiM0hO7Lyq7MJYecutw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntK5q2WOlFsPqVraMo3AKMkskoa-fNivn5j43r5AeFO38Ti9Eux7_8hPWH8JltcUd0jfB-qMCiJ89zviAGrhmVQaQWtNOZaXto8QQ6d1sQXIniZA4plYxmvg53dPVlQlofYUxcoIIq6R8eKWRM7GXlDsgMKR251hSUTcjqJU8WO7-OOg9a5XdDj3kfKGMFBjr6rmaXevp3EJ6w2aTlvUjj2DY7iR4qd_qb8Bp9WUKzeyA5CqufDQxY9eTlWIwvytsGqdDxg4vO_4_lN0UOkDFVeSdLLuxTflMVfReq-sLCL1LqA6_xb6I0KT3eZB1pdyV63g0y7WE5-eFDGqljLqLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Me44qhIEBHdshV6mLBDfpFVym5vRu6hLZ6AasDnlPBLgiPXIzro3bfW9cKV8DZNXP_zAvD--tEnck3k7L1eecXc8RSMhbidNwxiCglkLlKi1Sl3rBALo2AkDhd9gRSR2wWZ2zqAKpaorNw9UyNScYlURQ7BQRbXmnCLTziFBlLxBusyn82V7LDVNVyMereD64gpN16FsF59J4q1Z46jamdx09T1_vK9JQRSOsAU0hftsoVOgmmasZ-rK3L9g-Gfjb_DesBH9Gt6UkEsaxSP854uen5KwXaI76BUBU2iaIfC2yCuulTlXBxg8WjwP-tLlDqpigdhU8W8-nhOV8_Kpog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور
وزیر اقتصاد دولت سیزدهم در خبرگزاری فارس
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/455313" target="_blank">📅 15:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455312">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvPkxT3XjX48mKIeMF2hgTwhi0jCEkDTcuIJbOcs6Y2jARKD330V22Om_Qa4mUlCBCcMZEL5BzzMHdQlYaPp06Xj9s4lbu4Is-gp_5nvVlJhoheaUwI0ddQNmQ1WBKUo87Ffcf0HDga3riXT-Vo1FavgPvBPFAf9C1-HlsREmsR8iQWnb44J8GpdJiYNFdDsrGSdeUYkHBQsi7WxoRr7eTPcihcKrGnn0y2bz0JxH-LHSvc5d_2MnShRez_MsugYsRRdGtfK3gHIoBdixTlLgKdSB6z7oQlYhAh2XxizFhj9lybN1LAlolFktQn0WtT8qclHiDn94l7Eulc9GA3V1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پزشکیان: هیچ قدرتی نمی‌تواند مردم ما را وادار به تسلیم کند
🔹
مردم با حضور در میدان، تهدیدها را به فرصت تبدیل کردند و همۀ معادلات دشمن را با وحدت و همدلی شکست دادند.   @Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/455312" target="_blank">📅 15:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455311">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdLxo_pi7acTris0K4mk4wUc_EezeqnYVD9c9_mCrpFt6MQpFlj6xqKgllruLNoJP4hlJ3LB3nuLocwwI-kZ2xvehuZe3YpIHPBPPryybgzz3CcgdGs0QQayVBbAu13SP0xJRGJ7ue9MBDA_tBJpuICi3E-MCQCLngqXDDhGKEzOXAUbEeZQleZOdUqrVjQFSUR1KNR2_3Sb8rf4_01ZR3mY3fkIBYyyVy4bmKV1mjEs_bWN285GYF5BbeFCMIeqKPdLiTllWnQ8qJORe4Buc4TV0nPPNqQpW8HcloqhhVY6wEeAXQZOEDFZOSZXAd8Q4LBxgO-xNwIEGuuwq0VztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: موشک‌های ایران قابلیت‌ تغییر مسیر دارند
🔹
موشک‌های ما قابلیت هدایت دارند و حتی برخی موشک‌ها می‌توانند در برابر سامانه‌های پدافندی دشمن تغییر مسیر دهند.
🔹
حتی اگر برای موشکی یک هدف مشخص شده باشد، می‌توانیم آن هدف را در میانۀ مسیر تغییر دهیم و هدف…</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/455311" target="_blank">📅 15:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455310">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/192af346a6.mp4?token=QQNv_pLQXj08O2sfshRiqMzi5iKNYIxTDeJQsAFlt2r3H06rOrg99QcuNVhg_MP10VVwlaCk6zMB2zZ8RrnAy0LR2rRaJdtmXFWCThSO-j9mNhqKNX8A8DNg4WkUVvl6hwtr7dQx-haaTy4fSDpe33wEw1aG2P4_joSF6dWgBUJhoTMS64i6Z61h_TxTtNKIeWgpDpgzzg-cBB4I-WUUrrLRDxOFuwrU6x1WXMSWQZ1hCEV0fu2Utzzw8PZKmjl7Q9t_xTAId8loqyyhAl5cO-DYuoSXRvpm3-Cjem857IXHFc6f9-uYIPGFk3IDBVnrPQHAaAxwULcdm_QC7TIDjQZo89bHNSkViB8fdbk9MAVGII7riKk-XVZgOoX9TwAEEGjraVW_mTM4HkLGTDA27BCapFTEyMI0LmjWuj2XCqVYX_xaue0iOx9zDY_VFwFESXxZgoiLABR9U0IIYHB9Tv_z9wkFDfSzHpqA7nT94ipjEfsc8H9oFo-7dTDbOchZqDLvy8gKxohufteeDLe43xam1WJcwewl2Q-Bnjkj05EWzAXM7HkxFXESSMHFUHd58jKCvSmxhd0yfvZCUUyvaxpUnoX1px3tf7GHt2FCu24vUh4vwvCUeNFXcWlR_TOOeGr2Z34wWpDRxtagblVbZ9TMUW1In66Ric-kCyxhMec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/192af346a6.mp4?token=QQNv_pLQXj08O2sfshRiqMzi5iKNYIxTDeJQsAFlt2r3H06rOrg99QcuNVhg_MP10VVwlaCk6zMB2zZ8RrnAy0LR2rRaJdtmXFWCThSO-j9mNhqKNX8A8DNg4WkUVvl6hwtr7dQx-haaTy4fSDpe33wEw1aG2P4_joSF6dWgBUJhoTMS64i6Z61h_TxTtNKIeWgpDpgzzg-cBB4I-WUUrrLRDxOFuwrU6x1WXMSWQZ1hCEV0fu2Utzzw8PZKmjl7Q9t_xTAId8loqyyhAl5cO-DYuoSXRvpm3-Cjem857IXHFc6f9-uYIPGFk3IDBVnrPQHAaAxwULcdm_QC7TIDjQZo89bHNSkViB8fdbk9MAVGII7riKk-XVZgOoX9TwAEEGjraVW_mTM4HkLGTDA27BCapFTEyMI0LmjWuj2XCqVYX_xaue0iOx9zDY_VFwFESXxZgoiLABR9U0IIYHB9Tv_z9wkFDfSzHpqA7nT94ipjEfsc8H9oFo-7dTDbOchZqDLvy8gKxohufteeDLe43xam1WJcwewl2Q-Bnjkj05EWzAXM7HkxFXESSMHFUHd58jKCvSmxhd0yfvZCUUyvaxpUnoX1px3tf7GHt2FCu24vUh4vwvCUeNFXcWlR_TOOeGr2Z34wWpDRxtagblVbZ9TMUW1In66Ric-kCyxhMec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس‌جمهور از دیدار ۷ ساعته با رهبر معظم انقلاب
🔹
پزشکیان: رهبر انقلاب بر حفظ وحدت و انسجام ملی و توجه به معیشت مردم تاکید داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/455310" target="_blank">📅 15:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455309">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌ دادسرای جنایی: پیکر حمیدرضا رجب‌زاده اطراف تهران کشف شد
🔹
براساس اعلام دادسرای جنایی در پی قتل فجیع حمیدرضا رجب‌زاده و دردسترس‌نبودن پیکر او، سرانجام با دستور قضایی و اقدامات جنایی پیکر وی ساعتی پیش در اطراف تهران پیدا شد.
🔹
با حضور بازپرس جنایی و تیم تشخیص…</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/455309" target="_blank">📅 15:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455308">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f435611b7.mp4?token=b5G1EGYSeqDGATmjVLY_khCcd9chHJreEugy67imCYw86O1SRkWcgDOaoMOl-8Mi55Ru4dHjkUmYHG3qin231xYtzl5FRUy0AvG2quVs1hll0d_pk40khmDEUC9beSUscukvGqHzmww1fLFHhe7wxigxKgivVVmrMpqyjb6taXZS-eoOgwuz87ggDV6YenXzOamsNHmZzOd2UNIYc3cJQe2Vjx3-HMDg_BljQr433sA11xE1QX9WuvraSf9_L20crSTnzeoJvg_MAbh2ahtzaDcmDcvyd-ud96dIfe5A5k8YpIzv0vusrYzoSDbMhd3ZkYY5jE1EoNnempwWixV21A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f435611b7.mp4?token=b5G1EGYSeqDGATmjVLY_khCcd9chHJreEugy67imCYw86O1SRkWcgDOaoMOl-8Mi55Ru4dHjkUmYHG3qin231xYtzl5FRUy0AvG2quVs1hll0d_pk40khmDEUC9beSUscukvGqHzmww1fLFHhe7wxigxKgivVVmrMpqyjb6taXZS-eoOgwuz87ggDV6YenXzOamsNHmZzOd2UNIYc3cJQe2Vjx3-HMDg_BljQr433sA11xE1QX9WuvraSf9_L20crSTnzeoJvg_MAbh2ahtzaDcmDcvyd-ud96dIfe5A5k8YpIzv0vusrYzoSDbMhd3ZkYY5jE1EoNnempwWixV21A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید سپهبد موسوی: هرچه تنبیه شدم، به‌خاطر خنده‌هایم بود!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/455308" target="_blank">📅 15:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455307">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_-pGH7fuT3Wd8FGl0bQGrVzxvFnTJW1Hj5xckOV7A00ivQOhgTbCFHlp9t8jKHHUibKAHUA1bY9TsoILD6Il4LFrvslylLq75Ja9OUHaUDHnksXN86BNlB5Y_jElgarDl5W_tnQac4ZLapZcd_9988HKeujS6lNOL6CXTsTf8S8YiqRu-gYIww5YllaS3rXeTjECQhJlCm51Xn3a4en9TiRTlHfZGCkbw0CWBPPBDjZ5l0Z542IkhFLod8ph0Pej9rbUGOad0m1OaO8LLvaBZTlwJgYgO1mPCR1Qy3J0PJ0GEyiXR0JFSbtPeofqu_G2napR3q9oPOryvsdbniLbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: موشک‌های ایران قابلیت‌ تغییر مسیر دارند
🔹
موشک‌های ما قابلیت هدایت دارند و حتی برخی موشک‌ها می‌توانند در برابر سامانه‌های پدافندی دشمن تغییر مسیر دهند.
🔹
حتی اگر برای موشکی یک هدف مشخص شده باشد، می‌توانیم آن هدف را در میانۀ مسیر تغییر دهیم و هدف ثانویه‌ای برای آن تعیین کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/455307" target="_blank">📅 15:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455306">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‌ فرمانده کل ارتش انتصاب محسن رضایی را تبریک گفت
🔹
بی‌تردید، این انتخاب شایسته، بیانگر اعتماد و اطمینان به تجربه، دانش، تعهد، درایت و توانمندی‌های ارزشمند جنابعالی در عرصه‌های راهبردی و امنیت ملی کشور، طی سالیان متمادی خدمت صادقانه در نظام مقدس جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/455306" target="_blank">📅 15:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455305">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDNc-SClcbz8o-jwBVMpgbQGpEhFDoCOF1O-7RH_-GRNrIb4CJOoFHigkpLMFLhWCH0BDcXFaUR-6XBIP7l20QhCI6_SomoCu-qcq6j-odwMV_tjY_wX1NLEbz0ypHhQgicp3cFUKTxrdsc9d-Fugn9ywHdJawkFg9xbpViqO2Df0HUmBxSKGIxGdGNAQJRbJJkk-4zoReCa6U1wNoGj1uyKXNl_VgiTtVq3HUraHIbEEzwuJ6XwQlaAqGSgh40qMs5iIVIkndEYPmA_nOlyGEqaI0kNEjWw2dpTTW18_1ks_gZ0Z2Zcv0CBjhh_wH-0DGAyZXPxoncm-OrBayrpeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فتاح» انتصاب «محسن رضایی» را به عنوان دبیر شعام تبریک گفت
🔹
در پی انتصاب سرلشکر پاسدار؛ محسن رضایی به عنوان نماینده رهبر معظم انقلاب و دبیر شورای‌عالی امنیت ملّى، سيّد پرویز فتاح رئیس ستاد اجرایی فرمان امام با صدور پیامی انتصاب وی را تبریک گفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/455305" target="_blank">📅 15:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455304">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRFauPEDYnXIGc4SciltWS-eJerkkN4E91h7sEpnYFl4KncXtnn77-rHwLdurJjzU-mOTl2k5r08sy6b5PYT4QzNHEIF6Qke0f8Aq_zOMH28YmZuhP2YiTyy0-qo-DZuAkdlpLfL2P6gM8zsqo46N0ecnQwQgJCtt3BASIwOouXxda-Gj-MdX4A-Kq0fUr1IMHKEBMVL8g7IiWkL-3IYhm58IAjilpJtlB_Ee0xw088GbopSq5DGPcXTs-nqGqx9VIRXROAiiqllH99yRb2O1YZMc0zGcyA4HGCLRLzoUE3j5wBzp7E-EN1icXOxqSAMoiPp2PUu_UrOyRbIRjIdUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسب رتبه نخست سازمان منطقه آزاد ارس در حوزه عمرانی و زیربنایی بین مناطق آزاد کشور</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/455304" target="_blank">📅 15:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455303">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/455303" target="_blank">📅 15:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455302">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات در سیریک
🔹
فرمانداری سیریک: انفجار کنترل‌شدهٔ مهمات عمل‌نکردهٔ دشمن امروز در بندرکوهستک انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/455302" target="_blank">📅 14:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455301">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec49f80d3b.mp4?token=JE7S0vIS8ME2kt9dVwmbsq3LuMqAkY1CRtEOx9NQ3wA2GNQcoAFbQEHGxDTjCXbhd5hhqf1q6C0k8w5zv0ZmwUM1H45gehii38V4fg-74rDE6cOgXV5XvdY8oQut1-0xmDLSnpspEuE9_8V9ftlWtXAOoRS1egDXbvIsZBx_01PAYwhWgOPQ3h9ONcWRn4JV0DyalCZ3maSn64YPxv-W9TpvCWLj6_va1yVRRoUD9XMUocetH9hc7R29RThFC7Jp7tPYk5fBiLQwyezBv87P7cNKvXM-BcqoxNdTwNMCVTVGiJq03kkayxB-fM6KF1bdxGHx9NxkCbtBqHyPYt75Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec49f80d3b.mp4?token=JE7S0vIS8ME2kt9dVwmbsq3LuMqAkY1CRtEOx9NQ3wA2GNQcoAFbQEHGxDTjCXbhd5hhqf1q6C0k8w5zv0ZmwUM1H45gehii38V4fg-74rDE6cOgXV5XvdY8oQut1-0xmDLSnpspEuE9_8V9ftlWtXAOoRS1egDXbvIsZBx_01PAYwhWgOPQ3h9ONcWRn4JV0DyalCZ3maSn64YPxv-W9TpvCWLj6_va1yVRRoUD9XMUocetH9hc7R29RThFC7Jp7tPYk5fBiLQwyezBv87P7cNKvXM-BcqoxNdTwNMCVTVGiJq03kkayxB-fM6KF1bdxGHx9NxkCbtBqHyPYt75Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری پزشک قلابی عمل‌های زیبایی در شهریار تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/455301" target="_blank">📅 14:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUeFgLZ8ZIwFyGX_7qh2P_Bje5rDd9WU_6-4YPpxlBf8t2VfmT0b_JstPK8c7JBhUm76iR_5fiO8C915LI1BQVQOZxH8AaKLVB2brBkZnbZyxg7esTU8V44GedTFkJUa5S0jM2w6lGYK-FAR1H7fihIewY3An3-TAQ5Uk-s0bCcxGlPczVA3scjtpBYghEG5O6CGtaOdxnJobowPTv1NlpBikti7seJ38qVGfCDLBtcIyXGxnTsdDM9HS32AUhtYDXpIlhXUD7w2ah25nNZJHZvBtnYcFz5UwFL_-0uaP7Lg2cDXIu3mMfLWU_PV6WOixrKo8k_f--QJ1_BD19cehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلی بازارهای میوه ‌و تره‌بار تهران در چهارشنبه
🔹
سازمان میادین میوه و تره‌بار: تمامی میادین و بازارهای میوه و تره‌بار شهرداری تهران در روز چهارشنبه همزمان با شهادت رسول اکرم(ص) و شهادت امام حسن مجتبی (ع) تعطیل و در روز پنجشنبه همزمان با شهادت امام رضا(ع) تا ساعت ۱۳ فعال هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/455300" target="_blank">📅 14:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455299">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f43b18398.mp4?token=iODdQSavrVEWJK9Gd64kPJYb1aePndQsjec9jR2Ddek7KZdDeTxD5xmOahtLrjladAPz-M_G6g4auxpSGle_-kEccB_aGkjoneWWZaUMRCIdR7bwqCZY2fzSAdwTGi7GRCnDUvyO-y2gE2qg4UmNAhT0PE7gKyWcWzjtsIzvLrDBNqCXViPe_gkkUGyt161A_FL14M2_2hJ3NfV1O1MiFTzAmCz5ohOJsQJTQlo2xTGuUkW03IqUxHnzMSn1dSOZEtrD6f516F8xaNVCoLT49k3LLGKeVdTPv6J4XnUuX_tm4Qb9PhrLjT56ZcmryHG5i0AeotvHrmZ39MtFksQ0nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f43b18398.mp4?token=iODdQSavrVEWJK9Gd64kPJYb1aePndQsjec9jR2Ddek7KZdDeTxD5xmOahtLrjladAPz-M_G6g4auxpSGle_-kEccB_aGkjoneWWZaUMRCIdR7bwqCZY2fzSAdwTGi7GRCnDUvyO-y2gE2qg4UmNAhT0PE7gKyWcWzjtsIzvLrDBNqCXViPe_gkkUGyt161A_FL14M2_2hJ3NfV1O1MiFTzAmCz5ohOJsQJTQlo2xTGuUkW03IqUxHnzMSn1dSOZEtrD6f516F8xaNVCoLT49k3LLGKeVdTPv6J4XnUuX_tm4Qb9PhrLjT56ZcmryHG5i0AeotvHrmZ39MtFksQ0nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هیچ قدرتی نمی‌تواند مردم ما را وادار به تسلیم کند
🔹
مردم با حضور در میدان، تهدیدها را به فرصت تبدیل کردند و همۀ معادلات دشمن را با وحدت و همدلی شکست دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/455299" target="_blank">📅 14:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حملات سایبری پیشرفته به امارات
🔹
شورای امنیت سایبری امارات از «حملات پیشرفته و سازمان‌یافته» به بخش‌های هواپیمایی، انرژی و آموزش این کشور خبر داد.
🔹
این شورا اعلام کرد که حملات شامل مسیرها و شیوه‌های هجومی متعددی بوده که تلاش برای نفوذ به سامانه‌ها و زیرساخت‌های دیجیتال، هدف‌قراردادن حساب‌ها و داده‌های عملیاتی و همچنین کارزارهای فیشینگ (Phishing) هدفمند و تلاش برای بهره‌برداری از کاربران به عنوان نقطه ورود به محیط‌های هدف را در بر می‌گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/455298" target="_blank">📅 14:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b7113c7d9.mp4?token=AFFvp2XXC8E8xPD1B-gcPheaz58cPINEQu2-CpVGpe-24h8fUlebJ3425W-lesyCmD62xDHlzMN72PAihqs0cxgayc3O1YYwzBkRT51QVz-zr_rNWXe0fOqtvANP70WMan6blbvu8wQtGu2QeYBAYXFZiRIq-ODayJC1_IZVm5yrotFOgDtOCcmWIdakFFebOYbimwPmaNQUtIBGbsRonYVZtf02cwfqpIFvyrTR3cKOy8O9GahlzHvQaGKaiFKk28nOK5o_ecI9SkZnsxs1qO0w0iC_Y0i2n0KDPNZjd8A0XbHfvsE-T9suBlimidSLS5tlXJvjktpG6Go9PWazJT8bbr1VBPE4vkeQ5y-MQ55Mx8j0jHKx3w6sV5SrA9VFzhxoGUZFJCndnEfqZDzPWUIgTCmzKNdciWcszA0WE3qOwTfNm-eVreDTSLkr6fkpGD9E9DSZyoOb6pBTUEidEwZUp0gbrvW_BO8tHgt7-eUUGa02HA9V4qkyxl-lErZ_b3j86unxTeOUtt40LVZA9QNh-ugNSf1wYsb_9WO-XlOUpAbjYOorPrxbnwBvkCr04c9VgsbRf-7mkkINEl8jg-B4Iewh1Nq4j0GfD2SpijuzVItXxCal_rTIPmJ-uBb8PWwXNkMGuBEekmv-8VwZGzGVDpxVW0PoPPRF31N9H0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b7113c7d9.mp4?token=AFFvp2XXC8E8xPD1B-gcPheaz58cPINEQu2-CpVGpe-24h8fUlebJ3425W-lesyCmD62xDHlzMN72PAihqs0cxgayc3O1YYwzBkRT51QVz-zr_rNWXe0fOqtvANP70WMan6blbvu8wQtGu2QeYBAYXFZiRIq-ODayJC1_IZVm5yrotFOgDtOCcmWIdakFFebOYbimwPmaNQUtIBGbsRonYVZtf02cwfqpIFvyrTR3cKOy8O9GahlzHvQaGKaiFKk28nOK5o_ecI9SkZnsxs1qO0w0iC_Y0i2n0KDPNZjd8A0XbHfvsE-T9suBlimidSLS5tlXJvjktpG6Go9PWazJT8bbr1VBPE4vkeQ5y-MQ55Mx8j0jHKx3w6sV5SrA9VFzhxoGUZFJCndnEfqZDzPWUIgTCmzKNdciWcszA0WE3qOwTfNm-eVreDTSLkr6fkpGD9E9DSZyoOb6pBTUEidEwZUp0gbrvW_BO8tHgt7-eUUGa02HA9V4qkyxl-lErZ_b3j86unxTeOUtt40LVZA9QNh-ugNSf1wYsb_9WO-XlOUpAbjYOorPrxbnwBvkCr04c9VgsbRf-7mkkINEl8jg-B4Iewh1Nq4j0GfD2SpijuzVItXxCal_rTIPmJ-uBb8PWwXNkMGuBEekmv-8VwZGzGVDpxVW0PoPPRF31N9H0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا فشار خون باعث سردرد می‌شود؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/455297" target="_blank">📅 14:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qke7M1o3Jxdo1aJC8f9qrVi_CehKWwGJ5pOcK78JLUEzbzkdU8cggNgIwbCj24tPLrm0N9iis3hXzpApqZMXdR4oU7jRTvlzP9wijgDuVNR4_f0TKVtjA9hfgdHDwagU2mwXW99gOIXyH5rP8IS49BIBQuA3avZYMQs6fFRmwvo9LXNrYiclYUW38zqa9vklkPfBRZX1ofnn19TmiPETRyxye2iSOTueVCiOBbQh8-SE8EcrG3htLX8UNTmfa_BZg8D2TgNsJZj2LLnMXthtxzodKSeqmMlvB2IhipSEPbK0Huc63vuo0H5uljCmlci0VO4ykXXKyIbA2TF1kBYkOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعزام نخستین محمولهٔ ریلی قیر از قم به ترکیه و کشورهای آفریقایی
🔹
راه‌آهن قم: برای نخستین‌بار یک محمولهٔ ۵۳۵ تنی قیر از قم با هدف صادرات به ترکیه و کشورهای آفریقایی جذب و پس‌از انجام امور گمرکی در قم، از طریق ریل اعزام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/455296" target="_blank">📅 14:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فروش متری خانه در تهران آغاز شد
🔹
مدیرعامل سازمان سرمایه‌گذاری شهر تهران: عرضهٔ آزمایشی خانه‌ریز در تهران آغاز شده و از این ماه کار به‌صورت گسترده از طریق سامانۀ شهرزاد شروع می‌شود.
🔹
قیمت خانه‌ریز معادل میانگین کل آن ملک است و افراد می‌توانند از چند متر…</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/455295" target="_blank">📅 13:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455294">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انهدام مهمات عمل‌نکردهٔ دشمن در پاکدشت
🔹
سپاه استان تهران: درپی انهدام مهمات عمل‌نکرده در پاکدشت تا ساعت ۱۶ امروز، احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/455294" target="_blank">📅 13:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455293">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اتوبوس‌های منتهی به حرم رضوی ۲ روز رایگان شد
🔹
مدیرعامل اتوبوس‌رانی مشهد: خطوط منتهی به حرم امام رضا(ع) در روزهای چهارشنبه و پنجشنبه، هم‌زمان با سالروز شهادت پیامبر اکرم(ص)، شهادت امام حسن مجتبی(ع) و شهادت امام رضا(ع)، رایگان خواهد بود.
🔹
خطوط ۸۰۱، ۸۰۲، ۸۳۱،…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/455293" target="_blank">📅 13:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455292">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎥
شکستن دوباره ظرف توسط شرکت‌کننده زن در «سرآشپز»/ یک لحظه سهل‌انگاری، کار را به خراب شدن غذا کشاند
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/455292" target="_blank">📅 13:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455291">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgFa0fcyBhw_gZomh7hu-ObvAW4YjyQvE3Qt7kv69MwbWokDwt3sDdgpCy20kHVPVeFcCb6h4ZjZmVcaYe2B7_WC1gmGvDVtcUyLhe8fyeDG0h7IGh381Zu7dbXKaTTLbE9cBu9Gc93nGZ0ApcAAPlHWbVNVuKjJv1xNuvbEp0u9uaqDJAd84qu7xGpDUFFko5VxJ6AQCy1tUHtL3KJfAKRe-UWrjihMWEMJuye7GAYEZFg3kYRi0fjcCXyTbmviLba7OD6ozBmX0oKP_L6eYglcPohoBAsUIUnB9L5AD7PMvrehdQM1bK5xTbnfsKgS2UretaocQWVeYxXk6zwRjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تأکید مدیرعامل پارس‌خودرو بر تسریع تکمیل‌کاری و تحویل
خودروها به مشتریان
مدیرعامل پارس‌خودرو با حضور در خطوط تولید این شرکت در ایام تعطیلات تابستانی، از نزدیک به بررسی جزئیات روند فعالیت و تکمیل کاری خودروها پرداخت.
بهمن حسین‌زاده در جریان این بازدید، با تأکید بر ضرورت استمرار و شتاب‌بخشی به فرآیند تولید و تکمیل کاری خودروها، خواستار تسریع در آماده‌سازی و تحویل خودروهای تکمیل‌شده به مشتریان شد و بر ضرورت برنامه‌ریزی دقیق واحدهای مختلف برای کاهش زمان انتظار مشتریان تأکید کرد.
حسین‌زاده تسهیل روند تأمین پایدار قطعات مورد نیاز پارس خودرو توسط شرکت تامین کننده قطعات در گروه را یکی از الزامات اصلی افزایش سرعت تکمیل خودروها دانست و تصریح کرد که هماهنگی بیشتر میان مجموعه‌های مرتبط، می‌تواند ضمن جلوگیری از توقف یا کندی فرآیند تکمیل کاری، زمینه تحویل سریع‌تر خودروها و جلب رضایت مشتریان را فراهم کند.
مشروح خبر</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/455291" target="_blank">📅 13:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/455290" target="_blank">📅 13:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455283">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JV92T2eQuXXNloQIJmxVL_NsYaxu_KdZl8RFcVEhq-KMeNxCIAHrLeVMGPX1_o9gEdF_jRmpYwt_i5lc7AltPA5DZC7R8VxtEPK_wNIOxhUL6tiDBQOWA_3nJUlnlHJO9ir4H-_bjc0o7DgY8JC4Wvbm1qJ-4sB_tJtTKQJRmQYB-hX2gQeApAv3vMiuR30WhKTTF3rMPKktCKatvJdmVia6BAJ217bpMUZYqyFAfRL_dHvp1kNeRsSiKpU-NwwlwYFGcC7DERVvb6N3yw_uQEwAtulUcUSA1c1oSy0D83Hkhn6BxHcCVp3ucHKovklU7a67Ic1VLdjIl2zJ8WC_OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgpeU6rOCdAjFlhLvjJ2th_2kh5a2pDbkoU7OCfHOdRJgLYNX5Ne1BFGNwiMWTAMATNT2hRc3wUSkX3FVl7Z5rwpdej3dSajsoqXCuDjKyVw0Pd4x7FJRzyOgfyOR-KVzqMz3wSSy7kAthQ5A5onaiQok3DhKWJEocKUojdFVsHxymUP9bNNtElcfb7PEx5QoRBH3Z40CJKlkeoWKhUWIy7X37O_OZmhtQkcbPVd5ok7k9xw8YVUh4O3sV1yp2OzNnaDXOvl13DncEQ8dehDBEKHpiV8UchZ2BYzCHqELXMpdE6jT8TTt_Xfs10mbGDT4YyoL1u4_mA9mn4ymBW4Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uF7qpPG66imAMSdWUmtnwzuyW0u-kLOVbwTPGz_fV6_mAnePgjJwSCCwEMoawuX5bRp5KLP4Y-SJNhouGiDe6xWNA2BtqRPvMhRbjgKEnRfSWqnLVeEcUDEpFchfEKiwZSSK4U-vwjqOu2ih-U00-dagseSUYIeQppqrtp0yLcWiK-VGkd5iZ32tG-CF0J_nPad0FwYWOAkZce3Ggav2BZB8-Po1Az2Lya0Q-g3fRKMR2WqkhxPnAjjxQ7aJqcplWQc8AW4LettNKKcMwzuzw_kNMTkkTZ46qGXTnfCrRDd0htQt39NVcOQWonG0MxWQyteYm77FWhGfqLs2CrPlQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xs0rdoL58fAu6HxmVmJWlfbe8gvRxPmNM9PI48ePJGwK_GN8scnHBE7KhcVyPOGl_aVdtjaSjcyaXu2gus99cBX3y4TZLDWDbiT-Hdu-FCspxqOEONZAItyyyCS7IsEIoyQbgWMwUxpUWPYPrEgpKMMnHhY93F5X5iEmR6LqRm5LsT3vBvGwEiFp-VIuXP2GKQCzYijPd8C6OqWySZx3hxw_gdncYB8ycbJdOUmKfnX02URnBYsxYOSDa4-O6Iy9btXJU0HfeJjU2tJIiKny9o1bpJUrPu9Ww5tFYDjNZZUalSHfNm33farKR_eNwsDtyehSPMxl6puocVWwJ9F8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jI_tpBOISOsR7NLz7xCE_G48gAx0loMzwI6CPCw97xuAEL1TUxlXqULrn0_yqebD7-AzAT8FeTzjE1ltV0e7jmCSFXANrZw4O3rshkNY-_92I-aaL6RFAGWAf1jeaLHG13E6wNA0Dewcy_qJZPgyYk_RCVEQAit7W1QVduZtNP_s576afGKNfNi-XKbA8aZOXLWKugesJXZB8J_lrZcKrJfoSNO8VmVJ1a4D441eZcKfow9ecBDQ7ixi2711gYRFGT8rxfML19NTaFdp8jGntkRkDn-20Udz0nEyAtU5i7eu7Op2tlUSZJsSh6_XxoHZNeq6ZEEl4ci9g4gEoIEm0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PIznW7OG6gNPIUefBHKlpx6tz_f8JyyZnD8BQ4jp2W-MYndpeIJIsCJnurTF43gT4bJwB9eKX1aSz7et5CHSahn8ALsfTdwJaiDUaVSYUY_ukiGrS4dM49Zx2P0e4ONBXvgWOs1ik-ErrRwVshiCOxuE2K-ULb3t1IbfQWti6wlyDu8wZfir_TrH3rDqcSSzvOaHnPUuhY-jj_UbvBPKkuWEWxO3hmG3NlkhaiiJdymmt1fKpZ9Cj9xvINFSbNQdeyYHYiByK7jCTLYEjPCi2jdgMm--clUJYsXbOhuB-UQX37_b5vVa-9o85XUo184DnCX-cvwLNprQmHj15wb2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dw5Zk8X1bT0HvNy1bfUXP5LBl6ZvYxUthQG2l6LPCw9EqvkeSRo0NneUjuOcJDL8FqyDGEz7F8yJXRoOnlDq5YenDr3xCr0WipchoLodbakUbJBGJSurVmhqfZm33qxSynj67Ao0-fBnxlw1oesFO6D1ZEtUDvMGVhxIW8FnsY43N94rOQjHaTM_jKA0gBJmT-mbxf1EISd_cK-2xs514viGCOgDl8C_YFFR1FZJ907-77_6MQo9OzMBCiPLW9F-75Yz2wz4C0jRkdPdIiq-iElqZ9dRPxwuounMKibSagPzjch6AzIlMBdzq1TZRogpbnImPIto6pF6_lEas9pRtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: پاکستان از قالیباف و عراقچی برای سفر به اسلام‌آباد دعوت کرده و این سفر در زمان مناسب انجام خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/455283" target="_blank">📅 13:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455282">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d37c01a31.mp4?token=mw3iyQsR8oDaeezKSGOeKInXRJT8fb-22iYOh1dXXXKzl6Yf3B4G7BsFcwdN-tWFdwvuLRN3przSgLYbqnEph1wMwba7m1BRkGF4rc3lB9N5lV0YWpHQdun1BQC4KRV3Zg-iWuPMY4JthIcJmr5zpZNJuUGEOX0WNlZT3gOb-LWsGjvYUuxi7MEjKcb0s3OfM77wZXwOmxokq6KGJPz0jPwogllXImb8DaWRRoOojzlB1cO0_-iG326DPlbGPahVn9Z33RWBonZQEplgKewB5Qz__L222k2nuwzgaooTxM5F3Jt19bomkV1T_U3b1Hdp-gP9Gp_XkqMXOnO1ABm1eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d37c01a31.mp4?token=mw3iyQsR8oDaeezKSGOeKInXRJT8fb-22iYOh1dXXXKzl6Yf3B4G7BsFcwdN-tWFdwvuLRN3przSgLYbqnEph1wMwba7m1BRkGF4rc3lB9N5lV0YWpHQdun1BQC4KRV3Zg-iWuPMY4JthIcJmr5zpZNJuUGEOX0WNlZT3gOb-LWsGjvYUuxi7MEjKcb0s3OfM77wZXwOmxokq6KGJPz0jPwogllXImb8DaWRRoOojzlB1cO0_-iG326DPlbGPahVn9Z33RWBonZQEplgKewB5Qz__L222k2nuwzgaooTxM5F3Jt19bomkV1T_U3b1Hdp-gP9Gp_XkqMXOnO1ABm1eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سازمان اطلاعات نظامی اوکراین: ۲ لانچر اس-۴۰۰ روسیه را منهدم کردیم
🔹
سازمان اطلاعات نظامی اوکراین اعلام کرد که در عملیات پهپادی در منطقهٔ کریمه، ۲ لانچر اس-۴۰۰ روسیه و یک آنتن کنترل پهپادهای روسیه منهدم شدند.
🔹
به روایت مقام‌های اوکراینی، در این حملات از شهپادهای «ماگورا» (Magura) برای حمل پهپادهای عامل حمله به لانچرهای روسی استفاده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/455282" target="_blank">📅 13:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455281">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOWNvIMgWBsuzyxPxGn8NcTX5MfVqGTVUSPXHaeusPZ46yV6rpG9eYEEu08JxBHAIZYqAkJVFiY1LrjAfNzjHHGxx9-DtQ0n7VA5n4-WDLQm5c6XXbp2XYUC4xRor6Vp_3Ph0lVhZGx2CwTMAREWNq2s_lQP5SrgMGCPnAZvI60rZyiTHB3qdFaEYuOMs5xzjsjVKbx940P8XNQ5BeKJDSSTl4gIp3vhP8MvF9l05a8qitQ6EJ7avPwLJ37JKSd630oBI6DmJ4DF8AesGE4D6VRBol0GF4f3p0ts-56ykD1dmDuqse3CTJVizcSDEU4o01rTjuk56Y4tG2LNpZQesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی به لیگ ازبکستان رفت
✔️
مرتضی پورعلی‌گنجی مدافع ۳۴ ساله پرسپولیس به پاختاکور ازبکستان پیوست.
@Sportfars</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/455281" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455280">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎥
بدهی مجموعۀ آزادی برای کشتی دردسرساز شد
🔹
بدهی مجموعۀ آزادی به وزارت نیرو برای مصرف برق باعث شد امروز برق قطع شود و حتی شنیده شده برق مجموعۀ انقلاب نیز قطع شده است.
🔹
این اتفاق درحالی رخ داده که تیم‌های ملی کشتی جوانان و بزرگسالان خود را برای مسابقات جهانی…</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/455280" target="_blank">📅 12:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455279">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AskwXeY4yJ_r3L44NaN2VOJ_sRpJJbC8TgQ2QdVtX2Zd96ftC4868BaPI_NcipI_TkdIG9IYXtNQ8pXnHE1GSW5SWFal6ShsxforrSVDRAldK4RVfISUugcH6sKhNvm96umeRA79VEQ8A4aBGL26FZG_MsBZDpBSGO4dPunoHgyN6bDox93vNeB7252u3-fAlmbAkuWtM-95Elb3IbGwYIjvxHbXBxAFx-WxEwkt5wXqhUmxdUvTgCL_Mp5fVYBfg2RxFxZX_Haq5c0mNsN_Ik7z-9aJPnpFmWzzj2lGuyzpj34wnspiU6c8tdTLv7D_MYfmwcUNiIZOlMT0kv0z1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با عبور از ۵ میلیون و ۶۰۰ هزار باز هم رکورد تاریخی زد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۹۴ هزار واحدی به ۵ میلیون و ۶۵۴ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/455279" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455278">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b222dc371a.mp4?token=KXkVJkeTY4ZOekIJBJIMCdCMeFD9D9zASOo67fl5s9vkyVnjbVw1ysrjvrEKd8cdbs8PrUzrK5nGG6GkgUfK5Tq0dnOxx0W4VriMKrMISWSuZfHe1p5KKMQmlsO9vUqJjOG8FAw9n0qZ87HyWwT2TTuq2G8MHJhCkcoGeN-dn-AXnlrEuGVw2OhOKYPc7TPVJ3pXwlRfoi2cCTgKr6fXh1Er63fE5ZUU1pGYMx8E1fIet7GS5E-6idnW9ed_Rh2BURaGh5-aq6pnOrEq3P60BVhG2rGvWbNRTwEabhRqwgfh_U34zcfHUDMhOhaoJk5HYaVRwDbciKNhdStunTDLGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b222dc371a.mp4?token=KXkVJkeTY4ZOekIJBJIMCdCMeFD9D9zASOo67fl5s9vkyVnjbVw1ysrjvrEKd8cdbs8PrUzrK5nGG6GkgUfK5Tq0dnOxx0W4VriMKrMISWSuZfHe1p5KKMQmlsO9vUqJjOG8FAw9n0qZ87HyWwT2TTuq2G8MHJhCkcoGeN-dn-AXnlrEuGVw2OhOKYPc7TPVJ3pXwlRfoi2cCTgKr6fXh1Er63fE5ZUU1pGYMx8E1fIet7GS5E-6idnW9ed_Rh2BURaGh5-aq6pnOrEq3P60BVhG2rGvWbNRTwEabhRqwgfh_U34zcfHUDMhOhaoJk5HYaVRwDbciKNhdStunTDLGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: پاکستان از قالیباف و عراقچی برای سفر به اسلام‌آباد دعوت کرده و این سفر در زمان مناسب انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/455278" target="_blank">📅 12:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455277">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc9a50c3c.mp4?token=GUYWbMEmH4pxJg0U5mIFJpWwJjfjZ6V0mnVbG2gH5RWINL_icfMjqAFVUu9LRHonic1mdiH-G8QygzhYk-tJwV7AIZqAQksixhYpdVloobszTqUiVQUa-BmU2OsFm9DIypZYXQO9tumLOG99KEYwOCXiC24of7xZpmgzCpAVyLSEdS8PyunjAYPwgR38uCiVMETw9lw6WaZ8FbfS7oVjb5HhJsrgEXzwqcx4fcnP_YgNrs5ES90H-Ur1zrfkIKzDHTB7nfysjVw3aFk5lXOs1U_ZYpnpb8juoG7E-OBzioxUAoNJ08foOtVfKL6KWy_vg3LrIZG0e2E9SSOjEc8CBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc9a50c3c.mp4?token=GUYWbMEmH4pxJg0U5mIFJpWwJjfjZ6V0mnVbG2gH5RWINL_icfMjqAFVUu9LRHonic1mdiH-G8QygzhYk-tJwV7AIZqAQksixhYpdVloobszTqUiVQUa-BmU2OsFm9DIypZYXQO9tumLOG99KEYwOCXiC24of7xZpmgzCpAVyLSEdS8PyunjAYPwgR38uCiVMETw9lw6WaZ8FbfS7oVjb5HhJsrgEXzwqcx4fcnP_YgNrs5ES90H-Ur1zrfkIKzDHTB7nfysjVw3aFk5lXOs1U_ZYpnpb8juoG7E-OBzioxUAoNJ08foOtVfKL6KWy_vg3LrIZG0e2E9SSOjEc8CBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: قاعدتاً خدمات دریایی مابه‌ازایی دارد و باید آن را دریافت کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/455277" target="_blank">📅 12:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455276">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWqBebWsFy8WFBi3ck_BRqhlsYzAWyVyHbJe6Ry0R7njw2uAn3WTTs--7-u-ooBP1VlnrJthflwWADIYGOAxwOKi3vgBSJEFnoTZ8b73YjnKtt-GrEECjrPwn931BOLlEnHEYACvM5aNzOsl5ohRzIM0fh1O-MbdNUN1-pV9-tA8pBGtnpSDeZeZRK8twa709slLcLWxehduD5i0pKd3fRtniC5mrZ-16RnzByH6uzwV8NBVvPFRtsIEzM8T3n3m-xos1grfL7lQIjMRVexLH2y2ka-psQLsD8JJuQ5OR3TBPDosS2gGJ8F9PSuOyLzDU_RcFVFapTXVaB4UEmLLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تعزیرات: سهمیهٔ گران‌فروشان نان قطع می‌شود
🔹
رئیس سازمان تعزیرات حکومتی: در صورت تکرار ۷ نوع تخلف، از جمله گران‌فروشی و برخی تخلفات مرتبط با عرضهٔ نان، با قطع یا کاهش سهمیهٔ آرد و همچنین تعطیلی واحد متخلف برخورد شود.
🔹
بیش‌از ۱۵ هزار پرونده در حوزهٔ تخلفات نان در سراسر کشور وارد شده که حدود ۱۳ هزار پرونده از این تعداد مختومه شده و حدود ۲۹۰۰ پرونده نیز همچنان درحال رسیدگی است.
عکس: علیرضا مولوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/455276" target="_blank">📅 12:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455275">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e0493aa7.mp4?token=he7Jg6bxWLczFeOomrts0mmSWX9r_fjGeYo7jVTRTS-elxZnvLZN0fhv_5zXH0j5YsPAu6hGJZWgzgUNkt4mXPCmOgjesZygmobIgQ714O0HDKUpFO-9I1YNZQZTwV7C6D_xIcus_qDOdVrWy_XXttD38UQ25IcPDOzQ2vBpwG-HKQslDXasj0Rwyl4tVbi-rlvQIfxGqO29t3RJ6qvXn4NNYpOG1BAFTKapzSjH2OHzWT3lyODLzrxeilGplK7LlTc5A0NKVc1AweiFrKVf3BwRfL0GiJ5jfOJaDBgxww0ODBZGXnpcUXO7nb4gtvKsuStH13Q0vARCrUiIKzjmKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e0493aa7.mp4?token=he7Jg6bxWLczFeOomrts0mmSWX9r_fjGeYo7jVTRTS-elxZnvLZN0fhv_5zXH0j5YsPAu6hGJZWgzgUNkt4mXPCmOgjesZygmobIgQ714O0HDKUpFO-9I1YNZQZTwV7C6D_xIcus_qDOdVrWy_XXttD38UQ25IcPDOzQ2vBpwG-HKQslDXasj0Rwyl4tVbi-rlvQIfxGqO29t3RJ6qvXn4NNYpOG1BAFTKapzSjH2OHzWT3lyODLzrxeilGplK7LlTc5A0NKVc1AweiFrKVf3BwRfL0GiJ5jfOJaDBgxww0ODBZGXnpcUXO7nb4gtvKsuStH13Q0vARCrUiIKzjmKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
محسن رضایی دبیر شورای‌عالی امنیت ملی شد
🔹
معاون ارتباطات دفتر رئیس جمهور: با حکم رئیس‌جمهور، محسن رضایی به‌عنوان دبیر شورای عالی امنیت ملی منصوب شد. @Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/455275" target="_blank">📅 12:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455274">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e338aa971e.mp4?token=YHN6T2p5As27-HVOkrD1wP7s6phjM42jG1hOa3C9lFusZMOZZXwHJ7s3CCDzWk_TYVOhM7yBHk6PyREusweBu684xvgwVN04gX33m5T_Lm-2Cb6hhfBAkr6lM1hiDRyD6BMTHDcQ1TdW0VgxNdI725cgPeOdB1lcQlKHzGtBj8Wrb5FM4xjTulnHoKAe4Sn-90tRlXwiVhTLQvC3nKnk70_qBPqrfLZSPMB-ptqgGEwhU-PPxax6UNRcF1Ogq8v8hfwz00OXHO8FkciXiB-hrMDJph-7cWvfr06xVZbt9Zq3-C9lzV9KA5Ou4qz1wiYpJ-L-MqJWU-q4STiQOoG0Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e338aa971e.mp4?token=YHN6T2p5As27-HVOkrD1wP7s6phjM42jG1hOa3C9lFusZMOZZXwHJ7s3CCDzWk_TYVOhM7yBHk6PyREusweBu684xvgwVN04gX33m5T_Lm-2Cb6hhfBAkr6lM1hiDRyD6BMTHDcQ1TdW0VgxNdI725cgPeOdB1lcQlKHzGtBj8Wrb5FM4xjTulnHoKAe4Sn-90tRlXwiVhTLQvC3nKnk70_qBPqrfLZSPMB-ptqgGEwhU-PPxax6UNRcF1Ogq8v8hfwz00OXHO8FkciXiB-hrMDJph-7cWvfr06xVZbt9Zq3-C9lzV9KA5Ou4qz1wiYpJ-L-MqJWU-q4STiQOoG0Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدهی مجموعۀ آزادی برای کشتی دردسرساز شد
🔹
بدهی مجموعۀ آزادی به وزارت نیرو برای مصرف برق باعث شد امروز برق قطع شود و حتی شنیده شده برق مجموعۀ انقلاب نیز قطع شده است.
🔹
این اتفاق درحالی رخ داده که تیم‌های ملی کشتی جوانان و بزرگسالان خود را برای مسابقات جهانی و بازی‌های آسیایی آماده می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/455274" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455273">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_SXfxl82RwL8TJSBHlTpOOVGnhuWAO1A5zL8ZEdfJF2RNTYWbRAPHLdtFIZ5OEv8E_HJf9dQWg8mzWwshc4i4Ju0Q8s4ByTOAu-I0d4Ic08fDmBxhKfcgvA10Dzrv0oIPDJ5BI6Sd1tNea6Xi-yizf_LEQWBNtWqu96lLICAioy8a0W8TGGQzZIBekJgJ2276f42df9mv8cn8qdPhtioPKwep5NHgf50JFyqDH-sRuLpvHvD8kYZm-EMkLsxzWyYA9pEwmgeUBl-UG-3iRenibA_5TZ0DpnW6cL3AIDjewg97iGI8nMwKxzzWy_KxEKaqxojYC-XPo26l8y0FNiSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدهٔ تازه سایپا به مشتریان در انتظار
🔹
مشتریان سایپا می‌گویند این خودروساز ساینا و سایر خودروهای ثبت نامی را تحویل نمی‌دهد.
🔹
برخی مخاطبان خبرگزاری فارس در پویشی اعلام کرده‌اند سایپا با وجود دریافت وجه و وعدهٔ تحویل ۹۰ روزه، پس از ۱۰ ماه هنوز خودروها را تحویل نداده است.
🔹
حالا سایپا می‌گوید روند کاهش تعهدات تا تحویل تمام خودروهای باقی‌مانده ادامه دارد.
🔸
اوایل اسفند سال گذشته، تعهدات معوق این شرکت ۵۸ هزار دستگاه اعلام شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/455273" target="_blank">📅 12:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455272">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45fb6fa172.mp4?token=hhD4fM1cusaIbkXonwvBBIJ8p-Op_POiEaSc_EmTvGn3alPz9ckXjUnzqOEllF3rNk3yVJF55sGyzeXQKsTI8e3sCvmKwvP6nckKEwEoAoQTTjifjfvQIKrxX1wM_wSzqc48sYIoKzvkWnXym2jV6UB9hJQW8fFYUjm6LsnQWRip4WajvTJSvL1mn6c5SVHx7gpG-yTaD28UWLh7iYnAliIppc3jcaMKpqo_qHwZZ6M700KfYdsZuO3QeODKRFvpkUOD-FegQnHXBZNLnD2FHGMHzD0B_kA8YxV3SOzFHLnY12x7uEyvGxIA0-YUbX4-tDxkOT5H7huWmH8it_QfIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45fb6fa172.mp4?token=hhD4fM1cusaIbkXonwvBBIJ8p-Op_POiEaSc_EmTvGn3alPz9ckXjUnzqOEllF3rNk3yVJF55sGyzeXQKsTI8e3sCvmKwvP6nckKEwEoAoQTTjifjfvQIKrxX1wM_wSzqc48sYIoKzvkWnXym2jV6UB9hJQW8fFYUjm6LsnQWRip4WajvTJSvL1mn6c5SVHx7gpG-yTaD28UWLh7iYnAliIppc3jcaMKpqo_qHwZZ6M700KfYdsZuO3QeODKRFvpkUOD-FegQnHXBZNLnD2FHGMHzD0B_kA8YxV3SOzFHLnY12x7uEyvGxIA0-YUbX4-tDxkOT5H7huWmH8it_QfIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: تنگهٔ هرمز به‌خاطر اختلاف‌نظر ایران و عمان بسته نشده که با توافق ایران و عمان باز شود
🔹
بازشدن تنگهٔ هرمز منوط به تحقق شرایطی است که در پی تجاوز نظامی آمریکا و رژیم صهیونیستی به ایران تحمیل شده؛ ما هنوز در جنگ هستیم و تا وقتی که محاصرهٔ…</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/455272" target="_blank">📅 11:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455271">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJXU1ygsOFxUQ76WqZYgyVKLLisFjN9b22fyAu6jScv2ZYVgbNS66FYJBZRkLoXqNfXqQabxduFq2zm8gxCWcKr16l34IaV8EIMbavsIfwHoUrawacMaGL_sn3afd6FhM45ny_XZ4_kX1Tit9w9PxvB1qxFoHFAyOseq4D8a2nGnIt5nuXTHyd7K54xnYrj6dCuTmuTF5JuX98_OzXjRuLp5F8QCNtqD8TokULyhl6k5cA87fyqpJRKyVntPCEfX1Acbz4iuKMwhm6r-iLHBHgQPtHUTpRmG4dQs9WhdFIElnbC2B2g_ovGf3RoillC2f_BOZ83_rzvZfCduoVtEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خضریان: کلیات طرح اقدام راهبردی امنیت تنگهٔ هرمز در کمیسیون امنیت ملی تصویب شد
🔹
عضو کمیسیون امنیت ملی: با توجه به موقعیت راهبردی خلیج فارس و تنگهٔ هرمز و لزوم اعمال حاکمیت جمهوری اسلامی ایران به‌منظور پیشگیری از تکرار اقدامات خصمانه علیه ایران، کلیات طرح…</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/455271" target="_blank">📅 11:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455270">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b1474c5f.mp4?token=BUuAn-lbIoBEozBmGZlH1_faiK0fcXY1DOhu9XsB-0QqJBt0ASKDCkMLNke4-f_cS7nUbzkW4UahnPMxK-k-h47puHR573ZDh3_IB5QoIRKC2F5fhoWYNI537O1sq2PlDeaYw1jJRYypmTg2jpz-RBljIYICmzV52ABWgu5Z1zi5qORc1WxsBCfQTOMqRBj3cXL1lrFYNYI2OOl5y_y8TlF6Jx2FSzaYDOttLI8Q2zrzN6Os72cVS4PiQzgkTpHg-XIwkmBn94Pc638goJVAl79Z6YMt61v01NDqCqgzsZvmea_ibqmNArpKOF-qe4liP07LBUFZ5_753ENrWevk1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b1474c5f.mp4?token=BUuAn-lbIoBEozBmGZlH1_faiK0fcXY1DOhu9XsB-0QqJBt0ASKDCkMLNke4-f_cS7nUbzkW4UahnPMxK-k-h47puHR573ZDh3_IB5QoIRKC2F5fhoWYNI537O1sq2PlDeaYw1jJRYypmTg2jpz-RBljIYICmzV52ABWgu5Z1zi5qORc1WxsBCfQTOMqRBj3cXL1lrFYNYI2OOl5y_y8TlF6Jx2FSzaYDOttLI8Q2zrzN6Os72cVS4PiQzgkTpHg-XIwkmBn94Pc638goJVAl79Z6YMt61v01NDqCqgzsZvmea_ibqmNArpKOF-qe4liP07LBUFZ5_753ENrWevk1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: تا زمانی که آمریکا موارد نقض تفاهم را جبران نکند، امکان مذاکره وجود ندارد
🔹
مذاکرات ما با عمان به‌معنی بازشدن تنگهٔ هرمز نیست و صرفاً جهت تعیین مسیری است که در صورت بازگشایی تنگهٔ هرمز از آن استفاده خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/455270" target="_blank">📅 11:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455269">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ba817d81.mp4?token=q1xZQ-bSfYh0NqQWi6x_tAmarg6cteFKvpSkskQ4vgR3pNzq6DVOONEcdXYEOVugFw6RkDnACOEB2iToL9w0VXa4V-C5CzOfOrFKmRllqX592iE1FLh-nr1TyatbamlCQxOAqf4XLHhMD_9X5pHtM8Ch906XodYLSNWE4RcBecqwuYiTlVZoQQN1E49-kZ7m1tJch8hEUpeSI0CJpVJgtChXr3aHlsPeQLrxfq5W6RKjOItR4Q3pSbma1nVoKb_6OijIsHlzAea5X2invTD-3btFnoHCVOAn4ugSi_H045zjZOjuMzYbRMd8hrXDxOqpKLdW3yu1h_5Ij-jMlDr3HUsWxD4Dp9_J1G1iZ8yU70Vt7-QVr4rKi8fx1nyR1nb2bNJR7wO9-oTbsH2ErU68cV_Tek8zqXmlXNOwzE928CaqKyCDtGypVGbaPSRYSFvQg-2WAwBdUd9Q3lmOJHD1bhkWHhb32YnK15W3QIZJY7ijtmeQ-NJ_SCsICtEHUZNt4ebIteh84vArGB0TlpOWzUIaeO83fbjf53Cl7QHL3FGg_u072bhhKzjrNPBxpGuDMt1XqdHCb189I7uPsYzmB6xnSQ-yxfVEWbi2UB0xCAiOy_zi7jXMF4rMW1QDzVG7BSjHq0KhYcsfcMI42we1fYkNQEpaCf_Uj3PMY2C2gfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ba817d81.mp4?token=q1xZQ-bSfYh0NqQWi6x_tAmarg6cteFKvpSkskQ4vgR3pNzq6DVOONEcdXYEOVugFw6RkDnACOEB2iToL9w0VXa4V-C5CzOfOrFKmRllqX592iE1FLh-nr1TyatbamlCQxOAqf4XLHhMD_9X5pHtM8Ch906XodYLSNWE4RcBecqwuYiTlVZoQQN1E49-kZ7m1tJch8hEUpeSI0CJpVJgtChXr3aHlsPeQLrxfq5W6RKjOItR4Q3pSbma1nVoKb_6OijIsHlzAea5X2invTD-3btFnoHCVOAn4ugSi_H045zjZOjuMzYbRMd8hrXDxOqpKLdW3yu1h_5Ij-jMlDr3HUsWxD4Dp9_J1G1iZ8yU70Vt7-QVr4rKi8fx1nyR1nb2bNJR7wO9-oTbsH2ErU68cV_Tek8zqXmlXNOwzE928CaqKyCDtGypVGbaPSRYSFvQg-2WAwBdUd9Q3lmOJHD1bhkWHhb32YnK15W3QIZJY7ijtmeQ-NJ_SCsICtEHUZNt4ebIteh84vArGB0TlpOWzUIaeO83fbjf53Cl7QHL3FGg_u072bhhKzjrNPBxpGuDMt1XqdHCb189I7uPsYzmB6xnSQ-yxfVEWbi2UB0xCAiOy_zi7jXMF4rMW1QDzVG7BSjHq0KhYcsfcMI42we1fYkNQEpaCf_Uj3PMY2C2gfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدرالحسینی، کارشناس مسائل غرب آسیا: پس‌از ۶۰ سال تنگهٔ هرمز کاملاً ایرانی شده
🔹
حاکمیت و مدیریت ایران بر عبور و مرور در تنگه تثبیت شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/455269" target="_blank">📅 11:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455268">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e8806c8be.mp4?token=BC1-EUCeJRhatOLuO8fjAV1Bu8L7VmlmW_r4J-8Q1QPJsrZ8XRS8AHpmuqf9kvdqVjU6ao6yO4roQTHmmAGaiykYeSsUPJ7RD8InkEvh4NyU-crSIYJV-NlZYh66OF_PQyVfQUnZ1_pRwIr_vDAzVZxDqCEgHrx17l8iM10a7GHeXpUOKEyV7xyTKpk8Ea7J9fZ37GMD-rzqRpQKYG8P6A9-ZtqYdIiaugeoGQfXBD3RDkN18fM92TyXwGVC4AhzusVnnz9XA6MgzfvtPJ8edGxfhUvYMnL7S4gDZaMunbnaqWaFby6fJuVumwVkyWVg2C_dkARww02v0GmF83QgjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e8806c8be.mp4?token=BC1-EUCeJRhatOLuO8fjAV1Bu8L7VmlmW_r4J-8Q1QPJsrZ8XRS8AHpmuqf9kvdqVjU6ao6yO4roQTHmmAGaiykYeSsUPJ7RD8InkEvh4NyU-crSIYJV-NlZYh66OF_PQyVfQUnZ1_pRwIr_vDAzVZxDqCEgHrx17l8iM10a7GHeXpUOKEyV7xyTKpk8Ea7J9fZ37GMD-rzqRpQKYG8P6A9-ZtqYdIiaugeoGQfXBD3RDkN18fM92TyXwGVC4AhzusVnnz9XA6MgzfvtPJ8edGxfhUvYMnL7S4gDZaMunbnaqWaFby6fJuVumwVkyWVg2C_dkARww02v0GmF83QgjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس اوراسیا: پیامدهای کنوانسیون دریای کاسپین از واگذاری بحرین هم زیان‌بارتر است
🔹
برهان حشمتی: در کنوانسیون رژیم حقوقی دریای کاسپین، فرمول ۱۵ مایل آب‌های سرزمینی و ۱۰ مایل منطقۀ انحصاری ماهیگیری پیش‌بینی شده؛ یعنی در مجموع ۲۵ مایل. این محدوده به‌هیچ‌عنوان…</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/455268" target="_blank">📅 11:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455267">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ab3f7d2.mp4?token=bjRQylS-ErnGywZflXtGKu13lC3P079pCBfjNMQThyB6CVzrTcOX6h56H8Vgn3ylKyJcyesuSlMFpBRD3WOZQIjfjB9Eurn6E1OiAKIqzaQZDCg8lMN-sYmzT_Ygi6qZvbimSy0kJAwuziZvW-1p1phGqU4Kl6kkxQ_dnwlb-buzl7rq6ur1s0j5mx5Jt888jqC5C3HKW61qdXc-RGiku3XsUhV6g65iaB0Y5eSzlAkK9WX0ww2afXQ1bOHYHabPXiDRZjjyQJOCQLguIs2kzC65x6DXlnnLc-TsS4v_-AxE6zz8sV0CiTHNKu1qDZBydiW2UO3nN3HXY2SQUjsL1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ab3f7d2.mp4?token=bjRQylS-ErnGywZflXtGKu13lC3P079pCBfjNMQThyB6CVzrTcOX6h56H8Vgn3ylKyJcyesuSlMFpBRD3WOZQIjfjB9Eurn6E1OiAKIqzaQZDCg8lMN-sYmzT_Ygi6qZvbimSy0kJAwuziZvW-1p1phGqU4Kl6kkxQ_dnwlb-buzl7rq6ur1s0j5mx5Jt888jqC5C3HKW61qdXc-RGiku3XsUhV6g65iaB0Y5eSzlAkK9WX0ww2afXQ1bOHYHabPXiDRZjjyQJOCQLguIs2kzC65x6DXlnnLc-TsS4v_-AxE6zz8sV0CiTHNKu1qDZBydiW2UO3nN3HXY2SQUjsL1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدئویی دیده‌نشده از شهید سپهبد موسوی کنار نوه‌اش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/455267" target="_blank">📅 11:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455266">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd73ed7028.mp4?token=UXZpqLUTYDEPiEnWr-LjX3ShLmeBdFDNwPgfjnDCObkLxazC-Xpee-4eVZ8cjv6Q1xNuyNSTcn1kUN4LXdOJOzemX8GrPdrVJuLQakRuE1ojhC_-SvGHUvKcjOlioWl_a8GpNLn4TDqSpFrLh8xDF-4Od6nts74HxhUww0_pPZSrqzqJdGkG9Wb0RnillJ2-TefQ38caV3x5U_SjftW7Sh-WlD-QpCbjpTAN7sbsthXR4_DKuW_KEIdu_kGpyfIxBoltiIiXQzvP8x7vpnRQ12NXiRm8cuUfSlOC_CXrsLFYubljfF-cxllYFw6VXGHuc3W7cl2YUORjkBX4Uk-TEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd73ed7028.mp4?token=UXZpqLUTYDEPiEnWr-LjX3ShLmeBdFDNwPgfjnDCObkLxazC-Xpee-4eVZ8cjv6Q1xNuyNSTcn1kUN4LXdOJOzemX8GrPdrVJuLQakRuE1ojhC_-SvGHUvKcjOlioWl_a8GpNLn4TDqSpFrLh8xDF-4Od6nts74HxhUww0_pPZSrqzqJdGkG9Wb0RnillJ2-TefQ38caV3x5U_SjftW7Sh-WlD-QpCbjpTAN7sbsthXR4_DKuW_KEIdu_kGpyfIxBoltiIiXQzvP8x7vpnRQ12NXiRm8cuUfSlOC_CXrsLFYubljfF-cxllYFw6VXGHuc3W7cl2YUORjkBX4Uk-TEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه در واکنش به پیمان دفاعی مکه: کشورهای منطقه در ۳ سال گذشته فهمیده‌اند که امنیت، کالای قابل‌خریداری از دلالان دروغین نیست
🔹
هر طرحی که مبتنی بر واقعیت‌ها باشد و دشمن و تهدید را درست بشناسد، به امنیت منطقه کمک می‌کند و جلوی بی‌ثباتی دشمن…</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/455266" target="_blank">📅 11:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455265">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">صدور کیفرخواست ۶ نفر از کارکنان یک‌ نهاد‌ اجرایی به‌اتهام اختلاس
🔹
دادگستری سمنان: کیفرخواست ۶ نفر از کارکنان یکی از نهاد‌های اجرایی گرمسار به‌اتهام مباشرت در اختلاس میلیاردی توأم با جعل، تضییع اموال عمومی، مشارکت و معاونت در اختلاس و دریافت رشوه صادر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/455265" target="_blank">📅 11:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455264">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80cff58db5.mp4?token=ciEPDtUlS1QCFIxeE-KJbAX3I3x0JLhH0BJZTuWMBJIBE3UIGkcDAPm45S1AIbJzjBX2IKjikG6HCD65PAMAak975Lo-f1IZQyWxluJWkt0AYPTNdY3l4VXjzoE5evPCOuKCIkDrXXMjpS99de6SDcgVL45Snz1dSJ9Se-LO5j-SrNo5p8LJpnb-ysAylcNaWLNcBrgrV6wBAfe--llQ4SPbR3AVk5F9qPK1E7F18GnohCvUNfaim02ZN3rKeiBo0QppraKU6KiA_Cwj_ZWZ6CxdRP427VEUD9uVSULfWI04NBZXg48aZKYsHkkZFYkXidcqwIK1Zsd08zu0haP9Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80cff58db5.mp4?token=ciEPDtUlS1QCFIxeE-KJbAX3I3x0JLhH0BJZTuWMBJIBE3UIGkcDAPm45S1AIbJzjBX2IKjikG6HCD65PAMAak975Lo-f1IZQyWxluJWkt0AYPTNdY3l4VXjzoE5evPCOuKCIkDrXXMjpS99de6SDcgVL45Snz1dSJ9Se-LO5j-SrNo5p8LJpnb-ysAylcNaWLNcBrgrV6wBAfe--llQ4SPbR3AVk5F9qPK1E7F18GnohCvUNfaim02ZN3rKeiBo0QppraKU6KiA_Cwj_ZWZ6CxdRP427VEUD9uVSULfWI04NBZXg48aZKYsHkkZFYkXidcqwIK1Zsd08zu0haP9Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: کویت هنوز امکان دسترسی کنسولی سفارت به ۴ شهروند دستگیرشدهٔ ایرانی را ایجاد نکرده است
🔹
اجازه‌دادن به طرف‌های متجاوز برای اقدام علیه ایران از سوی دولت‌های منطقه، آن‌ها را کنار طرف‌های متجاوز خواهد نشاند. @Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/455264" target="_blank">📅 11:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455263">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROpp_jKuVIsxEX8junY0PCZC4sPqzdircgPdJoXw0UzLMlss0FasNaFQ5vd_YgCDupENPE0UK1_gp8Q6oeUVDlfcmtVZPS5f74Ml0-aITXtoLSFCeoORqqM2GYbjE5uVxabb9zFWS-g4hpxrQTaUsaa2255gvmoUQDNh-jH9ptcVGn2sEPXdhAsyZefmIY3OnKDTl0jfAOYvavEHgDziDiUHroXDenQGDrbd9tuqIBHddcBBiRUHECgssCcP_GYYcm3u8KHgsiSUU1okahUgi-jL5Pdu4rwPEuD-Hugh2Eo7Sz5m0f1D-gPZVnvfeQd-CE-pIYlpAnVIDrgUbJyNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس قید قربانی را زد
⚽️
مسئولان پرسپولیس در مقطعی مذاکراتی را برای جذب محمد قربانی انجام دادند اما درخواست مالی باشگاه الوحده برای صدور رضایتنامۀ او باعث شد انتقالش منتفی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/455263" target="_blank">📅 11:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455262">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae325ab684.mp4?token=IpvwLUtGdIDAyHgM7lQJ9pnQ7iazEBqIVTHbBIeAj1OJ5TCJ23MhUrFO13uBqZxlM7pQZN8TRM9ZtbgWNceEDsK79mmJb7sHJaohsMosPhX4tBiJPpRWSZZZpPWZMQvf759b0qoIrsn3gpdrcVYyWXcl9B6xxzbX2OzxRNjGfWcmH6GrDBJFbOd46L_vBS74nqYWFpUml7tIHkklmOFoh24Sg-tTxeu8WPwsPbTB2a33gngkJ6HRTFFheXqiKIB5tAIzJR6EFW7QUccY9K9H1KtHECpUsHzG4FJWFJg8MXga0VCKUpd7PDzO_lHrGskmvrAynel-1gOXB3TnVKghtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae325ab684.mp4?token=IpvwLUtGdIDAyHgM7lQJ9pnQ7iazEBqIVTHbBIeAj1OJ5TCJ23MhUrFO13uBqZxlM7pQZN8TRM9ZtbgWNceEDsK79mmJb7sHJaohsMosPhX4tBiJPpRWSZZZpPWZMQvf759b0qoIrsn3gpdrcVYyWXcl9B6xxzbX2OzxRNjGfWcmH6GrDBJFbOd46L_vBS74nqYWFpUml7tIHkklmOFoh24Sg-tTxeu8WPwsPbTB2a33gngkJ6HRTFFheXqiKIB5tAIzJR6EFW7QUccY9K9H1KtHECpUsHzG4FJWFJg8MXga0VCKUpd7PDzO_lHrGskmvrAynel-1gOXB3TnVKghtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: افزایش اعتبار کالابرگ به‌زودی اطلاع‌رسانی می‌شود
🔹
شرایط جنگی تأمین منابع افزایش اعتبار کالابرگ را با مشکل مواجه کرد، اما دولت درحال تدوین برنامه‌ها و اتخاذ تصمیمات جدید برای تأمین منابع مورد نیاز است.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/455262" target="_blank">📅 11:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455261">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59de1a44be.mp4?token=JO_ptWfAm0sHItOos4z_Gz4uhyUF5a8bUpwZ2FqaU2jxUeyHl4SCPhQdyIY9LgEtF32qrcwUp-qIY_ZYyVSeNC0mALQlbWfo-mfNQgc2tbQJGoFYUyPnJfsnoCpcxZG2n_DsTKIKWehS_0okD_ECkGU7vhKi706YiBmXbcxg0K144dRjulSYMPelgQsix1oTAIV60QkPZuPx0jBpFVbmohRZnerNLOwbOP5kmKr5SSni68O8d8Dty6EkH0cTeDI3paTyB08jpvjQL-5dGt-yXaocJE5uFQw_zTU0nadC8Buv9kTb2I41fRfnflSczWJ6Cj9L8uGo_DLET0KVoVnxUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59de1a44be.mp4?token=JO_ptWfAm0sHItOos4z_Gz4uhyUF5a8bUpwZ2FqaU2jxUeyHl4SCPhQdyIY9LgEtF32qrcwUp-qIY_ZYyVSeNC0mALQlbWfo-mfNQgc2tbQJGoFYUyPnJfsnoCpcxZG2n_DsTKIKWehS_0okD_ECkGU7vhKi706YiBmXbcxg0K144dRjulSYMPelgQsix1oTAIV60QkPZuPx0jBpFVbmohRZnerNLOwbOP5kmKr5SSni68O8d8Dty6EkH0cTeDI3paTyB08jpvjQL-5dGt-yXaocJE5uFQw_zTU0nadC8Buv9kTb2I41fRfnflSczWJ6Cj9L8uGo_DLET0KVoVnxUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه ترکیه: در مکه علیه ایران ائتلاف نکردیم
🔹
هاکان فیدان، وزیر امور خارجه ترکیه در مصاحبه‌ با خبرگزاری آناتولی گفت که ائتلاف سه‌گانه مکه می‌تواند گسترش یابد و علیه هیچ کشوری از جمله ایران نیست.
🔹
او همچنین تأکید کرد که ایران «هدف» این توافق نیست. فیدان…</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/455261" target="_blank">📅 10:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455260">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2LhfiYerYfzS8yG5sq2OmLG269xvbt3DvLdL57ImJDFQdApfjoHy153GmEYDOlgcd2oeX_MgeDMqVYdAwwTOPrFTADst5QeEf-NaWUpooyUFcxJp-Z0RF6CgItFEg2G29FDOYWLgtA5oDpRd0FV8wu7icjgKRPEPgCKKbJ-4hgFsbGZQUFQX3hKZVNliLh0Mkk7Y8Gqu19u2IlVmQtXC3hVwjRnzqSaCPmpk36fYqwpnCvpaTsjCxwOzQj8FkmV157bgDVm-Bp4gGFsxrGyKfDTykrhKJoL1pCjY0ncwCVYFtTorDSwdlJgPozSym9Y_CvJMATmyZRwh4N5KQ641Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
بانک رفاه کارگران وارد عرصه بانکداری ارزش‌آفرین شده است
🔹️
مدیرعامل بانک رفاه کارگران گفت: زنجیره مکانیزه تهاتر مطالبات و بدهی‌های سازمان تامین اجتماعی (تکو) گامی عملی برای تأمین مالی غیرتورمی و پشتیبانی از زنجیره تولید محسوب می‌شود و در این بانک ابزارهای اثربخشی به منظور تحقق اهداف این زنجیره طراحی و عملیاتی شده است.
🔹️
دکتر اسماعیل للـه‌گانی با بیان این مطلب در همایش ملی "معرفی و تبیین بهره‌برداری از توکن تکو"، این زنجیره را نقطه عطفی در مدیریت مطالبات و بدهی‌های سازمان تامین اجتماعی برشمرد و با اشاره به ظرفیت‌های این بانک در مسیر اجرای آن گفت: بانک رفاه کارگران با عبور از بانکداری سنتی و دیجیتال، وارد عرصه «بانکداری ارزش‌آفرین» شده است. این بانک تحول خود را بر پایه ایجاد راهکارهای هوشمند و متنوع مالی، حمایت از اکوسیستم تولید و ایجاد اعتبار شفاف برای خانوارها و بنگاه‌ها دنبال می‌کند.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/455260" target="_blank">📅 10:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455259">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqryfzU9O3WMkJc6NiIGImcyyoQSPozb3tBacTOFd8a54cVoZsNKLEa5B83kmn_blg9KYgYi2LS5cpxHQCQq48kHaDbBZua5h7uh6-B-PNhHOCEcut6YCW305u6nhCaF1c4fHxuUM1WzJlpxMm9WKKxNbMlQk0UHsQbm6NnkZoXKVEDzBdzN-W-ElcxyZjDLmjFAHRC0Jd4-lm0uHQA_aYDT74iYpfn6__wk_lF4qB8TvGAFoN06r_8WINRKoMMGHlYoR2MHauVL42Pl31h1gv0-A6C30i8MuBSWbj8wvjwAIDpXiO54bDPBMfcyIkviHcwLSV4dOIwrYzarjOaFlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ثبت‌نام دوره تخصصی «هوش مصنوعی در روابط عمومی و رسانه» آغاز شد.
🔹
این دوره یک برنامه آموزشی جامع، کاربردی و پروژه‌محور است که به شما می‌آموزد چگونه هوش مصنوعی را وارد فرآیندهای واقعی روابط عمومی، رسانه و ارتباطات سازمانی کنید.
🔹
در این دوره ۲۴ ساعته، از تولید محتوای حرفه‌ای و مهندسی پرامپت تا تحلیل افکار عمومی، رصد رسانه‌ها و مدیریت هوشمند بحران را به‌صورت گام‌به‌گام فرا می‌گیرید.
🎉
ویژه مدیران و کارشناسان روابط عمومی، رسانه و ارتباطات
⚠️
مهلت ثبت‌نام: تا ۲۷ مردادماه
📝
ثبت‌نام دوره حضوری
📝
ثبت‌نام دوره آنلاین
مرکز آموزش‌های آزاد خبرگزاری فارس</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/455259" target="_blank">📅 10:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455258">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/455258" target="_blank">📅 10:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455257">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اتوبوس‌های منتهی به حرم رضوی ۲ روز رایگان شد
🔹
مدیرعامل اتوبوس‌رانی مشهد: خطوط منتهی به حرم امام رضا(ع) در روزهای چهارشنبه و پنجشنبه، هم‌زمان با سالروز شهادت پیامبر اکرم(ص)، شهادت امام حسن مجتبی(ع) و شهادت امام رضا(ع)، رایگان خواهد بود.
🔹
خطوط ۸۰۱، ۸۰۲، ۸۳۱، ۸۳۲، ۸۳۳ و ۱۲ در شب چهارشنبه تا ساعت ۲ بامداد و در شب پنجشنبه به‌صورت شبانه‌روزی فعال خواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/455257" target="_blank">📅 10:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455256">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌ تبریک سرلشکر خلبان عبداللهی درپی انتصاب محسن رضایی به دبیری شورای‌عالی امنیت ملی
🔹
متن پیام فرمانده قرارگاه مرکزی خاتم‌الانبیا: انتصاب شایسته جنابعالی به‌سمت دبیری شورای‌عالی امنیت ملی و نمایندۀ رهبری در این شورا را صمیمانه تبریک و تهنیت عرض می‌نماییم.…</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/455256" target="_blank">📅 10:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455255">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6396b5eab3.mp4?token=nX-leuzL4kEzGPjs0r48hmDwire0xPig6Xs8UJDnNleyjbzVlK3efX_Qk8xBxdIaRz9kNueWPh0fugPQ7BYd2TWmIl3l4cmJ2kmXoE1Fygg7Qr36MI889IFJh0TgQW-14iSlyRUs8xqkZjAJwEt6qDuLFZ46p3zUgIngL7RTYGOpuF9Gv0BirbaYU7RW9qnLVUCQDgcgMA5QECIlG4tQNE3izCqzp73EX3CeFlnDgiFL8064BdeVt7TgbfwsLV_JwH9Qt2fQJALCUwMS7bcTuhXmBL0oEsdaYtriixKpoKRjXggggk99aFuHqTv4WTCTaIeGnb5xxkazrovwpv5nKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6396b5eab3.mp4?token=nX-leuzL4kEzGPjs0r48hmDwire0xPig6Xs8UJDnNleyjbzVlK3efX_Qk8xBxdIaRz9kNueWPh0fugPQ7BYd2TWmIl3l4cmJ2kmXoE1Fygg7Qr36MI889IFJh0TgQW-14iSlyRUs8xqkZjAJwEt6qDuLFZ46p3zUgIngL7RTYGOpuF9Gv0BirbaYU7RW9qnLVUCQDgcgMA5QECIlG4tQNE3izCqzp73EX3CeFlnDgiFL8064BdeVt7TgbfwsLV_JwH9Qt2fQJALCUwMS7bcTuhXmBL0oEsdaYtriixKpoKRjXggggk99aFuHqTv4WTCTaIeGnb5xxkazrovwpv5nKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا فشار خون باعث سردرد می‌شود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/455255" target="_blank">📅 10:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455254">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ولایتی: محسن رضایی برای صیانت از امنیت و منافع ملی ایران نگاه راهبردی دارد ‌
🔹
مشاور رهبر انقلاب: در بحبوحۀ دگرگونی‌های ژرف جغرافیای سیاسی منطقه و جهان، اعتماد به نیروهای کارآزموده‌ای که در مکتب امامین انقلاب و در میدان‌های دشوار مدیریتی پرورش‌یافته‌اند، نشانۀ…</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/455254" target="_blank">📅 10:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455253">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: تا ساعت ۱۴ امروز احتمال شنیدن صدای انفجارهای کنترل‌شده در صفه، بهارستان و اطراف آن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/455253" target="_blank">📅 10:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455252">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzY_bu9lhINJuEZnrCaNQ6rzf-YbxkqzAM30kL9oPH8777G5T4GExDqdoYGnaVJ7-3YZ01BN2MIRuM6KQG0067jY4U-OMnu3v4CL9wbRkTK36bjvjKQ0g9F3HiNHCTGVkH_vAcn2acwbS20YaE3wg6L78Uid3pHKYTkz5ok6AjyYL6noEIFjgH7IGOvL9FkcT1q8s5oJ1OG-4THlM7yGDiIiT6lAPn-LNAymAa3sWVE-6YzU8oskysBN7YeXxVwKcqvcaI_Wegf51HA53N0lFOUZl-fniM1aKgDq7_MMWXM9mysH1cUPjYv2WDjifiC_2iZWXo1uUrlzKiRUarNSKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخبر: سرلشکر رضایی به مسائل راهبردی کشور شناخت عمیق دارند
🔹
پیام مشاور رهبر انقلاب به انتصاب محسن رضایی به‌سِمت دبیر شورای‌عالی امنیت ملی: شناخت عمیق جنابعالی از مسائل راهبردی کشور، تحولات منطقه و عرصۀ بین‌الملل و همچنین تجربه ارزشمندتان در عالی‌ترین سطوح…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/455252" target="_blank">📅 10:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455251">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3641e81aea.mp4?token=kJCR6RkwaHxwM2SWEJUyHwkG1uiTs15sJ2tQL61pOK-rjWJ2e4PRMqrL4aPktCq3vB8NotMbRVxyHizv1ph3A-fPQB_j3xZqXylPeZTwN3inb5A8fq2-SBSgduPbhv8odJOtGxAWdXK5Wn641uBhNRIObirF7aPBP6x-Fd5KMOYoaAedijWpI3dJ-3VoIvaAMFX1rTiNEbo2PlgFn9c8tPpzGMgrgyfCfKx8E2uSFKnyAgQiibzzQmRcxYc62pdlvFzSDbcGCZo7KCQ_BKgZJ-093qu82Ds2wyLl-LSMIRXFsHHIk1N0MIM0BFLzvXX858YymkulNHSu403rq5gVwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3641e81aea.mp4?token=kJCR6RkwaHxwM2SWEJUyHwkG1uiTs15sJ2tQL61pOK-rjWJ2e4PRMqrL4aPktCq3vB8NotMbRVxyHizv1ph3A-fPQB_j3xZqXylPeZTwN3inb5A8fq2-SBSgduPbhv8odJOtGxAWdXK5Wn641uBhNRIObirF7aPBP6x-Fd5KMOYoaAedijWpI3dJ-3VoIvaAMFX1rTiNEbo2PlgFn9c8tPpzGMgrgyfCfKx8E2uSFKnyAgQiibzzQmRcxYc62pdlvFzSDbcGCZo7KCQ_BKgZJ-093qu82Ds2wyLl-LSMIRXFsHHIk1N0MIM0BFLzvXX858YymkulNHSu403rq5gVwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی اوکراین به پالایشگاه نفت در نیژنکامسک روسیه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/455251" target="_blank">📅 10:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455250">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKgO0cVMgFgTrUSd2x0QJOMxXkOBfnLuLE2avP7HOE6TShP2oPzKDDgwnYK6akdqrVPIZSKP0Hg10Ls2Fpv3JpKsjYyC2cAiJFQ3HPrRO1DWGV-rKjv-Vgp80h42lTvwZYqlk_uI7HlEdFKGxIlcvbcHPPK6S79VAzW9tCRnDaP5cmt8NJnMkFP1qIdxRPmG81nU4wBbXFD5-dWSnrGW2yPuRbWBQ5r2REoYKug5YVz8r4WBcmXqGF2ks_FoUMSuwcgEq6o5BwXwtEzY_8n5gTG-_uwMCY4sz9mBbNTonGdeqV25ulFtknTIjOCyNxLTTSPySEQ3oYzW5JRFJ5tj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف انتصاب سرلشکر رضایی در شورای‌عالی امنیت ملی را تبریک گفت
🔹
معاون اول رئیس‌جمهور:  در شرایط حساس و پیچیدۀ کنونی که کشور بیش از هر زمان دیگری به تقویت وفاق، همبستگی و انسجام ملی نیاز دارد، تدوین سیاست‌های دفاعی-امنیتی هوشمندانه و اتکا به تجارب متراکم حکمرانی،…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/455250" target="_blank">📅 09:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455249">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">احتمال شنیدن صدای انفجارهای کنترل‌شده در دزفول
🔹
فرمانداری دزفول: به‌دلیل امحای مهمات تا ساعت ۱۱ امروز، احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/455249" target="_blank">📅 09:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455248">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c6e05ad7.mp4?token=kPuT9w09jhIBywXni_5WO1UDgRA5VFZghjAJcrdOhinTahLoNVzHUv9NRH4AwumYIZ4opN0YjblKSTVf3SiT5vQQVRXqJHlEpp6X1ijwX3AlRLMe5rHwpPj9y-GpJHd9bKf4lvM1JyU56y1iVvX_NO8XK-rROucm05N88YskoDmp7Mm4-jGzxpJ1fBoDMgn2dg1sSyTYoicn2rPskXzO8nQCXBFMzZJZhIjAcliimQqlrVnJ5bKNtx8svhlwACQrAfxSHunFnQNz5MO8c_Qep97SIWqt3JdUsSMbt_PI2DpS22KZlCIrWwsiab4StIWGTUFm1h2m5HlyXJWlfirA4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c6e05ad7.mp4?token=kPuT9w09jhIBywXni_5WO1UDgRA5VFZghjAJcrdOhinTahLoNVzHUv9NRH4AwumYIZ4opN0YjblKSTVf3SiT5vQQVRXqJHlEpp6X1ijwX3AlRLMe5rHwpPj9y-GpJHd9bKf4lvM1JyU56y1iVvX_NO8XK-rROucm05N88YskoDmp7Mm4-jGzxpJ1fBoDMgn2dg1sSyTYoicn2rPskXzO8nQCXBFMzZJZhIjAcliimQqlrVnJ5bKNtx8svhlwACQrAfxSHunFnQNz5MO8c_Qep97SIWqt3JdUsSMbt_PI2DpS22KZlCIrWwsiab4StIWGTUFm1h2m5HlyXJWlfirA4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چگونه انواع سردرد و علت آن را تشخیص دهیم؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/455248" target="_blank">📅 09:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455247">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0C67Y2fwoYSwMTEKn11NuTspAelwbQS_77OFsiGHs2cQWUmcK-p3WZuJHqB15972GEQsZvnSNYzQSem7Ib66fdPoyBlTKzPFWUB693PUiIdXq98XyLHJmWAz3rN6XfA-AwmcXGX3psud-ZzxkgmMW1V7RZH3h-dvwmLPVjlxXUDVUpdw58EwYq2DRBNx4fchr36z0ISyJZblJzBA7pysOSquOfqnrnvrBlg1Wr846XtQKoYioSUIGzGS9JhNqf8e72BVCT3J0ZbyF9e-9WvY6j3V6Xh9GoN65mnQb8YHMDJDeOlhsav4aPsFOO5fs18-129NoJ1-Vf2SuqY1AxUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
محسن رضایی دبیر شورای‌عالی امنیت ملی شد
🔹
معاون ارتباطات دفتر رئیس جمهور: با حکم رئیس‌جمهور، محسن رضایی به‌عنوان دبیر شورای عالی امنیت ملی منصوب شد. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/455247" target="_blank">📅 09:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455246">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB2zOB0DFz-3SZX3VwqHGEirYoWuFCIFlCXkzwDDBtvvH7kl26-vOKbaUzxo7eJSNJsCm6RSYVgK6dGLjy1cTJcuk0QqTkN27xl4so6ePuYmHoUshRxOWQtOPoqpIrXdyKPLUstcWvdHBV40bqkqGSo8QTwOSVgv9au3Jk1di036nJXosIBEFejrNhgTF89XPTlv1GL0GMQeBVZwTglIc1z9F_bbvaC0r7LgzjY2ZP93St43ANvKNxhOLjdosnE3K64L8DuH9Je323eCF58crAmeXuAapC27FNJ7ESHPtk_W7pbB-UvjJVrRcmjj_NU-gE6KOCYNW5x1MRY6Th7ERA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان تشنگی فضای سبز تهران با راه‌اندازی سه تصفیه‌خانۀ جدید
🔹
رئیس کمیسیون سلامت، محیط‌زیست و خدمات شهری شورای شهر تهران از موافقت شهردار تهران با احداث سه تصفیه‌خانۀ جدید در چیتگر، لویزان و سرخه‌حصار خبر داده است؛ پروژه‌هایی که می‌توانند بخشی از نیاز آبی فضای سبز پایتخت را از طریق استفاده از پساب تأمین کنند.
🔹
بر اساس این برنامه، با احداث و بهره‌برداری از سه تصفیه‌خانۀ جدید، بیش از ۵۰ میلیون مترمکعب پساب برای استفاده در فضای سبز تهران اختصاص خواهد یافت؛ ظرفیتی که می‌تواند وابستگی آبی فضای سبز به منابع آب شرب و منابع محدود زیرزمینی را کاهش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/455246" target="_blank">📅 07:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455245">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-T-Geykr5v5_8w9QO0hJi8jhV49_n58EdXhmB96Va27nTjm-gdMKoivcgp-ivRI-TKDfNPT7q5ChgOH3A5IhXSTMtvWyoEYO2xKSwV7GjhAyV6dE_CW2EYPT-f_U7bhlHXZjUjJnxjGgKnsAyyPT7AA2ep3jhjpsgsLIp2fzxn0q0cpkDRq4-h2Ed52OY6DLKZRk64C4uxlAaQuvEzJUZm0CXyqmEBlgG1J9dW6rSDXL2eZon5CMZ28L39twEp1TnXCNwyqM4akb8inL23lolcSkJ2x7lv7E9Xob0Ng25EgEu-OB31RJqoZcd7l1swAoOKrUahi85cy_unViLrdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکونام مافیا را سربه‌نیست کرد!
🔹
«مافیا اجازه نمی‌دهد به فوتبال برگردم» ۲۲ تیرماه ۱۴۰۵ جواد نکونام دربارۀ اینکه چرا به لیگ برتر نمی‌گردد این را گفت.
🔹
او نام از فرد خاصی نبرد اما حدسش سخت نبود که منظورش امیر قلعه‌نویی، سرمربی تیم ملی است. آنها سال ۹۳ زمانی که نکونام کاپیتان و قلعه‌نویی سرمربی استقلال بود به اختلاف خوردند. فاصله آن‌قدری زیاد شد که در میانۀ فصل نکونام از ابی پوشان جدا و به الکویت کویت ملحق شد.
🔹
البته اولین باری نبود که نکونام پای مافیا پیش کشید. او ۴ خرداد ۱۴۰۳ زمانی که سکان هدایت استقلال را برعهده داشت، در کوران کورس با پرسپولیس، عنوان کرد: «چندین و چند بار گفتم که نمی‌گذارند و نخواهند گذاشت که قهرمان شویم». استقلال در انتهای آن فصل به‌خاطر مساوی بد موقع برابر نساجی جام را از کف داد.
🔹
این سندرم البته تنها مختص به نکونام نیست. خود قلعه‌نویی زمانی که سرمربی گل‌گهر بود پس از باخت به استقلال در نیمه‌نهایی جام حذفی مقابل استقلال با عصبانیت گفت: «در این ۴۰ سال فقط ظلم بوده و ظلم بوده و ظلم». قلعه‌نویی بعدتر سرمربی تیم ملی شد و با ایران در جام جهانی ۲۰۲۶ حضور پیدا کرد.
🔹
یحیی گل محمدی، سرمربی پرسپولیس که تیمش در یک دهه اخیر اکثر جام‌های داخلی ایران را کسب کرده در کوران رقابت با استقلال مجیدی رویکرد مشابهی را پیش گرفته بود. اینکه نمی‌خواهند بگذارند قهرمان شویم. مونولوگی آشنا برای مخاطبان فوتبال.
🔹
حالا و کمتر از یک ماه بعد و ۵ روز مانده به آغاز لیگ برتر، تراکتور تصمیم گرفت محمد ربیعی، سرمربی تیمش را برکنار و جواد نکونام را به‌جای او به تبریز ببرد. تراکتوری که بی‌تردید پرستاره‌ترین تیم لیگ امسال و از مدعیان اصلی قهرمانی است و به‌عنوان نمایندۀ ایران در لیگ نخبگان نیز حضور خواهد داشت.
🔹
تیمی که حالا با حضور نکونام در فصل جدید برای سه جام خواهد جنگید. گویا مافیایی که او مدعی بود این بار جلویش را که نگرفته، برایش ماشین هم فرستاده تا به تبریز برود!
@Sportfars</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/455245" target="_blank">📅 07:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455244">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At9NN9y6G5ezfoJBBF9JqmtrvrTuxO73HbuqOMr_mtWkHFgigrlFl4_RfkgSQo7qxtHxEbtbODBQflibgOON41a199v96vWY8nw3VV3-dFBaYghifoHlTwRjNXb-RjXtdn_PHLVM1Uspsr8SY0UVivXSiUx3yJxY3GpnC8R6WjYnkdWyzplj9gIihl-NF5svgJFoWCn4F8QGJGjkUpVPbkARWRmE5uzb4Hahr__i5atm4SrTrVo-tEyTW2QXfCZ8Im2LeoJv3aH7llfV3kwxhgQ6ye1RKL9ODEQfA1SToPSEQj3f9NGCuKS423FrFCMKkzF6-MVa0YPW1-Ku5kccjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای تهران هم‌چنان در وضعیت قابل‌قبول
🔹
بر اساس اعلام شرکت کنترل کیفیت هوای تهران، شاخص کیفیت هوای پایتخت امروز روی عدد ۹۱ قرار گرفته و در وضعیت قابل‌قبول است.
🔹
طی ۲۴ ساعت گذشته نیز، شاخص کیفیت هوا عدد ۸۴ را نشان می‌داد و در وضعیت قابل‌قبول قرار داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/455244" target="_blank">📅 07:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455243">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlU552MF13UOY8WEKb81RLgzjgFEPL_z7_DrqRl5SpFh9WUj8dTIO_zm9LufcXjTkRN7bMm_B1NNhmTgZwcM5ukB6Ofk314lQTuWYMbMV96bnX5bsW9rHqW9TVGIOKZwwimDA9u1sNQIkBwJ8weNOWqlWKiJa9UI4Q9PmRJSDXCoK5j1V_wviahLjEA81TnVq2QhkFduVDZtoSyAvnJbfiR_LSOEHbqR0W8RuVZvdXPH2knCwtzN5PDCNFXo_hhcyaohRGlgGR_9GEY1xFmJeD6YOr-589HO2k-txr7X64HrfMyLAh9MyJfzYfmXA-2IB1Fc-VXAAKDDCtRGFTic1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احیای ۹۵ واحد تولیدی آسیب‌دیده از جنگ در استان تهران
🔹
قائم‌مقام بنیاد علوی: در چارچوب مأموریت بنیاد علوی برای حمایت از تولید، اشتغال و تقویت تاب‌آوری اقتصادی، تاکنون ۹۵ واحد تولیدی و اقتصادی در شهرستان‌های بهارستان، رباط‌کریم و شهرقدس به چرخۀ تولید بازگشته‌اند.
🔹
از مجموع واحدهای احیاشده، ۶۰ واحد در شهرستان بهارستان، ۳۰ واحد در رباط‌کریم و ۵ واحد در شهرستان شهرقدس قرار دارند که پس از انجام اقدامات حمایتی و رفع موانع، فعالیت خود را از سر گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/455243" target="_blank">📅 06:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455242">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حملات یمن به المخا ۷ کشته و ۳۰ مجروح برجا گذاشت
🔹
مزدوران مورد حمایت عربستان در یمن اعلام کردند حملۀ موشکی و پهپادی انصارالله به شهر المخا و بندر آن در غرب این کشور ۷ کشته و ۳۰ زخمی بر جای گذاشته است.
🔹
به گزارش شبکۀ الجزیره، شبه‌نظامیان وابسته به سعودی اعلام کردند شهر المخا و بندر آن روز یکشنبه هدف حملۀ موشکی و پهپادی نیروهای انصارالله قرار گرفته است.
🔹
پیش از این شبکۀ المسیره یمن از کشته شدن چند افسر سعودی در این حملات خبر داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/455242" target="_blank">📅 05:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455241">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خرید روزمرۀ ایرانی‌ها چقدر آنلاین شده است؟
🔹
نتایج پنج موج پیمایش مرکز تحلیل اجتماعی «متا» از بهمن ۱۴۰۳ تا اردیبهشت ۱۴۰۵ نشان می‌دهد ۳۰.۲ درصد مردم برای خرید مایحتاج روزانه، «بعضی اوقات» یا «تقریباً همیشه» سراغ فروشگاه‌های آنلاین می‌روند.
🔹
در مقابل، ۳۷.۳ درصد «اصلاً» و ۳۲.۵ درصد «به‌ندرت» از این فروشگاه‌ها استفاده می‌کنند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/455241" target="_blank">📅 05:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455240">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06fd67e16.mp4?token=D8i-7wcdWm7Xh2jx1x7qkf9ix1Pf-C0aV7440RWcA0g2FgIrqPVRVtgU7lGLnkMF4AaZ2Mk6IkrbHetoYBqG1BAtGbv-ZcjEkOvvlAjF5RKgwMbjGqxRSWme6pHzVZ9HhWMwLgp7oDqXKjYJQFr93DVfPKEX4RMWLz0oDfzJpuj57Pvd2MOOh8KXCrmG7hkA9jZp-9Du92Q1KUmF9G9hTUgFx43C4OW59JRU8t5Lsq_CVMbL_u62ejRzMncfCmvSjRbRp0k6i-_six4e1kdlF00X0GqCXy5bR-pUXQ-Nj4kdEgjHLls8qS_nMKwzEYg4OsYevBZNE2q5NM9qBCmRTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06fd67e16.mp4?token=D8i-7wcdWm7Xh2jx1x7qkf9ix1Pf-C0aV7440RWcA0g2FgIrqPVRVtgU7lGLnkMF4AaZ2Mk6IkrbHetoYBqG1BAtGbv-ZcjEkOvvlAjF5RKgwMbjGqxRSWme6pHzVZ9HhWMwLgp7oDqXKjYJQFr93DVfPKEX4RMWLz0oDfzJpuj57Pvd2MOOh8KXCrmG7hkA9jZp-9Du92Q1KUmF9G9hTUgFx43C4OW59JRU8t5Lsq_CVMbL_u62ejRzMncfCmvSjRbRp0k6i-_six4e1kdlF00X0GqCXy5bR-pUXQ-Nj4kdEgjHLls8qS_nMKwzEYg4OsYevBZNE2q5NM9qBCmRTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا از بمبی که ظریف گفت خبری نیست؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/455240" target="_blank">📅 04:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455239">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTmH5f3-c4pAkCmcSZKHeprASRVIIoOBTB6RWiRd6QJxwpJ2GozcYKXo_Ifne3KI_yI8VdYvh13VSnHM4BXHifbbZ67yo4XIQFf0OhfjXTcz8pcNaHVDfYDxccB5Dg2AsdodGfB5ej9jO6dy74IqADAAT07Fahl5RyGRjpJtqE_aAFJn67ZRUhaFz86_oLrtimBrl7g9LsPxBHR5PRri3KeEWFjJ_7t4VUJ6KBxw_4Y7iqfdslIGradAvKkPcfyHhRvfTnhMngN0XbPF_KiU7Y2kA6WDxiXr_Uq2W9d4vbv4fXc23-UsXTvl_iSOs2DqWCE7y7GYpWrRWtYv_wIb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ سابق ترامپ: اینکه ایران دست بالا را دارد واقعیت است
🔹
وزیر جنگ دولت اول ترامپ با بیان اینکه ایرانی‌ها اکنون دست بالا را در اختیار دارند گفت، رهبران ایران نسبت به موقعیت خود در مذاکرات و اهرم فشاری که از طریق کنترل تنگۀ هرمز در اختیار دارند، اطمینان پیدا کرده‌اند.
🔹
این نشان می‌دهد آنها معتقدند دست بالا را دارند و فکر می‌کنند در حال پیروزی هستند؛ و در واقع همینطور هم هست. این چیزی است که ما اکنون با آن مواجه هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/455239" target="_blank">📅 04:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455238">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تظاهرات گسترده در سئوتا؛ معترضان خواستار استعفای دولت مادرید
شدند
هزاران نفر از ساکنان سئوتا، منطقه تحت حاکمیت اسپانیا در شمال آفریقا، با در دست داشتن پرچم‌های اسپانیا به خیابان‌ها آمدند و در اعتراض به مدیریت دولت پدرو سانچز در بحران مهاجرتی اخیر، خواستار استعفای نخست‌وزیر این کشور شدند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/455238" target="_blank">📅 02:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455237">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حملات رژیم صهیونیستی به جنوب لبنان و فلسطین اشغالی
🔹
منابع خبری از حملات مختلف رژیم صهیونیستی به مناطقی از جنوب لبنان، و هم‌چنین مناطقی از نوار غزه در فلسطین اشغالی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/455237" target="_blank">📅 02:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455236">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYSGWjVowDwlA4gIfKgj-FryTjZ2y8IoD_ao4xNo9LWwEFYm8uPeV2ZbgNvhv_6Uy3RpMxVe0j1DRzO8XMZ_GKxcuBKW5SAQJAEWI-tD-Zd1SQXNS3qRorXJE4B_iz9releTF50LEGwlx5T8gcoI799f00_qZGtqG8hKo-ateH8n_KasPT-7XBtnTj6vG8K5CDCSQFwUg-VXv9gTjUx5EPOTrrhEdQFvvQWGwKkZrzZxWVungv82syHi4lbEMp8hh4O0dBkFITaZRJQ7wffkpYicZK4Tk3L5MMcbn1-XDKxSt8tfF2zGrDr0cWNtmkg3YOOIao-SkwHr0YgfknYGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: دولت با واگذاری بخشی از امور معیشتی تهران به شهرداری موافقت کرد
🔹
شهردار تهران: از دولت درخواست کردیم بخشی از امور مرتبط با معیشت مردم تهران به شهرداری واگذار شود. حدود سه هفته است با آن موافقت شده و رئیس‌جمهور نیز از این موضوع استقبال کردند.
🔹
آثار این اقدام ظرف ماه‌های آینده مشخص خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/455236" target="_blank">📅 01:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455235">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12bac62a0c.mp4?token=jaD9CylhOXYTyEsXq3rwUcmLe7nlybBi49OnO78enn_fqBBTPS2qYx9fiw0Gj_NANS954uA0cN1ZVso9uOFW1Afjtj792QVemCiAN9ggOYH7xDqlxF3gD_k3lqnuSEQn1jzlO064fg-magtHD6hrAZ-u2CP0K5BEhiDXGJ6gN0W9HF5R6akwodlkl5mw3D2rpvPwufDR0ah0N6rYOE8aFuKFulKOkY8pG08fkurDyHuOQuwWacaAsYeXxxT8z6DMnuJhhpcvfuZ037NIMc7gCVR0ue-2KxDj--YqOPxiXEYpP2iTSvyFoE1ozCl0QBwWOTB5VdcTVzPF5oP_YbbdpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12bac62a0c.mp4?token=jaD9CylhOXYTyEsXq3rwUcmLe7nlybBi49OnO78enn_fqBBTPS2qYx9fiw0Gj_NANS954uA0cN1ZVso9uOFW1Afjtj792QVemCiAN9ggOYH7xDqlxF3gD_k3lqnuSEQn1jzlO064fg-magtHD6hrAZ-u2CP0K5BEhiDXGJ6gN0W9HF5R6akwodlkl5mw3D2rpvPwufDR0ah0N6rYOE8aFuKFulKOkY8pG08fkurDyHuOQuwWacaAsYeXxxT8z6DMnuJhhpcvfuZ037NIMc7gCVR0ue-2KxDj--YqOPxiXEYpP2iTSvyFoE1ozCl0QBwWOTB5VdcTVzPF5oP_YbbdpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدوشصت‌ودومین شب خون‌خواهی قمی‌ها در میدان خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/455235" target="_blank">📅 01:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455230">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTDbnmD-OJn3GZ1Fx6tMygSldw26pjrz8c1KYkDyIvymgrzhOoDpUaKtJk5XJzeihMHXHOKjXRNN33_oWT6gLXWLqlQ_Bf7DH7pIiaRptLoEit3V_MFtAvoe_VjsMEB2413A-AQmnjrxYXAk3ZAHGj6qjSTAOHRY488XPBwZ4XmhaDQKwwOdo6tHRdQdd49OM3LAhSqqdnl0jcYSL8QFGrPpWQiE_4L8RlbyhFr_zybQRwpeUdFAe4acYU3Lto1bujWdGOQAygqQLctScLwSfKUk9mWz1TMj9Ybx7LQYogQOFHGxeGF47a4OlLksm4d6oFwW92lk_kkE69CENwsBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCeFxTKQIUWn3x7gIEgp9nhNfXKjgLqNs8tX-tnlWiTWcCTcA-VaOBjncPyH-XdMWQtb16rULXpUecO_Ym2ubfewoF6p7mtG30zBTeumakb7y95atrqYtQd_jCV0da7zQfhz7olTsYp2xXHgTVCq_QxW0MDxg4ScFDT9Bl7JAfxM0jDCbO4iT75L59XiJj81BQTZaLnOcwnNi6Bb5Dep2KN9lKPOlwlw7estNoxSQgX01GhDZhWk8TfYBojiyqhItlEwbXK3ssmO7nrtAn_uWimL2o3ySpucMTzUv0rEOePKYAsNbdwoYMQbUe8J5seNCIu-N8SjPaI3zSIscNXxFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyODLoVARjUya_llVdj9YRBFLiIc3HoVGAK6LF1Rm0G-ZTQL6GzaX63db0hOzMhLG1B4ljKLD3P-SbFIh8NAcs3Hdwhwijq6kgwEGRtYvXlvOchQem1BRJbh1v1MdsA8iwiY0_glQKppv9W4pe39K0W04BDN_Z8JGzDdh0FuplYMyWTof_CbvR0S6Mnqux_PJmOZrZd6xYukNM6edx8XJvJITKLlizDftZrxPOWuvg5bOycV_ttHYFSorc5a0AjSpwUiYBiee5BvTP5Y94G2kt-W30xyXsMMhhcAXE78cesNc5C6GZ3cZt8XB75IZmficOv4mIXrxQZQEYYSAcy-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9qMHXHF-qNHNyUzX0q_ALO5r5BOUcwUpiy4CTLnXBa8b6GbYGGiPlSVwEDsUf71u2M4H8U4D0XYrhLbh03MKvzNGixGZJ7P0VLUyFZ0GhPqnxa1Az4dF_0he8vY4erbPri1zPskKfqIGxFtd5_mmcPgdmuapHsQw38KFNoAra3TankSmXIjKxjnPfXc-5i7ciDOrafxabKAI5vESKvWCQp4PmGeFlvtj22oKExn-QicKFkR4rPNQmMSo2ju1loVO37iX3qCr-BZtQ0thYd66-n0dyFtbUgwNXqfn0QGfHR3kjmXv0e-QIqcWH3QdhYsc7mBKAdZNQKODTyBa4jKVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-mVsX4Kzwzv_zVdPdlQga9KxHyxv00UstRbYmc3kBzzSuMpZIgasuSTsqSn6hJaZ_GSGDpZ3DXiNi6ygNf6znE1k4EVT4pUCr79l9PO2063qxtJe6Sbk_tsKw9j3oRe4x-qpEtPjfKtGTKG_r_t2powdqt0aoVX6I-NZ9b2e1tRSejzGCUTPZaS4dH2ajqRzVVIpSc6T9lcyszPNJy-gOeyjtfu6uL8GTne1A9z6d10YlXIaz7_gqKmkUoemcjD_oL8RDOVTEvA4UeQBEKus_LAuV0QCh8QFKLaQpGDAAs0SRnO9zkSnxJ3x3uKd9-V8JgK_gZeXmLj-U2lGVoXhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱۹ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/455230" target="_blank">📅 01:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455220">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAfQ21tYb5h6P7VJ8CN_LcAyF6WI_oGHChRqJ5oKmcfpMm6TFZdpZjcVFGdHLBDdA6FnilKQMLrFYf5niFNqu_QEnNMVwfdrk_3ctoOpGL-dyYcUqaJbWD8sKn0no0TKeaDMmbh7aa9n-Wks5xT8zcPhw4NN87Yi5naz1LaafavvWn-e8A30fv7Sf5Nct4pTUTCuIrvXfDpx5kzTPIszInUrapKBGOUfyLqABj429jy36POHcJHRbboReDO1bvUxTsAIhPppEgae527ZKRKvwcNcu-Z_mp9D2tEiqIGnT9QhHc5NgwJYRrQqFoSBWckkJGxWiZK1cTZtLNzNRV_3cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LiXNzNM494DtTFeUuTeHUCa_icBJUWvVQz60AfeuHkRyYpShxnqSnBB0SEGwovQaAwCWm-q75RI4xJM8hI7JmLIZIa05_2PMzsNquvqHtngbjfJzybQsa7K6huQlchiCrXxHYUDBGHpi1SfVx_NMAjzf4OasBeM7LM0c6mPGDlNhXhrCXWgYifZP6LPPSEI8BQIDezCEawlrwTxynbG2sMsCesHy86FSFsOfrXfGijL9Fs-m17Cx49_wJwb6VNy9-R2sRCY2n8CH6bzRfLJodWaRSFxir1JlHciarevt7t6E3C_fyD7Zu0ZXzYxG6g3Ukq7--kETDprbrfU05jKllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcMJDnsaNOa-5uEM8X9XR6nyJmRyuH3AEzLND0xebMxxMVEtdxw7Bp9CqfR4XfBGwiWDVYp-Pbxe0xPIo26BiXr8pE5yzxJZGhv3DZnvhz7qISSVOUTwGEQr-tr0VGeD_L3MGeIs1xR4p30W6ZmvBIw6PMRTVQR85280rXFf30sAwOBIVL20Dun-8apLB03Dd030s9q_2Ii6-6bcq8XiBGCjCGNnKwvZ1OfkVLcOkV0mQvcYHYnZVZyqa0aNtEHr0xJwld56TSg-ywDOw946-mYX3e4WWRAbIx2Hlg3G-a7GZ_zM8Fx3eiTNqjPKfM-oj65dCSgvlF5Wbfz6QyGogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIgWo5aYfrI_gsYfxXeuFtxdW7K630Zq6CmwzSYHMDPWq2nwNKFnIRK88W1Nb4Qc47b72EO04tV5YWBrw_TMrI6OcN0PH9cX6ZUtjToBBpItm4ftRDEnk_x_TDytbKww7Vkl90B7ju1ovqphbnFbtanSR6QazBuIPcnrc8J7xX-X2OELQkPxghFUo2O2oWahOGnYMKsVluwdV3W8RkucUkkhQv_ulY7JXwbDYGOJVzLXbXnLPvXZqCvA5772AmTi5ElI_Ugt1g0elgGDSI-TPomeZLk5O2_fIDdJ7czDBEMQPZ7EWfxzzQ-H7CBXwxCIq1ePE1hNuXDIruDI1NrBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5wdRD5IoFUDAGm9OdpLhjm672IlvKGep4mOI7-bR-1g3a1XjbNKoOlZFx82dTdJDT22H-j-dMkOVlO9zpZtDU4ARNHL6L30z6gOVXcI7Tr7XRU2m52-nUIy1EW0inHA7eBmmx5vVAcuHLVpsTPIR79IP3lxn_vZI1hz4QLMKYp3AKzempBz1tbeW3mV1FCJ_o4QBnnDCJ2CMQ69zrF4T-ahShYkIP_xGbAfC67dEHIB1Sok98a0dxi8JsLM68aYJx1bBAA_4RHERQAXA3pFLL4aOh7NyciN7bw59ZVPXzEpqs29MaB1gkiFD-hywHMnqRd9v2wUl-OoX9q6X4IJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ixfbt1k3LrAgRVaJ-zNlY0-_JL7NjPRIiqEKr8ADdvESAnqR0KBPm2TsdFq93UqFrcK9s3xwWH0DEPLVcxpTQfr-lJalPLt_NcHbfI5ZLMa23K2Ecop7ifHtdieb2dlwT5gi8RbWrhEOAhnxeGFfB1dbWVvBPYsIEZ-BnBAik-SsL0z2EGBiHHvqRsCEm4maKJrB7oreTeqCnOQX7f_hqLZOlJPJOLluUMCvK-f_EHNnMunE3qmiEEL5l2mR7K4W_L9nDC11hbraA8KVBpftXe1yXAYGe6bs_VWqOMowY5twdTeOVISYL4WtvBmgH8gbOCKsz6W3Cyb3BvoWpBGOyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/klAP2vyzEDh7hJN0LH9wM1QJOTeLLyI6dlTHg7pKaIoxNVVCDt2VzflQHok5ajVY7j9rBor5sfcK_MGUvukB_1qM0D2Pe-N9hzAH57NL85783xEfmzI2KjSVplYeJxzKnh_e1emO2y8eeKA4fPonXxNa2KnCabkGTK3BIDTBrbesyvzLTDcBb-qDmcsBWnLPdgfbc_es4KOt73cVyS5C3_E4VXVxwssmWdiwXrNJ929m0wft-HumEnAA8YZzFBlKlPlkwUXUW-BZxHco0FIENq5z2bG7CyS1UWjRpmQc7-xVfvsrx7gsV5bxYMRUCm1eDEjUeWfe8Kk81Xwt1bjNSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xwq8YOhVi9_LwAVFFBFiKGPh0ydL9HWPxqeM3TCbVZeFUvanl1yIVVbjG7h4hiI0ZkBcPxHfm6MMmkcyWQftdWoskYpNLaM2fFpPyi5UY3HYmwWdV3x0n6Vz10D8BeReSQcgsd-ksxEL8T-BAS5dgsuEtcJXA9k8e-RWxiQJRLLyfcR7PTXTdiVWxaC5HV_MjpzGVtY0yCuFD3k4VDXDqA1-W9Lf5GiI50yTXUnqRJY9MK7BPufDWpqZ3rHteFGvTTuBUU_nRPANFWaGLQRBSoMQLxMQ_5DydUWnbE2EubxyGRK_GIanSTCKU2a8LwZP6xFn-giZMAxg09AxT1v7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAGw2SbF0SuQWxnT2nE11GRKF_G2yCt-ZJFyHMIDspHIjKwcM9BAEZ3PFB3JJrs1UeVSedVVkRES0O1eipghjvlyULm7d3tqA20XibJhUeo5CiUPxl19ASPtBekhKvJGJ8_SRiZkdb1uG7_X5ETMfQx5WQnlQtEEMj3TAPaEmCHcGdLsLr0KoGgHmsUfKE-BfM-H9eGe_7kYOtWbcdyCL4MbueiktB5IkRqQwNaDFT83yJEAaD86ZfkSPejeqADfM5w31-OlM6HEKw2v5oZ1OMEBHJMbgz_A_uQlYuJbi0-cQzPDukDYdMBrQX7O78oBXrZNsYzDTLCXsdsHQETokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_lGQ0srxJtCo_BHZEiyFd6zLESU5ElXGeGvM-KmVwOPgxXet_6TClqDSz7IKmUmSBwUbI9ujfZRKKa-fR3Fr7AmpW7zGB5-mGelf9qkvYgZr-meCmymuu8QDjrqv2E8tk14zg2FpJ-nDFeKQZOwzM2XGkMOGJiy-G4gnS6xnAzPDmjHbSu1L5ZnKWnqHG5JsVFaQheSd5MQIOFuUWkyfwBJgmOYdRmTYiseA4ZH-6JA6BLGarytNO-ZgKCmbmvRWtGSEce5qmM2K_IADViT0YjgECJ72FQmrVDUs-ROdUDplr0a2wD55RhhSQR3qGQ9ab910GjDdOjktNcsU1Mv0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/455220" target="_blank">📅 01:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455219">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee78c69f85.mp4?token=JTECXvJAvZw0jXqZ60VmTecT23ftpS_lFwYHOEvPhkDOlPwQjCAr_fXUKs81ZzHURliyGB9_LaoAAD0uS9nHeriGSPTiUMUBr7lxCP3HcDh3zL0zB3JRGc2rXDydYufYMFVvJ4MhNHh71GG1mb1aDmDCb6cp2FIuDQ2wb81QcFWa6foHWWCUw8KPqgwPI1rM-ug5rYEWFPBcWeeFqUocS-s3EqlliFnYV4ZpiBUu-hhqOh-CK1TVPD68hzNGHrwGyrTJATlfhnNCC-2LYALapgD92PlNmviSjFNH5Ileu_jvZInDiWMtGRtLNUZJBbQNL7OCIBfQ3mL-VFi0fS-lOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee78c69f85.mp4?token=JTECXvJAvZw0jXqZ60VmTecT23ftpS_lFwYHOEvPhkDOlPwQjCAr_fXUKs81ZzHURliyGB9_LaoAAD0uS9nHeriGSPTiUMUBr7lxCP3HcDh3zL0zB3JRGc2rXDydYufYMFVvJ4MhNHh71GG1mb1aDmDCb6cp2FIuDQ2wb81QcFWa6foHWWCUw8KPqgwPI1rM-ug5rYEWFPBcWeeFqUocS-s3EqlliFnYV4ZpiBUu-hhqOh-CK1TVPD68hzNGHrwGyrTJATlfhnNCC-2LYALapgD92PlNmviSjFNH5Ileu_jvZInDiWMtGRtLNUZJBbQNL7OCIBfQ3mL-VFi0fS-lOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخی منابع خبری از شنیده‌شدن صدای انفجار در نزدیکی تنگۀ هرمز خبر می‌دهند
🔹
شبکه راشا تودی گزارش داد، شعله‌های آتش از فواصلی دور بر فراز آب‌های عمان قابل مشاهده است اما علت آن هنوز مشخص نیست.  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/455219" target="_blank">📅 00:58 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
