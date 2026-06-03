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
<img src="https://cdn4.telesco.pe/file/JdMi9JV36DLpvEf5klHmupy0B3KUsp23BwKuBSo41U1KuiIAeOhyqPkeuzOydAcadUH9EbnNWkatbZbTHcSWhsD6OiKckGFcgdD2tTB4oOQCdxC5vL_8xBvkcsatyjQb54IV5E1sUUFvNlYqjl6X5T2jJ63jTG9PlC_tmLOvFM7nbPqEGtUApSw8v_fLZ02MQJUp_dqBkW79UI22_HcM4vR-6inq-0JDjDWDuFvtnbH5J5x-IuXYZrv7FK5Uc1ITRinyVRdJ8mmCgzc3aH9Ilqs2lZpv_MEg36nOiVwBLDX3xA7ObZ8KgNF0INAkKeRHxWtJrprEbyILGmcalMuOWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.01M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 20:54:24</div>
<hr>

<div class="tg-post" id="msg-655848">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
وزارت نیرو شایعات خاموشی‌های برنامه‌ریزی‌شده را تکذیب کرد
🔹
هرگونه تصمیم درباره خاموشی‌های احتمالی صرفاً از طریق مراجع رسمی اطلاع‌رسانی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36 · <a href="https://t.me/akhbarefori/655848" target="_blank">📅 20:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655847">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
فیلم چرت زدن ترامپ،مارکو روبیو را رسوا کرد
🔹
مارکو روبیو، وزیر خارجه دولت تروریستی آمریکا در جلسه استماع سنا مدعی شد: هرگز ندیده‌ام  ترامپ به خواب برود.
🔹
اندکی بعد تد لیئو، نماینده دموکرات: من به شما فیلم کوتاه نشان خواهم داد که اثبات می‌کند دقیقاً به…</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/akhbarefori/655847" target="_blank">📅 20:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655846">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHUdu1_r6M4d0gegNG-0yWmQA917FFTuIuH-kMLT9wflDehfIEVdG3ldtbuEl7W7yZuG9wGGK1KowiDtVsDCOwoBiXND2-qYz5Mea-TEIgSXtij_Dya3YUQRf9ixrybWcJ_GmLmGrvaVsIdl1qu0D5u88SnS-Y8zZTqUmOZj6n5HGmamhY7OIsCn6EJMJUkiXN8N8n0sCTFAxyzJi7a35pxp8XxPPt12xasHj42GEI2aaVwIWGH75AcOyYLviZAL5fRy492su4g-0LXVIkX5WqjYVjrMIp3i6LBDsKB-zV26krHBMBRcGteX7HWICU3pvrVIm4BdVvfvj658OrfjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
اعمال روز عید غدیر
#عید_غدیر
💚
مداحی های جدید غدیری رو اینجا ببینید
👇🏻
👇🏻
@Heyate_gharar
@Heyate_gharar</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/655846" target="_blank">📅 20:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655844">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای ترامپ: رابطه من با نتانیاهو عالی است و در مورد مسئله لبنان بین ما توافق وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/akhbarefori/655844" target="_blank">📅 20:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655843">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fcfa0d3b0.mp4?token=R1gqWEiwKtwUmQO-bN2B3TClcvdBjiLuX4cb-F8XVrGi-RkEfIOkDMvP7AtWjAK-qH9ddGkNgfOULtA6NqaFfb88SBG5q39DPe2rIb45FI2gtscfhbiB2lhZT5wg7GihSNdmSoCF_KNgcxPmbhsSfIX09OrK-BioO-X1YUlF8nvSNAcca-vC-B9EL1G_sYnacuwXfqGseuN4H7A-68GnSZ3vlD3sOuYzk2emJaiCdPOcaJkaOBxVaBhLCLWtgzQfkZLpV_2FOEU6nC3rJP6SouIZj04TekaOQp3MVsVo9Wxmj21bu7M8s5ADwKGehKdHcS9bOqllTZRaG_dPjnuE9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fcfa0d3b0.mp4?token=R1gqWEiwKtwUmQO-bN2B3TClcvdBjiLuX4cb-F8XVrGi-RkEfIOkDMvP7AtWjAK-qH9ddGkNgfOULtA6NqaFfb88SBG5q39DPe2rIb45FI2gtscfhbiB2lhZT5wg7GihSNdmSoCF_KNgcxPmbhsSfIX09OrK-BioO-X1YUlF8nvSNAcca-vC-B9EL1G_sYnacuwXfqGseuN4H7A-68GnSZ3vlD3sOuYzk2emJaiCdPOcaJkaOBxVaBhLCLWtgzQfkZLpV_2FOEU6nC3rJP6SouIZj04TekaOQp3MVsVo9Wxmj21bu7M8s5ADwKGehKdHcS9bOqllTZRaG_dPjnuE9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مغلطه نتانیاهو کودک کش برای توجیه وضعیت تنگه هرمز
🔹
نخست‌وزیر رژیم صهیونیستی در مصاحبه‌ای امروز چهارشنبه به جای پیشنهاد دادن راهی برای حل و فصل بحران تنگه هرمز در نتیجه جنگ‌افروزی علیه ایران مدعی شده که مسئله به گونه‌ای دیگر حل خواهد شد.
🔹
او در این مصاحبه…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/655843" target="_blank">📅 20:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655842">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b912394c9.mp4?token=vLfikQz-PIzLAcPDUILhhJ439xlzY2tKizuP3EcobtdZt95NwMzbKTdQ-qI09M05EcQcM07DYn61K-daMaFu1YnxZX9cJ4s30dsf6sZ5zJG5nLgqW_Leka4kzwI2syhr1r0M1NAap704ZrVD4TBlynhunFGXpTdfxj6MPFssvE-p9JmcqLD8rXe1KkaqaETaYj-IqndDz5i-99PXiPBOuVTfhQN3sKrInb4-9rbua6prXoUKfxjcAWelGY34qYR4qwhM0-v7f-qf_E3cpE95leNcuB2v45985qE1IJuTUXU51WtFPh5LSVw5wy2q_WckNpF7jsBciYVq2RwxzY212Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b912394c9.mp4?token=vLfikQz-PIzLAcPDUILhhJ439xlzY2tKizuP3EcobtdZt95NwMzbKTdQ-qI09M05EcQcM07DYn61K-daMaFu1YnxZX9cJ4s30dsf6sZ5zJG5nLgqW_Leka4kzwI2syhr1r0M1NAap704ZrVD4TBlynhunFGXpTdfxj6MPFssvE-p9JmcqLD8rXe1KkaqaETaYj-IqndDz5i-99PXiPBOuVTfhQN3sKrInb4-9rbua6prXoUKfxjcAWelGY34qYR4qwhM0-v7f-qf_E3cpE95leNcuB2v45985qE1IJuTUXU51WtFPh5LSVw5wy2q_WckNpF7jsBciYVq2RwxzY212Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مغلطه نتانیاهو کودک کش برای توجیه وضعیت تنگه هرمز
🔹
نخست‌وزیر رژیم صهیونیستی در مصاحبه‌ای امروز چهارشنبه به جای پیشنهاد دادن راهی برای حل و فصل بحران تنگه هرمز در نتیجه جنگ‌افروزی علیه ایران مدعی شده که مسئله به گونه‌ای دیگر حل خواهد شد.
🔹
او در این مصاحبه مدعی شده که کشورها در آینده به جای عبور دادن نفت خودشان از مسیر خلیج فارس راه‌هایی جایگزین پیدا خواهند کرد.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/655842" target="_blank">📅 20:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655841">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kY2AhOlct7Kt32doBOQ-SOepNseZINZ-MLKP-Cq6SrLWugdE0HtfXuq-DV7zjzomXVfZ-oflOqYjXWPn9dDcuAVueb48i1lzKaH56UZakB7agYSO2jxC3SBq5ec-WWnXYiwGjD5mwtKvWRZDKxcxqdMwI8JOxtiM7RQg6973fohgTQzdPEzbnH_uI67AeM3gpeNChwm2XHi6shZTYj3GMUErXf9Q51IoWG-HisklVkAckcs-pja5KjsJqbucKvg-b8mDtFQxlEAZhWO68Q3KPGyZxE9oEtF8cBDRCsnNpSVmTxYdgL3oQ-MaJ21FvxQkP50ObgJbsbREAgebtmKYng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه ۵۳ نهج‌البلاغه؛ منشور عدالت و مردم‌داری
🔹
این نامه، مجموعه‌ای از توصیه‌های بنیادین در باب
تقوا، عدالت، رحمت، رعایت حق، رسیدگی به طبقات ضعیف، توجه به رضایت عمومی و پرهیز از خودکامگی
را در بر دارد.
🔹
در این متن شریف، نگاه به مردم بر پایه کرامت انسانی و مسئولیت‌پذیری استوار شده است؛
آنجا که می‌فرماید:
«مردم دو دسته‌اند؛ یا برادر دینی تو هستند، یا همانند تو در آفرینش.»
🔹
در این نگاه، اداره امور با
عدالت، میانه‌روی در حق، دقت در رسیدگی، توجه به ضعفا و حفظ حرمت مردم
معنا پیدا می‌کند.
🔹
همچنین تأکید می‌شود که
رضایت عمومی
، اصلی اساسی در پایداری و سلامت جامعه است.
🔹
نامه ۵۳ نهج‌البلاغه، صرفاً یک متن تاریخی نیست؛ بلکه معیاری روشن برای فهم نسبت میان
قدرت، مسئولیت، عدالت و حقوق مردم
است.
🔹
بازخوانی این نامه، بازخوانی اصولی است که هر جامعه برای استقرار انصاف، آرامش و اعتماد عمومی به آن نیازمند است.
وَاللَّهُ الْمُسْتَعَانُ عَلَى كُلِّ شَيْءٍ
وَ لَا قُوَّةَ إِلَّا بِاللَّهِ
#حکمت_علوی
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/655841" target="_blank">📅 20:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655840">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xsi32tIKgcG-JdR-rM9n6_5VXMUqDhq1DA8X2ADzhXCivBLJuLZZESkNX4Fb2w9a066wzzliECrAfrLGEFXw_sD1GS6YEzgkbdHk5k5gRd2mcrgiUYYXRMBdqqO0ksUK5yDhogPF4xE5u_CyElOwMbUJaNrAI50bWz_RSIrLMtLe4u-bgVaOr372rLRTlfmnuNseCDow2jnWny95_41gfxpC5AwhtwgeBBnsCUX3g7hOf307qxlFloOwFqM27OKdguPgOpV1BDGxjPZR5hLQWSkJSqvZLI_QzPeqUFJGFWSv6kAVgMqXgYBczYvwOvM7ZJrm1rwYlUxTbhR9ycE-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غدیر یعنی سپردنِ تمامِ نشدن‌ها به کسی که براش هیچ بن‌بستی وجود نداره
#حیدر
#VoiceOfAli
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/655840" target="_blank">📅 20:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655839">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
قالیباف: دوران تهدید بی هزینه به پایان رسیده است/ امام‌ به ما آموخت در برابر زورگویی عقب‌نشینی نکنیم
‌
رئیس مجلس در پیامی به مناسبت ۱۴ خرداد سالروز ارتحال امام راحل تاکید کرد:
🔹
امام خمینی(ره) به ملت ایران آموخت که در برابر زورگویی و سلطه‌طلبی عقب‌نشینی نکند و امروز ملت ایران با الهام از همان مکتب، در نبرد با آمریکا و رژیم صهیونیستی نشان داد که دوران تهدید بی‌هزینه ایران به پایان رسیده و هر تجاوزی با پاسخی قاطع، پشیمان‌کننده و متناسب مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori
| Link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/akhbarefori/655839" target="_blank">📅 20:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655837">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3fCdyAE6t6v4T6Hl0XOF4w5lIjKEiaKXN-aSGJtcgyhFR6913vAIuQs4HPisp7R0uEy8AxVh9B7I1P8iGSuF_S_x9Kr1puyf2gW8nTJAHBDIc35MNnJasv_5-W2Y9yJD26o3szvYyI-7hobJx-Qtj4yqLCo12mhh-gNq7Ls3xvsYbQQ_Sht97V3q7Ev75jCOE9cPvK7M1bmSiIi8YE3Gm6gqpyh4MGNARPYyADO_eTROdls9fR38nc9HpTFo3vwZhvG7Ow_tO9jn9xVXadcqmwUm-j3tsoUe6TLb380hSjb_jp3kty3FZXP1Gmp5JccT5BcwmFeXE6pOkwAFDrRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vr4xFVcSyNdvhHvNnZTaVPdbMDTlin7tSGBN0_rMZoCOgpGbmaYUjXOKivpZo09Csco8gn9S_S8aGAHRc_odYe1Eht-VGlq9C7iXwhhPP_zbUb1L4WUSuHYBKNVSkrx6ws62Njs__GNs6hHdynx-Jiup_THDpkDNHRHBikEvvLbA59q8Bwc5jA3TtC8zKmkWS88ljV8Plj6b3U5Zkcd5YrDC-HfxALpiD08DcPqfUPQY88SCCe_BsaL7QDPx4DvZ-m_PZR18WqOlVv2fnngX5Jduk5IR5dXs4N5lwZ08e_9gIFD4mznceo06L4Oyz9T8auC5RXVD7_I_9wDBQgwTJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: علی از زبان علی
🖋
نویسنده: محمد محمدیان
🔹
شاهکاری مستند که نگارش آن بالغ بر ده سال زمان برده است و زندگانی امیرالمؤمنین را از ولادت تا شهادت، تنها با تکیه بر سخنان خود ایشان روایت می‌کند؛ سفری عمیق و اول‌شخص به قلب تاریخ، عدالت و مظلومیت فاتح خیبر.
🔹
«علی از زبان علی» دعوتی است برای شنیدن علی(ع) از زبان خود او.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/655837" target="_blank">📅 20:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655836">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای گروسی: ذخایر اورانیوم غنی شده ایران همچنان در همان محل پیشین قرار دارد، اما دسترسی به آن به دلیل خسارت‌های فیزیکی دشوار است
🔹
ذخایر یاد شده «به شکل گاز در سیلندرها» نگهداری می‌شوند و رسیدگی یا جابه‌جایی آن‌ها بسیار دشوار است، اما غیر ممکن نیست
🔹
برخی کشورها برای میزبانی از این مواد اعلام آمادگی کرده‌اند‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/akhbarefori/655836" target="_blank">📅 20:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655835">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGNlB1t8yNjaEW5oxiT3dW49lCQnpJRe6fj3qt-65q50dVNnLhqjj4HURRL2s5JLNrhE3_ISpgnvUvadok9eQRWwmR96GNxgx8viX81qZ4X2k1-s-Ea29oR7gBSQhuPvhn3slZ03PGt7TbbMnqkRXdlxOtR29UtwbP3GFeUQkRi6EUuOHJzG05Hr2bUuEdAGcSqxjtv0nXiUxSQg-NQ63_89N2oMsuSF3ADJkDn-gTx2YO2Ck3oL7uD0J9qJbPps4Bu3XG68PH90SyUxFg4l4TUar5ev0aU3UG70dIVUiffm1KGrH-CbgKAZpb3tN9g_Nk6NJ4kMCdKxphpUr5FaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خروس‌ها در سودای سومین ستاره | فرانسه آماده فتح جهان | چرا فرانسه مدعی شماره یک جام جهانی است؟
🔹
تیم ملی فوتبال فرانسه بار دیگر با نسلی پرستاره و ترکیبی از تجربه و جوانی، یکی از اصلی‌ترین مدعیان جام جهانی ۲۰۲۶ به شمار می‌رود. فرانسوی‌ها که در دو دوره اخیر جام جهانی یک قهرمانی و یک نایب‌قهرمانی به دست آورده‌اند، حالا با هدایت دیدیه دشان به دنبال ثبت افتخاری تاریخی هستند؛ حضوری در سومین فینال متوالی جام جهانی.
در خبرفوری بخوانید و ببینید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3218944</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/akhbarefori/655835" target="_blank">📅 20:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655834">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/914771dc29.mp4?token=mDyKlTnz1lSRHrhBlY5HuYfgX4KPL7yy4Umg-6RhIS7twTtobKoiMk-0fiXh4RYL0YCvLN8I7HR2xMn4WhSos_PmaaZ-9ihu641dDKG-LmKdqUDnORKu4oWq-SdIaURkz4O-qVNy6aZpF6U6iIAxVkj30E6xNvN3V5RDLWXF51nmFw-yM484uan96n8X-oA1EuPBk3kuz0RHxxE_2j29RT7YQBpqACiGfrebiNIt6b7u59OciDIUKgcpC8-CyKBtg9s7Ei7sC873TGqXJvtJd4z2WHcHsKJLngc3t9gTb3lHeSqcZDvoOA099ww0Lxyuj6MX5se5ogu1As2kQoiCRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/914771dc29.mp4?token=mDyKlTnz1lSRHrhBlY5HuYfgX4KPL7yy4Umg-6RhIS7twTtobKoiMk-0fiXh4RYL0YCvLN8I7HR2xMn4WhSos_PmaaZ-9ihu641dDKG-LmKdqUDnORKu4oWq-SdIaURkz4O-qVNy6aZpF6U6iIAxVkj30E6xNvN3V5RDLWXF51nmFw-yM484uan96n8X-oA1EuPBk3kuz0RHxxE_2j29RT7YQBpqACiGfrebiNIt6b7u59OciDIUKgcpC8-CyKBtg9s7Ei7sC873TGqXJvtJd4z2WHcHsKJLngc3t9gTb3lHeSqcZDvoOA099ww0Lxyuj6MX5se5ogu1As2kQoiCRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم چرت زدن ترامپ،مارکو روبیو را رسوا کرد
🔹
مارکو روبیو، وزیر خارجه دولت تروریستی آمریکا در جلسه استماع سنا مدعی شد: هرگز ندیده‌ام  ترامپ به خواب برود.
🔹
اندکی بعد تد لیئو، نماینده دموکرات: من به شما فیلم کوتاه نشان خواهم داد که اثبات می‌کند دقیقاً به کنگره دروغ گفتید.
🔹
این ویدیویی است که در آن دونالد ترامپ در حالی که شما صحبت می‌کنید، واقعاً خوابیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/akhbarefori/655834" target="_blank">📅 20:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655833">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwM0W0XyIumR3G1dys5hyNrLS6a6YsEh6rg__ZKDhtBjo4AED8HBbXqC8lwsvQpgSOYCofGSIyX8RcQsknhrXqf25JkoPJKuToQH7wHi9b6T00XuqUeS6oNeRBo5D8icTTBQuEEuy8COOgKSCzsfVqakkmzGrqYt209MajgsvSpFse0Fh_475EfGROCKzgtFAeqQxjpVm7iSchKlu5dGgaFVrdhxyjvtFiqNjljfvYtZP69pMZJCGEgIjseYFtL4vYzYXg2x2fWklaYhfx8dkbdMUNLyddmMlp3j3NUerjLM_dZN7S776fJT5A3-oizfOx3gIItVTpLA9MO2bDTJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بمب گوگل ترکید؛ شگفتانه باورنکردنی هوش مصنوعی!
🔹
گوگل از مدل جدید هوش مصنوعی خود با نام Gemini Omni رونمایی کرد، ابزاری که فراتر از یک چت‌بات عمل می‌کند. این سامانه قادر است همزمان متن، عکس، صدا و ویدیو را درک کرده و خروجی ویدیویی تولید کند.
🔹
از جمله قابلیت‌های آن می‌توان به تبدیل متن و عکس به ویدیو، درک فیزیک و نور، ویرایش ویدیو با تایپ، ترکیب رسانه‌های مختلف و حفظ پیوستگی شخصیت‌ها اشاره کرد. به بیان ساده، کاربر با یک استودیوی تمام‌عیار تولید محتوا گفتگو می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/akhbarefori/655833" target="_blank">📅 20:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655832">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a97ba8ff0.mp4?token=PfY0JgP4oIUx6r7w_oWWw17VNuAQfdYLzV5ZP5i3-L0Plp1MHr_glDx2iBSVDhUqH4j200Pp7Sn_vmhyovh6y4PXunzE1WSPCWJxWVcgwH8kR0NodO3PjeZsP8T0sMzZApm2KVVhWYw1wKCWdk8B_InpNJIWJmrJfE-Um4Z6eOMh814t9Pg_Ohq-I4FcB7sp79KCmsP_TWMTx2ZsjttCFuzf4sUBwIt62o3oRHI-P6csteJXyZNKT-wvJFBrrG0kiXAfqIyhoTdcU3PQ94VtSiXYj23zi3Skj42-PzjFVuVSlAcyl30v5sQU1KHsS7pTwyiu2aSJObTjKsHaUG6V-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a97ba8ff0.mp4?token=PfY0JgP4oIUx6r7w_oWWw17VNuAQfdYLzV5ZP5i3-L0Plp1MHr_glDx2iBSVDhUqH4j200Pp7Sn_vmhyovh6y4PXunzE1WSPCWJxWVcgwH8kR0NodO3PjeZsP8T0sMzZApm2KVVhWYw1wKCWdk8B_InpNJIWJmrJfE-Um4Z6eOMh814t9Pg_Ohq-I4FcB7sp79KCmsP_TWMTx2ZsjttCFuzf4sUBwIt62o3oRHI-P6csteJXyZNKT-wvJFBrrG0kiXAfqIyhoTdcU3PQ94VtSiXYj23zi3Skj42-PzjFVuVSlAcyl30v5sQU1KHsS7pTwyiu2aSJObTjKsHaUG6V-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی علی؛ تو به ولله تمام منی
❤️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/akhbarefori/655832" target="_blank">📅 20:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655831">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پیام تبریک پزشکیان بمناسبت فرارسیدن عید سعید غدیر
‌
🔹
عید غدیر، فصل باران حقیقت بر شوره‌زار مسیر تاریخ است ،غدیر تراز جاودانه حکمرانی مبتنی بر عدالت و کرامت انسانی است.
🔹
برای عبور از تنگناها باید به صداقت علوی و عدالت غدیری بازگردیم.
🔹
این‌جانب ضمن گرامی‌داشت یاد و خاطره بنیان‌گذار فقید انقلاب و بزرگ‌داشت رهبر عظیم‌الشأن شهیدمان، این عید بزرگ و میثاق مبین را به محضر یکایک آزادگان جهان و دوست‌داران و شیعیان آن امام همام تبریک و تهنیت می‌گویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/655831" target="_blank">📅 19:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655829">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgXFF9N88t1vSTNIclPPqHaIWEfkgBiNJ8o4olwwiPiThp1VFrrd4k_JReefNy3mKB5riJrdXV3kMAEZVwPfof5e82jhaQQmUKCaawgnbVUnTlIvhD6eGRqx_0etuNJyQHgxY1BF294FUnDQz-2wT9UesHGrrw0puxNi63vz9KAcowhtxRAskyNoOc618A6N7pntfSOwrHzfrspAa3ksiyG6DH-suBu--DtyenNunG1eSv3BCdj056u4miq8gHgVv35GOj8R9pU4Kt0El2NYaUNqiNI0rmxNiyRyyxPTfLraqGaWCJYF3Daebpw9vZtDjM5NGBlH5jxnvY-UnaYZ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف و ضبط محموله‌ تجهیزات خرابکارانه از شبکه بزرگ خرابکاری، انتقال اقلام نظامی گروهک‌های تروریستی تجزیه طلب
قرارگاه حمزه سید الشهدا (ع) نیروی زمینی سپاه:
🔹
گروهک های تروریستی تجزیه طلب با هماهنگی و هدایت سرویس های جاسوسی استکبار جهانی، قصد داشتند تجهیزاتی را جهت اقدامات خرابکارانه به داخل کشور منتقل نمایند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/655829" target="_blank">📅 19:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655828">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بهزیستی در پرونده قتل مهسا شاکی است / بسیاری از مقامات از بهزیستی فرزند می‌خواهند ولی نمی‌دهیم / دلیلی ندارد کودکی را از خانواده‌ای که به آن اُنس گرفته جدا کنیم
رئیس سازمان بهزیستی کشور در گفتگو با خبر فوری:
🔹
در پرونده قتل مهسا هم پدر زیستی او و هم بهزیستی شاکی است. بخشی از این پرونده اداری است که شما دیدید من برخورد کردم و برخوردم را رسانه ای کردم و همکارانم را از سمتشان برکنار کردم. بخشی دیگر نیز قضایی است و الان همکاری کامل با قاضی پرونده داریم
🔹
بسیار پیش می آید که مقامات در سطح استاندار، وزیر، نماینده مجلس و... از من تقاضای فرزند می کنند اما تنها جایی که علیرغم همه احترامی که برایشان قائلم، به سادگی پاسخشان را نمی‌دهم، فرزندخواندگی است. به خاطر اینکه آنها هم حتما باید از نظر کارشناسی تایید شوند
🔹
بچه ای که با خانواده ای انس گرفته، نباید از خانواده گسسته شود و ما هم تا جایی که قانون اجازه می دهد، نمی گذاریم این اتفاق بیفتد ولی در برخی موارد از دست ما خارج است و کاری نمی توانیم انجام دهیم.
گفتگوی مریم محمدپور با سیدجواد حسینی را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3219779</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/655828" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655825">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZ4s_Yrq8V9WdDKKooUzKjchMuMI4cfZUO8z102YEqKyrAL8bfDA1_UKOKa_U6M6ejA8ZSikV6D-B7SNhpAgQKzFlBLvz8jYSWzvk59t_sFUMVxHWTkuDSYAYWzQgRVBL3p2--cYClhI48qSfAmLRjqBFsz8wYGw2P3PmoMXPiEZAJ_i0fnM5bITEQIZF85y8HgiB0x27A5M8ZXunA1WWqAL_xzyCOX6pUV0vKERcGTu3tTFS20kU-g4Z1EuMQyf-A3ooJW8vf_NoZqbfSl1gwACnExOEM1XczODRsth2cPGWhkqSWgA0MRkCAcaFz-DBAb10KJwcuZtJhqVm5lYoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سند زنانه غدیر، روایتی که از دستان فاطمه‌ها گذشت
🔹
روایت غدیر از کم‌نظیرترین روایات اسلامی است؛ زیرا در سندی از این روایت، تمام راویان آن زنانی از خاندان پیامبر(ص) هستند. بیشتر آنان «فاطمه» نام دارند و هر راوی، روایت را از عمه خود نقل کرده است.
🔹
اهمیت دیگر این حدیث، نقل آن در منابع معتبر اهل سنت و تأکید آن بر دو حدیث بنیادین «غدیر» و «منزلت» است که جایگاه امیرالمؤمنین(ع) را تبیین می‌کنند.
#جرعه‌ای_از_خم
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/655825" target="_blank">📅 19:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655824">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه
بسم الله الرّحمن الرّحیم
🔹
با تبریک عید سعید غدیرخم و گرامیداشت سی‌وهفتمین سالگرد رحلت جانگداز بنیان‌گذار جمهوری اسلامی ایران حضرت امام خمینی رحمةالله‌علیه، به‌اطلاع ملّت بزرگ ایران، آزادگان جهان و علاقه‌مندان به رهبر شهید انقلاب اسلامی حضرت آیت‌الله‌العظمی سیّدعلی حسینی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه می‌رساند، برنامه‌ریزی‌های لازم برای برگزاری باشکوه مراسم وداع، تشییع و تدفین امام مجاهد شهیدمان توسط دستگاه‌های مسئول و گروه‌های مردمی، در حال پیگیری است؛ لذا شایعات و برخی گمانه‌زنی‌های رسانه‌ای درباره‌ی جزئیات این رویداد فاقد اعتبار است.
🔹
برنامه‌ها، اقدامات رسانه‌ای و جزئیات این رویداد عظیم در اطلاعیه‌های بعدی ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه اعلام خواهدشد. ان‌شاء‌الله.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/655824" target="_blank">📅 19:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655823">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای رئیس ستاد ارتش اسرائیل: آماده‌ایم فوراً به نبرد علیه ایران بازگردیم
🔹
نیروی دریایی نقش تعیین‌کننده‌ای در هرگونه رویارویی نظامی جدید با ایران خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/655823" target="_blank">📅 19:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655822">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
بازداشت ۱۵ شهروند بحرینی توسط حکومت دست نشانده آل خلیفه
🔹
وزارت کشور حکومت آل خلیفه در ادامه خوش رقصی برای عناصر آمریکایی صهیونیستی، ۱۵ شهروند خود را به اتهام آنچه ارتباط با ایران خوانده است، به طرز وحشیانه‌ای بازداشت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/655822" target="_blank">📅 19:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655821">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
گزارش تحقیقی نیویورک تایمز از جنایت آمریکا در شهر لامرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/655821" target="_blank">📅 19:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655820">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLsZa8ZNEjXQNECmgfpc1yZw0XEMBStaZ1kH8h4pKh6P7a5-5MejTZNvGDz4z_h-zTGy-RpOMe3StqufenByRCWU56HXAuoIXu5YRwLqWEM76K_iYDTxuEWNiAxerVub5zWcJGrTTFW9h8jglb6A3_8W3kKkRzJuH5JFr9HISvCs__Flks1j0NKPHCG0rDdc76nA0M0audVAdXqWAsSZaouCy80APFtuOVld388uLU_FZCGGHA9HBtbXcFbTuX0roviQPCzwa9RcUY3zNajhhoiNy6Q1UjESvM3czKIbcOWfVAvoCUQxoODFiTypFg478dhMyDWZQteOBgDzm7B2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار قاطع وزیر امور خارجه کشورمان/ هرگونه اقدام خصمانه با پاسخی فوری و قاطع مواجه خواهد شد
🔹
نیروهای مسلح ما در حال انجام حملات دفاعی در چارچوب حق مشروع دفاع از خود علیه مکان‌هایی هستند که از آنجا به ایالات متحده اجازه داده می‌شود برای حمله به کشتی‌رانی غیرنظامی و نقض آتش‌بس استفاده کند.
🔹
هرگونه اقدام خصمانه با پاسخی فوری و قاطع مواجه خواهد شد. آنچه تحریم‌ها و جنگ نتوانستند به آن دست یابند، با جنگ بیشتر نیز به دست نخواهد آمد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/655820" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655819">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
رئیس ستاد ارتش اسرائیل آتش‌بس با لبنان را انکار کرد
رئیس ستاد ارتش رژیم صهیونیستی:
🔹
هیچ برنامه یا تصمیمی برای برقراری آتش‌بس برای نیروهای اسرائیلی در جبهه لبنان وجود ندارد. ارتش رژیم صهیونیستی در حال شناسایی و هدف قرار دادن هرگونه تهدید ادعایی در لبنان است و از هر فرصتی برای از بین بردن آن استفاده می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/655819" target="_blank">📅 19:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655816">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnJ2Q__n6Wq78LU91Lb6BbgK1Wyl3cDvLg9pDVJSTmiBjCzeqISr-hFPM_YKM7Om9M0435hPFDIoFHG-dg0EE8kzHodh6MOC774Ll40uQV0BmUEsuApWM_MXFK9iRHY4iMDcNVFlt9Rxo3a76Lx33kqVcrm5911Sf51q0tJDWk4_BesuWjLNkOw1fhI7obDjBmP3h7zSsmu1n-JHVfTdcgYHKRW65tq6OAIzm3-0TrB3mp8dZciwF2DyDTK_Q4SCWT96Urtbv84NDz366qAYe26mjq7lV5AxWGvzNwlaE7XwC3iToZ5oDN0rhSsT5zt3FJNAQOfzHeJzJAFatbPi0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DASOXlQhuD8uEMWwUSI645ndSxjM34GwT24s-3z-SmcU5rlLjDJ2igIMeL_hdXVcIFjMDbeCSL5yNRob93ux7GXmknRa8oR5NZBOHw8WuI90nPTLYb_gPb0MPwoL1K8zXo-5jrivZm7jNcNxb_zUkl8w8uQHG3VteUoOMfpC3WLUFjKa4lGBEqppTJJ2vzJ99rPOscRPR6-_SMTCECjUBRBJsVLbOqdVc3jjWxySiJraGLCriM5nTl9TRIXHZeOax3GSlP6HcZ9u3qbeRzyPq63IAzd-yXGrBc2gkf6Y2ddOhQ4AoI6NAguTnUn91OiQHNRcsb_dKbTB_EnSGNp8Dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c78edaed6.mov?token=hEZ8DTyAYlS5jwYLsBd1ZY31Im4351jmyoEEmFfOIZt-sY4ruSPFUemyyKMiZcjvELti0Xee40R-YF3pdZ8rpntHQLiQJyDoV2WGCWMtKnUBi-3ZVivuXdIZendCC_QbnUYwx-I-L2nfU8hnp1iIUsBd030nlLURNKhatdpgqjTiIyl-rdAcxlt1-pmcPM51bqebHsSecEkjzPFI3kIV1wECSaZMizt7zkJbIWorRTQeuPx7EycBCtByu9PQFsTClXvad3D_VdpCQ-m_XPzjlRgZdmb5bgVue6b0mIUgnsDSYPkhCCJYei8PuPsACK6EzTUvAJEGF4YHN6DlAhNiSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c78edaed6.mov?token=hEZ8DTyAYlS5jwYLsBd1ZY31Im4351jmyoEEmFfOIZt-sY4ruSPFUemyyKMiZcjvELti0Xee40R-YF3pdZ8rpntHQLiQJyDoV2WGCWMtKnUBi-3ZVivuXdIZendCC_QbnUYwx-I-L2nfU8hnp1iIUsBd030nlLURNKhatdpgqjTiIyl-rdAcxlt1-pmcPM51bqebHsSecEkjzPFI3kIV1wECSaZMizt7zkJbIWorRTQeuPx7EycBCtByu9PQFsTClXvad3D_VdpCQ-m_XPzjlRgZdmb5bgVue6b0mIUgnsDSYPkhCCJYei8PuPsACK6EzTUvAJEGF4YHN6DlAhNiSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بنی‌باراک اسرائیل؛ غرق در فاضلاب
🔹
رسانه‌های عبری زبان در گزارشاتی از وجود چندین حادثه نشت فاضلاب منطقه بنی باراک رژیم صهیونیستی خبر دادند که زندگی هزاران نفر از ساکنین اشغالگر این شهر را تحت تاثیر قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/655816" target="_blank">📅 19:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655815">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای نتانیاهو: ما تصمیم‌گیری در مورد اینکه آیا تشدید تنش ضروری است و آیا باز کردن تنگه هرمز از نظر نظامی امکان‌پذیر است را به ترامپ واگذار می‌کنیم  #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/655815" target="_blank">📅 19:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655814">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtQhXvewtPQv8xncdULuZCqfwiiLqDaC2ul0Z0_R9dhuLPXVLhyyA6Sg-KQHTcdKXYz81dlhKA4w28PhpSn8rea0i0gtCsSarFL_HiEErH7ZIbjO762B8PUqQIeaMIC4EVQcQoMbn4RALKqzvyoD2PFs_o2YElKYZKxdHiNcUqAHC55NgPnoZkQ_XD1-RD8KMyTPnYKhUD4FFNsrlXMBsKpsAVNsaNAHvKXTjsRu1uvUR6Dquk2XxVNMIAdSsK5Cjh3rmja5TNv__TcFSgICCmQ0lpnckxhSogo7tkwvjnWhUvIwJWF14Yj_s8YwFT_3KYwPlMgnruSZz-unPBy-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
از اجتماع بزرگ غدیری ها در میدان امام حسین(ع) جا نمونید
📌
اجتماع بزرگ «ایران؛ ذوالفقار علی»
🇮🇷
👥
با اجرای:
مژده خنجری و آرش رضوانی
👤
سخنران:
حجت‌الاسلام مهدی طباخیان
💬
با نوای مداحان اهل‌بیت:
حاج محمد کریمی، حاج عبدالرضا هلالی، کربلایی محمد اسداللهی، کربلایی امین مقدم، کربلایی امیر برومند، کربلایی محمدرضا نوشه‌ور، کربلایی حسین ایزدخواه
📝
با هنرمندی خوانندگان:
زانکو، احسان یاسین، مجال، شروین معینی و سبطین غلامحسین (خواننده پاکستانی)
🔢
وعده دیدار ما:
پنجشنبه ۱۴ خردادماه (روز عید غدیر)
از ساعت ۱۵ لغایت ۲۲
👀
میدان آئینی امام حسین (ع)</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/655814" target="_blank">📅 19:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655813">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ec3c85c8.mp4?token=BCPXnqlEN9griAFvn2z3appJWwyHolRCs7RiXoNWA6ZCbUczrx7714P-3Xq9WMpwjuIpKve4hq0RuBiRwGR2WEmVbGXqGYXkFhRt3GtdaoWH9BdqKWPnKhuh-83D5I7vWSvwY9ATOqRLdHAlxXaaTItmCLHqeTUx63Fkb8ThyaLUhL9iKHjur7gkQPJFVVlismo-CpqHOCsueoYUKNZJN5SJScJR2szNx1B87adoNsQ54nSHCG8MyiiZ2Z5jk_j_92DLGL6YqdXb63W_zmivfW77J4HCeooTz8PIOjk6ORpFyVD8G28IaCgPyRN4niP8ryHJaAFuSG60veBoEg-u7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ec3c85c8.mp4?token=BCPXnqlEN9griAFvn2z3appJWwyHolRCs7RiXoNWA6ZCbUczrx7714P-3Xq9WMpwjuIpKve4hq0RuBiRwGR2WEmVbGXqGYXkFhRt3GtdaoWH9BdqKWPnKhuh-83D5I7vWSvwY9ATOqRLdHAlxXaaTItmCLHqeTUx63Fkb8ThyaLUhL9iKHjur7gkQPJFVVlismo-CpqHOCsueoYUKNZJN5SJScJR2szNx1B87adoNsQ54nSHCG8MyiiZ2Z5jk_j_92DLGL6YqdXb63W_zmivfW77J4HCeooTz8PIOjk6ORpFyVD8G28IaCgPyRN4niP8ryHJaAFuSG60veBoEg-u7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به جز از علے نباشد به جهان گره ‌گشايی
🌸
طلب مدد از او کن چو رسد غم و بلايی
🌼
چو به کار خويش مانی در رحمت علے زن
🌸
به جز او به زخم دل‌ها ننهد کسے دوايی
🌼
♦️
عید غدیر مبارک
🎉
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/655813" target="_blank">📅 19:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655812">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
زمان‌ شارژ کالابرگ خرداد اعلام شد
🔹
رقم پایانی کد ملی ۰، ۱ و ۲:
از ۱۵ خرداد.
🔹
رقم پایانی کد ملی ۳، ۴، ۵ و ۶:
از ۲۰ خرداد.
🔹
رقم پایانی کد ملی ۷، ۸ و ۹:
از ۲۵ خرداد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/655812" target="_blank">📅 18:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655810">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9QngcZY5p0JiJdAFdtf92ZuadxE4dnwUgr1_SBw6l_Z92BhnWwKveX5xt2uRJrQAMYo3iltBx1C1FdgItg8Swfv1VXejOkdU_SZTP7wNvnvL9YPVYKBXJs1rV1zdohewN5rBCTObnJ7sJ5R0m9tAcMzXDJbwNxXigVb1zQOlfMl4xLpBM5bbHANy-aqmRegTLGakDUE8MrWVJ8IM9qW5QKNN81Tik0by8BfwS9fqX-WdZ45_1NcoHn_ZltHpnyCDPFi0qDNKhKfPGJjA4XHLt1_HiV62YnGj4XUu-TyavApPHHbmUw8jn3p9yoxFYZ2EEinwXgvC2XKFuWv_M1fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابن ابی‌الحدید دانشمند و مفسر بزرگ قرن هفتم در ستایش اصالت فضایل علی گفت:
من چه بگویم درباره مردی که تمام فضیلت‌ها به او ختم می‌شوند و هر فرقه و گروهی، خود را به او منتسب می‌کند؟ او سرچشمه همه‌ کمالات انسانی است.
منبع: شرح نهج‌البلاغه
#VoiceOfAli
#حیدر
با یک کلیک به ویراستی خبرفوری بپیوندید
👇🏻
https://virasty.com/r/BWcv</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/655810" target="_blank">📅 18:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655809">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjk0f6gEtjn5uNeNglLqAf6SRnwLjVZMuBzgqPMjZXs_tUdpBuq-qCELtFvJDritlhp3Tylg3eHNm2p8Jqr4l0fWiAnyBh7z9FOGYRvgV7zsLpFoyEkhWoSrTSSLIK0_hJ4r211xynm3zB-z-FMlJoUshHWqNLWvkpzK_ZxIgxib2NyffwUhWrXwl1EpaynUocJeTeSsMhLypcbCfFouNYFhhp6-fs8Ntid4zMqulHAW74TB6s3sTzws3HAh-wSN9xmzdQ4svEmv2Tq45izR_NMx0lobRzNpXsyvkok36R4bhakT-tR1FS_fUyTVEEs9JFDV8yWKt17a2LQdqychIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«زنی در سایه» که از پشت پرده به شاه‌عباس دستور می‌داد!
🔹
تا حالا اسم «زینب‌بیگم» رو شنیدی؟ زنی که در اوج قدرت صفویه، مردانه‌ترین دربار تاریخ ایران رو مدیریت می‌کرد. اون فقط عمه‌ی شاه‌عباس نبود؛ بلکه مغز متفکر سیاست، مِهر‌دارِ سلطنتی و رئیس واقعی حرمسرا…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/655809" target="_blank">📅 18:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655808">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCwQgZnZYk4YkRELoOfqgjPxDM8Q7-CkRAqOdi4i-EOklibACuzvGzK39nXcx-ZMUuqHKMf-bRD6tP6DsJWMv-2yBtzOKin0TXnC3jtNTRp9-H7TESvGczt-yXpD4xRIRY5Tqe0tcQRk6jztXLoXdNMwld2YXqOccroX-yUTNajzHjBszAenHHhMOPE1LfS_OcGXQcLCRWjnW27aj38RXtHu_2vnceQzp7Ikkdtq8srOpZghqEi_lKC8PsUepdkIA7MS0tuv980jOPv57FktyKunhoWmQKPJC-LVKoSKUrnbCvrjR8HywppNPAk97XsQ_wmgzw_LMM-RN8ZL7X2Zlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/655808" target="_blank">📅 18:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655807">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
صدور روادید بازیکنان، کادر فنی و اجرایی تیم ملی فوتبال ایران  سفیر ایران در ترکیه:
🔹
بر اساس پیگیری‌ و هماهنگی به‌عمل آمده میان سفارت جمهوری اسلامی ایران در آنکارا و سفارت مکزیک، امروز روادید بازیکنان تیم ملی فوتبال جمهوری اسلامی ایران، کادر فنی و اجرایی…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/655807" target="_blank">📅 18:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655806">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bi0_hZcg2h3sQYrasXOJ3F1-JRFCtlLI3NJaWyHAf81CVKHSc66wborRkF5hqQ4_51XWFVJeq61N6E4KZaCAJ6Hr1tG01-xDclKIB8FgOAUsr1-iExRJwLFk0kbRtadGQcH2sLKdCYFwy_kx6xOCGQ6bCp_o4q4SQLo7F152Abjq42JxTsPeRPGXf9d6dY43GZAsAVSZOHrdiPOzdRhXv1IuX8G7hniyg-gaVtOi9BmhTwsBjavVl75VoSVvMxL52A70wVtk14SyLT2oZxB-o4qiRXsEkLdYnCVqfHBjmKxVZ-ImyVB7T-W4rxHc9uHNl1lyGSK1WhgiZxq7UtEt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌱
در پناه ِ غدیر، در کنار یکدیگر هستیم
🔹
در یازدهمین جشنواره مردمی اطعام عید غدیر همراه ما باشید...
🔸
با اجرای: مژده لواسانی و امیر مهدی باقری
🔸
با کلام: حجت الاسلام برمایی
🔸
با حضور: حسین حقیقی
🔸
با نوای: کربلایی علی اکبر حائری
✨
وعده ما: ۱۴ خردادماه از ساعت ۱۹ هم‌زمان با شام عید سعید غدیر در خیابان فدائیان اسلام(بین چهارراه نخرسی و چمن)</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/655806" target="_blank">📅 18:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655805">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM-95a_bi0Y1V-rzrbfMqb1riqL8Pd56L4zs9_X_3xa76DZ3tQputTnkQBRYS9F0nRLtUiazo6uK8VVUuoerYlKOzhucoEFqCdqYNldglMpqWPWxmRSt9oDNWt8MGtsc_KGPtaATHPVYR8EcalRQnnpICGtO6l3BFer9_gFK2in5tYFhlgYppM-j8sib2sb70Aq3FGDZh_pZgYJmBPKXBR2KfhK15pMSdx-P_oU2xIJYUOc6lpkvlIEZuArb1G7thbgh1b3Sy3qurTMtUnMWU_wM9IV4oIOYvKbLyW4e75WlQ8NMGNENh7K6piFxzpEpDZRHKmtDh9C6_A1U7eGfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین سفر پیامبر(ص)
🔹
سال دهم هجری قمری...
پیامبر اسلام(ص) همراه هزاران مسلمان برای انجام آخرین حج خود راهی مکه شدند. سفری که بعدها «حجةالوداع» نام گرفت.
🔹
مناسک حج به پایان رسید و کاروان‌های مسلمانان راه بازگشت را در پیش گرفتند. هیچ‌کس نمی‌دانست در مسیر بازگشت، اتفاقی در راه است که برای همیشه در تاریخ اسلام ماندگار خواهد شد.
🔹
در نزدیکی جُحفه، کاروان به سرزمینی به نام «غدیر خم» نزدیک می‌شد...
#روایت_غدیر
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/655805" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655804">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
مارکو روبیو: به دلایل مختلف درباره توان هسته‌ای اسرائیل اظهارنظر نمی‌کنیم
🔹
به عنوان بخشی از سیاست خارجی ایالات متحده و به دلایل مختلف، واشنگتن به صورت علنی درباره داشتن یا نداشتن سلاح اتمی توسط اسرائیل صحبت نمی‌کند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/655804" target="_blank">📅 18:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655803">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
نتانیاهو در پاسخ به این پرسش که طبق گزارش‌ها ترامپ او را «دیوانهٔ لعنتی» خطاب کرده: نمی‌خواهم وارد جزئیات شوم #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/655803" target="_blank">📅 18:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655802">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlCOWxGQdPD_oyd4hthbCIkySAdW4oZfI_Fu1WD3gCuF9c_4E488JppwtqyDKrQQE2DroiQ94T0Er9WJh69kpEGJ1EyPXQ-Y17PEV0reyN0CBxC0pMdZ1V7bbxiZrzoP_PUgqesHLyi1s8tlRlffUUHcLiakRCWWBPHFcN-1977aKLipddLsxaRanQb6D6x6j5NzxFbkIUfsFof7mNZRakhgCQkR5VomAQaT1cD6vY_Nnxc7Wvj3fJ44TV0LXgWA0YHjH1F08u5DkDs2ntTFV1SCtmB5Pbe0-x1JLC3cnHBVZwwxEhv9_t_XlhZzSgG595r-Ozl41arldID7Yg8EWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده یک باور رایج | آیا جام جهانی فوتبال قاچاق انسان را افزایش می‌دهد؟
🔹
با نزدیک شدن میزبانی شهرهای آمریکا از مسابقات جام جهانی فوتبال، هشدارهای همیشگی درباره افزایش قاچاق انسان در جریان رویدادهای بزرگ ورزشی دوباره مطرح شده‌اند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3220187</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/655802" target="_blank">📅 18:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655801">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
مارکو روبیو: به دلایل مختلف درباره توان هسته‌ای اسرائیل اظهارنظر نمی‌کنیم
🔹
به عنوان بخشی از سیاست خارجی ایالات متحده و به دلایل مختلف، واشنگتن به صورت علنی درباره داشتن یا نداشتن سلاح اتمی توسط اسرائیل صحبت نمی‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/655801" target="_blank">📅 18:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655800">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
نتانیاهو به سی‌ان‌بی‌سی: بسیاری از کسانی که اسرائیل را هدف قرار می‌دهند، در بیروت هستند
🔹
با ترامپ در مسائل مرتبط با ایران موافقم و گاهی در جنبه‌های تاکتیکی اختلاف نظر داریم، اما به راه‌حل‌هایی می‌رسیم.
🔹
ترامپ معتقد است که می‌تواند مشکل غنی‌سازی را با مذاکرات…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/655800" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655795">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVZ1Ypx3LLTZ_6t-7G41VpWZwO4A35y2zQW975s_3BO5GswLcIg1omXGj71u1Y9EmsWbYuFDXOCUsqyCfRW5MAC8xcLZKlpjO9lMFmzeqH1P-qOBrgdLFjSXWgwwRhId7OEs-AOILG1BJUcM-xFIAJSMMDsaVJGxCMjlTQcQFaPeFi23vfpqVbWCwmsCd4kVrfXun47h0xgSQmquk2powPLZ_chzNVlnYeuMdq2pFoLsIwYwICrHIJqXE6E_XnEpzOD-mGThB1A1cH6n3Dg8YSmsXpPlRAAYKD7GrY4QhtR8M-wNnCHuuLpKBXe-aXYPQ95T1krMaLBZK6Z2XoDZxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbRKwDYq-akTmEAzMcP1NC4BaZWE6tmUm9sieWZpr7cJ2krBeK1463NJZ7f2uYMJcivSnPzBXBwaMXu7ZndMo6uH4W0DjtCvttmmvp8XXA3cCQ7XoX3uCj91qSOTnAarvVxGbRtJDsySXhvKrESTkrqF_5_A23SidkCx8fohzaGZMqSEhCFan4cyF_9fV4RCI7Bsh7WHqBZnEYVkjOEydLCjNy8oP_yPuB3lDU-sb1eniTO52kqbsDv_R9DBQkwtNXmcS2FLyfzB-zdKdfzHrwVgCAAUC-z8e4smdXJt_dmAaTvaAXscyNk-JJpK50D_aINUtoIyRvgwq_bfGgT4jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YaQUda6d-n2t42d82JF0wRZwAKAH4b5hwnxrRfQ5VYXfUrkUFzbmtzCU8OEua7jF82wAmTxz1KfF9edwceZNbN5yePhiulI6sWlOt1iTa0IVcQvSi9FdO3RAKouD89W0-2AXrmrFjuqZLZ23KqGJC1XCiC80YwY8nhS6sFSoCg6uUoQgu1IHRk2MTV5nRikA2vD306PVIDLQqwp-x7YKuVoVoH5dCOXL1oddsv31w3CSQlql-5Q5VL46jF2UyBDNOT3C9dsuFIYtc6cBCYPDm0iQDlkFFfes76xJc_SOQsE9ImPfZCTacY24gxT6l_jUMxVyikLFkmuZwiuCq1rmhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAQriaLlJwoHsskIsHaa_flgBKja1L9JmqUUEQxT4GhnNNqrnplzVaLS4X0uKsAlCglP8S29XLaVWKW21rXHhGnnWskg43wTz_em6F7XCofj-JhhZAmq0Sx3lN_ytmPPMB1MopiGgL-mX2rNCVkD8XYXD2uMY8jI9ZOZdYx-_jnxetINWJ4ISF-y5nsORypJv5ym1MDRPiZwSRzb0dyOcXWlOIOuhrQOBVGAXOB8PLJ2XFWF-Tm837JzsWTmpjK40n3Ts9wMqwlnnlKzwKPHamk-Lh5aJO1WfERckdOTkuLwMA4T_fG6TMSvGzaJUPPKOGG1FRQHhx2aPlU2TSMbxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eHilnmhZb7yiQEHEWMviYFv3XLM0quD6eawq7zOjLtoYsQa6XMjU-sghN9N5kJ2BEIIjAWa5OCsVxWiACPfLYdThhtslYjzCGOL017AdouQP7qTdpJD7cs1mObWNcVsz1n3e1Wb6DGdXnMB3uPWnXmYVRszcSXqvIFwzPSn33YwXJqXsVRAMi4yqvqK3alADai22cPSVdr-_48AajAf0JhXNyFWds8MA7gMwW8ezPbZ6hU_VqEqp4r-PWVc9zE7VkFZpD1f7KhXLltme37OnD7DIiIIU6CEDmh97z-gUB74eUwyUIFpyrzun5YAwx-OsRKdlzlXqMkakg5_oUWW72g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
استوری تعدادی از هنرمندان به‌بهانه‌ی عید غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/655795" target="_blank">📅 18:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655794">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ee6adbb12.mp4?token=koEkTzyZgZDdnUytqWrxjAI5neFwc5WE7_We3fT8aEzK1j2o2I4Pr6p73dtFmBSRvB_V8BEj3jv9cxoHM9eZrZGWqaVK-b70cxNil5AlzBuNzXeuYMPe6fuGAZH7a4yQ8bEX-mSHL-bwEqF1Mo6eTOR4Rp3GT9b8HR2FA7SuCqva7IbLfNaxF7cfsjDyXTAbHVp37raitPKYCOAmbPC9R2ct_cWr77PKg0EYZ-4qQp4x934jA9t_x_xxQPYvQoQXghzUo2ul_5FZkGX9cTYDzBPVfODijOBE8Fx7QtrDKVznFDx6xt04NdEoUrXEAGCc3Wae2q4__DFt_Ms0dePBEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ee6adbb12.mp4?token=koEkTzyZgZDdnUytqWrxjAI5neFwc5WE7_We3fT8aEzK1j2o2I4Pr6p73dtFmBSRvB_V8BEj3jv9cxoHM9eZrZGWqaVK-b70cxNil5AlzBuNzXeuYMPe6fuGAZH7a4yQ8bEX-mSHL-bwEqF1Mo6eTOR4Rp3GT9b8HR2FA7SuCqva7IbLfNaxF7cfsjDyXTAbHVp37raitPKYCOAmbPC9R2ct_cWr77PKg0EYZ-4qQp4x934jA9t_x_xxQPYvQoQXghzUo2ul_5FZkGX9cTYDzBPVfODijOBE8Fx7QtrDKVznFDx6xt04NdEoUrXEAGCc3Wae2q4__DFt_Ms0dePBEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محدودیت های ترافیکی مهمونی کیلومتری غدیر تهران از زبان فرمانده پلیس راهور تهران بزرگ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/655794" target="_blank">📅 18:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655793">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10db4c8596.mp4?token=V8P9SVrter9ygCnj2i28u0x-Fm40yNC6EX-jzO-6eq_ZnWT3ArrMrM-b0wohiF8X-0SyIe7eKXOPSkjeCUuf-bT8ypJUimVqoBDOT7EiwKbP6JDkENp-EPBB8Q7Ru2PIo9mRB7R9zehISODKNEG9DkwRFWV_-asfO0adaYXOElOwIpwX6a8pZnhrtYj_qag97kz1A0oTCuccZHzW9rzPUJX8xroEiNhroTqosgKM7q2ezhkMqLFGHOKsjsRRCcAIlT0H3EWFz7PBnqtx_UOUYvSZMUikQvDzN-7QpNlgk59WhV7bXZI3CaSWpsecj8JRG2unF62kgfNzxGwddmgxADuG5x75Agsu95vFKSMFyBvLh3d9TcyPdTsEFzvrc91Eqf4wNfg4zAHFzg1vGQ4dkQoEc2VjbI9qNph4W4EEBpgbTTnHacnEz6MLLHgmfwRQoJpIJsuc6MgCKpsEkkzjpLB23Ik8vlSWcG-qBS7FpnnQR3nuoVX8P4hLKkklFqjGeY0i0XrIBHK_iYSEIFxOeENzWoxi6EK-06hKK74bysYvXFmENQU69YMhsX_c7Lhd9jK4AXpAtS4RRqkxVyTV7H3J5jN28Xjq-TncUnG0S2_WKjfTQFed9xdaUDZdh0f_dM1pUxmY-oSYJUIAy6-3WDwe6DPsmipHJ1BNCWG-_4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10db4c8596.mp4?token=V8P9SVrter9ygCnj2i28u0x-Fm40yNC6EX-jzO-6eq_ZnWT3ArrMrM-b0wohiF8X-0SyIe7eKXOPSkjeCUuf-bT8ypJUimVqoBDOT7EiwKbP6JDkENp-EPBB8Q7Ru2PIo9mRB7R9zehISODKNEG9DkwRFWV_-asfO0adaYXOElOwIpwX6a8pZnhrtYj_qag97kz1A0oTCuccZHzW9rzPUJX8xroEiNhroTqosgKM7q2ezhkMqLFGHOKsjsRRCcAIlT0H3EWFz7PBnqtx_UOUYvSZMUikQvDzN-7QpNlgk59WhV7bXZI3CaSWpsecj8JRG2unF62kgfNzxGwddmgxADuG5x75Agsu95vFKSMFyBvLh3d9TcyPdTsEFzvrc91Eqf4wNfg4zAHFzg1vGQ4dkQoEc2VjbI9qNph4W4EEBpgbTTnHacnEz6MLLHgmfwRQoJpIJsuc6MgCKpsEkkzjpLB23Ik8vlSWcG-qBS7FpnnQR3nuoVX8P4hLKkklFqjGeY0i0XrIBHK_iYSEIFxOeENzWoxi6EK-06hKK74bysYvXFmENQU69YMhsX_c7Lhd9jK4AXpAtS4RRqkxVyTV7H3J5jN28Xjq-TncUnG0S2_WKjfTQFed9xdaUDZdh0f_dM1pUxmY-oSYJUIAy6-3WDwe6DPsmipHJ1BNCWG-_4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیعیان اندونزی در حال تدارک برای پیوستن مهمونی کیلومتری غدیر با نام ali day festival هستند.
امسال مهمونی کیلومتری غدیر همزمان با ایران و مهمونی غدیر تهران در ۳۰ نقطه جهان برگزار می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/655793" target="_blank">📅 18:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655792">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
نتانیاهو به سی‌ان‌بی‌سی: بسیاری از کسانی که اسرائیل را هدف قرار می‌دهند، در بیروت هستند
🔹
با ترامپ در مسائل مرتبط با ایران موافقم و گاهی در جنبه‌های تاکتیکی اختلاف نظر داریم، اما به راه‌حل‌هایی می‌رسیم.
🔹
ترامپ معتقد است که می‌تواند مشکل غنی‌سازی را با مذاکرات حل کند؛ من فکر می‌کنم باید به او فرصت داد.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/655792" target="_blank">📅 18:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655791">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
نیویورک تایمز: کنترل ایران بر تنگه هرمز به اهرم فشار قدرتمند علیه ترامپ تبدیل شد
نیویورک‌تایمز:
🔹
ایران با در دست گرفتن کنترل تنگه هرمز، یکی از مهم‌ترین اهرم‌های فشار خود در برابر دونالد ترامپ را به‌کار گرفته است.
🔹
سپاه پاسداران پیش از آغاز جنگ با برگزاری رزمایش با سلاح‌های واقعی در آب‌های ساحلی خود هشدار جدی به واشنگتن داده بود؛ هشداری که تا حد زیادی نادیده گرفته شد.
🔹
پس از شروع درگیری‌ها و کنترل تنگه، قیمت انرژی افزایش یافت و این موضوع به اهرم مهمی در مذاکرات درباره برنامه هسته‌ای ایران تبدیل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/655791" target="_blank">📅 17:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655790">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
امکان ثبت‌نام دانش‌آموز نزدیک محل کار پدر یا مادر
🔹
وزارت آموزش‌وپرورش در دستورالعمل جدید ثبت‌نام دانش‌آموزان اعلام کرد فرزندان والدین شاغل می‌توانند در مدرسه‌ای نزدیک محل کار پدر یا مادر ثبت‌نام شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/655790" target="_blank">📅 17:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655789">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUePi68wseYUmWxmjnhhe7qZZZgMe5vvYuEdV5sfgK80HP8GzDjD3CJjemJjc-SI3mFj9cxhg2KrDxtM2U65mJxAy-KSAGKlLioRUwOuKa45zGniCg2U3NTABqxxngYT-Zyft8AiGU8moRGhWVv4hOncZGJ3EUxPpIBKaE3s_QZEot9v9Ef-xZjmHPm5RIlGFPAelPgKFRf87WDajo4i8fx0epIFTAGZ779xyZsQB45PNK8qfXt-oSxnVCf5VYzQFg_0xmloMhxAJ8wwFuDq7NS97GX2Bmmk1FOnfWS_VCPs1ddiiT0HVYn8tDzVnK4-tVh9tJG6o-wNYVSzP7nubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاریکاتور متفاوت «کمال شرف» هنرمند یمنی درباره یک تروریست متوهم خودشیفته در حال سقوط
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/655789" target="_blank">📅 17:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655786">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YE-d99EtPSJWX_Y0WlqUBVYUWPLaRLX0ALl5fv8wnl5DUa6PiB3Lwr6-oE0C_lOuNSsClbhovLWb5HaHR-ESeMyTRA3n0Qkgw8nPFWQCjs2l9kzfmGf2Lp4gqDxb8punGA293raApInxAyIcpA0IK1E0RQbCRieootenpbgqUdYmHq1K4zdAyfLSSAmGhCLG5uK9BaqjQd1mVX1CA8UAKgc8N6zaha4rQa9sAG2ZUSxE-wFnBde5HvtGJ3A6_bupk676CdXZmjID_gz0ggjiOs0CJHwKZS0FBRkVAHj0Aavhec-PepbXNMTybPqgnfj3uJNRuR48vLkj_nUIoaQ02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2aiAMl4T6lebnAWFISAf5nvFnkullbKnRgeKesyb8E9lldQdV3hB4_DCKJJAUyjyxkDWknjy66TELSXBoFACpX2wA-JuL6D-DobL4fW4vi313oT9hbbQQtRFscCHDGXbdIgzzwF_aOkJbLQbHApYevGmuS4W_oXbZQBvXUGs7jnKw8i1-NVMpMlwiJ9aTWvl3CX4cQ8_cU5xyLuBil9vnnJ3gkYlemO6Zg6w50Dpc7-CqMgyXMgn64JuK283IqioI9MgFLuh9_gLN0N9_qnoEhAXlNfhJUBrUbpx4QC1dfg5yvgAv6Y_mVfwx3MhBE5HnQNCiS7G4OeQ94pjk7VFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KxP46RW2LE_lB8YtAy0D-LouxgvdZKTLtOtp0ZYqJ-gStXZAgcSkFgELpnCOOcZdZvmmKnhV5vXVAJRirgOsgn9z0ljhmRedwsUpn8OM4HRIhImhtkqvE6oXVvfnOMsM8WmCpW0dfFEg1h737k7wkOGeoLzKZ29wj8MtvUmHZmJY3O07kYM4QzXYjyk_5oxNCzFx92g5yu1W1Yn-P-HAH4IgcTdWFMgWijX9VA2A5C5hRqnPQs4TTMVaaV1_BbVdnqO_x2M2P_dRmLYyVInKAsaOXLLSFO4PF_wyib6-HGA3JjFz-6oDepZ5osIY3bh9fnNrLClyN5AyoGA9Mg4hHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا هیچ ثروتمندی پول نقد نگه نمی‌داره؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/655786" target="_blank">📅 17:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYaKKfekaX4Qo0qalkT_4tJoIc6zRJGPQQwUHaPonsxE-I55p4OOXzjFhH02vyu1SIv6JGNiPjHbMCkPMN06ouMdUfX7ncaGQGcUqhXtn37PeNRFeHiXx_gNu6eWucQKybI5_20VwKuOkuaGXoE1wYCgtjkxrptZzkM5LYkgPRqRkGxCG-lKBhk0kNm27Uno5HrBsdbrimAST3XpmyXnoCf8K-PgxM4azVUUNVHtkbaJFeyxqbiu8vYZK5Sa-kbNcyi0y3PLgm7KUXG3Bm6n8g9rUUdmye5n1atmzY-Ygk2yKtj-SjB2XF_H_m0d5p5-CCfttBtFSXXv6OgJqNb_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بارگیری نفت همچنان در خارگ ادامه دارد
تانکرترکرز:
🔹
یک نفتکش غول‌پیکر برای نخستین بار در ۴ هفته گذشته در حال بارگیری نفت در جزیره خارگ دیده شده؛ با وجود این نفتکش‌ها و مخازن خشکی، وضعیت ذخیره‌سازی این کشور در شرایط بحرانی نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/655784" target="_blank">📅 17:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCCSIslMfG8j6Znzj9DnKYxg-yYW8VcwdGqIYmxfya2g8vHe6pRTLn3fMXrpCsNpaizfDlkQY8xGO3kOtsEi8F7cHnPOg6-o8EJ-Xsl-8NzAPtK8YYgIuVVm3m1-DGBaBKtPConbCUF1qlTl2qtgM81hN8y-GnpfsIZptCYI7RNNlvOwndIalb-DaKbnVM3OdGNyaJVrBwMCqXuhyx08-yiWMdwwYGIfaC-ucUH2bRy8QUbubXlu3Z5Gnv7mt5HtFUjncrHcq4_QA2l6vkDeGPqMLjzua7glmElvJ2QtTngPMHqHPS6bpKtzVkN--lsjY-Ijbe6wFyLgVy0qeVhUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محل کمپ ۴۸ تیم حاضر در جام جهانی
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/655783" target="_blank">📅 17:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naV4WbwvRCeNBKY9HMa2ZpaBKMs6VdjKPsbAMGYMKgjac1DbZRyOcFb-BklNuKSCpwIZZRxaKoAn43BeJR_zk74qbOkNVHK1FmxDTbbp7QgrfI7slM3gPwJSWAw32_6c02IZF7PaNdm2gJWDo76CML6iH59drLm2ftMI425amqvrWv0Jyb1XqMLNpUjwn2BL8oSd_BE_pvuXRN9ArdOb3w7bhCnVzBOVBH1Mqvk86aokwapit32rAoq04ecfkgcH3dwTu5p5JSCSbwt_0HgHhqc8g8_ZAHXX4ulBQ9_NutJp-6wC6t0rAhDpSdVG1QQ1dcy-JVTOp9hBmtEPgONiQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهدید تحریف
🔹
یکی از مهم‌ترین تهدیدهای پیش روی انقلاب، تلاش برای تحریف مسیر اصیل آن است. برخی می‌کوشند در کنار ریل روشن و معتبر انقلاب اسلامی که بر مبنای اندیشه‌های امام خمینی(ره) و رهبر شهید انقلاب ترسیم شده، مسیرهای جدیدی مبتنی بر برداشت‌ها، سلیقه‌ها و تحلیل‌های شخصی خود ایجاد کنند. هدف این جریان‌ها آن است که نقش بیشتری در جهت‌دهی به آینده انقلاب ایفا کنند و مسیر حرکت آن را مطابق تشخیص خود شکل دهند. در حالی که انقلاب اسلامی دارای مبانی، اصول و چارچوب‌های مشخصی است که از سوی آن دو امام عزیز تبیین شده است. فاصله گرفتن از این اصول و جایگزین کردن قرائت‌های شخصی، نه یک اختلاف سلیقه ساده، بلکه تحریفی خطرناک است که می‌تواند هویت، جهت‌گیری و آرمان‌های انقلاب را با چالش‌های جدی مواجه کند.
🔹
هفتصدوشصت‌وششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/655782" target="_blank">📅 17:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای اسرائیل هیوم درباره شرط واشنگتن برای اعلام توافق با تهران
اسرائیل‌ هیوم:
🔹
واشنگتن از تهران خواسته پیش از اعلام هرگونه توافق، محل ذخیره اورانیوم غنی‌شده را مشخص کند.
🔹
بر اساس این ادعا، آمریکا همچنین اعلام کرده تا پیش از اطلاع از مکان این ذخایر، محاصره و تحریم‌ها لغو نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/655781" target="_blank">📅 17:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تلاش مسافر برای باز کردن در هواپیما در ارتفاع ۳۶هزار پایی
🔹
پرواز فرانتیر ایرلاینز از سن‌خوآن به شیکاگو پس از آنکه یک مسافر تلاش کرد در خروجی هواپیما را در حین پرواز باز کند، دچار هرج‌ومرج شد؛ این فرد مهار شد و هواپیما در نهایت به سلامت در میامی فرود آمد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/655780" target="_blank">📅 16:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655778">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlZDaWbWU_nuSJulZBl6wRuAEQF-pi_8kieT-IMEaaVbcJasdH1AFBVOapxeaoklwY0UnO-FkEPCzct8S9dcNYxlt0LsytTFCLa8fpoQCO3i1DsyArZ0JGiEgg6bVhY6qFThTfIAfIE7HCU8MNLaqY5bGzdLv5_JtEuaE7bUzQ6hLcPs232wVdCT_dht4jK8VSpGQEqwseJM_DiPXMZatqQo1QTjpR8we4kL3KY3JSnzcaK3gxcakruMfmoogP4Z4ej7DEoU-H2DRL0SPqeW0-7ZE9H6vGY3MzJBMHESVoqxr6_vNe0rZ5Qk03seoorp1o3dXvlstdkiTj2x01_qCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غدیر را روایت کنیم
🔹
امسال شما راوی عید غدیر باشید؛ عکس، ویدئو یا حتی یه متن کوتاه ارسال کنید
💚
🔹
همین کارای ساده، حال‌وهوای عید رو قشنگ‌تر می‌کنه.
#فقط_به_عشق_علی
#LiveLikeAli
شما هم به این پویش بپیوندید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/655778" target="_blank">📅 16:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655777">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFveDJNGtw4L6n_FdWmWrclf9XgTJWVWUfW-OAYkW0fKmQbw19kkBz25HiQ8UsODCdsoRiUKeVMbUfpxOnmNppjFdu_x1JTnjsm36Q9MGi0Lxw1MW99a1zkKW1osuMXdPEv-M1reqBPlN842VxTKdxnB4-mjRGqDLR3z8Mye4Nh1JgQkm-YU87P7A37yFvhkYPxG8GIGnYjeRZVGQAV9Qjg_Y59BJQPANMxdtjZAQvJpw-IuGU1zxRyqPCfD1kH8EvqVqXvWoWShbYbyy_fUEkcxgNJbKooQfF3T-nHctsGo17gz7Es_8JoCARV-YiVCQ6XaBfeRsUt8cSBAUG7rbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دکتر طه حسین نویسنده و متفکر برجسته مصری در ستایش زهد و پایداری علی بر سر حق می‌گوید: علی پس از پیامبر، نمونه کامل زهد، تقوا، عدل و شجاعت بود. او هرگز به خاطر منافع دنیوی از حق عدول نکرد و همین ایستادگی بر سر حق، او را به شهادت رساند.
منبع: الفتنة الکبری
#VoiceOfAli
#حیدر
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/655777" target="_blank">📅 16:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655776">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
وزارت امور خارجه کویت: کویت کاردار ایران را احضار کرد و دو دیپلمات ایرانی را به عنوان «عنصر نامطلوب» اعلام کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/655776" target="_blank">📅 16:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655775">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6001bc8056.mp4?token=Do5fOAeZhtWFupWv3oqHo7QA6inp11CGgtJFgdnb7uMWiddqj5yIVQXmGe5Jr6Yz09w5WOVsVYedgiFGY6UT_m6EnjkUQ4-jc7fojpj-302ETtV4Bv-LhAjIYkdiujtXhLbSRskRL0N5VSpsQm6lAD3u-lN6A7Y1bLE7GYvriBXxKZWedIdCHIJyCIwa5zHZH-62EkbEEUBBvBZxawA9Kb1DHh6PqptrnPbDHCb88092v1_IfwWQQn2dljJLOBu536c70erGKPWeGT_OWuUUd7C50ZoU7c923zLz8pvTkMIjEyu-7iP9gPL_OT0bDOlYgr-vgYyiTFuEA_Hrng1Cug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6001bc8056.mp4?token=Do5fOAeZhtWFupWv3oqHo7QA6inp11CGgtJFgdnb7uMWiddqj5yIVQXmGe5Jr6Yz09w5WOVsVYedgiFGY6UT_m6EnjkUQ4-jc7fojpj-302ETtV4Bv-LhAjIYkdiujtXhLbSRskRL0N5VSpsQm6lAD3u-lN6A7Y1bLE7GYvriBXxKZWedIdCHIJyCIwa5zHZH-62EkbEEUBBvBZxawA9Kb1DHh6PqptrnPbDHCb88092v1_IfwWQQn2dljJLOBu536c70erGKPWeGT_OWuUUd7C50ZoU7c923zLz8pvTkMIjEyu-7iP9gPL_OT0bDOlYgr-vgYyiTFuEA_Hrng1Cug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوتید به بزرگترین عید تشیع و مهمونی کیلومتری غدیر
به یاد امام راحل (ره) و رهبر شهید انقلاب اسلامی
فردا از ساعت ۱۵
میدان امام حسین علیه السلام تا میدان آزادی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/655775" target="_blank">📅 16:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655774">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0d107b53.mp4?token=bYHZ8I44TwmZTLggHRTgF34fCEIn6MmKE0jTaH72pyFkmHK6hfJTBIcRnGdXQD-FGivl9o0iAOrg1r6-FS39K1tnoDwLEssnXS5wrWgBX6vjPht0P8vc4uV7Fq9WyzH2iYbr-iofsHwOAexy9b861XILE7hogD5-LJdBm4bm9BSU1-HkxhL1VZnz596HsD2VMSUKnosr-KBqnJBbohb8-OIRJ4rEZmUWsDByi5OwedzZDgR_PsSblHnnDtBdoBzd8vYGeQNMiddzwPe7LyFkWli0OH0jnJnJUUGqdvLt2O-rxMAAXULEeshaDyPJPYgqHvxnGmFnQe0ehqCO0xa0Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0d107b53.mp4?token=bYHZ8I44TwmZTLggHRTgF34fCEIn6MmKE0jTaH72pyFkmHK6hfJTBIcRnGdXQD-FGivl9o0iAOrg1r6-FS39K1tnoDwLEssnXS5wrWgBX6vjPht0P8vc4uV7Fq9WyzH2iYbr-iofsHwOAexy9b861XILE7hogD5-LJdBm4bm9BSU1-HkxhL1VZnz596HsD2VMSUKnosr-KBqnJBbohb8-OIRJ4rEZmUWsDByi5OwedzZDgR_PsSblHnnDtBdoBzd8vYGeQNMiddzwPe7LyFkWli0OH0jnJnJUUGqdvLt2O-rxMAAXULEeshaDyPJPYgqHvxnGmFnQe0ehqCO0xa0Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش تند پلیس آلمان به یکی از شرکت‌کنندگان در تجمعات حمایتی
🔹
برای دیدن ویدئو کامل و جزئیات بیشتر کلیک کنید
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/655774" target="_blank">📅 16:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655773">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5371cd0bb.mp4?token=sk_SSigBVWEWn8-v9og8OzDbC3hnQ_90dd3PP4U47BYuAvBcnFIgaJgPG67kted6ADPUdPTVsfWjC2KoBaHMPEQASHKtd1UrcP3_NH8XDttyhWHX6N_IyF9bFj-YI48ZnlHodR7UeWiBmXws9n7Fuugd0OFuhMFv5oGGnOVOSPNV8TWZD4pboMnzkiBHN3U9YAaY1wImz-z8gEUgFJwyE3ekcoQjLohjmZNeALjuPTMQgZVeLNpiI6s09QQBsVADaQem5SVwNlJfhBMva7iP_NJ0Kflg7inKZ1HfRCowxz8cQQsJb39xSd7Dl1HLDyyg44FtE1YZ46GiOAKZff-SEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5371cd0bb.mp4?token=sk_SSigBVWEWn8-v9og8OzDbC3hnQ_90dd3PP4U47BYuAvBcnFIgaJgPG67kted6ADPUdPTVsfWjC2KoBaHMPEQASHKtd1UrcP3_NH8XDttyhWHX6N_IyF9bFj-YI48ZnlHodR7UeWiBmXws9n7Fuugd0OFuhMFv5oGGnOVOSPNV8TWZD4pboMnzkiBHN3U9YAaY1wImz-z8gEUgFJwyE3ekcoQjLohjmZNeALjuPTMQgZVeLNpiI6s09QQBsVADaQem5SVwNlJfhBMva7iP_NJ0Kflg7inKZ1HfRCowxz8cQQsJb39xSd7Dl1HLDyyg44FtE1YZ46GiOAKZff-SEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آب زاینده‌رود به اصفهان رسید
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/655773" target="_blank">📅 16:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655772">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
آمریکا تعهداتش را در قبال متحدانش در ناتو کاهش خواهد داد
فرماندهی ناتو در اروپا:
🔹
دولت آمریکا به متحدان خود در ناتو اطلاع داده است که مشارکت‌های خود را در ناتو «تنظیم مجدد» خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/655772" target="_blank">📅 16:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655771">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1GcZpTWAp05sMfem6_JPwWPi1KLMzd29xw_nKCOkRiMIYF_wiHn-LDyjS8LU4G_2FyV6YZQK7VgVYblYA-5vDYIt5jEmsKdT7kncNlMrbRecv-LrSpC0VQXBBwYsv-21vtiNcsfqNkQ2uw70jP2cNRsBEqbJb2K2C4XbKVQwqPpYxyX_SvaqL5qYlvPbCcIvBprO2lobKL2mrqKiaSm_kPgOgNTYvmAiKlGSUXGpU8KXXjLWXRFPUuqUKBI04EWaKendixPWENJ8fPhX1Bwktxx6dTnMInVndFEkAMaOmuSW4WrgXJZ22xUnzwJTBRJ8AYNPnAFuN-uy-LneWfVIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاریخ جام‌جهانی| تیم‌هایی که بیشترین گل را به ثمر رسانده‌اند
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/655771" target="_blank">📅 16:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655770">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPYhrhiHUEvYrURT5i3FnMOaQ8FeHAN6DGI9kW-L1pOvW8Y-BhLU6uPDLUTPlyLh-8TeL9pCf9vv6Bsepl0CUjRVd-5OPhC8L_rNwzQeAkwERoHOULQNL3hbWnGI1wznMRSLD_s0x0BTditBqShHHiPlYQgEJgFAJ5juHQvPblloaVFUR417G92CdZvBUcNc1F5q-9JG_EWP8i1DBaMpb93d4U0HCxubJKDokDh8wQB--RflcOjngr1W6qOR6Ix-212rMc3qQm0tg4FwsJK3grME1WUIG3ffu-WukGLlFj-5UJeiJPD0meXryp-GPfnZtG95V0sgeAfnoQyEBX0EJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شایعه تجاوز به محمدرضا شهبازی تکذیب شد
محمد امین میمندیان، نویسنده پاورقی و دوست محمدرضا شهبازی در
#گفتگو
با خبرفوری:
🔹
شایعه تجاوز به محمدرضا شهبازی، خزعبل و شایعه است و کاملا تکذیب می‌کنم.
🔹
محمدرضا شهبازی بدخواه و دشمن زیاد دارد و اسکرین‌هایی که دیدم در خصوص این شایعه، همه از یک پیج منتشر می‌شد.
🔹
شایعه‌ای که بیشتر آبروی او را هدف قرار می‌دهند را پخش کردند و او به این شایعات و تهدیدها عادت دارد.
🔹
این هم یکی از تیرهایی است که انداختند و به زودی رسوا می‌شوند.
🔹
برنامه طبق روال در حال پخش است و امشب هم منتشر می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/655770" target="_blank">📅 16:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655769">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
گردباد نادر بر فراز آتشفشان کیلاوئا
🔹
گردباد نادری به نام «پواهیوهو» بر فراز آتشفشان کیلاوئا در هاوایی دیده شده که بر اثر گرمای مواد مذاب شکل می‌گیرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/655769" target="_blank">📅 16:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655768">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQShhL8HyCch0VBpL3-4dJdKcIK8uU1F1GJzBg2l5L381J-BKTPgknZi_KUXfyxYmpx5uRjUpqdr6CiiMeS-wtKR9Fdgs_fK2fSlZJvA51fq0mrGZHg1RSZpQtDm_SNx0VBGFvQPLKEXf5-xc8ynACZeyshhj-PQDFaBozdGkAE8NHNLveZjPX2H2gdQAJ67HDsugjCdDcvgfGRpEGTxQ0j9mu6ldGSi_HPMgEsi65toMeqqEdfK0mPPSbooeMno9kLKZOjW8eqLw4nzZYkywzJSaix5d_zXH_PgjZXm9ee7R8Gdu25_F-SHsgoxrfmp6bsnm2zENWh_XqfHNS6xlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی هوش مصنوعی به انتخاب هندوانه هم می‌آید!
🔹
کاربرد هوش مصنوعی فقط به حوزه‌های علمی و تخصصی محدود نیست؛ گاهی در کارهای ساده روزمره هم کمک می‌کند.
🔹
یک کاربر از هوش مصنوعی پرسید کدام هندوانه بهتر است و نتیجه هم ظاهراً درست از آب درآمد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/655768" target="_blank">📅 15:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655767">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYa3DUf2O732BJBF0mlguTXM4LoMJXgPRY2gzvvxU1IfoozqUrliQWmzlsNw9VsuJ6PkWlFV0wUzaB-vYhVjoXzseTY7vynXsnB_3nkkRh_4ySeT7agI5HOBea5d3fuNOl_Tvm9FVACVAyG2F6C2ILlT0_meiuWZDgYEUPcfaPkNIDB2xmxu36Eq9lYn619txqLo4gpbYblJ0H2L9M5n05BXsvYdF2a5aIWHRuBj0Ka0BC7wztDtL8L7p229rxWuXSxr1IZvthwPpvP8hoqY0WBTo4Gbv-hKA19F6tNB8dNJhdihV1nt1SMaI-XNwiHwwAmxB0lUCRkWhtuRLc-k1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
تسهیلات ۱۰۰ میلیون تومانی غیرحضوری در طرح افق۲ بانک رفاه کارگران
🔹
بانک رفاه کارگران با هدف تسهیل دسترسی مشتریان به تسهیلات قرض‌الحسنه و توسعه خدمات غیرحضوری، طرح «افق ۲» را ویژه اشخاص حقیقی از طریق سامانه فرارفاه ارائه کرده است.
🔹
در قالب این طرح، متقاضیان می‌توانند با افتتاح حساب قرض‌الحسنه و ایجاد میانگین حساب، بدون مراجعه به شعبه و به‌صورت کاملاً غیرحضوری، تسهیلاتی بین ۱۰ تا ۱۰۰ میلیون تومان دریافت کنند.
🔹
مبنای پرداخت تسهیلات در این طرح، میانگین حساب مشتریان است و متقاضیان می‌توانند میانگین حساب دوماهه خود را از طریق سامانه فرارفاه مشاهده کنند.
🔹
این تسهیلات با کارمزد ۴ درصد و بازپرداخت ۱۲ ماهه پرداخت می‌شود و تمامی مراحل از افتتاح حساب، ثبت درخواست، پیگیری و پرداخت تسهیلات به‌صورت آنلاین انجام می‌شود.
🔹
در طرح «افق ۲» فرآیند تأمین تضامین تسهیل شده و بنابر ضوابط اعلامی، وثایق شغلی و هویتی از متقاضیان دریافت نمی‌شود.
🔹
سامانه فرارفاه از طریق
پورتال بانک رفاه کارگران
و همچنین فروشگاه اینترنتی کافه بازار در دسترس مشتریان قرار دارد.
@Refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/655767" target="_blank">📅 15:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655766">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
اقدام عجیب صرافی‌های رمزارز خارجی در مورد کاربران ایرانی
🔹
شنیده‌ها از برخی کاربران ایرانی نشان می‌دهد تعدادی از صرافی‌های خارجی، حتی برای حساب‌هایی که قبلا احراز هویت شده‌اند، محدودیت‌هایی مثل مسدودسازی دارایی، تعلیق برداشت یا بررسی‌های طولانی‌مدت اعمال کرده‌اند. به اعتقاد کارشناسان با این روند، انتقال دارایی رمزارزی به صرافی‌های خارجی گزینه امنی محسوب نمی‌شود و می‌تواند ریسک‌های تازه‌ای برای کاربران ایجاد کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/655766" target="_blank">📅 15:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655765">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbrpifyJTXA6x869wdSchGUxTAfqa0_Dac-e5Umh9UBd7B3BOTnCA0q9fSS8mpumpdLAZH8jNZGE9fIX-hPj-QKu917vdTc4HgASJlsfpjhLv49MryB6RJdl4rvLsYLclCf0gkp0jXMKjhNjGdvwNXQoEF8TYzXNfmxqfQwR-u8mTwb7Ve4O8VmVD9erAjAWN0n-sTu14ZV77-1hgtWdGwEyPwNuWQ5zQqX8wYPok1oqI-vEOjuOZs-Ns4YE5GI_8Aas46qYhiz3etNaKnVI6iwZTu2xXXWtv49iGqC8cFMh0Htzpu0gSq_VQUxTHhKwOf7-fmQXkZCYtOwNlwoTyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ارتش کویت: ۱۳ موشک بالستیک و ۱۷ پهپاد رهگیری شد
🔹
همچنین یک مقیم هندی جان باخته، چند نفر دیگر زخمی شده‌اند و خسارات مادی قابل توجهی گزارش شده است.
🔹
در پی این حملات آژیرهای هشدار پنج بار در طول روز به صدا درآمد.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/655765" target="_blank">📅 15:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655764">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای کویت: ۶۳ نفر در اثر حمله ایران به کویت مجروح شده‌اند
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/655764" target="_blank">📅 15:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655762">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
صدور روادید بازیکنان، کادر فنی و اجرایی تیم ملی فوتبال ایران
سفیر ایران در ترکیه:
🔹
بر اساس پیگیری‌ و هماهنگی به‌عمل آمده میان سفارت جمهوری اسلامی ایران در آنکارا و سفارت مکزیک، امروز روادید بازیکنان تیم ملی فوتبال جمهوری اسلامی ایران، کادر فنی و اجرایی برای حضور در رقابت‌های جام جهانی ۲۰۲۶ صادر و تحویل شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/655762" target="_blank">📅 15:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655761">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1018e153e.mp4?token=FZzPV_JI8sjxYUjSbksF1dl9fR9qhQeGZITXNTFij-OwxSWeWttl_0u391aEOLPO-GOz195xQce4YTu_3NysnvZsYXGl-MqRcuO3XlDrP1_adS8N5Gep6OGhUs5ySkRPhXHt_q6jngryh5ajUFBNhwRWUxKwR8_4jwP5mXygUXvHzjsNuGEvkRPT9kVEVuw8JALz8OQim_YbxEn8W7XQj2WeEJkQ74FyGggX2vrsVblHI4tNW35Cd76UrKjZgS_Rjs-UMl7pTVmQaJhiYsYki0N-sz_ulT-1ttrzM_4Q63yrmW5t3nZpasWCQMKBqNGYEbVbTPJFg82HJEmOTP_LUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1018e153e.mp4?token=FZzPV_JI8sjxYUjSbksF1dl9fR9qhQeGZITXNTFij-OwxSWeWttl_0u391aEOLPO-GOz195xQce4YTu_3NysnvZsYXGl-MqRcuO3XlDrP1_adS8N5Gep6OGhUs5ySkRPhXHt_q6jngryh5ajUFBNhwRWUxKwR8_4jwP5mXygUXvHzjsNuGEvkRPT9kVEVuw8JALz8OQim_YbxEn8W7XQj2WeEJkQ74FyGggX2vrsVblHI4tNW35Cd76UrKjZgS_Rjs-UMl7pTVmQaJhiYsYki0N-sz_ulT-1ttrzM_4Q63yrmW5t3nZpasWCQMKBqNGYEbVbTPJFg82HJEmOTP_LUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات دوخواهر از خانه ای در محله حاجی‌آباد
🔹
۲خواهر ۷ و ۱۵ ساله در سنندج پس از تحمل شرایطی دردناک، با دستور قضایی و ورود اورژانس اجتماعی از خانه‌ای در محله حاجی‌آباد نجات یافتند.
🔹
بر اساس گزارش‌ها، این کودکان توسط پدر و نامادری خود در سرویس بهداشتی منزل محبوس شده بودند و هنگام نجات در وضعیت جسمی و روحی نامناسبی قرار داشتند.
🔹
تحقیقات قضایی درباره ابعاد این پرونده ادامه دارد.
#اخبارفوری_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/655761" target="_blank">📅 15:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655760">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f95f4785.mp4?token=vY-LqPRWgZa17VePuH9bDRYgAVgzUmQ66cN5Zs1DCAHnYJWoMWa66hKMbFos7xUUnZhHm08oemM3OUK2q6lx_ZYxTcBi1yEUHSeD59amb5Jb17zs9jNekFVSOrmCLzS0PhzxPqarXQjtVgg-fgJTw5uzONgFerEwRGAmr-mM7S3hK0h6Bl0mpwposi1ul3KwcYHBJG8nqyJIv2y7uUfp3YZd95jt5QGGhCQ7Owz4Wl1ZH7jcBbpHEE3-bNn8F3-ti6g6YlmXr0AKr2j7AYTIAzHig5YcBYYzUnrT7mXxpXS4mAcB_ntbKFsiaP8FsQgfq4iPnViWzK16oun3idhydw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f95f4785.mp4?token=vY-LqPRWgZa17VePuH9bDRYgAVgzUmQ66cN5Zs1DCAHnYJWoMWa66hKMbFos7xUUnZhHm08oemM3OUK2q6lx_ZYxTcBi1yEUHSeD59amb5Jb17zs9jNekFVSOrmCLzS0PhzxPqarXQjtVgg-fgJTw5uzONgFerEwRGAmr-mM7S3hK0h6Bl0mpwposi1ul3KwcYHBJG8nqyJIv2y7uUfp3YZd95jt5QGGhCQ7Owz4Wl1ZH7jcBbpHEE3-bNn8F3-ti6g6YlmXr0AKr2j7AYTIAzHig5YcBYYzUnrT7mXxpXS4mAcB_ntbKFsiaP8FsQgfq4iPnViWzK16oun3idhydw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش باران در حرم مطهر رضوی در آستانه عید غدیر
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/655760" target="_blank">📅 15:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655759">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ششمین سال خشکسالی در فلات مرکزی؛ کاهش ۳۹ درصدی بارش در تهران
رئیس مرکز مدیریت بحران خشکسالی سازمان هواشناسی:
🔹
استان‌های فلات مرکزی تا محدوده گیلان از جمله اصفهان، قم، مرکزی، تهران، قزوین، سمنان و گیلان در سال آبی جاری با بارش کمتر از حد نرمال مواجه شده‌اند.
🔹
در این میان تهران با ۳۹ درصد کاهش بارندگی بیشترین کم‌بارشی را ثبت کرده و پس از آن استان‌های مرکزی و قزوین با حدود ۳۰ درصد کاهش قرار دارند.
🔹
میزان کاهش بارش در گیلان نیز حدود ۲۵ درصد اعلام شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/655759" target="_blank">📅 15:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655758">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b44dad95ff.mp4?token=XU-kN1HG1RtgvGqJldc_kuf4L7ZdQuIdMGrTrvqw09ovVE6Bt0NKQU6SaIH0MBJoO9JiKj-1FvE1VgxnothQu0JksKpXU3lb0o8d0kImSSDsQVJPdJJNOwvwejHEprB235tn-l5Lga5atm4zaR_0bY8PewR92RgH3KGhZ32GqYww-kEEHKSC5u1pPde-mcBz1B-956k-13H4takONqmvKrXQKSCXT4VSh5-o4z993vk7CQwsWIMIb8yYqPaDgWRtJAPqQpzEbJBhxu1IzvdpsBeXttSansrVXwUKA_Tp4Eg7whubrfyh94Zw-gsnr-Dbj3hDa6PjklTYsAv8wGHvby2rESLZsXGrK-MC5AuvUvpvvfR51CwI705ytkG-dehrCIZAUnY1kjGSrZ2MOQrxfPm_ycMZ9pnMulEKG4rqErdnbyTF0DLw1xpNRGq_AF5OkadaUqDRWsV9bEznQCGGPRaAMJ-6oAPAq5ODYSw3vvOAAZyeiXDA6qVeBHtH4ygPR7_aK3k2WHhiCRxmXU4NyzwvLlvJxXcXGtwdums28Km3jQHXvA9URtAIiLhcxuW746Zj4aQOA50r9cW8WLPEavTA1Vxr1qPGRjqjhRFL7kg7BQcT3Mx1k6B3IPB7FAgZIRjvRksfhxMT1SabgYWRIxh_hzYkV4ew4Xmd5H53SPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b44dad95ff.mp4?token=XU-kN1HG1RtgvGqJldc_kuf4L7ZdQuIdMGrTrvqw09ovVE6Bt0NKQU6SaIH0MBJoO9JiKj-1FvE1VgxnothQu0JksKpXU3lb0o8d0kImSSDsQVJPdJJNOwvwejHEprB235tn-l5Lga5atm4zaR_0bY8PewR92RgH3KGhZ32GqYww-kEEHKSC5u1pPde-mcBz1B-956k-13H4takONqmvKrXQKSCXT4VSh5-o4z993vk7CQwsWIMIb8yYqPaDgWRtJAPqQpzEbJBhxu1IzvdpsBeXttSansrVXwUKA_Tp4Eg7whubrfyh94Zw-gsnr-Dbj3hDa6PjklTYsAv8wGHvby2rESLZsXGrK-MC5AuvUvpvvfR51CwI705ytkG-dehrCIZAUnY1kjGSrZ2MOQrxfPm_ycMZ9pnMulEKG4rqErdnbyTF0DLw1xpNRGq_AF5OkadaUqDRWsV9bEznQCGGPRaAMJ-6oAPAq5ODYSw3vvOAAZyeiXDA6qVeBHtH4ygPR7_aK3k2WHhiCRxmXU4NyzwvLlvJxXcXGtwdums28Km3jQHXvA9URtAIiLhcxuW746Zj4aQOA50r9cW8WLPEavTA1Vxr1qPGRjqjhRFL7kg7BQcT3Mx1k6B3IPB7FAgZIRjvRksfhxMT1SabgYWRIxh_hzYkV4ew4Xmd5H53SPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری شبکه افق: فردوسی‌پور و قیاسی چطور می‌توانند از تیم ملی فوتبال ایران صحبت کنند وقتی از کودکان ایرانی پرپرشده توسط آمریکا و اسرائیل حرفی نزدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/655758" target="_blank">📅 15:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655757">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76da5eaac.mp4?token=pGmFScU0c6a53_p7gYnBr50k1a6EgDxRqEvy2spJJYPEQdPl7r-__Qe7pAF-PegWwEqAZQFByJUR8hdRT40Er_aaQVSoc8hX6oZErjkzXoOG9Z9rNaKWKfrqY747adoIYhVPJfvMumzzetfkG6T-PdkIvERt6aW4LzvcsvOXBqjJLyps1xr0tZ0ZN9Hti-IGXBRzDzr9pERlOP4v2SDCC5rBshZwcU_Va01ACTbieloHUdixm2XnMqJvgdQf_BLpytSF2zEwq9HvrItSaoOvXVNxWkW_nvyS6c_vPhytWWb-9WWc7qZ5UkV3EG59Bl_AJgjdpSucu5PWWR_fcgJL_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76da5eaac.mp4?token=pGmFScU0c6a53_p7gYnBr50k1a6EgDxRqEvy2spJJYPEQdPl7r-__Qe7pAF-PegWwEqAZQFByJUR8hdRT40Er_aaQVSoc8hX6oZErjkzXoOG9Z9rNaKWKfrqY747adoIYhVPJfvMumzzetfkG6T-PdkIvERt6aW4LzvcsvOXBqjJLyps1xr0tZ0ZN9Hti-IGXBRzDzr9pERlOP4v2SDCC5rBshZwcU_Va01ACTbieloHUdixm2XnMqJvgdQf_BLpytSF2zEwq9HvrItSaoOvXVNxWkW_nvyS6c_vPhytWWb-9WWc7qZ5UkV3EG59Bl_AJgjdpSucu5PWWR_fcgJL_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت مردی در اربیل به‌دلیل ایجاد صدای شبیه پهپاد «شاهد»
🔹
پلیس اربیل در شمال عراق فردی را بازداشت کرد که با استفاده از یک بوق، صدایی شبیه به پهپادهای شاهد ایجاد می‌کرد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/655757" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655756">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
زمان شروع قطعی برق خانه‌ها مشخص شد
آرش نجفی، رئیس کمیسیون انرژی اتاق بازرگانی، صنایع، معادن و کشاورزی ایران:
🔹
پیش‌بینی می‌شود که این روند از اواخر خرداد یا اوایل تیرماه آغاز شود و مردم ایران احتمالاً به مدت سه ماه با این شرایط درگیر خواهند بود که در این مدت همراهی و همدلی همگانی ضروری است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/655756" target="_blank">📅 14:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655755">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f4873087b.mp4?token=aGphsp0W_t8gpPh4M27G-aLpbaOWYYkfjidOq93ihIu7FAAIrNdWi-xnfpw6OcG7vt_bmnVnDG4AboMLyHVQrhlSMBiw7cpoGH7c5CCe4CmVeFGlVuMiFSa-NVXTMHjSQ-HZmcHYplSJR-1vKsDY9d8kHzMMKPhf0z36iXMjM8HpSH0lrCTcFKPk8T6UTqeMf5wIxJXccXW4MmIjuxxQZj98KaMbKfwKZIrG68EJb8US2UQBe3cTaIkJsPhRTScYgiyXjRS4C45kNnB1efocij8ec9DHKs3UvdX8dDNzeGSz7HGivIn_nEXHqL_e-R-A_2YJLx13RZdpUIAGqzHg_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f4873087b.mp4?token=aGphsp0W_t8gpPh4M27G-aLpbaOWYYkfjidOq93ihIu7FAAIrNdWi-xnfpw6OcG7vt_bmnVnDG4AboMLyHVQrhlSMBiw7cpoGH7c5CCe4CmVeFGlVuMiFSa-NVXTMHjSQ-HZmcHYplSJR-1vKsDY9d8kHzMMKPhf0z36iXMjM8HpSH0lrCTcFKPk8T6UTqeMf5wIxJXccXW4MmIjuxxQZj98KaMbKfwKZIrG68EJb8US2UQBe3cTaIkJsPhRTScYgiyXjRS4C45kNnB1efocij8ec9DHKs3UvdX8dDNzeGSz7HGivIn_nEXHqL_e-R-A_2YJLx13RZdpUIAGqzHg_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب امام خمینی(ره) به تمجید آیت‌الله مشکینی از ایشان
🔹
ما آن قدری که گرفتار به نفس خودمان هستیم کافی است، دیگر مسائلی نفرمایید که انباشته بشود در نفوس ما و ما را به عقب برگرداند. شما دعا کنید که آدم بشویم. دعا کنید به ظواهر اسلام حداقل عمل کنیم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/655755" target="_blank">📅 14:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655754">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/956d48d0ad.mp4?token=QirUFzvENooH4oIRfYn-6XAdkPKiAf3wORDgozMoNHQ8wp4LP7bkgKJh0__89RAHR0y5hJWwZXSEBmSunMSgPziD64BXEp8oecCd7QHwqQQA_ovctrtqVqxwUuMWEmOm74iMz3v4LO6tvJlpqidPOlseeCM_GdJS9PX2gu-ZqXQNyDo5nBzNmIl8VKF1hxhTWEWvOZEdmSjD0xbj8TpcZIHA2KTm9JATc4QxU3TEdlaEocTO0EL3mHxRlhiQM5XTWlzJ9dwP0p6MAw7baEWkMgtNjpyV4ZkEZzK3j6MEFe5BtyVtp2i0ujxP4NZctdbycZ1ep8aUzP-fhwj6dN0Sxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/956d48d0ad.mp4?token=QirUFzvENooH4oIRfYn-6XAdkPKiAf3wORDgozMoNHQ8wp4LP7bkgKJh0__89RAHR0y5hJWwZXSEBmSunMSgPziD64BXEp8oecCd7QHwqQQA_ovctrtqVqxwUuMWEmOm74iMz3v4LO6tvJlpqidPOlseeCM_GdJS9PX2gu-ZqXQNyDo5nBzNmIl8VKF1hxhTWEWvOZEdmSjD0xbj8TpcZIHA2KTm9JATc4QxU3TEdlaEocTO0EL3mHxRlhiQM5XTWlzJ9dwP0p6MAw7baEWkMgtNjpyV4ZkEZzK3j6MEFe5BtyVtp2i0ujxP4NZctdbycZ1ep8aUzP-fhwj6dN0Sxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوق زده شدن داوران برنامه محفل از قرآن خوندن بامزه دختر بچه شیرین زبون
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/655754" target="_blank">📅 14:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655752">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
دقایقی پیش بارش فوق شدید و استوایی باران در شهرستان سلماس
#اخبار_اذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/655752" target="_blank">📅 14:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655751">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c63ec2e8.mp4?token=Wu6WEIxgSSvKVOBqqD9Pl3SYZHHVHp0VuqtSVwpAPjW5ywsRouAVon_Gmxu5VPPMX55pCi8kDlTn0mhzei18ze_IEXXgIFGP4MN8K_7Q2wUgYSjrui8Mth16h8FLvhvexfxHXQ03moasyuOgKAJSeNGDg1dSQew5qHcelJZU8CcAihOVXE8sSvwx2hkj1EWjlyV2R3y51gKZYSFKAYmXh7P3B3GjByuk0s6qIExe_jcfuPeTmy5QB2A9tbf6tAvwTrB7TBWt_M9ZD6zRt4WdL5Sj0hNqmnjkZjUKrF8up-TQH2895As_DbI0kHhs7RonZ5Isx6OHZiE5OTk9k59k6TKUQrbfcdTNrRLjwE0Mjg2NA4sl-AV0XK5Oes9AeseffwEqqj5UUfyxbybDZkGDzqDwb-0gaO1VHRDGSI7wIV5K4Gd6glAZxME_DsnXh6dxfEK8yGfAUcrpGdOIV3Gwb16Gz-gpzgLhoOnLZ4cCwr2Lt0niq-UT40Pa23HhHDC2ERBlOaY0-4w5ryMn5bzD-M-wgnl4Q5IQZXPdR-52S-awoS-PYyorWmVX0IZGQibWaAvIfBPQJtl6kd9GNN7C2comfTVUDxZtKICyR2QEEwcMKuJMmbwHYmlwtyEWAroiEHtdXTjXGSqqhKTiLKur9CD7mSBSPI3j79nVbtpl6ls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c63ec2e8.mp4?token=Wu6WEIxgSSvKVOBqqD9Pl3SYZHHVHp0VuqtSVwpAPjW5ywsRouAVon_Gmxu5VPPMX55pCi8kDlTn0mhzei18ze_IEXXgIFGP4MN8K_7Q2wUgYSjrui8Mth16h8FLvhvexfxHXQ03moasyuOgKAJSeNGDg1dSQew5qHcelJZU8CcAihOVXE8sSvwx2hkj1EWjlyV2R3y51gKZYSFKAYmXh7P3B3GjByuk0s6qIExe_jcfuPeTmy5QB2A9tbf6tAvwTrB7TBWt_M9ZD6zRt4WdL5Sj0hNqmnjkZjUKrF8up-TQH2895As_DbI0kHhs7RonZ5Isx6OHZiE5OTk9k59k6TKUQrbfcdTNrRLjwE0Mjg2NA4sl-AV0XK5Oes9AeseffwEqqj5UUfyxbybDZkGDzqDwb-0gaO1VHRDGSI7wIV5K4Gd6glAZxME_DsnXh6dxfEK8yGfAUcrpGdOIV3Gwb16Gz-gpzgLhoOnLZ4cCwr2Lt0niq-UT40Pa23HhHDC2ERBlOaY0-4w5ryMn5bzD-M-wgnl4Q5IQZXPdR-52S-awoS-PYyorWmVX0IZGQibWaAvIfBPQJtl6kd9GNN7C2comfTVUDxZtKICyR2QEEwcMKuJMmbwHYmlwtyEWAroiEHtdXTjXGSqqhKTiLKur9CD7mSBSPI3j79nVbtpl6ls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت این پرچم هزاران عشق نهفته‌‌است
❤️
#ایران_من
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/655751" target="_blank">📅 14:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655750">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
جراحی زیبایی به قیمت جان؛ مرگ دختر جوان در پی عمل بینی
🔹
دختر جوانی که از یکی از شهرستان‌های غرب کشور برای انجام عمل زیبایی بینی به تهران آمده و در یکی از بیمارستان های خصوصی بستری شده بود، شب گذشته جانش را از دست داد.
🔹
اولیای این دختر جوان ۲۷ ساله از کادر درمان شکایت کردند.
🔹
به دستور  بازپرس شعبه پنجم دادسرای جنایی، این پرونده به دادسرای ویژه جرائم پزشکی ارسال شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/655750" target="_blank">📅 14:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655749">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dd0d23fac.mp4?token=YdmGZ9JVjCgP6IwX_d2FUGjHGujPSRwsjKfpQfwFIM9ixuzrrmBp3ApaUoumeIpJwzDu1VVfTlcKfdWNA6y04Q60IwJNgCJDSS15d6-O5ENeHzeVGDuC2_YytVXDQPnpfAfhOPAZZoWQtzPNYD737O6O0NMwnU5fi9QBkp5lOyfNEFk3fZV4KgMDxpd4JJuVhEecF2Uy8hb4ml4PSEV4SV_kDVHJiQAqNeAMTw6apuP-BoYrE0dqs-gIyj8qwTszYKgonINYJXlugfbXgSLZazttoWsiSN_Tgq5Q-lGO7xJAkWxTEpbEnJmGJfOejB8b8tyX3p67mnrgFW1p365RBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dd0d23fac.mp4?token=YdmGZ9JVjCgP6IwX_d2FUGjHGujPSRwsjKfpQfwFIM9ixuzrrmBp3ApaUoumeIpJwzDu1VVfTlcKfdWNA6y04Q60IwJNgCJDSS15d6-O5ENeHzeVGDuC2_YytVXDQPnpfAfhOPAZZoWQtzPNYD737O6O0NMwnU5fi9QBkp5lOyfNEFk3fZV4KgMDxpd4JJuVhEecF2Uy8hb4ml4PSEV4SV_kDVHJiQAqNeAMTw6apuP-BoYrE0dqs-gIyj8qwTszYKgonINYJXlugfbXgSLZazttoWsiSN_Tgq5Q-lGO7xJAkWxTEpbEnJmGJfOejB8b8tyX3p67mnrgFW1p365RBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاهد وارد باشگاه شکارچیان لانچر شد
🔹
برای نخستین بار، نیروهای روسی یک لانچر پهپاد انتحاری (FP) اوکراینی را که روی یک کامیون نصب شده بود، با استفاده از پهپاد شاهد-۱۳۶ هدف قرار داده و منهدم کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/655749" target="_blank">📅 14:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655748">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ویدئویی از کویتی‌هایی که هنگام رانندگی سعی دارند از فعالیت پدافند هوایی فیلمبرداری کنند و با ماشین تصادف می‌کنند
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/655748" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655747">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b99f8f25c.mp4?token=h5l9q7-MPx7OBdv0W9CO6y3KybjxIJNUlBsxyOB5WtHEx4UhOyQCcMqVCIu_iAGMwX25C6vudCKx3B9Nk-8ivtAyQxFpIpPA64KLqJHHJN9bqRyQmoFDrbr1zzSqjrKOdEuM9TbDQAAB21NT72j_AkwGGf0-rttsiua2wRQ1df80rom3J5e-eDyfW_L_WrppMIyHEg7AOs_YRj5O_ultTq-bjTgiaSHwVq9I0zyM8WzgGvAUVTyzp6erxVaqxWVvnB-3sOs9RM0DF0a5noRmcmfXfIhnBrujdoqxQ6_WPT4puObFcLJyTMMETEE3jkDY5BGGh3u6zsqFFxqFoZ_Ikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b99f8f25c.mp4?token=h5l9q7-MPx7OBdv0W9CO6y3KybjxIJNUlBsxyOB5WtHEx4UhOyQCcMqVCIu_iAGMwX25C6vudCKx3B9Nk-8ivtAyQxFpIpPA64KLqJHHJN9bqRyQmoFDrbr1zzSqjrKOdEuM9TbDQAAB21NT72j_AkwGGf0-rttsiua2wRQ1df80rom3J5e-eDyfW_L_WrppMIyHEg7AOs_YRj5O_ultTq-bjTgiaSHwVq9I0zyM8WzgGvAUVTyzp6erxVaqxWVvnB-3sOs9RM0DF0a5noRmcmfXfIhnBrujdoqxQ6_WPT4puObFcLJyTMMETEE3jkDY5BGGh3u6zsqFFxqFoZ_Ikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: در حال حاضر نیازی به اعزام نیروی زمینی به ایران نداریم #Devil
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/655747" target="_blank">📅 14:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655746">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
سپاه: دشمن ناگزیر به پذیرش قواعد جدید ایران است
سپاه پاسداران در پیامی به مناسبت گرامیداشت سالروز رحلت امام خمینی (ره) و قیام ۱۵ خرداد:
🔹
حضور مردم در خیابان‌ها پشتیبان میدان رزم، سنگر دیپلماسی و عامل ضروری رقم خوردن پیروزی کامل و نهایی است.
🔹
ایرانیان هرگز تسلیم واژه‌سازی‌ها و دستاوردسازی‌های دروغین دشمن نخواهند شد.
🔹
دشمن ناگزیر به پذیرش قواعد جدیدی است که ملت ایران و نیروهای مسلح بر میدان تحمیل کرده‌اند؛ به ویژه در عرصه مدیریت و کنترل هوشمند تنگه هرمز.
🔹
مقاومت تا نابودی کامل توطئه‌های استکباری، اخراج بیگانگان از غرب آسیا و آزادی قدس شریف با نابودی رژیم صهیونیستی، مقتدرانه ادامه خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/655746" target="_blank">📅 14:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655745">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
تسنیم: مذاکرات تا زمانی که شروط ایران درباره لبنان تامین شود در حالت تعلیق می‌ماند
منابع آگاه:
🔹
طی روزهای گذشته ایران هیچ پاسخی به آمریکایی‌ها درباره متن تفاهم نداده و به دلیل جنایات رژیم صهیونیستی در لبنان، عملاً تبادل متن از طریق واسطه‌ها را نیز تا زمانی که شروط ایران درباره لبنان تامین شود، تعلیق کرده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/655745" target="_blank">📅 14:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655744">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ترامپ: نتانیاهو را «دیوانه لعنتی» خطاب کردم  نیویورک پست:
🔹
دونالد ترامپ تأیید کرد که در تماس تلفنی روز دوشنبه، بنیامین نتانیاهو را «دیوانهٔ لعنتی» خطاب کرده است.
🔹
او گفت از ادامه درگیری‌های نتانیاهو با لبنان ناراضی بوده و از او خواسته آتش‌بس کند. با این…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/655744" target="_blank">📅 14:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655743">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d85b392914.mp4?token=L2HiFtFRqDXwo5h2Bp0I4Pc7hyowGYv4L0w3OnTqP0f9pbW0WEGebwfYanUOw1rxAFtIi_isfu44i4qM1uQwr_dcpan-ASIBwjmPryMFcq4fV6D2MShk5pqCAw4qpv8i-_ir1L0642w5ARDvWZHnD-HCoChpPIPocQvlPAopVKNoZvpFkwkb_6OL3nVU2IRGojT5h6yg9NuNyHOUVZ956ZNzp9Vq8oW8kTd-9HnWgn8_bVhx9l1tj9iGAxLIpEHnkGjjz5ivCDJbKpq4HpLZJMi7h4soa-QHGyJhVJqtab4tn1VAzIWYretqjz4WWXSHmlCLTvrEaPmloFNuomqPCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d85b392914.mp4?token=L2HiFtFRqDXwo5h2Bp0I4Pc7hyowGYv4L0w3OnTqP0f9pbW0WEGebwfYanUOw1rxAFtIi_isfu44i4qM1uQwr_dcpan-ASIBwjmPryMFcq4fV6D2MShk5pqCAw4qpv8i-_ir1L0642w5ARDvWZHnD-HCoChpPIPocQvlPAopVKNoZvpFkwkb_6OL3nVU2IRGojT5h6yg9NuNyHOUVZ956ZNzp9Vq8oW8kTd-9HnWgn8_bVhx9l1tj9iGAxLIpEHnkGjjz5ivCDJbKpq4HpLZJMi7h4soa-QHGyJhVJqtab4tn1VAzIWYretqjz4WWXSHmlCLTvrEaPmloFNuomqPCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
هدف، هدف، ای مقصود من نجف
وطن کجاست، عقلا منطقا نجف...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/655743" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655742">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
تیزر قسمت ششم از فصل چهارم
🔹
در این قسمت روایت اولین تجربه نزدیک به مرگ آقای محمدعلی درودی که به خاطر شرایط سخت زندگی با پدر جانبازش و غم از دست دادن برادرش از زندگی ناامید شده و از خداوند طلب مرگ می کند به همین دلیل تجربه‌ای از جدا شدن روح از جسم توسط موجودی وحشتناک و رفتن به عالم برزخ و درک عمیقی از الطاف الهی را مشاهده و با ما در میان می گذارند
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: محمدعلی درودی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/655742" target="_blank">📅 14:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655741">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای اکسیوس: ترامپ به نتانیاهو گفت چه غلطی داری می‌کنی؟  خلاصه صحبت‌های ترامپ با نتانیاهو را این مقام آمریکایی چنین بیان کرد:
🔹
«تو دیوانه‌ای. اگر من نبودم، الان زندان بودی. دارم نجاتت می دهم. الان همه از تو متنفرند. به خاطر این قضیه، همه از اسرائیل متنفرند.»…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/655741" target="_blank">📅 14:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655740">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای ترامپ: اوضاع با ایران به سرعت در حال پیشرفت است و بسیار خوب خواهد شد
🔹
رهبر ایران در حال حاضر مشغول مذاکرات با ماست و ممکن است در مقطعی با او دیدار کنم.
🔹
ممکن است محاصره ایران تا روز کارگر برداشته شود. #Devil
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/655740" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655739">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNELvPfhAy3UVcPjEZje85YP8F-JreS0B-ZyD2kKPqFHYI_kFknji5lFcmdQ0ekzD5oKZJ_1cNMUdX559qVPVrJamQzo_ZoaMDM4myLhbsTelQkCE0ohPxA-_TVy1khylM4xODimLFUoqjB8GTLZFCqvnf-VsLNMQYybm0NtyvhzWYhBu12vaUHZYVcLJ1QFn8ZTsoYKXhZ6t2-KqRXqjJUSfmwnWl7r_U6Vf-DYYtdQ1nY8JHSpEygaKqLPk2sctx8CFqdncOqVFV3z-J5Sa4TYX5REA7U7gD2FODccxJwkDU9j3Skyse_w8RjA4zDMYd1JaEqcuNnHnCWk8Z1w-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست عجیب ترامپ: Trump 007
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/655739" target="_blank">📅 13:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655738">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdc7ddeec0.mp4?token=ade_LB_6mDYeEv5W6OwjLfnH4xcRLZNqd91LCaIDN5WBT6g-mtst1hVpERqPxIKkkxKn29ARU1wq-_4oUwreYIdq0wVcIIsuRRqTgpFY2IsUgyyl56V45eQqBoptqdNn-deJAFCVOWLHJ2h0-ck18o8WPIn2sA5CUtk85mzSwV-y8ncXpxjlex_QamFH-xZJLx37FC8VzaCMaJQck_N3wPiZ0SpLyNJkw67P09uyE8CLY708f71tlsGKun865iFM5N2S63-juvPHEbcVO3fYmNE2k0o9aleVt53Sj2A4d52Dcox8FCsnsUwGUH4jVhrYx0XjgnqH7Y2DOHX9ripRwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdc7ddeec0.mp4?token=ade_LB_6mDYeEv5W6OwjLfnH4xcRLZNqd91LCaIDN5WBT6g-mtst1hVpERqPxIKkkxKn29ARU1wq-_4oUwreYIdq0wVcIIsuRRqTgpFY2IsUgyyl56V45eQqBoptqdNn-deJAFCVOWLHJ2h0-ck18o8WPIn2sA5CUtk85mzSwV-y8ncXpxjlex_QamFH-xZJLx37FC8VzaCMaJQck_N3wPiZ0SpLyNJkw67P09uyE8CLY708f71tlsGKun865iFM5N2S63-juvPHEbcVO3fYmNE2k0o9aleVt53Sj2A4d52Dcox8FCsnsUwGUH4jVhrYx0XjgnqH7Y2DOHX9ripRwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ایران موافقت کرده است که سلاح هسته‌ای نداشته باشد #Devil
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/655738" target="_blank">📅 13:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655737">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb634c64b.mp4?token=VxAp0n4Y-7QXN7iFNupRm2JYccwWJf7KOigKT8v6dZQdL_ZJcMiLsgKzq--eKndW2gcGF68G6KZK92fgia51KfnfwzTOx1WXdqc1w5XqVjPH88Fpdpj0cz_yg3GkSabLx12n89D7VRkOYnaTgDZKhsmxUk2ivP1sE0BI_BEeo76GC0Y81kDSdnozjwkvjH-F2S9Sk41Wmu1Vf1M-4JCffyWlcYPE9d9I8caP2r8frN26cXmfjl2u8zG6tsZwYcCTIO9ctFsFGppLndBJ7SfbzXOO1f11DAB2ziIZgDQ6y53BCapPXnzjpCz-CJRvjyFpQSeswiwvB5pcd0YLJ97ozg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb634c64b.mp4?token=VxAp0n4Y-7QXN7iFNupRm2JYccwWJf7KOigKT8v6dZQdL_ZJcMiLsgKzq--eKndW2gcGF68G6KZK92fgia51KfnfwzTOx1WXdqc1w5XqVjPH88Fpdpj0cz_yg3GkSabLx12n89D7VRkOYnaTgDZKhsmxUk2ivP1sE0BI_BEeo76GC0Y81kDSdnozjwkvjH-F2S9Sk41Wmu1Vf1M-4JCffyWlcYPE9d9I8caP2r8frN26cXmfjl2u8zG6tsZwYcCTIO9ctFsFGppLndBJ7SfbzXOO1f11DAB2ziIZgDQ6y53BCapPXnzjpCz-CJRvjyFpQSeswiwvB5pcd0YLJ97ozg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع آتش سوزی مهیب در جنگل‌های اسپانیا
🔹
آتش سوزی بزرگ جنگلی در مورسیای اسپانیا، بیش از ۱۰۰ هکتار از جنگل های این منطقه را سوزانده و ساکنان را مجبور به تخلیه خانه های خود کرده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/655737" target="_blank">📅 13:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655736">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
عصائب اهل الحق عراق کمیته‌ای برای پایبندی به انحصار سلاح تشکیل داد
🔹
گروه عصائب اهل حق عراق از تشکیل یک کمیته مرکزی برای شروع اقدامات قطع ارتباط با حشد‌الشعبی و پایبندی به انحصار سلاح در دست دولت خبر داد.
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/655736" target="_blank">📅 13:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655735">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای
ترامپ: ایران موافقت کرده است که سلاح هسته‌ای نداشته باشد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/655735" target="_blank">📅 13:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655734">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyS-xo259qA_ce6qpwhwt8GlujbMuqorp1UyM4bAPdXBXaPNNpqbhEqdOTLhlWXBLafkwePoCheFgPHNujtbmj6L7FHiqW9jXPqSMZ8Wh-ka4mUAg8R-SIJhkbEYsLFyCnmZSJpOplY4Lb3Qigx-tchZK8yRdG5pwAB2ysrRf9qEwTPkZnjNSq4GmPeF7b-ZGoLmhC9bnJ8x-JhmY5XmFuurpG-J7K21EMzNxImBsJknGC3505rcw7gejeZTxvX0QgsYyJCq006ZDEWDIHKttZ5FFtiZ0MdiJisllYa1Njk5gdF76KGVCH_A1Y9CC3NUvoYqqlFcNlw64YA_BaHHsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس با رخت سبز به تعطیلات رفت
🔹
در جریان معاملات امروز شاخص کل بورس با افزایش ۱۴ هزار و ۳۷۴ واحد در سطح ۴ میلیون و ۳۵۸ هزار واحدی ایستاد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/655734" target="_blank">📅 13:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655733">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571a0fb2b2.mp4?token=Gw0b5Ix_8-Y2dkpigsQxI1ZSOBRqAnbyY4AzYoJ14oKtZvg3uYOm3hgIqdNYjr_iGSIMAC4qE8QwuO5YpdMg7RKgOzmInTx7lRv-l8wqWEFnmWeSI3Ng9KhXK0lfY8cyQT-Lj4Nfy83MCHhFdHJnJKbgvpajuaEP8w8n5Vu7JxO8q2a-ZxI7bYtetSdct-97xjj9SNgmaRit6H0gSy-SmFH5SZdEjlJznMwOtfdsx7UKjG7dFIHfUetfRH7z82NUUk1UViMSysOkIqJVmFkBZ7mfPLCY84j_oYIlBnJP9HsK_ikJ3cpVlLqHEt3mKeuh57BrAs1Y-NEzhCW1jOx5RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571a0fb2b2.mp4?token=Gw0b5Ix_8-Y2dkpigsQxI1ZSOBRqAnbyY4AzYoJ14oKtZvg3uYOm3hgIqdNYjr_iGSIMAC4qE8QwuO5YpdMg7RKgOzmInTx7lRv-l8wqWEFnmWeSI3Ng9KhXK0lfY8cyQT-Lj4Nfy83MCHhFdHJnJKbgvpajuaEP8w8n5Vu7JxO8q2a-ZxI7bYtetSdct-97xjj9SNgmaRit6H0gSy-SmFH5SZdEjlJznMwOtfdsx7UKjG7dFIHfUetfRH7z82NUUk1UViMSysOkIqJVmFkBZ7mfPLCY84j_oYIlBnJP9HsK_ikJ3cpVlLqHEt3mKeuh57BrAs1Y-NEzhCW1jOx5RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ شقایق نوروزی؛ فمینیست و فعال سیاسی ضدجنگ به ناامید شدن مجری ایران اینترنشنال از پهلوی و اپوزیسیون و آرزوی او برای حضور فردی شبیه جولانی در ایران: نگاه کن ببین ایران اصلا جولانی‌خیز هست یا نه؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/655733" target="_blank">📅 13:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655732">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سقوط بالگرد در جنوب غرب انگلیس
پلیس انگلیس:
🔹
یک بالگرد نیروی دریایی در مزرعه‌ای در جنوب غرب کشور سقوط کرده است.
🔹
جزئیات حادثه در دست بررسی است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/655732" target="_blank">📅 13:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655731">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd4306a5.mp4?token=HE-pdH0KoWWWzmPjFwduX8TOc_kNkOah1qpnQ-DATduRKVEiqOFNAauFOPsX6THSqKCmV3bstz0hbXlDGxILYf6WstbESq_xFxClU08k-6VcMYhAuvHdEJqMF7HyCyuPD-TtKQHV4rbfJgRF5Ak6pNI6hSkubp4DAgFyBnqKl-T2zYEbYg7pMYL3YOb3qRaNkwdMcjHqKf_ldk_d1E7kNPPu4rbrL_IOM7kmph_f3Pz1-seihB9yMopoBw5_EbhNCEnlw3zoa19LMh1w4AhCGQuwXfuAkxx7u7bHbeTLH0CWn86ShaTROQ2mycMzAX6GP5DjJTeYXFlNQ7cAVZGEKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd4306a5.mp4?token=HE-pdH0KoWWWzmPjFwduX8TOc_kNkOah1qpnQ-DATduRKVEiqOFNAauFOPsX6THSqKCmV3bstz0hbXlDGxILYf6WstbESq_xFxClU08k-6VcMYhAuvHdEJqMF7HyCyuPD-TtKQHV4rbfJgRF5Ak6pNI6hSkubp4DAgFyBnqKl-T2zYEbYg7pMYL3YOb3qRaNkwdMcjHqKf_ldk_d1E7kNPPu4rbrL_IOM7kmph_f3Pz1-seihB9yMopoBw5_EbhNCEnlw3zoa19LMh1w4AhCGQuwXfuAkxx7u7bHbeTLH0CWn86ShaTROQ2mycMzAX6GP5DjJTeYXFlNQ7cAVZGEKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدیده عجیب رعد و برق در کوهستان‌ مه‌آلود |گواتمالا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/655731" target="_blank">📅 13:11 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
